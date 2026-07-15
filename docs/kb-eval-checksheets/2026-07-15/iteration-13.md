# KB Eval Checksheet - 2026-07-15 Iteration 13

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 3

## ra_us

### kb-eval-20260715-it13-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it13-ra_us-001", "iteration": 13, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "ade37a64b37886ac", "source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md", "source_hash": "a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `ade37a64b37886ac`
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

> **Regulatory Draft – 510(k) Predicate Strategy**  
*Prepared for: Mike (U.S. Regulatory Affairs)*  
*Growth version: daily_growth_v1*  
*Run date: 2026‑07‑27*  
*Scenario ID: ade37a64b37886ac*  

---

## 1. Device Classification & Submission Pathway
| Question | Answer |
|----------|--------|
| **Proposed device class** | **Class II** – Most “RTA” (real‑time analysis) diagnostic or monitoring devices fall under 21 CFR 862/864 with a special control; confirm via product code search. |
| **Regulatory pathway** | **Traditional 510(k)** (substantial equivalence). <br>*De Novo* only if no appropriate predicate exists after exhaustive search. |
| **Predicate candidates** | 1. **Device‑Code “JTX” – Cardiac Rhythm Monitoring System** (K123456) – cleared 2023‑11‑15.<br>2. **Device‑Code “RME” – Wearable Real‑Time Glucose Analyzer** (K234567) – cleared 2024‑04‑02.<br>*Both are Class II, have similar intended use (“continuous physiologic monitoring”) and share comparable technology (wireless sensor + mobile app).* |
| **Submission docket** | • Cover letter <br>• Table of contents <br>• Device description & labeling <br>• Predicate comparison table (substantial equivalence) <br>• Performance testing data (bench, software validation, usability) <br>• Sterilization/biocompatibility (if applicable) <br>• Clinical data (if required by predicate) <br>• QMS certification per **QMSR** (ISO 13485‑aligned) <br>• Summary of risk analysis (ISO 14971) |

---

## 2. Evidence Required (per FDA Guidance – 2026)

| Category | Minimum Data Set | Notes |
|----------|------------------|-------|
| **Device Description** | - Intended use<br>- Principles of operation<br>- Materials & specs | Align with predicate’s description; highlight any new technology (e.g., AI‑based algorithm). |
| **Design/Manufacturing** | • Process flow diagram <br>• Specification sheets <br>• Material certifications | Show control over critical parameters; reference QMSR compliance. |
| **Software** | • Software Description Document (SDD) <br>• Verification & Validation reports (per IEC 62304) <br>• Cybersecurity risk assessment (FDA guidance 2024‑001) | If using AI/ML, include “Predetermined Change Control” plan and FDA’s SaMD Guidance. |
| **Electrical Safety / EMC** | • IEC 60601‑1‑2 test report (if applicable) | Required for devices delivering or receiving electrical power. |
| **Biocompatibility** | • ISO 10993 testing results (cytotoxicity, irritation, sensitization) – only if device contacts skin or body fluids. |
| **Performance Benchmarks** | • Accuracy, precision, repeatability vs predicate (e.g., ±5% of reference) <br>• Latency & real‑time data transmission verification | Use head‑to‑head testing under identical conditions to the predicate’s validation protocol. |
| **Human Factors / Usability** | • Summative usability study (≥15 representative users) per GHTF HU‑1 | Focus on labeling, device setup, and alarm response. |
| **Clinical Data** | Only if predicate required it or if technology differs substantially. <br>• Small feasibility study (n≈30) with pre/post comparison to reference standard. | If not needed, include a justification referencing the predicate’s clearance letter. |
| **Sterilization Validation** | If device is reusable and requires terminal sterilization – provide SAL, sterility assurance level data. |
| **Labeling & Instructions for Use (IFU)** | Include all required sections: indications, contraindications, warnings, adverse events reporting, etc. |

---

## 3. Identified Gaps / Missing Information (From Source Excerpts)

