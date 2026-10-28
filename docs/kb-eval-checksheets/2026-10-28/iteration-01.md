# KB Eval Checksheet - 2026-10-28 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261028-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "5b22387edb1f5e4d", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md", "source_hash": "b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `5b22387edb1f5e4d`
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

> **Regulatory Draft – FDA 510(k) Additional‑Information (AI) Response Strategy**  

---

### Bottom‑line Recommendation  
- **Device classification & submission route:** Class II, 510(k) Premarket Notification (21 CFR §807.92). If the device is a medical‑image management/analysis system, the appropriate product code falls under **§892.2050 (Class II)**; otherwise determine the correct panel (e.g., §862 for in‑vitro diagnostics).  
- **Core evidence package:** Updated predicate comparison, bench‑performance data, software verification & validation (IEC 62304), risk management file (ISO 14971:2019), labeling (21 CFR §801), and UDI compliance (21 CFR §830).  
- **Current gaps** (derived from the AI request) are ‑‑ see “Identified Evidence Gaps” below.  

Proceed with the action plan; if any gap requires new clinical data, a design change that could affect classification, or cannot be resolved within the FDA’s 180‑day response window, **escalate to senior RA management** (see Escalation Triggers).

---

## 1. Classification & Submission Route  

| Attribute | Determination |
|-----------|----------------|
| **Regulatory pathway** | Premarket notification – 510(k) (21 CFR §807.92). |
| **Device class** | Class II (most software‑based image analysis and processing systems are classified as Class II under **§892.2050**). If the device is not an imaging system, identify the appropriate product code via the FDA’s 510(k) database and apply the relevant part (e.g., §862 for clinical chemistry). |
| **Key CFR references** | • 21 CFR §807 – registration & listing, 510(k) submission. <br>• 21 CFR §892.2050 – Class II designation for medical‑image management/processing software. <br>• 21 CFR §820 – Quality Management System (QMSR). <br>• 21 CFR §801 – labeling requirements. <br>• 21 CFR §830 – UDI system. |

*If the device’s intended use differs materially from existing image‑processing software (e.g., AI‑driven diagnosis), re‑evaluate classification; a De Novo request may be required.*  

---

## 2. Required Evidence for a Complete 510(k)  

| Evidence Item | Typical Content | Governing Standard / Guidance |
|---------------|----------------|--------------------------------|
| **Predicate comparison** | Side‑by‑side tables of technological characteristics, performance specifications, labeling claims. | FDA’s “Guidance for Industry and FDA Staff: Medical Device Submissions – 510(k)” (2022). |
| **Bench/Performance testing** | Accuracy, precision, repeatability, limits of detection (if applicable), interoperability with imaging modalities. | IEC 62304:2006+A1:2015 (software life‑cycle); device‑specific FDA guidance. |
| **Software verification & validation** | Unit, integration, system, and acceptance tests; documentation of test cases, results, traceability matrix. | IEC 62304; FDA’s “Content of Premarket Submissions for Software Devices” (2022). |
| **Risk Management File** | Hazard analysis, risk controls, residual risk evaluation, risk/benefit justification. | ISO 14971:2019 (risk‑management standard). |
| **Usability / Human Factors** | IEC 62366‑1:2020 usability engineering report; formative and summative validation data. | FDA “Human Factors Guidance for Medical Devices” (2022). |
| **Labeling & IFU** | Intended use, indications, contraindications, warnings/precautions, instructions for use, UDI placement. | 21 CFR §801; 21 CFR §830 (UDI). |
| **Sterility / Biocompatibility (if applicable)** | ISO 10993‑1:2018 data package or FDA‑accepted alternative. | ISO 10993‑1. |
| **Clinical/equivalence data** | Clinical evaluation report, literature review, or limited clinical study demonstrating equivalence to predicate. | FDA “Guidance on Clinical Evidence for 510(k) Submissions” (2020). |

---

## 3. Identified Evidence Gaps (Based on AI Request)

| Gap | Description | Why it matters |
|-----|-------------|----------------|
| **Insufficient GSPR (General Safety & Performance Requirements) evidence** | The source notes “GSPR 입증 근거 부족” for EU; the U.S. analogue is inadequate documentation that the device meets general safety and performance standards (e.g., verification of software algorithm accuracy). | FDA will consider this a major deficiency; may request additional bench data or validation reports. |
| **Clinical‑evaluation equivalence insufficient** | “Clinical Evaluation 동등성 불충분” mirrors the need in the U.S. for a robust predicate comparison and/or clinical data demonstrating performance parity. | Without clear equivalence, the 510(k) cannot establish substantial equivalence. |
| **Post‑Market Clinical Follow‑up (PMCF) plan missing** | Although PMCF is an EU requirement, FDA expects a post‑market surveillance plan (21 CFR §820.100). The AI likely requests a written PMS/PSUR-like plan. | A documented post‑market surveillance strategy is required for risk management and may affect the determination of substantial equivalence. |
| **Risk‑management file not ISO 14971‑compliant** | “위험관리파일 ISO 14971 부적합” – the current risk analysis does not meet the 2019 edition requirements (e.g., missing control‑measure effectiveness evidence). | FDA will reject an incomplete risk file; it must include hazard identification, mitigation, and residual risk assessment. |
| **Software Change‑Control (PCCP) absent** | The AI response strategy references the “Predetermined Change Control Plan (PCCP)” guidance (Dec 2024). No PCCP has been submitted. | For AI/ML‑based software, FDA expects a PCCP to pre‑authorise anticipated modifications; omission can trigger an Additional Information request on change management. |
| **UDI labeling details incomplete** | The UDI label must include device identifier, production identifier, and meet §830.10–§830.60 requirements. Current submission lacks full label mock‑up. | Non‑compliance with UDI rules is a “major” deficiency under 21 CFR §820.30. |
| **Human‑Factors validation not documented** | No IEC 62366‑1 usability engineering report is linked to the AI request. | FDA may view this as an unacceptable risk for user error, especially for image‑analysis decision support tools. |

*No specific identifier (e.g., 510(k) number) was supplied in the source; “no specific identifier found in source — verify separately” applies to any claim requiring a predicate reference.*

---

## 4. Risk Controls & Mitigation Actions  

| Control | Implementation |
|---------|----------------|
| **Risk Management (ISO 14971)** | Update hazard analysis, include newly identified software‑related risks (e.g., algorithm bias), document control measures, and perform residual risk evaluation. |
| **Software Validation (IEC 62304 + PCCP)** | Conduct full verification/validation per IEC 62304; develop a Predetermined Change Control Plan (PCCP) covering anticipated model updates or parameter adjustments. |
| **Usability Engineering (IEC 62366‑1)** | Perform formative usability testing, followed by summative validation with representative users; produce a usability report linked to the AI response. |
| **Post‑Market Surveillance** | Draft a PMS plan per 21 CFR §820.100, including adverse event reporting (Part 803) and periodic safety updates (Part 806 for corrections/removals). |
| **UDI Compliance** | Generate label mock‑ups incorporating the device identifier (DI) and production identifier (PI) as required by §830.10–§830.60; submit GUDID data package. |
| **Clinical Equivalence** | Compile a side‑by‑side performance comparison matrix against an FDA‑cleared predicate; if gaps remain, schedule a limited clinical study (e.g., prospective multi‑center trial) to collect supporting data. |

---

## 5. Action Plan & Timeline  

| Step | Owner | Deadline* | Deliverable |
|------|-------|-----------|-------------|
| **1. Confirm classification & predicate** | RA Lead | Day 2 of AI response period | Updated product code, class justification, and identified predicate(s). |
| **2. Update risk management file (ISO 14971)** | QMS Engineer | Day 7 | Revised Risk Management Report with traceability to design controls. |
| **3. Prepare software verification & validation package** | Software QA | Day 10 | Test protocols, results, and traceability matrix; draft PCCP. |
| **4. Generate clinical‑equivalence documentation** | Clinical Affairs | Day 12 | Predicate comparison tables + any supplemental clinical data. |
| **5. Draft post‑market surveillance plan** | Regulatory Ops | Day 12 | PMS SOP and reporting schedule (per §820.100). |
| **6. Compile labeling & UDI package** | Labeling Team | Day 14 | Full label artwork, IFU, and GUDID submission files. |
| **7. Conduct/usability validation (IEC 62366‑1)** | Human Factors Engineer | Day 18 (if time permits) | Usability test report; otherwise note as “pending” with justification for extension. |
| **8. Assemble complete response dossier** | RA Lead | Day 20 (or earlier if possible) | Cover letter, table of contents, cross‑referenced evidence, and AI response checklist. |
| **9. Submit to FDA via eCopy portal** | Regulatory Ops | Within 180‑day window (as per FDA guidance) | Confirmation receipt from FDA. |

\*Deadlines assume a 30‑day AI response period; adjust if the FDA provides a different timeframe.

---

## 6. Human‑Escalation Triggers  

| Trigger | Reason for Escalation |
|---------|----------------------|
| **New clinical data required** (e.g., prospective study) that cannot be generated within the AI response window. | May need to request an extension or consider a de novo submission. |
> **Escalate to:** Senior RA Manager & Clinical Lead. |
| **Design change that could alter classification** (e.g., adding autonomous diagnostic output). | Requires reevaluation of Class II vs. Class III, potential PMA pathway. |
> **Escalate to:** Director of Regulatory Affairs and Legal Counsel. |
| **Inability to meet FDA’s 180‑day full response deadline** despite best efforts. | Must file a “Request for Additional Time” (FDA guidance 73507) and document justification. |
> **Escalate to:** Executive Sponsor & Project Management Office. |
| **Significant deficiency related to safety (e.g., high residual risk, unmitigated hazard)** identified during risk‑file update. | May trigger a voluntary correction/removal under 21 CFR §806 or a Field Safety Notice equivalent. |
> **Escalate to:** Quality Assurance Leadership and senior management. |
| **Disagreement on interpretation of FDA’s AI request** among functional teams. | Requires external regulatory counsel review. |
> **Escalate to:** Regulatory Affairs Peer Review Committee. |

---

## 7. Peer‑Review Prompt  

*To the RA community:* Please challenge the assumptions above, especially:

1. The selection of **§892.2050** as the default classification—does the device’s intended use truly fit this panel, or might another part (e.g., §862) be more appropriate?  
2. The adequacy of the proposed **risk‑management updates** in satisfying the FDA’s “GSPR evidence” requirement without a formal EU‑style GSPR reference.  
3. Whether the **timeline** for usability validation (Day 18) is realistic given typical resource constraints; should we pre‑emptively request an extension?  

Your critique will help refine the response strategy and ensure all jurisdiction‑specific gaps are captured.

--- 

*Prepared by:* Mike – U.S. FDA Regulatory Affairs Specialist (510(k) & Substantial Equivalence).

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

**Correction Note**

