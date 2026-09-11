#!/usr/bin/env python3
"""#147 케이스 생성 결함 11건 재질의 — 전용 실행기 (기본 dry-run).

## 왜 전용 실행기인가

기존 `kb-eval-checksheet.py` 를 그대로 쓰면 안 된다(2026-09-11 preflight 확인):

- **케이스 지정 인자가 없다.** `select_cases()` 가 `--date` 기준으로 **새로** 뽑으므로
  이 11건을 겨냥하지 못한다.
- **호출 수가 범위를 넘는다.** 기본 3 iterations × 3 agents × 5 cases = 최대 45회.
  승인된 것은 11회다.
- **원본을 덮어쓴다.** 같은 date/iteration 으로 재실행하면 기존 `iteration-NN.md` 를
  `write_text` 로 덮는다 — 채점 근거가 사라진다.

그래서 이 스크립트는 **원본 체크시트를 읽지도 쓰지도 않고**, 지정된 11건만,
독립 출력 디렉터리에 기록한다.

## 안전 규칙

- 기본 **dry-run**. `--execute` 없이는 LLM 을 호출하지 않는다.
- 호출 상한 **11회 고정**. 실패도 예산을 소모한다(재시도하지 않는다).
- 출력은 `reports/kb-eval-requery-147/` 아래. `docs/kb-eval-checksheets/` 는 건드리지 않는다.
- 과거 레코드를 수정하지 않는다. 결과는 **새 산출물**이며 old→new lineage 를 함께 남긴다.

사용:
    python3 scripts/kb-eval-requery-147.py            # 계획만 출력
    python3 scripts/kb-eval-requery-147.py --execute  # 실제 11회 호출
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "reports" / "kb-eval-requery-147"
CALL_BUDGET = 11                      # 승인된 호출 수 — 초과 금지

# 재선정 결과(#147 댓글 게시분). old_source 는 lineage 기록용이며 호출에는 쓰지 않는다.
CASES: list[dict] = [
    {"n": 1, "case_id": "kb-eval-20260716-it01-ra_eu-005", "profile": "ra-eu", "peer": "ra_eu",
     "focus": "clinical evaluation gap analysis", "defect": "capture_failed",
     "old_source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md",
     "new_source": "Clinical_Evaluation_MDR_동등성_충분성_기준.md"},
    {"n": 2, "case_id": "kb-eval-20260717-it01-ra_eu-004", "profile": "ra-eu", "peer": "ra_eu",
     "focus": "PMS and PMCF planning", "defect": "source_mismatch",
     "old_source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md",
     "new_source": "158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md"},
    {"n": 3, "case_id": "kb-eval-20260718-it01-ra_kr-003", "profile": "ra-kr", "peer": "ra_kr",
     "focus": "supplementary-response strategy", "defect": "source_mismatch",
     "old_source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용_방사선_발생장치_안전관리규칙_제1122호.md",
     "new_source": "MFDS_보완자료_대응전략.md"},
    {"n": 4, "case_id": "kb-eval-20260719-it01-ra_us-003", "profile": "ra-us", "peer": "ra_us",
     "focus": "510(k) predicate strategy", "defect": "source_mismatch",
     "old_source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md",
     "new_source": "eSTAR_02_Substantial_Equivalence.md"},
    {"n": 5, "case_id": "kb-eval-20260720-it01-ra_eu-005", "profile": "ra-eu", "peer": "ra_eu",
     "focus": "clinical evaluation gap analysis", "defect": "source_mismatch",
     "old_source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md",
     "new_source": "Clinical_Evaluation_MDR_동등성_충분성_기준.md"},
    {"n": 6, "case_id": "kb-eval-20260722-it02-ra_us-002", "profile": "ra-us", "peer": "ra_us",
     "focus": "510(k) predicate strategy", "defect": "source_mismatch",
     "old_source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md",
     "new_source": "eSTAR_02_Substantial_Equivalence.md"},
    {"n": 7, "case_id": "kb-eval-20260722-it02-ra_us-003", "profile": "ra-us", "peer": "ra_us",
     "focus": "510(k) predicate strategy", "defect": "source_mismatch",
     "old_source": "github:holee9/MD-process/issue-drafts/979_FDA_510k_RTA_기초보강_4주차_재이월.md",
     "new_source": "eSTAR_02_Substantial_Equivalence.md"},
    {"n": 8, "case_id": "kb-eval-20260722-it02-ra_us-004", "profile": "ra-us", "peer": "ra_us",
     "focus": "510(k) predicate strategy", "defect": "source_mismatch",
     "old_source": "github:holee9/MD-process/issue-drafts/220_13_FDA_510k_RTA_핵심양식_초안.md",
     "new_source": "eSTAR_02_Substantial_Equivalence.md"},
    {"n": 9, "case_id": "kb-eval-20260722-it02-ra_eu-005", "profile": "ra-eu", "peer": "ra_eu",
     "focus": "MDR classification and conformity route", "defect": "source_mismatch",
     "old_source": "github:holee9/MD-process/issue-drafts/902_AUDIT_GUIDE-VIG-001_EU_MDR_보존기한_인용부정확.md",
     "new_source": "943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md"},
    {"n": 10, "case_id": "kb-eval-20260723-it01-ra_kr-002", "profile": "ra-kr", "peer": "ra_kr",
     "focus": "MFDS classification and licensing route", "defect": "source_mismatch",
     "old_source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md",
     "new_source": "MFDS_디지털의료제품법_하위고시_추적.md"},
    {"n": 11, "case_id": "kb-eval-20260724-it03-ra_kr-005", "profile": "ra-kr", "peer": "ra_kr",
     "focus": "supplementary-response strategy", "defect": "source_mismatch",
     "old_source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md",
     "new_source": "MFDS_보완자료_대응전략.md"},
]


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def resolve_source(conn, filename: str) -> tuple[str, str, list[str]] | None:
    """재선정된 파일명으로 실제 source_path·hash·발췌를 찾는다. 없으면 None."""
    # ra_knowledge 에는 source_hash 컬럼이 없다(실제 스키마: id, source_path, chunk_index,
    # content, embedding, metadata, indexed_at). 해시는 metadata 에 있으면 쓰고 없으면 비운다.
    with conn.cursor() as cur:
        cur.execute(
            "SELECT source_path, COALESCE(metadata->>'source_hash', ''), content "
            "FROM ra_knowledge WHERE source_path LIKE %s ORDER BY chunk_index LIMIT 3",
            (f"%{filename}",),
        )
        rows = cur.fetchall()
    if not rows:
        return None
    return rows[0][0], rows[0][1], [r[2][:600] for r in rows]


def build_assignment(case: dict, source_path: str, source_hash: str, excerpts: list[str]) -> str:
    """과제문. 원본 파이프라인과 같은 골격을 쓰되 재질의임을 명시한다."""
    lines = [
        "Daily regulatory growth case (re-query)",
        f"[internal run metadata — not a device attribute] Re-query of: {case['case_id']}",
        f"[internal run metadata — not a device attribute] Reason: case-generation defect ({case['defect']})",
        f"Primary focus: {case['focus']}",
        f"Source: {source_path}",
        f"Source hash: {source_hash}",
        "Note: the lines above marked '[internal run metadata]' are pipeline bookkeeping only — "
        "they are not device names, categories, or classifications. Do not reference them when "
        "determining device type, intended use, or regulatory classification.",
        "Assignment: Produce a regulatory draft that identifies classification/submission route, "
        "required evidence, missing information, risk controls, citations, and human-escalation triggers.",
        "Cite only identifiers that appear in the source excerpts below. If the source does not "
        "contain an identifier you need, say so explicitly instead of supplying one.",
        "",
        "Source excerpts:",
    ]
    lines += [f"- {e}" for e in excerpts]
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="#147 결함 11건 재질의 (기본 dry-run)")
    ap.add_argument("--execute", action="store_true", help="실제 LLM 호출 (없으면 계획만)")
    a = ap.parse_args(argv)

    dsn = os.environ.get("POSTGRES_URL")
    if not dsn:
        print(json.dumps({"error": "POSTGRES_URL 미설정"}, ensure_ascii=False))
        return 2

    assert len(CASES) == CALL_BUDGET, f"케이스 수({len(CASES)}) != 승인 호출 수({CALL_BUDGET})"

    import psycopg2
    sheet = _load("kb_eval_checksheet_147", "kb-eval-checksheet.py")

    plan, unresolved = [], []
    with psycopg2.connect(dsn) as conn:
        for c in CASES:
            found = resolve_source(conn, c["new_source"])
            if not found:
                unresolved.append(c["case_id"])
                continue
            path, shash, excerpts = found
            plan.append({**c, "resolved_source": path, "source_hash": shash,
                         "assignment": build_assignment(c, path, shash, excerpts)})

    if unresolved:
        print(json.dumps({"error": "재선정 소스를 KB 에서 찾지 못함", "cases": unresolved},
                         ensure_ascii=False, indent=2))
        return 2

    if not a.execute:
        print(json.dumps({
            "mode": "dry-run", "planned_calls": len(plan), "call_budget": CALL_BUDGET,
            "output_dir": str(OUT_DIR.relative_to(ROOT)),
            "touches_original_checksheets": False,
            "cases": [{"n": p["n"], "case_id": p["case_id"], "profile": p["profile"],
                       "old_source": p["old_source"].split("/")[-1],
                       "new_source": p["resolved_source"].split("/")[-1],
                       "assignment_chars": len(p["assignment"])} for p in plan],
        }, ensure_ascii=False, indent=2))
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    results, used = [], 0
    for p in plan:
        if used >= CALL_BUDGET:                       # 상한 초과 방지 — 실패도 예산 소모
            break
        used += 1
        text, error = sheet.capture_agent_response(p["profile"], p["assignment"])
        results.append({
            "n": p["n"], "case_id": p["case_id"], "profile": p["profile"], "peer": p["peer"],
            "focus": p["focus"], "defect": p["defect"],
            "old_source": p["old_source"], "new_source": p["resolved_source"],
            "source_hash": p["source_hash"],
            "ok": not error and bool(text and text.strip()),
            "error": error or None, "chars": len(text or ""), "response": text or "",
            "captured_at": datetime.now(timezone.utc).isoformat(),
        })

    out = OUT_DIR / f"requery-{stamp}.json"
    out.write_text(json.dumps({
        "issue": 147, "call_budget": CALL_BUDGET, "calls_used": used,
        "ok": sum(1 for r in results if r["ok"]), "failed": sum(1 for r in results if not r["ok"]),
        "lineage_note": "원본 레코드는 수정하지 않았다. 이 산출물은 새 기록이며 old_source↔new_source 로 추적한다.",
        "results": results,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({"mode": "execute", "calls_used": used,
                      "ok": sum(1 for r in results if r["ok"]),
                      "failed": sum(1 for r in results if not r["ok"]),
                      "output": str(out.relative_to(ROOT))}, ensure_ascii=False, indent=2))
    return 0 if all(r["ok"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
