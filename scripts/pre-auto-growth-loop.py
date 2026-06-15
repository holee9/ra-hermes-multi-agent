#!/usr/bin/env python3
"""Pre-automation readiness loop for daily RA growth.

The loop is intentionally conservative: it verifies the contracts and live
Honcho state required before promoting daily growth to a timer. It does not
quarantine or delete data. Any dirty state fails the run and is recorded in the
JSON report for issue-based follow-up.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import psycopg2
import psycopg2.extras


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports" / "pre-auto-growth"
ENV_FILE = REPO_ROOT / "scripts" / ".env"
AGENT_PEERS = ("ra_us", "ra_eu", "ra_kr")
VERIFY_SCRIPTS = (
    "scripts/verify-study-scheduler.py",
    "scripts/verify-curriculum-seed.py",
    "scripts/verify-daily-growth-runner.py",
    "scripts/verify-non-email-growth-loop.py",
    "scripts/verify-pre-auto-growth-loop.py",
)


@dataclass(frozen=True)
class CommandResult:
    cmd: list[str]
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0

    def to_report(self) -> dict[str, Any]:
        return {
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
    if not path.exists():
        return env
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        env.setdefault(key, value)
    return env


def run_command(cmd: list[str], env: dict[str, str], timeout: int = 300) -> CommandResult:
    proc = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        env=env,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    return CommandResult(cmd=cmd, returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)


def connect(env: dict[str, str]) -> Any:
    dsn = env.get("POSTGRES_URL", "")
    if not dsn:
        fail("POSTGRES_URL is required; set it in scripts/.env or environment")
    return psycopg2.connect(dsn)


def fetch_queue_snapshot(conn: Any) -> dict[str, Any]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT task_type, processed, COUNT(*)::int AS count
            FROM queue
            GROUP BY task_type, processed
            ORDER BY task_type, processed
            """
        )
        by_task = [dict(row) for row in cur.fetchall()]
        cur.execute("SELECT COUNT(*)::int FROM queue WHERE NOT processed")
        pending_total = int(cur.fetchone()["count"])
        cur.execute(
            """
            SELECT m.peer_name, COUNT(*)::int AS count
            FROM queue q
            JOIN messages m ON m.id = q.message_id
            WHERE NOT q.processed
              AND m.peer_name = ANY(%s)
            GROUP BY m.peer_name
            ORDER BY m.peer_name
            """,
            (list(AGENT_PEERS),),
        )
        pending_by_ra = {peer: 0 for peer in AGENT_PEERS}
        pending_by_ra.update({row["peer_name"]: int(row["count"]) for row in cur.fetchall()})
    return {
        "pending_total": pending_total,
        "pending_by_ra": pending_by_ra,
        "by_task": by_task,
    }


def fetch_self_docs(conn: Any) -> dict[str, int]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT observer, COUNT(*)::int
            FROM documents
            WHERE deleted_at IS NULL
              AND observer = observed
              AND observer = ANY(%s)
            GROUP BY observer
            ORDER BY observer
            """,
            (list(AGENT_PEERS),),
        )
        counts = {peer: 0 for peer in AGENT_PEERS}
        counts.update({row[0]: int(row[1]) for row in cur.fetchall()})
        return counts


def fetch_growth_message_health(conn: Any, run_date: str) -> dict[str, Any]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT COUNT(*)::int AS total,
                   COUNT(*) FILTER (WHERE content ~ '^\\s*[\\{\\[]')::int AS json_envelopes,
                   COUNT(*) FILTER (WHERE peer_name LIKE '%%-%%')::int AS hyphen_peers,
                   COUNT(DISTINCT metadata->>'scenario_id')::int AS distinct_scenarios
            FROM messages
            WHERE metadata->>'record_type' = 'daily_growth_case'
              AND metadata->>'run_date' = %s
            """,
            (run_date,),
        )
        return dict(cur.fetchone())


