#!/usr/bin/env python3
"""Run or plan non-email RA growth cadence.

This loop is the growth side of automation. It does not read mail-triage input.
It uses already indexed regulatory knowledge, curriculum seeds, autonomous
study delta checks, and source coverage audits.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import psycopg2
import psycopg2.extras


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = REPO_ROOT / "scripts" / ".env"
REPORTS_DIR = REPO_ROOT / "reports" / "non-email-growth"
RA_PEERS = ("ra_us", "ra_eu", "ra_kr")
AGENT_KEYWORDS = {
    "ra_us": ("FDA", "510k", "510(k)", "De Novo", "PMA", "QSR", "QMSR"),
    "ra_eu": ("MDR", "IVDR", "MDCG", "EUDAMED", "Notified Body"),
    "ra_kr": ("MFDS", "KGMP", "식약처", "국내_MFDS", "디지털의료제품법", "의료기기법"),
}


@dataclass(frozen=True)
class CommandResult:
    name: str
    cmd: list[str]
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0

    def to_report(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cmd": self.cmd,
            "returncode": self.returncode,
            "stdout": self.stdout.strip(),
            "stderr": self.stderr.strip(),
        }


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(2)


def load_env_file(path: Path = ENV_FILE) -> dict[str, str]:
    env = os.environ.copy()
    if path.exists():
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            env.setdefault(key.strip(), value.strip().strip('"').strip("'"))
    return env


def run_command(name: str, cmd: list[str], env: dict[str, str], timeout: int = 600) -> CommandResult:
    proc = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        env=env,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    return CommandResult(name=name, cmd=cmd, returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)


def connect(env: dict[str, str]) -> Any:
    dsn = env.get("POSTGRES_URL", "")
    if not dsn:
        fail("POSTGRES_URL is required")
    return psycopg2.connect(dsn)


def keyword_where(keywords: tuple[str, ...]) -> tuple[str, list[str]]:
    clauses: list[str] = []
    params: list[str] = []
    for keyword in keywords:
        clauses.append("(source_path ILIKE %s OR metadata::text ILIKE %s)")
        pattern = f"%{keyword}%"
        params.extend([pattern, pattern])
    return " OR ".join(clauses), params


def fetch_ra_queue(conn: Any) -> dict[str, int]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT m.peer_name, COUNT(*)::int AS count
            FROM queue q
            JOIN messages m ON m.id = q.message_id
            WHERE NOT q.processed
              AND m.peer_name = ANY(%s)
            GROUP BY m.peer_name
            """,
            (list(RA_PEERS),),
        )
        counts = {peer: 0 for peer in RA_PEERS}
        counts.update({row["peer_name"]: int(row["count"]) for row in cur.fetchall()})
        return counts


