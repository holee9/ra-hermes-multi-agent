#!/usr/bin/env python3
"""Non-destructive ra_kr growth-depth planning report for #59."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import psycopg2
import psycopg2.extras

import importlib.util
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = REPO_ROOT / "scripts" / ".env"
REPORTS_DIR = REPO_ROOT / "reports" / "ra-kr-growth"
DEFAULT_OPERATION_TIMEZONE = os.environ.get("AUTO_GROWTH_OPERATION_TZ", "Asia/Seoul")

CURRICULUM = REPO_ROOT / "scripts" / "curriculum-seed.py"
DAILY = REPO_ROOT / "scripts" / "daily-growth-runner.py"
STUDY = REPO_ROOT / "scripts" / "autonomous-study-scheduler.py"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(2)


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_env_file(path: Path = ENV_FILE) -> dict[str, str]:
    env = os.environ.copy()
    if not path.exists():
        return env
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        clean_key = key.strip()
        clean_value = value.strip().strip('"').strip("'")
        env.setdefault(clean_key, clean_value)
        os.environ.setdefault(clean_key, clean_value)
    return env


def connect(env: dict[str, str]) -> Any:
    dsn = env.get("POSTGRES_URL", "")
    if not dsn:
        fail("POSTGRES_URL is required")
    return psycopg2.connect(dsn)


def fetch_self_docs(conn: Any) -> dict[str, int]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT observer, COUNT(*)::int
            FROM documents
            WHERE deleted_at IS NULL
              AND observer = observed
              AND observer IN ('ra_us', 'ra_eu', 'ra_kr')
            GROUP BY observer
            ORDER BY observer
            """
        )
        counts = {"ra_us": 0, "ra_eu": 0, "ra_kr": 0}
        counts.update({row[0]: int(row[1]) for row in cur.fetchall()})
        return counts


def fetch_ra_pending(conn: Any) -> dict[str, int]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT m.peer_name, COUNT(*)::int
            FROM queue q
            JOIN messages m ON m.id = q.message_id
            WHERE NOT q.processed
              AND m.peer_name IN ('ra_us', 'ra_eu', 'ra_kr')
            GROUP BY m.peer_name
            """
        )
        counts = {"ra_us": 0, "ra_eu": 0, "ra_kr": 0}
        counts.update({row[0]: int(row[1]) for row in cur.fetchall()})
        return counts


def fetch_source_coverage(conn: Any) -> dict[str, Any]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT
              COUNT(DISTINCT source_path) FILTER (
                WHERE source_path ILIKE '%MFDS%'
                   OR source_path ILIKE '%KGMP%'
                   OR source_path ILIKE '%국내_MFDS%'
                   OR metadata::text ILIKE '%MFDS%'
                   OR metadata::text ILIKE '%KGMP%'
                   OR metadata::text ILIKE '%식약처%'
              )::int AS kr_sources,
              COUNT(*) FILTER (
                WHERE source_path ILIKE '%MFDS%'
                   OR source_path ILIKE '%KGMP%'
                   OR source_path ILIKE '%국내_MFDS%'
                   OR metadata::text ILIKE '%MFDS%'
                   OR metadata::text ILIKE '%KGMP%'
                   OR metadata::text ILIKE '%식약처%'
              )::int AS kr_chunks,
              COUNT(DISTINCT source_path)::int AS total_sources,
              COUNT(*)::int AS total_chunks
            FROM ra_knowledge
            """
        )
        coverage = dict(cur.fetchone())
        cur.execute(
            """
            SELECT source_path, COUNT(*)::int AS chunks
            FROM ra_knowledge
            WHERE source_path IS NOT NULL
              AND source_path <> ''
              AND source_path NOT ILIKE '%/wiki/entities/%'
              AND (
                source_path ILIKE '%MFDS%'
                OR source_path ILIKE '%KGMP%'
                OR source_path ILIKE '%국내_MFDS%'
                OR metadata::text ILIKE '%MFDS%'
                OR metadata::text ILIKE '%KGMP%'
                OR metadata::text ILIKE '%식약처%'
              )
            GROUP BY source_path
            ORDER BY chunks DESC, source_path ASC
            LIMIT 20
            """
        )
        coverage["top_kr_sources"] = [dict(row) for row in cur.fetchall()]
        return coverage


def curriculum_gap(conn: Any, curriculum: Any) -> dict[str, Any]:
    agent = curriculum.AGENTS["ra-kr"]
    scopes: dict[str, Any] = {}
    for scope, limit in (("explicit", 80), ("shared", 80), ("all", 120)):
        candidates = curriculum.fetch_source_candidates(conn, agent, scope, limit, include_entities=False)
        existing = curriculum.fetch_existing_hashes(conn, agent)
        new_candidates = [candidate for candidate in candidates if candidate.source_hash not in existing]
        scopes[scope] = {
            "candidates": len(candidates),
            "already_seeded": len(candidates) - len(new_candidates),
            "to_seed": len(new_candidates),
            "preview": [
                {
                    "source": candidate.source_path,
                    "chunks": candidate.chunk_count,
                    "matched_keywords": list(candidate.matched_keywords),
                }
                for candidate in new_candidates[:10]
            ],
        }
    return scopes


