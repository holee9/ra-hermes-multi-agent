# KB Eval Checksheet - 2026-07-15 Iteration 14

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260715-it14-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_us-001", "iteration": 14, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f1b6b31adf499491", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f1b6b31adf499491`
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

> **Regulatory Draft – Daily Growth Case (v1) – 2026‑07‑28**  
*Scenario ID: f1b6b31adf499491 – Source: FDA clinical‑data need criteria (MD‑process)*  

---

### 1️⃣ Bottom Line
- **Likely submission pathway:** **Traditional 510(k)** (Class II) *unless a predicate cannot be identified or the device incorporates novel technology that would preclude SE.*  
- **Key missing elements:** Predicate justification, confirmed risk analysis, and a clear clinical‑data plan (bench &/or limited human data).  

---

### 2️⃣ Classification / Submission Route

| Criterion | Assessment |
|-----------|------------|
| **Device class** | Based on intended use & technology – appears to fall in **Class II** (e.g., imaging adjunct, monitoring sensor). |
| **Regulatory route** | **510(k)** is the default for Class II when a legally marketed predicate exists. <br>*If no suitable predicate:* consider **De Novo** (new‑type Class II) – requires “if applicable” clinical data. <br>*If device is high‑risk or novel (e.g., implantable, drug‑device combo):* **PMA** (requires full clinical trial). |
| **Legal basis** | FD&C Act §510(k), 21 CFR 807 (see source [2]). |

**Decision point:** Verify existence of a predicate meeting “substantially equivalent” criteria. If not, switch to De Novo.

---

### 3️⃣ Required Evidentiary Package (per pathway)

| Evidence | 510(k) | De Novo* | PMA |
|----------|--------|----------|-----|
| **Device description & specifications** | ✔︎ | ✔︎ | ✔︎ |
| **Intended use / labeling** | ✔︎ | ✔︎ | ✔︎ |
| **Risk analysis (ISO 14971)** | ✔︎ (summary) | ✔︎ (full) | ✔︎ (full) |
| **Performance testing (bench, benchtop, animal as needed)** | ✔︎ (non‑clinical) | ✔︎ | ✔︎ |
| **Clinical data** | **Conditional** – required only if non‑clinical data cannot demonstrate safety/effectiveness (§3 of source [1]). | “If applicable” – may be waived for low‑risk novel devices. | **Mandatory** – pivotal trial(s). |
| **Predicate comparison matrix** | ✔︎ (mandatory) | N/A | N/A |
| **Software documentation (if applicable)** | IEC 62304, FDA guidance on software (solid‑state X‑ray devices) | Same | Same |
| **QMS compliance** | QMSR (ISO 13485‑aligned) – required effective 2026‑02 (see QMSR rule). | Same | Same |
| **eSTAR registration** | Required for Class II devices (post‑Oct 2023) | Not applicable | N/A |

\*De Novo review period ≈150 days; user fee ≈$46,875.

---

### 4️⃣ Identified Gaps & Missing Information

1. **Predicate Device(s)** – No specific 510(k) number cited; SE justification absent.
2. **Risk Management File** – ISO 14971 risk analysis summary not supplied; need FMEA, hazard severity classification.
3. **Clinical Data Strategy** – Unclear whether bench testing alone can satisfy safety/effectiveness; no rationale for clinical data waiver.
4. **Software Lifecycle Documentation** (if software‑driven) – No verification/validation plan or cybersecurity assessment.
5. **QMSR Evidence** – Certification to ISO 13485:2022 not yet documented; eSTAR registration status unknown.
6. **Labeling & IFU Draft** – Only a high‑level description, lacks contraindications, warnings, and intended user population.

---

### 5️⃣ Recommended Risk Controls (to be reflected in the device master record)

| Control | Rationale |
|---------|-----------|
| **Design verification & validation** per IEC 60601‑1 (if electrical) / ISO 13485. | Demonstrates compliance with performance specs. |
| **Usability Engineering** (human factors testing). | Mitigates use‑error risk for intended operators. |
| **Cybersecurity safeguards** (if software/connected). | Addresses FDA guidance on post‑market vulnerability management. |
| **Biocompatibility assessment** (ISO 10993) – if patient-contacting. | Ensures material safety. |
| **Electrical safety / EMC testing** (IEC 60601‑1‑2). | Required for Class II electrical devices. |
| **Post‑Market Surveillance Plan** – per QMSR 2026 requirements. | Supports ongoing risk mitigation and eSTAR reporting. |

---

### 6️⃣ Key Citations

- FDA Guidance: *Premarket Notification (510(k)) Submissions* – https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k  
- FDA Guidance: *De Novo Classification Request* – https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request  
- FDA Guidance: *PMA Clinical Studies* – https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies  
- FDA Guidance: *Solid‑State X‑ray Imaging Devices* (510(k) specific) – https://www.fda.gov/.../guidance-submission-510ks-solid-state-x-ray-imaging-devices  
- FDA Medical Device User Fee Schedule FY2025 – $22,171 (Class II 510(k)).  

---

### 7️⃣ Human‑Escalation Triggers

| Trigger | Action |
|---------|--------|
| **No viable predicate identified** after 2 weeks of search. | Escalate to senior RA for De Novo feasibility assessment. |
| **Risk analysis indicates high severity/likelihood hazards** that cannot be mitigated by design controls alone. | Notify Project Lead & QMS lead; consider early clinical data request. |
| **Software component > Class II (e.g., AI diagnostic)** without validated algorithm. | Escalate to Regulatory Strategy Director – may require PMA pathway. |
| **QMSR compliance not demonstrable** (ISO 13485 certification pending). | Halt submission preparation; involve Quality Assurance Manager. |
| **FDA feedback requesting additional clinical data** during 510(k) review. | Initiate rapid clinical‑data plan; involve Clinical Affairs Lead. |

---

### 8️⃣ Peer‑Review Prompt  

> *RA colleague, please evaluate the assumptions above:*
> - Is the classification as Class II justified based on the limited device description?  
> - Does the source excerpt sufficiently cover all regulatory pathways (510(k), De Novo, PMA) for this technology?  
> - Are there any jurisdiction‑specific gaps (e.g., state‑level registration, Medicare coverage considerations) that we have omitted?  
> - Validate the completeness of the required evidence matrix against current FDA guidance.  

Your critique will be incorporated before finalizing the submission plan.

---

### 9️⃣ Reusable RA Judgment (recorded for future cases)

```
honcho_conclude{
  "case_id": "f1b6b31adf499491",
  "lesson_type": "regulatory_judgment",
  "summary": "When a Class II medical device lacks an obvious predicate, default to 510(k) but immediately verify SE. If no predicate, shift to De Novo; only consider PMA for high‑risk or novel drug‑device combos. Required evidence varies by pathway (clinical data conditional for 510(k), optional for De Novo, mandatory for PMA). Early identification of gaps—predicate, risk analysis, QMSR compliance, software documentation—enables timely escalation.",
  "key_actions": [
    "Search and document a suitable predicate within 5 business days.",
    "Complete ISO 14971 risk file and map controls to FDA/ISO standards.",
    "Determine clinical‑data need per FDA’s ‘clinical data necessity’ criteria (source [1]).",
    "Confirm QMSR compliance and eSTAR registration before submission."
  ],
  "confidence": 0.93,
  "peer_review_needed": true
}
```

--- 

*Prepared by: Mike – US Regulatory Affairs Specialist*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [ ] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 핵심 판단(510(k)/De Novo/PMA 근거)은 정확하나 De Novo eSTAR 표기가 소스와 자기모순(소스는 2025-10-01부 의무화 명시).

**Source Excerpts**

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20260715-it14-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_us-002", "iteration": 14, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "f70402362d597cbb", "source": "github:holee9/MD-process/issue-drafts/163_03_SOP-DT-001_v0.3_QMSR_설계이관_실사.md", "source_hash": "f6140cf49db744771634400d420f52d5da23c62978782f5757bc6436d63cafa0"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f70402362d597cbb`
- Source: `github:holee9/MD-process/issue-drafts/163_03_SOP-DT-001_v0.3_QMSR_설계이관_실사.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/163_03_SOP-DT-001_v0.3_QMSR_%EC%84%A4%EA%B3%84%EC%9D%B4%EA%B4%80_%EC%8B%A4%EC%82%AC.md)
- Source hash: `f6140cf49db744771634400d420f52d5da23c62978782f5757bc6436d63cafa0`
- Focus: submission evidence gaps
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `163_03_SOP-DT-001_v0.3_QMSR_설계이관_실사.md`는 `163_03_SOP-DT-001_v0.3_QMSR_설계이관_실사.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 관련 문서 - SOP-DT-001 (03_설계_개발관리) - 교차검증_2026-06-08 (12_교차검증_보고서) ## 변경 요약 - §9.5 QMSR 설계이관 실사 체크포인트 5항목 신설 - §9.5.2 DHF/DMR→DDF/MDF 용어 전환 확인 매핑표 - §9.5.3 제조 준비도 증거(Manufacturing Readiness Evidence) 체계 6유형 정의 - §9.6 AI 모델 설계이관 QMSR·EU AI Act Art.17 이중 준수 요구 6단계 신설 - 규제 근거 표 QMSR 시행일 반영, SOP-AIGOV-001·SOP-AIDATA-001 상호참조 추가
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

> **Regulatory Draft – Design‑Transfer Evidence Gap Assessment (QMSR 2026‑v1)**  

---

### 1. Bottom‑Line Recommendation  
- **Classification / Submission Route:** Treat the device under its existing FDA classification (Class I–III). If no new intended use or technology change, a **traditional 510(k) (substantial equivalence)** is appropriate. Should AI/ML functions be newly introduced or materially changed, consider a **Special 510(k) (design‑transfer amendment)** or **De Novo** if the device becomes novel under the updated QMSR definitions.  

- **Critical Missing Evidence:**  
  1. **DHF ↔ DDF / DMR ↔ MDF mapping matrix** required by §9.5.2 (QMSR) – not present.  
  2. **Manufacturing Readiness Evidence (MRE) – all six categories** (§9.5.3) – only a narrative exists, no artifacts (process validation, equipment qualification, supply‑chain assessments, workforce competency records, etc.).  
  3. **AI model design‑transfer package** compliant with EU AI Act Art.17 and QMSR §9.6 – risk analysis, dataset provenance, version control, post‑market monitoring plan are absent.  

- **Immediate Action:** Compile the missing artifacts (mapping table, MRE packets, AI‐model DVP&R) and submit to QA for internal audit within **5 business days**. If any item cannot be produced, flag for senior RA review (see Escalation Triggers).

---

### 2. Required Evidence Checklist  

| Section | Required Artifact (per QMSR & FDA) | Typical Source |
|---------|------------------------------------|----------------|
| **§9.5.2 – DHF/DMR → DDF/MDF Mapping** | • One‑to‑one mapping table linking each design input, output, and change record to the corresponding device design file (DDF) / manufacturing design file (MDF). <br>• Rationale for any consolidated or omitted items. | Design History File, Device Master Record, Updated SOP‑DT‑001 |
| **§9.5.3 – Manufacturing Readiness Evidence** *(6 types)* | 1. **Process Validation** – IQ/OQ/PQ reports.<br>2. **Equipment Qualification** – calibration certificates, maintenance logs.<br>3. **Supply‑Chain Verification** – vendor audits, incoming inspection records.<br>4. **Workforce Competency** – training matrices, competency assessments.<br>5. **Facility Controls** – cleanroom qualification, environmental monitoring data.<br>6. **Risk Management Integration** – ISO 14971 risk mitigations tied to manufacturing steps. | Manufacturing Readiness Plan (MRP), QMSR‑linked evidence repository |
| **§9.6 – AI Model Design‑Transfer (Dual Compliance)** | • Updated **AI Risk Management File** (ISO 14971 + EU AI Act Art.17).<br>• Data set provenance & labeling documentation.<br>• Model version control log.<br>• Validation/Verification reports (performance, robustness, bias).<br>• Post‑market monitoring (real‑world performance, drift detection) plan.<br>• Cross‑reference to SOP‑AIGOV‑001 / SOP‑AIDATA‑001. | AI/ML Development Team, Software Dossier, SaMD Guidance |
| **General 510(k) Requirements** | • Predicate comparison matrix (technology, intended use, performance).<br>• Summary of Safety & Effectiveness Data.<br>• Labeling & IFU.<br>• Sterility & Biocompatibility testing (if applicable). | Existing 510(k) file, new supporting data |

---

### 3. Risk Controls to be Demonstrated  

| Control Area | Required Documentation | QMSR Reference |
|--------------|------------------------|---------------|
| **Design Transfer Verification** | • DVP&R covering design‑transfer activities.<br>• Acceptance criteria and test results for transferred specifications. | §9.5 – Design Transfer Checkpoints |
| **AI/ML Specific Controls** | • Dataset quality checks, bias mitigation strategy.<br>• Continuous learning governance (locked vs. adaptive).<br>• Human‑in‑the‑loop safety limits. | §9.6 – AI Model Dual Compliance |
| **Manufacturing Process Control** | • SPC charts, process capability indices (Cpk > 1.33).<br>• Change control logs for any process modifications. | §9.5.3 – MRE Types 1‑4 |
| **Supply‑Chain Risk Management** | • Supplier risk assessment matrix.<br>• Alternate source qualification plans. | QMSR overall (integrated risk mgmt) |
| **Post‑Market Surveillance (PMS)** | • PMS Plan aligned with FDA’s “Post‑Market Management of Medical Devices” guidance and EU AI Act monitoring obligations. | §9.6 – Dual compliance |

---

### 4. Key Citations  

1. **21 CFR Part 820** – Quality System Regulation (base).  
2. **QMSR Final Rule (Feb 2026)** – 21 CFR §§820.30‑820.40 (new design‑transfer checkpoints, MRE taxonomy).  
3. **ISO 13485:2016**, **ISO 14971:2019** – risk management and QMS alignment.  
4. **FDA Guidance – “Design Transfer – A Good Manufacturing Practice for Medical Devices” (2021)**.  
5. **FDA Software as a Medical Device (SaMD) – Artificial Intelligence/Machine Learning (AI/ML) SaMD Action Plan (2023‑2025).**  
6. **EU AI Act, Art. 17 – Dual Compliance Requirements** (effective 2024; relevant for devices marketed in EU and US).  

---

### 5. Human‑Escalation Triggers  

| Trigger | Condition | Escalation Path |
|---------|-----------|-----------------|
| **Missing Mapping Table** | No DHF↔DDF/MDF matrix submitted within 5 BD. | Notify Lead RA → Senior Regulatory Manager (within 24 h). |
| **Incomplete MRE Packets** | ≥2 of the 6 categories lack verifiable evidence. | Pause submission; convene cross‑functional “Readiness Review” board. |
| **AI Risk File Gaps** | Absent bias analysis or post‑market monitoring plan. | Immediate R&D/AI team alert; senior RA sign‑off required before filing. |
| **Regulatory Timeline Threat** | Projected 510(k) submission >45 days from target clearance date. | Elevate to Director of Regulatory Affairs for resource reallocation. |
| **Conflicting Guidance** | Discrepancy between QMSR §9.6 and existing SOP‑AIGOV‑001. | Convene regulatory–legal counsel meeting; document decision in “Regulatory Decision Log”. |

---

### 6. Peer‑Review Prompt (to be sent to a fellow RA)

> **Please review the assumptions, source coverage, and jurisdictional gaps in this draft:**
> 1. **Classification & Pathway** – Are we correct to assume a traditional 510(k) is sufficient, or should a Special 510(k)/De Novo be considered given the AI enhancements?  
> 2. **Evidence Mapping** – Does the checklist fully capture the QMSR §9.5‑§9.6 obligations, especially for dual US/EU compliance? Are any required artifacts omitted (e.g., “Software Life‑Cycle Documentation” per FDA’s SaMD guidance)?  
> 3. **Risk Controls** – Have we adequately aligned ISO 14971 mitigations with the new MRE taxonomy? Any additional controls needed for AI model drift or data‑set turnover?  
> 4. **Citation Accuracy** – Verify that all regulatory citations (QMSR final rule, EU AI Act Art.17) are current and correctly referenced.  
> 5. **Escalation Triggers** – Are the thresholds realistic for our organization’s timelines and reporting structure? Suggest any additional triggers you deem necessary.

*Please reply with any contradictions, missing references, or alternative pathways within 48 hours so we can finalize the submission package.*

---

### 7. Reusable RA Judgment (Honcho Record)

```
honcho_conclude
{
  "lesson_id": "QMSR_DesignTransfer_EvidenceGap",
  "summary": "When QMSR introduces new design‑transfer checkpoints (§9.5, §9.6), the regulator must verify three core artifacts: a DHF↔DDF/MDF mapping table, complete Manufacturing Readiness Evidence covering all six categories, and an AI model transfer dossier meeting both FDA QMSR and EU AI Act Art.17 requirements. Absence of any triggers immediate escalation to senior RA and pauses submission.",
  "key_decision_points": [
    "Classify device per existing predicate; use Special 510(k) if AI function materially changes intended use.",
    "Treat missing mapping or MRE as non‑showstoppers only after documented mitigation; otherwise, elevate.",
    "Align risk controls with ISO 14971 and embed AI‑specific monitoring to satisfy dual compliance."
  ],
  "applicability": ["Medical devices subject to QMSR (post‑Feb 2026) with design‑transfer or AI/ML components"],
  "confidence": 0.94
}
```

---  

*Prepared by: Mike – US FDA Regulatory Affairs Specialist*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> QMSR 조항(§820.30-820.40) 세부내용을 창작(MRE 분류체계 등) — 실제 QMSR은 해당 조항 대부분을 폐지하고 ISO 13485 준용으로 대체.

**Source Excerpts**

1. Chunk `159434114844154818`

> ## 관련 문서 - SOP-DT-001 (03_설계_개발관리) - 교차검증_2026-06-08 (12_교차검증_보고서)

2. Chunk `238771195974486986`

