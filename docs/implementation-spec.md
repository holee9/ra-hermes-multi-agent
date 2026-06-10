# 구현 명세서 (Implementation Spec)

> **대상 독자: AI 코딩 툴(Claude Code CLI / Codex CLI 등) 및 구현 담당.** 툴 중립.
> **원칙**: 인터페이스는 엄격히 고정, 내부 구현은 위임. 이 시스템은 *학습하며 성장*하므로, 평가로 수렴할 규칙(투표·가중치·임계)은 **의도적 공백**으로 둔다 — 미결이 아니라 설계다. 그 부분은 인터페이스만 만들고 내부는 운영·학습이 채운다.
> **정확성 우선 원칙**: 의료기기 인허가 도메인에서 속도보다 정확성이 항상 우선한다. **Cold start(임계값 미설정) 상태에서는 모든 판단을 Yellow 게이트(사람 확인)로 처리한다.** 자동 처리 비중은 학습·평가 누적 이후에만 단계적으로 확대한다.
> **성숙도 표기**: `[구현]` 코딩 가능 깊이로 명세 / `[IF]` 인터페이스만 — 내부는 PoC·학습이 채움(임의 구현 금지, 비워두거나 사람에게 질의).
> 사실 기준일 2026-06-05. 상세 설계 근거는 RA-multi-agent-master-design.md 참조.

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

### 2.3 mail-triage 워크플로우 (n8n) `[구현]`
입력: 재전송 Gmail. 출력: OpenProject WP 코멘트/생성 + Honcho conclusion 기록.
- **본문 파싱** `[구현]`: 재전송 본문에서 원 제목·원 발신자·사안 식별자 추출 → 정규화 매칭 키. (헤더는 재전송으로 파괴됨 → 본문 기반)
- **규제권 라우팅** `[구현]`: 본문의 규제기관(FDA/MDR/MFDS)·제출 종류 → ra_us|ra_eu|ra_kr 결정. 판별 불가 시 사람 질의(Yellow).
- **RA 호출** `[구현]`: 해당 프로파일을 Hermes `/v1/chat/completions`(또는 게이트웨이)로 호출, 분석 결과 수신.
- **WP 반영** `[구현]`: 미완료 WP(오픈·진행중·리뷰중) 매칭 시 코멘트 추가, 미매칭 시 WP 생성. (n8n OpenProject 커뮤니티 노드 또는 OpenProject MCP 서버 — create_work_package / add_comment / update_work_package_status / get_statuses)
- **기록** `[구현]`: 사안↔WP 매핑을 Honcho conclusion으로 기록(다음 회차 매칭에 사용).
- **게이트** `[구현]`: 매칭·코멘트=자율(Green). 상태 전이 제안=Yellow(사람 확정). 완료=사람 전용(불변, 코드로 차단).

#### mail-triage 데이터 계약 (입출력 고정)
RA 분석 결과 JSON(고정):
```json
{ "actor":"ra_us", "wp":"WP-123|null", "match":"existing|new",
  "confidence":0.0-1.0, "region":"US|EU|KR",
  "comment":"...", "transition_proposed":"리뷰중|null" }
```

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
- 역할: HWP/DOCX/PDF/PPTX/XLS 원본 → Markdown 변환 → llm-wiki(가로획 토대)에 공급. 새 조각 아닌 **llm-wiki 입력 단계**.
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
2. `[구현]` 재전송 메일 → ra_us 분석 → 미완료 WP 코멘트 / 신규 WP 생성 → Honcho 기록.
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
