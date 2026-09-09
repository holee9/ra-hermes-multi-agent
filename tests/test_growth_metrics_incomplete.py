"""#103 — a page failure mid-walk (or an API total larger than what was collected) is
reported as ingestion_diagnostics.collection_incomplete instead of a silent short scan.
Network-free: honcho_post is monkeypatched.
"""
import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "growth-metrics.py"


def _load():
    spec = importlib.util.spec_from_file_location("growth_metrics_incomplete", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["growth_metrics_incomplete"] = mod
    spec.loader.exec_module(mod)
    return mod


gm = _load()


def _pages(responses):
    calls = []

    def fake_post(path, body):
        calls.append(path)
        page = int(path.rsplit("page=", 1)[1])
        return responses.get(page)
    return fake_post, calls


def test_full_walk_is_complete(monkeypatch):
    gm.PAGINATION_INCOMPLETE.clear()
    post, calls = _pages({1: {"items": [{"id": 1}] * 50, "pages": 2, "total": 60},
                          2: {"items": [{"id": 2}] * 10, "pages": 2, "total": 60}})
    monkeypatch.setattr(gm, "honcho_post", post)
    items = gm._list_all_pages("/sessions/list", ("items",))
    assert len(items) == 60 and len(calls) == 2
    assert gm.PAGINATION_INCOMPLETE == []


def test_page_failure_after_first_page_is_flagged(monkeypatch):
    gm.PAGINATION_INCOMPLETE.clear()
    post, _ = _pages({1: {"items": [{"id": 1}] * 50, "pages": 3, "total": 130}, 2: None})
    monkeypatch.setattr(gm, "honcho_post", post)
    items = gm._list_all_pages("/sessions/list", ("items",))
    assert len(items) == 50                                  # partial data is still returned
    [flag] = gm.PAGINATION_INCOMPLETE
    assert flag == {"path": "/sessions/list", "page_failed": 2, "pages_expected": 3,
                    "items_collected": 50, "total_expected": 130}


def test_total_larger_than_collected_is_flagged_even_without_page_error(monkeypatch):
    gm.PAGINATION_INCOMPLETE.clear()
    post, _ = _pages({1: {"items": [{"id": 1}] * 50, "pages": 1, "total": 259}})
    monkeypatch.setattr(gm, "honcho_post", post)
    items = gm._list_all_pages("/sessions/list", ("items",))
    assert len(items) == 50
    [flag] = gm.PAGINATION_INCOMPLETE
    assert flag["page_failed"] is None and flag["total_expected"] == 259


def test_first_page_failure_is_not_double_counted(monkeypatch):
    gm.PAGINATION_INCOMPLETE.clear()
    post, _ = _pages({1: None})
    monkeypatch.setattr(gm, "honcho_post", post)
    assert gm._list_all_pages("/sessions/list", ("items",)) == []
    assert gm.PAGINATION_INCOMPLETE == []      # API_ERRORS already carries the outright failure


def test_compute_metrics_surfaces_collection_incomplete(monkeypatch):
    post, _ = _pages({1: {"items": [{"id": "s1"}], "pages": 2, "total": 2}, 2: None})
    monkeypatch.setattr(gm, "honcho_post", post)
    monkeypatch.setattr(gm, "list_messages", lambda sid: [])
    from datetime import datetime, timezone
    out = gm.compute_metrics(datetime(2026, 9, 1, tzinfo=timezone.utc), datetime(2026, 9, 2, tzinfo=timezone.utc))
    diag = out["ingestion_diagnostics"]
    assert diag["collection_incomplete"] is True
    assert diag["incomplete_pages"][0]["page_failed"] == 2
