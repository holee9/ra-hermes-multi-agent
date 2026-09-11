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
    monkeypatch.setattr(m, "ROOT", tmp_path)          # rel() 이 임시 경로에서도 동작하도록
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


# ── main() 자체를 구동하는 재개 검증 ──────────────────────────────────────────────
# 앞의 테스트들은 ledger_append 를 직접 불러서, main() 의 재개 경로 결함(unknown 케이스
# 재전송)을 잡지 못했다. 여기서는 DB·LLM 을 스텁으로 막고 main() 을 실제로 돌린다.
class _Cur:
    def __init__(self, paths): self._paths, self._rows = paths, []
    def __enter__(self): return self
    def __exit__(self, *a): return False
    def execute(self, sql, args=None):
        self._rows = [(p,) for p in self._paths] if "DISTINCT source_path" in sql else [("hash", "발췌")]
    def fetchall(self): return self._rows


class _Conn:
    def __init__(self, paths="auto"): self._paths = paths
    def __enter__(self): return self
    def __exit__(self, *a): return False
    def cursor(self): return _Cur(["github:holee9/x/도큐.md"])


def _drive(m, monkeypatch, calls, fail_at=None):
    monkeypatch.setitem(sys.modules, "psycopg2", type("P", (), {"connect": staticmethod(lambda dsn: _Conn())}))
    monkeypatch.setenv("POSTGRES_URL", "postgres://stub")

    def fake_capture(profile, assignment):
        calls.append(profile)
        if fail_at is not None and len(calls) == fail_at:
            raise RuntimeError("주입된 중단")
        return f"응답{len(calls)}", ""
    monkeypatch.setattr(m, "_load", lambda n, f: type("S", (), {"capture_agent_response": staticmethod(fake_capture)}))
    return m


def test_main_crash_then_resume_makes_no_extra_call(tmp_path, monkeypatch):
    """3번째에서 죽은 뒤 같은 원장으로 재개하면 **추가 호출 0회** 여야 한다.
    이전 구현은 성공한 case 만 제외해서 unknown 케이스를 다시 보냈다."""
    m = _load(tmp_path, monkeypatch)
    calls = []
    _drive(m, monkeypatch, calls, fail_at=3)
    with pytest.raises(RuntimeError):
        m.main(["--execute"])
    st = m.ledger_state()
    assert st["resolved"] == 2 and len(st["unknown"]) == 1, st
    before = len(calls)

    m.LOCK.unlink(missing_ok=True)                 # 비정상 종료로 남은 락을 사람이 지운 상황
    rc = m.main(["--execute"])                     # 재개 시도
    assert len(calls) == before, f"재개가 추가 호출 {len(calls) - before}회를 썼다"
    assert rc == 2, "unknown 이 있는데 재개를 막지 않았다"


def test_main_refuses_when_ledger_corrupt(tmp_path, monkeypatch):
    m = _load(tmp_path, monkeypatch)
    calls = []
    _drive(m, monkeypatch, calls)
    m.ledger_append({"event": "attempt_start", "attempt_id": "a1", "case_id": "c1"})
    with open(m.LEDGER, "a", encoding="utf-8") as f:
        f.write("{깨진\n")
    assert m.main(["--execute"]) == 2
    assert calls == [], "손상 원장에서 호출이 나갔다"


def test_all_failures_exit_nonzero(tmp_path, monkeypatch):
    """11건 전부 오류여도 기록은 확정되므로 resolved 는 11 이다. 그것을 성공으로 읽으면 안 된다."""
    m = _load(tmp_path, monkeypatch)
    calls = []
    monkeypatch.setitem(sys.modules, "psycopg2",
                        type("P", (), {"connect": staticmethod(lambda dsn: _Conn())}))
    monkeypatch.setenv("POSTGRES_URL", "postgres://stub")
    monkeypatch.setattr(m, "_load", lambda n, f: type("S", (), {
        "capture_agent_response": staticmethod(lambda pr, a: (calls.append(pr), ("", "fixture timeout"))[1])})) 
    rc = m.main(["--execute"])
    st = m.ledger_state()
    assert len(calls) == len(m.CASES) and st["resolved"] == len(m.CASES)
    assert st["done_case_ids"] == set(), "실패인데 성공으로 집계됐다"
    assert rc != 0, "전건 실패가 성공 종료코드로 나갔다"


