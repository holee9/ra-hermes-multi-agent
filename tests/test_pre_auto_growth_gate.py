"""#136 — the deriver-flush gate reports "probe unavailable" separately from "setting False".

Codex review (2026-09-09): translating an execution/permission/parse failure into
"DERIVER_FLUSH_ENABLED is not True" pointed operators at the wrong fix. The gate stays
closed in both cases; only the reported cause changes. Network/docker-free.
"""
import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "pre-auto-growth-loop.py"


def _load():
    spec = importlib.util.spec_from_file_location("pre_auto_growth_loop", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["pre_auto_growth_loop"] = mod
    spec.loader.exec_module(mod)
    return mod


m = _load()


def _cmd(returncode, stdout="", stderr=""):
    return m.CommandResult(cmd=["docker"], returncode=returncode, stdout=stdout, stderr=stderr)


def _report(flush):
    queue = {"pending_total": 0, "pending_by_ra": {}}
    return {"deriver_flush": flush, "queue_before": queue, "queue_after": queue, "verifiers": [],
            "daily_growth_dry_run": {"plan": {"execute_gate": {"allowed": True}}, "command": {"returncode": 0}},
            "growth_message_health": {"json_envelopes": 0, "hyphen_peers": 0}}


def test_probe_ok_true_opens_flush_check(monkeypatch):
    monkeypatch.setattr(m, "run_command", lambda cmd, env, timeout=60: _cmd(0, "True\n"))
    r = m.check_deriver_flush({})
    assert r["ok"] is True and r["probe"] == "ok" and r["value"] == "True"


def test_probe_ok_false_is_a_setting_verdict(monkeypatch):
    monkeypatch.setattr(m, "run_command", lambda cmd, env, timeout=60: _cmd(0, "False\n"))
    r = m.check_deriver_flush({})
    assert r["ok"] is False and r["probe"] == "ok"
    failures = m.evaluate_iteration(_report(r), max_pending=0, pending_scope="all")
    assert "DERIVER_FLUSH_ENABLED is not True" in failures


def test_docker_unreachable_is_probe_unavailable_not_false(monkeypatch):
    monkeypatch.setattr(m, "run_command", lambda cmd, env, timeout=60: _cmd(
        1, "", "Cannot connect to the Docker daemon at unix:///var/run/docker.sock"))
    r = m.check_deriver_flush({})
    assert r["ok"] is False and r["probe"] == "unavailable"
    failures = m.evaluate_iteration(_report(r), max_pending=0, pending_scope="all")
    assert len(failures) == 1
    assert failures[0].startswith("DERIVER_FLUSH_ENABLED probe unavailable")
    assert "Docker daemon" in failures[0]
    assert "is not True" not in failures[0]


def test_garbage_output_is_probe_unavailable(monkeypatch):
    monkeypatch.setattr(m, "run_command", lambda cmd, env, timeout=60: _cmd(0, "Traceback ...\n"))
    r = m.check_deriver_flush({})
    assert r["ok"] is False and r["probe"] == "unavailable"


def test_legacy_report_without_probe_field_still_evaluates():
    failures = m.evaluate_iteration(_report({"ok": False, "value": ""}), max_pending=0, pending_scope="all")
    assert failures == ["DERIVER_FLUSH_ENABLED is not True"]
