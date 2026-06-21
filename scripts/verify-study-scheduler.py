#!/usr/bin/env python3
"""Regression checks for autonomous-study-scheduler.py.

The checks are intentionally local-only: they import the scheduler, monkeypatch Honcho
writes, and assert that peer IDs and message content obey the frozen data contract.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import SimpleNamespace
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEDULER = ROOT / "scripts" / "autonomous-study-scheduler.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_scheduler() -> Any:
    spec = importlib.util.spec_from_file_location("autonomous_study_scheduler", SCHEDULER)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCHEDULER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# @MX:WARN: [AUTO] main — study-scheduler verification; highest assertion branching
# @MX:REASON: Cyclomatic complexity 20 (highest in the verify suite); guards the scheduler peer_id/profile_id contract (bootstrap-safety). Incorrect branching hides autonomous-study bootstrap regressions.
def main() -> None:
    scheduler = load_scheduler()
    scheduler.validate_agent_config()

    expected_peers = {"ra_us", "ra_eu", "ra_kr"}
    actual_peers = {agent["peer_id"] for agent in scheduler.AGENTS}
    if actual_peers != expected_peers:
        fail(f"unexpected peer IDs: {sorted(actual_peers)}")

    for agent in scheduler.AGENTS:
        if "-" in agent["peer_id"]:
            fail(f"hyphenated Honcho peer_id found: {agent}")
        if "_" not in agent["peer_id"]:
            fail(f"underscore Honcho peer_id missing: {agent}")
        if "-" not in agent["profile_id"]:
            fail(f"hyphen profile_id missing: {agent}")
        if agent["profile_id"] == agent["peer_id"]:
            fail(f"profile_id and peer_id collapsed: {agent}")

    source = SCHEDULER.read_text(encoding="utf-8")
    forbidden_snippets = [
        '"peer_id": agent_id',
        "record_insight(session_id, agent_id",
        "save_bootstrap_progress(agent_id",
        "load_bootstrap_progress().get(agent_id",
        "create_study_session(agent_id",
    ]
    for snippet in forbidden_snippets:
        if snippet in source:
            fail(f"forbidden legacy scheduler pattern remains: {snippet}")

    calls: list[tuple[str, dict[str, Any]]] = []

    def fake_post(path: str, body: dict[str, Any]) -> dict[str, Any]:
        calls.append((path, body))
        return {"id": body.get("id", "ok")}

    scheduler.honcho_post = fake_post
    scheduler.requests.get = lambda *args, **kwargs: SimpleNamespace(status_code=404)

    agent = next(item for item in scheduler.AGENTS if item["peer_id"] == "ra_us")
    chunk = {
        "id": "chunk-1",
        "source_path": "FDA/example.md",
        "content": "FDA requires design history file controls.",
    }
    insight = {
        "topic": "Design controls",
        "finding": "FDA requires traceable design history file controls.",
        "relevance": "Useful for US medical-device submission readiness.",
        "confidence": 0.91,
        "action_hint": "Check DHF completeness before review.",
    }
    run_ts = "2026-06-13T00:00:00+00:00"

    session_id = scheduler.create_study_session(agent, "bootstrap", run_ts)
    if session_id != "study-ra_us-bootstrap-2026-06-13":
        fail(f"session ID uses wrong peer convention: {session_id}")
    session_body = calls[-1][1]
    if session_body["metadata"]["actor"] != "ra_us":
        fail("session actor was not ra_us")

    scheduler.record_insight("session-1", agent, chunk, insight, run_ts)
    msg = calls[-1][1]["messages"][0]
    if msg["peer_id"] != "ra_us":
        fail(f"record_insight wrote wrong peer_id: {msg['peer_id']}")
    if msg["metadata"]["actor"] != "ra_us":
        fail(f"record_insight wrote wrong actor: {msg['metadata']['actor']}")
    if msg["content"].lstrip().startswith("{"):
        fail("record_insight content is still a JSON envelope")
    if "Finding: FDA requires traceable design history file controls." not in msg["content"]:
        fail("record_insight content lost domain finding text")

    source_agent = next(item for item in scheduler.AGENTS if item["peer_id"] == "ra_eu")
    scheduler.record_peer_insight("session-1", agent, source_agent, insight, run_ts)
    peer_msg = calls[-1][1]["messages"][0]
    if peer_msg["peer_id"] != "ra_us":
        fail(f"record_peer_insight wrote wrong target peer_id: {peer_msg['peer_id']}")
    if peer_msg["metadata"]["source_agent"] != "ra_eu":
        fail("record_peer_insight lost underscore source peer_id")
    if peer_msg["content"].lstrip().startswith("{"):
        fail("record_peer_insight content is still a JSON envelope")

    scheduler.record_session_complete("session-1", agent, 3, 2, run_ts)
    complete_msg = calls[-1][1]["messages"][0]
    if complete_msg["peer_id"] != "ra_us":
        fail(f"record_session_complete wrote wrong peer_id: {complete_msg['peer_id']}")
    if complete_msg["content"].lstrip().startswith("{"):
        fail("record_session_complete content is still a JSON envelope")

    print("OK: autonomous study scheduler peer_id contract holds")


if __name__ == "__main__":
    main()
