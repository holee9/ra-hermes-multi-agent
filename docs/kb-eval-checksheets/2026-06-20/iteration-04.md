# KB Eval Checksheet - 2026-06-20 Iteration 04

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260620-it04-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_us-001", "iteration": 4, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "acd22701c477f3a6", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "f6a2c1ada430e6553587ff0dec2d0d4a5c2f07d9d5324d083fb4cbfb7dc3d256"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `acd22701c477f3a6`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md`
- Source hash: `f6a2c1ada430e6553587ff0dec2d0d4a5c2f07d9d5324d083fb4cbfb7dc3d256`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, 510k, PMA

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

2. Chunk `753170761960322016`

> ## 수록 대상 - Premarket Notification 510(k) 제출 가이던스 - PMA (Premarket Approval) 관련 문서 - De Novo Classification Request 관련 문서 - eSTAR / eSubmitter 제출 양식 및 매뉴얼

### kb-eval-20260620-it04-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_us-002", "iteration": 4, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "ff4810d805139cb9", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `ff4810d805139cb9`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md`
- Source hash: `9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, 510k, PMA

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

### kb-eval-20260620-it04-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_us-003", "iteration": 4, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "1c88f209f2d71f6d", "source": "gitea:DR_RnD/ra-llm-wiki/wiki/concepts/fda-premarket-cybersecurity-guidance-2023.md", "source_hash": "8cce89162a47f3c0ae05f96e6d4f93d20e6969ec2dec9e665a364e26a96ad213"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `1c88f209f2d71f6d`
- Source: `gitea:DR_RnD/ra-llm-wiki/wiki/concepts/fda-premarket-cybersecurity-guidance-2023.md`
- Source hash: `8cce89162a47f3c0ae05f96e6d4f93d20e6969ec2dec9e665a364e26a96ad213`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1095479905700035165`

> HnX-P1/HnX-PB 510(k) 요약서 Rev3는 사이버보안 항목에서 이 가이드를 직접 언급한다. 이는 해당 제출이 단순 전기 안전과 성능 시험만이 아니라, 소프트웨어 및 연결성 기기의 보안 제출 관행까지 반영했음을 보여 준다. 기존 위키의 [[facility-implemented-access-control-for-radiation-device]]는 주로 사용설명서 관점의 통제 개념이라면, 이 페이지는 프리마켓 제출 패키지 차원의 사이버보안 규제 근거를 다룬다.

2. Chunk `430018873236804839`

> --- type: concept title: 2023 FDA 프리마켓 사이버보안 가이드 created: 2026-06-08 updated: 2026-06-08 tags: [fda, 사이버보안, 가이드라인, 프리마켓, 의료기기] related: [hnx-p1, hnx-pb, facility-implemented-access-control-for-radiation-device, iso-14971, iec-62304, software-included-medical-device, 39-DHF%20%28%EC%9D%B8%ED%97%88%EA%B0%80%29--21-05_HnX-P1%2C%20HnX-PB--31-92_%EC%9D%B8%EC%A6%9D%20-%20FDA--10-Att--62dlaw] sources: ["DHF (인허가)/05_HnX-P1", "HnX-PB/92_인증 - FDA/Attachment/036_510(K) Summary (Rev3).docx", "DHF (인허가)/05_HnX-P1, HnX-PB/92_인증 - FDA/Attachment/036_510(K) Summary (Rev3).docx"] --- # 2023 FDA 프리마켓 사이버보안 가이드 [[fda-premarket-cybersecurity-guidance-2023]]는...

### kb-eval-20260620-it04-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_us-004", "iteration": 4, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "c3fdcb056429e992", "source": "github:holee9/MD-process/issue-drafts/157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md", "source_hash": "7ceead695690f1ea2c83bf679e8114b768ad7b4b8dbab95eccc08d70d1be9f02"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c3fdcb056429e992`
- Source: `github:holee9/MD-process/issue-drafts/157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md`
- Source hash: `7ceead695690f1ea2c83bf679e8114b768ad7b4b8dbab95eccc08d70d1be9f02`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `124189968261264047`

> ## 변경 요약 - §5.11 신설: FDA QMSR CP 7382.850 하 FSCA 실사 대응 - §5.11.1 FSCA-CAPA 연계 강화 및 문서화 경로도 - §5.11.2 FSCA 실사 자가점검표 (5항목) - §5.12 신설: EUDAMED 의무화 대응 FSCA 보고 경로 전환 - §5.12.1 현행 보고 경로 (과도기) - §5.12.2 Vigilance 의무화 후 전환 계획 - §5.12.3 Market Surveillance 활용 (현재 의무) - §5.1 트리거에 EUDAMED Market Surveillance 모듈 추가 - frontmatter: applicable에 FDA CP 7382.850 추가, related-docs에 SOP-RM-001 추가

