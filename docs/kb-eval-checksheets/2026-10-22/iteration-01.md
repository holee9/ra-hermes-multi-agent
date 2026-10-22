# KB Eval Checksheet - 2026-10-22 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261022-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "760d57bf5597bd55", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md", "source_hash": "17067eef9c351571ca7c8dedcea62a4c6b790ae298cec359778dca145c690031"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `760d57bf5597bd55`
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

> **Regulatory Draft – SaMD Change Impact Assessment (2026‑10‑22)**  

---

### 1. Bottom‑Line Decision  
| Item | Assessment |
|------|------------|
| **Device class & FDA pathway** | *Indeterminate* – classification cannot be finalized without the device’s intended use, indications, and target patient population. Most SaMDs fall in **Class II (21 CFR 892.2050)** when they perform image management/analysis or **Class II under 21 CFR 862** for clinical‑laboratory software. The default route is a **510(k) Premarket Notification** using the substantial‑equivalence paradigm; a **De Novo** submission should be considered only if no suitable predicate exists. |
| **Submission type** | 510(k) (substantial equivalence) – pending predicate identification. |
| **Primary regulatory evidence required** | 1. Device description & intended use statement.<br>2. Predicate comparison matrix (if 510(k)).<br>3. Software Design History File (DHF) aligned to **IEC 62304:2006+A1:2015** (including verification/validation reports).<br>4. Risk Management File per **ISO 14971:2019** (see Section 5.3 of source).<br>5. SBOM & SOUP inventory (per FDA 524B guidance).<br>6. Predetermined Change Control Plan (PCCP) for AI/ML updates.<br>7. Labeling (21 CFR 801) and UDI (21 CFR 830) documentation.<br>8. QMS compliance evidence – **21 CFR 820** (QMSR, ISO 13485:2016 aligned). |
| **Key missing information** | • Exact intended use & clinical context.<br>• Device functional description (diagnostic, monitoring, therapeutic?).<br>• Classification rule citation from the FDA’s product classification database.<br>• Predicate device 510(k) number(s).<br>• Clinical performance data requirement (if intended for diagnosis/therapy).<br>• Cybersecurity plan details beyond SBOM. |
| **Human‑escalation triggers** | • Inability to locate a suitable predicate → escalation to senior RA for De Novo feasibility.<br>• Residual risk not acceptable per ISO 14971:2019 risk assessment – send to risk management lead.<br>· Change scope exceeds what is covered by the existing PCCP → request FDA pre‑market clarification (AI/ML change plan) before proceeding.<br>· SBOM or SOUP list incomplete → involve software engineering & supply‑chain compliance team.<br>· FDA Additional Information (AI) request projected >180 days response window → flag to project manager for timeline impact. |
| **Next actionable steps** | 1. Obtain complete device specification, intended use, and target user.<br>2. Perform a classification search in the FDA Product Classification database; record the applicable CFR part & section (e.g., §892.2050).<br>3. Identify one or more predicate devices (clearance numbers) for a 510(k) claim.<br>4. Populate the Risk Management File using the template outlined in **ISO 14971:2019** and link each hazard to design control entries in IEC 62304 §7 (as indicated in source).<br>5. Compile a full SBOM & SOUP inventory; map mitigation strategies per FDA 524B guidance.<br>6. Draft or update the Predetermined Change Control Plan (PCCP) for any AI/ML model updates, referencing the December 2024 FDA final guidance. |
---  

### 2. Required Evidence Detail  

| Evidence | Source Requirement | Notes |
|----------|--------------------|-------|
| **Device Description & Intended Use** | 21 CFR 807 (registration/listing) & labeling (§801) | Must be precise to enable predicate comparison. |
| **Predicate Comparison Matrix** | 21 CFR 807.92 – Substantial‑equivalence analysis | Requires identification of cleared 510(k)s; *no specific identifier found in source – verify separately*. |
| **Software Design History File (DHF)** | IEC 62304:2006+A1:2015 – Sections on software development lifecycle, verification & validation. | Source links risk analysis to IEC 62304 §7. |
| **Risk Management File** | ISO 14971:2019 – Required elements: Risk Management Plan, Hazard analysis, Risk evaluation, Risk control, Residual risk assessment, and Risk Management Report (source §5.3). | Include “risk → control → verification traceability matrix.” |
| **SBOM & SOUP List** | FDA 524B (Software Bill of Materials) guidance – mandatory for medical device software. Source notes SBOM requirement; no CFR citation needed. |
| **Predetermined Change Control Plan (PCCP)** | FDA Final Guidance, Dec 2024 – “Predetermined Change Control Plan (PCCP).” | Required for AI/ML SaMD changes. |
| **Labeling & UDI** | 21 CFR 801 (labeling) and 21 CFR 830 (UDI) | Includes device name, intended use, warnings, and unique identifier. |
| **Quality Management System Evidence** | 21 CFR 820 (QMSR), effective Feb 2026; ISO 13485:2016 alignment – required for all Class II devices. |
| **Clinical Performance Data (if applicable)** | FDA guidance on clinical evaluation of SaMD (e.g., “Policy for Device Software Functions and Clinical Evaluation”). | Needed when software provides diagnostic or therapeutic output. |

### 3. Risk Controls Summary  

1. **Risk Management Plan** – define risk acceptance criteria; reference ISO 14971:2019.  
2. **Software Hazard Analysis** – map each identified hazard to a design control in IEC 62304 §7 (architecture, code modules).  
3. **Verification & Validation Matrix** – trace each control to verification test results; ensure coverage of all software requirements.  
4. **SOUP Mitigation** – maintain an up‑to‑date SBOM; apply vendor security assessments and version control; isolate third‑party components where feasible.  
5. **PCCP Governance** – predefine the scope of permissible AI/ML model updates, performance monitoring metrics, and post‑deployment change verification steps.  
6. **Cybersecurity Controls** – implement FDA’s “Content of Premarket Submissions for Management of Cybersecurity” recommendations; include threat modeling, encryption, access control.  
7. **Post‑Market Surveillance** – integrate a field safety corrective action plan (21 CFR 806) for any residual risk that becomes unacceptable after launch.

### 4. Citations  

| Item | Citation Type | Reference |
|------|--------------|-----------|
| ISO 14971 Risk Management File requirement | Framework reference | **ISO 14971:2019** |
| IEC 62304 software‑risk linkage (Section 7) | Framework reference – appears in source | **IEC 62304 § 7** |
| SBOM requirement under FDA 524B | Framework reference (FDA guidance) | No specific identifier found in source — verify separately |
| Predetermined Change Control Plan (PCCP) | Framework reference (final guidance, Dec 2024) | No specific identifier found in source — verify separately |
| QMSR (21 CFR 820) and ISO 13485:2016 alignment | Framework reference | **21 CFR 820**; **ISO 13485:2016** |
| UDI requirements | Framework reference | **21 CFR 830** |
| Labeling requirements | Framework reference | **21 CFR 801** |

*(All framework references are stated as facts per the instruction. No invented device numbers or specific CFR subsections beyond those provided in the source have been added.)*

### 5. Human‑Escalation Triggers  

| Trigger | Action |
|--------|--------|
| **No clear predicate identified** | Escalate to senior RA for De Novo feasibility analysis and possible early FDA interaction (Pre‑Submission). |
| **Residual risk > acceptance criteria** | Stop submission preparation; convene cross‑functional risk review; potentially redesign software. |
| **Planned AI/ML change exceeds scope of existing PCCP** | Submit a supplemental pre‑market notification to FDA or request clarification via Q‑submission. |
| **SBOM/SOUP list incomplete or contains undocumented components** | Pause submission; involve procurement & cybersecurity teams to remediate. |
| **FDA issues an Additional Information (AI) request with >180 days response window** | Notify project manager; re‑baseline schedule; consider requesting a meeting with FDA to clarify expectations. |
| **Uncertainty in device classification or applicable CFR part** | Immediately seek input from the regulatory classification database team and/or senior regulator before finalizing pathway. |

---

### 6. Peer Review Prompt  

> **Colleague, please review:**  
> 1. Are the assumptions about defaulting to a 510(k) appropriate given the limited device description?  
> 2. Does the list of required evidence fully capture FDA expectations for an AI‑enabled SaMD with SOUP components?  
> 3. Have we identified all jurisdiction‑specific gaps (e.g., missing reference to IEC 62366‑1 usability engineering, or Cybersecurity content per FDA’s “Content of Premarket Submissions for Management of Cybersecurity” guidance)?  
> 4. Are the escalation triggers sufficiently granular to prompt timely human intervention?  

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

1. Chunk `1023300943338888510`

> ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. ---

2. Chunk `1150973762104113645`

> + SOUP (IEC 62304) | SOUP 목록 (IEC 62304 준수) | SOUP 목록 (IEC 62304) + SBOM (SBOM 의무는 FDA 524B; MDR은 명시 SBOM 요건 없음 — MDCG 2019-16 사이버보안 준용) | | AI/ML 소프트웨어 | PCCP (Predetermined Change Control Plan, 2024 Final) | AI 의료기기 가이드라인 (MFDS 2025) | MDCG 2021-6 AI 가이던스 |

### kb-eval-20261022-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "96d232857ab58cd2", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `96d232857ab58cd2`
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

> **Regulatory Draft – SaMD Change Impact Assessment for “촬영실 GUI Software” (Imaging‑Room Image Processing & Display Application)**  

---

### 1. Bottom Line  
- **Device class:** Class II – Image Processing Software (21 CFR §892.2050).  
- **Primary submission route:** Traditional 510(k) (Premarket Notification) with the eSTAR format for software‑focused evidence.  
- **Current status:** Existing cleared software; a change is planned. The change must be evaluated against FDA’s “Predetermined Change Control Plan (PCCP)” guidance. If the modification exceeds the scope of the original clearance (new intended use, new risk class, or new functionality), a **new 510(k) submission** is required; otherwise a **supplemental 510(k)** may suffice.  

---

### 2. Classification & Regulatory Pathway  

| Item | Reference |
|------|------------|
| Device type – Image processing software (Class II) | 21 CFR §892.2050 |
| Applicable FDA guidance for content of software submissions | “Guidance for the Content of Premarket Submissions for Device Software Functions” (June 14 2023, Final) |
| Cybersecurity expectations | “Cybersecurity in Medical Devices” (Sept 27 2023, Final) |
| Software life‑cycle standard | IEC 62304:2006+A1:2015 |

*Conclusion:* The product falls squarely under the 510(k) pathway for Class II devices.  

---

### 3. Required Evidence Package (eSTAR Section G – Performance Testing ‑ Software)

| Document | Purpose | Minimum content |
|----------|---------|-----------------|
| Executive Summary of GUI SW Validation | High‑level overview & conclusions | Scope, test strategy, pass/fail criteria |
| Software Requirements Specification (SRS) | Captures user needs & functional requirements | Intended use, performance requirements, safety functions |
| Software Design Specification (SDS) | Architecture & detailed design | Module definitions, algorithms, interface specs |
| Requirements Traceability Matrix (RTM) | Links SRS → SDS → verification/validation (V&V) | Bidirectional traceability for all requirements |
| Software Validation Plan (SVP) | Test planning | Unit, integration, system, performance test plans; acceptance criteria |
| Software Validation Report (SVR) | Evidence of V&V execution | Complete test results, defect logs, resolution records |
| Unit / Integration / System Test Results (folders) | Detailed raw data | Pass/fail tables, screenshots, log files |
| Performance Test Results (folder) | Demonstrates intended image processing performance | Accuracy, precision, latency, display fidelity |
| Validation Dataset Description | Data provenance & suitability | Source of images, ground truth, anonymization details |
| Anomaly Log & Resolution Spreadsheet | Issue tracking & corrective actions | Defect ID, severity, root‑cause analysis, mitigation status |

*All documents must be signed by a qualified individual (e.g., QA manager) and cross‑referenced to the RTM.*  

---

### 4. Risk Management Requirements  

| Requirement | Where it is addressed |
|-------------|-----------------------|
| Overall risk management file (ISO 14971:2019) | Separate “Risk Management Report” linked in eSTAR Section G |
| Software safety class determination (IEC 62304) – Class B for this viewer/processor | Table in source excerpt (Class B = minor to moderate harm) |
| Hazard analysis & risk controls (e.g., UI mis‑display, data corruption) | Included in the Risk Management Report and SDS |
| Cybersecurity threat assessment & mitigations (FDA Guidance 2023‑09‑27) | Separate “Cybersecurity Threat Model” and “Mitigation Plan” referenced in SVP |
| Post‑market surveillance plan (21 CFR §820.150) | Mentioned in QMS documentation, not required for clearance but advisable |

*Missing:* A **formal Risk Management Report** with hazard analysis, risk evaluation, and verification of mitigations is not listed among the eSTAR files; it must be produced before submission.

---

### 5. Missing Information & Gap Checklist  

| Gap | Impact if left unresolved |
|-----|---------------------------|
| **Intended Use Statement** (clear, concise description) | Needed for predicate comparison and risk analysis |
| **Predicate Device Identification** (510(k) number, market‑cleared device) | Required to demonstrate substantial equivalence |
| **Labeling & UDI considerations** (21 CFR §820.100, §830.10‑§830.70) | Must be included in the 510(k) labeling section |
| **Software Change Description** (what is being modified, rationale) | Determines whether a new or supplemental submission is needed |
| **Verification that change does not alter class** – e.g., adding AI‑based feature would trigger PCCP evaluation | Critical for pathway decision |
| **Human Factors / Usability validation** (especially for GUI interaction) | Required for Class II devices with user interface |
| **Software Configuration Management plan** (change control, versioning) | Needed to satisfy QMSR (21 CFR §820.30) and support future PCCP |
| **Cybersecurity Evidence of Ongoing Monitoring** (patch management strategy) | Required by 2023 cybersecurity guidance |

---

### 6. Change‑Impact Decision Flow  

1. **Is the change limited to bug fixes or minor UI tweaks that do not affect functionality, risk class, or intended use?**  
   - *Yes* → Prepare a **Supplemental 510(k)** (formerly “Special 510(k)”) with updated validation results & risk analysis.  

2. **Does the change add new processing algorithms, increase performance claims, modify data handling, or introduce AI/ML functions?**  
   - *Yes* → The change likely exceeds the original clearance scope. Initiate a **new Traditional 510(k)** (or consider filing a **Predetermined Change Control Plan (PCCP)** if the manufacturer has an FDA‑approved PCCP for this device).  

3. **If any new hazard is identified or risk class would shift to Class C (per IEC 62304),** → Escalate immediately; a **De Novo** request may be required.

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required |
|--------|-----------------|
| New intended use, performance claim, or algorithm added | Notify senior regulatory lead → prepare full 510(k) dossier |
| Risk analysis reveals *unmitigated* Class C hazard | Pause release → engage engineering & QA → consider De Novo pathway |
| Cybersecurity vulnerability disclosed that impacts device integrity | Immediate safety recall assessment under 21 CFR §806; prepare Field Safety Notice / Voluntary Corrective Action Report |
| FDA issues an Additional Information (AI) request during review exceeding 180 days response window | Escalate to Regulatory Affairs Manager for senior leadership approval of timeline and resources |
| Ambiguity in whether change fits within existing PCCP scope | Request formal clarification from FDA via the 510(k) pre‑submission Q&A process |

---

### 8. Regulatory Judgment  

