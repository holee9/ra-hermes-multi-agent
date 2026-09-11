#!/usr/bin/env python3
"""성장 리포트 동기화 클라이언트 (#103) — 소비 호스트(raspi5p 등)에서 실행.

`reports/growth-YYYY-MM-DD.json` 은 `.gitignore` 대상이라 수집 호스트(T3610) 로컬 산출물이다.
이 스크립트는 T3610 API 의 읽기 전용 엔드포인트에서 **없는 날짜만** 받아 로컬 `reports/` 에 채운다.
그래야 `growth-transition-readiness.py` 같은 게이트 점검이 소비 호스트에서도 같은 근거로 돈다.

- 읽기 전용: 서버에 아무것도 쓰지 않는다. 로컬은 리포트 파일만 추가한다(기존 파일은 기본 보존).
- 인증: 기존 API 키를 그대로 쓴다(`API_SERVER_KEY`). 새 자격증명·SSH 경로를 만들지 않는다.
- 원자적 쓰기: 임시 파일 → rename. 부분 파일이 남지 않는다.
- 실패는 조용히 넘어가지 않는다: 실패 건수를 종료코드로 알린다(0 정상, 1 일부 실패, 2 연결/인증 실패).

사용:
    API_BASE=http://<t3610>:8643 API_SERVER_KEY=... python3 scripts/fetch-growth-reports.py [--days 30] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

API_BASE = os.environ.get("API_BASE", "http://localhost:8643").rstrip("/")
API_KEY = os.environ.get("API_SERVER_KEY", "")
TIMEOUT = int(os.environ.get("FETCH_TIMEOUT", "20"))
REPORTS_DIR = Path(os.environ.get("GROWTH_REPORTS_DIR",
                                  str(Path(__file__).resolve().parent.parent / "reports")))
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _positive_int(v: str) -> int:
    """`--days` 는 양의 정수만 받는다.

    `0` 은 `sorted(dates)[-0:]` 가 **전체**를 선택해서 "최신 N일 제한" 의 의미가 뒤집힌다.
    음수도 같은 이유로 막는다(#103 Codex 리뷰).
    """
    n = int(v)
    if n < 1:
        raise argparse.ArgumentTypeError("--days 는 1 이상이어야 한다 (0 은 전체를 선택해 버린다)")
    return n


def _get(path: str) -> dict:
    req = urllib.request.Request(f"{API_BASE}{path}", method="GET",
                                 headers={"Authorization": f"Bearer {API_KEY}"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


class RemoteMisconfigured(RuntimeError):
    """서버의 리포트 디렉터리가 없다 — 진짜 0건이 아니라 설정 오류다."""


def list_remote(days: int) -> list[str]:
    """서버가 가진 날짜 중 최신 `days` 개.

    서버가 `dir_exists: false` 를 주면 **0건으로 삼키지 않는다**. 그것이 #103 의 원래 실패
    모양(조용한 0건)이므로 예외로 올려 종료코드로 드러낸다(Codex 리뷰).
    """
    data = _get("/v1/growth/reports")
    if data.get("dir_exists") is False:
        raise RemoteMisconfigured(data.get("hint") or "서버 리포트 디렉터리 없음")
    dates = [r["date"] for r in data.get("reports", [])
             if isinstance(r, dict) and DATE_RE.match(str(r.get("date", "")))]
    return sorted(dates)[-days:]


def missing_locally(dates: list[str], overwrite: bool = False) -> list[str]:
    if overwrite:
        return list(dates)
    return [d for d in dates if not (REPORTS_DIR / f"growth-{d}.json").exists()]


def save(date: str, payload: dict) -> Path:
    """같은 디렉터리에 **고유·배타적** 임시파일을 만들고 원자적으로 교체한다.

    고정 이름 `.tmp-growth-<date>.json` 은 두 가지 문제가 있었다(#103 Codex 리뷰):
    동시 실행이 같은 임시파일을 공유하고, 그 자리에 미리 심볼릭 링크가 있으면
    `write_text` 가 링크를 따라가 **바깥 파일을 덮는다**. `mkstemp` 는 O_EXCL 로 만들어
    두 경우 모두 성립하지 않는다. 실패하면 임시파일을 남기지 않는다.
    """
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    dest = REPORTS_DIR / f"growth-{date}.json"
    fd, tmp_name = tempfile.mkstemp(dir=str(REPORTS_DIR), prefix=f".tmp-growth-{date}-", suffix=".json")
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
        # mkstemp 의 0600 을 그대로 둔다. 공유가 필요하다는 근거 없이 world-readable 로
        # 넓히지 않는다 — 리포트에는 운영 정보가 들어갈 수 있다(Codex 리뷰).
        tmp.replace(dest)                   # 원자적 교체 — 부분 파일 없음
    except BaseException:
        tmp.unlink(missing_ok=True)         # 실패 시 잔여물 없음
        raise
    return dest


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="T3610 에서 성장 리포트를 받아 로컬 reports/ 를 채운다")
    ap.add_argument("--days", type=_positive_int, default=30, help="최신 N일 (양의 정수, 기본 30)")
    ap.add_argument("--overwrite", action="store_true", help="이미 있는 날짜도 다시 받는다")
    ap.add_argument("--dry-run", action="store_true", help="받을 목록만 출력")
    a = ap.parse_args(argv)

    if not API_KEY:
        print(json.dumps({"error": "API_SERVER_KEY 미설정"}, ensure_ascii=False))
        return 2
    try:
        remote = list_remote(a.days)
    except RemoteMisconfigured as e:
        print(json.dumps({"error": "서버 리포트 경로 미설정", "detail": str(e),
                          "api_base": API_BASE,
                          "fix": "T3610 서비스에 GROWTH_REPORTS_DIR 를 생산자와 같은 경로로 설정"},
                         ensure_ascii=False))
        return 2                              # 0건으로 삼키지 않는다 (#103 재발 방지)
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, json.JSONDecodeError) as e:
        print(json.dumps({"error": "목록 조회 실패", "detail": type(e).__name__,
                          "api_base": API_BASE}, ensure_ascii=False))
        return 2

    wanted = missing_locally(remote, a.overwrite)
    if a.dry_run:
        print(json.dumps({"api_base": API_BASE, "remote": len(remote), "would_fetch": wanted},
                         ensure_ascii=False))
        return 0

    fetched, failed = [], []
    for d in wanted:
        try:
            save(d, _get(f"/v1/growth/reports/{d}"))
            fetched.append(d)
        except (urllib.error.URLError, urllib.error.HTTPError, OSError, json.JSONDecodeError) as e:
            failed.append({"date": d, "detail": type(e).__name__})
    print(json.dumps({"api_base": API_BASE, "remote": len(remote), "fetched": fetched,
                      "failed": failed, "reports_dir": str(REPORTS_DIR)}, ensure_ascii=False))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