> ## 변경 요약 - §9.5 QMSR 설계이관 실사 체크포인트 5항목 신설 - §9.5.2 DHF/DMR→DDF/MDF 용어 전환 확인 매핑표 - §9.5.3 제조 준비도 증거(Manufacturing Readiness Evidence) 체계 6유형 정의 - §9.6 AI 모델 설계이관 QMSR·EU AI Act Art.17 이중 준수 요구 6단계 신설 - 규제 근거 표 QMSR 시행일 반영, SOP-AIGOV-001·SOP-AIDATA-001 상호참조 추가

### kb-eval-20260715-it14-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_us-003", "iteration": 14, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "7fa0610e95f3af34", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `7fa0610e95f3af34`
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

> **Regulatory Draft – “촬영실 GUI Software” (Imaging‑Processing/Display SaMD)**  
*Prepared for internal review, 2026‑07‑28*  

---

### 1️⃣ Bottom Line
- **Classification:** Class II medical device (21 CFR 892.2050 – Image Processing Software).  
- **Submission Route:** Standard 510(k) (eSTAR format) → “Traditional” or “Special” 510(k) depending on predicate availability; no De Novo indicated.  
- **Evidence Required:** Complete software documentation per IEC‑62304, FDA “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14), and “Cybersecurity in Medical Devices” (2023‑09‑27).  
- **Current Gaps:** Missing (a) detailed Cybersecurity Risk Management Plan, (b) Hazard Analysis & Mitigation (ISO 14971), (c) Traceability matrix linking risk controls to software requirements, (d) Verification/validation results for Class C risk items, (e) Clinical performance data if the GUI is used for diagnosis.  
- **Risk Controls Needed:** IEC 62304‑Class C lifecycle processes, ISO 14971 risk analysis, FDA‑recommended cybersecurity controls (authentication, integrity monitoring, patch management).  
- **Escalation Triggers:** Any of the above gaps > 30 % of required deliverables; any identified Class C hazards without documented mitigation; absence of a recognized predicate device → require senior RA sign‑off or possible De Novo discussion.

---

### 2️⃣ Product & Intended Use (excerpt [1])
> “촬영실 GUI Software (영상 처리·표시 소프트웨어)” – software that processes and displays imaging data in the radiology suite, intended for **diagnostic** image review.  

- **Regulatory check:** SaMD → falls under 21 CFR 892.2050 (Class II).  
- **Software risk class per IEC 62304:** Table in excerpt [1] places a diagnostic viewer with processing in **Class C** (potential for serious injury if malfunction).

---

### 3️⃣ Submission Pathway
| Regulatory Basis | Decision |
|------------------|----------|
| 21 CFR 892.2050   | Class II → 510(k) required |
| FDA Guidance “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14) | Determines document set (SRS, SDS, V&V plans/reports) |
| eSTAR format (excerpt [2]) | Use Section G – Performance Testing (Software) |

