# KB Eval Checksheet - 2026-07-23 Iteration 03

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260723-it03-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_us-001", "iteration": 3, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "fd74cfc48014cb28", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `fd74cfc48014cb28`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md)
- Source hash: `7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`는 `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분 --- doc-id: FDA_QMSR_820.35_vs_ISO13485_4.2.5 title: "FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표" type: Guide version: v0.2 status: draft ca...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR & Design‑Control Readiness for an X‑ray Imaging System**

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|----------------|
| **Product family** | Diagnostic X‑ray imaging system (hardware + software) |
| **Regulatory panel** | Radiology / imaging devices – **21 CFR Part 892** *(framework reference)* |
| **Class** | Presumed Class II (most X‑ray systems are classified under §892.1590). <br>*No specific identifier found in source – verify separately* |
| **Primary submission route** | 510(k) Premarket Notification demonstrating **substantial equivalence** to a cleared predicate (e.g., K1234567). |
| **Alternative pathways** | If no adequate predicate exists, consider **De Novo Classification** (Class II) followed by future 510(k)s. |

---

### 2. Core Regulatory Evidence Required  

| Category | Required Artefacts | Rationale / CFR/Standard |
|----------|-------------------|---------------------------|
| **Device Description & Intended Use** | Full device description, indications, labeling draft. | 21 CFR 807.92 (device description). |
| **Predicate Identification** | Predicate 510(k) number, comparison matrix (technology, intended use, performance). | 21 CFR 807.87 (substantial equivalence). |
| **Performance & Safety Testing** | • Electrical safety (IEC 60601‑1)<br>• Radiation safety (IEC 62471 / IEC 61326 / FDA guidance for x‑ray systems)<br>• Imaging performance (resolution, DQE, etc.)<br>• Software verification/validation if applicable (21 CFR 820.30). | 21 CFR 820.30(c) (design validation). |
| **Risk Management** | ISO 14971 risk analysis file (risk management plan, FMEA/FMECA, risk control measures, residual risk evaluation). | 21 CFR 820.30(b) (design verification). |
| **Design‑Control Documentation** | Design History File (DHF), Device Master Record (DMR), design inputs/outputs, change‑control procedures, verification & validation protocols and reports. | 21 CFR 820.30–820.190 (design controls). |
| **QMSR Compliance Evidence** | • Copy of QMS compliant with **21 CFR §820.35** (record‑keeping) and overall Part 820 requirements.<br>• Mapping table showing how ISO 13485:2016 §4.2.5 record‑management is supplemented by the additional FDA requirements in §820.35 (as highlighted in source). | **Source excerpt [1]** confirms that ISO 13485 §4.2.5 alone is insufficient; **§820.35** adds mandatory U.S. record‑keeping elements. |
| **UDI Implementation** | UDI assignment plan, label mock‑ups, GUDID submission package (Device Identifier, Production Identifier). | 21 CFR 830.10‑830.60 (UDI labeling). |
| **Post‑Market Surveillance & Reporting** | PSUR procedure, Medical Device Reporting (MDR) SOPs (21 CFR 803), corrective‑action plan. | 21 CFR 803 (MDR); 21 CFR 820.100‑820.200 (CAPA). |
| **Software Precertification (if applicable)** | If the system includes AI/ML, a **Predetermined Change Control Plan (PCCP)** per FDA Guidance Dec 2024. | FDA “Predetermined Change Control Plan” guidance (not in source; cited as regulatory program). |

---

### 3. Gaps / Missing Information  

| Gap | Impact on Submission | Recommended Action |
|-----|----------------------|--------------------|
| **Exact classification section** – the precise §892 subsection for this X‑ray system is not provided. | May affect predicate selection and clearance language. | Verify the correct §892 identifier (e.g., §892.1590) with FDA product code database. |
| **Predicate device number** | Required for 510(k) substantial equivalence claim. | Identify a cleared X‑ray system with same modality, technology level; record its K‑number. |
| **Clinical performance data** – source does not include any imaging quality or human factors study results. | Needed to support safety and effectiveness claims. | Conduct bench‑testing & limited clinical evaluation per FDA guidance for x‑ray devices. |
| **Software validation plan** (if software component exists). | 21 CFR 820.30 requires documented verification/validation. | Draft a V&V plan aligned with IEC 62304; map to design inputs/outputs. |
| **UDI label artwork** – only general UDI requirement mentioned. | Required for labeling and GUDID submission. | Produce final label mock‑ups incorporating GTIN, serial number, production date. |
| **Risk analysis specific to radiation exposure** – source mentions ISO 14971 but no detailed FMEA. | Critical for demonstrating control of radiation hazards. | Perform a dedicated risk assessment covering dose, shielding, interlocks; document outcomes. |

---

### 4. Key Risk Controls (derived from FDA QMSR & ISO 14971)

1. **Record‑Keeping Control (§820.35)** – implement controlled manufacturing and distribution records, retention schedule >10 years as required for radiation devices.  
2. **Design Verification/Validation** – systematic testing of electrical safety, radiation output, image quality per IEC standards; documented in DHF.  
3. **Software Change Management** – PCCP to pre‑authorize AI/ML model updates without new 510(k) when within predetermined limits.  
4. **CAPA System** – proactive detection and correction of nonconformities; linked to MDR reporting (§803).  
5. **UDI Traceability** – bidirectional linkage between device identifier and batch/serial numbers to enable rapid field actions.  
6. **Radiation Safety Controls** – interlocks, dose‑monitoring, shielding verification per FDA “Performance Standards for X‑ray Equipment” guidance.

---

### 5. Citations  

| Requirement | Source / Reference |
|-------------|--------------------|
| FDA QMSR adds record‑keeping beyond ISO 13485 §4.2.5 | Excerpt **[1]** – “FDA는 §820.35에서 추가 요건을 부과” |
| Comparative table of §820.35 vs. ISO 13485 §4.2.5 | Document metadata **[2]** (title indicating QMSR ↔ ISO 13485 difference table). |
| Part 892 panel for imaging devices | Framework reference – 21 CFR Part 892 |
| QMS requirements overall | 21 CFR Part 820 (framework reference) |
| UDI labeling obligations | 21 CFR §830.10‑§830.60 (framework reference) |
| Predetermined Change Control Plan (PCCP) | FDA Final Guidance, Dec 2024 (program name required). |

*No other instance identifiers were present in the source excerpts; any that are needed (e.g., predicate K‑numbers, exact §892 subsection) must be verified separately.*

---

### 6. Human‑Escalation Triggers  

| Situation | Escalation Action |
|-----------|-------------------|
| **Unresolved classification** – unable to confirm the precise §892 code for the X‑ray system. | Notify Regulatory Lead; initiate FDA product‑code lookup before finalizing 510(k) strategy. |
| **Missing predicate device number** after exhaustive search. | Elevate to Senior RA Manager to consider De Novo pathway. |
| **Insufficient evidence for radiation safety or clinical performance** (e.g., test data gaps). | Pause submission preparation; request additional testing budget and timeline. |
| **QMSR non‑conformance identified in internal audit** (e.g., missing §820.35 records). | Immediate corrective action plan; inform QA/Compliance Director. |
| **Software AI/ML change exceeds PCCP scope**. | Escalate to Clinical & Regulatory Committee for risk re‑assessment and potential new 510(k). |
| **UDI label artwork rejected by FDA during pre‑submission review**. | Route to Labeling Lead for redesign; inform Project Manager of impact on launch schedule. |

---

### 7. Peer Review Prompt  

> *RA colleague, please challenge the assumptions above:*
> - Are we confident that a Class II X‑ray system always falls under §892.1590, or could it be assigned another subsection?  
> - Does the source provide sufficient basis to conclude that ISO 13485 §4.2.5 is “basic” and FDA §820.35 is “additional,” or should we seek supplemental guidance?  
> - Are there any jurisdiction‑specific gaps (e.g., state radiation licensing, NEMA standards) not captured in this draft that could affect our 510(k) package?

--- 

**End of Draft**

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

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `195154780902741471`

> --- doc-id: FDA_QMSR_820.35_vs_ISO13485_4.2.5 title: "FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표" type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: "FDA QMSR §820.35와 ISO 13485 §4.2.5 간 차이 분석 및 X-ray 시스템 기록관리 적용 지침" applicable: [FDA QMSR 21 CFR 820, ISO13485:2016 §4.2.5, 21 CFR 803, 21 CFR 830, 21 CFR Part 11, UDI] forms: [F-QMSR-REC-001] related-docs: - FDA_QMSR_2026 - ISO13485_2016_요약 - SOP-DOC-001 - SOP-TRC-001 - SOP-FSCA-001 - SOP-PSUR-001 related-issues: [44] owner: RA/QA Lead last-review: 2026-05-25 review-due: 2027-05-25 --- # FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표

### kb-eval-20260723-it03-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_us-002", "iteration": 3, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "4e1e7fc04e25a0c9", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `4e1e7fc04e25a0c9`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR & Design‑Control Readiness**

---

### 1. Device Classification & Likely Premarket Pathway  
| Item | Assessment |
|------|------------|
| **Device class** | *Undetermined* – classification hinges on the device’s intended use, technological characteristics and risk profile (21 CFR 862 for clinical chemistry; 892 for imaging; otherwise 820). Current source provides no functional description; a definitive class must be confirmed with the sponsor. |
| **Premarket submission route** | *If Class II/III*: Standard 510(k) (21 CFR 807) with Design‑Control documentation per QMSR (§820.30). <br>*If novel and without predicate*: Consider De Novo classification (21 CFR 814). |

*Action:* Obtain intended‑use statement, target clinical indication, and a short device description to finalize class determination.

---

### 2. Applicable Regulatory Framework  

| Area | Reference |
|------|-----------|
| **Quality Management System Regulation (QMSR)** – effective 26 Feb 2026, ISO 13485‑aligned | 21 CFR 820 (full part) |
| **Design Controls** (mandatory under QMSR) | §820.30 (design & development planning, inputs, outputs, verification, validation, review, transfer) |
| **Service Records Requirements** | §820.35 – detailed service‑record documentation |
| **Complaint Handling** | §820.20 – record the timestamp of complaint investigation completion |
| **FDA Inspection Scope** (post‑QSR changes) | “구 QSR §820.180(c)” – former exemption removed; device is now a routine audit target |
| **Global Alignment – MDSAP** | MDR Annex IX §3.2 – partial acceptance of MDSAP audits for EU market entry |
| **Post‑Market Surveillance (PMS) Data** | MDR Art. 83‒86 – mandatory PSUR/PMSR data collection (referenced in source) |

*Note:* No imaging‑specific section (e.g., §892.xxx) is cited; if the device falls under the imaging panel, the appropriate §892 classification must be added later.

---

### 3. Evidence Required for a 510(k) Submission  

| Requirement | Typical Content | Source‑derived Note |
|-------------|----------------|---------------------|
| **Device description & intended use** | Narrative, labeling excerpts, schematics | *Missing – not in source* |
| **Predicate device comparison** | Side‑by‑side table of technological characteristics and performance data | *Missing – not in source* |
| **Design‑Control documentation** | Design History File (DHF) covering planning, inputs/outputs, verification & validation reports | Must satisfy §820.30; service record evidence needed per §820.35 |
| **Risk Management file** | ISO 14971 risk analysis, mitigation measures, residual risk justification | *No specific identifier in source – verify separately* |
| **Software documentation (if applicable)** | Software Development Plan, verification/validation, Predetermined Change Control Plan (PCCP) if AI/ML | *No reference in source – verify separately* |
| **Manufacturing process validation** | Process qualification data, equipment calibration records (incl. §820.35 service records) | Align with ISO 13485 & QMSR |
| **Sterilization/biocompatibility (if applicable)** | ASTM/FDA test reports, ISO 10993 data | *No reference – verify separately* |
| **Labeling & UDI** | Full label set, UDI configuration per 21 CFR 830.10‑§830.60 | *Not in source – verify separately* |
| **Post‑Market Surveillance Plan** | PMS/PSUR approach aligned with MDR Art. 83‑86 (for global markets) | Source links PMS data collection to §8.4 & MDR Art. 83‑86 |

---

### 4. Identified Gaps / Missing Information  

1. **Intended use and device function** – required for class determination.  
2. **Predicate device identification** – essential for a traditional 510(k).  
3. **Complete Design History File (DHF)** – only service‑record (§820.35) and complaint timestamps (§820.20) are highlighted; other design‑control elements are absent.  
4. **Risk Management dossier** – ISO 14971 reference needed; not supplied in source.  
5. **Software change‑control strategy** – if software is involved, a Predetermined Change Control Plan (PCCP) must be prepared (per FDA Dec 2024 guidance).  
6. **UDI implementation plan** – §830 requirements not addressed.  
7. **MDSAP audit evidence** – source notes “MDSAP 수용 (실사 대체 가능)” but no audit report provided; verify that MDSAP scope covers all QMSR elements.  

*Action:* Request the above artifacts from the product team before finalizing the submission strategy.

---

### 5. Recommended Risk Controls (Design‑Control & Post‑Market)

| Control | Rationale / Regulatory Tie‑in |
|---------|------------------------------|
| **Design input verification** | Demonstrates compliance with user needs; required by §820.30(b). |
| **Design output validation in intended use environment** | Needed for safety/effectiveness claim; ties to FDA’s “clinical evaluation” expectations. |
| **Failure Mode & Effects Analysis (FMEA)** per ISO 14971 | Core risk mitigation, especially where PSUR/PMSR data will be collected (MDR Art. 83‑86). |
| **Predetermined Change Control Plan (PCCP)** (if AI/ML) | Enables pre‑authorized post‑market algorithm updates; FDA guidance Dec 2024. |
| **Service record maintenance** | Complies with §820.35 – provides traceability of field repairs and corrective actions. |
| **Complaint handling & timely closure logging** | Meets §820.20 requirement for timestamped investigation completion. |
| **MDSAP audit coordination** | Aligns U.S. QMSR compliance with EU MDR Annex IX §3.2, reducing duplicate inspections. |

---

### 6. Key Citations (as appearing in source)

| Requirement | Citation |
|-------------|----------|
| Service‑record detailed requirements | **§820.35** |
| Complaint‑investigation completion timestamp | **§820.20** |
| FDA inspection target – former QSR exemption removed | **구 QSR §820.180(c)** |
| MDSAP partial acceptance for EU market | **MDR Annex IX §3.2** |
| PMS data collection obligations | **MDR Art. 83‑86** (referenced in source) |

*No additional instance identifiers were found in the supplied excerpts; all other regulatory citations are framework references.*

---

### 7. Human‑Escalation Triggers  

| Situation | Trigger & Recommended Action |
|-----------|------------------------------|
| **Unresolved device class** | Escalate to senior RA lead for classification workshop; cannot finalize submission route without this. |
| **Missing predicate or comparable device data** | Pause 510(k) timeline; request market research / engineering input. |
| **Incomplete DHF (e.g., no design‑verification records)** | Flag to product development manager; hold off FDA pre‑submission meeting until resolved. |
| **Absent ISO 14971 risk file** | Immediate escalation to risk‑management lead; risk analysis is a regulatory “must”. |
| **Software present without PCCP** | Escalate to software QA/AI governance team; non‑compliance with upcoming AI/ML change‑control expectations. |
| **UDI plan not drafted** | Notify labeling & supply‑chain stakeholder; UDI compliance required before market entry (21 CFR 830). |
| **MDSAP audit evidence insufficient for EU acceptance** | Engage global regulatory liaison; may require supplemental QMS audit. |

---

### 8. Peer Review Prompt  

> @RA‑Peer: Please challenge the assumptions made above regarding (a) the sufficiency of the cited QMSR sections to cover all design‑control elements, (b) the completeness of the risk‑management expectations given the absence of ISO 14971 identifiers, and (c) any jurisdictional gaps—especially whether additional EU MDR Annexes or US FDA guidance documents (e.g., final guidance on AI/ML change control) should be incorporated at this stage.  

---

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

1. Chunk `1012828200772392062`

> II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동일 | **FDA 실사 대상** (구 QSR §820.180(c) 예외 삭제) | NB 불시 감사 대상 | | **8.2.3 공정 모니터링** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.3 부적합 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.4 데이터 분석** | ISO 동일 | ISO 동일 | PSUR/PMSR 작성 근거 데이터 | | **8.5 개선** | ISO 동일 | ISO 동일 | ISO 동일 |

2. Chunk `1037950769042691196`

> MDSAP 수용 (실사 대체 가능) | MDR Annex IX §3.2 — MDSAP 부분 수용 |

### kb-eval-20260723-it03-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_us-003", "iteration": 3, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "2ca568c14498b491", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md", "source_hash": "5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `2ca568c14498b491`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-20_GSPR_QMSR_PRRC_%EC%A0%95%ED%95%A9%EC%84%B1%EA%B2%80%EC%A6%9D.md)
- Source hash: `5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `2026-04-20_GSPR_QMSR_PRRC_정합성검증.md`는 `2026-04-20_GSPR_QMSR_PRRC_정합성검증.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR & Design‑Control Readiness Assessment**

---

### 1. Intended regulatory pathway
| Device context (as inferred from source) | Likely FDA classification | Recommended submission route |
|------------------------------------------|---------------------------|------------------------------|
| Software‑driven AI/ML medical device ‑ no explicit predicate in the source | Class II (most software devices) – **21 CFR Part 892.2050** if image‑processing, otherwise **21 CFR Part 820** for QMSR compliance | 510(k) with substantial‑equivalence argument *or* De Novo (if truly novel) |

> **Citation:** Part 820 (QMSR) – effective Feb 2026; Part 892.2050 for medical image management systems (no device type identified ⇒ verify later).

---

### 2. Core QMSR evidence required (per **21 CFR §820**)

| Requirement | Evidence to be supplied |
|-------------|--------------------------|
| **Quality System Manual & SOPs** – complete and current | • Updated SOP for MDR decision documents (ML‑MDR‑001) <br>• Integrated UDI master record SOP (covers §820.35(b), 21 CFR §830, EU MDR Art.27) |
| **UDI Management** | • Record of label & device identifier per **21 CFR §830.10–§830.60** <br>• Demonstrated integration with GUDID (or US equivalent) |
| **Electronic Signature Policy** | • Scope definition document (QM‑IT‑001) aligning with **21 CFR Part 11** |
| **Design Control & Risk Management** | • Design History File (DHF) <br>• Risk Management File (RMF) per **ISO 14971:2021** (harmonized) <br>• Software Development Plan per **IEC 62304** (state‑of‑the‑art) |
| **Usability & Human Factors** | • Usability engineering file per **IEC 62366‑1** |
| **Cybersecurity & AI/ML Change Control** | • Predetermined Change Control Plan (PCCP) per FDA Guidance Dec 2024 <br>• Evidence of compliance with **IEC 81001‑5‑1** |

*All cited standards are listed as harmonized in the source; they remain valid references for the QMSR audit.*

---

### 3. Gaps identified in source & required actions

| Gap (source) | Required remediation |
|--------------|----------------------|
| **No SOP template for MDR decision documents** | Draft and approve *ML‑MDR‑001* (decision/report tree). |
| **UDI master record fragmented** | Consolidate into a single UDI Data Record SOP; reference **§820.35(b)**, **21 CFR §830**, and **EU MDR Art.27**. |
| **Internal audit report lacks objective evidence citations** | Revise template to mandate citation of supporting records (e.g., test reports, risk analyses). |
| **Scope of electronic signatures undefined** | Issue *QM‑IT‑001* defining Part 11 applicability; map signature usage across design, manufacturing, and post‑market activities. |
| **AI/ML device – no EU AI Act filing** (EU focus) | For US submission: develop PCCP; flag need for parallel EU AI Act compliance if marketed in Europe. |

> **Citation:** No specific identifier found in source for the above gaps – verify separately.

---

### 4. Risk controls to be demonstrated

| Control area | Evidence needed |
|--------------|-----------------|
| **Risk Management (ISO 14971)** | Hazard analysis, risk evaluation matrix, mitigations with verification records. |
| **Software Lifecycle (IEC 62304)** | Software development plan, verification & validation reports, configuration management. |
| **Usability (IEC 62366‑1)** | Use‑error analysis, formative and summative usability testing results. |
| **Cybersecurity (IEC 81001‑5‑1)** | Threat model, security controls, vulnerability management process. |
| **AI/ML Change Management** | Predetermined Change Control Plan (PCCP) detailing preapproved algorithm updates, monitoring plan, post‑deployment performance data. |

All controls must be linked to the QMSR documents and shown in the DHF.

---

### 5. Human‑escalation triggers (when a reviewer must intervene)

| Trigger | Action |
|--------|--------|
| **Unresolved SOP gaps > 14 days** after assignment | Escalate to QA Manager & RA Lead for corrective action plan approval. |
| **UDI master record fragmentation persists after SOP issuance** | Notify Director of Regulatory Affairs; initiate FDA‑style deviation report (21 CFR §820.90). |
| **Electronic signature scope not approved before system go‑live** | Halt release; require sign‑off from Compliance Officer per Part 11. |
| **PCCP not finalized before any AI/ML algorithm update** | Suspend deployment; document as non‑conforming change and report to FDA via a 510(k) supplement if applicable. |
| **Audit findings lacking objective evidence citations** | Require re‑submission of audit report with proper references; if not remedied, raise to Senior Management for possible regulatory inspection readiness issue. |

---

### 6. Bottom line

- The organization must close the identified SOP and documentation gaps before any FDA submission can be considered complete.
- Align all QMSR artifacts with **21 CFR Part 820**, **§820.35(b)** (UDI records), and **21 CFR Part 830** (labeling) while leveraging the harmonized ISO standards listed in the source.
- For AI/ML components, a **Predetermined Change Control Plan (PCCP)** is mandatory; absence constitutes a regulatory deficiency.

---

### 7. Peer‑review request

> *Please review the assumptions made about device classification (Class II vs. De Novo), the completeness of the listed evidence requirements, and any jurisdiction‑specific omissions (e.g., FDA’s recent guidance on medical device software documentation). Highlight any gaps that may affect UDI management or AI/ML change‑control compliance.*

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

1. Chunk `1061533089543682126`

> ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적용 | | AI/ML 기기 | OJEU/MDCG 단독 등재 없음 → EU AI Act 병행 필요(후속 과제) | | 운영 영향 | 체크리스트에 H/S 컬럼 신설, 개정판 번호(A11, A1, A2) 기재 의무화 |

2. Chunk `1066441905930561439`

> ### Gap → 조치 | Gap | 조치 | |-----|------| | 국내 SOP에 MDR 결정문서 양식 부재 | 양식 ML-MDR-001 초안(보고/미보고 결정트리) 신설 | | UDI 마스터 레코드 단편화 | UDR(UDI Data Record) 통합 관리 SOP 초안 (§820.35(b) + 21 CFR 830 + EU MDR Art.27) | | 내부감사 보고서 서술 수준 | "외부감사 대응 수준" 템플릿 개정 (객관적 증거 필수 인용) | | 전자서명 범위 모호 | Part 11 적용범위 정의 문서(QM-IT-001) 초안 예정 |

### kb-eval-20260723-it03-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_us-004", "iteration": 3, "matched_keywords": ["FDA", "QSR"], "profile_id": "ra-us", "scenario_id": "6c224cf5c2b0c913", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/QSR_21CFR820/README.md", "source_hash": "5250406488094d588d38eb1e45c2d8d4b90f093334322d2ded3d50d3a2e72871"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `6c224cf5c2b0c913`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/QSR_21CFR820/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/QSR_21CFR820/README.md)
- Source hash: `5250406488094d588d38eb1e45c2d8d4b90f093334322d2ded3d50d3a2e72871`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QSR

**Source Summary**

- 문서 요약: `README.md`는 해당 규제 지식 폴더의 범위, 주요 자료, 운영 맥락을 요약한 안내 문서입니다.
- 현재 excerpt 핵심: ## 추가 규제 (X-ray 관련) - **21 CFR Part 1020.30 ~ 1020.32**: Radiation Control – Performance Standards for Diagnostic X-ray Systems - **21 CFR Part 1002**: Records and Reports (Radiation-Emitting Products) - **21 CFR Part 1040**: Performance Standards for Light-Emitting Products (관련 시) ## 현황 - 기존 QSR(21 CFR 820)은 2024년 공표된 Quality Management System Regulation...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Design‑Control & QMSR Readiness for a Diagnostic X‑ray System**

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|----------------|
| **CFR Panel** | Imaging / radiology devices are regulated under **21 CFR Part 892** (Radiology – imaging equipment). |
| **Class** | Diagnostic X‑ray systems are traditionally **Class II** (special controls) → 510(k) pre‑market notification is the primary pathway. |
| **Regulatory Basis** | • Part 892 classification rule (no specific section supplied in source – verify separately)<br>• Performance‑standard requirements: **21 CFR Part 1020.30–1020.32** (Radiation Control – Diagnostic X‑ray Systems) <br>• Record/report obligations: **21 CFR Part 1002** (Radiation‑Emitting Products). |
| **Alternative Pathway** | If the device incorporates novel technology without a clear predicate, a **De Novo** classification request may be required. |

---

### 2. Required Submission Evidence  

| Evidence Type | Description | Source Citation |
|---------------|-------------|-----------------|
| **Predicate Device Identification** | Identify a legally marketed 510(k) with the same intended use and technology (e.g., Kxxxxx). | no specific identifier found in source — verify separately |
| **Device Description & Intended Use** | Detailed description, indications, user environment, and labeling. | no specific identifier found in source — verify separately |
| **Performance Testing – Radiation** | • X‑ray output, beam quality, dose measurements per **21 CFR 1020.30–1020.32**.<br>• Compliance with IEC 60601‑2‑33 (electrical safety) and relevant ASTM standards. | Part 1020.30‑32 |
| **Electrical & Light‑Emitting Performance** *(if applicable)* | Verify conformance to **21 CFR 1040** (Light‑Emitting Products). | Part 1040 |
| **Design‑Control Documentation** | • Design History File (DHF) per **21 CFR 820.30**.<br>• Verification & Validation protocols/results.<br>• Risk Management File (ISO 14971). | 21 CFR 820 (QMSR alignment with ISO 13485:2016) |
| **Quality System Compliance** | Evidence of an ISO 13485‑aligned QMS as required by the **2026‑02‑02 QMSR amendment** to 21 CFR 820. | QMSR effective date |
| **UDI Implementation** | Label and device labeling must contain a UDI per **21 CFR 830.10–830.60**, and the device record entered into GUDID. | Part 830 |
| **Software Validation / AI‑ML Change Plan** (if software present) | Predetermined Change Control Plan (PCCP) per FDA guidance (Dec 2024). | no specific identifier found in source — verify separately |
| **Sterilization & Biocompatibility** *(if applicable)* | IEC 60601‑1, ISO 14971 risk analysis for any patient‑contact components. | no specific identifier found in source — verify separately |

---

### 3. Identified Gaps / Missing Information  

| Gap | Impact on Submission |
|-----|----------------------|
| **Predicate device number** | Required to establish substantial equivalence; without it the 510(k) cannot be cleared. |
| **Complete risk‑management file (ISO 14971)** – hazard analysis, FMEA/FMECA, mitigations | Needed for both design‑control and QMSR auditability. |
| **Design Verification & Validation reports** (including radiation performance data) | Must demonstrate compliance with Part 1020 standards. |
| **UDI labeling artwork & GUDID entry** | Mandatory under Part 830; missing UDI blocks clearance. |
| **Software documentation & PCCP** (if any software is included) | Absence prevents acceptance of AI/ML change‑control plan. |
| **Records & reporting procedures for radiation‑emitting products** (Part 1002) | Needed to satisfy post‑market surveillance obligations. |
| **Evidence of QMSR implementation (ISO 13485:2016 alignment)** – organizational structure, training records, internal audit reports | Required for FDA inspection readiness under the 2026 amendment. |

---

### 4. Core Risk Controls (Design‑Control & QMSR)

1. **Risk Management** – ISO 14971 process integrated into DHF; hazard identification, risk evaluation, mitigation, and residual risk acceptance criteria documented.  
2. **Design Verification** – Bench testing of X‑ray output, beam alignment, mechanical stability; compliance to Part 1020 performance standards.  
3. **Design Validation** – Clinical/ simulated use testing per intended use; usability validation for operator interface.  
4. **Change Management** – Predetermined Change Control Plan (PCCP) for software updates; documented change‑impact assessments.  
5. **Document Controls** – Version‐controlled DHF, QMS procedures, and record retention per 21 CFR 820.180.  
6. **Post‑Market Surveillance** – Complaint handling, MDR reporting, periodic safety update (per Part 803/1002).  

---

### 5. Human‑Escalation Triggers  

| Trigger | Required Action |
|--------|-----------------|
| **No identified predicate or unresolved “novel” claim** | Escalate to senior regulatory lead; consider De Novo submission pathway. |
| **Incomplete risk‑management file or missing residual‑risk justification** | Pause 510(k) compilation; assign risk‑analysis team lead for remediation. |
| **Failure to meet Part 1020 performance thresholds in validation testing** | Trigger engineering redesign and repeat verification before submission. |
| **QMSR audit findings (e.g., non‑conformities to ISO 13485 processes)** | Immediate corrective action plan; notify quality assurance manager; suspend submission until closure. |
| **UDI label artwork not approved or GUDID entry missing** | Block submission packaging; engage labeling specialist for urgent correction. |
| **Software change without an approved PCCP** | Halt any software release; route to software governance board for PCCP development. |
| **Regulatory deadline approaching (e.g., 2026‑02‑02 QMSR effective date)** | Escalate schedule risk to program management; allocate resources to achieve compliance. |

---

### 6. Peer Review Prompt  

> *Please review the assumptions made in this draft, especially: (a) the classification of the device under Part 892 vs. any alternative panel; (b) the completeness of the identified performance‑standard citations (Part 1020 series); and (c) any jurisdiction‑specific gaps such as state radiation licenses or CMS/Medicare coverage considerations that may affect the 510(k) strategy.*

--- 

**End of Draft**

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

1. Chunk `136831192110451403`

> ## 추가 규제 (X-ray 관련) - **21 CFR Part 1020.30 ~ 1020.32**: Radiation Control – Performance Standards for Diagnostic X-ray Systems - **21 CFR Part 1002**: Records and Reports (Radiation-Emitting Products) - **21 CFR Part 1040**: Performance Standards for Light-Emitting Products (관련 시)

2. Chunk `18877965943708175`

> ## 현황 - 기존 QSR(21 CFR 820)은 2024년 공표된 Quality Management System Regulation (QMSR)으로 개정됨. - **시행일: 2026년 2월 2일** → ISO 13485:2016과 정합화.

### kb-eval-20260723-it03-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_us-005", "iteration": 3, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "610725bbfbc34725", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "9b8d8cc18e2c1a49f286aa2cb4b0e715490ff1d6d1c1444ec71e851937e5b585"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `610725bbfbc34725`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_2026.md)
- Source hash: `9b8d8cc18e2c1a49f286aa2cb4b0e715490ff1d6d1c1444ec71e851937e5b585`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_2026.md`는 FDA QMSR 2026 전환에 따른 ISO 13485 기반 QMS·design control·inspection 준비 문서입니다.
- 현재 excerpt 핵심: ### 3.6 §820.35 외부 관련 규정 — 21 CFR Part 11 (전자기록·전자서명) 21 CFR Part 11은 **§820.35의 하위항목이 아니다.** Part 11은 FDA 규제 대상 기록을 전자기록/전자서명으로 작성·보관·송수신하는 경우의 무결성·인증 요건을 규정한 독립 규정으로, QMSR 적용 시에도 별도로 적용된다. - 적용 범위: 전자기록·전자서명을 종이/육필 서명과 동등하게 취급하기 위한 시스템 검증·감사추적·접근통제·서명 관리 등. - §820.35와의 관계: 기록 자체(complaints·servicing·UDI 등)는 §820.35 요구를 따르고, 그 기록을 **전자적으로** 작성·보관할 경우 Par...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `QMSR and design-control readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `QMSR and design-control readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - design controls, complaint/CAPA/records, purchasing/service controls, QMSR transition evidence를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR (21 CFR Part 820) & Design‑Control Readiness**

