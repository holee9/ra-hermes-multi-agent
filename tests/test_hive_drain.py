"""delivery-gate §3/§3.1/§4/§5.1/§6 판정 회귀 — tools/hive_drain.py (P3-2).

Hermes는 없다: 상태 소스·sink는 가짜 콜러블. 이 파일은 '긴 턴 무로그에서 전달 안 함'을
'소스가 idle을 주지 않으면 전달 안 함'으로 검증한다 — 로그를 읽는 경로 자체가 없다.
"""
import importlib.util
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load():
    spec = importlib.util.spec_from_file_location("hive_drain", ROOT / "tools" / "hive_drain.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["hive_drain"] = mod
    spec.loader.exec_module(mod)
    return mod


hd = _load()
NOW = datetime(2026, 9, 10, 12, 0, 0, tzinfo=timezone.utc)


@pytest.fixture
def hive(tmp_path):
    for a in ("ra_us", "ra_eu"):
        (tmp_path / "agents" / a / "inbox").mkdir(parents=True)
    return tmp_path


def _msg(hive, actor, n=1, manual=False, mid=None):
    mid = mid or f"evt_20260910T120000_{n:04x}"
    p = hive / "agents" / actor / "inbox" / f"20260910T12000{n}p0900-{mid}.json"
    p.write_text(json.dumps({"id": mid, "kind": "handoff", **({"manual": True} if manual else {})}))
    return p, mid


def _drain(hive, state=None, sink=None, handled=lambda _id: False, cfg=None):
    return hd.Drain(hive, cfg=cfg or hd.Config(), source=(lambda actor: state) if state is not None else None,
                    sink=sink, handled=handled, now=lambda: NOW, execute=True)


def test_no_source_means_unavailable_and_no_delivery(hive):
    _msg(hive, "ra_us")
    sent = []
    d = _drain(hive, sink=lambda a, i, b, t: sent.append(i) or True).run([hd.Peer("ra_us")])[0]
    assert d.action == "hold" and d.reason == "state-unavailable" and sent == []


@pytest.mark.parametrize("value", ["busy", "unknown", "garbage"])
def test_non_idle_states_hold(hive, value):
    _msg(hive, "ra_us")
    d = _drain(hive, state=hd.GateState(value, NOW)).run([hd.Peer("ra_us")])[0]
    assert d.action == "hold" and d.reason.startswith("state-")


def test_idle_older_than_max_age_is_stale(hive):
    _msg(hive, "ra_us")
    d = _drain(hive, state=hd.GateState("idle", NOW - timedelta(seconds=31))).run([hd.Peer("ra_us")])[0]
    assert d.reason == "state-stale"


def test_idle_without_timestamp_is_unknown(hive):
    _msg(hive, "ra_us")
    d = _drain(hive, state=hd.GateState("idle", None)).run([hd.Peer("ra_us")])[0]
    assert d.reason == "state-unknown"


def test_idle_delivers_and_records_last_written(hive):
    p, mid = _msg(hive, "ra_us")
    sent = []
    peer = hd.Peer("ra_us")
    d = _drain(hive, state=hd.GateState("idle", NOW), sink=lambda a, i, b, t: sent.append((a, i)) or True).run([peer])[0]
    assert d.action == "deliver" and sent == [("ra_us", mid)] and peer.last_written == mid


def test_turn_spacing_waits_for_handled_even_when_idle(hive):
    """§3 턴 단위 간격: 직전 분이 handled 확인 전이면 idle이어도 다음 메시지를 넣지 않는다."""
    _msg(hive, "ra_us", 2)
    peer = hd.Peer("ra_us", last_written="evt_prev")
    d = _drain(hive, state=hd.GateState("idle", NOW)).run([peer])[0]
    assert d.action == "hold" and d.reason == "awaiting-handled:evt_prev"
    d = _drain(hive, state=hd.GateState("idle", NOW), handled=lambda i: i == "evt_prev").run([peer])[0]
    assert d.action == "deliver"


def test_manual_bypasses_pause_only(hive):
    _msg(hive, "ra_us", manual=True)
    peer = hd.Peer("ra_us", paused=True)
    assert _drain(hive, state=hd.GateState("idle", NOW)).run([peer])[0].action == "deliver"
    assert _drain(hive, state=hd.GateState("busy", NOW)).run([peer])[0].reason == "state-busy"      # idle은 우회 못 함
    peer.breaker = "stopped"
    assert _drain(hive, state=hd.GateState("idle", NOW)).run([peer])[0].reason == "breaker-stopped"


def test_paused_without_manual_holds(hive):
    _msg(hive, "ra_us")
    d = _drain(hive, state=hd.GateState("idle", NOW)).run([hd.Peer("ra_us", paused=True)])[0]
    assert d.reason == "paused"


def test_boot_grace_holds(hive):
    _msg(hive, "ra_us")
    cfg = hd.Config(grace=timedelta(seconds=60))
    d = _drain(hive, state=hd.GateState("idle", NOW), cfg=cfg).run([hd.Peer("ra_us", booted_at=NOW - timedelta(seconds=10))])[0]
    assert d.reason == "boot-grace"


def test_manual_goes_first_then_arrival_order(hive):
    _msg(hive, "ra_us", 1)
    _msg(hive, "ra_us", 2)
    pm, mm = _msg(hive, "ra_us", 3, manual=True)
    assert hd.next_message(hive / "agents/ra_us/inbox") == (pm, mm)
    pm.unlink()
    assert hd.next_message(hive / "agents/ra_us/inbox")[1].endswith("0001")


def test_non_conforming_names_and_tmp_are_ignored(hive):
    inbox = hive / "agents/ra_us/inbox"
    (inbox / "notes.json").write_text("{}")
    (inbox / ".tmp-20260910T120001p0900-evt_x.json").write_text("{}")
    assert hd.next_message(inbox) is None


def test_per_batch_limit_without_accept_contract(hive):
    """수신측 accept 계약이 없으면 peer당 배치 1건 — 조회 후 연속 투입 금지(§3.1)."""
    _msg(hive, "ra_us", 1)
    st = hd.GateState("idle", NOW)
    d1 = hd.decide(hd.Peer("ra_us"), st, hd.next_message(hive / "agents/ra_us/inbox"), NOW, hd.Config(),
                   handled=lambda _i: True, delivered_this_batch=1)
    assert d1.action == "hold" and d1.reason == "per-batch-limit"
    d2 = hd.decide(hd.Peer("ra_us"), hd.GateState("idle", NOW, accept_token="tok"),
                   hd.next_message(hive / "agents/ra_us/inbox"), NOW, hd.Config(), handled=lambda _i: True, delivered_this_batch=1)
    assert d2.action == "deliver"


def test_sink_refusal_is_hold_not_written(hive):
    """수신측이 거절(reject-busy)하면 written으로 기록하지 않는다."""
    _msg(hive, "ra_us")
    peer = hd.Peer("ra_us")
    d = _drain(hive, state=hd.GateState("idle", NOW), sink=lambda a, i, b, t: False).run([peer])[0]
    assert d.action == "hold" and d.reason == "sink-refused" and peer.last_written is None


def test_cli_dry_run_never_delivers(hive, capsys):
    _msg(hive, "ra_us")
    assert hd.main([str(hive), "--peer", "ra_us", "--peer", "ra_eu"]) == 0
    lines = [json.loads(line) for line in capsys.readouterr().out.strip().splitlines()]
    assert lines[0]["action"] == "hold" and lines[0]["reason"] == "state-unavailable"
    assert lines[1]["action"] == "none"


# ---------------------------------------------------------------- codex 사전검토 3점 (P3-2)

def test_source_exception_is_unknown_hold_not_crash(hive):
    _msg(hive, "ra_us")
    _msg(hive, "ra_eu")

    def boom(actor):
        if actor == "ra_us":
            raise RuntimeError("socket down")
        return hd.GateState("idle", NOW)
    sent = []
    res = hd.Drain(hive, source=boom, sink=lambda a, i, b, t: sent.append(a) or True, now=lambda: NOW, execute=True).run(
        [hd.Peer("ra_us"), hd.Peer("ra_eu")])
    assert res[0].action == "hold" and res[0].reason.startswith("state-unknown:RuntimeError")
    assert res[1].action == "deliver" and sent == ["ra_eu"]                # 다른 peer는 계속 처리


@pytest.mark.parametrize("ts", [NOW.replace(tzinfo=None), NOW + timedelta(seconds=5), "2026-09-10"])
def test_naive_future_or_garbage_timestamp_is_unknown(hive, ts):
    _msg(hive, "ra_us")
    d = _drain(hive, state=hd.GateState("idle", ts)).run([hd.Peer("ra_us")])[0]
    assert d.reason == "state-unknown"


def test_accept_token_reaches_sink_and_is_journaled(hive):
    _, mid = _msg(hive, "ra_us")
    got = []
    hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW, accept_token="tok-7"),
             sink=lambda a, i, b, t: got.append(t) or True, now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])
    assert got == ["tok-7"]
    j = json.loads((hive / ".drain" / "ra_us.json").read_text())
    assert j["written"][mid] == {"ts": NOW.isoformat(timespec="seconds"), "accept_token": "tok-7", "status": "written"}