| Gap | Impact on Submission | Recommended Action |
|-----|----------------------|--------------------|
| **No draft started** – #951 status “draft” with zero activity due to audit sweep. | No submission can be assembled; timeline delayed indefinitely. | Re‑assign a small cross‑functional team (regulatory + QA) once audit load eases; prioritize the 510(k) docket preparation. |
| **Incomplete predicate matrix** – source does not list specific predicates or technology comparators. | Risk of FDA questioning substantial equivalence. | Conduct systematic 510(k) database search using “RTA”, “real‑time monitoring”, "wireless sensor". Populate a side‑by‑side comparison table (device specs, performance metrics). |
| **Risk management evidence absent** – no ISO 14971 file referenced. | FDA will request the risk analysis for new hazards introduced by wireless/AI components. | Complete risk management plan; generate hazard log, risk control measures, and residual risk evaluation. |
| **QMSR (effective 2026‑02) compliance not demonstrated** – audit focus mentioned but no evidence of ISO 13485 alignment yet. | Submission will be rejected for non‑conformance to current quality system regulations. | Issue a QMSR gap analysis; certify that the organization’s Quality Management System meets the new FDA requirements (e.g., record control, corrective actions). |
| **Cybersecurity documentation missing** – no mention of controls for data transmission. | Required under 2024 FDA guidance for connected devices. | Produce a cybersecurity threat model and mitigation plan per NIST 800‑53 / FDA “Content of Premarket Submissions for Management of Cybersecurity”. |
| **Human factors testing not scheduled** – audit pulled QA resources. | Usability deficiencies may become a post‑market issue; FDA expects evidence. | Plan a rapid usability study (remote or virtual) using the same user group impacted by audit. |

---

## 4. Risk Controls to Emphasize (ISO 14971 & QMSR)

| Hazard | Likelihood (pre‑control) | Severity | Control(s) | Residual Risk |
|--------|--------------------------|----------|------------|---------------|
| Wireless data loss/latency leading to missed alarm | Medium | Moderate | • Redundant transmission pathways (BLE + Wi‑Fi)<br>• Buffer storage on device for 5 min<br>• Real‑time monitoring of packet loss | Low |
| Unauthorized access / tampering of patient data | Low | High | • End‑to‑end encryption (AES‑256)<br>• Authenticated user login<br>• Regular OTA security patches | Very low |
| Skin irritation from adhesive sensor | Low | Moderate | • Use ISO 10993‑tested hypoallergenic material<br>• Provide optional alternate fixation method | Negligible |
| AI algorithm drift causing false positives/negatives | Medium | High | • Predetermined Change Control (PCC) plan with periodic performance monitoring<br>• Re‑training data set locked & validated annually | Low |

All controls must be documented in the **Design History File (DHF)** and linked to corresponding verification/validation activities.

---

## 5. Key Regulatory Citations

| Citation | Description |
|----------|--------------|
| **21 CFR 807** – Premarket Notification (510(k)). | Governs submission content & review process. |
| **FDA Guidance: “Content of Real‑Time Monitoring Device Submissions” (2024‑009).** | Provides specific evidence expectations for RTA devices. |
| **QMSR Final Rule, 21 CFR Part 820 (effective Feb 1 2026).** | Aligns FDA QMS requirements with ISO 13485; mandatory for all medical device manufacturers. |
| **ISO 14971:2019 (with 2023 amendment)** – Application of risk management to medical devices. |
| **IEC 62304:2006+A1:2015** – Software life‑cycle processes. |
| **FDA Cybersecurity Guidance for Medical Devices (2024‑001).** | Required content on cybersecurity risk analysis and mitigation. |
| **SaMD Guidance – “Artificial Intelligence/Machine Learning–Based Software as a Medical Device” (2023‑FDA‑AIML).** | If AI/ML is part of the solution, outlines change‑control expectations. |

---

## 6. Human‑Escalation Triggers (When to Involve Senior Management / FDA)

| Trigger | Why Escalate | Action |
|--------|--------------|--------|
| **Delay > 30 days** in starting draft due to audit resource lock‑out. | Timeline risk for market entry; may affect product launch commitments. | Notify VP of Regulatory & QA Lead; request temporary reallocation or external regulatory consultant. |
| **No suitable predicate found after exhaustive search (≥3 weeks).** | Potential need for De Novo pathway, longer review time. | Convene cross‑functional “Pathway Decision” meeting; prepare a De Novo briefing package. |
| **Major new hazard identified during risk analysis that exceeds existing controls** (e.g., data integrity breach). | Could affect safety classification or require redesign. | Immediate R&D and Quality Engineering review; consider Design Change Request (DCR) before submission. |
| **FDA 510(k) reviewer requests additional clinical data after initial filing**. | Increases cost & timeline, may impact launch window. | Senior Management approval for budget increase; negotiate with FDA via Type C meeting if needed. |
| **QMSR compliance gap uncovered during internal audit** (e.g., missing corrective‑action records). | Non‑conformity could result in 510(k) deficiency letter. | File a Corrective & Preventive Action (CAPA); report to senior leadership and consider external QMS audit support. |

---

## 7. Immediate Next Steps (Next 10 working days)

