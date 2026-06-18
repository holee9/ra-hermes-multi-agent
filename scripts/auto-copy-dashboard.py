#!/usr/bin/env python3
"""
Automatically copy dashboard and reports to designated locations.

Supports copying:
- Latest dashboard HTML to configured destinations
- Growth report JSON files to backup locations
- Readiness reports to backup locations
"""

from __future__ import annotations

import logging
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/dashboard-auto-copy.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Directories
ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
DASHBOARD = ROOT / "docs" / "growth-dashboard.html"
CONFIG = ROOT / "scripts" / "dashboard-copy-config.json"

# Default copy destinations
DEFAULT_DESTINATIONS = {
    "dashboard": [],  # List of destination paths for dashboard HTML
    "reports_backup": [],  # List of destination paths for reports backup
}


def load_config() -> dict[str, Any]:
    """Load copy configuration from JSON file."""
    try:
        if CONFIG.exists():
            import json
            content = CONFIG.read_text(encoding="utf-8")
            return json.loads(content)
        else:
            logger.info(f"Config file not found: {CONFIG}, using defaults")
            return DEFAULT_DESTINATIONS
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        return DEFAULT_DESTINATIONS


def copy_file(src: Path, dst: Path) -> bool:
    """Copy a single file with error handling."""
    try:
        # Ensure destination directory exists
        dst.parent.mkdir(parents=True, exist_ok=True)

        # Copy file
        shutil.copy2(src, dst)
        logger.info(f"Copied: {src.name} -> {dst}")
        return True
    except Exception as e:
        logger.error(f"Failed to copy {src} to {dst}: {e}")
        return False


def sync_dashboard(destinations: list[Path]) -> dict[str, Any]:
    """Sync dashboard to all destinations."""
    if not DASHBOARD.exists():
        logger.error(f"Dashboard not found: {DASHBOARD}")
        return {"success": False, "copied": 0, "failed": 0}

    results = {"success": True, "copied": 0, "failed": 0, "destinations": []}

    for dest_path in destinations:
        dest = dest_path / "growth-dashboard.html"
        if copy_file(DASHBOARD, dest):
            results["copied"] += 1
            results["destinations"].append(str(dest))
        else:
            results["failed"] += 1
            results["success"] = False

    return results


def backup_reports(destinations: list[Path]) -> dict[str, Any]:
    """Backup latest reports to configured destinations."""
    if not REPORTS.exists():
        logger.warning(f"Reports directory not found: {REPORTS}")
        return {"success": False, "copied": 0, "failed": 0}

    # Get latest reports
    growth_reports = sorted(REPORTS.glob("growth-*.json"))
    readiness_reports = sorted((REPORTS / "auto-growth-readiness").glob("*.json")) if (REPORTS / "auto-growth-readiness").exists() else []

    if not growth_reports and not readiness_reports:
        logger.warning("No reports to backup")
        return {"success": True, "copied": 0, "failed": 0, "message": "No reports found"}

    results = {"success": True, "copied": 0, "failed": 0, "files": []}

    # Backup latest growth report
    if growth_reports:
        latest_growth = growth_reports[-1]
        for dest_path in destinations:
            dest = dest_path / "reports" / latest_growth.name
            if copy_file(latest_growth, dest):
                results["copied"] += 1
                results["files"].append(str(dest))
            else:
                results["failed"] += 1
                results["success"] = False

    # Backup latest readiness report
    if readiness_reports:
        latest_readiness = readiness_reports[-1]
        for dest_path in destinations:
            dest = dest_path / "reports" / "auto-growth-readiness" / latest_readiness.name
            if copy_file(latest_readiness, dest):
                results["copied"] += 1
                results["files"].append(str(dest))
            else:
                results["failed"] += 1
                results["success"] = False

    return results


def generate_sample_config() -> None:
    """Generate sample configuration file."""
    import json

    sample_config = {
        "dashboard_destinations": [
            "/path/to/nas/ra-hermes/reports",
            "/path/to/backup/location"
        ],
        "reports_backup_destinations": [
            "/path/to/nas/ra-hermes/reports/backup"
        ],
        "note": "Edit these paths to match your environment"
    }

    try:
        CONFIG.parent.mkdir(parents=True, exist_ok=True)
        CONFIG.write_text(json.dumps(sample_config, indent=2, ensure_ascii=False), encoding="utf-8")
        logger.info(f"Generated sample config: {CONFIG}")
    except Exception as e:
        logger.error(f"Failed to generate sample config: {e}")


def main() -> None:
    """Main entry point."""
    try:
        # Ensure logs directory exists
        logs_dir = ROOT / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Starting dashboard auto-copy...")

        # Load configuration
        config = load_config()

        # Convert destination strings to Path objects
        dashboard_dests = [Path(d) for d in config.get("dashboard_destinations", [])]
        reports_dests = [Path(d) for d in config.get("reports_backup_destinations", [])]

        if not dashboard_dests and not reports_dests:
            logger.warning("No destinations configured, generating sample config...")
            generate_sample_config()
            logger.info("Please edit the config file and run again")
            return

        # Sync dashboard
        if dashboard_dests:
            dashboard_results = sync_dashboard(dashboard_dests)
            logger.info(f"Dashboard sync: {dashboard_results['copied']} copied, {dashboard_results['failed']} failed")

        # Backup reports
        if reports_dests:
            reports_results = backup_reports(reports_dests)
            logger.info(f"Reports backup: {reports_results['copied']} copied, {reports_results['failed']} failed")

        logger.info("Dashboard auto-copy completed")

    except Exception as e:
        logger.error(f"Auto-copy failed: {e}")
        raise


if __name__ == "__main__":
    main()