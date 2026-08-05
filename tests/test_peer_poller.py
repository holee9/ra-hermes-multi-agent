"""Unit tests for scripts/peer-comment-poller.py (SPEC-DEVCOMM-001 M2).

Covers REQ-DC-003 logic without touching real GitHub or the live server:
  - gh api invocation shape (absolute /usr/bin/gh, since=<last_seen>, per_page=100)
  - self-author filtering (holee9 comments never nudged — anti-loop)
  - nudge payload build (4-field schema, issue parsed from issue_url)
  - last_seen state: default when missing, updated only after full success,
    NOT updated on post failure or dry-run
  - --dry-run: no POST, no state write
  - fail-closed (C4/C5): missing API_SERVER_KEY -> non-zero exit, no action
"""
import importlib.util
import json
from pathlib import Path

import pytest

_POLLER = Path(__file__).resolve().parent.parent / "scripts" / "peer-comment-poller.py"


def _load():
    spec = importlib.util.spec_from_file_location("peer_comment_poller", _POLLER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


p = _load()

SELF = "holee9"
PEER_COMMENT = {
    "html_url": "https://github.com/holee9/ra-hermes-multi-agent/issues/141#issuecomment-200",
    "issue_url": "https://api.github.com/repos/holee9/ra-hermes-multi-agent/issues/141",
    "user": {"login": "hnabyz-bot"},
    "created_at": "2026-08-05T01:00:00Z",
    "updated_at": "2026-08-05T01:00:00Z",
}
SELF_COMMENT = {
    "html_url": "https://github.com/holee9/ra-hermes-multi-agent/issues/141#issuecomment-201",
    "issue_url": "https://api.github.com/repos/holee9/ra-hermes-multi-agent/issues/141",
    "user": {"login": SELF},
    "created_at": "2026-08-05T02:00:00Z",
    "updated_at": "2026-08-05T02:30:00Z",
}


@pytest.fixture()
def env(monkeypatch, tmp_path):
    """Isolated poller environment: tmp state file, fake key, quiet logs."""
    state_path = tmp_path / "peer-poll-state.json"
    monkeypatch.setattr(p, "POLL_STATE", str(state_path))
    monkeypatch.setattr(p, "API_KEY", "test-key")
    monkeypatch.setattr(p, "SELF_LOGIN", SELF)
    return state_path


# ── filtering (anti-loop) ─────────────────────────────────────────────────
def test_filter_excludes_self_comments():
    kept = p.filter_comments([PEER_COMMENT, SELF_COMMENT], SELF)
    assert kept == [PEER_COMMENT]


def test_filter_tolerates_missing_user():
    assert p.filter_comments([{"html_url": "x"}], SELF) == []


# ── nudge payload (frozen 4-field schema) ─────────────────────────────────
def test_build_nudge_shape():
    nudge = p.build_nudge(PEER_COMMENT)
    assert nudge == {
        "issue": 141,
        "comment_url": PEER_COMMENT["html_url"],
        "author": "hnabyz-bot",
        "ts": "2026-08-05T01:00:00Z",
    }
    assert isinstance(nudge["issue"], int)


# ── gh subprocess invocation ──────────────────────────────────────────────
def test_fetch_comments_invokes_gh_with_since(monkeypatch):
    captured = {}

    class _Result:
        returncode = 0
        stdout = json.dumps([PEER_COMMENT])
        stderr = ""

    def _fake_run(argv, **kwargs):
        captured["argv"] = argv
        return _Result()

    monkeypatch.setattr(p.subprocess, "run", _fake_run)
    comments = p.fetch_comments("holee9/ra-hermes-multi-agent", "2026-08-05T00:00:00Z")
    assert comments == [PEER_COMMENT]
    assert captured["argv"][0] == "/usr/bin/gh"
    assert captured["argv"][1] == "api"
    assert "since=2026-08-05T00:00:00Z" in captured["argv"][2]
    assert "per_page=100" in captured["argv"][2]
    assert "repos/holee9/ra-hermes-multi-agent/issues/comments" in captured["argv"][2]


def test_fetch_comments_nonzero_exit_raises(monkeypatch):
    class _Result:
        returncode = 1
        stdout = ""
        stderr = "gh: HTTP 401"

    monkeypatch.setattr(p.subprocess, "run", lambda *a, **k: _Result())
    with pytest.raises(RuntimeError):
        p.fetch_comments("holee9/ra-hermes-multi-agent", "2026-08-05T00:00:00Z")


# ── state handling ────────────────────────────────────────────────────────
def test_state_roundtrip(env):
    p.save_state({"last_seen": "2026-08-05T03:00:00Z"})
    assert p.load_state() == {"last_seen": "2026-08-05T03:00:00Z"}


def test_load_state_missing_file_is_empty(env):
    assert p.load_state() == {}


def test_compute_new_last_seen_uses_max_updated_at():
    out = p.compute_new_last_seen([PEER_COMMENT, SELF_COMMENT], "2026-08-05T00:00:00Z")
    assert out == "2026-08-05T02:30:00Z"


def test_compute_new_last_seen_no_comments_keeps_previous():
    assert p.compute_new_last_seen([], "2026-08-05T00:00:00Z") == "2026-08-05T00:00:00Z"


# ── run(): normal flow ────────────────────────────────────────────────────
def test_run_posts_peer_comments_and_updates_state(env, monkeypatch):
    p.save_state({"last_seen": "2026-08-05T00:00:00Z"})  # cursor before fixture ts
    posted = []
    monkeypatch.setattr(p, "fetch_comments", lambda repo, since: [PEER_COMMENT, SELF_COMMENT])
    monkeypatch.setattr(p, "post_nudge", lambda n: posted.append(n) or {"status": "accepted"})
    assert p.run(dry_run=False) == 0
    assert len(posted) == 1
    assert posted[0]["author"] == "hnabyz-bot"
    assert p.load_state()["last_seen"] == "2026-08-05T02:30:00Z"


def test_run_no_new_comments_is_noop_success(env, monkeypatch):
    p.save_state({"last_seen": "2026-08-05T00:00:00Z"})
    monkeypatch.setattr(p, "fetch_comments", lambda repo, since: [])
    monkeypatch.setattr(p, "post_nudge", lambda n: pytest.fail("must not post"))
    assert p.run(dry_run=False) == 0
    assert p.load_state()["last_seen"] == "2026-08-05T00:00:00Z"


# ── run(): --dry-run ──────────────────────────────────────────────────────
def test_dry_run_no_post_no_state_update(env, monkeypatch):
    monkeypatch.setattr(p, "fetch_comments", lambda repo, since: [PEER_COMMENT])
    monkeypatch.setattr(p, "post_nudge", lambda n: pytest.fail("dry-run must not POST"))
    assert p.run(dry_run=True) == 0
    assert not Path(env).exists()  # state file never written


# ── run(): failure paths (fail-closed C4) ─────────────────────────────────
def test_run_post_failure_exits_nonzero_and_keeps_state(env, monkeypatch):
    p.save_state({"last_seen": "2026-08-05T00:00:00Z"})

    def _boom(nudge):
        raise RuntimeError("connection refused")

    monkeypatch.setattr(p, "fetch_comments", lambda repo, since: [PEER_COMMENT])
    monkeypatch.setattr(p, "post_nudge", _boom)
    assert p.run(dry_run=False) != 0
    # last_seen NOT advanced -> next timer run retries; server dedup absorbs overlap
    assert p.load_state()["last_seen"] == "2026-08-05T00:00:00Z"


def test_run_fetch_failure_exits_nonzero(env, monkeypatch):
    def _boom(repo, since):
        raise RuntimeError("gh api failed")

    monkeypatch.setattr(p, "fetch_comments", _boom)
    assert p.run(dry_run=False) != 0


def test_run_without_api_key_exits_nonzero(env, monkeypatch):
    monkeypatch.setattr(p, "API_KEY", "")
    monkeypatch.setattr(p, "fetch_comments", lambda repo, since: pytest.fail("must not fetch"))
    assert p.run(dry_run=False) != 0


def test_dry_run_allowed_without_api_key(env, monkeypatch):
    monkeypatch.setattr(p, "API_KEY", "")
    monkeypatch.setattr(p, "fetch_comments", lambda repo, since: [])
    assert p.run(dry_run=True) == 0


# ── post retry ceiling ────────────────────────────────────────────────────
def test_post_nudge_retries_at_most_three_times(env, monkeypatch):
    attempts = []

    def _always_fail(req, timeout=None):
        attempts.append(1)
        raise OSError("refused")

    monkeypatch.setattr(p.urllib.request, "urlopen", _always_fail)
    monkeypatch.setattr(p.time, "sleep", lambda s: None)
    with pytest.raises(RuntimeError):
        p.post_nudge(p.build_nudge(PEER_COMMENT))
    assert len(attempts) == 3