- The “촬영실 GUI Software” is a Class II SaMD (image processing) cleared under 21 CFR §892.2050.  
- A **new or supplemental 510(k)** will be required depending on the nature of the modification; the decision hinges on whether the change alters intended use, introduces new functionality, or elevates risk.  
- The current eSTAR package is largely complete but lacks a formal Risk Management Report, Intended Use statement, Predicate device citation, and Human Factors validation evidence—these must be added before any submission.  

**Proceed with a gap‑closure work package to generate the missing artifacts, then apply the change‑impact decision flow above to select the appropriate 510(k) pathway.**

---

### 9. Peer‑Review Prompt  

> *Colleague RA, please review:*
> - **Assumptions about Class II classification** (are we certain no hardware component or higher‑risk function is involved?)  
> - **Completeness of evidence** (does the eSTAR checklist satisfy FDA’s 2023 software guidance in full?)  
> - **Jurisdictional gaps** (any EU/Korean references in source material that might affect US filing strategy?).  

Your feedback will help validate the pathway choice and ensure no regulatory blind spots remain.

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

### kb-eval-20261022-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "a9eb5e3658e2cd2f", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `a9eb5e3658e2cd2f`
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

> **Regulatory Draft – Imaging‑Workstation Software (SaMD) 510(k) Strategy**

---

### 1. Device Overview & Intended Use  
- **Product:** GUI/firmware for an imaging workstation (acquisition, processing, display, storage, transfer, worklist, QA).  
- **Intended Use Statement (proposed):** “To acquire, process, display, store and transmit DICOM‑compatible medical images on a dedicated workstation for use by qualified healthcare professionals.”  
- **AI/ML:** Not indicated in source; to be confirmed.

---

### 2. Classification & Submission Pathway  

| Item | Regulation |
|------|------------|
| **Device Class** | Class II (medical image management and processing system) – **21 CFR §892.2050** |
| **Premarket Route** | Traditional **510(k)‑based substantial equivalence** submission – 21 CFR §§807, 820, 830 |
| **Regulatory Program References** | *QMSR* (21 CFR Part 820), *UDI* (21 CFR Part 830), *Labeling* (21 CFR Part 801) |

---

### 3. Predicate‑Selection Requirements (per source checklist)

1. Search FDA 510(k) database by **product code** (e.g., “QZ” for imaging workstations).  
2. Prefer predicates cleared **≤ 5 yr** old; older (> 7 yr) predicates require additional justification. – *no specific identifier found in source — verify separately*  
3. Verify that each predicate:  
   - Is still commercially marketed (not retired/discontinued).  
   - Has no recall or safety communication (MAUDE/Recall DB). – *no specific identifier found in source — verify separately*  
4. Conduct **Indications‑for‑Use** text comparison; our IFU must be identical or narrower.  
5. List all **technical differences** and provide supporting data for each.  
6. Use a single primary predicate; split predicates are prohibited.

**Missing Information**  
- Exact product code(s) and candidate 510(k) numbers.  
- Confirmation of market status & recall history of each candidate predicate.  

---

### 4. Evidence Package – Minimum Required

| Evidence | Basis |
|----------|-------|
| **Predicate comparison table** (IFU, indications, labeling, intended use) | 21 CFR §807.92(b)(5); source checklist |
| **Risk Management File** (ISO 14971:2019) with hazard analysis, risk control measures, and residual risk justification | ISO 14971 (framework reference) |
| **Software Development Lifecycle Documentation** – IEC 62304 safety class determination (A/B/C) & verification/validation reports | IEC 62304 2006+A1:2015 |
| **Cybersecurity Plan** – authentication, encryption, audit logs, update mechanisms; alignment with FDA “Content of Pre‑market Submissions for Device Software” (2023 Basic/Enhanced) | FDA 2023 software guidance (framework reference) |
| **DICOM Conformity Statement** – mapping to SCU/SCP services (Storage, Worklist, MPPS, Print) | DICOM Standard (reference) |
| **SBOM** – SPDX or CycloneDX format | Supply‑Chain Transparency guidance (framework reference) |
| **Interoperability Evidence** – HL7 FHIR, IHE profile test results (if claimed) | IHE Technical Framework (framework reference) |
| **Labeling & UDI** – label page, Instructions for Use, UDI placement per 21 CFR §§801, 830.10‑830.60 | 21 CFR Parts 801 & 830 |
| **AI/ML Controls** (if applicable) – Predetermined Change Control Plan (PCCP) submission | FDA Dec 2024 PCCP guidance |

**Missing Information**  
- Confirmation of AI/ML module presence and intended use; if present, a draft PCCP.  
- Detailed OS and minimum hardware specifications.  
- Exact list of supported languages/localizations.

---

### 5. Risk Controls & Design Mitigations  

| Hazard Category | Control(s) |
|-----------------|------------|
| **Software safety class** (IEC 62304) – assign Class C if failure could cause patient harm; otherwise B/A. | Design controls per 21 CFR Part 820, verification/validation, and risk control implementation. |
| **Data integrity / image corruption** | CRC checks, DICOM SOP compliance, backup & restore procedures. |
| **Unauthorized access** | Role‑based authentication, TLS encryption for network communications, audit logging. |
| **AI/ML unintended output** (if applicable) | PCCP with pre‑market performance verification and post‑market monitoring plan. |
| **Usability errors** | Human factors validation per IEC 62366‑1 2015; GUI labeling consistency with IFU. |

---

### 6. Outstanding Items / Information Gaps  

| Gap | Action Required |
|-----|-----------------|
| Predicate device list (510(k) numbers, market status) | Conduct database search & MAUDE review. |
| AI/ML module scope (if any) | Provide functional description; develop PCCP. |
| Detailed OS/hardware spec sheet | Obtain from development team. |
| Interoperability protocol test reports (HL7 FHIR, IHE) | Generate and include validation data. |
| Localization matrix (languages supported) | Document and map to UI elements. |

---

### 7. Human‑Escalation Triggers  

- **Predicate uncertainty** – no clear primary predicate or market/recall status unresolved → Escalate to RA Lead for alternative strategy (de Novo, split‑predicate review).  
- **AI/ML inclusion discovered** – requires PCCP; if not prepared, pause 510(k) timeline and trigger AI/ML work‑stream.  
- **Safety class upgrade to IEC 62304 Class C** → Re‑evaluate need for additional clinical data or special controls; escalate to Regulatory Strategy Lead.  
- **Significant change in intended use (e.g., addition of diagnostic interpretation)** → May shift device to a higher classification; immediate escalation required.  
- **Inability to provide justified equivalence for any technical difference** → Pause submission preparation; involve engineering and safety teams for remediation.

---

### 8. Peer‑Review Prompt  

> *Please review the assumptions above: (1) classification as Class II under §892.2050, (2) completeness of the predicate‑selection checklist without specific 510(k) identifiers, (3) the sufficiency of listed evidence items for a “Basic” software submission, and (4) any jurisdiction‑specific gaps such as post‑market surveillance requirements that may affect this SaMD.*

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

### kb-eval-20261022-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_us-004", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "1337a5578f5f7bfe", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `1337a5578f5f7bfe`
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

> **Regulatory Draft – SaMD “촬영실 GUI” (Imaging‑Room User‑Interface Software)**  

---

### 1. Device Overview & Intended Use  
- **Product:** Stand‑alone medical software that provides the graphical user interface for image acquisition and display in a radiology imaging suite (X‑ray/CT/ultrasound).  
- **Intended Use Statement (example):** “The software enables real‑time visualization, manipulation and annotation of diagnostic images captured by FDA‑cleared imaging modalities. It does not perform automated diagnosis or quantitative analysis.”  

---

### 2. Classification & Submission Pathway  

| Item | Determination | Regulatory Basis |
|------|--------------|-------------------|
| **Device Class** | **Class II** (moderate risk) | 21 CFR §892.2050 – *Medical image management and processing system* (software that provides display/management of radiologic images). The GUI fits this definition because it exclusively presents images captured by a regulated imaging modality. |
| **Regulatory Pathway** | **510(k) Premarket Notification** (substantial equivalence) | 21 CFR §807 – requirements for Class II devices. A predicate device cleared under §892.2050 (e.g., a previously cleared PACS viewer or radiology workstation software) must be identified. |
| **Alternative Pathway (if no suitable predicate)** | De Novo classification request (Class II) | 21 CFR §814.2(b)(3). Use only if substantial equivalence cannot be demonstrated. |

> *No specific 510(k) numbers appear in the source – verify separately.*

---

### 3. Core Regulatory Requirements & Evidence Package  

| Requirement | Evidence to Submit | Source‑based Citation |
|-------------|-------------------|-----------------------|
| **Device Description & Intended Use** | Detailed UI flow diagrams, function list, hardware platform description (if any) | §892.2050 (classification) |
| **Substantial Equivalence Comparison** | Side‑by‑side table with cleared predicate(s): device name, 510(k) number, technological characteristics, performance claims | 21 CFR §807.92 |
| **Risk Management File** | ISO 14971:2019 risk analysis, risk control measures, residual risk justification | Framework reference (ISO 14971). |
| **Software Development Life‑Cycle Documentation** | IEC 62304:2006+A1:2015 compliance evidence – software development plan, requirements spec (SDP/SRS), design docs (SAD), verification & validation reports (SVP/SVR) | IEC 62304 §8.1 (software verification). |
| **Software Validation & Verification** | Unit, integration, system testing results; regression‑test automation artifacts; change‑control SOPs | IEC 62304 §8.1; source Table “SW 밸리데이션”. |
| **Cybersecurity / Change Control** | Threat model, SBOM, Predetermined Change Control Plan (PCCP) per FDA Final Guidance (Dec 2024), mapping to AI/ML change management if applicable | FDA PCCP (2024‑12‑03); source “사이버보안” row. |
| **UDI Assignment & Labeling** | Device identifier, production identifier, label artwork, GUDID submission evidence | 21 CFR §830.10–§830.60 (UDI) – cited in ARR requirement. |
| **Post‑Market Reporting Obligations** | MDR (Medical Device Reporting) procedure, correction/removal SOP per §§803 & 806; complaint handling record template satisfying §820.35(a) | §§820.10(b), 820.35(a); source “불만 파일 강화”. |
| **Quality Management System – QMSR** | Full ISO 13485:2016‑based QMS with added ARR activities (UDI, MDR reporting, corrections/removals) and inclusion of contract sterilizer/re‑labeler under §820.10(a). Internal audit reports demonstrably accessible to FDA inspectors (§820 overall). | §§820.10(b), 820.35, 820.20; source “ARR”, “내부감사 실사”. |
| **Clinical Performance (if required)** | If the software claims affect clinical interpretation, provide a small usability/clinical validation study (per FDA guidance on SaMD). Otherwise a bench‑level functional test suite suffices. | No specific identifier in source – verify separately. |

---

### 4. Identified Gaps / Missing Information  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Predicate Device(s)** | Essential for 510(k) claim of substantial equivalence. | Perform market search; select at least one cleared device under §892.2050 and obtain its 510(k) number. |
| **Detailed Intended Use Statement** | Determines classification and whether a clinical performance study is needed. | Draft precise language; confirm with product team. |
| **AI/ML Feature Specification (if any)** | Requires PCCP documentation and may trigger additional FDA review of change‑control plans. | Provide algorithm description, intended use, training data set details; develop PCCP. |
| **UDI Allocation Strategy** | ARR clause demands integration of UDI generation and GUDID submission. | Assign Issuing Agency, generate label content, complete GUDID entry. |
| **Contract Sterilizer / Re‑labeler Agreements** | §820.10(a) now includes these parties in QMSR scope; lack of documented controls could be a deficiency. | Capture supplier qualification records and SOPs for outsourced processes. |
| **Complaint/Adverse Event Triage Procedure** | Must record MDR reportability decision per §820.35(a); currently only mentioned generically. | Develop SOP with decision tree, train staff, retain records. |

---

### 5. Risk Controls (Key Elements)  

1. **Design Controls** – enforce IEC 62304 development lifecycle; link each software requirement to test case.  
2. **Hazard Analysis** – per ISO 14971: identify hazards such as incorrect image rendering, user input errors, data loss. Apply mitigations (e.g., UI confirmation dialogs, redundancy of image storage).  
3. **Cybersecurity** – threat modeling (STRIDE or similar), SBOM for third‑party libraries, PCCP to pre‑authorize patches and algorithm updates without new 510(k).  
4. **Usability Engineering** – formative/usability testing to reduce use errors; incorporate findings into risk assessment.  
5. **Post‑Market Surveillance** – MDR reporting workflow (30‑day submission) integrated with complaint handling; corrective actions documented per §§803/806.  

---

### 6. Human‑Escalation Triggers  

| Situation | Escalate To | Reason |
|-----------|-------------|--------|
| No viable predicate device identified after market search | Senior Regulatory Lead / Director of RA | 510(k) cannot be prepared without a predicate. |
| AI/ML functionality added or modified after initial submission draft | Head of Software‑SaMD Strategy + FDA Liaison | May require new PCCP amendment or supplemental 510(k). |
| Incomplete QMSR coverage (e.g., missing ARR activities, contract sterilizer controls) | Quality Assurance Manager | Non‑compliance with §820.10(b) could trigger FDA Form 483. |
| UDI generation plan not finalized before filing | Regulatory Project Manager | Missing mandatory labeling element under 21 CFR §830.10. |
| Evidence of inadequate cybersecurity (no threat model / PCCP) | Chief Information Security Officer & RA Lead | Potential for FDA safety notice per CFR 822 (not shown but implied). |
| Failure to produce a complete risk management file (ISO 14971) | Risk Management Committee Chair | Core requirement for SaMD acceptance. |

---

### 7. Peer‑Review Prompt  

> **Action:** Request another RA colleague to review this draft, specifically:  
> - Confirm the suitability of the chosen predicate(s) and whether additional predicates are needed.  
> - Validate that all ARR obligations (UDI, MDR reporting, corrections/removals) are fully captured under QMSR.  
> - Check for any jurisdiction‑specific gaps (e.g., missing references to FDA’s “Software Pre‑certification” which is no longer active).  

---

**Bottom Line:**  
The “촬영실 GUI” SaMD falls under **Class II, §892.2050**, requiring a **510(k) submission** with substantial‑equivalence evidence, full **QMSR compliance** (including ARR items), ISO 14971 risk management, IEC 62304 software validation, FDA‑approved **PCCP** for any AI/ML changes, and complete UDI labeling. The identified missing items must be addressed before the submission docket is closed; any unresolved trigger should be escalated per the table above.  

*No specific device numbers or regulatory notices were extracted from the source – those identifiers must be verified separately.*

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

### kb-eval-20261022-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "40f2679dcd1f77ab", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `40f2679dcd1f77ab`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_01_Device_Description_IFU.md)
- Source hash: `70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_01_Device_Description_IFU.md`는 FDA eSTAR device description 및 IFU 작성에 필요한 제품 설명·표시 정보 문서입니다.
- 현재 excerpt 핵심: ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA For...
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

> **Regulatory Draft – Software‑only Radiography Acquisition & Control System (GUI)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|----------------|
| **CFR Panel** | Imaging & radiology devices → **21 CFR Part 892** (see Part map). |
| **Device Class** | The software provides image acquisition, review and management but expressly *does not* perform primary diagnosis. Under § 892.2050 (Medical image management and processing system) the device is a **Class II** product. |
| **Regulatory Route** | **Traditional 510(k)** (21 CFR 807). An abbreviated 510(k) could be pursued only after a suitable predicate with identical technological characteristics and intended use is identified – this must be verified. |

*Citation:* Classification based on function and the “not for primary diagnosis” language in the Indications for Use statement (Excerpt 2).  

---

### 2. Core Submission Content & Evidence Required  

