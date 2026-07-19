# KB Eval Checksheet - 2026-07-23 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260723-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_us-001", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "56f0a9dd295f8e5c", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md", "source_hash": "b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `56f0a9dd295f8e5c`
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

> **Regulatory Draft – Evidence Gap Analysis & Submission Roadmap**

---

### 1. Bottom‑Line Recommendation  
| Item | Decision |
|------|----------|
| **Regulatory pathway** | Premarket Notification (510(k)) – most likely **Class II** under **21 CFR 807**. If the device’s intended use, risk profile, or technology aligns with an EU **Class IIb/III** product, a **de Novo** request may be required; however, based on typical U.S. classification of comparable imaging/AI software, a 510(k) is expected to be acceptable. |
| **Predicate device** | Identify a cleared 510(k) that matches the device’s intended use, technology (e.g., AI‑assisted image analysis), and performance claims. Predicate selection will drive the substantive content of the “substantial equivalence” argument. |
| **Primary regulatory citations** | • **21 CFR 807** – Premarket notification requirements (submission format, labeling, UDI). <br>• **21 CFR 820** – Quality Management System (QMS) compliance (ISO 13485‑aligned QMSR effective 2026‑02). <br>• **21 CFR 892.2050** (if the device is a medical image management/processing system). <br>• **ISO 14971:2019** – Risk Management for medical devices. <br>• FDA Guidance “FDA and Industry Actions on 510(k) Submissions” (Oct 2022) – additional information (AI) response strategy. |
| **Evidence‑gap priority** | 1️⃣ GSPR (General Safety & Performance Requirements) substantiation – *missing*. <br>2️⃣ Clinical‑evaluation equivalence data – *insufficient*. <br>3️⃣ Post‑Market Clinical Follow‑up (PMCF) plan – *absent*. <br>4️⃣ Risk‑management file (ISO 14971) – *non‑conforming/ incomplete*. |

---

### 2. Required Evidence & Current Deficiencies  

| Regulatory Requirement | Expected Content (US) | Gap Identified in Source | Action Needed |
|------------------------|-----------------------|--------------------------|---------------|
| **General Safety & Performance Requirements (GSPR)** | Demonstrate that the device meets all applicable FDA performance standards, including intended‑use testing, software validation, and cybersecurity. | “GSPR 입증 근거 부족” (lack of GSPR evidence) – cited in EU MDR deficiency note. | Prepare a comprehensive GSPR matrix mapping each FDA safety/performance criterion to supporting data (bench, animal, clinical). |
| **Clinical Evaluation / Equivalence** | - Clinical performance data or a well‑justified equivalence comparison with the predicate.<br>- Statistical analysis of sensitivity/specificity, ROC curves, etc. | “Clinical Evaluation 동등성 불충분” – noted as a common deficiency. | Conduct a formal clinical‐evaluation report (CER) that includes: <br> • Study protocol & IRB approval.<br> • Patient demographics, endpoints, statistical plan.<br> • Direct comparison to predicate device performance. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | Detailed PMCF strategy (study design, timelines, risk mitigation, data collection) consistent with FDA’s post‑market surveillance expectations (21 CFR 822). | “PMCF 계획 미비” – absent in source. | Draft a PMCF plan outlining: <br> • Surveillance objectives.<br> • Real‑world evidence sources (registries, EHR).<br> • Interim reporting triggers. |
| **Risk Management File (ISO 14971)** | • Hazard analysis, risk evaluation, risk control measures, residual risk justification.<br>• Updated throughout design lifecycle. | “위험관리파일 ISO 14971 부적합” – flagged as non‑conforming. | Update the risk‑management file: <br> • Perform Failure Modes & Effects Analysis (FMEA).<br> • Document all mitigations and verify their effectiveness.<br> • Align with FDA’s “Software Pre‑market Guidance for AI/ML Devices” where applicable. |
| **Quality Management System (QMS)** | Demonstrate compliance with the QMSR (21 CFR 820) and ISO 13485:2016 (or later). | Not explicitly mentioned, but implied by EU MDR NB review; assume current QMS needs verification against U.S. expectations. | Conduct a gap analysis of the existing QMS vs. 21 CFR 820 & ISO 13485; implement required SOP updates (design controls, document management, complaint handling). |
| **Labeling & UDI** | • Device label compliant with 21 CFR 801.<br>• UDI on labeling and packaging per 21 CFR 830. | Not discussed in source excerpts – presumed missing. | Prepare full labeling set (label, IFU, promotional material) and generate a compliant UDI (Device Identifier + Production Identifier). |
| **Software Validation & Predetermined Change Control Plan (PCCP)** (if AI/ML) | • Verification & validation documentation.<br>• PCCP outlining allowable post‑market algorithm updates. | No direct reference; however, FDA’s “Additional Information” guidance emphasizes readiness for AI‑related queries. | Develop a software validation plan and, if applicable, a **Predetermined Change Control Plan (PCCP)** per the Dec 2024 FDA Guidance. |

> **Citation note** – The source excerpts did not contain any specific device numbers, docket IDs, or regulation article citations; therefore no instance identifiers are provided here. Verify any needed identifiers separately.

---

### 3. Risk Controls to be Documented  

| Control Category | Example Measures (to be included in submission) |
|------------------|-----------------------------------------------|
| **Design‑Control** | Design history file (DHF), design verification/validation protocols, traceability matrix linking requirements to test results. |
| **Software Assurance** | Code reviews, static analysis, unit/integration testing, cybersecurity threat model, IEC 62304 compliance evidence. |
| **Human Factors** | Usability engineering report, formative and summative validation studies (per FDA Human‑Factors Guidance). |
| **Post‑Market Surveillance** | PMCF plan, adverse event monitoring procedures, periodic safety update reports (PSUR) aligned with 21 CFR 822. |
| **Manufacturing Controls** | Process validation records, incoming inspection SOPs, sterilization (if applicable), environmental controls. |

---

### 4. Human‑Escalation Triggers  

| Trigger Condition | Escalation Action |
|--------------------|-------------------|
| **Critical evidence gap remains unresolved ≥ 30 days** (e.g., no clinical equivalence data) | Senior RA sign‑off required; consider filing an FDA “Request for Information” (RFI) pre‑submission meeting. |
| **Risk‑management file fails ISO 14971 audit** | Pause submission build; involve Quality & Regulatory Lead to remediate before proceeding. |
| **Predicate device cannot be identified or is not substantially equivalent** | Initiate De Novo pathway assessment; engage regulatory counsel for classification appeal. |
| **Significant changes to algorithm after 510(k) clearance are anticipated** | Draft and submit a **Predetermined Change Control Plan (PCCP)**; obtain FDA concurrence before implementation. |
| **Unresolved UDI/Labeling non‑compliance** | Escalate to Labeling Specialist and QMS Manager; issue go/no‑go decision for filing. |

---

### 5. Peer‑Review Prompt  

> *“Please review the above assumptions regarding classification, the selection of a 510(k) route versus De Novo, and the identified evidence gaps. Confirm that no relevant FDA guidance (e.g., AI/ML SaMD Guidance, Cybersecurity Recommendations) has been omitted, and flag any jurisdiction‑specific items that may still be missing from our gap analysis.”*

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

1. Chunk `1062884112493939033`

> ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합

2. Chunk `1076622801663602202`

> > 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: https://www.fda.gov/media/73507/download (FDA Guidance: FDA and Industry Actions on 510(k) Submissions, Oct 2022) | https://medicaldeviceacademy.com/additional-information-request/ | https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process | MDUFA V Commitment Letter https://www.fda.gov/media/158308/download # FDA Additional Information (AI) 대응 전략 및 샘플 답변 체계

### kb-eval-20260723-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_us-002", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "64feae2a34a29c41", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `64feae2a34a29c41`
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

> **Regulatory Draft – Determining the Correct Premarket Pathway & Evidence Package**

---

### 1. Bottom‑Line Recommendation (what you need to decide now)

| Device Profile (assumed) | Likely FDA Classification | Recommended Premarket Route |
|--------------------------|---------------------------|-----------------------------|
| Class I or II medical device that **does not introduce a new intended use, technology, or biological risk** relative to an existing cleared product | Class I‑II (21 CFR 892 §§2050–2040 for imaging; other panels as appropriate) | **510(k) – Substantial Equivalence** (if a suitable predicate exists) |
| Same as above **but no legally marketed predicate** (new technology or novel indication) | Class I‑II (new device type) | **De Novo Classification Request** |
| Device intended for **Class III** risk level, or a Class I/II that requires **clinical data to demonstrate safety & effectiveness** (e.g., implantable, life‑supporting, high‑risk software) | Class III | **PMA** |

*Apply the decision matrix in Source [2] “경로별 규제 근거 요약” – see rows for “대상 등급”, “Predicate 필요”, and “임상데이터”.*

---

### 2. Evidence Required per Pathway  

| Requirement | 510(k) | De Novo | PMA |
|-------------|--------|----------|-----|
| **Legal Authority** | FD&C Act §510(k), 21 CFR 807 (Source [2]) | FD&C Act §513(f)(2), 21 CFR 860 (Source [2]) | FD&C Act §515, 21 CFR 814 (Source [2]) |
| **Predicate Device** | Mandatory – must identify a legally marketed device with the same intended use and technology (Source [2] “Predicate 필요: 필수”) | Not required (Source [2] “Predicate 필요: 불필요”) | Not required (Source [2] “Predicate 필요: 불필요”) |
| **Clinical Data** | Conditional – only when needed to resolve a “clinical question” defined in §3 of the FDA guidance on clinical data requirements (Source [2] “임상데이터 | 조건부 (§3 참조)”) | “If applicable”; typically required for new technology or risk claim (Source [2]) | Mandatory – must include well‑designed clinical study(s) (Source [2] “임상데이터 | 필수”) |
| **Performance Benchmarks** | Benchtop, animal testing, and/or limited human factors as appropriate; may be waived if data already exist in predicate | Device‑specific performance testing plus any risk‑based validation that cannot be demonstrated by bench work alone | Full preclinical & clinical safety/effectiveness data package (PMA) |
| **Risk Management** | ISO 14971:2019 (or later) aligned with QMSR, 21 CFR 820 (effective Feb 2026) – documented in Design History File | Same as 510(k), but must also address any novel risks not covered by existing guidance | Same as De Novo; additionally a Formal Risk Analysis Summary required for PMA Review |
| **Quality Management System** | Establishment registration & listing per 21 CFR 807; QMSR compliance expected (Part 820) | Same; De Novo applicants must submit a QMS summary (no eSTAR requirement) | Same; full QMS documentation required for FDA inspection |
| **User Fee (FY‑2025)** | ≈ $22,171 (Source [2]) | ≈ $46,875 (Source [2]) | ≈ $438,330 (Source [2]) |
| **Review Timelines** | Target 90 days (Source [2]) | ~150 review days (Source [2]) | Target 180 days (Source [2]) |
| **eSTAR Submission** | Mandatory from 2023‑10‑01 onward (Source [2]) | Mandatory from 2025‑10‑01 onward (Source [2]) | Not applicable (Source [2]) |

---

### 3. Evidence Gaps – What is Likely Missing

| Gap Category | Typical Missing Item | Impact on Pathway |
|--------------|---------------------|-------------------|
| **Predicate Identification** | No clear, legally marketed device with identical intended use & technology. | Forces move to De Novo (or PMA if Class III). |
| **Clinical Data Justification** | Lack of a documented “clinical question” that cannot be answered by bench/animal data. | May trigger FDA request for additional clinical evidence even in 510(k). |
| **Risk Management File** | Incomplete ISO 14971 risk analysis, especially for new software algorithms or AI/ML components. | Could delay clearance; may require a Predetermined Change Control Plan (PCCP) for post‑market modifications. |
> *Note: The PCCP mechanism is the FDA’s pre‑authorised change‑control plan for AI/ML devices (final guidance Dec 2024). It should be referenced if the device includes adaptive algorithms.*

| **Quality System Documentation** | No QMSR‐aligned SOPs, Design History File, or Device Master Record as required by 21 CFR 820 (effective Feb 2026). | Non‑compliance may lead to complete refusal of filing. |
| **UDI & Labeling** | Missing UDI label per 21 CFR 830 (no §830.10‑§830.60 evidence supplied). | FDA will issue a Refuse to Accept (RTA) letter. |
| **Human Factors / Usability** | No validated usability study for intended user population. | Especially critical for Class II/III devices; can be an RTA trigger. |

If any of the above items are absent, **escalate to senior regulatory lead** before submission.

---

### 4. Risk Controls & Mitigation Strategies (aligned with QMSR)

1. **Design Controls** – Follow 21 CFR 820.30; capture user needs, design inputs/outputs, verification, validation.
2. **Risk Management** – Conduct ISO 14971‑based risk analysis; generate a Residual Risk Report for submission.
3. **Predetermined Change Control Plan (PCCP)** – If AI/ML is involved, draft the PCCP now to streamline future updates (per FDA final guidance Dec 2024).  
   *Citation*: “Predetermined Change Control Plan (PCCP)” – FDA finalized guidance 12/2024.
4. **UDI Implementation** – Assign a device identifier per 21 CFR 830; submit the record to GUDID before filing.
5. **Human Factors Validation** – Perform formative and summative usability testing; include results in the “Human Factors Engineering” section of the submission.

---

### 5. Citations (per source)

| Item | Source Citation |
|------|-----------------|
| Legal bases for each pathway, classification targets, predicate requirement, clinical data need, fees, timelines, eSTAR duties | Table in Source [2] (“경로별 규제 근거 요약”) – includes FD&C Act §§ 510(k), 513(f)(2), 515; 21 CFR 807, 860, 814; fee amounts; review days. |
| Conditional clinical data requirement for 510(k) | “임상데이터 | 조건부 (§3 참조)” in Source [2] – indicates that §3 of the FDA guidance on clinical data determines when clinical data are needed. |
| List of FDA guidance documents (solid‑state X‑ray imaging, de‑novo, PMA clinical studies) | URLs listed in Source [1]; no specific section numbers supplied → **no specific identifier found in source – verify separately**. |
| Predetermined Change Control Plan (PCCP) reference | Mentioned in the developer instructions; not present in the excerpts – **no specific identifier found in source – verify separately**. |

---

### 6. Human‑Escalation Triggers

| Condition | Action Required |
|-----------|-----------------|
| No suitable predicate identified | Escalate to senior regulatory manager → consider De Novo or PMA strategy. |
| Clinical data need cannot be justified by a documented “clinical question” (per §3) | Pause submission; request clinical study plan and risk‑benefit justification before proceeding. |
| Incomplete QMSR documentation (21 CFR 820) after February 2026 deadline | Halt filing; engage quality assurance lead to close gaps. |
| Missing UDI or labeling per 21 CFR 830 | Issue a “Refuse to Accept” risk → submit corrective label package before resubmission. |
| AI/ML component without a drafted PCCP | Notify device development team; draft PCCP immediately; do not file until approved by regulatory lead. |
| Any discrepancy between the evidence package and the selected pathway’s statutory requirements (e.g., trying to clear a Class III device via 510(k)) | Immediate escalation to senior RA & legal counsel; re‑evaluate classification. |

**Decision Point:** If any trigger fires, stop the submission workflow and open a “Regulatory Gap Review” work package for senior review.

---

### 7. Peer‑Review Prompt

> *“Colleague, please challenge the assumptions made above:*
> 
> - *Is the conditional clinical data requirement correctly interpreted based on §3 of the FDA guidance?*  
> - *Does the evidence gap list capture all items needed for a solid‑state X‑ray imaging device (if that is our product)?*  
> - *Are there any jurisdiction‑specific nuances—such as state‑level requirements or recent guidance updates—not reflected in the source excerpts that could affect our pathway choice?”*

--- 

