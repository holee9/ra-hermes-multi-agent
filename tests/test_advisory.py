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


# ── #134 C1: structural regulatory-citation gate ──────────────────────────

def test_validate_nonexistent_article_subpoint_is_yellow():
    # Art.86(1) has (a)(b)(c) only — a cited (d) cannot exist and downgrades
    # to yellow_review (tier C1 hard gate).
    _, yellow = m.validate_advisory(
        {"confidence": 0.9, "evidence": ["ra-project/psur.md"],
         "recommended_comment": "PMCF 결과는 Art.86(1)(d)에 기재합니다."},
        "ra_eu",
    )
    assert yellow == "citation_error"


def test_validate_existing_article_subpoint_ok():
    # Art.86(1)(c) is real — must not gate.
    _, yellow = m.validate_advisory(
        {"confidence": 0.9, "evidence": ["ra-project/psur.md"],
         "recommended_comment": "판매량은 Art.86(1)(c)에 기재합니다."},
        "ra_eu",
    )
    assert yellow is None


def test_validate_citation_gate_does_not_fire_on_semantic_c2():
    # C2 (subject<->citation mismatch, e.g. SSCP->Art.66) is NOT shipped/gated —
    # only the structural C1 tier gates. A prose SSCP/Art.66 mismatch must pass
    # the live gate (it is left to persona + human review).
    _, yellow = m.validate_advisory(
        {"confidence": 0.9, "evidence": ["ra-project/sscp.md"],
         "recommended_comment": "The SSCP is prepared per Art. 66."},
        "ra_eu",
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


# ── #137 content-emptiness gate ───────────────────────────────────────────
@pytest.mark.parametrize("query", [
    "Subject: \nFrom: \nAttachments:",          # the raspi5p hourly phantom body
    "Subject:\nFrom:\nAttachments:",            # no trailing spaces
    "제목: \n보낸사람: \n첨부:",                  # Korean header labels
    "테스트",
    "hello",
])
def test_empty_content_rejected(query):
    assert m.has_substantive_content(query) is False


@pytest.mark.parametrize("query", [
    # the subject IS the matter — stripping whole header lines would mis-reject this
    "Subject: FW: FW: AZTEC & H&abyz : Registration in Thailand\nFrom: sales@axtech.co.th\nAttachments:",
    "문서 검토 필요합니다",                       # 11 chars: real advisory in production logs
    "EU MDR Annex II 기술문서 구성 항목 확인 부탁드립니다",
    "FDA 510(k) submission basics",
])
def test_substantive_content_accepted(query):
    assert m.has_substantive_content(query) is True


def test_header_labels_stripped_values_kept():
    # values survive the label strip, so a header-only mail with a real subject passes
    assert m.has_substantive_content("Subject: MFDS 2등급 인허가 절차") is True
    # ...while a header skeleton with empty values does not
    assert m.has_substantive_content("Subject:\nFrom:") is False


# ── #138 routing-rejection dedup ──────────────────────────────────────────
def test_dedup_suppresses_repeat_routing_rejection():
    m._dedup_seen.clear()
    q = "오늘 날씨가 좋습니다 일반적인 안부 인사입니다"
    assert m.is_duplicate_rejection(q) is False
    m.mark_rejected(q, "unclear_region")
    assert m.is_duplicate_rejection(q) is True


@pytest.mark.parametrize("reason", [
    "parse_or_hermes_failure",   # a retry must be able to reach the LLM again
    "low_confidence",            # observed conf 0.0 -> 0.78 on re-submission
    "no_evidence",
    None,                        # successful advisory is never cached
])
def test_dedup_preserves_retry_for_non_routing_outcomes(reason):
    m._dedup_seen.clear()
    q = "eSTAR Labeling IFU Form 3881 predicate device 확인"
    m.mark_rejected(q, reason)
    assert m.is_duplicate_rejection(q) is False


def test_dedup_scoped_to_identical_body():
    m._dedup_seen.clear()
    m.mark_rejected("사내 품질문서 통합관리 절차 검토", "unclear_region")
    assert m.is_duplicate_rejection("전혀 다른 사안에 대한 자문 요청입니다") is False


def test_dedup_key_ignores_header_labels():
    a = "Subject: EU MDR Annex II 검토\nFrom: x@y.com"
    b = "EU MDR Annex II 검토\nx@y.com"
    assert m._dedup_key(a) == m._dedup_key(b)


def test_dedup_disabled_when_window_zero(monkeypatch):
    m._dedup_seen.clear()
    monkeypatch.setattr(m, "ADVISORY_DEDUP_WINDOW", 0)
    q = "MFDS 의료기기 1등급 기준 확인"
    m.mark_rejected(q, "unclear_region")
    assert m.is_duplicate_rejection(q) is False


# ── #138 review: dedup key must include routing context ───────────────────
def test_dedup_allows_requery_with_added_region_hint():
    m._dedup_seen.clear()
    q = "Subject: 의료기기 허가 문의\n제품 등록 서류 안내 요청"
    m.mark_rejected(q, "unclear_region")                      # first attempt: no hint
    assert m.is_duplicate_rejection(q) is True                  # bare retry still suppressed
    assert m.is_duplicate_rejection(q, "KR") is False           # corrected re-ask is new
    assert m.is_duplicate_rejection(q, None, 1042) is False     # WP context is new too


def test_dedup_key_normalizes_hint_and_ignores_empty_wp():
    assert m._dedup_key("q", "kr") == m._dedup_key("q", "KR")
    assert m._dedup_key("q", None, None) == m._dedup_key("q", "", "")
    assert m._dedup_key("q", "KR") != m._dedup_key("q", "US")


def test_dedup_same_hint_repeat_is_still_suppressed():
    m._dedup_seen.clear()
    q = "일반 안부 인사 메일입니다"
    m.mark_rejected(q, "unclear_region", "KR", 7)
    assert m.is_duplicate_rejection(q, "kr", 7) is True


_UUID_REF = __import__("re").compile(r"^adv-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")


def _post_advisory(monkeypatch, query, **body):
    """Call the real endpoint through Flask's test client with side effects stubbed:
    no Honcho write, no KB-gap write, no LLM — the request log call is captured instead."""
    captured = []
    monkeypatch.setattr(m, "API_KEY", "test-key")
    monkeypatch.setattr(m, "_honcho_record", lambda *a, **k: None)
    monkeypatch.setattr(m, "_log_kb_gap", lambda *a, **k: None)
    monkeypatch.setattr(m, "_log_adv_request", lambda ref, q, hint, adv, *a, **k: captured.append((ref, q, hint, adv)))
    # Force the routing-rejection (Yellow) path so no Hermes/LLM subprocess is ever spawned.
    monkeypatch.setattr(m, "route_advisory_region", lambda q, h: (None, "unclear_region"))
    m._dedup_seen.clear()
    client = m.app.test_client()
    resp = client.post("/v1/ra/advisory", json={"query": query, **body},
                       headers={"Authorization": "Bearer test-key"})
    return resp, captured


def test_request_ref_is_uuid_and_matches_response_and_log(monkeypatch):
    """#141 (codex review): the ref must come from a large ID space AND the value the caller
    receives must be the same one written to the request log (join-key integrity)."""
    q = "오늘 날씨가 좋습니다 일반적인 안부 인사 메일입니다"      # no region keyword → yellow, no LLM
    resp, captured = _post_advisory(monkeypatch, q)
    assert resp.status_code == 200
    ref = resp.get_json()["request_ref"]
    assert _UUID_REF.match(ref), ref
    assert len(captured) == 1 and captured[0][0] == ref and captured[0][3]["request_ref"] == ref


def test_request_refs_differ_across_requests_in_same_second(monkeypatch):
    q = "사내 품질문서 통합관리 절차 검토 요청입니다"
    refs = set()
    for i in range(5):
        m._dedup_seen.clear()
        resp, _ = _post_advisory(monkeypatch, q + f" ({i})")
        refs.add(resp.get_json()["request_ref"])
    assert len(refs) == 5


def test_duplicate_rejected_path_returns_400_with_code(monkeypatch):
    q = "오늘 날씨가 좋습니다 일반적인 안부 인사 메일입니다"
    resp1, _ = _post_advisory(monkeypatch, q)
    assert resp1.status_code == 200 and resp1.get_json()["yellow_reason"] == "unclear_region"
    client = m.app.test_client()
    resp2 = client.post("/v1/ra/advisory", json={"query": q}, headers={"Authorization": "Bearer test-key"})
    assert resp2.status_code == 400 and resp2.get_json()["code"] == "duplicate_rejected"
    resp3 = client.post("/v1/ra/advisory", json={"query": q, "region_hint": "KR"},
                        headers={"Authorization": "Bearer test-key"})
    assert resp3.status_code != 400 or resp3.get_json().get("code") != "duplicate_rejected"


# ── #150 codex 재현: chat-completions 가 subprocess 비정상 종료를 정상 completion 으로 반환 ──────────
class _Proc:
    def __init__(self, rc, out, err=""):
        self.returncode, self.stdout, self.stderr = rc, out, err


def _chat_client(monkeypatch, proc):
    monkeypatch.setattr(m, "API_KEY", "test-key")
    monkeypatch.setattr(m, "_run_rag_search", lambda q, top=5: [])
    monkeypatch.setattr(m, "_run_knowledge_fetch", lambda q, p, top=3: [])
    monkeypatch.setattr(m.subprocess, "run", lambda *a, **k: proc)
    return m.app.test_client()


def test_chat_completion_nonzero_exit_with_partial_stdout_is_failure(monkeypatch):
    client = _chat_client(monkeypatch, _Proc(1, "partial stdout before failure", "boom"))
    r = client.post("/v1/chat/completions", json={"model": "hermes-ra", "messages": [{"role": "user", "content": "hi"}]},
                    headers={"Authorization": "Bearer test-key"})
    assert r.status_code == 200
    content = json.loads(r.get_json()["choices"][0]["message"]["content"])
    wp = content["wp_comment"]
    assert "hermes_failed" in wp["flags"] and wp["confidence"] == 0.0
    assert "hermes exit 1" in wp["recommendation"]
    body = json.dumps(content)
    assert "partial stdout" not in body and "boom" not in body                 # 원문 stderr/stdout 외부 미노출


def test_chat_completion_zero_exit_keeps_stdout(monkeypatch):
    client = _chat_client(monkeypatch, _Proc(0, "plain answer"))
    r = client.post("/v1/chat/completions", json={"model": "hermes-ra", "messages": [{"role": "user", "content": "hi"}]},
                    headers={"Authorization": "Bearer test-key"})
    assert r.get_json()["choices"][0]["message"]["content"] == "plain answer"


def test_invoke_hermes_nonzero_exit_reports_error(monkeypatch):
    monkeypatch.setattr(m.subprocess, "run", lambda *a, **k: _Proc(2, "partial", ""))
    out, err = m._invoke_hermes("ra-us", "ctx")
    assert out == "" and err == "hermes exit 2"                                # 원문 미포함


def test_nonzero_exit_diagnostic_goes_to_server_log_only(monkeypatch, caplog):
    import logging
    monkeypatch.setattr(m.subprocess, "run", lambda *a, **k: _Proc(3, "partial", "secret-trace"))
    with caplog.at_level(logging.WARNING, logger="hermes.subprocess"):
        out, err = m._invoke_hermes("ra-us", "ctx")
    assert "exit 3" in caplog.text and "ra-us" in caplog.text                  # 메타데이터만 (profile·코드·길이)
    assert "secret-trace" not in caplog.text and "secret-trace" not in err      # 원문은 로그에도 남기지 않음


# ── #150 P3-0 (세션 모델 A): HIVE 수락 계약 endpoint ──────────────────────────────────
def _hive_client(monkeypatch, run=None, ledger_path=""):
    monkeypatch.setattr(m, "API_KEY", "test-key")
    monkeypatch.setattr(m, "HIVE_LEDGER_PATH", ledger_path)
    m._hive_ledger.clear()
    m._profile_busy.clear()
    if run is not None:
        monkeypatch.setattr(m.subprocess, "run", run)
    return m.app.test_client()


H = {"Authorization": "Bearer test-key"}


def test_hive_state_idle_then_busy_during_subprocess(monkeypatch):
    seen = {}

    def run(*a, **k):
        seen["state_during"] = m._hive_state_for("ra_us")["value"]
        return _Proc(0, "ok")
    client = _hive_client(monkeypatch, run)
    st = client.get("/v1/hive/state/ra_us", headers=H).get_json()
    assert st["value"] == "idle" and st["scope"] == "this-api-process-only" and st["generation"] == m.HIVE_GENERATION
    assert st["observed_at"].endswith("+00:00")                                  # tz 있는 시각 (drain _normalize 요구)
    m._invoke_hermes("ra-us", "ctx")
    assert seen["state_during"] == "busy"
    assert client.get("/v1/hive/state/ra_us", headers=H).get_json()["value"] == "idle"   # 슬롯 해제
    assert client.get("/v1/hive/state/ra_kr", headers=H).status_code == 404          # 파일럿 2 peer 한정
    assert client.get("/v1/hive/state/ra_us").status_code == 401


def test_hive_submit_accepts_runs_and_records_ledger(monkeypatch):
    calls = []

    def run(cmd, **k):
        calls.append(cmd)
        return _Proc(0, "answer")
    client = _hive_client(monkeypatch, run)
    body = {"actor": "ra_eu", "msg_id": "evt_1", "payload": {"id": "evt_1", "kind": "handoff", "payload": {"x": 1}}}
    r = client.post("/v1/hive/submit", json=body, headers=H)
    assert r.status_code == 200
    j = r.get_json()
    assert j["result"] == "accepted" and j["status"] == "completed" and j["output"] == "answer"
    assert calls[0][1:3] == ["-p", "ra-eu"] and json.loads(calls[0][4]) == body["payload"]  # 문맥 = payload 만
    lk = client.get("/v1/hive/lookup/evt_1", headers=H).get_json()
    assert lk["known"] is True and lk["status"] == "completed" and lk["generation"] == m.HIVE_GENERATION
    assert client.get("/v1/hive/lookup/evt_nope", headers=H).status_code == 404


def test_hive_submit_duplicate_msg_id_is_idempotent(monkeypatch):
    calls = []
    client = _hive_client(monkeypatch, lambda cmd, **k: calls.append(cmd) or _Proc(0, "a"))
    body = {"actor": "ra_us", "msg_id": "evt_2", "payload": {"id": "evt_2"}}
    client.post("/v1/hive/submit", json=body, headers=H)
    r = client.post("/v1/hive/submit", json=body, headers=H)
    assert r.get_json()["result"] == "duplicate" and r.get_json()["status"] == "completed" and len(calls) == 1


def test_hive_submit_rejects_when_profile_busy(monkeypatch):
    client = _hive_client(monkeypatch)
    m._profile_busy["ra-us"] = 1                                                   # 다른 요청이 점유 중
    r = client.post("/v1/hive/submit", json={"actor": "ra_us", "msg_id": "evt_3", "payload": {"id": "evt_3"}}, headers=H)
    assert r.status_code == 409 and r.get_json()["result"] == "reject-busy"
    assert client.get("/v1/hive/lookup/evt_3", headers=H).status_code == 404       # 거절은 원장에 남지 않음


def test_hive_submit_failed_subprocess_is_recorded_not_completed(monkeypatch):
    client = _hive_client(monkeypatch, lambda cmd, **k: _Proc(1, "partial", "err"))
    r = client.post("/v1/hive/submit", json={"actor": "ra_us", "msg_id": "evt_4", "payload": {"id": "evt_4"}}, headers=H)
    j = r.get_json()
    assert j["status"] == "failed" and j["error"] == "hermes exit 1" and j["output"] == ""
    assert client.get("/v1/hive/state/ra_us", headers=H).get_json()["value"] == "idle"   # 실패 후 점유 해제


@pytest.mark.parametrize("body,code", [
    ({"actor": "ra_kr", "msg_id": "evt_5", "payload": {"id": "evt_5"}}, 400),
    ({"actor": "ra_us", "msg_id": "nope", "payload": {"id": "nope"}}, 400),
    ({"actor": "ra_us", "msg_id": "evt_6", "payload": {"id": "evt_other"}}, 400),
    ({"actor": "ra_us", "msg_id": "evt_7", "payload": "text"}, 400),
])
def test_hive_submit_validation(monkeypatch, body, code):
    client = _hive_client(monkeypatch)
    assert client.post("/v1/hive/submit", json=body, headers=H).status_code == code


def test_hive_ledger_persists_and_survives_restart(monkeypatch, tmp_path):
    path = str(tmp_path / "ledger.jsonl")
    client = _hive_client(monkeypatch, lambda cmd, **k: _Proc(0, "a"), ledger_path=path)
    client.post("/v1/hive/submit", json={"actor": "ra_us", "msg_id": "evt_8", "payload": {"id": "evt_8"}}, headers=H)
    lines = [json.loads(x) for x in open(path, encoding="utf-8")]
    assert [x["status"] for x in lines] == ["accepted", "completed"]              # accept 가 실행보다 먼저 영속
    m._hive_ledger.clear()                                                        # 재시작 흉내
    lk = client.get("/v1/hive/lookup/evt_8", headers=H).get_json()
    assert lk["known"] is True and lk["status"] == "completed"