def fetch_source_coverage(conn: Any) -> dict[str, Any]:
    coverage: dict[str, Any] = {}
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT COUNT(DISTINCT source_path)::int AS distinct_sources,
                   COUNT(*)::int AS chunks,
                   MIN(indexed_at)::text AS first_indexed_at,
                   MAX(indexed_at)::text AS last_indexed_at
            FROM ra_knowledge
            WHERE source_path IS NOT NULL
              AND source_path <> ''
              AND source_path NOT ILIKE %s
            """,
            ("%/wiki/entities/%",),
        )
        coverage["all"] = dict(cur.fetchone())
        for peer, keywords in AGENT_KEYWORDS.items():
            where_sql, params = keyword_where(keywords)
            cur.execute(
                f"""
                SELECT COUNT(DISTINCT source_path)::int AS distinct_sources,
                       COUNT(*)::int AS chunks,
                       MIN(indexed_at)::text AS first_indexed_at,
                       MAX(indexed_at)::text AS last_indexed_at
                FROM ra_knowledge
                WHERE source_path IS NOT NULL
                  AND source_path <> ''
                  AND source_path NOT ILIKE %s
                  AND ({where_sql})
                """,
                ["%/wiki/entities/%", *params],
            )
            coverage[peer] = dict(cur.fetchone())
    return coverage


def fetch_growth_records(conn: Any) -> dict[str, Any]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT peer_name,
                   metadata->>'record_type' AS record_type,
                   COUNT(*)::int AS count,
                   COUNT(*) FILTER (WHERE content ~ '^\\s*[\\{\\[]')::int AS json_envelopes,
                   COUNT(*) FILTER (
                       WHERE content ~ '^\\s*[\\{\\[]'
                         AND COALESCE(metadata->>'quarantine_status', '') <> 'quarantined'
                   )::int AS active_json_envelopes,
                   COUNT(*) FILTER (
                       WHERE content ~ '^\\s*[\\{\\[]'
                         AND metadata->>'quarantine_status' = 'quarantined'
                   )::int AS quarantined_json_envelopes,
                   COUNT(DISTINCT COALESCE(metadata->>'source_hash', metadata->>'scenario_id'))::int AS distinct_keys
            FROM messages
            WHERE peer_name = ANY(%s)
              AND metadata->>'record_type' IN ('daily_growth_case', 'curriculum_seed', 'study_insight', 'peer_study_insight')
            GROUP BY peer_name, metadata->>'record_type'
            ORDER BY peer_name, metadata->>'record_type'
            """,
            (list(RA_PEERS),),
        )
        return {"by_peer_record_type": [dict(row) for row in cur.fetchall()]}


def run_verifiers(env: dict[str, str]) -> list[dict[str, Any]]:
    commands = [
        ("verify-study-scheduler", ["python3", "scripts/verify-study-scheduler.py"]),
        ("verify-curriculum-seed", ["python3", "scripts/verify-curriculum-seed.py"]),
        ("verify-daily-growth-runner", ["python3", "scripts/verify-daily-growth-runner.py"]),
        ("verify-pre-auto-growth-loop", ["python3", "scripts/verify-pre-auto-growth-loop.py"]),
        ("verify-non-email-growth-loop", ["python3", "scripts/verify-non-email-growth-loop.py"]),
    ]
    return [run_command(name, cmd, env, timeout=300).to_report() for name, cmd in commands]


def run_daily(env: dict[str, str], args: argparse.Namespace) -> dict[str, Any]:
    cmd = [
        "python3",
        "scripts/daily-growth-runner.py",
        "--agent",
        args.agent,
        "--cases-per-agent",
        str(args.cases_per_agent),
        "--source-pool",
        str(args.source_pool),
        "--max-chunks-per-case",
        str(args.max_chunks_per_case),
        "--manual-growth-complete",
        "--max-pending",
        str(args.max_pending),
    ]
    if args.date:
        cmd.extend(["--date", args.date])
    cmd.extend(["--operation-timezone", args.operation_timezone])
    if args.execute_daily:
        cmd.append("--execute")
    return run_command("daily-kb-growth", cmd, env, timeout=600).to_report()


def run_weekly(env: dict[str, str], args: argparse.Namespace) -> dict[str, Any]:
    cmd = [
        "python3",
        "scripts/curriculum-seed.py",
        "--agent",
        args.agent,
        "--scope",
        args.curriculum_scope,
        "--limit-sources",
        str(args.curriculum_limit_sources),
        "--max-chunks-per-source",
        str(args.curriculum_max_chunks),
        "--preview",
        str(args.curriculum_preview),
    ]
    if args.execute_curriculum:
        cmd.append("--execute")
    return run_command("weekly-source-curriculum", cmd, env, timeout=600).to_report()


def run_monthly(env: dict[str, str], args: argparse.Namespace) -> dict[str, Any]:
    cmd = ["python3", "scripts/autonomous-study-scheduler.py", "delta", "--dry-run"]
    return run_command("monthly-study-delta-dry-run", cmd, env, timeout=args.study_timeout).to_report()


def build_quarterly_audit(conn: Any) -> dict[str, Any]:
    return {
        "source_coverage": fetch_source_coverage(conn),
        "audit_focus": [
            "jurisdiction source coverage",
            "stale source candidates",
            "duplicate source hash review",
            "FDA/EU/MFDS routing keyword drift",
        ],
    }


