#!/usr/bin/env python3
"""Replay #49 wrong-peer study insights into the correct Honcho peers.

This script does not mutate the old wrong-peer messages. It reads their JSON payloads,
normalizes them into memory-derivable text, and writes new messages to ra_us/ra_eu
with recovery metadata so the operation is idempotent.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from typing import Any

import psycopg2
import psycopg2.extras
import requests


HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WS", "work")
PG_DSN = os.environ.get("POSTGRES_URL", "")

ISSUE = "49"
RUN_DATE = "2026-06-13"


@dataclass(frozen=True)
class Agent:
    wrong_peer: str
    profile_id: str
    peer_id: str
    region: str
    name: str
    session_name: str


AGENTS = {
    "ra-us": Agent(
        wrong_peer="ra-us",
        profile_id="ra-us",
        peer_id="ra_us",
        region="US",
        name="Mike",
        session_name=f"study-ra_us-bootstrap-recovery-{RUN_DATE}",
    ),
    "ra-eu": Agent(
        wrong_peer="ra-eu",
        profile_id="ra-eu",
        peer_id="ra_eu",
        region="EU",
        name="Theo",
        session_name=f"study-ra_eu-bootstrap-recovery-{RUN_DATE}",
    ),
}


def clean_text(value: Any) -> str:
    return str(value or "").strip()


def confidence(value: Any) -> float:
    try:
        return max(0.0, min(1.0, float(value)))
    except (TypeError, ValueError):
        return 0.0


def format_recovered_content(agent: Agent, payload: dict[str, Any]) -> str:
    return "\n".join([
        "Regulatory knowledge seed",
        f"Audience: {agent.name} ({agent.region} RA)",
        f"Topic: {clean_text(payload.get('topic'))}",
        f"Finding: {clean_text(payload.get('finding'))}",
        f"Regulatory relevance: {clean_text(payload.get('relevance'))}",
        f"Operational hint: {clean_text(payload.get('action_hint'))}",
        f"Confidence: {confidence(payload.get('confidence')):.2f}",
        f"Source: {clean_text(payload.get('source'))}",
        f"Chunk ID: {clean_text(payload.get('chunk_id'))}",
    ])


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


def ensure_session(agent: Agent) -> None:
    path = f"/v3/workspaces/{HONCHO_WS}/sessions/{agent.session_name}"
    response = honcho_get(path)
    if response.status_code == 200:
        return
    if response.status_code not in {404, 405}:
        response.raise_for_status()
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions",
        {
            "id": agent.session_name,
            "metadata": {
                "actor": agent.peer_id,
                "peer_id": agent.peer_id,
                "profile_id": agent.profile_id,
                "session_type": "autonomous_study_recovery",
                "source_issue": ISSUE,
                "run_date": RUN_DATE,
            },
        },
    )


def fetch_source_messages(conn: Any) -> list[dict[str, Any]]:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT id, public_id, peer_name, content::jsonb AS content_json, created_at
            FROM messages
            WHERE peer_name IN ('ra-us', 'ra-eu')
              AND metadata->>'record_type' = 'study_insight'
              AND session_name LIKE 'study-ra-%bootstrap-2026-06-12'
            ORDER BY id ASC
            """
        )
        return [dict(row) for row in cur.fetchall()]


def fetch_replayed_ids(conn: Any) -> set[str]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT metadata->>'source_message_public_id'
            FROM messages
            WHERE metadata->>'recovered_from_issue' = %s
              AND metadata->>'source_message_public_id' IS NOT NULL
            """,
            (ISSUE,),
        )
        return {row[0] for row in cur.fetchall()}


def build_message(agent: Agent, source: dict[str, Any]) -> dict[str, Any]:
    content_json = source["content_json"]
    if isinstance(content_json, str):
        content_json = json.loads(content_json)
    payload = content_json.get("payload", {})
    source_public_id = source["public_id"]
    return {
        "content": format_recovered_content(agent, payload),
        "peer_id": agent.peer_id,
        "metadata": {
            "record_type": "study_insight",
            "actor": agent.peer_id,
            "peer_id": agent.peer_id,
            "profile_id": agent.profile_id,
            "source": clean_text(payload.get("source")),
            "chunk_id": clean_text(payload.get("chunk_id")),
            "topic": clean_text(payload.get("topic")),
            "confidence": confidence(payload.get("confidence")),
            "recovered_from_issue": ISSUE,
            "source_message_public_id": source_public_id,
            "source_message_db_id": source["id"],
            "source_peer_name": source["peer_name"],
            "source_actor": clean_text(payload.get("actor")),
            "source_run_ts": clean_text(content_json.get("ts")),
        },
    }


def post_batch(agent: Agent, messages: list[dict[str, Any]]) -> None:
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions/{agent.session_name}/messages",
        {"messages": messages},
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Write recovered messages")
    parser.add_argument("--batch-size", type=int, default=50)
    args = parser.parse_args()

    if not PG_DSN:
        print("POSTGRES_URL is required", file=sys.stderr)
        raise SystemExit(2)
    if args.batch_size < 1:
        print("--batch-size must be >= 1", file=sys.stderr)
        raise SystemExit(2)

    with psycopg2.connect(PG_DSN) as conn:
        source_messages = fetch_source_messages(conn)
        replayed_ids = fetch_replayed_ids(conn)

    candidates = [
        row for row in source_messages
        if row["public_id"] not in replayed_ids and row["peer_name"] in AGENTS
    ]

    by_peer: dict[str, int] = {}
    for row in candidates:
        by_peer[row["peer_name"]] = by_peer.get(row["peer_name"], 0) + 1

    print(f"source_messages={len(source_messages)} already_replayed={len(replayed_ids)} to_replay={len(candidates)}")
    for peer_name, count in sorted(by_peer.items()):
        print(f"{peer_name}: {count}")

    if not args.execute:
        print("dry-run only; pass --execute to write recovered messages")
        return

    for agent in AGENTS.values():
        ensure_session(agent)

    written = 0
    current_agent: Agent | None = None
    batch: list[dict[str, Any]] = []

    def flush() -> None:
        nonlocal batch, current_agent, written
        if not batch or current_agent is None:
            return
        post_batch(current_agent, batch)
        written += len(batch)
        print(f"wrote {written}/{len(candidates)}")
        batch = []

    for row in candidates:
        agent = AGENTS[row["peer_name"]]
        if current_agent is not None and agent.peer_id != current_agent.peer_id:
            flush()
        current_agent = agent
        batch.append(build_message(agent, row))
        if len(batch) >= args.batch_size:
            flush()

    flush()
    print(f"complete written={written}")


if __name__ == "__main__":
    main()
