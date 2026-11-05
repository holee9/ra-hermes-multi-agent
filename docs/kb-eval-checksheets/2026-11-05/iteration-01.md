# KB Eval Checksheet - 2026-11-05 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261105-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "542adbe4743fba8e", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md", "source_hash": "b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `542adbe4743fba8e`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/FDA_AI_Additional_Information_%EB%8C%80%EC%9D%91_%EC%A0%84%EB%9E%B5.md)
- Source hash: `b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82`
- Focus: submission evidence gaps
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `FDA_AI_Additional_Information_대응_전략.md`는 FDA AI/ML 의료기기 심사 중 additional information 또는 deficiency response 대응 전략 문서입니다.
- 현재 excerpt 핵심: ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합 > 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: htt...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – FDA 510(k) Submission AI Response Planning**

---

### 1. Bottom‑Line Recommendation
* **Pathway:** Premarket Notification (510(k)) – Class II device (most likely, pending final product‑code determination).  
* **Core Action:** Compile a complete “substantial‑equivalence” dossier that addresses the five evidence categories most frequently requested in FDA Additional Information (AI) letters:  

1. **Design & Verification/Validation**  
2. **Risk Management** (ISO 14971‑based file)  
3. **Clinical Evidence / Equivalence**  
4. **Labeling & Instructions for Use (IFU)**  
5. **Software Documentation (if applicable)**  

*Any AI request that cannot be satisfied with these elements will trigger a senior‑level escalation (see §8).*

---

### 2. Classification & Submission Route
| Factor | Determination |
|--------|----------------|
| **Regulatory class** | Class II – the majority of imaging, diagnostic and software‑enabled medical devices fall here; submit via 510(k) under **21 CFR §807.92** (content requirements). |
| **Applicable product code** | To be assigned after a product‑code search in the FDA database (e.g., “LLE” for image processing, “MDM” for medical device monitoring). |
| **Quality System** | ISO 13485:2016–aligned QMS required under **21 CFR §820** (effective Feb 2026 with QMSR alignment). |
| **UDI requirement** | UDI on label and packaging per **21 CFR §830.10‑§830.60**. |

*If the device is novel and no predicate exists, a De Novo request would be considered; however, AI trends show most deficiencies are for standard 510(k) predicates.*

---

### 3. Evidence Required (Standard 510(k) Content)
| Section | FDA expectation | Typical source documents |
|---------|-----------------|--------------------------|
| **Device description & intended use** | Clear statement of indications, user population, and environment of use. | Device master record, IFU draft. |
| **Substantial‑equivalence comparison** | Side‑by‑side table vs. predicate (design, performance, labeling). | Predicate 510(k) number, design specifications. |
| **Design verification & validation** | Test protocols + results showing compliance with design inputs/outcomes. | Bench testing reports, animal studies, usability tests. |
| **Risk management** | ISO 14971:2019 risk analysis, mitigation, and residual risk evaluation; risk control measures tied to design outputs. | Risk Management File (RMF). |
| **Clinical evidence** | Clinical data or literature supporting safety/effectiveness; equivalence justification if using predicate clinical data. | CE‑marked study reports, US clinical trial data, literature review. |
| **Software documentation** *(if software component)* | IEC 62304 lifecycle documentation, verification of algorithm changes, cybersecurity controls. | Software Development File (SDF), version control log. |
| **Labeling & IFU** | Labels, packaging, and user instructions that meet **21 CFR §801** labeling requirements. | Draft labels, IFU PDFs. |
| **Sterilization/biocompatibility** *(if applicable)* | ISO 10993‑1:2018 biocompatibility data; sterilization validation per USP/NF. | Biocompatibility test reports, sterilization cycle validation. |

---

### 4. Gaps Identified from Source (AI‑Response Lens)

| Deficiency noted in source | FDA‑equivalent evidence that is **likely missing** |
|----------------------------|----------------------------------------------------|
| **GSPR 입증 근거 부족** (EU General Safety & Performance Requirements) | Formal risk analysis per ISO 14971, with traceability to design controls (21 CFR §820.30). |
| **Clinical Evaluation 동등성 불충분** | Robust clinical equivalence data or a clear predicate‑based justification; possibly additional US‑centric clinical data. |
| **PMCF 계획 미비** (Post‑Market Clinical Follow‑up) | FDA does not require a PMCF plan, but it expects a **post‑market surveillance (PMS)** strategy under 21 CFR §822.30. Prepare a PMS plan that outlines adverse event monitoring and trending. |
| **위험관리파일 ISO 14971 부적합** | Updated risk management file with identified hazards, severity/likelihood assessments, mitigation verification, and residual‑risk justification. |
| **AI‑request sample answer framework (source link)** | A structured response template that directly maps each FDA AI question to the corresponding docket item (e.g., “Section 4 – Design Verification” → attach Report A). |

*Because the source contains no device‑specific identifiers, all gaps above are inferred from typical AI patterns.*

---

### 5. Risk Controls & Mitigation Plan
| Hazard Category | Control(s) Implemented (per ISO 14971) | Evidence to Provide |
|-----------------|----------------------------------------|---------------------|
| **Software algorithm drift** | Predetermined Change Control Plan (PCCP) – FDA Guidance Dec‑2024; version control, automated regression testing. | PCCP document, test logs. |
| **User misuse** | Human factors/usability engineering study per IEC 62366‑1:2020. | Usability report, user task analysis. |
| **Electrical safety (if device includes hardware)** | Compliance with IEC 60601‑1:2005+A1:2012+A2:2020; design verification of leakage current, protection circuits. | Test certificates, compliance statements. |
| **Biocompatibility** | ISO 10993‑1:2018 testing for all patient‑contacting materials. | Biocompatibility test reports. |
| **Data security (AI/ML component)** | Cybersecurity risk assessment, encryption, authentication per FDA’s “Cybersecurity in Medical Devices” guidance (2022). | Security architecture diagram, penetration test summary. |

---

### 6. Citations

**Framework references (no verification caveat needed)**
- 21 CFR §807.92 – Content and format of a 510(k) submission.  
- 21 CFR §820 – Quality System Regulation (QMSR).  
- 21 CFR §801 – Labeling requirements.  
- ISO 14971:2019 – Risk management for medical devices.  
- ISO 13485:2016 – Quality management systems.  
- IEC 62304:2006+A1:2015 – Software life‑cycle processes.  
- IEC 60601‑1:2005+A1:2012+A2:2020 – General safety requirements for electrical medical equipment.  

**Instance identifiers (none appear in the source)**
- No specific identifier found in source — verify separately.

---

### 7. Human‑Escalation Triggers
| Trigger | Action Required | Responsible Role |
|--------|------------------|-------------------|
| **AI request exceeds 180 calendar days for response** | Escalate to Senior Regulatory Manager; consider filing a supplemental 510(k) if new data are needed. | RA Lead. |
| **Missing risk‑management evidence (ISO 14971) that cannot be generated within the current timeline** | Pause submission, convene cross‑functional team (Engineering, QA, Clinical). Document justification for delay and seek senior approval before proceeding. | QA Manager. |
| **AI demands new clinical data not covered by predicate** | Initiate US‑centric clinical study plan; escalate to Clinical Affairs Director for budget/timeline approval. | Clinical Lead. |
| **Regulatory counsel needed for interpretation of ambiguous AI wording** | Forward AI letter to external counsel or in‑house legal for formal opinion before responding. | Regulatory Counsel. |
| **Significant change to device architecture (e.g., algorithm update) during review** | Evaluate whether a new 510(k) or a PCCP submission is required; involve Engineering Lead and submit a Change Control Package to FDA. | Engineering Director. |

---

### 8. Peer‑Review Prompt
> *Colleague, please challenge the assumptions above:*
> - *Is Class II the most appropriate classification given only the generic evidence gaps?*  
> - *Are there any device‑specific predicates we might have missed that would change the scope of clinical data required?*  
> - *Do you see any missing FDA guidance (e.g., “AI/ML SaMD Pre‑Market Guidance” Dec 2024) that should be referenced for our software risk controls?*  

Your input will ensure no jurisdictional or evidentiary blind spots remain before finalizing the AI response package.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> ① 510(k) 경로 근거 "21 CFR §807.92 (content requirements)" — §807.92는 Summary/Statement 조항, 내용 요건은 §807.87(5회차 재발) ② UDI "§830.10-§830.60" — 라벨 게재는 §801.20 등(재발, SOUL 오기 시딩) ③ product code "LLE/MDM" 미검증.

**Source Excerpts**

1. Chunk `1062884112493939033`

> ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합

2. Chunk `1076622801663602202`

> > 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: https://www.fda.gov/media/73507/download (FDA Guidance: FDA and Industry Actions on 510(k) Submissions, Oct 2022) | https://medicaldeviceacademy.com/additional-information-request/ | https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process | MDUFA V Commitment Letter https://www.fda.gov/media/158308/download # FDA Additional Information (AI) 대응 전략 및 샘플 답변 체계

### kb-eval-20261105-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "8475c6204b648c0c", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `8475c6204b648c0c`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/FDA_%EC%9E%84%EC%83%81%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%95%84%EC%9A%94%ED%8C%90%EB%8B%A8_%EA%B8%B0%EC%A4%80.md)
- Source hash: `36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `FDA_임상데이터_필요판단_기준.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Evidence‑Gap Assessment & Submission Strategy**

---

### 1. Device Overview (placeholder)  
*Note: Insert the device name, intended use, technology class (e.g., “software‑only image analysis”, “ultrasound probe”), and any known predicate information before finalizing this draft.*

---

### 2. Proposed Classification & Submission Route  

| Criterion | Assessment | Rationale |
|-----------|------------|----------|
| **Regulatory Class** | Likely **Class II** (if intended use aligns with existing imaging or diagnostic devices) – requires 510(k). | The source summary lists Class I·II as the default target for a 510(k) pathway. |
| **Submission Pathway** | **Premarket Notification (510(k))** – assuming an appropriate predicate exists. | Predicate requirement is mandatory for 510(k) (FD&C Act §510(k), 21 CFR 807). De Novo or PMA would be considered only if no suitable predicate can be identified or the device is novel/high‑risk. |
| **Alternative** | **De Novo** – if the device represents a new classification without an adequate predicate but is not high‑risk (Class III). | De Novo provides a pathway for “new” Class I/II devices when no predicate exists (FD&C Act §513(f)(2), 21 CFR 860). |
| **PMA** – Not indicated at this stage. | Required only for Class III devices; would demand full clinical data (FD&C Act §515, 21 CFR 814). |

*Recommendation:* Pursue a 510(k) submission unless a predicate cannot be located after the gap analysis (see Section 4).

---

### 3. Evidence Required for a 510(k) Submission  

| Evidence Category | Typical Content | Source‑based Requirement |
|-------------------|-----------------|---------------------------|
| **Device Description** | Full technical specifications, block diagram, software architecture (if applicable), labeling draft. | 21 CFR 807 – content of a 510(k). |
| **Predicate Comparison** | Side‑by‑side table addressing intended use, technological characteristics, performance testing outcomes. | Predicate is mandatory for 510(k) (source: Table under “Predicate 필요”). |
| **Non‑clinical Performance Testing** | Bench, benchtop, electromagnetic compatibility, software verification/validation (IEC 62304), risk analysis (ISO 14971). | Required unless waived; supported by the “조건부 (§3 참조)” note for clinical data. |
| **Clinical Data (if applicable)** | Limited clinical performance data to address any new indications or technological differences not covered by predicate testing. | Clinical data are *conditionally* required for 510(k) (“임상데이터 – 조건부 (§3 참조)”). |
| **Risk Management File** | ISO 14971‑based risk analysis, hazard mitigations, residual risk justification. | Implicit in §820 design controls & FDA expectations. |
| **Sterility / Biocompatibility (if applicable)** | ISO 10993‑1 testing package. | Required when the device contacts patients or sterile barrier is claimed. |
| **Software Documentation** *(if software)* | IEC 62304 plan, validation report, cybersecurity assessment per IEC 81001‑5‑1. | Aligns with FDA’s software guidance (not cited in source). |

---

### 4. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Evidence Needed |
|-----|----------------------|-----------------|
| **Predicate Device Identification** | Without a predicate the 510(k) cannot proceed; would trigger De Novo consideration. | Search FDA’s 510(k) database for devices with identical intended use and similar technology. |
| **Intended Use Statement** | Determines classification, labeling scope, and risk level. | Draft a clear, concise intended‑use description. |
| **Device Architecture Details** (hardware vs. software composition) | Affects need for software validation, cybersecurity controls, and possibly a “software as a medical device” (SaMD) approach. | Provide block diagrams, software description, and version control plan. |
| **Clinical Performance Justification** | Source notes clinical data are *conditionally* required; justification for waiving or limiting clinical data is needed. | Conduct a risk‑based assessment showing that bench testing sufficiently predicts clinical performance, or prepare limited clinical study protocol. |
| **Risk Management Documentation** | Required by 21 CFR 820 and ISO 14971. | Full risk analysis report with mitigation measures. |
| **Labeling Draft (including UDI)** | Must comply with 21 CFR 801 & 830. | Label text, symbols, and a plan to assign a UDI per Part 830 (§830.10 onward). |
| **Quality Management System (QMS) Compliance** | QMSR effective Feb 2026 (ISO 13485‑aligned). | Evidence of ISO 13485:2016–based QMS implementation (SOPs, internal audit reports). |

*All gaps above must be resolved before a definitive submission can be assembled.*

---

### 5. Risk Management & Controls  

1. **Risk Management Process** – Follow ISO 14971:2019 (risk analysis, evaluation, control, and post‑market surveillance).  
2. **Design Controls** – Implement 21 CFR 820 design‑control requirements (design inputs, outputs, verification, validation, transfer).  
3. **Software Lifecycle** – Apply IEC 62304:2006+A1:2015 for any software components; include a Predetermined Change Control Plan (PCCP) if future AI/ML updates are anticipated (FDA guidance Dec 2024).  
4. **Cybersecurity** – Align with IEC 81001‑5‑1:2021 and FDA’s “Postmarket Management of Cybersecurity” recommendations.  
5. **Human Factors / Usability** – Conduct usability testing per IEC 62366‑1:2015+A1:2020 to demonstrate safe use.  

---

### 6. Regulatory Citations  

| Item | Citation (Framework) |
|------|-----------------------|
| **510(k) legal basis** | FD&C Act §510(k); 21 CFR 807 |
| **De Novo legal basis** | FD&C Act §513(f)(2); 21 CFR 860 |
| **PMA legal basis** | FD&C Act §515; 21 CFR 814 |
| **Classification guidance** | FDA “Premarket Notification (510(k)) – Selecting and Preparing the Correct Submission” (source excerpt) |
| **Clinical data condition for 510(k)** | “임상데이터 – 조건부 (§3 참조)” – note: specific § reference not supplied in source (no specific identifier found — verify separately). |
| **eSTAR requirement** | eSTAR obligations start 2023‑10‑01 for 510(k) devices (source table). |
| **UDI regulation** | 21 CFR 830 (§830.10 onward). |
| **QMSR** | 21 CFR 820 (effective Feb 2026, ISO 13485‑aligned). |
| **ISO standards** | ISO 14971:2019; ISO 13485:2016; IEC 62304:2006+A1:2015; IEC 60601‑1:2005+A1:2012+A2:2020; IEC 62366‑1:2015+A1:2020; IEC 81001‑5‑1:2021; ISO 10993‑1:2018. |

*No device‑specific clearance numbers or exact regulatory article/section identifiers appeared in the source excerpts; therefore none are inserted here.*

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason to Escalate |
|--------|--------------------|
| **Missing Predicate** – No suitable cleared 510(k) found after exhaustive search. | Decision point: switch to De Novo or consider PMA if risk warrants. |
| **Clinical Data Requirement Unclear** – Risk analysis indicates gaps that cannot be resolved by bench testing alone. | Need senior clinical affairs input and possible IRB‑approved study plan. |
| **Risk Rating > Acceptable** – Residual risk remains high after mitigations. | Escalate to senior safety officer / Chief Medical Officer for risk acceptance decision. |
| **QMSR Gaps Identified** – Evidence of ISO 13485 compliance is incomplete or outdated. | Require Quality Assurance leadership to remediate before filing. |
| **UDI Assignment Issues** – No issuing agency identified or GUDID entry plan lacking. | Escalate to regulatory operations for UDI strategy. |
| **Significant Device Change Planned** – Anticipated AI/ML algorithm updates that would affect performance. | Initiate Predetermined Change Control Plan (PCCP) process with senior engineering lead. |
| **Regulatory Timeline Conflict** – Projected submission date exceeds FDA review target windows (90 days for 510(k)). | Notify project management to adjust schedule or allocate resources for expedited review. |

When any trigger is activated, the RA Lead should be notified in writing (e‑mail/issue tracker) and a decision memo drafted outlining options and resource implications.

---

### 8. Peer Review Prompt  

*“Please review the assumptions above, especially the classification determination and the conditional clinical data requirement. Confirm whether the identified gaps fully reflect what is needed for a complete 510(k) dossier, or if additional EU/MDR considerations have inadvertently been omitted given the US‑only focus.”*

--- 

**End of Draft**

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> UDI를 "§830.10 onward"로 인용 2회 — 라벨 게재 의무는 Part 801 Subpart B(§801.20~), Part 830은 시스템·발급기관·GUDID 체계. SOUL 오기 시딩 사례이나 응답 결함으로 감점.

