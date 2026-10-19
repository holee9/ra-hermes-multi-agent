"""kb-watch (#158) — unit tests. No network, no DB required."""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("kb_watch", ROOT / "scripts" / "kb-watch.py")
m = importlib.util.module_from_spec(spec)
sys.modules["kb_watch"] = m
spec.loader.exec_module(m)


def test_issue_body_is_english_and_has_fields():
    body = m.build_issue_body("holee9/ra-project", "some/file.md", ["guidance-dates"])
    assert "ra-hermes watcher" in body
    assert "holee9/ra-project" in body
    assert "guidance-dates" in body
    # language policy 2026-10-19: agent-facing issue bodies are English
    for token in ("레포", "확인", "수정 필요"):
        assert token not in body


def test_ledger_append_writes_jsonl(tmp_path, monkeypatch):
    ledger = tmp_path / "ledger.jsonl"
    monkeypatch.setattr(m, "LEDGER", ledger)
    m.ledger_append({"kind": "kb-file-changed", "repo": "r", "file": "a.md"})
    m.ledger_append({"kind": "kb-file-changed", "repo": "r", "file": "b.md"})
    lines = ledger.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["file"] == "a.md"


def test_detect_smoke_no_crash(monkeypatch, tmp_path):
    # A checkout path that does not exist must yield a checkout-missing finding,
    # not a crash — detection robustness over completeness.
    monkeypatch.setattr(m, "KB_REPOS", {"x/y": tmp_path / "nope"})
    findings = m.detect(1)
    assert findings == [{"kind": "checkout-missing", "repo": "x/y",
                         "path": str(tmp_path / "nope")}]
