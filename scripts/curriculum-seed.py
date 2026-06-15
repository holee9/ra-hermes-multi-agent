#!/usr/bin/env python3
"""Seed source-level curriculum cards from ra_knowledge into Honcho peers.

This is intentionally deterministic and fast: it does not call an LLM. It turns
already-indexed source chunks into clean, memory-derivable Honcho messages so the
deriver can build initial source awareness before slower autonomous study runs.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Iterable

import psycopg2
import psycopg2.extras
import requests


HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WS", "work")
PG_DSN = os.environ.get("POSTGRES_URL", "")
CURRICULUM_VERSION = "source_curriculum_v1"


@dataclass(frozen=True)
class Agent:
    profile_id: str
    peer_id: str
    name: str
    region: str
    explicit_keywords: tuple[str, ...]
    shared_keywords: tuple[str, ...]


@dataclass(frozen=True)
class SourceCandidate:
    source_path: str
    chunk_count: int
    source_hash: str
    first_indexed_at: str
    last_indexed_at: str
    matched_keywords: tuple[str, ...]


AGENTS: dict[str, Agent] = {
    "ra-us": Agent(
        profile_id="ra-us",
        peer_id="ra_us",
        name="Mike",
        region="US",
        explicit_keywords=(
            "FDA",
            "510k",
            "510(k)",
            "De Novo",
            "PMA",
            "QSR",
            "QMSR",
        ),
        shared_keywords=(
            "ISO",
            "IEC",
            "QMS",
            "CAPA",
            "PMS",
            "clinical",
            "risk",
            "cybersecurity",
            "software",
        ),
    ),
    "ra-eu": Agent(
        profile_id="ra-eu",
        peer_id="ra_eu",
        name="Theo",
        region="EU",
        explicit_keywords=(
            "MDR",
            "IVDR",
            "EUDAMED",
            "Notified Body",
            "MDCG",
        ),
        shared_keywords=(
            "ISO",
            "IEC",
            "QMS",
            "CAPA",
            "PMS",
            "clinical",
            "risk",
            "cybersecurity",
            "software",
        ),
    ),
    "ra-kr": Agent(
        profile_id="ra-kr",
        peer_id="ra_kr",
        name="Sam",
        region="KR",
        explicit_keywords=(
            "MFDS",
            "KGMP",
            "식약처",
            "국내_MFDS",
            "의료기기법",
            "디지털의료제품법",
        ),
        shared_keywords=(
            "ISO",
            "IEC",
            "QMS",
            "CAPA",
            "PMS",
            "clinical",
            "risk",
            "cybersecurity",
            "software",
        ),
    ),
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(2)


def validate_agent_config() -> None:
    for key, agent in AGENTS.items():
        if key != agent.profile_id:
            fail(f"agent key/profile mismatch: {key} != {agent.profile_id}")
        if "-" not in agent.profile_id:
            fail(f"profile_id must use hyphen convention: {agent.profile_id}")
        if "-" in agent.peer_id or "_" not in agent.peer_id:
            fail(f"peer_id must use underscore Honcho convention: {agent.peer_id}")
        if agent.profile_id == agent.peer_id:
            fail(f"profile_id and peer_id must be distinct: {agent}")


def keywords_for_scope(agent: Agent, scope: str) -> tuple[str, ...]:
    if scope == "explicit":
        return agent.explicit_keywords
    if scope == "shared":
        return agent.shared_keywords
    if scope == "all":
        return tuple(dict.fromkeys(agent.explicit_keywords + agent.shared_keywords))
    fail(f"invalid scope: {scope}")
    return ()


def compact_text(value: Any, max_chars: int) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def find_matches(text: str, keywords: Iterable[str]) -> tuple[str, ...]:
    haystack = text.casefold()
    matches = [word for word in keywords if word.casefold() in haystack]
    return tuple(dict.fromkeys(matches))


def source_hash_from_chunks(chunks: list[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for chunk in sorted(chunks, key=lambda row: str(row.get("id", ""))):
        digest.update(str(chunk.get("id", "")).encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(chunk.get("content", "")).encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def build_source_where(keywords: tuple[str, ...]) -> tuple[str, list[str]]:
    conditions: list[str] = []
    params: list[str] = []
    for keyword in keywords:
        conditions.append("(source_path ILIKE %s OR metadata::text ILIKE %s)")
        pattern = f"%{keyword}%"
        params.extend([pattern, pattern])
    return " OR ".join(conditions), params


def fetch_source_candidates(
    conn: Any,
    agent: Agent,
    scope: str,
    limit_sources: int,
    include_entities: bool,
) -> list[SourceCandidate]:
    keywords = keywords_for_scope(agent, scope)
    where_sql, params = build_source_where(keywords)
    entity_filter = ""
    if not include_entities:
        entity_filter = "AND source_path NOT ILIKE %s"
        params.append("%/wiki/entities/%")
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            f"""
            SELECT
              source_path,
              COUNT(*)::int AS chunk_count,
              MIN(indexed_at)::text AS first_indexed_at,
              MAX(indexed_at)::text AS last_indexed_at
            FROM ra_knowledge
            WHERE source_path IS NOT NULL
              AND source_path <> ''
              AND ({where_sql})
              {entity_filter}
            GROUP BY source_path
            ORDER BY COUNT(*) DESC, source_path ASC
            LIMIT %s
            """,
            [*params, limit_sources],
        )
        rows = [dict(row) for row in cur.fetchall()]

    candidates: list[SourceCandidate] = []
    for row in rows:
        chunks = fetch_source_chunks(conn, row["source_path"], max_chunks=10_000)
        source_text = " ".join([
            row["source_path"],
            " ".join(str(chunk.get("metadata", "")) for chunk in chunks[:10]),
        ])
        candidates.append(
            SourceCandidate(
                source_path=row["source_path"],
                chunk_count=int(row["chunk_count"]),
                source_hash=source_hash_from_chunks(chunks),
                first_indexed_at=row["first_indexed_at"],
                last_indexed_at=row["last_indexed_at"],
                matched_keywords=find_matches(source_text, keywords),
            )
        )
    return candidates


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


def fetch_existing_hashes(conn: Any, agent: Agent) -> set[str]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT metadata->>'source_hash'
            FROM messages
            WHERE workspace_name = %s
              AND peer_name = %s
              AND metadata->>'record_type' = 'curriculum_seed'
              AND metadata->>'curriculum_version' = %s
              AND metadata->>'source_hash' IS NOT NULL
            """,
            (HONCHO_WS, agent.peer_id, CURRICULUM_VERSION),
        )
        return {row[0] for row in cur.fetchall()}


