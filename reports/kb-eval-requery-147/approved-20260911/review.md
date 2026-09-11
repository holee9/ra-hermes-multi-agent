# #147 재질의 결과 검토 자료

배치: `approved-20260911` · 시도 11 · 결과 11 · 응답 수신 6

> **이 자료는 사람 판정을 대신하지 않는다.** 자동 점검은 기계로 확인 가능한 것만 본다 —
> 통과했다고 규제적으로 옳다는 뜻이 아니고, 규제 판단은 사람이 해야 한다.

## 요약

| case | 수신 | 자 | old source | new source | 미검증 식별자 | 인용 오류 | 판정 |
|---|---|---|---|---|---|---|---|
| `0260716-it01-ra_eu-005` | X | 0 | PMS_Plan_MDR_Article84_템플릿 | Clinical_Evaluation_MDR_동등 | - | 0 | 응답 없음 |
| `0260717-it01-ra_eu-004` | X | 0 | EUDAMED_모듈별_등록_실무가이드.md | 158_08_SOP-PMS-001_v0.3_QM | - | 0 | 응답 없음 |
| `0260718-it01-ra_kr-003` | X | 0 | 진단용_방사선_발생장치_안전관리규칙_제1122호 | MFDS_보완자료_대응전략.md | - | 0 | 응답 없음 |
| `0260719-it01-ra_us-003` | X | 0 | 959_FDA_510k_RTA_기초보강_3주차_ | eSTAR_02_Substantial_Equiv | - | 0 | 응답 없음 |
| `0260720-it01-ra_eu-005` | X | 0 | PMS_Plan_MDR_Article84_템플릿 | Clinical_Evaluation_MDR_동등 | - | 0 | 응답 없음 |
| `0260722-it02-ra_us-002` | O | 6289 | 959_FDA_510k_RTA_기초보강_3주차_ | eSTAR_02_Substantial_Equiv | - | 0 | 자동 점검 통과 |
| `0260722-it02-ra_us-003` | O | 5535 | 979_FDA_510k_RTA_기초보강_4주차_ | eSTAR_02_Substantial_Equiv | - | 0 | 자동 점검 통과 |
| `0260722-it02-ra_us-004` | O | 7872 | 220_13_FDA_510k_RTA_핵심양식_초 | eSTAR_02_Substantial_Equiv | - | 0 | 자동 점검 통과 |
| `0260722-it02-ra_eu-005` | O | 9628 | 902_AUDIT_GUIDE-VIG-001_EU | 943_AUDIT_CHK-DR-001_EU_MD | - | 0 | 자동 점검 통과 |
| `0260723-it01-ra_kr-002` | O | 9337 | MFDS_디지털의료기기_표시기재_가이드라인_대응 | MFDS_디지털의료제품법_하위고시_추적.md | - | 0 | 자동 점검 통과 |
| `0260724-it03-ra_kr-005` | O | 7370 | README.md | MFDS_보완자료_대응전략.md | - | 0 | 자동 점검 통과 |

## 자동 점검이 본 것 / 보지 않은 것

**본 것**: 응답이 인용한 FDA 식별자(K/P/DEN 번호)가 전달한 발췌에 실제로 있는지, 구조적으로 불가능한 조문 인용이 있는지, 응답 길이.

**보지 않은 것**: 규제 판단의 타당성, 분류·경로 선택의 정확성, 인용 조문이 **맥락에 맞는지**, 새 소스가 그 focus 에 정말 적절한지. 전부 사람 판정 영역이다.

### kb-eval-20260722-it02-ra_us-002

focus: 510(k) predicate strategy

<details><summary>응답 전문</summary>

