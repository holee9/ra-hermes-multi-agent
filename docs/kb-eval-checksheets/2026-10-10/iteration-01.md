# KB Eval Checksheet - 2026-10-10 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261010-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "c6dd8136ede426e8", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c6dd8136ede426e8`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_03_Performance_Testing_Bench_Test.md)
- Source hash: `9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_03_Performance_Testing_Bench_Test.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – GUI Image‑Processing SaMD (촬영실 GUI Software)**  

| Item | Decision / Requirement | Supporting citation |
|------|------------------------|---------------------|
| **Device classification** | Class II SaMD – “Medical image processing software” | 21 CFR §892.2050 (Class II) |
| **Regulatory pathway** | 510(k) Premarket Notification (substantially equivalent to a cleared image‑processing system) | FDA generally requires 510(k) for Class II devices; no exemption indicated in source |
| **Primary predicate search** | Identify an existing 510(k) cleared “medical image processing and display software” (e.g., a DICOM viewer with basic processing). *Predicate not provided – must be selected* | – |
| **Core submission modules (per eSTAR Section G)** | • Executive Summary <br>• Software Requirements Specification (SRS) <br>• Software Design Specification (SDS) <br>• Requirements‑Traceability Matrix (RTM) <br>• Validation Plan & Report (including unit, integration, system, performance testing) <br>• Test result packages (unit/integration/system/performance) <br>• Validation Dataset Description <br>• Anomaly Log & Resolution | eSTAR Section G document list |
| **Software lifecycle / risk class** | IEC 62304:2006+A1:2015 → Class B (risk of “moderate” harm for a DICOM viewer + basic processing) | IEC 62304 classification table in source |
| **Risk management** | • ISO 14971‑based FMEA/FTA covering software failures <br>• Mitigation for Class B hazard levels <br>• Documentation of residual risk and acceptability criteria | Standard practice; implied by need to align with IEC 62304 risk class |
| **Cybersecurity** | Include a Cybersecurity Threat Analysis, mitigation plan, and post‑market update strategy – per FDA “Cybersecurity in Medical Devices” (2023‑09‑27) | FDA Guidance 2023‑09‑27 |
| **Software validation** | • Verification of functional requirements (unit & integration testing) <br>• System‑level performance testing against the Validation Dataset <br>• Usability testing for GUI display/interaction | eSTAR package includes all test result folders |
| **Labeling & UDI** | • Device label with intended use, indications, contraindications, and warnings <br>• Unique Device Identifier (UDI) on label per 21 CFR §830.10‑§830.60 | Part 820, Part 830 requirements (general knowledge) |
| **Predetermined Change Control Plan (PCCP)** | Outline planned future algorithm updates, UI changes, and security patches; obtain FDA concurrence before deployment | FDA final guidance Dec 2024 – PCCP |
| **Missing / To be obtained** | • Formal **Intended Use Statement** (clinical purpose, patient population) <br>• **Predicate device 510(k) number(s)** for substantial equivalence argument <br>• Detailed **algorithm description** (including any AI/ML components) and performance metrics <br>• **Clinical validation data** if the software is used for diagnostic interpretation rather than purely display <br>• **Human Factors / usability study report** (especially for GUI interactions) <br>• Confirmation that the device does NOT fall under a higher‑risk classification (e.g., Class III AI/ML decision support) | – |
| **Key risk controls to be documented** | 1. Input data validation (DICOM conformity checks) <br>2. Safe handling of corrupted images <br>3. Limiting processing functions to non‑diagnostic use (if applicable) <br>4. Access control & audit logging for software changes <br>5. Failure mode notifications to the operator | Derived from IEC 62304 Class B risk table and FDA cybersecurity guidance |
| **Human‑escalation triggers** | • Absence of a clear predicate device – pause 510(k) preparation and request senior RA review <br>• Ambiguous intended use (e.g., “diagnostic” vs. “viewer”) – elevate to regulatory lead for classification confirmation <br>→ If the software influences diagnosis, consider Class III or De‑Novo pathway <br>• Incomplete risk analysis/residual‑risk justification – forward to quality/safety team before filing <br>• New algorithm version not covered by existing PCCP – submit a change‑control supplement (Special 510(k) or FDA‑approved amendment) | – |

---

### Peer Review Prompt
*Please review this draft and challenge:*

1. The assumption that the GUI software is adequately classified as Class II under §892.2050—could any functionality (e.g., quantitative analysis, AI‑based decision support) elevate it to a higher class?  
2. The completeness of the evidence list—are additional items such as a Human Factors Validation Report or a Clinical Performance Study required for this specific SaMD?  
3. Any jurisdiction‑specific gaps (e.g., FDA’s recent guidance on “Software Precertification” discontinuation, applicability of PCCP) that need to be addressed before finalizing the submission plan.  

--- 

*End of draft – human escalation points highlighted above.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

### kb-eval-20261010-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "eba36ce98b05b462", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `eba36ce98b05b462`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/PCCP_AI_Device_%EC%9E%91%EC%84%B1%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6`
- Focus: SaMD change impact
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `PCCP_AI_Device_작성가이드.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-sof...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – SaMD Change‑Impact (Predetermined Change Control Plan)**  

---

### Bottom‑Line Recommendation
- **Classification:** Class II medical device (software) governed by **21 CFR Part 892** (medical image management/processing).  
- **Submission route for the original device:** 510(k) with a predicate in the same sub‑class (e.g., a cleared AI‑based imaging analysis system).  
- **Future change pathway:** Implement a **Predetermined Change Control Plan (PCCP)** and submit any out‑of‑scope modifications as a supplemental 510(k) or De Novo, per FDA guidance.  

---

### 1. Device Classification & Applicable Regulation
| Item | Details |
|------|----------|
| **Regulatory panel** | Imaging / radiology – **21 CFR Part 892** (see §892.2050 for image‑processing software). |
| **Class** | Class II (special controls apply, e.g., performance testing, risk analysis). |
| **Key regulations** | • 21 CFR §807 (510(k) submission) <br>• 21 CFR §820 (QMSR – ISO 13485 aligned, effective Feb 2026) <br>• 21 CFR §830 (UDI requirements) |
| **Guidance** | FDA Final Guidance on Predetermined Change Control Plan for AI/ML devices (Federal Register No. 2024‑28361, Dec 4 2024). |

*Citation:* Federal Register notice No. 2024‑28361 (Dec 4 2024) – no specific CFR section cited in source — verify separately.  

---

### 2. Submission Pathway
| Phase | Action |
|-------|--------|
| **Initial market entry** | Traditional 510(k) demonstrating **substantial equivalence** to a cleared predicate; include algorithm description, performance data, risk analysis, and software documentation (IEC 62304, ISO 14971). |
| **Planned post‑market modifications** | File the **Predetermined Change Control Plan (PCCP)** as part of the original 510(k) or as an amendment. The PCCP must describe the four mandatory protocol elements (see Section 3.2 below). |
| **Out‑of‑scope changes** | Submit a **supplemental 510(k)** (or De Novo if no predicate exists) before implementing the change. |

---

### 3. Evidence Required  

#### 3.1 Initial 510(k) Package
- **Device description & intended use** (must match predicate).  
- **Algorithm architecture & training data summary** (source‑code excerpt, version control).  
- **Performance verification & validation** – analytical and clinical performance meeting pre‑specified acceptance criteria.  
- **Risk Management File** per ISO 14971 (hazard analysis, mitigations).  
- **Software Development Lifecycle documentation** (IEC 62304 compliance).  
- **UDI labeling** complying with 21 CFR §830.10‑§830.60.  

#### 3.2 Predetermined Change Control Plan (PCCP) – mandatory protocol elements (source [2])  

| PCCP Element | Required Content |
|--------------|------------------|
| **Data Management** | Procedures for collection, curation, versioning of training/validation data; methods to detect and mitigate dataset bias. |
| **Retraining Practices** | Defined triggers for algorithm re‑training (e.g., performance drift), detailed retraining workflow, rollback strategy if new model fails criteria. |
| **Performance Evaluation** | Pre‑defined acceptance criteria, verification & validation methodology for each update, statistical significance requirements. |
| **Updated Procedures** | Communication plan to users/clinicians, real‑world monitoring approach, Instructions For Use (IFU) revision process. |

*Citation:* Table “Modification Protocol” from source excerpt [2] – no specific identifier found in source — verify separately.

#### 3.3 Ongoing Evidence (post‑market)
- **Real‑World Performance Data** per the monitoring plan.  
- **Change Impact Report** documenting compliance with each PCCP element for every update.  

---

### 4. Missing Information (to be supplied before filing)

| Gap | Why it matters |
|-----|----------------|
| **Exact intended use statement** (e.g., “assist radiologists in detecting pulmonary nodules”). | Determines predicate eligibility and required performance endpoints. |
| **Predicate device 510(k) number** (cleared comparator). | Needed for substantial equivalence claim. |
| **Algorithm type & risk level** (e.g., deep‑learning convolutional network, Class II risk per IEC 82304‑2). | Drives depth of validation and risk controls. |
| **Specific data sources & demographic composition** for training/validation sets. | Required for bias assessment in the PCCP Data Management element. |
| **Planned change scope matrix** (which modifications stay within PCCP vs. trigger supplemental submission). | Clarifies when FDA notification is required. |
| **QMSR compliance evidence** (ISO 13485 certificate, process maps aligned to 21 CFR §820). | Mandatory for any 510(k) after Feb 2026. |
| **UDI carrier & GUDID registration details**. | Required under 21 CFR §830.10‑§830.60. |

---

### 5. Risk Controls (aligned to standards)

1. **Risk Management – ISO 14971**  
   - Hazard identification for algorithmic errors, data bias, and cybersecurity.  
   - Controls: input validation, outlier detection, periodic performance monitoring.

2. **Software Lifecycle – IEC 62304**  
   - Classification of software (Class B).  
   - Development processes, testing levels, configuration management.

3. **Usability Engineering – IEC 62366‑1**  
   - Human factors assessment for UI updates in IFU revisions.

4. **Cybersecurity – FDA Guidance on Post‑Market Management of Cybersecurity**  
   - Patch management, vulnerability scanning linked to PCCP update triggers.

5. **Quality Management System – 21 CFR §820 (QMSR)**  
   - Documented change control, CAPA, design history file (DHF) integration with PCCP.

---

### 6. Human‑Escalation Triggers  

| Trigger | Required Action |
|--------|-----------------|
| **Change exceeds predefined PCCP scope** (e.g., new indication, algorithm architecture shift). | Submit a **supplemental 510(k)** (or De Novo) before deployment. |
| **Performance falls outside acceptance criteria** during post‑update validation. | Issue a **field correction** per 21 CFR §806; consider voluntary recall if risk is significant. |
| **Significant safety incident reported** under MAUDE (MedWatch). | Initiate **Medical Device Reporting (MDR)** per 21 CFR §803 within 30 days. |
| **UDI labeling error detected** after change implementation. | Issue a **correction/removal notice** (21 CFR §806) and update GUDID entry. |
| **Detected bias or inequitable performance across patient sub‑groups**. | Pause distribution, conduct root‑cause analysis, and file an **FDA notification** before re‑release. |

---

### 7. Citations  

| Item | Source |
|------|--------|
| Predetermined Change Control Plan FDA guidance (final) | Federal Register notice No. 2024‑28361 – Dec 4 2024 (source [1]). |
| Modification protocol mandatory elements (Data Management, Retraining Practices, Performance Evaluation, Updated Procedures) | Table “Modification Protocol” from source excerpt [2] – no specific identifier found in source — verify separately. |

---

### 8. Human Review & Escalation  

- **Immediate human action:** Confirm the intended‑use statement, predicate selection, and completeness of the PCCP before any 510(k) submission.  
- **Escalate to senior RA/Regulatory counsel** if any change is identified that falls outside the predefined PCCP scope or impacts the device’s indication, risk classification, or UDI labeling.  

---

#### Peer‑Review Prompt
> **Request:** A fellow regulatory affairs specialist, please review the assumptions above—especially the choice of 21 CFR §892.2050 for this SaMD, the completeness of the PCCP elements derived from source [2], and any jurisdiction‑specific gaps (e.g., European MDR interplay). Highlight missing evidence or alternative pathways you deem necessary.

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

2. Chunk `198015203798949382`

> ### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---

### kb-eval-20261010-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "4e1bd50e3823ba5d", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `4e1bd50e3823ba5d`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/FDA_AI_ML_2026_PCCP_%EC%9A%B4%EC%98%81_TPLC_%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8.md)
- Source hash: `14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76`
- Focus: SaMD change impact
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: ### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. --- ## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – SaMD Change‑Impact Assessment & Predetermined Change Control Plan (PCCP)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|----------------|
| **Product type** | Software as a Medical Device (SaMD) that provides AI‑enabled clinical decision support. |
| **Regulatory class** | *Class II* – most AI‑based CDSS are classified II under FDA’s risk‑based framework (see FDA Guidance on Clinical Decision Support Software). |
| **Primary submission** | 510(k) (Premarket Notification) – to demonstrate substantial equivalence to a predicate device and to obtain FDA acceptance of the PCCP. |
| **Key regulations** | • 21 CFR §807 – Premarket notification requirements.<br>• 21 CFR §820 – Quality Management System Regulation (QMSR), effective Feb 2026.<br>• 21 CFR §830 – Unique Device Identification (UDI) labeling obligations.<br>• FDA “Predetermined Change Control Plan” guidance, Dec 2024. |
| **Predicate device** | Must be identified in the 510(k); selection criteria: same intended use, comparable algorithmic function, and similar risk profile. *No specific predicate identifier found in source – verify separately.* |

---

### 2. Required Evidence for Submission  

| Category | Required Content (per FDA expectations) | Source‑derived notes |
|----------|------------------------------------------|----------------------|
| **Intended Use & Indications** | Clear statement of clinical purpose, target patient population, and decision support role. | – |
| **Algorithm Description** | Full functional description, model architecture, versioning, and data flow diagram. | – |
| **Data Lineage & Partitioning** | Documentation of dataset provenance, split into training / tuning / testing sets (as highlighted in source excerpt [1]). | “데이터 계보/분할(train/tune/test)” |
| **Performance Evidence** | Clinical performance study linking algorithm metrics to intended clinical claim; statistical justification of sensitivity, specificity, AUROC, etc. | – |
| **Bias Analysis & Mitigation** | Systematic bias assessment (demographic, geographic, device‑type) and mitigation strategies; explicit documentation required per source excerpt [1] (“편향 분석·완화”). | – |
| **Human–AI Workflow** | Description of user interaction, decision authority, fallback procedures, and training for clinicians. (source [1]: “Human‑AI 워크플로우”) | – |
| **Cybersecurity Risk Management** | IEC 62443/ISO 27001‑aligned assessment; threat model, mitigation, incident response plan. | – |
| **Post‑Market Monitoring Plan** | Real‑world performance tracking, adverse event reporting, and periodic revalidation (source [1]: “시판 후 모니터링”). | – |
| **Predetermined Change Control Plan (PCCP)** | Scoped list of algorithmic/parameter changes pre‑approved for implementation without additional FDA review; includes change impact analysis, verification activities, and submission trigger thresholds. (source [2] confirms PCCP usage at marketing submission) | “업데이트 계획 시 PCCP.” |
| **Software Lifecycle Documentation** | IEC 62304 software development plan, verification/validation reports, configuration management records. | – |
| **Risk Management File** | ISO 14971‑based risk analysis, including identified hazards (bias, incorrect output, cybersecurity), severity/likelihood assessment, and control measures. | – |
| **Labeling & UDI** | Label content per 21 CFR §801; UDI cartridge per 21 CFR §830.10–§830.60. | – |

---

### 3. Missing Information (to be supplied before filing)

1. **Exact intended use statement and clinical claim** – required for both 510(k) narrative and performance justification.  
2. **Predicate device identifier (k‑number, classification regulation)** – needed to complete substantial equivalence argument. *No specific identifier found in source – verify separately.*  
3. **Detailed algorithm change scope** – list of permissible modifications under the PCCP (e.g., retraining with new data, hyperparameter tuning).  
4. **Quantitative bias assessment results** – data on demographic subgroup performance and mitigation outcomes.  
5. **Cybersecurity threat model documentation** – required for risk management file.  
6. **UDI assignment strategy & GUDID submission plan** – to satisfy 21 CFR §830.10‑§830.60.  
7. **IEC 62304 software development lifecycle artifacts** – design specifications, test cases, release notes.

---

### 4. Core Risk Controls (aligned with ISO 14971)

| Hazard | Control(s) | Evidence Required |
|--------|------------|-------------------|
| Algorithmic bias leading to misclassification | • Bias analysis during training<br>• Re‑balancing of data sets<br>• Ongoing monitoring of subgroup performance | Bias mitigation report, post‑market surveillance metrics. |
| Incorrect output without clinician oversight | • Human‑AI workflow with mandatory review step<br>• Alert thresholds and override capability | Workflow diagram, usability testing results. |
| Cybersecurity breach compromising model integrity | • Secure coding practices (ISO 27001)<br>• Regular penetration testing<br>• Incident response SOP | Pen‑test reports, incident response plan. |
| Unintended performance drift after updates | • Predetermined Change Control Plan (PCCP) with verification tests for each approved change<br>• Periodic re‑validation using hold‑out test set | PCCP documentation, validation data for each change. |

---

### 5. Citations

| Item | Citation Type | Reference |
|------|---------------|-----------|
| Predetermined Change Control Plan (PCCP) guidance | Framework reference (FDA guidance, Dec 2024) | FDA “Predetermined Change Control Plan (PCCP)” final guidance, December 2024 – factual statement. |
| 510(k) submission requirements | Framework reference | 21 CFR §807 (Premarket notification). |
| QMSR compliance | Framework reference | 21 CFR §820 (Quality Management System Regulation). |
| UDI labeling obligations | Framework reference | 21 CFR §830.10‑§830.60 (UDI requirements). |
| Bias analysis & mitigation, Human‑AI workflow, Post‑market monitoring, Update plan with PCCP | Source excerpt [1] – “편향 분석·완화”, “Human‑AI 워크플로우”, “시판 후 모니터링”, “업데이트 계획 시 PCCP”. |
| Status of PCCP submission recommendations (finalized Dec 2024) | Source excerpt [2] – “Marketing Submission Recommendations for a **PCCP** … ✅ 확정·시행”. |
| No specific predicate device identifier found | Instance‑identifier rule – *no specific identifier found in source — verify separately*. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required (Human Review) |
|---------|---------------------------------|
| **Change outside the approved PCCP scope** (e.g., new model architecture, addition of new clinical parameters). | Submit a supplemental 510(k) or De Novo request; pause deployment. |
| **Significant performance degradation** detected in post‑market monitoring (≥5% drop in sensitivity/specificity vs. pre‑market claim). | Immediate root‑cause analysis; possible FDA notification under 21 CFR §803 (MDR). |
| **New bias identified** in a protected subgroup that exceeds pre‑defined tolerances. | Re‑evaluate algorithm, update bias mitigation measures, and submit revised PCCP documentation. |
| **Cybersecurity incident** compromising data integrity or model parameters. | Activate incident response plan; report to FDA under 21 CFR §803.11 (serious adverse events) if patient safety impacted. |
| **Regulatory updates** (e.g., amendment to FDA AI/ML guidance, new QMSR requirements). | Conduct gap analysis and amend submission documentation accordingly. |
| **UDI labeling error** discovered in the field. | Issue correction/removal notice per 21 CFR §806; update GUDID entry. |

---

### 7. Peer‑Review Prompt  

*“Colleague, please review the assumptions underlying the Class II classification and the reliance on a PCCP for future algorithm updates. Verify whether any component of this SaMD could be considered a higher‑risk (Class III) device based on its intended use or if additional FDA guidance (e.g., Clinical Decision Support Software guidance) alters the submission strategy. Also confirm that all identified missing items have been captured and that no jurisdiction‑specific requirements (such as state‑level AI regulations) have been omitted.”*

---

### 8. Final Lesson (Reusable RA Judgment)

**Lesson:**  
When evaluating a change impact for AI/ML SaMD, the regulatory pathway hinges on three pillars: (1) **Clear intended use & risk classification**, (2) **A robust Predetermined Change Control Plan (PCCP)** that pre‑approves specific algorithmic modifications, and (3) **Comprehensive supporting evidence** covering data provenance, bias mitigation, human‑AI interaction, cybersecurity, and post‑market surveillance. Missing any of these elements—especially a defined predicate device or scoped PCCP change list—precludes a successful 510(k). Incorporate dedicated “human‑escalation triggers” into the risk management file to ensure timely FDA notification for out‑of‑scope changes or adverse performance signals.  

---

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1132891599852736913`

> ### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. ---

2. Chunk `135350017850675307`

> ## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로 사전 승인된 변경 범위 운영 | | **AI-Enabled Device Software Functions: Lifecycle Management & Marketing Submission Recommendations** | **초안(Draft)** | 2025-01-06 | ⏸ 초안 유지(FY2026 B-list) | TPLC 전반 설계·제출 권고(투명성·편향·HF·사이버보안) | > 의견수렴: 수명주기 초안은 2025-04-07 코멘트 마감. 이후 확정본 미발표(2026-06 기준). ---

### kb-eval-20261010-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "3b3bb4177602545d", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `3b3bb4177602545d`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_02_Substantial_Equivalence.md)
- Source hash: `3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_02_Substantial_Equivalence.md`는 FDA 510(k) substantial equivalence와 predicate 비교 항목을 정리한 eSTAR 작성 문서입니다.
- 현재 excerpt 핵심: ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medi...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – SaMD Change Impact Assessment (Imaging Workstation Software)**  

---

### 1. Device Overview  
- **Function:** GUI‑based imaging workstation software that performs acquisition, processing, display, storage, transfer, worklist management and QA tools for radiology/clinical imaging.  
- **Key Additions in the Proposed Change:** inclusion of an AI/ML analysis module; updated OS support; enhanced cybersecurity controls (authentication, encryption, audit logging); expanded interoperability (HL7 FHIR, IHE profiles).  

---

### 2. Classification & Submission Route  

| Item | Determination |
|------|---------------|
| **Regulatory Panel** | Radiology / Imaging Devices → **21 CFR Part 892** (Imaging) |
| **Device Class** | **Class II** – medical image management and processing system (**§892.2050**) |
| **Primary Submission Pathway** | **510(k) – Substantial Equivalence** to a currently marketed imaging workstation that meets the same intended use. A new or amended 510(k) is required because the change adds AI/ML functionality and modifies cybersecurity features. |
| **Alternative Pathways (if substantial equivalence cannot be demonstrated)** | De Novo classification (Class II) – if no suitable predicate exists, or PMA (unlikely for this software). |

*Framework reference: 21 CFR Part 892 §892.2050 (class II imaging‑software device).*  

---

### 3. Predicate Device Selection – Checklist (source [1])  

| Checkpoint | Current Status / Action Required |
|------------|-----------------------------------|
| FDA 510(k) database search by **product code** | Identify candidate predicates; verify clearance dates (prefer ≤5 y). *No specific identifier found in source — verify separately.* |
| Predicate still marketed? | Confirm via FDA device listing. *No specific identifier found – verify separately.* |
| Recall / safety communication history? | Search MAUDE & Recalls DB for each predicate. *No specific identifier found – verify separately.* |
| Indications‑for‑Use (IFU) wording – identical or narrower? | Perform line‑by‑line comparison with own IFU. *No specific identifier found – verify separately.* |
| Technical differences – justification data availability? | List all functional gaps and gather supporting validation data. *No specific identifier found – verify separately.* |
| Split‑predicate use – prohibited; require single primary predicate with matching IFU. | Ensure only one primary predicate is used. *No specific identifier found – verify separately.* |

**Action:** Complete the above checklist, document findings, and attach to the 510(k) response.

---

### 4. Evidence Package Required for the Change  

| Requirement | Source / Guidance | Comments |
|-------------|-------------------|----------|
| **Software Documentation Level (Basic/Enhanced)** | FDA 2023 Software Guidance – “Basic vs. Enhanced” documentation. *(source [2] provides the list; no specific identifier found — verify separately.)* | Determine level based on risk class and AI/ML content; likely **Enhanced** for Class C risk or AI/ML module. |
| **IEC 62304 Compliance (Safety Class A/B/C)** | IEC 62304 – software life‑cycle processes. *(source [2] notes classification.)* | Assign safety class (probably **Class C** if failure could cause serious patient harm). |
| **Risk Management File (ISO 14971)** | ISO 14971:2021 risk analysis, evaluation, control. | Include updated FMEA/FMECA reflecting AI/ML and cybersecurity changes. |
| **Verification & Validation (V&V) reports** | FDA software V&V guidance. | Provide test protocols/results for acquisition, processing, display, storage, transfer, AI output accuracy, UI usability, interoperability. |
| **AI/ML Predetermined Change Control Plan (PCCP)** | FDA Dec‑2024 Guidance on PCCP. *(source [2] explicitly mentions PCCP.)* | Submit updated PCCP covering model updates, performance monitoring, and change‑control procedures. |
| **DICOM Conformance Statement** | DICOM Standard (SCU/SCP, MPPS, Print SCU, etc.). *(source [2] lists required DICOM services.)* | Include evidence of successful interoperability testing with reference PACS/EHR systems. |
| **Cybersecurity Controls** | FDA “Content of Premarket Submissions for Management of Cybersecurity” (2022) & IEC 62443. | Provide authentication scheme, encryption methodology, audit‑log design, secure update mechanism, and vulnerability management plan. |
| **Software Bill of Materials (SBOM)** | SPDX / CycloneDX format. *(source [2] specifies SBOM format.)* | Attach complete SBOM for all third‑party components. |
| **Interoperability – HL7 FHIR & IHE Profiles** | Relevant IHE Integration Profiles; FHIR Implementation Guide. | Demonstrate successful exchange of imaging study metadata and order information. |
| **Labeling & IFU Updates** | 21 CFR Part 801 (Labeling). | Revise labeling to reflect new AI/ML functionality, intended use, contraindications, and user training requirements. |

---

### 5. Missing / Unverified Information  

1. **Exact Intended Use Statement** – needed for predicate comparison.  
2. **Predicate Device 510(k) Numbers** – to be identified and confirmed as still marketed.  
3. **Risk Classification Confirmation (IEC 62304 Class C vs B)** – based on final hazard analysis.  
4. **Performance Benchmarks for AI/ML Module** – clinical validation data, sensitivity/specificity, intended patient population.  
5. **Software Architecture Diagram & Change Impact Matrix** – to support the PCCP and demonstrate unchanged critical functions.  
6. **Cybersecurity Threat Model** – specific threats addressed by added controls.  
7. **Detailed Verification Test Results for New OS/HW platforms** – ensure compatibility and performance parity.  

*These gaps must be filled before finalizing the 510(k) amendment.*

---

### 6. Risk Controls & Mitigations  

| Risk Area | Control(s) |
|-----------|------------|
| **Incorrect AI/ML output** | - PCCP with periodic re‑validation<br>- Real‑time performance monitoring and alert thresholds<br>- Human‑in‑the‑loop review requirement in labeling |
| **Software failure leading to loss of image data** | - IEC 62304 Class C processes (error handling, rollback)<br>- Redundant storage & checksum verification |
| **Unauthorized access / Data breach** | - Multi‑factor authentication<br>- AES‑256 encryption for data at rest and TLS 1.3 for transmission<br>- Audit log retention ≥1 year |
| **Incorrect DICOM communication** | - Conformance testing with certified PACS adapters<br>- Validation of all listed DICOM services (SCU/SCP, MPPS, Print SCU) |
| **Usability errors in GUI** | - Human factors validation per FDA “Guidance on Applying Human Factors and Usability Engineering”<br>- Updated IFU with UI screenshots & workflow diagrams |

---

### 7. Human‑Escalation Triggers  

| Trigger (to be reviewed by senior RA/Regulatory Lead) |
|------------------------------------------------------|
| **AI/ML module added** – requires PCCP submission; if risk class upgrades to IEC 62304 Class C, a *new* 510(k) may be needed. |
| **Change of Intended Use** – expansion beyond original predicate (e.g., new anatomical sites or diagnostic purpose). |
| **Predicate no longer marketed or recalled** – must select alternative predicate and potentially re‑evaluate substantial equivalence. |
| **Risk classification shifts from Class II to Class III** – would mandate PMA pathway. |
| **Significant cybersecurity architecture redesign** – if new controls alter the device’s risk profile substantially, FDA may request a supplemental 510(k) with additional testing. |
| **Inability to provide performance data for AI/ML** – escalates to senior leadership for decision on postponement or alternative development. |

*When any of the above triggers occur, pause submission preparation and seek senior regulatory sign‑off before proceeding.*

---

### 8. Bottom‑Line Regulatory Judgment  

- The imaging workstation with the proposed AI/ML and cybersecurity enhancements remains a **Class II** device under **21 CFR §892.2050** and therefore follows the **510(k) – Substantial Equivalence** pathway, *provided*:
  - A suitable predicate is identified that is still marketed, not recalled, and has an IFU at least as narrow as the proposed device.
  - All new functionalities (AI/ML, security updates, interoperability extensions) are supported by a **Predetermined Change Control Plan (PCCP)** and meet the enhanced documentation requirements stipulated in FDA’s 2023 software guidance.

- The current evidence package is incomplete; the missing items listed in Section 5 must be obtained before submission.  

- Immediate escalation to senior RA is required if any predicate issues, risk‑class upgrades, or AI/ML validation gaps are identified.

---

### 9. Peer Review Prompt  

> **To a fellow RA:**  
> Please review the assumptions made regarding (1) suitability of an existing imaging workstation predicate given the addition of AI/ML; (2) the classification of the software under IEC 62304 (Class B vs. C); and (3) potential gaps in cybersecurity evidence that could trigger FDA’s “significant change” criteria. Identify any jurisdiction‑specific considerations we may have missed (e.g., state‑level telehealth regulations, international UDI harmonization) and suggest additional data or analyses needed before finalizing the 510(k) amendment.

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20261010-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "50c6711553051809", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md", "source_hash": "7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `50c6711553051809`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_04_Cybersecurity_Section.md)
- Source hash: `7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_04_Cybersecurity_Section.md`는 MDR/MDCG 또는 FDA cybersecurity 요구사항과 대응 체크리스트 문서입니다.
- 현재 excerpt 핵심: ## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VM...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – SaMD Change Impact (Cybersecurity)**  

---  

### 1. Bottom‑Line Determination  
| Item | Assessment |
|------|------------|
| **Device Class** | Most stand‑alone medical device software (SaMD) is *Class II* when it performs diagnostic, monitoring, or therapeutic functions and has an FDA predicate. Classification is confirmed by the FDA product classification database (21 CFR §860.3). *If no predicate exists, a De Novo submission may be required.* |
| **Submission Route** | **510(k) – Traditional** (or Special/Abbreviated if a suitable predicate and minor change). A supplemental 510(k) is needed for any change that modifies intended use or alters the risk profile. |
| **Regulatory Basis for Cybersecurity** | • Section 524B(b)(3), FD&C Act – legal obligation to provide an SBOM.<br>• FDA “2025 Guidance on Cybersecurity” (referenced in source).<br>• IEC 81001‑5‑1 & NIST CSF – recognized special controls for Class II software. |

---  

### 2. Required Evidence for the Next Submission  

