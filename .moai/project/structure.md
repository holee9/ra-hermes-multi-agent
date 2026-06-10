# RA Hermes 멀티 에이전트 — 프로젝트 구조

## 시스템 아키텍처

### 작업 공간(Business Workspace) vs 인프라 공간(Infrastructure Workspace)

```
┌─────────────────────────────────────────────────────────────────┐
│  업무 Workspace (work)                                           │
│  ├─ ra_us (FDA 510(k) 담당)                                     │
│  ├─ ra_eu (MDR CE 담당)                                         │
│  ├─ ra_kr (MFDS/KGMP 담당)                                      │
│  ├─ op_manager (OpenProject 사안 추적)                          │
│  └─ n8n_manager (자동화 워크플로우 관리)                         │
├─ RI 소집(투표) ←┐                                               │
└───────────────┼────────────────────────────────────────────────┘
                │
┌───────────────┼────────────────────────────────────────────────┐
│  인프라 Workspace (infra)                                       │
│  ├─ infra_t3610 (Honcho 서버 호스트)                            │
│  ├─ infra_gx10 (LLM 추론 엔진)                                  │
│  └─ infra_rpi (n8n + OpenProject 호스트)                        │
│  └─ 셋이 협의 → 분산 투표 기반 판단                             │
└────────────────────────────────────────────────────────────────┘

흐름:
이메일 → n8n mail-triage → RA 분석(Hermes) → WP 반영 → Honcho 기록
↓
학습 피드백(사람 3점) → Deriver → 다음 판단에 반영
```

## 에이전트 맵

### 업무 Workspace (5 에이전트)

| 에이전트 ID | 역할 | SOUL.md 인물 | 책임 |
|----------|------|-----------|------|
| `ra_us` | FDA 규제 분석 | Mike | 510(k), 실질적 동등성(SE), 임상자료 미국 기준 |
| `ra_eu` | MDR 규제 분석 | Theo | CE MDR, Notified Body 심사, 임상근거 EU 기준 |
| `ra_kr` | KGMP 규제 분석 | Sam | MFDS 허가, 국제 정합(OECD), 한국 특수성 |
| `op_manager` | WP 라이프사이클 추적 | Margot | OpenProject 상태 전이, 완료 판정, 히스토리 |
| `n8n_manager` | 자동화 개선 | Olly | mail-triage 워크플로우 수정, 신규 규칙 추가 |

### 인프라 Workspace (3 에이전트)

| 에이전트 ID | 역할 | SOUL.md 인물 | 책임 |
|----------|------|-----------|------|
| `infra_t3610` | Honcho 서버 관리 | Finn | Docker, PostgreSQL, API 상태 모니터링 |
| `infra_gx10` | LLM 추론 엔진 | Leo | Ollama/Qwen3 성능, GPU 메모리, 응답 시간 |
| `infra_rpi` | n8n & OpenProject | Gus | RPi 호스트, 네트워크, 포트, 볼륨 마운트 |

**투표 방식**: 분산 합의 기반. 인프라 3노드가 장애/성능 이슈를 감지하면 자율로 투표 소집 → 업무 팀에 알림.

## 모듈별 책임

### 루트 디렉토리 구조

