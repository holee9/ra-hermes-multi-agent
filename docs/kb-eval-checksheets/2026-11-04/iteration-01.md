# KB Eval Checksheet - 2026-11-04 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261104-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "769f1429d00cf33a", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `769f1429d00cf33a`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/FDA_%EC%9E%84%EC%83%81%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%95%84%EC%9A%94%ED%8C%90%EB%8B%A8_%EA%B8%B0%EC%A4%80.md)
- Source hash: `36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `FDA_임상데이터_필요판단_기준.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Predicate‑Strategy Overview for a New U.S. Medical Device (510(k) Pathway)**  

---

### 1. Target Classification & Submission Route
| Parameter | Recommended FDA pathway |
|-----------|--------------------------|
| **Statutory basis** | FD&C Act §510(k)  |
| **CFR reference** | 21 CFR §807 (premarket notification) |
| **Typical class** | Class II (most imaging, diagnostic and software devices) – may be Class I if low‑risk. |
| **Predicate requirement** | Mandatory – a legally marketed device of the same intended use and technological characteristics must be identified. |
| **Clinical data** | Conditional; required only when substantial equivalence cannot be demonstrated on bench/analytical data alone (see §3 of FDA guidance). |
| **Review timeline** | Target 90 days (FDA goal) – schedule ~120 days to accommodate correspondence. |

> **Citation:** FD&C Act §510(k); 21 CFR §807 – *no specific identifier found in source — verify separately* (framework reference).

---

### 2. Evidence Portfolio Required for a Complete 510(k)

| Evidence Category | Typical Content | When It Is Mandatory |
|-------------------|-----------------|----------------------|
| **Device description** | Detailed specifications, block diagram, software architecture (if applicable). | Always |
| **Intended use & Indications for Use** | Clear statement aligning with predicate. | Always |
| **Substantial‑Equivalence Comparison Table** | Side‑by‑side matrix of device features, performance metrics, and labeling against selected predicate(s). | Always |
| **Bench / Performance Testing** | Electrical safety (IEC 60601‑1 2005+A1:2012+A2:2020), electromagnetic compatibility, software verification/validation (IEC 62304 2006+A1:2015), usability (IEC 62366‑1 2015+A1:2020), biocompatibility (ISO 10993‑1 2018) where applicable. | Always |
| **Risk Management File** | Hazard analysis, risk control measures, residual risk assessment per ISO 14971 2019. | Always |
| **Labeling & IFU** | Conforms to 21 CFR §801 (labeling). Includes UDI per 21 CFR §830.10‑§830.60. | Always |
| **Sterility / Shelf‑life (if applicable)** | Validation data, packaging integrity testing. | As indicated by device type |
| **Clinical Data** | Clinical performance or safety data *only if* bench/analytical data insufficient to support SE (see FDA guidance “510(k)s for Solid‑State X‑ray Imaging Devices” and §3 of the clinical‑data‑need decision framework). | Conditional – see Section 3 below |
| **Software Documentation** *(if software is a component)* | Software Description File, architecture diagram, source code control summary, cybersecurity risk assessment (per FDA’s “Cybersecurity for Medical Devices” guidance), Predetermined Change Control Plan (PCCP) when post‑market modifications are anticipated. | Always for SaMD/SiMD |

---

### 3. Clinical Data Determination – Conditional Requirement
- **Rule:** Clinical data are required *only* when the device cannot be shown substantially equivalent based on non‑clinical testing alone.  
- **Reference:** FDA guidance “510(k)s: Solid‑State X‑ray Imaging Devices” (PDF # 171837) & the decision matrix in the source document (Section 3 referenced).  

**Action:**  
1. Perform a head‑to‑head performance comparison with the chosen predicate(s).  
2. If statistical equivalence is demonstrated on pre‑clinical endpoints, omit clinical study and provide justification within the 510(k) Summary/Statement of Safety and Effectiveness.  
3. If gaps exist (e.g., new algorithmic output, different patient population), plan a *limited* clinical performance study (IDE‑exempt if risk ≤ IIb; otherwise IDE required).  

> **Citation:** “임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA” – URL links to FDA guidance documents; §3 referenced within the source.  

---

### 4. Missing Information & Decision Points (to be supplied by development team)

| Item | Why Needed | Impact if Unavailable |
|------|------------|-----------------------|
| **Exact intended use & indications** | Drives predicate selection and risk classification. | Cannot finalize SE comparison; may force De Novo route. |
| **Proposed predicate device(s) (K‑Numbers)** | Required to claim substantial equivalence. | Without a valid predicate, 510(k) not permissible. |
| **Device architecture diagram (hardware/software split)** | Determines applicable standards and testing scope. | Incomplete risk analysis; may trigger additional FDA queries. |
| **Biocompatibility exposure profile** (if patient‑contacting) | Required for ISO 10993‑1 assessment. | Potential safety deficiency flagged during review. |
| **Cybersecurity threat model** | Needed for PCCP and post‑market change control plan. | May result in a “Additional Information” request on software security. |
| **UDI labeling strategy (HRI vs label)** | Must comply with 21 CFR §830.10‑§830.60. | Non‑compliant labeling leads to refusal-to-accept (RTA). |

*These gaps constitute immediate escalation triggers (see Section 6).*

---

### 5. Core Risk Controls (aligned to ISO 14971 2019)

1. **Hazard Identification:** Failure mode and effects analysis (FMEA) of hardware, software, and user interaction.  
2. **Risk Control Measures:** Design safeguards (e.g., lock‑out, alarm thresholds), redundancy for critical sensors, input validation for software.  
3. **Residual Risk Evaluation:** Comparison against acceptable risk criteria; documented justification for any residual risk that remains.  
4. **Verification/Validation:** Test plans covering each control per IEC 60601‑1, IEC 62304, and IEC 62366‑1 where applicable.  
5. **Post‑Market Monitoring:** Implement FDA’s Medical Device Reporting (MDR) under 21 CFR §803 and voluntary correction/removal procedures under 21 CFR §806.

---

### 6. Human‑Escalation Triggers

| Trigger | Reason for Escalation | Recommended Owner |
|---------|-----------------------|-------------------|
| **Absence of a clear predicate (K‑Number)** | Unable to submit SE claim; risk of De Novo classification. | Project Lead / Regulatory Strategy Lead |
| **Unresolved clinical data requirement** after bench comparison | FDA may issue an AI request demanding clinical evidence. | Clinical Affairs Lead |
| **Incomplete risk management file** (missing FMEA, residual‑risk justification) | Likely source of 21 CFR §820.30 non‑conformance; could delay clearance. | QA/QMS Manager |
| **UDI labeling plan not finalized** | Potential RTA under 21 CFR §807. | Labeling Specialist |
| **Cybersecurity PCCP not drafted** (for software device) | FDA may request a Predetermined Change Control Plan per Dec 2024 guidance. | Software Engineering Lead |
| **Biocompatibility data gap for patient‑contacting components** | Violation of ISO 10993‑1 requirements; safety concern. | Materials / Biocompatibility Team |

When any trigger is identified, the responsible owner must:
1. Document the issue in the regulatory tracker.  
2. Convene a cross‑functional review (RA, Engineering, Clinical).  
3. Provide a mitigation plan within 5 business days.  

If resolution cannot be achieved within 15 days, **escalate to senior management** and consider alternative pathways (De Novo or PMA) per the summary table in the source.

---

### 7. Peer‑Review Prompt
> *“Colleague, please evaluate whether our assumption that a Class II 510(k) is feasible given the limited information on intended use and predicate devices holds up under FDA’s decision matrix. Are there any jurisdictional nuances (e.g., QMSR Part 820 alignment, UDI labeling) we have missed or mis‑applied? Also, verify that all cited CFR sections correspond to the current edition of the regulations.”*  

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

> ① "voluntary correction/removal procedures under 21 CFR §806" — §806는 의무 보고(3회차 재발 계열) ② UDI 라벨 배치 "§830.10-§830.60" — 배치는 Part 801 Subpart B(재발 계열).

**Source Excerpts**

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20261104-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "069be81777ba2be7", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `069be81777ba2be7`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/README.md)
- Source hash: `1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `README.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용 ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Info...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **510(k) Predicate Strategy – Draft Regulatory Plan**

---

### 1. Classification & Submission Route  
| Item | Determination | Rationale / Citation |
|------|---------------|----------------------|
| **Device class** | Class II (most imaging‑related hardware/software) | Default for medical image management/processing systems under **21 CFR §892.2050** (Class II). If the device is a storage, communications, or digitizer unit, use §§ 892.2010‑892.2040 accordingly. |
| **Submission type** | Premarket Notification – 510(k) | Required for Class II devices unless exempt; see **21 CFR §807.92(a)**. |
| **Regulatory pathway** | Substantial‑equivalence claim with identified predicate(s) | Follow the three‑step workflow listed in the source (predicate search → SE comparison table → 510(k) sections). |

*If no appropriate predicate is found, consider a De Novo classification request.*

---

### 2. Required Evidentiary Package  

| Section (per 21 CFR §807.92) | Core Elements | Typical Supporting Documents |
|------------------------------|---------------|-------------------------------|
| **Device Description & Indications for Use** | Detailed narrative, drawings, photos, labeling excerpts | eSTAR Device‑Description template; IFU draft. |
| **Substantial‑Equivalence Comparison Table** | Side‑by‑side table of device specifications, performance, labeling | Completed SE matrix (source step 2). |
| **510(k) Summary / Statement** | Synopsis of device, intended use, differences from predicate | FDA‑formatted summary. |
| **Performance Testing** | Bench or animal studies demonstrating functional equivalence (e.g., image quality metrics, throughput, latency) | Test protocols, raw data, statistical analysis. |
| **Biocompatibility** *(if patient-contacting)* | ISO 14971 risk assessment; ISO 10993‑1 testing where applicable | Cytotoxicity, sensitization, irritation reports. |
| **Electromagnetic Compatibility (EMC)** | IEC 60601‑1‑2 (or relevant IEC/ISO for non‑clinical devices) compliance data | Emissions & immunity test reports. |
| **Software Validation** *(if software component ≥ Class II)* | IEC 62304 development lifecycle evidence; verification & validation results | Code review records, unit/integration testing logs. |
| **Risk Management File** | ISO 14971:2019 risk analysis, mitigations, residual risk evaluation | Risk management plan & report (RM‑01). |
| **Labeling & IFU** | 21 CFR §801 labeling requirements; UDI placement per **21 CFR §830.10‑§830.30** | Draft labels, packaging artwork, UDI carrier file. |
| **Quality System Documentation** | Compliance with QMSR (21 CFR Part 820) aligned to ISO 13485:2016 | SOPs, design history file, complaint handling. |

*All sections are to be assembled in the eSTAR electronic submission template (source step 4).*

---

### 3. Gaps / Missing Information (to be sourced from the sponsor)

| Required Item | Current Status | Action Needed |
|---------------|----------------|---------------|
| **Exact Intended Use & Indications for Use** | Not provided in source excerpts | Obtain final IFU wording; confirm patient population, clinical setting. |
| **Predicate Device List (K- numbers)** | Only a generic “predicate search” described | Perform FDA 510(k) database query; capture K‑numbers, cleared dates, and classification codes. |
| **Device Architecture Diagram** | Not in excerpt | Supply high‑level block diagram with hardware/software interfaces. |
| **Risk Management Report (ISO 14971)** | No reference | Draft RM file covering hazards, severity, probability, mitigations. |
> *If any of the above cannot be supplied within 30 days, trigger human escalation.*

---

### 4. Risk Controls & FDA‑Specific Plans  

1. **Risk Management** – ISO 14971:2019 (risk analysis, mitigation, verification).  
2. **Design Controls** – 21 CFR §820.30 (design input/output, verification, validation).  
3. **Software Change Control** – If AI/ML updates are anticipated, develop a **Predetermined Change Control Plan (PCCP)** per FDA final guidance (Dec 2024).  
4. **UDI Implementation** – Follow 21 CFR §830.10‑§830.30; register device identifier in GUDID.  
5. **Post‑market Surveillance** – Set up a complaint handling system and voluntary correction/removal process under **21 CFR Part 806** (field safety notice equivalent).  

---

### 5. Citations  

| Regulatory Requirement | Source Type | Citation |
|------------------------|------------|----------|
| Classification of imaging software | Framework reference | 21 CFR §892.2050 (Class II) |
| 510(k) submission requirements | Framework reference | 21 CFR §807.92(a) |
| QMS regulation effective Feb 2026 | Framework reference | 21 CFR Part 820 (QMSR) |
| UDI labeling obligations | Framework reference | 21 CFR §830.10‑§830.30 |
| Risk management standard | Framework reference | ISO 14971:2019 |
| Software development lifecycle | Framework reference | IEC 62304 2006+A1:2015 |
| Biocompatibility standard | Framework reference | ISO 10993-1:2018 |
| EMC testing requirement | Framework reference | IEC 60601‑1‑2 (referenced by FDA for medical devices) |
| Predetermined Change Control Plan (PCCP) guidance | Framework reference | FDA Final Guidance, Dec 2024 – “Predetermined Change Control Plan” |

*No specific instance identifiers (e.g., K-numbers, docket IDs) were present in the source excerpts; therefore none are listed — verify separately.*

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Why Escalate | Recommended Action |
|-------------------|--------------|---------------------|
| **No suitable predicate identified** after exhaustive FDA database search | Unable to claim substantial equivalence → possible De Novo or PMA need | Notify project lead; prepare De Novo dossier outline. |
| **Intended Use or Indications for Use remain undefined** past 30‑day grace period | Classification may shift; labeling non‑compliant | Senior RA review and sign‑off before draft submission. |
| **Risk Management File incomplete (missing hazard analysis)** | FDA will issue AI on risk controls, delaying clearance | Elevate to Quality Manager; allocate resources for RM completion. |
| **FDA issues an Additional Information (AI) request** during review | 180‑day response clock starts; may affect launch timeline | Activate AI response team; escalate to Project Manager for schedule impact. |
| **Emergent safety signal reported in post‑market period** | Potential FDA enforcement or recall under Part 806 | Initiate field corrective action plan; involve regulatory affairs senior leadership. |

---

### 7. Bottom‑Line Regulatory Judgment  

- The device is a **Class II imaging system** and will pursue **510(k) clearance via substantial equivalence** to identified predicate devices.  
- Completion of the evidentiary package (performance, biocompatibility, EMC, software validation, risk management, labeling, UDI) as outlined above is mandatory before electronic submission using the eSTAR template.  
- Any gap in predicate identification, intended use definition, or risk analysis must be escalated immediately to senior RA staff to avoid downstream FDA AI requests or the need to shift to a De Novo pathway.

---

**Peer‑Review Prompt**  
> *Please review this draft for any overlooked jurisdictional nuances (e.g., recent QMSR updates), gaps in source coverage, or assumptions about device class that may require confirmation. Highlight any additional evidence you believe is essential for the 510(k) submission.*

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

> ① 510(k) 제출요건 근거 "21 CFR §807.92(a)" — §807.92는 Summary 조항(4회차 재발) ② "voluntary correction/removal process under Part 806" (재발) ③ UDI 배치 §830.10-§830.30.

