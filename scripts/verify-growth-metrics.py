#!/usr/bin/env python3
"""Focused contract checks for scripts/growth-metrics.py."""

from __future__ import annotations

import importlib.util
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MODULE_PATH = ROOT / "scripts" / "growth-metrics.py"


def load_module():
    spec = importlib.util.spec_from_file_location("growth_metrics", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load growth-metrics.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    gm = load_module()
    since = datetime(2026, 6, 16, 0, 0, tzinfo=timezone.utc)
    until = datetime(2026, 6, 16, 23, 59, tzinfo=timezone.utc)
    messages = {
        "mail-triage-fixture": [
            {
                "content": (
                    '{"ts":"2026-06-16T01:00:00+00:00","type":"mail_triaged",'
                    '"payload":{"actor":"ra_us","decision_ref":"D1","confidence":0.8,'
                    '"has_past_context":true,"comment":"FDA 510(k) cybersecurity review"}}'
                ),
                "metadata": {"record_type": "mail_triaged", "actor": "ra_us", "peer_id": "ra_us"},
                "peer_name": "ra_us",
            },
            {
                "content": (
                    '{"ts":"2026-06-16T02:00:00+00:00","type":"score_given",'
                    '"payload":{"decision_ref":"D1","score":3,'
                    '"dimensions":{"match_correct":true},"delta":{"self_correction":false}}}'
                ),
                "metadata": {"record_type": "score_given", "has_dimensions": True, "actor": "human"},
                "peer_name": "ra_us",
            },
            {
                "content": (
                    '{"ts":"2026-06-16T03:00:00+00:00","type":"yellow_gate",'
                    '"payload":{"yellow_reason":"low_confidence","comment":"clinical evaluation CER gap"}}'
                ),
                "metadata": {"record_type": "yellow_gate", "actor": "ra_eu"},
                "peer_name": "ra_eu",
            },
        ],
        "study-fixture": [
            {
                "content": (
                    '{"ts":"2026-06-16T04:00:00+00:00","type":"study_insight",'
                    '"payload":{"actor":"ra_kr","topic":"KGMP CAPA","source":"fixture"}}'
                ),
                "metadata": {"record_type": "study_insight", "actor": "ra_kr", "peer_id": "ra_kr"},
                "peer_name": "ra_kr",
            }
        ],
    }

    contract = gm.record_contract_diagnostics(messages, since, until)
    assert contract["expected_records_found"] >= 3
    assert contract["messages_in_window"] == 4
    assert contract["peer_counts"]["ra_us"] == 2
    # Baseline: all JSON-content fixtures parse cleanly.
    assert contract["content_parse_failures"] == 0, (
        f"JSON fixtures must not trigger parse failures, got {contract['content_parse_failures']}"
    )

    # P1 (#97) regression guard: plain-text content carrying a metadata.record_type
    # is an intentional clean-text record (daily_growth_case, study_insight,
    # ra_advisory*, curriculum_seed) and must NOT count as a parse failure. Only
    # non-JSON content with no metadata type is a genuine failure. Reverting the
    # record_contract_diagnostics text-content fix would make this assert fail.
    text_records = {
        "growth-session": [
            {
                "content": "Daily regulatory growth case\nGrowth version: daily_growth_v1\n",
                "metadata": {"record_type": "daily_growth_case", "actor": "ra_kr", "peer_id": "ra_kr"},
                "peer_name": "ra_kr",
            },
            {
                "content": "free-form text with no metadata record_type",
                "metadata": {},
                "peer_name": "ra_us",
            },
        ],
    }
    text_contract = gm.record_contract_diagnostics(text_records, since, until)
    assert text_contract["content_parse_failures"] == 1, (
        f"expected exactly 1 genuine failure (no-record_type text), "
        f"got {text_contract['content_parse_failures']} — clean-text records with "
        "metadata.record_type must not be counted as parse failures"
    )
    assert text_contract["record_type_counts"]["daily_growth_case"] == 1, (
        "clean-text daily_growth_case must still be classified via metadata.record_type"
    )

    cause = gm.classify_empty_cause(2, 2, 2, 0, 4, contract)
    assert cause == "metrics_input_available"

    accuracy = gm.compute_first_pass_match_accuracy(messages, since, until)
    assert accuracy["value"] == 1.0

    calibration = gm.compute_confidence_calibration(messages, since, until)
    assert calibration["n_pairs"] == 1

    absence = gm.compute_absence_pattern_signals(messages, since, until)
    assert absence["yellow_total"] == 1
    assert absence["yellow_by_domain"]["clinical_evaluation"] == 1

    no_session_cause = gm.classify_empty_cause(0, 0, 0, 0, 0, {
        "messages_in_window": 0,
        "expected_records_found": 0,
        "expected_activity_found": 0,
    })
    assert no_session_cause == "no_sessions_returned"

    # H1 (#80): window timezone — UTC → KST(Asia/Seoul) midnight alignment.
    # Regression guard: reverting OPERATION_TZ to UTC would re-split a KST day.
    from datetime import timedelta
    from zoneinfo import ZoneInfo

    assert isinstance(gm.OPERATION_TZ, ZoneInfo), "OPERATION_TZ must be ZoneInfo"
    assert str(gm.OPERATION_TZ) == "Asia/Seoul", f"expected Asia/Seoul, got {gm.OPERATION_TZ}"
    cron_until = datetime(2026, 6, 23, 2, 0, 0, tzinfo=gm.OPERATION_TZ)  # KST 02:00 timer fire
    since = (cron_until - timedelta(days=1)).replace(hour=0, minute=0, second=0)
    assert since.hour == 0 and since.utcoffset().total_seconds() == 9 * 3600
    assert since.strftime("%Y-%m-%d") == "2026-06-22"

    print("growth-metrics contract OK")


if __name__ == "__main__":
    main()