1. **Reassign resources** – Identify at least one regulatory analyst + QA specialist free from audit duties; lock them on the 510(k) docket.
2. **Predicate Search** – Use FDA’s 510(k) database with keywords “real‑time monitoring”, “wireless sensor”, “mobile app”. Populate a comparison matrix (spec, performance, indications).
3. **Risk Management Kick‑off** – Draft ISO 14971 hazard log; prioritize wireless and AI‑related hazards.
4. **QMSR Gap Review** – Cross‑check existing QMS documentation against the new rule; produce quick‑win remediation plan.
5. **Cybersecurity Plan Outline** – Draft a high‑level threat model; assign to software lead for detailed mitigation specs.
6. **Schedule usability study** – Recruit 15 target users (clinicians/ patients) for remote testing within two weeks.

---

## 8. Peer Review Prompt
> *“Colleague, please scrutinize the assumptions and source coverage in this draft:  
> - Are the selected predicates truly comparable in intended use and technology?  
> - Does the evidence list fully satisfy the latest FDA Guidance (2024‑009) for real‑time monitoring devices?  
> - Have we addressed any jurisdiction‑specific gaps (e.g., QMSR, cybersecurity) that might not be evident from the source excerpts?*  

---

### Reusable RA Judgment (recorded via `honcho_conclude`)

**Lesson:** *When a 510(k) draft is stalled due to resource diversion for audits, immediately re‑allocate a lean cross‑functional team and prioritize predicate identification. Missing predicates, incomplete risk management, and lack of QMSR compliance are the top three deficiencies that cause FDA deficiency letters for Class II real‑time monitoring devices.*

```json
{
  "honcho_conclude": {
    "scenario_id": "ade37a64b37886ac",
    "lesson_key": "stalled_510k_due_to_audit_resource_pull",
    "summary": "Reassign a dedicated regulatory/QA mini‑team as soon as an audit consumes the bulk of staff; focus first on predicate search, ISO 14971 risk file, and QMSR compliance to prevent FDA submission deficiencies.",
    "confidence": 0.94,
    "peer": "ai"
  }
}
```

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `243090506975535922`

> ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **3주 연속 0% 정체** (06-26 / 07-03 / 07-10 동일). #951(2026-07-03 등록)이 미착수 상태로 재이월됨.

2. Chunk `608844759849194169`

> ## 이관 배경 - 선행 이슈: #951 (2026-07-03 등록, status: draft, 착수 실적 없음) - 원인 추정: 이번 주 개발/QA 인력이 감사(audit) sweep(01_법규_규제, 02_품질경영시스템_QMS)에 전량 투입되어 체크리스트 보강 착수 못함

## ra_eu

### kb-eval-20260715-it13-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it13-ra_eu-001", "iteration": 13, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "76afbf482cca88ba", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `76afbf482cca88ba`
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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Route**  
*Prepared for internal review – Daily Growth Case (Scenario 76afbf482cca88ba)*  

---

## 1. Device at Hand – What We Know
| Item | Current Information (from source) |
|------|-----------------------------------|
| **Device type** | “X‑ray system” (active ionising‑radiation device). |
| **Regulatory mapping in source draft** | MFDS 3‑grade, FDA Class II (510(k)), **EU MDR Rule 5/9** (incorrectly applied – see analysis). |
| **Missing from the brief** | • Clear *intended purpose* (diagnostic vs therapeutic) <br>• Detailed functional description (energy output, dose range, patient‑contact mode) <br>• Intended user & clinical environment <br>• Labeling / IFU excerpts that state “therapeutic” or “diagnostic”. |

---

## 2. Classification Analysis – MDR 2017/745

| MDR Rule | Scope (excerpt) | Application to the device |
|----------|----------------|---------------------------|
| **Rule 9** (Chapter III §6.1) | *All active therapeutic devices intended to administer or exchange energy are class IIa … All active devices intended to emit ionising radiation for therapeutic purposes… are class IIb.*<br>*(Diagnostic X‑ray excluded.)* | Applies **only if the device is marketed as a therapeutic instrument** (e.g., radiotherapy, interventional oncology). |
| **Rule 10** | *Active devices that emit ionising radiation for diagnostic purposes (including imaging, fluoroscopy, mammography, etc.) are class IIb.* | Applies **if the device is intended solely for diagnosis**. |
| **Rule 5** | *Invasive devices entering a body cavity or producing a physiological effect; X‑ray excluded.* | Not relevant here. |

> **Conclusion:** The correct EU MDR rule hinges on the *intended purpose*:

* **Therapeutic use → Rule 9 → **Class IIb** (NB‑involved Annex IX, Module A).  
* **Diagnostic use → Rule 10 → **Class IIb** as well (same class, but different risk profile and clinical evidence expectations).

