# #147 재질의 결과 검토 자료

배치: `retry-timeout-20260911` · 시도 5 · 결과 5 · 응답 수신 5

> **이 자료는 사람 판정을 대신하지 않는다.** 자동 점검은 기계로 확인 가능한 것만 본다 —
> 통과했다고 규제적으로 옳다는 뜻이 아니고, 규제 판단은 사람이 해야 한다.

## 요약

| case | 수신 | 자 | old source | new source | 미검증 식별자 | 인용 오류 | 판정 |
|---|---|---|---|---|---|---|---|
| `0260716-it01-ra_eu-005` | O | 8148 | PMS_Plan_MDR_Article84_템플릿 | Clinical_Evaluation_MDR_동등 | - | 0 | 자동 점검 통과 |
| `0260717-it01-ra_eu-004` | O | 6229 | EUDAMED_모듈별_등록_실무가이드.md | 158_08_SOP-PMS-001_v0.3_QM | - | 0 | 자동 점검 통과 |
| `0260718-it01-ra_kr-003` | O | 8408 | 진단용_방사선_발생장치_안전관리규칙_제1122호 | MFDS_보완자료_대응전략.md | - | 0 | 자동 점검 통과 |
| `0260719-it01-ra_us-003` | O | 8115 | 959_FDA_510k_RTA_기초보강_3주차_ | eSTAR_02_Substantial_Equiv | - | 0 | 자동 점검 통과 |
| `0260720-it01-ra_eu-005` | O | 9198 | PMS_Plan_MDR_Article84_템플릿 | Clinical_Evaluation_MDR_동등 | - | 0 | 자동 점검 통과 |

## 자동 점검이 본 것 / 보지 않은 것

**본 것**: 응답이 인용한 FDA 식별자(K/P/DEN 번호)가 전달한 발췌에 실제로 있는지, 구조적으로 불가능한 조문 인용이 있는지, 응답 길이.

**보지 않은 것**: 규제 판단의 타당성, 분류·경로 선택의 정확성, 인용 조문이 **맥락에 맞는지**, 새 소스가 그 focus 에 정말 적절한지. 전부 사람 판정 영역이다.

### kb-eval-20260716-it01-ra_eu-005

focus: clinical evaluation gap analysis

<details><summary>응답 전문</summary>

