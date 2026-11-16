# KB Eval Checksheet - 2026-11-16 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261116-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "cf4cc92c37dd38f6", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cf4cc92c37dd38f6`
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

> **Regulatory Draft – 510(k) Predicate‑Strategy Checklist**

| Section | Core Requirement | Typical Evidence | Where to Find the Rule (framework reference) | Source‑specific identifier |
|---------|------------------|-----------------|---------------------------------------------|----------------------------|
| **1. Device Classification & Submission Pathway** | Identify Class (I, II, III) and confirm that a 510(k) is appropriate. | • Intended Use / Indications for Use<br>• Product Code search in FDA 510(k) Database | 21 CFR 807.92 (class determination); 21 CFR 812 (510(k) requirements) | *no specific identifier found in source – verify separately* |
| **2. Predicate Device Selection** | Locate one or more legally marketed devices that are “substantially equivalent.” | • Predicate 510(k) number(s)<br>• Comparison of technological characteristics, intended use, labeling | FDA 510(k) Database (public); guidance on substantial equivalence (21 CFR 812.2) | *no specific identifier found in source – verify separately* |
| **3. Substantial‑Equivalence Comparison Table** | Show side‑by‑side comparison of the new device vs each predicate. | • Device description, materials, energy source, performance claims, labeling | 21 CFR 812.2(b)(1) (comparison table requirement) | *no specific identifier found in source – verify separately* |
| **4. Device Description & Indications for Use** | Detailed narrative of device architecture, function, and clinical purpose. | • eSTAR “Device Description / IFU” section (see Source [1])<br>• Diagrams, specifications | 21 CFR 807.87 (labeling) ; eSTAR template guidance (source) | *no specific identifier found in source – verify separately* |
| **5. Performance Testing** | Demonstrate that the device meets its intended performance. | • Bench/bench‑top tests (accuracy, precision, repeatability)<br>• Animal or clinical data if required<br>• Software verification & validation (IEC 62304) when applicable | 21 CFR 820.30 (design validation); IEC 62304 2006+A1:2015 (software); FDA guidance on performance testing (non‑specific) | *no specific identifier found in source – verify separately* |
| **6. Biocompatibility** | Show that patient‑contacting materials are safe. | • ISO 14971 risk analysis<br>• ISO 10993‑1 2018 biocompatibility test plan & results | ISO 14971:2019 (risk management); ISO 10993‑1 2018 (biological evaluation) | *no specific identifier found in source – verify separately* |
| **7. Electrical Safety / EMC** | Verify compliance with applicable electrical standards. | • IEC 60601‑1 2005+A1:2012+A2:2020 (general safety)<br>• IEC 61010‑1, IEC 62368‑1 as appropriate | 21 CFR 820.70 (process controls) ; FDA guidance on EMI/EMC (non‑specific) | *no specific identifier found in source – verify separately* |
| **8. Labeling & UDI** | Provide labeling that meets FDA requirements and includes a UDI. | • Device label & IFU (incl. intended use)<br>• UDI placement on label per §801.20‑§801.50 (Part 801) and formatting per §830.20 (Part 830) | 21 CFR 801.20‑801.70 (labeling); 21 CFR 830.20, §830.300‑330 (UDI system) | *no specific identifier found in source – verify separately* |
| **9. Quality Management System (QMSR)** | Demonstrate compliance with the FDA QMS regulation effective Feb 2026. | • ISO 13485:2016–aligned SOPs (e.g., SOP‑RA‑002, SOP‑CA‑001 etc.)<br>• Design history file, risk management file, validation records | 21 CFR 820 (QMS); QMSR (effective Feb 2026) | *no specific identifier found in source – verify separately* |
| **10. Submission Package** | Assemble all sections into the electronic eSTAR format and submit via FDA’s ESG portal. | • 510(k) Summary, Device Description, Comparison Table, Test Reports, Labeling, QMS certifications, UDI dossier | 21 CFR 807.100 (electronic submissions); Source [2] outlines steps 1‑5 (predicate search → eSTAR template → FDA AI response) | *no specific identifier found in source – verify separately* |

---

### Missing Information / Immediate Action Items
| Item | Why It Matters | Next Step |
|------|----------------|-----------|
| **Exact Intended Use & Indications** | Drives classification and predicate choice. | Obtain finalized IFU language from product team. |
| **Predicate Device(s) Identified** | Required for substantial equivalence claim. | Search FDA 510(k) Database; record numbers, product codes. |
| **Risk Management File (ISO 14971)** | Supports design controls & hazard mitigations. | Create/complete risk analysis worksheet; map hazards to controls. |
> **If any of the above cannot be resolved within 2 weeks, escalate to Senior RA Lead** (see escalation triggers below).

---

### Core Risk Controls (per ISO 14971:2019)
| Hazard Type | Example | Control Strategy |
|-------------|---------|-------------------|
| Electrical shock / fire | High‑voltage circuitry | Built‑in protection, IEC 60601‑1 compliance, verification testing. |
| Software malfunction (if applicable) | Algorithm error in image processing | Follow IEC 62304 lifecycle; implement Predetermined Change Control Plan (PCCP) for post‑market updates. |
| Biocompatibility issue | Device contacts skin/body fluids | Conduct ISO 10993‑1 tests per identified contact duration; material certification. |
| EMI/EMC interference | Wireless telemetry interfering with other equipment | Perform IEC 60601‑1‑2 (EMC) testing; shielding designs. |
| Labeling misuse | Ambiguous instructions could cause user error | Human factors validation, clear IFU language, UDI on label per §801.20–§801.50. |

All controls must be documented in the **Design History File** and referenced in the 510(k) submission.

---

### Human‑Escalation Triggers
| Situation | Trigger | Escalation Path |
|-----------|---------|-----------------|
| **Classification Unclear** (e.g., novel algorithm, AI/ML) | Unable to assign Class I/II after product code search. | Notify Senior RA → consider De Novo pathway (21 CFR 812.2(b)(3)). |
| **No Viable Predicate Found** | No device with substantially equivalent intended use or technology. | Escalate to Regulatory Lead for De Novo or PMA feasibility study. |
| **FDA Issues Additional Information (AI) Request** > 180 days response deadline. | AI pending beyond standard response window. | Senior RA approval required; consider filing a “Request for Extension” under 21 CFR 814.124 if moving toward PMA. |
| **QMS Non‑conformance Identified** | Audit finds missing SOPs (e.g., SOP‑RA‑002, SOP‑CA‑001) or lack of QMSR compliance. | Immediate corrective action plan; Senior QA/RA sign‑off before filing. |
| **Significant Gap in Performance Data** (e.g., lacking clinical data for a Class II device with invasive use). | Incomplete testing package. | Escalate to Clinical Affairs & RA leadership; consider obtaining additional data or revising intended use. |

---

### Bottom Line
- **Submission Route:** 510(k) – provided a suitable predicate exists and the device is classified as Class I/II (or Class III with special controls).  
- **Key Evidence Required:** Device description, substantial‑equivalence comparison, performance test reports, biocompatibility data, electrical safety/EMC data, labeling & UDI dossier, QMSR compliance documentation.  
- **Immediate Gaps:** Intended use finalization, predicate identification, risk management file completion, and any technology‑specific testing plans (software validation, clinical data).  

**Action:** Populate the missing items, assemble the eSTAR template per Source [2], and submit a draft 510(k) to senior RA for review. Trigger escalation if any gap persists beyond the defined timelines.

---

#### Peer Review Prompt
> **To another RA colleague:** Please challenge the assumptions above—especially the classification inference without device specifics, the completeness of the evidence list for potentially software‑driven imaging devices, and any jurisdictional gaps (e.g., whether a De Novo discussion is warranted). Identify any missing citations required by FDA guidance that were not covered in the source excerpts.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> Part 812(=IDE)를 510(k) 요건·SE 근거·De Novo(§812.2(b)(3))로 오인용 3회 + §807.92를 분류 근거로 오인용(계열 8회차) + §807.100 '전자제출' 오귀속 — 다중 심각 결함(오귀속·비존재 인용). 510(k) 요건은 Part 807 Subpart E, De Novo는 §513(f)(2)/21 CFR 860.

**Source Excerpts**

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20261116-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "af1944770534876f", "source": "github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md", "source_hash": "fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `af1944770534876f`
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

> **Regulatory Draft: 510(k) Substantial‑Equivalence Strategy for a New X‑ray Imaging System**

---

### 1. Intended Classification & Submission Route  

| Item | Determination |
|------|----------------|
| **Device family** | Radiology / X‑ray imaging hardware (US FDA panel → 21 CFR Part 892). |
| **Regulatory class** | Class II (most diagnostic X‑ray systems are classified as Class II under 21 CFR §892.XXXXX – exact subsection to be confirmed). |
| **Submission type** | Traditional 510(k) (full substantive review) – the device does not qualify for Abbreviated or Special pathways because it is a new hardware platform and no predicate with identical intended use/technology exists at this time. |
| **Applicable regulations** | • 21 CFR §892 (Imaging devices)  <br>• 21 CFR §807 (Premarket notification)  <br>• 21 CFR §801 (Labeling – UDI placement)  <br>• 21 CFR §830 (UDI system)  <br>• 21 CFR §820 (Quality Management System Regulation, effective Feb 2026)  <br>• ISO 14971:2019 (Risk management)  <br>• IEC 62304:2006+A1:2015 (Software life‑cycle, if software is embedded)  <br>• IEC 62366‑1:2015+A1:2020 (Usability engineering) |

*Citation note:* the source lists “21 CFR 1020” as a required citation; this part addresses enforcement policy for certain devices. No other specific CFR section appears in the excerpt – **no specific identifier found in source — verify separately** for the exact imaging‑device classification (§892.xxx).

---

### 2. Predicate Device Selection (SE 5‑step Decision Point)

The decision flow chart from FDA 2014 Guidance (Appendix A) is reproduced in the source (Chunk [2]). The steps to apply are:

1. **DP1 – Legally marketed predicate?**  
   *If “No” → NSE (De Novo or PMA).*  

2. **DP2 – Same intended use?**  
   *If “No” → NSE.*  

3. **DP3 – Same technological characteristics?**  
   *If “Yes” → proceed to DP5; if “No”, go to DP4.*  

4. **DP4 – Do the different tech features raise new safety/effectiveness questions?**  
   *If “Yes” → NSE; if “No” → DP5.*  

5. **DP5 – Does performance data show at least predicate level of safety & effectiveness?**  
   *If “Yes” → SE (clearance possible); if “No” → NSE.*

*Citation:* the decision points are taken directly from the source excerpt; **no specific identifier found in source — verify separately** for the official guidance reference number.