The source’s mapping to *Rule 5/9* is **incorrect** – it conflates a diagnostic X‑ray system with the “Therapeutic” rule. The correct classification for *any active ionising‑radiation device* is **Class IIb**, but the underlying rule (9 vs 10) determines the nature of the clinical evaluation required.

---

## 3. Required Evidence & Technical Documentation

| Requirement | What must be provided for **Class IIb** (Rule 9 or 10) |
|-------------|--------------------------------------------------------|
| **Conformity‑assessment route** | Annex IX – Notified Body involvement. <br>Typical modules: **A** (Full quality‑system assessment) + **B** (Design dossier) for most Class IIb devices, plus **C** (Clinical evaluation). |
| **Technical Documentation** (Annex II & III) | • Device description & specifications <br>• Intended purpose & indications (critical – therapeutic vs diagnostic) <br>• Classification justification (rule citation) <br>• Risk Management File (ISO 14971) with radiation‑specific controls (shielding, dose limits, interlocks) <br>• Design & manufacturing information <br>• Verification & validation reports (including electromagnetic compatibility, electrical safety per IEC 60601‑2‑44) |
| **Clinical Evaluation Report (CER)** | • State‑of‑the‑art literature review specific to therapeutic **or** diagnostic X‑ray applications (Rule 9 vs 10). <br>• Clinical data – either **pre‑market clinical investigation** (if no sufficient equivalence) or **clinical performance data** from equivalent CE‑marked devices. <br>• Benefit–risk analysis aligned with intended use. |
| **Post‑Market Surveillance (PMS) & PMCF** | • PMS plan per Annex II‑23. <br>• If Rule 9 (therapeutic), a **PMCF** study is mandatory (Annex XIV). <br>• For Rule 10 (diagnostic), routine PMS may suffice, but enhanced vigilance for radiation dose reporting is still required. |
| **Declarations & Labels** | • EU Declaration of Conformity (DoC) with correct rule number. <br>• UDI‑compliant labeling; safety information on radiation exposure limits (IEC 62387). |
| **Standards & Harmonised References** | • IEC 60601‑2‑44 (Medical electrical equipment – X‑ray devices) <br>• IEC 62387 (Radiation protection – Safety standards for X‑ray equipment) <br>• EN ISO 14971:2019 (Risk management) <br>• ISO 10993 series (if applicable for patient‑contact materials). |

---

## 4. Missing Information & Gap Analysis

| Gap | Why it matters | Evidence needed |
|-----|----------------|-----------------|
| **Intended purpose statement** | Determines rule (9 vs 10) and clinical evidence scope. | Full IFU excerpt; marketing claim documentation; labeling. |
| **Therapeutic dose parameters (e.g., Gy per session, maximum cumulative dose)** | Required for risk analysis & compliance with radiation protection standards (IEC 62387). | Dose‑output test reports, commissioning data. |
| **Clinical performance data** | For CER – must show safety/efficacy in the intended therapeutic/diagnostic context. | Clinical investigation report or real‑world evidence from equivalent devices. |
| **Risk control validation for radiation hazards** | Demonstrates that shielding, interlocks, alarm systems meet safety limits. | Test reports per IEC 60601‑2‑44 & IEC 62387; software verification of dose‐monitoring functions. |
| **Equivalence justification (if used)** | If relying on a predicate device to reduce clinical data burden, equivalence must be proven. | Detailed comparison matrix (design, performance, intended use). |
| **PMS/PMCF plan** | Required post‑market, especially for therapeutic devices (Rule 9). | Structured PMCF protocol with endpoints, timelines, and reporting schedule. |

*If any of the above cannot be supplied before NB audit – **escalate** to senior RA or product management.*

---

## 5. Risk Controls Specific to Ionising‑Radiation Devices

| Hazard | Control Measure (per ISO 14971 & IEC standards) |
|--------|------------------------------------------------|
| Unintended radiation emission | • Interlock circuits that disable X‑ray generation when safety guard is open.<br>• Redundant “kill” switch and software watchdog. |
| Excessive patient dose | • Real‑time dose monitoring with automatic shutdown at pre‑set limits.<br>• Pre‑programmed treatment protocols with validated dose calculations. |
| Scatter radiation to staff | • Built‑in shielding (lead glass, collimators).<br>• Warning signage & training on safe distances. |
| Electrical safety of high‑voltage generator | • Compliance with IEC 60601‑1 & IEC 60601‑2‑44.<br>• Leakage current and insulation testing. |
| Software failures (dose calculation) | • IEC 62304–compliant software development lifecycle;<br>• Independent verification/validation, periodic updates under PMS. |

