#!/usr/bin/env python3
"""Non-destructive readiness report for pre-production auto-growth hardening."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import psycopg2
import psycopg2.extras


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = REPO_ROOT / "scripts" / ".env"
REPORTS_DIR = REPO_ROOT / "reports" / "auto-growth-readiness"
AGENT_PEERS = ("ra_us", "ra_eu", "ra_kr")
EXPECTED_SEEDS = {"ra_us": 48, "ra_eu": 31, "ra_kr": 29}
DEFAULT_OPERATION_TIMEZONE = os.environ.get("AUTO_GROWTH_OPERATION_TZ", "Asia/Seoul")
COVERAGE_GUARDS = REPO_ROOT / "scripts" / "coverage-guards.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(2)


def load_env_file(path: Path = ENV_FILE) -> dict[str, str]:
    env = os.environ.copy()
    if not path.exists():
        return env
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env.setdefault(key.strip(), value.strip().strip('"').strip("'"))
    return env


def load_coverage_guards(path: Path = COVERAGE_GUARDS) -> dict[str, Any]:
    if not path.exists():
        return {
            "source_coverage": {"expected_explicit_sources": EXPECTED_SEEDS},
            "self_doc_depth_floors": {
                "ra_us": {"min": 5000},
                "ra_eu": {"min": 2000},
                "ra_kr": {"min": 500},
            },
            "relative_depth_floors": [
                {
                    "id": "kr_not_below_20pct_eu",
                    "agent": "ra_kr",
                    "baseline": "ra_eu",
                    "min_ratio": 0.2,
                }
            ],
        }
    return json.loads(path.read_text(encoding="utf-8"))


def run(cmd: list[str], timeout: int = 60) -> dict[str, Any]:
    proc = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    return {
        "cmd": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def connect(env: dict[str, str]) -> Any:
    dsn = env.get("POSTGRES_URL", "")
    if not dsn:
        fail("POSTGRES_URL is required")
    return psycopg2.connect(dsn)


def fetch_db_state(conn: Any) -> dict[str, Any]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("SELECT COUNT(*)::int AS count FROM queue WHERE NOT processed")
        pending_total = int(cur.fetchone()["count"])

        cur.execute(
            """
            SELECT q.task_type,
                   COALESCE(m.peer_name, '<missing-message>') AS peer_name,
                   COALESCE(m.metadata->>'record_type', '') AS record_type,
                   COUNT(*)::int AS count
            FROM queue q
            LEFT JOIN messages m ON m.id = q.message_id
            WHERE NOT q.processed
            GROUP BY q.task_type, COALESCE(m.peer_name, '<missing-message>'), COALESCE(m.metadata->>'record_type', '')
            ORDER BY count DESC, q.task_type, peer_name
            """
        )
        pending_breakdown = [dict(row) for row in cur.fetchall()]

        cur.execute(
            """
            SELECT m.peer_name, COUNT(*)::int AS count
            FROM queue q
            JOIN messages m ON m.id = q.message_id
            WHERE NOT q.processed
              AND m.peer_name = ANY(%s)
            GROUP BY m.peer_name
            """,
            (list(AGENT_PEERS),),
        )
        pending_by_ra = {peer: 0 for peer in AGENT_PEERS}
        pending_by_ra.update({row["peer_name"]: int(row["count"]) for row in cur.fetchall()})

        cur.execute("SELECT COUNT(*)::int AS count FROM messages WHERE peer_name IN ('ra-us', 'ra-eu')")
        wrong_messages = int(cur.fetchone()["count"])

        cur.execute(
            """
            SELECT COUNT(*)::int AS count
            FROM queue q
            JOIN messages m ON m.id = q.message_id
            WHERE m.peer_name IN ('ra-us', 'ra-eu')
            """
        )
        wrong_queue_refs = int(cur.fetchone()["count"])

        cur.execute("SELECT COUNT(*)::int AS count FROM message_embeddings WHERE peer_name IN ('ra-us', 'ra-eu')")
        wrong_embeddings = int(cur.fetchone()["count"])

        cur.execute(
            """
            SELECT COUNT(*)::int AS count
            FROM documents
            WHERE deleted_at IS NULL
              AND (observer IN ('ra-us', 'ra-eu') OR observed IN ('ra-us', 'ra-eu'))
            """
        )
        wrong_active_docs = int(cur.fetchone()["count"])

        cur.execute(
            """
            SELECT observer, COUNT(*)::int AS count
            FROM documents
            WHERE deleted_at IS NULL
              AND observer = observed
              AND observer = ANY(%s)
            GROUP BY observer
            ORDER BY observer
            """,
            (list(AGENT_PEERS),),
        )
        self_docs = {peer: 0 for peer in AGENT_PEERS}
        self_docs.update({row["observer"]: int(row["count"]) for row in cur.fetchall()})

        cur.execute(
            """
            SELECT peer_name,
                   COUNT(*)::int AS total,
                   COUNT(*) FILTER (WHERE content ~ '^\\s*[\\{\\[]')::int AS json_envelopes,
                   COUNT(DISTINCT metadata->>'source_hash')::int AS distinct_hashes
            FROM messages
            WHERE metadata->>'record_type' = 'curriculum_seed'
            GROUP BY peer_name
            ORDER BY peer_name
            """
        )
        curriculum_seed = {row["peer_name"]: dict(row) for row in cur.fetchall()}

        cur.execute(
            """
            SELECT COALESCE(metadata->>'record_type', '') AS record_type,
                   COUNT(*) FILTER (
                     WHERE content ~ '^\\s*[\\{\\[]'
                       AND COALESCE(metadata->>'quarantine_status', '') <> 'quarantined'
                   )::int AS active_json_envelopes,
                   COUNT(*) FILTER (WHERE peer_name LIKE '%%-%%')::int AS hyphen_peers
            FROM messages
            WHERE metadata->>'record_type' IN ('daily_growth_case', 'curriculum_seed', 'study_insight')
            GROUP BY COALESCE(metadata->>'record_type', '')
            ORDER BY record_type
            """
        )
        growth_health = [dict(row) for row in cur.fetchall()]

    return {
        "pending_total": pending_total,
        "pending_breakdown": pending_breakdown,
        "pending_by_ra": pending_by_ra,
        "wrong_peer": {
            "messages": wrong_messages,
            "queue_refs": wrong_queue_refs,
            "embeddings": wrong_embeddings,
            "active_docs": wrong_active_docs,
        },
        "self_docs": self_docs,
        "curriculum_seed": curriculum_seed,
        "growth_health": growth_health,
    }


def run_daily_plan(env: dict[str, str], run_date: str, operation_timezone: str, output: Path) -> dict[str, Any]:
    cmd = [
        "python3",
        "scripts/daily-growth-runner.py",
        "--agent",
        "all",
        "--cases-per-agent",
        "1",
        "--source-pool",
        "10",
        "--max-chunks-per-case",
        "1",
        "--manual-growth-complete",
        "--max-pending",
        "0",
        "--date",
        run_date,
        "--operation-timezone",
        operation_timezone,
        "--output",
        str(output),
    ]
    proc = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        env=env,
        text=True,
        capture_output=True,
        timeout=600,
        check=False,
    )
    plan = json.loads(output.read_text(encoding="utf-8")) if output.exists() else None
    return {
        "command": {
            "cmd": cmd,
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        },
        "plan": plan,
    }


def score_matrix(report: dict[str, Any]) -> dict[str, Any]:
    db = report["db"]
    timer = report["timer"]
    daily_plan = report["daily_plan"]["plan"] or {}
    coverage_guards = load_coverage_guards()

    scores: dict[str, dict[str, Any]] = {}

    def dimension_score(checks: dict[str, bool]) -> int:
        true_count = sum(1 for ok in checks.values() if ok)
        if all(checks.values()):
            return 4
        return min(3, true_count)

    gate_checks = {
        "timer_inactive": timer["active"]["stdout"] == "inactive",
        "timer_disabled": timer["enabled"]["stdout"] == "disabled",
        "not_scheduled": "hermes-auto-growth.timer" not in timer["timers"]["stdout"],
        "persistent_false": timer["persistent_false"],
        "activation_guard": report["activation_guard"]["returncode"] == 2,
    }
    scores["activation_control"] = {
        "score": dimension_score(gate_checks),
        "checks": gate_checks,
    }

    contamination_checks = {
        "pending_total_zero": db["pending_total"] == 0,
        "ra_pending_zero": sum(db["pending_by_ra"].values()) == 0,
        "wrong_peer_zero": sum(db["wrong_peer"].values()) == 0,
        "active_json_zero": all(int(row["active_json_envelopes"]) == 0 for row in db["growth_health"]),
        "hyphen_peer_zero": all(int(row["hyphen_peers"]) == 0 for row in db["growth_health"]),
    }
    scores["data_cleanliness"] = {
        "score": dimension_score(contamination_checks),
        "checks": contamination_checks,
    }

    seed_counts = {
        peer: int((db["curriculum_seed"].get(peer) or {}).get("total") or 0)
        for peer in AGENT_PEERS
    }
    expected_seeds = coverage_guards.get("source_coverage", {}).get("expected_explicit_sources", EXPECTED_SEEDS)
    growth_checks = {
        "operation_date_matches": daily_plan.get("run_date") == report["operation_date"],
        "daily_plan_available": int(daily_plan.get("planned_case_count") or 0) >= 3,
        "execute_gate_ready": bool((daily_plan.get("execute_gate") or {}).get("allowed")),
        "curriculum_seed_complete": all(seed_counts.get(peer, 0) >= int(expected_seeds[peer]) for peer in AGENT_PEERS),
    }
    scores["growth_input_quality"] = {
        "score": dimension_score(growth_checks),
        "checks": growth_checks,
        "seed_counts": seed_counts,
    }

    self_docs = db["self_docs"]
    depth_floors = coverage_guards.get("self_doc_depth_floors", {})
    balance_checks = {
        "ra_us_has_depth": self_docs["ra_us"] >= int((depth_floors.get("ra_us") or {}).get("min", 5000)),
        "ra_eu_has_depth": self_docs["ra_eu"] >= int((depth_floors.get("ra_eu") or {}).get("min", 2000)),
        "ra_kr_minimum_met": self_docs["ra_kr"] >= int((depth_floors.get("ra_kr") or {}).get("min", 500)),
    }
    for guard in coverage_guards.get("relative_depth_floors", []):
        guard_id = guard["id"]
        agent = guard["agent"]
        baseline = guard["baseline"]
        min_ratio = float(guard["min_ratio"])
        balance_checks[guard_id] = self_docs[agent] >= int(self_docs[baseline] * min_ratio)
    scores["agent_balance"] = {
        "score": dimension_score(balance_checks),
        "checks": balance_checks,
        "self_docs": self_docs,
        "guard_source": str(COVERAGE_GUARDS.relative_to(REPO_ROOT)),
    }

    total_score = sum(item["score"] for item in scores.values())
    return {
        "scale": "4 dimensions x 4 target score; 16 is fully ready for approval review",
        "scores": scores,
        "total_score": total_score,
        "max_score": 16,
        "timer_operation_recommendation": "keep_off" if total_score < 16 else "approval_review_required",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--operation-timezone", default=DEFAULT_OPERATION_TIMEZONE)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    env = load_env_file()
    operation_date = datetime.now(ZoneInfo(args.operation_timezone)).date().isoformat()
    output_path = Path(args.output) if args.output else REPORTS_DIR / f"readiness-{datetime.now(ZoneInfo(args.operation_timezone)).strftime('%Y%m%dT%H%M%S')}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    daily_plan_path = output_path.with_name(f"{output_path.stem}-daily-plan.json")

    with connect(env) as conn:
        db_state = fetch_db_state(conn)

    timer_content = (REPO_ROOT / "scripts" / "systemd" / "hermes-auto-growth.timer").read_text(encoding="utf-8")
    report: dict[str, Any] = {
        "record_type": "auto_growth_readiness_report",
        "issue": "58",
        "created_at": datetime.now(ZoneInfo(args.operation_timezone)).isoformat(),
        "operation_timezone": args.operation_timezone,
        "operation_date": operation_date,
        "timer": {
            "active": run(["systemctl", "is-active", "hermes-auto-growth.timer"]),
            "enabled": run(["systemctl", "is-enabled", "hermes-auto-growth.timer"]),
            "timers": run(["systemctl", "list-timers", "--all", "--no-pager"]),
            "persistent_false": "Persistent=false" in timer_content and "Persistent=true" not in timer_content,
        },
        "activation_guard": run(["bash", "scripts/install-auto-growth-timer.sh", "--enable"]),
        "db": db_state,
        "daily_plan": run_daily_plan(env, operation_date, args.operation_timezone, daily_plan_path),
    }
    report["matrix"] = score_matrix(report)
    output_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"report": str(output_path), "matrix": report["matrix"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
