#!/usr/bin/env python3
"""Render a standalone HTML growth dashboard from local report JSON files."""

from __future__ import annotations

import html
import json
import logging
import math
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/growth-dashboard-errors.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
OUTPUT = ROOT / "docs" / "growth-dashboard.html"
COVERAGE_GUARDS = ROOT / "scripts" / "coverage-guards.json"
GROWTH_TARGETS = ROOT / "scripts" / "growth-targets.json"


def load_json(path: Path) -> dict[str, Any] | None:
    """Load and parse JSON file with error handling."""
    try:
        content = path.read_text(encoding="utf-8")
        return json.loads(content)
    except OSError as e:
        logger.warning(f"File not found: {path} - {e}")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing failed for {path}: {e}")
        return None


def latest_json(paths: list[Path]) -> tuple[Path | None, dict[str, Any] | None]:
    existing = [path for path in paths if path.exists()]
    if not existing:
        return None, None
    latest = max(existing, key=lambda path: path.stat().st_mtime)
    return latest, load_json(latest)


def run(cmd: list[str]) -> str:
    """Run subprocess command with enhanced error handling."""
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
            timeout=30
        )
        result = (proc.stdout or proc.stderr).strip()

        if proc.returncode != 0:
            logger.debug(f"Command failed: {' '.join(cmd)} - return code: {proc.returncode}")

        return result
    except subprocess.TimeoutExpired as e:
        logger.error(f"Command timeout: {' '.join(cmd)} - {e}")
        return "timeout"
    except FileNotFoundError as e:
        logger.error(f"Command not found: {' '.join(cmd)} - {e}")
        return "not_found"


def fmt(value: Any, fallback: str = "-") -> str:
    if value is None or value == "":
        return fallback
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def esc(value: Any, fallback: str = "-") -> str:
    return html.escape(fmt(value, fallback))


def status_class(ok: bool | None) -> str:
    if ok is True:
        return "ok"
    if ok is False:
        return "bad"
    return "warn"


def collect_snapshot() -> dict[str, Any]:
    """Collect dashboard data with validation and error handling."""
    try:
        # Ensure reports directory exists
        if not REPORTS.exists():
            logger.warning(f"Reports directory not found: {REPORTS}")
            return {"error": "reports_directory_not_found", "generated_at": datetime.now().astimezone().isoformat()}

        readiness_path, readiness = latest_json(sorted((REPORTS / "auto-growth-readiness").glob("*.json")))
        growth_paths = sorted(REPORTS.glob("growth-*.json"))
        growth_reports = [(path, load_json(path)) for path in growth_paths]
        growth_reports = [(path, data) for path, data in growth_reports if data]
        latest_growth_path, latest_growth = latest_json(growth_paths)

        matrix = (readiness or {}).get("matrix", {})
        scores = matrix.get("scores", {})
        db = (readiness or {}).get("db", {})
        growth_metrics = (latest_growth or {}).get("metrics", {})
        coverage_guards = load_json(COVERAGE_GUARDS) or {}
        growth_targets = load_json(GROWTH_TARGETS) or {}

        hermes_timer_active = run(["systemctl", "is-active", "hermes-auto-growth.timer"])
        hermes_timer_enabled = run(["systemctl", "is-enabled", "hermes-auto-growth.timer"])
        metrics_timer_active = run(["systemctl", "is-active", "ra-growth-metrics.timer"])
        metrics_timer_enabled = run(["systemctl", "is-enabled", "ra-growth-metrics.timer"])

        trend_rows: list[dict[str, Any]] = []
        for path, data in growth_reports[-14:]:
            metrics = data.get("metrics", {})
            trend_rows.append({
                "file": path.name,
                "generated_at": data.get("generated_at"),
                "sessions_scanned": data.get("sessions_scanned"),
                "messages_scanned": data.get("messages_scanned"),
                "correction_rate": (metrics.get("correction_rate") or {}).get("value"),
                "first_pass_match_accuracy": (metrics.get("first_pass_match_accuracy") or {}).get("value"),
                "autonomous_study_sessions": (metrics.get("autonomous_study_sessions") or {}).get("value"),
                "study_insights_count": (metrics.get("study_insights_count") or {}).get("value"),
            })

        return {
            "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "readiness_file": readiness_path.name if readiness_path else None,
            "growth_file": latest_growth_path.name if latest_growth_path else None,
            "readiness": {
                "total_score": matrix.get("total_score"),
                "max_score": matrix.get("max_score"),
                "recommendation": matrix.get("timer_operation_recommendation"),
                "dimension_scores": {key: value.get("score") for key, value in scores.items()},
            },
            "timers": {
                "hermes_auto_growth": {"active": hermes_timer_active, "enabled": hermes_timer_enabled},
                "ra_growth_metrics": {"active": metrics_timer_active, "enabled": metrics_timer_enabled},
            },
            "cleanliness": (scores.get("data_cleanliness") or {}).get("checks", {}),
            "activation": (scores.get("activation_control") or {}).get("checks", {}),
            "self_docs": ((scores.get("agent_balance") or {}).get("self_docs") or db.get("self_docs") or {}),
            "seed_counts": (scores.get("growth_input_quality") or {}).get("seed_counts", {}),
            "growth_latest": {
                "generated_at": (latest_growth or {}).get("generated_at"),
                "sessions_scanned": (latest_growth or {}).get("sessions_scanned"),
                "messages_scanned": (latest_growth or {}).get("messages_scanned"),
                "metrics": {
                    key: {
                        "value": value.get("value"),
                        "direction": value.get("direction"),
                        "note": value.get("note"),
                    }
                    for key, value in growth_metrics.items()
                    if isinstance(value, dict)
                },
            },
            "trend_rows": trend_rows,
            "coverage_guards": coverage_guards,
            "growth_targets": growth_targets,
        }
    except Exception as e:
        logger.error(f"Failed to collect snapshot: {e}")
        return {"error": "snapshot_collection_failed", "generated_at": datetime.now().astimezone().isoformat()}


