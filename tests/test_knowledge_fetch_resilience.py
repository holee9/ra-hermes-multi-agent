"""Layer 4 외부 API 파서가 비정상 응답에서 죽지 않는지 고정 (네트워크 없음).

이 파서들은 규제 자문의 근거 자료를 만든다. 외부 API(openFDA·data.go.kr·law.go.kr·
MFDS RSS·CDRH RSS·MDCG)가 예상 밖 형태를 돌려줬을 때 예외로 죽으면 자문 경로 전체가
근거 없이 진행되거나 중단된다. 현재 구현은 전부 빈 목록으로 우아하게 물러난다 —
그 성질을 회귀로 박아 둔다(지금은 이 파일이 유일한 커버리지다).
"""
import importlib.util
import inspect
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "knowledge_fetch.py"

PARSERS = ["fetch_openfda", "fetch_data_go_kr", "fetch_law_kr",
           "fetch_mfds_notices", "fetch_cdrh_guidance_rss", "fetch_mdcg_guidance"]

MALFORMED = {
    "top_level_list": b"[1,2]",
    "top_level_string": b'"oops"',
    "top_level_number": b"123",
    "field_is_string": (b'{"results":"x","body":{"items":"x"},'
                        b'"LawSearch":{"law":"x"},"header":{"resultCode":"00"}}'),
    "null_fields": b'{"results":null,"body":null,"LawSearch":null}',
    "empty_body": b"",
    "not_json": b"<html>503 Service Unavailable</html>",
    "truncated_json": b'{"results":[{"id":',
}


def _load():
    spec = importlib.util.spec_from_file_location("knowledge_fetch_res", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["knowledge_fetch_res"] = mod
    spec.loader.exec_module(mod)
    # 키가 비어 있으면 세 파서가 _http_get 전에 [] 로 빠져 시험이 공허해진다 — 가짜 키로 경로를 연다.
    mod.OPENFDA_API_KEY = mod.DATA_GO_KR_API_KEY = mod.LAW_GO_KR_OC = "test-key"
    return mod


def _call(fn):
    """첫 인자가 query 인 파서와 top 만 받는 파서를 구분해 호출한다."""
    params = list(inspect.signature(fn).parameters)
    # 제품명(체온계)이 있어야 data.go.kr 도 요청 단계까지 간다 — 없으면 공허한 시험이 된다.
    return fn("체온계 의료기기 허가") if params and params[0] != "top" else fn()


@pytest.mark.parametrize("name", PARSERS)
@pytest.mark.parametrize("label", sorted(MALFORMED))
def test_parser_degrades_instead_of_raising(monkeypatch, name, label):
    m = _load()
    monkeypatch.setattr(m, "_http_get", lambda *a, **k: MALFORMED[label])
    out = _call(getattr(m, name))
    assert isinstance(out, list), f"{name} 이 {label} 에서 리스트를 돌려주지 않았다: {type(out)}"


@pytest.mark.parametrize("name", PARSERS)
def test_parser_returns_empty_on_transport_failure(monkeypatch, name):
    """_http_get 이 None(요청 실패)이어도 예외가 아니라 빈 결과여야 한다."""
    m = _load()
    monkeypatch.setattr(m, "_http_get", lambda *a, **k: None)
    assert _call(getattr(m, name)) == []


@pytest.mark.parametrize("name", PARSERS)
def test_parser_does_not_swallow_programming_errors(monkeypatch, name):
    """반대편: 전송 계층이 예외를 던지면 그대로 드러나야 한다 — 조용한 성공으로 감추지 않는다."""
    m = _load()

    def boom(*a, **k):
        raise MemoryError("주입")
    monkeypatch.setattr(m, "_http_get", boom)
    with pytest.raises(MemoryError):
        _call(getattr(m, name))
