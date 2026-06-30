# RA Hermes 멀티 에이전트 시스템

> 의료기기 인허가(RA) 도메인의 **정확성·신뢰성 우선** 학습 멀티 에이전트 시스템. 에이전트는 사람 RA 전문가를 *보조*한다.
> Hermes Agent v0.15.1 / Honcho v0.15.1 기반. 사실 기준일: 2026-06-21.

**[사용 가이드 →](docs/usage-guide.md)** | [📘 인터랙티브 사용 매뉴얼](docs/user-guide-korean.html) | [마스터 설계서 (Hermes v0.15.1)](docs/RA-multi-agent-master-design.md) | [구현 명세](docs/implementation-spec.md) | [운영 전략](docs/operations-guide.md) | [🌐 원격 접속 가이드](docs/remote-access-guide.md) | [🔧 테스트케일 망 설정 가이드](docs/tailscale-setup-guide.md) | [성장 대시보드 바로보기](https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html) | [대시보드 운영 문서](docs/growth-dashboard.md)

GLM-5.2/Z.ai 전환은 [GLM-5.2 설정 메모](docs/glm-5.2-setup.md)를 따른다. 기본 운영 경로는 GX10 `gpt-oss:120b`이며, `scripts/configure-glm.sh`로 필요한 프로파일만 OpenAI-compatible GLM endpoint로 바꿀 수 있다.

---

## 현재 상태

**✅ 구축 완료 · 인터랙티브 사용 매뉴얼 배포 · 상세 스크린샷 시스템 완료(19개) · 시스템 운영 가이드 제공** | 최종 갱신: 2026-06-28

