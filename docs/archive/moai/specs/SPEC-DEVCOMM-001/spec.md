---
id: SPEC-DEVCOMM-001
title: T3610↔raspi5p 기기간 소통 채널 — 푸시 + 폴링 백스톱 2계층 알림
status: in-progress
created: 2026-08-05
updated: 2026-08-05
tier: M
owner_device: T3610
counterpart_device: raspi5p
related_issues: []
---

# SPEC-DEVCOMM-001 — 기기간 소통 채널 (Comment Nudge + Reconcile Poll)

## 1. 배경 / 문제 정의

- 양 장치(T3610, raspi5p)는 GitHub 이슈에 각자 계정(holee9 / hnabyz-bot)으로 코멘트를 **쓸 수 있으나**, 어느 쪽도 상대 코멘트를 **감시하지 않음**. 실례: T3610의 2,623자 코멘트가 40분간 미열람 (2026-08-05 딥리서치 결론: "병목은 권한이 아니라 알림 부재").
- 로컬 정찰 확정 사실:
  - T3610에는 어떤 인바운드 워처도 없음 — GitHub 코멘트를 읽는 코드 0건, `.github/workflows/`에 `issue_comment` 트리거 없음 (`kb-eval-publish-issues.py`는 쓰기 전용).
  - raspi5p의 n8n 워크플로우(`n8n/workflows/*.json`)에 GitHub 노드 0개.
  - 알림 수신처 전부 null: `HUMAN_ALERT_WEBHOOK_URL`, `growth-trigger-config.json`의 `n8n_webhook_url`.
  - 기존 양방향 채널 `:8643 /v1/ra/advisory(+feedback)`는 Pi 측 참조 0건으로 미사용 상태였다가, 2026-08-05 E2E로 advisory 경로는 개통됨.
  - 기존 systemd 타이머 5종은 전부 일 1회 — 분 단위 폴러는 신규 유닛 필요.

## 2. 설계 원칙 (기존 제약 계승 — 위반 금지)

| # | 제약 | 근거 |
|---|---|---|
| C1 | 장치간 HTTP 표면은 `:8643` 단일 유지 (Honcho :8000 비노출) | docs/ra-advisory-api.md:17 |
| C2 | Honcho 장애 알림은 Honcho 비경유 (순환 금지) — 본 채널은 Honcho 독립 | docs/implementation-spec.md:180 |
| C3 | T3610은 advisor-only, OpenProject에 쓰기 금지 | docs/ra-advisory-api.md:3 |
| C4 | 실패 시 fail-closed — 채널 장애가 어느 쪽에서도 자율 행동을 트리거하지 않음 (알림 유실 = 폴링이 복구, 그 이상 없음) | docs/ra-advisory-api.md:76 |
| C5 | URL/토큰/주기 등 값은 env·config로 주입, 하드코딩 금지 ([IF] 패턴) | SPEC-RA-TOOL-001 §2.2 |
| C6 | n8n 워크플로우 변경(GATE-2)·systemd 설치(sudo)는 사람 보고/승인 후 | CLAUDE.local.md, GATE 규칙 |
| C7 | GitHub 이슈가 유일한 영구 원장 — 본 채널은 알림(nudge)만 나르고 내용을 저장하지 않음 | 설계 결정 |

## 3. 아키텍처 — 2계층

```
[계층 1: 푸시 nudge — 지연 <1s]
T3610 코멘트 작성 → POST https://n8n.abyz-lab.work/webhook/gh-comment-nudge  (Pi 측 n8n Webhook 트리거)
raspi5p 코멘트 작성 → POST http://100.119.79.28:8643/v1/peer/notify           (T3610 hermes-api-server 신규 엔드포인트, Bearer)

[계층 2: 폴링 백스톱 — 지연 ≤5분, 푸시 유실 자동 복구]
T3610: systemd timer(5분) → gh api repos/.../issues/comments?since=<last_seen> → 자기 계정(holee9) 이외 작성자 코멘트 감지
raspi5p: n8n Schedule(5분) → GitHub REST 동일 폴링 (hnabyz-bot PAT, 60req/hr ≪ 5,000/hr 한도)
```

- nudge 페이로드(공통 스키마): `{ "issue": <번호>, "comment_url": "<url>", "author": "<login>", "ts": "<iso8601>" }` — 본문 미포함(C7).
- 수신 측 동작: nudge 수신 → 즉시 해당 코멘트 fetch → 각자의 처리 큐로 (T3610: 로그 + 가상오피스 이벤트 `{ts,type:"peer_comment",actor,payload}` 게시(기존 이벤트 계약 준수) / Pi: n8n 후속 노드).
- 멱등성: 수신 측은 `comment_url` 기준 dedup — 푸시와 폴링이 같은 코멘트를 중복 전달해도 1회만 처리.

## 4. 요구사항 (GEARS)

### T3610 측 (이 SPEC의 구현 범위)

