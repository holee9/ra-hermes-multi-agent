#!/usr/bin/env python3
"""
Day 15 Midpoint System Health Check

Comprehensive system health check for midpoint review.
Covers all major components: metrics, dashboard, automation, agents, infrastructure.
"""

from __future__ import annotations

import json
import logging
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/day15-midpoint-check.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
DASHBOARD = ROOT / "docs" / "growth-dashboard.html"
SCRIPTS = ROOT / "scripts"

# Health check categories
CATEGORIES = {
    "growth_metrics": "Growth Metrics Collection",
    "dashboard": "Dashboard Generation",
    "auto_copy": "Dashboard Auto-Copy",
    "readiness": "Readiness Matrix",
    "automation": "Automation Timers",
    "agents": "RA Agents Activity",
    "infrastructure": "Infrastructure Health"
}


def check_growth_metrics() -> dict[str, Any]:
    """Check growth metrics system health."""
    issues = []
    status = "ok"

    try:
        # Check latest growth report
        growth_files = sorted(REPORTS.glob("growth-*.json"))
        if not growth_files:
            issues.append("No growth reports found")
            return {"status": "fail", "issues": issues}

        latest_growth = growth_files[-1]
        data = json.loads(latest_growth.read_text(encoding="utf-8"))

        sessions = data.get("sessions_scanned", 0)
        messages = data.get("messages_scanned", 0)

        if sessions == 0 or messages == 0:
            issues.append(f"Zero data collection (sessions: {sessions}, messages: {messages})")
            status = "warn"

        # Check ingestion diagnostics
        ingestion = data.get("ingestion_diagnostics", {})
        api_status = ingestion.get("api_status", "unknown")

        if api_status == "failed":
            issues.append(f"Honcho API failed: {api_status}")
            status = "fail"
        elif api_status == "partial_failure":
            issues.append(f"Honcho API partial failure: {api_status}")
            if status != "fail":
                status = "warn"

    except Exception as e:
        issues.append(f"Growth metrics check failed: {e}")
        status = "fail"

    return {"status": status, "issues": issues}


def check_dashboard() -> dict[str, Any]:
    """Check dashboard system health."""
    issues = []
    status = "ok"

    try:
        if not DASHBOARD.exists():
            issues.append("Dashboard file not found")
            return {"status": "fail", "issues": issues}

        # Check dashboard age
        import time
        dashboard_age = time.time() - DASHBOARD.stat().st_mtime
        age_hours = dashboard_age / 3600

        if age_hours > 48:  # 2 days
            issues.append(f"Dashboard outdated ({age_hours:.1f} hours old)")
            status = "warn"

        # Check dashboard content
        html_content = DASHBOARD.read_text(encoding="utf-8")

        required_terms = ["RA Growth Operations Dashboard", "Growth Trend Verdict"]
        for term in required_terms:
            if term not in html_content:
                issues.append(f"Dashboard missing required term: {term}")
                status = "fail"

    except Exception as e:
        issues.append(f"Dashboard check failed: {e}")
        status = "fail"

    return {"status": status, "issues": issues}


def check_auto_copy() -> dict[str, Any]:
    """Check auto-copy system health."""
    issues = []
    status = "ok"

    try:
        config_file = SCRIPTS / "dashboard-copy-config.json"

        if not config_file.exists():
            issues.append("Auto-copy config not found")
            return {"status": "fail", "issues": issues}

        config = json.loads(config_file.read_text(encoding="utf-8"))

        dashboard_dests = config.get("dashboard_destinations", [])
        reports_dests = config.get("reports_backup_destinations", [])

        if not dashboard_dests and not reports_dests:
            issues.append("No copy destinations configured")
            status = "warn"

        # Check if destinations exist
        for dest in dashboard_dests:
            dest_path = Path(dest)
            if not dest_path.exists():
                issues.append(f"Dashboard destination not found: {dest}")
                status = "fail"

        for dest in reports_dests:
            dest_path = Path(dest)
            if not dest_path.exists():
                issues.append(f"Reports backup destination not found: {dest}")
                status = "fail"

    except Exception as e:
        issues.append(f"Auto-copy check failed: {e}")
        status = "fail"

    return {"status": status, "issues": issues}


def check_readiness() -> dict[str, Any]:
    """Check readiness matrix health."""
    issues = []
    status = "ok"

    try:
        readiness_dir = REPORTS / "auto-growth-readiness"
        if not readiness_dir.exists():
            issues.append("Readiness reports directory not found")
            return {"status": "fail", "issues": issues}

        readiness_files = sorted(readiness_dir.glob("*.json"))
        if not readiness_files:
            issues.append("No readiness reports found")
            return {"status": "fail", "issues": issues}

        latest_readiness = readiness_files[-1]
        data = json.loads(latest_readiness.read_text(encoding="utf-8"))

        matrix = data.get("matrix", {})
        total_score = matrix.get("total_score", 0)
        max_score = matrix.get("max_score", 16)

        if total_score < max_score * 0.8:  # Less than 80%
            issues.append(f"Readiness score low: {total_score}/{max_score}")
            status = "warn"

    except Exception as e:
        issues.append(f"Readiness check failed: {e}")
        status = "fail"

    return {"status": status, "issues": issues}


