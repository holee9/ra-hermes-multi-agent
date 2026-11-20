# KB Eval Checksheet - 2026-11-20 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261120-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "1ac5844bd2d69f7f", "source": "github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md", "source_hash": "fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `1ac5844bd2d69f7f`
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

> **Regulatory Draft – 510(k) Predicate‑Strategy for a New X‑ray Imaging Product**

---

### 1. Classification & Submission Route  
| Attribute | Determination |
|-----------|---------------|
| **Product class** | Class II (most diagnostic X‑ray systems are classified as Class II under **21 CFR Part 892**) |
| **Regulatory part** | Premarket notification – **510(k)**, 21 CFR §807.92 (Traditional/Abbreviated/Special) |
| **Relevant device‑type section** | Likely **21 CFR §892.2050** (Medical image management & processing system) or the appropriate X‑ray subsection of Part 892 – *needs confirmation* |
| **Submission type** | Traditional 510(k) if a legally marketed predicate with identical intended use and substantially similar technological characteristics exists; otherwise De Novo (NSE) pathway. |

---

### 2. Substantial‑Equivalence Decision Flow (per FDA 2014 Guidance, Appendix A)

1. **DP‑1 – Predicate legally marketed?**  
   *If No → NSE route (De Novo or PMA).*  

2. **DP‑2 – Same intended use?**  
   *If No → NSE.*  

3. **DP‑3 – Same technological characteristics?**  
   *If Yes → proceed to DP‑5; if No → evaluate safety questions (DP‑4).*

4. **DP‑4 – Do new tech differences raise novel safety/effectiveness questions?**  
   *If Yes → NSE.*  

5. **DP‑5 – Does performance data show the new device meets or exceeds predicate performance?**  
   *If Yes → SE; if No → NSE.*

*Citation:* no specific identifier found in source — verify separately.

---

### 3. Evidence Package Required for a Traditional 510(k)

| Evidence | Requirement | Typical Content |
|----------|-------------|-----------------|
| **Predicate Device(s)** | Legally marketed, FDA‑cleared; same intended use & comparable tech. | 510(k) number, device name, classification, labeling excerpts. |
| **Intended Use Statement** | Must match predicate or be justified as “substantially equivalent.” | Full text from labeling & instructions for use (IFU). |
| **Technological Characteristics Comparison** | Side‑by‑side table of hardware, software, performance specs. | Component list, imaging chain description, radiation dose parameters. |
| **Performance Data** | Bench, animal, and/or clinical testing demonstrating at least parity with predicate. | - Image quality metrics (MTF, NPS, DQE) <br> - Radiation safety tests (dose, beam quality) <br> - Software validation (IEC 62304) if applicable |
| **Risk Management File** | Hazard analysis & mitigations per **ISO 14971:2019**. | FMEA/FMECA tables, risk control measures, residual risk justification. |
| **Design Controls** | Conformity to QMSR – ISO 13485:2016 design‑control clauses (**ISO 13485 §7.3**). | Design History File (DHF) entries, verification & validation reports. |
| **Labeling & UDI** | Label must bear a UDI (plain‑text + AIDC) per **21 CFR §801.20+**; device identifier submission to GUDID (**21 CFR §830.300‑360**) | Final label artwork, packaging text, UDI issuance documentation. |
| **Sterilization / Reprocessing (if applicable)** | Control of records & labeling per **21 CFR §820.35** (QMSR). | Validation reports, reprocessor agreements. |

*Framework citations:* 21 CFR Part 892; 21 CFR Part 807; 21 CFR Part 801 §§801.20‑801.50; 21 CFR Part 830 §§830.20, §830.300‑360; ISO 14971:2019; ISO 13485:2016; IEC 62304 2006+A1:2015; IEC 60601‑1 2005+A1:2012+A2:2020; IEC 62366‑1 2015+A1:2020.

*Instance identifiers:* none provided in source – verify separately (e.g., predicate 510(k) number, exact §892 subsection).

---

### 4. Missing Information & Data Gaps (to be obtained before filing)

| Gap | Why it matters |
|-----|----------------|
| **Exact device functional description** (e.g., digital radiography vs fluoroscopy) | Determines correct Part 892 subsection and predicate search scope. |
| **Clear Intended Use claim** | Required for DP‑2 comparison; must be identical or defensibly equivalent. |
| **Candidate Predicate(s)** with 510(k) numbers | Needed to populate the comparison tables and satisfy SE criteria. |
| **Bench‑test protocols & results** (image quality, dose) | Basis for DP‑5 performance demonstration. |
| **Risk Management Report (ISO 14971)** | Demonstrates mitigation of new hazards; required for SE justification. |
| **Design Control artifacts (DHF entries)** | Required under QMSR to prove compliance with design‑control expectations. |
| **UDI issuance evidence** | Mandatory labeling element under 21 CFR §801.20+. |
| **Software documentation (if software present)** – verification/validation plan per IEC 62304. | Supports performance claims and risk controls for digital processing functions. |

---

### 5. Risk Controls & Mitigation Strategies  

1. **Radiation Safety** – Shielding analysis, dose‑monitoring interlocks, compliance with **IEC 60601‑2‑XX** (radiographic equipment).  
2. **User Interface / Software** – UI hazard analysis per **IEC 62366‑1**, usability testing, error‑proofing.  
3. **Electrical Safety** – Compliance with **IEC 60601‑1** clauses on protection against electric shock, EMC.  
4. **Mechanical Integrity** – Stress/deflection testing of gantry and detector housing.  
5. **Labeling & Training** – Clear instructions for safe operation, warning statements, and required training curricula.  

All controls must be documented in the risk‑management file and reflected in design verification/validation records.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **No legally marketed predicate identified** (DP‑1) | Escalate to senior RA; consider De Novo or PMA pathway. |
| **Intended use differs from any candidate predicate** (DP‑2) | Seek senior review; develop supplemental clinical data or consider NSE route. |
| **Technological characteristics diverge and raise novel safety questions** (DP‑4) | Initiate detailed risk assessment; involve engineering & QA leadership before proceeding. |
| **Performance data insufficient to meet/exceed predicate** (DP‑5) | Halt submission preparation; design additional studies or re‑engineer features. |
| **Missing QMSR evidence (design controls, record control)** | Escalate to Quality Management lead for corrective actions prior to filing. |
| **UDI / labeling non‑compliant** | Pause submission; involve Regulatory Labeling specialist. |
| **Regulatory deadline approaching with unresolved gaps** | Notify project manager and senior RA for risk–benefit decision on timeline vs data completeness. |

---

### 7. Bottom‑Line Recommendation  

- **If a predicate meeting DP‑1 through DP‑5 is confirmed**, prepare a **Traditional 510(k)** using the evidence list above.  
- **If any DP step fails** (particularly lack of legally marketed predicate or substantial tech differences), **escalate to senior RA** and evaluate a **De Novo (NSE) submission** as the next fastest credible route.

---

### 8. Peer‑Review Prompt  

> *Please review the above assumptions regarding device classification, the completeness of the evidence matrix, and any jurisdiction‑specific omissions (e.g., FDA‑specific reporting requirements not covered). Identify any gaps in the predicate‑search methodology or risk‑control documentation that could affect the SE determination.*

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

> §807.92를 510(k) 유형(Traditional/Abbreviated/Special) 근거로 오인용(계열 — §807.92=510(k) Summary 조항, 유형 구분은 Subpart E/가이던스 소관). QMSR 매핑(design→ISO 13485 §7.3·§820.35)은 정확 — SOUL 라인 반영.

**Source Excerpts**

1. Chunk `1061195424067242245`

> ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과제 3-2 SE 비교표 제출 필수 ---

2. Chunk `1072507187378217632`

> ### 4.1 SE 5단계 Decision Point (FDA 2014 Guidance Appendix A) ``` DP1. Predicate이 Legally Marketed Device인가? │ No → NSE (De Novo 또는 PMA) │ Yes ↓ DP2. 동일한 Intended Use인가? │ No → NSE │ Yes ↓ DP3. 동일한 Technological Characteristics인가? │ Yes → DP5 │ No ↓ DP4. 다른 기술특성이 Different Questions of Safety & Effectiveness를 제기하는가? │ Yes → NSE │ No ↓ DP5. 성능 데이터가 새 장치 ≥ Predicate 수준임을 입증하는가? │ Yes → SE (Clearance 가능) │ No → NSE ```

### kb-eval-20261120-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "bc4afd0df3c60671", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `bc4afd0df3c60671`
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

> **Regulatory Draft – 510(k) Predicate‑Strategy Outline**

---

### 1. Bottom‑Line Recommendation
| Item | Decision |
|------|----------|
| **Submission pathway** | Premarket Notification (510 (k)) – Class II, unless device function falls outside the imaging portfolio (then re‑evaluate under the appropriate 21 CFR part). |
| **Primary classification reference** | If the product is a medical image management/processing system → **21 CFR §892.2050 (Class II)**; if it is an image storage, communication, digitizer or hardcopy device, apply the corresponding §892.* sections. |
| **Next step** | Conduct definitive predicate‑device search in the FDA 510(k) database and complete a Substantial‑Equivalence (SE) comparison table. |

*If the device does not fit any §892 subsection, classification must be confirmed with the FDA Division of Industry and Consumer Affairs (DICA).*

---

### 2. Required Evidence Package (per 21 CFR §§807.92 & 892)

| Section | Typical content | Comments |
|---------|----------------|----------|
| **Device Description & Indications for Use** | Detailed narrative, intended patient population, clinical environment. | Follow the *eSTAR_01_Device_Description_IFU* guide (source [1]). |
| **510(k) Summary** | Concise overview of device, comparison to predicate(s), labeling excerpts. | Must be uploaded electronically per 21 CFR §807.92(c). |
| **Substantial‑Equivalence Comparison Table** | Side‑by‑side matrix: device description, intended use, technological characteristics, performance specifications vs. predicate. | Required by step 2 of the submission overview (source [2]). |
| **Performance Testing** | • Bench testing (accuracy, precision, repeatability) <br>• Usability/human factors validation <br>• Electromagnetic Compatibility (EMC) <br>• Software verification & validation (if applicable) | Align with FDA guidance on “Software as a Medical Device” and IEC 62304 (2006+A1:2015). |
| **Biocompatibility** | ISO 14971‑based risk assessment, ISO 10993‑1 (2018) testing plan/results. | Required for any patient‑contacting material. |
| **Labeling & IFU** | Full labeling set, including UDI conforming to 21 CFR Part 801 (§801.20+) and Part 830 system requirements. | Use the eSTAR template for electronic submission (source [2]). |
| **Quality Management System** | ISO 13485:2016‑based QMS compliant with **21 CFR Part 820 (QMSR)** – design controls, production controls, complaint handling per §820.35. | Evidence = SOPs, certificates of compliance, audit reports. |
| **Predetermined Change Control Plan (PCCP)** *(if AI/ML component)* | Documented plan for post‑market algorithm updates. | Required by FDA Guidance Dec 2024. |

---

### 3. Missing Information – Items Requiring Clarification Before Finalizing the Submission

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact device function & user interface** | Determines applicable §892 subsection and any special controls. | Obtain a finalized Device Description from product engineering. |
| **Intended use statement** | Drives predicate selection and risk analysis scope. | Draft precise Indications for Use (IFU). |
| **Material composition of patient‑contacting parts** | Needed to select ISO 10993 tests & risk assessment inputs. | Provide bill of materials (BOM) with material IDs. |
| **Software architecture details (if software‑based)** | Determines need for IEC 62304 compliance, PCCP, and software validation scope. | Supply software design documentation, versioning scheme. |
| **Proposed predicate devices** | The SE argument cannot be completed without identified cleared comparators. | Perform database search; list 510(k) numbers (e.g., K123456). |
| **Risk Management File (RMF)** | Required for ISO 14971‑based risk analysis and to map residual risks to controls. | Compile FMEA/FMECA, hazard mitigations, verification records. |
| **UDI strategy** | UDI placement on label & submission to GUDID must be demonstrated. | Define UDI carrier (GTIN/serial) and submit registration data. |

*All missing items should be resolved before the “eSTAR template” is populated for electronic filing.*

---

### 4. Core Risk Controls (per ISO 14971:2019 & FDA QMSR)

| Hazard Category | Control(s) | Evidence |
|-----------------|------------|----------|
| Electrical safety (IEC 60601‑1 compliance) | Design input limits, protective earth, insulation testing | Test reports, design verification data. |
| Electromagnetic interference (EMC) | Shielding, filtering, IEC 60601‑1‑2 testing | EMC test report. |
| Software failure / algorithm error | Code reviews, unit/integration tests, PCCP for post‑market updates | Verification & validation protocol/report; change‑control SOP. |
| Biocompatibility (patient contact) | Material selection per ISO 10993‑1, cytotoxicity/skin irritation testing | Test certificates. |
| Usability errors | Human factors engineering study, task analysis, labeling clarity check | Usability test report, user interface mock‑ups. |
| Data integrity / cyber security | Encryption, access controls, audit trails (IEC 62366‑1 compliance) | Security assessment documentation. |

---

### 5. Key Regulatory Citations (framework references)

- **Classification & device type:** 21 CFR §892.2050 (image management/processing) – Class II.  
- **510(k) content requirements:** 21 CFR §§807.92, 807.95, 892.* sections as appropriate.  
- **UDI label placement:** 21 CFR Part 801 (§§801.20‑801.50).  
- **UDI system & GUDID submission:** 21 CFR Part 830 (§§830.20, 830.300‑830.360).  
- **Quality Management System (QMSR):** 21 CFR Part 820 – design controls per ISO 13485 §7.3, production controls §7.5, complaint handling §8.2.2 + FDA §820.35.  
- **Risk management:** ISO 14971:2019 (risk analysis, evaluation, control).  
- **Biocompatibility testing:** ISO 10993‑1:2018.  
- **Software lifecycle:** IEC 62304:2006+A1:2015.  
- **Usability engineering:** IEC 62366‑1:2015+A1:2020.  

*No specific device identifiers or docket numbers appear in the source material; therefore no instance citations are provided.*

---

### 6. Human‑Escalation Triggers

| Condition | Escalation to Senior RA / Regulatory Lead |
|-----------|--------------------------------------------|
| **Unresolved classification** – device function does not map clearly to any §892 subsection. | Immediate review & possible pre‑submission meeting with FDA (Q‑Submission). |
| **Predicate search yields no suitable cleared device** or only devices from a different product code. | Consider De Novo pathway; flag for senior decision. |
| **Biocompatibility data unavailable for a patient‑contacting component**. | Halt submission until testing completed; notify project management. |
| **Software component lacking documented PCCP** (if AI/ML). | Escalate to software engineering lead & regulatory compliance officer. |
| **UDI strategy not finalized** – missing issuing agency accreditation or GUDID entry. | Pause electronic filing; coordinate with labeling team. |
| **Significant gaps in RMF** that could impact safety claims. | Escalate for risk‑management expert review. |

When any trigger is met, the RA should log a **Yellow Gate Action** and request human approval before proceeding.

---

### 7. Peer‑Review Prompt
> *Colleague, please challenge the assumptions above:  
> • Is the classification under §892 confident without a concrete device description?  
> • Are there any additional FDA programs (e.g., Special 510(k), Abbreviated pathway) that could shorten time‑to‑market for this product type?  
> • Have we captured all evidence categories required for an imaging‑device submission, especially regarding software and cybersecurity?*  

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

> IEC 62366-1(사용적합성)을 data integrity/cybersecurity 준거로 오귀속. §807.95는 존재하나(eCFR 확인: Confidentiality of information) 이를 510(k) 내용 요건 근거로 오인용 — 내용 요건은 §807.87. QMSR 3종 매핑(§7.3/§7.5/§8.2.2+§820.35) 정확.

**Source Excerpts**

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20261120-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "28b416f47df29080", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `28b416f47df29080`
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

> **Regulatory Draft – 510(k) Strategy for Imaging Workstation Software (GUI SW)**  

---

### 1. Bottom‑Line Recommendation  
- **Class:** Class II medical device – *Medical image management and processing system* → **21 CFR §892.2050**.  
- **Submission route:** Traditional PMA‑exempt **510(k) Premarket Notification** (Part 807).  
- **Core path:** Identify a single primary predicate meeting the checklist in Source [1]; if none is adequate, consider a De Novo request.

---

### 2. Classification & Submission Pathway  

| Item | Regulation |
|------|-------------|
| Device class | Class II under **21 CFR §892.2050** (medical image management/processing system). |
| Premarket submission | Standard **510(k)** (Section 807.92) with electronic 510(k) format. |
| QMS requirement | ISO 13485:2016‑based Quality Management System Regulation (QMSR) – **21 CFR Part 820** (design controls → ISO 13485 §7.3; production controls → ISO 13485 §7.5). |
| UDI labeling | Placement on label per **21 CFR §801.20‑§801.50** (label presentation) and system registration under **21 CFR Part 830** (UDI issuance). |
| Software documentation level | Follow FDA 2023 “Software Guidance” – select *Basic* or *Enhanced* as appropriate. |
| AI/ML component | If present, must be covered by a **Predetermined Change Control Plan (PCCP)** (FDA final guidance, Dec 2024). |

---

### 3. Required Evidentiary Package  