**Source Excerpts**

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20261104-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "fb8982d1b88cf65b", "source": "github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md", "source_hash": "fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `fb8982d1b88cf65b`
- Source: `github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week03_FDA_510k_%EC%83%81%EC%84%B8.md)
- Source hash: `fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `Week03_FDA_510k_상세.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Predicate Strategy for Company‑X X‑ray Device**

---

### 1. Classification & Submission Route  

| Item | Determination |
|------|---------------|
| **Regulatory panel** | Imaging / Radiology devices → **21 CFR Part 892** (Imaging equipment). |
| **Device class** | Most X‑ray systems are **Class II** (special controls) – see §892.1580 (X‑ray system) in the FDA regulations (confirm exact sub‑section for the specific product line). |
| **510(k) pathway** | • If a legally marketed predicate with *identical intended use* and *no new technological features* is identified, pursue a **Traditional 510(k)**. <br>• If the device shares intended use but incorporates minor design changes covered by recognized guidance (e.g., “Abbreviated” or “Special” 510(k) criteria), an **Abbreviated** or **Special 510(k)** may be appropriate. The decision follows the **SE‑5‑step decision tree** (see Section 2). |
| **Regulatory citations** | • Imaging panel – **21 CFR Part 892**.<br>• Premarket notification – **21 CFR Part 807**.<br>• Quality System Regulation (post‑Feb 2026) – **21 CFR Part 820** (QMSR).<br>• UDI requirements – **21 CFR Part 830**. |

---

### 2. SE‑5‑Step Predicate Decision (FDA 2014 Guidance, Appendix A)

| Step | Question | Outcome for Company‑X X‑ray |
|------|----------|----------------------------|
| **DP1** | Is the predicate a *legally marketed* device? | Identify FDA‑cleared X‑ray system(s). <br>**If none → NSE (De Novo or PMA).** |
| **DP2** | Does it have the *same intended use*? | Compare labeling and Indications for Use. <br>**If different → NSE.** |
| **DP3** | Are *technological characteristics* identical? | Evaluate source, detector type, dose control, software algorithms. <br>**If identical → proceed to DP5.** |
| **DP4** | Do differing tech features raise new safety/effectiveness questions? | Conduct risk analysis (ISO 14971) and determine if additional testing is required. <br>**If yes → NSE.** |
| **DP5** | Can performance data demonstrate *at least* predicate performance? | Generate bench, animal, or clinical data as needed. <br>**If yes → SE (clearance possible).** |

*The above logic must be documented in the “Substantial Equivalence Discussion” section of eSTAR.*

---

### 3. Required Evidence Package (eSTAR Core Sections)

| Section | Minimum Content |
|---------|-----------------|
| **Device Description & Intended Use** | Detailed description, labeling claim, comparison to predicate intended use. |
| **Predicate Device(s)** | Clearance number(s), device name, FDA‑cleared indication – *no specific identifier found in source — verify separately*. |
| **Technological Comparison** | Side‑by‑side table of design specs (energy range, detector size, software features). |
| **Risk Management** | ISO 14971:2019 risk analysis file; identified hazards, mitigations, residual risk. |
| **Performance Testing** | • *Bench* – x‑ray output, beam quality, uniformity.<br>• *Software validation* – IEC 62304 (2006+A1:2015) compliance if digital processing is included.<br>• *Biocompatibility* – ISO 10993‑1 (if patient‑contacting materials). |
| **Electrical Safety & EM Compatibility** | IEC 60601‑1 (2005+A1:2012+A2:2020) test reports. |
| **Usability/ Human Factors** | IEC 62366‑1 (2015+A1:2020) verification results. |
| **Labeling & UDI** | Draft labeling per 21 CFR Part 801; UDI configuration statement per 21 CFR Part 830. |
| **Quality System** | Evidence of compliance with the new QMSR (Part 820). |

> **Note:** Any absence of a listed element must be flagged as *missing information* and addressed before submission.

---

### 4. Identified Gaps & Missing Information  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Predicate clearance number(s)** | Required for the “Substantial Equivalence” narrative. | Conduct market search; record FDA K numbers. |
| **Exact intended‑use statement** | Determines DP2 outcome and classification scope. | Draft precise Indications for Use aligned with predicate. |
| **Technological characteristics matrix** | Needed for DP3/DP4 assessment. | Populate comparison table (energy, detector type, software). |
| **Performance data plan** | Supports DP5; must meet “≥ predicate performance”. | Develop test protocols; schedule bench and possibly clinical studies. |
| **Risk Management file (ISO 14971)** | Demonstrates control of new hazards arising from any tech differences. | Compile hazard analysis, risk controls, validation reports. |
| **QMSR documentation (Part 820)** | Mandatory for all 510(k) submissions after Feb 2026. | Ensure SOPs, CAPA records, design history file are current and uploaded to eSTAR. |
| **UDI strategy** | FDA requires label and packaging UDI per Part 830. | Assign device identifier; generate GUDID record. |

---

### 5. Core Risk Controls (per ISO 14971)

1. **Radiation safety controls** – Beam limiting devices, automatic exposure control, interlocks.  
2. **Electrical safety** – Built‑in earth leakage protection, IEC 60601‑1 compliance testing.  
3. **Software safeguards** – Version control, validated algorithms, PCCP (Predetermined Change Control Plan) if post‑market updates are anticipated.  
4. **User interface design** – Hazard analysis of misuse modes; usability validation per IEC 62366‑1.  

*All controls must be documented in the risk management file and linked to verification testing.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Path |
|--------|-----------------|
| **NSE determination at any DP step** (no suitable predicate) | Immediate consult with senior RA; evaluate De Novo or PMA route. |
| **Insufficient performance data to meet DP5** | Pause submission; schedule additional testing; inform project lead. |
| **FDA Additional Information (AI) request** – >180 days to respond | Activate “AI response team”; enforce 180‑day deadline tracking. |
| **QMSR non‑conformance identified during internal audit** | Stop submission preparation; remediate QMS gaps before filing. |
| **UDI label design not compliant with Part 830** | Suspend labeling finalization; involve regulatory affairs and packaging departments. |

---

### 7. Summary Judgment  

*Based on the SE‑5‑step framework, Company‑X can pursue a Traditional or Abbreviated 510(k) **provided** a legally marketed X‑ray predicate sharing identical intended use and technological characteristics is identified. All required evidence (predicate details, risk management, performance testing, labeling/UDI, QMSR compliance) must be compiled in the eSTAR submission. Any gap that leads to an NSE outcome or FDA AI request should trigger immediate senior RA review.*

---

### 8. Peer‑Review Prompt  

> **To a fellow RA:** Please challenge the assumptions above—especially (a) the classification of our X‑ray system under §892.1580, (b) the completeness of the evidence list for a “Special 510(k)” versus an “Abbreviated 510(k),” and (c) any jurisdictional omissions such as FDA‑specific labeling nuances or UDI generation requirements. Identify where additional source verification is needed.

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

1. Chunk `1061195424067242245`

> ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과제 3-2 SE 비교표 제출 필수 ---

2. Chunk `1072507187378217632`

> ### 4.1 SE 5단계 Decision Point (FDA 2014 Guidance Appendix A) ``` DP1. Predicate이 Legally Marketed Device인가? │ No → NSE (De Novo 또는 PMA) │ Yes ↓ DP2. 동일한 Intended Use인가? │ No → NSE │ Yes ↓ DP3. 동일한 Technological Characteristics인가? │ Yes → DP5 │ No ↓ DP4. 다른 기술특성이 Different Questions of Safety & Effectiveness를 제기하는가? │ Yes → NSE │ No ↓ DP5. 성능 데이터가 새 장치 ≥ Predicate 수준임을 입증하는가? │ Yes → SE (Clearance 가능) │ No → NSE ```

### kb-eval-20261104-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f5c7ddd243c97b45", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f5c7ddd243c97b45`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_01_Device_Description_IFU.md)
- Source hash: `70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_01_Device_Description_IFU.md`는 FDA eSTAR device description 및 IFU 작성에 필요한 제품 설명·표시 정보 문서입니다.
- 현재 excerpt 핵심: ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA For...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Radiographic Image‑Acquisition GUI Software (510(k) Strategy)**  

---

### 1. Classification & Submission Route  
| Attribute | Determination |
|-----------|----------------|
| **Product class** | Class II medical device (software that controls acquisition of digital X‑ray images). |
| **CFR part** | 21 CFR **Part 892** – Radiology/Imaging devices. The most fitting product code is **“P” (Medical image management and processing system)** → § 892.2050 (Class II). If the FDA determines a more specific sub‑category, re‑classification to § 892.2030 (Image digitizer) or § 892.2020 (Communications device) may be required. |
| **Submission type** | Traditional 510(k) – substantial equivalence to a cleared predicate that performs comparable image acquisition/control functions without diagnostic claims. |
| **Regulatory timeline** | Standard review period ≈ 90 days; expect possible FDA Additional Information (AI) requests (180 calendar days to respond). |

---

### 2. Predicate Identification (to be confirmed)  
*Potential predicates (publicly cleared devices with similar functionality):*  

1. **Device A – “X‑Ray Acquisition Control Software”** – 510(k) No. _______ (Class II, §892.2050).  
2. **Device B – “Radiography Image Management System”** – 510(k) No. _______ (Class II, §892.2050).

> **Note:** The source does not provide explicit predicate identifiers. *“No specific identifier found in source — verify separately.”* A systematic search of the FDA 510(k) database using keywords “radiographic acquisition”, “X‑ray control software”, and product code “P” is required to select an appropriate predicate.

If no suitable predicate exists, a **De Novo** request (21 CFR 812.2) must be considered.

---

### 3. Required Evidence Package  

| Section | Evidence Needed | Reference |
|---------|-----------------|-----------|
| **Device Description** | • Full narrative of hardware/software architecture (modules, processes, DB, DICOM nodes). <br>• Minimum OS and hardware requirements.<br>• Compatibility list for detectors/generators with version numbers. | 21 CFR 807.87; Source excerpt 4.3 |
| **Intended Use & Indications** | • Form‑3881 (Indications for Use) completed in English. <br>• Explicit statement that the software is *not* for primary diagnosis or image interpretation. | FDA Guidance “General/Specific Intended Use” (1998); Source excerpt 4.3 |
| **Software Documentation** | • IEC 62304‑based Software Development Life Cycle artifacts: requirements, design, verification and validation reports.<br>• Software safety class (A/B/C) justification – likely Class C for acquisition control. <br>• List of SOUP components with supplier IDs. | IEC 62304 2006+A1:2015 |
| **Risk Management** | • ISO 14971‑2019 risk analysis file, including hazard identification, severity/occurrence assessment, and mitigations (e.g., fail‑safe image loss handling). <br>• Traceability matrix linking hazards to controls. | ISO 14971 2019 |
| **Verification & Validation** | • Bench testing of DICOM SCU/SCP functions (Storage, Worklist, MPPS). <br>• Performance metrics: image transfer latency, error rates, compatibility verification with each listed detector/generator.<br>• Cybersecurity assessment – authentication, encryption, audit‑log review. | FDA Guidance “Format for Traditional and Abbreviated 510(k)s” (2019‑09‑13) |
| **Labeling & IFU** | • Full labeling per 21 CFR 801; includes intended use statement, contraindications, warnings, and user training requirements.<br>• UDI label compliant with 21 CFR 830.10–830.60 (include device identifier, production identifier). | 21 CFR 801; 21 CFR 830 |
| **Quality System** | • Demonstration of compliance with the new **QMSR (Part 820)** effective February 2026 – ISO 13485:2016‑aligned. <br>• SOPs for software release, change control, and post‑market surveillance. | 21 CFR 820 |
| **Predetermined Change Control Plan** *(if future AI/ML updates anticipated)* | • PCCP (Predetermined Change Control Plan) covering planned modifications, validation approaches, and FDA notification process. | FDA Guidance “Predetermined Change Control Plan” (Dec 2024) |

---

### 4. Gaps / Missing Information (to be obtained before submission)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Predicate 510(k) numbers** | Essential for substantial equivalence claim. | Perform targeted FDA 510(k) database search; document selected predicate(s). |
| **DICOM conformance test reports** | Evidence of interoperability and data integrity. | Conduct formal DICOM SCU/SCP validation per IHE profiles; retain full report. |
| **Cybersecurity testing artifacts** | Required under Section 892.2050 and FDA guidance on software security. | Provide penetration test summary, threat model, and mitigation documentation. |
| **Risk Management Report (ISO 14971)** | Must show hazard controls for acquisition‑control failures. | Complete risk file; include residual risk justification. |
| **Labeling & UDI labeling details** | Regulatory compliance under Parts 801/830. | Draft final label; generate UDI per GUDID requirements. |
| **QMSR (Part 820) SOPs** | New QMSR mandates ISO 13485‑aligned procedures. | Verify existence of SOP‑RA‑002, SOP‑CA‑001, etc., and update to reflect 2026 requirements. |

---

### 5. Risk Controls & Mitigations (high‑level)

| Hazard | Potential Harm | Control(s) |
|--------|----------------|------------|
| Incorrect image acquisition parameters (e.g., exposure time) due to software error | Patient over‑/under‑exposure, diagnostic delay | Input validation, default safe settings, real‑time sensor feedback, alarm on out‑of‑range values. |
| Loss of acquired images before storage | Missing clinical data | Immediate local buffering with checksum verification; automatic retry to DICOM Storage SCP; audit log of transfer status. |
| Unauthorized access / tampering | Data breach, image manipulation | Role‑based authentication, TLS encryption for all network traffic, immutable audit logs, periodic security patching. |
| Software update introduces new bug (post‑market) | Device malfunction | Predetermined Change Control Plan (PCCP) with pre‑deployment regression testing and FDA notification if change alters intended use or safety class. |

All controls must be traceable to ISO 14971 risk analysis entries.

---

### 6. Regulatory Citations  

| Topic | Citation (framework) |
|-------|----------------------|
| Submission content requirements | **21 CFR 807.87** |
| 510(k) Summary format | **21 CFR 807.92** |
| Device classification – imaging | **21 CFR Part 892**, § 892.2050 (Class II, medical image management & processing) |
| Labeling requirements | **21 CFR 801** |
| UDI labeling obligations | **21 CFR 830.10–830.60** |
| Quality System Regulation (new QMSR) | **21 CFR 820** (effective Feb 2026) |
| Software life‑cycle & safety class | **IEC 62304 2006+A1:2015** |
| Risk management standard | **ISO 14971 2019** |
| Predetermined Change Control Plan guidance | FDA Final Guidance, Dec 2024 (“Predetermined Change Control Plan (PCCP)”) |

> No specific device identifiers or CFR subsection numbers beyond the framework citations were present in the source – *no specific identifier found in source — verify separately*.

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason for escalation |
|--------|-----------------------|
| **No suitable predicate identified** after exhaustive search | Decision point: move to De Novo submission; requires senior RA sign‑off and possibly FDA pre‑submission meeting. |
| **Risk analysis indicates residual risk > acceptable** | Must be reviewed by the Risk Management Lead and potentially re‑engineered before filing. |
| **Cybersecurity controls insufficient for FDA expectations** | Escalate to the CISO/Information Security lead; may need additional testing or design changes. |
| **QMSR non‑conformance (e.g., missing SOPs)** | Immediate corrective action plan needed; pause submission preparation until compliance achieved. |
| **FDA issues an Additional Information (AI) request** | Response must be coordinated across engineering, QA, and regulatory to meet the 180‑day deadline; trigger a formal AI response tracking log. |
| **Discrepancy between intended use statement and functional claims** (e.g., inadvertent diagnostic wording) | Senior RA must review and amend labeling/IFU to avoid reclassification to a higher risk class. |

Escalations should be logged in the project’s risk register and communicated to the Project Lead for timely decision‑making.

---

### 8. Peer Review Prompt  

