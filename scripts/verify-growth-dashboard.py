#!/usr/bin/env python3
"""Local contract checks for the static growth dashboard."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render-growth-dashboard.py"
DASHBOARD = ROOT / "docs" / "growth-dashboard.html"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
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
        "측정 불충분",
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
        "active/enabled",
    ]
    for term in required_html_terms:
        if term not in html:
            fail(f"dashboard html missing {term}")

    if "fetch(" in html:
        fail("dashboard must be standalone and not fetch local JSON")
    if "http://" in html or "https://" in html:
        fail("dashboard must not depend on external network resources")

    print("OK: static growth dashboard contract holds")


if __name__ == "__main__":
    main()