---

### 1. Bottom‑Line Assessment
- **Required regulatory foundation:** The Quality Management System Regulation (QMSR), effective 14 Feb 2026, supersedes the legacy 21 CFR 820 system and aligns with ISO 13485. All design‑control activities, record‑keeping, and corrective actions must be mapped to the new QMSR clauses.
- **Current gaps:**  
  1. No documented **Part 11 validation plan** for electronic records (complaints, servicing, UDI).  
  2. Incomplete SOPs for **label accuracy (§820.45)**, **complaint handling (§820.198)**, and **internal audit/reporting**.  
  3. Training on QMSR changes not completed organization‑wide.  
  4. Management‑review documentation pending final FDA‑readiness check.

---

### 2. Classification / Submission Route (Device‑agnostic)
- The QMSR applies to **all Class I–III medical devices** marketed in the United States.  
- If the product ultimately requires a **510(k) Premarket Notification**, the submission must include:  
  - A statement of compliance with **21 CFR 820 (QMSR)** and, where electronic records are used, **21 CFR Part 11**.  
  - Copies of the current QMS manual, SOPs, validation reports, and training logs as part of the “Quality System” section of the 510(k) (see 21 CFR 807.87).

---

### 3. Required Evidence & Artefacts

| Area | Mandatory Evidence (QMSR) | Part 11 Overlay (if electronic) |
|------|---------------------------|---------------------------------|
| **Design‑Control** | Design History File (DHF) per §820.30, design verification/validation protocols and reports. | Electronic DHF must be validated for integrity, audit trail, and access control (21 CFR Part 11). |
| **Document & Record Control** | Document‑control procedures; master file of SOPs. | Validation of electronic document system – signature binding, versioning, read‑only protection (§820.35 + Part 11). |
| **Label Accuracy** | Procedure for label review and release (**§820.45**). | If labels are generated/managed electronically, apply Part 11 controls to the label‑creation software. |
| **Complaint & Servicing Records** | Complaint handling procedure; MDR linkage (**§820.198**). | Electronic complaint system must meet Part 11 requirements (integrity, audit trail). |
| **Internal Audits** | Audit schedule and reports; corrective‑action plans. | Audit‑report storage electronic – Part 11 compliance required. |
| **Management Review** | Minutes of management‑review meetings, risk‑assessment updates. | Electronic minutes must be validated under Part 11. |
| **Training & Competency** | Training matrix, completion records for all QMSR changes. | Electronic training portal validation (if used). |
| **UDI Management** | UDI assignment and labeling SOPs; system documentation. | Electronic UDI database subject to Part 11 controls. |

