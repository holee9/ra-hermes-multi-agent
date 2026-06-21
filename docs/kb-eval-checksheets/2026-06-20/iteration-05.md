# KB Eval Checksheet - 2026-06-20 Iteration 05

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260620-it05-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_us-001", "iteration": 5, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "7be9e36f79e668ae", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md", "source_hash": "c016b9b71c421bbff191427c089029b85d25aab55e122f03e3dabbff564b8880"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `7be9e36f79e668ae`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md`
- Source hash: `c016b9b71c421bbff191427c089029b85d25aab55e122f03e3dabbff564b8880`
- Focus: SaMD change impact
- Matched keywords: FDA

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
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

1. Chunk `1031538840091158839`

> ### 4.2 응답서 구성 원칙 **FDA Guidance 권고 (Section V of FDA Guidance on deficiency responses)**: 각 결함에 대해 다음 3가지 중 하나로 응답: 1. 요청된 정보 또는 데이터 제공 2. 해당 사항이 없는 이유 설명 3. 대체 정보 제공 + 왜 그 정보가 문제를 해결하는지 설명 **형식 원칙**: - 결함 번호를 **원문 그대로** 복사·유지 (순서 변경 금지) - 표(Table) 형식 + 행 색상 교차 (FDA 원문 vs 회사 응답 구분) - 단일 부록 번호 체계 유지 (AI Response App. 001, 002, …) - 각 부록 표지: "What this is / What it proves / Where it's referenced" ---

2. Chunk `1062884112493939033`

> ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합

### kb-eval-20260620-it05-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_us-002", "iteration": 5, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "41f250c8fefe47dc", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d5412d37b42151a55d00d8ebb4711becdd2240ca934acae093691cb40fe3c58b"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `41f250c8fefe47dc`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md`
- Source hash: `d5412d37b42151a55d00d8ebb4711becdd2240ca934acae093691cb40fe3c58b`
- Focus: SaMD change impact
- Matched keywords: FDA

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
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

1. Chunk `1081838125103053920`

> ## 8. MFDS: 사전변경관리계획 (디지털의료제품법) - 디지털의료기기 AI 알고리즘 변경 시, 사전에 변경관리계획 제출·승인 - 승인된 범위 내 변경 → 별도 허가 면제 - 생성형 AI 의료기기 허가·심사 가이드라인 (2025-01-24, 세계 최초 발간): 생성형 AI 특성 반영한 별도 심사 기준 포함 ---

2. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

### kb-eval-20260620-it05-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_us-003", "iteration": 5, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "a677c77afb92eb4a", "source": "github:holee9/MD-process/issue-drafts/158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md", "source_hash": "ec94495a1bf80d4e9e3bb0b8c01801499bd1ff16dd2c0697728ee0455ba62816"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `a677c77afb92eb4a`
- Source: `github:holee9/MD-process/issue-drafts/158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md`
- Source hash: `ec94495a1bf80d4e9e3bb0b8c01801499bd1ff16dd2c0697728ee0455ba62816`
- Focus: SaMD change impact
- Matched keywords: QMSR

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
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

1. Chunk `108529124691273873`

> ## 변경 요약 - §7 신설: FDA QMSR CP 7382.850 불만처리 실사 대응 - §7.1 QMSR 하 불만처리 프로세스 정합 (§8.2.2/§8.2.3 매핑) - §7.2 CP 7382.850 실사 대비 불만처리 자가점검표 (7항목) - §7.3 FDA Guidance Agenda 2026 불만처리 가이드라인 대비 - §8 신설: EUDAMED 연계 불만처리 - §8.1 Actor Registration/UDI/Market Surveillance 연계 - §8.2 PSUR 제출 연계 (Class III EUDAMED 의무) - §8.3 Vigilance 모듈 과도기 - frontmatter: applicable 확장, related-docs에 SOP-RM-001/PRO-DA-001 추가, title·purpose 정규화 - F-PMS-002 양식에 UDI-DI/SRN 필드 추가

2. Chunk `710767560367426911`

> --- title: "SOP-PMS-001 v0.3 보강 — QMSR 불만처리 실사 대응 및 EUDAMED 연계" labels: ["enhancement", "08_PMS", "QMSR", "EUDAMED", "v0.3"] state: closed ---

### kb-eval-20260620-it05-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_us-004", "iteration": 5, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "6937348208307a7d", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "f6a2c1ada430e6553587ff0dec2d0d4a5c2f07d9d5324d083fb4cbfb7dc3d256"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `6937348208307a7d`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md`
- Source hash: `f6a2c1ada430e6553587ff0dec2d0d4a5c2f07d9d5324d083fb4cbfb7dc3d256`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
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

