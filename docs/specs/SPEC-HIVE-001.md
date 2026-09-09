# SPEC-HIVE-001 — 파일 기반 hive 프로토콜 이식 (이벤트 계약 v2.1)

- 상태: Draft (ADR-002 Proposed와 연동 — 사람 승인 전)
- 이슈: #150
- 결정: `docs/adr/ADR-002-agent-messaging-substrate.md`
- 이 파일은 **추적되는 정본**이다. 이전에 이슈·ADR이 가리키던 `.moai/specs/SPEC-HIVE-001/spec.md`는 미추적 스캐폴드였고 원격 트리에 존재한 적이 없다(#150 리뷰 5598913943 §1-1). 본 문서는 ADR-002와 아래 명세 문서에서 재구성했으며, 그 문서들에 없는 내용은 §6 "미확정"에 둔다.

## 1. 목적

peer 간 논의 매체가 없는 현 이벤트 계약(v2)에 **화행·홉 상한·단일 기록자·전달 게이트·차단 사다리**를 더해, 사람이 최종 결정자인 채로 RA peer 간 제한적 자동 대화를 가능하게 한다. 중앙 두뇌(GOD) 없음, 살(가상 오피스)은 읽기 전용(ECOSYSTEM 원칙 1·3·4·7).

## 2. 범위

| 결손 | 해법 | 정본 문서 | 구현 종류 |
|---|---|---|---|
| D1 화행 부재 | `act` 7종 + `requires_reply` | `docs/contract/event-contract-v2.1.md` §3 | 계약 |
| D2 루프 방어 부재 | `hops` + `HOP_CAP` + 종결형 | 동 §3.3, `docs/hive/router-spec.md` §6 | 계약 + 라우터 |
| D3 동시 쓰기 규율 부재 | 파일당 단일 기록자·단일 커미터 | `docs/hive/hive-layout.md` §2 | 구현 규율 |
| D4 폭주 차단 사다리 부재 | steer → constrain → stop | `docs/governance/circuit-breaker.md` | n8n 플로우 |
| (전달) | inbox → peer 턴 게이트 | `docs/governance/delivery-gate.md` | 구현 규율 |

범위 밖(ADR-002 "채택하지 않음"): Buzz, Electron 앱, GOD, Stop 훅 자율 루프, board/tasks/memory 파일, 외부 아트 에셋.

## 3. 산출물

| # | 산출물 | 경로 |
|---|---|---|
| A1 | 이벤트 계약 v2.1 + JSON Schema | `docs/contract/event-contract-v2.1.md`, `docs/contract/event-v2.1.schema.json` |
| A2 | 검증기 + 회귀 테스트 + fixture | `tools/validate_events.py`, `tests/test_validate_events.py`, `tests/fixtures/events-v2.1-invalid-mixed.jsonl` |
| A3 | 목업 로그 | `virtual-office/mock/events-v2.1.jsonl` |
| A4 | hive 레이아웃·registry 형식·actor 매핑표 | `docs/hive/hive-layout.md` |
| A5 | 라우터 명세 (n8n) | `docs/hive/router-spec.md` |
| A6 | peer 대면 규약 | `hive/PROTOCOL.md` |
| A7 | 전달 게이트·서킷 브레이커 | `docs/governance/delivery-gate.md`, `docs/governance/circuit-breaker.md` |

## 4. 단계 (P0 → P4) — #150 리뷰 §2의 순서를 그대로 채택

| 단계 | 내용 | 진입 기준 | 상태 |
|---|---|---|---|
| **P0 정본·경계 확정** | 추적 SPEC(본 문서), actor→profile→host 매핑(A4 §4.1), raw/정규화 경계(A5 §2, A6 §2), action enum 확장(A1), 미확인 corr 거부(A5 §3), 상수 "테스트 전용" 표기 | 사람 승인 (ADR 상태 전환 + 파일럿 범위) | 문서 작업 완료, 승인 대기 |
| **P1 검증기·회귀 고정** | 최상위 타입, ts 포맷, 필드 타입 안전성, corr 인과·선행·스키마오류 참조, id 중복, 종료코드 | §5 검증 행렬 통과 | 완료 (tests 46건) |
| **P2 격리 라우터** | normalize → validate → route → deliver → audit → archive 상태 머신, dry-run 기본, 중복 키·수신자별 전달 상태·재시작 복구·단일 lock — **Python 참조 구현** `tools/hive_router.py` (n8n 이식은 P4) | 외부 쓰기 없이 장애 주입 통과 (`tests/test_hive_router.py`) | 참조 구현 완료, 리뷰 대기 |
| **P3 최소 런타임 연결** | `ra_us`·`ra_eu` 2개 peer, 수락/처리 신호, drain gate, hop guard, 수동 pause/resume | 사람 승인한 메시지 예산·실행 시간·복구 절차 | 미착수 |
| **P4 제한 운영·VO 연결** | n8n 변경 사전 보고 후 파일럿, 기존 VO 피드 유지 + 읽기 전용 projection 비교 | 운영 증거 리뷰 후 별도 승인 | 미착수 |

각 단계는 검증 가능한 작은 커밋/PR로 나누고, 변경 파일·실행 명령·결과·미검증·롤백 방법을 #150에 기록한다. 앞 단계의 미해결 계약을 구현자가 임의 기본값으로 메우지 않는다.

## 5. 인수 기준 (검증 행렬)

### 5.1 계약 (P1 — `tests/test_validate_events.py`)

| # | 기준 | 테스트 |
|---|---|---|
| C1 | v2 관찰 이벤트(`to` 없음)가 v2.1 검증기를 통과한다 | `test_v2_observation_event_without_to_passes` |
| C2 | 목업 35건: 오류 0, 경고 1(refuse-deadlock), exit 0 | `test_mock_passes_with_one_deadlock_warning`, `test_cli_exit_codes_0_1_2` |
| C3 | 최상위 null/배열/스칼라, JSON 파싱 실패 → 계약 오류 보고, 예외 없음 | `test_top_level_non_object_*`, `test_load_jsonl_*` |
| C4 | 잘못된 시각·타임존 없는 시각·비문자열 ts → 스키마 오류 | `test_bad_or_tz_less_timestamp_is_schema_error` |
| C5 | id/act/kind/hops/actor/to/corr/requires_reply/conversation 타입 오류 → 스키마 오류, 예외 없음 (정상 이벤트 사이 삽입 포함) | `test_wrong_field_type_*`, `test_invalid_events_interleaved_*` |
| C6 | 종료코드 0/1/2 고정 | `test_cli_exit_codes_0_1_2` |
| C7 | `policy.action`에 `release`·`refuse-invalid` 허용 (additive) | `test_policy_action_release_and_refuse_invalid_accepted` |

### 5.2 대화 (P1)

| # | 기준 | 테스트 |
|---|---|---|
| D1 | 자기전달·종결형 답신요구·broadcast 답신요구 → 오류 | `test_self_send_terminal_reply_and_broadcast_reply_flags` |
| D2 | request→agree 등 정상 corr 체인 통과 | `test_valid_reply_chain_passes` |
| D3 | 미확인 corr·미래 corr·스키마오류 이벤트 참조 corr → 오류 | `test_unknown_corr_*`, `test_future_corr_*`, `test_corr_to_schema_invalid_source_*` |
| D4 | 종결형에 답신·hops 불일치·conversation 불일치·corr 없이 hops≠0 → 오류 | `test_reply_to_terminal_*`, `test_wrong_hops_and_conversation_*`, `test_hops_without_corr_must_be_zero` |
| D5 | 홉 상한 초과는 경고(에스컬레이션 대상), `--strict`에서 실패 | `test_hop_cap_is_warning_and_strict_makes_it_fail` |
| D6 | id 중복 → 오류, ts 역행 → 경고 | `test_duplicate_id_is_error`, `test_ts_regression_is_warning_only` |

### 5.3 내구성·권한·게이트 (P2 — `tests/test_hive_router.py`, 참조 구현 기준)

| # | 기준 | 테스트 |
|---|---|---|
| R1 | dry-run은 어떤 파일도 쓰지 않는다 (CLI 기본) | `test_dry_run_writes_nothing`, `test_cli_dry_run_default_and_exit_codes` |
| R2 | 정상 request: inbox 원자 기록 → log `delivered_to`=실제 성공분 → `.sent/` → cursor; 산출 log가 검증기 오류 0 | `test_request_is_delivered_logged_archived` |
| R3 | 답신은 corr 원인의 conversation 상속·hops+1; 종결형 답신·미확인 corr·자기전달·broadcast 답신요구 → `.rejected/` + `policy(refuse-invalid)` + peer inform | `test_reply_inherits_*`, `test_invalid_message_is_rejected_*`, `test_reply_to_terminal_*` |
| R4 | 비활성 수신자·기록 실패 수신자 → human `escalation(undeliverable)`, 원본 보존 | `test_paused_target_is_escalated_*`, `test_unwritable_target_inbox_*` |
| R5 | broadcast는 발신자 제외 active 전원; 부분 실패 시 성공/미전달 분리 보존 | `test_broadcast_fans_out_*`, `test_partial_broadcast_*` |
| R6 | HOP_CAP 미설정 → 대화 이벤트 보류(전달 없음); 초과 → `escalation(hop-cap)` 1회, 원본 `.rejected/` | `test_hop_cap_unset_holds_*`, `test_hop_cap_exceeded_*` |
| R7 | 장애 주입(inbox 기록 직후 / log append 직전·직후 / archive 직전) 후 재시작 → 중복 inbox·중복 log 없이 완주 | `test_crash_then_restart_*`, `test_partial_broadcast_*` |
| R8 | actor는 outbox 디렉토리가 정본(payload 위장 무시); registry 밖 outbox 무시·보고; `.tmp-*` 무시 | `test_actor_is_taken_from_outbox_directory_*`, `test_outbox_outside_registry_*`, `test_tmp_files_are_ignored` |
| R9 | 단일 실행 lock: 살아있는 pid → 거부(exit 2), 죽은 pid만 인계, 손상 lock은 삭제하지 않음 | `test_lock_held_by_live_pid_*` |
| R10 | id 충돌 시 재발급, 재시도 시 처음 발급 id 보존 | `test_id_collision_is_reissued_*` |

P2에서 **다루지 않은** 행렬 항목(P3/P4로 이월): n8n 배치 중첩·breaker 플로우와의 동시 요청, 사람 registry PR과 라우터 커밋 충돌(git 커밋은 참조 구현 범위 밖 — `run()`이 stage 경로 목록만 반환), busy/startup/paused 게이트(delivery-gate — Hermes idle 신호 실측 필요), 읽음≠완료 확인 신호, breaker 레벨 통지, 비밀값 최소화·원장 중복·OP close/reopen·VO 직접 쓰기 회귀(운영 안전).

## 6. 미확정 (실측 또는 사람 결정 필요)

| 항목 | 현재 표기 | 확정 시점 |
|---|---|---|
| `HOP_CAP` | 미확정. 미설정 시 대화 전달 비활성 (A5 §6) | P3 관찰 후 사람 승인 |
| 브레이커 비트 60s / 진행 창 300s / 트립 임계 | 테스트 전용 기본값 | P3/P4 사람 승인 |
| 폴링 주기 15s | 테스트 전용 기본값 | 동일 |
| 분산 파일 접근 | T3610/GX10 peer와 rpi5 라우터가 같은 `ra-hive` 워킹카피를 어떻게 공유하는지 미정. Gitea repo 존재 ≠ 공유 파일시스템 | P2 설계 결정 (사람) |
| 관측 피드 전환 | 기존 VO의 Honcho 기반 기록과 새 `log.jsonl`의 관계. 즉시 교체 금지, P4에서 읽기 전용 projection으로 병행 비교 | P4 |
| `inform` 처리 완료 신호 | 선택적 ack 이벤트 vs 세션 로그 턴 종료 (A7 delivery-gate §5.1) | P3 Hermes 실측 |
| Hermes idle 노출 여부 | 미확인. 미노출 시 자동 전달 금지 | P3 |
| `ra_case` 프로필 | 미존재 → `paused` | 프로필·SOUL PR 후 |
| op_manager / infra_gx10 / infra_rpi 상주 호스트 | 프로필은 T3610에만 확인됨 | 각 호스트 setup.sh 실행 후 매핑표 갱신 |

## 7. 사람 제어 권한 (변경 없음)

- WP 완료·재오픈: 사람 전용 (CLAUDE.md Gate Rules).
- `policy(action:resume)`·`release`: 정문(n8n webhook / Telegram / 오피스 컴포저) 경유 사람만.
- registry·identity.md·PROTOCOL.md: PR 머지로만 변경.
- n8n 워크플로 변경·운영 배포: 사전 보고 후 승인.
