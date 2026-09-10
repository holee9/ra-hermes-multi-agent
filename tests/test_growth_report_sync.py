"""#103 성장 리포트 동기화 — 서버 엔드포인트 + 소비 호스트 클라이언트 회귀. 네트워크 모킹."""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
H = {"Authorization": "Bearer test-key"}


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


srv = _load("hermes_api_server_reports", ROOT / "scripts" / "hermes-api-server.py")
cli = _load("fetch_growth_reports", ROOT / "scripts" / "fetch-growth-reports.py")


@pytest.fixture
def served(tmp_path, monkeypatch):
    d = tmp_path / "reports"
    d.mkdir()
    (d / "growth-2026-09-10.json").write_text(json.dumps({"messages_scanned": 5}), encoding="utf-8")
    (d / "growth-2026-09-11.json").write_text(json.dumps({"messages_scanned": 7}), encoding="utf-8")
    (d / "growth-diagnostic-2026-06-16.json").write_text("{}", encoding="utf-8")   # 날짜형 아님 → 제외
    monkeypatch.setattr(srv, "API_KEY", "test-key")
    monkeypatch.setattr(srv, "GROWTH_REPORTS_DIR", d)
    return d, srv.app.test_client()


# ── 서버 ───────────────────────────────────────────────────────────────────
def test_list_returns_only_dated_reports(served):
    _, c = served
    body = c.get("/v1/growth/reports", headers=H).get_json()
    assert body["count"] == 2 and [r["date"] for r in body["reports"]] == ["2026-09-10", "2026-09-11"]
    assert all(r["bytes"] > 0 for r in body["reports"])


def test_get_returns_report_content(served):
    _, c = served
    assert c.get("/v1/growth/reports/2026-09-11", headers=H).get_json() == {"messages_scanned": 7}


def test_missing_date_is_404_and_bad_format_is_400(served):
    _, c = served
    assert c.get("/v1/growth/reports/2026-01-01", headers=H).status_code == 404
    for bad in ("2026-9-1", "latest", "../../etc/passwd", "2026-09-11.json"):
        assert c.get(f"/v1/growth/reports/{bad}", headers=H).status_code in (400, 404)


def test_auth_required(served):
    _, c = served
    assert c.get("/v1/growth/reports").status_code == 401
    assert c.get("/v1/growth/reports/2026-09-11").status_code == 401


def test_symlinked_report_is_not_served(served, tmp_path):
    d, c = served
    outside = tmp_path.parent / f"{tmp_path.name}-outside.json"
    outside.write_text(json.dumps({"secret": True}), encoding="utf-8")
    (d / "growth-2026-09-12.json").symlink_to(outside)
    assert c.get("/v1/growth/reports/2026-09-12", headers=H).status_code == 404
    assert "2026-09-12" not in [r["date"] for r in c.get("/v1/growth/reports", headers=H).get_json()["reports"]]


def test_no_write_endpoint_exists():
    rules = [(r.rule, sorted(r.methods - {"HEAD", "OPTIONS"})) for r in srv.app.url_map.iter_rules()
             if r.rule.startswith("/v1/growth")]
    assert rules and all(m == ["GET"] for _, m in rules)


# ── 클라이언트 ─────────────────────────────────────────────────────────────
def _wire(monkeypatch, tmp_path, remote: dict, fail: set = frozenset()):
    monkeypatch.setattr(cli, "API_KEY", "test-key")
    monkeypatch.setattr(cli, "REPORTS_DIR", tmp_path / "local")

    def fake_get(path):
        if path == "/v1/growth/reports":
            return {"count": len(remote), "reports": [{"date": d, "bytes": 1} for d in sorted(remote)]}
        date = path.rsplit("/", 1)[-1]
        if date in fail:
            raise OSError("boom")
        return remote[date]
    monkeypatch.setattr(cli, "_get", fake_get)
    return tmp_path / "local"


def test_client_fetches_only_missing_dates(monkeypatch, tmp_path, capsys):
    local = _wire(monkeypatch, tmp_path, {"2026-09-10": {"a": 1}, "2026-09-11": {"a": 2}})
    local.mkdir()
    (local / "growth-2026-09-10.json").write_text("{}", encoding="utf-8")
    assert cli.main([]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["fetched"] == ["2026-09-11"] and out["failed"] == []
    assert json.loads((local / "growth-2026-09-11.json").read_text()) == {"a": 2}
    assert (local / "growth-2026-09-10.json").read_text() == "{}"        # 기존 파일 보존


def test_client_dry_run_writes_nothing(monkeypatch, tmp_path, capsys):
    local = _wire(monkeypatch, tmp_path, {"2026-09-11": {"a": 2}})
    assert cli.main(["--dry-run"]) == 0
    assert json.loads(capsys.readouterr().out)["would_fetch"] == ["2026-09-11"]
    assert not local.exists()


def test_client_reports_partial_failure_with_exit_1(monkeypatch, tmp_path, capsys):
    _wire(monkeypatch, tmp_path, {"2026-09-10": {"a": 1}, "2026-09-11": {"a": 2}}, fail={"2026-09-11"})
    assert cli.main([]) == 1
    out = json.loads(capsys.readouterr().out)
    assert out["fetched"] == ["2026-09-10"] and out["failed"][0]["date"] == "2026-09-11"


def test_client_without_key_exits_2(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(cli, "API_KEY", "")
    monkeypatch.setattr(cli, "REPORTS_DIR", tmp_path / "local")
    assert cli.main([]) == 2
    assert "API_SERVER_KEY" in capsys.readouterr().out


def test_client_days_window_limits_requests(monkeypatch, tmp_path, capsys):
    _wire(monkeypatch, tmp_path, {f"2026-09-{d:02d}": {"a": d} for d in range(1, 12)})
    assert cli.main(["--days", "3", "--dry-run"]) == 0
    assert json.loads(capsys.readouterr().out)["would_fetch"] == ["2026-09-09", "2026-09-10", "2026-09-11"]
