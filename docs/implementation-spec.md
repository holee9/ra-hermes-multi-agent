# 구현 명세서 (Implementation Spec)

> **대상 독자: AI 코딩 툴(Claude Code CLI / Codex CLI 등) 및 구현 담당.** 툴 중립.
> **원칙**: 인터페이스는 엄격히 고정, 내부 구현은 위임. 이 시스템은 *학습하며 성장*하므로, 평가로 수렴할 규칙(투표·가중치·임계)은 **의도적 공백**으로 둔다 — 미결이 아니라 설계다. 그 부분은 인터페이스만 만들고 내부는 운영·학습이 채운다.
> **정확성 우선 원칙**: 의료기기 인허가 도메인에서 속도보다 정확성이 항상 우선한다. **Cold start(임계값 미설정) 상태에서는 모든 판단을 Yellow 게이트(사람 확인)로 처리한다.** 자동 처리 비중은 학습·평가 누적 이후에만 단계적으로 확대한다.
> **성숙도 표기**: `[구현]` 코딩 가능 깊이로 명세 / `[IF]` 인터페이스만 — 내부는 PoC·학습이 채움(임의 구현 금지, 비워두거나 사람에게 질의).
> 사실 기준일 2026-06-13. 상세 설계 근거는 RA-multi-agent-master-design.md 참조.

---

## 0. 무엇을 만드는가 (목표지향점)

**학습하며 성장하는 RA 멀티 에이전트 시스템.** 코딩이 만드는 것은 *자라날 그릇*이고, Hermes 운영이 그 그릇을 *채워 키운다*. MVP는 전체 골격이 cold start로 한 바퀴 도는 상태, 프로덕션은 같은 골격이 평가 누적으로 성숙한 상태. **새 기능으로 프로덕션이 되는 게 아니라, 같은 골격이 학습으로 깊어져 프로덕션이 된다.**

### 코딩 산출물 vs Hermes 운영 (경계)
- **코딩으로 만든다**: n8n 워크플로우(mail-triage), 본문 파싱·매칭·라우팅 로직, Honcho 기록 연동, 투표 집계 자리, 가상 오피스 웹앱.
- **Hermes 운영으로 굴러간다**(코딩 아님): RA 프로파일·SOUL.md, Honcho 학습 루프, 사후 3점 평가, 프로파일별 메모리 누적.
- 경계 위반 금지: 이미 Hermes가 제공하는 것(메모리·세션·스킬 자기개선)을 다시 코딩하지 말 것.

---

## 1. 시스템 구성 (전체 골격)

```
업무 workspace                          인프라 workspace
 ├ ra_us / ra_eu / ra_kr (Hermes 프로파일)  ├ infra_t3610 / infra_gx10 / infra_rpi
 ├ op_manager                              └ (셋이 투표로 종합 판단)
 └ n8n_manager
        │                                         │
   [n8n: mail-triage, 게이트, 출력]  ←브릿지(n8n)←┘
        │
   OpenProject (WP)  ·  Honcho(T3610, 두 workspace)  ·  GX10 Qwen3(추론)
        │
   가상 오피스 웹앱 (Honcho 활동 기록 단방향 읽기)
```

---

## 2. 컴포넌트별 명세

### 2.1 Honcho 서버 `[구현]`
- 스택: API(:8000) + deriver + PostgreSQL(pgvector/pgvector:pg15) + Redis. docker-compose.
- 환경: `DB_CONNECTION_URI=postgresql+psycopg://...`(프리픽스 필수), `CACHE_URL=redis://...`, `CACHE_ENABLED=true`.
- LLM 위임: Deriver/Dialectic/Summary/Dream의 `*_MODEL_CONFIG__OVERRIDES__BASE_URL`을 GX10 Qwen3로. **tool calling 지원 필수.**
- workspace 2개 생성: `work`, `infra`.
- 포트 바인딩: API·PG는 LAN(0.0.0.0) 오픈 — T3610 멀티 장비 접근 목적. PG 호스트 포트는 5433(호스트 기존 5432 충돌 회피). Redis는 루프백(127.0.0.1) 유지.
- 빠른 경로: elkimek/honcho-self-hosted 자동 스크립트 활용 가능.

