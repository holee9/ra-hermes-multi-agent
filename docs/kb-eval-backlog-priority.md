# KB Eval 채점 백로그 — 우선순위 정렬

생성: 2026-08-28 · 측정 기준 `docs/kb-eval-checksheets/`

## 감축 근거

| 단계 | 건수 |
|---|---:|
| 전체 케이스 | 648 |
| 채점 완료 | 59 |
| 미채점 | 589 |
| 응답 80자 미만 제외 (채점 불가) | -306 |
| 채점 가치 있는 미채점 | 283 |
| **시나리오 중복 제거 후 (실제 목표)** | **143** |

중복 제거 규칙: 동일 `scenario_id` 는 최신 `base_date`/`iteration` 1건만 채점한다.

## 채점 순서

| # | base_date | agent | decision_ref | 파일 |
|---:|---|---|---|---|
| 1 | 2026-07-24 | ra_us | `kb-eval-20260724-it03-ra_us-005` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 2 | 2026-07-24 | ra_us | `kb-eval-20260724-it03-ra_us-004` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 3 | 2026-07-24 | ra_us | `kb-eval-20260724-it03-ra_us-001` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 4 | 2026-07-24 | ra_us | `kb-eval-20260724-it02-ra_us-005` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 5 | 2026-07-24 | ra_us | `kb-eval-20260724-it02-ra_us-004` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 6 | 2026-07-24 | ra_us | `kb-eval-20260724-it02-ra_us-002` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 7 | 2026-07-24 | ra_us | `kb-eval-20260724-it02-ra_us-001` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 8 | 2026-07-24 | ra_us | `kb-eval-20260724-it01-ra_us-001` | `docs/kb-eval-checksheets/2026-07-24/iteration-01.md` |
| 9 | 2026-07-24 | ra_kr | `kb-eval-20260724-it03-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 10 | 2026-07-24 | ra_kr | `kb-eval-20260724-it03-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 11 | 2026-07-24 | ra_kr | `kb-eval-20260724-it03-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 12 | 2026-07-24 | ra_kr | `kb-eval-20260724-it02-ra_kr-003` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 13 | 2026-07-24 | ra_kr | `kb-eval-20260724-it02-ra_kr-001` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 14 | 2026-07-24 | ra_kr | `kb-eval-20260724-it01-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-24/iteration-01.md` |
| 15 | 2026-07-24 | ra_kr | `kb-eval-20260724-it01-ra_kr-003` | `docs/kb-eval-checksheets/2026-07-24/iteration-01.md` |
| 16 | 2026-07-24 | ra_kr | `kb-eval-20260724-it01-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-24/iteration-01.md` |
| 17 | 2026-07-24 | ra_kr | `kb-eval-20260724-it01-ra_kr-001` | `docs/kb-eval-checksheets/2026-07-24/iteration-01.md` |
| 18 | 2026-07-24 | ra_eu | `kb-eval-20260724-it03-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 19 | 2026-07-24 | ra_eu | `kb-eval-20260724-it03-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 20 | 2026-07-24 | ra_eu | `kb-eval-20260724-it03-ra_eu-002` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 21 | 2026-07-24 | ra_eu | `kb-eval-20260724-it03-ra_eu-001` | `docs/kb-eval-checksheets/2026-07-24/iteration-03.md` |
| 22 | 2026-07-24 | ra_eu | `kb-eval-20260724-it02-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 23 | 2026-07-24 | ra_eu | `kb-eval-20260724-it02-ra_eu-002` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 24 | 2026-07-24 | ra_eu | `kb-eval-20260724-it02-ra_eu-001` | `docs/kb-eval-checksheets/2026-07-24/iteration-02.md` |
| 25 | 2026-07-24 | ra_eu | `kb-eval-20260724-it01-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-24/iteration-01.md` |
| 26 | 2026-07-23 | ra_us | `kb-eval-20260723-it01-ra_us-004` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 27 | 2026-07-23 | ra_us | `kb-eval-20260723-it01-ra_us-003` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 28 | 2026-07-23 | ra_us | `kb-eval-20260723-it01-ra_us-002` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 29 | 2026-07-23 | ra_us | `kb-eval-20260723-it01-ra_us-001` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 30 | 2026-07-23 | ra_kr | `kb-eval-20260723-it01-ra_kr-003` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 31 | 2026-07-23 | ra_kr | `kb-eval-20260723-it01-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 32 | 2026-07-23 | ra_eu | `kb-eval-20260723-it01-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 33 | 2026-07-23 | ra_eu | `kb-eval-20260723-it01-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 34 | 2026-07-23 | ra_eu | `kb-eval-20260723-it01-ra_eu-003` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 35 | 2026-07-23 | ra_eu | `kb-eval-20260723-it01-ra_eu-002` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 36 | 2026-07-23 | ra_eu | `kb-eval-20260723-it01-ra_eu-001` | `docs/kb-eval-checksheets/2026-07-23/iteration-01.md` |
| 37 | 2026-07-22 | ra_us | `kb-eval-20260722-it03-ra_us-005` | `docs/kb-eval-checksheets/2026-07-22/iteration-03.md` |
| 38 | 2026-07-22 | ra_us | `kb-eval-20260722-it03-ra_us-004` | `docs/kb-eval-checksheets/2026-07-22/iteration-03.md` |
| 39 | 2026-07-22 | ra_us | `kb-eval-20260722-it03-ra_us-001` | `docs/kb-eval-checksheets/2026-07-22/iteration-03.md` |
| 40 | 2026-07-22 | ra_us | `kb-eval-20260722-it02-ra_us-005` | `docs/kb-eval-checksheets/2026-07-22/iteration-02.md` |
| 41 | 2026-07-22 | ra_us | `kb-eval-20260722-it02-ra_us-004` | `docs/kb-eval-checksheets/2026-07-22/iteration-02.md` |
| 42 | 2026-07-22 | ra_us | `kb-eval-20260722-it02-ra_us-003` | `docs/kb-eval-checksheets/2026-07-22/iteration-02.md` |
| 43 | 2026-07-22 | ra_us | `kb-eval-20260722-it02-ra_us-002` | `docs/kb-eval-checksheets/2026-07-22/iteration-02.md` |
| 44 | 2026-07-22 | ra_us | `kb-eval-20260722-it01-ra_us-005` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 45 | 2026-07-22 | ra_us | `kb-eval-20260722-it01-ra_us-004` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 46 | 2026-07-22 | ra_us | `kb-eval-20260722-it01-ra_us-002` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 47 | 2026-07-22 | ra_us | `kb-eval-20260722-it01-ra_us-001` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 48 | 2026-07-22 | ra_kr | `kb-eval-20260722-it03-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-22/iteration-03.md` |
| 49 | 2026-07-22 | ra_kr | `kb-eval-20260722-it03-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-22/iteration-03.md` |
| 50 | 2026-07-22 | ra_kr | `kb-eval-20260722-it02-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-22/iteration-02.md` |
| 51 | 2026-07-22 | ra_kr | `kb-eval-20260722-it01-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 52 | 2026-07-22 | ra_kr | `kb-eval-20260722-it01-ra_kr-003` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 53 | 2026-07-22 | ra_kr | `kb-eval-20260722-it01-ra_kr-001` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 54 | 2026-07-22 | ra_eu | `kb-eval-20260722-it02-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-22/iteration-02.md` |
| 55 | 2026-07-22 | ra_eu | `kb-eval-20260722-it01-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 56 | 2026-07-22 | ra_eu | `kb-eval-20260722-it01-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 57 | 2026-07-22 | ra_eu | `kb-eval-20260722-it01-ra_eu-003` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 58 | 2026-07-22 | ra_eu | `kb-eval-20260722-it01-ra_eu-002` | `docs/kb-eval-checksheets/2026-07-22/iteration-01.md` |
| 59 | 2026-07-21 | ra_us | `kb-eval-20260721-it01-ra_us-005` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 60 | 2026-07-21 | ra_us | `kb-eval-20260721-it01-ra_us-004` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 61 | 2026-07-21 | ra_us | `kb-eval-20260721-it01-ra_us-003` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 62 | 2026-07-21 | ra_us | `kb-eval-20260721-it01-ra_us-002` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 63 | 2026-07-21 | ra_us | `kb-eval-20260721-it01-ra_us-001` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 64 | 2026-07-21 | ra_kr | `kb-eval-20260721-it01-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 65 | 2026-07-21 | ra_kr | `kb-eval-20260721-it01-ra_kr-003` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 66 | 2026-07-21 | ra_kr | `kb-eval-20260721-it01-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 67 | 2026-07-21 | ra_eu | `kb-eval-20260721-it03-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-21/iteration-03.md` |
| 68 | 2026-07-21 | ra_eu | `kb-eval-20260721-it02-ra_eu-003` | `docs/kb-eval-checksheets/2026-07-21/iteration-02.md` |
| 69 | 2026-07-21 | ra_eu | `kb-eval-20260721-it01-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 70 | 2026-07-21 | ra_eu | `kb-eval-20260721-it01-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 71 | 2026-07-21 | ra_eu | `kb-eval-20260721-it01-ra_eu-003` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 72 | 2026-07-21 | ra_eu | `kb-eval-20260721-it01-ra_eu-002` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 73 | 2026-07-21 | ra_eu | `kb-eval-20260721-it01-ra_eu-001` | `docs/kb-eval-checksheets/2026-07-21/iteration-01.md` |
| 74 | 2026-07-20 | ra_us | `kb-eval-20260720-it01-ra_us-003` | `docs/kb-eval-checksheets/2026-07-20/iteration-01.md` |
| 75 | 2026-07-20 | ra_us | `kb-eval-20260720-it01-ra_us-002` | `docs/kb-eval-checksheets/2026-07-20/iteration-01.md` |
| 76 | 2026-07-20 | ra_us | `kb-eval-20260720-it01-ra_us-001` | `docs/kb-eval-checksheets/2026-07-20/iteration-01.md` |
| 77 | 2026-07-20 | ra_kr | `kb-eval-20260720-it01-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-20/iteration-01.md` |
| 78 | 2026-07-20 | ra_kr | `kb-eval-20260720-it01-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-20/iteration-01.md` |
| 79 | 2026-07-20 | ra_kr | `kb-eval-20260720-it01-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-20/iteration-01.md` |
| 80 | 2026-07-20 | ra_kr | `kb-eval-20260720-it01-ra_kr-001` | `docs/kb-eval-checksheets/2026-07-20/iteration-01.md` |
| 81 | 2026-07-20 | ra_eu | `kb-eval-20260720-it01-ra_eu-003` | `docs/kb-eval-checksheets/2026-07-20/iteration-01.md` |
| 82 | 2026-07-19 | ra_us | `kb-eval-20260719-it01-ra_us-005` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 83 | 2026-07-19 | ra_us | `kb-eval-20260719-it01-ra_us-004` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 84 | 2026-07-19 | ra_us | `kb-eval-20260719-it01-ra_us-003` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 85 | 2026-07-19 | ra_us | `kb-eval-20260719-it01-ra_us-001` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 86 | 2026-07-19 | ra_kr | `kb-eval-20260719-it01-ra_kr-003` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 87 | 2026-07-19 | ra_kr | `kb-eval-20260719-it01-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 88 | 2026-07-19 | ra_eu | `kb-eval-20260719-it01-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 89 | 2026-07-19 | ra_eu | `kb-eval-20260719-it01-ra_eu-002` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 90 | 2026-07-19 | ra_eu | `kb-eval-20260719-it01-ra_eu-001` | `docs/kb-eval-checksheets/2026-07-19/iteration-01.md` |
| 91 | 2026-07-18 | ra_us | `kb-eval-20260718-it01-ra_us-005` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 92 | 2026-07-18 | ra_us | `kb-eval-20260718-it01-ra_us-002` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 93 | 2026-07-18 | ra_us | `kb-eval-20260718-it01-ra_us-001` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 94 | 2026-07-18 | ra_kr | `kb-eval-20260718-it01-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 95 | 2026-07-18 | ra_kr | `kb-eval-20260718-it01-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 96 | 2026-07-18 | ra_eu | `kb-eval-20260718-it01-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 97 | 2026-07-18 | ra_eu | `kb-eval-20260718-it01-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 98 | 2026-07-18 | ra_eu | `kb-eval-20260718-it01-ra_eu-002` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 99 | 2026-07-18 | ra_eu | `kb-eval-20260718-it01-ra_eu-001` | `docs/kb-eval-checksheets/2026-07-18/iteration-01.md` |
| 100 | 2026-07-17 | ra_us | `kb-eval-20260717-it01-ra_us-005` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 101 | 2026-07-17 | ra_us | `kb-eval-20260717-it01-ra_us-003` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 102 | 2026-07-17 | ra_us | `kb-eval-20260717-it01-ra_us-002` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 103 | 2026-07-17 | ra_us | `kb-eval-20260717-it01-ra_us-001` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 104 | 2026-07-17 | ra_kr | `kb-eval-20260717-it01-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 105 | 2026-07-17 | ra_kr | `kb-eval-20260717-it01-ra_kr-003` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 106 | 2026-07-17 | ra_kr | `kb-eval-20260717-it01-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 107 | 2026-07-17 | ra_eu | `kb-eval-20260717-it01-ra_eu-002` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 108 | 2026-07-17 | ra_eu | `kb-eval-20260717-it01-ra_eu-001` | `docs/kb-eval-checksheets/2026-07-17/iteration-01.md` |
| 109 | 2026-07-16 | ra_us | `kb-eval-20260716-it01-ra_us-005` | `docs/kb-eval-checksheets/2026-07-16/iteration-01.md` |
| 110 | 2026-07-16 | ra_us | `kb-eval-20260716-it01-ra_us-004` | `docs/kb-eval-checksheets/2026-07-16/iteration-01.md` |
| 111 | 2026-07-16 | ra_kr | `kb-eval-20260716-it01-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-16/iteration-01.md` |
| 112 | 2026-07-16 | ra_kr | `kb-eval-20260716-it01-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-16/iteration-01.md` |
| 113 | 2026-07-16 | ra_kr | `kb-eval-20260716-it01-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-16/iteration-01.md` |
| 114 | 2026-07-16 | ra_kr | `kb-eval-20260716-it01-ra_kr-001` | `docs/kb-eval-checksheets/2026-07-16/iteration-01.md` |
| 115 | 2026-07-16 | ra_eu | `kb-eval-20260716-it01-ra_eu-003` | `docs/kb-eval-checksheets/2026-07-16/iteration-01.md` |
| 116 | 2026-07-15 | ra_us | `kb-eval-20260715-it17-ra_us-005` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 117 | 2026-07-15 | ra_us | `kb-eval-20260715-it17-ra_us-003` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 118 | 2026-07-15 | ra_us | `kb-eval-20260715-it17-ra_us-002` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 119 | 2026-07-15 | ra_us | `kb-eval-20260715-it17-ra_us-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 120 | 2026-07-15 | ra_us | `kb-eval-20260715-it16-ra_us-005` | `docs/kb-eval-checksheets/2026-07-15/iteration-16.md` |
| 121 | 2026-07-15 | ra_us | `kb-eval-20260715-it16-ra_us-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-16.md` |
| 122 | 2026-07-15 | ra_us | `kb-eval-20260715-it15-ra_us-004` | `docs/kb-eval-checksheets/2026-07-15/iteration-15.md` |
| 123 | 2026-07-15 | ra_us | `kb-eval-20260715-it15-ra_us-003` | `docs/kb-eval-checksheets/2026-07-15/iteration-15.md` |
| 124 | 2026-07-15 | ra_us | `kb-eval-20260715-it15-ra_us-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-15.md` |
| 125 | 2026-07-15 | ra_us | `kb-eval-20260715-it14-ra_us-005` | `docs/kb-eval-checksheets/2026-07-15/iteration-14.md` |
| 126 | 2026-07-15 | ra_us | `kb-eval-20260715-it14-ra_us-002` | `docs/kb-eval-checksheets/2026-07-15/iteration-14.md` |
| 127 | 2026-07-15 | ra_us | `kb-eval-20260715-it14-ra_us-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-14.md` |
| 128 | 2026-07-15 | ra_us | `kb-eval-20260715-it13-ra_us-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-13.md` |
| 129 | 2026-07-15 | ra_kr | `kb-eval-20260715-it17-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 130 | 2026-07-15 | ra_kr | `kb-eval-20260715-it17-ra_kr-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 131 | 2026-07-15 | ra_kr | `kb-eval-20260715-it16-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-15/iteration-16.md` |
| 132 | 2026-07-15 | ra_kr | `kb-eval-20260715-it15-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-15/iteration-15.md` |
| 133 | 2026-07-15 | ra_kr | `kb-eval-20260715-it15-ra_kr-002` | `docs/kb-eval-checksheets/2026-07-15/iteration-15.md` |
| 134 | 2026-07-15 | ra_kr | `kb-eval-20260715-it14-ra_kr-005` | `docs/kb-eval-checksheets/2026-07-15/iteration-14.md` |
| 135 | 2026-07-15 | ra_kr | `kb-eval-20260715-it14-ra_kr-004` | `docs/kb-eval-checksheets/2026-07-15/iteration-14.md` |
| 136 | 2026-07-15 | ra_kr | `kb-eval-20260715-it14-ra_kr-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-14.md` |
| 137 | 2026-07-15 | ra_kr | `kb-eval-20260715-it13-ra_kr-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-13.md` |
| 138 | 2026-07-15 | ra_eu | `kb-eval-20260715-it17-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 139 | 2026-07-15 | ra_eu | `kb-eval-20260715-it17-ra_eu-004` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 140 | 2026-07-15 | ra_eu | `kb-eval-20260715-it17-ra_eu-003` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 141 | 2026-07-15 | ra_eu | `kb-eval-20260715-it17-ra_eu-001` | `docs/kb-eval-checksheets/2026-07-15/iteration-17.md` |
| 142 | 2026-07-15 | ra_eu | `kb-eval-20260715-it16-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-15/iteration-16.md` |
| 143 | 2026-07-15 | ra_eu | `kb-eval-20260715-it15-ra_eu-005` | `docs/kb-eval-checksheets/2026-07-15/iteration-15.md` |
