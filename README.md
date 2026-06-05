# RA Hermes 멀티 에이전트 시스템

> 의료기기 인허가(RA) 도메인의 학습하는 멀티 에이전트 시스템.
> Hermes Agent v0.14.0 / Honcho 기반. 사실 기준일: 2026-06-05.

---

## 현재 상태

**MVP 골격 구현 완료 — T3610 배포 진행 중 / SPEC-RA-TOOL-001 완료** | 최종 갱신: 2026-06-05

| 단계 | 상태 | 이슈 |
|---|---|---|
| 설계 | ✅ 완료 | [#12 ADR-001](https://github.com/holee9/ra-hermes-multi-agent/issues/12) |
| 골격 코드 구현 | ✅ 완료 | — |
| Honcho T3610 배포 | 🔄 진행 중 | [#3](https://github.com/holee9/ra-hermes-multi-agent/issues/3) |
| MVP 자동화 스크립트 (SPEC-RA-TOOL-001) | ✅ 완료 | [#16](https://github.com/holee9/ra-hermes-multi-agent/issues/16) |
| RA 프로파일 생성 (PROFILE-1, PROFILE-2) | ✅ 완료 | [#4](https://github.com/holee9/ra-hermes-multi-agent/issues/4), [#6](https://github.com/holee9/ra-hermes-multi-agent/issues/6) |
| SKILL.md 심화 이식 | ✅ 완료 | [#13](https://github.com/holee9/ra-hermes-multi-agent/issues/13) |
| 지식베이스 연결 | ⏸ 대기 | [#15](https://github.com/holee9/ra-hermes-multi-agent/issues/15) |
| MVP Cold Start 검증 | ⏸ 대기 | [#11](https://github.com/holee9/ra-hermes-multi-agent/issues/11) |
| hermes-ra 흡수·아카이브 | ⏸ 대기 (#11 게이트) | [#14](https://github.com/holee9/ra-hermes-multi-agent/issues/14) |

> **README 갱신 규칙**: 이슈 close 시마다 위 표 상태를 갱신한다. `⏸ 대기 → 🔄 진행 중 → ✅ 완료` 순서로 전환.

### 골격 구현 포함 항목 (배포·연결 대기 중)

| 컴포넌트 | 파일 | 상태 |
|---|---|---|
| Honcho 서버 설정 | `honcho/docker-compose.yml`, `init-vector-dim.sql`, `init-workspaces.sh` | 설정 완료, T3610 배포 진행 중 |
| RA 프로파일 템플릿 | `profiles/honcho-config-templates/` 8종 | 완료 — #3 완료 후 Honcho API에 생성 |
| SOUL.md 페르소나 | `profiles/souls/` 6종 (ra-us/eu/kr, op/n8n-manager, infra) | 완료 — #4 완료 후 세션 이식 |
| mail-triage 워크플로우 | `n8n/workflows/mail-triage.json` (17K) | 완료 — #4 완료 후 RPi n8n import |
| 브릿지 워크플로우 | `n8n/workflows/infra-to-work-bridge.json` (7.6K) | 완료, relay_conditions는 [IF] |
| 피드백 워크플로우 | `n8n/workflows/feedback-recorder.json` (5.1K) | 완료, 가중치 공식은 [IF] |
| 투표 집계 인터페이스 | `voting/vote-aggregator.js` (96줄), `vote-rules.json` [IF] | 완료 — 규칙은 운영이 채움 |
| 가상오피스 | `virtual-office/virtual-office.html` + 어댑터 + Dockerfile | 완료 — Honcho 실데이터 연결 대기 |

> [IF] 표시 항목은 의도적 공백 — 운영·학습으로 채워지는 설계. 하드코딩 금지.

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
#   EMBEDDING_MODEL_CONFIG__OVERRIDES__MODEL=qwen3-embedding:latest
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
| 1 | [#3 SETUP-1](https://github.com/holee9/ra-hermes-multi-agent/issues/3) | Honcho 서버 배포 · GX10 Qwen3 연결 검증 | T3610 | 🔄 |

### Phase 2 — Profiles + Knowledge (T3610, #3 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 2a | [#4 PROFILE-1](https://github.com/holee9/ra-hermes-multi-agent/issues/4) | RA 프로파일 생성 (ra-kr/ra-us/ra-eu/op-manager) | T3610 | ✅ |
| 2b | [#13 ABSORB-1](https://github.com/holee9/ra-hermes-multi-agent/issues/13) | hermes-ra SKILL.md → SOUL.md 3종 심화 이식 | T3610 | ⏸ |
| 2c | [#6 PROFILE-2](https://github.com/holee9/ra-hermes-multi-agent/issues/6) | 인프라 프로파일 생성 (infra-t3610/gx10/rpi) | T3610 | ✅ |
| 2d | [#15 CONNECT-1](https://github.com/holee9/ra-hermes-multi-agent/issues/15) | ra-project + MD-process → Honcho 지식 연결 | T3610 | ⏸ |

> 2a·2b는 병행 가능. 2a 완료 후 2b 시작 권장 (프로파일 디렉토리 확정 후 이식).

### Phase 3 — Workflows (RPi, #4 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 3a | [#5 WORKFLOW-1](https://github.com/holee9/ra-hermes-multi-agent/issues/5) | mail-triage n8n 배포 · E2E 검증 | RPi | ⏸ |
| 3b | [#10 SETUP-2](https://github.com/holee9/ra-hermes-multi-agent/issues/10) | 가상오피스 Docker 빌드 · Honcho 실데이터 연결 | T3610 | ⏸ |

### Phase 4 — IF 구현 (선택적, #5 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 4a | [#7 WORKFLOW-2](https://github.com/holee9/ra-hermes-multi-agent/issues/7) | 투표 집계 자리 동작 확인 [IF] | T3610 | ⏸ |
| 4b | [#8 WORKFLOW-3](https://github.com/holee9/ra-hermes-multi-agent/issues/8) | 브릿지 n8n 배포 · 단방향 검증 [IF] | RPi | ⏸ |
| 4c | [#9 WORKFLOW-4](https://github.com/holee9/ra-hermes-multi-agent/issues/9) | 3점 평가 루프 n8n 배포 [IF] | RPi | ⏸ |

### Phase 5 — Validate + Archive (전체 완료 후)

| 순서 | 이슈 | 내용 | 장비 | 상태 |
|---|---|---|---|---|
| 5a | [#11 MVP-VALIDATE](https://github.com/holee9/ra-hermes-multi-agent/issues/11) | Cold Start E2E 검증 — **hermes-ra 종료 게이트** | 전체 | ⏸ |
| 5b | [#14 ABSORB-2](https://github.com/holee9/ra-hermes-multi-agent/issues/14) | hermes-ra 스크립트 이전 + 아카이브 (#11 PASS 후) | T3610 | ⏸ |

```
#3 → #4 + #13(병행) + #6 + #15 → #5 + #10 → #7 + #8 + #9 → #11 → #14
```

---

## 핵심 원칙

- **학습하며 성장**: 골격 고정, 내용물(판단·기억·평가)이 성숙해지는 구조
- **T자형**: 공통 지식(llm-wiki·ra-project·MD-process 단방향 참조) + 개별 전문성(Honcho 누적)
- **사람 = 최종 결정자**: WP 완료·재오픈은 사람 전용. 에이전트는 제안만.
- **[IF] = 의도적 공백**: 투표 규칙·가중치·임계값은 운영하며 채움. 코드 하드코딩 금지.

---

## 문서 읽는 순서

1. `docs/RA-multi-agent-master-design.md` — 전체 그림, 설계 철학
2. `docs/implementation-spec.md` — 구현 경계 (`[구현]` vs `[IF]`)
3. `docs/operations-guide.md` — 프로파일·학습 루프·게이트·성장 기준
4. `virtual-office/virtual-office-mvp.md` — 가상오피스 설계
