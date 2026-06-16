#!/usr/bin/env python3
"""Evaluate readiness for post-mail-triage growth transitions.

This script does not activate automation. It summarizes whether enough valid
growth evidence exists for:
- #65 threshold/notification policy
- #40 form workflow transfer
- #41 specialist expansion review
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT / "reports"
TRIGGER_CONFIG = ROOT / "feedback" / "config" / "growth-trigger-config.json"


def load_json(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, dict) else {}


def load_reports(limit: int = 30) -> list[dict[str, Any]]:
    reports = []
    for path in sorted(REPORTS_DIR.glob("growth*.json")):
        data = load_json(path)
        if not isinstance(data.get("metrics"), dict):
            continue
        data["_path"] = str(path.relative_to(ROOT))
        reports.append(data)
    return reports[-limit:]


def metric_value(report: dict[str, Any], name: str) -> Any:
    return ((report.get("metrics") or {}).get(name) or {}).get("value")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate growth transition readiness.")
    parser.add_argument("--output", help="Optional output JSON path.")
    parser.add_argument("--min-valid-days", type=int, default=30)
    args = parser.parse_args()

    reports = load_reports(limit=max(args.min_valid_days, 30))
    trigger_cfg = load_json(TRIGGER_CONFIG) if TRIGGER_CONFIG.exists() else {}
    valid_reports = [
        report for report in reports
        if int(report.get("messages_scanned") or 0) > 0
        and ((report.get("ingestion_diagnostics") or {}).get("empty_cause") in (None, "metrics_input_available"))
    ]
    latest = reports[-1] if reports else {}
    thresholds_defined = [
        name for name, cfg in (trigger_cfg.get("triggers") or {}).items()
        if cfg.get("threshold") is not None
    ]
    null_thresholds = [
        name for name, cfg in (trigger_cfg.get("triggers") or {}).items()
        if cfg.get("threshold") is None
    ]

    latest_absence = ((latest.get("metrics") or {}).get("absence_pattern_signals") or {})
    form_conditions = {
        "valid_metrics_days": len(valid_reports),
        "requires_valid_metrics_days": args.min_valid_days,
        "latest_messages_scanned": latest.get("messages_scanned", 0),
        "latest_empty_cause": (latest.get("ingestion_diagnostics") or {}).get("empty_cause"),
        "thresholds_defined": thresholds_defined,
        "null_thresholds": null_thresholds,
    }
    form_ready = (
        len(valid_reports) >= args.min_valid_days
        and len(null_thresholds) == 0
        and metric_value(latest, "correction_rate") is not None
        and metric_value(latest, "first_pass_match_accuracy") is not None
        and metric_value(latest, "escalation_precision") is not None
    )

    specialist_review_ready = (
        int(latest_absence.get("value") or 0) > 0
        and int(latest.get("messages_scanned") or 0) > 0
    )

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "reports_loaded": len(reports),
        "valid_reports": len(valid_reports),
        "latest_report": latest.get("_path"),
        "threshold_policy": {
            "ready_for_definition": len(valid_reports) > 0,
            "status": "ready_for_human_policy" if len(valid_reports) > 0 else "blocked_by_metrics_ingestion",
            "thresholds_defined": thresholds_defined,
            "null_thresholds": null_thresholds,
        },
        "form_transfer": {
            "ready": form_ready,
            "status": "ready_for_design" if form_ready else "blocked_by_growth_evidence",
            "conditions": form_conditions,
        },
        "specialist_expansion": {
            "ready_for_review": specialist_review_ready,
            "status": "review_signal_present" if specialist_review_ready else "insufficient_operating_signal",
            "absence_pattern_signals": latest_absence,
        },
    }

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
