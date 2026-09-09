---
id: SPEC-DEVCOMM-001
artifact: plan
status: in-progress
created: 2026-08-05
---

# SPEC-DEVCOMM-001 구현 계획

## 마일스톤 (T3610 측 — 순서대로, 각각 독립 배포 가능)

### M1 — 수신 엔드포인트 (`/v1/peer/notify`)
- `scripts/hermes-api-server.py`에 라우트 추가: Bearer 인증(`check_auth` 재사용) → 4필드 스키마 검증 → `comment_url` dedup(메모리 + 파일 영속) → JSON 로그 + 가상오피스 이벤트 게시.
- 테스트: `tests/test_peer_notify.py` — 200/401/400/dedup 4계열.
- 배포: 기존 `deploy-local.sh` 경로 (#139 수정본) → **사람 재시작 1회 필요**.

### M2 — 폴링 백스톱 (`peer-comment-poller.py` + timer)
- `scripts/peer-comment-poller.py`: `gh api repos/{repo}/issues/comments?since=<last_seen>` → 자기 계정 외 코멘트 → M1과 동일 처리 경로(내부 함수 재사용 또는 localhost POST).
- `scripts/systemd/hermes-peer-poll.{service,timer}` (`OnUnitActiveSec=5min`) + 설치 스크립트(sudo confirm 플래그 패턴).
- 테스트: 드라이런 모드(`--dry-run`) + 실코멘트 감지 1회.
- **M2만으로 "5분 내 감지" 목표 달성 — Pi 측과 무관하게 가치 발생.**

### M3 — 발신 nudge (T3610 → Pi)
- 코멘트 작성 지점(`kb-eval-publish-issues.py` 등)에 공용 헬퍼 `notify_peer(issue, comment_url)` 추가: `PEER_NUDGE_URL` env 설정 시에만 POST(3회 재시도, 실패는 로그만).
- Pi 측 REQ-DC-101(n8n webhook) 준비 전에는 env 미설정 no-op 상태 유지.

### M4 — 상대측 인계 (raspi5p 담당 — T3610은 계약 문서만 제공)
- 산출물: `docs/peer-notify-contract.md` (nudge 스키마, 엔드포인트, 키 배포 절차, REQ-DC-101~103) 작성 → GitHub 이슈로 Pi 측에 전달.
- GATE-2: Pi의 n8n 워크플로우 변경은 사람 보고/승인 후 Pi 쪽에서 수행. **T3610 세션은 Pi 작업을 직접 하지 않음** (device-role discipline).

## 검증 계획
- 각 마일스톤: 단위 테스트 + AC 대응 (AC-1·2=M1, AC-3·5·6=M2/M3, AC-4=M4 이후 E2E).
- 최종 E2E: Pi 코멘트 → 1초 내 T3610 수신 로그 / 푸시 차단 상태에서 5분 내 폴러 감지.

## 사람 개입 지점 (사전 고지)
1. M1 배포 후 `hermes-api-server` 재시작 (기존 블로커와 동일).
2. M2 timer 설치 (`sudo` + confirm 플래그).
3. hnabyz-bot PAT 발급/배포 (Pi 폴링용, fine-grained 최소권한).
4. M4 Pi 측 구현 착수 승인 (GATE-2).

## 순서 원칙
M1 → M2 완료 시점에 이미 문제(40분 미감지)가 5분으로 해소됨. M3/M4는 5분 → 1초 개선분.
