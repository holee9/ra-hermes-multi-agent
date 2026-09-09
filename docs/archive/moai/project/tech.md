# RA Hermes 멀티 에이전트 — 기술 참고서

## 런타임 스택

### 에이전트 런타임

**Hermes Agent v0.15.1** (NousResearch, MIT 라이선스)
- 자기개선 루프: 성공한 워크플로우 → 스킬 자동 추출
- 메모리 플러그인: Honcho(내장), mem0, supermemory 등 지원
- 터미널 백엔드: Local, Docker, SSH, Daytona, Singularity, Modal
- 현재 구성: Local(T3610) + Docker(GX10 Ollama)

**특징**:
- 프로파일당 독립 SOUL.md(페르소나), config, 메모리 저장소
- 동일 workspace에 다수 peer 수용(사람 1 + AI N)
- Kanban 보드로 분산 작업 추적 (v0.13.0+)

### 메모리 백엔드

**Honcho v0.15.1** (AI-native 메모리 시스템)

**스택**:
- FastAPI `:8000` — API 서버
- PostgreSQL 15 (pgvector 확장) `:5433` — 벡터 + 메타 저장
- Redis `:6379` — 세션 캐시
- Deriver 워커 — 백그라운드 추론/정제

**설정**:
```bash
# 환경 변수
DB_CONNECTION_URI=postgresql+psycopg://honcho:honcho@localhost:5433/honcho
CACHE_URL=redis://127.0.0.1:6379/0
CACHE_ENABLED=true

# 추론 LLM 위임 (GX10 Qwen3)
DERIVER_MODEL_CONFIG__OVERRIDES__BASE_URL=http://gx10:11434
SUMMARY_MODEL_CONFIG__OVERRIDES__BASE_URL=http://gx10:11434
DREAM_MODEL_CONFIG__OVERRIDES__BASE_URL=http://gx10:11434
```

**핵심 기능**:
- **honcho_search**: 세션 히스토리에서 유사 맥락 검색
- **honcho_context**: AI peer의 활동 컨텍스트 조회
- **honcho_reasoning**: LLM 기반 사후 추론(dialectic)
- **honcho_conclude**: 대화 결론 저장

### LLM 추론 백엔드

**Ollama + Qwen3 (GX10)**

**엔드포인트**: `http://gx10:11434`(OpenAI 호환)

**모델 스펙**:
- Qwen3 (또는 LLaMA 기반 120B)
- Tool calling 필수(function_call 지원)
- 컨텍스트: 128K 이상
- 응답 시간: 초 단위(LAN 속도에 의존, 현재 2.5G)

**검증**(T3610에서):
```bash
curl -X POST http://gx10:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3:120b",
    "messages": [{"role":"user", "content":"test"}],
    "tools": [{"type":"function","function":{"name":"test"}}]
  }'
# 정상: JSON 응답 + tool_call 필드
```

## 하드웨어 토폴로지 (고정)

### 3노드 구성

| 노드 | 사양 | T3610 기준 호스트명 | 역할 |
|------|------|----------------|------|
| **T3610** | Xeon 12C/24T, 32GB RAM, Linux | `localhost` 또는 `192.168.x.x` | Honcho 서버 + RA 에이전트 |
| **GX10** | Grace Blackwell ARM, Qwen3 | `gx10` (DNS/hosts 설정) | LLM 추론 (OpenAI 호환 :11434) |
| **Raspberry Pi 5+** | 16GB RAM | `raspi5p` (alias 권장) | n8n + OpenProject |

**네트워크**:
- T3610 ↔ GX10: 2.5G LAN 직결 (로컬 네트워크)
- T3610 ↔ RPi: 로컬 네트워크 또는 SSH 터널
- 외부 인터넷: 지식 기반 참조용(llm-wiki, ra-project)

## 서비스 포트 바인딩

### T3610 (Honcho 호스트)

| 서비스 | 포트 | 바인드 | 용도 |
|--------|------|--------|------|
| Honcho API | 8000 | 0.0.0.0 | 모든 장비 접근 가능 |
| PostgreSQL | 5433 | 0.0.0.0 | 다른 장비 pgvector 쿼리(백업) |
| Redis | 6379 | 127.0.0.1 | 로컬 캐시만 |

**주의**: 호스트 포트 5432는 기존 사용 중 → Honcho는 5433 사용.

### GX10

| 서비스 | 포트 | 용도 |
|--------|------|------|
| Ollama API | 11434 | LLM 추론 (OpenAI 호환) |
| GPU 모니터링 | (필요시 설정) | 메모리, 온도 |

### Raspberry Pi 5+

| 서비스 | 포트 | 용도 |
|--------|------|------|
| n8n | 5678 | 워크플로우 자동화 |
| OpenProject | 8080 | WP 관리 |

## 벡터 저장소 설정

### pgvector (PostgreSQL 확장)

**차원**: 4096 (Qwen3 임베딩 크기와 매칭)