| Section | Required Sub‑elements | Source / Reference |
|---------|----------------------|--------------------|
| **Device Description** | • Software architecture diagram (modules, processes, DB, DICOM node) <br>• OS and minimum hardware specs <br>• List of compatible detectors/generators with versions <br>• DICOM conformance statement (SCU roles, MPPS, Worklist) <br>• Cybersecurity features (encryption, authentication, audit logs) <br>• IEC 62304 safety class (A/B/C) <br>• SOUP inventory & identification | Excerpt 2 – “Device Description 포함 항목” |
| **Intended Use / Indications for Use** | Formal statement on Form 3881; wording must avoid “diagnosis” or “interpretation.” | FDA Form 3881 (Excerpt 1) |
| **Software Development Lifecycle** | IEC 62304‑compliant design history file, verification & validation protocols/reports, traceability matrix. | IEC 62304 (framework reference) |
| **Risk Management** | ISO 14971:2019 risk analysis, mitigation plan, post‑market surveillance strategy. | Framework reference – ISO 14971 |
| **Cybersecurity Documentation** | Threat model, mitigation controls, update/authentication procedures; reference to FDA “Predetermined Change Control Plan (PCCP)” if future updates are anticipated. | FDA guidance on PCCP (2024) – framework |
| **Performance/Functional Testing** | • Image acquisition timing, DICOM transmission integrity <br>• Image quality metrics (resolution, contrast‑to‑noise) <br>• Usability testing with trained technologists (per IEC 62366‑1) | IEC 62366‑1 (framework) |
| **Labeling & IFU** | 21 CFR 801 labeling requirements; full Instructions for Use (IFU) consistent with Form 3881. | Excerpt 1 – “FDA Form 3881” |
| **Quality System Evidence** | QMS compliant with 21 CFR 820 and the new Quality Management System Regulation (QMSR) effective Feb‑2026. | Part 820 (framework) |
| **Unique Device Identification (UDI)** | Label & packaging must contain a UDI per 21 CFR 830; registration in GUDID. | Part 830 (framework) |
| **Predicate Comparison** | Side‑by‑side table of technological attributes, indications, and performance with an identified legally marketed device (e.g., a cleared radiography acquisition workstation). | *No specific identifier found in source — verify separately* |

---

### 3. Gaps / Missing Information (to be supplied before filing)

| Gap | Why needed | Action |
|-----|------------|--------|
| **Predicate Device** | Required to establish substantial equivalence for any 510(k). | Conduct market search; document device name, K‑number, and compare specifications. |
| **Detailed Verification & Validation Results** | Demonstrates compliance with IEC 62304 and performance claims. | Provide test protocols, raw data, summary reports. |
| **Comprehensive Cybersecurity Threat Model** | FDA expects documented risk analysis for software security (PCCP). | Produce a threat‑risk matrix; outline mitigation and maintenance plan. |
| **SOUP Inventory List with Versioning** | Needed for IEC 62304 compliance and traceability. | Compile list of all third‑party components, licenses, and verification status. |
| **Usability/Human Factors Evaluation** | Required under IEC 62366‑1 to show safe use by trained technologists. | Conduct formative & summative usability studies; submit findings. |
| **Labeling Draft Packaged with Form 3881** | Must match intended‑use statement and avoid diagnostic claims. | Prepare labeling, IFU, and complete Form 3881. |
| **UDI Implementation Plan** | Part 830 compliance is mandatory for Class II devices. | Assign issuing agency, generate device identifier, register in GUDID. |
| **QMS Documentation (Design Controls, CAPA, Document Control)** | Required by 21 CFR 820 & QMSR. | Provide extracts of SOPs, design history file, and audit reports. |

---

### 4. Risk Controls & Mitigation Summary  

| Hazard | Potential Harm | Control(s) |
|--------|----------------|------------|
| Incorrect image acquisition parameters (exposure, positioning) | Sub‑optimal diagnostic image → potential delayed diagnosis (though device not for interpretation) | UI lock‑outs for out‑of‑range settings; alerts to operator; default safe presets. |
| Data corruption during DICOM transfer | Loss of patient data, need for repeat imaging | End‑to‑end checksum verification, MPPS status monitoring, automatic retransmission on error. |
| Unauthorized access to acquisition console | Manipulation of device settings or exposure values | Role‑based authentication, encrypted network traffic (TLS), audit log retention ≥ 1 year. |
| Software crash / unexpected shutdown | Interrupt workflow, possible patient safety event if exposure continues | Watchdog timer; safe‑state shutdown of X‑ray generator; fail‑safe hardware interlock. |
| Vulnerable third‑party library (SOUP) | Exploitable security flaw | Maintain inventory, apply version‑specific patches, perform static analysis and penetration testing. |

Risk management performed per **ISO 14971:2019** with design controls aligned to **21 CFR 820**. Cybersecurity addressed through the FDA’s PCCP framework (2024 guidance).

---

### 5. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **No suitable predicate identified** within 30 days of project start | Escalate to senior RA lead; consider De Novo or PMA pathway. |
| **Intended use statement changes to include “diagnosis” or “interpretation.”** | Immediate stop‑work; re‑evaluate classification (possible Class III) and submission strategy. |
| **Critical cybersecurity vulnerability discovered post‑submission** | Initiate Predetermined Change Control Plan (PCCP); submit a 510(k) supplement if change impacts safety/effectiveness. |
| **QMS audit reveals non‑conformity with Part 820/QMSR** | Halt filing; remediate QMS gaps and document corrective actions before submission. |
| **FDA issues an Additional Information (AI) request exceeding 180 days** | Notify project manager; allocate resources for response; consider deadline impact on product launch. |

---

### 6. Bottom‑Line Regulatory Judgment  

- The GUI software is a **Class II medical device** governed by **21 CFR Part 892 (§892.2050)** and must be cleared via a **Traditional 510(k)** demonstrating substantial equivalence to an existing radiography acquisition workstation.  
- All core evidence items listed above are required; the current source provides only a high‑level description of needed content (Excerpt 2) and the regulatory forms / CFR citations (Excerpt 1). Significant gaps remain, especially the predicate identification, detailed verification/validation data, cybersecurity threat model, SOUP inventory, and complete QMS/UDI documentation.

**Proceed with:**  
1. Predicate search and comparison matrix.  
2. Completion of the missing evidence items.  
3. Draft of the 510(k) submission incorporating the sections outlined.  

If any of the escalation triggers are hit, raise to senior RA leadership for pathway reassessment.

---

### 7. Peer‑Review Prompt  

> *Colleague, please review the assumptions made about classification (§ 892.2050), the completeness of the evidence list, and any jurisdiction‑specific items that may be missing (e.g., UDI plan, QMSR compliance). Highlight any gaps in source coverage or potential EU/Korean regulatory bleed‑through.*

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

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

## ra_eu

### kb-eval-20261022-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7b5d23aec1907098", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7b5d23aec1907098`
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

> **Regulatory Draft – Notified‑Body Query Response**  
*(Prepared for the EU MDR 2017/745 pathway)*  

---

## 1. Scope of the Request  

The NB’s question concerns the **classification and conformity‑assessment route**, together with the **evidence package** that must be assembled in the Technical Documentation (TD) before submission. No device‑specific description was supplied; therefore the draft outlines the *general* requirements and flags the information gaps that must be filled by the manufacturer before a definitive judgment can be made.

---

## 2. Classification & Conformity‑Assessment Route  

| Step | Action | Regulatory reference |
|------|--------|-----------------------|
| **2.1 Identify intended purpose & mode of action** | Needed to select the appropriate rule in Annex VIII (e.g., Rule 9, 10, 11, 17…) | *Annex VIII – Classification rules* |
| **2.2 Apply the rule → assign Class I–III** | If the device is non‑sterile, non‑measuring and not reusable surgical → Class I; otherwise follow the rule outcome (e.g., Rule 9 ⇒ IIa/IIb). | *Annex VIII – Rule tables* |
| **2.3 Determine conformity‑assessment route (Art 52)** | • **Class I (non‑sterile, non‑measuring, non‑reusable‑surgical):** Self‑declaration – technical documentation + EU DoC (no NB involvement).  <br>• **Is / Im / Ir:** Annex IX Chapters I & III *or* Annex XI Part A (NB limited scope).  <br>• **Class IIa:** Annex IX (full QMS + TD assessment) – NB required.  <br>• **Class IIb / III:** Either (i) Annex IX (full QMS + TD) *or* (ii) Annex X (type‑examination) **combined with** Annex XI (production conformity verification). | *Art. 52(3‑7)*; *Annex IX*, *Annex X*, *Annex XI* |
| **2.4 NB involvement** | Mandatory for Class Is/Im/Ir, IIa, IIb and III under the routes above. | *Art. 52 & 53* |

> **Current status:** *No intended purpose or rule identifier is present in the source excerpts.* → **Missing information – see Section 4.1**.

---

## 3. Required Evidence (Technical Documentation – Annex II)

The TD must contain the six sections listed in Annex II §1‑6. The mapping supplied by the source (Excerpt [1]) confirms the correspondence between MDR Annex II clauses and the typical US/Korean artefacts. This table can be used as a checklist:

| Annex II clause | Content required | Example evidence (per source) |
|------------------|------------------|------------------------------|
| **§1 Device description** | Intended purpose, indications, mode of action, variants, accessories. | – |
| **§2 Labeling & IFU** | Labels, symbols, Instructions for Use (IFU) in required languages. | “Labeling” column shows alignment with FDA 21 CFR 801 and MFDS Chapter 3. |
| **§3 Design & Manufacturing** | Device architecture, materials, manufacturing processes, specifications. | Corresponds to “Design & Manufacturing” / “제2장 구조·원재료·제조방법”. |
| **§4 GSPR checklist** | Statement of compliance with each of the 23 General Safety and Performance Requirements (Annex I). | Linked to “Safety requirements” / “510(k) SE comparison + Performance testing”. |
| **§5 Risk Management** | Full risk management file per ISO 14971 (risk analysis, evaluation, controls, residual‑risk acceptance). | Mentioned as “Risk Management File (ISO 14971…)”. |
| **§6 Verification & Validation** | V&V plan and reports demonstrating that the device meets its specifications and intended performance. | “Verification & Validation” / “V&V Reports (DHF)”. |

Additional mandatory annexes for MDR:

| Requirement | Where it belongs | Reference |
|-------------|------------------|-----------|
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (kept current under Art. 61). | *Art. 61; Annex XIV Part A* |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Annex XIV Part B. | *Annex XIV Part B* |
| **Post‑Market Surveillance (PMS) system & plan** | Art. 83 (system), Art. 84 (plan). | *Art. 83–84* |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | Art. 86 (frequency: annually for IIb/III, every 2 y for IIa). | *Art. 86(1‑2)* |
| **EU Declaration of Conformity** | Art. 19; content defined in Annex IV. | *Art. 19; Annex IV* |
| **Summary of Safety and Clinical Performance (SSCP)** – for Class III & implantables | Art. 32. | *Art. 32* |

---

## 4. Gaps / Missing Information  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **4.1 Intended purpose, indications and mode of action** | Determines the applicable rule in Annex VIII → class assignment. | Manufacturer must provide a clear “Intended Use” statement (including patient population, clinical setting, intended users). |
| **4.2 Exact classification rule number** | Needed to cite the rule (e.g., Rule 9) and justify class. | Map the intended purpose to Annex VIII rules; supply the rule reference. |
| **4.3 Clinical evidence** – type of data (clinical investigations, literature, equivalence) | Determines whether a full CER & PMCF are required or if a “clinical similarity” argument suffices. | Provide a clinical evaluation plan and any existing clinical investigation results or literature reviews. |
| **4.4 Device variants / accessories list** | Required for §1 and for the risk‑management file (risk propagation). | Submit a complete Bill of Materials (BoM) and variant matrix. |
| **4.5 Language compliance** – confirm which EU languages are required beyond English | Annex II states “minimum English; NB may require additional languages.” | Clarify target Member States and provide translated labeling/IFU where needed. |
| **4.6 Confirmation of QMS certification (ISO 13485:2016) & scope** | Mandatory for any route involving a Notified Body (Annex IX, X). | Submit the current ISO 13485 certificate with scope covering the device. |

> **Note:** The source excerpts only provide a generic mapping table (Excerpt [1]) and a high‑level overview of MDR applicability (Excerpt [2]). No device‑specific identifiers or regulatory numbers appear; therefore no instance‑identifier citations are inserted.

---

## 5. Recommended Risk Controls  

| Area | Control measure | Regulatory basis |
|------|----------------|-------------------|
| **Risk Management** | Complete ISO 14971:2019 risk management file, with risk analysis, evaluation, control measures, residual‑risk acceptance justification. | *Annex I §3 (RMF); Annex II §5* |
| **Usability / Human Factors** | Apply IEC 62366‑1:2020 usability engineering process; incorporate findings in the risk analysis. | *Annex I §17 (Electronic programmable systems & software)* |
| **Software Lifecycle (if applicable)** | Follow IEC 62304:2006+A1:2015 for any software component considered a device. | *Annex I §17* |
| **Electrical Safety / EMI** | Demonstrate conformity to IEC 60601‑1 series (e.g., 60601‑2‑54 for X‑ray if relevant). | *Annex I §16 (Radiation protection)* |
| **Biocompatibility** | Conduct ISO 10993‑1:2018 assessments per material contact time and nature. | *Annex I §§20‑22* |
| **Performance Testing** | Provide bench testing, validation data, and, where required, clinical performance testing (e.g., for active therapeutic devices). | *Annex II §4 GSPR checklist; Annex XIV Part A* |

---

## 6. Human‑Escalation Triggers  

The following events should be escalated to the RA manager or legal/compliance team before any NB submission:

1. **Uncertainty in classification** (no rule can be confidently assigned).  
2. **Absence of a clinical evaluation strategy** for Class IIa/IIb/III devices.  
3. **Missing ISO 13485 certification** when an NB route demands it (Annex IX or X+XI).  
4. **Inadequate PMS plan** – e.g., no defined post‑market surveillance system per Art. 83–84.  
5. **Labeling language gaps** for the intended EU market(s).  
6. **Discrepancy between declared GSPR compliance and supporting evidence** (e.g., performance test missing, risk analysis not covering identified hazards).  

Escalation should be documented in the project’s risk register and a decision‑record issued before proceeding.

---

## 7. Summary Judgment  

*Based on the information currently available, the device cannot yet be classified or assigned a definitive conformity‑assessment route.* The manufacturer must furnish:

- A precise **intended purpose** that can be mapped to an Annex VIII rule,
- The corresponding **classification rule number**, and
- The **clinical evidence dossier** (CER/PMCF) appropriate to the determined class.

Once these items are provided, the TD checklist in Annex II (sections 1‑6) can be populated, the required PMS system set up (Art. 83‑86), and the correct NB route (Annex IX or Annex X + XI) selected per Art. 52.

---

## 8. Peer‑Review Prompt  

> **To a fellow RA colleague:** Please review the assumptions made in Sections 2–5, especially the interpretation of the “generic mapping table” from source excerpt [1]. Verify that no device‑specific regulatory identifiers have been inadvertently omitted and confirm whether any additional EU national requirements (e.g., language or Notified Body‑specific annexes) might affect the evidence package for the anticipated classification.  

--- 

*End of Draft.*

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

### kb-eval-20261022-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "62f9ee40c9cb05a0", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `62f9ee40c9cb05a0`
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

> **Regulatory Draft – Determination of Classification, Conformity‑Assessment Route and Evidence Package**  

---

### 1 Device Information required (currently missing)

