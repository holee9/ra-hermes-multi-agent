"""autonomous-study-scheduler.py — RA agent autonomous learning loop.

Modes:
  bootstrap  First run: study all pgvector ra_knowledge chunks per agent.
  delta      Incremental run: only chunks added/updated since last checkpoint.

Per agent (ra-us/ra-eu/ra-kr):
  1. Pull relevant chunks from pgvector ra_knowledge (filtered by profile region).
  2. For each chunk batch, send a study prompt to hermes-api-server (/v1/chat/completions).
  3. Parse extracted insights from the response.
  4. Record insights as Honcho messages (type=study_insight) in a dedicated study session.
  5. Record session_complete summary message.

Peer exchange (post-study):
  After all three agents finish, each agent's top insights are cross-injected
  to the other two so they can build on each other's findings (e.g. Mike's FDA
  501(k) findings are shared with Theo/Sam for their EU/KR context).

Checkpoint:
  scripts/study-checkpoint.json — stores last_run_ts per mode so delta can filter.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

try:
    import psycopg2
    import psycopg2.extras
    _PSYCOPG2_OK = True
except ImportError:
    _PSYCOPG2_OK = False

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WS", "work")
HERMES_API_URL = os.environ.get("HERMES_API_URL", "http://localhost:8643")
HERMES_API_KEY = os.environ.get("API_SERVER_KEY", "")
# POSTGRES_URL must be set in scripts/.env (git-ignored) — no hardcoded default
PG_DSN = os.environ.get("POSTGRES_URL", "")
CHUNK_BATCH_SIZE = int(os.environ.get("STUDY_BATCH_SIZE", "5"))
MAX_CHUNKS_PER_SESSION = int(os.environ.get("STUDY_MAX_CHUNKS", "200"))
# Bootstrap fetches all available chunks; delta is bounded by MAX_CHUNKS_PER_SESSION
BOOTSTRAP_MAX = int(os.environ.get("STUDY_BOOTSTRAP_MAX", "9999"))
REQUEST_TIMEOUT = int(os.environ.get("STUDY_TIMEOUT", "120"))
# Seconds between Hermes API calls — prevents overloading GX10
CALL_DELAY = float(os.environ.get("STUDY_CALL_DELAY", "1.0"))

# Claude Code CLI backend — set USE_CLAUDE_CLI=1 to bypass hermes-api-server
CLAUDE_BIN = os.environ.get(
    "CLAUDE_BIN",
    "/home/abyz-lab/.npm-global/lib/node_modules/@anthropic-ai/claude-code"
    "/node_modules/@anthropic-ai/claude-code-linux-x64/claude",
)
USE_CLAUDE_CLI = bool(os.environ.get("USE_CLAUDE_CLI", ""))
SOUL_BASE_DIR = Path(os.environ.get("SOUL_BASE_DIR", "/home/abyz-lab/.hermes/profiles"))
_PROFILE_MAP: dict[str, str] = {"ra_us": "ra-us", "ra_eu": "ra-eu", "ra_kr": "ra-kr"}

CHECKPOINT_FILE = Path(__file__).parent / "study-checkpoint.json"
PROGRESS_FILE = Path(__file__).parent / "study-bootstrap-progress.json"

# Agents ordered for peer exchange
AGENTS: list[dict[str, str]] = [
    {"id": "ra-us", "model": "ra_us", "region": "US", "name": "Mike"},
    {"id": "ra-eu", "model": "ra_eu", "region": "EU", "name": "Theo"},
    {"id": "ra-kr", "model": "ra_kr", "region": "KR", "name": "Sam"},
]

# SQL region filters per agent — matches tags/source fields used at index time
REGION_FILTER: dict[str, list[str]] = {
    "ra-us": ["US", "FDA", "510k", "MDR", "global"],
    "ra-eu": ["EU", "CE", "MDR", "IVDR", "global"],
    "ra-kr": ["KR", "MFDS", "Korea", "global"],
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Checkpoint helpers
# ---------------------------------------------------------------------------

def load_checkpoint() -> dict:
    if CHECKPOINT_FILE.exists():
        try:
            return json.loads(CHECKPOINT_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_checkpoint(data: dict) -> None:
    CHECKPOINT_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("Checkpoint saved: %s", CHECKPOINT_FILE)


def load_bootstrap_progress() -> dict:
    """Load per-agent batch progress for resumable bootstrap runs."""
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_bootstrap_progress(agent_id: str, chunks_done: int, session_id: str, insights_count: int) -> None:
    """Persist per-agent progress after each batch so bootstrap can resume on restart."""
    progress = load_bootstrap_progress()
    progress[agent_id] = {
        "chunks_done": chunks_done,
        "session_id": session_id,
        "insights_count": insights_count,
    }
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# pgvector helpers
# ---------------------------------------------------------------------------

def fetch_chunks(since_ts: str | None = None, limit: int = MAX_CHUNKS_PER_SESSION) -> list[dict]:
    """Fetch ra_knowledge chunks. If since_ts given, only rows created after it."""
    if not _PSYCOPG2_OK:
        log.error("psycopg2 not installed — run: pip install psycopg2-binary")
        return []

    conn = None
    try:
        conn = psycopg2.connect(PG_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        if since_ts:
            cur.execute(
                """
                SELECT id, content, source_path, metadata, indexed_at
                FROM ra_knowledge
                WHERE indexed_at > %s
                ORDER BY indexed_at ASC
                LIMIT %s
                """,
                (since_ts, limit),
            )
        else:
            cur.execute(
                """
                SELECT id, content, source_path, metadata, indexed_at
                FROM ra_knowledge
                ORDER BY indexed_at ASC
                LIMIT %s
                """,
                (limit,),
            )

        rows = cur.fetchall()
        return [dict(r) for r in rows]
    except Exception as exc:
        log.error("pgvector query failed: %s", exc)
        return []
    finally:
        if conn:
            conn.close()


def fetch_chunks_for_agent(agent_id: str, since_ts: str | None = None,
                            limit: int = MAX_CHUNKS_PER_SESSION) -> list[dict]:
    """Fetch chunks relevant to the agent's region using ILIKE filters on source/metadata."""
    if not _PSYCOPG2_OK:
        log.error("psycopg2 not installed — run: pip install psycopg2-binary")
        return []

    regions = REGION_FILTER.get(agent_id, ["global"])
    # Build OR conditions for region matching in source or metadata JSONB
    conditions = " OR ".join(
        f"(source_path ILIKE %s OR metadata::text ILIKE %s)" for _ in regions
    )
    params: list[Any] = []
    for region in regions:
        params.extend([f"%{region}%", f"%{region}%"])

    if since_ts:
        params.append(since_ts)
        where = f"({conditions}) AND indexed_at > %s"
    else:
        where = f"({conditions})"

    params.append(limit)

    conn = None
    try:
        conn = psycopg2.connect(PG_DSN)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(
            f"SELECT id, content, source_path, metadata, indexed_at FROM ra_knowledge "  # noqa: S608
            f"WHERE {where} ORDER BY indexed_at ASC LIMIT %s",
            params,
        )
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    except Exception as exc:
        log.error("pgvector agent-filtered query failed (%s): %s", agent_id, exc)
        # Fallback: return unfiltered subset
        return fetch_chunks(since_ts=since_ts, limit=limit // 3)
    finally:
        if conn:
            conn.close()


# ---------------------------------------------------------------------------
# Hermes API helpers
# ---------------------------------------------------------------------------

def _hermes_headers() -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if HERMES_API_KEY:
        headers["Authorization"] = f"Bearer {HERMES_API_KEY}"
    return headers


def build_study_prompt(agent: dict, chunk: dict) -> str:
    """Build the study prompt for a single knowledge chunk."""
    agent_name = agent["name"]
    region = agent["region"]
    source = chunk.get("source", "unknown")
    content = chunk.get("content", "")
    return (
        f"[자율 학습 세션] {agent_name}({region} RA 전문가)로서 아래 지식베이스 내용을 분석해주세요.\n\n"
        f"출처: {source}\n"
        f"---\n{content[:3000]}\n---\n\n"
        "다음 형식으로 JSON을 반환하세요 (마크다운 없이 순수 JSON만):\n"
        '{"insights": ['
        '{"topic": "주제", "finding": "핵심 발견사항", "relevance": "규제 업무 연관성", '
        '"confidence": 0.0-1.0, "action_hint": "후속 조치 힌트(있으면)"}'
        ']}'
    )


def _load_soul(agent_model: str) -> str:
    profile = _PROFILE_MAP.get(agent_model, "ra-us")
    soul_path = SOUL_BASE_DIR / profile / "SOUL.md"
    try:
        return soul_path.read_text(encoding="utf-8")
    except OSError:
        return ""


# @MX:ANCHOR: [AUTO] call_hermes — hermes-api-server OpenAI-compatible call
# @MX:REASON: Called per chunk per agent; failure must not abort entire study loop
def call_hermes(agent: dict, user_message: str) -> str | None:
    """Call Claude Code CLI or hermes-api-server; return assistant content."""
    if USE_CLAUDE_CLI:
        soul = _load_soul(agent["model"])
        full_prompt = f"{soul}\n\n---\n\n{user_message}" if soul else user_message
        try:
            result = subprocess.run(
                [CLAUDE_BIN, "-p", full_prompt, "--model", "claude-haiku-4-5-20251001"],
                capture_output=True,
                text=True,
                timeout=REQUEST_TIMEOUT,
            )
            return result.stdout.strip() or None
        except Exception as exc:
            log.warning("claude -p error (%s): %s", agent["id"], exc)
            return None

    payload = {
        "model": agent["model"],
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.3,
        "max_tokens": 1024,
    }
    try:
        resp = requests.post(
            f"{HERMES_API_URL}/v1/chat/completions",
            headers=_hermes_headers(),
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except requests.RequestException as exc:
        log.warning("Hermes API error (%s): %s", agent["id"], exc)
        return None


def extract_insights(raw: str) -> list[dict]:
    """Parse JSON insight list from Hermes response. Returns [] on failure."""
    if not raw:
        return []
    # Strip potential markdown fences
    clean = raw.strip()
    if clean.startswith("```"):
        lines = clean.split("\n")
        clean = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    try:
        data = json.loads(clean)
        return data.get("insights", []) if isinstance(data, dict) else []
    except json.JSONDecodeError:
        # Try to extract JSON object from messy response
        m = re.search(r'\{.*"insights".*\}', clean, re.DOTALL)
        if m:
            try:
                data = json.loads(m.group(0))
                return data.get("insights", [])
            except json.JSONDecodeError:
                pass
    return []


# ---------------------------------------------------------------------------
# Honcho helpers
# ---------------------------------------------------------------------------

def _honcho_headers() -> dict[str, str]:
    return {"Content-Type": "application/json"}


def honcho_post(path: str, body: dict) -> dict | None:
    url = f"{HONCHO_URL}{path}"
    try:
        resp = requests.post(url, headers=_honcho_headers(), json=body, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        log.warning("Honcho POST %s failed: %s", path, exc)
        return None


def create_study_session(agent_id: str, mode: str, run_ts: str) -> str | None:
    """Get or create a Honcho session for this study run, return session id or None.

    Idempotent: if a session with today's name already exists, reuse it to avoid
    duplicate session records on repeated bootstrap runs within the same day.
    """
    session_name = f"study-{agent_id}-{mode}-{run_ts[:10]}"
    # Check if session already exists (idempotency guard)
    try:
        resp = requests.get(
            f"{HONCHO_URL}/v3/workspaces/{HONCHO_WS}/sessions/{session_name}",
            timeout=10,
        )
        if resp.status_code == 200:
            log.info("[%s] Reusing existing study session: %s", agent_id, session_name)
            return session_name
    except Exception:
        pass  # Fall through to create

    data = honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions",
        {
            "id": session_name,
            "metadata": {
                "actor": agent_id,
                "session_type": "autonomous_study",
                "mode": mode,
                "run_ts": run_ts,
            },
        },
    )
    return (data or {}).get("id")


def record_insight(session_id: str, agent_id: str, chunk: dict,
                   insight: dict, run_ts: str) -> None:
    """Record a single extracted insight as a Honcho message."""
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions/{session_id}/messages",
        {
            "messages": [{
                "content": json.dumps({
                    "ts": run_ts,
                    "type": "study_insight",
                    "actor": agent_id,
                    "payload": {
                        "actor": agent_id,
                        "source": chunk.get("source_path", ""),
                        "chunk_id": str(chunk.get("id", "")),
                        "topic": insight.get("topic", ""),
                        "finding": insight.get("finding", ""),
                        "relevance": insight.get("relevance", ""),
                        "confidence": insight.get("confidence", 0.0),
                        "action_hint": insight.get("action_hint", ""),
                    },
                }, ensure_ascii=False),
                "peer_id": agent_id,
                "metadata": {"record_type": "study_insight", "actor": agent_id},
            }],
        },
    )


def record_peer_insight(session_id: str, target_agent: str, source_agent: str,
                        insight: dict, run_ts: str) -> None:
    """Record a peer-exchanged insight to the target agent's study session."""
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions/{session_id}/messages",
        {
            "messages": [{
                "content": json.dumps({
                    "ts": run_ts,
                    "type": "study_insight",
                    "actor": target_agent,
                    "payload": {
                        "actor": target_agent,
                        "source_agent": source_agent,
                        "topic": insight.get("topic", ""),
                        "finding": insight.get("finding", ""),
                        "relevance": insight.get("relevance", ""),
                        "confidence": insight.get("confidence", 0.0),
                        "action_hint": insight.get("action_hint", ""),
                        "peer_exchange": True,
                    },
                }, ensure_ascii=False),
                "peer_id": target_agent,
                "metadata": {"record_type": "study_insight", "actor": target_agent, "peer_exchange": True},
            }],
        },
    )


