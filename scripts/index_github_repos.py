#!/usr/bin/env python3
"""
GitHub + Gitea MD Indexing Script
Indexes all .md files from configured GitHub repos and Gitea repos into the ra_knowledge pgvector table.

MIGRATION: Qdrant → pgvector (2026-06, issue #17)
  POSTGRES_URL → postgresql://honcho:honcho@localhost:5433/honcho
  Table: ra_knowledge  (dim=768, nomic-embed-text, ivfflat cosine)
  Qdrant COLLECTION "hermes-ra-knowledge" maps to table "ra_knowledge"

Source path prefixes:
  github:{owner/repo}/{path}  → public GitHub repos (MD-process, ra-project)
  gitea:{owner/repo}/{path}   → internal Gitea repos (llm-wiki)
"""

import argparse
import base64
import hashlib
import json
import os
import sys
import time
import warnings
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from typing import Optional

import requests
import psycopg2
import psycopg2.extras

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPOS = ["holee9/MD-process", "holee9/ra-project"]
GITHUB_TOKEN: Optional[str] = os.environ.get("GITHUB_PAT") or os.environ.get("GITHUB_TOKEN")
POSTGRES_URL = os.environ.get("POSTGRES_URL", "postgresql://honcho:honcho@localhost:5433/honcho")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://192.168.100.1:11434")
TABLE = "ra_knowledge"
EMBED_MODEL = "nomic-embed-text"
EMBED_DIM = 768  # nomic-embed-text output dimension
STATE_FILE = "/tmp/github_index_state.json"
SERVER_PORT = 7791

GITHUB_API = "https://api.github.com"

# Gitea (internal NAS Gitea, reachable via Tailscale: diskstation:7001)
GITEA_URL = os.environ.get("GITEA_URL", "http://diskstation:7001")
GITEA_TOKEN: Optional[str] = os.environ.get("GITEA_TOKEN")
GITEA_REPOS = ["DR_RnD/ra-llm-wiki"]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def github_headers() -> dict:
    h = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return h


def github_get(url: str, params: dict = None) -> requests.Response:
    """GET with one retry and rate-limit handling."""
    for attempt in range(2):
        try:
            resp = requests.get(url, headers=github_headers(), params=params, timeout=30)
            if resp.status_code in (403, 429):
                print(f"  [warn] Rate limited on {url}, sleeping 2s …", flush=True)
                time.sleep(2)
                continue
            return resp
        except requests.RequestException as exc:
            if attempt == 0:
                print(f"  [warn] Network error ({exc}), retrying …", flush=True)
                time.sleep(1)
            else:
                print(f"  [warn] Network error ({exc}), skipping.", flush=True)
                return None
    return None


def gitea_headers() -> dict:
    h = {"Accept": "application/json"}
    if GITEA_TOKEN:
        h["Authorization"] = f"token {GITEA_TOKEN}"
    return h


def gitea_get(path: str, params: dict = None) -> requests.Response:
    """GET {GITEA_URL}/api/v1/{path} with one retry."""
    url = f"{GITEA_URL}/api/v1/{path}"
    for attempt in range(2):
        try:
            resp = requests.get(url, headers=gitea_headers(), params=params, timeout=30)
            if resp.status_code in (429,):
                print(f"  [warn] Gitea rate limited, sleeping 2s …", flush=True)
                time.sleep(2)
                continue
            return resp
        except requests.RequestException as exc:
            if attempt == 0:
                print(f"  [warn] Gitea network error ({exc}), retrying …", flush=True)
                time.sleep(1)
            else:
                print(f"  [warn] Gitea network error ({exc}), skipping.", flush=True)
                return None
    return None


def get_gitea_head_sha(repo: str) -> Optional[str]:
    """Return HEAD commit SHA for the default branch of a Gitea repo."""
    resp = gitea_get(f"repos/{repo}")
    if resp is None or resp.status_code != 200:
        return None
    default_branch = resp.json().get("default_branch", "main")

    resp2 = gitea_get(f"repos/{repo}/branches/{default_branch}")
    if resp2 is None or resp2.status_code != 200:
        return None
    return resp2.json().get("commit", {}).get("id")