```
**Regulatory Draft – 510(k) Substantial‑Equivalence Strategy**  

---

### 1. Classification & Submission Route (bottom line)

*Because the device’s intended use and technological characteristics have not been provided, a definitive classification cannot be assigned at this stage.*  
- **If** the device is found to belong to an FDA‑recognized Class I/II product code with no special controls, the **Premarket Notification (510(k))** pathway applies.  
- **If** it falls under a Class III product code or presents new safety/effectiveness questions, a **De Novo** or **PMA** route will be required.

The determination must follow the FDA 510(k) SE decision‑flow (DP1–DP5) outlined in the eSTAR guidance.  

> **Citation:** 21 U.S.C. §360c(i)(1)(A); 21 CFR 807.92(a)(3) – legal definition of Substantial Equivalence and its two core requirements (same intended use; same or non‑conflicting technological characteristics).  

---

### 2. Required Evidence – What must be in the 510(k) submission

| Decision Point | Evidence needed to satisfy the point | Typical dossier components |
|----------------|--------------------------------------|----------------------------|
| **DP1** – Predicate is a legally marketed device (cleared via 510(k), PMA, or pre‑amendment) | Copy of predicate’s FDA clearance/license; confirmation that it is not a Class III PMA‑only device. | – Predicate 510(k) summary/letter<br>– Device registration number (if available) |
| **DP2** – Same Intended Use | Narrative comparison of intended uses (indications, patient population, clinical setting). | – Indications for use statements for both devices |
| **DP3** – Same Technological Characteristics | Side‑by‑side table of design, materials, energy source, algorithmic approach, etc. | – Device specifications<br>– Block diagrams / schematics |
| **DP4 (if DP3 = “No”)** – No new safety/effectiveness questions | Scientific justification why the differences do *not* raise a new question (bench testing, literature, risk analysis). | – Non‑clinical bench data<br>– Risk management file (ISO 14971) showing mitigated hazards |
| **DP5** – Performance Data demonstrates at least equal safety & effectiveness | Comparative performance results (e.g., accuracy, precision, functional tests) that meet or exceed predicate metrics. | – Test protocols & reports<br>– Statistical analysis |

---

### 3. Missing Information (human‑escalation triggers)

| Gap | Why it matters | Trigger for human review |
|-----|----------------|--------------------------|
| **Device description** (intended use, anatomical site, patient population) | Needed to assess DP2. | If unavailable → *Escalate*: “Provide intended‑use statement.” |
| **Predicate identification** (product code, 510(k) number, clearance date) | Required for DP1 and baseline comparison. | If no legally marketed predicate can be identified → *Escalate*: “Consider De Novo or PMA route.” |
| **Technological characteristics matrix** | Determines DP3/D​P4 outcome. | Absence of detailed design data → *Escalate*: “Submit engineering specs for comparison.” |
| **Risk analysis showing no new safety questions** | Critical for DP4 clearance when tech differs. | Missing or incomplete ISO 14971 risk file → *Escalate*: “Complete risk management documentation.” |
| **Performance test results** (bench, animal, or clinical) | Required to satisfy DP5. | Lack of comparative data → *Escalate*: “Generate and include performance testing.” |

---

### 4. Risk Controls & Quality System Reference (quick outline)

1. **Risk Management** – Perform ISO 14971‑based risk analysis; demonstrate that any new hazards introduced by differing technology are mitigated to an acceptable level (supports DP4).  
2. **Design Validation** – Conduct validation activities reflecting intended use.  
3. **Labeling Review** – Ensure labeling (21 CFR 801) matches cleared indications and does not introduce new uses.  

> *Note:* Specific CFR citations for risk management (e.g., 21 CFR 820) are **not present in the source excerpt**; they should be added once the device class is confirmed.

---

### 5. Citations from Source Excerpts

| Item | Source citation |
|------|-----------------|
| Legal definition of Substantial Equivalence (two core criteria) | 21 U.S.C. §360c(i)(1)(A); 21 CFR 807.92(a)(3) |
| Decision‑point flow (DP1–DP5) | FDA eSTAR “The 510(k) Program: Evaluating Substantial Equivalence in Premarket Notifications” (2014‑07‑28 Final), Appendix A Flowchart – summarized in the source under **1.2 SE 판정 흐름도** |
| Guidance URLs for predicate searching & overall 510(k) process | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k ; https://www.fda.gov/regulatory-information/search-fda-guidance-documents/510k-program-evaluating-substantial-equivalence-premarket-notifications-510k ; https://www.fda.gov/media/82395/download ; https://www.fda.gov/medical-devices/premarket-notification-510k/how-find-and-effectively-use-predicate-devices ; https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-E/section-807.92 |

---

### 6. Human‑Escalation Summary (action list)

| Situation | Escalate to |
|-----------|-------------|
| No legally marketed predicate identified (DP1 failure) | Regulatory Lead – evaluate De Novo / PMA feasibility |
| Intended use differs from any known predicate (DP2 failure) | Product Development – clarify or adjust indications |
| Technological differences raise new safety/effectiveness questions (DP4 “Yes”) | Clinical/Pre‑clinical Team – plan additional testing; consider higher risk pathway |
| Insufficient performance data to prove equivalence (DP5 “No”) | Testing Lab / Engineering – generate missing data |
| Any of the *Missing Information* items above remain unresolved after reasonable effort | Project Manager – decision on go/no‑go or redesign |

--- 

**Bottom line:** Proceed with a traditional 510(k) only after confirming a legally marketed
```

</details>

### kb-eval-20260722-it02-ra_us-003

focus: 510(k) predicate strategy

<details><summary>응답 전문</summary>