def selected_cadences(cadence: str) -> list[str]:
    if cadence == "all":
        return ["daily", "weekly", "monthly", "quarterly"]
    return [cadence]


def evaluate(report: dict[str, Any], max_pending: int) -> list[str]:
    failures: list[str] = []
    if sum(report["ra_pending_after"].values()) > max_pending:
        failures.append("RA pending queue exceeds max_pending")
    for result in report["verifiers"]:
        if result["returncode"] != 0:
            failures.append(f"verifier failed: {result['name']}")
    for cadence, result in report["cadence_results"].items():
        if isinstance(result, dict) and "returncode" in result and result["returncode"] != 0:
            failures.append(f"cadence failed: {cadence}")
    for row in report["growth_records"]["by_peer_record_type"]:
        if int(row.get("active_json_envelopes") or 0) != 0:
            failures.append(f"active JSON envelope contamination: {row['peer_name']} {row['record_type']}")
    return failures


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cadence", default="all", choices=["daily", "weekly", "monthly", "quarterly", "all"])
    parser.add_argument("--agent", default="all", choices=["ra-us", "ra-eu", "ra-kr", "all"])
    parser.add_argument("--date", default=None)
    parser.add_argument("--operation-timezone", default=os.environ.get("AUTO_GROWTH_OPERATION_TZ", "Asia/Seoul"))
    parser.add_argument("--max-pending", type=int, default=0)
    parser.add_argument("--cases-per-agent", type=int, default=1)
    parser.add_argument("--source-pool", type=int, default=10)
    parser.add_argument("--max-chunks-per-case", type=int, default=1)
    parser.add_argument("--execute-daily", action="store_true")
    parser.add_argument("--curriculum-scope", default="explicit", choices=["explicit", "shared", "all"])
    parser.add_argument("--curriculum-limit-sources", type=int, default=30)
    parser.add_argument("--curriculum-max-chunks", type=int, default=5)
    parser.add_argument("--curriculum-preview", type=int, default=5)
    parser.add_argument("--execute-curriculum", action="store_true")
    parser.add_argument("--study-timeout", type=int, default=600)
    parser.add_argument("--skip-verifiers", action="store_true")
    parser.add_argument("--output", default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.max_pending < 0:
        fail("--max-pending must be >= 0")
    env = load_env_file()
    output = Path(args.output) if args.output else REPORTS_DIR / f"non-email-growth-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    output.parent.mkdir(parents=True, exist_ok=True)

    with connect(env) as conn:
        ra_pending_before = fetch_ra_queue(conn)
        source_coverage_before = fetch_source_coverage(conn)

    cadence_results: dict[str, Any] = {}
    for cadence in selected_cadences(args.cadence):
        if cadence == "daily":
            cadence_results[cadence] = run_daily(env, args)
        elif cadence == "weekly":
            cadence_results[cadence] = run_weekly(env, args)
        elif cadence == "monthly":
            cadence_results[cadence] = run_monthly(env, args)
        elif cadence == "quarterly":
            with connect(env) as conn:
                cadence_results[cadence] = build_quarterly_audit(conn)

    with connect(env) as conn:
        report: dict[str, Any] = {
            "record_type": "non_email_growth_loop",
            "issue": "54",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "cadence": args.cadence,
            "execute_daily": bool(args.execute_daily),
            "execute_curriculum": bool(args.execute_curriculum),
            "ra_pending_before": ra_pending_before,
            "ra_pending_after": fetch_ra_queue(conn),
            "source_coverage_before": source_coverage_before,
            "source_coverage_after": fetch_source_coverage(conn),
            "growth_records": fetch_growth_records(conn),
            "verifiers": [] if args.skip_verifiers else run_verifiers(env),
            "cadence_results": cadence_results,
        }

    failures = evaluate(report, args.max_pending)
    report["ok"] = not failures
    report["failures"] = failures
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"ok": report["ok"], "failures": failures, "report": str(output)}, ensure_ascii=False))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
