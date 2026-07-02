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
import time
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Literal
from zoneinfo import ZoneInfo

import requests

# ---------------------------------------------------------------------------
# Configuration & Logging
# ---------------------------------------------------------------------------

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/growth-metrics-errors.log'),
        logging.StreamHandler(sys.stderr)
    ]
)
logger = logging.getLogger(__name__)

# Operation timezone for window boundaries. Growth activity is measured in KST
# business days; UTC midnights would split a KST day and mis-align the window.
OPERATION_TZ = ZoneInfo(os.environ.get("GROWTH_OPERATION_TZ", "Asia/Seoul"))

# Retry configuration
MAX_RETRIES = int(os.environ.get("GROWTH_METRICS_MAX_RETRIES", "3"))
RETRY_DELAY = float(os.environ.get("GROWTH_METRICS_RETRY_DELAY", "1.0"))
API_TIMEOUT = int(os.environ.get("GROWTH_METRICS_TIMEOUT", "30"))

# Honcho configuration
HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WORKSPACE", "work")
REPO_ROOT = Path(__file__).parent.parent
REPORTS_DIR = REPO_ROOT / "reports"
TRIGGER_CONFIG = REPO_ROOT / "feedback" / "config" / "growth-trigger-config.json"
EXPECTED_GROWTH_RECORD_TYPES = {
    "score_given",
    "mail_triaged",
    "ra_analysis",
    "study_session_complete",
    "study_insight",
}
EXPECTED_ACTIVITY_TYPES = {
    "score_given",
    "mail_received",
    "matched",
    "comment_added",
    "transition_proposed",
    "escalated",
    "escalation_requested",
    "study_session_complete",
    "study_insight",
}

# Enhanced error tracking
API_ERRORS: list[dict] = []

# Error classification for better diagnostics
class ErrorType:
    TRANSIENT = "transient"  # Temporary network issues, timeouts
    PERMANENT = "permanent"  # Auth errors, 404, invalid data
    UNKNOWN = "unknown"  # Uncategorized errors

# @MX:ANCHOR: Critical error classification function used by all retry logic
# @MX:REASON: Called by honcho_get() and honcho_post() to determine retry strategy
def classify_error(exc: requests.RequestException) -> str:
    """Classify error as transient, permanent, or unknown."""
    if isinstance(exc, requests.Timeout):
        return ErrorType.TRANSIENT
    elif isinstance(exc, requests.ConnectionError):
        return ErrorType.TRANSIENT
    elif isinstance(exc, requests.HTTPError):
        status_code = getattr(exc.response, 'status_code', 0)
        if 500 <= status_code < 600:
            return ErrorType.TRANSIENT  # Server errors - retry
        elif 400 <= status_code < 500:
            return ErrorType.PERMANENT  # Client errors - don't retry
        return ErrorType.UNKNOWN
    return ErrorType.UNKNOWN

ABSENCE_DOMAINS = {
    "clinical_evaluation": ["cer", "clinical", "임상", "clinical evaluation", "clinical trial"],
    "quality_capa": ["qms", "capa", "audit", "kgmp", "품질", "시정", "예방조치", "감사"],
    "pms_vigilance": ["pms", "pmcf", "fsca", "vigilance", "시판후", "안전성 정보"],
    "cybersecurity": ["cyber", "524b", "mdcg 2019-16", "mdcg 2021-6", "보안", "사이버"],
    "coordination": ["multi-region", "multi_region", "yellow_multi_region", "조율", "coordination"],
}


# ---------------------------------------------------------------------------
# Honcho query helpers
# ---------------------------------------------------------------------------

# @MX:WARN: Retry logic with exponential backoff and error classification
# @MX:REASON: Complex retry logic (Cyclomatic complexity > 15) with error type classification
def honcho_get(path: str, params: dict | None = None) -> dict | list | None:
    """GET request with retry logic for transient errors."""
    url = f"{HONCHO_URL}/v3/workspaces/{HONCHO_WS}{path}"

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(url, params=params, timeout=API_TIMEOUT)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as exc:
            error_type = classify_error(exc)

            # Don't retry permanent errors
            if error_type == ErrorType.PERMANENT:
                logger.error(f"GET {path} failed (permanent): {exc}")
                API_ERRORS.append({
                    "method": "GET",
                    "path": path,
                    "params": params or {},
                    "error": str(exc),
                    "error_type": error_type,
                    "attempts": attempt + 1,
                })
                return None

            # Log and retry for transient errors
            if attempt < MAX_RETRIES - 1:
                logger.warning(f"GET {path} failed (attempt {attempt + 1}/{MAX_RETRIES}): {exc} - retrying...")
                time.sleep(RETRY_DELAY * (2 ** attempt))  # Exponential backoff
            else:
                # Final attempt failed
                logger.error(f"GET {path} failed after {MAX_RETRIES} attempts: {exc}")
                API_ERRORS.append({
                    "method": "GET",
                    "path": path,
                    "params": params or {},
                    "error": str(exc),
                    "error_type": error_type,
                    "attempts": MAX_RETRIES,
                })

    return None


