# SPEC — KB RAG Sync (ra-project/MD-process/llm-wiki 단절 해결 + 정기 동기화 파이프라인)

> **Document type**: 설계(PLAN) 전용 SPEC. 구현(Run phase)은 별도 사용자 승인 단계에서 진행.
> **Status**: **Phase 1 IMPLEMENTED (2026-07-10, GATE-3 승인 받아 실행)** — 2/3 KB(MD-process·ra-project) 정기 동기화 확립. Phase 2 RAG 전환은 여전 PROPOSED(DEFERRED). ⚠️ llm-wiki는 인덱서 페이지네이션 한계로 미완(신규 이슈, Annex C 참조).
> **Date**: 2026-07-10.
> **Tracking issue**: #107 ([MONITOR-6] pgvector ra_knowledge 정기 인덱싱 스케줄 부재).

---

## 1. Overview / Problem

사용자 점검 요청(2026-07-10): "지식베이스들이 진전되었는데, 원격 저장소 내용과 정기 동기화하고 있는지 점검" (#107).

점검 결과, 세 원격 KB 저장소(ra-project, MD-process, llm-wiki)의 markdown 내용은 **에이전트의 RAG 경로와 구조적으로 단절**되어 있다. 이 단절은 두 가지 독립적인 결함의 합이다.

### 1.1 에이전트의 실제 RAG 경로 (Layer 매핑)

`scripts/hermes-api-server.py`가 사용하는 지식 검색 경로는 두 개다:

| Layer | 함수 | 스크립트 | 데이터 소스 | 동기화 상태 |
|---|---|---|---|---|
| **Layer 1 (RAG)** | `_run_rag_search` (`hermes-api-server.py:138-160`) | `RAG_SCRIPT = /opt/hermes-ra/skills/ra-expert/scripts/rag_search.py` (`hermes-api-server.py:119`) | **Qdrant collection `nas_ra_docs`** (2,094,439 points, size 4096, Cosine) | 매일 02:00 `nas_indexer.py`가 NAS 파일시스템 `/mnt/nas-ra/...`만 스캔. 세 git repo는 스캔 대상 아님 |
| **Layer 4 (실시간)** | `_run_knowledge_fetch` (`hermes-api-server.py:163-179`) | `KNOWLEDGE_SCRIPT = /opt/hermes-ra/scripts/knowledge_fetch.py` (`hermes-api-server.py:127`) | llm-wiki (Gitea realtime API) + openFDA + law.go.kr | 실시간 API 호출 (정상) |

> **핵심**: Layer 1 RAG는 **Qdrant `nas_ra_docs`만 읽는다**. pgvector `ra_knowledge`를 읽는 코드가 `hermes-api-server.py`에 **한 줄도 없다** (grep 검증 완료).

### 1.2 세 저장소의 단절 메커니즘

세 git repo의 markdown은 `scripts/index_github_repos.py`에 의해 pgvector `ra_knowledge`에 인덱싱된다 (9,272 rows: MD-process 3,530 / ra-project 3,106 / llm-wiki 2,636). 그러나:

**결함 A — 정기 스케줄 부재**:
- `index_github_repos.py`에는 cron/timer/systemd 어떤 것도 등록되어 있지 않다.
- 유일한 실행일자: 2026-06-11 (~30일 정체).
- ra-project 최신 커밋 07-06, MD-process 최신 커밋 07-10(오늘) → pgvector에 미반영.
- abyz-lab crontab 현황: `07:00 ra-project git pull`, `07:05 MD-process git pull`, `02:00 nas_indexer.py → Qdrant`. **`index_github_repos.py` 항목 없음** (#107 확인).

**결함 B — RAG 전환 미완료**:
- RAG(Layer 1)는 Qdrant `nas_ra_docs`를 읽지, pgvector `ra_knowledge`를 읽지 않는다.
- 이는 #17(Qdrant→pgvector 마이그레이션)의 미완료된 절반이다: 인덱서 포팅은 완료, RAG 전환은 미수행.

### 1.3 결과

| 저장소 | 에이전트 도달 여부 | 경로 |
|---|---|---|
| ra-project (GitHub) | **완전 단절** | pgvector에 6/11 스냅샷만 존재 + RAG가 pgvector 미참조 |
| MD-process (GitHub) | **완전 단절** | 동일 |
| llm-wiki (Gitea) | Layer 4 실시간 API로만 생존 | pgvector에는 있으나 RAG 미참조; Layer4가 우회 지원 |

---

## 2. Scope

| Dimension | In Scope | Out of Scope |
|---|---|---|
| 대상 저장소 | ra-project, MD-process (GitHub), llm-wiki (Gitea) — 읽기 전용 | 기타 NAS 파일시스템 문서 (기존 `nas_indexer.py` 담당) |
| Phase 1 | `index_github_repos.py` 정기 cron 스케줄 신설 + pgvector `ra_knowledge` 신선도 관측 | RAG 경로 변경 없음 (Phase 1만으로는 에이전트 도달 안 됨 — 사전 정지작업 성격) |
| Phase 2 | Layer 1 RAG를 Qdrant `nas_ra_docs` 단일 → pgvector `ra_knowledge` 포함 경로로 전환 | 전환 상세 설계는 본 SPEC에서 **DEFERRED** (Section 4.3) |
| 쓰기 권한 | GitHub/Gitea API **읽기 전용** (인덱싱만) | KB repo 쓰기/push/upload — **영구 금지** (CLAUDE.md:176, :206-210) |
| 인덱싱 대상 | `.md` 파일 (markdown) | xlsx/pptx — `hermes-indexer.service`(`index_ra_knowledge.py`) 별건, 본 SPEC 범위 외 |
| 스케줄러 | 기존 crontab (abyz-lab 계정) | systemd timer 신설, k8s cronjob |

**명시적 제외**:
- KB repo 쓰기 — 영구 금지 (CLAUDE.md:176).
- Qdrant `nas_ra_docs` 2,094,439 points의 pgvector 마이그레이션 — Phase 2 DEFERRED (Section 4.3).
- `hermes-indexer.service` (xlsx/pptx 인덱서, `index_ra_knowledge.py`) 활성화 여부 — 별건 (#107 권장 2).

---

## 3. Design Pillars (Hybrid Phased 전략)

사용자 승인(2026-07-10)된 전략: **Hybrid Phased**. 위험도가 다른 두 결함을 분리하여, 안전한 것부터 순차적으로 적용한다.

### 3.1 Phase 1이 안전하고 선행되는 이유

Phase 1은 `index_github_repos.py`를 정기 cron으로 실행하여 pgvector `ra_knowledge`를 최신 상태로 유지하는 것이다.

- **기존 코드 변경 없음**: `index_github_repos.py`는 이미 2026-06-11에 정상 동작하여 9,272건을 인덱싱한 검증된 스크립트. cron 항목 추가만으로 완료.
- **멱등성 보장**: SHA 기반 증분 동기화(`index_github_repos.py:467-468` GitHub, `:573-574` Gitea) — 변경 없으면 "No changes since last run (sha=...), skipping" 로그만 남기고 종료. 반복 실행 안전.
- **에이전트 무영향**: Phase 1만으로는 RAG 경로가 바뀌지 않으므로, 잘못되어도 에이전트 품질에 영향 없음. 최악의 경우 pgvector가 비대해지는 것뿐.
- **필수 선행 조건**: Phase 2(RAG 전환) 전에 pgvector가 최신이어야 한다. 정체된 pgvector로 전환하면 에이전트가 30일 된 지식만 보게 됨.

### 3.2 Phase 2가 별도 라이브 검증을 필요로 하는 이유

Phase 2는 Layer 1 RAG 조회 경로를 Qdrant → pgvector로 전환하는 것이다.

- **에이전트 직격**: RAG 경로는 모든 advisory/email triage의 지식 근거. 잘못 전환하면 전 서비스 품질 저하.
- **#105 교훈**: advisory SPEC에서 코드만 검증하고 "PASS" 선언했다가, 라이브 서버 배포 후 회귀 발견(`advisory-chat-channel-spec.md` Phase 1 Implementation Log 참조). 라이브 e2e 없는 완료 선언은 금지.
- **2,094,439 vs 9,272 데이터 손실 위험**: 단순히 pgvector만 읽도록 바꾸면 NAS 문서 2.09M건이 증발. 이 결정은 충분한 설계 검토 없이 진행하면 안 됨 (Section 4.3 DEFERRED).

### 3.3 왜 한 번에 안 하는가

두 결함(A: 스케줄, B: 전환)을 한 번에 처리하면:
- 변경 범위가 커져 리스크 집중
- Phase 1만으로도 가치가 있음(운영 가시성, 정체 해소)
- Phase 2 설계(nas_ra_docs 처리)는 별도 브레인스토밍이 필요

분리는 위험 관리다.

---

## 4. Requirements (EARS format)

> 각 요구사항은 EARS 문법을 따른다. ID는 세션 간 안정적. Phase 1/Phase 2 표기 명시.

### REQ-KBS-001 (Phase 1 — 정기 cron 스케줄 신설)
**WHEN** 매일 정해진 시각(cron), **THE SYSTEM SHALL** `scripts/index_github_repos.py`를 무인수(one-shot incremental) 모드로 실행하여 GitHub(`holee9/MD-process`, `holee9/ra-project`) 및 Gitea(`DR_RnD/ra-llm-wiki`)의 `.md` 파일을 pgvector `ra_knowledge`에 동기화한다.

- 인터페이스: `index_github_repos.py:37`(`REPOS`), `:52`(`GITEA_REPOS`), `:41`(`TABLE="ra_knowledge"`).
- 실행 빈도: 매일 1회 (권장 04:00 — 기존 `02:00 nas_indexer.py`와 `07:00/07:05 git pull` 사이. 정확한 시각은 Run phase에서 `scripts/.env`와 조정).
- 환경변수: `POSTGRES_URL`(`:39`), `GITHUB_PAT`/`GITHUB_TOKEN`(`:38`), `GITEA_URL`/`GITEA_TOKEN`(`:50-51`), `OLLAMA_URL`(`:40`), `EMBED_MODEL`(`:42`).

### REQ-KBS-002 (Phase 1 — 멱등성 보장)
**THE SYSTEM SHALL** 동일한 HEAD SHA에 대해 재실행 시 쓰기를 수행하지 않고 skip 로그만 남긴다.

- 근거: `index_github_repos.py:467-468`(GitHub) — `state.get(repo) == head_sha` 시 "No changes since last run (sha=...), skipping"; `:573-574`(Gitea) 동일 패턴; 파일 단위 `pgvector_source_exists()`(`:517`) skip.
- 상태 파일: `/tmp/github_index_state.json`(`:44`). cron 반복 실행 안전.

### REQ-KBS-003 (Phase 1 — pgvector ra_knowledge 신선도 관측)
**THE SYSTEM SHALL** pgvector `ra_knowledge`의 최신 `indexed_at`을 조회 가능한 관측 지점을 제공한다.

- `indexed_at`은 UTC ISO-8601로 각 row에 기록됨: `index_github_repos.py:530, 549`(`indexed_at = datetime.now(timezone.utc).isoformat()`).
- 관측 방식(Run phase 결정): (a) cron 실행 후 stdout을 로그 파일로 리다이렉트하여 마지막 실행 시각/처리 건수 확인, 또는 (b) 간단한 psql 쿼리 `SELECT MAX(indexed_at) FROM ra_knowledge;`를 모니터링 스크립트에 추가.
- 목표: cron 실행 후 `MAX(indexed_at)`이 24시간 이내.

### REQ-KBS-004 (Phase 2 — RAG Layer 1 전환, DEFERRED 상세 설계)
**WHEN** Phase 1이 안정적으로 운영 중일 때, **THE SYSTEM SHALL** Layer 1 RAG(`hermes-api-server.py:138-160`, `_run_rag_search`)의 조회 대상을 Qdrant `nas_ra_docs` 단일 → pgvector `ra_knowledge` 포함 경로로 전환하여, ra-project/MD-process markdown이 에이전트에 도달하도록 한다.

- 현재 전환 표면: `hermes-api-server.py:119`(`RAG_SCRIPT`), `:120`(`QDRANT_URL`), `:144`(subprocess call to `RAG_SCRIPT`).
- 대상 스크립트(서버): `/opt/hermes-ra/skills/ra-expert/scripts/rag_search.py` — `DEFAULT_COLLECTION="nas_ra_docs"`, embed via `OLLAMA_URL /api/embed`(`qwen3-embedding:latest`), Qdrant `/collections/{collection}/points/search`.

> **⚠️ DEFERRED 설계 결정 (REQ-KBS-004a — 본 SPEC에서 결정하지 않음)**:
>
> 전환 시 아래 딜레마를 반드시 해결해야 한다:
> - Qdrant `nas_ra_docs` = **2,094,439 points** (NAS 문서). pgvector `ra_knowledge` = **9,272 rows** (세 git repo markdown).
> - 임베딩 호환: 동일 모델(`qwen3-embedding:latest`), 동일 차원(4096), 동일 거리(Cosine). 벡터 자체는 호환.
> - **그러나** 단순히 pgvector만 읽도록 바꾸면 NAS 문서 2.09M건이 사라진다.
>
> 후보 (Phase 2 Run phase에서 별도 설계):
> - **(a)** Qdrant `nas_ra_docs` 전량을 pgvector로 마이그레이션 → 단일 소스. 대규모 이관 + 성능 검증 필요.
> - **(b)** 하이브리드 조회 (Qdrant `nas_ra_docs` + pgvector `ra_knowledge` 병렬 검색 후 결과 병합) → 복잡도 증가, 두 소스 일관성 관리.
> - **(c)** 그 외 Run phase에서 제안 가능.
>
> **본 SPEC은 (a)/(b)/(c) 중 어느 것도 선택하지 않는다.** Phase 2는 별도 설계 세션에서 이 결정을 내린 후 Run phase로 진입한다.

### REQ-KBS-005 (Phase 2 — 라이브 e2e 검증 필수)
**THE SYSTEM SHALL NOT** Phase 2 RAG 전환을 "완료"로 선언하기 위해 단위 테스트만으로 충족한다. 반드시 실서버(T3610 `/opt/hermes-ra/`)에서 라이브 e2e 검증을 수행해야 한다.

- 검증 시나리오: ra-project 또는 MD-process에만 존재하는 내용(예: 특정 문서 구문)을 쿼리하여 해당 출처가 evidence로 반환되는지 확인.
- 근거: #105 교훈 — `advisory-chat-channel-spec.md` "Phase 1 Implementation Log"에서 코드 검증 PASS 선언 후 라이브 배포에서 회귀 발견, 롤백 수순. "직접 단발 테스트는 비결정적 수렴에 불과" (`advisory-chat-channel-spec.md` TV 교훈).
- 금지: "테스트 통과" 선언만으로 완료 처리.

### REQ-KBS-006 (GATE-3 — 사람 승인 없이 실행 금지)
**THE SYSTEM SHALL NOT** Phase 1 cron 등록 또는 Phase 2 RAG 전환을 사용자 명시적 승인 없이 실행한다.

- 근거: CLAUDE.md Gate Rules — "n8n workflow changes: Report first, then proceed", "Destructive infra actions: Human approval required". cron/systemd 변경과 RAG 경로 전환은 모두 인프라 변경.
- 본 SPEC은 설계(PLAN) 전용. Run phase 진입은 별도 `/moai run` 단계에서 사용자가 승인해야 한다 (Section 9).

### REQ-KBS-007 (KB 저장소 읽기 전용 — 영구 제약)
**THE SYSTEM SHALL NOT** ra-project, MD-process, llm-wiki 저장소에 어떤 형태의 쓰기(push, upload, commit, PR 생성)도 수행한다.

- 근거: CLAUDE.md:176("Write to llm-wiki / ra-project / MD-process repos: Prohibited permanently — read-only from this repo"), CLAUDE.md:206-210(지식기반 완전 읽기 전용).
- `index_github_repos.py`는 GitHub/Gitea **읽기 API**(`GET /repos/.../contents`, `GET /repos/.../git/trees`)만 사용. 쓰기 API 호출 없음(`index_github_repos.py` 전체 검증).
- 위반 시 즉시 중단.

### REQ-KBS-008 (Phase 1 — 임베딩 모델 일관성)
**WHILE** `index_github_repos.py`가 pgvector에 임베딩을 생성할 때, **THE SYSTEM SHALL** 기존 `ra_knowledge` row와 동일한 모델(`qwen3-embedding:latest`, dim=4096)을 사용한다.

- 근거: `index_github_repos.py:42-43`(`EMBED_MODEL`, `EMBED_DIM=4096`). Qdrant `nas_ra_docs`와 동일 스펙. Phase 2 전환 시 벡터 호환성 전제.
- 위반(모델 변경) 시 기존 row와 신규 row가 섞여 검색 품질 저하. 모델 변경은 별도 SPEC 필요.

---

## 5. Acceptance Criteria (Definition of Done)

### Phase 1

| # | Criterion (Given/When/Then) | Verification |
|---|---|---|
| AC-P1-1 | **Given** cron 등록 완료, **When** 최초 cron 실행 종료, **Then** `SELECT MAX(indexed_at) FROM ra_knowledge;` 결과가 24시간 이내 | psql 직접 조회 (T3610 `localhost:5433`) |
| AC-P1-2 | **Given** 첫 cron 실행 후, **When** 동일 SHA로 재실행, **Then** "No changes since last run (sha=...), skipping" 로그 출력 + row 수 불변 | cron 로그 파일 확인; `SELECT COUNT(*) FROM ra_knowledge;` 비교 |
| AC-P1-3 | **Given** ra-project 또는 MD-process에 신규 커밋, **When** 다음 cron 실행, **Then** 해당 repo 신규/수정 `.md`가 pgvector에 반영 (`source_path LIKE 'github:holee9/ra-project/%'` row의 `indexed_at` 갱신) | 의도적 테스트 커밋(읽기 전용이므로 별도 repo에서) 또는 실제 커밋 대기 후 psql 조회 |
| AC-P1-4 | **Given** cron 실행, **When** GitHub/Gitea API 호출, **Then** 읽기 API만 사용 (쓰기/PR/push 0건) | cron 로그 + GitHub/Gitea audit 확인 |
| AC-P1-5 | **Given** cron 실행 실패(네트워크/API 오류), **When** 다음 cron 실행, **Then** 정상 복구 (멱등성으로 손상 없음) | 일시적 오류 유발 후 재실행 |

### Phase 2 (REQ-KBS-004a DEFERRED 결정 이후)

| # | Criterion (Given/When/Then) | Verification |
|---|---|---|
| AC-P2-1 | **Given** RAG 전환 배포, **When** ra-project 또는 MD-process에만 존재하는 내용 쿼리, **Then** evidence `source_path`에 `github:holee9/ra-project/...` 또는 `github:holee9/MD-process/...` 반환 | **실서버 라이브 e2e** (`/v1/ra/advisory` 호출 후 evidence 검사). 단위 테스트만으로는 불충분(REQ-KBS-005) |
| AC-P2-2 | **Given** RAG 전환 배포, **When** 기존 NAS 문서 관련 쿼리, **Then** 기존 Qdrant `nas_ra_docs` 결과가 회귀 없이 동등하게 반환 (또는 DEFERRED 결정에 따라 pgvector에 이관 완료) | 라이브 e2e; NAS 전용 용어 쿼리로 회귀 확인 |
| AC-P2-3 | **Given** DEFERRED 설계 결정(REQ-KBS-004a: (a) 전량 이관 / (b) 하이브리드 조회 / (c) 기타), **When** Phase 2 Run 진입 전, **Then** 사용자가 설계 대안을 선택했음이 문서화되어 있음 | 설계 결정 기록 (별도 문서 또는 #107 코멘트) |

---

## 6. Delta Markers (Brownfield)

본 SPEC은 기존 시스템에 대한 변경이다. 각 대상의 변경 유형:

| 대상 | 변경 유형 | 상세 |
|---|---|---|
| `scripts/index_github_repos.py` | **[EXISTING]** | 코드 변경 없음. 이미 2026-06-11 동작 검증. Phase 1에서는 cron 항목만 추가. |
| abyz-lab crontab | **[NEW entry]** (Phase 1) | `index_github_repos.py` 일일 실행 항목 신설. 기존 `07:00/07:05 git pull`, `02:00 nas_indexer.py` 항목은 변경 없음. |
| `scripts/hermes-api-server.py` `_run_rag_search` | **[MODIFY]** (Phase 2) | `:138-160` Layer 1 RAG 조회 경로. `:119` `RAG_SCRIPT` / `:120` `QDRANT_URL` / `:144` subprocess call 전환 대상. DEFERRED 결정(REQ-KBS-004a)에 따라 상세 결정. |
| `/opt/hermes-ra/skills/ra-expert/scripts/rag_search.py` (서버) | **[MODIFY]** (Phase 2) | `DEFAULT_COLLECTION="nas_ra_docs"` 조회 경로. DEFERRED 결정에 따라 pgvector 조회 또는 하이브리드로 전환. |
| `scripts/nas_indexer_v2.py` | **[OBSERVE]** | 본 SPEC 범위 외. 단, v1→v2 cron 전환(#107 권장 3)과 본 SPEC Phase 1 cron이 동일 crontab에 공존하므로 시각 중복 주의. |

---

## 7. Exclusions (What NOT to Build)

> [HARD] 본 SPEC은 아래를 명시적으로 제외한다.

1. **KB 저장소 쓰기 (영구 제외)** — ra-project, MD-process, llm-wiki에 대한 push/upload/PR 생성은 CLAUDE.md:176에 의해 영구 금지. `index_github_repos.py`는 읽기 전용 API만 사용.
2. **Qdrant `nas_ra_docs` 2,094,439 points의 pgvector 마이그레이션** — Phase 2 DEFERRED 설계 결정(REQ-KBS-004a)의 하위 과제. 본 SPEC에서 설계하지 않음.
3. **`hermes-indexer.service` (xlsx/pptx 인덱서, `index_ra_knowledge.py`) 활성화** — 별건(#107 권장 2). disabled/inactive 상태이나 본 SPEC이 다루지 않음.
4. **nas_indexer v1→v2 cron 전환** — #107 권장 3, docstring "If OK, update cron to use v2". 본 SPEC 범위 외.
5. **임베딩 모델 교체** — `qwen3-embedding:latest` (dim=4096) 변경 없음. 교체 시 별도 SPEC.
6. **다중 사용자/RBAC/인증 시스템** — 본 SPEC은 파이프라인 스케줄링 + RAG 전환이며 사용자 인증과 무관.
7. **Phase 2 RAG 전환의 구현 코드** — 본 문서는 설계(PLAN). Phase 2 코드는 `/moai run` 별도 단계(Section 9).

---

## 8. Related Issues

| Issue | 관계 | 설명 |
|---|---|---|
| **#107** | 본 SPEC의 추적 이슈 | [MONITOR-6] pgvector ra_knowledge 정기 인덱싱 스케줄 부재. 본 SPEC이 해결 대상. |
| **#17** | 선행 마이그레이션 | [MIGRATE-1] Qdrant→pgvector. 인덱서 포팅은 완료, RAG 전환 미수행. 본 SPEC Phase 2가 그 후속. |
| **#34** | 관련 | [TSHAPE-1] 자동 인덱싱. 일회성으로 끝남(#107 확인). 본 SPEC Phase 1이 정기화로 해결. |
| **#50** | 관련 | [GROWTH-9] scheduled knowledge sync. 본 SPEC과 목적 중복; 본 SPEC이 #107의 구체적 설계를 제공. |
| **#19** | 관련 | [MIGRATE-2]. #17 후속 맥락. |
| **#105** | 교훈 | advisory Hermes CLI 지연/루프. 본 SPEC REQ-KBS-005(라이브 e2e 필수)의 근거. `advisory-chat-channel-spec.md` "Phase 1 Implementation Log"의 "직접 단발 테스트는 비결정적 수렴에 불과" 교훈 반영. |

### 검증 항목 (Phase 1 Run 전 확인 권장)

> 아래는 본 SPEC 작성 중 식별된 미확인 사항. Phase 1 Run 진입 전 확인 권장(블로커 아님).

- **daily-growth 루프의 "ra-project source" 참조 확인**: daily-growth runner(curriculum-seed 등)가 "ra-project source"를 참조할 때, 이것이 (a) curriculum-seed 라벨/메타데이터인지, (b) 실제 RAG 검색 경로인지 확인 필요. 만약 (b)라면 daily-growth도 Phase 2 전환의 영향권. Phase 1(pgvector 최신화)은 이와 무관하게 독립 가치.

---

## 9. Implementation Separation Note

> **본 SPEC은 설계(PLAN phase) 전용이다.**

- 본 문서는 `docs/specs/kb-rag-sync-spec.md`에 위치하며, 요구사항 정의 + 기술 검증 + 인수 기준을 제공한다.
- **구현(Run phase)은 별도 단계**: `/moai run` 등의 별도 사용자 승인 명령으로 진입한다.
- Phase 1 cron 신설과 Phase 2 RAG 전환은 모두 GATE-3(사람 승인) 영역(REQ-KBS-006). 본 SPEC의 존재가 실행 허가가 아니다.
- Phase 2는 REQ-KBS-004a(DEFERRED 설계 결정)가 해결되기 전까지 Run 진입 불가.

### 구현 순서 (사용자 승인 후)

- **Phase 1** (사용자 승인 후 `/moai run`): crontab 항목 추가 + 환경변수 확인(`scripts/.env`의 `GITHUB_PAT`, `GITEA_TOKEN`, `POSTGRES_URL`) + AC-P1-1~P1-5 검증. 코드 변경 없음.
- **Phase 2 준비**: REQ-KBS-004a (a)/(b)/(c) 설계 결정 세션 → 별도 설계 문서 작성 → 사용자 승인.
- **Phase 2 실행** (Phase 1 안정 + 설계 결정 완료 후): RAG 경로 전환 + **라이브 e2e**(REQ-KBS-005) + AC-P2-1~P2-3 검증.

---

## Annex A — Cross-reference Index

| Claim | Source |
|---|---|
| Layer 1 RAG → Qdrant `nas_ra_docs` | `scripts/hermes-api-server.py:138-160` (`_run_rag_search`), `:119` (`RAG_SCRIPT`), `:120` (`QDRANT_URL`) |
| Layer 4 → llm-wiki/openFDA/law.go.kr | `scripts/hermes-api-server.py:163-179` (`_run_knowledge_fetch`), `:127` (`KNOWLEDGE_SCRIPT`) |
| hermes-api-server에 ra_knowledge 조회 0건 | grep 검증 (본 SPEC 작성 시) |
| `index_github_repos.py` 인터페이스 | `scripts/index_github_repos.py:37` (REPOS), `:52` (GITEA_REPOS), `:41` (TABLE), `:39` (POSTGRES_URL), `:45` (SERVER_PORT=7791) |
| SHA 기반 증분 동기화 | `scripts/index_github_repos.py:467-468` (GitHub), `:573-574` (Gitea), `:517` (파일 단위 skip) |
| `indexed_at` UTC ISO-8601 기록 | `scripts/index_github_repos.py:530, 549` |
| 소스 경로 prefix | `github:{owner/repo}/{path}` (`index_github_repos.py:12` docstring), `gitea:{owner/repo}/{path}` (`:516`) |
| Qdrant `nas_ra_docs` 2,094,439 points | #107 점검 결과 (2026-07-10) |
| pgvector `ra_knowledge` 9,272 rows (정체) | #107 점검 결과 — MAX/MIN `indexed_at` = 2026-06-11 |
| KB repo 읽기 전용 영구 금지 | `CLAUDE.md:176`, `CLAUDE.md:206-210` |
| Gate Rules (cron/systemd = 사람 승인) | `CLAUDE.md` Gate Rules 표 |
| #105 라이브 e2e 교훈 | `docs/specs/advisory-chat-channel-spec.md` "Phase 1 Implementation Log" |
| 기존 crontab (git pull + nas_indexer) | #107 점검 결과 — `index_github_repos.py` 항목 부재 확인 |

---

## Annex C — Phase 1 Implementation Log (2026-07-10, GATE-3 승인 실행)

> 사용자 #107 Phase 1 승인(2026-07-10)에 따라 실행. "코드 변경 0" 원칙 — 단, 사전 검증에서 2건의 선행 setup이 필요했음(아래).

### 사전 검증에서 발견된 선행 setup (SPEC "검증 항목" 예상 범위)
1. **`/opt/hermes-ra/index_github_repos.py`가 구형 Qdrant 버전** (May 22, pgvector 마커 0/qdrant 13). cron이 /opt 경로를 쓰므로 repo의 pgvector 버전으로 교체 (구 버전은 `.bak-qdrant-20260710` 백업).
2. **env**: `scripts/.env`엔 `POSTGRES_URL`만 있었음. `GITHUB_PAT`(gh CLI 토큰, ra-project 비인증 60/hr 제한 해소)·`GITEA_TOKEN`(실제 40-char, `/opt/hermes-ra/.env`에서 확보 — `.bashrc` 값은 동적 변수 참조라 쓰레기값) 추가 통합.

### 실행 (2회 인덱서 실행, idempotent)
| KB | 결과 | rows | latest indexed_at | fresh ≤24h |
|----|------|------|-------------------|------------|
| MD-process | RUN1: new=167, +590 chunks | 4120 | 2026-07-10 05:38 | ✅ |
| ra-project | RUN2(GITHUB_PAT): new files, +167 chunks | 3273 | 2026-07-10 05:50 | ✅ |
| llm-wiki | **미완** (페이지네이션 한계, 아래) | 2636 | 2026-06-11 | ❌ |
- 전체: 9,272(06-11 스냅샷) → **10,029** (+757). idempotency: RUN2에서 MD-process "No changes since last run (sha=…), skipping" 로그로 AC-P1-2 입증.

### cron 설치 (abyz-lab crontab, 백업 `~/crontab.bak-20260710`)
```
17 3 * * * mkdir -p /home/abyz-lab/logs && bash -c 'set -a; . /opt/hermes-ra/.env; set +a; /usr/bin/python3 /opt/hermes-ra/index_github_repos.py >> /home/abyz-lab/logs/hermes-kb-index.log 2>&1'
```
- 시각 03:17 (nas_indexer 02:00 Ollama 경합 회피, off-round). `/var/log` 비쓰기 가능 → 사용자 영역 `~/logs/`.

### AC-P1 검증
| AC | 결과 | 근거 |
|----|------|------|
| AC-P1-1 freshness ≤24h | ✅ MD·ra-project / ❌ llm-wiki | docker psql `MAX(indexed_at)` per KB |
| AC-P1-2 idempotency | ✅ | RUN2 sha-skip 로그 + per-file `pgvector_source_exists` skip |
| AC-P1-3 신규 커밋 반영 | ✅ | ra-project·MD-process 신규 .md 757 chunks 반영 |
| AC-P1-4 읽기 API only | ✅ | github_get/gitea_get = GET 전용(POST는 로컬 Ollama 임베딩 only) |
| AC-P1-5 실패 복구 | ✅ | RUN1 ra-project 레이트리밋 실패 → RUN2 GITHUB_PAT로 복구(idempotent) |

### ⚠️ llm-wiki 미완 — 인덱서 페이지네이션 한계 (신규 이슈)
- **Gitea `git/trees?recursive=true`가 1000엔트리에서 `truncated: true`** → 인덱서가 페이지네이션 없이 첫 ~990 파일만 인덱싱. llm-wiki는 07-05 "auto-update 14276 files" 커밋 등 대규모 자동생성 위키 → 1000+ .md가 첫 페이지를 넘어 누락.
- 인덱서가 **기존 파일 내용 변경도 미감지** (`pgvector_source_exists` 시 skip, force=False). 변경된 파일 재임베딩 안 됨.
- 전체 동기화 = 인덱서 코드 개선(페이지네이션 + 변경 감지) + **수시간 GX10 임베딩(실시간 자문 백엔드 경합 = production risk) + 자동생성 위키 수만 건 DB 증가**. 이는 **REQ-KBS-004a DEFERRED 대규모 볼륨 영역**이자 **RA 품질 판단(사람 영역)**.
- → 별도 이슈 등록(indexer 페이지네이션 개선 + llm-wiki 볼륨 전략). 사용자 결정 대기. cron은 llm-wiki 첫 1000 파일 유지 보수(완전 동기화 전까지).

### GATE-3 준수
- 사용자 명시 승인(2026-07-10 #107 Phase1) 후 실행. crontab 변경(cron/systemd = 사람 결정 영역)은 대리 추가(백업 보존). `/opt/hermes-ra/` 인덱서 교체·`.env` 통합은 비파괴(abyz-lab 소유, 서비스 재기동 없음, DB는 idempotent 인덱싱만).
- KB repo 읽기 전용(REQ-KBS-007) 준수 — GET only.

End of SPEC.