| Evidence Category | Details required | Source reference |
|-------------------|------------------|------------------|
| **Predicate justification** | • Search FDA 510(k) database by product code.<br>• Prioritize predicates cleared ≤5 yr; if >7 yr, provide supplemental “use of predicates” rationale (modernization).<br>• Confirm predicate is still on market and not recalled (MAUDE/Recall DB).<br>• Verify that the predicate’s Indications for Use are identical or broader than the applicant’s IFU. | Source [1] checklist; **no specific identifier found in source — verify separately** for exact predicate numbers. |
| **Intended Use Statement** | Exact verbatim wording from labeling; must be ≤or narrower than predicate’s claim. | – |
| **Software Design Documentation** | • Software Development Plan (SDP).<br>• Requirements Specification.<br>• Architecture & Interface Design (including DICOM SCU/SCP, Worklist, MPPS, Print).<br>• Source code excerpts for safety‑critical modules. | FDA 2023 software guidance; **no specific identifier found in source — verify separately**. |
| **IEC 62304 Safety Classification** | Assign Class A/B/C; provide justification and evidence of conformance (process verification, unit testing). | Source [2] – mentions “IEC 62304 Safety Class (A/B/C)”. |
| **Risk Management File** | ISO 14971:2019‑based risk analysis, evaluation, mitigation, and residual risk summary. Include FMEA/FMECA for AI/ML if applicable. | Framework reference – ISO 14971:2019. |
| **Verification & Validation (V&V)** | • Bench testing of acquisition, processing, display, storage, transfer, worklist.<br>• Clinical performance data (if new functionality).<br>• Interoperability testing against IHE profiles and HL7 FHIR if claimed. | – |
| **Cybersecurity** | • Threat analysis, mitigation plan, authentication & encryption design.<br>• Audit‑log specification, update mechanism security assessment.<br>• Reference NIST SP 800‑53 or FDA Cybersecurity Guidance (2022). | – |
| **SBOM** | Provide in SPDX or CycloneDX format for all third‑party components. | Source [2] – “SBOM 제공 형식”. |
| **Labeling & UDI** | • Device label with plain‑text UDI + 2‑D barcode (per §801.20+).<br>• IFU matching predicate scope.<br>• Software version and update policy. | Part 801 §§801.20‑801.50; Part 830 §§830.20, §830.300‑§830.360. |
| **AI/ML Controls (if applicable)** | • PCCP detailing pre‑authorized changes, monitoring plan.<br>• Data set documentation and performance metrics. | FDA Dec 2024 PCCP guidance; Source [2] – “AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정”. |
| **Software Level of Documentation** | Determine *Basic* vs *Enhanced* per 2023 FDA software guidance; include appropriate documentation depth. | FDA 2023 Software Guidance. |

---

### 4. Identified Missing Information (Gap Analysis)  

| Gap | Impact if Unresolved | Suggested Action |
|-----|----------------------|------------------|
| **Exact predicate(s)** – No specific 510(k) numbers identified in source. | Unable to demonstrate substantial equivalence; potential refusal‑to‑accept. | Conduct database search, document predicate IDs, evaluate market status, recall history. |
| **Indications for Use (IFU) text** – Not provided. | Mis‑alignment may trigger a “different intended use”. | Draft precise IFU and perform side‑by‑side comparison with predicate. |
| **Hardware platform details** – Minimum OS & HW requirements listed but not quantified. | Validation of performance on target platforms incomplete. | Provide detailed spec sheet (CPU, RAM, GPU, supported OS versions). |
| **AI/ML module scope** – Presence noted, but no PCCP or dataset description. | FDA will issue an Additional Information request for change‑control plan. | Create PCCP and submit as part of 510(k) if AI/ML is used. |
| **Cybersecurity Plan depth** – Only high‑level measures mentioned. | Insufficient evidence for “reasonable assurance” under 21 CFR 820.30 (design controls). | Develop detailed threat model, mitigation matrix, update process documentation. |
| **Interoperability claims** – HL7 FHIR/IHE support asserted but no test reports. | Claims may be considered unsubstantiated. | Perform conformance testing and attach reports. |
| **SBOM format confirmation** – Format selected (SPDX/CycloneDX) but not generated. | Missing SBOM can delay review under FDA’s software supply‑chain expectations. | Generate and submit SBOM alongside 510(k). |
| **Labeling & UDI draft** – No label mock‑up provided. | Failure to meet §801.20‑§801.50 may block clearance. | Prepare label with required elements, UDI placement, and graphics. |

---

### 5. Risk Management & Controls  

| Control Area | Required Output |
|--------------|-----------------|
| **Risk Analysis (ISO 14971:2019)** | Hazard identification, risk estimation, mitigation, residual risk justification. |
| **Software Safety Classification (IEC 62304)** | Assignment of safety class with rationale; implementation of required lifecycle processes (e.g., verification, validation). |
| **Cybersecurity** | Threat analysis, security requirements, encryption/authentication design, incident‑response plan. |
| **AI/ML Change Control (PCCP)** | Documented pre‑determined change control plan covering model updates, monitoring, and post‑market surveillance. |
| **Design Controls (ISO 13485:2016 / QMSR)** | Design input/output matrices, design verification & validation protocols, traceability to risk controls. |
| **Usability/Human Factors** | Formative/usability testing for GUI; UI/UX hazard mitigation (e.g., misinterpretation of images). |
| **Interoperability Testing** | DICOM conformance statements, IHE profile test reports, HL7 FHIR validation logs. |

---

### 6. Regulatory Citations (Framework References)

- **Device classification:** 21 CFR §892.2050 – Medical image management and processing system (Class II).  
- **Premarket notification:** 21 CFR §807.92 – 510(k) submission requirements.  
- **Quality System Regulation (QMSR):** 21 CFR Part 820 – ISO 13485:2016 referenced; design controls → ISO 13485 §7.3, production controls → ISO 13485 §7.5, complaint handling → ISO 13485 §8.2.2 plus FDA §820.35.  
- **UDI labeling:** 21 CFR §801.20‑§801.50 (label placement).  
- **UDI system:** 21 CFR Part 830 – formatting (§830.20), agency accreditation (§830.100‑130), GUDID submission (§830.300‑360).  
- **Software documentation levels:** FDA Guidance for Industry – “Content of Premarket Submissions for Management of Cybersecurity in Medical Devices” (2023) and “Guidance on Software Documentation” (2023) – Basic vs Enhanced.  
- **AI/ML change control:** FDA Final Guidance, *Predetermined Change Control Plan* (December 2024).  
- **Risk management standard:** ISO 14971:2019 (risk analysis & mitigation).  

*(No instance identifiers such as specific 510(k) numbers or docket IDs were present in the source excerpts; therefore “no specific identifier found in source — verify separately” applies to predicate selection and any regulatory docket references.)*

---

### 7. Human‑Escalation Triggers  

| Trigger Condition | Action Required |
|-------------------|-----------------|
| **Predicate not confirmed** (no clear 510(k) number, market status unknown, recall history pending). | Escalate to senior RA for predicate validation or consider De Novo path. |
| **AI/ML module present without a completed PCCP.** | Halt submission; develop and review PCCP before proceeding. |
| **Cybersecurity plan insufficient (threat model missing or no mitigation matrix).** | Forward to cybersecurity lead, obtain detailed plan, then resume. |
| **Risk Management File incomplete or lacking residual risk justification.** | Pause clearance preparation; request completion from engineering. |
| **Labeling/UDI draft not ready for electronic 510(k) submission.** | Notify regulatory operations to prepare label package. |
| **Interoperability claims unsupported by test data.** | Require conformance testing reports before finalizing the submission. |
| **SBOM not generated or format mismatched.** | Obtain SBOM from software supply‑chain team; verify SPDX/CycloneDX compliance. |
| **Discrepancy between intended use and predicate claim (IFU broader).** | Re‑draft IFU to be equal or narrower; obtain clinical justification if needed. |

---

### 8. Peer Review Prompt  

*“Colleague, please review the assumptions underlying our predicate selection (especially the five‑year recency rule and market status verification), the completeness of AI/ML change‑control documentation, and whether any EU/MDR concepts have inadvertently entered this US‑focused draft. Identify any jurisdiction‑specific gaps—particularly around QMSR implementation post‑Feb 2026 and UDI labeling—that may affect our 510(k) strategy.”*

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

> ① §807.92를 '510(k) submission requirements'로 오인용 2곳(계열) ② gap 표에 §820.30 'design controls' 잔존 1건 — QMSR 제거조항 계열 재발(타 부분은 §7.3/§7.5 정확). 사이버 가이던스 '2022' 연도 의심 재발.

**Source Excerpts**

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20261120-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "8d96f2215a30415a", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A1_Cover_Letter_템플릿.md", "source_hash": "27034e7259b482d0ed24713a8f35b4d9f41831499a0ac3e06bb99100802d0bf5"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `8d96f2215a30415a`
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

> **Regulatory Draft – 510(k) Predicate‑Strategy Package**  

---

### 1. Classification & Submission Route  
| Item | Determination |
|------|---------------|
| **Device Class** | To be confirmed by matching the intended use, technology and performance claims to the FDA classification database (21 CFR part 807). The draft assumes a **Class II** device pending identification of an appropriate predicate. |
| **Regulatory pathway** | **Premarket Notification (510(k))** – standard Sub‑section A submission (cover letter, device description, substantial‑equivalence comparison). |
| **Governing CFR parts** | • 21 CFR §807 – registration, listing and 510(k) submission requirements.<br>• 21 CFR §820 – Quality Management System Regulation (QMSR), effective 02 Feb 2026 (ISO 13485:2016‑aligned).<br>• 21 CFR Part 801 §801.20+ – label must contain a UDI (plain‑text and AIDC). |
| **Applicable guidance** | FDA “Refuse to Accept Policy for 510(k)s” (RTA) – provides the checklist for initial acceptance (no specific section number supplied in source; verify separately). |

---

### 2. Required Evidence Package  

| Section (per FDA RTA & typical 510(k) expectations) | Core content needed | Typical source / standard |
|------|------------------------|----------------------------|
| **Cover Letter** (Template T‑FDA510K‑A1 Cover‑Letter) | • Device Trade Name / Common Name.<br>• Statement of intended use, classification claim and reference to predicate device(s).<br>• Confirmation of compliance with QMSR and UDI labeling. | FDA 510(k) submission guidance; 21 CFR §807. |
| **Device Description** (Template T‑FDA510K‑B1) | • Detailed description of device hardware, software, accessories.<br>• Indications for use (clear, concise).<br>• Technological characteristics and performance specifications. | ISO 13485 §7.3 (design controls); IEC 62304 (software life‑cycle). |
| **Predicate Device Comparison Table** (Template T‑FDA510K‑B3) | • Side‑by‑side matrix of each technological characteristic, intended use, performance test outcomes.<br>• Clear justification of “substantially equivalent” for every claim. | FDA 510(k) substantial‑equivalence guidance; no specific identifier in source – verify separately. |
| **Performance Testing** | • Bench testing (e.g., accuracy, precision, reliability).<br>• Electrical safety & EM compliance (IEC 60601‑1 series where applicable).<br>• Biocompatibility (ISO 10993‑1) if patient contact.<br>• Software validation/verification (IEC 62304, IEC 62366‑1). | Relevant consensus standards (current editions listed in the knowledge base). |
| **Risk Management** | • ISO 14971:2019 risk analysis file with identified hazards, severity, probability, and mitigations.<br>• Controls mapped to design inputs & verification activities. | ISO 14971 (risk management). |
| **Labeling & UDI** | • Device label & IFU containing UDI in plain‑text (per 21 CFR §801.20+) and bar‑code/RFID (AIDC) per Part 830 requirements.<br>• GUDID submission evidence. | 21 CFR Part 801 §801.20+; 21 CFR Part 830 §§830.20, 830.300‑830.360. |
| **Quality System Evidence** | • Certificate of compliance with QMSR (ISO 13485:2016).<br>• Records of design controls, production processes and complaint handling per §820.35. | 21 CFR Part 820 (current sections as noted). |

---

### 3. Missing Information / Gaps Identified  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact device classification code** (e.g., 878.x for a specific imaging modality) | Determines applicability of special controls and the correct §892 sub‑section (if applicable). | Perform a classification search in FDA’s Product Classification Database; document the resulting product code. |
| **Predicate device identifiers** (K numbers, 510(k) numbers) | Required for substantive comparison table and to meet RTA “predicate evidence” requirement. | Identify at least one cleared device with identical/near‑identical intended use & technology; capture its 510(k) number. |
| **Performance test protocols & raw data** | FDA expects complete validation packages; missing data can trigger a Refuse‑to‑Accept (RTA). | Compile bench, animal or clinical test reports; ensure they meet consensus‑standard limits. |
| **Risk Management File (ISO 14971)** – hazard analysis not yet drafted. | Demonstrates mitigation of identified risks and satisfies §820.35 record‑control requirements. | Conduct risk assessment; populate ISO 14971 worksheet; map controls to design outputs. |
| **UDI implementation plan** – no GUDID submission evidence shown. | Label compliance cannot be verified without a registered UDI; failure results in RTA. | Generate and submit the device’s entry into the Global Unique Device Identification Database (GUDID). |
| **Software Documentation (if software‑driven)** – verification/validation plan absent. | Required under IEC 62304 & FDA guidance for software‑based devices. | Prepare Software Development Plan, Verification Summary Report, Validation Report. |

---

### 4. Risk Controls to Emphasize in the Submission  

1. **Design Controls** (ISO 13485 §7.3) – traceability matrix linking user needs → design inputs → design outputs → verification/validation.  
2. **Process Controls** (ISO 13485 §7.5) – manufacturing SOPs, environmental monitoring, sterilization validation where applicable.  
3. **Complaint Handling & Post‑Market Surveillance** – procedures per 21 CFR §820.35; include a Predetermined Change Control Plan (PCCP) if the device incorporates AI/ML algorithms.  
4. **Labeling Controls** – ensure UDI placement on label and packaging (per §801.20+).  
5. **Software Life‑Cycle Controls** – IEC 62304 compliance, including risk‑based classification of software modules, verification of each development phase.  

---

### 5. Citations  

| Item | Citation Type | Reference |
|------|---------------|-----------|
| FDA 510(k) submission requirements | Framework | 21 CFR §807 (registration & listing), §820 (QMSR), §801.20+ (UDI labeling). |
| QMSR current sections | Framework | 21 CFR Part 820 – applicability (§820.10) and record‑control (§820.35). |
| UDI system regulations | Framework | 21 CFR Part 830 §§830.20, 830.300‑830.360; labeling requirement §801.20+. |
| Consensus standards (current editions) | Framework | ISO 14971:2019; ISO 13485:2016; IEC 62304 2006+A1:2015; IEC 60601‑1 series 2005+A1:2012+A2:2020; IEC 62366‑1 2015+A1:2020; ISO 10993‑1 2018. |
| RTA guidance (Refuse to Accept Policy) | Instance – no specific identifier in source | “Refuse to Accept Policy for 510(k)s” Guidance – verify exact section numbers separately. |
| Predicate device comparison template | Instance – no specific identifier in source | T‑FDA510K‑B3 SE 비교표 템플릿 – verify separate if a predicate number is required. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Recommended action |
|--------|-----------------------|--------------------|
| **Unresolved classification** (no product code identified) | Could result in submission to the wrong regulatory pathway or missed special controls. | Senior RA reviews FDA Classification Database; if still ambiguous, consider a pre‑submission meeting with CDRH. |
| **No viable predicate device found** | Substantial equivalence cannot be demonstrated → 510(k) may be refused. | Escalate to product development lead to assess redesign or De Novo pathway feasibility. |
| **Incomplete performance data** (missing raw data, protocol deviations) | RTA will reject the submission, delaying clearance. | QA/Testing manager must provide missing datasets; RA verifies completeness before filing. |
| **Risk Management File absent or not linked to design inputs** | FDA may deem risk controls insufficient. | Risk management team prepares ISO 14971 file; RA reviews for traceability before inclusion. |
| **UDI/GUDID registration not confirmed** | Label non‑compliance leads to RTA. | Assign UDI coordinator to complete GUDID entry; obtain confirmation of successful upload. |
| **Software documentation gaps (IEC 62304) when software is a component** | FDA may request additional information, extending review time. | Software engineering lead prepares missing verification/validation artifacts; RA conducts gap analysis. |

---

### 7. Bottom‑Line Regulatory Judgment  

- The device appears to be a **Class II** medical device requiring a standard **510(k) Premarket Notification**.  
- Submission must contain: Cover Letter, Device Description, Predicate Comparison Table, complete performance testing data, a fully documented risk management file, UDI evidence, and QMSR compliance records.  
- Current source material provides the template framework but **lacks specific predicate identifiers, classification code, and supporting test data** – these gaps must be resolved before filing.  

If any of the escalation triggers above arise, the submission should be paused and escalated to senior RA or cross‑functional leadership for resolution.

---

#### Peer Review Prompt  
*“Please review this draft for any assumptions about device type, classification logic, or missing jurisdiction‑specific requirements (e.g., special controls, AI/ML change plans). Confirm that all required evidence items align with the latest FDA Refuse‑to‑Accept checklist and note any gaps in our source coverage.”*

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

> '878.x for a specific imaging modality' — 878=정형외과 패널, 영상기기는 892(동 문서가 §892도 병기) 오인용 예시. 나머지 정확(§820.10/§820.35 현행 조항 처리 포함).

**Source Excerpts**

1. Chunk `108125790997756669`

> ## 관련 문서 | 문서 | 연계 내용 | |------|-----------| | 13_규제평가_체크리스트/FDA_510k_RTA.md | FDA-510K-A1~A5 (Section A: Submission Coverage) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B1_Device_Description_템플릿.md | Device Description (본 Cover Letter의 Device Trade Name/Common Name 근거) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md | Predicate Device 비교 근거 |