def test_assignment_text_is_recorded(tmp_path, monkeypatch):
    """길이만이 아니라 실제 전달 과제문이 원장에 남아야 재현·판정이 가능하다."""
    m = _load(tmp_path, monkeypatch)
    calls = []
    _drive(m, monkeypatch, calls)
    m.main(["--execute"])
    starts = [json.loads(l) for l in m.LEDGER.read_text(encoding="utf-8").splitlines()
              if json.loads(l).get("event") == "attempt_start"]
    assert starts and all(s.get("assignment") for s in starts)
    assert all("Source:" in s["assignment"] for s in starts)


def test_lock_error_reports_owner_and_liveness_steps(tmp_path, monkeypatch, capsys):
    """락 안내는 소유 PID 와 **생존 확인 먼저** 를 알려야 한다.
    살아 있는 소유자를 확인하지 않고 지우면 중복 실행이 같은 예산을 또 쓴다."""
    m = _load(tmp_path, monkeypatch)
    _drive(m, monkeypatch, [])                      # DB·LLM 스텁 (이 테스트는 호출까지 가지 않는다)
    assert m.acquire_lock() is True                 # 선점된 상태를 만든다
    rc = m.main(["--execute"])
    out = json.loads(capsys.readouterr().out)
    assert rc == 2
    import os as _os
    assert str(_os.getpid()) in out["lock_owner"], "소유 PID 를 안내하지 않는다"
    steps = " ".join(out["steps"])
    assert "kill -0" in steps or "ps -p" in steps, "생존 확인 방법이 없다"
    assert "살아 있으면 지우지 말 것" in steps, "생존 시 삭제 금지 경고가 없다"