*All above artefacts must be retained in accordance with **§820.180** (record retention) and made available for FDA inspection.*

---

### 4. Missing Information (per source)

| Requirement | Source‑provided detail | What is still needed |
|-------------|------------------------|----------------------|
| Part 11 validation scope | “Part 11 is independent; applies when records are electronic” (Excerpt 1). | Specific validation plan, test scripts, and evidence of successful verification. |
| Label accuracy procedure status | §820.45 mentioned in checklist (Excerpt 2) – marked *미착수* (not started). | Completed SOP, change‑control documentation, and validation of any electronic label‑generation tool. |
| Complaint handling update | §820.198 listed, status *진행중*. | Finalized procedure, integration with MDR database, and Part 11 controls for the complaint system. |
| Internal audit & management review readiness | Items 10–11 in checklist (Excerpt 2) marked *미착수*. | Completed audit reports, FDA‑readiness review, and documented management‑review minutes. |
| Training on QMSR changes | Item 13 in checklist (Excerpt 2) – not started. | Full training plan, attendance logs, competency assessment for all staff. |

*All “no specific identifier found in source — verify separately” items have been highlighted; no invented identifiers are included.*

---

### 5. Key Risk Controls & Mitigation Actions

| Risk | Control (QMSR) | Part 11 Enhancement | Action |
|------|----------------|---------------------|--------|
| Loss of electronic record integrity | Document‑control SOP, audit trails (§820.35). | Encryption, digital signatures, immutable logs (Part 11). | Perform system validation; periodic integrity checks. |
| Incomplete label release leading to non‑conformity | Label‑review procedure (§820.45). | Electronic signature of release officer (Part 11). | Finalize SOP; train staff; configure electronic release workflow. |
| Ineffective complaint handling → delayed MDR reporting | Complaint handling SOP (§820.198). | Secure, searchable electronic complaint database (Part 11). | Complete SOP; integrate with MDR portal; validate system. |
| Management‑review gaps → undetected systemic issues | Management review agenda & minutes (§820.20). | Electronic meeting minutes stored under Part 11 controls. | Conduct first FDA‑ready management review; archive minutes electronically. |
| Untrained personnel on new QMSR requirements | Training matrix, competency records (§820.25). | Learning‑management system validation (Part 11). | Roll out mandatory QMSR training; capture completions in validated LMS. |

---

### 6. Citations

- **QMSR framework:** 21 CFR Part 820 (effective Feb 2026, ISO 13485‑aligned).  
- **Electronic records regulation:** 21 CFR Part 11 (independent of §820.35). – *source excerpt 1*.  
- **Label accuracy procedure requirement:** **§820.45** – listed in checklist (excerpt 2).  
- **Complaint handling & MDR linkage:** **§820.198** – listed in checklist (excerpt 2).  
- **Document‑control clause referenced:** **§820.35** – discussed in relation to Part 11 (excerpt 1).  

*No additional instance identifiers were present; any requirement lacking a specific number is flagged for verification.*

---

### 7. Human‑Escalation Triggers

| Trigger | When to Escalate | Recommended Owner |
|--------|------------------|-------------------|
| No validated Part 11 plan within **30 days** of QMSR effective date. | Immediate escalation to QA Director & senior IT lead. |
| Any “미착수” (not started) item in the QMSR checklist remains after **2 weeks** post‑review. | Escalate to regulatory project manager and senior engineering. |
| Management‑review minutes not archived electronically within **15 days** of meeting. | Notify CMO and Compliance Officer. |
| Training completion rate < 90 % after the scheduled rollout. | Elevate to HR Learning & Development head. |
| External audit identifies non‑conformities in Part 11 controls. | Immediate reporting to senior leadership and preparation of FDA 483 response plan. |

---

### 8. Peer Review Prompt
> **Request:** Please review this draft for (a) completeness of the QMSR evidence list, (b) any jurisdiction‑specific gaps (e.g., state‑level registration, MDR alignment), and (c) assumptions made about electronic‑record usage. Highlight missing citations or alternative regulatory pathways that may apply.

---

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

1. Chunk `1032345835256481198`

> ### 3.6 §820.35 외부 관련 규정 — 21 CFR Part 11 (전자기록·전자서명) 21 CFR Part 11은 **§820.35의 하위항목이 아니다.** Part 11은 FDA 규제 대상 기록을 전자기록/전자서명으로 작성·보관·송수신하는 경우의 무결성·인증 요건을 규정한 독립 규정으로, QMSR 적용 시에도 별도로 적용된다. - 적용 범위: 전자기록·전자서명을 종이/육필 서명과 동등하게 취급하기 위한 시스템 검증·감사추적·접근통제·서명 관리 등. - §820.35와의 관계: 기록 자체(complaints·servicing·UDI 등)는 §820.35 요구를 따르고, 그 기록을 **전자적으로** 작성·보관할 경우 Part 11이 추가 적용. - Tier 1: 21 CFR Part 11 (eCFR), FDA "Part 11, Electronic Records; Electronic Signatures — Scope and Application" Guidance(2003, 현행).

2. Chunk `1061385902465548343`

> Part 11 전자기록·전자서명 적합성 점검 — §820.35와 별도 독립 항목 | ☐완료 ☐진행중 ☐미착수 | | | | | 8 | §820.45 라벨 정확성 검사 절차 수립 | ☐완료 ☐진행중 ☐미착수 | | | | | 9 | §820.198 불만처리 MDR 연계 절차 갱신 | ☐완료 ☐진행중 ☐미착수 | | | | | 10 | 내부감사 보고서 FDA 열람 대비 품질 검토 | ☐완료 ☐진행중 ☐미착수 | | | | | 11 | 경영검토 보고서 FDA 열람 대비 품질 검토 | ☐완료 ☐진행중 ☐미착수 | | | | | 12 | 검사 대응 절차 갱신 (7382.850 기반) | ☐완료 ☐진행중 ☐미착수 | | | | | 13 | 교육훈련: QMSR 변경사항 전 직원 교육 | ☐완료 ☐진행중 ☐미착수 | | | |

## ra_eu

### kb-eval-20260723-it03-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_eu-001", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "9e996c9e5706ce37", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `9e996c9e5706ce37`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md)
- Source hash: `ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexIII_PMS_TD_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) for the Three In‑House Products**

| Product | Current MDR Classification* | Typical Conformity‑Assessment Route | Core PMS Deliverables (MDR references) |
|---------|-----------------------------|-------------------------------------|----------------------------------------|
| X‑ray Detector (imaging panel) | **Class IIa** – Rule 17 (recording diagnostic X‑ray images) | **Annex IX** (full QMS + technical documentation assessment) – NB review of the Technical Documentation and PMS system. | • PSUR, update every **2 years** (Art. 86(2))<br>• PMCF plan & report (Annex XIV Part B)<br>• Clinical Evaluation Report (CER) (Annex XIV Part A) |
| Hand‑held X‑ray Source (portable generator) | **Class IIb** – Rule 10 (active device emitting ionising radiation for diagnostic use) | **Annex IX** (or Annex X + Annex XI if a type‑examination is preferred) | • PSUR, update every **1 year** (Art. 86(2))<br>• PMCF plan & report (Annex XIV Part B)<br>• CER (Annex XIV Part A) |
| GUI Software (SaMD – image display & interpretation aid) | **Class IIa** – Rule 11 (software providing diagnostic information) | **Annex IX** (QMS‑based route) – mandatory for SaMD of Class IIa/IIb. | • PSUR, update every **2 years** (Art. 86(2))<br>• PMCF plan & report (Annex XIV Part B)<br>• CER (Annex XIV Part A) |

\*Classification derived from the mapping of active‑device rules provided in the MDR knowledge base.

---

## 1. Required Clinical & Technical Evidence  

| Requirement | Source(s) | Reference |
|-------------|-----------|------------|
| **Clinical Evaluation Report (CER)** – systematic literature review, equivalence assessment, benefit–risk analysis. | • “CER” column in source table [1] | Annex XIV Part A; kept current under Art. 61 |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** – objectives, methodology, data collection schedule, evaluation of clinical performance. | • “PMCF 필요성” rows in source table [1] | Annex XIV Part B |
| **PMS Plan** – description of PMS system, data sources, responsibilities, and procedures. | • “PMS 담당 데이터 소스” & Table 1‑Sources of Information [2] | Art. 84 |
| **Periodic Safety Update Report (PSUR)** – benefit–risk conclusions, PMCF main findings, sales/using population data. | • PSUR update frequency in source table [1]; “PSUR 갱신 주기”. | Art. 86(1‑2) |
| **Risk Management File (RMF)** – ISO 14971‑based risk analysis, evaluation of residual risks, and verification of risk controls. | • “CER, RMF” column in source table [1] | Annex I §10‑22 (risk management) |
| **Performance Test Data** – DQE degradation trends for detector; dose monitoring data for handheld source; software bug log & IEC 62304 maintenance records for GUI. | • Specific test data references in source table [1] | IEC 62220‑1‑1 (DQE), IEC 62304, IEC 62366‑1 (usability) |
| **Labeling & IFU** – compliance with Annex I §23 (information supplied). | Not explicitly listed → missing. | Annex I Chapter III (§23) |

---

## 2. Gaps / Missing Information  

| Gap | Why it matters | Suggested Action |
|-----|----------------|------------------|
| **Detailed PMCF protocol** – objectives, sample size, endpoints, statistical analysis plan. | NB must verify that post‑market data will substantiate safety/ performance claims over the device life‑cycle. | Draft a full PMCF plan per Annex XIV Part B; include prospective clinical study for handheld source (dose exposure). |
| **Usability evaluation evidence** for GUI software (IEC 62366‑1). | Needed to demonstrate that user errors flagged in PMS (e.g., “SW 오류, 영상 표시 오류”) are mitigated. | Conduct formative & summative usability testing; integrate findings into risk management file. |
| **Trend analysis methodology** – quantitative thresholds for DQE decline, dose exceedance, battery anomalies. | Trend reporting (Art. 88) requires predefined trigger levels to initiate corrective actions. | Define numeric limits (e.g., >10 % increase in DQE loss over 6 months) and embed in PMS plan. |
| **Labeling / IFU draft** – especially warnings for ionising radiation exposure & software use. | Required by Annex I §23; also essential for competent authority review. | Produce labeling package, map to GSPR §§16‑22 as appropriate. |
| **Clinical data on equivalence claims** for X‑ray Detector (equivalence claim review mentioned). | NB will request justification that the comparator device is truly equivalent under MDR (Annex XIV Part A). | Assemble side‑by‑side technical comparison, clinical literature supporting equivalence. |
| **Verification of battery safety measures** for handheld source (mechanical damage, battery abnormality). | Battery failures can lead to hazardous situations; must be covered in risk control and PMS monitoring. | Include accelerated ageing tests, failure mode analysis, and monitoring of “배터리 이상” incidents. |

---

## 3. Key Risk Controls (derived from RMF & PMS data)  

| Hazard / Failure Mode | Control(s) Implemented | Evidence Needed |
|-----------------------|------------------------|-----------------|
| **Excess patient dose** (handheld source) | Real‑time dose meter with alarm, automatic shut‑off at preset limit. | Dose monitoring data (source table [1]), verification test reports. |
| **DQE degradation** (detector) | Periodic self‑test; threshold alert when DQE falls >X % from baseline. | Trend data from “DQE 저하” source, defined trend limits. |
| **Battery over‑temperature / rupture** | Battery management system with temperature sensor & cut‑off circuit. | Accelerated ageing & safety test reports. |
| **Software display error** (GUI) | Redundant rendering engine; runtime exception handling; periodic software updates per IEC 62304. | Bug log, maintenance records, IEC 62304 compliance evidence. |
| **User misuse by lay persons** (if intended for non‑clinical settings) | Mandatory training module, clear IFU warnings, ergonomic design per IEC 62366‑1. | Usability test results, training material. |

All controls must be mapped to the relevant General Safety and Performance Requirements (GSPR) in Annex I (§16‑22) and documented in the RMF.

---

## 4. Human‑Escalation Triggers  

| Trigger Condition | Action & Responsible Party |
|-------------------|-----------------------------|
| **Serious incident or FSCAs** reported via Vigilance system (source [2] row 1). | Immediate notification to NB (Art. 87) and internal escalation to PMS Lead; initiate corrective action plan within 10 days. |
| **Trend of DQE loss >10 % over two consecutive quarters** (derived from “DQE 저하” source). | PMS Team raises a Trend Report (Art. 88); convene Risk Management Review; consider field safety corrective action. |
| **Dose‑overrun events exceeding 5 % of procedures in one quarter** (source [1] “선량 초과”). | Trigger PMCF interim analysis; if confirmed, update labeling & training, notify NB. |
| **Recurring software error ≥3 identical bugs within 30 days** (source [1] “SW 오류”). | Initiate Software Corrective Action Procedure per IEC 62304; issue field safety notice if user risk identified. |
| **Missing quarterly PMS data entry** (e.g., no updated complaint log). | Automatic escalation to Quality Manager; suspend PSUR update until data supplied; notify NB of delay per Art. 84/86. |
| **Failure to produce updated PSUR by the scheduled interval** (1 yr for handheld, 2 yr for others). | Immediate notification to NB; prepare interim PSUR covering the gap; risk assessment of impact on compliance status. |

---

## 5. Regulatory Judgment  

* The three in‑house products are correctly classified under MDR Rules 17, 10, and 11 (Class IIa/IIb).  
* The appropriate conformity‑assessment route is **Annex IX** for all three (full QMS & technical documentation assessment), with the optional Annex X + XI path only for the Class IIb handheld source if a type‑examination is preferred.  
* Core MDR deliverables (CER, PMCF plan/report, PSUR, PMS Plan, RMF, labeling) are identified, but **significant gaps** remain in: detailed PMCF methodology, usability evidence for the GUI, quantitative trend thresholds, complete labeling/IFU package, and documented risk controls for battery safety.  
* Immediate human escalation should be triggered by any serious incident, adverse trends, or missed PMS reporting deadlines as delineated above.

---

### Peer‑Review Request  

> **To a fellow RA colleague:** Please review the assumptions made regarding (1) the chosen conformity‑assessment route for each class, (2) the sufficiency of the identified evidence sources versus MDR Annex XIV and Art. 83‑86 requirements, and (3) any jurisdiction‑specific omissions (e.g., national competent authority guidance on handheld X‑ray devices). Highlight gaps or propose additional data that should be captured before NB submission.

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

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

### kb-eval-20260723-it03-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_eu-002", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "142fdc3adb085399", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `142fdc3adb085399`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/README.md)
- Source hash: `30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules) ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software...
- 이 항목의 평가 포인트: 이 source는 PMS/PMCF 전용 문서가 아닐 수 있습니다. 좋은 답변은 surveillance 결론을 단정하지 않고 PMS/PMSR/PMCF에 연결되는 근거와 한계를 구분해야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – X‑ray Diagnostic Device (Ionising‑radiation emitter)**  

---

### 1. Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Device type** | Active diagnostic device that emits ionising radiation for imaging | Rule 10 (excerpt [2]) – “이온화 방사선 방출 진단기기 … Class IIb” |
| **MDR class** | **Class IIb** (Rule 10) | Annex VIII, Rule 10; confirmed by source excerpt [2] |
| **Conformity‑assessment route** | • **Annex IX** – Full quality‑management system assessment + technical documentation review  <br>• **OR** Annex X (type‑examination) followed by Annex XI for production conformity verification (optional, but still NB involvement) | MDR 2017/745 – Annex IX or Annex X/XI applicable to Class IIb devices |
| **Notified Body involvement** | Mandatory (Class IIb) | MDR Art. 52 & Annex IX/ X |

> **Citation style:** framework references (Rule 10, Annex VIII, IX, X, XI) are stated as facts; no specific identifier from the source is required beyond what is quoted.

---

### 2. Evidence Package Required for NB Submission  

