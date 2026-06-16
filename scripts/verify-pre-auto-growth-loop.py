#!/usr/bin/env python3
"""Local contract checks for scripts/pre-auto-growth-loop.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "pre-auto-growth-loop.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("pre_auto_growth_loop", SCRIPT)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()
    if module.AGENT_PEERS != ("ra_us", "ra_eu", "ra_kr"):
        fail(f"unexpected AGENT_PEERS: {module.AGENT_PEERS}")
    if "scripts/verify-daily-growth-runner.py" not in module.VERIFY_SCRIPTS:
        fail("daily growth verifier must be part of the pre-auto loop")
    if "scripts/verify-non-email-growth-loop.py" not in module.VERIFY_SCRIPTS:
        fail("non-email growth verifier must be part of the pre-auto loop")
    if "scripts/verify-study-scheduler.py" not in module.VERIFY_SCRIPTS:
        fail("study scheduler verifier must be part of the pre-auto loop")
    if "scripts/verify-auto-growth-activation-policy.py" not in module.VERIFY_SCRIPTS:
        fail("activation policy verifier must be part of the pre-auto loop")
    if "scripts/verify-auto-growth-readiness-report.py" not in module.VERIFY_SCRIPTS:
        fail("readiness report verifier must be part of the pre-auto loop")
    if module.DEFAULT_OPERATION_TIMEZONE != "Asia/Seoul":
        fail("default operation timezone must be Asia/Seoul")

    parser = module.build_parser()
    args = parser.parse_args([])
    if args.iterations != 1:
        fail("default iterations must be 1")
    if args.max_pending != 0:
        fail("default max_pending must be 0")
    if args.pending_scope != "all":
        fail("default pending_scope must be all")
    if args.execute_daily_growth:
        fail("execute_daily_growth must be opt-in")
    if args.operation_timezone != "Asia/Seoul":
        fail("default operation timezone arg must be Asia/Seoul")
    if args.cases_per_agent != 1 or args.source_pool != 10 or args.max_chunks_per_case != 1:
        fail("default smoke size changed unexpectedly")

    clean_report = {
        "deriver_flush": {"ok": True},
        "queue_before": {"pending_total": 0},
        "verifiers": [{"cmd": ["python3", "ok.py"], "returncode": 0}],
        "daily_growth_dry_run": {
            "command": {"returncode": 0},
            "plan": {"execute_gate": {"allowed": True}},
        },
        "growth_message_health": {"json_envelopes": 0, "hyphen_peers": 0},
        "queue_after": {"pending_total": 0},
    }
    if module.pending_for_scope({"pending_total": 2, "pending_by_ra": {"ra_us": 0, "ra_eu": 0, "ra_kr": 0}}, "ra") != 0:
        fail("RA pending scope must ignore non-RA pending")
    if module.evaluate_iteration(clean_report, 0, "all"):
        fail("clean report should not fail")

    dirty_report = dict(clean_report)
    dirty_report["queue_after"] = {"pending_total": 1}
    if not module.evaluate_iteration(dirty_report, 0, "all"):
        fail("dirty queue must fail evaluation")

    print("OK: pre-auto growth loop contract holds")


if __name__ == "__main__":
    main()
