# KB Eval Checklists - 2026-10-16

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-10-16, 채점 반영 전 기록)

운영본 가드(_unverified_identifiers + citation_error C1 + kr_grade_pathway) 15건 오프라인 적용 — **Yellow 4/15**:

| 케이스 | 판정 | 근거 |
|---|---|---|
| us-002·003·004·005 | Yellow | §892.2050 / §892.2020·2030 / Part 892 — 각 excerpt에 없음 |
| 나머지 11건 | 통과 | |

citation_error(C1)=0건, kr_grade_pathway=0건 발동(#145 해법 유지 — KR 전건 등급·경로 정상).

## 가채점 결과 (2026-10-16, 원문 대조 + 웹 팩트검증)

- **3점 12 · 2점 3 · 1점 0** (10-15 대비 3점 4→12). 환각(no_hallucination 실패) 3건(us-002 EU 용어 혼입, eu-005 Annex II 경로 오서술, kr-001 QMSR/MFDS 혼동·OECD-MAD 병합).
- **케이스 결함 1건**: eu-001 `kb_source_error` — 원문 7.2표 "Rule 9 — 방사선 발생 기기"가 KB 원본 오류(진단용은 Rule 10 → IIb, Rule 9는 치료용; 웹 교차검증 완료). 응답은 원문 충실, #144 경로 원본 정정 대상.
- 관측: us-002에서 FDA AI 요청 기한 180일 정확 서술(이전 회차 30일 창작과 동일 자리 — #146 SOUL 규칙 효과 후보).