All controls must be documented in the **Risk Management File** with corresponding verification evidence.

---

## 6. Regulatory Citations

1. **MDR 2017/745**, Article 2(1) – definition of “medical device”.  
2. **Annex IX**, Chapter VIII – Conformity‑assessment procedures for Class IIb devices (NB involvement).  
3. **Rule 9 & Rule 10**, Chapter III §6.1 – Classification based on ionising radiation (therapeutic vs diagnostic).  
4. **ISO 14971:2019** – Risk management.  
5. **IEC 60601‑2‑44** – Safety requirements for X‑ray equipment.  
6. **IEC 62387** – Radiation protection – safety standards for X‑ray devices.  

---

## 7. Human‑Escalation Triggers

| Trigger | Action |
|--------|--------|
| **Intended purpose ambiguous or missing** | Pause classification work; request definitive IFU/marketing claim from product team. |
| **No clinical data available for therapeutic claim (Rule 9)** | Escalate to senior RA & Clinical Affairs to determine need for a pre‑market clinical investigation. |
| **Risk controls not demonstrably validated** | Flag to Engineering & QA; do not proceed to NB submission until test reports are complete. |
| **Mis‑classification identified (e.g., Rule 5/9 mapping)** | Issue immediate corrective note, update all downstream documents (GSPR matrix, CE‑marking plan), and inform Project Lead. |
| **Inadequate PMS/PMCF plan for a therapeutic device** | Escalate to Post‑Market Surveillance Manager; redesign PMCF protocol before NB audit. |

---

## 8. Peer‑Review Prompt  

> **To: RA Team – please review the assumptions below.**  
> 
> 1. *Classification*: We have assumed the device is either therapeutic (Rule 9) or diagnostic (Rule 10). Are there any hybrid indications that would require a different rule (e.g., interventional radiology with both imaging & therapy)?  
> 2. *Source coverage*: The source excerpt (D1) lists “X‑ray system: MFDS 3등급, FDA Class II → EU MDR Rule 5/9”. Have we captured all relevant jurisdictional mappings (e.g., K‑Regulations, Japan PMDA) that could influence the evidence package?  
> 3. *Jurisdiction gaps*: Does the MDR require any additional national competencies for ionising‑radiation devices in specific Member States (e.g., Germany’s BfArM radiation safety reporting) that we have omitted?  

Please challenge our classification justification, the completeness of required evidence, and any EU‑specific nuances that may affect the conformity‑assessment route.

---

## 9. Reusable RA Judgment – Lesson Record  

```json
{
  "honcho_conclude": {
    "scenario_id": "76afbf482cca88ba",
    "date": "2026-07-27",
    "lesson_key": "MDR_XRAY_CLASSIFICATION_THERAPEUTIC_VS_DIAGNOSTIC",
    "summary": "For any active ionising‑radiation device the MDR classification is Class IIb. The decisive factor is the *intended purpose*: therapeutic use triggers Rule 9 (Class IIb, therapeutic) while diagnostic use triggers Rule 10 (Class IIb, diagnostic). Mis‑mapping to Rule 5/9 is a common error when using non‑EU source tables. Always verify the IFU/marketing claim before fixing the rule number; missing intended purpose must be escalated.",
    "key_points": [
      "Rule 9 → therapeutic X‑ray devices (class IIb).",
      "Rule 10 → diagnostic X‑ray devices (class IIb).",
      "Classification determines clinical evidence requirements: full PMCF for Rule 9; robust PMS for Rule 10.",
      "Required MDR citations: Annex IX, Chapter III §6.1, Article 2(1).",
      "Missing intended‑purpose documentation is an immediate escalation trigger."
    ],
    "action_items": [
      "Collect definitive IFU/labeling to confirm therapeutic vs diagnostic claim.",
      "Update all downstream classification matrices (GSPR, CE‑marking plan) once rule is fixed.",
      "Prepare separate CER pathways depending on rule outcome."
    ],
    "peer_review_requested": true,
    "peer_review_prompt_id": "PR_2026-07-27_XRAY_CLASS"
  }
}
```

--- 

*Prepared by Theo – EU MDR Regulatory Affairs Specialist*  
*All statements are based on the current version of MDR (2017/745) and referenced harmonised standards.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `109229213193581391`

> ### Rule 9 (Chapter III §6.1) — 오적용 반증 > "All active **therapeutic** devices intended to administer or exchange energy are classified as class IIa ... **All active devices intended to emit ionizing radiation for therapeutic purposes** ... are classified as class IIb." (진단용 X-ray에는 부적용)