**End of Draft**

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

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20260723-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_us-003", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "85c0ee79c16fe2d9", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_PreSubmission_QSub_가이드.md", "source_hash": "417191845804e82051a123525f91ed116a02c2eba4f516018604d1460525c8f5"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `85c0ee79c16fe2d9`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_PreSubmission_QSub_가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/FDA_PreSubmission_QSub_%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `417191845804e82051a123525f91ed116a02c2eba4f516018604d1460525c8f5`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `FDA_PreSubmission_QSub_가이드.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 3.1 Cover Letter (표지 서한) | 필드 | 내용 | |---|---| | 제목 | "Pre-Submission for [Device Name]" | | 회사명, 주소 | 정식 등록 정보 | | Primary Contact | 이름, 직함, 전화, 이메일 | | Regulatory Contact | 담당 RA 담당자 | | 제출 목적 | 한 문단 (어떤 피드백이 필요한가) | | 계획 중인 제출 유형 | 예: "510(k) 제출 예정" / "IDE 신청 전 SRD 요청" | | 회의 요청 여부 | 서면 피드백만 / 회의 병행 중 선택 | ## 7. 3개 지역 Pre-Sub 동등 제도 비교 | 항목 | FDA (미...
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

> **Regulatory Draft – Pre‑Submission Planning for an X‑ray Imaging Device**

---

### 1. Bottom‑Line Recommendation  
- **Classification:** Class II medical imaging device governed by **21 CFR Part 892** (radiology/imaging). The exact subsection (e.g., §892.1470) must be confirmed once the intended use and technology are defined.  
- **Primary pathway:** Traditional **510(k) Premarket Notification**. Initiate a **FDA Pre‑Submission (Q‑Sub)** 6–12 months before the planned 510(k) filing – this is now considered “best practice” for X‑ray devices (see Table in source [2]).  

---

### 2. Required Evidence Package (per 21 CFR §§807, 820, 830 and FDA guidance)

| Element | What to submit | Reason |
|---------|----------------|--------|
| **Device description** – intended use, indications, technology, specifications | Narrative + block diagram | Basis for predicate search & classification |
| **Predicate comparison** – side‑by‑side table (device name, 510(k) number, similarities/differences) | Identify at least one legally marketed device of the same classification | Demonstrates substantial equivalence (21 CFR 807.92) |
| **Performance testing** – bench, electrical safety (IEC 60601‑1), radiation safety (IAEA/ANSI standards), image quality (e.g., phantom studies) | Test reports, statistical analysis | Shows device meets applicable performance standards for X‑ray equipment |
| **Software validation (if applicable)** – Verification & Validation plan, source code control, cybersecurity risk assessment | Documentation per 21 CFR 820.30 & FDA’s “Predetermined Change Control Plan (PCCP)” guidance (Dec 2024) | Required for any software component; PCCP enables pre‑authorised post‑market updates |
| **Risk Management** – ISO 14971‐based hazard analysis, mitigations, and residual risk evaluation | Risk management file | Supports safety claims required in the 510(k) and under Part 820.30 |
> *Citation*: No specific identifier found in source — verify separately for exact FDA guidance documents (e.g., “Guidance for Industry: Content of Premarket Submissions for Management of Cybersecurity”).  

| **Labeling & IFU** – device name, intended use, contraindications, warnings, UDI placement | Draft labeling per 21 CFR 801 and UDI data sheet (Part 830) | Mandatory for clearance |
| **Quality System Evidence** – copy of QMS manual, design history file, production process validation | Demonstrates compliance with Part 820 and the new QMSR (effective Feb 2026, ISO‑13485 aligned) | Required for 510(k) supporting documentation |
| **Sterilization / Biocompatibility (if applicable)** – ISO 10993 data | If device contacts patient | Evidences safety of materials |
| **Clinical data (if needed)** – limited clinical study or literature support | When performance cannot be demonstrated solely by bench testing | May be required for novel X‑ray modalities |

---

### 3. Gaps Identified From Current Documentation  

| Missing / Unclear Item | Impact on Submission | Suggested Action |
|------------------------|----------------------|------------------|
| **Device name & precise intended use** (e.g., “portable chest radiography system”) | Prevents predicate identification and classification decision | Add to cover letter and 510(k) body; define clearly. |
| **Exact regulatory class subsection** (specific §892.xxxx) | Determines testing scope (radiation safety standards) | Conduct a class‑determination review using FDA product codes / CDRH database. |
| **Predetermined Change Control Plan (PCCP)** – not mentioned | If software/AI components are present, absence blocks post‑market flexibility | Develop PCCP per FDA Dec 2024 guidance; include in pre‑submission. |
| **UDI strategy** – label format, issuance agency, GUDID submission plan | Required under Part 830 for all Class II devices | Prepare UDI labeling mock‑up and draft GUDID submission. |
| **QMSR documentation** – alignment with ISO 13485 (effective 2026) | Non‑compliance will be flagged during 510(k) review | Update QMS to reflect new QMSR requirements; include evidence in pre‑submission. |
| **Risk analysis summary** – only high‑level hazards listed | Insufficient for FDA risk management expectations | Expand to full ISO 14971 risk file, map mitigations to design controls. |
| **Radiation safety test plan** – no reference to IEC/ANSI standards | May lead to additional FDA requests | Cite applicable standards (e.g., IEC 60601‑2‑33) and include test protocols. |

---

### 4. Risk Controls to Highlight in the Submission  

1. **Design Controls (21 CFR 820.30)** – requirement traceability matrix linking user needs → design inputs → verification/validation results.  
2. **Radiation Protection** – shielding calculations, dose measurements, compliance with IEC 60601‑2‑33 or FDA’s “Performance Standard for X‑ray Systems”.  
3. **Software Lifecycle Management** – use of PCCP for any AI/ML updates; version control, rollback procedures.  
4. **Cybersecurity** – threat modeling per FDA’s 2024 guidance, implementation of secure boot and data encryption.  
5. **Human Factors / Usability** – formative/usability testing to mitigate user error (relevant for positioning and exposure settings).  

---

### 5. Citations (per source excerpts)

| Item | Citation |
|------|----------|
| Cover‑letter content requirements (title, company info, purpose, submission type, meeting request) | Source [1] – “3.1 Cover Letter” table |
| FDA pre‑submission response targets (70 days written / 100 days with meeting) and recommendation to submit a Q‑Sub 6–12 months before a 510(k) for X‑ray devices | Source [2] – “X‑ray 특이사항” row & overall table |
| Comparison of pre‑submission processes across FDA, MFDS, MDR/NB (non‑binding nature, free cost, online portal) | Source [2] – “3개 지역 Pre‑Sub 동등 제도 비교” |

> No specific 510(k) numbers, CFR subsection IDs beyond the framework references were present in the excerpts; thus no device‑specific identifiers are included. Verify any detailed requirement citations (e.g., exact §892.xxxx) separately.

---

### 6. Human‑Escalation Triggers  

| Trigger | Why it warrants escalation |
|--------|-----------------------------|
| **Uncertain classification** (cannot assign a definitive §892 subsection) | May alter testing scope; requires senior regulatory sign‑off and possibly FDA clarification. |
| **No identified predicate or multiple candidates with significant differences** | Needs strategic decision on whether to pursue 510(k) vs. De Novo pathway – senior review required. |
| **Absence of PCCP for software/AI components** | Could delay clearance; escalation to the software engineering lead and regulatory manager. |
| **QMSR non‑conformance** (evidence that ISO 13485 alignment is missing) | Must be remedied before filing; involves quality assurance leadership. |
| **Inadequate risk management documentation** | Failure to satisfy ISO 14971 expectations; requires risk manager involvement. |
| **UDI plan not finalized** | UDI non‑compliance leads to FDA hold; senior RA must approve final labeling package. |

When any of the above triggers are detected, **immediately notify the Project Lead** and create a *Work Package* comment recommending review and potential re‑scope before proceeding with the Q‑Sub submission.

---

### 7. Peer Review Prompt  

> **@RA‑Team – please challenge:**  
> 1. The assumption that a traditional 510(k) is the optimal pathway given the device’s X‑ray technology—could a De Novo route be more appropriate?  
> 2. Whether the evidence list above fully reflects the latest FDA “Radiation Safety” guidance (2025 update).  
> 3. If any additional regional pre‑submission considerations (e.g., MFDS or EU NB) affect our U.S. submission timeline or data package.  

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

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `124523812258860464`

> ### 3.1 Cover Letter (표지 서한) | 필드 | 내용 | |---|---| | 제목 | "Pre-Submission for [Device Name]" | | 회사명, 주소 | 정식 등록 정보 | | Primary Contact | 이름, 직함, 전화, 이메일 | | Regulatory Contact | 담당 RA 담당자 | | 제출 목적 | 한 문단 (어떤 피드백이 필요한가) | | 계획 중인 제출 유형 | 예: "510(k) 제출 예정" / "IDE 신청 전 SRD 요청" | | 회의 요청 여부 | 서면 피드백만 / 회의 병행 중 선택 |

2. Chunk `367708542439035920`

> ## 7. 3개 지역 Pre-Sub 동등 제도 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR/NB (유럽) | |---|---|---|---| | 제도명 | Pre-Submission (Q-Sub) | 사전상담 (제조·수입업 허가 전 상담) | NB Early Dialogue / Scientific Advice | | 법적 구속력 | 없음 (non-binding) | 없음 (참고 의견) | 없음 (NB opinion) | | 응답 목표 | 70일 (서면) / 100일 (회의) | 명시 없음 (통상 수 주) | NB별 상이 (30~90일) | | 비용 | 무료 (PDUFA/MDUFA 포함) | 무료 | NB 과금 (별도 견적) | | 온라인 제출 | CDRH Portal (PreSTAR) | 민원24 / 온라인 신청 [검증 필요] | NB 시스템별 상이 | | 제출 빈도 제한 | 없음 (단, 과도한 중복 질문 지양 권고) | 없음 | NB별 상이 | | X-ray 특이사항 | CDRH 방사선 부서(OSB) 담당 | 의료기기안전국 체외진단기기과 [검증 필요] | NB 방사선 전문 심사관 배정 | **자사 행동 지시 (3개 지역)**: - **FDA**: 510(k) 제출 6~12개월 전 Pre-Sub 1회 필수 고려 (시험...

### kb-eval-20260723-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "d2d1345b8aac7f73", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `d2d1345b8aac7f73`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_01_Device_Description_IFU.md)
- Source hash: `70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_01_Device_Description_IFU.md`는 FDA eSTAR device description 및 IFU 작성에 필요한 제품 설명·표시 정보 문서입니다.
- 현재 excerpt 핵심: ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA For...
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

> **Regulatory Draft – Radiographic Acquisition‑Control Software (GUI)  

1. Classification & Submission Pathway**  
- **Device class:** Likely **Class II** imaging device regulated under **21 CFR Part 892** (Radiology/Imaging). The exact subsection (e.g., §892.2050 – Medical image management and processing system, or §892.2030 – Medical image digitizer) must be confirmed against FDA product classification database.  
- **Submission route:** **Traditional 510(k)** (use of a cleared predicate is expected; no indication that the device qualifies for an abbreviated or special 510(k)).  

**2. Required Evidence & Documentation**  

| Requirement | Source / Basis | Expected Content |
|-------------|----------------|------------------|
| **Device Description** | FDA Guidance “Electronic Submission Template for Medical Device 510(k) Submissions” (2023); §892.xx (to be verified) | • Software architecture diagram (modules, processes, DB, DICOM nodes)<br>• Minimum OS & hardware specs<br>• Compatible detector/generator list (with versions)<br>• DICOM conformance statement (Storage SCU, Worklist SCU, MPPS, etc.) |
| **Intended Use** | FDA Form 3881; Guidance “General/Specific Intended Use” (1998) | Exact wording: *“intended for use by trained technologists to acquire, review, and manage digital radiographic images… not intended for primary diagnosis or image interpretation.”* |
| **Software Safety Classification** | IEC 62304 (referenced in source) | Declare software safety class (A/B/C). If class C, provide full life‑cycle processes. |
| **Cybersecurity Controls** | Source list “cybersecurity features (authentication, encryption, audit log)” | Provide SSP/SAFETY plan, threat model, mitigation strategy. |
| **SOUP Management** | Source mention of SOUP usage | Identify all third‑party components, versioning, risk assessment per IEC 62304 & ISO 14971. |
| **Performance Testing** (bench) | Implicit from 510(k) requirements (21 CFR 807.87) | • Image quality metrics (MTF, DQE, uniformity)<br>• Interoperability with X‑ray console and PACS<br>• Timing & latency measurements |
| **Risk Management** | ISO 14971 (implied) | Hazard analysis, risk control measures, residual risk evaluation. |
| **Usability Engineering** | IEC 62366‑1 (recommended) | Human factors validation for GUI controls, labeling of “review” vs “diagnosis”. |
| **Labeling & IFU** | 21 CFR 801; Form 3881 | Include intended use statement, contraindications, warnings about diagnostic claims. |
| **UDI Plan** | 21 CFR 830 (label must bear a UDI) | Assign device‑identifier, submit to GUDID, include labeling per §830.10–§830.60. |
| **Quality Management System Evidence** | QMSR (effective Feb 2026) – 21 CFR 820; ISO 13485 alignment | Copy of QMS certificate, SOPs for software development, change control (Predetermined Change Control Plan – PCCP). |

**3. Evidentiary Gaps Identified from Source**  

| Missing Item | Reason / Impact |
|--------------|-----------------|
| **Predicate device identification & 510(k) comparison matrix** | Required to demonstrate substantial equivalence; absent in source. |
| **Quantitative bench‑test data (image quality, interface performance)** | Needed for clearance; only a high‑level description is present. |
| **Clinical/Usability validation (if any)** | If intended use includes “review”, FDA may expect limited clinical evaluation – not described. |
| **UDI labeling details (device identifier, production identifier format)** | No UDI plan supplied. |
| **QMSR compliance documentation** | QMS evidence required for 2026 submissions; not referenced. |
| **Full risk management file (ISO 14971) and IEC 62304 life‑cycle deliverables** | Only high‑level statements appear. |
| **Exact Part 892 subsection** | Device’s functional classification needs confirmation before final submission routing. |

**4. Core Risk Controls (to be reflected in the 510(k) and PCCP)**  

1. **Software safety class C controls** – verification/validation, failure‑mode analysis per IEC 62304.  
2. **Cybersecurity** – authentication, role‑based access, encrypted DICOM transmission, audit log retention ≥ 1 year.  
3. **User interface safeguards** – Clear differentiation between “review” and “diagnosis”; mandatory user acknowledgement before image export.  
4. **SOUP risk mitigation** – component inventory, vulnerability monitoring, patch management plan.  
5. **Interoperability safety** – DICOM conformance testing to prevent data loss or misrouting.  

**5. Citations (per rules)**  

- **Framework references:** 21 CFR 807.87 (information required in a 510(k)); 21 CFR 807.92 (510(k) Summary format); 21 CFR 820 (QMSR); 21 CFR 830 (UDI requirements).  
- **Instance identifiers:** *no specific identifier found in source — verify separately* (e.g., predicate 510(k) number, exact §892 subsection).  

**6. Human‑Escalation Triggers**  

| Trigger | Action Required |
|--------|-----------------|
| Unconfirmed **Part 892 subsection** → Classification ambiguity | Flag for senior RA / FDA classification query. |
| No identified **predicate device** | Escalate to product team to locate appropriate cleared comparator; cannot proceed without it. |
| Missing **bench‑test data** or **clinical validation** | Require generation of performance study plan before submission drafting. |
| Absent **UDI plan** or **GUDID entry** | Initiate UDI working group; hold 510(k) until completed. |
| Incomplete **QMSR evidence** (ISO 13485/QMS certificates) | Pause submission until QMS audit/registration confirmed. |
| Unresolved **cybersecurity risk analysis** | Conduct detailed threat‑model review, then resume. |

---

### Peer Review Prompt  
> *Colleague RA, please evaluate the assumptions above: Is the classification under Part 892 appropriate for a radiographic acquisition‑control GUI? Are there any additional FDA guidance documents (e.g., “Medical Device Data Systems” guidance) that might affect the 510(k) pathway or evidence requirements? Also verify whether an abbreviated 510(k) could be justified given the available predicates.*  

---  

**Reusable RA Judgment (recorded for future reference)**  
- Radiographic acquisition‑control GUI software is typically a **Class II imaging device** under **21 CFR Part 892**; confirm exact subsection via FDA Product Classification database.  
- A **Traditional 510(k)** remains the fastest credible route when a suitable predicate exists; abbreviated pathways are unlikely unless the device is identical to an existing cleared software module.  
- Core submission evidence includes detailed software architecture, IEC 62304 safety class documentation, cybersecurity controls, SOUP inventory, risk management (ISO 14971), performance testing (image quality & DICOM interoperability), labeling with clear non‑diagnostic intent, UDI assignment, and QMSR compliance.  
- Missing predicate identification, quantitative bench data, clinical/usability validation, UDI plan, and full QMSR evidence must be resolved before filing.  

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

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

### kb-eval-20260723-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_us-005", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "164066096f05c2ab", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `164066096f05c2ab`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_03_Performance_Testing_Bench_Test.md)
- Source hash: `9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc`
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

> **Regulatory Draft – GUI Image‑Processing/Display Software (SaMD)**  

---

### 1. Classification & Submission Pathway  
| Element | Determination |
|---|---|
| **Device type** | Software as a Medical Device (SaMD) – image processing/visualization for radiology suites |
| **CFR Part / Section** | **21 CFR §892.2050** – Image Processing Software (Class II) |
| **Regulatory route** | Traditional 510(k) Premarket Notification (substantial‑equivalence) – *unless* a novel algorithmic function requires De Novo. |
| **Primary predicate** | To be identified (e.g., cleared “Image Viewer and Basic Processing” devices such as K123456). *Missing from source – verify separately.* |

---

### 2. Evidence Required for 510(k) Submission  

| Category | Required Deliverable (per FDA eSTAR guidance & 21 CFR §807) | Source‑based indication |
|---|---|---|
| **Device description** | Detailed Intended Use, Indications, Device Architecture diagram | – |
| **Predicate comparison** | Side‑by‑side table of functional, technological and performance attributes vs. selected predicate(s) | *Missing – verify separately.* |
| **Software Development Lifecycle** | IEC 62304 compliance evidence (processes, class assignment, verification/validation activities). The source already maps the software to Class B (basic processing) → IEC 62304 Class B. | IEC 62304 citation in source |
| **Risk Management** | ISO 14971 risk analysis file; risk control measures for hazards identified (e.g., incorrect image display, data corruption). | No specific identifier – verify separately |
| **Cybersecurity** | FDA “Cybersecurity in Medical Devices” guidance implementation plan: threat modeling, vulnerability mitigation, update strategy. | 2023‑09‑27 FDA Guidance cited |
| **Performance Testing (Software)** | Complete eSTAR Section G package (see source). Must include:<br>• Executive Summary of Validation<br>• SRS & SDS<br>• Requirements Traceability Matrix (RTM)<br>• Validation Plan & Report covering Unit, Integration, System and Performance tests<br>• Test datasets description and justification<br>• Anomaly/Defect log with resolution | eSTAR package structure shown in source |
| **Usability Engineering** | IEC 62366‑1 usability validation report demonstrating safe use by intended users (radiology technologists). | Not listed – missing |
| **Labeling & UDI** | 21 CFR §801 labeling content; 21 CFR §830.10–.30 UDI placement on label and inclusion in GUDID. | No specific identifier – verify separately |
| **Quality Management System** | Evidence of compliance with **21 CFR Part 820** (QMSR, ISO 13485‑aligned). Include Design History File (DHF) sections referenced in eSTAR. | Part 820 citation (framework) |
| **Software Documentation for Post‑Market** | Predetermined Change Control Plan (PCCP) if any AI/ML components are present; otherwise a Software Change Management Procedure. | No AI/ML mentioned – confirm absence |

---

### 3. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Recommended Action |
|---|---|---|
| **Predicate device(s)** not identified in the source. | Required to demonstrate substantial equivalence; without it, 510(k) cannot be cleared. | Conduct market search, select at least one FDA‑cleared predicate, and prepare comparison matrix. |
| **Usability/Human Factors documentation** absent. | Needed for Class II SaMD to show safe use under intended conditions. | Perform formative/validation usability study; produce IEC 62366 report. |
| **Cybersecurity risk assessment details** only referenced generically. | FDA expects a documented threat model and mitigation strategy. | Develop and attach Cybersecurity Risk Management Plan per 2023‑09‑27 Guidance. |
| **UDI implementation plan** not mentioned. | Mandatory for all Class II devices marketed after Feb 2026. | Draft UDI labeling spec, submit to GUDID, reference in 510(k). |
| **Complete Validation Dataset description** – only file name listed (Validation_Dataset_Description.pdf) without content outline. | FDA will review dataset relevance, size, diversity, and ground‑truth methodology. | Populate the document with dataset characteristics, source, labeling process, statistical justification. |
| **Change Control / PCCP** – not indicated. | If future algorithm updates are anticipated, a PCCP must be submitted. | Determine if any future changes will be “predetermined”; prepare PCCP if applicable. |
| **Software Maintenance/Service Plan** – absent. | Required to show continued compliance post‑market (Part 820). | Draft Software Maintenance Procedure and include in DHF. |

---

### 4. Core Risk Controls (per ISO 14971 & IEC 62304)  

1. **Error Detection & Safe Default:** If image rendering fails, the software shall display a clear error message and abort processing; no corrupted images are saved.  
2. **User Authentication & Role‑Based Access:** Only authorized radiology staff may modify processing parameters.  
3. **Data Integrity Checksums:** All DICOM files are verified on import/export to prevent silent data loss.  
4. **Audit Trail:** Every processing step, parameter change, and user action is logged with timestamps.  
5. **Encryption in Transit & At Rest:** TLS 1.2+ for network communication; AES‑256 storage encryption per cybersecurity guidance.  
6. **Input Validation:** Strict DICOM tag validation to guard against malformed files (buffer overflow mitigation).  
7. **Fail‑Safe Shutdown:** On critical fault detection, the software transitions to a read‑only mode preserving original images.  

---

### 5. Citations  

| Item | Citation Type | Reference |
|---|---|---|
| Device classification | Framework reference | **21 CFR §892.2050** (Class II Image Processing Software) |
| Quality System requirements | Framework reference | **21 CFR Part 820** (QMSR) |
| Software lifecycle standard | Framework reference | IEC 62304:2006+A1:2015 |
| Risk management standard | Framework reference | ISO 14971 |
| FDA software content guidance | Framework reference | “Guidance for the Content of Premarket Submissions for Device Software Functions” (2023‑06‑14 Final) |
| FDA cybersecurity guidance | Framework reference | “Cybersecurity in Medical Devices” (2023‑09‑27 Final) |
| eSTAR performance testing structure | Instance identifier *as listed* | Section G layout shown in source excerpt – no external case number; **no specific identifier found in source — verify separately** |

---

### 6. Human‑Escalation Triggers  

- **Predicate Gap:** No predicate identified → **Escalate to Sponsor/Project Lead** for market search before proceeding.  
- **Usability Deficiency:** Missing IEC 62366 report → **Escalate to Human Factors Team**; cannot finalize 510(k).  
- **Cybersecurity Plan Incomplete** (threat model absent) → **Escalate to Cybersecurity Lead**.  
- **UDI Plan Not Drafted** → **Escalate to Regulatory Operations** for labeling compliance.  
- **Dataset Description Insufficient** → **Escalate to Validation Engineer**; request full dataset justification.  
- **Potential AI/ML Updates Identified Later** → **Escalate to Software Architecture Lead** to develop PCCP.  

If any of the above triggers are activated, pause submission package assembly and obtain the missing artifacts before moving forward.

---

### 7. Peer Review Request  

*Please have another RA colleague review this draft for:*  

1. **Assumption Validity:** Are we correct in treating the GUI as a Class II SaMD under §892.2050 without additional device functions that could shift classification?  
2. **Source Coverage:** Did we overlook any requirement elements present in the source excerpts (e.g., specific performance metrics)?  
3. **Jurisdictional Gaps:** Are there any FDA‑specific items (e.g., special controls for image processing software) not captured here that must be addressed before filing?  

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

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

## ra_eu

### kb-eval-20260723-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "b6dea4f737f3e163", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b6dea4f737f3e163`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis (MDR 2017/745)**  

