"""#108 — llm-wiki on-demand consumer: Korean tokens, single tree call (no traversal).

Review (codex, 2026-09-09) reproduced on 5d683f5:
  - _tokenize dropped every non a-z/0-9 char → a Korean-only query had zero tokens
  - _get_wiki_files made ONE recursive tree call and ignored `truncated: true`
Network-free: _http_get is monkeypatched.
"""
import importlib.util
import json
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "knowledge_fetch.py"


def _load():
    spec = importlib.util.spec_from_file_location("knowledge_fetch_wiki", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["knowledge_fetch_wiki"] = mod
    spec.loader.exec_module(mod)
    return mod


kf = _load()


# ------------------------------------------------------------ tokenize

def test_korean_query_produces_tokens():
    toks = kf._tokenize("의료기기 허가 등급 분류 기준")
    assert {"의료기기", "허가", "등급", "분류", "기준"} <= toks


def test_mixed_query_keeps_latin_and_hangul():
    toks = kf._tokenize("IEC 60601-1-3 방사선 안전")
    assert {"iec", "60601", "방사선", "안전"} <= toks
    assert "1" not in toks                     # short digit token still dropped


def test_short_latin_tokens_still_dropped():
    assert kf._tokenize("an eu md") == set()


def test_korean_query_scores_korean_filename():
    q = kf._tokenize("의료기기 등급 분류")
    assert kf._score_file("wiki/concepts/의료기기-등급-분류.md", q) > 0
    assert kf._score_file("wiki/concepts/unrelated-topic.md", q) == 0


# ------------------------------------------------------------ tree pagination

def _tree(paths, truncated):
    return json.dumps({"tree": [{"path": p, "type": "blob"} for p in paths], "truncated": truncated}).encode()


def _serve(pages, calls):
    """페이지 파라미터가 없으면 1페이지를 준다 — 순회 제거 후 URL 에 page= 가 없다."""
    def fake_get(url, headers=None, timeout=10):
        calls.append(url)
        page = int(url.rsplit("&page=", 1)[1]) if "&page=" in url else 1   # per_page= 와 혼동 금지
        return pages.get(page)
    return fake_get


def test_tree_is_called_exactly_once_no_pagination(monkeypatch):
    """[HARD] #108 역할 경계: tree 순회로 truncation 을 뚫는 것은 금지된 우회다.
    `docs/specs/llm-wiki-operating-model.md` §역할 경계 — "tree 순회·전체 임베딩 우회 ✕".
    b6d47bb·e519986 이 페이지를 돌았고 2026-09-11 사용자 결정으로 철회했다.
    truncated 여도 **호출은 한 번**이어야 한다."""
    kf._wiki_file_cache.clear()
    calls = []
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md", "b.md", ".obsidian/x.md"], True)}, calls))
    files = kf._get_wiki_files()
    assert files == ["a.md", "b.md"]                      # .obsidian 제외는 유지
    assert len(calls) == 1, f"tree API 를 {len(calls)}회 호출 — 순회는 금지다"
    assert "&page=2" not in "".join(calls)


def test_truncated_flag_is_recorded_not_defeated(monkeypatch):
    """truncated 는 뚫을 대상이 아니라 기록할 사실이다. 부분 목록으로 매칭하되
    완전한 목록인 척하지 않는다."""
    kf._wiki_file_cache.clear()
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md"], True)}, []))
    kf._get_wiki_files()
    assert kf.WIKI_TREE_STATUS[kf.GITEA_WIKI_REPO] == {"files": 1, "truncated": True}


def test_truncated_limitation_is_logged_as_by_design(monkeypatch, caplog):
    kf._wiki_file_cache.clear()
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md"], True)}, []))
    kf._get_wiki_files()
    assert "truncated" in caplog.text and "manifest" in caplog.text   # 해소 경로는 manifest


def test_untruncated_tree_reports_complete(monkeypatch):
    kf._wiki_file_cache.clear()
    calls = []
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md"], False)}, calls))
    assert kf._get_wiki_files() == ["a.md"] and len(calls) == 1
    assert kf.WIKI_TREE_STATUS[kf.GITEA_WIKI_REPO]["truncated"] is False


def test_non_md_entries_are_filtered(monkeypatch):
    kf._wiki_file_cache.clear()
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md", "image.png", "b.txt"], False)}, []))
    assert kf._get_wiki_files() == ["a.md"]


def test_listing_is_cached_per_process(monkeypatch):
    kf._wiki_file_cache.clear()
    calls = []
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md"], False)}, calls))
    kf._get_wiki_files()
    kf._get_wiki_files()
    assert len(calls) == 1


def test_first_page_failure_is_not_cached_and_recovers(monkeypatch):
    kf._wiki_file_cache.clear()
    calls = []
    state = {"fail": True}

    def flaky(url, headers=None, timeout=10):
        calls.append(url)
        if state["fail"]:
            return None
        return _tree(["a.md"], False)
    monkeypatch.setattr(kf, "_http_get", flaky)
    assert kf._get_wiki_files() == []
    assert kf.WIKI_TREE_STATUS[kf.GITEA_WIKI_REPO]["truncated"] is True
    assert kf.GITEA_WIKI_REPO not in kf._wiki_file_cache          # 실패는 캐시하지 않는다
    state["fail"] = False
    assert kf._get_wiki_files() == ["a.md"]                        # 복구 후 HTTP 재시도로 정상 목록
    assert len(calls) == 2