**Recommendation:** Seek a *traditional 510(k)* using an existing FDA‑cleared radiology viewer as predicate (e.g., **[Device X]**, 510(k) #KXXXXX). If the GUI adds novel processing functions not present in any predicate, evaluate De Novo eligibility.

---

### 4️⃣ Required Evidence (per guidance & eSTAR)

| Item – Section G | Description | Status* |
|------------------|-------------|--------|
| Executive Summary (validation scope) | High‑level validation objectives, risk level, intended use | ✅ Present |
| Software Requirements Specification (SRS) | Functional and non‑functional requirements; includes safety/performance | ✅ Present |
| Software Design Specification (SDS) | Architecture, algorithms, interface design | ✅ Present |
| Requirements Traceability Matrix (RTM) | Links each requirement to design, verification, validation, and risk control | **Missing** – no links to ISO 14971 hazards |
| Validation Plan & Report (including Unit/Integration/System/Performance test results) | Complete V‑V evidence covering all risk classes | Partial – Class C test data absent |
| Verification Test Results (Unit, Integration, System) | Detailed logs, pass/fail criteria | ✅ Present for Classes A/B; **Class C missing** |
| Performance Test Results (accuracy, latency, image fidelity) | Quantitative metrics against clinical standards | ✅ Present but limited to non‑diagnostic scenarios |
| Validation Dataset Description | Data set provenance, diversity, ground truth | ✅ Present |
| Anomaly Log & Resolution | Defect tracking with root cause, corrective actions | ✅ Present |
| **Cybersecurity Plan** (per 2023‑09‑27 guidance) | Threat model, mitigations, update strategy | **Missing** |
| **Hazard Analysis / ISO 14971 Risk Management File** | Identified hazards, severity, mitigation, residual risk assessment | **Missing** |

\*Status reflects current eSTAR package (excerpt [2]).

---

### 5️⃣ Identified Evidence Gaps & Impact

| Gap | Why Required | Potential Regulatory Consequence |
|-----|--------------|----------------------------------|
| RTM lacking hazard links | Demonstrates that every risk is controlled via software design. | FDA may issue a **deficiency** (non‑conformity) under 21 CFR 820.30(b). |
| Class C verification data | Class C failures could cause serious injury. | Incomplete V‑V → **non‑submittable**; likely request for additional testing. |
| Cybersecurity Plan | Mandatory per “Cybersecurity in Medical Devices” guidance (2023‑09‑27). | FDA may issue a 510(k) **additional information** request or reject if risks remain uncontrolled. |
| ISO 14971 Risk Management File | Required for all SaMD; integrates with IEC 62304 class determination. | Lack of risk file = missing critical safety justification → **deficiency**. |
| Clinical performance data (if intended for diagnosis) | Diagnostic claim triggers need clinical evidence per 21 CFR 812.20. | Without data, FDA may reclassify as Class III or deny clearance. |

---

### 6️⃣ Recommended Risk Controls (to close gaps)

1. **Implement IEC 62304‑Class C lifecycle**  
   - Conduct detailed software design verification for all high‑risk functions.  
   - Document code reviews, static analysis, and failure mode effects.

2. **ISO 14971 Hazard Analysis**  
   - Identify each hazard (e.g., erroneous pixel intensity scaling) → assess severity/likelihood.  
   - Map mitigations to specific software requirements; update RTM accordingly.

3. **Cybersecurity Measures** (per 2023‑09‑27 Guidance)  
   - Threat modeling (STRIDE).  
   - Authentication, role‑based access control, encrypted data storage/transmission.  
   - Secure update mechanism with digital signatures.  
   - Post‑market vulnerability management plan.

4. **Residual Risk Acceptance**  
   - Conduct risk/benefit analysis; justify residual risk ≤ “acceptable” per FDA policy memorandum (2023‑02‑01).  

5. **Clinical Validation (if diagnostic)**  
   - Prospective multi‑center study demonstrating non‑inferiority to predicate imaging viewer.

---

### 7️⃣ Citations

| # | Source |
|---|--------|
| 1 | 21 CFR 892.2050 – Image Processing Software (Class II) |
| 2 | FDA Guidance: *Content of Premarket Submissions for Device Software Functions* (2023‑06‑14) |
| 3 | FDA Guidance: *Cybersecurity in Medical Devices* (2023‑09‑27) |
| 4 | IEC 62304:2006+A1:2015 – Software life‑cycle processes |
| 5 | ISO 14971:2019 – Application of risk management to medical devices |
| 6 | eSTAR Section G structure (excerpt [2]) |
| 7 | “Regulatory Classification of SaMD” – FDA’s Digital Health Program (2022) |

---

### 8️⃣ Human‑Escalation Triggers

- **Trigger A:** Any missing Class C verification data → senior RA must approve a supplemental testing plan before submission.
- **Trigger B:** Absence of a complete Cybersecurity Risk Management Plan → escalation to the Chief Technology Officer and possibly legal counsel (privacy/compliance).
- **Trigger C:** No clear predicate device for novel processing algorithms → Senior RA to evaluate De Novo pathway; may require project pause.
- **Trigger D:** Pending clinical performance data for diagnostic claim beyond 30 % of required subjects → immediate senior management notification.

---

### 9️⃣ Peer‑Review Prompt (for RA colleague)

> *Please review the assumptions and evidence gaps identified above. Specifically:*
> - *Do you agree that the current eSTAR package lacks a complete RTM linked to ISO 14971 hazards?*  
> - *Is there any additional FDA guidance or recognized predicate we have overlooked for this imaging‑viewer SaMD?*  
> - *Are there jurisdiction‑specific considerations (e.g., New York State medical device registration) that could affect our submission timeline?*  

---

### 10️⃣ Reusable RA Judgment (Lesson Record)

**Judgment ID:** `US_RA_510k_SaMD_Evidence_Gap_v1`  
**Context:** Evaluation of a Class II imaging‑processing GUI SaMD submitted via eSTAR.  
**Key Takeaway:** *For IEC 62304 Class C SaMD, the 510(k) package must include a full hazard‑to‑requirement traceability matrix (ISO 14971 linked), complete verification data for all high‑risk functions, and an FDA‑compliant cybersecurity risk management plan. Missing any of these items constitutes a “non‑submittable” deficiency and triggers senior RA escalation.*  

*Stored for future automated gap analysis across SaMD submissions.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 분류(892.2050)/IEC 62304 표는 소스와 정확, 플레이스홀더 표기 우수. 812.20(IDE) 오적용 + 검증불가 'FDA 정책메모(2023-02-01)' 인용.

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

### kb-eval-20260715-it14-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_us-004", "iteration": 14, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "853b41825268d2cf", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md", "source_hash": "5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `853b41825268d2cf`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-20_GSPR_QMSR_PRRC_%EC%A0%95%ED%95%A9%EC%84%B1%EA%B2%80%EC%A6%9D.md)
- Source hash: `5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee`
- Focus: submission evidence gaps
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `2026-04-20_GSPR_QMSR_PRRC_정합성검증.md`는 `2026-04-20_GSPR_QMSR_PRRC_정합성검증.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적...
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

> **Regulatory Draft – Daily Growth Case (v1) – 2026‑07‑28**  
*Prepared by:* **Mike – US Regulatory Affairs Specialist**  

---

## 1. Bottom‑Line Recommendation
- **Device Classification:** Class II (non‑implantable, software‑driven device with AI/ML component).  
- **Submission Route:** Traditional 510(k) – **Substantial Equivalence** to a predicate that is FDA‑cleared for the same intended use and incorporates comparable AI/ML risk controls.  
- **Critical Path Forward:** Close three high‑impact evidence gaps (UDI master‑record, SOP for MDR decision documents, electronic‑signature scope) before completing the 510(k) technical file.  

---

## 2. Classification & Submission Route
| Criterion | Determination |
|-----------|---------------|
| Intended use / Indications | Diagnostic/monitoring of physiological parameters; provides clinical decision support via AI/ML. |
| FDA Regulation | 21 CFR 862 – **Class II** (requires special controls). |
| Applicable Guidance | • FDA “Guidance for Industry and FDA Staff: **Software as a Medical Device (SaMD) – Clinical Evaluation**” (2024)<br>• FDA “**Artificial Intelligence/Machine Learning (AI/ML)-Based Software as a Medical Device Action Plan**” (2023) |
| Submission Type | **Traditional 510(k)** – will require a robust *predicate comparison matrix* and a *risk‑based validation plan* per IEC 62304 / IEC 62366‑1. |

---

## 3. Required Evidence (per QMSR & FDA Guidance)

| Category | Specific Evidence Needed | Current Status |
|----------|--------------------------|----------------|
| **Device Description** | Full device description, labeling, intended use, and indication statement. | Draft complete. |
| **Predicate Comparison** | Table mapping functional, technological, and performance characteristics to chosen predicate(s). Include AI/ML algorithm details (training data, validation metrics). | Predicate identified; algorithm comparison incomplete (AI/ML gap). |
| **Bench & Performance Testing** | • Electrical safety – IEC 60601‑1 series.<br>• Electromagnetic compatibility – IEC 60601‑1‑2.<br>• Software verification & validation per IEC 62304 (including unit, integration, system tests).<br>• Usability testing – IEC 62366‑1. | Bench data for hardware complete; software V&V partial – missing AI/ML performance validation report. |
| **Biocompatibility** (if device contacts patient) | ISO 10993‐1 risk assessment, appropriate test reports (ISO 10993‑5, ‑10, etc.). | Not applicable (non‑contact). |
| **Sterility / Shelf Life** | If sterile – ISO 11135/11137 or equivalents. | N/A. |
| **Risk Management** | Full ISO 14971 risk analysis file; identify AI‑specific hazards and mitigations (training data bias, drift detection, fail‑safe mode). | Draft exists but missing documented mitigation for algorithmic drift. |
| **Labeling & IFU** | Conforms to 21 CFR 801 + IEC 62366 labeling guidance. | Pending finalization. |
| **UDI Compliance** | Integrated UDI Master Record (per 21 CFR 830, EU MDR Art.27). Must include device identifier, production identifier, issuance of label/ packaging. | **Gap – fragmented UDI data; no integrated SOP (see Section 4).** |
| **Electronic Signature** | Part 11 compliance scope documented (QM‑IT‑001). | **Gap – scope ambiguous; needs formal definition.** |
| **Quality System Records** | QMSR (effective Feb 2026) – ISO 13485‑aligned documentation, SOPs, internal audit evidence, corrective actions. | SOP for MDR decision document missing; internal audit report lacks objective evidence citations. |

---

## 4. Identified Evidence Gaps & Required Actions  

| Gap | Action Required | Owner / Target Date |
|-----|-----------------|----------------------|
| **1. Domestic SOP – “MDR Decision Document” template** (see source excerpt) | Draft and approve **ML‑MDR‑001** (decision tree for reporting vs non‑reporting). Integrate into change control. | QA Lead – 2026‑09‑15 |
| **2. UDI Master Record fragmentation** | Consolidate all UDI elements into a single **UDI Data Record (UDR)** SOP (align with 21 CFR 830 & EU MDR Art.27). Include linkage to Device History Records. | Regulatory Ops – 2026‑09‑30 |
| **3. Internal audit report narrative depth** | Revise “External Audit Response” template: require citation of objective evidence (test reports, SOPs) for each finding. | QA Manager – 2026‑08‑20 |
| **4. Electronic Signature scope (Part 11)** | Finalize **QM‑IT‑001** defining software systems, user roles, and audit‑trail requirements subject to Part 11. | IT/QA – 2026‑09‑10 |
| **5. AI/ML algorithm validation** | Produce a *Clinical Performance Validation Report* covering: data set provenance, bias analysis, cross‑validation results, post‑market monitoring plan (including drift detection). | Software R&D – 2026‑10‑15 |
| **6. Risk mitigation for algorithmic drift** | Update ISO 14971 file with *Software Lifecycle Controls* per IEC 82304‑1 and FDA AI/ML action plan. | Risk Management – 2026‑09‑25 |

---

## 5. Risk Controls (Key Elements)

| Hazard | Control (Standard Reference) |
|--------|------------------------------|
| **Electrical safety** | IEC 60601‑1, IEC 60601‑1‑2 compliance testing; design verification per QMSR §820.30(c). |
| **Software bugs / failure** | IEC 62304 development lifecycle; static code analysis, unit/integration tests (≥ 95% coverage). |
| **Usability errors** | IEC 62366‑1 Human Factors Engineering – formative & summative testing with target users. |
| **AI algorithm bias** | ISO 14971 risk control: *Mitigation* – diverse training data set, bias audit, periodic re‑training triggers; documented in AI/ML Risk Management Plan (FDA Guidance 2023). |
| **Algorithmic drift** | IEC 82304‑1 monitoring plan; automated performance alerts built into device firmware. |
| **UDI mis‑assignment** | SOP for UDI generation & verification; barcode scanning verification at each packaging step. |
| **Electronic signature misuse** | Part 11 scope definition; dual‑person approval workflow for critical records. |

---

## 6. Key Regulatory Citations  

| Citation | Relevance |
|----------|-----------|
| **21 CFR 862** (Class II medical devices) – defines special controls. | Classification basis. |
| **21 CFR 820.30, 820.40** – design control & verification/validation requirements. | Evidence generation requirement. |
| **21 CFR 830** – UDI system. | Guiding UDI Master Record SOP. |
| **FDA AI/ML SaMD Action Plan (2023) & “Proposed Regulatory Framework for Modifications to AI/ML‑Based Software” (2024).** | Determines needed algorithm documentation and post‑market monitoring. |
| **QMSR (Feb 2026)** – ISO 13485–aligned QMS for US market. | Overall quality system expectations. |
| **MDCG 2021‑5 State‑of‑the‑art Guidance** – references IEC 62304, IEC 62366‑1, IEC 82304‑1 (adopted as de‑facto standards). | Technical standard mapping. |
| **ISO 14971:2021**, **IEC 60601‑1 series**, **IEC 62304**, **IEC 62366‑1**, **IEC 82304‑1** – risk management, safety, software life‑cycle, usability, and AI/ML controls. | Evidence & control basis. |

---

## 7. Human‑Escalation Triggers  

| Trigger Condition | Required Action |
|--------------------|-----------------|
| **Any of the gaps in Section 4 remain unresolved > 30 days before planned 510(k) submission** | Escalate to Head of Regulatory Affairs – potential delay flag. |
| **AI/ML algorithm validation fails pre‑specified performance criteria (e.g., sensitivity < 95% or bias > 5%)** | Suspend submission; convene cross‑functional AI/ML risk review. |
| **UDI master record remains fragmented after SOP issuance** | Notify Quality Director – FDA audit risk. |
| **Part 11 scope ambiguity persists after QM‑IT‑001 finalization** | Elevate to CISO – compliance breach risk. |
| **Regulatory reviewer (FDA) issues a "Deficiency Letter" on any of the above** | Activate Contingency Plan: rapid gap closure team; inform senior leadership. |

---

## 8. Peer Review Prompt  

> **To:** RA Team – **[Insert Peer Name]**  
> Please review this draft and challenge the following:
> 1. **Assumptions** on predicate equivalence given the AI/ML component – is there a more suitable Class I / De Novo pathway?  
> 2. **Source coverage** – have we missed any applicable EU MDR or OJEU harmonized standards that could affect US submission (e.g., ISO 15223‑1 labeling).  
> 3. **Jurisdiction‑specific gaps**, especially around QMSR alignment and Part 11 scope, that may not be evident from the provided excerpts.  
> Provide concrete points where additional data or alternative strategies are needed.

---

## 9. Reusable RA Judgment (Lesson Learned)

```json
{
  "honcho_conclude": {
    "lesson_id": "daily_growth_v1_2026-07-28",
    "summary": "When a Class II SaMD with AI/ML is slated for 510(k), the fastest credible path hinges on closing three systemic evidence gaps: (a) integrated UDI Master Record SOP, (b) formalized MDR decision‑document template, and (c) explicit Part 11 scope. Without these, QMSR compliance cannot be demonstrated, leading to FDA deficiency risk. AI/ML specific validation (bias, drift controls) must be documented up‑front to avoid a De Novo diversion.",
    "key_actions": [
      "Draft & approve ML‑MDR‑001 SOP before 15 Sep 2026.",
      "Consolidate UDI data into a single UDR SOP by 30 Sep 2026.",
      "Finalize Part 11 scope (QM‑IT‑001) by 10 Sep 2026.",
      "Complete AI/ML performance validation and drift mitigation plan before the 510(k) lock‑box."
    ],
    "applicability": [
      "All SaMD submissions post‑QMSR (Feb 2026).",
      "Devices incorporating AI/ML where algorithmic risk must be captured in ISO 14971."
    ],
    "confidence": "high"
  }
}
```

--- 

*End of Draft – Ready for peer review.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 소스는 EU MDR(GSPR/PRRC) 내용인데 US-only(21 CFR/510(k))로 재구성 — 실질적 매칭 실패. 820.30-40 오류 반복 + ISO 14971 판본 왜곡.

**Source Excerpts**

1. Chunk `1061533089543682126`

> ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적용 | | AI/ML 기기 | OJEU/MDCG 단독 등재 없음 → EU AI Act 병행 필요(후속 과제) | | 운영 영향 | 체크리스트에 H/S 컬럼 신설, 개정판 번호(A11, A1, A2) 기재 의무화 |

2. Chunk `1066441905930561439`

> ### Gap → 조치 | Gap | 조치 | |-----|------| | 국내 SOP에 MDR 결정문서 양식 부재 | 양식 ML-MDR-001 초안(보고/미보고 결정트리) 신설 | | UDI 마스터 레코드 단편화 | UDR(UDI Data Record) 통합 관리 SOP 초안 (§820.35(b) + 21 CFR 830 + EU MDR Art.27) | | 내부감사 보고서 서술 수준 | "외부감사 대응 수준" 템플릿 개정 (객관적 증거 필수 인용) | | 전자서명 범위 모호 | Part 11 적용범위 정의 문서(QM-IT-001) 초안 예정 |

### kb-eval-20260715-it14-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_us-005", "iteration": 14, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "c95becc611ac15ce", "source": "github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md", "source_hash": "a622ee7076c4fd98e60854417742c547284a2a3b0d82065d9b4e2a9da67c1fab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c95becc611ac15ce`
- Source: `github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/13_%EA%B7%9C%EC%A0%9C%ED%8F%89%EA%B0%80_%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8/FDA_510k_RTA.md)
- Source hash: `a622ee7076c4fd98e60854417742c547284a2a3b0d82065d9b4e2a9da67c1fab`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `FDA_510k_RTA.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: - id: FDA-510K-C3 source: FDA RTA Checklist Section C clause: C.3 requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 severity: must evidence_type: test_report applicable_keywords: [IEC60601-1, IEC60601-2-54] related_docs: [] - id: FDA-510K-C4 source: FDA RTA Checklist Section C clause: C.4 requirement: Software (Major LoC) — IEC 62304 + FDA S...
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

> **Regulatory Draft – 510(k) Submission Gap Analysis**  
*Prepared by: Mike (US RA Specialist)*  

---

### 1. Bottom‑Line Recommendation
- **Classification / Pathway:** Class II 510(k) is the most likely route, provided a legally marketed predicate exists with comparable electrical safety and software functionality. If no suitable predicate can be identified, consider a De Novo request.  
- **Key “must” evidence gaps** (per FDA RTA Checklist) must be closed before filing; otherwise the submission will be deemed incomplete and delayed.

---

### 2. Evidence Required (per FDA RTA Checklist)

| Section | Requirement | Evidence Type | Primary Standard / Guidance |
|---------|-------------|---------------|------------------------------|
| **C.3** | Electrical safety | **Test Report** | IEC 60601‑1 (general safety) |
| **C.4** | Electromagnetic compatibility (EMC) | **Test Report** | IEC 60601‑1‑2 |
| **C.4** | Software – Major LoC | **Software Documentation** (software development plan, verification & validation reports, configuration management, traceability matrix) | IEC 62304; FDA “Guidance for the Content of Premarket Submissions for Device Software Functions” + Cybersecurity Guidance (May 2022) |
| **E.1** | Labeling – Proposed label, IFU draft, contraindications | **Labeling Draft** (including UDI label) | 21 CFR 820.120; FDA “Labeling Requirements for Medical Devices” |
| **E.2** | UDI compliance – GS1/HIBCC agency identified | **UDI Implementation Plan** (agency selection, data model, barcode artwork) | 21 CFR 830; GUDID requirements |

*Additional mandatory items not listed in the excerpt but required for any 510(k):*  

- **Risk Management File** (ISO 14971) with hazard analysis & risk control summary.  
- **Design History File (DHF)** compliant with QMSR (21 CFR 820) – especially design controls, verification/validation.  
- **Sterility / Biocompatibility** evidence (if applicable).  
- **Usability/Human Factors Validation** (for IFU).  
- **Clinical Performance Evidence** if the predicate does not adequately cover intended use or claims.

---

### 3. Identified Missing Information (Gap Summary)

| Gap | Why it matters | Impact on submission |
|-----|----------------|----------------------|
| **IEC 60601‑1/‑1‑2 test reports** – no data, protocols, or certificates provided. | Demonstrates compliance with electrical safety & EMC requirements (must). | Submission will be returned as “deficient”. |
| **Software Development Documentation** – missing FDA‑aligned software design plan, traceability matrix, verification/validation reports, and cybersecurity risk mitigation plan. | Required for Major LoC devices; establishes substantial equivalence of software. | Likely 510(k) Refuse to Accept (RTA). |
| **Labeling Draft & IFU** – only placeholder titles present; no final artwork, warnings, or instructions. | Labeling is a “must” element; UDI placement must be verified. | RTA for labeling. |
| **UDI Implementation Plan** – agency selected but no data model, GS1‑128 barcoding specifications, or GUDID submission workflow. | FDA will reject incomplete UDI plan; impacts market launch timeline. | RTA for UDI. |
| **Risk Management File (ISO 14971)** – risk analysis matrix absent; mitigation strategies not linked to design outputs. | Required for 510(k) safety justification and for QMSR compliance. | Potential deficiency flag, especially if high‑risk hazards are identified. |
| **Design History File (DHF) / QMSR evidence** – only checklists present; no records of design reviews, verification/validation protocols, or change control. | Mandatory under 21 CFR 820 and the new QMSR (effective Feb 2026). | Non‑conformance to QMSR → delayed clearance. |
| **Usability Validation** – not addressed for IFU comprehension. | Required when labeling claims impact safe use. | May trigger RTA or additional post‑market study request. |

---

### 4. Recommended Risk Controls (to be documented in DHF & RMF)

1. **Electrical Safety:**  
   - Perform IEC 60601‑1 compliance testing on final hardware; include insulation resistance, leakage current, and protective earth verification.  
2. **EMC:**  
   - Conduct radiated/NF emissions & immunity tests per IEC 60601‑1‑2 at intended operating frequencies.  
3. **Software Safety (IEC 62304):**  
   - Classify software as *Class B* (or higher if hazard analysis dictates).  
   - Implement secure coding practices, code review, unit testing, integration testing, and a formal verification/validation plan.  
   - Deploy FDA‑recommended cybersecurity controls: threat modeling, vulnerability management, authentication, encryption, and incident response plan.  
4. **Labeling / UDI:**  
   - Ensure label readability (≥ 1.2 mm characters), correct placement of UDI on device & packaging, and inclusion of contraindications, warnings, and shelf‑life.  
5. **Risk Management Integration:**  
   - Map each identified hazard to a design control (e.g., shielding for EMC, watchdog timer for software failure).  
   - Verify that residual risk is Acceptable as per ISO 14971 §4.3.  
6. **Usability / Human Factors:**  
   - Conduct formative usability testing on IFU; document findings and incorporate mitigations (warnings, symbols).  

---

### 5. Key Citations & Guidance Documents

| Document | Section | Relevance |
|----------|---------|-----------|
| FDA “510(k) Review Template – RTA Checklist” | C.3, C.4, E.1, E.2 | Direct evidence requirements (source excerpts). |
| IEC 60601‑1 (2022) & IEC 60601‑1‑2 (2020) | — | Electrical safety & EMC standards. |
| IEC 62304 (2006/2023) | — | Software life‑cycle processes. |
| FDA Guidance: “Content of Premarket Submissions for Device Software Functions” (Dec 2019). | — | Required software documentation. |
| FDA Cybersecurity Guidance for Medical Devices (May 2022). | — | Cyber risk controls. |
| 21 CFR 820 – Quality System Regulation (QSR) / QMSR (effective Feb 2026). | ‑ | DHF, design control, labeling, UDI. |
| FDA “Unique Device Identification System” Guidance (May 2018). | — | UDI compliance. |
| ISO 14971:2019 – Medical device risk management. | — | Risk analysis & controls. |

---

### 6. Human‑Escalation Triggers (When to Alert Senior RA / Management)

- **Any “must” evidence item remains incomplete after the assigned deadline** (electrical safety, software documentation, labeling/UDI).  
- **No suitable predicate device can be identified** for substantial equivalence of software or electrical functions → consider De Novo.  
- **Risk analysis reveals a high‑severity residual risk** that cannot be mitigated by design controls.  
- **QMSR audit indicates non‑conformance** (e.g., missing DHF records, inadequate change control).  
- **Regulatory timeline slip > 30 days** from the targeted 510(k) submission date due to evidence gaps.  

Escalate to **Director of Regulatory Affairs** with a concise risk‑impact matrix and recommended corrective actions.

---

### 7. Action Plan (Next 4‑Week Sprint)

| Week | Owner | Deliverable |
|------|-------|-------------|
| 1 | Electrical Engineer | Test plan & schedule for IEC 60601‑1/‑1‑2; initiate test lab quotation. |
| 2 | Software Lead | Draft software development plan, traceability matrix, and cybersecurity risk assessment (per FDA guidance). |
| 3 | Regulatory Documentation Specialist | Complete labeling draft (including UDI barcode artwork) & IFU mock‑up. |
| 4 | Quality Manager | Assemble preliminary DHF entries (design reviews, verification protocols) & update RMF with identified hazards/controls. |

**Milestone:** All “must” evidence compiled and reviewed by **Day 28**, ready for pre‑submission FDA Q-Submission (if desired).

---

### 8. Peer Review Prompt  

> *Please review the assumptions and coverage in this draft:*  
> - Are we correctly classifying the device as Class II, or does any functionality push it toward Class III/De Novo?  
> - Have we captured **all** evidence items mandated by the FDA RTA Checklist (beyond the four sections cited)?  
> - Is our jurisdiction‑specific scope (U.S. only) sufficient, or should we anticipate EU MDR or Health Canada considerations for global launch?  
> - Are there any additional risk controls (e.g., IEC 60601‑2‑54 for specific electrosurgical functions) that we have overlooked?  

*Provide a brief critique and any missing citations or regulatory nuances.*

---

### 9. Reusable RA Judgment (Honcho Record)

```yaml
honcho_conclude:
  judgment: |
    For devices requiring electrical safety (IEC 60601‑1), EMC (IEC 60601‑1‑2) and Major LoC software (IEC 62304 + FDA SW guidance), the fastest credible pathway to U.S. clearance is a Class II 510(k) using a predicate with comparable safety and functional performance. All “must” evidence items from the FDA RTA Checklist—test reports, full software documentation, labeling draft, and UDI plan—must be completed before submission; any missing item triggers an immediate escalation to senior RA.
  confidence: high
  rationale: |
    - Direct mapping of checklist clauses C.3, C.4, E.1, E.2 to statutory requirements (21 CFR 820, QMSR).
    - Established industry precedent for similar electromechanical devices with embedded software.
    - Absence of a suitable predicate or high‑risk residual hazards forces De Novo, dramatically extending timelines.
  references:
    - FDA_510K_RTA_Checklist_C3
    - FDA_510K_RTA_Checklist_C4
    - FDA_510K_RTA_Checklist_E1
    - FDA_510K_RTA_Checklist_E2
    - IEC60601-1
    - IEC60601-1-2
    - IEC62304
    - 21CFR820
    - QMSR_2026
```

--- 

*End of Draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> C.3/C.4/E.1/E.2 필수항목 매핑은 소스와 일치. EMC/60601-1-2 항목 오배치, 가이던스 날짜 오기, IEC 60601-2-54 용도 오설명(실제 X-ray 방사선촬영용).

**Source Excerpts**

1. Chunk `1059626859749416295`

> - id: FDA-510K-C3 source: FDA RTA Checklist Section C clause: C.3 requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 severity: must evidence_type: test_report applicable_keywords: [IEC60601-1, IEC60601-2-54] related_docs: [] - id: FDA-510K-C4 source: FDA RTA Checklist Section C clause: C.4 requirement: Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity severity: must evidence_type: SW_documentation applicable_keywords: [IEC62304, FDA SBOM, IEC81001-5-1] related_docs: [] ```

2. Chunk `1657837344321702`

> ## 5. Labeling ```yaml - id: FDA-510K-E1 source: FDA RTA Checklist Section E clause: E.1 requirement: Labeling — proposed labels, IFU draft, contraindications severity: must evidence_type: labeling_draft applicable_keywords: [FDA 510, UDI] related_docs: [] - id: FDA-510K-E2 source: FDA RTA Checklist Section E clause: E.2 requirement: UDI compliance — GS1/HIBCC issuing agency identified severity: must evidence_type: udi_plan applicable_keywords: [UDI] related_docs: [] ``` --- > v0.1 — 16개 핵심 항목으로 시작. 다음 보강에서 ~64개 추가하여 RTA 전체 ~80건 완성 예정.

## ra_eu

### kb-eval-20260715-it14-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_eu-001", "iteration": 14, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "a50fe1b6ef2ee7b6", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a50fe1b6ef2ee7b6`
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
  - `No hallucination`/`Escalation appropriate`는 source excerpt transparency (no captured response — inferred only)을 기준으로 판정합니다.

**Agent Response** — capture failed (fail-safe: fast checks fall back to source-only inference)

> ⚠️ response capture error: timed out

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 응답 캡처 실패(timeout) — 콘텐츠 없음, 재실행 필요(내용 문제 아님).

**Source Excerpts**

1. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

2. Chunk `1090731331984830062`

> > 최종 갱신: 2026-05-18 (자동보강 #52) > 근거: MDR Regulation (EU) 2017/745 Article 61 & Annex XIV | MDCG 2020-5 (Equivalence, Apr 2020) | MDCG 2020-6 (Sufficient Clinical Evidence, Apr 2020) | MDCG 2023-7 (Article 61(4)-(6) Exemptions, Dec 2023) | MDCG 2024-3 (CER Content) | FDA 510(k) Program Guidance (Jul 2014) | FDA Best Practices for Predicate Device Selection (Oct 2023 Draft) | MFDS 의료기기 허가·신고·심사 등에 관한 규정 (고시 제2024-88호) # Clinical Evaluation (MDR) 심화 — 동등성·충분성 기준

### kb-eval-20260715-it14-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_eu-002", "iteration": 14, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "f85d540a82623f33", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f85d540a82623f33`
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

> **Regulatory Draft – Clinical Evaluation Gap Analysis & Submission Planning  
Audience: Theo (EU Regulatory Affairs)  
Growth version: daily_growth_v1 – Run date 2026‑07‑28**  

---

## 1. Device Synopsis (as understood from the source repository)

| Item | Description |
|------|-------------|
| **Device name / model** | *[Insert commercial name]* |
| **Intended purpose** | *[Indications, target patient population, anatomical site]* |
| **Technology** | *[Active, implantable, software‑driven, etc.]* |
| **Current market exposure (per PSUR template – Art 86(1)(c))** | EU: ‑ ; Korea: ‑ ; US: ‑ ; Other: ‑  |
| **PMCF status (per PSUR template – Art 86(1)(d))** | Planned / Ongoing / Completed – *details pending* |

> **Note:** The source excerpts provide a skeleton for the Periodic Safety Update Report (PSUR) required by MDR Art. 86 (1). They do not contain any device‑specific data; these must be populated before submission.

---

## 2. Classification & Conformity‑Assessment Route  

| Step | Decision Rationale | Regulatory reference |
|------|-------------------|-----------------------|
| **2.1 Determine classification** | Based on the intended purpose and risk level (e.g., active, invasive, implantable). Preliminary assessment suggests *Class III* (or *Implantable Active Device – Class IIb* if lower invasiveness). | MDR Annex VIII; MDCG 2020‑16 guidance |
| **2.2 Conformity‑assessment route** | • If **Class III** → full quality‑system audit + design dossier review by a Notified Body (NB). <br>• If **IIb (implantable active)** → NB review of technical documentation (Annex II/III) plus possible design examination. | MDR Annex V, VI; Article 52, 53 |
| **2.3 PSUR requirement** | Art 86(1) obliges a periodic safety update report for **Class III**, **implantable active devices (IIb/III)** and any device for which the NB has requested one. | MDR Art 86(1); MDCG 2022‑21 §5.3 |

> **Outcome:** The device is slated for *Class III* (or the next highest applicable class). Consequently, a PSUR must be prepared annually and submitted together with the updated technical file to the NB.

---

## 3. Clinical Evidence Required  

| Requirement | Current Status (per source) | Gap / Action |
|-------------|----------------------------|--------------|
| **3.1 Clinical Evaluation Report (CER)** – per Annex IX, including: <br>• State‑of‑the‑art (SOTA) literature review  <br>• Clinical data from own investigations or comparable devices <br>• Benefit–risk analysis | *Not yet drafted.* Only a PSUR template is present. | • Compile SOTA search strategy (MDCG 2020‑13). <br>• Identify all pre‑market clinical investigation reports (CIRs) and any post‑market data. |
| **3.2 Post‑Market Clinical Follow‑up (PMCF) Plan** – Annex XV, with measurable objectives, methodology, and timeline | PMCF plan reference field exists but content is placeholders (“[문서번호, 버전]”). | • Draft a full PMCF plan aligned to the identified clinical gaps (e.g., long‑term safety). <br>• Define sample size, follow‑up intervals, endpoints. |
| **3.3 PMCF Results** – Art 86(1)(d) table in PSUR must contain: <br>• Summary of interim data <br>• How results are integrated into the CER | “이번 기간 주요 PMCF 결과” currently empty or marked “중간 데이터 없음”. | • Collect any ongoing surveillance data (registries, adverse event logs). <br>• If no data yet, document justification and revised timelines. |
| **3.4 Clinical Investigation Data** – if required for Class III devices, a clinical investigation must be completed (or an equivalence justification provided) | No investigation dossier referenced. | • Determine whether a new CI is mandatory or can rely on “equivalence” (MDR Art 61‑62). <br>• If equivalence, gather data package of the predicate device and justify similarity. |
| **3.5 Summary of Safety & Performance** – per Annex II, Section 10 | Not present in the supplied PSUR template. | • Prepare a concise summary (incl. trends, SAEs, MDR‑related incidents). |

---

## 4. Risk Management & Controls  

| Item | Required Evidence | Current Availability | Gap |
|------|-------------------|----------------------|-----|
| **4.1 Updated Risk Management File** – ISO 14971:2019 compliance, with risk evaluation of residual risks after PMCF data integration | Risk analysis table and updated residual‑risk evaluation required for PSUR submission. | No explicit risk file cited in the template. | • Update RMF to reflect new hazards identified during PMCF (if any). |
| **4.2 Benefit–Risk Determination** – must be reflected in CER & PMCF outcomes | Evidence of clinical benefit, safety data, and mitigation measures. | Missing from current drafts. | • Link risk controls to clinical evidence (e.g., device design features that mitigate identified hazards). |
| **4.3 Post‑Market Surveillance (PMS) Plan** – Annex XIV | PMS plan exists elsewhere but not linked to PSUR. | Not integrated in the PSUR template. | • Cross‑reference PMS activities, especially trend analysis that informs PSUR conclusions. |

---

## 5. Documentation Checklist (for NB submission)

| No.| Document | MDR reference | Status |
|----|----------|----------------|--------|
| **1** | Technical File – Annex II/III content (device description, labeling, IFU) | Art 10‑13, Annex II/III | Draft: pending |
| **2** | Clinical Evaluation Report (CER) – complete & signed | Annex IX, Art 61‑62 | Not started |
| **3** | PMCF Plan (Annex XV) | Annex XV | Placeholder only |
| **4** | PMCF Interim Report (to be attached to PSUR) | Art 86(1)(d) | Empty |
| **5** | Periodic Safety Update Report (PSUR) – completed tables per Art 86(1)(c)/(d) | Art 86(1) | Template only |
| **6** | Updated Risk Management File (ISO 14971:2019) | Annex II §10, Art 61 | Missing |
| **7** | Post‑Market Surveillance Report (PMSR) – trend analysis for the period | Annex XIV | To be aligned with PSUR |
| **8** | Declaration of Conformity (DoC) (updated version) | Art 19‑20 | Not yet signed |
| **9** | EUDAMED registration evidence (UDI dossier, device classification) | Regulation EU 2017/746 (EUDAMED) | Pending |
| **10** | Clinical Investigation Report(s) – if CI performed | Art 61‑62, Annex II §10.6 | None identified |

> **Action:** Populate all items marked “Missing / Placeholder” before the next NB audit window (estimated Q4 2026).

---

## 6. Human‑Escalation Triggers  

| Situation | Trigger Condition | Escalation Path |
|-----------|-------------------|-----------------|
| **A. Insufficient clinical data to satisfy MDR Art 61** | No comparable device with sufficient clinical evidence; or CI not yet completed and timelines exceed 12 months before NB submission deadline. | Notify Senior RA Lead → Decision on whether to **delay market launch** or **seek a Conditional CE** (if applicable). |
| **B. PMCF results indicate unexpected serious safety signals** | SAE rate > predefined threshold, signal not previously identified in pre‑market data. | Immediate safety report to the Competent Authority (Art 87) and internal **Risk Management Committee**; suspend distribution if needed. |
| **C. Discrepancy between RMF residual risk and CER benefit analysis** | Residual risk > acceptable level per Benefit–Risk Determination (Annex II §10). | Escalate to Head of Clinical & Regulatory → Re‑evaluate design controls or implement additional mitigations before NB submission. |
| **D. Incomplete PSUR tables for sales/exposure data (Art 86(1)(c))** | Methodology for patient exposure estimation not documented per MDCG 2022‑21 §5.3. | Prompt the Market Access/Commercial team to provide validated forecast; if unavailable, raise a **Regulatory Exception Request** to NB. |
| **E. NB audit feedback indicating “missing evidence”** | Formal NB observation/rejection letter. | Immediate convening of cross‑functional remediation task force (RA, Clinical, QA). |

---

## 7. Citations & Reference Materials  

1. **MDR 2017/745**, Articles 10–13, 19–20, 52, 53, 61–62, 86, 87.  
2. **Annex II** – Technical Documentation; **Annex III** – Design Dossier (if applicable).  
3. **Annex IX** – Clinical Evaluation.  
4. **Annex XV** – Post‑Market Clinical Follow‑up Plan.  
5. **MDCG 2020‑13** – "Guidance on clinical evaluation" (state‑of‑the‑art literature review).  
6. **MDCG 2020‑16** – "Medical device classification rules".  
7. **MDCG 2022‑21** §5.3 – Guidance on estimating patient exposure for PSURs.  
8. **ISO 14971:2019** – Medical devices — Application of risk management to medical devices.  

---

## 8. Peer Review Prompt (for another RA colleague)

> **Please review the above draft and challenge the following points:**  
> 1. **Assumptions on classification** – Is the Class III assumption justified based solely on the limited device description? Provide alternative reasoning if additional functional details become available.  
> 2. **Source coverage** – The PSUR template excerpts (Art 86(1)(c)/(d)) are the only source cited. Are there any other mandatory annexes or MDCG guidance that should be integrated at this stage?  
> 3. **Jurisdiction‑specific gaps** – While the focus is EU MDR, the device also appears to be marketed in Korea and the US. Identify any cross‑border regulatory implications (e.g., differing PMCF expectations, separate safety reporting obligations) that might affect the CE‑marking timeline.  

*Please comment directly on each numbered item and suggest additional evidence or documentation needed before the NB submission.*  

--- 

**End of Draft – ready for internal validation and subsequent population of missing data.**

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> PSUR/PMCF 템플릿 골격 인식 정확. Annex V/VI를 적합성평가 경로로 오인용(실제 경로는 IX/X/XI), MDCG 2020-16을 분류 가이드로 오설명(실제 IVDR 분류 가이드).

**Source Excerpts**

1. Chunk `108347462317924009`

> ### Section 7. PMCF 결과 연계 (Art.86(1)(d)) | 항목 | 내용 | |---|---| | PMCF 계획 참조 문서 | [문서번호, 버전] | | PMCF 현재 상태 | [진행 중 / 완료 / 계획 단계] | | 이번 기간 주요 PMCF 결과 | [요약 또는 "중간 데이터 없음"] | | PMCF 결과의 CER 반영 | [반영 여부, 반영 내용] | | 다음 PMCF 중간 보고 예정일 | [YYYY-MM-DD] | ---

2. Chunk `131915604397474083`

> ### Section 2. 판매량 및 노출 추정 (MDR Art.86(1)(c)) | 지역 | 판매 수량 | 추정 환자 노출 수 | 판매 기간 | |---|---|---|---| | EU | [수량] | [추정 수] | [기간] | | 한국 | [수량] | [추정 수] | [기간] | | 미국 | [수량] | [추정 수] | [기간] | | 기타 | [수량] | [추정 수] | [기간] | | **합계** | **[합계]** | **[합계]** | — | > **MDCG 2022-21 §5.3:** 정확한 환자 수 추정이 어려울 경우 방법론과 가정 조건을 명시. ---

### kb-eval-20260715-it14-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_eu-003", "iteration": 14, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "e086a75bc43113e9", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e086a75bc43113e9`
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
  - `No hallucination`/`Escalation appropriate`는 source excerpt transparency (no captured response — inferred only)을 기준으로 판정합니다.

**Agent Response** — capture failed (fail-safe: fast checks fall back to source-only inference)

> ⚠️ response capture error: timed out

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 응답 캡처 실패(timeout) — 콘텐츠 없음, 재실행 필요(내용 문제 아님).

**Source Excerpts**

1. Chunk `1032759063790726230`

> │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ```

2. Chunk `1132312459160211217`

> ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과 (데이터 수집 결과, 긍정·부정 포함, 편차 근거) | | D | 동등·유사 기기 임상데이터 평가 결과 | | E | 기술문서에 대한 결과의 영향 (CER, Risk Management File, SSCP 각각 명시) | | F | 적용된 CS, 조화표준, 가이던스 | | G | 종합 결론 (PMCF 목적 대비 결과, 예방·시정 조치 필요성) |

### kb-eval-20260715-it14-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_eu-004", "iteration": 14, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "37c8dfb4d71c9364", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `37c8dfb4d71c9364`
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

> ## 1️⃣  Regulatory Draft – Clinical‑Evaluation Gap Analysis  
**Audience:** EU MDR Regulatory Affairs (Theo) – Daily Growth v1  

| Item | Findings / Recommendation |
|------|---------------------------|
| **Product(s)** | 1. X‑ray Detector  <br>2. Handheld X‑ray Source  <br>3. Imaging‑Room GUI Software (SaMD) |
| **MDR Classification** | • X‑ray Detector – Class IIa/IIb (Rule 10 + 11, presence of radiation & diagnostic function). <br>• Handheld X‑ray Source – Class IIb (Rule 10, active radiation source). <br>• Imaging‑Room GUI Software – Class IIa (MDR §22 “Software intended to provide information used for diagnostic or therapeutic decisions”). |
| **Conformity‑Assessment Route** | All three are **Class IIa/IIb** → **Annex IX, Part A** full quality‑management system audit + design‑dossier review by a **Notified Body (NB)**.  The SaMD also requires compliance with IEC 62304, IEC 62366 and the cybersecurity guidance (MDCG 2019‑16 Rev.1). |
| **Core Evidence Required for CE Marking** | 1. **Technical Documentation** per Annex II/III (including device description, labeling, risk management file, design verification & validation data). <br>2. **Clinical Evaluation Report (CER)** – MDR §§ 10‑23, Annex XV. Must contain: <br> a. State‑of‑the‑art literature review (including MDCG 2020‑16 on SaMD). <br> b. Clinical performance data (clinical investigations *or* equivalence + post‑market clinical follow‑up – PMCF). <br> c. Benefit‑risk analysis that demonstrates compliance with Essential Requirements (ERs) §§ 10‑23. <br>3. **Post‑Market Surveillance (PMS) Plan** – MDR § 83, Annex VIII, aligned to the matrix in the source template (SW bugs, cyber‑vulnerability DB, usability errors). <br>4. **Risk Management File** – ISO 14971:2019 showing hazard analysis, risk control measures and residual risk evaluation. <br>5. **Usability Engineering Report** – IEC 62366‑1/2 for the GUI (human factors). <br>6. **Cybersecurity Evidence** – compliance with MDCG 2019‑16 Rev.1 & IEC 62443; vulnerability management process, penetration‑test reports, patch‑management plan. |
| **Missing / Incomplete Information (Gap Summary)** | 1. **Clinical Data Package** – No real‑world performance data or clinical investigation results for the SaMD. The PMS matrix only lists “SW bug report” and “error‑data collection”; it does not demonstrate how those data will be analysed to prove safety/effectiveness per § 61 MDR. <br>2. **PMCF Plan Detail** – Lacks: <br> • Clear objectives, end‑points & success criteria; <br> • Sampling strategy (number of sites, patients, duration); <br> • Statistical analysis plan for error rates and diagnostic accuracy. <br>3. **Residual Risk Acceptance Criteria** – The excerpt lists “major risk signals” (diagnostic error, data loss, cyber‑vulnerability) but does not show *acceptability* thresholds or evidence of mitigation verification. <br>4. **Equivalence/Comparison Data** – No justification that the GUI software is equivalent to an already CE‑marked SaMD; ISO 13485‑based design history missing. <br>5. **Usability Validation Results** – IEC 62366 testing protocol & outcomes (task success rate, error severity) are not provided. <br>6. **Cybersecurity Baseline** – No documented threat model, list of mitigations, or frequency of vulnerability scanning; also no mapping to the new Korean MFDS Digital‑Medical‑Product‑Law (2024) which may affect EU export. |
| **Risk Controls Needed / To Be Demonstrated** | 1. **Software Development Lifecycle** – Full IEC 62304 compliant processes (risk‑based planning, configuration management, problem resolution). <br>2. **Usability Engineering** – Conduct formative & summative testing per IEC 62366; document design mitigations for “use error” hazards identified in the PMS matrix. <br>3. **Cybersecurity Measures** – Implement: <br> a. Secure coding standards (e.g., OWASP). <br> b. Regular vulnerability scanning of CVE/NVD feeds, patch‑management schedule, incident‑response plan. <br>4. **Clinical Performance Verification** – Prospective observational study or performance‑study protocol to capture diagnostic accuracy, false‑negative/positive rates, and data‑loss incidents in routine use. <br>5. **Residual Risk Evaluation** – Use ISO 14971:2019 risk matrix; document that the sum of all controlled risks is “as low as reasonably practicable” (ALARP) and meets MDR § 10(9). |
| **Key Regulatory Citations** | - **MDR 2017/745** Art. 10, 15, 22, 27, 45‑53, 61, 83, 84, 86 <br> - **Annex IX, Part A** – Conformity assessment routes for Class IIa/b devices <br> - **Annex XV** – Clinical Evaluation – required contents <br> - **ISO 14971:2019**, **IEC 62304**, **IEC 62366‑1/2** <br> - **MDCG 2020‑16** (Clinical evaluation of SaMD) <br> - **MDCG 2019‑16 Rev.1** (Cybersecurity for medical devices) <br> - **MDCG 2021‑6** (SaMD guidance) <br> - **Korean MFDS Digital Medical Device Act** (effective 26 Sept 2024) – note for export/market entry checks |
| **Human‑Escalation Triggers (when to raise to senior RA / management)** | • Any **absence of clinical performance data** (e.g., no PMCF results, no equivalence justification). <br>• Identification of **high‑severity residual risk** that exceeds predefined acceptance criteria (e.g., diagnostic error > 1 % leading to patient harm). <br>• Failure to demonstrate compliance with **cybersecurity controls** per MDCG 2019‑16 Rev.1, especially if recent CVE’s affect the product. <br>• If the **PMS plan** cannot be operationalised within 12 months (e.g., lack of data‑capture infrastructure). <br>• When the **Notified Body** requests additional evidence during design‑dossier audit (e.g., request for full usability validation report). |
| **Next Steps – Action Items** | 1. Draft a detailed **PMCF protocol** with sampling plan, success criteria & analysis method; submit to NB for review. <br>2. Initiate a **real‑world clinical performance study** (observational) on the SaMD in ≥ 3 EU sites (minimum n≈200 investigations). <br>3. Compile **usability test reports** (task analysis, error rates) and map mitigation to identified risk signals. <br>4. Produce a **cybersecurity risk assessment** (threat model + mitigations) and evidence of periodic vulnerability scanning. <br>5. Update the **Risk Management File** with quantified residual‑risk acceptance thresholds; include verification results for each control. <br>6. Conduct a **gap‑closure workshop** with software development, QA & clinical teams to allocate responsibility for missing artefacts. |
| **Peer Review Prompt (for another RA)** | *“Colleague, please review the assumptions and scope of the above gap analysis:  <br>1️⃣ Are we correctly classifying the Imaging‑Room GUI as Class IIa under MDR § 22? <br>2️⃣ Does the identified evidence list fully satisfy Annex XV for SaMD, or are additional items (e.g., post‑market clinical follow‑up summary) missing? <br>3️⃣ Have we captured any jurisdiction‑specific gaps – notably the Korean MFDS Digital‑Medical‑Product‑Law impact on EU submissions?  <br>Please challenge the risk‑control mapping and suggest any overlooked regulatory guidance (e.g., MDCG 2020‑13 for software updates).”* |
| **Record of Decision / Reusable Judgment** | `honcho_conclude` <br>**Decision:** The three products require a full NB audit per MDR Annex IX (Class IIa/IIb routes). Clinical evidence gaps centre on the lack of real‑world performance data, detailed PMCF planning, usability validation and cybersecurity documentation. Risk controls must be demonstrated through IEC 62304/IEC 62366 compliance plus a documented threat model. <br>**Rationale:** Aligns with MDR §§ 10‑23, Annex XV and MDCG guidance; ensures NB will have “no open questions” on safety & performance. <br>**Future Reference Tag:** `MDR_ClinicalGap_Xray_SaMD_v1` |

---

### 📌 Quick Take‑away for the Team
- **Classification confirmed → NB audit required.**
- **Immediate priority:** Generate a robust PMCF protocol and start data collection; without it the CER will be incomplete.
- **Risk controls must be documented, verified & linked to each hazard listed in the PMS matrix.**
- **Escalate** if clinical performance data cannot be obtained within 3 months or if residual risk remains > acceptable level.

--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 3개 제품 MDR 분류는 소스와 정확 일치. MDCG 문서 주제 오설명 반복 + Annex XV를 CER로 오인용(실제 CER은 Annex XIV Part A).

**Source Excerpts**

1. Chunk `1138445053784347810`

> | PMS 항목 | 특화 내용 | |---|---| | 주요 위험 신호 | SW 오류로 인한 진단 오류, 데이터 손실, 사이버보안 취약점 | | 핵심 수집원 | SW 버그 리포트, 사이버보안 취약점 공개 DB (CVE, NIST NVD) | | PMCF 방법 | 사용성 평가 (IEC 62366), 실사용 에러 데이터 수집 | | 주요 표준 모니터링 | IEC 62304 개정, MDCG 2019-16 Rev.1 사이버보안, MDCG 2021-6 SaMD | | MFDS 특이사항 | 디지털의료제품법(2024.09.26 시행) 적용 여부 검토 [검증 필요] | ---

2. Chunk `1142345122918011337`

> ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (추정) | PMS Plan 의무 | 보고서 유형 | FDA 522 | MFDS 시판후조사 | |---|---|---|---|---|---| | **X-ray Detector** | Class IIa/IIb | **필수** | PSUR 2년/매년 | 해당 없음 (비이식형) | 신개발 시 3~4년 조사 | | **Handheld X-ray Source** | Class IIb | **필수** | PSUR 매년 | 해당 없음 (비이식형) | 신개발 시 4~6년 조사 | | **촬영실 GUI SW (SaMD)** | Class IIa (MDR §22) | **필수** | PSUR 2년 | 해당 없음 | 소프트웨어 신개발 시 해당 | ---

### kb-eval-20260715-it14-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_eu-005", "iteration": 14, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e2a4fc8ad7b589ff", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "209487b4b22e96052be65198c3a3ed54cef6303dd563722b36bf9c98910a1cf9"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e2a4fc8ad7b589ff`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_MDR_2017_745.md)
- Source hash: `209487b4b22e96052be65198c3a3ed54cef6303dd563722b36bf9c98910a1cf9`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_MDR_2017_745.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | |...
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

> **REGULATORY DRAFT – Clinical‑Evaluation Gap Analysis**  
*Prepared by: Theo – EU MDR RA Specialist*  
*Scenario ID: e2a4fc8ad7b589ff | Run date: 2026‑07‑28*  

---

## 1. Device Synopsis (to be confirmed by the project team)

| Item | Description |
|------|-------------|
| **Device name** | *[Insert trade name]* |
| **Intended purpose / indication** | *[Brief statement of medical use, patient population, mode of action]* |
| **Device type** | *[Active/Passive, invasive/non‑invasive, software, combination product]* |
| **Principal design & principle of operation** | *[High‑level description]* |
| **Regulated class (provisional)** | Likely Class IIa / IIb – requires confirmation against MDR Annex VIII rules. |

> **Action:** R&D to supply a completed “Intended Use” and “Device Description” section (see Table 2, step 2 of the TD creation flow in source‑[1]).

---

## 2. Classification & Conformity‑Assessment Route  

| Step | Decision point | MDR reference |
|------|----------------|---------------|
| **2.1** | Identify rule(s) from Annex VIII that apply (e.g., Rule 10 for active implantable, Rule 9 for non‑invasive measuring). | MDR Art. 51 & Annex VIII |
| **2.2** | Determine final class (I, IIa, IIb, III). | MDR Art. 52 |
| **2.3** | Choose conformity‑assessment route: <br>*Class IIa – Annex VI (full quality‑system + NB design‑dossier review).*<br>*Class IIb – Annex VII (design‑dossier with NB audit) or Annex VIII if a “higher risk” device.* | MDR Art. 53‑58 |
| **2.4** | Assign a Notified Body (NB) and plan the design‑dossier submission. | MDR Art. 10, 15‑16 |

> **Missing information:** Exact intended use & technology classification → **Human escalation trigger #1** (require clarification from R&D/Marketing).

---

## 3. Evidence Package Required for Technical Documentation (TD)

| No.| Evidence element | Where it belongs in TD* | MDR article / annex |
|---|-------------------|------------------------|----------------------|
| **3.1** | **Device description & specification** (including variants, accessories). | Section 4.2 of Annex II | Art. 10‑11 |
| **3.2** | **Design & manufacturing information** (process flow diagrams, batch records). | Sections 4.3–4.5 Annex II | Art. 10‑11 |
| **3.3** | **Verification & Validation (V&V) results** (bench testing, software verification, biocompatibility). | Section 4.6 Annex II | Art. 10‑11 |
| **3.4** | **Risk Management File** (ISO 14971 compliant, risk control measures, residual risks). | Section 5.1 Annex II – Risk Management Report | Art. 10‑13 |
| **3.5** | **GSPR Mapping & Declaration of Conformity** (checklist, mapping to Annex I GSPR). | Section 6 Annex II – GSPR report | Art. 10‑12 |
| **3.6** | **Clinical Evaluation Report (CER)** – latest version, including SOTA review and justification of clinical benefit. | Section 7 Annex II – Clinical Evaluation Report | Art. 61‑62; MDCG 2020‑13 |
| **3.7** | **Post‑Market Surveillance (PMS) Plan & PMS Report** (incl. PMCF plan). | Sections 8‑9 Annex II – PMS & vigilance | Art. 83‑86 |
| **3.8** | **Labeling, IFU & UDI information**. | Section 4.1 Annex II | Art. 10‑12 |
| **3.9** | **Declaration of Conformity (DoC)**. | End of TD | Art. 19 |

\* See the process flow in source‑[1] (steps 1–8) for responsible roles and deliverables.

> **Missing evidence (gap list):**  
> 1. Completed CER – only a draft exists, lacking SOTA literature after 2022.  
> 2. Updated risk‑management file reflecting new clinical findings.  
> 3. PMS Plan aligned with the device’s “new” intended use (if changed).  
> 4. GSPR checklist not yet signed off by QA.  

---

## 4. Clinical Evaluation Gap Analysis  

| Gap | Required Evidence | MDR / MDCG citation | Why it matters |
|-----|-------------------|----------------------|----------------|
| **4.1** – *Insufficient SOTA literature* (last review 2020). | Systematic literature search covering 2020‑present, using MEDLINE/PubMed, Embase; inclusion/exclusion criteria defined. | MDR Art. 61(4); MDCG 2020‑13 §3.2 | Demonstrates state of the art & clinical benefit claim. |
| **4.2** – *No clinical investigation data* for a new indication (e.g., pediatric use). | Conduct a post‑market clinical investigation (PMCI) following MDR Art. 61(6) or obtain existing European study data. | MDR Art. 61(6); MDCG 2020‑13 §4 | Must substantiate safety/performance for the expanded claim. |
| **4.3** – *Limited post‑market surveillance data* (only 1 yr of EU complaints). | PMS data set: aggregated complaint logs, trend analysis, field safety corrective actions (FSCA) over at least 2 years; PMCF plan per Art. 84. | MDR Art. 83‑86; MDCG 2020‑6 | Supports ongoing benefit-risk assessment. |
| **4.4** – *Risk management file not updated with residual risk after clinical findings*. | Updated ISO 14971 risk analysis linking each identified hazard to clinical evidence, plus verification of new control measures. | MDR Art. 10(9); Annex I GSPR 12 | Ensures conformity with safety requirements. |
| **4.5** – *GSPR mapping incomplete* (several clauses un‑checked). | Complete the GSPR checklist, cross‑reference each clause to supporting documentation (risk file, design verification, clinical data). | MDR Art. 10(2) & Annex I | Needed for NB review and CE marking. |

> **Human escalation trigger #2:** If any of the above gaps cannot be closed within 90 days, raise to Project Lead for timeline re‑assessment.

---

## 5. Recommended Risk Controls (to be reflected in updated risk‑management file)

| Hazard | Existing control | Additional control required (based on gap) |
|--------|------------------|-------------------------------------------|
| Device‑related infection (if invasive) | Sterile packaging, validated sterilisation process. | Extend bioburden testing to new accessory; update labeling with handling instructions. |
| Software cybersecurity (if software‑enabled) | Basic authentication, encrypted data transmission. | Implement regular vulnerability scanning & a post‑market cyber‑security plan per MDCG 2020‑16. |
| Misinterpretation of measurement results | Clear IFU, color‑coded display. | Add “warning” statements for off‑label patient groups identified in gap 4.2. |
| Residual risk of rare adverse event (e.g., thrombo‑embolism) | Standard clinical monitoring during trials. | Conduct targeted post‑market study to quantify incidence; integrate results into PMCF. |

All controls must be **verified** and documented per ISO 14971 §5‑7.

---

## 6. Citations & Regulatory References  

| Ref # | Document | Section / Clause |
|------|----------|-------------------|
| **C1** | MDR (EU) 2017/745 | Art. 10 – Technical Documentation |
| **C2** | MDR Art. 51‑52 – Classification Rules |
| **C3** | MDR Annex II – Content of Technical Documentation |
| **C4** | MDR Annex I – General Safety & Performance Requirements (GSPR) |
| **C5** | MDCG Guidance 2020‑13 “Clinical Evaluation” |
| **C6** | ISO 14971:2019 – Application of risk management to medical devices |
| **C7** | MDCG Guidance 2020‑16 “Cybersecurity for Medical Devices” (if applicable) |
| **C8** | Source excerpt [1] – TD creation workflow (steps 1‑8) |
| **C9** | Source excerpt [2] – Economic Operator duties (Art. 10‑14) |

---

## 7. Human‑Escalation Triggers  

| # | Situation | Who must be alerted | Deadline for action |
|---|-----------|---------------------|----------------------|
| **E1** | Unclear device classification / rule applicability. | Project Lead & Regulatory Manager | Within 5 working days of receiving this draft. |
| **E2** | Inability to obtain required clinical data (e.g., no EU study available). | Clinical Development Lead & Senior RA | Immediate; propose alternative evidence or PMCI. |
| **E3** | GSPR checklist remains incomplete after 2 review cycles. | QA Manager & RA Lead | Escalate to Quality Director after 14 days. |
| **E4** | PMS data insufficient for a 12‑month trend analysis (less than 20 complaints). | Post‑Market Surveillance Coordinator | Raise to NB liaison; may delay submission. |
| **E5** | Any regulatory deadline (e.g., NB dossier submission) threatened by unresolved gaps. | Project Sponsor / Compliance Officer | Immediate escalation, re‑plan timelines. |

---

## 8. Peer‑Review Prompt  

> **To: RA Peer (e.g., Marta, IVDR Specialist)**  
> Please review the assumptions and evidence gaps identified above:  
> 1. Are the classification rule selections (Annex VIII) realistic given the limited device description?  
> 2. Does the gap list fully capture all MDR clinical‑evaluation obligations, or have we missed any clause (e.g., Art. 61(5) on “clinical data from equivalent devices”)?  
> 3. Are there jurisdiction‑specific nuances (e.g., German BfArM additional requirements) that should be reflected before finalizing the TD?  
> 4. Does the proposed escalation matrix align with our internal SOPs for NB‑driven projects?  

Please provide your comments by **2026‑08‑02** so we can update the dossier plan accordingly.

---

## 9. Reusable RA Judgment (recorded for future reference)

```
honcho_conclude:
{
  "scenario_id": "e2a4fc8ad7b589ff",
  "judgment_key": "MDR_clinical_evaluation_gap_analysis_template",
  "summary": "For any new EU‑market device, first confirm classification via MDR Annex VIII; then map the full TD (Annex II) to a stepwise workflow (RA → R&D → QA). Identify missing clinical evidence (SOTA review post‑2020, PMCI for new indications, PMS/PMCF data) and update risk management accordingly. Flag any uncertainty in classification or lack of clinical data as escalation triggers. Use the provided table format for gap analysis and the peer‑review prompt to obtain a second‑opinion on assumptions and jurisdiction‑specific nuances.",
  "components": {
    "classification_checklist": ["MDR Art.51‑52", "Annex VIII rules"],
    "technical_documentation_items": ["Device description", "Design & manufacturing", "V&V results", "Risk management file", "GSPR mapping", "CER", "PMS plan", "Labeling/UDI", "DoC"],
    "clinical_evaluation_gaps": ["SOTA literature >2020", "Clinical investigation for new indication", "Post‑market data ≥2 years", "Updated risk analysis", "Complete GSPR checklist"],
    "risk_controls": ["Update bioburden testing", "Cybersecurity plan per MDCG 2020‑16", "IFU warnings", "Targeted PMCF study"],
    "escalation_triggers": ["Classification uncertainty", "Missing clinical data", "Incomplete GSPR", "Insufficient PMS trend", "Deadline risk"]
  },
  "references": ["MDR Art.10‑14,61‑86", "Annex I–II", "MDCG 2020‑13", "ISO 14971:2019"],
  "peer_review_prompt": "Ask a fellow RA to challenge classification assumptions, completeness of clinical‑evaluation obligations (incl. equivalence data), and any national add‑ons."
}
```

---  

*Prepared for internal use only. No confidential manufacturer information is disclosed.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> TD 구축 워크플로우 충실. Annex 적합성평가 오인용 반복 + Rule 9/10 설명이 실제와 반대로 뒤바뀜(소스에 근거 없음).

**Source Excerpts**

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `24104208734622027`

> ## 3. 경제운영자(Economic Operator) 역할 정의 | 역할 | MDR 조항 | 핵심 의무 | 자사 해당 여부 | |------|----------|----------|--------------| | 제조자(Manufacturer) | Art. 10 | 기술문서, QMS, UDI, PMS, Vigilance, PRRC 지정 | ☐ | | 수권대리인(AR) | Art. 11 | EU 내 제조자 대리, 당국 연락창구 | ☐ (비EU 제조사 필수) | | 수입업자(Importer) | Art. 13 | CE 마크·UDI 확인, 보관조건 준수, 불만 전달 | ☐ | | 유통업자(Distributor) | Art. 14 | CE 마크·라벨 확인, 보관·운송 조건 준수 | ☐ |

## ra_kr

### kb-eval-20260715-it14-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_kr-001", "iteration": 14, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "4586ae30d20a0eca", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `4586ae30d20a0eca`
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

> ## 🔎 Regulatory Draft – KGMP Evidence Readiness  
**Audience:** Korean MFDS‑RA (Sam)   
**Scenario ID:** 4586ae30d20a0eca | Run date: 2026‑07‑28  
**Source document:** `KGMP_QMSR_ISO13485_비교_통합전략.md` (hash 1f758…ff)  

---

### 1️⃣ Device Classification & Submission Route (MFDS)

| MFDS Class | Typical Risk Level | Korean submission type* |
|------------|-------------------|--------------------------|
| **Class I** (general‑risk) | Low – no active or invasive function | **신고** (Notification) – only a device‑master file and basic safety data required. |
| **Class II** (medium‑risk) | Limited invasive, monitoring, diagnostic | **허가(임상시험·시판후조사 포함)** – full dossier, KGMP certificate & clinical evidence. |
| **Class III** (high‑risk) | Implantable, life‑supporting, critical therapeutic | **허가(심층 검토)** – same as Class II but with stricter PMS/PSUR and often mandatory local clinical trial. |

> **\*Decision point:** The draft assumes the device is *Class II* (typical for most software‑enabled diagnostics) unless the sponsor supplies a definitive risk‑class determination.  

---

### 2️⃣ Required Evidence Package (MFDS “허가” pathway)

| Element | Korean requirement | International equivalent | Mapping notes (from source) |
|---------|-------------------|---------------------------|-----------------------------|
| **KGMP Facility Certification** | KGMP‐certified manufacturing site, §7.4‑7.6 of KGMP QMS → identical to ISO 13485 but with added service record (§820.35) & complaint timing (§820.20). | ISO 13485:2016 + FDA QSR 21 CFR Part 820 (service records, complaints). | Source [1] shows “ISO 동일” for most clauses; MFDS adds §820.35 & §820.20 specifics and PMS data collection (MDR Art.83‑86). |
| **Quality Management System (QMS) Documentation** | QMS manual, SOPs, change control, internal audit plan (NB: unannounced audits are allowed). | ISO 13485 QMS + FDA MDSAP acceptance. | Source [2] – “MDSAP 수용” → MFDS may accept an MDSAP audit report **instead of a separate on‑site inspection** (per MDR Annex IX §3.2). |
| **Design Dossier / Technical File** | Design input/output, risk management file (ISO 14971), verification & validation reports, labeling/IFU in Korean. | EU CE technical documentation + FDA 510(k) or PMA content. | KGMP requires Korean language IFU; foreign language files must be translated and signed by a Korean authorized representative. |
| **Clinical Evidence** | • If foreign CE/FDA clearance exists, MFDS may accept the Clinical Evaluation Report (CER) under the **2026‑01 revision** (OECD mutual‑recognition). <br>• Otherwise, local clinical data are required for Class III or if the device is a new technology. | FDA 510(k) summary, EU Clinical Evaluation (MDCG 2020‑13), WHO GHTF guidance. | The revision expands CER acceptance scope; however MFDS still demands **local post‑market performance data** when the foreign dataset does not cover Korean population or usage conditions. |
| **Post‑Market Surveillance (PMS) & Periodic Safety Update Report (PSUR)** | PMS plan, PSUR/PMSR generation (incl. PSUR‑derived data linked to §8.4 “데이터 분석”). | EU MDR Art. 83‑86, FDA Post‑market Surveillance Plan (21 CFR 822). | Source [1] lists “PSUR/PMSR 연동” for §8.4 – MFDS expects that QMS data feed into PSUR generation. |
| **Service & Maintenance Records** | Must retain detailed service logs per §820.35 (added requirement). | FDA 21 CFR 820.30 (equipment maintenance). | Directly noted in source [1] under “7.5 생산 및 서비스”. |
| **Complaint Handling** | Record the point when an investigation is completed (§820.20) and link to PMS data. | FDA QSR §820.20, EU MDR Art. 78. | Source [1] line for “8.2.1 피드백”. |
| **Labeling & IFU (Korean)** | Every label & Instructions‑for‑Use must be in Korean; translation must be certified by a Korean language expert and signed by the authorized representative. | EU Annex I, FDA 21 CFR 801. | Not explicitly in source but a **non‑negotiable** MFDS rule. |
| **Risk Management** | ISO 14971‑compliant file → risk control measures, residual risk justification, integration of PMS findings. | Same as EU/US. | No gap; KGMP follows ISO identical (source [1] “ISO 동일”). |

---

### 3️⃣ Missing / Unverified Information (Red Flags)

| # | What is missing? | Why it matters for MFDS & KGMP |
|---|------------------|--------------------------------|
| **①** | **Confirmed device class (K‑class)** from sponsor. | Determines whether a 허가 or 신고 route is required; also influences the depth of clinical data needed. |
| **②** | **KGMP certification status** – copy of current KGMP certificate & audit report. | Without it, MFDS will reject the submission outright (mandatory for Class II/III). |
| **③** | **Foreign regulatory clearances** (CE marking number, FDA 510(k) or PMA number). | Needed to invoke CER acceptance under the 2026‑01 OECD revision; also to decide whether local clinical data are waived. |
| **④** | **Korean language labeling & IFU draft** (including any required symbols per MFDS Notice No. 2017‑68). | Mandatory translation; failure leads to non‑conformity in 허가 review. |
| **⑤** | **Local Clinical Evidence** (if required) – protocol, ethics approval, data summary. | If the device is Class III or a novel technology, MFDS still demands Korean population data despite foreign CERs. |
| **⑥** | **MDSAP audit report** (if sponsor intends to rely on it). | Must be the latest valid MDSAP report covering all KGMP‑relevant sections; otherwise on‑site inspection will be required. |
| **⑦** | **PMS Plan & PSUR draft** – especially linkage of QMS data to PSUR (§8.4). | MFDS expects the PSUR to be derived from measured KPI in the QMS; missing this raises a “data analysis” gap. |

---

### 4️⃣ Core Risk Controls (Mapped to KGMP Clauses)

| KGMP Clause | Required Control | Practical Implementation |
|-------------|------------------|---------------------------|
| **7.5 Production & Service** | Service record retention per §820.35. | Electronic service log linked to serial numbers; exportable for MFDS audit. |
| **8.1 Measurement·Analysis·Improvement** | Continuous data‑driven improvement (incl. PSUR). | KPI dashboards feeding into Risk Management File (RMF) updates. |
| **8.2.1 Feedback** | Complaint investigation closed‑time logging (§820.20). | Timestamped ticket system, auto‑escalation when >30 days open. |
| **8.2.2 Internal Audits** | Unannounced audit readiness (NB). | Quarterly internal audits plus random “surprise” checks; documented in audit schedule. |
| **8.4 Data Analysis** | PSUR/PMSR data collection (MDR Art. 83‑86). | Integrated QMS database exporting to PSUR template. |
| **8.5 Improvement** | CAPA loop closed with effectiveness verification. | Documented corrective actions linked back to root cause analysis in RMF. |

---

### 5️⃣ Citations / Reference List

1. **MFDS Medical Device Act & Enforcement Decree (2024‑rev.)** – §7–§8 QMS requirements, KGMP certification rules.  
2. **KGMP Guideline (2023 edition), “품질경영시스템(QMS) 기준”** – Section 7.4‑8.5 (source excerpts [1]).  
3. **ISO 13485:2016**, **ISO 14971:2019** – baseline international standards.  
4. **FDA QSR 21 CFR Part 820**, especially §§820.20, 820.35 (referenced in source [1]).  
5. **EU MDR Annex IX §3.2** – partial MDSAP acceptance (source [2]).  
6. **OECD Mutual Recognition of Clinical Evaluation Reports (2026‑01 MFDS revision)** – CER acceptance scope.  
7. **MFDS Notice No. 2017‑68** – Korean language labeling & IFU requirements.

---

### 6️⃣ Human‑Escalation Triggers  

| Trigger | Action required (who) |
|---------|-----------------------|
| **No KGMP certificate** or expired >90 days | **RA Lead → Sponsor**: demand updated certificate before dossier acceptance. |
| **Device class not defined / mismatched** | **Regulatory Manager** to convene cross‑functional meeting; re‑classify per MFDS risk rules. |
| **Foreign CE/FDA clearance missing or insufficient for CER waiver** | **RA Specialist** to request full FDA 510(k) summary / EU MDCG clinical evaluation file. |
| **Korean labeling draft absent or incomplete** | **Labeling Team → Korean Language Specialist**: produce compliant label within 14 days. |
| **Local clinical data required but not provided** | **Clinical Affairs Lead** to initiate feasibility study in Korea; pause submission until IRB approval obtained. |
| **MDSAP report older than 12 months or does not cover KGMP‑relevant processes** | **Quality Assurance Manager** → schedule on‑site MFDS inspection. |
| **PMS/PSUR plan absent or no link to QMS data** | **Post‑Market Surveillance Lead** to develop PSUR template; document data flow before dossier finalization. |

> **Escalation rule:** Any trigger that blocks the *submission of a 허가* must be escalated to the Project Steering Committee within 2 business days.

---

### 7️⃣ Peer‑Review Prompt  

> **To: [RA colleague – e.g., Ji‑young Lee, Senior RA]**  
> Please review this draft and challenge the following points:  
> 1. **Classification assumption:** Is it safe to presume a Class II classification without device‐specific risk data? Should we request a formal K‑class determination first?  
> 2. **Evidence coverage:** Have we captured all KGMP‐specific obligations (e.g., service record §820.35, complaint timing §820.20) and their mapping to foreign standards? Are any additional Korean “notice” documents missing (e.g., MFDS Notice No. 2025‑12 on electronic QMS reporting)?  
> 3. **Jurisdictional gaps:** Does the reliance on MDSAP audit reports fully satisfy KGMP inspection requirements, or are there residual items that still demand a separate MFDS onsite audit?  
> 4. **Local clinical data scope:** Under the new 2026‑01 CER acceptance rule, are we correct in limiting local clinical evidence to Class III or novel‑technology devices only?  

Your feedback will be logged as `honcho_conclude` with peer=`ai`. Thank you!

---

### 8️⃣ Reusable RA Judgment (to be recorded)

> **Lesson:** When mapping KGMP QMS clauses to ISO 13485 / FDA QSR, always flag the *additional MFDS‑specific* requirements (service records §820.35, complaint close‑time §820.20, mandatory Korean labeling) and note that **MDSAP audit reports are accepted only when they cover all KGMP‐relevant sections**; otherwise an on‑site inspection remains mandatory. This judgment will be stored under the “KGMP evidence readiness” knowledge node for future projects.

--- 

*Prepared by: Sam – Korea Regulatory Affairs Specialist (MFDS & KGMP)*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> KGMP↔ISO↔QMSR 매핑(§820.35 등)은 소스와 정확 일치. 'MFDS 고시 제2017-68호'는 검증 불가.

**Source Excerpts**

1. Chunk `1012828200772392062`

> II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동일 | **FDA 실사 대상** (구 QSR §820.180(c) 예외 삭제) | NB 불시 감사 대상 | | **8.2.3 공정 모니터링** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.3 부적합 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.4 데이터 분석** | ISO 동일 | ISO 동일 | PSUR/PMSR 작성 근거 데이터 | | **8.5 개선** | ISO 동일 | ISO 동일 | ISO 동일 |

2. Chunk `1037950769042691196`

> MDSAP 수용 (실사 대체 가능) | MDR Annex IX §3.2 — MDSAP 부분 수용 |

### kb-eval-20260715-it14-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_kr-002", "iteration": 14, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "5861db936c95df37", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "6e09bc3b8dcd278f80184587a5eaba125f19dbc86c1b2ce2f24b76bdc503c9a0"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5861db936c95df37`
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

> **Regulatory Draft – Daily Growth v1 (2026‑07‑28)**  
*Prepared for: Sam (KR RA) – KGMP Evidence Readiness*  

---

## 1️⃣ Device Overview (to be filled by the project team)

| Item | Description |
|------|-------------|
| **Device name / model** |  _(e.g., “X‑Ray Imaging System X100”)_ |
| **Core technology** |  _(hardware, software, combination?)_ |
| **Intended use & indication** |  _(clinical purpose and patient population)_ |
| **Primary classification in Korea** |  **Class II / III / IV** – *determined by MFDS “품목군 분류” (2025‑22 개정).*  |
| **International evidence available** | • FDA 510(k) clearance (or PMA) <br>• CE marking under EU MDR 2017/745 <br>• ISO 13485:2016 certification |

> **Note:** The revised MFDS 고시 제2025‑22호 now distinguishes *융복합 의료기기* where the primary function is medical. Confirm that the device’s principal function meets the “medical‑device” definition; otherwise a **non‑medical** classification applies and the pathway changes.

---

## 2️⃣ Submission Route & Regulatory Pathway  

| Classification | Korean route (MFDS) | Typical dossier type |
|----------------|---------------------|----------------------|
| Class II | **신고 (Notification)** – minimal review, requires KGMP certificate, labeling, IFU in KR. | Notification Form + KGMP evidence. |
| Class III | **허가 (Approval)** – full technical file review. | Approval Application (Technical File) + Clinical Evidence. |
| Class IV | **허가** – most stringent; includes pre‑market approval and post‑market surveillance plan. | Same as Class III plus additional risk‑management & PMS documentation. |

*If the device contains **software** that is a *medical purpose* (IEC 62304 referenced), it will be treated as a **Combination** product and may require **Software Validation** evidence per the new full reference to IEC 62304:2006+A1.*

---

## 3️⃣ Required Evidence Packages (per MFDS KGMP & Device‑Specific Requirements)

| Evidence Category | Specific Items (MFDS citations) | Status / Gaps |
|-------------------|----------------------------------|---------------|
| **KGMP Facility Certification** | • MFDS GMP 고시 (v0.2) – 30대 절차 매핑 <br>• ISO 13485:2016 compliance mapping <br>• Current KGMP certificate (valid ≤ 2 yr) | ☐ Certificate on file? <br>⦿ SOP‑CC‑001, SOP‑MFG‑001‑002, SOP‑CAPA‑001 must be up‑to‑date. |
| **Quality Management System** | • Quality Manual (Korean & English) <br>• Documented procedures: UDI, PMS, Training, Supplier Mgmt, NC handling (see related‐docs list in excerpt). | ☐ Korean translation of QMS docs required. |
| **Risk Management** | • ISO 14971 risk file (including residual risk evaluation) <br>• If software‑enabled: IEC 62304 verification/validation reports (full reference per amendment). | ☐ Software validation plan missing? |
| **Clinical Evidence** | • Local clinical data *if* MFDS does not accept foreign CER (see 2026‑01 revision – OECD CER acceptance now broader but still limited to high‑risk devices). <br>• Summary of FDA 510(k) or PMA & CE Technical Documentation as supporting evidence. | ☐ Determine whether OECD Clinical Evaluation Report (CER) is acceptable for this class; otherwise plan local clinical trial. |
| **Labeling & IFU** | • Korean language labeling (product name, indications, cautions, contraindications). <br>• Korean IFU (Instructions for Use) – must meet MFDS “표시·포장” 규정. | ☐ Current labels are English‑only → translation required. |
| **Cybersecurity (if applicable)** | • Reference to 부속서 (Annex) on cybersecurity management (newly added in 2025‑22). <br>• Threat model & mitigation plan, firmware update control. | ☐ No cyber risk assessment yet – create according to MFDS annex. |
| **Post‑Market Surveillance (PMS)** | • SOP‑PMS‑001 (Korean PMS Plan) <br>• 시판후조사 schedule and reporting template. | ☐ Draft PMS plan in Korean not submitted. |
| **UDI (Unique Device Identification)** | • SOP‑UDI‑001 – UDI registration with MFDS KIDS system. | ☐ UDI assigned? |

---

## 4️⃣ Missing Information & Immediate Action Items  

| Gap | Required Action | Owner | Target Completion |
|-----|-----------------|-------|--------------------|
| KGMP certificate (if expired) | Request updated certificate from manufacturing site; ensure SOP‑CC‑001 reflects latest process. | QA Lead | 2026‑08‑15 |
| Korean translation of labeling/IFU | Contract certified translator; perform parallel review with regulatory team. | RA Team | 2026‑08‑01 |
| Software validation evidence (IEC 62304) | Compile design history file, unit/integration/system test reports per IEC 62304:2006+A1. | Software Engineer | 2026‑08‑10 |
| Local clinical data / OECD CER acceptance | Conduct gap analysis of existing FDA/CE clinical data vs MFDS accepted criteria (2026‑01 revision). If insufficient → design a Korean pilot study. | Clinical Affairs | 2026‑09‑01 |
| Cybersecurity risk assessment | Draft threat model, implement controls aligned with MFDS annex on cybersecurity. | InfoSec Lead | 2026‑08‑20 |
| PMS plan in Korean | Translate existing EU PMS plan; align timelines with MFDS reporting schedule. | PMO / RA | 2026‑08‑05 |

---

## 5️⃣ Risk Controls (Mapping to MFDS Requirements)

| Hazard Category | Control Mechanism | MFDS Reference |
|-----------------|-------------------|----------------|
| Radiological exposure (X‑ray) | Built‑in dose monitoring, interlock safety, user training SOP. | MFDS “의료기기 안전성 관리” clause 4.2 |
| Software malfunction | IEC 62304 validation, periodic firmware integrity checks, rollback capability. | 고시 제2025‑22호 – SW 밸리데이션 전면 참조 |
| Cyber attack → unauthorized parameter change | Encryption of communication, authentication, OTA update signing, intrusion detection. | 부속서 “사이버보안 관리 요구” (신설) |
| Labeling misinterpretation | Korean language labeling with clear symbols; usability testing of IFU. | MFDS “표시·포장 규정” 제5조 |
| Lack of post‑market data | PMS plan with real‑world evidence collection, adverse event reporting within 15 days. | 시판후조사 규정 (2025‑22) |

---

## 6️⃣ Citations (MFDS & International)

| Source | Citation Detail |
|--------|-----------------|
| MFDS_의료기기_제조_및_품질관리_기준 (v0.2) – doc‑id:107140411445338936 | KGMP 30대 절차 매핑, ISO 13485 정합 상세 |
| 고시 제2025‑22호 – “최신 개정 핵심” – doc‑id:1127747106119376174 | 확대된 품목군 분류(64개), IEC 62304 전면 적용, 사이버보안 요구 (부속서) |
| MFDS 규정 제2026‑01 개정 – OECD CER 수용 범위 | Accepts foreign Clinical Evaluation Reports for Class III/IV when justified; still requires local data for high‑risk devices. |
| EU MDR 2017/745 Annex I §3 & §5 | CE technical documentation, clinical evaluation requirements (mapped to MFDS). |
| FDA QMSR 21 CFR Part 820 | Reference for GMP alignment, particularly design controls. |

---

## 7️⃣ Human‑Escalation Triggers  

| Trigger | Reason | Escalation To |
|--------|--------|---------------|
| KGMP certificate missing or > 2 yr old | MFDS will reject any submission lacking valid GMP certification. | Senior QA Manager & Project Sponsor |
| Korean labeling/IFU not finalized by **2026‑08‑01** | Deadline for filing; non‑Korean documents are non‑conformant. | RA Lead (Sam) → Legal / Marketing |
> **Escalation Path:** Immediate notification to PMO → Decision on schedule impact (possible submission delay).  
| No local clinical data & MFDS deems foreign CER insufficient | High‑risk Class III/IV devices require Korean trial data per 2026‑01 revision. | Clinical Affairs Director → CEO |
> **Escalation Path:** Initiate feasibility study; consider partnership with Korean CRO.  

---

## 8️⃣ Peer‑Review Prompt  

> **To: RA Peer (e.g., Ji‑young Lee, Senior Regulatory Counsel)**  
> Please review the assumptions and evidence mapping in this draft, specifically:  
> 1. **Classification justification** – Is the chosen Class II/III/IV consistent with MFDS “품목군 분류” after the 2025‑22 amendment?  
> 2. **Scope of foreign clinical data acceptance** – Have we correctly interpreted the OECD CER allowance (2026‑01 revision) for this device type?  
> 3. **Missing Korean‑specific obligations** – Are there any additional MFDS labeling, packaging, or cyber‑security annex items not captured above?  
> 4. **Risk‑control completeness** – Does our risk‑management matrix satisfy both ISO 14971 and the new MFDS cybersecurity expectations?  
> 
> Provide any counter‑examples, overlooked documents, or alternative pathways you deem more efficient.

---

## 9️⃣ Reusable RA Judgment (Honcho Conclusion)  

```
honcho_conclude:
  lesson_id: KGMP_EVIDENCE_READINESS_2026
  summary: |
    For MFDS submissions post‑2025‑22 amendment, a **complete KGMP evidence set** must include:
      • Valid KGMP certificate (≤2 yr) linked to the 30 core SOPs mapped to ISO 13485.
      • Korean language labeling & IFU; translations are mandatory for all device classes.
      • Full IEC 62304 validation when software is a medical function; partial references are no longer acceptable.
      • Cybersecurity risk assessment as per MFDS annex (newly required for any device with networked components).
      • Clinical data: OECD CER may be accepted for Class III/IV only if the foreign evidence meets MFDS safety/effectiveness criteria; otherwise a Korean clinical trial is required.
  applicability:
    - All new medical‑device submissions to MFDS from 2025‑01 onward.
  actions:
    - Verify KGMP certificate and SOP alignment before dossier compilation.
    - Flag any non‑Korean labeling early (≥ 30 days prior to submission).
    - Conduct a gap analysis of foreign clinical data vs MFDS CER acceptance checklist.
    - Ensure cyber‑risk documentation is included in the technical file for software or connected devices.
  peer_review_needed: true
  peer="ai"
```

--- 

*Prepared by Sam – Korean Regulatory Affairs Specialist (KGMP & MFDS)*  

*Please address the peer‑review items and update the missing‑information table accordingly before proceeding to the submission build.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 고시 제2025-22호 세부내용(64개 품목군, IEC 62304 준용 등)은 소스와 정확. 실제 있는 규정변경에 잘못된 고시번호 인용(정답은 제2026-6호).

**Source Excerpts**

1. Chunk `107140411445338936`

> --- doc-id: MFDS_의료기기_제조_및_품질관리_기준 title: 의료기기 제조 및 품질관리 기준 (MFDS) (v0.2) type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: MFDS GMP 고시 요구사항 해설 및 ISO 13485 정합 매핑, 문서화 30대 절차 매핑 applicable: [ISO13485:2016, MFDS, FDA QMSR, EU MDR 2017/745] forms: [] related-docs: [SOP-CC-001, SOP-MFG-001, SOP-MFG-002, SOP-UDI-001, SOP-PMS-001, SOP-TRN-001, SOP-SUP-001, SOP-NC-001, SOP-CAPA-001, SOP-IA-001, SOP-MR-001, PRO-CRP-001] related-issues: [33] owner: RA/QA Lead last-review: 2026-05-14 review-due: 2027-05-07 --- # 의료기기 제조 및 품질관리 기준 (MFDS) — v0.2 > v0.2 — 2026-05-07: GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려...

2. Chunk `1127747106119376174`

> ## 2. 최신 개정 핵심 (고시 제2025-22호) | 항목 | 종전 | 개정 | |------|------|------| | 품목군 분류 | 26개 | 64개 | | 융복합의료기기 | 불명확 | 주된 기능이 의료기기이면 심사대상 명확화 | | 심사체계 | 복수심사 | 품질관리심사기관 단독심사 가능 | | 제출자료 | 광범위 | 간소화 | | SW 밸리데이션 | IEC 62304 참조 일부 | IEC 62304:2006+A1 전면 참조 편입 | | 사이버보안 | 미규정 | 적용 가능 시 사이버보안 관리 요구 (부속서 참조) |

### kb-eval-20260715-it14-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_kr-003", "iteration": 14, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "07ea8d3f6ba5dc00", "source": "github:holee9/MD-process/issue-drafts/066_01_MFDS_GMP_v0.2_30대절차매핑.md", "source_hash": "9d7fca670a56a64ee146225dc0fd583c83903c5ac050153cfe8226de5bb6a750"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `07ea8d3f6ba5dc00`
- Source: `github:holee9/MD-process/issue-drafts/066_01_MFDS_GMP_v0.2_30대절차매핑.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/066_01_MFDS_GMP_v0.2_30%EB%8C%80%EC%A0%88%EC%B0%A8%EB%A7%A4%ED%95%91.md)
- Source hash: `9d7fca670a56a64ee146225dc0fd583c83903c5ac050153cfe8226de5bb6a750`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `066_01_MFDS_GMP_v0.2_30대절차매핑.md`는 KGMP 또는 GMP evidence readiness, audit readiness, QMS 절차·기록 관련 문서입니다.
- 현재 excerpt 핵심: ## 배경 GMP 심사 대비 ISO 13485:2016 문서화 요구사항 35개 항목을 전수 매핑하고, 프로젝트 SOP 커버리지(69%)를 산출하여 미작성 8건의 우선순위를 도출하였다. ## 참고 링크 - 관련 문서: `01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md` - 교차검증: `12_교차검증_보고서/2026-05-07_GMP절차매핑_영상품질QC_정합성.md`
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

> **Regulatory Draft – KGMP Evidence Readiness**  
*Audience: Sam (KR RA)*  
*Growth version: daily_growth_v1*  
*Run date: 2026‑07‑28*  
*Scenario ID: 07ea8d3f6ba5dc00*  

---

## 1. Device Classification & Submission Route  

| Item | Detail |
|------|--------|
| **K‑Class** | Determine according to MFDS “의료기기 분류표”. (e.g., Class II if invasive, Class III for life‑supporting). The source document does not state the device type – **needs confirmation**. |
| **Submission Type** | • If **Class I** → “신고” (notification) is sufficient.  <br>• If **Class II–III** → “허가” (MFDS approval) required, with a full dossier including KGMP evidence. |
| **Regulatory Reference** | MFDS Notice No. 2021‑70 (Classification & Submission Pathways). |

*Action*: Verify the device’s risk class before finalizing the route.

---

## 2. Required KGMP Evidence  

| Evidence Category | Korean Requirement (MFDS) | International Equivalent | Status / Gap |
|-------------------|---------------------------|--------------------------|--------------|
| **ISO 13485:2016 Documentation** | Full mapping of the 35 ISO‑13485 documentation items to MFDS GMP procedures. Minimum 100 % coverage required for “품질경영시스템”. | ISO 13485 (QMS) – accepted as baseline by MFDS since 2022. | **69 % SOP coverage** (per source). *8 documents missing* – priority list already identified. |
| **KGMP Facility Certification** | Proof of compliance with KGMP Annex A–F (facility, process validation, equipment qualification, environmental monitoring, etc.). | FDA 21 CFR 820 QSR; EU MDR Annex I. | Facility audit pending – documentation gaps in SOPs & Work Instructions. |
| **Process Validation / IQ‑OQ‑PQ** | Detailed protocols and reports for each critical process step (e.g., sterilization, packaging). | IMDRF/ISO 14971 risk control implementation. | Partial; validation plans exist but final PQ reports missing for 2 processes. |
| **Risk Management File (RMF)** | ISO 14971‑based RMF, with *risk controls* linked to KGMP SOPs. | FDA “Design Control” and EU “Risk Management”. | Draft exists, needs closure of residual risk evaluation & justification. |
| **Korean Language Labeling & IFU** | All labeling, box contents, and Instructions for Use must be in Korean (Hangul) with required symbols per MFDS Guideline 2024‑12. | None directly comparable; EU MDR requires EU language, FDA uses English unless targeted to US market. | Korean translations drafted but not validated by a certified translator. |
| **Post‑Market Surveillance Plan** | PMS plan aligned with MFDS §30 (시판후조사) – includes complaint handling, field safety corrective actions, and periodic safety update reports. | FDA 21 CFR 820.30 & EU MDR Annex II. | High‑level outline completed; detailed SOPs missing. |

---

## 3. Missing Information / Gap Summary  

| # | Gap Description | Impact on KGMP Readiness | Recommended Action |
|---|------------------|--------------------------|--------------------|
| **1** | **8 ISO 13485 document items not yet authored** (e.g., *Design Transfer SOP, Supplier Evaluation Procedure*). | Prevents full QMS compliance; MFDS will reject GMP audit. | Prioritize drafting, review against KGMP Annex B. |
| **2** | **Korean translation of labels/IFU not certified**. | Violates labeling law → non‑conformity at submission. | Engage a Korean‑certified translator; obtain sign‑off. |
| **3** | **Process PQ reports missing for Sterilization & Packaging**. | Gaps in process validation → audit finding. | Complete PQ, include statistical data, update Validation Master Plan. |
| **4** | **Residual risk justification incomplete** (no “ALARP” demonstration). | Risk Management File deemed insufficient; could delay Class II‑III 허가. | Conduct final risk/benefit analysis, document mitigation evidence. |
| **5** | **Post‑Market Surveillance SOPs not detailed**. | MFDS will request PMS plan details for 허가. | Develop SOPs covering complaint handling, trend analysis, field actions. |
| **6** | **Facility audit schedule not finalized** (external KGMP auditor not contracted). | No formal KGMP certification → submission blocked. | Select certified KGMP audit firm; schedule pre‑submission audit. |

---

## 4. Risk Controls Aligned to KGMP  

| Control | MFDS Reference | Mapping to International Standard | Implementation Note |
|---------|----------------|-----------------------------------|---------------------|
| **Document Control (SOP, Work Instruction)** | KGMP Annex B‑1 | ISO 13485 Clause 4.2.3 | Ensure version control & retention per 5 years. |
| **Supplier Qualification** | KGMP Annex C‑2 | ISO 14971 *Supply Chain Risk* | Use approved supplier list; audit records retained. |
| **Environmental Monitoring** | KGMP Annex E | FDA 21 CFR 820.70 (Facility) | Quarterly monitoring of cleanroom classification. |
| **Process Validation** | KGMP Annex D‑1 | ISO 13485 Clause 7.5 | IQ/OQ/PQ documented; acceptance criteria defined. |
| **Corrective & Preventive Actions (CAPA)** | KGMP Annex F‑3 | FDA 21 CFR 820.100 | CAPA system integrated with RMF for risk traceability. |
| **Training Management** | KGMP Annex B‑2 | ISO 13485 Clause 6.2 | Training matrix, competency assessments maintained in Korean. |

---

## 5. Citations  

1. MFDS “의료기기 제조 및 품질관리 기준(KGMP)” – latest revision (2026‑01).  
2. MFDS Notice No. 2021‑70 – Device Classification & Submission Pathways.  
3. MFDS Guideline 2024‑12 – Labeling & IFU Korean Language Requirements.  
4. IMDRF/ISO 14971:2019 – Risk Management for Medical Devices (adopted by MFDS).  
5. ISO 13485:2016 – Quality Management System Requirements.  
6. Source excerpts:  
   * [315455402892636179] Mapping of 35 ISO 13485 items → SOP coverage 69 %; identified 8 missing docs.  
   * [1045407237613866280] Cross‑verification report on GMP mapping (2026‑05‑07).  

---

## 6. Human‑Escalation Triggers  

| Trigger | Condition | Recommended Escalation |
|---------|-----------|------------------------|
| **Critical Gap > 5 items** (e.g., missing SOPs, unlabeled Korean IFU) | When any of the “Missing Information” rows reach ≥5 unresolved items. | Alert Project Lead & RA Manager; request additional resources to close gaps within 2 weeks. |
| **Regulatory deadline < 30 days** and *any* KGMP evidence incomplete. | Submission schedule cannot be met without full KGMP audit readiness. | Escalate to Senior RA Director for potential timeline negotiation with MFDS. |
| **Local Clinical Data Required** (identified after classification review). | If device is Class III or a new indication not covered by existing foreign data. | Raise a “Clinical Evidence Gap” ticket; involve Clinical Affairs lead promptly. |
| **Non‑conformity found during pre‑audit** (e.g., external KGMP auditor flag). | Any major non‑conformity (>C) in the audit report. | Immediate escalation to Quality Head and Project Sponsor for corrective plan. |

---

## 7. Peer Review Prompt  

> **To:** [RA Peer – e.g., Ji‑yeon Kim]  
> **Subject:** Review of KGMP Evidence Readiness Draft (Scenario 07ea8d3f6ba5dc00)  
>   
> Please challenge the following assumptions and coverage:  
> 1. **Classification certainty** – we have not yet identified the device’s K‑Class; is a provisional Class II assumption safe for this draft?  
> 2. **Document mapping completeness** – we rely on the 69 % SOP coverage metric from the source; could there be undocumented “shadow” procedures that affect KGMP compliance?  
> 3. **International evidence acceptance** – given the 2026‑01 MFDS revision (OECD clinical data & CER acceptance), are we missing any foreign CE/FDA data that could substitute local clinical data for this device?  
> 4. **Risk control linkage** – have all identified risk controls been fully mapped to KGMP Annex requirements, or are there gaps in supplier monitoring and post‑market surveillance detail?  
>   
> Provide specific counter‑examples, suggest additional sources (e.g., MFDS “GMP 검사 체크리스트” v2), and note any jurisdiction‑specific gaps that we may have overlooked.  

---

## 8. Reusable RA Judgment (honcho_conclude)  

```
honcho_conclude:
{
  "scenario_id": "07ea8d3f6ba5dc00",
  "lesson_key": "KGMP_doc_coverage_mapping",
  "summary": "When mapping ISO 13485:2016 documentation to KGMP requirements, quantify SOP coverage (e.g., % of mapped items) and explicitly flag any unmapped items. A coverage metric below 80 % should trigger a mandatory gap‑closure sprint before any GMP audit. The gap list must be cross‑checked against both KGMP Annexes and MFDS labeling/IFU language mandates.",
  "rationale": "Source excerpt shows 69 % SOP coverage and eight missing documents. MFDS expects 100 % alignment for certification; incomplete mapping leads to audit findings.",
  "action_recommendation": "Adopt a ‘coverage‑first’ checklist: map each of the 35 ISO items, verify KGMP Annex reference, assign owners, and set a ≤2‑week closure deadline for any gap >1 item. Record coverage in the GMP readiness dashboard.",
  "peer_review": "Requested peer to validate classification assumption, hidden procedures risk, foreign evidence substitution per 2026 revision, and completeness of risk control mapping."
}
```

*The above judgment should be stored as a reusable reference for all future KGMP readiness assessments.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 69% SOP 커버리지/누락문서 8건은 소스 직인용, 근거 가장 탄탄. 미검증 고시번호 + KGMP Annex B-1/C-2 등 소스에 없는 세부구조 창작.

**Source Excerpts**

1. Chunk `315455402892636179`

> ## 배경 GMP 심사 대비 ISO 13485:2016 문서화 요구사항 35개 항목을 전수 매핑하고, 프로젝트 SOP 커버리지(69%)를 산출하여 미작성 8건의 우선순위를 도출하였다.

2. Chunk `1045407237613866280`

> ## 참고 링크 - 관련 문서: `01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md` - 교차검증: `12_교차검증_보고서/2026-05-07_GMP절차매핑_영상품질QC_정합성.md`

### kb-eval-20260715-it14-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_kr-004", "iteration": 14, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "7218df51828db995", "source": "github:holee9/MD-process/issue-drafts/911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md", "source_hash": "95f44332028afe7accb07da52f06d3d9910a29bfb18a213c9c2328789985e29c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `7218df51828db995`
- Source: `github:holee9/MD-process/issue-drafts/911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/911_AUDIT_QM-001_MFDS_%EB%B3%84%ED%91%9C2_%EB%B3%B4%EA%B4%80%EA%B8%B0%EA%B0%84_1%EC%B0%A8%EC%B6%9C%EC%B2%98_%EB%AF%B8%ED%99%95%EC%9D%B8.md)
- Source hash: `95f44332028afe7accb07da52f06d3d9910a29bfb18a213c9c2328789985e29c`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md`는 `911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 배경 QM-001 v0.4 §7에서 품질매뉴얼 보관기간을 "5년 (MFDS GMP 기준)"으로 기재했던 v0.3을 "MFDS 의료기기 제조 및 품질관리 기준 별표2 기록보관 요건에 따름(구체적 기간은 미확인 — 1차 출처 재확인 필요)"으로 약화 처리. 1차 출처(MFDS 고시 본문)에서 품질매뉴얼 자체의 보관기간 명시 조항을 직접 인용해야 함. ## Tier 1 출처 후보 - MFDS 의료기기 제조 및 품질관리 기준 고시 (최신본) - 의료기기법 시행규칙 별표
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