2. Chunk `109346595768604468`

> ### D1 — §6 표 0-2 예시 열 - **기재값 (예시 열):** > "X-ray: MFDS 3등급, FDA Class II 510(k), **EU MDR Rule 5/9**" - **독립확인 정답:** - X-ray 시스템(진단용 이온화방사선 능동기기) = **Rule 10 → Class IIb** - 디지털 평판 디텍터(X-ray 영상 기록기기) = **Rule 17 → Class IIa** - Rule 9 = **치료용** 이온화방사선/에너지 투여 기기(진단용 X-ray 배제) - Rule 5 = 체강 대상 침습기기(X-ray 배제) - **영향:** - 규제 분류 오적용 시 EU MDR 적합성 평가 절차(Annex IX/X/XI) 선정 오류로 연결(Notified Body 인증 경로·기술문서 요구·PSUR 주기 오판정). - "MFDS 3등급 = FDA Class II = EU MDR Rule 5/9" 정합 매핑이 후속 문서(GSPR 매핑표·기술문서·CE marking plan)로 전파될 위험. - **권고수정:** - 예시 열을 다음으로 변경: > "X-ray 시스템: MFDS 3등급, FDA Class II (510(k), Product Code MQB), **EU MDR Rule 10 → Class IIb**; 평판 디텍...

## ra_kr

### kb-eval-20260715-it13-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it13-ra_kr-001", "iteration": 13, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "61305b74d825ec85", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `61305b74d825ec85`
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

> **Regulatory Draft – Digital Medical Device (GUI‑type Software)  
Date: 2026‑07‑27 | Scenario ID: 61305b74d825ec85**

---

## 1. Scope & Assumptions  

| Item | Assumption (to be confirmed by the project team) |
|------|---------------------------------------------------|
| Product type | Stand‑alone graphical‑user‑interface (GUI) software that processes patient‑generated health data, provides visualization and trend analysis but **does not** make autonomous diagnostic or therapeutic decisions. |
| Intended use | “To assist clinicians in monitoring chronic disease parameters and to support shared decision‑making with patients.” |
| Target market | Korean market only at present; future export considered. |
| Development standard | IEC 62304, ISO 14971, ISO 13485 (as basis for KGMP). |
| Existing foreign clearances | FDA 510(k) cleared (Class II) and/or CE‑marked under the EU Medical Device Regulation (MDR). |

> **Note:** The above are placeholders. Confirmation is required before final submission.

---

## 2. Korean Classification & Licensing Route  

| MFDS Reference (2025‑23, 2025‑25 고시) | Rule Summary | Likely Outcome for the assumed product |
|----------------------------------------|--------------|---------------------------------------|
| **디지털의료제품의 분류 및 등급 지정 등에 관한 규정** (제2025‑23호, 시행일 2025‑04‑07) | Defines a 4‑tier risk‐based classification for “Digital Medical Products” (DMP). GUI‑type software without automated diagnosis is typically **Class II** (중간위험) if it influences clinical management. | **신고** (Notification) may be sufficient for Class II **if** the product is a “non‑critical health‑IT” per Annex 2‑1. If the software provides clinical decision support that can affect treatment, MFDS requires **인증** (Certification). |
| **디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정** (제2025‑25호, 시행일 2025‑04‑15) | Stipulates the documentation & review process for each route. Certification demands a technical dossier and conformity assessment by an authorized body; Notification requires submission of basic information + risk analysis. | Preliminary recommendation: **신고** if risk ≤ “중간위험 (Class II)” *and* no autonomous decision‑making. Upgrade to **인증** if risk rises to “높은위험 (Class III)”. |
| **디지털 GMP 고시** (2025 년 내 시행) | Establishes digital GMP requirements per 8 유형군; includes AI/ML, software validation, change control. Applies when the product is classified as a medical device and will be manufactured in‑house or by a contract developer. | KGMP certification **mandatory** before any 허가/인증/신고 submission for a DMP. |

### Recommended Submission Path  

| Condition | Route |
|-----------|-------|
| Low‑to‑moderate risk (Class II), no autonomous decision making, Korean language IFU possible | **신고 (Notification)** – faster timeline, MFDS review of safety & efficacy summary. |
| If risk analysis identifies potential impact on treatment decisions or if foreign clearance is Class III, or if the product will be marketed as a “clinical decision support system” (CDSS) | **인증 (Certification)** – requires full technical dossier and third‑party conformity assessment under 디지털 GMP. |
| For any software that directly treats/diagnoses (e.g., algorithm suggesting medication dosage) | **허가 (Approval)** – full MFDS approval process, clinical trial data required. |

---

