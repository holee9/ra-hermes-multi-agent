# RA Hermes 프로젝트 — 운영 상태 & 완성도 점검

> 이 파일은 주기적 전수 조사 결과를 누적 기록한다.
> 이후 작업 착수 전 "현재 어디까지 됐나" 확인 기준점으로 사용한다.

---

## 점검 기록 #5 — 2026-06-13

### 관련 문서 상세화 및 push 준비

#### 문서 보강 범위

| 문서 | 보강 내용 |
|------|-----------|
| `docs/implementation-spec.md` | Yellow 게이트 조건, OpenProject 상태 허용/차단 계약, n8n env/config 계약, 운영 검증 시나리오 |
| `docs/usage-guide.md` | RPi n8n 환경변수, Yellow 운영 기준, 기존 WP 상태 검증, import 후 E2E 절차 |
| `docs/operations-guide.md` | #43~#45 운영 import 순서, env 적용, 이슈 이력 기록 기준 |
| `docs/RA-multi-agent-master-design.md` | mail-triage 최신 흐름, 사람 알림, 외부 설정 원칙 |
| `README.md` | n8n 운영 적용 체크리스트와 검증 명령 |
| `.moai/project/*` | 구조/기술/codemap 설명을 최신 파일·게이트 기준으로 동기화 |
| `docs/ecosystem.md` | 2026-06-13 기준 우선순위와 ra-hermes 상태 갱신 |

#### 운영상 남은 항목

- #43~#45: RPi n8n import와 실제 Webhook/OpenProject 상태 조회 E2E.
- #37: Layer 4 API → mail-triage 실시간 연결.
- #39: vote-rules 운영 초기값과 브로드캐스트 결정.
- #49: autonomous study peer_id 오염 데이터 cleanup/migration 방침 사람 승인.

## 점검 기록 #4 — 2026-06-13

### 전수 리뷰 후 하드닝 구현

#### 기준선

- 신규 품질 이슈: #43~#47 등록.
- 운영 후속 오픈: #2(RULE), #37(Layer 4 mail-triage 연결), #39(인프라 투표 활성화), #40~#41(확장), #43~#45(n8n 운영 import/E2E).
- 완료 처리 대상: #46(`npm test` 품질 게이트), #47(문서 동기화).

#### 변경된 구현

| 이슈 | 변경 |
|------|------|
| #43 | `mail-triage.json`에 Yellow confidence 게이트, 파싱 실패/저신뢰 사람 알림 payload, 선택 Webhook 전송 경로 추가 |
| #44 | 기존 WP 매칭 시 OpenProject 상태 조회·검증을 추가하고, 종료/조회 실패/불명 상태는 Yellow 사람 검토로 전환 |
| #45 | n8n workflow의 OpenProject/Honcho URL, 브릿지 relay 조건, feedback 가중치 설정을 env/config 입력으로 외부화 |
| #46 | `npm test`를 정적 검증 + Playwright E2E로 복구하고 n8n Code node 컴파일 검증 스크립트 추가 |
| #47 | README, CLAUDE, 설계서, 운영 가이드, 생태계 지도, 상태 기록의 완료/대기 표현 동기화 |

#### 검증

- `npm run test:static`: 통과.
- `npm test`: 통과. Playwright 11/11 테스트 통과.
- Playwright 브라우저 설치는 Ubuntu 26.04 환경에서 공식 chromium 패키지 미지원으로 실패했으며, 로컬 `/usr/bin/chromium-browser` 실행 경로로 검증했다.

#### 남은 운영 작업

- #43~#45 변경 workflow를 RPi n8n에 import하고 실제 알림/Webhook/OP 상태 조회 경로를 E2E 검증.
- #37 Layer 4 API를 mail-triage 실시간 질의 경로에 연결.
- #39 인프라 투표 브로드캐스트와 vote-rules 운영 초기값 확정.
- #40~#41 확장 트리거는 성장 지표 운영 데이터 누적 후 사람 판단으로 진행.

## 점검 기록 #3 — 2026-06-11

### .env 점검 및 인프라 정보 반영

#### 발견 및 변경 사항