def test_written_message_is_never_reselected_and_moves_to_done_after_handled(hive):
    """codex 3점: sink 성공 후 파일이 남아도 재선택·재전달하지 않는다. handled 뒤 .done/ 정리. 재시작은 저널 기준."""
    p1, m1 = _msg(hive, "ra_us", 1)
    p2, m2 = _msg(hive, "ra_us", 2)
    sent = []
    mk = lambda handled: hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW),  # noqa: E731
                                  sink=lambda a, i, b, t: sent.append(i) or True, handled=handled, now=lambda: NOW, execute=True)
    assert mk(lambda i: False).run([hd.Peer("ra_us")])[0].action == "deliver" and sent == [m1]
    d = mk(lambda i: False).run([hd.Peer("ra_us")])[0]                       # 새 프로세스(새 Peer): 저널이 정본
    assert d.action == "hold" and d.reason == f"awaiting-handled:{m1}" and sent == [m1]
    d = mk(lambda i: i == m1).run([hd.Peer("ra_us")])[0]                      # m1 handled → .done, m2 전달
    assert (hive / "agents/ra_us/inbox/.done" / p1.name).exists() and not p1.exists()
    assert d.action == "deliver" and d.msg_id == m2 and sent == [m1, m2]
    _msg(hive, "ra_us", 3)
    d = mk(lambda i: i == m1).run([hd.Peer("ra_us")])[0]
    assert d.reason == f"awaiting-handled:{m2}" and sent == [m1, m2]  # m2 재전달 없음, m3 대기


