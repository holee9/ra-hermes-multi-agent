# KB Eval Checklists - 2026-10-10

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (#153, 채점 전 기록)

채점 후 사람 판정과 비교해 가드의 실제 정밀도를 재기 위해, 채점 **전에** 운영 가드 결과를 남겨 둔다.
채점할 때 이 표를 참고하지 말고 응답만 보고 판정한다.

| 케이스 | 가드 | 근거 |
|---|---|---|
| ra_us-002 | Yellow | `21 CFR §892.2050`, `Part 892` — excerpt에 없음 |
| ra_us-004 | Yellow | `21 CFR §892.2050`, `Part 892` — excerpt에 없음 |
| ra_eu-004 | Yellow | `MDCG 2021-24` — excerpt에 없음 |
| ra_kr-001 | Yellow | 고시 `제2023-45호` — excerpt에 없음 |
| ra_kr-002·003·004 | Yellow | 2등급 계열을 허가로 매핑, 같은 줄에 인증 없음 |
| 나머지 8건 | 통과 | |

가드 Yellow 7/15. 채점이 끝나면 `kb-eval-feedback-ingest.py --execute` 후 이 표와 대조해 #153에 기록한다.
