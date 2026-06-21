#!/usr/bin/env python3
"""Plan or run daily KB-driven growth routines for RA agents.

This runner is intentionally dry-run first. It prepares non-email-dependent
growth work from ra_knowledge, but execute mode is gated until manual growth and
deriver backlog are complete.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo

import psycopg2
import psycopg2.extras
import requests


HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WS", os.environ.get("HONCHO_WORKSPACE", "work"))
PG_DSN = os.environ.get("POSTGRES_URL", "")
GROWTH_VERSION = "daily_growth_v1"
REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
DEFAULT_OPERATION_TIMEZONE = os.environ.get("AUTO_GROWTH_OPERATION_TZ", "Asia/Seoul")


@dataclass(frozen=True)
class Agent:
    profile_id: str
    peer_id: str
    name: str
    region: str
    keywords: tuple[str, ...]
    daily_focus: tuple[str, ...]


@dataclass(frozen=True)
class SourceCase:
    scenario_id: str
    source_path: str
    source_hash: str
    chunk_count: int
    matched_keywords: tuple[str, ...]
    excerpts: tuple[dict[str, str], ...]


AGENTS: dict[str, Agent] = {
    "ra-us": Agent(
        profile_id="ra-us",
        peer_id="ra_us",
        name="Mike",
        region="US",
        keywords=("FDA", "510k", "510(k)", "De Novo", "PMA", "QSR", "QMSR"),
        daily_focus=(
            "510(k) predicate strategy",
            "submission evidence gaps",
            "QMSR and design-control readiness",
            "SaMD change impact",
        ),
    ),
    "ra-eu": Agent(
        profile_id="ra-eu",
        peer_id="ra_eu",
        name="Theo",
        region="EU",
        keywords=("MDR", "IVDR", "MDCG", "EUDAMED", "Notified Body"),
        daily_focus=(
            "MDR classification and conformity route",
            "clinical evaluation gap analysis",
            "PMS and PMCF planning",
            "Notified Body question response",
        ),
    ),
    "ra-kr": Agent(
        profile_id="ra-kr",
        peer_id="ra_kr",
        name="Sam",
        region="KR",
        keywords=("MFDS", "KGMP", "식약처", "국내_MFDS", "디지털의료제품법", "의료기기법"),
        daily_focus=(
            "MFDS classification and licensing route",
            "KGMP evidence readiness",
            "digital medical products act impact",
            "supplementary-response strategy",
        ),
    ),
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(2)


# @MX:WARN: [AUTO] daily-growth-runner — large file; config invariants centralized here
# @MX:REASON: 554-line script (line_count_warn threshold). Per-function complexity is low, but validate_agent_config is the shared peer_id/agent-config gate also exercised by ra-kr-growth-plan and autonomous-study-scheduler — changes ripple across the growth loop.
def validate_agent_config() -> None:
    peer_ids: set[str] = set()
    for key, agent in AGENTS.items():
        if key != agent.profile_id:
            fail(f"agent key/profile mismatch: {key} != {agent.profile_id}")
        if "-" not in agent.profile_id:
            fail(f"profile_id must be hyphenated: {agent.profile_id}")
        if "-" in agent.peer_id or "_" not in agent.peer_id:
            fail(f"peer_id must use underscore Honcho convention: {agent.peer_id}")
        if agent.profile_id == agent.peer_id:
            fail(f"profile_id and peer_id must be distinct: {agent}")
        if agent.peer_id in peer_ids:
            fail(f"duplicate peer_id: {agent.peer_id}")
        peer_ids.add(agent.peer_id)


def compact_text(value: Any, max_chars: int = 650) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def find_matches(text: str, keywords: Iterable[str]) -> tuple[str, ...]:
    haystack = text.casefold()
    return tuple(dict.fromkeys(word for word in keywords if word.casefold() in haystack))


def source_hash(chunks: list[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for chunk in sorted(chunks, key=lambda row: str(row.get("id", ""))):
        digest.update(str(chunk.get("id", "")).encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(chunk.get("content", "")).encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def build_keyword_where(keywords: tuple[str, ...]) -> tuple[str, list[str]]:
    clauses: list[str] = []
    params: list[str] = []
    for keyword in keywords:
        clauses.append("(source_path ILIKE %s OR metadata::text ILIKE %s)")
        pattern = f"%{keyword}%"
        params.extend([pattern, pattern])
    return " OR ".join(clauses), params


def fetch_queue_status(conn: Any) -> dict[str, dict[str, int]]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT m.peer_name,
                   COALESCE(m.metadata->>'record_type', '') AS record_type,
                   q.processed,
                   COUNT(*)::int AS count
            FROM queue q
            JOIN messages m ON m.id = q.message_id
            WHERE m.peer_name = ANY(%s)
            GROUP BY m.peer_name, COALESCE(m.metadata->>'record_type', ''), q.processed
            ORDER BY m.peer_name, record_type, q.processed
            """,
            ([agent.peer_id for agent in AGENTS.values()],),
        )
        rows = [dict(row) for row in cur.fetchall()]

    status = {agent.peer_id: {"pending": 0, "processed": 0} for agent in AGENTS.values()}
    for row in rows:
        peer = row["peer_name"]
        bucket = "processed" if row["processed"] else "pending"
        status.setdefault(peer, {"pending": 0, "processed": 0})
        status[peer][bucket] += int(row["count"])
    return status


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
            """,
            ([agent.peer_id for agent in AGENTS.values()],),
        )
        return {row[0]: row[1] for row in cur.fetchall()}


def fetch_source_paths(conn: Any, agent: Agent, limit: int) -> list[str]:
    where_sql, params = build_keyword_where(agent.keywords)
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT source_path
            FROM ra_knowledge
            WHERE source_path IS NOT NULL
              AND source_path <> ''
              AND source_path NOT ILIKE %s
              AND ({where_sql})
            GROUP BY source_path
            ORDER BY COUNT(*) DESC, source_path ASC
            LIMIT %s
            """,
            ["%/wiki/entities/%", *params, limit],
        )
        return [row[0] for row in cur.fetchall()]