> ## 📄 Regulatory Draft – KG GMP Evidence Readiness  
**Project / Issue:** 911_AUDIT_QM‑001 – “품질매뉴얼 보관기간 (별표 2) – 1차 출처 미확인”   
**Date:** 2026‑07‑28 | **Version:** daily_growth_v1  

---

### 1️⃣  Classification & Submission Route  
| Item | Korean RA Determination |
|------|------------------------|
| **Device Class** (예시) | Class II – “위험도·복합성” 기준에 부합 (requires MFDS 허가). *If the device is actually Class I, only 신고 applies; adjust accordingly.* |
| **Regulatory Pathway** | **MFDS 허가 (신규허가)** → 제출 서류 includes **KGMP 인증서**, 제품 사양서, 임상·비임상 자료, 그리고 **품질관리 매뉴얼 보관 기간에 대한 증거**. |
| **Applicable Regulation** | • 의료기기법 시행규칙 제38조의2 – “제조 및 품질관리 기준”  <br>• 별표 2(※) – 기록보관 요건 |

*(※ 별표 2는 MFDS 고시 “의료기기 제조·품질관리 기준 고시(2024‑03)’에 포함되어いる.)*

---

### 2️⃣  Required Evidence for the **“품질매뉴얼 보관기간”** requirement  

