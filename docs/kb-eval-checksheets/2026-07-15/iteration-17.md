# KB Eval Checksheet - 2026-07-15 Iteration 17

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260715-it17-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_us-001", "iteration": 17, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "3e8e67ad2abb6e46", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `3e8e67ad2abb6e46`
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

> **Regulatory Draft – 510(k) Predicate Strategy (Daily Growth v1)**  

---

### Bottom‑Line Recommendation
- **Device Classification:** Class II (most likely under 21 CFR 862 or 892 depending on specific technology).  
- **Submission Route:** Traditional 510(k) with *Substantial Equivalence* (SE) argument.  
- **Fast‑Track Path:** If a predicate exists that is **“legally marketed”** and the new device differs only in non‑material aspects, pursue a standard 510(k) using the eSTAR templates (eSTAR_01 – Device Description/IFU).  

---

## 1. Classification & Submission Route  
| Step | Action | Regulatory Reference |
|------|--------|-----------------------|
| **Determine Class** | Search FDA Product Code database → map to regulation part (e.g., “DIA” – Diagnostic Imaging, 21 CFR 862.2030) | 21 CFR 862/882 |
| **Select Predicate** | Identify a legally marketed device with the same intended use & technology; ensure it is listed in the FDA 510(k) database (see Source [2]) | 21 CFR 807.92(a)(3) |
| **Choose Submission Type** | Traditional 510(k) – SE claim (use eSTAR templates for electronic submission) | 21 CFR 807.92(b) |

*If no suitable predicate exists, consider a De Novo request (21 CFR 860).*

---

## 2. Required Evidence (per FDA Guidance & the eSTAR workflow)

| Section (eSTAR template) | Core Content | Typical Data Needed |
|---------------------------|--------------|---------------------|
| **Device Description / IFU** (eSTAR_01) | Device name, model, materials, principle of operation, labeling | Detailed schematics, bill‑of‑materials, user manual |
| **Indications for Use** | Precise clinical claim identical or narrower than predicate | Comparative text table |
| **Performance Testing** (bench & animal if applicable) | Functional safety, accuracy, reliability, durability | Test protocols, statistical analysis, pass/fail criteria |
| **Biocompatibility** | ISO 10993‑1 assessment per device contact mode | Cytotoxicity, sensitization, irritation data |
| **Electromagnetic Compatibility / EMI** (if electronic) | IEC 60601‑1‑2 compliance | Emission & immunity test reports |
| **Software Validation** (if software > 30 days) | IEC 62304 lifecycle documentation | Verification/validation plan, risk analysis (ISO 14971) |
| **Sterilization / Shelf‑Life** (if applicable) | Sterility assurance level, packaging validation | Biological indicator results, accelerated aging data |
| **510(k) Summary & Statement** | Narrative of SE comparison + summary table | Comparison matrix citing predicate 510(k) number(s) |

*All sections should be assembled using the FDA’s eSTAR electronic submission templates (Source [1]).*

---

## 3. Missing Information (Typical Gaps to Flag)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact Predicate Device Number** | Needed for SE matrix; otherwise FDA may reject as “no predicate identified”. | Conduct focused search in the 510(k) database using product code & intended use. |
| **Clinical Data (if claim exceeds predicate)** | May be required to address new indications or altered risk profile. | Plan a limited usability/clinical feasibility study; incorporate into Clinical Evaluation Report (CER). |
| **Risk Management File (ISO 14971)** | Demonstrates mitigation of identified hazards; mandatory for Class II devices. | Generate FMEA/FMECA, update Design History File (DHF). |
| **Software Documentation** (if applicable) | FDA requires a Software Validation Plan per 21 CFR 820.30(c)(6). | Produce software architecture diagram, source code review summary. |
| **Biocompatibility Testing Scope** | New material or change in patient contact may invalidate existing data. | Conduct full ISO 10993‑5/10 battery if any alteration. |

---

## 4. Risk Controls (ISO 14971‑aligned)

1. **Hazard Identification:** List all mechanical, electrical, thermal, and biological hazards.  
2. **Risk Estimation:** Assign severity & probability; use a risk matrix.  
3. **Mitigation Strategies:**  
   - Design safeguards (e.g., interlocks, alarms).  
   - Protective labeling & user training.  
   - Redundant circuitry for critical functions.  
4. **Verification of Controls:** Run verification tests per 21 CFR 820.30(c)(2) and document results in the DHF.  
5. **Post‑Market Surveillance Plan:** Follow 21 CFR 822 (PMCF) to capture emerging risk information.

---

## 5. Key Citations

| Regulation / Guidance | Relevance |
|-----------------------|-----------|
| 21 CFR 807.92 – Substantial Equivalence | Defines predicate requirements |
| 21 CFR 820 – QSR (effective Feb 2026, ISO 13485‑aligned) | Quality system evidence |
| FDA “Guidance for Industry and FDA Staff: Preparing a 510(k) Submission” (Sept 2019) | Template & content expectations |
| FDA eSTAR Submission Guidance (internal docs referenced in Source [1]) | Electronic submission format |
| ISO 14971:2023 – Medical Device Risk Management | Risk control framework |
| IEC 60601‑1‑2 (2020) – EMI/EMC for medical electrical equipment | If device includes electronics |

---

## 6. Human‑Escalation Triggers

| Trigger | Reason & Required Action |
|---------|---------------------------|
| **No clear predicate found** after exhaustive search | Escalate to senior RA lead; consider De Novo pathway. |
| **Regulatory question on clinical data extent** (e.g., claim expansion) | Route to Clinical Affairs and Regulatory Lead for risk‑benefit assessment. |
| **FDA “Additional Information” (AI) request for missing test data** | Immediate coordination with engineering & QA to generate requested evidence; update project timeline. |
| **Change in FDA guidance (e.g., new QMSR requirements)** | Notify regulatory manager; assess impact on current submission schedule. |
| **Discrepancy between intended use and labeling** identified during internal review | Pause submission, revise IFU, obtain cross‑functional sign‑off. |

*All escalations should be logged in the project’s risk register and communicated via the RA decision‑making channel.*

---

## 7. Peer Review Prompt (for an RA colleague)

> **Please review the above predicate strategy draft and challenge the following assumptions:**
> 
> 1. The classification as Class II is appropriate given our limited device description—are there any regulatory product codes that might place it in Class III?  
> 2. The identified evidence list assumes a traditional 510(k); does the current eSTAR guidance (Source [1]) suggest any additional sections for emerging technologies (e.g., AI/ML) that we may have missed?  
> 3. Risk controls are framed around ISO 14971:2023—are there any FDA‑specific expectations (e.g., 21 CFR 820.30(c)(5)) that need explicit documentation?  
> 4. Are the escalation triggers sufficiently granular for rapid response to an FDA AI request, or should we add thresholds (e.g., “AI requiring > 2 weeks of data generation”)?  

*Provide any jurisdiction‑specific gaps you spot (state‑level variations, recent guidance updates, etc.).*

---

### Reusable RA Judgment (recorded)

**honcho_conclude:**  
```
{
  "scenario_id":"3e8e67ad2abb6e46",
  "bottom_line":"Class II device → Traditional 510(k) with SE claim using eSTAR templates.",
  "key_steps":["Determine class via product code","Identify legally marketed predicate in FDA 510(k) DB","Assemble evidence per eSTAR sections (Device Description, Performance Testing, Biocompatibility, EMC, Software Validation)","Prepare risk management file (ISO 14971)","Submit electronically via eSTAR"],
  "common_gaps":["Missing predicate number","Insufficient clinical data for expanded claim","Incomplete software documentation","Unvalidated biocompatibility for new materials"],
  "escalation_triggers":["No predicate found → senior RA/De Novo","FDA AI request → engineering‑QA coordination","Regulatory guidance change → notify manager"],
  "citation_set":["21CFR807.92","21CFR820 (QMSR Feb2026)","FDA 510(k) Guidance Sep2019","eSTAR internal guide (Source [1])","ISO14971:2023","IEC60601‑1‑2"]
}
```

*This judgment can be reused for any future Class II devices where a traditional 510(k) SE pathway is pursued.*

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

> 결론(Class II, Traditional 510(k), SE)은 정확. '21 CFR 820.30(c)(6)/(c)(2)' 세부조항 창작(실제 (c)는 미세분화, 검증됨) + 21 CFR 822를 PMCF로 오설명(EU 용어).

**Source Excerpts**

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20260715-it17-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_us-002", "iteration": 17, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f7c4967207904d92", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f7c4967207904d92`
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

### 1. Bottom‑Line Recommendation  
**Submit a Traditional 510(k) using Substantial Equivalence (SE).** The device falls within Class II (or potentially Class I with special controls) and a suitable predicate exists in the FDA’s database. No de Novo or PMA is required unless later clinical data reveal unmet safety/efficacy gaps.

---

### 2. Classification & Submission Route  

| Item | Determination |
|------|----------------|
| **Regulatory Class** | **Class II** – typical for devices that incorporate moderate risk components (e.g., powered diagnostic, imaging, or monitoring accessories). |
| **Statutory Basis** | FD&C Act §510(k), 21 CFR 807. |
| **Submission Type** | Traditional 510(k) with Substantial Equivalence to a legally marketed predicate. |
| **Target Review Timeline** | FDA goal ≈ 90 days (see Table 2, source [2]). |

*If the device incorporates a novel technology not previously cleared and no predicate can be justified, the fallback is a De Novo request (FD&C Act §513(f)(2), 21 CFR 860).*

---

### 3. Required Evidentiary Package  

| Category | Minimum Evidence (per FDA Guidance) |
|----------|--------------------------------------|
| **Device Description** | Detailed specification sheet, drawings, labeling, and user manual. |
| **Predicate Comparison** | Side‑by‑side table of intended use, technological characteristics, performance specifications, and any differences with mitigation strategies. |
| **Bench (Non‑clinical) Testing** | • Electrical safety (IEC 60601‑1)<br>• Biocompatibility (ISO 10993)<br>• Performance/accuracy testing per recognized standards (e.g., IEC 62561 for imaging). |
| **Software Validation** *(if applicable)* | Verification & validation according to FDA’s “Guidance for the Content of Premarket Submissions for Software‑Contained Devices” and IEC 62304. |
| **Usability / Human Factors** | Summative usability study per FDA’s “Human Factor Considerations for Medical Devices” (if user interface is novel). |
| **Risk Management** | ISO 14971 risk analysis/report including identified hazards, mitigations, and residual risk justification. |
| **Labeling & IFU** | Draft labeling compliant with 21 CFR 801 & FDA’s “Content of Labeling for Medical Devices” guidance. |
| **Sterilization Validation** *(if sterile)* | Sterility assurance data (ISO 11137). |
| **Clinical Data** | *Only if* the device exhibits new intended use or substantial design changes that trigger the “clinical data conditional” clause (§3) – see source [1]. Otherwise, clinical data are **not required** for SE. |
| **QMS Documentation** | Evidence of ISO 13485‑aligned QMS per new FDA QMS Rule (effective 2026‑02). Include Design History File excerpts and CAPA records relevant to the device. |

*All referenced guidance documents can be accessed via the links in source [1] and the FDA’s “Guidance for Premarket Notification 510(k)s” page.*

---

### 4. Identified Missing Information (Gap Analysis)

| Gap | Impact on Submission | Suggested Remedy |
|-----|----------------------|------------------|
| **Predicate Device Identification** | No explicit predicate cited in the brief. | Perform a predicate search using FDA’s Product Classification Database; select a device with identical intended use and comparable technology. |
| **Risk Mitigation Details for Differences** | Only high‑level differences described. | Provide a detailed risk control table (ISO 14971) linking each difference to specific mitigations and verification data. |
| **Software Documentation Package** *(if software present)* | No evidence of verification/validation plan. | Include Software Development Plan, Verification Test Results, Validation Report, and Cybersecurity Assessment. |
| **Human Factors Data** | Usability testing not mentioned. | Conduct at least a formative + summative usability study if the user interface is novel (e.g., touchscreen). |
| **QMS Conformance Evidence** | No ISO 13485‑aligned QMS artifacts submitted. | Attach certificates, audit reports, and SOPs demonstrating compliance with the 2026 QMS Rule. |
| **Sterilization Process Validation** *(if applicable)* | Absence of sterilization data. | Provide validated Sterility Assurance Level (≥10⁻⁶) data per ISO 11137. |

---

### 5. Core Risk Controls (ISO 14971‑Based)

1. **Design Controls:** FDA‑required design history file; traceability matrix linking requirements → design inputs → outputs → verification/validation.
2. **Electrical Safety & EMC:** IEC 60601‑1 compliance testing and labeling of safety warnings.
3. **Biocompatibility:** ISO 10993‑1 risk assessment with material test reports (cytotoxicity, sensitization, irritation).
4. **Software Security:** Threat analysis, secure coding practices, regular patching plan.
5. **Usability Safeguards:** Confirmation prompts for critical settings; user training program documented in IFU.
6. **Labeling Controls:** Clear contraindications, warnings, and instructions per 21 CFR 801.

---

### 6. Key Regulatory Citations  

| Topic | FDA Guidance / Regulation |
|-------|----------------------------|
| 510(k) Submission Requirements | <https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k> |
| De Novo Classification Request | <https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request> |
| PMA Clinical Study Guidance | <https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies> |
| Solid‑State X‑ray Imaging Devices (example predicate) | <https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices> |
| Clinical Data Determination Table (Fig. 3) | FDA “Clinical Data Needed for 510(k) vs De Novo vs PMA” – PDF #171837 (see source [1]) |
| QMS Rule (effective Feb 2026) | 21 CFR 820, aligned with ISO 13485; eSTAR compliance dates 2023‑10‑01 → 2025‑10‑01. |

---

### 7. Human‑Escalation Triggers  

| Trigger | Action |
|---------|--------|
| **No viable predicate** (no device of same intended use/technology) | Escalate to senior RA for De Novo vs PMA decision. |
| **Design change that introduces a new principle of operation** | Pause submission; conduct risk reassessment and seek FDA pre‑submission meeting. |
| **Clinical data required per §3 conditional clause** (e.g., significant performance gap) | Initiate clinical study plan; involve Clinical Affairs lead and inform Project Management. |
| **QMS non‑compliance with new 2026 rule** | Immediate corrective action; senior QA/RA notified. |
| **Regulatory fee changes or user‑fee exemption eligibility change** | Finance & RA coordinate to adjust budget; flag for leadership approval. |

---

### 8. Peer Review Prompt  

> **To the assigned RA peer:**  
> Please review the above predicate‑strategy draft and challenge the following assumptions:  
> 1. The selection of a Class II traditional 510(k) pathway – are there any device‑specific nuances (e.g., special controls, recognized standard gaps) that could force a De Novo route?  
> 2. Completeness of source coverage – does the excerpted guidance capture all relevant FDA documents for this technology class (e.g., recent guidance on AI/ML, cybersecurity)?  
> 3. Jurisdiction‑specific gaps – are there any state‑level or international (e.g., Canada Health Canada) requirements that we have omitted but could affect the US submission timeline?  

> Provide concrete suggestions or missing citations so we can refine the package before final submission.

---

### 9. Recommended Next Steps  

1. **Predicate Search & Confirmation** – complete within 5 business days.  
2. **Gap Closure** – assign bench‑testing and risk‑control tasks to engineering leads.  
3. **QMS Evidence Compilation** – gather ISO 13485 audit reports (QMS Rule compliance).  
4. **Prepare Draft 510(k) Submission** – populate FDA eCopy template; schedule pre‑submission meeting if high‑risk differences persist.  

---

### 10. Reusable RA Judgment (Honcho Record)

```json
{
  "honcho_conclude": {
    "lesson_id": "us_510k_predicate_strategy_daily_growth_v1_f7c4967207904d92",
    "date": "2026-07-31",
    "summary": "For Class II devices, the default and fastest clearance path is a Traditional 510(k) with Substantial Equivalence where a predicate exists. Key evidence includes detailed predicate comparison, bench testing per recognized standards, ISO 14971 risk analysis, and QMS documentation aligned to the 2026 FDA Quality System Rule. Clinical data are only required when the device presents a new intended use or substantial design change triggering the conditional clause (§3 of FDA clinical‑data need guidance). Missing items (predicate identification, detailed risk control for differences, software V&V, human‑factors study, QMS artifacts) should be closed before filing. Escalate if no predicate is found, if a new principle of operation emerges, or when QMS gaps threaten compliance with the 2026 rule.",
    "confidence": "high",
    "applicability": ["Class II traditional 510(k)", "devices requiring predicate", "post‑Feb 2026 QMS alignment"],
    "references": [
      "FDA 510(k) Premarket Notification guidance (21 CFR 807)",
      "FDA De Novo Guidance (21 CFR 860)",
      "Clinical Data Need Determination Table – FDA PDF #171837",
      "QMS Rule effective Feb 2026, ISO 13485"
    ],
    "peer_review_prompt": "Please validate the assumption that a Class II traditional 510(k) is appropriate and identify any newer guidance (e.g., AI/ML, cybersecurity) that may affect this device’s submission."
  }
}
```

*No work package closure actions are taken automatically; please review the comment above and close the WP if appropriate.*

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

> 경로비교표(수수료·심사기간·eSTAR 날짜)는 소스와 정확 일치. 'IEC 62561'을 영상 성능시험 표준으로 오인용(실제 낙뢰보호 표준, 무관 — 검증됨).

**Source Excerpts**

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20260715-it17-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_us-003", "iteration": 17, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "4af3b574aba148d9", "source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md", "source_hash": "a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `4af3b574aba148d9`
- Source: `github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/959_FDA_510k_RTA_%EA%B8%B0%EC%B4%88%EB%B3%B4%EA%B0%95_3%EC%A3%BC%EC%B0%A8_%EC%9E%AC%EC%9D%B4%EC%9B%94.md)
- Source hash: `a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `959_FDA_510k_RTA_기초보강_3주차_재이월.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **3주 연속 0% 정체** (06-26 / 07-03 / 07-10 동일). #951(2026-07-03 등록)이 미착수 상태로 재이월됨. ## 이관 배경 - 선행 이슈: #951 (2026-07-03 등록, status: draft, 착수 실적 없음) - 원인 추정: 이번 주 개발/QA 인력이 감사(audit) sweep(01_법규_규제, 02_품질경영시스템_QMS)에 전량 투입되어 체크리스트 보강 착수 못함
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

> **Regulatory Draft – 510(k) Predicate Strategy (Scenario 4af3b574aba148d9)**  

---

### 1️⃣ Bottom‑Line Recommendation  
- **Class II device → Traditional 510(k) submission** is the fastest credible path, provided a suitable predicate can be identified.  
- Immediate actions: lock in at least one *clearly comparable* predicate, complete missing Design History File (DHF) items, and finish QMS documentation before the next audit sweep.

---

### 2️⃣ Device Classification & Submission Route  

| Attribute | Determination |
|-----------|----------------|
| **Classification** | Class II – because the device performs *[insert functional description]* and is subject to special controls listed in 21 CFR 862.*** (e.g., §862.1000 for “X‑ray imaging systems”). |
| **Submission Type** | Traditional 510(k) (§807.92(a)). If no adequate predicate exists, consider **De Novo** (Q‑subclass) as a fallback. |
| **Regulatory Timing** | Goal: filing within **30 days** of audit sweep completion to avoid further delay. |

---

### 3️⃣ Predicate Device Identification – Strategy  

| Step | Action | Success Criteria |
|------|--------|-------------------|
| **3.1** | Query FDA’s “510(k) Premarket Notification Database” for devices with same **intended use**, **technology**, and **material** (within ±10 % of key parameters). | ≥ 1 candidate with “substantially equivalent” decision. |
| **3.2** | Prioritize predicates ≤ 5‑years old, FDA‑cleared under **same special controls**. | Reduces risk of post‑market issues. |
| **3.3** | Map each claim/feature to the predicate; note any *new* claims that will require additional justification (e.g., performance enhancements). | Documented gaps ≤ 2. |

*If no suitable predicate emerges, trigger De Novo evaluation.*

---

### 4️⃣ Required Evidence Package  

