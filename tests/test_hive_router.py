"""P2 격리 라우터 테스트 (SPEC-HIVE-001 §4 P2, #150 리뷰 5598913943 §3 검증 행렬).

외부 서비스 쓰기 없음 — 모든 검사는 tmp_path 안의 hive 사본에서만 일어난다.
행렬 매핑:
  계약   : 라우터 산출 log.jsonl이 tools/validate_events.py 를 오류 0으로 통과
  대화   : 자기전달·종결형 답신·broadcast·corr 규칙·미확인 corr·홉 상한
  내구성 : inbox 쓰기 직후 / log append 직전·직후 / archive 직전 장애 → 재시작 시 중복 없이 완주,
           부분 broadcast는 성공 수신자와 미전달 수신자를 따로 보존
  권한·동시성: 다른 peer 위장(actor 덮어쓰기), registry 밖 outbox 무시, 단일 실행 lock(pid 확인)
  게이트·폭주: HOP_CAP 미설정 시 전달 없음, 초과 시 escalation 1회, undeliverable은 사람에게
"""
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ROUTER = ROOT / "tools" / "hive_router.py"
VALIDATOR = ROOT / "tools" / "validate_events.py"
KST = timezone(timedelta(hours=9))


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod          # dataclasses + __future__ annotations need the module registered
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def hr():
    return _load(ROUTER, "hive_router")


@pytest.fixture(scope="module")
def ve():
    return _load(VALIDATOR, "validate_events")


class Clock:
    """단조 증가 시계 — ts 역행 경고 없이 이벤트 순서를 고정한다."""
    def __init__(self):
        self.t = datetime(2026, 9, 9, 12, 0, 0, tzinfo=KST)

    def __call__(self):
        self.t += timedelta(seconds=1)
        return self.t


@pytest.fixture
def hive(tmp_path):
    root = tmp_path / "ra-hive"
    (root / "registry").mkdir(parents=True)
    (root / "registry" / "actors.json").write_text(json.dumps({"version": 1, "actors": {
        "ra_us": {"workspace": "work", "status": "active"},
        "ra_eu": {"workspace": "work", "status": "active"},
        "ra_kr": {"workspace": "work", "status": "paused"},
        "infra_t3610": {"workspace": "infra", "status": "active"},
    }}), encoding="utf-8")
    for a in ("ra_us", "ra_eu", "ra_kr", "infra_t3610", "human"):
        (root / "agents" / a / "outbox").mkdir(parents=True)
        (root / "agents" / a / "inbox").mkdir(parents=True)
    return root


def _outbox(root, actor, raw, name="20260909T120000-0001.json"):
    p = root / "agents" / actor / "outbox" / name
    p.write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    return p


def _router(hr, root, clock=None, **kw):
    kw.setdefault("hop_cap", 12)
    kw.setdefault("execute", True)
    return hr.HiveRouter(root, now=clock or Clock(), **kw)


def _log(root):
    p = root / "log.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def _inbox(root, actor):
    return sorted(f for f in (root / "agents" / actor / "inbox").iterdir() if f.is_file())


def _tree(root):
    return sorted(str(p.relative_to(root)) + (f":{p.stat().st_size}" if p.is_file() else "")
                  for p in root.rglob("*"))


def _assert_log_valid(ve, root):
    schema = json.loads((ROOT / "docs/contract/event-v2.1.schema.json").read_text(encoding="utf-8"))
    records = ve.load_jsonl(root / "log.jsonl")
    errors, _, _ = ve.validate(records, schema, hop_cap=12)
    assert errors == [], errors


REQ = {"kind": "handoff", "case": {"wp": 1042, "regime": "US"}, "to": "ra_eu", "act": "request",
       "payload": {"to_actor": "ra_eu", "reason": "EU MDR 확인"}, "corr": None, "conversation": None}


# ---------------------------------------------------------------- dry-run