---

### 1. Scope & Device Assumptions  
*The source material does not contain a specific device description. The analysis therefore proceeds on the basis that the sponsor is preparing a clinical‑evaluation report (CER) for a medical device that intends to rely on equivalence with one or more predicate devices.*  

> **Citation:** MDR Regulation (EU) 2017/745, Art. 61 & Annex XIV (clinical evaluation); MDCG 2020‑5, 2020‑6 and 2023‑7 (equivalence & sufficient clinical evidence).  

---

### 2. Classification / Conformity‑Assessment Route  
| Item | Determination | Rationale |
|------|----------------|-----------|
| **Device class** | *To be defined by the sponsor* – must apply Annex VIII classification rules (e.g., Rule 9, 10, 11, 17) once intended use and mode of action are known. | No information on active/diagnostic/implantable nature is supplied in the source. |
| **Conformity‑assessment route** | *Annex IX* – full quality‑management‑system (QMS) assessment together with technical documentation, if class IIa or higher. For class I non‑sterile devices a self‑declaration (Annex IV) may be sufficient. | The MDR requires use of the Annex number only (no “module” terminology). |

> **Citation:** Classification rules – Annex VIII; Conformity‑assessment routes – Annex IX, X, XI.

**Human‑escalation trigger 1:** *If the sponsor cannot identify a single applicable classification rule because the intended purpose or mode of action is ambiguous, the project manager must pause the submission and request a definitive “intended use” statement before any further work.*  

---

### 3. Required Clinical‑Evidence – Equivalence (per MDCG 2020‑5/6)  
| Requirement | What the NB expects | Current status (based on source) |
|-------------|---------------------|----------------------------------|
| **Clinical state & purpose** – identical disease/condition, severity, stage. | Must be demonstrated with a side‑by‑side table of the investigational device vs. each predicate. | Covered by source Table 2.3 (identical clinical state = “same” criteria). |
| **Anatomical site** – same body region. | Explicit statement that the anatomical location is identical. | Source notes “same body part (**‘same’ expression**)”. |
| **Patient population** – age, anatomy, physiology. | Detailed demographics of the predicate’s study population must match the intended use population. | Source lists “similar patient group (age, anatomy, physiology)”. |
| **User type** – professional vs. lay‑person. | *New MDR requirement*: device must be used by the same user category as the predicate; a home‑care device cannot rely on a predicate intended for HCPs and vice‑versa. | Explicitly highlighted in source (MDR adds “same user type”). |
| **Intended purpose & core clinical performance** – comparable claim. | Must show that the key performance parameters (KPPs) linked to the intended purpose are equivalent. | Source states “similar intended purpose core clinical performance”. |
| **Clinical data from predicate** – availability of a complete CER for the predicate, including any post‑market surveillance (PMS). | NB expects access to the predicate’s full technical documentation (including its own CER). | Not addressed in source – *gap identified*. |

> **Citations:** MDCG 2020‑5 (Equivalence), MDCG 2020‑6 (Sufficient Clinical Evidence), MDR Art. 61 & Annex XIV Part A.

**Human‑escalation trigger 2:** *If the sponsor cannot provide a full, up‑to‑date CER for every predicate device (including PMS data), the clinical‑evaluation work‑package must be halted and a request issued to the original manufacturer or to the NB for evidence of compliance.*  

---

### 4. Missing Information & Evidence Gaps  
| Gap | Why it matters / regulatory reference |
|-----|----------------------------------------|
| **Exact intended use statement** (including indication, patient group, user). | Required to apply Annex VIII rules and to determine equivalence criteria (Art. 61). |
| **User‑type classification** – confirmation whether the device is for HCPs or lay persons. | MDR explicitly adds this as an equivalence condition (source “동일한 사용자 유형”). |
| **Predicate CER & PMS data** (including any PMCF activities). | Annex XIV Part A mandates that the clinical evaluation be based on valid, up‑to‑date data; NB must see the full documentation. |
| **Clinical performance parameters (KPPs)** of both investigational and predicate devices, with quantitative comparison. | Needed to satisfy “core clinical performance” equivalence (source). |
| **Justification for any differences** in age range, anatomical variations, or user training that could affect safety/performance. | Must be documented in the CER under risk‑benefit analysis (Art. 61(4)–(6)). |
| **Post‑Market Clinical Follow‑up (PMCF) plan** if equivalence is partial or high‑risk. | Annex XIV Part B – PMCF planning required for class IIa and above when clinical data are insufficient. |
| **Risk‑management file (ISO 14971)** aligned with identified differences in user type or patient population. | Annex I (§ 16–§ 23) & ISO 14971 required to demonstrate that all residual risks have been reduced to an acceptable level. |

**Human‑escalation trigger 3:** *Any of the above gaps remain unresolved after two weeks of targeted information requests, the project lead must flag the case for senior RA review and possibly re‑scope the clinical‑evaluation strategy.*  

---

### 5. Recommended Risk Controls (to be reflected in the risk‑management file)  
1. **User‑error mitigation** – clear labeling and IFU tailored to the identified user type (HCP vs. lay).<br>   *Reference:* Annex I § 22 (devices intended for use by lay persons).  
2. **Age‑specific safety testing** – if the patient population differs from the predicate, perform bench or simulated clinical tests covering the age range.<br>   *Reference:* ISO 14971 risk‑control measures.  
3. **Usability validation** – especially when changing user type (e.g., moving from HCP to home use).<br>   *Reference:* IEC 62366‑1.  
4. **PMS & PMCF activities** – establish a PMS plan (Art. 84) and, where needed, a PMCF plan (Annex XIV Part B) to collect real‑world data on the new user group.<br>   *Reference:* Art. 83–86.  
5. **Software validation** – if software is part of the device, ensure compliance with IEC 62304 and consider classification under Rule 11 (Annex VIII).  

All risk controls must be documented in the **Risk Management Report** and cross‑referenced to the CER conclusions.

---

### 6. Documentation Checklist for NB Submission  
| Document | Required by | Status / Gap |
|----------|--------------|-------------|
| **Technical Documentation** – Annex II (including device description, labeling, IFU). | MDR Art. 10 & Annex II. | Pending – user‑type details missing. |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A. | MDR Art. 61 & Annex XIV Part A. | Gap: predicate CERs not supplied; equivalence justification incomplete. |
| **PMCF Plan / Evaluation Report** (if needed). | Annex XIV Part B. | Not prepared – to be drafted once gaps identified. |
| **Post‑Market Surveillance (PMS) Plan & Reports**. | Art. 84–86. | PMS system required; plan not yet defined. |
| **Risk Management File** – ISO 14971 compliant. | Annex I § 16‑23. | Draft exists but lacks controls for user‑type change. |
| **Declaration of Conformity (DoC)**. | Annex IV. | Pending final classification & conformity assessment outcome. |

---

### 7. Human‑Escalation Triggers Summary  

| Trigger # | Condition | Action Required |
|-----------|------------|-----------------|
| 1 | No clear intended use / user type defined. | Pause work; request definitive statement from product‑owner. |
| 2 | Predicate CER or PMS data unavailable. | Halt clinical‑evaluation draft; obtain documents or consider alternative predicates. |
| 3 | Any identified gap remains after two weeks of targeted follow‑up. | Escalate to senior RA manager for re‑assessment of equivalence strategy. |
| 4 | New high‑risk findings emerging from risk analysis (e.g., a residual risk > acceptable). | Trigger immediate risk‑acceptance review and possible redesign before submission. |

---

### 8. Peer‑Review Prompt  

> **To an RA colleague:** Please examine the assumptions made above, especially the interpretation of “same user type” as a strict equivalence condition, and confirm whether any additional MDR provisions (e.g., Art. 61(4)–(6) exemptions) might allow a less‑stringent justification in our case. Also verify that the listed documentation checklist aligns with the latest MDCG guidance (2024‑3) on CER content.

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

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

2. Chunk `1090731331984830062`

