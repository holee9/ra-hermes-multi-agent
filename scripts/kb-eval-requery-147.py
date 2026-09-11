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


def rel(p: Path) -> str:
    """저장소 기준 상대경로. 테스트가 OUT_DIR 를 임시 디렉터리로 바꿔도 죽지 않는다."""
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


LEDGER = OUT_DIR / "ledger.jsonl"
LOCK = OUT_DIR / ".lock"


def ledger_append(rec: dict) -> None:
    """append + fsync. 호출 **전에** 기록되어야 의미가 있으므로 즉시 내구화한다."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def ledger_state() -> dict:
    """누적 예산 상태. `attempt_start` 는 있는데 `attempt_result` 가 없으면 `unknown` 이다.

    unknown 을 0 으로 초기화하지 않는다 — 호출이 실제로 나갔는지 알 수 없으므로
    **소비한 것으로 계산**한다. 이것이 승인 총량을 지키는 유일한 안전한 가정이다.
    """
    starts, results, corrupt = {}, {}, 0
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except ValueError:
                corrupt += 1               # 건너뛰면 소비를 **적게** 세게 된다 — 아래서 fail-closed
                continue
            if r.get("event") == "attempt_start":
                starts[r["attempt_id"]] = r
            elif r.get("event") == "attempt_result":
                results[r["attempt_id"]] = r
    unknown = [a for a in starts if a not in results]
    # 손상 줄이 있으면 그것이 잃어버린 attempt_start 일 수 있어 **소비 수를 확정할 수 없다.**
    # 추측 복구나 0 초기화 대신 실행을 막는다(fail-closed). 사람이 원장을 보고 판단해야 한다.
    return {"consumed": len(starts), "resolved": len(results), "corrupt_lines": corrupt,
            "determinable": corrupt == 0,
            "unknown": unknown, "remaining": CALL_BUDGET - len(starts),
            # **시도된 모든 case 를 제외한다** — 성공한 것만 제외하면 unknown 케이스가 재전송된다.
            # unknown 은 호출이 실제로 나갔는지 알 수 없는 상태이므로 다시 보내면 예산을 두 번 쓴다.
            "attempted_case_ids": {r["case_id"] for r in starts.values()},
            "done_case_ids": {results[a]["case_id"] for a in results if results[a].get("ok")}}


def acquire_lock() -> bool:
    """배타 실행 — 중복 실행이 같은 예산을 따로 소비하지 못하게 한다."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, f"{os.getpid()} {datetime.now(timezone.utc).isoformat()}\n".encode())
    os.close(fd)
    return True


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def resolve_source(conn, filename: str) -> tuple[str, str, list[str]] | None:
    """재선정된 파일명 → **단일 정규 source_path** 확정 후 그 경로의 발췌만 가져온다.

    이전 구현의 결함(리뷰 지적): `LIKE %filename` 은 두 가지로 틀렸다.
    1. `_` 가 SQL 와일드카드라 의도치 않은 경로가 매칭된다(파일명에 `_` 가 많다).
    2. 여러 `source_path` 가 한 결과집합에 섞이는데 `LIMIT 3` 로 잘라 **첫 경로만 기록**하므로
       발췌 출처가 섞일 수 있다 — 기록된 출처와 실제 전달 내용이 달라진다.

    그래서 경로 확정과 발췌 조회를 **두 단계로 분리**하고, `_`·`%` 를 이스케이프한다.
    후보 경로가 여러 개면 모호하므로 None 을 반환해 호출을 막는다.
    """
    esc = filename.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    with conn.cursor() as cur:
        cur.execute(
            "SELECT DISTINCT source_path FROM ra_knowledge "
            "WHERE source_path LIKE %s ESCAPE '\\' ORDER BY source_path",
            (f"%/{esc}",),
        )
        paths = [r[0] for r in cur.fetchall()]
    if len(paths) != 1:
        return None                       # 0건이거나 모호 — 추측하지 않는다
    path = paths[0]
    with conn.cursor() as cur:
        cur.execute(
            "SELECT COALESCE(metadata->>'source_hash', ''), content FROM ra_knowledge "
            "WHERE source_path = %s ORDER BY chunk_index LIMIT 3",
            (path,),
        )
        rows = cur.fetchall()
    if not rows:
        return None
    return path, rows[0][0], [r[1][:600] for r in rows]


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
            "output_dir": rel(OUT_DIR),
            "touches_original_checksheets": False,
            "cases": [{"n": p["n"], "case_id": p["case_id"], "profile": p["profile"],
                       "old_source": p["old_source"].split("/")[-1],
                       "new_source": p["resolved_source"].split("/")[-1],
                       "assignment_chars": len(p["assignment"])} for p in plan],
        }, ensure_ascii=False, indent=2))
        return 0

    if not acquire_lock():
        print(json.dumps({"error": "다른 실행이 진행 중이거나 비정상 종료로 락이 남아 있다",
                          "lock": rel(LOCK),
                          "hint": "예산 상태를 ledger.jsonl 로 확인한 뒤 수동으로 락을 지울 것"},
                         ensure_ascii=False, indent=2))
        return 2

    try:
        st = ledger_state()
        if not st["determinable"]:
            print(json.dumps({"error": "원장에 손상된 줄이 있어 소비 호출 수를 확정할 수 없다",
                              "corrupt_lines": st["corrupt_lines"], "ledger": rel(LEDGER),
                              "note": "추측 복구·0 초기화 금지. 사람이 원장을 확인하고 판단해야 한다"},
                             ensure_ascii=False, indent=2))
            return 2
        if st["remaining"] <= 0:
            print(json.dumps({"error": "승인 예산 소진", **st,
                              "note": "unknown 은 소비로 계산한다 — 실제 호출 여부를 알 수 없기 때문"},
                             ensure_ascii=False, indent=2, default=list))
            return 2

        if st["unknown"]:
            # 결과가 없는 시도가 남아 있으면 재개 자체를 막는다. 그 호출이 실제로 나갔는지
            # 알 수 없으므로, 이어서 도는 것은 예산을 얼마나 쓰는지 모른 채 쓰는 것이다.
            print(json.dumps({"error": "결과 없는 시도(unknown)가 있어 재개하지 않는다",
                              "unknown": st["unknown"], "consumed": st["consumed"],
                              "ledger": rel(LEDGER),
                              "note": "자동 재전송 금지. 사람이 원장을 보고 잔여 예산을 확정해야 한다"},
                             ensure_ascii=False, indent=2))
            return 2

        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        # 시도된 case 는 성공·실패를 가리지 않고 전부 제외한다(재전송 금지).
        todo = [p for p in plan if p["case_id"] not in st["attempted_case_ids"]]
        used = 0
        for p in todo:
            if used >= st["remaining"]:               # 누적 상한 — 실패·unknown 도 예산 소모
                break
            attempt_id = f"{run_id}-{p['n']:02d}"
            # (1) 네트워크 호출 **전에** 예산 소비를 영속 기록한다. 여기서 죽어도 소비가 남는다.
            ledger_append({"event": "attempt_start", "attempt_id": attempt_id,
                           "case_id": p["case_id"], "profile": p["profile"],
                           "source_path": p["resolved_source"], "source_hash": p["source_hash"],
                           # 길이만 남기면 "무엇을 보냈는지" 가 재구성되지 않는다 — 실제 과제문을
                           # 통째로 기록해 이후 판정이 같은 입력을 볼 수 있게 한다.
                           "assignment": p["assignment"], "excerpt_chars": len(p["assignment"]),
                           "ts": datetime.now(timezone.utc).isoformat()})
            used += 1
            text, error = sheet.capture_agent_response(p["profile"], p["assignment"])
            ok = not error and bool(text and text.strip())
            # (2) 응답·오류를 **즉시** 저장한다. 다음 호출을 기다리지 않는다.
            ledger_append({"event": "attempt_result", "attempt_id": attempt_id,
                           "case_id": p["case_id"], "ok": ok, "error": error or None,
                           "chars": len(text or ""),
                           "old_source": p["old_source"], "new_source": p["resolved_source"],
                           "focus": p["focus"], "defect": p["defect"],
                           "response": text or "",
                           "ts": datetime.now(timezone.utc).isoformat()})

        st2 = ledger_state()
        # `resolved` 는 "응답이든 오류든 **기록이 확정된** 수" 이지 성공 수가 아니다.
        # 둘을 구분하지 않으면 11건 전부 실패해도 성공으로 보고된다.
        ok_n = len(st2["done_case_ids"])
        failed_n = st2["resolved"] - ok_n
        missing_n = len(CASES) - ok_n
        print(json.dumps({
            "mode": "execute", "run_id": run_id, "calls_this_run": used,
            "budget": CALL_BUDGET, "consumed_total": st2["consumed"],
            "recorded": st2["resolved"], "ok": ok_n, "failed": failed_n,
            "unknown": st2["unknown"],
            "remaining_cases": missing_n, "remaining_budget": st2["remaining"],
            "ledger": rel(LEDGER),
            "lineage_note": "원본 레코드는 수정하지 않았다. ledger 가 old_source↔new_source 추적을 담는다.",
        }, ensure_ascii=False, indent=2))
        # (3) unknown 은 자동 재전송하지 않는다. 실패·미완이 하나라도 있으면 nonzero 로 끝낸다 —
        # 전건 실패가 성공 종료코드로 나가면 호출자가 성공으로 오독한다.
        return 0 if (missing_n == 0 and failed_n == 0 and not st2["unknown"]) else 1
    finally:
        LOCK.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