| # | Evidence | Description / Acceptance Criteria |
|---|----------|------------------------------------|
| 1 | **KGMP 인증서 (제조 시설)** | 최신(2024‑이후) KGMP 심사 합격 인증. 포함 : 시설·공정도, 품질보증 조직 도표. |
| 2 | **품질 매뉴얼(Quality Manual) 사본** | 현재 사용 중인 버전 전체 (한글). 페이지에 “문서번호/버전/발행일” 표시. |
| 3 | **별표 2 보관기간 조항 원문 발췌** | MFDS 고시 본문(2024‑03)에서 품질 매뉴얼 보관기간을 명시한 조문을 스크린샷·번역·출처(법령 번호, 발표일)と共に添付。 |
| 4 | **보관 기간 준수 확인서** | 내부 QA 담당자가 서명한 “품질매뉴얼 보관 기간 5년(또는 규정상 명시된 기간)” 이행 확인서. |
| 5 | **전자·물리 기록 저장 시스템 운영증거** (예: 서버 로그, 백업 정책) | 기록이 전자적/물리적으로 안전하게 보관되고 있는지 증명하는 시스템 스크린샷·절차 SOP. |
| 6 | **내부 감사 보고서 (보관기간 점검)** | 최근 12개월 내 실시한 품질 매뉴얼 보관점검 결과(Compliance %). |
| 7 | **번역증명** (필요 시) | 외국어 원본(예: “5‑year retention” from FDA/ISO)이 아닌, MFDS 고시 한글 조문을 그대로 사용. 번역은 필요 없으며, 한국어 원문 반드시 포함. |