def test_dry_run_writes_nothing(hr, hive):
    _outbox(hive, "ra_us", REQ)
    before = _tree(hive)
    res = _router(hr, hive, execute=False).run()
    assert [p.outcome for p in res.plans] == ["deliver"] and res.plans[0].targets == ["ra_eu"]
    assert res.touched == [] and _tree(hive) == before


def test_cli_dry_run_default_and_exit_codes(hive):
    _outbox(hive, "ra_us", REQ)
    r = subprocess.run([sys.executable, str(ROUTER), str(hive), "--hop-cap", "12"], capture_output=True, text=True)
    assert r.returncode == 0 and "[DRY-RUN]" in r.stdout and not (hive / "log.jsonl").exists()
    r = subprocess.run([sys.executable, str(ROUTER), str(hive / "nope")], capture_output=True, text=True)
    assert r.returncode == 2


# ---------------------------------------------------------------- happy path

def test_request_is_delivered_logged_archived(hr, ve, hive):
    src = _outbox(hive, "ra_us", REQ)
    res = _router(hr, hive).run()
    assert res.errors == []
    inbox = _inbox(hive, "ra_eu")
    assert len(inbox) == 1
    ev = json.loads(inbox[0].read_text(encoding="utf-8"))
    assert ev["actor"] == "ra_us" and ev["hops"] == 0 and ev["requires_reply"] is True
    assert "corr" not in ev and ev["conversation"].startswith("conv_1042_handoff_")
    log = _log(hive)
    assert len(log) == 1 and log[0]["payload"]["delivered_to"] == ["ra_eu"] and log[0]["id"] == ev["id"]
    assert not src.exists() and (src.parent / ".sent" / src.name).exists()
    assert json.loads((hive / "agents/ra_us/cursor.json").read_text())["last_processed"] == ev["id"]
    assert all(str(t).startswith(str(hive)) for t in res.touched)
    _assert_log_valid(ve, hive)


def test_reply_inherits_conversation_and_increments_hops(hr, ve, hive):
    _outbox(hive, "ra_us", REQ)
    clock = Clock()
    _router(hr, hive, clock).run()
    first = _log(hive)[0]
    _outbox(hive, "ra_eu", {"kind": "comment", "to": "ra_us", "act": "agree", "payload": {"text_ref": "op://x"},
                            "corr": first["id"]})
    _router(hr, hive, clock).run()
    reply = _log(hive)[1]
    assert reply["hops"] == 1 and reply["conversation"] == first["conversation"] and reply["corr"] == first["id"]
    assert reply["requires_reply"] is False
    _assert_log_valid(ve, hive)


def test_observation_event_without_to_is_logged_not_delivered(hr, ve, hive):
    _outbox(hive, "ra_us", {"kind": "comment", "case": {"wp": 1}, "payload": {"text_ref": "op://x"}})
    _router(hr, hive).run()
    assert len(_log(hive)) == 1 and "to" not in _log(hive)[0]
    assert all(_inbox(hive, a) == [] for a in ("ra_eu", "ra_us", "human"))
    _assert_log_valid(ve, hive)


# ---------------------------------------------------------------- conversation rules

@pytest.mark.parametrize("raw,reason", [
    ({**REQ, "to": "ra_us"}, "self-send"),
    # 종결형/broadcast의 requires_reply=true는 스키마(const false)가 먼저 잡는다 — 사유는 "schema:" 접두
    ({**REQ, "act": "inform", "requires_reply": True}, "schema"),
    ({**REQ, "to": "broadcast", "requires_reply": True}, "schema"),
    ({**REQ, "corr": "evt_20260909T000000_dead"}, "unknown-corr"),
    ({**REQ, "kind": "not-a-kind"}, "schema"),
])
def test_invalid_message_is_rejected_with_policy_and_peer_notice(hr, ve, hive, raw, reason):
    src = _outbox(hive, "ra_us", raw)
    res = _router(hr, hive).run()
    assert res.plans[0].outcome == "reject" and reason in res.plans[0].reason
    assert (src.parent / ".rejected" / src.name).exists()
    log = _log(hive)
    pol = [e for e in log if e["kind"] == "policy"]
    assert len(pol) == 1 and pol[0]["payload"]["action"] == "refuse-invalid" and reason in pol[0]["payload"]["reason"]
    assert pol[0]["payload"]["target_actor"] == "ra_us"
    notice = _inbox(hive, "ra_us")
    assert len(notice) == 1 and json.loads(notice[0].read_text())["act"] == "inform"
    assert _inbox(hive, "ra_eu") == []
    _assert_log_valid(ve, hive)