- **REQ-DC-001** (Ubiquitous): hermes-api-server는 `POST /v1/peer/notify` 엔드포인트를 제공한다. Bearer 인증(`check_auth` 재사용), 스키마 검증(위 4필드), 검증 실패 시 400.
- **REQ-DC-002** (Event): 유효한 nudge 수신 시, 시스템은 `comment_url` dedup 후 수신 로그(`_log_adv_request` 계열 JSON 로그)를 남기고 가상오피스 이벤트를 게시한다. Honcho 기록은 하지 않는다(C2 — Honcho 독립 채널).
- **REQ-DC-003** (Ubiquitous): 신규 폴러 스크립트 `scripts/peer-comment-poller.py`는 `since=<last_seen>` 기반으로 대상 repo의 이슈 코멘트를 조회하고, 자기 계정 외 작성자의 신규 코멘트를 REQ-DC-002와 동일 경로로 처리한다. `last_seen` 상태는 파일(`.moai/state/` 아님 — 런타임 전용 `~/.hermes/` 또는 `/var/lib/`)에 영속.
- **REQ-DC-004** (Ubiquitous): 폴러는 systemd timer `hermes-peer-poll.timer`(`OnUnitActiveSec=5min`, 기존 `hermes-study.timer` 패턴 준수, `EnvironmentFile=scripts/.env`)로 구동. 설치 스크립트는 기존 `install-auto-growth-timer.sh` 패턴(sudo + 명시 confirm 플래그).
- **REQ-DC-005** (Event): T3610이 대상 repo에 이슈 코멘트를 작성하는 기존 경로(`kb-eval-publish-issues.py` 등 gh 사용 지점)가 코멘트 작성 성공 시 Pi nudge URL(`PEER_NUDGE_URL`, env)로 POST한다. 3회 재시도, 최종 실패 시 로그만(C4 — 폴링이 복구).
- **REQ-DC-006** (State): `PEER_NUDGE_URL` 또는 PAT 미설정 시 해당 계층은 조용히 비활성(no-op) — 기존 `n8n_webhook_url` null 패턴과 동일한 fail-open 설정 구조.
- **REQ-DC-007** (Unwanted): 채널의 어떤 실패도 advisory 본 기능(`/v1/ra/advisory`)의 응답 경로에 영향을 주지 않는다 (알림은 부가 기능).

### raspi5p 측 (상대측 작업 — 이 SPEC은 계약만 정의, 구현은 Pi 담당)

- **REQ-DC-101**: n8n Webhook 트리거 `gh-comment-nudge` 신설 — nudge 수신 → 코멘트 fetch → Pi 측 처리(예: OpenProject 활동 기록은 Pi 재량, C3에 따라 T3610은 관여 안 함).
- **REQ-DC-102**: n8n Schedule(5분) + HTTP Request 노드로 GitHub 코멘트 폴링 (hnabyz-bot PAT — n8n credential 유실 사고(2026-06-21) 재발 방지 위해 credential 백업 절차 준수).
- **REQ-DC-103**: Pi가 코멘트 작성 시 `POST :8643/v1/peer/notify` 호출 (기존 advisory와 동일 Bearer 키 또는 별도 키 — 키 배포는 기존 `ra-advisory-raspi5p-integration.md` 절차 재사용).

## 5. 명시적 비범위 (Out of Scope)

- 인프라룸 투표/협의 런타임([IF] 미정 사항) 구현 — 별도 SPEC.
- 사람 알림(폰/메일) — ntfy 등은 후속 확장 후보로만 기록.
- MQTT 브로커 도입 — 2순위 예비안. 장치가 3대 이상으로 늘거나 토픽이 다양해지면 재평가.
- GitHub 웹훅/Tailscale Funnel — 공개 노출 비용으로 기각.

## 6. 수용 기준 (Acceptance Criteria)

- **AC-1**: `POST /v1/peer/notify` — 유효 페이로드 200 + 로그 기록, 무인증 401, 스키마 오류 400. (단위 테스트 + 라이브 curl)
- **AC-2**: 동일 `comment_url` 2회 전송 시 처리 1회 (dedup 검증).
- **AC-3**: 폴러 드라이런 — 테스트 코멘트 작성 후 5분 내 감지 로그 확인.
- **AC-4**: nudge E2E — Pi에서 코멘트 작성 → T3610이 1초 내 수신 로그 (Pi 측 REQ-DC-103 완료 후; 그 전까지는 curl 모의 호출로 대체).
- **AC-5**: `PEER_NUDGE_URL` 미설정 상태에서 기존 전 테스트 회귀 없음 (no-op 확인).
- **AC-6**: advisory 엔드포인트 기존 테스트 전건 통과 (REQ-DC-007).

## 7. 리스크

| 리스크 | 완화 |
|---|---|
| Pi 측 구현 지연 → 반쪽 채널 | T3610 폴러(계층 2)만으로도 "5분 내 감지"가 성립 — 독립 배포 가능 |
| n8n credential 유실 재발 (PAT) | 2026-06-21 사고 절차 준수, PAT는 최소권한 fine-grained |
| 서비스 재시작 필요(:8643 신규 엔드포인트) | 기존 재시작 블로커와 동일 — 사람 재시작 1회 필요, 배포 계획에 명시 |
| 폴러가 자기 코멘트에 반응(루프) | 작성자 필터(자기 계정 제외) + dedup |
