# RA Hermes 멀티 에이전트 시스템

> 의료기기 인허가(RA) 도메인의 **정확성·신뢰성 우선** 학습 멀티 에이전트 시스템. 에이전트는 사람 RA 전문가를 *보조*한다.
> Hermes Agent v0.15.1 / Honcho v0.15.1 기반. 사실 기준일: 2026-06-15.

**[사용 가이드 →](docs/usage-guide.md)** | [마스터 설계서](docs/RA-multi-agent-master-design.md) | [구현 명세](docs/implementation-spec.md) | [운영 전략](docs/operations-guide.md)

---

## 현재 상태

**Phase 1~2 완료 · 성장 루프/자율 학습 구현 · #48,#49 peer_id 복구 완료 · #50 source curriculum seed 완료 · #57 자동성장 timer off·승인 게이트 보완 중** | 최종 갱신: 2026-06-16

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
| source-level curriculum seed fast-track | ✅ 완료 (`ra_us` 48개, `ra_eu` 31개, `ra_kr` 29개 explicit source seed processed, `curriculum_seed` JSON envelope 0, idempotence `to_seed=0`) | [#50](https://github.com/holee9/ra-hermes-multi-agent/issues/50) (closed) |
| 비메일 성장 cadence loop | 🔄 구현 완료·운영 timer off (승인 없이 활성화된 #57 오판 보정 중, `hermes-auto-growth.timer` inactive/disabled, RA pending 0, 수동 readiness 점검 가능) | [#50](https://github.com/holee9/ra-hermes-multi-agent/issues/50) (closed), [#51](https://github.com/holee9/ra-hermes-multi-agent/issues/51) (closed), [#52](https://github.com/holee9/ra-hermes-multi-agent/issues/52) (closed), [#53](https://github.com/holee9/ra-hermes-multi-agent/issues/53) (closed), [#54](https://github.com/holee9/ra-hermes-multi-agent/issues/54) (closed), [#55](https://github.com/holee9/ra-hermes-multi-agent/issues/55) (closed), [#57](https://github.com/holee9/ra-hermes-multi-agent/issues/57) |
| mail-triage Yellow 게이트·사람 알림 강화 | 🔄 레포 반영, RPi n8n import/E2E 대기 | [#43](https://github.com/holee9/ra-hermes-multi-agent/issues/43) |
| 기존 WP 매칭 시 OpenProject 상태 검증 | 🔄 레포 반영, RPi n8n import/E2E 대기 | [#44](https://github.com/holee9/ra-hermes-multi-agent/issues/44) |
| n8n 워크플로우 env/config 외부화 | 🔄 레포 반영, RPi n8n import/E2E 대기 | [#45](https://github.com/holee9/ra-hermes-multi-agent/issues/45) |
| npm test 품질 게이트 복구 | ✅ 완료 (`test:static` + Playwright E2E 11건) | [#46](https://github.com/holee9/ra-hermes-multi-agent/issues/46) |
| 문서 상태 불일치 정리 | ✅ 완료 (README·설계·운영·생태계·상태 문서 동기화) | [#47](https://github.com/holee9/ra-hermes-multi-agent/issues/47) |

> **README 갱신 규칙**: 이슈 close 시마다 위 표 상태를 갱신한다. `⏸ 대기 → 🔄 진행 중 → ✅ 완료` 순서로 전환.

### Hermes 프로파일 & Honcho 피어 현황 (2026-06-13 기준)

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

### 주요 구현 항목

| 컴포넌트 | 파일 | 상태 |
|---|---|---|
| Honcho 서버 설정 | `honcho/docker-compose.yml`, `init-vector-dim.sql`, `init-workspaces.sh` | 완료, T3610 배포 완료 |
| RA 프로파일 템플릿 | `profiles/honcho-config-templates/` 8종 | 완료 |
| SOUL.md 페르소나 | `profiles/souls/` 6종 (ra-us/eu/kr, op/n8n-manager, infra) | 완료 |
| mail-triage 워크플로우 | `n8n/workflows/mail-triage.json` | 완료, #43/#44/#45 안전 게이트 레포 반영 — RPi n8n 재import 필요 |
| 브릿지 워크플로우 | `n8n/workflows/infra-to-work-bridge.json` | 완료, relay 조건 env/config 외부화(#45) |
| 피드백 워크플로우 | `n8n/workflows/feedback-recorder.json` | 완료, 가중치 공식 env/config 외부화(#45) |
| 투표 집계 인터페이스 | `voting/vote-aggregator.js` (96줄), `voting/config/vote-rules.json` [IF] | 완료 — 규칙은 운영이 채움 |
| 가상오피스 | `virtual-office/virtual-office.html` + 어댑터 + Dockerfile | 완료, Playwright 11건 `npm test` 통합(#46) |
| 자율 학습 scheduler guard | `scripts/verify-study-scheduler.py`, `scripts/replay-study-insights-issue49.py` | #49 peer_id 계약 검증·오염 payload clean replay 완료 |
| source curriculum seed | `scripts/curriculum-seed.py`, `scripts/verify-curriculum-seed.py` | #50 기존 `ra_knowledge` source를 clean text curriculum seed로 빠르게 이식 (`ra_us` 48, `ra_eu` 31, `ra_kr` 29 processed) |
| non-email growth loop | `scripts/non-email-growth-loop.py`, `scripts/verify-non-email-growth-loop.py`, `scripts/pre-auto-growth-loop.py`, `scripts/auto-growth-runner.sh`, `scripts/systemd/hermes-auto-growth.{service,timer}`, `scripts/verify-auto-growth-activation-policy.py` | #51/#53/#54 메일 수신 없이 KB/source curriculum/autonomous study/coverage audit cadence 실행, #57 이후 timer 활성화는 명시 승인 게이트 필요 |

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
│       └── feedback-recorder.json   # 3점 평가 → Honcho 기록
│
├── voting/                          # 인프라 투표 자리 [IF]
│   ├── vote-aggregator.js           # 집계 인터페이스 (규칙은 외부 설정)
│   └── config/vote-rules.json       # 집계 규칙 (의도적 공백 — 운영이 채움)
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