# @MX:WARN: POST retry logic with exponential backoff and error classification
# @MX:REASON: Complex retry logic (Cyclomatic complexity > 15) with error type classification
def honcho_post(path: str, body: dict) -> dict | None:
    """POST request with retry logic for transient errors."""
    url = f"{HONCHO_URL}/v3/workspaces/{HONCHO_WS}{path}"

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.post(url, json=body, timeout=API_TIMEOUT)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as exc:
            error_type = classify_error(exc)

            # Don't retry permanent errors
            if error_type == ErrorType.PERMANENT:
                logger.error(f"POST {path} failed (permanent): {exc}")
                API_ERRORS.append({
                    "method": "POST",
                    "path": path,
                    "body": body,
                    "error": str(exc),
                    "error_type": error_type,
                    "attempts": attempt + 1,
                })
                return None

            # Log and retry for transient errors
            if attempt < MAX_RETRIES - 1:
                logger.warning(f"POST {path} failed (attempt {attempt + 1}/{MAX_RETRIES}): {exc} - retrying...")
                time.sleep(RETRY_DELAY * (2 ** attempt))  # Exponential backoff
            else:
                # Final attempt failed
                logger.error(f"POST {path} failed after {MAX_RETRIES} attempts: {exc}")
                API_ERRORS.append({
                    "method": "POST",
                    "path": path,
                    "body": body,
                    "error": str(exc),
                    "error_type": error_type,
                    "attempts": MAX_RETRIES,
                })

    return None


def list_sessions(limit: int = 200) -> list[dict]:
    result = honcho_post("/sessions/list", {"page": 1, "page_size": limit, "size": limit})
    if isinstance(result, dict):
        items = result.get("items", result.get("sessions", result.get("data", [])))
        return items if isinstance(items, list) else []
    return result or []


def list_messages(session_id: str, limit: int = 500) -> list[dict]:
    result = honcho_post(
        f"/sessions/{session_id}/messages/list",
        {"page": 1, "page_size": limit, "size": limit},
    )
    if isinstance(result, dict):
        items = result.get("items", result.get("messages", result.get("data", [])))
        return items if isinstance(items, list) else []
    return result or []


def session_identifier(session: dict) -> str:
    for key in ("id", "name", "session_id"):
        value = session.get(key)
        if value:
            return str(value)
    return ""


# ---------------------------------------------------------------------------
# Message parsing helpers
# ---------------------------------------------------------------------------

def parse_activity_log(msg: dict) -> dict | None:
    """Parse a Honcho message with type=activity_log into structured data."""
    meta = msg.get("metadata") or {}
    if meta.get("type") != "activity_log":
        return None

    content_raw = msg.get("content", "")
    if not content_raw:
        logger.debug(f"Empty content in activity_log message (session: {msg.get('peer_name', 'unknown')})")
        return None

    try:
        content = json.loads(content_raw)
        return content
    except json.JSONDecodeError as exc:
        logger.warning(f"JSON decode error in activity_log: {exc}")
        logger.debug(f"Content preview: {content_raw[:200]}")
        return None
    except TypeError as exc:
        logger.warning(f"Invalid content type in activity_log: {exc}")
        return None


def parse_content(msg: dict) -> dict:
    """Parse message content with enhanced error tracking."""
    content_raw = msg.get("content", "")
    if not content_raw:
        return {}

    try:
        content = json.loads(content_raw)
        return content if isinstance(content, dict) else {}
    except json.JSONDecodeError as exc:
        logger.debug(f"JSON decode error: {exc} in message from {msg.get('peer_name', 'unknown')}")
        return {}
    except TypeError as exc:
        logger.debug(f"Invalid content type: {exc}")
        return {}