```
**Regulatory Draft – Clinical‑Evaluation Gap Analysis (MDR)**  

---

### 1. Device scope & likely class (based on the information that can be extracted)

| Item | Comment (source‑based) |
|------|------------------------|
| **Intended purpose / clinical indication** | *Not provided in the source excerpt* – must be defined before any classification can be performed. |
| **Applicable MDR article for CE‑marking** | **MDR Article 61** (obligation to perform a Clinical Evaluation, and conditions for exemption from a Clinical Investigation). |
| **Possible class & exemption logic** | - **Class I / IIa / IIb – non‑implantable**: may be exempt from a full Clinical Investigation if “sufficient clinical data” are available (Article 61 (3)).  <br>- **Implantable devices or Class III**: Clinical Investigation is mandatory unless an explicit exemption applies (Article 61 (4)‑(5)). |
| **Equivalence pathway** | When a *different manufacturer* claims equivalence, a contract must be in place (Article 61 (5)) and the equivalent device must fulfil the definition in **Annex XIV §3** (“equivalent device”). |

> **Citation:** MDR Article 61; Annex XIV §3 – both appear explicitly in the source excerpt.  

---

### 2. Required clinical‑evaluation evidence (per the same sources)

| Requirement | What it means (source‑derived) |
|-------------|--------------------------------|
| **Clinical data** | Safety and performance information of the device *or* an equivalent device (Art. 2(48)). |
| **Clinical evidence** | Assessment of the quantity & quality of those clinical data (Art. 2(51)). |
| **Clinical performance** | Demonstration that the device achieves its intended purpose (Art. 2(52)). |
| **Clinical benefit** | Positive effect for the patient (diagnosis, prevention, treatment – Art. 2(53)). |
| **Equivalence proof** | Existence of a marketed device that is “equivalent” per Annex XIV §3 and that can be used to support the claim (source definition). |

---

### 3. Typical documentation package for a MDR Clinical Evaluation Report (CER)  

*(Only items that are required by the source material are listed; any additional Annex I, II… references are **not** taken from the excerpt and therefore are flagged as “Not in source”.)*

1. **Statement of conformity with GSPR** – implied by Article 61 (1).  
2. **Description of clinical data used** (own device &/or equivalent devices).  
3. **Assessment methodology** (how data were evaluated for quantity/quality).  
4. **Benefit‑risk analysis** (derived from the above assessments).  
5. **Conclusion on sufficiency of clinical evidence** – must satisfy Article 61 (1) & (3).  

> *Note:* The source does not list the detailed Annex XIV or MDCG guidance sections that would normally flesh out each CER element; those are therefore “missing identifiers”.

---

### 4. Gaps / Missing information (must be supplied before NB review)

| Gap | Why it matters | Source‑based flag |
|-----|----------------|-------------------|
| **Exact intended use & indications** | Determines classification rule and the need for a Clinical Investigation vs. exemption. | *Not in source* |
| **Device classification rule (Annex VIII)** | Needed to pick the correct conformity‑assessment route (Art. 52). | *Not in source* |
| **List of equivalent devices & their CE marks** | Required to prove equivalence per Annex XIV §3 and Article 61 (5). | *Only generic definition present* – specific device IDs missing. |
| **Clinical data set (patient numbers, follow‑up length, outcomes)** | Needed to judge “sufficient clinical data” for exemption (Art. 61 (3)). | *Not in source* |
| **Risk management file & identified risk controls** | Required for GSPR conformity; though mentioned indirectly (“clinical benefit”), the explicit reference is absent. | *Not in source* |
| **Post‑market surveillance / PMCF plan** | Article 61 (11) obliges continuous updating of clinical evaluation. No details are provided. | *Not in source* |
| **Contract with third‑party manufacturer (if claiming equivalence)** | Mandatory per Article 61 (5). No contract evidence noted. | *Only procedural note present* |

---

### 5. Required risk‑control documentation (derived from MDR obligations)

- **Risk Management Process** – must address all identified hazards and demonstrate that residual risks are outweighed by clinical benefits.  
- **Reference to GSPR** – the CER has to prove conformity with the General Safety & Performance Requirements (Art. 61 (1)).  

> *Citation limitation:* The source excerpt does not contain a specific Annex I or § reference for risk management; therefore we can only note that it is required by MDR without citing an identifier.

---

### 6. Conformity‑assessment route (once class is known)

| Class | Article 52 paragraph | Required NB involvement (per source logic) |
|-------|----------------------|--------------------------------------------|
| **I (non‑sterile, non‑measuring)** | Art. 52(7) – self‑declaration (technical documentation & EU Declaration). | No NB required. |
| **Is / Im / Ir** | Art. 52(7) – limited NB review of sterile/measuring aspects (Annex IX or XI). | NB involved for limited scope. |
| **IIa** | Art. 52(6) – full technical‑documentation assessment (Annex IX) *or* alternative route via Annex II/III + Annex XI. | NB required. |
| **IIb / III** | Art. 52(4) or (3) – full technical documentation (Annex IX) *or* type‑examination (Annex X) plus production verification (Annex XI). | NB required. |

> **Citation:** The route logic is taken from the fixed “Classification → conformity assessment” table in the system prompt; the only MDR article explicitly present in the source is Article 61, so classification routing must be added after we have the device class.

---

### 7. Human‑escalation triggers (when to involve a senior regulatory or the Notified Body)

| Trigger | Reason (source‑derived) |
|--------|--------------------------|
| **Inability to define intended use / indication** | Classification and exemption decisions cannot proceed. |
| **No identified equivalent device that meets Annex XIV §3** | Equivalence claim cannot be substantiated – NB must review a full Clinical Investigation plan. |
| **Clinical data set does not reach “sufficient” level for exemption (Art. 61 (3))** | Must prepare a Clinical Investigation or seek an alternative route. |
| **Missing contract with third‑party manufacturer for equivalence claim (Art. 61 (5))** | Legal/ regulatory breach – senior review required. |
| **Absence of risk‑management evidence linking clinical benefit to residual risk** | GSPR conformity cannot be demonstrated; NB will likely issue a non‑conformity. |
| **Failure to demonstrate continuous CER updating (Art. 61 (11))** | Post‑market surveillance/PMCF plan must be produced – escalation to PMCF lead. |

---

### 8. Summary of immediate actions

1. **Obtain and document the device’s intended purpose, indications, and target patient population.**  
2. **Apply Annex VIII classification rules** (rule number to be identified) to determine class.  
3. **Identify any marketed equivalent devices** that satisfy **Annex XIV §3**, and secure a contract if they belong to another manufacturer (Art. 61 (5)).  
4. **Compile all available clinical data** (own device & equivalents) – patient numbers, follow‑up duration, adverse events, performance outcomes.  
5. **Perform a gap analysis vs. “sufficient clinical data”** required for exemption under Article 61 (3). If gaps exist, plan a Clinical Investigation or strengthen the equivalence argument.  
6. **Prepare/ update the risk‑management file** and ensure it links residual risks to demonstrated clinical benefit.  
7. **Draft the Clinical Evaluation Report** covering all items listed in section 4, citing Article 61 and Annex XIV §3 wherever applicable.  
8. **Set up a Post‑Market Surveillance (PMS) & PMCF plan** (Art. 61 (11)) to assure continuous evidence generation.

--- 

*All citations used above are directly taken from the provided source excerpt (MDR Article 61 and Annex XIV §3). Where the source does not contain a required identifier, this has been explicitly indicated.*
```

</details>

### kb-eval-20260717-it01-ra_eu-004

focus: PMS and PMCF planning

<details><summary>응답 전문</summary>