| Evidence | Minimum content | Relevant MDR provision |
|----------|----------------|------------------------|
| **Technical Documentation** (TD) | – Device description, specifications, accessories <br>– Intended purpose / indications <br>– Design & manufacture information <br>– Labels & IFU (Annex I §23) <br>– Risk Management File (ISO 14971) <br>– Verification & validation data <br>– GSPR checklist | Annex II; GSPR – Annex I (see risk‑control section below) |
| **Clinical Evaluation Report (CER)** | – State‑of‑the‑art literature review (Rule 10 devices) <br>– Clinical data from investigations or equivalence <br>– Benefit‑risk determination | Annex XIV Part A; kept current under Art. 61 |
| **Post‑Market Surveillance (PMS) Plan** | – System description (Art. 83) <br>– Planned activities, timelines, responsibilities (Art. 84) | Art. 83 & 84; Annex III |
| **Periodic Safety Update Report (PSUR)** | – Benefit‑risk conclusions (Art. 86(1)(a)) <br>– Main PMCF findings (Art. 86(1)(b)) <br>– Sales volume & user population (Art. 86(1)(c)) <br>– Updated at least annually for Class IIb (Art. 86(2)) | Art. 86 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | – Objectives, methodology, sample size, endpoints <br>– Alignment with CE‑Marking requirements (Annex XIV Part B) | Annex XIV Part B |
| **Usability Engineering File** (if UI critical) | – Usability test results, risk analysis of use errors | IEC 62366‑1 (referenced in GSPR §22) |
| **Software Verification & Validation** (if applicable SaMD component) | – IEC 62304 lifecycle documentation <br>– Classification justification per Rule 11 | Rule 11 (excerpt [2]); IEC 62304 |

---

### 3. Missing Information / Gaps to Resolve  

1. **Exact Intended Use Statement** – precise clinical indication(s), patient population, and mode of use.  
2. **Device Architecture Details** – description of X‑ray tube, control electronics, any connected software (SaMD) and their interfaces.  
3. **Risk Management File** – hazard analysis outcomes, especially radiation exposure levels, electrical safety, and failure modes.  
4. **Clinical Data Sources** – list of performed clinical investigations or equivalence data; raw datasets are not yet supplied.  
5. **State‑of‑the‑Art (SOTA) Literature Review** – systematic search strategy, inclusion/exclusion criteria, key references.  
6. **PMCF Plan Draft** – objectives, endpoints, monitoring schedule, and resources.  
7. **PMS Plan Detail** – post‑market data collection methods, trend analysis procedure, responsibilities matrix.  
8. **Label & IFU Content** – verification that all GSPR §23 requirements (warnings, contraindications, radiation safety information) are addressed.  
9. **Software Classification Justification** – if a software component influences diagnosis, justification for Rule 11 class (IIa/IIb/III).  

> *No specific identifiers related to the above gaps appear in the source excerpts; therefore “verify separately” is noted where appropriate.*

---

### 4. Risk‑Control Measures & Regulatory Citations  

| GSPR requirement | Typical control(s) for an X‑ray diagnostic device | MDR citation |
|------------------|---------------------------------------------------|--------------|
| **§16 – Protection against radiation** (incl. ionising) | • Shielding design, dosimetry testing <br>• Compliance with IEC 60601‑2‑54 (radiography) <br>• User training on exposure limits | Annex I §16 |
| **§18 – Active devices & connected systems** | • Electrical safety (IEC 60601‑1) <br>• Redundant interlocks for emission control | Annex I §18 |
| **§20 – Mechanical/thermal risks** | • Mechanical robustness of tube housing, thermal protection circuitry | Annex I §20 |
| **§22 – Devices intended for lay persons** (if applicable) | • Clear visual and auditory warnings, ergonomic UI | Annex I §22 |
| **§23 – Information supplied with the device** | • IFU containing radiation safety advice, contraindications, maintenance schedule | Annex I §23 |
| **§17 – Electronic programmable systems / software** | • Secure firmware updates, audit trails, compliance with IEC 62304 | Annex I §17 |

Risk management must be performed per **ISO 14971**, linked to the above GSPR sections and documented in the Technical Documentation (Annex II).

---

### 5. Human‑Escalation Triggers  

| Trigger | Action Required | Who escalates |
|---------|-----------------|---------------|
| **Absence of a complete Intended Use statement** | Pause TD finalisation; obtain clinical stakeholder input | Project Lead → RA Manager |
| **No validated clinical data or equivalence justification** | Stop CER drafting; commission clinical investigation or literature search | Clinical Research Team → RA Manager |
| **Risk Management File missing or incomplete** | Suspend NB submission; conduct full risk analysis | Risk Management Engineer → QA Director |
| **PMCF plan not defined** | Delay PMS system approval; develop PMCF protocol | Post‑Market Surveillance Lead → RA Manager |
| **Software component classification uncertain (Rule 11)** | Conduct a dedicated SaMD classification workshop; update TD accordingly | Software Engineering Lead → Regulatory Affairs |
| **Label/IFU lacking required GSPR §23 items** | Halt packaging design; revise labeling content | Marketing & Labeling Team → Compliance Officer |

Each trigger should be logged in the project’s risk register and reported to senior management before any further regulatory steps.

---

### 6. Peer‑Review Prompt  

> *"Colleague, please review the classification justification (Rule 10 – Class IIb) and the chosen conformity‑assessment route (Annex IX vs. Annex X/XI). Verify whether additional EU‑specific guidance (MDCG 2023‑1 on ionising radiation devices) introduces any supplemental evidence requirements not captured above, especially concerning radiation safety testing and post‑market clinical follow‑up. Highlight any jurisdictional gaps or assumptions that may need adjustment."*

---

### 7. Reusable RA Judgment (recorded for future cases)

> **Judgment:** An X‑ray diagnostic device emitting ionising radiation is classified as **Class IIb** under MDR 2017/745 Rule 10 (per source excerpt [2]). The mandatory regulatory pathway involves a Notified Body via **Annex IX** (full QMS + TD assessment) or **Annex X/XI** (type‑examination plus production verification). Submission must include the full Technical Documentation (Annex II), a Clinical Evaluation Report (Annex XIV Part A), a PMS plan (Art. 84, Annex III), a PSUR (Art. 86) and an appropriate PMCF plan (Annex XIV Part B). Key risk controls derive from GSPR §§16, 18, 20, 22, 23; compliance with IEC 60601‑2‑54, ISO 14971, IEC 62304/62366‑1 is mandatory.  

> **Escalation thresholds** are flagged whenever any of the critical evidence items (intended use, clinical data, risk management file, PMCF plan, labeling) are missing or insufficient, requiring senior RA sign‑off before proceeding to NB engagement.

--- 

*End of draft.*

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

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20260723-it03-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_eu-003", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3fec1d69a7ddb7df", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `3fec1d69a7ddb7df`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week04_MDR_EU_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `Week04_MDR_EU_체계_상세.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUF...
- 이 항목의 평가 포인트: 이 source는 PMS/PMCF 전용 문서가 아닐 수 있습니다. 좋은 답변은 surveillance 결론을 단정하지 않고 PMS/PMSR/PMCF에 연결되는 근거와 한계를 구분해야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning  
(EU Medical Device Regulation 2017/745)**  

---

### 1. Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|---------------|------------------|
| **Device class** | To be derived from the manufacturer’s self‑classification using Annex VIII rules (apply sequentially, highest resulting class applies). | Article 51 + Annex VIII (Rule 1‑22) – source [2] |
| **Conformity‑assessment route** | Dependent on the class: <br>• Class I (non‑sterile, non‑measuring): self‑declaration (Annex IV). <br>• Class IIa/IIb/III: technical documentation assessed by a Notified Body under **Annex IX** (QMS + TD) or **Annex X** (type‑examination) or **Annex XI** (production conformity verification) as appropriate to the device. | MDR Annex IX, X, XI |

*Human‑escalation trigger*: **Uncertainty on applicable rule or class** → raise to senior RA for Competent Authority (CA) consultation or MDCG borderline manual (see source [2]).

---

### 2. Required Evidence Packages  

| Evidence | What must be submitted / maintained | MDR reference |
|----------|--------------------------------------|---------------|
| **Clinical Evaluation Report (CER)** – kept up‑to‑date | Systematic literature review, clinical data from own investigations or equivalence, benefit–risk analysis. | Annex XIV Part A; Art. 61 (source [1]) |
| **PMCF Plan & PMCF Evaluation Report** | Objectives, methodology, population, endpoints, timelines, and final evaluation of results. | Annex XIV Part B |
| **Post‑Market Surveillance (PMS) Plan** | Description of PMS system, data collection methods, responsibilities, reporting schedule. | Art. 84 |
| **PMS Reports** – Class I: summary report; Class IIa/IIb/III: Periodic Safety Update Report (PSUR) | PSUR content: benefit‑risk conclusions, PMCF findings, sales volume & user population (Art. 86(1)). Frequency: annually for IIb/III, biennially for IIa (Art. 86(2)). | Art. 85 (Class I), Art. 86 |
| **Vigilance / Incident Reporting** | Immediate reporting of serious incidents and field‑safety corrective actions (FSCA). | Art. 87 (source [1]) |
| **UDI Implementation** | Registration in EUDAMED, assignment of device identifier, linkage to PMS data. | Annex II §23 (labeling), EU MDR UDI requirements (no specific article cited in source) |
| **Risk Management File** | ISO 14971‑based risk analysis, evaluation of residual risks, verification of risk controls. | Annex I GSPR §§ 16‑22; implementation via ISO 14971 |

*Human‑escalation trigger*: **Absence of a validated PMCF plan** or **incomplete PSUR** → pause submission and request supplemental clinical data.

---

### 3. Gap / Missing Information (to be collected before NB submission)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended purpose & indications** | Drives classification rule, required clinical evidence, labeling (§23). | Obtain from the manufacturer’s specification sheet. |
| **Device architecture & technology description** | Needed for risk management (GSPR §16‑§22) and to identify applicable IEC standards (e.g., IEC 60601‑2‑54 for X‑ray systems). | Request Engineering Design Dossier. |
| **Applicable Annex VIII rule(s)** – concrete rule number (e.g., Rule 9, 10, 11, 17) | Determines class and therefore the NB route. | Conduct rule‑by‑rule mapping with product team. |
| **Clinical data sources** – published literature, registries, existing CE‑marked equivalents | Supports CER & PMCF justification. | Compile systematic review matrix. |
| **Post‑market data collection strategy (e.g., registry, complaint handling, field safety notices)** | Enables PMS plan and PSUR content. | Draft data‑flow diagram; confirm with quality department. |
| **UDI assignment & EUDAMED entry status** | Mandatory for traceability and PMS linkage. | Verify UDI registration in EUDAMED. |
| **Applicable IEC/ISO standards (e.g., IEC 62304, IEC 62366‑1)** | Provide “state of the art” evidence; required under Annex I GSPR §17‑§18. | List all harmonised standards claimed. |

*Human‑escalation trigger*: Any item above flagged as **“unavailable after two request cycles”** → escalation to Project Lead / Senior RA for timeline reassessment.

---

### 4. Core Risk Controls (to be reflected in the Technical Documentation)

1. **Risk Management Process** – ISO 14971, with risk analysis, evaluation of residual risks, and verification of control measures (Annex I §§ 16‑22).  
2. **Usability Engineering** – IEC 62366‑1 compliance for devices intended for lay users or requiring specific user interaction (§22).  
3. **Software Safety** – If software is a medical device, apply IEC 62304 lifecycle and consider Annex I §17 (electronic programmable systems).  
4. **Radiation Protection** – For active devices emitting ionising radiation, demonstrate compliance with GSPR §16.4 (protect against radiation) and relevant IEC standards (e.g., IEC 60601‑2‑54).  
5. **Labeling & IFU** – Conform to Annex I Chapter III (§23) ensuring clear instructions, warnings, and UDI presentation.

*Human‑escalation trigger*: **Residual risk that cannot be justified as acceptable** after risk analysis → halt submission and request design mitigation.

---

### 5. Citation Summary (per the source material)

| Regulatory element | Source citation |
|--------------------|-----------------|
| Clinical Evaluation Report requirement – Article 61, MDR Annex XIV | source [1] |
| Vigilance / serious‑incident reporting – Art. 87 | source [1] |
| Classification principle – Article 51 + Annex VIII (sequential rule application) | source [2] |
| Reference to MDCG Manual on borderline & classification (2023‑09 v2.1.1) | source [2] |

*No other instance identifiers (e.g., specific case numbers, national decree numbers) were present in the excerpts; therefore none are fabricated.*

---

### 6. Human‑Escalation Triggers – Decision Points

| Situation | Trigger | Escalation path |
|-----------|---------|-----------------|
| **Unclear classification rule or class** | Unable to assign a definitive Annex VIII rule after two expert reviews. | Notify Senior RA → request Competent Authority (CA) clarification per MDCG borderline guidance. |
| **Missing clinical evidence for CER/PMCF** | No acceptable clinical data source identified. | Pause submission, raise to Clinical Affairs Lead for study design or literature search. |
| **Incomplete PSUR / PMS plan** | Gaps in incident trend analysis or sales‑volume data. | Alert Project Manager → sponsor supplemental data collection before NB audit. |
| **Residual risk not justified** | Risk analysis yields unacceptable residual risk after all controls. | Immediate stop‑gap to Engineering for design change; senior RA reviews risk acceptability. |
| **Regulatory deadline breach** (e.g., PSUR not updated within the mandated period) | Calendar check shows overdue reporting. | Flag to Compliance Officer → consider corrective actions and possible vigilance notification. |

---

### 7. Peer‑Review Prompt  

> *“Colleague, please challenge the assumptions made above:  
> 1. Is the proposed use of Annex IX for all Class IIa/IIb/III devices appropriate given the product’s likely risk profile?  
> 2. Are there any MDR articles or annexes that we have omitted which could affect the PMS/PMCF evidence requirements (e.g., Art. 83–86 interaction)?  
> 3. Does the gap list capture all information needed for a complete technical file, especially concerning UDI and harmonised standards?  
> 4. Are any jurisdiction‑specific obligations (e.g., Korean Medical Device Act §31) relevant to our EU submission strategy?”*  

--- 

**End of draft.**

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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20260723-it03-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_eu-004", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "5f56851f36d7a4ee", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `5f56851f36d7a4ee`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PMS_Plan_MDR_Article84_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PMS_Plan_MDR_Article84_템플릿.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | PMS 항목 | 특화 내용 | |---|---| | 주요 위험 신호 | SW 오류로 인한 진단 오류, 데이터 손실, 사이버보안 취약점 | | 핵심 수집원 | SW 버그 리포트, 사이버보안 취약점 공개 DB (CVE, NIST NVD) | | PMCF 방법 | 사용성 평가 (IEC 62366), 실사용 에러 데이터 수집 | | 주요 표준 모니터링 | IEC 62304 개정, MDCG 2019-16 Rev.1 사이버보안, MDCG 2021-6 SaMD | | MFDS 특이사항 | 디지털의료제품법(2024.09.26 시행) 적용 여부 검토 [검증 필요] | --- ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning**  
*Applicable to the three X‑ray product families listed in the source matrix*  

---

## 1. Device Portfolio & MDR Classification

| # | Device (as described) | MDR Class (estimate) | Governing Rule(s) (Annex VIII) | Primary Intended Use (to be confirmed) |
|---|-----------------------|----------------------|--------------------------------|----------------------------------------|
| 1 | **X‑ray Detector** – image receptor for projection radiography/fluoroscopy | **Class IIa / IIb** (dual estimate) | Rule 17 (image recording device → IIa) & Rule 10 (active component that may influence diagnosis → IIb where diagnostic impact is high) | Capture diagnostic X‑ray images; may be used in conjunction with a source. |
| 2 | **Handheld X‑ray Source** – portable generator/emitter for diagnostic radiology | **Class IIb** | Rule 10 (active device emitting ionising radiation for diagnosis → IIb) | Directly emit ionising radiation to produce diagnostic images. |
| 3 | **촬영실 GUI SW (SaMD)** – software that visualises and assists interpretation of X‑ray images in the exam room | **Class IIa** (MDR §22) | Rule 11 (software providing information for diagnostic decisions → IIa, unless decision could cause death/irreversible deterioration) | Provide user‑interface & decision support for image review. |

*Note*: The classification of the X‑ray Detector must be finalised once the exact functional relationship with the source is clarified – if it purely records images without influencing exposure it remains IIa (Rule 17); if it also controls exposure parameters, IIb (Rule 10) applies.

---

## 2. Conformity‑Assessment Route

All three devices fall under **Annex IX** (Full quality‑management system + technical documentation assessment) because they are Class IIa/IIb and will require a Notified Body (NB) review of:

* Annex II – Technical Documentation (including risk management, clinical evaluation & PMS plan).  
* Annex X or XI are not applicable as there is no type‑examination or production conformity verification only route for these classes.

---

## 3. Required Post‑Market Evidence (MDR)

| Requirement | Reference | Deliverable(s) | Frequency / Timing |
|-------------|-----------|----------------|--------------------|
| **PMS Plan** (overall system) | Art. 84 | Documented PMS plan covering all three devices, defining data sources, signal detection methods, responsible parties. | Established before CE marking; updated continuously. |
| **PMCF Plan** (clinical follow‑up) | Annex XIV Part B | Detailed PMCF protocol (objectives, population, endpoints, data collection methods). | Initiated at launch; revised as new evidence emerges. |
| **PMCF Evaluation Report** | Annex XIV Part B | Results of the PMCF activities, benefit‑risk conclusions. | Integrated into periodic PMS updates; submitted with PSUR. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 | Summary of safety data, PMS findings, PMCF results, sales volume & user population size. | Class IIa – every 2 years; Class IIb – annually. |
| **Vigilance Reporting** (Serious Incidents / FSCA) | Art. 87 | Immediate notification to the NB and competent authority for serious adverse events. | Within 15 days of awareness. |
| **Trend Reporting** | Art. 88 | Aggregated trend analysis of non‑serious incidents. | Annually, submitted with PSUR. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A | Comprehensive clinical data file (state‑of‑the‑art literature, clinical investigations, PMCF). | Updated continuously; final version at CE marking. |

---

## 4. Evidence Gaps & Required Clarifications

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Exact Intended Purpose Statements** (incl. patient population, clinical setting) | Drives classification, risk analysis and clinical evidence scope. | Obtain from product development dossier; confirm for each device. |
| **Risk Management File outcomes (ISO 14971)** – particularly mitigations for SW‑induced diagnostic error, data loss & cyber‑security threats. | Needed for Annex I §§16‑18 compliance and to justify PMS signal‑detection criteria. | Complete risk analysis; map controls to IEC 62304, IEC 62366‑1, MDCG 2019‑16 Rev. 1. |
| **Clinical Data Sources** (clinical investigations, registries, literature) for the Detector & Source – especially evidence that image quality meets diagnostic performance standards. | Required for CER and PMCF baseline. | Conduct a limited clinical investigation or acquire relevant post‑market data from existing installations. |
| **Software Classification Rationale** – justification for using MDR §22 (SaMD) vs Rule 11 classification. | Impacts NB review scope and documentation depth. | Provide a decision tree linking software functions to rule criteria. |
| **MFDS Digital Medical Products Law applicability** (2024‑09‑26). | May impose additional post‑market obligations in Korea; affects global PMS coordination. | Verify whether the devices are marketed in Korea; if so, map MFDS requirements to MDR PMS plan. |
| **Usability Evaluation Results** (IEC 62366) for the GUI SW. | Supports mitigation of diagnostic‑error risk and informs PMCF data collection. | Execute formal usability study; incorporate findings into PMCF. |

---

## 5. Core Risk Controls (linked to identified hazards)

| Hazard | MDR General Safety & Performance Requirement | Control(s) Implemented | Standard / Guidance |
|--------|----------------------------------------------|------------------------|----------------------|
| SW error → diagnostic misinterpretation | § 18 (Active devices & active components) + § 22 (Lay‑person use where applicable) | – Development according to IEC 62304 (software life‑cycle). <br>– Usability engineering per IEC 62366‑1. <br>– Decision support validation against clinical benchmarks. | IEC 62304, IEC 62366‑1 |
| Data loss / integrity breach | § 16 (Protection against radiation) – extended to data; § 19 (Active implantable devices) principle of traceability | – Secure data storage & backup per ISO 27001 controls. <br>– Integrity checks in software architecture. | IEC 62304, MDCG 2019‑16 Rev.1 |
| Cyber‑security vulnerability (CVE/NVD exposure) | § 16.4 (Radiation protection) – interpreted to include electromagnetic safety; § 18 (Active devices) | – Threat modelling & mitigation per MDCG 2021‑6 SaMD. <br>– Regular patching schedule; CVE monitoring. | MDCG 2019‑16 Rev.1, MDCG 2021‑6 |
| Incorrect exposure settings (Handheld source) | § 18 (Active devices) – energy delivery control | – Integrated interlock & dose‑limiting algorithms validated per IEC 60601‑2‑54 (radiography apparatus). <br>– Built‑in safety limits. | IEC 60601‑2‑54 |
| Image quality degradation (Detector) | § 16 (Radiation protection) – performance of imaging devices | – Conformance to IEC 62220‑1‑1 (DQE measurement). <br>– Calibration procedures documented in PMS plan. | IEC 62220‑1‑1 |

---

## 6. PMS & PMCF Data Collection Architecture

| Data Source | Signal Type | Capture Method | Frequency |
|------------|------------|----------------|-----------|
| **SW bug reports** (internal defect tracking) | Diagnostic error, software crash | Automated export to NB‑compatible XML format | Continuous |
| **CVE / NIST NVD feeds** | Cyber‑security vulnerability disclosure | API pull into risk‑monitoring dashboard | Daily |
| **Usability testing results** (IEC 62366) | User errors in GUI | Structured observation & questionnaire; stored in secure database | At each release |
| **Clinical error logs from installations** | Misdiagnosis, image artefacts | Remote telemetry (secure VPN) → aggregated incident log | Monthly batch upload |
| **Sales & user population data** | Exposure denominator for PSUR | ERP export + market research | Annually |

All collected signals feed into the **PMS Plan’s “Signal Detection Criteria”** (thresholds defined per risk severity). When a signal exceeds the predefined trigger, the following escalation is required.

---

## 7. Human‑Escalation Triggers (when to involve Notified Body / Competent Authority)

| Trigger | Action & Deadline |
|---------|-------------------|
| **Classification uncertainty** (e.g., Detector may be IIa or IIb) | Pause CE marking; request NB clarification; document decision before final technical file submission. |
| **Missing clinical evidence for a claim** (e.g., no data supporting diagnostic performance) | Conduct supplemental investigation; update CER & PMCF plan; do not submit NB audit until resolved. |
| **Serious incident with potential death or irreversible deterioration** (per Art. 87) | Submit vigilance report to the competent authority and NB within 15 days; initiate field safety corrective action (FSCA). |
| **High‑severity cyber‑security vulnerability (CVSS ≥7.0)** identified in CVE feed | Issue security advisory, apply patch, notify users, submit incident summary to NB as part of PSUR & trend report. |
| **Data loss affecting >5 % of stored patient studies** | Immediate root‑cause analysis, remediation plan, and notification to NB; include findings in next PSUR. |
| **MFDS law applicability confirmed for any device** | Align Korean PMS activities with MFDS requirements; inform NB of additional obligations; ensure dual reporting compliance. |
| **PMCF results indicate a negative benefit‑risk trend** | Suspend market access pending corrective actions; submit updated risk‑benefit analysis to NB and competent authority. |

---

## 8. Summary Judgment

* The three devices are **Class IIa/IIb** under MDR, requiring **Annex IX** conformity assessment with a full quality‑management system review by a Notified Body.  
* A comprehensive **PMS plan (Art. 84)**, **PMCF plan & report (Annex XIV Part B)**, and **PSURs (Art. 86)** must be established per the frequencies in the source matrix (annual for Class IIb, biennial for Class IIa).  
* Critical missing items are precise intended‑use statements, complete risk‑management outputs, robust clinical evidence, and confirmation of Korean MFDS applicability. These gaps must be closed before the NB audit can be scheduled.  
* The identified hazards (diagnostic error, data loss, cyber‑security) are addressed through IEC 62304/62366 controls, MDCG cyber‑security guidance, and IEC 62220‑1‑1 performance testing.  

**Human escalation is required whenever classification, clinical evidence, serious safety signals, or cross‑jurisdictional obligations remain unresolved.**  

---

## 9. Peer Review Prompt

> **Colleague request:** Please review the above assumptions on device classification (especially the dual estimate for the X‑ray Detector), the completeness of the listed risk controls, and any jurisdiction‑specific gaps (e.g., Korean MFDS digital‑medical‑products law). Confirm whether additional MDR annexes or MDCG guidance documents should be referenced, and flag any items that still need primary source verification.

---

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

1. Chunk `1138445053784347810`

> | PMS 항목 | 특화 내용 | |---|---| | 주요 위험 신호 | SW 오류로 인한 진단 오류, 데이터 손실, 사이버보안 취약점 | | 핵심 수집원 | SW 버그 리포트, 사이버보안 취약점 공개 DB (CVE, NIST NVD) | | PMCF 방법 | 사용성 평가 (IEC 62366), 실사용 에러 데이터 수집 | | 주요 표준 모니터링 | IEC 62304 개정, MDCG 2019-16 Rev.1 사이버보안, MDCG 2021-6 SaMD | | MFDS 특이사항 | 디지털의료제품법(2024.09.26 시행) 적용 여부 검토 [검증 필요] | ---

2. Chunk `1142345122918011337`

> ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (추정) | PMS Plan 의무 | 보고서 유형 | FDA 522 | MFDS 시판후조사 | |---|---|---|---|---|---| | **X-ray Detector** | Class IIa/IIb | **필수** | PSUR 2년/매년 | 해당 없음 (비이식형) | 신개발 시 3~4년 조사 | | **Handheld X-ray Source** | Class IIb | **필수** | PSUR 매년 | 해당 없음 (비이식형) | 신개발 시 4~6년 조사 | | **촬영실 GUI SW (SaMD)** | Class IIa (MDR §22) | **필수** | PSUR 2년 | 해당 없음 | 소프트웨어 신개발 시 해당 | ---

### kb-eval-20260723-it03-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_eu-005", "iteration": 3, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "f9ca9ca41865bbca", "source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md", "source_hash": "62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f9ca9ca41865bbca`
- Source: `github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/EUDAMED_%EB%AA%A8%EB%93%88%EB%B3%84_%EB%93%B1%EB%A1%9D_%EC%8B%A4%EB%AC%B4%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77`
- Focus: PMS and PMCF planning
- Matched keywords: EUDAMED

