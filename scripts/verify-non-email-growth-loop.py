#!/usr/bin/env python3
"""Local contract checks for scripts/non-email-growth-loop.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "non-email-growth-loop.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("non_email_growth_loop", SCRIPT)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()
    if module.RA_PEERS != ("ra_us", "ra_eu", "ra_kr"):
        fail(f"unexpected RA_PEERS: {module.RA_PEERS}")
    if module.selected_cadences("all") != ["daily", "weekly", "monthly", "quarterly"]:
        fail("all cadence order changed")

    parser = module.build_parser()
    args = parser.parse_args([])
    if args.cadence != "all":
        fail("default cadence must be all")
    if args.execute_daily or args.execute_curriculum:
        fail("writes must be opt-in")
    if args.max_pending != 0:
        fail("default max_pending must be 0")

    report = {
        "ra_pending_after": {"ra_us": 0, "ra_eu": 0, "ra_kr": 0},
        "verifiers": [{"name": "ok", "returncode": 0}],
        "cadence_results": {"daily": {"returncode": 0}},
        "growth_records": {
            "by_peer_record_type": [
                {
                    "peer_name": "ra_us",
                    "record_type": "daily_growth_case",
                    "json_envelopes": 0,
                    "active_json_envelopes": 0,
                    "quarantined_json_envelopes": 0,
                }
            ]
        },
    }
    if module.evaluate(report, 0):
        fail("clean report should pass")

    dirty = dict(report)
    dirty["ra_pending_after"] = {"ra_us": 1, "ra_eu": 0, "ra_kr": 0}
    if not module.evaluate(dirty, 0):
        fail("RA pending must fail")

    quarantined = dict(report)
    quarantined["ra_pending_after"] = {"ra_us": 0, "ra_eu": 0, "ra_kr": 0}
    quarantined["growth_records"] = {
        "by_peer_record_type": [
            {
                "peer_name": "ra_us",
                "record_type": "study_insight",
                "json_envelopes": 1,
                "active_json_envelopes": 0,
                "quarantined_json_envelopes": 1,
            }
        ]
    }
    if module.evaluate(quarantined, 0):
        fail("quarantined JSON envelope should not fail active growth gate")

    print("OK: non-email growth loop contract holds")


if __name__ == "__main__":
    main()