```
**Regulatory Draft – 510(k) Substantial‑Equivalence (SE) Strategy**

---

### 1. Device Overview (to be supplied)
| Item | Required Information |
|------|-----------------------|
| **Trade name / model** | —  |
| **Intended use statement** (clinical indication, patient population, setting) | —  |
| **Device description & core technology** (materials, energy source, software algorithm, etc.) | —  |

> *Missing: All of the above must be supplied before any classification or predicate analysis can be performed.*

---

### 2. Classification & Submission Route  
- **Presumed pathway:** Premarket Notification – 510(k) (Class II).  
- **Citation:** The legal definition of SE is found at **21 U.S.C. §360c(i)(1)(A)** and **21 CFR 807.92(a)(3)**.  

> *Missing:* The specific FDA product code / regulation part (e.g., 21 CFR 892.2050 for medical‑image management software) is not identified in the source. Provide the device’s primary function to confirm the correct subsection.

---

### 3. Predicate Device Strategy  
Follow the FDA eSTAR decision‑point flowchart (Appendix A, “The 510(k) Program: Evaluating Substantial Equivalence”):

| Decision Point | Action / Evidence Needed |
|----------------|--------------------------|
| **DP1** – Is the predicate a legally marketed device? (cleared via 510(k), PMA, or pre‑1976 Class III exemption) | Identify *at least one* cleared device with the same FDA product code. Provide its 510(k) number and clearance date. |
| **DP2** – Same intended use? | Produce a side‑by‑side table of the proposed device’s intended use versus the predicate’s. Identical wording or logically equivalent statements are required. |
| **DP3** – Same technological characteristics? | List core design elements (materials, energy source, algorithmic approach). If differences exist, proceed to DP4. |
| **DP4** – Do the different technologies raise *different questions of safety and effectiveness*? | Conduct a risk‑based comparison (ISO 14971) to show that any new features do not introduce new hazards or clinical concerns. If they do, SE is NOT attainable → De Novo or PMA route required. |
| **DP5** – Performance data demonstrate at least equivalent safety/effectiveness? | Provide bench testing, animal studies, and/or limited clinical data sufficient to prove the device performs as safely and effectively as the predicate. |

---

### 4. Required Evidence (per FDA guidance)

| Evidence Type | Typical Content | Reference |
|---------------|----------------|-----------|
| **Bench / performance testing** | Accuracy, precision, repeatability, safety limits under worst‑case conditions. | eSTAR flowchart DP5 |
| **Software verification/validation** (if applicable) | Module‑level tests, risk control verification, cybersecurity assessment. | 21 CFR 820 (QMSR) – not in source but required by FDA for software. |
| **Animal or clinical data** (as needed) | Comparative study vs. predicate; endpoint aligned with intended use. | DP5 requirement |
| **Risk Management File** | ISO 14971–based hazard analysis, risk control measures, residual risk justification. | Implied in DP4 evaluation |
| **Labeling & IFU** | Intended‑use statements, contraindications, warnings, user instructions. | 21 CFR 801 (Labeling) – required for any submission |

> *Missing:* Specific performance criteria, acceptance limits, and test protocols must be defined once the device’s functional specifications are known.

---

### 5. Risk Controls & Quality System

| Requirement | Detail |
|-------------|--------|
| **Quality Management System** | Must comply with **21 CFR 820** (QMS Regulation) – ISO 13485‑aligned, effective 2026‑02 (QMSR). |
| **UDI labeling** | Assign a Unique Device Identifier per **21 CFR 830.10–830.60**; register device record in the GUDID. |
| **Predetermined Change Control Plan (PCCP)** | If AI/ML components are present, outline allowable post‑market modifications under the FDA PCCP guidance (Dec 2024). |
| **Post‑market surveillance** | Implement a PMS plan consistent with 21 CFR 803 (MDR) and 21 CFR 806 (corrections/removals). |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Action |
|-------------------|--------|
| **No legally marketed predicate** (DP1 failure) | Escalate to regulatory lead → consider De Novo or PMA pathway. |
| **Intended use mismatch** (DP2 failure) | Pause submission; revise IFU and intended‑use statement, then re‑evaluate predicates. |
| **Technological differences raise new safety questions** (DP4 “Yes”) | Immediate escalation – prepare a De Novo request or PMA dossier; 510(k) not viable. |
| **Performance data insufficient to meet DP5** | Request additional bench/clinical testing; engage FDA via Q‑submission for clarification. |
| **Missing critical identifiers** (e.g., product code, CFR subsection) | Hold work package; request detailed device function classification from the project team. |

---

### 7. Outstanding Information Needed Before Proceeding  

1. **Clear intended‑use statement** (identical to that of any chosen predicate).  
2. **Device functional description** to map to an FDA product code and part/subsection (e.g., 21 CFR 892.xxx).  
3. **List of candidate predicates** with their 510(k) numbers, clearance dates, and product codes.  
4. **Technology comparison matrix** highlighting any differences.  
5. **Preliminary risk analysis** (hazard list, severity, likelihood).  

> *Once these items are supplied, the SE evaluation can move through DP1‑DP5 and a complete 510(k) submission dossier can be assembled.*
```

