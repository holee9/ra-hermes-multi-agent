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
import json
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


def test_route_hint_accepts_label_format():  # US/EU/KR label (doc format) accepted
    assert m.normalize_region_hint("US") == "ra_us"
    assert m.normalize_region_hint("kr") == "ra_kr"
    actor, yellow = m.route_advisory_region("일반 사안", "EU")
    assert actor == "ra_eu" and yellow is None


def test_route_hint_accepts_actor_format():  # ra_us/ra_eu/ra_kr also accepted
    actor, yellow = m.route_advisory_region("일반 사안", "ra_us")
    assert actor == "ra_us" and yellow is None


def test_route_hint_invalid_is_ignored():
    assert m.normalize_region_hint("XX") is None
    actor, yellow = m.route_advisory_region("FDA 사안", "XX")
    assert actor == "ra_us"  # invalid hint ignored, keyword still routes


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


# ── #109: summary must come from body analysis, not Subject; ≤100 chars ────
def test_build_advisory_context_summary_body_analysis_guard():
    ctx = m.build_advisory_context("query 본문", "ra_us", "US", [], None, None)
    assert "Subject:" in ctx                 # explicit subject-copy prohibition present
    assert "본문" in ctx and "분석" in ctx    # body-analysis requirement stated
    assert "100자" in ctx                      # length guard present (255 is raspi5p safety net)


# ── REQ-AC-002b: learning history injection (a) ────────────────────────────
def test_build_advisory_context_with_learning_history():
    lh = (
        "## 담당자 최근 학습 이력 (Honcho)\n"
        "최근 본인이 학습한 RA 주제 (최근 순):\n"
        "- 2026-07-07: MFDS classification and licensing route"
    )
    ctx = m.build_advisory_context(
        "최근 학습 정리", "ra_kr", "KR", [], None, None, learning_history=lh
    )
    assert "담당자 최근 학습 이력" in ctx
    assert "MFDS classification and licensing route" in ctx


def test_build_advisory_context_learning_history_default_omitted():
    # When learning_history is None, the section header must NOT appear.
    ctx = m.build_advisory_context("query", "ra_us", "US", [], None, None)
    assert "담당자 최근 학습 이력" not in ctx


def test_fetch_learning_history_rejects_non_actor():
    # Hyphen profile id / unknown actor must return "" (peer-id safety invariant).
    assert m._fetch_learning_history("ra-us") == ""
    assert m._fetch_learning_history("unknown") == ""


# ── #105 fix: direct LLM call (no agentic tool-loop) ───────────────────────
def test_load_soul_missing_profile_is_empty():
    assert m._load_soul("does-not-exist-zzz") == ""
    assert isinstance(m._load_soul("ra-kr"), str)  # type check (content if profiles dir present)


def test_invoke_llm_direct_returns_content(monkeypatch):
    """#105: direct ollama completion — builds /v1/chat/completions, returns content."""
    captured = {}

    class _FakeResp:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            pass

        def read(self):
            return b'{"choices":[{"message":{"content":"payload"}}]}'

    def _fake_urlopen(req, timeout=None):
        captured["url"] = req.full_url
        captured["body"] = req.data.decode("utf-8")
        return _FakeResp()

    monkeypatch.setattr(m.urllib.request, "urlopen", _fake_urlopen)
    out, err = m._invoke_llm_direct("ra-kr", "advisory context")
    assert err == ""
    assert out == "payload"
    assert "/v1/chat/completions" in captured["url"]
    assert "system" in captured["body"]  # persona + user turn


def test_invoke_llm_direct_error_is_safe(monkeypatch):
    """On endpoint failure, returns ('', error) → advisory collapses to Yellow."""
    def _boom(req, timeout=None):
        raise OSError("connection refused")
    monkeypatch.setattr(m.urllib.request, "urlopen", _boom)
    out, err = m._invoke_llm_direct("ra-kr", "ctx")
    assert out == ""
    assert "llm_direct error" in err


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


# ── #118 part B: unverified-identifier cross-check ────────────────────────
def test_validate_cites_identifier_present_in_shown_text_ok():
    shown = "github:holee9/ra-project/foo.md K213497 predicate 510(k) clearance"
    adv, yellow = m.validate_advisory(
        {"confidence": 0.8, "evidence": ["github:holee9/ra-project/foo.md"],
         "recommended_comment": "predicate K213497 확인됨"},
        "ra_us", shown,
    )
    assert yellow is None


def test_validate_fabricated_identifier_not_in_shown_text_is_yellow():
    shown = "github:holee9/ra-project/foo.md some unrelated excerpt text"
    _, yellow = m.validate_advisory(
        {"confidence": 0.8, "evidence": ["github:holee9/ra-project (source K123456)"],
         "recommended_comment": ""},
        "ra_us", shown,
    )
    assert yellow == "unverified_identifier"


def test_validate_identifier_check_skipped_when_shown_text_empty():
    # Backward compatibility: omitting shown_source_text (or passing "") must
    # not trigger the new check — existing callers/tests are unaffected.
    adv, yellow = m.validate_advisory(
        {"confidence": 0.8, "evidence": ["a.md#s"], "recommended_comment": "K123456 인용"},
        "ra_us",
    )
    assert yellow is None