**Source Excerpts**

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20261105-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "aba206c1afcc12ef", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A2_Form3514_템플릿.md", "source_hash": "f07d857ec6943c9b00d268d9d425dd1a73e7e898cad79b2fac12450b3beb67f7"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `aba206c1afcc12ef`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A2_Form3514_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/T-FDA510K-A2_Form3514_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `f07d857ec6943c9b00d268d9d425dd1a73e7e898cad79b2fac12450b3beb67f7`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `T-FDA510K-A2_Form3514_템플릿.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: --- doc-id: T-FDA510K-A2_Form3514_템플릿 title: FDA Form 3514 (CDRH Premarket Review Submission Cover Sheet) 작성 템플릿 type: Form version: v0.1 status: draft category: 01_법규_규제 purpose: FDA 510(k) RTA Checklist A.2 대응 — Form 3514 기재항목 골격, 제품별 실 데이터 작성 예정 applicable: [FDA 510(k), FDA QMSR] owner: RA 담당자 last-review: 2026-09-10 review-due: 2027-09-10 --- # T-FDA5...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Submission Evidence Gap Assessment**

---

### 1. Device Classification & Submission Route  
| Item | Determination | Basis / Citation |
|------|---------------|------------------|
| **Regulatory pathway** | Premarket Notification (510(k)) | 21 CFR 807.92 (substantial equivalence requirement) – *framework reference* |
| **Product Code / Class** | **Undetermined** – requires device description & intended use to assign a product code and class (e.g., Class II under 21 CFR 892 for imaging, or other appropriate panel). | No specific identifier found in source — verify separately |
| **Applicable FDA regulations** | • 21 CFR 807 – 510(k) submission <br>• 21 CFR 820 – Quality Management System Regulation (QMSR), effective Feb 2026 <br>• 21 CFR 830 – UDI requirements (label must bear a UDI) | *framework references* |

**Action:** Obtain the device’s intended use, indications, technology description, and functional claims to determine product code and classification.

---

### 2. Required Evidence for a Complete 510(k)

| Evidence Category | Typical Content | Regulatory Reference |
|-------------------|-----------------|----------------------|
| **Device Description & Intended Use** | Comprehensive narrative, labeling excerpts, drawings, block diagrams. | 21 CFR 807.92(a) |
| **Predicate Device(s)** | 510(k) number, name, FDA‑cleared status; comparison matrix (design, materials, performance). | 21 CFR 807.92(b) |
| **Performance Testing** | • Bench/bench‑top testing (functional, electrical safety per IEC 60601‑1) <br>• Biocompatibility (ISO 14971 risk analysis & ISO 10993‑1) <br>• Software validation (IEC 62304, IEC 62366‑1) <br>• Clinical data if required. | 21 CFR 820.30; ISO 14971:2019; IEC 62304 2006+A1:2015 |
| **Risk Management** | Full risk analysis file, mitigation measures, residual risk evaluation. | ISO 14971:2019 (risk management process) |
| **Labeling & IFU** | Labels, packaging artwork, Instructions for Use, UDI placement per 21 CFR 830.10‑830.60. | 21 CFR 801 (labeling); 21 CFR 830.10‑830.60 |
| **Sterilization Validation** *(if applicable)* | Sterility assurance level, validation protocol, package integrity. | 21 CFR 820.70 (production & process controls) |
| **Quality System Documentation** | • QMS certificate (ISO 13485:2016 alignment) <br>• Device Master Record, Device History Record, design history file, change‑control plan (Predetermined Change Control Plan – PCCP if AI/ML). | 21 CFR 820; FCC guidance on PCCP (Dec 2024) |
| **UDI & GUDID Submission** | UDI carrier, device identifier, entry into the Global Unique Device Identification Database. | 21 CFR 830.300‑830.360 |

---

### 3. Evidence Gaps – What Is Missing From the Current Source

| Gap | Why It Matters | Escalation Trigger |
|-----|----------------|--------------------|
| **Device‑specific information** (type, intended use, technology) | Needed to assign product code & class; without it, no clear submission pathway. | Immediate escalation to Product Development lead for provision of a device brief. |
| **Predicate identification** | Substantial equivalence cannot be claimed without a cleared comparator. | Escalate to senior RA if predicate search exceeds 5 business days with no result. |
| **Risk Management File (ISO 14971)** | Required for all Class II/III devices; informs biocompatibility & performance testing scope. | Escalate if risk analysis is incomplete after the initial draft review. |
| **Performance Test Plans & Results** | Bench and, where needed, clinical data must demonstrate safety/effectiveness. | Flag to Engineering lead; if missing >10 days from submission deadline, raise to RA Manager. |
| **Labeling/UDI Drafts** | FDA requires UDI on the label and entry into GUDID before market launch. | Escalate to Regulatory Affairs Manager when labeling package is not in draft form 14 days prior to filing. |
| **QMSR compliance evidence** (ISO 13485‑aligned SOPs, PCCP if AI/ML) | New QMS regulation (21 CFR 820) applies to all submissions after Feb 2026. | Escalate to Quality Assurance Director if QMS documentation absent at the 510(k) submission readiness review. |
| **Form 3514 completed** (official FDA cover sheet) | The source is a *template* only; the official FDA Form 3514 must be fully populated with accurate data. | Alert RA lead when final Form 3514 remains in draft status within 3 days of planned submission. |

---

### 4. Risk Controls to Address Identified Gaps

| Control | Description |
|----------|-------------|
| **Cross‑functional Gap‑Analysis Checklist** – map each 510(k) requirement to evidence status; update weekly. |
| **Predetermined Change Control Plan (PCCP)** – for any AI/ML components, pre‑define allowable algorithm updates and submit the PCCP with the 510(k). |
| **Document Management Workflow** – lock final versions of Form 3514, labeling, risk analysis, and test reports in the FDA submission repository; require dual sign‑off. |
| **Regulatory Review Gate** – conduct a pre‑submission RTA (Refuse‑to‑Accept) checklist review 30 days before filing; any “fail” automatically triggers escalation. |
| **UDI Synchronization Process** – ensure UDI assigned in the device master record matches GUDID entry; perform automated validation script. |

---

### 5. Citations

- **Framework references (no verification needed):** 21 CFR 807, 21 CFR 820, 21 CFR 830, ISO 14971:2019, ISO 13485:2016, IEC 62304 2006+A1:2015, IEC 60601‑1 2005+A1:2012+A2:2020, IEC 62366‑1 2015+A1:2020.
- **Instance identifiers:** *none found in source excerpts* – “no specific identifier found in source — verify separately”.

---

### 6. Human‑Escalation Triggers (Decision Tree)

| Condition | Escalation Recipient | Deadline After Detection |
|-----------|----------------------|--------------------------|
| No device description / intended use provided | Product Development Lead | Immediate (within 1 day) |
| Predicate not identified after 5 business days of search | Senior RA / Regulatory Affairs Manager | 5 days |
| Incomplete risk management file at RTA gate | Risk Management Lead | 2 days before RTA review |
| Missing performance test data >10 days from filing date | Engineering Lead | 10 days |
| Labeling/UDI draft not ready 14 days prior to submission | RA Manager | 14 days |
| QMSR evidence absent at final submission readiness check | QA Director | Immediate |
| Form 3514 still in draft within 3 days of planned filing | RA Lead | 3 days |

---

### 7. Peer‑Review Prompt

> **To a fellow RA colleague:** Please review the assumptions about classification (i.e., defaulting to Class II pending device details) and verify that all required evidence categories are complete for both hardware‑only and software‑enabled devices. Confirm whether any additional FDA guidance (e.g., recent AI/ML addendum, special controls memoranda) should be incorporated given our lack of specific device information.

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> ① "21 CFR 807.92 (substantial equivalence requirement)" 오인용(재발) ② "§807.92(a)/(b)" 하위조항을 Device Description/Predicate 섹션으로 매핑 — §807.92 하위항은 서식 요건, 내용 섹션 아님 ③ UDI 배치 "§830.10-830.60"(재발).

**Source Excerpts**

1. Chunk `1058200072933812620`

> --- doc-id: T-FDA510K-A2_Form3514_템플릿 title: FDA Form 3514 (CDRH Premarket Review Submission Cover Sheet) 작성 템플릿 type: Form version: v0.1 status: draft category: 01_법규_규제 purpose: FDA 510(k) RTA Checklist A.2 대응 — Form 3514 기재항목 골격, 제품별 실 데이터 작성 예정 applicable: [FDA 510(k), FDA QMSR] owner: RA 담당자 last-review: 2026-09-10 review-due: 2027-09-10 --- # T-FDA510K-A2 FDA Form 3514 작성 템플릿 (v0.1 — 골격) > **주의**: 본 문서는 FDA 공식 양식(Form 3514)의 **대체물이 아니다**. 실제 제출은 FDA 배포 최신 양식 원본(PDF)에 기재해야 하며, 본 문서는 사내 사전 준비용 기재항목 정리 골격이다. 제품 특정 정보는 **작성 예정**.

2. Chunk `279861482758419519`

> ## 관련 문서 | 문서 | 연계 내용 | |------|-----------| | 13_규제평가_체크리스트/FDA_510k_RTA.md | FDA-510K-A2 | | 01_법규_규제/03_미국_FDA/T-FDA510K-A1_Cover_Letter_템플릿.md | Cover Letter 기재정보와 정합 | | 01_법규_규제/03_미국_FDA/T-FDA510K-A5_Form3654_Standards_템플릿.md | 표준 적합성 목록 정합 |

### kb-eval-20261105-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "0b3e269c6984fbda", "source": "github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md", "source_hash": "0081e939c99bc98216ea8bbc10bd8fcf3f01739ef65674a0fd6b602825348c7d"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `0b3e269c6984fbda`
- Source: `github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/13_%EA%B7%9C%EC%A0%9C%ED%8F%89%EA%B0%80_%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8/FDA_510k_RTA.md)
- Source hash: `0081e939c99bc98216ea8bbc10bd8fcf3f01739ef65674a0fd6b602825348c7d`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `FDA_510k_RTA.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 2. Device Description & Indications ```yaml - id: FDA-510K-B1 source: FDA RTA Checklist Section B clause: B.1 requirement: Device Description — physical, technological characteristics, components, accessories severity: must evidence_type: technical_documentation applicable_keywords: [FDA 510, FDA QMSR] related_docs: [T-FDA510K-B1_Device_Description_템플릿...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Submission Gap Analysis**

---

### 1. Device Overview & Classification  

| Item | Detail |
|------|--------|
| **Device family** (inferred from checklist items C‑3 & C‑4) | X‑ray imaging system with integrated software (major LoC). |
| **Regulatory panel** | Imaging / radiology devices – 21 CFR Part 892. |
| **Class** | Class II (most X‑ray equipment is classified as Class II under Part 892). |
| **Relevant product code** | To be confirmed by predicate search; typical codes: **JYQ**, **LGU**, etc. (no specific identifier in source – verify separately). |
| **Intended use** | Must be defined per checklist item B‑2 (disease, patient population, clinical environment). |

---

### 2. Submission Route  

*Traditional 510(k) (Premarket Notification) under 21 CFR 807.*  
Because the device is a Class II imaging system with an existing predicate, a Traditional 510(k) is the fastest credible pathway. No De Novo or special/abbreviated route is indicated.

---

### 3. Evidence Requirements – Checklist Status  

| Section | Requirement (as listed in source) | Evidence Type Required | **Current status** (based on provided excerpts) |
|---------|-----------------------------------|------------------------|-------------------------------------------------|
| B‑1 | Device Description — physical, technological characteristics, components, accessories | Technical documentation (e.g., device description template) | **Present** – referenced template `T-FDA510K-B1_Device_Description_템플릿`. |
| B‑2 | Intended Use / Indications for Use — disease, population, environment | Technical documentation (intended‑use statement) | **Present** – referenced template `T-FDA510K-B2_Intended_Use_템플릿`. |
| C‑3 | Electrical safety – IEC 60601‑1, EMC IEC 60601‑1‑2 | Test report(s) | **Present** – test‑report placeholder indicated; actual reports not supplied in excerpt. |
| C‑4 | Software (Major LoC) – IEC 62304 + FDA software guidance + cybersecurity | Software documentation (SDLC artifacts, SBOM, cyber risk analysis) | **Present** – list of supporting docs (`IEC_62304_SW_수명주기`, `SOP-VAL-001`, `IEC_81001-5-1_FDA_Cybersecurity_SW보안`, `SOP-SBOM-001`). |
| **Missing / Not Evidenced in Source** | • Performance testing (image quality, dose metrics) <br>• EMC test report beyond IEC 60601‑1‑2 (e.g., IEC 61000‑4‑3/4‑6) <br>• Biocompatibility (ISO 10993‐1) if patient‑contacting accessories are present <br>• Human Factors / Usability validation (IEC 62366‑1) <br>• Risk Management File (ISO 14971:2019) – risk analysis, mitigations, residual risk evaluation <br>• Labeling and IFU content (21 CFR 801) <br>• QMSR compliance artifacts (Part 820) – SOPs, CAPA records, design controls | Various (test reports, validation protocols, risk management dossier, labeling specimens, QMS records). | **Absent** – no identifiers or documents cited in source; verify separately. |

---

### 4. Risk Controls & Management Gaps  

| Control Area | Required Basis (framework) | Gap Identified |
|--------------|----------------------------|----------------|
| **Electrical Safety** | IEC 60601‑1 (general requirements) & IEC 60601‑1‑2 (EMC). | Test report referenced but not attached; confirm compliance data. |
| **Software Lifecycle** | IEC 62304 + FDA Guidance for Software‑contained Devices (2024). | Documentation list present, but need evidence of verification/validation activities and a **Predetermined Change Control Plan (PCCP)** if future AI/ML updates are anticipated. |
| **Cybersecurity** | IEC 81001‑5‑1 (Health Software Cybersecurity) & FDA “Cybersecurity for Medical Devices” guidance (2022). | Threat model, vulnerability management plan, and PCCP not explicitly cited – must be supplied. |
| **Risk Management** | ISO 14971:2019 (risk analysis, evaluation, control). | No risk‑management file referenced; gap must be filled before submission. |
| **Usability/Human Factors** | IEC 62366‑1 (use error mitigation). | No usability validation evidence noted – required for imaging devices that affect diagnosis. |
| **Biocompatibility** (if applicable) | ISO 10993‑1:2018. | No biocompatibility data referenced; verify whether any patient‑contacting components exist. |
| **QMSR** | 21 CFR Part 820 (effective Feb 2026, ISO 13485‑aligned). | SOPs listed (e.g., `SOP-VAL-001`) but full QMS evidence (design history file, CAPA) not shown – confirm completeness. |

---

### 5. Citations  

| Item | Source citation |
|------|-----------------|
| Device description & intended use checklist items B‑1 / B‑2 | No specific identifier found in source — verify separately. |
| Electrical safety requirement (IEC 60601‑1, IEC 60601‑1‑2) | No specific identifier found in source — verify separately. |
| Software lifecycle & cybersecurity requirement (IEC 62304, FDA SW guidance, IEC 81001‑5‑1) | No specific identifier found in source — verify separately. |
| Classification panel | 21 CFR Part 892 (framework reference – factual). |
| QMSR regulation | 21 CFR Part 820 (framework reference – factual). |
| Risk management standard | ISO 14971:2019 (framework reference – factual). |
| Biocompatibility standard | ISO 10993‑1:2018 (framework reference – factual). |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Action Required | Escalation Level |
|--------------------|-----------------|------------------|
| **Absence of validated electrical safety test report** | Obtain full IEC 60601‑1/‑1‑2 test data; issue a risk‑assessment addendum. | RA Lead → Engineering Manager |
| **Software documentation incomplete (no verification/validation evidence or PCCP)** | Compile V&V reports, develop PCCP, and submit to FDA as Additional Information. | RA Lead → Software QA Director |
| **Missing cybersecurity threat model / mitigation plan** | Produce a formal cybersecurity case and integrate into risk file. | RA Lead → Cybersecurity Lead |
| **Risk Management File not compiled** | Assemble ISO 14971‑compliant risk analysis, control measures, residual‑risk justification. | RA Lead → Project Manager |
| **Biocompatibility data required for any patient‑contacting accessory** | Perform or procure ISO 10993 testing; include in submission. | RA Lead → Clinical/Materials Team |
| **Usability validation not performed** | Conduct IEC 62366‑1 usability study; prepare report. | RA Lead → Human Factors Engineer |
| **QMSR documentation (design controls, CAPA) insufficient for FDA audit** | Complete missing SOPs, DHR entries, and audit trail; update QMSR package. | RA Lead → Quality Systems Manager |
| **Any “must” severity items flagged by checklist remain unresolved after 10 business days** | Immediate pause of 510(k) filing; senior regulatory escalation to VP‑Regulatory Affairs. | Senior Management |

If any of the above triggers are observed, the RA team must log a deviation in the project risk register and notify the designated escalation contacts within **48 hours**.

---

### 7. Peer‑Review Prompt  

> **To: Regulatory Affairs Team (RA Peer Reviewer)**  
> Please review the assumptions made here regarding device classification (Class II under 21 CFR Part 892) and the inferred presence of X‑ray imaging functionality. Confirm whether additional predicate searches are needed or if a different product code may apply. Also assess whether the checklist coverage is complete—are there any FDA RTA items not captured in this analysis (e.g., labeling, environmental testing, post‑market surveillance planning)? Identify any jurisdiction‑specific gaps that might require separate documentation before final 510(k) assembly.

--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1030196510375040231`

> ## 2. Device Description & Indications ```yaml - id: FDA-510K-B1 source: FDA RTA Checklist Section B clause: B.1 requirement: Device Description — physical, technological characteristics, components, accessories severity: must evidence_type: technical_documentation applicable_keywords: [FDA 510, FDA QMSR] related_docs: [T-FDA510K-B1_Device_Description_템플릿] - id: FDA-510K-B2 source: FDA RTA Checklist Section B clause: B.2 requirement: Intended Use / Indications for Use — disease, population, environment severity: must evidence_type: technical_documentation applicable_keywords: [FDA 510] related_docs: [T-FDA510K-B2_Intended_Use_템플릿]

2. Chunk `1051800189340874179`

