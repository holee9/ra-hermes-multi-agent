# KB Eval Checklists - 2026-11-04

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-11-04)
**Yellow 0/15** — C1/C3 0건, 캡처 실패 0건, PSUR IIb KB 전파 0건(2회차 연속). MFMF 1건(kr-001 "MFMF guidelines", 부수·스코어 무영향 — 간헐 패턴 지속).

## 가채점 결과 (2026-11-04) — shadow 4차 반영
- **3점 4 · 2점 11 · 1점 0** (세션 1차 3점 8·2점 7 → shadow 이의 수용 4·기각 7)
- 예외 미발동 → 자동 ingest 진행
- **PSUR IIb '연간' 모델 내재 오류 3건(eu-001·003·005) — 4회차 연속 관측**. KB 전파는 0(정정 유지)이나 소스 무관 오류 지속 → **ra-eu PSUR 주기 페르소나 규칙 승인 필요성 재확인**
- shadow 기각 7건 중 다수: **shadow의 Art.52 오매핑 3회차 연속 재발**(IIa=52(7)·IIb=52(6) 주장 — 원문 판정과 불일치) + 제28조 주장(KB 반박) — shadow 프롬프트에 Art.52 원문 매핑 고정 주입 여부 검토 후보
- 재발 계열 결함: §806 '자발적 보고' 2건(누적 다수)·§807.92 오인용 1(4회차)·De Novo→§812.2 1·UDI §830 배치 범위 3
- 신규: IEC 82301-1 비존재 표준 인용(eu-002)·측정추적성↔ISO 10993-1 오결합(eu-002)·Special 510(k) 신규/변경 혼동(us-003)·제25조 면제요건 예시 창작(kr-001)·EU식 DoC 한국 혼입(kr-003)
