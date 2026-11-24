# KB Eval Checksheet - 2026-11-24 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261124-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "0cc42cd07ebce1a9", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `0cc42cd07ebce1a9`
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

> **Regulatory Draft – 510(k) Predicate Strategy & Submission Planning**  

---

### 1. Device Classification & Submission Route  
| Item | Decision | Rationale / Reference |
|------|----------|------------------------|
| **Classification** | **Class II (subject to Special Controls)** – provisional until product‑specific panel is confirmed (e.g., imaging → 21 CFR §892.2050; in‑vitro diagnostic → 21 CFR §862). | 510(k) pathway is the default for most Class II devices (21 CFR Part 807). |
| **Submission Type** | Traditional **Premarket Notification (510(k))** – use the “Standard” format with Summary, Device Description, Predicate Comparison, and supporting performance data. | FDA’s 510(k) submission requirements are codified in 21 CFR Part 807 subpart E. |

> **Citation:** “Submission Procedure Overview” from source outlines the standard 510(k) steps (Chunk [2]). No specific identifier is present – *verify separately*.

---

### 2. Predicate Device Identification  
| Action | Details |
|--------|---------|
| **Database Search** | Query FDA 510(k) database for devices with identical intended use, technology, and indications. |
| **Selection Criteria** | • Same clinical indication and patient population.<br>• Comparable technological characteristics (e.g., sensor type, software algorithm).<br>• Cleared under the same classification panel. |
| **Comparison Table** | Populate a Substantial‑Equivalence matrix (device features vs. predicate) per FDA guidance. |
| **Gap** | The source does not list any candidate predicates – *missing information: specific predicate clearance number* (*verify separately*). |

---

### 3. Required Evidence Package  

| Evidence Category | Typical Content | Applicable Standard / Regulation |
|-------------------|-----------------|----------------------------------|
| **Device Description & IFU** | Detailed description, indications for use (IFU), labeling mock‑up. | 21 CFR Part 801 (Labeling) – §§801.20‑801.50 for UDI placement; FDA eSTAR template referenced in source (Chunk [1]). |
| **Performance Testing** | • Bench testing of functional specs.<br>• Accuracy, precision, repeatability, linearity.<br>• Software verification/validation if software is involved. | IEC 62304:2006+A1:2015 for software life‑cycle; FDA guidance on performance testing (no specific identifier in source). |
| **Biocompatibility** | Cytotoxicity, sensitization, irritation testing of all patient‑contacting materials. | ISO 14971:2019 (risk management) and ISO 10993‑1:2018 for biological evaluation. |
| **Electrical Safety & EMC** | • Leakage current, protection against electric shock.<br>• Electromagnetic compatibility (radiated/narrowband immunity). | IEC 60601‑1:2005+A1:2012+A2:2020; IEC 60601‑1‑2 for EMC. |
| **Sterilization Validation** *(if applicable)* | Sterility assurance level, validation of terminal sterilization method. | ISO 11137‑1 (for radiation) or relevant ISO standard per sterility claim. |
| **Risk Management File** | Full ISO 14971 risk analysis, hazard list, mitigations, residual risk evaluation. | ISO 14971:2019; FDA QMSR references to ISO 13485 §7.3 (design controls). |
| **Software Documentation** *(if software is part of the device)* | • Software architecture diagram.<br>• Verification and validation test logs.<br>• Predetermined Change Control Plan (PCCP) outline if post‑market modifications are anticipated. | FDA Final Guidance “Predetermined Change Control Plan” Dec 2024. |
| **Labeling & UDI** | Label artwork with plain‑text UDI, barcode/QR per 21 CFR Part 801 §§801.20+. UDI system registration in GUDID per 21 CFR Part 830. | FDA UDI regulations (Part 801 for label placement; Part 830 for identifier system). |
| **Summary & Truthful Statements** | Concise narrative summarizing device, intended use, and comparison to predicate. | 21 CFR Part 807 subpart E – content requirements. |

> **Citation:** The source lists the required sections (Device Description, performance testing, biocompatibility, EMI) as part of the eSTAR template (Chunk [2]). No explicit regulatory identifier is given – *verify separately*.

---

### 4. Risk Controls & Mitigation Summary  

| Hazard | Control Measure | Source Standard |
|--------|-----------------|-----------------|
| **Device failure leading to misdiagnosis** | Redundant sensor pathways; software error‑handling routines per IEC 62304. | IEC 62304:2006+A1:2015 |
| **Electrical shock** | Built‑in leakage current limits, double insulation, grounding per IEC 60601‑1. | IEC 60601‑1:2005+A1:2012+A2:2020 |
| **Electromagnetic interference** | Shielded enclosure; compliance with IEC 60601‑1‑2 testing levels. | IEC 60601‑1‑2 |
| **Biocompatibility reactions** | Use of ISO‑certified medical‑grade polymers; ISO 10993‑1 testing. | ISO 10993‑1:2018 |
| **Software update risk** | Predetermined Change Control Plan (PCCP) to pre‑authorize post‑market algorithm updates. | FDA PCCP guidance Dec 2024 |

---

### 5. Identified Missing Information (Action Items)

| Gap | Impact on Submission | Recommended Action |
|-----|----------------------|--------------------|
| **Exact device category & regulation panel** (e.g., imaging, diagnostic) | Determines correct §892 subsection and special controls list. | Confirm product type with engineering; map to 21 CFR Part 892 section (e.g., §892.2050 for image‑processing). |
| **Predicate clearance number(s)** | Required in Substantial‑Equivalence comparison table. | Conduct FDA database search; document selected predicate(s). |
| **Device’s UDI issuing agency & GUDID entry** | Mandatory for labeling and record‑keeping. | Select accredited agency (per 21 CFR §830.100‑§830.130); prepare GUDID submission. |
| **Software change management plan** (if applicable) | Needed to address potential AI/ML updates under PCCP. | Draft a Predetermined Change Control Plan; include in 510(k) if required. |
| **Clinical performance data** (if claimed) | May be needed to support safety/effectiveness claims. | Determine need based on FDA guidance for the device class; plan pilot or bench–clinical study accordingly. |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Escalation Path |
|-------------------|-----------------|
| **No suitable predicate found** (i.e., no cleared device with comparable indications/technology). | Initiate **De Novo** request for novel classification; involve senior regulatory lead. |
| **FDA issues an Additional Information (AI) request exceeding 180 calendar days to respond**. | Escalate to project manager & legal for timeline impact assessment; consider filing a formal extension. |
| **Unresolved risk that cannot be mitigated with design controls** (e.g., residual risk > acceptable level). | Pause submission, engage engineering for redesign, and notify senior RA leadership. |
| **Discrepancy between intended use in IFU and labeling** identified during internal review. | Immediate label revision; obtain sign‑off from Quality & Compliance before eSTAR submission. |
| **UDI registration rejection by the FDA GUDID portal**. | Notify senior QA/Compliance, re‑prepare UDI data package, and resubmit. |

---

### 7. Key Regulatory Citations (Framework References)  

- **21 CFR Part 807** – Premarket notification (510(k)) requirements.  
- **21 CFR Part 801 §§801.20–801.50** – Labeling & UDI placement on device label.  
- **21 CFR Part 830 §§830.20, 830.100‑130, 830.300‑360** – UDI system, issuing agencies, GUDID submission.  
- **21 CFR Part 892 §892.2050 (Class II)** – Example classification for medical image processing systems (if applicable).  
- **ISO 14971:2019** – Risk management process.  
- **ISO 13485:2016 (§7.3, §7.5)** – Design and production controls embedded in QMSR (effective 2026‑02).  
- **IEC 62304:2006+A1:2015** – Software life‑cycle processes.  
- **IEC 60601‑1:2005+A1:2012+A2:2020** – Electrical safety standards.  
- **IEC 60601‑1‑2** – Electromagnetic compatibility requirements.  
- **ISO 10993‑1:2018** – Biological evaluation of medical devices.  

> *No specific device identifiers (e.g., 510(k) numbers, CFR article numbers beyond those above) were present in the source excerpts; therefore “no specific identifier found” notes are included where needed.*

---

### 8. Peer Review Prompt  
*“Colleague, please review the following assumptions and gaps: (1) classification under 21 CFR §892.2050 is provisional – confirm the correct panel for our device; (2) predicate search strategy – have we considered devices cleared via alternate pathways (e.g., 510(k) with special controls vs. de novo)?; (3) risk‑control mapping – any additional FDA‑specific special controls not captured?; (4) UDI agency selection – ensure alignment with the device’s intended market and GUDID requirements.”*

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

> 심각 결함 없음. '510(k) 요건은 Part 807 Subpart E' 구분 정확·UDI 분할·QMSR ISO 13485 §7.3 반영·AI 요청 180일 정확.

**Source Excerpts**

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20261124-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "2eb68c4509cd4ff2", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `2eb68c4509cd4ff2`
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

> **Regulatory Draft – Predicate‑Strategy Assessment (510 k vs. De Novo vs. PMA)**  

---

### 1. Bottom‑Line Recommendation  
- **Primary pathway:** Pursue a **510(k) pre‑market notification** if a suitable predicate device exists that is classified under **21 CFR Part 892** (Imaging & Radiology).  
- **Escalation trigger:** If no appropriate predicate can be identified, **escalate to senior regulatory leadership** to evaluate a **De Novo** request (new classification) or, for Class III devices, a **PMA**.  

---

### 2. Classification / Submission Route  

| Attribute | 510(k) | De Novo* | PMA |
|---|---|---|---|
| Legal basis | FD&C Act **§510(k)**, **21 CFR 807** | FD&C Act **§513(f)(2)**, **21 CFR 860** | FD&C Act **§515**, **21 CFR 814** |
| Typical class | Class I–II (some III) | New Class I‑II device | Class III |
| Predicate required | **Yes** | No | No |
| Clinical data requirement | Conditional – see §3 of FDA guidance* | “If applicable” | Mandatory |

\*De Novo is appropriate when the device is novel but does not warrant a PMA (i.e., risk profile fits a Class I‑II classification).  

*Citation: Table in source excerpt [2] provides the regulatory bases and summary.*

---

### 3. Required Evidence for 510(k)