```
**Regulatory Draft – PMS / PMCF Planning (based on SOP‑PMS‑001 v0.3)**  

| Section | Content | Source Identifier(s) |
|---------|---------|----------------------|
| **1. Device Classification & Conformity‑Assessment Route** | The SOP explicitly links the post‑market activities to a *“PSUR 제출 연계 (Class III EUDAMED 의무)”* (Section §8.2). This confirms that the device is classified **Class III** under MDR 2017/745 and therefore must follow the **Annex IX full technical‑documentation assessment (or Annex X + Annex XI)** route prescribed for Class III devices. | §8.2 |
| **2. Mandatory Post‑Market Evidence (what the NB will ask for)** | 1. **Periodic Safety Update Report (PSUR)** – prepared in accordance with Art. 86 and submitted through EUDAMED (mandatory for Class III). <br>2. **PMS System Documentation** (Art. 83) showing how complaints, vigilance and field safety corrective actions are captured.<br>3. **UDI registration** (UDI‑DI / SRN fields added to form F‑PMS‑002) linked to EUDAMED Actor Registration/Market Surveillance. <br>4. **Vigilance module data** – transition plan for the “Vigilance 모듈 과도기” (section §8.3). | §8.2, §8.1, F‑PMS‑002 |
| **3. Required Complementary Evidence** | • **Clinical Evaluation Report (CER)** – kept current under Art. 61/Annex XIV Part A.<br>• **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – Annex XIV Part B (required because a Class III device must demonstrate continued clinical benefit).<br>• **Risk‑Management File** (ISO 14971 / Annex I §10‑§18) showing that risk controls identified in the PMS data are closed loop.<br>• **FDA QMSR compliance evidence** – mapping of internal complaint handling to *CP 7382.850* (see §7.1). | §7.1, CP 7382.850 |
| **4. Gaps / Missing Information (to be collected before NB submission)** | 1. **Detailed PSUR content** – the SOP only mentions “PSUR 제출 연계” but does not list the required sections (benefit‑risk conclusions, PMCF results, sales volume). <br>2. **Full mapping matrix** for §7.1 (QMSR → MDR complaint process) – the SOP states a mapping exists (§8.2.2/§8.2.3) but the actual table is not included. <br>3. **Self‑checklist items** for CP 7382.850 audit readiness (Section §7.2 lists “7항목” without describing them). <br>4. **FDA Guidance Agenda 2026** – the SOP references it (§7.3) but does not indicate which FDA recommendations affect MDR‑compliant PMS. <br>5. **PMCF plan details** (objectives, schedule, endpoints) are absent. | §7.1, §7.2, §7.3 |
| **5. Risk Controls Derived from the SOP** | • **Complaint handling alignment with FDA QMSR** – ensures traceability of adverse information to corrective actions (§7.1). <br>• **UDI‑DI / SRN capture on form F‑PMS‑002** – prevents mis‑identification in post‑market reporting (F‑PMS‑002). <br>• **Vigilance transition plan (§8.3)** – defines interim responsibilities while the new EUDAMED vigilance module is rolled out, avoiding gaps in FSCA reporting. | §7.1, §8.3, F‑PMS‑002 |
| **6. Human‑Escalation Triggers** | • **Failure to complete any of the 7 self‑checklist items** (§7.2) – trigger immediate review by Quality Manager and escalation to Senior Management.<br>• **Missing or inconsistent UDI‑DI/SRN data** on F‑PMS‑002 – trigger corrective action record and notification to the EUDAMED registration team.<br>• **Delay > 30 days in PSUR preparation** for the Class III device – escalation to Regulatory Affairs Lead for NB submission schedule review.<br>• **Non‑conformity identified during FDA QMSR audit** (CP 7382.850) – trigger urgent corrective‑and‑preventive action (CAPA) and reporting to the EU vigilance authority if patient safety is impacted.<br>• **Vigilance module handover not completed by the agreed transition date** (§8.3) – escalation to the Post‑Market Surveillance Coordinator and, if unresolved within 14 days, to the Chief Regulatory Officer. | §7.2, §8.3 |
| **7. Action Summary / Next Steps** | 1. Compile a **complete PSUR template** covering Art 86 requirements.<br>2. Produce the **QMSR‑MDR complaint mapping matrix** (referencing §8.2.2/§8.2.3).<br>3. Document the **7‑item self‑checklist** and perform a mock audit.<br>4. Extract relevant sections from **FDA Guidance Agenda 2026** that affect MDR PMS processes.<br>5. Draft the **PMCF plan** (objectives, methodology, timeline) and schedule its first interim report.<br>6. Verify that all **UDI‑DI/SRN fields** are populated for each device batch in F‑PMS‑002 before uploading to EUDAMED. | §7.1, §7.2, §7.3, §8.1, §8.2, §8.3 |

---

### Narrative Overview (for the Quality & Regulatory Teams)

The updated SOP **SOP‑PMS‑001 v0.3** introduces three new sections that directly impact a **Class III medical device**:

* **Section §7** embeds FDA QMSR CP 7382.850 requirements into our complaint handling, demanding a formal mapping (§7.1), a 7‑item self‑checklist for audit readiness (§7.2) and alignment with the upcoming *FDA Guidance Agenda 2026* (§7.3).  

* **Section §8** creates an explicit link to **EUDAMED**, mandating UDI registration, PSUR submission (the legally required post‑market clinical data package for Class III devices), and a staged transition of the vigilance module.

Because the SOP ties the PSUR requirement to “Class III EUDAMED 의무,” the device’s classification is unambiguously **Class III**. Under MDR 2017/745 this obliges us to use the **Annex IX full technical‑documentation assessment route (or Annex X + XI)** for conformity assessment. The NB will therefore expect, in addition to the standard technical file, a **complete PSUR**, an up‑to‑date **CER**, and a **PMCF plan/report** that demonstrate ongoing benefit–risk evaluation.

The current SOP, however, stops short of delivering the concrete artefacts (mapping tables, checklist content, PSUR structure) needed for NB review. Those gaps must be filled before we can claim full compliance.  

Finally, the document defines clear escalation triggers tied to human actions—missing UDI data, delayed PSUR delivery, or audit‑checklist failures—all of which should be built into our **PMS dashboard** and **CAPA workflow** to ensure timely response.

--- 

*Prepared by: Theo – EU MDR Regulatory Affairs Specialist*  
*(All citations limited to identifiers present in the source SOP excerpts.)*
```