def list_md_files_gitea(repo: str) -> list[dict]:
    """Return list of {path, sha} for all .md files in a Gitea repo (recursive tree)."""
    # Get HEAD SHA first
    head_sha = get_gitea_head_sha(repo)
    if not head_sha:
        print(f"  [warn] Could not get HEAD sha for gitea:{repo}", flush=True)
        return []

    resp = gitea_get(f"repos/{repo}/git/trees/{head_sha}", params={"recursive": "true"})
    if resp is None or resp.status_code != 200:
        print(f"  [warn] Could not list tree for gitea:{repo}: {resp}", flush=True)
        return []

    tree = resp.json().get("tree", [])
    return [
        {"path": item["path"], "sha": item.get("sha", "")}
        for item in tree
        if item.get("type") == "blob" and item["path"].lower().endswith(".md")
    ]


def fetch_gitea_file_content(repo: str, path: str) -> Optional[str]:
    """Fetch raw .md file content from Gitea via contents API."""
    resp = gitea_get(f"repos/{repo}/contents/{path}")
    if resp is None or resp.status_code != 200:
        return None
    data = resp.json()
    encoded = data.get("content", "")
    try:
        return base64.b64decode(encoded).decode("utf-8", errors="replace")
    except Exception:
        return None


def embed_text(text: str) -> Optional[list]:
    """Embed text via Ollama. Returns embedding vector or None on error."""
    payload = {"model": EMBED_MODEL, "prompt": text[:2000]}
    for attempt in range(2):
        try:
            resp = requests.post(
                f"{OLLAMA_URL}/api/embeddings", json=payload, timeout=60
            )
            if resp.status_code == 200:
                return resp.json().get("embedding")
            print(
                f"  [warn] Embed HTTP {resp.status_code}: {resp.text[:200]}", flush=True
            )
        except requests.RequestException as exc:
            if attempt == 0:
                print(f"  [warn] Embed error ({exc}), retrying …", flush=True)
                time.sleep(1)
            else:
                print(f"  [warn] Embed error ({exc}), skipping chunk.", flush=True)
    return None


def make_id(text: str) -> int:
    return int(hashlib.md5(text.encode()).hexdigest()[:15], 16)


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_state() -> dict:
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(state: dict):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ---------------------------------------------------------------------------
# GitHub helpers
# ---------------------------------------------------------------------------

def get_head_sha(repo: str) -> Optional[str]:
    url = f"{GITHUB_API}/repos/{repo}/commits/HEAD"
    resp = github_get(url)
    if resp and resp.status_code == 200:
        return resp.json().get("sha")
    return None


def list_md_files(repo: str) -> list[dict]:
    """Return list of {path, sha, url} for all .md blobs in repo tree."""
    url = f"{GITHUB_API}/repos/{repo}/git/trees/HEAD"
    resp = github_get(url, params={"recursive": "1"})
    if not resp or resp.status_code != 200:
        print(f"  [warn] Could not fetch tree for {repo}: status={getattr(resp, 'status_code', 'N/A')}", flush=True)
        return []
    tree = resp.json().get("tree", [])
    return [
        item for item in tree
        if item.get("type") == "blob" and item.get("path", "").lower().endswith(".md")
    ]


def fetch_file_content(repo: str, path: str) -> Optional[str]:
    """Fetch and decode a file from GitHub Contents API."""
    url = f"{GITHUB_API}/repos/{repo}/contents/{path}"
    resp = github_get(url)
    if not resp or resp.status_code != 200:
        print(f"  [warn] Could not fetch {repo}/{path}: status={getattr(resp, 'status_code', 'N/A')}", flush=True)
        return None
    data = resp.json()
    encoded = data.get("content", "")
    try:
        return base64.b64decode(encoded).decode("utf-8", errors="replace")
    except Exception as exc:
        print(f"  [warn] Base64 decode error for {path}: {exc}", flush=True)
        return None


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------

