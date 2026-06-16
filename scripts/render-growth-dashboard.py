#!/usr/bin/env python3
"""Render a standalone HTML growth dashboard from local report JSON files."""

from __future__ import annotations

import html
import json
import math
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
OUTPUT = ROOT / "docs" / "growth-dashboard.html"


def load_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def latest_json(paths: list[Path]) -> tuple[Path | None, dict[str, Any] | None]:
    existing = [path for path in paths if path.exists()]
    if not existing:
        return None, None
    latest = max(existing, key=lambda path: path.stat().st_mtime)
    return latest, load_json(latest)


def run(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=False, timeout=30)
    return (proc.stdout or proc.stderr).strip()


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
    readiness_path, readiness = latest_json(sorted((REPORTS / "auto-growth-readiness").glob("*.json")))
    growth_paths = sorted(REPORTS.glob("growth-*.json"))
    growth_reports = [(path, load_json(path)) for path in growth_paths]
    growth_reports = [(path, data) for path, data in growth_reports if data]
    latest_growth_path, latest_growth = latest_json(growth_paths)

    matrix = (readiness or {}).get("matrix", {})
    scores = matrix.get("scores", {})
    db = (readiness or {}).get("db", {})
    growth_metrics = (latest_growth or {}).get("metrics", {})

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
    }


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