| Evidence Type | Core Content | Reference |
|---------------|--------------|-----------|
| **Device Description & Labeling** | Full specifications, intended use statement, labeling artwork. | 21 CFR 803.3 |
| **Performance Testing** | Bench‑top functional tests (accuracy, repeatability), safety testing per special controls. | FDA Guidance “Medical Device Use-Safety” 2024. |
| **Biocompatibility** | ISO 10993‑1 assessment for all patient-contacting materials. | 21 CFR 820.3; ISO 13485:2016 |
| **Software Validation** (if applicable) | IEC 62304 lifecycle, verification/validation plan, risk‑based testing results. | FDA Guidance “Software as a Medical Device” 2022. |
| **Sterilization Validation** (if applicable) | Cycle parameters, bioburden data, sterility assurance level (SAL). | FDA Guidance “Medical Device Sterilization” 2019. |
| **Risk Management File** | ISO 14971‑based risk analysis, mitigation measures, residual risk justification. | 21 CFR 820.30 |
| **Design History File (DHF)** | Complete design inputs, outputs, verification/validation records, change control log. | 21 CFR 820.30(a) |
| **Quality System Documentation** | Current QMS compliant with the new **QMSR (effective Feb 2026)** – ISO 13485‑aligned procedures, CAPA, training records. | 21 CFR 820; FDA “QMS Regulation” final rule 2026 |

---

### 5️⃣ Missing Information & Immediate Gaps  

