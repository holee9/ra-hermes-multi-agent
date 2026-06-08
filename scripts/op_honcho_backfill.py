#!/usr/bin/env python3
"""
OpenProject → Honcho Backfill Script (issue #18 SEED-1)

Extracts WP history from OpenProject and injects into Honcho `work` workspace
as session/message records for RA agent learning.

Mapping:
  WP ID                 → session.id = "wp-{id}"
  Subject + Description → first message (peer_id=human)
  Status transitions    → one message per transition (peer_id=human)
  Comments              → one message per comment (peer_id=human)

Usage:
  python3 scripts/op_honcho_backfill.py [--dry-run] [--project <id>] [--limit N]

Environment variables:
  OPENPROJECT_BASE_URL    - default: https://plm.abyz-lab.work
  OPENPROJECT_API_TOKEN   - required
  HONCHO_URL              - default: http://localhost:8000
  HONCHO_WORKSPACE        - default: work
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OP_BASE_URL = os.environ.get("OPENPROJECT_BASE_URL", "https://plm.abyz-lab.work")
OP_API_TOKEN = os.environ.get("OPENPROJECT_API_TOKEN", "")
HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WORKSPACE", "work")

PEER_ID_HUMAN = "human"

# ---------------------------------------------------------------------------
# OpenProject helpers
# ---------------------------------------------------------------------------


def op_auth() -> tuple[str, str]:
    return ("apikey", OP_API_TOKEN)


def op_get(path: str, params: dict = None, retries: int = 3) -> dict | None:
    url = f"{OP_BASE_URL}/api/v3{path}"
    for attempt in range(retries):
        try:
            resp = requests.get(url, auth=op_auth(), params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            if resp.status_code in (429, 503):
                time.sleep(2 ** attempt)
                continue
            print(f"  [warn] OP GET {path}: HTTP {resp.status_code}", flush=True)
            return None
        except requests.RequestException as exc:
            if attempt < retries - 1:
                time.sleep(1)
            else:
                print(f"  [warn] OP GET {path}: {exc}", flush=True)
    return None


def op_check_connection() -> bool:
    data = op_get("/users/me")
    if data:
        print(f"[op] Connected as: {data.get('login', '?')} / {data.get('name', '?')}", flush=True)
        return True
    print("[op] Connection failed — check OPENPROJECT_API_TOKEN", flush=True)
    return False


def op_list_projects() -> list[dict]:
    data = op_get("/projects", params={"pageSize": 100})
    if not data:
        return []
    return data.get("_embedded", {}).get("elements", [])


def op_list_work_packages(project_id: str | None, page_size: int = 100) -> list[dict]:
    """Paginate all WPs, optionally filtered by project."""
    results = []
    offset = 1
    while True:
        params: dict = {"pageSize": page_size, "offset": offset}
        if project_id:
            params["filters"] = json.dumps([{"project": {"operator": "=", "values": [str(project_id)]}}])
        data = op_get("/work_packages", params=params)
        if not data:
            break
        elements = data.get("_embedded", {}).get("elements", [])
        results.extend(elements)
        total = data.get("total", 0)
        if offset * page_size >= total:
            break
        offset += 1
    return results


def op_get_activities(wp_id: int) -> list[dict]:
    data = op_get(f"/work_packages/{wp_id}/activities")
    if not data:
        return []
    return data.get("_embedded", {}).get("elements", [])


# ---------------------------------------------------------------------------
# Honcho helpers
# ---------------------------------------------------------------------------


def honcho_post(path: str, body: dict, retries: int = 3) -> dict | None:
    url = f"{HONCHO_URL}{path}"
    for attempt in range(retries):
        try:
            resp = requests.post(url, json=body, timeout=30)
            if resp.status_code in (200, 201):
                return resp.json()
            if resp.status_code == 422:
                print(f"  [warn] Honcho POST {path}: 422 {resp.text[:200]}", flush=True)
                return None
            if resp.status_code in (429, 503):
                time.sleep(2 ** attempt)
                continue
            print(f"  [warn] Honcho POST {path}: HTTP {resp.status_code}", flush=True)
            return None
        except requests.RequestException as exc:
            if attempt < retries - 1:
                time.sleep(1)
            else:
                print(f"  [warn] Honcho POST {path}: {exc}", flush=True)
    return None


def honcho_session_exists(session_id: str) -> bool:
    url = f"{HONCHO_URL}/v3/workspaces/{HONCHO_WS}/sessions/{session_id}"
    try:
        resp = requests.get(url, timeout=10)
        return resp.status_code == 200
    except requests.RequestException:
        return False


def honcho_create_session(session_id: str, metadata: dict) -> bool:
    body = {"id": session_id, "metadata": metadata}
    result = honcho_post(f"/v3/workspaces/{HONCHO_WS}/sessions", body)
    return result is not None


def honcho_add_message(session_id: str, content: str, peer_id: str,
                       metadata: dict, created_at: str) -> bool:
    if not content or not content.strip():
        return False
    body = {
        "content": content[:25000],
        "peer_id": peer_id,
        "metadata": metadata,
        "created_at": created_at,
    }
    result = honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions/{session_id}/messages", body
    )
    return result is not None


# ---------------------------------------------------------------------------
# WP → Honcho conversion
# ---------------------------------------------------------------------------

def extract_region(wp: dict) -> str:
    """Try to extract region from WP custom fields or subject."""
    # Check custom_fields for region/규제권
    cfs = wp.get("customFields", {})
    for k, v in cfs.items():
        if isinstance(v, dict):
            raw = v.get("raw", "")
        else:
            raw = str(v)
        if raw in ("US", "EU", "KR"):
            return raw

    # Fallback: look for region keyword in subject
    subject = (wp.get("subject") or "").upper()
    for region in ("US", "EU", "KR"):
        if region in subject:
            return region
    return "UNKNOWN"


def wp_to_session_id(wp_id: int) -> str:
    return f"wp-{wp_id}"


def format_wp_first_message(wp: dict) -> str:
    subject = wp.get("subject", "(제목 없음)")
    desc = ""
    desc_raw = wp.get("description", {})
    if isinstance(desc_raw, dict):
        desc = desc_raw.get("raw", "") or desc_raw.get("html", "")
    elif isinstance(desc_raw, str):
        desc = desc_raw
    lines = [f"[WP] {subject}"]
    if desc.strip():
        lines.append("")
        lines.append(desc.strip()[:3000])
    return "\n".join(lines)


def activity_to_message(activity: dict, wp: dict) -> tuple[str, str] | None:
    """Return (content, created_at) or None if activity should be skipped."""
    activity_type = activity.get("_type", "")
    created_at = activity.get("createdAt", "")

    if activity_type == "Activity::Comment":
        comment_raw = activity.get("comment", {})
        if isinstance(comment_raw, dict):
            text = comment_raw.get("raw", "") or comment_raw.get("html", "")
        else:
            text = str(comment_raw)
        if not text.strip():
            return None
        author = activity.get("user", {})
        author_name = author.get("name", "?") if isinstance(author, dict) else "?"
        content = f"[코멘트] {author_name}\n{text.strip()[:3000]}"
        return content, created_at

    if activity_type == "Activity::AttributeChange" or "details" in activity:
        details = activity.get("details", [])
        lines = []
        for detail in details:
            attr = detail.get("attribute", "")
            old_val = detail.get("oldValue", "")
            new_val = detail.get("newValue", "")
            if attr and (old_val or new_val):
                lines.append(f"  {attr}: {old_val!r} → {new_val!r}")
        if not lines:
            return None
        author = activity.get("user", {})
        author_name = author.get("name", "?") if isinstance(author, dict) else "?"
        content = f"[상태변경] {author_name}\n" + "\n".join(lines)
        return content, created_at

    return None


# ---------------------------------------------------------------------------
# Backfill one WP
# ---------------------------------------------------------------------------

def backfill_wp(wp: dict, dry_run: bool) -> dict:
    wp_id = wp.get("id")
    session_id = wp_to_session_id(wp_id)
    subject = wp.get("subject", "")

    region = extract_region(wp)
    status = (wp.get("status", {}) or {}).get("title", "?") if isinstance(wp.get("status"), dict) else "?"
    project_name = ""
    if isinstance(wp.get("_links"), dict):
        proj = wp["_links"].get("project", {})
        project_name = proj.get("title", "") if isinstance(proj, dict) else ""

    created_at = wp.get("createdAt", datetime.now(timezone.utc).isoformat())
    updated_at = wp.get("updatedAt", created_at)

    metadata = {
        "region": region,
        "status": status,
        "project": project_name,
        "wp_subject": subject,
        "wp_updated_at": updated_at,
        "source": "openproject_backfill",
    }

    messages_added = 0

    if dry_run:
        print(f"  [dry] session={session_id} region={region} subject={subject[:60]}", flush=True)
    else:
        if honcho_session_exists(session_id):
            print(f"  [skip] {session_id} already exists", flush=True)
            return {"skipped": True, "session_id": session_id}

        if not honcho_create_session(session_id, metadata):
            print(f"  [error] Failed to create session {session_id}", flush=True)
            return {"error": True, "session_id": session_id}

        # First message: subject + description
        first_content = format_wp_first_message(wp)
        if honcho_add_message(session_id, first_content, PEER_ID_HUMAN,
                              {"type": "wp_initial", "wp_id": wp_id}, created_at):
            messages_added += 1

    # Activities (comments + transitions)
    activities = op_get_activities(wp_id) or []
    for activity in activities:
        result = activity_to_message(activity, wp)
        if result is None:
            continue
        content, act_created_at = result
        if dry_run:
            print(f"    [dry] message: {content[:60]!r}", flush=True)
        else:
            act_meta = {
                "type": activity.get("_type", "activity"),
                "wp_id": wp_id,
            }
            if honcho_add_message(session_id, content, PEER_ID_HUMAN,
                                  act_meta, act_created_at):
                messages_added += 1

    return {
        "session_id": session_id,
        "messages_added": messages_added,
        "activities": len(activities),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Backfill OpenProject WP history into Honcho work workspace."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would happen without writing to Honcho.")
    parser.add_argument("--project", default=None,
                        help="OpenProject project ID to filter (default: all).")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max WPs to process (0 = all).")
    args = parser.parse_args()

    if not OP_API_TOKEN:
        print("[error] OPENPROJECT_API_TOKEN not set. See /opt/hermes-ra/.env", flush=True)
        sys.exit(1)

    print("=" * 60, flush=True)
    print("OpenProject → Honcho Backfill", flush=True)
    print(f"OP URL   : {OP_BASE_URL}", flush=True)
    print(f"Honcho   : {HONCHO_URL}  ws={HONCHO_WS}", flush=True)
    print(f"Dry-run  : {args.dry_run}", flush=True)
    print("=" * 60, flush=True)

    if not op_check_connection():
        sys.exit(1)

    print("[op] Listing work packages ...", flush=True)
    wps = op_list_work_packages(args.project)
    print(f"[op] Found {len(wps)} WPs", flush=True)

    if args.limit > 0:
        wps = wps[: args.limit]
        print(f"[op] Limiting to {args.limit} WPs", flush=True)

    total_sessions = 0
    total_messages = 0
    skipped = 0
    errors = 0

    for i, wp in enumerate(wps):
        wp_id = wp.get("id")
        subject = wp.get("subject", "")
        print(f"\n[{i+1}/{len(wps)}] WP-{wp_id}: {subject[:60]}", flush=True)

        result = backfill_wp(wp, args.dry_run)

        if result.get("skipped"):
            skipped += 1
        elif result.get("error"):
            errors += 1
        else:
            total_sessions += 1
            total_messages += result.get("messages_added", 0)

        # Brief pause to avoid overwhelming Honcho
        if not args.dry_run:
            time.sleep(0.05)

    print("\n" + "=" * 60, flush=True)
    print(f"Done. sessions_created={total_sessions}, messages_added={total_messages}, "
          f"skipped={skipped}, errors={errors}", flush=True)
    print("=" * 60, flush=True)


if __name__ == "__main__":
    main()