> > 최종 갱신: 2026-05-18 (자동보강 #52) > 근거: MDR Regulation (EU) 2017/745 Article 61 & Annex XIV | MDCG 2020-5 (Equivalence, Apr 2020) | MDCG 2020-6 (Sufficient Clinical Evidence, Apr 2020) | MDCG 2023-7 (Article 61(4)-(6) Exemptions, Dec 2023) | MDCG 2024-3 (CER Content) | FDA 510(k) Program Guidance (Jul 2014) | FDA Best Practices for Predicate Device Selection (Oct 2023 Draft) | MFDS 의료기기 허가·신고·심사 등에 관한 규정 (고시 제2024-88호) # Clinical Evaluation (MDR) 심화 — 동등성·충분성 기준

### kb-eval-20260723-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "83356594e071d8f8", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `83356594e071d8f8`
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

> **Draft – Clinical Evaluation & PMCF Evidence Gap Analysis (MDR 2017/745)**  

---

### 1. Device scope & provisional classification  
| Item | Assessment |
|------|------------|
| **Intended purpose / clinical application** | The source only lists “clinical‑application area”, “target population” and “user type” as required items, but does not disclose the actual intended use (e.g., diagnostic, therapeutic, monitoring). *Classification cannot be finalised* until the full Intended Use Statement is available. |
| **Applicable MDR rule** | Once the intended purpose is known the device will fall under one of the active‑device rules in Annex VIII (Rule 9, Rule 10, Rule 11 or Rule 17) or a non‑active rule (e.g., Rule 1–8). *Provisional assumption*: if the device delivers energy for therapy → **Rule 9**; if it only measures/monitors physiological data → **Rule 10**. |
| **Class** | – Under Rule 9: Class IIa (low‑risk therapeutic) or IIb (higher‑risk therapeutic). <br>– Under Rule 10: Class IIa (non‑critical monitoring) or IIb (monitoring of vital parameters that could lead to immediate danger). <br>*Exact class pending intended‑use clarification.* |
| **Conformity‑assessment route** | • If Class IIa – **Annex IX** (full quality‑management system assessment + technical documentation review). <br>• If Class IIb/III – **Annex X** (type‑examination) or **Annex XI** (production conformity verification), depending on the NB’s preferred route. |
| **Citation** | Classification rules – Annex VIII; Conformity‑assessment routes – Annex IX, X, XI. |

---

### 2. Required clinical‑evaluation evidence (MDR)  
| Requirement | What must be provided | Regulatory reference |
|-------------|----------------------|----------------------|
| **Clinical Evaluation Report (CER)** – kept current | • Systematic literature review of state‑of‑the‑art (SOTA) clinical data.<br>• Clinical investigation results (if any).<br>• Comparison with equivalent devices (if applicable).<br>• Benefit‑risk analysis. | Annex XIV Part A; Art. 61 (kept current). |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** (initial) | • Defined objectives, methodology and timelines.<br>• Targeted patient groups, clinical endpoints, data sources. | Annex XIV Part B. |
| **PMCF Evaluation Report** – final report | Must contain the mandatory sections A–G listed in the source excerpt (manufacturer contact, device description, results of performed PMCF activities, evaluation of equivalent‑device data, impact on technical documentation, applied standards/guidances, overall conclusion). | Annex XIV Part B – “PMCF Evaluation Report” (see source Table 5.2). |
| **Risk Management File (RMF)** | • Updated ISO 14971 risk analysis incorporating PMCF findings.<br>• Revised risk‑control measures where needed. | Annex I, §§16‑22; ISO 14971. |
| **Summary of Safety and Clinical Performance (SSCP)** for Class III or high‑risk devices | Integrated summary of safety & performance data, including PMCF outcomes. | Annex II, § 19 (for implantables) / relevant MDR article. |

---

### 3. Gaps identified from the supplied source excerpts  

| Gap | Evidence missing / clarification required |
|-----|--------------------------------------------|
| **Intended use description** | No explicit statement of the clinical indication, target patient group or user type – needed to select the correct classification rule (Annex VIII). |
| **Clinical performance endpoints** | The excerpt only mentions “핵심 성능” (core performance) as a required field but does not list the actual measurable performance criteria. |
| **Comparative device data (Section D of PMCF report)** | No comparative clinical data has been supplied; the table simply notes the section title. Evidence on equivalence or similarity must be provided. |
| **Impact on technical documentation (Section E)** | The effect of PMCF results on CER, RMF and SSCP is not documented yet – a narrative linking findings to required updates is needed. |
| **Applied standards & guidance (Section F)** | No specific harmonised standards or MDCG guidances are listed; these must be identified (e.g., IEC 60601‑2‑54 for X‑ray, ISO 14971, MDCG 2020‑5). |
| **Overall PMCF conclusion (Section G)** | The final judgement on whether the PMCF objectives have been met and any corrective actions are required is not yet drafted. |
| **Evidence of ongoing PMS system** | No reference to Art. 83–86 (PMS system/plan/report) is present – a description of the PMS processes that feed into PMCF must be included. |

*All the above items are mandatory for a complete MDR technical file and will be scrutinised by the Notified Body.*

---

### 4. Recommended risk‑control actions (to be reflected in RMF & SSCP)

1. **Update risk analysis** with any new hazards identified during PMCF data collection (e.g., unexpected adverse events, performance drift).  
2. **Implement corrective actions** where Section G of the PMCF report indicates preventive or remedial measures – e.g., software update, user‑training enhancement, labeling change (§ 23, Annex I).  
3. **Re‑evaluate residual risk** after applying new controls; ensure that the benefit‑risk determination remains favourable (Art. 61 MDR).  
4. **Document all changes** in the Technical Documentation (Annex II) and propagate them to the CER, RMF and SSCP as required by Section E of the PMCF Evaluation Report.

---

### 5. Human‑escalation triggers  

| Situation | Action & responsible party |
|-----------|-----------------------------|
| **Unclear intended use / classification** | Senior RA must obtain a finalized Intended Use Statement from the product team and perform a definitive rule check (Annex VIII). Escalate to Regulatory Lead before any NB interaction. |
| **Missing comparative clinical data** | Clinical‑studies manager must source or generate appropriate equivalence evidence within 30 days; otherwise halt dossier preparation. |
| **PMCF report sections incomplete** | PMCF coordinator to complete Sections A–G and resubmit for RA review within 2 weeks; if not achieved, flag to Project Manager for timeline reassessment. |
| **Residual risk after PMCF > acceptable** | Immediate stop‑work order; convene Risk Management Committee (RMC) to decide on redesign or market withdrawal – Senior Safety Officer leads. |
| **PMS system not demonstrable** | Quality‑Management Lead must provide documented PMS procedures (Art. 83‑86). If unavailable, the NB submission is blocked. |

---

### 6. Summary judgment  

- The device’s **classification and conformity‑assessment route cannot be finalised** until the full intended‑use description is supplied.  
- A **complete CER (Annex XIV Part A)** and a **PMCF Evaluation Report covering all mandatory sections (A–G) per Annex XIV Part B** are required. Current documentation gaps must be resolved before any Notified Body audit.  
- All identified risk‑control updates must be reflected in the RMF, SSCP and technical documentation to satisfy MDR §§ 16‑22 (Annex I).  

---

### 7. Peer‑review prompt  

> *Colleague RA, please challenge the assumptions made above:*  
> - Are we correctly interpreting the need for a comparative device assessment given the limited source detail?  
> - Does the provisional classification under Rule 9 or Rule 10 align with typical devices that have “core performance” as a mandatory field in Korean regulatory templates?  
> - Have we captured all relevant MDCG guidances (e.g., MDCG 2020‑5, 2020‑6) that should be listed in Section F of the PMCF report?  
> - Are any additional MDR articles (e.g., Art. 86 PSUR requirements for Class IIa/IIb/III) applicable at this stage?  

Please provide feedback on potential omissions or alternative interpretations.

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

1. Chunk `1032759063790726230`

> │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ```

2. Chunk `1132312459160211217`

> ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과 (데이터 수집 결과, 긍정·부정 포함, 편차 근거) | | D | 동등·유사 기기 임상데이터 평가 결과 | | E | 기술문서에 대한 결과의 영향 (CER, Risk Management File, SSCP 각각 명시) | | F | 적용된 CS, 조화표준, 가이던스 | | G | 종합 결론 (PMCF 목적 대비 결과, 예방·시정 조치 필요성) |

### kb-eval-20260723-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "fa90ff878ef527e7", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `fa90ff878ef527e7`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter |...
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & NB Deficiency Response**  

---

### 1. Device Scope & Likely MDR Classification  
| Item | Assessment |
|------|------------|
| **Intended use** – “standard diagnostic radiology” (X‑ray system) | Active medical device that emits ionising radiation for diagnostic purposes. |
| **Applicable classification rule** – Rule 10 (active devices for diagnosis/monitoring) → **Class IIb** (energy emitted may be hazardous). <br>*Citation*: MDR Annex VIII, Rule 10. |
| **Secondary subsystems** – detector (Rule 17, Class IIa) and any image‑processing software (Rule 11, Class IIa/IIb depending on decision impact). The overall system is placed in the highest class → **Class IIb**. |

---

### 2. Required Conformity‑Assessment Route  
| Requirement | MDR route |
|-------------|-----------|
| **Technical documentation + QMS assessment** for a Class IIb device | **Annex IX** (full quality‑management system audit together with technical file review). <br>Alternative (type‑examination + production conformity) is possible but most NB’s prefer Annex IX for X‑ray systems. |
| **Declaration of Conformity** | Annex IV. |
| **Post‑Market Surveillance (PMS)** | System per Art. 83, PMS plan Art. 84, PSUR (Class IIb → annual) Art. 86. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61. |
| **PMCF** (if required for equivalence justification) | Annex XIV Part B (plan + evaluation report). |

---

### 3. Evidence Currently Available (per source excerpt [1])  
| Evidence | Comment |
|----------|---------|
| **Clinical equivalence claim** – same clinical condition & DQE ≥ 65 % (IEC 62220‑1‑1) with reference to Test Report TR‑2024‑015. | Meets a quantitative performance metric for detector component (Rule 17). |
| **Revised CER Rev. 3 attached as Annex A** | Provides baseline clinical evaluation, but completeness must be verified against Annex XIV Part A requirements. |
| **Reference to IEC 62220‑1‑1** – detector quantum efficiency measurement. | Acceptable for performance testing of the imaging chain. |

---

### 4. Missing / Incomplete Information (gap analysis)  

| Gap | Required Evidence / Documentation | Why needed (regulatory reference) |
|-----|-----------------------------------|------------------------------------|
| **Full Clinical Evaluation Report** – justification of equivalence across the *entire system* (source [1] only addresses detector DQE). | Complete CER covering: <br>• Clinical background, state‑of‑the‑art literature, <br>• Benefit–risk analysis, <br>• Residual risk evaluation. | Annex XIV Part A; Art. 61 – CE marking requires a *complete* CER. |
| **Device‑specific performance data for the X‑ray source** (radiation output, dose uniformity). | Test reports complying with IEC 60601‑2‑54 (diagnostic radiology) and IEC 60601‑2‑28 (tube assemblies). | GSPR §16 (protection against radiation); Annex XIV Part A (clinical data must support safety/performance). |
| **Software validation evidence** (if image‑processing software is a medical device). | IEC 62304 lifecycle files, verification & validation protocols, risk management for software (§17). | GSPR §17; Annex XIV Part B (PMCF may be required for software). |
| **Risk Management File (RMF) – latest ISO 14971** covering the combined system and all identified hazards (radiation, electrical, mechanical). | Updated RMF with residual‑risk evaluation & risk‑control measures. | Annex I §18; ISO 14971 (mandatory for MDR). |
| **Usability/Human Factors Engineering** – especially if intended for lay‑person use (§22). | IEC 62366‑1 usability engineering file. | GSPR §22. |
| **Labeling & IFU** – conformity to Annex I Chapter III (§23). | Complete labeling package (EU label, CE mark image, instructions for use). | Annex I §23. |
| **PMS Plan & PMCF Plan** – tailored to Class IIb diagnostic X‑ray system. | Art. 84 PMS plan; Annex XIV Part B PMCF plan (including post‑market clinical follow‑up strategy). |
| **Declaration of Conformity (DoC)** – signed, includes reference to applicable standards & conformity‑assessment route. | Annex IV DoC. |
| **NB‑specific deficiency items** (QMS non‑conformities, TD shortcomings, labeling) – listed in source [2] under “주요 결함 유형”. | Full corrective‑action evidence for each NC (e.g., updated procedures, records of implementation). | MDR Annex VII + 2026/977 (source [2]). |

---

### 5. Risk Controls to be Demonstrated  

| Hazard | Control(s) | Regulatory basis |
|--------|-----------|-------------------|
| **Ionising radiation exposure** | • Shielding design per IEC 60601‑2‑54 §16.4 <br>• Dose monitoring & alarm functions <br>• Periodic calibration program | GSPR §16 (radiation protection). |
| **Electrical safety / EMC** | IEC 60601‑1 compliance, protective earth, leakage current limits. | GSPR §§18–20. |
| **Software malfunction influencing diagnosis** | IEC 62304 lifecycle management; verification of diagnostic algorithms; fail‑safe state & user alerts. | GSPR §17; Annex XIV Part B (if PMCF needed). |
| **User error (lay‑person operation)** | Ergonomic design, colour‑coded controls, clear IFU per IEC 62366‑1. | GSPR §22. |
| **Residual risk from combined system** | Updated RMF (ISO 14971) showing acceptance of residual risk after application of all above controls. | Annex I §§18–20; Art. 61 CER requirement. |

---

### 6. Citations  

| Source | Citation in draft |
|--------|-------------------|
| MDR Annex VIII – Rule 10 (active diagnostic devices) | “Rule 10 → Class IIb” |
| MDR Annex IX (conformity‑assessment route for Class IIb) | “Annex IX” |
| MDR Annex XIV Part A – Clinical Evaluation Report | “Annex XIV Part A; kept current under Art. 61” |
| MDR Annex XIV Part B – PMCF plan/evaluation report | “Annex XIV Part B” |
| MDR Articles 83‑86 (PMS system, plan, PSUR) | “Art. 84 PMS plan; Art. 86 PSUR (annual for Class IIb)” |
| IEC 62220‑1‑1 – DQE measurement | Referenced in source [1] “DQE(0) ≥ 65 % … Ref. Test Report TR‑2024‑015, IEC 62220‑1‑1” |
| IEC 60601‑2‑54 – X‑ray equipment (diagnostic radiology) | Required for source performance data (gap). |
| IEC 62304 – Software lifecycle | Needed for software validation (gap). |
| ISO 14971 – Risk management | Mandatory RMF (gap). |
| MDR Annex VII + 2026/977 – NB deficiency categories | Source [2] “근거 법령 | MDR Annex VII + 2026/977”. |
| MDR Annex I §§16, 17, 18, 22, 23 – GSPR chapters | Cited where specific hazards are addressed. |
| IEC 62366‑1 – Usability engineering | Needed for lay‑person use (gap). |

*No instance identifiers (e.g., clearance numbers) appeared in the source excerpts; therefore none are inserted.*

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required | Reason |
|---------|-----------------|--------|
| **NB clock‑stop expires without submission** (source [2] “Clock‑stop → 예 (NB 요청 당일 stop, 제출 익일 resume)”) | Escalate to Senior RA Manager & Legal for possible rejection; prepare contingency filing. | Non‑response leads to “평가 종료 / 불승인”. |
| **Outstanding QMS non‑conformities** not closed within NB’s stipulated timeframe (max 4 verification cycles) | Immediate corrective‑action plan, notify Quality Assurance Head, consider temporary suspension of production under Art. 90. | NB may issue non‑approval if NCs remain. |
| **Missing CER elements** that prevent Annex XIV Part A compliance (e.g., no benefit–risk analysis) | Trigger urgent clinical‑evaluation team tasking; involve Clinical Affairs Lead. | Without a complete CER the device cannot be placed on the market. |
| **PMS/PMCF evidence not ready for PSUR (annual)** | Alert Post‑Market Surveillance Coordinator to prioritize data collection; schedule interim report. | Failure breaches Art. 86 reporting obligations → possible corrective action by authority. |
| **Disagreement on classification** (e.g., NB proposes Class IIa) | Request Structured Dialogue per Art. 7 of the 2026/977 amendment (source [2] “사전 대화 창구 | Structured Dialogue (Art. 7, 2026/977)”). | To obtain clarification before final conformity assessment. |
| **Regulatory‑change impact** – upcoming amendment to MDR Annex VII or new EU guidance on DQE thresholds | Inform Regulatory Strategy Lead; update technical file accordingly. | Prevents future non‑conformity. |

---

### 8. Summary Judgment  

- The device is **Class IIb** under **MDR Rule 10** (active diagnostic X‑ray system).  
- The appropriate conformity‑assessment route is **Annex IX** (full QMS + technical file audit).  
- Current documentation addresses only the detector’s DQE performance; a *complete* CER, source‑performance data, software validation, updated risk management, labeling, PMS/PMCF plans, and DoC are all required to satisfy MDR Annex XIV, Annex I GSPR, and Articles 83‑86.  
- The NB deficiency letter (source [2]) indicates gaps in **CER, Technical Documentation, QMS non‑conformities, and labeling** – all must be closed before the NB’s clock‑stop expires.  

**Immediate actions:**  

1. Compile missing evidence listed in Section 4 and submit a revised technical documentation package addressing each NB deficiency item.  
2. Update the CER (Annex XIV Part A) to include full system clinical equivalence, benefit–risk analysis, and residual risk evaluation.  
3. Generate source‑type test reports (IEC 60601‑2‑54 & IEC 60601‑2‑28) and software lifecycle documentation (IEC 62304).  
4. Finalise PMS/PMCF plans and align PSUR schedule to annual reporting for Class IIb.  

*All actions must be tracked against the NB’s clock‑stop timeline; any delay beyond the agreed date shall trigger escalation per Section 7.*

---

### 9. Peer‑Review Prompt  

> **Colleague, please review:**  
> - Are we correct in classifying the complete X‑ray system as Class IIb solely on Rule 10 (active diagnostic) despite the detector being Rule 17?  
> - Does the evidence list fully cover the NB’s “주요 결함 유형” (CER, TD, QMS NC, labeling) as described in source [2]?  
> - Have we captured any jurisdiction‑specific requirements that might be missing for the Korean MFDS or US FDA pathways, given the cross‑reference table in source [2]?  
> – Identify any additional EU MDR annexes or articles that should be cited to solidify our gap‑analysis.  

Please challenge the assumptions and flag any overlooked gaps.

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

### kb-eval-20260723-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7f031b9b3ec42e2c", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7f031b9b3ec42e2c`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PSUR_%ED%85%9C%ED%94%8C%EB%A6%BF_MDR_Article86.md)
- Source hash: `6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PSUR_템플릿_MDR_Article86.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Section 7. PMCF 결과 연계 (Art.86(1)(d)) | 항목 | 내용 | |---|---| | PMCF 계획 참조 문서 | [문서번호, 버전] | | PMCF 현재 상태 | [진행 중 / 완료 / 계획 단계] | | 이번 기간 주요 PMCF 결과 | [요약 또는 "중간 데이터 없음"] | | PMCF 결과의 CER 반영 | [반영 여부, 반영 내용] | | 다음 PMCF 중간 보고 예정일 | [YYYY-MM-DD] | --- ### Section 2. 판매량 및 노출 추정 (MDR Art.86(1)(c)) | 지역 | 판매 수량 | 추정 환자 노출 수 | 판매 기간 | |---|---|---|---| | EU...
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

> **Regulatory Draft – PSUR (Art 86 MDR) Gap Analysis & Submission Planning**

---

### 1️⃣ Device Identification – What is missing?  

| Item | Current status (from source) | Required for classification / PSUR |
|------|-----------------------------|------------------------------------|
| **Device name / model** | not provided | Needed to locate the applicable device‑specific regulations and to populate the “sales & exposure” tables. |
| **Intended medical purpose** | not provided | Determines the classification rule (Annex VIII) and the depth of clinical evidence required (Art 61, Annex XIV). |
| **Technology / principal mode of action** | not provided | Required for selecting the correct Classification Rule (e.g., Rule 9‑12, 17). |
| **Regulatory status in other jurisdictions** | none cited | Helpful for leveraging existing clinical data but not mandatory. |

> **Action:** Request a concise device description (intended use, principal technology, target patient population) before any classification work can commence.

---

### 2️⃣ Classification & Conformity‑Assessment Route – Preliminary view  

| Step | Reference | What we need to decide |
|------|-----------|------------------------|
| **Determine class** | Annex VIII – Classification Rules (e.g., Rule 9, 10, 11, 17) | Requires the intended purpose and whether the device is active, implantable, software‑driven, etc. |
| **Select route** | *Annex IX* (QMS + Technical Documentation assessment) for Class IIa/IIb/III; *Annex X* or *Annex XI* only for lower‑risk (Class I, non‑sterile, non‑measuring) devices. | Dependent on the class that will be assigned in the previous step. |

> **Current judgment:** Classification cannot be finalised without the missing device‐specific information.  

> **Human‑escalation trigger #1:** If the RA team cannot obtain a complete intended‑use statement within 10 working days, senior management must approve a “classification hold” and liaise with the product owner.

---

### 3️⃣ Clinical Evaluation & Post‑Market Clinical Follow‑up (PMCF) – Evidence required  

| Required element (MDR) | Where it belongs | Citation |
|------------------------|------------------|----------|
| **Clinical Evaluation Report (CER)** – up‑to‑date, addressing benefit–risk and the state of the art. | Annex XIV Part A; kept current under Art 61. | — |
| **PMCF Plan** – description of objectives, methodology, timelines, cohorts, endpoints. | Annex XIV Part B. | — |
| **PMCF Report (interim & final)** – results integrated into the CER. | Annex XIV Part B; referenced in Art 86(1)(d). | Art 86(1)(d) |
| **PMS data** needed for PSUR (sales, exposure, adverse trends). | Art 83‑86 (PMS system & reports). | Art 86(1)(c)–(d) |

#### Gaps identified in the source excerpts  

| Section (source) | Expected content | What is missing / incomplete |
|------------------|------------------|------------------------------|
| **7. PMCF 결과 연계** (Art 86(1)(d)) | • Reference to the *PMCF plan* document (ID & version).<br>• Current status of the PMCF activity.<br>• Summary of key results for the reporting period.<br>• Explicit statement on how these results have been reflected in the CER.<br>• Date of the next interim PMCF report. | All fields are placeholders (`[문서번호, 버전]`, `[진행 중 / 완료 …]`, etc.). No actual data supplied. |
| **2. 판매량 및 노출 추정** (Art 86(1)(c)) | • Quantified sales per region.<br>• Estimated patient‑exposure numbers.<br>• Period covered.<br>• Methodology & assumptions when exposure cannot be directly measured (MDCG 2022‑21 §5.3). | All cells contain placeholders (`[수량]`, `[추정 수]`, …) and the methodology narrative is absent. |

> **Action items**  
1. Populate the PMCF table with a *validated* reference to the approved PMCF plan, indicate which milestones have been achieved, summarise any safety signals or performance trends, and explicitly note CER updates.  
2. Complete the sales‑exposure matrix with audited sales data (EU, Korea, US, Others) and apply the methodology described in **MDCG 2022‑21 §5.3** when patient numbers are estimated.  

> **Human‑escalation trigger #2:** If any of the above tables remain incomplete past the internal PSUR submission deadline, the Responsible Person must be notified to either (a) provide the missing data or (b) justify a postponement to the Notified Body.

---

### 4️⃣ Risk Management – Required controls & linkage  

| Requirement | Where it belongs in the technical file | Citation |
|-------------|----------------------------------------|----------|
| **Risk management file** (ISO 14971‑based) covering residual risk, risk‑benefit analysis, and verification of risk controls. | Annex I §16‑22 (General Safety & Performance Requirements), implemented via ISO 14971. | — |
| **Linkage of PMCF findings to residual risks** – any new hazards or increased probability must be reflected in the risk file and CER. | Art 61 (clinical evaluation) & Art 86(1)(d). | Art 86(1)(d) |
| **Corrective actions / field safety corrective actions (FSCAs)** where trends require action. | Art 87 (Vigilance reporting). | — |

> **Current gap:** No evidence in the source that PMCF outcomes have been mapped to risk‑control updates or that corrective actions have been taken.

> **Human‑escalation trigger #3:** Detection of a newly identified hazard (e.g., a serious adverse event not previously captured) must be escalated immediately to the Notified Body per Art 87 and to senior management for risk‑benefit re‑evaluation.

---

### 5️⃣ PSUR Content Checklist (Art 86 MDR)  

| Item (Art 86(1)) | Required evidence / documentation |
|------------------|------------------------------------|
| **(a) Conclusions of the benefit–risk determination** | Updated CER, summary of residual risk, any changes since previous PSUR. |
| **(b) Main findings of the PMCF** | Completed PMCF interim report (see Section 7). |
| **(c) Volume of sales & estimate of the size & characteristics of the using population** | Populated table from Section 2; methodology per MDCG 2022‑21 §5.3. |
| **(d) Any corrective actions taken, including field safety corrective actions (FSCA)** | Records of FSCAs, post‑market recalls, and updates to risk file. |

> **Status:** Items (b) and (c) are currently empty placeholders; items (a) and (d) lack supporting documents in the provided excerpt.

---

### 6️⃣ Human‑Escalation Triggers – When a reviewer must intervene  

| Trigger | Condition | Escalation path |
|---------|-----------|-----------------|
| **#1 – Missing intended‑use / technology description** | No response within 10 working days. | Notify senior RA manager → postpone classification decision → inform product development lead. |
| **#2 – Incomplete PMCF or sales/exposure tables at PSUR cut‑off** | Any placeholder (`[…]`) remains after the internal deadline. | Immediate email to Responsible Person and Project Lead; if not resolved within 5 working days, elevate to Quality Management (QM) Director for possible extension request to Notified Body. |
| **#3 – New safety signal or trend detected in PMCF data** | Signal meets predefined severity threshold (e.g., ≥ 2 serious adverse events linked to the device). | Trigger Art 87 reporting → fast‑track to Vigilance Officer → submit FSCA to NB within 15 days. |
| **#4 – Failure to demonstrate methodology for patient‑exposure estimation** | No documented method or assumptions per MDCG 2022‑21 §5.3. | Request documentation from Market Access; if unavailable, raise to Regulatory Steering Committee for risk‑based decision on postponement of PSUR submission. |

---

### 7️⃣ Summary Judgment & Next Steps  

*Based on the current source material, the PSUR draft lacks all quantitative clinical and post‑market data required by **Art 86(1)(c)–(d)** and does not provide the linkage to the **CER** demanded by **Art 86(1)(d)**. Classification cannot be finalised without a clear description of intended use and technology, which also determines the depth of clinical evidence needed (Art 61, Annex XIV).*

**Immediate actions**

1. Obtain a concise device definition (intended purpose, active/implantable status, software component) – trigger #1 if delayed.  
2. Fill in the PMCF section with an actual plan reference, current status, results summary, and CER integration note.  
3. Complete the sales & patient‑exposure table and attach a methodology narrative complying with **MDCG 2022‑21 §5.3**.  
4. Verify that any new risks identified by PMCF are reflected in the risk management file (ISO 14971) and that corrective actions are documented.

---

### 8️⃣ Peer Review Prompt  

> *“Colleague, could you review the assumptions made above regarding the classification dependency on intended‑use information, the completeness of the PSUR content checklist, and the escalation thresholds? Please confirm whether any additional MDR annexes or MDCG guidance (e.g., MDCG 2020‑13) should be considered for this device’s post‑market clinical follow‑up plan.”*

**Citation Lint (C1 — 구조적 인용 오류 자동 감지)**

- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)

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

1. Chunk `108347462317924009`

> ### Section 7. PMCF 결과 연계 (Art.86(1)(d)) | 항목 | 내용 | |---|---| | PMCF 계획 참조 문서 | [문서번호, 버전] | | PMCF 현재 상태 | [진행 중 / 완료 / 계획 단계] | | 이번 기간 주요 PMCF 결과 | [요약 또는 "중간 데이터 없음"] | | PMCF 결과의 CER 반영 | [반영 여부, 반영 내용] | | 다음 PMCF 중간 보고 예정일 | [YYYY-MM-DD] | ---

2. Chunk `131915604397474083`

> ### Section 2. 판매량 및 노출 추정 (MDR Art.86(1)(c)) | 지역 | 판매 수량 | 추정 환자 노출 수 | 판매 기간 | |---|---|---|---| | EU | [수량] | [추정 수] | [기간] | | 한국 | [수량] | [추정 수] | [기간] | | 미국 | [수량] | [추정 수] | [기간] | | 기타 | [수량] | [추정 수] | [기간] | | **합계** | **[합계]** | **[합계]** | — | > **MDCG 2022-21 §5.3:** 정확한 환자 수 추정이 어려울 경우 방법론과 가정 조건을 명시. ---

### kb-eval-20260723-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a5eea01bffb14927", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a5eea01bffb14927`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PMS_Plan_MDR_Article84_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PMS_Plan_MDR_Article84_템플릿.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | PMS 항목 | 특화 내용 | |---|---| | 주요 위험 신호 | SW 오류로 인한 진단 오류, 데이터 손실, 사이버보안 취약점 | | 핵심 수집원 | SW 버그 리포트, 사이버보안 취약점 공개 DB (CVE, NIST NVD) | | PMCF 방법 | 사용성 평가 (IEC 62366), 실사용 에러 데이터 수집 | | 주요 표준 모니터링 | IEC 62304 개정, MDCG 2019-16 Rev.1 사이버보안, MDCG 2021-6 SaMD | | MFDS 특이사항 | 디지털의료제품법(2024.09.26 시행) 적용 여부 검토 [검증 필요] | --- ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (...
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

> **Regulatory Draft – Clinical‑Evidence Gap Analysis for the Three MDR Products**

| # | Item | Findings (as derived from source) | Required Evidence / Documentation | Missing or Incomplete Information | Risk Controls (proposed) | Regulatory Citations |
|---|------|-----------------------------------|-----------------------------------|-----------------------------------|--------------------------|-----------------------|
| 1 | **Device : X‑ray Detector**<br>Intended use – acquisition of diagnostic images generated by ionising radiation. | • MDR class shown as “Class IIa/IIb” (matrix). <br>• No explicit rule cited in source. | • Classification justification (Rule 17 → Class IIa; possible up‑classification to IIb if the detector is integral to a therapeutic system). <br>• Clinical Evaluation Report (CER) – Annex XIV Part A.<br>• PMCF plan & report – Annex XIV Part B. <br>• PSUR (2‑year cycle for Class IIa, annual for IIb) – Art 86.<br>• Risk Management file – ISO 14971 / Annex I §§16‑20. <br>• State‑of‑the‑art literature review on detector performance (DQE, noise). | • No documented justification why the device is placed in Class IIa *or* IIb; rule reference absent.<br>• No evidence of clinical data that demonstrates equivalence or superiority to existing detectors. <br>• No description of the PMCF methodology beyond “usability evaluation” (IEC 62366) – needs sample size, collection period, performance endpoints.<br>• No confirmation whether Korean MFDS Digital‑Medical‑Product Act (effective 2024‑09‑26) applies; source flags “검증 필요”. | • Redundant hardware checks (self‑test, error codes). <br>• Shielding verification and interlock safety to prevent unintended exposure. <br>• Software error detection & fallback mode (per IEC 62304). <br>• Periodic cybersecurity patching (see §2 risk‑signal). | **Classification** – Rule 17 (recording diagnostic images) ⇒ Class IIa (Annex VIII, Rule 17).<br>**Conformity route** – Annex IX (QMS + technical documentation assessment) for both IIa and IIb.<br>**Clinical evidence** – Annex XIV Part A (CER); Art 61/62 (keep CER up‑to‑date).<br>**PMCF** – Annex XIV Part B. <br>**PMS plan/report** – Art 84, Art 86.<br>**Risk management** – Annex I §§16‑20; ISO 14971.<br>**Usability** – IEC 62366‑1.<br>**Software lifecycle** – IEC 62304.<br>**Cybersecurity** – MDCG 2019‑16 Rev.1, MDCG 2021‑6. |
| 2 | **Device : Handheld X‑ray Source**<br>Intended use – emission of ionising radiation for diagnostic radiography (portable). | • MDR class shown as “Class IIb”. <br>• No rule cited in source. | • Classification justification (Rule 10 – active devices emitting ionising radiation ⇒ Class IIb). <br>• Clinical Evaluation Report – Annex XIV Part A.<br>• PMCF plan & report – Annex XIV Part B (focus on dose‑monitoring, usability in emergency settings).<br>• PSUR – annual (Art 86 for Class IIb). <br>• PMS system – Art 83; PMS plan – Art 84.<br>• Risk Management file – ISO 14971 / Annex I §§16‑20 (radiation protection, mechanical safety). | • No documented analysis of radiation dose distribution, beam steering, or compliance with IEC 60601‑2‑54 (X‑ray equipment for radiography). <br>• Absence of a detailed PMCF protocol: number of procedures, patient population, follow‑up period. <br>• No evidence that the device meets the “digital medical product” definition under MFDS law; source flags verification required.<br>• No explicit labeling content (Annex I §23). | • Built‑in dose‐monitoring and automatic shut‑off if threshold exceeded.<br>• Physical interlocks + software watchdog to prevent accidental emission.<br>· Periodic cybersecurity assessment of firmware (CVE/NIST NVD monitoring).<br>· Usability safeguards per IEC 62366‑1 (error‑proof user interface, colour coding). | **Classification** – Rule 10 (active device for diagnosis/monitoring emitting ionising radiation) ⇒ Class IIb (Annex VIII, Rule 10).<br>**Conformity route** – Annex IX (QMS + technical file); optional Annex X type‑examination if manufacturer prefers. <br>**Clinical evidence** – CER Annex XIV Part A; clinical data on image quality & dose.<br>**PMCF** – Annex XIV Part B (focus on radiation safety).<br>**PMS plan/report** – Art 84, Art 86 (annual PSUR).<br>**Risk management** – Annex I §16 (radiation protection), §20 (mechanical/thermal risks).<br>**Standards** – IEC 60601‑2‑54; IEC 62304; IEC 62366‑1.<br>**Cybersecurity** – MDCG 2019‑16 Rev.1, MDCG 2021‑6. |
| 3 | **Device : “촬영실 GUI SW (SaMD)”**<br>Software that provides the user interface for image acquisition and interpretation in an X‑ray suite. | • MDR class shown as “Class IIa (MDR §22)”. <br>• No rule number provided; source links class to §22 (general safety requirement for lay‑person use). | • Classification justification (Rule 11 – software providing diagnostic information ⇒ at least Class IIa, possibly higher if decision impact is severe). <br>• Clinical Evaluation Report – Annex XIV Part A (clinical performance of the software on image interpretation).<br>• PMCF plan & report – Annex XIV Part B (usability testing, real‑world error logs).<br>• PSUR – 2‑year cycle for Class IIa (Art 86). <br>• PMS plan – Art 84; PMS system – Art 83.<br>• Risk Management file – ISO 14971 / Annex I §§17‑18 (electronic programmable systems, active devices).<br>· Software lifecycle documentation – IEC 62304 (revision noted in source).<br>· Usability engineering – IEC 62366‑1. | • No explicit Rule 11 citation; classification based only on MDR §22 which refers to user‑friendly design for lay persons, not the rule set used for SaMD.<br>• No evidence of clinical performance (e.g., diagnostic accuracy, reader studies) beyond “software new development”.<br>• PMCF description limited to “usability evaluation”; missing quantitative success criteria, number of users, statistical analysis plan.<br>· Cybersecurity controls mentioned only in the PMS matrix; no dedicated threat‑model or mitigation strategy presented. | • Secure coding practices (IEC 62304). <br>· Role‑based access control, audit trails per MDCG 2021‑6 SaMD guidance.<br>· Regular vulnerability scanning against CVE/NVD feeds.<br>· Redundant validation of image data before display (failsafe to default view).<br>· Usability safeguards: lockout after repeated invalid inputs, clear error messages. | **Classification** – Rule 11 (SaMD providing diagnostic info) ⇒ Class IIa (Annex VIII, Rule 11). <br>**Conformity route** – Annex IX (QMS + technical file).<br>**Clinical evidence** – CER Annex XIV Part A (clinical performance study).<br>**PMCF** – Annex XIV Part B (real‑world usability & error data).<br>**PMS** – Art 84 (plan), Art 83 (system), Art 86 (PSUR every 2 years).<br>**Risk management** – Annex I §§17‑18; ISO 14971.<br>**Software lifecycle** – IEC 62304 (revision monitored in source).<br>**Usability** – IEC 62366‑1.<br>**Cybersecurity** – MDCG 2019‑16 Rev.1, MDCG 2021‑6 SaMD. |

---

### Summary of Overall Gaps & Actions Required

| Gap | Product(s) Affected | Action Needed (by RA/Clinical team) | Escalation Trigger |
|-----|----------------------|------------------------------------|---------------------|
| **Classification rule justification** (Rule 10, 11, 17) | All three | Produce a *Classification Justification Report* citing the exact Annex VIII rule(s) and rationale for any up‑classification (e.g., X‑ray Detector to IIb). | If justification cannot be substantiated within 2 weeks → senior RA sign‑off required. |
| **Clinical Evidence** – CER completeness (clinical data, SOTA literature) | All three | Assemble clinical performance data: bench tests, equivalence studies (for detector), dose‑distribution study (handheld source), diagnostic accuracy/reader study (GUI). Update CER per Annex XIV Part A. | Missing any primary clinical data → halt conformity assessment submission; notify Project Lead. |
| **PMCF Plan Detail** – endpoints, sample size, data collection timeline | All three | Draft detailed PMCF protocols aligned with Annex XIV Part B, including statistical analysis plans and monitoring of usability‑error logs. | Incomplete PMCF plan after review → pause TB assessment; inform TM. |
| **Risk Management File** – updated FMEAs covering software bugs & cyber threats | All three | Extend risk file to include *software error* (SW‑bug) and *cybersecurity* scenarios, reference CVE/NVD feeds as identified risk signals. | Unmitigated high‑risk cyber vulnerability → immediate product hold; senior security officer involvement. |
| **Standards Monitoring** – IEC 62304 revision, MDCG guidance updates | All three | Implement a standards‑watch process (e.g., quarterly review) to capture revisions and update technical documentation accordingly. | Failure to record a new relevant standard before next audit → raise Non‑Conformity alert. |
| **MFDS Digital‑Medical‑Product Law applicability** – verification for each device | X‑ray Detector, Handheld Source | Obtain legal opinion on whether the Korean “디지털의료제품법” (effective 2024‑09‑26) is triggered; if yes, align with MFDS post‑market surveillance requirements. | Uncertainty after legal review → forward to cross‑border compliance lead. |
| **Labeling & IFU** – Annex I §23 content completeness | All three | Prepare draft labeling that includes intended use, contraindications, radiation safety info (for active devices), user instructions, and cybersecurity notice. | Labeling gaps identified in TB audit → escalation to Documentation Manager. |

---

### Human‑Escalation Triggers

1. **Classification Ambiguity** – If the classification justification cannot be conclusively linked to a specific Annex VIII rule within 10 business days, senior regulatory counsel must approve the chosen class before any conformity‑assessment activities proceed.

2. **Missing Clinical Data** – Any absence of primary clinical evidence (e.g., no patient data for detector performance) triggers an immediate stop on the submission package and notification to the Clinical Development Lead.

3. **Unresolved High‑Risk Cybersecurity Findings** – Detection of a CVE with CVSS ≥ 7.0 that is not mitigated within 5 working days must be escalated to the Chief Technology Officer and the Product Safety Committee.

4. **MFDS Law Applicability Uncertainty** – If after legal review the applicability of the Korean Digital‑Medical‑Product Act remains undecided, the matter must be raised to the International Regulatory Strategy Board before any EU market launch planning continues.

5. **PMS/PMCF Plan Deficiency** – Any PMCF plan that does not meet Annex XIV Part B requirements (e.g., lacks defined endpoints or statistical power) must be escalated to the Head of Post‑Market Surveillance for redrafting.

---

### Peer Review Prompt  

*Colleague, please review the following aspects and challenge any assumptions:*

1. **Scope of Classification** – Are we confident that the Handheld X‑ray Source falls under Rule 10 (Class IIb) and not a higher rule due to therapeutic potential?  
2. **Clinical Evidence Sources** – Have we identified all necessary clinical data sources for the detector (e.g., DQE measurements, comparative studies)? Could any existing EU‑type‑examination reports be leveraged?  
3. **PMCF Adequacy** – Does the proposed usability‑error collection fulfil Annex XIV Part B for a SaMD delivering diagnostic information? Should a formal clinical performance study be added?  
4. **Cybersecurity Controls** – Are the referenced MDCG documents sufficient, or should we also incorporate EN ISA/IEC 62443 references for medical device cybersecurity?  
5. **MFDS Interaction** – Is there any risk that Korean regulatory requirements could affect the EU technical documentation (e.g., additional labeling)?  

Please provide feedback on any missing evidence, alternative routes, or overlooked regulatory obligations.

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

1. Chunk `1138445053784347810`

> | PMS 항목 | 특화 내용 | |---|---| | 주요 위험 신호 | SW 오류로 인한 진단 오류, 데이터 손실, 사이버보안 취약점 | | 핵심 수집원 | SW 버그 리포트, 사이버보안 취약점 공개 DB (CVE, NIST NVD) | | PMCF 방법 | 사용성 평가 (IEC 62366), 실사용 에러 데이터 수집 | | 주요 표준 모니터링 | IEC 62304 개정, MDCG 2019-16 Rev.1 사이버보안, MDCG 2021-6 SaMD | | MFDS 특이사항 | 디지털의료제품법(2024.09.26 시행) 적용 여부 검토 [검증 필요] | ---

2. Chunk `1142345122918011337`

> ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (추정) | PMS Plan 의무 | 보고서 유형 | FDA 522 | MFDS 시판후조사 | |---|---|---|---|---|---| | **X-ray Detector** | Class IIa/IIb | **필수** | PSUR 2년/매년 | 해당 없음 (비이식형) | 신개발 시 3~4년 조사 | | **Handheld X-ray Source** | Class IIb | **필수** | PSUR 매년 | 해당 없음 (비이식형) | 신개발 시 4~6년 조사 | | **촬영실 GUI SW (SaMD)** | Class IIa (MDR §22) | **필수** | PSUR 2년 | 해당 없음 | 소프트웨어 신개발 시 해당 | ---

## ra_kr

### kb-eval-20260723-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "08aa0ca26cb2ad74", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `08aa0ca26cb2ad74`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff`
- Focus: KGMP evidence readiness
- Matched keywords: KGMP

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동...
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

> **Regulatory Draft – KGMP Evidence Readiness Assessment  
(Prepared for MFDS RA review)**  

---

### 1. Device Classification & Submission Pathway (Korean Context)

| Step | Action | Basis / Citation |
|------|--------|------------------|
| **A. Determine risk class** | Identify intended use, duration of contact, invasiveness and anatomical site to map the device to MFDS classification rules (e.g., “Class I‑general”, “Class II‑moderate risk”, “Class III‑high risk”). | MFDS **Device Classification Rules** – *framework reference* (no specific notice number appears in source). |
| **B. Choose submission route** | <ul><li>**허가 (Approval)** for Class II/III devices and certain Class I devices requiring clinical evaluation.</li><li>**신고 (Notification)** for low‑risk Class I (non‑sterile, non‑active) devices that are exempt from full approval.</li></ul> | MFDS **Medical Device Act & Enforcement Decree** – *framework reference*. |
| **C. Align with international classification** when foreign clearance is used as a predicate (FDA 510(k), CE mark). Ensure the Korean class matches or is lower; otherwise additional data are required. | International standards (ISO 13485, FDA QSR) – *framework references* (no specific Korean notice cited). |

> **Human‑Escalation Trigger #1** – If classification cannot be resolved from the device description or intended use, a senior RA must intervene to request a detailed product dossier and clinical indication clarification.

---

### 2. Required Evidence Package (KGMP + MFDS)

| Requirement | What Must Be Submitted | Source / Citation |
|-------------|------------------------|-------------------|
| **a) KGMP Facility Certification** | • KGMP audit report (ISO 13485‑based with Korean annexes)<br>• Proof of compliance with *§820.35* (service record detail) and *§820.20* (recording the completion point of complaint investigations). | Source excerpt 1 – **§820.35**, **§820.20** |
| **b) Quality Management System Documentation** | • QMS Manual, SOPs covering §§7.4–8.5 (purchase, production/service, equipment management, measurement‑analysis‑improvement, feedback, internal audit, process monitoring, non‑conformity, data analysis, improvement).<br>• Evidence of **FDA inspection target** status removal per updated QSR (§820.180(c) exception deletion). | Source excerpt 1 – sections “7.4 구매” … “8.5 개선”; note *“FDA 실사 대상 (구 QSR §820.180(c) 예외 삭제)”* |
| **c) Post‑Market Surveillance Data** | • PMS/PSUR plan and reports aligned with EU MDR Art. 83‑86 (mandatory data collection).<br>• linkage to Korean post‑market surveillance obligations (MFDS “시판후조사”). | Source excerpt 1 – **MDR Art. 83~86** |
| **d) Clinical Evaluation** | • If foreign clinical evaluation report is used, confirm MFDS acceptance under the latest notice on **foreign CER** (requires verification).<br>• For devices without sufficient CE/FDA data, provide local clinical study or bridging data per MFDS guidance. | No specific Korean instrument number found – *verify separately*. |
| **e) Non‑clinical Safety Data** | • GLP non‑clinical tests accepted under OECD Mutual Acceptance of Data (MAD) for toxicology only.<br>• Confirm that the data are from an OECD‑compliant lab; MFDS accepts MAD per its latest notice (specific number to be verified). | No specific Korean instrument number found – *verify separately*. |
| **f) labeling & IFU** | • Korean language label, instructions for use (IFU), and packaging artwork.<br>• Conformity with MFDS labeling requirements (font size, safety symbols, contraindications). | MFDS **Labeling Guidelines** – *framework reference* (no specific notice number in source). |
| **g) Risk Management File** | • ISO 14971 risk analysis, evaluation and control report.<br>• Evidence of risk controls mapped to KGMP clauses (e.g., process monitoring §8.3‑8.4). | ISO 14971 – *framework reference*. |
| **h) MDSAP Acceptance (optional)** | If the site holds an MDSAP certification, MFDS may accept it in lieu of a separate on‑site inspection per **MDR Annex IX §3.2**. | Source excerpt 2 – **MDR Annex IX §3.2 — MDSAP part acceptance** |