### kb-eval-20260620-it05-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_us-005", "iteration": 5, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "9f1e6a64039f3a29", "source": "github:holee9/MD-process/issue-drafts/009_03_SW_사이버보안_IEC81001_5_1_FDA.md", "source_hash": "bfde8ccac162058d143af5ce7e6e0ec7f9d3f13456d947bcf5780e1b7e49e1e1"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `9f1e6a64039f3a29`
- Source: `github:holee9/MD-process/issue-drafts/009_03_SW_사이버보안_IEC81001_5_1_FDA.md`
- Source hash: `bfde8ccac162058d143af5ce7e6e0ec7f9d3f13456d947bcf5780e1b7e49e1e1`
- Focus: SaMD change impact
- Matched keywords: FDA

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
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

1. Chunk `1139028071545473971`

> ## 참고 링크 - `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md` - `03_설계_개발관리/IEC_62304_SW_수명주기.md` - `12_교차검증_보고서/2026-04-21_Xray_안전성능_사이버보안_정합성.md`

2. Chunk `147599709023299597`

> ## 체크리스트 - [x] 표준·규제 범위 정의 - [x] Security Management Plan 11개 절 구조 확정 - [x] 81001-5-1 ↔ 62304 매핑표 - [x] FDA 제출물(SBOM, Threat Model, Architecture, VM Plan, Testing) 매핑 - [x] Coordinated Vulnerability Disclosure 절차 초안 - [ ] SBOM 생성 툴체인(CycloneDX/SPDX) 선정 - [ ] 디지털의료제품법·MFDS 가이드 최신 개정 반영 - [ ] TD 템플릿 Cybersecurity Annex로 연결

## ra_eu

### kb-eval-20260620-it05-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_eu-001", "iteration": 5, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "e19ab3c5f240e287", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/README.md", "source_hash": "71c0d67fb6fa7c6ec5b92f4aeea270911ed9f7094081e3008d2b6b6bbdf37a2a"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e19ab3c5f240e287`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/README.md`
- Source hash: `71c0d67fb6fa7c6ec5b92f4aeea270911ed9f7094081e3008d2b6b6bbdf37a2a`
- Focus: Notified Body question response
- Matched keywords: MDR, MDCG

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
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

### kb-eval-20260620-it05-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_eu-002", "iteration": 5, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "dcad872801338fdb", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2019-16_Rev1_Cybersecurity_대응_체크리스트.md", "source_hash": "73cd35ce968999ac597a2ffd2cc0e9de93103ba5c45edee078877a0e708818ce"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `dcad872801338fdb`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2019-16_Rev1_Cybersecurity_대응_체크리스트.md`
- Source hash: `73cd35ce968999ac597a2ffd2cc0e9de93103ba5c45edee078877a0e708818ce`
- Focus: Notified Body question response
- Matched keywords: MDR, MDCG

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
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

1. Chunk `1033927941898965900`

> > ✅: 필수 적용 / △: 조건부 적용 / -: 해당없음 (위험 평가 결과에 따라 조정)

2. Chunk `1035120197226241881`