### 2.2 RA 전문가 프로파일 (Hermes 운영 — 코딩 아님)
- `hermes profile create ra-us` → `--clone`으로 ra-eu·ra-kr.
- 각 honcho.json host 블록: `workspace="work"`, `aiPeer="ra_us|ra_eu|ra_kr"`.
- SOUL.md는 운영 전략서가 정의.

### 2.2a 자율 학습 scheduler peer 계약 `[구현]`

`scripts/autonomous-study-scheduler.py`는 Hermes 프로파일 ID와 Honcho peer ID를 분리해서 다룬다.

| 개념 | 형식 | 예 |
|---|---|---|
| Hermes profile / SOUL directory | hyphen | `ra-us`, `ra-eu`, `ra-kr` |
| Honcho peer / aiPeer / memory key | underscore | `ra_us`, `ra_eu`, `ra_kr` |

고정 규칙:

- Honcho `sessions.metadata.actor`, message `peer_id`, message metadata `actor`, bootstrap progress key는 모두 underscore peer ID만 사용한다.
- `profile_id`는 SOUL.md 로딩과 region filter 등 프로파일 선택에만 사용한다.
- `peer_id`에 하이픈이 들어가면 preflight에서 실패해야 한다.
- study message 본문은 deriver가 바로 domain fact로 읽을 수 있는 자연어 텍스트여야 하며, raw JSON envelope를 Honcho content에 넣지 않는다.
- structured 필드는 metadata에 보존한다: `record_type`, `actor`, `peer_id`, `profile_id`, `source`, `chunk_id`, `topic`, `confidence`.
- 변경 후에는 `python3 scripts/verify-study-scheduler.py`를 통과해야 한다.

#49 복구에서 확인된 금지 패턴:

- wrong-peer messages/documents/queue를 SQL rename으로 `ra-us -> ra_us` 처리하지 않는다.
- wrong-peer derived documents를 정상 peer로 직접 이식하지 않는다.
- recoverable raw payload만 추출해 clean text로 replay한다.

복구 replay 도구:

```bash
set -a && . scripts/.env && set +a
python3 scripts/replay-study-insights-issue49.py          # dry-run
python3 scripts/replay-study-insights-issue49.py --execute --batch-size 50
```

### 2.3 mail-triage 워크플로우 (n8n) `[구현]`
입력: 재전송 Gmail. 출력: OpenProject WP 코멘트/생성 + Honcho conclusion 기록.
- **본문 파싱** `[구현]`: 재전송 본문에서 원 제목·원 발신자·사안 식별자 추출 → 정규화 매칭 키. (헤더는 재전송으로 파괴됨 → 본문 기반)
- **규제권 라우팅** `[구현]`: 본문의 규제기관(FDA/MDR/MFDS)·제출 종류 → ra_us|ra_eu|ra_kr 결정. 판별 불가 시 사람 질의(Yellow).
- **RA 호출** `[구현]`: 해당 프로파일을 Hermes `/v1/chat/completions`(또는 게이트웨이)로 호출, 분석 결과 수신.
- **WP 반영** `[구현]`: 기존 WP 매칭 시 OpenProject 상태를 먼저 조회한다. 오픈·진행중·리뷰중 계열 상태만 자율 코멘트(Green)를 허용하고, 완료·종결·닫힘·조회 실패·불명 상태는 Yellow로 전환한다. 미매칭 시에는 신규 WP를 생성한다.
- **기록** `[구현]`: 사안↔WP 매핑을 Honcho conclusion으로 기록(다음 회차 매칭에 사용).
- **게이트** `[구현]`: 매칭·코멘트=자율(Green), 단 기존 WP가 허용 상태일 때만. 상태 전이 제안·저신뢰 분석·파싱 실패·라우팅 불명확·완료/종결 WP 매칭은 Yellow(사람 확정). 완료=사람 전용(불변, 코드로 차단).

