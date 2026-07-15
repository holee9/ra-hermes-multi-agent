#!/usr/bin/env python3
"""Local regression checks for scripts/kb-eval-checksheet.py (#113 response capture)."""

from __future__ import annotations

import importlib.util
import sys
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "kb-eval-checksheet.py"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("kb_eval_checksheet", SCRIPT)
    if spec is None or spec.loader is None:
        fail(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()

    agent = SimpleNamespace(
        peer_id="ra_us",
        profile_id="ra-us",
        name="Mike",
        region="US",
        daily_focus=("510(k) predicate strategy",),
    )
    case = SimpleNamespace(
        scenario_id="scn-1",
        source_path="github:holee9/ra-project/foo.md",
        source_hash="hash-1",
        matched_keywords=("FDA",),
        excerpts=({"id": "chunk-1", "excerpt": "FDA 510(k) predicate guidance."},),
    )

    # #113 — with a captured response, the case renders an Agent Response
    # section and points hallucination/escalation checks at it.
    rendered_with = module.render_case(date(2026, 7, 15), 13, agent, 1, case, response="A generated RA judgment.")
    if "**Agent Response**" not in rendered_with:
        fail("Agent Response section missing when response is provided")
    if "A generated RA judgment." not in rendered_with:
        fail("captured response text not rendered")
    if "Agent Response을 기준으로 판정" not in rendered_with:
        fail("hallucination/escalation judgment target must reference Agent Response when captured")

    # Without a response (default / --capture-responses omitted), behavior must
    # be unchanged from before #113 except for the explicit fallback note.
    rendered_without = module.render_case(date(2026, 7, 15), 13, agent, 1, case)
    if "**Agent Response**" in rendered_without:
        fail("Agent Response section must not render when no response was captured")
    if "source excerpt transparency" not in rendered_without:
        fail("fallback judgment-target note missing when no response was captured")

    # A capture error must render a visible, non-crashing fallback note (fail-safe).
    rendered_error = module.render_case(date(2026, 7, 15), 13, agent, 1, case, response_error="timeout after 90s")
    if "capture failed" not in rendered_error or "timeout after 90s" not in rendered_error:
        fail("capture-error fallback note missing or incomplete")

    # capture_agent_response must fail closed (return an error tuple, never raise)
    # when the LLM endpoint is unreachable.
    module.ADVISORY_LLM_URL = "http://127.0.0.1:1"  # unroutable — fast connection refusal
    text, error = module.capture_agent_response("ra-us", "test assignment")
    if text or not error:
        fail(f"capture_agent_response must fail closed on unreachable endpoint, got text={text!r} error={error!r}")

    print("OK: kb-eval-checksheet response-capture contract holds")


if __name__ == "__main__":
    main()
