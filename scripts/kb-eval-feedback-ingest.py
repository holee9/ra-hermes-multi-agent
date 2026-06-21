#!/usr/bin/env python3
"""Convert checked KB eval Markdown into Honcho score_given feedback.

Default mode is dry-run. Use --execute only after reviewing the parsed records.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import psycopg2
import psycopg2.extras
import requests


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs" / "kb-eval-checksheets"
HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WS", os.environ.get("HONCHO_WORKSPACE", "work"))

CASE_RE = re.compile(r"^<!-- kb_eval_case (?P<meta>.+) -->$")
CHECK_RE = re.compile(r"^- \[(?P<mark>[ xX])\] (?P<label>.+)$")

SCORE_LABELS = {
    "Score 3 - pass / usable without correction": 3,
    "Score 2 - usable with minor correction": 2,
    "Score 1 - correction required": 1,
}
DIMENSION_LABELS = {
    "Match correct": "match_correct",
    "Evidence supported": "evidence_supported",
    "Source cited": "source_cited",
    "No hallucination": "no_hallucination",
    "Escalation appropriate": "escalation_appropriate",
}


def checked(mark: str) -> bool:
    return mark.lower() == "x"


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def run(cmd: list[str]) -> str:
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"command failed ({result.returncode}): {' '.join(cmd)}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result.stdout.strip()


# @MX:WARN: [AUTO] parse_text — multi-section sheet parser; stateful section tracking
# @MX:REASON: Cyclomatic complexity 16; in_note state-machine parsing. Fixed in f3aca88 (section-header reset + multi-line note accumulation) after a regression where correction notes overwrote source excerpts. High regression risk on sheet-format changes; writes only Honcho messages, never knowledge repos.
def parse_text(source: str, text: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    checks: dict[str, bool] = {}
    correction_note: str | None = None
    in_note = False

    def flush() -> None:
        nonlocal current, checks, correction_note, in_note
        if current is None:
            return
        score_checks = [value for label, value in SCORE_LABELS.items() if checks.get(label)]
        if len(score_checks) == 0:
            current = None
            checks = {}
            correction_note = None
            in_note = False
            return
        if len(score_checks) > 1:
            raise ValueError(f"{source}: {current['decision_ref']} has multiple score boxes checked")
        score = score_checks[0]
        dimensions = {key: bool(checks.get(label)) for label, key in DIMENSION_LABELS.items()}
        human_correction = bool(checks.get("Human correction needed")) or score == 1
        payload = {
            "decision_ref": current["decision_ref"],
            "target_actor": current["agent"],
            "score": score,
            "dimensions": dimensions,
            "delta": {
                "self_correction": human_correction,
                "changed": {"note": correction_note or ""} if human_correction and correction_note else {},
            },
            "source": current["source"],
            "source_hash": current["source_hash"],
            "kb_eval": {
                "base_date": current["base_date"],
                "iteration": current["iteration"],
                "scenario_id": current["scenario_id"],
                "checksheet": source,
            },
        }
        records.append(payload)
        current = None
        checks = {}
        correction_note = None
        in_note = False

    for line in text.splitlines():
        case_match = CASE_RE.match(line)
        if case_match:
            flush()
            current = json.loads(case_match.group("meta"))
            checks = {}
            correction_note = None
            in_note = False
            continue
        if current is None:
            continue
        if line.startswith("**") and line.endswith("**"):
            # Section header: Optional Correction Note starts note capture;
            # any other section (e.g. Source Excerpts) ends it so its quoted
            # excerpt lines cannot overwrite the reviewer's note.
            in_note = line == "**Optional Correction Note**"
            continue
        check_match = CHECK_RE.match(line)
        if check_match:
            checks[check_match.group("label")] = checked(check_match.group("mark"))
            continue
        if in_note and line.startswith(">"):
            note = line[1:].strip()
            if note:
                correction_note = note if correction_note is None else f"{correction_note}\n{note}"
    flush()
    return records


def parse_file(path: Path) -> list[dict[str, Any]]:
    return parse_text(display_path(path), path.read_text(encoding="utf-8"))


def fetch_github_issue_records(search: str, limit: int) -> list[dict[str, Any]]:
    out = run([
        "gh",
        "issue",
        "list",
        "--state",
        "all",
        "--search",
        search,
        "--json",
        "number,title,body,url",
        "--limit",
        str(limit),
    ])
    issues = json.loads(out or "[]")
    records: list[dict[str, Any]] = []
    for issue in issues:
        source = f"github_issue:{issue['url']}"
        for record in parse_text(source, issue.get("body") or ""):
            record["kb_eval"]["github_issue"] = {
                "number": issue["number"],
                "title": issue["title"],
                "url": issue["url"],
            }
            records.append(record)
    return records


def existing_decision_refs(pg_dsn: str, refs: list[str]) -> set[str]:
    if not refs:
        return set()
    with psycopg2.connect(pg_dsn) as conn, conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT content
            FROM messages
            WHERE workspace_name = %s
              AND metadata->>'record_type' = 'score_given'
              AND content IS NOT NULL
            """,
            (HONCHO_WS,),
        )
        found: set[str] = set()
        wanted = set(refs)
        for row in cur.fetchall():
            try:
                payload = json.loads(row["content"]).get("payload") or {}
            except Exception:
                continue
            ref = str(payload.get("decision_ref") or "")
            if ref in wanted:
                found.add(ref)
        return found


