#!/usr/bin/env python3
"""KB knowledge-layer watcher (#158).

Role discipline (user directive 2026-10-19): this repo OBSERVES and REGISTERS
issues; it never writes knowledge into the KB repos. KB maintenance tasks own
the fixes. A human notification is an ESCALATION ONLY — when a registered
issue ages past ESCALATE_AFTER_DAYS unresolved, or a closed fix fails
re-verification.

Pipeline per run:
  1. DETECT  — commits in the last N hours on each KB checkout; changed .md
     files; per-file reflection check (does pgvector hold chunks for the
     file's current path?); reference-table domain overlap flag.
  2. LEDGER  — append findings to reports/kb-watch/ledger.jsonl (fsync).
  3. TRACK   — summarize open registered issues and their age.
  4. (opt) REGISTER — file an English issue on the owning KB repo. Dry-run by
     default; the first real registration must be user-confirmed (#158 DoD).

Agent-facing output is English (language policy 2026-10-19). The Korean
surface is the daily monitoring report and this repo's issues only.

Usage:
  python3 scripts/kb-watch.py                     # detect + ledger + summary
  python3 scripts/kb-watch.py --register <id>     # file the flagged finding (EN)
  python3 scripts/kb-watch.py --hours 24          # look-back window
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "reports" / "kb-watch" / "ledger.jsonl"
ESCALATE_AFTER_DAYS = 7

# KB checkouts (read-only from this repo — never written).
KB_REPOS: dict[str, Path] = {
    "holee9/ra-project": Path.home() / "work/workspace-github/holee9/ra-project",
    "holee9/MD-process": Path.home() / "work/workspace-github/holee9/MD-process",
}

# Reference-table domains (docs/ra/standard-editions.md + SOUL tables): a
# changed file touching one of these keyword families may require OUR table
# refresh — that part is ours to fix, not a KB-repo issue.
DOMAIN_KEYWORDS: dict[str, list[str]] = {
    "standard-editions": ["14971", "13485", "62304", "62366", "81001-5-1", "82304", "10993"],
    "guidance-dates": ["Final Guidance", "guidance", "가이던스", "guideline", "2024-28361"],
    "regulation-articles": ["Article 8", "Art.", "Annex VIII", "21 CFR", "Rule 1", "Rule 2", "제정", "전부개정"],
}


def run(cmd: list[str], cwd: Path | None = None) -> str:
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        return ""
    return r.stdout.strip()


def detect(hours: int) -> list[dict]:
    findings: list[dict] = []
    dsn = os.environ.get("POSTGRES_URL")
    for repo, path in KB_REPOS.items():
        if not path.exists():
            findings.append({"kind": "checkout-missing", "repo": repo, "path": str(path)})
            continue
        since = (datetime.now(timezone.utc) - timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M")
        # core.quotePath=false: Korean filenames otherwise arrive octal-escaped
        # ("01_\352\267..." style) and the .md suffix check silently misses them.
        out = run(["git", "-c", "core.quotePath=false", "log", "--since", since,
                   "--name-only", "--pretty=format:"], cwd=path)
        files = sorted({f.strip().strip('"') for f in out.splitlines()
                        if f.strip().endswith(".md")})
        for f in files:
            domains = [d for d, kws in DOMAIN_KEYWORDS.items() if any(k in f for k in kws)]
            reflected = None
            if dsn:
                try:
                    import psycopg2
                    with psycopg2.connect(dsn) as conn, conn.cursor() as cur:
                        cur.execute(
                            "SELECT count(*) FROM ra_knowledge WHERE source_path LIKE %s",
                            (f"%/{f}",),
                        )
                        reflected = cur.fetchone()[0] > 0
                except Exception as e:  # DB probe failure must not kill detection
                    reflected = f"probe-error:{type(e).__name__}"
            findings.append({
                "kind": "kb-file-changed", "repo": repo, "file": f,
                "pgvector_chunks_present": reflected,
                "reference_domains": domains,
            })
    return findings


def ledger_append(rec: dict) -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def build_issue_body(repo: str, f: str, domains: list[str]) -> str:
    """English issue body — consumed by the KB maintenance tasks (agents)."""
    lines = [
        "## KB source finding from ra-hermes watcher",
        "",
        f"- Repo: `{repo}`",
        f"- File: `{f}`",
        f"- Detected reference domains: {', '.join(domains) or 'n/a'}",
        "",
        "This file changed recently. The ra-hermes advisory pipeline serves",
        "content from it. Please verify the file's regulatory facts (standard",
        "editions, guidance dates, article numbering) against primary sources",
        "and correct if needed. This issue is informational; resolution is",
        "owned by this repo's KB maintenance task.",
    ]
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="KB knowledge-layer watcher (#158)")
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--register", metavar="FILE", help="file an English issue on the owning KB repo for this changed file")
    a = ap.parse_args(argv)

    if a.register:
        repo = next((r for r, p in KB_REPOS if (p / a.register).exists()), None)
        if not repo:
            print(json.dumps({"error": "file not found in any KB checkout", "file": a.register}))
            return 2
        body = build_issue_body(repo, a.register, [])
        print(json.dumps({"mode": "register-dry-run", "repo": repo, "file": a.register,
                          "issue_body": body}, ensure_ascii=False, indent=2))
        return 0

    findings = detect(a.hours)
    ts = datetime.now(timezone.utc).isoformat()
    for f in findings:
        ledger_append({"ts": ts, **f})
    changed = [f for f in findings if f["kind"] == "kb-file-changed"]
    not_reflected = [f for f in changed if f["pgvector_chunks_present"] is False]
    domain_hits = [f for f in changed if f["reference_domains"]]
    print(json.dumps({
        "run_ts": ts, "window_hours": a.hours,
        "kb_files_changed": len(changed),
        "not_reflected_in_pgvector": [f["file"] for f in not_reflected],
        "reference_domain_hits": {f["file"]: f["reference_domains"] for f in domain_hits},
        "other": [f for f in findings if f["kind"] != "kb-file-changed"],
        "escalate_after_days": ESCALATE_AFTER_DAYS,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
