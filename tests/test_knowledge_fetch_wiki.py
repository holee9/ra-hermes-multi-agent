"""#108 — llm-wiki on-demand consumer: Korean tokens, truncated tree pagination.

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
    def fake_get(url, headers=None, timeout=10):
        calls.append(url)
        page = int(url.rsplit("page=", 1)[1])
        return pages.get(page)
    return fake_get


def test_truncated_tree_is_walked_across_pages(monkeypatch):
    kf._wiki_file_cache.clear()
    calls = []
    pages = {1: _tree(["a.md", "b.md", ".obsidian/x.md"], True),
             2: _tree(["c.md", "d.txt"], True),
             3: _tree(["e.md"], False)}
    monkeypatch.setattr(kf, "_http_get", _serve(pages, calls))
    files = kf._get_wiki_files()
    assert files == ["a.md", "b.md", "c.md", "e.md"]
    assert len(calls) == 3 and "per_page=" in calls[0] and "page=3" in calls[2]
    assert kf.WIKI_TREE_STATUS[kf.GITEA_WIKI_REPO] == {"files": 4, "truncated": False}


def test_single_untruncated_page_makes_one_call(monkeypatch):
    kf._wiki_file_cache.clear()
    calls = []
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md"], False)}, calls))
    assert kf._get_wiki_files() == ["a.md"] and len(calls) == 1


def test_page_failure_mid_walk_is_reported_as_truncated(monkeypatch, caplog):
    kf._wiki_file_cache.clear()
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md"], True), 2: None}, []))
    files = kf._get_wiki_files()
    assert files == ["a.md"]                                       # 부분 목록은 이번 호출에 사용
    assert kf.WIKI_TREE_STATUS[kf.GITEA_WIKI_REPO]["truncated"] is True
    assert kf.GITEA_WIKI_REPO not in kf._wiki_file_cache          # 실패 목록은 캐시하지 않음 (리뷰 2차)
    assert "fetch failed" in caplog.text


def test_page_ceiling_reports_truncated(monkeypatch):
    kf._wiki_file_cache.clear()
    monkeypatch.setattr(kf, "WIKI_TREE_MAX_PAGES", 2)
    pages = {1: _tree(["a.md"], True), 2: _tree(["b.md"], True), 3: _tree(["c.md"], False)}
    monkeypatch.setattr(kf, "_http_get", _serve(pages, []))
    assert kf._get_wiki_files() == ["a.md", "b.md"]
    assert kf.WIKI_TREE_STATUS[kf.GITEA_WIKI_REPO]["truncated"] is True


def test_listing_is_cached_per_process(monkeypatch):
    kf._wiki_file_cache.clear()
    calls = []
    monkeypatch.setattr(kf, "_http_get", _serve({1: _tree(["a.md"], False)}, calls))
    kf._get_wiki_files()
    kf._get_wiki_files()
    assert len(calls) == 1


# ---- #108 review round 2 (2026-09-10)

def test_page_with_only_non_md_entries_does_not_stop_the_walk(monkeypatch):
    kf._wiki_file_cache.clear()
    pages = {1: _tree(["a.md"], True), 2: _tree(["image.png"], True), 3: _tree(["required.md"], False)}
    monkeypatch.setattr(kf, "_http_get", _serve(pages, []))
    assert kf._get_wiki_files() == ["a.md", "required.md"]
    assert kf.WIKI_TREE_STATUS[kf.GITEA_WIKI_REPO]["truncated"] is False


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
