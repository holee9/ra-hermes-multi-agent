"""#147 — 캡처 타임아웃이 실제 응답 시간 분포의 상단에 붙어 정상 응답을 잘라내던 문제.

실측(2026-09-11 재질의 11회): 성공 응답 47.6~87.5초, 상한 90초에서 5건이 정확히 90.1초에
잘렸다. 최대 성공값과 상한의 여유가 2.5초뿐이라 정상 응답이 '캡처 실패' 로 기록됐다.
"""
import importlib.util
import os
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "kb-eval-checksheet.py"

# 2026-09-11 재질의 배치에서 성공한 호출의 실측 소요(초)
OBSERVED_SUCCESS_SECONDS = [51.7, 47.6, 67.1, 76.3, 87.5, 70.0]


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


def test_timeout_has_headroom_over_observed_responses():
    """상한이 관측 최대에 붙어 있으면 정상 응답이 잘린다. 충분한 여유가 있어야 한다."""
    m = _load()
    worst = max(OBSERVED_SUCCESS_SECONDS)
    assert m.RESPONSE_CAPTURE_TIMEOUT >= worst * 2, (
        f"상한 {m.RESPONSE_CAPTURE_TIMEOUT}초는 관측 최대 {worst}초에 비해 여유가 부족하다")


def test_old_default_would_have_truncated_observed_responses():
    """회귀의 근거 고정 — 옛 기본값 90초는 관측 최대 87.5초와 2.5초 차이였다."""
    worst = max(OBSERVED_SUCCESS_SECONDS)
    assert 90 - worst < 5, "옛 상한이 관측 최대에 붙어 있었다는 전제가 깨졌다"


def test_timeout_is_still_bounded():
    """상한을 없애면 안 된다 — 무한정 대기는 다른 문제를 만든다."""
    m = _load()
    assert 0 < m.RESPONSE_CAPTURE_TIMEOUT <= 900


def test_env_override_still_works():
    m = _load({"KB_EVAL_RESPONSE_TIMEOUT": "123"})
    assert m.RESPONSE_CAPTURE_TIMEOUT == 123
