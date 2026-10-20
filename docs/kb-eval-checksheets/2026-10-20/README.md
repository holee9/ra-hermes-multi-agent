# KB Eval Checklists - 2026-10-20

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-10-20, 채점 반영 전 기록)

**Yellow 2/15** (10-19 대비 6→2):
- us-003·us-004: K123456 — 모두 "(e.g., …)" 예시 표기 + "no identifier in source — verify separately" 명시. 환각 아님(판번 예시 포맷).
- citation_error 0건. MFMFDS 오타 0건(10-19 관찰 이후 소멸).

## 가채점 결과 (2026-10-20, 원문 대조 + 결함류 스캔 + 웹 팩트검증)

- **3점 14 · 2점 1 · 1점 0** (10-19 대비 동일 분포: 3점 14·2점 1·1점 0)
- **KR 역방향 관할 혼입 0건** — e5a34b3(524B·PSUR·PMCF 혼입 금지) **완전 적용 첫 회차, 혼입 0 달성**. kr-001은 "no EU PSUR term used" 명시, kr-003~005는 외국 규정 혼입 방어 서술("MFDS does not accept QMSR", foreign dossier 혼입 정리 절차)까지 등장
- 표준 판번·Annex 역할·US-EU 병입: **연속 0건 유지**
- **2점 1건 (us-003)**: "(MDR §822)" — FDA MDR=21 CFR Part 803(보고)과 §822/Section 522(시판후 감시)의 프로그램명 오귀속. 행 인용 자체는 정확. 웹검증 완료(eCFR/FDA). 식별자 계열 신관찰 — 기존 5개 결함류 외 서브유형으로 #134 기록
- 식별자 원문 대조: kr-004 고시 제2025-22호·kr-005 고시 제2026-46/47호 — KB 원문 실재 확인(ra-project GMP_심사자료 README 라인 15-16), 환각 아님
- 웹 팩트검증 4건 전부 정확: FDA 소프트웨어 가이던스 2023-06-14 ✅, 사이버보안 가이던스 2023-09-27 ✅, AI Act Annex I Section A point 11=MDR ✅, QMSR effective Feb 2026 ✅
- 잔여 관찰: 사이버보안 가이던스(2023-09-27)는 2026-02 후속판에 의해 대체됨 — source 작성 시점 기준이라 에이전트 결함은 아니나 KB 갱신 후보