def test_router_inbox_output_feeds_drain(tmp_path):
    """연결 회귀: P2 라우터가 실제로 쓴 inbox 파일을 drain이 선택하고, 소스 없이는 전달하지 않는다."""
    spec = importlib.util.spec_from_file_location("hive_router_for_drain", ROOT / "tools" / "hive_router.py")
    hr = importlib.util.module_from_spec(spec)
    sys.modules["hive_router_for_drain"] = hr
    spec.loader.exec_module(hr)
    root = tmp_path / "ra-hive"
    (root / "registry").mkdir(parents=True)
    (root / "registry" / "actors.json").write_text(json.dumps({"version": 1, "actors": {
        "ra_us": {"workspace": "work", "status": "active"}, "ra_eu": {"workspace": "work", "status": "active"}}}))
    for a in ("ra_us", "ra_eu", "human"):
        (root / "agents" / a / "outbox").mkdir(parents=True)
        (root / "agents" / a / "inbox").mkdir(parents=True)
    (root / "agents/ra_us/outbox/20260910T120000-0001.json").write_text(json.dumps(
        {"kind": "handoff", "case": {"wp": 1, "regime": "US"}, "to": "ra_eu", "act": "request",
         "payload": {"to_actor": "ra_eu", "reason": "x"}, "corr": None, "conversation": None}))
    clock = iter(datetime(2026, 9, 10, 12, 0, s, tzinfo=timezone.utc) for s in range(1, 60))
    res = hr.HiveRouter(root, now=lambda: next(clock), hop_cap=12, execute=True).run()
    assert res.errors == [] and res.plans[0].outcome == "deliver"
    inbox_files = sorted((root / "agents/ra_eu/inbox").glob("*.json"))
    assert len(inbox_files) == 1
    sel = hd.next_message(root / "agents/ra_eu/inbox")
    assert sel is not None and sel[0] == inbox_files[0] and sel[1] == res.plans[0].msg_id
    d = hd.Drain(root, now=lambda: NOW).run([hd.Peer("ra_eu")])[0]            # 소스 미주입
    assert d.action == "hold" and d.reason == "state-unavailable" and inbox_files[0].exists()
    sent = []
    d = hd.Drain(root, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: sent.append(i) or True,
                 now=lambda: NOW, execute=True).run([hd.Peer("ra_eu")])[0]
    assert d.action == "deliver" and sent == [res.plans[0].msg_id]