2. Chunk `362018177408777344`

> --- title: "SOP-FSCA-001 v0.3 보강 — QMSR FSCA 실사 대응 및 EUDAMED 보고 경로 전환" labels: ["enhancement", "08_PMS", "QMSR", "EUDAMED", "v0.3"] state: closed ---

### kb-eval-20260620-it04-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_us-005", "iteration": 4, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "064219d3c0ed7ffe", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "5efbe22295bef8ba002a4a98b9810b1add07c3de15e6e35a2236ecceda3f5fc2"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `064219d3c0ed7ffe`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md`
- Source hash: `5efbe22295bef8ba002a4a98b9810b1add07c3de15e6e35a2236ecceda3f5fc2`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, 510k, PMA

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1145353526911094904`

> ### 2.3 작성 원칙 (FDA RTA 회피) - 전체 제출물 내 IFU 문장 **문구 일치** (라벨·IFU·SE 비교표·Summary 전부 동일) - Predicate과 동일하거나 더 좁은 범위 (확장 시 de novo·PMA 위험) - 진단 성능·치료 효과에 대한 **임상 주장은 임상 데이터가 뒷받침**하는 범위로 한정 - 환자군·해부 부위·사용 환경(병원·가정·야전 등) 명시

2. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

## ra_eu

### kb-eval-20260620-it04-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_eu-001", "iteration": 4, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "ac643302b9b690aa", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "07766aa926d3be57b6bf2d75f4605289efab7c283eadd6841a001afa2d8987be"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `ac643302b9b690aa`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md`
- Source hash: `07766aa926d3be57b6bf2d75f4605289efab7c283eadd6841a001afa2d8987be`
- Focus: PMS and PMCF planning
- Matched keywords: MDR, MDCG

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1079572648514538742`

> ## 관련 KB 문서 - [공통_Clinical_Evaluation_Plan_Report_MDR_템플릿](../../../02_제품별_기술파일/공통/공통_Clinical_Evaluation_Plan_Report_MDR_템플릿.md) — CEP/CER 작성 템플릿 - [MDR_AnnexI_GSPR_Checklist](../MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md) — GSPR 전항목 체크리스트 - [MDR_AnnexII_Technical_Documentation_Template](../MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md) — 기술문서 구조 - [MDR_AnnexIII_PMS_TD_Template](../MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md) — PMCF 포함 PMS 문서

2. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

### kb-eval-20260620-it04-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_eu-002", "iteration": 4, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c72d0ced7824b130", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c72d0ced7824b130`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source hash: `a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1014893419282866507`

> | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter | 보완 요청 | Additional Information (AI) Request | | 근거 법령 | MDR Annex VII + 2026/977 | 의료기기법 §12 + 허가·신고·심사 규정 | 21 CFR 807 + FDA Review Policy | | 답변 기한 | NB와 합의 (법정 상한 없음) | 1차 60일, 2차 60일 | 180일 (타임라인 기산일부터) | | 최대 중단 횟수 | 4회 (product verification 기준) | 2차까지 (실질 2회) | 제한 없음 (Interactive Review 가능) | | Clock-stop | 예 (NB 요청 당일 stop, 제출 익일 resume) | 예 (보완 기간 제외) | 예 (AI 발송일부터 stop) | | 미응답 시 | 평가 종료 / 불승인 | 취하 간주 | 허가 거부 | | 사전 대화 창구 | Structured Dialogue (Art.7, 2026/977) | 상담제도 (비공식) | Pre-Sub (Q-Sub) (공식, 문서화) | | 주요 결함 유형 | CER, TD, QMS NC, Labelin...

### kb-eval-20260620-it04-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_eu-003", "iteration": 4, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "06a4948c0723b020", "source": "github:holee9/MD-process/issue-drafts/147_02_SOP-CC-001_v0.3_EUDAMED_변경통제.md", "source_hash": "fc0e54ecdc1c1c11682572837470660b240448e2fff735983c531e09ea0c4c83"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `06a4948c0723b020`
- Source: `github:holee9/MD-process/issue-drafts/147_02_SOP-CC-001_v0.3_EUDAMED_변경통제.md`
- Source hash: `fc0e54ecdc1c1c11682572837470660b240448e2fff735983c531e09ea0c4c83`
- Focus: PMS and PMCF planning
- Matched keywords: EUDAMED

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `152830173003720653`