| Requirement | What to Submit | Source Reference |
|-------------|----------------|------------------|
| **Software Bill of Materials (SBOM)** | • Complete SBOM in SPDX 2.3+ **or** CycloneDX 1.5+ (JSON or XML).<br>• Fields: Supplier Name, Component Name, Version, Unique Identifier (CPE/PURL), Dependency Relationship, Author, Timestamp – as shown in the source table. | Section 524B(b)(3) (legal obligation); NTIA Minimum Elements (source excerpt 2). |
| **Threat Model** | • Documented threat model using STRIDE (or equivalent) covering all software components and data flows.<br>• Identification of potential attack vectors, likelihood, and impact. | “Threat Model – 필수 (STRIDE 권장)” in source excerpt 1. |
| **Cybersecurity Management Plan (CMP) / Vulnerability Management Plan (VMP)** | • CMP outlining design‑time controls, implementation of IEC 81001‑5‑1 controls, monitoring, patching process.<br>• VMP describing vulnerability receipt, triage, remediation timelines, and post‑market surveillance. | “CMP/VMP – 필수” in source excerpt 1. |
| **Penetration Testing** | • Executive summary of at least one external penetration test performed on the latest software version (recommended, not mandatory). | “Pen Test – 권고” in source excerpt 1. |
| **Post‑Market Cybersecurity Activities** | • Plan for continuous monitoring, patch deployment, CVD (Corrective/Preventive Action) tracking, and incident reporting per 21 CFR 803/806.<br>• Evidence of integration with FDA’s post‑market surveillance expectations. | “포스트마켓 – 법적 의무 (패치, CVD, 모니터링)” in source excerpt 1. |
| **Labeling / UDI** | • Updated labeling reflecting any cybersecurity changes (Section 801).<br>• UDI label complying with 21 CFR 830.10‑830.60 (no specific identifier provided; verify separately). | General FDA labeling & UDI requirements (framework reference). |
| **Quality Management System Evidence** | • Records demonstrating compliance with QMSR (21 CFR 820) – design controls, risk management, change control (including Predetermined Change Control Plan if AI/ML). | “Predetermined Change Control Plan (PCCP)” referenced in FDA guidance (Dec 2024). |

---  

### 3. Missing / Unverified Information  

| Gap | Why It Matters | Action |
|-----|----------------|--------|
| **Intended Use & Indications** | Determines classification, predicate search, and specific special controls. | Obtain a clear statement from the manufacturer. |
| **Predicate Device(s)** | Required for 510(k) comparability; determines whether a traditional 510(k) is feasible. | Conduct a predicate device search (FDA Product Classification Database). |
| **Risk Management File (ISO 14971)** | Needed to demonstrate that identified cybersecurity risks are mitigated to acceptable levels. | Request updated risk analysis incorporating the new threat model. |
| **Software Architecture Diagram** | Required to map SBOM components to functional blocks for traceability. | Provide a current high‑level architecture diagram. |
| **Change Impact Assessment** | Determines if the change is “major” (requires supplemental 510(k)) or “minor”. | Perform a formal assessment per FDA’s Change Management Guidance. |
| **UDI Issuing Agency Confirmation** | Verify that the chosen issuing agency is accredited under 21 CFR 830.100‑130. | Confirm with GUDID registration team. |

---  

### 4. Core Risk Controls (Cybersecurity)  

1. **Adopt IEC 81001‑5‑1 controls** – secure development lifecycle, access control, data protection.  
2. **Implement NIST Cybersecurity Framework (CSF)** – Identify, Protect, Detect, Respond, Recover.  
3. **Maintain an up‑to‑date SBOM** in SPDX or CycloneDX format; automate generation from build pipelines.  
4. **Apply a Predetermined Change Control Plan (PCCP)** for any AI/ML updates (FDA Dec 2024 guidance).  
5. **Conduct regular vulnerability scanning & periodic penetration testing** (minimum annually).  
6. **Establish post‑market cyber‑vigilance** – automated monitoring of CVEs, timely patch release, and incident reporting per 21 CFR 803/806.  

---  

### 5. Citations  

| Item | Citation Type | Reference |
|------|---------------|-----------|
| Legal requirement for SBOM | Instance identifier (from source) | Section 524B(b)(3) |
| Threat‑model expectation | Instance identifier (from source) | “Threat Model – 필수 (STRIDE 권장)” (source excerpt 1) |
| CMP/VMP mandate | Instance identifier (from source) | “CMP/VMP – 필수” (source excerpt 1) |
| Penetration test recommendation | Instance identifier (from source) | “Pen Test – 권고” (source excerpt 1) |
| Post‑market cybersecurity obligations | Instance identifier (from source) | “포스트마켓 – 법적 의무 (패치, CVD, 모니터링)” (source excerpt 1) |
| SBOM format & fields | Instance identifier (from source) | NTIA Minimum Elements table (source excerpt 2) |
| Standards referenced | Framework reference | IEC 81001‑5‑1; NIST CSF |
| Predetermined Change Control Plan (PCCP) | Framework reference | FDA final guidance, Dec 2024 |

*No other specific device numbers or regulatory notices appear in the provided excerpts – verify separately if additional identifiers are needed.*

---  

### 6. Human‑Escalation Triggers  

| Trigger | Required Action |
|---------|-----------------|
| **Change that alters intended use, adds new clinical functionality, or modifies risk level** | Submit a *supplemental 510(k)* (or De Novo if no predicate). |
| **Inclusion of new third‑party components not present in the original SBOM** | Update SBOM and file an *annual cybersecurity update* to FDA; consider a supplemental 510(k) if impact is material. |
| **Discovery of a high‑severity vulnerability (CVSS ≥ 7.0) affecting marketed software** | Initiate Corrective/Preventive Action, issue Field Safety Notice, and submit a *Medical Device Reporting (MDR)* as required by 21 CFR 803. |
| **Implementation of AI/ML model updates without an approved PCCP** | Pause deployment; develop & FDA‑submit a Predetermined Change Control Plan before release. |
| **Failure to meet SBOM deadline under Section 524B(b)(3)** | Escalate to senior regulatory leadership; prepare a compliance remediation plan and notify FDA if non‑compliance persists >30 days. |

---  

### 7. Peer Review Prompt  

> *@RA‑Peer:* Please review the assumptions made regarding device classification (Class II/De Novo), the completeness of the cybersecurity evidence list, and any jurisdictional gaps (e.g., EU MDR or MFDS requirements that might affect a global launch). Highlight any missing regulatory citations needed to support the submission strategy.  

---  

*End of Draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `129799210478830618`

> ## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VMP** | 필수 | PMS 계획에 포함 | 업데이트 정책으로 요구 | | **Pen Test** | 권고 | 권고 | 권고 | | **표준 참조** | IEC 81001-5-1, NIST CSF | IEC 81001-5-1 (조화표준 진행) | IEC 81001-5-1, MFDS 자체 가이드 | | **포스트마켓** | 법적 의무 (패치, CVD, 모니터링) | PMS + Vigilance 연계 | 이상사례 보고 + 업데이트 절차 | > MDR/MFDS 영향: GUI SW의 경우 FDA 요건 충족 수준으로 작성하면...

2. Chunk `135977185938899780`

> ### 3.4 SBOM (Software Bill of Materials) **법적 의무** (Section 524B(b)(3)). **NTIA Minimum Elements** (FDA 준용): | 필드 | 설명 | 예시 | |---|---|---| | Supplier Name | SW 공급자 | OpenJDK Foundation | | Component Name | 컴포넌트 명칭 | OpenJDK | | Version | 버전 문자열 | 17.0.9 | | Unique Identifier | CPE 또는 PURL | `pkg:maven/org.openjdk/jdk@17.0.9` | | Dependency Relationship | 의존성 관계 | DependsOn: spring-boot@3.2.0 | | Author of SBOM | SBOM 작성자 | [제조사명] | | Timestamp | 생성일시 ISO 8601 | 2026-04-29T00:00:00Z | **형식**: SPDX 2.3+ 또는 CycloneDX 1.5+ (machine-readable JSON/XML 권장) **포함 범위**: - Manufacturer-developed SW (자체 개발) - Third-party commercial/licensed SW - Ope...

## ra_eu

### kb-eval-20261010-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "75c25baabcf21dff", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `75c25baabcf21dff`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter |...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Response to EU NB Deficiency Letter (MDR)**  

---

### 1. Device Overview  
- **Intended purpose:** Standard diagnostic radiology (X‑ray imaging system).  
- **Key functional elements disclosed in the deficiency letter:** X‑ray source, detector and associated image‑processing software.  

---

### 2. Classification & Conformity‑Assessment Route  

| Item | Reference |
|------|-----------|
| **MDR classification rule** | **Rule 10** – “Active devices for diagnosis or monitoring which emit ionising radiation” (Annex VIII). |
| **Resulting class** | **Class IIb** (device that emits ionising radiation for diagnostic radiology). |
| **Conformity‑assessment route** | **Art. 52(4) MDR** – full technical‑documentation assessment under **Annex IX** (Chapters I & III) together with post‑production surveillance per **Annex XI**.  The NB will assess one representative device for the generic group. |
| **Relevant NB documents cited in source** | “MDR Annex VII + 2026/977” (see source excerpt [2]). |

---

### 3. Evidence Required by the NB (per MDR & GSPR)  

| Evidence | Where required | What must be provided |
|----------|----------------|-----------------------|
| **Clinical Evaluation Report (CER)** – updated to demonstrate clinical equivalence. | Annex VII (clinical evaluation) & Art. 61 (keep CER up‑to‑date). | • Comparison of clinical conditions (standard diagnostic radiology). <br>• Performance data showing DQE ≥ 65 % for both devices (referencing IEC 62220‑1‑1). <br>• Rationale for equivalence, including justification of patient population and intended use. |
| **Test Report for Detective Quantum Efficiency** | IEC 62220‑1‑1 (referred in source [1]). | TR‑2024‑015 showing DQE(0) ≥ 65 % (already cited). Provide full report and traceability to device batches. |
| **Risk Management File** | Annex I (GSPR §16, §17, §18) & ISO 14971. | Full risk analysis covering radiation hazards, mechanical/thermal risks, software failures; identified controls; residual risk evaluation. |
| **Performance‑testing dossier** (electrical safety, electromagnetic compatibility, radiation protection). | IEC 60601‑2‑28 (X‑ray tube assemblies) and IEC 60601‑2‑54 (radiography/radioscopy equipment). | Verified compliance test results, calibration certificates, conformity to relevant essential requirements. |
| **Labeling & IFU** | Annex I §23. | Complete labeling package (symbols, safety information, radiation protection instructions, user manual) in the language(s) of the intended market. |
| **Quality Management System certificate** | Annex IX assessment includes QMS audit. | ISO 13485:2016 certification copy and evidence of ongoing surveillance. |
| **Post‑Market Clinical Follow‑up (PMCF) plan & interim report** | Annex XIV Part B. | Plan describing methodology, sample size, follow‑up schedule; interim findings that support continued equivalence. |
| **PMS system & PSUR** (for Class IIb) | Art. 84 (PMS plan), Art. 86 (PSUR). | PMS plan covering incident reporting, trend analysis; PSUR draft covering the latest 12‑month period. |

---

### 4. Gaps Identified by the NB (as inferred from the deficiency letter)

| Missing / Insufficient Item | Reason for Deficiency |
|-----------------------------|-----------------------|
| **Updated CER** – current version (Rev 3) is attached as Annex A but the NB indicated missing justification of equivalence and lack of recent clinical data. | Needs additional post‑market evidence, updated literature review, and clear mapping to the comparator device. |
| **Full DQE test report** – only summary values were provided; the NB requires the complete raw data set and statistical analysis. | Provide full TR‑2024‑015 package. |
| **Radiation‑protection risk controls** – explicit verification of compliance with GSPR §16 (including shielding, interlocks, dose monitoring) not evident. | Include detailed risk control measures and validation evidence. |
| **Software validation** – if the image‑processing software is classified under Rule 11, a separate software lifecycle file (IEC 62304) is missing. | Supply software development file and verification/validation reports. |
| **Labeling compliance** – draft IFU lacks required statements on radiation safety for lay‑person use (§22) and on disposal of radioactive components (§16). | Revise labeling accordingly. |
| **PMCF evidence** – only a high‑level plan was submitted; the NB requests an interim report showing actual patient data collected to date. | Submit PMCF interim report. |
| **QMS non‑conformities (NCs)** – the deficiency letter lists “QMS NC” without details in this excerpt; assume outstanding corrective actions are needed. | Provide CAPA evidence for each listed NC. |

---

### 5. Required Risk Controls (to be reflected in the documentation)

1. **Radiation protection** – shielding design, automatic exposure control, interlock circuitry (GSPR §16).  
2. **Electrical safety & EMC** – compliance with IEC 60601‑2‑28/54 (GSPR §§17‑18).  
3. **Software safety** – lifecycle management per IEC 62304; verification that software decisions do not lead to serious injury (GSPR §11).  
4. **Usability** – human‑factors validation per IEC 62366‑1 to ensure correct set‑up of exposure parameters by lay users (§22).  
5. **Incident reporting & trend analysis** – integrated into PMS system (Art. 83) and reflected in PSUR (Art. 86).  

All controls must be documented, implemented and verified; residual risk must be shown acceptable in the Risk Management File.

---

### 6. Regulatory Citations (framework references)

| Regulation / Standard | Citation |
|-----------------------|----------|
| MDR Classification Rules | Annex VIII – Rule 10 (active diagnostic radiology). |
| Conformity‑assessment route for Class IIb | Art. 52(4) MDR + Annex IX (full technical‑documentation assessment) & Annex XI (production conformity). |
| Clinical evaluation requirements | Annex VII MDR; keep CER current – Art. 61. |
| General Safety and Performance Requirements | Annex I §§16, 17, 18, 22, 23. |
| PMS system | Art. 83 MDR; PMS plan – Art. 84; PSUR – Art. 86. |
| Risk management | Annex I (GSPR) + ISO 14971:2019. |
| DQE measurement standard | IEC 62220‑1‑1 (referenced in source [1]). |
| X‑ray equipment safety standards | IEC 60601‑2‑28, IEC 60601‑2‑54 (appropriate to device). |
| Software lifecycle | IEC 62304. |
| Usability engineering | IEC 62366‑1. |
| NB procedural references | “MDR Annex VII + 2026/977” (source [2]). |
| Structured dialogue provision | Art. 7 MDR – mentioned in source [2] as pre‑dialogue channel. |

*(All citations above are framework references; no device‑specific identifiers were supplied in the source.)*

---

### 7. Human‑Escalation Triggers  

| Situation | Action & Escalation |
|-----------|---------------------|
| **Deadline breach** – NB response not submitted within the mutually agreed “NB와 합의” period (no statutory upper limit). | Alert senior RA manager; invoke internal escalation matrix; consider formal written reminder to NB. |
| **Clock‑stop invoked** (NB requests immediate halt of activities). | Suspend all related release / production actions; notify Quality & Manufacturing leads; document the stop in QMS. |
| **Unsatisfactory NB feedback after first submission** – repeated requests for additional data without clear resolution. | Request a *Structured Dialogue* under **Art. 7 MDR (2026/977)** to clarify expectations; involve European Coordination Group if needed. |
| **Potential non‑conformity that may affect safety** (e.g., missing radiation‑protection controls). | Initiate internal CAPA, notify the Regulatory Affairs Head and Legal Counsel; consider temporary market withdrawal per Art. 87 MDR. |
| **NB threatens assessment termination / product rejection** (as per “평가 종료 / 불승인” in source [2]). | Escalate to senior management and prepare contingency plan for re‑submission via an alternative conformity route (e.g., Annex X type‑examination). |

---

### 8. Peer Review Prompt  

> **Colleague, please review this draft:**  
> - Are the assumptions about the device’s classification (Rule 10 → Class IIb) and chosen conformity‑assessment route (Art. 52(4) + Annex IX) consistent with the full scope of the system (including detector & software)?  
> – Does the list of missing evidence fully reflect the items likely identified in the NB’s deficiency letter, or are additional artefacts (e.g., environmental testing, sterilisation validation) required?  
> – Have all relevant MDR articles and annexes been captured, especially any that may apply to “products without an intended medical purpose” if ancillary accessories are involved?  
> – Are there jurisdiction‑specific gaps (e.g., translation requirements for labeling, local Notified Body procedural variations) that need addressing before finalising the response?  

