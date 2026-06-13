#!/usr/bin/env python3
"""Local regression checks for scripts/curriculum-seed.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "curriculum-seed.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("curriculum_seed", SCRIPT)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()
    module.validate_agent_config()

    agent = module.AGENTS["ra-kr"]
    if agent.peer_id != "ra_kr":
        fail(f"ra-kr must write to ra_kr, got {agent.peer_id}")
    if "-" in agent.peer_id:
        fail(f"hyphenated Honcho peer_id found: {agent.peer_id}")

    session_name = module.build_session_name(agent, "2026-06-13")
    if session_name != "study-ra_kr-curriculum-seed-2026-06-13":
        fail(f"wrong session naming convention: {session_name}")

    candidate = module.SourceCandidate(
        source_path="github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md",
        chunk_count=2,
        source_hash="abc123",
        first_indexed_at="2026-06-01T00:00:00+00:00",
        last_indexed_at="2026-06-02T00:00:00+00:00",
        matched_keywords=("MFDS", "국내_MFDS"),
    )
    chunks = [
        {"id": "chunk-1", "content": "MFDS approval requires a technical document."},
        {"id": "chunk-2", "content": "KGMP evidence must be checked before submission."},
    ]
    message = module.build_message(
        agent=agent,
        candidate=candidate,
        chunks=chunks,
        run_ts="2026-06-13T00:00:00+00:00",
        scope="explicit",
        source_rank=1,
        max_snippet_chars=200,
    )

    if message["peer_id"] != "ra_kr":
        fail(f"message peer_id must be ra_kr, got {message['peer_id']}")
    if message["content"].lstrip().startswith("{"):
        fail("message content is a JSON envelope")
    if "Regulatory source curriculum seed" not in message["content"]:
        fail("message content lost curriculum heading")
    if "Source hash: abc123" not in message["content"]:
        fail("message content lost source hash")

    metadata = message["metadata"]
    if metadata["record_type"] != "curriculum_seed":
        fail(f"wrong record_type: {metadata['record_type']}")
    if metadata["actor"] != "ra_kr" or metadata["peer_id"] != "ra_kr":
        fail(f"metadata actor/peer_id mismatch: {metadata}")
    if metadata["profile_id"] != "ra-kr":
        fail(f"profile_id must stay hyphenated: {metadata['profile_id']}")
    if metadata["curriculum_version"] != module.CURRICULUM_VERSION:
        fail("curriculum version mismatch")

    print("OK: curriculum seed peer_id contract and payload shape hold")


if __name__ == "__main__":
    main()