2. Chunk `137836772921583289`

> ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance (최신 개정판 확인 후 인용 필요 — 본 v0.1은 구조만 정의, 조항 원문 대조 미실시)

### kb-eval-20261120-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "f165fed52f0a1f0e", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md", "source_hash": "6c864b98fca94d3a9546fde9cef298ef58210c9ac702628a937bcf05144604b6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f165fed52f0a1f0e`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/T-FDA510K-B3_SE_%EB%B9%84%EA%B5%90%ED%91%9C_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `6c864b98fca94d3a9546fde9cef298ef58210c9ac702628a937bcf05144604b6`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `T-FDA510K-B3_SE_비교표_템플릿.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 개정 이력 | 버전 | 일자 | 변경 내용 | 작성자 | |------|------|-----------|--------| | v0.1 | 2026-09-09 | 골격 템플릿 신규 생성 (FDA-510K-B3 증빙 미비 해소) | RA 담당자 | --- ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance Section B.3 - FDA 510(k) Premarket Notification Database (predicate 검색·K-number 확인용, 실 predicate 선정 시 필수 조회)
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

> **510(k) Predicate‑Strategy Draft**

---

### 1. Classification & Submission Route  
- **Device class:** Class II (most imaging and diagnostic devices fall under 21 CFR Part 892; if the device is an image‑management/processing system, the applicable classification is §892.2050).  
- **Regulatory pathway:** Premarket Notification (510(k)) – submission of a traditional 510(k) with a **Refuse‑to‑Accept (RTA)** check as defined in FDA’s *“Refuse to Accept Policy for 510(k)s”* Guidance, **Section B.3**.  

> **Citation:** Refuse to Accept Policy for 510(k)s – Section B.3 (source excerpt [2]).

---

### 2. Required Evidence Package (per 21 CFR §807.92 & FDA guidance)

| Evidence Element | Typical Content | Where it is required | Gap indicated by source |
|------------------|-----------------|----------------------|--------------------------|
| **Predicate device identification** | K‑number, cleared indication, classification panel, comparison matrix | 510(k) Substantial Equivalence (SE) narrative | No specific predicate K‑numbers supplied – *verify separately* |
| **Device description & intended use** | Detailed hardware/software architecture, clinical context, labeling claims | §807.92(a)(1) | Missing in template – *verify separately* |
| **Performance testing data** | Bench, benchtop functional testing; if applicable, animal or clinical studies showing equivalence | §807.92(a)(2) | No test results provided – *verify separately* |
| **Risk Management documentation** | ISO 14971:2019 risk analysis & mitigation report (including design‑controlled hazard identification) | §807.92(a)(3) | Not present in excerpt – *verify separately* |
| **Software validation (if applicable)** | IEC 62304 (2006+A1:2015) development lifecycle documentation, verification/validation plan, cybersecurity controls per FDA AI/ML guidance (PCCP where relevant) | §807.92(a)(4) | Not present – *verify separately* |
| **Labeling** | Full label set with UDI placement (plain‑text & AIDC) as required by 21 CFR §801.20 et seq.; labeling statements matching predicate claims | §801.20–§801.45 | No label package shown – *verify separately* |
| **UDI assignment** | Device Identifier (DI) and Production Identifier (PI) per FDA GUDID submission, format per 21 CFR §830.20 | Part 830 (label placement per Part 801) | Not referenced – *verify separately* |
| **Quality Management System evidence** | ISO 13485:2016‑based QMS compliant with the post‑Feb‑2026 QMSR (design controls → ISO 13485 §7.3; production controls → §7.5; complaint handling → §8.2.2 + §820.35) | Part 820, effective 02‑Feb‑2026 | No QMS documentation cited – *verify separately* |
| **Predetermined Change Control Plan (PCCP)** *(if AI/ML component)* | Documented change‑control plan covering anticipated algorithm updates | FDA Guidance Dec 2024 | Not mentioned – *verify separately* |

---

### 3. Missing Information & “Verify Separately” Flags  
- **Specific predicate K‑numbers** – source only notes the need to use the FDA 510(k) Premarket Notification Database for search; actual numbers must be identified.  
- **Evidence satisfying Guidance Section B.3 (RTA criteria)** – no checklist items or supporting documents are listed.  
- **Risk analysis, software validation, labeling, UDI, QMS records** – absent from the provided excerpt; each requires source verification.  

> *All items above are flagged “no specific identifier found in source — verify separately.”*

---

### 4. Core Risk Controls (to be documented)

1. **Hazard Identification & Mitigation** – ISO 14971:2019 process, capturing software‑related and hardware hazards.  
2. **Design Controls** – ISO 13485:2016 §7.3 (design and development planning, verification, validation).  
3. **Production Process Controls** – ISO 13485:2016 §7.5 (process validation, traceability).  
4. **Complaint & Servicing Records** – FDA‑specific §820.35 supplementing ISO 13485 §8.2.2.  
5. **UDI Traceability** – Part 801 label placement + Part 830 GUDID filing.  

---

### 5. Human‑Escalation Triggers  

| Trigger | Action Required |
|--------|-----------------|
| **Unresolved RTA deficiencies** (e.g., missing Section B.3 checklist items) | Pause submission; senior RA to convene a cross‑functional review and obtain the needed evidence before re‑submission. |
| **No viable predicate identified within FDA database** | Escalate to regulatory leadership for possible De Novo request or redesign of intended use. |
| **Risk analysis reveals high‑risk hazards without adequate mitigations** | Stop submission; trigger design‑control change and risk‑mitigation plan, involve engineering lead. |
| **UDI/labeling non‑compliance detected (e.g., missing plain‑text UDI on label)** | Immediate correction by labeling team; senior RA sign‑off before filing. |
| **QMSR audit notes gaps in ISO 13485:2016 compliance** | Escalate to Quality Assurance manager for corrective action and documentation prior to submission. |
| **Software component classified as AI/ML without PCCP** | Raise to Software Development Lead; develop Predetermined Change Control Plan before including software data in 510(k). |

---

### 6. Regulatory Judgment  

- The device appears to be a **Class II imaging‑system** requiring a **traditional 510(k)** submission.  
- The primary regulatory gap is the **absence of documented predicate identification and supporting evidence that satisfy FDA’s Refuse‑to‑Accept Policy Section B.3**.  
- Until all “verify separately” items (predicate K‑numbers, risk analysis, labeling/UDI, QMSR compliance, performance data) are compiled and assessed against the RTA checklist, **the submission should be held in a “not ready” status** and escalated to senior RA for remediation.

---

### 7. Peer Review Prompt  

> *Colleague, please challenge the following assumptions: (1) that the device falls under §892.2050; (2) that a traditional 510(k) is the optimal pathway versus a De Novo route if no suitable predicate exists; and (3) that all required evidence items listed above are exhaustive for an imaging‑system under current FDA guidance. Identify any jurisdiction‑specific gaps or missing citations that could affect our submission strategy.*

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

> §807.92(a)(1)~(4)에 근거요소 4종을 매핑 — §807.92(a)에 그러한 하위 항목 체계 없음(비존재 하위조항 창작, §807.87이 정보 요건 조항). QMSR 3종 매핑·RTA B.3(source) 정확.

**Source Excerpts**

1. Chunk `162881704545950641`

> ## 개정 이력 | 버전 | 일자 | 변경 내용 | 작성자 | |------|------|-----------|--------| | v0.1 | 2026-09-09 | 골격 템플릿 신규 생성 (FDA-510K-B3 증빙 미비 해소) | RA 담당자 | ---

2. Chunk `349912156821510479`

> ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance Section B.3 - FDA 510(k) Premarket Notification Database (predicate 검색·K-number 확인용, 실 predicate 선정 시 필수 조회)

## ra_eu

### kb-eval-20261120-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a56533756ed0b276", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a56533756ed0b276`
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

> **Regulatory Draft – Classification & Conformity Assessment Route (X‑ray Diagnostic Device with Software)**  

---

### 1. Scope & Device Overview  
| Item | Description |
|------|-------------|
| **Device type** | X‑ray diagnostic equipment that emits ionising radiation for radiography/radioscopy, together with integrated medical‑device software (SaMD) that processes the images and supports diagnostic decisions. |
| **Intended use** | Generation of diagnostic images of the patient’s anatomy; software provides image enhancement and decision‑support information to qualified healthcare professionals. |
| **Regulatory source** | MDR 2017/745 – classification rules (Annex VIII) and general safety & performance requirements (Annex I). |

---

### 2. Classification  

| Component | Applicable MDR rule (Annex VIII) | Resulting class* |
|-----------|---------------------------------|------------------|
| **X‑ray source / generator** (emits ionising radiation for diagnosis) | Rule 10 – “Ionising radiation emitting diagnostic devices” | **Class IIb** (per source excerpt) |
| **Imaging software (SaMD)** (provides information used for diagnostic decisions) | Rule 11 – “Medical Device Software” | **Class IIa** (unless the software alone could cause serious deterioration or death, in which case Class IIb/III would apply). |
| **Overall system** (integrated hardware‑software solution) | The higher class of any constituent part governs the system. | **Class IIb** |

\*The source excerpt explicitly states “X‑ray 발생장치 → Class IIb” under Rule 10 and notes SaMD classification under Rule 11.

**Citation:** Rule 10 (Annex VIII) – ionising radiation diagnostic device → Class IIb; Rule 11 (Annex VIII) – SaMD classification.  

---

### 3. Conformity Assessment Route  

| Class | Art. 52 reference | MDR Annex route (full designation) | Notified Body involvement |
|-------|-------------------|------------------------------------|---------------------------|
| IIb   | Art. 52(4)        | **Annex IX** (QMS + technical‑documentation assessment) **or** **Annex X** (type‑examination) **combined with Annex XI** (production conformity verification) | Mandatory NB review for either route |

Because the device is Class IIb, a full QMS‑driven assessment under Annex IX is permissible, but manufacturers often prefer the type‑examination route (Annex X + XI) when the device has complex hardware such as an X‑ray source.  

**Citation:** Art. 52(4); Annex IX; Annex X + XI.

---

### 4. Required Evidence & Documentation  

| dossier element | MDR requirement | Typical content |
|-----------------|------------------|-----------------|
| **Technical documentation (TD)** | Annex II §1‑6 (device description, intended use, design & manufacturing, GSPR compliance, benefit‑risk analysis, verification/validation) | • Detailed device description (hardware + software)<br>• Intended purpose statement<br>• Design drawings, schematics, BOM<br>• List of applicable standards (e.g., IEC 60601‑2‑54 for radiography equipment; IEC 62304 for software) |
| **Risk Management File (RMF)** | Annex I §3‑9 (risk management system) – ISO 14971:2019 as reference standard | • Hazard analysis, risk evaluation, residual risk assessment<br>• Specific controls for radiation exposure (Annex I §16.4) |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | • State‑of‑the‑art literature review (x‑ray diagnostics)<br>• Clinical data from equivalence studies or a clinical investigation if required |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | • Planned activities to monitor radiation safety, image quality, software performance after launch |
| **PMS System & PMS Plan** | Art. 83 (system); Art. 84 (plan) | • Procedures for incident reporting, trend analysis, field safety corrective actions |
| **Periodic Safety Update Report (PSUR)** | Art. 86 (Class IIb – update at least every 2 years) | • Benefit‑risk conclusions, PMCF results, sales & user population data |
| **EU Declaration of Conformity** | Art. 19; content as per Annex IV | • Manufacturer details, device identifier, conformity route, references to standards, signed by authorised representative |
| **Summary of Safety and Clinical Performance (SSCP)** | Required only for Class III/implantables – *not* mandatory here, but a concise summary may be prepared voluntarily. |
| **Labeling & IFU** | Annex I §23; also Annex II §5 (information supplied with the device) | • Radiation safety instructions, user warnings, software user manual, CE marking details |

---

### 5. Identified Missing Information  

1. **Exact intended‑use statement** (including patient population, clinical indications).  
2. **Full list of applicable harmonised standards** (e.g., IEC 60601‑2‑54, IEC 60601‑1, IEC 62366‑1) – not explicit in the source.  
3. **Clinical data package** – no evidence that a CE‑marking‑sufficient clinical investigation or equivalence study has been performed.  
4. **Software classification justification** – need to confirm whether the SaMD could influence therapeutic decisions (which would raise its class).  
5. **Risk control measures for radiation exposure** – must demonstrate compliance with Annex I §16 (e.g., dose‑monitoring, shielding).  
6. **Usability engineering evidence** (IEC 62366‑1) to address use‑error risks (Annex I §5).  
7. **Post‑market surveillance plan** – specifics on data collection methods, reporting timelines, and responsible personnel are absent.  

These gaps must be filled before the Technical Documentation can be submitted for NB review.

---

### 6. Core Risk Controls (aligned with GSPR)  

| GSPR clause | Control measure |
|-------------|-----------------|
| **§3 – Risk management system** | ISO 14971:2019‑based RMF covering all hardware and software hazards. |
| **§4 – Risk control measures** | Implement shielding, interlocks, dose‑limiting algorithms; software verification & validation per IEC 62304. |
| **§5 – Use‑error risks** | Conduct usability testing (IEC 62366‑1) to ensure correct operation by trained personnel; include clear warnings in IFU. |
| **§6 – Device lifetime** | Define service life of X‑ray tube, calibration intervals, and software version support policy. |
| **§16 – Protection against radiation** | Demonstrate compliance with IEC 60601‑2‑54 (radiation safety) and perform dose measurements per IEC 62220‑1‑1. |
| **§23 – Label & instructions for use** | Provide radiation safety warnings, exposure limits, emergency stop procedures, and software user guidance. |

---

### 7. Human‑Escalation Triggers  

| Trigger condition | Action required (who) |
|-------------------|-----------------------|
| **Unclear intended use or clinical indication** | Senior RA must request clarification from the product development team; cannot proceed with classification until resolved. |
| **Missing or insufficient clinical evidence** | Clinical affairs lead to initiate a clinical investigation or compile equivalence data; escalation to Project Manager for timeline impact. |
| **Software classification ambiguity (potential Class IIb/III)** | Software safety engineer and senior RA must perform a decision‑impact analysis; if class may increase, inform top management and reconsider conformity route. |
| **Absence of a complete PMS plan** | Quality manager must draft the PMS system; pending approval the NB submission is put on hold. |
| **Risk‑control gaps (e.g., radiation dose monitoring not demonstrated)** | Risk management team to generate additional test reports; issue logged in risk register and escalated to Head of R&D. |
| **Any non‑conformity identified during internal audit of TD** | Immediate corrective action per ISO 13485:2016; QA lead to document and report to senior management. |

---

### 8. Summary Judgment  

* The device is classified **Class IIb** under MDR Rule 10 (ionising radiation diagnostic equipment).  
* Conformity assessment must follow **Annex IX** (full QMS & TD review) *or* the **type‑examination route Annex X + XI**, both requiring NB involvement.  
* The current evidence package is incomplete: intended use, clinical data, risk controls for radiation, software classification justification, and a detailed PMS plan are missing. These items must be supplied before the Technical Documentation can be accepted by the Notified Body.  

---

### 9. Peer‑Review Prompt  

> *Colleague, please challenge the assumptions above:*  
> - Are we confident that Rule 10 alone determines Class IIb for the entire system, or could any ancillary functions (e.g., integrated dose‑calculation software) elevate the overall classification?  
> - Have we captured all relevant harmonised standards applicable to X‑ray diagnostic equipment and SaMD under MDR?  
> - Is there any recent EU guidance (2023/607 amendment) that modifies the PSUR cadence or PMS expectations for Class IIb devices that we need to incorporate?  