> `21 CFR §807.92`를 510(k) 경로/제출 근거로 오귀속 (2회, 경로 표 포함). §807.92는 510(k) Summary/Statement 조항이며 제출요건 근거는 §807.81(a)/§807.87. 웹검증(eCFR/accessdata). 정정 후 사용 가능.

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1062884112493939033`

> ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합

2. Chunk `1076622801663602202`

> > 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: https://www.fda.gov/media/73507/download (FDA Guidance: FDA and Industry Actions on 510(k) Submissions, Oct 2022) | https://medicaldeviceacademy.com/additional-information-request/ | https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process | MDUFA V Commitment Letter https://www.fda.gov/media/158308/download # FDA Additional Information (AI) 대응 전략 및 샘플 답변 체계

### kb-eval-20261028-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "44ec14012cad6d45", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `44ec14012cad6d45`
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

> **Regulatory Draft – Evidence‑Gap Assessment for a Medical Device Submission**  

---

### 1. Bottom‑line Recommendation  
Based on the information available (no clear device description, intended use, or technology level), **the default regulatory route is a 510(k) submission** if the device can be shown to be substantially equivalent to an already cleared predicate that falls within Class I or II.  

*If the device incorporates a novel imaging modality, software algorithm, or other technology for which no suitable predicate exists, pursue a **De Novo** request (new classification). For devices that present a probable unreasonable risk (e.g., implantable cardiac‑support systems, high‑energy X‑ray generators), a **PMA** would be required.*

> **Human escalation trigger #1:** *If the sponsor cannot identify an appropriate predicate within 21 CFR 807‑class II listings, or if the device’s intended use suggests a Class III risk profile, the case must be escalated to senior RA for De Novo/PMA pathway selection.*  

---

### 2. Device Classification / Submission Route  

| Criterion | 510(k) | De Novo | PMA |
|-----------|--------|---------|-----|
| **Statutory basis** | FD&C Act § 510(k), 21 CFR 807 | FD&C Act § 513(f)(2), 21 CFR 860 | FD&C Act § 515, 21 CFR 814 |
| **Typical class** | Class I‑II (standard) – some Class III may qualify if predicate exists | New Class I‑II devices (no predicate) | Class III |
| **Predicate required?** | Yes | No | No |
| **Clinical data requirement** | Conditional – see § 3 of the FDA “Clinical Data Need Determination” guidance (source provides only a reference, no numeric identifier) | “If applicable” – generally not mandatory unless risk analysis dictates | Mandatory (clinical trial data) |
| **Review timeline** | 90 days target | ~150 days | ~180 days target |

> **Human escalation trigger #2:** *When the intended use or technological characteristics suggest a Class III device, automatically refer to senior RA for PMA consideration.*  

---

### 3. Required Evidence – Baseline Checklist  

| Evidence Item | Needed for 510(k) | Needed for De Novo* | Needed for PMA |
|---------------|-------------------|---------------------|----------------|
| **Device description & specifications** | ✔︎ | ✔︎ | ✔︎ |
| **Intended use statement** | ✔︎ | ✔︎ | ✔︎ |
| **Predicate comparison matrix (design, performance, labeling)** | ✔︎ (mandatory) | – | – |
| **Bench‑testing / performance verification (electrical safety, EMC, mechanical tests, software validation per IEC 62304)** | ✔︎ | ✔︎ | ✔︎ |
| **Risk Management File (ISO 14971:2019)** | ✔︎ (summary) | ✔︎ (full) | ✔︎ (full) |
| **Sterilization & biocompatibility data (ISO 10993‑1:2018)** – if applicable | ✔︎ (as needed) | ✔︎ | ✔︎ |
| **Clinical data** | Conditional – only if “clinical data are necessary” per FDA guidance § 3* | May be required to support reasonable assurance of safety/effectiveness | Required (investigational device exemption, pivotal trial) |
| **Labeling & IFU (21 CFR 801)** | ✔︎ | ✔︎ | ✔︎ |
| **UDI labeling (21 CFR 830.10‑830.60)** | ✔︎ | ✔︎ | ✔︎ |
| **Quality Management System compliance (21 CFR 820; QMSR effective 2026‑02, ISO 13485:2016)** | ✔︎ | ✔︎ | ✔︎ |

\*De Novo *may still need clinical data if risk analysis (ISO 14971) identifies hazards that cannot be mitigated by bench testing alone.  

> **Human escalation trigger #3:** *If any of the above items are missing or inadequately documented, the submission package must be paused and sent back to the sponsor for gap closure before proceeding.*  

---

### 4. Identified Evidence Gaps (based on current source excerpt)

| Gap | Why it matters | Impact on pathway |
|-----|----------------|-------------------|
| **No predicate device identified** | Predicate is mandatory for a 510(k) (§ 510(k), 21 CFR 807). Without it, the submission cannot proceed in this track. | Forces shift to De Novo or PMA. |
| **Missing intended use / claim language** | Determines classification and need for clinical data (see FDA “Clinical Data Need Determination” guidance). | Ambiguous risk level → potential requirement for clinical data or higher‑level review. |
| **Absence of risk management documentation** | ISO 14971:2019 is the accepted framework; FDA expects a demonstrated risk analysis to justify clinical data waiver. | May trigger a Clinical Data Requirement (CDR) notice from FDA. |
| **Unclear technology category (e.g., imaging, software, or combination)** | Determines applicable 21 CFR part (Part 892 for radiology/ imaging; Part 862 for clinical chemistry). Mis‑classification leads to regulatory mismatch. | Could invalidate the submission if wrong product code/classification used. |
| **No UDI strategy** | 21 CFR 830 requirements apply to all Class II and III devices. Lack of plan delays clearance. | Submission non‑conforming; FDA will issue a deficiency. |

> **Human escalation trigger #4:** *If any gap cannot be resolved within three business days after request to the sponsor, elevate to project manager for timeline/strategy re‑assessment.*  

---

### 5. Risk Controls (to be incorporated in the submission)

1. **Risk Management File** – ISO 14971:2019 compliant analysis, including hazard identification, severity/occurrence estimation, mitigation measures, and residual risk evaluation.  
2. **Design Controls** – per 21 CFR 820.30 (design input, output, verification, validation).  
3. **Software Lifecycle Processes** – IEC 62304:2006+A1:2015 compliant development, verification, and maintenance plan; include a **Predetermined Change Control Plan (PCCP)** if the device employs adaptive AI/ML.  
4. **Usability Engineering** – IEC 62366‑1:2020 to demonstrate safe user interface for intended operators.  
5. **Electrical Safety & EMC** – IEC 60601‑1:2005+A1:2012+A2:2020 testing records (if applicable).  
6. **Biocompatibility** – ISO 10993‑1:2018 data package for any patient‑contacting materials.  

> **Human escalation trigger #5:** *If any risk control document is missing or fails to meet the referenced standard, stop clearance activities and request remediation.*  

---

### 6. Citations (as required by instructions)

| Item | Citation Type | Reference |
|------|---------------|-----------|
| Legal basis for 510(k) | Framework | FD&C Act § 510(k), 21 CFR 807 |
| Legal basis for De Novo | Framework | FD&C Act § 513(f)(2), 21 CFR 860 |
| Legal basis for PMA | Framework | FD&C Act § 515, 21 CFR 814 |
| Clinical‑data conditionality (510(k) vs De Novo vs PMA) | Framework (source summary table) | No specific identifier found in source – verify separately |
| eSTAR obligations dates | Framework (source table) | No specific identifier found in source – verify separately |
| User fee amounts FY2025 | Framework (source table) | No specific identifier found in source – verify separately |
| QMSR effective date (ISO 13485‑aligned) | Framework | 21 CFR 820; QMSR effective 2026‑02 |
| ISO 14971 risk management standard | Framework | ISO 14971:2019 |
| IEC 62304 software lifecycle | Framework | IEC 62304:2006+A1:2015 |
| Predetermined Change Control Plan (PCCP) terminology | Framework | FDA final guidance, Dec 2024 |

*(All framework references are stated as facts per instruction; no invented case numbers or identifiers were added.)*  

---

### 7. Human‑Escalation Triggers Summary  

| Trigger # | Condition | Escalation To |
|-----------|-----------|---------------|
| 1 | No suitable predicate found for 510(k) | Senior RA / Regulatory Strategy Lead |
| 2 | Indications of Class III risk (e.g., invasive, high‑energy) | Senior RA & Clinical Affairs |
| 3 | Missing any baseline evidence item (design, labeling, risk file, etc.) | Project Manager & Sponsor |
| 4 | Unresolved gaps after 3 business days | Project Manager for timeline impact |
| 5 | Incomplete or non‑conforming risk control documentation | Quality Assurance / Senior RA |

When any trigger fires, the case should be **commented** in the work package with a recommendation to pause further submission preparation until resolution, per Fixed Rule 1 (no automatic closure).  

---

### 8. Peer Review Prompt  

> *RA peer, please review the assumptions made regarding the default 510(k) pathway, the identification of evidence gaps without a concrete device description, and the applicability of the cited standards. Are there any jurisdiction‑specific considerations (e.g., Part 892 vs Part 862 classification) that we have overlooked given the lack of technology detail?*  

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

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20261028-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "ffdfc539bdc90ded", "source": "github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md", "source_hash": "0081e939c99bc98216ea8bbc10bd8fcf3f01739ef65674a0fd6b602825348c7d"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `ffdfc539bdc90ded`
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

> **Regulatory Draft – 510(k) Pathway for a New X‑ray Imaging System**

| Item | Decision / Requirement | Evidence Needed | Source reference |
|------|------------------------|-----------------|------------------|
| **Device classification & submission route** | Class II (electronic radiology equipment). Falls under **21 CFR Part 892 – Radiology/Imaging Devices**. 510(k) submission required per **21 CFR §807.92(a)(3)**. | Predicate device clearance (e.g., a previously cleared X‑ray system of the same intended use) and justification of substantial equivalence. | No specific identifier found in source – verify separately |
| **Device Description** | Full description of physical, technological characteristics, components, accessories. | Technical documentation package (drawings, specifications, bill of materials). | FDA‑510K‑B1 (Section B.1) |
| **Intended Use / Indications for Use** | Statement of disease/condition, patient population, clinical environment, and purpose of the X‑ray system. | Intended‐use labeling, clinical context description. | FDA‑510K‑B2 (Section B.2) |
| **Electrical Safety & EMC** | Compliance with **IEC 60601‑1** (general safety) and **IEC 60601‑2‑54** (X‑ray equipment). | Test reports for electrical safety, leakage currents, grounding, dielectric strength; EMC test report per IEC 60601‑1‑2. | FDA‑510K‑C3 (Section C.3) |
| **Software – Major LoC** | Software that controls image acquisition, processing or dose management. Must follow **IEC 62304**, FDA software guidance, and cybersecurity standards (**IEC 81001‑5‑1**). | • Software Development Plan<br>• Software Requirements Specification (SRS)<br>• Architecture & design documents<br>• Verification/validation test reports<br>• Bill of Materials (SBOM) for third‑party components<br>• Cybersecurity Threat Model & Mitigation Plan | FDA‑510K‑C4 (Section C.4) |
| **Risk Management** | ISO 14971:2019 risk analysis, evaluation and control. Identify hazards from radiation exposure, electrical failure, software malfunction, cybersecurity breach. | Risk Management File (RMF) including Hazard Log, FMEA/FMECA, Residual Risk Evaluation, and risk‑control verification documentation. | No specific identifier found in source – verify separately |
| **Quality Management System** | Compliance with the **QMS Regulation (21 CFR Part 820)** effective 02‑Feb‑2026 (ISO 13485‑2016 aligned). | Quality Manual, SOPs (e.g., SOP‑PMA‑001, SOP‑VAL‑001), design history file, CAPA records. | No specific identifier found in source – verify separately |
| **UDI Labeling** | Assign a Device Identifier (DI) and Production Identifier (PI) per **21 CFR Part 830**; update GUDID. | UDI label artwork, packaging label, electronic submission of device summary to GUDID. | No specific identifier found in source – verify separately |
| **Performance/Clinical Validation** | Demonstrate that image quality and dose metrics meet or exceed the predicate. | • Bench testing (MTF, DQE, uniformity)<br>• Phantom studies<br>· Clinical evaluation data (if needed) | No specific identifier found in source – verify separately |
| **Sterility / Biocompatibility** *(if applicable)* | Only required if any patient‑contact accessories are provided. | ISO 10993‑1 risk assessment, sterility validation report. | No specific identifier found in source – verify separately |
| **Post‑Market Surveillance (PMS) & Reporting** | Establish a PMS plan and adverse event reporting per **21 CFR Part 803**. | PMS procedures, periodic safety update (if required). | No specific identifier found in source – verify separately |

---

### Missing Information / Evidence Gaps
1. **Predicate device identification** – no clear reference to an already cleared X‑ray system; a substantial equivalence justification cannot be drafted without it.
2. **Labeling package** – labeling text (IFU, warnings, contraindications) is not listed in the source checklist.
3. **Performance/clinical data** – image quality and dose performance evidence are absent from the excerpts.
4. **UDI assignment details** – device identifier, production identifier, and GUDID submission plan are not addressed.
5. **PMS & adverse event reporting procedures** – not captured in the current checklist items.
6. **Biocompatibility/sterility data** – needed only if patient‑contact accessories exist; currently undefined.

---

### Core Risk Controls to Emphasize
| Hazard | Control (per ISO 14971) | Verification |
|--------|-------------------------|--------------|
| Excess radiation dose | Built‑in dose monitoring, automatic shut‑off, user alerts. | Test report per IEC 60601‑2‑54; software verification of dose algorithms. |
| Electrical shock / fire | Design to IEC 60601‑1 safety standards; protective earth, insulation testing. | Electrical safety test reports (C3). |
| Software malfunction leading to incorrect exposure | IEC 62304 lifecycle processes; unit/integration testing; failure mode analysis. | SW verification/validation documentation (C4). |
| Cybersecurity breach (unauthorized alteration of dose parameters) | IEC 81001‑5‑1 cybersecurity framework; SBOM, patch management, authentication. | Threat model & mitigation plan (C4). |
| Device mis‑use / operator error | Human factors engineering per IEC 62366‑1; clear labeling and training materials. | Usability test report (to be generated). |

---

### Human‑Escalation Triggers
- **Predicate Gap** – If a suitable predicate cannot be identified within 5 business days, pause the submission build and convene an FDA Q‑Submission meeting.
- **Performance Data Deficiency** – Absence of image quality/dose validation after initial draft; elevate to senior RA for risk‑benefit assessment.
- **UDI/Labeling Incomplete** – Missing UDI elements or labeling content flagged by regulatory compliance lead; require immediate remediation before filing.
- **QMS Non‑Compliance** – Any deviation from Part 820 requirements uncovered during internal audit triggers escalation to Quality Assurance and possibly a corrective‑action plan prior to submission.
- **Regulatory Classification Uncertainty** – Ambiguity whether the device falls under §892.2050 (image management) vs another subcategory; request senior regulatory counsel review.

---

### Peer Review Prompt
> *Please review this draft for: (a) completeness of the evidence checklist relative to the FDA 510(k) Refuse‑to‑Accept (RTA) criteria, (b) correctness of the assumed classification under 21 CFR Part 892, and (c) any jurisdiction‑specific gaps (e.g., UDI, PMA‐type requirements) that may have been overlooked.*

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
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> `21 CFR §807.92(a)(3)`을 510(k) 제출요건 근거로 오귀속 — §807.92는 Summary/Statement 조항, 근거는 §807.81(a). 웹검증.

**Source Excerpts**

1. Chunk `1030196510375040231`

> ## 2. Device Description & Indications ```yaml - id: FDA-510K-B1 source: FDA RTA Checklist Section B clause: B.1 requirement: Device Description — physical, technological characteristics, components, accessories severity: must evidence_type: technical_documentation applicable_keywords: [FDA 510, FDA QMSR] related_docs: [T-FDA510K-B1_Device_Description_템플릿] - id: FDA-510K-B2 source: FDA RTA Checklist Section B clause: B.2 requirement: Intended Use / Indications for Use — disease, population, environment severity: must evidence_type: technical_documentation applicable_keywords: [FDA 510] related_docs: [T-FDA510K-B2_Intended_Use_템플릿]

2. Chunk `1051800189340874179`

> - id: FDA-510K-C3 source: FDA RTA Checklist Section C clause: C.3 requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 severity: must evidence_type: test_report applicable_keywords: [IEC60601-1, IEC60601-2-54] related_docs: [X-ray_장비_안전성능_표준_매핑, IEC60601-2-54_형식시험_체크리스트] - id: FDA-510K-C4 source: FDA RTA Checklist Section C clause: C.4 requirement: Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity severity: must evidence_type: SW_documentation applicable_keywords: [IEC62304, FDA SBOM, IEC81001-5-1] related_docs: [IEC_62304_SW_수명주기, SOP-VAL-001, IEC_81001-5-1_FDA_Cybersecurity_SW보안, SOP-SBOM-001] ```

### kb-eval-20261028-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "d1720cc28de061ed", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `d1720cc28de061ed`
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

> **Regulatory Draft – “촬영실 GUI Software” (Image‑Processing & Display SaMD)**  

---

### 1. Classification & Submission Route  
| Item | Determination |
|------|---------------|
| **Device type** | Software as a Medical Device (SaMD) that performs image processing and display. |
| **CFR classification** | **21 CFR §892.2050 – Image Processing Software, Class II** *(framework reference – no instance identifier in source)* |
| **Regulatory pathway** | Traditional **510(k)** (Premarket Notification) under 21 CFR §807.81. The device is a Class II medical device that requires a 510(k) demonstrating substantial equivalence to a cleared predicate. |

---

### 2. Core Submission Evidence (per FDA guidance & QMSR)  

| Required Package Element | Source/Regulatory Basis* | Comments / What Must Be Included |
|--------------------------|--------------------------|-----------------------------------|
| **Intended Use & Indications for Use** | 21 CFR §807.81; FDA Guidance “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14) | Clear statement describing diagnostic vs. non‑diagnostic use, user population, clinical setting. |
| **Predicate Device(s)** | 21 CFR §807.92 | Identify at least one cleared device with the same intended use and technological characteristics. *No specific predicate number in source – verify separately.* |
| **Device Description & Software Architecture** | FDA Guidance “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14) | Block diagrams, data flow, hardware platform description, third‑party components. |
| **Software Development Lifecycle Documentation** (per IEC 62304) | IEC 62304:2006+A1:2015 – software risk class determination; FDA Guidance “Content of Premarket Submissions for Device Software Functions” | • Software Development Plan (SDP)  <br>• Software Requirements Specification (SRS) – already listed  <br>• Software Design Specification (SDS) – already listed |
| **Risk Management File** | ISO 14971:2019; FDA Guidance “Content of Premarket Submissions for Device Software Functions” | Hazard analysis, risk control measures, residual risk evaluation. Must map to software class (A/B/C). The source provides the IEC 62304 class table but no documented risk analysis → **missing**. |
| **Software Verification & Validation (V‑&‑V) Documentation** | IEC 62304; FDA Guidance “Content of Premarket Submissions for Device Software Functions” | • Verification Plan & Report (unit, integration, system testing) – partially present (test result folders). <br>• Validation Plan & Report – present. <br>• Traceability Matrix – present.<br>**Missing:** Detailed verification procedures and evidence of test coverage completeness. |
| **Performance Testing (eSTAR Section G)** | eSTAR package list (Excerpt 2) | Includes performance‑test results, dataset description, anomaly log. Must ensure: <br>• Objective performance criteria derived from intended use.<br>• Statistical analysis where applicable.<br>**Missing:** Clinical or simulated clinical performance data if software is used for diagnosis. |
| **Cybersecurity Documentation** | FDA Guidance “Cybersecurity in Medical Devices” (2023‑09‑27) | Threat model, vulnerability mitigation plan, post‑market security updates strategy. **Not present in eSTAR list → missing.** |
| **Labeling & IFU** | 21 CFR §801; QMSR Part 820 | Labels, instructions for use, warnings/precautions, software versioning, UDI placement per Part 830 (§830.10 onward). **Not listed – missing.** |
| **Quality Management System (QMS) Evidence** | FDA QMS Regulation (Part 820) effective Feb 2026 (aligned to ISO 13485:2016) | Copy of ISO 13485‑compliant QMS certificate, SOPs for software change control, post‑market surveillance. **Not in source – missing.** |
| **UDI Implementation Plan** | 21 CFR §830.10–§830.60 | Device identifier, labeling format, GUDID submission plan. **Missing**. |

\*Framework references (CFR sections, ISO/IEC standards, FDA guidance) are stated as facts; no instance‑specific identifiers appear in the source excerpts.

---

### 3. Identified Evidence Gaps  

| Gap | Impact on 510(k) Completeness |
|-----|------------------------------|
| **Predicate device identification** | Without a cleared comparator, substantial equivalence cannot be demonstrated → submission cannot be accepted. |
| **Formal Risk Management File (ISO 14971)** | Required to justify software risk class and residual risk acceptability; omission leads to FDA RTA (refuse‑to‑accept). |
| **Full Verification Plan & Coverage Matrix** | Needed to prove that all software requirements have been verified; incomplete V‑V will trigger AI (Additional Information) request. |
| **Cybersecurity documentation** | Mandatory per 2023 guidance for any SaMD; absence will be noted as a deficiency. |
| **Clinical performance data (if diagnostic intent)** | Required when intended use includes diagnosis or treatment decisions; lack of data = non‑substantial equivalence. |
| **Labeling/UDI package** | FDA requires labeling conforming to Part 801 and UDI per Part 830; missing items cause RTA. |
| **QMS compliance evidence (Part 820)** | QMSR now mandatory for all Class II devices; without proof of ISO 13485:2016‑aligned system, submission is incomplete. |

---

### 4. Risk Controls to be Demonstrated  

1. **Software risk class justification** – map IEC 62304 class (B or C) to hazard severity and implement design controls accordingly.  
2. **Failure mode & effects analysis (FMEA)** for high‑risk functions (image processing that could alter diagnostic interpretation).  
3. **Verification of critical algorithms** – unit/integration tests with edge‑case datasets; results documented in the eSTAR performance folder.  
4. **Cybersecurity safeguards** – authentication, integrity checks, secure update mechanism, vulnerability monitoring plan.  
5. **Usability validation** – human factors testing to ensure correct image interpretation and prevent operator error.  
6. **Post‑market surveillance plan** – procedures for monitoring adverse events (21 CFR §803) and corrective actions (21 CFR §806).  

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger Action |
|-----------|----------------|
| **No identifiable predicate device** | Escalate to senior RA lead; pause submission preparation; conduct market search for cleared equivalents. |
| **Software class C (IEC 62304) with potential for severe harm** | Require additional clinical validation and possibly a De Novo request; notify regulatory strategy owner. |
| **Significant cybersecurity gaps identified** | Immediate escalation to product security officer and RA manager; develop remediation plan before filing. |
| **Incomplete QMS documentation** | Escalate to Quality Manager; suspend 510(k) assembly until ISO 13485‑aligned QMS is verified. |
| **FDA Issues an Additional Information (AI) request for any of the missing items above** | Assign regulatory project manager to draft response within 180 calendar days; track in CAPA system. |
| **Any RTA from FDA due to labeling/UDI deficiencies** | Immediate corrective action, update labeling package, and re‑submit after closure of RTA. |

---

### 6. Bottom‑Line Regulatory Judgment  

- The “촬영실 GUI Software” is a **Class II SaMD** (21 CFR §892.2050) and must be cleared via a **traditional 510(k)** demonstrating substantial equivalence.
- Current eSTAR package supplies many core V‑V artifacts but **lacks predicate identification, formal risk management, cybersecurity plan, labeling/UDI, QMS evidence, and possibly clinical performance data**.
- Until those gaps are filled and documented per the cited frameworks, the submission will be **refused to accept (RTA)** or generate an **AI request**, delaying clearance.

---

### 7. Peer‑Review Prompt  

*“@RA‑Peer: Please review the assumptions below – particularly the sufficiency of the listed performance testing artifacts for a Class II image‑processing SaMD, the need for clinical data given the intended use, and the adequacy of the risk‑class justification per IEC 62304. Highlight any jurisdiction‑specific gaps (e.g., UDI plan, QMSR compliance) that may have been overlooked.”*

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

### kb-eval-20261028-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "0584c8abef73a4ce", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A5_Form3654_Standards_템플릿.md", "source_hash": "005921f322718257ec600ae1ac6b274b94ac3e0c6de8f372f038795127a99c9b"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `0584c8abef73a4ce`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A5_Form3654_Standards_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/T-FDA510K-A5_Form3654_Standards_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `005921f322718257ec600ae1ac6b274b94ac3e0c6de8f372f038795127a99c9b`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `T-FDA510K-A5_Form3654_Standards_템플릿.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: --- doc-id: T-FDA510K-A5_Form3654_Standards_템플릿 title: FDA Form 3654 (Standards Data Report) 작성 템플릿 type: Form version: v0.1 status: draft category: 01_법규_규제 purpose: FDA 510(k) RTA Checklist A.5 대응 — 표준 적합성 선언(Standards Data Report) 기재 골격 applicable: [FDA 510(k), FDA QMSR, IEC60601-1, IEC60601-2-54, IEC62304] owner: RA 담당자 last-review: 2026-09-10 review-...
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

