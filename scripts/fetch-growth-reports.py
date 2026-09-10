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
import urllib.error
import urllib.request
from pathlib import Path

API_BASE = os.environ.get("API_BASE", "http://localhost:8643").rstrip("/")
API_KEY = os.environ.get("API_SERVER_KEY", "")
TIMEOUT = int(os.environ.get("FETCH_TIMEOUT", "20"))
REPORTS_DIR = Path(os.environ.get("GROWTH_REPORTS_DIR",
                                  str(Path(__file__).resolve().parent.parent / "reports")))
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _get(path: str) -> dict:
    req = urllib.request.Request(f"{API_BASE}{path}", method="GET",
                                 headers={"Authorization": f"Bearer {API_KEY}"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def list_remote(days: int) -> list[str]:
    """서버가 가진 날짜 중 최신 `days` 개."""
    data = _get("/v1/growth/reports")
    dates = [r["date"] for r in data.get("reports", [])
             if isinstance(r, dict) and DATE_RE.match(str(r.get("date", "")))]
    return sorted(dates)[-days:]


def missing_locally(dates: list[str], overwrite: bool = False) -> list[str]:
    if overwrite:
        return list(dates)
    return [d for d in dates if not (REPORTS_DIR / f"growth-{d}.json").exists()]


def save(date: str, payload: dict) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    dest = REPORTS_DIR / f"growth-{date}.json"
    tmp = dest.with_name(f".tmp-{dest.name}")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(dest)                       # 원자적 교체 — 부분 파일 없음
    return dest


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="T3610 에서 성장 리포트를 받아 로컬 reports/ 를 채운다")
    ap.add_argument("--days", type=int, default=30, help="최신 N일 (기본 30)")
    ap.add_argument("--overwrite", action="store_true", help="이미 있는 날짜도 다시 받는다")
    ap.add_argument("--dry-run", action="store_true", help="받을 목록만 출력")
    a = ap.parse_args(argv)

    if not API_KEY:
        print(json.dumps({"error": "API_SERVER_KEY 미설정"}, ensure_ascii=False))
        return 2
    try:
        remote = list_remote(a.days)
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