def test_reply_to_terminal_event_is_rejected(hr, hive):
    _outbox(hive, "ra_us", {**REQ, "act": "inform", "requires_reply": False})
    clock = Clock()
    _router(hr, hive, clock).run()
    first = _log(hive)[0]
    _outbox(hive, "ra_eu", {"kind": "comment", "to": "ra_us", "act": "agree", "payload": {}, "corr": first["id"]})
    res = _router(hr, hive, clock).run()
    assert res.plans[0].outcome == "reject" and "reply-to-terminal" in res.plans[0].reason


def test_non_object_or_broken_json_goes_to_rejected(hr, hive):
    p = hive / "agents/ra_us/outbox/20260909T120000-0001.json"
    p.write_text("null", encoding="utf-8")
    q = hive / "agents/ra_us/outbox/20260909T120000-0002.json"
    q.write_text("{bad", encoding="utf-8")
    res = _router(hr, hive).run()
    assert [x.outcome for x in res.plans] == ["reject", "reject"]
    assert not p.exists() and (p.parent / ".rejected" / p.name).exists() and (q.parent / ".rejected" / q.name).exists()


# ---------------------------------------------------------------- routing / gate

def test_paused_target_is_escalated_to_human_not_dropped(hr, ve, hive):
    src = _outbox(hive, "ra_us", {**REQ, "to": "ra_kr"})
    res = _router(hr, hive).run()
    assert res.plans[0].outcome == "escalate" and res.plans[0].reason == "undeliverable"
    esc = json.loads(_inbox(hive, "human")[0].read_text())
    assert esc["kind"] == "escalation" and esc["to"] == "human" and esc["payload"]["reason"] == "undeliverable"
    assert esc["payload"]["targets"] == ["ra_kr"] and esc["payload"]["ref_evt"] == res.plans[0].msg_id
    assert (src.parent / ".rejected" / src.name).exists() and _inbox(hive, "ra_kr") == []
    _assert_log_valid(ve, hive)


def test_broadcast_fans_out_to_active_peers_except_sender(hr, ve, hive):
    _outbox(hive, "ra_us", {**REQ, "to": "broadcast", "act": "inform", "payload": {"note": "x"}})
    _router(hr, hive).run()
    assert len(_inbox(hive, "ra_eu")) == 1 and len(_inbox(hive, "infra_t3610")) == 1
    assert _inbox(hive, "ra_us") == [] and _inbox(hive, "ra_kr") == []
    assert _log(hive)[0]["payload"]["delivered_to"] == ["infra_t3610", "ra_eu"]
    _assert_log_valid(ve, hive)


def test_hop_cap_unset_holds_conversation_events(hr, hive):
    _outbox(hive, "ra_us", REQ)
    _outbox(hive, "ra_us", {"kind": "comment", "payload": {}}, name="20260909T120000-0002.json")
    before = _tree(hive)
    res = _router(hr, hive, hop_cap=None).run()
    assert [p.outcome for p in res.plans] == ["held", "observe"]
    assert len(_inbox(hive, "ra_eu")) == 0
    assert (hive / "agents/ra_us/outbox/20260909T120000-0001.json").exists()   # 그대로 남는다
    assert len(_log(hive)) == 1                                                  # 관찰 이벤트만
    assert before != _tree(hive)


