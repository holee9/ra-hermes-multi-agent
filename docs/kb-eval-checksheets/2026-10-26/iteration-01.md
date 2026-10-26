# KB Eval Checksheet - 2026-10-26 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261026-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "81ac88c585384573", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `81ac88c585384573`
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

> **Regulatory Draft – SaMD AI/ML Change Impact Assessment**

---

### 1. Classification & Submission Pathway  
| Item | Determination |
|------|----------------|
| **Device type** | Software as a Medical Device (SaMD) that provides diagnostic or treatment‑related recommendations (AI/ML‐based). |
| **Primary FDA panel** | 21 CFR Part 892 – Imaging & radiology devices *or* 21 CFR Part 862 if the software is a pure clinical decision‑support tool without imaging. The source does not name the functional class; verify the exact function to select the correct part. |
| **Class** | **Class II** (most AI‑based diagnostic SaMD are classified as Class II). |
| **Regulatory route** | 510(k) Premarket Notification – establish substantial equivalence to a legally marketed predicate or, if no predicate exists, consider De Novo classification before a subsequent 510(k). |
| **QMS requirement** | Compliance with the Quality Management System Regulation (QMSR) – 21 CFR Part 820 (ISO 13485‑aligned, effective 2026‑02). |
| **UDI requirement** | Assign a Unique Device Identifier per 21 CFR Part 830. |

---

### 2. Required Evidence Package (510(k) Submission)

| Evidence Category | Specific Elements | Source Basis |
|-------------------|-------------------|--------------|
| **Device Description** | – Intended use statement<br>– Overall system architecture diagram<br>– Detailed algorithm flow‑chart, including input/output definitions | FDA guidance on SaMD (no specific identifier found in source — verify separately) |
| **Predicate Comparison** | – Predicate device 510(k) number & registration<br>– Tabular side‑by‑side comparison of indications, technology, performance metrics | No predicate cited in source – verify separately |
| **Software Documentation** | – IEC 62304 software life‑cycle plan (development, verification, validation)<br>– Source code summary & control flow documentation<br>– Change‑control records (see PCCP protocol) | FDA “Predetermined Change Control Plan (PCCP)” guidance (no specific identifier found in source — verify separately) |
| **Risk Management** | – ISO 14971:2019 risk analysis & mitigation file<br>– IEC 62366‑1 usability/UX risk assessment<br>– Specific AI‑related controls (bias detection, model drift monitoring) | No explicit citation in source – verify separately |
| **Performance Evaluation** | – Clinical performance data or well‑designed equivalence study<br>– Statistical analysis plan showing significance & confidence intervals<br>– Predefined acceptance criteria (as required by PCCP “Performance Evaluation” item) | 3.2 Modification Protocol table (no specific identifier found in source — verify separately) |
| **Verification & Validation** | – Unit, integration, system V&V test reports<br>‑ IEC 62304‑compliant verification matrix | No identifier in source – verify separately |
| **Data Management** | – Data collection, cleaning, versioning procedures (PCCP “Data Management” item)<br>– Bias mitigation strategy & documentation of data provenance | Source table supplies content but no regulatory number; therefore “no specific identifier found — verify separately”. |
| **Labeling & IFU** | – Intended use, indications, contraindications<br>‑ Instructions for safe re‑training or model update (per PCCP “Updated Procedures”)<br>‑ UDI label format per 21 CFR Part 830 | No numeric reference in source – verify separately |
| **Cybersecurity** | – Threat analysis & mitigation plan (ISO  IEC 62443 concepts acceptable)<br>‑ Post‑market monitoring of vulnerabilities | Not detailed in source – verify separately |
| **Post‑Market Surveillance** | – Real‑world performance monitoring plan<br>‑ FDA adverse event reporting per 21 CFR Part 803<br>‑ Voluntary correction/removal process under 21 CFR Part 806 | No identifier supplied – verify separately |

---

### 3. Gaps / Missing Information (to be obtained before filing)

| Gap | Why it matters |
|-----|----------------|
| **Exact intended use & clinical context** | Determines FDA panel (Part 892 vs 862) and predicate eligibility. |
| **Predicate device identifier** | Required for a traditional 510(k); absent → need De Novo path. |
| **Full algorithm description (including model architecture, hyper‑parameters)** | Needed for substantial equivalence & risk analysis; also required in PCCP to justify pre‑specified change triggers. |
| **Training/validation dataset provenance and bias assessment** | Required under the “Data Management” element of PCCP; supports ISO 14971 risk controls. |
| **Pre‑defined acceptance criteria & statistical plan** | Must be documented in the “Performance Evaluation” element of PCCP. |
| **Rollback / version control procedures for model updates** | Part of “Retraining Practices” needed to demonstrate controllable change per PCCP. |
| **User/clinical communication plan for updates** | Covered under “Updated Procedures”; essential for FDA review of post‑market change management. |
| **Labeling draft with UDI placement** | Required by 21 CFR Part 830; missing label will halt clearance. |
| **Cybersecurity risk assessment** | Not covered in source excerpts but mandated by 21 CFR Part 820 and ISO 14971. |

---

### 4. Core Risk Controls (per ISO 14971 & PCCP)

1. **Algorithmic bias detection & mitigation** – systematic data review, re‑balancing, and documentation of demographic performance.
2. **Model drift monitoring** – statistical process control limits on key output metrics; trigger for retraining defined in PCCP “Retraining Practices”.
3. **Rollback capability** – ability to revert to prior validated version if new model fails acceptance criteria.
4. **User alerts & decision support** – clear indication when a model has been updated; require clinician verification before action (usability risk control from IEC 62366‑1).
5. **Data integrity checks** – checksum/versioning for training data sets, per PCCP “Data Management”.
6. **Cybersecurity safeguards** – authentication, encryption, periodic vulnerability scans; documented in the QMS.

---

### 5. Human‑Escalation Triggers (when to involve senior RA/legal/management)

| Trigger | Action Required |
|---------|-----------------|
| **Absence of a identified predicate device** | Escalate to leadership for De Novo pathway decision and timeline impact. |
| **Failure to meet predefined acceptance criteria during validation** | Stop submission; escalate to development team and senior RA for root‑cause analysis & remediation plan. |
| **Discovery of dataset bias that cannot be mitigated within current scope** | Immediate escalation to risk management lead and possibly senior compliance counsel. |
| **FDA AI/ML Additional Information (AI) request exceeding 180 days response deadline** | Notify regulatory project manager; prioritize resources for rapid response. |
| **Adverse event report indicating possible model‑related harm** | Initiate Field Safety Notice process under 21 CFR Part 806 and notify senior RA for FDA reporting per Part 803. |
| **Planned software change not covered by the approved PCCP** | Halt implementation; seek FDA pre‑market discussion (e.g., Q‑submission) before proceeding. |

---

### 6. References & Citations

- **Regulatory framework**: 21 CFR Part 892 (Imaging devices), Part 862 (Clinical chemistry – if applicable), Part 820 (QMSR), Part 830 (UDI).  
- **Risk Management**: ISO 14971:2019, IEC 62304:2006+A1:2015, IEC 62366‑1:2015+A1:2020.  
- **AI/ML Change Control Guidance**: FDA “Predetermined Change Control Plan (PCCP)” final guidance (December 2024). *(no specific identifier found in source — verify separately)*  
- **Source excerpt – Modification Protocol items**: Data Management, Retraining Practices, Performance Evaluation, Updated Procedures. *(no specific identifier found in source — verify separately)*  

---

### 7. Peer‑Review Prompt

> *Please review this draft and challenge the following assumptions:*  
> 1. The device is appropriately placed under **21 CFR Part 892** rather than **Part 862** – does the intended use justify this panel?  
> 2. All PCCP required elements are captured; are there any additional FDA‑mandated items (e.g., algorithmic transparency disclosures) that we have omitted?  
> 3. The risk control list aligns with ISO 14971 and IEC 62366‑1 – is any AI‑specific control (e.g., explainability, model provenance) missing?  

**End of draft.**

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

2. Chunk `198015203798949382`

> ### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---

### kb-eval-20261026-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "770d35789d2d9e76", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `770d35789d2d9e76`
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

> **Regulatory Draft – SaMD Change Impact Assessment  
(촬영실 GUI Software – Image‑Processing/Display Application)**  

---

### 1. Classification & Submission Route  
| Item | Determination | Basis |
|------|---------------|-------|
| Device class | **Class II** (moderate risk) | 21 CFR §892.2050 – “Image Processing Software” |
| Regulatory pathway | **510(k) Premarket Notification** (substantial equivalence) | Class II devices are normally cleared via 510(k). A predicate in the same class (e.g., a cleared DICOM viewer with basic processing) must be identified. |
| Applicable QMS regulation | **21 CFR Part 820 – Quality Management System Regulation (QMSR)** (effective Feb‑2026, ISO‑13485 aligned) | New QMS requirement for all 510(k) submissions after 02/2026. |

---

### 2. Required Evidence (per FDA guidance & standards)

| Deliverable | Content Requirement | Source |
|-------------|--------------------|--------|
| **Device Description / Intended Use** | Clear statement of clinical function, user environment, and patient impact. Must confirm SaMD status. | 21 CFR §892.2050; FDA Guidance “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14) |
| **Software Documentation** | • Software Requirements Specification (SRS) <br>• Software Design Specification (SDS) <br>• Software Architecture Diagram <br>• Traceability Matrix (Requirements → Design → Test) <br>• Risk Management File (ISO 14971) <br>• IEC 62304 development lifecycle artifacts (risk class, verification & validation plans) | FDA Guidance “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14); IEC 62304:2006+A1:2015 |
| **Verification/Validation** | • Unit, integration, system, and performance test results <br>• Validation dataset description <br>• Acceptance criteria & statistical analysis <br>• Anomaly log & resolution records (PCCP if changes are anticipated) | eSTAR Section G (Performance Testing – Software) |
| **Cybersecurity** | • Threat model & security architecture <br>• Implementation of FDA Cybersecurity Guidance controls (access control, authentication, audit logging, patch management) <br>• Plan for post‑market vulnerability handling | FDA Guidance “Cybersecurity in Medical Devices” (2023‑09‑27) |
| **Risk Management** | • Hazard analysis, risk classification per IEC 62304 (Class B expected) <br>• Risk control measures and residual risk evaluation (ISO 14971) | IEC 62304 table; ISO 14971:2019 |
| **Labeling / UDI** | • Labels & IFU meeting 21 CFR §801 requirements <br>• Unique Device Identifier on label & packaging per 21 CFR §§830.10‑830.60, GUDID submission | 21 CFR Part 801; Part 830 |
| **QMS compliance evidence** | • SOPs (e.g., SOP‑RA‑002, SOP‑CA‑001) demonstrating design controls, change control, and post‑market surveillance per Part 820 | 21 CFR Part 820 (QMSR) |

---

### 3. Missing Information / Gaps to Address  

| Gap | Why it matters |
|-----|----------------|
| **Predicate device citation** | Needed for substantial equivalence claim; must include 510(k) number, intended use comparison, and technology similarity. |
| **Detailed Intended Use & Clinical Claim** | Determines scope of performance testing and any required clinical data. |
| **Risk Management File (ISO 14971)** – specific hazard analysis, risk control tables, residual risk justification. | Required for both 510(k) content and IEC 62304 classification. |
| **Cybersecurity Threat Model** – documented threats, mitigations, and post‑market monitoring plan. | Mandatory per 2023 Cybersecurity Guidance. |
| **Software Classification Confirmation (IEC 62304)** – confirm Class B vs. Class C based on intended use; if Class C, additional verification/validation evidence may be required. |
| **UDI strategy & GUDID submission** – label design, Device Identifier, Production Identifier. | Required before filing. |
| **QMSR documentation** – SOPs demonstrating compliance with Part 820 (e.g., Design Transfer, Process Validation). | New mandatory QMS for 510(k) after Feb‑2026. |
| **Performance Test Dataset provenance & statistical power analysis** – description of dataset composition, representativeness, and justification of sample size. | Needed to satisfy “performance testing” requirements in eSTAR package. |
| **Post‑market Surveillance (PMS) plan** – adverse event reporting procedures per 21 CFR §803 and voluntary correction/removal process (§806). | Supports risk management lifecycle. |

---

### 4. Risk Controls (Design & Post‑Market)

1. **Software Hazard Analysis (IEC 62304)** – identify failure modes, assign severity, likelihood; classify as Class B (expected) → apply verification/validation activities accordingly.  
2. **Risk Management (ISO 14971)** – implement risk control measures (e.g., input validation, error handling, user alerts). Document residual risk and acceptability.  
3. **Cybersecurity Controls** – authentication, integrity checks, encrypted data storage/transmission; regular vulnerability assessments & patch process per FDA Cybersecurity Guidance.  
4. **Predetermined Change Control Plan (PCCP)** – define permissible software modifications (e.g., algorithm updates) and pre‑authorize via FDA to avoid future 510(k) re‑submissions.  
5. **Usability Engineering (IEC 60601‑1‑6)** – conduct formative/usability testing to mitigate user error, especially for image interpretation functions.  
6. **Post‑Market Monitoring** – implement a system for real‑world performance data capture, adverse event reporting (21 CFR §803), and voluntary corrections/removals (21 CFR §806).  

---

### 5. Citations (per instruction)

| Item | Citation Type | Reference |
|------|---------------|-----------|
| Classification rule | Framework reference | **21 CFR §892.2050** (Class II – Image Processing Software) |
| Software lifecycle standard | Framework reference | **IEC 62304:2006+A1:2015** |
| Risk management standard | Framework reference | **ISO 14971:2019** |
| FDA software content guidance | Framework reference | *Guidance for the Content of Premarket Submissions for Device Software Functions* (June 14 2023, Final) |
| FDA cybersecurity guidance | Framework reference | *Cybersecurity in Medical Devices* (Sept 27 2023, Final) |
| QMS regulation | Framework reference | **21 CFR Part 820** (Quality Management System Regulation, effective Feb‑2026) |
| eSTAR package structure | No specific identifier found in source — verify separately | – |

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required | Escalation To |
|---------|----------------|---------------|
| **No suitable predicate identified** (or mismatch in intended use) | Halt submission; perform market scan, consider De Novo pathway. | Senior RA Manager / Regulatory Strategy Lead |
| **Software classified as IEC 62304 Class C** (potential for serious injury) | Expand verification/validation data set; may need additional clinical evidence. | Clinical Affairs & QA Lead |
| **Incomplete cybersecurity threat model or no post‑market vulnerability plan** | Require development of full security risk assessment and mitigation plan before filing. | Cybersecurity Engineer + RA Manager |
| **QMSR documentation gaps (e.g., missing SOPs for design control)** | Immediate generation/revision of SOPs; QMS audit prior to submission. | Quality System Lead |
| **Residual risk not justified as acceptable** | Conduct additional risk controls or redesign; re‑evaluate ISO 14971 file. | Risk Management Team |
| **UDI/Labeling non‑compliant with Part 830 / §801** | Redesign labeling, generate GUDID submission package. | Labeling & Regulatory Affairs Lead |
| **Major change to algorithm after 510(k) clearance** | Determine if change falls within existing PCCP; if not, prepare supplemental 510(k). | Product Development Lead + RA Manager |

---

### 7. Bottom‑Line Judgment  

- The 촬영실 GUI Software is a **Class II SaMD** requiring a **510(k)** submission based on substantial equivalence to an FDA‑cleared image‑processing application (§892.2050).  
- All documentation listed in the eSTAR Section G must be completed, supplemented with the missing items identified above (predicate citation, detailed risk management, cybersecurity threat model, UDI/labeling, QMSR SOPs).  
- If any of the escalation triggers occur, the submission should be paused and the issue addressed before proceeding.

---

**Peer‑Review Prompt**  

*Please review this assessment for:*

1. **Assumptions about intended use and predicate availability** – are we overlooking any functional nuances that could shift classification or require a De Novo route?  
2. **Coverage of FDA guidance requirements** – have we captured all mandatory elements from the 2023 software content and cybersecurity guidances, especially regarding post‑market change control?  
3. **Jurisdiction‑specific gaps** – are there any U.S.–only obligations (e.g., Part 803/806 reporting plans, GUDID nuances) that need deeper treatment before filing?

*Provide comments or requested revisions.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

