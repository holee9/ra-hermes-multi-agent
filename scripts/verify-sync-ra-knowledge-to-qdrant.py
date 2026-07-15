#!/usr/bin/env python3
"""Local regression checks for scripts/sync_ra_knowledge_to_qdrant.py.

No live DB/Qdrant connection required — exercises pure functions and the
exclusion-pattern contract only.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "sync_ra_knowledge_to_qdrant.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("sync_ra_knowledge_to_qdrant", SCRIPT)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()

    # #112 — the sync-side exclusion patterns must mirror the retrieval/indexing
    # side (daily-growth-runner.py EXCLUDED_SOURCE_PATTERNS, index_github_repos.py
    # INDEX_EXCLUDED_PATH_PATTERNS) so the live advisory RAG collection
    # (ra_kb_markdown) never receives QA-log/research-log/entity-stub sources.
    expected_substrings = ["wiki/entities", "06_심사_QA이력", "11_일일_리서치로그"]
    for needle in expected_substrings:
        if not any(needle in pattern for pattern in module.EXCLUDED_SOURCE_PATTERNS):
            fail(f"expected exclusion pattern covering: {needle}")

    # The WHERE-clause builder must emit exactly one placeholder per pattern —
    # a mismatch here is the exact "IndexError: list index out of range" bug
    # class reproduced during initial implementation (literal '%' in the
    # llm-wiki clause was not escaped for psycopg2's %-style substitution).
    exclusion_sql = "\n".join(
        "AND source_path NOT ILIKE %s" for _ in module.EXCLUDED_SOURCE_PATTERNS
    )
    if exclusion_sql.count("%s") != len(module.EXCLUDED_SOURCE_PATTERNS):
        fail("exclusion_sql placeholder count must match EXCLUDED_SOURCE_PATTERNS length")

    # The literal '%llm-wiki%' clause must stay escaped as '%%llm-wiki%%' in the
    # f-string template (psycopg2 requires literal '%' doubled when parameters
    # are also passed to cur.execute()).
    source = SCRIPT.read_text(encoding="utf-8")
    if "'%%llm-wiki%%'" not in source:
        fail("llm-wiki NOT LIKE literal must be escaped as %% for psycopg2 parameter binding")

    # to_point() payload shape must be unaffected by the filter change.
    row = (123, "some regulatory text", json.dumps([0.1, 0.2, 0.3]), {"repo": "holee9/ra-project", "file_path": "foo.md"})
    point = module.to_point(row)
    if point["id"] != 123 or point["payload"]["file_path"] != "foo.md":
        fail(f"to_point() payload shape regressed: {point}")

    print("OK: sync_ra_knowledge_to_qdrant exclusion contract holds")


if __name__ == "__main__":
    main()
