"""#65 — 트리거 달성 시 알림 경로 회귀 (네트워크 없음).

`n8n_webhook_url: null` 은 "알림 비활성" 정책이다(#65: 30일 유효 지표 전까지 임계값·webhook 을
null 로 둔다). 그런데 그 정책이 **코드로 지켜지는지** 고정한 시험이 없었다. null 인데 POST 가
나가면 아직 근거 없는 임계값으로 운영 알림을 울리게 되고, 반대로 설정했는데 안 나가면 임계
달성이 조용히 묻힌다. 두 방향을 모두 고정한다.
"""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "growth-metrics.py"


def _load():
    spec = importlib.util.spec_from_file_location("growth_metrics_notify", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["growth_metrics_notify"] = mod
    spec.loader.exec_module(mod)
    return mod


def _config(tmp_path, webhook, threshold=0.5):
    cfg = tmp_path / "growth-trigger-config.json"
    cfg.write_text(json.dumps({
        "notification": {"n8n_webhook_url": webhook},
        "triggers": {
            "t_low": {"metric": "correction_rate", "threshold": threshold,
                      "direction": "below", "next_action": "확인"},
        },
    }, ensure_ascii=False), encoding="utf-8")
    return cfg


METRICS = {"date": "2026-09-12", "metrics": {"correction_rate": {"value": 0.1}}}


class _Posted(list):
    def post(self, url, **kw):
        self.append((url, kw))
        raise AssertionError("webhook 이 null 인데 POST 가 나갔다")


def test_null_webhook_sends_no_request(tmp_path, monkeypatch):
    """임계 달성은 화면에 알리되, webhook 이 null 이면 전송하지 않는다."""
    m = _load()
    monkeypatch.setattr(m, "TRIGGER_CONFIG", _config(tmp_path, None))
    posted = _Posted()
    monkeypatch.setattr(m.requests, "post", posted.post)

    m.check_and_notify_triggers(METRICS)          # 예외 없이 끝나야 한다
    assert posted == [], "null 정책인데 알림이 전송됐다"


def test_configured_webhook_receives_triggered_payload(tmp_path, monkeypatch):
    """설정돼 있으면 달성 트리거가 실려 나가야 한다 — 조용히 묻히면 안 된다."""
    m = _load()
    monkeypatch.setattr(m, "TRIGGER_CONFIG", _config(tmp_path, "http://n8n.invalid/hook"))
    sent = []

    class _Resp:
        def raise_for_status(self): return None

    monkeypatch.setattr(m.requests, "post", lambda url, **kw: (sent.append((url, kw)), _Resp())[1])
    m.check_and_notify_triggers(METRICS)

    assert len(sent) == 1, "설정된 webhook 으로 전송되지 않았다"
    url, kw = sent[0]
    assert url == "http://n8n.invalid/hook"
    body = kw["json"]
    assert body["event"] == "growth_trigger_activated"
    assert [t["trigger"] for t in body["triggers"]] == ["t_low"]
    assert body["triggers"][0]["value"] == 0.1


def test_threshold_null_never_triggers(tmp_path, monkeypatch):
    """threshold 가 null 이면 그 트리거는 판정 대상이 아니다 (#65 정책)."""
    m = _load()
    monkeypatch.setattr(m, "TRIGGER_CONFIG", _config(tmp_path, "http://n8n.invalid/hook",
                                                     threshold=None))
    posted = _Posted()
    monkeypatch.setattr(m.requests, "post", posted.post)
    m.check_and_notify_triggers(METRICS)
    assert posted == [], "threshold null 인데 알림이 나갔다"