```
/
├─ .moai/
│  ├─ project/                    # 프로젝트 메타데이터
│  │  ├─ product.md               # 제품 비전 (이 문서)
│  │  ├─ structure.md             # 프로젝트 구조 (현재 파일)
│  │  └─ tech.md                  # 기술 스택
│  └─ specs/                      # SPEC 문서 (실행 계획)
│
├─ docs/                          # 사용자 문서
│  ├─ RA-multi-agent-master-design.md     # 마스터 설계서
│  ├─ implementation-spec.md      # 구현 명세(코딩 경계)
│  ├─ operations-guide.md         # 운영 가이드
│  ├─ usage-guide.md              # 에이전트 사용 설명서
│  └─ ECOSYSTEM.md                # 전체 생태계 맵
│
├─ bridge/                        # n8n 브릿지 (인프라 ← → 업무)
│  ├─ relay-conditions.json       # [IF] 중계 규칙(운영이 설정)
│  └─ bridge-trigger.py           # Honcho 신호 감지 스크립트
│
├─ honcho/                        # Honcho 서버 설정 (T3610)
│  ├─ docker-compose.yml          # 전체 스택
│  ├─ init-workspaces.sh          # 두 workspace 생성 스크립트
│  ├─ init-vector-dim.sql         # pgvector 4096차원 설정
│  └─ Dockerfile                  # 커스텀 이미지 (필요시)
│
├─ n8n/                           # n8n 워크플로우 (RPi)
│  ├─ workflows/
│  │  ├─ mail-triage.json         # 이메일 분류 → WP 자동화
│  │  ├─ infra-to-work-bridge.json # 인프라 신호 → 업무팀
│  │  └─ feedback-recorder.json   # 사람 평가 → Honcho 기록
│  └─ IMPORT.md                   # n8n import 가이드
│
├─ profiles/                      # Hermes 프로파일 설정 (T3610)
│  ├─ honcho-config-templates/
│  │  ├─ ra-us.json               # FDA 프로파일 템플릿
│  │  ├─ ra-eu.json               # MDR 프로파일 템플릿
│  │  ├─ ra-kr.json               # KGMP 프로파일 템플릿
│  │  ├─ op-manager.json
│  │  ├─ n8n-manager.json
│  │  ├─ infra-t3610.json
│  │  ├─ infra-gx10.json
│  │  └─ infra-rpi.json
│  │
│  ├─ souls/                      # SOUL.md 페르소나
│  │  ├─ ra-us.md                 # Mike의 FDA 전문성
│  │  ├─ ra-eu.md                 # Theo의 MDR 전문성
│  │  ├─ ra-kr.md                 # Sam의 KGMP 전문성
│  │  ├─ op-manager.md            # Margot의 WP 추적 노하우
│  │  ├─ n8n-manager.md           # Olly의 자동화 개선
│  │  └─ infra.md                 # 3인 인프라팀 협력 규칙
│  │
│  └─ setup.sh                    # 프로파일 자동 생성 (SPEC-RA-TOOL-001)
│
├─ reports/                       # 성장 지표 및 분석
│  ├─ growth-metrics.py           # 일일 지표 계산 (GROWTH-5)
│  └─ 2026-06-metrics.csv         # 누적 데이터
│
├─ scripts/                       # 운영 스크립트
│  ├─ detect-device.sh            # 현재 장비 자동 식별
│  ├─ verify-honcho.sh            # Honcho 서버 상태 확인
│  ├─ cold-start-verify.sh        # MVP 기동 점검(GROWTH-1 워밍)
│  ├─ extract-mail-qa.py          # pgvector 이메일 QA 추출
│  └─ openproject-backfill.py     # OP 기존 WP → Honcho 시드
│
├─ virtual-office/                # 가상 오피스 (시각화)
│  ├─ virtual-office.html         # 자체 포함 픽셀아트 앱
│  ├─ virtual-office-org-chart.md # 캐릭터 ↔ 에이전트 매핑
│  ├─ pixel-character-guide.md    # 스프라이트 가이드
│  ├─ virtual-office-mvp.md       # MVP 설계
│  ├─ Dockerfile                  # 단일 컨테이너 배포
│  └─ honcho-adapter.js           # Honcho API ↔ HTML 연결
│
├─ voting/                        # 인프라 투표 집계 ([IF])
│  ├─ vote-aggregator.js          # 분산 투표 인터페이스
│  ├─ vote-rules.json             # [IF] 내부 규칙 (운영 설정)
│  └─ consensus-engine.md         # 투표 메커니즘 설명
│
└─ README.md                      # 현재 상태 요약
```

## 통합 지점(Integration Points)

### 1. 이메일 입수 → n8n mail-triage

**흐름**:
```
Gmail(재전송) 
  → n8n webhook 수신
  → 본문 파싱(정규화)
  → 규제권 라우팅 판정(FDA/MDR/MFDS)
  → Hermes ra_us|ra_eu|ra_kr 호출(/v1/chat/completions)
  → WP 매칭(OpenProject)
  → Honcho conclusion 저장
```

**책임 분담**:
- **n8n(RPi)**: 메일 수신, 파싱, 라우팅, API 호출 조율
- **Hermes(T3610)**: 규제분석 실행
- **OpenProject(RPi)**: WP CRUD
- **Honcho(T3610)**: 분석 결과 메모리 저장

### 2. 인프라 신호 → 브릿지 → 업무팀

**흐름**:
```
infra_* 에이전트(투표)
  → n8n infra-to-work-bridge.json
  → [IF] relay-conditions 검토
  → op_manager 또는 모니터링 알림
```

**책임 분담**:
- **인프라 Workspace**: 장애/성능 감지, 투표 소집
- **n8n 브릿지**: 신호 전달, 필터링
- **op_manager**: 확인 및 에스컬레이션

### 3. 사람 피드백 → Honcho 학습

**흐름**:
```
사람(RA 담당/리더)
  → n8n feedback-recorder 또는 CLI
  → 3점 평가 제출(판단근거, 실제결과, 점수)
  → Honcho AI peer 기록
  → Deriver 백그라운드 추론
  → 다음 판단에 Warm-Start로 주입
```

**책임 분담**:
- **사람**: 판단 근거·피드백 제출
- **n8n/CLI**: 데이터 수집
- **Honcho**: 저장 및 추론 기동

### 4. 가상 오피스 ← 활동 기록

**흐름**:
```
Honcho activity log
  ← 모든 판단(mail-triage 분석)
  ← 모든 피드백(사람 평가)
  ← 모든 상태 전이(WP 변경)
  → virtual-office.html (단방향 읽기)
  → 픽셀아트 시각화(에이전트 활동)
```

**책임 분담**:
- **Honcho**: 이벤트 기록
- **honcho-adapter.js**: API 조회
- **virtual-office.html**: 렌더링