def check_deriver_flush(env: dict[str, str]) -> dict[str, Any]:
    cmd = [
        "docker",
        "compose",
        "-f",
        "honcho/docker-compose.yml",
        "--env-file",
        "honcho/.env",
        "exec",
        "-T",
        "deriver",
        "python",
        "-c",
        "from src.config import settings; print(settings.DERIVER.FLUSH_ENABLED)",
    ]
    result = run_command(cmd, env, timeout=60)
    value = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else ""
    return {
        "ok": result.ok and value == "True",
        "value": value,
        "command": result.to_report(),
    }


def run_verifiers(env: dict[str, str]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for script in VERIFY_SCRIPTS:
        result = run_command(["python3", script], env, timeout=300)
        results.append(result.to_report())
    return results


def run_daily_growth(
    env: dict[str, str],
    args: argparse.Namespace,
    report_path: Path,
    execute: bool,
) -> dict[str, Any]:
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
        "--output",
        str(report_path),
    ]
    if args.date:
        cmd.extend(["--date", args.date])
    if execute:
        cmd.append("--execute")
    result = run_command(cmd, env, timeout=600)
    plan: dict[str, Any] | None = None
    if report_path.exists():
        plan = json.loads(report_path.read_text(encoding="utf-8"))
    return {
        "execute": execute,
        "command": result.to_report(),
        "plan": plan,
    }


def pending_for_scope(snapshot: dict[str, Any], pending_scope: str) -> int:
    if pending_scope == "all":
        return int(snapshot["pending_total"])
    if pending_scope == "ra":
        return sum(int(value) for value in snapshot["pending_by_ra"].values())
    raise ValueError(f"unknown pending scope: {pending_scope}")


def wait_for_drain(
    env: dict[str, str],
    max_pending: int,
    timeout_seconds: int,
    sleep_seconds: int,
    pending_scope: str,
) -> dict[str, Any]:
    deadline = time.monotonic() + timeout_seconds
    snapshots: list[dict[str, Any]] = []
    while True:
        with connect(env) as conn:
            snapshot = fetch_queue_snapshot(conn)
        snapshots.append(snapshot)
        if pending_for_scope(snapshot, pending_scope) <= max_pending:
            return {"ok": True, "pending_scope": pending_scope, "snapshots": snapshots}
        if time.monotonic() >= deadline:
            return {"ok": False, "pending_scope": pending_scope, "snapshots": snapshots}
        time.sleep(sleep_seconds)