def honcho_post(path: str, body: dict[str, Any]) -> dict[str, Any]:
    response = requests.post(
        f"{HONCHO_URL}{path}",
        headers={"Content-Type": "application/json"},
        json=body,
        timeout=60,
    )
    response.raise_for_status()
    return response.json()


def ensure_feedback_session(base_date: str) -> str:
    session_name = f"kb-eval-feedback-{base_date}"
    response = requests.get(f"{HONCHO_URL}/v3/workspaces/{HONCHO_WS}/sessions/{session_name}", timeout=20)
    if response.status_code == 200:
        return session_name
    if response.status_code not in {404, 405}:
        response.raise_for_status()
    honcho_post(
        f"/v3/workspaces/{HONCHO_WS}/sessions",
        {
            "id": session_name,
            "metadata": {
                "actor": "human",
                "peer_id": "human",
                "session_type": "kb_eval_feedback",
                "base_date": base_date,
            },
        },
    )
    return session_name


def build_message(payload: dict[str, Any]) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    return {
        "content": json.dumps({"ts": now, "type": "score_given", "payload": payload}, ensure_ascii=False),
        "peer_id": "human",
        "metadata": {
            "record_type": "score_given",
            "actor": "human",
            "peer_id": "human",
            "target_actor": payload["target_actor"],
            "has_dimensions": True,
            "source": "kb_eval_checksheet",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="File or directory to scan.")
    parser.add_argument("--github-search", default=None, help="Read checked GitHub issue bodies matching this search query.")
    parser.add_argument("--github-limit", type=int, default=100)
    parser.add_argument("--execute", action="store_true", help="Write parsed score_given feedback to Honcho.")
    args = parser.parse_args()

    records: list[dict[str, Any]] = []
    files: list[Path] = []
    if args.github_search:
        records.extend(fetch_github_issue_records(args.github_search, args.github_limit))
    else:
        input_path = Path(args.input)
        files = [input_path] if input_path.is_file() else sorted(input_path.glob("**/iteration-*.md"))
        for path in files:
            records.extend(parse_file(path))

    pg_dsn = os.environ.get("POSTGRES_URL")
    if not pg_dsn:
        raise SystemExit("POSTGRES_URL is required")
    existing = existing_decision_refs(pg_dsn, [record["decision_ref"] for record in records])
    new_records = [record for record in records if record["decision_ref"] not in existing]

    summary = {
        "files_scanned": len(files),
        "github_search": args.github_search,
        "checked_records": len(records),
        "already_ingested": len(existing),
        "new_records": len(new_records),
        "execute": bool(args.execute),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    if not args.execute or not new_records:
        return

    by_date: dict[str, list[dict[str, Any]]] = {}
    for record in new_records:
        by_date.setdefault(record["kb_eval"]["base_date"], []).append(record)
    for base_date, items in by_date.items():
        session = ensure_feedback_session(base_date)
        honcho_post(
            f"/v3/workspaces/{HONCHO_WS}/sessions/{session}/messages",
            {"messages": [build_message(item) for item in items]},
        )
        print(f"wrote {len(items)} score_given records to {session}")


if __name__ == "__main__":
    main()