def render_metric_row(name: str, data: dict[str, Any]) -> str:
    value = data.get("value")
    cls = "warn" if value is None else "ok"
    return (
        "<tr>"
        f"<th>{esc(name)}</th>"
        f"<td><span class='pill {cls}'>{esc(value, 'N/A')}</span></td>"
        f"<td>{esc(data.get('direction'))}</td>"
        f"<td>{esc(data.get('note'))}</td>"
        "</tr>"
    )


def evidence_label(name: str) -> str:
    labels = {
        "knowledge_depth_proxy": "Knowledge Depth Proxy",
        "source_coverage": "Source Coverage",
        "safety_cleanliness": "Safety Cleanliness",
        "behavioral_metrics": "Behavioral Metrics",
        "human_feedback": "Human Feedback",
    }
    return labels.get(name, name)


def number(value: Any, fallback: float = 0.0) -> float:
    try:
        if value is None:
            return fallback
        return float(value)
    except (TypeError, ValueError):
        return fallback


def pct(value: float, denominator: float) -> float:
    if denominator <= 0:
        return 0.0
    return max(0.0, min(100.0, (value / denominator) * 100.0))


def evidence_scores(snapshot: dict[str, Any]) -> dict[str, float]:
    guards = snapshot.get("coverage_guards", {})
    expected_sources = (guards.get("source_coverage") or {}).get("expected_explicit_sources") or {}
    depth_floors = guards.get("self_doc_depth_floors") or {}
    self_docs = snapshot.get("self_docs", {})
    seed_counts = snapshot.get("seed_counts", {})
    growth_latest = snapshot.get("growth_latest", {})
    growth_targets = snapshot.get("growth_targets", {})
    target_metrics = ((growth_targets.get("phase2_dynamic_learning") or {}).get("metrics") or {})

    source_values = [
        min(1.0, number(seed_counts.get(agent)) / max(number(expected), 1.0))
        for agent, expected in expected_sources.items()
    ]
    source_coverage = (sum(source_values) / len(source_values)) if source_values else 0.0

    depth_values = [
        min(1.0, number(self_docs.get(agent)) / max(number(config.get("min")), 1.0))
        for agent, config in depth_floors.items()
        if isinstance(config, dict)
    ]
    depth_proxy = (sum(depth_values) / len(depth_values)) if depth_values else 0.0

    cleanliness_values = [1.0 if bool(value) else 0.0 for value in snapshot.get("cleanliness", {}).values()]
    safety_cleanliness = (sum(cleanliness_values) / len(cleanliness_values)) if cleanliness_values else 0.0

    sessions = number(growth_latest.get("sessions_scanned"))
    messages = number(growth_latest.get("messages_scanned"))
    metrics = growth_latest.get("metrics", {})
    behavior_values = []
    for metric_name, target in target_metrics.items():
        metric = metrics.get(metric_name) or {}
        value = metric.get("value")
        if value is None:
            behavior_values.append(0.0)
            continue
        metric_value = number(value)
        if "target_min" in target:
            behavior_values.append(1.0 if metric_value >= number(target.get("target_min")) else 0.0)
        elif "target_max" in target:
            behavior_values.append(1.0 if metric_value <= number(target.get("target_max")) else 0.0)
    behavioral_signal = 0.0 if sessions == 0 or messages == 0 else (
        (sum(behavior_values) / len(behavior_values)) if behavior_values else 0.0
    )

    min_feedback = number((growth_targets.get("phase2_dynamic_learning") or {}).get("min_feedback_coverage"))
    feedback_metric = metrics.get("human_feedback_coverage") or metrics.get("feedback_coverage") or {}
    feedback_value = feedback_metric.get("value")
    feedback_signal = 0.0
    if sessions > 0 and messages > 0 and feedback_value is not None:
        feedback_signal = min(1.0, number(feedback_value) / max(min_feedback, 0.01))

    return {
        "knowledge_depth_proxy": depth_proxy * 4,
        "source_coverage": source_coverage * 4,
        "safety_cleanliness": safety_cleanliness * 4,
        "behavioral_metrics": behavioral_signal * 4,
        "human_feedback": feedback_signal * 4,
    }


def radar_chart(scores: dict[str, Any], title: str) -> str:
    order = [
        ("knowledge_depth_proxy", "Depth"),
        ("source_coverage", "Sources"),
        ("safety_cleanliness", "Safety"),
        ("behavioral_metrics", "Behavior"),
        ("human_feedback", "Feedback"),
    ]
    cx = cy = 130
    radius = 86
    rings = []
    for step in range(1, 5):
        r = radius * step / 4
        points = []
        for idx in range(len(order)):
            angle = -math.pi / 2 + (math.tau * idx / len(order))
            points.append(f"{cx + math.cos(angle) * r:.1f},{cy + math.sin(angle) * r:.1f}")
        rings.append(f"<polygon points='{' '.join(points)}' class='radar-ring' />")

    axes = []
    labels = []
    values = []
    for idx, (key, label) in enumerate(order):
        angle = -math.pi / 2 + (math.tau * idx / len(order))
        end_x = cx + math.cos(angle) * radius
        end_y = cy + math.sin(angle) * radius
        label_x = cx + math.cos(angle) * (radius + 27)
        label_y = cy + math.sin(angle) * (radius + 27)
        score = number(scores.get(key))
        value_r = radius * max(0, min(4, score)) / 4
        values.append(f"{cx + math.cos(angle) * value_r:.1f},{cy + math.sin(angle) * value_r:.1f}")
        axes.append(f"<line x1='{cx}' y1='{cy}' x2='{end_x:.1f}' y2='{end_y:.1f}' class='radar-axis' />")
        labels.append(
            f"<text x='{label_x:.1f}' y='{label_y:.1f}' class='radar-label' "
            f"text-anchor='middle' dominant-baseline='middle'>{esc(label)}</text>"
        )

    return (
        f"<svg class='radar' viewBox='0 0 260 260' role='img' aria-label='{esc(title)}'>"
        f"{''.join(rings)}{''.join(axes)}"
        f"<polygon points='{' '.join(values)}' class='radar-fill' />"
        f"<polyline points='{' '.join(values)} {values[0] if values else ''}' class='radar-line' />"
        f"{''.join(labels)}"
        "</svg>"
    )


