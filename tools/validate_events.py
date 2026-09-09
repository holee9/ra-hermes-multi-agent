#!/usr/bin/env python3
"""
계약 v2.1 검증기.

검사 항목:
  1. JSON Schema (docs/contract/event-v2.1.schema.json)
  2. 대화 규칙 — 자기전달·종결형 답신·broadcast 답신의무·requires_reply 파생
  3. 홉 체인 — corr가 가리키는 이벤트 존재, hops == 원인.hops+1, conversation 상속
  4. id 유일성, ts 단조성(경고)
  5. 홉 상한 — --hop-cap 지정 시 초과 이벤트 보고(에스컬레이션 대상)

사용:
  python3 tools/validate_events.py mock/events-v2.1.jsonl
  python3 tools/validate_events.py log.jsonl --hop-cap 12 --strict
종료코드: 0 통과 / 1 오류 / 2 입력 문제
의존: jsonschema (pip install jsonschema --break-system-packages)
"""
import argparse, json, sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("jsonschema 미설치: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

TERMINAL = {"inform", "agree", "refuse", "done"}
OBLIGATING = {"request", "query", "propose"}
DEFAULT_ACT = {
    "case_open": "inform", "matching": "propose", "comment": "inform", "handoff": "request",
    "vote_call": "query", "vote_cast": "inform", "vote_result": "inform", "eval3": "inform",
    "artifact": "inform", "absence": "inform", "infra": "inform", "policy": "inform",
    "hire_proposal": "propose", "escalation": "request",
}


def load_jsonl(path):
    events = []
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                events.append((n, json.loads(line)))
            except json.JSONDecodeError as e:
                events.append((n, {"__parse_error__": str(e)}))
    return events


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--schema", default=str(Path(__file__).resolve().parent.parent / "docs/contract/event-v2.1.schema.json"))
    ap.add_argument("--hop-cap", type=int, default=None)
    ap.add_argument("--strict", action="store_true", help="경고도 오류로")
    a = ap.parse_args()

    schema = json.load(open(a.schema, encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    events = load_jsonl(a.jsonl)

    errors, warns = [], []
    by_id = {}
    last_ts = None

    def err(n, ev, msg): errors.append(f"L{n} {ev.get('id','?')}: {msg}")
    def warn(n, ev, msg): warns.append(f"L{n} {ev.get('id','?')}: {msg}")

    # pass 1: schema + index
    for n, ev in events:
        if "__parse_error__" in ev:
            errors.append(f"L{n}: JSON 파싱 실패 — {ev['__parse_error__']}")
            continue
        for e in validator.iter_errors(ev):
            err(n, ev, f"schema: {e.message} @ {'/'.join(map(str, e.absolute_path)) or '<root>'}")
        eid = ev.get("id")
        if eid:
            if eid in by_id:
                err(n, ev, f"id 중복 (첫 등장 L{by_id[eid][0]})")
            else:
                by_id[eid] = (n, ev)
        ts = ev.get("ts")
        if ts and last_ts and ts < last_ts:
            warn(n, ev, f"ts 역행 ({last_ts} → {ts})")
        if ts:
            last_ts = ts

    # pass 2: conversation rules
    for n, ev in events:
        if "__parse_error__" in ev or "to" not in ev:
            continue
        actor, to, act = ev.get("actor"), ev["to"], ev.get("act")
        rr, hops, corr = ev.get("requires_reply"), ev.get("hops"), ev.get("corr")

        if to == actor:
            err(n, ev, "자기 전달 (to == actor)")
        if act in TERMINAL and rr is True:
            err(n, ev, f"종결형 act={act}에 requires_reply=true")
        if to == "broadcast" and rr is True:
            err(n, ev, "broadcast에 requires_reply=true")
        if act in OBLIGATING and rr is False and to != "broadcast":
            warn(n, ev, f"act={act}인데 requires_reply=false — 의도적이면 허용")
        # comment는 범용 답신 운반체, artifact는 done 동반이 정상 — 기본 act 이탈 경고 면제
        exp = DEFAULT_ACT.get(ev.get("kind"))
        if act and exp and act != exp and ev.get("kind") not in ("policy", "escalation", "comment", "artifact"):
            warn(n, ev, f"kind={ev['kind']} 기본 act={exp}, 실제 {act}")

        if corr:
            if corr not in by_id:
                err(n, ev, f"corr {corr} 가 로그에 없음")
            else:
                _, src = by_id[corr]
                if src.get("act") in TERMINAL:
                    err(n, ev, f"종결형 이벤트 {corr}(act={src.get('act')})에 답신")
                sh = src.get("hops", 0)
                if hops != sh + 1:
                    err(n, ev, f"hops={hops}, 기대값 {sh + 1} (corr hops={sh})")
                if src.get("conversation") and ev.get("conversation") != src.get("conversation"):
                    err(n, ev, f"conversation 불일치: {ev.get('conversation')} ≠ 원인 {src.get('conversation')}")
        else:
            if hops not in (0, None):
                err(n, ev, f"corr 없는데 hops={hops} (최초 발신은 0)")

        if a.hop_cap is not None and hops is not None and hops > a.hop_cap:
            warn(n, ev, f"hops={hops} > HOP_CAP={a.hop_cap} → 에스컬레이션 대상")

    # refuse-deadlock
    refusers = {}
    for n, ev in events:
        if ev.get("act") == "refuse" and ev.get("conversation"):
            refusers.setdefault(ev["conversation"], set()).add(ev.get("actor"))
    for conv, who in refusers.items():
        if len(who) >= 2:
            warn(0, {"id": conv}, f"거절 교착: {sorted(who)} 상호 refuse → 에스컬레이션 대상")

    total = sum(1 for _, e in events if "__parse_error__" not in e)
    conv = sum(1 for _, e in events if "to" in e)
    print(f"이벤트 {total}건 (대화 {conv}, 관찰 {total - conv})")
    for w in warns: print(f"  WARN  {w}")
    for e in errors: print(f"  ERROR {e}")
    fail = bool(errors) or (a.strict and warns)
    print("결과:", "실패" if fail else "통과", f"— 오류 {len(errors)}, 경고 {len(warns)}")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