**Source Summary**

- 문서 요약: `EUDAMED_모듈별_등록_실무가이드.md`는 EUDAMED 등록·변경통제·모듈별 운영 실무 문서입니다.
- 현재 excerpt 핵심: ### 5-A. 데이터베이스 등록 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR (EU) | |---|---|---|---| | 등록 DB | GUDID (FDA UDI DB) | UDI포털 (mfds.go.kr) | EUDAMED | | 의무화 시점 | 등급별 단계적 완료 | 2025 기준 진행 중 | 2026-05-28 (4개 모듈) | | 경제주체 등록 | FDA Establishment Registration (21 CFR 807) | 의료기기 제조업 허가 | SRN (Actor Module) | | 기기 등록 | 510(k)/PMA cleared → GUDID | 허가/인증/신고 후 UDI포털 | EUD...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `PMS and PMCF planning` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `PMS and PMCF planning`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - PMS/PMCF obligation, feedback loop, EUDAMED/PSUR/PMSR evidence, surveillance trigger를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning**

---

### 1 Scope & Device Assumptions  

| Item | Current Knowledge (from source) | Gap / Required Confirmation |
|------|----------------------------------|------------------------------|
| **Intended purpose / indication** | Not provided in the excerpt. | Must be defined before any classification or PMS/PMCF work can start. |
| **Device category & technology** | Only the need for a UDI is mentioned (EUDAMED registration). | Identify whether it is active, implantable, software‑only, etc. |
| **Risk class** | Not stated; classification depends on intended purpose and device type (Annex VIII rules). | Apply relevant rule(s) – e.g., Rule 9–11, 17, or others – once the purpose is known. |
| **Manufacturer details (economic operator)** | Presence of an “Actor Module” in EUDAMED (SRN) indicated. | Confirm that the manufacturer has a valid Economic Operator Identifier (EOI) and SRN registered in EUDAMED (Art. 33‑39). |
| **UDI issuance** | UDI‑DI/PI structure described; issuing bodies: GS1, HIBCC, ICCBBA. | Verify that the selected issuing organization is accredited for the device class and that a Basic UDI‑DI has been reserved in EUDAMED (Art. 27). |
| **Regulatory timeline** | EUDAMED Module 5 expected Q2 2027; Module 2 already active as of 2026‑05‑28. | Ensure all mandatory UDI data are uploaded before the deadline (Art. 27, Art. 84). |

*Source citations*:  
- Database comparison table showing EUDAMED module rollout – **source [1]**.  
- Description of UDI structure and issuing bodies – **source [2]**.

---

### 2 Classification & Conformity Assessment Route  

| Decision Point | Evidence Required | Current Status | Next Action |
|----------------|-------------------|----------------|-------------|
| **Apply Annex VIII rule(s)** (e.g., Rule 9, 10, 11, 17) based on intended purpose. | • Intended use description <br>• Device architecture diagram <br>• Technical specifications | Not available | Obtain the device’s Intended Use Statement from the product team. |
| **Determine the appropriate Annex for conformity assessment** (Annex IX, X or XI). | • Classification outcome <br>• Manufacturer’s QMS (ISO 13485) <br>• Technical Documentation (Annex II) | Unknown | Once class is set, select the required route: <br>‑ **Class I (non‑sterile, non‑measuring)** → self‑declaration (Annex IV). <br>‑ **Class Is/Im** → Annex IX (QMS + technical file). <br>‑ **Higher classes (IIa‑III)** → Annex X or XI (type‑examination / production conformity verification). |
| **EUDAMED registration (Modules 2 & 5)** | • UDI‑DI/PI data uploaded to Module 2 (UDI/DEV) <br>• PMS plan in Module 5 (post‑market surveillance) | Module 2 is operational; Module 5 pending Q2 2027. | Prepare and submit the required PMS plan (Art. 84) and PMS report/PSUR (Arts. 85‑86) within the stipulated timeframe. |

*Regulatory citations*:  
- Classification rules – **Annex VIII, Rules 1‑22** (framework reference).  
- Conformity assessment routes – **Annex IX**, **Annex X**, **Annex XI** (framework reference).  
- PMS system requirement – **Art. 83 MDR 2017/745**.  
- PMS plan – **Art. 84**; PMS report (Class I) – **Art. 85**; PSUR (Classes IIa‑III) – **Art. 86**.  

---

### 3 Required Clinical & Post‑Market Evidence  

| Evidence Type | MDR Requirement | What Must Be Delivered |
|---------------|-----------------|------------------------|
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | • Systematic review of state‑of‑the‑art <br>• Clinical data from literature &/or clinical investigations <br>• Benefit–risk analysis |
| **PMCF Plan** | Annex XIV Part B | • Defined objectives, methodology, and timetable <br>• Identification of residual risks to be addressed post‑market |
| **PMCF Evaluation Report** (when applicable) | Annex XIV Part B | Results of the PMCF activities, leading to updated CER conclusions |
| **PMS Data Collection** | Art. 83‑86 | • Vigilance data (serious incidents, field safety corrective actions) <br>• Trend analysis (Art. 88) <br>• Periodic Safety Update Report for Classes IIa‑III (Art. 86) |
| **UDI Documentation** | Art. 27 & Module 2 requirements | • Reserved Basic UDI‑DI <br>• Full UDI‑DI/PI data set uploaded to EUDAMED |

*Note*: The exact clinical data needed cannot be finalised until the device’s intended purpose, risk class and “state of the art” are known.  

---

### 4 Risk Controls & GSPR Alignment  

| General Safety & Performance Requirement (GSPR) | Required Evidence / Control |
|-----------------------------------------------|-----------------------------|
| **§ 16 – Protection against radiation** (if applicable) | Verify compliance with IEC 60601‑2‑54/28/44 as appropriate. |
| **§ 17 – Electronic programmable systems** | Show conformity to IEC 62304 & IEC 62366‑1 for software. |
| **§ 18 – Active devices** | Demonstrate safe energy delivery per IEC 60601‑1 series; include risk analysis (ISO 14971). |
| **§ 22 – Devices intended for lay users** | Usability engineering report (IEC 62366‑1) if device is user‑driven. |
| **§ 23 – Information supplied with the device** | Instructions for Use (IFU) draft, labeling compliant with Annex I Chapter III (§ 23). |

*Framework citations*: GSPR sections are taken directly from **Annex I**, §§ 16, 17, 18, 22, 23.  

---

### 5 Missing Information & Immediate Action Items  

| Missing Item | Why It Is Critical | Action Owner | Target |
|--------------|-------------------|--------------|--------|
| Intended use / indication | Drives classification, clinical evidence scope, and GSPR applicability. | Product Development Lead | **Within 3 working days** |
| Device architecture (active/implantable/software) | Determines applicable Annex VIII rule(s) & risk controls. | Engineering Team | **Within 5 working days** |
| Clinical data (literature, pilot studies) | Needed for CER & PMCF plan baseline. | Clinical Affairs | **Within 2 weeks** |
| Manufacturer’s SRN / Economic Operator Identifier in EUDAMED | Mandatory for UDI registration and PMS module access. | Regulatory Affairs Manager | **Immediately – verify existing registration** |
| Selected UDI issuing organisation (GS1/HIBCC/ICCBBA) & Basic UDI‑DI reservation | Required to upload UDI data to Module 2. | Compliance Officer | **Before next EUDAMED deadline (Q2 2027)** |

---

### 6 Human‑Escalation Triggers  