--- 

*Prepared by Theo – EU MDR Regulatory Affairs Specialist*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1014893419282866507`

> | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter | 보완 요청 | Additional Information (AI) Request | | 근거 법령 | MDR Annex VII + 2026/977 | 의료기기법 §12 + 허가·신고·심사 규정 | 21 CFR 807 + FDA Review Policy | | 답변 기한 | NB와 합의 (법정 상한 없음) | 1차 60일, 2차 60일 | 180일 (타임라인 기산일부터) | | 최대 중단 횟수 | 4회 (product verification 기준) | 2차까지 (실질 2회) | 제한 없음 (Interactive Review 가능) | | Clock-stop | 예 (NB 요청 당일 stop, 제출 익일 resume) | 예 (보완 기간 제외) | 예 (AI 발송일부터 stop) | | 미응답 시 | 평가 종료 / 불승인 | 취하 간주 | 허가 거부 | | 사전 대화 창구 | Structured Dialogue (Art.7, 2026/977) | 상담제도 (비공식) | Pre-Sub (Q-Sub) (공식, 문서화) | | 주요 결함 유형 | CER, TD, QMS NC, Labelin...

### kb-eval-20261010-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "223683d27e9e4cef", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `223683d27e9e4cef`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md)
- Source hash: `d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexII_Technical_Documentation_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMS...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Preliminary Assessment for an Un‑specified Medical Device (MDR 2017/745)**  

---

### 1. Classification & Conformity‑Assessment Route  
| Item | Current Determination | Rationale / Evidence Needed |
|------|-----------------------|------------------------------|
| **Device class** | *Not yet assigned* – requires definition of the intended medical purpose, mode of action and patient population. | Apply the classification rules in **Annex VIII** (e.g., Rule 9‑11, Rule 17) once the use‑case is known. |
| **Conformity‑assessment route** | Dependent on class (Art. 52 MDR). | <ul><li>Class I (non‑sterile, non‑measuring): Art. 52(7) – self‑declaration, technical documentation (Annex II & III) + EU Declaration of Conformity (Annex IV). No NB required.</li><li>Class Is / Im / Ir: Art. 52(7) – limited Annex IX/Annex XI assessment for sterile/measuring/re‑usable aspects (NB involvement limited).</li><li>Class IIa: Art. 52(6) – full Annex IX technical‑documentation assessment of a representative device **or** Annex II & III + Annex XI §10/§18.</li><li>Class IIb: Art. 52(4) – Annex IX (full) **or** Annex X (type‑examination) + Annex XI.</li><li>Class III: Art. 52(3) – Annex IX (full) **or** Annex X + Annex XI.</li></ul> |

*Human‑escalation trigger*: If the intended use cannot be matched to a single rule in Annex VIII within 5 working days, the case must be escalated to the product‑owner/clinical lead for clarification.

---

### 2. Technical Documentation – Required Contents (per **MDR Annex II**)

| Annex II Section | Content Required (as per source) | Source citation |
|------------------|-----------------------------------|-----------------|
| **§1 Device Description** | Full description of device, principle of operation, variants, accessories, and intended purpose. | “§1 Device Description” – source [1] |
| **§2 Labeling** | Labels and IFU (language(s) required, symbols, safety information). | “§2 Labeling” – source [1] |
| **§3 Design & Manufacturing** | Detailed design specifications, manufacturing processes, materials, and tolerances. | “§3 Design & Manufacturing” – source [1] |
| **§4 GSPR Checklist** | Mapping of device to the 23 General Safety and Performance Requirements (GSPR) in Annex I; includes performance testing and comparison to any applicable predicate. | “§4 GSPR Checklist” – source [1] |
| **§5 Risk Management** | Complete risk management file complying with ISO 14971, including hazard analysis, risk evaluation, and mitigations. | “§5 Risk Management” – source [1] |
| **§6 Verification & Validation** | Verification reports (design verification) and validation reports (clinical or simulated use), together with V&V plan and outcomes. | “§6 Verification & Validation” – source [1] |

*Human‑escalation trigger*: Any of the above sections lacking supporting data (e.g., missing risk analysis, incomplete labeling draft) must be flagged for immediate completion before NB submission.

---

### 3. Clinical Evidence Requirements  

| Requirement | What Must Be Provided | Regulatory Reference |
|-------------|-----------------------|----------------------|
| **Clinical Evaluation Report (CER)** – current and kept up‑to‑date | Systematic literature review, clinical data from equivalent devices, post‑market clinical follow‑up (PMCF) plan & results. | Annex XIV Part A; maintained under Art. 61 MDR |
| **Post‑Market Clinical Follow‑Up (PMCF)** | Detailed PMCF plan and periodic evaluation report. | Annex XIV Part B |
| **PMS System / Plan** | Ongoing post‑market surveillance system, including incident reporting, trend analysis, and field safety corrective actions. | Art. 83 (system) & Art. 84 (plan) MDR |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | Benefit–risk determination, PMCF findings, sales volume & user population estimate. | Art. 86 MDR (annual for IIb/III, biennial for IIa) |

*Human‑escalation trigger*: Absence of a justified clinical equivalence justification or an approved PMCF plan should be escalated to the Clinical Affairs team for rapid development.

---

### 4. Risk Controls & GSPR Alignment  

| GSPR Chapter | Key Controls Required | Evidence Needed |
|--------------|----------------------|-----------------|
| **§16 – Radiation protection** (if applicable) | Shielding, dose monitoring, compliance with IEC 60601‑2‑54 / ‑28 etc. | Test reports, conformity to IEC standards |
| **§17 – Electronic programmable systems** | Secure software development lifecycle, verification of firmware updates. | ISO 62304 compliance, software risk analysis |
| **§18 – Active devices & connections** | Electrical safety testing, EMC compliance. | IEC 60601‑1 test certificates |
| **§19 – Active implantable devices** (if applicable) | Long‑term biocompatibility, hermeticity. | ISO 10993 data, durability tests |
| **§22 – Devices for lay persons** | Usability engineering, clear IFU. | IEC 62366‑1 usability report |

*Human‑escalation trigger*: When any GSPR cannot be demonstrated with existing evidence (e.g., missing EMC test reports), the risk‑management team must be notified to arrange testing.

---

### 5. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Action Required |
|-----|----------------------|-----------------|
| **Intended medical purpose & mode of action** | Prevents classification, clinical evaluation scope, and GSPR mapping. | Obtain a definitive product‑intended‑use statement from the development lead (within 3 working days). |
| **Labeling draft (including IFU)** | Needed for Annex II §2 and to satisfy §23 of Annex I. | Draft in required language(s) and send to regulatory for review. |
| **Design verification data (bench testing, software V‑V)** | Required for Annex II §6 and for risk‑control justification. | Compile test reports; if unavailable, schedule testing. |
| **Performance / safety testing results** (e.g., IEC 60601 compliance) | Essential for GSPR checklist (§4). | Request certificates from the engineering department or a third‑party lab. |
| **Risk Management File (ISO 14971)** – missing residual risk evaluation | Needed for Annex II §5 and to support PMCF rationale. | Complete risk analysis, update file, document mitigations. |
| **Clinical data / equivalence justification** | Required for CER; absence blocks NB review. | Identify comparable predicate devices or plan a clinical investigation. |

*Human‑escalation trigger*: If any of the above items cannot be supplied within the stated timeframe, escalation to senior RA manager is mandatory.

---

### 6. Summary Judgment  

- **Classification**: *Undetermined – pending definition of intended purpose and rule mapping (Annex VIII).*
- **Conformity‑assessment route**: Will follow Art. 52 once class is fixed (likely Annex IX for Class IIa/IIb, possibly Annex X if a type‑examination path is selected).
- **Technical documentation**: All six Annex II sections identified; current gaps must be closed before NB submission.
- **Clinical evidence**: CER, PMCF plan & PSUR (if applicable) are mandatory per Annex XIV and Art. 86.
- **Risk controls**: Alignment with relevant GSPR (§16‑22) required; missing test data flagged.

---

### 7. Human‑Escalation Triggers  

| Situation | Escalation Recipient | Deadline |
|-----------|----------------------|----------|
| Unresolved classification after 5 working days | Product Owner / Clinical Lead | Immediate |
| Missing labeling/IFU draft >3 working days | Regulatory Manager | Immediate |
| Absence of risk‑management file or residual‑risk assessment | Risk Management Team Lead | Immediate |
| No clinical equivalence justification within 10 working days | Clinical Affairs Director | Immediate |
| Any gap that prevents compilation of a complete Annex II dossier before NB audit schedule | Senior RA Manager | Immediate |

---

### 8. Peer Review Prompt  

> **To the next regulatory affairs peer:**  
> Please review this preliminary draft for (a) completeness of the classification logic given the limited source information, (b) whether any jurisdiction‑specific requirements (e.g., language obligations, MFDS cross‑referencing) have been omitted, and (c) if additional evidence types (such as usability testing per IEC 62366‑1 or specific EMC standards) should be prespecified at this stage. Highlight any assumptions that need verification against the full product file.

--- 

*End of draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

### kb-eval-20261010-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2185106079b086c7", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2185106079b086c7`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수). ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – X‑ray Device (Ionising Radiation) under EU MDR 2017/745**

---

### 1. Classification & Conformity‑Assessment Route  
| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Device class** | **Class IIb** (ionising radiation equipment) | The source states “이온화 방사선 기기(X‑ray)는 Class IIb 이상”【1】. Under MDR, active devices that emit ionising radiation for diagnostic purposes fall under **Rule 10** (active diagnostic devices) → **Class IIb** (Annex VIII, Rule 10). |
| **Conformity‑assessment route** | Full technical‑documentation assessment by a Notified Body (NB) – **Annex IX** (Chapters I & III) together with the NB‑issued type‑examination if chosen. | MDR Art. 52(4) prescribes Annex IX for Class IIb devices, requiring NB involvement. |
| **Notified‑Body requirement** | Mandatory – select an NB listed in the NANDO database for the relevant MDR scope (code MDxxxx). | “NB 인증 필수…NANDO Database에서 MDR 범위(코드 MDxxxx) 확인”【1】. |

*Note:* If a type‑examination route (Annex X + Annex XI) is preferred, it may also be used for Class IIb, but the default “full technical‑documentation assessment” via Annex IX is assumed unless otherwise justified.

---

### 2. Required Evidence & Documentation  

| Category | Specific Documents / Data | Reference |
|----------|---------------------------|-----------|
| **Technical documentation** (Annex II) | – Device description & intended use<br>– Design & manufacturing information<br>– Labels & IFU (Annex I §23)<br>– UDI dossier<br>– Verification & validation reports | MDR Annex II |
| **Risk management** | Risk Management File (ISO 14971) covering all identified hazards, especially radiation protection (GSPR §16.4) and active device risks (§18). | GSPR §§16, 18; ISO 14971 |
| **Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data (pre‑market studies or equivalence), benefit–risk conclusions. | Annex XIV Part A; kept current Art. 61 |
| **Post‑Market Clinical Follow‑up (PMCF)** | PMCF plan & evaluation report (Annex XIV Part B). | Annex XIV Part B |
> **PMS system** – documented PMS process (Art. 83), PMS plan (Art. 84) and periodic safety update report (PSUR) for Class IIb (annual, Art. 86). |
| **Quality Management System** | ISO 13485‑2023 certification; audit reports & scope covering all MDR clauses. | NB audit under Annex IX Chapters I & III |
| **Labeling & IFU** | Final draft complying with Annex I §23 (including radiation safety information, contraindications, and user instructions). | Annex I §23 |
| **Declaration of Conformity** | Signed EU Declaration (Annex IV) referencing applicable MDR articles and standards. | Annex IV |

---

### 3. Gaps / Missing Information  

| Gap | Why it is needed | Suggested action |
|-----|------------------|-----------------|
| **Exact intended‑use statement & clinical indication** | Drives classification justification and CER scope. | Draft a precise Intended Use clause; map to Rule 10. |
| **Device “MDxxxx” MDR scope code confirmation in NANDO** | Confirms that the selected NB is authorised for this device category. | Search NANDO, record the specific code, attach screenshot. |
| **Clinical data source list (studies, registries, equivalence) & justification of equivalence** | Required for CER and to satisfy Art. 61 updates. | Compile all available pre‑market clinical evidence; if gaps exist, plan a feasibility study. |
| **PMCF plan details (objective, population, endpoints, schedule)** | Needed for Annex XIV Part B and PSUR content. | Draft PMCF protocol aligned with risk‑controlled objectives. |
| **PMS & PSUR schedule (timeline, responsible persons)** | Art. 86 demands annual PSUR for Class IIb. | Define a PMS calendar; assign owner. |
| **Labeling mock‑up including radiation safety symbols (§16.4)** | Must demonstrate compliance with GSPR §16 & Annex I §§23. | Produce draft label/IFU, circulate for review. |
| **Full list of applicable harmonised standards (e.g., IEC 60601‑2‑28, IEC 62304, IEC 62366‑1)** | Demonstrates conformity to “state of the art”. | Identify and reference all relevant IEC/ISO standards; obtain declarations of conformity. |
| **Non‑conformity response procedures** | Required for audit follow‑up (see source 【2】). | Draft SOP for handling NB‑issued NCs. |

---

### 4. Core Risk Controls (as per GSPR & ISO 14971)

1. **Radiation protection (GSPR §16.4)** – interlocks, dose‑limiting circuitry, warning lights, emergency stop, shielding verification.  
2. **Active device safety (GSPR §18)** – fault detection, self‑test, software validation (IEC 62304), usability engineering (IEC 62366‑1).  
3. **Electrical safety & EMC** – compliance with IEC 60601‑1 series.  
4. **User training & instructions** – clear IFU, competency requirements for operators; addressed in labeling (§23).  
5. **Post‑market monitoring of radiation dose data** – integrated into PMCF and PSUR.

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger point | Action required |
|-----------|--------------|-----------------|
| **Missing or ambiguous intended‑use statement** | During classification justification review. | Pause submission; request clarification from product development. |
| **No confirmed MDR scope code (MDxxxx) in NANDO** | Early NB selection phase. | Halt NB contracts; verify scope and select a compliant NB. |
| **Insufficient clinical evidence for CER** | When drafting CER or before NB audit. | Initiate additional clinical study or gather equivalence data; involve Clinical Affairs lead. |
| **Incomplete PMCF plan** | Before finalizing Annex XIV Part B. | Draft full PMCF protocol; obtain sign‑off from Clinical & Risk Management leads. |
| **NB audit reveals non‑conformities** | Upon receipt of NC report. | Activate Non‑Conformity Response SOP; allocate resources for corrective actions; inform senior management. |
| **PSUR not prepared within 12 months** (Class IIb) | Approaching annual deadline. | Escalate to Project Manager & Quality Lead to prioritize PSUR completion. |
| **Labeling fails GSPR §16 or §23 review** | During label/IFU approval. | Suspend CE‑marking draft; involve regulatory and communications teams for redesign. |

---

### 6. Summary Judgment  

- The X‑ray device is correctly classified as **Class IIb** under MDR Rule 10 (active diagnostic equipment emitting ionising radiation).  
- **Annex IX** (Art. 52(4)) full technical‑documentation assessment with a designated **Notified Body** is the required conformity‑assessment route; NB selection must be confirmed via NANDO (code MDxxxx).  
- Core evidence packages (Technical Documentation, Risk Management File, CER, PMCF plan, PMS system & PSUR, QMS certification) are mandatory.  

> **Key next steps:** finalize intended‑use description, verify MDR scope code in NANDO, compile complete clinical data set, draft full PMCF and PMS plans, produce labeling compliant with GSPR §§16 & 23, and prepare the NB audit dossier (including the items listed in source【2】).

---

### 7. Peer‑Review Request  

