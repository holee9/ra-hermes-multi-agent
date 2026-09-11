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


# ── #103 Codex 리뷰 반영 회귀 ───────────────────────────────────────────────
def test_list_surfaces_reports_dir_and_missing_dir(tmp_path, monkeypatch):
    """P1: 배포 위치에서 서빙 경로가 생산자와 달라도 '0건' 이 조용하면 #103 을 반복한다.
    경로와 존재 여부를 응답에 실어 설정 오류와 진짜 0건을 구분 가능하게 한다."""
    monkeypatch.setattr(srv, "API_KEY", "test-key")
    missing = tmp_path / "opt" / "reports"                  # 배포 기본값이 가리킬 법한 없는 경로
    monkeypatch.setattr(srv, "GROWTH_REPORTS_DIR", missing)
    body = srv.app.test_client().get("/v1/growth/reports", headers=H).get_json()
    assert body["count"] == 0 and body["dir_exists"] is False
    assert body["reports_dir"] == str(missing) and "GROWTH_REPORTS_DIR" in body["hint"]


def test_list_reports_dir_present_when_dir_exists(served):
    d, c = served
    body = c.get("/v1/growth/reports", headers=H).get_json()
    assert body["dir_exists"] is True and body["reports_dir"] == str(d) and "hint" not in body


def test_save_does_not_follow_preexisting_symlink(monkeypatch, tmp_path):
    """P2: 고정 임시파일명은 그 자리에 심볼릭 링크가 있으면 바깥 파일을 덮었다.
    mkstemp 는 O_EXCL 로 만들므로 성립하지 않는다."""
    local = tmp_path / "local"
    local.mkdir()
    outside = tmp_path / "outside.json"
    outside.write_text("원본 보존", encoding="utf-8")
    (local / ".tmp-growth-2026-09-11.json").symlink_to(outside)   # 예전 고정 이름
    monkeypatch.setattr(cli, "REPORTS_DIR", local)
    cli.save("2026-09-11", {"a": 1})
    assert outside.read_text(encoding="utf-8") == "원본 보존"      # 바깥 파일 무사
    assert json.loads((local / "growth-2026-09-11.json").read_text()) == {"a": 1}


def test_save_concurrent_same_date_does_not_share_tempfile(monkeypatch, tmp_path):
    """P2 원결함 고정: **같은 날짜**를 여러 스레드가 동시에 쓸 때 고정 임시파일명은 하나를
    공유해 서로의 쓰기에 끼어든다(잘린 JSON / 뒤섞인 내용). 날짜를 다르게 쓰면 옛 구현도
    통과하므로 회귀가 되지 않는다 — 반드시 동일 날짜여야 한다."""
    local = tmp_path / "local"
    monkeypatch.setattr(cli, "REPORTS_DIR", local)
    import threading
    date, errors = "2026-09-11", []
    payload = {"filler": "x" * 20000, "n": 1}          # 한 번의 write 로 끝나지 않게 크게

    def w():
        try:
            cli.save(date, payload)
        except Exception as e:                          # noqa: BLE001
            errors.append(e)

    ts = [threading.Thread(target=w) for _ in range(20)]
    [t.start() for t in ts]; [t.join() for t in ts]
    assert not errors, errors
    assert json.loads((local / f"growth-{date}.json").read_text(encoding="utf-8")) == payload
    assert not list(local.glob(".tmp-*")), "임시파일 잔여물"


def test_save_leaves_no_tempfile_on_failure(monkeypatch, tmp_path):
    local = tmp_path / "local"
    monkeypatch.setattr(cli, "REPORTS_DIR", local)

    class Boom:
        def __repr__(self): raise RuntimeError("boom")
    with pytest.raises((RuntimeError, TypeError)):
        cli.save("2026-09-11", {"bad": Boom()})
    assert not list(local.glob(".tmp-*"))


@pytest.mark.parametrize("bad", ["0", "-1"])
def test_days_must_be_positive(bad):
    """P2: --days 0 은 [-0:] 로 전체를 선택해 '최신 N일' 의미가 뒤집힌다."""
    with pytest.raises(SystemExit):
        cli.main(["--days", bad, "--dry-run"])


def test_client_exits_2_when_server_dir_missing(monkeypatch, tmp_path, capsys):
    """서버가 dir_exists:false 를 주면 클라이언트가 0건으로 삼키지 않고 종료코드 2 로 드러낸다.
    조용한 0건이 #103 의 원래 실패 모양이었다."""
    monkeypatch.setattr(cli, "API_KEY", "test-key")
    monkeypatch.setattr(cli, "REPORTS_DIR", tmp_path / "local")
    monkeypatch.setattr(cli, "_get", lambda p: {"count": 0, "reports": [], "dir_exists": False,
                                                "reports_dir": "/opt/reports", "hint": "GROWTH_REPORTS_DIR 를 설정"})
    assert cli.main([]) == 2
    out = json.loads(capsys.readouterr().out)
    assert "GROWTH_REPORTS_DIR" in out["fix"] and out["error"]


def test_client_still_accepts_genuine_zero(monkeypatch, tmp_path, capsys):
    """진짜 0건(디렉터리는 있고 리포트만 없음)은 정상 종료다 — 설정 오류와 구분된다."""
    monkeypatch.setattr(cli, "API_KEY", "test-key")
    monkeypatch.setattr(cli, "REPORTS_DIR", tmp_path / "local")
    monkeypatch.setattr(cli, "_get", lambda p: {"count": 0, "reports": [], "dir_exists": True})
    assert cli.main([]) == 0
    assert json.loads(capsys.readouterr().out)["fetched"] == []


def test_saved_report_is_not_world_readable(monkeypatch, tmp_path):
    """근거 없이 권한을 넓히지 않는다 — mkstemp 의 0600 을 유지한다(Codex 리뷰)."""
    local = tmp_path / "local"
    monkeypatch.setattr(cli, "REPORTS_DIR", local)
    dest = cli.save("2026-09-11", {"a": 1})
    assert dest.stat().st_mode & 0o077 == 0, oct(dest.stat().st_mode)