def is_within_window(ts_str: str, since: datetime, until: datetime) -> bool:
    try:
        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        return since <= ts <= until
    except (ValueError, TypeError):
        return False


def record_contract_diagnostics(messages_by_session: dict[str, list[dict]],
                                since: datetime, until: datetime) -> dict:
    record_type_counts: dict[str, int] = {}
    activity_type_counts: dict[str, int] = {}
    actor_counts: dict[str, int] = {}
    peer_counts: dict[str, int] = {}
    in_window = 0
    expected_records_found = 0
    expected_activity_found = 0
    parse_failures = 0
    unsupported_samples: list[dict] = []

    for session_id, msgs in messages_by_session.items():
        for msg in msgs:
            meta = msg.get("metadata") or {}
            record_type = str(meta.get("record_type") or meta.get("type") or "unclassified")
            record_type_counts[record_type] = record_type_counts.get(record_type, 0) + 1
            if record_type in EXPECTED_GROWTH_RECORD_TYPES:
                expected_records_found += 1

            content = parse_content(msg)
            # Plain-text content carrying a metadata record_type is an
            # intentional clean-text record (daily_growth_case, study_insight,
            # ra_advisory*, curriculum_seed) — NOT a parse failure. Only count
            # genuine parse failures: non-empty content that is neither valid
            # JSON nor backed by a metadata record_type.
            content_raw = msg.get("content") or ""
            if not content and content_raw and record_type == "unclassified":
                parse_failures += 1
            activity_type = str(content.get("type") or "unclassified")
            activity_type_counts[activity_type] = activity_type_counts.get(activity_type, 0) + 1
            if activity_type in EXPECTED_ACTIVITY_TYPES:
                expected_activity_found += 1

            ts = content.get("ts") or meta.get("ts") or meta.get("created_at") or msg.get("created_at")
            if ts and is_within_window(str(ts), since, until):
                in_window += 1

            actor = (
                meta.get("actor")
                or meta.get("peer_id")
                or content.get("actor")
                or (content.get("payload") or {}).get("actor")
                or "unknown"
            )
            actor_counts[str(actor)] = actor_counts.get(str(actor), 0) + 1

            peer = (
                msg.get("peer_name")
                or msg.get("peer_id")
                or meta.get("peer_id")
                or meta.get("actor")
                or "unknown"
            )
            peer_counts[str(peer)] = peer_counts.get(str(peer), 0) + 1

            if (
                len(unsupported_samples) < 5
                and record_type not in EXPECTED_GROWTH_RECORD_TYPES
                and activity_type not in EXPECTED_ACTIVITY_TYPES
            ):
                unsupported_samples.append({
                    "session": session_id,
                    "record_type": record_type,
                    "activity_type": activity_type,
                    "metadata_keys": sorted(meta.keys())[:12],
                    "content_prefix": str(msg.get("content", ""))[:120],
                })

    return {
        "expected_record_types": sorted(EXPECTED_GROWTH_RECORD_TYPES),
        "expected_activity_types": sorted(EXPECTED_ACTIVITY_TYPES),
        "record_type_counts": dict(sorted(record_type_counts.items())),
        "activity_type_counts": dict(sorted(activity_type_counts.items())),
        "expected_records_found": expected_records_found,
        "expected_activity_found": expected_activity_found,
        "messages_in_window": in_window,
        "content_parse_failures": parse_failures,
        "actor_counts": dict(sorted(actor_counts.items())),
        "peer_counts": dict(sorted(peer_counts.items())),
        "unsupported_samples": unsupported_samples,
    }


def classify_empty_cause(sessions_listed: int,
                         sessions_with_messages: int,
                         message_fetch_attempts: int,
                         message_fetch_failures: int,
                         total_messages: int,
                         contract: dict) -> str:
    if API_ERRORS and sessions_listed == 0:
        return "api_unreachable_or_auth_failed"
    if sessions_listed == 0:
        return "no_sessions_returned"
    if message_fetch_attempts > 0 and message_fetch_failures == message_fetch_attempts:
        return "message_fetch_failed"
    if sessions_with_messages == 0:
        return "sessions_returned_but_no_messages"
    if total_messages == 0:
        return "no_messages_loaded"
    if contract.get("messages_in_window", 0) == 0:
        return "messages_loaded_but_none_in_window"
    if (
        contract.get("expected_records_found", 0) == 0
        and contract.get("expected_activity_found", 0) == 0
    ):
        return "messages_loaded_but_no_supported_growth_records"
    return "metrics_input_available"


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
# Metric 6: autonomous_study_sessions
# Count study sessions recorded by autonomous-study-scheduler per agent
# ---------------------------------------------------------------------------

