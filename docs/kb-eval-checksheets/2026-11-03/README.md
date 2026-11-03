# KB Eval Checklists - 2026-11-03

This folder stores human review checksheets generated from the current RA knowledge base.
Checked boxes are kept in git as audit history and can later be converted into Honcho `score_given` feedback.

- Iterations: 1
- Cases per agent per iteration: 5
- Expected total cases: 15
- Latest generation mode: random

Files:

- [Iteration 01](iteration-01.md)

## 운영 가드 사전 판정 (2026-11-03)
**Yellow 0/15** — C1/C3 0건, K번호 0건, MFMF 0건, 캡처 실패 0건. **PSUR IIb KB 전파 0건 — KB 정정(11-03 `2e280a2`) 효과 확인, #144 완결 처리.**

## 가채점 결과 (2026-11-03) — shadow 3차·원문 원칙 반영
- **3점 2 · 2점 13 · 1점 0** (세션 1차 3점 9·2점 6 → shadow 이의 수용 7·기각 1)
- 예외 미발동(1점 0·KB오류 0·신유형 없음) → 자동 ingest 진행
- **PSUR IIb '연간' 오류 4건(eu-002~005)** — 이번 회차 소스들엔 주기가 없어 **KB 정정이 미치지 못하는 모델 내재 오류**임이 확인됨. KB 전파(소스 인용)는 차단됐으나 모델 사전지식 오류는 별개 → ra-eu 페르소나/참조표에 PSUR 주기 규칙(IIa·IIb 2년, III·이식형 연간) 추가 후보
- shadow 수용 7건: UDI §830/§801 배치 혼동 2(us-001·004)·"FDA 자발적 보고" 오기(us-001)·62304 Class C→FDA Class III 혼동(us-005)·**clock-stop 규칙 창작**(kr-001, 65/80일=심사기간인데 보완기한으로 전용)·62304를 영상시험 기준으로 인용(kr-002)·HIRA 기관 오귀속(kr-004)·등급별 사이버보안 적용 분할 창작(kr-005)
- shadow 기각 1건: kr-003(KGMP ≥2등급 서술·라벨링 부담 확장 해석 — 근거 불충분, 제28조는 KB 반박)
- **추이 해석 주의**: 3점 2/15는 품질 급락이 아니라 shadow 3회차 연속 전수 하향 심사의 누적 효과 — 회차 간 채점 기준(v3+원문) 동일하므로 10-29(3점 2)·11-02(3점 4)·11-03(3점 2)은 동일 기준 연속 데이터. 3점 기준이 지속적으로 상향 평준화된 상태로, 주간보고 3호에서 기준 재정의(3점의 실용적 의미) 논의 필요