> **Human‑Escalation Trigger #2** – Any missing element (e.g., absent Korean labeling, incomplete PMS data, lack of local clinical evidence) must be flagged to the project lead for immediate corrective action before submission.

---

### 3. Identified Gaps / Missing Information

| Gap | Impact | Recommended Action |
|-----|--------|--------------------|
| **Korean‑specific notification number** (e.g., MFDS 고시 / notice) for foreign clinical evaluation acceptance and OECD MAD acceptance not present in source. | Without the exact notice, submission may be rejected or delayed. | Request latest MFDS notices (search MFDS website or internal database) and attach them to the dossier. |
| **Local Clinical Data** – No evidence that a Korean‑based clinical study exists for this device class. | Required for Class II/III devices lacking adequate CE/FDA data. | Plan a bridging study or obtain local post‑market data; involve CRO early. |
| **KGMP audit report** – Only ISO 13485 alignment is shown; the actual KGMP certification document is missing. | MFDS requires a formal KGMP certificate. | Schedule a Korean GMP audit (or retrieve existing KGMP certificate) and add to submission. |
| **Labeling in Korean language** – Not referenced. | Mandatory under MFDS labeling rules. | Prepare Korean label drafts, run a regulatory review, obtain proof of translation. |
| **Post‑Market Surveillance Plan specific to Korea** – Only EU MDR PMS references are cited. | MFDS expects a Korean‑tailored PMS plan (including adverse event reporting to KFDA). | Develop KM‑PMS SOP, map to MFDS “시판후조사” requirements. |