**Action:** Compile a shortlist of candidate predicates (e.g., 510(k) K####### for comparable conventional X‑ray systems). For each, document:

* Legal market status (cleared & marketed).  
* Intended use phrasing.  
* Core technological characteristics (tube voltage range, detector type, filtration, image processing algorithms).  

If any predicate fails DP1–DP4, the project must pivot to a De Novo submission.

---

### 3. Required Evidence Package for Traditional 510(k)

| Evidence Type | Content Requirement | Regulatory Basis |
|---------------|---------------------|------------------|
| **Device description** | Detailed specifications, block diagram, bill of materials, software architecture (if applicable). | 21 CFR §807.87; ISO 14971:2019 risk analysis inputs. |
| **Intended use & labeling** | Clear statement of clinical indication(s), user population, operating environment; label draft with UDI placement per §801.20+. | 21 CFR §801.5; 21 CFR §830.20 (UDI format). |
| **Predicate comparison** | Side‑by‑side table covering intended use, technological characteristics, performance claims. | FDA SE decision flow (DP1‑DP5). |
| **Performance testing** | *Bench* – X‑ray output (kVp stability, mA accuracy, focal spot size), radiation safety tests (leakage, scatter); *Imaging* – resolution (MTF), contrast-to-noise ratio, dose metrics (CTDI, DAP) compared to predicate; *Software* – verification/validation per IEC 62304 if digital processing is present. | 21 CFR §892.* sections for imaging devices; ISO 14971 risk control verification. |
| **Safety testing** | Electrical safety (IEC 60601‑1 compliance), electromagnetic compatibility, mechanical integrity, thermal safety. | IEC 60601‑1:2005+A1:2012+A2:2020; 21 CFR §820.70 (Design verification). |
| **Risk Management File** | Hazard analysis, risk controls, residual risk assessment, risk-benefit justification. | ISO 14971:2019 (no amendment required). |
| **Usability / Human Factors** | Summative usability validation for operator interface and workflow. | IEC 62366‑1:2015+A1:2020. |
| **Sterilization & Biocompatibility** (if applicable) | ISO 10993‑1:2018 testing plan if any patient‑contact components exist. | ISO 10993‑1. |
| **Quality System Evidence** | Certificate of compliance with QMSR (21 CFR §820) and copy of current ISO 13485:2016 registration; evidence of corrective‑and‑preventive actions, design control records. | 21 CFR §820; effective QMSR Feb 2026. |
| **UDI / GUDID submission** | Device identifier (DI), production identifier (PI) in both plain‑text and AIDC; electronic submission to GUDID per §830.300‑330. | 21 CFR §801.20+ (label); 21 CFR §830.300+. |
| **Regulatory Summary** | Narrative that addresses each SE criterion, cross‑referencing the above evidence. | FDA 510(k) guidance; internal eSTAR checklist (source). |

*Citation note:* The scoring table in source Chunk [1] references “21 CFR 1020” – this is recorded as **no specific identifier found in source — verify separately** for its relevance to the X‑ray device.

---

### 4. Identified Gaps / Missing Information  

| Gap | Why it matters | Required action |
|-----|----------------|-----------------|
| **Exact intended use statement** | Drives predicate comparison and labeling compliance. | Draft a concise indication (“Diagnostic radiographic imaging of adult skeletal structures” etc.). |
| **List of candidate predicates with 510(k) numbers** | Needed for DP1–DP4 assessment & comparative tables. | Search FDA’s 510(k) database; select at least two cleared devices matching the modality (e.g., “Portable X‑ray System, K#######”). |
| **Detailed technological characteristics** (tube voltage range, detector type, filtration, software algorithms) | Determines DP3/DP4 outcomes and performance testing scope. | Provide engineering spec sheets. |
| **Performance test plan & acceptance criteria** | Must demonstrate at least predicate level of safety/effectiveness (DP5). | Develop protocol; align metrics with FDA’s guidance for X‑ray devices. |
| **Software description (if applicable)** – version, development environment, risk classification per IEC 62304. | Impacts software validation and PCCP considerations. | Create Software Development File. |
| **Risk Management File** – hazard analysis results, mitigations, residual risk evaluation. | Required for SE narrative & ISO 14971 compliance. | Conduct risk analysis, populate RMF. |
| **QMSR documentation** – proof of certification under the new 2026 QMSR (ISO 13485‑aligned). | Mandatory for all Class II submissions post‑Feb 2026. | Obtain certificate; compile SOPs (e.g., SOP‑CA‑001, SOP‑RA‑002). |
| **UDI strategy** – chosen Issuing Agency, DI/PI format, labeling mock‑up. | Required under Parts 801 & 830. | Select issuing agency; generate label artwork. |
| **Usability validation data** (if user interface) | Needed for IEC 62366‑1 compliance and to address potential safety concerns from new tech features. | Conduct formative then summative usability testing. |

---

### 5. Risk Controls (selected examples)

| Hazard | Control (design / process) | Verification |
|--------|----------------------------|--------------|
| Excessive radiation dose to patient | Automatic exposure control, dose‑monitoring algorithm, compliance with IEC 60601‑1 limits. | Bench dosimetry; software verification per IEC 62304. |
| Electrical shock | Dual‑input isolation, leakage current < 10 µA (IEC 60601‑1). | Electrical safety testing (EN 60601‑1 equivalent). |
| Detector failure leading to image loss | Redundant data buffering, self‑diagnostic checks. | Failure mode analysis; functional test. |
| Operator error from complex UI | Simplified workflow, clear on‑screen prompts, user training SOP. | Usability validation study. |

All controls must be traced in the Design History File (DHF) and reflected in the Risk Management File per ISO 14971:2019.

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Action |
|---------|-----------------------|--------|
| **No legally marketed predicate identified** (DP1 “No”) | SE not possible; De Novo or PMA required. | Notify Project Lead; initiate De Novo feasibility study. |
| **Intended use differs from all predicates** (DP2) | New clinical claim → higher regulatory burden. | Pause 510(k) preparation; reassess intended use scope. |
| **Technological differences raise new safety questions** (DP4 “Yes”) | FDA may require additional pre‑market data or a PMA. | Escalate to senior RA for risk‑benefit analysis and possible PMA routing. |
| **Performance data insufficient to meet or exceed predicate** (DP5 “No”) | Clearance denied; need more testing or redesign. | Trigger engineering review; plan supplemental bench/clinical studies. |
| **QMSR non‑compliance identified during document audit** | 21 CFR §820 violation blocks submission. | Immediate corrective action; involve quality assurance manager. |
| **UDI labeling not compliant with §§801.20+ or 830.20** | Labeling deficiency causes Refuse‑to‑Accept (RTA). | Pause submission; revise label; re‑submit to FDA RTA checklist. |
| **Major change to software algorithm after SE submission** (post‑clearance) | Requires Predetermined Change Control Plan (PCCP) per Dec 2024 guidance. | Prepare PCCP and submit as Additional Information (AI) request response. |

When any trigger is hit, the RA team must log a “Regulatory Escalation Note” in the project tracker and obtain approval from the regulatory manager before proceeding.

---

### 7. Peer‑Review Prompt  

> *Colleague, please review the above 510(k) strategy draft. In particular, challenge: (1) the assumption that an existing Class II X‑ray predicate is available; (2) whether all required testing (dose, safety, usability) aligns with current FDA guidance for radiographic devices; and (3) any jurisdictional gaps—e.g., UDI labeling nuances under Part 801 vs. Part 830, or QMSR evidence needed after the February 2026 transition.*  

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
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> §820.70을 'Design verification'으로 오귀속(구 QSR §820.70=생산·공정관리, 설계검증은 §820.30(d)이며 QMSR 2026-02 개편 후 제거조항 계열). Part 1020 'enforcement policy' 주제 오서술(실제=방사선 방출 성능기준) — hedged라 경미 처리.

**Source Excerpts**

1. Chunk `1061195424067242245`

> ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과제 3-2 SE 비교표 제출 필수 ---

2. Chunk `1072507187378217632`

> ### 4.1 SE 5단계 Decision Point (FDA 2014 Guidance Appendix A) ``` DP1. Predicate이 Legally Marketed Device인가? │ No → NSE (De Novo 또는 PMA) │ Yes ↓ DP2. 동일한 Intended Use인가? │ No → NSE │ Yes ↓ DP3. 동일한 Technological Characteristics인가? │ Yes → DP5 │ No ↓ DP4. 다른 기술특성이 Different Questions of Safety & Effectiveness를 제기하는가? │ Yes → NSE │ No ↓ DP5. 성능 데이터가 새 장치 ≥ Predicate 수준임을 입증하는가? │ Yes → SE (Clearance 가능) │ No → NSE ```

### kb-eval-20261116-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "cf2592659d90ded0", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cf2592659d90ded0`
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

> **Regulatory Draft – 510(k) Predicate Strategy**

---

### 1. Bottom‑Line Determination  

| Decision Point | Recommended Pathway |
|----------------|---------------------|
| **Device class (US)** – if the device is Class I or II *and* a legally marketed predicate exists → submit a **Traditional 510(k) (substantial equivalence)**. |
| If no suitable predicate but the device is “new” for its intended use and still falls in Class I‑II ⇒ pursue a **De Novo** request to create a new classification. |
| If the device is intrinsically high risk, requires permanent implant, or otherwise meets the definition of Class III – **PMA** is required (clinical data mandatory). |

*The final route depends on confirming the FDA product code & class for the specific intended use; this must be done before any submission is prepared.*

---

### 2. Required Evidentiary Elements (per pathway)

| Element | 510(k) – Traditional | De Novo | PMA |
|---------|----------------------|----------|-----|
| **Predicate device** | Mandatory – identify legally marketed device with same intended use, technology, and performance specifications. | Not required. | Not applicable; full pre‑market approval dossier needed. |
| **Clinical data** | Conditional – required only if the predicate does not adequately address safety/ efficacy of a new technological feature (source notes “조건부 (§3 참조)”). No specific identifier in source – verify separately. | “If applicable” per De Novo guidance; may be waived if non‑clinical testing is sufficient. | Mandatory – robust clinical investigation required (FD&C Act §515, 21 CFR 814). |
| **Non‑clinical data** (bench, animal, software validation) | Required to support substantial equivalence. | Required where applicable. | Required; must meet FDA’s risk‐based expectations. |
| **Risk Management** | ISO 14971:2019–compliant risk analysis & mitigations. | Same. | Same plus PMA‑specific benefit‑risk assessment. |
| **Quality System** | 21 CFR 820 (QMSR, effective 2026‑02; aligns with ISO 13485:2016). | Same. | Same (plus additional design‑control documentation). |
| **Labeling & UDI** | Label must carry a UDI per 21 CFR 801.20+; device identifier per 21 CFR 830 (formatting, GUDID submission). | Same. | Same. |
| **eSTAR registration** | Required for certain Class II devices beginning 2023‑10‑01 (source table lists eSTAR obligation “2023-10-01~”). Verify if device falls under eSTAR scope; otherwise not applicable. | Not required (source: “해당 없음”). | Not required. |
| **User Fee FY2025** | Approx. $22,171 (source). | Approx. $46,875 (source). | Approx. $438,330 (source). |

*All citations below correspond to the framework references from the source.*

---

### 3. Missing Information & Verification Needs  

| Item | Why it matters | Action |
|------|----------------|--------|
| **Exact intended use & indications** | Determines classification and predicate eligibility. | Obtain from product development team; map to FDA product codes. |
| **Identification of a suitable predicate (510(k) number, regulation‑cleared device)** | Required for SE claim. | Conduct 510(k) database search; confirm same technological characteristics. |
| **Clinical data requirement justification** – does the new feature trigger “conditional” clinical data per §3? | Source only mentions “조건부 (§3 참조)” without a specific citation. | Review FDA guidance (e.g., Guidance for Solid‑State X‑ray Imaging Devices) to ascertain if the device falls under the conditional clause; verify separately. |
| **eSTAR applicability** – is the device listed in the eSTAR registration list? | Source provides date range but not device‑specific status. | Cross‑check with FDA’s eSTAR database (2025 update). |
| **Risk analysis outputs & mitigations** | Must be aligned with ISO 14971:2019 and documented per 21 CFR 820. | Draft risk management file; identify any residual risks requiring post‑market controls. |
| **Software/AI change control plan** – if device includes software algorithms that may evolve, a Predetermined Change Control Plan (PCCP) is needed (FDA Dec 2024 guidance). | Not addressed in source. | Determine if PCCP applies; prepare draft if so. |

*All items flagged as “verify separately” because the source does not provide concrete identifiers.*

---

### 4. Core Risk Controls (to be reflected in the submission)

| Control | Regulatory Basis |
|--------|-------------------|
| **Design controls** – per 21 CFR 820.30 (including design verification & validation). | FDA QMSR (Part 820). |
| **Risk management** – ISO 14971:2019 process, documented in Design History File. | FDA expectation for all Class I‑III devices. |
| **Usability/ Human factors testing** – per IEC 62366‑1:2020, integrated into risk analysis. | Required when user error could lead to serious injury. |
| **Software validation & cybersecurity** – IEC 62443 and FDA’s Content of Premarket Submissions for Device Software (including PCCP if applicable). | FDA guidance on Cybersecurity (2024) & software lifecycle. |
| **Labeling & UDI compliance** – 21 CFR 801.20+ (label), 21 CFR 830 (UDI system). | Mandatory for marketing. |

---

### 5. Citations  

| Statement | Citation Type |
|-----------|---------------|
| Legal basis for 510(k) submission: **FD&C Act §510(k)**, **21 CFR 807**. | Framework reference (case 1). |
| De Novo legal basis: **FD&C Act §513(f)(2)**, **21 CFR 860**. | Framework reference. |
| PMA legal basis: **FD&C Act §515**, **21 CFR 814**. | Framework reference. |
| Clinical‑data condition for 510(k) (conditional): “조건부 (§3 참조)” – no specific identifier in source; verify separately. | Instance identifier (case 2). |
| eSTAR obligation start date “2023‑10‑01~” for 510(k) devices. | Instance identifier (source table). |
| FY2025 user‑fee estimates ($22,171 / $46,875 / $438,330). | Instance identifier (source table). |

All other standards (ISO 14971:2019, ISO 13485:2016, IEC 62304 2006+A1:2015, IEC 60601‑1 2005+A1:2012+A2:2020) are cited as **framework references** per the current edition list.

---

### 6. Human‑Escalation Triggers  

| Trigger | When to Escalate |
|---------|------------------|
| **Unclear classification or lack of predicate** – cannot determine SE claim. | Immediately to senior RA lead for product‑code mapping and predicate search. |
| **Clinical data requirement ambiguous** – “조건부 (§3)” without concrete guidance. | Pause submission preparation; request clarification from FDA via Pre‑Submission (Q‑Submission) or consult internal clinical affairs. |
| **eSTAR registration status unknown** – potential non‑compliance risk. | Escalate to regulatory compliance officer for eSTAR verification before filing. |
| **Budget breach on user fee** – projected FY2025 fee exceeds allocated budget. | Alert finance & project manager; consider alternative pathway (e.g., De Novo vs 510(k) if feasible). |
| **PCCP needed but not drafted** – AI/ML algorithm updates anticipated post‑market. | Engage software engineering lead to develop PCCP; involve senior RA for FDA guidance alignment. |

If any of the above triggers are hit, a formal **Regulatory Decision Memo** must be prepared and routed for sign‑off before proceeding.

---

### 7. Peer Review Prompt  

> *Please review the assumptions underlying the classification decision (especially the device’s intended use and predicate availability), the completeness of the evidence matrix (clinical vs non‑clinical data), and any jurisdiction‑specific gaps such as eSTAR applicability or PCCP requirements that may have been omitted from this draft.*

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> §820.30 design controls를 현행 요건으로 인용 — QMSR(2026-02-02) 개편으로 제거된 구 조항 잔존(계열). 나머지 인용(De Novo §513(f)(2)/860, PMA §515/814, UDI 분할) 정확.

**Source Excerpts**

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20261116-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f7b5965676144e9c", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f7b5965676144e9c`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_02_Substantial_Equivalence.md)
- Source hash: `3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_02_Substantial_Equivalence.md`는 FDA 510(k) substantial equivalence와 predicate 비교 항목을 정리한 eSTAR 작성 문서입니다.
- 현재 excerpt 핵심: ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medi...
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

> **Regulatory Draft – Imaging Workstation Software (GUI) 510(k) Strategy**

| Item | Determination & Required Evidence | Gaps / Missing Information | Action Needed |
|------|-----------------------------------|----------------------------|---------------|
| **Device Classification** | Class II imaging device – *Medical image management and processing system* (software) → **21 CFR §892.2050** (Class II). | None identified. | Confirm that the intended use stays within the functional scope of §892.2050 (acquisition, processing, display, storage, transfer, worklist, QA tools). |
| **Submission Pathway** | Standard 510(k) Premarket Notification – **21 CFR §807**. Use “Traditional” substantial‑equivalence route; no De Novo needed because a clear predicate exists in the imaging software space. | Predicate device(s) not yet selected. | Conduct predicate search (product‑code based, FDA 510(k) database) per checklist item 1. |
| **Predicate Selection – Checklist** (source [1])<br>• Search by product code → identify recent (<5 yr) clearances.<br>• Prefer predicates still on the market; verify retired/discontinued status.<br>• Check MAUDE/Recall DB for any safety communications.<br>• Compare Indications‑for‑Use (IFU) text – must be identical or narrower.<br>• List technical differences & provide justification data per item. | • No specific predicate numbers supplied in source → **no specific identifier found in source — verify separately**. | Populate the above checklist with at least one primary predicate; document all comparative tables. |
| **Software Documentation Level** (source [2])<br>– Follow FDA 2023 Software Guidance (Basic vs Enhanced).<br>– IEC 62304 safety class (A/B/C) determination.<br>– Provide functional list (Acquisition, Processing, … QA Tools). | • Safety class not yet assigned (A/B/C).<br>• AI/ML module presence unknown. | Conduct IEC 62304 classification; if AI/ML present draft a **Predetermined Change Control Plan (PCCP)** per FDA Dec‑2024 guidance. |
| **Technical Evidence Required** | 1. **Device Description & Architecture** – block diagram, software modules, interfaces.<br>2. **DICOM Conformance Statement** – list of SCU/SCP services (Storage, Worklist, MPPS, Print etc.).<br>3. **Interoperability Claims** – HL7 FHIR, IHE profiles supported (if any).<br>4. **Operating System & Minimum Hardware Requirements**.<br>5. **Security Measures** – authentication method, encryption, audit logs, update mechanism.<br>6. **Software Bill of Materials (SBOM)** – SPDX or CycloneDX format.<br>7. **Verification & Validation Data** – unit, integration, system testing; performance testing for each function listed.<br>8. **Risk Management Report** – ISO 14971:2019 risk analysis, risk control measures, residual risk evaluation.<br>9. **Labeling & IFU** – indications, contraindications, warnings, UDI placement (see below). | • No detailed UI/UX hazard analysis.<br>• No cybersecurity post‑market management plan (FDA guidance 2022).<br>• SBOM format not yet decided.<br>• Interoperability standards support not specified. | Gather these deliverables; map each to the corresponding FDA guidance or standard. |
| **Quality System Requirements** | • **QMSR** – compliance with 21 CFR §820 (effective Feb 2026, ISO 13485:2016‑aligned).<br>• Device‑specific SOPs (e.g., `SOP-RA‑002`, `SOP-PMA-001`) to demonstrate design controls and post‑market surveillance. | None specific; need evidence of QMS implementation for this software line. | Provide device‐level QMS excerpt (design history file, risk management file, etc.). |
| **UDI Requirements** | • Label must bear a UDI – placement per **21 CFR §801.20‑§801.50** (Part 801).<br>• Formatting & issuance per **21 CFR §830.20**, agency accreditation §§830.100‑830.130, and GUDID submission §§830.300‑830.360. | No UDI assigned yet. | Obtain issuing‑agency identifier; prepare label mock‑up with plain‑text and AIDC barcode/QR. |
| **Risk Controls** (ISO 14971:2019) | • Identify software‐related hazards (mis‑display, data loss, unauthorized access).<br>• Apply IEC 62304 design controls per safety class.<br>• Implement cybersecurity safeguards (encryption, authentication, logging).<br>• Conduct user‑interface hazard analysis (ISO 62366‑1:2020). | • Hazard list not provided.<br>• Residual risk acceptance criteria undefined. | Complete a full Risk Management File; include verification of each control. |
| **Human‑Escalation Triggers** | 1. **Predicate Uncertainty** – no suitable primary predicate found or predicate is discontinued/recall‑subject → senior RA review before filing.<br>2. **AI/ML Inclusion Without PCCP** – must develop & FDA‑reviewed PCCP; escalation to regulatory counsel if timeline impacts launch.<br>3. **Residual Risk > Acceptable Level** after risk analysis → require redesign or additional mitigations; escalates to senior engineering and RA leadership.<br>4. **Security Gaps** (e.g., missing encryption, inadequate audit logs) – trigger cybersecurity specialist review and possible FDA pre‑market discussion.<br>5. **Classification Ambiguity** (possible Class I if functions limited) → seek FDA classification request or use Q-Submission to confirm class before proceeding. |
| **Citations** | • **21 CFR §892.2050** – Imaging work‑station software classification (Framework reference).<br>• **21 CFR §807** – 510(k) requirements (Framework).<br>• **21 CFR §820** – Quality System Regulation (Framework).<br>• **21 CFR §801.20‑§801.50** – UDI label placement (Framework).<br>• **21 CFR §830.20, §830.100‑§830.130, §830.300‑§830.360** – UDI system & GUDID (Framework).<br>• **ISO 14971:2019**, **ISO 13485:2016**, **IEC 62304:2006+A1:2015**, **IEC 62366‑1:2020** (Framework).<br>• FDA 2023 Software Guidance – Basic/Enhanced documentation (source [2] provides context; no identifier to quote).<br>• Predetermined Change Control Plan (PCCP) guidance – Dec 2024 (Framework).<br>• Source checklist items – predicates, recall check, IFU comparison (source [1]). | No instance‑specific identifiers (e.g., 510(k) numbers, MAUDE case IDs) appear in the excerpts; therefore none are inserted. |
| **Next Steps** | 1. Execute predicate search and complete checklist (source [1]).<br>2. Draft comparative summary table with IFU text side‑by‑side.<br>3. Perform IEC 62304 safety class assignment; document AI/ML scope and create PCCP if needed.<br>4. Assemble software documentation package per FDA 2023 guidance (Basic vs Enhanced).<br>5. Complete risk management file (ISO 14971) and cybersecurity plan.<br>6. Generate labeling mock‑up with UDI placement.<br>7. Review all items against the “Human‑Escalation Triggers” list; route any flagged items to senior RA or regulatory counsel. | – | – |

---

**Peer‑Review Prompt**

*Please review this draft and challenge the following points:*  

1. **Predicate Choice** – Is a single primary predicate truly sufficient, or would a split‑predicate approach ever be defensible for this software?  
2. **Classification Accuracy** – Does the functional list (including QA tools) risk moving the device toward a higher‑risk category that might require a different part of 21 CFR (e.g., Part 892.2010 for storage only)?  
3. **AI/ML Scope** – Are we assuming too much by requiring a PCCP only when “AI/ML module” is present; could certain algorithmic features trigger FDA’s “Software as a Medical Device” (SaMD) criteria even without explicit AI/ML labeling?  
4. **Cybersecurity Evidence** – Does the draft adequately reflect the post‑market cybersecurity management guidance, or should we add a dedicated “Cybersecurity Vulnerability Management Plan”?  

*Identify any jurisdiction‑specific gaps (e.g., missing references to Part 806 for field safety notices) and suggest additional evidence that may strengthen the 510(k) submission.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. §892.2050='Medical image management and processing system' Class II — eCFR 원문 확인 정확. 미세 관찰: 'cybersecurity post-market plan (FDA guidance 2022)' 연도 미검증(현행 사이버 가이던스는 2023-06). [최종 2점 — shadow 8차 하향 수용: ① 'cybersecurity post-market plan (FDA guidance 2022)' — 현행 premarket 사이버 가이던스는 2023-09 final(2025 갱신), postmarket은 2016 — '2022'는 비존재 판번 인용 ② 'no De Novo needed because a clear predicate exists' — 동일 문서가 predicate 미선정을 gap으로 명시, 근거 없는 경로 결론.]

**Source Excerpts**

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20261116-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "cf706c61baa2606d", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cf706c61baa2606d`
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

> **Regulatory Draft – 510(k) Predicate Strategy for “Radiographic Acquisition & Control GUI Software”**

| Item | Assessment |
|------|-------------|
| **Device Function / Intended Use** | A software application that runs on a workstation in the X‑ray suite and provides (i) acquisition control of compatible digital X‑ray detectors/generators, (ii) image review and management, and (iii) DICOM work‑list/MPPS services.  Not intended for primary diagnosis or image interpretation. |
| **Regulatory Class / FDA Product Code** | **Class II** – likely falls under **21 CFR Part 892**, **§892.2050 “Medical image management and processing system”** (PACS‑type software). The acquisition‑control aspect is covered by this section; no separate “image digitizer” classification is appropriate because the device does not convert analog signals to digital. |
| **Submission Route** | Traditional 510(k) (or abbreviated if a suitable predicate with identical intended use is identified). No De Novo needed unless no predicate exists. |
| **Potential Predicate Devices** | • FDA‑cleared X‑ray acquisition/work‑list software (e.g., “Model XYZ” – Kxxxxxx, cleared under §892.2050). <br>• Clearances that list “digital radiography acquisition and image management” as intended use.  *(Exact numbers must be retrieved from the FDA 510(k) database; not present in source.)* |
| **Core Submission Content (per 21 CFR §807.87 & Guidance “Format for Traditional and Abbreviated 510(k)s”)** | 1. **Device Description** – software architecture, modules, DB schema, DICOM nodes (Storage SCU, Worklist SCU, MPPS). <br>2. **Indications for Use** – Form 3881; include the exact phrasing quoted in source. <br>3. **Software Classification** – IEC 62304 safety class (A/B/C) as identified. <br>4. **SOUP Inventory** – list, version, supplier, justification. <br>5. **Hardware Requirements** – OS, minimum CPU/RAM, supported detector/generator models. <br>6. **DICOM Conformance Statement** – declaration of compliance with relevant SOPs (Storage SCU, Worklist SCU, MPPS). <br>7. **Cybersecurity Information** – authentication, encryption, audit‑log mechanisms (per FDA “Postmarket Management of Cybersecurity” guidance). <br>8. **Risk Management File** – ISO 14971:2019 risk analysis, including software‑related hazards and mitigations. <br>9. **Verification & Validation Data** – functional testing, image quality metrics (spatial resolution, contrast, DQE), interoperability tests with each listed detector/generator version, usability testing with trained technologists. <br>10. **Labeling & UDI** – device label per 21 CFR §801.20+ (UDI placement) and Part 830 system identifier submission to GUDID. <br>11. **QMS Evidence** – ISO 13485:2016‑aligned quality system, compliance with the new QMSR (21 CFR Part 820). |
| **Missing / To Be Obtained from Sponsor** | • Full list of comparable cleared 510(k) numbers (predicate search). <br>• Quantitative performance test reports (image quality, DICOM interoperability, latency). <br>• Complete ISO 14971 risk management report (including residual risk assessment). <br>• Cybersecurity threat model and mitigation plan. <br>• Software validation master record (including sample size, statistical analysis). <br>• UDI label artwork & GUDID submission package. |
| **Key Risk Controls** | • IEC 62304 processes (software development lifecycle, configuration management). <br>• ISO 14971‑based risk mitigation: error detection, safe‑state shutdown, user alerts for acquisition failures. <br>• Cybersecurity controls: role‑based access, TLS encryption of DICOM traffic, immutable audit log, periodic vulnerability scanning. <br>• Predetermined Change Control Plan (PCCP) if future algorithm updates are anticipated. |
| **Citations (Framework Only)** | • 21 CFR Part 892 – imaging device classification. <br>• 21 CFR §892.2050 – medical image management and processing system (Class II). <br>• 21 CFR Part 807 §§807.87, 807.92 – required content of a 510(k) & Summary. <br>• FDA Guidance “Electronic Submission Template for Medical Device 510(k) Submissions” (eSTAR v5.x, 2023). <br>• FDA Guidance “Format for Traditional and Abbreviated 510(k)s” (Sept 13 2019). <br>• FDA Form 3881 – Indications for Use. <br>• IEC 62304:2006+A1:2015 – software life‑cycle processes. <br>• ISO 14971:2019 – risk management for medical devices. <br>• 21 CFR Part 801 §§801.20+ – UDI label placement. <br>• 21 CFR Part 830 §§830.20, 830.100‑130 – UDI system requirements. |
| **Human‑Escalation Triggers** | 1. **Predicate Uncertainty** – If no suitable cleared 510(k) is found within §892.2050, pause and consult senior RA or consider a De Novo request. <br>2. **Classification Dispute** – If FDA reviewer questions whether the software is “image acquisition” vs “diagnostic image processing,” refer to senior regulatory counsel for clarification before resubmission. <br>3. **Missing Performance Data** – Absence of objective image‑quality or interoperability data → halt submission preparation and request additional testing from the sponsor. <br>4. **Cybersecurity Gaps** – If threat model does not meet FDA “Postmarket Management of Cybersecurity” expectations, escalate to cybersecurity specialist for remediation. <br>5 UD​I/Labeling Ambiguities – Unclear label placement per §801.20+ → route to labeling lead for final artwork approval before filing. |
| **Regulatory Judgment** | The product is a Class II imaging‑software device under 21 CFR §892.2050 and should be cleared via a traditional (or abbreviated, if predicate identical) 510(k). All required sections listed in §807.87 must be compiled; the sponsor must furnish the missing performance, risk‑management, cybersecurity, and UDI evidence before submission can be finalized. |

---

**Peer Review Prompt**

> *Colleague, please review the following aspects: (1) suitability of §892.2050 as the primary classification versus alternative Part 892 sections; (2) completeness of predicate identification strategy given the limited source excerpts; (3) any US‑specific evidence gaps not addressed above (e.g., electromagnetic compatibility, human factors testing); and (4) whether the escalation triggers capture all scenarios that could stall the 510(k) review.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
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
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

## ra_eu

### kb-eval-20261116-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "ef4870b1ce663e1e", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `ef4870b1ce663e1e`
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

> **Regulatory Draft – Classification & Conformity Assessment for an X‑ray Diagnostic Device (Ionising‑radiation emitting equipment)**  

---

### 1. Device Synopsis (derived from source)

| Item | Description |
|------|-------------|
| **Intended purpose** | Generation of ionising radiation for diagnostic imaging (e.g., radiography / fluoroscopy). |
| **Key technology** | X‑ray tube assembly, high‑voltage generator and control electronics; may include software that processes images. |
| **Regulatory source excerpt** | “Rule 10: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb)”【2】. |

---

### 2. Classification  

| Reference | Determination |
|-----------|---------------|
| **Rule 10 – radiology limb** (ionising‑radiation emitting diagnostic device) | Places the device in **Class IIb** (Annex VIII, Rule 10). |
| **Rule 11** (SaMD) – applies only if a separate software component makes independent diagnostic decisions; otherwise classification follows Rule 10. | No extra class uplift needed unless the software alone meets the higher criteria of Rule 11 (e.g., decision‑making that could cause serious deterioration → possible Class IIb/III). |

**Citations:** Rule 10 (Annex VIII) – Class IIb; Annex I §§16 (radiation protection) applies.  

---

### 3. Conformity Assessment Route  

| Device class | Art. 52 paragraph | Mandatory route(s) |
|--------------|-------------------|--------------------|
| **Class IIb** | Art 52(4) | • **Annex IX** – full QMS (ISO 13485:2016) + technical‑documentation assessment by a Notified Body  <br>or <br>• **Annex X + Annex XI** – type‑examination followed by production conformity verification. |

*Decision:* Select the route that matches the manufacturer’s existing quality system and NB capacity.  

**Citations:** Art 52(4); Annex IX; Annex X & XI.  

---

### 4. Evidence Required for Submission (per MDR)

| Evidence | Regulatory basis | What must be supplied |
|----------|-------------------|-----------------------|
| **Technical Documentation (TD)** – device description, design‑manufacturing information, labeling, etc. | Annex II §§1‑6 (structure) |
| **Risk Management File** (including risk analysis, evaluation of residual risks) | Annex I §3 (risk‑management system) – implement ISO 14971:2019 |
| **Clinical Evaluation Report (CER)** – state‑of‑the‑art literature review, clinical data, benefit–risk analysis | Annex XIV Part A; kept current under Art 61 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B |
| **Post‑Market Surveillance (PMS) System** – procedures, plan and periodic report | Art 83 (system); Art 84 (plan) |
| **Periodic Safety Update Report (PSUR)** – every 2 years for Class IIb | Art 86(1)/(2) |
| **Usability engineering file** (if device used by lay persons or has complex UI) | Annex I §22; IEC 62366‑1:2020 |
| **Software development lifecycle evidence** (if SaMD component) | IEC 62304:2006+A1:2015 |
| **Electrical safety & performance testing** (IEC 60601‑2‑54 for X‑ray equipment) | IEC standard reference – required by GSPR §16.4 |
| **Labeling & IFU** – content per Annex I §23 | Annex I §23 |
| **Declaration of Conformity (DoC)** – signed EU DoC with Annex IV content | Art 19; Annex IV |

---

### 5. Gaps / Missing Information (to be clarified before NB submission)

1. **Precise Intended Use Statement** – wording, clinical indications, patient population.  
2. **Complete Device Description** – dimensions, materials, electrical specifications, radiation output parameters.  
3. **Clinical Data Package** – results of any pre‑market clinical investigations or post‑market data that support safety & performance.  
4. **Software Scope Definition** – whether the image‑processing software is a separate SaMD; if so, classification under Rule 11 must be documented and supporting evidence (software verification/validation) supplied.  
5. **Risk Control Measures for Radiation** – quantitative shielding calculations, dose limits, interlocks.  
6. **Usability Validation** – test reports covering intended operators (radiographers, doctors).  
7. **Manufacturing Process Description & Supplier Controls** – especially for X‑ray tube assemblies (IEC 60601‑2‑28 relevance).  
8. **Labeling / IFU Drafts** – in all required languages; conformity with Annex I §23.  
9. **Post‑Market Surveillance Plan Details** – methodology, data sources, trigger thresholds.  
10. **PSUR Schedule & Initial Data** – sales volume forecast and population size for first reporting period.

*Each missing element must be obtained or generated before the technical file is considered complete.*

---

### 6. Core Risk Controls (aligned with GSPR)

| Risk category | Control measure | Regulatory reference |
|----------------|-----------------|-----------------------|
| **Ionising radiation exposure** | Built‑in dose‑monitoring, interlocks, shielding; compliance with IEC 60601‑2‑54 and Annex I §16.4 (radiation protection). |
| **Electrical safety** | Ground fault detection, leakage current limits per IEC 60601‑1; Annex I §20. |
| **Software errors / misinterpretation** | IEC 62304 lifecycle, IEC 62366 usability engineering, validation against clinical algorithms; Annex I §§17–18. |
| **Use‑error (operator)** | Training program, clear labeling (Annex I §23), ergonomic UI design; Annex I §22. |
| **Mechanical/thermal hazards** | Material selection, temperature monitoring, mechanical integrity testing; Annex I §20. |
| **Residual risk evaluation** | Overall benefit‑risk assessment documented in CER and RMF; Annex I §§8‑9. |

---

### 7. Human‑Escalation Triggers (when to pause/seek higher‑level decision)

| Trigger | Action required |
|---------|-----------------|
| **Unresolved classification of software component** (Rule 11 may up‑classify) | Escalate to senior RA lead; consider re‑classification to Class III and adjust conformity route. |
| **Insufficient clinical evidence for safety/performance** | Stop dossier finalisation; initiate additional clinical investigation or collect post‑market data before NB review. |
| **GSPR non‑compliance identified in risk analysis** (e.g., radiation dose exceeds limits) | Immediate mitigation design change; re‑run verification & validation. |
| **NB indicates need for a type‑examination (Annex X)** after initial Annex IX review | Re‑plan conformity route, allocate resources for additional testing and certificate issuance. |
| **PMS/PMCF plan lacks measurable objectives or data sources** | Suspend submission; develop detailed PMS procedure per Art 84. |
| **Labeling draft fails Annex I §23 checklist** | Pause until revised labeling approved by regulatory affairs manager. |
| **Sales forecast unknown → PSUR volume calculations impossible** | Obtain market launch data before finalising PSUR schedule (Art 86). |

---

### 8. Summary Judgment  

*The device is a diagnostic X‑ray system emitting ionising radiation and therefore falls under **Rule 10 (Annex VIII) → Class IIb**. The appropriate conformity assessment route is either **Annex IX** (full QMS & technical‑documentation assessment) or the combination **Annex X + Annex XI** (type‑examination plus production verification), as mandated by **Art 52(4)**. A complete MDR‑compliant dossier must include the items listed in Section 4, with particular attention to clinical evidence, radiation‑specific risk controls, and a robust PMS/PMCF programme. All identified gaps (Section 5) must be closed before the Notified Body can issue conformity assessment. Any of the escalation triggers in Section 7 should provoke an immediate halt of the submission process until resolved.*

---

### 9. Peer‑Review Prompt  

> **Colleague, please review:**  
> - Are there any additional MDR or GSPR clauses (e.g., Annex I §§14–15 for electromagnetic compatibility) that we have omitted for X‑ray equipment?  
> – Does the proposed evidence list fully satisfy the requirements of Annex II §6.1 and Annex XIV Part A/B for a Class IIb device with a software component?  
> – Have we correctly identified all potential classification interactions between Rule 10 (device) and Rule 11 (software), or is a more detailed software hazard analysis required?  

*Your feedback will be used to refine the dossier before the Notified Body review.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
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
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261116-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "36ae8240718c2a9b", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `36ae8240718c2a9b`
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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Route**  
*(Prepared for internal EU RA review)*  

---

### 1. Scope of the Assessment  

| Item | Current knowledge (from source) |
|------|----------------------------------|
| **Regulation** | Medical Device Regulation (EU) 2017/745 (MDR) |
| **Key regulatory extracts quoted** | • Classification rules – Article 51 + Annex VIII (source [2])  <br>• Clinical‑evaluation requirements – Article 61 & Annex XIV Part A (source [1])  <br>• UDI & EUDAMED obligations – “UDI portal” & “EUDAMED UDI/DEV” (source [1])  <br>• Post‑market surveillance – Vigilance Art. 87, PSUR (source [1])  <br>• Authorized Representative – Article 11 (source [1]) |
| **Device description** | *Not provided in source* – must be supplied by the manufacturer before any classification can be finalised. |

---

### 2. Classification Determination  

1. **Manufacturer‑led self‑classification** is mandatory (Article 51 & Annex VIII) – the maker bears full responsibility for selecting the correct rule(s) and class (source [2]).  
2. **Procedure**  
   - List all intended uses, indications, and modes of action of the device.  
   **→ Missing:** detailed intended‑use statement, patient population, anatomical site, duration of contact, energy source, software functions, etc.  
   - Apply Annex VIII rules sequentially (Rule 1 → Rule 22) and adopt the *highest* class reached (source [2]).  
   - If any doubt remains, consult the **Competent Authority** or the MDCG “Borderline and Classification” Manual v2.1.1 (2023‑09) (source [2]).  

3. **Potential outcomes (examples)** – *illustrative only*; final class depends on the data supplied:  

| Rule(s) triggered | Example device type | Resulting Class |
|-------------------|--------------------|-----------------|
| Rule 9 (active therapeutic) | Energy‑delivering wound‑healing system | IIa or IIb (energy hazardous) |
| Rule 10 (diagnostic – radiology limb) | X‑ray generator for projection imaging | **IIb** |
| Rule 11 (software decision support) | AI‑based diagnosis aid | IIa → IIb → III depending on impact |
| Rule 17 (human/animal tissue) | Tissue‑engineered skin graft | **III** |

> **Action:** Populate the “Classification Matrix” with the manufacturer’s device description and map each attribute to the relevant Annex VIII rule(s).  

---

### 3. Conformity‑Assessment Route (Art. 52)  

| Device Class | Mandatory route (per Art. 52) | NB involvement | Required MDR references |
|--------------|-------------------------------|----------------|--------------------------|
| **I** (non‑sterile, non‑measuring, non‑reusable surgical) | Self‑declaration – technical documentation (Annex II & III) + EU Declaration of Conformity (Art. 19/Annex IV) | No NB | Art. 52(7) |
| **Is / Im / Ir** | Annex IX Chapters I & III *or* Annex XI Part A (limited scope) | Yes (limited) | Art. 52(7) |
| **IIa** | Annex IX (QMS + technical‑documentation assessment of a representative device) **or** Annex II/III + Annex XI §10 or §18 | Yes | Art. 52(6) |
| **IIb** | Annex IX (full TD assessment) **or** Annex X + Annex XI (type‑examination & production verification) | Yes | Art. 52(4) |
| **III** | Annex IX (full TD assessment) **or** Annex X + Annex XI | Yes | Art. 52(3) |

> **Decision point:** Once the Class is fixed, select the appropriate route and inform the manufacturer of the required NB contract scope (e.g., “Annex IX – full technical‑documentation audit”).  

---

### 4. Evidence Package Required for Submission  

| Evidence area | MDR citation* | Typical contents |
|---------------|----------------|------------------|
| **Technical Documentation** | Annex II §1‑6 (incl. design, GSPR, risk management, verification/validation) | Device description, intended use, labeling (Annex I §23), manufacturing process, etc. |
| **Risk Management File** | Annex I Chapter I §3 (risk‑management system) – ISO 14971:2019 (framework) | Risk analysis, control measures, residual risk evaluation, evaluation of benefit‑risk (Art. 61). |
| **Clinical Evaluation Report (CER)** | Article 61 & Annex XIV Part A (clinical‑evaluation) | State‑of‑the‑art literature review, clinical data (post‑market or investigations), justification of equivalence where used. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan / Report** | Annex XIV Part B (PMCF) | Planned post‑market studies, criteria for success, schedule, updates. |
| **PMS System & Reports** | Art. 83 (system), Art. 84 (plan), Art. 85 (Class I report), Art. 86 (PSUR for IIa/IIb/III) – Vigilance Art. 87 (serious‑incident reporting) | PMS plan, periodic safety update reports (frequency per class). |
| **UDI & EUDAMED Registration** | UDI portal / EUDAMED reference in source [1] | Device identifier, manufacturer info, registration of the device model and variants. |
| **Authorized Representative Declaration** | Article 11 (AR) – source [1] | Contract with EU‑based AR, proof of competence. |
| **Declaration of Conformity** | Art. 19 (DoC content per Annex IV) – not directly quoted but required for all classes. |

\*Framework references are provided without “verify separately” caveat.

---

### 5. Identified Gaps / Missing Information  

| Gap | Why it matters | Required action |
|-----|----------------|-----------------|
| **Complete device description & intended use** | Needed to apply Annex VIII rules and populate technical documentation (Annex II). | Request from manufacturer – include indication, patient population, mode of operation, software functions, energy source, etc. |
| **Classification‑rule mapping table** | Without a rule matrix the class cannot be justified; NB will flag this. | Manufacturer to fill in “Rule‑mapping worksheet”. |
| **Clinical data (pre‑market or equivalence)** | CER must be current per Art. 61 – otherwise NB will request additional investigations. | Gather CE marked predicate devices, clinical investigation reports, or real‑world evidence. |
| **Risk analysis outcomes** | Required for Annex I §3 and to support benefit‑risk determination (Art. 61). | Provide ISO 14971 risk‑management file; identify any residual risks not mitigated. |
| **Post‑market surveillance plan** | Art. 84 demands a PMS plan; Art. 86 PSUR schedule must be defined per class. | Draft PMS/PMCF plan, assign responsibilities. |
> **Human escalation trigger:** If any of the above items cannot be supplied within 4 weeks, elevate to the Project Lead and consider pausing the conformity‑assessment timeline.

---

### 6. Risk Controls – Minimum Requirements (Annex I)  

| Annex I § | Control requirement | Typical implementation |
|-----------|---------------------|------------------------|
| §3 (Risk‑management system) | Establish RMF per ISO 14971:2019 | Documented risk analysis, evaluation of residual risk, benefit‑risk justification. |
| §4 (Risk control) | Apply inherent safety measures, protective measures, informational warnings | Design safeguards, software error handling, alarm thresholds. |
| §5 (Use‑error) | Identify and mitigate user errors through design or labeling | Human factors testing (IEC 62366‑1:2020), clear IFU (Annex I §23). |
| §6 (Device lifetime) | Define service life, maintenance schedule | Longevity claims validated by durability testing. |
| §7 (Transport & storage) | Verify robustness under intended logistics conditions | Packaging validation, temperature/humidity limits. |
| §8 (Known and foreseeable risks vs benefits) | Overall benefit‑risk determination | Integrated into CER conclusion (Art. 61). |
| §16 (Radiation protection – if applicable) | Comply with IEC 60601‑2‑54 & MDR §16.4 for ionising radiation | Shielding calculations, dose limits, safety interlocks. |

> **Note:** Specific risk controls will be refined once the device’s functional and technological characteristics are clarified.

---

### 7. Human‑Escalation Triggers (Decision Log)  

| Trigger condition | Escalation level | Responsible party |
|-------------------|------------------|--------------------|
| Missing or ambiguous intended‑use description > 4 weeks | **Level 1** – Project Manager | RA Lead |
| No mapping to Annex VIII rule after two classification attempts | **Level 2** – Senior Regulatory Counsel | RA Lead |
| Incomplete CER (no clinical data, no equivalence) after 6 weeks post‑request | **Level 3** – Head of Regulatory Affairs | Clinical Evaluation Team |
| NB requests additional evidence that exceeds original scope (e.g., new clinical investigation) | **Level 4** – Executive Sponsor | QA/Regulatory Management |
| Any regulatory deadline (e.g., PSUR submission date) at risk of breach | Immediate escalation to **Compliance Officer** and **Legal** | Project Coordinator |

---

### 8. Summary Judgment  

- **Current status:** Only high‑level procedural references are known; the device’s substantive characteristics are missing, preventing a definitive classification or route selection.  
- **Next steps:** Obtain full intended‑use dossier from the manufacturer, complete Annex VIII rule mapping, and assemble the evidence pack outlined in Section 4.  
- **Escalation:** If any of the critical gaps (device description, clinical data, risk analysis) cannot be resolved within the timelines above, trigger Level 1 escalation.

---

### 9. Peer‑Review Prompt  

> *Colleague, please review this draft for:*  
> - Completeness of the classification‑rule check given only the high‑level MDR extracts.  
> - Whether any additional EU‑specific obligations (e.g., EUDAMED registration deadlines, UDI batch‐release procedures) should be added at this stage.  
> - Potential jurisdictional blind spots, especially concerning cross‑border equivalence claims or reliance on non‑EU clinical data.  

*Your feedback will ensure that no hidden assumption remains unchecked before we request the missing manufacturer information.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
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
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. Art.52 전 계열(7/6/4/3, IIa 대안 Annex II/III+XI §10/§18) 정확, Rule 17=인체·동물조직 III 정확(11-10 정정 정착). 미세 관찰: 'MDUFA IV (FY2026)'은 source 원문 표기 인용(FY2026은 MDUFA V 시기 — KB 원본 후보).

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261116-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "8dd68d6ceb924d26", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md", "source_hash": "9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `8dd68d6ceb924d26`
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

> **Regulatory Draft – MDR 2017/745 Classification & Conformity‑Assessment Planning**

---

### 1. Device Summary (as far as can be extracted from the source)

| Item | Current status (from the DoC template) | Gap / What is needed |
|------|----------------------------------------|----------------------|
| **Manufacturer name** | Placeholder `[회사명]` | Confirm legal entity name and address. |
| **EUDAMED SRN** | Placeholder `[EUDAMED SRN — 미취득 시 공백]` | Obtain a registered SRN or note that one is pending – must be filled before DoC issuance. |
| **Authorized Representative (AR)** | Placeholder `[EU 대리인명 및 주소 — 역외 제조사 해당 시]` | If the manufacturer is located outside the EU, provide AR name and address; otherwise state “Not applicable”. |
| **Basic UDI‑DI** | Placeholder `[…]` – see Annex VI Part C | Allocate a Basic UDI‑DI in the EUDAMED database. |
| **Product identification** (name, trade name, model/Catalogue number) | Place‑holders `[제품명]`, `[상품명]`, `[모델 번호 / 카탈로그 번호]` | Exact product name and model numbers are required for traceability and for the DoC. |
| **Intended use** | Placeholder “[…]” (brief description) | A clear, concise statement of the device’s intended medical purpose, target patient group, clinical indications, and mode(s) of action is mandatory – it drives classification (Art. 2(1)). |
| **Signature block** | Completed with signer name/role | Verify that the signatory has full authority (e.g., CEO or QA Director). |

> **Regulatory implication:** The DoC cannot be finalized until all placeholders are populated with verified data. The missing items also prevent any classification analysis because the *intended use* and *technology description* are unknown.

---

### 2. Classification – How it will be determined

| Step | Action | Regulatory reference |
|------|--------|-----------------------|
| **2.1 Identify intended purpose & mode of action** | Obtain the definitive “Intended use” text (see above). | Art. 2(1) MDR 2017/745 |
| **2.2 Map to Annex VIII classification rules** | Apply the appropriate rule(s) (e.g., Rule 9, 10, 11, 17, etc.) based on whether the device is active, invasive, software‑driven, uses a measuring function, or contains human/animal tissue/cells. | Annex VIII |
| **2.3 Determine risk class** | *Result* will be I, Is/Im/Ir, IIa, IIb, or III. | Art. 52 MDR (class → conformity‑assessment route) |

> **Current status:** No classification can be assigned – the source does not disclose any of the technical or clinical characteristics required to select a rule. *Missing information*: full intended use description plus device architecture (active/passive, invasive/non‑invasive, software component, radiation emission, etc.).

---

### 3. Conformity‑Assessment Route (once class is known)

| Class | Mandatory route (Art 52) | Notified Body involvement |
|-------|--------------------------|----------------------------|
| **I** (non‑sterile, non‑measuring, non‑reusable surgical) | Art. 52(7): self‑declaration – technical documentation (Annex II & III) + EU Declaration of Conformity (Annex IV). | No NB required. |
| **Is / Im / Ir** | Art. 52(7): Annex IX Chapters I & III *or* Annex XI Part A (limited scope for sterile, measuring or reusable surgical aspects). | NB required for the specific aspect. |
| **IIa** | Art. 52(6): Annex IX (QMS + technical‑doc assessment of a representative device) **or** Annex II + III together with Annex XI §10/§18. | NB required. |
| **IIb** | Art. 52(4): Annex IX (full QMS + technical‑doc assessment of each generic group) **or** Annex X (type‑examination) combined with Annex XI (production conformity verification). | NB required – either route A or B. |
| **III** | Art. 52(3): Annex IX (full assessment) **or** Annex X + Annex XI. | NB required – full assessment mandatory. |

> **Citation:** “Annex IV” for DoC content; “Art. 19” outlines the legal basis and mandatory content of the EU Declaration of Conformity (minimum items listed in Annex IV).  

---

### 4. Evidence Package Required for Technical Documentation (Annex II §6)

| Section | Required evidence | Typical sources |
|---------|-------------------|-----------------|
| **4.1 Device description & specification** | Full device description, variants, accessories, intended purpose, mode of action, labeling. | Design specifications, product catalogue, label art. |
| **4.2 Manufacturing information** | Process flow diagram, quality‑system procedures, manufacturing sites. | ISO 13485:2016 QMS records. |
| **4.3 General Safety & Performance Requirements (GSPR) compliance** | Demonstration of conformity with each of the 23 GSPR (Annex I). | Risk Management File, test reports, clinical data. |
| **4.4 Benefit‑risk analysis** | Updated benefit‑risk determination (incl. residual risk evaluation). | RMF conclusions + clinical evaluation summary. |
| **4.5 Verification & validation** | Bench testing, performance testing, sterility verification (if applicable), software verification/validation (IEC 62304, IEC 62366‑1). | Test reports, validation protocols. |
| **4.6 Clinical Evaluation Report (CER)** | State of the art literature review, clinical data from investigations or post‑market sources. | Annex XIV Part A; must be kept current (Art. 61). |
| **4.7 Post‑Market Surveillance (PMS) plan & report** | PMS system (Art. 83), PMS plan (Art. 84), PSUR (Art. 86) for classes IIa‑III, PMS report (Art. 85) for class I. | PMS database, periodic safety update reports. |
| **4.8 Declaration of Conformity** | Completed DoC (Annex IV) with all mandatory fields filled. | This draft must be signed by an authorized person (see source excerpt [1]). |

> **Missing items:** The current DoC template lacks concrete data for every mandatory field; consequently, many sections above cannot yet be populated.

---

### 5. Risk Management & Controls (ISO 14971:2019)

| Required artifact | Content | Regulatory anchor |
|-------------------|---------|--------------------|
| **Risk Management Plan** | Scope, responsibilities, criteria for risk acceptability. | Annex I §3 (risk‑management system). |
| **Hazard identification & risk analysis** | List of all foreseeable hazards, severity & probability estimates. | ISO 14971:2019; Annex I §§4–8. |
| **Risk control measures** | Design safeguards, protective functions, user training, labeling, usability evaluation (IEC 62366‑1). | Annex I §5 (risk control) and §22 (lay‑person use). |
| **Residual risk evaluation & Benefit‑Risk determination** | Summarise remaining risks vs clinical benefits. | Annex I §8; CER conclusions (Art. 61). |
| **Post‑market feedback loop** | Integration of field data into RMF updates. | Art. 83–86 PMS system. |

> **Current status:** No RMF has been referenced in the source material – it must be created and linked to the DoC before submission.

---

### 6. Evidence Gaps & Immediate Action Items

| Gap | Why it matters | Suggested action (owner) |
|-----|----------------|--------------------------|
| **Intended use & mode of action** | Determines classification (Annex VIII) and clinical evidence scope. | Product Development – provide a concise “Intended Use” statement. |
| **Complete product identification (name, model, catalogue number)** | Required for traceability and DoC completeness (Annex IV). | Marketing/Regulatory – fill placeholders. |
| **EUDAMED SRN & Basic UDI‑DI** | Mandatory identifiers for market entry and DoC (Art. 19, Annex VI). | Regulatory – register in EUDAMED, allocate UDI. |
| **Authorized Representative details (if applicable)** | Legal requirement for non‑EU manufacturers (Annex IV). | Business Development – appoint AR or confirm “Not applicable”. |
| **Risk Management File** | Basis for GSPR compliance and residual risk evaluation. | Quality/Regulatory – develop RMF per ISO 14971. |
| **Clinical Evaluation Report (CER)** | Needed to satisfy Annex XIV Part A and Art. 61. | Clinical Affairs – initiate literature review & collect clinical data. |
| **Post‑Market Surveillance plan** | Required for all classes (Art. 84) and PSUR/PMS report (Art. 85/86). | Regulatory – draft PMS plan aligned with device class. |
| **Signatory authority verification** | DoC must be signed by a person with full authority (source [1] shows signature block). | Legal/Management – confirm signatory’s role and obtain signature. |

> **Note:** “no specific identifier found in source — verify separately” applies to all the above items because the excerpt provides only generic placeholders.

---

### 7. Human‑Escalation Triggers

| Situation | Escalation point | Rationale |
|-----------|------------------|----------|
| **Cannot determine classification** (missing intended use/technology description) | Immediate escalation to Product Management & Clinical Lead. | Classification drives the entire conformity route; postponement blocks NB engagement. |
| **DoC contains any empty mandatory field** after initial completion attempt | Escalate to Legal / Senior Management for sign‑off before submission. | Incomplete DoC is non‑compliant with Annex IV and Art. 19 – will be rejected by the Notified Body. |
| **Device appears to fall into Class IIb/III** (based on preliminary intended use) | Early notification of a Notified Body (within 3 months of design freeze). | High‑risk devices require NB assessment; early involvement reduces later gaps. |
| **Risk Management File shows unresolved high‑severity hazards** | Escalate to R&D engineering & Quality Assurance leads for mitigation. | Residual risks must be acceptable per Annex I §8 before DoC signing. |
| **EUDAMED SRN or Basic UDI‑DI still pending close to market launch date** | Escalate to Regulatory Project Manager and senior leadership. | Market entry cannot occur without these identifiers (Art. 19, Annex VI). |

---

### 8. Peer‑Review Prompt

> *Colleague, could you verify that the listed evidence gaps align with the latest MDR expectations for a Class IIa/IIb device? Please also challenge whether any additional annexes (e.g., Annex XII on clinical investigations) might become relevant once the intended use is clarified. Let me know if any jurisdiction‑specific nuances (e.g., transition period provisions) have been overlooked.*

---

*End of regulatory draft.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
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
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1085205256397640486`

> 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` ---

2. Chunk `1141859994065237405`

> ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ───────────────────────────────────────────── 1. MANUFACTURER Company name : [회사명] SRN : [EUDAMED SRN — 미취득 시 공백] Address : [등록 사업장 주소] Authorised Representative: [EU 대리인명 및 주소 — 역외 제조사 해당 시] 2. SOLE RESPONSIBILITY STATEMENT This EU Declaration of Conformity is issued under the sole responsibility of the manufacturer named above. 3. BASIC UDI-DI [Basic UDI-DI — Annex VI Part C 기준] 4. PRODUCT IDENTIFICATION Product name : [제품명] Trade name : [상품명] Model / Cat.# : [모델 번호 / 카탈로그 번호] Intended use : [의도된 사용 목적 — 간략 기재] Photograph : [첨부...

### kb-eval-20261116-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6460f695e88058d8", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `6460f695e88058d8`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md)
- Source hash: `d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexII_Technical_Documentation_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMS...
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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Pathway**

---

### 1. Scope of the Review  
The material supplied (excerpts [1] and [2]) only contains a generic mapping of **MDR Annex II** requirements to other jurisdictions and an overview table of the annex. No device‑specific information (intended purpose, indications, mode of action, patient population, or design attributes) is provided. Consequently the classification and the detailed submission route cannot be finalised at this stage. The draft below summarises what must be demonstrated, highlights the evidence that is presently missing, and sets out the logical steps to reach a definitive judgment.

---

### 2. Classification Approach (Art 52 MDR)

| Step | Requirement | Evidence Needed | Reference |
|------|--------------|-----------------|-----------|
| **2.1 Identify Intended Use & Indications** | Clear description of medical purpose, target patient group, and claimed benefits. | • Device Description (Annex II §1)  <br>• Labeling / IFU (Annex II §2) | Annex II §1‑2 |
| **2.2 Determine applicable Classification Rule(s)** | Apply the rule(s) from **Annex VIII** that match the device’s mode of action (e.g., Rule 9, 10, 11, 17 etc.). | • Technical description of energy exchange, software decision‑making, invasiveness, measuring/sterile functions. | Annex VIII – classification rules |
| **2.3 Assign MDR Class** | Result from 2.2 maps to Class I, Is/Im/Ir, IIa, IIb or III. | — | Art 52 (par. 3‑7) – class → route mapping |
| **2.4 Select Conformity‑Assessment Route** | According to the identified class, choose the appropriate Annex (IX alone, or X + XI). | • Evidence of QMS compliance (ISO 13485:2016)  <br>• Technical documentation ready for NB review (Annex II §6) | Art 52 + Annex IX / X / XI |

*Current status*: **Step 2.1 is missing** – the source does not contain any intended‑use statement. Therefore classification cannot be resolved; a provisional “Class pending” flag must be applied.

---

### 3. Required Evidence Package (per MDR Annex II)

| Annex II Section | Content Requirement | Documents / Artefacts to be provided |
|-------------------|---------------------|--------------------------------------|
| **§1 – Device Description** | Full description of the device, its variants, accessories and intended purpose. | • Design Output (DHF)  <br>• Intended‑use statement |
| **§2 – Labeling & IFU** | All labeling, packaging artwork and Instructions for Use in required language(s). | • Label mock‑ups <br>• IFU drafts (English + national language) |
| **§3 – Design & Manufacturing Information** | Detailed design drawings, manufacturing processes, critical process parameters. | • Design History File (DHF) sections §7.3 (QMSR)  <br>• Process Flow Diagrams |
| **§4 – GSPR Checklist** | Evidence that the device meets each of the 23 General Safety & Performance Requirements (Annex I). | • Completed GSPR matrix, cross‑referencing to test reports and risk controls |
| **§5 – Risk Management** | Full ISO 14971:2019 risk management file covering risk analysis, evaluation, control measures and residual risk. | • Risk Management Plan, Hazard Log, FMEA/FMECA, risk acceptability justification |
| **§6 – Verification & Validation** | Results of verification (design output vs. input) and validation (clinical/benchtop performance against intended use). | • V&V reports, test protocols, acceptance criteria, data tables |
| **Annex XIV Part A – Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data summary, benefit–risk analysis. | • CER dossier <br>• Device‑specific clinical data or equivalent literature |
| **Annex XIV Part B – PMCF Plan & Report** (if applicable) | Planned post‑market clinical follow‑up activities and periodic results. | • PMCF plan, interim reports |
| **Art 83/84 – PMS System & Plan** | Ongoing surveillance system to collect real‑world performance data. | • PMS SOPs, reporting procedures |
| **Art 85/86 – Periodic Safety Update Report (PSUR)** | For Class IIa–III devices, a PSUR summarising PMS findings and benefit‑risk updates (every 2 y for IIa/IIb; annually for III). | • Draft PSUR (when applicable) |
| **Art 19 – EU Declaration of Conformity** | Signed declaration with required content (manufacturer details, device identification, conformity route). | • DoC template completed |

*Missing evidence* (based on supplied excerpts): all items above are absent; only a generic mapping table is available.  

---

### 4. Risk Controls Expected (Annex I §3‑8)

| GSPR Clause | Typical Control(s) | Proof Needed |
|-------------|-------------------|---------------|
| **§3 – Risk Management System** | Implementation of ISO 14971:2019, documented RMF, periodic review. | • RMF file, audit logs |
| **§4 – Risk Controls** | Protective measures, safe‑use information, alarms, redundancy. | • Design controls, verification tests demonstrating effectiveness |
| **§5 – Use‑Error Mitigation** | Human factors/usability engineering (IEC 62366‑1:2020). | • Usability validation study report |
| **§6 – Device Lifetime** | Defined service life, maintenance schedule, end‑of‑life disposal. | • Reliability data, degradation studies |
| **§7 – Transport & Storage** | Packaging tests, temperature/humidity limits. | • Transport simulation test results |
| **§8 – Benefit–Risk Determination** | Residual risk analysis, clinical benefit evidence. | • CER conclusions, risk acceptability statements |

*Current status*: No risk management documentation is provided; the requirement is flagged as **missing**.

---

### 5. Human‑Escalation Triggers

| Trigger Condition | Action Required | Escalation Point |
|--------------------|-----------------|------------------|
| **No Intended‑Use Statement after 5 working days** | Request manufacturer to supply a definitive intended‑use description (including indications, patient group, mode of action). | RA Lead – Classification Blocker |
| **Unresolved Classification Rule(s) after 10 working days** | Convene classification working‑group with clinical & engineering SMEs to interpret applicable Annex VIII rule(s). | RA Manager – Decision Needed |
| **Incomplete Technical Documentation (any Annex II §1‑6 section missing)** | Issue a “Documentation Gap Notice” to the project team; set 7‑day remediation deadline. | Project Owner – Gap Closure Required |
| **Risk Management File Not Provided** | Suspend further NDA preparation until RMF is delivered and reviewed for completeness. | Quality Assurance – Stop‑Work Order |
| **Clinical Evidence Insufficient (no CER, no device‑specific data)** | Trigger engagement of Clinical Evaluation Expert; consider feasibility of a clinical investigation per Annex XV. | Clinical Lead – Investigation Planning |
| **NB Review Feedback indicating “non‑conformity to GSPR”** | Pause submission, address each non‑conformity, and re‑submit for NB assessment. | Regulatory Affairs Director – Oversight |

Any trigger that remains unresolved after the stipulated deadline must be escalated to the **Regulatory Affairs Steering Committee** for a go/no‑go decision.

---

### 6. Summary Judgment

*Given the current source material, the classification cannot be finalised because the device’s intended purpose and mode of action are not disclosed. Consequently, the appropriate conformity‑assessment route (Annex IX alone or Annex X + XI) remains indeterminate.*  

**Immediate next steps**

1. Obtain a complete **Device Description & Intended Use** from the manufacturer.  
2. Populate all sections of **MDR Annex II** (§1‑6) with corresponding artefacts.  
3. Conduct a **classification exercise** using Annex VIII rules once intended use is known.  
4. Assemble supporting **risk management, verification/validation, and clinical evaluation** evidence in line with the requirements listed above.  

---

### 7. Peer‑Review Prompt (for an RA colleague)

> *Please review the assumptions made above regarding the missing device‑specific data and the resulting “classification pending” status. Verify that all cited framework references (Annex II §§1‑6, Annex VIII rules, Art 52, Annex IX/X/XI) are correctly applied to our generic workflow. Identify any additional MDR annexes or Articles (e.g., Article 83‑86 PMS obligations) that may require earlier attention for this device class once the intended use is clarified. Also, check whether any jurisdiction‑specific nuances (e.g., Korean MFDS documentation requirements mentioned in the source table) could affect our evidence‑gathering plan.*  

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
- [ ] No hallucination
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

### kb-eval-20261116-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6096bdce42c7bee5", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `6096bdce42c7bee5`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수). ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료
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

> **Regulatory Draft – X‑ray Medical Device (MDR 2017/745)**  

---

### 1. Device Synopsis (as understood from the source)
* **Type:** Ionising‑radiation equipment (X‑ray system) for medical diagnosis / radiography.  
* **Core components likely involved:**   
  1. X‑ray tube/generator – emits ionising radiation.  
  2. Detector or image plate – records the emitted image.  
  3. Software that processes the image and may provide diagnostic information.  

*(The source does not supply a detailed intended‑use statement, component list or user group; these items are required for a complete classification justification.)*  

---

### 2. Classification & Conformity‑Assessment Route  

| Item | Regulatory basis | Determination |
|------|------------------|---------------|
| **Device class** | MDR Annex VIII – Rule 10 (radiology limb) → **Class IIb** for equipment that emits ionising radiation for diagnostic purposes.  <br> *Source [1] states “X‑ray 기기 … Class IIb 이상”.* | **Class IIb** |
| **Conformity‑assessment route** | MDR Art. 52(4) – for Class IIb the possible routes are: <br> • **Annex IX** (full QMS + technical‑documentation assessment by a NB)  <br> or <br> • **Annex X** (type‑examination) *combined with* **Annex XI** (production‑conformity verification). | Both routes are viable; selection will be made after NB discussion. |
| **NB involvement** | MDR Art. 52(4) – NB mandatory for Class IIb.  <br> *Source [1] confirms “NB 인증 필수”.* | Required |

---

### 3. Evidence Package Required for the Chosen Route  

| Documentation (MDR reference) | Content required | Remarks / Gaps |
|-------------------------------|------------------|----------------|
| **Technical Documentation** – Annex II §§1‑6 (incl. §6.1) | • Device description, intended use, variants, accessories <br>• Design & manufacturing information <br>• General Safety & Performance Requirements (GSPR) compliance evidence <br>• Risk Management File (ISO 14971:2019) <br>• Verification & validation data <br>• Clinical Evaluation Report (CER) – Annex XIV Part A | *Source [2] lists “Technical Documentation Assessment 보고서” – the TD itself is not provided.* |
| **EU Declaration of Conformity** – Art. 19 / Annex IV | Signed declaration referencing all applicable conformity‑assessment procedures. | Not present in source. |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A, kept current under Art. 61 | Systematic literature review, state‑of‑the‑art analysis, clinical data (e.g., investigations, post‑market surveillance). | No clinical data cited; must be generated. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – Annex XIV Part B | Planned PMCF activities, methodology, results, conclusions. | Absent. |
| **Post‑Market Surveillance (PMS) System** – Art. 83 & PMS Plan (Art. 84) | Ongoing collection and analysis of safety/performance data; PSUR for Class IIb (Art. 86). | No PMS documentation referenced. |
| **Risk Management File** – ISO 14971:2019, Annex I §3 | Hazard identification, risk evaluation, control measures, residual‑risk assessment, post‑market risk updates. | Not supplied. |
| **Usability Engineering / Human Factors** – IEC 62366‑1 (2020) | Usability verification to meet GSPR §5 & §22. | Not mentioned. |
| **Electrical Safety & Radiation Protection** – IEC 60601‑2‑54 (for radiography) & Annex I §16 (radiation protection). | Tests for electrical safety, electromagnetic compatibility, DQE (IEC 62220‑1‑1), radiation dose limits. | No test reports provided. |
| **Software Lifecycle Documentation** – IEC 62304 (2006+A1:2015) if software is a medical device component. | Architecture, hazard analysis, verification & validation, maintenance plan. | Not referenced. |
| **Labeling & IFU** – Annex I §23 | Labels, packaging, instructions for use, symbols, user manual. | No sample labeling supplied. |
| **Notified Body (NB) Contractual Documents** – Source [2] lists “심사 계약서·견적서”. | Signed contract/quotation confirming scope of assessment (Annex IX or X+XI). | Must be obtained from the selected NB. |

---

### 4. Identified Missing Information / Gaps  

| Gap | Why it matters | Recommended action |
|-----|----------------|--------------------|
| **Exact intended‑use statement & user profile** | Needed to justify classification rule and to draft CER/labeling. | Obtain from product development team; include in TD §1. |
| **Component breakdown (tube, detector, software) with individual specifications** | Each limb may fall under a different Rule (10 radiology vs 10 recording vs 11 software). Clear mapping required for correct classification justification. | Request detailed BOM and functional description. |
| **Clinical data (clinical investigation or existing literature)** | Mandatory for CER; absence blocks CE‑marking. | Conduct systematic literature review; plan/execute a clinical investigation if justified. |
| **Risk Management File (RMF) & risk analysis** | Required by Annex I §3 and ISO 14971. | Compile hazards, severity, probability, controls; include residual‑risk evaluation. |
| **Usability / Human‑factors assessment** | GSPR §§5 & 22 demand mitigation of use‑error risks. | Perform usability testing per IEC 62366‑1. |
| **Electrical safety and radiation protection test reports** | Must demonstrate compliance with IEC 60601‑2‑54 and Annex I §16. | Arrange test lab validation; collect certificates. |
| **Software development documentation (if applicable)** | Required by IEC 62304 & GSPR §17. | Gather software lifecycle artefacts. |
| **Labeling & IFU in required languages** | Needed for Annex I §23 and for the EU Declaration of Conformity. | Draft labeling, circulate for review. |
| **NB selection confirmation (scope code MDxxxx)** | Source uses placeholder “MDxxxx”. Exact NB scope code is mandatory for the conformity‑assessment request. | Verify the correct MDR designation in NANDO; confirm with chosen NB. |

---

### 5. Risk Controls to be Demonstrated  

1. **Radiation dose management** – Engineering controls, shielding, interlocks (Annex I §16).  
2. **Electrical safety & EMC** – IEC 60601‑2‑54 compliance (protect against electric shock, leakage currents).  
3. **Software safety** – Hazard classification, error handling per IEC 62304; verification that diagnostic output cannot cause inappropriate clinical decisions without clinician oversight (GSPR §17).  
4. **Usability safeguards** – Interface design to minimise user error; labeling of critical steps (GSPR §§5 & 22).  
5. **Residual risk acceptance** – Documented in RMF; justification that residual risks are outweighed by clinical benefits (GSPR §8).  

All controls must be traceable from risk analysis to verification/validation evidence and reflected in the Technical Documentation.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action required | Escalation level |
|---------|----------------|------------------|
| **Absence of a finalized intended‑use statement** (deadline > 2 weeks) | Pause classification justification; request senior product manager input. | RA Team Lead |
| **No clinical evidence identified after 4 weeks of literature search** | Initiate clinical investigation plan; involve Clinical Affairs lead and seek NB guidance on acceptable data scope. | Clinical Lead & RA Manager |
| **NB scope code not confirmed (placeholder MDxxxx still present)** | Immediate verification in NANDO; if mismatch, select alternative NB or re‑evaluate classification. | Regulatory Project Sponsor |
| **Risk Management File incomplete after 3 weeks of drafting** | Convene risk analysis workshop with R&D, QA, and safety experts to close gaps. | Head of Safety / Quality Manager |
| **PMS system not established before CE‑mark application** (required for Class IIb) | Halt submission; develop PMS plan per Art. 84 and assign responsible person. | RA Director |
| **Disagreement on classification route (Annex IX vs X+XI)** | Schedule decision meeting with senior RA, NB liaison, and legal counsel to select the most efficient path based on timeline & market strategy. | Senior Management |

---

### 7. Regulatory Judgment  

*Based on the information available, the X‑ray medical device must be classified as **Class IIb** under MDR Annex VIII Rule 10 (radiology limb). Consequently, a **Notified Body‑involved conformity assessment** is mandatory, either via **Annex IX** alone or **Annex X + XI**. The current documentation package is incomplete; the missing items listed above must be supplied before any NB audit can commence.*

---

### 8. Peer‑Review Prompt  

> **To a fellow EU RA colleague:**  
> Please review the classification justification (Rule 10 radiology limb) and the choice of conformity‑assessment routes for this X‑ray system. Are there any additional MDR provisions, IEC standards, or market‑specific considerations (e.g., specific radiation dose limits, national requirements) that have not been addressed? Verify whether the listed evidence gaps fully capture what a Notified Body will request for a Class IIb device, and flag any jurisdictional nuances you identify.  

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
- [ ] No hallucination
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

### kb-eval-20261116-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "adc8c31410f3ebef", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `adc8c31410f3ebef`
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

> **Regulatory Draft – 촬영실 GUI SW (2등급)**  

---

### 1. Korean Classification & Submission Route  
| Attribute | Determination |
|-----------|----------------|
| **Device grade** | 2등급 – confirmed by the excerpt that “촬영실 GUI SW (2등급)” is listed under MFDS guidance【2】. |
| **Regulatory pathway** | Primary route: **인증** (technical‑document review by an MFDS‑designated 심사기관). The same excerpt also notes the option to consider a parallel route under the *디지털의료제품법* if the functional scope meets that law’s definition【2】. |
| **Applicable MFDS instruments** | • 「의료기기 품목 및 품목별 등급에 관한 규정」 (품목·등급 지정) <br>• 「의료기기 허가·신고·심사 등에 관한 규정」 (인증 절차) <br>• 「의료기기 GMP 심사·평가 등에 관한 규정」 (KGMP 인증)  — all cited in the overview of the Korean medical‑device regulatory hierarchy【1】. |
| **No specific notice / article number** found in source – verify separately if a later MFDS 고시 (e.g., 최신 고시 번호) is required for this product category. |

---

### 2. Required Evidentiary Package  

| Category | Required Documents / Evidence | Legal/Standard Basis |
|----------|------------------------------|----------------------|
| **Technical Documentation** (MFDS 인증 심사) | • Device Description & Intended Use <br>• Classification justification (grade 2등급) <br>• IEC 62304‑based Software Life‑Cycle documentation (development, verification, validation, maintenance) <br>• IEC 60601‑1 safety reference if hardware is involved (not required for pure software) <br>• IEC 14971 위험관리 파일 (risk analysis, risk control measures) <br>• IEC 62366‑1 사용적합성(Usability Engineering) 보고서 <br>• Cybersecurity plan per MFDS 사이버보안 가이드라인 (IEC 81001‑5‑1 적용) | MFDS 고시 “의료기기 허가·신고·심사 등에 관한 규정” (technical‑document requirements); IEC 62304, IEC 14971, IEC 62366‑1, IEC 81001‑5‑1. |
| **KGMP Facility Certification** | • KGMP 적합성인증서 (의료기기법 제28조) <br>• 제조·품질관리 공정도 및 QMS 운영 증빙 | 「의료기기 GMP 심사·평가 등에 관한 규정」【1】. |
| **Labeling & IFU** | • Korean‑language 라벨 (제품명, 적용 대상, 사용 제한 등) <br>• 한국어 사용자 매뉴얼 (IFU) with safety warnings, contraindications, and maintenance instructions <br>• If the device contains AI: disclosure of AI function, limitation, and post‑market monitoring plan | MFDS 고시 “의료기기 품목 및 품목별 등급에 관한 규정” (라벨·사용설명서 요구) |
| **Clinical Evidence** *(if required)* | • Clinical Evaluation Report (CER) based on Korean‑relevant data or acceptable foreign clinical evaluation when MFDS has granted mutual acceptance (OECD MAD does NOT cover CER). <br>• For pure software without invasive risk, often a literature review & expert opinion suffice, but a formal CER is advisable. | MFDS 고시 “의료기기 허가·신고·심사 등에 관한 규정” – clinical data requirements for 2등급. |
| **AI‑Specific Evidence** (only when AI 기능 포함) | • Generative AI 가이드라인 적용 증빙 <br>• AI 모델 설명서, 데이터 관리 정책, 변동관리계획 (Change Management Plan) <br>• 위험도 평가에 AI‑특화 위험(예: 오판 위험) 추가 | “생성형 AI 가이드라인” referenced in excerpt【2】. |
| **Software Change Management** | • 변경관리계획서 (Change Management Plan) per IEC 62304 & MFDS 요구사항 <br>• 추적가능성 매트릭스 (Requirement ↔ Code ↔ Test) | IEC 62304, MFDS 고시 “의료기기 품목 및 품목별 등급에 관한 규정”. |
| **Post‑Market Surveillance (PMS)** | • 시판후조사 계획서 (PMS plan) including adverse event reporting, periodic safety update, and if AI: continuous performance monitoring. | MFDS 고시 “의료기기 GMP 심사·평가 등에 관한 규정” – PMS obligations for 인증 대상. |

---

### 3. Missing Information & Data Gaps  

| Gap | Impact on Submission | Action Required |
|-----|----------------------|-----------------|
| **Precise Intended Use Statement** (e.g., “real‑time image overlay in X‑ray room”) | Needed to justify 2등급 classification and risk analysis. | Obtain from product owner / marketing team. |
| **Detailed AI Function Description** (type of algorithm, training data, validation results) | Required for Generative AI 가이드라인 compliance; influences risk controls & PMS. | Request AI development dossier. |
| **Korean‑language labeling draft** | Non‑compliance leads to re‑submission. | Prepare provisional label & IFU in Korean; obtain translation verification. |
| **KGMP 인증 현황** (facility certification status) | Without KGMP, 인증 cannot proceed. | Verify current KGMP certificate or schedule audit. |
| **Clinical Evidence Scope** – whether local clinical data are mandatory for this software category | If required, missing CER will block approval. | Conduct a targeted clinical evaluation or map acceptable foreign data with MFDS liaison. |
| **Cybersecurity Risk Assessment** (threat model, mitigation) | Cybersecurity is explicitly cited in the excerpt; lacking documentation halts review. | Develop cybersecurity threat analysis per MFDS 사이버보안 가이드라인. |
| **Change Management Procedures** (process for future updates) | Required by IEC 62304 and MFDS for software. | Draft SOPs for version control & post‑market changes. |

---

### 4. Core Risk Controls to be Implemented  

1. **Risk Management System (IEC 14971)** – Identify hazards, evaluate risk levels, apply ALARP controls; include AI‑specific misuse scenarios.  
2. **Software Life‑Cycle Processes (IEC 62304)** – Structured development phases, verification/validation at each stage, configuration management.  
3. **Usability Engineering (IEC 62366‑1)** – Conduct formative and summative usability tests with target users (radiology technicians).  
4. **Cybersecurity Measures** – Secure coding practices, vulnerability scanning, encryption of data transmission, periodic security patches; align with MFDS 사이버보안 가이드라인.  
5. **AI Governance** – Model monitoring, bias assessment, explainability documentation as per Generative AI 가이드라인.  
6. **Post‑Market Surveillance Program** – Routine collection of field performance data, adverse event reporting workflow, and plan for AI performance drift detection.

---

### 5. Citations  

| Item | Source |
|------|--------|
| Regulatory hierarchy (법률 → 시행령 → 시행규칙) & MFDS 고시 list | 【1】 |
| Device grade 2등급, 인증 pathway, IEC 62304 lifecycle, 사이버보안, 사용적합성, AI 가이드라인 reference | 【2】 |
| No specific notice/article number for this product in the provided excerpts | — (verify separately) |

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason & Recommended Action |
|---------|------------------------------|
| **Unresolved missing data** (intended use, AI specifics, Korean label draft) | Pause submission preparation; assign to product development lead for immediate provision. |
| **KGMP certification not yet obtained** | Escalate to manufacturing/quality manager – schedule GMP audit before dossier finalization. |
| **Clinical evidence scope unclear** | Engage MFDS liaison or external consultant to confirm whether local clinical data are mandatory; if yes, initiate clinical evaluation project. |
| **Cybersecurity assessment incomplete** | Notify IT‑security officer; require completion of threat model prior to filing. |
| **Change Management SOPs absent** | Request Quality Assurance to draft SOPs; halt dossier until documented. |
| **AI component falls outside current MFDS AI guidance** | Elevate to regulatory strategy team for possible need for supplemental review under 디지털의료제품법 or a separate AI‑specific clearance. |

When any of the above triggers are hit, the RA lead should **escalate to senior RA manager** with a concise gap report and request resources / timeline extension before proceeding to MFDS 인증 submission.

---

### 7. Reusable RA Judgment (Lesson Learned)  

> *For software‑type medical devices classified as 2등급 in Korea, always start the certification plan by confirming the “인증” pathway, then assemble a technical file that includes IEC 62304 lifecycle documentation, IEC 14971 risk management, IEC 62366‑1 usability evidence, and MFDS‑specific cybersecurity & AI guidance where applicable. Verify KGMP facility certification early, prepare Korean‑language labeling before dossier finalization, and clarify the need for local clinical data (MFDS does not automatically accept foreign CER). Missing any of these elements should trigger an immediate escalation to senior RA management.*  

---

### 8. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions made about the necessity of a Korean clinical evaluation report for this software, the completeness of AI‑specific documentation under the Generative AI 가이드라인, and whether any additional MFDS 고시 (e.g., recent amendment to the “디지털의료제품법” related to software) might affect the chosen 인증 route. Identify any jurisdiction‑specific gaps or alternative evidence that could be leveraged.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 「의료기기 품목 및 품목별 등급에 관한 규정」에 라벨·사용설명서 요구와 SW 변경관리 요건을 오배치(동 고시는 품목·등급 지정 관할 — 오귀속 2건). 미세: 'IEC 14971' 표기 3회(정확히는 ISO 14971; 내용 매핑은 정확).

**Source Excerpts**

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `39359892234270838`

> ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재검증 — 핵심 규제사실 반영 확인. · 상태: 승인 · 일자: 2026-06-09

### kb-eval-20261116-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "607966dfa2c5cf3a", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `607966dfa2c5cf3a`
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

> **Regulatory Draft – P3 촬영실 GUI Software (Digital Medical‑Device Software)**  

---

### 1. Korean Regulatory Classification & Submission Route  

| Item | Determination | Rationale / Source |
|------|---------------|--------------------|
| **Product type** | Digital medical‑device software (디지털의료기기소프트웨어) | Stated in excerpt [2] (“P3 촬영실 GUI SW(디지털의료기기소프트웨어에 해당하는 경우)”). |
| **Grade (등급)** | **Uncertain – likely 2등급** but must be confirmed. | Excerpt [2] notes “GUI SW가 2등급이든 등급 미지정이든 …”. Korean grade is defined in 「의료기기 품목 및 품목별 등급에 관한 규정」; no explicit grade appears in the source – **no specific identifier found in source — verify separately**. |
| **Submission track** | **인증 (Technical‑documentation review by MFDS‑designated 심사기관)** if confirmed as 2등급. | Korean rule: 2등급 → 인증 (MFDS_인허가_상세가이드.md §2). |
| **Possible exemption / alternative pathway** | May qualify for “면제·대체 경로” under the revised 제25조 of the Digital‑Medical‑Device Act implementation rules. | Excerpt [2] – “GUI SW… 기능별 임상시험 자료의 면제·대체 경로가 열린다 … 개정 제25조 각 호”. **No specific identifier found in source — verify separately** (need exact clause numbers). |

---

### 2. Evidence Package Required for Certification  

| Evidence | Requirement | Reference / Comment |
|----------|-------------|----------------------|
| **Device Description & Intended Use** | Detailed description, software architecture, intended clinical function, AI‑assist scope (if later added). | Korean labeling law requires full Korean IFU; see MFDS guidance on digital medical devices. |
| **Risk Management File** | ISO 14971:2019–based risk analysis, hazard identification, mitigation measures, residual risk evaluation. Must address AI‑related risks if AI module is planned. | Framework reference – ISO 14971 (2019). |
| **Software Development Lifecycle Documentation** | IEC 62304:2006+A1:2015 compliance (software safety class determination, verification/validation activities). | Framework reference – IEC 62304 (2006+A1:2015). |
| **Clinical Evaluation / Performance Evidence** | • If exemption applies: proof that the device meets the criteria of 제25조 (각 호) – e.g., low‑risk category, existence of comparable foreign CE/FDA clearance, or prior clinical data. <br>• If no exemption: comparative clinical trial design per the 2025‑10‑31 AI 임상시험 가이드라인 (9종 개정). | • Guideline revision date cited in excerpt [1] (“2025‑10‑31”). <br>• Need exact clause of 제25조 – **no specific identifier found in source — verify separately**. |
| **Labeling & IFU** | Korean language labeling, safety symbols, user manual in Korean, and any required warnings for AI assistance. | MFDS 고시 on labeling (standard requirement). |
| **Quality Management System** | KGMP certification + ISO 13485:2016‑based QMS; maturity may be leveraged as a “우수관리체계 특례” benefit (excerpt [2]). | Framework reference – ISO 13485 (2016). |
| **Cybersecurity** | Compliance with MFDS 사이버보안 가이드라인 referencing IEC 81001‑5‑1:2021. | Framework reference – IEC 81001‑5‑1 (2021). |
| **Post‑Market Surveillance Plan** | Korean 시판후조사 (post‑market investigation) plan, including adverse event reporting and periodic safety update. | MFDS 고시 on PMS. |

---

### 3. Missing / Unverified Information  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Exact grade (1~4등급)** | Determines the submission pathway (신고/인증/허가). | Verify in 「의료기기 품목 및 품목별 등급에 관한 규정」 – obtain official classification code. |
| **Specific clause numbers of 제25조 (면제·대체 경로)** | Needed to prove eligibility for clinical‑data exemption. | Retrieve the latest version of “디지털의료제품법 시행규칙” (2026‑01‑23 amendment) and locate 제25조 각 호. |
| **Intended use statement & AI module roadmap** | Influences risk class, need for AI‑specific validation, and comparative trial design per 2025 guideline. | Draft precise intended-use description; decide whether AI will be a future add‑on or current function. |
| **Foreign clearance (e.g., FDA 510(k) / CE) if used to support exemption** | May satisfy criteria under 제25조 (예: 해외 인증 보유 시 면제). | Compile any existing foreign clearances; if none, plan for Korean clinical data. |
| **Korean labeling draft** | Mandatory for certification; errors cause re‑submission. | Prepare preliminary IFU in Korean and have it reviewed by a native‐language specialist. |
| **Exact MFDS 고시 / 시행규칙 identifiers** (e.g., “디지털의료제품법 시행규칙 제25조”) | Required for citation in the submission dossier. | Extract exact article/section numbers from the official Gazette; note that the source excerpts only give amendment dates, not identifiers – **no specific identifier found in source — verify separately**. |

---

### 4. Core Risk Controls (to be reflected in the risk‑management file)

| Hazard | Control Measure | Reference |
|--------|----------------|-----------|
| Misinterpretation of AI assistance leading to diagnostic error | Clear UI cues that AI output is advisory only; mandatory clinician confirmation before action. | IEC 62304, ISO 14971 |
| Software malfunction (crash / data loss) | Robust exception handling, automated backups, fail‑safe mode. | IEC 82304 (if applicable), MFDS cybersecurity guidance |
| Cybersecurity breach exposing patient data | Encryption of data at rest & in transit; regular vulnerability assessments per IEC 81001‑5‑1. | IEC 81001‑5‑1 |
| Inadequate user training resulting in misuse | Korean language training manual, on‑site training sessions, competency assessment. | MFDS 교육·훈련 가이드라인 |
| Compatibility with X‑ray hardware (P1/P2) leading to unsafe exposure | Interface validation; IEC 60601‑1 compliance for electrical safety if direct connection occurs. | IEC 60601‑1 |

---

### 5. Human‑Escalation Triggers  

| Situation | Reason for escalation | Who should be consulted |
|-----------|-----------------------|--------------------------|
| **Uncertainty about the device grade (1~4등급)** | Incorrect classification leads to wrong submission route and possible regulatory rejection. | Senior RA manager / legal counsel; reference 《의료기기 품목 및 품목별 등급에 관한 규정》. |
| **Clarification of exemption eligibility under 제25조** | Missing clause numbers prevent definitive claim for clinical‑data waiver. | Lead RA specialist on Digital Medical Device Act; obtain the latest 시행규칙 (2026‑01‑23). |
| **Planned AI functionality not yet defined** | AI introduces new risk profile and may invoke the 2025 임상시험 가이드라인 comparative design requirement. | Clinical research lead & biostatistician; determine need for a comparative clinical study. |
| **Absence of foreign clearance that could support exemption** | If no CE/FDA clearance, must generate Korean clinical data – budget and timeline impact. | Project manager & regulatory strategy lead. |
| **Korean labeling draft not completed or not reviewed by native speaker** | Non‑compliant labeling results in re‑submission and possible delay. | Medical writer (Korean) + compliance officer. |
| **QMS maturity insufficient to claim “우수관리체계 특례” benefit** | Incorrect claim may be rejected during 인증 review. | Quality assurance manager; verify KGMP/ISO 13485 certification status. |

---

### 6. Summary Judgment  

*The P3 촬영실 GUI software is a digital medical‑device software whose grade must be confirmed (likely 2등급). If classified as 2등급, the submission route is **인증** through an MFDS‑designated 심사기관. The device may qualify for a clinical‑data exemption under the revised 제25조 of the Digital Medical‑Device Act implementation rules; however, the exact clause numbers and conditions must be verified in the latest 시행규칙 (2026‑01‑23 amendment).*  

*If exemption is not applicable, a comparative clinical study complying with the 2025‑10‑31 AI 임상시험 가이드라인 (9종 개정) will be required. The evidence package must include risk‑management documentation (ISO 14971), software development lifecycle records (IEC 62304), KGMP/ISO 13485 QMS proof, Korean labeling, cybersecurity controls (IEC 81001‑5‑1), and a post‑market surveillance plan.*

*All identified gaps—grade confirmation, exact 제25조 clauses, intended‑use definition, foreign clearances, and Korean labeling—should be resolved before dossier assembly. Any unresolved item triggers the escalation actions listed above.*

---

#### Peer Review Prompt  

> **To a fellow RA colleague:** Please examine the assumptions made regarding (1) the likely 2등급 classification, (2) applicability of the 제25조 면제·대체 pathway without concrete clause citations, and (3) the sufficiency of the evidence list given current MFDS digital‑health guidance. Identify any jurisdiction‑specific gaps or alternative interpretations not covered here, especially concerning AI‑related clinical trial design requirements introduced in the 2025 guideline amendment.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> shadow 8차 하향 수용: 제25조 면제 요건 예시('저위험·해외 CE/FDA 인증·기존 임상데이터') — 원문은 면제 경로 존재만 서술하고 요건은 [검증 필요] 처리. 검증 안 된 요건을 예시로 제시 = 창작(경계선이나 정확성 우선 원칙상 수용).

**Source Excerpts**

1. Chunk `1127968925422991528`

> ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향후 AI 모듈 추가 가능성 고려해 비교설계 원칙 사전 학습 권고. - 출처: 정책브리핑 2025-10-31(https://www.korea.kr/briefing/pressReleaseView.do?newsId=156724315) ---

2. Chunk `198902914416608487`

> - 영향 제품: **P3 촬영실 GUI SW**(디지털의료기기소프트웨어에 해당하는 경우). P1 X-ray Detector·P2 Handheld X-ray Source는 의료기기법 체계 적용으로 **직접 영향 없음**(§3·§4 매트릭스 유지). - 나항은 자사에 **유리한 완화**다. GUI SW가 2등급이든 등급 미지정이든 기능별 임상시험 자료의 **면제·대체 경로가 열린다**. 다만 면제·대체의 개별 요건(개정 제25조 각 호)은 조문 전문 확인이 필요하다 — `[검증 필요]`. - 가항은 요건의 삭제가 아니라 **근거 조문의 이동(고시 → 시행규칙)** 이다. 「디지털의료제품법 시행규칙」(2026-01-23 개정)의 해당 조문을 확인해야 실제 의무 범위를 알 수 있다 — `[검증 필요]`. - 다항의 우수관리체계 특례는 **QMS 성숙도를 인허가 편익으로 전환**하는 제도다. KGMP·ISO 13485 기반이 갖춰진 경우 중장기 활용 가치가 있다. **행동 (Action)**

### kb-eval-20261116-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "305b935cc0a22d84", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `305b935cc0a22d84`
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

> **Regulatory Draft – MFDS Classification & Licensing Pathway**

---

### 1. Device Overview (as inferred from the source)

| Item | Status / Comment |
|------|-------------------|
| **Product type** | Medical‑software–enabled system (detector + source, SW may be standalone) |
| **Intended use** | Diagnostic imaging (detector = IIa / IIb under EU MDR Rule 10; source = IIb) – “특정 부위·용도·SW 역할” to be defined |
| **Key specifications needed** | 정격관전압, 관전류, 적용부위, SW 기능 등 (see Chunk 1 – “각 제품의 상세 사양 확보”) |
| **MFDS 품목코드 (A‑code)** | Not yet assigned (Chunk 1) |

---

### 2. MFDS Classification & Submission Route  

| Criterion (source) | Determination |
|--------------------|---------------|
| **Domestic classification** – “2등급” stated in Chunk 2, backed by *“의료용 소프트웨어 허가·심사 가이드라인」* and the new *「디지털의료제품법」* (effective 2025‑01‑24) | **2등급** |
| **Regulatory pathway for 2등급** – per MFDS 인허가 상세가이드, §2 (등급 및 인허가 경로) | **인증** via MFDS‑designated 심사기관 (e.g., KTL, KTC, KTR) |
| **Potential upward shift** – “보조 기능 수준에 따라 상향 가능” noted in Chunk 2 | Must verify that ancillary functions do not raise the grade to 3등급·4등급; if they do, pathway switches to **허가** |

> **Citation** – Classification “2등급” and its basis are taken from source excerpt [2]. No specific notice number is provided in the excerpt; verification of the exact guideline reference (e.g., 고시 번호) should be performed separately.

---

### 3. Required Evidence Package (MFDS 인증)

| Evidence | Reference / Rationale |
|----------|-----------------------|
| **Technical Documentation** – device description, specifications, intended use, labeling, IFU (Korean language) | Requirement in MFDS 인증 guidelines; aligns with ISO 13485:2016 QMS documentation. |
| **Risk Management File** – risk analysis, mitigation, residual risk evaluation per **ISO 14971:2019** | Mandatory for all medical devices; cited as the current edition in the reference table. |
| **Software Documentation** – architecture, algorithm description, version control, validation plans (including AI/ML if applicable) | Required by *“디지털의료기기소프트웨어 허가·심사 가이드라인」* (source [2]). |
| **Cybersecurity Assessment** – conformity to MFDS 사이버보안 가이드라인 (references IEC 81001‑5‑1:2021) | Applicable for any device with networked software. |
| **Usability Validation** – per **IEC 62366‑1:2015+A1:2020** | Required for user‑interface safety. |
| **Clinical Evaluation Report (CER)** – if foreign clinical data are used, must demonstrate relevance to Korean population and meet MFDS acceptance criteria (separate from OECD MAD which only covers non‑clinical GLP data). | MFDS now accepts foreign CERs under certain conditions; no specific notice number is given in the excerpts. |
| **KGMP Facility Certification** – proof of compliance with Korean GMP for medical devices (법 제28조) | Mandatory for manufacturing sites before 인증 can be granted. |
| **Change‑Management Plan** – especially required by the *2025 디지털의료제품법* for AI/ML updates | Referenced in Chunk 2 (“변경관리계획”). |
| **A‑code Assignment Confirmation** – official MFDS 품목코드 | Must be obtained prior to submission. |

---

### 4. Missing Information & Gap Analysis  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Complete product specification** (전압·전류·용도·SW 역할) – not yet defined | Determines classification, labeling, and safety testing scope | Capture detailed specs from engineering; update the “제품 전략·사양 확정” checklist (Chunk 1). |
| **Predicate device identification** – FDA Product Classification Database lookup mentioned but results absent | Used for foreign clinical/evidence justification if pursuing an 510(k)‑type reference (although not a direct MFDS pathway, it may support CER) | Perform predicate search; document the US device number and similarity rationale. |
| **EU MDR Rule 10/11 outcome** – only noted as “적용 최종 판단” but decision missing | Affects whether components are considered separate devices or accessories, which impacts classification in Korea | Confirm final EU MDR rule application; reflect in Korean submission. |
| **Notified Body selection** – indicated for EU strategy, not required for MFDS 인증, but could be relevant if the device will also be marketed in EU | May affect parallel submission timelines | Decide whether EU market entry is pursued; select NB accordingly. |
| **AI/ML algorithm validation plan** – required under the 2025 디지털의료제품법, not detailed | Lack of AI‑specific risk analysis can lead to re‑classification or additional data requests | Develop a pre‑market evaluation plan for AI components (data set description, performance metrics, post‑market monitoring). |
| **Korean language labeling & IFU** – no drafts supplied | MFDS mandates Korean labeling for all devices; non‑compliance blocks certification | Prepare Korean label/IFU per MFDS 라벨링 가이드라인. |
| **KGMP certification status** – not mentioned | Manufacturing site must hold KGMP before 인증 issuance | Verify facility compliance; obtain KGMP certificate. |

---

### 5. Core Risk Controls (to be reflected in the dossier)

1. **Risk Management Process** – ISO 14971‑based hazard identification, risk estimation, mitigation, verification of controls.
2. **Cybersecurity Measures** – network isolation, firmware integrity checks, encryption; compliance with IEC 81001‑5‑1 and MFDS 사이버보안 가이드라인.
3. **Usability Engineering** – user tasks analysis, formative/summative testing to prevent use errors.
4. **Software Lifecycle Controls** – version control, configuration management, traceability matrix (requirements ↔ design ↔ test).
5. **Post‑Market Surveillance Plan** – 시판후조사 framework (periodic safety updates, adverse event reporting, field safety corrective actions).

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger for escalation to senior RA / regulatory affairs lead |
|-----------|--------------------------------------------------------------|
| **Uncertainty on final grade** – evidence suggests potential upgrade to 3등급·4등급 (e.g., additional therapeutic claim) | Immediate review; may shift pathway from 인증 to 허가. |
| **A‑code not yet assigned** after the pre‑submission meeting deadline | Escalate to project manager for expedited MFDS communication. |
| **Missing KGMP certification** or pending facility audit results | Halt submission until certificate obtained; notify quality assurance. |
| **AI/ML validation plan incomplete** under 디지털의료제품법 requirements | Pause filing; require AI risk assessment and change‑management documentation. |
| **Foreign clinical evidence rejected** because it does not meet MFDS CER criteria (e.g., lack of Korean population data) | Seek local clinical study or additional bridge data before proceeding. |
| **Labeling/IFU translation issues** identified during internal review | Engage native‑language specialist; delay submission until compliance confirmed. |
| **Regulatory notice number for the new digital medical device law not verified** (no specific 고시 번호 in source) | Assign a regulatory affairs analyst to locate the exact 고시 / 시행령 number before final dossier compilation. |

---

### 7. Peer‑Review Prompt  

> *"Colleague, could you examine whether my assumptions about the classification remaining at **2등급** are robust given the possibility of ancillary functions elevating the grade? Please also verify that all required Korean‐specific evidence (KGMP certification, Korean labeling, AI change‑management plan) is fully captured, and check if any additional MFDS 고시 번호 should be referenced for the 2025 디지털의료제품법 implementation."*

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
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. 2등급→인증 source-grounded, 상향 가능성 헷징. 미세 관찰: Device Overview 'detector = IIa / IIb' 병기 모호(source는 Detector=IIa 영상기록).

**Source Excerpts**

1. Chunk `1097646391221557778`

> ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정

2. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

### kb-eval-20261116-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "373a9d1424c0b04b", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `373a9d1424c0b04b`
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

> **Regulatory Draft – MFDS Classification & Submission Route  
(Prepared for a digital‑health medical device – SaMD)**  

---

### 1. Determination of Korean Grade (1~4등급) and Applicable Pathway  
| Step | What to verify | Why it matters | Sources |
|------|----------------|----------------|---------|
| **Intended use & risk profile** | Identify the clinical indication, invasiveness, duration of contact, and whether the device performs a diagnostic or therapeutic function. | The MFDS grading matrix (‑ “의료기기 품목 및 품목별 등급에 관한 규정”) assigns 1~4등급 based on these factors. | Framework reference – MFDS grade matrix (no specific identifier in source). |
| **Digital‑medical‑product law** | Confirm whether the device is covered by the *디지털의료제품법* that came into effect 2025‑01‑24. | SaMD are now classified and approved under this law; the law also expands NIDS authority for GMP assessment of digital devices. | Excerpt [2] – “디지털의료제품법 시행 … SaMD 분류·허가 체계 변화, NIDS 권한 확대”. |
| **AI/ML‑based GUI software** | If the device contains AI/ML algorithms or a GUI that influences clinical decisions, check the MFDS digital‑medical‑device guideline (issued 2025‑05‑07) for classification and clinical evidence requirements. | The 2025 guideline adds specific clinical‑evaluation obligations for AI/ML SaMD. | Excerpt [2] – “AI/ML 기반 GUI SW 분류·임상 요건 확인 필요”. |
| **Grade outcome** | - **1등급 → 신고** (notification) <br> - **2등급 → 인증** (technical‑document review by an MFDS‑designated 심사기관) <br> - **3등급·4등급 → 허가** (full MFDS approval) | The submission track follows the Korean grade; note that 2등급 does *not* go through “허가”. | Framework reference – MFDS_인허가_상세가이드.md §2. |
| **Human‑escalation trigger #1** | If the intended use or risk analysis cannot be matched to a definitive grade, halt drafting and request clarification from product development. |

---

### 2. Required Evidence Package (per the identified pathway)

| Evidence Type | Requirement Detail | Applicable Grade/Pathway | Source |
|---------------|-------------------|--------------------------|--------|
| **KGMP 적합인정** | • GMP 심사 신청 → 현장조사 → 결함 통보 → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요). <br>• For digital devices the review agency may be one of 6 listed entities **including NIDS** (effective 2025‑01‑24). | Mandatory for all grades that require 인증 or 허가; also required for 신고 when MFDS explicitly requests KGMP evidence. | Excerpt [1] – full GMP 절차 and list of 심사기관, with note on NIDS. |
| **Technical Documentation** (Korean “기술문서”) | • Device description, intended use, risk management file (ISO 14971:2019), design verification & validation, labeling, IFU in Korean language, software lifecycle documentation (IEC 62304:2006+A1:2015). <br>• For AI/ML SaMD, include algorithm change‑control plan and performance monitoring strategy per MFDS 2025 guideline. | Required for 인증 and 허가; also attached to 신고 when requested. | Framework references – ISO 14971 (2019), IEC 62304 (2006+A1:2015). |
| **Clinical Evaluation Report (CER)** | • Non‑clinical data (GLP toxicology) can be accepted under OECD “mutual acceptance of data” only for GLP safety studies. <br>• For clinical evidence, either Korean post‑market surveillance data or a foreign CER that MFDS has explicitly accepted (separate from OECD MAD). | Required for 3등급·4등급 허가; may be waived for low‑risk 2등급 if MFDS determines no local data needed. | Note – distinction between OECD MAD (non‑clinical) and foreign CER acceptance is mandated by MFDS policy (no specific notice number in source). |
| **Labeling & IFU** | • All labeling, package inserts, and user manuals must be provided in Korean language; supplemental English version permissible. | Mandatory for every submission pathway. | Framework reference – MFDS labeling requirements (standard practice). |
| **Software Validation** | • IEC 62304 compliance, plus risk‑based verification/validation plan per ISO 14971. <br>• For AI/ML: traceability matrix linking data sets, model versioning, and performance metrics. | Required for any SaMD regardless of grade when software is a principal component. | Framework references – IEC 62304 (2006+A1:2015), ISO 14971 (2019). |
| **Human‑escalation trigger #2** | If any of the above evidence cannot be produced (e.g., no Korean CER, missing KGMP certificate, or unavailable NIDS review agency capacity), flag for senior RA review and possible alternate pathway (e.g., seeking exemption). |

---

### 3. Risk Controls & Post‑Market Surveillance (시판후조사)  

| Control | Detail | Applicability |
|---------|--------|----------------|
| **Risk Management File** | Complete ISO 14971:2019 risk analysis, evaluation of residual risk, and implementation of mitigations. | All grades. |
| **Cybersecurity** | Follow MFDS 사이버보안 가이드라인 (references IEC 81001‑5‑1 2021) for SaMD with network connectivity. | Required for digital/AI devices. |
| **Post‑Market Surveillance Plan** | • Define PMS activities (clinical follow‑up, complaint handling, trend analysis). <br>• For 3등급·4등급 허가, submit a detailed 시판후조사 계획 to MFDS. | Mandatory for 인증 and 허가; optional but recommended for 신고. |
| **Change Management** | Upcoming “네거티브 방식 변경허가제” (2026 예정) – major changes need prior approval, minor changes post‑notification. Prepare a change‑impact assessment framework now. | All grades; especially important for AI/ML models that are updated frequently. |
| **Human‑escalation trigger #3** | If risk control documentation is incomplete or PMS plan does not meet MFDS expectations (e.g., lacking cybersecurity measures), suspend submission and involve the quality‑assurance lead. |

---

### 4. Missing Information – Gaps to Resolve Before Submission  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended use & risk classification** | Determines Korean grade and whether AI/ML guideline applies. | Obtain a clear indication statement from product management; perform MFDS grading matrix analysis. |
| **KGMP certification status of manufacturing site** | GMP 적합인정 is prerequisite for 인증/허가. | Request KGMP audit report or schedule NIDS/KTL review if not yet performed. |
| **Korean‑language labeling & IFU drafts** | Mandatory for all pathways; late discovery leads to resubmission. | Draft Korean labeling now; run translation verification. |
| **Clinical evidence strategy (local vs. foreign CER)** | Determines need for local trial data; affects timeline. | Decide whether a foreign CER can be used (confirm MFDS acceptance) or plan a Korean clinical study. |
| **Algorithm change‑control documentation** (if AI/ML) | Required by 2025 MFDS guideline for GUI‑based SaMD. | Create version‑control and performance‑monitoring documents. |
| **Exact regulatory instrument numbers** | Some MFDS notices/guidelines referenced in internal SOPs may have specific numbers that need citation. | Verify the official notice number (e.g., 고시 제xxxx‑xx호) from MFDS website; currently “no specific identifier found in source — verify separately”. |

---

### 5. Human‑Escalation Triggers Summary  

| Trigger | Condition | Recommended Escalation |
|----------|-----------|------------------------|
| **Uncertain grade** | Intended use/risk matrix yields ambiguous 2등급 vs. 3등급 result. | Pause dossier; involve senior RA and possibly a regulatory consultant with MFDS experience. |
| **Missing KGMP certificate** | No GMP 적합인정 or agency (KTL/KTR/NIDS) assignment confirmed. | Alert manufacturing QA leader; schedule KGMP audit within 2 months. |
| **Insufficient clinical data** | No CER that satisfies MFDS for the identified grade. | Escalate to Clinical Development lead – decide on local study vs. foreign data justification. |
| **AI/ML algorithm update plan absent** | Device includes adaptive AI but lacks change‑control documentation. | Raise with software engineering; draft a post‑market performance monitoring plan before submission. |
| **Regulatory instrument number missing** | Any citation of MFDS 고시, notice, or guideline required for compliance statements cannot be located. | Request legal/regulatory affairs to retrieve the official document and confirm its identifier. |

---

### 6. Peer‑Review Prompt  

> *Please review this draft and challenge: (a) the completeness of the evidence list given a SaMD with AI/ML components, (b) whether the source excerpts adequately cover all required Korean regulatory citations, and (c) any jurisdiction‑specific gaps (e.g., language‑only labeling, change‑management under the upcoming “네거티브 방식 변경허가제”).*  

---

**End of Draft.**

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 'SaMD are now classified and approved under this law(디지털의료제품법)' — 분류·허가 관할 과잉 단정(등급은 의료기기법 소관, 디지털의료제품법은 병용 검토 경로 — 11-10 kr 계열 2회차 재발, 루브릭 §7 트리거 후보). 등급 근거 자체는 올바르게 표기.

**Source Excerpts**

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---

### kb-eval-20261116-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-16", "decision_ref": "kb-eval-20261116-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "78e52e8fbea544f7", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `78e52e8fbea544f7`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f`
- Focus: MFDS classification and licensing route
- Matched keywords: KGMP

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관...
- 이 항목의 평가 포인트: 이 source는 classification route를 직접 확정하는 문서가 아닐 수 있습니다. 좋은 답변은 class/rule을 단정하기보다 route 판단에 필요한 evidence와 확인 대상을 제시해야 합니다.
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

> **Regulatory Draft – SaMD “촬영실 GUI SW” (Standalone Imaging‑room Software)**  

---

### 1. Korean Classification & Submission Route  
| Item | Finding / Requirement |
|------|------------------------|
| **Korean grade** | Must be determined from the MFDS “의료기기 품목 및 품목별 등급에 관한 규정”. For a standalone imaging‑room GUI that performs image acquisition/processing, the default is **3등급·4등급** (high‑risk software) unless the intended use is limited to non‑diagnostic display. <br>*Action*: request the exact wording of the intended use and risk claim → confirm grade with MFDS or by consulting the classification table. |
| **Submission pathway** | If classified as **3등급·4등급**, the device follows the **허가 (approval) route** – full MFDS review of technical documentation, clinical evaluation, and KGMP compliance. <br>If later re‑classified as 2등급, the route would switch to **인증** via an MFDS‑designated 심사기관. |
| **Citation** | No specific identifier for the classification rule appears in the source – *verify separately* against 「의료기기 품목 및 품목별 등급에 관한 규정」 (§ 2 of MFDS_인허가_상세가이드.md). |

---

### 2. Required Evidence Package  

| Evidence | Korean Requirement | Mapping to International Standard / Guidance (framework reference) |
|----------|-------------------|-------------------------------------------|
| **KGMP facility certification** | Mandatory for all 3등급·4등급 devices; MFDS 고시 제2025‑22호 (referenced in KGMP‑QMSR comparison). | KGMP (MFDS) – aligns with ISO 13485:2016 (see Table 1 of source). |
| **Software Development Lifecycle documentation** | Full SDP, SRS, SAD, SVP, SVR required; must demonstrate compliance with IEC 62304 Safety Class C. | IEC 62304 §8.1 – *SW 개발 수명주기* (source [2]). |
| **Risk Management File** | ISO 14971:2019 risk analysis, evaluation, control & post‑market monitoring; Korean labeling of risk controls required. | ISO 14971 (framework). |
| **Cybersecurity Dossier** | Threat model, Software Bill of Materials (SBOM), and PCCP (Pre‑Market Cybersecurity Plan) per MFDS 사이버보안 가이드라인 2025. | MFDS 사이버보안 가이드라인 2025 (source [2]). |
| **Clinical Evaluation Report (CER)** | Required for 3등급·4등급 SaMD; local clinical data may be needed unless a recognized foreign CER can be accepted under the latest MFDS notice expanding mutual acceptance of foreign CERs. | Not directly cited – *verify separately* whether a specific MFDS 고시 permits use of FDA/EU CERs for this indication. |
> **Note:** The source excerpt on ARR (Applicable Regulatory Requirements) describes UDI, MDR‑type reporting and Corrections & Removals obligations that must also be reflected in the QMS procedures (source [1] – §820.10(b), §820.35(a)). While these are FDA citations, MFDS expects equivalent Korean‑language compliance (e.g., UDI‑KOR format, 신고/허가 reporting).  

---

### 3. Missing Information & Gaps  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Exact intended use / claim** | Determines grade and the need for clinical data. | Obtain a signed product specification from the development team. |
| **Korean labeling & IFU drafts** | Korean language required for all labeling, patient‑facing documents and Instructions for Use. | Draft Korean labeling early; flag to translation team. |
| **UDI implementation plan** | MFDS requires UDI in Korean (K‑code) for 3등급·4등급 devices. | Define UDI strategy – GS1 or K‑code, include in technical file. |
| **Local clinical data requirement** | If foreign CER is not accepted, local pilot study needed. | Check latest MFDS notice on acceptance of foreign CERs; plan accordingly. |
| **Post‑market surveillance (PMS) plan** | Korean “시판후조사” must include adverse event reporting, trend analysis, and field safety corrective actions. | Develop PMS SOP in line with MFDS 고시 § 23‑45 (exact number not in source – verify). |
| **AI/ML algorithm description (if applicable)** | AI‑based SaMD may trigger additional regulatory obligations under the Digital Medical Device Act and MFDS AI guidance. | Confirm whether AI/ML is present; if yes, prepare algorithm change management & validation documentation. |

---

### 4. Key Risk Controls (to be reflected in the QMS)  

1. **Software safety class C controls** – per IEC 62304: redundant error handling, safe‑state functions, and failure mode mitigation.  
2. **Cybersecurity:** Threat modelling, SBOM tracking, PCCP submission; periodic vulnerability scanning as required by MFDS 사이버보안 가이드라인 2025.  
3. **Change Management:** Regression test automation (source [2] – “Regression Test 자동화, 변경 관리 SOP”).  
4. **Complaint handling & MDR‑type reporting** – align complaint intake with §820.35(a) requirements; Korean equivalent must log reportability assessment.  
5. **Contract sterilizer / re‑labeler inclusion** – if the software is distributed via third parties, extend QMS scope per §820.10(a) (source [1]).

---

### 5. Human‑Escalation Triggers  

| Trigger | Escalation Level |
|---------|-------------------|
| **Uncertain grade** after review of intended use | Immediate escalation to senior regulatory manager for MFDS classification confirmation. |
| **Missing Korean labeling or IFU draft > 30 days before submission deadline** | Alert project lead; engage translation vendor. |
| **Inability to provide local clinical data while foreign CER acceptance is unclear** | Escalate to Clinical Affairs Lead – consider conducting a limited local study. |
| **Cybersecurity vulnerability discovered post‑release** | Trigger emergency MDR‑type field safety corrective action (FSCA) process and notify MFDS within 48 h per Korean reporting obligations. |
| **AI/ML algorithm update that alters intended use or performance claims** | Require re‑assessment of classification & possible supplemental approval – route to regulatory reviewer for MFDS AI guidance compliance check. |

---

### 6. Citations  

| Category | Reference |
|----------|-----------|
| **Framework references** (no verify caveat) | IEC 62304 Safety Class C; IEC 62304 §8.1; ISO 14971:2019; ISO 13485:2016; MFDS 사이버보안 가이드라인 2025; KGMP (MFDS 고시 제2025‑22호 – cited in source [1]). |
| **Instance identifiers** (appear in source) | No specific device clearance number, notice number or article/section identifier was found in the provided excerpts. *No specific identifier found in source — verify separately*. |

---

### 7. Peer Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions underlying the grade determination (3등급·4등급 vs 2등급), the completeness of the evidence list (especially the acceptance of foreign clinical evaluation reports), and any jurisdiction‑specific gaps such as Korean UDI format, post‑market surveillance SOP references, and AI/ML regulatory handling. Highlight any missing citations or areas where additional source material is required to substantiate the proposed submission pathway.

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> ① 촬영실 GUI SW 'default 3·4등급→허가' 단정 — KB 정합 위반(MFDS_인허가_상세가이드·제품별_등급분류 모두 2등급→인증) 핵심 판단 오류 ② PCCP='Pre-Market Cybersecurity Plan' 오확장 재발(11-06 kr-002 계열 — 실제 Predetermined Change Control Plan) ③ 'MFDS 고시 제2025-22호 cited in source' — 제시 excerpt에 없는 식별자 창작 의심 ④ 'K-code' 비표준 용어. 다중 심각.

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...