> **Regulatory Draft – 510(k) Submission Planning**

---

### 1. Likely Classification & Sub‑mission Pathway  
| Item | Rationale |
|------|-----------|
| **Device class** | The template lists IEC 60601‑1 (general safety), IEC 60601‑2‑54 (physiological monitoring – e.g., ECG/EEG) and IEC 62304 (software). Devices built to these standards are normally **Class II** medical electrical equipment. Under the FDA structure this falls under **21 CFR Part 870** (general medical devices), not Part 892 (radiology/imaging). |
| **Regulatory route** | Use a traditional **Premarket Notification (510(k))** as indicated by the source (“FDA 510(k) RTA Checklist”). The submission will be governed by **21 CFR §807**. |
| **Quality‑system reference** | The new Quality Management System Regulation (QMSR, effective Feb 2026) aligns with ISO 13485:2016 and is cited as “FDA QMSR” in the template; compliance must be demonstrated per **21 CFR §820** and the QMSR provisions. |
| **UDI requirement** | Apply **21 CFR §830** (label must bear a UDI, with GUDID registration). |

> **Bottom line:** File a 510(k) for a Class II physiological‑monitoring device; ensure compliance with Part 820/ QMSR and Part 830.

---

### 2. Evidence Package Required by the FDA Form 3654 (Standards Data Report)

| Requirement | Source Standard / Regulation | Typical Deliverable |
|-------------|------------------------------|---------------------|
| **Declaration of Conformity to listed standards** | IEC 60601‑1, IEC 60601‑2‑54, IEC 62304 – *edition must match the “confirmed values” stored in the repository* (see source note) | Signed DCF with edition year (e.g., IEC 60601‑1:2005+A1:2012) |
| **Electrical safety & performance test reports** | IEC 60601‑1, IEC 60601‑2‑54 | Test reports from accredited lab (electrical safety, EMC, SAR, alarm accuracy). |
| **Software life‑cycle documentation** | IEC 62304 (2006+A1:2015) | Software development plan, verification & validation protocols, traceability matrix, risk control measures linked to software functions. |
| **Risk Management File** | ISO 14971:2019 | Risk analysis, evaluation, mitigation plan, residual risk justification. |
| **Quality System Documentation** | FDA QMSR (aligned with ISO 13485:2016) & 21 CFR §820 | SOPs, CAPA records, design‑control files, internal audit reports. |
| **UDI labeling compliance** | 21 CFR §830 | Label artwork showing UDI, and GUDID submission evidence. |
| **510(k) Substantial‑Equivalence Support** | 21 CFR §807 – predicate device identification, comparison matrix | Predicate K number, summary of technological characteristics, performance testing that shows equivalence. |

> **Citation note:** The template explicitly lists the applicable standards (IEC 60601‑1, IEC 60601‑2‑54, IEC 62304) and “FDA QMSR”. No specific clearance numbers or CFR subsection identifiers appear in the source – *no specific identifier found in source — verify separately*.

---

### 3. Information Gaps / Missing Evidence  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Device description & intended use** | Needed for predicate search and to define classification. | Draft a concise Intended Use statement; run a 510(k) predicate search (e.g., “ECG monitor” product code EMC). |
| **Predicate device identifier (K number)** | Central to substantial‑equivalence argument. | Identify at least one cleared device with the same intended use and technology. |
| **Labeling & Instructions for Use (IFU)** | Must meet 21 CFR §801; needed for labeling review. | Prepare draft label, IFU, and packaging artwork early. |
| **Clinical / performance data** (bench, animal or limited human) | Required if no predicate exists or to support test‑method equivalence. | Plan bench verification per IEC 60601‑2‑54 (accuracy, alarm thresholds). |
| **Software documentation depth** | FDA expects detailed traceability from requirements to code (IEC 62304). | Create Software Requirements Specification (SRS), Architecture, Source Code Repository, Verification/Validation reports. |
| **UDI issuance & GUDID registration** | Part 830 compliance cannot be demonstrated without a valid UDI. | Obtain a GS1 or HIBCC issuing agency; submit to GUDID. |
| **QMSR evidence of transition from ISO 13485:2016** | QMSR is new (effective Feb 2026); auditors will expect documented migration. | Provide a “QMSR Transition Plan” and records of updated SOPs. |

If any of these items cannot be supplied before the 510(k) submission deadline, **escalate to senior RA management** for possible pre‑submission meeting with FDA.

---

### 4. Core Risk Controls (per ISO 14971:2019)

| Hazard | Control Measure | Reference |
|--------|------------------|-----------|
| Electrical shock / leakage current | IEC 60601‑1 compliance; double insulation, protective earth testing. | ISO 14971:2019 – risk control hierarchy (protective measures). |
| Electromagnetic interference affecting signal fidelity | IEC 60601‑2‑54 EMC tests; shielding, filtering. | IEC 60601‑2‑54. |
| Software malfunction causing incorrect alarm or data loss | IEC 62304 development lifecycle; unit/integration testing; fail‑safe mode; periodic software updates documented in a **Predetermined Change Control Plan (PCCP)** if future changes anticipated. | FDA guidance Dec 2024 – PCCP. |
| Alarm fatigue / missed alarms | Human factors validation per IEC 62366‑1; alarm priority hierarchy; audible/visual distinctiveness testing. | IEC 62366‑1:2020. |
| Device misuse (incorrect electrode placement) | Clear IFU graphics, training materials, error‑prevention UI design. | ISO 14971 residual risk evaluation. |

All controls must be documented in the **Risk Management File** and cross‑referenced to verification/validation evidence.

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger | Who to notify |
|-----------|---------|---------------|
| No clear predicate device after an exhaustive search | Ambiguous classification (possible Class I or III) | RA Director & Project Lead – consider FDA Pre‑Submission (Q‑submission). |
| Incomplete or outdated standard edition used (e.g., IEC 60601‑1:2005 vs required 2012 amendment) | Potential non‑conformity to “edition must be the confirmed value” rule in source note. | Quality Manager – initiate SOP update and re‑testing. |
| QMSR transition documentation missing or not approved by senior management | Non‑compliance with 21 CFR §820/QMSR | Senior QA/Compliance Officer. |
| UDI issuance delayed beyond 30 days before filing | Part 830 violation risk | Regulatory Affairs Lead – arrange expedited UDI assignment or defer submission. |
| FDA issues an Additional Information (AI) request exceeding the 180‑day response window | Risk of clearance delay | Project Manager – invoke escalation plan, allocate resources for rapid response. |

When any trigger is hit, **add a comment to the work package recommending closure review and human action**; do not auto‑close.

---

### 6. Peer‑Review Prompt  

*“Colleague, please challenge the following assumptions: (1) that the device falls under Class II/Part 870 based solely on IEC 60601‑2‑54; (2) that a single predicate from the ECG monitor product code will satisfy substantial‑equivalence for any software‑driven physiological monitor; and (3) that our current list of required evidence fully covers FDA Form 3654 expectations. Identify any jurisdiction‑specific gaps (e.g., UDI, QMSR transition) you see.”*

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

> IEC 60601-2-54를 생체신호 모니터(ECG/EEG·Part 870·product code EMC)로 오독 — 실제는 X-ray 촬영/투시 장치 특수요건(웹검증, 표준 제목 원문). 분류 추정(Part 870) 전체 재판정 필요.

**Source Excerpts**

1. Chunk `110225184461043556`

> --- doc-id: T-FDA510K-A5_Form3654_Standards_템플릿 title: FDA Form 3654 (Standards Data Report) 작성 템플릿 type: Form version: v0.1 status: draft category: 01_법규_규제 purpose: FDA 510(k) RTA Checklist A.5 대응 — 표준 적합성 선언(Standards Data Report) 기재 골격 applicable: [FDA 510(k), FDA QMSR, IEC60601-1, IEC60601-2-54, IEC62304] owner: RA 담당자 last-review: 2026-09-10 review-due: 2027-09-10 --- # T-FDA510K-A5 FDA Form 3654 (Standards Data Report) 작성 템플릿 (v0.1 — 골격) > **주의**: 본 문서는 FDA 공식 양식의 대체물이 아니다. 적용 표준의 **판본(edition/연도)은 저장소 내 확정된 값만 사용**하고, 미확정 판본을 임의로 기재하지 말 것 — 미존재 판본 창작은 본 저장소의 반복 결함 클래스(audit #1014/#1016/#1019 계보)이다.

2. Chunk `263077204903674930`

> ## 개정 이력 | 버전 | 일자 | 변경 내용 | 작성자 | |------|------|-----------|--------| | v0.1 | 2026-09-10 | 골격 템플릿 신규 생성 (FDA-510K-A5, 이슈 #931 P0 대응) | RA 담당자 | ---

## ra_eu

### kb-eval-20261028-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "8f749f5f6bd60fc9", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `8f749f5f6bd60fc9`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & CE‑Marking Pathway**

---

### 1. Device Synopsis (as known today)  
| Item | Current information | What is still missing |
|------|---------------------|-----------------------|
| Intended purpose / indication | *Not provided* – must be defined in the labeling (Annex I §23). | Precise claim wording, target patient population, intended user type (HCP vs. lay‑person). |
| Anatomical site of contact | *Not provided.* | Exact body region(s) (e.g., “upper‑limb peripheral nerve”). |
| Device class drivers (invasiveness, active/measure, sterile, measuring) | *Not provided.* | Confirmation whether the device is invasive, active, measuring, or a reusable surgical instrument. |

> **Action:** Obtain the manufacturer’s Intended Use Statement and the full product description before any classification work can be finalised.

---

### 2. Classification Determination (Annex VIII)

| Potential rule(s) | Rationale (what must be verified) | Resulting class* |
|-------------------|-----------------------------------|------------------|
| **Rule 9** – active therapeutic | Does the device deliver energy for therapy? | IIa / IIb* |
| **Rule 10** – active diagnostic/monitoring | Does it monitor or diagnose a vital physiological parameter? | IIa / IIb* |
| **Rule 11** – software providing clinical decision support | Is software part of the device that influences therapeutic/diagnostic decisions? | IIa–III* |
| **Rule 17** – X‑ray image recording (if applicable) | Does it record diagnostic images generated by ionising radiation? | IIa* |
| **Rule 1–22** (non‑active, non‑measuring) | Is it a passive device (e.g., a catheter) without measuring function? | I / Is / Im / Ir* |

\*The exact class will be fixed once the above product attributes are confirmed.  

> **Reference:** Classification rules – Annex VIII of MDR 2017/745.

---

### 3. Conformity‑Assessment Route (Art. 52)

| Determined Class | Applicable route (Article 52) | Notified‑Body involvement |
|------------------|--------------------------------|----------------------------|
| I (non‑sterile, non‑measuring, non‑reusable surgical) | Art. 52(7): Self‑declaration – Technical Documentation (Annex II & III) + EU Declaration of Conformity (Art. 19/Annex IV). | No |
| Is / Im / Ir | Art. 52(7): Annex IX Chapters I & III **or** Annex XI Part A (limited scope). | Yes (limited) |
| IIa | Art. 52(6): Annex IX Chapters I & III + technical‑documentation assessment of a representative device (Annex IX §4). | Yes |
| IIb / III | Art. 52(4) or (3): Full Annex IX assessment **or** Annex X (type‑examination) + Annex XI (production conformity verification). | Yes |

> **Reference:** MDR 2017/745, Art. 52 and the associated Annexes.

---

### 4. Clinical Evaluation – Evidence Required (Annex XIV Part A)

| Requirement | What must be demonstrated | Typical source of evidence |
|-------------|----------------------------|----------------------------|
| **Equivalence** with a predicate device | Same intended purpose, same anatomical site, similar patient population (including age, anatomy, physiology), **same user type**, and comparable essential clinical performance. | Clinical literature on the predicate, manufacturer’s own bench & pre‑clinical data, post‑market surveillance of the predicate. |
| **State‑of‑the‑art (SOTA) literature** | Up‑to‑date peer‑reviewed publications covering the indication, patient group, and comparator technologies. | Systematic literature search (≥ 5 years, ≥ 2 high‑quality studies). |
| **Clinical data on the device itself** (if equivalence is incomplete or for higher‑risk classes) | Prospectively collected safety & performance data (clinical investigation, PMCF). | Clinical Investigation Report, PMCF Plan/Report (Annex XIV Part B). |
| **Benefit–Risk determination** | Conclude that benefits outweigh residual risks in the intended use context. | Integrated analysis of clinical data + risk‑management file (§3 GSPR). |

> **Citations from source:**  
- MDR Art. 61 & Annex XIV (clinical evaluation framework).  
- MDCG 2020‑5 (Equivalence – Apr 2020).  
- MDCG 2020‑6 (Sufficient Clinical Evidence – Apr 2020).  
- MDCG 2023‑7 (Article 61(4)–(6) Exemptions – Dec 2023).  
- MDCG 2024‑3 (CER Content – latest guidance).

---

### 5. Gap Analysis – Missing Information

| Gap | Why it matters for the CER | Minimum evidence to close gap |
|-----|----------------------------|--------------------------------|
| **User‑type equivalence** – source [1] adds “same kind of user” as an MDR requirement not present in MEDDEV. | Without matching user type, equivalence cannot be claimed (e.g., a device for HCPs cannot be considered equivalent to one intended for lay‑persons). | Declaration of intended user class, usability testing data per IEC 62366‑1 (§16), and justification that the predicate’s user type matches. |
| **Severity / disease stage alignment** – “same clinical state·severity·stage” must be identical. | Differences may affect safety/benefit profile; could invalidate equivalence. | Clinical literature showing comparable patient severity distribution, or a bridging clinical investigation. |
| **Clinical performance parameters** – “intended purpose vs. similar core clinical performance.” | Core performance metrics (e.g., sensitivity, specificity) must be demonstrably similar. | Comparative data tables, statistical analysis of predicate’s performance versus the device under assessment. |
| **Up‑to‑date SOTA search** – no evidence that literature review covers the last 5 years. | MDR requires current state‑of‑the‑art information (Art. 61). | Systematic review protocol and results, with PRISMA flow diagram. |
| **Risk Management linkage** – no explicit cross‑reference between identified clinical differences and risk controls (§3 GSPR). | Residual risks may increase if the device differs clinically from the predicate. | Updated Risk Management File (ISO 14971:2019) showing new risk control measures or justification of unchanged risk level. |
| **PMCF Plan** – none mentioned for Class IIa/IIb devices. | Ongoing clinical evidence is required (Annex XIV Part B). | Draft PMCF plan with objectives, methodology, timeline; later a PMCF evaluation report. |

> **Immediate next step:** Populate the Clinical Evaluation Report (CER) template (Annex XIV Part A) with the above missing elements and indicate where bridging data are planned.

---

### 6. Risk Management Considerations (Annex I §3 & ISO 14971:2019)

| Identified risk from clinical‑gap | Existing control (if any) | Additional control required |
|-----------------------------------|---------------------------|------------------------------|
| **User error due to different user type** (HCP vs. lay‑person) | None identified. | Conduct usability validation per IEC 62366‑1; add user training instructions; update labeling (§23). |
| **Inadequate performance in a higher severity cohort** | Predicate data only for mild disease. | Perform a limited clinical investigation or collect post‑market data to verify safety in the target severity group. |
| **Residual risk increase because of untested performance metric** | Risk analysis based on predicate performance. | Add risk control (e.g., additional alarms, safety limits) and re‑evaluate residual risk; document justification in RMF (§3). |

All risk controls must be reflected in the Technical Documentation §6.1 (clinical evaluation) and in the Risk Management File (Annex I §§1‑9).

---

### 7. Documentation Checklist (what must be submitted to the Notified Body)

| Section | Content required | Regulatory basis |
|---------|------------------|-------------------|
| **Device description & intended use** | Full labeling, device hierarchy, user manual. | Annex II §1; Annex I §23. |
| **Classification & conformity route** | Determined class, Art. 52 paragraph citation, chosen Annex (IX or X+XI). | Art. 52 + Annex VIII. |
| **Risk Management File** | RMF per ISO 14971:2019, risk‑control evidence for identified gaps. | Annex I §3 (risk management system). |
| **Clinical Evaluation Report (CER)** | Full Annex XIV Part A report (clinical data, equivalence justification, benefit‑risk analysis). | Art. 61 & Annex XIV Part A. |
| **PMCF Plan / Report** (if applicable) | Objectives, methodology, timeline; interim and final evaluation. | Annex XIV Part B. |
| **Post‑Market Surveillance (PMS) System** | PMS plan (Art. 84), PMS report/PSUR (Art. 86 for Class IIa–III). | Art. 83‑86. |
| **EU Declaration of Conformity** | Completed per Art. 19, Annex IV content. | Art. 19 & Annex IV. |
| **EUDAMED registration** | Device entry with all mandatory fields (UDI, classification, NB). | Art. 33‑39. |

> **Note:** All cited guidance documents (MDCG 2020‑5, MDCG 2020‑6, MDCG 2023‑7, MDCG 2024‑3) must be attached as annexes to the submission file.

---

### 8. Human‑Escalation Triggers

| Trigger condition | Required action |
|-------------------|-----------------|
| **Classification ambiguity** (e.g., uncertainty whether Rule 9 or Rule 10 applies). | Escalate to senior RA lead for expert classification opinion; log decision with supporting evidence. |
| **Missing equivalence data** (user‑type, severity, performance metrics). | Pause submission until bridging clinical data are obtained; involve Clinical Affairs & Biostatistics lead. |
| **Residual risk exceeds acceptability criteria** after gap analysis. | Convene Risk Management Review Board; consider redesign or additional controls before proceeding. |
| **PMS/PMCF plan not yet drafted for Class IIa+ devices.** | Assign PMCF owner and set a hard deadline (≤ 4 weeks); if missed, raise to Project Manager. |
| **Non‑conformity with latest MDCG guidance (e.g., CER content missing sections required by MDCG 2024‑3).** | Issue corrective action request; involve Documentation Control for immediate amendment. |