def status_lights(title: str, checks: dict[str, Any]) -> str:
    items = []
    for name, value in checks.items():
        cls = status_class(bool(value))
        items.append(
            "<div class='status-row'>"
            f"<span class='dot {cls}'></span>"
            f"<span>{esc(name)}</span>"
            f"<strong>{esc(value)}</strong>"
            "</div>"
        )
    return f"<div class='status-panel'><h3>{esc(title)}</h3>{''.join(items)}</div>"


def progress_bar(width: float, extra_class: str = "") -> str:
    width = max(0.0, min(100.0, width))
    return (
        "<div class='bar-track'>"
        f"<div class='bar-fill {extra_class}' style='width:{width:.1f}%'></div>"
        "</div>"
    )


def agent_display_name(peer: str) -> str:
    return {
        "ra_us": "Mike / US FDA",
        "ra_eu": "Theo / EU MDR",
        "ra_kr": "Sam / MFDS",
    }.get(peer, peer)


def agent_growth_cards(snapshot: dict[str, Any]) -> str:
    self_docs = snapshot["self_docs"]
    seed_counts = snapshot["seed_counts"]
    guards = snapshot.get("coverage_guards", {})
    expected_sources = (guards.get("source_coverage") or {}).get("expected_explicit_sources") or {}
    depth_floors = guards.get("self_doc_depth_floors") or {}
    growth_metrics = snapshot.get("growth_latest", {}).get("metrics", {})
    study_by_agent = (growth_metrics.get("autonomous_study_sessions") or {}).get("by_agent") or {}
    insights_by_agent = (growth_metrics.get("study_insights_count") or {}).get("by_agent") or {}
    messages_scanned = number(snapshot.get("growth_latest", {}).get("messages_scanned"))

    cards = []
    for peer in ("ra_us", "ra_eu", "ra_kr"):
        docs = number(self_docs.get(peer))
        floor_config = depth_floors.get(peer) if isinstance(depth_floors.get(peer), dict) else {}
        depth_floor = number(floor_config.get("min"))
        seeds = number(seed_counts.get(peer))
        expected = number(expected_sources.get(peer))
        study_count = number(study_by_agent.get(peer))
        insight_count = number(insights_by_agent.get(peer))
        foundation = (pct(docs, depth_floor) + pct(seeds, expected)) / 2
        operations = 0.0 if messages_scanned == 0 else min(100.0, study_count * 20 + insight_count * 5)
        level = "ok" if foundation >= 100 and operations > 0 else ("warn" if foundation >= 100 else "bad")
        status = (
            "기초 KB 확보 / 운영 성장 데이터 없음"
            if foundation >= 100 and operations == 0
            else ("운영 성장 측정 중" if operations > 0 else "기초 KB 부족")
        )
        cards.append(
            f"<article class='growth-card {level}'>"
            f"<div class='growth-card-head'><span>{esc(agent_display_name(peer))}</span><strong>{esc(status)}</strong></div>"
            "<div class='growth-score'>"
            f"<span>{esc(int(foundation))}%</span><small>foundation</small>"
            "</div>"
            "<div class='growth-bars'>"
            "<div class='growth-bar-row'><span>KB Depth</span>"
            f"{progress_bar(pct(docs, depth_floor), 'depth-fill')}"
            f"<strong>{esc(int(docs))}/{esc(int(depth_floor))}</strong></div>"
            "<div class='growth-bar-row'><span>Sources</span>"
            f"{progress_bar(pct(seeds, expected), 'source-fill')}"
            f"<strong>{esc(int(seeds))}/{esc(int(expected))}</strong></div>"
            "<div class='growth-bar-row'><span>Ops Evidence</span>"
            f"{progress_bar(operations, 'ops-fill')}"
            f"<strong>{esc(int(study_count))} study / {esc(int(insight_count))} insight</strong></div>"
            "</div>"
            "</article>"
        )
    return "".join(cards)


def growth_signal_strip(snapshot: dict[str, Any], maturity_measurable: bool) -> str:
    growth_latest = snapshot["growth_latest"]
    latest_messages = int(number(growth_latest.get("messages_scanned")))
    latest_sessions = int(number(growth_latest.get("sessions_scanned")))
    trend_messages = sum(int(number(row.get("messages_scanned"))) for row in snapshot.get("trend_rows", []))
    trend_insights = sum(int(number(row.get("study_insights_count"))) for row in snapshot.get("trend_rows", []))
    state = "blocked" if not maturity_measurable else "running"
    verdict = "성장 추세 미측정" if not maturity_measurable else "성장 추세 측정 중"
    next_action = (
        "결론: KB foundation은 준비됐지만 운영 성장 데이터가 0건입니다. 성장 신호는 Operational Input에서 끊겼고, 먼저 metrics ingestion을 고쳐야 합니다."
        if not maturity_measurable
        else "결론: 운영 성장 데이터가 들어오고 있습니다. 7일/30일 추세와 사람 피드백 기준선을 확인합니다."
    )
    return (
        f"<section class='growth-summary {state}'>"
        "<div>"
        "<div class='eyebrow'>RA Growth Operations</div>"
        f"<h2>{esc(verdict)}</h2>"
        f"<p>{esc(next_action)}</p>"
        "</div>"
        "<div class='summary-metrics'>"
        f"<div><strong>{esc(latest_messages)}</strong><span>latest messages</span></div>"
        f"<div><strong>{esc(latest_sessions)}</strong><span>latest sessions</span></div>"
        f"<div><strong>{esc(trend_messages)}</strong><span>14-report messages</span></div>"
        f"<div><strong>{esc(trend_insights)}</strong><span>14-report insights</span></div>"
        "</div>"
        "</section>"
    )


