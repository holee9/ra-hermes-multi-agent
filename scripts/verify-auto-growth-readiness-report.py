#!/usr/bin/env python3
"""Local regression checks for scripts/auto-growth-readiness-report.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "auto-growth-readiness-report.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("auto_growth_readiness_report", SCRIPT)
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
    if module.AGENT_PEERS != ("ra_us", "ra_eu", "ra_kr"):
        fail("unexpected RA peer list")
    if module.EXPECTED_SEEDS != {"ra_us": 48, "ra_eu": 31, "ra_kr": 29}:
        fail("expected seed counts changed unexpectedly")

    sample = {
        "operation_date": "2026-06-16",
        "timer": {
            "active": {"stdout": "inactive"},
            "enabled": {"stdout": "disabled"},
            "timers": {"stdout": "ra-growth-metrics.timer"},
            "persistent_false": True,
        },
        "activation_guard": {"returncode": 2},
        "db": {
            "pending_total": 0,
            "pending_by_ra": {"ra_us": 0, "ra_eu": 0, "ra_kr": 0},
            "wrong_peer": {"messages": 0, "queue_refs": 0, "embeddings": 0, "active_docs": 0},
            "self_docs": {"ra_us": 9064, "ra_eu": 2956, "ra_kr": 362},
            "curriculum_seed": {
                "ra_us": {"total": 48},
                "ra_eu": {"total": 31},
                "ra_kr": {"total": 29},
            },
            "growth_health": [
                {"record_type": "daily_growth_case", "active_json_envelopes": 0, "hyphen_peers": 0}
            ],
        },
        "daily_plan": {
            "plan": {
                "run_date": "2026-06-16",
                "planned_case_count": 3,
                "execute_gate": {"allowed": True},
            }
        },
    }
    matrix = module.score_matrix(sample)
    if matrix["scores"]["activation_control"]["score"] != 4:
        fail("activation control should be fully ready in sample")
    if matrix["scores"]["data_cleanliness"]["score"] != 4:
        fail("data cleanliness should be fully ready in sample")
    if matrix["scores"]["growth_input_quality"]["score"] != 4:
        fail("growth input quality should be fully ready in sample")
    if matrix["scores"]["agent_balance"]["score"] >= 4:
        fail("agent balance should expose current ra_kr depth gap")
    if matrix["timer_operation_recommendation"] != "keep_off":
        fail("timer recommendation must remain keep_off when matrix is below 16")

    print("OK: auto-growth readiness report contract holds")


if __name__ == "__main__":
    main()