| Item | Why needed | MDR reference |
|------|------------|----------------|
| **Trade name / model number** | Forms the basis for TD identification and traceability. | Art. 10(1), Annex II §1 |
| **Intended purpose & indications for use** | Determines classification rule (Annex VIII) and clinical‑evaluation scope. | Art. 2(1); Annex VIII |
| **Target patient population / user group** | Impacts risk analysis, PMS plan and labeling. | Annex I §22; Art. 84 |
| **Key design & operating principles (e.g., active, radiological, software)** | Needed to select the correct classification rule(s) (Rule 9‑11, 17 etc.) and applicable harmonised standards. | Annex VIII, Rules 9–11, 17 |
| **Material composition / sterilisation method** (if relevant) | Required for biocompatibility & risk management evidence. | ISO 14971 §3; Annex I §§4‑6 |
| **Device life‑cycle (single‑use vs reusable)** | Influences GSPR §§5‑7 and PMS obligations. | Annex I §§5‑7 |

> **Action:** The manufacturer must supply the above data before any classification or NB submission can be finalised.

---

### 2 Provisional Classification & Conformity‑Assessment Route (to be confirmed)

| Step | Procedure | MDR citation |
|------|-----------|--------------|
| **a. Apply Annex VIII classification rules** based on the intended purpose once clarified. | Identify rule(s) (e.g., Rule 9 for active therapeutic, Rule 10 for diagnostic, Rule 11 for software). | Annex VIII – “Classification Rules” |
| **b. Determine device class (I, Is/Im/Ir, IIa, IIb, III)** | Use the outcome of Step a. | Art. 52(1‑5) |
| **c. Select conformity‑assessment route** | • Class I (non‑sterile, non‑measuring): self‑declaration – Art. 52(7). <br>• Classes Is/Im/Ir: Annex IX limited scope or Annex XI (limited NB involvement). <br>• Class IIa: Annex IX **or** Annex II + III + Annex XI §10/§18. <br>• Class IIb / III: Annex IX **or** Annex X + Annex XI. | Art. 52 (paragraphs 3‑7) together with the relevant Annexes (IX, X, XI). |

> **Current status:** Classification cannot be assigned until the missing device information is provided.

---

### 3 Evidence Package required for Technical Documentation (TD)

| TD Section (Annex II §1‑6) | Required evidence (per MDR & source [1]) | Comments / gaps |
|----------------------------|-------------------------------------------|-----------------|
| **1. Device description & specification** | • Trade name, model, variants.<br>• Intended purpose, indication, user group.<br>• Classification rule justification. | *Missing* – requires manufacturer input. |
| **2. Information on the manufacturer** | Legal entity, address, authorised representative (if any). | Usually available; verify completeness. |
| **3. Design & manufacturing information** | • Design dossier, drawings, bill of materials.<br>• Process flow, manufacturing sites, quality‑system certificates (ISO 13485:2016).<br>• Verification & validation (V&V) results. | V&V data expected from R&D (source step 2). |
| **4. General Safety & Performance Requirements (GSPR)** | Mapping of device characteristics to the 23 GSPR (§1‑9, §10‑22, §23). *Source [1] Step 3 – “GSPR 매핑 완성”.* | GSPR check‑list required; mapping not yet supplied. |
| **5. Benefit‑risk analysis & risk management** | • Risk Management File (RMF) complying with ISO 14971:2019 (Annex I §3). *Source [1] Step 5 – “위험관리 파일 통합”.* | RMF draft needed; residual‑risk acceptance criteria not yet shown. |
| **6. Clinical evaluation** | • Clinical Evaluation Report (CER) per Annex XIV Part A, kept up‑to‑date (Art. 61). *Source [1] Step 4 – “임상평가 보고서(CER) 작성·갱신”.* | Requires clinical data, literature review, PMCF plan. |
| **7. Post‑market surveillance** | • PMS Plan (Art. 84) and PMS Report/PSUR (Art. 85‑86). *Source [1] Step 6 – “PMS 계획서 작성”.* | PMS plan draft required; PSUR schedule depends on class. |

> **Additional annexes to reference:**  
> - Annex I (GSPR) §§1‑9 (risk‑management), §23 (labeling).  
> - Annex III (post‑market surveillance technical documentation).  

---

### 4 Risk Controls (to be demonstrated)

| Control | MDR / GSPR basis | Expected evidence |
|---------|------------------|-------------------|
| **Risk management process** (risk analysis, evaluation, control) | Annex I §3; ISO 14971:2019 | RMF with risk register, mitigations, residual‑risk acceptance. |
| **Usability / use‑error mitigation** | Annex I §5 (use error); IEC 62366‑1 (2020) | Usability engineering file, Human Factors validation results. |
| **Sterility & re‑usability controls** (if applicable) | Annex I §§4‑6; ISO 14937 (sterilisation). | Sterilisation validation reports, reusable instrument maintenance plan. |
| **Electromagnetic / radiation safety** (X‑ray systems) | Annex I §16 (radiation); IEC 60601‑2‑54, IEC 60601‑1. | Test reports for emission limits, shielding calculations. |
| **Software lifecycle management** (if software is a device) | Annex I §17; IEC 62304. | Software development plan, verification & validation documentation. |

> **Current status:** No risk‑management artefacts have been attached to the submission record – “위험관리 보고서” is listed as an output but not yet produced.

---

### 5 Missing Information / Open Items (to be resolved before NB submission)

| Item | Reason for requirement | Source reference |
|------|------------------------|------------------|
| Complete **device description & intended use** | Needed to apply Annex VIII classification rule. | Art. 2(1); Annex VIII |
| **Classification rule justification** (e.g., Rule 9, 10, 11, 17) | Determines class and NB involvement. | Annex VIII |
| **Clinical data set** (clinical investigations, literature, post‑market clinical follow‑up) | Required for CER & PMCF. | Annex XIV Part A; Art. 61 |
| **PMS Plan details** (activities, reporting cadence, responsible persons) | Mandatory under Art. 84 and to feed PSUR/PSUR. | Art. 84; source step 6 |
> **Action‑point:** The manufacturer must populate the TD checklist (F‑MDR‑TD‑CHK‑001 – see source [2]) with the above items and submit a revised draft for review.

---

### 6 Human‑Escalation Triggers

| Trigger | Escalation to Human RA Lead | Reason |
|---------|----------------------------|--------|
| **Classification cannot be resolved** after request for intended purpose. | Immediate – decision on NB route depends on class. |
| **Absent or outdated CER** (no clinical data, no literature search). | Immediate – MDR Art. 61 requires a current CER; NB will reject. |
| **Risk Management File incomplete** (missing risk acceptability justification). | Immediate – non‑conformity with Annex I §3 and ISO 14971. |
| **PMS Plan not submitted** or lacking key elements (e.g., defined reporting intervals). | Immediate – Art. 84 compliance required before conformity assessment. |
| **GSPR mapping gaps** (unchecked requirements). | Escalate to QA for cross‑check with GSPR checklist (source [1] step 3). |
| **No evidence of QMS certification (ISO 13485:2016)** where NB involvement is mandatory (Class IIa–III). | Immediate – Annex IX requires a certified QMS. |

---

### 7 Peer‑Review Prompt

*“Please review the assumptions made above, especially concerning the classification pathway and evidence requirements. Verify that all cited MDR provisions (Art. 52, Annex VIII, Annex I §§1‑9, Art. 84‑86) are correctly applied to a generic X‑ray system as implied by source [2]. Identify any jurisdiction‑specific gaps (e.g., UDI, AI Act overlap) that may affect the TD completeness.”*

--- 

**Summary Judgment:**  
At present the device cannot be classified nor can a conformity‑assessment route be definitively selected because critical information on intended purpose, design characteristics and clinical evidence is missing. The manufacturer must furnish the items listed in Section 1 before any NB engagement can proceed. All subsequent documentation (GSPR mapping, RMF, CER, PMS Plan) should follow the structure outlined in Sections 3‑5 to satisfy MDR technical‑documentation obligations.

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

### kb-eval-20261022-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "641c6d1e76d432be", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `641c6d1e76d432be`
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

> **Regulatory Draft – Response to Notified Body Deficiency Letter**  
*Prepared for the manufacturer of a diagnostic‑radiology X‑ray system (including source, detector and associated software).*

---

### 1. Device classification & applicable conformity‑assessment route  

| Item | Determination | Legal basis |
|------|---------------|-------------|
| **MDR Rule** | **Rule 10** – “Active devices for diagnosis and monitoring” that emit ionising radiation. | Annex VIII, Rule 10 (MDR 2017/745) |
| **Class** | **IIb** – active X‑ray equipment emitting ionising radiation is placed in Class IIb under Rule 10. | Rule 10 → Class IIb |
| **Conformity‑assessment route** | **Annex IX (full QMS + technical‑documentation assessment) with NB involvement**.  The manufacturer may also use the alternative **Annex X + Annex XI (type‑examination + production conformity verification)**; the choice must be confirmed in the EU declaration of conformity. | Art. 52(4) MDR – NB mandatory for Class IIb; Annex IX alone or Annex X + XI are the only permissible combinations for this class. |

> **Note** – The deficiency letter does not indicate which route was selected; the response must confirm the chosen route and provide the corresponding evidence.

---

### 2. Evidence required by the MDR (summary of mandatory files)

| Category | Required artefact(s) | Core content & relevant references |
|----------|----------------------|-------------------------------------|
| **Technical Documentation** (Annex II §6.1) | – Device description, intended purpose, variants<br>– Design‑manufacturing information<br>– Verification & validation data (including IEC 60601‑2‑54 electrical safety, IEC 62220‑1‑1 DQE test)<br>– Labeling & IFU (Annex I §23) | Annex II, Annex IX (QMS), ISO 14971:2019 risk management |
| **Clinical Evaluation Report (CER)** | Updated CER (latest revision attached as Annex A). Must demonstrate clinical equivalence and safety/performance for the whole system. | Annex XIV Part A; Art. 61 MDR – keep current |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | PMCF plan (Annex XIV Part B) and interim evaluation report covering at least 2 years of clinical use or a defined number of examinations. | Annex XIV Part B; Art. 83–86 MDR |
| **Risk Management File (RMF)** | ISO 14971:2019 analysis, risk control measures for radiation exposure, interlocks, dose‑monitoring, software hazards (IEC 62304, IEC 62366‑1). | Annex I §§3‑8; Art. 10(9) MDR |
| **Usability/ Human Factors** | Usability engineering file demonstrating compliance with IEC 62366‑1:2020 (lay‑person use not expected but ergonomics of positioning & control must be shown). | Annex I §22; IEC 62366‑1 |
| **Software Documentation** (if applicable) | Software development lifecycle documentation – IEC 62304:2006+A1:2015, verification/validation test reports. | Annex I §17; IEC 62304 |
| **Essential‑principles testing** | • Radiation protection – IEC 60601‑2‑54 & IEC 62220‑1‑1 DQE results (DQE(0) ≥ 65 %).<br>• Electrical safety, electromagnetic compatibility. | Annex I §16; IEC 60601 series |
| **Declaration of Conformity** | EU DoC with full content per Art. 19 & Annex IV. | Art. 19 MDR; Annex IV |
| **Summary of Safety and Clinical Performance (SSCP)** – only if the device is an implantable or class‑III; not required for a Class IIb diagnostic X‑ray system. | — | — |

---

### 3. Gaps identified in the current dossier (as inferred from the deficiency letter)

| Missing / insufficient item | Reason it is required | Evidence needed to close the gap |
|-----------------------------|----------------------|-----------------------------------|
| **Full CER supporting clinical equivalence** – only a revised “CER Rev 3” is attached; no traceability of clinical data sources, nor justification that DQE alone proves equivalence. | Clinical evaluation must demonstrate safety *and* performance in the intended use environment (Annex XIV Part A). | • Full literature review and/or comparative clinical study linking DQE ≥ 65 % to diagnostic accuracy and patient dose.<br>• Summary of any post‑market surveillance or real‑world data. |
| **PMCF plan & interim report** – not mentioned in the submission. | MDR requires a PMCF for Class IIb (Art. 83–86). | • Detailed PMCF protocol (objectives, population, endpoints, timelines).<br>• Interim results covering at least 12 months of use or ≥ 10 000 examinations. |
| **Risk Management File** – only implied through “clinical equivalence” statement; no explicit RMF linking DQE performance to radiation risk reduction. | Annex I §3‑8 and ISO 14971 demand that residual risks be identified, evaluated and controlled. | • Updated RMF showing: <br> – Hazard identification for ionising radiation.<br> – Control measures (automatic exposure control, interlocks, shielding).<br> – Residual risk evaluation with benefit‑risk analysis (Art. 61 MDR). |
| **Usability/ Human Factors documentation** – absent. | Annex I §22 requires assessment of use errors that could affect safety/performance. | • Usability engineering file per IEC 62366‑1, including user‑interface validation and identified use‑error mitigations. |
| **Software development evidence (if software is a device)** – no reference to IEC 62304 compliance. | Annex I §17 mandates conformity of medical device software. | • Software life‑cycle documentation, verification & validation test reports. |
| **Electrical safety / EMC testing** – only DQE test report provided. | IEC 60601‑2‑54 (radiography) is mandatory for X‑ray equipment; compliance must be shown in the technical file. | • Test reports for electrical safety and electromagnetic compatibility. |
| **Labeling & IFU** – no copies supplied. | Annex I §23 requires complete information supplied with the device. | • Final labeling, symbols (IEC 60601‐2‑54), instructions for use, contraindications, radiation safety notices. |
| **Declaration of Conformity** – not referenced in the letter. | Art. 19 MDR & Annex IV demand a signed DoC before CE marking. | • Completed EU DoC with reference to all applicable conformity‑assessment procedures (Annex IX or X+XI). |

---

### 4. Recommended risk controls to address identified gaps

1. **Radiation dose mitigation** – implement and document an *Automatic Exposure Control* (AEC) algorithm; verify against IEC 60601‑2‑54 test data.  
2. **Interlock & shielding verification** – provide evidence that interlocks prevent accidental exposure; include mechanical safety tests.  
3. **Clinical performance linkage** – supplement DQE results with a *clinical sensitivity/specificity* study (e.g., detection of lung nodules) to demonstrate diagnostic benefit.  
4. **Software safeguards** – if software determines exposure parameters, apply IEC 62304‑compliant error handling and periodic security updates.  
5. **Usability measures** – conduct formative/usability testing with intended operators (radiographers); record critical task success rates and incorporate design changes where failure > 3 %.  

All controls must be recorded in the RMF and cross‑referenced to the relevant GSPR clauses (Annex I §§16, 17, 22).

---

### 5. Action items & human‑escalation triggers

| Step | Responsible party | Deadline* | Trigger for escalation |
|------|-------------------|-----------|------------------------|
| **1 – Confirm conformity route** (Annex IX vs Annex X+XI) and update declaration accordingly. | RA Lead | 5 days after receipt of NB letter | If not clarified → Senior Regulatory Manager to approve alternative route. |
| **2 – Complete CER** with full clinical data package, referencing literature & any post‑market evidence. | Clinical Affairs + RA | 15 days | Delay > 7 days → Project Management escalation; possible NB deadline breach. |
| **3 – Draft PMCF plan & collect interim data** (≥ 12 months or 10 000 exams). | Post‑Market Surveillance Team | 20 days | Inability to meet sample size → Legal/Quality Manager review for risk‑based justification. |
| **4 – Update RMF** with radiation‑risk analysis, controls, residual‑risk evaluation. | Quality / Risk Management | 12 days | Missing or inconsistent risk statements → Immediate QA escalation. |
| **5 – Assemble missing test reports** (IEC 60601‑2‑54, IEC 62220‑1‑1, EMC). | Engineering & Test Labs | 10 days | Failure to obtain report → Procurement/Contract Management involvement for third‑party lab. |
| **6 – Produce labeling, IFU, and final DoC** (Annex IV). | Documentation Specialist | 14 days | Non‑conformity with Annex I §23 → Senior Regulatory Manager sign‑off required before submission. |
| **7 – Submit complete remedial dossier to NB** (cover letter referencing each deficiency item). | RA Lead | 30 days (or NB‑specified deadline) | Missed deadline → Formal escalation to Business Unit Head & potential market launch delay notification. |