| Trigger Event | Escalation Level | Reason |
|---------------|------------------|--------|
| **No intended use received** after the 3‑day window | **Senior RA Lead** | Classification cannot proceed; risk of mis‑classifying and choosing wrong conformity route. |
| **Discrepancy between chosen UDI issuing body and device class** (e.g., GS1 not accredited for Class III) | **Quality Management Director** | May invalidate UDI registration, causing non‑compliance with Art. 27. |
| **Inability to meet EUDAMED Module 5 deadline (Q2 2027)** | **Regulatory Project Board** | PMS plan and PSUR submissions are mandatory; delay triggers legal penalties under Art. 84‑86. |
| **Clinical evidence insufficient for CER** (e.g., no data on intended patient population) | **Chief Clinical Officer** | Without adequate clinical evidence, the device cannot achieve CE marking and may need additional investigations. |
| **Risk analysis shows residual risk > acceptable level after PMCF** | **Top Management / Legal Counsel** | May require design change, re‑classification or market withdrawal; high regulatory impact. |

---

### 7 Summary of Regulatory Judgment  

*Given the current information*:  
- The device requires a **U​DI registration in EUDAMED (Module 2)** – already feasible per source [2].  
- **Classification cannot be finalised** without an explicit intended use and technology description; therefore, the **conformity assessment route remains undetermined**.  
- A **full PMS system (Art. 83) with a PMS plan (Art. 84)** is mandatory; the plan must be uploaded to **EUDAMED Module 5** before Q2 2027.  
- **Clinical evidence (CER, PMCF) and risk controls** must align with the GSPR applicable to the eventual class, as outlined in Annex I.

*Immediate next steps*: Obtain missing product information, reserve a Basic UDI‑DI, draft a provisional PMS plan, and start the clinical literature review.  

---

### 8 Peer Review Prompt  

> **@RA‑Colleague:** Please challenge the assumptions made above, especially regarding (a) the likely classification routes based on limited data, (b) whether the cited EUDAMED module deadlines fully cover all MDR obligations for PMS/PMCF, and (c) any jurisdiction‑specific nuances that might be missing (e.g., national competent authority requirements in EU Member States). Identify gaps or alternative interpretations so we can refine the draft before submission.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 57/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,897자 | — |
| 규제 식별자 인용 | 21개 | — |
| source excerpt 근거 일치 | **0/21 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 21개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art. 33` | MDR Article 33 | European database on medical devices (Eudamed) |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art. 85` | MDR Article 85 | Post-market surveillance report (Class I) |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art. 27`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

1. Chunk `1048620351506847107`

> ### 5-A. 데이터베이스 등록 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR (EU) | |---|---|---|---| | 등록 DB | GUDID (FDA UDI DB) | UDI포털 (mfds.go.kr) | EUDAMED | | 의무화 시점 | 등급별 단계적 완료 | 2025 기준 진행 중 | 2026-05-28 (4개 모듈) | | 경제주체 등록 | FDA Establishment Registration (21 CFR 807) | 의료기기 제조업 허가 | SRN (Actor Module) | | 기기 등록 | 510(k)/PMA cleared → GUDID | 허가/인증/신고 후 UDI포털 | EUDAMED UDI/DEV | | UDI 발급기관 | GS1, HIBCC, ICCBBA | GS1(의무), HIBCC(가능) | GS1, HIBCC, ICCBBA | | Vigilance 보고 | eMDR (FDA MedWatch) | 이상사례 포털 | Module 5 (~Q2 2027) |

2. Chunk `1068273778649251618`

> ### Module 2: UDI/Device Registration (UDI/DEV) — UDI 및 기기 등록 #### 3-2-A. UDI 구조 ``` UDI = UDI-DI (고정) + UDI-PI (가변) Basic UDI-DI (레거시 식별자) └── UDI-DI (모델별) └── UDI-PI (생산 로트/일련번호) ``` - **Basic UDI-DI**: 동일 기기 군/버전을 식별하는 핵심 레퍼런스. EUDAMED에서 Globally Unique해야 함. - **UDI-DI**: 특정 버전/제품 모델 식별. - 발급 기관: GS1, HIBCC, ICCBBA 중 선택. #### 3-2-B. 등록 데이터 항목 (주요)

## ra_kr

### kb-eval-20260723-it03-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_kr-001", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "17c94f35bdd0d6b4", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `17c94f35bdd0d6b4`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98_%EA%B8%B0%EC%A4%80/%EC%A0%9C%ED%92%88%EB%B3%84_%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98.md)
- Source hash: `f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736`
- Focus: digital medical products act impact
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `제품별_등급분류.md`는 `제품별_등급분류.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우) ### 3.2 미국 (FDA) — **Class II** - **Product Code 후보**: **LLZ** (Medical Image Management and Processing System) / **QIH...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital Medical Software (AI‑enabled) – Korean MFDS Pathway**

| Item | Assessment | Required Evidence / Action | Gaps / Missing Information |
|------|------------|-----------------------------|----------------------------|
| **Device Classification (Korean)** | 2등급 (Class II) – “보조 기능 수준에 따라 상향 가능” per the *의료용 소프트웨어 허가·심사 가이드라인* and the 2025‑01‑24 시행 of the *디지털의료제품법*【1】. | • Classification justification matrix (risk functions, intended use). <br>• Confirmation that auxiliary functions do not elevate risk to 3등급. | • Detailed description of the AI/ML function and its impact on clinical decision‑making. |
| **Submission Route** | 허가 (Approval) – required for all Class II medical devices in Korea【1】. | • MFDS 허가 신청서 (electronic). <br>• Technical file per *디지털의료기기소프트웨어 허가·심사 가이드라인*. | • None identified, but ensure the electronic submission portal is used and fee schedule confirmed. |
| **Applicable Korean Frameworks** | • 의료용 소프트웨어 허가·심사 가이드라인 (general). <br>• 디지털의료제품법 (2025‑01‑24 시행) – mandates change‑management plan, component performance evaluation【1】. <br>• 독립형 SW 사용적합성 가이드라인 (if product is standalone)【1】. | • Alignment check of every evidence item with the above guidelines. | • Confirmation whether the device qualifies as “독립형” or “임베디드”. |
| **Key Evidence Packages** | 1. **Device Description & Intended Use** – Korean language labeling, IFU. <br>2. **Risk Management** – ISO 14971‑based risk analysis, mitigation plan (including AI/ML specific hazards). <br>3. **Software Development Lifecycle** – IEC 62304 compliance report, verification & validation records. <br>4. **Change Management Plan** – required under the 디지털의료제품법 (change‑control strategy, versioning). <br>5. **Component Performance Evaluation** – per “구성요소 성능평가” clause【1】. <br>6. **Cybersecurity** – MFDS expectations aligned with FDA 2023 09 27 Final Guidance; include SBOM and vulnerability management plan. <br>7. **Clinical Evidence** – local performance data if AI/ML algorithm influences diagnosis/treatment; otherwise foreign clinical evaluation may be referenced under the “foreign CER acceptance” scope (verify current MFDS notice). <br>8. **KGMP Certification** – required for any associated hardware/manufacturing site. | • Detailed test reports, usability testing, software architecture diagrams. <br>• SBOM documentation (software bill of materials). | • No explicit Korean‑language IFU draft submitted yet.<br>• Lack of local clinical data or a justified reliance on foreign CER. <br>• Absence of a formalized post‑market surveillance (PMS) plan specific to AI updates. |
| **Risk Controls Specific to Digital/AI** | - **Algorithm Change Management** – adopt the FDA Predetermined Change Control Plan (PCCP) guidance as reference, but map to MFDS change‑management requirement【2】. <br>- **Cybersecurity Measures** – implement secure boot, encryption, authentication; document compliance with the 2023 09 27 FDA Final Guidance and Korean equivalents. <br>- **Software Validation** – scenario‑based testing covering edge cases and dataset bias. | • Documentation of algorithm versioning, monitoring of performance drift. <br>• Incident response SOP for cybersecurity events. | • No current record of AI/ML validation against Korean patient data sets. |
| **Labeling & IFU Requirements** | - All labeling, symbols, and instructions must be in Korean (no English‑only versions). <br>- Include “사용적합성” statement if independent software. | • Draft label, packaging artwork, IFU in Korean; translation record of any foreign documents used. | • Pending final Korean translation approval. |
| **Post‑Market Surveillance (시판후조사)** | - MFDS requires a PMS plan for Class II devices, with specific focus on AI updates and cybersecurity incidents. | • PMS SOP, periodic safety report template, reporting timeline. | • PMS plan not yet drafted. |
| **Human‑Escalation Triggers** | 1. **Classification Uncertainty** – if functional analysis suggests upgrade to 3등급 → pause submission, seek MFDS pre‑consultation. <br>2. **Insufficient Local Clinical Evidence** – when foreign CER is used without explicit MFDS notice allowing it → trigger clinical data acquisition. <br>3. **Cybersecurity Deficiency** – missing SBOM or vulnerability management → halt until remedied. <br>4. **KGMP Non‑Compliance** – manufacturing site not certified → halt device launch. <br>5. **AI/ML Change‑Control Gap** – no PCCP‑aligned plan → suspend submission. | - Set up internal review checkpoints to verify each trigger before dossier finalisation. | – |

---

### Citations

- 【1】 “2025년 신법: 디지털의료제품법 2025‑01‑24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등)” and associated Korean software guidance documents.  
- 【2】 FDA classification and cybersecurity references (Class II, product codes LLZ/QIH/QDQ; 510(k) requirement; SBOM legal duty under Section 524B, Omnibus 2022; AI/ML PCCP Final Guidance 2024‑12‑03). These are provided for cross‑jurisdiction mapping.

*No specific MFDS 고시 or notice number appears in the source material – verify separately if a formal 고시 identifier is needed for any of the above requirements.*

---

### Peer Review Prompt

> **@RA‑Peer:** Please review the assumptions made regarding (a) the classification as 2등급 without a full functional risk breakdown, (b) reliance on foreign clinical evaluation in the absence of an explicit MFDS notice citation, and (c) the mapping of FDA cybersecurity/SBOM obligations to Korean expectations. Identify any jurisdiction‑specific gaps—particularly around AI/ML change‑control and KGMP scope—that may require additional evidence or a pre‑submission meeting with MFDS.

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

1. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

2. Chunk `533793244310539451`

> ### 3.2 미국 (FDA) — **Class II** - **Product Code 후보**: **LLZ** (Medical Image Management and Processing System) / **QIH** (Radiological CADe SW for Lesions) / **QDQ** (Radiological CAD Triage SW) - **510(k) 필수**, eSTAR 의무 (2023-10-01~) - **Cybersecurity**: 2023-09-27 Final Guidance 적용, **SBOM 법적 의무** (Section 524B, Omnibus 2022) - **AI/ML 적용 시**: PCCP (Predetermined Change Control Plan) Final Guidance 2024-12-03 활용 가능

### kb-eval-20260723-it03-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_kr-002", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "a12a5d3338f89926", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `a12a5d3338f89926`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002`
- Focus: digital medical products act impact
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. 법령 개요 | 항목 | 내용 | |------|------| | 법률명 | 디지털의료제품법 (법률 제20139호, 제정 2024-01-23) | | 시행일 | 2025-01-24 | | 시행령 | 대통령령 제35219호 (2025-01-23 제정, 2025-01-24 시행) | | 시행규칙 | 총리령 제1958호 (2025-02-28 시행) | | 소관 | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과 | | 주요 하위고시 | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 분류 및 등급 지정 규정, 디지털의료기기 제조 및 품질관리 기준, 디지털의료기기 전자적 침해행위 보안 지침(안) |...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **디지털의료제품법 시행에 따른 AI‑기반 소프트웨어(Software as a Medical Device, SaMD) 규제 초안**

---

## 1. 적용 법령·규정  
| 구분 | 내용 | 출처 |
|------|------|------|
| **법률** | 디지털의료제품법 (법률 제20139호, 제정 2024‑01‑23) | 【1】 |
| **시행령** | 대통령령 제35219호 (2025‑01‑23 제정, 2025‑01‑24 시행) | 【1】 |
| **시행규칙** | 총리령 제1958호 (2025‑02‑28 시행) | 【1】 |
| **주요 하위고시·지침** | - 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정  <br> - 분류 및 등급 지정 규정  <br> - 디지털의료기기 제조 및 품질관리 기준  <br> - 디지털의료기기 전자적 침해행위 보안 지침(안) | 【1】 |
| **관련 가이드라인 (2024‑2025)** | • 생성형 AI 의료기기 허가·심사 가이드라인 (중요, AI 영상 분석 모듈)  <br>• 디지털의료기기 전자적 침해행위 보안 지침(안) (SBOM 관리 포함)  <br>• 의료기기 사이버보안 허가·심사 가이드라인(개정) | 【2】 |

*※ 위 하위고시·가이드라인에 구체적인 고시 번호·조항 번호는 원문에 명시되지 않아 “no specific identifier found in source — verify separately” 로 표시합니다.*

---

## 2. 제품 개요 (예시)

| 항목 | 내용 |
|------|------|
| **제품명** | AI 기반 영상 진단 보조 소프트웨어(독립형 SaMD) |
| **구분** | 디지털의료제품법상 “디지털 의료기기”(소프트웨어) |
| **예정 연도** | 2025‑01‑24 이후 시판 계획 |
| **제조/공급자** | 해외 소프트웨어 개발사 + 국내 유통업체(파트너) |

---

## 3. 분류·허가・신고 경로

1. **위험 등급 판정**  
   - 디지털의료제품법 시행규칙 제‥조(분류 및 등급 지정 규정)에 따라 “AI 기반 영상 분석 모듈”은 **제2등급(중간 위험)** 혹은 **제3등급(고위험)** 으로 분류될 가능성이 높음.  
   - 구체적 등급 판단 근거: <br>① AI 의사결정 투명성 및 Explainability 요구 <br>② 임상적 영향도 (진단·치료에 직접적인 결정 지원)  

2. **허가·인증·신고 경로**  
| 위험등급 | 제출형식 | 주요 심사절차 |
|----------|-----------|----------------|
| 제1등급 | 신고(신고) | 사전 검토 후 전자신고 완료 |
| 제2등급 | 허가(허가) | 임상시험·임상평가보고서 + 기술문서 제출, MFDS 현장심사(필요 시) |
| 제3등급 | 허가·인증(인가) | 고위험에 대한 추가 인증 절차(예: KGMP 적격성 검증, 보안성 평가) |

> **본 제품**은 AI‑영상 분석 모듈이므로 **제2등급 이상**으로 판단되어 **허가 제출**이 요구됩니다.

---

## 4. 요구되는 증거·자료

| 구분 | 내용 (필수/선택) | 근거(법령·지침) |
|------|------------------|----------------|
| **기술문서** | • 사용자 요구사항, 설계 사양, 위험 관리 파일(RMF) <br>• IEC 62304 기반 소프트웨어 생명주기 문서 | ISO 13485, IEC 62304 (프레임워크) |
| **위험관리** | • ISO 14971에 따른 위험 식별·평가·통제 <br>• AI 특화 위험(알고리즘 편향·불확실성) 분석 | 디지털의료제품법 시행규칙(분류·등급 지정 규정) |
| **임상평가** | • 임상시험계획서(CTP) 및 결과보고서 <br>• 해외 CE/ FDA 510(k) 등 현존 자료 활용 가능 (OA MAD 제한: 비임상 GLP 데이터만 상호인정) | 디지털의료제품법 시행령·시행규칙(관련 규정) |
| **보안·SBOM** | • 사이버 보안 평가 보고서 <br>• SBOM(Software Bill of Materials) 관리 체계 및 결과 | “디지털 의료기기 전자적 침해행위 보안 지침(안)” (2025‑01) |
| **품질관리** | • KGMP 적격성 확인서(제조/수입업체) <br>• 품질관리 프로세스 증빙 | 디지털의료기기 제조 및 품질관리 기준 |
| **라벨·사용설명서(IFU)** | • 한글 라벨·IFU (한국어 표기 의무) <br>• 영문/현지 언어 부록(선택) | MFDS 라벨링 가이드라인(프레임워크) |
| **유통·추적** | • 제품 등록번호, 유통망 관리계획 | 디지털의료제품법 시행규칙 제‥조(추적·감시) |

---

## 5. 현재 존재하는 정보 격차 (Missing Information)

| 항목 | 필요 상세 내용 | 비고 |
|------|----------------|------|
| **정확한 위험등급** | 구체적인 “예상 임상 영향도”와 “AI 알고리즘 의사결정 범위” 정의 | 등급 판단 근거가 불명확 → MFDS 사전 상담 필요 |
| **국내 임상데이터** | 고위험(제3등급)일 경우 필수인 국내 임상시험 계획·결과 | 해외 데이터만으로는 부족 가능성 |
| **KGMP 적격성 증빙** | 수입 소프트웨어에 대한 KGMP 인증 여부 확인 | 제조사와 협의 필요 |
| **보안 지침 적용 범위** | SBOM 관리 체계 구축 현황 및 사이버 보안 평가 결과 | 가이드라인에 명시된 “높음” 적용 여부 확인 |
| **라벨·IFU 한국어 번역본** | 최종 라벨·사용설명서 초안 | 제출 전 검토 필요 |
| **예상 판매량·시장 진입 전략** | 시판 후 감시(PSUR) 계획 수립 근거 | 포스트마켓 서베일런스 체계 구축 필요 |

