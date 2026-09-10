"""Regression tests for scripts/growth-transition-readiness.py report selection (#103, #65, #40).

Reproduced defect (codex review 2026-09-09): `sorted(REPORTS_DIR.glob("growth*.json"))`
sorts by FILENAME, so "growth-diagnostic-2026-06-16.json" sorts after
"growth-2026-09-09.json" and was selected as the latest report, and
valid_metrics_days counted files rather than distinct dates.
"""
import importlib.util
import json
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "growth-transition-readiness.py"


def _load():
    spec = importlib.util.spec_from_file_location("growth_transition_readiness", _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


r = _load()


def _report(messages=10, cause="metrics_input_available", value=0.5):
    return {"messages_scanned": messages, "ingestion_diagnostics": {"empty_cause": cause},
            "metrics": {"correction_rate": {"value": value}}}


@pytest.fixture
def reports_dir(tmp_path, monkeypatch):
    d = tmp_path / "reports"
    d.mkdir()
    monkeypatch.setattr(r, "REPORTS_DIR", d)
    monkeypatch.setattr(r, "ROOT", tmp_path)
    return d


def _write(d, name, data):
    (d / name).write_text(json.dumps(data), encoding="utf-8")


def test_latest_is_newest_date_not_last_filename(reports_dir):
    _write(reports_dir, "growth-2026-06-16.json", _report())
    _write(reports_dir, "growth-2026-09-09.json", _report(value=0.7))
    _write(reports_dir, "growth-diagnostic-2026-06-16.json", _report(value=0.9))   # not a report
    _write(reports_dir, "growth-summary.json", _report())                            # not a report
    reports = r.load_reports()
    assert [x["_date"] for x in reports] == ["2026-06-16", "2026-09-09"]
    assert reports[-1]["_path"].endswith("growth-2026-09-09.json")


def test_report_date_regex():
    assert r.report_date(Path("growth-2026-09-09.json")) == "2026-09-09"
    assert r.report_date(Path("growth-diagnostic-2026-06-16.json")) is None
    assert r.report_date(Path("growth-2026-9-9.json")) is None


def test_unique_days_counts_dates_not_files(reports_dir):
    _write(reports_dir, "growth-2026-09-08.json", _report())
    _write(reports_dir, "growth-2026-09-09.json", _report())
    reports = r.load_reports()
    assert r.unique_days(reports) == 2
    assert r.unique_days(reports + [dict(reports[0])]) == 2


def test_reports_without_metrics_are_skipped(reports_dir):
    _write(reports_dir, "growth-2026-09-09.json", {"messages_scanned": 1})
    assert r.load_reports() == []


def test_main_output_uses_dated_latest(reports_dir, monkeypatch, capsys):
    _write(reports_dir, "growth-2026-06-16.json", _report(messages=0, cause="no_sessions"))
    _write(reports_dir, "growth-2026-09-09.json", _report())
    _write(reports_dir, "growth-diagnostic-2026-06-16.json", _report())
    monkeypatch.setattr(r, "TRIGGER_CONFIG", reports_dir / "missing.json")
    monkeypatch.setattr("sys.argv", ["readiness", "--min-valid-days", "30"])
    r.main()
    out = json.loads(capsys.readouterr().out)
    assert out["latest_report_date"] == "2026-09-09"
    assert out["reports_loaded"] == 2 and out["valid_reports"] == 1 and out["valid_metrics_days"] == 1
    assert out["form_transfer"]["ready"] is False
    assert out["form_transfer"]["conditions"]["valid_metrics_days"] == 1


# ---- #65 review (2026-09-10): incomplete collection must not count as valid evidence

def _incomplete(**kw):
    r = _report(**kw)
    r["ingestion_diagnostics"]["collection_incomplete"] = True
    return r


def test_incomplete_collection_days_are_not_valid_evidence(reports_dir, monkeypatch, capsys):
    for i in range(1, 31):
        _write(reports_dir, f"growth-2026-08-{i:02d}.json", _incomplete())
    (reports_dir.parent / "feedback" / "config").mkdir(parents=True, exist_ok=True)
    cfg = reports_dir.parent / "feedback" / "config" / "growth-trigger-config.json"
    cfg.write_text(json.dumps({"triggers": {"a": {"threshold": 0.1}}}), encoding="utf-8")
    monkeypatch.setattr(r, "TRIGGER_CONFIG", cfg)
    monkeypatch.setattr("sys.argv", ["readiness", "--min-valid-days", "30"])
    r.main()
    out = json.loads(capsys.readouterr().out)
    assert out["reports_loaded"] == 30 and out["valid_reports"] == 0 and out["valid_metrics_days"] == 0
    assert out["form_transfer"]["ready"] is False
    assert out["form_transfer"]["conditions"]["latest_collection_incomplete"] is True
    assert out["threshold_policy"]["status"] == "blocked_by_metrics_ingestion"


def test_complete_collection_days_still_count(reports_dir, monkeypatch, capsys):
    for i in range(1, 31):
        _write(reports_dir, f"growth-2026-08-{i:02d}.json", _report())
    monkeypatch.setattr(r, "TRIGGER_CONFIG", reports_dir / "missing.json")
    monkeypatch.setattr("sys.argv", ["readiness", "--min-valid-days", "30"])
    r.main()
    out = json.loads(capsys.readouterr().out)
    assert out["valid_metrics_days"] == 30 and out["form_transfer"]["conditions"]["latest_collection_incomplete"] is False