> **Request:** Please challenge the assumptions made above, especially:  
> - The suitability of § 892.2050 versus other § 892 sections for this software.  
> - The completeness of the predicate search strategy and whether alternative product codes (e.g., “D” – X‑ray imaging system) might be more appropriate.  
> - Potential gaps in cybersecurity evidence relative to FDA’s latest guidance on medical device security.  
> - Any jurisdiction‑specific nuances missed (e.g., UDI carrier requirements, post‑market surveillance expectations under the new QMSR).  

Your feedback will ensure this draft fully addresses all US regulatory obligations before the submission package is finalized.

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

> ① De Novo 근거 "21 CFR 812.2" — §812는 IDE(연구기기 면제)이며 De Novo는 Part 860/§513(f)(2) — 재발 계열 ② UDI 배치 §830.10–830.60 범위.

**Source Excerpts**

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

### kb-eval-20261104-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "58fd31b86d3969e0", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A1_Cover_Letter_템플릿.md", "source_hash": "27034e7259b482d0ed24713a8f35b4d9f41831499a0ac3e06bb99100802d0bf5"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `58fd31b86d3969e0`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A1_Cover_Letter_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/T-FDA510K-A1_Cover_Letter_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `27034e7259b482d0ed24713a8f35b4d9f41831499a0ac3e06bb99100802d0bf5`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `T-FDA510K-A1_Cover_Letter_템플릿.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 관련 문서 | 문서 | 연계 내용 | |------|-----------| | 13_규제평가_체크리스트/FDA_510k_RTA.md | FDA-510K-A1~A5 (Section A: Submission Coverage) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B1_Device_Description_템플릿.md | Device Description (본 Cover Letter의 Device Trade Name/Common Name 근거) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md | Predicate Device 비교 근거 | ## 출처 - FDA, "Refus...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Strategy & Gap Assessment**

---

### Bottom‑Line Recommendation
- **Submit a traditional Premarket Notification (510(k))** under **21 CFR §807**.  
- Target **Class II** clearance unless the device’s intended use or technology places it in Class III; in that case, evaluate a De Novo request first.  
- Build the submission around the **FDA‑510K‑A1–A5 cover‑letter framework** (Section A: Submission Coverage) and the **Predicate Device Comparison Table (B3)** required by FDA’s Refuse‑to‑Accept (RTA) policy.

---

### 1. Classification & Submission Route
| Item | Determination |
|------|---------------|
| **Device Class** | Assume **Class II** (most imaging, diagnostic and therapeutic devices). Verify using the appropriate product code or 21 CFR §862/§892 classification rule once intended use is finalized. |
| **Regulatory Pathway** | Traditional **510(k) Premarket Notification** (21 CFR §§807.81‑807.100). If no legally marketed predicate exists, consider a **De Novo** request (21 CFR §860.30). |
| **Key CFR References** | 21 CFR §807 (submission), 21 CFR Part 820 (QMS), 21 CFR Part 830 (UDI). |

---

### 2. Core Evidence Required for a Complete 510(k)  
| Category | Typical Content | Minimum Supporting Documents |
|----------|----------------|------------------------------|
| **Device Description** | Trade name, common name, model numbers, specifications, accessories, labeling excerpts. | Template B1 – Device Description (internal). |
| **Intended Use & Indications for Use** | Clear statement matching that of the predicate. | Cover letter Section A2; label draft. |
| **Predicate Comparison (Substantial Equivalence)** | Table showing each characteristic (technology, materials, performance) side‑by‑side with the selected predicate(s). | Template B3 – Predicate Device Comparison. Must include predicate’s 510(k) number and FDA clearance date. |
| **Performance Testing** | • Bench/bench-top testing (e.g., accuracy, precision, durability). <br>• Electrical safety & EMC per IEC 60601‑1 (if applicable).<br>• Software verification/validation (IEC 62304) when software is present.<br>• Biocompatibility per ISO 10993‑1 (if patient‑contacting).<br>• Sterilization validation (where relevant). | Test protocols, raw data, statistical analysis reports. |
| **Clinical Data** *(only if needed to bridge a technological gap)* | Limited clinical study or literature support demonstrating safety/effectiveness comparable to predicate. | IRB approval, informed consent forms, case report forms, statistical summary. |
| **Labeling & IFU** | Full labeling set (USP, Instructions for Use, packaging). Must meet 21 CFR §801. | Drafts, font size verification. |
| **UDI Plan** | Device identifier, production identifier, label layout, GUDID submission evidence. | UDI implementation plan per 21 CFR Part 830. |
| **Quality Management System Evidence** | Declaration of conformity to **QMSR (21 CFR Part 820)** – ISO 13485:2016 alignment; procedures for design control, risk management, corrective action, etc. | SOP list (e.g., SOP‑RA‑002, SOP‑CA‑001), audit reports, CAPA logs. |
| **Risk Management** | ISO 14971:2019 risk analysis file – hazard identification, evaluation, mitigation, residual risk justification. | Risk Management Report, FMEA/FMECA tables. |

---

### 3. Missing / Unverified Information (Gap List)  
1. **Predicate Device Identifier(s)** – specific 510(k) numbers and product codes not supplied in the source.  
2. **Exact Intended Use Statement** – needs to be drafted and cross‑checked with predicate labeling.  
3. **Risk Management File** – ISO 14971 analysis, risk control measures, verification results absent.  
4. **Performance Test Results** – protocols, raw data, statistical justification not yet prepared.  
5. **UDI Implementation Details** – label format, issuance agency, GUDID submission evidence missing.  
6. **QMS Documentation for New QMSR (effective Feb‑2026)** – SOPs aligned to 21 CFR Part 820 and ISO 13485:2016 need confirmation.  
7. **Software Documentation** (if applicable) – IEC 62304 development lifecycle, PCCP (Predetermined Change Control Plan) for any AI/ML updates not addressed.  

> *No specific identifier found in source – verify separately* (e.g., predicate 510(k) numbers, exact CFR sections cited in the RTA guidance).

---

### 4. Risk Controls – Core Elements to Include
| Hazard Category | Control Strategy | Reference Standard |
|-----------------|------------------|--------------------|
| Electrical safety / leakage currents | Design compliance with IEC 60601‑1 (2005+A1:2012+A2:2020) | IEC 60601‑1 |
| Software failures (if device contains software) | Development lifecycle per IEC 62304 (2006+A1:2015); PCCP for post‑market changes | IEC 62304, Predetermined Change Control Plan (Dec 2024 guidance) |
| Biocompatibility (patient contact) | Material testing per ISO 10993‑1 (2018) – cytotoxicity, sensitization, irritation, etc. | ISO 10993‑1 |
| Sterilization efficacy (if marketed sterile) | Validation per ASTM E3135; sterilization cycle verification & residue analysis | ASTM/ISO standards (referenced in FDA guidance). |
| Use errors / usability | Human factors engineering per IEC 62366‑1 (2015+A1:2020). | IEC 62366‑1 |
| Residual risk – overall | ISO 14971:2019 risk assessment, residual risk acceptance criteria documented. | ISO 14971 |

---

### 5. Citations  

**Framework References (no verification caveat needed)**  
- **21 CFR §807** – Premarket Notification (510(k)).  
- **21 CFR Part 820** – Quality System Regulation (QMSR, effective Feb 2026).  
- **21 CFR Part 830** – Unique Device Identification.  
- **ISO 14971:2019** – Risk Management for Medical Devices.  
- **ISO 13485:2016** – QMS requirements.  
- **IEC 62304:2006+A1:2015** – Software Life Cycle Processes.  
- **IEC 60601‑1:2005+A1:2012+A2:2020** – General Safety and Performance Requirements for Medical Electrical Equipment.  
- **IEC 62366‑1:2015+A1:2020** – Usability Engineering.  

**Instance Identifiers (source‑derived)**  
- Source mentions *“FDA, ‘Refuse to Accept Policy for 510(k)s’ Guidance”* but provides no section number → **no specific identifier found in source – verify separately**.

---

### 6. Human‑Escalation Triggers  

| Condition | Action |
|-----------|--------|
| **Predicate not identified or unsuitable** (no legally marketed counterpart) | Escalate to senior RA for De Novo/PMA pathway consideration. |
| **RTA notice issued** (FDA deems submission non‑acceptable) | Pause filing, convene cross‑functional review, and address the cited deficiencies before resubmission. |
| **Major risk control gaps** (e.g., missing ISO 14971 file, incomplete IEC 62304 verification) | Escalate to QA/Engineering lead for immediate mitigation; halt submission prep until resolved. |
| **UDI labeling non‑compliant** (label lacks required format or GUDID data) | Notify regulatory ops and packaging teams; do not submit until corrected. |
| **New QMSR requirements unmet** (evidence of 21 CFR Part 820 compliance absent) | Raise to Quality Assurance manager for gap remediation. |
| **AI/ML algorithm change planned without PCCP** | Trigger a PCCP creation and FDA interaction before any post‑market software update. |

---

### 7. Peer‑Review Prompt  

> *Colleague, please challenge the assumptions above: (1) Is Class II the most appropriate default given we lack device‑specific details? (2) Have we captured all evidence categories required by the latest RTA guidance, or are any FDA‑specified items omitted? (3) Are there jurisdictional gaps—particularly regarding the new QMSR and UDI implementation—that need deeper analysis before finalizing the submission plan?*  

--- 

**End of Draft**

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

1. Chunk `108125790997756669`

> ## 관련 문서 | 문서 | 연계 내용 | |------|-----------| | 13_규제평가_체크리스트/FDA_510k_RTA.md | FDA-510K-A1~A5 (Section A: Submission Coverage) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B1_Device_Description_템플릿.md | Device Description (본 Cover Letter의 Device Trade Name/Common Name 근거) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md | Predicate Device 비교 근거 |

2. Chunk `137836772921583289`

> ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance (최신 개정판 확인 후 인용 필요 — 본 v0.1은 구조만 정의, 조항 원문 대조 미실시)

## ra_eu

