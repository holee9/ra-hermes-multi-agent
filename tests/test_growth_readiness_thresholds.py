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


def _full(**over):
    """계약이 고정한 4개 트리거를 유효하게 채운 설정. 일부만 바꿔 음성 사례를 만든다."""
    base = {n: {"metric": metric, "threshold": 0.5}
            for n, metric in m.TRIGGER_METRIC_CONTRACT.items()}
    base.update(over)
    return {"triggers": base}


@pytest.mark.parametrize("cfg,why", [
    ({}, "triggers 키 자체가 없음"),
    ({"triggers": {}}, "트리거가 하나도 없음 — 공허참"),
    ({"triggers": {"x": {"threshold": "invalid"}}}, "비수치 임계값"),
    ({"triggers": {"x": {"threshold": True}}}, "bool 은 수치가 아니다"),
    ({"triggers": {"x": {"threshold": None}}}, "미설정"),
    ({"triggers": {"x": "설정아님"}}, "트리거 항목이 객체가 아님"),
    ({"triggers": "설정아님"}, "triggers 가 객체가 아님"),
    ({"triggers": {"임의키": {"metric": "m", "threshold": 0.5}}}, "계약의 4개 트리거가 아닌 임의 키"),
    ({"triggers": {n: {"metric": m.TRIGGER_METRIC_CONTRACT[n], "threshold": 0.5} for n in
                   ["duplicate_wp_reduction", "human_correction_rate", "transition_accuracy"]}},
     "4개 중 3개만 있음 — 나머지는 여전히 미정"),
])
def test_unusable_threshold_config_blocks_form_ready(tmp_path, monkeypatch, cfg, why):
    out = _run(tmp_path, monkeypatch, cfg)
    assert out["form_transfer"]["ready"] is False, f"{why} 인데 준비 완료로 판정됨"
    assert out["form_transfer"]["conditions"]["thresholds_usable"] is False


def test_valid_numeric_thresholds_allow_form_ready(tmp_path, monkeypatch):
    """반대편 보존: 수치 임계값이 제대로 있으면 막지 않는다."""
    out = _run(tmp_path, monkeypatch, _full())
    c = out["form_transfer"]["conditions"]
    assert c["thresholds_usable"] is True and c["triggers_defined"] == 4
    assert c["missing_triggers"] == [] and c["triggers_without_metric"] == []
    assert out["form_transfer"]["ready"] is True


def test_invalid_and_null_are_reported_separately(tmp_path, monkeypatch):
    out = _run(tmp_path, monkeypatch, _full(
        transition_accuracy={"metric": "m", "threshold": "x"},
        mail_triage_stability={"metric": "m", "threshold": None}))
    c = out["form_transfer"]["conditions"]
    assert c["invalid_thresholds"] == ["transition_accuracy"]
    assert c["null_thresholds"] == ["mail_triage_stability"]


@pytest.mark.parametrize("bad", [float("nan"), float("inf"), float("-inf")])
def test_non_finite_threshold_is_invalid(tmp_path, monkeypatch, bad):
    """NaN·무한대는 타입만 보면 통과하지만 임계값으로 쓸 수 없다."""
    out = _run(tmp_path, monkeypatch, _full(human_correction_rate={"metric": "m", "threshold": bad}))
    c = out["form_transfer"]["conditions"]
    assert c["thresholds_usable"] is False, f"{bad!r} 이 사용 가능으로 판정됨"
    assert "human_correction_rate" in c["invalid_thresholds"]


@pytest.mark.parametrize("metric,why", [
    (None, "metric 없음"),
    (123, "문자열이 아님 — str() 강제 변환으로 통과하면 안 된다"),
    ("not_a_metric", "계약이 정한 지표와 다름"),
    ("", "빈 문자열"),
])
def test_metric_must_match_contract(tmp_path, monkeypatch, metric, why):
    """임계값이 어떤 지표에 걸리는지는 계약이 정한다. 이름만 맞고 지표가 틀리면
    그 0.5 가 무엇에 대한 0.5 인지 알 수 없다."""
    cfg = {"threshold": 0.5} if metric is None else {"metric": metric, "threshold": 0.5}
    out = _run(tmp_path, monkeypatch, _full(transition_accuracy=cfg))
    c = out["form_transfer"]["conditions"]
    assert c["thresholds_usable"] is False, why
    assert c["triggers_without_metric"] == ["transition_accuracy"]


def test_contract_matches_shipped_config():
    """코드의 매핑이 배포 설정과 어긋나면 검증 자체가 틀린 것이다."""
    import json as _json
    cfg = _json.loads((Path(__file__).resolve().parent.parent /
                       "feedback" / "config" / "growth-trigger-config.json").read_text(encoding="utf-8"))
    shipped = {n: c.get("metric") for n, c in cfg["triggers"].items()}
    assert shipped == m.TRIGGER_METRIC_CONTRACT


def test_shipped_config_is_reported_as_not_usable(tmp_path, monkeypatch):
    """실제 배포 설정은 임계값이 전부 null 이므로 사용 불가로 보고돼야 한다(활성화 아님)."""
    import json as _json
    cfg = _json.loads((Path(__file__).resolve().parent.parent /
                       "feedback" / "config" / "growth-trigger-config.json").read_text(encoding="utf-8"))
    out = _run(tmp_path, monkeypatch, cfg)
    c = out["form_transfer"]["conditions"]
    assert c["thresholds_usable"] is False
    assert sorted(c["null_thresholds"]) == sorted(m.REQUIRED_TRIGGERS)
    assert c["missing_triggers"] == []
