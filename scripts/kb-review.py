#!/usr/bin/env python3
"""KB pre-index review — API-based regulatory sanity check for changed KB files.

Complements kb-watch (#158): kb-watch detects WHAT changed; this script reviews
the CONTENT before it propagates into advisory answers. Targets the #132/#144
defect class (KB source errors reaching agents).

All API calls go through anthropic_guard (#159) — monthly credit capped.

Usage:
  python3 scripts/kb-review.py --file <kb-repo>/<path>.md
  python3 scripts/kb-review.py --since 24        # review kb-watch ledger entries
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anthropic_guard import call  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "reports" / "kb-watch" / "ledger.jsonl"
OUT_DIR = ROOT / "reports" / "kb-review"
KB_ROOT = Path("/home/abyz-lab/work/workspace-github")

MAX_DOC_CHARS = 30_000

SYSTEM = """You are a senior medical-device regulatory affairs editor. Review the given KB
document for defects that would propagate into regulatory advice. Check ONLY:
1. Regulatory citations: article/section numbers, regulation names, standard
   editions/years, guidance dates — internally consistent and plausibly real.
2. Jurisdiction attribution: FDA / EU MDR / MFDS concepts not mixed
   (e.g. 'MFDS Section 524B', QMSR-as-KGMP, PSUR/PMCF unlabeled in KR context).
3. Dates & staleness: guidance or law references that are superseded or
   internally contradicted by the document's own changelog.
4. Structural contradictions: table rows or sections asserting conflicting facts.
Do NOT flag style, brevity, or missing content — only defects.
Respond with JSON only:
{"verdict": "ok" | "warn",
 "findings": [{"severity": "high" | "low", "type": "citation|jurisdiction|staleness|contradiction",
               "quote": "<exact short quote from doc>", "note": "<one-line reason>"}]}"""


def review_file(path: Path, model: str) -> dict:
    text = path.read_text(encoding="utf-8")[:MAX_DOC_CHARS]
    user = f"Review this KB document ({path.name}):\n\n{text}"
    data = call(model, [{"role": "user", "content": user}], 4000, system=SYSTEM,
                thinking={"type": "between_tools"})
    raw = "".join(b.get("text", "") for b in data["content"] if b.get("type") == "text").strip()
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    verdict = json.loads(m.group(0)) if m else {"verdict": "warn",
                                                "findings": [{"severity": "low", "type": "citation",
                                                              "quote": "", "note": f"unparseable reply: {raw[:120]}"}]}
    return {"file": str(path), "reviewed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "model": model, **verdict}


def files_since(hours: int) -> list[Path]:
    out, seen = [], set()
    if not LEDGER.exists():
        return out
    now = datetime.now(timezone.utc).timestamp()
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        ts = datetime.fromisoformat(rec["ts"]).timestamp()
        if now - ts > hours * 3600 or rec.get("kind") != "kb-file-changed":
            continue
        p = KB_ROOT / rec["repo"] / rec["file"]
        if p.suffix == ".md" and p.exists() and str(p) not in seen:
            seen.add(str(p))
            out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="KB pre-index API review (#160)")
    ap.add_argument("--file", help="KB file to review (relative to workspace-github, e.g. holee9/ra-project/...)")
    ap.add_argument("--since", type=int, help="review kb-watch ledger entries from last N hours")
    ap.add_argument("--model", default="claude-sonnet-5-5")
    a = ap.parse_args()
    if not a.file and a.since is None:
        ap.error("need --file or --since")

    paths = [KB_ROOT / a.file] if a.file else files_since(a.since)
    paths = [p for p in paths if p.exists()]
    if not paths:
        print(json.dumps({"result": "no files to review"}))
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    high_total = 0
    for p in paths:
        v = review_file(p, a.model)
        slug = re.sub(r"[^A-Za-z0-9_-]+", "-", str(p.relative_to(KB_ROOT)))[:120]
        out = OUT_DIR / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-{slug}.json"
        out.write_text(json.dumps(v, ensure_ascii=False, indent=2), encoding="utf-8")
        high = [f for f in v.get("findings", []) if f.get("severity") == "high"]
        high_total += len(high)
        print(json.dumps({"file": str(p.relative_to(KB_ROOT)), "verdict": v["verdict"],
                          "high": len(high), "report": str(out.relative_to(ROOT))}, ensure_ascii=False))
    return 1 if high_total else 0


if __name__ == "__main__":
    sys.exit(main())
