"""Unit tests for POST /v1/peer/notify (scripts/hermes-api-server.py).

SPEC-DEVCOMM-001 M1 (REQ-DC-001, REQ-DC-002, AC-1, AC-2):
  - Bearer auth reuse (check_auth): no/bad token -> 401
  - 4-field schema validation ({issue:int, comment_url:str, author:str, ts:str}) -> 400
  - valid nudge -> 200 + peer_comment event log line ({ts,type,actor,payload})
  - comment_url dedup: second delivery -> 200 {"status":"duplicate"}, single processing
  - dedup persistence: file survives restart, capped at ~500 entries
  - Honcho independence (C2): the notify path never calls _honcho_record
"""
import importlib.util
import json
from pathlib import Path

import pytest

_SERVER = Path(__file__).resolve().parent.parent / "scripts" / "hermes-api-server.py"


def _load():
    spec = importlib.util.spec_from_file_location("hermes_api_server_peer", _SERVER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = _load()

TEST_KEY = "test-peer-key"
VALID_NUDGE = {
    "issue": 141,
    "comment_url": "https://github.com/holee9/ra-hermes-multi-agent/issues/141#issuecomment-1",
    "author": "hnabyz-bot",
    "ts": "2026-08-05T00:00:00Z",
}


@pytest.fixture()
def client(monkeypatch, tmp_path):
    """Isolated Flask test client: known API key, tmp dedup state, captured event log."""
    monkeypatch.setattr(m, "API_KEY", TEST_KEY)
    monkeypatch.setattr(m, "PEER_NOTIFY_STATE", str(tmp_path / "peer-notify-seen.json"))
    m._peer_seen.clear()
    m._peer_seen_order.clear()
    logged = []
    monkeypatch.setattr(m._peer_notify_logger, "info", lambda msg: logged.append(msg))
    c = m.app.test_client()
    c.logged = logged
    yield c


def _post(client, payload, key=TEST_KEY):
    headers = {"Authorization": f"Bearer {key}"} if key else {}
    return client.post("/v1/peer/notify", json=payload, headers=headers)


# ── AC-1: auth ────────────────────────────────────────────────────────────
def test_notify_without_auth_is_401(client):
    resp = client.post("/v1/peer/notify", json=VALID_NUDGE)
    assert resp.status_code == 401
    assert resp.get_json()["error"] == "Unauthorized"


def test_notify_wrong_key_is_401(client):
    resp = _post(client, VALID_NUDGE, key="wrong-key")
    assert resp.status_code == 401


# ── AC-1: accepted nudge ──────────────────────────────────────────────────
def test_notify_valid_payload_is_200_accepted(client):
    resp = _post(client, VALID_NUDGE)
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["status"] == "accepted"
    assert body["comment_url"] == VALID_NUDGE["comment_url"]


def test_notify_logs_frozen_event_contract(client):
    # REQ-DC-002: event record follows {ts, type, actor, payload} (C2: log-only,
    # never Honcho — the only live VO feed is the Honcho adapter, forbidden here).
    _post(client, VALID_NUDGE)
    assert len(client.logged) == 1
    event = json.loads(client.logged[0])
    assert set(event) == {"ts", "type", "actor", "payload"}
    assert event["type"] == "peer_comment"
    assert event["actor"] == "hnabyz-bot"
    assert event["payload"]["issue"] == 141
    assert event["payload"]["comment_url"] == VALID_NUDGE["comment_url"]


def test_notify_never_records_to_honcho(client, monkeypatch):
    # C2 hard constraint: this channel is Honcho-independent.
    calls = []
    monkeypatch.setattr(m, "_honcho_record", lambda *a, **k: calls.append(a))
    _post(client, VALID_NUDGE)
    assert calls == []


# ── AC-1: schema validation ───────────────────────────────────────────────
@pytest.mark.parametrize("missing", ["issue", "comment_url", "author", "ts"])
def test_notify_missing_field_is_400(client, missing):
    payload = {k: v for k, v in VALID_NUDGE.items() if k != missing}
    resp = _post(client, payload)
    assert resp.status_code == 400
    assert "error" in resp.get_json()


@pytest.mark.parametrize("bad_issue", ["141", 1.5, None, True])
def test_notify_non_int_issue_is_400(client, bad_issue):
    resp = _post(client, {**VALID_NUDGE, "issue": bad_issue})
    assert resp.status_code == 400


@pytest.mark.parametrize("field", ["comment_url", "author", "ts"])
def test_notify_empty_string_field_is_400(client, field):
    resp = _post(client, {**VALID_NUDGE, field: "  "})
    assert resp.status_code == 400


def test_notify_non_json_body_is_400(client):
    resp = client.post(
        "/v1/peer/notify", data="not json",
        headers={"Authorization": f"Bearer {TEST_KEY}", "Content-Type": "text/plain"},
    )
    assert resp.status_code == 400


# ── AC-2: dedup — same comment_url processed once ─────────────────────────
def test_duplicate_comment_url_processed_once(client):
    first = _post(client, VALID_NUDGE)
    second = _post(client, VALID_NUDGE)
    assert first.get_json()["status"] == "accepted"
    assert second.status_code == 200
    assert second.get_json()["status"] == "duplicate"
    assert len(client.logged) == 1  # event emitted exactly once


def test_distinct_comment_urls_both_processed(client):
    _post(client, VALID_NUDGE)
    other = {**VALID_NUDGE, "comment_url": VALID_NUDGE["comment_url"] + "0"}
    resp = _post(client, other)
    assert resp.get_json()["status"] == "accepted"
    assert len(client.logged) == 2


# ── dedup persistence (restart survival + ~500 cap) ───────────────────────
def test_seen_state_persists_to_file_and_reloads(client):
    _post(client, VALID_NUDGE)
    state = json.loads(Path(m.PEER_NOTIFY_STATE).read_text())
    assert VALID_NUDGE["comment_url"] in state
    # simulate service restart: clear memory, reload from file
    m._peer_seen.clear()
    m._peer_seen_order.clear()
    m._peer_seen_load()
    resp = _post(client, VALID_NUDGE)
    assert resp.get_json()["status"] == "duplicate"


def test_seen_state_keeps_last_500_entries(client):
    for i in range(510):
        m._peer_seen_add(f"https://example.com/c/{i}")
    state = json.loads(Path(m.PEER_NOTIFY_STATE).read_text())
    assert len(state) == 500
    assert state[0] == "https://example.com/c/10"   # oldest 10 dropped
    assert state[-1] == "https://example.com/c/509"
    assert "https://example.com/c/9" not in m._peer_seen


def test_seen_load_tolerates_missing_and_corrupt_file(client):
    m._peer_seen_load()  # file absent -> no raise
    Path(m.PEER_NOTIFY_STATE).write_text("{corrupt")
    m._peer_seen_load()  # corrupt file -> no raise
    assert _post(client, VALID_NUDGE).get_json()["status"] == "accepted"
