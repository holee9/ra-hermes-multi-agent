## [HIVE] 이벤트 계약 v2.1 — 화행·홉 상한·단일 기록자·서킷 브레이커

**SPEC**: `.moai/specs/SPEC-HIVE-001/spec.md` · **브랜치**: `feat/hive-v2.1`

### 배경
Munder Difflin(MIT) `HIVE.md`·`hive.ts`·`breaker.ts`·`message-queue.md` 정독 결과, 현 설계 결손 4건 확인. `scripts/hermes-api-server.py`에 `act`·`requires_reply`·`hops` 없음(실측).

| # | 결손 | 해법 | 문서 |
|---|---|---|---|
| D1 | 화행 부재 | `act` 7종 + `requires_reply` | docs/contract/event-contract-v2.1.md |
| D2 | 루프 방어 부재 | `hops` 상한 → **사람 에스컬레이션**(MD는 폐기) | docs/hive/router-spec.md §6 |
| D3 | 동시 쓰기 규율 부재 | 단일 커미터·파일당 단일 기록자 | docs/hive/hive-layout.md |
| D4 | 폭주 사다리 부재 | steer→constrain→stop | docs/governance/circuit-breaker.md |

### 검증 완료
- 목업 35건 `tools/validate_events.py` 통과 (오류 0)
- 위반 6종 주입 → 전부 감지, exit 1
- `actor:"Mike"` 스키마 거부 = 원칙 9 강제

### 채택하지 않음
GOD 에이전트 · MD 앱 · Stop 훅 자율 루프 · board.md/tasks.json/memory.md · MemPalace · LimeZu 타일셋. Buzz는 Phase 4 조건부.

### DoD
SPEC §5 A1–A6. **A1·A2는 이 브랜치에서 이미 충족.**

### 착수 전 필수
SPEC §6 C1·C3·C5·C7 대조. C1(actor ID 실명)이 선행.