def growth_flow(maturity_measurable: bool) -> str:
    steps = [
        ("ok", "1", "Knowledge Base", "seed/depth ready"),
        ("bad" if not maturity_measurable else "ok", "2", "Operational Input", "messages scanned"),
        ("bad" if not maturity_measurable else "ok", "3", "Feedback Signal", "human review"),
        ("warn" if not maturity_measurable else "ok", "4", "Expert Growth", "trend verdict"),
    ]
    nodes = []
    for level, step, title, detail in steps:
        nodes.append(
            f"<div class='flow-node {level}'>"
            f"<span>{esc(step)}</span><strong>{esc(title)}</strong><small>{esc(detail)}</small>"
            "</div>"
        )
    return f"<section><h2>Growth Signal Flow</h2><div class='flow'>{''.join(nodes)}</div></section>"


def agent_evidence_bars(snapshot: dict[str, Any]) -> str:
    self_docs = snapshot["self_docs"]
    seed_counts = snapshot["seed_counts"]
    guards = snapshot.get("coverage_guards", {})
    expected_sources = (guards.get("source_coverage") or {}).get("expected_explicit_sources") or {}
    depth_floors = guards.get("self_doc_depth_floors") or {}
    rows = []
    for peer in sorted(set(self_docs) | set(expected_sources)):
        docs = number(self_docs.get(peer))
        floor_config = depth_floors.get(peer) if isinstance(depth_floors.get(peer), dict) else {}
        depth_floor = number(floor_config.get("min"))
        seeds = number(seed_counts.get(peer))
        expected = number(expected_sources.get(peer))
        rows.append(
            "<div class='agent-card'>"
            f"<div class='agent-name'>{esc(peer)}</div>"
            "<div class='agent-metric'><span>Depth Proxy</span>"
            f"<strong>{esc(int(docs))}/{esc(int(depth_floor))}</strong></div>"
            f"{progress_bar(pct(docs, depth_floor), 'depth-fill')}"
            "<div class='agent-metric'><span>Source Coverage</span>"
            f"<strong>{esc(int(seeds))}/{esc(int(expected))}</strong></div>"
            f"{progress_bar(pct(seeds, expected), 'source-fill')}"
            "</div>"
        )

    for guard in guards.get("relative_depth_floors", []):
        agent = guard.get("agent")
        baseline = guard.get("baseline")
        ratio = number(guard.get("min_ratio"))
        current = number(self_docs.get(agent))
        target = int(number(self_docs.get(baseline)) * ratio)
        rows.append(
            "<div class='threshold-card'>"
            f"<div class='threshold-head'><span>{esc(guard.get('id'))}</span>"
            f"<strong>{esc(int(current))}/{esc(target)}</strong></div>"
            f"{progress_bar(pct(current, target if target else 1), 'threshold-fill')}"
            f"<p><code>{esc(guard.get('status'))}</code> · {esc(guard.get('basis'))}</p>"
            "</div>"
        )
    return "".join(rows)


def coverage_basis(snapshot: dict[str, Any]) -> str:
    guards = snapshot.get("coverage_guards", {})
    source = guards.get("source_coverage") or {}
    depth = guards.get("self_doc_depth_floors") or {}
    source_rows = "\n".join(
        f"<tr><th>{esc(agent)}</th><td>{esc(expected)}</td><td>{esc(snapshot.get('seed_counts', {}).get(agent))}</td></tr>"
        for agent, expected in (source.get("expected_explicit_sources") or {}).items()
    )
    depth_rows = "\n".join(
        f"<tr><th>{esc(agent)}</th><td>{esc(config.get('min'))}</td><td>{esc(snapshot.get('self_docs', {}).get(agent))}</td><td>{esc(config.get('basis'))}</td></tr>"
        for agent, config in depth.items()
        if isinstance(config, dict)
    )
    legacy_rows = "\n".join(
        "<tr>"
        f"<th>{esc(guard.get('id'))}</th>"
        f"<td><code>{esc(guard.get('status'))}</code></td>"
        f"<td>{esc(guard.get('agent'))} >= {esc(guard.get('baseline'))} * {esc(guard.get('min_ratio'))}</td>"
        f"<td>{esc(guard.get('basis'))}</td>"
        "</tr>"
        for guard in guards.get("relative_depth_floors", [])
    )
    return (
        f"<p>{esc(source.get('_rationale'))}</p>"
        "<div class='grid two compact-tables'>"
        "<div><h3>Source Coverage</h3>"
        f"<table><thead><tr><th>Agent</th><th>Expected</th><th>Current</th></tr></thead><tbody>{source_rows}</tbody></table></div>"
        "<div><h3>Depth Proxy Floors</h3>"
        f"<table><thead><tr><th>Agent</th><th>Floor</th><th>Current</th><th>Basis</th></tr></thead><tbody>{depth_rows}</tbody></table></div>"
        "</div>"
        "<h3>Legacy Relative Guard</h3>"
        f"<table><thead><tr><th>Guard</th><th>Status</th><th>Rule</th><th>Basis</th></tr></thead><tbody>{legacy_rows}</tbody></table>"
        "<div class='note'>KR/EU 20% is a legacy_pre_activation_floor and not expert maturity. It only prevents a near-empty KR corpus before automation review.</div>"
    )


