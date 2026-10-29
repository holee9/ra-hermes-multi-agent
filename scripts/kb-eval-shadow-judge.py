#!/usr/bin/env python3
"""kb-eval shadow judge (#159 API layer, 2026-10-29) — independent second opinion.

Runs AFTER the session's provisional scoring (가채점). For each case, asks the
Anthropic API to independently score the captured response against the same
source excerpts, under the primary-source discipline codified from the
2026-10-28 mis-verification incident:

  - A defect may only be asserted with the correct fact AND its primary basis
    (regulation article, standard title/edition, official guidance name).
  - Search-engine summaries / general recollection are NOT evidence; if the
    judge cannot substantiate a defect from primary knowledge it must mark it
    "unverified_suspicion" (advisory) instead of asserting it.
  - No penalties for style, brevity, or conservative hedging.

The judge has PROPOSAL power only: disagreements are surfaced for the human /
next session round; this script never changes scores or ingests anything.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_guard_spec = importlib.util.spec_from_file_location("anthropic_guard", str(ROOT / "scripts" / "anthropic_guard.py"))
_guard = importlib.util.module_from_spec(_guard_spec)
_guard_spec.loader.exec_module(_guard)

SYSTEM = """You are an independent reviewer for medical-device regulatory-affairs answer quality (RA kb-eval).
You will get: a case focus, the KB source excerpts the answer was based on, the captured agent answer,
and the first reviewer's score + note. Score the answer independently on the same scale:
3 = pass, usable without correction; 2 = usable with minor correction (a specific defect exists);
1 = correction required (serious error or fabricated regulatory claim).

HARD DISCIPLINE (from a measured incident where a reviewer's own web-verification was wrong):
1. Assert a defect ONLY if you can state the correct fact AND its primary basis
   (regulation article number, standard title/edition, official guidance name) from your
   own solid knowledge. If you are not certain, list it under "unverified_suspicion" instead
   — an unverified suspicion must NEVER lower the score.
2. Search-engine summaries and vague recollections are not evidence.
3. Never penalize conservative hedging, style, or brevity. Judge only regulatory substance.

Respond with JSON only:
{"score": 1|2|3,
 "defects": [{"type": "citation|jurisdiction|subject|fabrication|other", "quote": "<exact short quote>",
              "correct_fact": "<...>", "basis": "<primary source>"}],
 "unverified_suspicion": [{"quote": "<...>", "doubt": "<one line>"}],
 "confidence": 0.0-1.0}"""

CASE_RE = re.compile(r"^### (kb-eval-\S+)", re.MULTILINE)


def parse_cases(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    cases = []
    parts = CASE_RE.split(text)
    # parts: [pre, id1, body1, id2, body2, ...]
    for i in range(1, len(parts) - 1, 2):
        cid, body = parts[i], parts[i + 1]
        focus = re.search(r"^- Focus: (.+)$", body, re.MULTILINE)
        m_score = re.search(r"- \[x\] Score (\d)", body)
        m_note = re.search(r"\*\*Optional Correction Note\*\*\n\n> ([^\n]+)", body)
        # response: between Agent Response and Reviewer Score
        m_resp = re.search(r"\*\*Agent Response\*\*[^\n]*\n(.*?)\n\*\*Reviewer Score\*\*", body, re.DOTALL)
        resp = m_resp.group(1) if m_resp else ""
        resp = "\n".join(re.sub(r"^>\s?", "", ln) for ln in resp.splitlines()).strip()
        # source excerpts
        m_ex = re.search(r"\*\*Source Excerpts\*\*\n(.*)$", body, re.DOTALL)
        excerpts = m_ex.group(1).strip()[:4000] if m_ex else ""
        if resp:
            cases.append({
                "case_id": cid,
                "focus": focus.group(1) if focus else "",
                "session_score": int(m_score.group(1)) if m_score else None,
                "session_note": m_note.group(1) if m_note else "",
                "response": resp[:12000],
                "excerpts": excerpts,
            })
    return cases


def judge(case: dict, model: str) -> dict:
    user = (
        f"Case: {case['case_id']}\nFocus: {case['focus']}\n\n"
        f"## KB source excerpts\n{case['excerpts']}\n\n"
        f"## Captured agent answer\n{case['response']}\n\n"
        f"## First reviewer\nscore: {case['session_score']}\nnote: {case['session_note'] or '(none)'}\n\n"
        "Score independently. JSON only."
    )
    data = _guard.call(model, [{"role": "user", "content": user}], 1500, system=SYSTEM,
                       thinking={"type": "between_tools"})
    raw = "".join(b.get("text", "") for b in data["content"] if b.get("type") == "text").strip()
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        return {"error": f"unparseable: {raw[:150]}"}
    return json.loads(m.group(0))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, help="scored iteration-XX.md")
    ap.add_argument("--model", default="claude-sonnet-5-5")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    path = Path(args.input)
    cases = parse_cases(path)
    if not cases:
        print("no scored cases found (score the checksheet first)", file=sys.stderr)
        return 2
    out_path = Path(args.out) if args.out else ROOT / "reports" / "kb-eval-shadow" / f"{path.parent.name}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    results = []
    disagree = 0
    for c in cases:
        try:
            v = judge(c, args.model)
        except Exception as e:  # fail-open: advisory layer must not break the round
            v = {"error": f"{type(e).__name__}: {e}"}
        d = v.get("score") if "score" in v else None
        if d is not None and c["session_score"] is not None and d != c["session_score"]:
            disagree += 1
        results.append({**c, "shadow": v})
        print(f"{c['case_id']}: session={c['session_score']} shadow={d}"
              f"{' <-- DISAGREE' if d is not None and d != c['session_score'] else ''}", flush=True)

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model": args.model,
        "cases": len(cases),
        "parsed": sum(1 for r in results if "score" in r["shadow"]),
        "agreements": len(cases) - disagree - sum(1 for r in results if "score" not in r["shadow"]),
        "disagreements": disagree,
    }
    out_path.write_text(json.dumps({"summary": summary, "results": results}, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    print(f"ledger: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
