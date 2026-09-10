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
                    sink=sink, handled=handled, now=lambda: NOW)


def test_no_source_means_unavailable_and_no_delivery(hive):
    _msg(hive, "ra_us")
    sent = []
    d = _drain(hive, sink=lambda a, f: sent.append(f) or True).run([hd.Peer("ra_us")])[0]
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
    d = _drain(hive, state=hd.GateState("idle", NOW), sink=lambda a, f: sent.append((a, f)) or True).run([peer])[0]
    assert d.action == "deliver" and sent == [("ra_us", p)] and peer.last_written == mid


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
    d = _drain(hive, state=hd.GateState("idle", NOW), sink=lambda a, f: False).run([peer])[0]
    assert d.action == "hold" and d.reason == "sink-refused" and peer.last_written is None


def test_cli_dry_run_never_delivers(hive, capsys):
    _msg(hive, "ra_us")
    assert hd.main([str(hive), "--peer", "ra_us", "--peer", "ra_eu"]) == 0
    lines = [json.loads(line) for line in capsys.readouterr().out.strip().splitlines()]
    assert lines[0]["action"] == "hold" and lines[0]["reason"] == "state-unavailable"
    assert lines[1]["action"] == "none"