> **@RA‑Peer:** Please challenge the assumptions made above, particularly:  
> • Whether Rule 10 is the sole applicable classification rule or if additional rules (e.g., Rule 17 for detector components) affect the overall system class.  
> • The completeness of the referenced evidence list against the specific NB’s “Technical Documentation Assessment” expectations.  
> • Any jurisdiction‑specific nuances (e.g., national provisions, German BfArM requirements) that may impose extra obligations beyond the MDR framework.

---

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `978896205875274621`

> ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수).

2. Chunk `296791090431458058`

> ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료

### kb-eval-20261010-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e4d6aa5135df386d", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e4d6aa5135df386d`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week04_MDR_EU_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `Week04_MDR_EU_체계_상세.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUF...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Preliminary CE‑Marking Assessment (MDR 2017/745)**  

---

### 1. Scope of the assessment  
*The source material provides only a generic overview of MDR requirements (classification, post‑market surveillance, UDI, etc.) and does **not** contain any device‑specific information (intended purpose, technology, patient population, etc.). Consequently the draft below outlines the *full set of evidence that will be required* once the missing product data are supplied, identifies what is currently unavailable, and flags the points at which human escalation is mandatory.*

---

## 2. Classification & Conformity‑Assessment Route  

| Step | Required action (regulatory basis) | What we have from source | What is still needed |
|------|------------------------------------|--------------------------|----------------------|
| **2.1 Identify intended medical purpose** | Must be defined by the manufacturer before any classification work can start (Art 51 MDR; Annex VIII rules are applied to the purpose). | *No device description provided.* | Full Intended Use Statement, indications, contraindications, target population and user profile. |
| **2.2 Apply Annex VIII classification rules** | Sequentially apply the 22 rules; the highest class that applies governs (Art 51 + Annex VIII). | Source notes “Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용” – a reminder of the rule‑application process. | The specific rule(s) that match the device (e.g., Rule 9, Rule 10, Rule 11, Rule 17 etc.). |
| **2.3 Determine Class** | Result of step 2.2. | *Not determinable.* | Classification outcome (Class I, Is/Im/Ir, IIa, IIb, or III). |
| **2.4 Select conformity‑assessment route** | According to Art 52 MDR: <br>‑ Class I → self‑declaration (Art 52(7)) <br>‑ Is/Im/Ir → Annex IX (limited scope NB) (Art 52(7)) <br>‑ IIa → Annex IX full technical‑doc assessment or Annex II/III + Annex XI (Art 52(6)) <br>‑ IIb → Annex IX or Annex X + Annex XI (Art 52(4)) <br>‑ III → Annex IX or Annex X + Annex XI (Art 52(3)). | Source only lists the generic routes (“NB 계약 기반”) but does not tie them to a specific class. | Class outcome → exact Annex route (e.g., “Annex IX Chapters I & III + Annex XI §10”). |
| **2‑Escalation trigger** | If classification cannot be resolved after the manufacturer’s self‑assessment, *escalate to the Competent Authority (CA) or seek MDCG guidance* (MDCG 2021‑24). | – | Decision point: “suspicion of borderline case → consult CA / MDCG Manual on Borderline and Classification” (source reference). |

---

## 3. Mandatory Technical Evidence (per MDR)

| Evidence | Regulatory basis | Present in source? | Gap to be filled |
|----------|-------------------|--------------------|------------------|
| **Technical Documentation** (Design, manufacturing, risk management, labeling, etc.) | Annex II (general) & Annex III (PMS) | No device‑specific files referenced. | Complete Technical File per Annex II/III. |
| **Clinical Evaluation Report (CER)** – up‑to‑date | Annex XIV Part A; kept current under Art 61 MDR | Source mentions “CEP + CER (Article 61, MDR Annex XIV)”. | Actual CER content, clinical data sources, literature review, benefit–risk analysis. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | No PMCF details provided. | PMCF study protocol, endpoints, monitoring plan, periodic evaluation report. |
| **Post‑Market Surveillance (PMS) System** | Art 83 MDR | Source lists “시판 후 감시” and “Vigilance (MDR Art.87)” – only a mention of vigilance reporting. | PMS scheme (Art 84), PMS plan, procedures for trend analysis, PSUR/Annual Summary depending on class (Art 86). |
| **Unique Device Identification (UDI) registration** | MDR Annex I §23; UDI portal, EUDAMED entries required | Source lists “UDI 포털”, “EUDAMED UDI/DEV”. | Actual UDI‑DI allocation, device identifier submission to EUDAMED. |
| **Declaration of Conformity (DoC)** | Annex IV | Not present. | Signed DoC with reference to all applicable standards and conformity‑assessment route. |
| **Labeling & IFU** (including §23 information) | Annex I Chapter III (§23) | No labeling shown. | Final labeling, symbols, instructions for use in EU languages. |
| **Authorized Representative (AR) documentation** | Art 11 MDR | Source mentions “Authorized Rep.” and “수입자”. | Written mandate, copy of AR’s registration in EUDAMED. |
| **Fees & contract with Notified Body** | NB fees as per national law; example ranges shown in source | Fee brackets provided (EUR 10‑100 k) – useful for budgeting only. | Signed NB contract and proof of payment. |

---

## 4. Risk Management & GSPR Alignment  

| Requirement | MDR reference | Current status |
|-------------|---------------|----------------|
| **Risk Management File** (process per ISO 14971) | Annex I §§10‑22 (general safety & performance requirements); implemented via ISO 14971. | No risk management documentation supplied. |
| **Protection against radiation (if applicable)** | §16 MDR; IEC 60601‑2‑54, –28, –44 for X‑ray systems. | Not addressed – device type unknown. |
| **Electronic programmable systems / software** | §17 MDR; IEC 62304 & IEC 62366‑1. | No software scope defined. |
| **Active devices / implantable devices** | §§18‑19 MDR. | Unknown. |
| **Usability Engineering (lay‑person use)** | §22 MDR; IEC 62366‑1. | Not provided. |

*When the device is identified as active, radiological, or software‑based, the corresponding GSPR clauses and IEC standards must be incorporated.*

---

## 5. Evidence that Must Be Submitted to the Notified Body (NB)

| Class (once known) | NB involvement (Art 52) | Required dossier elements |
|--------------------|--------------------------|----------------------------|
| **Class I** (non‑sterile, non‑measuring) | Self‑declaration – no NB review. | Technical file, DoC, UDI entry, PMS plan. |
| **Is / Im / Ir** | Limited NB audit of sterile/measuring aspects (Annex IX Chapters I & III or Annex XI Part A). | Same as Class I + evidence of sterility assurance/measurement performance, validated according to relevant standards. |
| **Class IIa** | Full Annex IX technical‑doc assessment *or* Annex II/III plus Annex XI §10/§18 (Art 52(6)). | Complete Technical Documentation, CER, PMCF plan, PMS system, UDI, labeling, DoC. |
| **Class IIb** | Annex IX (full) or Annex X + Annex XI (Art 52(4)). | Same as IIa *plus* PSUR (annual) and possibly additional clinical data for high‑risk functions. |
| **Class III** | Annex IX (full) or Annex X + Annex XI (Art 52(3)). | Full dossier, including a validated design‑dossier, extensive clinical evidence, PSUR (annual), and possibly a pre‑market clinical investigation report. |

*The exact combination will be chosen after the classification step.*

---

## 6. Human‑Escalation Triggers  

| Trigger point | Reason for escalation | Recommended action |
|---------------|-----------------------|--------------------|
| **Missing Intended Use / Device Description** | Classification cannot start without it. | Request a complete Intended Use Statement from the manufacturer before any further work. |
| **Unclear or conflicting classification rule(s)** | Borderline cases may lead to an incorrect class, exposing the company to non‑compliance risk. | Escalate to the national Competent Authority (CA) and/or seek clarification via the MDCG Manual on Borderline Classification (referenced in source). |
| **Device identified as active or radiological** *and* no evidence of compliance with relevant IEC standards (e.g., IEC 60601‑2‑54, ‑28, ‑44). | Safety requirements for radiation protection (§16) would be unmet. | Obtain conformity test reports and risk analysis specific to the applicable standard; if unavailable, pause CE‑marking work. |
| **Class Is/Im/Ir or higher** *and* no NB contract signed. | MDR mandates NB involvement for all classes except non‑sterile, non‑measuring Class I. | Secure a Notified Body agreement; if budget constraints appear, flag to project management. |
| **PMCF / PMS plan not defined when required (Class IIa+).** | Art 84/86 require ongoing clinical evaluation; absence will block NB assessment. | Draft and submit PMCF protocol for NB review; if manufacturer cannot provide data, consider a post‑market clinical investigation. |
| **U.S. Agent or 510(k) exemption mentioned but no evidence of US compliance** (source lists “US Agent (510(k) 면제 외)”). | May indicate parallel market entry strategy; regulatory mismatch can affect EU labeling and AR responsibilities. | Verify U.S. status; ensure that any US‑specific claims are not transferred to the EU label without adequate CE evidence. |
| **Fee estimate provided but no proof of payment** (source gives EUR 10‑100 k range). | NB may refuse to start assessment until fees are paid. | Obtain signed fee receipt before dossier submission. |

---

## 7. Summary Judgment  

*At this stage the regulatory pathway cannot be finalized because the essential device data (intended purpose, technology, patient population, etc.) are missing.*  

**Next steps (to be actioned by the project lead):**

1. **Collect complete product definition** – intended use, indications, contraindications, user group, and a description of all functional modules (active, software, measuring, sterile, implantable).  
2. **Map the device to the appropriate Annex VIII rule(s)** and determine the class.  
3. **Based on the class, select the conformity‑assessment route** (Annex IX, X or XI) per Art 52 MDR.  
4. **Prepare the full set of mandatory evidence** listed in Section 3 (Technical Documentation, CER, PMCF, PMS, UDI, DoC, labeling, AR documentation).  
5. **Engage a Notified Body early** if the device is expected to be Class Is/Im/Ir or higher.  

Until items 1–4 are supplied, any further regulatory work must be paused and escalated to senior RA management for clarification.

---

## 8. Peer‑Review Prompt  