### kb-eval-20261104-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "43fefc68dc864555", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `43fefc68dc864555`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/README.md)
- Source hash: `30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules) ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MDR 2017/745 Classification & Conformity‑Assessment Pathway**

---

### 1. Device Scope (derived from source)

| Element | Observation (source) |
|---------|----------------------|
| **Device family** | “Ionising radiation emitting diagnostic device (X‑ray generator)” – Rule 10 (source [2]) |
| **Software component** | “Medical Device Software (SaMD)” – Rule 11 (source [2]) |
| **Applicable MDR parts** | Annex I (GSPR), Annex II (Technical Documentation), Annex III (PMS), Annex VIII (Classification Rules) (source [1]) |

> *The draft assumes the device under review is an X‑ray generator (or a related diagnostic system) that may incorporate SaMD. If the actual product differs, re‑classify accordingly.*

---

### 2. Classification Determination  

| MDR element | Requirement | Application to the device |
|-------------|-------------|----------------------------|
| **Rule 10** – ionising radiation emitting diagnostic devices | Class IIb (direct emission of ionising radiation) | Applies to the X‑ray source/generator (source [2]) |
| **Rule 11** – SaMD providing diagnostic information | Class IIa (if impact limited) or IIb/III (if decision could cause serious deterioration or death) | Apply the higher class that results from the combined system; for a typical diagnostic X‑ray workflow the software is usually **Class IIa**, but if it drives therapy or critical decisions the class may rise. |
| **Overall device class** | Highest class triggered by any constituent | **Class IIb** (driven by Rule 10) |

**Citation:** MDR 2017/745 Rule 10 & Rule 11; Annex VIII classification rules (source [2]).

---

### 3. Conformity‑Assessment Route  

| Class | Art. 52 paragraph | Mandatory NB involvement | Applicable route |
|-------|-------------------|--------------------------|------------------|
| IIb   | Art. 52(4)        | Yes                      | **Annex IX** (QMS + full technical‑documentation assessment) **or** **Annex X + Annex XI** (type‑examination + production conformity verification) |

> *The manufacturer may select either route; the choice must be reflected in the EU Declaration of Conformity (Art. 19).*

**Citation:** MDR Art. 52(4); Annex IX, Annex X, Annex XI (framework reference).

---

### 4. Evidence Package Required for NB Review  

| Documentation | Core content (MDR references) | Remarks |
|---------------|--------------------------------|---------|
| **Technical Documentation (TD)** | Annex II §§1‑6 – device description, intended purpose, design & manufacturing information, GSPR compliance, risk management & benefit–risk analysis, verification/validation data. | Must include the classification justification (Rule 10) and any software documentation. |
| **EU Declaration of Conformity** | Art. 19; content specified in Annex IV. | Signed by the legal manufacturer. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept up‑to‑date (Art. 61). | Should contain state‑of‑the‑art literature on diagnostic X‑ray systems, equivalence justification if applicable, and a risk–benefit assessment. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B. | Required for Class IIb devices; defines ongoing clinical data collection. |
| **PMS System** | Art. 83; PMS Plan Art. 84; PSUR Art. 86 (annual for Class IIb). | Include procedures for trend reporting (Art. 88) and vigilance (Art. 87). |
| **Risk Management File** | ISO 14971:2019; Annex I §3‑9 (risk management system, risk control, use‑error analysis, device lifetime, transport/storage, benefit‑risk). Specific to X‑ray: radiation protection – Annex I §16.4. |
| **Usability Engineering File** | IEC 62366‑1:2015+A1:2020 (if software influences user interaction). | Aligns with Annex I §17 (electronic programmable systems) and §22 (lay‑person use, if applicable). |
| **IEC Standards for X‑ray Equipment** | IEC 60601‑2‑54 (projection radiography), IEC 60601‑2‑28 (X‑ray tube assemblies), IEC 60601‑2‑44 (CT). | Demonstrate compliance with essential safety requirements. |

All above items must be referenced in the TD (§6.1 of Annex II) and made available to the NB during assessment.

---

### 5. Identified Gaps – Information Needed Before Submission  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended use statement** (patient group, clinical setting, imaging modality) | Determines applicability of Rule 10 & influences risk analysis. | Obtain from product specification / labeling. |
| **Software architecture description & classification justification** | Needed for Rule 11 application and IEC 62304 compliance. | Provide Software Design Description, SaMD classification rationale. |
| **Clinical performance data (bench + in‑vivo) or equivalence evidence** | Required for CER; supports safety claim for ionising radiation exposure levels. | Compile literature search, pre‑market studies, or equivalence dossier. |
| **Radiation dose management strategy & verification of compliance with Annex I §16.4** | Demonstrates adherence to radiation protection GSPR. | Submit measurement reports, DQE data (IEC 62220‑1‑1) and shielding analysis. |
| **PMS Plan details (frequency of PSUR, trend‑analysis methodology)** | Needed for Art. 84/86 compliance; NB will review completeness. | Draft PMS plan with defined post‑market data sources. |
| **Risk Management File – residual risk evaluation** (particularly use‑error & accidental exposure) | Annex I §3‑9 requirement; high relevance for ionising radiation devices. | Complete ISO 14971 analysis, include mitigations and verification results. |

---

### 6. Core Risk Controls (per GSPR)

| Control Area | Relevant GSPR clause | Implementation note |
|--------------|----------------------|---------------------|
| **Risk Management System** | Annex I §3‑9 | ISO 14971:2019 based RMF, updated after each design change. |
| **Radiation Protection** | Annex I §16.4 | Shielding, dose monitoring, compliance with IEC 60601‑2‑54/28; validated by test data. |
| **Software Safety & Usability** | Annex I §17 (electronic programmable systems), §22 (lay‑person) | IEC 62366‑1 UI validation, IEC 62304 lifecycle controls. |
| **Active Device Controls** | Annex I §18 (active devices) | Ensure safe operation of power supplies, interlocks, emergency stop. |
| **Labeling & IFU** | Annex I §23 | Clear indications, contraindications, exposure limits, user training instructions. |

---

### 7. Human‑Escalation Triggers  

| Situation | Trigger for escalation to senior RA / regulatory manager |
|-----------|----------------------------------------------------------|
| **Unclear classification** – conflicting Rule 10 vs. Rule 11 outcomes or missing intended‑use definition. |
| **Insufficient clinical evidence** – no equivalence justification, or lack of post‑market data for radiation dose. |
| **Risk‑management gaps** – residual risk not justified as acceptable, especially use‑error leading to over‑exposure. |
| **PMS/PMCF plan not aligned with Art. 86 cadence** (annual PSUR missing). |
| **NB feedback indicating incomplete TD** (e.g., missing software validation reports). |
| **Regulatory change notice** – new EU regulation or guidance affecting X‑ray devices (e.g., amendment to Regulation 2023/607). |

When any trigger occurs, the case must be flagged in the project tracker and a formal request for additional information or expert review initiated.

---

### 8. Peer Review Prompt  

> **RA Peer:** Please challenge the assumptions made above regarding (a) the applicability of Rule 10 to the X‑ray generator versus possible classification under Rule 9, (b) whether the chosen conformity‑assessment route (Annex IX vs. Annex X + XI) best fits a combined hardware‑software system, and (c) any jurisdiction‑specific gaps that might arise from recent updates to Regulation 2023/607. Identify missing source coverage or alternative interpretations that could affect the classification or evidence requirements.

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

> "PSUR Art. 86 (annual for Class IIb)" — IIb는 최소 2년. 소스에 주기 없는 모델 내재 오류 3연속 회차 재발.

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261104-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b1708f548ad30357", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b1708f548ad30357`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week04_MDR_EU_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `Week04_MDR_EU_체계_상세.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUF...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Classification, Conformity‑assessment Route & Evidence Gap‑Analysis**

---

### 1. Device Context (to be supplied by the manufacturer)

| Item | What is required from the sponsor | Why it matters |
|------|-----------------------------------|----------------|
| **Intended purpose / indication** | Full natural‑language statement plus any labelled claims (diagnostic, therapeutic, monitoring, etc.) | Drives the selection of the appropriate Annex VIII rule and therefore the class. |
| **Target patient group & user profile** | Adults, paediatric, lay‑person use, professional only, etc. | Affects “use‑error” considerations (Annex I §5) and may up‑grade classification under Rule 11/9. |
| **Device description & principal design** | Materials, energy source, software components, ancillary accessories, measuring/active functions. | Needed to map the device against the 22 Annex VIII rules (Article 51 + Annex VIII). |
| **Technical specifications** | Nominal power, frequency, radiation output, measurement range, connectivity, etc. | Required for risk‑management inputs and for determining whether a rule concerning active or measuring devices applies. |
| **Lifecycle & re‑usability** | Single‑use vs reusable surgical instrument, sterile vs non‑sterile. | Determines whether the “Is/Im/Ir” sub‑class applies (Art 52(7)). |

*If any of the above are missing, classification cannot be finalised – see Section 4.*

---

### 2. Classification Procedure (per MDR)

1. **Apply self‑classification** – manufacturer must perform the classification in accordance with **Article 51 + Annex VIII** (source [2]).  
   - Sequentially test the device against the 22 rules; the highest rule that applies gives the final class.  
2. **If doubt remains** → request an informal opinion from the Competent Authority (CA) or consult the **MDCG “Borderline and Classification” manual v2.1.1 (2023‑09)** (source [2]).  
3. **Document the decision** in a *Classification Report* including: rule applied, rationale, and reference to supporting technical data.

> **Citation:** Article 51; Annex VIII (classification rules); MDCG Manual v2.1.1 (2023‑09).

---

### 3. Conformity‑Assessment Route (Art 52 mapping)

| Determined Class | MDR Art 52 paragraph* | Required NB involvement & route |
|------------------|----------------------|---------------------------------|
| **Class I** (non‑sterile, non‑measuring) | Art 52(7) – self‑declaration | No NB; technical file + EU DoC (Annex IV). |
| **Class Is / Im / Ir** | Art 52(7) – limited NB scope (sterility/measurement) | NB review of sterile/measuring aspects only (Annex IX Chapters I & III or Annex XI Part A). |
| **Class IIa** | Art 52(6) | Full assessment under **Annex IX** (QMS + technical documentation) *or* Annex II + III with production conformity verification (Annex XI §10). |
| **Class IIb** | Art 52(4) | Either **Annex IX** (full NB review) *or* **Annex X** (type‑examination) + **Annex XI** (production conformity). |
| **Class III** | Art 52(3) | Full NB assessment under **Annex IX** *or* **Annex X** + **Annex XI**. |

\*The exact paragraph is taken from the MDR; see **Art 52** for the mapping.

---

### 4. Evidence Package Required (per class)

| Evidence Item | Minimum Content | Reference |
|---------------|-----------------|-----------|
| **Technical Documentation (TD)** | Sections 1‑6 of **Annex II** (device description, design & manufacturing, GSPR fulfilment, risk‑benefit analysis, verification & validation). For Classes IIa+ also include **Annex III** PMS documentation. | Annex II; Annex III |
| **Clinical Evaluation Report (CER)** | Systematic literature review + clinical data satisfying **Article 61** and **Annex XIV Part A** (state‑of‑the‑art, clinical performance). | Article 61; Annex XIV Part A |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | For Classes IIa+ – PMCF plan per **Annex XIV Part B**, updated annually. | Annex XIV Part B |
| **PMS System** | PMS system (Art 83), PMS plan (Art 84), periodic safety update report (PSUR) for IIa/IIb/III (Art 86). | Art 83‑86 |
| **Risk Management File (RMF)** | Full RMF compliant with **ISO 14971:2019** and fulfilling **Annex I §3‑9**. | Annex I §§1‑9; ISO 14971:2019 |
| **Usability/IEC 62366‑1 evidence** (if user interaction is critical) | Usability engineering file demonstrating compliance with **Annex I §17**. | IEC 62366‑1:2020 |
| **Software Lifecycle Dossier** (if device contains software ≥ Class IIa) | Conformance to **IEC 62304** and evidence of classification under **Rule 11**. | IEC 62304; Rule 11 |
| **UDI Registration** | EUDAMED entry for UDI/DEV, linkage to GMDN/ICD coding. | MDR Art 27‑28 (EUDAMED) |
| **Authorized Representative Declaration** | Signed AR appointment per **Article 11**. | Article 11 |

*Note:* The source excerpt mentions **“CEP + CER (Article 61, MDR Annex XIV)”**, confirming the need for a clinical evaluation. It also lists **Vigilance (MDR Art.87), PSUR** and **Authorized Rep. (Art.11)** – these are included above.

---

### 5. Identified Gaps & Missing Information

| Gap | Impact on Regulatory Submission | Action Required |
|-----|----------------------------------|-----------------|
| **Intended purpose / indication not provided** | Cannot select correct Annex VIII rule → classification unresolved. | Obtain a complete intended‑use statement from the sponsor. |
| **Device architecture (active/diagnostic/software) unknown** | May miss Rule 9, 10, 11, 17 application; risk of under‑classifying. | Request detailed block diagram and functional description. |
| **Clinical data / literature search not supplied** | CER cannot be compiled → non‑compliant with Art 61/Annex XIV Part A. | Provide pre‑market clinical investigation results or published studies. |
| **Risk management file absent** | Non‑conformity with Annex I §3‑9; NB will reject. | Deliver a full RMF (ISO 14971). |
| **PMS plan not drafted** (required from Class IIa upward) | Failure to meet Art 84/86 obligations → post‑market non‑compliance. | Draft PMS plan and schedule PSUR updates. |
| **UDI allocation strategy missing** | EUDAMED registration incomplete; market entry delayed. | Allocate a GMDN‑linked UDI and complete the EUDAMED entry. |
| **Authorized Representative not appointed (if manufacturer outside EU)** | Article 11 requirement unsatisfied → cannot place CE mark. | Identify and contract an AR in the EU. |

---

### 6. Risk Controls to be Demonstrated

1. **Risk Management System** – per **Annex I §3** and **ISO 14971:2019** (risk analysis, evaluation, control, residual risk acceptance).  
2. **Use‑Error Mitigation** – address **Annex I §5**, especially if device is intended for lay users.  
3. **Sterility Assurance / Measuring Accuracy** – where “Is/Im/Ir” applies, evidence of validated sterilisation processes (ISO 13408) and measurement traceability (ISO 10993‑1 for biocompatibility if invasive).  
4. **Software Safety** – compliance with **Annex I §17**, IEC 62304 lifecycle documentation, and cybersecurity measures per IEC 82301‑1 (if applicable).  
5. **Radiation Protection** – if the device emits ionising radiation, demonstrate conformity to **Annex I §16** and relevant IEC 60601‑2‑* standards*.  

All controls must be reflected in the TD, RMF and the clinical evaluation.

---

### 7. Human‑Escalation Triggers (when to raise to senior RA / legal)

| Trigger | Reason for escalation |
|--------|-----------------------|
| **Unresolved classification** after applying all Annex VIII rules and consulting MDCG manual. | Risks incorrect NB route; may require CA formal advice. |
| **Lack of clinical data** for a Class IIa+ device (no CE‑marked predicate, no robust literature). | May need to design/execute a clinical investigation – requires project planning & budget approval. |
| **Missing Authorized Representative** for non‑EU manufacturer. | Legal liability; cannot proceed with CE marking without AR appointment (Art 11). |
| **Significant residual risk** that cannot be justified by benefit (Annex I §8). | Needs senior clinical/safety review and possibly redesign. |
| **Discrepancies between the RMF and GSPR fulfilment claims** in TD. | NB audit will flag; must resolve before submission. |
| **Regulatory fee uncertainty** (e.g., NB contract costs, MDUFA fees mentioned in source). | Financial approval needed from management. |

When any of these triggers are hit, the RA should log a *Work Package* comment recommending human review and pause further document finalisation.

---

### 8. Summary Judgment

- **Current status:** Classification cannot be confirmed without detailed intended‑use and functional information.  
- **Next steps:** Obtain missing device description, perform rule‑by‑rule classification (Annex VIII), compile the required evidence list above, and develop risk‑management & PMS artefacts in parallel.  
- **Conformity route:** Once class is known, follow the Art 52 mapping to either self‑declaration (Class I) or NB‑involved assessment (Classes Is/Im/Ir, IIa–III).  

---

### 9. Peer‑Review Prompt

> *@RA‑colleague:* Please review the assumptions made in Sections 1‑4, especially regarding the applicability of Annex VIII rules without a concrete device description. Verify that all cited MDR articles and annexes correspond to the latest (2024) consolidated text. Check whether any additional EU guidance (e.g., MDCG 2022‑5 on clinical evaluation for software) should be referenced given the possible presence of software components.

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

> ① "cybersecurity measures per IEC 82301-1" — 해당 번호 표준 없음(81001-5-1/82304-1 혼동 추정) ② "measurement traceability (ISO 10993-1 for biocompatibility if invasive)" — 측정추적성과 생체적합성 표준의 오결합.

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261104-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "baf42440b110ec02", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md", "source_hash": "4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `baf42440b110ec02`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_%EC%9D%B8%ED%97%88%EA%B0%80_%EC%83%81%EC%84%B8%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_인허가_상세가이드.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 2.3 Rule 11 (SW) > Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as class IIa. > 단, decision may cause (a) death or irreversible deterioration → **Class III**; (b) serious deterioration or surgical intervention → **Class IIb**. > Software intended to monitor physiological...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Imaging‑Room GUI Software (Medical Device Software)**  

---

### 1. Device Synopsis (derived from source)

| Item | Detail |
|------|--------|
| **Product type** | Graphical‑user‑interface (GUI) software used in the radiology imaging suite to display image data and provide information that may be used for diagnostic or therapeutic decisions (“촬영실 GUI SW”). |
| **Intended purpose** | To present acquired X‑ray/CT/MR images together with basic quantitative parameters (e.g., DICOM tags, exposure settings) that can influence the clinician’s decision on diagnosis or subsequent treatment. |
| **Regulatory source excerpt** | “촬영실 GUI SW = Rule 11 적용, 영향도에 따라 IIa ~ III”【1】 |

---

### 2. Classification Determination (MDR)

| Clause / Rule | Application to the software | Preliminary class* |
|----------------|-----------------------------|-------------------|
| **Rule 11 (Software)** – “software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes” → classified **class IIa**; if the decision may cause **(a) death/irreversible deterioration** → **Class III**, **(b) serious deterioration or surgical intervention** → **Class IIb**【1】 | The GUI supplies image information that can be decisive for a diagnostic conclusion. Without evidence that the software alone triggers life‑threatening decisions, the default is **Class IIa**. If the manufacturer states that the software drives immediate therapeutic actions (e.g., automated dose adjustment) that could cause serious deterioration, upgrade to **Class IIb**; if it can cause death/irreversible damage, **Class III**. |
| **Final classification** | *To be confirmed* – requires a risk‑based justification of the decision impact (see Section 4). |

\*The draft assumes Class IIa pending further clarification.

---

### 3. Conformity‑Assessment Route (Art. 52 MDR)

| Device class | Applicable route(s) | Notified‑Body involvement |
|--------------|---------------------|----------------------------|
| **Class IIa** | Art. 52(6): **Annex IX** – QMS (ISO 13485:2016) + technical‑documentation assessment of a representative device (no Annex XI required). | Yes – NB review of QMS and TD. |
| **Class IIb** | Art. 52(4): either <br>• **Annex IX** (QMS) + technical‑documentation assessment of one representative device per generic group, *or*<br>• **Annex X** (type‑examination) together with **Annex XI** (production conformity verification). | Yes – NB required for either route. |
| **Class III** | Art. 52(3): either <br>• **Annex IX** (full technical‑documentation assessment), *or*<br>• **Annex X** + **Annex XI**. | Yes – NB mandatory. |

**Key citations:** Art. 52 paragraphs, Annex IX, X, XI (MDR 2017/745).

---

### 4. Evidence Package Required for the Technical Documentation (Annex II §6.1)

| Evidence element | Content requirement | Class‑specific depth |
|------------------|---------------------|----------------------|
| **Device description & intended use** | Full functional specification, user roles, workflow diagram, decision‑impact analysis (justification of class). | Required for all classes; critical for classification justification. |
| **Risk Management File (RMF)** | ISO 14971:2019‑based process – risk analysis, evaluation, control measures, residual‑risk acceptability, verification of controls. Map to GSPR §§3‑9 (Annex I). | Full RMF mandatory for all classes; higher‑class devices need more extensive validation of high‑severity risks. |
| **Software Lifecycle Documentation** | IEC 62304:2006+A1:2015 – development plan, architecture, verification & validation reports, configuration management, change control. | Mandatory for all software devices (class I‑III). |
| **Usability Engineering** | IEC 62366‑1:2015+A1:2020 – user‑interface risk analysis, formative and summative usability testing, validation of use errors. | Required for all classes; higher class demands more extensive summative testing. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – systematic literature review, clinical benefit‑risk assessment, justification of equivalence or supplemental clinical data. | Class IIa: CER sufficient if supported by reasonable equivalent devices. <br>Class IIb/III: More robust clinical data or a dedicated clinical investigation may be required. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B – objectives, methodology, timelines, data collection, analysis plan; final PMCF report. | Class IIa: Minimum PMCF to confirm continued safety/ performance.<br>Class IIb/III: Detailed PMCF, often prospective studies, feeding into PSUR (Art. 86). |
| **Post‑Market Surveillance (PMS) System** | Art. 83 – systematic plan; Art. 84 – PMS Plan; Art. 85/86 – periodic safety update reports (PSUR) for Class IIa/IIb/III. | PSUR required annually for Class IIb/III, biennially for Class IIa (Art. 86(2)). |
| **Summary of Safety and Clinical Performance (SSCP)** | Art. 32 – only mandatory for Class III implantable devices; not required for a GUI unless the software is classified as an implantable medical device (unlikely). | Not applicable unless later re‑classified to Class III implantable. |
| **Labeling & IFU** | Annex I §23 – content of label, symbols, instructions for use, electronic IFU if applicable; ensure user‑training requirements are clear. | Required for all classes. |
| **Declaration of Conformity (DoC)** | Art. 19 – signed by manufacturer, includes device identification, classification, conformity assessment route, reference to standards, etc. | Required for all classes. |

---

### 5. Gaps / Missing Information (to be supplied before NB submission)

1. **Detailed intended‑use statement** – explicit description of the clinical decision(s) supported and whether they can lead to serious deterioration or death.
2. **Decision‑impact analysis** – quantitative/qualitative justification for selecting Class IIa, IIb, or III (risk matrix, severity & probability).  
3. **Clinical data source list** – bibliography of literature supporting safety/effectiveness; if no adequate equivalents exist, a clinical investigation protocol is needed.
4. **Software architecture diagram** – showing separation of safety‑critical functions vs. non‑critical UI components.
5. **Usability test reports** – especially for “lay‑person” use (if any) and for detection of use errors that could affect diagnosis.
6. **Cybersecurity assessment** – per IEC 62304 & MDR GSPR §16 (if software connects to networked imaging equipment).
7. **Verification of interoperability** with DICOM modalities – evidence that data displayed are accurate and unaltered.
8. **Post‑market surveillance plan** aligned with the transition deadlines in Table 2 of the source (see below).  

---

### 6. Risk Controls (aligned with GSPR §3–§9, Annex I)

| Hazard | Control(s) | Evidence |
|--------|------------|----------|
| Incorrect image display (e.g., wrong patient ID) | Dual verification of DICOM header, mandatory barcode scan before load; audit trail logging. | Verification test report (IEC 62304). |
| Software‑induced misinterpretation (e.g., auto‑contrast leading to diagnostic error) | Disable automatic image processing for diagnostic view; user must manually approve any algorithmic changes. | Usability validation & risk analysis. |
| Cybersecurity breach / unauthorized access | Role‑based authentication, encrypted communication (TLS), regular vulnerability scans. | Security assessment report (ISO 14971 residual‑risk justification). |
| User error (incorrect parameter entry) | Input constraints, contextual help, “confirm” dialogs for critical settings. | IEC 62366‑1 usability test results. |
| System crash / loss of data during examination | Redundant storage, automatic session backup every 5 s, graceful shutdown routine. | Software verification & validation records. |

---

### 7. Relevant Timeline (from source excerpt)

| Class | Deadline for conformity under the “차등 시한” schedule |
|-------|----------------------------------------------------------|
| **Class III – custom‑made implantable** | 2026‑05‑26 |
| **Class III / Class IIb – implantable (excluding sutures, screws)** | 2027‑12‑31 |
| **Class IIb – non‑implantable**, **Class IIa**, **Is/Im** | **2028‑12‑31**【2】 |

*Implication:* If the software is ultimately classified as Class IIb (or higher), the manufacturer must have a full conformity assessment in place before 31 Dec 2028. Early engagement with an NB is advisable to avoid time pressure.

---

### 8. Human‑Escalation Triggers

| Trigger | Action required |
|---------|------------------|
| **Unclear decision impact** – unable to justify class (IIa vs IIb/III) | Pause dossier preparation; request detailed clinical scenario and severity analysis from product team. |
| **Absence of sufficient equivalent clinical data** – literature search yields no device with comparable intended use or risk profile | Initiate a prospective clinical investigation (Art. 61 MDR) before proceeding to NB audit. |
| **Missing cybersecurity evidence** – no threat‑model or mitigation plan | Engage IT‑security specialist; produce ISO/IEC 27001‑aligned assessment. |
| **Approaching deadline without complete TD** (e.g., <12 months to the Class IIb/III cutoff) | Escalate to senior RA manager and schedule urgent NB pre‑assessment meeting. |
| **NB feedback indicating insufficient RMF for high‑severity risk** | Conduct additional verification & validation cycles; update RMF with residual‑risk acceptance evidence. |
| **Regulatory change notice (e.g., new MDR amendment) after 2026‑11‑04** | Review impact on classification or PMS obligations; update documentation accordingly. |

---

### 9. Summary Judgment

- **Provisional classification:** **Class IIa**, pending a formal decision‑impact analysis.  
- **Conformity route:** **Art. 52(6) – Annex IX** (QMS + technical‑documentation assessment).  
- **Key evidence needed:** detailed intended‑use description, risk‑management file, software lifecycle documentation (IEC 62304), usability validation (IEC 62366‑1), clinical evaluation report (Annex XIV Part A), PMCF plan/report (Annex XIV Part B), PMS system (Art. 83‑86).  
- **Critical gaps:** justification of class, clinical equivalence data, cybersecurity assessment, usability test reports.  

If any of the escalation triggers materialize, the dossier must be paused and supplemented before NB submission, especially given the 2028‑12‑31 deadline for Class IIb/III devices.

---

### 10. Peer Review Prompt

> **Colleague, please evaluate**:  
> - The adequacy of our classification justification based solely on Rule 11 as quoted.  
> - Whether the listed evidence aligns with the latest MDR expectations for a software device of this class (including any recent MDCG guidance).  
> - Any jurisdiction‑specific nuances we may have missed (e.g., EUDAMED registration obligations under Art 33‑39, or upcoming amendments to Annex IX).  

Your feedback will be incorporated before finalizing the Technical Documentation package.

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

> "PSUR annually for Class IIb/III, biennially for Class IIa (Art. 86(2))" — IIb는 2년(III·이식형만 연간).

**Source Excerpts**

1. Chunk `1007248354989010815`

> ### 2.3 Rule 11 (SW) > Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as class IIa. > 단, decision may cause (a) death or irreversible deterioration → **Class III**; (b) serious deterioration or surgical intervention → **Class IIb**. > Software intended to monitor physiological processes: 일반 IIa / immediate danger IIb. > Others: Class I. **→ 촬영실 GUI SW = Rule 11 적용, 영향도에 따라 IIa ~ III**

2. Chunk `1007987960287657537`

> ### 7.1 차등 시한 | Class | 시한 | |---|---| | Class III **custom-made** implantable | 2026-05-26 | | Class III / Class IIb **implantable** (sutures·screws 등 제외) | **2027-12-31** | | Class IIb **non-implantable** / IIa / Is / Im | **2028-12-31** |

### kb-eval-20261104-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "87349dc9039b7d94", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md", "source_hash": "9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `87349dc9039b7d94`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_DoC_%EC%96%91%EC%8B%9D_%EC%9E%91%EC%84%B1%EC%A7%80%EC%B9%A8.md)
- Source hash: `9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_DoC_양식_작성지침.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` --- ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ─────────────────────────...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – EU MDR (Regulation (EU) 2017/745) – Classification & Conformity‑Assessment Planning**

---

### 1. Device Identification (as required in the EU Declaration of Conformity – Annex IV)

| Item | Current status (from source) | Gap / Action needed |
|------|------------------------------|---------------------|
| **Manufacturer name** | Placeholder “[회사명]” | Insert legal company name as it appears on the trade register. |
| **SRN (EUDAMED Single Registration Number)** | “[EUDAMED SRN — 미취득 시 공백]” | Register in EUDAMED and record the issued SRN. |
| **Authorised Representative** | Placeholder “[EU 대리인명 및 주소 — 역외 제조사 해당 시]” | Provide name, address and contact details of the EU‑based authorised representative (if manufacturer is outside the EU). |
| **Basic UDI‑DI** | “[Basic UDI‑DI — Annex VI Part C 기준]” | Allocate a Basic UDI‑DI from an approved issuing agency; record in the DoC. |
| **Product name / Trade name** | Place‑holders “[제품명]”, “[상품명]” | Insert commercial name(s) as used on the market label. |
| **Model / Catalogue number** | Placeholder “[모델 번호 / 카탈로그 번호]” | List every distinct model that will be placed on the EU market. |
| **Intended use (purpose)** | Placeholder “[의도된 사용 목적 — 간략 기재]” | Provide a concise, complete description of the intended medical purpose together with any contraindications, target patient group and clinical indications. |
| **Date & Signature** | Template fields only | Completed by an authorised individual (e.g., CEO, QA Director) once all documentation is finalised. |

> **Citation:** EU Declaration of Conformity – Regulation (EU) 2017/745 Annex IV (framework reference).

---

### 2. Preliminary Classification & Conformity‑Assessment Route  

| Step | Required information | Decision criteria | Current status / gap |
|------|---------------------|-------------------|----------------------|
| **2.1 Determine device class** | • Intended use<br>• Invasiveness, measuring function, sterile/reusable surgical instrument status<br>• Energy source (active therapeutic/diagnostic) | Apply the rules of Annex VIII (e.g., Rule 9, Rule 10, Rule 11, Rule 17). | No intended‑use description supplied → **classification cannot be assigned**. |
| **2.2 Select conformity‑assessment route** | Class result from 2.1 | *Art. 52(7)* – Class I ⇒ self‑declaration (no NB)<br>*Art. 52(6)* – Class IIa ⇒ Annex IX (QMS + technical‑doc) **or** Annex II/III + Annex XI §10/§18<br>*Art. 52(4)* – Class IIb ⇒ Annex IX or Annex X + XI<br>*Art. 52(3)* – Class III ⇒ Annex IX or Annex X + XI | Route cannot be defined until class is known. |
| **2.3 Notified Body involvement** | • Class of device<br>• Whether sterile, measuring or reusable surgical instrument (Is/Im/Ir) | NB required for all classes except non‑sterile Class I (see *Art. 52*). | Undetermined – pending classification. |

> **Citation:** Classification rules – Annex VIII; conformity‑assessment routes – Art. 52(3‑7) together with Annex IX, Annex X and Annex XI (framework references).

---

### 3. Required Evidence Package (per MDR)

| Evidence | Regulatory reference | What must be supplied | Current status |
|----------|----------------------|-----------------------|----------------|
| **Technical Documentation** (TD) – Sections 1‑6 of Annex II | Annex II §1‑6 | • Device description & specification<br>• Design/Manufacturing information<br>• General Safety & Performance Requirements (GSPR) compliance (Annex I)<br>• Benefit–risk analysis & risk management file (RMF) (§3‑8, Annex I)<br>• Verification & validation data<br>• Clinical evaluation (CER) & PMCF data (Annex XIV Part A/B) | Only DoC template present; all TD elements missing. |
| **Risk Management File** (ISO 14971:2019) | ISO 14971 (2019 edition) – referenced in MDR §10(9) and Annex I §3‑8 | • Hazard identification<br>• Risk analysis & evaluation<br>• Risk control measures<br>• Evaluation of residual risk vs benefit | No RMF provided. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | Systematic review of state‑of‑the‑art literature, clinical data, and/or a clinical investigation report. | Not supplied – “no specific identifier found in source — verify separately”. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | • Description of routine PMS activities, data collection methods, etc. | Not supplied. |
| **Periodic Safety Update Report (PSUR)** (for Class IIa/IIb/III) | Art. 86 | • Benefit–risk conclusions, PMCF results, sales volume & user population. | Not applicable until classification known; PSUR not yet drafted. |
| **PMS System** (overall) | Art. 83 | • Organizational structure, procedures for PMS data handling, trend analysis, corrective actions. | Not supplied. |
| **Usability Engineering File** (if software or UI is involved) | IEC 62366‑1:2020 (cited by Annex I §17) | Human factors testing, risk control for use errors. | No information. |
| **IEC standards specific to device type** (e.g., IEC 60601‑2‑54 for X‑ray equipment) | Device‑specific standard list (see “IEC standards in the X‑ray domain” table). | Declaration of conformity with applicable IEC safety standards. | Not identified – need to establish which, if any, apply. |
| **Labeling & IFU** | Annex I §23 | Final labeling, symbols, instructions for use consistent with GSPR. | Only placeholders in DoC template; full labeling missing. |

> **Citation:** Evidence requirements – Annex II (TD), Annex XIV Part A/B (CER/PMCF), Art. 83‑86 (PMS/PSUR), IEC 62366‑1, IEC 60601‑2‑54 etc. (framework references).

---

### 4. Identified Gaps & Immediate Actions  

| Gap | Impact on CE‑marking timeline | Action |
|-----|------------------------------|--------|
| **Intended use / clinical purpose** not defined | Prevents classification and clinical evaluation scope definition. | Obtain a concise intended‑use statement from product development/marketing. |
| **Classification rule selection** (Annex VIII) | Unknown route → cannot engage Notified Body. | Apply the appropriate rule(s) once intended use is known; document justification. |
| **SRN & EUDAMED registration** | Mandatory for DoC, UDI‑DI, and market entry. | Register manufacturer and device in EUDAMED; obtain SRN and Basic UDI‑DI. |
| **Risk Management File (ISO 14971)** | GSPR compliance cannot be demonstrated without RMF. | Conduct risk analysis, implement controls, compile RMF. |
| **Clinical Evaluation Report** | Required for all classes; missing data triggers NB request for additional evidence. | Perform literature search and/or clinical investigation; draft CER per Annex XIV Part A. |
| **PMS system & plan (Art. 83‑84)** | Needed for ongoing compliance; absence blocks DoC finalisation. | Develop PMS procedures, define data sources, set up trend analysis. |
| **Technical Documentation – full content** | Incomplete TD leads to NB non‑conformity findings. | Populate all Annex II sections with design files, specifications, verification/validation reports, GSPR matrix, labeling, etc. |
| **Authorized Representative details (if applicable)** | Missing for manufacturers located outside the EU → illegal market placement. | Appoint and document an EU authorising representative. |
| **Usability / Human‑Factors Evidence** (if device includes software/UI) | Required by Annex I §17; lack may cause NB to request additional testing. | Conduct usability engineering activities per IEC 62366‑1. |
| **IEC safety standard conformity** (device‑specific) | Mandatory for most medical devices; missing leads to non‑compliance with GSPR. | Identify applicable IEC standards, perform compliance testing, retain certificates. |

---

### 5. Draft Risk Controls Overview (to be expanded in the RMF)

1. **Hazard Identification** – catalogue all foreseeable hazards linked to intended use, including biological, electrical, mechanical and software‑related risks.
2. **Risk Evaluation** – apply ISO 14971 risk matrix; determine acceptability criteria per Annex I §8 (benefit–risk).  
3. **Risk Control Measures** –  
   - Design safeguards (e.g., redundant safety circuits, interlocks).  
   - Protective labeling and IFU warnings (Annex I §23).  
   - Usability‑driven controls to minimise use errors (IEC 62366‑1).  
4. **Residual Risk Assessment** – verify that remaining risks are outweighed by the clinical benefits (Annex I §8).  
5. **Verification of Controls** – testing reports, validation protocols, and post‑market data (PMCF) will demonstrate effectiveness.

> **Citation:** General Safety & Performance Requirements – Annex I §§3‑9 (risk management), §23 (labeling); ISO 14971:2019 for risk‑management methodology.

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason | Escalation recipient |
|--------|--------|-----------------------|
| **No intended‑use statement received within 5 working days** | Classification and clinical evaluation cannot start. | Project Lead / Regulatory Manager. |
| **EUDAMED SRN not allocated after 10 working days of registration request** | DoC cannot be completed; market entry blocked. | Compliance Officer & Legal Counsel. |
| **Risk Management File draft overdue (>2 weeks past schedule)** | GSPR compliance risk; NB will reject TD. | Quality‑Assurance Manager. |
| **Clinical evidence gap identified (e.g., missing clinical investigation data) after the first CER draft** | Potential NB request for additional data, delaying timeline. | Clinical Affairs Lead. |
| **PMS plan not approved before final DoC signing** | Art. 84 non‑compliance; post‑market obligations unmet. | Post‑Market Surveillance Coordinator. |
| **Authorized Representative not appointed when manufacturer is outside EU** | Legal requirement for market access under MDR. | Business Development / Legal Team. |

When any of these triggers fire, the responsible party must raise a **Regulatory Issue Record (RIR)** in the project tracking system and request an urgent review meeting with the RA team.

---

### 7. Peer‑Review Prompt  

> *"Colleague, please examine this draft and challenge:*
> - *Are there any MDR provisions or Annexes that I have omitted for a device of unknown class?*  
> - *Does the evidence checklist align fully with current MDCG guidance on clinical evaluation and PMCF for all classes?*  
> - *Have I correctly distinguished between framework citations (Annex/Article numbers) and instance identifiers, given the source material provided?"  

Your feedback will help close any jurisdiction‑specific gaps before we engage a Notified Body.

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

>

**Source Excerpts**

1. Chunk `1085205256397640486`

> 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` ---

