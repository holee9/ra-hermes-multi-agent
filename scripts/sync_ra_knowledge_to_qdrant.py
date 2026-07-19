#!/usr/bin/env python3
"""Sync ra_knowledge (pgvector) -> Qdrant ra_kb_markdown collection (reverse migration).

#107 Phase 2 (c1): ra-project/MD-process markdown embeddings (already computed in pgvector)
are copied into a dedicated Qdrant collection so the agent's Layer 1 RAG can reach them via
hybrid lookup (hermes-api-server queries nas_ra_docs + ra_kb_markdown). No re-embedding —
vectors are copied as-is from pgvector, so GX10 is never touched (the key cost saving over
SPEC option (a) bulk migration). Idempotent: Qdrant point id = ra_knowledge.id (upsert overwrites).

Env: POSTGRES_URL, QDRANT_URL (default http://localhost:6333), EMBED_DIM (4096),
     RA_KB_COLLECTION (default ra_kb_markdown), SYNC_BATCH (default 500).
Usage: python3 sync_ra_knowledge_to_qdrant.py [--dry-run]
"""
import json
import os
import sys
import urllib.request
import urllib.error

import psycopg2

QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333").rstrip("/")
COLLECTION = os.environ.get("RA_KB_COLLECTION", "ra_kb_markdown")
EMBED_DIM = int(os.environ.get("EMBED_DIM", "4096"))
BATCH = int(os.environ.get("SYNC_BATCH", "500"))
POSTGRES_URL = os.environ.get("POSTGRES_URL")


def _env_list(name, default):
    raw = os.environ.get(name, "")
    if not raw.strip():
        return default
    return tuple(item.strip() for item in raw.split(",") if item.strip())


# @MX:NOTE: [AUTO] #112 — low-signal / PII-bearing source folders excluded from
# the Qdrant mirror. Mirrors daily-growth-runner.py's EXCLUDED_SOURCE_PATTERNS
# (retrieval-side) and index_github_repos.py's INDEX_EXCLUDED_PATH_PATTERNS
# (indexing-side); this is the sync-side equivalent so the live advisory RAG
# collection (ra_kb_markdown, queried by hermes-api-server._run_rag_search)
# never receives these patterns via the nightly resync.
EXCLUDED_SOURCE_PATTERNS = _env_list(
    "SYNC_EXCLUDED_SOURCE_PATTERNS",
    (
        "%/wiki/entities/%",
        "%/06_심사_QA이력/%",
        "%/11_일일_리서치로그/%",
        "%/issue-drafts/%",   # audit/issue-draft process meta, not regulatory knowledge — #128
    ),
)


def qdrant(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        f"{QDRANT_URL}{path}", data=data, method=method,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        return {"_http_error": e.code, "_body": e.read().decode()[:300]}


def ensure_collection():
    info = qdrant("GET", f"/collections/{COLLECTION}")
    if info.get("_http_error") == 404:
        r = qdrant("PUT", f"/collections/{COLLECTION}",
                   {"vectors": {"size": EMBED_DIM, "distance": "Cosine"}})
        status = r.get("result")
        if isinstance(status, bool):
            status = "ok" if status else "failed"
        print(f"[ensure] created {COLLECTION} (dim {EMBED_DIM}, Cosine): {status}")
    else:
        cfg = info.get("result", {}).get("config", {}).get("params", {}).get("vectors", {})
        print(f"[ensure] {COLLECTION} exists (dim {cfg.get('size')}, {cfg.get('distance')})")


def fetch_rows():
    conn = psycopg2.connect(POSTGRES_URL)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM ra_knowledge")
    total = cur.fetchone()[0]
    exclusion_sql = "\n".join(
        "AND source_path NOT ILIKE %s" for _ in EXCLUDED_SOURCE_PATTERNS
    )
    cur.execute(
        # llm-wiki is EXCLUDED — it is a Karpathy on-demand knowledge layer consumed via
        # Layer 4 fetch, NOT a pgvector/RAG embedding target (user decision 2026-07-10).
        # Only ra-project / MD-process markdown belong in the RAG collection. Legacy
        # llm-wiki rows still in ra_knowledge (#27 cleanup pending) are filtered out here.
        # #112: low-signal / PII-bearing source folders excluded (see EXCLUDED_SOURCE_PATTERNS).
        f"""
        SELECT id, content, embedding::text, metadata FROM ra_knowledge
        WHERE metadata->>'repo' NOT LIKE '%%llm-wiki%%'
        {exclusion_sql}
        ORDER BY id
        """,
        list(EXCLUDED_SOURCE_PATTERNS),
    )
    rows = cur.fetchall()
    conn.close()
    return total, rows


def to_point(row):
    rid, content, emb_str, meta = row
    meta = meta or {}
    vec = json.loads(emb_str)  # pgvector ::text is a JSON array "[..]"
    repo = meta.get("repo")
    payload = {
        "text": content,
        "file_path": meta.get("file_path"),
        "repo": repo,
        "doc_type": meta.get("doc_type"),
        "chunk_index": meta.get("chunk_index"),
        # Distinguishes markdown-KB points from NAS docs when surfaced as evidence.
        "kb_source": "markdown_kb",
        "source": f"github:{repo}" if repo else "markdown_kb",
    }
    return {"id": rid, "vector": vec, "payload": payload}


def upsert_batch(points):
    r = qdrant("PUT", f"/collections/{COLLECTION}/points", {"points": points})
    if r.get("_http_error"):
        return False, r.get("_body")
    return True, r.get("result", {})


def main():
    dry = "--dry-run" in sys.argv
    if not POSTGRES_URL:
        print("ERROR: POSTGRES_URL not set")
        sys.exit(1)
    ensure_collection()
    total, rows = fetch_rows()
    mode = "dry-run" if dry else "execute"
    print(f"[plan] ra_knowledge rows: {total} | collection: {COLLECTION} | batch: {BATCH} | mode: {mode}")
    if dry:
        print("[dry-run] collection ready, skipping upsert")
        return
    done = 0
    failed = 0
    nbatches = (len(rows) + BATCH - 1) // BATCH
    for i in range(0, len(rows), BATCH):
        chunk = rows[i:i + BATCH]
        points = [to_point(r) for r in chunk]
        ok, res = upsert_batch(points)
        if ok:
            done += len(points)
        else:
            failed += len(points)
            print(f"[FAIL] batch @ {i}: {res}")
        bnum = i // BATCH
        if bnum % 4 == 0 or bnum == nbatches - 1:
            print(f"  ... {done}/{total} upserted")
    print(f"[done] upserted={done} failed={failed} -> {COLLECTION}")


if __name__ == "__main__":
    main()
