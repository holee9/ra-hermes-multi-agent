# KB Eval Checksheet - 2026-10-19 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261019-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "c92d5f3a1f54e5db", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c92d5f3a1f54e5db`
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

> **Regulatory Draft – 510(k) Predicate Strategy**  

---

### 1. Bottom‑Line Regulatory Pathway  
- **Submission route:** Premarket Notification (510 (k)) under **21 CFR §807**.  
- **Device class:** Probable Class II (most imaging/diagnostic software and accessories fall under **21 CFR Part 892**, e.g., §892.2050 for image‑processing systems). *Class to be confirmed once device function is defined.*  

---

### 2. Core Submission Elements (derived from the source workflow)  

| Section | Required Evidence / Documentation | Status / Gaps |
|---|---|---|
| **Device Description & Indications for Use (IFU)** | • Narrative description of hardware, software, accessories.<br>• Intended use statement matching predicate. <br>*Source:* eSTAR 01_Device_Description_IFU guide. | *Missing*: Finalized device description and IFU wording. |
| **Predicate Device Identification** | • Search FDA 510(k) database for a cleared device with same intended use & technology.<br>• Record K-number, registration number, classification. | *Missing*: Specific predicate(s) – no identifier found in source — verify separately. |
| **Substantial‑Equivalence Comparison Table** | • Side‑by‑side matrix of each characteristic (technology, indications, performance, labeling). | *Missing*: Completed comparison table – requires selected predicate. |
| **510(k) Summary** | • Concise summary per 21 CFR §807.92 (device description, intended use, technological characteristics, performance testing). | *Missing*: Draft summary. |
| **Performance Testing** | • Bench / benchtop functional tests demonstrating equivalence.<br>• Usability/ human factors if UI is involved.<br>*Relevant standards:* IEC 62304 (software life‑cycle), IEC 60601‑1‑2 (EMC) – use current editions. | *Missing*: Test protocols & data. |
| **Biocompatibility** | • ISO 14971:2019 risk management file → biocompatibility assessment per ISO 10993‑1:2018. | *Missing*: Risk analysis & material testing results. |
| **Electromagnetic Compatibility (EMC)** | • IEC 60601‑1‑2 compliance data. | *Missing*: EMC test reports. |
| **Labeling** | • 21 CFR §801 labeling requirements; include UDI per **21 CFR §830**. | *Missing*: Final label artwork and UDI assignment plan. |
| **Quality Management System (QMS)** | • Conformance to QMSR (21 CFR Part 820) aligned with ISO 13485:2016; evidence of design controls (§820.30). | *Missing*: Updated SOPs, including any `SOP-RA-002` or `SOP-PMA-001` that pertain to this device. |
| **UDI Implementation** | • Assign a Device Identifier (DI) and Production Identifier (PI); submit to GUDID per 21 CFR §830.300‑§830.360. | *Missing*: UDI strategy – no specific identifier found in source — verify separately. |

---

### 3. Risk Controls & Engineering Strategies  

| Control Area | Standard / Regulation | Application |
|---|---|---|
| **Risk Management** | ISO 14971:2019 (Amd 1:2024) | Identify hazards, evaluate severity/occurrence, implement mitigations; integrate into design history file. |
| **Software Development** | IEC 62304 2006+A1:2015 | Define software life‑cycle processes, verification & validation, maintain traceability to risk controls. |
| **Usability / Human Factors** | IEC 62366‑1 2015+A1:2020 | Conduct formative and summative usability testing; include HF report in submission. |
| **Design Controls** | 21 CFR §820.30 | Document design inputs/outputs, verification, validation, change control (see PCCP below). |
| **Predetermined Change Control Plan (PCCP)** | FDA Guidance (Dec 2024) | If the device incorporates AI/ML, develop a PCCP to pre‑authorize future algorithm updates. |

---

### 4. Key Citations  

- **Framework references (no verification caveat needed):**  
  - 21 CFR §807 – Premarket Notification (510(k)).  
  - 21 CFR Part 820 – Quality System Regulation (effective Feb 2026).  
  - 21 CFR Part 830 – Unique Device Identification.  
  - 21 CFR Part 892 – Imaging devices (e.g., §892.2050 for image‑processing software).  
  - ISO 14971:2019, ISO 13485:2016, IEC 62304 2006+A1:2015, IEC 60601‑1‑2 (current edition).  

- **Instance identifiers:** *No specific identifier found in source — verify separately.*  

---

### 5. Human‑Escalation Triggers  

| Trigger | Action & Responsible Party |
|---|---|
| **No suitable predicate identified** after exhaustive search | Escalate to Senior Regulatory Manager → evaluate De Novo or PMA pathway. |
| **FDA Additional Information (AI) request exceeds 180 days** to respond | Notify Lead RA; obtain management sign‑off on response plan; consider filing a Request for Extension if justified. |
| **Classification ambiguity (e.g., device could be Class I vs. II)** | Convene cross‑functional classification review with Regulatory, Clinical, and QA leads; document decision per 21 CFR §807.92(b). |
| **Significant gaps in risk management or testing data** that preclude substantial equivalence | Pause submission preparation; engage engineering for remedial studies before proceeding. |
| **UDI allocation conflicts or GUDID entry errors** | Raise to QMS/Labeling Lead; correct and re‑submit within 30 days of FDA notice. |

---

### 6. Reusable RA Judgment (Memory Record)  

- Follow the eSTAR‐based workflow: predicate search → SE table → compile required 510(k) sections (Device Description/IFU, Summary, performance, biocompatibility, EMC, labeling, QMS evidence).  
- Use current editions of ISO/IEC standards listed above; do not assume newer editions exist.  
- Apply the Predetermined Change Control Plan only for AI/ML‑based devices; do **not** mix with discontinuated “Pre‑Cert” terminology.  
- If a predicate cannot be located, shift to De Novo evaluation rather than forcing a 510(k).  

---

### 7. Peer Review Prompt  

*Please review the assumptions above: (1) classification as Class II under Part 892, (2) completeness of required evidence list given the limited source detail, and (3) any jurisdiction‑specific gaps such as EU/MDR concepts inadvertently carried over.*  



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

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20261019-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "3bdc02f0cf850ee6", "source": "github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md", "source_hash": "fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `3bdc02f0cf850ee6`
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

> **Regulatory Draft – 510(k) Predicate Strategy for an X‑ray Imaging Device**

---

### 1. Device Classification & Submission Pathway
| Item | Determination |
|------|----------------|
| **Product family** | X‑ray imaging system (radiology device). |
| **CFR Panel** | **21 CFR Part 892 – Radiology / Imaging Devices** (see Part map). |
| **Regulatory Class** | Likely **Class II** (most diagnostic X‑ray systems are classified as II under §892.1800‑§892.1850; the exact section must be confirmed against the FDA product classification database). |
| **Submission route** | **510(k) Premarket Notification** – Traditional pathway is recommended when a legally marketed predicate with identical intended use and sufficiently similar technology exists. An **Abbreviated** 510(k) could be considered if recognized guidance or special controls are applicable, but no such guidance is cited in the source. |
| **Alternative** | If no suitable predicate is identified, the device would fall into **Not Substantially Equivalent (NSE)** and require a **De Novo classification request** (or PMA for high‑risk). |

