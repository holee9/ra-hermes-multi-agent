# KB Eval Checklists - 2026-11-26

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)


## 운영 가드 사전 판정 (2026-11-26)
**Yellow 0/15** — 캡처 15/15 OK, MFMF 1건(kr-005 'MFMF review' — 11-02 이후 간헐 재발, 부수·연속 아님), C3 린트 3건 = 기존 오탐 계열(Art.52 전체 매핑 라인+자기 에코). 11-25 공백 후 재개.

## 가채점 결과 (2026-11-26) — 세션 1차 (v4 4회차, shadow 11차 대기)
- **3점 7 · 2점 8 · 1점 0** (가채점 집계 정정)

## 효과 판정 (세션 1차 기준)
- ✅ **kr 조문 창작 0건** — ra-kr SOUL 라인 첫 회차 효과(kr-004 '§?? article not listed' 정직한 자리표시자, kr-005 무조문 경로 서술)
- ✅ PSUR 전건 정확 — eu-001 제품별 주기(Detector 2년/Source 1년/GUI 2년)까지 롤백 KB 정확 반영, eu-005 MDCG 2022-21 Annex IV 명시 인용. 종결 상태 유지
- ❌ **QMSR 제거조항 소멸 실패(4회차)** — us-001·us-003 잔존('withdrawn' 인지 멘트를 단 폐지 조항 나열이 하나의 서식으로 정착하는 형태) → 대응 후보 검토 필요
- 🔄 §807.87/92 오인용 재발(us-002 2건 — 11-24 0건 후 간헐 재발, 미종결)
- ⚠️ **신규 다발 후보: KR 등급 상향 계열 3건**(kr-001 'most SaMD→4등급'·kr-002 '3~4등급'·kr-003 '3등급' — 전부 소스 무등급+KB 정합 위반[GUI SW 2등급·X-ray 발생장치 2~3등급]) → §7 트리거 관찰
- KB 내부 불일치 관찰: 사이버 가이드라인 RA 요건 수 20(kr-003 소스)↔35(11-24 kr-004 소스) — 별도 정리 후보


## 최종 결과 (2026-11-26) — shadow 11차 이의 심사 반영
- **3점 4 · 2점 11 · 1점 0** (세션 1차 3점 7·2점 8 → 수용 하향 3[eu-001·eu-004·kr-004]·기각 3·합치 8·파싱 실패 1[eu-003 — API 무응답, 세션 점수 유지])
- **예외 미발동 — 자동 ingest 15건** (세션 kb-eval-feedback-2026-11-26)
- 수용 3건: eu-001 §22(일반인용 조항)를 전문가용 기기에 오적용 · eu-004 Art 83(2) 보존기간 오귀속+87조 '2영업일' 오인용(15일 기본/2일 공중보건 한정)·'≥100 patients' 무근거 · kr-004 DR-02 P0/P1 소스 불일치
- 기각 3건(us-004·eu-005·kr-005): 전부 경미(§11.10 체계 세부·IIa 'full assessment' 압축·사이버 가이드라인 교차-KB 인용)
- **shadow 11차 관찰**: '경미→심각 오판'은 완화(하향 6 중 3건 수용 — 10차 1/11 대비 개선), 사실표·KB 근거 영역 정확도 유지. v4 프롬프트 명문화는 보류 관찰.
- 재발 계열: QMSR 제거조항 4회차(us-001·003 'withdrawn' 멘트 나열형 정착) · §807.87/92 간헐 재발(us-002) · **신규 후보 KR 등급 상향 3건**(kr-001·002·003 — 소스 무등급+KB 정합 위반) · MFMF 1건(kr-005 부수)
- KB 관찰: 사이버 가이드라인 RA 요건 20↔35 문서 간 불일치