\*All dates are indicative; the exact NB response timeline must be respected as stipulated in the deficiency letter.

---

### 6. Peer‑review request  

> **To:** RA peer (e.g., *Anna Müller, MD‑Regulatory Affairs*)  
> **Please review** this draft for:  
> - Completeness of identified gaps versus the source excerpts and MDR requirements.  
> - Correctness of the classification & conformity‑assessment route selection (Rule 10, Class IIb, Annex IX vs X+XI).  
> - Any jurisdiction‑specific nuances that may affect the evidence package (e.g., additional French “Déclaration d’Exigence”).  
> – Whether any further IEC/ISO standards (e.g., IEC 60601‑2‑54 amendment) should be added.  

Your comments and suggested amendments are requested within **5 business days** so that we can finalise the NB response before the statutory deadline.

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

### kb-eval-20261022-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b65cf725d895aa37", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b65cf725d895aa37`
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

> **Regulatory Draft – X‑ray Generation Device (and associated SaMD) under EU MDR 2017/745**  

---

### 1. Scope & Intended Use (as inferred from source)

| Element | Description |
|---|---|
| **Device family** | – X‑ray generation unit (produces ionising radiation for diagnostic imaging).<br>– Medical‑device software (SaMD) that receives the image data and provides diagnostic decision support. |
| **Intended purpose** | “To generate X‑ray beams for radiographic / fluoroscopic examinations of patients” (hardware) and “to analyse acquired images and provide diagnostic suggestions to the treating clinician” (software). <br>*Exact wording not supplied in source – must be confirmed.* |

> **Action:** Obtain the manufacturer’s finalized Intended Purpose statements before any classification decision is finalised.  

---

### 2. Classification

| Component | Applicable MDR rule (Annex VIII) | Resulting class* |
|---|---|---|
| X‑ray generator (emits ionising radiation for diagnosis) | **Rule 10** – “Active devices that emit ionising radiation for diagnostic or therapeutic purposes” | **Class IIb** (source excerpt confirms: *“X‑ray 발생장치 → Class IIb”*) |
| SaMD (diagnostic decision support) | **Rule 11** – “Software providing information used to take a diagnostic decision”. The impact of the software on patient care (diagnosis that may lead to immediate treatment) places it in **Class IIb**. If the decision influence is limited to non‑critical advice, it could be Class IIa; this must be clarified with the manufacturer. |

\*MDR classification table: Art. 52(4) – devices classified as IIb require a conformity assessment involving a Notified Body (NB).  

> **Citations:** Rule 10 & Rule 11 of Annex VIII; Art. 52(4) MDR 2017/745.  

---

### 3. Conformity‑Assessment Route

| Class | Applicable route (Art. 52) | NB involvement |
|---|---|---|
| **IIb** (both hardware and software) | **Annex IX** – Full quality‑management system assessment + technical‑documentation review *or* **Annex X + Annex XI** – Type‑examination plus production conformity verification. The manufacturer may choose either route, but NB involvement is mandatory for all steps. | Required (full audit of QMS &/or type‑examination). |

> **Citation:** Art. 52(4) MDR 2017/745; Annex IX; Annex X + XI.  

---

### 4. Evidence Package Required for NB Submission

| Requirement | Where it belongs in the Technical Documentation (TD) | Key supporting standards / guidance |
|---|---|---|
| **Device Description & Specification** (design, variants, accessories) | Annex II §1‑2 | – |
| **Intended Purpose & Indications** | Annex II §3 | – |
| **Labeling & IFU** (including radiation safety info) | Annex II §6; **Annex I §23** (information supplied with the device) | – |
| **Risk Management File (RMF)** – hazard analysis, risk evaluation, residual‑risk acceptability | Annex II §5; **Annex I §3‑9** (risk‑management system) | ISO 14971:2019 (risk management) |
| **Clinical Evaluation Report (CER)** – state‑of‑the‑art review, clinical data, equivalence justification | **Annex XIV Part A** (kept current under Art. 61) | MDCG 2023‑X guidelines; MEDDEV‑2.7/1 revision 4 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | **Annex XIV Part B** | – |
| **Post‑Market Surveillance (PMS) System & Plan** | Art. 83 (system); Art. 84 (plan) | – |
| **Periodic Safety Update Report (PSUR)** – annually for Class IIb | Art. 86(1)(a‑c) (benefit–risk, PMCF findings, sales/using population) | – |
| **Usability Engineering File** (IEC 62366‑1:2020) | Sub‑section of Annex II §4 (design & manufacture) | IEC 62366‑1 |
| **Software Development Lifecycle Documentation** (IEC 62304:2006+A1:2015) | Annex II §4 / Annex III (if software is a separate device) | IEC 62304 |
| **Electrical Safety & Electromagnetic Compatibility** (IEC 60601‑2‑54 for X‑ray equipment) | Annex II §4 (verification & validation) | IEC 60601‑2‑54 |
| **Radiation Protection Evidence** (dose measurements, shielding calculations) | Annex I §16 (protection against radiation) | IEC 60601‑2‑54, IEC 62220‑1‑1 (DQE) |

> **Note:** The source does not supply concrete document numbers or dates; each of the above items must be produced and cross‑referenced in the TD.  

---

### 5. Gaps / Missing Information (to be resolved before NB submission)

| Gap | Why it matters | Required action |
|---|---|---|
| **Exact Intended Purpose statements** for both hardware and SaMD | Drives classification, risk analysis, labeling, clinical evidence scope. | Obtain from the manufacturer’s product specification dossier. |
| **Clinical data source list** (clinical investigations, literature, equivalence) | Needed for CER (Art. 61 & Annex XIV Part A). | Compile and assess; if no sufficient device‑specific data exist, plan a clinical investigation per MDCG 2020‑13. |
> **No specific identifier found in source — verify separately** (e.g., MDR article/section numbers already cited are framework references; any predicate or registration number is absent.)  
| **PMCF objectives & methodology** (population size, follow‑up duration) | Required for Annex XIV Part B and PSUR. | Draft a PMCF plan aligned with risk controls; get sponsor sign‑off. |
| **Labeling / IFU content** (including radiation warnings, user instructions) | Must satisfy Annex I §23 & GSPR checklist. | Produce draft labeling; perform usability validation per IEC 62366‑1. |
| **Risk control measures for software decision impact** (e.g., error handling, fail‑safe states) | Essential to demonstrate residual risk acceptability (§8 GSPR). | Document in RMF and verify by software verification/validation activities. |
| **PMS system architecture & reporting procedures** | Art. 83–86 require a functional PMS that can generate PSURs. | Implement a PMS database; define SOPs for trend analysis (Art. 88). |
| **Declaration of Conformity (DoC) content** | Must include mandatory elements per Art. 19 & Annex IV. | Prepare DoC once all other documentation is complete. |

---

### 6. Risk‑Control Summary (high‑level)

1. **Radiation hazards** – Shielding design, interlocks, dose‑monitoring, compliance with IEC 60601‑2‑54 and Annex I §16.  
2. **Software decision‑support errors** – Fault‑tree analysis of incorrect output; implementation of IEC 62304 development lifecycle; verification that erroneous outputs trigger user alerts (risk control per ISO 14971).  
3. **Electrical safety & EMC** – Conformance to IEC 60601‑1 series, including IEC 60601‑2‑54 testing.  
4. **Usability / Use‑error** – Human‑factors analysis (IEC 62366‑1) to mitigate incorrect set‑up or exposure parameters.  
5. **Residual risk evaluation** – Documented in RMF; must show that residual risks are outweighed by clinical benefits (Annex I §8).  

---

### 7. Human‑Escalation Triggers

| Situation | Trigger & Rationale |
|---|---|
| **Unclear intended purpose or scope** | Classification may change (Rule 10 vs Rule 11 impact); must be resolved by senior RA before proceeding. |
| **Insufficient clinical evidence** | If no adequate device‑specific data, a clinical investigation is mandatory – decision to launch a study must be approved by the sponsor’s Clinical Lead. |
| **Unmitigated high‑severity risk** (e.g., radiation overexposure not controllable) | Must be addressed prior to any conformity‑assessment step; escalation to Head of Regulatory & Safety. |
| **PMS system not demonstrably functional** (no incident capture, no trend analysis) | NB will reject submission – escalates to Project Manager for resource allocation. |
> **Escalation path:** RA analyst → Senior Regulatory Affairs Lead → Compliance Officer (if risk‑acceptance decision required).  

---

### 8. Regulatory Judgment

- **Classification:** X‑ray generator – Class IIb (Rule 10). SaMD – likely Class IIb under Rule 11 (subject to confirmation of clinical impact).  
- **Conformity‑Assessment Route:** Choose either **Annex IX** full QMS & TD assessment *or* **Annex X + XI** type‑examination + production verification. NB involvement is mandatory.  
- **Evidence Package:** Must contain complete technical documentation (Annex II), a robust CER, PMCF plan/report, PMS system & PSUR, RMF, and all applicable IEC/ISO supporting documents.  
- **Current status:** Several critical pieces (intended purpose, clinical data, PMCF details, labeling) are missing; the dossier is not ready for NB audit.  

**Immediate next steps:** Collect the missing manufacturer information, draft the CER & PMCF plan, and verify software classification before finalising the route.

---

### 9. Peer‑Review Prompt

> *Colleague, please review: (a) the assumed impact level of the SaMD under Rule 11 – could a Class IIa justification be defensible?; (b) completeness of the listed evidence items against the latest MDCG guidance for X‑ray devices; and (c) any jurisdiction‑specific nuances (e.g., transition periods from Regulation 2023/607) that may affect timing or documentation requirements.*  

--- 

*Prepared by Theo – EU MDR Regulatory Affairs Specialist*

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

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261022-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "02dd686f6de603af", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `02dd686f6de603af`
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

> **Regulatory Draft – X‑ray Medical Device (Ionising‑radiation equipment)**  
*Prepared for internal response to the Notified Body (NB) inquiry*  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Intended purpose** – “diagnostic X‑ray system for radiography / radioscopy” (ionising‑radiation equipment). | **Class IIb** (active device that emits ionising radiation) | Rule 10 of Annex VIII, MDR 2017/745 → **Rule 10 ⇒ Class IIb**. |
| **Conformity‑assessment route** – Full NB involvement (type‑examination & production verification). | **Annex X + Annex XI** (EU type‑examination together with production conformity verification) | Art. 52(4) MDR 2017/745, which assigns Class IIb to the “Annex X + XI” route. |
| **NB designation** – Verify that the selected NB is authorised for the MDxxxx code (MDR scope). | *Action*: Search NANDO database for the exact MD‑code and confirm the NB’s designated range. | No specific identifier in source – verify separately. |

> **Citation** – Rule 10, Annex VIII; Art. 52(4) MDR 2017/745.  

---

### 2. Required Evidence Package (per NB expectations)

| Area | Documents / Data | Regulatory reference |
|------|------------------|-----------------------|
| **Technical Documentation (TD)** – complete according to Annex II §6.1, including: <br>• Device description & intended use <br>• Design & manufacturing information <br>• Verification & validation reports <br>• Clinical Evaluation Report (CER) | Annex II (sections 1‑6); **Annex XIV Part A** for CER (kept current under Art. 61). |
| **Risk Management File (RMF)** – ISO 14971:2019 implementation covering risk analysis, evaluation, control and residual‑risk justification. | Annex I §§3‑9 (risk management system). |
| **Clinical Evidence / PMCF** – • Clinical Evaluation Report (state of the art, clinical data) <br>• Post‑Market Clinical Follow‑up (PMCF) plan & interim/final reports | **Annex XIV Part A** (CER) and **Part B** (PMCF). |
| **Post‑Market Surveillance (PMS)** – • PMS system description (Art. 83) <br>• PMS plan (Art. 84) <br>• Periodic Safety Update Report (PSUR) for Class IIb, annually (Art. 86) | Art. 83‑86 MDR. |
| **Regulatory‑type examination** – • Type‑examination report issued by the NB (Annex X). | Annex X – type‑examination requirements. |
| **Production conformity verification** – • Certificate of compliance for each batch/lot (Annex XI). | Annex XI – production conformity verification. |
| **QMS evidence** – • ISO 13485:2016 certified QMS, audit reports, corrective‑action records. | Art. 10(9) MDR; NB will assess via QMS audit (see §2 of source). |
| **IEC standards compliance** – • IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy) <br>• IEC 60601‑1 (general safety) <br>• IEC 62304 (software lifecycle, if applicable) | No specific identifier in source – verify separately. |
| **Labelling & IFU** – Conform to Annex I §23 (information supplied with the device). | Annex I §23. |

---

### 3. Gaps / Missing Information (as identified from the NB‑question context)

1. **Exact MDR product‑code (MDxxxx)** – placeholder in source; need concrete code from NANDO.  
2. **Full Intended‑Use Statement** – must be precise (e.g., “diagnostic radiography of adult patients, up to 150 kV”).  
3. **Clinical data package** – no evidence supplied yet whether a CER exists or if clinical investigation is required under Rule 10.  
4. **IEC 60601‑2‑54 test reports** – conformity assessment results not referenced.  
5. **Software classification** (if any) – need to confirm whether software falls under Rule 11 and the resulting class.  
6. **PMS plan specifics** – frequency of data collection, responsible persons, trending methodology absent.  
7. **Non‑conformity response evidence** – only listed as “Non-conformity 대응 자료” without actual remediation records.  

*Action*: Request the above items from the device manufacturer before NB audit.

---

### 4. Required Risk Controls (aligned with GSPR)

| Requirement | Control measure |
|-------------|-----------------|
| **Radiation protection** – limit patient dose, ensure shielding, interlocks. | Conform to Annex I §16 (radiation protection) and IEC 60601‑2‑54 performance criteria. |
| **Software safety** (if applicable). | Apply Annex I §17 & IEC 62304 for software development lifecycle; perform usability validation per IEC 62366‑1. |
| **Use‑error mitigation** – ergonomic design, clear labeling. | Annex I §5 (use‑error risk control) and IFU compliance with §23. |
| **Residual risk justification** – benefit‑risk analysis documented. | Annex I §8 (overall risk/benefit). |
| **Device lifetime & maintenance** – define service life, periodic safety checks. | Annex I §6 (device lifetime) and IEC 60601‑1 maintenance requirements. |

---

### 5. Human‑Escalation Triggers  

| Trigger condition | Escalation action | Responsible party |
|-------------------|------------------|-------------------|
| **Missing MDR product‑code or NANDO confirmation** | Halt NB submission; senior RA to obtain official code & update dossier. | RA Lead |
| **Absence of a validated Clinical Evaluation Report** | Pause conformity assessment until CER completed and signed off. | Clinical Affairs |
| **Non‑conformities not remedied within 30 calendar days** | Issue formal non‑compliance notice; escalate to Quality Manager for CAPA initiation. | QA Manager |
| **PMS plan lacking defined data‑collection frequency for Class IIb** | Request detailed PMS schedule; if not provided, raise to Project Sponsor for resource allocation. | Post‑Market Surveillance Lead |
| **Any IEC standard evidence (e.g., 60601‑2‑54) pending** | Immediate request to engineering for test reports; if unavailable >7 days, inform NB of delay and seek extension. | Engineering Manager |
| **NB audit report indicates “critical” non‑conformities** | Stop product launch; convene cross‑functional corrective‑action team and inform senior management. | Compliance Officer |