def daily_plan(conn: Any, daily: Any, run_date: str) -> dict[str, Any]:
    class Args:
        date = run_date
        operation_timezone = DEFAULT_OPERATION_TIMEZONE
        agent = "ra-kr"
        cases_per_agent = 5
        source_pool = 40
        max_chunks_per_case = 2
        manual_growth_complete = True
        max_pending = 0
        execute = False

    plan = daily.build_plan(Args())
    return {
        "run_date": plan["run_date"],
        "planned_case_count": plan["planned_case_count"],
        "skipped_existing": plan["skipped_existing"],
        "execute_gate": plan["execute_gate"],
        "planned_cases": plan["planned_cases"].get("ra_kr", []),
    }


def autonomous_study_plan(conn: Any, study: Any) -> dict[str, Any]:
    checkpoint = study.load_checkpoint()
    since_ts = checkpoint.get("last_delta_ts") or checkpoint.get("last_bootstrap_ts")
    mode = "delta" if since_ts else "bootstrap"
    limit = study.MAX_CHUNKS_PER_SESSION if mode == "delta" else study.BOOTSTRAP_MAX
    chunks = study.fetch_chunks_for_agent("ra-kr", since_ts=since_ts, limit=limit)
    batches = (len(chunks) + study.CHUNK_BATCH_SIZE - 1) // study.CHUNK_BATCH_SIZE
    return {
        "mode": mode,
        "since_ts": since_ts,
        "chunk_limit": limit,
        "candidate_chunks": len(chunks),
        "batch_size": study.CHUNK_BATCH_SIZE,
        "estimated_batches": batches,
        "estimated_llm_calls": len(chunks),
        "preview_sources": [
            {
                "id": str(chunk.get("id", "")),
                "source": str(chunk.get("source_path", "")),
                "indexed_at": str(chunk.get("indexed_at", "")),
            }
            for chunk in chunks[:10]
        ],
    }


def recommendation(report: dict[str, Any]) -> dict[str, Any]:
    curriculum_all = report["curriculum_gap"]["all"]
    daily = report["daily_plan"]
    study = report["autonomous_study_plan"]
    self_docs = report["self_docs"]

    options: list[dict[str, Any]] = []
    options.append({
        "option": "daily_case_burst",
        "write_required": True,
        "expected_queue_rows": daily["planned_case_count"],
        "risk": "low",
        "fit": "good for immediate KR-specific source rotation if approved",
    })
    options.append({
        "option": "additional_curriculum_seed",
        "write_required": True,
        "expected_queue_rows": curriculum_all["to_seed"],
        "risk": "medium" if curriculum_all["to_seed"] > 20 else "low",
        "fit": "good if unseeded KR/shared sources remain",
    })
    options.append({
        "option": "autonomous_study_delta",
        "write_required": True,
        "expected_llm_calls": study["estimated_llm_calls"],
        "risk": "high" if study["estimated_llm_calls"] > 50 else "medium",
        "fit": "best for deep reasoning but slowest and highest queue/LLM load",
    })

    if self_docs["ra_kr"] < 500 and daily["planned_case_count"] > 0:
        preferred = "approved_daily_case_burst_first"
    elif curriculum_all["to_seed"] > 0:
        preferred = "approved_additional_curriculum_seed"
    else:
        preferred = "autonomous_study_delta_after_manual_review"

    return {
        "preferred_next_step": preferred,
        "timer_policy": "keep_off",
        "approval_required_before_write": True,
        "options": options,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--operation-timezone", default=DEFAULT_OPERATION_TIMEZONE)
    parser.add_argument("--date", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    env = load_env_file()
    run_date = args.date or datetime.now(ZoneInfo(args.operation_timezone)).date().isoformat()
    output = Path(args.output) if args.output else REPORTS_DIR / f"ra-kr-growth-plan-{run_date}.json"
    output.parent.mkdir(parents=True, exist_ok=True)

    curriculum = load_module("curriculum_seed", CURRICULUM)
    daily = load_module("daily_growth_runner", DAILY)
    study = load_module("autonomous_study_scheduler", STUDY)
    curriculum.validate_agent_config()
    daily.validate_agent_config()
    study.validate_agent_config()

    with connect(env) as conn:
        report: dict[str, Any] = {
            "record_type": "ra_kr_growth_plan",
            "issue": "59",
            "created_at": datetime.now(ZoneInfo(args.operation_timezone)).isoformat(),
            "operation_timezone": args.operation_timezone,
            "run_date": run_date,
            "timer_policy": "keep_off",
            "self_docs": fetch_self_docs(conn),
            "ra_pending": fetch_ra_pending(conn),
            "source_coverage": fetch_source_coverage(conn),
            "curriculum_gap": curriculum_gap(conn, curriculum),
            "daily_plan": daily_plan(conn, daily, run_date),
            "autonomous_study_plan": autonomous_study_plan(conn, study),
        }
    report["recommendation"] = recommendation(report)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({
        "report": str(output),
        "preferred_next_step": report["recommendation"]["preferred_next_step"],
        "self_docs": report["self_docs"],
        "daily_planned": report["daily_plan"]["planned_case_count"],
        "curriculum_all_to_seed": report["curriculum_gap"]["all"]["to_seed"],
        "study_candidate_chunks": report["autonomous_study_plan"]["candidate_chunks"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
