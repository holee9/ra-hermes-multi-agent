"""#147 — case-generation defects are recorded and reported separately from agent errors.

Review (codex, 2026-09-09): capture_failed / source_mismatch had no structured field in
the feedback parser, correction_rate had no split, and assemble_cases back-filled a short
pool with focus-unrelated sources. Also: input defects must NOT be dropped from the
system-level quality signal — both are reported.
"""
import importlib.util
import json
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
    assert rec["case_defect"] == {"capture_failed": False, "source_mismatch": False}


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


def test_correction_rate_reports_system_and_agent_attributable_split():
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
    assert r["case_defects"] == {"count": 2, "corrected": 2, "capture_failed": 1, "source_mismatch": 1}
    assert r["agent_attributable"] == {"value": 1 / 3, "numerator": 1, "denominator": 3}
    assert any(s.get("case_defect") == {"capture_failed": True} for s in r["samples"])


def test_correction_rate_without_defect_field_is_unchanged():
    since = datetime(2026, 7, 16, tzinfo=timezone.utc)
    until = datetime(2026, 7, 17, tzinfo=timezone.utc)
    r = gm.compute_correction_rate({"f": [_score_msg("2026-07-16T01:00:00+00:00", True)]}, since, until)
    assert r["value"] == 1.0 and r["case_defects"]["count"] == 0
    assert r["agent_attributable"] == {"value": 1.0, "numerator": 1, "denominator": 1}


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
