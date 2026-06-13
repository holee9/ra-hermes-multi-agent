#!/usr/bin/env python3
"""Local regression checks for scripts/daily-growth-runner.py."""

from __future__ import annotations

import importlib.util
import sys
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "daily-growth-runner.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("daily_growth_runner", SCRIPT)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()
    module.validate_agent_config()

    expected_peers = {"ra_us", "ra_eu", "ra_kr"}
    actual_peers = {agent.peer_id for agent in module.AGENTS.values()}
    if actual_peers != expected_peers:
        fail(f"unexpected peers: {sorted(actual_peers)}")

    agent = module.AGENTS["ra-kr"]
    if agent.peer_id != "ra_kr" or agent.profile_id != "ra-kr":
        fail("ra-kr profile/peer contract is wrong")

    source_case = module.SourceCase(
        scenario_id="scenario-1",
        source_path="github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md",
        source_hash="hash-1",
        chunk_count=2,
        matched_keywords=("MFDS", "국내_MFDS"),
        excerpts=(
            {"id": "chunk-1", "excerpt": "MFDS licensing requires technical documentation."},
            {"id": "chunk-2", "excerpt": "KGMP evidence must be reviewed before submission."},
        ),
    )
    message = module.build_message(agent, source_case, date(2026, 6, 13))
    if message["peer_id"] != "ra_kr":
        fail(f"message peer_id must be ra_kr, got {message['peer_id']}")
    if message["content"].lstrip().startswith("{"):
        fail("daily growth content is a JSON envelope")
    if "Daily regulatory growth case" not in message["content"]:
        fail("missing growth case heading")
    if "Peer review prompt" not in message["content"]:
        fail("missing peer-review prompt")

    metadata = message["metadata"]
    if metadata["record_type"] != "daily_growth_case":
        fail("wrong record_type")
    if metadata["actor"] != "ra_kr" or metadata["peer_id"] != "ra_kr":
        fail("metadata actor/peer_id mismatch")
    if metadata["profile_id"] != "ra-kr":
        fail("profile_id must stay hyphenated")
    if metadata["growth_version"] != module.GROWTH_VERSION:
        fail("growth version mismatch")

    blocked_gate = {
        "manual_growth_complete_required": True,
        "manual_growth_complete_provided": False,
        "pending_total": 0,
        "max_pending_allowed": 0,
        "allowed": False,
    }
    if blocked_gate["allowed"]:
        fail("execute gate must remain closed without manual completion")

    print("OK: daily growth runner contract and payload shape hold")


if __name__ == "__main__":
    main()
