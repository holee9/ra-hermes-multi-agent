#!/usr/bin/env python3
"""
Growth Metrics Script (issue #24 GROWTH-5)

Queries Honcho work workspace to compute 5 daily growth indicators.
Output: reports/growth-YYYYMMDD.json

Metrics:
  correction_rate         - fraction of decisions overridden by humans
  first_pass_match_accuracy - match correctness on first human review
  confidence_calibration  - Brier score (confidence vs actual correct)
  warmstart_lift          - score diff: warm-context vs cold-context decisions
  escalation_precision    - fraction of escalations requiring actual human intervention

Usage:
  python3 scripts/growth-metrics.py [--date YYYYMMDD] [--days N]
  python3 scripts/growth-metrics.py --output reports/growth-2026-06-09.json

Environment variables:
  HONCHO_URL        - default: http://localhost:8000
  HONCHO_WORKSPACE  - default: work
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WORKSPACE", "work")
REPO_ROOT = Path(__file__).parent.parent
REPORTS_DIR = REPO_ROOT / "reports"
TRIGGER_CONFIG = REPO_ROOT / "feedback" / "config" / "growth-trigger-config.json"


# ---------------------------------------------------------------------------
# Honcho query helpers
# ---------------------------------------------------------------------------

def honcho_get(path: str, params: dict | None = None) -> dict | list | None:
    url = f"{HONCHO_URL}/v3/workspaces/{HONCHO_WS}{path}"
    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        print(f"  [warn] GET {path} failed: {exc}", file=sys.stderr)
        return None


def honcho_post(path: str, body: dict) -> dict | None:
    url = f"{HONCHO_URL}/v3/workspaces/{HONCHO_WS}{path}"
    try:
        resp = requests.post(url, json=body, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        print(f"  [warn] POST {path} failed: {exc}", file=sys.stderr)
        return None


def list_sessions(limit: int = 200) -> list[dict]:
    result = honcho_get("/sessions", params={"limit": limit})
    if isinstance(result, dict):
        return result.get("items", [])
    return result or []


def list_messages(session_id: str, limit: int = 500) -> list[dict]:
    result = honcho_get(f"/sessions/{session_id}/messages", params={"limit": limit})
    if isinstance(result, dict):
        return result.get("items", [])
    return result or []


# ---------------------------------------------------------------------------
# Message parsing helpers
# ---------------------------------------------------------------------------

def parse_activity_log(msg: dict) -> dict | None:
    """Parse a Honcho message with type=activity_log into structured data."""
    meta = msg.get("metadata") or {}
    if meta.get("type") != "activity_log":
        return None
    try:
        content = json.loads(msg.get("content", "{}"))
    except (json.JSONDecodeError, TypeError):
        return None
    return content


def is_within_window(ts_str: str, since: datetime, until: datetime) -> bool:
    try:
        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        return since <= ts <= until
    except (ValueError, TypeError):
        return False


# ---------------------------------------------------------------------------
# Metric 1: correction_rate
# Fraction of RA decisions where human changed match or transition
# ---------------------------------------------------------------------------

def compute_correction_rate(messages_by_session: dict[str, list[dict]],
                             since: datetime, until: datetime) -> dict:
    """
    Scan feedback sessions for score_given records that have delta.self_correction=True.
    correction_rate = self_correction_count / total_scored_count
    """
    total = 0
    corrected = 0
    samples: list[dict] = []

    for session_id, msgs in messages_by_session.items():
        if not session_id.endswith("-feedback-"):
            pass
        for msg in msgs:
            meta = msg.get("metadata") or {}
            if meta.get("record_type") != "score_given":
                continue
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            ts = content.get("ts", "")
            if not is_within_window(ts, since, until):
                continue
            payload = content.get("payload", {})
            total += 1
            delta = payload.get("delta") or {}
            if delta.get("self_correction") is True:
                corrected += 1
                samples.append({
                    "session": session_id,
                    "actor": payload.get("target_actor"),
                    "score": payload.get("score"),
                    "changed": delta.get("changed", {}),
                })

    rate = corrected / total if total > 0 else None
    return {
        "value": rate,
        "numerator": corrected,
        "denominator": total,
        "samples": samples[:5],
        "direction": "down",
        "note": "fraction of human-reviewed decisions where agent was overridden",
    }


# ---------------------------------------------------------------------------
# Metric 2: first_pass_match_accuracy
# match_correct=True fraction from dimensions field
# ---------------------------------------------------------------------------

def compute_first_pass_match_accuracy(messages_by_session: dict[str, list[dict]],
                                       since: datetime, until: datetime) -> dict:
    total = 0
    correct = 0

    for _, msgs in messages_by_session.items():
        for msg in msgs:
            meta = msg.get("metadata") or {}
            if meta.get("record_type") != "score_given":
                continue
            if not meta.get("has_dimensions"):
                continue
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            ts = content.get("ts", "")
            if not is_within_window(ts, since, until):
                continue
            payload = content.get("payload", {})
            dimensions = payload.get("dimensions") or {}
            match_correct = dimensions.get("match_correct")
            if match_correct is None:
                continue
            total += 1
            if match_correct is True:
                correct += 1

    rate = correct / total if total > 0 else None
    return {
        "value": rate,
        "numerator": correct,
        "denominator": total,
        "direction": "up",
        "note": "fraction of WP match decisions confirmed correct by human",
    }


# ---------------------------------------------------------------------------
# Metric 3: confidence_calibration (Brier score)
# Brier = mean((confidence - actual_correct)^2), lower is better
# ---------------------------------------------------------------------------

def compute_confidence_calibration(messages_by_session: dict[str, list[dict]],
                                    since: datetime, until: datetime) -> dict:
    """
    Look for mail_triaged messages that have both confidence and
    a corresponding feedback score_given in the same window.
    Match by decision_ref → session_id.
    """
    # Collect triaged decisions: decision_ref → {confidence, actor}
    triage_map: dict[str, dict] = {}
    for session_id, msgs in messages_by_session.items():
        for msg in msgs:
            meta = msg.get("metadata") or {}
            if meta.get("record_type") not in ("mail_triaged", "ra_analysis"):
                continue
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            ts = content.get("ts", "")
            if not is_within_window(ts, since, until):
                continue
            payload = content.get("payload", {})
            conf = payload.get("confidence")
            decision_ref = payload.get("decision_ref") or content.get("decision_ref")
            if conf is not None and decision_ref:
                triage_map[str(decision_ref)] = {
                    "confidence": float(conf),
                    "actor": payload.get("actor", ""),
                }

    # Collect feedback scores: decision_ref → match_correct
    feedback_map: dict[str, bool] = {}
    for _, msgs in messages_by_session.items():
        for msg in msgs:
            meta = msg.get("metadata") or {}
            if meta.get("record_type") != "score_given":
                continue
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            payload = content.get("payload", {})
            decision_ref = payload.get("decision_ref")
            dimensions = payload.get("dimensions") or {}
            match_correct = dimensions.get("match_correct")
            if decision_ref and match_correct is not None:
                feedback_map[str(decision_ref)] = match_correct

    # Compute Brier score for matched pairs
    brier_terms: list[float] = []
    for ref, triage in triage_map.items():
        if ref in feedback_map:
            conf = triage["confidence"]
            actual = 1.0 if feedback_map[ref] else 0.0
            brier_terms.append((conf - actual) ** 2)

    brier = sum(brier_terms) / len(brier_terms) if brier_terms else None
    return {
        "value": brier,
        "n_pairs": len(brier_terms),
        "direction": "zero",
        "note": "Brier score: mean((confidence - actual_correct)^2). Lower → better calibrated.",
    }


# ---------------------------------------------------------------------------
# Metric 4: warmstart_lift
# Score diff between decisions with warm context vs cold
# ---------------------------------------------------------------------------

def compute_warmstart_lift(messages_by_session: dict[str, list[dict]],
                            since: datetime, until: datetime) -> dict:
    """
    Look for mail_triaged messages with has_past_context flag.
    Compute mean score for warm vs cold and return the difference.
    """
    warm_scores: list[float] = []
    cold_scores: list[float] = []

    # Build score lookup by decision_ref from feedback
    score_by_ref: dict[str, int] = {}
    for _, msgs in messages_by_session.items():
        for msg in msgs:
            meta = msg.get("metadata") or {}
            if meta.get("record_type") != "score_given":
                continue
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            payload = content.get("payload", {})
            ref = payload.get("decision_ref")
            score = payload.get("score")
            if ref and score:
                score_by_ref[str(ref)] = int(score)

    # Match triage decisions with their feedback scores
    for _, msgs in messages_by_session.items():
        for msg in msgs:
            meta = msg.get("metadata") or {}
            if meta.get("record_type") not in ("mail_triaged", "ra_analysis"):
                continue
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            ts = content.get("ts", "")
            if not is_within_window(ts, since, until):
                continue
            payload = content.get("payload", {})
            ref = payload.get("decision_ref") or content.get("decision_ref")
            has_context = bool(payload.get("has_past_context", False))
            if ref and str(ref) in score_by_ref:
                sc = score_by_ref[str(ref)]
                if has_context:
                    warm_scores.append(sc)
                else:
                    cold_scores.append(sc)

    warm_mean = sum(warm_scores) / len(warm_scores) if warm_scores else None
    cold_mean = sum(cold_scores) / len(cold_scores) if cold_scores else None
    lift = (warm_mean - cold_mean) if (warm_mean is not None and cold_mean is not None) else None

    return {
        "value": lift,
        "warm_mean": warm_mean,
        "cold_mean": cold_mean,
        "warm_n": len(warm_scores),
        "cold_n": len(cold_scores),
        "direction": "positive",
        "note": "warm_mean - cold_mean (1-3 scale). Positive → memory helps.",
    }


# ---------------------------------------------------------------------------
# Metric 5: escalation_precision
# Fraction of escalations that actually needed human intervention
# ---------------------------------------------------------------------------

def compute_escalation_precision(messages_by_session: dict[str, list[dict]],
                                  since: datetime, until: datetime) -> dict:
    """
    Count escalation events and check which ones received human feedback (score 1 or 2).
    escalation_precision = escalations_requiring_intervention / total_escalations
    """
    escalations: list[str] = []
    intervention_refs: set[str] = set()

    for session_id, msgs in messages_by_session.items():
        for msg in msgs:
            meta = msg.get("metadata") or {}
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            ts = content.get("ts", "")
            if not is_within_window(ts, since, until):
                continue
            msg_type = content.get("type", "")
            payload = content.get("payload", {})

            if msg_type in ("escalated", "escalation_requested"):
                ref = payload.get("decision_ref") or session_id
                escalations.append(str(ref))

            # Human intervention: low score (1) or explicit comment feedback
            if meta.get("record_type") == "score_given":
                score = payload.get("score")
                ref = payload.get("decision_ref")
                if score == 1 and ref:
                    intervention_refs.add(str(ref))

    total_esc = len(escalations)
    actual_intervention = sum(1 for r in escalations if r in intervention_refs)
    precision = actual_intervention / total_esc if total_esc > 0 else None

    return {
        "value": precision,
        "numerator": actual_intervention,
        "denominator": total_esc,
        "direction": "up",
        "note": "fraction of escalations that required actual human correction (score=1)",
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def compute_metrics(since: datetime, until: datetime) -> dict:
    print(f"Querying Honcho: {HONCHO_URL}/v3/workspaces/{HONCHO_WS}", flush=True)
    print(f"  window: {since.date()} → {until.date()}", flush=True)

    sessions = list_sessions(limit=500)
    print(f"  sessions found: {len(sessions)}", flush=True)

    messages_by_session: dict[str, list[dict]] = {}
    for session in sessions:
        sid = session.get("id", "")
        if not sid:
            continue
        msgs = list_messages(sid, limit=500)
        if msgs:
            messages_by_session[sid] = msgs

    total_messages = sum(len(v) for v in messages_by_session.values())
    print(f"  messages loaded: {total_messages}", flush=True)

    metrics = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "window_start": since.isoformat(),
        "window_end": until.isoformat(),
        "honcho_url": HONCHO_URL,
        "workspace": HONCHO_WS,
        "sessions_scanned": len(messages_by_session),
        "messages_scanned": total_messages,
        "metrics": {
            "correction_rate": compute_correction_rate(messages_by_session, since, until),
            "first_pass_match_accuracy": compute_first_pass_match_accuracy(messages_by_session, since, until),
            "confidence_calibration": compute_confidence_calibration(messages_by_session, since, until),
            "warmstart_lift": compute_warmstart_lift(messages_by_session, since, until),
            "escalation_precision": compute_escalation_precision(messages_by_session, since, until),
        },
    }
    return metrics


# @MX:ANCHOR: [AUTO] check_and_notify_triggers — growth-trigger-config.json reader and webhook caller
# @MX:REASON: Called from main() after metrics save. Webhook is null-safe (no-op when unconfigured).
def check_and_notify_triggers(metrics: dict) -> None:
    """Check growth-trigger-config.json thresholds and POST to n8n webhook if met."""
    if not TRIGGER_CONFIG.exists():
        return

    with open(TRIGGER_CONFIG, encoding="utf-8") as f:
        cfg = json.load(f)

    webhook_url: str | None = cfg.get("notification", {}).get("n8n_webhook_url")
    triggers = cfg.get("triggers", {})
    metric_values = {name: data.get("value") for name, data in metrics.get("metrics", {}).items()}

    triggered = []
    for trigger_name, tdef in triggers.items():
        threshold = tdef.get("threshold")
        if threshold is None:
            continue
        metric_name = tdef.get("metric")
        direction = tdef.get("direction", "below")
        value = metric_values.get(metric_name)
        if value is None:
            continue
        met = (direction == "below" and value < threshold) or (direction == "above" and value > threshold)
        if met:
            triggered.append({
                "trigger": trigger_name,
                "metric": metric_name,
                "value": value,
                "threshold": threshold,
                "direction": direction,
                "next_action": tdef.get("next_action"),
            })

    if not triggered:
        return

    print("\n=== 성장 트리거 달성 ===", flush=True)
    for t in triggered:
        print(f"  [{t['trigger']}] {t['metric']}={t['value']:.3f} {t['direction']} {t['threshold']}", flush=True)

    if not webhook_url:
        print("  (n8n_webhook_url 미설정 — 알림 없음)", flush=True)
        return

    payload = {
        "event": "growth_trigger_activated",
        "date": metrics.get("date", ""),
        "triggers": triggered,
    }
    try:
        resp = requests.post(webhook_url, json=payload, timeout=15)
        resp.raise_for_status()
        print(f"  n8n webhook 알림 전송: {webhook_url}", flush=True)
    except requests.RequestException as e:
        print(f"  Webhook 호출 실패: {e}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute daily growth metrics from Honcho workspace."
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Target date YYYYMMDD (default: today).",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=1,
        help="Number of days to look back (default: 1).",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output JSON path (default: reports/growth-YYYYMMDD.json).",
    )
    args = parser.parse_args()

    if args.date:
        until = datetime.strptime(args.date, "%Y%m%d").replace(tzinfo=timezone.utc)
        until = until.replace(hour=23, minute=59, second=59)
    else:
        until = datetime.now(timezone.utc)

    since = (until - timedelta(days=args.days)).replace(hour=0, minute=0, second=0)

    metrics = compute_metrics(since, until)

    # Determine output path
    if args.output:
        out_path = Path(args.output)
    else:
        date_str = until.strftime("%Y-%m-%d")
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS_DIR / f"growth-{date_str}.json"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    print(f"\nOutput: {out_path}", flush=True)

    # Summary
    print("\n=== Growth Metrics Summary ===", flush=True)
    for name, data in metrics["metrics"].items():
        val = data.get("value")
        val_str = f"{val:.3f}" if val is not None else "N/A (no data yet)"
        n = data.get("denominator") or data.get("n_pairs") or data.get("warm_n", 0) + data.get("cold_n", 0)
        direction = data.get("direction", "")
        print(f"  {name}: {val_str}  (n={n}, target={direction})", flush=True)

    # Check growth triggers and notify if thresholds are met
    check_and_notify_triggers(metrics)


if __name__ == "__main__":
    main()
