#!/usr/bin/env python3
"""Contract checks for scripts/knowledge_fetch.py — error classification (#80 H2/H3).

Guards:
- H2: _http_get must classify errors (HTTPError/URLError/Timeout) and return None,
  not silently swallow them as empty results.
- H3: openFDA rate-limit / error responses must yield [] without being confused
  with "no clearances found" (which would mislead RA confidence).
"""

from __future__ import annotations

import importlib.util
import json
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parent.parent
MODULE_PATH = ROOT / "scripts" / "knowledge_fetch.py"


def load_module():
    spec = importlib.util.spec_from_file_location("knowledge_fetch", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load knowledge_fetch.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _mock_urlopen(body: bytes):
    """Build a urlopen mock whose context manager returns `body` from .read()."""
    cm = MagicMock()
    cm.__enter__.return_value.read.return_value = body
    cm.__exit__.return_value = False
    return cm


def main() -> None:
    kf = load_module()

    # --- H2: _http_get error classification ---
    with patch("urllib.request.urlopen", return_value=_mock_urlopen(b'{"ok":1}')):
        assert kf._http_get("http://x") == b'{"ok":1}', "normal GET must return body bytes"

    with patch("urllib.request.urlopen", side_effect=urllib.error.HTTPError("u", 404, "nf", {}, None)):
        assert kf._http_get("http://x") is None, "HTTPError must yield None"

    with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("dns failure")):
        assert kf._http_get("http://x") is None, "URLError must yield None"

    with patch("urllib.request.urlopen", side_effect=TimeoutError("timed out")):
        assert kf._http_get("http://x") is None, "Timeout must yield None"

    # --- H3: openFDA error response (rate limit) must yield [], not be parsed as results ---
    err_body = json.dumps({"error": {"code": "OVER_RATE_LIMIT", "message": "slow down"}}).encode()
    with patch.object(kf, "_http_get", return_value=err_body), patch.object(kf, "OPENFDA_API_KEY", "k"):
        assert kf.fetch_openfda("device implant") == [], "openFDA error response must yield []"

    # --- H3: openFDA valid results must parse correctly ---
    ok_body = json.dumps({"results": [{"k_number": "K123", "device_name": "implant"}]}).encode()
    with patch.object(kf, "_http_get", return_value=ok_body), patch.object(kf, "OPENFDA_API_KEY", "k"):
        out = kf.fetch_openfda("device implant")
        assert len(out) == 1 and out[0]["k_number"] == "K123", "valid openFDA must parse results"

    print("knowledge_fetch contract OK")


if __name__ == "__main__":
    main()