def evaluate_iteration(report: dict[str, Any], max_pending: int, pending_scope: str) -> list[str]:
    failures: list[str] = []
    if not report["deriver_flush"]["ok"]:
        failures.append("DERIVER_FLUSH_ENABLED is not True")
    pending_before = pending_for_scope(report["queue_before"], pending_scope)
    if pending_before > max_pending:
        failures.append(f"{pending_scope} queue pending before loop is {pending_before}")
    for verifier in report["verifiers"]:
        if verifier["returncode"] != 0:
            failures.append(f"verifier failed: {' '.join(verifier['cmd'])}")
    dry_plan = report["daily_growth_dry_run"].get("plan") or {}
    if not dry_plan.get("execute_gate", {}).get("allowed"):
        failures.append("daily-growth-runner execute gate is not allowed in dry-run")
    if report["daily_growth_dry_run"]["command"]["returncode"] != 0:
        failures.append("daily-growth-runner dry-run command failed")
    if report.get("daily_growth_execute") and report["daily_growth_execute"]["command"]["returncode"] != 0:
        failures.append("daily-growth-runner execute command failed")
    if report.get("drain") and not report["drain"]["ok"]:
        failures.append("queue did not drain before timeout")
    health = report["growth_message_health"]
    if int(health.get("json_envelopes") or 0) != 0:
        failures.append("daily_growth_case JSON envelope contamination detected")
    if int(health.get("hyphen_peers") or 0) != 0:
        failures.append("daily_growth_case hyphen peer contamination detected")
    pending_after = pending_for_scope(report["queue_after"], pending_scope)
    if pending_after > max_pending:
        failures.append(f"{pending_scope} queue pending after loop is {pending_after}")
    return failures


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iterations", type=int, default=1)
    parser.add_argument("--sleep-seconds", type=int, default=10)
    parser.add_argument("--drain-timeout-seconds", type=int, default=420)
    parser.add_argument("--max-pending", type=int, default=0)
    parser.add_argument("--pending-scope", default="all", choices=["all", "ra"])
    parser.add_argument("--agent", default="all", choices=["ra-us", "ra-eu", "ra-kr", "all"])
    parser.add_argument("--date", default=None, help="Run date YYYY-MM-DD, default daily-growth-runner UTC today")
    parser.add_argument("--cases-per-agent", type=int, default=1)
    parser.add_argument("--source-pool", type=int, default=10)
    parser.add_argument("--max-chunks-per-case", type=int, default=1)
    parser.add_argument("--execute-daily-growth", action="store_true")
    parser.add_argument("--skip-verifiers", action="store_true")
    parser.add_argument("--output", default=None)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.iterations < 1:
        fail("--iterations must be >= 1")
    if args.sleep_seconds < 1:
        fail("--sleep-seconds must be >= 1")
    if args.drain_timeout_seconds < 1:
        fail("--drain-timeout-seconds must be >= 1")
    if args.max_pending < 0:
        fail("--max-pending must be >= 0")

    env = load_env_file()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = Path(args.output) if args.output else REPORTS_DIR / f"pre-auto-growth-loop-{timestamp}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    top_report: dict[str, Any] = {
        "record_type": "pre_auto_growth_loop",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "issue": "53",
        "iterations_requested": args.iterations,
        "execute_daily_growth": bool(args.execute_daily_growth),
        "pending_scope": args.pending_scope,
        "iterations": [],
        "ok": False,
    }

    all_failures: list[str] = []
    for index in range(1, args.iterations + 1):
        iteration_dir = output_path.parent / f"{output_path.stem}-iteration-{index}"
        iteration_dir.mkdir(parents=True, exist_ok=True)
        run_date_for_health = args.date or datetime.now(timezone.utc).date().isoformat()
        with connect(env) as conn:
            queue_before = fetch_queue_snapshot(conn)
            docs_before = fetch_self_docs(conn)
            health_before = fetch_growth_message_health(conn, run_date_for_health)

        dry_report_path = iteration_dir / "daily-growth-dry-run.json"
        execute_report_path = iteration_dir / "daily-growth-execute.json"
        iteration_report: dict[str, Any] = {
            "iteration": index,
            "started_at": datetime.now(timezone.utc).isoformat(),
            "queue_before": queue_before,
            "self_docs_before": docs_before,
            "growth_message_health_before": health_before,
            "deriver_flush": check_deriver_flush(env),
            "verifiers": [] if args.skip_verifiers else run_verifiers(env),
            "daily_growth_dry_run": run_daily_growth(env, args, dry_report_path, execute=False),
        }
        if args.execute_daily_growth:
            iteration_report["daily_growth_execute"] = run_daily_growth(env, args, execute_report_path, execute=True)
            iteration_report["drain"] = wait_for_drain(
                env=env,
                max_pending=args.max_pending,
                timeout_seconds=args.drain_timeout_seconds,
                sleep_seconds=args.sleep_seconds,
                pending_scope=args.pending_scope,
            )

        with connect(env) as conn:
            iteration_report["queue_after"] = fetch_queue_snapshot(conn)
            iteration_report["self_docs_after"] = fetch_self_docs(conn)
            iteration_report["growth_message_health"] = fetch_growth_message_health(conn, run_date_for_health)

        failures = evaluate_iteration(iteration_report, args.max_pending, args.pending_scope)
        iteration_report["failures"] = failures
        iteration_report["ok"] = not failures
        top_report["iterations"].append(iteration_report)
        all_failures.extend(f"iteration {index}: {failure}" for failure in failures)
        output_path.write_text(json.dumps(top_report, indent=2, ensure_ascii=False), encoding="utf-8")
        if failures:
            break
        if index < args.iterations:
            time.sleep(args.sleep_seconds)

    top_report["ok"] = not all_failures
    top_report["failures"] = all_failures
    top_report["completed_at"] = datetime.now(timezone.utc).isoformat()
    output_path.write_text(json.dumps(top_report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"ok": top_report["ok"], "failures": all_failures, "report": str(output_path)}, ensure_ascii=False))
    if all_failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