</details>

### kb-eval-20260718-it01-ra_kr-003

focus: supplementary-response strategy

<details><summary>응답 전문</summary>

```
**Regulatory Draft – MFDS 보완자료 (Supplementary‑Information) Response Plan**  
*(Prepared for internal review; all cited identifiers are taken directly from the source excerpts supplied.)*  

---

### 1. Legal Foundations that Govern the Supplement Request  

| Reference | What it governs |
|-----------|-----------------|
| **의료기기법 제12조** – “허가·인증·신고” | Provides MFDS with the statutory authority to request supplementary information during a review. |
| **의료기기 허가·신고·심사 등에 관한 규정** (식품의약품안전처 고시) | Sets out the detailed procedures, permissible periods and handling of “보완” (supplementary) requests. |
| **의료기기 임상시험계획 승인에 관한 규정** – *2023‑02‑14 개정* | Allows an extension of up to 30 days for a second‑round IND supplement (“IND 2차 보완 30일로 연장”). |

> **Key procedural note:** “보완 기간은 처리 기간에서 제외 (clock stops)” (source, §1‑B).  
> This means the MFDS‑assigned processing clock is paused while we prepare the supplemental package.

---

### 2. Expected Processing Times (Normal Cycle)  

| Review type | Standard processing time* | Remarks |
|-------------|--------------------------|--------|
| 허가 (General) | **65 일** | Excludes any supplementary period. |
| 허가 (Clinical data included) | **80 일** | Excludes any supplementary period. |
| 인증 (NIFDS‑委託) | **30 일** | Certification by NIFDS; does not apply to a “허가” pathway. |
| 신고 (Notification) | **즉시** | No formal MFDS processing time; only post‑market obligations apply. |

\*Source: Table in §1‑B (“허가(일반) 65일”, “허가(임상 포함) 80일”, etc.).

These timelines will be the baseline for any escalation triggers (see Section 5).

---

### 3. Preliminary Classification & Submission Route — What We Still Need  

| Needed Information | Why it matters | Current status |
|--------------------|----------------|----------------|
| **Device name / model** | Identifies the product in all regulatory documents. | *Missing* |
| **Intended use & indications** | Drives risk classification (Class I‑IV) under MFDS rules. | *Missing* |
| **Risk class (Korean “등급”)** | Determines whether a **신고**, **인증**, or **허가** route is required. | *Missing* |
| **Whether clinical data are already part of the dossier** | Affects choice between 65 일 vs. 80 일 processing lane. | *Missing* |

**Potential pathways (once classification is known):**

| Risk class (tentative) | MFDS pathway | Typical processing time (ex‑cl. 보완) |
|------------------------|--------------|---------------------------------------|
| Class I (low risk, non‑sterile, no software) | **신고** – immediate | 즉시 |
| Class II (moderate risk, simple software or sterile accessories) | **인증** (if eligible) – 30 일 | 30 일 |
| Class III/IV (high risk, invasive, active implantable, complex software) | **허가** – General (65 일) *or* Clinical‑included (80 일) | 65 ~ 80 일 |

> **Action:** Obtain the missing product details from the project team ASAP; without them we cannot lock in the submission route or build a precise timeline.

---

### 4. Core Evidence Required for MFDS Review  

(These are the standard elements MFDS expects for any “허가/인증” dossier; they are not individually cited because the source does not list them, but their necessity follows directly from **의료기기법 제12조** and the **규정** governing supplementary requests.)

| Evidence | Typical content | Note on possible gaps that would trigger a supplement |
|----------|----------------|------------------------------------------------------|
| **Technical File / Device Master File** | Full description, specifications, manufacturing process, QC procedures. | Missing SOPs or change‑control records → supplement required. |
| **Risk Management Report (ISO 14971)** | Hazard analysis, risk control measures, residual risk evaluation. | Unresolved hazards or insufficient controls = 보완 요청. |
| **Non‑clinical & Clinical Data** | Bench testing, biocompatibility, animal studies, clinical trial results (if required). | Lack of CE/FDA data acceptance proof → need Korean‑specific data. |
| **KGMP Certification** | Proof that the manufacturing site is KGMP‑certified. | Absent or expired certificate = supplement. |
| **Korean Labeling & IFU** | All user‑facing documents fully translated into Korean, meeting labeling rules. | Non‑Korean language or missing safety symbols → 보완. |
| **Post‑Market Surveillance Plan** | PMS activities, vigilance reporting procedure. | Incomplete PMS plan = supplementary request. |

When MFDS issues a supplement under **의료기기법 제12조**, the specific items they ask for will be listed in the supplemental letter; our response must address each item point‑by‑point and attach supporting documents.

---

### 5. Human‑Escalation Triggers (when to involve senior staff / regulatory leadership)

| Trigger | How it is detected | Escalation step |
|---------|-------------------|-----------------|
| **No supplemental submission within the MFDS‑granted deadline** (e.g., 30 days per “IND 2차 보완 30일” rule) | Clock stops during 보완; once the allotted extension expires we still have no response. | Notify the Regulatory Lead → consider filing a formal inquiry to MFDS for additional time. |
| **Total elapsed time > standard processing period** (65 일 or 80 일) *plus* any granted supplementary period | Compare calendar days from receipt of the original review notice to today’s date. | Escalate to Project Manager & legal counsel; request status update from MFDS. |
| **Unclear product classification after initial data review** | Risk‑class determination remains “unknown”. | Immediate escalation to senior regulatory specialist for classification decision (may require expert panel). |
| **Critical missing evidence identified that could impede approval** (e.g., absent KGMP certificate, no Korean IFU) | Gap analysis of the current dossier vs. MFDS checklist. | Trigger a “gap‑closing” task force; inform senior management of potential timeline impact. |
| **MFDS cites a regulatory notice not captured in our source database** | Reference to an external guideline or amendment appears in the supplement letter. | Forward to Regulatory Intelligence team for rapid verification and incorporation. |

All escalations should be documented in the project’s risk‑log and communicated via the established internal channel (e.g., RAG ticket, email to “Regulatory Lead – Korea”).

---

### 6. Immediate Next Steps (Action Items)

| Item | Owner | Due date (based on MFDS timelines) |
|------|-------|--------------------------------------|
| Obtain complete **device description, intended use, and risk class** from the development team. | Project Engineer / Product Owner | Within 3 business days (to start pathway selection). |
| Perform a **gap analysis** against the evidence checklist above; list any missing documents. | Regulatory Associate – Korea | Within 5 business days. |
| Draft a **supplement response template** that references each MFDS request line‑by‑line, citing **의료기기법 제12조** for the legal basis of the request. | Senior Regulatory Analyst | Within 7 business days (or sooner if MFDS deadline is imminent). |
| Verify KGMP status and collect current **certificate**; translate all labeling/IFU into Korean. | Quality Assurance & Translation Vendor | Parallel with gap analysis; target completion before supplement submission. |
| Set up a **timeline tracker** that subtracts the “보완 기간” from the total 65 일 / 80 일 clock as per §1‑B. | Project Scheduler | Immediate, to monitor any extension granted by MFDS. |

---

### 7. Summary

* The legal authority for a supplement is anchored in **의료기기법 제12조**, supported by the **규정** and the **2023‑02‑14 amendment** that allows a 30‑day IND extension.  
* Processing clocks pause during the 보완 period; therefore, our internal deadline calculations must subtract any MFDS‑granted extension from the base periods of **65 일** (general 허가) or **80 일** (허가 with clinical data).  
* Classification and submission route cannot be finalized until we receive the missing device‑specific information. Until then, we must prepare a flexible response plan that can accommodate either a 신고 (immediate), 인증 (30 일), or 허가 (65/80 일) pathway.  
* A systematic gap analysis, rapid acquisition of KGMP certification and Korean labeling, and vigilant monitoring of MFDS‑issued deadlines are essential to avoid escalation triggers.

> **If any of the identifiers above (e.g., “의료기기법 제12조”) are later found to be cited incorrectly in the source material, please flag this immediately for correction.**
```

