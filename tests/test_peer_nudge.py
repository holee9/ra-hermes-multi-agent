"""SPEC-DEVCOMM-001 M3 발신 nudge 회귀 (네트워크 없음).

이 계층은 **지연 단축용**이다. 폴링(M2)이 5분 백스톱이므로, 실패해도 호출자(코멘트 작성)를
깨뜨리면 안 된다. 세 가지를 고정한다: 미설정 no-op(AC-5), 성공 경로, 그리고 어떤 오류에서도
예외가 올라가지 않는 것.
"""
import importlib.util
import json
import sys
import urllib.error
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "peer_nudge.py"


def _load():
    spec = importlib.util.spec_from_file_location("peer_nudge_test", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["peer_nudge_test"] = mod
    spec.loader.exec_module(mod)
    return mod


class _Resp:
    status = 204

    def __enter__(self): return self
    def __exit__(self, *a): return False


def test_no_url_is_silent_noop(monkeypatch):
    """PEER_NUDGE_URL 미설정은 정상 상태다 — 호출도, 경고도 없다 (REQ-DC-006 / AC-5)."""
    m = _load()
    monkeypatch.delenv("PEER_NUDGE_URL", raising=False)
    called = []
    monkeypatch.setattr(m.urllib.request, "urlopen", lambda *a, **k: called.append(1))
    assert m.notify_peer(143, "https://x/issues/143#c1") == "disabled"
    assert called == [], "미설정인데 요청이 나갔다"


def test_missing_key_does_not_send(monkeypatch):
    """수신부가 Bearer 를 요구하므로 키 없이 보내면 401 만 만든다 — 보내지 않는다."""
    m = _load()
    monkeypatch.setenv("PEER_NUDGE_URL", "http://pi.invalid/v1/peer/notify")
    monkeypatch.delenv("API_SERVER_KEY", raising=False)
    called = []
    monkeypatch.setattr(m.urllib.request, "urlopen", lambda *a, **k: called.append(1))
    assert m.notify_peer(143, "https://x/issues/143#c1") == "no_key"
    assert called == []


def _armed(monkeypatch, m):
    monkeypatch.setenv("PEER_NUDGE_URL", "http://pi.invalid/v1/peer/notify")
    monkeypatch.setenv("API_SERVER_KEY", "k")


def test_sends_four_field_schema_with_bearer(monkeypatch):
    m = _load()
    _armed(monkeypatch, m)
    seen = {}

    def fake(req, timeout=None):
        seen["url"] = req.full_url
        seen["auth"] = req.headers.get("Authorization")
        seen["body"] = json.loads(req.data.decode("utf-8"))
        return _Resp()

    monkeypatch.setattr(m.urllib.request, "urlopen", fake)
    assert m.notify_peer(143, "https://x/issues/143#c1", "t3610", "본문") == "sent"
    assert seen["auth"] == "Bearer k"
    assert set(seen["body"]) == {"issue", "comment_url", "author", "body"}
    assert seen["body"]["issue"] == 143 and isinstance(seen["body"]["issue"], int)


def test_transient_failure_retries_then_gives_up_without_raising(monkeypatch):
    """3회까지 시도하고, 실패해도 예외를 올리지 않는다 — 폴링이 복구한다."""
    m = _load()
    _armed(monkeypatch, m)
    attempts = []

    def boom(req, timeout=None):
        attempts.append(1)
        raise urllib.error.URLError("down")

    monkeypatch.setattr(m.urllib.request, "urlopen", boom)
    assert m.notify_peer(143, "https://x/issues/143#c1").startswith("failed:")
    assert len(attempts) == m.MAX_ATTEMPTS


def test_client_error_is_not_retried(monkeypatch):
    """400 대역은 재시도해도 같은 결과다 — 한 번만 시도한다."""
    m = _load()
    _armed(monkeypatch, m)
    attempts = []

    def bad(req, timeout=None):
        attempts.append(1)
        raise urllib.error.HTTPError(req.full_url, 400, "bad schema", {}, None)

    monkeypatch.setattr(m.urllib.request, "urlopen", bad)
    assert m.notify_peer(143, "https://x/issues/143#c1") == "failed:http_400"
    assert len(attempts) == 1, "4xx 에 재시도했다"


def test_body_is_truncated_not_dropped(monkeypatch):
    m = _load()
    _armed(monkeypatch, m)
    seen = {}
    monkeypatch.setattr(m.urllib.request, "urlopen",
                        lambda req, timeout=None: (seen.update(json.loads(req.data)), _Resp())[1])
    m.notify_peer(143, "https://x/issues/143#c1", "t3610", "가" * 5000)
    assert len(seen["body"]) == 2000