> > 최종 갱신: 2026-05-14 (자동보강 #44) > 근거: https://health.ec.europa.eu/system/files/2022-01/md_cybersecurity_en.pdf | https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en # MDCG 2019-16 Rev.1 Cybersecurity 대응 체크리스트

### kb-eval-20260620-it05-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_eu-003", "iteration": 5, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "aca65a7b9faf9135", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `aca65a7b9faf9135`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md`
- Source hash: `d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731`
- Focus: Notified Body question response
- Matched keywords: MDR

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
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

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

### kb-eval-20260620-it05-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_eu-004", "iteration": 5, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "e523d5c5df0128d8", "source": "github:holee9/MD-process/issue-drafts/147_02_SOP-CC-001_v0.3_EUDAMED_변경통제.md", "source_hash": "fc0e54ecdc1c1c11682572837470660b240448e2fff735983c531e09ea0c4c83"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e523d5c5df0128d8`
- Source: `github:holee9/MD-process/issue-drafts/147_02_SOP-CC-001_v0.3_EUDAMED_변경통제.md`
- Source hash: `fc0e54ecdc1c1c11682572837470660b240448e2fff735983c531e09ea0c4c83`
- Focus: Notified Body question response
- Matched keywords: EUDAMED

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
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

### kb-eval-20260620-it05-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_eu-005", "iteration": 5, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "29ac71354b4e3707", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `29ac71354b4e3707`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
- Focus: Notified Body question response
- Matched keywords: MDR

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

## ra_kr

### kb-eval-20260620-it05-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_kr-001", "iteration": 5, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "d26365e2a144c8d8", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "f7cbb3934bcbba6112884ce0da34c36acc448d5de57ca375d45a234998110525"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `d26365e2a144c8d8`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md`
- Source hash: `f7cbb3934bcbba6112884ce0da34c36acc448d5de57ca375d45a234998110525`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
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

1. Chunk `1087366389248262195`

> ### G6. SOP-SBOM-001과 SOP-CC-001(Change Control) 인터페이스 미정의 - SBOM 변경이 Change Control 트리거하는 조건 명시 필요 - **조치**: SOP-CC-001 v0.2에 SBOM 컴포넌트 추가/제거/버전업 시 Change 분류 기준 반영

2. Chunk `1097781465051134503`

> ### G4. MFDS RA-01 ~ RA-20 체크리스트 전수 대응 문서화 미흡 - 현재 확보된 문서는 SBOM(RA-07) 중심 - **조치**: RA-01~RA-20 전체 매트릭스 작성 (별도 이슈)

### kb-eval-20260620-it05-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_kr-002", "iteration": 5, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "c1c2aa41dfd0f6a9", "source": "github:holee9/MD-process/issue-drafts/091_01_MFDS_GMP_커버리지_94퍼센트_갱신.md", "source_hash": "fe21b220c92090300334febc505ac3e1af4cc3c647d04fe11961d30402702598"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `c1c2aa41dfd0f6a9`
- Source: `github:holee9/MD-process/issue-drafts/091_01_MFDS_GMP_커버리지_94퍼센트_갱신.md`
- Source hash: `fe21b220c92090300334febc505ac3e1af4cc3c647d04fe11961d30402702598`
- Focus: supplementary-response strategy
- Matched keywords: MFDS

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
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

1. Chunk `1124004338404433649`

> ## 배경 MFDS GMP 가이드에서 미작성으로 표시되었던 3건(§4.2.3 의료기기파일, §7.5.4 서비스활동, §8.4 데이터분석)이 이미 작성 완료(TF-TD-001, SOP-SVC-001, PRO-DA-001)되어 있어 매핑 현황을 갱신하였다. 미작성 절차 우선순위 섹션도 전량 완료 현황으로 업데이트.

2. Chunk `134744712691084534`

> ## 체크리스트 - [x] §4.2.3 → TF-TD-001 매핑 반영 - [x] §7.5.4 → SOP-SVC-001 매핑 반영 - [x] §8.4 → PRO-DA-001 매핑 반영 - [x] 커버리지 요약 86% → 94% 갱신 - [x] 미작성 절차 우선순위 → 작성 완료 현황으로 전환

### kb-eval-20260620-it05-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_kr-003", "iteration": 5, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "c32672f608a606aa", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `c32672f608a606aa`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md`
- Source hash: `f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
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

1. Chunk `1002132727008468922`

> ## 1. 법령 개요 | 항목 | 내용 | |------|------| | 법률명 | 디지털의료제품법 (법률 제20139호, 제정 2024-01-23) | | 시행일 | 2025-01-24 | | 시행령 | 대통령령 제35219호 (2025-01-23 제정, 2025-01-24 시행) | | 시행규칙 | 총리령 제1958호 (2025-02-28 시행) | | 소관 | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과 | | 주요 하위고시 | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 분류 및 등급 지정 규정, 디지털의료기기 제조 및 품질관리 기준, 디지털의료기기 전자적 침해행위 보안 지침(안) |

2. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

### kb-eval-20260620-it05-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_kr-004", "iteration": 5, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "f816cdb5f2e0d475", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/README.md", "source_hash": "955a83a25d265db55798a04d0d7968a79f47ac36e05a19a9321ef64a0749ffab"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f816cdb5f2e0d475`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/README.md`
- Source hash: `955a83a25d265db55798a04d0d7968a79f47ac36e05a19a9321ef64a0749ffab`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
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

1. Chunk `205092528198502292`

> ## 핵심 근거 (X-ray 관련) - 의료기기법 및 시행규칙 - 「의료기기 품목 및 품목별 등급에 관한 규정」 - 「의료기기 허가·신고·심사 등에 관한 규정」 - 「의료기기 GMP 심사·평가 등에 관한 규정」 - 「의료용 X선 발생장치 등 기술문서 작성 가이드라인」 - 「의료용 SW 허가·심사 가이드라인」

2. Chunk `550471061485587044`

> ## 수록 대상 - 의료기기법, 시행령, 시행규칙 - 식약처 고시 (제조·수입품목허가·신고 등) - 식약처 가이드라인·민원인안내서 - 의료기기 기술문서·임상시험 관련 고시

### kb-eval-20260620-it05-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-06-20", "decision_ref": "kb-eval-20260620-it05-ra_kr-005", "iteration": 5, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "ec020d9f53350bdd", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `ec020d9f53350bdd`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source hash: `1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff`
- Focus: supplementary-response strategy
- Matched keywords: KGMP

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
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

1. Chunk `1012828200772392062`

> II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동일 | **FDA 실사 대상** (구 QSR §820.180(c) 예외 삭제) | NB 불시 감사 대상 | | **8.2.3 공정 모니터링** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.3 부적합 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.4 데이터 분석** | ISO 동일 | ISO 동일 | PSUR/PMSR 작성 근거 데이터 | | **8.5 개선** | ISO 동일 | ISO 동일 | ISO 동일 |

2. Chunk `1037950769042691196`

> MDSAP 수용 (실사 대체 가능) | MDR Annex IX §3.2 — MDSAP 부분 수용 |