#### mail-triage 데이터 계약 (입출력 고정)
RA 분석 결과 JSON(고정):
```json
{ "actor":"ra_us", "wp":"WP-123|null", "match":"existing|new",
  "confidence":0.0-1.0, "region":"US|EU|KR",
  "comment":"...", "transition_proposed":"리뷰중|null" }
```

#### mail-triage 안전 게이트 계약 (#43, #44)

Yellow 게이트로 전환되는 조건은 보수적으로 유지한다.

| 조건 | `yellow_reason` | 처리 |
|------|-----------------|------|
| RA 응답 JSON 파싱 실패 | `parse_error` | 사람 검토 payload 생성, 자동 WP 반영 중단 |
| 필수 필드 누락 | `missing_fields` | 누락 필드 포함해 사람 검토 |
| `confidence`가 숫자/0~1 범위가 아님 | `invalid_confidence` | 사람 검토 |
| `YELLOW_CONFIDENCE_THRESHOLD` 미설정/비정상 | `threshold_unconfigured` | cold start로 간주해 사람 검토 |
| `confidence < YELLOW_CONFIDENCE_THRESHOLD` | `low_confidence` | 사람 검토 |
| 기존 WP ID 누락 | `wp_id_missing` | 사람 검토 |
| OpenProject 상태 조회 실패 | `wp_status_lookup_failed` | 사람 검토 |
| 매칭 WP가 완료/종결/닫힘 계열 | `wp_closed_or_done` | 사람 검토, 재오픈/신규 생성은 사람 결정 |
| 매칭 WP 상태가 허용 목록 밖 | `wp_status_unknown` | 사람 검토 |
| 규제권 미판별/다중 판별 | `yellow_no_region`, `yellow_multi_region` | 담당자 수동 배정 |

Yellow payload는 `human_alert`에 표준화한다. `HUMAN_ALERT_WEBHOOK_URL`이 있으면 Webhook으로 전송하고, 없으면 n8n 실행 로그와 payload만 남긴다. `HUMAN_ALERT_EMAIL`은 채널 메타데이터로 남기되, 실제 이메일 발송 노드는 운영자가 별도 SMTP 설정 후 연결한다.

#### OpenProject 상태 허용 계약 (#44)

기존 WP에 대한 자율 코멘트는 다음 상태명 패턴에만 허용한다.

| 분류 | 패턴 |
|------|------|
| 허용 | `open`, `new`, `progress`, `review`, `오픈`, `진행`, `리뷰`, `검토` |
| 차단 | `closed`, `done`, `complete`, `completed`, `완료`, `종결`, `닫힘` |

OpenProject 응답의 상태 필드는 `status.title`, `status.name`, `_embedded.status.title`, `_embedded.status.name`, `_links.status.title`, `_links.status.name` 순서로 읽는다. 응답에 `id`가 없거나 오류 payload로 보이면 조회 실패로 처리한다.

#### n8n 환경변수/config 계약 (#45)

| 변수 | 필수 | 용도 | 비고 |
|------|------|------|------|
| `HONCHO_API_URL` | 필수 | Honcho API base URL | 예: `http://t3610:8000` |
| `HONCHO_WORK_WORKSPACE` | 필수 | work workspace 이름 | 기본 운용값은 n8n `.env`에서 관리 |
| `OPENPROJECT_API_URL` | 필수 | OpenProject API base URL | hardcode 금지 |
| `OPENPROJECT_DEFAULT_PROJECT_ID` | 필수 | 신규 WP 생성 대상 project | 운영 환경별 값 |
| `YELLOW_CONFIDENCE_THRESHOLD` | 필수 | Yellow 전환 confidence 기준 | 미설정/비정상은 Yellow |
| `HUMAN_ALERT_WEBHOOK_URL` | 선택 | Yellow payload 전송 Webhook | 비워도 workflow는 동작 |
| `HUMAN_ALERT_EMAIL` | 선택 | 알림 대상 메타데이터 | SMTP 노드 연결 시 사용 |
| `BRIDGE_RELAY_CONFIG_JSON` | 선택 | bridge relay 조건 | 비우면 초기 기본값(전달) |
| `WEIGHT_ADJUSTMENT_CONFIG_JSON` | 선택 | feedback 가중치 공식 자리 | 비우면 기록만 하고 조정 생략 |