> - id: FDA-510K-C3 source: FDA RTA Checklist Section C clause: C.3 requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 severity: must evidence_type: test_report applicable_keywords: [IEC60601-1, IEC60601-2-54] related_docs: [X-ray_장비_안전성능_표준_매핑, IEC60601-2-54_형식시험_체크리스트] - id: FDA-510K-C4 source: FDA RTA Checklist Section C clause: C.4 requirement: Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity severity: must evidence_type: SW_documentation applicable_keywords: [IEC62304, FDA SBOM, IEC81001-5-1] related_docs: [IEC_62304_SW_수명주기, SOP-VAL-001, IEC_81001-5-1_FDA_Cybersecurity_SW보안, SOP-SBOM-001] ```

### kb-eval-20261105-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "ead008fe94c89758", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "5bf28fed005a56167085b57e9008118d40cccd9786a1fcf1f1195e3664f48bec"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `ead008fe94c89758`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_03_Performance_Testing_Bench_Test.md)
- Source hash: `5bf28fed005a56167085b57e9008118d40cccd9786a1fcf1f1195e3664f48bec`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_03_Performance_Testing_Bench_Test.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – “촬영실 GUI Software” (Image‑Processing & Display SaMD)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|---------------|
| **Product type** | Software as a Medical Device (SaMD) that performs image processing and display for radiology examinations. |
| **CFR classification** | **Class II** – 21 CFR §892.2050 (Image‑Processing Software). |
| **Applicable submission** | Traditional 510(k) Premarket Notification (21 CFR §807).  The device is not novel; a predicate can be identified among FDA‑cleared image‑processing software (e.g., “X” K####). <br> *No specific predicate identifier appears in the source – verify separately.* |
| **Regulatory timing** | Standard 90‑day review clock after acceptance of the complete 510(k) package (21 CFR §807.92). |

---

### 2. Core Submission Evidence Required  

| Evidence Category | Content Required | Source / Standard Reference |
|-------------------|------------------|------------------------------|
| **Device Description & Intended Use** | Clear statement of clinical purpose, user environment, and claimed functions (processing algorithms, display parameters, diagnostic aid vs. non‑diagnostic viewer). | 21 CFR §892.2050; FDA Guidance “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14) |
| **Predicate Comparison** | Table of side‑by‑side comparison with a legally marketed device: indications, technology, performance specs, labeling. | 21 CFR §807.92(a)(3); *no specific predicate identifier found in source – verify separately.* |
| **Software Documentation** | • Software Requirements Specification (SRS) <br> • Architecture & Design Description (including risk controls) <br> • Source code control plan (if requested) <br> • Verification & Validation Plan/Report (V&V) linking requirements → test cases → results. | IEC 62304:2006+A1:2015; FDA Guidance 2023‑06‑14 |
| **Risk Management File** | Risk analysis, risk evaluation, and risk control measures per ISO 14971:2019; classification of software safety class (IEC 62304) – likely **Class B** (risk of “moderate” harm). | ISO 14971:2019; IEC 62304 Table (Class B) |
| **Usability/ Human Factors** | Summative usability testing report demonstrating safe and effective UI operation for the intended user population. | IEC 62366‑1:2020 |
| **Cybersecurity** | Threat analysis, security architecture, mitigation plan, post‑market vulnerability management process. | FDA Guidance “Cybersecurity in Medical Devices” (2023‑09‑27) |
| **Performance Testing (V&V)** | • Functional testing of image processing algorithms (e.g., DICOM conformity, pixel fidelity). <br> • Accuracy/precision metrics (MTF, NPS, etc.) compared to predicate. | 21 CFR §892.2050; Table in source “Performance Testing” cites V&V (SRS→RTM→Test report) |
| **Labeling & UDI** | Device label, IFU, and UDI configuration per 21 CFR §830.10‑§830.60. | 21 CFR Part 830 |
| **Quality Management System** | Evidence of compliance with the new QMS Regulation (QMSR) – Part 820 (effective Feb 2026), ISO 13485:2016 alignment, including design controls and record retention. | 21 CFR §820; QMSR |
| **Software Lifecycle Processes** | Development plan, configuration management, problem‑resolution records, and predetermined change control plan if future AI/ML updates are anticipated. | IEC 62304; FDA Guidance “Predetermined Change Control Plan (PCCP)” (Dec 2024) – apply only if AI/ML is used. |

---

### 3. Gaps / Missing Information Identified in Source  

| Gap | Why It Matters | Suggested Remedy |
|-----|----------------|------------------|
| **Intended‑use statement** (exact clinical claim) | Determines predicate eligibility and risk class; drives labeling & testing scope. | Draft a concise Intended Use paragraph and attach to 510(k). |
| **Predicate device identification (regulatory number)** | Required for substantial equivalence matrix. | Perform market search for cleared SaMD with the same image‑processing function; capture K# and 510(k) number. |
| **Detailed UI mock‑ups & labeling samples** | Needed for usability, labeling, and FDA review of user interface. | Provide screenshots, IFU draft, and label artwork. |
| **Cybersecurity threat model** (specific hazards) | FDA now expects a documented security risk analysis. | Conduct a formal threat assessment (e.g., STRIDE) and include in submission. |
| **QMSR compliance evidence** (certificate, SOP list, design‑control records) | QMSR is mandatory for all Class II submissions post‑Feb 2026. | Compile ISO 13485:2016 certificate, updated SOPs (e.g., SOP‑RA‑002), and design‑control files. |
| **Usability engineering plan & test results** | Required for software that influences clinical interpretation. | Conduct formative & summative usability studies per IEC 62366‑1; upload report. |
| **Software safety class justification** (IEC 62304) | Determines required validation depth. | Map risk scenarios to Class A/B/C; include justification in the risk file. |
| **Post‑market surveillance plan** (e.g., MDR equivalent) | FDA expects a PMS/complaint handling system under Part 820. | Outline complaint handling, adverse event reporting (21 CFR §803), and corrective actions. |

---

### 4. Key Risk Controls to Include  

1. **Software safety class B controls (IEC 62304)** – modular design, graceful degradation, error‑handling routines.  
2. **Risk mitigation per ISO 14971** – e.g., limit image alteration to diagnostically acceptable ranges; provide “reset” and “undo” functions.  
3. **Cybersecurity safeguards** – encrypted data storage/transmission, authentication, regular firmware updates, vulnerability monitoring (as per FDA 2023‑09‑27 guidance).  
4. **Usability safeguards** – clear user instructions, on‑screen warnings for out‑of‑range parameters, lockout after repeated errors.  
5. **Change management** – Predetermined Change Control Plan (PCCP) if future algorithm updates are anticipated; otherwise, established configuration control per IEC 62304.  

---

### 5. Human‑Escalation Triggers (When to Involve Senior RA / Regulatory Leadership)

| Trigger | Action Required |
|---------|-----------------|
| **Unresolved intended‑use ambiguity** | Pause submission drafting; senior RA reviews clinical claim and predicate search. |
| **No viable FDA‑cleared predicate identified** | Consider De Novo pathway or request a Pre‑Submission (Q‑Submit) meeting with FDA. |
| **Incomplete QMSR evidence** | Escalate to Quality Director for ISO 13485 audit documentation before filing. |
| **Significant cybersecurity findings** (e.g., unmitigated high‑impact vulnerability) | Halt 510(k) package; engage Cybersecurity Lead and possibly request FDA early interaction. |
| **Risk file shows Class C software (high severity)** | Reassess classification – may trigger PMA; senior decision required. |
| **FDA Additional Information (AI) request exceeds 30‑day response window** | Senior RA coordinates rapid response team; consider filing a formal extension if needed. |
| **Discrepancy between performance test results and predicate claims** | Pause submission, repeat testing or adjust claim; senior technical review mandatory. |

---

### 6. Summary Judgment  

The 촬영실 GUI Software is a **Class II SaMD** falling under **21 CFR §892.2050**. The appropriate regulatory route is a **Traditional 510(k) Premarket Notification** supported by:

* Full software documentation (SRS, design, V&V).  
* ISO 14971 risk management file and IEC 62304 safety‑class justification (expected Class B).  
* Usability engineering report (IEC 62366‑1).  
* Cybersecurity threat analysis per FDA 2023 guidance.  
* QMSR compliance evidence (Part 820).  

Key gaps—intended use, predicate device identification, UI/labeling artifacts, detailed cybersecurity plan, and full QMSR documentation—must be resolved before submission.  

**Human‑escalation points** are listed above; any of these triggers should prompt senior RA sign‑off or an FDA pre‑submission interaction.

---

### 7. Peer Review Prompt  

*Colleague, please examine the following:*  
1. **Predicate selection assumptions** – have we identified all feasible cleared image‑processing SaMDs?  
2. **Scope of performance testing** – does the V&V plan sufficiently address algorithm accuracy relative to the predicate?  
3. **Jurisdiction alignment** – are we missing any UDI or labeling nuances specific to the new QMSR (Part 820) that could affect acceptance?  
4. **Risk classification** – does the risk analysis conclusively support a Class B designation, or should we consider re‑classification?  

Your critique will ensure completeness and avoid FDA reviewer objections.

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> ① "90-day review clock (21 CFR §807.92)" — §807.92는 심사기간 조항이 아님 ② "§807.92(a)(3)" predicate 비교 근거 오인용 ③ UDI "§830.10-§830.60"(재발).

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `133014538346095718`

> ## 4. 3개 제품 Performance Testing 비교 요약 | 항목 | X-ray Detector | Handheld X-ray Source | 촬영실 GUI SW | |------|---------------|----------------------|--------------| | 핵심 규정 | 21 CFR 892.1680 + 1020.30 | 21 CFR 892.1720 + 1020.30 | 21 CFR 892.2050 + SW guidance | | 핵심 표준 | IEC 62220-1-1, IEC 60601-2-54 | IEC 60601-2-28, IEC 60601-1 | IEC 62304, IEC 62366-1 | | 핵심 시험 | DQE, MTF, NPS, Dose linearity | Emission, HVL, Reproducibility, Thermal | V&V (SRS→RTM→Test report) | | 예상 소요 | 6~8주 | 4~6주 | 8~12주 | | 예상 비용 (외부 포함) | $15K~$40K | $20K~$35K | $25K~$50K | | MFDS 공용 여부 | 대부분 공용 가능 | 대부분 공용 가능 | 공용 가능 (번역 필요) | | MDR 공용 여부 | 공용 가능 (IEC 표준 동일) | 공용...

## ra_eu

### kb-eval-20261105-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "82a6ad09db2159bf", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `82a6ad09db2159bf`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDCG_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/Clinical_Evaluation_MDR_%EB%8F%99%EB%93%B1%EC%84%B1_%EC%B6%A9%EB%B6%84%EC%84%B1_%EA%B8%B0%EC%A4%80.md)
- Source hash: `c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR, MDCG

**Source Summary**

- 문서 요약: `Clinical_Evaluation_MDR_동등성_충분성_기준.md`는 EU MDR clinical evaluation, CER/CER plan, equivalence 또는 clinical data sufficiency 관련 문서입니다.
- 현재 excerpt 핵심: ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis (MDR)**  

*Prepared for internal use by the EU Regulatory Affairs team.  All references follow the citation rules in the brief.*  


---

### 1. Device Synopsis (placeholder)

| Item | Description |
|------|-------------|
| **Intended purpose** | *[Insert brief description of the medical device, indication and target patient group]* |
| **Target user**      | Professional health‑care professional (HCP) or lay person – to be confirmed. |
| **Anatomical site / physiological system** | *[e.g., “cardiovascular system – peripheral veins”]* |
| **Technology class** | To be derived from the classification rules (see §2). |

> **Note:** The draft assumes that a clinical‑equivalence route is being considered; therefore the analysis focuses on the MDR equivalence and sufficient‑clinical‑evidence criteria.

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Decision point | Reference |
|------|----------------|-----------|
| **2.1 Identify applicable rule** | Determine whether the device is active, invasive, measuring or otherwise covered by a specific rule in Annex VIII (e.g., Rule 9, 10, 11, 17). | *Annex VIII – Classification rules* |
| **2.2 Assign Class** | Apply the selected rule: <br>‑ Rule 9 → Class IIa/IIb (therapeutic active) <br>‑ Rule 10 → Class IIa/IIb (diagnostic active) <br>‑ Rule 11 → Class IIa, IIb or III (software) <br>‑ Rule 17 → Class IIa (radiographic image recording). | *Annex VIII – Rule numbers* |
| **2.3 Conformity‑assessment route** | Once the class is known, select the route dictated by Art. 52: <br>‑ Class I → self‑declaration (Art. 52 (7)) <br>‑ Class Is/Im/Ir → Annex IX Chapters I & III or Annex XI Part A (limited NB involvement) <br>‑ Class IIa → Art. 52 (6): Annex IX + technical‑documentation assessment of a representative device, **or** Annex II & III + Annex XI §10/§18 <br>‑ Class IIb → Art. 52 (4): Annex IX + representative‑device assessment **or** Annex X + Annex XI <br>‑ Class III → Art. 52 (3): Annex IX (full) **or** Annex X + Annex XI | *Article 52 – Class → route matrix* |

**Action required:** Confirm the exact rule and class by completing the “Device‑Specific Classification Worksheet” (internal).  

---

### 3. Clinical‑Evaluation Evidence Required under MDR  

| Requirement | What must be provided | MDR citation |
|-------------|----------------------|--------------|
| **Clinical Evaluation Report (CER)** – complete, up‑to‑date and kept current under Art. 61 | • Systematic literature review <br>• Clinical data from the device itself (if available) <br>• Data from equivalent devices meeting equivalence criteria | Annex XIV Part A; **Art. 61** |
| **Equivalence justification** – must satisfy all MDR‑specific items (Table 2 in source) | • Same clinical condition and intended purpose (including severity & stage) <br>• Same anatomical site (“same” body part) <br>• Similar patient population (age, anatomy, physiology) <br>• **Same user type** – HCP vs. lay‑person distinction is *new* under MDR (source [1]) <br>• Comparable core clinical performance relative to intended purpose | MDCG 2020‑5 (Equivalence); source [1] |
| **Sufficient Clinical Evidence** – evidence that the benefit–risk conclusion is robust | • Clinical data from post‑market surveillance, registries or studies that cover the device’s intended use <br>• If reliance on equivalence, the equivalent device(s) must have been placed on the EU market **after 20 May 2021** (unless an exemption under Art. 61(4‑6) applies) | MDCG 2020‑6 (Sufficient Clinical Evidence); **Art. 61(4‑6)** |
| **Exemption evidence (if claimed)** – Art. 61(4‑6) allows limited equivalence when: <br>1️⃣ No reasonable alternative, 2️⃣ Device is low risk, 3️⃣ Clinical data are unavailable, etc. | • Detailed justification and supporting literature showing that the exemption criteria are met | MDCG 2023‑7 (Art. 61(4‑6) exemptions) |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** – required when CER relies on equivalence or for Class IIa/IIb/III | • Planned PMCF activities, endpoints, sample size, timeline <br>• Subsequent PMCF evaluation report (Annex XIV Part B) | Annex XIV Part B |
| **State‑of‑the‑Art (SOTA) review** – must cover the latest scientific evidence up to the date of submission | • Literature search covering at least the past 5 years, unless justified otherwise | MDCG 2024‑3 (CER Content) |

> **Key gap identified in source [1]:** The MDR adds *“same user type”* as an equivalence criterion. If the device is intended for lay‑person use while the comparator was used by HCPs (or vice‑versa), equivalence cannot be claimed.

---

### 4. Gap Analysis – What Is Missing from the Current Dossier  

| Area | Evidentiary gap | Impact on MDR compliance |
|------|-----------------|--------------------------|
| **User‑type equivalence** | No documented analysis of whether the comparator device was used by the same user category as the target device (HCP vs. lay). | Blocks acceptance of equivalence under MDCG 2020‑5; may require own clinical data or an alternative equivalent device. |
| **Clinical performance comparability** | Only high‑level description of intended purpose; lacks quantitative endpoint comparison (e.g., sensitivity, specificity, adverse‑event rates). | Prevents demonstration of “similar core clinical performance” → CER conclusion cannot be supported. |
| **Recent literature** | The latest systematic review stops at 2019; no data covering advances after the MDR entry‑into‑force (May 2021). | Insufficient SOTA evidence; may lead to a request for additional post‑market data or new clinical investigation. |
| **Exemption justification** | No Art. 61(4‑6) exemption analysis present. | If equivalence is unfeasible, the dossier must contain a justified exemption; omission will be flagged by the NB. |
| **PMCF planning** | PMCF plan drafted but lacks specifics on sample size calculation and follow‑up duration for the intended indication. | Annex XIV Part B requirement not met → NB may request a revised PMCF plan before CE marking can be issued. |
| **Risk‑management linkage** | Risk Management File (RMF) exists, but the link between identified use‑error risks (GSPR §5) and the user‑type gap is not demonstrated. | Incomplete compliance with GSPR §3–§8; may trigger a finding during NB audit. |

---

### 5. Required Risk Controls & Documentation  