---

### 6. Summary Judgment  

- The X‑ray medical device is **Class IIb** under **Rule 10 (Annex VIII)** and must follow the **Annex X + Annex XI** conformity‑assessment route, requiring full NB involvement.  
- A complete evidence package comprising TD (Annex II), RMF (ISO 14971), CER & PMCF (Annex XIV), PMS system & PSUR (Art. 83‑86), QMS audit (ISO 13485) and IEC standard conformity reports is mandatory.  
- Several critical items are currently missing (exact MD‑code, finalized clinical evidence, IEC 60601‑2‑54 test data, detailed PMS plan). These must be supplied before the NB can issue a type‑examination certificate.  

**Immediate next steps:** obtain the precise MDR product‑code from NANDO, collect the listed missing documents, and address any non‑conformities identified in the QMS audit within the defined timeframes.

---

### 7. Peer‑Review Prompt  

*Please review this draft for:*

1. **Assumptions on classification** – Is Rule 10 the appropriate rule given the device’s specific functions?  
2. **Source coverage** – Does the evidence list align fully with what the NB expects according to the supplied excerpt?  
3. **Jurisdictional gaps** – Are there any MDR provisions (e.g., specific annexes or articles) that have been omitted but are required for an X‑ray device?  

*Provide feedback and flag any additional documentation that may be needed.*

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

1. Chunk `978896205875274621`

> ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수).

2. Chunk `296791090431458058`

> ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료

## ra_kr

### kb-eval-20261022-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "13bb296d5086163c", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "e14006879a7b7ab39dd0ecfd162427da3e451ed2ff187ebb988bf9beba930afe"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `13bb296d5086163c`
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

> **Regulatory Draft – Supplementary‑Response Strategy (보완자료 대응전략)**  

---

### 1. Device Classification & Submission Route  
| Product (예시) | Likely Korean Grade* | Primary MFDS Track |
|---------------|---------------------|--------------------|
| X‑ray Detector | **3등급 or 4등급** (high‑risk radiological device) | 허가 (MFDS approval) |
| Hand‑held X‑ray Source | **3등급 or 4등급** (radiation emitting equipment) | 허가 |
| 촬영실 GUI SW | **2등급** (software that supports imaging but does not itself deliver radiation) – *if classified as “의료기기·소프트웨어”* | 인증 (technical‑document review by designated 심사기관) |

\*The exact grade must be confirmed against 「의료기기 품목 및 품목별 등급에 관한 규정」. If the device falls outside the radiological category, a lower grade may apply; therefore **grade confirmation is required before finalizing the submission route**.

---

### 2. Required Evidence for Initial Submission (per MFDS)

| Evidence Category | Korean Requirement | Typical International Equivalent |
|-------------------|--------------------|----------------------------------|
| **Device Technical Documentation** | Full 기술문서 (품질·안전·성능) per MFDS 규정 | FDA QSR 21 CFR 820, EU MDR Annex II |
| **Risk Management File** | 위험관리 파일 연계 요구 (ISO 14971) | ISO 14971 2019 |
| **Software Lifecycle Documentation** | IEC 62304 산출물 전부 (설계·검증·유효성) | IEC 62304 2006+A1:2015 |
| **Biological Safety Evaluation** | ISO 10993‑1 기반 생물학적 안전성 평가 | ISO 10993‑1 2018 |
| **Performance & Safety Test Data** | • DQE/MTF (X‑ray Detector) <br>• kVp·mA 출력 특성, 방사선 방호 시험 (Hand‑held Source) <br>• IEC 60601‑1‑3 적용 여부 | IEC 62220‑1‑1, IEC 60601‑1‑3 |
| **Cybersecurity Evidence** (for GUI SW) | 최신 사이버보안 가이드라인(IEC 81001‑5‑1 2021) 적용 증빙 | IEC 81001‑5‑1 2021 |
| **KGMP Facility Certification** | 제조·품질관리 시설에 대한 KGMP 적합성인증 (의료기기법 제28조) | N/A – Korean‑specific |
| **Korean Language Labeling & IFU** | 라벨·사용설명서 한국어 번역 및 검토 (MFDS 고시) | N/A – Korean‑specific |

---

### 3. Gaps Identified in the Source (Type 1 보완 – 가장 빈번)

| Gap | Description (as cited) |
|-----|------------------------|
| **① Performance data insufficient** | “시험 방법·결과 누락” – e.g., missing DQE/MTF, kVp·mA output curves. |
| **② Unclear intended use / principle of operation** | “작용원리·사용목적 기술 불명확”. |
| **③ Incomplete risk‑management linkage** | “위험관리 파일 연계 미흡 (ISO 14971)”. |
| **④ Software documentation lacking** | “SW 문서 미흡 (IEC 62304 산출물 누락)”. |
| **⑤ Missing biological safety assessment** | “생물학적 안전성 평가 누락 (ISO 10993‑1)”. |
| **⑥ Cybersecurity evidence absent** (for GUI SW) | Listed under “Cybersecurity (2025.01)” – no deliverable yet. |

These are exactly the items that most frequently trigger a supplementary request from MFDS.

---

### 4. Risk Controls & Mitigation Plan  

| Gap | Control Action | Expected Outcome |
|-----|----------------|------------------|
| **① Performance data** | • Issue immediate test orders to accredited lab (e.g., KTL) <br>• Use reverse‑schedule to meet the MFDS “보완 기간 내 결과 수령 가능 여부” check. | Complete DQE, MTF, kVp·mA curves; satisfies performance evidence requirement. |
| **② Intended use** | • Draft a clear “사용목적 및 작용원리” section referencing IEC/ISO standards (e.g., IEC 62220‑1‑1 for detectors). <br>• Include labeling excerpts that mirror Korean IFU format. | Eliminates ambiguity; aligns with MFDS technical‑document expectations. |
| **③ Risk‑management linkage** | • Update risk analysis per ISO 14971 2019, map each hazard to verification/validation data (including new performance test results). <br>• Attach revised 위험관리 파일 as an annex in the 보완서. | Demonstrates systematic risk control; satisfies MFDS audit of RMP. |
| **④ Software documentation** | • Generate missing IEC 62304 deliverables: software design description, unit‑test reports, verification & validation plan, traceability matrix. <br>• Provide source‑code excerpts where needed. | Completes the SW dossier; removes “SW 문서 미흡” trigger. |
| **⑤ Biological safety** | • Conduct ISO 10993‑1 tests (cytotoxicity, sensitization, irritation) on all patient‑contact materials. <br>• Compile a Biocompatibility Assessment Report. | Provides required non‑clinical safety evidence; fulfills MFDS’s “생물학적 안전성 평가”. |
| **⑥ Cybersecurity** | • Apply IEC 81001‑5‑1 2021 controls (threat modeling, patch management plan). <br>• Submit a Cybersecurity Risk Management Report with validation results. | Addresses the upcoming 2025 cybersecurity requirement; prevents future 보완. |

All actions should be logged in a **보완 요청서** with numbered items matching the MFDS request (e.g., “Item 1‑a”, “Item 2‑b”), and each response must cite the regulatory basis (framework reference) used.

---

### 5. Citations  

| Item | Citation Type | Reference |
|------|---------------|-----------|
| Processing‑time table (허가 65일, 인증 30일…) | Instance identifier – none supplied in source | *no specific identifier found in source — verify separately* |
| Risk‑management requirement | Framework reference | ISO 14971 2019 |
| Software lifecycle requirement | Framework reference | IEC 62304 2006+A1:2015 |
| Biological safety assessment | Framework reference | ISO 10993‑1 2018 |
| Performance test standards for detectors | Framework reference | IEC 62220‑1‑1 (adopted by MFDS) |
| Radiation safety for handheld source | Framework reference | IEC 60601‑1‑3 |
| Cybersecurity guideline | Framework reference | IEC 81001‑5‑1 2021 |
| KGMP certification requirement | Framework reference | 의료기기법 제28조 (KGMP) |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Action Required | Responsible Role |
|-------------------|-----------------|------------------|
| **Supplementary response exceeds 30 calendar days** (clock‑stop excluded) | Escalate to Project Lead & request MFDS “보완 기간 연장” justification. | RA Manager |
| **Critical safety data still missing after first test order** (e.g., no DQE/MTF) | Immediate senior‑level review; consider parallel testing with second lab. | QA Director |
| **Regulatory deadline (80 days for 허가 with clinical)** approaches and any “보완 기간” remains unresolved | Convene cross‑functional “날짜 마감” meeting; prepare contingency filing or risk‑based justification for earlier submission. | PMO |
| **New MFDS notice affecting classification or evidence** identified (outside current source) | Pause submission, request legal/regulatory update, and re‑assess grade & route. | Compliance Officer |
| **Discrepancy between Korean IFU translation and original device labeling** | Halt filing; engage certified translator and medical writer for revision. | Documentation Specialist |

When any trigger fires, the designated person must log the event in the project risk register and notify the RA team lead within 24 hours.

---

### 7. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made regarding device grades (especially for the GUI software) and the completeness of the listed evidence gaps. Verify whether any additional Korean‑specific obligations (e.g., post‑market surveillance plan for 3등급/4등급, specific MFDS 고시 numbers for labeling) have been omitted from this draft. Also, confirm that the “no specific identifier” note on processing times aligns with the latest MFDS 고시.

---

### 8. Reusable RA Judgment (honcho_conclude)

```
honcho_conclude:
- When constructing a supplementary‑response plan for Korean MFDS submissions, always start by **confirming the device’s exact grade** from 「의료기기 품목 및 품목별 등급에 관한 규정」 before assigning the submission track.
- List typical evidence categories (risk management, performance testing, software lifecycle documents, biocompatibility, KGMP certification, Korean labeling) as a baseline; then map any MFMF‑identified gaps to concrete mitigation actions with clear timelines.
- Cite **framework references** (ISO/IEC standards, Acts, Article names) directly; only include **instance identifiers** (notice numbers, article sections) if they appear explicitly in source material—otherwise flag them with “no specific identifier found – verify separately”.
- Use the MFDS processing‑time table as a timing benchmark but do not assume an underlying 고시 number unless it is provided.
- Define human‑escalation triggers based on clock‑stop periods, critical safety data gaps, and regulatory deadline proximity to ensure timely management escalation.
```

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

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `233519449609923302`

> ### Type 1: 기술문서 보완 (가장 빈번) **빈번 사유** - 성능 데이터 불충분 (시험 방법·결과 누락) - 작용원리·사용목적 기술 불명확 - 위험관리 파일 연계 미흡 (ISO 14971) - SW 문서 미흡 (IEC 62304 산출물 누락) - 생물학적 안전성 평가 누락 (ISO 10993-1) **대응 전략** 1. 보완 요청서 접수 즉시 내용 분류 (Type, 소관 부서, 데이터 필요 여부) 2. 추가 시험이 필요한 항목은 즉시 시험 의뢰 (기간 역산 필요) 3. 보완서 구조: 요청 항목별 번호 대응 + 인용 근거 명시 4. 규격 시험 기관과 보완 기한 내 결과 수령 가능 여부 사전 확인 **자사 3제품 적용** | 제품 | 주요 보완 예상 항목 | |---|---| | X-ray Detector | DQE·MTF 시험 데이터, IEC 62220-1-1 적합성 | | Handheld X-ray Source | kVp·mA 출력 특성, 방사선 방호 (IEC 60601-1-3) | | 촬영실 GUI SW | IEC 62304 SW 수명주기 산출물, Cybersecurity (2025.01) | ---

### kb-eval-20261022-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "a516b6d614a2dd98", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `a516b6d614a2dd98`
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

> **Regulatory Draft – Digital‑Medical‑Device Software (Labeling & Cybersecurity)**  

---

## 1 Classification & Submission Route  
| Item | Requirement | Current Source Evidence |
|------|-------------|--------------------------|
| **Device grade** | Must be determined against 「의료기기 품목 및 품목별 등급에 관한 규정」. The amendment *법률 제21949호* (공포 2026‑09‑15) expands online‐display/advertisement rules but does not itself alter the risk‑grade matrix. | No specific grade indicated in source – **verify separately**. |
| **Submission track** | • 1등급 → 신고  <br>• 2등급 → 인증 (MFDS‑designated 심사기관 review)  <br>• 3·4등급 → 허가  | Determined after grade confirmation. |

*Action:* Obtain the intended use and risk classification from the product dossier; assign the appropriate Korean grade and route.

---

## 2 Mandatory Evidence Package (per MFDS expectations for digital medical‑device software)  

| Category | Required Item(s) | Basis in Source |
|----------|------------------|-----------------|
| **Regulatory law** | Confirmation that the device complies with the amended *의료기기법* (법률 제21949호, 공포 2026‑09‑15). | 【1】 |
| **Software versioning & release** | Version number, build number, and release date. | S‑1 – “SW 버전·빌드 번호·릴리스일” (필수) → 근거: 디지털의료제품법 시행규칙 |
| **Software update policy** | Description of update method(s) and scheduled frequency. | S‑2 (필수) → MFDS SW 가이드라인 |
| **System requirements** | Minimum/Recommended OS, CPU, RAM, storage, monitor resolution, network specs. | S‑3 (필수) → MFDS SW 가이드라인 |
| **Compatibility list** | List of compatible medical devices and interface specifications. | S‑4 (필수) – no explicit external reference; treat as mandatory data element. |
| **Data exchange formats** | Supported DICOM, HL7 (or other) input/output formats. | S‑5 (필수) – no external reference. |
| **Cybersecurity settings** | Encryption policies, network segregation, access control measures. | S‑6 (필수) → MFDS 사이버보안 가이드라인 2025.01 |
| **Patch management** | Procedure and responsibility for security‑patch application. | S‑7 (필수) → MFDS 사이버보드 가이드라인 2025.01 |
| **Residual cyber risks** | Identified residual threats & mitigation plan. | S‑8 (필수) → MFDS 사이버보드 가이드라인 2025.01 |
| **Backup & recovery** | Data backup schedule, storage location, and recovery process. | S‑9 (필수) – no external reference. |
| **Log management** | System log collection, retention period, and review procedure. | S‑10 (권장) → MFDS 사이버보드 가이드라인 |
| **Quality Management System** | KGMP certification for manufacturing; ISO 13485:2016 compliance. | Framework reference – required by MFDS for all graded devices. |
| **Risk Management** | ISO 14971:2019 risk analysis, including software‑specific hazards & cyber risk controls. | Framework reference (ISO 14971). |
| **Software Lifecycle** | IEC 62304:2006+A1:2015 development and maintenance processes. | Framework reference (IEC 62304). |
| **Labeling / IFU** | Korean language labeling that incorporates all mandatory “S‑” items; QR‑code or electronic IFU must be provided in Korean as per MFDS labeling guidance. | Implicit from the table’s “필수” status and from the overall amendment (법률 제21949호) which tightens online advertising/display rules. |
| **Clinical Evidence** | If device is 3등급·4등급, a clinical evaluation report (CER) meeting MFDS requirements; foreign CER may be accepted only where MFDS has announced mutual‑acceptance – check current notice for acceptance scope. | No specific identifier in source – **verify separately**. |
| **Post‑Market Surveillance** | PMS plan aligned with MFDS 시판후조사 규정 (including adverse event reporting, periodic safety updates). | Framework reference – required for 2등급·이상. |