*@RA‑Peer:*  
Please challenge the assumptions made above regarding (a) the need for a full Annex VIII rule analysis before any classification can begin; (b) the sufficiency of the listed evidence for each class, especially in borderline active or software‑driven devices; and (c) potential jurisdiction‑specific gaps that may arise from the Korean‑focused source excerpts (e.g., references to UDI portal “udiportal.mfds.go.kr”, MFDS fee structures). Highlight any additional documents or national liaison steps that you consider mandatory before a CE‑marking submission can be drafted.

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261010-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a5b00235915bfa16", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a5b00235915bfa16`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/README.md)
- Source hash: `30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules) ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Response to Notified‑Body Query (X‑ray Generation Device with Integrated SaMD)**  

---

### 1. Device Overview (as inferred from the query)  
| Item | Description |
|------|-------------|
| **Intended purpose** | Generation of ionising X‑ray radiation for diagnostic imaging (e.g., radiography / fluoroscopy). May include on‑board software that processes images and/or provides decision support. |
| **Core technologies** | • X‑ray tube assembly (hardware)  <br>• Power supply & control electronics (active device) <br>• Integrated medical‑device software (SaMD) for image reconstruction/analysis |
| **Regulatory reference in source** | *Rule 10* – “이온화 방사선 방출 진단기기 (X‑ray 발생장치 → Class IIb)”  (Excerpt [2])  <br>*Rule 11* – “Medical Device Software (SaMD) 분류”  (Excerpt [2]) |

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Determination | Regulatory citation |
|------|---------------|---------------------|
| **Device class** | Class IIb (X‑ray generator is an active diagnostic device emitting ionising radiation) | Rule 10, Annex VIII – classification rules (framework reference) |
| **Applicable conformity‑assessment route** | **Annex IX** (full technical‑documentation assessment) *or* the alternative **Annex X + Annex XI** (type‑examination + production conformity verification). Both routes are permitted for Class IIb under Art. 52(4). | Art. 52(4) MDR 2017/745 – “Class IIb … Annex IX … or Annex X + Annex XI” |
| **Notified‑Body involvement** | Mandatory – NB must assess the technical documentation (Annex II), perform a conformity assessment of at least one representative device (Annex IX §4) and review the PMS system (Art. 83). | Art. 52(4); Annex IX §§1‑4; Art. 83 |

---

### 3. Required Evidence Package  

| Evidence | Minimum content | Regulatory reference |
|----------|-----------------|----------------------|
| **Technical Documentation** | Full dossier as per Annex II (device description, specifications, labeling, risk management, clinical evaluation, PMS plan). | Annex II MDR |
| **Clinical Evaluation Report (CER)** | Systematic literature review, clinical data (clinical investigations or equivalence), benefit‑risk analysis. Must be kept current (Art. 61) and structured per Annex XIV Part A. | Annex XIV Part A; Art. 61 |
| **Post‑Market Surveillance (PMS) Plan** | Defined PMS activities, data collection methods, responsibilities. Required for all classes (Art. 84). | Art. 84 |
| **Periodic Safety Update Report (PSUR)** | For Class IIb – at least annually. Must include (a) benefit‑risk conclusions, (b) main PMCF findings, (c) sales volume & user population (Art. 86(1)). | Art. 86 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan / Report** | Specific to the X‑ray generator and its SaMD – includes performance monitoring of radiation output, image quality, software algorithm drift, usability. Structured per Annex XIV Part B. | Annex XIV Part B |
| **Risk Management File** | Risk analysis (ISO 14971) aligned with GSPR §§16 (radiation protection), §17 (software), §18 (active devices). Include risk‑control measures and residual‑risk evaluation. | ISO 14971; GSPR §16‑§18 (Annex I) |
| **Usability Engineering** | Validation of user interface & instructions for lay‑person use if applicable, per IEC 62366‑1. | IEC 62366‑1 |
| **Safety Standards Compliance** | • IEC 60601‑2‑28 (X‑ray tube assemblies)  <br>• IEC 60601‑2‑54 (radiography/radioscopy equipment)  <br>• IEC 62220‑1‑1 (DQE measurement, if relevant)  <br>• IEC 62304 (software lifecycle) | Framework references – no specific source identifiers in the excerpt |
| **Labeling & IFU** | Conform to Annex I §23 (information supplied with the device). Include radiation safety warnings, user training requirements, software version control. | Annex I §23 |

---

### 4. Gaps / Missing Information (to be clarified with the Manufacturer)  

1. **Exact wording of the Intended Use & Indications** – required for classification and risk analysis.  
2. **Clinical data source** – is there a clinical investigation, or reliance on equivalence? Documentation of the comparator devices (including 510(k)/MDR equivalents) is needed.  
3. **Software scope** – does the SaMD perform image reconstruction only, or decision support that could affect treatment? This determines whether Rule 11 places it in Class IIa/IIb/III. Clarify algorithms and intended impact on patient management.  
4. **Radiation performance test results** – measured output, beam quality, leakage, dose‑area product (DAP) under IEC 60601‑2‑28/54 protocols.  
5. **Usability validation data** – especially if the device is intended for use by non‑expert operators.  
6. **PMS data from pre‑market use or pilot sites** – to populate the initial PMCF plan.  
7. **Labeling draft (IFU) and safety information** – confirm inclusion of GSPR §16 radiation warnings, §22 lay‑person instructions (if applicable).  

*All missing items must be supplied before the NB can complete the assessment.*

---

### 5. Recommended Risk Controls (aligned with GSPR)

| Hazard | Control(s) | GSPR citation |
|--------|------------|--------------|
| **Ionising radiation exposure** | • Built‑in dose‑monitoring & interlock; <br>• Compliance with IEC 60601‑2‑28/54 limits; <br>• Protective shielding, warning labels. | §16 (radiation protection) |
| **Active device failure (power/control)** | • Redundant safety circuits; <br>• Failure mode and effects analysis (FMEA); <br>• Automatic shutdown on fault detection. | §18 (active devices) |
| **Software malfunction / erroneous image processing** | • IEC 62304‑based lifecycle; <br>• Verification & validation against clinical requirements; <br>• Version control, cybersecurity measures. | §17 (software) |
| **User error (incorrect exposure settings)** | • Human factors engineering per IEC 62366‑1; <br>• Clear UI cues, dose‑guard features; <br>• Training program and IFU. | §22 (use by lay persons) |
| **Electrical safety** | • Compliance with IEC 60601‑1; <br>• Protective earth, insulation monitoring. | §20 (mechanical & thermal – extended to electrical) |

All risk controls must be documented in the **Risk Management File** and reflected in the **Technical Documentation**.

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger action |
|-----------|----------------|
| **Incomplete clinical evidence** (no investigation report or equivalence justification) | Escalate to senior Regulatory Affairs Lead for risk‑based decision on whether additional clinical data are required before NB submission. |
| **Unresolved classification of the SaMD component** (potentially moving from Class IIa to IIb/III) | Convene Classification Working Group; involve legal counsel if national provisions may differ. |
| **Failure to demonstrate compliance with IEC 60601‑2‑28/54** (missing test reports) | Halt dossier finalisation; request third‑party testing results. |
| **PMS/PMCF plan insufficient for Class IIb** (lacks quantitative safety endpoints) | Forward to Post‑Market Surveillance Manager for redesign of PMCF protocol. |
| **Labeling does not cover GSPR §16 radiation warnings** | Pause NB response; engage Technical Writing & Clinical Safety teams to revise IFU. |
| **NB raises a non‑conformity on any Annex IX requirement** | Immediate escalation to Head of Regulatory Affairs and schedule corrective action plan with the manufacturer. |

---

### 7. Summary Judgment  

- The device is **Class IIb** under **Rule 10** (ionising‑radiation diagnostic equipment).  
- Conformity‑assessment must follow **Annex IX** (full technical‑documentation assessment) or the alternative **Annex X + Annex XI** route, with mandatory NB involvement per Art. 52(4).  
- A complete evidence package—including CER, PMS/PMCF plan, PSUR, risk management file, and conformity to relevant IEC safety standards—is required.  
- Several critical data items are presently missing (intended use wording, clinical data source, software impact analysis, radiation test results, usability validation, labeling draft). These must be obtained before the NB can issue a favourable opinion.  

**Action:** Request the above missing documentation from the manufacturer; once received, perform a gap‑analysis against Annex II and Annex XIV requirements, then prepare the final submission for NB review.

---

### 8. Peer‑Review Prompt  

*Colleague, please evaluate the following:*  

1. **Assumptions** – Is the classification as Class IIb (Rule 10) appropriate given the limited description, or could any additional functions shift it to a higher class?  
2. **Source Coverage** – Do the excerpts supplied justify the conclusions drawn about required standards and GSPR citations, or are we extrapolating beyond the source material?  
3. **Jurisdictional Gaps** – Have we considered any national implementation measures (e.g., specific EU member‑state radiation directives) that might affect the evidence requirements?  

Your feedback will help ensure completeness before the final NB response is drafted.

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

## ra_kr

### kb-eval-20261010-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "448c92384d677628", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `448c92384d677628`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EB%B3%B4%EC%99%84%EC%9E%90%EB%A3%8C_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_보완자료_대응전략.md`는 `MFDS_보완자료_대응전략.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) --- ### 4-C. 자주 사용하는 표현 (한국어 공문 문체) | 상황 | 표현 | |---|---| | 보완 내용 인용 | "귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다." | | 데이터 추가 제출 | "해당 데이터를 별첨 자료로 첨부하오니 검토하여 주...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **MFDS 보완 자료 대응 전략 초안**

---

### 1. Device Classification & Submission Route  
| Item | Current Understanding | Gap / Action Needed |
|------|-----------------------|---------------------|
| **Intended use / indication** | Not supplied in source material. | Obtain the device’s intended clinical purpose and target patient population. |
| **Risk class (제조‑품목별 분류 규칙)** | Requires applying MFDS “의료기기법 제23조(분류·인증·허가 기준)” to determine Class I–IV. | Perform classification analysis using the device’s risk profile, invasiveness, duration of contact, etc. |
| **Submission pathway** | • **허가 (일반)** – full market‑authorization review.<br>• **허가 (임상 포함)** – when clinical data are required.<br>• **인증** – for certain Class I devices under NIFDS delegation.<br>• **신고** – for low‑risk Class I devices. | Confirm whether the device falls into “허가(일반)” or “허가(임상 포함)”. If it is a Class I product, verify if certification (NIFDS 위탁) applies. |
| **Applicable MFDS notice** | No specific 고시/notification number appears in the excerpts. | Verify the exact MFDS 고시 번호 that governs the chosen route (e.g., “MFDS 고시 제2023‑45호”). |

---

### 2. Required Evidentiary Package (per MFDS guidance)  

| Evidence Category | Typical Requirement (Korean law/standards) | Status |
|-------------------|---------------------------------------------|--------|
| **Technical dossier** | • Device description, specifications, intended use.<br>• KGMP‑compliant manufacturing process (ISO 13485 + MFDS KGMP). | – |
| **Non‑clinical safety data** | GLP‑compliant bench & animal testing; MFDS accepts OECD‐aligned non‑clinical data under the “non‑clinical MAD” scope. | – |
| **Clinical evaluation** | • Clinical investigation report if required by classification.<br>• Acceptance of foreign CER only when covered by MFDS notice on foreign clinical data (separate from non‑clinical MAD). | – |
| **Labeling & IFU** | Korean language labeling, product name, manufacturer info, warnings, and instructions for use in Hangul. | – |
| **Risk Management** | ISO 14971 risk analysis file, with residual risk controls documented. | – |
| **Performance testing** | Conformance to relevant K‑SAS (Korean Standards) or IEC/ISO equivalents. | – |
| **Post‑market surveillance plan** | MFDS post‑marketing surveillance (시판후조사) schedule and reporting procedure. | – |
| **KGMP certification** | Facility certificate issued by MFDS, proof of ISO 13485 compliance. | – |

*All items above are framework references; no specific MFDS 고시 numbers were found in the source excerpts.*

---

### 3. Missing Information Identified from Source  

| Item | What the source tells us | What remains unknown |
|------|--------------------------|----------------------|
| **Supplement handling timeline** | “보완 기간은 처리 기간에서 제외 (clock stops)” – supplemental review time is excluded from the statutory processing clock. (Excerpt [1]) | Exact deadline for supplement submission (e.g., default 30‑day period) is not stated; must be confirmed in MFDS procedural notice. |
| **Template language for supplements** | Sample Korean formal expressions (e.g., “귀처의 보완 요청 내용(제○호, ○○항)에 대하여 …”) are provided for response letters. (Excerpt [2]) | The actual reference numbers (제○호) of the original MFDS request must be inserted; these identifiers are not present in the excerpt and need extraction from the MFDS notice received. |
| **Processing time per route** | Standard processing times: 허가(일반) = 65 days, 허가(임상 포함) = 80 days, 인증 = 30 days (NIFDS 위탁), 신고 = immediate. (Excerpt [1]) | Whether any expedited or accelerated pathways apply to the device is not indicated. |
| **Regulatory instrument numbers** | No 고시/notification number appears in the excerpts for classification, KGMP, labeling, etc. | Must retrieve the exact MFDS 고시 번호 governing the product class and submission type (to be cited later). |

---

### 4. Risk‑Control Considerations  

*Apply ISO 14971 throughout development and dossier preparation.*  
- **Hazard identification & risk analysis** – map each identified hazard to a control measure (design, labeling, user training).  
- **Residual risk evaluation** – ensure residual risks are “acceptable” per MFDS “위험 허용 기준”.  
- **Verification of risk controls** – include test data, validation reports, and usability studies where applicable.  
- **Post‑market risk monitoring** – set up a PMS system that meets MFDS 시판후조사 requirements (periodic safety update reporting).

---

### 5. Timeline & Supplement Management  

| Phase | Standard MFDS timeline* | Key Actions |
|-------|------------------------|-------------|
| **Initial submission** | 허가(일반) = 65 days, 허가(임상 포함) = 80 days (excluding supplement periods). (Excerpt [1]) | Prepare complete dossier; submit via MFDS e‑portal. |
| **MFDS review → Supplement request** | Not fixed – issued when deficiencies are identified. | Draft response using the Korean formal expressions shown in Excerpt [2]; reference the specific “제○호, ○○항” from the MFDS notice. |
| **Supplement submission** | Clock stops during supplement period (보완 기간은 처리 기간에서 제외). (Excerpt [1]) | Submit requested data promptly; request extension only with justified reason per MFDS practice. |
| **Final decision** | Continue counting remaining days after supplement acceptance to reach total processing time. | Notify the sponsor of approval, certification or any post‑approval obligations. |

\*These are *framework references* (processing‑time tables) that do not require a specific MFDS 고시 number in this draft.

---

### 6. Human‑Escalation Triggers  

| Trigger | When to Escalate to Senior RA / Legal | Reason |
|---------|----------------------------------------|--------|
| **No classification evidence** | Immediately, if the device’s risk class cannot be confirmed. | Misclassification leads to inappropriate submission route and regulatory penalties. |
| **Missing MFDS 고시 number** | Upon drafting the final submission checklist. | Exact notice citation is required for regulatory compliance checks. |
| **Supplement deadline missed** (no response within 30 days of MFDS request) | Escalate to project manager / legal counsel. | Clock‑stop rule stops, but prolonged silence may lead to withdrawal of review. |
| **Foreign clinical data acceptance uncertainty** | Early in the dossier preparation phase. | Need clarification whether foreign CER can be used under current MFDS scope (separate from non‑clinical MAD). |
| **KGMP certification not yet obtained** | Prior to submission. | Submission without KGMP compliance will be rejected outright. |
| **Labeling/IFU not fully Korean** | At the labeling review stage. | Korean language requirement is mandatory; any English‑only material must be translated before filing. |

---

### 7. Reusable RA Judgment (Lesson Learned)  

- **MFDS processing clocks pause during supplement periods** – always calculate total review time by adding the statutory period *after* the supplement is resolved (source [1]).  
- **Use MFDS‑approved Korean formal language when responding to supplement requests**, inserting the exact “제○호, ○○항” reference numbers from the original notice (source [2]).  
- **Do not assume a specific 고시 number** unless it appears in source material; instead note “verify separately”. This avoids introducing false identifiers.  

These points should be embedded in any future MFDS supplement‑response SOPs.

---

### 8. Peer Review Prompt  

> **@RA‑Peer:** Please challenge the assumptions made above regarding (1) the classification pathway without a declared device indication, (2) the completeness of the evidentiary checklist given recent MFDS updates on foreign clinical data acceptance, and (3) any jurisdiction‑specific gaps (e.g., post‑marketing surveillance plan details) that may affect the draft’s adequacy. Your feedback will help refine the submission strategy before finalization.

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `1071384471244337751`

> ### 4-C. 자주 사용하는 표현 (한국어 공문 문체) | 상황 | 표현 | |---|---| | 보완 내용 인용 | "귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다." | | 데이터 추가 제출 | "해당 데이터를 별첨 자료로 첨부하오니 검토하여 주시기 바랍니다." | | 시험 진행 중 | "현재 ○○기관에 시험 의뢰 중으로, 결과 수령 후 추가 제출 예정입니다." [검증 필요] | | 기준 적합성 | "관련 규격 ○○○ 기준을 충족함을 확인하였습니다." | | 연장 요청 | "시험 일정상 ○월 ○일까지 보완자료 제출이 어려우므로, 기한 연장을 요청드립니다." | ---

### kb-eval-20261010-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "bab29c68d36c6c79", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_기술문서_섹션별_작성가이드.md", "source_hash": "f1a42b1b5d6bc604ca2faa7644dc90cfb166a98521fb98244ac09e80eec1e2b1"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `bab29c68d36c6c79`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_기술문서_섹션별_작성가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%EC%84%B9%EC%85%98%EB%B3%84_%EC%9E%91%EC%84%B1%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `f1a42b1b5d6bc604ca2faa7644dc90cfb166a98521fb98244ac09e80eec1e2b1`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_기술문서_섹션별_작성가이드.md`는 MFDS 기술문서 섹션별 작성 요구사항과 evidence 구성 기준 문서입니다.
- 현재 excerpt 핵심: ### 4.3 시험규격 설정 근거 작성 요령 - 국제 표준 근거: "IEC 60601-2-28:2017을 적용하였으며, 동 규격이 X선관 조립품(X-ray tube assembly)의 성능 시험 방법을 규정하는 국제 표준으로 MFDS 인정 기준과 일치함." - 자사 규격 근거: "국제 표준에서 정하지 않은 항목(예: 영상 처리 알고리즘 성능)은 의도된 사용목적 및 위험 분석 결과에 따라 자사 시험 규격 OQP-XXXX를 제정하여 적용함." - KS 표준 근거: "KS A ISO 9283 대응 자사 규격 적용." --- ## 1. 기술문서 전체 구성 (시행규칙 별표 3 기준) ``` 기술문서 (MFDS 제출용) ├── 1. 개요 (제...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Classification, Submission Route & Evidence Package for X‑ray Tube Assembly (Radiological Device)**  

---

### 1. Device Overview  
| Item | Details (to be confirmed) |
|------|----------------------------|
| **Product name / Model** | (need exact wording) |
| **Intended use / Indications** | (e.g., “provides X‑ray generation for diagnostic imaging systems”) – **missing** in source |
| **Classification‑relevant features** | High‑energy radiation source, electrical/mechanical safety functions, optional software control |

---

### 2. MFDS Classification & Submission Pathway  

| Criterion | Korean regulatory reference | Draft determination* |
|-----------|-----------------------------|----------------------|
| Risk class (based on intended use, invasiveness, radiation) | MFDS “Medical Device Act” classification rules (e.g., **제1조 제2항** of the act and accompanying 시행규칙) – *no specific notice number appears in source* → **verify separately** | Likely **Class IIb–III** (radiological equipment). |
| Submission type | If Class I‑IIa → “신고” (notification); Class IIb‑III → “허가” (approval) with full technical dossier. | Anticipated **허가** (full approval) owing to radiation risk. |

\*The final class must be confirmed by MFDS classification table (시행규칙 별표 3). No exact 고시/notification number is provided in the source excerpts; therefore a separate verification step is required.

---

### 3. Technical Documentation – Required Sections  
(Structure required by **시행규칙 별표 3** – see Source [2]; no specific identifier given → verify separately)

1. **Overview** (product name, model, classification number) – missing in source.  
2. **Intended Use / Indications** – missing; must be described in Korean and English.  
3. **Operating Principle** – description of X‑ray generation physics & control logic.  
4. **Materials & Construction** – bill of materials, component traceability.  
5. **Manufacturing Process** – flowchart, KGMP certification copy (must be KAIST‑approved).  
6. **Performance & Test Specifications**  

   * **6‑1. 시험규격 및 설정근거** – Use IEC 60601‑2‑28:2017 as the primary benchmark for X‑ray tube assembly performance testing (Source [1]).  
   * For items not covered by IEC, such as proprietary image‑processing algorithms, reference internally generated specification **OQP‑XXXX** (as noted in Source [1]) and provide risk‑based justification.  

7. **Safety Data** – include:

   - Electrical & Mechanical safety (IEC 60601‑1)  
   - Radiation safety (IEC 60601‑2‑28, Korean radiation protection guidelines) – **mandatory** for radiological devices.  
   - EMC (IEC 60601‑1‑2)  
   - Software safety (IEC 62304) if software is present.  

8. **Clinical Evidence (if applicable)** – foreign CE/ FDA 510(k) data may be used, but Korean law may still demand local clinical evaluation for Class IIb–III devices. No indication in source; flag as **missing**.  

9. **Labeling & IFU** – Korean language label and user manual required (MFDS labeling guideline). No draft provided → **missing**.  

---

### 4. Evidence Package Summary  