</details>

### kb-eval-20260722-it02-ra_us-004

focus: 510(k) predicate strategy

<details><summary>응답 전문</summary>

```
**Regulatory Draft – 510(k) Substantial‑Equivalence Strategy**

---

### 1. Bottom‑Line Recommendation  
- **Primary pathway:** Premarket Notification (510 k).  
- **Decision framework:** Follow the FDA eSTAR decision‑point flowchart (DP1‑DP5). If any decision point returns “No,” elevate to senior review for a De Novo or PMA route.

---

### 2. Classification / Submission Route  

| Question | What to Determine | Where to Confirm* |
|----------|-------------------|--------------------|
| **Intended use** (clinical indication, patient population, anatomical site) | Must be *identical* to that of the predicate device. | FDA product‑code database or 510(k) summary of selected predicate. |
| **Regulatory class** | After establishing SE, the device inherits the predicate’s classification (most imaging‑software/processing tools are Class II). | Verify against 21 CFR Part 892 (for imaging) *or* the specific regulation linked to the predicate; not cited here because the source excerpt does not list it. |

\*No explicit CFR part is cited from the provided source, so class assignment will be finalized **after** predicate confirmation.

---

### 3. Required Evidence Package (to satisfy DP5)

| Evidence | Purpose | Reference |
|----------|---------|-----------|
| **Intended‑Use Statement** – precise description matching the predicate. | Meets DP2 (“same intended use”). | 21 U.S.C. §360c(i)(1)(A); 21 CFR 807.92(a)(3) |
| **Predicate Device(s)** – complete 510(k) numbers, registration dates, and labeling excerpts. | Validates DP1 (legally marketed) & provides baseline for comparison. | FDA guidance URLs in source (e.g., https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k) |
| **Technological‑Characteristics Comparison** – side‑by‑side table of materials, design, software algorithms, energy sources, etc. | Addresses DP3 (same tech) and sets up DP4 analysis if differences exist. | 21 U.S.C. §360c(i)(1)(A); 21 CFR 807.92(a)(3) |
| **Risk Analysis & Mitigation** – hazard identification, risk‑control measures, verification of controls. | Demonstrates that any differing characteristics do **not** raise new safety/effectiveness questions (DP4). | Implicit in the “different questions of safety and effectiveness” criterion from 21 CFR 807.92(a)(3) |
| **Performance Testing** – bench‑level functional tests, accuracy/precision studies, usability testing; clinical data if required by the predicate’s labeling. | Provides the data for DP5 (“performance evidence shows at least as safe/effective as predicate”). | Same statutory citation (21 U.S.C. §360c(i)(1)(A); 21 CFR 807.92(a)(3)) |
| **Labeling & IFU** – complete package labeling, warnings, contraindications, and intended‑use paragraph. | Must be consistent with the predicate; supports overall SE argument. | Part of the “same intended use” requirement (see above citations). |
| **QMS Compliance Evidence** – ISO 13485–aligned quality system documentation (Design Controls, Document Control, etc.). | Required for 510(k) submissions under the Quality System Regulation (21 CFR 820) *though not cited in source*, note as a standard prerequisite. | — *Not quoted because the source excerpt does not list this identifier.* |

---

### 4. Missing Information (must be supplied before submission)

| Item | Why Needed |
|------|------------|
| **Exact Intended‑Use Statement** – wording, clinical context, patient population. | To pass DP2. |
| **List of Candidate Predicate Devices** – including 510(k) numbers and their clearance dates. | To verify DP1 and build the comparison matrix. |
| **Detailed Technological Description** – schematics, software architecture, signal‑processing algorithms, hardware specifications. | To evaluate DP3/DP4. |
| **Risk Management Report** (ISO 14971 style). | To prove that any tech differences do *not* raise new safety questions (DP4). |
| **Performance Test Protocols & Results** – raw data, statistical analysis, acceptance criteria. | Needed for DP5 demonstration of safety/effectiveness. |
| **Labeling Draft** – intended‑use paragraph, warnings, instructions for use. | Must mirror predicate and support SE claim. |

---

### 5. Risk Controls (to satisfy the “different questions of safety and effectiveness” test)

1. **Design Controls** – requirement capture, verification/validation plans, traceability matrix.  
2. **Software Validation** – unit, integration, system testing; use of a Predetermined Change Control Plan (PCCP) if future algorithm updates are anticipated (per FDA guidance Dec 2024).  
3. **Usability Engineering** – Human‑Factors validation to ensure proper operation in the intended clinical environment.  
4. **Labeling Safeguards** – explicit warnings, contraindications, and user instructions that mitigate identified hazards.  
5. **Post‑Market Surveillance Plan** – procedures for monitoring adverse events (21 CFR 803) and trend analysis.

*(These controls are standard expectations; the source excerpt only mandates that differing tech must *not* raise new safety questions per 21 CFR 807.92(a)(3).)*

---

### 6. Citations (only identifiers present in the source)

| Identifier | Reference |
|------------|-----------|
| **21 U.S.C. §360c(i)(1)(A)** | Legal definition of Substantial Equivalence. |
| **21 CFR 807.92(a)(3)** | FDA’s regulatory criteria for SE (same intended use; same or non‑new safety questions). |
| **DP1–DP5** | Decision‑point flowchart from “The 510(k) Program: Evaluating Substantial Equivalence” (FDA eSTAR guide, Appendix A). |
| **FDA guidance URLs** – e.g., https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k ; https://www.fda.gov/media/82395/download | Supporting documents for predicate selection and SE evaluation. |
| **21 CFR 807.92** (subpart‑E) | General 510(k) requirements; source includes link to ecfr.gov section 807.92. |

---

### 7. Human‑Escalation Triggers  
```