Your feedback will help ensure no jurisdictional nuance has been overlooked.

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
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. Rule 10 IIb·Rule 11 상향 요건·52(4) IX 또는 X+XI·PSUR IIb 2년·GSPR §3-6/16/23 전부 정확.

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261120-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "f2001ab2ca528f07", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f2001ab2ca528f07`
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

> **Regulatory Draft – Classification & Conformity‑Assessment Roadmap**

---

### 1. Scope of the assessment  
*The source material supplies only generic MDR procedural information (Article 51, Annex VIII classification rules; Article 61/Annex XIV clinical‑evaluation requirements; Art. 87 vigilance). No device‑specific description, intended purpose, or risk profile is provided.*  

Consequently the draft below outlines **the evidential framework that must be assembled** once the missing product data become available, and it flags the exact points at which a human reviewer must intervene.

---

## 2. provisional classification approach  

| Step | Requirement (regulatory source) | What must be supplied / verified | Current status |
|------|--------------------------------|----------------------------------|----------------|
| **2.1** Identify Intended Purpose & Indications for Use | Article 51 MDR – “classification principle” (device purpose drives the rule).<br>Annex VIII – 22 sequential rules, highest‑grade rule applied. | Complete device description, target patient group, mode of action, anatomical site, measurement/therapeutic function, whether the device is active, sterile, measuring or a reusable surgical instrument. | *Missing – no intended purpose supplied.* |
| **2.2** Select applicable Annex VIII rule(s) | “Sequential application of the 22 rules; highest class prevails” (source‑derived). | Map product’s functional attributes to the rule matrix (e.g., Rule 9, 10, 11, 17 etc.). | *Cannot be performed without step 2.1.* |
| **2.3** Determine final MDR class | Article 52 – class‑specific conformity routes (Art. 52(7) for Class I; Art. 52(6) for IIa; Art. 52(4) for IIb; Art. 52(3) for III). | Result of step 2.2. | *Pending.* |
| **2.4** Confirm need for Notified Body involvement | Classes Is/Im/Ir, IIa‑III require NB review (see Art. 52 table). | Class outcome from 2.3. | *Pending.*

> **Human escalation trigger #1:** *When the intended purpose is clarified, a classification workshop must be convened to apply Annex VIII rules and confirm the MDR class.*  

---

## 3. Conformity‑assessment route (once class is known)

| Class | Route (Article 52) | Required NB involvement | Key annexes for technical documentation |
|-------|-------------------|-------------------------|------------------------------------------|
| I (non‑sterile, non‑measuring, non‑reusable surgical) | Art. 52(7): self‑declaration – Technical Documentation (Annex II §§1‑6) + EU DoC (Art. 19/Annex IV). | **No** NB required. | Annex II; PMS system (Art. 83). |
| Is / Im / Ir | Art. 52(7): limited scope NB review – Annex IX Chapters I & III **or** Annex XI Part A (sterility/measuring/reuse). | Yes – limited NB audit. | Annex II + Annex IX §§1‑3 (QMS) + Annex XI §10/§18 as appropriate. |
| IIa | Art. 52(6): full NB review – Annex IX Chapters I & III **plus** technical‑documentation assessment of a representative device (Annex IX §4). | Yes – full NB audit. | Annex II + Annex IX §§1‑3; optional Annex XI if production verification chosen. |
| IIb | Art. 52(4): either (i) Annex IX with group‑level assessment **or** (ii) Annex X (type‑examination) **plus** Annex XI (production conformity). | Yes – NB audit of type‑exam or full technical file. | Annex II + Annex X; if using X+XI, both must be satisfied. |
| III | Art. 52(3): Annex IX (full technical‑documentation assessment) **or** Annex X + XI. | Yes – NB audit mandatory. | Annex II + Annex X (type‑exam). |

> **Human escalation trigger #2:** *If the class lands in IIa–III, a contract with an appropriate Notified Body must be initiated before any clinical investigation or PMCF plan can be finalised.*  

---

## 4. Evidence package required for the Technical Documentation (Annex II)

| Annex II Section | Required contents (framework) | Typical source documents |
|-------------------|--------------------------------|--------------------------|
| **1 – Device description & specification** | Intended purpose, indications, contraindications, variants, accessories, labeling (Annex I §23). | Product label, IFU, marketing brochure. |
| **2 – Manufacturer information** | Legal entity, address, contact details, UDI‑Issuer, Authorized Representative (Art. 11). | Company registration, AR agreement. |
| **3 – Design & manufacturing information** | Design drawings, specifications, manufacturing processes, quality‑system certificates (ISO 13485:2016), sterilisation validation (if applicable). | Design dossier, process flow charts. |
| **4 – General Safety & Performance Requirements (GSPR)** | Demonstration of compliance with Annex I §§1‑23 (risk management, radiation protection §16, software §17, active devices §18, etc.). | Risk Management File (ISO 14971:2019), verification/validation reports. |
| **5 – Benefit–Risk analysis & Conclusions** | Summary of risk evaluation, residual risk justification, benefit‑risk determination. | RMF summary, clinical‑evaluation conclusions. |
| **6 – Clinical Evaluation** | CER (Annex XIV Part A) *kept current* (Art. 61). If Class IIa–III, also PMCF plan & report (Annex XIV Part B). | Literature review, post‑market clinical follow‑up data, clinical investigation reports. |

> **Human escalation trigger #3:** *Any missing component from the above list must be flagged for acquisition before the Notified Body audit can commence.*  

---

## 5. Clinical evidence requirements

| Requirement | Regulatory basis | Typical evidence |
|-------------|------------------|------------------|
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 MDR. | Systematic literature review, state‑of‑the‑art analysis, clinical investigation data if required by rule. |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Annex XIV Part B. | PMCF protocol, periodic updates, summary of findings integrated into PSUR/benefit‑risk. |
| **PMS System** | Art. 83 MDR. | PMS Plan (Art. 84), procedures for trend reporting (Art. 88). |
| **Periodic Safety Update Report (PSUR)** | Art. 86 – required for Class IIa, IIb, III (frequency: every 2 years for IIa/IIb; annually for III/implants). | PSUR containing benefit‑risk conclusions, PMCF results, sales volume & user population data. |
| **Vigilance reporting** | Art. 87 MDR – serious incident and field‑safety corrective actions (FSCA). | Incident logs, FSCA procedures, communication records with competent authorities. |

> **Human escalation trigger #4:** *If the device is a Class IIa–III active or implantable product, a PMCF plan must be drafted and approved by the NB before market launch.*  

---

## 6. Risk‑management & GSPR linkage

| GSPR clause | Relevant risk control activity |
|--------------|--------------------------------|
| **§3** – Risk management system | ISO 14971:2019 compliant RMF (risk analysis, evaluation, control). |
| **§4** – Risk control measures | Implementation of protective measures identified in the RMF; verification of effectiveness. |
| **§5** – Use‑error risks | Usability engineering per IEC 62366‑1:2020; Human factors testing. |
| **§6** – Device lifetime & maintenance | Specification of service life, maintenance schedule, and end‑of‑life handling. |
| **§7** – Transport & storage | Validation of packaging, transport conditions, cold chain if needed. |
| **§8** – Known/foreseeable risks vs benefits | Benefit‑risk analysis (RMF summary) integrated into CER. |
| **§16** – Radiation protection (if applicable) | Compliance with IEC 60601‑2‑54 (radiography) and evidence of dose limits, shielding tests. |
| **§17** – Software safety | IEC 62304:2006+A1:2015 lifecycle; verification/validation reports. |
| **§22** – Devices for lay persons | Labelling & instructions meeting Annex I §23 readability requirements. |

> **Human escalation trigger #5:** *Any GSPR clause that cannot be demonstrably satisfied (e.g., lack of usability test data) must be escalated to the product development team before the technical file is considered complete.*  

---

## 7. UDI & EUDAMED registration

*Source excerpt mentions “UDI 포털” and “EUDAMED UDI/DEV”.*  

- **UDI‑Issuer**: Identify a competent UDI‑Issuer (e.g., GUDID, Korean UDI portal) and obtain a Basic UDI‑D.  
- **EUDAMED entry** – Populate device‑identification module (basic UDI data, manufacturer, AR).  
- **National portals** – If the product will be marketed in Korea, also register on the Korean UDI portal (as indicated).

> **Human escalation trigger #6:** *UDI allocation must be finalised before submission of the DoC and prior to placing the device on the EU market.*  

---

## 8. EU Declaration of Conformity (DoC)

- **Legal basis**: Art. 19 MDR – content defined in Annex IV.  
- Must reference the applicable conformity‑assessment route (e.g., “Conformity assessed according to Annex IX” or “Annex X + XI”).  
- Include signed statement, device identification, manufacturer details, NB certificate number (if applicable), and list of harmonised standards applied.

> **Human escalation trigger #7:** *Draft DoC cannot be signed until the NB issues a conformity‑assessment certificate and all referenced evidence is verified.*  

---

## 9. Summary judgment & next steps

| Item | Status |
|------|--------|
| Device intended purpose / indication | **Missing** – required to apply Annex VIII rules. |
| Classification outcome (Class I–III) | **Undetermined** – depends on step 1. |
| Technical documentation completeness | **Partial** – framework defined, content awaiting device‑specific data. |
| Clinical evidence (CER/PMCF) | **Pending** – need clinical data or justification for exemption. |
| PMS & vigilance infrastructure | **Conceptual** – processes must be documented per Art. 83‑87. |
| UDI allocation & EUDAMED entry | **Planned** – contingent on device ID. |
| Notified Body engagement | **Conditional** – will be required for any class > I or sterile/measuring/reusable instruments. |

**Immediate human actions needed**

1. Obtain the full *intended purpose, indications for use and mode of action* from product development.  
2. Conduct a classification workshop applying Annex VIII rule hierarchy; record the selected rule(s) and resulting MDR class.  
3. If Class IIa–III (or Is/Im/Ir), initiate contact with an appropriate Notified Body to discuss scope, timelines and fees.  
4. Draft a risk‑management plan (ISO 14971) and map each GSPR clause to concrete evidence items.  

---  

### Peer‑review request
> *Colleague, please challenge the assumptions above:*
> - Are there any MDR annexes or articles that we have omitted for this device type?  
> - Does the reference to “의료기기법 §31” imply additional national reporting obligations that must be reflected in our vigilance plan?  
> - Have we correctly interpreted the need for a PMCF plan versus reliance on existing clinical data for a Class IIa device?  

*Your feedback will ensure all jurisdictional gaps are covered before finalising the regulatory strategy.*

**Citation Lint (C1/C3 — 구조적 인용 오류 자동 감지)**

- ⚠️ Art. 52(6) is inconsistent with the device class on this line (Class I (52(7))) — verify the paragraph against MDR Art. 52. (`Art. 52(6)`)
- ⚠️ Art. 52(4) is inconsistent with the device class on this line (Class I (52(7))) — verify the paragraph against MDR Art. 52. (`Art. 52(4)`)
- ⚠️ Art. 52(3) is inconsistent with the device class on this line (Class I (52(7))) — verify the paragraph against MDR Art. 52. (`Art. 52(3)`)

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
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. Art.52 전표 정확 + PSUR 'III/implants annually' 이식형 포함 정확 + GSPR §17/§18/§22 매핑 정확. 미세: Is/Im/Ir 행에 'XI §10/§18' 병기(IIa 대안 조항 혼입, 'as appropriate' 헷지).

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261120-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "58241c40201f21bf", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `58241c40201f21bf`
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

> **Regulatory Draft – Classification & Conformity‑Assessment Roadmap**  
*Device concept inferred from source excerpts: an X‑ray imaging system intended for “standard diagnostic radiology” (generating digital images measured by DQE).*

---

### 1. Device Classification  

| Element | Reference | Determination |
|---------|-----------|---------------|
| **Rule applied** | Annex VIII, **Rule 10 – Radiology limb** (active device that emits ionising radiation for diagnostic purposes) | → **Class IIb** |
| **Supporting facts from source** | “Both indicated for standard diagnostic radiology” (Excerpt [1]); DQE ≥ 65 % measured according to IEC 62220‑1‑1. | Confirms device is an active X‑ray system, not merely a detector. |

*Result:* **Class IIb (MDR 2017/745).**

---

### 2. Conformity‑Assessment Route  

| Class | MDR route (Art 52) | Annex(es) required |
|-------|-------------------|--------------------|
| IIb   | **Art 52(4)** – either <br>• **Annex IX** (full QMS + technical‑documentation assessment) **or** <br>• **Annex X** (type‑examination) **+ Annex XI** (production conformity verification) | • Quality‑management system per Art 10(9) & Annex IX §2  <br>• Technical documentation (Annex II §§1‑6)  <br>• Type‑examination certificate (if Annex X route)  <br>• Ongoing production conformity verification (Annex XI) |

*Recommended pragmatic choice:* **Annex X + Annex XI** – the typical route for Class IIb imaging equipment, allowing a focused type‑examination on the radiation‑emitting sub‑assembly while retaining NB oversight of the whole device.

---

### 3. Required Evidence & Documentation  

| Item | Content (regulatory basis) | Source‑derived notes |
|------|----------------------------|----------------------|
| **Technical documentation** | Annex II §6.1 – includes device description, intended purpose, GSPR compliance, clinical evaluation, risk management file. | Device description must expand beyond “standard diagnostic radiology”. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art 61. Must show clinical equivalence to a predicate or state‑of‑the‑art device. | *Excerpt [1]* provides **CER Rev. 3** (Annex A) and DQE data (≥ 65 %). Verify that the CER also addresses safety, usability, and patient population. |
| **Test report for DQE** | IEC 62220‑1‑1 (2021) – measurement of detective quantum efficiency; referenced as **TR‑2024‑015** in source. | Attach full test report; confirm traceability to IEC standard. |
| **Risk Management File (RMF)** | ISO 14971:2019; Annex I §3‑9 (risk management system, risk controls, benefit–risk analysis). | Must contain radiation‑exposure risk assessment (§16.4) and residual‑risk justification. |
| **Post‑Market Surveillance (PMS) System** | Art 83 (system); Art 84 (plan). Provide PMS plan documenting data collection, trend analysis, field safety corrective actions. |
| **Periodic Safety Update Report (PSUR)** | Art 86 – for Class IIb at least every **2 years**. Include conclusions of benefit‑risk, PMCF results, sales volume & using population. |
| **PMCF Plan & Evaluation Report** | Annex XIV Part B. Outline prospective data collection (e.g., registry, real‑world performance) and subsequent evaluation. |
| **IEC conformity assessment** | • IEC 60601‑2‑54 (radiography equipment) <br>• IEC 60601‑2‑28 (X‑ray tube assemblies) <br>• IEC 62304 (software life‑cycle) <br>• IEC 62366‑1 (usability) | Verify that the device complies with each relevant standard; include test certificates. |
| **Labeling & IFU** | Annex I §23 – contents of labeling, safety information, intended use, contraindications. | Must reflect radiation dose limits, user training, and disposal instructions. |
| **EU Declaration of Conformity (DoC)** | Art 19; content listed in Annex IV. Signed by the authorised representative. | Ensure all referenced standards & NB certificates are enumerated. |
| **Summary of Safety and Clinical Performance (SSCP)** – *only if* device is **implantable** or **Class III** (not applicable here). | — | — |

---

### 4. Gaps / Missing Information (as highlighted by the NB Deficiency Letter concept)

| Gap | Why it matters (GSPR / MDR) | Action needed |
|-----|----------------------------|---------------|
| **Comprehensive Intended Use Statement** | Required for classification, risk analysis and CER scope (Annex II §1). | Provide a detailed description of clinical indications, patient groups, anatomical sites, and operating modes. |
| **Full Risk Controls for Radiation Exposure** | Annex I §16.4 – protection against ionising radiation. | Document shielding design, dose‑monitoring interlocks, maximum exposure limits, and verification testing per IEC 60601‑2‑54. |
| **Usability / Human Factors Analysis** | Annex I §5 (use‑error) & IEC 62366‑1. | Conduct a usability validation study; include findings in the RMF. |
| **Manufacturing Process Validation** | Annex II §4 (design & manufacturing). | Provide process qualification reports for tube assembly, detector fabrication, and software build. |
| **Post‑Market Surveillance Plan Detail** | Art 84 – must describe data sources, frequency of review, trigger thresholds. | Submit a written PMS plan covering adverse event reporting, trend analysis, and periodic updates. |
| **PMCF Implementation Details** | Annex XIV Part B – specify data collection methodology, sample size, statistical methods. | Draft a PMCF protocol; schedule interim reports aligned with PSUR cadence. |
| **Labeling Content (Radiation Safety Information)** | Annex I §23 – must include dose limits, protective measures, and instructions for lay‑person use if applicable (§22). | Produce draft IFU and label; review against GSPR. |
| **Evidence for Pediatric Use (if claimed)** | Clinical data required for any specific sub‑population (Art 61). | Provide clinical studies or literature supporting safety/efficacy in children, or restrict intended use to adults only. |
| **Signed Declaration of Conformity** | Art 19 – mandatory before CE marking. | Ensure an authorised person signs the DoC and references all applicable standards/NB certificates. |

---

### 5. Core Risk Controls (mapping to GSPR)

| GSPR § | Control measure (example) | Rationale |
|--------|---------------------------|----------|
| §3 (Risk management system) | ISO 14971‑based RMF covering radiation, electrical safety, software failures. | Provides systematic identification & mitigation of hazards. |
| §4 (Risk control) | Engineering controls: lead shielding, interlocks, automatic exposure termination. | Reduces residual risk from ionising radiation. |
| §5 (Use‑error) | Usability testing per IEC 62366‑1; clear IFU graphics for set‑up and operation. | Minimises operator error leading to overexposure. |
| §6 (Device lifetime) | Defined service life, periodic performance checks, replacement schedule for tube & detector. | Ensures safety throughout intended lifespan. |
| §7 (Transport & storage) | Protective packaging, humidity / temperature limits, handling instructions. | Prevents damage that could impact radiation output. |
| §8 (Known/foreseeable risks vs benefits) | Benefit‑risk analysis documented in CER & RMF; includes DQE performance, diagnostic accuracy, dose reduction compared to legacy devices. | Demonstrates overall net clinical benefit. |
| §16.4 (Protection against radiation) | Compliance with IEC 60601‑2‑54 limits on emitted dose, built‑in dosimetry, compliance test reports. | Directly addresses ionising‑radiation hazard. |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger condition | Escalation path |
|-----------|-------------------|-----------------|
| **NB Deficiency Letter issued** (e.g., missing risk analysis, incomplete PMCF) | Receipt of NB letter → **5 working days** to prepare a corrective‑action response. | RA Lead → Senior Regulatory Manager; if not resolved within additional 5 days, escalate to Head of Regulatory Affairs. |
| **Critical clinical data gap identified** (e.g., no paediatric safety data when intended for children) | Gap prevents completion of CER/PMCF. | Immediate pause of submission activities; notify Project Manager and Clinical Lead; obtain senior approval before proceeding. |
| **PMS adverse‑event trend exceeding predefined threshold** (per Art 88) | Trend identified in quarterly PMS review. | Rapid alert to Quality & Safety Team; trigger FSCA if required (Art 87); inform RA Lead for possible NB notification. |
| **Failure to obtain type‑examination certificate within scheduled timeline** | Delay > 30 days beyond agreed date with NB. | Escalate to Business Development/Program Management for resource reallocation and potential schedule impact. |
| **Regulatory deadline missed (e.g., PSUR submission)** | Approaching due date with < 10 days remaining and draft incomplete. | Automatic notification to Regulatory Director; request interim resources or extension justification. |

---

### 7. Summary Judgment  

- **Classification:** Class IIb – Rule 10 (radiology limb).  
- **Conformity Route:** Annex X (type‑examination) + Annex XI (production conformity verification) — *or* full Annex IX assessment if the manufacturer prefers a single‑NB route.  
- **Core Evidence Needed:** Complete CER with DQE data, risk management file addressing radiation risks, IEC‑conformity test reports, PMCF plan, PMS system & PSUR schedule, labeling/DoC, and all applicable IEC standards (60601‑2‑54, 60601‑2‑28, 62304, 62366‑1).  
- **Current Deficiencies:** Lack of detailed intended‑use statement, full radiation risk controls, usability evidence, manufacturing validation, PMS plan specifics, and signed DoC.  

**Action:** Compile the missing items listed in Section 4, submit a corrective‑action response to the NB within 5 working days, and proceed with the chosen conformity‑assessment route.

---

### Peer‑Review Prompt  

> *Colleague, please review the assumptions made about classification (Rule 10 radiology limb) and the recommended Annex X + XI route. Verify whether any additional classification rules (e.g., Rule 11 for embedded software) might push the device to a higher class, and check that all referenced GSPR sections are correctly aligned with the evidence gaps identified. Also assess whether any jurisdiction‑specific requirements (e.g., EU‑wide radiation dose limits) have been omitted.*

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
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. 52(4) IX 또는 X+XI·PSUR IIb 2년·Art 10(9) QMS·§16.4 정확. [최종 2점 — shadow 9차 하향 수용: TD 전체 내용(device description 등)을 'Annex II §6.1'로 귀속 — §6.1=preclinical/clinical data, device description는 §1 (조항-주제 오귀속). +PSUR IIb '2년'은 KB 오염 전파(case defect로 분리).]

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1107467848736309543`

> ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통지하는 문서. 국내 MFDS "보완 요청", FDA "Additional Information (AI) Request"에 해당하는 EU MDR 용어. ---

### kb-eval-20261120-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "108708a2854a29f9", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md", "source_hash": "9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `108708a2854a29f9`
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

> **Regulatory Draft – Classification & Conformity Route Assessment (EU MDR 2017/745)**  

---

### 1. Scope of the source material  
The supplied excerpts describe a **template for an EU Declaration of Conformity (DoC)** (see excerpt [2]). No product‑specific data (device description, intended purpose, model number, etc.) are present. Consequently the classification and the exact conformity‑assessment route cannot be finalised at this stage; the draft below outlines what must be supplied, how the classification is derived under MDR, which evidence the Notified Body will require, and where the current documentation is incomplete.

---

### 2. Classification & Conformity‑Assessment Route  

| Step | What is required | How to obtain it | Expected outcome |
|------|------------------|------------------|-------------------|
| **2.1 Device description & intended purpose** | Full textual description of the device, its accessories, and a concise “intended use” statement (as required in DoC line 4). | Populate the placeholders *Product name*, *Trade name*, *Model/Cat.#* and *Intended use* in the DoC template. | Enables selection of an Annex VIII classification rule. |
| **2.2 Apply Annex VIII rules** | Identify the appropriate rule (e.g., Rule 9, 10, 11, 17 or a measuring/sterile rule). | Compare the intended purpose against each rule in Annex VIII. | Determines device class (I, Is/Im/Ir, IIa, IIb, III). |
| **2.3 Determine conformity‑assessment route** | Use Art. 52 together with the class from 2.2. | <ul><li>Class I (non‑sterile, non‑measuring) → self‑declaration, no NB involvement (Art 52(7)).</li><li>Class Is/Im/Ir → Annex IX Chapters I & III or Annex XI Part A (NB required for sterile/measuring aspects, Art 52(7)).</li><li>Class IIa → Annex IX (full QMS + technical‑doc assessment) – NB involvement (Art 52(6)).</li><li>Class IIb / III → either Annex IX (full assessment) **or** Annex X + XI (type‑examination & production conformity verification) (Art 52(4)/3).</li></ul> | Defines the exact NB audit scope and the set of deliverables. |

*Because no intended use is provided, the classification step cannot be completed.*  

---

### 3. Evidence Packages Required for Each Conformity Route  

| Deliverable (MDR reference) | Relevance per class/route | Typical contents |
|------------------------------|---------------------------|------------------|
| **Technical Documentation** – Annex II §§1‑6 (incl. device description, design & manufacturing information, GSPR compliance, risk management file, verification/validation). | All classes. | Detailed drawings, specifications, labeling (Annex I §23), UDI‑DI (Annex VI Part C). |
| **EU Declaration of Conformity** – Annex IV (content listed in DoC template). | All classes. | Completed DoC with manufacturer name, SRN, authorised representative, Basic UDI‑DI, product identification, intended use, signatures (see excerpt [1] for signature block). |
| **Risk Management File** – ISO 14971:2019 (Art 10 & Annex I §3). | All classes. | Risk management plan, hazard analysis, risk evaluation, residual risk assessment, risk‑control measures, post‑market information updates. |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A; kept current under Art 61. | Class IIa, IIb, III and any class I device that claims a therapeutic claim or otherwise requires clinical data. | State‑of‑the‑art literature review, clinical data from investigations or equivalence, benefit–risk conclusion. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – Annex XIV Part B. | Class IIa, IIb, III; also recommended for high‑risk class I devices. | Planned PMCF activities, timeline, endpoints, results summary. |
| **PMS System / Plan** – Art 83 (system) and Art 84 (plan). | All classes. | Procedures for gathering and analysing post‑market data, vigilance reporting (Art 87), trend reporting (Art 88). |
| **Periodic Safety Update Report (PSUR)** – Art 86 (for Class IIa/IIb/III). | Class IIa & IIb – at least every 2 years; Class III – annually. | Benefit‑risk determination, PMCF findings, sales volumes, user demographics. |
| **Labeling & IFU** – Annex I §23. | All classes. | Mandatory safety information, intended use, symbols, UDI, instructions for lay users (if applicable). |
| **Quality Management System (QMS) certificate** – ISO 13485:2016 (Annex IX requirement). | Classes requiring NB involvement (Is/Im/Ir, IIa, IIb, III). | Certified QMS covering design‑control, supplier management, post‑market activities. |

---

### 4. Gaps / Missing Information Identified in the Source  

| Item | What is missing from the DoC template / source | Why it matters |
|------|-----------------------------------------------|----------------|
| **Manufacturer name & address** (field 1) | Placeholder `[회사명]`, `[등록 사업장 주소]` are empty. | Needed for Art 19(1) DoC obligations and EUDAMED SRN registration. |
| **EUDAMED SRN** | Not filled (`[EUDAMED SRN — 미취득 시 공백]`). | Required for traceability in the EU database (Art 33‑39). |
| **Authorised Representative details** (if manufacturer is non‑EU) | Empty placeholder. | Mandatory when a third‑country manufacturer exports to the EU (Art 10(9)). |
| **Basic UDI‑DI** (Annex VI Part C) | Placeholder only. | Needed for device identification in EUDAMED and on labeling (Art 27). |
| **Product identification** – name, trade name, model/ catalogue number | All placeholders. | Required for risk classification and to link the DoC with the technical documentation. |
| **Intended use statement** | Placeholder `[의도된 사용 목적 — 간략 기재]`. | Core input for Annex VIII rule selection; also drives clinical‑evaluation scope (Annex XIV). |
| **Signature block details** – signatory name and function | Placeholders only (`[서명자 이름]`, `[직함]`). | Legal responsibility under Art 19(1) must be traceable. |
| **Photograph / device illustration** | Not supplied. | Helpful for Annex II §1 description; may be required by NB. |

*No specific instance identifiers (e.g., case numbers, gazette notices) appear in the source excerpts.*  
> **Verification note:** *no specific identifier found in source — verify separately* (applies to all missing fields above).

---

### 5. Recommended Risk‑Control Measures (aligned with GSPR §3‑9)

1. **Risk Management Plan** – ISO 14971:2019 (Art 10, Annex I §3).  
2. **Design Controls** – Address hazards identified in the risk analysis; implement protective measures (e.g., redundancy for active devices, shielding for ionising radiation per GSPR §16.4 if applicable).  
3. **Usability Engineering** – IEC 62366‑1:2020 (GSPR §17) to mitigate use‑error (Annex I §5).  
4. **Electrical Safety** – IEC 60601‑1 series where relevant (GSPR §20).  
5. **Software Validation** – IEC 62304:2006+A1:2015 for any software component (GSPR §17 & §18).  

These controls must be documented in the Risk Management File and referenced throughout the Technical Documentation.

---

### 6. Citations (framework references)

| Reference | Content |
|-----------|---------|
| **Art 19** – EU Declaration of Conformity obligations (minimum content listed in Annex IV). |
| **Annex IV** – DoC template structure (source excerpt [2]). |
| **Annex II §§1‑6** – Technical Documentation required for all devices. |
| **Annex VIII** – Classification rules (Rule 9, 10, 11, 17, etc.). |
| **Art 52** – Mapping of device class to conformity‑assessment route (see table in Section 2). |
| **Art 61** – Keeping the CER up‑to‑date. |
| **Annex XIV Part A/B** – Clinical Evaluation and PMCF procedures. |
| **Art 83–86** – PMS system, plan, report, PSUR requirements. |
| **ISO 14971:2019**, **ISO 13485:2016**, **IEC 62366‑1:2020**, **IEC 62304:2006+A1:2015** – Supporting standards for risk management, QMS, usability, and software lifecycle. |
| **Annex I §3‑9** – General Safety & Performance Requirements (risk management, control measures, use error, lifetime, transport, benefits). |

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required | Who should act |
|--------|------------------|----------------|
| **Missing mandatory DoC fields** (manufacturer name, SRN, intended use, UDI‑DI) | Pause submission; request complete data from the product development team. | RA Lead / Project Manager. |
| **Unclear classification** (no intended‑use description) | Convene a cross‑functional review (clinical, engineering, regulatory) to draft a precise intended‑use statement and apply Annex VIII rules. | Regulatory Scientist + Clinical Lead. |
| **Intended use suggests a higher risk class** (e.g., active therapeutic function, ionising radiation) without supporting clinical data | Initiate a clinical‑investigation plan or collect equivalence data; elevate to senior RA for NB strategy decision. | Senior RA & Clinical Research Unit. |
| **Absence of Basic UDI‑DI** (no EUDAMED registration) | Register the device in EUDAMED, obtain SRN before DoC finalisation. | Regulatory Operations. |
| **Evidence gap for clinical evaluation** (e.g., no CE-marked predicate, insufficient literature) | Develop a PMCF study protocol or arrange a Notified‑Body‑accepted clinical investigation. | Clinical Development Lead. |
| **Risk Management File not aligned with GSPR §3‑9** | Conduct a risk‑management audit; update hazard analyses and residual‑risk justification. | Quality/Compliance Officer. |
| **Any discrepancy identified by the Notified Body during the audit** | Immediately notify the project team, revise technical documentation, and re‑submit the required sections. | Project Manager & RA Lead. |

When any of these triggers are hit, the responsible owner must log a **Work Package (WP) status change to “Yellow”** in the internal tracker and request formal review before proceeding.

---

### 8. Peer‑Review Prompt  

> *Please review this draft with another EU‑RA colleague. Focus on:*  
> - **Assumptions about classification** – Are we missing any device‑type clues that could move the class to IIb/III?  
> - **Source coverage** – Have we correctly identified all mandatory DoC elements from the template, and are there any extra fields in the actual MDR Annex IV that need attention?  
> - **Jurisdictional gaps** – Verify whether additional EU‑specific obligations (e.g., EUDAMED SRN, UDI‑DI, Authorized Representative) have been fully captured for a non‑EU manufacturer.  

--- 

*End of regulatory draft.*

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
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> ① AR(수입자) 지정 의무를 Art 10(9)(=QMS 조항)로 오귀속(AR은 Art 11) ② 사용적합성 IEC 62366-1을 GSPR §17(=소프트웨어)에 매핑 오귀속(§5 임). PSUR 'III annually'에 이식형 누락은 경미.

**Source Excerpts**

1. Chunk `1085205256397640486`

> 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` ---

2. Chunk `1141859994065237405`

> ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ───────────────────────────────────────────── 1. MANUFACTURER Company name : [회사명] SRN : [EUDAMED SRN — 미취득 시 공백] Address : [등록 사업장 주소] Authorised Representative: [EU 대리인명 및 주소 — 역외 제조사 해당 시] 2. SOLE RESPONSIBILITY STATEMENT This EU Declaration of Conformity is issued under the sole responsibility of the manufacturer named above. 3. BASIC UDI-DI [Basic UDI-DI — Annex VI Part C 기준] 4. PRODUCT IDENTIFICATION Product name : [제품명] Trade name : [상품명] Model / Cat.# : [모델 번호 / 카탈로그 번호] Intended use : [의도된 사용 목적 — 간략 기재] Photograph : [첨부...

### kb-eval-20261120-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "16a2ddf072647275", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md", "source_hash": "83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `16a2ddf072647275`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_AI_Act_MDR_%EC%A4%91%EC%B2%A9%EC%A0%81%EC%9A%A9_%EB%A7%A4%ED%95%91.md)
- Source hash: `83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_AI_Act_MDR_중첩적용_매핑.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은...
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

> **Regulatory Draft – AI‑enabled SaMD under the EU MDR & AI Act**

---

### 1. Device Scope (generic)

| Item | Content |
|------|---------|
| **Intended purpose** | Software that uses artificial intelligence (machine‑learning or rule‑based) to support diagnosis / therapy in a medical context (e.g., risk‑prediction for cardiovascular disease). |
| **Regulatory basis** | Regulation (EU) 2017/745 MDR – Annex I product group “Medical devices”<br>AI Act (Regulation (EU) 2026/1744) – high‑risk AI systems (Art. 6(1)). |

---

### 2. Classification under the MDR  

| Step | Reasoning | Citation |
|------|-----------|----------|
| **a. Verify that the product falls within Annex I, point 11** (MDR “medical device” definition). | Yes – software used for a medical purpose. | MDR Annex I, §1‑9 (generic definition). |
| **b. Apply the MDR classification rule for software** – Rule 11 (Annex VIII). | The software provides information that influences diagnostic/therapeutic decisions. | **Rule 11** (Annex VIII). |
| **c. Determine class based on impact of a wrong decision**: <br>‑ If an erroneous output could cause serious deterioration or surgical intervention → **Class IIb**.<br>‑ If only moderate risk → **Class IIa**. | Preliminary assessment points to at least **Class IIa**; many AI‑SaMDs are deemed **high‑risk** under the AI Act (Art. 6(1)). | **Art. 6(1) AI Act** – high‑risk AI system definition.<br>**MDCG 2025‑6/AIB 2025‑1 Q2·Table 1** (NB involvement for Class Is/Im/Ir and for high‑risk AI). |
| **d. Final class** | **Class IIa or IIb** – to be confirmed once the impact analysis is finalised. | No specific identifier found in source — verify separately (impact‑analysis matrix). |

---

### 3. Conformity‑Assessment Route  

| Class | MDR route (Art. 52) | NB involvement | AI Act overlay |
|-------|-------------------|----------------|----------------|
| **IIa** | **Art. 52(6)** – Annex IX (QMS + technical‑documentation assessment of one representative device). | Yes – NB audits the QMS and evaluates the TD. | High‑risk AI → full AI Act Chapter III requirements; registration in EU database (Art. 49 AI Act). |
| **IIb** | **Art. 52(4)** – Annex IX (full technical‑documentation assessment) *or* Annex X + XI (type‑examination & production verification). | Yes – NB required for the chosen route. | Same AI Act requirements as above; stricter post‑market monitoring (Annex III of AI Act). |

> **Citation**: Art. 52(6) & Art. 52(4) MDR; Annex IX (full QMS + TD assessment); Annex X + XI (type‑examination route).

---

### 4. Evidence Package Required for Submission  

| Evidence | Minimum content (MDR / AI Act) | Reference |
|----------|--------------------------------|-----------|
| **Technical Documentation** – Annex II §6.1 (device description, intended use, labeling, GSPR compliance). | – Device‑specification sheet<br>– Intended‑use statement<br>– Risk Management File (ISO 14971:2019)<br>– Verification & validation reports | MDR Annex II §§1‑6; **Art. 3(2) MDR** (TD requirement). |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A, kept current under Art. 61. | • State‑of‑the‑art literature review<br>• Clinical data from comparable devices or own studies<br>• Benefit‑risk analysis | **Annex XIV Part A**; **Art. 61 MDR**. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – Annex XIV Part B. | • Planned clinical investigations for AI algorithm performance drift<br>• Monitoring of real‑world outcomes | **Annex XIV Part B**; **Art. 84 MDR** (PMS plan). |
| **Post‑Market Surveillance (PMS) System** – Art. 83 & 84. | • PMS plan (risk‑based), incident reporting, trend analysis. | **Art. 83/84 MDR**. |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb: Art. 86 (every two years). | • Updated benefit‑risk conclusions<br>• PMCF findings<br>• Sales & user population data | **Art. 86 MDR**. |
| **AI‑specific documentation** – AI Act Chapter III (high‑risk AI system). | • Description of the AI model, training data set, performance metrics, reproducibility, robustness, explainability.<br>• Conformity assessment report per Annex III AI Act.<br>• Registration in EU database (Art. 49 AI Act). | **AI Act Art. 6(1)**; **Art. 49 AI Act**; **Annex III AI Act**. |
| **Usability & Cybersecurity Assessment** – IEC 62366‑1, IEC 60601‑1 (if applicable). | • Human factors analysis<br>• Threat modelling and mitigation plan. | **IEC 62366‑1:2020**, **IEC 60601‑1 +A2:2020** (where relevant). |
| **Declaration of Conformity (DoC)** – Art. 19, content per Annex IV. | • Manufacturer details, device identification, conformity claims, signed by authorised representative. | **Art. 19 MDR**, **Annex IV**. |