def fetch_source_chunks(conn: Any, source_path: str, max_chunks: int) -> list[dict[str, Any]]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT id::text, content, metadata, indexed_at::text AS indexed_at
            FROM ra_knowledge
            WHERE source_path = %s
            ORDER BY indexed_at ASC, id::text ASC
            LIMIT %s
            """,
            (source_path, max_chunks),
        )
        return [dict(row) for row in cur.fetchall()]


def scenario_id_for(run_date: date, agent: Agent, source_path: str) -> str:
    raw = f"{GROWTH_VERSION}:{run_date.isoformat()}:{agent.peer_id}:{source_path}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def select_daily_cases(
    conn: Any,
    agent: Agent,
    run_date: date,
    cases_per_agent: int,
    source_pool: int,
    max_chunks: int,
) -> list[SourceCase]:
    paths = fetch_source_paths(conn, agent, source_pool)
    if not paths:
        return []
    offset = run_date.toordinal() % len(paths)
    rotated = paths[offset:] + paths[:offset]
    cases: list[SourceCase] = []
    for source_path in rotated:
        chunks = fetch_source_chunks(conn, source_path, max_chunks)
        if not chunks:
            continue
        matched = find_matches(source_path + " " + " ".join(str(c.get("metadata", "")) for c in chunks), agent.keywords)
        excerpts = tuple(
            {"id": str(chunk.get("id", "")), "excerpt": compact_text(chunk.get("content", ""))}
            for chunk in chunks
        )
        cases.append(
            SourceCase(
                scenario_id=scenario_id_for(run_date, agent, source_path),
                source_path=source_path,
                source_hash=source_hash(chunks),
                chunk_count=len(chunks),
                matched_keywords=matched,
                excerpts=excerpts,
            )
        )
        if len(cases) >= cases_per_agent:
            break
    return cases


def fetch_existing_scenarios(conn: Any, run_date: date) -> set[str]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT metadata->>'scenario_id'
            FROM messages
            WHERE workspace_name = %s
              AND metadata->>'record_type' = 'daily_growth_case'
              AND metadata->>'growth_version' = %s
              AND metadata->>'run_date' = %s
              AND metadata->>'scenario_id' IS NOT NULL
            """,
            (HONCHO_WS, GROWTH_VERSION, run_date.isoformat()),
        )
        return {row[0] for row in cur.fetchall()}


