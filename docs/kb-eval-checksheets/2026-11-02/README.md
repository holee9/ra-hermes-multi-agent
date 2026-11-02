# KB Eval Checklists - 2026-11-02

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-11-02)
**Yellow 0/14** — C1/C3 0건, K번호 0건. MFMF 오타 **재발 2건**(kr-001 "MFMF 고시"·kr-004 "full MFMF approval" — 10-29 소멸 후 재발, 부수·스코어 무영향). **us-001 캡처 실패(타임아웃)** — 미채점 처리(#147).

## 가채점 결과 (2026-11-02) — shadow 2차·원문 재검증 반영
- **3점 4 · 2점 9 · 1점 1 · 미채점 1(캡처 실패)** (14채점)
- **1점 kr-003 — 예외 발동(2회차): ingest 승인 대기.** 근거: 외국 CER 고시 날짜 오전용(2025-01-10=사이버보안 가이드라인 날짜)·라벨링↔SBOM 제16조 식별자 오결합·근거 없는 등급 규칙 창작("Korean guidance classifies... 3등급")·Generator 비의료기기→신고 자기모순
- **원문 재검증으로 채점자(세션) 판정 2건 철회**: "Annex II/III + Annex XI §10/§18"은 Art. 52(6) 제2옵션의 **정확한 표현**(eu-001·eu-004 → 3점) — 세션이 '왜곡'으로 오단했고 shadow가 맞았음. 10-29 eu-001 재심 근거 ②도 동일 철회 대상(근거 ① Art.83/84 라벨 교차로 2점 유지).
- shadow 수용: us-002·us-005 — **QMSR 제거 조항(구 §820.30·§820.100) 인용** + QMS-510(k) 심사 경계 혼동 + §820.35(b)≠문서관리. kr-005 — 소스 없는 현황 기술(FMEA 수행 중 등).
- **KB 원본 오류 재관측**(eu-001, #144): PSUR IIb '1년'(Art. 86(1)상 2년) — 10-29 발견분과 동일 원본, **정정 승인 대기 중**
- PSUR IIb 주기 오류 3연속 회차 관측(10-29 eu-002·005, 11-02 eu-002·003) — KB 정정이 근본 차단
- MFMF 재발(2건) — 페르소나 정정으로 소멸했다가 재발: 철자 규칙만으로는 불충분, 다음 관찰 후 대응 결정
- shadow judge: 일치 6·이의 8 — 채택 5(섀도 승)/기각 3(섀도 패: Art.52 매핑 오류 재발·의료기기법 제28조). **원문 재검증이 세션 오단까지 잡음 — 삼중 구조(세션↔shadow↔원문) 정착**