def test_hop_cap_exceeded_escalates_once_and_rejects_original(hr, ve, hive):
    clock = Clock()
    _outbox(hive, "ra_us", {**REQ, "act": "query"})
    _router(hr, hive, clock, hop_cap=2).run()
    prev = _log(hive)[-1]
    actors = ["ra_eu", "ra_us"]
    for i in range(3):
        a = actors[i % 2]
        _outbox(hive, a, {"kind": "comment", "to": actors[(i + 1) % 2], "act": "query", "payload": {}, "corr": prev["id"]},
                name=f"20260909T12000{i + 1}-0001.json")
        res = _router(hr, hive, clock, hop_cap=2).run()
        prev = [e for e in _log(hive) if e["actor"] == a][-1] if res.plans[0].outcome == "deliver" else prev
    assert res.plans[0].outcome == "escalate" and res.plans[0].reason == "hop-cap"
    esc = [json.loads(f.read_text()) for f in _inbox(hive, "human")]
    assert len(esc) == 1 and esc[0]["payload"]["reason"] == "hop-cap" and esc[0]["payload"]["hops_reached"] == 3
    _assert_log_valid(ve, hive)


# ---------------------------------------------------------------- durability (fault injection)

def _run_with_fault(hr, hive, clock, fault_at, target=None):
    with pytest.raises(hr.InjectedFault):
        _router(hr, hive, clock, fault_at=fault_at, fault_target=target).run()
    assert not (hive / ".router/lock").exists()          # finally 절에서 lock 해제


@pytest.mark.parametrize("fault_at", ["before_log_append", "after_log_append", "before_archive"])
def test_crash_then_restart_completes_without_duplicates(hr, ve, hive, fault_at):
    src = _outbox(hive, "ra_us", REQ)
    clock = Clock()
    _run_with_fault(hr, hive, clock, fault_at)
    res = _router(hr, hive, clock).run()
    assert res.errors == [] and res.plans[0].outcome == "deliver"
    assert len(_inbox(hive, "ra_eu")) == 1
    log = _log(hive)
    assert len(log) == 1 and log[0]["payload"]["delivered_to"] == ["ra_eu"]
    assert (src.parent / ".sent" / src.name).exists() and not src.exists()
    j = json.loads((hive / ".router/journal" / f"{log[0]['id']}.json").read_text())
    assert j["step"] == "archived"
    _assert_log_valid(ve, hive)


def test_partial_broadcast_keeps_delivered_and_undelivered_apart(hr, ve, hive):
    _outbox(hive, "ra_us", {**REQ, "to": "broadcast", "act": "inform", "payload": {"note": "x"}})
    clock = Clock()
    # 두 번째 대상(ra_eu) 기록 직전에 죽는다 — infra_t3610은 이미 기록됨
    _run_with_fault(hr, hive, clock, "deliver", target="ra_eu")
    assert len(_inbox(hive, "infra_t3610")) == 1 and _inbox(hive, "ra_eu") == []
    assert not (hive / "log.jsonl").exists()               # 실제 전달 확인 전에는 log에 없다
    journal = next((hive / ".router/journal").glob("*.json"))
    assert json.loads(journal.read_text())["delivered"] == ["infra_t3610"]
    res = _router(hr, hive, clock).run()                    # 재시작
    assert res.errors == []
    assert len(_inbox(hive, "infra_t3610")) == 1 and len(_inbox(hive, "ra_eu")) == 1   # 중복 없음
    log = _log(hive)
    assert len(log) == 1 and log[0]["payload"]["delivered_to"] == ["infra_t3610", "ra_eu"]
    _assert_log_valid(ve, hive)


