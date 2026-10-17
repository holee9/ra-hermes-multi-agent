# KB Eval Checklists - 2026-10-17

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-10-17, 채점 반영 전 기록)

운영본 가드 15건 오프라인 적용 — **Yellow 4/15**:

| 케이스 | 판정 | 근거 |
|---|---|---|
| us-001·002·003 | Yellow | §892.2050 / Part 892·862 — excerpt에 없음 |
| kr-002 | Yellow | kr_grade_pathway 1줄 — 가채점상 등급·경로 정상(3점)이라 **과잉 후보** |
| 나머지 11건 | 통과 | |

citation_error(C1)=0건.

## 가채점 결과 (2026-10-17, 원문 대조 + 웹 팩트검증)

- **3점 13 · 2점 2 · 1점 0** (10-16 대비 3점 12→13, 환각 3→2)
- **#157 참조표 3계열 전부 소멸 관측**:
  - 표준 판번 창작 **0건** — 전 응답이 레지스트리 판번과 일치(14971:2019, 62304:2006+A1:2015, 13485:2016, 62366-1:2015+A1:2020)
  - Annex 역할 혼동 **0건**(IX+XI 조합·Annex II 경로화 없음)
  - **US 응답의 EU 용어 병입 0건**(us-001은 교차 관할 소스를 명시 분리 처리 — 관할 규칙 가동 관측)
- 잔존 결함 2건(모두 KR·역방향 관할 혼입): kr-001 'MFDS Section 524B'(미국 FD&C 조문을 MFDS에 귀속)+PSUR 혼입, kr-004 PMCF 혼입+원본 없는 '7일' 수치
- us-005 FR 문서번호(2024-01709 등) **실재 확인**(QMSR 최종규칙 89 FR 7496) — 플래그와 함께 정밀 인용