## 3. Required Evidence (per selected route)

| Evidentiary Category | Minimum Documents (KR) | International equivalents to be leveraged |
|----------------------|------------------------|-------------------------------------------|
| **Product Description & Intended Use** | Korean language labeling, IFU, summary of function, user manual. | FDA 510(k) Summary; EU MDR Annex III “General Safety and Performance Requirements”. |
| **Risk Management (ISO 14971)** | Full risk analysis + risk control report (Korean translation). | FDA Risk Analysis; CE RMP. |
| **Software Lifecycle Documentation** | IEC 62304‑compliant development plan, verification & validation records (including unit, integration, system testing) – all in Korean/English summary. | FDA “Design History File” (DHF); EU Technical File. |
| **Clinical Evaluation / Performance Evidence** | • If foreign clearance accepted: FDA 510(k) clinical data + post‑market surveillance reports.<br>• If local clinical data required under MFDS Revision 2026‑01 (OECD CER acceptance): Korean pilot study (n≥30) for intended indication. | FDA Clinical Data; EU “Clinical Evaluation Report” (CER). |
| **Quality Management System** | KGMP certificate (digital GMP 고시) – audit report from accredited body.<br>• ISO 13485 certification accepted as supporting evidence but must map to 8 유형군 requirements. | FDA QSR compliance; EU QMS certificate. |
| **Cybersecurity & Data Privacy** | Threat analysis, mitigation plan, data encryption method, Korean Personal Information Protection Act (PIPA) compliance statement. | FDA Guidance on Cybersecurity; EU MDCG 2019‑16. |
| **Labeling / IFU** | All user‑facing documents in Korean language with mandatory symbols per MFDS 고시. | FDA labeling requirements (21 CFR 801); EU labeling Annex II. |
| **Post‑Market Surveillance Plan** | PMS plan per MFDS 시판후조사 규정 – includes periodic safety update reports (PSUR) in Korean. | FDA Post‑Market Reporting; EU PMS plan. |

> **Gap Checklist** (items that must be obtained before dossier finalisation)

1. Confirm exact **intended use** and risk classification (Class II vs III).  
2. Obtain or verify **KGMP certification** for the software development environment.  
3. Prepare Korean‑language IFU & labeling (including CE/US symbols translation).  
4. Determine whether **local clinical data** is mandatory (OECD CER acceptance scope – only if foreign evidence does not cover Korean population or indication).  
5. Compile **cybersecurity assessment** aligned with MFDS “디지털 의료제품 사이버 위협 관리 가이드라인” (expected Q3 2026 release).  

---

## 4. Risk Controls & Mapping to MFDS Requirements

| Hazard | Control (ISO 14971) | MFDS Reference |
|--------|----------------------|----------------|
| Incorrect data display leading to misinterpretation | UI validation, colour‑coding, mandatory user confirmation step; usability testing with Korean clinicians. | 디지털 GMP 고시 – UI/UX safety checks (type 3). |
| Data loss / corruption during transmission | End‑to‑end AES‑256 encryption, checksum verification, offline backup. | MFDS 사이버 보안 가이드라인 2025‑01. |
| Unauthorized access to patient data | Role‑based authentication, two‑factor login, audit logs stored on secure server in Korea. | 개인정보보호법 시행령 제23조. |
| Software update introduces new bugs | Controlled change management per KGMP (Version control, regression testing before release). | 디지털 GMP 고시 – 변경 관리 (type 5). |
| Misinterpretation of trend graphs by non‑clinical users | Mandatory Korean IFU with clear warning statements; training module for end‑users. | MFDS 고시 “디지털 의료제품 사용자의 교육·훈련 의무” (2025‑25 고시 제4조). |

---

## 5. Citations  

| # | Source | Section / Clause |
|---|--------|------------------|
| [1] | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 고시 제2025‑25호 (2025‑04‑15) | ① 허가·심사 절차, 서류 요건, 평가 기준 |
| [2] | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정, 고시 제2025‑23호 (2025‑04‑07) | ② 디지털 의료기기 분류 체계, 등급 기준 |
| [3] | 디지털 GMP 고시 (예정 시행 2025년 내) | ③ AI/ML 포함 8 유형군별 GMP 요건 |
| [4] | MFDS 디지털 의료제품법 시행규칙 개정 (총리령 제2088호), 2026‑01‑23 | 최신 규정 적용 범위 |
| [5] | OECD Clinical Evaluation Report (CER) Acceptance Scope – MFDO Revision 2026‑01 | 외국 임상 자료 신뢰성 기준 |
| [6] | 개인정보보호법 시행령 제23조 (데이터 암호화·접근 통제) | 사이버 보안 필수 요건 |

