"""P3-0 (5) 스레드 재구성 빌더 회귀 — tools/hive_thread.py. LLM 호출 없음, 목업 log 사용."""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load():
    spec = importlib.util.spec_from_file_location("hive_thread", ROOT / "tools" / "hive_thread.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["hive_thread"] = mod
    spec.loader.exec_module(mod)
    return mod


ht = _load()
MOCK = [json.loads(x) for x in (ROOT / "virtual-office/mock/events-v2.1.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]


def _ev(i, actor, conv=None, corr=None, ts=None, **kw):
    return {"v": "2.1", "id": f"evt_{i:04d}", "ts": ts or f"2026-09-10T09:{i:02d}:00+09:00", "workspace": "work",
            "actor": actor, "kind": kw.pop("kind", "handoff"), "payload": kw.pop("payload", {"n": i}),
            **({"conversation": conv} if conv else {}), **({"corr": corr} if corr else {}), **kw}


def test_thread_from_mock_log_is_ordered_and_past_only():
    target = next(r for r in MOCK if r.get("conversation") == "conv_1042_matching" and r.get("corr"))
    t = ht.collect(MOCK, target["id"])
    assert t.conversation == "conv_1042_matching" and t.events[-1]["id"] == target["id"]
    assert all(r["ts"] <= target["ts"] for r in t.events)
    assert [r["id"] for r in t.events] == sorted((r["id"] for r in t.events), key=lambda i: next(x["ts"] for x in MOCK if x["id"] == i))
    assert t.chars == len(t.context) and t.est_tokens == t.chars // 4 and t.sources == [r["id"] for r in t.events]


def test_later_events_in_same_conversation_are_excluded():
    recs = [_ev(1, "ra_us", "c"), _ev(2, "ra_eu", "c", corr="evt_0001"), _ev(3, "ra_us", "c", corr="evt_0002")]
    t = ht.collect(recs, "evt_0002")
    assert [r["id"] for r in t.events] == ["evt_0001", "evt_0002"]


def test_corr_chain_without_conversation_is_followed():
    recs = [_ev(1, "ra_us"), _ev(2, "ra_eu", corr="evt_0001"), _ev(3, "ra_us", corr="evt_0002")]
    t = ht.collect(recs, "evt_0003")
    assert t.conversation is None and [r["id"] for r in t.events] == ["evt_0001", "evt_0002", "evt_0003"]


def test_max_events_truncates_oldest_and_reports():
    recs = [_ev(i, "ra_us", "c") for i in range(1, 21)]
    t = ht.collect(recs, "evt_0020", max_events=5)
    assert len(t.events) == 5 and t.truncated == 15 and t.events[0]["id"] == "evt_0016"
    assert t.context.startswith("[이전 15개 항목 생략")


def test_payload_is_serialized_verbatim_and_refs_untouched():
    recs = [_ev(1, "ra_us", "c", payload={"text_ref": "op://wp/1/c1", "b": [1, 2]})]
    t = ht.collect(recs, "evt_0001")
    assert '"text_ref": "op://wp/1/c1"' in t.context and '"b": [1, 2]' in t.context


def test_unknown_target_raises():
    with pytest.raises(KeyError):
        ht.collect(MOCK, "evt_nope")


def test_cli_json_report(tmp_path, capsys):
    log = tmp_path / "log.jsonl"
    log.write_text("\n".join(json.dumps(r) for r in MOCK) + "\n{not json\n")
    target = next(r for r in MOCK if r.get("conversation") == "conv_1042_matching")
    assert ht.main([str(log), target["id"], "--json"]) == 0
    rep = json.loads(capsys.readouterr().out)
    assert rep["events"] >= 1 and rep["est_tokens_heuristic"] == rep["chars"] // 4 and "sources" in rep
