#!/usr/bin/env python3
"""Security classification scan (covenant v1.0, 2026-10-20) — user-directed.

Scans git-tracked text files for [내부]-grade source markers (NAS paths,
company/partner email domains, invoice patterns). Any hit is a violation
candidate: review and remediate BEFORE pushing. Exit 1 on any finding.

This is a tripwire, not a guarantee — classified-by-source discipline in
CLAUDE.md remains the primary control.
"""

from __future__ import annotations

import re
import subprocess
import sys

# [내부] source markers — extend as new internal sources are identified
PATTERNS = [
    (re.compile(r"[A-Za-z0-9._%+-]+@abyzr\.com"), "company email address (full)"),
    (re.compile(r"/mnt/nas"), "NAS mount path"),
    (re.compile(r"[A-Za-z0-9._%+-]+@(actslab\.co\.kr|3ec\.sk)"), "partner email address (full)"),
    (re.compile(r"DR_RnD/"), "internal Gitea repo reference (DR_RnD)"),
    (re.compile(r"(Invoice|인보이스)\s*(No\.?|번호)?\s*[:.]?\s*[0-9]{4,}"), "invoice number"),
    (re.compile(r"[0-9]{1,3}(?:[,.][0-9]{3})+\.?[0-9]{0,2}\s*(EUR|USD|원)"), "invoice-like amount"),
]

EXCLUDES = ("scripts/security-scan.py", "CLAUDE.md")  # rule definitions themselves


def main() -> int:
    files = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True, check=True
    ).stdout.splitlines()
    findings = 0
    for path in files:
        if path in EXCLUDES or not path.endswith((".md", ".json", ".txt", ".py", ".yml", ".yaml", ".ts", ".js")):
            continue
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for pat, label in PATTERNS:
            for m in pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                # code/spec references to infra paths are pointers, not internal data
                infra_label = label in ("NAS mount path", "internal Gitea repo reference (DR_RnD)")
                severity = "infra-ref" if (infra_label or path.endswith(".py")
                                           or "/specs/" in path or path in ("README.md",)) else "CONTENT"
                if severity == "CONTENT":
                    findings += 1
                print(f"[내부?/{severity}] {path}:{line} — {label}: {m.group(0)[:60]}")
    print(f"scan complete: {findings} CONTENT finding(s) across {len(files)} tracked files")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
