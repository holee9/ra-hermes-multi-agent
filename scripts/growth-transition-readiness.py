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
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT / "reports"
TRIGGER_CONFIG = ROOT / "feedback" / "config" / "growth-trigger-config.json"

# 설정 계약(`feedback/config/growth-trigger-config.json`)이 고정한 트리거 → 지표 매핑.
# 임계값 **값**은 사람이 정하지만, 어떤 트리거가 어떤 지표에 걸리는지는 계약이 정한다.
# 이름만 확인하고 지표를 안 보면 "0.5" 가 무엇에 대한 0.5 인지 모르는 채 통과한다.
TRIGGER_METRIC_CONTRACT: dict[str, str] = {
    "duplicate_wp_reduction": "duplicate_wp_rate_7d_ma",
    "human_correction_rate": "correction_rate",
    "transition_accuracy": "first_pass_match_accuracy",
    "mail_triage_stability": "correction_rate",
}
REQUIRED_TRIGGERS = frozenset(TRIGGER_METRIC_CONTRACT)


def load_json(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, dict) else {}


# Only dated snapshots count. `growth-diagnostic-*.json` and other growth* files are
# NOT reports: sorting by filename let "growth-diagnostic-2026-06-16.json" sort after
# "growth-2026-09-09.json" and be picked as the latest report (#103, #65, #40 review).
REPORT_NAME = re.compile(r"^growth-(\d{4}-\d{2}-\d{2})\.json$")


def report_date(path: Path) -> str | None:
    m = REPORT_NAME.match(path.name)
    return m.group(1) if m else None


def load_reports(limit: int = 30) -> list[dict[str, Any]]:
    """Dated growth-YYYY-MM-DD.json snapshots, oldest → newest by DATE (not filename)."""
    dated = []
    for path in REPORTS_DIR.glob("growth-*.json"):
        day = report_date(path)
        if day is None:
            continue
        data = load_json(path)
        if not isinstance(data.get("metrics"), dict):
            continue
        data["_path"] = str(path.relative_to(ROOT))
        data["_date"] = day
        dated.append(data)
    dated.sort(key=lambda r: r["_date"])
    return dated[-limit:]


def unique_days(reports: list[dict[str, Any]]) -> int:
    return len({r["_date"] for r in reports if r.get("_date")})


def metric_value(report: dict[str, Any], name: str) -> Any:
    return ((report.get("metrics") or {}).get(name) or {}).get("value")


