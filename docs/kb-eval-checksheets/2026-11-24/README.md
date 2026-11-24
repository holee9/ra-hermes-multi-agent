# KB Eval Checklists - 2026-11-24

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)


## 운영 가드 사전 판정 (2026-11-24)
**Yellow 0/15** — 캡처 실패 0건(15/15 OK), MFMF 0건, **C1/C3 린트 0건** (오탐 0 — 11-20의 9건 오탐도 없음). 11-21~23 공백 후 재개.

## 가채점 결과 (2026-11-24) — 세션 1차 (v4 3회차, shadow 10차 대기)
- **3점 10 · 2점 5 · 1점 0** — v4 도입 후 최고 3점율.

## 효과 판정 (세션 1차 기준)
- ✅ **PSUR 'IIb 2년' 0건 — 오염 완전 종결**: 관련 4건(eu-001·002·003·004+) 전부 'annual for IIb/III, ≤2-yearly for IIa' 정확. 11-24 3계층 정정(KB f2dd8c0·SOUL·사실표)이 첫 회차에서 전부 유효 — 시딩 수명주기 사례 4호(정정 사슬 롤백형).
- ✅ **§807.87/§807.92/§807.95 오인용 0건**: us-001 'Subpart E' 구분·us-005 807.87/807.92 분할 정확(소스 eSTAR 문서 기반) — 다음 회차 지속 여부 관찰.
- ✅ 디지털의료제품법 관할 과잉 0건(2회차 연속 — 종결 상태 유지)
- 🔄 QMSR 제거조항: us-003 1건 잔존('§§820.30-820.70 (withdrawn but still referenced via ISO 13485)' — 폐지 인지 후에도 요건 열거). 11-20에 이어 2회차 연속 us 계열 잔존이나 형태가 '인지+나열'로 변화. 다음 회차 완전 소멸 시 종결.


## 최종 결과 (2026-11-24) — shadow 10차 이의 심사 반영
- **3점 10 · 2점 4 · 1점 1(kr-005)** (세션 1차 3점 10·2점 5·1점 0 → 수용 하향 1[kr-005 2→1]·기각 10·합치 4)
- **1점 kr-005 — 예외 조항 7회차 발동: ingest 승인 대기**
  - 경로별 조문 pinpoint 창작 3건: '신고 §33-2 / 인증 §34-5 / 허가 §§35-1~35-7' — 소스 발췌에 전무 + shadow 원문 대조로도 비실재(한국 인증·허가는 의료기기법 제6조·제12조 계열). SOUL 규칙 6('그럴듯한 번호는 없느니만 못하다') 정면 위반 — 11-16 '고시 제2025-22호'(시딩)·11-20 '식별·추적 관리법'에 이은 kr-005 식별자 창작 3회차 연속.
- **shadow 10차 관찰**: 하향 11건 중 10건 기각 — 기각 형태는 ①답이 스스로 헷지한 사항 재지적 ②경미 표기·표현 pedantry ③소스(통합전략 문서)의 목적에 부합하는 서술. v4 3회차인데도 '경미→심각 오판' 지속 — 사실표가 참인 영역(PSUR·Art.52)에서는 정확하나 severity 판별이 여전히 취약. 11차에서 동일 경향이면 shadow 프롬프트에 v4 정의 명문화 검토 후보.
- 미세 관찰(3점 내): us-002 'Part 820 §7.3/§7.5' 표기 혼동·us-004 Special 510(k) 서술·eu-001 '§11 (Rule)' 표기·eu-003 'Rule 11-1/11-2' 비표준·eu-004 'requires Annex IX' 과잉·eu-005 '60601-2-54=electrical safety' 압축·kr-001 라벨/PMS 규정 귀속·kr-004 'K-UDI'·'고시 제2024-xx호' 자리표시자·'PCCP-style' 524B 병기(소스 유래)
- 기각 상세(대표): us-001 14971+10993 병기는 표준 관행 / us-002 영상기기 가정은 소스 문맥과 일치 / kr-002 'default 2등급'은 소스의 조건부 상향 논리 그대로 / kr-004 pathway 무조문 서술에 shadow가 스스로 조문 추가(결함 아님)