---

### 5. Gaps / Missing Information (to be provided before NB submission)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended‑use wording & patient population** | Needed for classification rule justification and for the AI Act high‑risk assessment. | Draft detailed IFU; obtain clinical stakeholder sign‑off. |
| **Algorithmic risk analysis (bias, drift, robustness)** | Required by AI Act Chapter III and ISO 14971 residual‑risk evaluation. | Conduct systematic risk assessment; document mitigation. |
| **Clinical data source & justification of equivalence** | To substantiate CER and support high‑risk AI claim. | Provide literature list + any pilot study results. |
| **Training‑data provenance, size, representativeness** | AI Act demands transparent data governance. | Compile dataset documentation (metadata, cleaning procedures). |
| **PMCF plan specifics (sample size, endpoints, follow‑up period)** | PSUR & Annex XIV Part B require a concrete plan. | Develop protocol; align with clinical experts. |
| **Post‑market monitoring of algorithm updates** | Ongoing compliance under AI Act and MDR PMS obligations. | Define version‑control & update‑impact assessment process. |

---

### 6. Risk Controls (aligned to Annex I GSPR)

| GSPR article | Control measure | Evidence |
|--------------|-----------------|----------|
| **§3 – Risk Management System** | Implement ISO 14971:2019 RMF; include AI‑specific hazard identification. | Risk Management File. |
| **§4 – Risk Control** | Apply design mitigations (e.g., fail‑safe mode, alerts for low confidence scores). | Design specifications & verification reports. |
| **§5 – Use Error** | Conduct usability testing per IEC 62366‑1; integrate user training. | Usability study report. |
| **§6 – Device Lifetime** | Define software lifecycle (updates, deprecation) and support period. | Software maintenance plan. |
| **§8 – Benefit–Risk** | Quantify clinical benefit versus AI‑related residual risk (e.g., false‑negative rate). | CER & PMCF data. |
| **§16 (4) – Radiation protection** | Not applicable (unless device incorporates ionising radiation). | N/A. |
| **§22 – Lay‑person use** | If intended for lay users, include clear decision‑support limits and warnings. | IFU and labeling review. |

---

### 7. Human‑Escalation Triggers  

1. **Classification Uncertainty** – If the impact analysis cannot conclusively place the device in Class IIa vs IIb, senior RA must approve a formal classification justification (escalate to Head of Regulatory).  
2. **AI Act High‑Risk Determination** – Any doubt whether Art. 6(1) applies → legal/compliance review before proceeding with NB assessment.  
3. **Missing Clinical Evidence** – Absence of sufficient clinical data or equivalence justification → pause dossier preparation; inform Clinical Development lead.  
4. **NB Feedback Requiring Additional PMCF** – If the Notified Body requests supplementary post‑market clinical follow‑up studies, raise a change‑control request to project management and update timeline.  
5. **Algorithm Update Impact** – Deployment of a software version that modifies AI behaviour > 10 % change in performance metrics → immediate risk reassessment and possible re‑classification; trigger urgent notification to NB.  

---

### 8. Peer‑Review Prompt  

> *@RA‑Peer* – Please challenge the following assumptions:  
> 1. The preliminary classification as **Class IIa/IIb** based solely on Rule 11 and AI‑Act high‑risk definition. Are there any product‑specific nuances (e.g., intended use, invasive nature) that could shift the class?  
> 2. The sufficiency of the listed evidence package for a **high‑risk AI system** – does the AI Act require additional artefacts (e.g., conformity‑assessment report per Annex III) not captured here?  
> 3. Any jurisdictional gaps, such as requirements from the upcoming **Regulation 2026/1744** that have not been covered (e.g., specific transparency obligations).  

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

