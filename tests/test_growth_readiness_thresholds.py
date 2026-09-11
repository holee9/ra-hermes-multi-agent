"""#65 — 임계값 정책이 실제로 정해졌는지 검증하지 않던 결함.

`len(null_thresholds) == 0` 만 보면 두 경우가 통과한다.
  (1) 트리거가 하나도 없을 때 — 빈 목록에 null 이 없어 **공허하게 참**
  (2) threshold 가 "invalid" 같은 비수치 값일 때 — None 이 아니라 정의된 것으로 셈
둘 다 "정책이 정해졌다" 는 근거가 못 되는데 form_ready 를 열어 줬다.
"""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "growth-transition-readiness.py"


def _load():
    spec = importlib.util.spec_from_file_location("growth_readiness", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["growth_readiness"] = mod
    spec.loader.exec_module(mod)
    return mod


m = _load()


def _run(tmp_path, monkeypatch, trigger_cfg, days=30):
    """리포트 30일치를 유효하게 채우고 트리거 설정만 바꿔 form_ready 를 본다."""
    reports = tmp_path / "reports"
    reports.mkdir()
    for d in range(1, days + 1):
        (reports / f"growth-2026-08-{d:02d}.json").write_text(json.dumps({
            "messages_scanned": 10,
            "ingestion_diagnostics": {"empty_cause": "metrics_input_available"},
            "metrics": {"correction_rate": {"value": 0.1},
                        "first_pass_match_accuracy": {"value": 0.8},
                        "escalation_precision": {"value": 0.7},
                        "absence_pattern_signals": {"value": 1}},
        }), encoding="utf-8")
    cfg = tmp_path / "trigger.json"
    cfg.write_text(json.dumps(trigger_cfg), encoding="utf-8")
    monkeypatch.setattr(m, "ROOT", tmp_path)          # _path 가 상대경로를 만들 때 필요
    monkeypatch.setattr(m, "REPORTS_DIR", reports)
    monkeypatch.setattr(m, "TRIGGER_CONFIG", cfg)
    monkeypatch.setattr(sys, "argv", ["x"])
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        m.main()
    return json.loads(buf.getvalue())


@pytest.mark.parametrize("cfg,why", [
    ({}, "triggers 키 자체가 없음"),
    ({"triggers": {}}, "트리거가 하나도 없음 — 공허참"),
    ({"triggers": {"x": {"threshold": "invalid"}}}, "비수치 임계값"),
    ({"triggers": {"x": {"threshold": True}}}, "bool 은 수치가 아니다"),
    ({"triggers": {"x": {"threshold": None}}}, "미설정"),
    ({"triggers": {"x": "설정아님"}}, "트리거 항목이 객체가 아님"),
    ({"triggers": "설정아님"}, "triggers 가 객체가 아님"),
])
def test_unusable_threshold_config_blocks_form_ready(tmp_path, monkeypatch, cfg, why):
    out = _run(tmp_path, monkeypatch, cfg)
    assert out["form_transfer"]["ready"] is False, f"{why} 인데 준비 완료로 판정됨"
    assert out["form_transfer"]["conditions"]["thresholds_usable"] is False


def test_valid_numeric_thresholds_allow_form_ready(tmp_path, monkeypatch):
    """반대편 보존: 수치 임계값이 제대로 있으면 막지 않는다."""
    out = _run(tmp_path, monkeypatch, {"triggers": {"correction_rate": {"threshold": 0.2},
                                                    "escalation": {"threshold": 3}}})
    c = out["form_transfer"]["conditions"]
    assert c["thresholds_usable"] is True and c["triggers_defined"] == 2
    assert out["form_transfer"]["ready"] is True


def test_invalid_and_null_are_reported_separately(tmp_path, monkeypatch):
    out = _run(tmp_path, monkeypatch, {"triggers": {"a": {"threshold": "x"}, "b": {"threshold": None}}})
    c = out["form_transfer"]["conditions"]
    assert c["invalid_thresholds"] == ["a"] and c["null_thresholds"] == ["b"]