def compute_autonomous_study_sessions(messages_by_session: dict[str, list[dict]],
                                       since: datetime, until: datetime) -> dict:
    """
    Count autonomous study sessions (type=study_session_complete) per agent within window.
    autonomous_study_sessions = total study sessions completed by all agents.
    """
    total = 0
    by_agent: dict[str, int] = {}
    samples: list[dict] = []

    for session_id, msgs in messages_by_session.items():
        if "study" not in session_id:
            continue
        for msg in msgs:
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            ts = content.get("ts", "")
            if not is_within_window(ts, since, until):
                continue
            if content.get("type") != "study_session_complete":
                continue
            payload = content.get("payload", {})
            actor = payload.get("actor", content.get("actor", "unknown"))
            total += 1
            by_agent[actor] = by_agent.get(actor, 0) + 1
            if len(samples) < 5:
                samples.append({
                    "session": session_id,
                    "actor": actor,
                    "chunks_studied": payload.get("chunks_studied", 0),
                    "insights_recorded": payload.get("insights_recorded", 0),
                    "ts": ts,
                })

    return {
        "value": total,
        "numerator": total,
        "denominator": None,
        "by_agent": by_agent,
        "samples": samples,
        "direction": "up",
        "note": "autonomous study sessions completed by all RA agents (higher = more self-study)",
    }


# ---------------------------------------------------------------------------
# Metric 7: study_insights_count
# Count unique insights extracted and stored during autonomous study
# ---------------------------------------------------------------------------