def record_session_complete(session_id: str, agent_id: str, chunks_studied: int,
                             insights_recorded: int, run_ts: str) -> None:
    """Record a study_session_complete summary message."""
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions/{session_id}/messages",
        {
            "messages": [{
                "content": json.dumps({
                    "ts": run_ts,
                    "type": "study_session_complete",
                    "actor": agent_id,
                    "payload": {
                        "actor": agent_id,
                        "chunks_studied": chunks_studied,
                        "insights_recorded": insights_recorded,
                    },
                }, ensure_ascii=False),
                "peer_id": agent_id,
                "metadata": {"record_type": "study_session_complete", "actor": agent_id},
            }],
        },
    )


# ---------------------------------------------------------------------------
# Core study loop per agent
# ---------------------------------------------------------------------------

# @MX:ANCHOR: [AUTO] study_agent — per-agent knowledge study loop
# @MX:REASON: Called for each of 3 agents per run; also provides insights dict for peer_exchange()
def study_agent(agent: dict, chunks: list[dict], mode: str, run_ts: str) -> dict:
    """Run the study loop for one agent. Returns collected insights for peer exchange.

    Bootstrap mode supports resuming from a saved progress file so a restart after
    process death skips already-processed chunks instead of redoing the entire run.
    """
    agent_id = agent["id"]
    total_chunks = len(chunks)
    all_insights: list[dict] = []
    chunks_studied = 0

    # Resume support: skip already-processed chunks on bootstrap restart
    resume_from = 0
    session_id: str | None = None
    if mode == "bootstrap":
        prev = load_bootstrap_progress().get(agent_id, {})
        resume_from = prev.get("chunks_done", 0)
        session_id = prev.get("session_id")
        if resume_from > 0:
            log.info("[%s] Resuming bootstrap from chunk %d/%d (session %s)",
                     agent_id, resume_from, total_chunks, session_id)
            chunks = chunks[resume_from:]

    # Already fully processed on a previous run — skip entirely
    if resume_from >= total_chunks:
        log.info("[%s] Already fully studied (%d/%d chunks) — skipping",
                 agent_id, resume_from, total_chunks)
        return {"agent_id": agent_id, "insights": [], "session_id": session_id}

    if not session_id:
        log.info("[%s] Starting %s study — %d chunks", agent_id, mode, total_chunks)
        session_id = create_study_session(agent_id, mode, run_ts)
        if not session_id:
            log.warning("[%s] Could not create Honcho study session — skipping", agent_id)
            return {"agent_id": agent_id, "insights": [], "session_id": None}

    total_batches = (total_chunks + CHUNK_BATCH_SIZE - 1) // CHUNK_BATCH_SIZE
    start_batch = resume_from // CHUNK_BATCH_SIZE

    for i in range(0, len(chunks), CHUNK_BATCH_SIZE):
        batch = chunks[i : i + CHUNK_BATCH_SIZE]
        for chunk in batch:
            prompt = build_study_prompt(agent, chunk)
            raw = call_hermes(agent, prompt)
            insights = extract_insights(raw)
            for insight in insights:
                record_insight(session_id, agent_id, chunk, insight, run_ts)
                all_insights.append(insight)
            chunks_studied += 1
            time.sleep(CALL_DELAY)

        batch_num = start_batch + i // CHUNK_BATCH_SIZE + 1
        log.info("[%s] Batch %d/%d done — %d insights so far",
                 agent_id, batch_num, total_batches, len(all_insights))

        if mode == "bootstrap":
            save_bootstrap_progress(agent_id, resume_from + chunks_studied, session_id, len(all_insights))

    record_session_complete(session_id, agent_id, resume_from + chunks_studied, len(all_insights), run_ts)
    log.info("[%s] Study complete — %d chunks, %d insights", agent_id, resume_from + chunks_studied, len(all_insights))
    return {"agent_id": agent_id, "insights": all_insights, "session_id": session_id}