#### mail-triage 검증 절차

레포 레벨 검증:

```bash
npm run test:static
npm test
```

운영 import 후 RPi n8n에서 확인할 시나리오:

1. 낮은 confidence 응답 → `low_confidence` Yellow payload 생성, WP 생성/코멘트 미실행.
2. `YELLOW_CONFIDENCE_THRESHOLD` 미설정 → `threshold_unconfigured` Yellow 전환.
3. 기존 WP가 open/progress/review 계열 → 기존 WP 코멘트 추가.
4. 기존 WP가 closed/done/완료/종결 계열 → `wp_closed_or_done` Yellow 전환.
5. OpenProject 인증/네트워크 실패 → `wp_status_lookup_failed` Yellow 전환.
6. `HUMAN_ALERT_WEBHOOK_URL` 설정 → Webhook payload 수신 확인.

### 2.4 인프라 에이전트 + 투표
- 프로파일 3개: infra_t3610·infra_gx10·infra_rpi, `workspace="infra"`. (Hermes 운영)
- **투표 소집** `[IF]`: 위험 감지한 에이전트가 자율 소집. *소집 임계 조건의 구체 값은 비움* — PoC·학습이 정함.
- **투표 집계** `[IF]`: 표를 받아 집계하는 *자리*만 구현(입력=표 배열, 출력=결정). **집계 규칙(정족수·가중치)은 임의 구현 금지.** 초기엔 가장 단순한 형태로 운영을 시작하되 그 형태는 사람이 정한다. 가중치는 평가로 사후 조정되므로 코드에 하드코딩하지 않고 외부에서 읽는다.
  - 입력 IF: `[{actor, vote, topic}]`  출력 IF: `{topic, result}`
  - Hermes Kanban(v0.13.0)을 공유 작업 보드로 활용 가능.

### 2.5 브릿지 (n8n) `[구현 + IF]`
- 인프라 workspace 합의 결론 → 업무 workspace로 옮겨 쓰는 **출력 동작** `[구현]`.
- 방향: 인프라→업무 단방향. 판단=인프라 셋, 출력=n8n.
- **전달 임계 조건** `[IF]`: 무엇을 흘릴지의 구체 규칙은 비움 — 운영하며 관찰된 패턴으로 채움.
- **순환 의존 차단** `[구현]`: Honcho 서버 자체 장애는 Honcho 경유 금지 → n8n이 Honcho 우회 직접 경보(별도 규칙).

### 2.6 사후 평가 루프 `[구현 + IF]`
- **평가 입력** `[구현]`: 사람이 결정에 3점(나쁨·보통·좋음) + 근거 한 줄. → Honcho에 기록되는 자리.
- **가중치 반영** `[IF]`: 평가가 사안 영역별 가중치를 조정하는 *연결*만 구현. 조정 공식은 비움 — 학습이 정함. 평가된 결정만 반영, 무평가=중립.

### 2.7 가상 오피스 웹앱 `[구현]`
- 현 virtual-office.html이 목업 기반 프로토타입(완성). 
- **데이터 소스** `[구현]`: `DATA_SOURCE` 환경변수로 목업↔Honcho 전환. Honcho 활동 기록을 이벤트 배열로 읽어 재생.
- 캐릭터: 코드 픽셀 기본값. Kenney CC0 PNG로 교체 가능(sprite 경로, pixel-character-guide.md).
- 배포: Docker 단일 컨테이너. 관찰자(읽기 전용) — 뼈대 무개입.

---