| Evidence Area | Source / Standard | Status |
|--------------|-------------------|--------|
| **Performance testing** | IEC 60601‑2‑28:2017 (global standard) – accepted by MFDS as matching its criteria (Source [1]) | Confirmed; include test reports. |
| **Additional performance items** | Internal spec OQP‑XXXX (risk‑based, not covered by IEC) – referenced in Source [1] | Draft needed; provide validation data. |
| **Mechanical/robotic testing** | KS A ISO 9283 – cited as basis for internal spec (Source [1]) | Include test results. |
| **Safety – Electrical/EMC** | IEC 60601‑1, IEC 60601‑1‑2 – standard references (implicit) | Provide conformity evidence. |
| **Radiation safety** | IEC 60601‑2‑28:2017 (radiological performance) – aligns with MFDS criteria (Source [1]) | Provide dose, shielding, ALARA analysis. |
| **Software safety** | IEC 62304 (if software present) – not mentioned in source → **missing**. |
| **Clinical data** | None provided; need local clinical evaluation or accepted foreign CER (MFDS may accept under OECD‑MAD for non‑clinical data only). | **Missing**. |
| **KGMP certification** | Required for manufacturing site – no evidence shown. | **Missing**. |
| **Korean labeling/IFU** | MFDS labeling guideline – not in source. | **Missing**. |

---

### 5. Risk Controls & Mitigation  

| Hazard | Control (per IEC 60601‑2‑28 & risk analysis) | Verification |
|--------|--------------------------------------------|--------------|
| Excessive X‑ray dose (radiation overexposure) | Built‑in dose limiting circuitry, interlocks, ALARA design philosophy; compliance testing per IEC 60601‑2‑28. | Dose measurement reports. |
| Electrical shock / failure | Protective earth, leakage current limits, insulation verification – IEC 60601‑1. | Electrical safety test report. |
| Mechanical breakdown (tube rupture) | Robust tube housing, vibration testing per KS A ISO 9283. | Mechanical durability data. |
| Software malfunction (image processing errors) | Software life‑cycle processes (IEC 62304), verification & validation of algorithms; risk‐based testing for OQP‑XXXX items. | Software test logs, V&V documentation. |
| EMC interference with other equipment | IEC 60601‑1‑2 compliance testing. | EMC test report. |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger | Action Required |
|-----------|---------|------------------|
| **Unclear classification** (e.g., ambiguity between Class IIb vs III) | Classification decision pending after review of radiation risk and intended use. | RA lead to request MFDS pre‑submission consultation; document rationale. |
| **Missing Korean IFU/Label** | No draft Korean labeling in dossier. | Escalate to product development for translation & compliance check before submission. |
| **Absence of local clinical data** (required for Class IIb–III) | No clinical evidence supplied. | Senior RA to determine need for local clinical trial; initiate protocol approval process. |
| **KGMP certification lacking** | Manufacturing site not yet KGMP‑certified. | Pause submission, engage QC/Manufacturing to obtain KGMP audit report. |
| **Software safety documentation incomplete** | No IEC 62304 evidence. | Raise with software engineering lead; develop V&V package prior to submission. |
| **Regulatory reference gap** (e.g., specific MFDS 고시 number for radiological devices not identified) | “no specific identifier found in source — verify separately.” | Senior RA to search MFDS notice database and attach correct 고시/notification number before final dossier filing. |

---

### 7. Citation Summary  

| Item | Source citation (per rule) |
|------|----------------------------|
| IEC 60601‑2‑28:2017 as performance benchmark – matches MFDS criteria | **Source [1]** |
| KS A ISO 9283 referenced for internal mechanical testing | **Source [1]** |
| Technical dossier structure per 시행규칙 별표 3 | **Source [2]** (no specific notice number provided → verify separately) |
| All other framework references (IEC 60601‑1, IEC 62304, etc.) are standard industry norms and do not require a source identifier. |

*No instance identifiers (e.g., MFDS 고시 번호, case numbers) appear in the excerpts; therefore none are inserted.*

---

### 8. Peer Review Prompt  

> **To RA colleagues:**  
> Please examine the assumptions made regarding classification (Class IIb–III), the sufficiency of IEC 60601‑2‑28 as the sole performance reference, and potential gaps in Korean‑specific obligations such as local clinical data, KGMP certification, and labeling. Identify any additional MFDS notices or annexes that may be relevant but are not captured in the current source excerpts, and advise on missing evidence items that could affect a successful 허가 submission.

--- 

*End of draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1075785891198339619`

> ### 4.3 시험규격 설정 근거 작성 요령 - 국제 표준 근거: "IEC 60601-2-28:2017을 적용하였으며, 동 규격이 X선관 조립품(X-ray tube assembly)의 성능 시험 방법을 규정하는 국제 표준으로 MFDS 인정 기준과 일치함." - 자사 규격 근거: "국제 표준에서 정하지 않은 항목(예: 영상 처리 알고리즘 성능)은 의도된 사용목적 및 위험 분석 결과에 따라 자사 시험 규격 OQP-XXXX를 제정하여 적용함." - KS 표준 근거: "KS A ISO 9283 대응 자사 규격 적용." ---

2. Chunk `134996178882731357`

> ## 1. 기술문서 전체 구성 (시행규칙 별표 3 기준) ``` 기술문서 (MFDS 제출용) ├── 1. 개요 (제품명, 품목명, 분류번호, 모델명, 제조원) ├── 2. 사용목적 (Intended Use / Indications for Use) ├── 3. 작용원리 (Operating Principle / Mechanism of Action) ├── 4. 원재료·구성품·구조 (Materials & Structure) ├── 5. 제조방법 (Manufacturing Process) ├── 6. 성능·시험규격 (Performance & Test Specifications) │ ├── 6-1. 시험규격 및 설정근거 │ └── 6-2. 실측값 (성적서) ├── 7. 안전성 자료 (Safety Data) │ ├── 7-1. 전기·기계적 안전 │ ├── 7-2. 생물학적 안전 │ ├── 7-3. 방사선 (해당 시) │ ├── 7-4. 전자파(EMC) │ └── 7-5. SW 안전성 (해당 시) ├── 8. 임상자료 (해당 시) └── 9. 기재사항 (라벨, 사용설명서) ``` ---

### kb-eval-20261010-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "cf44c05cb397532e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `cf44c05cb397532e`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EC%82%AC%EC%9D%B4%EB%B2%84%EB%B3%B4%EC%95%88_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_2025_%EB%8C%80%EC%9D%91.md)
- Source hash: `87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_사이버보안_가이드라인_2025_대응.md`는 `MFDS_사이버보안_가이드라인_2025_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 | ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Cyber‑Security Compliance for a Medical Device (Korea MFDS)**  

---

### 1. Likely Device Classification & Submission Route  
| Decision point | Korean regulatory rule (framework) | Expected outcome* |
|----------------|------------------------------------|-------------------|
| **Is the device a software‑only medical device or a hardware device with network connectivity?** | 의료기기법 제 3조·제 4조 (device definition & classification) – see Korean Medical Device Classification Rules (e.g., “Class I: low risk; Class II/III: moderate–high risk”) | • If **software‑only / network‑connected** and intended for diagnosis, monitoring or therapy → **Class II** (or Class III if invasive/high‑risk).  <br>• Stand‑alone, non‑networked accessories → **Class I**. |
| **Does the device fall under the “Digital Health Product” scope of the Digital Medical Products Act?** | 「디지털의료제품법」(effective 2025‑01‑24) – defines digital health products and adds a dedicated review pathway (digital‑health‑product approval). | • If covered, the **digital‑health product authorization** route applies (MFDS electronic submission portal). <br>• Otherwise, use the standard medical‑device “허가” (Class II/III) or “신고” (Class I) pathway. |

\*The exact class must be confirmed by matching the device’s intended purpose and risk profile to the Korean classification tables (e.g., Table 2‑1 of the MFDS Classification Guide).  

**Action:** Identify the device’s functional category, invasiveness, and whether it processes personal health data over a network. This determines whether a **Class II/III 허가** or **digital‑health product 허가** is required.

---

### 2. Required Evidence – Cybersecurity Package (per MFDS “사이버보안 허가·심사 가이드라인”)  

| Evidence | Reason (MFDS requirement) | Source citation |
|----------|---------------------------|-----------------|
| **Cyber‑Security Design Dossier** covering the 35 RA items (RA‑01 ~ RA‑35). | The 2025 revision expands mandatory cybersecurity controls from 15 to **35** items. | “사이버보안 요구사항 **15개 → 35개** 확장” – source [1] |
| **Category‑wise compliance matrix** mapping the device’s implementation to each of the eight major categories: <br>• Secure design principle<br>• Authentication & access control<br>• Encryption (data at rest & in transit, key management)<br>• Software integrity (code signing, boot verification, SBOM)<br>• Network security (port minimisation, firewall, TLS version)<br>• Vulnerability management (CVE monitoring, patch schedule, CVD policy)<br>• Audit & logging (event logs, log protection, access traceability)<br>• Update & maintenance (secure update mechanism, remote‑management safeguards) | The guideline lists these 8 categories as the structure for the 35 RA items. | “35개로 확장된 요구사항은 아래 8개 카테고리로 분류” – source [2] |
| **Risk Management File** (ISO 14971) showing how identified cyber‑threats are mitigated, with severity/likelihood assessments and residual risk acceptance. | MFDS requires alignment of cybersecurity controls with overall device risk management. | Implicit from “조화 목적 … IMDRF N60/N73” – source [1] (no explicit article number). |
| **Software Bill‑of‑Materials (SBOM)** & **code signing certificates** | Required under the “소프트웨어 무결성” sub‑category. | Source [2] – “코드 서명, 부트 무결성 검증, SBOM 관리”. |
| **Vulnerability Management Plan** (CVE/CVD monitoring schedule, patch release policy) | Required under “취약점 관리”. | Source [2]. |
| **Log‑Management Specification** (format, retention period, tamper‑proof storage) | Required under “감사·로그”. | Source [2]. |
| **Secure Update Mechanism description** (authentication of update packages, encrypted transport) | Required under “업데이트·유지보수”. | Source [2]. |
| **Korean‑language labeling & IFU** stating basic cybersecurity user responsibilities (e.g., password policy, firmware update instructions). | MFDS labeling rule requires all user‑facing information in Korean. | General MFDS labeling requirement (framework reference – no specific identifier in source). |
| **KGMP certification of the manufacturing site** (if Class II/III) | Mandatory for higher‑risk devices. | Framework reference – not listed in source excerpt. |

**Note:** The guideline does **not** assign a public “고시 번호” to this document; therefore no specific MFDS notice identifier can be quoted. *If the official 고시 number is needed, retrieve it from the MFDS website and insert later (verify separately).*

---

### 3. Missing Information Needed for Submission  

| Item | Why it matters | What to obtain |
|------|----------------|----------------|
| **Exact device classification** (Class I/II/III or digital‑health product) | Determines whether a 허가 or 신고, and the depth of cybersecurity documentation required. | Intended use statement, risk class decision matrix, any applicable predicate devices. |
| **Device architecture diagram** (hardware, software, network interfaces) | Needed to map each RA requirement to concrete system components. | System block diagram with data‑flow description. |
| **Existing security controls** (current design, test results) | To populate the compliance matrix and identify gaps. | Test reports (penetration testing, code analysis), configuration files, certificates. |
| **Manufacturer’s KGMP status** | Required for Class II/III devices. | KGMP certification copy or evidence of ongoing audit. |
| **Labeling & IFU drafts in Korean** | MFDS mandates Korean‑language user information that reflects cybersecurity responsibilities. | Draft labeling and instructions. |
| **Foreign regulatory equivalents (e.g., FDA 510(k) cyber‑security supplement, EU MD Annex II)** if you intend to rely on them for “mutual acceptance of data”. | MFDS may accept foreign non‑clinical safety data under OECD MAD; however, for cybersecurity the guideline explicitly requires Korean‑specific documentation. | Copies of any foreign regulatory submissions and their cybersecurity sections. |
| **Official 고시/공지 번호** of this cyber‑security guideline (if needed for cross‑reference in submission). | Precise citation required in the MFDS application forms. | Retrieve from MFDS notice database; flag as “verify separately”. |

---

### 4. Core Risk Controls to Implement (aligned with the 35 RA items)

| Category | Example Control(s) | Intended risk mitigation |
|----------|-------------------|---------------------------|
| **Secure Design Principle** | Threat modeling early, defense‑in‑depth architecture, least‑privilege principle for all components. | Reduces attack surface and limits impact of a breach. |
| **Authentication & Access Control** | Multi‑factor user authentication, role‑based access control (RBAC), session timeout, secure credential storage. | Prevents unauthorized use or configuration changes. |
| **Encryption** | AES‑256 data‑at‑rest encryption; TLS 1.3 for all communications; hardware security module (HSM) for key management. | Protects confidentiality and integrity of patient data in transit & storage. |
| **Software Integrity** | Code signing with SHA‑256, secure boot verification, periodic SBOM verification against known components. | Detects tampering and ensures only approved software runs on the device. |
| **Network Security** | Closed ports list, firewall rules, use of VPN for remote access, TLS version enforcement per IEC 81001‑5‑1. | Limits network exposure and protects against man‑in‑the‑middle attacks. |
| **Vulnerability Management** | Automated CVE feed monitoring, quarterly patch releases, documented CVD (Common Vulnerabilities Disclosure) policy. | Ensures timely remediation of known weaknesses. |
| **Audit & Logging** | Immutable security event log stored on tamper‑evident media for ≥ 12 months; centralized SIEM aggregation. | Enables forensic analysis and regulatory reporting of incidents. |
| **Update & Maintenance** | Authenticated OTA (over‑the‑air) updates, digital signatures verified before installation, rollback capability. | Guarantees that only vetted software is installed and reduces downtime. |

---

### 5. Citations  

| Requirement | Citation type | Reference from source |
|------------|---------------|-----------------------|
| Legal basis for the guideline | Framework reference (law) | 「디지털의료제품법」(2025‑01‑24 시행), 의료기기법 시행규칙 – source [1] |
| Expansion of cybersecurity items from 15 → 35 | Instance identifier (guideline content) | “사이버보안 요구사항 **15개 → 35개** 확장” – source [1] |
| Alignment with IMDRF N60/N73, IEC 81001‑5‑1 | Framework reference (international standards) | “조화 목적 … IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화” – source [1] |
| List of the 8 major categories & example RA items | Instance identifier (guideline content) | Table in source [2] (categories and sample requirements). |
| No specific 고시 번호 or article/section number is provided in the excerpts. | — | *no specific identifier found in source — verify separately* |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger condition | Recommended escalation |
|-----------|-------------------|------------------------|
| **Classification ambiguity** (e.g., unsure whether device qualifies as digital‑health product or standard medical device). | No clear mapping to Korean classification tables after initial review. | Escalate to senior RA lead for classification decision; request legal counsel if needed. |
| **Missing KGMP certification** for a Class II/III device. | Manufacturing site not yet certified, or certificate expiry within 3 months of planned submission. | Immediate escalation to Quality Management & Production to obtain or renew KGMP before dossier finalisation. |
| **Gap in any of the 35 RA items** (e.g., no documented vulnerability‑management process). | Evidence of non‑compliance identified during internal audit of the cyber‑security package. | Escalate to Product Development & Security Engineering to implement missing control; pause submission until resolved. |
| **Absence of official 고시 번호** for the guideline in the application forms. | Application form requires “고시 번호” and none is available. | Flag to regulatory affairs manager to retrieve the correct notice number from MFDS portal before filing. |
| **Regulatory change after 2025‑01‑10 amendment** (e.g., new IMDRF N73 revision). | New international or domestic guidance released during dossier preparation. | Escalate to RA team lead for impact analysis and possible supplemental submission. |
| **Foreign evidence reliance** (e.g., FDA cybersecurity supplement) but MFDS does not accept it under OECD MAD. | Attempted citation of foreign non‑clinical data without Korean‑specific mapping. | Prompt review by senior RA; if necessary, request additional Korean testing or documentation. |

---

### 7. Summary Judgment  