def split_by_paragraphs(text: str, max_size: int = 800) -> list[str]:
    """Split text at paragraph boundaries to fit within max_size."""
    paragraphs = text.split("\n\n")
    chunks = []
    current = ""
    for para in paragraphs:
        candidate = (current + "\n\n" + para).strip() if current else para.strip()
        if len(candidate) <= max_size:
            current = candidate
        else:
            if current:
                chunks.append(current)
            if len(para) > max_size:
                for i in range(0, len(para), max_size):
                    chunk = para[i : i + max_size].strip()
                    if chunk:
                        chunks.append(chunk)
                current = ""
            else:
                current = para.strip()
    if current:
        chunks.append(current)
    return chunks


def chunk_markdown(text: str, max_chunk: int = 800, min_chunk: int = 50) -> list[str]:
    """
    Split markdown at ## / ### boundaries.
    Each chunk = heading + content until next heading.
    Chunks > max_chunk are further split at paragraph boundaries.
    Chunks < min_chunk are skipped.
    """
    import re

    parts = re.split(r"(?=^#{2,3} )", text, flags=re.MULTILINE)

    raw_chunks = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if len(part) <= max_chunk:
            raw_chunks.append(part)
        else:
            raw_chunks.extend(split_by_paragraphs(part, max_chunk))

    return [c for c in raw_chunks if len(c) >= min_chunk]


# ---------------------------------------------------------------------------
# pgvector helpers
# ---------------------------------------------------------------------------

