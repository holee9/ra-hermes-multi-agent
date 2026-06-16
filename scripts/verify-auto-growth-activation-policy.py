#!/usr/bin/env python3
"""Local regression checks for auto-growth activation safety policy."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIMER = ROOT / "scripts" / "systemd" / "hermes-auto-growth.timer"
INSTALLER = ROOT / "scripts" / "install-auto-growth-timer.sh"
DAILY_RUNNER = ROOT / "scripts" / "daily-growth-runner.py"
PRE_AUTO = ROOT / "scripts" / "pre-auto-growth-loop.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_daily_runner():
    spec = importlib.util.spec_from_file_location("daily_growth_runner", DAILY_RUNNER)
    if spec is None or spec.loader is None:
        fail(f"could not load {DAILY_RUNNER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    timer = TIMER.read_text(encoding="utf-8")
    if "Persistent=false" not in timer:
        fail("hermes-auto-growth.timer must use Persistent=false")
    if "Persistent=true" in timer:
        fail("hermes-auto-growth.timer must not enable missed-run catch-up")

    installer = INSTALLER.read_text(encoding="utf-8")
    if "--confirm-auto-growth-activation" not in installer:
        fail("installer must require explicit auto-growth activation marker")
    if "Refusing to activate auto growth without explicit approval" not in installer:
        fail("installer must refuse activation without approval")

    daily = load_daily_runner()
    if daily.DEFAULT_OPERATION_TIMEZONE != "Asia/Seoul":
        fail("daily growth default operation timezone must be Asia/Seoul")

    pre_auto = PRE_AUTO.read_text(encoding="utf-8")
    if "scripts/verify-auto-growth-activation-policy.py" not in pre_auto:
        fail("pre-auto loop must include activation policy verifier")
    if "--operation-timezone" not in pre_auto:
        fail("pre-auto loop must pass operation timezone to daily growth runner")

    print("OK: auto-growth activation policy holds")


if __name__ == "__main__":
    main()