### 2.8 문서 변환 전처리 (doc-converter) `[구현]`
- 역할: HWP/DOCX/PDF/PPTX/XLS 원본 → 텍스트 추출 → **pgvector ra_knowledge 직접 인덱싱**.
- **[HARD] llm-wiki·ra-project·MD-process는 완전 읽기 전용 — 이 레포에서 절대 쓰지 않는다.** 이 스크립트는 pgvector에만 쓴다.
- 도구: claude-tomd-skill(외부, Claude Code 스킬). 한국어·HWP 95, DOCX/PDF 95, Obsidian/Claude Code 98, **XLS 75(병합셀·표구조 약함)**.
- 용도 분기: 서술형 RA 문서(심사의견·가이드라인·보고서·공문·교육자료)는 변환 적용. **XLS 구조화 데이터(검증 매트릭스·RTM)는 표 손상 위험 → 선별 적용 또는 원본 유지.**
- 규제 안전: 변환물을 규제 판단의 유일 근거로 삼지 말 것 → 중요 사안은 원본 병행·사람 검증(기존 게이트 원칙).
- 종속 회피: 개인 제작물(유지보수 불확실) → 변환 단계는 **교체 가능하게**, 시스템이 강하게 종속되지 않도록.

---

## 3. 데이터 계약 (코딩 산출물 ↔ Hermes 운영 접점)

### 3.1 활동 기록 = 뼈대 출력 = 가상 오피스 입력 (고정)
```json
{ "ts":"ISO8601", "type":"mail_received|matched|comment_added|transition_proposed|vote_opened|vote_cast|vote_result|score_given",
  "actor":"<actor_id>", "payload":{...} }
```
- 이 형식이 n8n·Hermes가 Honcho에 남기는 기록이자 가상 오피스가 읽는 형식. 양쪽이 이 계약을 기준으로 만든다.
- actor_id(기계): ra_us/ra_eu/ra_kr/op_manager/n8n_manager/infra_*/human/system. 살 이름 매핑은 가상 오피스 내부(virtual-office-org-chart.md).

---

## 4. 수용 기준 (MVP 한 바퀴)

전체 골격이 cold start로 한 사이클 도는 것 = MVP 성공.
1. `[구현]` Honcho가 GX10 Qwen3로 deriver 관찰 추출 성공(tool-calling 검증).
2. `[구현]` 재전송 메일 → ra_us 분석 → 허용 상태의 미완료 WP 코멘트 / 신규 WP 생성 → Honcho 기록. 저신뢰·완료 WP 매칭·조회 실패는 Yellow 전환.
3. `[구현]` 동일 사안 반복 메일에서 중복 WP 생성 감소(핵심 지표).
4. `[IF]` 인프라 3종이 투표 자리에서 표를 집계해 결정 산출(규칙은 단순 시작).
5. `[구현]` 브릿지가 인프라 결정을 업무 workspace로 전달.
6. `[구현]` 사람 3점 평가가 Honcho에 기록되어 차회 분석에 영향.
7. `[구현]` 가상 오피스가 Honcho 활동 기록을 읽어 재생(목업→실데이터 전환).

---

## 5. 구현 금지·주의

- `[IF]` 표시 부분의 내부 규칙을 임의로 하드코딩하지 말 것 — 비워두고 외부 설정/사람 결정에 위임.
- Hermes 제공 기능(메모리·세션·스킬 자기개선·Kanban) 재구현 금지.
- 완료/재오픈 전이는 코드로 사람 전용 보장(에이전트 경로 차단).
- 가상 오피스는 읽기 전용 — 뼈대에 쓰기 금지.
- 가중치·임계값은 코드 상수 금지 → 외부에서 읽어 운영 중 조정 가능하게.

---

## Phase 2: T자형 가로획 구축 (MVP 완료 후 다음 단계)

> MVP 골격이 학습을 시작했다면, 다음 단계는 지식 토대(가로획)를 살아있는 파이프라인으로 연결하는 것이다.

### P2.1 ra-project / MD-process 자동 인덱싱 `[구현]` (#34)

- 대상: `ra-project/`, `MD-process/` 레포의 마크다운 파일
- 스크립트: `scripts/index_ra_knowledge.py` 확장
- 인덱싱: Honcho pgvector (4096차원, qwen3-embedding)
- 증분: 변경 파일만 재인덱싱 (파일 해시 또는 mtime 비교)
- 자동화: systemd timer (일 1회)
- 방향: **단방향 참조** — 가로획 레포에 쓰기 금지, 에이전트는 읽기만

### P2.2 llm-wiki NAS 연결 `[구현]` (#35)

- 경로: Tailscale `diskstation:7001` 경유
- T3610 Tailscale 클라이언트 설치·인증 필요
- 연결 성공 후 `index_ra_knowledge.py` NAS 경로 활성화
- 실패 시 graceful degradation 유지

### P2.3 doc-converter `[구현]` (#36)

- 입력: HWP/DOCX/PDF/PPTX (서술형 RA 문서)
- 변환: claude-tomd-skill (교체 가능 설계)
- 출력: pgvector ra_knowledge 직접 인덱싱 (`source_path: nas://...` 형식, llm-wiki에 쓰지 않음)
- XLS 처리: 표구조 손상 위험 — 선별 적용 또는 원본 유지
- 제약: 시스템이 claude-tomd-skill에 강하게 종속되지 않도록

### P2.4 source-level curriculum seed `[구현]` (#50)

- 목적: 이미 `ra_knowledge`에 색인된 원천을 chunk별 LLM bootstrap보다 빠르게 담당 RA peer에 이식한다.
- 스크립트: `scripts/curriculum-seed.py`
- 검증: `scripts/verify-curriculum-seed.py`
- 출력: Honcho `messages`에 clean text `curriculum_seed` 기록.
- metadata 계약: `record_type`, `actor`, `peer_id`, `profile_id`, `curriculum_version`, `source`, `source_hash`, `chunk_count`, `sampled_chunk_count`, `matched_keywords`.
- idempotence: `peer_name + curriculum_version + source_hash` 기준으로 이미 seed된 source를 건너뛴다.
- 안전 장치: 프로파일 ID는 hyphen(`ra-kr`), Honcho peer ID는 underscore(`ra_kr`)로 분리한다. content는 JSON envelope 금지.
- precision 기본값: `wiki/entities/*`는 제외한다. 엔티티 페이지는 초기 전문성 seed가 아니라 보조 context로 취급한다.
- 2026-06-15 상태: `ra_us` 48건, `ra_eu` 31건, `ra_kr` 29건 explicit source seed 완료. JSON envelope 0, correct metadata 108/108, idempotence `to_seed=0`, RA deriver pending 0.

### P2.5 daily KB-driven growth runner `[구현]` (#51)