</details>

### kb-eval-20260722-it02-ra_eu-005

focus: MDR classification and conformity route

<details><summary>응답 전문</summary>

```
**Regulatory Draft – X‑ray Diagnostic System (including detector & image‑processing software)**  
*Prepared in response to audit CHK‑DR‑001 “Rule 5/9” factual error.*

---

### 1. Device Overview (as understood from the source)

| Component | Intended Use (per documentation) | MDR rule that applies (source) |
|-----------|----------------------------------|--------------------------------|
| **X‑ray generator / emitting unit** | Produces ionising radiation for *diagnostic* radiology (radiography, fluoroscopy). | **Rule 10 – Class IIb**【source】 |
| **Digital Flat‑Panel Detector (DFPD)** | Records the X‑ray image that is generated by the above unit. | **Rule 17 – Class IIa** (special provision)【source】 |
| **Image‑processing / reading software** | Provides information used for diagnostic interpretation of the recorded images. | **Rule 11** (software special rule) – class to be aligned with the host device or, if a higher impact is demonstrated, upgraded accordingly【source】 |

> The audit identified that the original checklist incorrectly cited **Rule 5/9** for the whole system.  Rule 5 concerns invasive devices and Rule 9 concerns *active therapeutic* devices; neither applies to a diagnostic X‑ray system (see source).  

---

### 2. MDR Classification Summary  

| Component | MDR rule (source) | Assigned class (per MDR Table 1, Annex VIII) |
|-----------|-------------------|--------------------------------------------|
| X‑ray generator (active ionising‑radiation device) | Rule 10 | **Class IIb** |
| Flat‑panel detector (recording device) | Rule 17 | **Class IIa** |
| Image‑processing software | Rule 11 | **Class IIa** *or* higher if the software alone can cause serious deterioration/death (not indicated in source). |

---

### 3. Conformity‑Assessment Route  

The source **does not contain** an identifier for the MDR conformity‑assessment routes (Art. 52, Annex IX, X or XI).  
> *Action*: Retrieve the applicable route from the MDR text:

| Class | Typical route (MDR) |
|-------|----------------------|
| IIa   | Art 52(6) – **Annex IX** assessment of technical documentation *or* Annex II/III + Annex XI (limited) |
| IIb   | Art 52(4) – **Annex IX** full technical‑documentation assessment *or* Annex X + Annex XI |

For the present system, **the highest class is IIb**, therefore the whole device family must be placed on a **full Annex IX technical‑documentation assessment** (Art 52(4)) and the Notified Body will issue a CE mark for the entire system.  

*Because the source does not provide these citations, they are flagged for confirmation.*

---

### 4. Evidence Required to Satisfy the Notified Body  

| Evidence type | Why required | MDR reference (not in source – flagged) |
|---------------|--------------|------------------------------------------|
| **Technical Documentation** (design dossier, risk management file, labeling, UDI etc.) | Demonstrates compliance with General Safety & Performance Requirements (GSPR). | Annex II (technical documentation) – *missing citation* |
| **Clinical Evaluation Report (CER)** – up‑to‑date per Art. 61 | Shows that the clinical performance and safety are supported by state‑of‑the‑art data. | Annex XIV Part A – *missing citation* |
| **Post‑Market Surveillance (PMS) Plan & System** (Art. 83/84) | Ongoing monitoring of radiation safety, detector performance, software updates. | Art. 83/84 – *missing citation* |
| **Periodic Safety Update Report (PSUR)** (Class IIb) – at least annually (Art. 86(2)) | Summarises benefit‑risk determination and PMCF results. | Art. 86 – *missing citation* |
| **Usability Engineering File** (IEC 62366‑1) & **Software Development Lifecycle** (IEC 62304) | Required for the software component (Rule 11). | IEC 62366‑1, IEC 62304 – *not in source* |
| **Radiation Protection Assessment** (Annex I §16.4) | Confirms compliance with ionising‑radiation limits and shielding. | Annex I §16.4 – *not in source* |

> *All items above are standard MDR requirements; the source excerpt only supplies the classification rules, so the exact article/annex numbers have been noted as “missing citation” where they do not appear in the provided material.*

---

### 5. Gaps / Missing Information (as identified from the audit)

| Gap | Impact on submission |
|-----|----------------------|
| **Incorrect classification entry** (Rule 5/9 instead of Rule 10/17) – high risk because it determines the conformity‑assessment route and NB involvement. | Must be corrected before any technical‑documentation review. |
| No explicit **intended purpose statement** for each component (generator, detector, software). | Required to map each device to the correct MDR rule; without it classification cannot be justified. |
| Absence of **risk‑management file** referencing radiation hazards (§16) and active‑device hazards (§18). | Prevents completion of Annex I compliance demonstration. |
| No documented **PMS plan** covering the whole system (including software updates). | Violates Art. 84; NB will request it before issuing a certificate. |
| Lack of **clinical data** specific to the detector’s performance and image‑quality metrics (e.g., DQE, MTF). | Needed for the CER and for Rule 17 justification (Class IIa). |
| No evidence that the software complies with **IEC 62304** and has undergone **usability testing** per IEC 62366‑1. | Required for Rule 11 classification; NB will request validation reports. |

---

### 6. Suggested Risk Controls (aligned to GSPR)

| Hazard | Relevant GSPR § (not in source – flagged) | Recommended control |
|--------|--------------------------------------------|----------------------|
| Ionising radiation exposure (generator) | Annex I §16.4 (radiation protection) | Shielding design, dose‑monitoring, interlocks, compliance with IEC 60601‑2‑54/28. |
| Mechanical/thermal injury from detector housing | Annex I §20 (mechanical & thermal risks) | Protective casing, ergonomic handling instructions. |
| Software errors leading to misdiagnosis | Annex I §1
```