def radar_chart(dimension_scores: dict[str, Any]) -> str:
    order = [
        ("activation_control", "Activation"),
        ("data_cleanliness", "Cleanliness"),
        ("growth_input_quality", "Input"),
        ("agent_balance", "Balance"),
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
        score = number(dimension_scores.get(key))
        value_r = radius * max(0, min(4, score)) / 4
        values.append(f"{cx + math.cos(angle) * value_r:.1f},{cy + math.sin(angle) * value_r:.1f}")
        axes.append(f"<line x1='{cx}' y1='{cy}' x2='{end_x:.1f}' y2='{end_y:.1f}' class='radar-axis' />")
        labels.append(
            f"<text x='{label_x:.1f}' y='{label_y:.1f}' class='radar-label' "
            f"text-anchor='middle' dominant-baseline='middle'>{esc(label)}</text>"
        )

    return (
        "<svg class='radar' viewBox='0 0 260 260' role='img' aria-label='readiness radar chart'>"
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


def agent_bars(self_docs: dict[str, Any], seed_counts: dict[str, Any]) -> str:
    max_docs = max([number(value) for value in self_docs.values()] + [1])
    rows = []
    for peer, value in self_docs.items():
        width = pct(number(value), max_docs)
        rows.append(
            "<div class='agent-bar-row'>"
            f"<div class='agent-name'>{esc(peer)}</div>"
            "<div class='bar-track'>"
            f"<div class='bar-fill' style='width:{width:.1f}%'></div>"
            "</div>"
            f"<div class='agent-value'>{esc(value)} docs · {esc(seed_counts.get(peer))} seeds</div>"
            "</div>"
        )

    eu = number(self_docs.get("ra_eu"))
    kr = number(self_docs.get("ra_kr"))
    kr_target = int(eu * 0.2)
    target_width = pct(kr, kr_target if kr_target else 1)
    rows.append(
        "<div class='threshold-card'>"
        "<div class='threshold-head'><span>KR/EU 20% balance</span>"
        f"<strong>{esc(int(kr))}/{esc(kr_target)}</strong></div>"
        "<div class='bar-track threshold'>"
        f"<div class='bar-fill threshold-fill' style='width:{min(target_width, 100):.1f}%'></div>"
        "</div>"
        "</div>"
    )
    return "".join(rows)


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
        "radar": radar_chart(readiness.get("dimension_scores", {})),
        "agent_bars": agent_bars(self_docs, seed_counts),
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
  <title>RA Hermes Growth Dashboard</title>
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
    .agent-bar-row {{ display:grid; grid-template-columns: 74px 1fr 150px; gap: 10px; align-items:center; padding: 9px 0; border-top: 1px solid var(--line); }}
    .agent-name {{ font-weight: 720; color: #27364b; }}
    .agent-value {{ color: var(--muted); font-size: 12px; text-align:right; }}
    .bar-track {{ height: 12px; background: #e7edf5; border-radius: 999px; overflow:hidden; position:relative; }}
    .bar-fill {{ height: 100%; background: linear-gradient(90deg, var(--teal), var(--blue)); border-radius: inherit; }}
    .threshold-card {{ margin-top: 14px; padding: 12px; background: #f8fafc; border: 1px solid var(--line); border-radius: 8px; }}
    .threshold-head {{ display:flex; justify-content:space-between; gap: 12px; margin-bottom: 8px; font-size: 13px; }}
    .threshold-fill {{ background: linear-gradient(90deg, var(--amber), var(--ok)); }}
    .spark-card {{ padding: 12px; border: 1px solid var(--line); border-radius: 8px; background: #fbfdff; }}
    .spark-head {{ display:flex; justify-content:space-between; gap: 12px; align-items:center; color: var(--muted); font-size: 13px; margin-bottom: 4px; }}
    .spark-head strong {{ color: var(--ink); font-size: 20px; }}
    .sparkline {{ width:100%; height: 62px; }}
    .sparkline polyline {{ fill:none; stroke: var(--blue); stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
    footer {{ padding: 0 32px 28px; max-width: 1280px; margin: 0 auto; color: var(--muted); font-size: 12px; }}
    @media (max-width: 900px) {{
      header, main, footer {{ padding-left: 16px; padding-right: 16px; }}
      .kpi-grid, .two, .visual-grid, .visual-grid-3 {{ grid-template-columns: 1fr; }}
      .agent-bar-row {{ grid-template-columns: 1fr; }}
      .agent-value {{ text-align:left; }}
      h1 {{ font-size: 23px; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>RA Hermes Growth Dashboard</h1>
    <p>Git에서 바로 열어 보는 정적 HTML snapshot. 자동성장 실행 화면이 아니라 readiness, 성장 지표, 안전 상태를 확인하는 운영용 보고서입니다.</p>
  </header>
  <main>
    <div class="grid kpi-grid">
      <section class="kpi">
        <div class="label">Readiness</div>
        <div class="value"><span class="pill {status_class(bool(score_ok))}">{esc(readiness.get('total_score'))}/{esc(readiness.get('max_score'))}</span></div>
        <div class="sub">{esc(readiness.get('recommendation'))}</div>
      </section>
      <section class="kpi">
        <div class="label">Auto Growth Timer</div>
        <div class="value"><span class="pill {status_class(timers['hermes_auto_growth']['active'] == 'inactive' and timers['hermes_auto_growth']['enabled'] == 'disabled')}">{esc(timers['hermes_auto_growth']['active'])}/{esc(timers['hermes_auto_growth']['enabled'])}</span></div>
        <div class="sub">명시 승인 전 off 유지</div>
      </section>
      <section class="kpi">
        <div class="label">Metrics Timer</div>
        <div class="value"><span class="pill {status_class(timers['ra_growth_metrics']['active'] == 'active' and timers['ra_growth_metrics']['enabled'] == 'enabled')}">{esc(timers['ra_growth_metrics']['active'])}/{esc(timers['ra_growth_metrics']['enabled'])}</span></div>
        <div class="sub">매일 02:00 KST</div>
      </section>
      <section class="kpi">
        <div class="label">Latest Growth Input</div>
        <div class="value">{esc(growth_latest.get('messages_scanned'))}</div>
        <div class="sub">messages scanned; 0이면 ingestion 보정 필요</div>
      </section>
    </div>

    <div class="grid visual-grid">
      <section>
        <div class="visual-title">
          <h2>Readiness Radar</h2>
          <span class="pill {status_class(bool(score_ok))}">{esc(readiness.get('total_score'))}/{esc(readiness.get('max_score'))}</span>
        </div>
        <div class="radar-wrap">{visuals['radar']}</div>
        <div class="note">4개 축이 모두 바깥 링에 닿으면 자동성장 승인 검토 기준을 충족합니다.</div>
      </section>
      <section>
        <h2>Agent Balance Bars</h2>
        {visuals['agent_bars']}
      </section>
    </div>

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
        <div class="note">Source: {esc(snapshot.get('readiness_file'))}. 16/16은 승인 검토 가능 상태이며, production timer 활성화 완료를 뜻하지 않습니다.</div>
      </section>
      <section>
        <h2>Agent Balance</h2>
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
  </main>
  <footer>
    Generated at {esc(snapshot.get('generated_at'))}. Regenerate with <code>python3 scripts/render-growth-dashboard.py</code>.
  </footer>
</body>
</html>
"""


def main() -> None:
    snapshot = collect_snapshot()
    OUTPUT.write_text(render(snapshot), encoding="utf-8")
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "readiness": snapshot["readiness"],
        "growth_file": snapshot["growth_file"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