### 2. Predicate Selection & SE 5‑Step Decision Logic (per FDA 2014 Guidance – Appendix A)
| Step | Question | Source logic (Excerpt [2]) | Outcome Required |
|------|----------|----------------------------|------------------|
| DP1 | Is the predicate a **legally marketed device**? | “No → NSE (De Novo or PMA)” | Identify a cleared 510(k) (e.g., K#######). |
| DP2 | Does it have the **same intended use**? | “No → NSE” | Align intended‑use statements. |
| DP3 | Are the **technological characteristics** identical? | “Yes → DP5; No → DP4” | Detail hardware, emissions, detector tech, software features. |
| DP4 | Do any differences raise new **questions of safety & effectiveness**? | “Yes → NSE” | Conduct additional bench/clinical testing to address gaps. |
| DP5 | Does the **performance data** demonstrate at least equivalent safety/effectiveness? | “Yes → SE (Clearance possible)” | Provide comparative performance results. |

*The decision tree must be documented in the 510(k) narrative.*

### 3. Required Evidence Package
| Category | Required Elements (framework references) |
|----------|-------------------------------------------|
| **Predicate Identification** | Predicate 510(k) number, registration status (21 CFR 807). |
| **Intended Use Comparison** | Side‑by‑side table of indications, patient population, anatomical site. |
| **Technological Characteristics** | Detailed specs (X‑ray tube voltage, filtration, detector type, software algorithms). |
| **Performance Data** | • Bench tests: output consistency, dose measurements, image quality metrics (e.g., modulation transfer function, contrast‑to‑noise ratio).<br>• Non‑clinical testing per IEC 60601‑1 and IEC 62304 (if software).<br>• Clinical data (if needed) demonstrating non‑inferiority to predicate. |
| **Risk Management** | ISO 14971:2019 risk analysis file; hazard list, severity/occurrence assessments, control measures, residual risk justification. |
| **Software Validation** *(if applicable)* | IEC 62304:2006+A1:2015 lifecycle processes; verification and validation reports for each software unit. |
| **Labeling & IFU** | 21 CFR 801 labeling requirements; FDA‑approved Summary of Safety and Effectiveness (SSED). |
| **UDI Assignment** | 21 CFR 830 – UDI labeling, issuance of a device identifier in the GUDID. |
| **QMS Compliance** | Conformance to **21 CFR 820** (QMSR effective Feb 2026) aligned with ISO 13485:2016; SOPs for design control, CAPA, etc. |
| **Sterilization / Biocompatibility** *(if applicable)* | ISO 10993‑1:2018 biological evaluation report; sterilization validation per FDA guidance (e.g., 21 CFR 820.75). |

### 4. Missing Information & Gaps (to be supplied before submission)
| Gap | Why it matters |
|-----|----------------|
| Exact **device description** (model, accessories, software version). | Needed for predicate matching and technological comparison. |
| **Predicate 510(k) number(s)** and confirmation that they are “legally marketed.” | Drives DP1 outcome; absence forces NSE pathway. |
| Formal **Intended Use statement** (including claim language). | Determines DP2; misalignment triggers NSE. |
| Detailed **technological differences** (if any) with justification of safety/effectiveness equivalence. | Required for DP3/DP4 analysis. |
| Complete **performance test plan & results** (bench, animal, clinical). | Basis for DP5. |
| Full **Risk Management File** (ISO 14971) and **Design History File** linkage to 21 CFR 820. | Mandatory for 510(k) technical sections (§807.92(f)). |
| **UDI issuance plan** (label format, packaging, GUDID record). | FDA requires UDI on label per Part 830. |
| Confirmation of **class designation** in the FDA Product Classification database (exact §892 subsection). | Ensures correct regulatory controls and special controls citation. |

### 5. Core Risk Controls (per ISO 14971 hierarchy)
1. **Inherent Safety Design** – Use proven X‑ray tube technology, limit beam filtration to reduce dose.
2. **Protective Measures** – Interlocks, automatic exposure termination, shielding on hardware.
3. **Administrative Controls** – Training requirements for operators; warnings in labeling.
4. **Monitoring & Alarms** – Real‑time dose monitoring, error detection software.
5. **Post‑Market Surveillance** – FDA 21 CFR 803 (MDR) and 21 CFR 806 (corrections/removals) plan.

### 6. Human‑Escalation Triggers
| Trigger | Action |
|---------|--------|
| No legally marketed predicate identified or predicate clearance status uncertain. | **Escalate to senior RA** for De Novo feasibility assessment. |
| Intended use differs from all known predicates. | **Escalate** – consider additional clinical data or De Novo path. |
| Technological differences raise new safety questions (DP4 “Yes”). | **Escalate** – develop supplemental bench/clinical studies; inform project lead. |
| Performance data does not meet equivalence criteria (DP5 “No”). | **Escalate** – redesign, additional testing, or alternative predicate search. |
| Incomplete risk management documentation. | **Escalate** – engage risk management team to finalize ISO 14971 file before submission. |
| Unresolved UDI/Labeling compliance gaps. | **Escalate** – coordinate with labeling & regulatory affairs for Part 830 remediation. |

### 7. Citations
- **Classification panel:** 21 CFR Part 892 (Radiology / Imaging Devices).  
- **510(k) decision flow:** FDA Guidance “Deciding When to Submit a Traditional, Abbreviated, or Special 510(k)” – Appendix A (excerpt [2]).  
- **Evaluation criteria for the assignment:** Table in excerpt [1] (no specific regulation numbers provided).  
- **QMSR reference:** 21 CFR 820 (effective Feb 2026, ISO 13485:2016‑aligned).  
- **UDI requirements:** 21 CFR 830 (general provisions §830.3 onward).  
- **Risk management standard:** ISO 14971:2019.  
- **Software lifecycle:** IEC 62304:2006+A1:2015.  
- **Biocompatibility:** ISO 10993‑1:2018.  

*No specific 510(k) numbers, CFR section citations beyond framework references, or device‑specific identifiers were present in the source excerpts; these will need verification.*

---

### 8. Peer Review Prompt
> **@RA‑Peer:** Please review the assumptions above—particularly the classification under §892 (exact subsection), the completeness of the predicate search criteria, and any omitted EU/Korean regulatory considerations that may affect our internal training material. Identify any gaps in source coverage or jurisdictional nuances that could alter the recommended submission pathway.

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

1. Chunk `1061195424067242245`

> ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과제 3-2 SE 비교표 제출 필수 ---

2. Chunk `1072507187378217632`

> ### 4.1 SE 5단계 Decision Point (FDA 2014 Guidance Appendix A) ``` DP1. Predicate이 Legally Marketed Device인가? │ No → NSE (De Novo 또는 PMA) │ Yes ↓ DP2. 동일한 Intended Use인가? │ No → NSE │ Yes ↓ DP3. 동일한 Technological Characteristics인가? │ Yes → DP5 │ No ↓ DP4. 다른 기술특성이 Different Questions of Safety & Effectiveness를 제기하는가? │ Yes → NSE │ No ↓ DP5. 성능 데이터가 새 장치 ≥ Predicate 수준임을 입증하는가? │ Yes → SE (Clearance 가능) │ No → NSE ```

### kb-eval-20261019-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "201a1be42171ec75", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `201a1be42171ec75`
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

> **Regulatory Draft – 510(k) Predicate Strategy & Evidence Gap Analysis**

---

### Bottom‑Line Recommendation  
- **Primary pathway:** Pursue a **510(k) Premarket Notification** if a suitable predicate device can be identified that demonstrates *substantial equivalence* for the intended use and technology.  
- **Escalation to De Novo:** If no appropriate predicate exists but the device is Class I/II (new technology, novel indication), submit a **De Novo classification request**.  
- **Escalation to PMA:** If the device will be classified as Class III (e.g., invasive, life‑supporting) or requires mandatory clinical data, prepare a **PMA**.

---

## 1. Classification / Submission Route

| Decision Factor | 510(k) | De Novo | PMA |
|-----------------|--------|---------|-----|
| **Legal basis** | FD&C Act §510(k), **21 CFR §807** | FD&C Act §513(f)(2), **21 CFR §860** | FD&C Act §515, **21 CFR §814** |
| **Target class** | Class I & II (standard) – some III | New Class I/II devices | Class III |
| **Predicate required?** | **Yes** | No | No |
| **Clinical data required?** | Conditional (see §3 of source) | “If applicable” | **Mandatory** |
| **Typical review time** | 90 days target | ~150 days | ~180 days target |

> *Source excerpt [2] provides the above table; no clause numbers are cited in the source, therefore “no specific identifier found in source — verify separately.”*

---

## 2. Required Evidence (per pathway)

### 2.1 510(k) – Substantial Equivalence Package  
| Component | Content | Regulatory reference |
|-----------|---------|----------------------|
| Device description & specifications | Materials, dimensions, operating principles, accessories | **21 CFR §807.92** (general) |
| Predicate device(s) | 510(k) number(s), comparison matrix (technology, intended use, performance) | **21 CFR §807.95** |
| Labeling & Instructions for Use | Indications, contraindications, warnings, US labeling format | **21 CFR §801** |
| Risk Management File | ISO 14971:2019 risk analysis, mitigations, residual risk evaluation | Framework reference – ISO 14971 |
| Software Documentation (if applicable) | IEC 62304:2006+A1:2015 software lifecycle plan; Verification & Validation reports | Framework reference – IEC 62304 |
| UDI compliance | Device label & packaging bear a UDI; GUDID submission per **21 CFR §830.10‑§830.36** | No specific identifier in source |
| QMS evidence (post‑Feb 2026) | Conformance to **21 CFR Part 820** (QMSR, ISO 13485‑aligned) – Design History File, CAPA records | Framework reference – Part 820 |
| Clinical data (if required) | Limited clinical or performance testing per FDA’s “conditional” requirement in §3 of the source guidance | No specific identifier found in source — verify separately |

### 2.2 De Novo Submission  
- Same documentation as 510(k) **except** predicate section is omitted.
- Provide **novelty justification**, risk classification rationale, and any applicable **clinical data** (“if applicable” per source).  

### 2.3 PMA – Full Premarket Approval Package  
- Includes all items above **plus**:
  - Comprehensive **clinical trial design & results** (mandatory).
  - Detailed **manufacturing process validation**.
  - **Environmental impact / biocompatibility** data per ISO 10993‑1:2018.

---

## 3. Missing Information / Evidence Gaps  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Intended use statement** | Determines classification & predicate relevance. | Draft precise indication, target population, and use environment. |
| **Predicate identification** | Required for 510(k); must be FDA‑cleared (or exempt). | Conduct database search (FDA 510(k) Premarket Notification Database) for devices with same technology/function. |
| **Risk Management Plan depth** | Must meet ISO 14971:2019; risk controls drive clinical need. | Populate a risk register, identify mitigations, perform residual risk evaluation. |
| **Software change‑control strategy (if AI/ML)** | FDA requires a **Predetermined Change Control Plan (PCCP)** for post‑market modifications. | Draft PCCP covering algorithm updates, performance monitoring. |
| **UDI labeling & GUDID submission** | Mandatory under Part 830; non‑compliance blocks clearance. | Prepare label artwork with UDI; complete GUDID entry. |
| **QMSR compliance evidence** | New QMS Regulation (effective 2026‑02) supersedes prior ISO 13485 references. | Map existing QMS to Part 820 requirements, prepare audit reports. |
| **Clinical data applicability** | Source indicates “conditional” clinical data for 510(k). | Determine if bench/animal testing suffices; otherwise plan limited clinical study. |
| **Device classification (specific CFR Section)** | Imaging devices fall under **21 CFR Part 892**, e.g., §892.2050 for image‑processing software. | Verify device function and assign correct Part 892 subsection (needs confirmation). |

---

## 4. Core Risk Controls (to be documented)

1. **Risk Management Process** – ISO 14971:2019 workflow (hazard identification → risk estimation → control implementation → residual risk evaluation).
2. **Design Controls** – 21 CFR §820.30 (design planning, inputs, outputs, review, verification, validation).  
3. **Software Lifecycle** – IEC 62304 compliance; include unit, integration, system testing and security verification.  
4. **Electrical Safety/EMC** – IEC 60601‑1:2005+A1:2012+A2:2020 (if applicable).  
5. **Usability/Human Factors** – IEC 62366‑1:2015+A1:2020 risk control for user interface.  
6. **Biocompatibility & Sterility** – ISO 10993‑1:2018 testing per intended contact duration.  

All controls must be cross‑referenced to the risk management file and incorporated into the Design History File (DHF).

---

## 5. citations

| Item | Citation Type |
|------|---------------|
| Legal bases for each pathway & classification table | **Framework reference** – FD&C Act §§ 510(k), 513(f)(2), 515; **21 CFR §807**, §860, §814 (no specific identifier in source) |
| Clinical‑data requirement conditionality | No specific identifier found in source — verify separately |
| eSTAR obligations & user‑fee amounts | No specific identifier found in source — verify separately |

---

## 6. Human‑Escalation Triggers  

- **No viable predicate** after exhaustive search → elevate to De Novo decision gate.  
- **Unclear clinical data necessity** (source only states “conditional”) → request FDA pre‑submission (Q‑Submission) for clarification.  
- **Device classified as Class III** by internal risk assessment → route to PMA project team.  
- **Incomplete QMSR evidence** or failure of ISO 14971 risk file audit → pause submission and engage quality assurance lead.  
- **UDI/GUDID non‑compliance** discovered during labeling review → stop clearance filing; involve regulatory affairs & packaging engineering.  
- **Predetermined Change Control Plan (PCCP) required for AI/ML** but not prepared → refer to software governance board before filing.

---

## 7. Peer Review Prompt  

*“@RA‑Peer, please challenge the assumptions made herein regarding predicate availability, the interpretation of ‘conditional’ clinical data requirements for a 510(k), and any jurisdiction‑specific gaps (e.g., imaging device classification under Part 892). Are there additional FDA guidance documents or recent MDEs we should incorporate before finalizing the submission strategy?”*

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

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20261019-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "37f03a6593c2c744", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `37f03a6593c2c744`
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

---

### 1. Device Classification & Submission Route
| Item | Determination |
|------|----------------|
| **Device Function** | Medical image management and processing system (Imaging Workstation GUI) |
| **Regulatory Panel** | **21 CFR Part 892** (Radiology/Imaging devices) |
| **Class** | Class II – classified under **§892.2050** (Medical image management and processing system) |
| **Submission Type** | Traditional 510(k) (Premarket Notification) – **no De Novo** needed because a cleared predicate exists in the same product‑code class. |

*Framework reference: 21 CFR §892.2050 (no identifier required).*

---

### 2. Predicate Selection – Evidence Required  
*(Checklist drawn from Source [1])*

| Requirement | What to Provide | Status |
|-------------|----------------|--------|
| **Product‑code search** in FDA 510(k) database | List of candidate predicates with product code(s) and clearance dates | – |
| **Recency** – Prefer ≤5 yr clearance; older (≥7 yr) need “additional strengthening” | Documented justification for using an older predicate (e.g., unchanged technology, continued market presence) | – |
| **Market status** – Predicate still sold? (not retired/discontinued) | Confirmation from manufacturer or FDA database that the predicate is commercially available | – |
| **Recall / Safety Communication check** | Verify no recent recall/MAUDE safety events for the predicate | – |
| **Indications for Use (IFU) comparison** – Exact wording match or narrower scope | Side‑by‑side table of IFU language; note any differences and provide justification | – |
| **Technical differences inventory** | Itemised list of hardware/software features that differ from the predicate, with supporting data (bench, user testing, literature) | – |
| **Split predicates prohibited** – Use a single primary predicate for IFU equivalence | Identify one primary predicate; ensure all claim elements are covered by it | – |

*Citation: Source [1] – “Predicate 선정 실무 체크리스트”. No specific device numbers were supplied in the excerpt (no identifier found – verify separately).*

---

### 3. Core Submission Content (Required Evidence)

| Section | Required Documents / Data | Regulatory Basis |
|---------|---------------------------|-------------------|
| **Device Description & Intended Use** | Full description, labeling draft, IFU, and intended‑use statement identical to or narrower than predicate | 21 CFR §807.92; Part 801 labeling |
| **Risk Management File** | ISO 14971:2019 risk analysis, risk control measures, post‑market surveillance plan | Framework reference – ISO 14971:2019 (no identifier needed) |
| **Software Documentation** | • IEC 62304:2006+A1:2015 software lifecycle plan <br>• Level of documentation per FDA 2023 Software Guidance (Basic vs. Enhanced) <br>• Verification & validation protocol/results (unit, integration, system testing) | 21 CFR §820.30; IEC 62304 |
| **Software Safety Class** | Assigned class (A/B/C) with justification (e.g., “Class B – non‑life‑supporting image processing”) | IEC 62304 |
| **Cybersecurity Controls** | Threat model, security architecture, authentication, encryption, audit logging, update mechanism, FDA Cybersecurity Guidance 2022 compliance | 21 CFR §§820.30/820.70; FDA Cybersecurity Guidance |
| **DICOM Conformance Statement** | Statement covering SCU/SCP, Worklist, MPPS, Print SCU etc., with test evidence of interoperability | Source [2] – “DICOM 적합성 진술서” |
| **Interoperability Claims** | HL7‑FHIR/IHE profile support documentation, mapping tables | Source [2] |
| **Software Bill of Materials (SBOM)** | SBOM in SPDX or CycloneDX format; generation methodology | Source [2] – “SBOM 제공 형식” |
| **AI/ML Component (if applicable)** | Predetermined Change Control Plan (PCCP) detailing change‑control strategy, algorithm versioning, performance monitoring | FDA Guidance Dec 2024 “Predetermined Change Control Plan (PCCP)” |
| **Quality System Evidence** | ISO 13485:2016–aligned QMS per new **QMSR (Part 820)** effective Feb 2026; device master record, design history file, CAPA records | 21 CFR Part 820; QMSR |
| **UDI Assignment** | UDI label & packaging format complying with §830.10‑§830.60; registration in GUDID | 21 CFR Part 830 |
| **Labeling (including IFU)** | Full labeling set, user manual, safety warnings, intended‑use statement | 21 CFR Part 801 |

*Citation: Source [2] – “4.3 촬영실 GUI SW (Imaging Workstation SW)” provides the detailed software items; no device‑specific identifiers appear (no identifier found – verify separately).*

---

### 4. Identified Missing Information / Data Gaps
| Gap | Action Needed |
|-----|----------------|
| **Exact product code & predicate clearance numbers** | Perform FDA database query and record numbers (e.g., K123456) |
| **Confirmation that selected predicate is still marketed** | Contact manufacturer or check FDA device listing |
| **Recall / safety communication history for predicate** | Search MAUDE/Recalls DB; document findings |
| **Precise IFU wording comparison** | Obtain the predicate’s IFU text and map against proposed IFU |
| **Technical differences justification data** | Provide bench‑test, performance‑test or literature supporting each difference |
| **Software safety class assignment (A/B/C)** | Conduct IEC 62304 classification analysis |
| **Presence of AI/ML modules** | Explicitly state whether AI/ML is included; if yes, develop PCCP |
| **Detailed cybersecurity threat model & mitigation plan** | Produce a documented risk‑based security assessment |
| **OS and minimum hardware specifications** | List supported operating systems, CPU/RAM/storage minima |
| **SBOM generation process** | Define tooling (e.g., SPDX‑tools) and create sample SBOM |
| **Interoperability test reports (DICOM, HL7/FHIR, IHE)** | Conduct conformance testing against reference devices |

---

### 5. Key Risk Controls (to be reflected in the submission)

1. **Risk Management** – ISO 14971 risk analysis with residual risk acceptance criteria.
2. **Software Lifecycle Controls** – IEC 62304 processes: requirements management, design verification/validation, configuration control.
3. **Cybersecurity** – Threat identification, encryption of PHI, role‑based access, secure OTA updates, audit trail logging.
4. **AI/ML Change Management** – PCCP covering pre‑specified changes, performance monitoring, post‑market algorithm updates.
5. **DICOM Network Security** – TLS for DICOM associations, firewall rules, network segmentation.
6. **Usability/Human Factors** – UI validation per FDA “Human Factors and Medical Devices” guidance to mitigate use errors.
7. **Recall Readiness** – Procedures aligned with 21 CFR Part 806 for voluntary corrections/removals.

---

### 6. Human‑Escalation Triggers

| Trigger | Reason & Escalation Path |
|--------|---------------------------|
| **Predicate > 5 yr old or discontinued** | Senior RA review to determine need for “additional strengthening” justification; possible escalation to Regulatory Lead. |
| **AI/ML module identified** | Immediate engagement with the AI/ML specialist team and senior regulatory counsel to develop a PCCP; escalate if PCCP cannot be finalized within timeline. |
| **Unresolved technical differences** (no supporting data) | Halt submission preparation; require engineering evidence or redesign; notify Project Manager. |
| **Failure to demonstrate predicate market presence** | Escalate to Business Development for alternative predicate search or consider De Novo pathway. |
| **Incomplete risk management file** | QA/CMO review required before filing; escalation to Quality Assurance Director. |
| **UDI non‑compliance (labeling, GUDID entry)** | Notify Regulatory Affairs Manager; may require legal review of labeling claims. |
| **Cybersecurity threat model missing or insufficient** | Elevate to Information Security Lead and Regulatory Affairs for remediation plan. |

---

### 7. Peer Review Prompt
> *Please have another RA colleague examine the assumptions above, specifically: (a) whether the selected predicate truly satisfies the “single‑primary” rule; (b) completeness of the AI/ML change‑control considerations under PCCP; and (c) any jurisdiction‑specific gaps such as EU MDR references that may have inadvertently crept into this US‑focused draft.*

---

**Regulatory Judgment:**  
The Imaging Workstation GUI is a Class II device under 21 CFR §892.2050 and should pursue a traditional 510(k). The core evidence set—predicate justification, risk management, IEC 62304 software validation, cybersecurity documentation, DICOM/IHE interoperability statements, SBOM, and (if applicable) PCCP—must be assembled before filing. Missing data points identified above must be resolved; any trigger listed should be escalated to the appropriate senior functional lead prior to submission.

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

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20261019-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "0137cb4a204b03a8", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md", "source_hash": "6c864b98fca94d3a9546fde9cef298ef58210c9ac702628a937bcf05144604b6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `0137cb4a204b03a8`
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

> **Regulatory Draft – 510(k) Predicate‑Selection Strategy**

| Item | Assessment / Recommendation | Supporting citation |
|------|-----------------------------|---------------------|
| **Device classification & submission route** | • Determine the product class by mapping its intended use to the appropriate FDA panel. For imaging‑related software or hardware the rule falls under **21 CFR Part 892** (e.g., §892.2050 for image‑management/analysis systems). <br>• If the device is a Class II device, pursue a traditional **510(k) Premarket Notification** under **21 CFR Part 807**. | Framework reference: 21 CFR Part 892; 21 CFR Part 807 |
| **Primary predicate‑search requirement** | • Use the FDA 510(k) Premarket Notification Database to locate all cleared devices whose intended use overlaps with the new device. <br>• Confirm each candidate’s **K‑number** and verify that it is listed as a “substantially equivalent” reference in the database. | Source: “FDA 510(k) Premarket Notification Database (predicate 검색·K-number 확인용, 실 predicate 선정 시 필수 조회)” – no specific identifier found in source — verify separately |
| **Evidence package for substantial equivalence** | 1. **Predicate comparison table** (device name, K‑number, classification, intended use, technological characteristics). <br>2. **Performance testing** (bench, animal, or clinical) that demonstrates parity with the predicate(s). <br>3. **Risk analysis** per ISO 14971:2019 (including risk control measures and residual risk evaluation). <br>4. **Software lifecycle documentation** (if software‑based) complying with IEC 62304:2006+A1:2015. <br>5. **Labeling** meeting 21 CFR §801 requirements (indications, contraindications, warnings, etc.). <br>6. **UDI labeling** per 21 CFR §830.10‑§830.60. <br>7. **QMS compliance** with the new Quality Management System Regulation (QMSR) – Part 820 (effective Feb 2026) aligned to ISO 13485:2016. | Framework references: ISO 14971:2019; IEC 62304:2006+A1:2015; 21 CFR §801; 21 CFR §830.10‑§830.60; 21 CFR Part 820 |
| **Missing information (as indicated by source)** | • No predicate K‑numbers have been identified yet – the “FDA‑510K‑B3 증빙 미비 해소” note signals a gap in documented predicates. <br>• Absence of a completed **Refuse to Accept (RTA) checklist** for Section B.3 of the FDA RTA Guidance. <br>• No explicit risk management file or software change‑control plan (PCCP) has been referenced. | Source: “FDA-510K-B3 증빙 미비 해소”; “Refuse to Accept Policy for 510(k)s” Guidance Section B.3 – no specific identifier found in source — verify separately |
| **Key risk controls to be documented** | • Design input verification against intended use. <br>• Hazard identification and mitigation per ISO 14971 (e.g., data integrity, cybersecurity, usability). <br>• Implementation of a **Predetermined Change Control Plan (PCCP)** if the device incorporates AI/ML components (FDA Guidance Dec 2024). <br>• Validation of labeling, UDI placement, and software verification/validation. | Framework references: ISO 14971; PCCP (FDA final guidance Dec 2024) |
| **Human‑escalation triggers** | 1. **Predicate gap:** If no K‑number is secured within *5 business days* after the start of the analysis, flag to senior RA lead for supplemental market research. <br>2. **RTA non‑acceptance:** Any “refuse‑to‑accept” finding in Section B.3 (e.g., missing predicate evidence, incomplete comparison table) triggers an immediate review by the regulatory manager. <br>3. **QMSR compliance deficiency:** Missing ISO 13485:2016‑aligned procedures or QMSR documentation → escalate to Quality Assurance Director. <br>4. **UDI/Labeling omission:** Absence of UDI data matrix on labeling → raise to product development lead for redesign. | No specific identifier found in source — verify separately |

---

### Action Summary
1. **Generate a predicate‑search worksheet** using the FDA 510(k) database; capture K‑numbers, classification, and intended use.
2. **Populate the B.3 RTA checklist** (refuse‑to‑accept criteria) with completed predicate evidence.
3. **Assemble the required evidentiary package** listed above, ensuring each element cites the appropriate CFR part or standard.
4. **Conduct a gap analysis** against QMSR (Part 820) and ISO 13485:2016; remediate any missing SOPs.
5. **Document risk controls** per ISO 14971 and, where applicable, develop a PCCP for future AI/ML updates.

---

### Peer Review Prompt
> *“Please review the assumptions underlying the predicate‑selection approach (e.g., reliance on the FDA 510(k) database alone, classification under Part 892), verify that all jurisdiction‑specific gaps (QMSR, UDI, RTA Section B.3) are captured, and flag any missing regulatory artifacts or mis‑mapped standards.”*

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

1. Chunk `162881704545950641`

> ## 개정 이력 | 버전 | 일자 | 변경 내용 | 작성자 | |------|------|-----------|--------| | v0.1 | 2026-09-09 | 골격 템플릿 신규 생성 (FDA-510K-B3 증빙 미비 해소) | RA 담당자 | ---

2. Chunk `349912156821510479`

> ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance Section B.3 - FDA 510(k) Premarket Notification Database (predicate 검색·K-number 확인용, 실 predicate 선정 시 필수 조회)

## ra_eu

### kb-eval-20261019-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "30471dd490a83897", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `30471dd490a83897`
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

> **Regulatory Draft – MDR 2017/745 Classification & Conformity‑Assessment Route**

---

### 1. Device Scope (as inferred from source)

| Item | Inferred content | Source note |
|------|------------------|-------------|
| Intended purpose | **Diagnostic X‑ray emitting device** (ionising radiation) | Rule 10 citation – “이온화 방사선 방출 진단기기 (X‑ray 발생장치)”【2】 |
| Software component (if any) | Medical‑device software (SaMD) that provides diagnostic information | Rule 11 citation – “Medical Device Software (SaMD)”【2】 |

> **Assumption:** The primary hardware is the X‑ray source; ancillary software is classified separately but considered part of the same system for MDR purposes.

---

### 2. Classification

| Element | Determination | Regulatory basis |
|---------|---------------|------------------|
| Hardware (X‑ray source) | **Class IIb** | **Rule 10** – active devices that emit ionising radiation for diagnostic use are classified IIb【2】 |
| Software (SaMD) | **Class IIa or IIb** depending on the impact of the clinical decision support. If the software alone can lead to a serious deterioration or surgical intervention, it is IIb; otherwise IIa. | **Rule 11** – SaMD classification criteria (no further detail in source)【2】 |
| Overall system | The higher class governs → **Class IIb** | MDR principle that the device with the highest class determines the route for the whole system.

> **Citation of classification rule:** Annex VIII, Rule 10 and Rule 11 (MDR 2017/745).  

---

### 3. Conformity‑Assessment Route

| Class | Applicable Art. 52 paragraph | Required NB involvement | MDR annex(es) to be applied |
|-------|------------------------------|------------------------|-----------------------------|
| IIb   | **Art. 52(4)** – “Annex IX (full technical‑documentation assessment) or Annex X + Annex XI” | Yes – Notified Body must assess either the full technical documentation (Annex IX) *or* conduct a type‑examination (Annex X) followed by production conformity verification (Annex XI). | **Annex IX** (quality‑management system + TD assessment) **or** **Annex X** + **Annex XI** |

> **Citation:** MDR Art. 52(4); Annex IX, X, XI.  

#### Recommended route for a Class IIb diagnostic device
- **Primary choice:** **Annex IX** (full technical‑documentation assessment) – preferred when the manufacturer already operates an ISO 13485:2016 QMS and wishes to avoid a type‑examination.
- **Alternative (if required by competent authority or market strategy):** **Annex X + Annex XI**.

---

### 4. Required Evidence & Documentation

| TD Section (Annex II §1‑§6) | Mandatory content for this device | Comments / Gaps |
|----------------------------|-----------------------------------|-----------------|
| **§1 Device description & intended use** | Detailed description of the X‑ray source, emission parameters, intended clinical applications, and any associated SaMD. | Verify that the software’s intended use is fully captured (especially decision impact). |
| **§2 Manufacturer information** | Legal name, address, EU‑representative if applicable. | None identified – confirm presence. |
| **§3 Design & manufacturing information** | Technical drawings, Bill of Materials, manufacturing process flow, sterilisation (if any), and verification of compliance with IEC 60601‑2‑28 (X‑ray tube assemblies). | IEC 60601‑2‑28 reference not yet cited – need to locate in standards list. |
| **§4 General Safety & Performance Requirements (GSPR)** | Demonstration of conformity with all 23 GSPR (Annex I), especially §§16 (radiation protection) and §17 (software). A checklist is mandatory. | Source states “GSPR 체크리스트 기반 적합성 평가 필수”【2】 – ensure completed checklist exists. |
| **§5 Benefit‑risk analysis** | Full risk management file (RMF) per ISO 14971:2019, including risk evaluation, residual risk justification, and verification of risk controls for radiation exposure and software errors. | Verify that the RMF includes use‑error analysis (§5 GSPR). |
| **§6 Clinical Evaluation & PMCF** | • **Clinical Evaluation Report (CER)** – Annex XIV Part A – based on state‑of‑the‑art literature and any clinical investigations.<br>• **PMCF Plan & Report** – Annex XIV Part B, describing ongoing data collection from post‑market use of the X‑ray system and software.<br>• **PSUR** (annual for Class IIb) – Art. 86(2). | Source requires “PMS / PMCF / PSUR 체계 구축 필요”【2】 – confirm that a written PMS plan (Art. 84) is in place, and schedule for PSUR. |
| **Annex III (Post‑Market Surveillance)** | PMS system (Art. 83), PMS plan (Art. 84), periodic safety update report (PSUR) per Art. 86. | None identified – must be drafted. |

#### Additional Specific Evidence Needed
1. **Radiation Safety Testing** – Dosimetry data, conformity to IEC 60601‑2‑28 & IEC 60601‑2‑54 (if the system includes projection radiography).  
2. **Software Validation** – According to IEC 62304:2006+A1:2015; usability verification per IEC 62366‑1:2020 if software is intended for lay users or critical decisions.  
3. **Clinical Data** – If no sufficient literature exists, a clinical investigation (Annex XIV Part B) may be required before CE marking.  

---

### 5. Identified Missing Information (to be supplied before NB submission)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended use statement** (clinical indication, patient population) | Drives classification of the software and defines clinical evaluation scope. | Obtain from product label/IFU draft. |
| **Risk Management File (RMF) – complete risk register** | Required for GSPR §§3‑9 & ISO 14971 compliance; NB will review residual risk. | Compile and cross‑reference with radiation exposure limits. |
| **Clinical Evaluation Report (CER) draft** | Annex XIV Part A – mandatory for MDR classification IIb. | Conduct systematic literature review, extract state‑of‑the‑art data, list any clinical investigations. |
| **PMCF Plan** (objectives, methodology, data sources) | Art. 84 & Annex XIV Part B – needed to show ongoing evidence of safety/performance. | Draft with clear timelines; include post‑market registry if applicable. |
| **PSUR schedule and template** | Art. 86(2) – annual for Class IIb. | Prepare a working document ready for first submission after market launch. |
| **IEC standard declarations (60601‑2‑28, 60601‑2‑54, 62304, 62366‑1)** | Demonstrates conformity with specific technical standards; often requested by NB. | List applicable standards and obtain certificates of conformity. |
| **Label & Instructions for Use (IFU) – Section §23** | Annex I §23 – must contain essential safety information, especially radiation warnings. | Draft IFU in CE language(s). |
| **Declaration of Conformity (DoC)** – content per Art. 19 & Annex IV | Required before placing on the market. | Prepare after NB assessment is successful. |

---

### 6. Risk Controls (Mapping to GSPR)

| Hazard | Control measure | Corresponding GSPR |
|--------|----------------|-------------------|
| Excessive patient/operator radiation dose | Engineering limits, automatic exposure control, shielding, compliance with IEC 60601‑2‑28 & IEC 60601‑2‑54; regular calibration. | §16 (radiation protection) |
| Software misinterpretation of image data | IEC 62304 development lifecycle, verification and validation testing, usability assessment per IEC 62366‑1, error handling routines. | §§17 (software), §5 (risk control) |
| Use‑error due to complex UI | Human factors engineering, labeling with clear warnings, training program for operators. | §22 (lay‑person use) & §5 (use‑error risk) |
| Electrical safety failure | IEC 60601‑1 compliance, protective earth, isolation testing. | §20 (mechanical/thermal – includes electrical safety) |

---

### 7. Human‑Escalation Triggers

| Condition | Triggered Action | Responsible party |
|-----------|------------------|-------------------|
| **Incomplete or missing CER** | Pause NB submission; request clinical data acquisition plan. | RA Lead → Project Manager |
| **RMF not signed off** | Escalate to Head of Risk Management for final review. | Quality Assurance |
| **PMS plan absent or lacking measurable objectives** | Immediate halt of market launch; draft PMS plan and submit for internal approval. | Post‑Market Surveillance Coordinator |
| **Discrepancy between intended use and classification (e.g., software impact underestimated)** | Re‑evaluate classification; possibly re‑classify to a higher class → inform NB. | Regulatory Strategy Lead |
| **Failure to demonstrate conformity with IEC 60601‑2‑28/54** | Launch corrective engineering actions; obtain test reports before proceeding. | Engineering Manager |
| **DoC drafted before all evidence is in place** | Suspend DoC signing; raise a compliance alert to senior management. | Legal / Compliance Officer |

---

### 8. Summary Verdict

- The device (X‑ray source) falls under **Rule 10 → Class IIb**; any SaMD component must be examined under **Rule 11** and classified at least IIa, possibly IIb.
- Conformity‑assessment route: **Art. 52(4)** – either **Annex IX** full technical‑documentation assessment *or* **Annex X + Annex XI** type‑examination plus production conformity verification.
- Core evidence required: complete Technical Documentation (Annex II), fully populated GSPR checklist, RMF (ISO 14971:2019), Clinical Evaluation Report (Annex XIV Part A), PMCF plan/report (Annex XIV Part B), PMS system/plan (Art. 83‑84) and annual PSUR (Art. 86).
- Current gaps: detailed intended use, complete RMF, drafted CER, PMCF plan, PSUR template, IEC standard compliance declarations, IFU/labeling, DoC.

**Next step:** Populate the missing items, select the preferred conformity route (Annex IX recommended), and initiate NB engagement once all documentation is ready.

---

### 9. Peer‑Review Prompt

> **@RA‑Peer** – Please review the assumptions made about the software’s impact on classification, the completeness of the listed GSPR sections, and the adequacy of the identified missing evidence. Are there any jurisdiction‑specific nuances (e.g., recent MDR amendments or national addenda) that we have overlooked for X‑ray devices? Highlight any gaps or alternative interpretations so we can refine this draft before NB submission.

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

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261019-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e958bcdf6af25ed0", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e958bcdf6af25ed0`
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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Pathway**

---

### 1. Scope of the Assessment  
*Device description and intended use have not been supplied in the source material.* The draft therefore outlines the **process** that must be followed once those product‑specific facts are known, using only the regulatory provisions that appear in the provided excerpts.

---

## 2. Classification Determination  

| Step | Action | Regulatory basis (framework reference) |
|------|--------|----------------------------------------|
| 2.1 | Manufacturer performs **self‑classification** – apply the 22 rules of Annex VIII sequentially and retain the highest class reached. | Article 51 + Annex VIII (see source excerpt [2]) |
| 2.2 | If any doubt remains after rule application, request an opinion from the **Competent Authority (CA)** or consult the *MDCG Manual on Borderline Classification* (latest version v2.1.1, Sep‑2023). | Source excerpt [2]; “관할 CA … 또는 MDCG Manual” |
| 2.3 | Record the classification rule number(s) used and the resulting class in the **Technical Documentation – Section 6.1** (clinical evaluation) as required by Annex II §6.1. | Annex II, §6.1 |

> **Missing information needed to complete step 2:**  
> • Exact intended medical purpose / indication(s).  
> • Physical and functional characteristics of the device (e.g., active vs passive, invasive, measuring function).  

*Human‑escalation trigger:* If after internal assessment the classification cannot be resolved confidently (i.e., more than one rule may apply), **escalate to the CA** for a formal classification opinion before proceeding.

---

## 3. Conformity‑Assessment Route Selection  

| Device Class | Applicable Art. 52 paragraph & route | NB involvement required? | Key annex(es) to be applied |
|--------------|--------------------------------------|--------------------------|-----------------------------|
| **Class I** (non‑sterile, non‑measuring, non‑reusable surgical) | Art. 52(7): self‑declaration – technical documentation (Annex II & III) + EU DoC (Art. 19) | No | Annex II, Annex III |
| **Class Is / Im / Ir** | Art. 52(7): Annex IX Chapters I & III *or* Annex XI Part A (limited scope) | Yes (limited) | Annex IX or Annex XI |
| **Class IIa** | Art. 52(6): Annex IX (full QMS + technical‑doc assessment of a representative device) *or* Annex II/III + Annex XI §10/§18 | Yes | Annex IX (primary) or Annex XI |
| **Class IIb** | Art. 52(4): Annex IX (representative device per generic group) *or* Annex X + Annex XI | Yes | Annex IX or Annex X + XI |
| **Class III** | Art. 52(3): Annex IX (full technical‑doc assessment) *or* Annex X + Annex XI | Yes | Annex IX or Annex X + XI |

> **Action:** Once the class is fixed in step 2, select the corresponding route and engage a **Notified Body (NB)** that is designated for that route.

*Human‑escalation trigger:* If the chosen route requires an NB assessment but no NB has been contracted, **initiate procurement of an NB** and inform senior project management because cost estimates (e.g., €10 k–€100 k) are noted in source excerpt [1].

---

## 4. Required Evidence & Documentation  

| Evidence | Where it belongs in the technical file | Relevant regulatory citation |
|----------|----------------------------------------|------------------------------|
| **Device description, specifications, labeling** | Annex II §1‑§3 (device description, intended purpose, labeling) | Annex II |
| **Risk Management File (RMF)** – ISO 14971:2019 compliance | Annex I §§3‑9 (risk management system) & Annex II §5 (risk analysis) | ISO 14971 (2019) ; Annex I §3 |
| **Clinical Evaluation Report (CER)** – state of the art, clinical data, benefit‑risk conclusion | Annex XIV Part A; Art. 61 – CER must be kept current | Article 61, MDR Annex XIV |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B (PMCF) | Annex XIV Part B |
| **PMS System (incl. PMS plan)** | Art. 83 (system); Art. 84 (plan) | Articles 83–84 |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | Art. 86 (PSUR content & update frequency) | Article 86 |
| **Vigilance / Serious Incident Reports** | Art. 87 (reporting of serious incidents and FSCA) | Article 87 |
| **Unique Device Identification (UDI)** – registration in EUDAMED, linkage to national UDI portal if applicable | Source excerpt [1] lists UDI portals (UdiPortal.mfds.go.kr, GUDID, EUDAMED) | No specific identifier required; framework reference only |
| **Authorized Representative documentation** | Art. 11 (role of AR in EU) – proof of AR appointment and powers | Article 11 |

> **Missing information to collect:**  
> 1. Detailed **intended use statements** for classification rule matching.  
> 2. Clinical data sources: literature review, existing clinical investigations, or need for a new investigation.  
> 3. Summary of **manufacturing processes** and product specifications required for Annex II §4.  
> 4. Confirmation that the device is not covered by any exemption (e.g., “custom‑made” or “investigational”).  

*Human‑escalation trigger:* If any of the above evidence gaps cannot be filled within the planned timeline, **raise a GAP‑analysis report** to project leadership and consider commissioning a clinical investigation (Art. 61 & Annex XIV).

---

## 5. Risk Controls Aligned with GSPR  

| GSPR § | Required control / documentation | Typical implementation for a generic medical device |
|--------|-----------------------------------|-----------------------------------------------------|
| §3 – General requirements / RMF | ISO 14971‑based risk management plan, risk analysis, evaluation of residual risks | Establish risk matrix, verify controls, update after PMS data |
| §4 – Risk control measures | Verify that identified risks are eliminated or mitigated (e.g., design safeguards, protective labeling) | Design features, alarms, fail‑safe modes |
| §5 – Use‑error related hazards | Usability engineering per IEC 62366‑1:2020; user testing results | Conduct formative and summative usability studies |
| §6 – Device lifetime & maintenance | Specification of expected service life, maintenance schedule | Include in labeling (Annex II §3) |
| §7 – Transport & storage | Validation of packaging, transport conditions | Perform environmental tests per IEC 60601‑1 |
| §8 – Benefits vs. residual risks | Benefit‑risk analysis within CER and RMF | Document justification for acceptable residual risk |
| §9 – Devices without a medical purpose | Verify that the device is indeed a medical device; if not, follow Annex XVI | Classification check (already performed) |

> **Missing information:** Specific hazard analyses, design verification/validation data, usability test reports.

*Human‑escalation trigger:* If residual risk cannot be justified as “acceptable” (i.e., benefits do not outweigh risks), **stop the CE‑marking process** and seek redesign or additional mitigation measures.

---

## 6. Summary Judgment  

1. **Classification:** Must be performed by the manufacturer using Annex VIII rules (Article 51). The exact class cannot be fixed without device‑specific data.  
2. **Conformity route:** Determined by the resulting class according to Art. 52(3‑7) – either Annex IX alone or Annex X + XI for higher classes. NB involvement is required for all classes except pure Class I.  
3. **Evidence package:** Technical Documentation (Annex II), CER (Art. 61, Annex XIV Part A), PMCF plan/report (Annex XIV Part B), PMS system (Arts 83‑86), RMF (ISO 14971 2019, Annex I §3).  
4. **Gaps:** Intended purpose, classification rule, clinical data sources, detailed risk analyses, and manufacturing specifications are absent from the source. These must be gathered before any NB audit.  

**Human‑escalation triggers** have been highlighted in sections 2–5 (classification doubt → CA; missing evidence → GAP report; unacceptable residual risk → redesign halt). 

---

## 7. Peer‑Review Prompt  

*Colleague, please review the following:*  

- Are the assumed classification steps and the mapping to Art. 52 routes complete for all possible classes?  
- Does the evidence checklist cover any additional MDR requirements that may apply (e.g., software documentation per IEC 62304 if applicable)?  
- Have we omitted any obligations specific to **authorized representatives** or **importers** that could affect a device entering the EU market through an importer?  
- Given the limited information from the source, are there other regulatory sources (MDCG guidance, national provisions) we should reference before finalising the GAP analysis?

--- 

*Prepared by Theo – EU MDR Regulatory Affairs Specialist.*

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

### kb-eval-20261019-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d428b7a5693049c1", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d428b7a5693049c1`
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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Planning**

| Item | What the MDR requires | Current status (based on supplied source) | Action / Evidence needed |
|------|-----------------------|-------------------------------------------|--------------------------|
| **1. Device description** | §1 of Annex II – a complete “Device Description” that includes intended purpose, mode of action, indications, contraindications and the principle of how the device works. | Only a generic placeholder is available in the source table (“제품 설명 §1 Device Description”). No detailed narrative or intended‑use statement has been supplied. | Provide a full narrative (max 500 words) together with any applicable reference standards, diagrams and a statement of the regulatory classification basis that will be used later. |
| **2. Intended purpose & Mode of Action** | Critical for applying the classification rules in Annex VIII. Must answer: <br>‑ Is the device active? (energy supplied/controlled) <br>‑ Does it diagnose, treat or monitor? <br>‑ Is it invasive, implantable, reusable surgical, measuring or sterile? | Not present in source excerpts. | Obtain the manufacturer’s “Intended Use” claim verbatim; map each attribute to the relevant rule(s) (e.g., Rule 9, 10, 11, 17). |
| **3. Classification** | Art. 52 combined with Annex VIII rules. The route follows the class (I, Is/Im/Ir, IIa, IIb, III). | No classification can be assigned because the intended‑use statement and technical characteristics are missing. | <ul><li>Apply the appropriate rule(s) from Annex VIII once the intended purpose is known.</li><li>If multiple rules apply, use the “higher” class as defined in MDR Annex VIII.</li></ul> |
| **4. Conformity‑assessment route** | Determined by Art. 52(3‑7) and the device class: <br>‑ Class I (non‑sterile, non‑measuring, non‑reusable‑surgical) → self‑declaration (no NB). <br>‑ Classes Is/Im/Ir → Annex IX or XI limited scope (NB required). <br>‑ Class IIa → Art. 52(6): Annex IX **or** Annex II + III + Annex XI §10/§18. <br>‑ Class IIb → Art. 52(4): Annex IX **or** Annex X + Annex XI. <br>‑ Class III → Art. 52(3): Annex IX **or** Annex X + Annex XI. | No class, therefore no route can be selected yet. | Once the class is fixed, select one of the two permitted routes and engage a Notified Body (NB) if required. |
| **5. Technical Documentation (TD)** – Annex II sections 1‑6 | <ul><li>§1 Device description (see #1).</li><li>§2 Labeling & IFU (Annex I §23).</li><li>§3 Design & Manufacturing information.</li><li>§4 GSPR checklist (Annex I §§1‑9, 16‑22).</li><li>§5 Risk Management (ISO 14971 2019; Annex I §3‑9). </li><li>§6 Verification & Validation reports.</li></ul> | The source mapping table lists the equivalent US/Korean documentation items but does not provide any of the actual artefacts. | Gather and organise all above files into the TD “Binder” as required by Annex II. |
| **6. Clinical Evaluation** | Annex XIV Part A (CER) – must be kept up‑to‑date under Art 61. Evidence can be from literature, clinical investigations or PMS data. | No CER has been mentioned. | Conduct a State‑of‑the‑Art (SOTA) literature review; if gaps remain, plan a Clinical Investigation (Annex XV) or PMCF (see #7). |
| **7. Post‑Market Surveillance (PMS)** | Art 83 (system), Art 84 (plan), Art 86 (PSUR for IIa/IIb/III) – technical documentation in Annex III. | No PMS plan or system described. | Draft a PMS plan (Art 84) and assign responsibilities; build a PMS database (Art 83). For Class IIa+ prepare a periodic safety update report per Art 86. |
| **8. Risk Controls** | Annex I §3 (risk management system), §§4‑9 (control measures, use‑error analysis, lifetime, transport, foreseeable risks, benefit–risk) – implemented via ISO 14971 2019. | Only a generic reference to “Risk Management File (ISO 14971)” appears in the source table. No specific risk analysis is present. | Produce a full Risk Management File covering: <br>‑ Hazard identification, <br>‑ Estimation of risk, <br>‑ Evaluation of residual risk versus benefits (§8), <br>‑ Production/ post‑production risk controls (use‑error, transport, etc.). |
| **9. Labeling & IFU** | Annex I §23 – must contain device name, intended purpose, indications, contraindications, warnings, sterilisation & shelf‑life (if applicable). | Only a placeholder “라벨·IFU §2 Labeling” is shown. | Draft the label and Instructions for Use in English (minimum) plus any NB‑requested language(s). |
| **10. Language & Translation** | Minimum English; additional languages may be required by the Notified Body or Member State. | Mentioned in source “언어 – 최소 영어 필수; NB 요구 언어 추가”. | Confirm which Member States will market the device and arrange professional translations. |

---

### Immediate Human‑Escalation Triggers  

| Trigger | Reason | Recommended escalation |
|--------|--------|--------------------------|
| **Missing Intended‑Use statement** | Classification cannot be performed without it. | Escalate to Product Owner / Clinical Team for a definitive “Intended Use” description (including target population, clinical condition, duration of use). |
| **Unclear active/sterile/measuring status** | Determines whether NB involvement is mandatory (Classes Is/Im/Ir, IIa‑III). | Escalate to Engineering Lead for clarification on device architecture and any sterilisation or measuring functions. |
| **No clinical evidence plan** | A CER (Annex XIV) or PMCF (Annex XIV Part B) is mandatory before conformity assessment. | Escalate to Clinical Affairs to initiate a literature review and/or Clinical Investigation protocol. |
| **Absence of Risk Management File** | GSPR compliance (§3‑9 Annex I) cannot be demonstrated. | Escalate to Quality/Regulatory Manager to commission risk analysis per ISO 14971 2019. |
| **Incomplete TD (missing design & manufacturing data)** | NB will reject technical documentation. | Escalate to Design Engineering for detailed BOM, manufacturing process flowcharts and validation protocols. |
| **No PMS system defined** | Art 83–86 require a functional PMS system before market entry for Class IIa+ devices. | Escalate to Post‑Market Surveillance Lead to design the PMS plan and database. |

---

### Peer‑Review Prompt  

> **To: RA peer (e.g., Ana, Marco, Li)**  
> Please review this draft focusing on:  
> 1. Whether the classification approach correctly anticipates all applicable Annex VIII rules given our limited device description.  
> 2. Any gaps in source coverage – e.g., missing identifiers that might exist elsewhere in the repository but are not reflected here.  
> 3. Jurisdiction‑specific nuances (e.g., language requirements, local QMS references) that could affect the selection of Annex IX vs. Annex X+XI routes.  
> Provide constructive challenges or ask for additional evidence so we can close the identified gaps before engaging a Notified Body.

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

### kb-eval-20261019-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "0772093e7a227eb2", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `0772093e7a227eb2`
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

> **Regulatory Draft – X‑ray Medical Device (Ionising Radiation Equipment)**  

---

### 1. Device Overview  
* **Intended purpose:** Generation of ionising radiation for diagnostic imaging (radiography / radioscopy).  
* **Core technology:** X‑ray tube assembly, high‑voltage generator and control unit; software that selects exposure parameters and records images.  

---

### 2. Classification & Conformity Assessment Route  

| Item | Determination |
|------|---------------|
| **Applicable MDR rule** | **Rule 10** – active device emitting ionising radiation for diagnostic purposes (IEC 60601‑2‑54 scope). |
| **Resulting class** | **Class IIb** (as stated in source excerpt [1] – “X‑ray is Class IIb 이상”). |
| **Conformity route (Art. 52 MDR)** | **Annex IX** (full quality‑management‑system + technical‑documentation assessment by a Notified Body).  <br>Reference: Art. 52(4) MDR – “Class IIb → Annex IX” and the mandatory NB involvement for Class IIb devices. |
| **Notified Body requirement** | Mandatory (NB certification required).  Sources list several designated NB‑s (TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ) – see excerpt [1]. |

*No specific MDR classification code (e.g. MDxxxx) is disclosed in the source; this must be verified in the NANDO database.*

---

### 3. Required Evidence & Documentation  

| Section | Required Item (Regulatory basis) | Current status (per source) |
|---------|----------------------------------|------------------------------|
| **Technical Documentation (Annex II §1‑6)** | • Device description, intended use, variants, labeling (Annex I §23). <br>• Design & manufacturing information (drawings, process flow). <br>• Risk Management File (ISO 14971:2019) – risk analysis, evaluation, control measures. <br>• Verification & validation results (including radiation safety tests per IEC 60601‑2‑54). | • “Technical Documentation Assessment report” referenced in excerpt [2] → indicates a draft TD exists for NB review. |
| **Quality Management System** | QMS certified to ISO 13485:2016, audited by the selected NB (Annex IX §2). | • “QMS Audit related documents” listed in excerpt [2]; audit plan & reports required. |
| **Clinical Evaluation (Annex XIV Part A)** | State‑of‑the‑art literature review, clinical performance data, benefit–risk determination. | Not mentioned – gap identified. |
| **Post‑Market Surveillance (Art. 83‑86)** | • PMS plan (Art. 84) describing systematic collection of field data. <br>• Periodic Safety Update Report (PSUR) for Class IIb (annual, Art. 86). | No PSUR or PMS artefacts referenced – gap identified. |
| **PMCF Plan & Report (Annex XIV Part B)** | Required for devices where pre‑market clinical data are insufficient; should outline ongoing data collection. | Not mentioned – gap identified. |
| **Labeling & IFU** | Conform to Annex I §23 (including radiation safety information, contraindications, intended user). | Not detailed in source – gap identified. |
| **Declaration of Conformity (Art. 19)** | Must contain content listed in Annex IV and be signed by the manufacturer. | Not referenced – gap identified. |

---

### 4. Missing Information & Immediate Actions  

1. **Exact MDR classification code (MD‑xxxx)** – verify in NANDO database; record the official code.  
2. **Complete Clinical Evaluation Report** – gather state‑of‑the‑art literature, any clinical investigations, and draft a CER (Annex XIV Part A).  
3. **PMS Plan & PSUR schedule** – develop in line with Art. 84/86; assign responsible post‑market surveillance team.  
4. **PMCF plan** – required if the pre‑market clinical data are not exhaustive; define endpoints, cohort size, and timelines.  
5. **Full labeling package (IFU, symbols, safety notices)** – ensure compliance with Annex I §23 and IEC 60601‑2‑54 radiation safety requirements.  
6. **Validated risk control measures** – especially pertaining to ionising radiation exposure limits, operator protection, and emergency shutdown; document in RMF per ISO 14971.  

---

### 5. Core Risk Controls (Annex I references)  

| GSPR § | Control measure (example) |
|--------|---------------------------|
| **§3** – Risk management system | Implement ISO 14971‑based RMF covering hazard identification of radiation dose, stray radiation, and electrical safety. |
| **§4** – Risk control measures | Shielding design, interlocks, automatic exposure termination, built‑in dose‐monitoring algorithms. |
| **§5** – Use‑error risks | User‑interface ergonomics, training instructions, colour‑coded controls to prevent accidental high‑dose selection. |
| **§6** – Device lifetime | Define maximum number of X‑ray exposures per tube; include service‑interval testing. |
| **§7** – Transport & storage | Provide packaging that protects tube integrity and calibration status. |
| **§8** – Benefit–risk analysis | Demonstrate clinical benefit (diagnostic image quality) outweighs radiation risk, supported by CER conclusions. |
| **§16** – Radiation protection | Verify compliance with IEC 60601‑2‑54 limits for patient skin dose and stray radiation; include test reports. |
| **§23** – Information supplied | IFU must contain radiation safety warnings, contraindications (e.g., pregnant patients), and emergency procedures. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason & Required Action |
|---------|---------------------------|
| **Absence of verified MD classification code** | Pause NB submission; assign regulatory analyst to query NANDO and update TD. |
| **Incomplete Clinical Evaluation (no CER draft)** | Escalate to clinical affairs lead – request literature search plan and/or post‑market data collection. |
| **No PMS/PMCF documentation prepared** | Alert post‑market surveillance manager; initiate development of PMS plan within 2 weeks. |
| **Non‑conformities identified in QMS audit (pending)** | Notify Quality Manager to resolve before NB audit; record in “Non‑conformity response” folder (excerpt [2]). |
| **Missing or incomplete labeling package** | Forward to regulatory writing team; lock release until full compliance check performed. |
| **Unclear NB selection criteria (only candidate list provided)** | Require documented NB comparison matrix and contract draft before proceeding with formal engagement. |

---

### 7. Peer‑Review Prompt  

> *Please review the assumptions made regarding the classification (Rule 10 → Class IIb) and the selected conformity route (Annex IX). Verify that no additional EU directives (e.g., Directive 93/42/EEC for legacy devices) apply, and check whether any specific national provisions (e.g., German medical device law) introduce extra evidentiary requirements. Also assess the completeness of the listed evidence gaps, especially the need for a Clinical Evaluation Report and PMS documentation.*  



--- 

*End of draft – further clarification required on MDR classification code and completion of clinical/post‑market evidence package before NB submission can proceed.*

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

### kb-eval-20261019-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c7e5f2b55cff0daf", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c7e5f2b55cff0daf`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md)
- Source hash: `ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexIII_PMS_TD_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이...
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

> **Regulatory Draft – Classification & Conformity Route (MDR 2017/745)**  

---

### 1. Device Portfolio & MDR Class

| # | Device | Intended Function (as inferred) | MDR Rule (Annex VIII) | Resulting Class* |
|---|--------|----------------------------------|-----------------------|-----------------|
| 1 | **X‑ray Detector** | Records diagnostic X‑ray images (radiology) | **Rule 17 – “devices specifically intended for recording diagnostic images generated by X‑ray radiation”**【no specific identifier found in source — verify separately】 | **Class IIa** |
| 2 | **Handheld X‑ray Source** | Emits ionising radiation for bedside imaging (diagnostic) | **Rule 10 – “active devices that emit ionising radiation for diagnostic or therapeutic radiology”**【no specific identifier found in source — verify separately】 | **Class IIb** |
| 3 | **GUI Software (SaMD)** | Provides image‑display and decision support for the detector | **Rule 11 – “software providing information used for diagnostic decisions”** (decision impact judged non‑life‑threatening)【no specific identifier found in source — verify separately】 | **Class IIa** |

\*The classification follows the MDR hierarchy; a device that could be placed under a higher rule would be re‑classified accordingly.

---

### 2. Conformity Assessment Route (Art. 52 MDR)

| Device | Art. 52 paragraph | Required NB involvement & Annexes |
|--------|-------------------|----------------------------------|
| X‑ray Detector (IIa) | **Art. 52(6)** – “Annex IX Chapters I & III + technical‑documentation assessment of one representative device” | **Annex IX** (QMS + technical‑documentation review). NB audit of the QMS and a single technical‑file sample. |
| Handheld X‑ray Source (IIb) | **Art. 52(4)** – “Annex IX Chapters I & III + technical‑documentation assessment of one representative device per generic group” (or alternative Annex X + XI) | **Annex IX** (full QMS review). Because the device emits ionising radiation, a dedicated NB with competence in radiology is required. |
| GUI Software (IIa) | **Art. 52(6)** – same route as other Class IIa devices | **Annex IX** (QMS audit and technical‑file assessment). |

*No “Annex X + XI” combination is used for any of the three devices, because all are non‑implantable.*  

---

### 3. Required Evidence Packages

| # | Evidence Item | Reg. Reference | Comments / Typical Content |
|---|---------------|----------------|----------------------------|
| 1 | **Technical Documentation (TD)** – Annex II §§1‑6 (device description, design & manufacturing, GSPR compliance, risk management, verification & validation) | Annex II §6.1; **Art. 61** (keeping CER up‑to‑date) | Must embed the clinical evaluation (see 3). |
| 2 | **Clinical Evaluation Report (CER)** – Annex XIV Part A | Annex XIV Part A; **Art. 61** | For X‑ray detector and handheld source, include state‑of‑the‑art literature (e.g., IEC 62220‑1‑1 DQE data) and any post‑market clinical follow‑up (PMCF) results. |
| 3 | **Post‑Market Clinical Follow‑Up (PMCF) Plan & Report** – Annex XIV Part B | Annex XIV Part B | Required for all three devices (see source “PMCF 필요성”). |
| 4 | **Periodic Safety Update Report (PSUR)** – Art. 86 (frequency per class) | **Art. 86(2)** – Class IIa ≥ every 2 years, Class IIb ≥ annually (matches table in source) | Must contain: (a) benefit‑risk conclusions, (b) main PMCF findings, (c) sales volume & user population estimate. |
| 5 | **PMS System** – Art. 83; PMS Plan – Art. 84 | **Art. 83**, **Art. 84** | Include data sources listed in source (serious incidents, complaints, trend reporting, literature, user feedback). |
| 6 | **Risk Management File (RMF)** – ISO 14971:2019 (Annex I §3) | Annex I §3‑9; ISO 14971 2019 | Must address radiation dose, DQE degradation, battery safety, software error modes, usability hazards (§22). |
| 7 **UDI Registration & Vigilance Reporting** – Art. 33‑39 (EUDAMED) | **Art. 33‑39** | UDI per device; vigilance data feed into PSUR and trend reporting (source shows “Vigilance 보고”). |
| 8 | **Relevant IEC Test Reports** – *Detector*: IEC 62220‑1‑1 (DQE), *Source*: IEC 60601‑2‑28 (X‑ray tube) / IEC 60601‑2‑54 (radiography); *Software*: IEC 62304 (software lifecycle) & IEC 62366‑1 (usability) | IEC 62220‑1‑1, IEC 60601‑2‑28/54, IEC 62304, IEC 62366‑1 | Must be referenced in the TD and RMF. |
| 9 | **Manufacturing Records / Process Validation** – Annex I §10‑22 (design & manufacture) | Annex I Chapter II §§10‑22 | Especially for the handheld source (battery safety, shielding). |

---

### 4. Gaps / Missing Information (to be collected before NB submission)

| # | Gap | Why it matters | Suggested source |
|---|------|----------------|------------------|
| 1 | **Exact Intended Use Statements** (indications, target population) | Drives classification and clinical evidence scope | Manufacturer labeling draft (§23 of Annex I). |
| 2 | **Full Risk Management Analysis** (hazard list, risk estimates, residual risk justification) | Required for RMF §3‑9; needed to justify GSPR compliance §8‑9 | ISO 14971 risk analysis worksheet. |
| 3 | **Clinical Data for Detector** – quantitative DQE trends over device lifetime | Supports CER & PMCF (source mentions “DQE 저하”) | IEC 62220‑1‑1 test reports, longitudinal study data. |
| 4 | **Radiation Dose Monitoring Data** for handheld source (dose‑rate maps, shielding validation) | Required by GSPR §16 & PSUR risk assessment | IEC 60601‑2‑28/54 validation reports. |
| 5 | **Usability Validation Evidence** for GUI software (user‑testing, error logs) | Addresses GSPR §§22‑23 and IEC 62366‑1 | Summaries of formative/usability tests; bug‑log analysis. |
| 6 | **PMCF Data Collection Plan Details** – sampling size, follow‑up periods, KPI definitions | Needed for Annex XIV Part B & PSUR update schedule | Draft PMCF protocol (source mentions “SaMD → 사용 중 오류 데이터 수집 필수”). |
| 7 | **UDI Assignment & EUDAMED Entry Confirmation** | Mandatory under Art. 33‑39; required for vigilance linkage | UDI Registry confirmation screenshot. |
| 8 | **Complaints & Vigilance Statistics (last 12 months)** | Feed into PSUR and trend reporting (§1 source) | Extract from complaint management system. |
| 9 | **Manufacturing Process Validation** (e.g., battery pack assembly, tube cathode cleaning) | Required for Annex I §§10‑22; influences GSPR §7 (lifetime) | Process validation protocols & batch records. |

---

### 5. Risk Controls to be Demonstrated

1. **Radiation Protection** – Shielding design calculations, interlock testing, dose‑monitor alarms (**Annex I §16**, IEC 60601‑2‑28/54).  
2. **Device Lifetime Management** – Battery health monitoring, tube aging curves, DQE degradation thresholds (**Annex I §§6‑7**).  
3. **Software Error Mitigation** – Fault‑tree analysis, automated error logging, periodic software updates with regression testing (**IEC 62304**, Annex I §23).  
4. **Usability Safeguards** – Human factors validation to prevent misinterpretation of images or accidental exposure (**IEC 62366‑1**, Annex I §§22‑23).  
5. **Electrical Safety & EMC** – Compliance with IEC 60601‑1 series, including protection against electrical shocks and electromagnetic interference (Annex I §§20‑21).  
6. **Labeling & IFU Controls** – Clear contraindications, exposure limits, user instructions in the Instructions for Use (IFU) (**Annex I §23**, Art. 10(9)).  

Each control must be traceable to a risk listed in the RMF and demonstrated by verification/validation testing or clinical data.

---

### 6. Human‑Escalation Triggers

| Trigger | Action Required | Escalation Path |
|---------|-----------------|-----------------|
| **Incomplete Clinical Evidence** (e.g., missing DQE trend data, no PMCF outcomes) | Pause NB submission; request supplemental clinical data | RA Manager → Clinical Team |
| **RMF gaps** (unassessed hazards, residual risk > acceptability) | Suspend TD finalisation; perform additional risk analysis | Risk Management Lead |
| **PSUR overdue or frequency mismatch** (e.g., Class IIa PSUR not updated within 2 years) | Issue internal reminder; update before NB audit | Post‑Market Surveillance Coordinator |
| **UDI/EUDAMED registration missing** | Immediate registration action; cannot issue DoC without UDI | Regulatory Compliance Officer |
| **Software bug‑log exceeds predefined threshold** (critical severity >5 per quarter) | Trigger corrective action and possible field safety notice (FSCA) | Quality Assurance → NB (if FSCA required) |
| **Non‑conformity identified during internal audit of QMS** (Annex IX requirement) | Implement corrective & preventive actions; re‑audit before NB engagement | Quality Manager |

When any trigger is hit, the responsible function must log the issue in the project tracker and notify the RA Team Lead for decision on proceeding to the Notified Body.

---

### 7. Summary Judgment

- **X‑ray Detector** – Class IIa, conformity route **Annex IX**; evidence package centred on CER, PMCF (moderate), PSUR every 2 years, IEC 62220‑1‑1 DQE data.
- **Handheld X‑ray Source** – Class IIb, conformity route **Annex IX** (full NB audit); tighter evidence needed: radiation dose monitoring, yearly PSUR, robust risk controls for ionising radiation.
- **GUI Software (SaMD)** – Class IIa, conformity route **Annex IX**; mandatory PMCF with active error‑data collection, usability validation, software lifecycle documentation per IEC 62304 / IEC 62366‑1.

All three devices require a complete **PMS system (Art. 83)**, **UDI registration (Art. 33‑39)**, and an up‑to‑date **RMF (ISO 14971:2019)**. The gaps listed above must be closed before the Notified Body can issue a CE certificate.

---

### 8. Peer Review Prompt

> *[To RA colleague]*  
> Please review the classification assumptions (Rule 17, Rule 10, Rule 11), the chosen conformity routes under Art. 52, and the completeness of the evidence list (especially the clinical data sources for the detector and source). Verify whether any additional MDR annexes (e.g., Annex X for a type‑examination alternative) might be more suitable for the handheld X‑ray source, considering its radiation emission characteristics. Also check if any jurisdiction‑specific obligations (e.g., national transposition in Germany or France) have been omitted.  

--- 

*Prepared by Theo – EU RA specialist (MDR 2017/745).*

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

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

## ra_kr

### kb-eval-20261019-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "b26ecae55816cd4a", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `b26ecae55816cd4a`
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

> **Regulatory Draft: MF DS Classification & Submission Pathway for the Software‑Enabled Medical Device (Detector/Source System)**  

---

### 1. Korean Grade & Regulatory Route  
| Item | Determination | Source |
|------|---------------|--------|
| **Korean grade** | **2등급** (potential to be up‑graded based on auxiliary function level) | 【2†excerpt】 |
| **Submission track** | **인증** – technical‑document review by an MFDS‑designated 심사기관 (e.g., KTL, KTC, KTR). 2등급 devices are not submitted via 허가 unless a specific exemption applies. | MFDS_인허가_상세가이드.md §2 (framework reference) |

> **Note** – No specific notice/decree number for the “2등급” rule appears in the source excerpts; verify the exact MFDS 고시 번호 separately.

---

### 2. Required Evidence Package  

| Category | Required Documents / Data | Korean‑specific Requirements |
|----------|---------------------------|------------------------------|
| **Product Specification** | Detailed specs (rated voltage, current, intended use, application site, software role) – as listed in the product strategy to‑do list. | Must be provided in Korean for MFDS review. |
| **Device Classification Justification** | Classification rationale referencing the “의료용 소프트웨어 허가·심사 가이드라인” and the 2025 Digital Medical Device Act (디지털의료제품법, 시행일 2025‑01‑24). | Include Korean language justification sheet; reference the guideline by title only – no specific notice number supplied in source (verify separately). |
| **Software Validation** | ‑ IEC 62304 (2006+A1:2015) compliance plan & verification/validation reports.<br>‑ ISO 14971 (2019) risk management file (risk analysis, risk controls, residual risk evaluation).<br>‑ If AI/ML component: change‑management plan and performance evaluation per the 2025 Digital Medical Device Act. | All user manuals, IFU, and software labels must be in Korean. |
| **Clinical Evaluation** | • Foreign clinical data (predicate device) can be used if it meets MFDS acceptance criteria for CER (separate from OECD MAD).<br>• Where MFDS requires local clinical data (e.g., for novel algorithms), submit a Korean‑language Clinical Evaluation Report per the “디지털의료기기소프트웨어 허가·심사 가이드라인”. | Verify whether CER is acceptable; MFDS guidance does not appear in source – confirm with latest MFDS notice. |
| **Non‑clinical (Safety) Data** | GLP toxicology / biocompatibility studies per ISO 10993‑1 (2018). OECD MAD may be cited for non‑clinical GLP data, but only covers safety; foreign clinical evaluations are handled separately. | No specific MFDS 고시 number is given in the source – confirm applicable notice for OECD MAD acceptance. |
| **Labeling & IFU** | Korean language labeling, instructions for use, and any software user manual. Include device name, intended purpose, contraindications, warnings, and disposal information per MFDS labeling rules. | No specific article number supplied – verify the exact MFDS 고시 (§ 23‑44 etc.) separately. |
| **KGMP Facility Certification** | Proof of KGMP (Korean Good Manufacturing Practice) compliance for the manufacturing site(s). | Requires on‑site audit by MFDS or recognized agency; reference MFDS KGMP regulation (제28조) – framework reference only. |
| **Post‑Market Surveillance Plan** | PMS plan conforming to MFDS 시판후조사 requirements (periodic safety update, adverse event reporting). | No exact rule number in source – verify the current MFDS 고시 for PMS obligations. |

---

### 3. Gaps & Missing Information  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended use statement** (e.g., “Standalone detector for intra‑operative imaging”) | Determines grade and need for local clinical data. | Obtain a concise, Korean‑language Intended Use description from product team. |
| **Predicate device details** (FDA Product Classification Database ID, 510(k) number) | Needed to justify reliance on foreign clinical evidence. | Pull the FDA 510(k) reference and include comparative table. |
| **AI/ML algorithm validation documentation** (if applicable) | The 2025 Digital Medical Device Act imposes separate performance & change‑management requirements for AI‑based software. | Provide algorithm training dataset description, performance metrics, and change‑control plan. |
| **Korean language labeling drafts** | MFDS will reject submissions lacking Korean labeling/IFU. | Draft Korean label & IFU; route to translation review. |
| **KGMP audit report** (current status) | Certification cannot proceed without KGMP compliance confirmation. | Schedule KGMP audit or obtain existing certificate. |
| **Exact MFDS 고시 / notice numbers** for classification, labeling, and CER acceptance | Required for complete submission checklist. | Search MFDS 최신 고시 database to capture identifiers; note “verify separately” until retrieved. |

---

### 4. Risk Controls (mapping to ISO 14971)  

1. **Hazard Identification** – Software malfunction, incorrect voltage/current delivery, data misinterpretation.  
2. **Risk Evaluation** – Use Failure Modes & Effects Analysis (FMEA) and software safety classification per IEC 62304.  
3. **Controls Implemented**  
   * Redundant hardware safeguards for over‑voltage/over‑current.  
   * Real‑time self‑diagnostics with user alerts in Korean.  
   * Secure firmware update mechanism (per IEC 81001‑5‑1, 2021).  
   * Access control & audit logging for AI components.  
4. **Residual Risk Assessment** – Document residual risk acceptance criteria; ensure they are “as low as reasonably practicable” (ALARP) per MFDS guidance.  

All risk management documentation must be included in the technical file submitted to the 심사기관.

---

### 5. Human‑Escalation Triggers  

| Trigger | Escalation Point |
|--------|-------------------|
| **Uncertainty about final grade** (possible uplift to 3등급) | Notify senior RA manager; request MFDS pre‑submission meeting. |
| **Missing Korean labeling/IFU** | Halt submission; involve translation/legal compliance team immediately. |
| **AI component not covered by current Digital Medical Device Act guidance** | Escalate to regulatory strategy lead for policy clarification. |
| **KGMP certification pending beyond the planned submission timeline** | Alert project manager; consider alternative manufacturing site or subcontractor. |
| **Foreign clinical evidence rejected by MFDS reviewer** | Engage external consultant experienced with MFDS CER acceptance and re‑package data. |
| **Regulatory notice numbers still unverified** (e.g., labeling rule, CER acceptance) | Flag to compliance audit team for rapid verification before dossier lock‑down. |

---

### 6. Summary Judgment  

- The device is **2등급** under MFDS → **인증** route via designated 심사기관.  
- A complete technical file must include Korean‑language specifications, KGMP certificate, risk management (ISO 14971), software lifecycle documentation (IEC 62304), biocompatibility data (ISO 10993‑1), and a PMS plan.  
- Foreign predicate device data can support the clinical evaluation but must be mapped to MFDS CER requirements; OECD MAD may be cited only for non‑clinical GLP safety data.  
- Several critical items (exact intended use, Korean labeling drafts, AI validation evidence, precise MFDS 고시 numbers) remain missing and must be secured before dossier finalization.

---

### 7. Peer‑Review Prompt  

> **@RA‑Peer:** Please challenge the assumptions made here regarding (1) the sufficiency of foreign clinical data under current MFDS CER policy, (2) whether any aspects of this software platform could trigger a reclassification to 3등급 based on “보조 기능 수준”, and (3) completeness of the risk controls in light of AI‑driven decision support. Also verify that all jurisdiction‑specific gaps have been identified.  

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

1. Chunk `1097646391221557778`

> ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정

2. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

### kb-eval-20261019-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "1551302da2b45ece", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `1551302da2b45ece`
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

> **Regulatory Draft – P3‑X‑GUI Software (Digital‑Medical‑Device Software)**  

---

### 1. Device Synopsis  
- **Product name (working title):** P3 촬영실 GUI SW  
- **Category:** Digital medical device software (디지털의료기기소프트웨어) that provides a graphical user interface for X‑ray imaging systems. At present it **does not embed AI**, but future versions may add an AI‐support module.  

---

### 2. Korean Classification & Submission Route  

| Item | MFDS determination (based on source) |
|------|---------------------------------------|
| **Device grade** | The source states the GUI SW *“could be 2등급 or un‑graded”*【198902914416608487】. The exact grade must be confirmed against 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **Submission track** | • If classified as **2등급**, the default pathway is **인증** (technical‑document review by an MFDS‑designated 심사기관).  <br>• If a grade is later assigned as 1등급, the route would be **신고**.  <br>• For 3~4등급 the route would be **허가**, but this is not indicated for the GUI SW. |
| **Potential exemption/alternative pathway** | The source notes that “clinical‑trial data may be exempted or replaced” for 2등급 (or un‑graded) devices, referencing **제25조 각 호** of the *디지털의료제품법 시행규칙* (2026‑01‑23 개정)【198902914416608487】. Confirmation of the exact clause(s) is required before invoking this route. |

> **Action:** Verify the device’s grade in the official “품목·등급” table and retrieve the full text of *제25조* in the 2026‑01‑23 amendment to determine eligibility for exemption/alternative evidence.

---

### 3. Evidence Package Required (minimum)  

| Area | Required Elements (MFDS expectation) |
|------|---------------------------------------|
| **Regulatory Classification** | Official grade certification (or documented justification if un‑graded). |
| **Quality Management System** | KGMP compliance based on **ISO 13485:2016** (framework reference – no specific notice needed). Evidence of a mature QMS can be leveraged for the “우수관리체계 특례” mentioned in the source. |
| **Risk Management** | Risk analysis & control per **ISO 14971:2019**; software‑specific development lifecycle compliance with **IEC 62304:2006+A1:2015** and usability standard **IEC 62366‑1:2015+A1:2020**. |
| **Clinical Evaluation** | • If the device remains a 2등급 GUI without AI, clinical‑trial data may be **exempted or substituted** under *제25조* (subject to verification). <br>• If an AI module is added later, the new guideline “2025‑10‑31 임상시험 가이드라인 9종 개정” requires a **comparative design** (AI + physician vs. physician alone) and presentation of analytical accuracy and effectiveness size【1127968925422991528】. |
| **Software Documentation** | - Software Description, Architecture, Algorithms, Validation plan & results (IEC 62304). <br>- Source code management and cybersecurity posture per the Korean Cyber‑Security Guideline (referencing IEC 81001‑5‑1:2021). |
| **Labeling / IFU** | All labeling, instructions for use, and promotional material must be in **Korean** per MFDS labeling rules. No foreign language content is permissible on mandatory labels. |
| **Post‑Market Surveillance (PMS)** | PMS plan aligned with MFDS 시판후조사 requirements (periodic safety update, adverse event reporting). |

---

### 4. Missing Information / Gaps  

| Gap | Why it matters | Suggested source/action |
|-----|----------------|------------------------|
| **Exact device grade** | Determines submission track & evidence scope. | Query the MFDS “품목·등급” database or use the latest *의료기기 품목 및 품목별 등급에 관한 규정*. |
| **Full text of 제25조 각 호 (2026‑01‑23 개정)** | Needed to confirm whether clinical‑trial exemption is permissible and what conditions apply. | Retrieve the amendment from the MFDS 고시/시행규칙 portal; map each clause to required documentation. |
| **Planned AI module scope** | If AI is added, the comparative clinical trial design becomes mandatory (per 2025‑10‑31 guideline). | Define functional specifications and timing of AI integration; assess impact on classification (possible upgrade to higher grade). |
| **Korean labeling draft** | MFDS requires Korean language for all required label elements. | Prepare draft label/IFU in Korean; conduct a regulatory translation review. |
| **Cybersecurity & data‑privacy controls** | Digital health software handling patient images must meet Korean cyber‑security standards (IEC 81001‑5‑1). | Conduct threat modelling and implement controls per the guideline. |

---

### 5. Risk Controls (core elements)  

1. **Risk Management File** – ISO 14971:2019 compliant file covering hazard identification, risk estimation, control measures, residual risk evaluation, and post‑market risk review.  
2. **Software Development Lifecycle** – IEC 62304 compliance: planning, development, verification, validation, maintenance. Include unit, integration, system testing, and regression testing for any future AI updates.  
3. **Usability Engineering** – IEC 62366‑1:2015+A1:2020 to guarantee safe user interaction with the GUI; conduct formative and summative usability studies (even if clinical data are exempt).  
4. **Cybersecurity** – Apply IEC 81001‑5‑1:2021 controls: authentication, encryption of image data, audit trails, vulnerability management.  
5. **PMS & Vigilance** – Establish a PMS plan that includes periodic safety updates, adverse event monitoring, and field corrective actions in line with MFDS 시판후조사 obligations.

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation to |
|--------|----------------|
| **Uncertainty on device grade** (e.g., cannot locate the item in the “품목·등급” table) | Senior Regulatory Lead / MFDS liaison for classification confirmation. |
| **Inability to retrieve *제25조* clauses** or ambiguity about exemption criteria | Legal/Regulatory counsel – request official interpretation from MFDS (공식 해석). |
| **Decision to add AI module** (changing functional scope) | Project Management & Clinical Affairs – initiate comparative clinical trial design per the 2025‑10‑31 guideline. |
| **Labeling draft fails Korean language review** | Marketing/Technical Writing team – revise labeling; repeat compliance check. |
| **QMS audit reveals gaps in KGMP/ISO 13485 implementation** | Quality Assurance Manager – remedial actions before submission. |
| **Cybersecurity assessment identifies high‑risk vulnerabilities** | IT Security Lead – implement mitigation, re‑test, and document in the cybersecurity section of the dossier. |

---

### 7. Citations  

| Source ID | Content Cited |
|-----------|---------------|
| 1127968925422991528 | New clinical‑trial guideline (2025‑10‑31) requiring comparative AI + physician design, analytical accuracy presentation, effectiveness‑size proof. |
| 198902914416608487 | Device identified as P3 촬영실 GUI SW; classification ambiguity (2등급 or un‑graded); reference to exemption/alternative route under *제25조 각 호* of the **디지털의료제품법 시행규칙** (2026‑01‑23 개정); note that verification of the clause movement from 고시 → 시행규칙 is required. |
| No specific MFDS notice or decree number appears in the excerpts beyond the above references; therefore “no specific identifier found in source — verify separately” for any other instrument numbers. |

---

### 8. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made about (1) the likely grade of the P3 GUI software and the reliance on *제25조* for clinical‑trial exemption, (2) the completeness of the evidence list given the upcoming AI module, and (3) any jurisdiction‑specific gaps not covered by the two source excerpts (e.g., labeling specifics, post‑market surveillance format). Highlight any missing Korean regulatory citations or alternative pathways that may apply.

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

### kb-eval-20261019-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "ec792e64a55c200f", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `ec792e64a55c200f`
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

> **Regulatory Draft – 촬영실 GUI SW (2등급)  

1. 품목 등급 및 허가·인증 경로**  
- **등급** : 2등급 (“2등급” 표기)【2】  
- **제출 경로** : 인증 (MFDS‑지정 심사기관을 통한 기술문서 검토)이며, 디지털의료제품법에 따른 병행 검토도 가능【2】  
- ※ MFDS가 정한 2등급 의료기기의 기본 제출 절차는 「의료기기 품목 및 품목별 등급에 관한 규정」·「의료기기 허가·신고·심사 등에 관한 규정」에 명시되어 있음【1】 – *구체적인 조문 번호는 원본에 표기되지 않아 별도 확인 필요*.

---

2. 제출에 요구되는 주요 근거 서류  

| 구분 | 요구 내용 (핵심) | 적용 기준(프레임워크) |
|------|------------------|------------------------|
| **소프트웨어 수명주기** | IEC 62304 기반 개발·검증·확인 기록 전체 | IEC 62304:2006+A1:2015 |
| **사이버보안** | 보안 위협 분석, 보안 설계·구현·시험 결과, 사이버보안 관리 체계(예: MFDS 사이버보안 가이드라인 참고) | IEC 81001‑5‑1:2021 (MFDS 가이드라인 연계) |
| **사용적합성** | 사용환경 분석, 사용성 위험 평가 및 검증 보고서 | IEC 62366‑1:2015+A1:2020 |
| **위험관리** | ISO 14971:2019 적용 전반(위험 식별·분석·통제·평가) | ISO 14971:2019 |
| **AI 적용** (생성형 AI 포함 시) | 생성형 AI 가이드라인에 따른 알고리즘 검증·변경 관리·데이터 품질·윤리·투명성 보고서; 변경관리계획서 | MFDS “생성형 AI 가이드라인”(2026‑06‑09 내부 QA 기록) |
| **품질·제조** | KGMP 적합성 인증(소프트웨어 개발/배포 조직) 및 품질관리 체계 서류 | 「의료기기 GMP 심사·평가 등에 관한 규정」【1】 |
| **라벨·사용설명서** | 모든 라벨·IFU를 한국어로 작성, 의료기기법 제28조에 따른 사용자 안내 내용 포함 | 의료기기법 및 시행령/시행규칙 규정 |
| **임상평가(필요 시)** | 2등급이지만 고위험 임상적 주장(예: 진단·치료 효과) 있는 경우 최소 현지 임상 데이터 또는 MFDS 허용 외국 임상 평가 보고서 제출 | 「의료기기 허가·신고·심사 등에 관한 규정」 중 임상평가 요구사항 (구체적 조문 번호는 원본에 없음) |

---

3. 현재 확인된 **부족 정보**  

| 항목 | 현 상황(출처 기반) | 추가 확보 필요사항 |
|------|-------------------|--------------------|
| **제품 정의·용도 서술** | 출처에 등급 및 경로만 명시【2】 | 구체적인 기능·사용자·시나리오 기술 |
| **위험관리 파일(RMF)** | 위험 관리 요구는 언급됨(ISO 14971)지만 상세 문서는 미제공 | 위험 분석·통제표, residual risk 평가 |
| **소프트웨어 아키텍처·코드** | IEC 62304 적용 의무만 확인【2】 | 개발 단계 산출물(요구사항 명세서, 설계도면 등) |
| **사이버보안 검증 결과** | 사이버보안 요구는 언급됨【2】 | 보안 테스트 보고서·취약점 분석 |
| **사용성 검증 데이터** | IEC 62366‑1 적용 의무만 확인【2】 | 사용성 시험 계획·결과(인체공학 검증) |
| **AI 알고리즘 상세** | “생성형 AI 가이드라인” 언급【2】 | 알고리즘 구조, 학습 데이터, 검증 프로세스 |
| **KGMP 인증 현황** | KGMP 관련 규정은 인용되었지만 조직 인증 여부는 미확인 | 개발/배포 기업의 KGMP 적합성 인증서 |
| **라벨·사용설명서(한국어)** | 라벨·IFU 요구는 법령에 포함돼 있으나 실제 초안 없음 | 한국어 번역본 및 레이아웃 검토 |

---

4. 핵심 위험통제 방안 (예시)  

1. **위험식별 & 평가** – ISO 14971 적용, 모든 소프트웨어 기능·인터페이스를 대상으로 FMEA 수행.  
2. **보호조치** – 사이버 위협 모델링(STRIDE 등) → 암호화·인증·패치 관리 체계 구축.  
3. **사용성 위험 억제** – 사용성 엔지니어링 프로세스 적용, 시뮬레이션 및 실제 임상 환경에서 사용자 테스트 수행.  
4. **AI 투명성** – 모델 설명 가능성 확보(Feature importance, decision logs) 및 변경 관리계획에 따라 버전 별 검증 시행.  
5. **변경관리** – MFDS “생성형 AI 가이드라인”과 연계한 Change Management Plan 수립, 모든 업데이트는 사전 위험 재평가 후 승인.  

---

5. 인용·참조 목록  

| 구분 | 출처 |
|------|------|
| 의료기기법 및 시행령/시행규칙 체계 | 【1】 |
| 2등급 GUI SW 인증 경로 및 AI 적용 가이드라인 | 【2】 |
| IEC 62304, IEC 62366‑1, ISO 14971 등 국제 표준 | 프레임워크 레퍼런스로 명시(프레임워크 번호는 기억에 의존) |
| 「의료기기 품목 및 품목별 등급에 관한 규정」·「의료기기 허가·신고·심사 등에 관한 규정」·「의료기기 GMP 심사·평가 등에 관한 규정」 | 【1】 (구체적 조문 번호는 출처에 없으므로 별도 확인 필요) |

*※ 위 표에서 “no specific identifier found in source — verify separately” 가 적용된 항목은 조문·고시 번호와 같이 정확히 명시되지 않은 경우이며, 추후 MFDS 고시(예: 고시 제2025‑22호 등)를 검증 후 삽입해야 함.*

---

6. **Human‑Escalation Triggers**  

| 상황 | 필요 행동 |
|------|-----------|
| 등급·용도 정의에 근거가 불명확하거나 기존 규정과 충돌 가능성 | RA 팀 리드에게 등급 재검토 요청(법령・고시 검증) |
| 위험관리 파일 미완료 또는 주요 위험 통제 누락 | 품질팀·위험관리 담당자와 회의 소집, 보완 계획 수립 |
| AI 알고리즘 변경이 빈번하거나 검증 체계가 부재 | 사이버보안·AI 전문 조직에 현황 점검 및 추가 검증 지시 |
| KGMP 인증 미확인 | 인증기관(예: KTL)에서 조직 적격성 확인 후 결과 보고 |
| 라벨·IFU 한국어 번역 초안이 없거나 오번역 발견 | 라벨링 담당 부서와 즉시 교정 프로세스 진행, 법무 검토 포함 |
| 해외 임상 데이터 활용 여부가 불투명 | MFDS “외국 임상평가 보고서” 허용 범위 확인 후 필요 시 현지 임상시험 계획 수립 |

---

### Reusable RA Judgment (Lesson Learned)

- **2등급 소프트웨어** → 기본 **인증** 경로이며, 디지털의료제품법과 병행 검토 가능함을 반드시 명시한다.  
- 국제 표준(IEC 62304, IEC 62366‑1, ISO 14971) 적용은 필수이지만, MFDS 고시·규정에 대한 **구체적 조문 번호**는 원본에 나타나지 않을 경우 *별도 검증*을 요구한다.  
- AI 포함 제품은 **생성형 AI 가이드라인**과 **변경관리계획**을 반드시 제출해야 하며, 이는 MFDS가 별도로 권고하는 요소이므로 누락 시 인증 불허 위험이 높다.  
- KGMP 적합성은 소프트웨어 개발·배포 조직에도 적용되며, 증빙서류(인증서) 확보가 선행되어야 함.  
- 라벨·사용설명서는 **전부 한국어**여야 하며, 법령상 요구되는 구체적 항목(제조업자 정보, 사용 목적 등)을 포함해야 한다.  

*위 판단은 현재 제공된 출처에 기반하며, 조문·고시 번호 등의 정확한 식별자는 추가 검증이 필요함을 명시한다.*

---

**Peer‑Review Prompt**  
> ⬇️ 동료 RA에게: 위 초안에서 (1) 2등급 의료기기에 적용되는 “디지털의료제품법 병행 검토” 구체적 요건은 충분히 반영됐는가? (2) 해외 임상평가 보고서(또는 외국 CER)의 수용 여부와 관련된 MFDS 고시 번호가 누락된 점이 실제 심사에서 문제될 가능성은? (3) AI‑관련 위험관리·변경 관리 체계에 대한 현재 제시 수준이 MFDS 기대치에 부합하는지 검토해 주세요.

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

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `39359892234270838`

> ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재검증 — 핵심 규제사실 반영 확인. · 상태: 승인 · 일자: 2026-06-09

### kb-eval-20261019-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "7da09b9182585c3a", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `7da09b9182585c3a`
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

> **Regulatory Draft – Korean Classification & Licensing Pathway for a Digital Medical Device (SaMD)**  

---

### 1. Scope of Assessment  
This draft assumes the product is a software‑only medical device that falls under the “digital medical device” umbrella introduced by the *디지털의료제품법* (effective 2025‑01‑24). The exact intended use, risk profile and AI/ML content are **not supplied** in the source material and must be clarified before final classification.  

---

### 2. Determination of Korean Grade (1~4등급)  

| Step | Action | Rationale / Source |
|------|--------|---------------------|
| 2‑1|Obtain the device’s official intended use, target patient group, invasive/non‑invasive nature and duration of use. | Required by **MFDS “의료기기 품목 및 품목별 등급에 관한 규정”** (see MFDS_인허가_상세가이드.md §2). |
| 2‑2|Map the intended use to the Korean grade table (1등급‑4등급). | No specific grade can be assigned without the above data; therefore **grade must be verified separately**. |
| 2‑3|If the device is classified as 3등급 or 4등급 → submission route = **허가** (full MFDS approval).<br>If 2등급 → default route = **인증** via an MFDS‑designated 심사기관.<br>If 1등급 → **신고**. | Korean classification rules are distinct from the U.S./EU “Class I/II/III” system and must be followed as written. |

> **Citation:** No specific grade identifier appears in the source excerpts; therefore *no specific identifier found in source — verify separately*.

---

### 3. Required Pre‑Submission Evidences  

| Evidence | Korean Requirement | International Reference (framework) | Comments / Source |
|----------|-------------------|--------------------------------------|-------------------|
| **KGMP 적합인정** (manufacturing site certification) | Must obtain a KGMP 적합인증서 (valid 3 years, renewal required). Procedure: GMP 심사 신청 → 품질문서 심사 → 현장조사 → 결함통보 → 시정 조치 제출 → 적합인정서 발급. | ISO 13485:2016 (QMS) – supporting standard. | *Source [1]* describes the GMP workflow and lists six accredited 심사기관 (KTL, KTR, etc.) and the addition of NIDS for digital devices (effective 2025‑01‑24). |
| **Technical Documentation** (design dossier) | Include device description, specifications, labeling (한국어), risk management file, software lifecycle documentation. | ISO 14971:2019; IEC 62304:2006+A1:2015; IEC 81001‑5‑1:2021 (cybersecurity). | Standard references are framework items – no citation caveat needed. |
| **Non‑clinical safety data** | GLP‑compliant biocompatibility testing per ISO 10993‑1:2018. OECD MAD *only* covers such non‑clinical data for mutual acceptance. | OECD “Mutual Acceptance of Data” (MAD) – non‑clinical scope only. | Framework reference; MFDS may accept foreign non‑clinical data under the OECD MAD programme, but this does **not** include clinical evidence. |
| **Clinical Evaluation Report (CER)** | If local clinical data are unavailable, a foreign CER may be accepted *only* when an MFDS notice explicitly permits it. No notice number is provided in the source; verification required. | MFDS guidance on foreign clinical data (no specific identifier in source). | *Citation*: “AI/ML 기반 GUI SW 분류·임상 요건 확인 필요” (source [2]) indicates that clinical requirements have been tightened for AI/ML SaMD, implying possible need for local data. |
| **Software‑Specific Validation** | For AI/ML algorithms: performance validation, explainability documentation, post‑market monitoring plan. | IEC 62366‑1:2015 (usability); IEC 62304; MFDS 디지털의료기기 가이드라인 6종 (2025‑05‑07). | No specific 고시 번호 is given; *no specific identifier found in source — verify separately*. |
| **Labeling & IFU** | All labeling, instructions for use and promotional material must be in Korean. Include CE/ FDA clearance statements only if they do not conflict with MFDS requirements. | MFDS 라벨링 지침 (법령 제23조 등). | No specific article number appears; *no specific identifier found in source — verify separately*. |
| **Post‑Market Surveillance (PMS) Plan** | Must outline periodic safety updates, adverse event reporting, and if applicable, a PMCF study for higher grades. | MFDS 시판후조사 규정. | Framework reference only. |

---

### 4. Identified Information Gaps  

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **Exact intended use & risk level** – needed to assign Korean grade (1~4등급) and determine required evidence depth. | Cannot select proper submission route (허가/인증/신고). | Request the product specification sheet from R&D. |
| **AI/ML algorithm details** – presence of adaptive learning, training data set, performance metrics. | Additional clinical validation & PMS requirements per 2025‑05‑07 guideline. | Obtain AI/ML description and risk assessment from development team. |
| **Manufacturing location(s)** – whether the site is already KGMP‑certified or needs a new 적합인정서. | Missing GMP certification blocks filing. | Conduct site audit; prepare documentation for chosen 심사기관 (e.g., KTL, NIDS). |
| **Foreign clinical data acceptance** – specific MFDS notice permitting use of foreign CER for this device type. | If not permitted, must generate Korean clinical data, extending timelines. | Search MFDS 고시 database for any notice post‑2025‑01‑24 relevant to the device category; record notice number (or note absence). |
| **Korean labeling draft** – complete IFU and packaging text in Korean. | Non‑compliance leads to FDA‐style clearance being insufficient. | Draft Korean label and submit to a certified translation service for review. |

---

### 5. Core Risk Controls (to be reflected in the Technical File)  

1. **Hazard Identification & Risk Evaluation** – per ISO 14971:2019; map each identified hazard to control measures.  
2. **Software Development Lifecycle Controls** – adherence to IEC 62304:2006+A1:2015, including configuration management and traceability matrices.  
3. **Usability Engineering** – conduct formative/usability testing in accordance with IEC 62366‑1:2015; document findings in the risk file.  
4. **Cybersecurity Measures** – implement baseline controls from IEC 81001‑5‑1:2021 (e.g., secure boot, authentication, vulnerability management).  
5. **AI/ML Specific Controls** – data set provenance, algorithm change management, performance monitoring plan (required by MFDS AI/ML guideline 2025‑05‑07).  

All risk controls must be summarized in the **Risk Management Report**, which will be part of the submission dossier for 인증 or 허가.

---

### 6. Citation Summary  

| Item | Source Chunk ID | Note |
|------|-----------------|------|
| GMP 적합인정 절차 & 심사기관 리스트 (including NIDS) | 1078228256164017760 | Direct excerpt from Section 5.2 of the source document. |
| Digital medical device regulatory changes – SaMD classification, NIDS authority, AI/ML guideline (2025‑05‑07) | 1121184088796802935 | Table of major regulatory updates (2025‑01‑24 to 2026 예정). |
| No specific 고시 번호 or article/section cited for labeling, CER acceptance, or AI/ML requirements. | – | “no specific identifier found in source — verify separately”. |

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason | Recommended Escalation |
|---------|--------|--------------------------|
| **Grade undetermined** after requesting intended use details. | Cannot select submission route; risk of filing under wrong track. | Pause project, notify Project Lead & Regulatory Manager for clarification. |
| **KGMP 적합인정 not yet issued** at the time of dossier assembly. | MFDS requires valid 인증서 before acceptance of technical file. | Alert Manufacturing Quality Lead to start GMP audit and schedule 심사기관. |
| **Foreign CER acceptance unclear** (no notice identifier available). | Potential rejection if foreign data are used without explicit MFDS permission. | Escalate to Senior RA for targeted search of MFDS 고시 database; consider parallel local clinical study plan. |
| **AI/ML algorithm present but AI‑specific guideline not satisfied** (e.g., missing performance validation). | Non‑compliance with 2025‑05‑07 guideline could block 허가. | Trigger a cross‑functional review involving R&D, Clinical & QA to develop required evidence. |
| **Korean labeling draft incomplete or non‑conformant**. | Labeling is a mandatory submission element; errors cause MFDS rejection. | Route to Regulatory Affairs – Labeling Sub‑team for immediate revision and Korean language verification. |

---

### 8. Peer Review Prompt  

> *“Please review this draft and challenge the following assumptions: (1) that the device will be treated as SaMD under the post‑2025 digital medical device law; (2) that foreign clinical data may be acceptable without a specific MFDS notice; (3) that the listed risk controls fully satisfy MFDS requirements for AI/ML devices. Identify any jurisdiction‑specific gaps, missing source coverage, or needed clarifications before finalizing the submission plan.”*

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

> KR PMS 계획에 'PMCF study'(EU 제도)를 if applicable로 포함 — 'Framework reference only' 라벨은 붙였으나 한국 시판후조사 체계에는 없는 제도라 제외하거나 'EU에서는 PMCF에 해당' 명시가 필요(#134 관할 규칙 잔여).
KR PMS 계획에 'PMCF study'(EU 제도)를 if applicable로 포함 — 'Framework reference only' 라벨은 붙였으나 한국 시판후조사 체계에는 없는 제도라 제외하거나 'EU에서는 PMCF에 해당' 명시가 필요(#134 관할 규칙 잔여).
>

**Source Excerpts**

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---

### kb-eval-20261019-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-19", "decision_ref": "kb-eval-20261019-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "67d90f6c40883196", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `67d90f6c40883196`
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

> **Regulatory Draft – Independent Imaging‑Room GUI Software (SaMD)**  

---

### 1. Device Overview  
| Item | Description |
|------|-------------|
| **Product type** | Stand‑alone medical software that provides a graphical user interface for imaging‑room operation (SaMD). |
| **Intended use** | *(to be supplied by the sponsor)* – e.g., display, manipulation and annotation of radiologic images; may include decision‑support or AI/ML functions. |
| **Regulatory reference** | Digital Medical Device Act (디지털의료제품법) & MFDS “의료기기 품목 및 등급에 관한 규정”. |

---

### 2. Korean Classification & Submission Route  

| Step | Determination | Rationale / Reference |
|------|----------------|------------------------|
| **Risk class** | **4등급** (high‑risk) – the default assumption for SaMD that performs image interpretation or provides clinical decision support. The exact grade must be verified against the official “품목별 등급표”. |
| **Submission track** | **허가** (MFDS approval). 4등급 devices are approved through the 허가 pathway (MFDS‑direct review). |
| **Citation** | No specific MFDS 고시/조항 number appears in the source excerpts; verification of the exact grade and the corresponding 허가 procedure should be performed using 「의료기기 품목 및 등급에 관한 규정」 (§ 2) and the MFDS 허가 상세 가이드 (MFDS_인허가_상세가이드.md §2).  **→ no specific identifier found in source — verify separately**. |

*If a sponsor later confirms that the software falls into a lower risk tier (e.g., 3등급), the route would still be 허가, but required evidence could differ.*

---

### 3. Required Evidence for 허가  

| Category | Required Artefacts | Regulatory / Standards Basis |
|----------|-------------------|------------------------------|
| **Quality Management System** | KGMP certification of the development organization (or a KGMP‑equivalent QMS audit report). | KGMP (의료기기법 제28조). |
| **Software Lifecycle Documentation** | • Software Development Plan (SDP)  <br>• Software Requirements Specification (SRS)  <br>• Software Architecture Design (SAD)  <br>• Verification Plan & Report (SVP/SVR)  <br>• Change‑control SOP & regression‑test automation evidence. | IEC 62304 2006+A1:2015 – Class C requirements (referenced in source excerpt). |
| **Risk Management** | • Hazard analysis & risk control report (ISO 14971 2019) specific to software hazards (e.g., mis‑diagnosis, data loss). | ISO 14971 2019. |
| **Cybersecurity** | Threat model, SBOM, and “PCCP” (Pre‑Market Cybersecurity Protection Plan) as required by MFDS 사이버보안 가이드라인 2025. | MFDS 사이버보안 가이드라인 2025 (source excerpt). |
| **Clinical Evaluation** | • Clinical performance data supporting intended use (local or accepted foreign clinical evaluation report). <br>• If FDA 510(k) or CE‑MDR conformity is used, evidence of MFDS acceptance of the foreign CER must be provided. | MFDS notice expanding acceptance of foreign clinical reports – specific notice number not listed in source (**→ verify separately**). |
| **Labeling & IFU** | Korean language labeling, UDI (21 CFR 830‑equivalent) format, and instructions for use meeting MFDS labeling requirements. | MFDS 고시 on labeling (specific article not cited in source – **verify separately**). |
| **Post‑Market Surveillance Plan** | PMS plan that includes complaint handling, MDR‑type reporting, and periodic safety update. | MFDS “시판후조사” regulations (no specific identifier in source). |
| **UDI & Traceability** | Device registration with UDI database; traceability matrix linking software components to risk controls. | 21 CFR 830 reference incorporated via ARR (Applicable Regulatory Requirements) in source excerpt. |
| **Foreign Evidence Mapping (if used)** | • FDA 510(k) summary or CE‑MDR Certificate <br>• Cross‑reference of foreign standards (ISO 13485, IEC 62304) to KGMP requirements. | ARR table (source §820.10(b)) indicates ISO 13485 alone is insufficient; additional UDI and MDR reporting obligations apply. |

---

### 4. Identified Gaps / Missing Information  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Exact risk class** (1~4등급) | Determines 허가 vs 인증 & evidence scope. | Obtain the official grade from the MFDS “품목별 등급표”. |
| **Intended use statement** | Needed for classification, clinical evaluation scope, and labeling. | Sponsor to provide a precise intended‑use description. |
| **Clinical performance data** (local or acceptable foreign) | Required for 허가 of 3~4등급 SaMD. | Submit a validated clinical evaluation report; if using foreign CER, confirm MFDS acceptance notice. |
| **Korean labeling draft** (including UDI format) | Korean language is mandatory; UDI must follow MFDS schema. | Prepare label & IFU in Korean and send for review. |
| **Post‑market surveillance details** (complaint handling SOP, periodic safety update schedule) | Required under MFDS 시판후조사 obligations. | Develop PMS plan aligned with MFDS guidelines. |
| **Cybersecurity implementation evidence** (threat model, SBOM) | Required by 2025 cyber guide; non‑compliance blocks approval. | Provide documented threat analysis and SBOM for all software components. |
| **Foreign regulatory instrument numbers** (e.g., MFDS 고시 번호 that permits foreign CER) | Needed to cite the exact legal basis when relying on foreign data. | Retrieve the current notice number from MFDS portal; cite it in the submission. |

---

### 5. Recommended Risk Controls (to be reflected in documentation)

1. **Software Hazard Analysis** – Per IEC 62304 Class C, identify all safety‑related hazards, assign severity & probability, and implement mitigations documented in risk management file.  
2. **Verification/Validation Matrix** – Map each requirement (SRS) to verification tests; include automated regression testing for every code change.  
3. **Change‑Control Process** – SOP that requires impact analysis, re‑validation, and MDR‑type reporting when changes affect safety functions.  
4. **Cybersecurity Controls** – Implement secure coding standards, conduct penetration testing, maintain SBOM, and produce a PCCP covering threat modeling, vulnerability management, and incident response.  
5. **Complaint & MDR Reporting Workflow** – Process to assess each complaint for “reportable” status under MFDS MDR reporting (aligned with ARR §820.35(a) in source). Record decisions in the complaint database.  

---

### 6. Citations  

| Citation Type | Reference |
|---------------|-----------|
| **Framework reference – ISO/IEC standards** | ISO 13485 2016; IEC 62304 2006+A1:2015 (Class C); ISO 14971 2019. |
| **MFDS regulatory guidance** | MFDS 사이버보안 가이드라인 2025 (referenced in source excerpt). |
| **ARR table (U.S. FDA requirements)** | Source Chunk [1] – “Applicable Regulatory Requirements” §820.10(b), §820.35(a). |
| **Software‑specific mapping** | Source Chunk [2] – Table showing KGMP ↔ IEC 62304 Class C, cyber‑security & AI/ML notes. |
| **Instance identifier** | *None found in source excerpts.*  → “no specific identifier found in source — verify separately”. |

---

### 7. Human‑Escalation Triggers  

| Trigger condition | Reason for escalation | Recommended action |
|-------------------|-----------------------|--------------------|
| **Uncertain device grade (1–4등급)** | Classification determines the entire regulatory pathway. | Prompt senior RA to consult MFMFDS grading table or request official clarification from MFDS. |
| **Missing clinical evidence** | 허가 cannot be granted without acceptable clinical performance data. | Escalate to project sponsor for generation of local clinical study or acquisition of validated foreign CER. |
| **Labeling not in Korean / UDI format incomplete** | Non‑compliance with labeling law leads to rejection. | Forward to regulatory writing team; hold submission until corrected. |
| **Cybersecurity documentation absent or fails MFDS guide** | 2025 cyber guide is a mandatory pre‑market requirement for SaMD. | Escalate to security engineering lead; request threat model, SBOM, PCCP. |
| **Foreign regulatory instrument number (e.g., notice allowing foreign CER) cannot be confirmed** | Needed to substantiate reliance on FDA/CE data. | Assign RA analyst to retrieve the latest MFDS notice and update the submission docket. |
| **Post‑market surveillance plan not drafted** | 시판후조사 is required for 3~4등급 devices. | Escalate to PMS coordinator; request full PMS SOP and schedule. |

If any of these triggers occur, the case should be paused pending resolution and a formal risk‑based decision documented in the project’s regulatory tracker.

---

### 8. Peer‑Review Prompt  

> **Colleague, please review:**  
> 1. The assumption that the imaging‑room GUI SaMD falls into 4등급 – can you locate the specific item entry in the MFDS “품목별 등급표” to confirm or correct this classification?  
> 2. Whether the cited foreign clinical evidence acceptance (MFDS notice) is currently valid for this product type, and if a more recent notice supersedes it.  
> 3. Any additional Korean‑specific obligations (e.g., mandatory “의료기기표시·포장·설명서” format, UDI issuance procedures) that have not been captured here.  
> 4. Gaps in the cybersecurity requirements beyond what is listed (e.g., need for a dedicated “보안등급평가” per MFDS).  

Your feedback will help close any jurisdictional gaps before the formal 허가 dossier is assembled.

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

> 'MFMFDS' → MFDS 오타(MFMF 계열 3회째 관측 — 표기 습관 결함, 응답 구조에는 무영향).
>

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...