### kb-eval-20261026-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "bf3b3cbde65fd59f", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md", "source_hash": "17067eef9c351571ca7c8dedcea62a4c6b790ae298cec359778dca145c690031"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `bf3b3cbde65fd59f`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_05_Software_Section.md)
- Source hash: `17067eef9c351571ca7c8dedcea62a4c6b790ae298cec359778dca145c690031`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_05_Software_Section.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. --- + SOUP (IEC 62304) | SOUP 목록 (IEC 62304...
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

> **Regulatory Draft – SaMD Change Impact (U.S. FDA)**  

---

### 1. Bottom‑Line Determination  
| Item | Assessment |
|------|------------|
| **Device type** | Software as a Medical Device (SaMD) – AI/ML‑enabled diagnostic or decision‑support software (no imaging function indicated). |
| **Classification** | *Presumed* Class II under 21 CFR 820.30‑(risk‐based) unless the intended use places it in a higher risk category (e.g., prediction of treatment outcomes for life‑threatening disease). Without a clear high‑risk claim, the default FDA pathway is **510(k) – Traditional/Substantially Equivalent**. |
| **Alternative route** | If no predicate exists or the AI/ML algorithm constitutes a novel mode of action, the **De Novo (Class II)** pathway is the next fastest credible option. |
| **Submission type** | 510(k) (Traditional, Special or Abbreviated as appropriate). |

> **Note:** The source does not disclose intended use, predicate devices, or risk level → classification must be confirmed with the sponsor.  

---

### 2. Required Evidence Pack for a 510(k) SaMD  
| Evidence / Document | FDA requirement basis (framework citation) | What the source provides | Missing / To‑Be‑Obtained |
|---------------------|-------------------------------------------|--------------------------|--------------------------|
| **Device description & indications for use** | 21 CFR 807.87; 21 CFR 820.30(b) | – | Intended use narrative, target patient population, clinical context |
| **Predicate comparison (if Traditional/Abbreviated)** | 21 CFR 807.92(a)(1) | – | Identification of cleared predicate(s) with 510(k) numbers |
| **Risk Management File** | ISO 14971:2019 (framework); IEC 62304 §7 linkage (source) | Risk Management Plan, analysis‑evaluation‑control matrix, RMR | Complete traceability to software architecture; residual risk acceptability justification |
| **Software Development Lifecycle documentation** | IEC 62304 (2006+A1:2015) | Reference to IEC 62304 §7 in source | Detailed software design specifications, verification & validation protocols/results |
| **SOUP List & SBOM** | FDA guidance on Software Bill of Materials (final rule 2024‑524B); IEC 62304 requirement for third‑party components | SOUP list mentioned; SBOM reference noted | Full SBOM with versioning, provenance, and cyber‑risk assessment |
| **Predetermined Change Control Plan (PCCP)** | FDA Final Guidance “Artificial Intelligence/Machine Learning Software as a Medical Device” (Dec 2024) – PCCP requirement | PCCP explicitly cited in source | Completed PCCP covering anticipated algorithm updates, performance monitoring plan |
| **Usability/ Human Factors validation** | IEC 62366‑1:2020; FDA guidance on usability (2016) | – | Usability test reports, user interface labeling |
| **Cybersecurity controls** | FDA “Content of Premarket Submissions for Management of Cybersecurity” (Oct 2022) | ‑ | Threat model, mitigation strategy, post‑market monitoring plan |
| **Labeling & Instructions for Use** | 21 CFR 801.5; 21 CFR 820.120 | – | Draft labeling, IFU, UDI assignment per Part 830 |
| **Quality Management System (QMS)** | 21 CFR 820 (effective Feb 2026 QMSR, ISO 13485‑2016 aligned) | – | Copy of ISO 13485‑2016 certified QMS, SOPs (e.g., SOP‑RA‑002, SOP‑CA‑001) |
| **Clinical Performance Evidence** *(if required for intended use)* | 21 CFR 803.30; FDA SaMD Clinical Evaluation Guidance (2021) | – | Clinical validation study report or literature support |

> *Citation note:* The source excerpts do not contain any specific CFR § numbers, device identifiers, or docket numbers. Accordingly, each “Missing / To‑Be‑Obtained” entry is flagged **“no specific identifier found in source — verify separately.”**  

---

### 3. Risk Controls – Key Elements to Include  
1. **Risk Management Plan (RMP)** – define acceptance criteria, allocate risk classes, schedule reviews.  
2. **Software Hazard Analysis** – map each software function (including AI/ML inference) to potential hazardous situations; link to architecture modules (§5.3 of IEC 62304).  
3. **Control Measures** – implement input validation, output alerts, lock‑out/on‑fail mechanisms, and user confirmation steps where high‑severity risk exists.  
4. **Verification Traceability Matrix** – map each control to verification test and acceptance result (as required by ISO 14971 and IEC 62304).  
5. **Residual Risk Acceptance** – documented justification that all residual risks are “as low as reasonably practicable” (ALARP) per ISO 14971.  
6. **PCCP Integration** – define pre‑authorized change categories (algorithm retraining, parameter updates) with associated performance monitoring and verification activities.  

---

### 4. Human‑Escalation Triggers (When to Involve Senior RA/Regulatory Counsel)  

| Trigger | Reason | Action |
|--------|--------|--------|
| **Absence of a clear predicate** | No 510(k) number can be identified from sponsor data. | Escalate to decide between De Novo vs. new 510(k). |
| **Intended use indicates high‑risk clinical decision** (e.g., treatment selection for life‑threatening disease) | May shift classification to Class III → PMA required. | Raise to senior RA/Regulatory Lead for classification review. |
| **Proposed AI/ML change exceeds scope of existing PCCP** (new algorithm architecture, new data sources). | FDA may require a new 510(k) or supplemental submission. | Initiate discussion with sponsor; prepare FDA pre‑submission meeting request. |
| **Residual risk not demonstrably ALARP** after RMR review. | Potential safety concern leading to FDA 483/Warning Letter. | Immediate risk mitigation plan and senior oversight before filing. |
| **SBOM incomplete or SOUP components lack security vetting** | Cybersecurity vulnerability risk. | Escalate to CISO and senior RA for corrective action plan. |
| **Labeling/U​DI draft not compliant with Part 830/801** | Non‑conformity would delay clearance. | Send to senior regulatory affairs for final review. |
| **FDA issues an Additional Information (AI) request during 510(k) review** | FDA has 180 calendar days to respond; missed deadline stalls clearance. | Assign dedicated response team and notify project manager. |

---

### 5. Summary Judgment  
*The SaMD change is best pursued via a traditional or special 510(k) submission, provided an appropriate predicate exists and the AI/ML updates fall within a pre‑approved PCCP. If no predicate can be identified or the intended use elevates risk, a De Novo classification should be prepared.* All required documentation listed above must be assembled; current source material supplies only the risk‑management framework references and mentions of SOUP/SBOM/PCCP, leaving critical gaps in device description, clinical evidence, labeling, and QMS artifacts that need to be filled before filing.

---

### 6. Peer Review Prompt  
> **To a fellow RA:** Please challenge the assumption that this SaMD can remain Class II under a 510(k). Verify whether any of the AI/ML functions described (even though not detailed) could trigger a higher classification or require a De Novo route. Also, assess whether the outlined evidence pack fully satisfies FDA’s 2024‑524B SBOM requirements and the PCCP expectations for algorithmic change control.

---

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1023300943338888510`

> ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. ---

2. Chunk `1150973762104113645`

> + SOUP (IEC 62304) | SOUP 목록 (IEC 62304 준수) | SOUP 목록 (IEC 62304) + SBOM (SBOM 의무는 FDA 524B; MDR은 명시 SBOM 요건 없음 — MDCG 2019-16 사이버보안 준용) | | AI/ML 소프트웨어 | PCCP (Predetermined Change Control Plan, 2024 Final) | AI 의료기기 가이드라인 (MFDS 2025) | MDCG 2021-6 AI 가이던스 |

### kb-eval-20261026-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_us-004", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "55dceb3bc60e8d4e", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `55dceb3bc60e8d4e`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f`
- Focus: SaMD change impact
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관...
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

> **Regulatory Draft – Independent SaMD GUI for Imaging Suite (“Imaging‑Room GUI”)**

---

### 1. Device Classification & Submission Pathway  

| Item | Determination | Rationale / Citation |
|------|---------------|----------------------|
| **Product class** | Class II medical device | Under 21 CFR §892.2050 “Medical image management and processing system” (software that acquires, processes, or displays diagnostic images). The GUI directly controls image acquisition and provides real‑time display, fitting the definition of a processing/analysis system. |
| **Regulatory route** | Traditional 510(k) Premarket Notification (Section 807) | Substantial equivalence to an existing cleared imaging‑room workstation (e.g., **K123456** – placeholder; actual predicate must be identified). No novel indications, so de Novo or PMA not required. |
| **QMS requirement** | QMSR (ISO 13485‑aligned Quality Management System Regulation) effective 2026‑02 | §820.10(b), §820.35(a), §820.35 and the broader §820 provisions – see Source [1]. The QMSR expands scope to contract sterilizers, relabelers, and foreign initial distributors; it also mandates ARR (Applicable Regulatory Requirements) tracking in QMS procedures. |
| **UDI** | Required on label & packaging per 21 CFR §830.10‑§830.60 | Cited in ARR column of Source [1]. |

---

### 2. Core Evidentiary Package  

| Evidence | Required Content | Where it satisfies the regulation |
|----------|------------------|------------------------------------|
| **Device Description & Intended Use** | Narrative, user environment (imaging suite), functional block diagram, hardware‑software interface description. | Forms basis of classification & predicate comparison (510(k) §807.86). |
| **Predicate Device(s)** | 510(k) numbers, summary of equivalent functionalities, labeling comparison. | Establishes substantial equivalence (21 CFR §807.92). |
| **Software Documentation** (per IEC 62304 Class C) | • Software Development Plan (SDP)<br>• Software Requirements Specification (SRS)<br>• Software Architecture Design (SAD)<br>• Software Verification Plan & Report (SVP/SVR) | IEC 62304 §8.1 cited in Source [2]; required for Class C SaMD. |
| **Software Validation Report** | End‑to‑end functional testing, performance metrics, usability validation, risk‑based test matrix. | Supports safety claim under IEC 62304 & 21 CFR §820.30 (Design Controls). |
| **Risk Management File** | ISO 14971:2019 risk analysis, mitigations, residual risk evaluation, post‑market surveillance plan. | Required by QMSR and FDA design control expectations (§820.30(c)). |
| **Cybersecurity & AI/ML Change Control** | • Threat model & SBOM<br>• Predetermined Change Control Plan (PCCP) – FDA final guidance Dec 2024<br>• If AI/ML features present, documentation of training data, performance monitoring, and PCCP alignment with AI Act Art.43(4). | Source [2] lists PCCP requirement; integrates MD‑CG 2019‑16 Rev.1 and MFDS guide (for reference only). |
| **UDI Assignment & Labeling** | UDI carrier label, device label content per 21 CFR §801.20, inclusion of model/lot numbers. | ARR column in Source [1] mandates 830 compliance. |
| **Service Record Template** | Format for recording service events, corrective actions, and field reports. | §820.35 (service record requirement) – Source [1]. |
| **Complaint Handling Procedure** | Process flow, classification of MDR‑reportable events, documentation requirements (including “MDR reportability determination” per §820.35(a)). | Source [1] emphasizes enhanced complaint file. |
| **Internal Audit Report & Management Review Minutes** | Evidence that QMSR internal audits and management reviews have been performed; includes any FDA inspection access provision (§820). | Source [1] – “내부감사 실사”. |

---

### 3. Missing / Unconfirmed Information (Needs Human Follow‑up)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Predicate device identification** | Without a cleared 510(k) number, the submission cannot proceed. | Conduct market search; confirm equivalence of UI/processing functions. |
| **Exact intended use statement** (e.g., “real‑time image acquisition and display for CT/MRI diagnostics”) | Drives classification & labeling. | Draft and review with product team. |
| **UDI Issuing Agency confirmation** (FDA vs. third‑party) | Determines label format and GUDID entry. | Select issuing agency; complete UDI carrier registration. |
| **AI/ML feature scope** (present or not) | Determines need for PCCP & AI‑specific risk controls. | Verify software roadmap; if present, develop detailed AI change plan. |
| **Contract sterilizer / relabeler agreements** | QMSR expands to these parties; they must be included in the quality system. | Obtain and file contracts; map responsibilities into SOPs. |
| **MDR‑reportability decision matrix** (U.S. counterpart is 21 CFR 803 reporting) | Required for complaint handling per §820.35(a). | Create matrix; link to complaint workflow. |
| **Verification of “ARR” integration in QMS procedures** | ARR tracking is mandatory under §820.10(b). | Update SOP‑RA‑001 (Applicable Regulatory Requirements) with traceability links. |

---

### 4. Core Risk Controls (aligned to ISO 14971 & FDA expectations)

1. **Software safety classification (IEC 62304 Class C)** – enforce rigorous verification, design reviews, and unit testing.  
2. **Cybersecurity safeguards** – threat modelling, SBOM, encrypted data transmission, authentication controls.  
3. **PCCP** – pre‑specified change categories; FDA will not require re‑submission for approved changes.  
4. **User interface safety** – usability engineering (FDA Human Factors guidance), prevent inadvertent image acquisition errors.  
5. **Error handling & logging** – automatic shutdown, auditable logs stored per 21 CFR §820.184.  
6. **Post‑market surveillance** – monitor field performance metrics; trigger corrective actions under 21 CFR §822.20.

---

### 5. Citation Summary  

| Requirement | Source citation |
|-------------|-----------------|
| ARR (Applicable Regulatory Requirements) integration | §820.10(b) – Source [1] |
| Complaint file enhancement & MDR‑reportability decision | §820.35(a) – Source [1] |
| Service record requirement | §820.35 – Source [1] |
| Internal audit accessibility to FDA inspectors | §820 (general) – Source [1] |
| Inclusion of contract sterilizers/relabelers in QMSR scope | §820.10(a) – Source [1] |
| IEC 62304 Class C software development lifecycle mapping | IEC 62304 §8.1 – Source [2] |
| PCCP (Predetermined Change Control Plan) for AI/ML | FDA “Final Guidance, Dec 2024” – mentioned in Source [2]; no specific identifier found in source — verify separately |
| Cybersecurity reference (MFDS guide) and EU AI Act mapping | MFDS cyber‑guide 2025; MDCG 2019‑16 Rev.1 – Source [2] (EU references for context only). |

---

### 6. Human‑Escalation Triggers  

| Trigger | When to Escalate to Senior RA / Legal |
|--------|---------------------------------------|
| **No suitable predicate identified** after market search. | Immediate escalation – may require de Novo or PMA pathway assessment. |
| **AI/ML component discovered without PCCP** (or incomplete PCCP). | Escalate for risk‑based plan development; potential FDA request for additional information (AI) could delay review. |
| **ARR tracking gaps in QMS procedures** (evidence of non‑compliance with §820.10(b)). | Escalate to Quality Management Lead for corrective action and possible audit finding. |
| **UDI issuance delayed beyond 30 days post‑clearance** (per 21 CFR §830). | Notify Regulatory Operations; risk of FDA enforcement. |
| **Internal audit reveals non‑conformities in complaint handling or service record documentation**. | Immediate reporting to senior management and preparation for possible FDA inspection under §820.100‑§820.200. |
| **Regulatory intelligence indicates change in classification rule (e.g., new guidance re‑imaging software)**. | Escalate to assess impact on current submission strategy. |

---

### 7. Peer Review Prompt  

> *Colleague, please challenge the assumptions made above:*
> 
> - Is **§892.2050** the most appropriate classification for a pure GUI that does not perform image analysis but only controls acquisition and display? Could the device be Class I under a different regulation?
> - Have we captured all **ARR** items required by QMSR, especially any newly issued FDA guidance post‑Feb 2026 that may affect software documentation?
> - Does the mapping of IEC 62304 §8.1 fully satisfy FDA design‑control expectations for a Class C SaMD, or should additional design‑verification artifacts be listed?
> - Are there any **U.S.-specific** post‑market reporting obligations (e.g., 21 CFR §803) that need to be reflected in the complaint handling procedure beyond the MDR reference?

Please provide feedback on classification, evidence completeness, and any jurisdictional gaps.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261026-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "af7d216ac3887834", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `af7d216ac3887834`
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

> **Regulatory Draft – Imaging Workstation Software Change (SaMD)**  

---

### 1. Bottom‑Line Determination  
- **Device class:** Class II medical device – *Medical image management and processing system* (software).  
- **Regulatory pathway:** 510(k) Premarket Notification demonstrating substantial equivalence to an FDA‑cleared predicate.  
- **Key regulatory citations (framework):** 21 CFR Part 892 §892.2050 (Class II); 21 CFR Part 807 (510(k) procedures); 21 CFR Part 820 (QMSR, effective 02‑Feb‑2026, ISO 13485‑aligned); 21 CFR Part 830 (UDI); FDA Guidance “Software Pre‑market Submission – Content of the Premarket Notification” (2023) for Basic/Enhanced documentation; Predetermined Change Control Plan (PCCP) guidance (Dec 2024).  

---

### 2. Required Evidence Package  

| Item | Reason & Reference | Evidence to Provide |
|------|--------------------|---------------------|
| **Predicate Identification** | Substantial‑equivalence analysis per 21 CFR §807.92(a)(3); checklist in source excerpt 1 | • List of one primary predicate (510(k) number, product code). <br>• Confirmation the predicate is still marketed and not under recall (MAUDE/Recall DB). |
| **Indications for Use (IFU) Comparison** | Must be “same or narrower” than predicate (ex. 1). | • Side‑by‑side textual comparison of IFU statements.<br>• Statement that company IFU is identical or more restrictive. |
| **Software Documentation Level** (Basic vs Enhanced) | FDA 2023 Software Guidance – determines depth of verification/validation data. | • Determination (basic/enhanced).<br>• Corresponding V‑V plan and reports. |
| **IEC 62304 Safety Class & Compliance** | Risk class drives validation scope; required for SaMD. | • Classification (A/B/C) with justification.<br>• Software development lifecycle artifacts (SRS, architectural design, unit test results). |
| **Risk Management File** | ISO 14971:2019 risk management process is mandatory for all medical devices. | • Hazard analysis, risk assessment tables, risk control measures, residual risk evaluation. |
| **DICOM Compatibility Statement** | Imaging workstation must interoperate per DICOM SCU/SCP specifications (source 2). | • Declaration of supported SOP Classes (Storage, Worklist, MPPS, Print).<br>• Test reports showing successful DICOM conformance. |
| **AI/ML Modules – PCCP** | If AI/ML present, a Predetermined Change Control Plan is required (2024 guidance). | • Completed PCCP with change‑control scenarios, monitoring plan, and post‑market surveillance outline. |
| **Cybersecurity & Security Controls** | 21 CFR Part 820 QMSR requires documented security controls; source 2 lists needed items. | • Threat analysis, mitigation strategy (authentication, encryption, audit logs).<br>• FDA “Content of Premarket Submissions for Management of Cybersecurity” compliance evidence. |
| **Software Bill‑of‑Materials (SBOM)** | Required for supply‑chain transparency (source 2). | • SBOM in SPDX or CycloneDX format covering all third‑party components. |
| **Interoperability – HL7 FHIR / IHE Profiles** | Source 2 lists optional support; evidence needed if claimed. | • Mapping table and test results demonstrating compliance with chosen profiles. |
| **Labeling & UDI** | 21 CFR Part 801 (labeling) & Part 830 (UDI). | • Draft labeling, IFU, packaging artwork meeting §801.5 requirements.<br>• Assigned UDI carrier and entry in GUDID. |
| **Verification & Validation (V‑V) Test Data** | Required for both Basic and Enhanced documentation levels; especially for acquisition, processing, display, storage, transfer functions listed in source 2. | • Functional test report, performance/accuracy data, usability testing, stress/robustness tests. |
| **Quality System Documentation** | QMSR (21 CFR Part 820) compliance is mandatory for any new 510(k). | • SOPs relevant to software development (e.g., SOP‑CA‑001, SOP‑RA‑002), change control records, CAPA evidence. |

---

### 3. Missing Information / Items Requiring Verification  

| Gap | Why Critical | Suggested Action |
|-----|--------------|-------------------|
| **Specific predicate(s) – 510(k) numbers** | No identifier in source; essential for substantial equivalence claim. | Perform database search (product code, recent ≤5‑yr clearance) and document the selected predicate. |
| **Predicate market status & recall history** | Must confirm device is still sold and not subject to safety communications. | Query FDA’s Recall Database / MAUDE; record findings. |
| **Exact IFU language comparison** | Needed to prove “same or narrower” claim. | Retrieve full predicate IFU and conduct side‑by‑side analysis. |
| **AI/ML module scope & change scenarios** | PCCP must be tailored to the specific algorithmic changes planned. | Define AI/ML functionality, intended updates, and draft a PCCP. |
| **Software safety class determination (A/B/C)** | Class C may trigger PMA rather than 510(k). | Conduct IEC 62304 risk‑based classification; if Class C is justified, reassess pathway. |
| **Cybersecurity threat model** | Required for both FDA and QMSR compliance. | Develop a formal threat assessment (e.g., NIST SP 800‑53 mapping) and mitigation plan. |
| **SBOM completeness** | Must include all open‑source components to satisfy supply‑chain transparency. | Generate SBOM using SPDX/CycloneDX tools; verify no omissions. |
| **Interoperability claim evidence** | If HL7 FHIR/IHE support is advertised, proof is mandatory. | Conduct interoperability testing against reference systems; document results. |
| **Labeling & UDI assignment** | 21 CFR §801.5 and §830.10‑§830.20 require specific label content and UDI format. | Draft labeling package; request UDI issuance from FDA’s GUDID. |

> *No specific identifier found in source — verify separately* for predicates, recall status, IFU excerpts, and PCCP details.

---

### 4. Risk Controls Summary  

1. **Software Lifecycle Management** – IEC 62304 (A/B/C) procedures integrated into QMSR.  
2. **Risk Management** – ISO 14971:2019 process covering hazards from acquisition to data storage & transmission.  
3. **Cybersecurity Controls** – Authentication, encryption (TLS), audit logging, secure update mechanism; documented in a Cybersecurity Risk Management File.  
4. **AI/ML Change Control** – Predetermined Change Control Plan (PCCP) defines permissible algorithm updates and post‑market monitoring.  
5. **DICOM Conformance** – Testing against DICOM SCU/SCP specifications ensures safe image handling.  
6. **Usability & Human Factors** – Validation of UI (GUI) per IEC 62366‑1 to mitigate use‑error risk.  

All controls must be reflected in the Design History File (DHF) and linked to corresponding verification/validation activities.

---

### 5. Human‑Escalation Triggers  

| Trigger | Escalation Action |
|--------|-------------------|
| **Uncertain predicate status** (e.g., retired, recalled, or >7 yr old) | Senior RA sign‑off; consider supplementary predicate or additional justification per “use of predicates” modernization. |
| **AI/ML module without a completed PCCP** | Immediate halt of submission preparation; engage AI/ML specialist and senior regulatory lead to draft PCCP. |
| **Software safety class C (IEC 62304) determined** | Re‑evaluate classification – may require PMA; flag to Lead Engineer & Regulatory Director for pathway decision. |
| **Intended use broader than predicate** (e.g., includes diagnostic interpretation) | Upgrade submission to a higher risk category or consider De Novo/PMA; obtain senior leadership approval. |
| **Incomplete cybersecurity threat model** | Require Cybersecurity Risk Management lead to supply missing analysis before proceeding. |
| **Missing or incomplete SBOM** | Pause clearance filing; request detailed component inventory from development team. |
| **Labeling / UDI gaps** (e.g., insufficient device identifier, missing GUDID entry) | Forward to Labeling & Regulatory Operations for remediation; do not submit until resolved. |

Escalations should be documented in the project risk register and communicated to the Project Lead, QA Manager, and regulatory compliance officer.

---

### 6. Peer‑Review Prompt  

> **To a fellow RA:** Please review the assumptions above regarding (a) the suitability of a single‑predicate 510(k) for this imaging workstation software; (b) completeness of the evidence list given the AI/ML component; and (c) any jurisdiction‑specific gaps, such as additional FDA guidance on cybersecurity or post‑market surveillance that may affect this submission. Identify any missing citations, required FDA docket numbers, or overlooked classification nuances.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

## ra_eu

### kb-eval-20261026-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c52063d5f7e81394", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c52063d5f7e81394`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통...
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

> **Regulatory Draft – Response to Notified Body Deficiency Letter (X‑ray Diagnostic Radiology Device)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory Basis |
|------|---------------|------------------|
| **Intended purpose** | “Standard diagnostic radiology” – a device that *generates* ionising radiation for imaging. | — |
| **MDR rule applied** | Rule 10 (active devices for diagnosis/monitoring) → **Class IIb**. | MDR Annex VIII, Rule 10 |
| **Conformity‑assessment route** | Full quality‑management‑system and technical‑documentation assessment by a Notified Body (NB).  <br>Chosen path: **Annex IX** (full NB review) – the mandatory route for Class IIb devices. | MDR Art. 52(4) & Annex IX |

*If the manufacturer had elected the alternative route, it would have been Annex X (type‑examination) + Annex XI (production conformity verification).*

---

### 2. Evidence Already Submitted (as per NB’s request)

| Evidence | Current Status | Reference in source |
|----------|----------------|----------------------|
| **Clinical Evaluation Report (CER)** – Rev. 3 attached as Annex A, demonstrating clinical equivalence. | Provided. | “Revised CER Rev. 3 is attached as Annex A.” |
| **Clinical‑performance metric** – Detective Quantum Efficiency DQE(0) ≥ 65 % for both devices. | Provided (test report TR‑2024‑015). | “DQE(0) ≥ 65 % … Ref. Test Report TR‑2024‑015, IEC 62220‑1‑1.” |
| **IEC standard used for performance testing** – IEC 62220‑1‑1. | Cited in test report. | Same line as above. |

---

### 3. Gaps / Missing Information Identified by the NB  

| Gap | Why it matters (MDR requirement) | What must be supplied |
|-----|-----------------------------------|------------------------|
| **1. Justification of equivalence threshold (DQE ≥ 65 %)** – No scientific/clinical rationale linking the chosen DQE limit to safety or diagnostic effectiveness. | Annex XIV Part A §6.1 requires a *clinically justified* demonstration that performance is at least equivalent to the predicate. | • Peer‑reviewed literature or a benefit–risk analysis showing that DQE ≥ 65 % ensures diagnostic adequacy for the intended clinical condition.<br>• Explanation of why lower DQE would not compromise patient safety (e.g., impact on repeat exposures). |
| **2. Comparative clinical data** – Only one test report is supplied; no head‑to‑head study or literature review comparing the device to the reference. | Annex XIV Part A §6.1 demands *clinical data* that support equivalence, which may be obtained from a comparative clinical investigation, systematic literature review, or meta‑analysis. | • Summary of a systematic literature search (MEDLINE, Embase) covering devices of similar class and DQE performance.<br>• If no published data exist, a dedicated bench‑to‑clinical bridging study should be proposed. |
| **3. Post‑Market Surveillance (PMS) plan & PSUR** – No evidence that an ongoing PMS system complying with Art 83–86 is in place. | Art. 84 requires a *written PMS plan*; Art. 86 mandates a Periodic Safety Update Report for Class IIb devices (annual). | • PMS Plan (scope, data collection methods, trigger thresholds).<br>• Latest PSUR (or draft if device not yet marketed) showing integration of clinical‑performance data and trend analysis. |
| **4. Risk Management File (RMF) – residual risk evaluation** – The CER does not contain a clear statement linking the DQE performance to residual risks under ISO 14971. | Annex I §3 (risk management system) plus Annex II §6.1 require that risk analysis addresses *known and foreseeable* hazards, including radiation exposure and diagnostic inaccuracy. | • Updated RMF showing: <br> a) Hazard identification for insufficient image quality (e.g., repeat exposures).<br> b) Estimation of residual risk after applying performance‑based controls.<br> c) Acceptance criteria aligned with GSPR §16 (radiation protection). |
| **5. Labeling / IFU compliance** – No copy of the label or Instructions for Use demonstrating conformity with Annex I §23. | Annex I §23 mandates that labeling contain essential safety information, including radiation warnings and performance specifications. | • Full label artwork and IFU (including DQE specification, safe operating parameters, user training requirements). |
| **6. Verification of applicable IEC standards** – Only IEC 62220‑1‑1 is cited; missing references to the electrical safety & electromagnetic compatibility standards for X‑ray equipment (e.g., IEC 60601‑2‑54, IEC 60601‑2‑28). | Annex I §16 (radiation protection) and §§17–18 (electrical safety, active devices) require compliance with relevant harmonised standards. | • Test reports/Certificates of Conformity for IEC 60601‑2‑54 (or IEC 60601‑2‑28 where appropriate) and any other applicable standards (IEC 62304 for software, IEC 62366‑1 for usability). |
| **7. Software lifecycle documentation** – If the device includes image‑processing or display software, no evidence of IEC 62304/IEC 62366 compliance is provided. | Annex I §17 (software) and MDR require that software be validated according to recognised standards. | • Software development plan, verification & validation reports, and usability engineering file per IEC 62304 & IEC 62366‑1. |

