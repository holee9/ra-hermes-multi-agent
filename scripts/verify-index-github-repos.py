#!/usr/bin/env python3
"""Local regression checks for scripts/index_github_repos.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "index_github_repos.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("index_github_repos", SCRIPT)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()

    # #112 — QA email logs and daily research logs must be excluded at index time.
    excluded_examples = [
        "01_규제지식베이스/미국_FDA/06_심사_QA이력/2026-06-20_문의.md",
        "11_일일_리서치로그/2026-06-01.md",
        "wiki/entities/some-stub.md",
    ]
    for path in excluded_examples:
        if not module.is_excluded_path(path):
            fail(f"expected path to be excluded: {path}")

    # Normal regulatory content must not be excluded (no over-filtering).
    kept_examples = [
        "01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md",
        "01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_원문.md",
        "05_전문가교육/Week04_MDR_EU_체계_상세.md",
    ]
    for path in kept_examples:
        if module.is_excluded_path(path):
            fail(f"unexpected exclusion (over-filtering) for: {path}")

    # list_md_files/list_md_files_gitea filter predicates must match is_excluded_path
    # exactly (reproduces the same list-comprehension logic without a network call).
    tree = [
        {"type": "blob", "path": "01_규제지식베이스/미국_FDA/06_심사_QA이력/foo.md"},
        {"type": "blob", "path": "01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md"},
        {"type": "tree", "path": "01_규제지식베이스"},
    ]
    filtered = [
        item for item in tree
        if item.get("type") == "blob"
        and item.get("path", "").lower().endswith(".md")
        and not module.is_excluded_path(item.get("path", ""))
    ]
    if len(filtered) != 1 or filtered[0]["path"] != "01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md":
        fail(f"list_md_files-style filter did not match expected result: {filtered}")

    print("OK: index_github_repos exclusion filter contract holds")


if __name__ == "__main__":
    main()