> --- title: "SOP-CC-001 v0.3 보강 — EUDAMED 등록 갱신·QMSR 기록 강화·IEC 62304 Ed2 대비" labels: [enhancement, 02_QMS, v0.3, EUDAMED, QMSR] state: closed --- SOP-CC-001 v0.2 → v0.3 보강 완료. - QMSR 실사 대응 변경통제 기록 FDA 열람 대비 (§9.1) - EUDAMED UDI/Device 등록 갱신 절차 추가, CIA 6축 확장 (§9.2) - IEC 62304 Ed2 SW 분류 전환 준비 항목 추가 (§9.3)

### kb-eval-20260620-it04-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_eu-004", "iteration": 4, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "245f13448c3d95e3", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/README.md", "source_hash": "71c0d67fb6fa7c6ec5b92f4aeea270911ed9f7094081e3008d2b6b6bbdf37a2a"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `245f13448c3d95e3`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/README.md`
- Source hash: `71c0d67fb6fa7c6ec5b92f4aeea270911ed9f7094081e3008d2b6b6bbdf37a2a`
- Focus: PMS and PMCF planning
- Matched keywords: MDR, MDCG

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `364087153572440679`

> ## 참고 - MDCG 가이던스는 법적 구속력은 없으나 Notified Body 심사 시 사실상 기준으로 활용됨. - 공식 소스: https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en

2. Chunk `655919733198120217`

> ## 주요 MDCG 문서 (X-ray / SW 관련) - **MDCG 2019-11**: Qualification and Classification of Software - **MDCG 2019-16**: Cybersecurity Guidance - **MDCG 2020-5**: Clinical Evaluation – Equivalence - **MDCG 2020-6**: Sufficient Clinical Evidence for Legacy Devices - **MDCG 2020-7**: PMCF Plan Template - **MDCG 2020-8**: PMCF Evaluation Report Template - **MDCG 2021-5**: Guidance on standardisation for medical devices - **MDCG 2021-24**: Classification of Medical Devices - **MDCG 2022-5**: Guidance on borderline between MDR and IVDR - **MDCG 2022-14**: Transition to MDR/IVDR - **MDCG 2023-3**: Questions and Answers on vigilance

### kb-eval-20260620-it04-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_eu-005", "iteration": 4, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3eade4215aa4ce58", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md", "source_hash": "e58a514ed0c819866f9eb094ca113d09dad260f22054cadd6a7b17a7302724ef"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `3eade4215aa4ce58`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md`
- Source hash: `e58a514ed0c819866f9eb094ca113d09dad260f22054cadd6a7b17a7302724ef`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1042295090390197081`

> - Regulation (EU) 2024/1689 (AI Act) — 전문, Art. 6, 9-17, 43, 61-62, Annex II/III/IV - Regulation (EU) 2017/745 (MDR) — Art. 10, 15, 83-87, Annex I-III, IX-XI - MDCG 2019-11 (소프트웨어 분류), MDCG 2019-16 Rev.1 (사이버보안), MDCG 2020-3 (significant changes) - IEC 62304:2006/A1:2015, IEC 62366-1:2015/A1:2020, IEC 81001-5-1:2021 - ISO 14971:2019/A11:2021 - FDA AI/ML-based SaMD Action Plan, PCCP Draft Guidance 2023 - DQS Global — AI Act & AI-Enabled Medical Devices: Regulatory Status 2026 - MedDeviceGuide — EU AI Act for Medical Devices Compliance Guide 2026 - Gibson Dunn — EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines (2026) - Bird & Bird...

2. Chunk `1046173636268087282`

> ### 4.2 데이터 거버넌스 | AI Act 요건 | 조항 | MDR / ISO 대응 | 통합 접근 | X-ray 적용 | |-------------|------|----------------|-----------|-----------| | Data & Data Governance | Art. 10 | MDR Annex II §6.1, IEC 62304, GMLP | 학습/검증/테스트 데이터셋 관리 SOP | X-ray 영상 데이터: 다기관(≥3), 다장비 브랜드, 체형·연령·성별 대표성 확보 | | 데이터 품질 | Art. 10(2-5) | — | 라벨링 품질 관리, 편향 점검 | 판독 전문의 ≥2인 합의 라벨링, Cohen's κ ≥ 0.80 |

## ra_kr

### kb-eval-20260620-it04-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_kr-001", "iteration": 4, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "10827e12b09f4e90", "source": "github:holee9/MD-process/issue-drafts/016_02_디지털의료제품법_요구사항_매트릭스.md", "source_hash": "1ca0054d754d312b28d0a37c0c01b90e9aee20167474ad514e422cd863b3c653"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `10827e12b09f4e90`
- Source: `github:holee9/MD-process/issue-drafts/016_02_디지털의료제품법_요구사항_매트릭스.md`
- Source hash: `1ca0054d754d312b28d0a37c0c01b90e9aee20167474ad514e422cd863b3c653`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1073623794890451367`

