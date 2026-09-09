"""Regression tests for tools/validate_events.py (#150 P1 — 검증기 회귀 고정).

Reproduction-first. Measured against 2caa0fd (the validator as shipped):

  echo null > n.jsonl; validate_events.py n.jsonl
    -> TypeError: argument of type 'NoneType' is not a container  (exit 0!)
  ts="not-a-timestamp"            -> 결과: 통과 (exit 0)  — format never checked
  id=["bad"] / act=[] / kind={} / hops="x"
    -> TypeError (unhashable / str-int compare) after the schema error was already
       collected, i.e. the semantic pass reused schema-invalid data.
  corr -> a later event                 -> passed (future corr not rejected)
  corr -> a schema-invalid event        -> TypeError or silent

Contract (docs/contract/event-contract-v2.1.md + #150 review 5598913943 §3):
  every malformed input MUST become a reported contract error with a documented
  exit code (0 pass / 1 error / 2 input problem), never an unhandled exception,
  and semantic checks MUST run only on schema-valid events.
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "tools" / "validate_events.py"
SCHEMA = ROOT / "docs" / "contract" / "event-v2.1.schema.json"
MOCK = ROOT / "virtual-office" / "mock" / "events-v2.1.jsonl"
FIXTURE_INVALID = ROOT / "tests" / "fixtures" / "events-v2.1-invalid-mixed.jsonl"


def _load_module():
    spec = importlib.util.spec_from_file_location("validate_events", VALIDATOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def ve():
    return _load_module()


@pytest.fixture(scope="module")
def schema():
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def mock_events():
    return [json.loads(line) for line in MOCK.read_text(encoding="utf-8").splitlines() if line.strip()]


def _records(objs):
    """Build validator records from python objects (dicts, or raw JSON strings for non-objects)."""
    recs = []
    for n, o in enumerate(objs, 1):
        if isinstance(o, str):
            parsed = json.loads(o)
            if isinstance(parsed, dict):
                recs.append((n, parsed, None))
            else:
                recs.append((n, None, f"최상위 JSON이 object가 아님 ({type(parsed).__name__})"))
        else:
            recs.append((n, o, None))
    return recs


def _run(ve, schema, objs, **kw):
    return ve.validate(_records(objs), schema, **kw)


def _base(mock_events):
    """First conversation event with `to` and without corr (L2 of the mock)."""
    for ev in mock_events:
        if "to" in ev and "corr" not in ev:
            return json.loads(json.dumps(ev))
    raise AssertionError("mock has no corr-less conversation event")


def _ev(**over):
    ev = {
        "v": "2.1", "id": "evt_20260909T120000_aa01", "ts": "2026-09-09T12:00:00+09:00",
        "workspace": "work", "actor": "ra_us", "kind": "comment", "payload": {},
    }
    ev.update(over)
    return ev


# ---------------------------------------------------------------- baseline

def test_mock_passes_with_one_deadlock_warning(ve, schema, mock_events):
    errors, warns, st = _run(ve, schema, mock_events, hop_cap=12)
    assert errors == []
    assert len(warns) == 1 and "거절 교착" in warns[0]
    assert st["valid"] == 35 and st["conversation"] == 23 and st["observation"] == 12


def test_v2_observation_event_without_to_passes(ve, schema):
    errors, warns, _ = _run(ve, schema, [_ev(v="2")])
    assert errors == [] and warns == []


# ------------------------------------------------- top-level / input errors

@pytest.mark.parametrize("raw", ["null", "[]", "17", '"str"', "true"])
def test_top_level_non_object_is_contract_error_not_exception(ve, schema, raw):
    errors, _, st = _run(ve, schema, [raw])
    assert len(errors) == 1 and "object가 아님" in errors[0]
    assert st["input_errors"] == 1 and st["valid"] == 0


def test_load_jsonl_reports_parse_error_and_non_object(ve, tmp_path):
    p = tmp_path / "in.jsonl"
    p.write_text('{"v":"2.1"\nnull\n\n{"v":"2.1","id":"x"}\n', encoding="utf-8")
    recs = ve.load_jsonl(p)
    assert [r[0] for r in recs] == [1, 2, 4]
    assert "JSON 파싱 실패" in recs[0][2]
    assert "object가 아님" in recs[1][2]
    assert recs[2][1] == {"v": "2.1", "id": "x"} and recs[2][2] is None


# ------------------------------------------------------------- ts format

@pytest.mark.parametrize("ts", ["not-a-timestamp", "2026-09-09T09:00:00", "2026-13-01T00:00:00+09:00", 17, None])
def test_bad_or_tz_less_timestamp_is_schema_error(ve, schema, ts):
    errors, _, st = _run(ve, schema, [_ev(ts=ts)])
    assert any("schema:" in e and "@ ts" in e for e in errors), errors
    assert st["schema_invalid"] == 1


@pytest.mark.parametrize("ts", ["2026-09-09T09:00:00+09:00", "2026-09-09T00:00:00Z", "2026-09-09T00:00:00.123456+00:00"])
def test_good_timestamps_pass(ve, schema, ts):
    errors, _, _ = _run(ve, schema, [_ev(ts=ts)])
    assert errors == []


# ---------------------------------------- field type safety after schema error

@pytest.mark.parametrize("field,value", [
    ("id", ["bad"]), ("id", []), ("id", None),
    ("act", []), ("act", {}),
    ("kind", {}), ("kind", []),
    ("hops", "x"), ("hops", None), ("hops", 1.5),
    ("actor", []), ("to", []), ("corr", 7), ("corr", []),
    ("requires_reply", "yes"), ("conversation", {}),
])
def test_wrong_field_type_reports_error_without_exception(ve, schema, mock_events, field, value):
    ev = _base(mock_events)
    ev[field] = value
    errors, _, st = _run(ve, schema, [ev], hop_cap=12)
    assert errors, f"{field}={value!r} produced no error"
    assert all("schema:" in e for e in errors), errors
    assert st["schema_invalid"] == 1 and st["valid"] == 0


def test_invalid_events_interleaved_with_valid_ones_report_all_and_keep_valid(ve, schema, mock_events):
    objs = list(mock_events)
    bad = [_base(mock_events) for _ in range(4)]
    bad[0]["id"] = ["bad"]
    bad[1]["act"] = []
    bad[2]["kind"] = {}
    bad[3]["hops"] = "x"
    for i, b in enumerate(bad):
        objs.insert(3 + i * 7, b)
    objs.insert(10, "null")
    errors, warns, st = _run(ve, schema, objs, hop_cap=12)
    assert st["valid"] == 35 and st["schema_invalid"] == 4 and st["input_errors"] == 1
    assert len([e for e in errors if "schema:" in e]) >= 4
    assert len([e for e in errors if "object가 아님" in e]) == 1
    assert len(warns) == 1  # deadlock warning from the mock still detected


# ------------------------------------------------------------- corr / hops

def _thread(mock_events):
    src = _base(mock_events)  # ra_case -> ra_us, propose, hops 0, conv conv_1042_matching
    reply = _ev(id="evt_20260909T120100_aa02", ts="2026-09-09T12:01:00+09:00", actor="ra_us",
                kind="comment", to="ra_case", act="agree", requires_reply=False, hops=1,
                conversation=src["conversation"], corr=src["id"])
    return src, reply


def test_valid_reply_chain_passes(ve, schema, mock_events):
    src, reply = _thread(mock_events)
    errors, _, _ = _run(ve, schema, [src, reply])
    assert errors == []


def test_unknown_corr_is_error(ve, schema, mock_events):
    _, reply = _thread(mock_events)
    reply["corr"] = "evt_20260909T000000_dead"
    errors, _, _ = _run(ve, schema, [reply])
    assert any("로그에 없음" in e for e in errors), errors


def test_future_corr_is_error(ve, schema, mock_events):
    src, reply = _thread(mock_events)
    errors, _, _ = _run(ve, schema, [reply, src])
    assert any("뒤에 오는 이벤트" in e for e in errors), errors


def test_corr_to_schema_invalid_source_is_reported_not_crashed(ve, schema, mock_events):
    src, reply = _thread(mock_events)
    src["hops"] = "x"
    errors, _, _ = _run(ve, schema, [src, reply])
    assert any("스키마 오류 이벤트" in e and "참조" in e for e in errors), errors


def test_reply_to_terminal_event_is_error(ve, schema, mock_events):
    src, reply = _thread(mock_events)
    src["act"], src["requires_reply"] = "inform", False
    errors, _, _ = _run(ve, schema, [src, reply])
    assert any("종결형 이벤트" in e for e in errors), errors


def test_wrong_hops_and_conversation_are_errors(ve, schema, mock_events):
    src, reply = _thread(mock_events)
    reply["hops"], reply["conversation"] = 5, "conv_other"
    errors, _, _ = _run(ve, schema, [src, reply])
    assert any("hops=5, 기대값 1" in e for e in errors), errors
    assert any("conversation 불일치" in e for e in errors), errors


def test_hops_without_corr_must_be_zero(ve, schema, mock_events):
    ev = _base(mock_events)
    ev["hops"] = 3
    errors, _, _ = _run(ve, schema, [ev])
    assert any("corr 없는데 hops=3" in e for e in errors), errors


def test_hop_cap_is_warning_and_strict_makes_it_fail(ve, schema, mock_events, tmp_path):
    # a legal 14-event thread: hops 0..13, each reply corr -> previous event
    chain = [_base(mock_events)]
    for i in range(1, 14):
        prev = chain[-1]
        nxt = _ev(id=f"evt_20260909T12{i:02d}00_aa{i:02x}", ts=f"2026-09-09T12:{i:02d}:00+09:00",
                  actor="ra_us" if i % 2 else "ra_case", to="ra_case" if i % 2 else "ra_us",
                  kind="comment", act="query", requires_reply=True, hops=i,
                  conversation=prev["conversation"], corr=prev["id"])
        chain.append(nxt)
    errors, warns, _ = _run(ve, schema, chain, hop_cap=12)
    assert errors == []
    assert any("HOP_CAP=12" in w for w in warns), warns
    p = tmp_path / "chain.jsonl"
    p.write_text("\n".join(json.dumps(e) for e in chain), encoding="utf-8")
    assert ve.main([str(p), "--hop-cap", "12"]) == 0
    assert ve.main([str(p), "--hop-cap", "12", "--strict"]) == 1


# ------------------------------------------------------ conversation rules

def test_self_send_terminal_reply_and_broadcast_reply_flags(ve, schema, mock_events):
    a = _base(mock_events)
    a["to"] = a["actor"]
    b = _base(mock_events)
    b.update(id="evt_20260909T120000_bb01", act="inform", requires_reply=True)
    c = _base(mock_events)
    c.update(id="evt_20260909T120000_cc01", to="broadcast", requires_reply=True)
    errors, _, _ = _run(ve, schema, [a, b, c])
    assert any("자기 전달" in e for e in errors)
    # b and c also violate the schema (const false) — reported as schema errors, never as a crash
    assert any("L2" in e for e in errors) and any("L3" in e for e in errors)


def test_duplicate_id_is_error(ve, schema):
    errors, _, _ = _run(ve, schema, [_ev(), _ev(ts="2026-09-09T12:00:01+09:00")])
    assert any("id 중복" in e for e in errors), errors


def test_ts_regression_is_warning_only(ve, schema):
    a = _ev()
    b = _ev(id="evt_20260909T120000_aa02", ts="2026-09-09T11:00:00+09:00")
    errors, warns, _ = _run(ve, schema, [a, b])
    assert errors == [] and any("ts 역행" in w for w in warns)


# ------------------------------------------------------------ CLI / exit

def _cli(*args):
    return subprocess.run([sys.executable, str(VALIDATOR), *args], capture_output=True, text=True)


def test_cli_exit_codes_0_1_2(tmp_path):
    assert _cli(str(MOCK), "--hop-cap", "12").returncode == 0
    bad = tmp_path / "bad.jsonl"
    bad.write_text("null\n", encoding="utf-8")
    r = _cli(str(bad))
    assert r.returncode == 1 and "Traceback" not in r.stderr and "object가 아님" in r.stdout
    assert _cli(str(tmp_path / "missing.jsonl")).returncode == 2
    assert _cli(str(MOCK), "--schema", str(tmp_path / "missing.json")).returncode == 2


def test_static_invalid_fixture_reports_expected_errors():
    r = _cli(str(FIXTURE_INVALID), "--hop-cap", "12")
    assert r.returncode == 1 and "Traceback" not in r.stderr
    last = [line for line in r.stdout.splitlines() if line.startswith("결과:")][-1]
    # 3 input errors + 5 schema errors + 1 semantic error (unknown corr) -> 9 error lines;
    # 2 lines are schema-valid (L9 fails semantically, L10 is clean)
    assert "유효 2건" in r.stdout and "스키마 오류 5건" in r.stdout and "입력 오류 3건" in r.stdout
    assert int(last.split("오류 ")[1].split(",")[0]) == 9