2. Chunk `1141859994065237405`

> ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ───────────────────────────────────────────── 1. MANUFACTURER Company name : [회사명] SRN : [EUDAMED SRN — 미취득 시 공백] Address : [등록 사업장 주소] Authorised Representative: [EU 대리인명 및 주소 — 역외 제조사 해당 시] 2. SOLE RESPONSIBILITY STATEMENT This EU Declaration of Conformity is issued under the sole responsibility of the manufacturer named above. 3. BASIC UDI-DI [Basic UDI-DI — Annex VI Part C 기준] 4. PRODUCT IDENTIFICATION Product name : [제품명] Trade name : [상품명] Model / Cat.# : [모델 번호 / 카탈로그 번호] Intended use : [의도된 사용 목적 — 간략 기재] Photograph : [첨부...

### kb-eval-20261104-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "22655a9b46828906", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `22655a9b46828906`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Strategy  
(derived from source [1]–[2])**

---

### 1. Device Synopsis (as inferred from the source)

| Item | Detail (source‑based) |
|------|-----------------------|
| **Intended use** | “Standard diagnostic radiology” – a medical device that emits ionising radiation for patient imaging. |
| **Key performance claim** | Detector quantum efficiency (DQE) ≥ 65 % (Test Report **TR‑2024‑015**, IEC 62220‑1‑1). |
| **Clinical evidence supplied** | Revised Clinical Evaluation Report (CER Rev. 3) attached as Annex A (source [1]). |