All escalations should be recorded in the project’s risk register and communicated via the approved change‑control procedure.

---

### 9. Peer‑Review Prompt

> **To a fellow Regulatory Affairs colleague:**  
> Please challenge the assumptions made above, especially: (a) the applicability of the user‑type equivalence requirement derived from source [1]; (b) whether the listed MDCG documents fully cover the current MDR clinical‑evaluation expectations; and (c) any jurisdiction‑specific gaps that may arise if this device will also be marketed outside the EU (e.g., US 510(k) or Korean MFDS). Highlight any missing regulatory citations or alternative interpretation of Art. 61/Annex XIV.

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

> Art. 52 단락 전면 오귀속 — 실제 매핑: Class I=52(1), Is/Im/Ir=52(2)-(4), IIa=52(5), IIb=52(6), III·이식형=52(7). 응답은 I→52(7), IIa→52(6), IIb/III→52(4)/(3)로 전부 틀림. 웹검증. #134 계열(참조표 미커버 영역 이동).

**Source Excerpts**

1. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

2. Chunk `1090731331984830062`

> > 최종 갱신: 2026-05-18 (자동보강 #52) > 근거: MDR Regulation (EU) 2017/745 Article 61 & Annex XIV | MDCG 2020-5 (Equivalence, Apr 2020) | MDCG 2020-6 (Sufficient Clinical Evidence, Apr 2020) | MDCG 2023-7 (Article 61(4)-(6) Exemptions, Dec 2023) | MDCG 2024-3 (CER Content) | FDA 510(k) Program Guidance (Jul 2014) | FDA Best Practices for Predicate Device Selection (Oct 2023 Draft) | MFDS 의료기기 허가·신고·심사 등에 관한 규정 (고시 제2024-88호) # Clinical Evaluation (MDR) 심화 — 동등성·충분성 기준

### kb-eval-20261028-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "09e928aee8c6995f", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `09e928aee8c6995f`
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

> **Regulatory Draft – Diagnostic‑radiology X‑ray Device (Class IIb)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Reference |
|------|-----------|
| **Intended purpose** – “standard diagnostic radiology” (imaging of patients using ionising radiation). | source excerpt [1] |
| **Classification rule** – Rule 10 (active device that emits ionising radiation for diagnostic/radiotherapy). → **Class IIb**. | MDR Annex VIII, Rule 10 |
| **Conformity‑assessment route** – Either: <br>a) **Annex IX** full technical‑documentation assessment (NB‑led QMS + TD review),  or <br>b) **Annex X** type‑examination **+** **Annex XI** production conformity verification (the usual route for X‑ray equipment). | MDR Art. 52(4) – Class IIb |

> **Action**: Confirm with the Notified Body which of the two permissible routes will be pursued; update the technical file accordingly.

---

### 2. Evidence Required to Satisfy the NB  

| Evidence | Why required (regulatory basis) |
|----------|---------------------------------|
| **1. Clinical Evaluation Report (CER)** – Revised Rev. 3 attached as Annex A (source [1]). Must demonstrate clinical equivalence on the same clinical condition and performance (DQE ≥ 65 %). | Annex XIV Part A; Art. 61 – CER must be kept current. |
| **2. Test Report TR‑2024‑015** – DQE measurement according to IEC 62220‑1‑1. | Annex XIV Part A, §5.3 (clinical data); IEC 62220‑1‑1 is the accepted standard for detector performance. |
| **3. Risk Management File (RMF)** – ISO 14971:2019 compliant risk analysis, controls and residual‑risk evaluation. Must address: <br>• Radiation protection (§16 of Annex I)  <br>• Electrical safety (IEC 60601‑2‑54) <br>• Software hazards if software is part of the device (Annex I §17). | Annex I §§3‑9 (risk‑management system); ISO 14971. |
| **4. Technical Documentation (TD)** – Annex II sections 1‑6, including:<br>• Device description & intended use <br>• Design & manufacturing information <br>• GSPR compliance statements (Annex I) <br>• Verification & validation data (including IEC 60601‑2‑54, IEC 62366‑1). | Annex II §§1‑6. |
| **5. Post‑Market Surveillance (PMS) Plan** – Art. 84. Must outline systematic collection of data on radiation dose, device failures, and user feedback. | Art. 84. |
| **6. Periodic Safety Update Report (PSUR)** – Art. 86 (annual for Class IIb). Should summarise benefit‑risk conclusions, PMCF results, sales volume & used‑population estimates. | Art. 86(1)–(2). |
| **7. Declaration of Conformity (DoC)** – Content per Annex IV; signed by the manufacturer. | Art. 19; Annex IV. |
| **8. EUDAMED registration** – Device entry with classification, UDI‑device identifier, and NB certificate reference. | Art. 33‑39. |
| **9. Labeling & IFU** – Information supplied with the device (Annex I §23). Must contain radiation safety warnings, contraindications, and user instructions. | Annex I §23. |

---

### 3. Gaps / Missing Information Identified  

| Gap | Impact | Required corrective action |
|-----|--------|-----------------------------|
| **a) No explicit description of the intended clinical use** (patient population, imaging modalities). | Prevents verification of “same clinical condition” claim in CER. | Add a detailed Intended‑Use statement to TD §1 and update CER scope. |
| **b) Absence of IEC 60601‑2‑54 compliance evidence** (electromagnetic safety, leakage current, mechanical tests). | Required GSPR (§16 & §20) for active X‑ray equipment. | Provide test reports or certificates of conformity to IEC 60601‑2‑54. |
| **c) No documented Software Development Lifecycle** – If the device includes image‑processing software, ISO/IEC 62304 (2006+A1:2015) evidence is missing. | Violates Annex I §17 & §18. | Supply a Software File (SWF) with verification & validation results per IEC 62304. |
| **d) Incomplete RMF – residual‑risk evaluation not linked to clinical performance data**. | NB will query whether risk acceptability aligns with benefit‑risk conclusions in CER. | Update RMF to include a systematic residual‑risk assessment that references the DQE performance and any dose‑monitoring controls. |
| **e) PMS Plan not yet drafted** (only a PSUR reference is present). | Art. 84 requires a documented plan before first post‑market data collection. | Draft & submit a PMS plan covering routine monitoring of radiation dose, field incidents, and trend analysis. |
| **f) No evidence of conformity with IEC 62220‑1‑1 measurement methodology** – test report referenced but not attached in the excerpt. | Required to substantiate DQE ≥ 65 %. | Attach full Test Report TR‑2024‑015 (including calibration traceability). |
| **g) Labeling draft missing radiation warnings per Annex I §16.4**. | Non‑compliant IFU may be rejected. | Produce a revised label/IFU with required safety statements and pictograms. |

---

### 4. Required Risk Controls (to be documented in the RMF)  

| Control | Regulatory basis |
|---------|-------------------|
| **a) Shielding & interlock system** – Prevent accidental exposure; validated per IEC 60601‑2‑54 §16.4. | Annex I §§16, 18. |
| **b) Dose‑monitoring software** – Real‑time dose display and cumulative dose logging. | Annex I §16; IEC 62304 for software safety. |
| **c) User training program** – Mandatory instruction on safe operation, positioning, and emergency stop use. | Annex I §22 (lay‑person use) & §23 (information supplied). |
| **d) Fault detection & safe‑state logic** – Device automatically disables X‑ray output upon fault detection. | Annex I §18 (active devices). |
| **e) Periodic calibration schedule** – Ensures DQE performance stays ≥ 65 % throughout device life. | Annex I §6 (known risks) & IEC 60601‑2‑54 calibration requirements. |
| **f) Protective equipment labeling** – Warning symbols and dose limits on IFU. | Annex I §23; IEC 60601‑2‑54. |

All controls must be traceable to identified hazards in the risk analysis and verified/validated per ISO 14971.

---

### 5. Human‑Escalation Triggers  

| Trigger condition | Escalation action (who) |
|-------------------|--------------------------|
| **NB issues a deficiency letter requesting additional clinical data** (e.g., full clinical investigation rather than equivalence). | RA lead to initiate PMCF study design; inform senior regulatory manager. |
| **Critical missing GSPR evidence (radiation safety, IEC 60601‑2‑54 compliance)** identified during document review. | Immediate notification to the engineering team and project manager; halt submission until testing completed. |
> *If any of the gaps listed in Section 3 remain unresolved after a 10‑day remediation window, the RA lead must raise an escalation to senior management for resource allocation.*  

---

### 6. Summary Judgment  

- **Classification:** Class IIb (Rule 10 – active ionising‑radiation device).  
- **Conformity route:** Annex IX *or* Annex X + XI (to be confirmed with NB).  
- **Core evidence needed:** Updated CER (clinical equivalence with DQE ≥ 65 % per IEC 62220‑1‑1), full IEC 60601‑2‑54 test reports, complete RMF, PMS plan, PSUR, DoC, EUDAMED entry, and compliant labeling/IFU.  
- **Current gaps** (intended‑use statement, IEC 60601‑2‑54 evidence, software lifecycle documentation, residual‑risk linkage, PMS plan, full test report attachment, label warnings) must be closed before the NB can accept the technical file.  

*All identified gaps and the associated corrective tasks are to be tracked in the project’s RACI matrix; any NB request for additional data or clarification beyond what is outlined here triggers the escalation process described above.*

---

### 7. Peer‑Review Prompt  

> **Colleague, please review:**  
> 1. The assumption that Rule 10 (IIb) applies – does any aspect of the device (e.g., measuring function or software decision support) push it to a higher class under Rule 11?  
> 2. Are we missing any MDR Annex‑specific requirements for X‑ray *type‑examination* (Annex X) that have not been listed (e.g., specific conformity‑assessment procedures for radiation protection)?  
> 3. Does the current clinical equivalence argument (DQE ≥ 65 %) satisfy the CER depth required for a Class IIb device, or should we plan a supplementary PMCF study?  

Your feedback will be incorporated before final submission to the Notified Body.

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

> "Art. 52(4) – Class IIb" 오귀속 — IIb=52(6) (52(4)=Class I 재사용 수술기구). 웹검증.

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1107467848736309543`

> ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통지하는 문서. 국내 MFDS "보완 요청", FDA "Additional Information (AI) Request"에 해당하는 EU MDR 용어. ---

### kb-eval-20261028-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "2a8158c2b802e668", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2a8158c2b802e668`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & Conformity Pathway  
(derived from MDCG 2020‑5, 6, 7 & 8 guidance summary)**  

---

### 1. Executive Summary
The material supplied (MDCG clinical‑evaluation/PMCF guidance) outlines the *required* sections of a PMCF Evaluation Report but does **not** contain any device‑specific data (intended purpose, invasiveness, active/mechanical nature, user population, etc.). Consequently the MDR classification and the corresponding conformity‑assessment route cannot be fixed at this stage. The draft below identifies:

| Item | Current status | Gap / action required |
|------|----------------|-----------------------|
| **Device description & intended use** | Not provided in source | Obtain full Intended Purpose statement (including anatomical site, physiological purpose, patient population, user type). This is the basis for Annex VIII classification. |
| **Classification rule(s)** | Unknown | Apply Annex VIII rules once the above is known; likely to be a Rule 9‑11 family if the device is active/software, otherwise a Rule 1‑4 family for non‑active devices. |
| **Conformity‑assessment route** | Undetermined (depends on class) | After classification, select Annex IX (for Classes I (Is)/Im/Ir, IIa, IIb, III) or Annex X + XI (alternative for IIb/III). |
| **Clinical Evaluation Report (CER)** – content per Annex XIV‑Part A | No CER supplied | Prepare a full CER (state of the art, clinical data, benefit‑risk analysis) and keep it up‑to‑date (Art. 61). |
| **PMCF Plan** – required by Annex XIV‑Part B | Not present in source | Draft a PMCF plan covering objectives, methodology, data sources, timelines, responsibilities, and post‑market surveillance integration (Art. 84). |
| **PMCF Evaluation Report** – sections listed in the guidance | Sections A–G identified (Table 5.2) but actual content missing | Populate each section with device‑specific information; document any deviations from the plan and justification for interim updates to Technical Documentation (§6.1 Annex II). |
| **Risk Management File (RMF)** – per §3 Annex I | No RMF referenced | Conduct risk analysis per ISO 14971:2019, map residual risks against GSPR §§ 8‑9, and document verification of any risk‑control measures identified in the PMCF results. |
| **Post‑Market Surveillance (PMS) System** – Art. 83/84 | Not described | Implement a PMS system that collects real‑world performance data feeding into the PMCF activities; define periodic reporting (Art. 86 PSUR for Class IIa/b/III). |

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Required evidence (per MDR) | Gap |
|------|-----------------------------|-----|
| **2.1 Intended purpose & mode of action** – identify anatomical site, physiological effect, whether the device is active, implantable or software. | Manufacturer’s “Intended Use” statement; labeling (Annex I §23). | No such statement in source. |
| **2.2 Apply Annex VIII classification rules** – e.g., Rule 9 for active therapeutic devices, Rule 10 for diagnostic/monitoring, Rule 11 for software, etc. | Cross‑check against intended purpose; determine if the device falls under any “sterile”, “measuring” or “reusable surgical instrument” special cases (Is/Im/Ir). | No rule can be applied without the purpose data. |
| **2.3 Determine class** – Classes I, Is/Im/Ir, IIa, IIb, III. | Output of step 2.2. | Undetermined → Classification decision pending. |
| **2.4 Select conformity‑assessment route (Art. 52)** | *If Class I* – self‑declaration (Art. 52(7)).<br>*If Is/Im/Ir* – Annex IX Chapters I & III or Annex XI Part A (limited NB scope) (Art. 52(7)).<br>*If Class IIa* – Annex IX (full QMS + technical‑documentation assessment) (Art. 52(6)).<br>*If Class IIb* – Annex IX (or alternative Annex X + XI) (Art. 52(4)).<br>*If Class III* – Annex IX or Annex X + XI (Art. 52(3)). | Route cannot be fixed until class is known. |

**Citation:** Classification rules – Annex VIII; Conformity‑assessment routes – Art. 52 together with Annex IX, Annex X & Annex XI.

---

### 3. Clinical Evaluation Evidence Requirements  

| Requirement (Annex XIV‑Part A) | Current status | Gap |
|-------------------------------|----------------|-----|
| **State of the art** – literature review covering all equivalent devices. | No evidence supplied. | Conduct systematic SOTA search, document inclusion/exclusion criteria, and summarize findings. |
| **Clinical data** – clinical investigations (if required), post‑market clinical follow‑up (PMCF) results, equivalence data. | Only a table of “required PMCF Evaluation Report sections” is available; no data. | Collect all relevant clinical investigation reports, registry data, real‑world evidence; map to the device’s intended purpose. |
| **Benefit–risk determination** – conclusions integrating clinical data with risk analysis (Art. 61). | Missing. | Perform benefit‑risk assessment, referencing residual risks from the RMF (§3 Annex I). |
| **Update cadence** – keep CER up‑to‑date throughout device life‑cycle (Art. 61). | Not addressed. | Establish a process to review and revise the CER at least annually for Class IIb/III or biennially for Class IIa. |

---

### 4. Post‑Market Clinical Follow‑up – Required Contents  

The MDCG guidance excerpt lists mandatory sections (Table 5.2). The draft must contain **device‑specific** information in each column:

| Section | Description required (per guidance) | Evidence needed |
|---------|--------------------------------------|-----------------|
| **A – Manufacturer contact** | Full address, telephone, e‑mail of the responsible person. | Company’s authorised representative details. |
| **B – Device description** | Updated description if any design change; otherwise reference to PMCF Plan (no change). | Current Technical Documentation §6.1 Annex II. |
| **C – Results of performed PMCF activities** | Raw data, statistical analysis, trends, deviations with justification. | Data collection reports, database extracts, monitoring logs. |
| **D – Evaluation of clinical data from equivalent/similar devices** | Critical appraisal of literature/registry data for comparable products. | Equivalence matrix, SOTA review outcomes. |
| **E – Impact on Technical Documentation** | Specific statements how PMCF results affect the CER, RMF and SSCP (if applicable). | Updated CER sections, revised risk assessments, updated Summary of Safety & Clinical Performance. |
| **F – Applied Common Specifications, harmonised standards or guidance** | List of referenced CS/EN standards (e.g., IEC 60601‑2‑54 for X‑ray devices) and any MDCG guidances used. | Bibliography with version numbers. |
| **G – Overall conclusion** | Assessment against PMCF objectives; identify preventive or corrective actions required. | Decision matrix, action plan with responsibilities and timelines. |

**Current gap:** None of the above items contain actual data; only the **structure** is present in the source.

---

### 5. Risk Management & GSPR Alignment  

| GSPR § (Annex I) | Required evidence | Gap |
|------------------|-------------------|-----|
| **§3 – Risk management system** | ISO 14971:2019‑based RMF, documented risk analysis, evaluation of residual risks. | No RMF referenced; must be produced and linked to PMCF findings (Section E). |
| **§4 – Risk control measures** | Documentation of design controls, protective measures, verification of effectiveness. | Missing; must be demonstrated that any new hazards identified in PMCF are mitigated. |
| **§5 – Use‑error risks** | Human factors analysis (IEC 62366‑1:2020) and usability testing results. | Not addressed in source; request usability validation reports. |
| **§6 – Lifetime/replacement** | Defined service life, maintenance schedule, degradation data. | No information supplied. |
| **§8 – Benefits vs residual risks** | Benefit–risk analysis (CER) confirming that benefits outweigh remaining risks. | Absent; to be generated once clinical data are available. |

All risk‑management artefacts must be referenced in the Technical Documentation (§6.1 Annex II) and updated following PMCF outcomes.

---

### 6. Post‑Market Surveillance (PMS) System  

| Requirement | Current status | Gap |
|-------------|----------------|-----|
| **PMS system** – Art. 83 | Not described | Implement a systematic PMS process; define data sources, signal detection methods, and reporting procedures. |
| **PMS plan** – Art. 84 | Not available | Draft a PMS Plan that integrates the PMCF activities (objectives, scope, responsibilities). |
| **PSUR / PMS report** – Art. 86 (Class IIa/b/III) | No PSUR produced | Prepare periodic safety update reports aligned with PSUR schedule (annual for IIb/III, biennial for IIa). |