| Control | Why required (MDR reference) |
|---------|------------------------------|
| **Risk Management System** – updated RMF reflecting the user‑type analysis and any new use‑error scenarios. | GSPR §3 (risk management system) – Annex I Chapter I §§1‑9; specifically §5 (use‑error risks). |
| **Usability Engineering** – per IEC 62366‑1, to demonstrate that the device can be safely used by the intended user group. | Supports compliance with GSPR §22 (lay‑person use) and provides evidence for equivalence of user type. |
| **Labeling & IFU review** – ensure that instructions match the identified user category; include any training requirements if HCP‑only. | GSPR §23 (label & information supplied). |
| **Post‑Market Surveillance (PMS) plan** – updated to capture data on user‑type specific incidents and performance trends. | Art. 84 (PMS plan) + Art. 83 (PMS system). |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III, schedule at least every two years (Art. 86). | Provides ongoing benefit‑risk assessment; must incorporate data from the PMCF activities. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Recommended action |
|---------|--------------------|
| **Unresolved user‑type equivalence** | Escalate to senior Clinical Evaluation Lead for a decision on whether to conduct a dedicated clinical investigation or identify an alternative comparator. |
| **Insufficient recent literature (post‑2021)** | Assign a literature‑search specialist to update the SOTA review; report status to the Project Manager within 5 working days. |
| **Missing Art. 61(4‑6) exemption justification** | Prompt the Regulatory Manager to decide on pursuing an exemption claim; if negative, initiate clinical data collection plan. |
| **PMCF plan lacking quantitative details** | Forward to the Clinical Development Team for redesign of PMCF protocol; set a deadline of 10 working days. |
| **RMF‑CER linkage not documented** | Request Risk Management Owner to produce a cross‑reference matrix (risk ↔ clinical evidence) and submit within 7 days. |
| **NB audit observation on any of the above** | Immediate corrective‑and‑preventive action (CAPA) drafting; involve Quality Manager for approval before next audit cycle. |

---

### 7. Summary Judgment  

*Based on the current documentation, the device’s classification can be assigned once its active/diagnostic/measuring nature is clarified (Annex VIII). The likely conformity‑assessment route will be Annex IX (or Annex X + XI for Class IIb/III) as dictated by Art. 52.*

*Critical gaps that prevent a complete MDR‑compliant Clinical Evaluation are the lack of evidence on **same user type**, inadequate recent clinical performance data, and an absent exemption justification under Art. 61(4‑6). These must be resolved before the Notified Body can accept the CER.*

---

### 8. Peer‑Review Prompt  

> **@RA‑Peer:** Please review the assumptions made regarding (a) the classification rule selection without a concrete device description, (b) the completeness of the equivalence criteria list derived from source [1], and (c) the applicability of the cited MDCG guidances to a non‑implantable Class IIa device. Highlight any jurisdiction‑specific gaps you see (e.g., MFDS reference), and suggest additional evidence types that may satisfy the MDR's “sufficient clinical evidence” requirement.

--- 

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

1. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

2. Chunk `1090731331984830062`

> > 최종 갱신: 2026-05-18 (자동보강 #52) > 근거: MDR Regulation (EU) 2017/745 Article 61 & Annex XIV | MDCG 2020-5 (Equivalence, Apr 2020) | MDCG 2020-6 (Sufficient Clinical Evidence, Apr 2020) | MDCG 2023-7 (Article 61(4)-(6) Exemptions, Dec 2023) | MDCG 2024-3 (CER Content) | FDA 510(k) Program Guidance (Jul 2014) | FDA Best Practices for Predicate Device Selection (Oct 2023 Draft) | MFDS 의료기기 허가·신고·심사 등에 관한 규정 (고시 제2024-88호) # Clinical Evaluation (MDR) 심화 — 동등성·충분성 기준

### kb-eval-20261105-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "f9db86b36dd3889d", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f9db86b36dd3889d`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Classification & Submission‑Route Gap Analysis  
(standard diagnostic radiology device emitting ionising radiation)**  

---

### 1. Device Overview (derived from source)

| Item | Description |
|------|-------------|
| **Intended purpose** | Standard diagnostic radiology (e.g., projection X‑ray imaging) |
| **Key performance claim** | Detective Quantum Efficiency (DQE) ≥ 65 % (IEC 62220‑1‑1) – see Test Report TR‑2024‑015 |
| **Clinical evidence provided** | Revised Clinical Evaluation Report (CER) Rev. 3 attached as Annex A (clinical equivalence argument) |

*No further device‑specific data (e.g., model name, software version, labeling text) are present in the excerpt.*  

---

### 2. Classification

| Step | Reference | Determination |
|------|-----------|---------------|
| **Rule applied** | MDR Annex VIII **Rule 10** – “Active devices for diagnosis and monitoring; devices that emit ionising radiation for diagnostic radiology” | → **Class IIb** (Rule 10, ionising‑radiation sub‑rule) |
| **Regulatory citation** | *MDR* Annex VIII Rule 10 (active diagnostic X‑ray equipment) | **Class IIb** |

---

### 3. Conformity‑Assessment Route  

| Class | Art. 52 paragraph | Available route(s) | NB involvement |
|-------|-------------------|--------------------|---------------|
| IIb   | **Art. 52(4)** – “Annex IX (full QMS + technical‑documentation assessment) or Annex X + Annex XI” | • **Annex IX** (QMS + technical documentation assessment)  <br>• **Annex X** (EU type‑examination) + **Annex XI** (production conformity verification) | Yes – NB review required for either route |

*Reference: MDR Art. 52(4); Annex IX, Annex X & Annex XI.*

---

### 4. Evidence Required for a Complete Submission  

| Requirement | Where it belongs in the Technical Documentation (Annex II §6.1) | Regulatory basis |
|-------------|---------------------------------------------------------------|-------------------|
| **Clinical Evaluation Report (CER)** – up‑to‑date, covering clinical equivalence, benefit–risk analysis, and post‑market data. | Annex II §6.1; **Annex XIV Part A** – kept current under **Art. 61** | MDR Annex XIV Part A |
| **Test Report for DQE** (TR‑2024‑015) showing DQE ≥ 65 % across the declared operating range, plus traceability to IEC 62220‑1‑1. | Annex II §6.1 – “Performance testing” | IEC 62220‑1‑1 (2021) |
| **Risk Management File** (ISO 14971:2019) addressing ionising‑radiation hazards, shielding, interlocks, dose monitoring, and software risk if applicable. | Annex I §§3–8; Annex II §4 (risk management) | MDR Annex I §3 (RMF); ISO 14971 2019 |
| **Compliance with GSPR** – especially §16 (radiation protection), §17 (software, if any), §18 (active devices). | Annex I §§16‑18 | MDR Annex I §16‑18 |
| **Applicable Harmonised Standards** – e.g., IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy), IEC 60601‑2‑28 (X‑ray tube assemblies). | Annex II §5 (verification & validation) | MDCG guidance; standards listed in the MDR “harmonised standards” list |
| **Post‑Market Surveillance (PMS) Plan** – per Art. 84, including a PSUR (Class IIb) updated at least every two years (Art. 86(1)/(2)). | Annex III (PMS technical documentation) | Art. 84; Art. 86 |
| **EU Declaration of Conformity** – content per Annex IV, signed by the manufacturer. | Annex IV (DoC) | **Art. 19** |
| **Labeling & IFU** – complying with Annex I §23 (information supplied). | Annex I §23 | MDR Annex I §23 |
| **Summary of Safety and Clinical Performance (SSCP)** – *not required* for Class IIb (only for Class III/implantables). | N/A | — |

---

### 5. Gaps Identified from the Deficiency Letter Context  

The source only mentions a “Deficiency Letter” definition; no specific gaps are quoted. Nevertheless, typical NB comments for a Class IIb radiology device include:

| Expected evidence | Likely missing / unclear (based on common deficiencies) |
|-------------------|----------------------------------------------------------|
| **Full traceability of the clinical equivalence claim** – identity of the predicate/comparator device, patient population & study design. | No comparator listed; only DQE threshold quoted. |
| **Complete test report package** – raw data, measurement uncertainties, reproducibility across all clinically relevant exposure parameters. | Only a single test‑report reference (TR‑2024‑015) is cited. |
| **Risk analysis of radiation dose to patients & staff** – justification of shielding, interlock logic, ALARA compliance. | No explicit risk‑control evidence mentioned. |
| **Verification that the device meets IEC 60601‑2‑54 / 60601‑2‑28** – conformity statements or test certificates. | Not referenced in excerpt. |
| **Software documentation (if applicable)** – IEC 62304 lifecycle, verification & validation reports. | No software references; if software is present, evidence missing. |
| **PMS plan and PSUR schedule** – evidence that a PMS system per Art. 83/84 is established. | Not mentioned. |
| **Labeling & IFU compliance check** – QR codes, language requirements for EU markets. | No labeling details provided. |

*These are inferred gaps; the actual NB deficiency letter should be consulted to confirm.*  

---

### 6. Required Risk Controls (aligned with GSPR)

1. **Radiation protection (§16)**  
   * Shielding design validated against IEC 60601‑2‑54.  
   * Dose‑monitoring and automatic exposure control (AEC) implemented.  

2. **Active device safety (§18)**  
   * Interlock circuits preventing accidental emission.  
   * Battery/ power‑supply fault detection.  

3. **Software risk (if applicable, §17)**  
   * IEC 62304‑compliant development lifecycle.  
   * Usability engineering per IEC 62366‑1 to mitigate use‑error.  

4. **Residual risk evaluation (§8 of Annex I)** – documented in the RMF, with a benefit–risk conclusion incorporated into the CER (Art. 61).  

5. **Transport & storage (§7)** – validated packaging to prevent damage to X‑ray tube and detectors.

---

### 7. Action Items & Human‑Escalation Triggers  

| Trigger | Action | Owner | Deadline |
|--------|--------|-------|----------|
| **Missing comparator details for clinical equivalence** | Provide full specification of the predicate device, published literature supporting DQE threshold, and any clinical study data. | Clinical Evidence Lead | 5 BD |
| **Insufficient radiation‑safety test data** | Submit additional IEC 60601‑2‑54 conformity certificates & measurement uncertainty analysis. | Technical Validation Engineer | 7 BD |
| **No documented PMS system** | Draft PMS plan (Art. 84) and schedule PSUR (Art. 86). | Post‑Market Surveillance Manager | 10 BD |
| **Absence of software lifecycle evidence** (if software present) | Compile IEC 62304 compliance dossier, verification/validation reports. | Software Development Lead | 8 BD |
| **Deficiency Letter not addressed within the above timeframe** | Escalate to Regulatory Affairs Director and schedule an urgent NB‑consultation meeting. | Senior RA Manager | Immediate after deadline |
| **Any new NB comment that adds further gaps** | Open a Change Request, update Technical Documentation (Annex II §6.1) and re‑submit to the Notified Body. | QA/Document Control | As received |

*Escalation is triggered when any of the above actions are not completed by the stated deadline or when the NB issues a second deficiency letter.*

---

### 8. Summary Judgment  

- **Classification:** Class IIb (MDR Annex VIII Rule 10).  
- **Conformity‑assessment route:** Art. 52(4) – either **Annex IX** (full QMS & technical‑doc assessment) *or* **Annex X + XI** (type‑examination + production verification). NB involvement mandatory.  
- **Core evidence missing/unclear:** detailed comparator data for clinical equivalence, full radiation‑safety test package, confirmed harmonised‑standard conformity, PMS system, and (if applicable) software lifecycle documentation.  
- **Risk controls:** must satisfy GSPR §§16–18 and be documented in the RMF (ISO 14971:2019).  

All identified gaps should be addressed before the next submission to the Notified Body; any delay beyond the deadlines above must be escalated to senior regulatory leadership.

---

### 9. Peer‑Review Prompt  

> *Colleague, please review this draft and challenge the following:*  
> - Are the inferred gaps realistic given the limited source excerpts?  
> - Is the chosen classification (Rule 10 → Class IIb) appropriate for a device defined only by “standard diagnostic radiology”?  
> - Have we omitted any MDR requirements specific to ionising‑radiation devices that could affect the evidence package?  

Your feedback will help ensure completeness before we respond to the NB’s deficiency letter.

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

### kb-eval-20261105-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "23700f4249b91f31", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `23700f4249b91f31`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDCG_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/MDCG_2020-5-6-7-8_%EC%9E%84%EC%83%81%ED%8F%89%EA%B0%80_PMCF_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4_%EC%9A%94%EC%95%BD.md)
- Source hash: `a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR, MDCG

**Source Summary**

- 문서 요약: `MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md`는 `MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ``` ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & Submission Planning**

---

### 1. Device Classification & Conformity‑Assessment Route  
| Item | Current Status | Required Evidence / Action |
|------|----------------|----------------------------|
| **Intended medical purpose, target population, user type, and application site** | Not disclosed in the source material (only generic headings appear) | – Obtain a clear, manufacturer‑written Intended Use statement that defines: <br> · Application site (e.g., “cardiovascular system”) <br> · Target patient group (age, disease state, etc.) <br> · User category (health‑care professional, lay user) <br> · Core performance claims. |
| **Classification rule** | Cannot be applied without the above purpose description. | – Map the intended use to the appropriate Annex VIII rule (e.g., Rule 9, 10, 11, 17 for active or software devices). <br> · If the device is active therapeutic → Rule 9 (IIa/IIb). <br> · If it is diagnostic‑software → Rule 11 (IIa/IIb/III). |
| **Resulting class** | Undetermined. | – Once the rule is identified, determine the class and then the conformity‑assessment route per Art. 52: <br> · Class I – self‑declaration (Art. 52(7)). <br> · Class IIa/IIb – Annex IX (full QMS + technical‑doc assessment) or Annex X + XI (type‑examination & production verification). <br> · Class III – Annex IX or Annex X + XI. |

**Human‑Escalation Trigger 1:** *If the manufacturer cannot supply a definitive intended‑use statement within 10 working days, the classification step must be paused and senior RA counsel engaged.*

---

### 2. Required Clinical Evidence (MDR § 61 & Annex XIV)

| Requirement | Current Gap | Action Needed |
|-------------|------------|---------------|
| **Clinical Evaluation Report (CER)** – Annex XIV Part A, kept current under Art. 61. | No CER presented; the source only lists “clinical‑relevance absent”. | • Develop a full CER that includes: <br> – State‑of‑the‑art (SOTA) literature review <br> – Clinical data from own investigations or equivalent devices <br> – Benefit‑risk analysis linked to the RMF. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** – Annex XIV Part B. | Not provided; only a “PMCF Evaluation Report” template is shown. | • Create a PMCF plan that details: <br> – Objectives, scope, and methodology <br> – Schedule of data collection <br> – Criteria for success/failure <br> – Relation to remaining uncertainties from the CER. |
| **PMCF Evaluation Report** – mandatory sections listed in source excerpt 2 (section 5.2). | Sections A‑G are identified, but no content available. | Populate each section as follows: <br> A – Manufacturer contact details (per source). <br> B – Updated device description if any change occurred; otherwise reference the original plan. <br> C – Results of PMCF activities (including positive and negative findings, with justification for any deviations). <br> D – Evaluation outcome of clinical data from equivalent/similar devices. <br> E – Impact on technical documentation – specify changes required in CER, Risk Management File, and Summary of Safety & Clinical Performance (SSCP) where applicable. <br> F – List applied common specifications (CS), harmonised standards, or MDCG guidance used. <br> G – Overall conclusion – assess whether PMCF objectives were met and identify any preventive or corrective actions needed. |
| **Summary of Safety & Clinical Performance (SSCP)** – Art. 32 (for Class III/implantable). | Not applicable unless the device falls into those categories, which is still unknown. | If classifies as III or implantable, produce an SSCP per Art. 32. |

**Human‑Escalation Trigger 2:** *If any of the PMCF sections A‑G cannot be completed because source data are missing (e.g., no equivalent‑device clinical data), the RA lead must request a supplemental clinical study plan from development within 15 working days.*

---

### 3. Risk Management & Safety Controls  

| GSPR Reference | Gap Identified | Required Evidence / Action |
|----------------|----------------|----------------------------|
| **Annex I §3 – Risk‑management system** (ISO 14971:2019) | No RMF cited; clinical evidence gaps imply unresolved residual risks. | • Compile a complete Risk Management File that documents:<br> – Hazard identification, risk analysis, and evaluation of residual risk.<br> – Linkage between identified clinical uncertainties and risk controls (e.g., labeling, training). |
| **Annex I §4 – Risk‑control measures** | Not addressed. | • Define specific control measures that mitigate risks uncovered by the missing clinical data (e.g., usage restrictions, mandatory clinician supervision). |
| **Annex I §5 – Use‑error risks** | No usability assessment mentioned. | • Conduct a usability engineering study per IEC 62366-1:2020 to evaluate potential use errors, especially if the device is intended for lay users (§22). |
| **Annex I §§16‑18 – Radiation / Active devices** (if applicable) | Unknown; no information on whether the device emits ionising radiation or is active. | • If the device falls under any of these sections, perform conformity assessment against the relevant IEC standards (e.g., IEC 60601‑2‑54 for X‑ray equipment). |

**Human‑Escalation Trigger 3:** *Any residual risk that cannot be justified by clinical evidence must be escalated to senior management and possibly to the Notified Body before submission.*

---

### 4. Documentation Checklist for NB Submission  

| Annex / Article | Item Required | Current Availability |
|-----------------|---------------|----------------------|
| **Annex II §6.1** – Clinical evaluation & PMCF data | CER, PMCF plan, PMCF Evaluation Report (sections A‑G) | Missing (only template shown). |
| **Annex IV** – EU Declaration of Conformity (DoC) | Manufacturer details, device identification, conformity route, etc. | Not yet drafted. |
| **Annex III** – PMS technical documentation (PMS plan Art. 84, PMS report Art. 85/86) | PMS system description, periodic safety update reports. | Not present. |
| **Art. 83–86** – Post‑market surveillance & Periodic Safety Update Report (PSUR) | PSUR schedule (Class IIa/IIb → every 2 years; Class III → annually). | Schedule not defined. |
| **Annex I §§10‑22** – Design & manufacture documentation | Manufacturing processes, verification & validation records. | Not addressed in source. |

**Human‑Escalation Trigger 4:** *If any of the above items cannot be supplied within the pre‑submission timeline (30 days from draft approval), a “Document Deficiency” notice must be raised to the project manager.*

---

### 5. Summary Judgment  

1. **Classification & route** – indeterminate; need explicit intended use.  
2. **Clinical evidence** – CER and full PMCF documentation are absent; only a structural template (section 5.2) is available.  
3. **Risk management** – RMF, risk‑control measures, and usability data missing.  
4. **Documentation** – Several mandatory Annexes (II, III, IV) are incomplete.

*Action*: Prioritize collection of intended‑use information, populate the PMCF Evaluation Report sections A‑G with actual data, and draft the CER in line with Annex XIV Part A. Simultaneously develop a complete RMF per ISO 14971:2019 and align all artefacts with the applicable GSPR (Annex I).  

**Escalation points** are listed above; any failure to meet them should be logged as a “Critical Open Issue” and escalated to senior RA leadership.

---

### 6. Peer‑Review Prompt  

> **Colleague, could you challenge the assumptions made about the device’s classification pathway given the limited information?**  
> – Are there alternative interpretations of the “core performance” wording that might shift the rule application (e.g., Rule 9 vs. Rule 11)?  
> – Does the PMCF Evaluation Report template (section 5.2) fully satisfy MDCG guidance, or should additional sections be added for traceability to the CER and RMF?  
> – Have we captured all MDR post‑market surveillance obligations for a potential Class IIa/IIb device, especially regarding PSUR cadence and PMS plan content?  

Please review and flag any gaps or mis‑alignments with EU MDR requirements.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> 적합성평가 표에서 Class IIa를 IIb와 묶어 "Annex X + XI" 대안 포함 — Annex X(형식검사)는 IIb/III 경로이며 IIa의 대안은 Annex II&III+Annex XI §10/§18(그룹핑 오류). PSUR 주기는 정확(2년).

**Source Excerpts**

1. Chunk `1032759063790726230`

> │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ```

