"""#147 재질의 실행기 — 손실 방지 회귀. 네트워크·DB 없이 검증한다.

이전 구현은 11회를 다 돌고 **마지막에 일괄 저장**해서, 중간에 죽으면 이미 소비한 호출과
응답이 전부 사라졌다(2026-09-11 실제 발생). 여기서는 3번째 호출에 예외를 주입해
앞 2건이 보존되는지, 재실행이 추가 호출을 쓰지 않는지 고정한다.
"""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("rq147", ROOT / "scripts" / "kb-eval-requery-147.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["rq147"] = m
    spec.loader.exec_module(m)
    monkeypatch.setattr(m, "OUT_DIR", tmp_path / "out")
    monkeypatch.setattr(m, "LEDGER", tmp_path / "out" / "ledger.jsonl")
    monkeypatch.setattr(m, "LOCK", tmp_path / "out" / ".lock")
    return m


def test_each_call_is_persisted_before_and_after(tmp_path, monkeypatch):
    m = _load(tmp_path, monkeypatch)
    m.ledger_append({"event": "attempt_start", "attempt_id": "a1", "case_id": "c1"})
    m.ledger_append({"event": "attempt_result", "attempt_id": "a1", "case_id": "c1", "ok": True})
    st = m.ledger_state()
    assert st["consumed"] == 1 and st["resolved"] == 1 and st["unknown"] == []
    assert st["remaining"] == m.CALL_BUDGET - 1


def test_crash_mid_run_preserves_earlier_results(tmp_path, monkeypatch):
    """3번째에서 죽어도 앞 2건의 응답은 파일에 남아 있어야 한다."""
    m = _load(tmp_path, monkeypatch)
    for i in (1, 2):
        m.ledger_append({"event": "attempt_start", "attempt_id": f"a{i}", "case_id": f"c{i}"})
        m.ledger_append({"event": "attempt_result", "attempt_id": f"a{i}", "case_id": f"c{i}",
                         "ok": True, "response": f"응답{i}"})
    m.ledger_append({"event": "attempt_start", "attempt_id": "a3", "case_id": "c3"})  # 결과 없이 중단

    st = m.ledger_state()
    assert st["resolved"] == 2, "앞 2건 결과가 소실됐다"
    assert st["unknown"] == ["a3"], "중단된 시도가 unknown 으로 남지 않았다"
    saved = [json.loads(l) for l in m.LEDGER.read_text(encoding="utf-8").splitlines()]
    assert [r.get("response") for r in saved if r.get("event") == "attempt_result"] == ["응답1", "응답2"]


def test_unknown_counts_as_consumed_not_reset_to_zero(tmp_path, monkeypatch):
    """unknown 을 0 으로 초기화하지 않는다 — 실제 호출 여부를 알 수 없으므로 소비로 센다."""
    m = _load(tmp_path, monkeypatch)
    for i in range(1, 4):
        m.ledger_append({"event": "attempt_start", "attempt_id": f"a{i}", "case_id": f"c{i}"})
    st = m.ledger_state()
    assert st["consumed"] == 3 and st["remaining"] == m.CALL_BUDGET - 3
    assert len(st["unknown"]) == 3


def test_budget_exhaustion_blocks_further_calls(tmp_path, monkeypatch):
    m = _load(tmp_path, monkeypatch)
    for i in range(m.CALL_BUDGET):
        m.ledger_append({"event": "attempt_start", "attempt_id": f"a{i}", "case_id": f"c{i}"})
    assert m.ledger_state()["remaining"] == 0


def test_lock_is_exclusive(tmp_path, monkeypatch):
    """중복 실행이 같은 예산을 따로 소비하지 못한다."""
    m = _load(tmp_path, monkeypatch)
    assert m.acquire_lock() is True
    assert m.acquire_lock() is False, "두 번째 실행이 락을 얻었다"
    m.LOCK.unlink()
    assert m.acquire_lock() is True


def test_corrupt_ledger_makes_consumption_indeterminable(tmp_path, monkeypatch):
    """손상 줄을 건너뛰면 소비를 **적게** 세어 승인 총량을 넘길 수 있다.
    손상된 줄이 잃어버린 attempt_start 일 수 있으므로 확정 불가로 표시하고 실행을 막는다."""
    m = _load(tmp_path, monkeypatch)
    m.ledger_append({"event": "attempt_start", "attempt_id": "a1", "case_id": "c1"})
    with open(m.LEDGER, "a", encoding="utf-8") as f:
        f.write("{깨진 줄\n")
    st = m.ledger_state()
    assert st["corrupt_lines"] == 1
    assert st["determinable"] is False, "손상 원장인데 소비 확정 가능으로 보고했다"


def test_clean_ledger_is_determinable(tmp_path, monkeypatch):
    m = _load(tmp_path, monkeypatch)
    m.ledger_append({"event": "attempt_start", "attempt_id": "a1", "case_id": "c1"})
    assert m.ledger_state()["determinable"] is True