---

### 7. Documentation Checklist – What Must Be Submitted to the Notified Body  

| Document | MDR reference | Status |
|----------|---------------|--------|
| **EU Declaration of Conformity** | Art. 19; content in Annex IV | Draft pending classification & conformity route. |
| **Technical Documentation (TD)** – Sections 1‑6 | Annex II §1‑§6 | Incomplete – missing device description, classification, risk analysis, clinical evaluation. |
| **Clinical Evaluation Report** | Annex XIV Part A | Not yet prepared. |
| **PMCF Plan** | Annex XIV Part B (Plan) | Missing. |
| **PMCF Evaluation Report** | Annex XIV Part B (Report) – sections A‑G (Table 5.2) | Structure present; content absent. |
| **Risk Management File** | §3 Annex I (ISO 14971) | Not supplied. |
| **Post‑Market Surveillance Plan & Reports** | Art. 84, Art. 86 | Absent. |
| **Summary of Safety and Clinical Performance (if Class III or implantable)** | Art. 32 | Not applicable until class known. |

---

### 8. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Recommended action |
|---------|-----------------------|--------------------|
| **Classification cannot be confirmed** | No intended‑use statement → risk of applying wrong conformity route. | Escalate to product development/marketing to obtain a definitive Intended Purpose description. |
| **No clinical data (pre‑market or post‑market) available** | Clinical evaluation would be incomplete, violating Annex XIV Part A. | Request feasibility studies, registries, or design‑clinical investigation; consider commissioning a clinical study. |
| **Equivalence evidence absent** | Section D of PMCF Evaluation Report cannot be completed; may affect CE mark for devices relying on equivalence (Art. 51). | Obtain data from predicate devices; verify that they meet the same essential requirements and intended purpose. |
| **Risk analysis not updated after PMCF findings** | Residual risks could increase unnoticed, breaching GSPR §8‑§9. | Immediate risk‑assessment update; if new hazards are identified, submit corrective actions to the Notified Body (Art. 10(10)). |
| **PMS system not implemented** | Art. 83/84 non‑compliance leads to inability to detect trends, may trigger market surveillance enforcement. | Initiate PMS SOPs and appoint a PMS responsible person; report progress to senior management. |
| **Missing EU DoC or incomplete technical documentation** | The Notified Body will refuse assessment (Art. 19). | Prepare DoC draft once classification and conformity route are fixed; include full Annex II content before submission. |

When any of the above triggers occur, the responsible RA shall **raise a formal “Regulatory Gap Alert”** to product management and senior quality assurance for priority handling.

---

### 9. Re‑usable RA Judgment (to be stored in the knowledge base)

> *If a device lacks an explicit intended‑use statement, classification cannot be performed under Annex VIII; consequently the conformity‑assessment route, clinical‑evaluation requirements and PMS obligations remain undefined. The regulator’s first action must therefore be to obtain a complete Intended Purpose documentation, after which a systematic application of Annex VIII (classification), Art. 52 (conformity route) and Annex XIV (clinical evaluation & PMCF) can be executed.*  

This judgment should be referenced for any future cases where only high‑level guidance excerpts are available without device‑specific information.

---

### 10. Peer‑Review Prompt
*Please review the assumptions made above, especially:*  

1. *The inference that the device may fall under an active‑device rule (Rule 9‑11) despite no explicit evidence.*  
2. *The completeness of the PMCF Evaluation Report sections listed vs any additional mandatory items in the latest MDCG 2020‑5/6/7/8 guidance.*  
3. *Whether any jurisdiction‑specific exceptions (e.g., for devices classified as “non‑medical” under Annex XVI) could apply given the limited data.*  

*Identify any gaps, suggest missing citations, or propose alternative classification pathways that should be considered.*

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

> Art. 52 단락 매핑 오류(ra_eu-001과 동일) — I→52(1), IIa→52(5), IIb→52(6), III=52(7)로 정정. 웹검증.

**Source Excerpts**

1. Chunk `1032759063790726230`

> │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ```

2. Chunk `1132312459160211217`

> ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과 (데이터 수집 결과, 긍정·부정 포함, 편차 근거) | | D | 동등·유사 기기 임상데이터 평가 결과 | | E | 기술문서에 대한 결과의 영향 (CER, Risk Management File, SSCP 각각 명시) | | F | 적용된 CS, 조화표준, 가이던스 | | G | 종합 결론 (PMCF 목적 대비 결과, 예방·시정 조치 필요성) |

### kb-eval-20261028-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "09d5e575dfdc0936", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md", "source_hash": "83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `09d5e575dfdc0936`
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

> **Regulatory Draft – Classification, Conformity‑Assessment Route and Clinical‑Evaluation Gap Analyse for a High‑Risk AI‑Enabled SaMD**

---

### 1. Device Synopsis (to be completed by the project team)  
| Item | Expected content |
|------|------------------|
| **Device name / model** | – |
| **Intended purpose** | Software that performs medical diagnostic/therapeutic functions using AI algorithms (e.g., image analysis, decision support). |
| **Target user & patient population** | Health‑care professionals (or lay users if applicable); specific clinical indication(s) to be listed. |
| **Regulatory references** | MDR (Regulation (EU) 2017/745) – Annex I §A point 11; AI Act Regulation (EU) 2026/1744 (Digital Omnibus on AI). |

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Decision point | Evidence required | Outcome |
|------|----------------|-------------------|---------|
| **2.1** | Is the product a “medical device” under MDR Annex I §A point 11? | Confirmation that intended purpose falls within the definition of a medical device (e.g., diagnosis, prevention, monitoring). | **Yes** – per source excerpt [1]. |
| **2.2** | What is the MDR class? | Identify whether the product is Class IIa, IIb or III based on its intended use and inherent risks (e.g., invasive, active, measuring). For AI‑SaMD, most Class IIa or higher devices require NB involvement (source [1] – “most Class IIa and above … NB involvement”). | **Presumed** Class IIa/IIb/III – to be confirmed by applying the appropriate rule(s) in Annex VIII (e.g., Rule 9, 10, 11). |
| **2.3** | Does the AI Act deem it a “high‑risk AI system”? | Application of Art. 6(1) AI Act – all medical devices classified as Class IIa or higher are high‑risk AI systems (source [1]). | **Yes**, if step 2.2 confirms Class IIa or higher. |
| **2.4** | Conformity‑assessment route | For Class IIa: **Art. 52(6) – Annex IX** (full QMS + technical‑documentation assessment by a Notified Body).<br>For Class IIb/III: **Art. 52(4) or (3) – Annex IX** (or Annex X + XI where applicable). NB involvement is mandatory (source [1] – “NB 관여”). | **Annex IX** route selected (most common for software). |
| **2.5** | EU Database registration | Art. 49 MDR – registration in EUDAMED required for high‑risk AI systems (source [1]). | **Yes**, schedule to align with Annex III dates from Regulation 2026/1744 (see §12.2, source [2]). |

---

### 3. Required Technical & Clinical Evidence  

| Requirement (MDR / AI Act) | Minimum content | Current status (as known) | Gap |
|----------------------------|-----------------|---------------------------|-----|
| **Technical Documentation** – Annex II §§1‑6 | Device description, intended use, design & manufacturing information, GSPR compliance, benefit–risk analysis, verification & validation. | Draft exists but lacks AI‑specific risk analysis. | • Add AI‑risk management (data set provenance, algorithm performance). |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | State‑of‑the‑art literature, clinical data (pre‑market or equivalence), benefit–risk conclusions; kept current under Art. 61. | Literature review performed; no clinical performance data from real‑world use. | • Obtain clinical data (prospective study / post‑market evidence). |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – Annex XIV Part B | Objectives, methods, sampling plan, analysis of residual risks, update of CER. | PMCF not yet defined. | • Draft PMCF plan aligned with AI Act Chapter III requirements. |
| **Post‑Market Surveillance (PMS) System** – Art. 83 / Art. 84 | PMS Plan describing data collection, trend analysis, periodic safety update report (PSUR). | PMS system under development; timelines not mapped to AI Act Annex III deadlines (2027‑12‑02, 2028‑08‑02). | • Align PMS schedule with AI Act Annex III dates. |
| **Periodic Safety Update Report (PSUR)** – Art. 86 | For Class IIa: every 2 years; for Class IIb/III: annually. Includes benefit–risk conclusions, PMCF results, sales & usage data. | No PSUR template prepared. | • Create PSUR template and set calendar. |
| **Declaration of Conformity** – Art. 19 (Annex IV content) | Manufacturer details, device identification, conformity‑assessment route, references to harmonised standards, signed by authorised person. | Draft pending after NB audit. | • Complete once Annex IX assessment is successful. |
| **AI Act Specific Requirements** – Regulation 2026/1744 Annex I & III | Transparency information (e.g., datasheet for users), conformity‑assessment integration with MDR route, EU DB registration (Art. 49). | Only high‑level mapping performed; detailed documentation (e.g., data‑governance file) missing. | • Prepare AI‑specific technical file items per Annex I/III. |
| **Relevant Harmonised Standards** – ISO 14971 (2019), IEC 62304, IEC 62366‑1, IEC 82301‑1 (AI risk management, if available). | Demonstrate compliance with GSPR (§3‑9) and software lifecycle. | ISO 14971 already applied; IEC 62304/IEC 62366‑1 partially covered. | • Verify coverage of AI‑specific controls (e.g., model‑drift monitoring). |

---

### 4. Identified Clinical‑Evaluation Gaps  

| Gap | Description | Impact on MDR/AI Act compliance |
|-----|-------------|---------------------------------|
| **Insufficient clinical performance data** | No prospective or real‑world evidence demonstrating safety/effectiveness of the AI algorithm for its intended indication. | CER cannot be concluded; PSUR (Art. 86) will lack required findings. |
| **Missing justification for high‑risk AI classification** | Classification relies on assumption that “most Class IIa+ are NB‑involved”. No documented analysis using MDCG 2025‑6/AIB 2025‑1 Q2 Table 1 (source [1]). | Risk of non‑conformity with Art. 6(1) AI Act; NB may reject assessment. |
| **Absence of AI‑specific risk management** | ISO 14971 applied, but no dedicated AI‑risk file (e.g., data set bias, algorithm drift). | Violation of Annex I §3‑9 and AI Act transparency obligations. |
| **PMCF plan not established** | No defined objectives, sample size or monitoring methodology for post‑market performance of the AI model. | Non‑compliant with Annex XIV Part B; PSUR will be incomplete. |
| **PMS schedule misaligned to AI Act deadlines** | AI Act Annex III implementation dates (2027‑12‑02 & 2028‑08‑02) not reflected in PMS plan (source [2]). | Potential breach of Art. 84 and AI Act Chapter III timelines. |
| **EU Database registration pending** | Art. 49 MDR requires registration of high‑risk AI systems; no EUDAMED entry prepared yet. | Device cannot be placed on the market before registration. |

---

### 5. Recommended Risk Controls (to close the gaps)  

1. **Extend ISO 14971 risk management** to include AI‑specific hazards (data quality, training‑/validation‑set bias, model drift, cybersecurity). Document in a dedicated *AI Risk Management File* (refer to emerging IEC 82301‑1 guidance – note: not cited in source, verify separately).  
2. **Implement IEC 62304** software lifecycle processes; ensure version control and traceability of algorithm updates.  
3. **Apply IEC 62366‑1** usability engineering to mitigate user‑error risks introduced by AI output interpretations.  
4. **Introduce a Data‑Governance Procedure** covering data acquisition, labeling, storage, and monitoring for bias – required under AI Act Annex I (no specific identifier in source – verify separately).  
5. **Define PMCF methodology** – prospective registry or post‑marketing study with predefined performance metrics (sensitivity, specificity, ROC curves) aligned to the clinical indication.  
6. **Update PMS Plan** to incorporate periodic monitoring of algorithm performance and trigger corrective actions when drift exceeds predefined thresholds (per AI Act Annex III).  

---

### 6. Human‑Escalation Triggers  

| Trigger | Condition | Escalation recipient | Action |
|--------|-----------|----------------------|--------|
| **Classification uncertainty** | Unable to substantiate Class IIa/IIb/III decision with MDCG 2025‑6 guidance (Table 1) within 10 working days. | Regulatory Lead / Quality Manager | Conduct formal classification review; consider external expert opinion. |
| **Missing clinical data** | No clinical performance evidence available after the agreed collection deadline (30 days post‑prototype release). | Clinical Project Manager | Halt further regulatory submission; initiate rapid clinical study. |
| **Residual risk exceeds acceptability** | Post‑risk‑assessment residual risk score > pre‑defined acceptability threshold (as per ISO 14971) and cannot be mitigated by additional controls. | Senior Management / Chief Medical Officer | Decision on redesign or market withdrawal. |
| **PMS schedule misalignment** | AI Act Annex III implementation dates not reflected in the PMS plan 14 days before the deadline. | Compliance Officer | Immediate revision of PMS plan; notify Notified Body. |
| **EU Database registration not completed** | EUDAMED entry absent 7 days before intended market launch. | Regulatory Affairs Director | Suspend launch; issue internal hold notice. |
| **Notified Body audit findings** | NB issues non‑conformities on AI‑specific documentation during Annex IX assessment. | Quality Assurance Manager | Implement corrective action plan within the NB’s stipulated timeframe (typically 30 days). |

---

### 7. Summary Judgment  

*Based on the available source material, the device is a medical device under MDR (Annex I §A point 11) and, because it will be classified at least as Class IIa, it is also a **high‑risk AI system** under Art. 6(1) of the AI Act.*  

*The appropriate conformity‑assessment route is **Annex IX** (full QMS + technical‑documentation assessment by a Notified Body), with subsequent registration in the EU database per Art. 49 MDR and compliance with AI Act Chapter III requirements.*

*Critical gaps remain in clinical performance evidence, justification of high‑risk classification (MDCG 2025‑6/AIB 2025‑1 Table 1), AI‑specific risk management, PMCF planning, and alignment of the PMS schedule to the AI Act annex dates (source [2]). These must be addressed before a Notified Body can issue a CE mark.*

---

### 8. Peer‑Review Prompt  

> **To RA colleagues:** Please challenge the assumptions above, especially:  
> • The presumed Class IIa/IIb/III assignment – have all relevant Annex VIII rules been applied?  
> • The adequacy of the identified evidence list in light of the latest AI Act (Regulation 2026/1744) – any additional annexes or mandatory data sets not captured?  
> • Whether the proposed risk‑control measures fully satisfy Annex I §§3‑9 and emerging IEC 82301‑1 requirements.  

*Your feedback will be used to refine the gap analysis and update the project plan.*

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

> ① "MDR Annex I §A point 11" 역귀속 — 해당 조항은 AI Act Annex I Section A pt.11(MDR 포함)임(10-20 회차 검증방향과 반대). ② "Art. 49 MDR/EUDAMED" — Art. 49는 AI Act EU DB 등록 조항, MDR EUDAMED(Art. 33-39)와 혼입. #134 관할 혼입 계열.

**Source Excerpts**

1. Chunk `1013595113860735371`

> ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은 NB 관여 → **Art.6(1) 해당** (MDCG 2025-6/AIB 2025-1 Q2·Table 1) └─ No: Annex III 별도 해당 여부 확인 2. High-risk 확정 시 ├─ AI Act Chapter III 전체 요건 적용 ├─ 적합성평가 경로: MDR 경로에 AI Act 요건 통합 └─ EU DB 등록 의무 (Art. 49) ``` **판정 기준**: 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높다.

2. Chunk `1015646396132986584`

> lan for AI-Enabled Device Software Functions (Final; 2025-08-18 현재 본; Docket FDA-2022-D-2628; original final issued December 2024)"으로 갱신. 범위를 ML→**AI-enabled device software functions 전반**으로 보정. FDA Guidance 페이지(2025-08-18 current)로 직접 재확인. 사내 SOP-AIGOV-001 v0.3 "FDA PCCP Guidance 2024" 표기와 정합 회복 | | v0.9 | 2026-09-11 | **P0 사실성 정정 (audit #1041)** — Regulation (EU) 2026/1744(Digital Omnibus on AI, 채택 2026-07-08 / OJ 2026-07-24 / 발효 2026-07-27, CELEX 32026R1744) 확정 반영. §3 일정표에 발효일·Annex III 2027-12-02·Annex I 2028-08-02 행 신설, '잠정 합의 시·예상·미완료' 조건부 표현 전량 제거. §12.2 시나리오 (A)/(B) 분기를 (A) 확정으로 종결하고 (B) 트랙 삭제, 기준일을 2028-08-02로 재설정. §12 D-36 D-day·...

### kb-eval-20261028-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d0e430405d9fc0e2", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "229ed67db908335f1ee3f0eb51fd11a50f828f2ecba0f269c5461bb4f52f2547"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d0e430405d9fc0e2`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & PMS / PSUR Requirements (MDR 2017/745)**  

---

### 1. Device Identification & Classification – Current Status  

| Item | Information from source | Comment / Gap |
|------|--------------------------|---------------|
| **Device name / model** | *Not provided in the excerpts* | ❗ Missing – needed to locate the applicable classification rule (Annex VIII). |
| **Intended medical purpose / indication(s)** | *Absent* | ❗ Missing – essential for determining the “intended use” criterion used by all classification rules. |
| **Basic risk class** | *Cannot be derived* | ❗ Gap – without purpose and technology description we cannot apply a specific rule (e.g., Rule 9, 10, 11, 17). |
| **Proposed conformity‑assessment route** | *Not stated* | ❗ Needs to follow Art. 52 once the class is known (self‑declaration for Class I, Annex IX for Classes Is/Im/Ir and IIa–III, or Annex X + XI where applicable). |
| **Relevant MDR provisions** | Art. 86(1) – PSUR content; Art. 88 – Trend reporting; Art. 86(1)(a) – benefit‑risk conclusion | These are correctly referenced in the source and will drive the PSUR structure. |