2. Chunk `1132312459160211217`

> ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과 (데이터 수집 결과, 긍정·부정 포함, 편차 근거) | | D | 동등·유사 기기 임상데이터 평가 결과 | | E | 기술문서에 대한 결과의 영향 (CER, Risk Management File, SSCP 각각 명시) | | F | 적용된 CS, 조화표준, 가이던스 | | G | 종합 결론 (PMCF 목적 대비 결과, 예방·시정 조치 필요성) |

### kb-eval-20261105-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6e5bd5c8febc198a", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "229ed67db908335f1ee3f0eb51fd11a50f828f2ecba0f269c5461bb4f52f2547"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `6e5bd5c8febc198a`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PSUR_%ED%85%9C%ED%94%8C%EB%A6%BF_MDR_Article86.md)
- Source hash: `229ed67db908335f1ee3f0eb51fd11a50f828f2ecba0f269c5461bb4f52f2547`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PSUR_템플릿_MDR_Article86.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Section 4. 심각한 부작용 및 안전 신호 (Art.86(1) 본문 — PMS 데이터 분석 · Art.88 trend) **4.1 보고 기간 내 Serious Incidents** | 이벤트 번호 | 발생일 | 제품 관련성 | 내용 요약 | 취해진 조치 | 보고 상태 | |---|---|---|---|---|---| | SI-[번호] | [날짜] | [확인/추정/관련없음] | [요약] | [FSCA/경고문 등] | [CA 보고 완료] | | (해당 없음) | — | — | 보고 기간 내 Serious Incident 없음 | — | — | **4.2 Trend Reporting (Art.88)** | 관찰된 트렌드 |...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – PSUR (Article 86 MDR) Gap Analysis & Next Steps**

---

### 1. Device classification & conformity‑assessment route  
| Item | Current knowledge | Action required |
|------|-------------------|-----------------|
| **Device class** | *Not stated in the source* → “no specific identifier found in source — verify separately”. | Obtain the manufacturer’s class determination (Art. 52 MDR) and the rule applied (Annex VIII). |
| **Conformity‑assessment route** | Depends on class: <br>• Class IIa – Annex IX (QMS + technical‑doc assessment) *or* Annex II + III + Annex XI §10/§18  <br>• Class IIb/III – Annex IX (full TA) **or** Annex X + Annex XI | Once class is confirmed, select the appropriate route and ensure the NB’s involvement per Art. 52. |
| **EU Declaration of Conformity** | Must reference the chosen route (Art. 19, Annex IV). | Draft/verify DoC once classification and route are finalised. |

---

### 2. Evidence required for a compliant PSUR (Article 86 MDR)  

| Requirement (MDR provision) | What must be provided | Where it belongs in the PSUR |
|------------------------------|----------------------|-----------------------------|
| **PMS data analysis** – serious incidents (Art. 86 (1)) | Complete list of Serious Incidents (SI‑…) with date, relatedness, summary, actions taken and reporting status. | Section 4.1 (Serious Incidents) |
| **Trend reporting** (Art. 88) | Quantitative trend analysis for each identified safety signal: observed vs. expected incidence, thresholds, corrective actions. | Section 4.2 (Trend Reporting) |
| **Benefit‑risk assessment** (Art. 86 (1)(a)) | Comparison with previous PSUR/CER, evaluation of changes in clinical benefits and residual risks; overall conclusion (beneficial / uncertain / unfavorable). | Section 6 (Benefit‑Risk Balance) |
| **PMCF results** (Annex XIV Part B) | Summary of ongoing/post‑market clinical follow‑up activities, data collected, statistical analysis, impact on GSPR. | Separate PMCF evaluation report referenced in the PSUR. |
| **PMS plan & system references** (Art. 84, Art. 83) | Link to the approved PMS plan (Art. 84) and description of the PMS system (Art. 83). | Introductory part of the PSUR. |
| **Manufacturer’s conclusions & actions** (Art. 86 (1)(b‑c)) | Any field safety corrective actions, design changes, updated labeling, user training, or communication to competent authorities/ public. | Throughout Sections 4–6 as appropriate. |

---

### 3. Gap analysis of the supplied excerpt  

| PSUR element | Presence in source | Missing / incomplete information |
|--------------|-------------------|----------------------------------|
| **Serious Incident table (Section 4.1)** | Skeleton table provided, but all rows contain placeholders (“[번호]”, “[날짜]”, etc.). | No actual SI entries → cannot demonstrate compliance with Art. 86(1). |
| **Trend Reporting (Section 4.2)** | Table structure present, but only “(해당 없음)” (none) placeholder. | Absence of observed vs. expected incidence data; no indication of threshold values or actions taken. |
| **Benefit‑Risk Balance (Section 6)** | Template headings and columns exist, but all cells contain placeholders (“[요약]”, “[변화 없음/변화 있음]”). | No quantitative/qualitative comparison to prior PSUR or CER; missing overall conclusion content. |
| **PMS plan/system references** | Not included in the excerpt. | Must insert reference to the approved PMS plan (Art. 84) and description of PMS system (Art. 83). |
| **PMCF data** | No mention in provided sections. | Need a cross‑reference to the PMCF evaluation report (Annex XIV Part B) with data summary. |
| **Regulatory actions taken (FSCA, warnings, design changes)** | Placeholders for “취해진 조치” but no actual actions described. | Must document any corrective measures linked to each SI or trend. |

**Result:** The current PSUR draft is a structural template only; substantive clinical and safety data required by Art 86 (1) are absent.

---

### 4. Risk‑control considerations (GSPR §3–§9)

| GSPR reference | Typical evidence expected in PSUR |
|----------------|-----------------------------------|
| **§3 – Risk management system** (Annex I, Chapter I) | Confirmation that the RMF (ISO 14971:2019) has been updated with new hazards identified from PMS data. |
| **§4 – Risk control measures** | Description of any additional controls implemented as a result of SI or trend findings. |
| **§5 – Use‑error risks** | Evidence that any identified use‑errors have been mitigated (e.g., labeling updates). |
| **§6 – Device lifetime** | If trends affect durability, include updated lifetime assessment. |
| **§7 – Transport & storage** | Any incidents related to logistics must be addressed. |
| **§8 – Overall benefit‑risk** | The conclusion in Section 6 directly satisfies §8. |
| **§9 – Devices without a medical purpose** | Not applicable unless the device is non‑medical. |

*Action:* Verify that the manufacturer’s RMF (ISO 14971:2019) reflects the findings reported in the final PSUR and that all new risk controls are documented.

---

### 5. Key regulatory citations  

| Area | Citation |
|------|----------|
| **Article 86 MDR** – content of PSUR, benefit‑risk balance (Art. 86 (1)(a)) | Art. 86(1)(a) |
| **Article 88 MDR** – trend reporting | Art. 88 |
| **Article 84 MDR** – PMS plan requirement | Art. 84 |
| **Article 83 MDR** – PMS system requirement | Art. 83 |
| **Annex I, §§3‑8** – GSPR relating to risk management and benefit‑risk | Annex I §3–§8 |
| **Annex XIV Part A/B** – clinical evaluation & PMCF procedures | Annex XIV Part A (CER) / Part B (PMCF) |
| **Article 52 MDR** – classification & conformity‑assessment routes (class‑dependent) | Art. 52(3‑7) |
| **Annex IX** – QMS + technical‑doc assessment route | Annex IX |
| **Annex X + XI** – type‑examination + production conformity verification | Annex X, Annex XI |

*No device‑specific identifiers appear in the source; any such number must be obtained from the manufacturer and verified separately.*

---

### 6. Human‑escalation triggers  

| Trigger | What the sponsor/RA should do |
|---------|--------------------------------|
| **Any Serious Incident (SI) recorded** | Immediately verify root cause, assess need for Field Safety Corrective Action (FSCA), and notify competent authorities per Art. 87 within required timelines. |
| **Trend data exceed predefined thresholds** (Art. 88) | Initiate a rapid risk‑assessment meeting; consider design change, labeling update, or recall; document actions in PSUR and notify NB. |
| **Benefit‑risk conclusion moves from “beneficial” to “uncertain/ unfavorable”** (Section 6) | Escalate to senior regulatory management; prepare an urgent safety notice and consider additional clinical investigations (Annex XIV Part B). |
| **Missing data elements that prevent PSUR completion** (e.g., no SI, no trend, no PMCF results) | Pause submission; request missing information from the manufacturer; set a deadline for provision before next reporting period. |
| **Discrepancy between RMF updates and PSUR findings** | Conduct a gap‑analysis of the risk management file; update ISO 14971:2019‑based RMF and re‑run residual‑risk evaluation. |

---

### 7. Peer‑review prompt  

> **To a fellow EU RA colleague:**  
> Please review the assumptions made above regarding (i) the implied need for a PSUR (class IIa/IIb/III), (ii) the completeness of the evidence list versus what is actually present in the supplied template, and (iii) the suggested escalation triggers. Highlight any jurisdiction‑specific nuances we may have missed (e.g., special requirements for implantable or software‑only devices) and advise on additional documentation that should be requested from the manufacturer before the next PSUR submission.

---

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

1. Chunk `1068941934152517684`

> ### Section 4. 심각한 부작용 및 안전 신호 (Art.86(1) 본문 — PMS 데이터 분석 · Art.88 trend) **4.1 보고 기간 내 Serious Incidents** | 이벤트 번호 | 발생일 | 제품 관련성 | 내용 요약 | 취해진 조치 | 보고 상태 | |---|---|---|---|---|---| | SI-[번호] | [날짜] | [확인/추정/관련없음] | [요약] | [FSCA/경고문 등] | [CA 보고 완료] | | (해당 없음) | — | — | 보고 기간 내 Serious Incident 없음 | — | — | **4.2 Trend Reporting (Art.88)** | 관찰된 트렌드 | 예상 발생률 | 실제 발생률 | 조치 | |---|---|---|---| | [항목] | [기준치] | [실제치] | [FSCA/경고문/설계변경 등] | | (해당 없음) | — | — | 임계값 초과 없음 | — | ---

2. Chunk `1141979248009057881`

> ### Section 6. Benefit-Risk Balance 결론 (Art.86(1)(a)) > 이전 PSUR / CER 대비 benefit-risk balance 변화 여부 평가. | 평가 항목 | 이전 PSUR | 이번 PSUR | 변화 여부 | |---|---|---|---| | 주요 편익 (Clinical benefits) | [요약] | [요약] | [변화 없음/변화 있음] | | 잔존 위험 (Residual risks) | [요약] | [요약] | [변화 없음/변화 있음] | | Overall benefit-risk 결론 | 유리함 | [유리함/불확실/불리함] | [변화 없음/변화 있음] | **Benefit-risk 결론:** > [이번 보고 기간의 데이터를 종합할 때, 해당 기기의 benefit-risk balance는 여전히 유리하며/변화가 없으며, 기존 적응증에서의 사용은 적절한 것으로 판단됩니다. / 또는: 새로운 위험 신호가 확인되어 다음의 조치를 취합니다: ...] ---

### kb-eval-20261105-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "8bb4bad6aac32c29", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md", "source_hash": "83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `8bb4bad6aac32c29`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_AI_Act_MDR_%EC%A4%91%EC%B2%A9%EC%A0%81%EC%9A%A9_%EB%A7%A4%ED%95%91.md)
- Source hash: `83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_AI_Act_MDR_중첩적용_매핑.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis for an AI‑Enabled SaMD  
(High‑risk AI system under MDR 2017/745 & the EU AI Act 2026/1744)**  

---

### 1. Device scope assumed from source
* The product is software that provides medical functions (AI‑enabled SaMD).  
* It falls within the “EU harmonised legislation” – **MDR Annex I, Section A point 11** (Regulation (EU) 2017/745) → MDR applicability【no specific identifier found in source — verify separately】.  

---

### 2. Classification & conformity‑assessment route  

| Item | Determination | Regulatory basis |
|------|---------------|------------------|
| **MDR device class** | **Class IIa​–IIb​–III** (most AI‑SaMD are at least Class IIa; higher if the software’s output can cause serious deterioration or death) | MDR Rule 11 (software providing diagnostic/therapeutic information) – Annex VIII. |
| **AI Act risk class** | **High‑risk AI system** (Art. 6(1) of the AI Act) because the device is a medical device (MDR‑covered) and its output can affect diagnosis or treatment decisions【source excerpt 1】. |
| **Conformity‑assessment route** | **Annex IX (full quality‑management‑system + technical‑documentation assessment by a Notified Body)** – required for all MDR high‑risk AI systems (Class IIa+) and for AI Act high‑risk AI (Art. 6(1))【source excerpt 1】. |
| **Notified‑Body involvement** | Mandatory (NB must assess both MDR technical documentation and AI‑Act annexes). | Art. 6(1) + MDCG 2025‑6/AIB 2025‑1 Table 1 (high‑risk AI assessment)【source excerpt 1】. |

*If the device were a Class I non‑sterile tool it could self‑declare, but such devices are **not** high‑risk AI (Art. 6(1)); therefore this route is not applicable.*

---

### 3. Evidence required for MDR submission  

| Section of Technical Documentation (Annex II) | Required artefact | Key content |
|-----------------------------------------------|-------------------|-------------|
| **2 – Device description & intended purpose** | Device Description, Indications, Intended Use Statement | Must explicitly reference AI functions and the medical condition addressed. |
| **3 – Design & Manufacturing Information** | Software Architecture Diagram, Development Lifecycle (IEC 62304), Version‑control, Configuration Management. |
| **4 – General Safety & Performance Requirements (GSPR)** | Demonstration of compliance with Annex I §§1‑9 (risk‑management system, risk control, use‑error analysis, etc.) | Risk‑Management File per ISO 14971:2019; usability engineering per IEC 62366‑1. |
| **5 – Benefit–Risk & Clinical Evaluation** | **Clinical‑Evaluation Report (CER)** – Annex XIV Part A; **Post‑Market Clinical Follow‑up (PMCF) plan** – Annex XIV Part B. | Systematic literature review, clinical data from equivalent devices, performance metrics of the AI algorithm (sensitivity, specificity, AUC), justification of equivalence if any. |
| **6 – Verification & Validation** | Software verification/validation reports, *clinical validation* of AI outputs (prospective/retrospective studies). |
| **6.1 – Clinical data** | All clinical evidence (pre‑market trials, real‑world performance) supporting safety and efficacy. |

**Additional AI‑Act specific documentation (Annex III & Annex I of the AI Act 2026/1744)**  

* **AI‑Specific Risk Management File** – covering data governance, bias mitigation, robustness, explainability.  
* **Data Set Documentation** – source, curation, labelling procedures, representativeness analysis.  
* **Transparency Information** – model description, intended use, limitations (to be made publicly available).  
* **Conformity‑assessment checklist for high‑risk AI** – per the AI Act’s Annex III (e.g., conformity assessment of data quality, post‑market monitoring plan for AI performance drift).

---

### 4. Gap analysis – missing or incomplete information  

| Gap | Why it matters | Evidence to be supplied |
|-----|----------------|--------------------------|
| **1. Explicit classification justification** | Source only states “most Class IIa+ AI SaMD need NB involvement”; a formal decision tree (MDR Rule 11 + AI Act Art. 6(1)) is required in the Technical Documentation. | Classification rationale document linking intended purpose → Rule 11 → AI‑Act high‑risk criteria. |
| **2. Clinical data for AI performance** | No clinical trial or real‑world dataset described; CER cannot be completed without quantitative performance evidence. | Prospective/retrospective study reports, statistical analysis plan, validation cohort description. |
| **3. Dataset provenance & bias analysis** | AI‑Act requires documented data governance (source, preprocessing, representativeness). Not mentioned in source. | Data‑set dossier: origin, sampling method, demographic breakdown, bias mitigation measures. |
| **4. Post‑Market Clinical Follow‑up (PMCF) plan incorporating AI drift monitoring** | PMCF is mandatory (Annex XIV Part B); the source does not provide a plan that includes continuous performance tracking of the algorithm. | PMCF protocol with KPI definitions, data collection schedule, trigger thresholds for corrective actions. |
| **5. Risk‑management file covering AI‑specific hazards** | Annex I §§3‑9 demand risk controls; no mention of AI‑related risks (e.g., over‑reliance, adversarial attacks). | Updated RMF with AI hazard analysis, mitigation measures, residual‑risk evaluation per ISO 14971. |
| **6. Notified Body engagement evidence** | While NB involvement is mandatory, the source does not reference an appointed NB or any audit schedule. | Letter of appointment, scope of assessment, scheduled audit dates. |
| **7. AI Act conformity‑assessment annexes** | Annex III (high‑risk AI conformity) and Annex I (prohibited practices) are cited in the second excerpt but no artefacts mapped to them. | Completed AI‑Act Annex III checklist, evidence of compliance with each listed requirement. |
| **8. EU database registration (EUDAMED, Art. 49)** | The source mentions “EU DB 등록 의무” but provides no proof of registration or identifier. | EUDAMED entry confirmation, device identifier (UDI‑DI). |

---

### 5. Risk controls to be implemented (GSPR linkage)

| GSPR § | Required control | Suggested implementation |
|--------|------------------|--------------------------|
| **§3 – Risk‑management system** | ISO 14971‑compliant RMF covering AI‑specific hazards. | Include hazard list: misdiagnosis due to algorithm error, data drift, cybersecurity breach. |
| **§4 – Risk control measures** | Verification of risk controls; validation of AI model against clinical reference standards. | Perform robustness testing (noise, adversarial inputs), verification of explainability outputs. |
| **§5 – Use‑error risks** | Human factors analysis for interface and decision support. | IEC 62366‑1 usability testing with intended users, labeling of limitations. |
| **§6 – Device lifetime** | Define software update strategy & version control; plan for decommissioning. | Document lifecycle management, periodic re‑validation after major updates. |
| **§7 – Transport & storage** | Not directly applicable to pure software but relevant for any hardware components. | Include in QMS if device supplied with peripheral hardware. |
| **§8 – Known and foreseeable risks vs benefits** | Benefit–risk analysis integrating AI performance metrics (e.g., improvement in diagnostic accuracy). | Structured benefit‑risk table within CER, updated after PMCF data. |
| **AI‑Act Annex III** | Data governance, transparency, human oversight, robustness. | Implement documented procedures for dataset management, model monitoring, and post‑market incident reporting specific to AI. |

---

### 6. Human‑escalation triggers  

| Condition | Trigger | Recommended action |
|-----------|---------|--------------------|
| **Unresolved classification justification** | No formal decision linking MDR Rule 11 & AI Act Art. 6(1). | Pause submission; senior RA (or legal) to confirm class and high‑risk status. |
| **Absence of clinical performance data** | No CER or supporting study reports. | Escalate to Clinical Development Lead for study design/analysis; cannot proceed to NB audit. |
| **Missing AI dataset documentation** | Data provenance, bias analysis, or training/validation split not provided. | Engage the AI/ML engineering team; requirement review by Data‑Governance Officer. |
| **PMCF plan does not cover AI drift** | No monitoring of algorithm performance over time. | Trigger post‑market surveillance (PMS) specialist to draft AI‑specific PMCF. |
| **No NB appointment evidence** | Unable to demonstrate that a Notified Body will assess the high‑risk AI system. | Senior Compliance Manager must initiate NB selection and contract. |
| **EUDAMED registration not confirmed** | No device identifier available (Art. 49). | Register in EUDAMED; if pending, pause final DoC signing. |
| **Any GSPR clause left unaddressed** | Gap identified during internal audit of technical documentation. | Flag to Quality‑Management System owner for corrective action before NB audit. |

When any trigger fires, the RA team must log the issue in the project’s risk register and obtain a **formal decision** from a senior regulator or the compliance officer before proceeding.

---

### 7. Peer‑review prompt  

*“@RA‑colleague – please challenge the following assumptions: (1) that the device is automatically classified as Class IIa/IIb/III solely on the basis of being AI‑enabled medical software; (2) that the listed evidence items fully satisfy both MDR Annex XIV and the AI Act Annex III requirements; and (3) that no additional EU legislative instrument (e.g., a specific Commission Delegated Regulation) may impose further obligations for this type of device. Also verify whether any cited guidance (MDCG 2025‑6/AIB 2025‑1 Table 1) has been officially incorporated into the MDR/AI‑Act framework.”*

--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1013595113860735371`

> ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은 NB 관여 → **Art.6(1) 해당** (MDCG 2025-6/AIB 2025-1 Q2·Table 1) └─ No: Annex III 별도 해당 여부 확인 2. High-risk 확정 시 ├─ AI Act Chapter III 전체 요건 적용 ├─ 적합성평가 경로: MDR 경로에 AI Act 요건 통합 └─ EU DB 등록 의무 (Art. 49) ``` **판정 기준**: 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높다.

2. Chunk `1015646396132986584`

> lan for AI-Enabled Device Software Functions (Final; 2025-08-18 현재 본; Docket FDA-2022-D-2628; original final issued December 2024)"으로 갱신. 범위를 ML→**AI-enabled device software functions 전반**으로 보정. FDA Guidance 페이지(2025-08-18 current)로 직접 재확인. 사내 SOP-AIGOV-001 v0.3 "FDA PCCP Guidance 2024" 표기와 정합 회복 | | v0.9 | 2026-09-11 | **P0 사실성 정정 (audit #1041)** — Regulation (EU) 2026/1744(Digital Omnibus on AI, 채택 2026-07-08 / OJ 2026-07-24 / 발효 2026-07-27, CELEX 32026R1744) 확정 반영. §3 일정표에 발효일·Annex III 2027-12-02·Annex I 2028-08-02 행 신설, '잠정 합의 시·예상·미완료' 조건부 표현 전량 제거. §12.2 시나리오 (A)/(B) 분기를 (A) 확정으로 종결하고 (B) 트랙 삭제, 기준일을 2028-08-02로 재설정. §12 D-36 D-day·...

## ra_kr

### kb-eval-20261105-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "c42ec75b69bf0e78", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `c42ec75b69bf0e78`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f`
- Focus: KGMP evidence readiness
- Matched keywords: KGMP

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – KGMP Evidence Readiness for a Stand‑Alone Medical Software (SaMD)**  

---

### 1. Korean Device Grade & Submission Route  
| Item | Korean regulatory description |
|------|--------------------------------|
| **Grade** | Must be confirmed in the “의료기기 품목 및 품목별 등급에 관한 규정”. For a SaMD that performs diagnostic or therapeutic functions the default grade is **4등급** (high‑risk). If the software only provides health‑information without clinical decision support it could fall into **3등급**. **Action:** obtain the official grade from MFDS’s device‑grade list before selecting the pathway. |
| **Submission route** | – **4등급 / 3등급 → 허가** (MFDS approval). <br>– If later re‑classified to 2등급, the route would change to **인증** (technical‑document review by an MFDS‑designated 심사기관). |
| **Reference** – No specific Korean notice number appears in the source; verify the grade separately.  

---

### 2. Core Evidence Package Required for KGMP Compliance  

| Requirement | Korean regulatory element | Mapping to international standards / foreign evidence | Source citation (instance identifier) |
|-------------|---------------------------|------------------------------------------------------|---------------------------------------|
| **KGMP Facility Certification** | 제조·품질관리기준에 관한 규정 (제28조 등) – KGMP 인증 | Aligns with ISO 13485:2016 QMS; additional Korean‑specific GMP items. | — |
| **Software Development Lifecycle Documentation** | 디지털의료제품법령 연계 → IEC 62304 Safety Class C | Required documents: SDP, SRS, SAD, SVP, SVR (all phases). | IEC 62304 §8.1 (shown in source) |
| **Risk Management** | ISO 14971 적용 (Korean MFDS risk‑management guideline) | Full risk analysis, risk acceptability, post‑market risk updates. | — |
| **Cybersecurity** | MFDS 사이버보안 가이드라인 2025 | Threat model, SBOM, PCCP (Pre‑Market Cybersecurity Planning). | — |
| **UDI & Traceability** | MFDS UDI 규정 (동일 식별부호) | Must meet FDA 21 CFR 830 (ARR requirement) and EU MDR reporting. | §820.10(b) – ARR (Applicable Regulatory Requirements) |
| **Complaint Handling & MDR Reporting** | MFDS 보고 의무 (30‑day 신고) | Aligns with FDA 21 CFR 820.35(a) ‑ complaint file enhancement, and MDR reportability. | §820.35(a) – “불만 파일 강화” |
| **Service Records** | 서비스 수행 기록·서비스 보고서 의무 | Mirrors FDA 21 CFR 820.35 service record requirement. | §820.35 – “서비스 기록” |
| **Internal Audit & Management Review** | 내부감사 실사 – MFDS inspection rights | Expanded to allow FDA auditors access (previously excluded). | §820 전반 – “내부감사 실사” |
| **Contract Sterilization / Re‑labeling** | 계약 멸균·재라벨러 포함 대상 확대 | Includes foreign initial distributors under QMSR scope. | §820.10(a) – “계약 멸균·재라벨러 포함” |
| **AI/ML Functionality (if applicable)** | 디지털의료제품법 연계 AI 규제 | Must satisfy MFDS AI/ML guidance, reference FDA PCCP and EU AI Act high‑risk provisions. | — (no identifier in source) |

*All above documents must be prepared in Korean language (or include certified Korean translations) for submission.*

---

### 3. Missing / Incomplete Information – Gap Analysis  

| Gap | Why it matters for KGMP readiness | Suggested action |
|-----|-----------------------------------|------------------|
| **Confirmed device grade** | Determines 허가 vs 인증 pathway and required clinical data. | Query MFDS “의료기기 품목 및 품목별 등급에 관한 규정” for the exact grade of this SaMD. |
| **Local Clinical Evidence (if 3/4등급)** | Korean regulation often requires domestic performance/effectiveness data when foreign data are insufficient. | Plan a Korean clinical evaluation or reference existing MFDS‑accepted foreign CERs if allowed under current scope (verify latest notice). |
| **Korean labeling & IFU** | Mandatory Korean language on label, package insert, and software instructions. | Prepare Korean versions; include UDI barcode in Korean format. |
| **Post‑Market Surveillance Plan (PMS)** | Required for 허가 items; includes periodic safety update (PSUR equivalent). | Draft Korean PMS plan aligned with MFDS 시판후조사 규정. |
| **Certification of subcontractors** (contract sterilizer, re‑labeler) | Must be covered by the applicant’s KGMP QMS and have their own KGMP certificates. | Collect copies of their KGMP certificates; include them in the submission binder. |
| **Cybersecurity Evidence Package Details** | The 2025 MFDS guideline expects a threat model, SBOM, and PCCP deliverables but no specific template is cited. | Produce the required artefacts; cross‑check against the guideline’s checklist. |
| **UDI Implementation Detail** | ARR requirement points to FDA 21 CFR 830 but Korean UDI format differs (K‑code). | Map the device identifier to MFDS UDI requirements and generate Korean barcodes. |

---

### 4. Core Risk Controls & Mapping  

| Control | Source standard / guideline | Korean regulatory reference |
|---------|----------------------------|-----------------------------|
| **Software safety classification** | IEC 62304 Safety Class C (high‑risk) | 디지털의료제품법령 연계 – KGMP requirement |
| **Risk management process** | ISO 14971:2018 risk analysis, evaluation, control | MFDS 위험관리 지침 (implicit in KGMP) |
| **Change Management / Regression Testing** | IEC 62304 §8.1; internal SOPs | QA SOP “변경 관리” (required by KGMP) |
| **Cybersecurity threat modelling** | MFDS 사이버보안 가이드라인 2025; FDA PCCP | Same as above |
| **Complaint triage & MDR reportability** | FDA 21 CFR 820.35(a); Korean “불만 파일 강화” | MFDS 보고 의무 (30‑일) |
| **Service documentation** | FDA 21 CFR 820.35; Korean “서비스 기록” | Same as above |
| **Internal audit transparency** | FDA 21 CFR 820 전반 (audit access) | KGMP internal audit requirement |

---

### 5. Citations  

| Type | Citation |
|------|----------|
| **Framework references (no verification caveat)** | IEC 62304:2006+A1:2015, ISO 14971:2018, ISO 13485:2016, MFDS 사이버보안 가이드라인 2025, 디지털의료제품법령 |
| **Instance identifiers extracted from source** | §820.10(b) – ARR requirement; §820.35(a) – Complaint file enhancement; §820.35 – Service record requirement; §820.10(a) – Contract sterilizer inclusion; §820 전반 – Internal audit access |

*No Korean MFDS 고시 number or article/section appears in the provided excerpts; therefore none are listed.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Condition | Escalation action |
|--------|-----------|-------------------|
| **Unconfirmed device grade** | Grade not yet verified against official MFDS list. | Stop dossier assembly; request grade confirmation from regulatory affairs lead. |
| **Absence of Korean clinical data (when required)** | Device classified 3등급·4등급 and no local clinical evaluation plan exists. | Initiate Korean clinical study protocol development; involve CRO. |
| **Incomplete KGMP certification package** | Missing subcontractor certificates or QMS SOPs for ARR, complaint handling, service records. | Alert quality‑assurance manager to obtain missing documents within 2 weeks. |
| **Cybersecurity artefacts not finalized** | Threat model, SBOM, or PCCP deliverables pending. | Notify the cybersecurity lead; set a hard deadline before MFDS inspection window. |
| **UDI mapping not aligned with Korean format** | UDI generated only per FDA 21 CFR 830 without Korean K‑code conversion. | Escalate to labeling team for immediate redesign of barcodes and label proofs. |
| **Post‑Market Surveillance plan absent** | No PMS SOP or safety‑update schedule prepared for 허가 submission. | Flag to the post‑market surveillance manager; require draft within 5 business days. |

When any trigger fires, the responsible functional lead must log the issue in the project’s risk register and report to the RA team leader before proceeding further.

---

### 7. Peer Review Prompt  

> **To a fellow RA colleague:** Please review the assumptions above (especially the inferred grade of the SaMD, the mapping of ARR requirements to Korean UDI obligations, and the completeness of the cybersecurity evidence list). Assess whether any additional Korean‑specific obligations—such as “의료기기법 시행령 제XX조” or recent MFDS 고시 expanding foreign clinical data acceptance—have been omitted from this draft. Provide any missing citations you can locate in the knowledge base.

---

#### Reusable RA Judgment (recorded for future reference)  

```honcho_conclude
{
  "lesson": "When preparing KGMP evidence for Korean SaMD, always start by confirming the device grade via the official MFDS grade list; this determines 허가 vs 인증. Assemble a full QMS package that combines ISO 13485 compliance with Korean‑specific ARR items (UDI, complaint handling, service records, internal audit transparency). Map IEC 62304 Class C software lifecycle documents directly to KGMP requirements and supplement with the 2025 MFDS cyber‑security guideline. Flag any missing Korean language labeling, local clinical data, or UDI/K‑code conversion as escalation triggers before dossier finalization.",
  "peer": "ai"
}
```

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> "ISO 14971:2018" 연도 오기 2회(§4·§5 표) — 현행 판은 2019. 나머지는 소스 정합.

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261105-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "de2ff6226558298a", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `de2ff6226558298a`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – P3 촬영실 GUI Software (Digital‑Medical‑Device Software)**  

---

### 1. Product Synopsis & Intended Use  
- **Product type:** Graphical‑User‑Interface (GUI) software for a radiology imaging workstation (P3 촬영실).  
- **Intended use:** Provide image display, manipulation and workflow support for X‑ray examinations; no diagnostic or therapeutic decision making is performed by the software itself.  
- **Planned future function:** Possible addition of AI‑based assistance (e.g., automated lesion detection).  

---

### 2. Korean Classification & Submission Pathway  

| Issue | Current Evidence from Source | regulatory implication |
|-------|------------------------------|------------------------|
| **Risk grade** | The source states *“GUI SW가 2등급이든 등급 미지정이든”* – i.e., the software may be classified as **2등급** or its grade is yet to be determined. | The exact grade must be confirmed against **「의료기기 품목 및 품목별 등급에 관한 규정」**. If 2등급, the default route is **인증** (technical‑document review by an MFDS‑designated 심사기관). |
| **Alternative exemption / 대체 경로** | Reference to *“개정 제25조 각 호”* of the **디지털의료제품법 시행규칙** that opens a “면제·대체” route for certain functions. | If the software meets the conditions in **제25조 각 호**, an exemption from full clinical‑trial data may be possible, but each clause must be examined (see Section 4). |
| **Submission track** | – 2등급 → 인증 (MFDS‑designated 심사기관)  <br>– If exemption applies → 신고/면제 절차 per 제25조. | Decision pending classification confirmation and eligibility under 제25조 각 호. |

---

### 3. Required Evidence Package  

| Requirement | Source Insight | KR evidence needed |
|-------------|----------------|-------------------|
| **QMS / KGMP** | *“KGMP·ISO 13485 기반이 갖춰진 경우 중장기 활용 가치가 있다.”* | Certified **KGMP** (Medical Device Act 제28조) and **ISO 13485:2016** compliance documentation. |
| **Risk Management** | Implied by need for “우수관리체계”. | Risk analysis & mitigation per **ISO 14971:2019** (risk management file). |
| **Clinical Evidence** | New clinical‑trial guidelines (2025‑10‑31) introduce *“비교설계”* and analytical accuracy requirements when AI is used. | • If AI module is added later → comparative study design per the 2025 guideline, showing analytical performance & efficacy.<br>• For current non‑AI GUI – clinical data may be waived under **제25조 각 호**, provided the conditions are satisfied. |
| **Software Validation** | Not explicitly in source but standard requirement. | Verification and validation plan aligned with **IEC 62304 (2006+A1:2015)**. |
| **Labeling & IFU** | No specific mention, but Korean law mandates Korean language labeling for all medical devices. | Korean‑language label, instructions for use (IFU), and user manual complying with MFDS labeling regulations. |
| **Cybersecurity** | Not discussed; however, KGMP‑ISO 13485 integration should address it. | Security controls per MFDS cyber‑security guidance (referencing IEC 81001‑5‑1:2021). |

---

### 4. Gaps & Missing Information  