</details>

### kb-eval-20260723-it01-ra_kr-002

focus: MFDS classification and licensing route

<details><summary>응답 전문</summary>

```
**Regulatory Draft – Preliminary Assessment for a Digital Medical Product (Software‑Based SaMD)**  

---

### 1. Applicable Legal Framework (Korean)

| Source | Identifier (as appears in the source) | Key Provision |
|--------|---------------------------------------|----------------|
| **Digital Medical Products Act** | *법률 제20151호* (디지털의료제품법, 시행일 2025‑01‑24) | Establishes the overarching legal regime for digital medical products, distinct from the traditional 의료기기법. |
| **Enforcement Decree** | *대통령령 제35065호* (디지털의료제품법 시행령, 시행일 2025‑01‑24) | Provides procedural rules for the Act. |
| **Enforcement Regulation** | *총리령 제2088호* (디지털의료제품법 시행규칙, 개정 2026‑01‑23) | Details technical and safety requirements; eight product‑type groups are defined (including AI/ML). |
| **MFDS Notice – Review & Approval Procedures** | *고시 번호 제2025‑25호* (디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 시행일 2025‑04‑15) | Sets the document checklist and evaluation flow for each regulatory route (허가, 인증, 신고). |
| **MFDS Notice – Classification & Grading** | *고시 번호 제2025‑23호* (디지털의료제품의 분류 및 등급 지정 등에 관한 규정, 시행일 2025‑04‑07) | Defines the classification matrix (Class I–III) and the criteria for assigning a grade. |
| **Digital GMP (품질관리 기준)** | *별도 고시* (디지털 의료기기 제조 및 품질관리 기준, 2025년 내 시행) | Introduces “Digital GMP” requirements that manufacturers must satisfy (8 유형군 별 요건, AI/ML 포함). |

> **Note:** All citations are taken verbatim from the source excerpt; no additional identifier numbers have been introduced.

---

### 2. Determination of Classification & Licensing Route  

| Step | Action Required | Reference |
|------|-----------------|-----------|
| **2‑1** | Define the *intended use* (diagnostic, monitoring, therapeutic decision support, etc.) and identify the product’s functional category (e.g., “AI‑based clinical decision support software”). | 고시 번호 제2025‑23호 |
| **2‑2** | Apply the classification matrix in 고시 번호 제2025‑23호 to assign a risk class: <br>• **Class I** – Low risk, non‑invasive, no active intervention.  <br>• **Class II** – Moderate risk (e.g., software that influences clinical management).<br>• **Class III** – High risk (software controlling life‑supporting functions). | 고시 번호 제2025‑23호 |
| **2‑3** | Choose the regulatory route based on class: <br>• **Class I** → *신고* (notification) under 고시 번호 제2025‑25호. <br>• **Class II/III** → *허가* (full approval) or *인증* (certification) depending on whether the product is a “software only” (GUI) vs. an integrated hardware‑software system, per 고시 번호 제2025‑25호. | 고시 번호 제2025‑25호 |

> **Human‑Escalation Trigger #1** – If the intended use or functional category does not clearly map onto any row of the classification table, a senior regulator must be consulted before proceeding.

---

### 3. Required Evidence Package (per route)

| Category | Documents / Data | When Required | Reference |
|----------|-------------------|--------------|-----------|
| **General Technical Documentation** | • Product description & user‑scenario<br>• Architecture diagram (modules, data flow)<br>• Software development lifecycle records (including version control) | All routes | 고시 번호 제2025‑25호 |
| **Risk Management File** | • Hazard analysis, risk assessment, and mitigation measures (aligned with the Digital GMP framework) | Class II/III (허가) – mandatory; Class I (신고) – summary risk table acceptable | 별도 고시 (Digital GMP) |
| **Clinical Evaluation Report (CER)** | • Clinical data from Korean subjects **or** validated foreign clinical evidence (if accepted under the latest MFDS scope expansion). | Class II/III – required; Class I – summary may suffice | 고시 번호 제2025‑25호 |
| **Software Validation & Cybersecurity** | • Verification/validation test reports, including performance testing<br>• Security architecture review, penetration‑test results, privacy impact assessment (PIPA compliance) | All routes (mandatory for AI/ML products) | 별도 고시 (Digital GMP) |
| **Manufacturing Quality System** | • Digital GMP certification (facility audit report) or compliance declaration if production is outsourced abroad.<br>• If manufacturing in Korea – KGMP‑style inspection certificate. | Required when the product is produced domestically; otherwise a foreign quality system equivalence statement may be submitted (subject to MFDS acceptance). | 별도 고시 (Digital GMP) |
| **Labeling & IFU** | • Korean language label, device name, intended use statement, contraindications, and user manual (IFU). All texts must be in Hangul. | Mandatory for all routes. | 고시 번호 제2025‑25호 |
| **Foreign Regulatory Clearances (if any)** | • FDA 510(k) / De Novo clearance or CE Mark technical file, with a note on the scope of acceptance under current MFDS policy. | May reduce need for duplicated clinical data, but must be cross‑referenced to the specific MFDS notice that permits foreign evidence (not present in this excerpt). | *Source does not contain a specific identifier; therefore, an explicit citation cannot be provided.* |
| **Post‑Market Surveillance Plan** | • PMS activities, adverse event reporting procedures, periodic safety update report (PSUR) schedule. | Required for Class II/III; recommended for Class I. | 고시 번호 제2025‑25호 |

> **Human‑Escalation Trigger #2** – Absence of any of the above documents in a submission for a Class II/III product must be flagged to senior review before acceptance.

---

### 4. Missing Information (to be obtained from Sponsor)

| Item | Why It Is Needed |
|------|------------------|
| **Precise Intended Use Statement** (including clinical indication, target patient population). | Determines classification under 고시 번호 제2025‑23호. |
| **Software Functional Specification** (detail of algorithms, AI/ML training data sources). | Required for risk analysis and software validation; also influences eligibility for foreign clinical evidence acceptance. |
| **Evidence of Korean Clinical Validation** (or justification for reliance on foreign data). | CER requirement per 고시 번호 제2025‑25호. |
| **Korean‑language Labeling Draft** (label,
```