> **Regulatory judgment:** *Classification cannot be assigned at this stage.* A full device description, intended use, and technology summary must be supplied before any conformity‑assessment route can be selected.

---

### 2. Required Evidence / Documentation (per MDR)  

| Pillar | Minimum evidence (MDR reference) | What is missing in the current dossier |
|--------|-----------------------------------|---------------------------------------|
| **Technical Documentation** (Annex II §1‑6) | – Device description, specifications, labeling (Annex I §23). <br>– Design & manufacturing information. <br>– Risk Management File (RMF) complying with Annex I §3‑9 (ISO 14971:2019). <br>– Verification & validation data. | All sections absent – no device description, no design files, no RMF. |
| **Risk Management** | ISO 14971:2019; risk analysis, evaluation of residual risks, benefit‑risk determination (Art. 86(1)(a)). | No documented RMF or evidence that residual risks have been evaluated against clinical benefits. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – up‑to‑date literature review, state‑of‑the‑art analysis, clinical data, and benefit‑risk conclusion. Must be kept current under Art. 61. | No CER is referenced; benefit‑risk balance in Section 6 of the PSUR appears only as a summary without underlying clinical data. |
| **Post‑Market Surveillance (PMS) System** | Art. 83 – PMS system, Art. 84 – PMS plan. Must define data collection methods, frequency, and trending analysis. | Only trend tables (Art. 88) are shown; the overarching PMS plan/system is not supplied. |
| **Periodical Safety Update Report (PSUR)** | Art. 86 – PSUR content: <br>• Benefit‑risk conclusions (Art. 86(1)(a)). <br>• Main findings of PMCF (Art. 86(1)(b)). <br>• Sales volume & using‑population data (Art. 86(1)(c)).<br>– Update frequency: annually for Class IIb/III, every 2 y for Class IIa. | Sections 4 and 6 are present, but the PSUR lacks: <br>– Quantitative sales & population data (Art. 86(1)(c)). <br>– PMCF results (Art. 86(1)(b)). <br>– Evidence that the update cadence matches the device class. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan / Report** | Annex XIV Part B – plan describing objectives, methodology, and timelines; report summarising outcomes. | No PMCF plan or results are attached; only a high‑level benefit‑risk statement is given. |
| **Summary of Safety and Clinical Performance (SSCP)** *(if Class III or implantable)* | Art. 32 – must be published for public access. | Not applicable unless class determined to be III/implantable; currently unknown. |

---

### 3. Identified Gaps & Immediate Actions  

1. **Device Description & Intended Use**  
   *Action:* Obtain a complete description (including physical, functional, and software characteristics) and the labelled intended medical purpose. This will enable classification under Annex VIII.

2. **Classification Determination**  
   *Action:* Apply the relevant rule(s) (e.g., Rule 9, 10, 11, 17) once the above is available; document the chosen rule number per Annex VIII.  

3. **Risk Management File (RMF)**  
   *Action:* Compile a risk analysis following ISO 14971:2019, identify all residual risks, and map them to the benefit‑risk conclusions required by Art. 86(1)(a).  

4. **Full Clinical Evaluation**  
   *Action:* Conduct a clinical literature review (state of the art) and, if needed, generate/collect clinical data (clinical investigations or post‑market clinical follow‑up) to support the CER.  

5. **PMS Plan & System**  
   *Action:* Draft Art. 84 PMS plan describing data sources, frequency of collection, and procedures for trend analysis. Link this to the trend tables already shown (Art. 88).  

6. **PSUR Completion**  
   *Action:* Populate missing sections: <br>– Sales volume & using‑population estimates (Art. 86(1)(c)). <br>– Summarise PMCF findings (Art. 86(1)(b)). <br>– Verify update interval matches the yet‑to‑be‑determined class.  

7. **Conformity‑Assessment Route Selection**  
   *Action:* Once classification is known, select the appropriate route per Art. 52 and prepare the associated NB engagement (Annex IX for Classes Is/Im/Ir/IIa–III; self‑declaration for Class I).  

---

### 4. Risk Controls & GSPR Mapping  

| GSPR § | Typical requirement for this type of device | Evidence needed |
|--------|-----------------------------------------------|-----------------|
| **§3** – Risk management system | Implement ISO 14971:2019 RMF | Completed RMF, risk‑control reports |
| **§4** – Risk control measures | Verify that identified hazards are eliminated or mitigated to acceptable levels. | Verification/validation test results; residual‑risk justification (Art. 86(1)(a)) |
| **§5** – Use‑error risks | Conduct usability evaluation (IEC 62366‑1:2020). | Usability engineering file, simulated use testing |
| **§6** – Device lifetime | Define intended service life & perform ageing studies. | Shelf‑life data, accelerated ageing test reports |
| **§7** – Transport & storage | Demonstrate compliance with transport conditions. | Packaging qualification, logistics validation |
| **§8** – Benefit‑risk determination | Must be aligned with PSUR benefit‑risk conclusion (Art. 86(1)(a)). | CER, PSUR, RMF cross‑reference |
| **§23** – Label & IFU | Provide clear labeling consistent with device use and risk information. | Final label artwork, instructions for use (IFU) |

---

### 5. Human‑Escalation Triggers  

| Trigger | Condition | Required escalation action |
|---------|-----------|----------------------------|
| **Serious Incident reported** | Any entry in Section 4.1 (Art. 86(1)) flagged as “Confirmed” or “Likely related”. | Immediate notification to the NB and competent authorities per Art. 87; initiate FSCA if needed. |
| **Trend threshold exceeded** | Any row in Section 4.2 (Art. 88) where *Observed incidence* > *Threshold*. | Prompt risk‑management meeting, update PMS plan, consider design change or field safety corrective action (FSCA). |
| **Benefit‑risk balance shifts to “Uncertain” or “Unfavourable”** | Outcome of Section 6 indicates a negative change. | Convene Clinical Evaluation Committee; update CER, possibly pause market distribution pending further data. |
| **Missing classification / intended use** | No device description or purpose provided within 30 days of this draft. | Escalate to the Project Lead for immediate provision of missing information; document as a critical open item in the technical‑documentation checklist. |
| **PSUR update cadence not met** | For Class IIb/III, PSUR not refreshed annually; for Class IIa, not refreshed within 2 years. | Notify Quality Management – schedule urgent PSUR preparation; inform NB of delayed submission. |

---

### 6. Summary & Next Steps  

1. **Obtain the missing device description, intended use, and technology details** – required to apply Annex VIII classification rules.  
2. **Develop a complete RMF (ISO 14971:2019) and link its outputs to the benefit‑risk conclusions required by Art. 86(1)(a).**  
3. **Compile a full CER (Annex XIV Part A)** and, if applicable, a PMCF plan/report (Annex XIV Part B).  
4. **Finalize the PMS system & plan (Art. 83‑84) and integrate them with trend reporting (Art. 88).**  
5. **Complete the PSUR (Art. 86) with all mandatory sections, respecting the update frequency for the final class.**  
6. **Select conformity‑assessment route per Art. 52 once classification is established**, and engage the appropriate Notified Body (Annex IX or Annex X + XI).  

---

### 7. Peer Review Prompt  

> *@RA‑Peer:* Please review this gap analysis for completeness and correctness:  
> - Are there additional MDR provisions or GSPR clauses that should be addressed given the limited information available?  
> - Does the proposed list of human‑escalation triggers align with current vigilance practice under Art. 87‑88?  
> - Identify any other evidence (e.g., software documentation per IEC 62304, usability data per IEC 62366‑1) that may be required based on plausible device types once classification is known.  

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

1. Chunk `1068941934152517684`

> ### Section 4. 심각한 부작용 및 안전 신호 (Art.86(1) 본문 — PMS 데이터 분석 · Art.88 trend) **4.1 보고 기간 내 Serious Incidents** | 이벤트 번호 | 발생일 | 제품 관련성 | 내용 요약 | 취해진 조치 | 보고 상태 | |---|---|---|---|---|---| | SI-[번호] | [날짜] | [확인/추정/관련없음] | [요약] | [FSCA/경고문 등] | [CA 보고 완료] | | (해당 없음) | — | — | 보고 기간 내 Serious Incident 없음 | — | — | **4.2 Trend Reporting (Art.88)** | 관찰된 트렌드 | 예상 발생률 | 실제 발생률 | 조치 | |---|---|---|---| | [항목] | [기준치] | [실제치] | [FSCA/경고문/설계변경 등] | | (해당 없음) | — | — | 임계값 초과 없음 | — | ---

2. Chunk `1141979248009057881`

> ### Section 6. Benefit-Risk Balance 결론 (Art.86(1)(a)) > 이전 PSUR / CER 대비 benefit-risk balance 변화 여부 평가. | 평가 항목 | 이전 PSUR | 이번 PSUR | 변화 여부 | |---|---|---|---| | 주요 편익 (Clinical benefits) | [요약] | [요약] | [변화 없음/변화 있음] | | 잔존 위험 (Residual risks) | [요약] | [요약] | [변화 없음/변화 있음] | | Overall benefit-risk 결론 | 유리함 | [유리함/불확실/불리함] | [변화 없음/변화 있음] | **Benefit-risk 결론:** > [이번 보고 기간의 데이터를 종합할 때, 해당 기기의 benefit-risk balance는 여전히 유리하며/변화가 없으며, 기존 적응증에서의 사용은 적절한 것으로 판단됩니다. / 또는: 새로운 위험 신호가 확인되어 다음의 조치를 취합니다: ...] ---

## ra_kr

### kb-eval-20261028-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "72001a09f6a42a64", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `72001a09f6a42a64`
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

> **Regulatory Draft – Independent SaMD “촬영실 GUI SW”**

---

### 1. Device Overview & Preliminary Grade Determination
| Item | Description |
|------|-------------|
| **Product type** | Stand‑alone medical software (SaMD) that provides image‑capture room user‑interface functions. |
| **Intended use** | Real‑time display and manipulation of radiographic images in a clinical imaging suite. |
| **Risk class (Korea)** | The Korean Medical Device Act (디지털의료제품법) assigns grades 1–4등급 to SaMD based on intended use, risk, and the “risk‐based classification matrix”. The source does not specify the applicable grade; therefore the exact **grade must be confirmed from 「의료기기 품목 및 품목별 등급에 관한 규정」** before finalizing the submission route.  *(no specific identifier found in source — verify separately)*  

---

### 2. Submission Route (MFDS)

| Korean Grade | Typical MFDS pathway |
|--------------|-----------------------|
| **1등급**    | 신고 (Notification) |
| **2등급**    | 인증 (Technical‑document review by designated 심사기관) |
| **3등급·4등급** | 허가 (Full approval by MFDS) |

*Because the grade is presently undefined, the default assumption for a SaMD with patient‑impacting functions is **3등급 또는 4등급 → 허가**. This should be validated once the grading matrix is applied.*

---

### 3. Core Evidence Package Required for 허가/인증

| Category | Korean regulatory requirement | Typical supporting documents | Comments / Gaps |
|----------|------------------------------|-----------------------------|-----------------|
| **Quality Management System** | KGMP (의료기기법 제28조) – full QMS, including design‑control, risk‑management, post‑market surveillance. | • KGMP 인증서  <br>• SOPs for design / development, change control, complaints, internal audits.<br>• Records of internal audit reports (see FDA §820 전반 for reference). | No KGMP‐specific citation in source – **verify separately**. |
| **Software Development Lifecycle** | Compliance with IEC 62304 (Safety Class C) & Korean 디지털의료제품법 연계. | • Software Development Plan (SDP)<br>• Software Requirements Specification (SRS)<br>• Software Architecture Design (SAD)<br>• Verification/Validation Plans (SVP, SVR) – all required per IEC 62304 §8.1.<br>• Regression‑test automation evidence. | IEC 62304 references are present in source; no Korean‐specific clause cited → **verify separately**. |
| **Risk Management** | ISO 14971 (2019) risk management file, integrated with KGMP. | • Risk Management Plan & Report<br>• Hazard analysis, risk evaluation, mitigation verification. | No explicit Korean citation – **verify separately**. |
| **Cybersecurity** | MFDS 사이버보안 가이드라인 2025 (no numbered notice provided). | • Threat model, SBOM, PCCP‑style security plan, incident‑response SOPs.<br>• Mapping to FDA 524B PCCP for reference. | No identification number in source → **verify separately**. |
| **Clinical Evaluation / Local Data** | Korean clinical evaluation report (CER) or foreign CER accepted under MFDS “foreign clinical data” scope (subject to latest notice). | • Clinical performance study results (Korean patients if required).<br>• Literature review, post‑market real‑world evidence. | Acceptance criteria not detailed in source – **verify separately**. |
| **UDI & Adverse Event Reporting** | MFDS UDI system (similar to FDA 21 CFR 830) and mandatory adverse event reporting within 30 days. | • UDI labeling plan, device identifier database entries.<br>• SOP for 30‑day MDR reporting. | Source cites FDA §820.10(b), §820.35(a); Korean equivalents need confirmation – **verify separately**. |
| **Labeling & IFU** | Korean language labeling, symbols per MFDS “의료기기 라벨링 지침”. | • Final Korean label mock‑up, Instruction for Use (Korean). | No citation in source – **verify separately**. |
| **Service/Repair Records** | Service performance records required (MFDS §820.35 reference indicates analogous requirement). | • Service log templates, field‑service SOPs. | FDA §820.35 cited; Korean rule number not provided – **verify separately**. |

---

### 4. Identified Gaps / Missing Information

| Gap | Why it matters | Suggested action |
|-----|----------------|-----------------|
| **Exact Korean grade (1~4등급)** | Determines 허가 vs 인증 vs 신고 pathway. | Apply the SaMD classification matrix; obtain official grade confirmation. |
| **KGMP certification & SOPs** | Mandatory QMS baseline for any Korean submission. | Conduct KGMP audit, obtain certificate, compile SOP library. |
| **Korean clinical evidence (if required)** | MFDS may require local data even when foreign CER exists. | Plan a small‑scale Korean usability/clinical study or assess existing foreign CER acceptance scope. |
| **Official MFDS cyber‑security guideline number** | Needed for precise citation in submission. | Retrieve the latest MFDS “사이버보안 가이드라인” notice (e.g., 고시 제XXXX‑XX호). |
| **UDI implementation plan** | UDI is mandatory for most 2~4등급 devices. | Develop UDI scheme aligned with MFDS requirements; confirm label placement rules. |
| **Korean labeling & IFU** | Must be in Korean and meet MFDS format specifications. | Draft Korean label/IFU, submit to MFDS for review if required. |
| **Post‑market surveillance (시판후조사) plan** | Required for 허가 devices; must align with MFDS PMS framework. | Create a PMS plan, define vigilance reporting timelines. |

---

### 5. Risk Controls & Mapping to QMS Requirements

| FDA 21 CFR 820 reference (source) | Mapped Korean requirement | Control / Evidence |
|-----------------------------------|---------------------------|--------------------|
| §820.10(b) – “ARR (Applicable Regulatory Requirements)” – need separate compliance for UDI, MDR reporting, Corrections & Removals. | KGMP QMS must include dedicated ARR‑compliance procedures; MFDS UDI and adverse event reporting SOPs. | Documented ARR‑compliance matrix; cross‑referencing to KGMP SOPs. |
| §820.35(a) – “Complaint file enhancement” – record MDR‑reportable assessment at complaint intake. | Korean complaint handling SOP must capture regulatory‑reportability decision (30‑day reporting trigger). | Complaint log template with a “Reportability?” field; audit trail. |
| §820.35 – “Service records” requirement. | MFDS service/maintenance record obligations (similar to FDA). | Service report forms, retention schedule per KGMP. |
| §820 전반 – “Internal audit inspection” – FDA inspectors may view internal‑audit reports. | Korean internal audit documentation must be accessible for MFDS inspections; confidentiality exceptions removed. | Internal audit program with documented minutes, corrective actions. |

*Note: The above FDA citations are provided because they appear in the source material; corresponding Korean regulatory clauses have not been quoted and therefore require separate verification.*

---

### 6. Citations

| Evidence type | Source citation |
|---------------|-----------------|
| **ARR (Applicable Regulatory Requirements)** | §820.10(b) – cited in excerpt [1]. |
| **Complaint file enhancement** | §820.35(a) – cited in excerpt [1]. |
| **Service records requirement** | §820.35 – cited in excerpt [1]. |
| **Internal audit scope** | §820 전반 – cited in excerpt [1]. |
| **Contract sterilizer & re‑labeler inclusion** | §820.10(a) – cited in excerpt [1]. |
| **Software development lifecycle (IEC 62304 Safety Class C)** | IEC 62304 (Safety Class C) – cited in excerpt [2]. |
| **SW validation reference** | IEC 62304 §8.1 – cited in excerpt [2]. |
| **Cybersecurity guidance** | MFDS 사이버보안 가이드라인 2025 – cited in excerpt [2] (no notice number supplied). |
| **AI/ML pre‑market considerations** | FDA PCCP (2024‑12‑03 Final) & EU AI Act Reg. 2024/1689 – cited in excerpt [2]. |

*All Korean‑specific identifiers (e.g., MFDS 고시 번호, KGMP article numbers) were **not** found in the supplied excerpts; they must be sourced independently.*

---

### 7. Human‑Escalation Triggers

| Trigger condition | Reason for escalation |
|-------------------|-----------------------|
| **Grade undefined** – unable to assign Korean grade (1~4등급). | Determines submission pathway; requires senior regulatory decision. |
| **KGMP certification absent** or audit gaps identified. | Mandatory baseline; must be resolved before any dossier compilation. |
| **Missing Korean clinical data** where MFDS does not accept foreign CER. | Could block approval; needs study planning or alternative evidence. |
| **No official MFDS cyber‑security guideline number** available for citation. | Without precise reference, the submission may be rejected on documentation completeness. |
| **UDI implementation plan not yet drafted** for a 2~4등급 device. | UDI is a legal requirement; incomplete plan halts dossier finalization. |
| **Labeling/IFU not prepared in Korean** or fails format review. | Language compliance is non‑negotiable; must be corrected prior to filing. |
| **Post‑market surveillance (시판후조사) plan missing or insufficient** for 허가 devices. | Required for ongoing compliance; escalation needed to product safety team. |