def check_automation() -> dict[str, Any]:
    """Check automation timer health."""
    issues = []
    status = "ok"

    try:
        # Check systemd timers (may not be available in all environments)
        timer_checks = [
            ("hermes-auto-growth.timer", "Hermes auto-growth timer"),
            ("ra-growth-metrics.timer", "Growth metrics timer")
        ]

        for timer_name, description in timer_checks:
            try:
                result = subprocess.run(
                    ["systemctl", "is-active", timer_name],
                    capture_output=True,
                    text=True,
                    timeout=5
                )

                if result.returncode != 0:
                    issues.append(f"{description} not active")
                    status = "warn"

            except (FileNotFoundError, subprocess.TimeoutExpired) as e:
                issues.append(f"Cannot check {description}: {e}")
                status = "warn"

    except Exception as e:
        issues.append(f"Automation check failed: {e}")
        status = "fail"

    return {"status": status, "issues": issues}


def check_agents() -> dict[str, Any]:
    """Check RA agents activity."""
    issues = []
    status = "ok"

    try:
        # Check latest growth report for agent activity
        growth_files = sorted(REPORTS.glob("growth-*.json"))
        if not growth_files:
            issues.append("No growth reports to check agent activity")
            return {"status": "fail", "issues": issues}

        latest_growth = growth_files[-1]
        data = json.loads(latest_growth.read_text(encoding="utf-8"))

        metrics = data.get("metrics", {})
        study_sessions = metrics.get("autonomous_study_sessions", {})
        study_sessions_value = study_sessions.get("value", 0)

        if study_sessions_value == 0:
            issues.append("No autonomous study sessions detected")
            status = "warn"

    except Exception as e:
        issues.append(f"Agent activity check failed: {e}")
        status = "fail"

    return {"status": status, "issues": issues}


def check_infrastructure() -> dict[str, Any]:
    """Check infrastructure health."""
    issues = []
    status = "ok"

    try:
        # Check if logs directory exists and is writable
        logs_dir = ROOT / "logs"
        if not logs_dir.exists():
            issues.append("Logs directory not found")
            status = "warn"
        else:
            # Test writability
            test_file = logs_dir / "health_check.tmp"
            try:
                test_file.write_text("test")
                test_file.unlink()
            except Exception as e:
                issues.append(f"Logs directory not writable: {e}")
                status = "fail"

        # Check reports directory
        if not REPORTS.exists():
            issues.append("Reports directory not found")
            status = "fail"

    except Exception as e:
        issues.append(f"Infrastructure check failed: {e}")
        status = "fail"

    return {"status": status, "issues": issues}


def generate_report(results: dict[str, Any]) -> str:
    """Generate formatted health check report."""
    lines = [
        "=" * 60,
        "Day 15 Midpoint System Health Check",
        f"Generated: {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 60,
        ""
    ]

    total_issues = 0
    fail_count = 0

    for category, check_name in CATEGORIES.items():
        result = results.get(category, {})
        status = result.get("status", "unknown")
        issues = result.get("issues", [])

        status_symbol = {
            "ok": "✅",
            "warn": "⚠️ ",
            "fail": "❌",
            "unknown": "❓"
        }.get(status, "❓")

        lines.append(f"{status_symbol} {check_name}: {status.upper()}")

        if issues:
            total_issues += len(issues)
            if status == "fail":
                fail_count += 1
            for issue in issues:
                lines.append(f"   - {issue}")
        lines.append("")

    # Summary
    lines.extend([
        "=" * 60,
        "SUMMARY",
        "=" * 60,
        f"Total Issues: {total_issues}",
        f"Failed Categories: {fail_count}",
        f"Overall Health: {'PASS' if fail_count == 0 else 'REVIEW NEEDED'}",
        "=" * 60
    ])

    return "\n".join(lines)


def main() -> None:
    """Main entry point."""
    try:
        # Ensure logs directory exists
        logs_dir = ROOT / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Starting Day 15 midpoint health check...")

        # Run all health checks
        results = {
            "growth_metrics": check_growth_metrics(),
            "dashboard": check_dashboard(),
            "auto_copy": check_auto_copy(),
            "readiness": check_readiness(),
            "automation": check_automation(),
            "agents": check_agents(),
            "infrastructure": check_infrastructure()
        }

        # Generate and print report
        report = generate_report(results)
        print(report)

        # Save report to file
        report_file = ROOT / "reports" / "day15-midpoint-health.txt"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        report_file.write_text(report, encoding="utf-8")

        logger.info(f"Health check report saved: {report_file.name}")

        # Exit with appropriate code
        fail_count = sum(1 for r in results.values() if r.get("status") == "fail")
        if fail_count > 0:
            logger.warning(f"Health check completed with {fail_count} failed categories")
            exit(1)
        else:
            logger.info("Health check passed")
            exit(0)

    except Exception as e:
        logger.error(f"Health check failed: {e}")
        print(f"ERROR: {e}")
        exit(1)


if __name__ == "__main__":
    main()