# ── 승인 배치별 원장 분리 ────────────────────────────────────────────────────
# 경로가 고정이면 이전 배치의 unknown 을 지우지 않고는 새 승인분을 돌릴 수 없다.
# 그 지우기가 바로 해서는 안 되는 일이므로(소비 기록 소실) 배치 경로를 분리한다.
def test_batch_isolates_ledger_and_preserves_previous(tmp_path, monkeypatch):
    m = _load(tmp_path, monkeypatch)
    base = m.OUT_DIR
    # 이전 배치: 결과 없는 시도 1건 (지우면 안 되는 기록)
    m.ledger_append({"event": "attempt_start", "attempt_id": "old-01", "case_id": "c1"})
    assert m.ledger_state()["unknown"] == ["old-01"]

    calls = []
    _drive(m, monkeypatch, calls)
    monkeypatch.setattr(m, "OUT_DIR", base)        # main 이 --batch 로 다시 계산한다
    m.main(["--execute", "--batch", "approved-2"])

    # 새 배치 원장은 별도 파일이고, 이전 기록은 그대로 남아 있다
    assert (base / "approved-2" / "ledger.jsonl").exists()
    assert (base / "ledger.jsonl").exists()
    old = [l for l in (base / "ledger.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(old) == 1 and "old-01" in old[0], "이전 배치 기록이 변경됐다"
    assert len(calls) == len(m.CASES), "새 배치가 전체 케이스를 돌지 않았다"


def test_batch_name_is_validated(tmp_path, monkeypatch):
    m = _load(tmp_path, monkeypatch)
    calls = []
    _drive(m, monkeypatch, calls)
    assert m.main(["--execute", "--batch", "../탈출"]) == 2
    assert calls == [], "잘못된 배치 이름으로 호출이 나갔다"


# ── 부분 승인 (--cases) ─────────────────────────────────────────────────────
# timeout 5건만 재호출 승인된 경우. 예산이 11 로 남아 있으면 승인보다 많이 쓸 수 있다.
def test_cases_subset_runs_only_selected_with_matching_budget(tmp_path, monkeypatch):
    m = _load(tmp_path, monkeypatch)
    calls = []
    _drive(m, monkeypatch, calls)
    rc = m.main(["--execute", "--batch", "retry-5", "--cases", "1,2,3,4,5"])
    assert len(calls) == 5, f"승인 5건인데 {len(calls)}회 호출"
    assert m.CALL_BUDGET == 5
    led = [json.loads(l) for l in (m.OUT_DIR / "ledger.jsonl").read_text(encoding="utf-8").splitlines()]
    ids = {r["case_id"] for r in led if r["event"] == "attempt_start"}
    assert ids == {c["case_id"] for c in m.CASES if c["n"] <= 5}
    assert rc == 0, "선택 5건 전부 성공인데 미완(nonzero)으로 끝났다"


def test_cases_requires_batch_and_valid_numbers(tmp_path, monkeypatch):
    m = _load(tmp_path, monkeypatch)
    calls = []
    _drive(m, monkeypatch, calls)
    assert m.main(["--execute", "--cases", "1,2"]) == 2, "--batch 없이 부분 실행을 허용했다"
    assert m.main(["--execute", "--batch", "b", "--cases", "0,12"]) == 2
    assert m.main(["--execute", "--batch", "b", "--cases", "x"]) == 2
    assert calls == [], "잘못된 --cases 로 호출이 나갔다"


# ── 검토 자료 생성기 (사람 판정 보조) ──────────────────────────────────────────
def test_review_flags_fabricated_identifier(tmp_path, monkeypatch):
    """응답이 인용한 식별자가 전달 발췌에 없으면 '검토 필요' 로 올라와야 한다 —
    이 프로젝트에서 실측된 실패 유형(#118)이다."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "rq_review", ROOT / "scripts" / "kb-eval-requery-review.py")
    rv = importlib.util.module_from_spec(spec)
    sys.modules["rq_review"] = rv
    spec.loader.exec_module(rv)

    shown = "Source excerpts:\n- 이 문서는 K123456 을 다룬다"
    assert rv.unverified_ids("predicate 는 K123456 입니다", shown) == []
    assert rv.unverified_ids("predicate 는 K999999 입니다", shown) == ["K999999"]
    # 한글 조사가 붙어도 잡는다 (\b 는 한글을 단어문자로 보므로 쓸 수 없다)
    assert rv.unverified_ids("K999999도 확인하세요", shown) == ["K999999"]
    # 공백·하이픈 차이는 같은 것으로 본다
    assert rv.unverified_ids("K 123456", "K123456") == []


def test_review_keeps_full_response_text(tmp_path, monkeypatch):
    """'응답 전문' 이라고 보여주면서 6000자에서 잘라내던 결함 — 끝까지 보존되어야 한다."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "rq_review_full", ROOT / "scripts" / "kb-eval-requery-review.py")
    rv = importlib.util.module_from_spec(spec)
    sys.modules["rq_review_full"] = rv
    spec.loader.exec_module(rv)
    monkeypatch.setattr(rv, "ROOT", tmp_path)

    end_mark = "END-MARK-7f3a9c"
    resp = "가" * 9000 + "\n```inner fence```\n" + end_mark
    base = tmp_path / "reports" / "kb-eval-requery-147" / "b1"
    base.mkdir(parents=True)
    (base / "ledger.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in [
        {"event": "attempt_start", "attempt_id": "a1", "case_id": "c1", "assignment": "x"},
        {"event": "attempt_result", "attempt_id": "a1", "case_id": "c1", "ok": True,
         "chars": len(resp), "response": resp},
    ]), encoding="utf-8")

    assert rv.main(["--batch", "b1"]) == 0
    md = (base / "review.md").read_text(encoding="utf-8")
    assert end_mark in md, "6000자 이후 응답이 잘렸다"
    assert resp in md
    assert "````\n" + resp + "\n````" in md, "응답 속 백틱이 코드 블록을 깨뜨린다"