**초기화**(처음 한 번):
```bash
# honcho/init-vector-dim.sql 실행
psql -h localhost -p 5433 -U honcho -d honcho \
  -c "CREATE EXTENSION IF NOT EXISTS vector;"
psql -h localhost -p 5433 -U honcho -d honcho \
  -c "ALTER DATABASE honcho SET pgvector.max_vectors=1000000;"
```

**테이블**: Honcho가 자동 생성 (embeddings 테이블)

**인덱싱**: 5개 지표 추적
- **정확도(Accuracy)**: WP 매칭 제안 승인률
- **신속도(Velocity)**: 분석 완료 시간(초)
- **신뢰도(Confidence)**: 평균 분석 신뢰도
- **학습량(Learning)**: 일일 피드백 누적
- **자동율(Automation)**: 사람 개입 없는 처리율

## 데이터 계약 (불변)

### RA 분석 결과 JSON

```json
{
  "actor": "ra_us|ra_eu|ra_kr",
  "wp": "WP-123|null",
  "match": "existing|new",
  "confidence": 0.0-1.0,
  "region": "US|EU|KR",
  "comment": "규제분석 요약",
  "transition_proposed": "리뷰중|승인|null"
}
```

**필드 제약**:
- `actor`: 세 RA 에이전트 중 하나
- `wp`: WP ID 형식(숫자) 또는 null
- `confidence`: 실수 0~1
- `region`: 정확히 하나 선택
- `transition_proposed`: 선택적, null 가능
- `confidence`가 `YELLOW_CONFIDENCE_THRESHOLD` 미만이거나 값 자체가 비정상이면 Yellow 게이트로 전환

### 활동 기록 포맷

```json
{
  "ts": "2026-06-10T14:30:00Z",
  "type": "mail_received|matched|comment_added|feedback_submitted|state_changed",
  "actor": "<actor_id>",
  "payload": {...}
}
```

**타입별 payload**:
- `mail_received`: `{ "from": "...", "subject": "...", "message_id": "..." }`
- `matched`: `{ "wp": "WP-123", "confidence": 0.85 }`
- `comment_added`: `{ "wp": "WP-123", "comment": "..." }`
- `yellow_gate`: `{ "yellow_reason": "...", "analysis": {...}, "op_wp_status": {...} }`
- `feedback_submitted`: `{ "wp": "WP-123", "evaluation": "..." }`
- `state_changed`: `{ "wp": "WP-123", "from": "진행중", "to": "리뷰중" }`

### n8n 하드닝 환경변수

| 변수 | 용도 |
|------|------|
| `OPENPROJECT_API_URL` | OpenProject API base URL. workflow 하드코딩 금지 |
| `HONCHO_WORK_WORKSPACE` | RA 업무 workspace 이름 |
| `YELLOW_CONFIDENCE_THRESHOLD` | mail-triage Yellow confidence 기준 |
| `HUMAN_ALERT_WEBHOOK_URL` | Yellow payload 전송 Webhook |
| `BRIDGE_RELAY_CONFIG_JSON` | infra→work bridge [IF] relay 조건 |
| `WEIGHT_ADJUSTMENT_CONFIG_JSON` | feedback [IF] 가중치 조정 공식 |

### 품질 게이트

```bash
npm run test:static   # JSON + n8n Code node + Python/shell syntax
npm test              # static + Playwright virtual-office E2E
```

## 개발 가이드

### [IF] 패턴 (의도적 공백)

**정의**: 인터페이스는 코딩, 내부는 비움 → 운영·학습이 채움.

**위치**:
- `n8n/workflows/feedback-recorder.json` — 가중치 공식 [IF]
- `voting/config/vote-rules.json` — 분산 투표 규칙 [IF]
- `BRIDGE_RELAY_CONFIG_JSON` / payload `bridge_config_json` — 신호 필터링 로직 [IF]

**규칙**:
- 하드코딩된 임계값 금지 (예: `if confidence > 0.8`)
- 외부 설정 파일에서 읽기 (예: config JSON, environment variables)
- [IF] 파일은 운영 중 실험으로 수정, 성숙하면 코드로 이동

### detect-device.sh 사용

모든 스크립트 실행 전에 장비 확인:

```bash
bash scripts/detect-device.sh --print
# 출력: T3610 | GX10 | RPI
```

**목적**: localhost 하드코딩 방지.

**스크립트 내부**:
```bash
source scripts/detect-device.sh  # 함수 로드
DEVICE=$(detect_device)
case $DEVICE in
  T3610) export HONCHO_URL=http://localhost:8000 ;;
  GX10)  export HONCHO_URL=http://t3610:8000 ;;
  RPI)   export HONCHO_URL=http://t3610:8000 ;;
esac
```

### GATE-3 제약 (T3610 파괴 작업)

T3610은 실제 운영 중인 Honcho 서버 호스트.

**금지**:
- ❌ `docker compose down -v` (볼륨 삭제)
- ❌ `DROP DATABASE honcho` (DB 초기화)
- ❌ `TRUNCATE` 테이블
- ❌ PG/Redis 설정 재초기화

**필수 절차**:
1. `scripts/verify-honcho.sh` 로 상태 확인
2. 사람 승인 획득 (GitHub Issue 코멘트 또는 메시지)
3. 백업 생성 (자동 또는 수동)
4. 스크립트 실행

