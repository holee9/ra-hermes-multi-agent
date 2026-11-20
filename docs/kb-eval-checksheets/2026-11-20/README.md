# KB Eval Checklists - 2026-11-20

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)


## 운영 가드 사전 판정 (2026-11-20)
**Yellow 0/15** — 캡처 실패 0건(15/15 OK), MFMF 0건. C3 린트 9건 = 전부 오탐(Art.52 전체 매핑을 한 줄에 나열한 표 셀 + 응답 내 라이브 린트 경고 자기 에코 — 11-16 이래 알려진 표/리스트 오탐 계열).

## 최종 결과 (2026-11-20) — shadow 9차 이의 심사 반영 (v4 2회차)
- **3점 4 · 2점 11 · 1점 0** (세션 1차 3점 5·2점 10 → 수용 하향 2[eu-003·kr-004]·기각 4·합치 9)
- **예외 미발동 — 자동 ingest 15건** (세션 kb-eval-feedback-2026-11-20)
- **효과 판정**: ① 디지털의료제품법 관할 과잉 **0건 — 종결**(kr-002 '어느 체계가 통치하는지 확인' gap 명시·kr-003 '병용 검토' 프레이밍·kr-004 소스 기반 인용) ② QMSR 제거조항 잔존 **us-003 1건만 재발**(11-16 2건 → 4/5 케이스 정확 매핑 §7.3/§7.5/§8.2.2+§820.35 — SOUL 라인 효과 부분 관측, 완전 소멸 시 다음 회차 판정) ③ PCCP 오확장 0건
- **신규 다발 계열: §807.87/§807.92 오인용** — us 5건 중 4건 변형 재발(§807.92를 유형·요건 근거로 / §807.92(a)(1)~(4) 하위조항 창작 / §807.95[기밀유지]를 내용 요건으로). §807.95 존재 eCFR 확인. → ra-us SOUL 참조표 추가 후보(§807.87=정보 요건·§807.92=Summary·§807.95=기밀유지)
- 수용 2건: eu-003(TD 전체를 Annex II §6.1로 귀속 — §6.1=preclinical/clinical, §1=기기서술)·kr-004('모든 등급 사이버 검증서 필수' 소스 불일치)
- 기타 1점 0·KR 관할 강건. kr-005 '의료기기 식별·추적 관리법' 비존재 법령명(shadow 동의)·kr-001 제28조(2) 임상평가 오귀속
- **PSUR IIb 주기 오검증 발견(중대)**: Art.86(1) 원문 확인(MDCG 2022-21 ANNEX IV 공식 표 + 조문 재현 2소스) — **IIa=2년 / IIb·III=연간**. 저희 #144 'IIb=2년' 확정값이 오검증이며 KB(ra-project)·ra-eu SOUL·shadow 사실표가 오염 상태. 오늘 EU 4건의 'IIb 2년' 서술은 오염 KB/SOUL 전파로 **Case Defect(KB source error propagated)로 분리 기록(#147)** — 에이전트 감점 제외. 정정 절차 승인 대기.
