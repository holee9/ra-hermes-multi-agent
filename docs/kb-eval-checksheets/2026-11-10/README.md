# KB Eval Checklists - 2026-11-10

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-11-10)
**Yellow 0/15** — C1/C3 린트 0건(응답 15건 전수), 캡처 실패 0건(15/15 OK), MFMF 0건. 11-07(토)·11-08(일)·11-09(월) 회차 공백 후 재개 회차.

## 가채점 결과 (2026-11-10) — 세션 1차 (shadow 7차 대기)
- **3점 6 · 2점 9 · 1점 0** (세션 1차)

## 최종 결과 (2026-11-10) — shadow 7차 이의 심사 반영
- **3점 2 · 2점 10 · 1점 3** (세션 1차 3점 6·2점 9 → 수용 하향 7[us-001·002·004→1점, kr-001·003·004·005→2점]·기각 1[eu-002 3점 유지]·무응답 3)
- **1점 3건(us-001·us-002·us-004) — 예외 조항 5회차 발동: ingest 승인 대기.**
  - us-001: predicate "GE LOGIQ-E9 = K191456" **오결합 — FDA DB 확인: K191456 = Campylobaster Quik Chek(Techlab, 미생물 IVD)** + 510(k)에 QMS 매뉴얼 증빙 요구 오류 + PCCP 의무화 과잉(§515C상 임의)
  - us-002: §814.102(e) 오인용(LII 확인: HUD 지정 조항 — 510(k) AI 180일 근거 아님) + ">30% 변경" 무근거 기준 창작 + §807.92 오인용(계열 7회차) + §820.30 잔존
  - us-004: QMSR 제거조항 다수 잔존(§820.100·820.20·820.25·Subpart C를 현행 요건으로) — QMSR 2026-02-02 시행 서술과 자기모순
- **PSUR IIb '1년' KB 원본 회귀 발견**: 11-03 정정(`2e280a2` 4개소)이 후속 커밋 `48524ca`(사실성 적재 게이트, 동시작업 lost-update)로 **되돌려짐** — 오늘 eu-001에 실제 전파(chunk: 자사 표 Handheld IIb=1년). 별도 파일 PMS_Plan_MDR_Article84_템플릿.md 자사 표(37-38행 '매년')도 미정정(같은 파일 186행은 2년으로 정합 — 파일 내 자기모순). → 재정정 제안 승인 대기
- **Rule 17 오매핑 재발 2건**(eu-001·eu-005: "Rule 17 = X-ray 영상기록" 주장) — KB 검증 기록(제품별_등급분류.md, 2026-06-09 EUR-Lex·TÜV·BSI)상 **Rule 10 영상기록=IIa / Rule 17=동물조직·세포**로 이미 정정된 사실의 재발. eu-003은 후보 나열 수준(경미)
- **shadow 7차 기각 1건(eu-002) = 지식 오류 6회차 연속**: PSUR IIb '연간' 재주장(#144 확정값 IIb=2년 배치) + GSPR §16≠방사선 주장(KB EUR-Lex 대조 체크리스트 §16=방사선 방호 배치) + Art.52(4) Annex IX 단독 불가 주장(EUR-Lex 원문상 가능) — 주간보고 3호 안건 2(정적 사실표 주입) 근거 추가
- shadow 수용 7건 중 부분 수용 1건(kr-003: 등급 판정 근거 디지털의료제품법 오귀속만 수용, 제28조 이의는 기각 — KB GMP_심사자료 정당)
- 기타 관찰: us-005 §820.30 잔존 1건·FDA 사이버 가이던스 '2023-05' 미검증 / kr-005 표기 파손 3건(未定 漢字·MFDO·'등 gradation 규정') / KB KGMP_QMSR_비교표 'SW 밸리데이션 ↔ IEC 62304 §8.1' 매핑 느슨(§8=구성관리 — 관찰)
- 원문 검증 4건: FDA DB(K191456)·LII(§814.102, §807.92)·EUR-Lex(Art.52(3)/(4)/(6) 경로 — eu-003 Class III Annex X+XI **정당** 확인·eu-005 IIa 대안 Annex II/III+XI §10 정당)·KB GSPR 체크리스트(§16)