*The source does not disclose the full device description, accessories, or software scope; these must be added to the technical documentation.*

---

### 2. Classification & Applicable Rules

| Aspect | Determination |
|--------|---------------|
| **MDR rule** | The device *generates* ionising radiation for diagnostic purposes → **Rule 10 (active devices for diagnosis and monitoring)** of Annex VIII. |
| **Resulting class** | Rule 10 places the device in **Class IIb** (when radiation is emitted) per MDR classification rules. |
| **Citation** | *Annex VIII, Rule 10*; *Class IIb* as defined by the rule. |

> **Note:** Sub‑components that only detect X‑ray images (e.g., a detector panel) may fall under **Rule 17** → **Class IIa**, but the overall system is governed by the highest class of any constituent part (the radiation source).

---

### 3. Conformity‑Assessment Route  

| Class | MDR route (Art. 52) | NB involvement | Required Annexes |
|-------|--------------------|----------------|------------------|
| **IIb** | **Art. 52(4)** – either <br>• **Annex IX** (full QMS + technical‑documentation assessment of a representative device), **or**<br>• **Annex X** (EU type‑examination) together with **Annex XI** (production conformity verification). | Yes – the Notified Body must audit the QMS and assess the TD/type. | Annex IX (or X + XI); Annex II & III for technical documentation; Annex IV for EU Declaration of Conformity. |

> *Citation*: **Art. 52(4) MDR 2017/745**.

---

### 4. Evidence Package Required for the NB

| Evidence | Content Requirement | Reg. / Standard Reference |
|----------|--------------------|---------------------------|
| **Technical Documentation (TD)** | Complete description, labeling, design‑manufacturing info, GSPR fulfilment (Annex II §§1‑6). | *Annex II MDR* |
| **EU Declaration of Conformity** | Manufacturer name, device identification, conformity route, reference to applicable standards. | **Art. 19**; content in *Annex IV*. |
| **Clinical Evaluation Report (CER)** | State of the art, clinical data, benefit‑risk analysis. Must be kept current under **Art. 61** and structured per *Annex XIV Part A*. | *Annex XIV Part A*; **Art. 61** |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Planned clinical data collection, methodology, evaluation of ongoing safety/performance. Structured per *Annex XIV Part B*. | *Annex XIV Part B* |
| **Risk Management File (RMF)** | Hazard identification, risk analysis, control measures, residual‑risk evaluation – ISO 14971:2019 compliant. Must address ionising‑radiation specific hazards (Annex I §16) and active‑device hazards (Annex I §18). | *Annex I §§3‑9*; **ISO 14971:2019** |
| **Usability Engineering File** | Human factors assessment per IEC 62366‑1. | **IEC 62366‑1:2020** |
| **Electrical Safety & Performance Test Reports** | Compliance with IEC 60601‑2‑54 (radiography) and IEC 60601‑2‑28 (X‑ray tube assemblies). | **IEC 60601‑2‑54**, **IEC 60601‑2‑28** |
| **Radiation Output & Image Quality Tests** | DQE ≥ 65 % – test report **TR‑2024‑015** (IEC 62220‑1‑1). | *Source [1]*; **IEC 62220‑1‑1** |
| **Post‑Market Surveillance (PMS) Plan & Periodic Safety Update Report (PSUR)** (for Class IIb) | PMS system (Art. 83), plan (Art. 84), PSUR (Art. 86 – annual). | **Art. 83‑86** |

---

### 5. Gaps / Missing Information Identified from the Source

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Full device description & intended user population** | Needed for Annex II §1 and to define clinical endpoints. | Provide detailed IFU, labeling, and intended‑use statement. |
| **Comprehensive clinical data beyond DQE equivalence** | CER must address safety, efficacy, and real‑world performance (e.g., image quality, dose metrics, adverse events). | Conduct or reference a clinical investigation / literature review per *Annex XIV Part A*. |
| **PMS plan & PSUR** | Mandatory for Class IIb (Art. 84‑86) – absent from source. | Draft PMS plan, schedule annual PSURs. |
| **Risk Management File** | No RMF cited; required to demonstrate compliance with Annex I §3‑9 and ISO 14971. | Compile hazard analysis, risk controls, residual‑risk evaluation. |
| **Usability / Human factors evidence** | IEC 62366‑1 compliance not shown. | Perform usability testing, create engineering file. |
| **Declaration of Conformity (DoC) draft** | Required to accompany submission; no mention in source. | Prepare DoC per *Annex IV* and Art. 19. |
| **Evidence of conformity with IEC 60601‑2‑54 / ‑28** | Electrical safety & performance standards not referenced. | Supply test reports or certificates of compliance. |
| **Clear mapping of each component to its classification rule** | NB will request justification for the overall class (Rule 10) and any lower‑class sub‑assemblies. | Provide a classification matrix linking components to Rule 10, Rule 17, etc. |

---

### 6. Risk Controls (Illustrative – to be detailed in RMF)

| Hazard | Control(s) | Regulatory basis |
|--------|------------|-------------------|
| **Ionising radiation exposure** | Shielding design, dose‑monitoring software, interlocks, compliance with IEC 60601‑2‑54 and Annex I §16. | *Annex I §16* |
| **Electrical shock / fire** | Built‑in protection (IEC 60601‑1), conformal coating, leakage current limits. | *Annex I §§3‑4* |
| **Software malfunction affecting image processing** | IEC 62304 lifecycle, IEC 62366‑1 usability validation, fail‑safe mode. | *Annex I §17*, **IEC 62304**, **IEC 62366‑1** |
| **Incorrect device set‑up by lay users** | Clear labeling (Annex I §23), training instructions, ergonomic design. | *Annex I §§22‑23* |
| **Residual risk after mitigations** | Benefit‑risk analysis documented in CER; periodic review via PMCF. | *Annex XIV Part A*, **Art. 61** |

---

### 7. Summary Judgment & Human‑Escalation Triggers

1. **Classification:** The system is a **Class IIb** medical device under **Rule 10 (active diagnostic)** – therefore the conformity‑assessment route must follow **Art. 52(4)** (Annex IX **or** Annex X + XI) with NB involvement.

2. **Submission readiness:** Current evidence covers only a limited performance metric (DQE ≥ 65 %) and a CER revision; substantial additional documentation is required to satisfy MDR technical‑documentation, clinical‑evaluation, risk‑management, PMS, and standards conformity obligations.

3. **Escalation triggers**  
   - **NB request for additional clinical data** → Escalate immediately to Clinical Development Lead (within 2 working days).  
   - **Identification of missing or incomplete RMF items** → Notify Product Development Manager; initiate risk‑analysis workshop (target completion < 10 working days).  
   - **PMS plan absent** → Trigger Regulatory Project Lead to draft PMS documentation (deadline: before NB audit start).  
   - **If the NB chooses Annex X route**, a type‑examination certificate will be required – trigger Coordination with External Testing Lab (within 5 working days of NB decision).

---

### 8. Peer‑Review Prompt

> *Colleague, please review the assumptions made regarding the device’s classification and the completeness of the evidence matrix above. Specifically:  
> • Are there any additional MDR annexes or articles that should be cited for the identified gaps?  
> • Does the proposed risk‑control mapping adequately address all Annex I requirements for ionising‑radiation devices?  
> • Have we missed any EU‑specific post‑market surveillance obligations for a Class IIb radiology system?*  

--- 

*All citations are drawn directly from the MDR framework (Annex/Article numbers) or from the source excerpts provided. No invented identifiers have been introduced.*

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

