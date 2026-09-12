#!/usr/bin/env python3
"""SPEC-DEVCOMM-001 M3 — 발신 nudge (T3610 → Pi).

이 저장소에서 이슈 코멘트를 작성하는 지점이, 작성 성공 직후 상대 기기의 nudge URL로
POST 한다. 폴링(M2)이 5분 백스톱이므로 이 계층은 **지연 단축용**이다 — 실패해도 폴링이
복구하니 호출자를 깨뜨리지 않는다(REQ-DC-005·C4).

계약:
- `PEER_NUDGE_URL` 미설정 → 조용히 no-op (REQ-DC-006, 기존 `n8n_webhook_url` null 패턴과 동일)
- 최대 3회 시도, 최종 실패는 로그만
- 본문은 수신부(`/v1/peer/notify`)와 같은 4필드 스키마: issue / comment_url / author / body

네트워크 라이브러리는 표준 라이브러리만 쓴다(이 스크립트군의 기존 관례).
"""
from __future__ import annotations

import json
import logging
import os
import urllib.error
import urllib.request

MAX_ATTEMPTS = 3
TIMEOUT = 5

logger = logging.getLogger(__name__)


def build_nudge(issue: int, comment_url: str, author: str, body: str) -> dict:
    """수신부 스키마와 동일한 4필드. body 는 길이만 의미가 있으므로 앞부분만 싣는다."""
    return {
        "issue": int(issue),
        "comment_url": str(comment_url),
        "author": str(author),
        "body": str(body)[:2000],
    }


def notify_peer(issue: int, comment_url: str, author: str = "t3610", body: str = "") -> str:
    """상대 기기에 nudge 를 보낸다. 반환값은 결과 사유(호출자는 무시해도 된다).

    절대 예외를 올리지 않는다 — 코멘트는 이미 작성됐고, 알림 실패로 그 작업을 되돌릴 수 없다.
    """
    url = os.environ.get("PEER_NUDGE_URL", "").strip()
    if not url:
        return "disabled"                      # REQ-DC-006: 미설정은 정상 상태다
    key = os.environ.get("API_SERVER_KEY", "").strip()
    if not key:
        logger.warning("PEER_NUDGE_URL set but API_SERVER_KEY missing — nudge skipped")
        return "no_key"                        # 수신부가 Bearer 를 요구한다(fail-closed)

    payload = json.dumps(build_nudge(issue, comment_url, author, body)).encode("utf-8")
    last = ""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        req = urllib.request.Request(
            url, data=payload, method="POST",
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                if 200 <= resp.status < 300:
                    return "sent"
                last = f"http_{resp.status}"
        except urllib.error.HTTPError as exc:
            last = f"http_{exc.code}"
            if 400 <= exc.code < 500:
                break                          # 스키마·인증 오류는 재시도해도 같다
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = type(exc).__name__
        logger.warning("peer nudge attempt %d/%d failed: %s", attempt, MAX_ATTEMPTS, last)
    logger.error("peer nudge failed after %d attempts (%s) — polling backstop covers it",
                 MAX_ATTEMPTS, last)
    return f"failed:{last}"
