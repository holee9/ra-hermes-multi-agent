# Project Interview Results

Generated: 2026-06-10
Workflow: /moai project (Phase 1.5 Deep Interview)

## Round 1: Ownership and Purpose

**Selection**: 운영 단계 진입 (Operational phase entry)

MVP 5단계가 모두 완료된 상태. GROWTH phases 1-5까지 완전히 구현됨 (warm-start, deriver, delta recording, WP 종결 digest, 성장 지표). 에이전트가 실제 이메일을 수신하며 학습 중인 운영 단계.

문서는 운영 안내 + 할 수 있는 것/할 수 없는 것의 경계를 중심으로 작성.

## Round 2: Architectural Constraints

**Selection**: 하드웨어 토폴로지 고정 (Fixed hardware topology)

3-node 고정 구성:
- **T3610** (Xeon 12C/24T, 32GB, Linux): Honcho server host (FastAPI :8000 + pgvector :5433 + Redis :6379). localhost = T3610. 이 머신은 프로덕션.
- **GX10** (Grace Blackwell ARM): Qwen3 inference (Ollama, OpenAI-compatible). 원격 LAN 접근 전용.
- **Raspberry Pi 5**: OpenProject + n8n automation.

코드에서 localhost를 hardcode하면 안 됨 — `${HONCHO_URL}`, `${GX10_URL}`, `scripts/detect-device.sh` 사용.

추가 제약:
- **GATE-3**: T3610에서의 파괴적 작업 (container deletion, DB reset, volume wipe)은 인간 승인 필수
- **[IF] 패턴**: voting rules, feedback weights 등 학습 매개변수는 외부 config에서 읽음 (하드코딩 금지)
- GATE-1/2/3 규칙: WP close/reopen은 영구적으로 인간 전용

## Round 3: Documentation Priority

**Selection**: 아키텍처 및 모듈 경계 (Architecture and module boundaries)

가장 중요하게 담아야 할 내용:
- Business workspace / Infrastructure workspace 구분
- Honcho 메모리 레이어 (FastAPI → PostgreSQL/pgvector 4096 dims → Redis)
- n8n 브리지 (unidirectional: infra → business)
- 에이전트 간 상호작용 경계 및 게이트 규칙
- 코딩 대상 vs Hermes 런타임 처리 대상 구분
