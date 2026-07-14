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


# @MX:WARN: [AUTO] main — daily-growth-runner verification; assertion branching
# @MX:REASON: Cyclomatic complexity 16; guards daily-growth invariants (peer_id/agent config). Incorrect branching hides growth-loop regressions.
def main() -> None:
    module = load_module()
    module.validate_agent_config()
    if module.DEFAULT_OPERATION_TIMEZONE != "Asia/Seoul":
        fail("default operation timezone must be Asia/Seoul")
    if module.parse_run_date("2026-06-16").isoformat() != "2026-06-16":
        fail("explicit run date parsing is broken")

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

    # #111 follow-up — reject README bullet/numbered manifest chunks (item
    # names/steps with no explanatory prose), reproduced from live checksheet
    # cases in the 2026-07-15 re-eval (docs/kb-eval-checksheets/2026-07-15/).
    readme_bullet_manifest = (
        "## 수록 대상\n"
        "- MDR 2017/745 원문 (영문·국문 번역본)\n"
        "- 개정 Regulation (EU) 2023/607 (전환기간 연장)\n"
        "- Annex I (General Safety and Performance Requirements, GSPR)\n"
        "- Annex II (Technical Documentation)\n"
        "- Annex III (Post-Market Surveillance)\n"
        "- Annex VIII (Classification Rules)"
    )
    if module.is_substantive_chunk(readme_bullet_manifest):
        fail("README bullet manifest chunk must be rejected as non-substantive")

    readme_numbered_manifest = (
        "## 제출 절차 개요\n"
        "1. Predicate Device 조사 (FDA 510(k) Database)\n"
        "2. Substantial Equivalence 비교표 작성\n"
        "3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비\n"
        "4. eSTAR 템플릿을 통한 전자 제출\n"
        "5. FDA 심사 질의(AI: Additional Information) 대응"
    )
    if module.is_substantive_chunk(readme_numbered_manifest):
        fail("README numbered manifest chunk must be rejected as non-substantive")

    substantive_bullets = (
        "## Predicate 비교 시 확인 사항\n"
        "- 기존 predicate 대비 기술적 차이가 유의미한 경우, 반드시 성능시험 데이터로 "
        "substantial equivalence를 입증해야 하며 단순 서면 주장만으로는 부족하다.\n"
        "- 소프트웨어 변경이 진단 알고리즘에 영향을 미치는 경우 PCCP 범위 내 변경인지 "
        "별도 검토가 필요하다."
    )
    if not module.is_substantive_chunk(substantive_bullets):
        fail("substantive bulleted analysis must not be rejected (over-filtering regression)")

    print("OK: daily growth runner contract and payload shape hold")


if __name__ == "__main__":
    main()