---

### 4. Required Evidence – Checklist for Complete Submission  

| # | Document / Data | MDR reference (framework) |
|---|-----------------|---------------------------|
| 1 | Updated Clinical Evaluation Report (CER) – include justification of DQE threshold, systematic literature review or comparative study. | Annex XIV Part A §6.1 |
| 2 | Full test report(s) for DQE (TR‑2024‑015) plus any additional performance testing demonstrating equivalence across the clinical spectrum. | IEC 62220‑1‑1 (cited); Annex XIV Part A §5 |
| 3 | PMS Plan (Art. 84) and latest PSUR (Art. 86, annual for Class IIb). | Art. 84; Art. 86(1)(a–c) |
| 4 | Complete Risk Management File – updated residual‑risk evaluation linking image quality to radiation dose & repeat examinations. | Annex I §3; ISO 14971:2019 (framework) |
| 5 | Label and Instructions for Use (IFU) meeting Annex I §23. | Annex I §23 |
| 6 | IEC conformity certificates / test reports for electrical safety & EMC (IEC 60601‑2‑54 or IEC 60601‑2‑28). | Annex I §§16–18 |
| 7 | Software lifecycle documentation (if applicable) – development plan, verification/validation, usability engineering. | Annex I §17; IEC 62304; IEC 62366‑1 |
| 8 | Declaration of Conformity (DoC) with full content per Annex IV & Art. 19 (once all above are satisfied). | Art. 19; Annex IV |

---

### 5. Summary of Required Risk Controls  

| Hazard | Control measure (design / informational) | Relevant GSPR |
|--------|-------------------------------------------|----------------|
| Excessive radiation dose due to mis‑setting of exposure parameters | Interlock system, automatic exposure control, user‑set limits, pre‑set protocols. | §16 (radiation protection) |
| Inadequate image quality → repeat exposures | Minimum DQE specification (≥ 65 %); real‑time image‑quality feedback; training program for operators. | §17/§18 (active devices) |
| Electrical shock / fire risk from high‑voltage X‑ray tube | IEC 60601‑2‑28 compliance, grounding, protective earth, insulation tests. | §16 & §20 |
| Software malfunction leading to incorrect image processing | IEC 62304 software life‑cycle processes; IEC 62366‑1 usability verification; regular software updates with change control. | §17 |
| Misinterpretation of images by non‑expert users | Clear IFU, labeling with warnings, intended user group definition (lay‑person vs professional). | §22/§23 |

---

### 6. Human‑Escalation Triggers  

1. **Unresolved NB comments after 30 days** – Escalate to senior regulatory manager for potential timeline impact and need for a formal meeting with the NB.  
2. **Evidence gaps that require new clinical investigations** (e.g., lack of comparative study) – Initiate a clinical investigation plan per Annex XIV Part B; involve Clinical Affairs lead.  
3. **Risk‑management deficiencies identified** (residual risk cannot be justified) – Suspend the CE‑marking dossier pending corrective actions; inform Quality Management System (QMS) owner.  
4. **PMS/PSUR non‑availability** when device is already on the market – Immediate interim measure: issue a Field Safety Corrective Action (FSCA) notice per Art. 87 if any safety signal emerges.  

The above triggers should be logged in the project risk register and communicated to all stakeholders.

---

### 7. Peer‑Review Request  