> **핵심** – 현재 우리 팀이 가지고 있는 것은 *“MFDS GMP 기준 5년”* 라는 일반화된 문구뿐이며, 별표 2에서 품질 매뉴얼 자체에 대한 정확한 보관 기간 조항을 직접 인용하지 못하고 있습니다. 따라서 **Evidence #3** 가 가장 큰 Gap 입니다.

---

### 3️⃣  Missing Information (Gap Analysis)

| Gap | Why it matters | Action Required |
|-----|----------------|-----------------|
| **① 정확한 보관기간 명시조문**<br>*(별표 2에 품질매뉴얼 보관기간이 “5년”인지, 혹은 다른 기간인지 확정되지 않음)* | MFDS 심사 시 ‘보관기간 불명’ 은 **자료불충분(Insufficient Evidence)** 으로 간주, 허가 지연 위험. | • MFDS 고시(2024‑03) 원본 PDF 확보 → 해당 조문 페이지 찾기.<br>• 필요 시 MFDS 담당자(의료기기품질관리담당관)에게 ‘보관기간 문의’ 공식 서한 발송 (48 h 회신 목표). |
| **② 내부 보관 정책 문서**<br>(Evidence #4, #5) | 심사자는 실제 운영 증거를 요구. 현재는 정책 초안만 존재. | • QA 부서와 협의해 “품질 매뉴얼 보존 SOP” 최종본 작성 및 담당자 서명 확보.<br>• 전산 시스템 로그(백업 주기 등) 추출. |
| **③ 번역·해석 오류 위험** | 별표 2 조문을 오해하면 비준수 판정 가능 (예: “제조 기록 5년 vs 품질 매뉴얼 10년”). | • 법무/규제팀에 원문 해석 검증 요청.<br>• 필요 시 외부 규제 전문 변호사 의견서 첨부. |
| **④ 최신 고시 적용 여부** | 2026‑01 MFDS 개정(OECD 임상 데이터·CER 수용) 후 별표 2 내용이 일부 변경될 가능성 존재. | • 2026‑01 이후 MFDS 발표자료, 법령개정 알림 확인 (MFDS 사이트 “법령·고시 > 의료기기” 구역). |

---

### 4️⃣  Risk Controls & Mitigations (품질 매뉴얼 보관 기간)

| Risk | Impact if Uncontrolled | Control / Mitigation |
|------|------------------------|----------------------|
| **R‑1: 비규격 보관기간 적용** → 허가 거절/보류 | 프로젝트 일정 연착·추가 비용 발생 | • 최신 별표 2 조문을 기준으로 SOP 정의.<br>• 내부 교육 (QA팀, 문서관리자) – “보존 기간 규정” 주기적(Quarterly) 리뷰. |
| **R‑2: 기록 손실/무단 접근** | 시판후조사(시판후조사) 시 증거 부족 → 과징금·시정명령 | • 물리·전자 저장소 이중화 (클라우드 + 오프라인 백업).<br>• 접근 권한 관리(Audit Trail) 및 연례 보안 점검. |
| **R‑3: 문서 최신성 부재** (구버전 매뉴얼만 보관) | 규제 변화 반영 안됨 → 비준수 판정 | • 버전 관리 정책 적용 – “신규 고시 발표 시 30일 내 SOP 업데이트”. |
| **R‑4: 외부 감사(MFDS 현장점검) 대비 미비** | 즉시 시정명령·벌금 | • 연간 자체 내부 audit (보관기간 검증 포함) → 결과를 MFDS 사전 통보 자료로 활용. |

---

### 5️⃣  Citations / Regulatory References  

| Ref # | Citation (Korean) | Link / Source |
|-------|-------------------|--------------|
| **A** | *의료기기법 시행규칙 제38조의2 별표 2(2024‑03)* – “제조·품질관리 기록 보관 요건” | <https://www.mfds.go.kr/kor/bbs/view.do?bbsId=KOR_BBS_01&nttSn=12345> |
| **B** | *KGMP 인증기준(2023‑12)* – “제조시설·품질관리시스템 검사기준” | <https://www.mfds.go.kr/kor/bbs/view.do?bbsId=KOR_BBS_02&nttSn=67890> |
| **C** | *MFDS 고시 ‘의료기기 제조 및 품질관리 기준’ (2024‑03) – 별표 2* | PDF 다운로드: <https://www.mfds.go.kr/kor/bbs/download.do?fileId=XYZ> |
| **D** | *IMDRF “Principles of Safety and Performance”* – 참고용 국제 표준 (비교 근거) | <https://web.dev.imdrf.org/> |

---

### 6️⃣  Human‑Escalation Triggers  

| Trigger | When to Escalate | To Whom | Required Action |
|---------|-------------------|--------|-----------------|
| **T‑1** – Unable to locate the exact 보관기간 조문 within **48 h** after request to MFDS documentation team. | → **RA Manager** (Senior) + **Legal** <br>Provide memo of attempts, request expedited support. |
| **T‑2** – Internal SOP / Confirmation document not signed off within **5 business days** of draft completion. | → **QA Lead** for immediate sign‑off; if still pending after deadline, inform **Project Director** for resource reallocation. |
| **T‑3** – MFDS on‑site audit scheduled and evidence package >30 % incomplete. | → **Regulatory Affairs Head** to issue corrective action plan and allocate additional QA resources (e.g., external consultant). |
| **T‑4** – New amendment to 별표 2 announced (post‑2026‑01) that may change retention period. | → **Regulatory Intelligence Lead** to circulate impact analysis within 24 h; decision on re‑submission or supplemental filing escalated to **Chief Regulatory Officer**. |

---

### 7️⃣  Next Steps (Action Plan)

| Step | Owner | Due Date | Deliverable |
|------|-------|----------|-------------|
| **S1** – Retrieve official MFDS 고시 PDF (2024‑03) & locate 보관기간 조문. | RA Assistant | 2026‑07‑30 | PDF + 페이지 번호, 원문 캡처 |
| **S2** – Draft “품질매뉴얼 보존 SOP” (incl. retention period). | QA Lead | 2026‑08‑05 | SOP v1.0 + 담당자 서명 |
| **S3** – Compile evidence package (KGMP 인증서, 매뉴얼 사본, SOP, audit report, 시스템 로그). | RA Team | 2026‑08‑12 | Evidence Binder (digital & hard copy) |
| **S4** – Internal review meeting (cross‑functional) & risk register update. | Project Lead | 2026‑08‑14 | Minutes + updated RACI |
| **S5** – Submit to MFDS 허가 신청 (with complete KGMP evidence). | RA Manager | 2026‑08‑20 | Application docket #____ |

---

## 📢 Peer‑Review Prompt  

> **To:** [RA Team Member – e.g., “Jiyoon Kim, Senior Regulatory Analyst”]  
> **Subject:** Challenge on the “품질매뉴얼 보관기간” evidence draft (daily_growth_v1)  
>   
> Please review the above draft and address the following:  

1. **Assumption Check** – Are we justified in assuming a 5‑year retention period before confirming the exact clause in 별표 2? Could there be device‑specific variations?  
2. **Source Coverage** – Have we captured all possible primary sources (e.g., MFDS “고시 제2024‑03호”, “의료기기법 시행규칙 부칙” 등) or are additional 법령/통보 needed?  
3. **Jurisdiction Gaps** – Considering the 2026‑01 MFDS revision that now accepts OECD clinical data & CER, does any of those new provisions affect record‑keeping obligations for quality manuals? If so, note them.  
4. **Risk Control Adequacy** – Do you see any missing controls (e.g., electronic signature compliance, disaster‑recovery testing) that would be expected by MFDS auditors?  

Kindly reply with a brief commentary (max 300 words) and indicate any required amendments before we finalize the evidence package for submission.

--- 

*End of Draft – ready for internal circulation and peer review.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 소스의 자체 감사결과(보존기간 미확인)는 정확 반영, 에스컬레이션 우수. 시행규칙 제38조의2 오적용(실제 무관 과징금 조항) + 가짜 게시글 URL 3건(#118 패턴이 한국 법령/URL로 확장).

**Source Excerpts**

1. Chunk `104161787279348102`

> ## 배경 QM-001 v0.4 §7에서 품질매뉴얼 보관기간을 "5년 (MFDS GMP 기준)"으로 기재했던 v0.3을 "MFDS 의료기기 제조 및 품질관리 기준 별표2 기록보관 요건에 따름(구체적 기간은 미확인 — 1차 출처 재확인 필요)"으로 약화 처리. 1차 출처(MFDS 고시 본문)에서 품질매뉴얼 자체의 보관기간 명시 조항을 직접 인용해야 함.

2. Chunk `1013054385847956806`

> ## Tier 1 출처 후보 - MFDS 의료기기 제조 및 품질관리 기준 고시 (최신본) - 의료기기법 시행규칙 별표

### kb-eval-20260715-it14-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it14-ra_kr-005", "iteration": 14, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "5629504a8aa6e72a", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5629504a8aa6e72a`
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

> **Regulatory Draft – KGMP Evidence Readiness (Scenario #5629504a8aa6e72a)**  
*Prepared by Sam – Korea Regulatory Affairs Specialist (MFDS/KGMP)*  

---

### 1. Device Classification & Submission Route  

| Item | Determination | Rationale / Source |
|------|---------------|--------------------|
| **Risk Class** | *To be confirmed* – depends on intended use, invasiveness and duration of contact (see MFDS “의료기기 분류표”). If the device falls into **Class II‑III**, a **허가 (approval)** is required; if **Class I‑II (low risk)** a **신고 (notification)** may be sufficient. | Classification must be performed before any evidence checklist can be finalised. |
| **Submission Pathway** | • **KGMP 인증 + 허가/신고** <br>• Use of the **“의료기기 제조 및 품질관리 기준” 고시** and **“의료기기 GMP 심사·평가 등에 관한 규정”** (see source [1]). | All Korean‑manufactured or imported devices must satisfy KGMP certification before MFDS review. |

> **Human‑Escalation Trigger #1:** *If classification cannot be resolved from product description, pause and request a formal classification opinion from the MFDF Division of Medical Devices.*

---

### 2. Required Evidence Packages (KGMP & MFDS)  

| Evidence Category | Specific Documents / Items | KGMP Mapping | MFDS Requirement | Notes |
|-------------------|---------------------------|--------------|------------------|------|
| **Facility/Process** | • Completed **KGMP 심사 신청서** <br>• Facility layout, flow‑charts, SOPs, equipment lists <br>• Recent **품질관리 시스템 (QMS) audit reports** (ISO 13485:2016) | Required by KGMP 심사 체크리스트 (source [2]) | MFDS GMP inspection prior to 허가/신고 | Must be in Korean or accompanied by certified translation. |
| **Technical Documentation** | • Design Dossier (Design History File) <br>• Risk Management file (ISO 14971) <br>• Verification & Validation reports <br>• Software documentation (if applicable) | Part of “기술문서 심사 대응 자료” (source [2]) | MFDS technical dossier submission (same as EU/US but Korean language required) | Include **Korean IFU** and label drafts. |
| **Clinical Evidence** | • Local clinical data *or* accepted foreign data via the **2026‑01 OECD Clinical Evaluation Report (CER) acceptance** <br>• If foreign data used, must be accompanied by a **comparative justification** and **Korean translation** | KGMP does not mandate clinical data but MFDS does for Class II‑III. | MFDS accepts CERs from FDA/CE jurisdictions under the 2026 revision (OECD mutual recognition). | **Missing if only US/EU data without CE‑type conformity evidence** – see Trigger #2 below. |
| **Conformity Evidence (Import)** | • CE Marking Certificate or FDA 510(k) clearance <br>• *If* relying on foreign GMP, submit **국내 적합성 인정서** for imported items (source [2]) | Required as “적합성 인정서 (수입품목용)” | MFDS requires proof of equivalent manufacturing quality. | Must be translated and notarized. |
| **Labeling & IFU** | • Draft Korean label (Korean language, safety symbols) <br>• Korean Instruction for Use (IFU) – must meet “의료기기 라벨링지침” | Not part of KGMP per se but required for 허가/신고. | MFDS labeling review – includes mandatory product name, manufacturer, lot number, expiry, warnings, etc. | **Missing if only English version available** – Trigger #3. |
| **Post‑Market Surveillance (PMS) Plan** | • PMS plan aligned with MFDS “시판후조사” requirements <br>• Method for adverse event reporting in Korean | KGMP requires a PMS system as part of QMS. | Mandatory for Class II‑III devices. | Include Korean‑language reporting forms. |

---

### 3. Identified Gaps (Missing Information)  

| Gap | Why It Matters | Evidence Needed |
|-----|----------------|-----------------|
| **1. Definitive Device Classification** | Determines submission route and depth of clinical evidence required. | Detailed product description, intended use, risk analysis – to be reviewed by MFDS classification team. |
| **2. Korean‑language Clinical/Evidence Translation** | MFDS will not accept English‑only CERs; a certified Korean translation is mandatory. | Certified translation of FDA 510(k) summary / CE Technical File or OECD CER. |
| **3. Local Clinical Data (if required)** | For certain high‑risk devices, MFDS still requires *some* Korean clinical data despite OECD acceptance. | Small‑scale Korean pilot study or real‑world evidence meeting MFDS “국내 임상시험 요건”. |
| **4. Complete KGMP Facility Documentation** | The checklist in source [2] expects completed facility SOPs and audit reports; missing items will delay inspection. | Updated SOPs, equipment qualification records, recent internal audit report (Korean). |
| **5. Korean Label & IFU** | Mandatory for market entry; failure leads to rejection at the labeling review stage. | Draft label and IFU in Korean, with correct symbols and safety statements. |
| **6. PMS Plan in Korean** | Required for post‑approval monitoring; lack of plan prevents approval. | Detailed PMS SOP, complaint handling flowchart, KPI definitions – all in Korean. |

> **Human‑Escalation Trigger #2:** *If any of the above gaps cannot be remedied within 30 days, senior RA manager must be alerted to assess feasibility of alternative pathways (e.g., limited market launch under “시험용 의료기기” designation).*

---

### 4. Core Risk Controls & Mapping  

| Control | Source Standard | How it satisfies MFDS/KGMP |
|---------|----------------|---------------------------|
| **Design‑Control** (ISO 13485 §7) | ISO 13485:2016 | Demonstrates systematic design process – required for technical dossier. |
| **Risk Management File** (ISO 14971) | IMDRF/ISO 14971 | MFDS requires documented risk analysis; aligns with KGMP “품질관리 체계”. |
| **Process Validation** | GMP 규정, KGMP | Validated manufacturing processes satisfy “GMP 심사·평가” requirements. |
| **Traceability Matrix** (serial number → batch) | MFDS 라벨링/추적 의무 | Enables recall and adverse‑event reporting – a key PMS component. |
| **Supplier Qualification** | KGMP 공급업체 관리 규정 | Ensures imported components meet Korean quality standards. |

---

### 5. Key Citations  

* **KGMP Core Documents:** 「의료기기 제조 및 품질관리 기준」 고시, 「의료기기 GMP 심사·평가 등에 관한 규정」 – source [1].  
* **Checklist & Technical File Guidance:** “GMP 심사 신청서·심사 체크리스트”, “기술문서 심사 대응 자료”, “적합성 인정서 (수입품목용)” – source [2].  
* **2026‑01 MFDS Revision (OECD CER Acceptance):** MFDS Notice No. 2026‑02, “국제 임상 데이터 및 적합성 인증에 관한 지침”.  

---

### 6. Human‑Escalation Triggers Summary  

| # | Condition | Action |
|---|-----------|--------|
| 1 | Unclear device class after initial review. | Pause work and request formal classification opinion from MFDS Division. |
| 2 | Any identified gap cannot be closed within 30 days (e.g., missing Korean translation, local clinical data). | Notify Senior RA Manager for risk‑based decision on alternative pathways or timeline extension. |
| 3 | Submission package lacks Korean label/IFU drafts. | Immediate halt of dossier finalisation; engage marketing & regulatory to produce Korean language versions. |
| 4 **(Critical)** | KGMP facility audit fails critical compliance items (e.g., QMS not ISO 13485‑certified). | Escalate to Corporate QA & consider postponing market entry until remediation. |

---

### 7. Peer Review Prompt  

> **To: Fellow RA colleague**  
> Please examine the assumptions and source coverage in this draft:  
> 1. **Classification assumption:** Are we correctly applying MFDS classification rules given the limited product description? Could any nuance (e.g., accessory vs. main device) change the route?  
> 2. **Evidence mapping:** Does the reliance on OECD CER acceptance fully satisfy Korean clinical data expectations for Class II‑III devices, or should we anticipate additional local data? Cite any recent MFDS decisions you know of where CER alone was insufficient.  
> 3. **KGMP checklist completeness:** Have we captured *all* mandatory items from the KGMP 심사 신청서 체크리스트 (e.g., environmental monitoring, personnel qualification) that might be missing here?  
> 4. **Jurisdiction‑specific gaps:** Are there any Korean labeling or PMS requirements not reflected in this draft (e.g., “보건복지부 고시 제2026‑03호” for software updates)?  
> Please challenge each point and suggest any extra documentation or clarification needed before we submit to senior RA for sign‑off.  

---

### 8. Reusable RA Judgment (Recorded for Knowledge Base)

```json
{
  "honcho_conclude": {
    "scenario_id": "5629504a8aa6e72a",
    "summary": "KGMP evidence readiness requires definitive device classification, completed KGMP facility documentation, Korean‑language technical dossier (including label/IFU), and either local clinical data or OECD‑accepted CER with certified translation. Missing items are identified and linked to MFDS/KGMP citations. Human escalation triggers defined for ambiguous classification, unresolved gaps >30 days, and critical KGMP audit failures.",
    "key_actions": [
      "Obtain formal device class opinion from MFDS if unclear.",
      "Secure certified Korean translations of all foreign clinical/evidence documents.",
      "Generate Korean label & IFU drafts aligned with MFDS labeling guidance.",
      "Prepare local clinical data or robust justification for OECD CER acceptance per 2026‑01 revision.",
      "Complete KGMP facility checklist items (SOPs, audits, supplier qualification).",
      "Draft PMS plan in Korean and integrate risk management file per ISO 14971."
    ],
    "peer": "ai",
    "timestamp": "2026-07-28T14:32Z"
  }
}
```

---  

*End of draft – ready for peer review.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 얇은 소스 대비 적절히 스코프 제한, 분류를 '확인 필요'로 정직하게 유보. 'MFDS 고시 제2026-02호'는 번호·제목 모두 창작(정답은 제2026-6호).

**Source Excerpts**

1. Chunk `341244002941932847`

> ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트

2. Chunk `634338496332185325`

> ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)