| 항목 | 이전 기록 | 확인된 실제 값 | 조치 |
|------|----------|--------------|------|
| NAS 연결 방식 | Tailscale HTTP (`diskstation:7001`) | NFS 로컬 마운트 (`/mnt/nas-ra/공통자료/RA`) | 이슈 #35 DoD 재정의, 코멘트 추가 |
| hermes-api-server.py 포트 | 미기록 | `8643` (`API_SERVER_PORT`) | master-design.md §14.1 업데이트 |
| Layer 4 API 키 변수명 | 미기록 | `OPENFDA_API_KEY`, `LAW_GO_KR_OC`, `DATA_GO_KR_API_KEY` | 이슈 #37 코멘트 추가 |
| GX10 Ollama URL | 192.168.100.1 (추정) | `http://192.168.100.1:11434` (확인) | master-design.md §14.1 추가 |
| Qdrant URL | pgvector 이전 완료 | 여전히 .env에 잔존 (미사용) | .env.example에 주석 처리 |

#### 변경된 파일

- `scripts/index_ra_knowledge.py`: `NAS_BASE` 하드코딩 → `NAS_RA_PATH` 환경변수 읽기
- `.env.example` 신규 생성: 모든 환경변수 이름 문서화 (값 없음)
- `docs/RA-multi-agent-master-design.md` §14.1: 운영 서비스 URL 맵 추가
- 이슈 #35 보정 코멘트: NAS 로컬 마운트 확인됨
- 이슈 #37 보정 코멘트: env var 이름 및 API 서버 포트 명시

---

## 점검 기록 #2 — 2026-06-11

### 전체 그림 재정립 (이 세션의 핵심 발견)

**핵심 재정립**: 이 시스템은 이메일 처리기가 아니다.  
**H&ABYZ의 AI 기반 의료기기 인허가 운영 부서**다.

H&ABYZ는 실제 X-ray 영상 진단 의료기기 제조사이며, 실제 제품들이 실제 허가를 받아야 한다.  
이메일 트리아지는 RA 업무 유입 채널(첫 번째 구현)이며, 시스템의 목적이 아니다.

### 생태계 구조 확인

```
지식 토대 (T자형 가로획 — 에이전트에게 단방향 주입)
  ra-project: 규제 지식 베이스
  MD-process: 사내 SOP·정책
  llm-wiki:   NAS 실무자료 RAG (인덱싱 진행중)
  → 모두 RA 에이전트에게 단방향 참조

RA 전문가 에이전트 (T자형 세로획 — H&ABYZ 특화 경험 누적)
  Mike(ra_us): FDA 510(k)/QMSR/Part 1020
  Theo(ra_eu): CE MDR/Notified Body
  Sam(ra_kr):  MFDS/KGMP/국제정합

관련 레포
  ra-med-bot(Regula): 내부 직원용 규제 Q&A (별도 레포)
  regula-eval-suite:  Regula 평가 스위트 (별도 레포)
```

### 식별된 구조적 갭 (현재 미완성)

| 갭 | 영향 | 비고 |
|----|------|------|
| ra-project/MD-process → pgvector 자동 인덱싱 없음 | T자형 가로획 미구축 | 수동 NAS 인덱싱만 |
| 성장 트리거 임계값 미정의 | 다음 단계 자동 진입 불가 | ops-guide §5.2 |
| infra 투표 브로드캐스트 없음 | 프랙탈 패턴 복제 불가 | [IF] 의도적 공백 |
| Layer 4 API 호출 mail-triage 미연결 | 실시간 규제 DB 미활용 | hermes-api-server.py 분리 |

### 제품 분류 수정

**이번 세션에서 보정**:
- `HnVUE` = **SaMD** (Software as a Medical Device — 독립 소프트웨어 의료기기)
- `Retrofit (HnX-R1)` = **SiMD** (Software in a Medical Device — 하드웨어 디지털화 키트 내장 SW)

**적용 문서**: ra-us/eu/kr-SOUL.md 전 3종 수정 완료 (2026-06-11)

**SaMD vs SiMD 규제 함의**:
- HnVUE(SaMD): IMDRF SaMD framework 적용; FDA FDARA §520(o); EU Rule 11; MFDS SDS 필수
- Retrofit(SiMD): 기기 허가 일부로 처리; FDA 510(k) device file; EU 기기 분류 루트; SaMD 독립 경로 불필요

---

## 점검 기록 #1 — 2026-06-11

### 요약 판정

**실사용 가능 상태 ✅** — MVP DoD 전 항목 완료, 미완료 작업 이슈 없음.

### GitHub 이슈 현황

| 구분 | 수 | 비고 |
|------|---|------|
| Open | 1 | #2 `[RULE]` rule-ref 참조 문서 (닫지 않는 이슈) |
| Closed | 33 | 모든 작업 이슈 완료 |

### 단계별 완료 현황