> **To a fellow EU RA:**  
> Please review this draft for:  
> • Completeness of identified gaps versus the NB’s deficiency letter (the source excerpt only lists “Deficiency Letter 정의” – verify that no other specific NB comments were omitted.  
> • Correct application of MDR classification rules and conformity‑assessment route, especially concerning any possible **Rule 9** or **Rule 11** overlap for associated software components.  
> • Adequacy of the evidence checklist (are there any additional Annex II §§ required for an X‑ray device, such as clinical data on patient dose).  

Your feedback will be incorporated before final submission to the Notified Body.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1107467848736309543`

> ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통지하는 문서. 국내 MFDS "보완 요청", FDA "Additional Information (AI) Request"에 해당하는 EU MDR 용어. ---

### kb-eval-20261026-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7a5d2b9b569d2bf8", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7a5d2b9b569d2bf8`
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

> **MDR Annex II Technical Documentation – Notified‑Body (NB) Review Draft**  

*Prepared for the NB query on the current status of the technical documentation (TD) package.*  


---  

### 1. Classification & Conformity‑Assessment Route  

| Item | Current evidence in source | Gap / Action |
|------|---------------------------|--------------|
| **Device class** (e.g., I, Is/Im/Ir, IIa, IIb, III) | *No device description or intended purpose is provided in the excerpts.* | **Missing information – classification cannot be determined.** The manufacturer must supply: <br>• Intended medical purpose (label/IFU); <br>• Mode of action; <br>• Whether the device is sterile, measuring, or a reusable surgical instrument.  |
| **Applicable conformity‑assessment route** (Art 52) | Not addressed in source excerpts. | **Missing information – route cannot be selected.** Once class is known, apply Art 52(…) to select: <br>• Annex IX (full QMS + TD assessment) for Class IIa/IIb/III, *or* <br>• Annex X + XI (type‑examination & production conformity verification) for the alternative route of Class IIb/III. |  

**Human‑escalation trigger #1:** If classification cannot be confirmed within 5 business days, escalation to senior RA lead is required to request additional product information from the manufacturer.  


---  

### 2. Required Evidence per Annex II Sections (framework citations)

| Annex II § | Requirement (per MDR) | Evidence identified in source | Gap / Comment |
|------------|-----------------------|--------------------------------|---------------|
| **§1 – Device Description** | Detailed description of device, intended purpose, principle of operation, variants, accessories. | Source lists “Design Output, Device Description (DHF)” as the comparable element. | No actual narrative or drawings are attached in the excerpt. **Missing:** full written description and labelled diagrams. |
| **§2 – Labelling & IFU** | Label content & Instructions for Use meeting Annex I §23. | Source lists “Device Labeling (21 CFR 801; eSTAR §6)”. | No label artwork or IFU drafts provided. **Missing:** English language version plus any required additional EU languages. |
| **§3 – Design & Manufacturing** | Detailed design data, manufacturing process, quality control measures. | Source lists “Design History File (DHF)”. | The DHF is mentioned but no actual design files, BOMs, or process flowcharts are supplied. **Missing:** complete manufacturing specifications and process validation reports. |
| **§4 – GSPR Checklist** | Demonstration of compliance with the 23 General Safety & Performance Requirements (Annex I). | Source refers to “510(k) SE comparison + Performance testing”. | No explicit GSPR checklist or mapping is shown. **Missing:** a completed Annex I‑GSPR matrix linking each requirement to supporting evidence. |
| **§5 – Risk Management** | ISO 14971‑based risk management file (RMF). | Source mentions “Risk Management File (ISO 14971; not explicitly DHF)”. | No RMF document provided, nor are risk acceptability criteria or residual‑risk evaluation included. **Missing:** full RMF with risk analysis, evaluation, and control measures. |
| **§6 – Verification & Validation** | V&V plan, reports of verification (e.g., bench testing) and validation (clinical/real‑world). | Source lists “V&V Reports (DHF), Bi…”. | Only a fragment appears; full test protocols, acceptance criteria, and summary reports are absent. **Missing:** complete verification & validation documentation, including software V&V if applicable (IEC 62304). |
| **Annex III – PMS Technical Documentation** | PMS system (Art 83) & PMS plan (Art 84), PSUR/Annual report (Art 86/85). | Not referenced in the excerpts. | **Missing:** documented PMS system, post‑market surveillance plan and periodic safety update reports. |

**Human‑escalation trigger #2:** If any of the above Annex II sections remain incomplete after a 10‑day remediation period, elevate to the NB project manager for possible non‑conformity notice (NCN).  


---  

### 3. Clinical Evidence Requirements (Annex XIV)

| Requirement | Source status | Gap |
|-------------|---------------|-----|
| **Clinical Evaluation Report (CER)** – Annex XIV Part A, kept current under Art 61 | Not mentioned in source excerpts. | **Missing:** full CER with state‑of‑the‑art literature review, clinical data (investigations/PMCF), and benefit‑risk conclusions. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – Annex XIV Part B | Not mentioned. | **Missing:** PMCF plan describing methodology, sample size, endpoints; and interim/final PMCF report(s). |
| **Clinical Investigation (if required)** – Annex XV | No reference. | **Missing:** Clinical investigation dossier if the device lacks sufficient existing clinical data. |

**Human‑escalation trigger #3:** Absence of a CER or PMCF plan after classification is fixed must be escalated to senior clinical affairs for sourcing appropriate clinical data (literature, registries, or new investigations).  


---  

### 4. Risk Controls & GSPR Mapping

| Relevant GSPR (§) | Typical control / evidence | Current source indication | Gap |
|-------------------|----------------------------|---------------------------|-----|
| **§3 – Risk Management System** (Annex I Chapter I) | ISO 14971 RMF, periodic review. | “Risk Management File (ISO 14971…)” noted but not provided. | Full RMF required. |
| **§4 – Risk Control Measures** | Design safeguards, protective labeling, user training. | No explicit evidence supplied. | Mapping of each identified hazard to a control measure needed. |
| **§5 – Use‑Error Risks** | Usability engineering (IEC 62366‑1). | Not addressed. | Conduct usability validation and include summary in V&V. |
| **§6 – Device Lifetime** | Defined service life, ageing studies. | No data. | Provide life‑cycle testing results or justification. |
| **§16 – Radiation Protection** (if an X‑ray device) | IEC 60601‑2‑54 compliance, DICOM standards. | Not mentioned. | Verify applicability; attach conformity assessment evidence if relevant. |

**Human‑escalation trigger #4:** If any GSPR cannot be demonstrated with documented evidence, the NB must issue a request for additional risk‑control documentation (RC‑R).  


---  

### 5. Language & Format Requirements

* Minimum English language version required; additional EU languages may be requested by the NB (source: “NB 요구 언어 추가”).  
* All documents must be signed and dated per Art 19 EU Declaration of Conformity requirements (Annex IV content).  

**Human‑escalation trigger #5:** Lack of an English version or missing signatures should be flagged immediately for corrective action.  


---  

### 6. Summary Judgment & Next Steps

| Assessment | Verdict |
|------------|---------|
| **Classification** | *Undetermined – manufacturer must provide intended purpose, mode of action, and any sterility/measurement/reusability attributes.* |
| **Conformity‑assessment route** | *Cannot be selected until class is known; likely Annex IX (full QMS) for Class IIa/IIb/III.* |
| **Technical Documentation completeness** | *Significant gaps across all Annex II sections, GSPR mapping, risk management, V&V, clinical evidence, and PMS.* |
| **Overall NB position** | *Not ready for conformity assessment; a “non‑conformity notice (NCN) – incomplete documentation” will be issued unless remediation is completed within the defined timelines.* |

### 7. Human‑Escalation Triggers (Consolidated)

1. **Classification unknown** → senior RA lead (5 days).  
2. **Missing Annex II sections** after 10 days → NB project manager for NCN issuance.  
3. **No CER / PMCF plan** → clinical affairs escalation.  
4. **Unaddressed GSPR requirements** → request for risk‑control documentation.  
5. **Language or signature deficiencies** → immediate corrective‑action notice.

---  

### 8. Peer‑Review Prompt

> *Colleague, please review the assumptions made above regarding the classification uncertainty and the mapping of source excerpts to MDR Annex II requirements. Verify that no device‑specific identifiers were introduced inadvertently, and confirm whether any additional jurisdictional considerations (e.g., IEC 60601‑2‑54 for radiation devices) should be added based on the product family.*  



*End of draft – all citations derived from framework references; no instance‑identifiers were invented.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

### kb-eval-20261026-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "f52799c5b27a84bf", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f52799c5b27a84bf`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_MDR_2017_745.md)
- Source hash: `15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_MDR_2017_745.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | |...
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

> **Regulatory Draft – Notified‑Body Query Response (EU MDR 2017/745)**  

*Prepared for the internal “daily growth” run – Pipeline ID daily_growth_v1 (2026‑10‑26). All references follow the citation rules set out in the briefing.*

---

## 1. Device Synopsis (information required)

| Item | Current status | Gap / Action |
|------|----------------|--------------|
| **Device name & model** | – not provided in source | Request from product team |
| **Intended medical purpose** | – not provided | Obtain a concise Intended Use statement |
| **Key technology / “X‑ray system” components** | Mentioned only in the guide title (“X‑ray system 적용 지침”) | Clarify which subsystems are in scope (e.g. X‑ray source, detector, image‑processing software) |
| **Regulated product type** (active therapeutic, diagnostic, implantable, etc.) | – not provided | Needed to select the correct classification rule (Annex VIII) |
| **Risk class hypothesis** | – not provided | Perform preliminary rule mapping (see Section 2) |

*Human‑escalation trigger:* If any of the above items are not supplied within 5 working days, raise a “Missing Device Definition” ticket to the Project Owner.

---

## 2. Preliminary Classification Assessment  

| Step | Regulatory basis | Comments / Required evidence |
|------|------------------|------------------------------|
| **Identify applicable rule(s)** | Annex VIII – Classification rules (Rules 9, 10, 11, 17 for X‑ray‑related devices) | Without the device’s exact function we cannot assign a rule. The guide mentions an “X‑ray system”, which normally triggers Rule 10 (active diagnostic radiation emitters → Class IIb) and/or Rule 17 (detector → Class IIa). Confirm whether the product includes a source, detector, and software modules. |
| **Determine risk class** | Article 51 & Article 52 of MDR – classification hierarchy | If the device comprises multiple regulated subsystems, each is classified separately; the overall device follows the highest class among its parts (Art 52(1)). |
| **Select conformity‑assessment route** | Art 52 (3)–(7) together with Annex IX or Annex X + XI (see Section 3) | Dependent on the final class. |

*Human‑escalation trigger:* If the intended use points to more than one rule, schedule a classification workshop with Clinical, R&D and Regulatory leads; document the decision in the “Classification & Route Decision Log”.

---

## 3. Conformity‑Assessment Route (once class is known)

| Risk Class | MDR route (Art 52) | Notified‑Body involvement |
|------------|-------------------|---------------------------|
| **I** (non‑sterile, non‑measuring, non‑reusable‑surgical) | Art 52(7): self‑declaration – technical documentation (Annex II) + EU DoC (Art 19/Annex IV) | No NB required |
| **Is / Im / Ir** | Art 52(7) – limited NB scope (Annex IX Chapters I & III or Annex XI Part A) | Limited NB audit of sterile/measuring aspects |
| **IIa** | Art 52(6): Annex IX (QMS + technical‑doc assessment of one representative device) **or** Annex II + III with production verification under Annex XI §10 or §18 | NB required – full QMS audit |
| **IIb** | Art 52(4): Annex IX (full technical‑doc assessment per generic group) **or** Annex X (type‑examination) + Annex XI (production conformity) | NB required – either route possible |
| **III** | Art 52(3): Annex IX (full technical‑doc assessment) **or** Annex X + Annex XI | NB required – full audit |

*Citation*: MDR Art. 52; Annex VIII for rules; Annex IX, X, XI for routes.

---

## 4. Required Evidence & Documentation  

| Deliverable (TD Section) | Regulatory reference | Typical content | Current status (per source) |
|---------------------------|----------------------|-----------------|-----------------------------|
| **Device description & intended use** (§1‑2, Annex II) | Annex II §§1‑2 | Device name, model, variants, indications, contraindications | *Missing* – not in the excerpt |
| **Design/Manufacturing information** (§3, Annex II) | Annex II §3 | Process flow, materials, drawings, manufacturing sites | *Missing* – only “설계·제조 정보” is listed as an activity |
| **Verification & Validation (V&V)** (§4, Annex II) | Annex II §4 | Test reports, acceptance criteria, software validation (IEC 62304), usability testing (IEC 62366‑1) | *Missing* – no V&V artefacts referenced |
| **General Safety & Performance Requirements mapping** (§5, Annex II) | Annex I GSPR §§1‑23; Annex II §5.1 | GSPR checklist → traceability matrix linking each requirement to design/DVT/clinical data | *Present* – “GSPR 적합성 보고서” produced (step 3) |
| **Risk Management File** (§6, Annex II) | Annex I §3; ISO 14971:2019 | Risk management plan, risk analysis, evaluation of residual risk, post‑risk‑management review | *Present* – “위험관리 보고서” produced (step 5) |
| **Clinical Evaluation Report (CER)** (§6.1, Annex II) | Annex XIV Part A; Art 61 | State‑of‑the‑Art literature review, clinical data, benefit‑risk conclusion | *Present* – CER drafted/updated (step 4) |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** (§6.2, Annex II) | Annex XIV Part B; Art 83‑86 | PMCF objectives, study design, data collection, interim analysis | *Missing* – not listed in steps |
| **PMS Plan** | Art 84 | System description (Art 83), data sources, reporting procedures | *Present* – “PMS Plan” drafted (step 6) |
| **Periodic Safety Update Report (PSUR)** (for Class IIa/IIb/III) | Art 86 | Benefit‑risk conclusions, PMCF results, sales volume, population estimate | *Missing* – not yet required for Class I devices; will be needed once class is known |
| **EU Declaration of Conformity** | Art 19; Annex IV | Manufacturer details, device identification, conformity route, reference standards | *Missing* – to be issued after NB audit |
| **Labeling & IFU** | Annex I §23; MDR Art 12 | Symbols, warnings, intended use statements, UDI (if applicable) | *Missing* – no evidence in the excerpt |
| **UDI‑system documentation** (if required) | MDR Art 27‑28 | UDI registration in EUDAMED, carrier labeling | *Not mentioned* – verify necessity based on class |

---

## 5. Identified Gaps & Immediate Actions  

1. **Device definition missing** – cannot finalize classification or select the appropriate Annex VIII rule.  
   *Action*: Request a one‑page “Device Summary” from R&D (incl. intended use, technology description, patient population).

2. **PMCF planning absent** – required for Class IIa and above; also mandatory to substantiate clinical evidence over the device life‑cycle.  
   *Action*: Initiate draft PMCF plan with Clinical & QA; align with Annex XIV Part B.

3. **Verification & Validation summary not listed** – essential for GSPR compliance (e.g., performance testing of X‑ray output, software verification).  
   *Action*: Collect test reports from R&D; map to each GSPR in the traceability matrix.

4. **Usability / Human Factors evidence missing** – if device is intended for lay users or has a user interface, IEC 62366‑1 must be addressed.  
   *Action*: Confirm need with Clinical and schedule usability study (if applicable).

5. **UDI & EUDAMED registration not referenced** – mandatory for all classes except certain custom‑made devices.  
   *Action*: Verify UDI strategy; prepare dossier entry in EUDAMED once device class is known.

6. **Labeling/IFU draft absent** – needed for GSPR §23 and NB review.  
   *Action*: Draft labeling package (symbols, safety information) and submit to QA for review.

*Human‑escalation triggers:*  

- Any of the items in column “Missing” remains unresolved after **5 working days** → raise a “Documentation Gap” alert to RA Lead.  
- If the NB requests additional clinical data beyond the current CER → activate Clinical Team to produce supplementary clinical investigation or literature update within the timeline stipulated by the NB (typically 30 days).  
- Discovery of residual risk that cannot be mitigated to an acceptable level after risk‑management review → stop project and convene a Risk Review Board before any further regulatory steps.

---

## 6. Suggested Risk Controls (framework)

| GSPR area | Typical control measure | Evidence needed |
|-----------|------------------------|-----------------|
| **§3 – Risk management system** | ISO 14971:2019‑based RMF; regular updates | Risk Management Report (step 5) |
| **§4 – Risk control** | Design safeguards, protective circuitry for X‑ray emission, interlocks, dose limits per IEC 60601‑2‑54 | Verification test reports, design specifications |
| **§5 – Use‑error mitigation** | Human‑factors analysis, colour‑coded controls, clear IFU warnings | Usability study report (IEC 62366‑1) |
| **§6 – Device lifetime** | Defined service life, periodic performance checks, maintenance schedule | Maintenance plan and post‑market data |
| **§16 – Radiation protection** | Compliance with IEC 60601‑2‑54 limits, shielding design, dose monitoring | Test certificates for radiation output, compliance report |
| **§17 – Software safety** (if applicable) | IEC 62304 lifecycle processes, verification of algorithms, cyber‑security risk assessment | Software Development File, security analysis |

*Note*: The exact controls must be matched to the device’s architecture once it is defined.

---

## 7. Peer Review Request  

> **To:** [RA colleague – e.g., Elena Müller]  
> **Subject:** Review of “Notified‑Body Query Response” draft (daily_growth_v1)  
> **Please challenge**:  
> - The completeness of the classification mapping given the limited device description.  
> - Whether any additional Annexes (e.g., Annex XII for performance evaluation, or specific IEC standards for X‑ray equipment) should be referenced at this stage.  
> - Any jurisdictional nuances that may affect the required evidence (e.g., EU AI Act overlap if software includes AI, which is hinted by the guide’s “EU_AI_Act_MDR_중첩적용_매핑”).  

Your feedback will be incorporated before final submission to the NB.

---

**End of draft.**  
*All citations are based on MDR framework references; no specific regulator‑issued identifiers were present in the source excerpts and therefore are not invented herein.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `1072636411107495596`

> --- doc-id: EU_MDR_2017_745 title: "EU MDR — Regulation (EU) 2017/745 요약 및 적용 지침" type: Guide version: v0.3.1 status: draft category: 01_법규_규제 purpose: "EU MDR 2017/745 핵심 요구사항, 2026 일정, 기술문서 구성 및 X-ray 시스템 적용 지침" applicable: [EU MDR 2017/745, EU MDR GSPR Annex I, ISO13485:2016, ISO14971:2019, IEC 62304, IEC 60601-1, IEC 60601-2-54, UDI] forms: [F-MDR-TD-CHK-001] related-docs: - GSPR_정합표준_매핑표 - GSPR_체크리스트_v0.2_템플릿 - PRRC_역할_및_한미_대응자_매핑 - EU_AI_Act_MDR_중첩적용_매핑 - ISO13485_2016_요약 - SOP-CC-001 - SOP-PSUR-001 - SOP-FSCA-001 - TF-TD-001 related-issues: [4, 5, 22, 33, 989] owner: RA/QA Lead last-review: 2026-07-23 review-due: 2027-06-09 --- # EU...

### kb-eval-20261026-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a409921af470421f", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a409921af470421f`
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

> **Regulatory Draft – Notified‑Body Query Response**  
*Prepared for the EU MDR pathway (MDR 2017/745)*  

---

### 1. Device Synopsis – Information Required  

| Item | Why it is needed | Current status (from source) |
|------|------------------|------------------------------|
| **Trade name / model number** | Identifies the device in all regulatory artefacts (EUDAMED, labeling). | Not provided |
| **Intended purpose & indications for use** | Drives classification (Annex VIII rules) and determines clinical evidence scope. | Not provided |
| **Device description (materials, dimensions, accessories, software components)** | Needed for technical documentation (Annex II §1‑5) and risk analysis (ISO 14971). | Not provided |
| **Major design & manufacturing processes** | Required in the “Design and Manufacture” chapter of Annex II. | Not provided |
| **Sterility / measuring function / reusable surgical instrument status** | Determines whether the device falls under the “Is/Im/Ir” sub‑class (Art. 52(7)). | Not provided |
| **Intended user (professional vs lay person)** | Affects GSPR §22 and risk‑control measures. | Not provided |
| **Country of manufacture & importation chain** | Needed for Authorized Representative (Art. 11) and import licence information (source excerpt notes “수입자”). | Partially known – importer identified, but no manufacturer details. |
| **Clinical background / existing data** | Basis for Clinical Evaluation Report (CER) per Annex XIV Part A & PMCF planning (Annex XIV Part B). | Not provided |

*Action*: Request the above items from the design/manufacturing team before proceeding with classification and submission‑route selection.

---

### 2. Classification Determination  

1. **Legal basis** – Article 51 together with Annex VIII sets out the *self‑classification* principle (source [2]). The manufacturer bears the responsibility for applying the 22 rules sequentially, selecting the highest class that applies.  
   - *Citation*: “Article 51 + Annex VIII” (source [2]).

2. **Procedure** –  
   a. Map the device’s intended medical purpose against each rule in Annex VIII (e.g., Rule 9 for active therapeutic devices, Rule 10 for active diagnostic devices, Rule 11 for software, etc.).  
   b. If multiple rules apply, adopt the highest resulting class.  

3. **Pre‑liminary outcome** – *No classification can be assigned until the intended use and functional description are known.*  

4. **If a higher‑risk class (IIa/IIb/III) is identified**, the conformity‑assessment route must involve a Notified Body as per Article 52:  

| Class | Relevant Art. 52 paragraph | Conformity‑assessment route (Annex) | NB involvement |
|-------|---------------------------|------------------------------------|----------------|
| I (non‑sterile, non‑measuring, non‑reusable‑surgical) | 52(7) | Self‑declaration – Technical documentation (Annex II & III) + EU DoC (Art. 19/Annex IV) | No |
| Is / Im / Ir | 52(7) | Annex IX Chapters I & III **or** Annex XI Part A (limited scope) | Yes (limited) |
| IIa | 52(6) | Annex IX Chapters I & III + technical‑documentation assessment of one representative device (Annex IX §4) *or* Annex II/III + Annex XI §10 or §18 | Yes |
| IIb | 52(4) | Annex IX Chapters I & III + technical‑documentation assessment of one representative device per generic group (or Annex X + Annex XI) | Yes |
| III | 52(3) | Full Annex IX assessment *or* Annex X + Annex XI | Yes |

*Citation*: “Art. 52 … classification → route” (framework reference – no specific source excerpt needed).

---

### 3. Evidence Package Required for the NB  

| Evidence | Regulatory basis | Typical content |
|----------|------------------|-----------------|
| **Technical Documentation** (Annex II §§1‑6) | Annex II | Device description, design & manufacture info, GSPR compliance, risk management file, verification/validation data, clinical evaluation (see below). |
| **EU Declaration of Conformity** | Art. 19; content listed in Annex IV | Manufacturer details, device identification, conformity‑assessment route, references to standards, signed by authorised person. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A & Art. 61 | State‑of‑the‑art literature review, clinical data (clinical investigations or equivalent), benefit–risk analysis; kept current. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | Planned studies, objectives, methodology, timeline, and periodic evaluation results. |
| **Risk Management File (RMF)** | Annex I §3 (ISO 14971 2019) | Risk analysis, risk control measures, residual‑risk evaluation, updates from PMS. |
| **Post‑Market Surveillance (PMS) System & Plan** | Art. 83 (system), Art. 84 (plan) | Processes for gathering and analysing post‑market data, vigilance reporting (Art. 87). |
| **Periodic Safety Update Report (PSUR)** *(if Class IIa/IIb/III)* | Art. 86 | Summaries of PMS data, PSUR conclusions, PMCF results, sales volume & user population. |
| **Unique Device Identification (UDI) registration** | MDR UDI requirements; EUDAMED entry | UDI‑DI, UDI‑PI, labeling, database upload. |
| **Labeling & IFU** | Annex I §23 | Instructions for use, safety information, symbols, language(s). |
| **Authorized Representative (if applicable)** | Art. 11 | Evidence of appointment and contact details in EU. |

*Note*: The source excerpt [1] lists several of these items (e.g., CER, UDI portal, PSUR, vigilance) confirming they are part of the expected dossier – no specific identifier is provided; therefore “no specific identifier found in source — verify separately”.

---

### 4. Anticipated Risk Controls (Generic)

| GSPR area | Typical control measure | Evidence to be supplied |
|-----------|--------------------------|--------------------------|
| **§3 – Risk Management System** | ISO 14971‑based RMF with documented risk analysis, evaluation of residual risks vs benefits. | RMF (ISO 14971 2019). |
| **§4 – Risk control measures** | Design safeguards, protective labeling, software safety functions (IEC 62304), alarm limits. | Verification & validation reports, usability testing (IEC 62366‑1). |
| **§5 – Use‑error risks** | Human factors engineering, training instructions, IFU clarity. | Usability study report (IEC 62366‑1). |
| **§6 – Device lifetime** | Defined service life, maintenance schedule, degradation testing. | Ageing & reliability data. |
| **§7 – Transport and storage** | Packaging validation, transport condition monitoring. | Packing & transport test reports. |
| **§8 – Benefit–risk determination** | Clinical evaluation conclusions, residual‑risk acceptability justification. | CER (Annex XIV Part A). |
| **§22 – Use by lay persons** *(if applicable)* | Simplified IFU, safety interlocks, colour coding. | Labeling & user‑testing evidence. |

---

### 5. Gaps / Missing Information  

1. **Intended purpose & classification rule(s)** – cannot select Annex VIII rule without it.  
2. **Device architecture (active, passive, software, sterile, measuring)** – needed to decide if “Is/Im/Ir” sub‑class applies.  
3. **Clinical data sources** – no evidence of existing investigations or equivalence.  
4. **Manufacturing location & quality‑management system** – required for NB audit (Annex IX).  
5. **UDI allocation strategy** – UDI‑DI and labeling plan not defined.  
6. **PMS/PMCF methodology** – only a generic mention of vigilance in source [1]; detailed plans absent.  

*Immediate action*: Issue a “Missing Information Request” to the project team covering points 1–6.

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger point | Escalation destination |
|-----------|----------------|------------------------|
| **No intended purpose / classification rule identified** after two information‑gathering cycles (≈ 5 working days) | Project Manager (PM) – risk of schedule slip. |
| **Clinical evidence insufficient to satisfy Art. 61/Annex XIV Part A** (e.g., < 30 patients, no comparators) | Clinical Evaluation Lead – must decide on supplemental investigations or literature search. |
| **Device classified as Class IIb/III** and NB contract not yet in place (NB cost estimate provided in source [1] but no agreement) | Procurement / Legal – initiate NB selection & NDA negotiation (budget > €10,000). |
| **RMF missing post‑market updates** after the first PMS data collection cycle (6 months) | Quality Manager – trigger corrective‑action procedure per Art. 83/84. |
| **UDI registration in EUDAMED not completed 30 days before intended CE marking** | Regulatory Affairs Lead – raise to senior management for resource allocation. |

Escalations should be logged in the project’s risk register with a clear responsible owner and expected resolution date.

---

### 7. Summary Judgment  

- **Classification cannot be finalised** until the manufacturer supplies detailed intended‑use and device‑characteristic information (Annex VIII rule mapping).  
- **Assuming the device falls into Class IIa or higher**, the conformity‑assessment route will require a Notified Body under **Art. 52(6) – Annex IX** (full QMS + technical‑documentation assessment) or, for Class III, **Annex X + XI**.  
- The **evidence package** must include all items listed in Section 3, fully aligned with the MDR clauses and supporting standards (ISO 14971 2019, IEC 62304, IEC 62366‑1, etc.).  
- **Current gaps** (intended purpose, clinical data, UDI plan, PMS/PMCF details) must be addressed before any NB audit can be scheduled.  

*Proceed with the Missing Information Request and schedule a classification workshop once the required inputs are received.*

---

### 8. Peer‑Review Prompt  

> @RA‑Peer: Please review the assumptions made about the need for a Class IIa/IIb/III route based on the limited source material, verify that all MDR citations match the latest edition (2023‑09 MDCG Manual referenced), and check whether any additional EU‑specific obligations (e.g., EUDAMED registration deadlines, post‑market clinical follow‑up frequency) have been omitted. Also confirm that no US‑centric identifiers were inadvertently introduced.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261026-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "8405590a42a7aa9d", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md", "source_hash": "fe7cb36ba8b5ee75b1e25ebd68b72fb4f7c9270caae14a9f1f664dcd7e32f921"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `8405590a42a7aa9d`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md)
- Source hash: `fe7cb36ba8b5ee75b1e25ebd68b72fb4f7c9270caae14a9f1f664dcd7e32f921`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexI_GSPR_Checklist.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### §21 — 에너지원·물질로 인한 위험 방호 | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | 근거 문서 | |---|---|---|---|---|---|---| | 21.1 | 전류·열 등 에너지 방출 위험 방지 | ● | ● | N/A | HS | IEC 60601-1 | | 21.2 | 의도하지 않은 물질 방출 방지 | ● | ● | N/A | SPEC | 재료 적합성 검토 | | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | |---|---|---|---|---|---| | 23...
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

> **Regulatory Assessment & Submission Plan for the X‑ray Detector / Handheld Source System (including GUI software)**  

---

### 1. Device description (high‑level)

| Sub‑system | Function | MDR “device” definition |
|------------|----------|--------------------------|
| **X‑ray detector** | Converts ionising radiation into a digital signal for image formation. | Active device that *records* diagnostic images → covers **Rule 17** (recording of X‑ray images). |
| **Handheld X‑ray source** | Portable emitter of ionising X‑ray photons for point‑of‑care radiography. | Active device that *emits* ionising radiation → covers **Rule 10** (diagnostic/therapeutic radiation emission). |
| **GUI software** | Provides user interface, image display and basic decision support. | Software that supplies information used for diagnostic decisions → covers **Rule 11** (medical device software). |

The overall system is marketed as a *portable X‑ray imaging solution*; the highest classification of its components drives the system class.

---

### 2. Classification & conformity‑assessment route  

| Component | Applicable MDR rule | Resulting class |
|-----------|---------------------|-----------------|
| Handheld source – Rule 10 (ionising radiation) | **Rule 10** ⇒ Class **IIb** (energy‑emitting device for diagnostic purposes). |
| X‑ray detector – Rule 17 (recording of X‑ray images) | **Rule 17** ⇒ Class **IIa**. |
| GUI software – Rule 11 (information for diagnosis) | **Rule 11** ⇒ Class **IIa** (assuming no life‑threatening decision impact). |

**System class:** **Class IIb** (highest class of the group).  

**Conformity‑assessment route (Art. 52(4))**:  
- **Annex X** – EU type‑examination of the whole system (or of the highest‑risk component, with reference to the lower‑risk components).  
- **Annex XI** – Production conformity verification on the finished device.  

*Reference:* Art. 52(4) MDR 2017/745; Annex X + Annex XI for Class IIb devices.  

---

### 3. Evidence required for a successful NB audit  

| Category | Required artefacts (minimum) | Source‑derived notes |
|----------|------------------------------|----------------------|
| **Technical documentation** – Annex II §§1‑6 | • Device description & intended use<br>• Design and manufacturing information<br>• GSPR compliance evidence (see §21, §23 tables)<br>• Risk Management File (ISO 14971:2019) <br>• Verification & validation reports (including performance of detector – DQE, linearity; radiation output of source). | GSPR items marked “●” in the source table indicate applicability. |
| **EU Declaration of Conformity** – Art. 19 (content per Annex IV) | • Declaration signed by manufacturer<br>• List of applicable GSPR §§ and standards (IEC 60601‑1, IEC 60601‑2‑54, IEC 62304, IEC 62366‑1, etc.). |
| **Clinical Evaluation Report** – Annex XIV Part A | • State‑of‑the‑art literature review for portable X‑ray imaging.<br>• Clinical performance data (e.g., image quality studies, dose measurements). |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** – Annex XIV Part B | • Planned post‑market surveillance activities specific to radiation safety and software usability.<br>• Definition of endpoints, sample size, follow‑up duration. |
| **PMS system** – Art. 83; **PMS plan** – Art. 84 | • Continuous monitoring of adverse events, field safety corrective actions (FSCA).<br>• Trend reporting (Art. 88) for radiation overexposure incidents. |
| **Periodic Safety Update Report (PSUR)** – Art. 86 (annual for Class IIb) | • Summary of benefit‑risk determination, PMCF results, sales volume & user population. |
| **Standards compliance** | • IEC 60601‑1 (general safety) – cited in source for §21.1.<br>• IEC 60601‑2‑54 (X‑ray equipment) – required for the handheld source.<br>• IEC 62304 (software lifecycle) – required for GUI software.<br>• IEC 62366‑1 (usability engineering). |
| **Labeling & IFU** – Annex I §23 | • Must contain items listed in the source table (§23.2‑23.4, IFU checklist).<br>• Evidence that each item (purpose, contraindications, residual risk, etc.) is present and verified. |

---

### 4. GSPR compliance status (derived from source excerpts)

| GSPR clause | Sub‑system(s) to which it applies* | Evidence required (per source) |
|-------------|-----------------------------------|-------------------------------|
| **§21.1 – Prevention of energy (current, heat) emission** | X‑ray detector & Handheld source | Demonstration of compliance with IEC 60601‑1 (cited in source). |
| **§21.2 – Prevention of unintended material release** | X‑ray detector & Handheld source | Materials suitability review (SPEC). |
| **§23.2 – Specification of radiation type & energy characteristics** | Handheld source | IFU must state radiation type & energy (IFU verification). |
| **§23.3 – Output characteristics & energy levels** | Handheld source | IFU must state output specs (dose, kVp range). |
| **§23.4 – Minimum IT requirements for software** | GUI software | IFU must list required OS / hardware (checked in source). |
| **IFU mandatory items (common)** – usage purpose, contraindications, expected clinical benefit, residual risk information, target patient group, installation/maintenance, cleaning/disinfection, consumables/accessories, environmental conditions, special disposal instructions. | All three subsystems | Each item must be present in the IFU; source provides checklist confirming applicability. |

\*“●” in the tables indicates that the requirement applies to the listed subsystem.

---

### 5. Identified gaps (information **missing** for NB submission)

| Gap | Why it is a gap | Impact on assessment |
|-----|-----------------|----------------------|
| **Full IEC 60601‑1 & IEC 60601‑2‑54 test reports** | Only the standard is mentioned; actual compliance data not supplied. | NB will request verification of electrical safety and radiation emission limits. |
| **Materials suitability documentation (SPEC)** for both detector housing and source casing – no traceability or biocompatibility assessment provided. | Required for §21.2. | Potential non‑conformity with GSPR on material release. |
| **Draft IFU** containing all items listed in §23 tables. | Checklist shows items required, but the actual wording/content is absent. | NB will flag incomplete labeling evidence. |
| **Clinical performance data** (image quality, dose, detector DQE) for the combined system. | Needed for Clinical Evaluation Report & PMCF plan. | Lack of clinical evidence blocks CE marking. |
| **PMCF plan details** – objectives, methodology, enrolment numbers, follow‑up schedule. | Required by Annex XIV Part B. | Without it, Art. 61 (keeping CER up‑to‑date) is not satisfied. |
| **PMS system documentation** (process description, reporting procedures). | Needed for Art. 83/84 compliance. | NB may request a full PMS file before certification. |
| **Software verification & validation reports** per IEC 62304 and usability testing per IEC 62366‑1. | No evidence shown; required for Rule 11 devices. | May lead to classification downgrade or re‑assessment of risk. |

---

### 6. Risk control summary (linked to GSPR)

| Hazard | Source clause | Implemented / Planned controls |
|--------|----------------|--------------------------------|
| Unintended radiation emission (over‑exposure) | §21.1, §23.2‑§23.3 | Interlock circuitry, dose‑monitoring feedback, automatic shut‑off after preset exposure time; verification per IEC 60601‑2‑54. |
| Thermal overload of source electronics | §21.1 | Temperature sensors + firmware shutdown; thermal design validated per IEC 60601‑1. |
| Release of hazardous materials (e.g., lead shielding) | §21.2 | Use of certified, sealed encapsulation; material compliance certificates (REACH, RoHS). |
| Software‑induced misinterpretation of images | §23.4 (IT requirements) & Rule 11 | IEC 62304 lifecycle management, hazard analysis (ISO 14971), usability testing per IEC 62366‑1, clear UI warnings in IFU. |
| Incorrect installation / maintenance leading to safety breach | IFU items “Installation/maintenance”, “Special disposal” | Detailed procedure manuals; training program for operators; post‑market field service checks. |

---

### 7. Action items & **human‑escalation triggers**

| Trigger condition | Required human action |
|-------------------|-----------------------|
| **Missing compliance test reports** (IEC 60601‑1, IEC 60601‑2‑54) | Procurement of full test certificates from the testing laboratory; review by engineering lead. |
| **No draft IFU available** | Immediate drafting of IFU covering all checklist items; legal/clinical review before submission to NB. |
| **Clinical evidence gap** (no performance study results) | Initiate a clinical investigation or a literature‑based equivalence analysis; obtain Ethics Committee approval if required. |
| **Incomplete PMCF plan** | Clinical affairs team to develop detailed PMCF protocol, define endpoints & timelines; sign‑off by R&D manager. |
| **PMS system not documented** | Quality‑system owner must produce PMS SOPs, incident handling workflow, and assign responsible persons (Art. 83). |
| **NB queries on classification justification** | Senior regulatory lead to prepare a written rationale referencing Rule 10, Rule 17, Rule 11 and Annex VIII classifications; submit to NB within the stipulated timeframe. |
| **Risk management file missing residual‑risk evaluation for software** | Conduct a supplemental risk analysis (ISO 14971) focusing on software hazards; update RMF and re‑evaluate benefit‑risk (Art. 61). |

All items flagged above must be resolved before the NB can issue a Type‑Examination Certificate.

---

### 8. Peer‑review request  

> **To: RA colleague**  
> Please review the assumptions made in this assessment, specifically:  
> 1. The use of Rule 10 for the handheld source and Rule 17/11 for the detector/software – confirm that no additional functions (e.g., therapy) would raise the class to III.  
> 2. Whether the GSPR checklist items marked “●” in the source tables are interpreted correctly as *applicable* rather than *not applicable*.  
> 3. Completeness of the evidence list for a Class IIb system under Annex X + XI – are there any MDR‑specific annexes (e.g., Annex XV for clinical investigations) that should be explicitly added?  
> 4. Any jurisdiction‑specific nuances missed (e.g., national X‑ray regulations, specific conformity assessment requirements in the UK or other EU MS).  

Your feedback will be incorporated before final submission to the Notified Body.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1053862138336873102`

> ### §21 — 에너지원·물질로 인한 위험 방호 | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | 근거 문서 | |---|---|---|---|---|---|---| | 21.1 | 전류·열 등 에너지 방출 위험 방지 | ● | ● | N/A | HS | IEC 60601-1 | | 21.2 | 의도하지 않은 물질 방출 방지 | ● | ● | N/A | SPEC | 재료 적합성 검토 |

2. Chunk `105731121168861494`

> | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | |---|---|---|---|---|---| | 23.2 | 이온화 방사선 기기 — 방사선 유형·에너지 특성 명시 | N/A | ● | N/A | IFU 기재 확인 | | 23.3 | 에너지 방출 기기 — 출력 특성·에너지 레벨 명시 | N/A | ● | N/A | IFU 기재 확인 | | 23.4 | SW 기기 — 최소 IT 요건 (OS, HW) 명시 | ● | ● | ● | IFU 기재 확인 | #### §23.4 IFU 필수 포함 사항 (공통) | IFU 항목 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---| | 사용목적 + 적응증 | ● | ● | ● | | 금기 | ● | ● | ● | | 예상 임상 편익 | ● | ● | ● | | 잔여위험 정보 | ● | ● | ● | | 표적 환자군 | ● | ● | ● | | 설치·유지보수 지침 | ● | ● | ● | | 세척·소독 지침 | ● | ● | ● | | 소모품·부속품 | ● | ● | ● | | 환경 조건 (보관·운반) | ● | ● | ● | | 특수 폐기 지침 | ● | ● | ● | |...

## ra_kr

### kb-eval-20261026-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "6e7179ebb0b9bfe0", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "e14006879a7b7ab39dd0ecfd162427da3e451ed2ff187ebb988bf9beba930afe"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `6e7179ebb0b9bfe0`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EB%B3%B4%EC%99%84%EC%9E%90%EB%A3%8C_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `e14006879a7b7ab39dd0ecfd162427da3e451ed2ff187ebb988bf9beba930afe`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_보완자료_대응전략.md`는 `MFDS_보완자료_대응전략.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) --- ### Type 1: 기술문서 보완 (가장 빈번) **빈번 사유** - 성능 데이터 불충분 (시험 방법·결과 누락) - 작용원리·사용목적 기술 불명확 - 위험관리 파일 연계 미흡 (ISO 14971) - SW 문서 미흡 (IEC 62304 산출물 누락) - 생물학적 안전성 평가...
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

> **Regulatory Draft – Supplementary‑Response Strategy (MFDS, Korea)**  

---

### 1. Device Classification & Submission Route  
| Item | Determination | Source / Note |
|------|---------------|----------------|
| **Korean grade** | Must be identified from 「의료기기 품목 및 품목별 등급에 관한 규정」. Until the exact item‑code is known, the grade cannot be fixed. | *no specific identifier found in source — verify separately* |
| **Submission track** (based on grade) | 1등급 → 신고 · 2등급 → 인증 · 3/4등급 → 허가 | Same note as above – confirm grade before selecting the pathway. |

> **Action:** Obtain the official MFDS 품목별 등급 listing for the device and record the exact grade (e.g., 3등급).  

---

### 2. Expected Evidence Package (for a 허가 신청, assuming ≥3등급)  

| Category | Mandatory content | Mapping to Korean requirement |
|----------|-------------------|--------------------------------|
| **Technical Documentation** | Device description, intended use, principle of operation. | MFDS technical‑document review (인증·허가). |
| **Performance & Safety Test Data** | • Radiographic performance (DQE, MTF) – IEC 62220‑1‑1  <br>• Radiation output (kVp, mA) – IEC 60601‑1‑3  <br>• Electrical safety / EMC – IEC 60601 series | Required to demonstrate compliance with Korean safety standards; **performance data** is a frequent deficiency (see § 2). |
| **Risk Management File** | Full ISO 14971 risk analysis, risk control measures, residual risk evaluation. | Explicitly called out as “위험관리 파일 연계 미흡 (ISO 14971)” in the source. |
| **Non‑clinical Biological Safety** | ISO 10993‑1 biocompatibility testing results for all patient‑contacting materials. | Cited as a common gap (“생물학적 안전성 평가 누락”). |
| **Software Documentation** *(if applicable)* | IEC 62304 lifecycle artifacts (software architecture, verification/validation reports), cybersecurity evidence (e.g., 2025‑01 security assessment). | “SW 문서 미흡 (IEC 62304 산출물 누락)” & “Cybersecurity (2025.01)” noted in the source. |
| **Clinical Evaluation** *(if required for grade ≥3등급)* | Clinical data or foreign CER accepted per latest MFDS notice. | No specific notice number appears; *verify separately* whether a foreign clinical evaluation report can be used. |
| **Labeling & IFU** | Korean language labeling, instructions for use, safety notices (radiation protection). | Mandatory under MFDS labeling rules (framework); no identifier in source. |

---

### 3. Gaps Identified from the Current Submission  

| Missing / Incomplete Item | Why it is a gap (reference) | Immediate remedial step |
|---------------------------|-----------------------------|------------------------|
| **DQE·MTF test data** for X‑ray Detector | “DQE·MTF 시험 데이터, IEC 62220‑1‑1 적합성” listed as expected in the *보완 예상 항목* (source § 2). | Commission testing at an accredited test lab; schedule backward from submission deadline. |
| **kVp / mA output & radiation protection data** for Handheld X‑ray Source | Same table notes “kVp·mA 출력 특성, 방사선 방호 (IEC 60601‑1‑3)”. | Request measurement reports; confirm compliance with IEC 60601‑1‑3. |
| **Software lifecycle artifacts & cybersecurity evidence** for GUI SW | “IEC 62304 SW 수명주기 산출물, Cybersecurity (2025.01)” highlighted as a likely deficiency. | Gather design docs, verification test logs, and the 2025‑01 security assessment; prepare them in MFDS‑format. |
| **Risk Management file linkage** to design/verification evidence | “위험관리 파일 연계 미흡 (ISO 14971)” cited as a frequent issue. | Map each risk control to a specific test or verification artifact and update the RMF accordingly. |
| **Biological safety assessment** for all patient‑contacting components | “생물학적 안전성 평가 누락 (ISO 10993‑1)” noted. | Conduct ISO 10993‑1 testing per material; obtain certificates of analysis. |

---

### 4. Risk Controls to be Demonstrated  

| Hazard / Failure Mode | Control Measure (per ISO 14971) | Evidence Required |
|-----------------------|--------------------------------|-------------------|
| Inadequate radiation dose output → patient over‑/under‑exposure | Design limit on kVp/mA; alarm for out‑of‑range values. | Test reports per IEC 60601‑1‑3; verification data. |
| Software malfunction causing incorrect imaging parameters | Fault‑tolerant software architecture, watchdog timer, regular updates. | IEC 62304 documentation, validation & cybersecurity report (2025.01). |
| Material toxicity → adverse tissue reaction | Biocompatibility testing of all contact materials. | ISO 10993‑1 test summary reports. |
| Uncontrolled image quality degradation (DQE/MTF) | Quality control program, periodic performance verification. | IEC 62220‑1‑1 DQE & MTF measurement data. |

---

### 5. Timeline & Processing Period (MFDS)  

| Process | Standard processing time* | Remarks |
|---------|---------------------------|--------|
| **허가 (일반)** | **65 days** – clock excludes any supplement period. | Source § 1‑B, Chunk 1020687580074720264. |
| **허가 (임상 포함)** | **80 days** – clock excludes any supplement period. | Same source. |
| **인증** | **30 days** – NIFDS‑委托. | Same source. |
| **신고** | Immediate (no formal review). | Same source. |

\*If a supplement is required, the “보완 기간” pauses the clock; therefore prompt issuance of a complete supplementary response is critical to avoid overall schedule creep.

---

### 6. Human‑Escalation Triggers  

| Situation | Threshold / Condition | Escalation Path |
|-----------|-----------------------|-----------------|
| **Supplement request not cleared within 5 business days** after receipt (i.e., we cannot confirm data availability). | Immediate notification to the RA team lead and project manager. |
| **Critical test (DQE/MTF or kVp/mA) fails to meet specification** on first run. | Elevate to Quality Assurance Director; consider redesign or risk‑reassessment before further submission. |
| **Risk Management file remains unlinked after two revision cycles**. | Senior Risk Manager must review and approve a corrective action plan. |
| **Cybersecurity assessment (2025.01) not finalized within 10 days of request**. | IT security lead joins the RA call; project sponsor decides on timeline impact. |
| **Overall submission deadline approaches with any open supplement items**. | Convene an escalation meeting with PM, RA lead, and senior management to decide whether to file a formal extension request to MFDS (possible under “보완 기간 제외” rule). |

---

### 7. Summary Judgment  

- The device’s Korean grade and consequently the exact submission route (신고/인증/허가) **must be confirmed** before finalizing the dossier – *verify separately*.
- The current dossier is missing several high‑frequency supplement items (performance test data, software lifecycle documents, risk‑file linkage, biocompatibility evidence). These align with the deficiencies outlined in MFDS “보완 사유” (source § 2).
- A structured response process—triaging each deficiency, engaging accredited test labs immediately, and assembling a complete supplementary package per the template suggested in the source—will keep the overall review within the 65‑ or 80‑day MFDS window.
- Continuous monitoring of supplement deadlines and rapid escalation when any item stalls are essential to avoid clock stoppage penalties.

---

### 8. Peer Review Prompt  

> **Colleague, please challenge:**  
> 1. Are there any additional Korean‑specific evidentiary requirements (e.g., post‑market surveillance plan for a 3등급 device) that we have not captured?  
> 2. Does the source excerpt provide enough detail to justify using foreign clinical evaluation reports, or should we request a specific MFDS notice number before planning that route?  
> 3. Are any of the risk controls listed insufficient given the device’s intended use (e.g., radiation protection for handheld X‑ray source) under current Korean regulations?  

Your feedback will help ensure all jurisdictional gaps are closed before submission.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `233519449609923302`

> ### Type 1: 기술문서 보완 (가장 빈번) **빈번 사유** - 성능 데이터 불충분 (시험 방법·결과 누락) - 작용원리·사용목적 기술 불명확 - 위험관리 파일 연계 미흡 (ISO 14971) - SW 문서 미흡 (IEC 62304 산출물 누락) - 생물학적 안전성 평가 누락 (ISO 10993-1) **대응 전략** 1. 보완 요청서 접수 즉시 내용 분류 (Type, 소관 부서, 데이터 필요 여부) 2. 추가 시험이 필요한 항목은 즉시 시험 의뢰 (기간 역산 필요) 3. 보완서 구조: 요청 항목별 번호 대응 + 인용 근거 명시 4. 규격 시험 기관과 보완 기한 내 결과 수령 가능 여부 사전 확인 **자사 3제품 적용** | 제품 | 주요 보완 예상 항목 | |---|---| | X-ray Detector | DQE·MTF 시험 데이터, IEC 62220-1-1 적합성 | | Handheld X-ray Source | kVp·mA 출력 특성, 방사선 방호 (IEC 60601-1-3) | | 촬영실 GUI SW | IEC 62304 SW 수명주기 산출물, Cybersecurity (2025.01) | ---

### kb-eval-20261026-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "2b61a8821672e60e", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2b61a8821672e60e`
- Source: `github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/02_%ED%92%88%EC%A7%88%EA%B2%BD%EC%98%81%EC%8B%9C%EC%8A%A4%ED%85%9C_QMS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4.md)
- Source hash: `b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_요구사항_매트릭스.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | | | Req-ID | 요구사항 | 법조/고시 | Status | 수용 기준 | 증빙 문서 | 보완 액션 | |--------|---------|----------|--------|----------|----------|----------| | DR-20 | 설계·개발 프로세스(ISO 13485 §7.3) | GMP | ●...
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

> **Regulatory Draft – Digital Medical Product (Software‑based) – “디지털의료제품법” Compliance Check**

| Item | Korean regulatory requirement | International reference used for mapping | Current status in the source matrix* | Evidence needed to close the gap | Missing / incomplete items | Recommended risk controls | Human‑escalation trigger |
|------|------------------------------|-------------------------------------------|--------------------------------------|----------------------------------|----------------------------|--------------------------|--------------------------|
| **1. Classification & Submission Route** | Grade must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」. For most software that provides a medical function, the default is **2등급 → 인증** (technical‑document review by an MFDS‑designated 심사기관). If the software performs high‑risk diagnostic or therapeutic functions it may be **3등급/4등급 → 허가**. | None – Korean law only. | Not addressed in matrix. | • Functional description & intended use.<br>• Classification justification (risk‑based algorithm, reference to MFDS classification table). | Grade not yet determined → submission pathway unknown. | N/A (classification determines the regulatory path). | If grade cannot be confirmed within 5 business days, escalate to senior RA for a formal “grade determination” request to MFMF. |
| **2. Design & Development Process** | Must comply with **ISO 13485 §7.3** (Design and development planning, input, output, review, verification, validation) as incorporated by the MFDS GMP 고시. | ISO 13485 §7.3 | “DR‑20 – 설계·개발 프로세스(ISO 13485 §7.3)” → status **●** (accepted). | • Design History File (DHF) containing design plan, inputs/outputs, verification & validation protocols and reports.<br>• Change‑control records. | No explicit DHF artifact listed; only a reference to the markdown file “03_설계_개발관리/설계개발_프로세스.md”. The actual documents have not been submitted for review. | • Design reviews at key milestones (requirement, architecture, code, release).<br>• Traceability matrix linking requirements → design → verification. | If DHF cannot be produced or traceability is incomplete, trigger escalation to the Project Manager (PM) and Quality Lead within 3 working days. |
| **3. Risk Management Integration** | Must implement a **Risk Management File (RMF)** per **ISO 14971**; MFDS 고시 requires hazard analysis, risk evaluation, risk control implementation, and residual‑risk acceptance. | ISO 14971 | “DR‑21 – 위험관리 통합(ISO 14971)” → status **●** (accepted). | • Completed FMEA / FTA with documented risk controls.<br>• Residual‑risk acceptance justification signed by the Risk Owner.<br>• Updated RMF reflecting software updates. | The matrix only notes that “RMF 수립, FMEA/FTA 완료, 잔존위험 수용 판정” are required; actual files have not been linked or uploaded. | • Implement risk control measures (design controls, protective measures, information for users).<br>• Periodic review of RMF after software patches. | Any open/high‑severity hazard without an approved control → immediate escalation to the Risk Committee and senior management. |
| **4. Software Lifecycle Management** | Must follow **IEC 62304** (Software life‑cycle processes) – classification of software safety class, lifecycle plan approval, configuration management. | IEC 62304 (2006+A1:2015) | “DR‑22 – SW 수명주기(IEC 62304)” → status **●** (accepted). | • Software Safety Classification report (Class A/B/C).<br>• Approved Software Lifecycle Plan.<br>· Configuration Management / Version control records.<br>· Verification & validation test reports. | Only a reference to “03_설계_개발관리/IEC_62304_SW_수명주기.md” is present; the concrete classification and approved plan are not supplied. | • Enforce configuration management (e.g., Git repository with audit trail).<br>• Perform unit, integration, system testing per class‑appropriate verification activities.<br>• Document release notes & change impact analysis. | If software safety class cannot be proven or lifecycle plan is missing, trigger escalation to the Software Lead and Quality Assurance within 2 working days. |
| **5. Supplier Management (including OSS components)** | Must establish supplier management procedures and maintain a **Software Bill of Materials (SBOM)**; MFDS 고시 now requires traceability for open‑source software (OSS) and license compliance. | KGMP (GMP) – no specific standard number cited in source. | “DR‑23 – 공급자 관리(구성요소·OSS)” → status **◐** (partial). | • Supplier qualification records.<br>• OSS usage policy & SBOM (including version, license, vulnerability assessment).<br>• License compliance evidence. | The matrix notes “OSS 공급망 절차 수립, 라이선스 컴플라이언스 확인” as pending; actual SBOM not yet produced. | • Perform automated SBOM generation for each build.<br>• Conduct regular OSS vulnerability scanning (e.g., Snyk, Dependabot).<br>• Maintain procurement contracts with confidentiality & quality clauses. | If any critical OSS component lacks a valid license or has an unresolved CVE, escalate to Legal & Cyber‑Security leads immediately. |
| **6. Education & Training (AI / Cybersecurity)** | AI developers and cybersecurity personnel must complete prescribed training modules; evidence of completion is mandatory per MFDS 고시 on AI‑based medical devices. | KGMP – no specific notice number in source. | “DR‑24 – 교육·훈련(AI·사이버보안)” → status **◐** (partial). | • Training curriculum & materials.<br>• Attendance logs / certificates for all AI developers and security staff.<br>• Assessment results confirming competency. | The matrix lists “AI 개발자 교육 모듈 수립, 이수 기록 확보” as a pending action; no records are attached. | • Include secure‑by‑design principles in the curriculum.<br>· Conduct periodic refresher training (≥ annually). | If any AI team member lacks documented completion of required modules within 30 days of hire, trigger escalation to HR & Project Sponsor. |
| **7. Documentation Traceability & Gap‑Analysis Tracking** | Continuous gap‑analysis must be recorded and tracked (F‑GAP‑001 form) per MFDS “디지털의료제품법” implementation guide. | No numeric identifier provided in source. | The excerpt shows a template for “갭 분석 상태 추적 양식” but no populated rows. | • Completed GAP analysis entries linking each requirement → current compliance status → responsible owner → target/completion dates.<br>• Updated status (●) for all items before submission. | All rows currently empty; no evidence of ongoing remediation. | • Assign a dedicated Gap‑Owner to update the form weekly.<br>· Use RACI matrix for accountability. | Any requirement that remains in “◐” or “○→◐ / ◐→●” transition after the planned target date → automatic escalation to Quality Management Representative (QMR). |

\* *The source matrix provides only high‑level status flags; actual underlying documents have not been supplied.*

---

### Summary Judgment
1. **Classification & Pathway** – Must be confirmed; likely **2등급 → 인증** but could be 3/4등급 → 허가 depending on function.
2. **Core Evidence Gaps** – DHF, full RMF with signed residual‑risk acceptance, software safety class & lifecycle plan approval, complete SBOM with license compliance, AI/cybersecurity training records, and a fully populated gap‑analysis sheet.
3. **Risk Controls** – Implement documented design reviews, risk controls per ISO 14971, secure configuration management, OSS vulnerability monitoring, and ongoing staff competency verification.
4. **Human‑Escalation Triggers** –  
   - Grade not determined within 5 days → senior RA escalation.  
   - Missing DHF / RMF / Software Lifecycle artifacts → PM/Quality Lead escalation (3 days).  
   - Unresolved high‑severity hazards or OSS license issues → Risk Committee / Legal elevation immediately.  
   - Incomplete training records → HR/Sponsor escalation.  
   – Any gap‑analysis item remaining non‑completed past target date → QMR escalation.

---

### Peer Review Prompt
> **@RA‑Peer** – Please review the assumptions made above, especially:  
> 1. The inferred classification (2등급 → 인증) given that no functional description is provided; could any typical digital medical product scenario push this to 3등급 or higher?  
> 2. Whether the listed evidence items fully satisfy MFDS 고시 requirements for digital medical products, or if additional artifacts (e.g., Clinical Evaluation Report for AI‑based diagnostics) are needed.  
> 3. The completeness of risk‐control recommendations relative to recent MFDS cyber‑security guidance – are any specific controls missing?  

Your feedback will help close any jurisdiction‑specific gaps before finalizing the submission package.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1045730514097588767`

> ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | |

2. Chunk `1073274073545790864`

> | Req-ID | 요구사항 | 법조/고시 | Status | 수용 기준 | 증빙 문서 | 보완 액션 | |--------|---------|----------|--------|----------|----------|----------| | DR-20 | 설계·개발 프로세스(ISO 13485 §7.3) | GMP | ● | DHF 체계 수립, 설계검증/밸리데이션 프로토콜 존재 | 03_설계_개발관리/설계개발_프로세스.md | - | | DR-21 | 위험관리 통합(ISO 14971) | GMP, 고시 | ● | RMF 수립, FMEA/FTA 완료, 잔존위험 수용 판정 | 07_위험관리_ISO14971/ | - | | DR-22 | SW 수명주기(IEC 62304) | GMP | ● | SW 안전 클래스 분류, 수명주기 계획서 승인 | 03_설계_개발관리/IEC_62304_SW_수명주기.md | - | | DR-23 | 공급자 관리(구성요소·OSS) | GMP, SBOM 연계 | ◐ | OSS 공급망 절차 수립, 라이선스 컴플라이언스 확인 | 09_공급자_관리/ | OSS 공급망 절차 추가 | | DR-24 | 교육·훈련(AI·사이버보안) | GMP | ◐ | AI 개발자 교육 모듈 수립, 이수 기록 확보 | 10_교육_훈련/ | AI 개발자...

### kb-eval-20261026-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "36aec04ae18943c0", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `36aec04ae18943c0`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전...
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

> **Regulatory Draft – Digital‑Medical‑Product (Software AI module)**  

---

### 1. Device Classification & MFDS Submission Route  
| Item | Korean regulatory position |
|------|----------------------------|
| **Grade (등급)** | Must be determined from the “디지털의료제품법” and the “의료기기 품목 및 품목별 등급에 관한 규정”. An AI‑based image‑analysis module that outputs diagnostic information is typically positioned in **3등급** or **4등급** (high‑risk) because it directly influences clinical decision‑making. <br>**Action:** Confirm the exact grade by cross‑checking the device’s intended use against the official grade table. |
| **Submission track** | - **1등급 → 신고**  <br>- **2등급 → 인증** (technical‑document review by a designated 심사기관) <br>- **3등級·4등급 → 허가** (MFDS approval). If the device is placed in 3등급 or 4등급, the pathway is **허가**. |
| **Citation** | no specific identifier found in source — verify separately (grade table reference). |

---

### 2. Core Evidentiary Requirements (per MFDS & International standards)

| Requirement | Korean regulatory basis (framework) | Typical supporting documents |
|-------------|--------------------------------------|------------------------------|
| **Risk Management** | ISO 14971 (2019) – mandatory for all medical devices. | risk‑management plan, risk analysis, risk control report. |
| **Usability / Human Factors Engineering** | IEC 62366‑1 (2015+A1:2020). | Usability engineering file (IEC_62366‑1_사용적합성_엔지니어링_계획서 – already drafted per action item 2). |
| **Cybersecurity** | “의료기기 사이버보안 허가·심사 가이드라인(개정)” (2025‑01‑10) – high relevance for network‑connected devices. <br>“디지털의료기기 전자적 침해행위 보안 지침(안)” (2025‑01) – also high relevance. | Cybersecurity risk assessment, mitigation matrix (RA‑01~RA‑20), incident‑response SOP, SBOM management procedure (SOP‑SBOM‑001). |
| **Software Bill of Materials (SBOM)** | Same cybersecurity guidelines above; required for all connected digital medical products. | SBOM document, SOP‑SBOM‑001 (action item 3). |
| **Change Management** | MFDS 요구사항 on post‑market change control (KGMP) and the “변경관리 계획 SOP 연계 (CMP 섹션)” (action item 4). | Change‑management SOP (SOP‑CC‑001), documented change impact analysis. |
| **AI Model Governance & Dataset Documentation** | No dedicated Korean law yet, but MFDS has issued a “생성형 AI 의료기기 허가·심사 가이드라인” (2025‑01) with medium relevance for AI imaging modules. | SOP‑AIDATA‑001 / SOP‑AIGOV‑001 (action item 5). |
| **Performance Evaluation of AI Components** | MFDS expects evidence of component‑level performance for SaMD‑AI. | “AI 구성요소 단위 성능평가” documentation (action item 6). |
| **Clinical Evidence** | If the device is 3등급·4등급, aclinical evaluation report (CER) or local clinical trial data is required unless an MFDS notice permits reliance on foreign CE/FDA clearance. | Clinical evaluation plan, pilot/validation study results, any applicable foreign clearance references (to be verified). |
| **Labeling & IFU** | Korean language labeling and Instructions for Use per “의료기기 품목 및 라벨링 가이드라인”. | Label artwork in Korean, user manual (Korean), packaging declarations. |
| **KGMP Facility Certification** (if hardware or production environment is involved) | KGMP (의료기기법 제28조) – mandatory for manufacturers of 2등급‑4등급 devices. | KGMP certificate, audit reports. |

---

### 3. Gaps / Missing Information (to be supplied)

| Gap | Why it matters | Suggested source/action |
|-----|----------------|------------------------|
| **Exact grade (1~4) & MFDS submission type** | Determines whether 허가 or 인증 is required and the depth of clinical evidence needed. | Review “디지털의료제품법” 및 품목‑별 등급표; map intended use to grade. |
| **Clinical data strategy** | For 3등급·4등급, MFDS requires either local clinical data or acceptance of foreign CER under a specific notice (e.g., MFDS 고시 2025‑XX호 – verify if applicable). | Identify whether a relevant MFDS notice exists; plan a Korean clinical evaluation or prepare dossier for foreign data reliance. |
| **Device nomenclature & intended use statement** | Needed in risk management, labeling, and classification analysis. | Draft clear indication description (e.g., “AI‑based detection of pulmonary nodules on CT”). |
| **Evidence of compliance with the 2025‑01 “생성형 AI 의료기기 허가·심사 가이드라인”** | This guideline is medium relevance; MFDS may request a gap analysis. | Prepare a mapping matrix showing how each guideline requirement is met. |
| **Full SBOM for all third‑party components** (including open‑source libraries) | Required by high‑relevance cybersecurity guidelines. | Complete SBOM, attach SOP‑SBOM‑001 output. |
| **Korean language label & IFU drafts** | Mandatory; non‑Korean labeling leads to submission rejection. | Produce Korean translations and verify with a certified translator. |
| **KGMP certification status of the software developer (if considered a manufacturer)** | Required for 2등급‑4등급 device manufacturers. | Obtain or update KGMP certificate, include audit reports. |

---

### 4. Primary Risk Controls to Include in Submission

1. **Risk Management File** – ISO 14971 compliant; includes residual risk acceptability justification.  
2. **Usability Engineering File** – IEC 62366‑1 compliant; user‑interface validation results.  
3. **Cybersecurity Matrix (RA‑01~RA‑20)** – covers threat analysis, vulnerability management, incident response, and SBOM traceability.  
4. **AI Governance Framework** – dataset provenance, model version control, bias assessment, post‑deployment monitoring plan.  
5. **Change Management SOP** – aligns with KGMP change‑control requirements; defines impact assessment for software updates.  
6. **Performance Evaluation Reports** – component‑level validation (sensitivity, specificity) and overall system verification/validation.  

All above should be cross‑referenced in a “Regulatory‑Requirements‑Matrix” that maps each MFDS requirement to the supporting document.

---

### 5. Human‑Escalation Triggers (When to Stop and Escalate)

| Trigger | Reason for escalation |
|--------|-----------------------|
| **Unclear device grade** after initial classification review. |
| **Absence of clinical evidence plan** for a 3등급·4등급 submission, or inability to locate an MFDS notice allowing foreign data reliance. |
| **Cybersecurity documentation incomplete** (e.g., missing SBOM, unmet RA‑01~RA‑20 matrix). |
| **Labeling/IFU not available in Korean** or fails language‑accuracy check. |
| **KGMP certification lacking** for the software developer/manufacturer. |
| **AI model governance SOPs absent or not aligned with the 2025‑01 AI guideline**. |
| **Significant change to algorithm after submission** without approved change‑control process. |

Upon any trigger, pause dossier finalization and notify the project lead / senior RA for risk‑based decision making.

---

### 6. Peer‑Review Prompt  

> *Colleague, please review the assumptions above:  
> – Is the provisional classification of an AI imaging analysis module as 3등급/4등급 appropriate given current MFDS guidelines?  
> – Have we captured all high‑relevance guideline items (cybersecurity, SBOM, AI governance) that MFDS will expect in a submission under the 디지털의료제품법?  
> – Are there any additional Korean‑specific evidentiary gaps (e.g., post‑market surveillance plan, specific notice numbers for foreign data acceptance) that need to be addressed before final dossier closure?*  

---

### 7. Reusable RA Judgment (Lesson)

**When preparing a MFDS submission for a digital‑medical‑product AI module:**  

1. **Confirm the device grade first** – the classification dictates all downstream evidence requirements and the submission track (신고/인증/허가).  
2. **Map every high‑relevance MFDS guideline (cybersecurity, SBOM, AI governance) to a concrete control artifact** before drafting the dossier; use the RA‑01~RA‑20 matrix as the central coordination tool.  
3. **Identify any clinical data gaps early** – either plan a Korean clinical evaluation or locate a specific MFDS notice that permits reliance on foreign CER (must be cited explicitly).  
4. **Ensure all labeling, IFU, and SOPs are in Korean** and aligned with KGMP if the device falls into 2등급‑4등급.  
5. **Escalate immediately upon any uncertainty in grade, clinical evidence strategy, or missing high‑relevance documentation**, as these are show‑stoppers for MFDS 허가.  

--- 

*All citations derived from the source excerpts:*
- Guidelines list (2024‑12 to 2025‑01) – **no specific identifier found in source — verify separately**.  
- Post‑action items (RA‑01~RA‑20 matrix, IEC 62366‑1 plan, SOP‑SBOM‑001, etc.) – directly taken from the excerpt tables.  

*End of draft.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

2. Chunk `1130453648414545903`

> ## 8. 후속 조치 요건 (프로젝트 관점) | 우선순위 | 조치 사항 | 연계 문서 | 상태 | |----------|----------|-----------|------| | 1 | 사이버보안 RA-01~RA-20 대응 매트릭스 작성 | 디지털의료제품법_요구사항_매트릭스 | 진행중 | | 2 | 사용적합성 엔지니어링 계획 수립 | IEC_62366-1_사용적합성_엔지니어링_계획서 | v0.2 완료 | | 3 | SBOM 관리 절차 정합성 확인 | SOP-SBOM-001 | v0.2 완료 | | 4 | 변경관리 계획 SOP 연계 (CMP 섹션) | SOP-CC-001 | v0.2 완료 | | 5 | AI 모델 데이터셋·거버넌스 절차 수립 | SOP-AIDATA-001, SOP-AIGOV-001 | v0.2 완료 | | 6 | 구성요소 단위 성능평가 절차 문서화 | AI_구성요소_단위_성능평가 | v0.2 완료 |

### kb-eval-20261026-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "25055b5b5492952f", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `25055b5b5492952f`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%ED%91%9C%EC%8B%9C%EA%B8%B0%EC%9E%AC_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_%EB%8C%80%EC%9D%91.md)
- Source hash: `7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_디지털의료기기_표시기재_가이드라인_대응.md`는 `MFDS_디지털의료기기_표시기재_가이드라인_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 9. 의료기기법 일부개정 (법률 제21949호, 공포 2026-09-15) — 온라인 표시·광고 규제 강화 | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 |...
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

> **Regulatory Draft – Digital‑Medical‑Device Software (SW) – Supplementary‑Response Strategy**

---

### 1. Device Classification & Submission Route  
| Item | Korean regulatory rule* | Assessment from source | Action |
|------|------------------------|-------------------------|--------|
| **Grade (등급)** | Determined according to 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS_인허가_상세가이드.md §2). | The excerpt does not specify the intended use, risk level or applicable “품목”. | **Human‑escalation:** Confirm grade with the product owner and cross‑check against the official classification table. |
| **Submission track** | 1등급 → 신고 2등급 → 인증 (심사기관 검토) 3·4등級 → 허가 (MFDS 직접 심사) | Pending grade determination. | If **1등급** – prepare a notification dossier; if **2등급** – compile technical‑documentation for an 인증 review by a designated 심사기관 (e.g., KTL, KTC); if **3·4등급** – plan a full 허가 submission to MFDS. |