> ① 'MDR Annex I point 11/§1-9 = medical device 정의' 오귀속 — 소스의 Annex I은 AI Act Annex I(조화법령 목록), MDR Annex I §1-9는 GSPR이며 정의는 Art 2(1) ② Art 3(2)를 TD 요건 근거로 오귀속(Art 10(4)이 TD 조항). 'Reg 2026/1744'·'MDCG 2025-6'은 소스 기반 무죄(audit #1041 확정값).

**Source Excerpts**

1. Chunk `1013595113860735371`

> ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은 NB 관여 → **Art.6(1) 해당** (MDCG 2025-6/AIB 2025-1 Q2·Table 1) └─ No: Annex III 별도 해당 여부 확인 2. High-risk 확정 시 ├─ AI Act Chapter III 전체 요건 적용 ├─ 적합성평가 경로: MDR 경로에 AI Act 요건 통합 └─ EU DB 등록 의무 (Art. 49) ``` **판정 기준**: 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높다.

2. Chunk `1015646396132986584`

> lan for AI-Enabled Device Software Functions (Final; 2025-08-18 현재 본; Docket FDA-2022-D-2628; original final issued December 2024)"으로 갱신. 범위를 ML→**AI-enabled device software functions 전반**으로 보정. FDA Guidance 페이지(2025-08-18 current)로 직접 재확인. 사내 SOP-AIGOV-001 v0.3 "FDA PCCP Guidance 2024" 표기와 정합 회복 | | v0.9 | 2026-09-11 | **P0 사실성 정정 (audit #1041)** — Regulation (EU) 2026/1744(Digital Omnibus on AI, 채택 2026-07-08 / OJ 2026-07-24 / 발효 2026-07-27, CELEX 32026R1744) 확정 반영. §3 일정표에 발효일·Annex III 2027-12-02·Annex I 2028-08-02 행 신설, '잠정 합의 시·예상·미완료' 조건부 표현 전량 제거. §12.2 시나리오 (A)/(B) 분기를 (A) 확정으로 종결하고 (B) 트랙 삭제, 기준일을 2028-08-02로 재설정. §12 D-36 D-day·...

## ra_kr

### kb-eval-20261120-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "122562f0489ad590", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `122562f0489ad590`
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

> **Regulatory Draft – MFDS Classification & Submission Pathway (Software‑Based Medical Device)**  

---

### 1. Determined Korean Grade & Submission Route
| Item | Finding | Source |
|------|---------|--------|
| **Korean grade** | **2등급** (may be upgraded to a higher grade depending on the level of auxiliary function) | Excerpt 2 – “국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능)” |
| **Submission track** | **인증** (technical‑documentation review by an MFDS‑designated 심사기관) – default for 2등급 devices | Korean regulatory framework § (「의료기기 품목 및 품목별 등급에 관한 규정」) – the standard pathway for all 2등급 items is 인증; no exemption to 허가 noted. |
| **Applicable Guidance** | *디지털의료기기소프트웨어 허가·심사 가이드라인* (medical‑software approval/examination guideline) & the 2025‑01‑24 Digital Medical Products Act (디지털의료제품법) for AI/SW products | Excerpt 2 – “근거: 의료용 소프트웨어 허가·심사 가이드라인, … 2025년 신법: 디지털의료제품법” |
| **A‑code (품목코드)** | Not yet assigned – must be secured before final submission. | Excerpt 1 – “식약처 품목코드(A-code) 확정” (to‑do item). |

**Regulatory judgment:** The device is presently classified as **2등급** and will follow the **인증** pathway, pending confirmation of the A‑code and verification that no functional elements trigger a higher grade.

---

### 2. Core Evidence Package Required for 인증

| Evidence | Requirement (Korean law / guideline) | Typical contents | Framework reference (no identifier needed) |
|----------|--------------------------------------|------------------|--------------------------------------------|
| **Technical Documentation** (동일성 검증을 위한 기술문서) | MFDS 인증심사 기준 – 전자·소프트웨어 제품에 대한 전체 설계·시험 자료 | • Device description & intended use <br>• Software architecture, algorithms, flowcharts <br>• IEC 62304‑compliant software life‑cycle documentation | IEC 62304 (2006+A1:2015) |
| **Risk Management File** | MFDS 위험관리 가이드라인 (ISO 14971 적용 의무) | • Hazard analysis & risk evaluation <br>• Risk control measures <br>• Residual risk justification <br>• Post‑market surveillance plan | ISO 14971 (2019) |
| **Usability / Human Factors Report** | 의료용 소프트웨어 가이드라인 – IEC 62366‑1 요구 | • Use‑case analysis, user interface specifications, validation testing with representative users | IEC 62366‑1 (2015+A1:2020) |
| **Cybersecurity Assessment** | MFDS 사이버보안 가이드라인 (참조 표준 IEC 81001‑5‑1) | • Threat modeling <br>• Security controls, patch management <br>• Incident response plan | IEC 81001‑5‑1 (2021) |
| **Korean Language IFU & Labels** | MFDS 라벨링·사용설명서 규정 (필수 한글) | • Full Korean user manual <br>• Label artwork with required symbols, registration number placeholders | — |
| **Clinical Evaluation** | 의료기기법 제28조(2) – 2등급 소프트웨어에 임상 평가 필요 (외국 CER 허용 여부은 MFDS 고시 확인 필요) | • Local clinical data or accepted foreign Clinical Evaluation Report (CER) <br>• Gap analysis vs. Korean patient population | no specific identifier found in source — verify separately |
| **KGMP Facility Verification** (if applicable) | KGMP 인증 (§28, 의료기기법) – 제조·품질관리 시설 | • KGMP certificate or evidence of compliance for the software development environment (e.g., ISO 13485‑aligned QMS) | ISO 13485 (2016) |
| **A‑code Confirmation** | MFDS 품목코드 부여 절차 | • Official A‑code letter from MFDS | no specific identifier found in source — verify separately |

---

### 3. Missing Information & Items to Secure Before Submission

| Gap | Why it matters | Action / escalation trigger |
|-----|----------------|----------------------------|
| **A‑code (품목코드)** not yet assigned. | Required on all labeling, IFU, and submission forms. | Escalate to product strategy team – request MFDS 품목코드 신청 ASAP. |
| **Final intended use / indication wording** (including target patient population). | Determines grade & clinical evidence scope; impacts risk analysis. | Confirm with R&D; if indication expands (e.g., diagnostic vs. monitoring) re‑evaluate grade. |
| **Whether the software is “독립형” or “보조형”.** | Independent‐type SW follows separate usability guideline; may affect classification. | Verify architecture; if independent, add 독립형 SW 사용적합성 가이드라인 compliance evidence. |
| **Foreign Clinical Evaluation Report (CER) acceptance** – existence of an MFDS notice permitting the specific foreign CER (e.g., FDA 510(k) predicate). | If local clinical data are not generated, reliance on foreign CER must be justified per MFDS scope change. | Search MFDS 고시/notice for foreign‑CER mutual‑recognition; if unavailable, plan Korean clinical study. |
| **Software “Predicate Device” selected via FDA Product Classification Database** (Excerpt 1). | Needed only if a 510(k) pathway is used as supporting evidence for safety/effectiveness. | Document predicate device and justification; ensure MFDS accepts the foreign classification as supplemental data. |
| **KGMP certification status of development environment**. | Required for manufacturing facilities; some software may be exempt but must be documented. | Obtain KGMP compliance statement or exemption rationale (MFDS guideline). |
| **Cybersecurity‑specific evidence** (e.g., penetration test reports). | MFDS cybersecurity guide mandates demonstrable controls. | Conduct and attach third‑party security assessment report. |

---

### 4. Core Risk Controls to Highlight in Submission

1. **Risk Management Plan** – ISO 14971‑based hazard identification, risk evaluation, mitigation, residual risk justification.
2. **Software Life‑Cycle Processes** – IEC 62304‑aligned development phases (planning → design → verification/validation → maintenance).
3. **Usability Engineering** – IEC 62366‑1 activities focusing on user interface clarity for Korean end‑users.
4. **Cybersecurity Measures** – Threat modeling, encryption, secure update mechanism, incident response per IEC 81001‑5‑1.
5. **Post‑Market Surveillance (PMS) Plan** – Real‑world performance monitoring, adverse event reporting, periodic safety updates.

---

### 5. Human‑Escalation Triggers

| Trigger | Reason for Escalation | Responsible Party |
|---------|----------------------|-------------------|
| **Unresolved grade ambiguity** (evidence that auxiliary function may elevate to 3등급) | Potential shift from 인증 → 허가, with major timeline impact. | Regulatory Lead – request senior review & possible MFDS consultation. |
| **Absence of verified A‑code** after 2 weeks of filing the request | Submission cannot be completed; labeling non‑compliant. | Product Management – prioritize MFDS communication. |
| **Lack of acceptable clinical evidence** (no local data, no foreign CER allowance) | Regulatory refusal risk under §28(2). | Clinical Affairs – initiate Korean feasibility study or seek alternative evidence sources. |
| **KGMP certification not obtained for the development facility** (if required) | Non‑compliance with 제조·품질관리 법령; may block 인증. | Quality Management – obtain KGMP or document exemption. |
| **Cybersecurity assessment fails** (critical vulnerabilities remain) | MFDS cybersecurity guidelines are mandatory for software products. | IT Security – remediate and re‑test before submission. |

---

### 6. Peer‑Review Prompt  

> **To: RA Team Member (e.g., Ji‑sun, Regulatory Affairs)**  
> Please review the assumptions above, especially:  
> • Whether the device’s auxiliary function truly limits it to **2등급** or if any functional element pushes it to a higher grade under the latest MFDS 규정.  
> • The completeness of the clinical evidence strategy – does an existing MFDS notice permit reliance on the FDA predicate CER referenced in our preliminary market analysis?  
> • Any gaps in KGMP applicability for software‑only products that we may have overlooked.  

Your feedback will be incorporated before finalizing the submission package.

--- 

*All citations are derived directly from the provided source excerpts or from the standard editions listed in the knowledge base; no invented identifiers are used.*

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

> 의료기기법 제28조(2)를 '2등급 SW 임상평가 필요' 근거로 오귀속 — 제28조는 KGMP 근거(사실표 확정값). 2등급→인증·등급 근거는 정확.

**Source Excerpts**

1. Chunk `1097646391221557778`

> ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정

2. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

### kb-eval-20261120-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "1e35947a8f3e6013", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `1e35947a8f3e6013`
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

> **Regulatory Draft – P3 촬영실 GUI SW (Digital‑Medical‑Device Software)**  

---

### 1. Korean Classification & Submission Route  

| Item | Assessment | Rationale / Source |
|------|------------|---------------------|
| **Device grade** | **2등급 or unassigned** – must be verified. | The excerpt states the GUI SW “2등급이든 등급 미지정이든” (Chunk [2]), indicating that its exact grade is not yet fixed and has to be confirmed against 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **Default submission track** | **인증** (Technical‑documentation review by an MFDS‑designated 심사기관) – applicable for 2등급 devices. | Korean regulation mandates certification for all 2등급 items unless a specific exemption applies (MFDS_인허가_상세가이드.md §2). |
| **Potential exemption / alternative route** | **면제·대체** path under the revised Digital‑Medical‑Product Law (디지털의료제품법 시행규칙) – possible if AI module is added later. | The source notes that “GUI SW가 2등급이든 등급 미지정이든 … 면제·대체 경로가 열린다” (Chunk [2]) and references the **제25조 각 호** of the 시행규칙 (2026‑01‑23 개정) as the legal basis – verification required. |
| **우수관리체계 특례** | May be used to convert QMS maturity (KGMP/ISO 13485) into a regulatory benefit. | Highlighted in Chunk [2]; applicable when the manufacturer holds an established KGMP‑compliant quality system. |

---

### 2. Required Evidence for Initial Certification (if pursued via 인증)

| Requirement | Details |
|-------------|---------|
| **Device Description & Intended Use** | Clear statement that the software is a GUI for P3 X‑ray rooms, functions as a digital‑medical‑device (software) with optional AI decision‑support add‑on. |
| **Risk Management File** | ISO 14971:2019‑based hazard analysis, risk control measures, residual risk evaluation and post‑market surveillance plan. |
| **Software Life‑Cycle Documentation** | IEC 62304:2006+A1:2015 compliant development plan, architecture description, verification/validation protocols, configuration management. |
| **Cybersecurity** | IEC 81001‑5‑1:2021 reference; summary of threat modelling, mitigation, and update strategy (especially if AI module will be added later). |
| **Quality Management System** | KGMP certification evidence (or ISO 13485:2016 certificate) – required for any 2등급 device and mandatory to invoke the 우수관리체계 특례. |
| **Labeling & IFU** | Korean‑language labeling, user manual, safety notices; compliance with MFDS labeling rules (no foreign language only). |
| **Clinical Evidence (if no exemption)** | • Comparative study design (AI‑assisted vs clinician‑only) per the 2025‑10‑31 임상시험 가이드라인 개정 (9종) — requires analytical accuracy, efficacy size, dropout management. <br>• For the baseline GUI (no AI), evidence may be limited to usability/validation data; however, MFDS may still request a minimal clinical evaluation because the software influences diagnostic workflow. |
| **Regulatory‑Instrument Citations** | • **디지털의료제품법 시행규칙 (2026‑01‑23 개정)** – particularly **제25조 각 호** for exemption/alternative route requirements (“[검증 필요]”). <br>• **2025‑10‑31 임상시험 가이드라인 9종 개정** – defines comparative design and analytical accuracy criteria for AI‑augmented devices (Chunk [1]). |

---

### 3. Missing / Unverified Information (Action Items)

| Gap | Why it matters | Suggested verification |
|-----|----------------|------------------------|
| **Exact device grade** (2등급 vs other) | Determines whether 인증, 허가 or exemption applies. | Query MFDS’s “의료기기 품목 및 품목별 등급에 관한 규정” database with product description; obtain a formal grade determination. |
| **Applicability of 면제·대체** under 제25조 | The excerpt flags the need for “조문 전문 확인”. Without confirming the specific conditions (e.g., AI module status, risk level), the exemption cannot be claimed. | Review the full text of **디지털의료제품법 시행규칙 (2026‑01‑23 개정) 제25조 각 호**; involve a legal counsel if interpretation is ambiguous. |
| **Whether the GUI SW falls under 디지털의료제품법 or 기존 의료기기법** | The source separates “P3 촬영실 GUI SW” from hardware items that remain under the Medical‑Device Act (§3·§4 매트릭스). Clarify which statutory regime fully governs the software. | Cross‑check product functions against the scope definitions in both the **디지털의료제품법** and **의료기기법**; confirm with MFDS or a regulatory consultant. |
| **QMS maturity level for 우수관리체계 특례** | The benefit is only granted if KGMP/ISO 13485 processes meet “우수” criteria. | Conduct an internal QMS audit; collect evidence of process metrics, continuous improvement records, and any previous MFDS inspections. |
| **AI module implementation timeline** | Future AI integration triggers new clinical‑trial obligations per the 2025 임상시험 가이드라인. Early planning is needed to avoid later project delays. | Draft a development roadmap that shows when (or if) AI will be added; align with the comparative‑design requirements now. |

---

### 4. Key Risk Controls & Post‑Market Surveillance

| Control | Description |
|--------|-------------|
| **Hazard Identification** (ISO 14971) – includes user error, misinterpretation of GUI data, and potential AI decision bias (once added). |
| **Design Verification / Validation** – unit tests, integration tests, usability testing with target operators (radiologists/technicians). |
| **Performance Monitoring** – real‑time logging of software events; periodic review of diagnostic concordance if AI support is deployed. |
| **Cybersecurity Management** – regular vulnerability scanning, secure update mechanism, and incident response plan per IEC 81001‑5‑1. |
| **Post‑Market Surveillance (시판후조사)** – collection of adverse event reports, field safety corrective actions (FSCA), annual summary submitted to MFDS. |
| **Training & User Instructions** – Korean language user manuals; on‑site training sessions; competency assessments for end users. |

---

### 5. Human‑Escalation Triggers  

| Trigger | Action Required | Responsible Party |
|---------|----------------|-------------------|
| **Unconfirmed device grade** | Pause submission preparation until official grade is obtained. | Regulatory affairs lead + MFDS liaison. |
| **Ambiguity in 제25조 적용** | Legal review of the 시행규칙 clause; decision on exemption vs full clinical data requirement. | In‑house counsel / external regulatory lawyer. |
| **QMS does not meet “우수관리체계” threshold** | Re‑evaluate benefit claim; consider proceeding without 특례 or improve QMS first. | Quality manager. |
| **AI module planned but timeline uncertain** | Update clinical‑trial design plan; possibly file a pre‑submission consultation with MFDS to clarify future data needs. | Clinical development lead. |
| **Cybersecurity audit flags critical vulnerability** | Immediate patch rollout and notification to MFDS under post‑market surveillance obligations. | IT security team + RA. |
| **Adverse event trend exceeding risk threshold** | Initiate field safety corrective action; prepare MFDS report within required timeframe. | Pharmacovigilance / PMS officer. |

---

### 6. Peer‑Review Prompt  

> *Please review the assumptions made in this draft, especially regarding (a) the classification of the P3 촬영실 GUI SW under the Digital‑Medical‑Product Law versus the traditional Medical‑Device Act, (b) the interpretation of 제25조 각 호 for exemption/alternative pathways, and (c) the completeness of the required evidence list given the optional future AI module. Highlight any jurisdiction‑specific gaps or additional documentation that may be needed before final submission.*

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
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. 등급 '2등급 또는 미지정 — 확인 필요' 헷징·제25조 [검증 필요] 유지·'디지털의료제품법 vs 의료기기법 어느 체계가 통치하는지 확인' gap 명시 — 관할 프레이밍 정확.

**Source Excerpts**

1. Chunk `1127968925422991528`

> ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향후 AI 모듈 추가 가능성 고려해 비교설계 원칙 사전 학습 권고. - 출처: 정책브리핑 2025-10-31(https://www.korea.kr/briefing/pressReleaseView.do?newsId=156724315) ---

2. Chunk `198902914416608487`

> - 영향 제품: **P3 촬영실 GUI SW**(디지털의료기기소프트웨어에 해당하는 경우). P1 X-ray Detector·P2 Handheld X-ray Source는 의료기기법 체계 적용으로 **직접 영향 없음**(§3·§4 매트릭스 유지). - 나항은 자사에 **유리한 완화**다. GUI SW가 2등급이든 등급 미지정이든 기능별 임상시험 자료의 **면제·대체 경로가 열린다**. 다만 면제·대체의 개별 요건(개정 제25조 각 호)은 조문 전문 확인이 필요하다 — `[검증 필요]`. - 가항은 요건의 삭제가 아니라 **근거 조문의 이동(고시 → 시행규칙)** 이다. 「디지털의료제품법 시행규칙」(2026-01-23 개정)의 해당 조문을 확인해야 실제 의무 범위를 알 수 있다 — `[검증 필요]`. - 다항의 우수관리체계 특례는 **QMS 성숙도를 인허가 편익으로 전환**하는 제도다. KGMP·ISO 13485 기반이 갖춰진 경우 중장기 활용 가치가 있다. **행동 (Action)**

### kb-eval-20261120-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "66d966b9d91ea269", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `66d966b9d91ea269`
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

> **Regulatory Draft – Imaging‑Room GUI Software (2등급)  
Prepared for MFDS (Korean) submission**

---

### 1. Device Overview (assumed)

| Item | Description |
|------|-------------|
| **Product name** | Imaging‑room graphical user interface (GUI) software, intended to control and display radiographic imaging equipment. |
| **Intended use** | Operates the acquisition, processing, and display of diagnostic images in a hospital radiology suite; includes optional AI‑based image enhancement functions. |
| **Technology class** | Stand‑alone medical device software (no accompanying hardware). |

> **Source evidence:** The source excerpt explicitly lists “촬영실 GUI SW (2등급)”【2】.

---

### 2. Korean Classification & Submission Route  

| Question | Answer | citation |
|----------|--------|----------|
| **Regulatory grade** | **2등급** (requires 인증) | 【2】 |
| **Primary submission track** | **인증** by an MFDS‑designated 심사기관 (e.g., KTL, KTC). The pathway may be supplemented with a “디지털의료제품법” combined review if the product is also considered a digital medical product. | 【2】 |
| **Alternative/optional track** | *병용 검토* under the Digital Medical Products Act – to be evaluated after preliminary 인증 eligibility check. | 【2】 |

> No specific 고시 번호 or 조항 was supplied in the source material; therefore no instance identifier is provided for the grade or pathway (‑ *no specific identifier found in source — verify separately*).

---

### 3. Required Technical Evidence  

| Category | Minimum items to be submitted | Regulatory basis / standard |
|----------|------------------------------|-----------------------------|
| **Technical Documentation (인증)** | • Device description, intended use, and functional specification.<br>• Software architecture & design description.<br>• IEC 62304‑based software life‑cycle documentation (development plan, verification/validation reports).<br>• Change‑management plan (especially for AI updates). | MFDS “인증” guideline – *no specific notice number in source*; IEC 62304 (software lifecycle)【2】 |
| **Risk Management** | • ISO 14971‑based risk management file (hazard identification, risk evaluation, mitigation measures, residual risk acceptance).<br>• Risk control matrix linking each identified hazard to a concrete control. | ISO 14971 (framework reference). |
| **Usability / Human Factors** | • IEC 62366‑1 usability engineering process report (use‑case analysis, formative & summative testing outcomes). | IEC 62366‑1 (framework reference). |
| **Cybersecurity** | • MFDS 사이버보안 가이드라인 compliance evidence (threat model, mitigation strategy, vulnerability management).<br>• If AI is employed: adherence to the “생성형 AI 가이드라인” and inclusion of a robust change‑management plan. | MFDS 사이버보안 가이드라인 (referenced in source)【2】 |
| **Clinical Evaluation** | • For 2등급 devices, Korean law typically *does not* require local clinical data unless the device claims new intended use or presents novel risk.<br>• If foreign Clinical Evaluation Report (CER) is used, confirm acceptance under latest MFDS notice on foreign clinical evidence (no identifier supplied). | MFDS “의료기기 허가·신고·심사 등에 관한 규정”. |
| **Labeling & IFU** | • Korean language labeling (product name, model, manufacturer, serial/lot numbers, intended use, contraindications, warnings).<br>• Instruction for Use (IFU) in Korean – must meet MFDS labeling requirements. | MFDS “의료기기 품목 및 품목별 등급에 관한 규정”. |
| **Manufacturing & QMS** | • KGMP certification of the manufacturing facility (or proof of compliance with 법률 제28조).<br>• Evidence of ISO 13485‑2016–aligned quality management system (optional, but strengthens the dossier). | KGMP (법률 제28조) – framework reference. |
| **Post‑Market Surveillance (시판후조사)** | • PMS plan outlining monitoring activities, adverse event reporting, and periodic safety update schedule. | MFDS 시판후조사 규정 (no specific identifier supplied). |

---

### 4. Missing / Unconfirmed Information  

| Item | Why needed & risk if absent |
|------|-----------------------------|
| **Exact intended‑use statement** (including any AI‑driven functions) | Determines grade, need for clinical data, and labeling content. |
| **Full software development lifecycle artifacts** (requirements traceability matrix, unit/integration test reports) | Required for IEC 62304 compliance; gaps will be flagged by the 심사기관. |
| **Detailed risk analysis results & residual risk justification** | Mandatory under ISO 14971; incomplete files lead to non‑acceptance. |
| **Cybersecurity threat model and mitigation details (especially for AI updates)** | MFDS cyber‑security guideline demands explicit controls; insufficient detail blocks certification. |
| **Korean language labeling/IFU drafts** | Korean language is a statutory requirement; English‑only drafts will be rejected. |
| **KGMP status of the software development/factory site** | KGMP certification is required for any device manufactured in Korea; absence stops the 인증 process. |
| **Decision on Digital Medical Products Act (디지털의료제품법) route** | If pursued, additional documentation (e.g., data‑privacy impact assessment) is needed; uncertainty delays submission. |
| **Evidence of foreign CER acceptance** (if any) | Must reference the specific MFDS notice that permits use of foreign clinical data; without it, a Korean clinical study may be required. |

> All above items are *currently absent* from the information set supplied.

---

### 5. Core Risk Controls (mapped to standards)

| Hazard / Failure Mode | Control(s) | Standard / Guideline |
|-----------------------|------------|----------------------|
| Software crash or unexpected shutdown during image acquisition | • Fault‑tolerant design, watchdog timer, safe‑state fallback.<br>• Rigorous unit & integration testing. | IEC 62304 |
| Incorrect image rendering (mis‑interpretation risk) | • Validation of display algorithms against reference datasets.<br>• Usability testing with radiologists (IEC 62366‑1). | IEC 62366‑1 |
| Unauthorized access / data breach | • Role‑based authentication, encryption of patient data in transit and at rest.<br>• Regular vulnerability scanning & patch management. | MFDS 사이버보안 가이드라인 |
| AI algorithm bias or unintended output | • Transparent model documentation, performance metrics across demographic groups.<br>• Change‑management plan for model updates (생성형 AI 가이드라인). | 생성형 AI 가이드라인; ISO 14971 (risk control) |
| Residual risk to patient safety | • Overall residual risk assessment and justification of acceptability in the risk management file. | ISO 14971 |

---

### 6. Human‑Escalation Triggers  

| Situation | Who must be alerted & why |
|-----------|--------------------------|
| **Incomplete Korean labeling/IFU** | Senior RA lead – labeling is a statutory blocker; cannot proceed to 인증 without it. |
| **KGMP certification not yet obtained or expired** | Manufacturing QMS manager & regulatory lead – KGMP is pre‑condition for submission. |
| **AI component validation plan insufficient (e.g., missing bias analysis)** | AI specialist + senior RA – MFDS may reject under the 생성형 AI 가이드라인; risk of major delay. |
| **Decision to pursue Digital Medical Products Act combined pathway** | Legal counsel & regulatory lead – additional privacy and data‑governance requirements apply. |
| **Unclear acceptance of foreign CER** (no notice identifier available) | Regulatory manager – must obtain MFDS clarification before finalizing clinical evidence package. |
| **Critical risk control gaps identified during internal audit** | QA/Compliance officer – required to remediate prior to submission; non‑compliance leads to rejection. |

---

### 7. Regulatory Judgment  

*Based on the source excerpts, the imaging‑room GUI software is classified as **2등급** and must follow the **인증** route, optionally supplemented by a Digital Medical Products Act combined review. The dossier must contain IEC 62304‑based lifecycle documents, ISO 14971 risk management evidence, usability engineering (IEC 62366‑1), cyber‑security compliance per MFDS guidelines, Korean language labeling/IFU, and proof of KGMP certification. Missing items listed above should be obtained before the submission package is assembled.*

**Key next steps**  

1. Collect all missing documents (intended use statement, full software development artifacts, risk analysis, cybersecurity threat model, Korean IFU, KGMP certificate).  
2. Confirm whether a foreign Clinical Evaluation Report will be used and request the exact MFDS notice that permits its acceptance.  
3. Decide on pursuing the 디지털의료제품법 combined pathway; if so, prepare the required privacy‑impact assessment.  

---

### 8. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions made about (i) the necessity of a Korean clinical evaluation for this 2등급 software, (ii) the applicability of the Digital Medical Products Act combined review, and (iii) any jurisdiction‑specific gaps that may have been overlooked (e.g., special labeling for AI‑enabled devices or additional post‑market surveillance obligations). Provide feedback on the completeness of evidence requirements and suggest any additional Korean regulatory citations that should be incorporated.

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

> 심각 결함 없음. 2등급→인증·디지털의료제품법 '병용 검토(optional supplement)' 프레이밍 정확(관할 이전 없음)·KGMP 제28조 정확.

**Source Excerpts**

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `39359892234270838`

> ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재검증 — 핵심 규제사실 반영 확인. · 상태: 승인 · 일자: 2026-06-09

### kb-eval-20261120-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "bb18b9ddd450dc1a", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `bb18b9ddd450dc1a`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EC%82%AC%EC%9D%B4%EB%B2%84%EB%B3%B4%EC%95%88_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_2025_%EB%8C%80%EC%9D%91.md)
- Source hash: `87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_사이버보안_가이드라인_2025_대응.md`는 `MFDS_사이버보안_가이드라인_2025_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 | ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개...
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

> **Regulatory Draft – Cyber‑security Compliance for a New Medical Device (MFDS KR) ⟶ Classification & Submission Pathway**

---

## 1. 판정 필요 사항  
| 항목 | 현황(출처) | 판단·추가 확인이 필요한 내용 |
|------|-----------|------------------------------|
| **법적 근거** | 「디지털의료제품법」(2025‑01‑24 시행)·의료기기법 시행규칙 (출처 [1]) | 해당 법령에 따른 사이버보안 요구사항 적용 여부 확인 |
| **가이드라인 명칭** | “의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서)” (개정일 2025‑01‑10) (출처 [1]) | 고시 번호(예: MFDS 고시 제XXXX‑XX호)는 문서에 명시되지 않음 → 별도 확인 필요 |
| **요구사항 수** | 기존 15→35항목 확대 (출처 [1]) | 세부 RA‑01~RA‑35 내용은 가이드라인 PDF에 포함 – 실제 적용 항목 검토 필요 |
| **주요 카테고리(8개)**<br>① 보안 설계 원칙<br>② 인증·접근 제어<br>③ 암호화<br>④ 소프트웨어 무결성<br>⑤ 네트워크 보안<br>⑥ 취약점 관리<br>Ⅶ 감사·로그<br>Ⅷ 업데이트·유지보수 (출처 [2]) | 35개 요구사항이 위 8가지 카테고리로 분류됨 | 각각의 세부 항목(RA‑01~RA‑35)과 해당 문서 페이지를 확인해 체크리스트 만들 필요 |
| **국제 표준 연계** | IMDRF N60/N73, IEC 81001‑5‑1 (출처 [1],[2]) | 국제표준 적용을 위한 내부 절차·증거 확보 필요 |

> **Note:** No specific MFDS 고시 번호 or article (§) is supplied in the source excerpts; therefore “no specific identifier found in source — verify separately” for those items.

---

## 2. 예상 등급 및 인허가 경로  

