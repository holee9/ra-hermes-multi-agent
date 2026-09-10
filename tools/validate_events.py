#!/usr/bin/env python3
"""
계약 v2.1 검증기.

검사 항목:
  1. JSON Schema (docs/contract/event-v2.1.schema.json) — ts는 타임존 포함 ISO-8601 강제
  2. 대화 규칙 — 자기전달·종결형 답신·broadcast 답신의무·requires_reply 파생
  3. 홉 체인 — corr가 가리키는 이벤트 존재·선행, hops == 원인.hops+1, conversation 상속
  4. id 유일성, ts 단조성(경고)
  5. 홉 상한 — --hop-cap 지정 시 초과 이벤트 보고(에스컬레이션 대상)

의미 검증(2·3·5)은 **스키마를 통과한 이벤트에만** 적용한다. 스키마 오류 이벤트는
오류로 보고되고 corr 인덱스에서 제외되므로, 그 이벤트를 corr로 참조하는 답신은
"스키마 오류 이벤트 참조"로 별도 보고된다. (#150 P1 — 잘못된 입력이 TypeError로
종료되지 않고 항상 계약 오류로 보고되어야 한다.)

사용:
  python3 tools/validate_events.py mock/events-v2.1.jsonl
  python3 tools/validate_events.py log.jsonl --hop-cap 12 --strict
종료코드: 0 통과 / 1 오류(계약 위반·JSON 파싱 실패·--strict 시 경고) / 2 입력 문제(파일·스키마·의존성)
의존: jsonschema (pip install jsonschema --break-system-packages)
"""
import argparse
import json
import sys
from datetime import datetime
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
# 기본 act 이탈 경고 면제: comment는 범용 답신 운반체, artifact는 done 동반이 정상
ACT_WARN_EXEMPT = {"policy", "escalation", "comment", "artifact"}

DEFAULT_SCHEMA = Path(__file__).resolve().parent.parent / "docs/contract/event-v2.1.schema.json"


def is_datetime_with_tz(value) -> bool:
    """계약 §1.1: ts는 ISO-8601 + 타임존 필수. 문자열이 아니면 type 검사가 따로 잡는다."""
    if not isinstance(value, str):
        return True
    try:
        return datetime.fromisoformat(value).tzinfo is not None
    except ValueError:
        return False


def build_validator(schema: dict) -> jsonschema.Draft202012Validator:
    fc = jsonschema.FormatChecker(formats=())
    fc.checks("date-time")(is_datetime_with_tz)
    return jsonschema.Draft202012Validator(schema, format_checker=fc)


def load_jsonl(path):
    """각 줄을 (줄번호, 이벤트 dict | None, 입력 오류 메시지 | None) 로 반환."""
    records = []
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                records.append((n, None, f"JSON 파싱 실패 — {e}"))
                continue
            if not isinstance(obj, dict):
                records.append((n, None, f"최상위 JSON이 object가 아님 ({type(obj).__name__})"))
                continue
            records.append((n, obj, None))
    return records