> ## 참고 링크 - 관련 문서: `02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md` - 교차검증: `12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md` - 관련 이슈: #014 디지털의료제품법_SaMD_AI_요구

2. Chunk `127614843726416513`

> --- title: "[02] 디지털의료제품법 35개 요구사항 매트릭스 v0.1 및 갭 분석" labels: "documentation,review,regulation,qms" state: closed ---

### kb-eval-20260620-it04-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_kr-002", "iteration": 4, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "15c1bc3b177d5ade", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_6종_가이드라인_요약.md", "source_hash": "59cd597ad73333f3a36a6a56fb5fd2997d20bab166a18e0b7ed594f77fe17fff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `15c1bc3b177d5ade`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_6종_가이드라인_요약.md`
- Source hash: `59cd597ad73333f3a36a6a56fb5fd2997d20bab166a18e0b7ed594f77fe17fff`
- Focus: digital medical products act impact
- Matched keywords: MFDS, 국내_MFDS

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1059459999498570675`

> ## 2. 6종 가이드라인 개요 | 번호 | 구분 | 가이드라인명 | 주요 적용 대상 | |---|---|---|---| | 1 | **제정** | 디지털의료기기소프트웨어 허가·심사 가이드라인 | 내장형·독립형 소프트웨어 전반 공통 기본서 | | 2 | 개정 | 의료기기 소프트웨어 허가·심사 가이드라인 | **내장형** 소프트웨어 + 의료기기 연동 앱·웹 | | 3 | 개정 | 인공지능기술이 적용된 디지털의료기기 허가·심사 가이드라인 | MLMD(Machine Learning-enabled Medical Device) 전반 | | 4 | 개정 | 가상융합기술이 적용된 디지털의료기기 허가·심사 가이드라인 | VR·AR·MR 기술 적용 의료기기 | | 5 | 개정 | 디지털치료기기 허가·심사 가이드라인 | **독립형** SW 중 질병 예방·관리·치료 목적 제품 | | 6 | 개정 | 인공지능기술이 적용된 디지털의료기기 임상시험방법 설계 가이드라인 | AI 적용 의료기기 임상시험계획 승인 | > **구조**: 가이드라인 1번(신제정)이 기본서 역할, 2~6번은 기본서를 보완하는 계층 구조. ---

2. Chunk `1114958470722170859`

> ## 7. 참조 문서 - `MFDS_디지털의료제품법_하위고시_추적.md` — 고시 제2025-23호·제2025-25호 상세 (#9) - `MFDS_기술문서_섹션별_작성가이드.md` — 기술문서 작성 지침 (#8) - `eSTAR_05_Software_Section.md` — FDA SW Section (IEC 62304 기반) 비교 참조 (#5)

### kb-eval-20260620-it04-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_kr-003", "iteration": 4, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "116503046c3b4537", "source": "gitea:DR_RnD/ra-llm-wiki/wiki/concepts/mfds-simple-change-notification-for-low-risk-accessory-change.md", "source_hash": "c6d0d4a5d02f873fa092229c96e78635cc89f16c13bc8d255846ccdee9cca50b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `116503046c3b4537`
- Source: `gitea:DR_RnD/ra-llm-wiki/wiki/concepts/mfds-simple-change-notification-for-low-risk-accessory-change.md`
- Source hash: `c6d0d4a5d02f873fa092229c96e78635cc89f16c13bc8d255846ccdee9cca50b`
- Focus: digital medical products act impact
- Matched keywords: MFDS

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `232824651692370829`

> --- type: concept title: 저위험 액세서리 변경에 대한 MFDS 단순변경 신고 created: 2026-06-10 updated: 2026-06-10 tags: [개념, mfds, 단순변경, level-3, 인허가, accessory] related: [aq-byeong-seungin-20230113-1, simple-change-without-design-change-document-in-had1717mc-mg-bom-management, low-risk-operational-change-classified-as-level-3-without-specification-change] sources: ["DHF (인허가)/01_HAD1717MC", "MG/구본/개발문서/DMR/12. 설계변경 문서/(단순변경으로 설변없이 진행) LAN Cable 사양 변경", "길이 추가 및 USB 추가/HAD1717MC. MG Lan Cable 변경 20221215-2.xlsx", "DHF (인허가)/01_HAD1717MC, MG/구본/개발문서/DMR/12. 설계변경 문서/(단순변경으로 설변없이 진행) LAN Cable 사양 변경, 길이 추가 및 USB 추가/HAD1717MC. MG Lan Cable 변경 20221215-2.xlsx"] --...

2. Chunk `609564720741101058`

> 이번 승인 문서에서는 “규제 당국 보고 대상 아님”이라고 적으면서도, 동시에 “국내에 대해서 MFDS 단순 변경 신고 진행 완료 : `2023-01-13`”라고 명시한다. 따라서 이 표현은 중대한 규제 보고나 재인증 대상은 아니지만, 경미 변경에 대한 행정적 신고 절차는 수행되었다는 의미로 읽는 것이 합리적이다. 이 개념은 [[simple-change-without-design-change-document-in-had1717mc-mg-bom-management]]를 보완한다. 폴더명만 보면 설계변경 문서 없이 진행된 것처럼 보이지만, 실제로는 내부 변경 요청·승인과 인허가 후속 조치가 함께 존재했다는 점이 확인되기 때문이다. > ⚠️ **모순:** “보고 대상 아님”과 “단순 변경 신고 완료”는 표면적으로 긴장된다. 다만 문맥상 서로 완전히 배타적인 표현은 아니며, 신고 수준의 경미 변경으로 해석하는 것이 타당하다.

### kb-eval-20260620-it04-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_kr-004", "iteration": 4, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "87f5b2f6bc9b8e12", "source": "github:holee9/MD-process/11_일일_리서치로그/2026-04-22_SBOM_SOP_디지털의료제품법_방사선규칙.md", "source_hash": "97d5ec93550108c32c415b428001b852fe4b5155602d1f7d37d2282afd2b529f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `87f5b2f6bc9b8e12`
- Source: `github:holee9/MD-process/11_일일_리서치로그/2026-04-22_SBOM_SOP_디지털의료제품법_방사선규칙.md`
- Source hash: `97d5ec93550108c32c415b428001b852fe4b5155602d1f7d37d2282afd2b529f`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1003768849121276725`