# ---------------------------------------------------------------- codex 재현 2건 (b777b13)

def test_dry_run_writes_nothing_and_calls_no_sink(hive, capsys):
    """P2: 기본(dry-run)은 .drain 저널·.done 이동·sink 호출이 없다."""
    _msg(hive, "ra_us")
    before = sorted(str(p) for p in hive.rglob("*"))
    called = []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, f, i, t: called.append(f) or True,
                 handled=lambda i: True, now=lambda: NOW).run([hd.Peer("ra_us")])[0]
    assert d.action == "deliver" and called == []                              # 판정만
    assert sorted(str(p) for p in hive.rglob("*")) == before and not (hive / ".drain").exists()
    hd.main([str(hive), "--peer", "ra_us"])
    assert not (hive / ".drain").exists()


def test_save_failure_after_sink_never_resubmits(hive, monkeypatch):
    """P1: sink True → 저널 저장 OSError → 재시작. sink는 총 1회. lookup 없으면 ambiguous 보류, lookup으로만 복구."""
    p1, m1 = _msg(hive, "ra_us", 1)
    calls = []
    mk = lambda lookup=None: hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW),  # noqa: E731
                                     sink=lambda a, i, b, t: calls.append(i) or True, lookup=lookup,
                                     now=lambda: NOW, execute=True)
    dr = mk()
    real_save = dr._save
    n = {"k": 0}

    def flaky(actor, j):
        n["k"] += 1
        if n["k"] == 2:                                                       # submitting 영속(1) 뒤, 결과 저장(2)에서 실패
            raise OSError("disk full")
        real_save(actor, j)
    monkeypatch.setattr(dr, "_save", flaky)
    with pytest.raises(OSError):
        dr.run([hd.Peer("ra_us")])
    assert calls == [m1]
    j = json.loads((hive / ".drain/ra_us.json").read_text())
    assert j["written"][m1]["status"] == "submitting"
    d = mk().run([hd.Peer("ra_us")])[0]                                       # 재시작, lookup 없음
    assert d.action == "hold" and d.reason == f"ambiguous-submit:{m1}" and calls == [m1]
    d = mk(lookup=lambda a, i: True).run([hd.Peer("ra_us")])[0]                # 수신측이 받았음 → written 확정
    assert calls == [m1]
    j = json.loads((hive / ".drain/ra_us.json").read_text())
    assert j["written"][m1]["status"] == "written" and j["last_written"] == m1
    assert d.reason == f"awaiting-handled:{m1}" or d.action == "none"