| 단계 | 판단 근거(법령) | 추정 등급 (1~4등급) | 적용 인허가 절차 |
|------|----------------|-------------------|-----------------|
| ① 제품 유형·위험 수준 파악 | 「의료기기 품목 및 품목별 등급에 관한 규정」 (§2) – **MFDS_인허가_상세가이드.md** 참고 | *미확정* (제품이 “소프트웨어형 의료기기”인지, “첨단치료제”, “일반‑의료기기”인지에 따라 다름) | 등급 확정 후 <br>• 1등급 → **신고**<br>• 2등급 → **인증** (MFDS‑지정 심사기관)<br>• 3·4등급 → **허가** |
| ② 사이버보안 요구사항 적용 여부 | 디지털의료제품법 및 가이드라인에 명시된 35개 항목 | 등급과 무관하게 모든 등급에 **사이버보안 검증서(보안 설계·시험 보고서)** 제출 필수 (MFDS 고시 제‑‑호, 추후 확인 필요) | 위 인허가 절차와 병행하여 사이버보안 평가자료 제출 |

> **Action:** 제품의 위험도 평가(ISO 14971) → 등급 산정 → 해당 인허가 트랙 선택.  

---

## 3. 요구되는 서류·증거 (전형적인 패키지)

| 구분 | 필요 서류/증거 | 근거 표준 / 규제 |
|------|----------------|------------------|
| **품질관리** | KGMP 인증서(의료기기법 제28조) <br>ISO 13485:2016 적합성 증빙 | KGMP, ISO 13485 |
| **위험 관리** | 위험 관리 파일(RMF) – ISO 14971:2019 적용 | ISO 14971 (2019) |
| **소프트웨어 생명주기** | IEC 62304(2006+A1:2015) 기반 개발·검증・검증 보고서 | IEC 62304 |
| **사이버보안** | • 보안 설계 원칙서 <br>• 인증·접근 제어 정책서 <br>• 암호화·키 관리 매뉴얼 <br>• 코드 서명·부트 무결성 검증 보고서 (SBOM 포함) <br>• 네트워크 방화벽·TLS 설정서 <br>• 취약점 관리 계획(CVE 모니터링, 패치 주기) <br>• 감사·로그 정책 및 샘플 로그 <br>• 업데이트·유지보수 절차 | IMDRF N60/N73, IEC 81001‑5‑1 (2021) |
| **임상·성능** | 필요 시, 한국 시장 전용 임상시험계획서(CTP) 및 결과보고서 <br>※ 2등급 이상·특정 고위험군에 한해 현지 임상자료 요구 가능 | 의료기기법 시행규칙 제23조 등 |
| **라벨·사용설명서** | 한국어 라벨·IFU (의료기기법 제30조) | MFDS 라벨링 규정 |
| **기술문서** | 기술 사양서, 설계 도면, 검증/확인 시험 성적서 등 | MFDS 인허가 가이드라인 |

---

## 4. 현재 확인 가능한 증거와 부족한 정보

| 항목 | 현황 (출처 기반) | 누락·보완 필요 |
|------|------------------|-----------------|
| **사이버보안 요구사항 상세** | 35개 요구사항이 8카테고리로 구분됨 (출처 [2]) | RA‑01~RA‑35 개별 내용, 적용 방안, 증거 형식(보고서·검증 결과) 확인 필요 |
| **법적 고시 번호** | 없음 (문서에 고시번호 미기재) | MFDS 고시 제XXX‑XX호(사이버보안 가이드라인) 여부 확인 → 정확한 고시 번호 확보 후 인용 |
| **제품 등급 판단 근거** | 출처에 등급 관련 내용 없음 | 제품 특성·위험도 분석 수행, 해당 규정 (§2) 검토 |
| **현지 임상 필요성** | 미확인 | 장치가 3·4등급이거나 고위험군이면 한국 임상자료 요구 여부 판단 |
| **KGMP 인증 현황** | 미제공 | 제조시설 KGMP 적합증명 확보 |
| **한국어 라벨/IFU** | 미제공 | 라벨·사용설명서 초안 준비 및 번역 검토 |

---

## 5. 위험 통제 방안 (사이버보안 중심)

1. **Secure‑by‑Design** – 설계 단계에서 위 “보안 설계 원칙” 적용, Threat Modeling 수행(ISO 14971 연계).  
2. **Access Control** – 역할 기반 접근(RBAC), 다중 인증(MFA) 구현; 세션 타임아웃 정책 수립.  
3. **Encryption** – AES‑256 이상 데이터 암호화 및 TLS 1.3 적용; 키 관리(KMS) 체계 문서화.  
4. **Software Integrity** – 디지털 서명, 부트 로더 무결성 검증, SBOM(소프트웨어 구성 목록) 관리.  
5. **Network Hardening** – 포트 최소화, 방화벽 정책, IDS/IPS 로그 수집.  
6. **Vulnerability Management** – CVE 모니터링 프로세스·정기 패치 일정 정의(CVD 정책).  
7. **Audit & Logging** – 보안 이벤트 로깅 표준(SYSLOG, ISO 27001 참고), 로그 무결성 보호(해시 체계).  
8. **Update Mechanism** – 인증된 OTA(Update‑Over‑The‑Air) 절차, 서명 검증 및 롤백 정책.

> 각 통제는 **위험 관리 파일(RMF)**에 기록하고, MFDS 심사 시 “보안 설계·검증 보고서” 형태로 제출한다.

---

## 6. 인허가 진행 흐름 (예시)

1. **제품 정의** → 위험도 평가(ISO 14971) → 등급 산정  
2. **필요 서류 준비** → KGMP, 기술문서, 사이버보안 패키지, 라벨·IFU  
3. **MFDS 사전 상담(선택사항)** – 고시 번호 및 사이버보안 요구사항 적용 확인  
4. **제출**  
   - 1등급 → 신고 (신고서 + 라벨·IFU)  
   - 2등급 → 인증 (심사기관 제출: 기술문서+KGMP+사이버보안 증거)  
   - 3·4등급 → 허가 (MFDS 직접 심사, 추가 임상자료 필요 시 포함)  
5. **심사 결과** → 보완 요구시(보완 요청서) → 최종 인허가·공고  

---

## 7. Human‑Escalation Triggers

| 상황 | 왜 사람 개입이 필요한가 |
|------|------------------------|
| **등급 미확정** | 위험도 평가 결과에 따라 인허가 경로가 달라짐 → 고위험 판단 시 즉시 임상·법무 검토 필요 |
| **고시 번호 부재** | 정확한 MFDS 고시(예: “MFDS 고시 제2025‑22호”)를 확인하지 않으면 제출 서류에 누락 위험 → 규제팀과 직접 문의 |
| **현지임상필요성 판단** | 3·4등급 혹은 특정 소프트웨어 의료기기에 대한 현지 임상 요구 여부가 애매함 → 임상시험 전문가와 협의 |
| **사이버보안 증거 부족** | RA‑01~RA‑35 상세 항목 중 아직 준비되지 않은 부분(예: 코드 서명 절차) → 보안 담당자와 조율 |
| **KGMP 인증 미취득** | 제조시설이 KGMP 기준을 충족하지 않음 → 품질팀에 설비·공정 개선 요구 |
| **라벨·IFU 번역/검증 지연** | 한국어 라벨·사용설명서가 최종 검수되지 않음 → 라벨링 담당자와 법무 부서의 최종 승인 필요 |

---  

## 8. Peer‑Review Prompt  
> **Please review:**  
> - Are the assumed 35 cyber‑security requirements (RA‑01~RA‑35) exhaustive for the device class we anticipate?  
> - Does the current source coverage adequately address any “local clinical data” obligations that might arise for a 3등급/4등급 product?  
> - Have we missed any jurisdiction‑specific gaps such as post‑market surveillance (시판후조사) reporting frequencies or mandatory cyber‑incident notification to MFDS?  

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
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. 등급 미확정 헷징·1/2/3·4등급→신고/인증/허가 정확·디지털의료제품법은 사이버 가이드라인 법적 근거로만 인용(소스 기반). 미세: 고시 번호 '제2025-22호'를 형식 예시로 사용(IEC 62304 편입 고시와 다른 문서에 예시 전용 — 확인 필요 프레이밍이라 감점 없음). [최종 2점 — shadow 9차 하향 수용: '등급과 무관하게 모든 등급에 사이버보안 검증서 제출 필수' — 소스는 가이드라인 존재와 35개 요건만 서술, '모든 등급 필수'는 소스 불일치 단정.]

**Source Excerpts**

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---

### kb-eval-20261120-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-20", "decision_ref": "kb-eval-20261120-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "64cdce791cf12cc1", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `64cdce791cf12cc1`
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

> **Regulatory Draft – Independent SaMD “촬영실 GUI SW”**

---

### 1. Korean Classification & Submission Route  
| Step | Required determination |
|------|------------------------|
| **Intended use & risk level** | Must be defined (e.g., image‑viewing, diagnostic support). The Korean grading (1~4등급) is assigned in accordance with 「의료기기 품목 및 품목별 등급에 관한 규정」.  <br> *No specific identifier found in source — verify separately.* |
| **Likely grade** | If the software performs only non‑clinical image display → probable **1등급** (신고).<br>If it provides diagnostic support or influences treatment decision → likely **2등급** (인증) or higher (**3등급·4등급**, 허가). |
| **Submission track** | 1등급 → 신고 (notification). <br>2등급 → 인증 (technical‑documentation review by MFDS‑designated 심사기관). <br>3·4등급 → 허가 (approval by MFDS). |

*Action:* Confirm grade with the Korean grading table before finalizing the pathway.

---

### 2. Required Evidence & Documentation  

| Requirement | Source / Framework | Notes |
|-------------|-------------------|-------|
| **QMS compliance** | KGMP (의료기기법 제28조) + ISO 13485:2016 | ISO 13485 alone is insufficient; ARR activities must be integrated (see FDA §820.10(b) in source [1]). |
| **Applicable Regulatory Requirements (ARR)** | FDA 21 CFR §§820.10(b), 820.35(a) – cited in source [1] | MFDS expects similar ARR integration (UDI, MDR‑type reporting, corrections & removals). |
| **Software Development Lifecycle** | IEC 62304:2006+A1:2015 – Safety Class C (source [2]) | All design history files (SDP, SRS, SAD, SVP, SVR) required. |
| **Risk Management** | ISO 14971:2019 | Must address device‑specific hazards; align with IEC 62304 risk analysis. |
| **Software Validation & Verification** | IEC 62304 §8.1 (source [2]) | Include regression test automation, change‑control SOPs. |
| **Cybersecurity** | MFDS 사이버보안 가이드라인 2025 (no specific 번호 in source – verify separately) ; FDA 524B PCCP; MDCG 2019‑16 Rev.1 (source [2]) | Threat model, SBOM, PCCP integration required. |
| **Clinical Evaluation** *(if grade ≥2등급)* | MFDS “foreign CER acceptance” notice (specific 번호 not in source – verify separately) | Local clinical data may be needed unless exemption applies. |
| **Labeling & IFU** | Korean language labeling requirement (MFDS 고시) – no identifier supplied in source. |
| **UDI Assignment** | 21 CFR §830 (ARR reference in source [1]) – MFDS expects UDI per “의료기기 식별·추적 관리법”. |
| **Post‑Market Surveillance (PMS)** | MFDS 시판후조사 규정 – complaint handling per FDA §820.35(a) (source [1]). |
| **Contract Sterilizer / Re‑labeler inclusion** | FDA §820.10(a) – expanded QMSR scope (source [1]) – ensure any outsourced sterilization/re‑labeling is covered in KGMP QMS. |

---

### 3. Missing Information (Need to Obtain)

| Item | Why needed |
|------|------------|
| **Exact intended use & risk claim** | Determines Korean grade and need for clinical evidence. |
| **Device name / model number** | Required for MFDS registration dossier. |
| **Clinical performance data** (if 2등급 이상) | To satisfy Korean clinical evaluation requirement. |
| **Korean‑language IFU & labeling assets** | Mandatory for market entry. |
| **UDI issuance plan** | Aligns with ARR and Korean traceability law. |
| **Evidence of KGMP certification** | Must be in place before filing 인증/허가. |
| **Confirmation of foreign evidence acceptance** (e.g., FDA 510(k) or CE mark) | MFDS may accept under specific notices; exact notice number not present in source. |

---

### 4. Core Risk Controls (Mapped to Standards)

| Control | Standard / Reference | Implementation focus |
|---------|----------------------|-----------------------|
| **Software safety class C controls** | IEC 62304 Class C (source [2]) | Fail‑safe design, watchdog timers, redundancy where required. |
| **Risk management process** | ISO 14971:2019 | Hazard identification, risk evaluation, mitigation, residual risk acceptance. |
| **Secure coding & vulnerability management** | MFDS Cybersecurity Guideline 2025; FDA 524B PCCP (source [2]) | Threat modeling, SBOM, regular pentests, incident response SOP. |
| **Change control & versioning** | IEC 62304 §8.1; KGMP QMS | Documented change impact analysis and validation for each release. |
| **Usability/ Human‑machine interface (HMI) validation** | IEC 62366‑1:2015 – not in source but required for SaMD. |
| **Complaint handling & MDR‑type reporting** | FDA §820.35(a) (source [1]) | Record whether complaint is reportable under Korean equivalent of MDR. |

---

### 5. Citations  

| Item | Citation type | Reference |
|------|----------------|-----------|
| ARR integration requirement | Instance identifier | FDA 21 CFR §§820.10(b), 820.35(a) – source [1] |
| Complaint file detail (MDR‑reportable) | Instance identifier | FDA 21 CFR §820.35(a) – source [1] |
| Service record requirement | Instance identifier | FDA 21 CFR §820.35 – source [1] |
| Contract sterilizer inclusion in QMS | Instance identifier | FDA 21 CFR §820.10(a) – source [1] |
| Software lifecycle mapping (IEC 62304 Class C) | Framework reference | IEC 62304:2006+A1:2015 – source [2] |
| SW validation clause | Framework reference | IEC 62304 §8.1 – source [2] |
| Cybersecurity guidance | Framework reference (no specific Korean notice number) | MFDS 사이버보안 가이드라인 2025 – source [2]; FDA 524B PCCP; MDCG 2019‑16 Rev.1 – source [2] |
| AI/ML regulatory cross‑reference | Framework reference | EU AI Act Reg. 2024/1689 (future) – source [2] |

*Note:* Where a specific Korean notice number or article is required but not supplied in the excerpts, the draft flags “verify separately”.

---

### 6. Human‑Escalation Triggers  

| Trigger condition | Reason for escalation |
|-------------------|-----------------------|
| **Uncertain Korean grade** (insufficient intended‑use detail) | Grade determines submission route; requires senior RA sign‑off before dossier preparation. |
| **Missing local clinical data** for a device projected as 2등급 이상 | May cause rejection at MFDS 심사기관; needs clinical affairs input. |
| **KGMP certification not yet obtained** | Certification is prerequisite for 인증/허가; escalation to quality / manufacturing leadership. |
| **Foreign evidence acceptance unclear** (e.g., CE mark, FDA 510(k) used as predicate) | Must verify applicable MFDS notice; involve regulatory affairs manager. |
| **Cybersecurity plan not aligned with MFDS 가이드라인 2025** | Potential post‑market compliance breach; counsel security team and senior RA. |
| **Labeling/IFU missing Korean translation** | Regulatory non‑conformity; escalation to translation / medical writing lead. |

When any trigger fires, the responsible RA should log a “Regulatory Review – Escalation Required” task in the project management system and notify the senior regulatory manager.

---

### 7. Peer Review Prompt  

> **To a fellow RA:** Please review the assumptions above regarding the likely Korean grade of this independent SaMD, the sufficiency of the listed foreign evidence (e.g., FDA 510(k) or CE mark) for MFDS acceptance, and any gaps in the mapping between IEC 62304 safety class C requirements and MFDS post‑market surveillance obligations. Highlight any additional Korean regulations not covered here that could affect the submission route.

---

### 8. Reusable RA Judgment (recorded)

```json
{
  "honcho_conclude": {
    "topic": "Independent SaMD (촬영실 GUI SW) – Korean classification & submission",
    "judgment": {
      "grade_determination_needed": true,
      "submission_route_options": ["신고 (1등급)", "인증 (2등급)", "허가 (3~4등급)"],
      "required_evidence": [
        "KGMP certification",
        "ISO 13485:2016 QMS",
        "IEC 62304 Class C documentation",
        "ISO 14971 risk management file",
        "Cybersecurity plan per MFDS 가이드라인 2025",
        "Clinical evaluation (if ≥2등급)",
        "Korean language labeling/IFU",
        "UDI issuance evidence"
      ],
      "missing_information": [
        "Exact intended use & risk claim",
        "Clinical performance data",
        "Confirmation of foreign evidence acceptance notice number"
      ]
    },
    "escalation_triggers": [
      "grade_uncertain",
      "clinical_evidence_missing",
      "kgmp_not_certified",
      "foreign_evidence_acceptance_undefined",
      "cybersecurity_noncompliant",
      "korean_labeling_absent"
    ],
    "peer_review_prompt": "Please challenge the grade assumption, foreign evidence mapping, and any overlooked Korean post‑market obligations."
  }
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
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> '의료기기 식별·추적 관리법'을 UDI 근거 법령으로 제시 — 비존재 법령명 후보(한국 UDI는 의료기기법 체계, 해당 법명은 KB 전체에 없음). 등급 조건부 헷징·PCCP 오확장 소멸·제28조 정확.

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...