> IIb 맥락 "PSUR (Art. 86 – annual)" — IIb는 2년.

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1107467848736309543`

> ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통지하는 문서. 국내 MFDS "보완 요청", FDA "Additional Information (AI) Request"에 해당하는 EU MDR 용어. ---

## ra_kr

### kb-eval-20261104-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "6d3fbc04630f1cc9", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `6d3fbc04630f1cc9`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital‑Medical‑Device GUI Software (P3 촬영실)**  

---

### 1. Classification & Submission Route  
| Item | Assessment | Basis / Citation |
|------|------------|------------------|
| **Device type** | “디지털의료제품소프트웨어” (software that supports X‑ray imaging workflow). | Excerpt [2] – *P3 촬영실 GUI SW* is listed under the digital‑medical‑device category. |
| **Regulatory grade** | Likely **2등급**, but the exact grade is not stated in the source and must be confirmed against the 《디지털의료제품법 시행규칙》 (2026‑01‑23 개정). | Excerpt [2] – *“GUI SW가 2등급이든 등급 미지정이든 …”* indicates uncertainty; a lookup of the rule’s device‑grade table is required. |
| **Submission track** | If confirmed as **2등급**, the route is **인증** (technical‑documentation review by an MFDS‑designated 심사기관). | MFDS_인허가_상세가이드.md §2 (등급 및 인허가 경로) – standard Korean pathway for 2등급 devices. |
| **Possible exemption / alternative path** | Under **제25조 각 호** of the digital‑medical‑device rule, certain clinical‑data requirements can be waived if conditions are met (e.g., low risk, no AI function). | Excerpt [2] – *“개정 제25조 각 호 … 면제·대체 경로가 열린다”*; direct reference to the clause. |

> **Citation note:** No specific 고시/notice number is supplied in the excerpts for the rule amendment (2026‑01‑23); therefore, “no specific identifier found in source — verify separately” is added for that item.

---

### 2. Required Evidence Package  

| Category | Documents / Data | Rationale |
|----------|------------------|-----------|
| **Quality Management** | KGMP certification dossier; ISO 13485:2016‑based QMS records. | Korean law mandates KGMP for all medical‑device manufacturers (의료기기법 제28조). |
| **Risk Management** | Risk Management Plan & Report per **ISO 14971:2019**. | Standard requirement for all device classes; risk controls must be demonstrated before market entry. |
| **Software Lifecycle** | • IEC 62304 (2006+A1:2015) software development plan, verification/validation reports.<br>• IEC 62366‑1 (2015+A1:2020) usability engineering file.<br>• Cybersecurity measures per MFDS 사이버보안 가이드라인 (referencing **IEC 81001‑5‑1 2021**). | Required for digital‑medical‑device software; cybersecurity is explicitly mandated for AI‑enabled or networked devices. |
| **Clinical Evaluation** | • If the GUI remains a *decision‑support* tool without autonomous AI, clinical data may be waived under **제25조 각 호** (subject to verification).<br>• If an AI module will be added, a **comparative clinical study** must follow the 2025‑10‑31 AI guideline (comparison vs clinician‑only diagnosis, analytical accuracy, effect‑size demonstration). | The new AI guideline (2025‑10‑31) imposes comparative design when AI assistance is used. |
| **Labeling & IFU** | Korean‑language labeling, instructions for use, and a summary of safety information in Hangul. | MFDS labeling rule requires all user‑facing documents to be provided in Korean. |
| **Post‑Market Surveillance (PMS)** | PMS plan consistent with KGMP and MFMF guidelines; adverse event reporting procedure. | Required for 2등급 devices to monitor real‑world performance. |

**Framework references** (ISO/IEC standards) are stated as facts and carry no “verify” caveat per the citation rule.

---

### 3. Missing / Unverified Information  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact device grade (1‑4등급)** | Determines submission track and extent of clinical evidence required. | Query the latest 《디지털의료제품법 시행규칙》 (2026‑01‑23 개정) or MFDS product‑grade database; record the official grade. |
| **Applicability of 제25조 면제** – which specific clause(s) can be invoked for this GUI software? | Determines whether clinical trial data are needed. | Review each sub‑paragraph of **제25조** to confirm criteria (e.g., risk level, AI presence). |
| **Planned AI functionality** – timeline and scope of any future AI module. | If AI is added later, a comparative clinical study will become mandatory per the 2025‑10‑31 guideline. | Obtain product roadmap; if AI integration is planned before market launch, prepare study design now. |
> **Citation note:** The source flags the need to “verify” clause migration from 고시 → 시행규칙; no definitive identifier is provided – “no specific identifier found in source — verify separately.”  

---

### 4. Key Risk Controls (to be documented)  

1. **Hazard Identification & Mitigation** – per ISO 14971, address software‑related hazards (e.g., incorrect image display, data loss).  
2. **Cybersecurity** – network isolation, authentication, encryption; align with IEC 81001‑5‑1 2021 and MFDS cyber‑security guidance.  
3. **Usability Engineering** – conduct user‑interface testing per IEC 62366‑1 to prevent use errors.  
4. **Software Validation** – unit, integration, system tests; traceability matrix linking requirements → verification.  
5. **Quality Assurance** – KGMP‑based QMS audits; periodic internal audits of design controls.  

---

### 5. Human‑Escalation Triggers  

| Trigger | Escalation Level | Reason |
|--------|-------------------|--------|
| **Unresolved grade determination after rule review** | RA lead → Legal / MFDS liaison | Classification directly impacts submission pathway. |
| **Inability to satisfy any sub‑clause of 제25조 for clinical data waiver** | Project manager & Clinical Lead | May require full comparative trial, affecting timeline and budget. |
| **Planned AI module confirmed before market launch** | Clinical Development team + RA lead | Necessitates design of a comparative study per 2025‑10‑31 AI guideline; risk of non‑compliance if omitted. |
| **High‑severity hazard uncovered in risk analysis (e.g., misinterpretation of image leading to diagnostic error)** | Safety Officer → MFDS (mandatory reporting) | Must trigger immediate corrective actions and possibly pre‑market safety review. |
| **KGMP certification not achieved within planned schedule** | Manufacturing QMS lead → Executive sponsor | Certification is a prerequisite for any 2등급 submission. |

---

### 6. Peer‑Review Prompt  

*“Please challenge the following assumptions: (1) that the P3 GUI software qualifies as 2등급 without detailed grade verification; (2) that the clinical‑data waiver under 제25조 can be applied based solely on current non‑AI functionality; and (3) that existing KGMP/ISO 13485 compliance suffices for the cybersecurity requirements defined in MFDS 사이버보안 가이드라인. Identify any gaps in source coverage or jurisdiction‑specific obligations that may have been overlooked.”*  

--- 

**End of draft – judgment pending verification of device grade, exemption clause applicability, and future AI plans.**

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

1. Chunk `1127968925422991528`

> ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향후 AI 모듈 추가 가능성 고려해 비교설계 원칙 사전 학습 권고. - 출처: 정책브리핑 2025-10-31(https://www.korea.kr/briefing/pressReleaseView.do?newsId=156724315) ---

2. Chunk `198902914416608487`

> - 영향 제품: **P3 촬영실 GUI SW**(디지털의료기기소프트웨어에 해당하는 경우). P1 X-ray Detector·P2 Handheld X-ray Source는 의료기기법 체계 적용으로 **직접 영향 없음**(§3·§4 매트릭스 유지). - 나항은 자사에 **유리한 완화**다. GUI SW가 2등급이든 등급 미지정이든 기능별 임상시험 자료의 **면제·대체 경로가 열린다**. 다만 면제·대체의 개별 요건(개정 제25조 각 호)은 조문 전문 확인이 필요하다 — `[검증 필요]`. - 가항은 요건의 삭제가 아니라 **근거 조문의 이동(고시 → 시행규칙)** 이다. 「디지털의료제품법 시행규칙」(2026-01-23 개정)의 해당 조문을 확인해야 실제 의무 범위를 알 수 있다 — `[검증 필요]`. - 다항의 우수관리체계 특례는 **QMS 성숙도를 인허가 편익으로 전환**하는 제도다. KGMP·ISO 13485 기반이 갖춰진 경우 중장기 활용 가치가 있다. **행동 (Action)**

### kb-eval-20261104-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "de68ceabac55bf94", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `de68ceabac55bf94`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98_%EA%B8%B0%EC%A4%80/%EC%A0%9C%ED%92%88%EB%B3%84_%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98.md)
- Source hash: `a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `제품별_등급분류.md`는 `제품별_등급분류.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정 ###...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Assessment Draft – Software‑Based Medical Device (2등급)**  

---

### 1. Korean Classification & Submission Route  
| Item | Determination | Source |
|------|---------------|--------|
| **MFDS Grade** | **2등급** – may be upgraded to a higher grade if the device provides “보조 기능 수준” that warrants it. | Excerpt [2] |
| **Regulatory Pathway** | **인증** (technical‑documentation review by an MFDS‑designated 심사기관). 2등급 devices are not submitted via 허가 unless a specific exemption applies. | Korean regulation (MFDS_인허가_상세가이드.md §2) – framework reference |
| **Relevant Guidance** | *“디지털의료기기소프트웨어 허가·심사 가이드라인”* and the *디지털의료제품법* (effective 2025‑01‑24). | Excerpt [2] |

> **Citation note:** No specific 고시/notice number is given in the source for the above guidelines; verify the exact 고시 번호 separately before final submission.

---

### 2. Required Evidence Package  

| Requirement | Expected Documentation / Data | Comments / Gaps |
|-------------|------------------------------|-----------------|
| **Device Specification & Intended Use** | Detailed specification (전압, 전류, 용도, 적용부위, SW 역할) and a clear intended‑use statement in Korean. | Not yet collected – see “제품 전략·사양 확정” To‑Do list. |
| **MFDS 품목코드 (A‑code)** | Assigned A‑code from MFDS product code database. | Pending – listed as a To‑Do item. |
| **Technical Documentation** (Korean) | • Device description, labeling & IFU in Korean  <br>• Software architecture diagram, verification & validation reports (IEC 62304:2006+A1:2015) <br>• Risk Management File (ISO 14971:2019) <br>• Usability Engineering (IEC 62366‑1:2015+A1:2020) | All must be in Korean; foreign language versions are supplemental only. |
| **KGMP Certification** | Certificate of compliance with KGMP (의료기기법 제28조) for any manufacturing/final assembly location. | Status unknown – required before 인증. |
| **Software Change Management** | Change‑control plan per 디지털의료제품법 (AI/ML update strategy, performance monitoring). | Needed if device incorporates AI or learns post‑market. |
| **Foreign Evidence (Optional)** | FDA predicate data (Product Classification Database) and/or EU MDR Rule 10/11 assessment as supporting evidence. MFDS may accept foreign non‑clinical GLP data under OECD MAD and clinical evaluation reports where a specific notice permits it. | No MFDS 고시 number cited; verify current acceptance scope before reliance on foreign data. |
| **Clinical Evidence** | Local clinical data or justified reliance on foreign clinical evaluation (if allowed by the latest MFDS notice). | Determine if local data are mandatory for 2등급 software; currently unclear – needs confirmation. |
| **Labeling & IFU** | Korean language labeling, product name, intended use, contraindications, warnings, and instructions for use (IFU) per MFDS labeling regulations. | None provided yet. |
| **Cybersecurity** | Compliance with MFDS 사이버보안 가이드라인 (referencing IEC 81001‑5‑1:2021). | Required if device connects to network or handles patient data. |

---

### 3. Missing Information – Action Items  

1. **Finalize detailed product specifications** (전압·전류·용도·적용부위·SW 역할) – complete the To‑Do checklist in Excerpt [1].  
2. **Secure MFDS 품목코드 (A‑code).**  
3. **Determine whether the software is “독립형” or an accessory** to decide applicability of the 독립형 SW 사용적합성 가이드라인 (referenced in Excerpt [2]).  
4. **Confirm KGMP certification status** for any manufacturing sites.  
5. **Clarify need for local clinical data** versus acceptable foreign clinical evaluation under current MFDS notice(s).  
6. **Prepare Korean language labeling & IFU drafts**.  
7. **Map FDA predicate and EU MDR Rule 10/11 analysis to Korean requirements**, documenting where foreign evidence will be relied upon.  

---

### 4. Core Risk Controls (per ISO 14971:2019)  

| Hazard | Control Measure | Verification |
|--------|-----------------|--------------|
| Software malfunction → incorrect therapy recommendation | • Robust software verification & validation (IEC 62304). <br>• Fail‑safe design with default safe mode. | Test reports, code reviews. |
| Data security breach → patient privacy loss | • Encryption of data at rest/in transit. <br>• Access control per IEC 81001‑5‑1. | Cybersecurity assessment report. |
| User error due to complex UI | • Usability engineering (IEC 62366‑1). <br>• Human factors validation with representative users in Korean language. | Usability test results, risk analysis updates. |
| AI/ML performance drift | • Continuous performance monitoring plan; periodic re‑validation. | Change‑management logs, post‑market surveillance data. |

All identified risks must be transferred to the **Risk Management File** and reflected in the **Technical Documentation** submitted for 인증.

---

### 5. Human‑Escalation Triggers  

| Trigger | When to Escalate to Senior RA / Regulatory Lead |
|--------|-----------------------------------------------|
| **Unresolved classification uncertainty** – evidence that device may qualify as 3등급 (e.g., additional therapeutic function). |
| **KGMP certification not obtained** before submission deadline. |
| **MFDS requests local clinical data** despite prior reliance plan on foreign evidence. |
| **Regulatory notice change** – new MFDS 고시 expanding or restricting acceptance of foreign data (requires re‑assessment). |
| **Significant AI/ML update** after market launch that alters intended use or risk profile. |
| **Failure to produce Korean labeling/IFU** within the review window. |

Escalation should be documented in the project risk register and communicated to the cross‑functional team promptly.

---

### 6. Peer Review Prompt  

*“@RA‑Peer, please challenge the following assumptions: (1) that the device can remain classified as 2등급 without further functional justification; (2) that reliance on FDA predicate data is permissible under current MFDS acceptance scope (no 고시 number cited); and (3) that the identified risk controls fully satisfy Korean regulatory expectations for independent software. Identify any jurisdiction‑specific gaps, especially regarding local clinical data requirements and KGMP certification coverage.”*

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

1. Chunk `1097646391221557778`

> ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정

2. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

### kb-eval-20261104-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "4a9c2ee8733ed487", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `4a9c2ee8733ed487`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%B8%ED%97%88%EA%B0%80_%EC%83%81%EC%84%B8%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_인허가_상세가이드.md`는 `MFDS_인허가_상세가이드.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수 ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – “촬영실 GUI SW” (2등급) – MFDS Classification & Licensing Pathway**

---

### 1. Device Overview  
| Item | Description |
|------|-------------|
| **Product name** | 촬영실 GUI SW (graphical user‑interface software for imaging‑room operation) |
| **Intended use** | Provides operators with control and visualization of radiographic equipment; may include AI‑based image quality optimisation. |
| **Risk category** | Determined by MFDS as **2등급** (see source excerpt [2]). |

---

### 2. Applicable Korean Regulatory Framework  

| Source type | Reference (framework) | Note on citation |
|-------------|-----------------------|------------------|
| Primary law | **의료기기법** (Medical Device Act) | No instrument number appears in the source – verify separate if a specific amendment is required. |
| Sub‑law | **시행령** (Presidential Decree) | — |
| Enforcement rule | **시행규칙** (Prime Ministerial Ordinance) | — |
| MFDS 고시 – grading | 「의료기기 품목 및 품목별 등급에 관한 규정」 | No specific 고시 번호 is given in the source – verify separately. |
| MFDS 고시 – approval/notification procedures | 「의료기기 허가·신고·심사 등에 관한 규정」 | — |
| MFDS 고시 – GMP assessment | 「의료기기 GMP 심사·평가 등에 관한 규정」 | — |

**International standards (framework references, no specific Korean instrument numbers required):**  

- IEC 62304 – Software life‑cycle processes (referenced in source [2]).  
- IEC 62366‑1 – Usability engineering.  
- ISO 14971:2019 – Medical device risk management (current edition per reference table).  
- ISO 13485:2016 – Quality‑management system (relevant for KGMP).  

---

### 3. Determination of Submission Route  

| Classification | Korean pathway | Typical review body |
|----------------|----------------|---------------------|
| **2등급** (software) | **인증** (certification) – technical‑documentation review by an MFDS‑designated 심사기관 (e.g., KTL, KTC). | MFDS‑designated certification agency. |

*The source also notes that a “디지털의료제품법 경로 병용 검토” may be applicable when the software is considered a digital health product; this should be assessed in parallel.*  

**Citation:** “경로: 인증 (또는 디지털의료제품법 경로 병용 검토)” – source [2].

---

### 4. Required Evidence Package (minimum)

| Evidence | Regulatory basis / standard | Comment |
|----------|----------------------------|---------|
| **Software development life‑cycle documentation** (plans, requirements, design, code, verification & validation) | IEC 62304 (life‑cycle), ISO 14971 (risk management) | Must show compliance with the IEC 62304 process model. |
| **Risk Management File** (hazard analysis, risk evaluation, risk control measures) | ISO 14971:2019 | Include risk acceptability justification for AI functions. |
| **Usability Engineering Report** (per IEC 62366‑1) | IEC 62366‑1 | Demonstrates user‑interface safety and error mitigation. |
| **Cybersecurity Plan & Assessment** (threat model, protection measures, vulnerability management) | MFDS 사이버보안 가이드라인 (referenced implicitly in source [2]) | Include encryption, authentication, audit logging. |
| **AI Governance Documentation** (if AI included) – algorithm description, training data provenance, performance validation, change‑management plan as per “생성형 AI 가이드라인” | 생성형 AI 가이드라인 (MFDS) | Source [2] states the need for these items when AI is used. |
| **Korean labeling & IFU** (product name, intended use, warnings, contraindications, disposal) | MFDS 고시 on labeling (no specific number in source) – must be Korean language. |
| **KGMP Certification of the manufacturing/development site** (if domestic) or proof of foreign facility compliance with KGMP equivalence | 「의료기기 GMP 심사·평가 등에 관한 규정」 | Required for 2등급 devices; foreign sites may need MFDS evaluation. |
| **Software version‑control & change‑management records** | Generation AI guideline, IEC 62304 change control | Demonstrates traceability of updates. |
| **Declaration of Conformity (DoC) to applicable standards** | ISO 14971, IEC 62304, IEC 62366‑1 | Signed by the manufacturer. |

*Where a specific MFDS 고시 number is required for any above item, the source does not supply it – “no specific identifier found in source — verify separately.”*

---

### 5. Gaps / Missing Information (to be obtained before submission)

| Gap | Why critical |
|-----|--------------|
| **Full intended‑use statement & clinical claim** | Needed for classification justification and to determine whether any local clinical data are required. |
| **Detailed AI algorithm description & training data set information** | Required by the “생성형 AI 가이드라인” and for risk management of algorithmic bias or drift. |
| **Cybersecurity threat‑model documentation** | MFDS explicitly expects a cyber‑risk assessment for software with network connectivity. |
| **Korean language IFU mock‑up** | Labeling must be in Korean; absence will delay certification. |
| **KGMP compliance evidence for the development site** (certificate or MFDS‑approved audit report) | Certification cannot proceed without proof of GMP‐equivalent quality system. |
| **Verification & Validation test reports (including usability testing)** | Needed to demonstrate that software meets functional and safety requirements per IEC 62304. |
| **Change‑management plan for future AI model updates** | Required by both the AI guideline and IEC 62304 change control. |
| **Clarification of whether digital‑medical‑product law route is also applicable** | Could affect review body (MFDS vs. Ministry of Health & Welfare) and documentation set. |

---

### 6. Core Risk Controls to be Demonstrated

1. **Functional safety controls** – error detection, safe shutdown, user alerts for abnormal conditions.  
2. **Usability safeguards** – prevention of input errors, clear labelling on UI elements, training mode.  
3. **Cybersecurity measures** – encrypted communication, strong authentication, periodic vulnerability scanning, incident‑response procedure.  
4. **AI‑specific controls** – model performance monitoring, out‑of‑distribution detection, fallback to non‑AI operation, audit trail of algorithm decisions.  
5. **Risk management linkage** – each identified hazard must be tied to a specific control documented in the RMF (ISO 14971).  

---

### 7. Human‑Escalation Triggers (When to Seek Senior Review / Decision)

| Trigger | Action |
|--------|--------|
| **Unclear classification justification** (e.g., risk analysis suggests >2등급) | Escalate to senior RA for re‑classification assessment and possible change to 허가 pathway. |
| **Missing KGMP evidence for the development site** | Pause submission; obtain certificate or MFDS audit report before proceeding. |
| **AI component lacks documented compliance with 생성형 AI 가이드라인** | Halt until AI governance package is completed and reviewed. |
| **Cybersecurity assessment incomplete or fails MFDS baseline** | Escalate to IT‑security lead for remediation; cannot submit without full plan. |
| **Korean labeling/IFU not finalized** | Stop submission packaging until Korean language documents are ready. |
| **Discrepancy between intended use and regulatory pathway (digital‑medical‑product law vs. MFDS 고시)** | Convene cross‑functional meeting with legal & product teams to decide appropriate review body. |
| **Any identified audit flag in source material (e.g., suspected outdated guidance)** | Verify the latest version of the cited regulation before finalizing documents. |

---

### 8. Peer‑Review Prompt  

> *@RA‑Colleague* – Please challenge the assumptions above, especially:  
> • Whether the “디지털의료제품법 경로” might supersede the standard 인증 route for this GUI software.  
> • The completeness of the AI governance evidence required under MFDS’s 생성형 AI 가이드라인.  
> • If any recent MFDS 고시 (post‑2026) introduces new Korean‑language labeling elements that we have not captured.  

---

*Prepared by Sam – KR RA Specialist*

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

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `39359892234270838`

> ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재검증 — 핵심 규제사실 반영 확인. · 상태: 승인 · 일자: 2026-06-09

### kb-eval-20261104-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "f20480a0ca9d5f16", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f20480a0ca9d5f16`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%ED%91%9C%EC%8B%9C%EA%B8%B0%EC%9E%AC_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_%EB%8C%80%EC%9D%91.md)
- Source hash: `7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_디지털의료기기_표시기재_가이드라인_대응.md`는 `MFDS_디지털의료기기_표시기재_가이드라인_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 9. 의료기기법 일부개정 (법률 제21949호, 공포 2026-09-15) — 온라인 표시·광고 규제 강화 | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 |...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital‑Health Software (Medical Device)  

1️⃣  Device Synopsis (as inferred from the source)**  
- **Product type:** Software (SW) that is intended for a medical purpose (e.g., diagnosis, monitoring, therapy support).  
- **Regulatory context in Korea:** Covered by the *의료기기법* and the *디지털의료제품법 시행규칙*. The recent amendment **법률 제21949호** (공포 2026‑09‑15) tightens online display/advertising requirements for medical devices.  

---

### 2️⃣ Classification & Submission Route (Korean “등급”)

| Grade | Typical Korean pathway | What is needed to confirm this grade |
|------|------------------------|---------------------------------------|
| **1등급** | 신고 (notification) | Device is low‑risk, non‑invasive, without software‑driven therapeutic function. |
| **2등급** | 인증 (technical‑document review by MFDS‑designated 심사기관) | Moderate risk; requires conformity assessment of technical documentation and KGMP compliance for any manufacturing. |
| **3등급 / 4등급** | 허가 (full MFDS approval) | High‑risk or invasive software, or a device that performs automated diagnosis/therapy. Requires clinical evidence, full safety & performance dossier, KGMP certification, and post‑market surveillance plan. |

> **Current knowledge gap:** The source does not state the intended use, risk level, or whether the software is standalone vs. accessory. **Classification cannot be finalized** until these details are supplied.

*Human‑escalation trigger 1:* If intended use/risk classification remains unknown after initial data collection, forward to a senior RA for clinical risk assessment.

---

### 3️⃣ Required Evidence (based on Korean law and the MFDS software guidelines)

| Evidence Category | Minimum requirement in Korea | Source citation |
|-------------------|------------------------------|-----------------|
| **Technical documentation** – version, build number, release date | S‑1: “SW 버전·빌드 번호·릴리스일” (필수) | 【2†S‑1】 |
| **Software update policy & schedule** | S‑2 (필수) | 【2†S‑2】 |
| **Minimum / recommended system requirements** (OS, CPU, RAM, storage, display, network) | S‑3 (필수) | 【2†S‑3】 |
| **Compatibility list of medical devices & interface specs** | S‑4 (필수) | 【2†S‑4】 |
| **Data exchange formats** (e.g., DICOM, HL7) | S‑5 (필수) | 【2†S‑5】 |
| **Cybersecurity configuration guidance** (password policy, network segregation, access rights) | S‑6 (필수) – MFDS 사이버보안 가이드라인 2025.01 | 【2†S‑6】 |
| **Security‑patch application procedure & responsibility** | S‑7 (필수) – MFDS 사이버보안 가이드라인 2025.01 | 【2†S‑7】 |
| **Known residual cyber risks & mitigation measures** | S‑8 (필수) – MFDS 사이버보안 가이드라인 2025.01 | 【2†S‑8】 |
| **Backup & recovery plan** | S‑9 (필수) | 【2†S‑9】 |
| **System log management** (recommended) | S‑10 (권장) – MFDS 사이버보안 가이드라인 | 【2†S‑10】 |
| **Labeling / IFU in Korean language** | Must comply with the *의료기기법* labeling provisions and the online display rules introduced by **법률 제21949호** (2026‑09‑15). | 【1†법률 제21949호】 |
| **Quality Management System** | KGMP certification (의료기기법 제28조) for 제조·품질관리. | Framework reference – KGMP (no specific identifier found in source — verify separately) |
| **Risk Management** | ISO 14971:2019 risk management process, with additional cybersecurity risk controls per MFDS 사이버보안 가이드라인 2025.01. | Framework reference – ISO 14971 (2019) |
| **Software Life‑Cycle Processes** | IEC 62304 (2006+A1:2015) compliance for medical device software. | Framework reference – IEC 62304 (2006+A1:2015) |
| **Clinical evaluation / performance data** | Required for 3등급·4등급 devices; may be satisfied with foreign CER only if MFDS has issued a specific notice permitting that (e.g., OECD‑MAD is limited to non‑clinical GLP data). The source does not provide such a notice. | No specific identifier found in source — verify separately |
| **Post‑market surveillance plan** | Required for 2등급·3등급·4등급 devices; must follow MFDS 시판후조사 규정. | Framework reference – MFDS post‑market surveillance (no specific identifier found in source — verify separately) |

---

### 4️⃣ Missing Information (must be obtained before dossier finalization)

| Item | Why needed | Source comment |
|------|------------|----------------|
| **Intended use / indication** | Drives risk grade, clinical evidence scope, labeling claims. | Not present in excerpts. |
| **Device classification justification** (risk analysis outcome) | Determines submission track (신고/인증/허가). | Not present. |
| **Manufacturing location & KGMP status of the facility** | KGMP certification is mandatory for 2‑4등급 devices. | No identifier in source. |
| **Clinical evidence strategy** – local data or foreign CER acceptance | Required for higher grades; MFDS may accept foreign CER only under specific notices. | No notice cited. |
> *Human‑escalation trigger 2:* If any of the above items cannot be supplied within 10 working days, raise to the project manager and consider revising scope.

---

### 5️⃣ Key Risk Controls (Korean‑aligned)

1. **Risk Management** – ISO 14971 (2019) process integrated with MFDS 사이버보안 가이드라인 2025.01 for cyber‑risk identification & mitigation.  
2. **Software Life‑Cycle** – IEC 62304 compliance; version control, configuration management (S‑1).  
3. **Cybersecurity Measures** – Password policy, network segmentation, access controls (S‑6), regular patching (S‑7), residual risk monitoring (S‑8).  
4. **Backup & Recovery** – Defined in S‑9; tested quarterly.  
5. **Usability / Human Factors** – Align with IEC 62366‑1 (2015+A1:2020) to ensure safe interaction, especially for AI/ML components (the table hints at AI/ML but details are missing).  

---

### 6️⃣ Citations

| Type | Citation |
|------|----------|
| **Framework reference – law amendment** | 법률 제21949호 (공포 2026‑09‑15) – 강화된 온라인 표시·광고 규제 |
| **Framework reference – ISO/IEC standards** | ISO 14971 (2019); ISO 13485 (2016); IEC 62304 (2006+A1:2015); IEC 62366‑1 (2015+A1:2020) |
| **Instance identifiers from source** | S‑1 … S‑10 items (mandatory/optional fields) – MFDS SW 가이드라인 & 사이버보안 가이드라인 2025.01 |
| **No specific identifier found** for KGMP, clinical‑evaluation notice, or post‑market surveillance rule number – verification needed. |

---

### 7️⃣ Human‑Escalation Triggers (summary)

| Trigger | Action |
|--------|--------|
| **Unclear grade** (no intended use/risk data) | Escalate to senior RA / risk‑assessment team. |
| **Missing clinical evidence strategy** (especially for 3등급·4등급) | Request regulatory intelligence on MFDS foreign‑CER acceptance; involve clinical affairs. |
| **KGMP status unknown** | Contact manufacturing QMS lead; if no KGMP, schedule certification audit. |
| **Cybersecurity residual risk not fully mitigated** | Raise to information security officer and device development lead for additional controls. |
| **Labeling/IFU language gaps (Korean translation missing)** | Send to medical writing team for Korean draft; confirm compliance with online display rules. |

---

### 8️⃣ Peer‑Review Prompt  

> **@RA‑Peer:** Please review the assumptions above—especially the inferred classification path and the completeness of required evidence. Verify whether any recent MFDS notice (post‑2025) permits reliance on foreign clinical evaluation reports for this device type, and confirm that the cited software‑guideline items (S‑1 – S‑10) are still current. Identify any jurisdiction‑specific gaps not covered by the excerpts (e.g., specific KGMP audit scope, post‑market surveillance plan format).  

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

1. Chunk `1044206327041877533`

> ## 9. 의료기기법 일부개정 (법률 제21949호, 공포 2026-09-15) — 온라인 표시·광고 규제 강화

2. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

### kb-eval-20261104-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-04", "decision_ref": "kb-eval-20261104-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "1cf8526b52258974", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `1cf8526b52258974`
- Source: `github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week02_MFDS_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `Week02_MFDS_체계_상세.md`는 `Week02_MFDS_체계_상세.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 --- ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|------...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital‑Medical Device (SaMD) Submission under MF DS**

| Item | Assessment / Requirement | Source Citation |
|------|--------------------------|-----------------|
| **1. Applicable MFDS pathway** | The device is a **디지털의료기기 (SaMD)**.  Classification into Korean grades 1‑4등급 must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」.  Once the grade is confirmed: <br>• 1등급 → 신고 (notification)<br>• 2등급 → 인증 (technical‑document review by an MFDS‑designated 심사기관)<br>• 3·4등급 → 허가 (full approval) | No specific identifier found in source — verify separately |
| **2. KGMP 적합인정** | All digital medical devices require a KGMP (Good Manufacturing Practice) certification before the technical review. The procedural flow is: <br>① GMP 심사 신청 → ② 심사기관 배정 → ③ 품질문서 심사 → ④ 제조소 현장조사 → ⑤ 결함사항 통보(3개 등급: Critical/Major/Minor) → ⑥ 시정 조치 제출 → ⑦ 적합인정서 발급 (유효기간 3년, 갱신 필요). | 【1078228256164017760】 |
| **3. Designated 심사기관** | Six organizations are officially authorized for KGMP 평가, including KTL, KTR and the two TÜV affiliates.  As of **2025‑01‑24**, NIDS (National Institute for Digital Health) has been added to perform GMP 적합판정 for digital medical devices. | 【1078228256164017760】 |
| **4. Recent regulatory changes affecting SaMD** | • 2025‑01‑24 – 시행 of the “디지털의료제품법” introduces a new classification & 허가 체계 for SaMD and expands NIDS authority.<br>• 2025‑05‑07 – MFDS released 6 updated digital‑medical‑device guidelines, explicitly addressing AI/ML‑based GUI software (clinical evidence required).<br>• 2026 예정 – “자율 성능 인증제” (pre‑certification → post‑surveillance) and a “네거티브 방식 변경허가제” (major changes pre‑approval, minor changes after‑notification). | 【1121184088796802935】 |
| **5. Evidence package (minimum)** | 1. **KGMP 인증서** (valid for the manufacturing site).<br>2. **Technical Documentation** (ISO 13485‑compliant QMS, risk management file per ISO 14971:2019, software life‑cycle per IEC 62304 2006+A1:2015, usability per IEC 62366‑1 2015+A1:2020).<br>3. **Korean labeling & IFU** (all user‑facing information in Korean; see MFDS 라벨링 규정 – no identifier in source).<br>4. **Clinical Evaluation Report (CER)** – required for 2등급 이상 SaMD and for AI/ML‑based devices per the 2025‑05‑07 guideline (specific article not quoted; verify separately).<br>5. **Foreign evidence**: MFDS may accept non‑clinical GLP data under OECD MAD and foreign CERs if a relevant notice exists – none is cited in the provided excerpts, so confirm current acceptance policy. | No specific identifier found in source — verify separately (for CER & foreign‑evidence policies) |
| **6. Missing / Unclear Information** | • Exact Korean grade of the SaMD (1~4등급).<br>• Whether the device contains AI/ML components that trigger the 2025‑05‑07 guideline requirements.<br>• Availability of a current KGMP 인증서 for the manufacturing site.<br>• Confirmation of local clinical data requirement (e.g., Korean patient cohort) – not addressed in excerpt. | — |
| **7. Risk Controls (framework)** | • Perform risk analysis per **ISO 14971:2019** and generate a Risk Management Report.<br>• Conduct usability validation per **IEC 62366‑1 2020** to address user errors.<br>• Implement cybersecurity controls in line with MFDS 사이버보안 가이드라인 (referencing IEC 81001‑5‑1 2021). | Framework references – no verification caveat needed |
| **8. Human‑Escalation Triggers** | 1. **Grade Uncertainty** – If the grade cannot be established from existing product information, pause submission and request a formal classification inquiry to MFDS.<br>2. **KGMP Gap** – Absence of a valid KGMP 인증서 blocks both 인증 and 허가 pathways; escalation to manufacturing QA for remediation is required.<br>3. **AI/ML Determination** – If the software includes adaptive algorithms, trigger a review against the 2025‑05‑07 AI/ML guideline; missing evidence forces a hold on filing.<br>4. **Labeling Deficiency** – Any non‑Korean labeling or untranslated IFU mandates immediate correction before dossier acceptance.<br>5. **Foreign Evidence Acceptance** – If relying on OECD MAD or foreign CER, verify the latest MFDS notice; absence of such a notice triggers escalation to regulatory affairs leadership for risk mitigation (e.g., generation of Korean clinical data). | — |

---

### Regulatory Judgment
- **Proceed with a pre‑submission readiness review** once the device’s Korean grade is confirmed.  
- **Assemble KGMP certification** and ensure all referenced standards are incorporated into the technical dossier.  
- **If the device falls into 2등급 or higher, or if AI/ML functionality is present**, prepare an MFDS‑compliant Clinical Evaluation Report per the 2025‑05‑07 guideline.  
- **Address any missing Korean language labeling** before filing.  

All identified gaps must be resolved prior to formal submission; otherwise, the case should be escalated to the senior RA manager for decision on whether to seek a classification clarification or to generate additional local clinical evidence.

---

#### Peer‑Review Prompt
> *Colleague, please review the assumptions made above:*
> 1. **Classification** – Is it reasonable to defer grade assignment pending a reference to the Korean “품목별 등급” regulation?  
> 2. **Scope of required evidence** – Have we captured all MFDS‑specific items for SaMD (e.g., software documentation, cybersecurity) given the 2025‑05‑07 guideline update?  
> 3. **Foreign evidence acceptance** – Does current practice allow reliance on OECD MAD or foreign CERs without an explicit notice cited in our source material?  
> 4. **Human‑escalation triggers** – Are any additional triggers (e.g., post‑market surveillance plan, PMCF) needed for a potential 3·4등급 SaMD?

Your feedback will help ensure completeness and jurisdictional fidelity before finalizing the submission package.

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

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---