## 키 파일 참조

### 설정 파일

**Honcho docker-compose**:
- `honcho/docker-compose.yml` — 전체 스택 정의
- `honcho/init-workspaces.sh` — work/infra 워크스페이스 생성
- `honcho/.env` — 비밀(DB 암호 등, git-ignored)

**Hermes 프로파일**:
- `profiles/honcho-config-templates/*.json` — 8개 프로파일 설정
- `profiles/souls/*.md` — 8개 SOUL.md 페르소나

**n8n 워크플로우**:
- `n8n/workflows/mail-triage.json` — 이메일 분류
- `n8n/workflows/infra-to-work-bridge.json` — 신호 브릿지
- `n8n/workflows/feedback-recorder.json` — 평가 기록

### 운영 스크립트

- `scripts/detect-device.sh` — 장비 자동 감지
- `scripts/verify-honcho.sh` — Honcho 상태 확인
- `scripts/cold-start-verify.sh` — MVP 초기 실행 검증
- `reports/growth-metrics.py` — 일일 지표 계산
- `profiles/setup.sh` — 프로파일 자동 생성(SPEC-RA-TOOL-001)

### 가상 오피스

- `virtual-office/virtual-office.html` — self-contained 픽셀아트 앱
- `virtual-office/honcho-adapter.js` — Honcho API 연결
- `virtual-office/Dockerfile` — 배포용 컨테이너

## 환경 변수 패턴

### T3610에서 로컬 실행

```bash
export HONCHO_URL=http://localhost:8000
export GX10_URL=http://gx10:11434
export OPENPROJECT_URL=http://raspi5p:8080
export OPENPROJECT_TOKEN=<plain_value>
```

### GX10에서 원격 Honcho 접근

```bash
export HONCHO_URL=http://t3610:8000
export GX10_URL=http://localhost:11434  # 자신의 로컬 Ollama
```

### RPi에서 T3610·GX10 접근

```bash
export HONCHO_URL=http://t3610:8000
export GX10_URL=http://gx10:11434
export OPENPROJECT_URL=http://localhost:8080  # 자신의 로컬 OP
```

**원칙**: localhost 하드코딩 금지 → 항상 `scripts/detect-device.sh` 로 환경 결정.

## 문제 해결

### Honcho 연결 실패

```bash
# 1. 서버 상태 확인
bash scripts/verify-honcho.sh

# 2. API 수동 테스트
curl http://t3610:8000/health

# 3. DB 연결 확인
psql -h t3610 -p 5433 -U honcho -d honcho -c "SELECT 1"

# 4. 로그 확인
docker compose -f honcho/docker-compose.yml logs api
```

### GX10 추론 실패

```bash
# 1. Ollama 상태
curl http://gx10:11434/api/tags

# 2. 모델 로드 상태
curl http://gx10:11434/api/show -d '{"name":"qwen3:120b"}'

# 3. Tool calling 검증
curl -X POST http://gx10:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen3:120b", "messages":[...], "tools":[...]}'
```

### RPi n8n 워크플로우 에러

```bash
# SSH 접속
ssh raspi5p

# n8n 상태
docker compose -f /path/to/n8n/docker-compose.yml logs

# 수동 workflow 트리거
curl -X POST http://localhost:5678/webhook/test-workflow \
  -H "Content-Type: application/json" \
  -d '{"test":"payload"}'
```

## 버전 핀(현재 기준: 2026-06-09)

| 컴포넌트 | 버전 | 핀 날짜 | 비고 |
|---------|------|--------|------|
| Hermes Agent | 0.15.1 | 2026-06-09 | PyPI v0.13.0(내장 Honcho) + Local 0.15.1 |
| Honcho | 0.15.1 | 2026-06-09 | FastAPI, pgvector 지원 |
| Ollama/Qwen3 | latest | 2026-06-09 | GX10, tool-calling 모델 |
| PostgreSQL | 15 + pgvector | 2026-06-09 | 4096차원 벡터 |
| Redis | 7.x | 2026-06-09 | 캐시 백엔드 |
| n8n | latest | 2026-06-09 | RPi 호스트 |
| OpenProject | v17 | 2026-06-09 | RPi 호스트, plain_value 토큰 |

**업그레이드 정책**:
1. 패치 업그레이드는 자동
2. 마이너 업그레이드는 테스트 후 수동
3. 메이저 업그레이드는 SPEC 문서 갱신 후

## 성능 목표

| 지표 | 목표 | 현재 달성 |
|------|------|---------|
| Honcho API 응답 | < 500ms | ✅ 150~300ms |
| RA 분석(Hermes 호출) | < 5초 | ✅ 2~4초 |
| WP 매칭 조회 | < 1초 | ✅ 200~500ms |
| 메일 수신~분석 완료 | < 10초 | ✅ 6~8초 |
| 일일 처리량 | 100+건 | ✅ 현재 15~20건(학습 중) |

---

**마지막 갱신**: 2026-06-09  
**담당**: 기술 아키텍처  
**검증**: scripts/verify-honcho.sh, scripts/detect-device.sh
