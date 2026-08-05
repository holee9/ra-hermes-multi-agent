#!/usr/bin/env python3
"""peer-comment-poller.py — GitHub issue-comment polling backstop (SPEC-DEVCOMM-001 M2).

Layer 2 of the T3610<->raspi5p comms channel: every 5 minutes (systemd timer
hermes-peer-poll.timer) fetch issue comments updated since last_seen, drop
comments authored by our own account (anti-loop), and POST each remaining
comment as a nudge to the local /v1/peer/notify endpoint (REQ-DC-003). The
endpoint dedups on comment_url, so push/poll overlap is safe (AC-2).

Fail-closed (C4): any failure logs and exits non-zero — the poller never
triggers any other action, and last_seen is only advanced after a fully
successful run (the next timer run re-fetches; server dedup absorbs overlap).

Config (env, via scripts/.env — no hardcoded URLs/tokens, C5):
  PEER_POLL_REPO          repo to poll        (default holee9/ra-hermes-multi-agent)
  PEER_POLL_SELF_LOGIN    own GitHub login    (default holee9)
  PEER_POLL_STATE         last_seen state file (default ~/.hermes/peer-poll-state.json)
  PEER_NOTIFY_LOCAL_URL   local notify URL    (default http://localhost:8643/v1/peer/notify)
  API_SERVER_KEY          Bearer key for the notify endpoint (required unless --dry-run)
  GH_BIN                  gh binary           (default /usr/bin/gh — absolute path required)

Usage:
  python3 scripts/peer-comment-poller.py [--dry-run]
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

GH_BIN = os.environ.get("GH_BIN", "/usr/bin/gh")
POLL_REPO = os.environ.get("PEER_POLL_REPO", "holee9/ra-hermes-multi-agent")
SELF_LOGIN = os.environ.get("PEER_POLL_SELF_LOGIN", "holee9")
POLL_STATE = os.environ.get(
    "PEER_POLL_STATE", os.path.expanduser("~/.hermes/peer-poll-state.json"))
NOTIFY_URL = os.environ.get(
    "PEER_NOTIFY_LOCAL_URL", "http://localhost:8643/v1/peer/notify")
API_KEY = os.environ.get("API_SERVER_KEY", "")
GH_TIMEOUT = int(os.environ.get("PEER_POLL_GH_TIMEOUT", "60"))
POST_TIMEOUT = int(os.environ.get("PEER_POLL_POST_TIMEOUT", "10"))
MAX_POST_RETRIES = 3  # hard ceiling — no retries beyond 3 (fail-closed C4)
FIRST_RUN_LOOKBACK_SECONDS = 3600  # bounded backfill when no state file exists


def _log(event: str, stream=sys.stdout, **fields) -> None:
    """One JSON line per event; systemd journal captures stdout/stderr."""
    record = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "event": event}
    record.update(fields)
    print(json.dumps(record, ensure_ascii=False), file=stream, flush=True)


def load_state() -> dict:
    """Read {last_seen: iso8601} from POLL_STATE. Missing/corrupt file -> {}."""
    try:
        with open(POLL_STATE) as f:
            state = json.load(f)
        return state if isinstance(state, dict) else {}
    except (OSError, ValueError):
        return {}


def save_state(state: dict) -> None:
    state_dir = os.path.dirname(POLL_STATE)
    if state_dir:
        os.makedirs(state_dir, exist_ok=True)
    with open(POLL_STATE, "w") as f:
        json.dump(state, f)


def _default_last_seen() -> str:
    """First run without state: look back one hour, not the whole issue history."""
    return time.strftime(
        "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - FIRST_RUN_LOOKBACK_SECONDS))


def fetch_comments(repo: str, since: str) -> list:
    """List issue comments updated since <since> via gh api (repo-wide endpoint)."""
    endpoint = f"repos/{repo}/issues/comments?since={since}&per_page=100"
    result = subprocess.run(
        [GH_BIN, "api", endpoint], capture_output=True, text=True, timeout=GH_TIMEOUT)
    if result.returncode != 0:
        raise RuntimeError(
            f"gh api exit {result.returncode}: {result.stderr.strip()[:500]}")
    data = json.loads(result.stdout)
    if not isinstance(data, list):
        raise RuntimeError("unexpected gh api response shape (expected list)")
    return data


def filter_comments(comments: list, self_login: str) -> list:
    """Keep only comments authored by someone other than our own account."""
    kept = []
    for c in comments:
        login = (c.get("user") or {}).get("login")
        if login and login != self_login:
            kept.append(c)
    return kept


def build_nudge(comment: dict) -> dict:
    """Map a GitHub comment to the frozen 4-field nudge schema (spec section 3)."""
    issue = int(comment["issue_url"].rstrip("/").rsplit("/", 1)[-1])
    return {
        "issue": issue,
        "comment_url": comment["html_url"],
        "author": comment["user"]["login"],
        "ts": comment["created_at"],
    }


def post_nudge(nudge: dict) -> dict:
    """POST the nudge to the local notify endpoint. At most MAX_POST_RETRIES tries."""
    body = json.dumps(nudge).encode("utf-8")
    last_err = None
    for attempt in range(1, MAX_POST_RETRIES + 1):
        try:
            req = urllib.request.Request(
                NOTIFY_URL,
                data=body,
                method="POST",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {API_KEY}",
                },
            )
            with urllib.request.urlopen(req, timeout=POST_TIMEOUT) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as exc:  # network/HTTP/JSON — all retried within ceiling
            last_err = exc
            if attempt < MAX_POST_RETRIES:
                time.sleep(1)
    raise RuntimeError(f"post failed after {MAX_POST_RETRIES} attempts: {last_err}")


def compute_new_last_seen(comments: list, previous: str) -> str:
    """Max updated_at (fallback created_at) across ALL fetched comments.

    Self-authored comments also advance the cursor — they never need
    reprocessing. ISO-8601 Z timestamps compare correctly as strings.
    """
    latest = previous
    for c in comments:
        ts = c.get("updated_at") or c.get("created_at") or ""
        if ts > latest:
            latest = ts
    return latest


def run(dry_run: bool = False) -> int:
    if not dry_run and not API_KEY:
        _log("error", stream=sys.stderr,
             reason="API_SERVER_KEY not set — cannot post nudges (fail-closed)")
        return 2

    state = load_state()
    last_seen = state.get("last_seen") or _default_last_seen()

    try:
        comments = fetch_comments(POLL_REPO, last_seen)
    except Exception as exc:
        _log("error", stream=sys.stderr, stage="fetch", detail=str(exc))
        return 2

    peers = filter_comments(comments, SELF_LOGIN)

    if dry_run:
        for c in peers:
            _log("dry-run-nudge", nudge=build_nudge(c))
        _log("dry-run-summary", repo=POLL_REPO, since=last_seen,
             fetched=len(comments), would_post=len(peers))
        return 0

    failures = 0
    for c in peers:
        nudge = build_nudge(c)
        try:
            resp = post_nudge(nudge)
            _log("posted", comment_url=nudge["comment_url"],
                 server_status=resp.get("status"))
        except Exception as exc:
            failures += 1
            _log("error", stream=sys.stderr, stage="post",
                 comment_url=nudge["comment_url"], detail=str(exc))

    if failures:
        # last_seen NOT advanced: the next timer run re-fetches the same window
        # and the server-side comment_url dedup absorbs the overlap (C4).
        _log("error", stream=sys.stderr, stage="summary",
             failures=failures, posted=len(peers) - failures)
        return 2

    new_last_seen = compute_new_last_seen(comments, last_seen)
    if new_last_seen != last_seen:
        save_state({"last_seen": new_last_seen})
    _log("ok", repo=POLL_REPO, since=last_seen, fetched=len(comments),
         posted=len(peers), last_seen=new_last_seen)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Poll GitHub issue comments and nudge the local peer channel")
    parser.add_argument("--dry-run", action="store_true",
                        help="print what would be sent; no POST, no state update")
    args = parser.parse_args()
    return run(dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