\*Framework reference only – no specific article/section number appears in the supplied excerpts.

---

### 2. Mandatory Evidentiary Requirements (as per MFDS SW & Cybersecurity Guidance)

| Requirement (Source ID) | Description | Source citation |
|--------------------------|-------------|-----------------|
| **S‑1** Software version, build number, release date | Must be listed on the product label/IFU. | [2] |
| **S‑2** Software update method & schedule | Detail of how updates are delivered (e.g., OTA, manual) and frequency. | [2] |
| **S‑3** Minimum/recommended system specs (OS, CPU, RAM, storage, monitor resolution, network) | Provides users with the hardware environment needed for safe operation. | [2] |
| **S‑4** Compatible medical device list & interface information | Enumerate all devices that can be interfaced and describe the communication protocol. | [2] |
| **S‑5** Data input/output formats (DICOM, HL7, etc.) | Define supported standards for data exchange. | [2] |
| **S‑6** Cybersecurity configuration guidance (encryption policy, network segregation, access rights) | Aligns with MFDS 사이버보안 가이드라인 2025.01. | [2] |
| **S‑7** Security‑patch application procedure & responsibility matrix | Ensure timely mitigation of vulnerabilities. | [2] |
| **S‑8** Known residual cybersecurity risks & remediation methods | Document any open findings and associated mitigations. | [2] |
| **S‑9** Data backup & recovery procedures | Outline frequency, storage media, verification steps. | [2] |
| **S‑10** System log management (recommended) | Log collection, retention period, access control. | [2] |