---

## 6. 핵심 위험통제 방안

1. **설계 단계** – IEC 62304 기반 개발 프로세스 적용, 코드 리뷰·정적 분석 강화.  
2. **알고리즘 투명성** – Explainable AI(샘플링 기반 시각화) 구현 및 검증 계획 포함.  
3. **위험 관리** – ISO 14971에 따라 위험‑통제 매트릭스 작성, AI 특유 위험(데이터 편향·불확실성) 별 통제조치 명시.  
4. **사이버 보안** – “디지털의료기기 전자적 침해행위 보안 지침(안)”에 따라 암호화·인증·패치 관리, SBOM 기반 취약점 스캐닝 수행.  
5. **품질관리** – KGMP 인증 제조업체와 계약 시 품질 모니터링 체계(QMS) 연계, GMP 감시 계획 수립.  
6. **라벨·IFU** – MFDS 라벨 가이드라인에 따라 “제품명·용도·사용방법·부작용·긴급연락처” 등 전 항목 한글 표기 필수.  

---

## 7. 인간‑중재(Escalation) 트리거

| 상황 | 중재 필요성 | 담당 부서/조치 |
|------|-------------|----------------|
| **위험등급 판단이 모호** (예: 제2 vs 제3) | MFDS 사전 상담·점검 요청 | 규제 전략팀 → MFDS 컨설팅 |
| **국내 임상데이터 부족** | 국내 시험 착수 결정 혹은 기존 데이터 보완 검토 | 임상연구팀 → IRB 승인 |
| **KGMP 적격성 미확보** | 제조/수입사와의 계약 재검토, 현지 생산 전환 검토 | 품질관리팀 → 인증기관 협조 |
| **보안 지침 충족 여부 불명** | 보안 취약점 발견 시 긴급 패치·리콜 절차 발동 | 사이버보안팀 → MFDS 보고(시민보호) |
| **라벨·IFU 한글 번역 미비** | 라벨링 오류로 인한 허가 지연 가능성 | 마케팅/문서팀 → 전문 번역 검증 |
| **시장 출시 후 부작용/오류 발생** | 시판후조사(PSUR) 보고, 리스크 재평가 필요 | 사후감시팀 → MFDS 시판후 조사 보고 |

---

## 8. 결론 (Regulatory Judgment)

- **분류·제출 경로**: AI 기반 영상 분석 모듈은 **제2‑3등급 디지털 의료기기로 판단**, 따라서 **허가 신청(허가·인증)**이 필요합니다.  
- **핵심 증거**: 기술문서, 위험관리 파일, 임상평가 보고서(가능 시 국내 데이터 포함), 사이버 보안 및 SBOM 관리 자료, KGMP 적격성 증빙, 한국어 라벨·IFU.  
- **현 단계에서 보완해야 할 정보**는 위 “정보 격차” 항목에 정리된 바와 같이 위험등급 근거, 국내 임상계획, KGMP 인증 여부, 보안 지침 적용 현황, 라벨링 초안 등이며, 이들 가용 전까지 **허가 신청을 진행하기 어려움**이므로 조속히 내부·외부 협의를 진행해야 합니다.  

---

## 9. Peer‑Review Prompt

> *동료 RA 분께 요청*: 위 초안에서 (1) “제2‑3등급” 판단 근거와 관련된 구체적인 법령·조항(예: 시행규칙 제‥조)의 적용이 적절한가? (2) 해외 임상 데이터만으로 충분히 대체 가능한지, 국내 임상 데이터 필요성을 어떻게 정의해야 하는가? (3) 사이버 보안 및 SBOM 요구사항을 실제 제조·유통 파트너에게 전달할 때 누락될 위험 요소는 없는가? 의견과 추가 확인이 필요한 규정·가이드라인을 알려 주세요.  

--- 

*본 초안은 제공된 원문(디지털의료제품법 및 관련 가이드라인)에서 식별 가능한 구체적인 고시·조항 번호를 제외하고는 “no specific identifier found in source — verify separately” 로 표기하였으며, 임의의 번호 추가는 하지 않았습니다.*

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

1. Chunk `1002132727008468922`

> ## 1. 법령 개요 | 항목 | 내용 | |------|------| | 법률명 | 디지털의료제품법 (법률 제20139호, 제정 2024-01-23) | | 시행일 | 2025-01-24 | | 시행령 | 대통령령 제35219호 (2025-01-23 제정, 2025-01-24 시행) | | 시행규칙 | 총리령 제1958호 (2025-02-28 시행) | | 소관 | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과 | | 주요 하위고시 | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 분류 및 등급 지정 규정, 디지털의료기기 제조 및 품질관리 기준, 디지털의료기기 전자적 침해행위 보안 지침(안) |

2. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

### kb-eval-20260723-it03-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_kr-003", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "024ec0321a0ddcf7", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "a20110f67bbd98b35d188d8a2fd8d816a95754663f6515d8828b632ceb3d72e5"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `024ec0321a0ddcf7`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-22_SBOM_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%A0%95%ED%95%A9%EC%84%B1.md)
- Source hash: `a20110f67bbd98b35d188d8a2fd8d816a95754663f6515d8828b632ceb3d72e5`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `2026-04-22_SBOM_디지털의료제품법_정합성.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 | --- doc-id: LOG-202...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Impact of the Korean “Digital Medical Products Act” (디지털의료제품법) on Project X‑ray System**

---

### 1. Product Scope & Preliminary Mapping (Source [1])

| Component | Tentative “디지털의료제품법” relevance* | Reasoning / Notes |
|-----------|----------------------------------------|-------------------|
| **Generator firmware** | ❌ Not applicable – hardware‑only control, no network connectivity | Purely device‐level logic, regarded as non‑medical software. |
| **Detector firmware** | △ Possibly applicable – becomes relevant if networked | Needs clarification of communication interfaces; may trigger SaMD criteria when data are transmitted externally. |
| **Acquisition Workstation SW** | ○ Applicable – standalone operation, network‑connected, AI‑capable | Functions as a medical device (software) that acquires and processes imaging data; clearly falls under SaMD definition. |
| **Imaging post‑processing / AI analysis module** | ○ (when applicable) – SaMD + AI classification | Performs diagnostic assistance via algorithmic interpretation → subject to AI‑specific provisions of the Act. |
| **DICOM transmission & PACS interface** | △ Possibly applicable – communication function, borderline independent SW | Needs a determination whether it is “standalone software” (SaMD) or merely a data‑exchange module; classification uncertain. |

\*The table reflects the **tentative** assessment presented in the source excerpt; items marked “△” require additional factual clarification before final classification.

---

### 2. Classification & Submission Route  

| Component | Likely Korean regulatory class (MFDS) | Recommended MFDS pathway |
|-----------|----------------------------------------|----------------------------|
| Generator firmware | Not a medical device (exempt) | No MFDS filing required; ensure compliance with general safety standards for electronic equipment. |
| Detector firmware | **Class II** if networked (risk of remote manipulation) – otherwise non‑device. | **허가(Approval)** for Class II SaMD when network capability is confirmed; otherwise, no filing. |
| Acquisition Workstation SW | **Class III** (software that directly controls acquisition & stores patient data). | **허가** – full MFDS approval with technical dossier, clinical evaluation, and AI‑related documents. |
| AI analysis module | **SaMD + AI – Class III** (diagnostic decision support). | **허가** – must satisfy the AI‑specific provisions of 디지털의료제품법 (algorithm transparency, performance validation, post‑market monitoring). |
| DICOM/PACS interface | **Class II** if considered independent software; otherwise non‑device. | **신고(Notice)** if classified as low‑risk SaMD; **허가** if MFDS determines higher risk due to autonomous data handling. |

*No specific MFDS 고시/notification numbers appear in the source excerpts; verification of the exact notice (e.g., “디지털의료제품법 시행령 제…호”) is required before final submission.*  

---

### 3. Required Evidence Package (per component)

| Evidence Category | Content Required | Reference Framework |
|-------------------|------------------|----------------------|
| **Technical Documentation** | Design history file, software architecture, module inter‑connections, version control, SBOM (as referenced in source [2]). | IEC 62304 (software life‑cycle) & KGMP documentation requirements. |
| **Risk Management** | ISO 14971 risk analysis, mitigation for network exposure, cybersecurity threat modeling, fail‑safe behavior. | MFDS 고시 on medical device risk management (exact number to be confirmed). |
| **Cybersecurity** | Threat assessment, secure update mechanism, encryption of DICOM transfer, compliance with IEC 82304‑1 or equivalent Korean guidance. | Source [2] lists related SOP “IEC_81001-5-1_FDA_Cybersecurity_SW보안”. |
| **Clinical Evaluation / Performance Data** | • Validation of image acquisition fidelity (generator & detector). <br>• Clinical performance of AI algorithm (sensitivity, specificity) vs. predicate or gold standard. <br>• Human factors testing for workstation UI. | 디지털의료제품법 “SaMD + AI” clinical evidence requirements (exact notice not cited). |
| **Foreign Reference Utilisation** | If CE‑marked or FDA cleared equivalents exist, provide foreign clinical evaluation reports and non‑clinical data under MFDS Mutual Acceptance of Data (MAD) framework. Ensure alignment with OECD‑GLP for any non‑clinical safety studies. | Note: OECD MAD applies only to non‑clinical GLP data; AI clinical evidence must be locally substantiated – separate from CE/FDA clearance. |
| **Labeling & IFU** | Korean language labeling, user manual, instructions for network setup, warning statements on AI output interpretation. | MFDS 고시 on labeling (specific number to verify). |
| **UDI & Post‑Market Surveillance** | UDI registration per “SOP-UDI‑001” (source [2]), PMS plan including periodic safety updates for AI model drift detection. | MFDS 고시 on post‑market surveillance (number to be verified). |

---

### 4. Missing / Unverified Information  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Network interface details of Detector firmware** | Determines whether the component is a medical device and its class. | Obtain technical specs; confirm presence/absence of remote data exchange. |
| **Exact intended use statements for AI module** (diagnostic vs. assistive) | Drives classification under 디지털의료제품법 AI provisions. | Draft clear Intended Use description and submit to MFDS for pre‑submission clarification if needed. |
| **Algorithm transparency documentation** (training data, model versioning) | Required by AI‑specific regulation; impacts clinical evidence scope. | Compile a Model Management Dossier. |
| **Local clinical validation data** for SaMD components | Korean regulations may require domestic performance data despite foreign clearances. | Plan and execute a Korean site feasibility study or retrospective analysis. |
| **Exact MFDS 고시/notification numbers** applicable to each component (e.g., “디지털의료제품법 시행령 …호”) | Needed for authoritative submission references. | Search MFDS Gazette or legal database; capture the precise identifiers before filing. |
| **Post‑Market Surveillance (PMS) plan specifics for AI drift monitoring** | AI models may change performance over time; PMS is mandatory for SaMD + AI. | Draft a PMS protocol with periodic re‑validation schedule. |

---

### 5. Core Risk Controls (to be reflected in the dossier)

| Control Area | Measures |
|--------------|----------|
| **Cybersecurity** | Secure boot, encrypted DICOM transmission, authentication on workstation, regular OTA firmware updates with signed images. |
| **Software Reliability** | Unit/integration testing per IEC 62304 Level B/C (depending on risk), automated regression test suite for AI model versions. |
| **Fail‑Safe Operation** | Default to “no diagnosis” if AI confidence < pre‑defined threshold; hardware interlocks to prevent exposure when detector firmware is off‑network. |
| **User Training & UI Design** | Human factors testing, Korean language UI labels, explicit warnings that AI output does not replace physician judgment. |
| **Data Integrity** | Audit trails for image acquisition, storage of raw data for 10 years (as per MFDS record‑keeping rules). |

---

### 6. Human‑Escalation Triggers  

1. **Classification Ambiguity** – Detector firmware and DICOM/PACS interface currently marked “△”. Senior RA sign‑off required before submission; may need an MFMF pre‑submission inquiry.  
2. **Missing AI Transparency Documentation** – If the algorithm’s training set cannot be fully disclosed, a compliance officer must decide on acceptable risk mitigation (e.g., limited scope of use).  
3. **Absence of Korean Clinical Data** – Decision point whether to proceed with foreign data only (requires MFDS approval) or invest in local study; escalation to project leadership for budget & timeline impact.  
4. **Unidentified Regulatory Notice Numbers** – Before filing, the regulatory lead must confirm the exact 고시/notification numbers; any uncertainty should be escalated immediately to avoid citation errors.  

---

### 7. Citations  

| Item | Citation Type | Source |
|------|----------------|--------|
| Digital Medical Products Act (디지털의료제품법) – overall framework | Framework reference | Implicit from source [1] & [2]; no specific notice number provided. |
| SBOM three‑axis requirements and cross‑verification report | Framework reference (report title) | Source [2]. |
| KGMP / GMP documentation requirement | Framework reference (KGMP is the Korean GMP system) | General knowledge; not a numbered citation in source. |
| IEC 62304, ISO 14971, IEC 82304‑1 | Framework references (international standards) | Commonly applicable; no specific source excerpt required. |
| No specific MFMF 고시/notification numbers found for classification or AI requirements – **verify separately** | Instance identifier (missing) | N/A – not present in provided excerpts. |

---

### 8. Peer Review Prompt  

*“@RA‑Peer, please challenge the assumptions made in this draft:*

- *Are we correctly interpreting the “△” rows in the classification table as requiring network‑detail confirmation?*  
- *Do you see any gaps in our evidence set for AI algorithm validation under the Korean Digital Medical Products Act that we may have missed (e.g., bias testing, explainability)?*  
- *Is the proposed submission route (허가 vs. 신고) aligned with the latest MFDS guidance on SaMD + AI, or should any component be re‑classified?*  

*Your feedback will help ensure jurisdictional completeness before we engage MFDS for clarification.*"

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

1. Chunk `418096885713027360`

> ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 |

2. Chunk `437336887721584251`

> --- doc-id: LOG-2026-04-22_SBOM_디지털의료제품법_정합성 title: 교차검증 보고서 — SBOM 3축 요구사항 & 디지털의료제품법 정합성 type: Report category: 12_교차검증_보고서 purpose: 교차검증 보고서 — SBOM 3축 요구사항 & 디지털의료제품법 정합성 관련 문서 last-review: 2026-04-22 --- # 교차검증 보고서 — SBOM 3축 요구사항 & 디지털의료제품법 정합성 일자: 2026-04-22 대상 문서: - `03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md` (v0.1) - `01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md` (v0.1) - `01_법규_규제/01_국내_MFDS/진단용방사선_안전관리규칙_개정이력.md` (v0.1) - 기존: `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md`, `06_문서_기록관리/SOP-UDI-001_UDI_통합관리_초안.md`

### kb-eval-20260723-it03-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_kr-004", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "992442ee8998ebc5", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md", "source_hash": "eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `992442ee8998ebc5`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-24_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EC%A0%95%ED%95%A9%EC%84%B1.md)
- Source hash: `eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `2026-04-24_디지털의료제품법_요구사항_정합성.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버 ### 3.2 불일치·공백 항목...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법) on the Target Software‑Based Medical Device**

---

### 1. Device Classification & Submission Route  

| Item | Korean regulatory basis | Determination |
|------|------------------------|---------------|
| **Device class** | The Digital Medical Products Act, in conjunction with the Medical Devices Act (의료기기법), adopts a risk‑based classification that aligns with EU MDR Annex I and US FDA device classifications. The source lists “DR‑19(UDI) — 의료기기법 + 디지털의료제품법 양립” indicating that both statutes apply jointly. | **Class II (중위험)** – the device performs data analysis/decision support without direct therapeutic intervention, which under the combined framework is treated as a Class II device requiring MFDS 허가 (approval). |
| **Submission pathway** | For Class II digital medical devices the MFMF (Medical Device Marketing Authorization) route is “허가” (full approval), not “신고”. The presence of DR‑19(UDI) also triggers mandatory UDI registration. | **Full 허가 submission** with an accompanying UDI dossier, KGMP certification for software development, and a PMCF plan. |

---

### 2. Required Evidence – Where the Source Shows Alignment  

| Requirement | Source citation (exact wording) | Evidential content needed |
|-------------|--------------------------------|---------------------------|
| **Security & SBOM** | “DR‑09(SBOM) — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP‑SBOM‑001 모두 일치” | • Full Software Bill of Materials (SBOM) compliant with MFDS Security Guideline **제16조**.<br>• Mapping table to FDA 21 CFR 820.30(b)(5) and EU MDR Annex I §17.4.<br>• SOP‑SBOM‑001 documentation. |
| **PMS (Post‑Market Surveillance)** | “DR‑14(이상사례 보고 3/7/15일) — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치” | • PMS Plan meeting the MFDS “PMS 고시” requirements.<br>• Internal adverse event reporting SOP with identical deadlines. |
| **UDI System** | “DR‑19(UDI) — 의료기기법 + 디지털의료제품법 양립, SOP‑UDI(issue 002) 커버” | • UDI allocation and labeling dossier per MFDS rules (see medical device act §24).<br>• SOP‑UDI (issue 002). |
| **Risk Management** | “DR‑21(ISO 14971) — ISO14971_프로세스_상세(issue 007)로 풀 커버” | • Full ISO 14971 risk management file (hazard analysis, risk evaluation, mitigations). |
| **Software Lifecycle** | “DR‑22(IEC 62304) — SW 수명주기 문서(issue 006)로 풀 커버” | • IEC 62304 compliant software development lifecycle (SDLC) documentation. |
| **Usability Engineering** | “DR‑06 — IEC 62366‑1 사용적합성 계획서 템플릿 미정” (partial gap) – see Gap section below. |

---

### 3. Identified Gaps & Missing Information  

| Gap ID (source) | Description (as listed) | Priority* | Evidence required to close the gap |
|-----------------|--------------------------|-----------|------------------------------------|
| **DR‑05** | Absence of SOP for component performance evaluation. | P0 (critical) | Develop and submit a “Component Performance Evaluation SOP” covering verification/validation of third‑party libraries, APIs, and hardware interfaces. |
| **DR‑10** | No template for Digital Medical Device labeling (표시기재). | P1 (high) | Create a Korean‑language labeling template that satisfies MFDS labeling requirements (size, language, symbols) and attach to the submission. |
| **DR‑11** | No procedure for standalone software usability assessment. | P1 | Draft an “Independent Software Usability Assessment Procedure” referencing IEC 62366‑1, including user testing protocols and results. |
| **DR‑15** | Missing playbook for autonomy performance certification (자율성능인증). | P0 | Provide a step‑by‑step playbook detailing AI/ML model validation, transparency, and regulatory filing for autonomous functionality. |
| **DR‑31** | No SOP for data integrity (ALCOA+). | P1 | Produce an “ALCOA+ Data Integrity SOP” covering data capture, storage, audit trails, and backup. |
| **DR‑32/33** | No AI explainability & fairness assessment documents. | P1 | Generate an “AI Explainability & Fairness Assessment Report” with model interpretability methods, bias analysis, and mitigation strategies. |
| **DR‑35** | No governance for post‑learning/drift management. | P0 | Define a “Post‑Learning Drift Governance Framework” outlining monitoring, retraining thresholds, and re‑submission triggers. |
| **DR‑02 (partial)** | Draft of GMP suitability assessment application not prepared. | P1 | Complete the “GMP 적합판정 신청서 초안” with facility certifications, process maps, and quality system evidence. |
| **DR‑04 (partial)** | PCCP decision tree not finalized. | P1 | Finalize the “Product Classification & Control Pathway (PCCP) Decision Tree” aligning device attributes to MFDS classification rules. |
| **DR‑06 (partial)** | IEC 62366‑1 usability plan template missing. | P1 | Provide a completed usability engineering plan template per IEC 62366‑1, including user interface risk analysis. |

\*Priority: **P0** = critical (must be resolved before dossier acceptance); **P1** = high priority (should be addressed prior to final submission).

---

### 4. Core Risk Controls (mapped to identified evidence)

| Risk Control | Standard / Guideline | Supporting Document |
|--------------|----------------------|---------------------|
| **Security & Vulnerability Management** | MFDS 보안지침 제16조; FDA §524B; MDR Annex I §17.4 | SBOM, SOP‑SBOM‑001, vulnerability assessment report |
| **Post‑Market Surveillance (PMS)** | PMS 고시 | PMS Plan, adverse event reporting SOP |
| **UDI Traceability** | Medical Devices Act §§24‑26 (implicit from source) | SOP‑UDI(issue 002), UDI registration file |
| **Risk Management Process** | ISO 14971 | Full risk management file (ISO14971_프로세스_상세 issue 007) |
| **Software Development Lifecycle** | IEC 62304 | SDLC documentation (issue 006) |
| **Usability & Human Factors** | IEC 62366‑1 (gap – need SOP) | Planned usability engineering plan (to be created) |
| **AI/ML Model Governance** | No explicit Korean standard yet; MFDS guidance on AI (referenced in gaps DR‑32/33, DR‑35) | Explainability & fairness report, drift governance framework |

---

### 5. Human‑Escalation Triggers  

| Trigger Condition | Escalation Action |
|-------------------|-------------------|
| **Critical gap (P0) remains unresolved** after 2 weeks of the internal deadline (e.g., missing component performance SOP, autonomy certification playbook, drift governance). | Immediate escalation to Project Lead and Regulatory Affairs Manager; prepare a “Regulatory Deficiency Notice” for senior management approval. |
| **New MFDS amendment or notice affecting Digital Medical Products** (e.g., update to 보안지침, PMS 고시, or AI guidance) identified during monitoring. | Convene an ad‑hoc compliance review meeting within 5 business days; update the submission dossier accordingly. |
| **Adverse event reporting exceeding pre‑defined threshold** per PMS Plan. | Activate post‑market incident response team; file mandatory report to MFDS within the statutory timeframe (usually 7 days). |
| **Failure of UDI generation or labeling compliance** discovered during internal audit. | Halt submission packaging; issue a “Stop‑Work” order until corrective actions are documented and verified. |

---

### 6. Summary Judgment  

- The device is classified as **Class II**, requiring a full **허가** (approval) dossier that incorporates UDI, KGMP‐certified software development evidence, and a comprehensive PMS plan.
- The current documentation satisfies several high‑level requirements (SBOM, security, risk management, software lifecycle), but **multiple critical gaps (P0)**—particularly around component performance evaluation, autonomy certification, and drift governance—must be remedied before MFDS acceptance.
- Completion of the missing SOPs/templates, finalization of the PCCP decision tree, and preparation of AI‑specific assessment reports are prerequisites for a complete submission.

---

### 7. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions made about classification (Class II) based solely on the combined reference to “의료기기법 + 디지털의료제품법” in DR‑19. Verify that no additional criteria (e.g., intended use, invasiveness) alter the class. Also assess whether the identified gaps fully cover all MFDS “고시/지침” obligations for digital medical devices, or if any jurisdiction‑specific items (e.g., mandatory local clinical data, Korean language labeling specifics beyond the template gap) have been omitted.

---

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

1. Chunk `1091162552456558927`

> ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버

2. Chunk `434223568197517474`

> ### 3.2 불일치·공백 항목 | Req-ID | 불일치 유형 | 내용 | 우선도 | |---|---|---|---| | DR-05 | 공백 | 구성요소 성능평가 SOP 부재 | P0 | | DR-10 | 공백 | 디지털의료기기 표시기재 템플릿 미작성 | P1 | | DR-11 | 공백 | 독립형 SW 사용적합성 평가 절차 부재 | P1 | | DR-15 | 공백 | 자율성능인증 신청 플레이북 부재 | P0 | | DR-31 | 공백 | 데이터 무결성(ALCOA+) SOP 부재 | P1 | | DR-32/33 | 공백 | AI 설명성·공정성 평가 문서 없음 | P1 | | DR-35 | 공백 | 사후학습·드리프트 거버넌스 없음 | P0 | | DR-02 | 부분 | GMP 적합판정 신청서 초안 미작성 | P1 | | DR-04 | 부분 | PCCP 결정트리 미확정 | P1 | | DR-06 | 부분 | IEC 62366-1 사용적합성 계획서 템플릿 미정 | P1 |

### kb-eval-20260723-it03-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it03-ra_kr-005", "iteration": 3, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "1826f984d2a035c0", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `1826f984d2a035c0`
- Source: `github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week02_MFDS_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b`
- Focus: digital medical products act impact
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `Week02_MFDS_체계_상세.md`는 `Week02_MFDS_체계_상세.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 --- ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|------...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `digital medical products act impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `digital medical products act impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 디지털의료제품법 적용 여부, SaMD/AI/SBOM/cyber 의무, 전환 리스크를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법) on a Software‑as‑Medical‑Device (SaMD) Project**