> ### 4) 진단용 방사선 안전관리 규칙 개정 - 2024-11-07 제1068호: 포터블 기준·방어시설 신설, 누설선량 한도 100mR → **2mR/h** 로 50배 강화 - 2025-07-18 제1122호: 조문 원문 확인 필요(오픈 작업) - 안전관리 정의에 환자 외 피폭 방지 포함 — IFU 설계 영향

2. Chunk `276419741497260621`

> ## 실행 내용 1. `03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md` v0.1 신규 — SBOM 생성·VEX·VDR·제출 체계 통합 SOP 2. `01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md` v0.1 신규 — 디지털의료제품법 핵심 요구·가이드라인 5종·프로젝트 영향도 분석 3. `01_법규_규제/01_국내_MFDS/진단용방사선_안전관리규칙_개정이력.md` v0.1 신규 — 2024(제1068호)·2025(제1122호) 개정 이력 및 제조자 영향 정리 4. `12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md` 신규 — FDA/MDR/MFDS 3축 SBOM 요구사항 정합성, 디지털의료제품법과 기존 의료기기법 갭 분석

### kb-eval-20260620-it04-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it04-ra_kr-005", "iteration": 4, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "b11a7b10e1688ee9", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `b11a7b10e1688ee9`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source hash: `fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce`
- Focus: digital medical products act impact
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1131342938714268388`

> ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건 (AI/ML 포함) | SW GMP 적용 기준 | ---

2. Chunk `385578214769089426`

> ## 5. 모니터링 포인트 | 항목 | 상태 | 확인 주기 | |---|---|---| | 디지털 GMP 고시 시행 | 2025년 내 예정 [검증 필요] | 분기별 확인 | | 디지털의료제품법 시행규칙 개정 (총리령 제2088호) | 2026-01-23 개정 완료 | — | | 추가 가이드라인 제정 | 지속 예고 중 | 월별 mfds.go.kr 확인 | | MFDS 6종 가이드라인 후속 개정 | 2025년 이후 수시 | 분기별 확인 | ---