</details>

### kb-eval-20260724-it03-ra_kr-005

focus: supplementary-response strategy

<details><summary>응답 전문</summary>

```
**Regulatory Draft – Supplementary‑Response Strategy (MFDS 보완자료 대응 전략)**  

---

### 1️⃣ Classification & Submission Route  
| Device risk class* | MFDS pathway (per **의료기기법 제12조**) | Typical dossier scope |
|--------------------|------------------------------------------|-----------------------|
| Class I (low‑risk) | **신고** – “즉시” processing (Table 1‑B) | Basic device description, Korean labeling/IFU, CE/FDA clearance (if referenced). |
| Class II (moderate) | **허가 (일반)** – 65 days processing (excludes supplement period) | Technical file, risk management plan, non‑clinical safety data, clinical evaluation (if needed). |
| Class III / IV (high) | **허가 (임상 포함)** – 80 days processing (excludes supplement period) | All of the above + full IND‑approved clinical trial dossier. |
| **Note**: The exact risk class must be determined according to the criteria set out in the *“의료기기 허가·신고·심사 등에 관한 규정”* (MFDS 고시).  The source excerpt does not provide the detailed classification table, so the analyst must retrieve it from the Regulation (see citation 1).  

\*If you do not yet know the class, request a **pre‑screening opinion** from MFDS or reference the product’s intended use and compare with the MFDS risk‑class matrix.

---

### 2️⃣ Required Evidence (per pathway)  
| Evidence | When required | Reference in source |
|----------|---------------|---------------------|
| **Korean labeling & IFU** (including symbols, contraindications, storage) | All classes | Implicit in “보완 절차·기간” of the 고시; Korean language is a statutory requirement. |
| **Technical specifications / design dossier** | Classes II‑IV | Covered by “보완 자료 요청 근거” under **의료기기법 제12조**. |
| **Non‑clinical safety data (GLP toxicology, biocompatibility)** | Class II‑IV | Accepted when MFDS recognises foreign GLP data under the *OECD Mutual Acceptance* framework – not explicitly cited here; must be confirmed via separate notice. |
| **Clinical Evaluation Report (CER) / IND‑approved trial results** | Class III‑IV or any device with a claim of therapeutic effect | Governed by **의료기기 임상시험계획 승인에 관한 규정 (2023‑02‑14 개정)** – allows a 30‑day extension for the second supplement (see “IND 2차 보완 30일로 연장”). |
| **Quality Management System certification (KGMP/ISO 13485)** | All classes requiring 허가 or 인증 | Required by the 고시 on “의료기기 허가·신고·심사 등에 관한 규정”. |

**Missing items you should verify with the MFDS supplement request:**  

- Exact list of documents MFDS flagged as absent (the source excerpt does not enumerate them).  
- Whether a Korean‑language translation of foreign clinical data is required.  
- Confirmation that any referenced FDA/CE evidence satisfies MFDS “foreign clinical evaluation” acceptance – this must be cross‑checked against the latest MFDS notice (not present in the excerpts).

---

### 3️⃣ Risk Controls to Emphasise in the Response  

| Control | Why it matters for the supplement | How to document |
|---------|-----------------------------------|-----------------|
| **Risk Management Plan (ISO 14971)** | Demonstrates systematic identification/mitigation of hazards – a core MFDS requirement cited under the 고시. | Submit updated risk analysis matrix, residual‑risk evaluation, and traceability to design controls. |
| **Post‑Market Surveillance (PMS) plan** | Required for Class II‑IV devices; MFDS expects evidence of ongoing safety monitoring. | Provide PMS protocol, adverse event reporting flowchart, and a summary of field data (if any). |
| **Sterilization validation / packaging integrity** (for sterile or package‑critical devices) | Often a cause of “보완 자료” requests for Class III/IV. | Include sterilization cycle reports, microbial challenge test results, and package leak test data. |
| **Korean labeling compliance** | MFDS can reject submission if any label element is not in Korean (mandatory). | Attach final Korean label artwork with regulatory legend, symbols, and batch‑lot traceability fields. |

---

### 4️⃣ Timeline & Clock Management  

- **Supplement period clock stops** (“보완 기간은 처리 기간에서 제외”).  
- For a *허가 (일반)* case the overall review deadline is **65 days** after the supplement is closed; for *허가 (임상 포함)* it is **80 days**.  
- If the device requires an IND, the **second‑supplement extension of 30 days** is permitted under **의료기기 임상시험계획 승인에 관한 규정 (2023‑02‑14 개정)**.

---

### 5️⃣ Human‑Escalation Triggers  

| Trigger | Action required | Owner |
|---------|----------------|-------|
| **No response received from sponsor/document owner within 7 calendar days** of MFDS supplement notice. | Escalate to Senior Regulatory Manager; issue internal “Supplement Deadline Alert”. | Regulatory Lead |
| **Submission of incomplete or non‑Korean material** (identified by QA review). | Immediate rework and submission of corrected package; notify MFDS of planned resubmission date. | Documentation Specialist |
| **Clock approaching the final MFDS deadline** (i.e., 10 days before the 65‑/80‑day limit after supplement closure). | Prepare “Final Extension Request” if additional data are unavoidable; obtain senior sign‑off. | Project Manager |
| **MFDS issues a second supplement request** (e.g., after the first response). | Verify whether the 30‑day IND extension applies; schedule an urgent internal meeting to allocate resources. | Clinical Affairs Lead |
| **Regulatory notice indicates new foreign‑data acceptance criteria** (e.g., change in OECD MAD scope) that affect our current evidence. | Conduct a gap analysis; if gaps exist, raise a “Regulatory Impact Assessment” to senior leadership. | Regulatory Strategy Team |

---

### 6️⃣ Citations from the Source  

1. **의료기기법 제12조** – legal basis for supplement requests.  
2. **의료기기 허가·신고·심사 등에 관한 규정** (식품의약품안전처 고시) – procedural rules, processing times, and supplement handling.  
3. **의료기기 임상시험계획 승인에 관한 규정 (2023‑02‑14 개정)** – permits a 30 day extension for the second IND supplement.  
4. Processing‑time table (Table 1‑B) showing “허가(일반) 65일”, “허가(임상 포함) 80일”, “인증 30일”, “신고 즉시”.  

*All other identifiers 
```

</details>