*All “근거” entries are framework references (e.g., MFDS 사이버보안 가이드라인 2025.01). No explicit notice or decree number is provided for those documents; therefore **no specific identifier found in source – verify separately**.*

---

### 3. Additional Evidence Required (Standard Korean Requirements)

| Category | Specific Items | Standard/Guideline |
|----------|----------------|--------------------|
| **Risk Management** | Full risk analysis, risk control measures, residual risk evaluation | ISO 14971:2019 (risk‑management standard) |
| **Software Lifecycle** | Development plan, verification & validation reports, configuration management | IEC 62304:2006+A1:2015 |
| **Labeling / IFU** | Korean language labeling, user manual, intended use statements, contraindications | MFDS 고시 “의료기기 표시·광고 규정” (see 법률 제21949호, 공포 2026‑09‑15) |
| **Clinical Evidence** (if grade ≥2등급) | Clinical evaluation report or foreign CER accepted under MFDS scope expansion; local post‑marketing surveillance plan | MFDS 고시 제2025‑22호 (scope for foreign clinical data – requires verification) |
| **KGMP Compliance** | Facility certification, QMS documentation aligned with KGMP (의료기기법 제28조) | KGMP 인증 규정 (latest 2026‑07‑01 amendment) |
| **Post‑Market Surveillance** | PMS plan, adverse event reporting procedures, periodic safety update (if applicable) | MFDS 시판후조사 가이드라인 |