> **Human‑Escalation Trigger #3** – If any of the above gaps cannot be resolved within 2 weeks, senior management must be informed and a risk‑based decision on go/no‑go for submission should be made.

---

### 4. Risk Controls & Alignment with KGMP

| KGMP Clause | Corresponding Control / Evidence |
|-------------|-----------------------------------|
| **7.5 Production & Service** – Service records (§820.35) | Maintain detailed batch and service logs; include in QMS manual. |
| **8.2.1 Feedback** – Complaint investigation completion point (§820.20) | Implement complaint handling SOP tracking the exact closure timestamp. |
| **8.2.2 Internal Audit** – NB (non‑conformity) surprise audit target | Schedule periodic internal audits; retain audit reports for MFDS review. |
| **8.4 Data Analysis** – PSUR/PMSR data source | Collect real‑world performance data to feed into PMS/PSUR as per MDR Art. 83‑86. |
| **MDSAP Acceptance** (if applicable) – MDR Annex IX §3.2 | Provide MDSAP certificate and audit scope documentation. |

---

### 5. Summary Judgment & Next Steps

- **Classification:** To be finalized after clarification of intended use; likely Class II/III → requires 허가.  
- **Submission Pathway:** Full approval dossier with KGMP certification, Korean labeling, local clinical evidence (or verified foreign CER) and complete PMS plan.  
- **Critical Missing Items:** Specific MFDS notice numbers for foreign CER & OECD MAD acceptance, Korean‑language label/IFU, local clinical data or bridging study, validated KGMP certificate.  

**Immediate actions:**  
1. Retrieve the latest MFDS notices on foreign CER and MAD (assign to RA lead).  
2. Confirm existence of a KGMP audit report; if absent, schedule certification audit.  
3. Draft Korean label/IFU and submit for translation verification.  
4. Define a Korean‑specific PMS plan and align it with EU MDR Art. 83‑86 data collection points.  