def build_session_name(agent: Agent, run_date: str) -> str:
    return f"study-{agent.peer_id}-curriculum-seed-{run_date}"


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


def ensure_session(agent: Agent, session_name: str, run_ts: str, scope: str) -> None:
    response = honcho_get(f"/v3/workspaces/{HONCHO_WS}/sessions/{session_name}")
    if response.status_code == 200:
        return
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
                "session_type": "curriculum_seed",
                "curriculum_version": CURRICULUM_VERSION,
                "scope": scope,
                "run_ts": run_ts,
            },
        },
    )


def format_curriculum_content(
    agent: Agent,
    candidate: SourceCandidate,
    chunks: list[dict[str, Any]],
    run_ts: str,
    max_snippet_chars: int,
) -> str:
    excerpt_lines: list[str] = []
    for index, chunk in enumerate(chunks, start=1):
        excerpt_lines.extend([
            f"[{index}] Chunk ID: {chunk.get('id', '')}",
            f"Excerpt: {compact_text(chunk.get('content', ''), max_snippet_chars)}",
        ])

    keyword_text = ", ".join(candidate.matched_keywords) or "source routing match"
    return "\n".join([
        "Regulatory source curriculum seed",
        f"Audience: {agent.name} ({agent.region} RA)",
        f"Curriculum version: {CURRICULUM_VERSION}",
        f"Source: {candidate.source_path}",
        f"Source hash: {candidate.source_hash}",
        f"Source indexed range: {candidate.first_indexed_at} to {candidate.last_indexed_at}",
        f"Chunk coverage: sampled {len(chunks)} of {candidate.chunk_count}",
        f"Priority reason: matched {keyword_text}",
        "Study objective: build source-level recall before case work; extract definitions, obligations, evidence requirements, timing, exceptions, and human-escalation triggers.",
        "Key excerpts:",
        *excerpt_lines,
        "Required follow-up: derive stable memory from this source only, cite source path and chunk IDs when reused, and escalate uncertain regulatory interpretation to human review.",
        f"Run timestamp: {run_ts}",
    ])


