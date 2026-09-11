"""#136 — deriver flush probe 가 예외에서 '진단 불가' 를 만들지 못하던 결함.

docker 바이너리 부재나 타임아웃은 예외로 나가 버려 unavailable 판정에 도달하지 못했다.
게이트는 어차피 닫히지만, "설정이 False" 인지 "probe 를 못 돌렸다" 인지가 구분되지 않아
운영자가 엉뚱한 것을 고치게 된다. Docker·운영 실행 없이 예외 주입으로 검증한다.
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "pre-auto-growth-loop.py"


def _load():
    spec = importlib.util.spec_from_file_location("pre_auto_growth", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["pre_auto_growth"] = mod
    spec.loader.exec_module(mod)
    return mod


m = _load()


@pytest.mark.parametrize("exc", [
    FileNotFoundError("docker"),                                   # 바이너리 없음
    subprocess.TimeoutExpired(cmd=["docker"], timeout=60),         # 응답 없음
    PermissionError("/var/run/docker.sock"),                       # 소켓 권한 (OSError 계열)
    subprocess.SubprocessError("spawn failed"),
])
def test_probe_exception_becomes_unavailable_not_crash(monkeypatch, exc):
    def boom(*a, **k):
        raise exc
    monkeypatch.setattr(m.subprocess, "run", boom)
    out = m.check_deriver_flush({})
    assert out["ok"] is False                      # 게이트는 닫힌 채로
    assert out["probe"] == "unavailable", "설정=False 와 구분되지 않는다"
    assert type(exc).__name__ in out["command"]["stderr"], "원인이 보고에 실리지 않는다"


def test_unavailable_keeps_same_result_shape(monkeypatch):
    """소비 측이 command.stderr 를 읽으므로 정상 경로와 키 모양이 같아야 한다."""
    monkeypatch.setattr(m.subprocess, "run", lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError()))
    out = m.check_deriver_flush({})
    assert set(("ok", "probe", "value", "command")) <= set(out)
    assert set(("cmd", "returncode", "stderr", "stdout")) <= set(out["command"])


def test_setting_false_is_not_reported_as_unavailable(monkeypatch):
    """반대편 보존: 실제로 False 면 unavailable 이 아니라 설정 문제로 보고돼야 한다."""
    class R:
        ok, stdout, stderr, returncode = True, "False", "", 0
        def to_report(self): return {"cmd": [], "returncode": 0, "stdout": "False", "stderr": ""}
    monkeypatch.setattr(m, "run_command", lambda *a, **k: R())
    out = m.check_deriver_flush({})
    assert out["probe"] == "ok" and out["ok"] is False and out["value"] == "False"


# ── 소비 경로까지: 최종 진단 문구에 원인이 실려야 한다 ─────────────────────────────
# probe 결과만 고쳐도 evaluate_iteration 이 command.stderr 를 읽으므로, 거기 원인이
# 없으면 운영자에게는 'no output' 으로만 보인다. 끝까지 전달되는지 고정한다.
def _report(flush):
    """evaluate_iteration 이 읽는 최소 보고 구조. 다른 검사는 전부 통과하도록 채워
    deriver_flush 진단만 남긴다."""
    return {
        "deriver_flush": flush,
        "queue_before": {}, "queue_after": {},
        "verifiers": [],
        "daily_growth_dry_run": {"command": {"returncode": 0},
                                 "plan": {"execute_gate": {"allowed": True}}},
        "growth_message_health": {"json_envelopes": 0},
    }


def test_exception_cause_reaches_final_diagnosis(monkeypatch):
    monkeypatch.setattr(m.subprocess, "run",
                        lambda *a, **k: (_ for _ in ()).throw(subprocess.TimeoutExpired(cmd=["docker"], timeout=60)))
    flush = m.check_deriver_flush({})
    monkeypatch.setattr(m, "pending_for_scope", lambda *a, **k: 0)
    failures = m.evaluate_iteration(_report(flush), max_pending=10, pending_scope="all")

    assert any("probe unavailable" in f for f in failures), failures
    joined = " ".join(failures)
    assert "TimeoutExpired" in joined, f"예외 유형이 최종 진단에 없다: {joined}"
    assert "no output" not in joined, "원인 없이 no output 으로만 보고된다"


def test_setting_false_diagnosis_is_distinct(monkeypatch):
    """반대편: 실제 False 는 'probe unavailable' 이 아니라 설정 문제로 보고돼야 한다."""
    class R:
        ok, stdout, stderr, returncode = True, "False", "", 0
        def to_report(self): return {"cmd": [], "returncode": 0, "stdout": "False", "stderr": ""}
    monkeypatch.setattr(m, "run_command", lambda *a, **k: R())
    monkeypatch.setattr(m, "pending_for_scope", lambda *a, **k: 0)
    failures = m.evaluate_iteration(_report(m.check_deriver_flush({})), max_pending=10, pending_scope="all")
    assert any("is not True" in f for f in failures), failures
    assert not any("probe unavailable" in f for f in failures), failures
