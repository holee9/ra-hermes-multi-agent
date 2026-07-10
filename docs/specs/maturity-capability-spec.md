# SPEC — Maturity Capability (별 역량 다축 진화 + (c) KB 갭 탐지 루프 통합)

> **Document type**: 설계(PLAN) 전용 SPEC. 구현(Run phase)은 별도 사용자 승인 단계에서 진행.
> **Status**: PROPOSED — Phase 1(KB 갭 탐지 루프)과 Phase 2(별 다축 진화) 구현은 모두 GATE-3(사람 승인) 영역.
> **Date**: 2026-07-10.
> **Tracking issue**: #106 ([ENHANCEMENT][GROWTH-14] 별(maturity) 시스템 역량 기반 진화 + (c) KB 갭 탐지 루프 통합).

---

## 1. Overview / Problem

RA 전문가 에이전트(ra_us/ra_eu/ra_kr)의 성숙도를 표시하는 **별(★ 1~5)** 시스템은 현재 **학습량(volume) 단일 축**이다. ra_kr이 2026-07-09 누적 61 case로 최초 별5 달성했으나, 별이 volume만 반영하므로 KB(지식베이스) 확장·점프 시 의미가 퇴색한다.

사용자의 본래 목적은 **"부족한 부분을 사용자가 개선"** 루프다. 이 루프의 핵심이 **(c) KB 갭 탐지**이며, 갭 탐지가 생성하는 실측 데이터(정확도·커버리지)가 별 역량 진화의 입력이 된다. 본 SPEC은 이 둘을 통합 설계한다.

### 1.1 현재 별 시스템 (volume 단일 축)

- `virtual-office/virtual-office-honcho-adapter.js:156` `levelFromCount(count)` — 별 = 순수 `daily_growth_case` 누적 case 수.
- `virtual-office-honcho-adapter.js:152` `@MX:NOTE` — "star mapping uses daily_growth_case cumulative count (learning VOLUME only, not accuracy)".
- `virtual-office-honcho-adapter.js:167` `computeAgentLevels()` — `accuracy: 'pending'` 고정.
- 환산(균등형): 1~9→1, 10~19→2, 20~34→3, 35~59→4, 60+→5.

### 1.2 퇴색 경로 (3)

