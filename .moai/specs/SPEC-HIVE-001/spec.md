---
id: SPEC-HIVE-001
title: 이벤트 계약 v2.1 — 화행·홉 상한·단일 기록자·서킷 브레이커
status: Planned
created: 2026-09-09
updated: 2026-09-09
tier: M
owner_device: T3610
related_issues: [148]
source_package: docs/contract, docs/hive, docs/governance, docs/skin, hive/PROTOCOL.md, tools/validate_events.py
---

# SPEC-HIVE-001 — 이벤트 계약 v2.1

## 1. 배경 / 문제 정의

현 이벤트 스키마(`scripts/hermes-api-server.py`)에는 `act`·`requires_reply`·`hops`가 없다. 실측 결손 4건:

| # | 결손 | 결과 |
|---|---|---|
| D1 | 화행 부재 | 수신자가 응답 의무를 판정 못함 |
| D2 | 루프 방어 부재 | peer 간 무한 핑퐁 시 예산 소진까지 정지 수단 없음 |
| D3 | 동시 쓰기 규율 부재 | 다수 peer 동시 커밋 시 `index.lock` 손상 가능 |
| D4 | 폭주 사다리 부재 | pause/resume 2단만 존재 |

원천: Munder Difflin `HIVE.md`·`hive.ts`·`breaker.ts`·`message-queue.md` (MIT) 정독. 상세 분석은 이슈 #148.

## 2. 범위

| 포함 | 제외 |
|---|---|
| 계약 v2.1 필드 4종 추가 (`to` `act` `requires_reply` `hops`) — additive-only | GOD 에이전트 (원칙 3·4 충돌) |
| JSON Schema + 검증기 CI 훅 | Munder Difflin 앱 (Electron) |
| `ra-hive` 저장소 레이아웃 + 단일 커미터 규율 | Buzz 릴레이 (Phase 4 조건부) |
| n8n 라우터: 이송·홉 가드·에스컬레이션 | `board.md`·`tasks.json`·`memory.md` (OpenProject·Honcho 대체) |
| 서킷 브레이커 3단 사다리 (관찰 모드 선행) | 도구별 스테이션 시각화 |
| 살 상태 기계 v2.1 + 목업 35건 | |

## 3. 설계 정본 (이 SPEC이 가리키는 문서)

| 문서 | 역할 |
|---|---|
| `docs/contract/event-contract-v2.1.md` | 계약 정본. §3 대화 규칙이 D1·D2 해법 |
| `docs/contract/event-v2.1.schema.json` | 기계 검증. `actor`에 사람 이름 거부(원칙 9) |
| `docs/hive/hive-layout.md` | D3 해법. 파일당 단일 기록자·단일 커미터 |
| `docs/hive/router-spec.md` | n8n 라우터. 홉 초과 시 **폐기 아닌 사람 에스컬레이션** |
| `docs/governance/circuit-breaker.md` | D4 해법. 한 비트 한 단계, hardStop OFF |
| `docs/governance/delivery-gate.md` | inbox→peer 턴 전달 조건 |
| `docs/skin/avatar-state-machine.md` | 살 상태 기계. 봉투 색=화행 |
| `hive/PROTOCOL.md` | peer 시작 컨텍스트 주입용 규약 |

## 4. 구현 순서

1. 계약 문서 커밋 → `tools/validate_events.py`를 `log.jsonl` 커밋 훅으로 등록
2. `virtual-office/mock/events-v2.1.jsonl` → 살 `DATA_SOURCE=mock` 재생 확인 (v1 필드명 어댑터 필요 여부 확인)
3. `ra-hive` 저장소 생성 (DS224+ Gitea) + `registry/actors.json` — **C1 actor ID 실명 대조 후**
4. `hive/PROTOCOL.md` → Hermes 프로파일(`profiles/souls/*-SOUL.md`) 시작 컨텍스트에 주입
5. n8n 라우터 플로우 — peer 2명(ra_us·ra_eu)으로 시작
6. n8n 브레이커 플로우 — 행동 미발화 관찰 모드
7. 2주 관찰 → `HOP_CAP`·임계 4종 설정 → 행동 발화 ON

## 5. 수용 기준 (DoD)

| 항목 | 기준 |
|---|---|
| A1 | `validate_events.py mock/events-v2.1.jsonl` 오류 0 |
| A2 | 위반 6종 주입 시 exit 1 (자기전달·종결형 답신의무·종결형에 답신·corr 없는 hops·사람 이름 actor·escalation 수신자) |
| A3 | 살이 v2.1 목업을 재생하며 봉투 색이 `act`를 반영 |
| A4 | 라우터가 `hops > HOP_CAP` 메시지를 human inbox에 `escalation`으로 전달, 원본 `.rejected/` 보존 |
| A5 | 라우터 외 프로세스의 `ra-hive` 커밋 0건 |
| A6 | 브레이커 관찰 모드 2주 로그에 `steering` 이상 발생 시 신호 원천 기록 |

## 6. 레포 정합 필수 확인 (커밋 전)

| # | 항목 | 불일치 시 |
|---|---|---|
| C1 | actor ID — `profiles/souls/*` 실명과 `registry/actors.json` 대조 | registry 수정, 계약 무영향 |
| C3 | `virtual-office.html` DATA_SOURCE 필드명(v1) | 어댑터 1개 |
| C5 | Hermes가 peer `idle`·`cache_read` 노출 여부 | delivery-gate §8·breaker §4 대체안 |
| C7 | vote 집계 위치 — 본 SPEC은 `voting/vote-aggregator.js`=n8n 가정 | `vote_result.actor` 조정 |

## 7. 미확정 값 — 실측 후 (지금 정하지 않음)

`HOP_CAP` · 브레이커 임계 4종 · 라우터 폴링 주기 · 전달 최소 간격 · 시작 유예 · `hardStop` ON 여부

## 8. 불변 원칙 영향

충돌 0 · 강화 5 (원칙 3·4·7·8·9) · 유지 4.
