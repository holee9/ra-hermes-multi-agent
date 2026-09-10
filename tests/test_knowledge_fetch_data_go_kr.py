"""#37 — data.go.kr 조회가 질문의 품목 키워드를 공식 검색 파라미터로 싣는지 검증.

Network-free: _http_get is monkeypatched. codex 재현(main ac39857): 서로 다른 질문에 대해
요청 URL 3개가 모두 동일했고(serviceKey/type/numOfRows/pageNo만) 같은 첫 페이지가 반환됐다.
"""
import importlib.util
import json
import sys
import urllib.parse
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "knowledge_fetch.py"


def _load():
    spec = importlib.util.spec_from_file_location("knowledge_fetch_dgk", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["knowledge_fetch_dgk"] = mod
    spec.loader.exec_module(mod)
    return mod


kf = _load()


def _stub(monkeypatch, responder):
    calls = []

    def fake(url, headers=None, timeout=0):
        calls.append(url)
        return responder(url)

    monkeypatch.setattr(kf, "_http_get", fake)
    monkeypatch.setattr(kf, "DATA_GO_KR_API_KEY", "k")
    return calls


def _ok(items, nested=False):
    rows = [{"item": i} for i in items] if nested else items
    return json.dumps({"header": {"resultCode": "00"},
                       "body": {"items": rows, "totalCount": len(items)}}).encode()


def _params(url):
    return dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))


def test_different_queries_produce_different_search_requests(monkeypatch):
    calls = _stub(monkeypatch, lambda u: _ok([]))
    kf.fetch_data_go_kr("초음파진단기 품목허가")
    first = list(calls)
    calls.clear()
    kf.fetch_data_go_kr("치과용임플란트 품목허가")
    second = list(calls)
    assert first and second and set(first).isdisjoint(second)
    assert {_params(u).get("prduct") or _params(u).get("item_name") for u in first} == {"초음파진단기"}
    assert {_params(u).get("prduct") or _params(u).get("item_name") for u in second} == {"치과용임플란트"}


def test_official_field_per_service_and_no_unfiltered_service(monkeypatch):
    calls = _stub(monkeypatch, lambda u: _ok([]))
    kf.fetch_data_go_kr("의료기기 품목허가")
    by_path = {urllib.parse.urlsplit(u).path.rsplit("/", 2)[-2]: _params(u) for u in calls}
    assert by_path["MdlpPrdlstPrmisnInfoService05"]["prduct"] == "의료기기"
    assert by_path["TraceManageMdlpInfoService01"]["item_name"] == "의료기기"
    assert "MdlpMnfcturPrmisnInfoService01" not in by_path     # 품목 검색 조건이 없는 서비스는 조회 안 함
    for p in by_path.values():
        assert "query" not in p                                # 임의 공통 파라미터 없음


def test_result_records_the_search_condition(monkeypatch):
    def responder(url):
        if "MdlpPrdlstPrmisnInfoService05" in url:
            return _ok([{"ENTRPS": "A", "PRDUCT": "초음파진단기", "PRDUCT_PRMISN_NO": "1"}], nested=True)
        return _ok([])
    _stub(monkeypatch, responder)
    res = kf.fetch_data_go_kr("초음파진단기 허가")
    assert len(res) == 1 and res[0]["query"] == {"prduct": "초음파진단기"}
    assert res[0]["item"]["PRDUCT"] == "초음파진단기"


def test_no_keyword_means_no_request(monkeypatch):
    calls = _stub(monkeypatch, lambda u: _ok([]))
    assert kf.fetch_data_go_kr("   ") == [] and calls == []


def test_transport_failure_degrades_to_empty(monkeypatch):
    def responder(url):
        return None if "TraceManage" in url else b"{not json"
    calls = _stub(monkeypatch, responder)
    assert kf.fetch_data_go_kr("초음파진단기") == [] and len(calls) == 2