---

## 3 Missing / Unverified Information  

| Gap | Why it matters | Suggested source/next step |
|-----|----------------|----------------------------|
| **Intended use & risk grade** | Determines submission track and depth of clinical evidence needed. | Review product specification; cross‑check with 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **Clinical evaluation strategy** | Required for 3·4등급 devices; may need local data if foreign CER not mutually accepted. | Obtain MFDS notice on foreign clinical evidence acceptance (latest 고시). |
| **KGMP certification status** | Mandatory manufacturing compliance for all grades except some exempted 1등급 items. | Request KGMP certificate or plan to obtain it. |
| **Korean language IFU & labeling files** | Online display rules (법률 제21949호) require Korean‑language information. | Prepare Korean translation; confirm format per MFDS 표시·광고 가이드라인. |
| **Usability testing in Korean target users** | Required for devices with interactive software to demonstrate safe use. | Conduct usability study and prepare report per MFDS usability guidance. |
| **Evidence of compliance with MFDS 사이버보안 가이드라인 2025.01** (e.g., penetration test reports, vulnerability management plan) | Mandatory “필수” items S‑6~S‑8; non‑compliance leads to rejection. | Generate and submit documented cybersecurity risk assessment & mitigation documentation. |
| **Reference number for the “디지털의료제품법 시행규칙”** | Needed when citing statutory basis for S‑1 requirement. | Locate the 최신 시행령 번호; if not in source, note “no specific identifier found – verify separately”. |

---

## 4 Risk Controls (aligned to mandatory items)  

| Hazard / Risk | Control Measure | Reference |
|---------------|-----------------|-----------|
| Incorrect software version displayed to users | Mandatory inclusion of version‑build‑release data on UI & labeling; enforce via change‑control. | S‑1 (디지털의료제품법 시행규칙). |
| Out‑of‑date software leading to safety issues | Defined update schedule, automated patch deployment, documented responsibility. | S‑2, S‑7 (MFDS SW 가이드라인 / 사이버보안 가이드라인 2025.01). |
| Incompatible hardware causing malfunction | Publish minimum system specs; embed hardware compatibility checks in installer. | S‑3 (MFDS SW 가이드라인). |
| Data exchange errors (DICOM/HL7) | Validation of input/output formats; conformance testing against IEC 62366‑1 usability standards. | S‑5 (no external ref); ISO 13485 quality processes. |
| Cyber‑attack leading to data breach or device misuse | Encryption, network segmentation, role‑based access control, regular security patches, residual risk mitigation plan. | S‑6~S‑8 (MFDS 사이버보안 가이드라인 2025.01). |
| Loss of patient data due to hardware failure | Routine backups, off‑site storage, documented recovery procedures. | S‑9 (no external ref). |
| Inadequate audit trail for forensic analysis | System log collection & secure retention per recommended practice. | S‑10 (권장) – implement as best practice. |
| Misinterpretation of labeling by end‑users | Korean language IFU, clear symbols, usability testing with target users. | MFDS 표시·광고 가이드라인; ISO 14971 risk control hierarchy. |

---

## 5 Human‑Escalation Triggers  

| Situation | Trigger Condition | Escalation Action |
|-----------|-------------------|-------------------|
| **Uncertain device grade** | No definitive classification after initial review. | Alert senior RA lead; postpone dossier submission until grade is confirmed. |
| **Missing mandatory “S‑” data** (e.g., no cybersecurity settings) | Any “✅ 필수” item not documented in the technical file. | Stop submission; require product team to provide missing evidence before proceeding. |
| **Foreign clinical evidence being considered** | Intended use places device in 3등급·4등급 but only foreign CER available. | Verify current MFDS notice on mutual‑acceptance; if not covered, request local clinical data or consult MFDS for a conditional waiver. |
| **KGMP certificate pending** | Manufacturing site not yet KGMP‑certified for a device that requires it (≥2등급). | Suspend dossier submission; initiate KGMP certification process and inform project timeline. |
| **Cybersecurity test failures** | Penetration test or vulnerability scan reveals critical findings. | Immediate remediation; risk assessment update; notify project manager and regulatory lead. |
| **Labeling language non‑compliance** | Draft IFU/label lacks Korean translation of any mandatory “S‑” item. | Halt review; engage translation team; re‑submit for compliance check. |
| **Regulatory amendment updates** | New MFDS 고시 or notice issued after dossier lock‑date that impacts the device (e.g., expanded online advertising rules). | Perform impact analysis; if material, reopen dossier and incorporate changes. |

---

## 6 Citations  

| Item | Citation Type | Source |
|------|---------------|--------|
| 법률 제21949호 (의료기기법 일부개정) | Instance identifier (specific instrument number) | 【1】 |
| S‑1〜S‑5 “필수” items – basis in 디지털의료제품법 시행규칙 / MFDS SW 가이드라인 | Framework reference (guideline name) | 【2】 |
| S‑6〜S‑8 cybersecurity requirements – MFDS 사이버보안 가이드라인 2025.01 | Framework reference (guideline name + year) | 【2】 |
| ISO 14971:2019 – risk management | Framework reference (standard) | General knowledge (no source needed) |
| IEC 62304:2006+A1:2015 – software lifecycle | Framework reference (standard) | General knowledge |
| ISO 13485:2016 – QMS for medical devices | Framework reference (standard) | General knowledge |

*No other specific notice numbers or article sections appear in the supplied excerpts; any such identifiers required for further items must be verified separately.*

---

## 7 Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made above regarding (1) the necessity of Korean‑language labeling for all “S‑” items, (2) the applicability of MFDS 사이버보안 가이드라인 2025.01 to the listed mandatory cybersecurity controls, and (3) the adequacy of treating the listed “필수” items as universally required across all device grades without grade‑specific exemption clauses. Identify any gaps in source coverage or jurisdiction‑specific nuances that may affect the submission strategy.

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

### kb-eval-20261022-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "0e4e8181350ce9ae", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `0e4e8181350ce9ae`
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

> **Regulatory Draft – Cyber‑security‑focused Medical Device (Korea)**  

---

### 1. Device Synopsis (as known)

| Item | Comment |
|------|---------|
| **Intended use / indication** | *Not provided in source* – required to determine Korean grade. |
| **Primary technology** | Software‑enabled medical device that processes, stores or transmits patient data; therefore subject to MF DS cyber‑security requirements (2025 revision). |
| **Regulatory trigger** | “의료기기의 사이버보안 허가·심사 가이드라인” (민원인 안내서) – amendment 2025‑01‑10 expands required cyber‑security controls from 15 to 35 items. |

*Action*: Obtain the full product description and intended use statement from the sponsor before any classification work can be completed.

---

### 2. Korean Classification & Submission Route  

| Korean grade | Typical submission track | When applicable |
|--------------|--------------------------|-----------------|
| **1등급** | 신고 (notification) | Low‑risk, non‑invasive devices without software that affects patient safety. |
| **2등급** | 인증 (technical‑document review by MFDS‑designated 심사기관) | Moderate risk; default for most software‑enabled devices that are not life‑supporting. |
| **3등급·4등급** | 허가 (full MFDS approval) | High‑risk, invasive or life‑supporting devices; also required when the device is a “software as a medical device” (SaMD) that performs diagnosis/treatment. |

> **Rule source**: Korean grading rules are set out in 「의료기기 품목 및 품목별 등급에 관한 규정」 (§2 of *MFDS_인허가_상세가이드.md*).  

**Current status:** The grade cannot be assigned from the excerpt alone.  
- **Missing information:** exact intended use, risk class according to Korean rules, and any prior MFDS classification (if already listed in the public catalogue).  

**Human‑escalation trigger #1** – *If the sponsor cannot supply a definitive intended‑use statement within 5 business days, raise to senior RA manager for risk‑based classification decision.*

---

### 3. Evidence Package Required by MFDS Cyber‑security Guideline (2025 revision)

The guideline expands **35 cyber‑security “RA requirements”** (RA‑01 ~ RA‑35) grouped into eight categories (see source excerpt [2]). The sponsor must provide documentary proof for each item.

| Category (per source [2]) | Typical evidence to submit |
|---------------------------|----------------------------|
| **보안 설계 원칙** – Secure by design, defense‑in‑depth, least privilege | System architecture diagram showing security layers; design rationale document; threat model. |
| **인증·접근 제어** – User authentication, RBAC, session management | Access‑control policy; user‑role matrix; screenshots of login/lockout mechanisms; penetration‑test report for authentication flow. |
| **암호화** – Data‑at‑rest & in‑transit encryption, key management | Encryption algorithm specification (AES‑256 etc.); certificate chain; HSM or key‑storage SOP. |
| **소프트웨어 무결성** – Code signing, boot integrity verification, SBOM management | Signed firmware/software binaries; code‑signing certificate; Secure Boot configuration; Software Bill‑of‑Materials (SBOM) list with version control. |
| **네트워크 보안** – Port minimisation, firewall, TLS version requirements | Network diagram; firewall rule set; TLS 1.2+ compliance test report. |
| **취약점 관리** – CVE monitoring, patch cadence, CVD policy | Vulnerability‑management plan; list of subscribed CVE feeds; schedule of periodic patches; record of last patch applied. |
| **감사·로그** – Security event logging, log protection, access history | Log‑capture specification (format, retention); tamper‑evident storage method; audit‑trail report from test environment. |
| **업데이트·유지보수** – Secure update mechanism, remote management security | Update delivery architecture (signed OTA packages); authentication of update server; maintenance SOP for remote access. |

> **Framework references** used to shape the evidence list: **IMDRF N60/N73**, **IEC 81001‑5‑1** (2021 edition), and **ISO 14971** (2019) for risk management integration.

### 4. Additional Korean‑specific Evidence Required

| Requirement | Detail |
|-------------|--------|
| **KGMP certification of manufacturing site** | Certificate issued under 의료기기법 제28조 (effective 2026‑07‑01). |
| **Korean language labeling & IFU** | All labeling, symbols and instructions must be in Korean; see MFDS 고시 on labeling (no specific 고시 number found in source – verify separately). |
| **Clinical evidence (if required)** | For 3등급·4등급 devices, domestic clinical data or foreign CER accepted per MFDS notice on clinical evaluation (specific notice number not provided – verify separately). |
| **Risk Management File** | ISO 14971‑based RMF that incorporates the cyber‑risk controls above; must be submitted as part of the technical dossier. |

---

### 5. Gaps / Missing Information (to be confirmed with sponsor)

1. **Device grade** – cannot be assigned without intended use and risk assessment.  
2. **Exact MFDS guideline identifier** – source only gives title, amendment date, and content; no 고시 번호 is listed. *Action*: request the official PDF to capture the formal notice number (e.g., “고시 제2025‑XX호”).  
3. **Foreign evidence mapping** – if using FDA 510(k) or CE mark data, confirm whether MFDS accepts those under current mutual‑recognition notices (specific notice numbers not present in source).  
4. **KGMP status of the manufacturing facility** – certificate copy required.  

---

### 6. Risk Controls & Integration into Korean RMF

| Cyber‑security control | Corresponding ISO 14971 risk control |
|------------------------|--------------------------------------|
| Secure by design (defense‑in‑depth) | **Risk control measure** – *Design safeguard* (Clause 5.3). |
| Code signing & SBOM | **Verification/validation activity** – *Software integrity check* (Clause 8). |
| Vulnerability monitoring (CVE) | **Post‑market surveillance** – *Detection of hazards* (Clause 10). |
| Secure OTA update | **Protective measure** – *Secure maintenance* (Clause 7). |

All cyber‑security controls must be reflected in the Hazard Identification & Risk Evaluation table, with accompanying verification evidence.

---

### 7. Human‑Escalation Triggers

| Trigger | Reason | Escalation path |
|--------|--------|-----------------|
| **Unresolved device grade** (after request for intended use) | Cannot select submission track; risk of non‑compliance. | Notify RA Team Lead → Decision on provisional classification or need for additional clinical data. |
| **Missing official guideline identifier** | Citation gaps may cause MFDS reviewer comments. | Request document from sponsor/legal; if unavailable, flag to Senior Regulatory Counsel for guidance. |
| **Incomplete evidence for any of the 35 RA items** | MFDS will reject dossier on cyber‑security grounds. | Pause submission → Issue “Evidence Gap” notice to sponsor with deadline (typically 10 working days). |
| **KGMP certificate absent or expired** | Manufacturing site not authorized. | Immediate halt of filing; open internal audit request and inform Quality Assurance. |
| **Foreign clinical evaluation data offered but no MFDS acceptance notice cited** | Potential rejection under “foreign CER” rules. | Seek clarification from MFDS liaison office; if uncertain, involve external consultant with Korean regulatory expertise. |

---

### 8. Recommended Next Steps (Actionable)

1. Obtain **full product description**, intended use, and any existing MFDS classification.  
2. Request the **official PDF** of the “의료기기의 사이버보안 허가·심사 가이드라인” to capture its 고시 번호.  
3. Compile **documented evidence** for each of the 35 RA requirements (use checklist aligned with categories above).  
4. Prepare a **Korean‑language labeling draft** and confirm KGMP certification status.  
5. Draft a **risk management file** (ISO 14971) that explicitly links identified cyber hazards to the controls listed.  

---

### 9. Peer‑Review Prompt

> *Colleague, could you review the assumptions made about the device’s classification path and the completeness of the evidence checklist? Specifically: (a) have we captured all MFDS‑required artefacts for a software‑enabled medical device under the 2025 cyber‑security guideline, and (b) are there any jurisdiction‑specific gaps—such as the need for a “사이버보안 인증서” or additional Korean‑language documentation—that we may have missed? Please also verify whether any recent MFDS notices (post‑2025) could affect the acceptance of foreign clinical evaluation reports for this device.*

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

### kb-eval-20261022-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "a8459a482fcf9a3b", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `a8459a482fcf9a3b`
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

> **Regulatory Draft – Digital‑Medical‑Product (디지털의료제품) Submission**

---

### 1. Korean Classification & Submission Route  

| Item | Guideline / Source | Determination |
|------|-------------------|---------------|
| **Device grade** | Must be cross‑checked against 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS_인허가_상세가이드.md §2). The source excerpts do not specify the grade. | *Grade to be confirmed* – if the product is a software‑only “digital health” tool it will often fall under **1등급 → 신고** or **2등급 → 인증**; higher risk AI‑driven/implantable solutions may be **3등급·4등급 → 허가**. |
| **Submission track** | Korean law separates **신고**, **인증**, and **허가** by grade (see “Korean Classification System” rules). | *Assign the appropriate track after confirming grade*; default for 2등급 is **인증** (technical‑document review by a designated 심사기관). |

> **Citation note:** No specific notice/decree number identifying the applicable grade appears in the provided excerpts – *verify separately*.

---

### 2. Core Evidence Required (as reflected in the matrix)