# @MX:ANCHOR: [AUTO] ensure_table creates ra_knowledge table — shared with index_ra_knowledge
# @MX:REASON: [AUTO] Both indexers write to the same table; schema must be created before first write
def ensure_table() -> None:
    """Create pgvector table and indexes if they do not exist."""
    with psycopg2.connect(POSTGRES_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {TABLE} (
                    id BIGINT PRIMARY KEY,
                    source_path TEXT,
                    chunk_index INT,
                    content TEXT,
                    embedding vector({EMBED_DIM}),
                    metadata JSONB,
                    indexed_at TIMESTAMP DEFAULT now()
                )""")
            cur.execute(
                f"CREATE INDEX IF NOT EXISTS {TABLE}_src_idx ON {TABLE} (source_path)"
            )
            cur.execute(
                f"""CREATE INDEX IF NOT EXISTS {TABLE}_emb_idx ON {TABLE}
                    USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)"""
            )
        conn.commit()


def pgvector_delete_by_source(source_path: str) -> None:
    """Delete all rows matching source_path field."""
    with psycopg2.connect(POSTGRES_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM {TABLE} WHERE source_path = %s", (source_path,))
        conn.commit()


def pgvector_upsert(points: list[dict]) -> None:
    """Upsert a batch of points into the ra_knowledge table."""
    if not points:
        return
    values = [
        (
            p["id"],
            p.get("source_path", ""),
            p.get("chunk_index", 0),
            p["content"],
            json.dumps(p["vector"]),
            json.dumps(p.get("metadata", {})),
        )
        for p in points
    ]
    with psycopg2.connect(POSTGRES_URL) as conn:
        with conn.cursor() as cur:
            psycopg2.extras.execute_values(
                cur,
                f"""INSERT INTO {TABLE} (id, source_path, chunk_index, content, embedding, metadata)
                    VALUES %s
                    ON CONFLICT (id) DO UPDATE SET
                        source_path = EXCLUDED.source_path,
                        chunk_index = EXCLUDED.chunk_index,
                        content = EXCLUDED.content,
                        embedding = EXCLUDED.embedding,
                        metadata = EXCLUDED.metadata,
                        indexed_at = now()""",
                values,
                template="(%s, %s, %s, %s, %s::vector, %s::jsonb)",
            )
        conn.commit()


def pgvector_count() -> int:
    """Return total row count in the table."""
    try:
        with psycopg2.connect(POSTGRES_URL) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT COUNT(*) FROM {TABLE}")
                return cur.fetchone()[0]
    except Exception:
        return -1


# ---------------------------------------------------------------------------
# Per-file indexing
# ---------------------------------------------------------------------------

def index_file(repo: str, path: str) -> int:
    """Fetch, chunk, embed, and upsert one .md file. Returns chunks added."""
    source_path = f"github:{repo}/{path}"
    repo_short = repo.split("/")[-1]

    content = fetch_file_content(repo, path)
    if content is None:
        return 0

    chunks = chunk_markdown(content)
    if not chunks:
        return 0

    pgvector_delete_by_source(source_path)

    indexed_at = datetime.now(timezone.utc).isoformat()
    points = []
    for i, chunk in enumerate(chunks):
        vector = embed_text(chunk)
        if vector is None:
            print(f"    [warn] Skipping chunk (embed failed): {chunk[:60]!r}", flush=True)
            continue
        point_id = make_id(source_path + chunk)
        points.append(
            {
                "id": point_id,
                "source_path": source_path,
                "chunk_index": i,
                "content": chunk,
                "vector": vector,
                "metadata": {
                    "sheet": repo_short,
                    "doc_type": "regulatory_knowledge",
                    "repo": repo,
                    "file_path": path,
                    "indexed_at": indexed_at,
                },
            }
        )

    if points:
        pgvector_upsert(points)

    return len(points)


# ---------------------------------------------------------------------------
# Full sync
# ---------------------------------------------------------------------------

def sync_repos(repos: list[str] = REPOS) -> dict:
    state = load_state()
    total_files = 0
    total_chunks = 0
    repos_processed = []

    for repo in repos:
        print(f"\n[{repo}] Checking HEAD commit …", flush=True)
        t0 = time.time()

        head_sha = get_head_sha(repo)
        if head_sha and state.get(repo) == head_sha:
            print(f"[{repo}] No changes since last run (sha={head_sha[:8]}), skipping.", flush=True)
            continue

        print(f"[{repo}] Listing .md files …", flush=True)
        md_files = list_md_files(repo)
        print(f"[{repo}] Found {len(md_files)} .md file(s).", flush=True)

        repo_files = 0
        repo_chunks = 0
        for item in md_files:
            path = item["path"]
            print(f"  Indexing: {path}", flush=True)
            added = index_file(repo, path)
            print(f"    → {added} chunk(s) added.", flush=True)
            repo_files += 1
            repo_chunks += added

        elapsed = time.time() - t0
        print(
            f"[{repo}] Done. files={repo_files}, chunks={repo_chunks}, time={elapsed:.1f}s",
            flush=True,
        )

        total_files += repo_files
        total_chunks += repo_chunks
        repos_processed.append(repo)

        if head_sha:
            state[repo] = head_sha
            save_state(state)

    return {
        "repos_processed": repos_processed,
        "total_files": total_files,
        "chunks_added": total_chunks,
    }


# ---------------------------------------------------------------------------
# Gitea indexing
# ---------------------------------------------------------------------------

def index_gitea_file(repo: str, path: str) -> int:
    """Fetch, chunk, embed, and upsert one Gitea .md file. Returns chunk count."""
    content = fetch_gitea_file_content(repo, path)
    if not content:
        print(f"    [warn] Could not fetch gitea:{repo}/{path}", flush=True)
        return 0

    chunks = chunk_markdown(content)
    source = f"gitea:{repo}/{path}"
    points = []

    for i, chunk in enumerate(chunks):
        embedding = embed_text(chunk)
        if embedding is None:
            continue
        chunk_id = hashlib.md5(f"{source}#{i}".encode()).hexdigest()
        points.append(
            {
                "id": chunk_id,
                "embedding": embedding,
                "source": source,
                "chunk_index": i,
                "content": chunk,
                "indexed_at": datetime.now(timezone.utc).isoformat(),
            }
        )

    if points:
        pgvector_upsert(points)

    return len(points)


def sync_gitea_repos(repos: list[str] = GITEA_REPOS) -> dict:
    """Sync all configured Gitea repos into ra_knowledge table."""
    state = load_state()
    total_files = 0
    total_chunks = 0
    repos_processed = []

    for repo in repos:
        state_key = f"gitea:{repo}"
        print(f"\n[gitea:{repo}] Checking HEAD commit …", flush=True)
        t0 = time.time()

        head_sha = get_gitea_head_sha(repo)
        if head_sha and state.get(state_key) == head_sha:
            print(f"[gitea:{repo}] No changes since last run (sha={head_sha[:8]}), skipping.", flush=True)
            continue

        print(f"[gitea:{repo}] Listing .md files …", flush=True)
        md_files = list_md_files_gitea(repo)
        print(f"[gitea:{repo}] Found {len(md_files)} .md file(s).", flush=True)

        repo_files = 0
        repo_chunks = 0
        for item in md_files:
            path = item["path"]
            print(f"  Indexing: {path}", flush=True)
            added = index_gitea_file(repo, path)
            print(f"    → {added} chunk(s) added.", flush=True)
            repo_files += 1
            repo_chunks += added

        elapsed = time.time() - t0
        print(
            f"[gitea:{repo}] Done. files={repo_files}, chunks={repo_chunks}, time={elapsed:.1f}s",
            flush=True,
        )

        total_files += repo_files
        total_chunks += repo_chunks
        repos_processed.append(f"gitea:{repo}")

        if head_sha:
            state[state_key] = head_sha
            save_state(state)

    return {
        "repos_processed": repos_processed,
        "total_files": total_files,
        "chunks_added": total_chunks,
    }


# ---------------------------------------------------------------------------
# HTTP server mode
# ---------------------------------------------------------------------------

class SyncHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # suppress default access log

    def send_json(self, code: int, data: dict):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            kb_rows = pgvector_count()
            self.send_json(200, {"status": "ok", "kb_rows": kb_rows})
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path == "/sync":
            print("[server] /sync triggered", flush=True)

            def run():
                r1 = sync_repos()
                r2 = sync_gitea_repos()
                kb = pgvector_count()
                print(f"[server] GitHub sync: {r1}", flush=True)
                print(f"[server] Gitea sync: {r2}", flush=True)
                print(f"[server] Sync complete, kb_rows={kb}", flush=True)

            t = Thread(target=run, daemon=True)
            t.start()
            self.send_json(202, {"status": "sync started"})
        else:
            self.send_json(404, {"error": "not found"})


def run_server():
    server = HTTPServer(("0.0.0.0", SERVER_PORT), SyncHandler)
    print(f"[server] Listening on port {SERVER_PORT} …", flush=True)
    print(f"  GET  /health  → {{status, kb_rows}}", flush=True)
    print(f"  POST /sync    → trigger full sync", flush=True)
    server.serve_forever()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Index .md files from GitHub repos into pgvector ra_knowledge table."
    )
    parser.add_argument(
        "--server",
        action="store_true",
        help=f"Run HTTP server on port {SERVER_PORT} instead of one-shot sync.",
    )
    parser.add_argument(
        "--repos",
        nargs="*",
        default=REPOS,
        metavar="OWNER/REPO",
        help="Override repo list (default: %(default)s).",
    )
    args = parser.parse_args()

    if args.server:
        ensure_table()
        run_server()
        return

    print("=" * 60, flush=True)
    print("GitHub + Gitea MD Indexer (pgvector)", flush=True)
    print(f"GitHub repos : {args.repos}", flush=True)
    print(f"Gitea repos  : {GITEA_REPOS}", flush=True)
    print(f"Gitea URL    : {GITEA_URL}", flush=True)
    print(f"Postgres     : {POSTGRES_URL}  Table: {TABLE}", flush=True)
    print(f"Embed        : {OLLAMA_URL}  Model: {EMBED_MODEL}", flush=True)
    print("=" * 60, flush=True)

    ensure_table()

    t_start = time.time()
    gh_result = sync_repos(args.repos)
    gt_result = sync_gitea_repos()
    elapsed = time.time() - t_start

    total_processed = len(gh_result["repos_processed"]) + len(gt_result["repos_processed"])
    total_files = gh_result["total_files"] + gt_result["total_files"]
    total_chunks = gh_result["chunks_added"] + gt_result["chunks_added"]

    kb_rows = pgvector_count()
    print("\n" + "=" * 60, flush=True)
    print(
        f"Finished. repos_processed={total_processed}, "
        f"files={total_files}, chunks={total_chunks}, "
        f"time={elapsed:.1f}s",
        flush=True,
    )
    print(f"  GitHub: {gh_result['repos_processed']}", flush=True)
    print(f"  Gitea:  {gt_result['repos_processed']}", flush=True)
    print(f"Total KB rows in table: {kb_rows}", flush=True)
    print("=" * 60, flush=True)


if __name__ == "__main__":
    main()