def test_lookup_false_allows_normal_resubmission(hive, monkeypatch):
    p1, m1 = _msg(hive, "ra_us", 1)
    (hive / ".drain").mkdir()
    (hive / ".drain/ra_us.json").write_text(json.dumps({"written": {m1: {"ts": "x", "accept_token": None,
                                                                          "status": "submitting"}}, "last_written": None}))
    calls = []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(i) or True,
                 lookup=lambda a, i: False, now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])[0]
    assert d.action == "deliver" and calls == [m1]                            # 수신측에 없음 → 정상 재판정 후 1회 전달


# ---------------------------------------------------------------- codex 재현 (9aee12c): 동시 실행·내구성

def test_second_process_is_refused_while_lock_held(hive):
    """단일 소유: lock 보유 중 두 번째 drain(execute)은 거부되고 sink를 부르지 않는다."""
    _msg(hive, "ra_us")
    holder = hd.Drain(hive, execute=True)
    holder.acquire_lock()
    calls = []
    try:
        with pytest.raises(hd.DrainError):
            hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(i) or True,
                     now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])
    finally:
        holder.release_lock()
    assert calls == []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(i) or True,
                 now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])[0]   # 해제 후 정상
    assert d.action == "deliver" and len(calls) == 1
    assert not (hive / ".drain/lock").exists() or True                      # lock 파일은 남아도 flock은 해제됨
    holder2 = hd.Drain(hive, execute=True)
    holder2.acquire_lock()                                                   # 재획득 가능 = 해제 확인
    holder2.release_lock()


def test_dry_run_takes_no_lock(hive):
    holder = hd.Drain(hive, execute=True)
    holder.acquire_lock()
    try:
        _msg(hive, "ra_us")
        assert hd.Drain(hive, now=lambda: NOW).run([hd.Peer("ra_us")])[0].reason == "state-unavailable"
    finally:
        holder.release_lock()


def test_sink_receives_explicit_msg_id(hive):
    _, mid = _msg(hive, "ra_us")
    got = []
    hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: got.append(i) or True,
             now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])
    assert got == [mid]


@pytest.mark.parametrize("content", ["{not json", "[]", json.dumps({"written": "x"})])
def test_corrupt_journal_holds_actor_without_overwrite(hive, content):
    _msg(hive, "ra_us")
    (hive / ".drain").mkdir()
    (hive / ".drain/ra_us.json").write_text(content)
    calls = []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(i) or True,
                 now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])[0]
    assert d.action == "hold" and d.reason == "journal-corrupt" and calls == []
    assert (hive / ".drain/ra_us.json").read_text() == content                # 덮어쓰지 않음


def test_journal_save_uses_fsync(hive, monkeypatch):
    _msg(hive, "ra_us")
    synced = []
    real = hd.os.fsync
    monkeypatch.setattr(hd.os, "fsync", lambda fd: synced.append(fd) or real(fd))
    hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: True,
             now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])
    assert len(synced) >= 2                                                  # 파일 + 디렉터리


# ---------------------------------------------------------------- codex 재현 (360cd45): 경로 이탈

def test_symlinked_lock_outside_root_is_refused(hive, tmp_path):
    """`.drain/lock` → root 밖 파일 symlink: run([])만으로 외부 파일이 덮어써지던 결함."""
    outside = tmp_path.parent / f"{tmp_path.name}-preserve.txt"
    outside.write_text("keep me")
    (hive / ".drain").mkdir()
    (hive / ".drain/lock").symlink_to(outside)
    with pytest.raises(hd.DrainError):
        hd.Drain(hive, execute=True).run([])
    assert outside.read_text() == "keep me"


def test_symlinked_drain_dir_outside_root_is_refused(hive, tmp_path):
    ext = tmp_path.parent / f"{tmp_path.name}-ext"
    ext.mkdir()
    (hive / ".drain").symlink_to(ext)
    with pytest.raises(hd.DrainError):
        hd.Drain(hive, execute=True).run([])
    assert list(ext.iterdir()) == []