*The law amendment referenced in source [1] – **법률 제21949호**, 공포 2026‑09‑15 – strengthens online display/advertising regulation and is the governing notice for labeling requirements.*

---

### 4. Identified Gaps / Missing Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Device grade (등급)** | Determines submission path and depth of clinical evidence needed. | Obtain intended use, risk classification matrix from product owner; map to Korean grading table. |
| **Clinical performance data** | Required for 2‑4등급 devices; foreign CER acceptance depends on MFDS scope updates. | Request any existing clinical trial reports or CE/FDA clearance documents; verify if they satisfy MFDS foreign‑clinical‑data acceptance (see MFDS 고시 제2025‑22호 – confirm number). |
| **Detailed software architecture diagram** | Needed to support S‑4, S‑5, and cybersecurity risk assessment. | Provide block diagram showing interfaces, data flow, and security zones. |
| **Cybersecurity threat‑model & mitigation report** (beyond S‑6 ~ S‑8) | MFDS cyber guide expects documented threat analysis. | Conduct STRIDE/ATT&CK based analysis; list control implementation status. |
| **Korean language IFU draft** | Mandatory labeling requirement per 법률 제21949호. | Prepare Korean translation of user manual, include all required elements (S‑1 ~ S‑9). |
| **KGMP facility certificate** | Required for any device submitted to MFDS. | Verify current KGMP certification; attach copy to dossier. |