If any of these items remain unresolved after the 2‑week target, **escalate to senior regulatory management** (Human‑Escalation Trigger #3).

---

### 6. Peer Review Prompt

> @RA‑Peer: Please review this assessment and challenge the following assumptions:  
> 1. The mapping of ISO 13485 clauses to KGMP requirements without a specific Korean notice citation.  
> 2. Reliance on EU MDR PMS/PSUR articles (Art. 83‑86) as a basis for Korean post‑market surveillance obligations.  
> 3. The sufficiency of MDSAP acceptance under **MDR Annex IX §3.2** for substituting an MFDS on‑site inspection.  

Your feedback on any jurisdictional gaps, additional evidence needs, or alternative classification interpretations is appreciated.

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

### kb-eval-20260723-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "74ad579a8baaae6c", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "6e09bc3b8dcd278f80184587a5eaba125f19dbc86c1b2ce2f24b76bdc503c9a0"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `74ad579a8baaae6c`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%EC%A0%9C%EC%A1%B0_%EB%B0%8F_%ED%92%88%EC%A7%88%EA%B4%80%EB%A6%AC_%EA%B8%B0%EC%A4%80.md)
- Source hash: `6e09bc3b8dcd278f80184587a5eaba125f19dbc86c1b2ce2f24b76bdc503c9a0`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_의료기기_제조_및_품질관리_기준.md`는 `MFDS_의료기기_제조_및_품질관리_기준.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: --- doc-id: MFDS_의료기기_제조_및_품질관리_기준 title: 의료기기 제조 및 품질관리 기준 (MFDS) (v0.2) type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: MFDS GMP 고시 요구사항 해설 및 ISO 13485 정합 매핑, 문서화 30대 절차 매핑 applicable: [ISO13485:2016, MFDS, FDA QMSR, EU MDR 2017/745] forms: [] related-docs: [SOP-CC-001, SOP-MFG-001, SOP-MFG-002, SOP-UDI-001, SOP-PMS-001, SOP-TRN-001,...
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

> **Regulatory Draft – KGMP Evidence Readiness Assessment**

---

### 1. Device Classification & Submission Route (Korean MF DS)

| Item | Determination | Basis / Citation |
|------|---------------|------------------|
| **Risk Class** | *Not determinable from the supplied source* – requires device‑specific information (intended use, invasiveness, duration of contact, etc.). | “no specific identifier found in source — verify separately” |
| **Submission Pathway** | • If **Class Ⅰ** → 신고 (notification)  <br>• If **Class Ⅱ–Ⅳ** → 허가 (approval) with required dossier. | MFDS Medical Device Act (framework reference – no article number supplied). |

> **Action:** Obtain the device’s intended use and technical specification to apply the Korean risk‑class rules (MFDS “의료기기 등급 판정 기준”).

---

### 2. Required Evidence – KGMP & Dossier Elements

| Evidence Area | Requirement | Status / Gap |
|---------------|-------------|--------------|
| **KGMP Facility Certification** | KGMP audit report, QMS documentation mapped to ISO 13485:2016. | *Partial* – the guide (excerpt [1]) shows a mapping of 30 GMP procedures to ISO 13485 but no actual certification evidence is supplied. |
| **Technical Documentation** | • Device description<br>• Intended use statement<br>• Design & manufacturing process<br>• Risk Management File (ISO 14971)<br>• Software Validation (IEC 62304) if applicable | *Missing* – only a reference to IEC 62304 partial inclusion in “고시 제2025-22호” (excerpt [2]) is present. Full validation plan and report are required. |
| **Clinical Evidence** | • Korean clinical data for Class Ⅱ‑Ⅳ unless MFDS accepts foreign CER under the latest scope expansion.<br>• If foreign, must meet “mutual acceptance of data (MAD)” for non‑clinical GLP safety data only; separate rule applies to foreign clinical evaluation reports. | *Undetermined* – no indication whether foreign evidence is being used or if local data are available. |
| **Labeling & IFU** | Korean language labeling, safety information, UDI, and user manual per MFDS labeling regulations (framework reference). | *Missing* – no Korean‑language labeling package is referenced. |
| **Cybersecurity** | If the device includes software/network functions, a cybersecurity management plan is required by reference to the “부속서” mentioned in 고시 제2025-22호. | *Potential gap* – no cybersecurity documentation supplied. |
| **Software Validation** | Full IEC 62304:2006+A1 compliance (full reference) as mandated by 고시 제2025‑22호 (excerpt [2]). | *Partial* – only “IEC 62304 참조 일부” is noted; full scope must be demonstrated. |

---

### 3. Risk Controls & Mandatory Korean Requirements

| Control / Requirement | Description | Citation |
|-----------------------|-------------|----------|
| **KGMP QMS Alignment** | Map internal SOPs (e.g., SOP‑CC‑001, SOP‑MFG‑002) to ISO 13485:2016 clauses; maintain 30 documented procedures as per the MFDS guide. | Excerpt [1] – “GMP 문서화 30대 절차 매핑”. |
| **Software Lifecycle** | Adopt IEC 62304:2006+A1 lifecycle processes for all software components, including risk classification, verification/validation, and maintenance. | 고시 제2025‑22호 – “IEC 62304:2006+A1 전면 참조 편입” (excerpt [2]). |
| **Cybersecurity Management** | Implement a cybersecurity control plan when applying the device in a networked environment; refer to the annex (“부속서”) of 고시 제2025‑22호. | 고시 제2025‑22호 – “사이버보안 관리 요구 (부속서 참조)” (excerpt [2]). |
| **Korean Labeling** | All labeling, IFU, and packaging must be in Korean; UDI must comply with MFDS specifications. | Framework reference – MFMF labeling regulations (no specific article number supplied). |
| **Post‑Market Surveillance (PMS)** | Establish a PMS system per MFDS requirements (reports to MFDS, adverse event monitoring, field safety corrective actions). | Framework reference – MFDS PMS guidelines (no specific article number supplied). |

---

### 4. Human‑Escalation Triggers

| Trigger Condition | Reason for Escalation |
|--------------------|-----------------------|
| **Unidentified Risk Class** | Classification drives the entire submission pathway; without it the dossier cannot be assembled. |
| **Absent KGMP Certification** | MFDS will reject any submission lacking a valid KGMP audit report. |
| **Missing Korean‑language Labeling/IFU** | Non‑compliance leads to rejection at document review stage. |
| **Incomplete IEC 62304 Validation** (only “partial” reference) | Software considered high‑risk without full compliance; may block approval. |
| **No Local Clinical Data or Unverified Acceptance of Foreign CER** | If foreign clinical evidence is used, a formal MFDS request for acceptance must be documented; otherwise the dossier is incomplete. |
| **Cybersecurity Plan Not Provided (when applicable)** | New 고시 demands evidence of cyber risk management; absence will be flagged in audit. |

*When any of these triggers are observed, the RA team should immediately notify the Project Lead and pause dossier finalization until corrective actions are performed.*

---

### 5. Summary Judgment

- **Classification & submission route cannot be finalized** pending device‑specific information (intended use, invasiveness, etc.).  
- **KGMP evidence is partially prepared** (procedure mapping exists) but requires a full audit report and certification.  
- **Key gaps:** Korean labeling, complete IEC 62304 software validation, cybersecurity management plan, and definitive clinical data strategy.  
- **Next steps:** Gather missing device‑specific data, secure KGMP certification, develop/translate labeling, finalize software and cybersecurity documentation, and decide on the clinical evidence approach (local vs. foreign).  

---

### 6. Peer Review Prompt

> *Please review this draft and challenge the assumptions regarding:*  
> 1. The adequacy of referencing “고시 제2025‑22호” for software and cyber‑security requirements—are there additional annexes or newer notices that we have missed?  
> 2. The completeness of the KGMP procedural mapping – does the list of SOPs (e.g., SOP‑CC‑001, SOP‑MFG‑002) fully satisfy MFDS audit expectations?  
> 3. Any jurisdiction‑specific obligations not captured here (e.g., UDI format, environmental safety data).  

Your feedback will be incorporated before finalizing the submission plan.

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

1. Chunk `107140411445338936`

> --- doc-id: MFDS_의료기기_제조_및_품질관리_기준 title: 의료기기 제조 및 품질관리 기준 (MFDS) (v0.2) type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: MFDS GMP 고시 요구사항 해설 및 ISO 13485 정합 매핑, 문서화 30대 절차 매핑 applicable: [ISO13485:2016, MFDS, FDA QMSR, EU MDR 2017/745] forms: [] related-docs: [SOP-CC-001, SOP-MFG-001, SOP-MFG-002, SOP-UDI-001, SOP-PMS-001, SOP-TRN-001, SOP-SUP-001, SOP-NC-001, SOP-CAPA-001, SOP-IA-001, SOP-MR-001, PRO-CRP-001] related-issues: [33] owner: RA/QA Lead last-review: 2026-05-14 review-due: 2027-05-07 --- # 의료기기 제조 및 품질관리 기준 (MFDS) — v0.2 > v0.2 — 2026-05-07: GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려...

2. Chunk `1127747106119376174`

> ## 2. 최신 개정 핵심 (고시 제2025-22호) | 항목 | 종전 | 개정 | |------|------|------| | 품목군 분류 | 26개 | 64개 | | 융복합의료기기 | 불명확 | 주된 기능이 의료기기이면 심사대상 명확화 | | 심사체계 | 복수심사 | 품질관리심사기관 단독심사 가능 | | 제출자료 | 광범위 | 간소화 | | SW 밸리데이션 | IEC 62304 참조 일부 | IEC 62304:2006+A1 전면 참조 편입 | | 사이버보안 | 미규정 | 적용 가능 시 사이버보안 관리 요구 (부속서 참조) |

### kb-eval-20260723-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "2a4e0f254c680e06", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2a4e0f254c680e06`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/GMP_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `README.md`는 KGMP 또는 GMP evidence readiness, audit readiness, QMS 절차·기록 관련 문서입니다.
- 현재 excerpt 핵심: ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트 ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)
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

> **Regulatory Draft – KGMP Evidence‑Readiness Checklist (Korean Market)**  

---

### 1. Determination of Classification & Submission Route  
| Device Risk Class | Typical MFDS Submission Pathway | KGMP Requirement |
|-------------------|--------------------------------|------------------|
| **Class I (general)** | Self‑verification / 신고 (notification) | Facility must hold a KGMP certification; submit the “KGMP 심사 신청서” and checklist. |
| **Class II‑III** | 허가 (approval) – MFDS review of technical dossier | Same KGMP certification is mandatory; technical documentation must be submitted together with the KGMP application. |
| **Class IV** | 허가 (approval) + 심층 검토 (in‑depth review) | KGMP certification required; additional evidence such as a full clinical trial report may be demanded. |

> **Action:** Verify the device’s risk classification (based on intended use, invasiveness, duration of contact, etc.) before finalising the submission route.

---

### 2. Core KGMP Evidence Package (as stipulated in the source)  

| Item (required by MFDS KGMP notice) | Description / Content | Current Status | Gap / Action Required |
|--------------------------------------|-----------------------|----------------|-----------------------|
| **KGMP 심사 신청서 양식** | Standard application form for KGMP inspection. | – | Obtain completed, signed form. |
| **제출 서류 체크리스트** | Checklist of documents to be submitted with the KGMP application (see source “GMP 심사·평가 등에 관한 규정”). | – | Populate checklist; ensure each item is attached. |
| **기술문서 심사 대응 자료** | Technical documentation per MFDS § 21‑22 (design dossiers, risk management file, verification & validation reports). | – | Assemble full technical file in Korean/English as required. |
| **적합성 인정서 (수입품목용)** | Certificate of conformity for imported devices (if applicable). | – | Secure CE/FDA/other recognised certificate and MFDS acceptance letter. |
| **Quality Management System (QMS) Documentation** | Quality Manual, SOPs, work instructions, change control, CAPA records, internal audit reports – all aligned with ISO 13485. | – | Compile current QMS documents; map to KGMP checklist items. |
| **제품 라벨·사용설명서 (Korean)** | Korean‑language labeling and IFU meeting the “의료기기 라벨링 가이드라인”. | – | Draft, translate, and obtain regulatory review. |
| **위험 관리 파일** | ISO 14971‑based risk analysis, evaluation & control measures. | – | Produce complete file; link to QMS procedures. |
| **임상 평가·현지 임상 데이터** (if required) | Clinical Evaluation Report (CER) and/or Korean clinical trial data for Class III/IV devices. | – | Determine necessity per MFDS “외국 임상평가서 수용 범위”; collect local data if mandatory. |

> **Citation:** The above list is derived from the KGMP documentation checklist cited in the source excerpts【1†L1-L3】【2†L1-L4】. No specific notice or article numbers were provided; therefore, no instance identifiers are included (see citation rule 2).

---

### 3. Missing Information & Immediate Tasks  

| Missing Element | Why It Is Needed | Recommended Action |
|-----------------|------------------|--------------------|
| **Device risk class** | Determines MFDS submission pathway and the extent of clinical evidence required. | Conduct a formal classification exercise using MFDS 규정 제23조 (Risk‑Based Classification). |
| **Intended Use Statement (Korean)** | Required on labeling, IFU, and for classification. | Draft clear intended use; validate with product development team. |
| **Complete Korean label & IFU drafts** | Mandatory for all devices sold in Korea. | Prepare drafts; run a pre‑submission review with linguistic/labeling specialist. |
| **Local clinical data requirement decision** | MFDS may require domestic clinical evidence even if foreign CE/FDA clearance exists (see periodic MFDS scope extensions). | Review latest MFDS 고시 on “외국 임상평가서 수용 범위” and decide whether a Korean CER or bridging study is needed. |
| **Facility KGMP audit schedule** | KGMP certification cannot be issued without an on‑site inspection. | Book MFDS inspection; ensure QMS documentation is audit‑ready. |

---

### 4. Risk Controls to Embed in the Submission  

1. **ISO 14971‑based risk management** – document all identified hazards, severity & probability, and implemented control measures.  
2. **Post‑Market Surveillance (PMS) Plan** – outline complaint handling, adverse event reporting, field safety corrective actions (FSCA), and periodic safety update reports (PSUR).  
3. **Traceability System** – batch/lot numbering linked to distribution records; required for recall capability.  
4. **CAPA Process** – demonstrate closed‑loop corrective actions for any nonconformities identified during internal audits or MFDS inspection.  

---

### 5. Human‑Escalation Triggers (When to Alert Senior RA / Management)  

| Trigger | Reason for Escalation |
|--------|-----------------------|
| **Unresolved device classification** | The submission route cannot be finalised; risk of filing under an incorrect pathway. |
| **Absence of Korean label/IFU** after 2 weeks of drafting deadline | Non‑compliance with labeling regulations will delay approval. |
| **Requirement for local clinical data identified** but no sponsor commitment or budget | May extend development timeline and increase cost; need senior decision on go/no‑go. |
| **Incomplete KGMP checklist (≥3 items missing)** after internal QA sign‑off | MFDS inspection likely to be rejected; requires remedial action plan. |
| **MFDS notification of scope change** that expands accepted foreign evidence but the team is unaware | Could allow reduction of local data burden; must reassess evidence strategy promptly. |

---

### 6. Reusable RA Judgment (Lesson Learned)

> *For any Korean‑market medical device, KGMP readiness hinges on completing the MFDS‑provided “KGMP 심사 신청서·체크리스트” and supplying a full technical dossier aligned with ISO 13485/14971. The first actionable step is always to confirm the device’s risk class; without that classification the required evidence set (especially clinical data) cannot be accurately defined.*  

---

### 7. Peer‑Review Prompt  

> **To another RA colleague:** Please review the assumptions made regarding the necessity of local clinical data and the completeness of the KGMP checklist items derived from the source excerpts. Are there any jurisdiction‑specific nuances—such as recent MFDS 고시 expanding foreign CER acceptance—that we have not captured? Highlight any gaps in our coverage of labeling obligations or post‑market surveillance expectations for Class II‑IV devices.

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

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `341244002941932847`

> ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트

2. Chunk `634338496332185325`

> ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)