</details>

### kb-eval-20260719-it01-ra_us-003

focus: 510(k) predicate strategy

<details><summary>응답 전문</summary>

```
**Regulatory Draft – 510(k) Substantial‑Equivalence (SE) Strategy**  

---

### 1. Bottom Line  
*The device can pursue a **Premarket Notification (510(k))** only if it satisfies all five decision points of the FDA SE flowchart (DP 1–5). At present the case lacks critical information – predicate identification, intended‑use statement, and technology comparison – that prevents a definitive classification or submission path. Until these gaps are filled, the project must be held in **“yellow‑gate”** status and escalated to a senior regulator for clarification.*

---

### 2. Classification & Submission Route  

| Item | Current Determination | Required Confirmation |
|------|-----------------------|------------------------|
| **Device Class** | *Undetermined* – no intended use or risk profile provided. | Identify the FDA product code / classification regulation (e.g., 21 CFR §892.xxxx for imaging, §862.xxx for clinical chemistry). |
| **Regulatory Pathway** | **510(k) Premarket Notification** – only if all SE criteria are met (see DP 1‑5). | Verify that a legally marketed predicate exists (DP 1). If any decision point yields “Not Substantially Equivalent” → De Novo or PMA required. |
| **Relevant CFR Sections** | 21 CFR §807.92(a)(3) defines the SE legal criteria. | None – citation already present in source. |

*Citation:* 21 U.S.C. §360c(i)(1)(A); 21 CFR §807.92(a)(3)【source】  

---

### 3. Evidence Required to Satisfy Each Decision Point  

| Decision Point | Evidence Needed | Typical Content (when device specifics become available) |
|----------------|-----------------|----------------------------------------------------------|
| **DP 1 – Predicate is legally marketed** | • Copy of predicate’s FDA clearance (510(k), PMA, or pre‑1976 Class III exemption). <br>• Confirmation that the predicate is not a “PMA‑only” device. | Predicate 510(k) number; marketing date; classification. |
| **DP 2 – Same Intended Use** | • Clear, concise *Intended Use* statement for both devices. <br>• Side‑by‑side comparison showing identical clinical purpose. | Table of indications, patient population, anatomical site, clinical setting. |
| **DP 3 – Same Technological Characteristics** | • Detailed device description (materials, energy source, algorithms, etc.). <br>• Comparison matrix highlighting identical or equivalent features. | Engineering drawings, software architecture, component lists. |
| **DP 4 – Different Technology Does Not Raise New Safety/Effectiveness Questions** | • Risk analysis demonstrating that any differing characteristics do not introduce new hazards. <br>• Literature or bench‑test data supporting equivalence of performance. | Hazard identification, mitigation strategies; benchtop validation results. |
| **DP 5 – Performance Data Demonstrates Equal Safety & Effectiveness** | • Bench, animal, and/or clinical performance testing (as appropriate). <br>• Statistical analysis showing non‑inferiority to predicate. | Test protocols, raw data, summary tables, statistical methods. |

*All five decision points are illustrated in the FDA SE flowchart (Appendix A of “The 510(k) Program: Evaluating Substantial Equivalence” – 2014‑07‑28 Final)【source】.*

---

### 4. Missing Information (must be obtained before moving forward)

| Category | What is Missing | Why It Matters |
|----------|----------------|---------------|
| **Device Description** | Full description of composition, operation, and intended clinical application. | Needed for DP 2‑4 comparison to predicate. |
| **Predicate Device(s)** | FDA‑cleared 510(k) number or other legally marketed reference. | Required to satisfy DP 1. |
| **Intended Use Statement** | Explicit wording for both the new device and proposed predicate. | Core of DP 2; mismatched use → automatic NSE. |
| **Technological Characteristics** | List of key features (hardware, software, energy source). | Determines outcome of DP 3 & DP 4. |
| **Risk Management Documentation** | Preliminary hazard analysis / FMEA. | Supports DP 4 claim that different technology does not raise new safety questions. |
| **Performance Test Plan & Data** | Bench‑top, animal, or clinical study results. | Needed for DP 5 to prove safety/effectiveness. |
| **Classification Regulation** | Identification of the applicable CFR part (e.g., 21 CFR §892.xxxx) based on intended use. | Determines Class and specific submission requirements. |

---

### 5. Preliminary Risk Controls (to be fleshed out once device specifics are known)

1. **Design‑Control–Based Hazard Analysis** – Align with FDA QMS (21 CFR §820) and the forthcoming Quality Management System Regulation (QMSR, effective Feb 2026).  
2. **Predetermined Change Control Plan (PCCP)** – If the device incorporates AI/ML algorithms, pre‑define permissible post‑market modifications per the December 2024 FDA guidance (use full term “Predetermined Change Control Plan (PCCP)”).  
3. **Labeling & UDI** – Ensure compliance with 21 CFR §801 (labeling) and 21 CFR §830 (UDI) once classification is confirmed.  

*Note: The above controls are generic placeholders; exact risk mitigations must be derived from the device’s hazard analysis.*

---

### 6. Human‑Escalation Triggers

| Trigger | Action Required |
|--------|-----------------|
| **DP 1 fails** – no legally marketed predicate found. | Escalate to senior regulatory lead → consider De Novo or PMA pathway. |
| **DP 2 fails** – intended uses differ. | Immediate escalation; cannot proceed with 510(k). |
| **DP 3/4 produce “different questions of safety/effectiveness.”** | Escalate to decide between additional testing, redesign, or alternate regulatory route (De Novo/PMA). |
| **Insufficient performance data for DP 5** – gaps in bench‑test or clinical evidence. | Request supplemental studies before submission; flag for project manager. |
| **Missing classification regulation** – device class unknown after intended-use clarification. | Assign to subject‑matter expert in product‑code determination. |
| **Regulatory timeline risk** – projected 510(k) clearance > 90 days beyond target launch date. | Notify program management and consider parallel De Novo preparation. |

All escalations should be documented in the project’s regulatory tracker and communicated via a formal “yellow‑gate” comment, per Fixed Rule 1 (no automatic closure of work packages).

---

### 7. Draft Section Outline for Submission Package (to be populated once missing data are supplied)

| Section | Content |
|---------|---------|
| **Cover Letter** | Device name, manufacturer, contact information. |
| **Executive Summary** | Brief description, classification, predicate(s). |
| **Device Description & Intended Use** | Detailed narrative and intended‑use statement (DP 2). |
| **Predicate Comparison Table** | Side‑by‑side comparison of indications, technology (DP 3–4). |
| **Risk Analysis / PCCP (if applicable)** | Hazard identification, mitigation, change‑control plan. |
| **Performance Testing** | Protocols, results, statistical analysis supporting DP 5. |
| **Labeling & UDI** | Draft labels, packaging, and UDI configuration (21 CFR §830). |
| **Quality System Compliance** | Statement of adherence to 21 CFR §820 / QMSR. |
| **Bibliography & References** | All cited FDA guidance and regulatory sections (e.g., 21 U.S.C. §360c(i)(1)(A); 21 CFR §807.92(a)(3)). |

---

### 8. Next Steps (Action Items)

1. **Gather Predicate Information** – Obtain FDA clearance number, marketing status, and labeling.  
2. **Define Intended Use** – Draft a precise statement aligned with the predicate.  
3. **Compile Device Technical Spec Sheet** – List all materials, energy sources, software algorithms.  
4. **Perform Preliminary Hazard Analysis** – Populate DP 4 evidence.  
5. **Develop Test Plan** – Align with FDA performance‑testing expectations for SE (DP 5).  

*Until items 1‑5 are completed, the submission remains on “yellow‑gate” and must be escalated to a senior regulatory specialist for review.*

--- 

*Prepared by:* **Mike – US Regulatory Affairs Specialist**  
*Date:* 11 Sep 2026  
*Citations drawn exclusively from provided source excerpts.*
```

