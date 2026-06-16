#!/usr/bin/env python3
"""Render a standalone HTML growth dashboard from local report JSON files."""

from __future__ import annotations

import html
import json
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
    footer {{ padding: 0 32px 28px; max-width: 1280px; margin: 0 auto; color: var(--muted); font-size: 12px; }}
    @media (max-width: 900px) {{
      header, main, footer {{ padding-left: 16px; padding-right: 16px; }}
      .kpi-grid, .two {{ grid-template-columns: 1fr; }}
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