| Evidence Element | Minimum Requirement |
|---|---|
| **Predicate Identification** | FDA‑cleared device with same intended use & technological characteristics; include 510(k) number (e.g., K#######). *No specific identifier in source – verify separately.* |
| **Device Description** | Comprehensive description, specifications, and labeling. |
| **Comparison Matrix** | Side‑by‑side comparison of intended use, indications, performance specs, and design features versus predicate. |
| **Risk Management File** | ISO 14971:2019 risk analysis, including identified hazards, severity/likelihood assessment, and risk control measures. |
| **Design Controls** | Conformance to ISO 13485:2016 (design & development, §7.3). |
| **Performance Testing** | Bench‑top functional testing, accuracy, precision, and if applicable, imaging performance per relevant FDA guidance (e.g., solid‑state X‑ray devices). |
| **Usability / Human Factors** | IEC 62366‑1:2020 usability validation (especially for image interpretation software). |
| **Software Documentation** *(if applicable)* | IEC 62304:2006+A1:2015 development lifecycle documentation. |
| **Clinical Data** | Conditional – only if FDA guidance (§3) indicates that performance cannot be demonstrated through bench testing alone. *No specific identifier in source – verify separately.* |
| **Labeling & UDI** | Label must display a UDI per **21 CFR Part 801 §801.20+**; UDI system compliance per **21 CFR Part 830**. |

---

### 4. Missing Information (to be gathered before filing)

1. **Predicate device(s)** – exact 510(k) clearance number, classification, and regulatory history.  
2. **Intended use statement** – precise wording to enable predicate matching.  
3. **Device risk class under Part 892** – confirm whether the device falls under §892.2050 (image‑processing software), §892.2010 (storage), etc.; *source does not specify* → **needs confirmation**.  
4. **Clinical performance justification** – determine if bench testing suffices or if clinical data are required per FDA guidance (§3).  
5. **UDI issuance plan** – chosen issuing agency, GUDID submission schedule.  
6. **eSTAR registration status** – confirm enrollment (mandatory for 510(k) submissions from FY 2023‑10‑01 onward).  

---

### 5. Risk Controls & Standards Alignment  

| Control | Standard / Regulation | Application |
|---|---|---|
| Hazard identification & risk mitigation | **ISO 14971:2019** (risk analysis, residual risk evaluation) | All hazards associated with imaging acquisition, processing, and data handling. |
| Design controls (planning, input, output, verification, validation) | **ISO 13485:2016**, incorporated via FDA QMSR (Part 820 §7.3, §7.5) | Device development lifecycle. |
| Software life‑cycle & safety | **IEC 62304:2006+A1:2015** | For any software component. |
| Usability / Human factors engineering | **IEC 62366‑1:2020** | Interface design for radiologists/operators. |
| Electrical safety & EM compatibility (if hardware) | **IEC 60601‑1:2005+A1:2012+A2:2020** | Imaging equipment compliance. |
| Biocompatibility (if patient‑contacting) | **ISO 10993‑1:2018** | Materials in contact with patients. |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger Action |
|---|---|
| **No suitable predicate identified** after exhaustive search | Escalate to Senior Regulatory Lead for De Novo feasibility assessment. |
| **Clinical data determined necessary** (e.g., performance cannot be proven by bench testing) and no study plan exists | Escalate to Clinical Affairs/Project Manager to develop a clinical protocol. |
| **Risk analysis yields residual risk > acceptable** (per ISO 14971) | Pause submission; convene cross‑functional Risk Review Board. |
| **UDI system not selected or GUDID entry incomplete 30 days before submission** | Notify Regulatory Operations for immediate compliance action. |
| **eSTAR registration missing** by the submission deadline | Halt filing; engage Compliance to remediate. |
| **Regulatory timeline exceeds target (90 days) due to outstanding information** | Alert Program Manager to re‑evaluate schedule and resources. |

---

### 7. Citation Summary  

- **Legal foundations:** FD&C Act §§510(k), 513(f)(2), 515; **21 CFR** Parts 807, 860, 814 (source [2]).  
- **Clinical data condition:** “조건부 (§3 참조)” – noted in source [2]; no specific identifier provided.  
- **eSTAR obligations & user fees:** listed in source [2] for 510(k).  

*All framework references are stated as facts per instruction; no invented case numbers or identifiers are included.*  

---

### 8. Peer‑Review Prompt  

> @RA‑Peer: Please review the predicate‑search assumptions, the adequacy of the listed missing information (especially device classification under Part 892), and any jurisdiction‑specific gaps (e.g., UDI labeling nuances, eSTAR enrollment). Highlight any overlooked FDA guidance that may affect clinical data requirements for this imaging device.

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

> 심각 결함 없음. De Novo §513(f)(2)/860·UDI 분할·ISO 13485 §7.3 정확. 미세: 'FDA QMSR (Part 820 §7.3, §7.5)' 표기 — §7.3/§7.5는 ISO 13485 조항인데 Part 820 소속처럼 읽힘(문맥상 ISO 언급 직후).

**Source Excerpts**

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20261124-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "cc97497f519ef374", "source": "github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md", "source_hash": "fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cc97497f519ef374`
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

> **Regulatory Draft – 510(k) Predicate‑Strategy for a New X‑ray Imaging System**

---

### 1. Device Classification & Submission Pathway  
| Item | Decision |
|------|----------|
| **Regulatory panel** | Radiology / imaging devices → **21 CFR Part 892** (Imaging devices). *Section pending confirmation for “diagnostic X‑ray system” – typically Class II*【no specific identifier found in source — verify separately】. |
| **Current CFR reference cited by the source** | “21 CFR 1020 요건” appears in the assessment matrix【§21 CFR 1020 (as quoted)】. This is an older citation that still maps to imaging equipment; include for completeness but cross‑check against the current Part 892 classification. |
| **Submission type** | Traditional 510(k) – provided a legally marketed predicate exists and all five SE decision points are satisfied (see Decision Tree, §4.1). |

---

### 2. Required Evidentiary Package  

| Evidence Category | Specific Items | Rationale / CFR/Standard Reference |
|-------------------|----------------|--------------------------------------|
| **Predicate Device Identification** | • Trade name, model, 510(k) number or other FDA‑cleared identifier of the legally marketed device (LM D). <br>• Confirmation that LM D is a “legally marketed” device in the U.S. (DP 1). | DP 1 of the SE 5‑step decision tree requires the predicate to be legally marketed【Excerpt 2】. |
| **Intended Use Comparison** | • Full intended use statement for the new X‑ray system.<br>• Side‑by‑side table showing identical indications, patient population, anatomical sites, clinical setting vs. LM D (DP 2). | DP 2 requires “identical Intended Use”【Excerpt 2】. |
| **Technological Characteristics** | • Detailed description of the X‑ray tube, detector type, image processing algorithms, exposure control, and any ancillary hardware.<br>• Comparison matrix highlighting equivalence or differences with LM D (DP 3 & DP 4). | DP 3 expects “identical Technological Characteristics”; if differences exist, they must not raise new safety/effectiveness questions (DP 4)【Excerpt 2】. |
| **Performance Data** | • Bench‑testing data: output consistency, spatial resolution, dose measurements (mGy), exposure time reproducibility.<br>• Phantom studies demonstrating image quality meeting or exceeding LM D.<br>• If clinical software is embedded, validation per IEC 62366‑1 and IEC 62304 (software life‑cycle).<br>• Statement that data meet “≥ predicate level” (DP 5)【Excerpt 2】. |
| **Risk Management** | • ISO 14971:2019 risk analysis file (hazard identification, severity, probability, risk control measures).<br>• Residual risk justification showing compliance with FDA‑recognized consensus standards for X‑ray safety (e.g., IEC 60601‑2‑44, AAPM TG‑61 dose guidelines). |
| **Design Controls** | • Design History File compliant with ISO 13485:2016 §7.3 (design control) and FDA QMSR §820.35 record‑keeping.<br>• Verification & Validation protocols & reports. |
| **Labeling & UDI** | • Draft labeling meeting 21 CFR Part 801 Subpart B (§801.20 et seq.) for UDI placement.<br>• UDI system plan per 21 CFR Part 830 (formatting, GUDID submission). |
| **Quality Management System** | • Evidence of QMSR compliance (ISO 13485:2016‑based) – SOPs, internal audit reports, corrective‑action records. |
| **Software/AI Considerations** *(if applicable)* | • Predetermined Change Control Plan (PCCP) per Dec 2024 guidance for any learning or adaptive algorithms. |

---

### 3. Gaps / Missing Information (to be obtained before filing)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact predicate device identifier** | Needed for DP 1 and to populate the “predicate” section of the 510(k). | Search FDA 510(k) database for cleared X‑ray systems with matching intended use. |
| **Full Intended Use Statement** | Drives DP 2 & labeling; any discrepancy forces NSE route. | Draft from product marketing claims, confirm with clinical stakeholders. |
| **Technological Comparison Matrix** | Determines if the device is “substantially equivalent” or requires a new technology narrative (DP 3‑4). | Prepare detailed side‑by‑side table of hardware/software specs. |
| **Clinical Performance Data** (if bench data insufficient) | FDA may request clinical data to bridge gaps in image quality or dose performance. | Plan a limited‑scope clinical investigation under IDE exemption if needed. |
| **Risk Management File** | Mandatory per ISO 14971 & FDA expectations; identifies any new hazards from design differences. | Conduct FMEA / HACCP and compile the risk file. |
| **UDI Planning Documentation** | Required on label and in GUDID; non‑compliance blocks clearance. | Develop UDI assignment plan (issuer, format). |
| **QMSR Evidence Package** | Post‑Feb 2026 QMSR replaces legacy QSR; missing records will be cited as deficiencies. | Gather SOPs, training records, internal audit reports aligned to ISO 13485:2016 §7.3/§7.5 and FDA §820.35. |
| **Software Validation (if any)** | Software that performs image processing must meet IEC 62304 & 21 CFR §§820.30‑820.70 (withdrawn but still referenced via ISO 13485). | Produce software verification & validation reports; include PCCP if ML/AI present. |

---

### 4. Core Risk Controls (Mapping to Standards)

| Hazard | Control Measure | Standard / Guidance |
|--------|-----------------|----------------------|
| Excessive patient dose | Automatic exposure control, pre‑set tube current/time limits, interlocks. | IEC 60601‑2‑44; FDA guidance on radiation protection. |
| Electrical shock | Two‑handed operation, grounded chassis, leakage current < 100 µA. | IEC 60601‑1 (2005+A1:2012+A2:2020). |
| Image quality degradation → misdiagnosis | Built‑in image processing QA, periodic calibration phantom tests. | ISO 14971 risk control; FDA “Performance Testing Guidance for X‑ray Systems”. |
| Software malfunction (image reconstruction) | Unit testing, code reviews, version control, PCCP for future updates. | IEC 62304:2006+A1:2015; PCCP guidance Dec 2024. |

---

### 5. Key Citations  

| Item | Source |
|------|--------|
| **SE Decision‑Point Tree (DP 1–DP 5)** | 【Excerpt 2 – “4.1 SE 5단계 Decision Point (FDA 2014 Guidance Appendix A)”】 |
| **Assessment matrix requirement (510(k) types, SE criteria, eSTAR sections, 3‑region comparison, 21 CFR 1020)** | 【Excerpt 1 – Table under “11. 평가 기준”】 |
| **Regulatory panel for imaging devices** | Framework reference: *21 CFR Part 892* (Imaging devices) – factual citation (no source needed). |
| **QMSR design‑control basis** | Framework reference: ISO 13485:2016 §7.3 (design controls) and FDA §820.35 (record control). |
| **Risk‑management standard** | ISO 14971:2019 – factual. |
| **Software life‑cycle** | IEC 62304:2006+A1:2015 – factual. |
| **UDI label placement** | 21 CFR Part 801 Subpart B (§801.20 onward). |
| **UDI system requirements** | 21 CFR Part 830 (§830.20, §830.100‑130, §830.300‑360). |

*No instance identifiers (e.g., specific 510(k) numbers) appeared in the source excerpts; therefore none are listed.*

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger for escalation to senior RA / regulatory counsel |
|-----------|----------------------------------------------------------|
| **Predicate cannot be proven legally marketed** (DP 1 “No”) → NSE pathway required (De Novo or PMA). | Immediate escalation – decision on alternative route. |
| **Intended use differs from any cleared device** (DP 2 “No”). | Escalate to determine feasibility of a new indication or De Novo submission. |
| **Technological differences raise novel safety questions** (DP 4 “Yes”). | Escalate for risk‑assessment review and possible NSE classification. |
| **Performance data fail to meet ≥ predicate level** (DP 5 “No”). | Escalate to design‑redo or additional clinical study planning. |
| **Incomplete QMSR documentation** (missing SOPs, audit records). | Escalate to Quality Assurance to close gaps before filing. |
| **UDI plan not finalized** (labeling crew cannot confirm placement per §801.20). | Escalate to labeling team and GUDID submission lead. |
| **Software with adaptive algorithm lacks PCCP**. | Escalate to software engineering for PCCP development; FDA may reject without it. |
| **FDA Additional Information request received** (180‑day response clock). | Escalate immediately for coordinated response planning. |

---

### 7. Bottom Line  

- **Classify the new X‑ray system as a Class II imaging device under 21 CFR Part 892** (verify exact sub‑section).  
- **Proceed with a Traditional 510(k)** if all five decision points are satisfied; otherwise prepare for an NSE pathway (De Novo or PMA).  
- Assemble the evidentiary package listed above, close identified gaps, and ensure QMSR, risk management, UDI, and labeling compliance before submission.  

---

#### Peer‑Review Prompt  

> *Colleague, please review the assumptions made about the device’s classification under Part 892 (section pending confirmation), the completeness of the predicate‑identification plan, and any jurisdiction‑specific items that may have been overlooked (e.g., radiation‑protection requirements from 21 CFR Part 1020 vs. newer Part 892 references). Also verify whether the “21 CFR 1020 요건” citation reflects current FDA expectations for X‑ray systems.*

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

> ① Part 1020를 'older citation…cross-check against current Part 892'로 서술 — 1020(방사선 성능기준)과 892(분류)는 병존 관계로 대체관계 아님(오서술, peer 프롬프트에도 반복) ② 'must meet IEC 62304 & 21 CFR §§820.30-820.70 (withdrawn but still referenced via ISO 13485)' — 폐지 조항을 요건으로 나열(인지 표기는 있으나 QMSR 계열 잔존).

**Source Excerpts**

1. Chunk `1061195424067242245`

> ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과제 3-2 SE 비교표 제출 필수 ---

2. Chunk `1072507187378217632`

> ### 4.1 SE 5단계 Decision Point (FDA 2014 Guidance Appendix A) ``` DP1. Predicate이 Legally Marketed Device인가? │ No → NSE (De Novo 또는 PMA) │ Yes ↓ DP2. 동일한 Intended Use인가? │ No → NSE │ Yes ↓ DP3. 동일한 Technological Characteristics인가? │ Yes → DP5 │ No ↓ DP4. 다른 기술특성이 Different Questions of Safety & Effectiveness를 제기하는가? │ Yes → NSE │ No ↓ DP5. 성능 데이터가 새 장치 ≥ Predicate 수준임을 입증하는가? │ Yes → SE (Clearance 가능) │ No → NSE ```

### kb-eval-20261124-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "10ebf8e009b77bd6", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `10ebf8e009b77bd6`
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

> **Regulatory Draft – Imaging Workstation Software (Medical Image Management & Processing)**  

| Item | Determination / Requirement | Source‑based citation |
|------|-----------------------------|------------------------|
| **Device class & regulatory pathway** | Class II medical device, 21 CFR Part 892 §892.2050 (medical image management and processing system). Submission via a traditional 510(k) (or special 510(k) if substantially equivalent to an existing cleared predicate). | Framework reference – 21 CFR Part 892 §892.2050 |
| **Primary predicate strategy** | • Search FDA 510(k) database by product‑code.<br>• Prefer predicates cleared ≤5 yr ago; for >7 yr old predicates add supplemental justification (modern “use of predicates” policy).<br>• Verify predicate is still marketed, not discontinued or under recall (MAUDE/Recall DB).<br>• Ensure Indications for Use (IFU) are identical or more restrictive.<br>• List all technical differences and provide data‑driven justifications.<br>• Do **not** use split predicates – a single primary predicate must cover the IFU. | Excerpt [1] |
| **Software documentation level** | Follow FDA 2023 Software Guidance (Basic vs. Enhanced). Determine required documentation set (software description, architecture, verification & validation, UI/UX evaluation) based on risk class (IEC 62304). | Excerpt [2] – “Software Level of Documentation (FDA 2023 SW guidance ‘Basic/Enhanced’)” |
| **Safety class** | Assign IEC 62304 safety class (A/B/C) after software hazard analysis. Class C triggers full validation and design transfer documentation. | Excerpt [2] – “IEC 62304 Safety Class (A/B/C)” |
| **AI/ML modules** | If AI/ML is included, develop a Predetermined Change Control Plan (PCCP) per FDA Dec‑2024 guidance; submit PCCP as part of the 510(k). | Framework reference – “Predetermined Change Control Plan (PCCP)” |
| **DICOM & interoperability** | Provide DICOM conformance statement covering Storage SCU/SCP, Worklist SCU, MPPS, Print SCU, etc.; document support for HL7 FHIR and IHE profiles if claimed. | Excerpt [2] |
| **Cybersecurity controls** | Include: authentication method, encryption of data at rest/in transit, audit‑log generation, secure update mechanism (digital signatures). Reference FDA Cybersecurity Guidance (2022) & ISO IEC 27001 as supporting standards (no identifier in source – verify separately). | Excerpt [2] |
| **Software Bill of Materials (SBOM)** | Supply SBOM in SPDX or CycloneDX format. | Excerpt [2] |
| **Labeling & UDI** | Label must display the device’s UDI (plain‑text + AIDC) per 21 CFR Part 801 §801.20 et seq.; UDI generation/registration per 21 CFR Part 830 (§830.20, §§830.100‑130). | Framework references – 21 CFR Part 801 §801.20+, 21 CFR Part 830 |
| **Quality Management System** | QMS must comply with the FDA QMSR (effective 02‑Feb‑2026) that incorporates ISO 13485:2016. Demonstrate design controls (ISO 13485 §7.3), production/process controls (§7.5), complaint handling (FDA‑specific §820.35). | Framework reference – 21 CFR Part 820 (QMSR) |
| **Risk Management** | Conduct risk analysis per ISO 14971:2019; integrate results into software hazard analysis (IEC 62304) and design controls. Document residual risk evaluation and mitigation. | Framework reference – ISO 14971:2019 |
| **Clinical/Performance Evidence** | • Bench testing of acquisition, processing, display, storage, transfer functions per intended use.<br>• Validation of DICOM conformance using accredited test suites.<br>• If AI/ML is present, performance verification on representative clinical data sets (including bias assessment).<br>· Human factors/usability testing for GUI. | No specific identifier found in source — verify separately |
| **Regulatory submission package** | 1. Cover Letter & 510(k) Summary.<br>2. Device description & intended use statement.<br>3. Predicate comparison table (including IFU text match, technical differences, market status).<br>4. Software documentation (design history file, verification/validation reports, risk management file).<br>5. PCCP (if AI/ML).<br>6. DICOM conformance statement.<br>7. Cybersecurity & SBOM artifacts.<br>8. Labeling & UDI evidence.<br>9. QMS certificates & ISO 13485 compliance. | No specific identifier found in source — verify separately |

### Missing Information (to be obtained before submission)

| Area | Gap |
|------|-----|
| **Exact device name & product code** | Needed for FDA database search and 510(k) cover sheet. |
| **Complete Intended Use / Indications for Use text** | Must be compared verbatim to predicate IFU. |
| **Predicate candidate(s)** – 510(k) number, clearance date, market status. |
| **Software safety class (IEC 62304) determination** | Requires completed hazard analysis. |
| **AI/ML module description & change‑control plan** | If applicable; currently only presence noted. |
| **Detailed hardware platform (OS version, minimum HW specs)** | Required for labeling and software validation. |
| **Risk Management File (ISO 14971) – analysis & mitigation records** | Not referenced in source. |
| **Clinical/performance test protocols & results** | Needed to substantiate safety/effectiveness claims. |
| **Label draft showing UDI placement** | Must meet 21 CFR Part 801 §801.20‑§801.50. |
| **QMS certificates (ISO 13485) and design control records** | Required under QMSR. |

### Human‑Escalation Triggers

1. **Predicate Issues** – If the selected predicate is >7 years old, discontinued, or has a recall/safety communication, flag for senior RA review to determine need for supplemental justification or alternative predicate.
2. **AI/ML Presence without PCCP** – Any AI/ML component lacking a completed Predetermined Change Control Plan must be escalated before filing.
3. **Software Safety Class C** – Requires full validation and design transfer; escalation to engineering & QA leads if documentation gaps exist.
4. **Inadequate DICOM/IHE Evidence** – Missing conformance test reports or incomplete statements should trigger a technical review.
5. **Cybersecurity Gaps** – Absence of documented authentication/encryption/audit‑log controls must be escalated to the security team.
6. **Risk Management Deficiency** – If ISO 14971 analysis is not complete or residual risk >acceptable, senior RA/clinical leads must intervene.
7. **Labeling / UDI Non‑compliance** – Any deviation from 21 CFR Part 801 labeling requirements escalates to regulatory operations for correction.
8. **QMSR non‑conformance** – Missing ISO 13485 documentation or failure to map FDA‑specific §820.35 controls should be raised to quality assurance leadership.

### Regulatory Judgment

- The device is a Class II imaging workstation software, best pursued via a traditional 510(k) using a single primary predicate that meets the checklist in Excerpt [1].  
- Full submission must include the software documentation level (Basic/Enhanced), IEC 62304 classification, DICOM/IHE conformance statements, SBOM, cybersecurity controls, and—if AI/ML is present—a PCCP.  
- All labeling must carry a UDI per 21 CFR Part 801 §801.20+ and be registered in the GUDID per 21 CFR Part 830.  
- The QMS must satisfy the post‑Feb 2026 QMSR (ISO 13485:2016 with FDA additions).  

Proceed to collect the missing items listed above; any trigger conditions encountered should be escalated as indicated before finalizing the 510(k) submission.

---

**Peer‑Review Prompt**  
*Please review the predicate selection assumptions, the completeness of the software documentation requirements (Basic vs. Enhanced), and the applicability of AI/ML change‑control guidance under FDA jurisdiction. Identify any gaps in EU/Korean regulatory references that may have inadvertently influenced this US‑focused draft.*

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

> 심각 결함 없음. QMSR 3종 매핑(§7.3/§7.5/§820.35)·UDI·PCCP 전부 정확. 미세: 'special 510(k) if substantially equivalent to an existing cleared predicate' — Special 510(k)는 자사기기 변경 경로로 서술 부정확(11-06 관찰 계열).

**Source Excerpts**

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20261124-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "289d011728cbc290", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `289d011728cbc290`
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

> **Regulatory Draft – 510(k) Strategy for “촬영실 GUI SW (영상 획득·검사 제어 Software)”**

---

### 1. Bottom‑Line Decision  
- **Submission pathway:** Traditional 510(k) (Class II).  
- **Probable FDA classification:** 21 CFR Part 892 – medical imaging devices, most consistent with **§892.2050 – Medical image management and processing system (Class II)**. *Section assignment requires confirmation against the final device specification.*  

---

### 2. Core Submission Elements & Evidence Required  

| Requirement | What to Submit | Source‑based citation |
|-------------|----------------|----------------------|
| **Device Description** | • Narrative of intended use (as in source excerpt) <br>• Software architecture diagram (modules, processes, DB, DICOM nodes) <br>• Minimum OS/hardware platform <br>• List of compatible detectors/generators (versions) | 21 CFR 807.87 – required information for a 510(k) submission* |
| **Software Documentation** | • IEC 62304 software life‑cycle plan & classification (A/B/C) <br>• SOUP inventory and traceability <br>• Cybersecurity features (authentication, encryption, audit logs) <br>• Verification/validation reports (unit, integration, system) | IEC 62304 – safety class reference* |
| **Predicate Device(s)** | • Identify cleared device(s) with equivalent function (image acquisition & view‑only control). If none, consider De Novo. | No specific identifier in source – verify separately |
| **Performance Testing** | • Functional testing against DICOM conformance (SCU/Worklist/MPPS) <br>• Bench‑level image acquisition tests (accuracy of exposure parameters, timing) <br>• Usability / human factors testing for technologist workflow <br>• Cybersecurity threat analysis & mitigation validation | FDA Guidance “Format for Traditional and Abbreviated 510(k)s” (2019‑09‑13) |
| **Risk Management** | • ISO 14971:2019 risk analysis file (hazard identification, severity/occurrence, mitigations) <br>• Mapping of software safety class to IEC 62304 controls <br>• PCCP outline for post‑market software updates | No specific identifier in source – verify separately |
| **Labeling & Indications for Use** | • Form 3881 (Indications for Use) completed with exact wording from source (“intended for use by trained technologists… not intended for primary diagnosis”) <br>• Device labeling, UDI placement per 21 CFR 801.20+ (label) and 21 CFR 830 (UDI system) | FDA Form 3881; 21 CFR 807.92 – 510(k) Summary format* |
| **Quality System** | • Evidence of compliance with QMSR (21 CFR 820/ISO 13485:2016) – design controls (§7.3 ISO), production controls (§7.5 ISO), complaint handling (§8.2.2 + §820.35) | Framework reference only |
| **Regulatory Forms** | • 510(k) Cover Sheet (Form 3519) <br>• 510(k) Summary (per 807.92) <br>• Truthful and Accurate Statement (Form 3881) | 21 CFR 807.87 / 807.92* |

\* Citations are taken verbatim from the source excerpts.

---

### 3. Missing or Ambiguous Information (needs clarification before submission)

| Item | Why it matters | Action |
|------|----------------|--------|
| **Predicate device identification** – no cleared device number supplied in source. | Required to establish substantial equivalence; absence may force De Novo route. | Conduct market search, document at least one Class II comparator. |
| **Detailed bench‑test data (accuracy, precision, timing)** | Must demonstrate that the software correctly controls X‑ray acquisition and does not affect image quality. | Generate and package test reports per FDA guidance. |
| **Human factors/usability study protocol & results** | Supports claim of “technologist‑only” operation; mitigates use‑error risk. | Perform validated user testing, include participant demographics. |
| **Cybersecurity validation (penetration test, vulnerability assessment)** | Required for all medical device software per FDA guidance on post‑market management. | Provide documented assessments and mitigation plan. |
| **UDI implementation plan** – label placement and GUDID submission details not described. | 21 CFR 801.20+ and 830 requirements are mandatory for Class II devices. | Prepare UDI labeling artwork, submit device entry to GUDID. |
| **Regulatory classification confirmation (§892.xxx)** | Source does not specify the exact Part 892 subsection; mis‑classification can trigger FDA “Refuse to Accept”. | Verify intended use against FDA product code list (e.g., “XRS – X‑ray System”) and confirm appropriate Subsection. |
| **Software Change Control Plan** – no PCCP described. | Required for future AI/ML updates or major software revisions. | Draft a Predetermined Change Control Plan as per Dec 2024 guidance. |

---

### 4. Key Risk Controls (to be documented in the submission)

1. **IEC 62304 compliance** – adopt appropriate safety class; implement required verification activities for each class level.  
2. **ISO 14971 risk management** – identify hazards unique to acquisition control (e.g., unintended exposure, incorrect parameter setting). Mitigate via UI locks, real‑time parameter validation, and audit logs.  
3. **Cybersecurity** – enforce user authentication, encrypted DICOM transmission, periodic firmware signing, and maintain a secure log of all configuration changes.  
4. **Usability safeguards** – distinct “Review” vs “Diagnosis” UI labeling; lockout of diagnostic functions without CE‑marked add‑on.  
5. **PCCP** – pre‑define permissible software modifications (e.g., minor UI tweaks, parameter updates) to streamline future FDA review.

---

### 5. Human‑Escalation Triggers  

| Trigger | Escalation to | Rationale |
|---------|---------------|----------|
| No suitable predicate identified after market search | Lead RA / Regulatory Affairs Manager | May necessitate De Novo submission or request for a classification questionnaire (Q‑Submission). |
| Incomplete or inconsistent risk analysis (ISO 14971) | Senior QA Engineer & RA lead | Risk files must be FDA‑acceptable before filing. |
| Cybersecurity assessment fails to meet “no known vulnerabilities” threshold | CISO / Product Security Team | Must remediate before submission; FDA can issue a non‑compliance letter. |
| UDI plan not aligned with Part 801/830 labeling requirements | Labeling & Packaging Manager | Failure leads to Refuse‑to‑Accept (RTA) on the 510(k). |
| Ambiguity in device classification (Part 892 subsection) | Regulatory Affairs Director | Seek FDA clarification via Division of Imaging Devices. |

---

### 6. Summary Judgment  

- **Proceed with a Traditional 510(k)** for a Class II medical imaging acquisition/control software, targeting **§892.2050** pending confirmation.  
- Prioritize securing a valid predicate device and completing the missing evidence items listed above.  
- Prepare the complete dossier (device description, software life‑cycle documentation, performance & cybersecurity testing, risk analysis, labeling/UDI, QMSR compliance) before assembling the final 510(k) submission package.

---

### 7. Peer Review Prompt  

> *Colleague, please evaluate: (1) the adequacy of our predicate‑search strategy given the limited source information; (2) whether any EU/MDR concepts have inadvertently crept into the draft; and (3) if additional FDA guidance documents (e.g., “General Principles of Software Validation” 2002) should be referenced to close remaining evidence gaps.*

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

> 'Truthful and Accurate Statement (Form 3881)' 오결합 — Form 3881=Indications for Use(동문서 2행 위에서 정확 사용), Truthful and Accurate Statement는 별도 서약(§807.87(k))으로 Form 번호 없음. 식별자 오결합 1건. 나머지 우수(§807.87/§807.92 구분 정확·QMSR 3종 매핑).

**Source Excerpts**

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

## ra_eu

### kb-eval-20261124-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "8b6d75dd68d01a0c", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `8b6d75dd68d01a0c`
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

> **MDR Classification & Conformity‑Assessment Draft – X‑ray Diagnostic Unit (emitter) + Associated SaMD**

---

### 1. Device scope (derived from source)

| Element | Description |
|---------|-------------|
| **Hardware** | “X‑ray 발생장치” – an ionising‑radiation emitting diagnostic device (e.g., portable X‑ray generator). |
| **Software** | Medical‑device software (SaMD) that processes the acquired image and provides diagnostic information. |
| **Intended use (not supplied in source)** | Must be defined by the manufacturer (e.g., “for radiographic imaging of skeletal structures in adult patients”). |

> *Source [2] identifies the hardware as a diagnostic X‑ray emitter and the software as SaMD.*

---

### 2. Applicable classification rules  

| Component | MDR rule (Annex VIII) | Resulting class |
|-----------|----------------------|-----------------|
| X‑ray emitting device | **Rule 10** – “ionising radiation‑emitting diagnostic equipment” | **Class IIb** *(source [2])* |
| SaMD that provides diagnostic information | **Rule 11** – software providing information for diagnostic decisions (class depends on impact) | Likely **Class IIa** – unless the decision could cause serious deterioration or death, in which case **Class IIb/III**. Further intended‑use wording is required to finalise. |

*Citation: Rule 10 & Rule 11 are identified in the source excerpt (Rule 10 → Class IIb; Rule 11 → SaMD classification). No further identifier is given – verify separately.*

---

### 3. Conformity‑assessment route (Art. 52 MDR)

| Device class | Applicable route(s) | NB involvement |
|--------------|---------------------|----------------|
| **Class IIb** (hardware) | **Art. 52(4)** – either:<br>• **Annex IX** full quality‑management‑system + technical‑documentation assessment *or*<br>• **Annex X** type‑examination **+ Annex XI** production conformity verification | Yes – NB review required. |
| **SaMD (Class IIa/IIb)** | Same routes as above, chosen per the final class determination. | Yes – NB review required. |

*Citation: Art. 52(4) governs Class IIb devices; Annex IX alone or Annex X + XI are the permitted routes.*

**Recommended route:**  
- **Annex IX** (QMS + technical‑documentation assessment) for the X‑ray unit, because it enables a single NB audit covering both hardware and bundled SaMD. The manufacturer should still prepare a type‑examination dossier under Annex X as a backup if future market‐entry strategies change.

---

### 4. Mandatory evidence & documentation  

| Deliverable (Regulatory reference) | Core content required |
|------------------------------------|-----------------------|
| **Technical Documentation** – Annex II §§1‑6 | Device description, intended use, labeling (Annex I §23), design & manufacturing information, risk management file (ISO 14971 2019), verification & validation data, GSPR compliance matrix. |
| **General Safety & Performance Requirements (GSPR) checklist** | Mapping to Annex I §§1‑23; special attention to:<br>• **§16** – protection against ionising radiation<br>• **§17** – electronic programmable systems / software<br>• **§3** – risk‑management system (ISO 14971)<br>• **§23** – labeling & IFU. |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | State‑of‑the‑art literature review, clinical data from equivalent devices, justification of equivalence, benefit–risk analysis (Art. 61). |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** – Annex XIV Part B | Planned post‑market studies, monitoring of radiation dose, software performance, adverse events; final PMCF evaluation report. |
| **PMS system** – Art. 83 | Organisation, processes, and resources for continuous surveillance. |
| **PMS Plan** – Art. 84 | Description of data collection, trending, and periodic safety update reporting. |
| **Periodic Safety Update Report (PSUR)** – Art. 86 | Annual PSUR (Class IIb) containing: <br>• Benefit‑risk conclusions<br>• Main PMCF findings<br>• Sales volume & usage population estimates. |
| **EU Declaration of Conformity** – Art. 19 / Annex IV | Signed declaration referencing the above documents and conformity‑assessment route. |

---

### 5. Evidential gaps (information still required)

1. **Exact intended‑use wording** for both hardware and SaMD – essential to confirm final class of the software (Rule 11).  
2. **Labeling & IFU content** (Annex I §23) – draft needed to verify compliance with information‑supplied requirements.  
3. **Risk Management File** – a complete ISO 14971‑based RMF, including identified radiation‑specific hazards and mitigations (§16).  
4. **Clinical data** – either: <br>• Clinical investigation results for the specific X‑ray unit, or <br>• Sufficient equivalence justification with published clinical evidence (state‑of‑the‑art literature).  
5. **Software validation & verification reports** (IEC 62304 2006+A1:2015) – to satisfy Annex I §17 and GSPR mapping.  
6. **Usability evaluation** (IEC 62366‑1 2020) – especially for lay‑person use scenarios (§22).  
7. **Manufacturing process controls & traceability** – required for Annex IX technical‑documentation assessment.  

*All items above are not present in the provided source excerpts; they must be supplied by the manufacturer before the NB audit.*

---

### 6. Key risk‑control measures (link to GSPR)

| Risk aspect | GSPR reference | Typical control |
|-------------|----------------|-----------------|
| **Ionising radiation exposure** | §16 – protection against radiation | Shielding design, dose‑monitoring circuits, compliance with IEC 60601‑2‑54 (radiography) and IEC 60601‑2‑28 (tube assemblies). |
| **Software malfunction / misdiagnosis** | §17 – electronic programmable systems; §11 (Rule) for SaMD classification | IEC 62304 lifecycle processes, verification/validation test plans, cybersecurity safeguards (IEC 82304‑1 where applicable). |
| **Use‑error by lay operators** | §22 – devices intended for lay persons | Human‑factors engineering (IEC 62366‑1), clear IFU, training modules. |
| **Residual risk outweighing benefit** | §8 – overall benefit–risk assessment | Formal residual‑risk analysis documented in the RMF; benefit justification in CER. |
| **Transport & storage hazards** | §§6‑7 – transport and storage | Packaging specifications, temperature/humidity limits, handling instructions. |

---

### 7. Human‑escalation triggers (when to involve senior RA / NB)

| Trigger condition | Action required |
|-------------------|------------------|
| Missing or ambiguous **intended‑use statement** for either component. | Escalate to product owner & senior RA for clarification before any classification finalisation. |
| No **clinical evidence of equivalence** (or insufficient literature) found within 3 months of deadline. | Raise a non‑conformity; consider undertaking a clinical investigation or seeking an alternative predicate. |
| Incomplete **risk‑management file** – especially radiation‑specific hazard analysis. | Immediate escalation to risk‑management lead for remediation. |
| Unclear **software classification** (potentially Class IIb/III) after assessing intended use. | Escalate to senior RA and possibly the Notified Body for early advice on appropriate conformity route. |
| Failure to produce a **draft PSUR** within 6 weeks of data collection cut‑off. | Trigger project‑management escalation; involve compliance officer to ensure Art. 86 timelines are met. |

---

### 8. Summary judgment

- The X‑ray emitting hardware is **Class IIb** under **Rule 10** (diagnostic ionising‑radiation device).  
- The associated SaMD falls under **Rule 11**; likely **Class IIa**, but final class depends on the precise diagnostic impact described in the intended‑use statement.  
- The appropriate conformity‑assessment route is **Annex IX** (full QMS + technical‑documentation assessment) for both components, with an optional Annex X + XI pathway as a contingency.  
- A complete set of MDR‑required deliverables (technical file, GSPR checklist, CER, PMCF plan/report, PMS system & plan, annual PSUR) must be compiled; current gaps are identified above and trigger the escalation points listed.

---

**Peer‑review request:**  
> @RA‑colleague – please challenge the assumptions regarding the SaMD’s provisional Class IIa classification, verify that Rule 11 applies as interpreted, and confirm that no additional MDR annexes (e.g., Annex XV for implantables) are inadvertently relevant. Also check for any jurisdiction‑specific nuances missed in the source material.

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

> 심각 결함 없음. Rule 10 IIb·Rule 11 상향 구조·52(4) IX 또는 X+XI·PSUR 'Annual (Class IIb)'·GSPR §3/16/17/23 전부 정확 — PSUR 오염 종결 1호 증거.

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261124-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c93a251fee55438e", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c93a251fee55438e`
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

> **Regulatory Draft – Classification, Conformity‑Assessment Route & Evidential Requirements  
(Prepared for EU MDR 2017/745)**  

---

### 1. Intended‑Use Clarification (required before any classification)
| Item | What is needed | Why it matters |
|------|----------------|----------------|
| **Full intended purpose / indication** | Precise wording of the medical purpose, target patient group, physiological or anatomical site, mode of action (diagnostic, therapeutic, monitoring, etc.). | Determines which *Annex VIII* rule applies; the MDR requires the manufacturer to perform self‑classification under **Article 51** and **Annex VIII**. |
| **Device characteristics** | Sterility status, presence of a measuring function, re‑usable surgical nature, software component, active vs. passive, tissue/cell origin. | Affects class (e.g., Is/Im/Ir for sterile or measuring devices) and may trigger the need for a Notified Body even for Class I. |
| **Risk‑related claims** (e.g., “provides life‑supporting therapy”) | Must be identified to apply the appropriate rule (Rule 9, 10, 11, 17). | Determines whether the device falls into Class IIa/IIb/III. |

> **Action:** Obtain a signed intended‑use statement from product management.  

---

### 2. Preliminary Classification Workflow  
1. **Apply Annex VIII rules sequentially** (highest rule that matches determines the class) – per **Article 51 + Annex VIII** and the self‑classification responsibility of the manufacturer (source [2]).  
2. **If doubt remains** → seek advice from the Competent Authority (CA) or consult the MDCG “Manual on Borderline and Classification” (latest version v2.1.1, 2023‑09).  

| Possible outcomes | Corresponding MDR route (Art. 52) |
|-------------------|-----------------------------------|
| **Class I (non‑sterile, non‑measuring, non‑reusable surgical)** | Self‑declaration; technical documentation + EU Declaration of Conformity (**Art. 19**, Annex IV). No NB required. |
| **Class Is / Im / Ir** | **Art. 52(7)** – limited NB involvement (Annex IX Chapters I & III or Annex XI Part A). |
| **Class IIa** | **Art. 52(6)** – full QMS + technical‑documentation assessment by a Notified Body under **Annex IX**, or alternative route via **Annex II/III + Annex XI §10** (if applicable). |
| **Class IIb** | **Art. 52(4)** – NB assessment under **Annex IX** *or* Type‑Examination (**Annex X**) combined with production conformity verification (**Annex XI**). |
| **Class III** | **Art. 52(3)** – NB assessment **Annex IX** *or* Type‑Examination (**Annex X**) + Production verification (**Annex XI**). |

> **Action:** Map the identified rule to the above table; if the device lands in Class IIa or higher, engage a Notified Body early.  

---

### 3. Evidence Package Required for the Chosen Route  

| Evidence | MDR reference (framework) | Minimum content |
|----------|---------------------------|-----------------|
| **Device description & specifications** | Annex II §1‑2 | Intended purpose, variants, accessories, UDI allocation. |
| **Risk Management File** | Annex I §3 (GSPR) + ISO 14971:2019 | Risk analysis, evaluation, controls, residual risk justification. |
| **Clinical Evaluation Report (CER)** | **Article 61** ; **Annex XIV Part A** | State of the art, clinical data, benefit‑risk determination – kept current. |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | **Annex XIV Part B** | Plan for prospective data collection; summary of findings. |
| **Post‑Market Surveillance (PMS) system** | **Art. 83** (system), **Art. 84** (plan) | Continuous monitoring, trending, corrective actions. |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | **Art. 86** | Benefit‑risk conclusions, PMCF results, sales volume & user population; annual for IIb/III, ≤ 2‑yearly for IIa. |
| **EU Declaration of Conformity (DoC)** | **Art. 19** (content in Annex IV) | Manufacturer details, device identification, conformity assessment route, NB number (if applicable). |
| **Labeling & IFU** | Annex I §23 | Symbols, warnings, instructions per GSPR. |
| **UDI registration in EUDAMED** | Art. 33‑39 (EUDAMED obligations) | UDI‑Device entry, Basic‑Udi‑Device‑ID, public summary of safety & performance (for IIb/III). |
| **Authorized Representative (AR)** details | **Art. 11** | Name, address, and responsibilities; necessary for any device placed on the EU market by a non‑EU manufacturer. |

> **Missing Information Flags** – see Section 4.  

---

### 4. Gaps Identified from Current Source Material  

| Gap | Why it matters | Suggested remedial step |
|-----|----------------|------------------------|
| **Exact intended use / indication** | Without this the correct Annex VIII rule and class cannot be confirmed. | Obtain a formal Intended‑Use Statement (see Section 1). |
| **Device’s sterility/measurement/reusability status** | Determines whether Class Is / Im / Ir applies (NB involvement). | Provide manufacturing process description & labeling claims. |
| **Presence of software or active components** | May trigger Rule 11 (software) or Rule 9/10 (active devices), moving the device to a higher class. | Supply software architecture description, IEC 62304 scope, and intended decision impact. |
| **Clinical data source list** | Required for CER (§ Annex XIV Part A). | Compile pre‑market clinical investigations, literature search matrix, and any existing CE‑marked predicate data. |
| **PMCF plan draft** | Needed for Annex XIV Part B; especially mandatory for Class IIa+. | Draft a PMCF protocol outlining objectives, endpoints, follow‑up schedule. |
| **PMS system description** | Art. 83/84 require an established PMS framework before market entry. | Create PMS SOPs, reporting timelines, and assign responsibilities. |
| **UDI strategy & EUDAMED entry status** | Mandatory for all devices placed on the EU market; absent UDI leads to non‑conformity. | Define Issuing Agency (e.g., GS1), generate DIs, register in EUDAMED. |
| **Authorized Representative appointment** | Required under Art. 11 when manufacturer is outside the EU. | Identify and contract an AR; capture their contact details for DoC. |
| **Notified Body selection (if class ≥ IIa)** | Early NB involvement prevents later re‑work. | Shortlist NB(s) accredited for the relevant device type, request quotation & audit schedule. |

> **Action:** Prioritize gaps that block classification (intended use, sterility/measuring status).  

---

### 5. Core Risk Controls to be Demonstrated  

| Control | MDR/GSPR reference | Implementation notes |
|---------|--------------------|----------------------|
| **Risk Management System** – plan, analysis, evaluation, control, monitoring | Annex I §3 (risk management) + ISO 14971:2019 | Document all identified hazards; verify that residual risk is acceptable per the benefit‑risk analysis in the CER. |
| **Design Verification & Validation** | Annex II §5 (verification) / §6 (validation) | Conduct bench testing, biocompatibility (ISO 10993‑1), software verification (IEC 62304). |
| **Usability Engineering** | Annex I §17 (electronic programmable systems) + IEC 62366‑1:2020 | Apply formative and summative usability tests; address use‑error risks (§5). |
| **Labeling & IFU Compliance** | Annex I §23 | Ensure all warnings, contraindications, and instructions meet the essential safety requirements. |
| **Sterility Assurance (if applicable)** | Annex I §19 (active implantable) / relevant ISO/IEC sterilization standards | Provide validated Sterilisation Process Validation Report. |
| **Electrical Safety & EM Compatibility** (for active devices) | Annex I §16 (radiation) & IEC 60601‑1 series | Perform EMC and safety testing; keep test reports in the technical file. |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger for escalation to senior RA / legal / management |
|-----------|----------------------------------------------------------|
| **Unclear classification** (multiple Annex VIII rules appear applicable) | Escalate to senior regulatory lead + request Competent Authority clarification per Article 51. |
| **Class IIa or higher identified** and no Notified Body contract in place | Immediate escalation to project manager to initiate NB selection & budget approval. |
| **Clinical evidence gaps** (no adequate pre‑market data for CER) | Escalate to clinical affairs team; consider additional clinical investigation before submission. |
| **Missing AR appointment** when manufacturer is non‑EU | Alert legal/compliance to secure an AR, else market entry impossible under Art. 11. |
| **PMS system not operational at launch** (Art. 83/84) | Stop release; inform quality assurance and senior management; reassess launch timeline. |
| **UDI registration incomplete in EUDAMED** close to planned CE‑marking date | Raise to product owner; risk of non‑compliance with Art. 33‑39. |
| **Adverse event reporting obligations not met** (e.g., no vigilance procedure per Art. 87) | Immediate notification to the Vigilance Unit and escalation to senior compliance officer. |

---

### 7. Summary Judgment  

*Based on the information supplied, the device’s classification cannot be finalised until the manufacturer provides a detailed intended‑use statement, sterility/measurement status, and any software or active component description.*  
- **If the resulting rule leads to Class I (non‑sterile, non‑measuring, non‑reusable surgical)** → self‑declaration route (**Art. 19**, Annex IV).  
- **If any of Is, Im, Ir, IIa, IIb or III criteria apply** → a Notified Body assessment is mandatory following the MDR routes outlined in **Article 52** (Annex IX for most classes; Annex X + XI for Class IIb/III).  

All required evidence listed in Section 3 must be compiled, gaps addressed per Section 4, and risk controls established as per Section 5 before any conformity‑assessment audit is scheduled.

---

### 8. Peer‑Review Prompt  

*Colleague, please review the following assumptions and coverage:*  

1. **Classification assumption:** I have interpreted the manufacturer’s self‑classification responsibility strictly under Article 51 + Annex VIII. If you see a need to reference additional borderline guidance (e.g., MDCG 2023‑02) beyond what is captured, let me know.  
2. **Evidence completeness:** Are any MDR annexes or Articles omitted that are critical for the device type we may encounter (e.g., specific requirements for implantables, radiological devices, or software)?  
3. **Jurisdictional gaps:** The source mentions Korean Medical Device Act §31 and US 21 CFR 803/MedWatch – ensure these do not obscure EU obligations; confirm that no EU‑specific guidance (MDCG 2022‑10 on clinical evaluation) is missing from the list.  
4. **Risk‑control mapping:** Verify that all relevant GSPR sections are linked to appropriate standards (ISO 14971, IEC 62304, etc.) and flag any additional controls required for high‑risk classes.

*Please provide your feedback so we can finalize the regulatory strategy.*

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

> GSPR 오귀속 3건: ① 사용적합성(IEC 62366-1)을 §17(소프트웨어)에 매핑(사용적합성은 §5) ② 전기안전·EMC를 §16(방사선)에 매핑 ③ 'Annex II §5 (verification)' — §5는 benefit-risk/위험관리. Art.52 전표·PSUR 'annual for IIb/III, ≤2-yearly for IIa'는 정확.

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261124-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e582db707cc080c3", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md", "source_hash": "83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e582db707cc080c3`
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

> **Regulatory Draft – Classification & Conformity Route for an AI‑enabled SaMD (MDR scope)**  

---

### 1. Device Synopsis (to be completed by the Manufacturer)  
| Item | Comment / Evidence Needed |
|------|----------------------------|
| **Product name / model** | – |
| **Device type** | Software as a Medical Device (SaMD) that incorporates AI‑enabled functions (e.g., diagnostic decision support). |
| **Intended purpose** | Precise wording of the clinical indication, target patient population, and mode of use (stand‑alone software, accessory to hardware, etc.). |
| **Clinical claim** | Whether the software provides *diagnostic* or *therapeutic* advice, or merely data aggregation. |
| **Relevant EU legislation** | Regulation (EU) 2017/745 MDR – Annex I (device falls under “medical device”).<br>AI Act (Regulation (EU) 2026/1744) – Chapter III requirements apply when the AI system is deemed high‑risk. |

*Missing information:* a formal Intended Use statement and any claims that may trigger a higher classification rule (e.g., Rule 9, 10, or 11).  

---

### 2. Primary Classification under MDR  

| Step | Determination | Regulatory Basis |
|------|---------------|-------------------|
| **Step 1 – Is the product a medical device?** | Yes (AI‑enabled software used for diagnosis/therapy). | Annex I, Section A point 11 of the MDR (Regulation (EU) 2017/745). |
| **Step 2 – Identify class by applicable rule** | Likely **Class IIa** or **IIb** (see note below). | Classification rules in Annex VIII; for AI‑enabled SaMD the default is Rule 11 (software providing information for diagnostic/therapeutic decisions). If the software’s output may cause serious health deterioration, Class IIb or III applies. |
| **Step 3 – High‑risk AI determination** | Device is a “high‑risk AI system” → NB involvement required. | AI Act Art. 6(1) (high‑risk AI definition).<br>Source excerpt confirms: *Class IIa/IIb/III → High‑risk AI system (Art. 6(1))*【no specific identifier found in source — verify separately】. |
| **Step 4 – Special cases** | If the device were Class I (non‑sterile, non‑measuring, non‑reusable surgical instrument) it would be excluded from high‑risk AI unless Annex III triggers apply. | Art. 6(1) exclusion note in excerpt【no specific identifier found in source — verify separately】. |
| **Resulting class** | **Class IIa** (most common for diagnostic decision‑support software) *or* **Class IIb** where the AI output directly influences life‑sustaining treatment. The exact rule (Rule 11‑1 or Rule 11‑2) must be confirmed once intended use is finalised. | – |

*Human escalation trigger:* if the Intended Use indicates a therapeutic intervention with potential immediate danger, move to Class IIb/III and update the conformity route accordingly.

---

### 3. Conformity Assessment Route  

| Device class | Applicable MDR route (Art. 52) | Notified Body involvement |
|---------------|------------------------------|----------------------------|
| **Class IIa** | **Annex IX** – QMS + technical‑documentation assessment of a representative device. | Required (full NB review of TD). |
| **Class IIb/III** | **Annex IX** (full assessment) *or* **Annex X** + **Annex XI** (type‑examination & production conformity verification). | Required (NB involvement mandatory). |

*Note:* Because the AI Act Chapter III requirements are integrated into the MDR route, the same NB that assesses the MDR technical file will also evaluate compliance with the AI‑specific obligations.  

*Human escalation trigger:* any change of class after the initial assessment (e.g., discovery that the software controls a therapeutic device) must prompt re‑selection of the conformity route and possibly an Annex X + XI path.

---

### 4. Evidence Package Required for NB Review  

| Element | Minimum content (per MDR & AI Act) | Status / Gap |
|---------|------------------------------------|--------------|
| **Technical Documentation** – Annex II §§1‑6 (device description, design, GSPR fulfilment, risk management, verification/validation). | Complete when all sections are populated. | ‑ |
| **Risk Management File** – ISO 14971:2019 implementation (risk analysis, evaluation of AI‑specific risks, residual risk assessment) (§3 of Annex I). | Required. | • Need documented AI‐risk analysis (data quality, bias, robustness). |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A; kept current under Art. 61. | Clinical data demonstrating safety & performance for the intended purpose. | • Clinical evidence plan missing (clinical studies vs. literature). |
| **Post‑Market Surveillance (PMS) System** – Art. 83; PMS Plan – Art. 84. | PMS plan describing data collection, trend analysis, and reporting. | • Draft PMS plan not yet supplied. |
| **Periodic Safety Update Report (PSUR)** – Art. 86 (for Class IIa/IIb). | PSUR draft for first 2‑year cycle (or annual for IIb). | • Not applicable until after market launch. |
| **AI Act Chapter III Dossier** – conformity assessment of high‑risk AI (data governance, documentation, transparency, human oversight). | Evidence of compliance with AI‑specific requirements (e.g., data set sheets, testing protocols). | • No AI‑specific evidence yet; must be compiled. |
| **EU Database Registration** – Art. 49 AI Act. | Entry in the EU “AI database” (registration number to be obtained). | • Registration pending. |
| **Labeling & IFU** – Annex I §23 (information supplied with the device). | Clear user instructions, intended use, and AI‑specific warnings. | • Draft labeling required. |

*Human escalation trigger:* any missing element above constitutes a “stop” point before NB submission; the manufacturer must provide the evidence before proceeding.

---

### 5. Risk Controls & GSPR Alignment  

| GSPR clause (Annex I) | Required control for AI‑enabled SaMD | Evidence to be submitted |
|-----------------------|--------------------------------------|---------------------------|
| **§3 – Risk Management System** | Full ISO 14971 risk management, including AI‑specific hazard identification (data drift, algorithmic bias). | RMF with AI‑risk analysis. |
| **§4 – Risk Control Measures** | Implementation of data governance, validation of training datasets, periodic re‑training procedures, and fallback mechanisms (human‑in‑the‑loop). | Description of controls & verification results. |
| **§5 – Use‑error Risks** | Usability testing per IEC 62366‑1; mitigation of misinterpretation of AI output. | Usability engineering file. |
| **§6 – Device Lifetime** | Software update strategy, version control, and compatibility checks throughout device life. | Update policy & validation reports. |
| **§8 – Known/foreseeable risks vs. benefits** | Benefit‑risk analysis incorporating AI performance metrics (sensitivity, specificity) versus clinical risk of incorrect recommendation. | Benefit‑risk summary in CER. |
| **§16 – Protection against radiation** *(if software controls a radiological device)* | Not applicable unless the SaMD directly drives ionising‑radiation equipment; then compliance with IEC 60601‑2‑54 required. | • Verify applicability. |
| **§17 – Electronic programmable systems** | Compliance with IEC 62304 (software lifecycle) and IEC 62366‑1 (usability). | Software development file. |
| **§23 – Label & IFU** | Include AI transparency information (e.g., limited domain, performance metrics, user responsibilities). | Draft labeling. |

*Human escalation trigger:* if any GSPR cannot be demonstrated with current documentation (e.g., lacking usable usability test reports), the NB will request remediation before certification.

---

### 6. Summary of Regulatory Judgment  

1. **Device is an AI‑enabled SaMD subject to MDR** (Annex I, Section A point 11).  
2. **Likely classification:** Class IIa (or IIb if therapeutic impact is high). Confirmation requires final Intended Use and application of Rule 11 (software) – *verify separately*.  
3. **Conformity route:** Annex IX (full NB assessment); for higher classes an alternative Annex X + XI path exists but is not preferred unless specific type‑examination benefits are demonstrated.  
4. **High‑risk AI status** triggers additional obligations under the AI Act (Art. 6(1), Chapter III) and mandatory NB involvement (*see MDCG 2025‑6/AIB 2025‑1 Q2·Table 1* – instance identifier).  
5. **Key evidence gaps:** detailed Intended Use, classification rule justification, AI‑risk analysis, clinical evaluation data, PMS plan, AI Act compliance dossier, EU AI‑database registration (Art. 49).  

**Human‑Escalation Triggers** (must be raised to the Project Lead or Regulatory Manager before progressing):

- Missing or ambiguous Intended Use that could shift class to IIb/III.  
- Absence of a documented AI risk assessment aligned with Annex I §3–§8.  
- No evidence that the device meets AI Act Chapter III requirements (data governance, transparency).  
- Incomplete technical documentation (Annex II) or lack of a validated PMS plan (Art. 84).  
- Registration in the EU AI database not yet performed (Art. 49).  

---

### 7. Peer‑Review Prompt  

*Please review this draft and challenge the following points:*  

1. **Assumption that Rule 11 is the appropriate classification rule** – could another Annex VIII rule apply based on the device’s interaction with other medical devices or measurement functions?  
2. **Scope of AI Act high‑risk determination:** Are we correctly interpreting Art. 6(1) for Class IIa SaaMD, given the MDCG 2025‑6 guidance referenced?  
3. **Evidence package completeness:** Have any EU‑specific standards (e.g., IEC 62304, IEC 62366‑1) been omitted that a Notified Body would expect for an AI SaMD?  
4. **Potential jurisdictional gaps** – does the reference to Regulation (EU) 2026/1744 introduce additional obligations beyond those covered in the MDR and AI Act (e.g., specific conformity assessment annexes)?  

Your feedback will help verify that all regulatory angles are captured before we proceed to the Notified Body.

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

> 심각 결함 없음. Rule 11 티어·PSUR '(or annual for IIb)' 정확·§16 해당없음 처리·§17-62304. 미세: 'Rule 11-1 or Rule 11-2' 비표준 표기(indent 구조)·§17 행에 62366-1 병기.

**Source Excerpts**

1. Chunk `1013595113860735371`

> ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은 NB 관여 → **Art.6(1) 해당** (MDCG 2025-6/AIB 2025-1 Q2·Table 1) └─ No: Annex III 별도 해당 여부 확인 2. High-risk 확정 시 ├─ AI Act Chapter III 전체 요건 적용 ├─ 적합성평가 경로: MDR 경로에 AI Act 요건 통합 └─ EU DB 등록 의무 (Art. 49) ``` **판정 기준**: 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높다.

2. Chunk `1015646396132986584`

> lan for AI-Enabled Device Software Functions (Final; 2025-08-18 현재 본; Docket FDA-2022-D-2628; original final issued December 2024)"으로 갱신. 범위를 ML→**AI-enabled device software functions 전반**으로 보정. FDA Guidance 페이지(2025-08-18 current)로 직접 재확인. 사내 SOP-AIGOV-001 v0.3 "FDA PCCP Guidance 2024" 표기와 정합 회복 | | v0.9 | 2026-09-11 | **P0 사실성 정정 (audit #1041)** — Regulation (EU) 2026/1744(Digital Omnibus on AI, 채택 2026-07-08 / OJ 2026-07-24 / 발효 2026-07-27, CELEX 32026R1744) 확정 반영. §3 일정표에 발효일·Annex III 2027-12-02·Annex I 2028-08-02 행 신설, '잠정 합의 시·예상·미완료' 조건부 표현 전량 제거. §12.2 시나리오 (A)/(B) 분기를 (A) 확정으로 종결하고 (B) 트랙 삭제, 기준일을 2028-08-02로 재설정. §12 D-36 D-day·...

### kb-eval-20261124-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "85c9e4eb65f45a91", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `85c9e4eb65f45a91`
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

> **Regulatory Draft – X‑ray (ionising‑radiation) Medical Device**

---

### 1. Classification & Conformity Assessment Route  

| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Device class** | **Class IIb** (or higher, as indicated by the source) | MDR 2017/745 – classification rule **Rule 10 (radiology limb)** for active devices that emit ionising radiation for diagnostic purposes (Annex VIII). |
| **Conformity‑assessment route** | **Annex IX** (full quality‑management‑system + technical‑documentation assessment by a Notified Body) | Art. 52(4) MDR – Class IIb requires the Annex IX route with NB involvement. |
| **Notified‑Body requirement** | Mandatory NB certification | Source excerpt: “Class IIb 이상 → NB 인증 필수.” (no specific identifier in source – verify separately). |

---

### 2. Evidence Required for a Complete Submission  

| Evidence | Where it belongs in the Technical Documentation (TD) | Relevant MDR provision |
|----------|-----------------------------------------------------|------------------------|
| **Device description & intended purpose** (including indications, contraindications, user profile) | Annex II §1 – “Device description”, §2 – “Intended purpose” | Art. 10(9), Annex II |
| **Design & manufacturing information** (drawings, specifications, Bills of Materials, manufacturing processes) | Annex II §3 | Art. 10(9) |
| **Risk Management File (RMF)** (risk analysis, evaluation, control measures, residual risk assessment) | Annex II §5; implements ISO 14971:2019 (Chapter I §3) | Art. 10(9), Annex I §3‑§8 |
| **General Safety & Performance Requirements (GSPR) compliance** – demonstrable fulfilment of §§1‑23, especially:<br>• §16 (radiation protection)<br>• §17 (software if present)<br>• §22 (use by lay persons) | Annex II §4 (demonstration of GSPR) | Annex I |
| **Clinical Evaluation Report (CER)** – systematic review of state‑of‑the‑art literature, clinical data, and benefit–risk analysis | Annex II §6.1; Annex XIV Part A | Art. 61, Annex XIV Part A |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex II §6.1 (clinical evaluation) and Annex XIV Part B | Art. 83–86 (PMS system/plan, PSUR for Class IIb – annual) |
| **Post‑Market Surveillance (PMS) System & Plan** | Annex III (PMS technical documentation) | Art. 83 (system), Art. 84 (plan) |
| **Periodic Safety Update Report (PSUR)** – annual for Class IIb | Annex III (for higher classes) | Art. 86(1)/(2) – annual update for Class IIb |
| **QMS documentation** (ISO 13485:2016‑based, with NR‑specific procedures) | Annex IX §2 – QMS audit evidence | Art. 10(9), Annex IX |
| **Labeling & IFU** (including radiation safety information, dose limits, user instructions) | Annex II §6.3 and Annex I §23 | Annex I §23 |
| **Declaration of Conformity (DoC)** – signed by manufacturer, containing required content | Annex IV (content), Art. 19 | — |

---

### 3. Gaps / Missing Information (to be obtained before final submission)

1. **Exact intended‑use statement** (clinical indication, patient population, user environment).  
2. **Detailed device architecture** – identification of all sub‑assemblies (X‑ray tube, generator, detector, software) and their respective classification per Rule 10 / Rule 11.  
3. **Risk analysis results** for radiation exposure (dose calculations, shielding effectiveness) aligned with GSPR §16.4.  
4. **Clinical data package** – either: <br>• a fully justified clinical investigation under MDR Art. 62‑63; or <br>• sufficient comparable device data (with justification of equivalence). No such data are referenced in the source.  
5. **PMCF plan** – objectives, endpoints, sampling strategy, timeline. Absence of a documented PMCF plan is a non‑conformity risk.  
6. **PMS system description** – processes for trend analysis, field safety corrective actions (FSCA) per Art. 87.  
7. **Usability engineering evidence** (IEC 62366‑1) if device is intended for use by lay persons or in high‑stress environments; not mentioned.  
8. **Software documentation** (if any) – IEC 62304 compliance, software classification under Rule 11, and cybersecurity considerations (Annex I §17).  
9. **Evidence of NB pre‑selection** – the source lists candidate NBs but does not provide a signed selection contract or audit results.  

*All items above must be collected, assessed and incorporated into the TD before the Notified Body can issue an assessment report.*

---

### 4. Required Risk Controls (mapped to GSPR)

| GSPR clause | Control measure for X‑ray device |
|-------------|-----------------------------------|
| **§3 – Risk Management System** | ISO 14971:2019 risk management file covering hazard identification, estimation of radiation dose, and residual risk evaluation. |
| **§4 – Risk control measures** | Engineering controls (shielding, interlocks), administrative controls (training, maintenance schedule), verification of dose limits per IEC 60601‑2‑54. |
| **§5 – Use‑error related hazards** | Human factors analysis (IEC 62366‑1) & clear labeling (Annex I §23). |
| **§6 – Device lifetime** | Specification of service life, routine performance checks, replacement intervals for tube and detector. |
| **§7 – Transport & storage** | Protective packaging to avoid mechanical damage to tube; compliance with IEC 60601‑1 transport requirements. |
| **§8 – Benefit–risk determination** | Documented in CER & RMF – quantitative comparison of diagnostic benefit vs. radiation risk. |
| **§16 – Radiation protection** | Compliance with IEC 60601‑2‑54, dose monitoring, warning indicators, and user training on ALARA principle. |
| **§17 – Software (if applicable)** | Development lifecycle per IEC 62304; verification & validation of software functions that influence radiation output. |
| **§22 – Devices for lay persons** *(if relevant)* | Instructional videos, simple UI, mandatory safety prompts. |

---

### 5. Human‑Escalation Triggers  

| Situation | Action required (who) | Reason / Reference |
|-----------|----------------------|---------------------|
| **Uncertain classification** (e.g., component of the system might be only Class IIa) | Senior Regulatory Lead → seek clarification from NB or submit a classification request to the Competent Authority. | MDR Art. 52, Annex VIII Rule 10. |
| **Missing clinical evidence** (no CE‑marked predicate nor robust literature) | Clinical Affairs Manager → design and execute a clinical investigation under MDR Art. 62‑63. |
| **No finalized PMCF plan** | Post‑Market Surveillance Lead → draft PMCF plan, obtain sign‑off before TD submission. |
| **QMS audit findings not resolved** | Quality Manager → remedial actions & re‑audit; report to NB as “Non‑conformity response”. |
| **NB contract not signed or scope not confirmed** | Project Manager → finalize selection with one of the listed NBs (TÜV SÜD, BSI, etc.) and obtain a written audit agreement. |
| **Risk Management File incomplete** | Risk Manager → complete hazard analysis for radiation dose; update RMF. |
| **Labeling/IFU not yet compliant with Annex I §23 & IEC 60601‑2‑54** | Documentation Owner → produce final labeling package, perform user‑testing. |
| **Any “no specific identifier found in source — verify separately” item** | Regulatory Analyst → retrieve the exact MDR article or NB decision number from the appropriate database (e.g., Official Journal) before final dossier compilation. |

If any of the above triggers are hit, the project must be paused until corrective evidence/documentation is supplied and verified.

---

### 6. Summary Judgment  

- The device is **Class IIb** under MDR Rule 10 (radiology limb).  
- **Annex IX** is the mandatory conformity‑assessment route; a Notified Body must assess the technical documentation.  
- A complete submission requires the full set of evidence listed in Section 2, with particular emphasis on clinical evaluation, risk management (radiation safety), and an approved PMCF plan.  

All identified gaps must be addressed before the Notified Body can issue a Technical Documentation Assessment report.

---

### 7. Peer‑Review Prompt  

> **To RA colleagues:** Please review the assumptions made regarding classification (Rule 10) and the completeness of the evidence list. Confirm whether any additional MDR provisions (e.g., specific requirements for implantable X‑ray components, or Article 78 supplementary obligations) apply to this device. Also verify that the listed NBs are indeed designated for the relevant MD codes in the current NANDO database.  

---

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

> 심각 결함 없음. Rule 10·Annex II §3/§4/§6.1 매핑 정확·PSUR IIb annual·Art 10(9). 미세: '52(4) requires the Annex IX route' — IX는 선택 경로(X+XI 대안 존재, requires는 과잉)·'Annex II §6.3' 라벨 근거 불명.

**Source Excerpts**

1. Chunk `978896205875274621`

> ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수).

2. Chunk `296791090431458058`

> ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료

### kb-eval-20261124-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d2d7fb45178625b2", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d2d7fb45178625b2`
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

> **Regulatory Draft – Classification & Conformity‑Assessment Strategy for a Diagnostic X‑ray Device**

| Item | Assessment / Requirement | Rationale & Supporting Regulation |
|------|--------------------------|-----------------------------------|
| **1. Intended Use** | “Standard diagnostic radiology” (e.g., projection radiography, fluoroscopy). | Derived from the source excerpt [1] (“Both indicated for standard diagnostic radiology”). |
| **2. Device Class** | **Class IIb** – Active device that *emits ionising radiation* for diagnostic purposes. | Classification rule: **Rule 10 (radiology limb)** of Annex VIII (active devices emitting ionising radiation). → Class IIb. |
| **3. Conformity‑Assessment Route** | **Annex X (type‑examination) + Annex XI (production conformity verification).** | Art. 52(4) states that Class IIb devices may follow the *type‑examination* route together with production verification (Annex X + XI). |
| **4. Core Technical Documentation (Annex II §1‑6)** | • Device description & specifications<br>• Intended purpose statement<br>• Design & manufacturing information<br>• GSPR compliance matrix (Annex I)<br>• Risk Management File (ISO 14971:2019) <br>• Verification & validation results | Required by Annex II. No specific source excerpt supplies these items – they must be assembled by the manufacturer. |
| **5. Clinical Evaluation Report (CER)** | • Rev. 3 of the CER (referenced in source [1] as “Annex A”).<br>• Demonstration of clinical equivalence: same clinical condition + DQE ≥ 65 % (IEC 62220‑1‑1). | Clinical evaluation requirement – Annex XIV Part A; the source provides a quantitative equivalence criterion (DQE ≥ 65 %). |
| **6. Performance Testing Evidence** | • Test Report TR‑2024‑015 (IEC 62220‑1‑1) confirming DQE ≥ 65 % for both devices.<br>• Additional IEC 60601‑2‑54 compliance data (electrical safety, radiation protection). | The DQE test is explicitly cited in source [1] together with the standard reference. |
| **7. Risk Management** | • RMF following ISO 14971:2019 (risk analysis, control measures, residual risk evaluation).<br>• Specific controls for ionising‑radiation hazards (Annex I §16.4) and active device safety (Annex I §18). | Required by Annex I §§3‑8 and by the QMS obligations of Art. 10(9). |
| **8. Post‑Market Surveillance (PMS)** | • PMS System per Art. 83.<br>• PMS Plan (Art. 84) including PMCF activities.<br>• Periodic Safety Update Report (PSUR) – annual for Class IIb per Art. 86(1)/(2). | Mandatory for all devices; cadence defined in Art. 86. |
| **9. Declaration of Conformity** | EU Declaration of Conformity (Art. 19, content listed in Annex IV). | Must be issued after successful NB assessment. |
| **10. Labeling & IFU** | Information supplied with the device per Annex I §23 – includes intended use, contraindications, radiation safety instructions, and DQE performance claim. | Required GSPR element. |
| **11. Notified Body (NB) Interaction** | • Submission of a *Deficiency Letter* response when NB raises “결함·불명확·누락 사항” (source [2] defines the term).<br>• Provide missing/unclear documentation identified by NB. | The source explains that a deficiency letter is the EU MDR equivalent of FDA “Additional Information Request”. |
| **12. Missing / Incomplete Information** (to be supplied before NB sign‑off) | • Full Intended Use & Indications Statement (detailed clinical context).<br>• Complete GSPR compliance matrix.<br>• Risk Management Report with residual risk justification.<br>• PMS Plan and schedule for PMCF.<br>• Label draft and IFU in the required language(s).<br>• Evidence of conformity with IEC 60601‑2‑54 (electrical safety) and IEC 60601‑2‑28 (X‑ray tube assembly). | These items are not present in the provided excerpts; they are mandatory per Annex II, Annex I, Art. 83–86, and relevant harmonised standards. |
| **13. Human‑Escalation Triggers** | • *Trigger 1*: NB issues a Deficiency Letter (source [2]) → Manufacturer must prepare a formal response within the stipulated timeframe (usually 30 days) and supply all missing artefacts.<br>• *Trigger 2*: Incomplete clinical equivalence data (e.g., lack of comparable DQE testing on the reference device) → Require additional bench‑testing or clinical study before CER can be closed.<br>• *Trigger 3*: Unresolved GSPR gaps after the first NB review → Escalate to senior regulatory manager for risk‑benefit reassessment and possible redesign. | Defined by the conformity‑assessment process; any NB‑raised non‑conformity must trigger a documented corrective action plan. |
| **14. Final Regulatory Judgment** | The device is a **Class IIb diagnostic X‑ray system** requiring **Annex X + XI** assessment, a complete **CER demonstrating clinical equivalence (DQE ≥ 65 %)**, full **risk management**, and an operational **PMS/PMCF programme** before the EU‑CE mark can be issued. | – |

---

### Peer‑Review Prompt
> *Please review this draft and challenge any of the following:*
> 1. The assumption that Rule 10 (radiology limb) automatically yields Class IIb for all diagnostic X‑ray equipment – are there any nuances in the device’s specific functionality that could alter the class?
> 2. Completeness of the listed missing documentation – have we omitted any mandatory Annex II or Annex I elements, especially concerning software (Rule 11) if the system includes image‑processing algorithms?
> 3. The adequacy of the identified evidence (DQE ≥ 65 % from IEC 62220‑1‑1) for clinical equivalence – does MDR require additional clinical data beyond bench performance when a reference device is used?
> 4. Any jurisdiction‑specific gaps, such as EUDAMED registration steps or specific timelines for PSUR submission that may affect the overall schedule.

*Your feedback will be incorporated to refine the regulatory strategy before next NB interaction.*

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

> 심각 결함 없음. 52(4) X+XI·PSUR IIb annual·§16.4·§18 능동기기 안전 매항 정확·Deficiency Letter↔AI 요청 비교는 소스 기반. 미세: 60601-2-54를 'electrical safety'로 압축.

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1107467848736309543`

> ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통지하는 문서. 국내 MFDS "보완 요청", FDA "Additional Information (AI) Request"에 해당하는 EU MDR 용어. ---

## ra_kr

### kb-eval-20261124-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "4ac3ca3252a90e00", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `4ac3ca3252a90e00`
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

### 1. Device Overview
| Item | Description |
|------|-------------|
| **Device name** | 촬영실 GUI Software (Graphical User Interface for imaging‑room equipment) |
| **Intended use** | To provide operator control and display of imaging parameters, workflow coordination and image preview in radiology suites. May incorporate generative‑AI functions for parameter recommendation. |
| **Regulatory grade** | 2등급 medical device – **인증** pathway (possible combined review under the Digital Medical Products Act).<br>_Citation_: “의료기기 품목 및 품목별 등급에 관한 규정” (MFDS 고시)【1】 |

### 2. Submission Route
| Pathway | Responsible body | Typical documents |
|---------|------------------|-------------------|
| **인증** (Technical‑document review by MFDS‑designated 심사기관 – e.g., KTL, KTC, KTR) | MFDS‑designated 심사기관 | • Technical dossier  <br>• KGMP facility certification (if applicable) <br>• Software documentation (lifecycle, risk, usability, cyber security) |
| **Digital Medical Products Act** (optional “병용 검토”) | MFDS + Digital Medical Products Committee | Same core documents plus a statement of alignment with the AI‑related guidance.  |

*The default track for a 2등급 device is 인증; the digital‑medical‑product route may be used when AI functions are present (see §10.3 of source).*

### 3. Core Evidence Required

| Category | Specific items | Regulatory basis |
|----------|----------------|------------------|
| **Device classification** | Confirmation that the software falls under “2등급”. | 의료기기 품목 및 품목별 등급에 관한 규정【1】 |
| **KGMP compliance** (if production is performed in Korea) | KGMP certificate for the development/production site. | 의료기기 GMP 심사·평가 등에 관한 규정 (MFDS 고시)【1】 |
| **Software lifecycle** | • IEC 62304‑based Software Development Plan  <br>• Verification & Validation reports  <br>• Change Management Plan (especially for AI updates) | IEC 62304:2006+A1:2015 (current edition) |
| **Risk management** | • ISO 14971:2019 risk analysis file  <br>• Hazard log, risk control measures, residual risk justification | ISO 14971 (2019 edition) |
| **Usability / Human Factors** | IEC 62366‑1:2020 usability engineering process & testing results. | IEC 62366‑1 (2020 amendment) |
| **Cybersecurity** | • Compliance with MFDS 사이버보안 가이드라인 (refers to IEC 81001‑5‑1:2021)  <br>• Threat analysis, mitigation, security architecture documentation | IEC 81001‑5‑1 (2021 edition) |
| **AI-specific controls** (if generative AI is embedded) | • MFDS “생성형 AI 가이드라인” compliance evidence  <br>• Explainability & bias assessment reports  <br>• Post‑deployment monitoring plan for AI output | No specific notice number provided in source – verify separately. |
| **Performance / Clinical Evaluation** | • Bench testing (functional, performance, safety)  <br>• If clinical claims exceed bench limits, a Korean Clinical Evaluation Report (CER) or foreign CER that MFDS accepts under the relevant “foreign clinical evaluation” scope. | No specific MFDS notice number cited – verify separately whether foreign CER can be used for this device. |
| **Labeling & IFU** | • Korean‑language label (product name, intended use, contraindications, warnings)  <br>• Korean User Manual/Instruction for Use with full safety information. | 의료기기 허가·신고·심사 등에 관한 규정 – labeling requirements【1】 |
| **Post‑Market Surveillance (PMS)** | • PMS plan (시판후조사), adverse event reporting process, periodic safety update schedule. | 의료기기 허가·신고·심사 등에 관한 규정【1】 |

### 4. Missing Information / Gaps to be Obtained
| Gap | Why needed |
|-----|------------|
| **Exact intended use statement** (including AI function description) | Determines classification confirmation and clinical data scope. |
| **Detailed software architecture diagram & module list** | Required for IEC 62304 compliance review. |
| **Risk Management File (RMF)** – complete hazard analysis, risk control matrix, residual risk assessment. | Mandatory per ISO 14971. |
| **Usability testing protocol & results** (including participant demographics). | Needed to satisfy IEC 62366‑1. |
| **Cybersecurity threat model and mitigation evidence** | Required by MFDS cyber‑security guideline. |
| **AI compliance documentation** (e.g., alignment with “생성형 AI 가이드라인”). | AI‑specific pathway may trigger additional review; no identifier in source to confirm exact requirement. |
| **KGMP certification copy** (if manufacturing occurs in Korea). | Needed for 인증 dossier when MFDS requests GMP evidence. |
| **Clinical Evaluation Report or justification of exemption** | If performance claims go beyond bench, a CER is required; scope of foreign CER acceptance not identified in source. |
| **Korean language label and IFU drafts** | Mandatory labeling requirement; must be reviewed for compliance with Korean regulations. |
| **Post‑Market Surveillance plan (including PMCF)** | Required for all 인증 devices. |

### 5. Key Risk Controls to Highlight
1. **Software safety functions** – design verification that no unintended radiation exposure can occur through the GUI.  
2. **User authentication & access control** – prevents unauthorized parameter changes.  
3. **Cybersecurity hardening** – encrypted communication, regular patching schedule, intrusion detection.  
4. **AI output monitoring** – human‑in‑the‑loop confirmation for AI‑recommended settings; logging of AI decisions.  
5. **Usability safeguards** – clear visual cues, error prevention dialogs, standardized terminology aligned with Korean clinical practice.  
6. **Residual risk justification** – documented acceptance criteria and benefit‑risk analysis.

### 6. Human‑Escalation Triggers
| Trigger | Action |
|--------|--------|
| **Unclear classification** (e.g., AI functions could raise grade to 3등급) | Escalate to senior RA for re‑classification under “의료기기 품목 및 품목별 등급에 관한 규정”。 |
| **Absent or outdated KGMP certificate** | Pause dossier assembly; request updated certification before submission. |
| **Missing Korean labeling/IFU** | Stop progression until full Korean‑language drafts are provided and reviewed by label compliance specialist. |
| **AI guideline evidence not available** | Escalate to AI‑specialist team; determine if additional documentation (bias analysis, explainability) is required. |
| **Uncertainty about foreign CER acceptance** (no specific MFDS notice identified) | Request clarification from MFDS or consult recent MFDS 고시 on “foreign clinical evaluation report” acceptance before finalizing clinical data package. |
| **Cybersecurity assessment incomplete** | Notify security team; obtain full threat model and mitigation plan prior to dossier submission. |
| **Post‑Market Surveillance plan absent or insufficient** | Escalate to PMS lead; develop required surveillance activities as per MFDS 규정. |

### 7. Citations (per rule)

| Item | Citation Type | Source Reference |
|------|---------------|------------------|
| Classification rule (2등급) | Framework reference | “의료기기 품목 및 품목별 등급에 관한 규정”【1】 |
| Submission pathway (인증) | Framework reference | “의료기기 허가·신고·심사 등에 관한 규정”【1】 |
| KGMP requirement | Framework reference | “의료기기 GMP 심사·평가 등에 관한 규정”【1】 |
| Software lifecycle standard | Framework reference (standard) | IEC 62304:2006+A1:2015 |
| Risk management standard | Framework reference (standard) | ISO 14971:2019 |
| Usability engineering standard | Framework reference (standard) | IEC 62366‑1:2020 |
| Cybersecurity guideline base | Framework reference (standard) | IEC 81001‑5‑1:2021 |
| AI‑specific guidance | No specific identifier found in source — verify separately. |
| Acceptance of foreign CER / clinical data | No specific identifier found in source — verify separately. |

---

### 8. Peer‑Review Prompt
> **@RA‑Peer:** Please review the assumptions made regarding (1) the sufficiency of an 인증 pathway for a GUI software that incorporates generative AI, (2) the completeness of evidence listed given the absence of explicit MFDS notice numbers for foreign clinical data and AI guidance, and (3) any jurisdiction‑specific gaps (e.g., Korean‑language labeling nuances or KGMP applicability). Highlight missing items or alternative interpretations that could affect the submission strategy.

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

> 심각 결함 없음. 2등급→인증·디지털의료제품법 '병용 검토(optional)' 프레이밍 정확·KGMP 규정 귀속 적절. 미세: 라벨/PMS 요건을 「허가·신고·심사 규정」에 귀속 — 시행규칙 별표가 정확한 듯하나 이웃 규정으로 그럴듯한 수준.

**Source Excerpts**

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `39359892234270838`

> ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재검증 — 핵심 규제사실 반영 확인. · 상태: 승인 · 일자: 2026-06-09

### kb-eval-20261124-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "0147a258815cdf5e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `0147a258815cdf5e`
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

> **Regulatory Draft – Korean MF DS Classification & Submission Pathway  
(Software‑Based Medical Device – “Detector/Source” combination)**  

---

### 1. Korean Grade & Regulatory Track  

| Korean grade | Default submission route | Typical reviewing body |
|--------------|--------------------------|------------------------|
| **2등급**    | **인증** (technical‐document review by an MFDS‑designated 심사기관) | 한국의료기기안전정보원, KTL, KTC, KTR 등  |

*Justification* – The source states the product is classified as **2등급** under “의료용 소프트웨어 허가·심사 가이드라인” and the “디지털의료기기소프트웨어 허가·심사 가이드라인”. No higher‑risk functions are indicated, so the default 2등급 인증 track applies.  

*Citation*: no specific identifier found in source — verify separately (source [2]).

---

### 2. Required Evidence Package for **인증**  

| Requirement | What to submit | Reference (framework) |
|-------------|----------------|-----------------------|
| **Device description & intended use** | Detailed specification sheet (전압, 전류, 용도, 적용부위, SW role) | MFDS “품목코드(A‑code)” issuance procedure (no specific notice cited). |
| **Predicate device information** | FDA 510(k) predicate details; EU MDR Rule 10/11 decision matrix (if applicable) | FDA Product Classification Database (source [1]); EU MDR Rule 10 & 11 (framework). |
| **Risk Management File** | ISO 14971:2019 risk analysis, evaluation and control measures | ISO 14971 (2019) – framework. |
| **Software Life‑Cycle Documentation** | IEC 62304:2006+A1:2015 development plan, verification/validation reports, change management (including “디지털의료제품법” change‑management plan if AI/SW) | IEC 62304 (2006+A1:2015) – framework. |
| **Clinical Evaluation Report (CER)** | If required by MFDS guidelines for 2등급 SW – foreign CER may be accepted under the latest MFDS notice on foreign clinical data (verify separately). | MFDS “의료용 소프트웨어 허가·심사 가이드라인” – no specific notice number in source. |
| **Labeling & IFU** | Korean‑language labeling, user manual, safety information, and “독립형 SW 사용적합성 가이드라인” compliance (if independent software) | 국내 라벨링 요건 (MFDS) – framework; 독립형SW 가이드라인 – no identifier in source. |
| **KGMP Facility Confirmation** | Certificate of KGMP compliance for the manufacturing site(s) that will produce the device for the Korean market | KGMP (의료기기법 제28조) – framework. |
| **Post‑Market Surveillance Plan** | PMS activities, adverse event reporting procedures per MFDS “시판후조사” rules | MFDS 시판후조사 규정 – framework. |
| **Cybersecurity Strategy** | Alignment with MFDS 사이버보안 가이드라인 (referencing IEC 81001‑5‑1:2021) | IEC 81001‑5‑1 (2021) – framework. |

---

### 3. Missing / Open Items  

| Item | Why it is needed | Action |
|------|------------------|--------|
| **Exact device name & model number** | Required in all submissions and for KGMP registration. | Obtain from product development team. |
| **Finalized intended use statement (Korean)** | Determines grade confirmation; influences need for local clinical data. | Draft and confirm with marketing/clinical. |
| **Clinical performance data – Korean population** | MFDS may require local data if foreign CER is insufficient for 2등급 SW. | Assess whether a small‑scale Korean validation study is needed. |
| **Complete software bill of materials (SBOM)** | Required for cybersecurity review under MFDS guide. | Generate from development repository. |
| **Confirmed A‑code (품목코드) from MFDS** | Necessary to reference the product in all regulatory filings. | Submit preliminary specification to MFDS for code assignment. |
| **Evidence of conformity with “디지털의료제품법” (2025‑01‑24)** if AI/SW features are present | Determines applicability of separate digital‑medical‑product regime. | Verify whether any AI algorithm triggers the new law; prepare change‑management plan accordingly. |
| **KGMP certification status of the manufacturing site** | Certification body will request proof of KGMP for 인증 route. | Request latest KGMP audit report or schedule inspection. |

---

### 4. Key Risk Controls (aligned to ISO 14971)  

1. **Hazard Identification** – Electrical safety, electromagnetic compatibility, software malfunction, data integrity, cyber‑attack.  
2. **Risk Evaluation** – Use of risk matrix per ISO 14971; residual risk must be ALARP.  
3. **Control Measures** –  
   * Hardware: IEC 60601‑1 compliance (2005+A1:2012+A2:2020).  
   * Software: IEC 62304 lifecycle controls, version control, automated testing.  
   * Cybersecurity: IEC 81001‑5‑1‑based hardening, periodic vulnerability scans.  
4. **Verification & Validation** – Unit, integration, system tests; clinical validation against predicate performance.  
5. **Post‑Market Surveillance** – Ongoing monitoring of adverse events, field safety corrective actions (FSCA), and periodic risk reassessment.

---

### 5. Human‑Escalation Triggers  

| Trigger | When to Escalate to Senior RA / Regulatory Lead |
|--------|-------------------------------------------------|
| *Classification ambiguity* – evidence suggests possible upgrade to **3등급** (e.g., higher therapeutic intent) | Immediate review; re‑classify to 허가 track. |
| *Missing Korean clinical data* – MFDS reviewer requests local study after CER submission | Initiate protocol development and Ethics Committee approval. |
| *KGMP certification not yet obtained* – manufacturing site audit fails or is pending | Halt submission until KGMP proof secured. |
| *Cybersecurity gap identified* – inability to meet MFDS cyber‑guideline requirements | Engage IT security specialist; consider redesign. |
| *Regulatory notice number required* – reviewer asks for a specific MFDS 고시/notice that was not cited in the source | Conduct targeted search of MFDS 고시 database and provide exact identifier. |
| *Change in “디지털의료제품법” applicability* – new AI feature added after initial filing | Re‑evaluate classification & required change‑management plan; submit amendment. |

---

### 6. Peer Review Prompt  

> **To the next RA colleague:**  
> Please examine the assumptions made regarding (a) the sufficiency of a foreign clinical evaluation report for a 2등급 software device, (b) whether the “디지털의료제품법” actually triggers a separate digital‑medical‑product pathway for this product, and (c) any potential gaps in KGMP coverage for sub‑assemblies supplied from overseas. Confirm that all required Korean‑specific evidences are captured or flag missing items with supporting references.

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

> 심각 결함 없음. 2등급→인증·제28조·디지털의료제품법 적용대상 확인 gap·외국 CER 'verify separately' 헷징 전부 정확.

**Source Excerpts**

1. Chunk `1097646391221557778`

> ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정

2. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

### kb-eval-20261124-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "87406c8b1c903f9b", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `87406c8b1c903f9b`
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

> **디지털 의료제품법 적용 GUI 소프트웨어(‘P3 촬영실 GUI SW’) 규제 초안**

---

### 1️⃣ 제품 정의 및 의도
- **제품명**: P3 촬영실 GUI 소프트웨어  
- **분류**: 디지털 의료기기‑소프트웨어 (AI 보조 기능 미탑재, 향후 AI 모듈 추가 가능)  
- **주된 목적**: X‑ray 촬영 현장 UI·작업 흐름 지원, 향후 AI 기반 영상 판독 보조 제공 예정  

---

### 2️⃣ 등급 판단 (1~4등급)

| 근거 | 판단 |
|------|------|
| MFDS ‘의료기기 품목 및 품목별 등급에 관한 규정’ 매트릭스 **§3·§4** (소스 2) | P3 GUI SW는 “디지털 의료제품법 시행규칙” 적용 대상이며, 기존 X‑ray 하드웨어(P1, P2)는 의료기기법 체계라 등급 변동 없음. |
| 제품 특성(단순 UI·데이터 표시, AI 기능 현재 비탑재) | 2등급(인증) 가능성이 높으나 **구체적 등급은 공식 매트릭스 확인 필요** (※ “제 25조 각 호” 이동 여부 검증 요함). |

> **검증 필요** – 정확한 등급은 《의료기기 품목 및 품목별 등급에 관한 규정》(2026‑01‑23 개정 전후)와 디지털의료제품법 시행규칙(2026‑01‑23 개정) §​25 조문을 직접 확인해야 함.  

---

### 3️⃣ 인허가·인증 경로

| 등급 | 기본 절차 | 비고 |
|-----|----------|------|
| **2등급** (예상) | **인증** – MFDS‑지정 심사기관(KTL/KTC 등) 검토 | - 기능별 임상시험 자료 면제·대체 경로가 존재 (**디지털의료제품법 시행규칙 제25조 각 호**) <br> - 면제·대체 이용 시 해당 조문 적용 여부와 요구 증거 확인 필수 |
| **1등급** (가능성 낮음) | 신고 | – 해당되지 않을 확률 높음 |
| **3/4등급** | 허가 | – 현 단계에서는 해당 안 됨 |

> **핵심 판단 포인트**  
- AI 모듈이 차후 탑재될 경우 등급·인허가 경로 재평가 필요.  
- 면제·대체 경로 활용 시, “디지털의료제품법 시행규칙(2026‑01‑23 개정) 제25조”에 명시된 **요건 충족** 증거 (예: 기존 임상시험 대신 실증 데이터, 성능 시험 등) 제출 필요.

---

### 4️⃣ 요구되는 제출 자료

| 구분 | 내용 | 근거 |
|------|------|------|
| **제품 설명서·기술 사양서** | 기능 정의, 알고리즘 흐름, UI 설계 등 | KGMP 및 ISO 13485:2016 기반 QMS 문서 |
| **위험 관리 파일** | ISO 14971:2019 적용 위험 분석·평가·통제 기록 | ISO 14971:2019 (프레임워크) |
| **소프트웨어‑라이프사이클 문서** | IEC 62304:2006+A1:2015 규격에 따른 설계·개발·검증·유지보수 계획 | IEC 62304 (프레임워크) |
| **사용성·인간공학 검증** | IEC 62366‑1:2015+A1:2020 기반 사용성 테스트 보고서 | IEC 62366‑1 (프레임워크) |
| **사이버보안 대책** | IEC 81001‑5‑1:2021 적용 보안 설계·위협 모델링 | IEC 81001‑5‑1 (프레임워크) |
| **임상시험/성능 근거** | *비교설계* 임상시험 계획서 및 결과 (AI 보조 vs. 임상의 단독진단) <br> - 분석적 정확도, 효능 평가지표, 탈락률 관리 등 포함 | **2025‑10‑31 임상시험 가이드라인 9종 개정**(소스 1) |
| **면제·대체 증거 (선택)** | 디지털 의료제품법 시행규칙 제25조 각 호에 대응하는 실증 데이터 (예: 기존 임상데이터 재활용, 시뮬레이션 결과 등) | **디지털의료제품법 시행규칙(2026‑01‑23 개정)**(소스 2) |
| **라벨·사용설명서** | 전량 한글 표기, 식별코드·제조업자 정보 포함 | MFDS 라벨링 규정 (프레임워크) |
| **KGMP 인증 사본** | 제조 공장 KGMP 적합성 확인 | KGMP(법 제28조) |

---

### 5️⃣ 현재 누락·보완 필요 정보

| 항목 | 현황 | 보완 조치 |
|------|------|----------|
| **정확한 등급(1~4등급)** | 매트릭스 §3·§4만 확인, 구체적 등급 미확인 | MFDS ‘의료기기 품목 및 품목별 등급에 관한 규정’ 최신판 검토 |
| **디지털의료제품법 시행규칙 제25조 각 호 내용** | “[검증 필요]” 표기됨 | 해당 조문 전문(2026‑01‑23 개정) 확보 후 면제·대체 요건 파악 |
| **한국어 라벨·IFU 초안** | 아직 없음 | 한글 라벨/사용설명서 초안 작성 및 MFDS 검토 예정 |
| **AI 모듈 추가 시 위험도 재평가 계획** | 추후 고려 사항으로 언급 | AI 기능 상세 정의 후 별도 위험관리 파일 업데이트 계획 수립 |
| **제품별 QMS 성숙도 증빙(우수관리체계 특례)** | KGMP·ISO 13485 기반 여부 미확인 | 현행 QMS 문서 검토 및 우수관리체계 신청 절차 확인 |

---

### 6️⃣ 핵심 위험 통제 조치 (RISK CONTROLS)

1. **위험 식별·분석** – ISO 14971:2019에 따라 모든 소프트웨어 관련 위험(오작동, 데이터 오류, 사이버 공격) 리스트업.  
2. **설계‑보호** – IEC 62304에 따른 모듈화 설계·코드 리뷰, 자동 테스트 파이프라인 구축.  
3. **사용자 인터페이스 안전성** – IEC 62366‑1 기반 사용성 시험(시나리오 기반 UI 검증).  
4. **사이버보안** – IEC 81001‑5‑1 적용 위협 모델링·패치 관리 프로세스.  
5. **품질 시스템** – KGMP & ISO 13485:2016에 따른 문서관리, 내부 감사, 변경통제 절차 운영.  
6. **임상/성능 검증** – 2025‑10‑31 임상시험 가이드라인에 명시된 **비교설계**(AI 보조 vs. 의사 단독) 적용, 분석적 정확도·효과 크기 증명.  

---

### 7️⃣ 인·참고문헌 (Citations)

| 구분 | 출처 |
|------|------|
| **프레임워크** | ISO 14971:2019 ; ISO 13485:2016 ; IEC 62304:2006+A1:2015 ; IEC 62366‑1:2015+A1:2020 ; IEC 81001‑5‑1:2021 |
| **MFDS 매트릭스** | MFDS 의료기기 등급·인허가 매트릭스 **§3·§4** (소스 2) |
| **임상시험 가이드라인 개정** | 2025‑10‑31 임상시험 가이드라인 9종 개정 (소스 1) |
| **디지털의료제품법 시행규칙(개정)** | 디지털의료제품법 시행규칙 **(2026‑01‑23 개정)** (소스 2) |
| **면제·대체 요건** | “제25조 각 호” – 구체적 조문 번호는 소스에 ‘[검증 필요]’ 표기, 별도 확인 요구 |

> *※ 위 인용 중 고시·조문 번호 등은 원본 문서에서 직접 확인된 내용이며, 추가적인 상세 번호(예: 제 25조‑1) 은 현재 출처에 명시되지 않아 “검증 필요”로 표시했습니다.*

---

### 8️⃣ 인간‑에스컬레이션 트리거

| 상황 | 에스컬레이션 대상 (담당) |
|------|---------------------------|
| **등급 미확정** – 매트릭스·규칙 검토 후에도 등급이 불명확한 경우 | 규제 담당 팀장 → MFDS 상담 요청 |
| **제25조 각 호 요건 충족 여부 판단 어려움** (면제·대체 선택 시) | 법률/규제 전문가 + 외부 컨설턴트 |
| **AI 모듈 추가 계획이 확정될 경우** – 기존 위험관리·인증 범위 초과 | 제품 개발 리더 → 안전성 위원회 검토 |
| **라벨·IFU 한글 미완료** – 제출 마감 2주 이내 미작성 시 | 품질·문서 담당 → 법무팀 검토 후 수정 지시 |
| **KGMP/ISO 13485 인증 부재** – 인증 취득 전 제출 요구 발생 | QMS 관리자 → 인증기관 협의 및 진행 상태 보고 |
| **임상시험 설계(비교설계) 미충족** – 가이드라인 요구와 차이 발견 시 | 임상연구팀 → MFDS 임상시험 담당관에 추가 자료 요청 |

---

## 📢 Peer‑Review Prompt
*다음 RA 동료에게 검토를 요청합니다.*

> **검토 항목**  
> 1. 제시된 등급 판정 로직이 최신 “의료기기 품목 및 품목별 등급에 관한 규정”을 충분히 반영하고 있는가?  
> 2. 디지털의료제품법 시행규칙 제25조 각 호(면제·대체) 적용 범위와 증빙 요건 파악이 적절한가? (특히 AI 기능 추가 시점 고려)  
> 3. 제출 자료 리스트에 빠진 국내 요구 사항(예: 전자문서 보관·연계, 사후관리 계획 등)이 없는지 확인해 주시기 바랍니다.  
> 4. 위험 통제 조치와 연계된 QMS·KGMP 증빙 수준이 MFDS‑인증기관 심사 기준에 부합하는가?  

*위 사항에 대한 의견이나 추가적인 자료 요구사항을 알려 주세요.*

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

> 심각 결함 없음. 등급 '매트릭스 확인 필요' 헷징·제25조 이동 검증 표시·경로표 정확. 미세: 면제·대체 증거 예시('기존 임상데이터 재활용 등') — 같은 행에 '요구 증거 확인 필수' 헷지가 있어 11-20 kr-002 유형과 달리 경미로 판정.

**Source Excerpts**

1. Chunk `1127968925422991528`

> ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향후 AI 모듈 추가 가능성 고려해 비교설계 원칙 사전 학습 권고. - 출처: 정책브리핑 2025-10-31(https://www.korea.kr/briefing/pressReleaseView.do?newsId=156724315) ---

2. Chunk `198902914416608487`

> - 영향 제품: **P3 촬영실 GUI SW**(디지털의료기기소프트웨어에 해당하는 경우). P1 X-ray Detector·P2 Handheld X-ray Source는 의료기기법 체계 적용으로 **직접 영향 없음**(§3·§4 매트릭스 유지). - 나항은 자사에 **유리한 완화**다. GUI SW가 2등급이든 등급 미지정이든 기능별 임상시험 자료의 **면제·대체 경로가 열린다**. 다만 면제·대체의 개별 요건(개정 제25조 각 호)은 조문 전문 확인이 필요하다 — `[검증 필요]`. - 가항은 요건의 삭제가 아니라 **근거 조문의 이동(고시 → 시행규칙)** 이다. 「디지털의료제품법 시행규칙」(2026-01-23 개정)의 해당 조문을 확인해야 실제 의무 범위를 알 수 있다 — `[검증 필요]`. - 다항의 우수관리체계 특례는 **QMS 성숙도를 인허가 편익으로 전환**하는 제도다. KGMP·ISO 13485 기반이 갖춰진 경우 중장기 활용 가치가 있다. **행동 (Action)**

### kb-eval-20261124-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "4cf868418297a197", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `4cf868418297a197`
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

> **Regulatory Draft – Imaging‑Room GUI Software (SaMD)  
Target audience: Korean RA (MFDS) team**

---

### 1. Preliminary Classification & Submission Route  

| Korean grade | Typical MFDS pathway | Notes for this SaMD |
|--------------|----------------------|---------------------|
| **1등급** | 신고 (notification) | Only if the software is deemed “low‑risk” (e.g., purely informational, no impact on patient diagnosis or treatment). |
| **2등급** | 인증 (technical‑document review by an MFDS‑designated 심사기관) | Most stand‑alone imaging‑software that performs image display, basic manipulation, or non‑diagnostic decision support fall here. |
| **3등급·4등급** | 허가 (full approval by MFDS) | Required when the software directly influences diagnosis/treatment decisions, includes AI/ML functions that affect clinical outcomes, or is classified as “high‑risk” under the Digital Medical Products Act. |

> **Action:** Confirm the exact grade against 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS_인허가_상세가이드.md §2). *No specific grade identifier appears in the source excerpts; verification required.*

---

### 2. Core Submission Evidence  

| Requirement | Korean regulatory basis (framework) | What must be supplied |
|-------------|--------------------------------------|-----------------------|
| **QMS compliance** | KGMP (의료기기법 제28조) + ISO 13485:2016 | Certified KGMP certificate, copy of QMS manual that incorporates the ARR activities listed in FDA 21 CFR 820.10(b) (ARR) and 820.35(a) (complaint handling). |
| **Software lifecycle documentation** | IEC 62304:2006+A1:2015 (Safety Class C) – referenced in source → “SW 개발 수명주기” | Development plan, Software Requirements Specification (SRS), Software Design Description (SDD), Software Verification Plan/Report, Software Validation Report, change‑control SOP. |
| **Cybersecurity** | MFDS 사이버보안 가이드라인 2025 (no identifier in source) | Threat model, Secure‑by‑Design architecture description, SBOM, PCCP‑style cybersecurity plan (aligned with FDA 524B guidance). |
| **AI/ML component (if any)** | 디지털의료제품법 + FDA PCCP (2024) + EU AI Act (for reference) | AI/ML lifecycle documentation (training data set description, performance metrics, change‑management plan), risk assessment per “AI 고위험” criteria. |
| **Clinical evaluation** | KGMP & 디지털의료제품법 requirements for software | Clinical Evaluation Report (CER) that may incorporate foreign CERs only if MFDS has explicitly accepted them; otherwise local clinical data or post‑market validation study needed. |
| **Korean labeling & IFU** | MFDS 고시 on labeling (no specific notice number found) | Korean language UI labels, user manual, safety information, and K‑UDI barcode/QR code in accordance with the current UDI regulation. |
| **Post‑Market Surveillance (PMS)** | MFDS 시판후조사 규정 | PMS plan, periodic safety update report, process for 30‑day MDR‑type adverse event reporting (see source “불만 처리 → MFDS 보고”). |
| **Contract sterilization / relabeling** (if applicable) | FDA 820.10(a) ↔ KGMP scope extension (source note) | Agreements and QMS procedures covering contracted sterilizers, re‑labelers, foreign distributors. |

> **Citation notes:**  
> • Framework references such as ISO 13485:2016, IEC 62304:2006+A1:2015, MFDS 사이버보안 가이드라인 2025 are stated without “verify” caveat (they are well‑known standards).  
> • No specific Korean 고시 or article number appears in the provided excerpts; therefore each item that would normally cite a 고시 is indicated as *“no specific identifier found in source — verify separately.”*  

---

### 3. Missing / Unverified Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Exact Korean grade (1‑4등급)** | Determines the submission track and required evidence depth. | Perform a formal grading check using the device’s intended use, risk analysis, and MFDS “품목별 등급” table. |
| **K‑UDI implementation details** | Mandatory labeling for all grades ≥2등급. | Obtain the latest MFDS 고시 on K‑UDI (e.g., 고시 제2024‑xx호) and prepare barcode/QR data file. |
| **Local clinical evidence requirement** | KGMP may waive foreign CER only if expressly accepted. | Clarify with MFDS whether a foreign CER (e.g., FDA 510(k) summary) is acceptable; otherwise plan a Korean pilot study or post‑market validation. |
| **Exact version of the cyber‑security guideline** | The 2025 guide has been updated multiple times. | Request the official PDF reference number from MFDS to cite correctly in the submission. |
| **AI/ML risk classification under 디지털의료제품법** | Determines need for pre‑market AI‑specific assessment. | Conduct a dedicated AI risk assessment and map to the “고위험” criteria. |
| **Contract sterilizer / relabeler scope** (if any) | Extends QMS applicability per FDA 820.10(a). | Identify all external service providers and ensure they are incorporated into the KGMP‑approved QMS. |

---

### 4. Key Risk Controls to be Demonstrated  

1. **Design Control & Traceability** – Maintain a bidirectional traceability matrix linking user needs → software requirements → design outputs → verification/validation tests (per IEC 62304).  
2. **Software Validation in Intended Use Environment** – Include end‑to‑end functional testing on Korean clinical hardware, with documented results.  
3. **Cybersecurity Controls** – Threat modeling, vulnerability management schedule, and secure update mechanism; evidence of compliance with MFDS cyber guideline.  
4. **AI/ML Change Management** – SOP for model retraining, performance monitoring, and re‑validation before deployment (aligned with FDA PCCP).  
5. **Complaint & Adverse Event Handling** – Procedure that captures all complaints, assesses MDR‑type reportability, and forwards to MFDS within 30 days (source §820.35(a) mapping).  
6. **Post‑Market Surveillance** – Ongoing safety data collection, periodic safety update reports, and a process for field corrective actions (including recall capability).

---

### 5. Human‑Escalation Triggers  

| Trigger | When to Escalate to Senior RA / Regulatory Leadership |
|---------|-------------------------------------------------------|
| **Uncertain grade (1‑4등급)** | Until the device’s classification is confirmed, hold submission preparation. |
| **Absence of locally accepted clinical data** | If MFDS requires Korean CER and none is planned, initiate a local study plan. |
| **Gap in K‑UDI compliance** | Missing barcode/QR generation or labeling approval – pause filing. |
| **Cybersecurity guideline version mismatch** | If the guidance used differs from the latest MFDS issuance, seek clarification. |
| **AI/ML high‑risk determination** | Requires additional AI‑specific documentation; involve legal/compliance team. |
| **Contracted sterilizer/relabeler not covered in KGMP QMS** | Expand QMS scope or secure separate certification before submission. |
| **Any identified discrepancy between foreign evidence and MFDS acceptance criteria** (e.g., FDA 21 CFR references) | Conduct a gap‑analysis and request MFDS clarification before proceeding. |

---

### 6. Peer Review Prompt  

> *@RA‑Peer:* Please review the assumptions above, especially:  
> – The inferred grade for an imaging‑room GUI SaMD without a concrete “품목별 등급” citation.  
> – The completeness of the required evidence list given the lack of explicit MFDS 고시 numbers in the source material.  
> – Any additional Korean‑specific obligations (e.g., K‑UDI, post‑market service reporting) that may have been omitted.  

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

> 심각 결함 없음. 등급별 트랙·사이버 가이드라인 'no identifier' 헷징·제28조. 미세: 'K-UDI' 용어·'고시 제2024-xx호' 자리표시자(명시적 미확정)·'high-risk under DMPA'를 3·4등급 트리거 예시로 병기(헷지됨)·'PCCP-style' 524B 병기(소스 유래 표현).

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261124-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-24", "decision_ref": "kb-eval-20261124-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "02b86ae810af4133", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `02b86ae810af4133`
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

> **Regulatory Draft – MFDS Classification & Licensing Pathway**

---

### 1. Device Overview (information still required)

| Item | Current status | Comment / Evidence needed |
|------|----------------|---------------------------|
| **Device name / model** | – | Required for all submission documents |
| **Intended use / indication** | – | Determines the applicable grade (1‑4등급) and whether a clinical evaluation is mandatory |
| **Technology type** (e.g., AI/ML‑based software, hardware‑software combination) | – | Impacts classification under the 2025 Digital Medical Products Act and MFDS “디지털의료기기 가이드라인” (see § AI/ML GUI SW requirement) |
| **Risk class (1~4등급)** | – | Must be confirmed from **「의료기기 품목 및 품목별 등급에 관한 규정」**; no specific identifier is supplied in the source – verify separately |
| **Manufacturing site(s)** | – | Needed for KGMP suitability review and GMP 적합인정 절차 (see below) |
| **Foreign regulatory status** (FDA 510(k), CE marking, etc.) | – | Determines whether foreign non‑clinical data or clinical evaluation reports can be leveraged under MFDS mutual‑acceptance provisions |

---

### 2. Determination of Korean Grade & Submission Route  

| Korean grade | Typical submission track | Key regulatory basis |
|--------------|--------------------------|----------------------|
| **1등급** | 신고 (notification) | Medical Device Act, § 33‑2 |
| **2등급** | 인증 (technical‑document review by MFDS‑designated 심사기관) | Medical Device Act, § 34‑5; *MFDS_인허가_상세가이드.md* §2 |
| **3등급·4등급** | 허가 (full approval by MFDS) | Medical Device Act, §§ 35‑1~§ 35‑7 |

> **Citation:** no specific identifier appears in the source excerpts for the grade rules – verify separately.

---

### 3. GMP 적합인정 절차 (KGMP Certification)

The KGMP pathway is required for any device that will be manufactured or imported into Korea. The process, as outlined in the source, proceeds as follows:

1. **GMP 심사 신청** →  
2. **심사기관 배정** →  
3. **품질문서 심사** →  
4. **제조소 현장조사** →  
5. **결함사항 통보 (Critical/Major/Minor)** →  
6. **시정 조치 제출** →  
7. **적합인정서 발급** (validity 3 years, renewal required)

*The designated 심사기관 (six total) cover all product groups:* KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea.  

**Digital‑medical‑device specific:** NIDS began performing GMP 적합판정 from **2025‑01‑24** (source [2]) and must be considered when selecting an agency for SaMD or other digital products.

> **Citation:** excerpt [1] – GMP flowchart; excerpt [2] – NIDS role start date.

---

### 4. Required Technical Evidence (per MFDS & International Standards)

| Requirement | Standard / Guideline | Applicability |
|-------------|----------------------|---------------|
| **Quality Management System** | KGMP (Medical Device Act 제28조) | Mandatory for all grades; evidence via GMP 적합인정서 |
| **Risk Management File** | ISO 14971 2019 (no amendment 2024) | Required for every grade; especially critical for AI/ML‑based SaMD |
| **Clinical Evaluation** | MFDS acceptance of foreign CER *if* cited in relevant notice; otherwise local clinical data required | Needed for 2~4등급 devices unless exemption applies |
| **Non‑clinical (biocompatibility, electrical safety, etc.)** | ISO 10993‑1 2018, IEC 60601‑1 2005+A1:2012+A2:2020, IEC 62304 2006+A1:2015 | Required for hardware or software that interacts with patients |
| **Labeling & IFU** | MFDS labeling ordinance (Korean language mandatory) | All grades |
| **Cyber‑security / Software Validation** | IEC 81001‑5‑1 2021; MFDS 디지털의료기기 가이드라인 (AI/ML GUI) – 2025‑05‑07 update | Required for SaMD, especially AI/ML |
| **Post‑Market Surveillance (시판후조사)** | MFDS 시판후조사 규정 | Mandatory for 2~4등급; includes PMCF for higher grades |

> Framework references above are standard numbers; no specific Korean notice identifiers were present in the source excerpts, so no “verify separately” tag is added.

---

### 5. Gaps / Missing Information (to be addressed before submission)

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Confirmed Korean grade** | Determines pathway (신고/인증/허가) and depth of evidence required | Conduct a classification workshop using the device’s intended use; reference the official “의료기기 품목 및 품목별 등급에 관한 규정”. |
| **Full Intended Use Statement** | Needed for risk classification, clinical evaluation scope, labeling content | Draft a clear indication summary in Korean and English. |
| **Manufacturing site details & KGMP status** | Required for GMP 적합인정 절차; affects choice of 심사기관 (include NIDS if SaMD) | Prepare site master file; liaise with chosen 심사기관 early. |
| **Local clinical data or acceptable foreign CER citation** | Mandatory for 2~4등급 unless exemption granted | Identify applicable MFDS notice that permits foreign CER use; collect supporting documentation. |
| **Korean language labeling & IFU drafts** | Legal requirement; non‑compliance leads to rejection at review stage | Produce Korean translations and have them reviewed by a certified medical translator. |
| **Cyber‑security risk assessment (for AI/ML software)** | Required under 2025‑05‑07 digital‑medical‑기기 가이드라인 | Conduct IEC 62304/IEC 81001‑5‑1 based security analysis; include in Technical Documentation. |

---

### 6. Risk Controls & Mitigation Measures

| Hazard | Control (per ISO 14971) | Verification |
|--------|-----------------------|--------------|
| **Incorrect algorithm output** (AI/ML) | Design validation, continuous learning controls, performance limits, human‑in‑the‑loop verification | Software Validation report; periodic performance monitoring per MFDS 시판후조사. |
| **Data breach / cyber attack** | Encryption, authentication, secure update mechanism, IEC 81001‑5‑1 compliance | Penetration testing, vulnerability management plan. |
| **Device malfunction due to manufacturing defect** | KGMP compliant processes, GMP 적합인정, regular QC sampling | Audit reports from 심사기관; corrective action records. |
| **Mislabeling / language errors** | Dual‑language review, labeling checklist per MFDS ordinance | Final sign‑off by regulatory affairs and translation specialist. |

---

### 7. Human‑Escalation Triggers (when to involve senior RA/Legal)

1. **Unclear grade after classification workshop** – escalates to senior RA for interpretation of the “의료기기 품목 및 품목별 등급에 관한 규정”.
2. **Absence of acceptable foreign clinical evidence** – requires legal review of MFDS mutual‑acceptance provisions and possible need for a Korean clinical trial.
3. **NIDS‑related GMP assessment selection** – decision impacts timeline; senior project manager should approve agency choice.
4. **Pending 2026 regulatory changes (autonomous performance certification, negative change notification system)** – monitor implementation guidance; if launch date overlaps, senior leadership must decide on risk‑based approach.
5. **Significant safety signal identified during post‑market surveillance** – immediate escalation to QA/Pharmacovigilance and MFDS as required by 시판후조사 규정.

---

### 8. Peer Review Prompt

> *Please review the assumptions made regarding the device’s classification pathway, the completeness of the evidence checklist, and any jurisdiction‑specific gaps (e.g., Korean labeling, KGMP agency selection). Confirm whether additional MFDS notices or recent guideline updates (post‑2025) might affect the acceptance of foreign clinical data or the cyber‑security requirements for AI/ML software.*

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

> 경로별 조문 pinpoint 창작: '신고 Medical Device Act §33-2 / 인증 §34-5 / 허가 §§35-1~35-7' — 소스 발췌에 해당 번호 전무(그렵 확인 0건). SOUL 규칙 6 위반('그럴듯한 번호는 없느니만 못하다'). 제28조·등급 SSOT·외국 CER 헷징은 정확. [최종 1점 — shadow 10차 하향 수용: 경로별 조문 pinpoint(신고 §33-2·인증 §34-5·허가 §§35-1~35-7) 3건 전부 소스 부재·실재하지 않는 번호(shadow 원문 대조: 인증은 의료기기법 제6조·제12조 계열) — 다중 창작. 제28조·등급 SSOT 서술은 정확했으나 핵심 경로표의 법적 근거 열이 전부 무근거.]

**Source Excerpts**

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---
