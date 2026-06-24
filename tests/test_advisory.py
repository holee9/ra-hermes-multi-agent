"""Unit tests for the RA advisory pipeline (scripts/hermes-api-server.py).

Covers #83 verification items that are deterministic (no live Hermes/GX10 needed):
  - server-side keyword routing (single / multi / unclear / hint / hint-conflict)
  - advisory JSON parsing from free-form LLM prose
  - contract validation (actor forced to underscore, confidence range,
    high-confidence requires evidence, invalid -> Yellow)
  - Yellow advisory shape (safe actor, non-executable)
  - peer-id invariant: a hyphen peer id (ra-us) can never leak into responses
"""
import importlib.util
from pathlib import Path

import pytest

_SERVER = Path(__file__).resolve().parent.parent / "scripts" / "hermes-api-server.py"


def _load():
    spec = importlib.util.spec_from_file_location("hermes_api_server", _SERVER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = _load()


# ── routing (#83 item 3: multi-region -> Yellow) ──────────────────────────
@pytest.mark.parametrize("query,expected_actor", [
    ("FDA 510(k) submission for a new device", "ra_us"),
    ("MDR CE 기술문서 갱신", "ra_eu"),
    ("식약처 허가 신청합니다", "ra_kr"),
    ("EUDAMED 등록 관련", "ra_eu"),
    ("KGMP 품질관리", "ra_kr"),
])
def test_route_single_region(query, expected_actor):
    actor, yellow = m.route_advisory_region(query, None)
    assert actor == expected_actor
    assert yellow is None


def test_route_multi_region_is_yellow():
    actor, yellow = m.route_advisory_region("MDR CE 문서와 FDA 510(k) 비교", None)
    assert actor is None
    assert yellow == "multi_region"


def test_route_unclear_is_yellow():
    actor, yellow = m.route_advisory_region("오늘 날씨가 좋습니다", None)
    assert actor is None
    assert yellow == "unclear_region"


def test_route_hint_honored_without_conflict():
    actor, yellow = m.route_advisory_region("사안 내용", "ra_eu")
    assert actor == "ra_eu"
    assert yellow is None


def test_route_hint_conflict_is_yellow():
    actor, yellow = m.route_advisory_region("FDA 관련 사안", "ra_eu")
    assert actor is None
    assert yellow == "multi_region"


# ── parsing (#83 item 1/2: normal JSON returned from prose) ───────────────
def test_parse_advisory_from_prose():
    sample = (
        "설명 텍스트...\n"
        '{"actor":"ra_kr","region":"KR","confidence":0.82,"decision":"comment_existing_wp",'
        '"wp_candidate":1234,"summary":"...","recommended_comment":"...","evidence":["s.md#x"],"yellow_reason":null}\n'
        "후행 텍스트"
    )
    adv = m.parse_advisory(sample)
    assert adv is not None
    assert adv["decision"] == "comment_existing_wp"
    assert adv["wp_candidate"] == 1234


def test_parse_advisory_nested_json():
    sample = '{"decision":"x","evidence":[{"a":1}],"confidence":0.5}'
    adv = m.parse_advisory(sample)
    assert adv is not None and adv["decision"] == "x"


def test_parse_advisory_no_match():
    assert m.parse_advisory("JSON 없는 일반 텍스트") is None


# ── context build (regression: must not crash with rag_results) ───────────
def test_build_advisory_context_with_rag():
    ctx = m.build_advisory_context(
        "식약처 허가 기준 질의", "ra_kr", "KR",
        rag_results=[{"source_file": "a.md", "score": 0.9, "text": "본문"}],
        wiki_results=None, wp_context={"wp_list": "WP-1 ...", "wp_id": 1},
    )
    assert "ra_kr" in ctx and "KR" in ctx
    assert "evidence" in ctx  # output instruction present
    assert "WP-1" in ctx       # wp_list included


def test_build_advisory_context_minimal():
    ctx = m.build_advisory_context("query", "ra_us", "US", [], None, None)
    assert isinstance(ctx, str) and "decision" in ctx


# ── validation (#83 items 4/5/6: evidence/low-conf/peer-id invariants) ────
def test_validate_no_evidence_is_yellow():  # DoD item 4: evidence 없는 응답 → Yellow
    adv, yellow = m.validate_advisory({"actor": "ra-us", "confidence": 0.9, "evidence": []}, "ra_kr")
    assert yellow == "no_evidence"
    assert adv["actor"] == "ra_kr"  # actor forced to routed underscore (never trust LLM)
    assert "-" not in adv["actor"]


def test_validate_low_confidence_is_yellow():  # DoD item 5: confidence 낮은 응답 → Yellow
    _, yellow = m.validate_advisory({"confidence": 0.3, "evidence": ["a.md#s"]}, "ra_us")
    assert yellow == "low_confidence"


def test_validate_valid_advisory_ok():
    adv, yellow = m.validate_advisory({"confidence": 0.8, "evidence": ["a.md#s"]}, "ra_us")
    assert yellow is None
    assert adv["actor"] == "ra_us"
    assert adv["region"] == "US"


def test_validate_moderate_conf_with_evidence_ok():
    adv, yellow = m.validate_advisory({"confidence": 0.6, "evidence": ["b.md"]}, "ra_eu")
    assert yellow is None
    assert adv["actor"] == "ra_eu"


def test_validate_invalid_confidence_is_yellow():
    _, yellow = m.validate_advisory({"confidence": "high"}, "ra_eu")
    assert yellow == "invalid_confidence"


def test_validate_confidence_out_of_range_is_yellow():
    for bad in (1.5, -0.1, True):
        _, yellow = m.validate_advisory({"confidence": bad, "evidence": ["x"]}, "ra_us")
        assert yellow == "invalid_confidence"


# ── peer-id invariant (#83 item 6: no wrong/hyphen peer id) ───────────────
def test_yellow_advisory_actor_is_safe():
    ya = m._yellow_advisory("multi_region", None)
    assert ya["decision"] == "yellow_review"
    assert ya["actor"] in ("system", "ra_us", "ra_eu", "ra_kr")
    assert "-" not in ya["actor"]
    assert ya["confidence"] == 0.0


def test_actor_profile_map_uses_hyphen_only_internally():
    # externally-exposed actor -> internal hermes profile (hyphen dir name)
    assert m.ADVISORY_ACTOR_PROFILE == {"ra_us": "ra-us", "ra_eu": "ra-eu", "ra_kr": "ra-kr"}
    assert set(m.ADVISORY_ACTOR_PROFILE) == {"ra_us", "ra_eu", "ra_kr"}