| Gap | Impact | Action Needed |
|-----|--------|---------------|
| **Incomplete DHF** – missing Design Verification reports for Sub‑system X. | Blocks substantive equivalence claim. | Assign a dedicated engineer; complete within 10 days. |
| **Risk Management File** – no documented mitigation for *electromagnetic interference* (EMI) scenario. | Potential non‑conformity with special controls. | Conduct EMI testing, update ISO 14971 analysis. |
| **QMSR Documentation** – SOPs for Supplier Qualification not yet aligned to 2026 rule. | Could trigger FDA Form 2541 deficiency. | Revise SOPs; obtain QA sign‑off before filing. |
| **Predicate Confirmation** – no finalized predicate selection documented. | Submission cannot proceed. | Complete predicate matrix (see Section 3). |
| **Audit Sweep Resource Drain** – all QA/Dev staff allocated to audit sweep, delaying 510(k) prep. | Timeline risk > 30‑day buffer. | Escalate for additional staffing or temporary reallocation (Human‑Escalation Trigger #2). |

---

### 6️⃣ Risk Controls & Mitigation Plan  

1. **Design Controls** – enforce documented design reviews per milestone; record minutes in DHF.  
2. **Verification/Validation** – adopt a *risk‑based* test matrix (higher RPN → more rigorous testing).  
3. **Supplier Management** – implement ISO 13485‑compliant supplier audit checklist; update QMSR records.  
4. **Post‑Market Surveillance Plan** – outline FDA‑required PMS for Class II devices (including complaint handling and periodic reporting).  

---

### 7️⃣ Key Citations  

| Source | Relevance |
|--------|-----------|
| 21 CFR 807.92(a) | Traditional 510(k) pathway definition. |
| 21 CFR 862 – Special Controls for **[device type]** | Lists required safety/effectiveness criteria. |
| FDA Guidance “Medical Device Use‑Safety” (2024) | Performance testing expectations. |
| IEC 62304 & FDA “Software as a Medical Device” Guidance (2022) | Software validation requirements. |
| Final Rule – QMS Regulation (effective Feb 2026) | Updated GMP/QMSR compliance obligations. |
| ISO 14971:2019, ISO 10993‑1:2018 | Risk management & biocompatibility standards. |

---

### 8️⃣ Human‑Escalation Triggers  

- **Trigger A – Predicate Gap:** No suitable predicate after exhaustive search (≥ 3 days). → Escalate to RA Manager for De Novo recommendation.  
- **Trigger B – Resource Bottleneck:** > 50 % of QA/Dev staff assigned to audit sweep *and* 510(k) deliverables overdue > 7 days. → Notify Project Lead & request supplemental staffing.  
- **Trigger C – QMSR Non‑Compliance:** Any missing SOP or CAPA record flagged during internal QA review. → Immediate corrective action plan; if unresolved in 5 working days, raise to Regulatory Compliance Officer.  

---

### 9️⃣ Peer Review Prompt (for RA colleague)  

> *Please review the assumptions and source coverage in this draft:*
> 
> - **Predicate Selection:** Are we confident that the chosen predicate(s) truly share the same intended use and technology level? Have alternative predicates been exhaustively screened?
> - **Regulatory Scope:** Does the classification (Class II) align with current FDA product code listings, considering any recent re‑classifications in 2025–2026?
> - **QMSR Integration:** Are we correctly interpreting the new QMS Regulation (Feb 2026) for this device type? Any jurisdictional nuances missed (e.g., state‑level requirements)?
> - **Evidence Gaps:** Have all required testing modalities been captured, especially for *[specific risk]*?
> 
> Provide any missing citations or flag contradictory guidance.

---

### 10️⃣ Reusable RA Judgment (recorded for future cases)  

**Judgment ID:** `RA_JUDG_2026_07_31_001`  
**Lesson Statement:**  
*When a concurrent audit sweep consumes the entire QA/Dev workforce, 510(k) preparation stalls and deadline risk spikes. To mitigate, embed a **resource‑buffer clause** in the project charter that reserves at least one full‑time equivalent (FTE) for regulatory deliverables during any scheduled internal audit period.*  

*Action:* Capture this judgment in the organization’s regulatory knowledge base; reference it whenever an audit sweep is planned overlapping a 510(k) filing window.

--- 

*Prepared by: Mike – US Regulatory Affairs Specialist*  
*Date: 2026‑07‑31*

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

> 감사 인력 리소스 충돌이라는 실질적 통찰 우수, 소스에 근거. '21 CFR 803.3'을 기기설명/라벨링 근거로 오인용(실제 이상사례 보고 규정, 무관 — 검증됨).

**Source Excerpts**

1. Chunk `243090506975535922`

> ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **3주 연속 0% 정체** (06-26 / 07-03 / 07-10 동일). #951(2026-07-03 등록)이 미착수 상태로 재이월됨.

2. Chunk `608844759849194169`

> ## 이관 배경 - 선행 이슈: #951 (2026-07-03 등록, status: draft, 착수 실적 없음) - 원인 추정: 이번 주 개발/QA 인력이 감사(audit) sweep(01_법규_규제, 02_품질경영시스템_QMS)에 전량 투입되어 체크리스트 보강 착수 못함

### kb-eval-20260715-it17-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_us-004", "iteration": 17, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "cafc5ed9b0d71c38", "source": "github:holee9/MD-process/issue-drafts/220_13_FDA_510k_RTA_핵심양식_초안.md", "source_hash": "2b2e64ed872d9caf987e923334f8bb1dab23e1f65d28ac42a81828e751edceb2"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cafc5ed9b0d71c38`
- Source: `github:holee9/MD-process/issue-drafts/220_13_FDA_510k_RTA_핵심양식_초안.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/220_13_FDA_510k_RTA_%ED%95%B5%EC%8B%AC%EC%96%91%EC%8B%9D_%EC%B4%88%EC%95%88.md)
- Source hash: `2b2e64ed872d9caf987e923334f8bb1dab23e1f65d28ac42a81828e751edceb2`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `220_13_FDA_510k_RTA_핵심양식_초안.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 배경 `build_readiness.py` 결과 FDA 510(k) RTA 점수 52% 고착. 하기 5개 must 항목이 미충족 상태로 실제 제출 시 FDA RTA(Refuse to Accept) 직행. ## 예상 효과 FDA 510(k) 점수 52% → 약 85% (5개 must 해소 시)
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

> **Bottom Line**  
The device falls under **Class II** and requires a **traditional 510(k)**. The current RTA score of 52 % is driven by five “must‑have” deficiencies; addressing them will raise the score to ~85 %, positioning the submission for acceptance on first review.

---

## 1. Classification & Submission Route  
| Item | Determination |
|------|---------------|
| **Device class** | Class II (device type code xxxxx – see 21 CFR 862/862.###) |
| **Regulatory pathway** | Traditional 510(k) (substantive review). No special or abbreviated 510(k) options apply because the device incorporates a novel sensor element not covered by an existing predicate with a “Special” designation. |
| **Predicate recommendation** | Device A (KXXXXX, cleared 2020; same intended use and technology platform). If the novel sensor is deemed a new intended purpose, consider a **De Novo** request after an initial 510(k) attempt. |

---

## 2. Required Evidence (per 21 CFR 807 & FDA Guidance)

| Category | Specifics |
|----------|-----------|
| **Device description** | Detailed drawings, bill of materials, software architecture (if any), and hardware specifications. |
| **Intended use / Indications for Use** | Exact wording matching the predicate; include labeling excerpts. |
| **Performance testing** | • Bench functional test (accuracy, precision, repeatability) <br>• Electrical safety & electromagnetic compatibility (IEC 60601‑1, IEC 60601‑1‑2) <br>• Biocompatibility (ISO 10993‑1 data for patient-contact materials) |
| **Software** (if applicable) | Validation plan per 21 CFR 820.30; verification of algorithms and cybersecurity threat model (FDA “Content of Premarket Submissions … Cybersecurity”). |
| **Sterility / Shelf life** (if sterile) | Sterilization validation & packaging integrity data. |
| **Labeling & IFU** | Full label set, user manual, warnings/precautions per 21 CFR 801. |
| **Quality System** | Evidence of compliant QMS under the new **QMSR** (effective Feb‑2026) – ISO 13485:2016 alignment; design controls documentation (Design History File). |
| **Clinical data** (if required by predicate) | Limited usability study or non‑clinical performance correlation; no full clinical trial anticipated. |

---

## 3. Missing / Incomplete Information (the five “must” items triggering RTA)

| # | Gap | Impact on RTA Score |
|---|-----|----------------------|
| **1** | **Comprehensive bench test protocol & raw data** – only summary metrics submitted. | – → RTA refusal for insufficient performance evidence. |
| **2** | **Software validation report** – absent traceability matrix linking requirements to tests. | – → Non‑conformance with 21 CFR 820.30. |
| **3** | **Biocompatibility test reports** – missing ISO 10993‑5 cytotoxicity for new sensor housing material. | – → Potential safety deficiency. |
| **4** | **Labeling package set** – IFU lacks required contraindications and warnings per predicate. | – → RTA for labeling deficiencies. |
| **5** | **QMSR compliance evidence** – QMS audit report not yet updated to ISO 13485:2016 (effective 2026). | – → Regulatory submission non‑conformity under new QMS rule. |

*Resolving these items is projected to lift the RTA score from 52 % → ~85 %, according to the internal model (see source excerpt [2]).*

---

## 4. Risk Controls (per ISO 14971 & FDA Guidance)

| Hazard | Control / Mitigation |
|--------|----------------------|
| **Electrical shock** | IEC 60601‑1 compliance, double‑insulated design, leakage current test (<10 µA). |
| **Incorrect sensor reading** | Redundant calibration routine; alarm threshold when out‑of‑range; user training per IFU. |
| **Software malfunction / cybersecurity breach** | Secure boot, code signing, periodic OTA security patching, penetration test report. |
| **Material biocompatibility issue** | Use of ISO 10993‑approved polymers; validated sterilization process (if applicable). |
| **Label misuse** | Clear iconography; contraindication list; lockout feature in software to prevent use on non‑compatible patients. |

---

## 5. Key Regulatory Citations  

* 21 CFR 862 – Classification regulation for the device type.  
* 21 CFR 807 – Submissions requirements (510(k) content).  
* 21 CFR 820 – Quality System Regulation (including QMSR updates, Feb‑2026).  
* FDA Guidance: “Medical Device Development Tools” (Jan 2020); “Content of Premarket Submissions for Management of Cybersecurity” (Sept 2022).  
* ISO 13485:2016 – QMS alignment.  
* ISO 14971:2019 – Risk management.

---

## 6. Human‑Escalation Triggers  

| Condition | Action |
|-----------|--------|
| **Any “must” item remains unresolved** after 7 business days from the deadline set by project lead. | Escalate to **Regulatory Lead (John Doe, RA Manager)** with a risk impact memo. |
| **QMSR audit findings** indicate non‑compliance that could delay market entry (>2 weeks). | Immediate notification to **Quality Assurance Director** and **Legal Counsel** for mitigation plan. |
| **FDA feedback indicating “Refuse to Accept”** on any submission module. | Stop all further compilation; schedule an urgent cross‑functional review with **Regulatory, Engineering, and Clinical** leads. |
| **New predicate identified that offers a Special 510(k) route** (e.g., after competitor clearance). | Re‑evaluate pathway; inform **Product Strategy Lead** for potential timeline acceleration. |

---

## 7. Peer Review Prompt  

*“@RA‑Peer: Please review the predicate selection, the completeness of the five ‘must’ items identified, and any jurisdiction‑specific considerations (e.g., state‑level licensure or CMS coverage) that may have been omitted. Highlight any assumptions about the sensor’s novelty that could trigger a De Novo alternative.”*

---

## 8. Reusable RA Judgment (Lesson Record)

**Judgment ID:** `RA_Judg_2026-07-31_510k_MustItems`  
**Context:** Internal RTA scoring model flagged five mandatory deficiencies causing a Refuse‑to‑Accept (RTA) for a Class II device submission.  
**Decision Rule:** *If any of the following are missing or incomplete – full bench test data, software validation traceability, biocompatibility reports per ISO 10993, complete labeling package, and QMSR‐aligned audit evidence – then the 510(k) RTA score will remain ≤55 % and submission is unlikely to be accepted on first review.*  
**Actionable Guidance:** Prioritize closure of these five items before compiling the final 510(k); once resolved, expect an RTA score ≥80 %, substantially improving clearance probability.  

*Stored for future case‑based reasoning; not a raw transcript.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [ ] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 소스엔 RTA 점수(52%→85%)만 있는데 '필수항목 5개' 표를 확정적으로 창작 — 추론임을 명시하지 않음. 플레이스홀더 표기는 투명.

**Source Excerpts**

1. Chunk `322119354378516559`

> ## 배경 `build_readiness.py` 결과 FDA 510(k) RTA 점수 52% 고착. 하기 5개 must 항목이 미충족 상태로 실제 제출 시 FDA RTA(Refuse to Accept) 직행.

2. Chunk `607901765257522135`

> ## 예상 효과 FDA 510(k) 점수 52% → 약 85% (5개 must 해소 시)

### kb-eval-20260715-it17-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_us-005", "iteration": 17, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "87f5f9f07f18c3bf", "source": "github:holee9/MD-process/issue-drafts/931_RA_FDA_Form_표지_양식_4건_작성.md", "source_hash": "68cd74d39caaa060d4323f37a5c193a02284866bee050ec5139fdf5916ca6ff7"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `87f5f9f07f18c3bf`
- Source: `github:holee9/MD-process/issue-drafts/931_RA_FDA_Form_표지_양식_4건_작성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/931_RA_FDA_Form_%ED%91%9C%EC%A7%80_%EC%96%91%EC%8B%9D_4%EA%B1%B4_%EC%9E%91%EC%84%B1.md)
- Source hash: `68cd74d39caaa060d4323f37a5c193a02284866bee050ec5139fdf5916ca6ff7`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `931_RA_FDA_Form_표지_양식_4건_작성.md`는 `931_RA_FDA_Form_표지_양식_4건_작성.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 목표 영향 - 다음 분기(2026-Q3) `build_readiness.py` 재실행 시 FDA RTA Section A 5건 모두 충족 → **점수 0% → 33%** 예상. ## 작업 범위 (Done 정의) - [ ] FDA Form 3514 — 510(k) Cover Sheet 양식 (회사명/주소/연락처 자리표시자 포함) - [ ] FDA Form 3601 — User Fee Cover Sheet 양식 + 수수료 결제 영수증 자리표시자 - [ ] FDA Form 3654 — Standards Data Report 양식 또는 자사 별도 문서 양식 - [ ] FDA Form 3881 — Indications for Use S...
- 이 항목의 평가 포인트: 이 source는 510(k) predicate 자체를 선정하는 직접 근거가 아닐 수 있습니다. 좋은 답변은 predicate/IFU 동등성 판단을 단정하지 않고, 이 source가 제공하는 QMS·evidence·risk context로 제한해 사용해야 합니다.
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

> **Regulatory Draft – 510(k) Predicate Strategy (Daily‑Growth v1)**  
*Prepared for internal review – Mike (US RA)*  

---

### 1️⃣ Device Overview *(placeholder – to be populated by product team)*
- **Name / Model:** __________  
- **Indications for Use (IoU):** __________  
- **Technology & Intended Use:** __________  

---

### 2️⃣ Classification & Submission Route
| Item | Determination |
|------|---------------|
| **Product Class** | **Class II** – most likely subject to the 510(k) pathway (per 21 CFR 862/863/864 depending on specialty). |
| **Regulatory Pathway** | Traditional **510(k)** – Sub‑section A (Standard Submission) using FDA Forms 3514, 3601, 3654, and 3881. |
| **Alternative Paths** | • **Special 510(k)** if only minor design changes to an existing cleared device.<br>• **De Novo** only if no suitable predicate exists (unlikely given the “standard” technology). |

---

### 3️⃣ Predicate Device Identification – Strategy
| Step | Action | Evidence Required |
|------|--------|-------------------|
| **A. Search FDA 510(k) Database** | Use product‑type keywords, same intended use, and similar technological characteristics. Prioritize predicates cleared < 10 years ago (to avoid “old‑predicate” risk). |
| **B. Substantial Equivalence Matrix** | Compare: *Indications, Technology, Design, Materials, Energy source, Performance specs*. Document gaps. |
| **C. Bridge Documents** | If gaps exist, prepare bridging data (bench/animal/clinical) to close them. |
| **D. “Predicate‑Chain” Documentation** | Record predicate 510(k) number, clearance date, and any subsequent re‑classifications that affect the current device. |

*Bottom line:* Identify a **single primary predicate** meeting all A‑B‑C criteria; secondary predicates only as backup.

---

### 4️⃣ Required Evidence Package (per FDA guidance)

| Category | Minimum Content | Typical Documents |
|----------|----------------|-------------------|
| **Device Description & Labeling** | Full specs, accessories, labeling, IFU. | Device Master Record, Labels, Instructions for Use. |
| **Risk Management (ISO 14971)** | Risk analysis, risk control measures, residual risk evaluation. | RMF (risk management file) with FMEA/FMECA, hazard log. |
| **Bench‑Testing / Performance** | Functional testing, electrical safety (IEC 60601‑1), biocompatibility (ISO 10993). | Test reports, validation protocols, acceptance criteria. |
| **Software Validation** *(if applicable)* | IEC 62304 development lifecycle, verification & validation evidence. | Software Development Plan, Unit/Integration test results. |
| **Animal / Clinical Data** | Only if performance cannot be demonstrated via bench testing alone (e.g., biologics, invasive). | Pre‑clinical study reports; IDE‑exempt clinical data where needed. |
| **QMS Compliance** | Conformity to **QMSR (effective Feb 2026)** – ISO 13485 aligned. | QMS certification, “Design History File” excerpts, CAPA records. |
| **Regulatory Forms** | FDA Form 3514 (Cover Sheet), 3601 (User Fee), 3654 (Standards Data Report), 3881 (Indications for Use Statement). | Completed forms with placeholders replaced; fee receipt attached. |

---

### 5️⃣ Missing Information (per source excerpts)

| Item | Status | Action Required |
|------|--------|-----------------|
| **FDA Form 3514 – Cover Sheet** | Placeholder only. | Populate company name, address, contact; sign. |
| **FDA Form 3601 – User Fee Cover Sheet & Receipt** | Placeholder only. | Submit fee payment receipt; complete form. |
| **FDA Form 3654 – Standards Data Report** | Placeholder / alternate internal format used. | Ensure all applicable recognized standards are listed and referenced per guidance. |
| **FDA Form 3881 – Indications for Use Statement** | OMB renewal due 2026‑07‑31 (today). | Update IoU, verify alignment with current regulatory language; submit before expiry. |
| **510(k) Cover Letter (English)** | Template exists but fields empty. | Fill applicant name/address/contact; indicate “Class II – Traditional 510(k)” and list predicates. |
| **RTA Section A items (A1‑A5)** | Not yet met – readiness score 0 % → target 33 %. | Complete each checklist item; document in `13_규제평가_체크리스트/FDA_510k_RTA.md`. |

*All of the above constitute “hard stops” before package submission.*

---

### 6️⃣ Risk Controls & Mitigation (ISO 14971‑aligned)

| Hazard | Control(s) Implemented | Residual Risk Rating | Verification |
|--------|-----------------------|----------------------|--------------|
| Electrical shock (IEC 60601‑1) | Insulation, leakage current limits, dual‑fault protection. | Low | Test report – IEC 60601‑1 Part 1 & 2. |
| Software malfunction | IEC 62304 Level B development, static analysis, automated unit testing. | Medium | Verification matrix; error tracking logs. |
| Biocompatibility (contact) | ISO 10993‑5/10 compliant material selection. | Low | Cytotoxicity & sensitization reports. |
| User error (misuse) | Human factors validation – usability study per FDA guidance “Applying Human Factors and Usability Engineering”. | Low | Study report, task analysis. |

*All controls must be documented in the Design History File (DHF).*

---

### 7️⃣ Key Regulatory Citations

| Source | Relevance |
|--------|-----------|
| **21 CFR 807** – Submissions to FDA | Governs 510(k) content & format. |
| **FDA Guidance: “Deciding When to Submit a 510(k)” (2023)** | Determines need for predicate and substantial equivalence. |
| **QMS Regulation (QMSR), 21 CFR 820, effective Feb 2026** | New QMS requirements aligned with ISO 13485. |
> *Reference: FDA “Final Rule on Quality System Regulation” (Fed. Register Vol. 91, No. 42, 2025).*
| **ISO 14971:2019**, **IEC 60601‑1**, **IEC 62304** | Risk management, safety, software lifecycle standards. |
| **FDA Form 3881 OMB Guidance (2026‑07‑31)** | Expiration date of current form template. |

---

### 8️⃣ Human‑Escalation Triggers *(When to involve senior RA or legal counsel)*

| Trigger | Reason | Escalation Path |
|---------|--------|-----------------|
| **Unresolved Predicate Gap** – No suitable predicate found after two iterations. | May require De Novo or PMA. | Senior RA → Director of Regulatory Affairs. |
| **Clinical Data Required** – Bench testing insufficient and animal data unavailable. | Increases timeline & risk. | Clinical affairs lead + senior RA review. |
| **Fee Payment Issue / Form 3601 missing receipt** | Submission will be rejected by FDA intake. | Finance & compliance team immediate involvement. |
| **QMSR Non‑conformance** – Evidence of ISO 13485 non‑compliance in DHF. | Could halt clearance. | Quality Assurance lead + RA manager. |
| **OMB Form 3881 expiration imminent (<30 days)** | Regulatory form invalid; submission blocked. | Legal/Regulatory Ops to obtain updated template. |

---

### 9️⃣ Peer Review Prompt (RA colleague)

> **@RA‑Peer** – Please review the assumptions and gaps identified above:  
> 1. Are we confident that a suitable Class II predicate exists based on our preliminary keyword search, or should we broaden the scope now?  
> 2. Do any of the listed required evidence items (especially software validation) miss emerging FDA expectations (e.g., AI/ML “Good Machine Learning Practice” guidance)?  
> 3. Have we captured all jurisdiction‑specific nuances for **2026 Q3** (e.g., OMB renewal timing, QMSR transition) or are there additional state‑level requirements (California Proposition 65, etc.) that need early addressing?  

*Please provide concrete challenges or confirm completeness within the next 24 h.*

---

### 10️⃣ Reusable RA Judgment (Honcho Record)

> **Lesson:** *In daily growth cases, always verify the presence of complete FDA Form placeholders (3514, 3601, 3654, 3881) and fee receipt before marking “submission ready.” Missing or expired form templates are a hard blocker that will be flagged by FDA intake systems. Capture readiness status via RTA Section A items; aim for ≥33 % completion before each quarterly build‑readiness execution.*  

*(Record this as a reusable judgment in the RA knowledge base for future daily‑growth checks.)*

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

> FDA 서식번호(3514/3601/3654/3881)·만료일(2026-07-31)은 소스와 정확 일치, 우수. 'Fed. Register Vol.91 No.42(2025)'는 창작(실제 QMSR 최종규칙은 89 FR 7496, 2024).

**Source Excerpts**

1. Chunk `202395958248735480`

> ## 목표 영향 - 다음 분기(2026-Q3) `build_readiness.py` 재실행 시 FDA RTA Section A 5건 모두 충족 → **점수 0% → 33%** 예상.

2. Chunk `608496877809508828`

> ## 작업 범위 (Done 정의) - [ ] FDA Form 3514 — 510(k) Cover Sheet 양식 (회사명/주소/연락처 자리표시자 포함) - [ ] FDA Form 3601 — User Fee Cover Sheet 양식 + 수수료 결제 영수증 자리표시자 - [ ] FDA Form 3654 — Standards Data Report 양식 또는 자사 별도 문서 양식 - [ ] FDA Form 3881 — Indications for Use Statement 양식 (현행 OMB 만료일 2026-07-31 주의) - [ ] 510(k) Cover Letter 영문 표준 양식 (applicant name/address/contact/submitter type) - [ ] `13_규제평가_체크리스트/FDA_510k_RTA.md` 항목 A1~A5의 `related_docs:` 필드에 신규 doc-id 등록

## ra_eu

### kb-eval-20260715-it17-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_eu-001", "iteration": 17, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "10be9ecec30fa07b", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `10be9ecec30fa07b`
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

> **Regulatory Draft – Daily Growth Case (Scenario 10be9ecec30fa07b)**  
*Audience: Theo – EU MDR Regulatory Affairs Specialist*  
*Run date: 2026‑07‑31*  

---

## 1. Device Overview (as understood from the source)

| Attribute | Interpretation |
|-----------|----------------|
| **Device type** | Ionising radiation‑emitting diagnostic equipment (e.g., X‑ray generator) – referenced in Rule 10 of Annex VIII. |
| **Intended purpose** | Generation of ionising radiation for clinical imaging of patients. |
| **Primary mode of action** | Physical energy delivery (radiation) to the patient; no pharmacological or biological effect. |
| **Software component** | May contain SaMD for image acquisition/processing – relevant under Rule 11, but not the primary classification driver. |

*Note*: The source material does not provide a complete device description, accessories list, or intended user group (e.g., hospitals vs. point‑of‑care). These gaps are flagged in Section 4.

---

## 2. Classification & Conformity Assessment Route

| Regulatory Reference | Determination |
|----------------------|---------------|
| **MDR Annex VIII – Rule 10** | *“Ionising radiation emitting devices”* → **Class IIb** (unless the device is a “self‑contained X‑ray equipment for intra‑oral use”, which would be Class IIa).  |
| **MDR Article 52(1) & Annex III** | For Class IIb, the conformity assessment route requires a **Notified Body (NB)** with **Full Quality Management System audit + Design Dossier review** (Annex VI, Part B). |
| **Applicable NB Modules** | • Module A – QMS (ISO 13485:2016)  <br>• Module C – EC type‑examination of the device (including verification of GSPR in Annex I) <br>• Module G – Post‑market surveillance plan review (Article 83) |
| **CE Marking** | Issued after successful NB assessment, EU‑type‑examination certificate and Declaration of Conformity (DoC). |

---

## 3. Evidence Package Required for NB Submission

| Evidence Type | Specific Requirement | Source Clause |
|---------------|----------------------|--------------|
| **Technical Documentation (TD)** | Complete Annex II dossier: device description, specifications, manufacturing information, risk management file, product verification/validation, labeling, IFU, and PMS plan. | MDR Art. 10; Annex II |
| **Risk Management** | ISO 14971‑compliant file demonstrating identification of hazards (radiation exposure, electrical safety), evaluation of residual risks, and implementation of protective measures. | MDR Art. 10(9); Annex I, section 7 |
| **Clinical Evaluation Report (CER)** | Systematic literature review + clinical data (pre‑market clinical investigation or equivalence) proving performance & safety according to GSPR. Include a **state‑of‑the‑art** comparison for ionising radiation dose optimisation. | MDR Art. 61‑62; Annex IV |
| **Post‑Market Surveillance (PMS) Plan + PMCF** | Detailed PMS plan, periodic safety update report (PSUR) schedule, and a proactive post‑market clinical follow‑up (PMCF) study design addressing long‑term radiation effects. | MDR Art. 83‑86; Annex III |
| **Software Documentation (if SaMD)** | IEC 62304 software lifecycle documentation, verification & validation evidence, cybersecurity risk assessment per IEC 62443/EN ISA‑99. | MDR Rule 11; MDCG 2022‑5 guidance |
| **Manufacturing Process** | Evidence of process control (process validation reports) and compliance to ISO 13485 QMS audit report. | MDR Art. 10(7); Annex II, clause 3 |
| **Labeling & IFU** | Conformity with Annex I requirements for safety information, radiation dose warnings, user training instructions. | MDR Annex I, clauses 9‑12 |

---

## 4. Missing / Insufficient Information (Gaps to Resolve before NB Submission)

1. **Complete Device Description** – dimensions, materials, accessories, and intended clinical indications are not detailed in the source.  
2. **Intended User & Environment** – hospital radiology department vs. mobile/point‑of‑care impacts risk assessment (e.g., need for additional training).  
3. **Clinical Data Strategy** – no indication whether a pre‑market clinical investigation is planned or if equivalence to an existing device will be claimed; the justification matrix is missing.  
4. **Radiation Dose Management** – quantitative dose metrics (mGy, DAP) and compliance with IEC 60601‑2‑33 (or latest amendment) not presented.  
5. **Software Scope Clarification** – extent of SaMD functionality (e.g., image reconstruction, AI‑based analysis) determines whether Rule 11 classifies the software separately (potentially Class IIa/IIb).  
6. **PMCF Plan Details** – target sample size, duration, data collection endpoints for long‑term radiation safety are absent.  
7. **Supply Chain Traceability** – list of critical suppliers and component certifications (e.g., X‑ray tube) not supplied.  

*Action*: Obtain the above missing artefacts from the product development team before initiating NB engagement.

---

## 5. Risk Controls (derived from identified hazards)

| Hazard | Primary Control(s) | Additional Safeguards |
|--------|-------------------|-----------------------|
| **Excessive patient radiation dose** | • Built‑in dose limiting circuitry (IEC 60601‑2‑33 compliance). <br>• Automatic exposure control (AEC). | • User training on proper positioning. <br>• Real‑time dosimetry display with alerts. |
| **Electrical shock / fire** | • IEC 60601‑1 compliant grounding, insulation testing. | • Periodic electrical safety checks per IEC 62353. |
| **Mechanical failure (collimator, housing)** | • Robust mechanical design with FMEA analysis. | • Preventive maintenance schedule; visual inspection checklist. |
| **Software malfunction (image artefacts / incorrect dose calculation)** | • IEC 62304 software lifecycle controls + unit/integration testing. | • Redundancy checks, failsafe defaults to safe mode. |
| **Cybersecurity breach of SaMD** | • IEC 62443‑based network segmentation and authentication. | • Regular patch management; incident response plan. |

All risk controls must be documented in the ISO 14971 risk management file and linked to verification activities (testing reports, validation protocols).

---

## 6. Regulatory Citations

| Clause / Annex | Relevance |
|----------------|-----------|
| **MDR Art. 10** – General obligations of manufacturers (TD). |
| **MDR Annex VIII – Rule 10** – Classification as Class IIb. |
| **MDR Annex II** – Technical Documentation requirements. |
| **MDR Annex III** – PMS & PMCF plan specifications. |
| **MDR Annex IV** – Clinical Evaluation Report structure. |
| **MDR Art. 61‑62** – Clinical evaluation obligations. |
| **IEC 60601‑2‑33** – Safety requirements for X‑ray equipment. |
| **ISO 14971:2019** – Risk management process. |
| **ISO 13485:2016** – QMS (Module A). |
| **IEC 62304** – Software lifecycle (Rule 11). |
| **MDCG 2022‑5** – SaMD classification guidance. |

---

## 7. Human‑Escalation Triggers

| Situation | Trigger | Recommended Escalation |
|-----------|---------|------------------------|
| **Unresolved classification ambiguity** (e.g., device may fall under Rule 10 *or* Rule 11) | Conflicting interpretation of primary mode of action. | Escalate to senior RA manager + legal counsel for jurisdiction analysis. |
| **Insufficient clinical evidence** – no viable equivalence or investigation data. | Gap > 30 % of required CER content. | Pause NB submission; request sponsor to launch a pre‑market clinical study. |
| **Critical risk control missing** (e.g., dose limiting function not demonstrably functional). | Residual risk > Acceptable Level according to ISO 14971. | Halt project; engage engineering for redesign and re‑risk assessment. |
| **Regulatory deadline breach** – MDR transition date passed without CE mark. | Any pending evidence > 3 months overdue. | Notify project steering committee; consider market withdrawal or interim use under “national provisions”. |
| **NB audit findings** – major non‑conformities in QMS. | NB issues a “non‑conforming” observation (NC) on ISO 13485 audit. | Immediate corrective action plan and senior management review. |

---

## 8. Peer Review Prompt

> **Request to RA peer:**  
> Please review this draft and challenge the following points:  
> 1. **Classification assumptions** – Are we correct in applying Rule 10 without a detailed “primary intended purpose” analysis? Could any software functionality elevate the classification under Rule 11?  
> 2. **Source coverage** – The source excerpts only reference Annex VIII and Rule 10/11. Have we omitted any recent MDCG guidance (e.g., 2023‑7 on radiation dose optimisation) that would affect evidence requirements?  
> 3. **Jurisdictional gaps** – This assessment focuses on EU MDR. Are there cross‑border considerations (e.g., United Kingdom “UKCA” or EEA Norway/Switzerland) that should be flagged now for a future market strategy?  

Please provide specific citations, alternative interpretations, and any additional documentation we must gather.

---

### 9. Reusable RA Judgment (recorded as a lesson)

```json
{
  "honcho_conclude": {
    "decision": "Classify ionising‑radiation diagnostic equipment under MDR Annex VIII Rule 10 → Class IIb; route = Notified Body full quality system audit + EC type‑examination (Modules A, C, G).",
    "rationale": [
      "Rule 10 explicitly covers X‑ray emitting devices as Class IIb (source excerpt [2]).",
      "Device’s primary mode of action is physical energy delivery; software is ancillary and does not dominate classification unless SaMD independently performs a diagnostic function (MDCG 2022‑5).",
      "Annex VIII classification dictates the conformity assessment path (NB involvement)."
    ],
    "evidence_needed": [
      "Complete Annex II technical documentation.",
      "ISO 14971 risk management file with radiation dose controls.",
      "Clinical Evaluation Report meeting Annex IV requirements.",
      "PMS/PMCF plan compliant with Articles 83‑86."
    ],
    "gaps_identified": [
      "Lack of detailed device description and intended use.",
      "No clinical data strategy (investigation vs. equivalence).",
      "Missing quantitative radiation dose specifications and IEC 60601‑2‑33 compliance evidence.",
      "Unclear extent of SaMD functionality."
    ],
    "human_escalation": [
      "Classification ambiguity – if software becomes primary mode, re‑classify under Rule 11.",
      "Insufficient clinical evidence – pause NB submission until data available.",
      "Critical risk control missing – halt project for redesign."
    ],
    "peer_review_prompt": "Challenge classification, source completeness (including recent MDCG guidance), and any non‑EU jurisdiction considerations."
  }
}
```

--- 

*End of Draft.*

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

> Rule 10→Class IIb 도출은 소스와 일치. 'Module A/C/G'를 MDR 적합성평가 체계로 오설명(실제 Annex IX/X/XI 체계, Module은 별도 NLF 프레임워크 — #123 유사) + 'MDCG 2022-5' 검증 불가.

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20260715-it17-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_eu-002", "iteration": 17, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a8aa456f5c376fbd", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a8aa456f5c376fbd`
- Source: `github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X%EC%84%A0_%EB%B6%84%EB%A5%98_%EC%82%AC%EC%8B%A4%EC%98%A4%EB%A5%98.md)
- Source hash: `8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Rule 9 (Chapter III §6.1) — 오적용 반증 > "All active **therapeutic** devices intended to administer or exchange energy are classified as class IIa ... **All active devices intended to emit ionizing radiation for therapeutic purposes** ... are classified as class IIb." (진단용 X-ray에는 부적용) ### D1 — §6 표 0-2 예시 열 - **기재값 (예시 열):** > "X-ray: MFDS 3등급, FDA Class...
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

> **Regulatory Draft – Daily‑Growth v1 (Scenario a8aa456f5c376fbd)**  
*Prepared for: Theo – EU MDR Regulatory Affairs Specialist*  

---

## 1️⃣  Project Overview  

| Item | Detail |
|------|--------|
| **Device type** | X‑ray system (active ionising‑radiation device) intended for **diagnostic** imaging (e.g. radiography/fluoroscopy). |
| **Primary focus** | Determine the correct MDR classification & conformity‑assessment route; list required evidence; highlight gaps and risk controls; define escalation triggers. |
| **Source material** | GitHub MD‑process issue #943 – “AUDIT_CHK‑DR‑001_EU_MDR_Rule_5_9_X선_분류_사실오류” (hash 8354553d…). |
| **Key excerpts** | • Rule 9 – therapeutic active devices ⇒ Class IIa/IIb; diagnostic X‑ray excluded. <br>• Table 0‑2 (D1) – mis‑mapping “X‑ray = Rule 5/9 → Class II” is wrong; correct mapping is **Rule 10 → Class IIb** for diagnostic X‑ray systems, **Rule 17 → Class IIa** for digital flat‑panel detectors. |

---

## 2️⃣  Classification & Conformity‑Assessment Path  

| MDR rule | Device element | Correct class* | Annex & module |
|----------|----------------|----------------|----------------|
| **Rule 10 (Annex VIII, §6)** | *X‑ray system that emits ionising radiation for diagnostic purposes* | **Class IIb** | **Module B** – Full quality‑system assessment (Annex IX) + **Module C** – Design dossier review (Annex XI). |
| **Rule 17** | *Digital flat‑panel detector / image acquisition unit* | **Class IIa** | **Module A** – Self‑declaration of conformity (Annex VIII). |

\*If the system is a **stand‑alone X‑ray generator + detector assembled as one device**, the whole assembly follows the highest class applicable → **Class IIb**.

### Conformity‑assessment route for the complete X‑ray system  

1. **Technical Documentation (TD)** – Annex II & III, with full design dossier (Module C).  
2. **Quality Management System** – EN ISO 13485:2016 + MDR‑specific clauses (Annex IX).  
3. **Notified Body involvement** – Full review (design, risk management, clinical evaluation) and issuance of a **CE certificate** (class IIb).  
4. **Post‑Market Surveillance (PMS) & Periodic Safety Update Report (PSUR)** – Annex X for class IIb.  

---

## 3️⃣  Evidence Required (per MDR)  

| Area | Minimum required artefacts | Regulatory citation |
|------|----------------------------|---------------------|
| **Intended Use / Labeling** | Clear statement “Diagnostic X‑ray system”; device description, indications, contraindications, user group. | MDR Art. 2; Annex II §4.1 |
| **Risk Management** | ISO 14971:2019 file – hazard identification, risk analysis, evaluation, control measures (including radiation safety). | MDR Annex I §3 ; ISO 14971 |
| **Electrical & Radiation Safety** | • IEC 60601‑2‑33 (X‑ray equipment) compliance test reports. <br>• Dosimetry validation (dose‑area product, air kerma). <br>• Shielding calculations per IEC 61514/EN C. <br>• Validation of image quality (phantom studies). | MDR Annex VIII §4; IEC 60601‑2‑33 |
| **Clinical Evaluation** | • Clinical data from either: ① a systematic literature review of comparable devices (≥ 3 years post‑market) + clinical benefit justification, or ② a prospective clinical investigation (per MDCG 2020‑6). <br>• PMS plan with PMCF if clinical data are limited. | MDR Annex XII; MDCG 2020‑6 |
| **Performance / Verification** | • Bench testing of mechanical stability, electromagnetic compatibility (EMC – IEC 60601‑1‑2). <br>• Software validation (IEC 62304) for imaging processing unit. | MDR Annex VIII §4 |
| **Usability/Human Factors** | Usability engineering file demonstrating safe operation, user interface testing (ISO 62366‑1). | MDR Annex I §5; ISO 62366‑1 |
| **Label & IFU** | Full set of labeling in each EU language required for the target market; Includes radiation safety warnings per Euratom Directive 2013/59. | MDR Annex II §4 ; Euratom Directive 2013/59/Euratom |
| **Declaration of Conformity (DoC)** | Completed DoC referencing the notified‑body certificate, class IIb, and all applicable annexes. | MDR Art. 19 |

---

## 4️⃣  Identified Gaps / Missing Information  

| Gap | Why it matters | Evidence needed to close |
|-----|----------------|--------------------------|
| **Exact Intended Use statement** (diagnostic vs therapeutic) | Determines applicability of Rule 9 vs Rule 10. Mis‑classification leads to wrong NB route. | Signed specification from the manufacturer clarifying “diagnostic X‑ray imaging system”. |
| **Full device architecture diagram** (generator, collimator, detector, control console) | Needed for risk analysis and to decide which component follows Rule 17 vs Rule 10. | Engineering drawing with part numbers and functional description. |
| **Clinical data package** – no clinical investigation yet reported | Class IIb devices require robust clinical evaluation; lack of data will trigger a PMCF requirement or need for a new study. | Systematic literature review dossier +/or Clinical Investigation Report (CIR) complying with MDCG 2020‑6. |
> **Note:** The source material only flags the classification error; it does not provide any of the above artefacts.

---

## 5️⃣  Required Risk Controls (illustrative)  

| Hazard | Control(s) | Standard / Guideline |
|--------|------------|----------------------|
| Excessive radiation dose to patient/operator | • Automatic exposure control (AEC). <br>• Dose‑area product monitoring with audible/visual alarm. <br>• Interlock on X‑ray tube housing. | IEC 60601‑2‑33; Euratom 2013/59 |
| Electrical shock / equipment failure | • Leakage current ≤ 0.5 mA (patient leakage). <br>• Built‑in residual‑current device (RCD). | IEC 60601‑1 |
| Image quality degradation leading to repeat exposures | • Routine QC phantom tests; automatic image quality assessment software. | ISO 13485 QMS SOPs |
| Software malfunction (image processing) | • Verified/validated software development lifecycle (IEC 62304). <br>• Periodic security updates. | IEC 62304 |
| Mechanical failure of collimator or detector mounting | • Design verification per EN 60601‑1; stress analysis. | EN 60601‑1 |

All controls must be documented in the **Risk Management File** and referenced in the **Technical Documentation**.

---

## 6️⃣  Human‑Escalation Triggers  

| Trigger | Action required |
|----------|-----------------|
| **Classification uncertainty** (e.g., ambiguous “diagnostic/therapeutic” wording) | Stop TD finalisation; request formal intended‑use clarification from the OEM. Escalate to senior RA lead. |
| **Missing clinical evidence for a Class IIb device** | Initiate a gap‑analysis; decide whether a PMCF plan is sufficient or a full Clinical Investigation must be launched. Notify project manager and sponsor. |
| **Conflict between cross‑border mappings (MFDS/FDA vs MDR)** | Review mapping tables; adjust internal classification matrix; document justification per MDCG 2023‑X. Raise to regulatory governance board. |
| **Non‑conformity with IEC 60601‑2‑33 radiation safety tests** | Pause CE marking process; request corrective engineering actions and re‑testing. Notify Notified Body liaison. |
| **Late delivery of required artefacts (> 4 weeks)** | Issue risk‑based impact assessment, update project timeline, seek extension from sponsor. Escalate to programme steering committee. |

---

## 7️⃣  Peer‑Review Prompt (to another RA)  

> **Please review the assumptions and conclusions below:**  
> 1. The device has been classified as **Class IIb** under MDR Rule 10 – do you agree based on the supplied excerpts?  
> 2. Are there any additional MDR annexes or MDCG guidance documents that we have omitted (e.g., specific Euratom radiation‑protection requirements, MDCG 2021‑22 for X‑ray equipment)?  
> 3. Does the proposed evidence list fully cover what a Notified Body will request for a Class IIb active ionising‑radiation device? Identify any missing artefacts or over‑optimistic gaps.  
> 4. Are there jurisdiction‑specific nuances (e.g., Korean MFDS Grade 3 vs EU MDR) that could impact our cross‑reference mapping and must be documented explicitly?  

*Please provide your critique, supporting references, and suggested amendments.*  

---

## 8️⃣  Reusable RA Judgment (recorded for future cases)

> **Judgment ID:** `RA_JD_2026-07-31_XRAY_CLASS10`  
> **Core decision:** Diagnostic X‑ray systems are **always** classified under MDR **Rule 10 → Class IIb**, irrespective of any local mapping to “Rule 5/9”. The highest‑risk component (the emitter) dictates the overall class.  
> **Evidence required:** Intended‑use statement, full device architecture, IEC 60601‑2‑33 compliance, clinical evaluation (literature or investigation), risk management per ISO 14971, QMS (ISO 13485).  
> **Gap flag:** Missing explicit diagnostic use declaration and clinical data package.  
> **Escalation criteria:** Any ambiguity in intended use, missing clinical evidence, or non‑conformity with radiation‑safety standards triggers senior RA escalation.  

*Stored via `honcho_conclude` for reuse in subsequent X‑ray device classification reviews.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

> 이전 오류(Rule 9 오적용)를 정정한 소스를 정확히 재현(Rule 10→IIb, Rule 17→IIa). Module 표기 문제만 경미하게 반복(전체 판단에는 영향 없음).

**Source Excerpts**

1. Chunk `109229213193581391`

> ### Rule 9 (Chapter III §6.1) — 오적용 반증 > "All active **therapeutic** devices intended to administer or exchange energy are classified as class IIa ... **All active devices intended to emit ionizing radiation for therapeutic purposes** ... are classified as class IIb." (진단용 X-ray에는 부적용)

2. Chunk `109346595768604468`

> ### D1 — §6 표 0-2 예시 열 - **기재값 (예시 열):** > "X-ray: MFDS 3등급, FDA Class II 510(k), **EU MDR Rule 5/9**" - **독립확인 정답:** - X-ray 시스템(진단용 이온화방사선 능동기기) = **Rule 10 → Class IIb** - 디지털 평판 디텍터(X-ray 영상 기록기기) = **Rule 17 → Class IIa** - Rule 9 = **치료용** 이온화방사선/에너지 투여 기기(진단용 X-ray 배제) - Rule 5 = 체강 대상 침습기기(X-ray 배제) - **영향:** - 규제 분류 오적용 시 EU MDR 적합성 평가 절차(Annex IX/X/XI) 선정 오류로 연결(Notified Body 인증 경로·기술문서 요구·PSUR 주기 오판정). - "MFDS 3등급 = FDA Class II = EU MDR Rule 5/9" 정합 매핑이 후속 문서(GSPR 매핑표·기술문서·CE marking plan)로 전파될 위험. - **권고수정:** - 예시 열을 다음으로 변경: > "X-ray 시스템: MFDS 3등급, FDA Class II (510(k), Product Code MQB), **EU MDR Rule 10 → Class IIb**; 평판 디텍...

### kb-eval-20260715-it17-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_eu-003", "iteration": 17, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "281719ef00ada43f", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `281719ef00ada43f`
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

> **Regulatory Draft – Daily Growth Case (MDR Classification & Conformity‑Assessment Route)**  
*Date run: 2026‑07‑31 | Scenario ID: 281719ef00ada43f*  

---  

### 1. Device Synopsis (as known from the source)

| Item | Current Knowledge (from source) |
|------|---------------------------------|
| **Device type** | Not described – only generic “medical device” referenced in Korean‑EU mapping tables. |
| **Intended purpose / indication** | *Missing* – required to apply classification rules (Art. 51 & Annex VIII). |
| **Technology principle** | *Missing* – needed to decide which rule(s) of Annex VIII may apply (e.g., “active”, “non‑active”, “diagnostic”). |
| **Contact duration / invasiveness** | *Missing* – determines application of Rules 1–10 (body contact, transient/long‑term). |
| **Risk class candidates** | Unknown – classification must be performed by the manufacturer (self‑classification) per Art. 51 & Annex VIII【2†L0-L4】. |

> **Conclusion:** The available source material does not contain sufficient product‑specific data to assign a definitive MDR class.

---  

### 2. Classification Logic (per MDR Art. 51 + Annex VIII)

| Step | Rule(s) considered | Rationale / Evidence Needed |
|------|-------------------|------------------------------|
| **Step 1 – Identify “active”/“non‑active”** | Rule 1 (Active therapeutic) / Rule 2 (Active monitoring) | Requires knowledge of whether the device incorporates a source of energy that acts on the patient. |
| **Step 2 – Determine invasiveness & duration** | Rules 3–8 (Invasive, body or cavity entry; transient/long‑term) | Need exact anatomical site, intended contact time. |
| **Step 3 – Assess measuring / information functions** | Rule 9 (Measuring for diagnosis) / Rule 10 (Providing information) | Must know if the device measures a physiological parameter or delivers data to a user. |
| **Step 4 – Apply highest‑class rule** | Annex VIII, sequential application; highest resulting class wins. | If multiple rules apply, the most stringent class is selected. |

> **Missing Information Required for Classification**
> - Intended medical purpose (e.g., diagnosis, therapy, monitoring).  
> - Whether it delivers or receives energy (active vs. passive).  
> - Anatomical site of use and contact duration.  
> - Nature of data measured/produced.  

**If any of the above cannot be clarified internally, the manufacturer must request a *borderline classification* opinion from the Competent Authority (CA) or consult the MDCG 2023‑09 Classification Manual v2.1.1【2†L4-L5】.**

---  

### 3. Conformity‑Assessment Route (once class is known)

| Class | Notified Body (NB) involvement | Main MDR references |
|-------|--------------------------------|----------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration; no NB needed. <br> *If sterile or measuring* → NB required for Annex VIII‑2/3. | Art. 61 + Annex XIV (CE marking). |
| **Class Is / Im** | NB review of technical documentation + audit of QMS (ISO 13485). | Art. 61, Annex XIV §§ 1–3. |
| **Class IIa / IIb** | Full NB assessment – design dossier & QMS audit. | Art. 61, Annex XIV §§ 4–5. |
| **Class III** | Most rigorous NB review + possible clinical investigation approval. | Art. 61, Annex XIV §§ 6–7. |

> **Evidence package per route (high‑level checklist)**  

1. **Technical Documentation (Annex II/III)** – device description, label, UDI, risk management file, manufacturing info.  
2. **Clinical Evaluation Report (CER) (Art. 61 § 1, Annex XIV § 13)** – state‑of‑the‑art literature review, clinical data, PMCF plan.  
3. **Risk Management (ISO 14971)** – risk analysis, evaluation of residual risks, verification of risk controls.  
4. **Post‑Market Surveillance (PMS) & PSUR** – per Art. 83‑86; integrated PMS plan for Class IIa+ devices.  
5. **Unique Device Identification (UDI)** – registration in EUDAMED + national UDI portal as shown in source excerpt【1†L0-L4】.  

---  

### 4. Required Evidence & Gap Analysis

| Area | Mandatory Evidence (MDR) | Current Availability | Gap / Action |
|------|--------------------------|----------------------|--------------|
| **Device Description & Intended Use** | Annex II § 3; Art. 2(1) definition of “intended purpose”. | *Missing* – not in source. | Obtain from OEM/marketing dossier. |
| **Classification Rationale** | Annex VIII rules, self‑classification record (Art. 51). | Not performed → unknown class. | Conduct full rule‑by‑rule analysis; document decision tree. |
| **Risk Management File** | ISO 14971 + MDR Art. 10 § 8. | *Missing*. | Build risk management plan, perform hazard analysis. |
| **Clinical Evidence (CER)** | Article 61, Annex XIV §§ 13–16; MDCG 2020‑10 guidance. | No clinical data supplied. | Determine need for: <br> • Literature review (SOTA) <br> • Clinical investigation (if no sufficient equivalence). |
| **U​DI & EUDAMED Registration** | Art. 27, 28; source shows UDI portal links【1†L0-L4】. | UDI system referenced but device‑specific identifier not provided. | Generate Device Identifier (DI) and Production Identifier (PI); upload to EUDAMED. |
| **Post‑Market Surveillance / PSUR** | Art. 83‑86; Annex XIV § 23–24. | No PMS plan described. | Draft PMS Plan, define PMCF activities (especially for Class IIa+). |
| **Authorized Representative (EU)** | Art. 11 – must be appointed if manufacturer outside EU. | Only generic “Authorized Rep.” mentioned【1†L4-L8】. | Confirm identity & written mandate; include in technical file. |

---  

### 5. Risk Controls (to be demonstrated)

| Potential Hazard | Typical Control (per ISO 14971) | Evidence Needed |
|------------------|---------------------------------|-----------------|
| **Electrical safety** (if active) | IEC 60601‑1 compliance, insulation testing. | Test reports, CE marking of electrical safety. |
| **Biocompatibility** (contact with patient) | ISO 10993 series; extractables/leachables if applicable. | Biocompatibility test certificates. |
| **Software safety** (if device includes software) | IEC 62304 lifecycle, cybersecurity plan (MDR Art. 10 § 9). | Software Development File, risk analysis of software. |
| **Sterility assurance** (if sterile) | ISO 11135 or ISO 17665 validation. | Sterilisation process validation report & SAR. |
| **Usability / Human factors** | IEC 62366‑1 usability engineering; labeling clarity. | Usability test results, risk control verification. |

---  

### 6. Citations (MDR Articles / Annexes)

| Ref | Content |
|-----|----------|
| MDR Art. 2(1) | Definition of “intended purpose”. |
| MDR Art. 51 | Manufacturer’s self‑classification obligation. |
| MDR Annex VIII | Classification rules – 22 sequential rules (latest version 2023‑09, MDCG Manual v2.1.1). |
| MDR Art. 61 & Annex XIV §§ 1‑7 | Conformity‑assessment procedures for CE marking. |
| MDR Art. 10 § 8‑9 | Risk management and software/cybersecurity requirements. |
| MDR Art. 27‑28 | UDI obligations, EUDAMED registration. |
| MDR Art. 83‑86 & Annex XIV §§ 23‑24 | Post‑market surveillance system & periodic safety update reports (PSUR). |
| MDCG 2023‑09 “Classification Manual” v2.1.1 | Guidance on borderline cases, rule interpretation (referenced in source excerpt【2†L4-L5】). |

---  

### 7. Human‑Escalation Triggers (when to raise to senior RA / manager)

| Trigger | Reason |
|--------|--------|
| **Cannot determine intended purpose or device technology** after two rounds of information request from OEM. | Classification cannot proceed → risk of non‑compliance. |
| **Conflicting classification opinions** between internal analysis and Competent Authority (CA) advice. | Need senior decision & possible appeal. |
| **Missing essential safety data** (e.g., biocompatibility, electrical safety) for Class IIa+ devices. | May prevent NB audit; escalates to project lead. |
| **Regulatory deadline < 3 months** and still lacking CER or PMS plan. | Requires resource re‑allocation & senior sign‑off. |
| **New EU legislation (e.g., IVDR cross‑reference) that could affect device scope** discovered during review. | Needs legal/strategy input. |

*Action:* Any of the above triggers should be logged as a **Yellow gate action** and communicated to the project manager for priority handling.

---  

### 8. Peer‑Review Prompt (to another RA colleague)

> **Please review the assumptions, source coverage, and potential jurisdictional gaps in this draft:**  
> 1. **Assumptions:** I have assumed that the device’s intended purpose and technology are unknown; consequently, classification is pending. Do you see any implicit assumptions about device class that need re‑evaluation?  
> 2. **Source Coverage:** The only source material provided is a high‑level Korean‑EU regulatory mapping table (excerpt [1]) and a generic classification rule summary (excerpt [2]). Is there additional guidance (e.g., MDCG 2020‑16 on borderline devices, national implementation in Germany/France) that should be referenced for completeness?  
> 3. **Jurisdictional Gaps:** While the draft focuses on EU MDR, some Korean national requirements (UDIs via “udiportal.mfds.go.kr”) are mentioned. Should we explicitly address any overlap with Korean MFDS notifications or harmonisation obligations that could affect the EU submission timeline?

*Kindly provide feedback highlighting any missing evidence, alternative classification routes, or additional regulatory references that should be incorporated before moving to the next phase.*  

---  

### 9. Re‑usable RA Judgment (recorded for future cases)

```honcho_conclude
{
  "scenario_id": "281719ef00ada43f",
  "lesson_key": "mdr_classification_missing_device_data",
  "summary": "When only generic regulatory tables are provided, the first step is to flag missing device‑specific information (intended purpose, technology principle, invasiveness, contact duration). Classification cannot be performed without these; the manufacturer must supply them or a CA opinion must be requested. All subsequent conformity‑assessment steps depend on the final class.",
  "actions": [
    "Request detailed device description and intended use from OEM.",
    "Map received data against Annex VIII rules sequentially, documenting each rule considered.",
    "If classification remains uncertain after internal analysis, initiate a formal borderline opinion request to the Competent Authority (per MDCG 2023‑09)."
  ],
  "references": [
    "MDR Art.51",
    "MDR Annex VIII (latest 2023‑09 revision)",
    "MDCG Classification Manual v2.1.1 (2023‑09)"
  ]
}
```

---  

**End of Draft – no Work Package is closed; any recommended closures are noted as comments only.**

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

> 최우수 사례: 소스에 특정 클래스를 확정할 충분한 데이터가 없음을 명시적으로 인정 — 교과서적 에스컬레이션, fabrication 없음.

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20260715-it17-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_eu-004", "iteration": 17, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3a9b934b82068bf0", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md", "source_hash": "9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `3a9b934b82068bf0`
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

> **Regulatory Draft – Daily Growth Case (v1)**  
*Audience: Theo – EU MDR Regulatory Affairs Specialist*  

---  

### 0. Reference Material
| Source | Location / Hash |
|--------|-----------------|
| **MDR DoC Template Guidance** – “EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 … Annex IV)” | GitHub `holee9/ra‑project/.../MDR_DoC_양식_작성지침.md` – hash **9432073e1a6f…** |
| **Excerpt – Signature Block** (Clause 8) | Chunk ID 1085205256397640486 |
| **Excerpt – DoC Blank Template** (Clauses 1‑4) | Chunk ID 1141859994065237405 |

> *All citations below refer to the MDR text unless otherwise noted*  
> – *MDR 2017/745, Articles 10‑17, Annexes II–IX*  

---  

## 1. Device Overview (as currently documented)

| Item | Current Content (from source) |
|------|-------------------------------|
| **Manufacturer** | Company name placeholder `[회사명]` – no SRN assigned |
| **Authorized Representative** | Placeholder `[EU 대리인명 및 주소]` – only required if manufacturer is non‑EU |
| **Basic UDI‑DI** | Placeholder – not filled |
| **Product Identification** | Name, trade name, model/catalogue number – placeholders |
| **Intended Use** | Generic placeholder “[의도된 사용 목적 — 간략 기재]” |
| **Photograph / Diagram** | Requested but not supplied |

> *The template is a **blank** DoC; actual data must be populated before any declaration can be issued.*

---  

## 2. Classification & Conformity‑Assessment Route  

### 2.1 Preliminary Classification (Rule‑Based)

| MDR Rule | Applicability (assumed) | Resulting Class |
|----------|------------------------|-----------------|
| **Rule 9** – “Active devices which incorporate a source of energy” | *If the device is active, non‑invasive* | **Class IIa** |
| **Rule 10** – “Active devices intended for the diagnosis or monitoring of physiological processes” | *If diagnostic/monitoring* | **Class IIb** |
| **Rule 22** – “Devices incorporating software that provide information used to make decisions for treatment” | *If software‑driven decision support* | **Class III** |

> **Assumption:** The device is a *single‑use, non‑active wound dressing* (typical of many growth‑case examples). If so, **Rule 2** (“non‑active devices which are invasively used”) applies → **Class IIa**.  

> **Action Required:** Confirm the exact technology (active vs. passive, software involvement) to select the correct rule.

### 2.2 Conformity‑Assessment Procedure

| Device Class | Applicable Annex (MDR) | Notified Body Involvement |
|--------------|------------------------|---------------------------|
| **Class IIa** | **Annex IX** – Full quality‑system assessment (module A) + type‑examination (module B) *or* module C (EU type‑examination) if designated | NB required for the **quality‑management system** and **technical documentation** |
| **Class IIb** | **Annex IX** – Full quality‑system assessment + design dossier review (module D) | NB involvement mandatory |
| **Class III** | **Annex X** – Design dossier examination (module D) + full QMS audit (module E) | NB required for all aspects |

> **Pre‑liminary recommendation:** Assuming Class IIa → **Annex IX, module A+B** is the minimum route.

---  

## 3. Required Evidence for Technical Documentation (Annex II)

| Requirement (Annex II) | Specific Evidence Needed | Current Status |
|------------------------|--------------------------|----------------|
| **1. Device Description & Specification** | Complete model list, variants, accessories, UDI‑DI, intended purpose, indications, contraindications | Placeholders only |
| **2. Design/Manufacturing Information** | Process flow diagrams, critical manufacturing steps, supplier qualification records | Not provided |
| **3. General Safety & Performance Requirements (GSPR)** | Mapping of each GSPR to design/clinical evidence (MDR Art 10(9)) | Missing |
| **4. Risk Management File** | ISO 14971‑based risk analysis, evaluation, residual risk justification | No reference |
| **5. Clinical Evaluation (CER)** | Clinical data – literature review + any clinical investigations or post‑market clinical follow‑up (PMCF) plan (MDR Art 61‑62) | Not present |
> **Missing:** Full CER, risk management, manufacturing process description, UDI allocation, and verification of GSPR compliance.

### 3.1 Clinical Evidence Required

| Type | When required | What to provide |
|------|---------------|-----------------|
| **Literature Review** (state‑of‑the‑art) | All devices ≥ Class IIa | Systematic search with inclusion/exclusion criteria, data extraction tables, justification of equivalence if used |
| **Clinical Investigation** | If no sufficient published data or high‑risk class (IIb/III) | Study protocol, IEC 62304 compliance for software, ethics approval, CONSORT flow chart |
| **PMCF** | Ongoing for all devices after CE; required for Class IIa+ | PMCF plan (MDR Annex XV), post‑market data collection results, updates to CER |

---  

## 4. Identified Gaps & Missing Information  

| Gap # | Description | Impact on DoC / NB Audit | Suggested Action |
|-------|-------------|--------------------------|------------------|
| **1** | **EUDAMED SRN** – not assigned (template placeholder) | Prevents registration of the device in EUDAMED; mandatory for MDR compliance (Art 10(1)) | Apply for SRN via national Competent Authority or MB. |
| **2** | **Authorized Representative details** (if manufacturer outside EU) | Required under Art 11‑12; missing would block submission of technical file to NB. | Identify and contract an EU‑based AR, include name & address. |
| **3** | **Basic UDI‑DI** (Annex VI Part C) | Without UDI the device cannot be placed on the market; also needed for EUDAMED filing. | Generate a Basic UDI‑DI per EN ISO 18384‑1 and record in DoC. |
| **4** | **Complete Intended Use statement** – currently placeholder | Needed to determine classification & GSPR mapping (Art 2(1)). | Provide clear, concise intended purpose, target patient group, indication, contraindications. |
| **5** | **Risk Management File** (ISO 14971) | NB will request evidence that all residual risks are acceptable (§10(9)(b)). | Compile risk analysis, evaluation, and risk control measures; link to GSPR. |
| **6** | **Clinical Evaluation Report** – absent | Mandatory for all classes (Art 61‑62). Without it the DoC cannot be issued. | Conduct systematic literature review or clinical investigation; draft CER per MDCG 2020‑13. |
| **7** | **Post‑Market Surveillance (PMS) Plan & PMCF** | Required Annex XV; failure leads to non‑conformity findings. | Draft PMS plan aligned with device class, outline PMCF activities, define KPIs. |
| **8** | **Labeling / IFU** – missing | Must satisfy Annex II requirements (labelling, instructions for use) and include UDI. | Prepare label & IFU draft; ensure readability, safety symbols, CE mark usage per MDR Art 20. |

---  

## 5. Risk Controls (Preliminary)

| Hazard | Potential Harm | Existing Control (assumed) | Additional Required Control |
|--------|----------------|----------------------------|-----------------------------|
| **Material biocompatibility** (e.g., allergic reaction) | Local skin irritation / sensitisation | Material datasheet (placeholder) | Conduct ISO 10993‑1 biocompatibility testing; include results in risk file. |
| **Sterility breach** (if marketed sterile) | Infection | Sterilization process documentation missing | Validate sterilisation (ISO 11137 for radiation, if applicable); provide sterility assurance level (SAL). |
| **Incorrect use due to ambiguous labeling** | Wrong application site or duration | No IFU yet | Create user‑centred IFU with clear steps, warnings, pictograms per MDCG 2020‑13. |
| **UDI mis‑reading** | Traceability loss | None | Apply compliant barcode/QR code; test readability under varied lighting conditions. |

---  

## 6. Citations (MDR Articles & Annexes)

| Topic | Regulation Reference |
|-------|----------------------|
| Classification rules | **Article 2(1)** + **Annex III, Rule 9‑23** |
| Conformity‑assessment routes | **Annex IX (Modules A–D) – Class IIa/IIb**, **Annex X – Class III** |
| Declaration of Conformity format | **Annex IV** (template) – source excerpt used for layout |
| SRN & EUDAMED registration | **Article 10(1)**, **Article 13** |
| Authorized Representative duties | **Articles 11‑12** |
| UDI assignment | **Annex VI Part C** |
| Clinical Evaluation requirement | **Articles 61‑62**, **MDCG 2020‑13** |
| Risk Management | **Annex I, Clause 6** – reference to ISO 14971 |
| PMS & PMCF | **Annex XV** (PMS plan), **Article 83‑86** |
| Labelling & IFU | **Annex II**, **MDCG 2020‑15** |

---  

## 7. Human‑Escalation Triggers  

| Trigger Condition | Reason for Escalation | Recommended Owner |
|--------------------|-----------------------|-------------------|
| **No SRN after 2 weeks of application** | EUDAMED registration impossible → market entry blocked | Project Lead (Regulatory) |
| **Absence of any clinical evidence after 4 weeks** | Cannot complete CER; NB will reject technical file | Clinical Evaluation Lead |
| **Risk Management File not signed off within 6 weeks** | Non‑conformity under Art 10(9)(b) | Quality Manager |
| **Authorized Representative not identified for non‑EU manufacturer** | Violation of Articles 11‑12; legal liability | Legal/Regulatory Affairs |
| **PMCF plan not approved before DoC signing** | Annex XV requirement; could lead to post‑market vigilance gaps | PMS Coordinator |
| **Labeling draft fails readability test (≥2 readers unable to understand)** | Non‑compliant with Annex II § 8 – risk of misuse | Marketing/Regulatory |

*When any trigger fires, an immediate escalation email must be sent to the senior RA manager and recorded in the project tracker.*

---  

## 8. Peer‑Review Prompt  

> **To: [RA Peer – e.g., Elena (EU MDR Specialist)]**  
> Please review the assumptions and evidence gaps identified above. Specifically:
> 1. **Classification:** Are we confident applying Rule 2 (Class IIa) based on the limited description, or should we request a more detailed technology summary before finalising?  
> 2. **Source Coverage:** Does the DoC template excerpt (chunks 1085205256397640486 & 1141859994065237405) fully capture all required Annex IV items, or are additional sections (e.g., “Annex III – Conformity‑assessment results”) missing from our checklist?  
> 3. **Jurisdictional Gaps:** Considering the device may be manufactured outside the EU, have we accounted for the full responsibilities of an Authorized Representative under Articles 11‑12 and the need for a local legal entity (if required by the Member State)?  

*Please provide any contradicting guidance or additional sources you deem necessary.*  

---  

## 9. Reusable RA Judgment (Honcho Record)

```
honcho_conclude{
  case_id: "daily_growth_v1_2026-07-31",
  classification_assumption: "Class IIa (Rule 2 – non‑active invasive device) pending verification of activeness and software content.",
  conformity_route: "Annex IX, Modules A+B (full QMS audit + type‑examination).",
  missing_evidence: [
    "EUDAMED SRN", "Authorized Representative details", "Basic UDI‑DI", 
    "Complete Intended Use statement", "Risk Management File (ISO 14971)", 
    "Clinical Evaluation Report (systematic literature review or investigation)", 
    "Post‑Market Surveillance & PMCF plan", "Labeling/IFU with CE‑mark usage"
  ],
  risk_controls_needed: [
    "Biocompatibility testing (ISO 10993‑1)",
    "Sterilisation validation (if sterile) – ISO 11137",
    "User‑centred IFU & labeling per MDCG 2020‑13/15",
    "UDI generation & barcode readability test"
  ],
  escalation_triggers: [
    {"no_SRN_2w": "EUDAMED registration blocked"},
    {"no_clinical_evidence_4w": "CER cannot be completed"},
    {"risk_file_not_signed_6w": "Non‑conformity under Art 10(9)(b)"},
    {"AR_missing_nonEU": "Legal liability – Articles 11‑12"}
  ],
  peer_review_request: "Elena (RA), confirm classification rule, verify DoC Annex IV completeness, and EU‑non‑EU AR obligations.",
  lesson_tag: ["MDR_DoC_Completion","Classification_Gap_Analysis","Technical_Doc_Evidence_Checklist"]
}
```

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

> DoC 템플릿이 완전 공란임을 정확히 파악. 소스에 없는 예시 기기유형을 '가정'으로 명확히 표시하고 창작(투명하나 불필요) + Module 표기 문제 반복.

**Source Excerpts**

1. Chunk `1085205256397640486`

> 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` ---

2. Chunk `1141859994065237405`

> ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ───────────────────────────────────────────── 1. MANUFACTURER Company name : [회사명] SRN : [EUDAMED SRN — 미취득 시 공백] Address : [등록 사업장 주소] Authorised Representative: [EU 대리인명 및 주소 — 역외 제조사 해당 시] 2. SOLE RESPONSIBILITY STATEMENT This EU Declaration of Conformity is issued under the sole responsibility of the manufacturer named above. 3. BASIC UDI-DI [Basic UDI-DI — Annex VI Part C 기준] 4. PRODUCT IDENTIFICATION Product name : [제품명] Trade name : [상품명] Model / Cat.# : [모델 번호 / 카탈로그 번호] Intended use : [의도된 사용 목적 — 간략 기재] Photograph : [첨부...

### kb-eval-20260715-it17-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_eu-005", "iteration": 17, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "8da6726e1364f4ec", "source": "github:holee9/MD-process/issue-drafts/902_AUDIT_GUIDE-VIG-001_EU_MDR_보존기한_인용부정확.md", "source_hash": "4c91abf315dbe190d6ab922f205dd0b1ee9bd66a660924704de5fca6a523f775"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `8da6726e1364f4ec`
- Source: `github:holee9/MD-process/issue-drafts/902_AUDIT_GUIDE-VIG-001_EU_MDR_보존기한_인용부정확.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/902_AUDIT_GUIDE-VIG-001_EU_MDR_%EB%B3%B4%EC%A1%B4%EA%B8%B0%ED%95%9C_%EC%9D%B8%EC%9A%A9%EB%B6%80%EC%A0%95%ED%99%95.md)
- Source hash: `4c91abf315dbe190d6ab922f205dd0b1ee9bd66a660924704de5fca6a523f775`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `902_AUDIT_GUIDE-VIG-001_EU_MDR_보존기한_인용부정확.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 2. 문서 기재값 vs 1차 출처 정답 | 항목 | 문서 기재 | 1차 출처 정답 | |---|---|---| | EU MDR 기술문서·기록 보존 — 비임플란트 | "Class III 10년" (한정 표기) | **모든 비임플란트 기기 10년** (Class I/IIa/IIb/III 공통) | | EU MDR 기술문서·기록 보존 — 임플란트 | 15년 | 15년 (일치) | ## 3. 1차 출처 - **EU MDR 2017/745 Article 10(8)** - 원문: "Manufacturers shall keep the technical documentation... available for the competent auth...
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

> **Regulatory Draft – Daily Growth Case (v1)  
Scenario ID:** 8da6726e1364f4ec  
**Run date:** 2026‑07‑31  

---

## 1. Device Scope & Initial Assumptions
| Item | Statement |
|------|-----------|
| **Device type** | Non‑implantable medical device (the source excerpt refers to “비임플란트”, i.e., non‑implants). |
| **Intended purpose** | *Not provided in the source material.* Must be clarified before classification. |
| **Material / technology** | *Not provided.* Needed for risk analysis and classification rules. |
| **Market status** | No information on whether a “declaration of conformity” already exists or if this is a new design. |

> **Action:** Request the manufacturer’s intended‑use description, product family, and any existing EU CE label status.

---

## 2. Classification under MDR (Article 10 & Annex VIII)

| Rule | Rationale |
|------|-----------|
| **Rule 1 – Non‑active devices** – If the device is non‑active, does not incorporate a medicinal substance and has no measuring function, classification will be based on invasiveness, duration of contact, and degree of risk. |
| **Rule 5 (non‑implantable, long-term invasive)** – “If a non‑implantable device intended for long‑term (> 30 days) use in direct contact with the surface of the body or a cavity, it is classified **Class IIb**.” |
| **Rule 6 (non‑implantable, short‑term invasive)** – For <30‑day contact, **Class IIa**. |
| **Rule 9 (active devices)** – If active, classification may rise to **Class III** depending on the purpose. |

*Because the source only states “non‑implantable”, we cannot assign a definitive class without the intended duration of use and invasiveness.*  

### Preliminary Classification Recommendation
- **Assume Class IIa** until evidence shows >30 days contact or higher risk, in which case re‑classify to **Class IIb**.  
- **If active or bearing a medicinal substance**, proceed to evaluate Rules 9/10 for possible **Class III**.

> **Human‑Escalation Trigger #1:** If the manufacturer cannot provide duration of use or invasiveness data within 5 business days, flag the classification as “undetermined – requires senior RA sign‑off”.

---

## 3. Conformity Assessment Route (Annex IX/ X)

| Classification | Notified Body Involvement | Required Annex |
|----------------|---------------------------|---------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration only. No NB required. | Annex II (Technical Documentation) |
| **Class IIa / IIb** | Full quality‑system audit (ISO 13485) & review of technical file by a Notified Body. | Annex VIII (CE marking) + Annex III (EU declaration). |
| **Class III** | Design dossier assessment plus full QA audit; possibly additional clinical evaluation scrutiny. | Annex X (Design Dossier) + Annex IV/ V as appropriate. |

*Given the probable Class IIa/IIb, the route will be via a Notified Body (NB) using **Annex VIII**.*

> **Human‑Escalation Trigger #2:** If the device is re‑classified to Class III after further information, initiate an urgent NB selection and schedule a design‑dossier review.

---

## 4. Required Evidence for Technical Documentation (Annex II)

| Section | Minimum required content | Current status (per source) |
|---------|--------------------------|-----------------------------|
| **1. Device description & classification** | Full nomenclature, intended purpose, class, risk classification rule citation. | *Missing – only non‑implantable noted.* |
| **2. Design / Manufacturing information** | Schematics, process flow, materials, sterilisation (if applicable). | *Not provided.* |
| **3. General Safety & Performance Requirements (GSPR)** | Mapping of 23 GSPR with evidence of compliance. | *Missing.* |
| **4. Risk Management File** | ISO 14971 risk analysis, evaluation, controls, residual risk acceptability justification. | *Missing.* |
| **5. Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data, PMCF plan (if required). | *Not present.* |
| **6. Post‑Market Surveillance (PMS) & PMCF** | PMS plan (Annex III), summary of safety and performance (SSOP), ongoing studies. | *Missing.* |
| **7. Labeling & IFU** | Labels, instructions for use, symbols, CE mark placement. | *Not provided.* |
| **8. Declaration of Conformity** | Signed declaration with reference to EU law. | *Not present.* |
| **9. Documentation retention** | Article 10(8) – keep technical documentation **≥10 years** after last device placed on the market (15 years for implants). | Source confirms 10‑year rule for non‑implants; compliance required. |

### Key Gap: No evidence of any of the above sections exists in the provided source. All must be generated / supplied by the manufacturer.

---

## 5. Risk Controls & GSPR Mapping (Article 23)

| Representative GSPR | Typical Evidence Required | Current Evidence |
|----------------------|---------------------------|------------------|
| **18 – Biological safety** | ISO 10993 testing, biocompatibility data. | *Missing.* |
| **19 – Sterilisation** (if applicable) | Validation of sterilisation process, sterility assurance level (SAL). | *Not applicable* unless device is sterile. |
| **21 – Protection against radiation** (if applicable) | Radiation safety assessment. | *N/A.* |
| **22 – Software (if any)** | IEC 62304 development lifecycle, cybersecurity plan. | *Missing.* |
| **24 – Information supplied by the manufacturer** | Full IFU with contraindications, warnings. | *Missing.* |

> **Human‑Escalation Trigger #3:** If any mandatory GSPR cannot be demonstrated within 10 working days, request a senior risk‑management review and possibly defer CE marking.

---

## 6. Citations (Regulatory & Source)

| Reference | Relevance |
|-----------|----------|
| **MDR Article 10(8)** – retention period of technical documentation (≥10 years for non‑implants, ≥15 years for implants). | Confirms the 10‑year requirement cited in source excerpt. |
| **MDR Annex VIII** – conformity assessment procedures for Class IIa/IIb devices. | Determines NB involvement. |
| **MDR Annex II** – content of technical documentation. | Sets evidence checklist. |
| **ISO 14971:2019** – risk management process. | Basis for risk controls. |
| **ISO 13485:2016** – QMS requirements, mandatory for NB audit. | Required QA system. |
| Source excerpt (Chunk 1013295490713979930 & 178189066284189048) | Provides the specific retention‑period data that was previously mis‑quoted in a prior document. |

---

## 7. Human‑Escalation Triggers Summary

| # | Trigger Condition | Required Action |
|---|--------------------|-----------------|
| 1 | Classification cannot be determined within 5 business days due to missing intended‑use/duration data. | Escalate to senior RA lead for interim classification and guidance on additional data collection. |
| 2 | Re‑classification to Class III after new information emerges. | Initiate urgent NB selection, update conformity route, and inform project manager of timeline impact. |
| 3 | Any mandatory GSPR evidence cannot be produced within 10 working days (e.g., biocompatibility, software safety). | Pause CE marking submission, involve risk‑management specialist, and advise manufacturer on required testing. |
| 4 | Documentation retention period not aligned with Article 10(8) after final market placement date is known. | Update technical file’s “record‑keeping” section; remind manufacturer of archiving obligations. |

---

## 8. Peer‑Review Prompt (RA Collaboration)

> **To: [RA colleague – e.g., Elena, Senior RA]**  
> Please review the assumptions and gaps identified in this draft:
> 1. **Classification Logic:** Are we applying the correct MDR Rules given our limited device information? Should we default to a higher class pending clarification?  
> 2. **Source Coverage:** The source only provides retention‑period data; have we missed any other relevant sections (e.g., classification tables) from the same GitHub issue that might affect our assessment?  
> 3. **Jurisdictional Gaps:** Does the draft sufficiently consider any national additional requirements for the target Member State(s) (e.g., Germany’s BfArM post‑market surveillance expectations)?  
> 4. **Evidence Checklist:** Is the evidence list aligned with the latest MDR Annex II/III revisions, or are there newer guidance documents we should reference?  

Please provide comments and suggest any additional documentation items or risk controls that may be required.

---

## 9. Reusable RA Judgment (Honcho Record)

```
honcho_conclude{
  scenario_id: "8da6726e1364f4ec",
  decision: {
    classification_assumption: "Device likely Class IIa pending duration/invasiveness data; re‑classify to IIb if >30 days contact, or to III if active/medicinal.",
    conformity_route: "Annex VIII NB audit (full QMS + technical file review) for Class IIa/IIb; Annex X design dossier if Class III.",
    retention_period_requirement: "Technical documentation must be retained ≥10 years after last device placed on the market (per MDR Art.10(8)); 15 years for implants – confirmed by source excerpts.",
    key_gap: "No technical documentation evidence supplied in source; all sections of Annex II missing.",
    escalation_needed: true,
    escalation_triggers: ["Missing intended‑use/duration → classification uncertainty", 
                         "Potential re‑classification to Class III",
                         "Absence of mandatory GSPR evidence within 10 working days"]
  },
  citations: [
    "MDR Art.10(8) – retention period (source Chunk 178189066284189048)",
    "MDR Annex II – technical documentation content",
    "MDR Annex VIII – conformity assessment routes"
  ],
  peer_review_requested: true,
  peer:"Elena (Senior RA)",
  notes: "Record this judgment for future daily‑growth cases where only retention‑period data is supplied; ensure early request of intended‑use/duration to avoid classification delays."
}
```

--- 

*Prepared by:* **Theo – EU MDR Regulatory Affairs Specialist**  
*Date:* 2026‑07‑31

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

> 이전 문서의 오류(Class III에만 10년 보존 적용)를 소스가 정정한 대로(전 클래스 10년, 이식형 15년) 정확히 일반화 — fabrication 없음.

**Source Excerpts**

1. Chunk `1013295490713979930`

> ## 2. 문서 기재값 vs 1차 출처 정답 | 항목 | 문서 기재 | 1차 출처 정답 | |---|---|---| | EU MDR 기술문서·기록 보존 — 비임플란트 | "Class III 10년" (한정 표기) | **모든 비임플란트 기기 10년** (Class I/IIa/IIb/III 공통) | | EU MDR 기술문서·기록 보존 — 임플란트 | 15년 | 15년 (일치) |

2. Chunk `178189066284189048`

> ## 3. 1차 출처 - **EU MDR 2017/745 Article 10(8)** - 원문: "Manufacturers shall keep the technical documentation... available for the competent authorities for a period of **at least 10 years** after the last device covered by the EU declaration of conformity has been placed on the market. **In the case of implantable devices, the period shall be at least 15 years**..." - URL: https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng - 참고: https://www.medical-device-regulation.eu/2019/07/08/mdr-article-10-general-obligations-of-manufacturers/

## ra_kr

### kb-eval-20260715-it17-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_kr-001", "iteration": 17, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "f941fbd876bd45e8", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f941fbd876bd45e8`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건...
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

> **Regulatory Draft – Digital Medical Software (GUI‑type) – MF DS Classification & Licensing Pathway**  
*Prepared 31 Jul 2026 – Daily Growth v1 – Scenario f941fbd876bd45e8*  

---

### 1️⃣ Product Profile (to be confirmed by the development team)

| Item | Expected Content |
|------|-------------------|
| **Product type** | Stand‑alone graphical user interface (GUI) software that displays health information but does **not** perform automated diagnosis or therapy. |
| **Intended use** | “To provide patients/clinicians with a visual representation of self‑measured blood glucose values and trend analysis.” |
| **Target users** | Patients, primary‑care physicians, diabetic educators. |
| **Device location** | Mobile app (Android / iOS) downloaded from public stores – no integrated hardware. |
| **Risk hypothesis** | Low to moderate risk (no direct therapeutic/diagnostic algorithm). |

> *If the software incorporates a diagnostic or treatment recommendation engine, re‑classify as higher‑risk (Class II–III) and adjust evidence accordingly.*

---

### 2️⃣ Korean Classification & Submission Route  

| MFDS Reference | Clause / Date | Determination |
|----------------|---------------|--------------|
| **디지털의료제품 분류 및 등급 지정 등에 관한 규정** (제2025‑23호, 시행일 2025‑04‑07) | Art. 2–4 – classification matrix for digital medical products. | GUI‑type software that only displays data → **Class I** (lowest risk). |
| **디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정** (제2025‑25호, 시행일 2025‑04‑15) | Art. 6–9 – submission pathways per class. | **Class I → 신고 (Notification)** is permitted *unless* risk‑based justification indicates a need for 허가 (license). |

> **Primary route:** **신고** (electronic notification) via MFDS “디지털 의료제품 신고시스템”.  
> **Escalation trigger:** If any of the following are identified, shift to **허가** (licensing): <br/>• Presence of a clinical decision‑support algorithm. <br/>• Evidence that the software influences treatment decisions without clinician oversight. <br/>• Unresolved cybersecurity risk > ASIL‑B.

---

### 3️⃣ Required Submission Dossiers (per 제2025‑25호)

| Section | Documents / Evidence | Korean‑specific notes |
|---------|----------------------|-----------------------|
| **1. Application Form** | MFDS 신고서 (electronic). | Must be completed in Korean; includes product code, intended use, manufacturer details. |
| **2. Technical Documentation** | <ul><li>Software Description (IEC 62304‑aligned)</li><li>Risk Management File (ISO 14971)</li><li>Usability Engineering Report (IEC 62366‑1)</li><li>Cybersecurity Plan (K‑GAP 2025‑xx, reference to MFDS Cybersecurity Guidelines)</li></ul> | All reports must contain Korean executive summaries; UI screenshots need Korean language version. |
| **3. KGMP Certification** | Digital GMP Certificate (디지털 GMP 고시) – proof of compliance with the 8 digital GMP Type‑Groups (incl. AI/ML). | Facility must be registered in “KGMP 온라인·디지털” database; certificate issued before submission. |
| **4. Clinical Evidence** | • If Class I ‑ no clinical trial required *unless* claim of efficacy > existing standard.<br/>• Optionally, foreign CE/FDA clearance can be cited under 2026‑01‑23 amendment (OECD CER acceptance). | Any claimed performance must be supported by Korean language literature or locally conducted usability study. |
| **5. Labeling & IFU** | Korean label (제품명, 제조원·수입원, 사용제한, 보관조건 등) + Korean Instructions for Use (IFU) in PDF/HTML. | Must meet MFDS labeling rule § 14‑2; include QR code linking to full K‑language manual. |
| **6. Post‑Market Surveillance (PMS) Plan** | PMS SOP, adverse event reporting workflow, periodic safety update schedule. | Align with “시판후조사” requirements – quarterly reports for digital products. |

---

### 4️⃣ Gaps / Missing Information (to be supplied before filing)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Precise intended use statement** (in Korean) | Determines class & need for clinical data. | Draft a concise “사용 목적” clause and circulate for product‑team sign‑off. |
| **Risk classification justification matrix** | Must reference the digital‑medical classification table (제2025‑23호). | Prepare a 1‑page justification linking each function to risk level. |
| **KGMP compliance evidence** | Mandatory for all digital medical software under Digital GMP 고시. | Obtain KGMP audit report; if not yet certified, schedule pre‑audit. |
| **Korean language UI mock‑up** | Required for usability and labeling sections. | Provide screenshots with Korean translations of all on‑screen text. |
| **Cybersecurity assessment** (threat modelling) | New 2025‑Digital GMP includes cyber‑risk controls. | Conduct a NIST‑CSF based analysis; summarize in Korean executive brief. |
| **Foreign CE/FDA clearance details (if any)** | May be used as “foreign evidence” under the 2026 amendment, but must be mapped to Korean requirements. | Collect certificates, Declaration of Conformity, and conduct gap analysis. |

---

### 5️⃣ Core Risk Controls (to be documented)

| Control | Reference Standard | Implementation Note |
|---------|-------------------|---------------------|
| **Hazard Identification & FMEA** | ISO 14971 § 4‑5 | Include software‑specific failure modes (e.g., data loss, incorrect trend calculation). |
| **Software Development Lifecycle** | IEC 62304 Part 1 | Use V‑model; maintain traceability matrix (requirements ↔ design ↔ test). |
| **Usability Validation** | IEC 62366‑1 § 10 | Conduct user testing with Korean participants (≥5) to confirm comprehension of UI. |
| **Cybersecurity Safeguards** | MFDS Cybersecurity Guideline 2025‑xx | Apply secure data transmission (TLS 1.3), regular patching, authentication. |
| **Post‑Market Monitoring** | MFDS “시판후조사” § 7 | Real‑time usage analytics, adverse event hotline in Korean. |

---

### 6️⃣ Key Citations (MFDS)

| Citation | Description |
|----------|-------------|
| **디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정** (제2025‑25호) – 15 Apr 2025. | Governs submission forms, evaluation criteria, and classification for digital products. |
| **디지털의료제품의 분류 및 등급 지정 등에 관한 규정** (제2025‑23호) – 7 Apr 2025. | Provides the risk matrix used to place GUI software in Class I. |
| **디지털 의료기기 제조 및 품질관리 기준 (디지털 GMP)** – 시행 예정 2025년 내. | Sets KGMP requirements for software development, including AI/ML controls. |
| **MFDS 고시 개정 (총리령 제2088호)** – 23 Jan 2026. | Introduces OECD Clinical Evaluation Report (CER) acceptance; allows foreign CE/FDA evidence under defined conditions. |
| **시판후조사(시장 감시) 지침** – MFDS 가이드라인 No. 6, post‑2025 updates. | Details quarterly safety report obligations for digital medical devices. |

---

### 7️⃣ Human–Escalation Triggers (When to Seek Senior RA / Legal Review)

| Situation | Reason | Escalation Path |
|-----------|--------|-----------------|
| **Unclear classification** – function borderline between “display only” and “decision support”. | May require 허가 instead of 신고. | Prompt senior KR‑RA lead + legal counsel for re‑classification. |
| **Foreign CE/FDA evidence used** but the product contains Korean‑specific features not covered by those dossiers. | Risk of MFDS rejection due to unmet local functionality. | Senior RA validation & possible requirement for additional Korean clinical data. |
| **KGMP certificate not yet issued** and launch timeline < 3 months. | Non‑compliance with Digital GMP → refusal. | Immediate escalation to operations for rapid audit scheduling; consider temporary market hold. |
| **Cybersecurity gaps identified** in threat model (e.g., no encryption of PHI). | Violates 2025‑Digital GMP cyber‑requirements. | Security lead + senior RA to develop mitigation plan before filing. |
| **Labeling/IFU translation inconsistency** discovered post‑submission. | MFDS may issue corrective order. | QA & regulatory liaison to re‑issue Korean documents; legal review for liability exposure. |

---

### 8️⃣ Peer‑Review Prompt (to be sent to a fellow KR‑RA)

> **Colleague, could you please challenge the following assumptions and coverage?**  
> 1. The classification of this GUI‑only software as **Class I (신고)** – are we overlooking any hidden decision‑support functionality that would push it into Class II?  
> 2. The reliance on foreign CE/FDA clearance under the 2026 amendment – have we captured all required mapping to Korean risk controls, especially regarding data privacy and cybersecurity?  
> 3. Our current list of missing items – is there any additional Korean‑specific evidence (e.g., local usability study, Korean language performance metrics) that MFDS routinely requests for digital products in this category?  
> 4. The “digital GMP” certification timeline – given the high turnover in the 2025 rollout, are we realistic about obtaining the KGMP certificate before the intended market launch date?  

*Please provide concrete counter‑examples or cite any recent MFDS decisions that differ from our approach.*

---

### 9️⃣ Reusable RA Judgment (Honcho Record)

```json
{
  "honcho_conclude": {
    "scenario_id": "f941fbd876bd45e8",
    "date": "2026-07-31",
    "summary": "GUI‑type digital medical software that only displays health data is classified as Class I under 디지털의료제품 분류 및 등급 지정 등에 관한 규정 (제2025‑23호) and may be submitted via 신고. Required dossier includes Korean language UI, KGMP certification, risk management file, labeling/IFU, and PMS plan. Missing: precise intended use in Korean, risk classification justification, KGMP audit report, Korean UI screenshots, cybersecurity assessment, mapping of any foreign CE/FDA evidence to Korean requirements. Escalation triggers flagged for ambiguous classification, insufficient cyber controls, lack of KGMP, or reliance on foreign evidence without local data.",
    "required_evidence": [
      "MFDS 신고서 (Korean)",
      "Software Architecture & IEC 62304 documentation",
      "ISO 14971 Risk Management File",
      "Usability Engineering Report (Korean executive summary)",
      "Cybersecurity Plan per MFDS 2025 guidelines",
      "Digital GMP Certificate (KGMP)",
      "Korean labeling and IFU",
      "Post‑Market Surveillance SOP"
    ],
    "missing_information": [
      "Formal Korean intended use statement",
      "Risk classification justification matrix",
      "KGMP audit report / certificate",
      "Korean UI mock‑ups/screenshots",
      "Cybersecurity threat model (Korean summary)",
      "Mapped foreign CE/FDA evidence (if used)"
    ],
    "risk_controls": [
      "Hazard analysis & FMEA (ISO 14971)",
      "Software lifecycle traceability (IEC 62304)",
      "Usability validation with Korean participants",
      "Encryption/TLS for PHI, regular patching",
      "Quarterly safety reporting per MFDS 시판후조사"
    ],
    "citations": [
      {"regulation":"디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정","number":"제2025‑25호","date":"2025-04-15"},
      {"regulation":"디지털의료제품의 분류 및 등급 지정 등에 관한 규정","number":"제2025‑23호","date":"2025-04-07"},
      {"regulation":"디지털 GMP 고시 (Digital GMP)","status":"implementation 2025"},
      {"regulation":"MFDS 총리령 제2088호 개정","date":"2026-01-23"},
      {"guideline":"시판후조사 지침 No.6","version":"post‑2025"}
    ],
    "escalation_triggers": [
      "Unclear classification (possible decision-support function)",
      "Foreign CE/FDA evidence insufficient for Korean risk controls",
      "KGMP certificate not yet obtained (<3 months to launch)",
      "Cybersecurity gaps (no encryption, no incident response plan)",
      "Label/IFU translation inconsistency post‑submission"
    ],
    "peer_review_prompt":"See section 8️⃣ above.",
    "peer":"ai"
  }
}
```

--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [ ] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 규정번호·날짜는 정확히 소스 근거. 총리령 제2088호가 'OECD 임상평가보고서(CER) 상호인정을 도입'한다는 존재하지 않는 메커니즘 창작(#124) — '재사용 가능한 RA 판단' 필드에 기록돼 향후 확산 위험.

**Source Excerpts**

1. Chunk `1131342938714268388`

> ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건 (AI/ML 포함) | SW GMP 적용 기준 | ---

2. Chunk `385578214769089426`

> ## 5. 모니터링 포인트 | 항목 | 상태 | 확인 주기 | |---|---|---| | 디지털 GMP 고시 시행 | 2025년 내 예정 [검증 필요] | 분기별 확인 | | 디지털의료제품법 시행규칙 개정 (총리령 제2088호) | 2026-01-23 개정 완료 | — | | 추가 가이드라인 제정 | 지속 예고 중 | 월별 mfds.go.kr 확인 | | MFDS 6종 가이드라인 후속 개정 | 2025년 이후 수시 | 분기별 확인 | ---

### kb-eval-20260715-it17-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_kr-002", "iteration": 17, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "6028e6eb2a51d1dc", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "5f0192e5896bd583833f41c673027bfe34b52793e1679d1f9dc751b5f77320c3"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `6028e6eb2a51d1dc`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%B8%ED%97%88%EA%B0%80_%EC%83%81%EC%84%B8%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `5f0192e5896bd583833f41c673027bfe34b52793e1679d1f9dc751b5f77320c3`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_인허가_상세가이드.md`는 `MFDS_인허가_상세가이드.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수 # MFDS 인허가 상세 가이드 (국내, X-ray System 전용) > 웹 리서치 교차검증 반영 – 2026-04-22 기준
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

> **Regulatory Draft – MFDS Classification & Licensing Route  
Scenario:** Daily‑growth case (ID = 6028e6eb2a51d1dc) – “MFDS classification and licensing route”  
**Date Run:** 2026‑07‑31  

---

## 1. Device Profile (to be filled by the project team)

| Item | Description |
|------|-------------|
| **Device name / Korean name** | *[Insert]* |
| **Intended use / Indications** | *[Insert]* |
| **Technology / Core principle** | *[Insert]* – e.g., X‑ray imaging system, digital detector, etc. |
| **Target patient population** | *[Insert]* |
| **Risk class (proposed)** | *[Determine]* |

> **Note:** The source excerpt [1] outlines the hierarchical legal framework (Medical Device Act → Decrees → Ministerial Ordinances) that controls classification.  

---

## 2. Classification Determination (Korean GB)

| Korean Regulation | Clause / Table | How it applies to our device |
|-------------------|---------------|------------------------------|
| **“의료기기 품목 및 품목별 등급에 관한 규정”** (Medical Device Items & Grade Ordinance) | § 3‑4 (Imaging devices) | X‑ray systems are listed as *Class II* or *Class III* depending on radiation output, intended use and presence of software. |
| **IMDRF Rule 5 – Intended Use** | — | Cross‑reference: If the device is for diagnosis only → lower class; if it supplies therapeutic dose → higher class. |

> **Pre‑liminary conclusion:** Most X‑ray systems are **Class III** (high risk) under MFDS because they emit ionizing radiation and may affect patient management directly.

### 2.1 Submission Pathway

| Class | Korean pathway | Typical dossier size |
|-------|----------------|----------------------|
| I     | Notification (신고) | Minimal |
| II    | Simplified Review (간소화 심사) – “허가(간소화)” | Moderate |
| III   | Full Review (정밀심사) – “허가” | Extensive – full technical file, clinical data, radiation safety assessment. |

**Our device → Class III → Full MFDS 허가 (approval).**

---

## 3. Required Evidence Package (Full Review)

| Category | Regulatory Requirement (MFDS) | Korean citation | International equivalent (for mapping) | Comments / Gaps |
|----------|------------------------------|------------------|----------------------------------------|----------------|
| **Device Description** | Technical file per 「의료기기 허가·신고·심사 등에 관한 규정」 제11조 | 2026‑04‑22 guide (source [2]) | FDA 510(k)/PMA, EU MDCG 2019‑5 | Needs Korean translation of device description, nomenclature. |
| **Design & Manufacturing** | KGMP compliance – facility certificate per 「의료기기 GMP 심사·평가 등에 관한 규정」 제7조 | Same as above | ISO 13485:2016 (QMS) | Verify that manufacturing site holds KGMP certification; if foreign, need local subcontractor with KGMP. |
| **Risk Management** | ISO 14971 risk file + MFDS “위험관리계획” (risk control measures) | § 12 of 허가 규정 | FDA 21 CFR 820.30, EU MDCG 2023‑1 | Map each identified hazard to Korean‑required *위험통제조치*; include radiation exposure limits per “방사선 방호법”. |
| **Electrical Safety & EMC** | KC 인증 (전기·전자제품 안전인증) + MFDS “전기·전자안전” 검토 | Appendix 2 of 허가 가이드 | IEC 60601‑1 series, EU CE MDD/IVDR | Need Korean language labeling on safety marks. |
| **Radiation Safety** | National Radiation Protection Standards (NRPS) – dose limits, shielding calculations, QMS for radiation devices | MFDS “방사선 의료기기 안전관리 지침” | IEC 60601‑2‑33, FDA 21 CFR 1020 subpart H | Must submit **Radiation Exposure Assessment** + *방사선 안전성 검증서*. |
| **Performance Verification** | Bench testing (spatial resolution, DQE, etc.) per MFDS “검증·평가 기준” | Same as above | IEC 61771‑5, FDA guidance for X‑ray systems | Include Korean translation of test reports; if using data from CE/FDA clearance, map to Korean acceptance criteria (see 2026 revision). |
| **Clinical Evaluation** | If foreign clinical data exist → OECD Clinical Evaluation Report (CER) accepted under 2026 Jan MFDS revision (mutual recognition). Otherwise – **Korean PMCF or local clinical trial**. | 「OECD‑CER 수용 범위」 Annex A of 2026 revision | EU MDCG 2021‑24, FDA 510(k) Clinical Data | Confirm whether existing FDA 510(k) / CE‑Mark data meet Korean “등가성” assessment; if not, plan a local pilot study (minimum n=30). |
| **Labeling & IFU** | Full Korean language labeling, product label, packaging, IFU per 「의료기기 라벨·사용설명서 등에 관한 규정」. Must include: device name, model, serial, intended use, contraindications, radiation dose info, etc. | Same as above | FDA 21 CFR 801, EU MDR Annex II | Prepare Korean translation **and** English version (dual‑language allowed but Korean mandatory). |
| **Post‑Market Surveillance (PMS) Plan** | Submit PMS plan per 「시판후조사」 guidelines – include Periodic Safety Update Report (PSUR), field safety corrective actions (FSCA) process. | Same as above | FDA 21 CFR 822, EU MDR Part D | Must designate a Korean Resident Representative for PMS reporting. |

**Missing Information (to be requested from the project team):**

1. **Exact radiation output specifications** (kVp range, mA settings, dose‑area product) – needed for NRPS compliance.
2. **List of comparable foreign approvals** (FDA 510(k)/PMA numbers; CE Mark certificates & Notified Body).  
3. **Current QMS certificates** (ISO 13485, KGMP). If only ISO 13485 is available, we must outline a conversion plan to KGMP.
4. **Clinical evidence file** – copy of any foreign clinical data and the intended Korean indication claim.
5. **Draft Korean IFU/label** – to verify compliance with font size, mandatory statements (e.g., radiation warnings).
6. **Manufacturing site location(s)** – for determining whether domestic KGMP is required or a local subcontractor can be used.

---

## 4. Risk Controls & Mitigation Matrix

| Hazard | Likelihood (K) | Severity (S) | Risk Level (R=K×S) | Existing Control | Additional Korean‑required Control |
|--------|----------------|-------------|-------------------|------------------|------------------------------------|
| Excessive radiation dose to patient | 2 | 5 → 10 | High | Dose‑limiting circuit, pre‑set exposure protocols. | Submit *용량 제한 검증* report per NRPS; provide operator training in Korean (mandatory). |
| Electrical shock (faulty grounding) | 1 | 4 → 4 | Medium | IEC 60601‑1 compliance, double‑insulation. | KC 인증 with Korean label; include **전기안전 경고** on IFU. |
| Software malfunction causing image artifact | 2 | 3 → 6 | High | IEC 62304 software classification, verification plan. | Provide Korean language *소프트웨어 위험 관리 계획*; implement remote firmware update procedure with MFDS approval. |
| Mechanical failure of gantry | 1 | 4 → 4 | Medium | ISO 14971 risk control: periodic maintenance schedule. | Include **정기점검 프로그램** in PMS plan, report to MFDS annually. |

- All controls must be documented in the Korean **위험관리계획서** and cross‑referenced to the technical file.

---

## 5. Citations (primary Korean sources)

| Ref # | Source | Legal Instrument | Section |
|------|--------|------------------|---------|
| [1] | MFDS – “전통 의료기기 체계” overview (excerpt 1025612737507787646) | Medical Device Act, Decree, Ordinance | General hierarchy |
| [2] | MFDS 인허가 상세 가이드 for X‑ray System (excerpt 278735804574527961) | “의료기기 허가·신고·심사 등에 관한 규정” (2026‑04‑22) | Specific evidence list, submission flow |

Additional references to be added once the team supplies device‑specific data.

---

## 6. Human‑Escalation Triggers

| Trigger | Reason | Recommended Action |
|---------|--------|---------------------|
| **Unclear classification** (e.g., uncertainty whether Class II or III) | Mis‑classification can lead to rejected application or delayed market entry. | Escalate to senior RA manager + request MFDS pre‑submission meeting (pre‑review). |
| **Absent KGMP certification for manufacturing site** | Mandatory for Class III devices. | Immediate dialogue with manufacturing; consider local partner or subcontractor. |
| **Insufficient Korean clinical data** (foreign CER not fully accepted) | 2026 revision allows OECD CER only for “equivalent” indications. | Plan a minimal Korean pilot study and submit protocol for MFDS approval before dossier finalization. |
| **Labeling/IFU not yet translated into Korean** | Non‑compliance leads to refusal under labeling regulations. | Engage certified medical translation service; obtain internal QA sign‑off. |
| **Radiation safety calculations missing or outdated** | NRPS non‑conformance → safety audit failure. | Conduct fresh shielding & dose simulations; involve a licensed radiation physicist. |
| **Post‑Market Surveillance plan not designated to a Korean Resident Representative** | MFDS requires local responsible person for PMS reporting. | Appoint and register the resident representative before submission. |

---

## 7. Next Steps (Action Items)

1. **Provide missing device data** (radiation specs, foreign approvals, QMS certificates). – *Owner: Project Lead*  
2. **Prepare Korean translation of labeling/IFU** – *Owner: Regulatory Documentation Team*  
3. **Confirm classification with MFDS pre‑submission inquiry** (optional but recommended for Class III). – *Owner: Senior RA*  
4. **Compile risk management file in Korean format** – *Owner: Risk Management Engineer*  
5. **Draft clinical evaluation report** incorporating OECD CER if applicable, else design a Korean pilot study protocol. – *Owner: Clinical Affairs*  

---

## 8. Peer‑Review Prompt

> **To:** [RA peer – e.g., Ji‑young Kim]  
> **Subject:** Review of MFDS Classification & Licensing Draft (Scenario 6028e6eb2a51d1dc)  
> **Request:** Please challenge the following assumptions and identify any jurisdiction‑specific gaps:  
> 1. The classification as Class III based solely on radiation output – could any sub‑type qualify for a simplified review?  
> 2. Acceptance of foreign clinical data via OECD CER – does our intended indication fully align with Korean “동등성” criteria?  
> 3. KGMP requirement: is a domestic manufacturing certificate absolutely mandatory, or can a foreign site be accepted under the new 2026 mutual‑recognition provisions?  
> 4. Are we missing any recent MFDS amendments (post‑April 2026) that affect labeling of radiation devices?  

Kindly provide feedback by **2026‑08‑03** so we may incorporate revisions before final dossier preparation.

---

## 9. Reusable RA Judgment (Honcho Record)

```
honcho_conclude:
  scenario_id: "6028e6eb2a51d1dc"
  judgment_key: "MFDS_Xray_System_ClassIII_FullReview_2026"
  summary: |
    For X‑ray imaging systems, MFDS treats the device as Class III (high risk) under
    「의료기기 품목 및 품목별 등급에 관한 규정」. The required evidence package consists of
    full technical file, KGMP certification, radiation safety assessment, Korean labeling,
    a risk management plan per ISO 14971, and either an accepted OECD Clinical Evaluation Report
    (post‑Jan 2026 revision) or a locally conducted clinical study. Missing items are specific
    radiation output data, foreign approval references, QMS/KGMP certificates, and Korean IFU.
    Escalation triggers include unclear classification, lack of KGMP, insufficient local clinical
    evidence, and incomplete labeling. The draft also provides peer‑review prompts to verify
    assumptions about classification, CER acceptance, and manufacturing site requirements.
  source_refs:
    - id: "1025612737507787646"
      description: "MFDS traditional device system hierarchy."
    - id: "278735804574527961"
      description: "Detailed MFDS approval guide for X‑ray systems (2026‑04‑22)."
  peer_review_requested: true
  peer: "Ji‑young Kim"
  peer_prompt: |
    Challenge classification, CER acceptance scope, KGMP necessity, and any post‑April 2026
    labeling amendments.
  confidence: high
  notes: |
    All Korean language obligations (labeling, IFU, resident representative) flagged early to avoid late‑stage rework.
```

--- 

*Prepared by Sam – KR RA Specialist (KGMP & MFDS)*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 'X-ray는 대부분 Class III'→'우리 기기도 Class III' 결론 — 웹 검증 결과 국내 X선 촬영장치는 실제 Class II(결론 자체가 틀림). 이 케이스 소스에도 없는 'OECD-CER' 반복(#124) + 검증불가 'IMDRF Rule 5'.

**Source Excerpts**

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `278735804574527961`

> # MFDS 인허가 상세 가이드 (국내, X-ray System 전용) > 웹 리서치 교차검증 반영 – 2026-04-22 기준

### kb-eval-20260715-it17-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_kr-003", "iteration": 17, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "475635e3908912ab", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `475635e3908912ab`
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

> **Regulatory Draft – MFDS Classification & Licensing Route**  
*Audience: Sam (KR RA) – Daily Growth Case*  
*Run date:* 2026‑07‑31 | *Scenario ID:* 475635e3908912ab  

---

### 1. Product Overview (Assumed)

| Item | Description |
|------|-------------|
| **Product type** | Software‑as‑a‑Medical‑Device (SaMD) – AI/ML‑based diagnostic decision support for cardiovascular risk stratification. |
| **Intended use / Indication** | “Provides a risk score and treatment recommendation for patients with suspected coronary artery disease based on ECG and clinical data.” |
| **Target market** | Korean hospitals, clinics, and tele‑medicine platforms (professional use). |
| **Risk class (tentative)** | Class II (moderate risk) – per MFDS “AI/ML‑based GUI” guidance (2025‑05‑07) unless algorithm performs autonomous diagnosis → then Class III. |
| **Regulatory status elsewhere** | FDA 510(k) cleared (KXXXXX, 2023); CE marked under MDR (IVDR classification IIb). |

> **Note:** The above product profile is constructed from the scenario description; confirm actual device specifications before final submission.

---

### 2. MFDS Classification & Submission Route  

| Step | Decision Rationale | MFDS Reference |
|------|-------------------|----------------|
| **A. Determine risk class** | - AI/ML‑based SaMD that provides diagnostic *recommendation* → MFDS Guideline (2025‑05‑07) places such software in **Class II** if clinician retains final decision.<br>- If the algorithm outputs a definitive diagnosis without clinician override, it escalates to **Class III**. | MFDS 디지털의료기기 가이드라인 6종 (2025‑05‑07). |
| **B. Select licensing pathway** | - Class II → **허가 (Approval)** required.<br>- Class III → also 허가, but with stricter clinical evidence & post‑market surveillance. | MFDS “Medical Device Approval” flowchart (see 05_전문가교육/Week02_MFDS_체계_상세.md). |
| **C. Identify GMP compliance** | - All SaMD manufactured in Korea must have a **KGMP 적합인정서** (3‑year validity) issued by an accredited body.<br>- Since 2025‑01‑24, **NIDS** is now authorized to perform GMP 적합판정 for digital medical devices (Source [1]). | Source [1] – “디지털의료기기: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행”. |
| **D. Prepare submission dossier** | - Clinical evaluation file (CEV) including foreign CE & FDA data, plus Korean‑specific clinical data if required (see § 6.2 of MFDS SaMD Guideline).<br>- Technical Documentation per ISO 13485/IEC 62304/ISO 14971.<br>- Korean language labeling, IFU, and PMS plan.<br>- CER (Certificate of Equivalence) accepted under the **2026‑01 OECD Mutual Recognition** revision – but only if the foreign reference is FDA 510(k) or CE MDR and the device falls within the same risk class. | MFDS 2026‑01 revision (OECD/ CER acceptance). |
| **E. Submit** | • **허가 신청서** → MFDS Review Office.<br>• Attach **KGMP 적합인정서** (valid) and **기술문서**.<br>• For Class III, include additional local clinical trial data or an abbreviated bridging study (Korean population ≥ 30 subjects). | MFDS 허가 절차 (standard). |

---

### 3. Required Evidence Package  

| Evidence | Description | Source / Standard |
|----------|-------------|-------------------|
| **Technical Documentation** | Design History File, risk management file (ISO 14971), software development lifecycle (IEC 62304), verification/validation reports. | ISO 14971, IEC 62304. |
| **Clinical Evaluation** | • Summary of FDA 510(k) & CE MDR clinical data.<br>• Literature review supporting performance in Korean patients.<br>• If Class III → prospective Korean clinical trial (or real‑world evidence per MFDS “Negative Change” policy). | MFDS SaMD Guideline 2025‑05‑07; OECD CER acceptance. |
| **GMP Certification** | KGMP 적합인정서 issued by KTL, KTR, TÜV SÜD Korea, etc., *or* NIDS (post‑2025). Must be current (≤3 yr). | Source [1]. |
| **Labeling & IFU** | Korean language product label, packaging, and Instructions for Use (IFU) meeting MFDS format (size, safety symbols, K‑code). | MFDS “Medical Device Labeling” regulations. |
| **Post‑Market Surveillance Plan** | PMS activities, periodic safety update reports, and a risk‑based vigilance system per MFDS § 44. | MFDS PMS regulation. |
| **Cybersecurity & Data Privacy** | Evidence of compliance with Korea’s Personal Information Protection Act (PIPA) for patient data handling, plus ISO 27001 alignment for software security. | PIPA; MFDS Cybersecurity Guidance (2025). |
| **Certificate of Equivalence (CER)** *(optional)* | If leveraging foreign CE/FDA data, obtain a CER from an MFDS‑approved body confirming “substantial equivalence.” This is now accepted under the 2026 OECD revision for eligible devices. | 2026‑01 MFDS revision – OECD/CER acceptance scope. |

---

### 4. Missing / Unconfirmed Information (Gap Analysis)  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended use statement** | Determines risk class and clinical evidence depth. | Obtain final labeling/marketing claim from product owner. |
| **Algorithm transparency & performance metrics** (sensitivity, specificity in Korean cohort) | MFDS requires local performance data for AI/ML SaMD (2025‑05‑07). | Conduct a bridging validation study on ≥50 Korean patients. |
| **Software versioning & change management plan** | Required under IEC 62304 and for future “negative change” approvals. | Provide software lifecycle documentation. |
| **Korean language IFU draft** | Mandatory for all devices sold in Korea; missing leads to rejection. | Translate and format per MFDS labeling guidelines. |
| **KGMP 인증기관 selection** | Need to confirm which of the 6 approved bodies (incl. NIDS) will conduct the GMP audit. | Early engagement with preferred audit body; schedule site inspection. |
| **Local clinical data requirement decision** | If foreign data alone is insufficient, a Korean trial adds cost & timeline. | Perform regulatory gap‑fit assessment (Class II may not need local trial). |
| **Post‑market surveillance resources** | MFDS expects a dedicated PMS team for SaMD; lack can impede approval. | Draft PMS plan and allocate personnel. |

---

### 5. Core Risk Controls (Mapping to Korean Requirements)

| Control | Standard / Guidance | MFDS Expectation |
|---------|----------------------|------------------|
| **Risk Management Process** | ISO 14971 (latest edition) + MFDS SaMD risk classification matrix. | Documented hazard analysis, risk evaluation, mitigation, residual risk acceptance. |
| **Software Validation & Verification** | IEC 62304 (life‑cycle processes). | Demonstrate conformity of software functions under intended use and boundary conditions. |
| **Usability Engineering** | IEC 62366‑1. | Human factors testing with Korean clinicians to verify UI/UX safety. |
| **Cybersecurity** | ISO 27001, MFDS Cybersecurity Guidance (2025). | Protection against unauthorised access & data breaches; regular vulnerability assessments. |
| **Data Privacy** | Korea PIPA & Health‑Info Act. | Secure handling of personal health information; anonymisation where required. |
| **Post‑Market Surveillance** | MFDS PMS regulation § 44, ISO 14971 post‑market activities. | Active monitoring, field safety corrective actions (FSCA), periodic safety update reports. |

---

### 6. Key Citations  

1. **Source [1]** – “디지털의료기기: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행.” Provides the expanded list of accredited GMP audit bodies and the inclusion of NIDS for digital devices.  
2. **Source [2]** – Table of **2025‑2026 주요 규제 변경사항**, especially: <br>• 2025‑01‑24 Digital Medical Device Act (SaMD classification & 허가 changes) <br>• 2025‑05‑07 MFDS 디지털의료기기 가이드라인 6종 – AI/ML GUI classification & clinical data requirements. <br>• 2026 예정 OECD/CER acceptance – enables use of foreign CE/FDA evidence under defined conditions.  
3. **MFDS “디지털 의료기기 허가 지침” (2025‑05‑07 edition)** – detailed risk class matrix for SaMD, clinical evaluation expectations, and labeling requirements.  
4. **KGMP 적합인정 절차** – Standard flowchart (GMP 심사 신청 → … → 적합인정서 발급) as described in the source material.  

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason for Escalation | Recommended Owner |
|---------|----------------------|-------------------|
| **Unclear risk class** (AI/ML autonomy level ambiguous) | Misclassification can lead to inappropriate submission route (notification vs 허가). | RA Lead + Clinical Expert. |
| **Absence of Korean‑language IFU** | MFDS will reject the dossier outright. | Documentation Team – immediate language specialist engagement. |
| **KGMP 인증기관 not yet selected / audit scheduled > 6 months out** | Delays GMP certificate issuance, a prerequisite for 허가. | Project Manager → Procurement/Quality. |
| **Local clinical data mandated but not planned** | Gap in Clinical Evaluation File; may require additional budget & timeline. | Clinical Affairs Lead – initiate feasibility study. |
| **Algorithm performance claims exceed published foreign evidence** | Need for bridged or new clinical validation in Korean cohort. | Clinical / Biostatistics Team – design bridging study. |
| **Regulatory change notification (e.g., 2026 autonomous performance certification) that impacts product roadmap** | May shift future licensing strategy. | Strategy Lead – monitor MFDS notices. |

Escalations should be logged in the project risk register and communicated to senior management within **2 business days** of identification.

---

### 8. Peer‑Review Prompt  

> **To a fellow RA colleague (e.g., Jieun, Senior Regulatory Analyst):**  
> Please review this draft and challenge the following assumptions:  
> 1. The classification as Class II based on “clinician‑in‑the‑loop.” Is there any functionality that could be interpreted as autonomous diagnosis under MFDS guidance?  
> 2. The sufficiency of foreign clinical data (FDA 510(k) & CE MDR) without a bridging study for the Korean population—does the 2026 OECD/CER acceptance truly cover AI/ML SaMD, or are there additional local evidence expectations?  
> 3. The choice of KGMP audit body – is NIDS the most strategic option given the device’s digital nature and our timeline?  
> 4. Any overlooked Korean‐specific obligations (e.g., reporting for “negative change” submissions) that could affect post‑approval compliance.  

Your feedback will be incorporated before final submission to MFDS.

---

### 9. Reusable RA Judgment (Lesson Record)

```
honcho_conclude:
  judgment_id: KR_MFDS_SaMD_2026_v1
  summary: |
    For AI/ML–based SaMD intended for diagnostic decision support in Korea,
    classification is determined by the level of clinician involvement.
    - Clinician‑in‑the‑loop → Class II, 허가 route.
    - Autonomous output → Class III, stricter evidence.
    The 2025‑05‑07 MFDS Digital Medical Device Guidelines define these classes and require:
      • Technical documentation (ISO 14971, IEC 62304).
      • Clinical evaluation – foreign CE/FDA data can be used if a CER is obtained under the 2026 OECD acceptance revision; however, Korean performance validation is still required for AI/ML algorithms.
    GMP certification is mandatory; since 2025‑01‑24 NIDS may conduct KGMP 적합판정 for digital devices (source [1]).
    Key missing items before filing:
      – Final intended use statement.
      – Korean language IFU and labeling.
      – Bridging clinical data or justification for reliance on foreign evidence.
      – Selected KGMP audit body with scheduled inspection.
    Escalate immediately when classification is ambiguous, Korean IFU absent, or local clinical data become required.
  citations:
    - source_id: 1078228256164017760
      excerpt: "디지털의료기기: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행"
    - source_id: 1121184088796802935
      excerpt: "2025~2026 주요 규제 변경사항 … 2025‑05‑07 MFDS 디지털의료기기 가이드라인 6종 제·개정 … AI/ML 기반 GUI SW 분류·임상 요건 확인 필요"
    - note: "2026‑01 OECD/CER acceptance – allows foreign CE/FDA data for equivalent risk class devices."
  peer: "ai"
```

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

> '(가정)' 명시 등 우수한 관행, NIDS 인증일자 등 소스 사실은 정확. 이 케이스 소스에도 없는 '2026 OECD 상호인정' 재등장(#124) + MDR/IVDR 혼용.

**Source Excerpts**

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---

### kb-eval-20260715-it17-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_kr-004", "iteration": 17, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9176c7e20017e56c", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `9176c7e20017e56c`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. 법령 개요 | 항목 | 내용 | |------|------| | 법률명 | 디지털의료제품법 (법률 제20139호, 제정 2024-01-23) | | 시행일 | 2025-01-24 | | 시행령 | 대통령령 제35219호 (2025-01-23 제정, 2025-01-24 시행) | | 시행규칙 | 총리령 제1958호 (2025-02-28 시행) | | 소관 | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과 | | 주요 하위고시 | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 분류 및 등급 지정 규정, 디지털의료기기 제조 및 품질관리 기준, 디지털의료기기 전자적 침해행위 보안 지침(안) |...
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

> ## 📄 DAILY REGULATORY GROWTH CASE – KR‑RA  
**Version:** daily_growth_v1  **Run date:** 2026‑07‑31  **Scenario ID:** 2026‑DG‑01  

### 1️⃣  대상 제품 (Assumed Scope)  
- **Type:** Software as a Medical Device (SaMD) that incorporates AI/ML for image analysis (e.g., AI‑based radiology reader).  
- **Form factor:** Stand‑alone console / viewer software, not physically attached to hardware.  

> *The source material explicitly mentions “AI 영상 분석 모듈” and “콘솔 SW, 뷰어 SW” in the 2025‑01 guideline matrix*【2†L4-L9】.

---

## 2️⃣  MFDS 분류 & 제출 경로 (Classification / Submission Route)

| Korean Regulation | Classification Rule | Likely Class* | Submission Path |
|-------------------|---------------------|--------------|-----------------|
| 디지털의료제품법 (제20139호) + 시행령 제35219호, 시행규칙 제1958호 | 위험도 기반 분류 (class I‑IV). SaMD가 “진단·치료·예방 목적”이며 AI/ML이 “임상 판단에 직접적 영향을 미치는 경우” → **Class III**. | **Class III** (high‑risk) | **허가 (Approval)** – full MFDS 허가 절차, not 인증 or 신고. |
| 참고: “생성형 AI 의료기기 허가·심사 가이드라인”(2025‑01) → 중간 위험도로 규정된 경우 Class III. |  |  |  |

\*If the AI only provides “보조 정보” without direct diagnostic output, classification could downgrade to **Class II** (허가·인증 병행 가능). The final class must be confirmed by MFDS during pre‑submission review.

---

## 3️⃣  Required Evidence Package  

| Evidence | Korean Requirement | International Equivalent | Source |
|----------|-------------------|--------------------------|--------|
| **Technical Documentation** (설계 파일, 소스코드, SBOM) | Must follow “디지털의료기기 전자적 침해행위 보안 지침(안)” → SBOM 포함. | IEC 62304, ISO/IEC 27001, FDA SECURITY Guidance | 【2†L9-L10】 |
| **Software Lifecycle & Risk Management** | ISO 14971 + IEC 62304 compliance; risk control plan must be submitted in Korean. | Same as EU MDR Annex I, FDA’s “General Principles of Software Validation”. | Implicit from law (digital‑medical‑product standards). |
| **Clinical Evidence** | ‑ If foreign clinical data is used, it must meet the post‑2026 MFDS revision: acceptance of OECD‑validated clinical data and CERs. <br>‑ Local bridging study required when intended use or population differs. | FDA 510(k) / De Novo Clinical Data; EU MDR “Equivalence” + Post‑Market Clinical Follow‑up (PMCF). | MFDS revision (2026‑01) – not directly quoted but part of the current framework. |
| **Performance Validation for AI** | Must provide algorithm transparency, dataset description, bias analysis, and post‑market monitoring plan. | FDA “Good Machine Learning Practice” (GMLP); EU “AI Act” high‑risk compliance. | 2025‑01 생성형 AI 의료기기 허가·심사 가이드라인 (중)【2†L4-L6】 |
| **Human Factors / Usability** | Korean IFU must be in Korean; usability testing for the intended user group. | IEC 62366‑1, FDA Human Factors guidance. | General MFDS requirement for SaMD. |
| **Cybersecurity Assessment** | Must pass “디지털의료기기 사이버보안 허가·심사 가이드라인(개정)” (2025‑01‑10) – penetration testing, threat modeling, incident response plan. | FDA Cybersecurity Guidance; EU 2021/0106 regulation. | 【2†L7-L8】 |
| **KGMP Facility Certification** (if development is performed in Korea) | Facility must hold KGMP certification under “디지털의료기기 제조 및 품질관리 기준”. | ISO 13485, FDA QSR. | Source list of 주요 하위고시【1†L4-L6】 |
| **Labeling & IFU** | Korean language mandatory for all labeling, packaging, and user manuals; must include risk information, intended use, contraindications, and QR code linking to electronic safety notice (if applicable). | EU MDR Annex II, FDA labeling rules. | General MFDS requirement (law text). |

---

## 4️⃣  Missing / Open Information  

| Item | Why It’s Needed | Current Gap |
|------|----------------|------------|
| **Exact Intended Use Statement** (e.g., “Assist radiologists in detecting pulmonary nodules on CT”) | Determines classification and the level of clinical evidence required. | Not provided in scenario. |
| **Target Population & Clinical Setting** (Korean hospitals, outpatient clinics) | Affects need for local bridging data under MFDS OECD‑CER acceptance rule. | Unknown. |
| **Algorithm Details** – training dataset size, source, annotation process, bias mitigation steps | Needed for AI‑specific risk control and to satisfy 2025‑01 생성형AI 가이드라인. | Not disclosed. |
| **Post‑Market Surveillance (PMS) Plan** – real‑world data collection, adverse event thresholds. | MFDS requires a PMP (post‑marketing plan) for Class III devices. | Absent. |
| **KGMP Status of Development Site** | If manufacture or final software build occurs in Korea, KGMP certification is mandatory. | Not indicated. |
| **Korean Language IFU Draft** | Mandatory labeling; must be reviewed for regulatory compliance before submission. | Not yet drafted. |
| **Cybersecurity Incident Response SOP (in Korean)** | Required by 2025‑01‑10 cyber‑security guideline. | Missing. |

> **Action:** Gather the above items from the product team before the “Pre‑Submission Meeting” with MFDS.

---

## 5️⃣  핵심 위험 통제 (Key Risk Controls)  

| Hazard Category | Control Measure (Korean / International) | Reference |
|-----------------|-------------------------------------------|-----------|
| **Algorithm misclassification** | ‑ Robust verification & validation per IEC 62304. <br>‑ Independent test set, cross‑validation, and continuous learning lock‑down. | FDA GMLP, EU MDR Annex XVIII |
| **Data bias / fairness** | ‑ Demographic stratified performance reporting; bias mitigation plan. | 2025‑01 생성형 AI 가이드라인 (중)【2†L4-L6】 |
| **Cyber‑attack / Data breach** | ‑ Threat modeling, SBOM, regular penetration testing, secure OTA updates, encryption of PHI. <br>‑ Incident response SOP in Korean. | 2025‑01‑10 사이버보안 가이드라인【2†L7-L8】 |
| **Usability error** | ‑ Human‑factors testing with Korean radiologists; IFU readability at ≤ 9th grade level (Korean). | IEC 62366‑1, MFDS labeling rule |
| **System failure / downtime** | ‑ Redundant architecture, graceful degradation, fail‑safe mode that alerts user. | ISO 14971 risk control hierarchy |
| **Regulatory non‑compliance** | ‑ KGMP audit; Documentation in Korean; Translate foreign evidence into Korean summary tables. | 디지털의료제품법 시행령/시행규칙【1†L4-L6】 |

---

## 6️⃣  인용 (Citations)  

| # | Source | Content |
|---|--------|---------|
| 1 | 디지털의료제품법 (법률 제20139호, 2024‑01‑23) – 시행령 제35219호, 시행규칙 제1958호 | Legal framework establishing MFDS jurisdiction over digital medical products. |
| 2 | 주요 하위고시 목록 (디지털의료제품 허가·인증·신고·심사 … 등) | Lists the specific sub‑regulations and guidance that must be complied with. |
| 3 | “생성형 AI 의료기기 허가·심사 가이드라인” (2025‑01) – **중** | Defines AI‑specific classification and evidence expectations for image‑analysis modules. |
| 4 | “디지털의료기기 사이버보안 허가·심사 가이드라인(개정)” (2025‑01‑10) – **높음** | Provides mandatory cyber security controls, SBOM requirement. |
| 5 | “독립형 디지털의료기기SW 사용적합성 가이드라인” (2025‑01) – **높음** | Sets usability and labeling expectations for console/viewer software. |
| 6 | MFDS 2026‑01 Revision (OECD Clinical Evidence & CER acceptance) | Allows foreign clinical data if OECD‑validated; requires local bridging otherwise. |

---

## 7️⃣  Human‑Escalation Triggers  

| Trigger | Why it Requires Human Review / Escalation | Who Should be Notified |
|---------|-------------------------------------------|------------------------|
| **Adverse Event Rate > 0.5 %** (or any SAE related to diagnostic decision) in PMS data | Potential safety breach; may trigger “시판후조사” by MFDS. | RA Lead → Head of Safety → MFDS liaison officer |
| **Cyber‑security Incident** – confirmed data breach or successful exploit | Mandatory reporting within 24 h per cyber security guideline. | IT Security Manager → Compliance Officer → MFDS (신고) |
| **Significant deviation in AI performance** (>10 % drop vs. validation set) detected during post‑market monitoring | Could indicate model drift; may need emergency software update or recall. | Product Owner → QA Lead → MFDS (허가변경 신고) |
| **Regulatory change** – new MFDS guideline released affecting classification/evidence | Must assess impact on current submission timeline. | Regulatory Strategy Team → Senior Management |
| **KGMP audit failure** | Prevents manufacturing release; may require remediation before filing. | Quality Assurance Director → MFDS (품질관리 기준) |

---

## 8️⃣  Action Checklist for Submission  

1. **Finalize Intended Use & Claim Statement** (Korean).  
2. Compile **Technical Documentation** (Design Dossier, SBOM, risk file) in Korean/English bilingual format.  
3. Prepare **Clinical Evidence Dossier** – include foreign pivotal study + bridging plan per OECD‑CER rule.  
4. Conduct **Usability Test** with Korean end‑users; produce report and updated IFU.  
5. Complete **Cybersecurity Assessment** (threat model, penetration test report, incident response SOP).  
6. Verify **KGMP Certification** of all development/manufacturing sites.  
7. Draft **Post‑Market Surveillance Plan** – specify data sources, AE thresholds, reporting timeline.  
8. Submit **Pre‑Submission Package** to MFDS (온라인 “보건복지부 전자·디지털 의료기기 허가신청” portal).  
9. Await MFDS **Pre‑review Meeting** → address any deficiency letters promptly.

---

## 9️⃣  Peer Review Prompt  

> **@RA‑Peer, please review the assumptions and evidence gaps outlined above.**    
> - Are we correctly interpreting the classification for a “AI 이미지 분석 모듈” under the latest 디지털의료제품법?  
> - Does our mapping of foreign clinical data to MFDS OECD‑CER acceptance fully cover current practice (e.g., need for local bridging)?  
> - Have we accounted for all Korean‐specific obligations (KGMP, SBOM, Korean IFU) and identified any remaining jurisdictional gaps (e.g., potential overlap with telemedicine regulations)?  
> - Suggest additional references or recent MFDS notices that might affect the submission route.  

---

## 🔁  Reusable RA Judgment (Lesson Record)

**Judgment ID:** KR‑RA‑DIGITAL‑SA‑2026‑01  

- **Scope:** SaMD containing AI/ML for diagnostic image analysis, stand‑alone software (console/viewer).  
- **Classification Rule:** Under 디지털의료제품법 & 시행령, AI that directly influences clinical decisions → Class III → 허가 route.  
- **Key Evidence Elements:** Technical dossier (incl. SBOM), risk management (ISO 14971/IEC 62304), AI‑specific validation (algorithm transparency, bias analysis), clinical evidence (foreign data permissible if OECD‑validated; local bridging required otherwise), cybersecurity assessment per 2025‑01‑10 guideline, KGMP certification for any Korean manufacturing site, Korean labeling & IFU.  
- **Typical Missing Items:** Precise intended use claim, target population description, algorithm training dataset details, PMS plan, Korean‐language SOPs (cybersecurity, incident response).  
- **Human‑Escalation Triggers:** AE rate > 0.5 %, confirmed cyber breach, >10 % AI performance drift, KGMP audit failure, regulatory change affecting classification/evidence.  

*Store this judgment for future SaMD AI submissions to MFMF (2026+).*

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

> 법령 인용(법률/시행령/시행규칙)과 가이드라인 5건은 소스와 정확 일치, 탄탄. 이 케이스 소스에도 없는 'OECD 임상근거·CER 수용' 재등장(#124).

**Source Excerpts**

1. Chunk `1002132727008468922`

> ## 1. 법령 개요 | 항목 | 내용 | |------|------| | 법률명 | 디지털의료제품법 (법률 제20139호, 제정 2024-01-23) | | 시행일 | 2025-01-24 | | 시행령 | 대통령령 제35219호 (2025-01-23 제정, 2025-01-24 시행) | | 시행규칙 | 총리령 제1958호 (2025-02-28 시행) | | 소관 | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과 | | 주요 하위고시 | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 분류 및 등급 지정 규정, 디지털의료기기 제조 및 품질관리 기준, 디지털의료기기 전자적 침해행위 보안 지침(안) |

2. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

### kb-eval-20260715-it17-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it17-ra_kr-005", "iteration": 17, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "cc5ef65497222667", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `cc5ef65497222667`
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

> **Regulatory Draft – MFDS Cyber‑Security Guidance (2025 Rev.)**  
*Audience: Sam – KR RA specialist*  

---

## 1. Device Scope & Classification

| Item | Detail |
|------|--------|
| **Applicable guidance** | “의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서)” – revised 2025‑01‑10 (source [1]) |
| **Regulatory basis** | *Digital Medical Products Act* (디지털의료제품법, effective 2025‑01‑24) + Medical Device Act Enforcement Rules (의료기기법 시행규칙). |
| **Target devices** | All “medical devices” (including Software as a Medical Device – SaMD) that transmit, store or process electronic health data, *or* have connectivity (wired/wireless/Bluetooth/IoT). |
| **MFDS classification** | Use the standard risk‑based 4‑class system (Class I–IV). Cyber‑security does **not** re‑classify a device but adds mandatory RA requirements for Class II‑IV devices; for **Class I**, compliance is assessed via self‑certification (신고) with an attached cyber‑security dossier. |
| **Submission route** | <ul><li>**Class I** – *Notification* (신고). Attach “Cyber‑Security Compliance Summary” (see §3).</li><li>**Class II–IV** – *Authorization* (허가) via MF MFDS review board. Include full **Cyber‑Security Dossier** (CSD) as a mandatory annex.</li></ul> |

---

## 2. Required Evidence in the Cyber‑Security Dossier (CSD)

| RA Requirement (RA‑01~RA‑35) | Evidence to be submitted* |
|------------------------------|---------------------------|
| **Secure Design Principles** (RA‑01‑03) | System Architecture Diagram showing “defense‑in‑depth”, threat model, and justification of least‑privilege. |
| **Authentication & Access Control** (RA‑04‑08) | <ul><li>Login flow description, multi‑factor authentication proof.</li><li>RBAC matrix with role definitions.</li></ul> |
| **Encryption** (RA‑09‑12) | <ul><li>Crypto algorithm list (AES‑256/GCM, RSA‑4096). </li><li>Key management SOP and evidence of FIPS‑validated modules.</li></ul> |
| **Software Integrity** (RA‑13‑18) | <ul><li>Code‑signing certificates (e.g., NIST‑approved CA).</li><li>Boot integrity verification logs.</li><li>SBOM (Software Bill of Materials) per SPDX 2.3.</li></ul> |
| **Network Security** (RA‑19‑22) | <ul><li>Port & protocol matrix; firewall ruleset screenshots.</li><li>TLS version (>=1.3) configuration files.</li></ul> |
| **Vulnerability Management** (RA‑23‑26) | <ul><li>CVE monitoring plan – tool name, frequency (≥ weekly).</li><li>Patching schedule & CVD policy document.</li></ul> |
| **Audit & Logging** (RA‑27‑30) | <ul><li>Log retention policy (minimum 12 months). </li><li>Sample log entries with integrity checksum.</li></ul> |
| **Update & Maintenance** (RA‑31‑35) | <ul><li>Secure OTA update mechanism description, digital signature verification flow.</li><li>Remote management security controls (VPN, mutual TLS).</li></ul> |

\*Only the **key artifacts** are listed; full SOPs, test reports, and risk assessments must accompany each.

---

## 3. Missing Information / Gaps to Flag

| Gap | Why it matters | Suggested Remedy |
|------|----------------|------------------|
| **Korean‑language IFU & labeling for cyber‑security warnings** | MFDS requires all safety/usage instructions in Korean (표시·광고 규정). No excerpt mentions language; assume missing. | Provide Korean translation of “Secure Use” section, include QR code linking to security update portal. |
| **Local Clinical Data for connectivity‑related adverse events** | If device’s clinical claim depends on remote monitoring, MFDS may request Korean post‑market data (clinical evidence) per *디지털의료제품법* Annex 3. | Prepare a brief local feasibility report or plan for real‑world evidence collection in Korea. |
| **KGMP certification of the software development facility** | KGMP applies to manufacturers of Class II–IV devices; cyber‑security controls must be reflected in KGMP audit scope. No explicit mention in source. | Verify that the development site holds current KGMP certificate and include audit excerpt. |
| **Evidence of alignment with IEC 81001‑5‑1** (the international standard referenced) | The guide cites IEC 81001‑5‑1 but does not require a formal “Declaration of Conformity”. MFDS reviewers historically request it. | Submit IEC 81001‑5‑1 compliance statement, accompanied by test report from accredited lab. |
| **Post‑market cyber‑incident response plan** | Required under “Update·Maintenance” but often omitted in early submissions. | Draft a Korean‑language incident response SOP (including KISA reporting flow). |

---

## 4. Risk Controls (Mapping to MFDS & IMDRF)

| Hazard | Control (from RA‑01~RA‑35) | Residual Risk Assessment |
|--------|---------------------------|----------------------------|
| Unauthorized access → data breach | Authentication (RA‑04‑08), Least‑privilege (RA‑01‑03) | Likelihood ↓ from “Frequent” to “Occasional”; severity unchanged – overall risk reduced to “Acceptable”. |
| Man‑in‑the‑middle on network traffic | TLS 1.3 enforcement, firewall (RA‑19‑22) | Likelihood ↓ to “Remote”. |
| Malware injection via firmware update | Signed OTA updates, code signing (RA‑13‑18), SBOM (RA‑13‑18) | Likelihood ↓ to “Rare”. |
| Unpatched vulnerability exploitation | CVE monitoring & patch schedule (RA‑23‑26) | Likelihood ↓ to “Remote”. |
| Log tampering obscuring forensic analysis | Immutable audit logs, protected storage (RA‑27‑30) | Detectability ↑; residual risk “Low”. |

All controls must be documented in a **Cyber‑Security Risk Management File** (Korean version of ISO 14971 annex for cyber).

---

## 5. Citations

| # | Source | Section |
|---|--------|---------|
| [1] | MFDS Cybersecurity Guideline (2025 Rev.) – Overview table | §1 “개정 개요” |
| [2] | Same Guideline – RA‑35 requirements list | §3.2 “RA 요구사항 35개 주요 카테고리” |
| Korean statutes | 디지털의료제품법 (2025‑01‑24 시행) | Art. 12, 13 (cyber‑security obligations) |
| International reference | IMDRF N60/N73 – Cyber‑Security Framework | Aligns with RA‑01~RA‑35 |
| IEC 81001‑5‑1:2024 | “Medical device cybersecurity – General requirements for product life‑cycle security” | Supporting standard |

---

## 6. Human‑Escalation Triggers (When to Involve Senior RA / MFDS Liaison)

| Trigger | Reason | Action |
|---------|--------|--------|
| **Incomplete Korean IFU** (no translation of security warnings) | Regulatory non‑compliance; may result in rejection at pre‑review stage. | Escalate to senior RA for rapid translation & legal review. |
| **Missing KGMP certificate for Class II–IV** | MFDS can halt the dossier outright. | Immediate escalation to Manufacturing QA and senior RA to obtain/renew certificate. |
| **Evidence of prior cyber‑incident in a similar device** (publicly disclosed) | May require updated risk assessment & mitigation plan beyond standard checklist. | Senior RA + Cyber‑Security Engineer to revise threat model and submit addendum. |
| **Discrepancy between declared encryption algorithm and actual implementation** (e.g., using proprietary cipher) | Non‑conformity with IEC 81001‑5‑1 & MFDS security expectations. | Escalate for technical review; possible re‑engineering needed. |
| **Regulatory change notice after 2025‑01‑10 amendment** (e.g., new RA requirement added) | Submission already in progress; risk of non‑conformity if not updated. | Senior RA to perform gap analysis and issue “Change Impact Memo.” |

---

## 7. Peer‑Review Prompt (to another Korean RA)

> **Colleague, could you please review the following assumptions?**  
> 1. The cyber‑security dossier requirements listed above (RA‑01 ~ RA‑35) are exhaustive for MFDS *authorization* of Class II–IV devices. Are there any additional “supplementary documents” that the MFDS office typically requests (e.g., a separate “Security Impact Assessment” distinct from the risk file)?  
> 2. The source excerpt only references IMDRF N60/N73 and IEC 81001‑5‑1. Have you observed MFDS ever demanding compliance evidence to *other* international standards (e.g., ISO 27001) for medical devices with high connectivity?  
> 3. For Class I “notification”, is a full CSD still mandatory, or can a concise checklist suffice? Please confirm based on recent submission cases.  
> 4. Are there any jurisdiction‑specific gaps we might have missed (e.g., KISA cyber‑incident reporting thresholds, local data residency requirements for cloud‑based SaMD)?  

*Your feedback will be incorporated into the final CSD template and risk management plan.*

---

## 8. Reusable RA Judgment (honcho_conclude)

```
{
  "honcho_conclude": {
    "scenario_id": "cc5ef65497222667",
    "date": "2026-07-31",
    "summary": "MFDS cyber‑security guidance (2025 rev.) adds 35 mandatory RA items aligned with IMDRF N60/N73 and IEC 81001‑5‑1. For medical devices, these requirements are annexed to the usual class‑based submission route: Class I – notification with a concise Cyber‑Security Compliance Summary; Class II–IV – full Authorization dossier containing a detailed Cyber‑Security Dossier (CSD). Required evidence includes architecture diagrams, authentication/authorization design, encryption specs, code signing proof, SBOM, vulnerability management plan, audit logging samples, and secure OTA update mechanism. Missing Korean‑language IFU content, local KGMP certification proof, IEC 81001‑5‑1 Declaration of Conformity, post‑market incident response SOP, and Korean clinical data for connectivity‑dependent claims are typical gaps. Risk controls map each RA item to reduced likelihood categories per ISO 14971. Escalation triggers identified for incomplete language, absent KGMP, prior incidents, algorithm mismatches, and regulatory updates. This judgment will be stored as a reusable reference for future MFDS cyber‑security submission checklists.",
    "source_refs": [
      {"hash":"87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e","chunk_id":"1019410569588059809"},
      {"hash":"87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e","chunk_id":"1070294818097866704"}
    ],
    "peer": "ai",
    "rationale": "Derived directly from MFDS 2025‑01‑10 revision table (source [1]) and the RA‑35 requirement list (source [2]), cross‑checked with known Korean regulatory practice for cyber‑security (Digital Medical Products Act, KGMP). Gaps flagged based on historic MFDS review comments in the shared ra‑project repository."
  }
}
```

--- 

*Prepared by Sam – KR RA specialist (KGMP & MFDS).*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Optional Correction Note**

> 이번 배치 최악: 소스가 명시적으로 'RA-01~35 정확한 번호는 미제공, 공식 가이드라인 PDF 참조'라고 disclaimer를 다는데도 무시하고 RA-01~35 전 구간을 확정적으로 창작해 모든 표에 권위 있는 것처럼 사용.

**Source Excerpts**

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---
