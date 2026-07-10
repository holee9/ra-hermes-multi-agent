# llm-wiki 운영 모델 (결정 기록)

> **Type**: 운영 결정(Operating Decision). 구현 SPEC 아님.
> **Date**: 2026-07-10. **Status**: ACCEPTED (사용자 합의 2026-07-10).
> **목적**: llm-wiki를 Hermes agent(ra_us/eu/kr)의 **성장동력**으로 활용하는 방향을 고정하여 표류 방지.

## 결정 (핵심 1줄)

**llm-wiki는 pgvector에 인제스트하지 않는다.** 사내 큐레이션 RA 자료이자 **Karpathy LLM-wiki 패턴의 "compile된 지식" 계층**(WIP)이므로, **Layer 4(`knowledge_fetch.py`)에서 개념 페이지를 on-demand 조회**로 활용한다. pgvector `ra_knowledge`는 ra-project/MD-process(vector-RAG 적합) 중심.

> 선행 결정 정정: kb-rag-sync SPEC Phase 1은 llm-wiki를 pgvector 인제스트 대상으로 포함했으나, **llm-wiki는 제외**한다(llm-wiki만 Layer 4로 분리).

## 운영 루프 — 양방향 성장 (agent 성장동력화)

- **소비**: agent advisory/study → Layer 4 `fetch_llm_wiki` → llm-wiki 개념 페이지 on-demand 조회 → 근거.
- **성장**: #106 KB 갭 탐지가 "llm-wiki에 이 개념 페이지 부재" 포착 → 사람이 llm-wiki에 compile → llm-wiki compound → agent 재활용.

llm-wiki = agent 성장을 흡수해 자라는 지식 계층. daily-growth(학습량) + llm-wiki compound(지식 축적) + #106(갭 탐지) = 단일 성장 엔진.

## 역할 경계 [HARD]

- 이 repo(ra-hermes) = **소비자**(read-only). llm-wiki 내용/구조 수정 ✕, tree 순회·전체 임베딩 "우회" ✕(Karpathy 설계 훐손 + 역할 위반).
- llm-wiki 수정·인터페이스 개선은 **llm-wiki repo(Gitea DR_RnD/ra-llm-wiki)** 영역 → cross-repo 이슈로 요청.

## 현재 갭 (원인 = llm-wiki 측 소비 인터페이스 부재, 이 repo 수정 영역 아님)

1. Gitea tree API 1,000 truncation → 22만 페이지 enumerate 불가.
2. 파일명 토큰 매칭만 → Karpathy 개념 구조(concepts/comparisons/synthesis) 미활용.
3. 한국어 alias 부재 → **ra_kr가 llm-wiki 검색 자체 불가**.

## 조치 — cross-repo 이슈

- **llm-wiki repo(Gitea) #1** (2026-07-10 등록): "[consumer-request] ra-hermes Layer 4 소비용 manifest/index 제공 요청".
- 요청: 기계 판독 manifest `{path, title, summary, tags, ko_aliases}` → ra-hermes가 작은 인덱스로 개념 매칭 → 히트 페이지 raw fetch(truncation 우회, ra_kr 활성, on-demand 정합, consumption-ready 태그로 WIP 구분).

## 대기/보류

- llm-wiki repo #1(manifest) 응답 대기. 제공 시 ra-hermes Layer 4 consumer 개선(한글 토큰화 + manifest 읽기) — **사용자 승인 전 코드 수정 보류**.
- pgvector llm-wiki 990건(2636 chunk) 정리: 운영 모델 확정 후 백업→DELETE(ra_knowledge는 현재 어떤 코드도 안 읽어 안전). 현재 보류.
- #107 Phase 1 cron(MD-process+ra-project, 03:17): 유효 유지.

## 관련

- ra-hermes #106(KB 갭 탐지 = 성장 루프 피드백) · #108(Layer 4 consumer 개선, llm-wiki #1 대기) · #107(MD-process/ra-project pgvector)
- llm-wiki repo(Gitea DR_RnD/ra-llm-wiki) #1
- `docs/specs/kb-rag-sync-spec.md` (llm-wiki 제외 정정 반영 필요)

---

Version: 1.0.0 | Date: 2026-07-10 | Owner: ra-hermes (consumer side)
