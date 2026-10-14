# KB Eval Checklists - 2026-10-14

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-10-14, 채점 반영 전 기록 — 정정판)

운영본 가드(#153 배포분: _unverified_identifiers + _citation_errors C1 + _kr_grade_pathway)를
15건 응답에 오프라인 적용한 결과 — **Yellow 9/15**:

| 케이스 | 판정 | 근거 |
|---|---|---|
| us-001 | Yellow | §892.2050 — excerpt에 없음 |
| us-003 | Yellow | §892.2050, Part 892 — excerpt에 없음 |
| us-004 | Yellow | Part 892, §892.2050 — excerpt에 없음 |
| us-005 | Yellow | Part 892, §892.2050 — excerpt에 없음 |
| kr-001·002·004·005 | Yellow | kr_grade_pathway (Class II → 허가, 인증 없음) |
| kr-003 | Yellow | 가공 고시번호 제2025-22호 — excerpt에 없음 |
| 나머지 6건 | 통과 | |

※ 최초 기록(Yellow 0/15)은 측정 하네스의 응답 추출 버그(블록인용 접두만 추출)로 잘못 측정된 값이라 정정한다.
가드 자체는 정상 동작했고, 채점(사람 판정 환각 11건) 대비 포착 8/11(73%), 과잉 2/4 —
10-10 측정(46%, 과잉 1/2) 대비 재현율 향상. 미포착 3건은 의미 수준 오배치(Annex VII=동등성, Art 33-39, Annex II 섹션 매핑).
