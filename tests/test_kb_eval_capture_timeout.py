"""#147 — 캡처 상한이 실제 응답 시간 분포의 상단에 붙어 있던 문제.

실측(2026-09-11 승인 재질의 11회): 성공 6건 47.6~87.5초, 실패 5건 전부 90.1초에서 잘림.
상한 90초와 최대 성공값 87.5초의 여유가 2.5초였다.

**한정**: 상한을 올린 것은 완화책이며 효과는 미검증이다. 실패한 5건이 정상 답변을
완성했을 것인지, 240초에서 성공할지는 이 관측으로 알 수 없다 — 성공 표본의 최대값이
실패 표본의 완료 시간을 증명하지 않는다.

네트워크 없이 urlopen 을 스텁으로 바꿔 **실제 함수 동작**을 검사한다.
"""
import importlib.util
import json
import os
import socket
import sys
import urllib.request
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "kb-eval-checksheet.py"

# 2026-09-11 재질의 배치에서 성공한 호출의 실측 소요(초)
OBSERVED_SUCCESS_SECONDS = [51.7, 47.6, 67.1, 76.3, 87.5, 70.0]
OLD_DEFAULT = 90


def _load(env=None):
    old = dict(os.environ)
    if env:
        os.environ.update(env)
    try:
        spec = importlib.util.spec_from_file_location("kb_eval_checksheet_to", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        sys.modules["kb_eval_checksheet_to"] = mod
        spec.loader.exec_module(mod)
        return mod
    finally:
        os.environ.clear()
        os.environ.update(old)


class _Resp:
    def __init__(self, payload): self._p = json.dumps(payload).encode()
    def __enter__(self): return self
    def __exit__(self, *a): return False
    def read(self): return self._p


# ── 실제 함수 동작 (무네트워크 스텁) ────────────────────────────────────────────
def test_capture_passes_configured_timeout_to_urlopen(monkeypatch):
    """상한 값이 실제로 urlopen 에 전달되는지 — 상수만 바꾸고 전달이 안 되면 무의미하다."""
    m = _load()
    seen = {}

    def fake(req, timeout=None):
        seen["timeout"] = timeout
        seen["url"] = req.full_url
        return _Resp({"choices": [{"message": {"content": "답변"}}]})
    monkeypatch.setattr(m.urllib.request, "urlopen", fake)
    monkeypatch.setattr(m, "_load_soul", lambda p: "soul")

    text, err = m.capture_agent_response("ra-us", "과제")
    assert (text, err) == ("답변", "")
    assert seen["timeout"] == m.RESPONSE_CAPTURE_TIMEOUT
    assert seen["timeout"] > OLD_DEFAULT, "옛 기본값 이하로 전달된다"


def test_capture_returns_timeout_as_error_not_exception(monkeypatch):
    """타임아웃은 예외로 터지지 않고 (빈 문자열, 오류) 로 돌아와야 한다 — fail-safe 계약."""
    m = _load()

    def fake(req, timeout=None):
        raise socket.timeout("timed out")
    monkeypatch.setattr(m.urllib.request, "urlopen", fake)
    monkeypatch.setattr(m, "_load_soul", lambda p: "soul")

    text, err = m.capture_agent_response("ra-us", "과제")
    assert text == ""
    assert "response capture error" in err and "timed out" in err


def test_capture_error_message_matches_observed_failures(monkeypatch):
    """이번 배치 실패 5건의 문자열과 같은 형태여야 원인 대조가 성립한다."""
    m = _load()
    monkeypatch.setattr(m.urllib.request, "urlopen",
                        lambda req, timeout=None: (_ for _ in ()).throw(socket.timeout("timed out")))
    monkeypatch.setattr(m, "_load_soul", lambda p: "soul")
    _, err = m.capture_agent_response("ra-us", "과제")
    assert err.startswith("response capture error: timed out")


def test_capture_survives_malformed_response(monkeypatch):
    """응답 형태가 어긋나도 예외로 터지지 않는다(체크시트 생성을 막지 않는 fail-safe)."""
    m = _load()
    monkeypatch.setattr(m.urllib.request, "urlopen",
                        lambda req, timeout=None: _Resp({"unexpected": True}))
    monkeypatch.setattr(m, "_load_soul", lambda p: "soul")
    text, err = m.capture_agent_response("ra-us", "과제")
    assert text == "" and "response capture error" in err


# ── 상한 값 자체 ───────────────────────────────────────────────────────────────
def test_timeout_has_headroom_over_observed_successes():
    m = _load()
    worst = max(OBSERVED_SUCCESS_SECONDS)
    assert m.RESPONSE_CAPTURE_TIMEOUT >= worst * 2, (
        f"상한 {m.RESPONSE_CAPTURE_TIMEOUT}초는 관측 최대 {worst}초에 비해 여유가 부족하다")


def test_old_default_had_almost_no_headroom():
    """옛 상한 90초는 관측 최대 87.5초와 2.5초 차이였다 — 상한이 분포 상단에 붙어 있었다.
    (관측된 성공들이 잘렸다는 뜻은 아니다. 잘린 5건의 완료 시간은 미상이다.)"""
    assert OLD_DEFAULT - max(OBSERVED_SUCCESS_SECONDS) < 5


def test_timeout_is_still_bounded():
    m = _load()
    assert 0 < m.RESPONSE_CAPTURE_TIMEOUT <= 900


def test_env_override_still_works():
    assert _load({"KB_EVAL_RESPONSE_TIMEOUT": "123"}).RESPONSE_CAPTURE_TIMEOUT == 123