def build_case_content(agent: Agent, case: SourceCase, run_date: date) -> str:
    focus = agent.daily_focus[run_date.toordinal() % len(agent.daily_focus)]
    lines = [
        "Daily regulatory growth case",
        f"Audience: {agent.name} ({agent.region} RA)",
        f"Growth version: {GROWTH_VERSION}",
        f"Run date: {run_date.isoformat()}",
        f"Scenario ID: {case.scenario_id}",
        f"Primary focus: {focus}",
        f"Source: {case.source_path}",
        f"Source hash: {case.source_hash}",
        f"Matched keywords: {', '.join(case.matched_keywords) or 'source routing match'}",
        "Assignment: Produce a regulatory draft that identifies classification/submission route, required evidence, missing information, risk controls, citations, and human-escalation triggers.",
        "Peer review prompt: Ask one other RA peer to challenge the assumptions, source coverage, and jurisdiction-specific gaps.",
        "Source excerpts:",
    ]
    for index, excerpt in enumerate(case.excerpts, start=1):
        lines.extend([
            f"[{index}] Chunk ID: {excerpt['id']}",
            f"Excerpt: {excerpt['excerpt']}",
        ])
    lines.append("Required memory outcome: record the final lesson as reusable RA judgment, not as a raw transcript.")
    content = "\n".join(lines)
    if content.lstrip().startswith("{"):
        fail("daily growth case content must not be a JSON envelope")
    return content


def build_message(agent: Agent, case: SourceCase, run_date: date) -> dict[str, Any]:
    return {
        "content": build_case_content(agent, case, run_date),
        "peer_id": agent.peer_id,
        "metadata": {
            "record_type": "daily_growth_case",
            "actor": agent.peer_id,
            "peer_id": agent.peer_id,
            "profile_id": agent.profile_id,
            "growth_version": GROWTH_VERSION,
            "run_date": run_date.isoformat(),
            "scenario_id": case.scenario_id,
            "source": case.source_path,
            "source_hash": case.source_hash,
            "matched_keywords": list(case.matched_keywords),
            "issue": "51",
        },
    }


def honcho_get(path: str) -> requests.Response:
    return requests.get(f"{HONCHO_URL}{path}", timeout=20)


def honcho_post(path: str, body: dict[str, Any]) -> dict[str, Any]:
    response = requests.post(
        f"{HONCHO_URL}{path}",
        headers={"Content-Type": "application/json"},
        json=body,
        timeout=60,
    )
    response.raise_for_status()
    return response.json()


def ensure_session(agent: Agent, run_date: date) -> str:
    session_name = f"growth-{agent.peer_id}-daily-{run_date.isoformat()}"
    response = honcho_get(f"/v3/workspaces/{HONCHO_WS}/sessions/{session_name}")
    if response.status_code == 200:
        return session_name
    if response.status_code not in {404, 405}:
        response.raise_for_status()
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions",
        {
            "id": session_name,
            "metadata": {
                "actor": agent.peer_id,
                "peer_id": agent.peer_id,
                "profile_id": agent.profile_id,
                "session_type": "daily_growth",
                "growth_version": GROWTH_VERSION,
                "run_date": run_date.isoformat(),
                "issue": "51",
            },
        },
    )
    return session_name


def post_messages(session_name: str, messages: list[dict[str, Any]]) -> None:
    if not messages:
        return
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions/{session_name}/messages",
        {"messages": messages},
    )


def operational_today(timezone_name: str = DEFAULT_OPERATION_TIMEZONE) -> date:
    try:
        return datetime.now(ZoneInfo(timezone_name)).date()
    except Exception as exc:
        fail(f"invalid operation timezone: {timezone_name}: {exc}")


def parse_run_date(value: str | None, timezone_name: str = DEFAULT_OPERATION_TIMEZONE) -> date:
    if not value:
        return operational_today(timezone_name)
    return datetime.strptime(value, "%Y-%m-%d").date()


def select_agents(agent_arg: str) -> list[Agent]:
    if agent_arg == "all":
        return list(AGENTS.values())
    agent = AGENTS.get(agent_arg)
    if agent is None:
        fail(f"unknown agent: {agent_arg}")
    return [agent]