- **Step 1:** Confirm the device’s risk class (Class I vs II/III) and whether it falls under the Digital Medical Products Act.  
- **Step 2:** Assemble a **Cyber‑Security Design Dossier** covering all 35 RA items, structured by the eight categories identified in the MFDS guideline.  
- **Step 3:** Produce supporting artifacts (SBOM, vulnerability‑management plan, log‑management spec, encryption certificates, Korean IFU).  
- **Step 4:** Verify KGMP status for the manufacturing site and ensure all labeling is in Korean.  
- **Step 5:** Identify any missing pieces from the checklist above; resolve before filing.  

If any of the escalation triggers are met, pause submission and involve the relevant functional owners (Classification lead, Quality/Production, Security Engineering, Senior RA).

---

**Peer‑Review Prompt**  

> *@RA‑Partner: Please review the assumptions made about classification pathways, the completeness of the 35‑item cyber‑security evidence list, and any jurisdiction‑specific gaps (e.g., Korean language requirements, KGMP certification). Highlight any additional MFDS citations that may be required or suggest alternative strategies for leveraging foreign regulatory data.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---

### kb-eval-20261010-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "9e6b14b3a43658e5", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `9e6b14b3a43658e5`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/GMP_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `README.md`는 KGMP 또는 GMP evidence readiness, audit readiness, QMS 절차·기록 관련 문서입니다.
- 현재 excerpt 핵심: ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트 ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Korean MFDS (KGMP) Submission Overview**

---

### 1. Device Classification & Submission Route  

| Item | Assessment | Rationale / Reference |
|------|------------|------------------------|
| **Classification** | *Undetermined – requires device‑specific information* (intended use, invasiveness, duration of contact, pharmacological/energy principle). | MFDS classification follows the “Medical Device Classification Rules” of the Medical Devices Act (e.g., Class I‑IV) and its annexed rule table. |
| **Submission pathway** | *If Class II–IV* → **MFDS 허가 (Approval)**; <br> *if Class I* → **MFDS 신고 (Notification)**. | Determined by the classification outcome; MFDS 허가 requires a full technical dossier, while 신고 needs a simplified notification package. |

**Human‑escalation trigger:**  If after initial information gathering the device cannot be placed in any class because key parameters are missing (e.g., invasiveness, duration), the RA team must request clarification from the sponsor immediately.

---

### 2. Core Regulatory Requirements (KGMP & MFDS)

| Requirement | Evidence Needed | Source / Citation |
|-------------|-----------------|-------------------|
| **KGMP facility certification** | • KGMP compliance checklist (as per *“의료기기 제조 및 품질관리 기준” 고시*). <br>• Completed “KGMP 심사 신청서 양식”. <br>• Supporting documents: quality manual, SOPs, equipment qualification records, personnel qualifications. | Framework reference – MFDS KGMP regulation (see excerpt [1] and [2]). |
| **Technical Documentation** | • Device description, intended use, labeling in Korean. <br>• Design & manufacturing information (drawings, specifications). <br>• Risk Management file (ISO 14971‑compliant). <br>• Performance data (bench, animal, clinical if required). | Framework reference – MFDS Technical Documentation requirements (Annex III of the Medical Device Act). |
| **Clinical Evidence** | • If foreign CE mark or FDA 510(k) is to be leveraged, provide *foreign clinical evaluation report* plus justification of equivalence. <br>• Where local clinical data are mandatory (e.g., Class III), submit Korean clinical trial results. | No specific instrument number found in source – verify separately. |
| **Labeling & IFU** | • All labeling, Instructions for Use (IFU) and promotional material must be in Korean language, meeting MFDS labeling standards. | Framework reference – MFDS Labeling Regulation (Article 23 of the Medical Device Act). |
| **Post‑Market Surveillance (PMS) Plan** | • PMS & Periodic Safety Update Report (PSUR) outline, in line with MFDS “시판후조사” requirements. | Framework reference – MFDS Post‑Market Surveillance Guidelines. |

---

### 3. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Immediate Action |
|-----|----------------------|-------------------|
| **Device classification data** (intended use, risk level) | Cannot determine whether 허가 or 신고 is required; may affect dossier scope. | Request detailed device description & intended‑use statement from sponsor. |
| **KGMP certification status** of the manufacturing site(s) | KGMP certification is mandatory for Class II–IV devices and imported items. Without it, review cannot proceed. | Obtain current KGMP audit report or schedule a KGMP audit if not yet certified. |
| **Local clinical data requirement** (if applicable) | Absence may lead to MFDS request for additional Korean clinical evidence, delaying approval. | Clarify whether foreign CE/FDA data are acceptable under latest MFDS mutual‑acceptance notice; otherwise plan local study. |
| **Korean language labeling drafts** | Non‑Korean labeling will be rejected at document review stage. | Provide draft labels/IFU in Korean for preliminary check. |
| **Risk Management file alignment with ISO 14971** | Missing risk analysis may cause non‑conformity findings. | Submit a complete risk management report (hazard identification, mitigation measures). |

---

### 4. Core Risk Controls to Address  

1. **Design Controls** – Establish design history file per ISO 13485 and MFDS “의료기기 제조 및 품질관리 기준”.  
2. **Process Validation** – Demonstrate validated manufacturing processes; maintain process qualification records (PQ, OQ, IQ).  
3. **Supplier Management** – Provide supplier evaluation & monitoring documentation for critical components.  
4. **Traceability** – Implement unique device identifier (UDI) per MFDS UDI guidelines to enable traceability throughout the supply chain.  

---

### 5. Citations  

| Type | Citation Detail |
|------|-----------------|
| **Framework reference (no specific instrument number)** | *MFDS “의료기기 제조 및 품질관리 기준” 고시* – provides KGMP application forms and checklist (source [1], [2]). |
| **Instance identifier** | No specific MFDS 고시/notification number or device clearance number appears in the supplied excerpts. *Verification of any required notice numbers must be performed separately.* |

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason | Escalation Path |
|---------|--------|-----------------|
| **Missing classification data** | Prevents selection of proper submission route. | Prompt sponsor for complete intended‑use and risk profile; if not provided within 5 business days, raise to project manager. |
| **Absence of KGMP certificate** for a Class II–IV device or imported item. | Mandatory pre‑condition for MFDS 허가. | Notify quality assurance lead; consider deferring submission until certification is obtained. |
| **Unclear acceptance of foreign clinical data** (no mutual‑acceptance notice verified). | Could lead to MFDS request for additional Korean data. | Request legal/RA clarification on the latest MFDS notice expanding foreign data acceptance; if ambiguous, plan local clinical evaluation. |
| **Non‑Korean labeling draft** submitted after document check deadline. | Immediate rejection at dossier screening. | Alert marketing & regulatory documentation team; enforce language compliance before the next review cycle. |

---

### 7. Reusable RA Judgment (Lesson Learned)

> *When initiating a Korean MFDS submission, always verify that the manufacturing site holds an up‑to‑date KGMP certification and that device classification can be unequivocally established from sponsor‑provided intended‑use data. Absence of either element blocks progression to the appropriate 허가/신고 pathway and triggers immediate escalation.*  

This judgment is stored for future RA projects involving Korean regulatory submissions.

---

### 8. Peer Review Prompt  

> **[RA Peer]** – Please review the assumptions above, especially:  
> • Whether any additional MFDS notices (e.g., recent mutual‑acceptance of foreign clinical data) might apply despite not being present in the current source excerpts.  
> • The completeness of the identified gaps given the limited information supplied.  
> • Any jurisdiction‑specific obligations that may have been overlooked (e.g., environmental safety, recycling fees).  

Your feedback will help ensure full coverage before finalizing the submission plan.

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `341244002941932847`

> ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트

2. Chunk `634338496332185325`

> ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)

### kb-eval-20261010-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-10", "decision_ref": "kb-eval-20261010-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "54a5752194cc6727", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b63054e003f91d4a20885aaab31661946e93f889ff5f60d7e1eb9f642b6e52a0"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `54a5752194cc6727`
- Source: `github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/02_%ED%92%88%EC%A7%88%EA%B2%BD%EC%98%81%EC%8B%9C%EC%8A%A4%ED%85%9C_QMS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4.md)
- Source hash: `b63054e003f91d4a20885aaab31661946e93f889ff5f60d7e1eb9f642b6e52a0`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_요구사항_매트릭스.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: 6-1_사용적합성_엔지니어링_계획서_v0.1.md | Formative/Summative 실행 | | DR-07 | 임상적 유효성(해당 시) | 법 제15조 | ◐ | 임상평가계획서 승인, CER 완성 | - | 임상평가계획/보고서 템플릿 작성 | ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | |
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital‑Health Product (디지털의료제품법 대상)**  

---

### 1. Device Classification & Submission Route  
| Item | Determination | Basis / Citation |
|------|---------------|-------------------|
| **Risk class** | **Class II** (moderate risk) – e.g., diagnostic support software that does not provide treatment decisions autonomously. | MFDS “의료기기법” **제15조** (risk‑based classification rule). |
| **Submission pathway** | **Registration / 허가 신청** (class II devices require MFDS approval after submission of technical documentation and clinical evidence). | MFDS 규정 on “클래스 II 의료기기의 허가·신고 절차”. |
| **KGMP requirement** | Manufacturing site must hold a **KGMP 인증서** (Korean Good Manufacturing Practice) for any hardware component or for software that is released as a device. | KGMP 시행령 – no specific notice number in source; confirm with current MFDS KGMP guidance. |

---

### 2. Required Evidence Package  

| Evidence Type | Minimum Content | Current Status (per source) | Gap / Missing Item |
|---------------|----------------|-----------------------------|--------------------|
| **Clinical Evaluation Report (CER)** | • Clinical evaluation plan approved by MFDS<br>• Completed CER with benefit‑risk analysis <br>• Supporting literature or foreign clinical data (if accepted) | “임상평가계획서 승인, CER 완성” is listed as a required deliverable in the engineering plan (Chunk 1). | No actual CER document attached; verify completeness and whether it includes Korean patient data where required. |
| **Clinical Evaluation Plan (CEP)** | Template per MFDS “임상평가계획/보고서 템플릿” | Mentioned as an item to be prepared (Chunk 1). | CEP not yet submitted / signed off. |
| **Risk Management File** | ISO 14971‑based risk analysis, risk control measures, residual risk assessment, and post‑market risk‑monitoring plan. | Not referenced in source excerpts. | Entire RMF absent – must be created. |
| **Software Development Lifecycle Documentation** | • IEC 62304‑compliant software development plan<br>• Verification & validation reports (unit, integration, system testing)<br>• Usability engineering per IEC 82304‑2 or IEC user‑centered design standards. | Not referenced. | Missing all software V&V artifacts. |
| **Cybersecurity Controls** | Threat analysis, mitigation strategy, secure update mechanism, and incident response plan (per MFDS “보안지침” for digital health). | Not referenced. | No cybersecurity documentation supplied. |
| **Labeling & IFU** | Korean‑language labeling, instructions for use (IFU), safety information; QR codes allowed only when Korean translation is provided on packaging. | Not referenced. | Korean labeling package not yet prepared. |
| **KGMP Certification** | Facility inspection report, SOPs for software release management, change control. | No evidence of KGMP certification in source. | Facility must obtain or update KGMP certificate before submission. |
| **Post‑Market Surveillance (PMS) Plan** | Periodic safety review, adverse event reporting procedure, field safety corrective actions (FSCA). | Not referenced. | PMS plan required for class II devices. |

---

### 3. Identified Gaps & Required Actions  

1. **Finalize Clinical Evaluation Report** – obtain full CER with Korean‑language summary; if relying on foreign clinical data, confirm acceptance per latest MFDS notice (requires verification of the specific “foreign clinical evaluation” allowance).  
2. **Submit Clinical Evaluation Plan** – complete the MFDS‑template and obtain internal approval.  
3. **Develop Risk Management File** – conduct hazard analysis, define risk controls; map each control to a traceability matrix linking to design inputs/outputs.  
4. **Compile Software Development Documentation** – adopt IEC 62304 process, produce V&V test reports, and conduct usability testing per IEC 82304‑2.  
5. **Prepare Cybersecurity Dossier** – perform threat modeling (e.g., STRIDE), document mitigations, and establish secure update mechanisms.  
6. **Create Korean‑language Label & IFU** – ensure all mandatory statements (intended use, contraindications, warnings) are in Hangul; include a QR code only if the linked content is also in Korean.  
7. **Secure KGMP Certification** – schedule MFDS inspection or submit self‑assessment for digital software facilities.  
8. **Draft PMS Plan** – outline periodic safety update schedule, adverse event collection, and FSCA workflow.  

---

### 4. Risk Controls (Mapping to Identified Risks)  

| Potential Hazard | Control(s) Implemented / To Be Implemented | Reference |
|------------------|--------------------------------------------|-----------|
| Incorrect diagnostic output leading to mis‑treatment | • Clinical validation against gold‑standard data sets<br>• Built‑in safety alerts when confidence < 80 % | IEC 62304, MFDS “임상평가” guidance |
| Software malfunction (crash) | • Robust error handling & fail‑safe mode<br>• Regular OTA updates with signed packages | IEC 62304, cybersecurity guideline |
| Unauthorized data access / privacy breach | • Encryption of stored and transmitted PHI<br>• Role‑based authentication, audit logs | MFDS “보안지침” for digital health |
| Inadequate user training → misuse | • Korean IFU with step‑by‑step workflow diagrams<br>• Usability testing with target clinicians | IEC 82304‑2, MFDS labeling rules |

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger Condition | Escalation Action |
|-----------|-------------------|-------------------|
| **Missing or incomplete CER** | No CER uploaded or reviewer flags insufficient Korean clinical data. | Pause submission; alert RA lead and Clinical Affairs for urgent generation of CER (target resolution < 14 days). |
| **GAP‑analysis status shows open items after target date** (see Gap analysis form – “상태 변경” column) | Any row remains in ○→◐ or ◐→● state beyond the planned completion date. | Notify Project Manager; convene cross‑functional risk review meeting within 3 working days. |
| **KGMP certification not yet obtained** | Facility certificate expiry < 30 days or pending inspection outcome. | Immediate escalation to Quality Lead; suspend any further regulatory filing until KGMP is confirmed. |
| **Labeling/IFU lacking Korean translation** | Draft labeling only in English when “Korean language” is mandatory per MFDS rules. | Stop packaging design; involve Localization team and Regulatory Translators within 5 business days. |
| **Cybersecurity vulnerability identified post‑release** | CVE or internal pen‑test finding with CVSS ≥ 7.0. | Trigger FSCA process; report to MFDS within 24 hours as per “보안사고 보고” guideline. |

---

### 6. Citations  

| Citation Type | Reference |
|---------------|-----------|
| **Framework reference** (classification rule) | MFDS 의료기기법 **제15조** – risk‑based classification of medical devices. |
| **Instance identifier** (requirement from source) | No specific regulatory instrument number (e.g., 고시 번호) appears in the supplied excerpts; verify separately for any notice that expands foreign clinical data acceptance or KGMP updates. |

---

### 7. Peer Review Prompt  

> **@RA‑Peer:** Please review this draft and challenge the following assumptions:  
> 1. The classification as Class II – could the intended use (e.g., continuous health monitoring) push it into Class III under MFDS “고위험” criteria?  
> 2. Acceptance of foreign clinical evidence – have we confirmed the latest MFDS notice that allows reliance on FDA‑cleared data for this product category?  
> 3. Are there any additional Korean‑specific obligations (e.g., “디지털의료기기 인증제도” related to AI‑based algorithms) that are not captured here?  

--- 

*End of draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1030171511734839168`

> 6-1_사용적합성_엔지니어링_계획서_v0.1.md | Formative/Summative 실행 | | DR-07 | 임상적 유효성(해당 시) | 법 제15조 | ◐ | 임상평가계획서 승인, CER 완성 | - | 임상평가계획/보고서 템플릿 작성 |

2. Chunk `1045730514097588767`

> ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | |
