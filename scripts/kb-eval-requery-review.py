#!/usr/bin/env python3
"""#147 재질의 결과 검토 자료 생성 — 원장·응답·출처를 연결하고 자동 점검을 붙인다.

사람 최종 판정을 **대신하지 않는다.** 사람이 보기 전에 기계로 확인 가능한 것만 미리 걸러
검토 시간을 줄이는 용도다. 자동 점검이 통과했다고 규제적으로 옳다는 뜻이 아니다.

붙이는 점검:
- **인용 식별자 검증**(#118 계열): 응답이 인용한 K/P 번호가 **전달한 발췌에 실제로 있는지**.
  없으면 창작 의심 — 이 프로젝트에서 실측된 실패 유형이다.
- **규제 인용 린트**(`ra_citation_lint`): 구조적으로 불가능한 조문 인용(C1).
- 길이·출처 대조 등 기초 지표.

네트워크·LLM 호출 없음. 원장만 읽는다.

사용:
    python3 scripts/kb-eval-requery-review.py --batch approved-20260911
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# FDA 식별자 패턴. 한글 조사가 붙어도 잡히도록 \b 대신 인접 영숫자 부재로 경계를 잡는다
# (Python 의 \b 는 한글을 단어 문자로 보기 때문에 "K222222도" 에서 실패한다).
_ID_PATTERNS = (
    re.compile(r"(?<![A-Za-z0-9])K\d{6}(?![A-Za-z0-9])"),
    re.compile(r"(?<![A-Za-z0-9])P\d{6}(?![A-Za-z0-9])"),
    re.compile(r"(?<![A-Za-z0-9])DEN\d{6}(?![A-Za-z0-9])"),
)


def _load_lint():
    path = Path(__file__).resolve().parent / "ra_citation_lint.py"
    spec = importlib.util.spec_from_file_location("ra_citation_lint_review", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ra_citation_lint_review"] = mod
    spec.loader.exec_module(mod)
    return mod


def cited_ids(text: str) -> list[str]:
    out: list[str] = []
    for p in _ID_PATTERNS:
        out += p.findall(text or "")
    return sorted(set(out))


def unverified_ids(response: str, shown: str) -> list[str]:
    """응답이 인용했는데 전달한 발췌에 없는 식별자. 공백·하이픈 차이는 무시한다."""
    norm = re.sub(r"[\s\-]", "", shown or "").upper()
    return [i for i in cited_ids(response) if re.sub(r"[\s\-]", "", i).upper() not in norm]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="#147 재질의 결과 검토 자료 (사람 판정 보조)")
    ap.add_argument("--batch", required=True, help="원장 배치 이름")
    ap.add_argument("--out", default=None, help="마크다운 출력 경로 (기본: 배치 디렉터리)")
    a = ap.parse_args(argv)

    base = ROOT / "reports" / "kb-eval-requery-147" / a.batch
    ledger = base / "ledger.jsonl"
    if not ledger.exists():
        print(json.dumps({"error": "원장 없음", "path": str(ledger)}, ensure_ascii=False))
        return 2

    recs = [json.loads(l) for l in ledger.read_text(encoding="utf-8").splitlines() if l.strip()]
    starts = {r["attempt_id"]: r for r in recs if r.get("event") == "attempt_start"}
    results = [r for r in recs if r.get("event") == "attempt_result"]
    lint = _load_lint()

    rows, detail = [], []
    for r in results:
        s = starts.get(r["attempt_id"], {})
        resp, shown = r.get("response") or "", s.get("assignment") or ""
        if r.get("ok"):
            bad_ids = unverified_ids(resp, shown)
            flags = lint.lint_citations(resp)
            errs = [f for f in flags if f.get("severity") == lint.SEV_ERROR]
            verdict = "검토 필요" if (bad_ids or errs) else "자동 점검 통과"
        else:
            bad_ids, errs, verdict = [], [], "응답 없음"
        rows.append({
            "case_id": r["case_id"], "ok": r.get("ok"), "chars": r.get("chars", 0),
            "old_source": (r.get("old_source") or "").split("/")[-1],
            "new_source": (r.get("new_source") or "").split("/")[-1],
            "cited_ids": cited_ids(resp), "unverified_ids": bad_ids,
            "citation_errors": [f.get("message", "")[:80] for f in errs],
            "verdict": verdict, "error": r.get("error"),
        })
        if r.get("ok"):
            detail.append((r["case_id"], r.get("focus", ""), resp))

    md = ["# #147 재질의 결과 검토 자료", "",
          f"배치: `{a.batch}` · 시도 {len(starts)} · 결과 {len(results)} · "
          f"응답 수신 {sum(1 for x in rows if x['ok'])}", "",
          "> **이 자료는 사람 판정을 대신하지 않는다.** 자동 점검은 기계로 확인 가능한 것만 본다 —",
          "> 통과했다고 규제적으로 옳다는 뜻이 아니고, 규제 판단은 사람이 해야 한다.", "",
          "## 요약", "",
          "| case | 수신 | 자 | old source | new source | 미검증 식별자 | 인용 오류 | 판정 |",
          "|---|---|---|---|---|---|---|---|"]
    for x in rows:
        md.append(f"| `{x['case_id'][-22:]}` | {'O' if x['ok'] else 'X'} | {x['chars']} | "
                  f"{x['old_source'][:26]} | {x['new_source'][:26]} | "
                  f"{', '.join(x['unverified_ids']) or '-'} | {len(x['citation_errors'])} | {x['verdict']} |")

    md += ["", "## 자동 점검이 본 것 / 보지 않은 것", "",
           "**본 것**: 응답이 인용한 FDA 식별자(K/P/DEN 번호)가 전달한 발췌에 실제로 있는지, "
           "구조적으로 불가능한 조문 인용이 있는지, 응답 길이.", "",
           "**보지 않은 것**: 규제 판단의 타당성, 분류·경로 선택의 정확성, 인용 조문이 "
           "**맥락에 맞는지**, 새 소스가 그 focus 에 정말 적절한지. 전부 사람 판정 영역이다.", ""]

    for cid, focus, resp in detail:
        # 사람 검토 자료다 — 전문을 자르지 않는다. 응답 속 백틱보다 긴 울타리로 감싼다.
        fence = "`" * max(3, max((len(m) for m in re.findall(r"`+", resp)), default=0) + 1)
        md += [f"### {cid}", "", f"focus: {focus}", "", "<details><summary>응답 전문</summary>", "",
               fence, resp, fence, "", "</details>", ""]

    out = Path(a.out) if a.out else base / "review.md"
    out.write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({
        "batch": a.batch, "results": len(results),
        "received": sum(1 for x in rows if x["ok"]),
        "auto_pass": sum(1 for x in rows if x["verdict"] == "자동 점검 통과"),
        "needs_review": sum(1 for x in rows if x["verdict"] == "검토 필요"),
        "no_response": sum(1 for x in rows if x["verdict"] == "응답 없음"),
        "output": str(out.relative_to(ROOT)),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