def test_unwritable_target_inbox_is_escalated_not_silently_lost(hr, ve, hive):
    _outbox(hive, "ra_us", {**REQ, "to": "broadcast", "act": "inform", "payload": {"note": "x"}})
    bad = hive / "agents/ra_eu/inbox"
    bad.rmdir()
    bad.write_text("not a directory")                      # inbox 경로가 파일 → OSError
    res = _router(hr, hive).run()
    assert res.errors == []
    log = _log(hive)
    delivered = [e for e in log if e["kind"] == "handoff"][0]
    assert delivered["payload"]["delivered_to"] == ["infra_t3610"]
    esc = json.loads(_inbox(hive, "human")[0].read_text())
    assert esc["payload"]["reason"] == "undeliverable" and esc["payload"]["targets"] == ["ra_eu"]
    _assert_log_valid(ve, hive)


# ---------------------------------------------------------------- permissions / concurrency

def test_actor_is_taken_from_outbox_directory_not_payload(hr, hive):
    _outbox(hive, "ra_us", {**REQ, "actor": "ra_eu", "to": "infra_t3610", "id": "evt_20260909T000000_beef",
                            "hops": 7, "v": "9"})
    _router(hr, hive).run()
    ev = json.loads(_inbox(hive, "infra_t3610")[0].read_text())
    assert ev["actor"] == "ra_us" and ev["hops"] == 0 and ev["v"] == "2.1" and ev["id"] != "evt_20260909T000000_beef"


def test_outbox_outside_registry_is_ignored_and_reported(hr, hive):
    (hive / "agents/ghost/outbox").mkdir(parents=True)
    _outbox(hive, "ghost", REQ)
    res = _router(hr, hive).run()
    assert res.plans == [] and any("ghost" in e for e in res.errors)
    assert _inbox(hive, "ra_eu") == []


def test_tmp_files_are_ignored(hr, hive):
    (hive / "agents/ra_us/outbox/.tmp-123-ab").write_text(json.dumps(REQ))
    res = _router(hr, hive).run()
    assert res.plans == []


def test_lock_held_by_live_pid_refuses_and_stale_lock_is_taken_over(hr, hive):
    (hive / ".router").mkdir()
    (hive / ".router/lock").write_text(str(os.getpid()))
    with pytest.raises(hr.LockHeld):
        _router(hr, hive).run()
    (hive / ".router/lock").write_text("999999")           # 죽은 pid
    _outbox(hive, "ra_us", REQ)
    res = _router(hr, hive).run()
    assert res.errors == [] and not (hive / ".router/lock").exists()
    (hive / ".router/lock").write_text("garbage")
    with pytest.raises(hr.LockHeld):
        _router(hr, hive).run()                              # 손상된 lock은 삭제하지 않는다


def test_id_collision_is_reissued_and_retry_keeps_id(hr, hive, monkeypatch):
    _outbox(hive, "ra_us", REQ)
    clock = Clock()
    _router(hr, hive, clock).run()
    existing = _log(hive)[0]["id"]
    def hexes():
        yield existing[-4:]                                   # 첫 발급은 기존 id와 충돌
        while True:
            yield "cafe"                                      # 이후 tmp 파일명·conversation 등에도 쓰임
    gen = hexes()
    monkeypatch.setattr(hr.secrets, "token_hex", lambda n=2: next(gen))
    clock2 = Clock()
    clock2.t = clock.t - timedelta(seconds=2)               # 같은 초 스탬프가 나오도록
    _outbox(hive, "ra_eu", {**REQ, "to": "ra_us", "act": "query"}, name="20260909T120000-0002.json")
    r = _router(hr, hive, clock2, fault_at="before_archive")
    with pytest.raises(hr.InjectedFault):
        r.run()
    assigned = json.loads(next((hive / ".router/journal").glob("*cafe.json")).read_text())["id"]
    assert assigned != existing and assigned.endswith("cafe")
    _router(hr, hive, clock2).run()
    assert _log(hive)[-1]["id"] == assigned                  # 재시도해도 id 보존