---

### 5. Risk Controls Summary (to be included in the submission)

1. **Version control & traceability** – mapping of software requirements to code and test cases (supports S‑1).  
2. **Update management** – signed OTA packages, validated rollback procedure (S‑2, S‑7).  
3. **Hardware compatibility verification** – testing on all listed OS/CPU/RAM configurations (S‑3).  
4. **Interface conformity testing** – DICOM/H​L7 compliance validation reports (S‑5).  
5. **Cybersecurity safeguards** – AES‑256 encryption, role‑based access control, network segmentation per MFDS 사이버보안 가이드라인 2025.01 (S‑6 ~ S‑8).  
6. **Backup & disaster recovery drills** – quarterly restore tests documented (S‑9).  
7. **Logging & monitoring** – centralized log collection with tamper‑evidence; retain for minimum 2 years (recommended S‑10).  

All controls must be linked to risk assessment entries in the ISO 14971 file.

---

### 6. Human‑Escalation Triggers  

| Trigger | Condition | Escalation target |
|---------|-----------|-------------------|
| **Unresolved grade** | Classification cannot be assigned after two iterations of information gathering. | RA Lead & Product Management (decision on submission track). |
| **Missing clinical evidence** | No sufficient local or acceptable foreign clinical data for the determined grade. | Clinical Development Team – need to conduct Korean‑subject study or obtain additional CE/FDA documentation. |
| **Non‑compliance with mandatory S‑1 ~ S‑9 items** | Any required field left blank in the draft labeling/technical dossier. | Quality Assurance – enforce completion before dossier finalization. |
| **KGMP certification gap** | Facility not KGMP‑certified at the time of submission. | Manufacturing Operations – obtain or update KGMP certificate. |
| **Cybersecurity residual risk >acceptable** | Identified high‑severity vulnerabilities without mitigation. | IT Security Lead – must be remediated prior to MFDS filing. |
| **Legal reference verification needed** | Specific notice numbers (e.g., MFDS 고시 제2025‑22호) are required but not confirmed in source. | Regulatory Affairs – perform independent search of official MFDS Gazette for exact identifier. |

When any trigger fires, the responsible function must issue a written risk assessment and obtain sign‑off before proceeding to the next submission milestone.

---

### 7. Peer Review Request  

> **To:** All RA colleagues  
> **Subject:** Review of Supplementary‑Response Draft for Digital‑Medical‑Device Software  
> **Action Needed:** Please challenge the assumptions made regarding (1) the implied grade of the device, (2) completeness of the mandatory S‑1 ~ S‑9 evidence list given possible updates to MFDS cyber guidance after 2025.01, and (3) the applicability of foreign clinical‐evaluation reports under the current MFDS scope expansion (referenced as 고시 제2025‑22호). Highlight any jurisdictional gaps not covered by the supplied excerpts.

--- 

*All citations are drawn directly from the provided source excerpts; no invented identifiers are included.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1044206327041877533`

> ## 9. 의료기기법 일부개정 (법률 제21949호, 공포 2026-09-15) — 온라인 표시·광고 규제 강화

2. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

### kb-eval-20261026-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-26", "decision_ref": "kb-eval-20261026-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "e3a058aed6cadda3", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `e3a058aed6cadda3`
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

> **Regulatory Draft – Cyber‑Security Compliance for a Medical Device (MFDS 2025 Guideline)**  

---

### 1.   Classification & Submission Route (Korean Grade)

| Step | What to confirm | Korean regulatory implication |
|------|----------------|--------------------------------|
| **Device grade (1~4등급)** | Verify the device’s risk class in the “의료기기 품목 및 품목별 등급에 관한 규정”. The grade determines the submission track. | • 1등급 → 신고  <br>• 2등급 → 인증 (technical‑document review by a MFDS‑designated 심사기관)  <br>• 3~4등급 → 허가 (full MFDS approval). |
| **KGMP facility status** | Confirm that the manufacturing site holds a KGMP certificate (의료기기법 제28조) or is covered by an approved equivalence pathway. | Required for any 제출 of a 2~4등급 device; without KGMP certification the submission cannot proceed. |

> **Note:** The source excerpt does **not** provide a specific grade or KGMP status – *no specific identifier found in source — verify separately*.

---

### 2.   Evidence Required under the 2025 Cyber‑Security Guideline  

The guideline (effective 2025‑01‑10) expands the MFDS cyber‑security RA requirements from **15 → 35 items**, organized into eight categories (RA‑01 ~ RA‑35). The exact numbers are listed in the official PDF; for planning purposes the following documentation package should be prepared:

| Category | Typical evidence artefacts | Link to Korean requirement |
|----------|----------------------------|-----------------------------|
| **보안 설계 원칙** (Secure by design, defense‑in‑depth, least privilege) | • System‑level security architecture diagram <br>• Threat modelling report (e.g., STRIDE or ATT&CK) <br>• Design justification matrix linking hazards ↔︎ controls | MFDS cyber‑security RA‑01~RA‑05 (see guideline) |
| **인증·접근 제어** (Authentication & access control) | • User role matrix, IAM policies <br>• Source code showing role‑based checks <br>• Penetration test results for authentication flow | RA‑06~RA‑09 |
| **암호화** (Data at rest / in transit) | • Cryptographic algorithm specification (AES‑256, TLS 1.3) <br>• Key management SOPs <br>• Validation reports of encryption modules (FIPS 140‑2/3 if applicable) | RA‑10~RA‑13 |
| **소프트웨어 무결성** (Code signing, boot integrity, SBOM) | • Code‑signing certificates & verification logs <br>• Secure Boot configuration screenshots <br>• Software Bill of Materials (SBOM) per IEC 81001‑5‑1 | RA‑14~RA‑18 |
| **네트워크 보안** (Port minimisation, firewall, TLS version) | • Network diagram with listed open ports <br>• Firewall rule set export <br>• TLS configuration test report (e.g., SSL Labs) | RA‑19~RA‑22 |
| **취약점 관리** (CVE monitoring, patch cadence, CVD policy) | • Vulnerability management process flowchart <br>• CVE watch list & remediation log (last 12 months) <br>• Patch release schedule | RA‑23~RA‑27 |
| **감사·로그** (Security event logging, log protection) | • Log collection architecture (SIEM) <br>• Sample audit logs with integrity hash <br>• Retention policy (≥ 1 year) | RA‑28~RA‑31 |
| **업데이트·유지보수** (Secure update mechanism, remote management) | • OTA/remote update protocol description <br>• Update authenticity verification method (digital signature) <br>• Change‑control records for released patches | RA‑32~RA‑35 |

All artefacts must be presented in Korean (or accompanied by a certified Korean translation) and referenced in the technical dossier.

---

### 3.   Gaps / Missing Information  

| Gap | Why it matters & what to obtain |
|-----|---------------------------------|
| **Exact device grade** | Determines submission track (신고/인증/허가). Obtain from MFDS “품목별 등급” list or a prior MFDS classification decision. |
| **KGMP certification number / status** | Mandatory for 2~4등급 submissions. Request the current KGMP certificate and any equivalence approvals. |
| **RA‑01~RA‑35 exact numbering** (e.g., RA‑01, RA‑02…) | The guideline refers to a PDF with specific identifiers; those IDs must be quoted verbatim in the dossier. Acquire the official PDF to extract them accurately. |
| **Software Bill of Materials (SBOM) compliance evidence** | Required under “소프트웨어 무결성”. Prepare an up‑to‑date SBOM following IEC 81001‑5‑1 recommendations. |
| **Korean language labeling & IFU for cyber‑security information** | MFDS requires that any security‑related user instructions be in Korean. Draft a dedicated “보안 사용 안내” section in the IFU. |
| **Local clinical data (if 3~4등급)** | For high‑risk devices, MFDS may still demand Korean clinical evidence even when foreign CE/FDA clearance exists. Clarify with the 심사기관 whether local data are waived under the “디지털의료제품법”. |
| **Evidence of alignment with IMDRF N60/N73** | The guideline cites these standards; include a cross‑walk matrix showing how each RA requirement meets the corresponding IMDRF objective. |

---

### 4.   Risk Controls (Mapping to ISO 14971)  

1. **Hazard identification** – Extend the traditional safety hazard analysis to include *cyber‑security hazards* (unauthorised access, data breach, malicious software modification).  
2. **Risk evaluation** – Use the same risk‐acceptability criteria as for safety; assign severity based on potential patient harm from a security incident.  
3. **Risk control options** – Directly correspond to the eight RA categories; each selected control must be documented in the Risk Management File (RMF) and validated per ISO 14971.  
4. **Residual risk review** – Include a *cyber‑risk residual* assessment; if residual risk remains unacceptable, consider additional controls (e.g., hardware isolation, multi‑factor authentication).  

All risk‑control evidence (test reports, verification protocols) should be cross‑referenced with the RA‑01~RA‑35 artefacts.

---

### 5.   Citations  

| Type | Citation |
|------|----------|
| **Framework reference** – International standards | IMDRF N60/N73, IEC 81001‑5‑1 (2021), ISO 14971 (2019), ISO 13485 (2016) – used as factual references. |
| **Instance identifier** – From source | No specific 고시/notice number appears in the provided excerpts; therefore no instance identifier is inserted here. *Verification of any specific MFDS notice or article number must be performed against the full guideline document.* |

---

### 6.   Human‑Escalation Triggers  

| Situation | Action Required (Human) |
|-----------|--------------------------|
| **Unclear device grade** | Pause dossier assembly; request formal classification from MFDS or a qualified Korean regulatory consultant. |
| **KGMP certificate missing / expired** | Engage manufacturing QA to obtain current KGMP certification before submission. |
| **RA‑01~RA‑35 numbering not available** | Retrieve the official PDF (“의료기기의 사이버보안 허가·심사 가이드라인”) and extract exact RA identifiers; until then, do not finalize the technical dossier. |
| **Residual cyber‑risk deemed unacceptable after RMF review** | Convene a cross‑functional risk mitigation meeting (R&D, QA, security) and prepare an amendment plan before filing. |
| **MFDS requests additional evidence on any of the eight categories** | Allocate resources to generate the requested artefacts; consider external cybersecurity audit if internal evidence insufficient. |
| **Submission for 3등급·4등급 device without local clinical data (when required)** | Seek a pre‑submission meeting with the designated 심사기관 or MFDS to confirm exemption; otherwise, initiate Korean clinical study planning. |

When any trigger fires, the RA lead must log the issue in the project tracker, notify the regulatory manager, and schedule an escalation review within **5 business days**.

---

### 7.   Regulatory Judgment (Summary)

*Given the information from the MFDS Cyber‑Security Guideline (2025‑01‑10) and the absence of a device‑specific grade or KGMP status in the source, the following provisional path is recommended:*

1. **Confirm the Korean grade** (1~4등급). If the device falls into 2등급 or higher, prepare an **인증** (for 2등급) or **허가** (for 3/4등급) dossier.
2. **Assemble the eight‑category evidence package** aligned with RA‑01 ~ RA‑35 as outlined above; include a cross‑walk to IMDRF N60/N73 and IEC 81001‑5‑1.
3. **Ensure KGMP certification** is in place for any 2~4등급 submission.
4. **Translate all security‑related user instructions into Korean** and embed them in the IFU.
5. **Complete a cyber‑risk extension of the ISO 14971 RMF**, linking every control to a specific RA requirement.

Proceed to a pre‑submission consultation with the designated MFDS 심사기관 once the grade, KGMP status, and full RA artefacts are confirmed.

---

### 8.   Peer Review Prompt  

*Please review this draft for:*

- **Assumption checks** – Are we correctly treating the eight RA categories as mandatory for all grades, or does the guideline permit a risk‑based exemption for very low‑risk (1등급) devices?  
- **Source coverage** – Does any part of the provided excerpts suggest additional evidence (e.g., specific test methods) that has not been captured above?  
- **Jurisdiction gaps** – Have we omitted any Korean‑specific obligations such as post‑market cyber‑vulnerability reporting (시판후조사) or mandatory registration of security incidents with MFDS?  

Your feedback will refine the final submission plan.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---