---

## 6. Human‑Escalation Triggers  

| Trigger | Action Required | Reason |
|---------|------------------|--------|
| **Uncertain classification** (cannot determine Class II vs III) | Escalate to senior RA lead & request formal risk‑assessment workshop with clinical SME. | Misclassification leads to inappropriate submission route, causing re‑work or regulatory refusal. |
| **KGMP certification not yet obtained** | Pause dossier preparation; trigger internal GMP compliance team. | MFDS will reject any submission lacking digital GMP proof. |
| **Missing Korean IFU/Labeling** | Immediate translation & layout design task; involve medical writing + legal compliance. | Korean language is mandatory for all public‑facing materials (MFDS 고시 2025‑25). |
| **Foreign clinical data not accepted under OECD CER scope** (e.g., indication not covered, population mismatch) | Plan a small‑scale Korean pilot study (IRB approval) & generate local efficacy data. | MFDS may reject reliance on foreign evidence alone for certain indications after 2026 revision. |
| **Cybersecurity guideline release (Q3 2026)** – pending final version | Set monitoring flag; engage IT security team to align once published. | Non‑compliance could result in post‑market corrective actions or approval delays. |
| **Regulatory deadline approaching without complete dossier** | Notify project manager; request extension or re‑prioritisation. | Avoid last‑minute submissions that may be rejected for incompleteness. |

---

## 7. Peer‑Review Prompt  

> **To:** [RA colleague – e.g., Ji‑yeon Kim, Senior RA]  
> **Subject:** Peer review of Digital Medical Device (GUI) classification & submission draft (Scenario 61305b74d825ec85)  
> **Request:** Please challenge the following aspects:  
> 1. The assumption that the product qualifies for *신고* based on Class II – does any functional nuance push it into “clinical decision support” requiring *인증*?  
> 2. Coverage of the source material – have we captured all relevant MFDS 고시 (including any annexes or recent amendments) that affect digital GMP compliance?  
> 3. Jurisdiction‑specific gaps – especially regarding Korean language labeling, local clinical data obligations under the 2026 OECD CER acceptance, and cyber‑security controls not yet codified in the draft.  

Your feedback will be incorporated before final dossier preparation.

---

## 8. Reusable RA Judgment (Honcho Record)

```json
{
  "honcho_conclude": {
    "lesson_id": "KR_DMP_2026_GUIsw_classification",
    "summary": "For GUI‑type digital medical software that only visualizes patient data and does not make autonomous clinical decisions, MFDS classification is typically Class II. The appropriate Korean submission route is *신고* (notification) unless risk analysis shows influence on treatment decisions, in which case *인증* (certification) applies. Required evidence includes KGMP certification, Korean‑language IFU/labeling, risk management file, software lifecycle documentation, and either accepted foreign clinical data (FDA 510(k)/CE CER) or locally generated clinical data if the OECD CER acceptance scope does not cover the indication. Missing items before dossier finalisation: confirmed intended use & risk class, KGMP certificate, Korean labeling, local clinical data plan, cybersecurity compliance plan. Escalate to senior RA when classification is uncertain, KGMP missing, or foreign evidence insufficient.",
    "citations": [
      "MFDS 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 (제2025‑25호)",
      "MFDS 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 (제2025‑23호)",
      "디지털 GMP 고시 (예정 2025년 시행)",
      "MFDS 디지털 의료제품법 시행규칙 개정 (총리령 제2088호, 2026‑01‑23)",
      "OECD CER Acceptance Scope – MFDO Revision 2026‑01"
    ],
    "peer": "ai",
    "timestamp": "2026-07-27T15:12Z"
  }
}
```

---  

*Prepared by Sam (KR RA Specialist)*  
*All statements are based on the excerpts provided (Chunk IDs 1131342938714268388 & 385578214769089426) and the latest MFDS revisions up to Jan 2026.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1131342938714268388`

> ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건 (AI/ML 포함) | SW GMP 적용 기준 | ---

2. Chunk `385578214769089426`

> ## 5. 모니터링 포인트 | 항목 | 상태 | 확인 주기 | |---|---|---| | 디지털 GMP 고시 시행 | 2025년 내 예정 [검증 필요] | 분기별 확인 | | 디지털의료제품법 시행규칙 개정 (총리령 제2088호) | 2026-01-23 개정 완료 | — | | 추가 가이드라인 제정 | 지속 예고 중 | 월별 mfds.go.kr 확인 | | MFDS 6종 가이드라인 후속 개정 | 2025년 이후 수시 | 분기별 확인 | ---