def validate(records, schema, hop_cap=None):
    """검증 본체. (errors, warns, stats) 반환. 어떤 입력에도 예외를 던지지 않는다."""
    validator = build_validator(schema)
    errors, warns = [], []

    def label(ev):
        eid = ev.get("id")
        return eid if isinstance(eid, str) else "?"

    def err(n, ev, msg): errors.append(f"L{n} {label(ev)}: {msg}")
    def warn(n, ev, msg): warns.append(f"L{n} {label(ev)}: {msg}")

    valid = []          # (n, ev) 스키마 통과
    by_id = {}          # id -> (n, ev)  스키마 통과 이벤트만
    invalid_ids = {}    # id -> n        스키마 오류 이벤트의 id (문자열인 경우)
    seen_ids = {}       # id -> n        중복 검사용 (스키마 통과 여부 무관)
    last_ts = None

    # pass 1: 입력 오류 + schema + 인덱스
    for n, ev, input_error in records:
        if input_error:
            errors.append(f"L{n}: {input_error}")
            continue
        schema_errors = list(validator.iter_errors(ev))
        for e in schema_errors:
            path = "/".join(map(str, e.absolute_path)) or "<root>"
            err(n, ev, f"schema: {e.message} @ {path}")

        eid = ev.get("id")
        if isinstance(eid, str):
            if eid in seen_ids:
                err(n, ev, f"id 중복 (첫 등장 L{seen_ids[eid]})")
            else:
                seen_ids[eid] = n

        if schema_errors:
            if isinstance(eid, str):
                invalid_ids.setdefault(eid, n)
            continue

        valid.append((n, ev))
        if eid not in by_id:
            by_id[eid] = (n, ev)
        ts = datetime.fromisoformat(ev["ts"])
        if last_ts and ts < last_ts:
            warn(n, ev, f"ts 역행 ({last_ts.isoformat()} → {ts.isoformat()})")
        last_ts = ts if last_ts is None else max(last_ts, ts)

    # pass 2: 대화 규칙 (스키마 통과 이벤트만 — 필드 타입은 스키마가 보장)
    for n, ev in valid:
        if "to" not in ev:
            continue
        actor, to, act, kind = ev["actor"], ev["to"], ev["act"], ev["kind"]
        rr, hops, corr = ev["requires_reply"], ev["hops"], ev.get("corr")

        if to == actor:
            err(n, ev, "자기 전달 (to == actor)")
        if act in TERMINAL and rr is True:
            err(n, ev, f"종결형 act={act}에 requires_reply=true")
        if to == "broadcast" and rr is True:
            err(n, ev, "broadcast에 requires_reply=true")
        if act in OBLIGATING and rr is False and to != "broadcast":
            warn(n, ev, f"act={act}인데 requires_reply=false — 의도적이면 허용")
        exp = DEFAULT_ACT.get(kind)
        if exp and act != exp and kind not in ACT_WARN_EXEMPT:
            warn(n, ev, f"kind={kind} 기본 act={exp}, 실제 {act}")

        if corr is None:
            if hops != 0:
                err(n, ev, f"corr 없는데 hops={hops} (최초 발신은 0)")
        elif corr in by_id:
            src_n, src = by_id[corr]
            if src_n >= n:
                err(n, ev, f"corr {corr} 가 뒤에 오는 이벤트(L{src_n})를 참조 — 원인은 선행해야 함")
            if src.get("act") in TERMINAL:
                err(n, ev, f"종결형 이벤트 {corr}(act={src.get('act')})에 답신")
            sh = src.get("hops", 0)
            if hops != sh + 1:
                err(n, ev, f"hops={hops}, 기대값 {sh + 1} (corr hops={sh})")
            if src.get("conversation") and ev.get("conversation") != src.get("conversation"):
                err(n, ev, f"conversation 불일치: {ev.get('conversation')} ≠ 원인 {src.get('conversation')}")
        elif corr in invalid_ids:
            err(n, ev, f"corr {corr} 가 스키마 오류 이벤트(L{invalid_ids[corr]})를 참조")
        else:
            err(n, ev, f"corr {corr} 가 로그에 없음")

        if hop_cap is not None and hops > hop_cap:
            warn(n, ev, f"hops={hops} > HOP_CAP={hop_cap} → 에스컬레이션 대상")

    # refuse-deadlock (스키마 통과 이벤트만)
    refusers = {}
    for n, ev in valid:
        if ev.get("act") == "refuse" and ev.get("conversation"):
            refusers.setdefault(ev["conversation"], set()).add(ev["actor"])
    for conv, who in refusers.items():
        if len(who) >= 2:
            warns.append(f"L0 {conv}: 거절 교착: {sorted(who)} 상호 refuse → 에스컬레이션 대상")

    parsed = sum(1 for _, ev, e in records if ev is not None and e is None)
    stats = {
        "lines": len(records),
        "input_errors": len(records) - parsed,
        "schema_invalid": parsed - len(valid),
        "valid": len(valid),
        "conversation": sum(1 for _, ev in valid if "to" in ev),
    }
    stats["observation"] = stats["valid"] - stats["conversation"]
    return errors, warns, stats


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    ap.add_argument("--hop-cap", type=int, default=None)
    ap.add_argument("--strict", action="store_true", help="경고도 오류로")
    a = ap.parse_args(argv)

    try:
        with open(a.schema, encoding="utf-8") as f:
            schema = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"스키마 로드 실패: {a.schema} — {e}", file=sys.stderr)
        return 2
    try:
        records = load_jsonl(a.jsonl)
    except OSError as e:
        print(f"입력 열기 실패: {a.jsonl} — {e}", file=sys.stderr)
        return 2

    errors, warns, st = validate(records, schema, hop_cap=a.hop_cap)

    print(f"입력 {st['lines']}줄 — 유효 {st['valid']}건 (대화 {st['conversation']}, 관찰 {st['observation']}), "
          f"스키마 오류 {st['schema_invalid']}건, 입력 오류 {st['input_errors']}건")
    for w in warns:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    fail = bool(errors) or (a.strict and bool(warns))
    print("결과:", "실패" if fail else "통과", f"— 오류 {len(errors)}, 경고 {len(warns)}")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