1. **절대 임계값 분해능 없음** — 60+가 전부 별5. 60·600·6000이 동일하게 보인다. KB가 10배 점프해도 별은 무반응.
2. **커버리지 역설** — KB가 확장되면 같은 case 수로 커버하는 영역 비율이 ↓ 하지만 별은 동일 → "별5인데 역량 밀도 ↓" 상태.
3. **정확도 축 부재** — 원래 학습량/정확도 2축 설계였으나 정확도는 `pending` (ra-advisory confidence는 raspi5p 무한 루프 오염으로 신뢰 불가, #69~72 사람 KB-eval 미도입).

### 1.3 핵심 통찰 — 갭 탐지 신호는 이미 존재한다

Phase 1(KB 갭 탐지)의 탐지 신호는 **이미 advisory 응답 경로에서 생성**되고 있다. 신규 추론을 만들 필요 없이 이 신호를 **로그로 수집·서피스**하면 된다.

- `scripts/hermes-api-server.py:411` `validate_advisory()` — confidence 위반·저신뢰도(< `LOW_CONF`)·evidence 부재 시 `yellow_review`로 분류하고 `yellow_reason` 부여.
- `scripts/hermes-api-server.py:559` `_yellow_advisory()` — `yellow_reason` ∈ {`low_confidence`, `no_evidence`, `invalid_confidence`}.
- advisory 응답 필드: `confidence`, `decision`, `evidence[]`, `yellow_reason`, `recommended_comment`, `summary`.

즉 **`decision == "yellow_review"` 또는 `evidence == []` 또는 `confidence < 임계값`** 인 응답이 곧 "이 주제는 KB 보완 필요" 갭 신호다. Phase 1은 이 신호를 포착해 갭 로그로 누적하는 것이다.

---

## 2. Scope

| Phase | 내용 | 산출 |
|-------|------|------|
| Phase 1 | (c) KB 갭 탐지 루프 — advisory yellow/no-evidence/low-confidence 신호를 갭 로그로 수집 → 대시보드 표시 → 사람 승인 | 갭 로그 + `/api/kb-gaps` + VO 갭 패널 |
| Phase 2 | 별 역량 다축 진화 — 학습량(현행) + 정확도(신규) + 커버리지(신규). KB 점프 시 별 재산정 | 다축 `computeAgentLevels` + VO 다축 표시 |

**In-scope:**
- Phase 1: 갭 신호 로깅, 갭 로그 저장, 서피스 엔드포인트, VO 패널, 사람 승인 표시 루프.
- Phase 2: 별 3축 정의, 결합/표시 방식, KB 점프 시 재산정 로직, 분해능 세분화.

**Out-of-scope (비범위):**
- 사람 KB-eval(#69~72) 데이터 생성 자체 — 별개 진행. 데이터가 들어오면 Phase 2 정확도 축 활성.
- 자동화 비중 확대 — GATE(Close/Reopen 영구 사람 전용) 유지.
- KB 저장소(llm-wiki/ra-project/MD-process) 쓰기 — 영구 읽기 전용(CLAUDE.md).
- ra-advisory confidence의 정확도 축 사용 — 오염된 신호이므로 영구 제외(REQ-MC-015).

---

## 3. Design Pillars

### 3.1 Phase 1이 선행하는 이유 (데이터 생성이 Phase 2 전제)

Phase 2의 정확도·커버리지 축은 **실측 데이터**를 필요로 한다. 현재 그 데이터가 없다(정확도 `pending`). Phase 1 갭 탐지 루프가 "어떤 주제가 부족한가" 실측 데이터를 생성하고, 이것이 커버리지 축의 입력이 된다. 정확도 축은 사람 KB-eval(#69~72)이 별개로 공급한다. 따라서 Phase 1 → Phase 2 순서가 자연스럽다.

### 3.2 갭 탐지는 신규 추론이 아니다 (로깅·서피스만)

`validate_advisory()`가 이미 갭 신호(yellow_reason, evidence 부재)를 분류한다. Phase 1은 이 분류 결과를 **갭 로그로 누적**하고 **사람이 볼 수 있게 서피스**하는 것이 전부다. advisory 추론 로직(`build_advisory_context`, `_invoke_llm_direct`)은 건드리지 않는다(#105 (b) 근본 fix 회귀 방지).

### 3.3 정확성 우선 — 별5는 "많이 학습"이지 "판단 신뢰"가 아니다

별은 **표시(display)** 장치다. 별5가 자동화 근거가 되면 안 된다. 설계 철학(CLAUDE.md "정확성·신뢰성 우선, 사람 보조") 준수: 별·갭 지표는 사람 판단을 **보조**하는 정보일 뿐, Close/Reopen·실행 결정의 근거가 될 수 없다(REQ-MC-012).

### 3.4 불확실하면 사람에게 — 갭 탐지는 표시만, 보완은 사람 승인

KB 갭이 탐지되면 "이 주제 KB 보완 필요"로 **표시**만 한다. KB 실제 보완(원격 repo 편집)은 사람이 한다. 에이전트·시스템은 KB repo에 쓰지 않는다(영구 제약, REQ-MC-014).

### 3.5 임계값은 하드코딩하지 않는다 ([IF] 원칙)

갭 탐지 임계값(confidence 커트오프, dedup 윈도우, 커버리지 정규화 기준 도메인 수)은 외부 설정에서 읽는다. 운영자가 런타임에 튜닝할 수 있도록 `[IF]` 마커를 따른다(implementation-spec.md "Implementation Maturity Markers").

---

## 4. Requirements (EARS format)

> 각 요구사항은 EARS 문법을 따른다. ID는 세션 간 안정적. Phase 표기 명시.

### REQ-MC-001 (Phase 1 — 갭 신호 포착)

**WHEN** `/v1/ra/advisory` 응답이 `decision == "yellow_review"` 이거나 `evidence == []` 이거나 `confidence < GAP_CONF_THRESHOLD` 일 때, **THE SYSTEM SHALL** 해당 응답을 KB 갭 후보로 식별하여 갭 로그에 기록한다.

- 갭 신호 원천: `validate_advisory()`(`hermes-api-server.py:411`)의 `yellow_reason` + `evidence` + `confidence`.
- `GAP_CONF_THRESHOLD` = 외부 설정([IF]). 기본값은 `LOW_CONF`와 정합.

### REQ-MC-002 (Phase 1 — 갭 로그 저장)

**THE SYSTEM SHALL** 갭 후보를 {actor, region, 주제 요약, yellow_reason, confidence, 발생 시각, source_query} 구조로 영속 저장한다.

- 저장소 = **설계 결정 대상(OD-1)**: (a) Honcho 전용 세션 `ra_kb_gaps`, (b) JSONL 파일, (c) DB 테이블. 본 SPEC은 선택하지 않는다(Run phase 결정).

### REQ-MC-003 (Phase 1 — 대시보드 서피스)

**THE SYSTEM SHALL** 갭 로그를 조회하는 `/api/kb-gaps` 엔드포인트를 신설하고, VO(virtual-office)에 KB 갭 패널을 추가하여 사람이 부족 주제를 한눈에 보게 한다.

- `/api/kb-gaps`는 기존 `/api/agent-levels`(`adapter.js:559`) 패턴(읽기 전용, 캐시 optional)을 따른다.
- VO 패널은 읽기 전용(관측자 모델 준수).

### REQ-MC-004 (Phase 1 — 사람 승인 루프 표시)

**WHEN** 갭이 서피스되면, **THE SYSTEM SHALL** 갭 상태를 {탐지됨 → 사람 검토 중 → KB 보완 완료}로 표시하되, 상태 전환의 실행(실제 KB 편집)은 사람 영역으로 둔다.

- 에이전트·시스템은 KB repo에 쓰지 않는다(REQ-MC-014). 루프는 "표시 + 사람 액션 대기"만.

### REQ-MC-005 (Phase 1 — 멱등·중복 억제)

**WHEN** 같은 주제의 갭 신호가 `GAP_DEDUP_WINDOW` 내 반복 발생하면, **THE SYSTEM SHALL** 동일 갭으로 병합하여 1건으로 표시한다(로그 폭증 방지).

- 근거: VO events 폭증 교훈(`adapter.js` `dedupeForDisplay` 5분 윈도우 — raspi5p 루프 산물 8511→1117건 압축).
- `GAP_DEDUP_WINDOW` = 외부 설정([IF]).

### REQ-MC-006 (Phase 2 — 학습량 축 유지)

**THE SYSTEM SHALL** 학습량 축을 현행 `daily_growth_case` 누적(`levelFromCount`)으로 유지한다(회귀 최소화).

### REQ-MC-007 (Phase 2 — 정확도 축)

**WHEN** 사람 KB-eval(#69~72) 데이터가 존재할 때, **THE SYSTEM SHALL** 정확도 축을 활성화한다. 데이터가 없으면 `pending`을 유지한다.

- 정확도 축 입력: KB-eval 점수 + Phase 1 갭 적중/미적중(갭이 탐지된 주제를 사람이 보완 후 재자문 시 해소 여부).
- ra-advisory confidence는 정확도 축에 사용 금지(REQ-MC-015).

### REQ-MC-008 (Phase 2 — 커버리지 축 + KB 점프 재산정)

**THE SYSTEM SHALL** 커버리지 축을 (학습 case 수 / KB 도메인 수) 정규화로 정의하고, KB 규모가 변하면(점프 시) 별을 재산정하여 인플레를 방지한다.

- 도메인 수 산정 기준 = **설계 결정 대상(OD-2)**: ra_knowledge 청크 수·메타데이터 도메인 태그·커리큘럼 시드 카테고리 중 무엇을 기준으로 할지.
- 재산정 트리거: `index_github_repos.py` 인덱싱 후 KB 규모 변동 감지 시(kb-rag-sync Phase 1 연관, #107).

### REQ-MC-009 (Phase 2 — 다축 결합/표시)

**THE SYSTEM SHALL** 3축(학습량/정확도/커버리지)을 결합하여 별에 반영하거나 축별로 별도 표시한다.

- 결합 방식 = **설계 결정 대상(OD-3)**: (a) 가중합 단일 별, (b) 축별 다중 표시(★학습 / ◆정확 / ▲커버), (c) 혼합.

### REQ-MC-010 (Phase 2 — 분해능 세분화)

**THE SYSTEM SHALL** 별5 내부를 세분화(5.0~5.9)하거나 마일스톤(100/200/500 case)으로 표시하여, 60+ 전부 동일 별5인 분해능 부재(퇴색 경로 1)를 해소한다.

### REQ-MC-011 (GATE-3 — 사람 승인 없이 실행 금지)

**THE SYSTEM SHALL NOT** Phase 1 갭 로깅 훅(advisory 경로 변경) 또는 Phase 2 별 진화 구현을 사용자 명시적 승인 없이 실행한다.

- Phase 1 중 `hermes-api-server.py` advisory 경로 변경 = production(`/opt/hermes-ra/`) = GATE-3(#105 (a)(b) 배포 이력).
- VO/adapter.js 변경은 Docker rebuild 수반 → 배포 액션.

### REQ-MC-012 (자동화 근거 사용 금지 — GATE 준수)

**THE SYSTEM SHALL NOT** 별 등급이나 KB 갭 지표를 WP Close/Reopen 또는 advisory 자동 실행 결정의 근거로 사용한다.

- 별·갭은 표시·관측 전용. CLAUDE.md Gate Rules(Close/Reopen = 영구 사람 전용) 준수.

### REQ-MC-013 (회귀 보호)

**THE SYSTEM SHALL** Phase 1/2 구현 후 기존 별 표시·VO 동작·advisory 응답 Contract C에 회귀가 없음을 라이브 e2e로 검증한다.

- 근거: #105 교훈 — 단발 테스트만 믿고 "PASS" 선언 후 라이브 회귀 발견. `advisory-chat-channel-spec.md` "Phase 1 Implementation Log" 참조.

### REQ-MC-014 (KB 저장소 읽기 전용 — 영구 제약)

**THE SYSTEM SHALL NOT** 갭 탐지·보완 제안 과정에서 llm-wiki/ra-project/MD-process 저장소에 쓰기/푸시/업로드한다.

- CLAUDE.md "Knowledge bases are completely read-only" 영구 제약. 갭 "보완 완료" 표시는 사람이 외부에서 편집했음을 기록만 한다.

### REQ-MC-015 (정확도 축 데이터 신뢰 — ra-advisory confidence 제외)

**THE SYSTEM SHALL NOT** ra-advisory confidence 값을 정확도 축의 신뢰 가능한 입력으로 사용한다.

- 근거: `adapter.js:565` `accuracy_status` — raspi5p 무한 루프가 ra-advisory confidence를 오염(ra_kr conf 0.01 등). 정확도 축은 사람 KB-eval(#69~72)만 허용.

---

## 5. Acceptance Criteria (Definition of Done)

### Phase 1

| ID | Given / When / Then | 검증 |
|----|---------------------|------|
| AC-P1-1 | **Given** advisory 엔드포인트, **When** no-evidence/low-confidence 응답 발생, **Then** 갭 로그에 1건 기록 | 단위 + 라이브 e2e(`/v1/ra/advisory` 호출 후 갭 로그 확인) |
| AC-P1-2 | **Given** 갭 로그 누적, **When** `/api/kb-gaps` 호출, **Then** 갭 목록 JSON 반환 | 엔드포인트 직접 호출 |
| AC-P1-3 | **Given** VO 로드, **When** 갭 존재, **Then** 갭 패널에 주제 표시 | chromium DOM 검증(기존 VO e2e 패턴) |
| AC-P1-4 | **Given** 동일 주제 갭 반복, **When** `GAP_DEDUP_WINDOW` 내, **Then** 1건으로 병합 | 단위(dedup 로직) |
| AC-P1-5 | **Given** Phase 1 배포, **When** 기존 advisory/VO 동작, **Then** 회귀 없음 | 라이브 e2e(REQ-MC-013) |

### Phase 2 (정확도 축 데이터(#69~72) + OD-1/2/3 결정 이후)

| ID | Given / When / Then | 검증 |
|----|---------------------|------|
| AC-P2-1 | **Given** 학습량 축, **When** case 누적, **Then** 현행 별 환산 유지(회귀 0) | 단위 |
| AC-P2-2 | **Given** KB-eval 데이터 존재, **When** 정확도 축 활성, **Then** 축 값 표시 | 단위 + VO |
| AC-P2-3 | **Given** KB 점프, **When** 커버리지 재산정, **Then** 별 인플레 미발생 | 단위(재산정 로직) |
| AC-P2-4 | **Given** OD-2(커버리지 기준)/OD-3(결합 방식) 설계 결정 완료 + #69~72 정확도 데이터 대기 상태 해소, **When** Phase 2 Run 진입 전, **Then** 결정이 문서화되어 있음 | 설계 결정 기록(#106 코멘트 또는 본 SPEC 개정). OD-1(갭 로그 저장소)은 Phase 1 전제이므로 제외. |

---

## 6. Delta Markers (Brownfield)

| 파일 | 마커 | 비고 |
|------|------|------|
| `scripts/hermes-api-server.py` advisory 경로 (`validate_advisory:411` / `_yellow_advisory:559`) | **[MODIFY]** (Phase 1) | 갭 신호 포착 훅. **production(`/opt/hermes-ra/`) = GATE-3**(REQ-MC-011). `_invoke_llm_direct`/`build_advisory_context` 미접촉(#105 회귀 방지). |
| `virtual-office/virtual-office-honcho-adapter.js` `levelFromCount:156` / `computeAgentLevels:167` / `/api/agent-levels:559` | **[MODIFY]** (Phase 2) | 다축 진화. 기존 volume 축 유지(REQ-MC-006). |
| `virtual-office/virtual-office-honcho-adapter.js` `/api/kb-gaps` | **[NEW]** (Phase 1) | 갭 로그 서피스 엔드포인트. `/api/agent-levels` 패턴. |
| `virtual-office/virtual-office.html` | **[MODIFY]** (Phase 1 갭 패널 + Phase 2 다축 표시) | 읽기 전용 패널. RA 3종 캐릭터 영역. |
| KB 갭 저장소 | **[NEW]** (Phase 1) | 저장소 결정 = OD-1. |
| 임계값 설정(`GAP_CONF_THRESHOLD`, `GAP_DEDUP_WINDOW`, 커버리지 기준) | **[NEW config]** | [IF] — 외부 설정, 런타임 튜닝. 하드코딩 금지. |

---

## 7. Exclusions (What NOT to Build)

> [HARD] 본 SPEC은 아래를 명시적으로 제외한다.

1. **사람 KB-eval(#69~72) 평가 데이터 생성** — 별개 사람 행동. 데이터가 들어오면 Phase 2 정확도 축 활성(REQ-MC-007).
2. **자동화 비중 확대** — Close/Reopen 영구 사람 전용 유지(REQ-MC-012).
3. **KB 저장소 쓰기** — 영구 읽기 전용(REQ-MC-014).
4. **ra-advisory confidence의 정확도 축 사용** — 오염 신호 영구 제외(REQ-MC-015).
5. **advisory 추론 로직(`build_advisory_context`, `_invoke_llm_direct`) 변경** — #105 (b) 근본 fix 회귀 방지. Phase 1은 분류 결과만 소비.
6. **Phase 1/2 구현 코드** — 본 문서는 설계(PLAN). 구현은 `/moai run` 별도 단계(Section 9).

---

## 8. Related Issues

| 이슈 | 관계 | 비고 |
|------|------|------|
| **#106** | 추적 이슈 | 본 SPEC의 tracking issue. |
| **#104** | 입력 채널 | VO 자문 채널 — 갭 탐지 입력. (a)+(b) 해결, Phase 1 코드 완료. |
| **#69 #70 #71 #72** | 데이터 의존 | KB Eval — 정확도 축 데이터. 사람 행동(비범위). |
| **#65** | 연관 | MONITOR-2 자동 성장 임계값 — 별 진화와 임계값 정책 연계 가능. |
| **#88** (CLOSED) | 패턴 참고 | unclear_region 군집 — 갭 신호 패턴 참고. |
| **#107** | KB layer 연관 | kb-rag-sync Phase 1(pgvector 최신화) — 커버리지 축 KB 규모 산정과 연관. |

---

## 9. Implementation Separation Note

> **본 SPEC은 설계(PLAN phase) 전용이다.**

- 본 SPEC의 존재가 실행 허가가 아니다.
- Phase 1(`hermes-api-server.py` advisory 경로 + adapter.js + VO)과 Phase 2(별 진화) 구현은 모두 GATE-3(REQ-MC-011).
- Phase 2는 OD-1/2/3(저장소/커버리지 기준/결합 방식) 설계 결정이 해결되기 전까지 Run 진입 불가(AC-P2-4).
- 정확도 축(REQ-MC-007)은 #69~72 데이터가 공급되기 전까지 `pending`.

### 구현 순서 (사용자 승인 후)

- **Phase 1 준비**: OD-1(갭 로그 저장소) 결정 → 갭 신호 포착 훅 설계 상세 → 사용자 승인.
- **Phase 1 실행** (승인 후 `/moai run`): advisory 갭 로깅 + `/api/kb-gaps` + VO 패널 + AC-P1-1~P1-5 라이브 e2e.
- **Phase 2 준비**: OD-2(커버리지 기준)/OD-3(결합 방식) 결정 + #69~72 데이터 대기 → 사용자 승인.
- **Phase 2 실행**: 다축 `computeAgentLevels` + KB 점프 재산정 + AC-P2-1~P2-4.

---

## Annex A — Open Design Decisions (OD)

본 SPEC이 결정하지 않고 Run phase로 연기하는 설계 결정:

| OD | 결정 사항 | 후보 |
|----|-----------|------|
| **OD-1** | KB 갭 로그 저장소 | (a) Honcho 세션 `ra_kb_gaps` / (b) JSONL 파일 / (c) DB 테이블 |
| **OD-2** | 커버리지 축의 "KB 도메인 수" 산정 기준 | ra_knowledge 청크 수 / 메타데이터 도메인 태그 / 커리큘럼 시드 카테고리 |
| **OD-3** | 3축 결합/표시 방식 | (a) 가중합 단일 별 / (b) 축별 다중 표시 / (c) 혼합 |

> OD는 코드-전( 코드 작성 전) 결정이 아니다 — 일부는 Phase 1/2 Run 진입 시점에, 실측 데이터를 보며 결정하는 것이 합리적이다(OD-2는 KB 규모 실측, OD-3은 사용자 UX 선호). 다만 OD-1은 Phase 1 착수 전 결정 필요.

### OD 결정 (2026-07-10, Phase 1/2 Run 진행 시점 — 실측 데이터 기반)

사용자 승인 하 Phase 1/2 Run을 진행하며 DB 실측 데이터를 보아 3개 OD를 확정했다.

| OD | 결정 | 근거 |
|----|------|------|
| **OD-1** | **(b) JSONL 파일** `reports/kb-gaps/kb-gaps.jsonl` | 기존 `reports/` 패턴 일관, append-only 이벤트 로그에 자연스러움, DB 스키마 추가 회피(GATE-3 영향 최소). Phase 1 구현 완료(`hermes-api-server.py:_log_kb_gap` + adapter `/api/kb-gaps`). |
| **OD-2** | **agent별 고유 학습 source 수 / KB 총 source 수**(정규화 비율) | DB 검증: `daily_growth_case` metadata `source` 100% 채워짐(ra_us 59/59·ra_eu 59/59·ra_kr 64/64). distinct source = **ra_us 22·ra_eu 17·ra_kr 17**. coverage = distinct growth source / `KB_TOTAL_SOURCES`([IF] env, 기본 1493). 청크 수가 아닌 **source(파일) 단위** — 학습 다양성이 volume(누적 case)과 직교하는 진짜 제2의 축. |
| **OD-3** | **(b) 축별 다중 표시** — ★ volume(현행·회귀 0) + `coverage_sources`/`coverage_pct` 보조 + accuracy pending | 정확도 축 데이터(#69~72) 미확보 상태에서 가중합은 의미 없음. volume 별은 `levelFromCount` 유지(REQ-MC-006 회귀=0, 단위 테스트 PASS), coverage는 표시용 보조 축. KB 점프 시 `KB_TOTAL_SOURCES` 갱신 → coverage_pct 재산정(REQ-MC-008 인플레 방지). |

> 정확도 축(REQ-MC-007)은 여전 `pending` — 사람 KB-eval(#69~72) 데이터에 의존하므로 본 Run에서는 활성하지 않는다. coverage 축은 메타데이터 기반으로 **지금 즉시 측정 가능**하여 활성했다(AC-P2-1 volume 회귀=0 / AC-P2-3 재산정 로직 단위 검증 / AC-P2-4 OD 문서화 충족).

---

## Annex B — Cross-reference Index

| 개념 | 위치 |
|------|------|
| 별 volume 단일 축 (현행) | `virtual-office-honcho-adapter.js:152,156,167` |
| `/api/agent-levels` 엔드포인트 | `virtual-office-honcho-adapter.js:559` |
| advisory 갭 신호 원천 | `hermes-api-server.py:411 validate_advisory`, `:559 _yellow_advisory` |
| accuracy pending 사유 (raspi5p 오염) | `virtual-office-honcho-adapter.js:565` |
| #105 라이브 e2e 교훈 | `docs/specs/advisory-chat-channel-spec.md` "Phase 1 Implementation Log" |
| KB 읽기 전용 영구 제약 | `CLAUDE.md` "Ecosystem Position" |
| [IF] 임계값 원칙 | `docs/implementation-spec.md` "Implementation Maturity Markers" |

---

Version: 1.0.0
Classification: PROPOSED (PLAN-phase design only)
Date: 2026-07-10
Tracking issue: #106
Related: #104 #69 #70 #71 #72 #65 #88 #107