def compute_study_insights_count(messages_by_session: dict[str, list[dict]],
                                  since: datetime, until: datetime) -> dict:
    """
    Count insight records (type=study_insight) deposited to Honcho during autonomous study.
    study_insights_count = total insight entries created within window.
    """
    total = 0
    by_agent: dict[str, int] = {}
    samples: list[dict] = []

    for session_id, msgs in messages_by_session.items():
        if "study" not in session_id:
            continue
        for msg in msgs:
            try:
                content = json.loads(msg.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                continue
            ts = content.get("ts", "")
            if not is_within_window(ts, since, until):
                continue
            if content.get("type") != "study_insight":
                continue
            payload = content.get("payload", {})
            actor = payload.get("actor", content.get("actor", "unknown"))
            total += 1
            by_agent[actor] = by_agent.get(actor, 0) + 1
            if len(samples) < 5:
                samples.append({
                    "session": session_id,
                    "actor": actor,
                    "topic": payload.get("topic", ""),
                    "source": payload.get("source", ""),
                    "ts": ts,
                })

    return {
        "value": total,
        "numerator": total,
        "denominator": None,
        "by_agent": by_agent,
        "samples": samples,
        "direction": "up",
        "note": "knowledge insights extracted during autonomous study (higher = richer knowledge base)",
    }


# ---------------------------------------------------------------------------
# Metric 8: absence_pattern_signals
# Early signal for #41 specialist-agent expansion decisions
# ---------------------------------------------------------------------------

def classify_absence_domain(text: str) -> str:
    lowered = text.lower()
    for domain, keywords in ABSENCE_DOMAINS.items():
        if any(keyword.lower() in lowered for keyword in keywords):
            return domain
    return "unclassified"


def compute_absence_pattern_signals(messages_by_session: dict[str, list[dict]],
                                     since: datetime, until: datetime) -> dict:
    yellow_by_domain: dict[str, int] = {}
    correction_by_domain: dict[str, int] = {}
    total_yellow = 0
    total_corrections = 0
    samples: list[dict] = []

    for session_id, msgs in messages_by_session.items():
        for msg in msgs:
            meta = msg.get("metadata") or {}
            content = parse_content(msg)
            ts = content.get("ts") or meta.get("ts") or msg.get("created_at") or ""
            if ts and not is_within_window(str(ts), since, until):
                continue
            payload = content.get("payload") or {}
            searchable = " ".join([
                str(content.get("type", "")),
                str(content.get("yellow_reason", "")),
                str(payload.get("yellow_reason", "")),
                str(payload.get("reason", "")),
                str(payload.get("comment", "")),
                str(payload.get("subject", "")),
                str(payload.get("domain", "")),
                str(payload.get("category", "")),
                str(msg.get("content", ""))[:500],
            ])
            domain = classify_absence_domain(searchable)

            yellow_reason = payload.get("yellow_reason") or content.get("yellow_reason")
            is_yellow = bool(yellow_reason) or content.get("type") in ("yellow_gate", "escalated", "escalation_requested")
            if is_yellow:
                total_yellow += 1
                yellow_by_domain[domain] = yellow_by_domain.get(domain, 0) + 1

            is_correction = (
                meta.get("record_type") == "score_given"
                and (payload.get("delta") or {}).get("self_correction") is True
            )
            if is_correction:
                total_corrections += 1
                correction_by_domain[domain] = correction_by_domain.get(domain, 0) + 1

            if len(samples) < 5 and (is_yellow or is_correction):
                samples.append({
                    "session": session_id,
                    "domain": domain,
                    "yellow_reason": yellow_reason,
                    "record_type": meta.get("record_type"),
                    "type": content.get("type"),
                })

    strongest_domain = None
    if yellow_by_domain or correction_by_domain:
        combined: dict[str, int] = {}
        for domain, count in yellow_by_domain.items():
            combined[domain] = combined.get(domain, 0) + count
        for domain, count in correction_by_domain.items():
            combined[domain] = combined.get(domain, 0) + count
        strongest_domain = max(combined, key=combined.get)

    return {
        "value": total_yellow + total_corrections,
        "yellow_total": total_yellow,
        "correction_total": total_corrections,
        "yellow_by_domain": dict(sorted(yellow_by_domain.items())),
        "correction_by_domain": dict(sorted(correction_by_domain.items())),
        "strongest_domain": strongest_domain,
        "domains": sorted(ABSENCE_DOMAINS.keys()),
        "samples": samples,
        "direction": "diagnostic",
        "note": "early absence-pattern signal for specialist expansion; not an auto-create trigger",
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def compute_metrics(since: datetime, until: datetime) -> dict:
    API_ERRORS.clear()
    print(f"Querying Honcho: {HONCHO_URL}/v3/workspaces/{HONCHO_WS}", flush=True)
    print(f"  window: {since.date()} → {until.date()}", flush=True)

    sessions = list_sessions(limit=500)
    print(f"  sessions found: {len(sessions)}", flush=True)

    messages_by_session: dict[str, list[dict]] = {}
    sessions_without_id = 0
    message_fetch_attempts = 0
    message_fetch_failures = 0
    session_samples: list[dict] = []
    for session in sessions:
        sid = session_identifier(session)
        if not sid:
            sessions_without_id += 1
            continue
        if len(session_samples) < 5:
            session_samples.append({
                "id": sid,
                "keys": sorted(session.keys())[:12],
                "metadata": session.get("metadata") or {},
            })
        before_errors = len(API_ERRORS)
        message_fetch_attempts += 1
        msgs = list_messages(sid, limit=500)
        if len(API_ERRORS) > before_errors:
            message_fetch_failures += 1
        if msgs:
            messages_by_session[sid] = msgs

    total_messages = sum(len(v) for v in messages_by_session.values())
    print(f"  messages loaded: {total_messages}", flush=True)
    contract = record_contract_diagnostics(messages_by_session, since, until)
    empty_cause = classify_empty_cause(
        sessions_listed=len(sessions),
        sessions_with_messages=len(messages_by_session),
        message_fetch_attempts=message_fetch_attempts,
        message_fetch_failures=message_fetch_failures,
        total_messages=total_messages,
        contract=contract,
    )

    metrics = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "window_start": since.isoformat(),
        "window_end": until.isoformat(),
        "honcho_url": HONCHO_URL,
        "workspace": HONCHO_WS,
        "sessions_listed": len(sessions),
        "sessions_scanned": len(messages_by_session),
        "sessions_with_messages": len(messages_by_session),
        "messages_scanned": total_messages,
        "ingestion_diagnostics": {
            "api_status": "failed" if API_ERRORS and len(sessions) == 0 else "partial_failure" if API_ERRORS else "ok",
            "api_errors": API_ERRORS[:10],
            "api_error_summary": {
                "total_errors": len(API_ERRORS),
                "transient_errors": sum(1 for e in API_ERRORS if e.get("error_type") == ErrorType.TRANSIENT),
                "permanent_errors": sum(1 for e in API_ERRORS if e.get("error_type") == ErrorType.PERMANENT),
                "unknown_errors": sum(1 for e in API_ERRORS if e.get("error_type") == ErrorType.UNKNOWN),
            },
            "sessions_listed": len(sessions),
            "sessions_without_id": sessions_without_id,
            "sessions_with_messages": len(messages_by_session),
            "message_fetch_attempts": message_fetch_attempts,
            "message_fetch_failures": message_fetch_failures,
            "empty_cause": empty_cause,
            "session_samples": session_samples,
            "record_contract": contract,
        },
        "metrics": {
            "correction_rate": compute_correction_rate(messages_by_session, since, until),
            "first_pass_match_accuracy": compute_first_pass_match_accuracy(messages_by_session, since, until),
            "confidence_calibration": compute_confidence_calibration(messages_by_session, since, until),
            "warmstart_lift": compute_warmstart_lift(messages_by_session, since, until),
            "escalation_precision": compute_escalation_precision(messages_by_session, since, until),
            "autonomous_study_sessions": compute_autonomous_study_sessions(messages_by_session, since, until),
            "study_insights_count": compute_study_insights_count(messages_by_session, since, until),
            "absence_pattern_signals": compute_absence_pattern_signals(messages_by_session, since, until),
        },
    }
    return metrics


# @MX:ANCHOR: [AUTO] check_and_notify_triggers — growth-trigger-config.json reader and webhook caller
# @MX:REASON: Called from main() after metrics save. Webhook is null-safe (no-op when unconfigured).
def check_and_notify_triggers(metrics: dict) -> None:
    """Check growth-trigger-config.json thresholds and POST to n8n webhook if met."""
    if not TRIGGER_CONFIG.exists():
        logger.debug(f"Trigger config not found: {TRIGGER_CONFIG}")
        return

    try:
        with open(TRIGGER_CONFIG, encoding="utf-8") as f:
            cfg = json.load(f)
    except (json.JSONDecodeError, IOError) as exc:
        logger.error(f"Failed to load trigger config: {exc}")
        return

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
        logger.warning("Webhook URL not configured - trigger notifications skipped")
        return

    payload = {
        "event": "growth_trigger_activated",
        "date": metrics.get("date", ""),
        "triggers": triggered,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # Enhanced webhook error handling with retry
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.post(webhook_url, json=payload, timeout=15)
            resp.raise_for_status()
            print(f"  n8n webhook 알림 전송: {webhook_url}", flush=True)
            logger.info(f"Webhook notification sent successfully to {webhook_url}")
            return
        except requests.RequestException as exc:
            error_type = classify_error(exc)

            if attempt < MAX_RETRIES - 1 and error_type == ErrorType.TRANSIENT:
                logger.warning(f"Webhook call failed (attempt {attempt + 1}/{MAX_RETRIES}): {exc} - retrying...")
                time.sleep(RETRY_DELAY)
            else:
                logger.error(f"Webhook notification failed after {MAX_RETRIES} attempts: {exc}")
                print(f"  Webhook 호출 실패 (영구적 오류 또는 재시도 초과): {exc}", flush=True)
                return


def main() -> None:
    # Ensure logs directory exists
    logs_dir = REPO_ROOT / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

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
        until = datetime.strptime(args.date, "%Y%m%d").replace(tzinfo=OPERATION_TZ)
        until = until.replace(hour=23, minute=59, second=59)
    else:
        until = datetime.now(OPERATION_TZ)

    since = (until - timedelta(days=args.days)).replace(hour=0, minute=0, second=0)

    logger.info(f"Starting growth metrics computation for window: {since.date()} → {until.date()}")
    metrics = compute_metrics(since, until)

    # Determine output path
    if args.output:
        out_path = Path(args.output)
    else:
        date_str = until.strftime("%Y-%m-%d")
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS_DIR / f"growth-{date_str}.json"

    # Write output with error handling
    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2, ensure_ascii=False)
        logger.info(f"Metrics successfully written to: {out_path}")
    except (IOError, OSError) as exc:
        logger.error(f"Failed to write metrics to {out_path}: {exc}")
        sys.exit(1)
    except Exception as exc:
        logger.error(f"Unexpected error writing metrics: {exc}")
        sys.exit(1)

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