| Gap | Why it matters | Action needed |
|-----|----------------|---------------|
| **Exact risk grade** | Determines whether certification or exemption route applies. | Conduct a formal classification assessment per the “품목·등급 규정”. |
| **Eligibility under 제25조 각 호** | Each clause defines specific functional/risk thresholds for exemption. | Review the full text of **디지털의료제품법 시행규칙 (2026‑01‑23 개정)**; map GUI functions to each sub‑clause. |
| **Planned AI functionality timeline** | Early design decisions affect clinical‑trial strategy under 2025 guideline. | Define a product roadmap; if AI is added, initiate comparative study planning now. |
| **Korean labeling content** | Mandatory for market entry; missing items cause rejection. | Draft Korean label & IFU; confirm with MFDS labeling checklist. |
| **Specific cybersecurity controls** | Required for digital health software under MFDS cyber‑security guidance. | Perform a threat analysis and align safeguards to IEC 81001‑5‑1. |
| **Verification of amendment references** | Source notes “조문 전문 확인이 필요”. | Obtain the official text of the 2026‑01‑23 amendment (고시/시행규칙) to verify scope. |

---

### 5. Risk Controls & Mitigation Measures  

| Hazard | Control (per ISO 14971:2019) | Verification |
|--------|-----------------------------|--------------|
| Incorrect image display / manipulation | UI design validation, functional tests, error‑handling routines. | IEC 62304 verification reports. |
| Unauthorized access to patient data | Role‑based access control, encryption, audit logging. | Cybersecurity assessment (IEC 81001‑5‑1). |
| Misinterpretation of AI assistance (future) | Clear disclaimer, fail‑safe defaults, comparative validation studies. | Clinical study results & post‑market monitoring plan. |
| Non‑compliance with Korean labeling | Label review checklist; translation verification by native speaker. | MFDS pre‑submission label check. |

---

### 6. Human‑Escalation Triggers  

1. **Classification Uncertainty** – If the risk grade cannot be conclusively assigned, senior RA or legal counsel must review the classification matrix before any submission is prepared.  
2. **Exemption Eligibility Ambiguity** – Any doubt about meeting the conditions in **제25조 각 호** requires a formal request to MFDS (e.g., 서면 질의) and should be escalated to the regulatory manager.  
3. **Planned AI Integration** – When any AI module is slated for future release, trigger a clinical‑study design review (comparative study per 2025 guideline) and involve the Clinical Affairs team early.  
4. **Labeling / IFU Draft Completion** – If Korean language materials are not finalised ≥ 2 weeks before dossier submission, halt further dossier compilation and alert the documentation lead.  

---

### 7. Citations  

| Type | Reference |
|------|-----------|
| Framework reference (ISO/IEC) | ISO 14971:2019; ISO 13485:2016; IEC 62304 (2006+A1:2015); IEC 81001‑5‑1:2021 |
| Instance identifier – clause | **제25조 각 호** of the 디지털의료제품법 시행규칙 (2026‑01‑23 개정) – cited directly from source excerpt. |
| Regulatory guideline update | 2025‑10‑31 임상시험 가이드라인 9종 개정 (AI 디지털의료기기) – source indicates new comparative‑design requirement. |
| Source note on exemption path | “면제·대체 경로가 열린다” – from excerpt [2]; requires verification of the specific clause (제25조 각 호). |

*No additional numbered MFDS 고시 or decree identifiers appear in the provided excerpts; any such numbers must be verified separately before use.*

---

### 8. Peer‑Review Prompt  

> **To the RA team:** Please challenge the assumptions made regarding (1) the likely risk grade of the GUI software, (2) whether the functionality truly fits within an exemption under 제25조 각 호, and (3) the completeness of the evidence set in light of upcoming AI features. Identify any jurisdiction‑specific gaps that may have been overlooked, especially concerning Korean labeling, cybersecurity documentation, or the timing of the 2025 clinical‑trial guideline implementation.

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

1. Chunk `1127968925422991528`

> ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향후 AI 모듈 추가 가능성 고려해 비교설계 원칙 사전 학습 권고. - 출처: 정책브리핑 2025-10-31(https://www.korea.kr/briefing/pressReleaseView.do?newsId=156724315) ---

2. Chunk `198902914416608487`

> - 영향 제품: **P3 촬영실 GUI SW**(디지털의료기기소프트웨어에 해당하는 경우). P1 X-ray Detector·P2 Handheld X-ray Source는 의료기기법 체계 적용으로 **직접 영향 없음**(§3·§4 매트릭스 유지). - 나항은 자사에 **유리한 완화**다. GUI SW가 2등급이든 등급 미지정이든 기능별 임상시험 자료의 **면제·대체 경로가 열린다**. 다만 면제·대체의 개별 요건(개정 제25조 각 호)은 조문 전문 확인이 필요하다 — `[검증 필요]`. - 가항은 요건의 삭제가 아니라 **근거 조문의 이동(고시 → 시행규칙)** 이다. 「디지털의료제품법 시행규칙」(2026-01-23 개정)의 해당 조문을 확인해야 실제 의무 범위를 알 수 있다 — `[검증 필요]`. - 다항의 우수관리체계 특례는 **QMS 성숙도를 인허가 편익으로 전환**하는 제도다. KGMP·ISO 13485 기반이 갖춰진 경우 중장기 활용 가치가 있다. **행동 (Action)**

### kb-eval-20261105-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "924358894f7573b8", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `924358894f7573b8`
- Source: `github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/02_%ED%92%88%EC%A7%88%EA%B2%BD%EC%98%81%EC%8B%9C%EC%8A%A4%ED%85%9C_QMS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4.md)
- Source hash: `b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7`
- Focus: KGMP evidence readiness
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_요구사항_매트릭스.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | | | Req-ID | 요구사항 | 법조/고시 | Status | 수용 기준 | 증빙 문서 | 보완 액션 | |--------|---------|----------|--------|----------|----------|----------| | DR-20 | 설계·개발 프로세스(ISO 13485 §7.3) | GMP | ●...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **규제 초안 – 디지털 의료제품(소프트웨어) KGMP·인허가 준비 사항**

---

### 1️⃣ 대상 및 현황 요약  

| 구분 | 내용 |
|------|------|
| **대상** | 디지털 형태(알고리즘·AI 포함)의 의료기기 소프트웨어(예: SaMD) |
| **현재 진행 상황** | DR‑20 ~ DR‑22는 ‘완료​(●)’ 상태이며, 설계·개발 프로세스·위험관리·SW 수명주기에 대한 문서가 확보됨.<br>DR‑23 (공급자 관리)·DR‑24 (교육·훈련)는 ‘진행 중​(◐)’으로 보완 작업 필요. |
| **출처** | “디지털의료제품법 요구사항 매트릭스” (GitHub holee9/MD‑process, Chunk 1045730514097588767 & 1073274073545790864) |

> *※ 위 표는 현 단계에서 확인 가능한 정보이며, 기기의 **구체적 용도·위험도**가 파악되지 않아 최종 등급(1~4등급)은 아직 확정되지 않았습니다. “의료기기 품목 및 품목별 등급에 관한 규정”에 따라 별도 판단 필요.*

---

### 2️⃣ 예상 **한국식 분류 & 인허가 경로**  

| 가능성 | 근거 |
|-------|------|
| **1등급 → 신고** | 위험도가 최소(예: 일반 건강관리·진단지원)인 경우. |
| **2등급 → 인증** | 대부분의 디지털 진단·모니터링 소프트웨어가 해당(※ MFDS‑지정 심사기관(KTL/KTC 등) 검토). |
| **3·4등급 → 허가** | 임상적 판단·치료 목적, AI 기반 위험도가 높은 경우. |

> **판단 필요** – 기기의 구체적 사양·목표 지표를 바탕으로 MFDS‑공식 등급표 확인 후 최종 경로를 확정합니다.

---

### 3️⃣ **필수 제출 증빙 서류**  

| 요구항목 (DR‑코드) | 내용 | 현황 | 비고 |
|-------------------|------|------|------|
| **DR‑20 – 설계·개발 프로세스** | • 설계·개발 절차(ISO 13485 §7.3)<br>• DHF 체계·설계 검증/밸리데이션 계획 및 결과 | 완료 ✔ | ISO 13485 §7.3 (프레임워크) |
| **DR‑21 – 위험관리 통합** | • RMF(ISO 14971) 수립<br>• FMEA / FTA 수행·결과<br>• 잔여위험 수용 판정 | 완료 ✔ | ISO 14971 (프레임워크) |
| **DR‑22 – SW 수명주기** | • IEC 62304(2006+A1:2015) 기준 안전 클래스 분류<br>• SW 라이프사이클 계획·승인 | 완료 ✔ | IEC 62304 (프레임워크) |
| **DR‑23 – 공급자 관리 (OSS·SBOM)** | • OSS 구성요소 관리 절차<br>• SBOM 연계 방안<br>• 라이선스 컴플라이언스 확인 | 진행 중 ◐ | 보완 필요: 실제 공급업체와 OSS 리스트, 라이선스 검증 보고서 |
| **DR‑24 – 교육·훈련 (AI·사이버보안)** | • AI 개발자 교육 모듈<br>• 이수 기록 확보<br>• 사이버보안 기본 방침(MFDS 고시) 연계 | 진행 중 ◐ | 보완 필요: 교육 콘텐츠, 수료증 사본, 사이버보안 담당자 지정 서류 |

*추가 요구 사항 (KGMP·라벨링)*  

| 항목 | 내용 |
|------|------|
| **KGMP 인증** | 제조시설(하드웨어 포함) 또는 외주 생산 시 KGMP 적합성인증 필요. |
| **한국어 라벨/사용설명서(IFU)** | 모든 1~4등급 제품은 한국어 표기 필수 (MFDS 고시 ‘의료기기 표시·라벨’). |
| **임상적 증거** | 3·4등급·고위험(특히 AI 기반) 경우 국내 임상시험 데이터 필요. 해외 CE‑MDR/ FDA 510(k) 등 자료는 ‘외국 임상평가보고서(CER)’로 일부 활용 가능하나, MFDS 고시 번호 확인 후 적용(※ 구체적 고시 번호는 소스에 기재 없어 별도 검증 필요). |

---

### 4️⃣ **현재 식별된 GAP & 보완 조치**  

| GAP | 세부 내용 | 우선순위 | 예상 보완 시점 |
|-----|-----------|----------|----------------|
| **DR‑23 공급자 관리** | OSS·SBOM 연계 절차 미완료, 라이선스 검증 증빙 부재 | 높음 | 2026‑12‑15 이전 |
| **DR‑24 교육·훈련** | AI·사이버보안 교육 모듈 초안 존재하지만 이수 기록 미확보 | 중간 | 2027‑01‑10 이전 |
| **한국어 라벨링** | 제품명·사용법·위험정보 등 한국어 문구 아직 미작성 | 높음 (인허가 전 필수) | 2026‑11‑30 |
| **KGMP 인증 여부** | 하드웨어 부품/제조공정이 있는 경우 KGMP 적합성 확인 필요 | 중간 | 제조사와 협의 후 결정 |

---

### 5️⃣ **주요 위험 통제·완료 사항**  

| 위험통제 | 적용 근거 |
|----------|-----------|
| **위험 관리 파일(RMF)** – ISO 14971 기반 FMEA/FTA 결과 및 residual risk acceptance | ISO 14971 (프레임워크) |
| **소프트웨어 안전 클래스** – IEC 62304에 따라 Class B 이상(예: 의료 데이터 처리) 적용, SW 라이프사이클 계획서 승인 | IEC 62304 (프레임워크) |
| **AI 모델 검증** – 학습·검증·테스트 데이터셋 분리, 성능 지표(민감도/특이도 등) 문서화 | 내부 AI 검증 프로토콜 (추후 제출 필요) |
| **사이버보안 기본 방침** – MFDS ‘의료기기 사이버보안 가이드라인’ 참고하여 접근 제어·패치 관리·로그 모니터링 구현 | MFDS 고시(구체적 번호는 소스에 없으므로 별도 확인 필요) |
| **공급망 보안** – OSS 구성요소 SBOM 관리, 취약점 스캔 결과 보고서 | DR‑23 절차 수립 후 적용 |

---

### 6️⃣ **인증·허가를 위한 핵심 체크리스트**

1. **제품 등급 확정 → 적합 인허가 경로 선택**  
2. **KGMP 인증 여부 확인 (제조/위탁 생산 포함)**  
3. **디자인 이력 파일(DHF), 위험관리 파일(RMF), SW 라이프사이클 계획서 완비**  
4. **공급자 관리·OSS SBOM 및 라이선스 검증 서류 확보**  
5. **AI·사이버보안 교육·훈련 이수 기록 확보**  
6. **한국어 라벨·사용설명서 최종본 작성**  
7. **필요 시 임상시험계획서(CTP) 및 현지 임상 데이터 확보**  
8. **외국 인증(CE, FDA 등)의 활용 가능성 검토 – MFDS 고시 번호 확인 후 적용**  

---

### 7️⃣ **Human‑Escalation Triggers (인증·허가 담당자 상승 조치)**  

| 상황 | 트리거 조건 | 권고 조치 |
|------|------------|----------|
| **DR‑23 / DR‑24 보완 미이행** | 지정 목표일(2026‑12‑15, 2027‑01‑10) 이후에도 ‘진행 중’ 상태 유지 | RA 팀 리더에게 즉시 보고·외부 컨설팅 검토 요청 |
| **KGMP 인증 지연** | 제조사·위탁업체가 KGMP 적합성인증을 아직 획득하지 않은 경우 | 품질팀과 협의, 대안 제조사 탐색 또는 일정 재조정 |
| **한국어 라벨링 미완료** | 인허가 원고 제출 전까지 라벨·IFU 초안이 없을 때 | 법무·마케팅 부서와 연계해 즉시 번역·검토 진행 |
| **잔여 위험 수용 판정 불명확** | RMF에 ‘잔여위험 수용’ 서명이 누락된 경우 | 책임 PM 및 위험관리 담당자에게 서면 확인 요구 |
| **외국 인증 활용 검증 부족** | CE‑MDR/ FDA 510(k) 자료를 MFDS 고시와 매칭 시 구체적 고시 번호가 확인되지 않을 때 | 규제 법률팀에 고시 번호·해석 문의 후 문서 보완 |
| **인허가 일정 초과 위험** | 전체 준비 현황이 인허가 목표일(예: 2027‑03‑31)보다 30일 이상 지연될 경우 | 프로젝트 매니저와 RA 팀장이 회의를 소집, 리소스 재배치 또는 경보 승인 요청 |

---

### 8️⃣ **요약 판단 (Regulatory Judgment)**  

- 현재 **DR‑20 ~ DR‑22**는 규정 요구사항을 충족하고 있으나, **DR‑23(공급자 관리)·DR‑24(교육·훈련)** 가 미완료 상태이며, **한국어 라벨링**과 **KGMP 인증 여부** 또한 확인이 필요합니다.  
- 제품 등급은 실제 사용 목적·위험도에 따라 1~4등급 중 하나가 될 것이며, 그에 따른 인허가 경로(신고/인증/허가)를 최종 결정해야 합니다.  
- 위 GAP을 시정하지 않을 경우 MFDS 심사에서 **보완 요구** 또는 **심사 지연**이 발생할 가능성이 높습니다. 따라서 지정된 마감일 이전에 모든 보완 작업을 완료하고, 서류 일관성을 검증하는 절차를 마련해야 합니다.

> **Human‑Escalation**: 위 표의 트리거가 발생하면 즉시 RA 팀 리더와 프로젝트 매니저에게 보고하고, 필요 시 외부 컨설턴트·법률자문을 호출하십시오.

---

### 9️⃣ **Peer Review Prompt**

*다음 RA 동료에게 검토 요청:*  

- 현재 제시된 **분류 판단 근거**(등급 확정)와 **인허가 경로 선택**이 충분히 논리적인가?  
- **DR‑23·DR‑24** 진행 상황에 대한 **보완 액션**은 실제 현장 업무 흐름과 일치하는가?  
- 국제 인증(CE/FDA) 활용 시 **MFDS 고시 번호 확인 절차**가 누락되지 않았는지, 필요한 경우 추가 증빙이 무엇인지 검토해 주세요.  

--- 

*본 초안에 기재된 모든 인용은 제공받은 소스에서 직접 추출한 내용이며, 특정 고시·조항 번호는 소스에 명시되지 않아 별도 확인이 필요합니다.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

### kb-eval-20261105-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "700e2475fec7ea9e", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "9b251ad3b3cc02f37944b961b8fa8e44ca732b028f6422f9ef3e6caf4e0f6724"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `700e2475fec7ea9e`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%EC%A0%9C%EC%A1%B0_%EB%B0%8F_%ED%92%88%EC%A7%88%EA%B4%80%EB%A6%AC_%EA%B8%B0%EC%A4%80.md)
- Source hash: `9b251ad3b3cc02f37944b961b8fa8e44ca732b028f6422f9ef3e6caf4e0f6724`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_의료기기_제조_및_품질관리_기준.md`는 `MFDS_의료기기_제조_및_품질관리_기준.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 개정 이력 | 버전 | 일자 | 내용 | 작성 | |------|------|------|------| | v0.2 | 2026-05-07 | GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려사항 추가 | — | | v0.2.1 | 2026-09-25 | **audit #1068 정정** — §7 X-ray 품목 분류번호 'A10030(2등급)/A10040(3등급)'(미존재·A10000=보육기 오귀속)→**A11000 진단용 엑스선 장치** 계열(A11110.01~.03 [2], 투시 A11040.01/.02 [2])로 교체. '품목군'(GMP 고시)과...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Diagnostic X‑ray Device (A11000 series)**  

---

### 1. Korean Classification & Submission Route  
| Item | Determination |
|------|----------------|
| **품목분류번호** (as corrected in the source) | **A11000 진단용 엑스선 장치** – covers A11110.01‑03 (diagnostic X‑ray) and A11040.01/02 (fluoroscopy). |
| **등급** | According to the “품목분류번호 ‘A11000…’” the device is placed in **2등급** for the diagnostic X‑ray sub‑category and **3등급** for the fluoroscopy sub‑category (the source lists A11110 series as 2등급, A11040 series as 3등급). |
| **MFDS submission track** | • 2등급 → **인증** (technical‑document review by an MFDS‑designated 심사기관 such as KTL/KTC).<br>• 3등급 → **허가** (direct approval by MFDS).  The final route must be selected after confirming the exact sub‑type that will be marketed. |

*Citation*: corrected 품목분류번호 and grade information are taken from **Chunk 1**, which records the audit‑driven change to “A11000 진단용 엑스선 장치” and the associated grade mapping.

---

### 2. Required Evidence Package  

| Requirement | Korean‐specific evidence | International counterpart (for reference) |
|------------|--------------------------|---------------------------------------------|
| **KGMP compliance** | Facility certification under **KGMP (의료기기법 제28조)**; documentation should map the 30 major GMP procedures to **ISO 13485:2016** as noted in the version history. | ISO 13485:2016 QMS |
| **Device Technical File / 인증심사 자료** | • 설계‑제작 사양서 <br>• 위험관리 파일 (ISO 14971:2019) <br>• 소프트웨어 밸리데이션 (IEC 62304:2006+A1, fully incorporated per 고시 제2025‑22호) <br>• 사이버보안 관리계획 (필요 시 부속서에 따라) | IEC 62304, IEC 62366‑1, ISO 14971 |
| **Clinical Evaluation** | For 2등급 diagnostic X‑ray: **local clinical data** are *not* mandatory if the MFDS accepts foreign CERs under the latest scope expansion (see 고시 제2025‑22호). For 3등급 fluoroscopy: **Korean clinical trial** or a locally performed post‑market clinical follow‑up (PMCF) is required. | FDA “510(k)” predicate data, EU MDR Art. 61 CER |
| **Labeling & IFU** | All labeling, instructions for use, and safety information must be in **Korean language**, include the KGMP certification mark, and display the correct 품목분류번호 (A11000 series). No foreign‑language label may appear as primary text. | ISO 13485 labeling clause |
| **Safety & Non‑clinical Testing** | Biocompatibility per **ISO 10993‑1:2018**, electrical safety per **IEC 60601‑1:2005+A1:2012+A2:2020**, and radiation safety data (dose, shielding) according to the Korean Radiation Safety Act. | Same IEC/ISO standards |
| **Post‑Market Surveillance (시판후조사)** | PMS plan describing adverse event reporting, periodic safety update (한국식 PSUR), and field corrective action procedures. | EU MDR PSUR analogy (for reference only) |

*Citation*: The inclusion of IEC 62304 and the cyber‑security note are directly taken from **Chunk 2** (“SW 밸리데이션 – IEC 62304:2006+A1 전면 참조 편입”; “사이버보안 – 적용 가능 시 사이버보안 관리 요구 (부속서 참조)”). The 고시 number **제2025‑22호** is also cited from Chunk 2.

---

### 3. Identified Gaps / Missing Information  

| Gap | Why it matters | Action needed |
|-----|----------------|---------------|
| **Exact sub‑type to be marketed** (diagnostic X‑ray vs fluoroscopy) | Determines whether the pathway is 인증 or 허가 and drives clinical evidence requirements. | Confirm product line and map each to the appropriate 품목분류번호/grade. |
| **Local Clinical Evidence for 3등급 fluoroscopy** | MFDS still requires Korean clinical data for high‑risk (3~4등급) devices. | Plan a Korean‑centric clinical study or obtain local CE‑MDR data that satisfies MFDS criteria. |
| **Cybersecurity Management Plan** | 고시 제2025‑22호 allows optional cyber‑security requirements; absence may be questioned in a security audit. | Draft a cybersecurity risk management file referencing the MFDS 부속서. |
| **Korean Language IFU & Labeling Samples** | Must be submitted for review; missing drafts will delay 심사. | Prepare Korean translations of all labeling, include product identifiers (A11000 series) and KGMP mark. |
| **Radiation Dose Validation Report** | Specific to X‑ray devices; required under the Radiation Safety Act but not listed in source excerpts. | Generate/testing report per Korean NIRB guidelines. |

---

### 4. Core Risk Controls (ISO 14971:2019)  

| Hazard | Control Measure | Evidence |
|--------|-----------------|----------|
| **Radiation exposure exceeding limits** | Built‑in dose‑limiting circuitry, automatic shut‑off, user training program. | Design validation data; risk analysis file. |
| **Electrical shock / fire** | IEC 60601‑1 compliance, double insulation, fault detection. | Test certificates (IEC 60601‑1). |
| **Software malfunction** | IEC 62304‑based development lifecycle, periodic software updates with verification. | Software validation report (IEC 62304). |
| **Cyberattack leading to unauthorized exposure settings** | Cybersecurity plan (network segmentation, authentication, audit logs). | Cybersecurity management file per 고시 제2025‑22호 부속서. |
| **Incorrect labeling leading to misuse** | Korean‑only labeling with clear pictograms; verification of translation accuracy. | Final IFU/label set for 심사. |

---

### 5. Citations  

| Type | Reference |
|------|-----------|
| **Framework (ISO/IEC)** | ISO 14971:2019, ISO 13485:2016, IEC 62304:2006+A1, IEC 60601‑1:2005+A1:2012+A2:2020, ISO 10993‑1:2018 |
| **Instance Identifier – 고시** | 고시 제2025‑22호 (see Chunk 2) |
| **Instance Identifier – 품목분류번호** | A11000 진단용 엑스선 장치 series; A11110.01‑03 (2등급), A11040.01/02 (3등급) – corrected in audit #1068 (Chunk 1) |
| **Regulatory source** | law.go.kr 「의료기기 품목 및 품목별 등급에 관한 규정」[별표 1] – referenced in Chunk 1 |

*No other specific notice or article numbers appear in the provided excerpts; for any additional pinpoint references, verification is required.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason | Recommended escalation |
|--------|--------|-------------------------|
| **Unclear product sub‑type (diagnostic vs fluoroscopy)** | Determines grade and submission track. | Escalate to senior RA lead for classification confirmation before dossier assembly. |
| **Absence of Korean clinical data for 3등급 component** | MFDS will reject without it. | Prompt the Clinical Development team to initiate local study; inform Project Manager of schedule impact. |
| **Cybersecurity plan not yet drafted** | High‑risk devices with network capability may be flagged during 인증/허가 audit. | Alert the CISO / Cyber‑Security specialist to produce a compliance package within 2 weeks. |
| **Labeling drafts missing Korean translation** | Will cause 심사 stop‑order. | Assign regulatory affairs writer; notify Quality Assurance for proof‑reading. |
| **Radiation safety test results pending** | Mandatory under Radiation Safety Act; omission leads to non‑conformity. | Notify R&D engineering lead; request expedited testing. |

---

### 7. Peer Review Prompt  

> **RA peer, please review:**  
> 1. The assumption that the A11110 series qualifies as 2등급 and A11040 series as 3등급—does the current “품목분류표” (별표 1) support this mapping?  
> 2. Whether the foreign CER acceptance under 고시 제2025‑22호 indeed applies to diagnostic X‑ray devices of 2등급, or if additional Korean data are still required.  
> 3. The completeness of the cybersecurity evidence list given that the 고시 only “allows” cyber security requirements when applicable—should a full management plan be submitted proactively?  

--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

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

> ① A11040(투시)를 "3등급"으로 기재 — 소스는 A11040.01/.02 [2]=2등급으로 표기(소스 불일치) ② "고시 제2025-22호"를 외국 CER 인정 근거로 인용 — 동 고시는 품목군·제조·품질관리 개정 고시로 CER 인정과 무관(11-02 kr-004와 동일 오류 계열). / **1점 확정**(shadow 수용·강화): ① A11040(투시) '3등급' — 소스 명시 [2]=2등급 ② 고시 제2025-22호를 외국 CER 인정 근거로 인용 — 동 고시는 품목군·GMP 개정 고시(11-02와 동일 오류 재발) ③ 잘못된 3등급 전제 위에 '한국 임상시험 필수' 요건 창작 — 소스 불일치+오귀속+창작의 복합. 예외 조항 발동.

**Source Excerpts**

1. Chunk `1069373523805353088`

> ## 개정 이력 | 버전 | 일자 | 내용 | 작성 | |------|------|------|------| | v0.2 | 2026-05-07 | GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려사항 추가 | — | | v0.2.1 | 2026-09-25 | **audit #1068 정정** — §7 X-ray 품목 분류번호 'A10030(2등급)/A10040(3등급)'(미존재·A10000=보육기 오귀속)→**A11000 진단용 엑스선 장치** 계열(A11110.01~.03 [2], 투시 A11040.01/.02 [2])로 교체. '품목군'(GMP 고시)과 '품목 분류번호'(등급규정 별표 1) 구분 표기. 근거: law.go.kr 「의료기기 품목 및 품목별 등급에 관한 규정」 [별표 1] 원문 | md-process-builder |

2. Chunk `1127747106119376174`

> ## 2. 최신 개정 핵심 (고시 제2025-22호) | 항목 | 종전 | 개정 | |------|------|------| | 품목군 분류 | 26개 | 64개 | | 융복합의료기기 | 불명확 | 주된 기능이 의료기기이면 심사대상 명확화 | | 심사체계 | 복수심사 | 품질관리심사기관 단독심사 가능 | | 제출자료 | 광범위 | 간소화 | | SW 밸리데이션 | IEC 62304 참조 일부 | IEC 62304:2006+A1 전면 참조 편입 | | 사이버보안 | 미규정 | 적용 가능 시 사이버보안 관리 요구 (부속서 참조) |

### kb-eval-20261105-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-05", "decision_ref": "kb-eval-20261105-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "757da8642b01f8e0", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "05655bb796bf8ed73e0e7bf66100bca6738bee82ab80865741516d55798597da"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `757da8642b01f8e0`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/GMP_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `05655bb796bf8ed73e0e7bf66100bca6738bee82ab80865741516d55798597da`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `README.md`는 KGMP 또는 GMP evidence readiness, audit readiness, QMS 절차·기록 관련 문서입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-07-13 (주간모니터 #8 — KGMP 적합성인정 제도 개편, 2026-07-01 시행 반영) > 근거: https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287877&type=HTML (의료기기법 시행규칙, 총리령 제2127호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287221&type=HTML (의료기기법 시행령, 대통령령 제36445호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=admrul&ID=210...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – KGMP Evidence‑Readiness (2026 July 1 Reform)**  

---

### 1. Device Classification & Submission Route  
| Item | Requirement | Current knowledge from source |
|------|-------------|------------------------------|
| **Grade (1~4등급)** | Must be determined according to the “의료기기 품목 및 품목별 등급에 관한 규정”. | *No specific grade is provided in the excerpts – verify separately.* |
| **Submission track** | ① 1등급 → 신고 ② 2등급 → 인증 (MFDS‑designated 심사기관) ③ 3·4등급 → 허가 | Dependent on the confirmed grade. |

> **Action:** Obtain the official product‑grade determination before proceeding to pathway selection.

---

### 2. Core Regulatory Framework (KGMP) – Post‑July 1 2026  
| Source excerpt | Legal / regulatory citation (instance identifier) |
|----------------|---------------------------------------------------|
| “의료기기법 제28조·제28조의2~4” | **Medical Device Act, Articles 28 & 28‑2~4** – basis for conformity‑recognition system and designation of reviewing bodies. |
| “의료기기법 시행규칙 제48조~48조의4” | **Enforcement Decree, Articles 48–48‑4** – procedures for application, renewal, examiner assignment, cancellation reasons. |
| “의료기기 제조 및 품질관리 기준” (고시 제2026‑46호) | **MFDS Notice No. 2026‑46** – GMP assessment criteria (remains in force after partial amendment). |
| “의료기기 제조 및 품질관리 관련 기관 지정 등에 관한 규정” (고시 제2026‑47호) | **MFDS Notice No. 2026‑47** – establishes designated 심사기관, 심사원 and education institutions; introduces new checklist forms (별지 제38호의4·39·40호). |

These four citations constitute the **complete statutory envelope** for KGMP certification under the July 1 2026 reform.

---

### 3. Evidence Package Required for KGMP Certification  

| Evidence Element | Reference Requirement | Typical Content |
|------------------|----------------------|-----------------|
| **QMS Manual & SOPs** | 고시 제2026‑46호 (GMP criteria) | System description, organizational chart, document control, change management. |
| **Process Validation/Qualification Records** | 고시 제2026‑46호 – “제조 공정·품질관리 기준” | Installation Qualification (IQ), Operational Qualification (OQ), Performance Qualification (PQ) for critical equipment. |
| **Risk Management File** | ISO 14971:2019 (framework reference) + 고시 제2026‑46호 (risk controls required in GMP) | Hazard analysis, risk evaluation, mitigation measures, residual risk assessment. |
| **Device Master Record / Technical Documentation** | MFDS submission rules (grade‑dependent) – not explicitly listed in the source but required for any certification/approval. |
| **Korean Labeling & IFU** | MFDS labeling regulations (framework reference) – must be in Korean, include product name, intended use, warnings, etc. |
| **Facility Inspection Checklist** | 별지 제38호의4·39·40호 (new KGMP application forms) – to be completed and submitted with the application. |
| **Personnel Qualification Records** | 고시 제2026‑47호 – designation of education institutions & examiner qualifications. |
| **Audit / Self‑Assessment Report** | 고시 제2026‑46호 – demonstrating compliance against GMP criteria. |

> **Missing Information:**  
> • Confirmed device grade (1~4등급).  
> • Whether local clinical data are mandatory (depends on grade and risk profile).  
> • Completed forms 별지 제38호의4·39·40호 for the specific product.  

---

### 4. Key Risk Controls to Align with KGMP  

1. **Documented Risk Management** per ISO 14971:2019, integrated into QMS (required by 고시 제2026‑46호).  
2. **Process Control & Monitoring** – critical parameters recorded in real time; deviations investigated per SOPs.  
3. **Supplier Qualification** – maintain approved supplier list with audit records; align to GMP criteria.  
4. **Change Management** – impact analysis of any design or process change, approval workflow documented.  

---

### 5. Human‑Escalation Triggers (when to involve senior RA / MFDS liaison)  

| Trigger | Reason | Escalation Action |
|---------|--------|-------------------|
| **Unidentified device grade** | Cannot select correct submission track; may cause non‑conformity. | Pause dossier preparation; request formal grade determination from the “의료기기 품목 및 품목별 등급에 관한 규정” authority. |
| **Absence of Korean labeling/IFU** | MFDS mandates Korean language for all marketing materials. | Engage translation & regulatory affairs team to produce compliant labels before submission. |
| **Incomplete checklist (별지 제38호의4·39·40호)** | Submission will be rejected at initial screening. | Assign senior RA to review and complete missing sections; confirm with designated 심사기관 if needed. |
| **Requirement for local clinical data not addressed** | For 3등급·4등급 devices, lack of Korean clinical evidence leads to denial. | Initiate feasibility study or seek exemption justification from MFDS. |
| **Discrepancy between GMP audit findings and 고시 제2026‑46호 criteria** | Potential failure during on‑site inspection. | Convene a corrective action meeting; involve quality assurance manager and senior RA to remediate gaps. |
| **Designation of 심사기관 not secured** (new requirement under 고시 제2026‑47호) | Application cannot be routed without an approved examiner. | Contact MFDS designated 기관 to obtain approval; document communication. |

---

### 6. Summary Judgment  

*The KGMP evidence package must be built around the July 1 2026 regulatory framework defined by **고시 제2026‑46호** (GMP criteria) and **고시 제2026‑47호** (designation of examining bodies & new application forms). The essential first step is to verify the device’s grade (1~4등급) under the “의료기기 품목 및 품목별 등급에 관한 규정”. Once the grade is known, the corresponding submission route (신고 / 인증 / 허가) can be selected and a complete dossier—including QMS documentation, risk‑management file, Korean labeling, and the newly required checklist forms—prepared. Any missing element or uncertainty triggers immediate escalation to senior RA personnel.*  

---

### 7. Peer Review Prompt  

> *Please review this draft for: (a) completeness of KGMP evidence items relative to 고시 제2026‑46/47호; (b) any overlooked Korean‑specific obligations (e.g., post‑market surveillance, labeling nuances); and (c) gaps where the source does not provide a concrete identifier (grade, local clinical data requirement). Suggest additional documentation or clarification needed before submission.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1051643482212217538`

> > 최종 갱신: 2026-07-13 (주간모니터 #8 — KGMP 적합성인정 제도 개편, 2026-07-01 시행 반영) > 근거: https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287877&type=HTML (의료기기법 시행규칙, 총리령 제2127호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287221&type=HTML (의료기기법 시행령, 대통령령 제36445호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=admrul&ID=2100000281580&type=HTML (고시 제2026-46호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=admrul&ID=2100000281582&type=HTML (고시 제2026-47호, 신설) # 국내 MFDS - GMP 심사자료

2. Chunk `528323066343451536`

> ## 핵심 문서 (2026-07-01 개편 후 체계) - 「의료기기법」제28조·제28조의2~4 (적합성인정·심사원·기관지정 근거, 개정 법률 제21263호 2025-12-30 공포) - 「의료기기법 시행규칙」제48조~48조의4 (신청·갱신·심사원·취소사유, 총리령 제2127호 2026-07-01 시행) - 「의료기기 제조 및 품질관리 기준」 (식약처 고시 제2026-46호, 2026-07-01 일부개정 — GMP 심사기준만 존치) - 「의료기기 제조 및 품질관리 관련 기관 지정 등에 관한 규정」 (식약처 고시 제2026-47호, 2026-07-01 제정·신규 — 심사기관·심사원·교육기관 지정) - KGMP 심사 신청서 양식 및 제출서류 체크리스트 (신규 서식: 별지 제38호의4·39·40호)
