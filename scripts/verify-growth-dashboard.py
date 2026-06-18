#!/usr/bin/env python3
"""Local contract checks for the static growth dashboard."""

from __future__ import annotations

import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/growth-dashboard-verify.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render-growth-dashboard.py"
DASHBOARD = ROOT / "docs" / "growth-dashboard.html"


def fail(message: str) -> None:
    """Fail with detailed error logging."""
    logger.error(f"Contract violation: {message}")
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    """Verify dashboard contract with enhanced error handling."""
    try:
        # Ensure logs directory exists
        logs_dir = ROOT / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Starting dashboard contract verification...")

        if not SCRIPT.exists():
            fail(f"Dashboard renderer script not found: {SCRIPT}")

        if not DASHBOARD.exists():
            fail(f"Dashboard HTML not found: {DASHBOARD}")

        script = SCRIPT.read_text(encoding="utf-8")
        html = DASHBOARD.read_text(encoding="utf-8")

        required_script_terms = [
            "auto-growth-readiness",
            "growth-*.json",
            "hermes-auto-growth.timer",
            "ra-growth-metrics.timer",
            "coverage-guards.json",
            "growth-targets.json",
            "standalone HTML growth dashboard",
        ]
        for term in required_script_terms:
            if term not in script:
                fail(f"dashboard renderer missing {term}")

        required_html_terms = [
            "RA Growth Operations Dashboard",
            "RA Growth Operations",
            "Growth Trend Verdict",
            "Growth Evidence Radar",
            "Growth Signal Flow",
            "Mike / US FDA",
            "Theo / EU MDR",
            "Sam / MFDS",
            "기초 KB 확보 / 운영 성장 데이터 없음",
            "측정 가능",
            "Coverage Guard Basis",
            "legacy_pre_activation_floor",
            "not expert maturity",
            "Depth Proxy",
            "Source Coverage",
            "Readiness Matrix",
            "Cleanliness",
            "Activation Control",
            "Growth Trend",
            "Latest Growth Metrics",
            "Growth Report Trend",
            "radar-fill",
            "sparkline",
            "bar-fill",
            "dot ok",
            "16/16",
        ]
        for term in required_html_terms:
            if term not in html:
                fail(f"dashboard html missing {term}")

        if "fetch(" in html:
            fail("dashboard must be standalone and not fetch local JSON")
        if "http://" in html or "https://" in html:
            fail("dashboard must not depend on external network resources")

        # Timer status can be active/inactive, enabled/disabled, or not_found/not_found
        timer_status_found = False
        timer_variations = ["active/", "enabled/", "not_found/", "inactive/", "disabled/"]
        for variation in timer_variations:
            if variation in html:
                timer_status_found = True
                break

        if not timer_status_found:
            fail("dashboard missing timer status information (active/enabled or not_found/not_found)")

        logger.info("Dashboard contract verification passed")
        print("OK: static growth dashboard contract holds")

    except Exception as e:
        logger.error(f"Verification failed: {e}")
        raise


if __name__ == "__main__":
    main()