def test_validate_identifier_check_hyphen_space_insensitive_match():
    # A real identifier embedded in a source path/excerpt with different
    # spacing/hyphenation than the model's citation must still verify.
    shown = "path/★ FDA 510(k) - K252912/참고자료"
    adv, yellow = m.validate_advisory(
        {"confidence": 0.8, "evidence": ["a.md#s"], "recommended_comment": "predicate K252912"},
        "ra_us", shown,
    )
    assert yellow is None


def test_shown_source_text_includes_all_wiki_sub_sources():
    # Boundary check: _shown_source_text must aggregate every wiki_results
    # sub-key that _add_wiki_context renders into the prompt (llm_wiki,
    # openfda, law_kr) — a real citation from any of these must verify.
    rag_results = [{"source_file": "github:holee9/ra-project/a.md", "text": "predicate context"}]
    wiki_results = {
        "llm_wiki": [{"path": "wiki/concepts/x.md", "excerpt": "concept excerpt K999999"}],
        "openfda": [{"k_number": "K888888", "product_code": "ABC", "device_name": "Widget"}],
        "law_kr": [{"summary": "국내 규정 요약"}],
    }
    shown = m._shown_source_text(rag_results, wiki_results)
    for expected in ("predicate context", "K999999", "K888888", "Widget", "국내 규정 요약"):
        assert expected in shown

    for identifier in ("K999999", "K888888"):
        _, yellow = m.validate_advisory(
            {"confidence": 0.8, "evidence": ["a.md"], "recommended_comment": f"predicate {identifier}"},
            "ra_us", shown,
        )
        assert yellow is None, f"{identifier} should verify against wiki_results-derived shown text"


# ── #118 follow-up: per-identifier forensic status + request logging ──────
def test_cited_identifier_status_reports_per_token_verification():
    shown = "some/path.md K111111 unrelated text"
    adv = {"recommended_comment": "predicate K111111 확인, 추가로 K222222도 검토", "evidence": [], "summary": ""}
    status = m._cited_identifier_status(adv, shown)
    assert status == {"K111111": True, "K222222": False}


def test_cited_identifier_status_empty_when_no_identifiers_cited():
    adv = {"recommended_comment": "no identifiers mentioned here", "evidence": [], "summary": ""}
    assert m._cited_identifier_status(adv, "any shown text") == {}


def test_log_adv_request_includes_cited_identifier_status_when_present(monkeypatch):
    captured = {}
    monkeypatch.setattr(m._adv_request_logger, "info", lambda msg: captured.setdefault("line", msg))
    m._log_adv_request("adv-1", "query", None, {"actor": "ra_us"}, {"K111111": True, "K222222": False})
    payload = json.loads(captured["line"])
    assert payload["cited_identifier_status"] == {"K111111": True, "K222222": False}


def test_log_adv_request_omits_cited_identifier_status_when_absent(monkeypatch):
    captured = {}
    monkeypatch.setattr(m._adv_request_logger, "info", lambda msg: captured.setdefault("line", msg))
    m._log_adv_request("adv-2", "query", None, {"actor": "ra_us"})
    payload = json.loads(captured["line"])
    assert "cited_identifier_status" not in payload


# ── peer-id invariant (#83 item 6: no wrong/hyphen peer id) ───────────────
def test_yellow_advisory_actor_is_safe():
    ya = m._yellow_advisory("multi_region", None)
    assert ya["decision"] == "yellow_review"
    assert ya["actor"] in ("system", "ra_us", "ra_eu", "ra_kr")
    assert "-" not in ya["actor"]
    assert ya["confidence"] == 0.0


def test_yellow_unclear_region_label_not_kr():  # #88/#77: unclear yellow -> region "unclear", not fallback actor's "KR"
    ya = m._yellow_advisory("unclear_region", None)
    assert ya["yellow_reason"] == "unclear_region"
    assert ya["decision"] == "yellow_review"
    assert ya["region"] == "unclear"
    assert ya["actor"] == "ra_kr"  # safe fallback actor unchanged (Honcho routing intact)


def test_yellow_multi_region_label():
    ya = m._yellow_advisory("multi_region", None)
    assert ya["region"] == "multi_region"


def test_yellow_low_confidence_keeps_routed_region():  # confidence/evidence yellow keeps the routed actor's real region
    ya = m._yellow_advisory("low_confidence", "ra_eu")
    assert ya["region"] == "EU"
    assert ya["actor"] == "ra_eu"


def test_actor_profile_map_uses_hyphen_only_internally():
    # externally-exposed actor -> internal hermes profile (hyphen dir name)
    assert m.ADVISORY_ACTOR_PROFILE == {"ra_us": "ra-us", "ra_eu": "ra-eu", "ra_kr": "ra-kr"}
    assert set(m.ADVISORY_ACTOR_PROFILE) == {"ra_us", "ra_eu", "ra_kr"}