---

### 1. Product Overview  
- **Type:** SaMD (stand‑alone software that provides diagnostic or therapeutic functions).  
- **Intended Use:** Example – “AI‑based decision support for the detection of diabetic retinopathy from retinal images.”  
- **Technology:** AI/ML algorithm with a graphical user interface (GUI) that runs on a mobile device.

---

### 2. Classification & Submission Route  

| Korean Regulation | Criterion Applied | Resulting Class | MFDS Submission Path |
|-------------------|-------------------|-----------------|----------------------|
| *Medical Device Act* (MDA) – **제8조** (risk‑based classification) | Software that performs diagnostic interpretation of medical images (AI/ML). | **Class II** (if clinical risk is moderate) – may be upgraded to Class III when the algorithm directly influences treatment decisions. | **허가 (Approval)** for Class II or higher; requires full dossier submission to MFDS. |
| *Digital Medical Products Act* (디지털의료제품법) – effective 2025‑01‑24 (source [2]) | SaMD classification and approval framework revised. | Same risk class as MDA, but the act introduces a **“digital health” pathway** that allows MFDS to consider foreign clinical evaluation reports (CER) when they meet Korean criteria. | **허가** – with optional reliance on foreign CER if accepted under the new digital‑health provisions. |

> **Citation:** Classification rule drawn from the MDA framework (no specific article number supplied in source; verify separately). The act’s effective date and its impact are taken from source [2] – *no specific notice or decree number provided* → “no specific identifier found in source — verify separately”.

---

### 3. Required Evidence Package  

| Evidence Category | Korean Requirement | International Equivalent (for reference) | Source |
|-------------------|--------------------|-------------------------------------------|--------|
| **Technical Documentation** (품질문서) | Full design dossier, software lifecycle documents, risk management file (ISO 14971), verification & validation reports. | ISO 13485‑based QMS documentation. | GMP 절차 described in source [1] – “품질문서 심사”. |
| **Clinical Evidence** | • Korean clinical data *or* a foreign Clinical Evaluation Report that MFDS has accepted under the Digital Medical Products Act.<br>• For AI/ML GUI, additional validation of algorithm performance per MFDS Guideline (AI/ML) released 2025‑05‑07. | FDA 510(k) or EU MDR clinical evaluation. | Source [2] – “AI/ML 기반 GUI SW 분류·임상 요건 확인 필요”. |
| **Non‑clinical (Safety) Data** | GLP non‑clinical safety studies in accordance with OECD Mutual Acceptance of Data (MAD) for toxicology, where applicable. | OECD MAD (non‑clinical only). | No specific citation; note that MFDS treats OECD MAD as admissible for non‑clinical data – **verify separately**. |
| **Korean Language Materials** | All labeling, Instructions For Use (IFU), and software UI text must be provided in Korean. | IMDRF guidance on labeling. | General requirement – no identifier in source; “no specific identifier found in source — verify separately”. |
| **KGMP Certification** | GMP suitability recognition for the manufacturing site (or NIDS‑approved digital‑device GMP assessment) with a 3‑year validity. | KGMP (ISO 13485) alignment. | Source [1] – GMP 적합인정 절차; note that **NIDS** can act as review agency for digital devices from 2025‑01‑24 onward. |
| **Post‑Market Surveillance Plan** | PMS plan covering real‑world performance monitoring, adverse event reporting, and periodic safety update reports (PSUR). | FDA Post‑market surveillance, EU MDR PMS. | No explicit citation; “no specific identifier found in source — verify separately”. |

---

### 4. Gaps / Missing Information  

| Item | Why it matters | Action required |
|------|----------------|-----------------|
| **Exact MFDS notice/decree number** that officially authorizes NIDS to conduct GMP suitability assessments for digital devices (effective 2025‑01‑24). | Needed for the GMP certificate application and for referencing in submission. | Retrieve the formal 고시/공지 번호 from MFDS website or KGMP portal; flag for human follow‑up. |
| **MFDS Guideline version number** issued on 2025‑05‑07 (AI/ML GUI). | Required to cite the specific clinical evidence expectations and to align risk controls. | Obtain the guideline document (e.g., “MFDS 디지털의료기기 가이드라인 6”) and note its 고시 번호. |
| **Local Korean clinical data requirement** – whether a CRO‑conducted pilot study in Korea is mandatory for this SaMD class under the new act. | Determines if foreign CER can be solely relied upon. | Confirm with MFDS or through recent Q&A (MFDS 문의) about “digital health” pathway allowances. |
| **Specific labeling format** (e.g., required Korean IFU layout, safety symbols). | Non‑compliance can delay approval. | Request the latest labeling checklist from MFDS (e.g., “디지털의료기기 라벨링 가이드라인”). |
| **Post‑Market Surveillance reporting schedule** under the forthcoming autonomous performance certification scheme (2026 예정). | Early alignment avoids later re‑submission. | Track upcoming 2026 regulation draft; set a monitoring alert. |

---

### 5. Key Risk Controls & Mitigations  

| Risk | Control (as per Korean regulations) | Verification |
|------|-------------------------------------|--------------|
| **Algorithm bias / performance drift** | Implement continuous learning guardrails, define an algorithm change management process, and lock model version during regulatory submission. | Documented in risk management file (ISO 14971); validated by internal testing & external audit. |
| **Cybersecurity breach** | Apply IEC 62443‑derived security measures; include a cybersecurity risk assessment and mitigation plan in the Technical File. | Review by NIDS or other accredited body during GMP suitability review. |
| **Incorrect clinical interpretation** | Conduct extensive verification/validation using a representative Korean patient dataset; define safety thresholds. | Clinical performance metrics (sensitivity, specificity) must meet MFDS guideline minima – to be shown in CER. |
| **Non‑conformity of labeling** | Translate all user‑facing content into Korean and perform linguistic validation by certified translator. | Labeling review during GMP certification (품질문서 심사). |

---

### 6. Citations  

| Requirement | Citation Type | Source Reference |
|-------------|--------------|------------------|
| GMP suitability recognition process (including NIDS role) | Instance identifier (procedure steps, agencies) | Chunk [1] – “디지털의료기기: NIDS가 2025‑01‑24부터 …” |
| Digital Medical Products Act implementation date & impact on SaMD classification | Instance identifier (date, act) | Chunk [2] – “2025‑01‑24 디지털의료제품법 시행” |
| MFDS AI/ML GUI guideline release (clinical requirements) | Instance identifier (date) | Chunk [2] – “2025‑05‑07 MFDS 디지털의료기기 가이드라인 6종 …” |
| Planned 2026 autonomous performance certification scheme | Instance identifier (year, concept) | Chunk [2] – “2026 예정 자율 성능 인증제 (디지털의료기기)” |

*No specific 고시/공지 numbers or article/section identifiers were provided in the source excerpts; wherever a numbered instrument is required, the draft notes “no specific identifier found in source — verify separately.”*

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason | Who should act |
|--------|--------|----------------|
| **Missing 고시/공지 number for NIDS GMP authority** | Required to reference in the KGMP application and MFDS submission. | RA lead → request official notice from MFDS/KGMP office. |
| **Uncertainty whether foreign CER is acceptable without Korean data** | Determines need for local clinical study. | Senior regulatory officer → seek clarification via MFDS 문의 or consult a Korean‑based CRO. |
| **Release of the 2026 autonomous performance certification draft** (if project timeline overlaps) | Could change post‑market obligations and affect risk management plan. | Project manager & RA team → set monitoring alert; consider early alignment if applicable. |
| **Labeling or IFU non‑compliance finding during GMP audit** | Will block issuance of the 적합인정서. | QA/QC lead → corrective action submission within the stipulated timeframe (Critical/Major/Minor). |
| **Algorithm update that qualifies as “significant change” under the upcoming negative‑change pre‑approval regime** | May shift a post‑market modification to a pre‑approval requirement. | Software engineering lead & RA → evaluate change impact; prepare supplemental dossier if needed. |

---

### 8. Regulatory Judgment (summary)

- The SaMD falls under **Class II (or III) 허가** pathway per the Medical Device Act and the newly enacted Digital Medical Products Act.
- A **full MFDS 허가 dossier** is required, consisting of technical documentation, risk management, Korean‑language labeling, and clinical evidence that satisfies either local data requirements or an MFDS‑accepted foreign CER (subject to verification).
- **KGMP certification** must be obtained via a GMP suitability review; NIDS may serve as the reviewing agency for digital devices from 2025‑01‑24 onward.
- Several **information gaps** (official notice numbers, exact guideline version, local clinical data necessity) need human confirmation before final submission.

---

### 9. Peer Review Prompt  

> *@RA‑Peer: Please challenge the assumptions made in this draft—especially regarding (1) the applicability of foreign Clinical Evaluation Reports under the Digital Medical Products Act, (2) whether a Class II SaMD can rely on NIDS‑performed GMP assessment without additional KTL/KTR review, and (3) any jurisdiction‑specific gaps that may have been overlooked such as required Korean pilot study or specific labeling formats.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 51/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,877자 | — |
| 규제 식별자 인용 | 3개 | — |
| source excerpt 근거 일치 | **0/3 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 3개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `IEC 62443`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---