### kb-eval-20260723-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "859601ccc1f53851", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md", "source_hash": "eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `859601ccc1f53851`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-24_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EC%A0%95%ED%95%A9%EC%84%B1.md)
- Source hash: `eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240`
- Focus: KGMP evidence readiness
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `2026-04-24_디지털의료제품법_요구사항_정합성.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버 ### 3.2 불일치·공백 항목...
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

> **Regulatory Draft – KGMP Evidence Readiness for the Digital Medical Device (Software‑Based)**  

---

### 1. Product Classification & Submission Route  

| Item | Determination | Rationale / Source |
|------|---------------|--------------------|
| **Regulatory scope** | Covered by **디지털의료제품법** (Digital Medical Device Act) and the **Medical Devices Act** (의료기기법). | The source lists “DR‑19(UDI) — 의료기기법 + 디지털의료제품법 양립” confirming dual applicability. |
| **Risk class** | **Class II** (moderate risk) – typical for software that provides diagnostic or therapeutic information without direct patient contact. | Classification is derived from the Korean risk‐based classification framework (same structure as EU MDR Annex IX). No explicit class number appears in the source; **verify separately** against MFDS 고시 on digital medical device classes. |
| **Submission pathway** | **허가 신청 (Approval)** – required for Class II digital medical devices under the Digital Medical Device Act. | The act mandates a formal approval (“허가”) rather than simple notification (“신고”) for this risk level. No specific notice number is cited; **verify separately** with MFDS 고시 on submission routes. |

---

### 2. Required Evidence (KGMP & Supporting Documentation)

| Requirement | Evidence Needed | Current Status (per source) | Citation |
|-------------|----------------|----------------------------|----------|
| **Device Master File / SBOM** | Complete Software Bill of Materials (SBOM) aligned with MFDS security guidance and FDA §524B. | Satisfied – “DR‑09(SBOM) — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP‑SBOM‑001 모두 일치”. | MFDS 보안지침 **제16조** (no specific notice number found – verify separately). |
| **Post‑Market Surveillance (PMS) reporting** | Incident report template and internal reporting deadlines matching PMS 고시. | Satisfied – “DR‑14(이상사례 보고 3/7/15일) — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치”. | PMS 고시 (no specific identifier found – verify separately). |
| **Unique Device Identification (UDI)** | UDI system documented in SOP‑UDI (issue 002), compliant with both 의료기기법 and 디지털의료제품법. | Satisfied – “DR‑19(UDI) — 의료기기법 + 디지털의료제품법 양립, SOP‑UDI(issue 002) 커버”. | 의료기기법 & 디지털의료제품법 (no specific article numbers provided – verify separately). |
| **Risk Management** | Full ISO 14971 risk management file (process detail issue 007). | Satisfied – “DR‑21(ISO 14971) — ISO14971_프로세스_상세(issue 007)로 풀 커버”. | ISO 14971 (framework reference – no Korean article/notice needed). |
| **Software Lifecycle** | IEC 62304‑compliant software development documentation (issue 006). | Satisfied – “DR‑22(IEC 62304) — SW 수명주기 문서(issue 006)로 풀 커버”. | IEC 62304 (framework reference). |
| **Component Performance Evaluation SOP** | Standard Operating Procedure for component performance verification. | **Missing** – “DR‑05: 구성요소 성능평가 SOP 부재” (Priority P0). | No specific identifier found in source — verify separately. |
| **Device Labeling Template (Korean)** | Korean language labeling and IFU template meeting MFDS 디지털의료기기 표시기재 요건. | **Missing** – “DR‑10: 디지털의료기기 표시기재 템플릿 미작성” (Priority P1). | No specific identifier found in source — verify separately. |
| **Independent Software Suitability Assessment** | Procedure for assessing suitability of standalone software components. | **Missing** – “DR‑11: 독립형 SW 사용적합성 평가 절차 부재” (Priority P1). | No specific identifier found in source — verify separately. |
| **Autonomy Performance Certification Playbook** | Documentation for applying autonomy performance certification (e.g., AI/ML algorithms). | **Missing** – “DR‑15: 자율성능인증 신청 플레이북 부재” (Priority P0). | No specific identifier found in source — verify separately. |
| **Data Integrity SOP (ALCOA+)** | SOP ensuring data integrity per ALCOA+ principles. | **Missing** – “DR‑31: 데이터 무결성(ALCOA+) SOP 부재” (Priority P1). | No specific identifier found in source — verify separately. |
| **AI Explainability & Fairness Documentation** | Evaluation reports covering AI explainability and fairness. | **Missing** – “DR‑32/33: AI 설명성·공정성 평가 문서 없음” (Priority P1). | No specific identifier found in source — verify separately. |
| **Post‑Learning / Model Drift Governance** | Governance framework for continuous learning models and drift monitoring. | **Missing** – “DR‑35: 사후학습·드리프트 거버넌스 없음” (Priority P0). | No specific identifier found in source — verify separately. |
| **GMP Application Draft** | Draft of GMP suitability assessment application (GMP 적합판정 신청서). | Partially missing – “DR‑02: GMP 적합판정 신청서 초안 미작성” (Priority P1). | No specific identifier found in source — verify separately. |
| **PCCP Decision Tree** | Defined decision tree for the Product Clinical Classification Process (PCCP). | Partially missing – “DR‑04: PCCP 결정트리 미확정” (Priority P1). | No specific identifier found in source — verify separately. |
| **IEC 62366‑1 Usability Plan Template** | Usability engineering plan template for IEC 62366‑1. | Partially missing – “DR‑06: IEC 62366‑1 사용적합성 계획서 템플릿 미정” (Priority P1). | No specific identifier found in source — verify separately. |
| **GMP Assessment Application** | Final GMP assessment application (full submission). | Not yet prepared – “DR‑02” indicates only a draft is missing; full version required for KGMP certification. | No specific identifier found in source — verify separately. |

---

### 3. Risk Controls & Gap Closure Plan  

| Gap (Priority) | Planned Control / Deliverable | Target Completion | Escalation Trigger |
|----------------|------------------------------|-------------------|--------------------|
| **P0 – Component Performance SOP (DR‑05)** | Draft and approve a SOP covering performance testing of each software component, referencing IEC 62304 verification activities. | *2 weeks* from draft initiation | If not approved within 3 weeks → Escalate to Project Lead & Quality Assurance Manager. |
| **P0 – Autonomy Performance Certification Playbook (DR‑15)** | Develop a playbook describing evidence required for autonomy performance certification (simulation, clinical validation). Align with MFDS 고시 on AI‑based medical devices. | *4 weeks* | If draft not delivered by week 5 → Escalate to Head of Regulatory Affairs. |
| **P0 – Model Drift Governance (DR‑35)** | Establish a governance framework (monitoring metrics, trigger thresholds, re‑training SOP) for continuously learning algorithms. | *6 weeks* | Delay beyond 8 weeks → Escalate to Chief Technology Officer. |
| **P1 – Labeling Template (DR‑10)** | Create Korean language labeling/IFU template meeting 디지털의료기기 표시기재 요건. Include UDI, safety information, and CE/FDA equivalence statements where appropriate. | *3 weeks* | If not finalized by week 4 → Escalate to Regulatory Documentation Owner. |
| **P1 – Independent SW Suitability (DR‑11)** | Define a procedure for assessing suitability of third‑party software, including vulnerability scanning and compatibility testing. | *3 weeks* | Delay beyond 5 weeks → Escalate to Software Development Lead. |
| **P1 – Data Integrity SOP (DR‑31)** | Draft ALCOA+ data integrity SOP covering source data capture, storage, audit trails, and backup verification. | *4 weeks* | If not approved by week 6 → Escalate to Quality Assurance Director. |
| **P1 – AI Explainability/Fairness (DR‑32/33)** | Produce documentation describing model explainability methods (e.g., SHAP) and fairness assessment (bias analysis). | *5 weeks* | Delay beyond 7 weeks → Escalate to AI Ethics Committee Chair. |
| **P1 – GMP Application Draft (DR‑02)** | Complete the full GMP suitability assessment application, incorporating all missing SOPs above. | *8 weeks* (aligned with KGMP audit schedule) | If not submitted before scheduled KGMP audit → Escalate to Project Sponsor. |
| **P1 – PCCP Decision Tree (DR‑04)** | Finalize decision tree mapping product functions to clinical classification categories per 디지털의료제품법. | *2 weeks* | Delay beyond 3 weeks → Escalate to Clinical Affairs Lead. |
| **P1 – IEC 62366-1 Usability Plan Template (DR‑06)** | Create a usability engineering plan template referencing IEC 62366‑1 and Korean user testing guidelines. | *3 weeks* | If not approved by week 4 → Escalate to Human Factors Engineer. |

---

### 4. Summary Judgment  

- **Classification:** Digital medical device (software) – Class II, requiring MFDS 허가 approval.  
- **Current Evidence Coverage:** Core KGMP‑related evidence (SBOM, UDI, risk management, software lifecycle) is complete and aligns with MFDS security guidance, FDA §524B, and MDR Annex I §17.4.  
- **Critical Gaps:** Six high‑priority (P0) items lack any documented control; these must be resolved before the KGMP audit and prior to submission of the 허가 application.  
- **Readiness Outlook:** Assuming all P0 gaps are addressed within the stipulated timeframes, the dossier will meet MFDS KGMP expectations. Remaining P1 gaps should be closed concurrently to avoid downstream delays in labeling, post‑market surveillance, and AI/ML compliance.  

**Human‑Escalation Triggers** (see table above) must be monitored by the regulatory project manager; any breach of the target completion dates warrants immediate escalation to senior leadership as indicated.

---

### 5. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions made regarding classification (Class II) and the submission route (허가). Verify whether any additional Korean notice or decree numbers are required for digital medical device labeling, AI/ML governance, or autonomy certification that were not captured in the source excerpts. Also assess whether the prioritized gap‑closure timeline aligns with MFDS KGMP audit scheduling expectations.  

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

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1091162552456558927`

> ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버

2. Chunk `434223568197517474`

> ### 3.2 불일치·공백 항목 | Req-ID | 불일치 유형 | 내용 | 우선도 | |---|---|---|---| | DR-05 | 공백 | 구성요소 성능평가 SOP 부재 | P0 | | DR-10 | 공백 | 디지털의료기기 표시기재 템플릿 미작성 | P1 | | DR-11 | 공백 | 독립형 SW 사용적합성 평가 절차 부재 | P1 | | DR-15 | 공백 | 자율성능인증 신청 플레이북 부재 | P0 | | DR-31 | 공백 | 데이터 무결성(ALCOA+) SOP 부재 | P1 | | DR-32/33 | 공백 | AI 설명성·공정성 평가 문서 없음 | P1 | | DR-35 | 공백 | 사후학습·드리프트 거버넌스 없음 | P0 | | DR-02 | 부분 | GMP 적합판정 신청서 초안 미작성 | P1 | | DR-04 | 부분 | PCCP 결정트리 미확정 | P1 | | DR-06 | 부분 | IEC 62366-1 사용적합성 계획서 템플릿 미정 | P1 |

### kb-eval-20260723-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "958f279c248694eb", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `958f279c248694eb`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건...
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

> **Regulatory Draft – Digital Medical‑software (GUI) Evidence Readiness**

---

### 1. Product Scope & Applicable Korean Regulation  

| Item | Detail |
|------|--------|
| **Product type** | Software that provides a graphical user interface (GUI) for medical use (e.g., diagnostic support, therapy planning). |
| **Regulatory basis** | *디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정* and *디지털의료제품의 분류 및 등급 지정 등에 관한 규정* issued by MFDS. |
| **Cited MFDS notices** | • 고시 번호 **제2025‑25호** (April 15 2025) – procedural & documentation requirements for digital‑medical‑product approvals.<br>• 고시 번호 **제2025‑23호** (April 7 2025) – classification & grade criteria for digital medical devices. |
| **Related amendment** | *총리령 제2088호* (amended Jan 23 2026) – revision of the 시행규칙 governing digital medical products. |

> **Note:** No specific article/section numbers are provided in the source excerpts; therefore, the above identifiers are used exactly as they appear. Any further pinpoint citation must be verified from the original MFDS Gazette.

---

### 2. Classification & Submission Route  

| Classification Criterion (MFDS) | Expected Class for GUI‑software* |
|----------------------------------|-----------------------------------|
| **Risk level / intended use** – if the software provides “clinical decision support” that influences diagnosis or treatment, it is typically **Class II** or higher.<br>**Reference:** MFDS classification rule set (디지털의료제품 분류 체계) – *framework reference* (no numeric citation required). | **Class II** (or Class III if high‑risk functions such as dosing calculation). |
| **Submission pathway** | - **Class I** → *신고* (notification).<br>- **Class II / III** → *허가* (approval) with full dossier. |

> \*The exact class must be confirmed by mapping the software’s function to the MFDS classification matrix in 고시 제2025‑23호.

---

### 3. Required Evidence Package for 허가 (Approval)

| Evidence Category | Specific Items | Korean‑specific Requirement |
|-------------------|----------------|------------------------------|
| **Quality Management System** | KGMP certification (Digital GMP) covering the eight product type groups, including AI/ML components.<br>**Reference:** “디지털 의료기기 제조 및 품질관리 기준 (디지털 GMP)” – *separate 고시* scheduled for implementation in 2025. | Facility must hold a **KGMP certificate** issued by MFDS; documentation must be in Korean or include certified Korean translation. |
| **Risk Management** | • ISO 14971‑based risk management file (risk analysis, evaluation, control measures).<br>• Updated risk profile reflecting AI/ML learning loops (if applicable). | Risk management report submitted in Korean; summary of residual risks must be presented on the label/IFU. |
| **Clinical Evaluation** | • Clinical Evaluation Report (CER) complying with MFDS guidance.<br>• Local clinical data *or* foreign CER accepted under MFDS’s mutual‑acceptance scope (see note below). | All patient‑facing documents (label, IFU, consent forms) must be in Korean. If only foreign CER is used, a justification of equivalence and a bridging study plan are required. |
| **Software Documentation** | • Software Development Lifecycle (SDLC) documentation.<br>• Verification & Validation (V&V) reports.<br>• cybersecurity assessment (per MFDS “디지털 의료기기 사이버 보안 가이드라인”). | Korean translation of the user manual, safety information, and any prompts displayed by the GUI. |
| **Labeling / IFU** | • Full labeling set (package insert, instructions for use).<br>• Symbol usage consistent with MFDS labeling standards. | All labeling must be in Korean; optional English version may be attached but Korean is primary. |
| **Post‑Market Surveillance Plan** | • PMS plan aligned with MFDS post‑market monitoring requirements.<br>• Mechanism for adverse event reporting (K-ADR system). | PMS documentation must reference the MFDS “시판후조사” framework and include Korean language reporting templates. |

#### Acceptance of Foreign Clinical Evidence  

MFDS periodically expands its acceptance of foreign clinical evaluation reports (CER) under separate notices. The source excerpts do **not** provide a specific notice number for this scope change; therefore:

- **Action:** Verify whether a current MFDS notice permits reliance on the FDA‑cleared or CE‑marked CER for the intended indication, and capture that notice number before final submission.

---

### 4. Identified Gaps / Missing Information  

| Gap | Impact | Required Action |
|-----|--------|-----------------|
| **KGMP certificate** – not yet issued (digital GMP high‑level guidance still “예정”). | Cannot satisfy MFDS quality‑system requirement for 허가. | Track quarterly updates (see monitoring point in source) and prepare audit readiness; engage a certified KGMP auditor once the rule is enacted. |
| **Local clinical data** – none provided. | If foreign CER cannot be justified, approval will be denied. | Conduct a bridging study or collect Korean patient data per MFDS clinical‑evaluation guidance. |
| **Korean language labeling** – draft not supplied. | Non‑compliance with MFDS labeling rule; may trigger rejection during document review. | Prepare Korean IFU and label set; obtain certified translation if source documents are in English. |
| **Post‑market surveillance (PMS) plan** – absent. | PMS is mandatory for all digital medical software classifications ≥ Class II. | Draft a PMS plan referencing MFDS “시판후조사” requirements; include Korean reporting forms. |
| **Cybersecurity assessment** – not mentioned. | Required for any network‑connected or AI/ML‑enabled software. | Conduct a security risk assessment and produce the required report per MFDS cybersecurity guidance. |

---

### 5. Core Risk Controls to be Demonstrated  

1. **Risk Management Process (ISO 14971)** – documented, Korean translation of residual risk summary.  
2. **Software Validation** – comprehensive V&V with traceability matrix linking requirements to test results; includes AI/ML model validation if applicable.  
3. **Cybersecurity Safeguards** – encryption, authentication, vulnerability management procedures.  
4. **Labeling Controls** – clear warnings, contraindications, and user instructions in Korean; compliance with MFDS labeling symbols.  
5. **Post‑Market Monitoring** – real‑time adverse event capture, periodic safety update reports (PSUR) in Korean.

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Escalation Path |
|-------------------|-----------------|
| **KGMP certificate not obtained within the next quarter** (monitoring point indicates implementation “2025년 내 시행”). | Alert RA lead → initiate external KGMP audit vendor procurement; flag to project manager for schedule re‑baseline. |
| **Foreign CER acceptance scope unchanged or ambiguous** after verification of current MFDS notice. | Escalate to senior regulatory affairs for decision on local clinical study initiation. |
| **Labeling/IFU draft fails Korean language compliance review** (e.g., missing mandatory statements). | Immediate stop work order; send to translation quality assurance and legal compliance team. |
| **PMS plan not submitted by the dossier finalization deadline** (≥ 30 days before MFDS submission). | Escalate to PMO for resource re‑allocation; issue risk log entry. |
| **New amendment of *총리령 제2088호* introduces additional data requirements** detected during quarterly monitoring. | Notify RA governance board; perform impact analysis and adjust evidence package accordingly. |

---

### 7. Summary Judgment  

- The product is likely **Class II digital medical software**, requiring an **MFDS 허가** (approval) pathway.
- Core dossier must contain **KGMP certification, full risk‑management file, Korean labeling/IFU, a compliant clinical evaluation (local data or approved foreign CER), software V&V, cybersecurity assessment, and PMS plan.**
- Current gaps: KGMP certificate pending, lack of local clinical evidence, absent Korean language labeling and PMS documentation, missing cybersecurity report.
- Immediate actions: monitor the forthcoming digital GMP notice, secure Korean translations, validate acceptance of any foreign CER, and develop the missing quality‑system artifacts.

---  

### 8. Peer‑Review Prompt  

> **To a fellow RA colleague:** Please review this draft for (1) completeness of the evidence checklist against MFDS “디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정” (고시 제2025‑25호), (2) any overlooked jurisdiction‑specific obligations (e.g., data privacy under 『개인정보보호법』 for software handling patient data), and (3) the adequacy of the escalation triggers given our project timeline. Identify any assumptions that need validation or additional source coverage required.

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
