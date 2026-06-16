#!/usr/bin/env python3
"""Local regression checks for scripts/ra-kr-growth-plan.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "ra-kr-growth-plan.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("ra_kr_growth_plan", SCRIPT)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()
    if module.DEFAULT_OPERATION_TIMEZONE != "Asia/Seoul":
        fail("default operation timezone must be Asia/Seoul")

    sample = {
        "self_docs": {"ra_us": 9064, "ra_eu": 2956, "ra_kr": 362},
        "daily_plan": {"planned_case_count": 5},
        "curriculum_gap": {"all": {"to_seed": 0}},
        "autonomous_study_plan": {"estimated_llm_calls": 80},
    }
    rec = module.recommendation(sample)
    if rec["timer_policy"] != "keep_off":
        fail("KR growth plan must keep timer off")
    if not rec["approval_required_before_write"]:
        fail("KR growth writes must require approval")
    if rec["preferred_next_step"] != "approved_daily_case_burst_first":
        fail("low KR depth should prefer approved daily case burst first")
    if len(rec["options"]) != 3:
        fail("recommendation must compare three growth options")

    print("OK: ra_kr growth plan contract holds")


if __name__ == "__main__":
    main()
