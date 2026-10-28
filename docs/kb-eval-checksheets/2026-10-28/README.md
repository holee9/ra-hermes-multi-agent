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

## 가채점 결과 (2026-10-28) — 동일일 재심 정정 반영
- **3점 10 · 2점 5 · 1점 0** (최초 가채점 3점 7·2점 8에서 eu-001·002·003 재심 정정)
- **재심 정정 사유**: 최초 채점의 "Art. 52 단락 오매핑 3건" 판정은 **채점자(세션)의 오검증**이었음 — 검색 AI 요약이 잘못된 매핑(52(1)=I·52(5)=IIa·52(7)=III)을 제공했고, 원문(Art. 52 전문 페이지) 확정 매핑은 **I=52(7)·Is/Im/Ir=52(7)·IIa=52(6)·IIb=52(4)/(5)·III=52(3)**로 응답이 정확했음. 이 과정에서 C3 린트의 초안 레지스트리도 동일 오류로 97 오탐을 냈으나 측정 절차(배포 전 오프라인 측정)가 원자적으로 포착·수정 — #134 측정 우선 원칙의 실효 실증.
- 확정 결함 내역 (전건 원문 검증): FDA §807.92 경로근거 오귀속 2(us-001·003) · IEC 60601-2-54 주제 오독 1(us-005, ECG/Part 870↔실제 X-ray) · AI Act↔MDR 혼입 1(eu-004, Annex I §A pt.11 역귀속+Art.49) · 비존재 개정판 표기 1(kr-005, ISO 14971 Amd 1:2024)
- KR 역방향 관할 6회 연속 0건 · 1점(환각) 0건
- 관찰 승격: **MFMF 오타 2회차 연속 재발 → 페르소나 정정 집행** (ra-kr SOUL, commit a8dacfa)
- 부기: Honcho ingest 15건은 최초 점수로 기록됨(첨부 전용) — 재심 정정은 본 원장이 기준(SSOT). 보수적 방향 오류로 correction_rate 지표가 흡수.
