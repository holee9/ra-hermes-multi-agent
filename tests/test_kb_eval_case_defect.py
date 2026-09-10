"""#147 — case-generation defects are recorded and reported separately from agent errors.

Review (codex, 2026-09-09): capture_failed / source_mismatch had no structured field in
the feedback parser, correction_rate had no split, and assemble_cases back-filled a short
pool with focus-unrelated sources. Also: input defects must NOT be dropped from the
system-level quality signal — both are reported.
"""
import importlib.util
import json
import pytest
import sys
from datetime import date, datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ingest = _load("kb_eval_feedback_ingest", "kb-eval-feedback-ingest.py")
gm = _load("growth_metrics", "growth-metrics.py")
runner = _load("daily_growth_runner", "daily-growth-runner.py")
sheet = _load("kb_eval_checksheet", "kb-eval-checksheet.py")

META = ('<!-- kb_eval_case {"decision_ref":"kb-eval-20260716-it01-ra_eu-005","agent":"ra_eu",'
        '"source":"s.md","source_hash":"abc","base_date":"2026-07-16","iteration":1,'
        '"scenario_id":"sc"} -->')


def _sheet(*checked: str, note: str | None = None) -> str:
    labels = list(ingest.SCORE_LABELS) + list(ingest.DIMENSION_LABELS) + ["Human correction needed"] \
        + list(ingest.CASE_DEFECT_LABELS)
    lines = [META, "", "**Reviewer Score**", ""]
    for label in labels:
        lines.append(f"- [{'x' if label in checked else ' '}] {label}")
    if note:
        lines += ["", "**Optional Correction Note**", "", f"> {note}"]
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------- parser

def test_parser_records_case_defect_fields():
    text = _sheet("Score 1 - correction required", "Capture failed")
    [rec] = ingest.parse_text("sheet", text)
    assert rec["case_defect"] == {"capture_failed": True, "source_mismatch": False}
    assert rec["score"] == 1 and rec["delta"]["self_correction"] is True   # both recorded


def test_parser_source_mismatch_with_passing_score():
    text = _sheet("Score 2 - usable with minor correction", "Source mismatch (focus vs source)")
    [rec] = ingest.parse_text("sheet", text)
    assert rec["case_defect"] == {"capture_failed": False, "source_mismatch": True}


def test_parser_backward_compatible_with_sheets_lacking_defect_boxes():
    text = _sheet("Score 3 - pass / usable without correction")
    text = "\n".join(line for line in text.splitlines() if not any(k in line for k in ingest.CASE_DEFECT_LABELS))
    [rec] = ingest.parse_text("sheet", text)
    assert rec["case_defect"] is None                                         # 항목 없음 = 미평가 (결함 없음 아님)


def test_parser_explicit_unchecked_boxes_are_evaluated_not_legacy():
    text = _sheet("Score 3 - pass / usable without correction")
    [rec] = ingest.parse_text("sheet", text)
    assert rec["case_defect"] == {"capture_failed": False, "source_mismatch": False}


def test_end_to_end_legacy_sheet_counts_as_unevaluated_in_metrics():
    """codex #147: 구 시트를 새로 ingest 해도 metrics 가 '평가 완료'로 오인하지 않는다 (파서→지표 연결)."""
    legacy = _sheet("Score 3 - pass / usable without correction")
    legacy = "\n".join(line for line in legacy.splitlines() if not any(k in line for k in ingest.CASE_DEFECT_LABELS))
    new = _sheet("Score 3 - pass / usable without correction")
    recs = ingest.parse_text("legacy", legacy) + ingest.parse_text("new", new)
    since = datetime(2026, 7, 16, tzinfo=timezone.utc)
    until = datetime(2026, 7, 17, tzinfo=timezone.utc)
    msgs = {"f": [{"content": json.dumps({"ts": f"2026-07-16T0{i}:00:00+00:00", "type": "score_given",
                                          "payload": {**r, "target_actor": "ra_eu"}}),
                   "metadata": {"record_type": "score_given", "actor": "human"}, "peer_name": "ra_eu"}
                  for i, r in enumerate(recs, 1)]}
    r = gm.compute_correction_rate(msgs, since, until)
    assert r["denominator"] == 2 and r["case_defects"]["unevaluated_legacy"] == 1


def test_checksheet_template_emits_defect_boxes():
    assert sheet.checkbox("Capture failed") == "- [ ] Capture failed"
    src = (SCRIPTS / "kb-eval-checksheet.py").read_text(encoding="utf-8")
    for label in ingest.CASE_DEFECT_LABELS:
        assert f'checkbox("{label}")' in src


# ------------------------------------------------------------- correction_rate

def _score_msg(ts: str, corrected: bool, defect: dict | None = None) -> dict:
    payload = {"decision_ref": ts, "score": 1 if corrected else 3, "target_actor": "ra_eu",
               "delta": {"self_correction": corrected}}
    if defect is not None:
        payload["case_defect"] = defect
    return {"content": json.dumps({"ts": ts, "type": "score_given", "payload": payload}),
            "metadata": {"record_type": "score_given", "actor": "human"}, "peer_name": "ra_eu"}