| 단계 | 상태 | 이슈 | 완료일 |
|------|------|------|--------|
| 설계 (ADR-001) | ✅ | #12 | ~06-02 |
| 골격 코드 구현 | ✅ | — | — |
| Honcho T3610 배포 | ✅ | #3 | 06-05 |
| MVP 자동화 스크립트 (SPEC-RA-TOOL-001) | ✅ | #16 | 06-05 |
| RA 프로파일 생성 (ra_us/eu/kr 외 5종) | ✅ | #4 | 06-05 |
| mail-triage n8n 배포 · E2E | ✅ | #5 | 06-08 |
| 투표 인터페이스 [IF] | ✅ | #7 | 06-08 |
| 브릿지 n8n 배포 | ✅ | #8 | 06-06 |
| 3점 평가 루프 n8n · Honcho 기록 | ✅ | #9 | 06-08 |
| Virtual Office Docker · 실데이터 연결 | ✅ | #10 | 06-08 |
| Cold Start E2E 검증 | ✅ | #11 | 06-08 |
| Qdrant → pgvector 포팅 (MIGRATE-1,2) | ✅ | #17, #19 | 06-08 |
| OP 이력 backfill 시드 (SEED-1) | ✅ | #18 | 06-09 |
| warm-start 학습 루프 (GROWTH-1) | ✅ | #20 | 06-09 |
| deriver reflection 활성화 (GROWTH-2) | ✅ | #21 | 06-09 |
| feedback delta 페어링 (GROWTH-3) | ✅ | #22 | 06-09 |
| WP 종결 → case digest (GROWTH-4) | ✅ | #23 | 06-09 |
| 일일 성장 지표 인프라 (GROWTH-5) | ✅ | #24 | 06-09 |
| Layer 4 knowledge_fetch E2E (openFDA/law.go.kr) | ✅ | #30 | 06-10 |
| data.go.kr Layer 4d 통합 (3/3 서비스) | ✅ | #31, #33 | 06-11 |
| hermes-api-server.py 프로파일 라우팅 수정 | ✅ | #28 | 06-10 |
| llm-wiki NAS 갭 (graceful degradation 처리) | ✅ | #29 | 06-10 |
| 정확성·신뢰성 원칙 문서 이식 | ✅ | #32 | 06-10 |
| Playwright E2E 테스트 추가 | ✅ | bc7379f | 06-11 |

### implementation-spec DoD 달성 현황

| # | 기준 | 유형 | 상태 |
|---|------|------|------|
| 1 | Honcho ↔ GX10 Qwen3 tool-calling 검증 | `[구현]` | ✅ |
| 2 | 재전송 메일 → RA 분석 → WP 처리 → Honcho 기록 | `[구현]` | ✅ |
| 3 | 반복 메일 중복 WP 감소 (핵심 지표) | `[구현]` | ✅ GROWTH 완료 |
| 4 | 인프라 3종 투표 집계 결정 산출 | `[IF]` | ⚙️ 의도적 공백 |
| 5 | 브릿지 인프라→업무 단방향 전달 | `[구현]` | ✅ |
| 6 | 3점 평가 Honcho 기록 → 차회 분석 영향 | `[구현]` | ✅ |
| 7 | Virtual Office 실데이터 재생 | `[구현]` | ✅ |

### [IF] 의도적 공백 항목 (버그 아님)

| 파일 | 내용 | 설명 |
|------|------|------|
| `voting/config/vote-rules.json` | 투표 집계 규칙 | 운영 관찰 후 채울 것 |
| `bridge/config/bridge-config.json` | relay_conditions | 운영 중 결정 |
| `feedback/config/weight-adjustment-config.json` | 가중치 공식 | 학습 데이터 쌓인 후 조정 |

### 현재 실사용 가능 기능

- Honcho 서버 (T3610, Docker 구동 중)
- mail-triage n8n 워크플로우 (RPi, E2E 검증)
- RA 에이전트 프로파일 3종 + 관리 에이전트 5종
- 3점 피드백 루프
- GROWTH 학습 루프 전체 (warm-start → deriver → delta → case digest → metrics)
- Layer 4 knowledge_fetch (openFDA, law.go.kr, data.go.kr)
- Virtual Office (목업↔실데이터 전환 가능)
- scripts/ 자동화 17종

### 잔여 과제 (필수 아님, 우선순위순)

1. llm-wiki NAS 라우팅 설정 (T3610 → 10.11.1.40 네트워크)
2. `vote-rules.json` 초기값 결정 (인프라 투표 활성화 시)
3. `growth-metrics.py` systemd timer 실 배포
