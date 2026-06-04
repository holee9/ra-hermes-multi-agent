# RA Hermes 멀티 에이전트 시스템

> 의료기기 인허가(RA) 도메인의 학습하는 멀티 에이전트 시스템.
> Hermes Agent v0.14.0 / Honcho 기반. 사실 기준일: 2026-05-28.

---

## 현재 상태

**MVP 골격 구현 완료 — T3610 배포 진행 중**

| 단계 | 상태 |
|---|---|
| 설계 | 완료 |
| 골격 코드 구현 | 완료 (35개 파일 커밋) |
| T3610 배포 | 진행 중 ([이슈 트래커](https://github.com/holee9/ra-hermes-multi-agent/issues)) |
| MVP Cold Start 검증 | 대기 |

---

## 장비별 역할

| 장비 | 역할 | 이 레포에서 할 일 |
|---|---|---|
| **T3610** | Honcho 서버 + Hermes 에이전트 | `git clone` 후 `honcho/` 기동, 프로파일 생성 |
| **GX10** | Qwen3 LLM 추론 엔진 | 별도 작업 없음 (T3610이 API 호출) |
| **Raspberry Pi 5+** | n8n + OpenProject | `n8n/workflows/*.json` 3개 import만 |

---

## T3610 빠른 시작

```bash
git clone https://github.com/holee9/ra-hermes-multi-agent.git
cd ra-hermes-multi-agent

# 1. 환경변수 설정
cp honcho/.env.example honcho/.env
# .env 편집 — 필수 항목:
#   GX10_BASE_URL=http://GX10_실제IP:11434/v1
#   GX10_MODEL=qwen3:30b
#   EMBEDDING_MODEL_CONFIG__OVERRIDES__MODEL=GX10에서_확인한_임베딩_모델명
#   POSTGRES_PASSWORD=안전한_비밀번호
#   SECRET_KEY=안전한_시크릿

# 2. Honcho 서버 기동 (pgvector 4096차원 자동 초기화 포함)
docker-compose -f honcho/docker-compose.yml up -d

# 3. Workspace 초기화 (work + infra)
bash honcho/init-workspaces.sh
```

**이후 작업은 [GitHub Issues](https://github.com/holee9/ra-hermes-multi-agent/issues)를 순서대로 따라가세요.**

---

## 구현 파일 구조

```
ra-hermes-multi-agent/
│
├── honcho/                          # T3610: Honcho 서버
│   ├── docker-compose.yml           # API + deriver + PostgreSQL + Redis
│   ├── .env.example                 # 환경변수 템플릿
│   ├── init-workspaces.sh           # work/infra workspace 초기화
│   └── init-vector-dim.sql          # pgvector 4096차원 초기화
│
├── profiles/                        # Hermes 프로파일 템플릿
│   ├── honcho-config-templates/     # ra-us, ra-eu, ra-kr, op-manager, n8n-manager, infra-* 8종
│   └── souls/                       # SOUL.md 페르소나 파일
│
├── n8n/workflows/                   # Raspberry Pi: n8n에 import
│   ├── mail-triage.json             # 핵심: 재전송 메일 → RA 분석 → WP 처리
│   ├── infra-to-work-bridge.json    # 인프라→업무 단방향 브릿지
│   └── feedback-recorder.json       # 3점 평가 → Honcho 기록
│
├── voting/                          # 인프라 투표 자리 [IF]
│   ├── vote-aggregator.js
│   └── config/vote-rules.json       # 집계 규칙 (의도적 공백 — 운영이 채움)
│
├── bridge/config/bridge-config.json # 브릿지 임계 조건 [IF]
├── feedback/config/weight-adjustment-config.json  # 가중치 설정 [IF]
│
├── virtual-office/                  # T3610: Docker 컨테이너 + 가상오피스 전체
│   ├── Dockerfile
│   ├── virtual-office-honcho-adapter.js
│   ├── virtual-office.html          # 픽셀아트 프로토타입 (브라우저 직접 열기)
│   ├── virtual-office-mvp.md        # 가상오피스 MVP 설계
│   ├── virtual-office-org-chart.md  # actor ID ↔ 캐릭터 매핑
│   └── pixel-character-guide.md     # 스프라이트 교체 가이드
│
├── implementation-spec.md           # AI 코딩 툴용 구현 명세 ([구현]/[IF] 구분)
├── operations-guide.md              # 사람+Hermes 운영 전략
├── RA-multi-agent-master-design.md  # 마스터 설계서
└── ECOSYSTEM.md                     # 생태계 지도
```

---

## GitHub Issues — 작업 순서

https://github.com/holee9/ra-hermes-multi-agent/issues

| 이슈 | 내용 | 장비 |
|---|---|---|
| #2 RULE | 절대 위반 금지 규칙 (상시 참조) | — |
| #3 SETUP-1 | Honcho 서버 T3610 배포 · GX10 연결 | T3610 |
| #4 PROFILE-1 | RA 에이전트 프로파일 생성 | T3610 (Hermes) |
| #5 WORKFLOW-1 | mail-triage n8n 배포 · E2E 검증 | RPi n8n |
| #6 PROFILE-2 | 인프라 에이전트 프로파일 생성 | T3610 (Hermes) |
| #7 WORKFLOW-2 | 투표 자리 동작 확인 [IF] | T3610 |
| #8 WORKFLOW-3 | 브릿지 n8n 배포 | RPi n8n |
| #9 WORKFLOW-4 | 3점 평가 루프 n8n 배포 | RPi n8n |
| #10 SETUP-2 | 가상 오피스 Docker 빌드 | T3610 |
| #11 MVP-VALIDATE | Cold Start 한 바퀴 E2E 검증 | 전체 |

**의존 순서**: #3 → (#4, #6 병렬) → (#5, #7 병렬) → (#8, #9, #10 병렬) → #11

---

## 핵심 원칙

- **학습하며 성장**: 골격은 고정, 내용물(판단·기억·평가)이 성숙해지는 구조
- **T자형**: 공통 지식(llm-wiki·ra-project·MD-process) + 개별 전문성(Honcho 누적)
- **사람 = 최종 결정자**: WP 완료·재오픈은 사람 전용. 에이전트는 제안만.
- **[IF] = 의도적 공백**: 투표 규칙·가중치·임계값은 운영하며 채움. 코드에 하드코딩 금지.
- **부재 기반 성장**: 필요가 확인될 때만 자리를 추가. 선제적 구현 금지.

---

## 문서 읽는 순서

1. **RA-multi-agent-master-design.md** — 전체 그림, 설계 철학
2. **implementation-spec.md** — 구현 경계 (`[구현]` vs `[IF]`)
3. **operations-guide.md** — 프로파일·학습 루프·게이트·성장 기준
4. **virtual-office-mvp.md** — 가상 오피스 설계