# @MX:WARN: [AUTO] main — growth-transition readiness evaluation; high branching
# @MX:REASON: Cyclomatic complexity 18; evaluates multiple metric thresholds to decide transition readiness. Incorrect branching yields a wrong readiness verdict (false go/no-go on autonomous growth).
def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate growth transition readiness.")
    parser.add_argument("--output", help="Optional output JSON path.")
    parser.add_argument("--min-valid-days", type=int, default=30)
    args = parser.parse_args()

    reports = load_reports(limit=max(args.min_valid_days, 30))
    trigger_cfg = load_json(TRIGGER_CONFIG) if TRIGGER_CONFIG.exists() else {}
    # A report counts as valid evidence only when ingestion was complete: #103's
    # collection_incomplete flag (partial page walk / API total not reached) must not feed
    # form_transfer / threshold readiness (#65 review: 30 incomplete days read as ready).
    valid_reports = [
        report for report in reports
        if int(report.get("messages_scanned") or 0) > 0
        and ((report.get("ingestion_diagnostics") or {}).get("empty_cause") in (None, "metrics_input_available"))
        and not (report.get("ingestion_diagnostics") or {}).get("collection_incomplete")
    ]
    latest_incomplete = bool(((reports[-1] if reports else {}).get("ingestion_diagnostics") or {}).get("collection_incomplete"))
    latest = reports[-1] if reports else {}
    # #65: `null_thresholds` 가 비었다는 것만 보면 두 경우가 통과한다.
    #   (1) 트리거가 **하나도 없을 때** — 빈 목록에는 null 이 없으므로 공허하게 참이 된다
    #   (2) threshold 가 `"invalid"` 같은 **비수치 값**일 때 — None 이 아니므로 정의된 것으로 센다
    # 둘 다 "임계값 정책이 정해졌다" 는 근거가 되지 못하는데 form_ready 를 열어 준다.
    # 그래서 존재·타입을 함께 본다.
    _triggers = trigger_cfg.get("triggers")
    triggers = _triggers if isinstance(_triggers, dict) else {}
    triggers_malformed = _triggers is not None and not isinstance(_triggers, dict)

    def _numeric(v: Any) -> bool:
        # NaN·Infinity 는 타입만 보면 통과하지만 임계값으로 쓸 수 없다 — 어떤 비교도
        # 의미가 없거나 항상 참/거짓이 된다. 유한성까지 본다.
        return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)

    thresholds_defined = [
        name for name, cfg in triggers.items()
        if isinstance(cfg, dict) and _numeric(cfg.get("threshold"))
    ]
    null_thresholds = [
        name for name, cfg in triggers.items()
        if not isinstance(cfg, dict) or cfg.get("threshold") is None
    ]
    invalid_thresholds = [
        name for name, cfg in triggers.items()
        if isinstance(cfg, dict) and cfg.get("threshold") is not None and not _numeric(cfg.get("threshold"))
    ]
    # 설정 계약이 고정한 네 트리거가 전부 있어야 한다. 임의의 키 하나로 통과하면
    # "정책이 정해졌다" 가 성립하지 않는다 — 나머지 셋은 여전히 미정이기 때문이다.
    missing_triggers = sorted(REQUIRED_TRIGGERS - set(triggers))
    # 각 트리거의 metric 이 **계약이 정한 지표와 정확히 일치**해야 한다.
    # `str(...)` 로 강제 변환하면 `metric: 123` 이나 엉뚱한 이름도 정상화돼 통과한다 —
    # 존재만 보지 말고 문자열 타입과 값을 함께 본다.
    triggers_without_metric = sorted(
        name for name, cfg in triggers.items()
        if isinstance(cfg, dict) and name in TRIGGER_METRIC_CONTRACT
        and cfg.get("metric") != TRIGGER_METRIC_CONTRACT[name]
    )
    # 트리거가 없거나 설정 자체가 잘못된 형태면 "정책 정의됨" 이라 부르지 않는다.
    thresholds_usable = (
        bool(triggers) and not triggers_malformed
        and not null_thresholds and not invalid_thresholds
        and not missing_triggers and not triggers_without_metric
    )

    latest_absence = ((latest.get("metrics") or {}).get("absence_pattern_signals") or {})
    valid_days = unique_days(valid_reports)   # distinct dates, not file count
    form_conditions = {
        "valid_metrics_days": valid_days,
        "requires_valid_metrics_days": args.min_valid_days,
        "latest_messages_scanned": latest.get("messages_scanned", 0),
        "latest_empty_cause": (latest.get("ingestion_diagnostics") or {}).get("empty_cause"),
        "latest_collection_incomplete": latest_incomplete,
        "thresholds_defined": thresholds_defined,
        "null_thresholds": null_thresholds,
        "invalid_thresholds": invalid_thresholds,
        "missing_triggers": missing_triggers,
        "triggers_without_metric": triggers_without_metric,
        "triggers_defined": len(triggers),
        "thresholds_usable": thresholds_usable,
    }
    form_ready = (
        not latest_incomplete
        and valid_days >= args.min_valid_days
        and thresholds_usable
        and metric_value(latest, "correction_rate") is not None
        and metric_value(latest, "first_pass_match_accuracy") is not None
        and metric_value(latest, "escalation_precision") is not None
    )

    specialist_review_ready = (
        int(latest_absence.get("value") or 0) > 0
        and int(latest.get("messages_scanned") or 0) > 0
    )

    # #103: reports/*.json 은 .gitignore(277행) 대상이라 **수집 호스트(T3610) 로컬 산출물**이다.
    # 다른 호스트(raspi5p 등)에서 이 스크립트를 돌리면 리포트가 0건이라 "blocked" 로 보이지만
    # 그것은 성장 정체가 아니라 **호스트를 잘못 고른 것**이다. 0건일 때 그 사실을 결과에 명시한다.
    no_reports_hint = None
    if not reports:
        no_reports_hint = (
            f"reports/growth-*.json 0건 — {REPORTS_DIR} 에 스냅샷이 없다. 이 파일들은 .gitignore 대상이라 "
            "git 으로 동기화되지 않으며 growth-metrics 를 실행하는 호스트(T3610)에만 존재한다. "
            "다른 호스트에서 실행했다면 이 결과는 성장 증거 부족이 아니라 호스트 불일치다 (#103)."
        )

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "reports_loaded": len(reports),
        "no_reports_hint": no_reports_hint,
        "valid_reports": len(valid_reports),
        "valid_metrics_days": valid_days,
        "latest_report": latest.get("_path"),
        "latest_report_date": latest.get("_date"),
        "threshold_policy": {
            "ready_for_definition": len(valid_reports) > 0,
            "status": "ready_for_human_policy" if len(valid_reports) > 0 else "blocked_by_metrics_ingestion",
            "thresholds_defined": thresholds_defined,
            "null_thresholds": null_thresholds,
            "invalid_thresholds": invalid_thresholds,
            "missing_triggers": missing_triggers,
            "triggers_without_metric": triggers_without_metric,
            "triggers_defined": len(triggers),
            "thresholds_usable": thresholds_usable,
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