**최신 완료 작업:**
- ✨ **가상 오피스 세부내용(detail) 창 확대** (2026-06-30): 기록창 하단 세부내용 창(`.detail-panel`) max-height 220→440px(+220). 행 클릭 시 상세 하단이 잘려 스크롤해야 하던 문제 해결. `max-height` 기반이라 **내용 양에 따라 0~440px 동적 높이**(내용 적으면 그만큼 축소) — 이 동작으로 확정(사용자 확인 완료). `.log` 220px는 유지. Docker rebuild 반영(포트 3001). 커밋 `ed0c20a`.
- 🐛 **가상 오피스 최신 activity 미표시 버그 수정** (2026-06-28, [#95](https://github.com/holee9/ra-hermes-multi-agent/issues/95)): adapter `postJson`이 `path`에 query string(search)을 버려 항상 page 1(oldest 50)만 조회 → RA 전문가 자문·raspi5p 실행 최신이 대시보드에 누락되고 page 재호출로 중복 수집. `pathname + search` + `?page=N` 순회로 수정. 검증: advisory_returned 50→114건, latest 14:02 KST(기존 06-26). 커밋 `ce9cad0`. (#96 회귀 의심은 오판 정정 — ra_advisory 정상 기록 중)
- 🛡️ **raspi5p 자문 실행 게이트 안전 강화 + unclear_region 해소** (2026-06-27, [#91](https://github.com/holee9/ra-hermes-multi-agent/issues/91)·[#88](https://github.com/holee9/ra-hermes-multi-agent/issues/88)): raspi5p `hermes_fallback`이 T3610 yellow(사람 승격)을 우회 실행하던 결함 수정 — advisoryGate에 `yellow_review`/`no_action` → `allowMutation:false` 분기 추가(hermes_fallback 경로 전, fail-closed 보장). raspi5p `region_hint` 프로덕션 v6 적용 + caller timeout `620000ms`(T3610 `ADVISORY_TIMEOUT=600`+20s). T3610은 advisory 요청 query+region_hint 로깅 추가([#92](https://github.com/holee9/ra-hermes-multi-agent/issues/92)). 교차검증: raspi5p n8n DB 배포 v6 + 런타임(region_hint 적용 후 unclear 0건·우회 0건).
- 🩺 **T3610 RA 자문 백엔드 → raspi5p Hermes 연동 기반** (2026-06-24, [#83](https://github.com/holee9/ra-hermes-multi-agent/issues/83)): T3610 RA agent를 raspi5p의 **RA 자문 backend**로(실행권한 이동 없음). `POST /v1/ra/advisory`·`/feedback`(8643 Bearer) — 서버측 키워드 라우팅·검증(actor underscore·저신뢰/근거없음→Yellow)·Honcho 기록(로컬만). raspi5p(Iris) 캐릭터 + advisory 이벤트 대시보드 가시화. live 전 검증(단위 25 PASS + live 단일/다중/Yellow/feedback/옵저버). 커밋 `b564156`(+review 수정). 상세: [docs/ra-advisory-api.md](docs/ra-advisory-api.md).
- 🏢 **가상 오피스 → 실제업무 대시보드 전환** (2026-06-24, [#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81)): 옵저버가 메일(activity_log)만 보던 한계 해소 — `metadata.record_type` 기반 매핑으로 RA 일일 학습(growth_case)·사람 KB-eval 평가(score_given)까지 표시. 하단 기록창 확대·폭 정렬 + 클릭 상세 패널(소스·도메인·점수·차원). 새 이벤트 실시간 애니메이션 사용자 브라우저로 검증. 커밋 `0f28c50`·`3b50e0e`.
- 🛡️ **RA 본질 견고성 개선** (2026-06-23, [#80](https://github.com/holee9/ra-hermes-multi-agent/issues/80)): Contract A confidence 타입 위반 수정·knowledge_fetch 에러 분류+로깅·openFDA 429 감지·growth-metrics 타임존 KST 보정. 회귀 테스트 추가(`verify-growth-metrics` H1·`verify-knowledge-fetch` 신규 H2/H3). py_compile + verify PASS. peer_id 하이픈 감별 위반 0건. 픽셀 아트(WCAG 팔레트+안경/수염) 시각 확인 완료.
- 🧭 **생태계 의사결정 원칙 전면 개정** (2026-06-21, `ECOSYSTEM-DECISION.md`): ECOSYSTEM 헌장(1·3·8) 기반 매 작업 전 4문 자문 훅. mail-triage/Gmail ⬇ 보류(Low), RA 자율 학습/지식/사람-에이전트 협업 ⬆ High.
- ✉️ **Gmail OAuth RPi→T3610 이전** (2026-06-21, [#75](https://github.com/holee9/ra-hermes-multi-agent/issues/75)): credential 이전(연결 test 200). 단 n8n 2.26.7 폴링 호환 에러로 **메일 처리 미동작 — mail-triage 보류**(채널 중 하나). **2026-06-23 정정: 이전 취소, n8n=RPi 정위치 복귀** (아래 "n8n 운영 위치" 참조).
- 🎮 **가상 오피스 재생→관측 모델 전환** (2026-06-21, [#74](https://github.com/holee9/ra-hermes-multi-agent/issues/74)): 관측 전용(read-only)으로 전환 — 재생 메타포 폐지, 과거는 정적 로그, 새 활동만 실시간 애니메이션, Heat Map 실데이터. chromium 렌더링 e2e 검증 완료.
- 🔧 **n8n credential 유실 복구** (2026-06-21, [#75](https://github.com/holee9/ra-hermes-multi-agent/issues/75)): DB credential 0건 → OP credential+URL(192.168.100.50:8080) 복구. OP 경로 e2e 4종 PASS.
- 🔍 **구현 전수 점검 완료** (2026-06-21): `[구현]` 30개 마커 ↔ 산물 대응, n8n 워크플로우 10개·SAFETY 게이트 검증(13/13 PASS)·growth snapshot 12개 전부 확인. **구현층 완결** — 남은 작업은 전부 외부 의존(30일 metrics·사람 승인·POC 평가). 시스템 🟢 NORMAL.
- 🔒 **n8n 보안 강화** (2026-06-21): 시크릿(JWT/BASIC_AUTH/POSTGRES) env화 + 강력 난수화, N8N_API_KEY 재발급(API 200), 보안 산물 gitignore 분리 — `reports/security-audit-2026-06-21.md`
- 📘 **상세 스크린샷 시스템**: 19개 포괄적인 시스템 캡쳐 자동 생성 (마스터 인덱스 포함)
- 📊 **E2E 검증 완료**: 모든 캡쳐가 실제 시스템 데이터와 상태 정보 포함
- 🔧 ~~**T3610 단일 n8n 운영**: 4개 워크플로우 import 및 활성화 완료~~ → **2026-06-23 철회** (반쪽짜리 이전, n8n=RPi 복귀)
- 📖 **문서 최신화**: 주요 문서 2026-06-21 기준

## 🏗️ 구축된 시스템 구성요소 상세

### 🤖 RA 에이전트 (8종 AI 전문가)

**모두 실제 작동 중** - 각 에이전트는 독립 SOUL.md와 전문 분야를 보유:

| 에이전트 | 역할 | SOUL.md | Honcho Peer ID | 작동 상태 |
|---------|------|---------|---------------|----------|
| **Mike (ra-us)** | FDA 510(k) 전문가 | ✅ 구축 완료 | `ra_us` | ✅ 활성 |
| **Theo (ra-eu)** | EU MDR 전문가 | ✅ 구축 완료 | `ra_eu` | ✅ 활성 |
| **Sam (ra-kr)** | MFDS/KGMP 전문가 | ✅ 구축 완료 | `ra_kr` | ✅ 활성 |
| **Margot (op-manager)** | OpenProject 사안 담당 | ✅ 구축 완료 | `op_manager` | ✅ 활성 |
| **Olly (n8n-manager)** | n8n 자동화 담당 | ✅ 구축 완료 | `n8n_manager` | ✅ 활성 |
| **Finn (infra-t3610)** | T3610 인프라 모니터링 | ✅ 구축 완료 | `infra_t3610` | ✅ 활성 |
| **Leo (infra-gx10)** | GX10 LLM 추론 관리 | ✅ 구축 완료 | `infra_gx10` | ✅ 활성 |
| **Gus (infra-rpi)** | RPi 인프라 관리 | ✅ 구축 완료 | `infra_rpi` | ✅ 활성 |

**특징**: 규제권별 철학이 다른 3종 RA 전문가, 실제 업무 경험과 피드백으로 성장

---

### 🏢 가상 오피스 (픽셀 아트 실제업무 대시보드)

**구축 완료: RA 조직의 실제 업무(학습·평가·메일 처리)를 실시간으로 비추는 읽기 전용 모니터링 대시보드**

메일 트리아지뿐 아니라 **RA 일일 학습(daily-growth)·사람 KB-eval 평가**까지 표시한다. 메일이 들어오지 않아도 학습 루프가 살아 있으면 오피스가 움직인다 — CLI 없이도 프로젝트 활동 이력을 파악하는 것이 목적이다.

| 컴포넌트 | 상태 | 특징 |
|----------|------|------|
| **virtual-office.html** | ✅ 구축 완료 | 픽셀 오피스(760×440) + 하단 기록창(상단 폭 정렬·확대) + 클릭 상세 패널 |
| **캐릭터 시각화** | ✅ 구축 완료 | 코드 기반 픽셀 캐릭터 (Kenney CC0 교체 가능), WCAG 팔레트 |
| **캐릭터-에이전트 매핑** | ✅ 구축 완료 | actor ID ↔ 캐릭터 자동 매핑 (ra_us/eu/kr·op/n8n manager·infra 3종·human·system) |
| **실제 업무 매핑** | ✅ [#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81) | `metadata.record_type` 기반 — daily_growth_case→학습, score_given→평가, activity_log→메일 |
| **Honcho 실데이터 연동** | ✅ 구축 완료 | 어댑터가 Honcho 세션/메시지 폴링 → 이벤트로 변환·렌더링 |
| **이벤트 시각화** | ✅ 구축 완료 | mail_received·matched·comment_added·transition_proposed·vote_*·score_given·growth_case |
| **클릭 상세 이력** | ✅ [#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81) | 기록 행 클릭 → 하단 패널에 소스·도메인·점수·평가차원 등 상세 표시 |
| **실시간 애니메이션** | ✅ [#81](https://github.com/holee9/ra-hermes-multi-agent/issues/81) 검증 | 새 이벤트만 캐릭터 반응, 과거는 정적 로그 (활동 없으면 조용함 = 정상 신호) |
| **Docker 컨테이너 배포** | ✅ 구축 완료 | 단일 컨테이너, `DATA_SOURCE=mock\|honcho` 전환 |
| **E2E 테스트** | ✅ 구축 완료 | 11개 Playwright 테스트 케이스 |

**작동 모드**: 읽기 전용 관찰자. `DATA_SOURCE`로 목업/Honcho 전환. 폴링(기본 30초) 중 새 이벤트가 오면 해당 캐릭터가 반응한다. 접속: `http://192.168.100.200:3001` / Tailscale `http://100.119.79.28:3001`.

---

### 📊 성장 대시보드 (Growth Dashboard)

**구축 완료: GitHub Pages 기반 정적 HTML 대시보드**

| 컴포넌트 | 상태 | 특징 |
|----------|------|------|
| **growth-dashboard.html** | ✅ 구축 완료 | standalone HTML snapshot (외부 의존 없음) |
| **RA Growth Operations 요약** | ✅ 구축 완료 | 전체 시스템 성장 현황 한눈에 파악 |
| **담당자별 성장 카드** | ✅ 구축 완료 | ra_us/ra_eu/ra_kr 개별 성장 추적 |
| **Growth Signal Flow** | ✅ 구축 완료 | 성장 신호 흐름 시각화 |
| **성장 측정 상태** | ✅ 구축 완료 | Trend Verdict, Evidence Radar 차트 |
| **커버리지 근거** | ✅ 구축 완료 | coverage-guards.json 기반 판정 |
| **inline SVG/CSS** | ✅ 구축 완료 | 독립 렌더링 (외부 fetch 없음) |

**데이터 소스**: reports/growth-YYYY-MM-DD.json, systemd 상태(`ra-growth-metrics.timer` active/enabled), readiness matrix 16/16. 집계 로직은 정상 작동한다(06-17~19 snapshot: 27 sessions / 302 messages). 06-20 snapshot은 timer 실행 시점의 Honcho 500 오류(`POST /v3/workspaces/work/sessions/list`)로 0건으로 회귀했고 현재는 복구됨 — `scripts/check-growth-metrics-health.py`로 매일 회귀를 감지한다(건강도 85/100). 행동/사람 피드백 metric 값이 아직 없어 Growth Trend Verdict는 warning을 유지한다.

---

### 🔧 Honcho 백엔드 시스템

**구축 완료: FastAPI + PostgreSQL + Redis + Deriver**

| 컴포넌트 | 상태 | 포트/구성 |
|----------|------|----------|
| **Honcho API** | ✅ 구축 완료 | :8000 (LAN 오픈) |
| **Deriver 워커** | ✅ 구축 완료 | 2 worker, flush 활성화 |
| **PostgreSQL/pgvector** | ✅ 구축 완료 | :5433 (4096차원, 1493 sources) |
| **Redis** | ✅ 구축 완료 | :6379 (루프백크) |
| **Workspace 2개** | ✅ 구축 완료 | work (업무), infra (인프라) 격리 |
| **Docker Compose** | ✅ 구축 완료 | 일관 기동 가능, T3610 운영 |

**환경**: T3610 단일 운영, GX10 Qwen3 연동 (tool calling 지원)

---

### ⚙️ n8n 워크플로우 자동화

**구축 완료: 4개 핵심 워크플로우 활성화**

| 워크플로우 | 상태 | 기능 |
|-----------|------|------|
| **mail-triage.json** | ✅ 구축 완료 | Gmail → RA 분석 → OpenProject 자동화 |
| **infra-vote-broadcast.json** | ✅ 구축 완료 | 인프라 3종 투표 브로드캐스트 |
| **feedback-recorder.json** | ✅ 구축 완료 | 3점 평가 → Honcho 기록 |
| **infra-to-work-bridge.json** | ✅ 구축 완료 | 인프라 → 업무 workspace 단방향 전달 |
| **form-triage-draft.json** | ✅ 구축 완료 | 폼 입력 처리 (gate 닫힘, 30일 metrics 미달) |

**안전 게이트**: Yellow 게이트 (low confidence → 사람 검토), WP 상태 검증, 환경변수 외부화 완료

---

### 💬 대화하는 칸반 (Interactive Components)

**구축 완료: RA 에이전트와 실제 대화하는 시스템**

| 컴포넌트 | 상태 | 특징 |
|----------|------|------|
| **Hermes Chat Completions API** | ✅ 구축 완료 | `/v1/chat/completions` 실시간 응답 |
| **세션 기반 대화** | ✅ 구축 완료 | SQLite 세션 히스토리, 문맥 유지 |
| **자기개선 루프** | ✅ 구축 완료 | 성공 워크플로우 → 스킬 자동 변환 |
| **Kanban 보드** | ✅ 구축 완료 | v0.13.0 (heartbeat, reclaim, zombie detection) |
| **메모리 시스템** | ✅ 구축 완료 | honcho_search, honcho_context, honcho_conclude |
| **Layer 4 RAG** | ✅ 구축 완료 | 실시간 규제 DB 조회 (openFDA, law.go.kr, data.go.kr) |

---

### 📚 지식 인프라 (Knowledge Infrastructure)

**구축 완료: pgvector 기반 지식베이스**

| 컴포넌트 | 상태 | 데이터 |
|----------|------|------|
| **pgvector ra_knowledge** | ✅ 구축 완료 | 1493 sources 인덱싱 완료 |
| **RA 프로젝트 레포** | ✅ 구축 완료 | ra-project + MD-process 마크다운 |
| **llm-wiki (NAS Gitea)** | ✅ 구축 완료 | DR_RnD/ra-llm-wiki 990 sources |
| **source curriculum seed** | ✅ 구축 완료 | ra_us 48, ra_eu 31, ra_kr 48 sources |
| **Layer 4 API 서버** | ✅ 구축 완료 | `/v1/knowledge/fetch` 실시간 조회 |

---

## 📸 실제 구동 현황 (E2E 검증 완료)

| 컴포넌트 | 상태 | 검증 상태 | 문서화 |
|----------|------|----------|--------|
| Honcho 서버 | ✅ 운영 중 | API :8000 정상 응답 확인 | ✅ 상세 캡쳐 완료 |
| 가상 오피스 | ✅ 구동 중 | 실제업무 대시보드 (학습/평가/메일 record_type 매핑) + 클릭 상세 패널 (#81, 재생→관측 전환 #74) | ✅ 상세 캡쳐 완료 |
| 성장 대시보드 | ✅ 배포 중 | GitHub Pages 렌더링, 16/16 readiness 확인 | ✅ 상세 캡쳐 완료 |
| n8n 워크플로우 | ✅ 활성 | 4개 workflow import/activate 상태 확인 | ✅ 상세 캡쳐 완료 |
| RA 에이전트 | ✅ 응답 중 | Hermes API 통해 실제 대화 가능 | ✅ 상세 캡쳐 완료 |
| Honcho 세션 관리 | ✅ 운영 중 | 142 활성 세션, 302 메시지 처리 | ✅ 상세 캡캡 완료 |
| 지식 베이스 | ✅ 운영 중 | pgvector 1493 sources 인덱싱, 검색 정상 | ✅ 상세 캡쳐 완료 |
| 인프라 투표 시스템 | ✅ 구동 중 | 3개 인프라 에이전트 투표 활성 | ✅ 상세 캡쳐 완료 |

**E2E 검증**: 모든 컴포넌트가 실제 환경(T3610)에서 구동 중임을 확인

### 🎯 상세 스크린샷 시스템 (2026-06-19 완료)

총 **19개**의 포괄적인 시스템 캡쳐가 생성되었습니다. 각 캡쳐는 실제 시스템 데이터와 E2E 검증 상태를 포함합니다.

**📘 마스터 인덱스**: [docs/screenshots/00-master-index.html](docs/screenshots/00-master-index.html)

**카테고리별 캡쳐 개요:**
- **시스템 개요 및 아키텍처** (4개): 기본 + 상세 아키텍처, Honcho API
- **에이전트 및 인터페이스** (4개): 가상 오피스, 대화 시스템  
- **모니터링 및 자동화** (4개): 성장 대시보드, n8n 워크플로우
- **전문 기능 분석** (6개): 세션, 지식, 트라이지, 투표, 성과, 통합
- **기능 플로우 및 시나리오** (6개): 이메일 E2E, 협업, 검색, 결정, 학습, 모니터링

---

| 단계 | 상태 | 이슈 |
|---|---|---|
| 설계 | ✅ 완료 | [#12 ADR-001](https://github.com/holee9/ra-hermes-multi-agent/issues/12) (closed) |
| 골격 코드 구현 | ✅ 완료 | — |
| Honcho T3610 배포 | ✅ 완료 | [#3](https://github.com/holee9/ra-hermes-multi-agent/issues/3) |
| MVP 자동화 스크립트 (SPEC-RA-TOOL-001) | ✅ 완료 | [#16](https://github.com/holee9/ra-hermes-multi-agent/issues/16) |
| RA 프로파일 생성 (PROFILE-1, PROFILE-2) | ✅ 완료 | [#4](https://github.com/holee9/ra-hermes-multi-agent/issues/4), [#6](https://github.com/holee9/ra-hermes-multi-agent/issues/6) |
| SKILL.md 심화 이식 | ✅ 완료 | [#13](https://github.com/holee9/ra-hermes-multi-agent/issues/13) |
| 지식베이스 연결 | ✅ 완료 | [#15](https://github.com/holee9/ra-hermes-multi-agent/issues/15) |
| hermes-ra 스크립트 이전 | ✅ 완료 (아카이브는 #11 게이트) | [#14](https://github.com/holee9/ra-hermes-multi-agent/issues/14) |
| n8n mail-triage 배포 (WORKFLOW-1) | ✅ 완료 | [#5](https://github.com/holee9/ra-hermes-multi-agent/issues/5) |
| 가상오피스 Honcho v3 API 연결 | ✅ 완료 (mail-triage 데이터 대기) | [#10](https://github.com/holee9/ra-hermes-multi-agent/issues/10) |
| MVP Cold Start 검증 | ✅ 완료 | [#11](https://github.com/holee9/ra-hermes-multi-agent/issues/11) (closed) |
| 인덱싱 스크립트 Qdrant → pgvector (MIGRATE-1) | ✅ 완료 | [#17](https://github.com/holee9/ra-hermes-multi-agent/issues/17) (closed) |
| extract_mail_qa.py Qdrant → pgvector (MIGRATE-2) | ✅ 완료 | [#19](https://github.com/holee9/ra-hermes-multi-agent/issues/19) (closed) |
| OpenProject → Honcho backfill (SEED-1) | ✅ 완료 (OP 토큰 갱신 + backfill 스크립트) | [#18](https://github.com/holee9/ra-hermes-multi-agent/issues/18) |
| warm-start 학습 루프 구축 (GROWTH-1,2) | ✅ 완료 (Honcho 컨텍스트 조회 + 프롬프트 주입 + deriver 활성화) | [#20](https://github.com/holee9/ra-hermes-multi-agent/issues/20), [#21](https://github.com/holee9/ra-hermes-multi-agent/issues/21) (closed) |
| feedback-recorder delta 페어링 (GROWTH-3) | ✅ 완료 (agent_judgment/human_correction/dimensions 기록) | [#22](https://github.com/holee9/ra-hermes-multi-agent/issues/22) (closed) |
| WP 종결 → case digest 자동 기록 (GROWTH-4) | ✅ 완료 (wp-close-recorder.json — OP webhook → Honcho AI peer) | [#23](https://github.com/holee9/ra-hermes-multi-agent/issues/23) (closed) |
| 일일 성장 지표 측정 인프라 (GROWTH-5) | ✅ 완료 (growth-metrics.py 5개 지표 + systemd timer 가이드) | [#24](https://github.com/holee9/ra-hermes-multi-agent/issues/24) (closed) |
| Layer 4 실시간 지식 통합 (llm-wiki/openFDA/law.go.kr) | ✅ 완료 (law.go.kr HTTP 수정, openFDA/law.go.kr E2E 검증 완료, graceful degradation 확인) | [#30](https://github.com/holee9/ra-hermes-multi-agent/issues/30) (closed) |
| Layer 4d data.go.kr MFDS DB 통합 (제조수입업허가/추적관리) | ✅ 완료 (DATA_GO_KR_API_KEY 통일, 2/3 서비스 E2E 검증) | [#31](https://github.com/holee9/ra-hermes-multi-agent/issues/31) (closed) |
| Layer 4d data.go.kr 품목허가(15057456) 3/3 서비스 완성 | ✅ 완료 (MdlpPrdlstPrmisnInfoService05, nested item 처리, 6건 E2E 검증) | [#33](https://github.com/holee9/ra-hermes-multi-agent/issues/33) (closed) |
| 정확성·신뢰성 우선 철학 전사 이식 | ✅ 완료 (CLAUDE.md·마스터설계·구현명세·운영전략·ra-us SOUL 전 문서 반영, cold start Yellow 게이트 기본값 명시) | [#32](https://github.com/holee9/ra-hermes-multi-agent/issues/32) (closed) |
| SaMD/SiMD 분류 보정 (ra-us/eu/kr SOUL.md) | ✅ 완료 (HnVUE=SaMD, Retrofit=SiMD 명시, SOUL.md 3종 테이블 갱신) | — |
| Phase 2~5 로드맵 문서화 | ✅ 완료 (master-design §12-§13, implementation-spec P2-P4, operations-guide §5 갱신) | [#34](https://github.com/holee9/ra-hermes-multi-agent/issues/34)~[#41](https://github.com/holee9/ra-hermes-multi-agent/issues/41) |
| Gitea API 인덱싱 지원 추가 (DR_RnD/ra-llm-wiki) | ✅ 완료 (Gitea 990 소스 pgvector 인덱싱 완료, ra_knowledge 총 1493 sources) | [#35](https://github.com/holee9/ra-hermes-multi-agent/issues/35) (closed) |
| hermes-api-server.py 버전 관리 편입 + deploy-local.sh | ✅ 완료 (Layer 4 API 서버 git 편입, /opt/hermes-ra/ 동기화 스크립트, .env.example GITEA_URL 등 추가) | [#37](https://github.com/holee9/ra-hermes-multi-agent/issues/37) (연관) |
| doc-converter NAS→pgvector 인덱싱 | ✅ 완료 (llm-wiki + #35 인덱싱으로 목적 충족, 별도 구현 불필요, scripts/doc-converter/ 삭제) | [#36](https://github.com/holee9/ra-hermes-multi-agent/issues/36) (closed) |
| growth-metrics systemd 타이머 + 트리거 알림 자동화 | ✅ 완료 (check_and_notify_triggers 추가, systemd/ra-growth-metrics.{service,timer} 생성, T3610 배포 명령 이슈 기록) | [#38](https://github.com/holee9/ra-hermes-multi-agent/issues/38) (closed) |
| 팀장 에이전트 자리 예약 + 확장 가이드 초안 | 🔄 진행 중 (coordinator-SOUL.md 미활성 초안, agent-expansion-guide.md 작성 완료, growth-metrics 카테고리 분류는 운영 데이터 필요) | [#41](https://github.com/holee9/ra-hermes-multi-agent/issues/41) |
| 에이전트 자율 학습 루프 (GROWTH-7) | ✅ 완료 (Layer 4 7소스, autonomous-study-scheduler.py Bootstrap/Delta 모드, 피어 교환, systemd 타이머, growth-metrics 지표 2개 추가) | [#42](https://github.com/holee9/ra-hermes-multi-agent/issues/42) (closed) |
| 자율 학습 peer_id 오염 복구 | ✅ 완료 (wrong-peer live messages/embeddings/queue refs/session peers 0, raw payload 2,085건 `ra_us`/`ra_eu` clean replay, JSONL 감사 백업 보존) | [#48](https://github.com/holee9/ra-hermes-multi-agent/issues/48), [#49](https://github.com/holee9/ra-hermes-multi-agent/issues/49), [#56](https://github.com/holee9/ra-hermes-multi-agent/issues/56) (closed) |
| source-level curriculum seed fast-track | ✅ 완료 (`ra_us` 48개, `ra_eu` 31개, `ra_kr` 48개 source seed processed, `curriculum_seed` JSON envelope 0, `ra_kr` all-scope idempotence `to_seed=0`) | [#50](https://github.com/holee9/ra-hermes-multi-agent/issues/50) (closed), [#60](https://github.com/holee9/ra-hermes-multi-agent/issues/60) (closed) |
| 비메일 성장 cadence loop | ✅ 구현 완료·운영 timer off (`hermes-auto-growth.timer` inactive/disabled, RA pending 0, 수동 readiness 16/16 확인, activation은 명시 승인 필요) | [#50](https://github.com/holee9/ra-hermes-multi-agent/issues/50) (closed), [#51](https://github.com/holee9/ra-hermes-multi-agent/issues/51) (closed), [#52](https://github.com/holee9/ra-hermes-multi-agent/issues/52) (closed), [#53](https://github.com/holee9/ra-hermes-multi-agent/issues/53) (closed), [#54](https://github.com/holee9/ra-hermes-multi-agent/issues/54) (closed), [#55](https://github.com/holee9/ra-hermes-multi-agent/issues/55) (closed), [#57](https://github.com/holee9/ra-hermes-multi-agent/issues/57) (closed), [#60](https://github.com/holee9/ra-hermes-multi-agent/issues/60) (closed) |
| 자동성장 pre-production hardening | ✅ 목표치 완료 (`auto-growth-readiness-report.py` 4x4 matrix 16/16, timer OFF 유지, `ra_kr` self-doc 638로 legacy pre-activation floor 통과. 이 20% floor는 전문가 성숙도 기준이 아님) | [#58](https://github.com/holee9/ra-hermes-multi-agent/issues/58) (closed), [#59](https://github.com/holee9/ra-hermes-multi-agent/issues/59) (closed), [#60](https://github.com/holee9/ra-hermes-multi-agent/issues/60) (closed) |
| mail-triage Yellow 게이트·사람 알림 강화 | ✅ RPi n8n import/activate, mail-triage Yellow smoke 완료 | [#43](https://github.com/holee9/ra-hermes-multi-agent/issues/43) |
| 기존 WP 매칭 시 OpenProject 상태 검증 | ✅ RPi n8n import/activate 완료 (통제된 closed-WP side-effect E2E는 별도 테스트 WP에서 수행) | [#44](https://github.com/holee9/ra-hermes-multi-agent/issues/44) |
| n8n 워크플로우 env/config 외부화 | ✅ RPi n8n env/compose 반영, workflow import/activate 완료 | [#45](https://github.com/holee9/ra-hermes-multi-agent/issues/45) |
| npm test 품질 게이트 복구 | ✅ 완료 (`test:static` + Playwright E2E 11건) | [#46](https://github.com/holee9/ra-hermes-multi-agent/issues/46) |
| 문서 상태 불일치 정리 | ✅ 완료 (README·설계·운영·생태계·상태 문서 동기화) | [#47](https://github.com/holee9/ra-hermes-multi-agent/issues/47) |
| 아키텍처 문서화 (Codemaps + SPEC-ARCH-001) | ✅ 완료 (전체 시스템 아키텍처 분석, 4개 codemaps + SPEC-ARCH-001 생성) | Codemaps 완료 |
| 제로 베이스 프로젝트 상태 재정렬 | ✅ 완료 (목표·현황·잔여 작업을 대시보드가 아니라 RA 전문가 성장 운영 기준으로 재정렬) | [#63](https://github.com/holee9/ra-hermes-multi-agent/issues/63) |
| 성장 지표 ingestion/data contract 보정 | ✅ 완료 (Honcho v0.15.1 `POST /sessions/list`·`POST /sessions/{id}/messages/list` 계약 반영, 2026-06-19 report 27 sessions/302 messages scanned) | [#64](https://github.com/holee9/ra-hermes-multi-agent/issues/64) |
| 자동성장 threshold/notification 정책 | ✅ 완료 (threshold null 정책·검증 추가, 30일 유효 metrics 전까지 자동 알림 비활성, error handling/dashboard/auto-copy/day15-checklist 구현) | [#65](https://github.com/holee9/ra-hermes-multi-agent/issues/65) |

> **README 갱신 규칙**: 이슈 close 시마다 위 표 상태를 갱신한다. `⏸ 대기 → 🔄 진행 중 → ✅ 완료` 순서로 전환.

### 제로 베이스 프로젝트 현황 (2026-06-16)

이 프로젝트의 목표는 대시보드 구축이 아니라 **H&ABYZ의 의료기기 인허가 업무를 보조하는 학습형 RA 전문가 조직**을 만드는 것이다. 에이전트는 사람 RA 전문가를 대체하지 않고, 지식베이스와 실제 업무 피드백을 통해 정확성·신뢰성 우선으로 성장한다.

| 축 | 현재 사실 | 판정 |
|---|---|---|
| 지식 토대 | `ra_knowledge` source curriculum seed와 Layer 4 API가 구축됨. `ra_us` 48, `ra_eu` 31, `ra_kr` 48 source seed 처리 완료 | ✅ foundation 존재 |
| 개별 성장 입력 | 메일 비의존 daily/weekly/monthly/quarterly growth loop 구현, timer는 승인 전 OFF | ✅ 구현 완료·운영 보류 |
| 성장 증명 데이터 | `growth-2026-06-19.json` 기준 27 sessions, 302 messages scanned. 행동/사람 피드백 metric은 N/A 또는 denominator 0. 2026-06-20 KB 평가 채점지 6회차/90건을 `docs/kb-eval-checksheets/`에 생성해 사람 체크 기반 denominator 확보를 시작 | ⚠️ 입력 수집됨·pilot evidence 확보 중 |
| 런타임 안전 게이트 | Yellow gate, WP 상태 검증, env/config 외부화 workflow를 RPi n8n에 import/activate. feedback + mail-triage Yellow smoke 완료 | ✅ 운영 반영 |
| 실시간 규제 활용 | `/v1/knowledge/fetch` 추가, T3610 runtime 배포/restart, RPi → Layer 4 smoke 200 OK | ✅ 운영 반영 |
| 인프라 의사결정 | `vote-rules.json` 초기값 + `infra-vote-broadcast` workflow 추가/import/activate, webhook smoke 완료 | ✅ skeleton 운영 반영 |
| 확장 | absence signal metric과 transition readiness report 추가. 현재 specialist/form 전환은 운영 데이터 부족으로 blocked | 🔄 데이터 대기 |
| 아키텍처 문서화 | 전체 시스템에 대한 codemaps (4개 파일)과 SPEC-ARCH-001 (3개 파일) 생성 완료 | ✅ 문서화 완료 |

### 남은 작업 우선순위

| 우선순위 | 작업 | 왜 필요한가 | 이슈 |
|---|---|---|---|
| P0 | 성장 metrics ingestion/data contract 보정 | 완료. 2026-06-19 daily report가 새 collector 계약으로 27 sessions / 302 messages를 스캔 | [#64](https://github.com/holee9/ra-hermes-multi-agent/issues/64) |
| P0 | #43~#45 RPi n8n import 및 smoke | 완료. 4개 workflow import/activate, env 반영, feedback webhook + mail-triage Yellow smoke 완료 | [#43](https://github.com/holee9/ra-hermes-multi-agent/issues/43), [#44](https://github.com/holee9/ra-hermes-multi-agent/issues/44), [#45](https://github.com/holee9/ra-hermes-multi-agent/issues/45) |
| P1 | Layer 4 API → mail-triage 실시간 연결 | 완료. n8n Layer 4 lookup node + prompt injection + runtime endpoint smoke 완료 | [#37](https://github.com/holee9/ra-hermes-multi-agent/issues/37) |
| P1 | 유효 metrics 기반 threshold/notification 정책 | policy/validator 구현. 임계값은 30일 valid metrics 전까지 null 유지 | [#65](https://github.com/holee9/ra-hermes-multi-agent/issues/65) |
| P1 | KB 기반 human-scored evidence 확보 | `ra_knowledge`에서 RA별 평가 채점지를 생성하고 체크 결과를 `score_given`으로 ingest하는 pilot evidence 루프 추가. 30일 production 기준은 유지 | 운영 |
| P2 | infra vote-rules와 n8n broadcast | 완료. 초기 2/3 quorum rule + broadcast workflow + webhook smoke | [#39](https://github.com/holee9/ra-hermes-multi-agent/issues/39) |
| P2 | 세부 전문가 확장 조건 데이터화 | 완료. `absence_pattern_signals` metric 추가. 현재 review signal 없음 | [#41](https://github.com/holee9/ra-hermes-multi-agent/issues/41) |
| P3 | form workflow 이관 | draft workflow/enable gate 구현. 현재 30일 valid metrics 미달로 `FORM_TRIAGE_ENABLED=false` 유지 | [#40](https://github.com/holee9/ra-hermes-multi-agent/issues/40) |

### 지속 성장 모니터링 현황 (2026-06-19)

| 구분 | 현재 상태 | 판정 |
|---|---|---|
| 자동성장 readiness | `scripts/auto-growth-readiness-report.py` 기준 4x4 matrix 16/16, `approval_review_required` | ✅ 승인 검토 가능 |
| 자동성장 timer | `hermes-auto-growth.timer` inactive/disabled, 명시 승인 전 자동 실행 없음 | ✅ 안전 |
| 일일 성장 지표 timer | `ra-growth-metrics.timer` active/enabled, 매일 02:00 KST 실행 | ✅ 스케줄러 존재 |
| 성장 지표 산출물 | `reports/growth-YYYY-MM-DD.json` 생성 (`correction_rate`, `first_pass_match_accuracy`, `confidence_calibration`, `warmstart_lift`, `escalation_precision`, `autonomous_study_sessions`, `study_insights_count`) | ⚠️ 파일 기반 |
| 최근 지표 유효성 | `growth-2026-06-19.json`: `sessions_scanned=27`, `messages_scanned=302`, 행동/사람 피드백 metric denominator 0 | ⚠️ 입력 수집됨·성장 판정 보류 |
| KB 평가 채점지 | `docs/kb-eval-checksheets/2026-06-20/`에 6 iterations / 90 cases 생성. 체크 후 `scripts/kb-eval-feedback-ingest.py`로 `score_given` 반영 가능 | 🔄 사람 채점 대기 |
| 웹 대시보드 | GitHub Pages `growth-dashboard.html` 바로보기 활성화. RA Growth Operations 요약, 담당자별 성장 카드, growth signal flow, 성장 측정 warning, 커버리지 근거 포함 | ✅ README 클릭 렌더링 |
| 트리거 알림 | `feedback/config/growth-trigger-config.json` 구조는 있으나 threshold/webhook은 null | ⚠️ 운영 기준 미정 |

현재 존재하는 것은 **자동 리포트와 정적 HTML snapshot 기반 모니터링**이다. [성장 대시보드 바로보기](https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html)는 README에서 클릭하면 렌더링된 HTML로 열린다. 2026-06-16 #64에서 Honcho v0.15.1 list API 계약을 `POST /sessions/list`, `POST /sessions/{id}/messages/list`로 보정했고, 2026-06-19 daily report는 27 sessions / 302 messages를 스캔한다. 다만 행동/사람 피드백 지표가 N/A 또는 denominator 0이므로 Growth Trend Verdict는 `측정 불충분` warning 상태가 맞다. 하단 readiness/coverage/raw metrics는 매일 볼 필수 현황이 아니라 기본 접힘 상태의 검증/감사 상세다. 열람·갱신·판정 기준은 [growth-dashboard.md](docs/growth-dashboard.md)에 정리했다. `virtual-office`는 Honcho 활동 이벤트를 시각화하는 읽기 전용 파일럿으로 분리한다. dashboard 표시 유지·보정은 [#62](https://github.com/holee9/ra-hermes-multi-agent/issues/62), metrics ingestion 보정 이력은 [#64](https://github.com/holee9/ra-hermes-multi-agent/issues/64), threshold/webhook 운영 기준은 [#65](https://github.com/holee9/ra-hermes-multi-agent/issues/65)에서 각각 추적한다.

### Hermes 프로파일 & Honcho 피어 현황 (2026-06-16 기준)

| 프로파일 | Honcho 피어 ID | Workspace | 인물 | 상태 |
|---------|--------------|-----------|-----|-----|
| ra-us | `ra_us` | work | Mike (FDA) | ✅ 등록·SOUL.md 이식 완료 |
| ra-eu | `ra_eu` | work | Theo (EU MDR) | ✅ 등록·SOUL.md 이식 완료 |
| ra-kr | `ra_kr` | work | Sam (MFDS) | ✅ 등록·SOUL.md 이식 완료 |
| op-manager | `op_manager` | work | Margot (WP) | ✅ 등록·SOUL.md 이식 완료 |
| n8n-manager | `n8n_manager` | work | Olly (n8n) | ✅ 등록·SOUL.md 이식 완료 |
| infra-t3610 | `infra_t3610` | infra | Finn (T3610) | ✅ 등록·SOUL.md 이식 완료 |
| infra-gx10 | `infra_gx10` | infra | Leo (GX10) | ✅ 등록·SOUL.md 이식 완료 |
| infra-rpi | `infra_rpi` | infra | Gus (RPi) | ✅ 등록·SOUL.md 이식 완료 |

> `honcho.json` `aiPeer` 값은 모두 언더스코어 형식(frozen 데이터 계약 준수). #49에서 `ra-us`/`ra-eu` wrong-peer bootstrap 오염을 복구했으며, 이후 자율 학습은 `scripts/verify-study-scheduler.py`와 dry-run을 통과한 뒤만 재시작한다. wrong-peer records는 직접 rename하지 않고 raw payload replay 방식만 허용한다.

### n8n 운영 위치 — RPi 단일 (2026-06-23 정정)

> **정정 (2026-06-23)**: 2026-06-19 "T3610 단일 n8n 운영" 선언은 **철회**. 조사 결과 (1) RPi 핵심 RA 워크플로우 32개(ra-reg-monitor·규제기관 스크래핑·Gitea 연동 등)가 이관 대상에서 누락, (2) 외부 도메인 `n8n.abyz-lab.work`가 RPi cloudflared에 묶인 채 T3610으로 전환 안 됨, (3) 4개만 부분 이전된 반쪽짜리 상태. **CLAUDE.md 원 설계(n8n=RPi 정위치)로 복귀**.

**현재 구성 (정정 후):**
- **RPi**: n8n + OpenProject (n8n 정위치, 36개 워크플로우 운영)
- **T3610**: Honcho server 전담 (n8n rollback/제거)

**이후 과제 — 이식성 개편 (별도 SPEC):**
- 현재 구조는 하드코딩 내부 IP(`172.18.0.1:*` 등)·도메인-인스턴스 결합으로 **머신 종속 → 이전 불가**
- 모든 서비스 주소를 env/논리 이름화, 도메인-인스턴스 분리, IaC화하여 **어느 머신에서든 운영 가능** 구조로 개편 선행 필요

**워크플로우 구현 현황:**
- `mail-triage`: Gmail 트리거 → 본문 파싱 → 규제권 라우팅 → Yellow 게이트 → RA 호출 → OpenProject 연동
- `infra-vote-broadcast`: Webhook 수신 → 투표 표준화 → 투표 집계 → 브릿지 전달
- `feedback-recorder`: 피드백 Webhook → 평가 검증 → Honcho 기록
- `infra-to-work-bridge`: 인프라 투표 결과 → 업무 workspace 전달

### 주요 구현 항목

| 컴포넌트 | 파일 | 상태 |
|---|---|---|
| Honcho 서버 설정 | `honcho/docker-compose.yml`, `init-vector-dim.sql`, `init-workspaces.sh` | 완료, T3610 배포 완료 |
| n8n 워크플로우 (T3610) | `n8n/workflows/mail-triage.json`, `infra-vote-broadcast.json`, `feedback-recorder.json`, `infra-to-work-bridge.json` | 완료, T3610 단일 운영 전환 |
| RA 프로파일 템플릿 | `profiles/honcho-config-templates/` 8종 | 완료 |
| SOUL.md 페르소나 | `profiles/souls/` 6종 (ra-us/eu/kr, op/n8n-manager, infra) | 완료 |
| mail-triage 워크플로우 | `n8n/workflows/mail-triage.json` | 완료, #43/#44/#45 안전 게이트 레포 반영 — RPi n8n 재import 필요 |
| 브릿지 워크플로우 | `n8n/workflows/infra-to-work-bridge.json` | 완료, relay 조건 env/config 외부화(#45) |
| 피드백 워크플로우 | `n8n/workflows/feedback-recorder.json` | 완료, 가중치 공식 env/config 외부화(#45) |
| 투표 집계 인터페이스 | `voting/vote-aggregator.js`, `voting/config/vote-rules.json`, `n8n/workflows/infra-vote-broadcast.json` | 완료 — 초기 2/3 quorum rule, RPi n8n import/activate, webhook smoke 완료 |
| 가상오피스 | `virtual-office/virtual-office.html` + 어댑터 + Dockerfile | 완료, Playwright 11건 `npm test` 통합(#46) |
| 자율 학습 scheduler guard | `scripts/verify-study-scheduler.py`, `scripts/replay-study-insights-issue49.py` | #49 peer_id 계약 검증·오염 payload clean replay 완료 |
| source curriculum seed | `scripts/curriculum-seed.py`, `scripts/verify-curriculum-seed.py` | #50/#60 기존 `ra_knowledge` source를 clean text curriculum seed로 빠르게 이식 (`ra_us` 48, `ra_eu` 31, `ra_kr` 48 processed) |
| non-email growth loop | `scripts/non-email-growth-loop.py`, `scripts/verify-non-email-growth-loop.py`, `scripts/pre-auto-growth-loop.py`, `scripts/auto-growth-readiness-report.py`, `scripts/auto-growth-runner.sh`, `scripts/systemd/hermes-auto-growth.{service,timer}`, `scripts/verify-auto-growth-activation-policy.py` | #51/#53/#54 메일 수신 없이 KB/source curriculum/autonomous study/coverage audit cadence 실행, #57 이후 timer 활성화는 명시 승인 게이트 필요, #58 pre-production readiness loop로 지속 개선 |
| KB eval checksheets | `scripts/kb-eval-checksheet.py`, `scripts/kb-eval-feedback-ingest.py`, `docs/kb-eval-checksheets/` | KB source를 평가 채점지로 변환해 git 이력으로 보관하고, 체크된 결과를 Honcho `score_given` feedback으로 ingest하는 controlled pilot evidence 루프 |
| static growth dashboard | `docs/growth-dashboard.html`, `docs/growth-dashboard.md`, `scripts/render-growth-dashboard.py`, `scripts/verify-growth-dashboard.py`, `scripts/coverage-guards.json` | #62 GitHub Pages에서 바로 보는 standalone HTML snapshot. RA Growth Operations 요약, 담당자별 성장 카드, growth signal flow, trend/evidence 시각화 |
| 아키텍처 Codemaps | `.moai/project/codemaps/` (overview.md, modules.md, dependencies.md, entry-points.md) | 전체 시스템 아키텍처 분석 완료. 30+ 모듈, 50+ 진입점, 내외부 의존성 그래프 문서화 |
| 아키텍처 개선 SPEC | `.moai/specs/SPEC-ARCH-001/` (spec.md, plan.md, acceptance.md) | SPEC-ARCH-001 생성 완료. EARS 형식 요구사항 15개, 5단계 구현 계획, Given-When-Then 수용 기준 |

> [IF] 표시 항목은 의도적 공백 — 운영·학습으로 채워지는 설계. 하드코딩 금지.

### n8n 운영 적용 체크리스트 (#43~#45)

RPi n8n에는 레포 변경을 import해야 실제 운영에 반영된다.

| 순서 | 확인 항목 |
|------|-----------|
| 1 | `n8n/.env.example` 기준으로 `OPENPROJECT_API_URL`, `HONCHO_WORK_WORKSPACE`, `YELLOW_CONFIDENCE_THRESHOLD` 확인 |
| 2 | 선택 알림 채널 `HUMAN_ALERT_WEBHOOK_URL` 설정 여부 결정 |
| 3 | `mail-triage.json`, `infra-to-work-bridge.json`, `feedback-recorder.json` import |
| 4 | 낮은 confidence, 완료 WP 매칭, OpenProject 조회 실패, bridge/feedback config parse 시나리오 E2E |
| 5 | 결과를 #43~#45 이슈에 코멘트 후 운영 기준값 변경 시 문서 동기화 |

레포 검증 명령:

```bash
npm run test:static
npm test
```

---

## 🖼️ 시스템 운영 및 E2E 검증

### 스크린샷 캡쳐 가이드

각 구성요소의 실제 운영 상태를 시각적으로 확인하고 E2E 검증을 수행하려면:

1. **캡쳐 가이드 참조**: `docs/screenshots/capture-guide.md` 
   - Honcho 대시보드, 가상 오피스, 성장 대시보드 등 6개 구성요소 캡쳐 방법
   - E2E 검증 체크리스트 포함

2. **주요 서비스 접속**:
   - Honcho API: `http://localhost:8000` 
   - n8n 워크플로우: `http://localhost:5678`
   - 가상 오피스: `virtual-office/virtual-office.html`
   - 성장 대시보드: [GitHub Pages](https://holee9.github.io/ra-hermes-multi-agent/growth-dashboard.html)

3. **인터랙티브 사용 매뉴얼**: 탭 기반 상세 가이드 제공
   - 시스템 개요, RA 에이전트, 가상 오피스, 성장 모니터링, n8n 워크플로우

### 시스템 상태 확인

```bash
# Honcho API 상태 확인
curl http://localhost:8000/health

# Docker 컨테이너 상태 확인  
docker ps | grep -E "honcho|postgres|redis"

# n8n 워크플로우 상태 확인
curl http://localhost:5678 | grep -o "<title>.*</title>"
```

---

## 장비별 역할

| 장비 | 역할 | 이 레포에서 할 일 |
|---|---|---|
| **T3610** | Honcho 서버 + Hermes 에이전트 | `git clone` 후 `honcho/` 기동, 프로파일 생성 |
| **GX10** | LLM 추론 엔진 (`gpt-oss:120b`, tool calling 확인) | 별도 작업 없음 (T3610이 API 호출) |
| **Raspberry Pi 5+** | n8n + OpenProject | `n8n/workflows/*.json` 3개 import만 |

---

## T3610 빠른 시작

```bash
git clone https://github.com/holee9/ra-hermes-multi-agent.git
cd ra-hermes-multi-agent

# 1. 환경변수 설정
cp honcho/.env.example honcho/.env
# .env 필수 편집 항목:
#   GX10_BASE_URL=http://GX10_실제IP:11434/v1
#   GX10_MODEL=gpt-oss:120b
#   EMBEDDING_MODEL_CONFIG__MODEL=qwen3-embedding:latest   ← __OVERRIDES__MODEL 아님
#   POSTGRES_PASSWORD=안전한_비밀번호
#   SECRET_KEY=안전한_시크릿

# 2. Honcho 서버 기동 (pgvector 4096차원 자동 초기화 포함)
docker-compose -f honcho/docker-compose.yml up -d

# 3. Workspace 초기화 (work + infra)
bash honcho/init-workspaces.sh
```

> **이후 작업은 [GitHub Issues](https://github.com/holee9/ra-hermes-multi-agent/issues) 순서대로 진행.**
> 이슈 #2 RULE을 먼저 읽고 시작할 것.

---

## 디렉터리 구조

```
ra-hermes-multi-agent/
│
├── .moai/                           # MoAI 프로젝트 관리
│   ├── project/                      # 프로젝트 산출물
│   │   └── codemaps/                # 아키텍처 Codemaps
│   │       ├── overview.md           # 시스템 개요
│   │       ├── modules.md            # 모듈 카탈로그 (30+ 모듈)
│   │       ├── dependencies.md       # 의존성 그래프
│   │       └── entry-points.md       # 진입점 매뉴얼 (50+ 진입점)
│   └── specs/                        # SPEC 문서
│       └── SPEC-ARCH-001/            # 전체 시스템 아키텍처 개선 SPEC
│           ├── spec.md               # EARS 형식 요구사항 (15개)
│           ├── plan.md               # 5단계 구현 계획
│           └── acceptance.md        # Given-When-Then 수용 기준
│
├── docs/                            # 설계·운영 문서
│   ├── RA-multi-agent-master-design.md  # 마스터 설계서 (전체 그림·철학)
│   ├── implementation-spec.md           # 구현 명세 ([구현]/[IF] 구분)
│   └── operations-guide.md              # 운영 전략 (프로파일·학습·게이트)
│
├── honcho/                          # T3610: Honcho 서버
│   ├── docker-compose.yml           # API + deriver + PostgreSQL(pgvector) + Redis
│   ├── .env.example                 # 환경변수 템플릿 → .env로 복사 후 편집
│   ├── init-workspaces.sh           # work/infra workspace 초기화 스크립트
│   └── init-vector-dim.sql          # pgvector 4096차원 초기화 (첫 기동 시 자동 실행)
│
├── profiles/                        # Hermes 프로파일 템플릿
│   ├── honcho-config-templates/     # ra-us, ra-eu, ra-kr, op-manager, n8n-manager, infra-* 8종
│   └── souls/                       # SOUL.md 페르소나 (ra-us/eu/kr, op-manager, n8n-manager, infra)
│
├── n8n/                             # Raspberry Pi: n8n에 import
│   ├── .env.example                 # n8n 환경변수 템플릿
│   └── workflows/
│       ├── mail-triage.json         # 핵심: 재전송 메일 → RA 분석 → WP 처리
│       ├── infra-to-work-bridge.json # 인프라→업무 단방향 브릿지
│       ├── infra-vote-broadcast.json # 인프라 투표 브로드캐스트 skeleton
│       ├── feedback-recorder.json   # 3점 평가 → Honcho 기록
│       └── form-triage-draft.json   # #40 form 이관 draft (FORM_TRIAGE_ENABLED=false)
│
├── voting/                          # 인프라 투표 자리 [IF]
│   ├── vote-aggregator.js           # 집계 인터페이스 (규칙은 외부 설정)
│   └── config/vote-rules.json       # 집계 규칙 (초기 운영값: quorum 2, threshold 0.66)
│
├── bridge/
│   └── config/bridge-config.json   # 브릿지 전달 임계 조건 [IF]
│
├── feedback/
│   └── config/weight-adjustment-config.json  # 가중치 설정 [IF]
│
├── scripts/                         # T3610 운영 스크립트
│   ├── hermes-api-server.py         # Layer 4 규제 API 서버 (openFDA/law.go.kr/data.go.kr) — 버전 관리 편입
│   ├── deploy-local.sh              # git scripts/ → /opt/hermes-ra/ 동기화 (--dry-run 지원)
│   ├── index_github_repos.py        # GitHub + Gitea 레포 → pgvector 인덱싱 (DR_RnD/ra-llm-wiki 포함)
│   ├── curriculum-seed.py           # ra_knowledge source-level curriculum seed → Honcho peer
│   ├── daily-growth-runner.py       # 메일 비의존 KB 기반 daily growth case planner/runner
│   ├── kb-eval-checksheet.py        # KB 기반 human review 채점지 생성
│   ├── kb-eval-feedback-ingest.py   # 체크된 채점지를 score_given feedback으로 반영
│   ├── verify-workflows.js          # n8n JSON/Code node 정적 검증
│   └── ...                          # 기타 자동화 17종
│
├── e2e/                             # Playwright E2E 테스트 (virtual-office)
│   └── virtual-office.spec.js       # 4 Suite 11 테스트 케이스
│
├── virtual-office/                  # 가상오피스 (자기완결)
│   ├── Dockerfile                   # Docker 단일 컨테이너 빌드
│   ├── virtual-office-honcho-adapter.js  # Honcho 실데이터 연결 어댑터
│   ├── virtual-office.html          # 픽셀아트 프로토타입 (브라우저 직접 열기)
│   ├── virtual-office-mvp.md        # 가상오피스 MVP 설계
│   ├── virtual-office-org-chart.md  # actor ID ↔ 캐릭터 매핑
│   └── pixel-character-guide.md     # 스프라이트 교체 가이드 (Kenney CC0)
│
├── README.md                        # 이 파일
├── CLAUDE.md                        # Claude Code 프로젝트 지시
└── ECOSYSTEM.md                     # RA 생태계 지도 (전 레포 공유)
```

---

## 실행 순서 (이슈 번호 아님 — 의존관계 기준)

> GitHub 이슈 번호는 등록 순서일 뿐이다. **실제 작업 순서는 아래 표를 따른다.**
> 이슈 목록: https://github.com/holee9/ra-hermes-multi-agent/issues

### 상시 참조 (닫지 않음)

| 이슈 | 내용 |
|---|---|
| [#2 RULE](https://github.com/holee9/ra-hermes-multi-agent/issues/2) | 절대 위반 금지 규칙 — 모든 작업 전 필독 |
| [#12 ADR-001](https://github.com/holee9/ra-hermes-multi-agent/issues/12) | 생태계 운영 결정 기록 — 레이어 모델, 개발 주력 확정 |

### Phase 1 — Foundation (T3610)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 1 | [#3 SETUP-1](https://github.com/holee9/ra-hermes-multi-agent/issues/3) | Honcho 서버 배포 · GX10 Qwen3 연결 검증 | T3610 | ✅ |

### Phase 2 — Profiles + Knowledge (T3610, #3 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 2a | [#4 PROFILE-1](https://github.com/holee9/ra-hermes-multi-agent/issues/4) | RA 프로파일 생성 (ra-kr/ra-us/ra-eu/op-manager) | T3610 | ✅ |
| 2b | [#13 ABSORB-1](https://github.com/holee9/ra-hermes-multi-agent/issues/13) | hermes-ra SKILL.md → SOUL.md 3종 심화 이식 | T3610 | ✅ |
| 2c | [#6 PROFILE-2](https://github.com/holee9/ra-hermes-multi-agent/issues/6) | 인프라 프로파일 생성 (infra-t3610/gx10/rpi) | T3610 | ✅ |
| 2d | [#15 CONNECT-1](https://github.com/holee9/ra-hermes-multi-agent/issues/15) | ra-project + MD-process → Honcho 지식 연결 | T3610 | ✅ |

> 2a·2b는 병행 가능. 2a 완료 후 2b 시작 권장 (프로파일 디렉토리 확정 후 이식).

### Phase 3 — Workflows (RPi, #4 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 3a | [#5 WORKFLOW-1](https://github.com/holee9/ra-hermes-multi-agent/issues/5) | mail-triage n8n 배포 · E2E 검증 | RPi | ✅ |
| 3b | [#10 SETUP-2](https://github.com/holee9/ra-hermes-multi-agent/issues/10) | 가상오피스 Docker 빌드 · Honcho 실데이터 연결 | T3610 | ✅ |

### Phase 4 — IF 구현 (선택적, #5 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 4a | [#7 WORKFLOW-2](https://github.com/holee9/ra-hermes-multi-agent/issues/7) | 투표 집계 자리 동작 확인 [IF] | T3610 | ✅ |
| 4b | [#8 WORKFLOW-3](https://github.com/holee9/ra-hermes-multi-agent/issues/8) | 브릿지 n8n 배포 · 단방향 검증 [IF] | RPi | ✅ |
| 4c | [#9 WORKFLOW-4](https://github.com/holee9/ra-hermes-multi-agent/issues/9) | 3점 평가 루프 n8n 배포 [IF] | RPi | ✅ |

### Phase 5 — Validate + Archive (전체 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 5a | [#11 MVP-VALIDATE](https://github.com/holee9/ra-hermes-multi-agent/issues/11) | Cold Start E2E 검증 — **hermes-ra 종료 게이트** | 전체 | ✅ |
| 5b | [#14 ABSORB-2](https://github.com/holee9/ra-hermes-multi-agent/issues/14) | hermes-ra 스크립트 이전 + 아카이브 (#11 PASS 후) | T3610 | ✅ |

```
#3 → #4 + #13(병행) + #6 + #15 → #5 + #10 → #7 + #8 + #9 → #11 → #14
```

---

## 핵심 원칙

- **정확성·신뢰성 우선** (최우선): 의료기기 인허가에서 오류는 환자 안전 문제다. 속도는 정확성이 확보된 뒤의 부산물. 불확실하면 반드시 사람에게 올린다. Cold start 상태에서 기본값은 Yellow 게이트(사람 확인).
- **학습하며 성장**: 골격 고정, 내용물(판단·기억·평가)이 성숙해지는 구조. 자동화 비중은 학습·성숙도 누적 후 점진적으로 확대.
- **T자형**: 공통 지식(llm-wiki·ra-project·MD-process 단방향 참조) + 개별 전문성(Honcho 누적)
- **사람 = 최종 결정자**: WP 완료·재오픈은 사람 전용(불변). 에이전트는 보조하고 제안만. 사람이 검토 루프에 있는 것은 약점이 아니라 설계.
- **[IF] = 의도적 공백**: 투표 규칙·가중치·임계값은 운영하며 채움. 코드 하드코딩 금지.

---

## 문서 읽는 순서

1. `docs/RA-multi-agent-master-design.md` — 전체 그림, 설계 철학
2. `docs/implementation-spec.md` — 구현 경계 (`[구현]` vs `[IF]`)
3. `docs/operations-guide.md` — 프로파일·학습 루프·게이트·성장 기준
4. `virtual-office/virtual-office-mvp.md` — 가상오피스 설계