def sparkline(rows: list[dict[str, Any]], key: str, label: str) -> str:
    values = [number(row.get(key), 0.0) for row in rows]
    width = 260
    height = 62
    pad = 8
    if not values:
        values = [0.0]
    max_v = max(values)
    min_v = min(values)
    spread = max(max_v - min_v, 1.0)
    points = []
    for idx, value in enumerate(values):
        x = pad + (width - pad * 2) * (idx / max(1, len(values) - 1))
        y = height - pad - ((value - min_v) / spread) * (height - pad * 2)
        points.append(f"{x:.1f},{y:.1f}")
    last_value = values[-1]
    return (
        "<div class='spark-card'>"
        f"<div class='spark-head'><span>{esc(label)}</span><strong>{esc(last_value)}</strong></div>"
        f"<svg class='sparkline' viewBox='0 0 {width} {height}' role='img' aria-label='{esc(label)} trend'>"
        f"<polyline points='{' '.join(points)}' />"
        "</svg>"
        "</div>"
    )


def render(snapshot: dict[str, Any]) -> str:
    readiness = snapshot["readiness"]
    timers = snapshot["timers"]
    self_docs = snapshot["self_docs"]
    seed_counts = snapshot["seed_counts"]
    growth_latest = snapshot["growth_latest"]
    score_ok = readiness.get("total_score") == readiness.get("max_score") and readiness.get("max_score")
    scores = evidence_scores(snapshot)
    sessions_scanned = number(growth_latest.get("sessions_scanned"))
    messages_scanned = number(growth_latest.get("messages_scanned"))
    maturity_measurable = sessions_scanned > 0 and messages_scanned > 0
    maturity_verdict = (
        "측정 가능: 행동/피드백 지표 기반으로 추세 판정 가능"
        if maturity_measurable
        else "측정 불충분: 행동/사람 평가 데이터 0건"
    )
    maturity_class = "ok" if maturity_measurable else "warn"
    evidence_rows = "\n".join(
        f"<tr><th>{esc(evidence_label(name))}</th><td>{esc(score)}/4</td></tr>"
        for name, score in scores.items()
    )

    dimension_rows = "\n".join(
        f"<tr><th>{esc(name)}</th><td>{esc(score)}/4</td></tr>"
        for name, score in readiness.get("dimension_scores", {}).items()
    )
    cleanliness_rows = "\n".join(
        f"<tr><th>{esc(name)}</th><td><span class='pill {status_class(bool(value))}'>{esc(value)}</span></td></tr>"
        for name, value in snapshot.get("cleanliness", {}).items()
    )
    activation_rows = "\n".join(
        f"<tr><th>{esc(name)}</th><td><span class='pill {status_class(bool(value))}'>{esc(value)}</span></td></tr>"
        for name, value in snapshot.get("activation", {}).items()
    )
    self_doc_rows = "\n".join(
        f"<tr><th>{esc(name)}</th><td>{esc(value)}</td><td>{esc(seed_counts.get(name))}</td></tr>"
        for name, value in self_docs.items()
    )
    metric_rows = "\n".join(
        render_metric_row(name, data)
        for name, data in growth_latest.get("metrics", {}).items()
    )
    trend_rows = "\n".join(
        "<tr>"
        f"<td>{esc(row['file'])}</td>"
        f"<td>{esc(row['sessions_scanned'])}</td>"
        f"<td>{esc(row['messages_scanned'])}</td>"
        f"<td>{esc(row['correction_rate'], 'N/A')}</td>"
        f"<td>{esc(row['first_pass_match_accuracy'], 'N/A')}</td>"
        f"<td>{esc(row['autonomous_study_sessions'])}</td>"
        f"<td>{esc(row['study_insights_count'])}</td>"
        "</tr>"
        for row in snapshot["trend_rows"]
    )
    visuals = {
        "radar": radar_chart(scores, "expert evidence radar chart"),
        "growth_summary": growth_signal_strip(snapshot, maturity_measurable),
        "growth_cards": agent_growth_cards(snapshot),
        "growth_flow": growth_flow(maturity_measurable),
        "agent_bars": agent_evidence_bars(snapshot),
        "coverage_basis": coverage_basis(snapshot),
        "cleanliness_lights": status_lights("Cleanliness", snapshot.get("cleanliness", {})),
        "activation_lights": status_lights("Activation Control", snapshot.get("activation", {})),
        "messages_spark": sparkline(snapshot["trend_rows"], "messages_scanned", "Messages scanned"),
        "insights_spark": sparkline(snapshot["trend_rows"], "study_insights_count", "Study insights"),
    }

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RA Growth Operations Dashboard</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f8fb;
      --panel: #ffffff;
      --ink: #17202f;
      --muted: #617086;
      --line: #d9e0ea;
      --ok: #16784f;
      --warn: #9a6500;
      --bad: #b42318;
      --blue: #2563eb;
      --teal: #0f766e;
      --amber: #d97706;
      --red-bg: #fff1f0;
      --green-bg: #edf9f2;
      --yellow-bg: #fff8e8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.45;
    }}
    header {{
      padding: 28px 32px 18px;
      border-bottom: 1px solid var(--line);
      background: #ffffff;
    }}
    h1 {{ margin: 0 0 8px; font-size: 28px; font-weight: 760; letter-spacing: 0; }}
    h2 {{ margin: 0 0 14px; font-size: 17px; font-weight: 720; letter-spacing: 0; }}
    p {{ margin: 0; color: var(--muted); }}
    main {{ padding: 24px 32px 36px; max-width: 1280px; margin: 0 auto; }}
    .grid {{ display: grid; gap: 16px; }}
    .kpi-grid {{ grid-template-columns: repeat(4, minmax(180px, 1fr)); }}
    .growth-agent-grid {{ grid-template-columns: repeat(3, minmax(220px, 1fr)); margin-top: 16px; }}
    .two {{ grid-template-columns: repeat(2, minmax(280px, 1fr)); margin-top: 16px; }}
    section {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      min-width: 0;
    }}
    .kpi .label {{ color: var(--muted); font-size: 13px; margin-bottom: 8px; }}
    .kpi .value {{ font-size: 24px; font-weight: 780; letter-spacing: 0; }}
    .kpi .sub {{ color: var(--muted); font-size: 12px; margin-top: 8px; overflow-wrap: anywhere; }}
    .growth-summary {{
      display: grid;
      grid-template-columns: minmax(280px, 1.2fr) minmax(320px, .8fr);
      gap: 18px;
      align-items: center;
      border-width: 2px;
    }}
    .growth-summary.blocked {{ background: var(--red-bg); border-color: #f5b5ae; }}
    .growth-summary.running {{ background: var(--green-bg); border-color: #9ad8b0; }}
    .eyebrow {{ color: var(--muted); font-size: 12px; font-weight: 780; text-transform: uppercase; letter-spacing: .08em; }}
    .growth-summary h2 {{ margin: 4px 0 8px; font-size: 30px; }}
    .growth-summary p {{ max-width: 760px; color: #3a4658; }}
    .summary-metrics {{ display:grid; grid-template-columns: repeat(2, minmax(130px, 1fr)); gap: 10px; }}
    .summary-metrics div {{ background: rgba(255,255,255,.7); border: 1px solid var(--line); border-radius: 8px; padding: 12px; }}
    .summary-metrics strong {{ display:block; font-size: 26px; }}
    .summary-metrics span {{ color: var(--muted); font-size: 12px; }}
    .growth-card {{ border: 1px solid var(--line); border-radius: 8px; padding: 16px; background: #fff; }}
    .growth-card.ok {{ border-color: #9ad8b0; background: var(--green-bg); }}
    .growth-card.warn {{ border-color: #f0ce80; background: var(--yellow-bg); }}
    .growth-card.bad {{ border-color: #f5b5ae; background: var(--red-bg); }}
    .growth-card-head {{ display:flex; justify-content:space-between; align-items:flex-start; gap: 12px; min-height: 44px; }}
    .growth-card-head span {{ font-weight: 780; font-size: 15px; }}
    .growth-card-head strong {{ color: #3a4658; font-size: 12px; text-align:right; max-width: 170px; }}
    .growth-score {{ display:flex; align-items:baseline; gap: 8px; margin: 12px 0; }}
    .growth-score span {{ font-size: 36px; font-weight: 820; }}
    .growth-score small {{ color: var(--muted); }}
    .growth-bar-row {{ display:grid; grid-template-columns: 92px 1fr 112px; gap: 10px; align-items:center; margin-top: 10px; font-size: 12px; }}
    .growth-bar-row span {{ color: var(--muted); }}
    .growth-bar-row strong {{ text-align:right; color: #27364b; }}
    .flow {{ display:grid; grid-template-columns: repeat(4, minmax(160px, 1fr)); gap: 10px; }}
    .flow-node {{ border: 1px solid var(--line); border-radius: 8px; padding: 14px; background: #fff; position:relative; min-height: 116px; }}
    .flow-node.ok {{ background: var(--green-bg); border-color: #9ad8b0; }}
    .flow-node.warn {{ background: var(--yellow-bg); border-color: #f0ce80; }}
    .flow-node.bad {{ background: var(--red-bg); border-color: #f5b5ae; }}
    .flow-node span {{ display:inline-grid; place-items:center; width: 28px; height: 28px; border-radius: 999px; background: #fff; border: 1px solid var(--line); font-weight: 800; }}
    .flow-node strong {{ display:block; margin-top: 12px; font-size: 15px; }}
    .flow-node small {{ display:block; margin-top: 5px; color: var(--muted); }}
    .support-details {{ margin-top: 16px; border: 1px solid var(--line); border-radius: 8px; background: #fff; }}
    .support-details > summary {{ cursor: pointer; padding: 16px 18px; font-weight: 780; color: #27364b; list-style-position: inside; }}
    .support-details > summary span {{ color: var(--muted); font-weight: 520; margin-left: 8px; }}
    .support-body {{ padding: 0 18px 18px; }}
    .support-purpose {{ display:grid; grid-template-columns: repeat(4, minmax(180px, 1fr)); gap: 10px; margin: 0 0 16px; }}
    .purpose-card {{ border: 1px solid var(--line); border-radius: 8px; padding: 12px; background: #fbfdff; }}
    .purpose-card strong {{ display:block; color: #27364b; margin-bottom: 6px; }}
    .purpose-card span {{ color: var(--muted); font-size: 12px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
    th, td {{ padding: 9px 8px; border-top: 1px solid var(--line); text-align: left; vertical-align: top; }}
    th {{ font-weight: 680; color: #27364b; }}
    .pill {{ display: inline-block; padding: 3px 8px; border-radius: 999px; font-weight: 700; font-size: 12px; }}
    .pill.ok {{ color: var(--ok); background: #e9f7ef; }}
    .pill.warn {{ color: var(--warn); background: #fff6df; }}
    .pill.bad {{ color: var(--bad); background: #feecec; }}
    .note {{ margin-top: 14px; padding: 12px 14px; border-left: 4px solid var(--teal); background: #eef8f6; color: #17443f; }}
    .scroll {{ overflow-x: auto; }}
    .visual-grid {{ grid-template-columns: 1.05fr .95fr; align-items: stretch; margin-top: 16px; }}
    .visual-grid-3 {{ grid-template-columns: repeat(3, minmax(220px, 1fr)); margin-top: 16px; }}
    .visual-title {{ display:flex; justify-content:space-between; gap:12px; align-items:center; margin-bottom: 10px; }}
    .radar-wrap {{ display:flex; align-items:center; justify-content:center; min-height: 292px; }}
    .radar {{ width: min(100%, 320px); height: auto; }}
    .radar-ring {{ fill: none; stroke: #dbe3ef; stroke-width: 1; }}
    .radar-axis {{ stroke: #c8d2df; stroke-width: 1; }}
    .radar-fill {{ fill: rgba(37, 99, 235, .20); }}
    .radar-line {{ fill: none; stroke: var(--blue); stroke-width: 3; stroke-linejoin: round; }}
    .radar-label {{ fill: #34435a; font-size: 12px; font-weight: 700; }}
    .status-panel h3 {{ margin: 0 0 10px; font-size: 14px; }}
    .status-row {{ display:grid; grid-template-columns: 16px 1fr auto; gap: 8px; align-items:center; padding: 8px 0; border-top: 1px solid var(--line); font-size: 13px; }}
    .dot {{ width: 11px; height: 11px; border-radius: 999px; display:inline-block; box-shadow: 0 0 0 4px rgba(0,0,0,.04); }}
    .dot.ok {{ background: var(--ok); }}
    .dot.warn {{ background: var(--warn); }}
    .dot.bad {{ background: var(--bad); }}
    .agent-card {{ padding: 12px 0; border-top: 1px solid var(--line); }}
    .agent-name {{ font-weight: 720; color: #27364b; }}
    .agent-metric {{ display:flex; justify-content:space-between; gap: 12px; color: var(--muted); font-size: 12px; margin: 8px 0 5px; }}
    .agent-metric strong {{ color: var(--ink); }}
    .bar-track {{ height: 12px; background: #e7edf5; border-radius: 999px; overflow:hidden; position:relative; }}
    .bar-fill {{ height: 100%; background: linear-gradient(90deg, var(--teal), var(--blue)); border-radius: inherit; }}
    .source-fill {{ background: linear-gradient(90deg, var(--blue), var(--teal)); }}
    .depth-fill {{ background: linear-gradient(90deg, var(--teal), var(--ok)); }}
    .ops-fill {{ background: linear-gradient(90deg, var(--amber), var(--bad)); }}
    .threshold-card {{ margin-top: 14px; padding: 12px; background: #f8fafc; border: 1px solid var(--line); border-radius: 8px; }}
    .threshold-head {{ display:flex; justify-content:space-between; gap: 12px; margin-bottom: 8px; font-size: 13px; }}
    .threshold-fill {{ background: linear-gradient(90deg, var(--amber), var(--ok)); }}
    .threshold-card p {{ margin-top: 8px; font-size: 12px; }}
    .verdict {{ border-left: 5px solid var(--warn); }}
    .verdict.ok {{ border-left-color: var(--ok); }}
    .verdict .value {{ font-size: 20px; line-height: 1.25; }}
    .compact-tables {{ margin-top: 12px; }}
    h3 {{ margin: 10px 0 8px; font-size: 14px; }}
    .spark-card {{ padding: 12px; border: 1px solid var(--line); border-radius: 8px; background: #fbfdff; }}
    .spark-head {{ display:flex; justify-content:space-between; gap: 12px; align-items:center; color: var(--muted); font-size: 13px; margin-bottom: 4px; }}
    .spark-head strong {{ color: var(--ink); font-size: 20px; }}
    .sparkline {{ width:100%; height: 62px; }}
    .sparkline polyline {{ fill:none; stroke: var(--blue); stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
    footer {{ padding: 0 32px 28px; max-width: 1280px; margin: 0 auto; color: var(--muted); font-size: 12px; }}
    @media (max-width: 900px) {{
      header, main, footer {{ padding-left: 16px; padding-right: 16px; }}
      .kpi-grid, .two, .visual-grid, .visual-grid-3, .growth-agent-grid, .growth-summary, .flow, .support-purpose {{ grid-template-columns: 1fr; }}
      .growth-bar-row {{ grid-template-columns: 1fr; }}
      .growth-bar-row strong {{ text-align:left; }}
      h1 {{ font-size: 23px; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>RA Growth Operations Dashboard</h1>
    <p>실제 운영 중 각 RA 담당자의 성장 입력, 학습 근거, 피드백 신호, 성장 추세 측정 가능 여부를 확인하는 현황판입니다.</p>
  </header>
  <main>
    {visuals['growth_summary']}

    <div class="grid growth-agent-grid">
      {visuals['growth_cards']}
    </div>

    {visuals['growth_flow']}

    <details class="support-details">
      <summary>검증/감사 상세 보기 <span>상단 결론을 검산하거나 이슈 근거가 필요할 때만 펼칩니다.</span></summary>
      <div class="support-body">
        <div class="support-purpose">
          <div class="purpose-card"><strong>결론 검산</strong><span>상단의 "성장 추세 미측정"이 실제 metrics 0건과 일치하는지 확인합니다.</span></div>
          <div class="purpose-card"><strong>병목 위치 확인</strong><span>Operational Input이 막힌 것인지, 피드백/정확도 지표가 부족한 것인지 구분합니다.</span></div>
          <div class="purpose-card"><strong>커버리지 오판 방지</strong><span>KB/source floor 통과를 전문가 성숙도와 혼동하지 않도록 근거를 확인합니다.</span></div>
          <div class="purpose-card"><strong>이슈 기록 근거</strong><span>GitHub issue에 남길 수치, 파일명, readiness/cleanliness 상태를 확인합니다.</span></div>
        </div>
        <div class="grid kpi-grid">
          <section class="kpi">
            <div class="label">Growth Trend Verdict</div>
            <div class="value"><span class="pill {maturity_class}">{esc(maturity_verdict)}</span></div>
            <div class="sub">성장 추세는 운영 입력과 피드백 데이터가 있어야 판정합니다.</div>
          </section>
          <section class="kpi">
            <div class="label">Latest Growth Input</div>
            <div class="value">{esc(growth_latest.get('messages_scanned'))}</div>
            <div class="sub">최근 보고서의 scanned messages</div>
          </section>
          <section class="kpi">
            <div class="label">Metrics Collection</div>
            <div class="value"><span class="pill {status_class(timers['ra_growth_metrics']['active'] == 'active' and timers['ra_growth_metrics']['enabled'] == 'enabled')}">{esc(timers['ra_growth_metrics']['active'])}/{esc(timers['ra_growth_metrics']['enabled'])}</span></div>
            <div class="sub">timer 상태. 입력 0건이면 수집 경로 장애</div>
          </section>
          <section class="kpi">
            <div class="label">Knowledge Foundation</div>
            <div class="value"><span class="pill {status_class(scores.get('knowledge_depth_proxy') >= 4 and scores.get('source_coverage') >= 4)}">ready</span></div>
            <div class="sub">기초 KB/소스 커버리지 floor</div>
          </section>
          <section class="kpi">
            <div class="label">Readiness</div>
            <div class="value"><span class="pill {status_class(bool(score_ok))}">{esc(readiness.get('total_score'))}/{esc(readiness.get('max_score'))}</span></div>
            <div class="sub">{esc(readiness.get('recommendation'))}</div>
          </section>
        </div>

        <div class="grid visual-grid">
          <section>
            <div class="visual-title">
              <h2>Growth Evidence Radar</h2>
              <span class="pill {maturity_class}">{esc(maturity_verdict)}</span>
            </div>
            <div class="radar-wrap">{visuals['radar']}</div>
            <div class="note">Depth와 Source는 사전 커버리지 proxy입니다. Behavior와 Feedback은 실제 행동/사람 평가 데이터가 없으면 0점이며, 이 상태에서는 전문가 수준을 판정하지 않습니다.</div>
            <table><tbody>{evidence_rows}</tbody></table>
          </section>
          <section>
            <h2>Depth Proxy & Source Coverage</h2>
            {visuals['agent_bars']}
          </section>
        </div>

        <section style="margin-top:16px">
          <h2>Coverage Guard Basis</h2>
          {visuals['coverage_basis']}
        </section>

        <div class="grid visual-grid-3">
          <section>{visuals['cleanliness_lights']}</section>
          <section>{visuals['activation_lights']}</section>
          <section>
            <h2>Growth Trend</h2>
            {visuals['messages_spark']}
            {visuals['insights_spark']}
            <div class="note">현재 messages scanned가 0이므로 ingestion 보정 전까지 성장 추세 해석은 보류합니다.</div>
          </section>
        </div>

        <div class="grid two">
          <section>
            <h2>Readiness Matrix</h2>
            <table><tbody>{dimension_rows}</tbody></table>
            <div class="note">Source: {esc(snapshot.get('readiness_file'))}. 16/16은 자동화 승인 검토 가능 상태입니다. 전문가 성숙도 증명이나 production timer 활성화 완료를 뜻하지 않습니다.</div>
          </section>
          <section>
            <h2>Raw Agent Inputs</h2>
            <table>
              <thead><tr><th>Agent</th><th>Self Docs</th><th>Curriculum Seeds</th></tr></thead>
              <tbody>{self_doc_rows}</tbody>
            </table>
          </section>
        </div>

        <div class="grid two">
          <section>
            <h2>Cleanliness</h2>
            <table><tbody>{cleanliness_rows}</tbody></table>
          </section>
          <section>
            <h2>Activation Control</h2>
            <table><tbody>{activation_rows}</tbody></table>
          </section>
        </div>

        <section style="margin-top:16px">
          <h2>Latest Growth Metrics</h2>
          <div class="scroll">
            <table>
              <thead><tr><th>Metric</th><th>Value</th><th>Direction</th><th>Note</th></tr></thead>
              <tbody>{metric_rows}</tbody>
            </table>
          </div>
          <div class="note">Source: {esc(snapshot.get('growth_file'))}. 최근 보고서가 sessions/messages 0건이면 timer는 돌고 있어도 성장 추세 집계는 아직 유효하지 않습니다.</div>
        </section>

        <section style="margin-top:16px">
          <h2>Growth Report Trend</h2>
          <div class="scroll">
            <table>
              <thead>
                <tr><th>File</th><th>Sessions</th><th>Messages</th><th>Correction</th><th>First Pass</th><th>Study Sessions</th><th>Insights</th></tr>
              </thead>
              <tbody>{trend_rows}</tbody>
            </table>
          </div>
        </section>
      </div>
    </details>
  </main>
  <footer>
    Generated at {esc(snapshot.get('generated_at'))}. Regenerate with <code>python3 scripts/render-growth-dashboard.py</code>.
  </footer>
</body>
</html>
"""


def main() -> None:
    """Main entry point with comprehensive error handling."""
    try:
        # Ensure logs directory exists
        logs_dir = ROOT / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Starting dashboard generation...")
        snapshot = collect_snapshot()

        if "error" in snapshot:
            error_type = snapshot["error"]
            logger.error(f"Dashboard generation failed: {error_type}")
            # Generate error dashboard
            error_snapshot = {
                "generated_at": snapshot["generated_at"],
                "error": error_type,
                "readiness": {"total_score": 0, "max_score": 16, "recommendation": "Data collection failed"},
                "timers": {
                    "hermes_auto_growth": {"active": "unknown", "enabled": "unknown"},
                    "ra_growth_metrics": {"active": "unknown", "enabled": "unknown"},
                },
                "cleanliness": {},
                "activation": {},
                "self_docs": {},
                "seed_counts": {},
                "growth_latest": {},
                "trend_rows": [],
                "coverage_guards": {},
                "growth_targets": {},
            }
            OUTPUT.write_text(render(error_snapshot), encoding="utf-8")
            logger.info("Error dashboard generated")
            return

        OUTPUT.write_text(render(snapshot), encoding="utf-8")
        logger.info(f"Dashboard generated: {OUTPUT.relative_to(ROOT)}")

        print(json.dumps({
            "output": str(OUTPUT.relative_to(ROOT)),
            "readiness": snapshot["readiness"],
            "growth_file": snapshot["growth_file"],
        }, ensure_ascii=False))

    except Exception as e:
        logger.error(f"Dashboard generation failed: {e}")
        raise


if __name__ == "__main__":
    main()