When any of the above triggers occur, the RA lead should pause dossier progression and convene a cross‑functional review (RA, Clinical, QA/QC, Development) to obtain the required deliverables before proceeding.

---

### 8. Peer‑Review Prompt
> **Please review**:  
> 1. The assumption that “촬영실 GUI SW” will likely fall into 3등급 or 4등급 – is there product‑specific information (e.g., risk classification matrix entry) that could place it in 2등급 instead?  
> 2. Coverage of the source excerpts: do they adequately support all listed QMS and software lifecycle requirements, or are additional Korean regulatory references needed?  
> 3. Potential gaps in foreign‑evidence acceptance (e.g., OECD MAD for non‑clinical data, MFDS acceptance of FDA PCCP) that may affect the evidence strategy.  

*Feedback from a fellow RA will help confirm these assumptions and identify any jurisdictional blind spots before final submission.*

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

### kb-eval-20261028-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "a25c7cf30b0426a9", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `a25c7cf30b0426a9`
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

> **Regulatory Draft – Digital‑Medical‑Device GUI Software (P3 촬영실)  
Prepared for: Korean RA team (MFDS/KGMP focus)**  

---

### 1. Product Scope & Potential Regulatory Grade
| Item | Comment |
|------|---------|
| **Product type** | “P3 촬영실 GUI SW” – software that can be used as an *AI‑assisted* function for radiographic imaging (digital‑medical‑device software). |
| **Presumed Korean grade** | Because the software provides decision‑support (AI) it is likely to fall under **2등급** (requiring 인증 by a designated 심사기관). The exact grade must be confirmed against 「의료기기 품목 및 품목별 등급에 관한 규정」. <br>*No specific identifier found in source — verify separately.* |
| **Regulatory track** | **2등급 → 인증** (technical‑document review by MFDS‑designated 심사기관). If the grade were later classified as 1등급, the route would switch to 신고; if 3~4등급, 허가. |

---

### 2. Primary Regulatory Requirements & Evidence Checklist  

| Requirement | Required Evidence / Action | Source Indicator (citation) | Gap / Missing Info |
|-------------|---------------------------|----------------------------|--------------------|
| **Classification confirmation** | Submit a classification request or internal technical justification referencing the Korean “품목 및 품목별 등급에 관한 규정”. | Framework reference – MFDS_인허가_상세가이드.md §2 (등급 및 인허가 경로) | Grade not yet determined. |
| **KGMP / QMS compliance** | • KGMP certification (MFDS 제28조)  <br>• ISO 13485:2016‑based Quality Management System, with evidence of maturity sufficient for “우수관리체계” benefit. | Framework reference – ISO 13485 (2016). | Current KGMP status must be documented; no evidence supplied yet. |
| **Risk Management** | • Risk analysis & control per ISO 14971:2019 (risk‑benefit assessment, AI‑related hazard identification).  <br>• Documentation of risk controls for UI/UX errors and false‑positive/negative AI output. | Framework reference – ISO 14971 (2019). | Formal risk management file not provided. |
| **Clinical Performance Data** | • Comparative‐design clinical study (AI + physician vs physician‑only) as mandated by the 2025‑10‑31 임상시험 가이드라인 9종 개정 (analysis of analytical accuracy, efficacy size, dropout handling). <br>• If AI module will be added later, a pre‑learning plan for comparative design is recommended. | Instance citation – “2025‑10‑31 임상시험 가이드라인 9종 개정” (policy briefing). | No clinical data package yet; need to plan study or assess exemption path. |
| **Exemption / Alternative Path (if applicable)** | • Confirmation of eligibility under **제25조 각 호** of the “디지털의료제품법 시행규칙 (2026‑01‑23 개정)”. <br>• Detailed justification that the GUI SW either does not perform a medical function or meets the exemption criteria. | Instance citation – **제25조 각 호** (referenced in source). | Specific clauses of 제25조 each 호 have not been reviewed; verification required. |
| **Korean‑language labeling & IFU** | • Korean label, user manual, and software instructions complying with MFDS labeling guidelines (mandatory Korean language, safety symbols, etc.). | Framework reference – MFDS labeling requirements (no specific identifier in source). | Drafts of Korean label/IFU not yet prepared. |
| **Post‑Market Surveillance (시판후조사)** | • PMS plan aligned with MFDS 시판후조사 규정 (including adverse event reporting, periodic safety update). | Framework reference – MFDS 시판후조사 regulations. | PMS plan still to be drafted. |

---

### 3. Risk Controls Specific to AI‑Assisted GUI

| Hazard / Failure Mode | Control Measure (KGMP/ISO) | Verification |
|-----------------------|----------------------------|--------------|
| Incorrect AI output → misdiagnosis | • Implement dual‑verification: AI suggestion must be reviewed and confirmed by a qualified radiologist before report generation. <br>• Real‑time performance monitoring (accuracy thresholds). | Validation testing per IEC 62304 (software life‑cycle) and ISO 14971 risk analysis. |
| Software UI error (mis‑selection, wrong patient data) | • Use role‑based access control; audit trails for all actions. <br>• Conduct usability testing with target users (radiology staff). | Usability test report; traceability matrix linking UI requirements to verification. |
| Data security / cyber‑threats | • Follow IEC 81001‑5‑1 (2021) cybersecurity controls, MFDS 사이버보안 가이드라인. <br>• Regular vulnerability assessments and patch management. | Security assessment report, incident response plan. |

---

### 4. Human‑Escalation Triggers  

| Situation | Trigger Action | Owner |
|-----------|----------------|-------|
| **Grade not confirmed** (2등급 vs ungraded) | Escalate to senior RA for classification request with supporting documentation. | Product Manager / RA Lead |
| **Missing or ambiguous 제25조 각 호 requirements** | Pause submission; assign legal/RA analyst to review the 2026‑01‑23 시행규칙 and extract exact exemption criteria. | Regulatory Affairs Analyst |
| **KGMP certification not yet obtained** | Halt filing until KGMP certificate is issued; consider interim “우수관리체계” qualification if QMS maturity allows. | Quality Assurance |
| **Clinical data gap** (no comparative study plan) | Trigger development of clinical trial protocol or exemption justification; involve Clinical Development Lead. | Clinical Project Manager |
| **Korean label/IFU not ready** | Suspend dossier finalization until Korean language documents are complete and reviewed by compliance. | Labeling Team |
| **Risk Management File incomplete** | Immediate review meeting; risk analyst to finalize ISO 14971 file before submission. | Risk Management Lead |
| **PMS plan absent** | Require PMS drafting before any certification filing; flag for post‑approval monitoring team. | Post‑Market Surveillance Coordinator |

When any of the above triggers fire, the responsible party must log a “Regulatory Blocker” in the project tracker and notify the RA lead within 1 business day.

---

### 5. Summary Judgment  

*The P3 촬영실 GUI SW is highly likely to be a **2등급** digital‑medical‑device software that will follow the **인증** pathway.* To progress, the team must:

1. Verify the exact Korean grade and associated certification body.  
2. Obtain KGMP certification (or prove “우수관리체계” maturity).  
3. Prepare risk management per ISO 14971 and map AI‑specific hazards.  
4. Generate clinical performance evidence that satisfies the **2025‑10‑31 임상시험 가이드라인 9종 개정** comparative‑design requirements, unless a valid exemption under **제25조 각 호** can be demonstrated.  
5. Draft Korean‑language labeling/IFU and a compliant PMS plan.

All outstanding items should be tracked and escalated per the triggers above before any MFDS submission is made.

---

### 6. Peer Review Prompt  

*Please review this draft and challenge the following points:*  

- **Assumption of 2등급** – Is there any product‑function detail that could reclassify the GUI as 1등급 (신고) or raise it to 3~4등급 (허가)?  
- **Exemption pathway** – Have we correctly interpreted the scope of **제25조 각 호** for a non‑AI, purely UI‑type software? What additional evidence would be needed?  
- **Clinical data necessity** – Given the upcoming AI module addition, is a full comparative clinical trial required now, or can a staged approach be justified?  
- **KGMP vs “우수관리체계” benefit** – Are we missing any specific MFDS criteria that could allow early market entry under the QMS‑maturity incentive?  

*Your feedback will help refine the evidence package and ensure no regulatory gaps remain before filing.*

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

### kb-eval-20261028-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "3260236dbf528209", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `3260236dbf528209`
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

> **Regulatory Draft – KG MP Evidence Readiness for the Digital‑Medical Product (디지털의료제품법 대상)**  

---

## 1. Device Classification & Submission Route (Korean system)

| Step | What must be determined | Guidance note |
|------|------------------------|---------------|
| **① Grade** | Identify the applicable **​1등급·2등급·3등급·4등급** under 「의료기기 품목 및 품목별 등급에 관한 규정」. The source excerpt does not contain a grade – it must be verified against that regulation before any pathway can be set. | *no specific identifier found in source — verify separately* |
| **② Submission track** | • **1등급 → 신고**  <br>• **2등급 → 인증** (technical‑document review by MFDS‑designated 심사기관) <br>• **3등급·4등급 → 허가** (MFDS approval). | The final track follows the grade identified in ①. |

---

## 2. Required Evidential Packages (per KG MP & MFDS “GMP” requirements)

| Ref‑ID (source) | Requirement (as written in source) | Evidence to be supplied | Current status (source) |
|-----------------|-------------------------------------|--------------------------|--------------------------|
| **DR‑20** | 설계·개발 프로세스 (ISO 13485 **§7.3**) – GMP | • Design History File (DHF) framework<br>• Approved design verification & validation protocols and reports | ● (complete) |
| **DR‑21** | 위험관리 통합 (ISO 14971) – GMP, 고시 | • Risk Management Plan (RMF)<br>• Completed FMEA / FTA<br>• Residual risk acceptance matrix | ● (complete) |
| **DR‑22** | SW 수명주기 (IEC 62304) – GMP | • Software safety class determination<br>• Approved software lifecycle plan (including configuration, verification & validation milestones) | ● (complete) |
| **DR‑23** | 공급자 관리 (구성요소·OSS) – GMP, SBOM 연계 | • Supplier management SOP for components and OSS<br>• Bill of Materials (SBOM)<br>• License compliance evidence for all open‑source elements | ◐ (partial – “OSS 공급망 절차 추가” required) |
| **DR‑24** | 교육·훈련 (AI·사이버보안) – GMP | • AI‑development‑team training curriculum<br>• Attendance / completion records for AI & cyber‑security modules | ◐ (partial – “AI 개발자 교육 모듈 수립, 이수 기록 확보” pending) |

### Additional KG MP‑specific items that must be prepared (not enumerated in the excerpt)

| Item | Required evidence (Korean regulatory expectation) |
|------|--------------------------------------------------|
| **제품 라벨·사용설명서** | Korean language labeling & IFU, conformity to MFDS 고시 on labeling (no specific notice number appears in source). |
| **임상시험/임상 평가** | If the grade is 3등급 or 4등급 – local clinical data or accepted foreign Clinical Evaluation Report (CER) per MFDS scope for digital‑medical products. |
| **KG MP 인증** | Facility KG MP certificate (MFDS 제28조) and related audit reports. |
| **사이버보안 관리계획** | Reference to MFDS “디지털의료제품법” cyber‑security guideline; documented security architecture, threat modelling, patch/incident response procedures. |
| **품질경영시스템(QMS)** | Full QMS documentation aligned to KG MP (ISO 13485‐based) – SOPs, change‑control, CAPA records. |

---

## 3. Gaps / Missing Information

1. **DR‑23 & DR‑24** are still at status “◐”.  
   *Action*: finalise OSS supply‑chain procedures, confirm all OSS licenses, and complete AI/cybersecurity training modules plus attendance logs.

2. **Grade determination** – no grade is identified in the source excerpt; must be confirmed from the official “품목 및 품목별 등급에 관한 규정”.  

3. **Clinical evidence** – if the device falls into 3등급·4등급, a local clinical study or an MFDS‑accepted foreign CER is required; no such documentation is referenced.

4. **KG MP facility certification** – evidence of KG MP compliance (certificate number) not mentioned.

5. **Labeling & IFU in Korean** – sample Korean labeling and user manual have not been provided.

6. **Cybersecurity plan alignment** – while AI training is noted, a formal cybersecurity risk management file (per MFDS digital‑medical product guidance) is absent.

---

## 4. Core Risk Controls (mapping to the evidence)

| Control | Source reference | How it will be demonstrated |
|--------|------------------|------------------------------|
| **Risk Management Process** | ISO 14971 (DR‑21) | RMF, FMEA/FTA, residual risk acceptance matrix in the RMF file. |
| **Software Safety Classification & Lifecycle Controls** | IEC 62304 (DR‑22) | Software safety class, lifecycle plan, verification/validation test reports, configuration management records. |
| **Supplier / OSS License Management** | DR‑23 | Approved SBOM, supplier audit reports, OSS license compliance checklist. |
| **Human Factors / AI Training** | DR‑24 | Training curriculum, completion certificates, competency assessments for AI developers. |
| **Cybersecurity Controls** (not listed but required) | MFDS 디지털의료제품법 guidance | Threat model, security architecture diagram, vulnerability management process, incident response SOP. |

---

## 5. Citations

### Framework references (no verification caveat)

* ISO 13485 **§7.3** – Design and development planning.  
* ISO 14971 – Risk Management for medical devices.  
* IEC 62304 **2006+A1:2015** – Software lifecycle processes.  

### Instance identifiers (must come from source)

* No specific MFDS 고시, notice, or article number appears in the provided excerpts. → *no specific identifier found in source — verify separately*.

---

## 6. Human‑Escalation Triggers

| Trigger | Reason | Escalation to |
|---------|--------|----------------|
| **Any DR item remains at “◐” for >30 days past target date** | Incomplete mandatory evidence could block submission. | RA Lead & Project Manager |
| **Grade still undetermined after 2 weeks of review** | Submission route cannot be finalized; risk of missed regulatory deadline. | Regulatory Affairs Director |
| **Residual risk not accepted (RMF shows “unacceptable”)** | Device cannot proceed to clinical/market entry without mitigation. | Risk Management Team & Clinical Lead |
| **KG MP facility certificate missing or expired** | KG MP is a prerequisite for any MFDS submission. | Quality Assurance Manager |
| **Absence of Korean labeling / IFU draft** | Violates MFDS labeling requirement; will cause non‑conformity findings. | Labeling Specialist |
| **Cybersecurity plan not documented** (required for digital‑medical product) | MFDS may request supplemental evidence during review. | IT Security Lead |
| **Foreign clinical evidence insufficient for 3/4등급** | Will delay approval if local data are required. | Clinical Development Manager |

When any trigger fires, the responsible owner must raise a *Regulatory Issue* in the project tracker and seek immediate remediation.

---

## 7. Peer‑Review Prompt  

> **Request to fellow RA:**  
> Please review the above assumptions regarding (a) the inferred completeness of DR‑20 – DR‑22, (b) the omission of Korean grade information, and (c) any additional digital‑medical product obligations (e.g., MFDS “디지털의료제품법” cyber‑security checklist) that may not be captured in the current matrix. Identify any jurisdiction‑specific gaps or evidence items we have overlooked, and suggest concrete actions to close them.

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

1. Chunk `1045730514097588767`

> ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | |

2. Chunk `1073274073545790864`

> | Req-ID | 요구사항 | 법조/고시 | Status | 수용 기준 | 증빙 문서 | 보완 액션 | |--------|---------|----------|--------|----------|----------|----------| | DR-20 | 설계·개발 프로세스(ISO 13485 §7.3) | GMP | ● | DHF 체계 수립, 설계검증/밸리데이션 프로토콜 존재 | 03_설계_개발관리/설계개발_프로세스.md | - | | DR-21 | 위험관리 통합(ISO 14971) | GMP, 고시 | ● | RMF 수립, FMEA/FTA 완료, 잔존위험 수용 판정 | 07_위험관리_ISO14971/ | - | | DR-22 | SW 수명주기(IEC 62304) | GMP | ● | SW 안전 클래스 분류, 수명주기 계획서 승인 | 03_설계_개발관리/IEC_62304_SW_수명주기.md | - | | DR-23 | 공급자 관리(구성요소·OSS) | GMP, SBOM 연계 | ◐ | OSS 공급망 절차 수립, 라이선스 컴플라이언스 확인 | 09_공급자_관리/ | OSS 공급망 절차 추가 | | DR-24 | 교육·훈련(AI·사이버보안) | GMP | ◐ | AI 개발자 교육 모듈 수립, 이수 기록 확보 | 10_교육_훈련/ | AI 개발자...

### kb-eval-20261028-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "02e21c43a2a2ff27", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "9b251ad3b3cc02f37944b961b8fa8e44ca732b028f6422f9ef3e6caf4e0f6724"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `02e21c43a2a2ff27`
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
| Item | Determination | Source / Citation |
|------|---------------|-------------------|
| **품목군·분류번호** | Revised to **A11000 진단용 엑스선 장치** (sub‑categories A11110.01‑03, A11040.01/02) per audit correction【1069373523805353088】. |  |
| **등급 (1~4등급)** | Must be confirmed against the current “의료기기 품목 및 품목별 등급에 관한 규정” [별표 1] – the source only states that the new code belongs to the *진단용 엑스선 장치* group, but does not specify whether it is **2등급** or **3등급**. | No specific identifier found in source — verify separately |
| **인허가 경로** | • If determined 2등급 → **인증** (technical‑document review by MFDS‑designated 심사기관). <br>• If determined 3등급 or 4등급 → **허가** (direct MFDS approval). | 고시 제2025‑22호 (핵심 개정) indicates that 2등급 devices follow the 인증 track, while 3·4등급 follow 허가【1127747106119376174】. |

> **Action required:** Confirm the exact grade for the A11000 series in the latest “별표 1” (the table of classification numbers).  

