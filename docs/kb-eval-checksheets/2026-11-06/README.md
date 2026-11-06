# KB Eval Checklists - 2026-11-06

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-11-06)
**Yellow 0/15** — C1/C3 린트 0건(응답 15건 전수), 캡처 실패 0건, MFMF 0건. **UDI '§830.10' 인용 0건 — ra-us SOUL 정정(11-05 `b126787`) 익일 소멸 확인, UDI 계열 종결 선언.** PSUR IIb 법적 오귀속 1건 변형 재발(eu-001, 상세 하단).

## 가채점 결과 (2026-11-06) — 세션 1차 (shadow 6차 대기)
- **3점 6 · 2점 9 · 1점 0** (세션 1차; shadow 이의 심사 후 최종 확정 예정)
- **UDI 계열 종결**: §830.10 0건 + us-002·us-004의 UDI 게재(§801.20+)/시스템(§830.20) 분할 서술 정확 — 페르소나-시딩 수명주기 2사례(PSUR·UDI) 모두 재현 확인
- **PSUR IIb 변형 재발 1건(eu-001)**: "annual PSUR is mandatory (Art. 86(1)/(2))" — 소스의 자사 1년 주기를 법 의무로 승격(같은 응답에 ≤2yr 정확 서술 병존·자기모순). 순수 페르소나 전파형은 아니나 종결 선언 재검토 후보
- 재발 계열: §807.92 오인용 6회차(us-005 "determine class per §807.92")·QMSR 제거 조항 잔존(§820.70(i) us-002·§820.100 us-005)·IEC 주제 오독 계열(us-004 "60601-2-22")
- 신규 관찰: "KTR (Korea Telecom Registry)" UDI 등록 창작(kr-002)·PCCP 오확장(kr-002)·NIDS 영문 확장 무근거(kr-005)·§820.35 하위문자 매핑 창작(us-001)·"SaMD default 4등급" 근거 없는 단정(kr-001)
- 제28조(=KGMP/GMP 적합인정 근거)는 KB 원문(GMP_심사자료/README)으로 정당 확인 — 과거 shadow 기각은 제28조 자체가 아닌 부속 해석이었음

## 최종 결과 (2026-11-06) — shadow 6차 이의 심사 반영
- **3점 3 · 2점 11 · 1점 1** (세션 1차 3점 6·2점 9 → shadow 수용 하향 4[us-003·us-005·eu-005·kr-005]·기각 하향 11)
- **1점 us-005 — 예외 조항 4회차 발동: ingest 승인 대기.** focus(design-control readiness) 이탈 + 결함 5건(§807.92 오인용 6회차·§820.100 제거조항·§814.126 비존재 의심·§820.35 명칭 오기·§820.30 오용)
- **shadow 6차 기각 11건 — 지식 오류 5회차 연속**: PSUR IIb '연간' 3건(eu-002·003·005 — 원문 86(1) IIb=2년, #144 확정)·GSPR §16=lay persons 주장(eu-002·003·004 — KB GSPR 체크리스트[#144 EUR-Lex 대조] §16=방사선 방호)·Art.52 매핑 불일치 재발(eu-003·005)·제28조 부정(kr-001·004 — KB GMP_심사자료 제28조=적합인정 근거). **주간보고 3호: shadow 프롬프트에 검증된 정적 사실표(Art.52·PSUR 86(1)·GSPR 16-18) 주입안 확정 근거 확보**
- us-004 "IEC 60601-2-22=radiology" — shadow가 근거 제공(60601-2-22=laser equipment): KB 무출연과 정합, 주제 오독 계열 확정
- UDI 계열 종결 확정(§830.10 0건+분할 서술 정확)·PSUR IIb 변형 재발 1건(eu-001)은 종결 조건 재검토 후보

## ingest (2026-11-06)
- 사용자 승인(15건 전체) 후 **15건 ingest 완료** (세션 kb-eval-feedback-2026-11-06, 1차 11건+정규화 후 4건)