## 데이터 계약 (Frozen)

### RA 분석 결과 JSON

```json
{
  "actor": "ra_us|ra_eu|ra_kr",
  "wp": "WP-123|null",
  "match": "existing|new",
  "confidence": 0.0-1.0,
  "region": "US|EU|KR",
  "comment": "분석 내용 요약",
  "transition_proposed": "리뷰중|승인|null"
}
```

**의미**:
- `actor`: 분석을 수행한 RA 에이전트
- `wp`: 매칭되는 기존 WP ID (없으면 null)
- `match`: 기존 WP 매칭 여부
- `confidence`: 신뢰도(0~1)
- `comment`: 규제분석 결과
- `transition_proposed`: 권장 상태(선택적)

### 활동 기록(Activity Log) JSON

```json
{
  "ts": "2026-06-10T14:30:00Z",
  "type": "mail_received|matched|comment_added|feedback_submitted|state_changed",
  "actor": "ra_us|ra_eu|ra_kr|op_manager|n8n_manager|infra_t3610|infra_gx10|infra_rpi|human|system",
  "payload": {...}
}
```

**의미**:
- `ts`: ISO8601 타임스탬프
- `type`: 이벤트 종류
- `actor`: 이벤트 발생자
- `payload`: 이벤트별 상세 데이터

## Gate 규칙 (코딩된 경계)

| 조작 | 권한 | 코드 구현 |
|------|------|---------|
| RA 분석 실행 | 에이전트 자율(Green) | n8n mail-triage에 포함 |
| 기존 WP 코멘트 추가 | 에이전트 자율(Green) | OpenProject API call |
| 신규 WP 생성 | 에이전트 자율(Green) | OpenProject API call |
| 상태 전이(리뷰중→승인 등) | Yellow(사람 확정) | n8n 조건 분기, 수동 승인 필수 |
| n8n 워크플로우 수정 | Yellow(사람 확정) | n8n 자체 편집 권한 |
| **WP 완료(Close)** | **Red(사람 전용)** | **n8n에서 조건 차단** |
| **WP 재개(Reopen)** | **Red(사람 전용)** | **n8n에서 조건 차단** |
| 인프라 구조 변경 | Red(사람 승인) | scripts/ 실행 시 확인 프롬프트 |

## 코딩 vs 운영 (경계)

### 이 레포에서 코딩하는 것([구현])

✅ n8n 워크플로우 (mail-triage, bridge, feedback-recorder)  
✅ 메일 본문 파싱 정규식  
✅ 규제권 라우팅 로직  
✅ OpenProject API 호출  
✅ Honcho conclusion 저장  
✅ WP 자동 매칭 알고리즘  
✅ 투표 인터페이스 (vote-aggregator.js)  
✅ 가상 오피스 웹앱  
✅ 성장 지표 계산 스크립트

### Hermes 운영이 담당하는 것([IF] 의도적 공백)

⚠️ RA 프로파일 SOUL.md(페르소나, 판단 철학)  
⚠️ Honcho 학습 루프(deriver, 추론, 피드백 가중치)  
⚠️ n8n relay-conditions(브릿지 신호 필터링)  
⚠️ voting/vote-rules.json(분산 투표 규칙)  
⚠️ n8n feedback-recorder 가중치 공식  

**원칙**: [IF] 항목은 인터페이스만 코딩, 내부는 비워둠 → 운영·학습이 실험으로 채움.

## 디렉토리 참조

### `docs/`
- **용도**: 사용자 및 운영진 문서
- **관리**: 설계서, 가이드, 예제
- **동기화**: SPEC 변경 시 매번 갱신

### `honcho/`
- **용도**: T3610 Honcho 서버 설정
- **관리**: docker-compose, 초기화 SQL, workspace 스크립트
- **배포**: `docker-compose up -d`

### `n8n/`
- **용도**: RPi n8n 워크플로우 정의
- **관리**: JSON 워크플로우 3개(mail-triage, bridge, feedback-recorder)
- **배포**: n8n UI 임포트

### `profiles/`
- **용도**: Hermes 프로파일 템플릿 및 SOUL.md
- **관리**: honcho-config, SOUL 페르소나, setup.sh
- **배포**: T3610 `bash profiles/setup.sh`

### `scripts/`
- **용도**: 운영 자동화
- **관리**: 상태 확인, 초기화, 마이그레이션
- **실행**: 항상 `bash scripts/detect-device.sh --print` 로 환경 확인 후

### `voting/`
- **용도**: 인프라 분산 투표 인터페이스
- **관리**: vote-aggregator.js, vote-rules.json([IF])
- **운영**: 규칙은 운영 중에 학습으로 채움

### `virtual-office/`
- **용도**: 픽셀아트 시각화 (에이전트 활동 모니터)
- **배포**: self-contained HTML 또는 Docker 컨테이너

---

**마지막 갱신**: 2026-06-09  
**담당**: 프로젝트 아키텍처  
**검증**: GitHub Issues / code review