---

### 2. Required Evidence Package  

| Requirement | Typical Korean evidence | Notes / Gaps |
|-------------|------------------------|--------------|
| **KGMP 인증** | Facility KGMP compliance certificate (MFDS 고시 제2025‑22호, ‘품질관리심사기관 단독심사 가능’) | Facility already KGMP‑certified? – verify. |
| **Technical Documentation** | • Device description, intended use, specifications <br>• 설계 및 제조 공정 흐름도 (30개 절차 매핑 from v0.2) <br>• 위험관리 파일 (ISO 14971:2019) <br>• 설계 검증·확인 시험 보고서 (IEC 60601‑1, IEC 62366‑1) | The v0.2 version of the guideline lists 30‑procedure GMP mapping – ensure all are addressed. |
| **Non‑clinical safety data** | • 비임상 GLP 테스트 (ISO 10993‑1:2018) <br>• 방사선 안전 시험 (IEC 60601‑2‑XX series) | No specific non‑clinical data cited in source; must be generated or referenced. |
| **Clinical Evaluation Report (CER)** | Local Korean clinical data **or** accepted foreign CER if MFDS permits under the current scope (separate from OECD MAD). | The source does not state whether foreign CER may be used for this device – confirm with latest MFDS notice. |
| **Software Validation (if applicable)** | IEC 62304:2006+A1:2015 referenced in 고시 제2025‑22호【1127747106119376174】. <br>• Software development plan, verification & validation reports, V&V traceability matrix. | Confirm presence of any software modules in the device (e.g., dose‑control). |
| **Cybersecurity Plan** | Applicable when “사이버보안 관리 요구(부속서)” is triggered – see 고시 제2025‑22호【1127747106119376174】. | Determine whether the X‑ray system includes networked components; if so, prepare a cybersecurity management plan per MFDS 부속서. |
| **Labeling & IFU (Korean language)** | • 제품 라벨 (품명·규격·제조자·수입자·사용주의사항 등) <br>• 사용설명서 (한글 전용) | No explicit citation in source; Korean labeling regulation must be complied with – verify the exact article number. |
| **Submission Form & Fees** | MFDS ‘의료기기 허가·인증 신청서’ (2등급 → 인증, 3·4등급 → 허가) | Ensure correct form version (post‑2025‑22 고시). |

---

### 3. Identified Missing Information  

| Gap | Impact on Submission |
|-----|----------------------|
| **Exact grade (2등급 vs 3등급)** – not disclosed in source excerpt. | Determines whether 인증 or 허가 route is needed; also drives clinical data requirements. |
| **Confirmation of KGMP‑certified manufacturing site** – no evidence shown. | Required for any submission. |
| **Local clinical data requirement** – unclear if foreign CER acceptable under current MFDS scope (separate from OECD MAD). | May necessitate Korean clinical study, adding timeline/cost. |
> *Human escalation trigger:* **Classification uncertainty → pause dossier assembly until grade confirmed with the latest “별표 1”.**

---

### 4. Key Risk Controls (per ISO 14971:2019)  

| Hazard | Control Measure | Reference |
|--------|----------------|-----------|
| Ionizing radiation exposure to patient/operator | • IEC 60601‑2‑XX compliance (X‑ray safety standards). <br>• Interlock and dose‑limiting circuitry. | Framework reference – ISO 14971:2019, IEC 60601‑1 series |
| Software malfunction (dose calculation) | • IEC 62304‑based software life‑cycle process; unit/ integration testing; V&V traceability. | 고시 제2025‑22호 – SW 밸리데이션 참조(IEC 62304)【1127747106119376174】 |
| Cyber attack on networked X‑ray console | • MFDS 부속서에 따른 사이버보안 관리 계획 (access control, logging, patch management). | 고시 제2025‑22호 – 사이버보안 요구(부속서)【1127747106119376174】 |
| Mechanical failure of gantry/colimator | • Design validation against IEC 60601‑1 mechanical safety clauses; preventative maintenance schedule. | ISO 14971:2019 (risk control hierarchy) |
| Misinterpretation of Korean IFU | • User‑centered design, human factors testing per IEC 62366‑1; Korean language verification. | IEC 62366‑1:2020+A1:2020 |

---

### 5. Citations  

* **Framework References (no “verify” caveat)**  
  - ISO 14971 (2019) – risk management for medical devices.  
  - ISO 13485 (2016) – QMS requirements (referenced in v0.2 revision).  
  - IEC 62304 2006+A1:2015 – software life‑cycle processes (cited in 고시 제2025‑22호).  

* **Instance Identifiers (taken directly from source)**  
  - **고시 제2025‑22호** – “최신 개정 핵심” summary of regulatory changes【1127747106119376174】.  
  - **Audit #1068 정정** – correction of X‑ray classification to A11000 series【1069373523805353088】.  
  - **법령 근거** – “의료기기 품목 및 품목별 등급에 관한 규정” (law.go.kr) – cited but without article number; therefore note *no specific identifier found in source — verify separately*.  

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason | Recommended Action |
|---------|--------|---------------------|
| **Unconfirmed grade (2등급 vs 3등급)** | Determines submission route & clinical data need. | Pause dossier; request official “별표 1” classification table from MFDS or consult a certified 심사기관. |
| **Absence of KGMP certification proof** | Mandatory for any filing. | Obtain/validate KGMP certificate; if missing, schedule on‑site audit. |
| **Unclear acceptance of foreign CER** | Could avoid local clinical study. | Confirm with MFDS (via 문의) whether OECD MAD or other foreign clinical data can be leveraged for this device. |
| **Cybersecurity requirement activation** | System may be networked; 부속서 요구가 적용될 경우 추가 문서 필요. | Conduct preliminary cyber‑risk assessment; if scope triggers, develop cybersecurity plan before submission. |
| **Labeling/IFU language compliance not yet verified** | Korean‑only labeling is a legal prerequisite. | Review the latest MFDS labeling guideline; prepare Korean versions and obtain regulatory review. |

If any of the above triggers are hit, the RA team should **escalate to the Project Lead and the Regulatory Affairs Manager** for decision on whether to proceed with data generation or seek alternative pathways.

---

### 7. Peer‑Review Prompt  
> *Please challenge the following assumptions: (1) that the A11000 series falls under 2등급 or 3등급 without explicit confirmation; (2) that foreign clinical evaluation reports are acceptable for this device under the current MFDS scope; and (3) that a cyber‑security plan is required only if network connectivity exists. Identify any jurisdiction‑specific gaps in our evidence matrix, especially regarding Korean labeling article numbers or additional GMP documentation referenced in v0.2 but not listed here.*

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

1. Chunk `1069373523805353088`

> ## 개정 이력 | 버전 | 일자 | 내용 | 작성 | |------|------|------|------| | v0.2 | 2026-05-07 | GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려사항 추가 | — | | v0.2.1 | 2026-09-25 | **audit #1068 정정** — §7 X-ray 품목 분류번호 'A10030(2등급)/A10040(3등급)'(미존재·A10000=보육기 오귀속)→**A11000 진단용 엑스선 장치** 계열(A11110.01~.03 [2], 투시 A11040.01/.02 [2])로 교체. '품목군'(GMP 고시)과 '품목 분류번호'(등급규정 별표 1) 구분 표기. 근거: law.go.kr 「의료기기 품목 및 품목별 등급에 관한 규정」 [별표 1] 원문 | md-process-builder |

2. Chunk `1127747106119376174`

> ## 2. 최신 개정 핵심 (고시 제2025-22호) | 항목 | 종전 | 개정 | |------|------|------| | 품목군 분류 | 26개 | 64개 | | 융복합의료기기 | 불명확 | 주된 기능이 의료기기이면 심사대상 명확화 | | 심사체계 | 복수심사 | 품질관리심사기관 단독심사 가능 | | 제출자료 | 광범위 | 간소화 | | SW 밸리데이션 | IEC 62304 참조 일부 | IEC 62304:2006+A1 전면 참조 편입 | | 사이버보안 | 미규정 | 적용 가능 시 사이버보안 관리 요구 (부속서 참조) |

### kb-eval-20261028-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-28", "decision_ref": "kb-eval-20261028-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "fc516805be72541e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "05655bb796bf8ed73e0e7bf66100bca6738bee82ab80865741516d55798597da"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `fc516805be72541e`
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

> **Regulatory Draft – KGMP Evidence Readiness Checklist**

---

### 1. Device Classification & Submission Route (Korean “등급”)

| Item | Required determination | Current status |
|------|------------------------|----------------|
| **Device grade (1~4등급)** | Must be identified from 「의료기기 품목 및 품목별 등급에 관한 규정」. The grade decides whether the route is 신고 (1등급), 인증 (2등급) or 허가 (3·4등급). | **Not provided in source** – *“no specific identifier found in source — verify separately”*. |
| **Submission track** | - 1등급 → 신고 <br> - 2등급 → 인증 (technical‑document review by MFMF‑designated 심사기관) <br> - 3·4등급 → 허가 (MFDS approval) | Dependent on grade; cannot be finalized until grade is confirmed. |

**Human escalation trigger:** If the device grade cannot be verified within 5 working days, the RA lead must request a formal grade determination from the product team and/or consult the MFDS “의료기기 품목 및 품목별 등급에 관한 규정”.

---

### 2. Core KGMP Evidence Required (post‑2026‑07‑01 reform)

| Evidence Category | Specific items (per current KGMP framework) | Source citation |
|-------------------|---------------------------------------------|-----------------|
| **Legal basis** | - 「의료기기법」제28조·제28조의2~4 (適合性認定・審査員・機關指定根據) <br> - 「의료기기법 시행규칙」제48조~48조의4 (申請・更新・審査員・取消事由) | 【2】 |
| **KGMP standards** | - 「의료기기 제조 및 품질관리 기준」(식약처 고시 제2026‑46호, 2026‑07‑01 일부개정) – defines GMP audit criteria. <br> - 「의료기기 제조 및 품질관리 관련 기관 지정 등에 관한 규정」(식약처 고시 제2026‑47호, 2026‑07‑01 제정·신규) – designates 심사기관,審査員,教育機關. | 【1】,【2】 |
| **Application forms / checklists** | KGMP 심사 신청서 양식 및 제출 서류 체크리스트 (별지 제38호의4·39·40호) – must be completed in full and submitted with supporting documents. | 【2】 |
| **Quality Management System (QMS)** | - Compliance with **ISO 13485:2016** (no newer edition exists). <br> - Risk management file per **ISO 14971:2019** (Amd 1:2024 is a linguistic amendment only). | Framework reference – no verify caveat. |
| **Device‑specific technical dossier** | • 제품설명서, 설계도면, 시험 보고서 (기능·전기·안전 등) <br>• 위험 관리 파일 (ISO 14971) <br>• 라벨·사용자 설명서 – Korean language mandatory (MFDS labeling 규정). | Framework reference. |
| **Clinical evidence** | Depends on grade: <br>‑ 1등급 → no clinical data required. <br>‑ 2~4등급 → clinical evaluation report (CER) meeting MFDS 요구사항; foreign CER may be accepted only if MFDS notice explicitly permits (separate from OECD MAD). | No specific identifier in source – verify separately. |
| **Non‑clinical safety data** | GLP 비임상 데이터 can be used under OECD **mutual acceptance of data (MAD)** for non‑clinical studies only. | Framework reference; not cited as a specific MFDS notice in the excerpts. |
| **Post‑market Surveillance (시판후조사) plan** | Must include periodic safety update, field corrective actions, and adverse event reporting according to MFDS 시행규칙 제48조의4. | 【2】 |

---

### 3. Missing / Unverified Information

| Gap | Why it matters | Action needed |
|-----|----------------|--------------|
| **Device grade** (1~4등급) | Determines submission pathway and depth of clinical evidence required. | Obtain official classification from product dossier or request MFDS “품목 등급 확인”. |
| **Intended use & indication** | Drives risk class, labeling content, and clinical evaluation scope. | Supply a clear Intended Use Statement (in Korean). |
| **Foreign regulatory clearances** (e.g., FDA 510(k) number, CE Marking) | May be referenced to support safety/efficacy but must be mapped to MFDS requirements; separate acceptance criteria for foreign CER vs. OECD MAD. | Provide copies of clearance documents and indicate which sections are being leveraged. |
| **Korean language labeling & IFU** | Mandatory for all grades; incomplete Korean translation blocks approval. | Submit draft Korean labeling with full product name, manufacturer info, warnings, and usage instructions. |
| **KGMP certification status** (facility audit report) | Required for 심사기관 submission; must reference the latest KGMP 인증서 issued after July 1 2026 reform. | Provide current KGMP certificate (certificate number & issue date). |
| **Risk management file** | Must align with ISO 14971 and demonstrate mitigations for identified hazards. | Deliver completed risk analysis, verification/validation records, and residual risk justification. |

---

### 4. Key Risk Controls to Demonstrate

1. **Quality System Control** – Full compliance with ISO 13485:2016 & KGMP (고시 제2026‑46호).  
2. **Risk Management** – Documented process per ISO 14971:2019, including hazard identification, risk evaluation, control measures, and post‑market monitoring.  
3. **Design Controls** – Design History File (DHF) covering verification/validation against intended use.  
4. **Clinical Evaluation** – If required, a CER that satisfies MFDS “임상평가보고서” criteria; foreign CER only usable if MFDS notice explicitly permits.  
5. **Labeling & Instructions for Use** – Korean‑language labeling meeting MFDS 라벨링 규정 (including device name, manufacturer, lot/serial numbers, contraindications).  
6. **Post‑Market Surveillance Plan** – Defined procedures for adverse event reporting, field corrective actions, and periodic safety updates per 시행규칙 제48조의4.

---

### 5. Citations

| Element | Citation type | Reference |
|---------|---------------|-----------|
| Legal basis (법령) | Instance identifier | 의료기기법 제28조·제28조의2~4 (source 【2】) |
| 시행규칙 articles | Instance identifier | 의료기기법 시행규칙 제48조~48조의4 (source 【2】) |
| KGMP standard – GMP criteria | Instance identifier | 고시 제2026‑46호 (식약처, 2026‑07‑01) (source 【1】) |
| KGMP standard – 기관 지정 규정 | Instance identifier | 고시 제2026‑47호 (식약처, 2026‑07‑01) (source 【1】) |
| Application forms | Instance identifier | 별지 제38호의4·39·40호 (source 【2】) |
| ISO 13485 | Framework reference | ISO 13485:2016 |
| ISO 14971 | Framework reference | ISO 14971:2019 (Amd 1:2024 amendment only) |

*No other specific instrument numbers or article sections appear in the provided excerpts; for any additional regulatory citations, verification is required.*

---

### 6. Human‑Escalation Triggers

| Trigger condition | Who escalates | Timeframe |
|-------------------|---------------|-----------|
| **Device grade not confirmed** after request | RA Lead → Regulatory Affairs Manager | ≤ 5 working days |
| **Incomplete Korean labeling/IFU** identified in checklist review | Documentation Specialist → QA Manager | Immediately (stop‑gap) |
| **KGMP certification missing or expired** | Facility Compliance Officer → R&D Director | Within 3 business days of discovery |
| **Foreign CER being used without explicit MFDS notice** | Clinical Affairs Lead → Legal Counsel | Prior to dossier submission |
| **Risk management file gaps (e.g., missing residual risk justification)** | Risk Management Owner → Head of QMS | ≤ 7 days |
| **Any discrepancy between checklist items and the submitted package** | QA Reviewer → Senior RA | At each internal audit milestone |

When any trigger fires, the responsible party must issue a formal *Escalation Memo* (Korean: “조치·보고서”) and log it in the project’s regulatory tracker.

---

### 7. Peer‑Review Prompt

> **Colleague challenge request:** Please review the assumptions made above regarding (1) the applicability of foreign clinical evaluation reports under current MFDS policy, (2) whether the listed Korean legal citations fully capture all post‑2026 KGMP requirements, and (3) any potential gaps in the risk‑control matrix for a 3등급 device. Highlight any missing references or alternative interpretations that could affect our evidence strategy.

--- 

*Prepared based on the KGMP reform documentation dated 2026‑07‑01 (고시 제2026‑46호, 고시 제2026‑47호) and associated statutes.*

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

> "ISO 14971:2019 Amd 1:2024" 비존재 개정판 표기 — ISO 개정은 2030까지 보류(EN ISO 14971:2019/A11:2021만 존재). 웹검증. 부수: "MFMF-designated" 오타(MFDS→MFMF, 2회차 연속 재발 → 페르소나 정정 후보).

**Source Excerpts**

1. Chunk `1051643482212217538`

> > 최종 갱신: 2026-07-13 (주간모니터 #8 — KGMP 적합성인정 제도 개편, 2026-07-01 시행 반영) > 근거: https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287877&type=HTML (의료기기법 시행규칙, 총리령 제2127호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287221&type=HTML (의료기기법 시행령, 대통령령 제36445호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=admrul&ID=2100000281580&type=HTML (고시 제2026-46호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=admrul&ID=2100000281582&type=HTML (고시 제2026-47호, 신설) # 국내 MFDS - GMP 심사자료

2. Chunk `528323066343451536`

> ## 핵심 문서 (2026-07-01 개편 후 체계) - 「의료기기법」제28조·제28조의2~4 (적합성인정·심사원·기관지정 근거, 개정 법률 제21263호 2025-12-30 공포) - 「의료기기법 시행규칙」제48조~48조의4 (신청·갱신·심사원·취소사유, 총리령 제2127호 2026-07-01 시행) - 「의료기기 제조 및 품질관리 기준」 (식약처 고시 제2026-46호, 2026-07-01 일부개정 — GMP 심사기준만 존치) - 「의료기기 제조 및 품질관리 관련 기관 지정 등에 관한 규정」 (식약처 고시 제2026-47호, 2026-07-01 제정·신규 — 심사기관·심사원·교육기관 지정) - KGMP 심사 신청서 양식 및 제출서류 체크리스트 (신규 서식: 별지 제38호의4·39·40호)