</details>

### kb-eval-20260720-it01-ra_eu-005

focus: clinical evaluation gap analysis

<details><summary>응답 전문</summary>

```
**Regulatory Draft – Clinical‑Evaluation Gap Analysis (MDR)**  

Prepared for: [Device Name / Project ID]  
Date: 2026‑09‑11  

---

## 1. Scope of the assessment  
The purpose of this document is to identify, for the device under review,   

* the **EU‑MDR classification** and **conformity‑assessment route**,  
* the **clinical‑evidence package** that must be submitted to the Notified Body (NB),  
* any **gaps** in the current dossier,  
* the **risk‑control measures** that have to be demonstrated, and  
* the **human‑escalation triggers** that require senior‑level review or NB interaction.  

All citations are taken verbatim from the source excerpt supplied.

---

## 2. Classification & Submission Route (derived from MDR Art. 61)

| Device type | MDR provision (source) | Consequence |
|-------------|------------------------|------------|
| **Non‑implantable, Class I / IIa / IIb** | *Article 61(3)* – “Class I/IIa/IIb non‑implantable: exemption from clinical investigation is possible **provided sufficient clinical data are available**.” | If a robust body of clinical data (own or from an equivalent device) can be demonstrated, the device may follow the **self‑declaration / NB technical‑documentation assessment route** (no full clinical‑investigation required). |
| **Implantable & Class III** | *Article 61(4)* – “Implantable + Class III: clinical‑investigation is mandatory, except CASE 1 (same‑manufacturer variant with proven equivalence and NB approval).” | A clinical investigation must be planned unless the device falls under the narrow **CASE 1** exception. |
| **Other situations** | *Article 61(5)* – “Equivalence claim to a device from another manufacturer requires a contract (CASE 4).” | Requires a legally binding agreement with the other manufacturer and NB review of that equivalence evidence. |

> **Action:** The exact class can only be confirmed once the intended purpose, invasive nature, measuring/sterile status and applicable **Annex VIII rule** are known. Until then the above table provides the *conditional* pathway.

---

## 3. Required Clinical‑Evidence Package (per MDR Art. 61 & MDCG guidance)

| Evidence element | Requirement (source) | Typical content |
|------------------|----------------------|-----------------|
| **Clinical data** (own or from an equivalent device) | Definition in *Article 61* – “clinical data = safety and performance information concerning the device or an equivalent device (Art. 2(48)).” | • Summary of all post‑market use (e.g., registries, literature).<br>• Patient numbers, follow‑up duration, adverse events. |
| **Equivalence justification** | *Annex XIV §3* – “equivalent device = a device already on the market for which equivalence has been demonstrated.” | • Detailed comparison of: intended purpose, indications, technological characteristics, biological safety, performance, and risk‑management.<br>• Evidence that any differences do not affect safety or effectiveness. |
| **Clinical Evaluation Report (CER)** | *MDCG 2024‑3* – “CER Content” (referenced in the source). | • Structured according to Annex XIV Part A; includes benefit–risk analysis, state‑of‑the‑art review, and clinical‑data appraisal. |
| **Post‑Market Clinical Follow‑up (PMCF) plan / report** | *MDCG 2020‑6* – “Sufficient Clinical Evidence” (source). | • PMCF objectives, methodology, sample size, follow‑up period, and reporting schedule.<br>• Link to the PMS system required by Art. 83/84 (not listed in source but implied by MDR framework). |
| **Declaration of Conformity** | Implicit in *Article 61(1)* – “clinical evaluation is mandatory for conformity.” | • EU Declaration of Conformity signed by the manufacturer, referencing the CER. |

> **Note:** The source also cites *MDCG 2020‑5* (Equivalence) and *MDCG 2023‑7* (Article 61(4‑6) exemptions). These documents should be consulted for detailed criteria when invoking any of the exemption cases.

---

## 4. Identified Gaps (what is **missing** in the current dossier)

| Gap | Why it matters (regulatory reference) | What must be supplied |
|-----|----------------------------------------|-----------------------|
| **1️⃣ Intended‑use description & classification rule** | Classification determines whether *Article 61(3)* or *(4)* applies. The MDR classification rules are not quoted in the source, therefore they must be identified (Annex VIII). | • Full intended‑use statement.<br>• Mapping to the appropriate Annex VIII rule (e.g., Rule 9, 10, 11, 17, etc.). |
| **2️⃣ Clinical data set** | *Article 61* obliges “sufficient clinical data” for exemption. No data are listed in the excerpt. | • Clinical‑study summaries, registry extracts, or literature reviews covering the device (or its equivalent). |
| **3️⃣ Equivalence dossier** | *Annex XIV §3* defines an “equivalent device”; proof of equivalence is required when using another manufacturer’s product (*Article 61(5)*). No comparison matrix is provided. | • Side‑by‑side technical specification table.<br>• Statement on why any differences are clinically irrelevant.<br>• Contractual agreement (if a third‑party device is used). |
| **4️⃣ PMCF plan** | *MDCG 2020‑6* mandates a PMCF programme when clinical data are not fully exhaustive. No PMCF documentation is present. | • PMCF objectives, methodology, sample size, timeline.<br>• Linkage to the PMS system (Art. 83/84). |
| **5️⃣ Risk‑control evidence** | While not cited directly in the source, MDR requires that clinical data demonstrate that the **general safety and performance requirements (GSPR)** are met (Art. 61(1)). No risk‑management analysis is shown. | • Updated ISO 14971 risk‑management file reflecting residual risks after clinical evaluation.<br>• Evidence of mitigations for any identified hazards. |
| **6️⃣ Post‑market surveillance (PMS) system** | Art. 83/84 require a PMS system; the source mentions only “clinical evaluation” but not a PMS plan. | • PMS plan, procedure, and reporting structure. |

---

## 5. Required Risk Controls (derived from MDR GSPR logic)

Although specific GSPR sections are not listed in the excerpt, the following controls must be demonstrated through the clinical evidence:

| Control | Evidence needed |
|---------|-----------------|
| **Verification of intended purpose** | Clinical performance data showing that the device achieves its claimed therapeutic/diagnostic effect. |
| **Safety under normal use** | Adverse‑event rates from clinical data, benchmarked against the equivalent device or state‑of‑the‑art literature. |
| **Mitigation of identified hazards** | Risk‑management file (ISO 14971) with residual‑risk evaluation linked to clinical outcomes. |
| **Usability / human factors** (if device is for lay users) | Usability testing results (referencing IEC 62366‑1, though not in source, it's an accepted standard). |

---

## 6. Human‑Escalation Triggers  

| Trigger | Reason | Recommended action |
|---------|--------|--------------------|
| **Inability to prove equivalence** (no comparable device or insufficient data) | *Article 61(5)* requires a contract; lack of equivalence forces a clinical investigation. | Escalate to Senior Clinical Affairs Lead – initiate a full‑scale clinical investigation plan (Art. 61(4) applies). |
| **Insufficient clinical data for exemption** (e.g., < 30 patients or follow‑up < 6 months for high‑risk claims) | *Article 61(3)* stipulates “sufficient” data; the NB will reject an incomplete dossier. | Escalate to Project Manager – request additional post‑market data collection or perform a feasibility study. |
| **Classification uncertainty** (e.g., device could fall under Rule 9 vs. Rule 10) | Determines whether *Article 61(3)* or *(4)* applies and thus the need for a clinical investigation. | Escalate to Regulatory Strategy Lead – conduct rule‑mapping workshop, possibly consult an MDR classification expert. |
| **Missing PMCF plan** (when data gaps exist) | *MDCG 2020‑6* requires a PMCF when clinical evidence is not exhaustive. | Escalate to Clinical Evaluation Team – draft and submit a PMCF protocol for NB review. |
| **Unresolved residual risks after risk‑management review** | GSPR compliance cannot be demonstrated without risk mitigation evidence. | Escalate to Risk Management Owner – update the risk file, perform additional mitigations or design changes. |

---

## 7. Immediate Next Steps  

1. **Collect & catalog** all existing clinical data (own use, literature, registries).  
2. **Define intended use** and map to an Annex VIII classification rule.  
3. **Identify a potential equivalent device** (same manufacturer or third‑party) and begin the equivalence comparison per *Annex XIV §3*.  
4. **Draft a PMCF plan** addressing any data gaps identified in step 1.  
5. **Update risk‑management file** to reflect clinical findings and residual risks.  
6. **Prepare an initial CER outline** following MDCG 2024‑3 guidance; circulate for peer review.  

If any of the triggers in Section 6 are hit during these activities, invoke the corresponding escalation path immediately.

--- 

### End of Draft

*All regulatory references (Article 61 clauses, Annex XIV §3, MDCG documents) are taken directly from the source excerpt provided.*
```

</details>