def build_plan(args: argparse.Namespace) -> dict[str, Any]:
    validate_agent_config()
    if not PG_DSN:
        fail("POSTGRES_URL is required")
    run_date = parse_run_date(args.date, args.operation_timezone)
    agents = select_agents(args.agent)

    with psycopg2.connect(PG_DSN) as conn:
        queue_status = fetch_queue_status(conn)
        self_docs = fetch_self_docs(conn)
        existing = fetch_existing_scenarios(conn, run_date)
        planned: dict[str, list[dict[str, Any]]] = {}
        skipped_existing = 0
        for agent in agents:
            cases = select_daily_cases(
                conn=conn,
                agent=agent,
                run_date=run_date,
                cases_per_agent=args.cases_per_agent,
                source_pool=args.source_pool,
                max_chunks=args.max_chunks_per_case,
            )
            planned[agent.peer_id] = []
            for case in cases:
                if case.scenario_id in existing:
                    skipped_existing += 1
                    continue
                planned[agent.peer_id].append(
                    {
                        "scenario_id": case.scenario_id,
                        "source": case.source_path,
                        "source_hash": case.source_hash,
                        "chunk_count": case.chunk_count,
                        "matched_keywords": list(case.matched_keywords),
                    }
                )

    pending_total = sum(queue_status.get(agent.peer_id, {}).get("pending", 0) for agent in agents)
    execute_gate = {
        "manual_growth_complete_required": True,
        "manual_growth_complete_provided": bool(args.manual_growth_complete),
        "pending_total": pending_total,
        "max_pending_allowed": args.max_pending,
        "allowed": bool(args.manual_growth_complete) and pending_total <= args.max_pending,
    }
    return {
        "run_date": run_date.isoformat(),
        "operation_timezone": args.operation_timezone,
        "growth_version": GROWTH_VERSION,
        "agent": args.agent,
        "execute_requested": bool(args.execute),
        "execute_gate": execute_gate,
        "queue_status": queue_status,
        "self_docs": self_docs,
        "planned_cases": planned,
        "planned_case_count": sum(len(items) for items in planned.values()),
        "skipped_existing": skipped_existing,
        "cadence": {
            "daily": "KB delta, source rotation, daily growth cases, deriver/backlog check",
            "weekly": "jurisdiction coverage audit and peer-review replay",
            "monthly": "human feedback review and SOUL/rule update candidates",
            "quarterly": "source freshness and regulatory baseline audit",
        },
    }


def execute_plan(args: argparse.Namespace, plan: dict[str, Any]) -> int:
    if not plan["execute_gate"]["allowed"]:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        fail("execute gate is closed; finish manual growth/backlog and pass --manual-growth-complete")

    run_date = parse_run_date(args.date, args.operation_timezone)
    agents = select_agents(args.agent)
    written = 0
    with psycopg2.connect(PG_DSN) as conn:
        existing = fetch_existing_scenarios(conn, run_date)
        for agent in agents:
            cases = select_daily_cases(
                conn=conn,
                agent=agent,
                run_date=run_date,
                cases_per_agent=args.cases_per_agent,
                source_pool=args.source_pool,
                max_chunks=args.max_chunks_per_case,
            )
            messages = [
                build_message(agent, case, run_date)
                for case in cases
                if case.scenario_id not in existing
            ]
            if not messages:
                continue
            session_name = ensure_session(agent, run_date)
            post_messages(session_name, messages)
            written += len(messages)
    return written


def write_report(plan: dict[str, Any], output: str | None) -> None:
    if not output:
        return
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"report={path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", default="all", choices=["ra-us", "ra-eu", "ra-kr", "all"])
    parser.add_argument("--date", default=None, help="Run date YYYY-MM-DD, default operation-timezone today")
    parser.add_argument("--operation-timezone", default=DEFAULT_OPERATION_TIMEZONE)
    parser.add_argument("--cases-per-agent", type=int, default=3)
    parser.add_argument("--source-pool", type=int, default=60)
    parser.add_argument("--max-chunks-per-case", type=int, default=3)
    parser.add_argument("--max-pending", type=int, default=0)
    parser.add_argument("--manual-growth-complete", action="store_true")
    parser.add_argument("--execute", action="store_true", help="Write daily_growth_case messages")
    parser.add_argument("--output", default=None, help="Optional JSON report path")
    args = parser.parse_args()

    if args.cases_per_agent < 1:
        fail("--cases-per-agent must be >= 1")
    if args.source_pool < args.cases_per_agent:
        fail("--source-pool must be >= --cases-per-agent")
    if args.max_chunks_per_case < 1:
        fail("--max-chunks-per-case must be >= 1")
    if args.max_pending < 0:
        fail("--max-pending must be >= 0")

    plan = build_plan(args)
    write_report(plan, args.output)
    if args.execute:
        written = execute_plan(args, plan)
        plan["written"] = written
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        print(f"complete written={written}")
        return

    print(json.dumps(plan, indent=2, ensure_ascii=False))
    print("dry-run only; pass --execute after manual growth is complete")


if __name__ == "__main__":
    main()