def test_symlinked_journal_is_held_not_read_or_written(hive, tmp_path):
    _msg(hive, "ra_us")
    outside = tmp_path.parent / f"{tmp_path.name}-journal.json"
    outside.write_text(json.dumps({"written": {}, "last_written": None}))
    (hive / ".drain").mkdir()
    (hive / ".drain/ra_us.json").symlink_to(outside)
    calls = []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(i) or True,
                 now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])[0]
    assert d.action == "hold" and d.reason == "journal-corrupt" and calls == []
    assert json.loads(outside.read_text()) == {"written": {}, "last_written": None}


def test_symlinked_inbox_file_is_not_handed_to_sink(hive, tmp_path):
    outside = tmp_path.parent / f"{tmp_path.name}-secret.json"
    outside.write_text(json.dumps({"id": "evt_x"}))
    link = hive / "agents/ra_us/inbox/20260910T120001p0900-evt_20260910T120000_0001.json"
    link.symlink_to(outside)
    calls = []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(i) or True,
                 now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])[0]
    assert d.action == "none" and calls == []                                # 후보에서 제외


def test_symlinked_inbox_dir_outside_root_is_held(hive, tmp_path):
    ext = tmp_path.parent / f"{tmp_path.name}-inbox"
    ext.mkdir()
    (ext / "20260910T120001p0900-evt_20260910T120000_0001.json").write_text(json.dumps({"id": "evt_x"}))
    inbox = hive / "agents/ra_us/inbox"
    inbox.rmdir()
    inbox.symlink_to(ext)
    calls = []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(i) or True,
                 now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])[0]
    assert d.action == "hold" and d.reason.startswith("path-escape") and calls == []


def test_done_dir_symlink_outside_root_blocks_settle(hive, tmp_path):
    p1, m1 = _msg(hive, "ra_us", 1)
    ext = tmp_path.parent / f"{tmp_path.name}-done"
    ext.mkdir()
    (hive / "agents/ra_us/inbox/.done").symlink_to(ext)
    (hive / ".drain").mkdir()
    (hive / ".drain/ra_us.json").write_text(json.dumps({"written": {m1: {"ts": "x", "accept_token": None,
                                                                          "status": "written"}}, "last_written": m1}))
    with pytest.raises(hd.DrainError):
        hd.Drain(hive, handled=lambda i: True, now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])
    assert p1.exists() and list(ext.iterdir()) == []


# ---------------------------------------------------------------- codex 리뷰 (b93c5a2): sink 인계 경계

def test_sink_receives_verified_bytes_not_path(hive):
    p, mid = _msg(hive, "ra_us")
    got = []
    hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: got.append(b) or True,
             now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])
    assert got == [p.read_bytes()] and isinstance(got[0], bytes)


def test_payload_id_must_match_filename_id(hive):
    inbox = hive / "agents/ra_us/inbox"
    (inbox / "20260910T120001p0900-evt_20260910T120000_0001.json").write_text(json.dumps({"id": "evt_other"}))
    calls = []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(i) or True,
                 now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])[0]
    assert d.action == "hold" and d.reason == "payload-mismatch" and calls == []
    assert not (hive / ".drain/ra_us.json").exists() or "evt_" not in (hive / ".drain/ra_us.json").read_text()


def test_file_swapped_to_symlink_after_selection_is_not_delivered(hive, tmp_path, monkeypatch):
    """검사 후 교체: 후보 선택 뒤 sink 전에 파일이 외부 symlink로 바뀌어도 외부 내용은 인계되지 않는다."""
    p, mid = _msg(hive, "ra_us")
    outside = tmp_path.parent / f"{tmp_path.name}-swap.json"
    outside.write_text(json.dumps({"id": mid, "kind": "evil"}))
    real = hd.next_message

    def swap(inbox, exclude=frozenset()):
        r = real(inbox, exclude)
        p.unlink()
        p.symlink_to(outside)
        return r
    monkeypatch.setattr(hd, "next_message", swap)
    calls = []
    d = hd.Drain(hive, source=lambda a: hd.GateState("idle", NOW), sink=lambda a, i, b, t: calls.append(b) or True,
                 now=lambda: NOW, execute=True).run([hd.Peer("ra_us")])[0]
    assert d.action == "hold" and d.reason == "payload-mismatch" and calls == []
