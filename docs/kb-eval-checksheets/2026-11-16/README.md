# KB Eval Checklists - 2026-11-16

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

> 생성 스크립트 기본값(--iterations 3)으로 45건이 캡처되었으나 회차 관례(15건)를
> 유지하기 위해 iteration-01만 공식 회차로 사용. 02·03 캡처분은 /tmp/kb-eval-20261116-reserve/
> 예비 보관(미채점·미커밋). 캡처 전건 성공(45/45 OK).

## 운영 가드 사전 판정 (2026-11-16)
**Yellow 0/15** — C1/C3 린트 0건(ra_citation_lint 응답 15건 전수 직접 실행), 캡처 실패 0건(15/15 OK), MFMF 0건. 11-11(수)~11-13(금) 회차 공백 + 주말(11-14~15) 후 재개 회차. **채점 기준 v4(severity) 첫 실전 적용 + shadow 8차 정적 사실표 주입 첫 가동**(#164).

## 가채점 결과 (2026-11-16) — 세션 1차 (v4 기준, shadow 8차 대기)
- **3점 8 · 2점 5 · 1점 2** (세션 1차) — v4 첫 회차. 경미 흠(표기·연도 미검증 등)은 3점 감점 없이 미세 관찰로 원장 기록.

## 최종 결과 (2026-11-16) — shadow 8차(정적 사실표 첫 가동) 이의 심사 반영
- **3점 6 · 2점 7 · 1점 2** (세션 1차 3점 8·2점 5·1점 2 → 수용 하향 2[us-004·kr-002]·기각 7·합치 6)
- **1점 2건(us-001·kr-005) — 예외 조항 6회차 발동: ingest 승인 대기.**
  - us-001: 21 CFR **Part 812(=IDE)를 510(k) 요건·SE 근거(§812.2)·De Novo(§812.2(b)(3))로 오인용** + §807.92 분류근거 오인용(계열 8회차) + §807.100 '전자제출' 오귀속 — 다중 심각. (shadow 동일 독립 확인: 510(k)=Part 807 Subpart E, De Novo=§513(f)(2)/Part 860)
  - kr-005: ① 촬영실 GUI SW 'default 3·4등급→허가' 단정 — KB 정합 위반(가이드·등급분류 모두 2등급→인증) ② PCCP='Pre-Market Cybersecurity Plan' 오확장 재발(11-06 계열 — 실제 Predetermined Change Control Plan) ③ 'MFDS 고시 제2025-22호' — **11-17 정정: ra-kr SOUL 참조표에 실재(IEC 62304 전면 참조 편입 근거) → 창작이 아닌 페르소나 시딩** (동일 문서의 제25조 라인과 혼결합; 점수 1점 유지 — 근거는 ①②) ④ 'K-code' 비표준 용어
- **효과 판정 2건 종결**: PSUR IIb '1년/매년' **0건**(eu-001·eu-004 'IIa/IIb 2년·III 매년' 정확 — Art.86(1)) → **11-10 KB 재정정(319153f) 회귀 종결**. Rule 17 영상기록 **0건**(eu-002 Rule 17=인체·동물조직 III 정확, eu-005 Rule 10 radiology/recording 구분) → **ra-eu SOUL 정정 종결**. 페르소나-시딩 수명주기 3사례 전부 완결.
- **shadow 8차(사실표 주입 첫 가동) 관찰**: 기각 7건 중 shadow 자신이 'minor'/'not a defect'/'acceptable'이라 서술한 것 5건+ — 지식 오류(Art.52(4) X+XI 부정, 원문 확인으로 기각)는 eu-001 등 소수로 축소되고 **'경미 흠을 심각으로 오판'(v4 severity 미적응)이 주된 기각 형태**. 수용 2건(us-004 사이버 가이던스 '2022' 비존재 판번·kr-002 제25조 요건 창작 예시)은 정당.
- **사실표 후보 정정**: 표 내 'Class IIb = Art.52(4) (alternatively Art.52(5))' — Article 52 원문 확인 결과 X+XI 대안은 52(4) 내부에 존재하고 52(5)는 면제목록 위임규정 조항. shadow의 eu-001 경로 이의가 이 표현을 근거로 한 것으로 보임 → 표 문구 수정 제안 승인 대기.
- 재발 계열: §807.92 오인용 8회차(us-001) · QMSR 제거조항 잔존(us-002 §820.70·us-003 §820.30 — 루브릭 §7 2회차 트리거 해당, ra-us SOUL 대조 후보) · 디지털의료제품법 관할 과잉 kr-004(2회차 — §7 트리거) · PCCP 오확장 재발(kr-005) · De Novo→§812.2 재발(us-001)
- 신규 관찰: 'IEC 14971' 표기 3회(kr-001, 정확히는 ISO — 미세) · MDUFA IV×FY2026 병기(eu-002, source 원문 인용 — KB 원본 후보) · KGMP_비교표 §820.10(b)/(a) 인용은 source 정확 반영 · us-005 §892.2050 적용 범위(acquisition-control 측면) hedge 없이 단정 — 관찰

## v4 첫 적용 관찰 (2026-11-16)
- EU 5건 전원 3점 확정 — Art.52 전 계열(52(7)/(6)/(4)/(3), IIa 대안 Annex II/III+XI §10/§18)·Rule 10/17 구분·GSPR §16/§17 매핑 정확. shadow 6-7차의 반복 지식 오류 영역(Art.52 매핑·PSUR 86(1)·GSPR §16)이 정적 사실표 주입 후 세션·원문 검증으로 전부 정답 처리 — **사실표 주입 목적(지식 오류 반복 차단) 달성 관측**.