def test_correction_rate_reports_system_and_conditional_split():
    since = datetime(2026, 7, 16, tzinfo=timezone.utc)
    until = datetime(2026, 7, 17, tzinfo=timezone.utc)
    msgs = {"feedback": [
        _score_msg("2026-07-16T01:00:00+00:00", True, {"capture_failed": True}),
        _score_msg("2026-07-16T02:00:00+00:00", True, {"source_mismatch": True}),
        _score_msg("2026-07-16T03:00:00+00:00", True),                     # genuine agent error
        _score_msg("2026-07-16T04:00:00+00:00", False),
        _score_msg("2026-07-16T05:00:00+00:00", False, {"capture_failed": False, "source_mismatch": False}),
    ]}
    r = gm.compute_correction_rate(msgs, since, until)
    assert r["denominator"] == 5 and r["numerator"] == 3 and r["value"] == 0.6   # system-level keeps all
    assert r["case_defects"] == {"count": 2, "corrected": 2, "capture_failed": 1, "source_mismatch": 1,
                                 "unevaluated_legacy": 2}                      # 3번·4번: case_defect 키 없음
    cond = r["excluding_case_defects"]
    assert (cond["value"], cond["numerator"], cond["denominator"]) == (1 / 3, 1, 3)
    assert "NOT agent attribution" in cond["meaning"] and "agent_attributable" not in r
    assert any(s.get("case_defect") == {"capture_failed": True} for s in r["samples"])


def test_correction_rate_without_defect_field_is_unchanged():
    since = datetime(2026, 7, 16, tzinfo=timezone.utc)
    until = datetime(2026, 7, 17, tzinfo=timezone.utc)
    r = gm.compute_correction_rate({"f": [_score_msg("2026-07-16T01:00:00+00:00", True)]}, since, until)
    assert r["value"] == 1.0 and r["case_defects"]["count"] == 0
    assert r["case_defects"]["unevaluated_legacy"] == 1                        # 결함 없음이 아니라 미평가
    cond = r["excluding_case_defects"]
    assert (cond["value"], cond["numerator"], cond["denominator"]) == (1.0, 1, 1)


def test_conditional_rate_does_not_claim_attribution_for_co_occurring_defects():
    """codex #147 재현: 입력 결함(source_mismatch)+교정 1건 + 정상 1건 → 전체 0.5, 조건부 0.0.
    조건부 0.0은 '입력 결함 표시 없는 사례의 교정률'이지 에이전트 무결함 판정이 아니다 — 명칭·meaning으로 고정."""
    since = datetime(2026, 7, 16, tzinfo=timezone.utc)
    until = datetime(2026, 7, 17, tzinfo=timezone.utc)
    msgs = {"f": [
        _score_msg("2026-07-16T01:00:00+00:00", True, {"source_mismatch": True}),   # 입력+출력 동시 결함 가능
        _score_msg("2026-07-16T02:00:00+00:00", False, {"capture_failed": False, "source_mismatch": False}),
    ]}
    r = gm.compute_correction_rate(msgs, since, until)
    assert r["value"] == 0.5 and r["case_defects"]["corrected"] == 1
    assert r["excluding_case_defects"]["value"] == 0.0
    assert r["case_defects"]["unevaluated_legacy"] == 0                       # 둘 다 평가 완료
    assert "attribution" in r["excluding_case_defects"]["meaning"]


def test_four_way_split_input_only_normal_and_legacy():
    since = datetime(2026, 7, 16, tzinfo=timezone.utc)
    until = datetime(2026, 7, 17, tzinfo=timezone.utc)
    msgs = {"f": [
        _score_msg("2026-07-16T01:00:00+00:00", False, {"capture_failed": True}),                    # 입력만 결함, 미교정
        _score_msg("2026-07-16T02:00:00+00:00", True, {"capture_failed": False, "source_mismatch": False}),  # 정상 평가, 교정
        _score_msg("2026-07-16T03:00:00+00:00", False),                                                # legacy 미평가
    ]}
    r = gm.compute_correction_rate(msgs, since, until)
    assert r["denominator"] == 3 and r["numerator"] == 1
    assert r["case_defects"]["count"] == 1 and r["case_defects"]["corrected"] == 0
    assert r["case_defects"]["unevaluated_legacy"] == 1
    assert r["excluding_case_defects"]["denominator"] == 2 and r["excluding_case_defects"]["numerator"] == 1


# ------------------------------------------------------------- assemble_cases floor

def _fake_chunks(conn, source_path, max_chunks):
    return [{"id": 1, "content": f"text about {source_path}", "metadata": {}}]


