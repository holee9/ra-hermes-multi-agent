# KB Eval Checklists - 2026-10-28

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-10-28)
**Yellow 0/15** — C1 citation_error 0건, K번호 0건. MFMFDS 오타 0이나 **변형 재발**(`MFMF-designated`, ra_kr-005 — 2회차 연속).

## 가채점 결과 (2026-10-28)
- **3점 7 · 2점 8 · 1점 0** — 무결 3회차 연속 종료, 식별자 오귀속 계열 8건 재발 (#134 지배 계열)
- 결함 내역 (전건 웹검증): FDA §807.92 경로근거 오귀속 2(us-001·003) · IEC 60601-2-54 주제 오독 1(us-005, ECG/Part 870↔실제 X-ray) · **MDR Art. 52 단락 오귀속 3(eu-001·002·003 — I→52(7)✗ 등 전면 오매핑, 실제 I=52(1)·IIa=52(5)·IIb=52(6)·III=52(7))** · AI Act↔MDR 혼입 1(eu-004, Annex I §A pt.11 역귀속+Art.49) · 비존재 개정판 표기 1(kr-005, ISO 14971 Amd 1:2024)
- KR 역방향 관할 6회 연속 0건 · 1점(환각) 0건
- 관찰 승격: **MFMF 오타 2회차 연속 재발 → 페르소나 정정 후보 확정** (10-27 부수 관찰에서 승격)
- 예외 조항(1점/kb_source_error/신유형) 미발동 → 자동 ingest 진행
