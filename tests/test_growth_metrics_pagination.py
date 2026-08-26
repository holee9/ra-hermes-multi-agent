"""Regression tests for scripts/growth-metrics.py session/message pagination (#103).

Reproduction-first (repo Rule 4). Observed defect, measured 2026-08-26 against the
live Honcho instance on T3610:

  reports/growth-2026-08-13..08-26.json  ->  sessions_scanned: 45, messages_scanned: 538
  identical for 14 consecutive days, and every growth metric reported 0 / None.

Root cause (measured, not inferred):
  The Honcho v3 API reads `page` from the QUERY STRING only. `list_sessions()`
  passes it in the JSON body, where it is ignored, so every call returns page 1.
  The API also caps `size` at 50 regardless of the requested page_size.

    POST /sessions/list  body={"page":1,"size":500}   -> 50 items, meta page=1 pages=5
    POST /sessions/list  body={"page":2,"size":50}    -> 50 items, meta page=1  (ignored)
    POST /sessions/list?page=2  body={}               -> 50 items, meta page=2  (honored)
    POST /sessions/list?page=5  body={}               -> 17 items, meta page=5  (last)

  total=217 sessions; the collector only ever saw the oldest 50 (2026-06-05 ~ 06-25,
  all June test fixtures), missing 167 sessions (77%) including every session from
  2026-06-25 onward. The metrics were therefore blind, not zero.

These tests are LIVE-dependent: they are skipped when Honcho is unreachable, so the
suite stays green in environments without the stack.
"""
import importlib.util
import os
from pathlib import Path

import pytest

requests = pytest.importorskip("requests")

_MOD = Path(__file__).resolve().parent.parent / "scripts" / "growth-metrics.py"
HONCHO_URL = os.environ.get("HONCHO_URL", "http://localhost:8000")
HONCHO_WS = os.environ.get("HONCHO_WS", "work")
_BASE = f"{HONCHO_URL}/v3/workspaces/{HONCHO_WS}"


def _load():
    spec = importlib.util.spec_from_file_location("growth_metrics", _MOD)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _session_total():
    """Authoritative session count straight from the API, or None if unreachable."""
    try:
        resp = requests.post(f"{_BASE}/sessions/list", json={}, timeout=10)
        resp.raise_for_status()
        return resp.json().get("total")
    except Exception:
        return None


live = pytest.mark.skipif(_session_total() is None, reason="Honcho unreachable")


@live
def test_api_ignores_page_in_body():
    """Contract guard: the body `page` is ignored. If this ever starts passing,
    the API changed and the query-string workaround can be revisited."""
    page2 = requests.post(f"{_BASE}/sessions/list", json={"page": 2, "size": 50}, timeout=10).json()
    assert page2.get("page") == 1, "body page is now honored — re-evaluate the fix"


@live
def test_api_honors_page_in_query_string():
    """Contract guard: the query-string `page` IS honored — the basis of the fix."""
    page2 = requests.post(f"{_BASE}/sessions/list?page=2", json={}, timeout=10).json()
    assert page2.get("page") == 2


@live
def test_api_caps_page_size_at_50():
    """Contract guard: requesting a larger page does not widen the page."""
    big = requests.post(f"{_BASE}/sessions/list", json={"size": 500, "page_size": 500}, timeout=10).json()
    assert len(big.get("items", [])) <= 50


@live
def test_list_sessions_returns_every_page():
    """THE regression. Must return all sessions, not just the first page.

    Fails before the fix (50 of 217); passes after."""
    total = _session_total()
    if total is None or total <= 50:
        pytest.skip("needs >50 sessions to exercise pagination")
    mod = _load()
    got = mod.list_sessions()
    assert len(got) == total, f"scanned {len(got)} of {total} sessions — pagination lost {total - len(got)}"


@live
def test_list_sessions_reaches_newest_session():
    """The practical consequence: the newest session must be in the scan.

    Before the fix the scan stopped at 2026-06-25 while activity continued to
    2026-08-25, which is why every growth metric read 0."""
    total = _session_total()
    if total is None or total <= 50:
        pytest.skip("needs >50 sessions to exercise pagination")
    last_page = requests.post(f"{_BASE}/sessions/list", json={}, timeout=10).json().get("pages", 1)
    tail = requests.post(f"{_BASE}/sessions/list?page={last_page}", json={}, timeout=10).json()["items"]
    newest = max(s.get("created_at", "") for s in tail)

    mod = _load()
    scanned = mod.list_sessions()
    assert scanned, "no sessions scanned"
    assert max(s.get("created_at", "") for s in scanned) == newest