| Req‑ID | Requirement (what the MFDS expects) | Current Status (from source) | Evidence Needed | Gap / Missing Item |
|-------|--------------------------------------|------------------------------|-----------------|--------------------|
| **DR‑20** | 설계·개발 프로세스 – compliance with **ISO 13485 §7.3** (design & development). | ● (completed) | • Design History File (DHF) architecture <br>• Design verification and validation protocols & reports | None identified – ensure all protocol documents are attached to the submission. |
| **DR‑21** | 위험관리 통합 – compliance with **ISO 14971** (risk management). | ● (completed) | • Risk Management File (RMF) – includes risk analysis (FMEA/FTA), risk evaluation, and residual‑risk acceptance justification. | None identified – verify that the RMF contains a documented “잔존위험 수용 판정”. |
| **DR‑22** | SW 수명주기 – compliance with **IEC 62304** (software lifecycle). | ● (completed) | • Software safety class determination <br>• Approved software‑life‑cycle plan (including development, maintenance, and release procedures). | None identified – confirm that the life‑cycle plan is signed off by a qualified authority. |
| **DR‑23** | 공급자 관리 – component & OSS supply chain management (SBOM linkage). | ◐ (in progress) | • Supplier management SOPs covering hardware components and open‑source software <br>• License compliance verification records <br>• Updated Software Bill of Materials (SBOM). | **Action:** Complete OSS‑supplier procedures; generate and attach SBOM. |
| **DR‑24** | 교육·훈련 – AI developer & cyber‑security training. | ◐ (in progress) | • Training curriculum for AI developers (including ethics, bias mitigation, data handling) <br>• Attendance / completion records <br>• Cyber‑security awareness program. | **Action:** Finalise AI education module; collect and archive trainee completion certificates. |

> **Citation note:** The matrix cites ISO/IEC standards only (ISO 13485 §7.3, ISO 14971, IEC 62304). No specific MFDS 고시 or notice numbers are present – *verify separately*.

---

### 3. Risk Controls & Acceptance Criteria  

| Control | Source Basis | Implementation Summary |
|---------|--------------|------------------------|
| **Design Verification / Validation** | ISO 13485 §7.3 (design verification and validation) | Test plans, acceptance criteria, traceability matrix linking requirements → design outputs → test results. |
| **Risk Management Process** | ISO 14971 (risk analysis, evaluation, control) | Conduct FMEA for functional hazards; apply risk‑control hierarchy (inherent safety, protective measures, information). Document residual risk level and obtain sign‑off that it is “acceptable”. |
| **Software Safety Classification** | IEC 62304 (software safety class A/B/C) | Classify software based on potential harm; higher classes require more rigorous verification/validation and documentation. |
| **Supply‑Chain Integrity** | Internal SOP (OSS & component management) | Maintain SBOM, perform license compliance checks, and enforce supplier audits for critical components. |
| **AI & Cybersecurity Training** | MFDS guidance on AI & cybersecurity (digital medical product law) | Provide mandatory training modules; maintain records to demonstrate competency of developers handling patient data or algorithm updates. |

---

### 4. Missing / Incomplete Documentation – Immediate Action Items  

1. **OSS Supplier Management SOP** – Draft, review, and obtain approval; attach SBOM.  
2. **AI Development Training Module** – Finalise curriculum; collect evidence of employee completion.  
3. **Software Life‑Cycle Plan Approval Sign‑off** – Ensure the plan is signed by a qualified (e.g., Certified Software Engineer) authority.  
4. **Residual Risk Acceptance Statement** – Include a clear statement in the RMF confirming that all identified residual risks meet MFDS acceptance criteria.  

*All above items must be attached as PDF/Excel bundles to the electronic submission package.*

---

### 5. Human‑Escalation Triggers  

| Trigger | Condition | Escalation Path |
|--------|-----------|-----------------|
| **Status ◐ (in progress) after 2 weeks** | DR‑23 or DR‑24 still not “●”. | Notify Project Lead → Schedule a remediation meeting with QA & Development leads; if not resolved within an additional week, raise to senior RA manager. |
| **Absence of any required evidence** (e.g., missing DHF, RMF) | Submission checklist shows a gap. | Immediate pause of dossier assembly; issue “stop‑work” notice to the responsible functional owner; involve QA for root‑cause analysis. |
| **Unclear device grade** | No definitive grade identified from regulatory list. | Prompt legal/RA team to perform classification review using MFDS classification table; defer submission until confirmed. |
| **Regulatory instrument identifier missing** (e.g., MFDS 고시 number) | Reviewer cannot reference a specific notice for a requirement. | Assign senior RA to locate the exact 고시 / notice in MFDS gazette and update the dossier bibliography before filing. |

---

### 6. Peer‑Review Prompt  

> **To: [RA Team Member]**  
> Please review this draft and challenge the following assumptions:  
> 1. The inferred submission track (인증 for a potential 2등급 device) – could the product fall into 3등급·4등급 based on AI functionality?  
> 2. That DR‑20 to DR‑22 are already “●”. Have we verified that all underlying documents (DHF, RMF, Software Life‑Cycle Plan) are complete and signed off?  
> 3. The sufficiency of the OSS supplier management procedures – does MFDS require any additional evidence (e.g., third‑party component certification) for digital health software?  
> 4. Whether any recent MFDS 고시 expanding acceptance of foreign clinical evaluation reports (CER) applies to this product; if so, we may need to include that citation.

Please provide feedback and indicate any gaps in source coverage or Korean‑specific obligations not captured here.

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

### kb-eval-20261022-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-22", "decision_ref": "kb-eval-20261022-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "f8204592d8e1288b", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f8204592d8e1288b`
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

> **Regulatory Draft – Digital‑Medical‑Product Act (디지털의료제품법) SaMD/AI Software**

---

### 1. Device Scope & Preliminary Classification  

| Item | Comment |
|------|---------|
| **Product type** | Independent digital medical‑software (콘솔 SW / 뷰어 SW) that performs AI‑based image analysis – falls under “독립형 디지털의료기기 SW”. |
| **Regulatory framework** | 디지털의료제품법 (Digital Medical‑Device Act).  The act references the same grade system as the Medical‑Device Act: 1등급·2등급·3등급·4등급. |
| **Likely grade** | The act classifies AI‑driven diagnostic support software usually as **2등급** or higher, depending on risk (risk of mis‑diagnosis, invasiveness, intended user).  The exact grade must be determined from 「의료기기 품목 및 품목별 등급에 관한 규정」. <br>*No specific identifier for the grade is supplied in the source – verify separately.* |
| **Submission route** | • If classified **2등급 → 인증** (technical‑document review by an MFDS‑designated 심사기관).  <br>• If later determined **3등급·4등급 → 허가** (full MFDS approval). |

---

### 2. Required Submission Evidence (per 현재 MFDS 규정)

| Requirement | Source / Standard | What must be supplied |
|-------------|-------------------|-----------------------|
| **Technical Documentation (QMS)** | KGMP (의료기기법 제28조) – “제조·품질관리 인증”.  ISO 13485:2016 is the accepted QMS model. | • KGMP certification of the software development facility.<br>• SOPs for change‑management, SBOM, AI data governance (see Section 8 actions). |
| **Usability / Human Factors** | IEC 62366‑1 (2015+A1:2020) – referenced in post‑action “사용적합성 엔지니어링 계획”. | • Usability engineering plan & validation report. |
| **Software Life‑Cycle Processes** | IEC 62304 (2006+A1:2015). | • Software development plan, verification/validation protocols, risk management file (ISO 14971:2019). |
| **Risk Management File** | ISO 14971:2019 (no amendment after 2024). | • Hazard analysis, risk control measures, residual risk evaluation. |
| **Cybersecurity** | “디지털의료기기 전자적 침해행위 보안 지침(안)” (2025‑01) and “의료기기 사이버보안 허가·심사 가이드라인(개정)” (2025‑01‑10) – both listed in the guide table. | • Cybersecurity risk assessment, SBOM, vulnerability management SOP (SOP‑SBOM‑001). |
| **AI Model Governance** | No specific Korean guideline yet; MFDS has issued a “생성형 AI 의료기기 허가·심사 가이드라인” (2025‑01) – listed with ‘중’ relevance. | • Dataset provenance, bias mitigation, performance monitoring SOPs (SOP‑AIDATA‑001, SOP‑AIGOV‑001). |
| **Clinical Evaluation** | MFDS may accept foreign Clinical Evaluation Reports (CER) under the “외국 임상평가보고서(CER) 상호인정” scope – but only if explicitly referenced in a recent notice. *No such notice appears in the source*, therefore local clinical data or Korean‑language CER must be prepared. |
| **Labeling & IFU** | MFDS labeling 규정 (Korean language mandatory, include CE/ FDA/ foreign clearances only as reference). | • Korean label, instructions for use, and safety information; electronic IFU must comply with the “디지털의료기기 전자적 침해행위 보안 지침”. |
| **Post‑Market Surveillance** | MFDS 시판후조사·감시 규정 (2024 revision). | • PMS plan, adverse event reporting procedure. |

---

### 3. Gaps / Missing Information (to be addressed before dossier finalisation)

1. **Exact device grade** – needs confirmation from the official grade table; cannot assume 2등급.  
   *Citation*: no specific identifier found in source — verify separately.  

2. **Clinical evidence** – absence of a locally‑conducted clinical study or Korean CER. If MFDS accepts foreign CER under the latest notice, that notice number must be identified and cited.  

3. **Korean language labeling draft** – not yet prepared; required for any submission.  

4. **KGMP certification status** – facility must have KGMP accreditation; current status unknown.  

5. **Detailed AI risk assessment** – while SOP‑AIDATA‑001/AIGOV‑001 are drafted (v0.2), the full risk control matrix linking algorithmic bias, data drift, and clinical impact is not yet documented.  

6. **Cybersecurity threat model** – high relevance guide exists, but a formal threat‑model & mitigation plan aligned to the “디지털의료기기 사이버보안 허가·심사 가이드라인(개정)” is pending.  

7. **SBOM completeness** – SOP‑SBOM‑001 v0.2 completed; verification of “정합성” (consistency) with actual software components still required.  

8. **Change‑Management SOP (CMP Section)** – SOP‑CC‑001 drafted (v0.2); needs full implementation for any post‑approval updates.

---

### 4. Core Risk Controls & Evidence Mapping

| Risk Area | Control(s) | Supporting Document / Standard |
|-----------|------------|--------------------------------|
| **Algorithmic performance / diagnostic error** | • Validation against annotated Korean datasets.<br>• Ongoing monitoring plan (AI model drift). | IEC 62304, ISO 14971, SOP‑AIDATA‑001, SOP‑AIGOV‑001. |
| **Usability hazards** | • Human‑factors testing with target users (physicians/radiologists). | IEC 62366‑1. |
| **Cybersecurity breach / tampering** | • SBOM generation & management.<br>• Vulnerability scanning, patch schedule.<br>• Network isolation where applicable. | “디지털의료기기 사이버보안 허가·심사 가이드라인(개정)”, SOP‑SBOM‑001, SOP‑CC‑001. |
| **Software defects / malfunction** | • IEC 62304 lifecycle verification & validation.<br>• Automated unit testing, code review. | IEC 62304. |
| **Regulatory non‑conformance (KGMP)** | • KGMP certification; routine internal audits. | 의료기기법 제28조. |
| **Labeling/Instruction misinterpretation** | • Korean language IFU with clear warnings, contraindications. | MFDS labeling 규정. |

---

### 5. Human‑Escalation Triggers (Review & Decision Points)

| Trigger | Escalation Action | Responsible Role |
|---------|-------------------|------------------|
| **Unresolved device grade** | Pause dossier assembly; request official grade confirmation from MFDS or consult “의료기기 품목 및 품목별 등급에 관한 규정”. | Regulatory Lead (RA). |
| **Missing local clinical data / unverified foreign CER acceptance** | Escalate to Clinical Affairs for study planning OR conduct a regulatory intelligence search for the relevant MFDS notice number. | Clinical Lead & RA Manager. |
| **KGMP certification not yet obtained** | Halt submission; initiate facility audit and KGMP application. | Quality‑Management Lead. |
| **Cybersecurity threat model incomplete (high‑risk AI module)** | Immediate escalation to CISO / Security Engineer for full risk analysis before filing. | Security Lead. |
| **SBOM inconsistency discovered in final verification** | Freeze submission; corrective action & re‑validation of SBOM. | Configuration Management Lead. |
| **Residual risk above acceptable level after ISO 14971 assessment** | Convene risk‑acceptance board; consider redesign or additional mitigations. | Risk‑Management Lead. |
| **Regulatory notice numbers (e.g., for foreign CER acceptance) cannot be located** | Flag to senior RA counsel for legal‑department assistance in obtaining official notice. | Senior RA Counsel. |

---

### 6. Citations

| Item | Citation Type | Reference |
|------|---------------|-----------|
| Digital Therapy Clinical Trial Design Guideline (2024‑12) – low relevance | Framework reference (guideline title) | “디지털치료기기 임상시험 설계 가이드라인”. |
| Generative AI Medical‑Device Approval/Review Guideline (2025‑01) – medium relevance | Framework reference | “생성형 AI 의료기기 허가·심사 가이드라인”. |
| Independent Digital‑Medical‑Device SW Usability Guideline (2025‑01) – high relevance | Framework reference | “독립형 디지털의료기기SW 사용적합성 가이드라인”. |
| Cybersecurity Approval/Review Guideline (rev.) (2025‑01‑10) – high relevance | Framework reference | “의료기기 사이버보안 허가·심사 가이드라인(개정)”. |
| Electronic Intrusion‑Security Guidance (2025‑01) – high relevance | Framework reference | “디지털의료기기 전자적 침해행위 보안 지침(안)”. |
| Post‑action matrix items (RA‑01~RA‑20, SBOM SOP, AI data‑governance SOPs) | Framework reference (internal documents) | Listed in Section 8 of source. |
| ISO 14971:2019 – risk management | Standard (framework) | ISO 14971 2019. |
| IEC 62366‑1 (2015+A1:2020) – usability | Standard (framework) | IEC 62366‑1 2015+A1:2020. |
| IEC 62304 (2006+A1:2015) – software lifecycle | Standard (framework) | IEC 62304 2006+A1:2015. |
| ISO 13485:2016 – QMS | Standard (framework) | ISO 13485 2016. |
| KGMP (법 §28) – manufacturing certification | Regulation (framework) | 의료기기법 제28조. |
| No specific MFDS 고시/notice number or article cited in source excerpts | Instance identifier | *no specific identifier found in source — verify separately*. |

---

### 7. Peer‑Review Prompt  

*“Colleague, please evaluate the assumptions made regarding device grading and clinical evidence requirements. Verify whether any recent MFDS notice (e.g., post‑2024) permits direct acceptance of foreign CER for AI‑based diagnostic software, and confirm that the cybersecurity guidance cited indeed applies to independent SaMD under 디지털의료제품법. Identify any additional Korean‑specific obligations (e.g., electronic IFU certification) that may have been omitted.”*

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

1. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

2. Chunk `1130453648414545903`

> ## 8. 후속 조치 요건 (프로젝트 관점) | 우선순위 | 조치 사항 | 연계 문서 | 상태 | |----------|----------|-----------|------| | 1 | 사이버보안 RA-01~RA-20 대응 매트릭스 작성 | 디지털의료제품법_요구사항_매트릭스 | 진행중 | | 2 | 사용적합성 엔지니어링 계획 수립 | IEC_62366-1_사용적합성_엔지니어링_계획서 | v0.2 완료 | | 3 | SBOM 관리 절차 정합성 확인 | SOP-SBOM-001 | v0.2 완료 | | 4 | 변경관리 계획 SOP 연계 (CMP 섹션) | SOP-CC-001 | v0.2 완료 | | 5 | AI 모델 데이터셋·거버넌스 절차 수립 | SOP-AIDATA-001, SOP-AIGOV-001 | v0.2 완료 | | 6 | 구성요소 단위 성능평가 절차 문서화 | AI_구성요소_단위_성능평가 | v0.2 완료 |
