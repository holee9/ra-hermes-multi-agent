# KB Eval Checklists - 2026-10-29

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-10-29)
**Yellow 1/15** — K123456 1건(us-002, "(e.g., …)" 예시 표기, 환각 아님). C1 0건. **C3 첫 실전 포착 1건(eu-005, III↔52(4) — 진양성)**. MFMF 오타 **0건 — 페르소나 정정 효과 확인(소멸)**.

## 가채점 결과 (2026-10-29) — shadow judge 1차 시행 반영
- **3점 2 · 2점 12 · 1점 1** (세션 1차 가채점 3점 10·2점 5에서 shadow 이의 심사 후 조정: 수용 8·기각 4)
- **1점 eu-004 — 예외 조항 발동: 자동 ingest 금지, 승인 대기.** 근거: ① UDI 근거 Reg. (EU) 2017/746(=IVDR) 오귀속 ② Annex II §7·§8 존재하지 않는 섹션 창작(실제 6개 섹션) ③ GSPR/Annex 번호 부정확 다수
- shadow 기각 사례(채점자 방어): shadow의 Art. 52 매핑(52(4)=IIa·52(7)=IIb) 및 의료기기법 제28조 부정은 원문(Art.52 전문)·KB(law.go.kr 근거 2026-07 개편)과 불일치 — 검증자도 오류를 만든다는 10-28 교훈의 재현, 이중 검증 구조의 실효 입증
- 주요 수용 결함: 구 QSR 서브섹션 체계 오매핑(us-003)·§820.35 내용 창작(us-001)·§806 의무/자발 반전(us-005)·**KR 역방향 관할 혼입 재발**(kr-003, ARR·FDA MDR을 MFDS 의무로 — 6회 연속 0 종료)·24시간 보고 수치 창작(kr-005)·PSUR IIb 주기 오기(eu-002·005: IIb는 2년, III·이식형만 연간)
- **KB 원본 오류 발견(eu-001 전파, #144)**: PSUR 주기 표에서 IIb '1년' — MDR Art. 86(1)상 IIa·IIb는 2년. 원본 정정 후보.
- shadow judge: claude-sonnet-5-5, 15케이스, 일치 3·이의 12(전부 하향), 원장 reports/kb-eval-shadow/2026-10-29.json