- 목적: 메일이 몇 달간 없어도 RA 담당자가 매일 지식베이스 기반으로 성장하도록 한다.
- 스크립트: `scripts/daily-growth-runner.py`
- 비메일 성장 cadence 루프: `scripts/non-email-growth-loop.py`
- 사전 전환 루프: `scripts/pre-auto-growth-loop.py`
- 자동 실행 entrypoint: `scripts/auto-growth-runner.sh`, `scripts/systemd/hermes-auto-growth.{service,timer}`
- pre-production readiness: `scripts/auto-growth-readiness-report.py`
- 검증: `scripts/verify-daily-growth-runner.py`, `scripts/verify-non-email-growth-loop.py`, `scripts/verify-pre-auto-growth-loop.py`, `scripts/verify-auto-growth-activation-policy.py`, `scripts/verify-auto-growth-readiness-report.py`
- 기본값: dry-run only. 자동 실행은 수동 성장/backlog 완료 전 금지한다.
- execute gate: `--execute`만으로는 실행되지 않는다. `--manual-growth-complete`가 필요하며, `--max-pending` 이하로 queue가 줄어야 한다.
- 출력 계획: 담당자별 daily regulatory case, source path, source hash, matched keywords, queue status, self docs, cadence.
- Honcho write record: `daily_growth_case` clean text message. JSON envelope 금지.
- metadata 계약: `record_type`, `actor`, `peer_id`, `profile_id`, `growth_version`, `run_date`, `scenario_id`, `source`, `source_hash`.
- source precision: 너무 넓은 `CE`, `US`, `KR`, `Korea` 단독 키워드는 daily case routing에서 제외한다. MDR/FDA/MFDS/KGMP처럼 신호가 강한 키워드를 우선한다.
- deriver 운영 조건: `DERIVER_FLUSH_ENABLED=true`가 필요하다. daily case는 보통 1024 token batch threshold보다 작으므로 flush가 꺼져 있으면 representation queue가 처리되지 않을 수 있다.
- 자동 timer 승격 조건: `pre-auto-growth-loop.py`가 local verifier, deriver flush, queue clean, daily runner idempotence, optional execute drain을 통과해야 한다. 일반 메일/Hermes 입력이 동시에 들어오는 시간에는 `--pending-scope ra`로 RA 담당자 큐를 strict gate로 두고 전체 pending은 감시값으로 분리한다.
- 성장 루틴: `non-email-growth-loop.py --cadence all` 기준 daily KB case, weekly source curriculum seed, monthly autonomous study delta dry-run, quarterly source coverage/freshness audit.
- 오염 판정: active growth record의 JSON envelope는 0이어야 한다. 과거 legacy test payload는 원본 백업 후 `metadata.quarantine_status=quarantined`로 표시하고 active gate에서 제외한다.
- timer 정책: `hermes-auto-growth.timer`는 운영 승인 후 매일 03:30 KST 실행한다. `auto-growth-runner.sh`는 `AUTO_GROWTH_OPERATION_TZ=Asia/Seoul` 기본값으로 운영일을 계산하고, daily KB growth를 idempotent execute하며, 월요일에는 curriculum seed도 idempotent execute한다.
- activation safety: `scripts/install-auto-growth-timer.sh`는 `--confirm-auto-growth-activation` 없이는 `--enable`/`--start-now`를 거부한다. timer unit은 `Persistent=false`로 missed-run 보상 실행을 차단한다.
- 2026-06-16 #57 보정 상태: 승인 없이 활성화된 timer는 stop/disable했으며, 현재 자동 실행 예약은 없다. 수동 readiness/service 실행은 가능하지만 운영 timer 승격은 승인 게이트 통과 후 별도 수행한다.
- 2026-06-16 #58 보정 상태: 운영 timer 승격 전 대기하지 않고 `auto-growth-readiness-report.py`와 non-email/pre-auto dry-run을 반복해 readiness matrix를 측정하고, 낮은 축은 별도 이슈로 fix한다.
- 2026-06-16 #60 보정 상태: `ra_kr` self-doc 균형을 638까지 보강해 `ra_kr >= int(ra_eu * 0.2)` 조건을 통과했다. 최종 readiness matrix는 16/16이고 pending/wrong-peer/live contamination은 0이다. 이 상태는 자동 timer 활성화가 아니라 운영 승인 검토 가능 상태다.

---

## Phase 3: 성장 루프 계장화

### P3.1 Layer 4 API → mail-triage 실시간 연동 `[구현]` (#37)

- n8n mail-triage에 Layer 4 조회 노드 추가 (규제권 분류 후, RA 호출 전)
  - US: openFDA API (product code, device class, 510k history)
  - KR: data.go.kr 품목허가 조회
- 조회 결과를 RA 에이전트 프롬프트에 컨텍스트로 주입
- 실패 시 graceful degradation (RA 호출은 계속)
- 캐싱: Redis (동일 product code 중복 조회 방지)

### P3.2 성장 트리거 자동화 `[구현 + IF]` (#38)

- systemd timer: `growth-metrics.timer` (일 1회 야간)
- 결과 저장: `logs/growth-metrics-YYYY-MM-DD.json`
- 트리거 임계값 설정: `feedback/config/growth-trigger-config.json` `[IF]`
- 트리거 달성 시 n8n webhook → 사람 알림 (자동 실행 아님)

---

## Phase 4: 인프라 투표 활성화

### P4.1 vote-rules.json 초기값 + 브로드캐스트 `[구현]` (#39)

- `voting/config/vote-rules.json` 초기값 채우기 (사람 결정 후)
- n8n 브로드캐스트 노드: 인프라 이상 감지 → vote-aggregator 호출 → 브릿지
- vote-aggregator.js: 외부 설정 파일 로드 검증
