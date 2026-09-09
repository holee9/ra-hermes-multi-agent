# ADR-002: 에이전트 간 메시징 기질 — 파일 기반 hive 프로토콜 우선

- 상태: Proposed (사람 승인 전)
- 날짜: 2026-09-09
- 근거 문서: `docs/research/2026-09-virtual-office/` (ai-office-benchmark, buzz-analysis, munder-difflin-analysis)
- 구현 명세: `.moai/specs/SPEC-HIVE-001/spec.md`

## 맥락

현 이벤트 계약에는 peer 간 논의 매체가 없다(투표는 있으나 회의가 없음). 벤치마크 3종을 검토했다: AI Office(제품 UI), Buzz(Block, Nostr 릴레이), Munder Difflin(파일+git hive).

## 결정

1. **파일 기반 hive 프로토콜을 먼저 이식한다.** Munder Difflin의 화행 7종·홉 상한·단일 커미터·파일당 단일 기록자·커서 멱등성(MIT). 신규 컨테이너 0.
2. **Buzz는 후순위.** 다중 호스트 실시간성 또는 암호학적 신원이 실제로 필요해진 시점의 조건부 후보. Postgres+Redis+S3 요구가 T3610 경합과 충돌.
3. **GOD 에이전트 배제.** 원칙 3(중앙 두뇌 없음)·4(사람=최종 결정자) 충돌. 기능은 n8n(라우팅)·OpenProject(원장)·Gitea(로스터)·사람(조정)에 분배.
4. **정문/창문 분리.** 사람 명령은 기존 정문(n8n webhook)으로만, 살은 `log.jsonl` 읽기 전용. 관찰자 원칙 보존.
5. **홉 초과 시 폐기 대신 사람 에스컬레이션.** MD 코드는 `HOP_CAP=12` 초과 시 drop — 우리는 원칙 4에 따라 사람 호출.

## 결과

- 이벤트 계약 v2.1 (`to`·`act`·`requires_reply`·`hops` 추가, additive-only)
- 불변 원칙 9개 중 충돌 0 · 강화 5 · 유지 4
- 미확정: `HOP_CAP`·브레이커 임계 — 운영 실측 후 설정

## 채택하지 않음

Munder Difflin 앱(Electron) · Stop 훅 자율 루프 · board.md/tasks.json/memory.md · MemPalace · LimeZu 타일셋 · Buzz 내장 포지·워크플로 엔진 · buzz.xyz 호스팅.