def build_message(
    agent: Agent,
    candidate: SourceCandidate,
    chunks: list[dict[str, Any]],
    run_ts: str,
    scope: str,
    source_rank: int,
    max_snippet_chars: int,
) -> dict[str, Any]:
    content = format_curriculum_content(agent, candidate, chunks, run_ts, max_snippet_chars)
    if content.lstrip().startswith("{"):
        fail("curriculum content must not be a JSON envelope")
    return {
        "content": content,
        "peer_id": agent.peer_id,
        "metadata": {
            "record_type": "curriculum_seed",
            "actor": agent.peer_id,
            "peer_id": agent.peer_id,
            "profile_id": agent.profile_id,
            "curriculum_version": CURRICULUM_VERSION,
            "scope": scope,
            "source": candidate.source_path,
            "source_hash": candidate.source_hash,
            "source_rank": source_rank,
            "chunk_count": candidate.chunk_count,
            "sampled_chunk_count": len(chunks),
            "matched_keywords": list(candidate.matched_keywords),
            "first_indexed_at": candidate.first_indexed_at,
            "last_indexed_at": candidate.last_indexed_at,
            "run_ts": run_ts,
        },
    }


def post_messages(session_name: str, messages: list[dict[str, Any]]) -> None:
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions/{session_name}/messages",
        {"messages": messages},
    )


def chunked(items: list[dict[str, Any]], batch_size: int) -> Iterable[list[dict[str, Any]]]:
    for index in range(0, len(items), batch_size):
        yield items[index : index + batch_size]


def select_agents(agent_arg: str) -> list[Agent]:
    if agent_arg == "all":
        return list(AGENTS.values())
    agent = AGENTS.get(agent_arg)
    if agent is None:
        fail(f"unknown agent: {agent_arg}")
    return [agent]


def run(args: argparse.Namespace) -> None:
    validate_agent_config()
    if args.limit_sources < 1:
        fail("--limit-sources must be >= 1")
    if args.max_chunks_per_source < 1:
        fail("--max-chunks-per-source must be >= 1")
    if args.batch_size < 1:
        fail("--batch-size must be >= 1")
    if args.max_snippet_chars < 120:
        fail("--max-snippet-chars must be >= 120")
    if not PG_DSN:
        fail("POSTGRES_URL is required")

    run_ts = datetime.now(timezone.utc).isoformat()
    run_date = run_ts[:10]
    total_written = 0
    total_skipped = 0

    with psycopg2.connect(PG_DSN) as conn:
        for agent in select_agents(args.agent):
            existing_hashes = fetch_existing_hashes(conn, agent)
            candidates = fetch_source_candidates(
                conn=conn,
                agent=agent,
                scope=args.scope,
                limit_sources=args.limit_sources,
                include_entities=args.include_entities,
            )
            new_candidates = [
                candidate for candidate in candidates
                if candidate.source_hash not in existing_hashes
            ]
            skipped = len(candidates) - len(new_candidates)
            total_skipped += skipped

            print(
                f"{agent.peer_id}: candidates={len(candidates)} "
                f"already_seeded={skipped} to_seed={len(new_candidates)} scope={args.scope}"
            )
            for rank, candidate in enumerate(new_candidates[: args.preview], start=1):
                print(
                    f"  {rank}. chunks={candidate.chunk_count} "
                    f"matches={','.join(candidate.matched_keywords) or '-'} "
                    f"source={candidate.source_path}"
                )

            if not args.execute:
                continue

            session_name = build_session_name(agent, run_date)
            ensure_session(agent, session_name, run_ts, args.scope)

            messages: list[dict[str, Any]] = []
            for rank, candidate in enumerate(new_candidates, start=1):
                chunks = fetch_source_chunks(conn, candidate.source_path, args.max_chunks_per_source)
                messages.append(
                    build_message(
                        agent=agent,
                        candidate=candidate,
                        chunks=chunks,
                        run_ts=run_ts,
                        scope=args.scope,
                        source_rank=rank,
                        max_snippet_chars=args.max_snippet_chars,
                    )
                )

            written_for_agent = 0
            for batch in chunked(messages, args.batch_size):
                post_messages(session_name, batch)
                written_for_agent += len(batch)
                total_written += len(batch)
                print(f"{agent.peer_id}: wrote {written_for_agent}/{len(messages)}")

    if not args.execute:
        print("dry-run only; pass --execute to write curriculum_seed messages")
    print(f"complete written={total_written} skipped={total_skipped}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", default="ra-kr", choices=["ra-us", "ra-eu", "ra-kr", "all"])
    parser.add_argument("--scope", default="explicit", choices=["explicit", "shared", "all"])
    parser.add_argument("--limit-sources", type=int, default=30)
    parser.add_argument("--max-chunks-per-source", type=int, default=5)
    parser.add_argument("--max-snippet-chars", type=int, default=700)
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--preview", type=int, default=10)
    parser.add_argument(
        "--include-entities",
        action="store_true",
        help="Allow low-level wiki/entities sources; excluded by default for precision",
    )
    parser.add_argument("--execute", action="store_true", help="Write curriculum_seed messages")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