def test_assemble_cases_applies_relevance_floor_when_configured(monkeypatch):
    agent = runner.AGENTS["ra-eu"]
    monkeypatch.setattr(runner, "fetch_source_chunks", _fake_chunks)
    monkeypatch.setattr(runner, "GROWTH_RANK_MODE", "keyword")
    scores = {"pms.md": 4, "udi.md": -3, "psur.md": 2}
    monkeypatch.setattr(runner, "focus_relevance", lambda focus, path, text: scores[path])
    paths = ["udi.md", "pms.md", "psur.md"]

    monkeypatch.setattr(runner, "GROWTH_FOCUS_MIN_RELEVANCE", None)
    cases = runner.assemble_cases(None, agent, "PMS", paths, date(2026, 7, 17), 3, 1)
    assert [c.source_path for c in cases] == ["pms.md", "psur.md", "udi.md"]   # legacy: no floor

    monkeypatch.setattr(runner, "GROWTH_FOCUS_MIN_RELEVANCE", 0)
    cases = runner.assemble_cases(None, agent, "PMS", paths, date(2026, 7, 17), 3, 1)
    assert [c.source_path for c in cases] == ["pms.md", "psur.md"]           # off-topic dropped


def test_assemble_cases_floor_ignored_in_vector_mode(monkeypatch):
    agent = runner.AGENTS["ra-eu"]
    monkeypatch.setattr(runner, "fetch_source_chunks", _fake_chunks)
    monkeypatch.setattr(runner, "GROWTH_RANK_MODE", "vector")
    monkeypatch.setattr(runner, "rank_paths_by_focus_vector", lambda conn, focus, pool: None)
    monkeypatch.setattr(runner, "GROWTH_FOCUS_MIN_RELEVANCE", 5)
    cases = runner.assemble_cases(None, agent, "PMS", ["a.md", "b.md"], date(2026, 7, 17), 2, 1)
    assert len(cases) == 2


# ── #147 DoD 4: focus 의미와 어긋나는 source 가 선택되는 경로 점검 ─────────────────
# 이슈에 기록된 실제 오배정 3건과 같은 focus 의 정답형 문서를 focus_relevance 로 점수화해
# **분리 가능성**을 회귀로 고정한다. 라우팅 표(FOCUS_ROUTING)가 바뀌어 오배정이 다시
# 정답형 수준으로 올라오면 이 테스트가 깨진다.
_MISMATCH = [
    # (focus, source_path, excerpt, 이슈의 오배정 사례)
    ("PMS and PMCF planning", "eu/EUDAMED_GUDID_UDI_등록DB_비교.md",
     "EUDAMED 와 GUDID 의 UDI 등록 DB 구조 비교. UDI-DI, Basic UDI-DI 발급 절차와 등록 화면.",
     "20260717-it01-ra_eu-004"),
    ("clinical evaluation gap analysis", "eu/PMS_특화표_PSUR_매트릭스.md",
     "PMS 특화표와 PSUR 매트릭스. surveillance 주기표.",
     "20260720-it01-ra_eu-005"),
    ("510(k) predicate strategy", "us/959_FDA_510k_RTA_기초보강_3주차_재이월.md",
     "3주차 인력 배치와 일정 이월 기록. 담당자별 진행률.",
     "ra_us-p2 #14"),
]
_ON_TOPIC = [
    ("PMS and PMCF planning", "eu/PMS_PMCF_계획서_템플릿.md",
     "PMS plan, PMCF plan, PSUR 주기, post-market surveillance 데이터 수집 계획."),
    ("clinical evaluation gap analysis", "eu/CER_임상평가_gap_analysis.md",
     "clinical evaluation report, CER, equivalence, MDCG 2020-5, PMCF gap."),
    ("510(k) predicate strategy", "us/510k_predicate_선정_전략.md",
     "510(k) predicate device 선정, substantial equivalence 논거, eSTAR 제출."),
]


@pytest.mark.parametrize("focus,path,text,case_id", _MISMATCH)
def test_known_mismatched_sources_score_below_floor_candidate(focus, path, text, case_id):
    """#147 오배정 사례는 relevance 3 미만이어야 한다(측정값 2/0/2)."""
    assert runner.focus_relevance(focus, path, text) < 3, case_id


@pytest.mark.parametrize("focus,path,text", _ON_TOPIC)
def test_on_topic_sources_stay_well_above_floor_candidate(focus, path, text):
    """같은 focus 의 정답형 문서는 3 이상이어야 한다(측정값 8/10/8)."""
    assert runner.focus_relevance(focus, path, text) >= 3


def test_mismatch_and_on_topic_are_separable_by_a_single_floor():
    """오배정 최댓값 < 정답형 최솟값 — 하나의 floor 값으로 분리 가능해야 한다."""
    worst_ok = min(runner.focus_relevance(f, p, t) for f, p, t in _ON_TOPIC)
    best_bad = max(runner.focus_relevance(f, p, t, ) for f, p, t, _ in _MISMATCH)
    assert best_bad < worst_ok, f"오배정 {best_bad} >= 정답형 {worst_ok} — 라우팅 표로 분리 불가"


def test_floor_is_unset_by_default_so_this_is_an_ops_decision():
    """기본값은 여전히 미설정(G7 운영값). 코드가 임의로 상한을 정하지 않는다."""
    assert runner.GROWTH_FOCUS_MIN_RELEVANCE is None