# ---------------------------------------------------------------------------
# Peer exchange
# ---------------------------------------------------------------------------

def peer_exchange(agent_results: list[dict], run_ts: str) -> None:
    """Cross-inject top insights between agents to build cross-regional awareness."""
    # Build a session for peer exchange per target agent
    for result in agent_results:
        target_id = result["agent_id"]
        session_id = result.get("session_id")
        if not session_id:
            continue

        for source_result in agent_results:
            source_id = source_result["agent_id"]
            if source_id == target_id:
                continue
            insights = source_result.get("insights", [])
            # Share top 5 insights (by confidence) from each peer
            top = sorted(insights, key=lambda x: x.get("confidence", 0), reverse=True)[:5]
            for insight in top:
                record_peer_insight(session_id, target_id, source_id, insight, run_ts)

        log.info("[%s] Peer exchange complete — received insights from peers", target_id)


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def run(mode: str, dry_run: bool = False) -> None:
    # Pre-flight: abort early on missing required env vars
    if not PG_DSN:
        log.error(
            "POSTGRES_URL is not set. Add it to scripts/.env (git-ignored). "
            "Example: POSTGRES_URL=postgresql://honcho:<pass>@localhost:5433/honcho"
        )
        sys.exit(1)
    if not HERMES_API_KEY:
        log.error(
            "API_SERVER_KEY is not set. Add it to scripts/.env (git-ignored). "
            "Check the running hermes-api-server.service environment for the value."
        )
        sys.exit(1)

    run_ts = datetime.now(timezone.utc).isoformat()
    checkpoint = load_checkpoint()

    since_ts: str | None = None
    if mode == "delta":
        since_ts = checkpoint.get("last_delta_ts") or checkpoint.get("last_bootstrap_ts")
        if not since_ts:
            log.info("No delta checkpoint found — running as bootstrap instead")
            mode = "bootstrap"

    log.info("=== Autonomous Study Scheduler [%s]%s ===", mode.upper(),
             " [DRY-RUN]" if dry_run else "")
    log.info("run_ts=%s  since_ts=%s", run_ts, since_ts)

    # Bootstrap: fetch all chunks (up to BOOTSTRAP_MAX); delta: respect MAX_CHUNKS_PER_SESSION
    chunk_limit = BOOTSTRAP_MAX if mode == "bootstrap" else MAX_CHUNKS_PER_SESSION

    agent_results: list[dict] = []
    for agent in AGENTS:
        chunks = fetch_chunks_for_agent(agent["id"], since_ts=since_ts, limit=chunk_limit)
        if not chunks:
            log.info("[%s] No chunks to study — skipping", agent["id"])
            agent_results.append({"agent_id": agent["id"], "insights": [], "session_id": None})
            continue
        if dry_run:
            log.info("[%s] DRY-RUN: would study %d chunks (no Honcho writes)", agent["id"], len(chunks))
            agent_results.append({"agent_id": agent["id"], "insights": [], "session_id": None,
                                   "_dry_chunk_count": len(chunks)})
            continue
        result = study_agent(agent, chunks, mode, run_ts)
        agent_results.append(result)

    if dry_run:
        total = sum(r.get("_dry_chunk_count", 0) for r in agent_results)
        log.info("DRY-RUN complete — would have studied %d total chunks across 3 agents", total)
        return

    # Peer exchange after all agents have finished studying
    peer_exchange(agent_results, run_ts)

    # Save checkpoint
    if mode == "bootstrap":
        checkpoint["last_bootstrap_ts"] = run_ts
        # Clear batch-level progress file — full run succeeded
        if PROGRESS_FILE.exists():
            PROGRESS_FILE.unlink()
            log.info("Bootstrap progress file cleared: %s", PROGRESS_FILE)
    else:
        checkpoint["last_delta_ts"] = run_ts
    checkpoint["last_run_ts"] = run_ts
    checkpoint["last_mode"] = mode
    save_checkpoint(checkpoint)

    total_insights = sum(len(r.get("insights", [])) for r in agent_results)
    log.info("=== Study run complete — total insights: %d ===", total_insights)


def main() -> None:
    parser = argparse.ArgumentParser(description="RA agent autonomous study scheduler")
    parser.add_argument(
        "mode",
        choices=["bootstrap", "delta"],
        nargs="?",
        default="delta",
        help="bootstrap = all chunks (first run); delta = incremental (daily)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Read pgvector and log what would be studied; skip all Honcho writes",
    )
    args = parser.parse_args()
    run(args.mode, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
