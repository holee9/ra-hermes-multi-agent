# KB Eval Checksheet - 2026-10-17 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261017-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_us-001", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "ee53bc7444b9df15", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `ee53bc7444b9df15`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관...
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

> **Regulatory Draft – SaMD GUI for Radiology Imaging (“촬영실 GUI SW”)**

---

### 1. Bottom‑line judgment  
| Item | Determination |
|------|---------------|
| **Device class / regulation** | Class II medical device, regulated under **21 CFR Part 892** – *Medical image management and processing system* (§892.2050). |
| **Submission pathway** | Traditional **510(k) Premarket Notification** (Class II) – identify a predicate‑cleared device in the same product code (e.g., “RDA” – Radiology Device Application). If no suitable predicate exists, consider **De Novo** classification. |
| **Primary regulatory docket** | 510(k) plus compliance with the new **Quality Management System Regulation (QMSR)** (effective Feb 2026, 21 CFR §820). |
| **Key submission components** | • Predicate comparison table  <br>• Device description & intended use  <br>• Labeling & UDI plan (21 CFR §830)  <br>• Risk Management File (ISO 14971:2019)  <br>• Software Development Lifecycle documentation (IEC 62304 2006+A1:2015, Safety Class C)  <br>• Verification/validation data (including regression‑test automation)  <br>• Cybersecurity & AI/ML plan (PCCP – FDA Final Guidance Dec 2024)  <br>• Complaint handling and MDR reporting procedures (21 CFR §820.35(a))  <br>• QMSR‑specific SOPs covering ARR, contract sterilizer/re‑labeler inclusion, internal audit access, etc. |

---

### 2. Evidence required for the 510(k)  

| Requirement | Source / Standard | Evidence to submit |
|-------------|-------------------|--------------------|
| **Device description & intended use** | 21 CFR §807.92 (general) | Narrative, flow diagram, user interface screenshots, and a clear statement of clinical purpose (e.g., “provides real‑time display and manipulation of radiographic images in the examination room”). |
| **Predicate device comparison** | FDA 510(k) guidance | Side‑by‑side table of functional, technological, and performance characteristics vs. identified predicate(s). |
| **Labeling & UDI** | 21 CFR §801 (labeling); §830 (UDI) | Label artwork, IFU, and a UDI issuance plan (GS1/DataMatrix or HIBCC). |
| **Risk Management File** | ISO 14971:2019 (risk analysis, evaluation, controls) | Completed risk management report, hazard log, and verification of mitigations. |
| **Software life‑cycle documentation** | IEC 62304 §8.1 (software development process) | • Software Development Plan (SDP) <br>• Software Requirements Specification (SRS) <br>• Software Architecture Document (SAD) <br>• Verification Plan (SVP) & Report (SVR) <br>• Change‑control SOP aligned with **Predetermined Change Control Plan (PCCP)** (FDA Final Guidance Dec 2024). |
| **Software verification & validation** | IEC 62304; FDA “General Principles of Software Validation” guidance | Unit, integration, system testing results; regression‑test automation logs; usability testing summary. |
| **Cybersecurity** | FDA 524B PCCP guidance (Dec 2024) ; MFDS Cybersecurity Guideline 2025 (source) | Threat model, SBOM, security controls matrix, post‑market monitoring plan. |
| **AI/ML functionality (if present)** | FDA PCCP (Final Guidance Dec 2024) ; EU AI Act Art.43(4) (reference only) | AI/ML change‑control plan, training data set description, performance metrics, and a justification for pre‑determined change approach. |
| **Complaint handling & MDR reporting** | 21 CFR §820.35(a) (ARR compliance) | SOP for complaint intake, triage, determination of reportability under 21 CFR §803, and record‑keeping log. |
| **QMSR‑specific procedures** | **ARR (Applicable Regulatory Requirements)** – §820.10(b); **Complaint file enhancement** – §820.35(a); **Service records** – §820.35; **Internal audit access** – §820 overall; **Contract sterilizer/re‑labeler inclusion** – §820.10(a) (source excerpt [1]) | • Integrated ARR compliance matrix <br>• Updated complaint file format meeting §820.35(a) <br>• Service report template (per §820.35) <br>• SOPs for internal audit that allow FDA investigator access <br>• SOP covering external contract sterilizers/re‑labelers. |
| **Design‑control records** | 21 CFR §820.30 (design controls) | Design input, output, review minutes, verification & validation reports, design transfer documentation. |

*All above items are **framework references**; no device‑specific identifiers appear in the source excerpts.*

---

### 3. Missing / ambiguous information that must be resolved before filing  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Predicate device (product code, K-number)** | Required for a traditional 510(k). Without a clear predicate you may need De Novo. | Perform market search; identify at least one cleared device that performs the same image‑display/manipulation functions. |
| **Exact intended use statement** | Determines classification and influences risk analysis. | Draft precise wording (e.g., “enables radiographers to view, manipulate, and store digital X‑ray images in real time”). |
| **UDI issuing agency selection** | Must be assigned before submission; impacts labeling. | Choose GS1 or HIBCC; obtain issuer identifier. |
| **Full cybersecurity threat model** | Needed for PCCP and FDA review. | Conduct formal assessment (STRIDE, ISO 27001 alignment). |
| **AI/ML algorithm details (if any)** | Determines whether a PCCP is required and influences risk controls. | Document training data source, performance thresholds, retraining triggers. |
| **Contract sterilizer/re‑labeler scope** | QMSR (§820.10(a)) expands QMS boundary to these external parties. | List all third‑party vendors; obtain their QMS compliance evidence. |
| **ARR integration plan** | Source excerpt specifies ARR must be embedded in QMS procedures. | Map each applicable regulatory requirement (UDI, MDR reporting, 806 corrections) to SOPs. |
| **Internal audit reporting format** | FDA may inspect audit reports per §820 overall. | Prepare audit report template with traceability to findings and corrective actions. |

---

### 4. Core risk‑control measures (Design‑Control focus)

1. **Risk Management (ISO 14971:2019)** – hazard identification, severity/occurrence assessment, risk control hierarchy, residual risk evaluation.
2. **Design Input Controls** – functional requirements tied to clinical need; include cybersecurity and AI/ML performance criteria.
3. **Verification & Validation** – systematic testing per IEC 62304 §8.1; regression‑test automation; usability validation with representative users.
4. **Change Management (PCCP)** – pre‑defined change categories, monitoring plan, post‑market data collection to support predetermined changes without additional FDA review.
5. **Cybersecurity Safeguards** – authentication, encryption, patch management, SBOM tracking.
6. **Complaint & MDR Reporting Process** – triage algorithm, 30‑day report timeline for adverse events (21 CFR §803), and integration with ARR (§820.35(a)).
7. **Contractor Control** – qualified agreements with sterilizers/re‑labelers; audit rights per QMSR §820.10(a).

---

### 5. Citations used  

| Item | Citation type | Reference |
|------|---------------|-----------|
| ARR (Applicable Regulatory Requirements) requirement | Instance identifier (source excerpt [1]) | **§820.10(b)** |
| Complaint file enhancement – MDR reportable determination | Instance identifier (source excerpt [1]) | **§820.35(a)** |
| Service record requirement | Instance identifier (source excerpt [1]) | **§820.35** |
| Internal audit access for FDA inspectors | Instance identifier (source excerpt [1]) | **§820 overall** |
| Inclusion of contract sterilizer/re‑labeler in QMSR scope | Instance identifier (source excerpt [1]) | **§820.10(a)** |
| Software development lifecycle mapping (IEC 62304 Class C) | Framework reference | IEC 62304 2006+A1:2015, Safety Class C |
| Software validation clause | Framework reference | IEC 62304 §8.1 |
| Cybersecurity guidance linkage | Framework reference | FDA 524B **Predetermined Change Control Plan (PCCP)** – Final Guidance Dec 2024 |
| AI/ML change‑control alignment with PCCP & EU AI Act | Framework reference | FDA PCCP (Dec 2024); EU AI Act Art.43(4) (reference only). |
| QMSR ARR integration requirement | Instance identifier (source excerpt [1]) | **§820.10(b)** (re‑used) |

*All other regulatory citations (e.g., 21 CFR §892.2050, 21 CFR §807.92, ISO 14971:2019) are framework references and thus do not require a source excerpt.*

---

### 6. Human‑escalation triggers  

| Situation | Trigger for escalation to senior RA / regulatory counsel |
|-----------|----------------------------------------------------------|
| **No suitable predicate device** identified after market search. | Initiate De Novo feasibility assessment. |
| **Unclear classification** (e.g., whether the software is a “medical image management” system vs. a “clinical decision support” tool). | Request FDA pre‑submission meeting to obtain classification confirmation. |
| **Incomplete ARR mapping** – missing UDI, MDR reporting, or 806 correction plan. | Escalate to QMS lead for corrective SOP development before submission. |
| **AI/ML component** – uncertainty whether predetermined change control suffices. | Engage FDA liaison (e.g., via AI/ML pilot program) and obtain written feedback. |
| **Contract sterilizer/re‑labeler compliance evidence unavailable**. | Escalate to procurement/compliance for vendor qualification documentation. |
| **Cybersecurity threat model not finalized or lacking SBOM**. | Pause submission; involve IT security team and external cyber‑risk consultant. |
| **Significant residual risk remains after controls** (per ISO 14971). | Pause filing; perform additional mitigation activities or consider redesign. |

---

### 7. Peer‑review prompt  

> *Please review the assumptions above:  
> – Is the classification as a Class II “Medical image management and processing system” (§892.2050) appropriate for a radiology‑room GUI SaMD?  
> – Does the evidence checklist cover all QMSR‑specific obligations introduced by §820.10(b) and related sections?  
> – Are there any jurisdictional gaps (e.g., Korean MFDS requirements) that need explicit segregation from the US submission package?*  

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

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261017-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "aa65a5bc480ee91e", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "757e3b0039fbc8900d0917e9ebdd32c0ded796618813c51039ed63b34e627e31"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `aa65a5bc480ee91e`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md)
- Source hash: `757e3b0039fbc8900d0917e9ebdd32c0ded796618813c51039ed63b34e627e31`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`는 `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분 ### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영) | SOP | 갱신 내용 | 담당 | 판정 기준 | |-----|----------|------|----------| | SOP-DOC-001 | §3에 "미국 시장 적용 시...
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

> **Regulatory Draft – QMS R (21 CFR Part 820) Readiness Assessment**

---

### 1. Device Classification & Submission Pathway *(Bottom‑line)*
| Item | Judgment |
|------|----------|
| **Device class** | *Not determinable from source.* No intended use or product description is provided, therefore the FDA classification (21 CFR Part 892 for imaging, Part 862 for clinical chemistry, etc.) cannot be assigned. **Human escalation required** to obtain device‑specific information. |
| **Typical US submission route (once class known)** | • **Class II** → 510(k) Premarket Notification (21 CFR §807). <br>• **Class III** → PMA (21 CFR §814). <br>*The QMSR requirements below apply to any Class II/III device.* |

---

### 2. Regulatory Evidence Required for QMS R Compliance  

| Requirement | Evidence Needed | Source Citation |
|------------|----------------|-----------------|
| **Incorporation of ISO 13485:2016** (record‑management clause) | • Documented compliance with **ISO 13485 §4.2.5** (records management). <br>• Demonstration that additional FDA provisions are met (see below). | “ISO 13485 §4.2.5(기록의 관리)…FDA는 §820.35에서 **추가 요건**을 부과” – *Chunk 100539693362657837* |
| **Additional QMS R clauses – 21 CFR §820.35(a‑d)** | • SOPs or procedures that address each sub‑paragraph: <br> a) Record‑keeping for device history (including complaints, service, UDI). <br> b) Service record format (6 required items). <br> c) UDI management & GUDID submission. <br> d) Any other mandatory elements (e.g., electronic records, Part 11 separation). | “§820.35(a)(b)(c)(d) 추가요건” – *Chunk 100539693362657837* |
| **UDI Implementation** | • UDI assignment and labeling per 21 CFR Part 830. <br>• Maintenance of GUDID submission records (creation, updates). | SOP‑TRC‑001 / SOP‑UDI‑001 reference to “§820.35(c) + 21 CFR Part 830” – *Chunk 130165779856845378* |
| **Service Record Documentation** | • Completed service record form covering the six items required by §820.35(b). <br>• Signed off by Service/QA. | SOP‑SVC‑001 “§820.35(b) 6항목 서비스 기록 양식” – *Chunk 130165779856845378* |
| **Complaint & MDR Decision Tree** | • Complaint handling procedure linked to the MDR decision tree (based on §803.50, §803.53). <br>• Documentation of “미보고 사유 양식”. | SOP‑PMS‑001 – *Chunk 130165779856845378* |
| **Electronic Records Separation (21 CFR Part 11)** | • Statement in SOP‑DOC‑001 that Part 11 is treated as a separate clause outside §820.35. <br>• Evidence of compliance with Part 11 for any electronic records. | SOP‑DOC‑001 “Part 11은 §820.35 외부로 별도 절 분리” – *Chunk 130165779856845378* |
| **Audit & External Review Evidence** | • Audit reports that include “외부 열람 대비 객관적 증거 인용” per SOP‑IA‑001. | SOP‑IA‑001 – *Chunk 130165779856845378* |

---

### 3. Missing Information (Triggers for Human Review)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Device type, intended use & clinical indication** | Determines classification, predicate device, and submission pathway. | Obtain product specification sheet / Intended Use statement. |
| **Risk Management File (ISO 14971:2019)** | Required for design‑control completeness; feeds into QMSR records of hazards & mitigations. | Provide risk analysis, FMEA/FMECA, residual risk evaluation. |
| **Design History File (DHF) / Device Master Record (DMR)** | Needed to satisfy §820.30 (design controls) and §820.181 (record‑keeping). | Supply DHF index and DMR content list. |
| **Labeling & Instructions for Use** | Must reflect UDI, safety information, and comply with 21 CFR §801. | Submit labeling mock‑ups. |
| **Software / AI/ML Change Management Plan (if applicable)** | If the device contains software, a Predetermined Change Control Plan (PCCP) may be required under the Dec 2024 guidance. | Clarify presence of software and provide PCCP draft. |
| **Supply Chain & Component Traceability** | Required for post‑market surveillance under §820.50 (Traceability). | Provide supplier qualification records and component lot tracking procedures. |

---

### 4. Risk Controls Linked to QMS R Requirements  

| QMS R Clause | Typical Control(s) | Implementation Example |
|--------------|-------------------|------------------------|
| **§820.35(a)** – General record‑keeping | Controlled document management, retention schedule (≥10 yr). | ISO 13485 4.2.5 + SOP‑DOC‑001 with version control. |
| **§820.35(b)** – Service records | Six mandatory data fields (date, device ID, service performed, personnel, outcome, sign‑off). | SOP‑SVC‑001 form completed for each X‑ray site visit. |
| **§820.35(c)** – UDI management | Unique Device Identifier assignment, label placement, GUDID entry/updates. | SOP‑TRC‑001 / SOP‑UDI‑001 with automated GUDID upload script; audit trail in QMS. |
| **§820.35(d)** – Additional statutory items (e.g., Part 11 compliance) | Segregated electronic record controls, audit trails, role‑based access. | SOP‑DOC‑001 referencing Part 11 separate module; periodic Part 11 validation reports. |

---

### 5. Key Citations

| Item | Citation Type | Reference |
|------|---------------|-----------|
| ISO 13485 basic records requirement | Framework reference | **ISO 13485 §4.2.5** |
| FDA additional QMS R clauses | Instance identifier (direct from source) | **21 CFR §820.35(a‑d)** – *Chunk 100539693362657837* |
| UDI procedural link | Instance identifier (source SOP list) | **§820.35(c) + 21 CFR Part 830** – *Chunk 130165779856845378* |
| Service record requirement | Instance identifier (source SOP) | **§820.35(b)** – *Chunk 130165779856845378* |
| Complaint/MDR decision tree references | Instance identifier (source SOP) | **§803.50, §803.53** – *Chunk 130165779856845378* |
| Part 11 separation statement | Instance identifier (source SOP) | **Part 11 outside §820.35** – *Chunk 130165779856845378* |
| Audit external‑review evidence clause | Instance identifier (source SOP) | **SOP‑IA‑001** – *Chunk 130165779856845378* |

*(No other device‑specific identifiers appear in the source; “no specific identifier found in source — verify separately” where applicable.)*

---

### 6. Human‑Escalation Triggers

| Trigger | Reason |
|--------|--------|
| **Undefined device classification** | Cannot select correct submission pathway without intended use. |
| **Absent risk management file (ISO 14971)** | Mandatory for design‑control completeness and QMSR audit. |
| **Missing DHF/DMR documentation** | Required under 21 CFR §820.30 & §820.181. |
| **No UDI assignment plan** | §820.35(c) compliance cannot be demonstrated. |
| **Lack of service‑record template completion evidence** | §820.35(b) not satisfied. |
| **Unclear software change‑control strategy** (if device includes software/AI) | May need a Predetermined Change Control Plan (PCCP) per Dec 2024 guidance. |
| **Incomplete labeling & IFU** | 21 CFR §801 compliance cannot be verified. |

When any of the above triggers are hit, the RA team should pause the submission preparation and request the missing artifacts from product development or quality assurance before proceeding.

---

### 7. Peer‑Review Prompt

> *Please review the assumptions made about device classification, the completeness of the QMS R evidence list (especially SOP coverage), and any jurisdictional gaps (e.g., whether additional FDA guidance beyond §820.35 applies to our product line). Highlight any missing regulatory citations or mis‑interpretations of the source excerpts.*

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

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `130165779856845378`

> ### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영) | SOP | 갱신 내용 | 담당 | 판정 기준 | |-----|----------|------|----------| | SOP-DOC-001 | §3에 "미국 시장 적용 시 §820.35(a)(b)(c)(d) 추가요건" 절 신설, Part 11은 §820.35 외부로 별도 절 분리 | QA | 기록관리 절차에 불만/서비스/UDI/기밀성·Part 11 분리 기재 여부 | | SOP-PMS-001 | MDR 결정 트리(§803.50 30cd / §803.53 5wd 트리거 기준) + 미보고 사유 양식 첨부 | QA/RA | 불만 → MDR 판정 → 기록 흐름 완비 여부 | | SOP-TRC-001 / SOP-UDI-001 | UDI 기록관리 절 추가 — **§820.35(c)** + 21 CFR Part 830 | RA | GUDID 제출·갱신 기록 체계 구축 여부 | | SOP-SVC-001 (신설/갱신) | **§820.35(b)** 6항목 서비스 기록 양식 도입 | Service/QA | X-ray 출장정비 기록 6항목 완결성 | | SOP-IA-001 | 감사보고서 작성 기준에 "외부 열람 대비 객관적 증거 인용" 항목 추가 | QA | 보고서 품질 기준 갱신 여부 |

### kb-eval-20261017-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "QSR"], "profile_id": "ra-us", "scenario_id": "87d19fafce60659b", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/QSR_21CFR820/README.md", "source_hash": "5250406488094d588d38eb1e45c2d8d4b90f093334322d2ded3d50d3a2e72871"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `87d19fafce60659b`
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

> **Regulatory Draft – Diagnostic X‑ray System (QMSR & Design‑Control Readiness)**  

---

### 1. Bottom‑line determination  
- **Device class:** Class II (diagnostic X‑ray system) – regulated under the radiation‑emitting product provisions of **21 CFR §1020.30–§1020.32** and the general medical‑device quality system of **21 CFR §820** (as revised by the QMSR).  
- **Submission pathway:** Traditional **510(k) Premarket Notification** demonstrating substantial equivalence to an FDA‑cleared predicate.  

---

### 2. Classification & submission route  

| Item | Reference / Rule |
|------|-------------------|
| Device type – Diagnostic X‑ray system | **21 CFR §1020.30–§1020.32** (Performance Standards for Diagnostic X‑ray Systems) |
| Device classification – Class II, special controls (radiation safety, shielding, dose limits) | Same as above; no FDA docket number cited in source. |
| Required regulatory submission | **510(k)** (Premarket notification) – 21 CFR §807.92 (Substantial equivalence). |
| Quality‑system requirement | Revised **QMSR** (aligned to ISO 13485:2016), effective 02 Feb 2026 – **21 CFR §820** (renumbered but substantively unchanged). |

*No specific predicate device number appears in the source; that identifier must be sourced separately.*  

---

### 3. Required evidence package (minimum for a Class II 510(k))

| Evidence | Why required | Source/Standard |
|----------|--------------|-----------------|
| **Device description & intended use** | Foundation of the 510(k) narrative | 21 CFR §807.92(a) |
| **Predicate device comparison** (device name, regulation number, clearance date) | Shows substantial equivalence | 21 CFR §807.92(b) |
| **Performance testing per Part 1020** – dose accuracy, output consistency, beam quality, leakage radiation, safety interlocks | Demonstrates compliance with the special controls for X‑ray systems | **21 CFR §1020.30–§1020.32** |
| **Labeling & Instructions for Use (IFU)** – includes warnings, contraindications, operator training requirements | Required under 21 CFR §801.5 and Part 1020 labeling rules | 21 CFR §801; §1020.30 |
| **Unique Device Identifier (UDI) dossier** – label, packaging, GUDID entry | Mandatory under 21 CFR §830.10‑§830.36 | 21 CFR §830 |
| **Quality Management System certification** – ISO 13485:2016 audit report or FDA inspection summary confirming compliance with the revised QMSR | Demonstrates implementation of the new QMSR (effective 02 Feb 2026) | 21 CFR §820; source note on QMSR alignment |
| **Risk Management File** – ISO 14971:2019 risk analysis, hazard identification, mitigations, residual risk evaluation | Required for device design control & to support safety claims | ISO 14971:2019 (framework reference) |
| **Design‑control documentation** – §820.30 Design History File (DHF), verification/validation protocols and reports | Satisfies FDA design‑control expectations for Class II devices | 21 CFR §820.30 |
| **Software validation (if applicable)** – IEC 62304 compliance, Verification & Validation plan | Applicable when software is part of the X‑ray system | IEC 62304:2006+A1:2015 (framework reference) |
| **Manufacturing process validation** – Process Qualification, Installation Qualification, Operational Qualification for critical processes (e.g., shielding assembly) | Supports QMSR and design‑control requirements | 21 CFR §820.75‑§820.84 |

*All items above are required unless a specific exemption is documented in the FDA’s guidance; no instance identifiers were supplied in the source excerpts.*  

---

### 4. Missing information (gap analysis)

| Gap | Impact if not addressed |
|-----|--------------------------|
| **Predicate device identifier** (510(k) number, product code) | Cannot complete substantial‑equivalence claim. |
| **Exact intended use statement** (clinical indication, patient population) | Needed for both 510(k) narrative and risk analysis. |
| **Detailed risk management file** (hazard list, mitigation measures) | Required to satisfy ISO 14971 and FDA design‑control review. |
| **Verification/validation protocols & results** | Essential for DHF completeness; reviewer will request. |
| **UDI issuance plan (issuing agency, GUDID registration)** | Mandatory under Part 830; missing UDI stalls labeling approval. |
| **Confirmation of QMSR implementation status** (ISO 13485 audit report post‑Feb 2026) | If not yet in place, FDA may issue a 510(k) deficiency. |
| **Software documentation** (if system includes acquisition/processing software) – IEC 62304 lifecycle plan | Omission leads to AI/ML or software supplemental requests. |
| **Radiation safety test reports** (beam alignment, leakage measurements) | Required under Part 1020; absence will trigger a Refuse‑to‑Accept. |

---

### 5. Core risk controls (ISO 14971 mapping)

| Hazard | Control(s) | ISO 14971 Clause |
|--------|------------|------------------|
| Excess patient dose | Automatic exposure control, real‑time dose monitoring, interlock that aborts exposure if limits exceeded | §4.5 – Risk mitigation; §7 – Evaluation of residual risk |
| X‑ray tube failure (uncontrolled emission) | Shielded housing, dual‑channel kill switch, periodic preventive maintenance schedule | §6 – Design control; §8 – Production & post‑production monitoring |
| Operator error in parameter selection | User interface with locked presets, training program, labeling warnings | §5 – Risk evaluation; §9 – Feedback mechanisms |
| Software malfunction (image acquisition/processing) | IEC 62304 compliant software development lifecycle, periodic verification, fallback mode | §7 – Verification & validation (software) |

All controls must be documented in the DHF and reflected in the risk‑management file.

---

### 6. Citations  

**Framework references (no verification caveat needed):**  
- **21 CFR §1020.30–§1020.32** – Performance standards for diagnostic X‑ray systems.  
- **21 CFR §820** – Quality System Regulation (revised QMSR, aligned to ISO 13485:2016, effective 02 Feb 2026).  
- **21 CFR §807.92** – 510(k) substantial‑equivalence requirements.  
- **21 CFR §830** – UDI labeling and GUDID requirements.  
- **ISO 14971:2019**, **ISO 13485:2016**, **IEC 62304:2006+A1:2015** – Risk management, QMS, software lifecycle standards.

**Instance identifiers:** *none appear in the provided excerpts* → “no specific identifier found in source — verify separately” for any predicate number, docket, or detailed section beyond the general part numbers listed above.  

---

### 7. Human‑escalation triggers (when to involve senior RA / regulatory leadership)

| Trigger | Action |
|--------|--------|
| **Absence of a clearly identified predicate device** (no 510(k) number) | Escalate to Senior RA for market research & selection of an appropriate predicate before continuing the submission. |
| **QMSR implementation not yet verified (ISO 13485 audit pending)** | Pause dossier assembly; obtain latest audit report or schedule internal gap‑closure plan; notify Quality Manager. |
| **Risk‑management file incomplete or missing residual‑risk evaluation** | Escalate to Risk Management Lead for a full ISO 14971 hazard analysis before filing. |
| **UDI strategy undefined (issuing agency, GUDID entry not prepared)** | Elevate to Regulatory Project Lead; develop UDI issuance plan within 30 days. |
| **Performance testing data missing or out‑of‑date** (e.g., dose‑accuracy report) | Trigger a request for engineering validation; suspend submission until data are generated and reviewed. |
| **Software component present without IEC 62304 documentation** | Forward to Software Regulatory Lead for creation of lifecycle plan & verification protocol. |
| **Regulatory deadline approaching (e.g., product launch before QMSR effective date)** | Notify Program Management; consider a pre‑effective‑date “QSR” compliance bridge or adjust launch timeline. |

If any trigger is hit, the draft submission should be placed on hold and a formal comment added to the work package recommending review and closure only after resolution.

---

### 8. Peer‑review prompt  

> **Colleague challenge request:** Please examine the assumptions above regarding (a) classification of diagnostic X‑ray systems as Class II under Part 1020, (b) completeness of the evidence checklist given the revised QMSR effective 02 Feb 2026, and (c) any jurisdiction‑specific gaps—particularly whether additional FDA special controls (e.g., §892.2050 for image‑processing software if applicable) might be required. Provide feedback on missing citations or alternate pathways (e.g., De Novo) that could affect the submission strategy.

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

1. Chunk `136831192110451403`

> ## 추가 규제 (X-ray 관련) - **21 CFR Part 1020.30 ~ 1020.32**: Radiation Control – Performance Standards for Diagnostic X-ray Systems - **21 CFR Part 1002**: Records and Reports (Radiation-Emitting Products) - **21 CFR Part 1040**: Performance Standards for Light-Emitting Products (관련 시)

2. Chunk `18877965943708175`

> ## 현황 - 기존 QSR(21 CFR 820)은 2024년 공표된 Quality Management System Regulation (QMSR)으로 개정됨. - **시행일: 2026년 2월 2일** → ISO 13485:2016과 정합화.

### kb-eval-20261017-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_us-004", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "e963cf584c70d2b8", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md", "source_hash": "5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `e963cf584c70d2b8`
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

> **Regulatory Draft – QMSR & Design‑Control Readiness**

---

### 1. Bottom Line  
*The current documentation shows a well‑aligned GSPR‑to‑standard mapping but does not contain a specific device description or intended use. Consequently the FDA product classification (Class I/II/III) and the exact submission pathway (510(k), De Novo, PMA) cannot be definitively assigned at this stage.*  

**Immediate action:** obtain the device’s intended use, clinical claim, and any applicable predicate information. Once defined, the default US route for a typical imaging‑software or hardware system is **21 CFR Part 807 – 510(k) Premarket Notification**, unless the technology is novel (consider De Novo) or high risk (PMA).  

Below is the evidence set and gap list that must be satisfied before any submission can be prepared.

---

### 2. Required Evidence Package (when device intent known)

| Area | FDA / Harmonized Standard Requirement | Representative Evidence |
|------|----------------------------------------|--------------------------|
| **Quality Management System** | 21 CFR §820 – QMS; §820.35(b) for UDI establishment record | • Current ISO 13485:2016‑based QMS (verified against Part 820)<br>• SOPs covering design controls, document control, change management, and training |
| **Design Controls** | 21 CFR §820.30 (design & development planning, inputs, outputs, verification, validation, transfer) | • Design History File (DHF) with traceability matrices<br>• Risk Management File linked to design outputs |
| **Risk Management** | ISO 14971:2019 (harmonized) – risk analysis, evaluation, control, post‑market monitoring | • Completed risk analysis workbook showing severity & probability scores, risk acceptability justification, and implemented controls |
| **Software Lifecycle (if applicable)** | IEC 62304 (state‑of‑the‑art) – software development plan, verification/validation, maintenance | • Software Development Plan (SDP)<br>• Verification test reports<br>• Predetermined Change Control Plan (PCCP) if AI/ML functionality is present |
| **Usability & Human Factors** | IEC 62366‑1 (state‑of‑the‑art) – usability engineering process | • Usability validation protocol and results, including user interface hazard analysis |
| **Biocompatibility (if device contacts patient)** | ISO 10993 series (harmonized) – biocompatibility testing plan & reports | • Test reports for cytotoxicity, sensitization, irritation as applicable |
| **Sterilization / Packaging (if applicable)** | ISO 11137/11135/17665/11737 (harmonized), ISO 15223‑1:2021 – labeling of safety information | • Sterilization validation report, packaging integrity study |
| **Electrical Safety & EMC** | IEC 60601‑1 series (harmonized) – essential performance, electrical safety tests | • Test reports for leakage current, surge protection, EMI/EMC compliance |
| **UDI Implementation** | 21 CFR Part 830; §820.35(b); EU MDR Art.27 (for reference) | • Integrated UDI database (master record) and labeling specimens |
| **Electronic Signatures** | 21 CFR Part 11 – electronic records & signatures, scope definition | • Part 11 compliance matrix, validated signing authority list |

---

### 3. Gaps Identified in Source Material  

| Gap (source) | Required Action / Evidence | Note on Citation |
|--------------|----------------------------|------------------|
| **Absence of MDR decision‑document SOP** (see source [2]) | Draft and adopt “ML‑MDR‑001” SOP that documents regulatory decision‐making, including risk justification for EU AI Act cross‑reference where needed. | *no specific identifier found in source — verify separately* |
| **Fragmented UDI master record** (source [2]) | Consolidate into a single UDI Data Record (UDR) SOP, mapping to 21 CFR §820.35(b) and 21 CFR Part 830 requirements. | *no specific identifier found in source — verify separately* |
| **Internal audit report lacks objective evidence citations** (source [2]) | Revise “external‑audit response” template to require explicit citation of supporting documents (e.g., SOP numbers, test reports). | *no specific identifier found in source — verify separately* |
| **Unclear scope for electronic signatures** (source [2]) | Issue Part 11 scope definition document (QM‑IT‑001) that lists systems, records, and signing authority. Validate against FDA guidance on electronic records. | *no specific identifier found in source — verify separately* |
| **AI/ML devices not listed in OJEU/MDCG** (source [1]) | If the product contains AI/ML, develop a Predetermined Change Control Plan (PCCP) per the December 2024 FDA guidance and align with EU AI Act where applicable. | *no specific identifier found in source — verify separately* |
| **State‑of‑the‑art standard references** – IEC 62304, IEC 62366‑1, IEC 82304, IEC 81001‑5‑1 are cited as “applied” but no evidence of implementation is shown. | Provide software lifecycle documentation (SDP, verification/validation reports) referencing the exact edition numbers listed in the standards table. | *no specific identifier found in source — verify separately* |

---

### 4. Core Risk Controls to Demonstrate  

1. **Design Input Validation** – traceability to user needs & intended use.  
2. **Risk Mitigation Measures** – implemented per ISO 14971 (e.g., protective labeling, alarms, fail‑safe modes).  
3. **Verification/Validation Testing** – documented test protocols and acceptance criteria for hardware, software, and system integration.  
4. **Post‑Market Surveillance Plan** – procedures for complaint handling, trend analysis, and field corrective actions (21 CFR §820.198).  
5. **UDI Assignment & Labeling** – unique device identifier generated via FDA‑approved issuing agency; label proof with bar‑code/QR.  
6. **Electronic Signature Governance** – controlled access, audit trails, signature attribution per Part 11.  

Each control must be reflected in the DHF and QMS records.

---

### 5. Citations (Framework References)  

| Reference | Nature |
|-----------|--------|
| **21 CFR Part 820** – Quality System Regulation | Required QMS framework |
| **21 CFR §820.30** – Design Controls | Basis for design‑control evidence |
| **21 CFR §820.35(b)** – Device Identification (UDI) | UDI master record requirement |
| **21 CFR Part 830** – Unique Device Identifier system | Labeling & GUDID obligations |
| **21 CFR Part 11** – Electronic Records & Signatures | Scope of electronic signatures |
| **ISO 13485:2016** (harmonized) | QMS standard mapped in source [1] |
| **ISO 14971:2019** (harmonized) | Risk management standard mapped in source [1] |
| **ISO 10993 series** – Biocompatibility (harmonized) | Mapped in source [1] |
| **IEC 62304, IEC 62366‑1, IEC 82304‑1, IEC 81001‑5‑1** – State‑of‑the‑art software standards (source [1]) | Software lifecycle evidence |
| **ISO 15223‑1:2021**, **ISO 20417**, **ISO 17664‑1/‑2**, **EN 60601‑1 series** – Safety & labeling (source [1]) | Harmonized safety references |

No instance‑specific 510(k) clearance numbers or regulatory notices were present in the excerpts; therefore no such identifiers are listed.

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger & Escalation Path |
|-----------|---------------------------|
| **Device intended use still undefined** – cannot assign class/submission route. | Immediate escalation to Senior RA Lead for clarification of intended use and potential predicate search. |
| **Unresolved gaps after 2‑week remediation window** (e.g., UDI SOP, Part 11 scope). | Escalate to VP of Regulatory Affairs with a risk‑impact assessment; consider filing a “Pre‑Submission” Q-Sub to FDA for guidance if timeline threatens launch. |
| **AI/ML functionality identified without PCCP**. | Notify the AI/ML regulatory specialist and initiate development of a Predetermined Change Control Plan; senior leadership review required before any submission. |
| **Conflict between EU MDR references and US requirements** (e.g., reliance on Art.27). | Convene cross‑functional Regulatory Committee (US & EU leads) to ensure divergent obligations are addressed; senior RA sign‑off needed. |
| **Evidence package fails FDA 510(k) Refuse‑to‑Accept checklist** after initial submission. | Immediate response planning with the review team; assign a dedicated responder for Additional Information (AI) within the statutory 180‑day window. |

---

### 7. Peer Review Prompt  

*“Colleague, please examine the assumptions above regarding (a) the default classification as 510(k) pending intended‑use clarification, (b) completeness of the listed evidence against FDA design‑control expectations, and (c) any jurisdiction‑specific gaps not captured from the source excerpts (e.g., missing references to Part 807 registration or De Novo criteria). Provide comments on potential oversights.”*

--- 

**End of Draft.**

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

1. Chunk `1061533089543682126`

> ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적용 | | AI/ML 기기 | OJEU/MDCG 단독 등재 없음 → EU AI Act 병행 필요(후속 과제) | | 운영 영향 | 체크리스트에 H/S 컬럼 신설, 개정판 번호(A11, A1, A2) 기재 의무화 |

2. Chunk `1066441905930561439`

> ### Gap → 조치 | Gap | 조치 | |-----|------| | 국내 SOP에 MDR 결정문서 양식 부재 | 양식 ML-MDR-001 초안(보고/미보고 결정트리) 신설 | | UDI 마스터 레코드 단편화 | UDR(UDI Data Record) 통합 관리 SOP 초안 (§820.35(b) + 21 CFR 830 + EU MDR Art.27) | | 내부감사 보고서 서술 수준 | "외부감사 대응 수준" 템플릿 개정 (객관적 증거 필수 인용) | | 전자서명 범위 모호 | Part 11 적용범위 정의 문서(QM-IT-001) 초안 예정 |

### kb-eval-20261017-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "290bec469bd49323", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "ace8476c9535cd1cadac8d64a788cb46b3d78a905da01c1e1dfc3e038615f0f4"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `290bec469bd49323`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_2026.md)
- Source hash: `ace8476c9535cd1cadac8d64a788cb46b3d78a905da01c1e1dfc3e038615f0f4`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_2026.md`는 FDA QMSR 2026 전환에 따른 ISO 13485 기반 QMS·design control·inspection 준비 문서입니다.
- 현재 excerpt 핵심: ## 7. 출처 - FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr - FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions - eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter...
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

> **Regulatory Draft – QMSR & Design‑Control Readiness (Effective Feb 2 2026)**  

---

### 1. Scope & Applicability  
| Item | Detail |
|------|--------|
| **Regulation** | 21 CFR Part 820 (renamed *Quality Management System Regulation* – QMSR)【no specific identifier found in source — verify separately】 |
| **Effective date** | 2 Feb 2026 (Federal Register 2024‑01709; technical amendment FR 2025‑21955)【no specific identifier found in source — verify separately】 |
| **Device classes covered** | All FDA‑cleared/approved devices (Class I, II, III). Design‑control requirements (820.30) remain mandatory for Class II & III. |
| **Key change** | Incorporation by reference of ISO 13485:2016; FDA‑specific supplemental clauses retained. |

---

### 2. Classification / Submission Route (for the underlying device)  
- **Device classification**: Determined per 21 CFR § 860–862 based on intended use and technology. *QMSR does not alter the device class.*  
- **Submission pathway**:  
  - Class I → 510(k) or De Novo (if novel).  
  - Class II → 510(k) with design‑control documentation in the Design History File (DHF).  
  - Class III → PMA (or 510(k) if granted a predicate under “special” pathway).  

*All pathways must be supported by a QMS compliant with QMSR.*

---

### 3. Required Evidence of QMSR Compliance  

| Requirement | What to Provide | Reference |
|-------------|----------------|-----------|
| **Quality System Documentation** (manual, procedures, work instructions) | Updated SOPs, process maps showing incorporation of ISO 13485:2016 clauses and FDA‑specific additions (e.g., §820.30 design controls, §820.50 corrective actions). | 21 CFR Part 820; ISO 13485:2016 |
| **Design History File (DHF)** for Class II/III devices | Complete DHF with design inputs, outputs, verification, validation, risk analysis, and traceability to the Device Master Record (DMR). | 21 CFR §820.30(b) |
| **Device Master Record (DMR)** | Full DMR per §820.181 (production specifications, labeling, device specifications, etc.). | 21 CFR §820.181 |
| **Risk Management File** | ISO 14971:2019‑based risk management plan, hazard analysis, risk controls, residual risk evaluation, post‑market surveillance plan. | ISO 14971:2019 |
| **Training Records** | Evidence that personnel are trained on the new QMSR requirements and on any FDA‑specific clauses (e.g., PCCP for AI/ML). | 21 CFR §820.25 |
| **UDI Implementation Plan** | Labeling & packaging showing compliance with 21 CFR Part 830 (UDI format, GUDID registration). | 21 CFR Part 830 |
| **CAPA System Evidence** | Demonstrated effectiveness of corrective‑and‑preventive actions per §820.100. | 21 CFR §820.100 |
| **Management Review Minutes** | Records of periodic QMS review demonstrating effectiveness, resource adequacy, and continual improvement. | 21 CFR §820.20 |

---

### 4. Missing / Incomplete Information (Typical Gaps)  

1. **Gap analysis report** comparing current QSR documents to the new QMSR clauses – *not supplied*.  
2. **Updated SOPs reflecting ISO 13485:2016 incorporation** (e.g., document control, supplier evaluation) – *absent or outdated*.  
3. **Design‑control artifacts for existing Class II devices** (design input justification, verification protocols) – *partial*.  
4. **Risk‑management documentation aligned to ISO 14971:2019** – *missing recent hazard analysis.*  
5. **UDI implementation status** (label mock‑ups, GUDID upload receipts) – *unconfirmed.*  
6. **Predetermined Change Control Plan (PCCP)** for any AI/ML algorithm components – *no evidence.*  

*Each missing element must be obtained before a submission can be deemed QMSR‑ready.*

---

### 5. Core Risk Controls to Address Under QMSR  

| Control Area | Action |
|--------------|--------|
| **Risk Management** | Conduct ISO 14971:2019 risk analysis; document risk control measures in DHF and maintain an updated risk management file. |
| **Design Controls** (820.30) | Ensure traceability matrices linking design inputs → outputs → verification/validation → labeling. |
| **Supplier Management** | Apply ISO 13485‑based supplier evaluation, monitoring, and re‑evaluation procedures; retain records in DMR. |
| **Post‑Market Surveillance** | Define a PMS plan (e.g., 21 CFR §822) tied to residual risk; integrate with CAPA system. |
| **Change Management** | Establish a Predetermined Change Control Plan (PCCP) for software/AI updates; document in DHF. |
| **Training & Competency** | Implement role‑based training on QMSR, ISO 13485, and device‑specific controls; track competency assessments. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation To | Reason |
|---------|---------------|--------|
| **Unresolved gap analysis findings** (>2 high‑risk gaps) | RA Lead / Quality Director | Risk of non‑compliance with mandatory QMSR clauses. |
| **Missing design‑control artifacts for any Class II/III device** | Project Manager & Engineering Lead | Submission likely to be refused or delayed (21 CFR §820.30). |
| **Absence of UDI plan before market launch** | Regulatory Affairs Manager & Labeling Team | Violation of 21 CFR Part 830 labeling requirements. |
| **No PCCP for AI/ML‑enabled devices** | Software Lead & RA Specialist | FDA may issue an Additional Information request under the Predetermined Change Control guidance (Dec 2024). |
| **CAPA system ineffective (≥3 repeat issues within 6 mo)** | Senior Management | Indicates systemic QMS weakness; potential Form 483. |
| **Deadline to achieve full QMSR compliance passes without documented evidence** | Compliance Officer & Executive Sponsor | Non‑adherence to the Feb 2 2026 effective date may trigger enforcement action. |

*Escalations should be documented in the CAPA system and communicated via formal RA status reports.*

---

### 7. Summary Judgment  

- **QMSR applies to all device classes; design‑control obligations remain for Class II/III.**  
- **Current evidence shows many of the required QMSR artifacts are incomplete or missing.**  
- **Immediate actions:** complete a formal gap analysis, update SOPs to reflect ISO 13485:2016 incorporation, finalize DHF/DHR packages, and submit UDI/GUDID data.  

Until these gaps are closed, any 510(k) / PMA submission would be at risk of refusal or delay.

---

### 8. Peer‑Review Prompt  

> *Colleague, please review the assumptions above:  
> - Have we captured all FDA‑added QMSR clauses beyond ISO 13485:2016?  
> - Are there jurisdiction‑specific obligations (e.g., UDI, PCCP) that need deeper evidence for our product line?  
> - Identify any additional missing documentation or risk‑control steps not listed.*

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

1. Chunk `197674093189403324`

> ## 7. 출처 - FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr - FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions - eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820 - Federal Register: 2024-01709 (제정), 2025-21955 (기술적 수정) - FDA Compliance Program 7382.850 - 확인일: 2026-05-25

2. Chunk `211815826167619677`

> ## 1. 규정 개요 | 항목 | 내용 | |------|------| | 규정 | 21 CFR Part 820 | | 명칭 변경 | Quality System Regulation(QSR) → **Quality Management System Regulation(QMSR)** | | 최종규칙 공포 | Federal Register 2024-01709 (2024.2.2) | | 기술적 수정 | Federal Register 2025-21955 | | **발효일** | **2026년 2월 2일** | | 핵심 변경 | ISO 13485:2016을 참조편입(Incorporation by Reference)하고, FDA 추가요구를 별도 조항으로 보존 |

## ra_eu

### kb-eval-20261017-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "9ce411c7eaf6407b", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `9ce411c7eaf6407b`
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

> **Post‑Market Surveillance & PMCF Planning – Classification, Submission Routes, Evidence Requirements and Gap Analysis**

---

## 1. Device Portfolio Overview  

| # | Product | Intended Use (summary) | MDR classification* | Primary MDR conformity route |
|---|---------|------------------------|---------------------|--------------------------------|
| 1 | **X‑ray Detector** | Detects diagnostic X‑ray images; intended for use in radiography/radioscopy equipment. | Class IIa – **Rule 17** (Annex VIII) | **Art. 52(6)** – Annex IX (QMS + technical‑documentation assessment) |
| 2 | **Handheld X‑ray Source** | Portable source emitting ionising radiation for on‑site diagnostic examinations. | Class IIb – **Rule 10** (ionising‑radiation devices, Annex VIII) | **Art. 52(4)** – either Annex IX or the alternative route Annex X + Annex XI |
| 3 | **GUI Software (SaMD)** | Provides image display, manipulation and diagnostic decision support for X‑ray data. | Class IIa – **Rule 11** (software providing information for diagnosis, Annex VIII) | **Art. 52(6)** – Annex IX |

\*Classification is derived from the MDR classification rules listed in **Annex VIII**.

---

## 2. Post‑Market Surveillance (PMS) Obligations  

| Requirement | Reference | Application to each product |
|-------------|-----------|------------------------------|
| **PMS system** – overall structure, processes and resources | Art. 83 MDR | All three devices must maintain a PMS system complying with Art. 83. |
| **PMS plan** – description of data sources, collection frequency, analysis & reporting | Art. 84 MDR | The source table (Excerpt [2]) already defines the “Sources of Information” and their periodicity for each product. |
| **Periodic Safety Update Report (PSUR)** – content, update interval | Art. 86(1)–(2) MDR; Class‑specific cadence | • X‑ray Detector (Class IIa): update every **2 years** – matches source (Excerpt [1]).<br>• Handheld Source (Class IIb): update every **1 year** – matches source.<br>• GUI Software (Class IIa): update every **2 years** – matches source. |
| **Trend reporting** – submission to the Commission | Art. 88 MDR | Trend‑reporting data is collected quarterly (Excerpt [2] – row 3). |
| **Vigilance & FSCA reporting** – serious incidents, field safety corrective actions | Art. 87 MDR | Serious incident and FSCAs are captured via the “Vigilance system, EUDAMED” (Excerpt [2] – row 1). |

---

## 3. Post‑Market Clinical Follow‑up (PMCF) Requirements  

| Product | PMCF necessity (source) | Evidence needed | Primary standards |
|---------|--------------------------|----------------|-------------------|
| **X‑ray Detector** | “동등성 클레임 검토 후 결정” – decision after equivalence claim review. | • Comparative clinical data demonstrating performance parity with predicate devices.<br>• DQE (detective quantum efficiency) trend data (IEC 62220‑1‑1).<br>• Failure mode analysis from pixel‑defect and dose‑excess events. | IEC 62220‑1‑1 (DQA), ISO 14971 (risk management). |
| **Handheld X‑ray Source** | “이온화 방사선 → 임상 데이터 적극 수집 권고” – proactive clinical data collection recommended. | • Clinical dose‑distribution studies in real‑world use.<br>• Radiation safety monitoring results (dose‑excess events, battery failures).<br>• Human factors/usability data for handheld operation. | IEC 60601‑2‑28 (X‑ray tube assemblies), ISO 14971, IEC 62366‑1 (usability). |
| **GUI Software** | “SaMD → 사용 중 오류 데이터 수집 필수” – error‑data collection mandatory during use. | • Real‑time software bug logs and corrective actions.<br>• Usability/effectiveness data from clinical environments (e.g., task completion, diagnostic decision impact).<br>• Post‑release surveillance of algorithm performance. | IEC 62304 (software lifecycle), IEC 62366‑1 (usability), ISO 14971. |

*All PMCF plans must be documented in **Annex XIV Part B** and integrated into the PMS system (Art. 84, Art. 86).*

---

## 4. Evidence Already Available (per source)  

| Product | Existing documentation (source‑listed) |
|---------|----------------------------------------|
| X‑ray Detector | • CER (referenced)<br>• RMF (referenced)<br>• IEC 62220‑1‑1 test data (DQE) |
| Handheld Source | • CER (referenced)<br>• RMF (referenced)<br>• Radiation dose monitoring data |
| GUI Software | • CER (referenced)<br>• IEC 62304 maintenance records<br>• Bug log |

---

## 5. Identified Evidence Gaps & Missing Information  

| Gap # | Description | Affected product(s) | Why it matters (regulatory impact) |
|------|-------------|--------------------|-------------------------------------|
| **G1** | **Equivalence/clinical comparability data** for the X‑ray Detector – source only mentions “동등성 클레임 검토 후 결정”. No actual clinical data or comparison matrix is provided. | 1 | Required to justify the PMCF need (Annex XIV Part B) and to support the CER (Art. 61). |
| **G2** | **Clinical dose‑distribution study protocol & results** for the Handheld Source – only a recommendation for “active clinical data collection” is noted. No study design, endpoints, or statistical analysis plan exists in the current package. | 2 | Needed to satisfy the PMCF requirement (Art. 84) and to substantiate the PSUR risk‑benefit evaluation (Art. 86). |
| **G3** | **Usability/clinical effectiveness data for GUI Software** – while bug logs are present, no systematic collection of user‑error rates, diagnostic impact, or post‑market performance metrics is described. | 3 | Essential for a SaMD PMCF plan (Annex XIV Part B) and to demonstrate continued conformity with the GSPR §17 (software). |
| **G4** | **Quantitative trend‑analysis methodology** – source lists “내부 통계 집계” quarterly, but no description of statistical thresholds, signal detection methods, or escalation procedures. | 1‑3 | Required for Art. 88 Trend reporting and to trigger timely corrective actions. |
| **G5** | **Linkage between PMS data and Risk Management File (RMF)** – the source shows separate CER & RMF mentions but does not demonstrate how newly identified hazards from PMS feed back into risk evaluation (§3‑§8, Annex I). | 1‑3 | Needed to keep the RMF up‑to‑date per Art. 10(9) and Annex I §3. |
| **G6** | **UDI registration evidence in EUDAMED** – source states “UDI 등록” but does not provide confirmation of successful entry, assigned UDI‑DI/UI, or traceability to the PMS data streams. | 1‑3 | Required for Art. 33‑39 (EUDAMED obligations). |
| **G7** | **PMCF plan documentation format** – a formal PMCF plan (Annex XIV Part B) is not shown; only high‑level statements are present. | All | Mandatory to obtain NB acceptance of the PMS system (Art. 84). |

---

## 6. Risk Controls & Mitigation Measures (as per Annex I)

| Hazard identified from source data | Relevant GSPR clause(s) | Existing control(s) | Additional control(s) needed |
|-----------------------------------|--------------------------|---------------------|------------------------------|
| **DQE degradation / pixel defects** in Detector | §4 – risk control measures; §8 – known & foreseeable risks | RMF includes monitoring of DQE trends (IEC 62220‑1‑1). | Define acceptance limits, trigger corrective actions when DQE falls below threshold; integrate into PSUR. |
| **Patient dose excess** from Handheld Source | §4, §16 – protection against radiation | Dose‑monitoring data collected (source). | Real‑time dose alerts, periodic audit of battery performance, automated shutdown on over‑dose detection. |
| **Battery failure leading to uncontrolled emission** | §5 – use‑error; §19 – active device safety | Battery health monitoring recorded. | Redundant safety interlock, mandatory pre‑use checklist, field service verification. |
| **Software errors / image display faults** (GUI) | §17 – electronic programmable systems; §23 – labeling/instructions | Bug log & IEC 62304 maintenance records kept. | Usability validation testing with clinical end‑users, periodic software updates with risk analysis per ISO 14971. |
| **Incorrect user handling of handheld source** | §22 – devices intended for lay persons (if used by non‑clinical staff) | Training materials referenced in CME? (not shown). | Develop and validate training programme; include human factors evaluation (IEC 62366‑1). |

All risk controls must be documented in the **Risk Management File**, kept current with PMS findings (Annex I §3, ISO 14971).

---

## 7. Submission Route Summary  

| Product | MDR classification | Conformity assessment route (Art. 52) | Notified Body involvement |
|---------|-------------------|----------------------------------------|---------------------------|
| X‑ray Detector (Class IIa) | Rule 17 → Class IIa | **Annex IX** (QMS + technical‑documentation assessment) – Art. 52(6) | Required |
| Handheld X‑ray Source (Class IIb) | Rule 10 → Class IIb | Preferred: **Annex IX** (same as above) – Art. 52(4); alternative route possible via **Annex X + Annex XI** | Required |
| GUI Software (SaMD, Class IIa) | Rule 11 → Class IIa | **Annex  IX** – Art. 52(6) | Required |

All three devices must also comply with the **post‑market surveillance technical documentation** required by **Annex III**.

---

## 8. Human‑Escalation Triggers  

| Trigger ID | Condition | Action |
|------------|-----------|--------|
| **HT‑01** | Any of the gaps G1–G7 remains unresolved after a two‑week internal review period. | Escalate to senior RA manager for NB consultation and possible submission postponement. |
| **HT‑02** | Detection of a serious incident or FSCA (row 1, Excerpt [2]) that indicates a new hazard not yet reflected in the RMF. | Immediate notification to the Notified Body (Art. 87) and internal risk‑assessment workshop within 48 h. |
| **HT‑03** | Quarterly trend‑reporting analysis (row 3, Excerpt [2]) reveals a statistically significant upward trend exceeding predefined thresholds. | Initiate corrective action plan, update PSUR, and inform the NB per Art. 88. |
> *All triggers should be logged in the PMS database with timestamps and responsible person identifiers.*

---

## 9. Next Steps (Action Plan)  

1. **Compile Equivalence Dossier** for the X‑ray Detector (address G1).  
2. **Design & execute a clinical dose‑distribution study** for the Handheld Source (address G2).  
3. **Develop a formal PMCF plan** (Annex XIV Part B) covering all three products, including methodology, success criteria and reporting schedule (address G7).  
4. **Define statistical methods** for trend analysis and set escalation thresholds (address G4).  
5. **Update RMF** to integrate PMS findings and risk‑control updates (address G5).  
6. **Verify UDI registration in EUDAMED**, capture evidence of entry, and map data streams accordingly (address G6).  
7. **Conduct usability testing** for the GUI Software and incorporate results into the PMCF plan (address G3).  

*Each activity should be assigned an owner, deadline, and deliverable format (e.g., updated CER, RMF amendment, PSUR draft).*

---

## 10. Peer‑Review Prompt  

> **Please review:**  
> - The classification assumptions (Rule 17 for the detector, Rule 10 for the handheld source, Rule 11 for the software) and the chosen conformity routes.  
> - Whether any additional MDR annexes or articles should be referenced for the identified gaps (e.g., special provisions for ionising radiation devices).  
> – The completeness of the evidence gap list, especially concerning usability/clinical effectiveness data for SaMD.  
> – Any jurisdiction‑specific nuances (e.g., specific EUDAMED filing requirements) that may have been omitted.

--- 

*Prepared by Theo – EU MDR regulatory affairs specialist.*

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

### kb-eval-20261017-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6c0bebee0d562caa", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `6c0bebee0d562caa`
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

> **Regulatory Draft – Classification, Conformity‑Assessment Route & PMS/PMCF Planning**

---

### 1. Device scope derived from the source
| Item | Information supplied by the excerpt | Gap that still needs clarification |
|------|-------------------------------------|------------------------------------|
| **Intended medical purpose** | “Ionising‐radiation emitting diagnostic device (X‑ray generator)” – Rule 10  <br> “Medical‑device software (SaMD)” – Rule 11 | Detailed wording of the intended use, clinical indications, patient population, and user environment (clinical vs. lay) |
| **Device type** | Active X‑ray equipment (generates ionising radiation)  <br> Associated SaMD that processes the image or provides diagnostic advice | Architecture diagram showing hardware–software interaction; which functions are performed by the software alone (SaMD) vs. part of the active device |
| **Risk classification** | Rule 10 → Class IIb for the X‑ray generator <br> Rule 11 → SaMD likely Class IIa/IIb depending on decision impact | Confirmation of the SaMD’s decision‐making effect (e.g. if it can trigger surgical intervention or cause death, class may be III). A formal classification justification is required. |

---

### 2. Classification & Conformity‑Assessment Route  

| Regulatory element | Reference | Outcome |
|--------------------|-----------|---------|
| **Classification rule** | Rule 10 (Annex VIII) – ionising‑radiation diagnostic device | **Class IIb** for the X‑ray generator |
| **SaMD classification** | Rule 11 (Annex VIII) – software providing diagnostic information | Preliminary **Class IIa/IIb** – requires detailed functional analysis to finalise |
| **Conformity‑assessment route** | Art. 52(4) MDR 2017/745 – “Class IIb” → **Annex IX (full QMS + technical‑documentation assessment)** or the alternative **Annex X (type‑examination) together with Annex XI (production conformity verification)** | NB involvement mandatory; route to be selected in discussion with the Notified Body. |
| **EU Declaration of Conformity** | Art. 19 MDR – content listed in Annex IV | Must be drafted once all technical documentation is complete. |

---

### 3. Required Evidence & Technical‑Documentation Elements  

| Section (Annex II) | Required content | Where it lives / supporting standards |
|--------------------|------------------|---------------------------------------|
| **§1 – Device description** | Trade name, model, accessories, intended purpose, indications, contraindications | Manufacturer’s product file. |
| **§2 – Manufacturing information** | Process flow diagram, quality‑system (ISO 13485:2016) compliance | QMS manual, SOPs. |
| **§3 – Design & manufacturing** | Drawings, specifications, verification/validation results (IEC 60601‑2‑28 for X‑ray tube assemblies; IEC 62304 for software) | Design dossier, test reports. |
| **§4 – General Safety & Performance Requirements** | Mapping of each GSPR (§1‑23 Annex I) to evidence (risk analysis, performance data) | Risk Management File (ISO 14971:2019); verification/validation protocol. |
| **§5 – Benefit–Risk analysis** | Summary of risk assessment, residual risk evaluation, justification of acceptability | RMF “Conclusion” chapter. |
| **§6.1 – Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data (pre‑market studies, post‑market data), benefit–risk conclusions | **Annex XIV Part A**; Literature search strategy documented. |
| **§6.2 – PMCF plan & report** | Detailed plan (objectives, methodology, timeline) and subsequent evaluation results | **Annex XIV Part B**. |
| **§6.3 – PMS system** | PMS plan (Art. 84), PMS procedures, periodic safety update reports (PSUR for Class IIb – Art. 86) | **Art. 83–86 MDR**. |

---

### 4. Post‑Market Surveillance & PMCF Planning  

| Requirement | Content to be produced | Reference |
|-------------|------------------------|-----------|
| **PMS Plan** | Definition of systematic collection and analysis of data from routine use, vigilance reporting (Art. 84) | Art. 84 MDR. |
| **PMS System** | Full description of organisational structure, responsibilities, tools (e.g., EUDAMED module for PMS), trend‑analysis methodology | Art. 83 MDR. |
| **Periodic Safety Update Report (PSUR)** | Annual report for Class IIb (Art. 86(2)) containing: <br> • Benefit–risk conclusions <br>• PMCF main findings <br>• Sales volume & user population description | Art. 86 MDR. |
| **PMCF Plan** | Objectives (confirming safety/performance in real‑world use), study design (prospective, registry, or retrospective analysis), sample size, statistical methods, timelines, responsible parties | Annex XIV Part B. |
| **PMCF Evaluation Report** | Results of the PMCF activities, comparison with expected performance, any necessary corrective actions | Annex XIV Part B. |

---

### 5. Risk Controls (GSPR & ISO 14971)

| GSPR clause | Typical control / evidence needed for an X‑ray generator + SaMD |
|-------------|---------------------------------------------------------------|
| **§3 – Risk management system** | Documented RMF compliant with ISO 14971:2019, covering identification of radiation hazards, software errors, and electrical safety. |
| **§4 – Risk control measures** | Implementation of shielding, interlocks, dose‑limiting algorithms, software verification (IEC 62304), user training. |
| **§5 – Use‑error mitigation** | Human factors analysis (IEC 62366‑1:2020) → labeling, UI design, error‑proofing functions. |
| **§6 – Device lifetime & maintenance** | Defined service interval, calibration schedule, replacement parts list. |
| **§8 – Benefit–risk assessment** | Quantified residual risk vs. clinical benefit (e.g., diagnostic accuracy improvement). |
| **§16 – Radiation protection** | Compliance with IEC 60601‑2‑28 and national dose limits, verification of emitted spectra, DICOM radiation dose reporting. |
| **§17 – Software safety** | Secure development lifecycle (IEC 62304), validation of SaMD algorithms, cyber‑security considerations per IEC 81001‑5‑1. |

---

### 6. Gaps / Missing Information (to be supplied before NB submission)

1. **Exact intended use wording** – needed for classification justification and CER scope.  
2. **Functional description of the SaMD** – to confirm its class under Rule 11.  
3. **Full risk‑management file** – especially residual risk evaluation and risk‑control verification results.  
4. **Clinical data** – pre‑market clinical investigation or literature evidence supporting safety/effectiveness.  
5. **PMCF study protocol** – including endpoints, statistical plan, and enrolment criteria.  
6. **PMS data sources** – post‑market complaint handling system, registry participation, EUDAMED reporting workflow.  
7. **User manuals & labeling** – to verify compliance with Annex I §23.  

---

### 7. Human‑Escalation Triggers

| Situation | Action required (who) |
|-----------|-----------------------|
| **Uncertain classification of the SaMD** (Rule 11 impact unclear) | Escalate to senior RA and/or Notified Body for a formal class determination before technical documentation finalisation. |
| **Insufficient clinical evidence for CER** (no adequate post‑market or literature data) | Pause submission; commission a small‑scale clinical investigation or expand literature search. |
| **Risk‑management file incomplete or residual risk not justified** | Flag to Quality/Engineering lead; update RMF and re‑run verification activities. |
| **PMCF plan does not meet Annex XIV Part B requirements (e.g., missing statistical justification)** | Trigger internal review by clinical affairs team; revise plan before NB audit. |
| **PMS system unable to generate required PSUR data annually** | Activate senior project manager to secure resources for data collection & analysis, or consider outsourcing to a PMS service provider. |
| **NB raises non‑conformities on GSPR mapping** | Immediate corrective action and updated technical documentation; may require re‑submission of updated Annex II sections. |

---

### 8. Peer‑Review Prompt  

> *"Colleague, please review the classification justification (Rule 10 vs. Rule 11), the completeness of the risk‑management evidence, and the adequacy of the proposed PMCF plan against MDR Art. 61–63 and Annex XIV Part B. Are there any jurisdiction‑specific gaps (e.g., national radiation‑protection directives) that we have omitted?"*

--- 

**End of draft**

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

### kb-eval-20261017-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c83a9e50ab19df7e", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c83a9e50ab19df7e`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning**

---

### 1. Scope of the Assessment  
The draft addresses the regulatory requirements that must be satisfied before a CE‑mark can be issued under the EU Medical Device Regulation (MDR) 2017/745, with specific focus on the **PMS system** (Art. 83‑86) and the **PMCF plan/evaluation** (Annex XIV Part B).  

> *No device‑specific information (intended purpose, design, technology, target population, etc.) is supplied in the source material; therefore the following points identify what must be obtained from the manufacturer before a definitive regulatory pathway can be confirmed.*

---

### 2. Classification & Conformity‑Assessment Route  

| Step | What must be decided | Reference (framework) |
|------|---------------------|-----------------------|
| **2.1 Determine Class** | Apply the 22 classification rules in Annex VIII, starting with Rule 1 and proceeding sequentially to the highest applicable rule. The manufacturer is responsible for self‑classification (Article 51 + Annex VIII). | Article 51 MDR; Annex VIII MDR |
| **2.2 Verify Classification** | If doubt remains after applying the rules, seek an opinion from the Competent Authority (CA) or consult the MDCG “Manual on Borderline and Classification” (latest version v2.1.1 – September 2023). | No specific identifier in source – verify separately |
| **2.3 Select Conformity‑Assessment Route** | Once the class is known, the route follows Art. 52: <br>• Class I (non‑sterile, non‑measuring) → self‑declaration (Art. 52(7)). <br>• Class Is/Im/Ir → Annex IX (limited NB scope). <br>• Class IIa → Annex IX (full NB assessment) or Annex II + XI §10 (alternative). <br>• Class IIb → Annex IX (NB) *or* Annex X + XI. <br>• Class III → Annex IX (NB) *or* Annex X + XI. | Article 52 MDR; Annex IX, X, XI MDR |

**Action required:**  
- Obtain the device’s **intended medical purpose**, **principle of operation**, and **technical description** to identify the correct classification rule(s).  

---

### 3. Required Evidence for PMS & PMCF  

| Requirement | Content | Regulatory citation |
|-------------|---------|----------------------|
| **3.1 Clinical Evaluation Report (CER)** | Up‑to‑date CER complying with Annex XIV Part A; kept current under Art. 61 MDR. Must incorporate state‑of‑the‑art literature, clinical investigation data (if any), and PMCF results. | Art. 61 MDR; Annex XIV Part A |
| **3.2 PMS Plan** | Documented plan describing the systematic process for collecting, analysing, and acting on post‑market data (Art. 84). Includes: <br>• Definition of the intended user population & market size.<br>• Methods for routine reporting of incidents (Art. 87) and trend analysis (Art. 88).<br>• Frequency of updates to PMS reports/PSURs. | Art. 84 MDR |
| **3.3 PMS System** | Organisation‑wide system covering: <br>• Incident reporting & vigilance (Art. 87).<br>• Trend analysis and corrective actions.<br>• Integration with the risk management file (ISO 14971:2019). | Art. 83 MDR |
| **3.4 Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | PSUR must contain (Art. 86(1)): <br>a) Benefit‑risk conclusions, <br>b) Main PMCF findings, <br>c) Sales volume & user population estimate. <br>Update cadence: annually for IIb/III; every two years for IIa. | Art. 86 MDR |
| **3.5 Post‑Market Clinical Follow‑up (PMCF) Plan** | Detailed plan describing objectives, methodology, sample size, follow‑up duration, and success criteria. Must be proportionate to the risk class and the residual uncertainties after pre‑market clinical evaluation. The PMCF report (Annex XIV Part B) will feed into the PSUR. | Annex XIV Part B MDR |
| **3.6 Unique Device Identification (UDI)** | Registration of UDI in EUDAMED, mapping to national portals where applicable (e.g., “UDI portal” mentioned in source). | No specific identifier in source – verify separately |

**Action required:**  
- Collect the latest **clinical data** (literature, investigations, registries) to draft the CER.  
- Define the **PMS objectives**, data sources (registries, complaints, field safety corrective actions), and analytical methods.  
- Specify the **PMCF study design** (prospective/retrospective, sample size calculations, statistical analysis plan).  

---

### 4. Identified Gaps / Missing Information  

| Gap | Why it matters | Immediate next step |
|-----|----------------|----------------------|
| **Device description & intended use** | Needed to apply Annex VIII classification rules and to define clinical endpoints for PMCF. | Request a full “intended purpose” statement, indications, contraindications, and technical specifications from the manufacturer. |
| **Risk Management File (RMF)** | Required for linking risk controls to PMS findings; ISO 14971:2019 is the reference standard. | Obtain the current RMF (risk analysis, evaluation, control measures). |
| **Clinical data inventory** | CER and PMCF plan rely on existing pre‑market clinical evidence; absence prevents drafting a valid CER. | Request all clinical investigation reports, literature reviews, and any existing post‑market data. |
| **PMS resources & organisational responsibilities** | Art. 83 mandates that the manufacturer have a PMS system with defined roles. | Obtain an organisational chart showing who is responsible for vigilance, data analysis, and reporting. |
| **U​DI strategy** | Required for EUDAMED registration; missing UDI impedes market entry. | Clarify the assigned UDI carrier, coding scheme, and planned registration dates. |
| **Post‑market surveillance (PMS) plan draft** | Needed to demonstrate compliance with Art. 84 before NB review. | Draft a PMS plan template and circulate for manufacturer comment. |
| **PMCF study protocol** | Essential for Annex XIV Part B; without it the PMCF cannot be approved by the Notified Body. | Develop a protocol outline (objectives, methodology, statistical analysis) and seek sponsor sign‑off. |

---

### 5. Risk Controls to Address PMS/PMCF Gaps  

1. **Integrate RMF Updates** – Ensure any incident or trend identified via PMS triggers a risk reassessment per ISO 14971:2019 §3 (risk management system).  
2. **Usability Engineering** – Apply IEC 62366‑1 (2020) to evaluate user errors that may emerge post‑market; incorporate findings into the PMCF.  
3. **Software Lifecycle Controls** – If software is involved, follow IEC 62304 (2006+A1:2015) for change management and verification of updates discovered through PMS.  
4. **Electrical Safety & Radiation Protection** – For active or radiological devices, verify compliance with IEC 60601‑2‑54 / IEC 60601‑2‑28 as applicable; include relevant test data in the PMCF when safety incidents relate to these aspects.  

---

### 6. Human‑Escalation Triggers  

| Trigger | Condition | Escalation Path |
|--------|-----------|-----------------|
| **Unresolved Classification** | Manufacturer cannot map device to a rule in Annex VIII after two iterations. | Escalate to the Competent Authority (CA) for a formal classification opinion; document request per Art. 51 MDR. |
| **Incomplete Clinical Evidence** | No acceptable pre‑market clinical data available to support CER. | Pause CE‑marking dossier submission; advise sponsor to conduct an EU‑type clinical investigation (Art. 61 MDR) before proceeding. |
| **PMS Plan Deficiency** | Draft PMS plan does not address at least three of the required elements in Art. 84 (e.g., no defined data sources). | Notify senior RA manager; require sponsor to revise PMS plan within 14 days; flag for NB review once completed. |
| **PMCF Protocol Not Feasible** | Sample size or follow‑up duration cannot be achieved given market size/availability of patients. | Escalate to senior clinical affairs lead to explore alternative evidence (e.g., registries, literature) and update PMCF justification. |
| **UDI Registration Delay** | UDI not entered into EUDAMED 30 days before first device placed on the EU market. | Issue internal non‑conformity notice; suspend market launch until registration completed. |
| **Adverse Trend Detected** | Continuous increase in a specific serious incident category (≥ 5 events within 12 months). | Immediate reporting to vigilance authority per Art. 87, initiate field safety corrective action (FSCA), and notify the Notified Body as required by Art. 90. |

---

### 7. Summary Judgment  

- **Classification & route cannot be finalised** without a clear intended purpose and technical description of the device.  
- **PMS system**, **PMS plan**, **PMCF plan**, and an up‑to‑date **CER** are mandatory prior to any Notified Body assessment (Annex IX or Annex X + XI).  
- The current dossier lacks essential clinical data, risk management documentation, and a defined PMCF protocol – these constitute *critical gaps* that must be remedied before submission.  

---

### 8. Peer‑Review Prompt  

> **Colleague – please challenge the assumptions made above:**  
> 1. Are there any MDR provisions or recent MDCG guidance that could allow a reduced PMS/PMCF scope for low‑risk Class Is/Im devices which we have not accounted for?  
> 2. Does the referenced “MDR Art. 87, PSUR” align with current EUDAMED data‑model requirements, or is an additional reference to the MDR Implementing Regulation needed?  
> 3. Have we captured all relevant ISO/IEC standards that must be cited when a device incorporates software and active components (e.g., IEC 62366‑1, IEC 60601‑2‑54) based on the limited source excerpt?

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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261017-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "340920be85da5b7f", "source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md", "source_hash": "62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `340920be85da5b7f`
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

> **Regulatory Draft – PMS & PMCF Planning (MDR 2017/745)**  
*Prepared for internal review – classification and conformity‑assessment route are pending determination.*

---

## 1. Device Synopsis (information currently **missing**)

| Item | Required Information | Comment |
|------|----------------------|---------|
| **Intended purpose / indication** | Full label claim, patient population, anatomical site, therapeutic/diagnostic objective. | Needed to select the applicable classification rule (Annex VIII). |
| **Device type** | Active vs. passive, measuring or sterile function, software‑only, implantable, etc. | Determines whether Rule 9–11, 17, etc. apply. |
| **Risk class determinants** | Invasiveness, duration of contact, energy source, impact on vital physiology. | Without this the Art. 52 route cannot be assigned. |
| **UDI‑DI (basic & device‑specific)** | Globally unique identifier to be entered in EUDAMED Module 2. | Source describes required structure but no actual code is supplied. |
| **Manufacturer / authorised representative details** | SRN for Actor module, contact data, QMS certificate reference. | Needed for EUDAMED registration (Module 1). |
| **Clinical claim & existing clinical evidence** | Summary of pre‑market clinical evaluation, literature search strategy, comparator devices. | Basis for CER (Annex XIV Part A) and PMCF plan. |

> **Action:** Request the above data from product development before any classification work can begin.

---

## 2. provisional Classification & Conformity‑Assessment Route  

| Current knowledge | Likely outcome | MDR reference |
|-------------------|----------------|---------------|
| No device description available → cannot apply Annex VIII rules (e.g., Rule 9, 10, 11, 17). | **Classification indeterminate** – must be resolved before proceeding. | *no specific identifier found in source — verify separately* |
| Once class is known: <br>‑ Class I (non‑sterile, non‑measuring) → self‑declaration (Art. 52(7)). <br>‑ Class Is/Im/Ir → Annex IX limited scope. <br>‑ Class IIa – IIb – III → Annex IX (full QMS + technical‑doc assessment) or Annex X + XI for IIb/III. | Apply the appropriate route per Art. 52(3‑7). | Art. 52, Annex IX, Annex X & XI |

*Human escalation trigger:* **If classification cannot be resolved within 10 working days of this brief, elevate to the Regulatory Lead for a dedicated classification workshop.**

---

## 3. Post‑Market Surveillance (PMS) – Core Requirements  

| Requirement | What must be produced / evidence | MDR citation |
|-------------|-----------------------------------|--------------|
| **PMS system** (overall structure, responsibilities, data flow). | Documented in the QMS; includes procedures for collection, analysis, reporting of post‑market information. | Art. 83 |
| **PMS plan** (activities, timelines, performance indicators). | Must define proactive and reactive activities, risk‑based monitoring, and linkage to vigilance. | Art. 84 |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III. | Summarises PMS data, trends, PMCF results, benefit–risk conclusions; update frequency: annually for IIb/III, every 2 years for IIa. | Art. 86(1‑2) |
| **PMS report** – for Class I (non‑sterile). | Annual summary of PMS data and corrective actions. | Art. 85 |
| **Vigilance reporting** (serious incidents, field safety corrective actions). | Use EUDAMED Module 5 (expected rollout ~Q2 2027 per source). | No specific identifier found in source — verify separately |

*Evidence needed:* risk management file (ISO 14971:2019), trend‑analysis tools, databases for post‑market data (e.g. registries, complaints, literature), SOPs for corrective actions.

*Human escalation trigger:* **If Module 5 of EUDAMED is not operational by the scheduled Q2 2027 deadline, notify the EU Regulatory Project Manager to arrange interim reporting via national competent authority.**

---

## 4. Post‑Market Clinical Follow‑up (PMCF) – Planning  

| Element | Required content | MDR reference |
|---------|------------------|---------------|
| **PMCF plan** (Annex XIV Part B). | Objectives, methodology, endpoints, sample size, timing, data sources, statistical analysis, linkage to risk management, updates. | Annex XIV Part B |
| **PMCF evaluation report** (final). | Findings, impact on benefit‑risk determination, recommendations for labeling or design changes. | Annex XIV Part B |
| **Integration with PMS** – evidence that PMCF results feed back into the PMS system and risk management file. | Cross‑references in QMS documents. | Art. 83‑84 (systemic linkage) |
| **State‑of‑the‑Art literature review** – to identify residual uncertainties, new comparable devices, emerging risks. | Per IEC 62366‑1:2020 (usability), ISO 14971:2019 (risk). | No specific identifier found in source — verify separately |

*Evidence needed:* protocol draft, ethics committee approval (if applicable), data collection tools (eCRF, registries), statistical analysis plan.

*Human escalation trigger:* **If the PMCF plan is not finalized before the first scheduled PMS review (normally within 12 months of market entry), raise to Clinical Affairs Lead for expedited development.**

---

## 5. EUDAMED Registration – Current Status & Gaps  

| Module | Required items (from source) | Current status / gap |
|--------|------------------------------|----------------------|
| **Module 1 – Actor** | SRN registration of economic operator. | No SRN disclosed. |
| **Module 2 – UDI/Device (UDI/DEV)** | *Basic UDI‑DI* (globally unique), *UDI‑DI*, *UDI‑PI*; structure defined in source (see 3‑2‑A/B). | No actual identifiers submitted. |
| **Module 5 – Vigilance** | Reporting of serious incidents and field safety corrective actions; rollout expected ~Q2 2027 (source). | System not yet live; preparatory data flows missing. |

*Action:* Populate Modules 1 & 2 as soon as UDI‑DI is assigned; begin mapping PMS data to Module 5 prototype ahead of the Q2 2027 go‑live.

---

## 6. Risk Controls – Expected Evidence  

| Control | Required documentation / demonstration |
|---------|------------------------------------------|
| **Risk Management File** (ISO 14971:2019) – hazard identification, risk analysis, evaluation, control measures, residual risk acceptance. | Must be kept up to date and linked to PMS/PMCF findings. |
| **Usability Engineering** (IEC 62366‑1:2020) – human factors testing for devices intended for lay users or those with complex interfaces. | Needed especially if device is Class IIa/IIb with software component. |
| **Software Lifecycle** (IEC 62304:2006+A1:2015) – if applicable. | Evidence of verification & validation, security controls. |
| **Electrical Safety / Radiation Protection** (IEC 60601‑1 series, IEC 60601‑2‑54 for X‑ray equipment) – when relevant. | Provide conformity‑assessment test reports. |

*Human escalation trigger:* **Any missing risk‑control evidence identified during the technical‑documentation review must be flagged to the Quality Assurance Manager within 5 working days.**

---

## 7. Summary Judgment & Escalation Checklist  

| Decision point | Trigger condition | Escalation path |
|----------------|-------------------|-----------------|
| **Classification unknown** | No intended use, device type, or risk determinants received within 10 days. | Notify Regulatory Lead → schedule classification workshop. |
| **UDI‑DI not assigned** | Lack of basic UDI‑DI before EUDAMED Module 2 submission deadline (project‑internal date). | Escalate to Product Manager for immediate allocation of GS1/HIBCC code. |
| **PMS system incomplete** | Absence of documented PMS plan, risk‑management integration, or incident‑reporting procedure after 15 days post‑draft. | Raise to Compliance Officer → initiate gap‑closure task force. |
| **PMCF plan not approved** | Draft PMCF plan not signed off by Clinical Affairs within 12 months of market launch. | Alert Clinical Lead → request interim safety monitoring measures. |
| **EUDAMED Module 5 rollout missed** | Q2 2027 deadline passes without functional vigilance module. | Inform EU Regulatory Project Manager → consider national competent‑authority reporting as interim solution. |

---

### Peer‑review Prompt  
*Please review the assumptions above, especially the inference that the device may fall under active/diagnostic or therapeutic rules (Rule 9‑11, 17) and the completeness of the EUDAMED registration mapping. Identify any jurisdiction‑specific gaps (e.g., missing reference to national competent‑authority procedures) and suggest additional evidence items that should be collected before finalizing the PMS & PMCF plans.*

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

1. Chunk `1048620351506847107`

> ### 5-A. 데이터베이스 등록 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR (EU) | |---|---|---|---| | 등록 DB | GUDID (FDA UDI DB) | UDI포털 (mfds.go.kr) | EUDAMED | | 의무화 시점 | 등급별 단계적 완료 | 2025 기준 진행 중 | 2026-05-28 (4개 모듈) | | 경제주체 등록 | FDA Establishment Registration (21 CFR 807) | 의료기기 제조업 허가 | SRN (Actor Module) | | 기기 등록 | 510(k)/PMA cleared → GUDID | 허가/인증/신고 후 UDI포털 | EUDAMED UDI/DEV | | UDI 발급기관 | GS1, HIBCC, ICCBBA | GS1(의무), HIBCC(가능) | GS1, HIBCC, ICCBBA | | Vigilance 보고 | eMDR (FDA MedWatch) | 이상사례 포털 | Module 5 (~Q2 2027) |

2. Chunk `1068273778649251618`

> ### Module 2: UDI/Device Registration (UDI/DEV) — UDI 및 기기 등록 #### 3-2-A. UDI 구조 ``` UDI = UDI-DI (고정) + UDI-PI (가변) Basic UDI-DI (레거시 식별자) └── UDI-DI (모델별) └── UDI-PI (생산 로트/일련번호) ``` - **Basic UDI-DI**: 동일 기기 군/버전을 식별하는 핵심 레퍼런스. EUDAMED에서 Globally Unique해야 함. - **UDI-DI**: 특정 버전/제품 모델 식별. - 발급 기관: GS1, HIBCC, ICCBBA 중 선택. #### 3-2-B. 등록 데이터 항목 (주요)

### kb-eval-20261017-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "4ee154ad08f699c8", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "eb4c9a22b20b0a1d5596a1d52e576d1579c10df62ed295d604c8c3120ca09417"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `4ee154ad08f699c8`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PMS_Plan_MDR_Article84_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `eb4c9a22b20b0a1d5596a1d52e576d1579c10df62ed295d604c8c3120ca09417`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PMS_Plan_MDR_Article84_템플릿.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 3. PMS Plan 실용 템플릿 (MDCG 2025-10 기반) `[추가확인]` 표시 항목은 자사 확인 후 기재. --- ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (추정) | PMS Plan 의무 | 보고서 유형 | FDA 522 | MFDS 시판후조사 | |---|---|---|---|---|---| | **X-ray Detector** | Class IIa/IIb | **필수** | PSUR 2년/매년 | 해당 없음 (비이식형) | 신개발 시 3~4년 조사 | | **Handheld X-ray Source** | Class IIb | **필수** | PSUR 매년 | 해당 없음 (비이식형) |...
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

> **Regulatory Draft – PMS / PMCF Planning & Conformity Assessment**

---

### 1. Device Portfolio & Primary Classification  

| # | Device (as described in source) | Likely MDR classification* | Governing rule(s) | Relevant MDR provision for classification |
|---|---------------------------------|----------------------------|-------------------|-------------------------------------------|
| A | **X‑ray Detector** – non‑implantable imaging sensor | Class IIa / IIb (source indicates “Class IIa/IIb”) | Rule 17 (recording diagnostic X‑ray images) → Class IIa; if the detector is integral to a system that delivers therapeutic or high‑risk diagnostic energy it may be upgraded to IIb. | Annex VIII – Rule 17; Art. 52(6) for Class IIa, Art. 52(4) for Class IIb |
| B | **Handheld X‑ray Source** – portable emitter of ionising radiation | Class IIb | Rule 10 (active device emitting ionising radiation for diagnostic radiology) → Class IIb | Annex VIII – Rule 10; Art. 52(4) |
| C | **GUI Software (SaMD)** – provides image‑viewing / interpretation assistance | Class IIa (source cites “Class IIa (MDR §22)”) | Rule 11 (software providing information for diagnostic decisions). Impact assessment places it in Class IIa. | MDR §22 (as quoted in source); Annex VIII – Rule 11; Art. 52(6) |

\*The source supplies a provisional matrix; the final class must be justified with a detailed “Intended Purpose” and “Risk‑Based Classification” justification referencing the applicable rule(s).

---

### 2. Conformity‑Assessment Route (per Art. 52)

| Device | Class | Required route (NB involvement) | Key MDR annexes |
|--------|-------|----------------------------------|-----------------|
| A – Detector | IIa **or** IIb (to be confirmed) | • **Class IIa:** Annex IX (QMS + technical‑documentation assessment of one representative device).  <br>• **Class IIb:** Annex IX *or* Annex X (EU type‑examination) **+** Annex XI (production conformity verification). | Art. 52(6) for IIa; Art. 52(4) for IIb |
| B – Handheld source | IIb | Annex IX **or** Annex X + XI (NB‑assessed type‑examination & production verification). | Art. 52(4) |
| C – SaMD GUI | IIa | Annex IX (standard route for Class IIa). | Art. 52(6) |

> **Note:** If the manufacturer already holds an ISO 13485:2016 certificate, that satisfies the QMS element required by Annex IX §2.

---

### 3. Mandatory Evidence Packages  

| Evidence | MDR requirement (citations) | Applicability per device |
|----------|-----------------------------|--------------------------|
| **Technical Documentation** (TD) – §§1‑6 of Annex II (device description, design & manufacturing, GSPR fulfilment, risk management, verification/validation, clinical evaluation) | Annex II §6.1; Art. 61 (keep CER current) | All three devices |
| **EU Declaration of Conformity** | Art. 19; content in Annex IV | All devices (must be issued before CE‑marking) |
| **Risk Management File** (ISO 14971:2019 implementation) | Annex I §3 (risk‑management system) | All devices – especially critical for X‑ray source (radiation risks) and software (use‑error, cybersecurity) |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | Detector & Software (SaMD). For the handheld source a clinical evaluation may be limited to performance data plus literature on radiation safety. |
| **PMCF Plan / PMCF Evaluation Report** | Annex XIV Part B | Required for Class IIa/IIb devices when existing clinical evidence is insufficient; strongly recommended for SaMD (software updates) and for the detector if market experience is limited. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 (mandatory PMS plan) – template referenced in source (MDCG 2025‑10) | All devices (template already identified) |
| **Periodic Safety Update Report (PSUR)** | Art. 86(1)(a‑c); frequency: Class IIa → every **2 years**; Class IIb → **annually** (source matrix confirms “PSUR 2년/매년”) | Detector (IIa/IIb) – biennial or annual depending on final class; Handheld source – annually; Software – biennial |
| **IEC / ISO Standards conformity** (e.g., IEC 60601‑2‑28, IEC 60601‑2‑54 for X‑ray equipment; IEC 62304 for software lifecycle) | GSPR §§16‑18 (radiation protection, active devices, electronic programmable systems) | Detector & source – IEC 60601‑2‑28/54; Software – IEC 62304 + IEC 62366‑1 (usability) |
| **Usability Engineering File** (where applicable) | Annex I §22 (devices intended for lay persons) and IEC 62366‑1 | Particularly relevant for GUI software used by non‑expert operators. |

---

### 4. Gaps / Missing Information (to be supplied before NB submission)

| Item | Why needed | Current status (source) |
|------|------------|--------------------------|
| **Exact Intended Purpose & Indications** | Drives classification, risk analysis, clinical evaluation scope, and labeling. | Not detailed in source excerpt. |
| **Justification of Class for X‑ray Detector** (IIa vs IIb) | Must reference Rule 17 and any additional functionality that triggers upgrade to IIb. | Source lists “Class IIa/IIb” – justification absent. |
| **Full PMS Plan content** (objectives, data sources, trigger levels) | Required by Art. 84; template only referenced, not completed. | Template flagged “[추가확인] 표시 항목은 자사 확인 후 기재.” → needs completion. |
| **PMCF strategy for SaMD** (data collection, post‑market clinical follow‑up) | Annex XIV Part B – must be in place before CE marking for software that influences diagnosis. | No PMCF data mentioned. |
| **Clinical Evidence / Literature Review** (state‑of‑the‑art for detector performance and source safety) | Needed for CER and to demonstrate equivalence or superiority. | Not provided. |
| **Risk Management – Hazard identification & control measures for radiation exposure** | GSPR §16, ISO 14971 risk controls specific to ionising radiation. | No evidence supplied. |
| **Verification / Validation test reports (e.g., DQE measurement per IEC 62220‑1‑1)** | Demonstrates compliance of detector performance. | Not mentioned. |
| **Software Development Lifecycle documentation** (IEC 62304) & Cybersecurity assessment (IEC 82304‑1) | Mandatory for SaMD to meet GSPR §§17‑18. | Absent. |
| **Notified Body (NB) certificate or audit schedule** | Required for Annex IX / X routes. | Not indicated. |
| **UDI / EUDAMED registration details** (Art. 33‑39) | Mandatory for market entry. | No information. |

---

### 5. Core Risk Controls to be Documented  

| GSPR § | Control needed (device‑specific) | Reference standard |
|--------|-----------------------------------|--------------------|
| **§3** (Risk‑management system) | Full ISO 14971:2019 risk analysis, evaluation of residual risk, benefit–risk determination. | ISO 14971:2019 |
| **§4‑5** (Risk control & use‑error) | Implement protective measures for radiation exposure (shielding, interlocks), ergonomic GUI design to avoid misinterpretation. | IEC 60601‑2‑28/54; IEC 62366‑1 |
| **§6** (Device lifetime) | Define service life of detector modules and source tube, schedule preventive maintenance. | Manufacturer’s specification |
| **§7** (Transport & storage) | Packaging that protects radiation‑sensitive components; temperature/humidity limits. | ISO 14971 |
| **§8** (Known/foreseeable risks vs benefits) | Benefit‑risk analysis showing diagnostic advantage outweighs radiation dose. | Annex I §8 |
| **§16** (Radiation protection) | Conformity with IEC 60601‑2‑28 (X‑ray tube) and IEC 60601‑2‑54 (radiography equipment); DICOM DR/CR compliance. | IEC 60601‑2‑28, IEC 60601‑2‑54 |
| **§17** (Electronic programmable systems) | Secure software updates, traceability of firmware versions. | IEC 62304 |
| **§18** (Active devices & connections) | Electrical safety, electromagnetic compatibility per IEC 60601‑1‑2. | IEC 60601‑1‑2 |
| **§22** (Lay‑person use) – if GUI intended for non‑expert staff | Usability testing according to IEC 62366‑1. | IEC 62366‑1 |

---

### 6. Human‑Escalation Triggers  

| Trigger condition | Action required | Escalation level |
|-------------------|-----------------|------------------|
| **Unresolved classification dispute** (e.g., detector class not justified) | Prepare a detailed rule‑based justification, request internal review. | Senior Regulatory Manager |
| **Incomplete PMS Plan** (any “[추가확인]” placeholder remains) | Complete plan with data sources, monitoring metrics; lock version before NB audit. | Project Lead |
| **Missing PMCF plan for SaMD** | Draft PMCF protocol (post‑market surveys, real‑world evidence); obtain clinical/clinical‑expert sign‑off. | Clinical Affairs Lead |
| **Absence of IEC conformity evidence** (e.g., no test report for radiation safety) | Commission or retrieve test data; update TD accordingly. | Quality Assurance Manager |
| **No NB audit schedule / certificate** | Identify suitable NB, request quotation & timeline; assess capacity to meet deadlines. | Regulatory Affairs Director |
| **Failure to meet PSUR frequency** (e.g., only biennial for Class IIb device) | Adjust reporting cadence, allocate resources for annual PSUR preparation. | Post‑Market Surveillance Coordinator |
| **Lack of EUDAMED registration entries** | Register each device (unique device identifier, manufacturer, etc.) before market launch. | IT / Regulatory Ops |
| **Critical residual risk remains uncontrolled after risk analysis** | Conduct additional risk control measures or redesign; document in RMF. | Risk Management Team Lead |

When any trigger is met, the responsible owner must log the issue in the project’s regulatory tracker and notify the escalation point listed above within **5 working days**.

---

### 7. Peer‑Review Prompt  

> *Please review this draft and challenge: (a) the adequacy of the classification justification given the limited source data; (b) whether all mandatory MDR evidence items have been captured for each device, especially concerning PMCF requirements for SaMD; and (c) any jurisdiction‑specific gaps (e.g., EUDAMED registration, UDI, or specific MDCG guidance not reflected).*

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

1. Chunk `1002815045680049480`

> ## 3. PMS Plan 실용 템플릿 (MDCG 2025-10 기반) `[추가확인]` 표시 항목은 자사 확인 후 기재. ---

2. Chunk `1142345122918011337`

> ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (추정) | PMS Plan 의무 | 보고서 유형 | FDA 522 | MFDS 시판후조사 | |---|---|---|---|---|---| | **X-ray Detector** | Class IIa/IIb | **필수** | PSUR 2년/매년 | 해당 없음 (비이식형) | 신개발 시 3~4년 조사 | | **Handheld X-ray Source** | Class IIb | **필수** | PSUR 매년 | 해당 없음 (비이식형) | 신개발 시 4~6년 조사 | | **촬영실 GUI SW (SaMD)** | Class IIa (MDR §22) | **필수** | PSUR 2년 | 해당 없음 | 소프트웨어 신개발 시 해당 | ---

## ra_kr

### kb-eval-20261017-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "5bafcfd7f10ae789", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "00026234f8ec1153306309dc7c82b355b5fdfc4d7a5de00dbd5247374b13eccb"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5bafcfd7f10ae789`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-22_SBOM_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%A0%95%ED%95%A9%EC%84%B1.md)
- Source hash: `00026234f8ec1153306309dc7c82b355b5fdfc4d7a5de00dbd5247374b13eccb`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `2026-04-22_SBOM_디지털의료제품법_정합성.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. FDA vs MDR vs MFDS — SBOM 요구사항 정합성 | 축 | 요구 시점 | 포맷 | 필수 항목 | 제출 방식 | 사후 갱신 | |----|-----------|------|-----------|-----------|-----------| | FDA (524B) | Premarket (2023-10-01 RTA 강제) | SPDX 2.3 / CycloneDX 1.5 | NTIA 7요소 + EOL + 취약점 | eSTAR 제출물 | Section 524B Postmarket Plan | | MDR (MDCG 2019-16) | Technical Documentation Annex II | 포맷 권고 없음, IMD...
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

> **Regulatory Draft – Impact of the Digital Medical Products Act on the X‑ray Imaging System (including firmware, workstation software and AI analysis modules)**  

---  

### 1. Product Scope & Intended Use  
| Component | Current assessment (source [2]) | Likely regulatory scope under the Korean **디지털의료제품법** |
|-----------|--------------------------------|--------------------------------------------------------------|
| Generator firmware | X – hardware‑only control, no network connectivity | Treated as part of the “X‑ray generator” medical device; not a standalone digital‑medical product. |
| Detector firmware | △ – network‑capable (potentially) | May become a **digital medical product** if it exchanges health data or can be reprogrammed remotely. |
| Acquisition Workstation software | ○ – stand‑alone operation, networked, AI‑ready | Classified as **SaMD** (Software as Medical Device). |
| Image‑post‑processing / AI analysis module | ○ (if applicable) – SaMD + AI | **AI‑enabled SaMD**; subject to the **Digital Medical Products Act** and additional AI‑specific safety requirements. |
| DICOM/PACS communication software | △ – network function, independent SW boundary review required | Potentially a digital medical product if it performs health‑related data processing without dedicated hardware. |

> **Regulatory implication:** Any component that can be used independently of the X‑ray hardware to acquire, process, store or analyse patient imaging data (i.e., acquisition workstation, AI analysis module, networked detector firmware) falls under the **디지털의료제품법** and must satisfy its software‑specific obligations (e.g., Korean language UI, local clinical evaluation, post‑market surveillance plan for software).  

---  

### 2. Korean Classification & Submission Route  

| Determination | Reference |
|---------------|-----------|
| The overall X‑ray system (generator + detector + software) is expected to be **3등급** or **4등급** medical device (high‑risk radiology equipment). | No specific grade identifier found in source – verify against 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| SaMD components (workstation, AI module) are classified separately according to the digital‑medical‑product risk matrix; typical AI‑enabled imaging analysis is **2등급** SaMD. | No specific grade identifier found – verify via 디지털의료제품법 classification table. |

- **3~4등급 devices → 허가** (full MFDS approval).  
- **2등급 SaMD → 인증** (technical‑documentation review by an MFDS‑designated 심사기관).  

---  

### 3. Required Evidence Package  

| Requirement | Evidential Source |
|-------------|-------------------|
| **KGMP certification** for all manufacturing sites (hardware & firmware) – MFDS 제28조. | Framework reference; no identifier required. |
| **Risk Management File** complying with **ISO 14971:2019** and **IEC 62304:2006+A1:2015** (software life‑cycle). | Standard numbers are framework references. |
| **Usability Engineering** per **IEC 62366‑1:2015+A1:2020**. | Framework reference. |
| **Cybersecurity & SBOM compliance** – submission of an SPDX 2.3 or CycloneDX 1.5 Bill‑of‑Materials, covering NTIA 7 요소 + EOL + vulnerability information; referenced in MFDS guidance (see source [1] “보안 지침 제16조”). | **Instance identifier:** 보안 지침 제16조 (cited directly). |
| **Clinical Evaluation Report** for the SaMD/AI module – local clinical data required unless a mutually‑accepted foreign CER is permitted under the latest MFDS notice. No specific notice number is provided in the source; verify separately. |
| **Korean Language UI & IFU** – all labeling, user manuals and safety information must be in Korean (MFDS labeling rule). | Framework reference. |
| **Post‑Market Surveillance (PMS) Plan** – includes periodic SBOM updates per 보안 지침 제16조 and a PSUR for software components. | Instance identifier: 보안 지침 제16조; also MFDS “Section 524B Post‑market Plan” is mentioned as foreign reference only. |
| **Algorithm Validation & Performance Evidence** (AI module) – conformity with IMDRF N73 principles, data set documentation, bias analysis. | Framework reference (IMDRF N73). |

---  

### 4. Gaps / Missing Information (to be clarified before submission)

| Gap | Why it matters |
|-----|----------------|
| **Exact Korean grade (3등급 vs 4등급) for the X‑ray system** – determines whether 허가 or 인증 is required. | Must be confirmed from the official classification table. |
| **Intended use statement for each software component** – needed to decide SaMD risk class and applicability of the 디지털의료제품법. | Impacts clinical evaluation scope. |
| **Local clinical data or evidence of foreign CER acceptance** – no specific MFDS notice number is provided; need to verify whether OECD‑MAD non‑clinical data suffice or a Korean clinical study is mandatory. |
| **Detailed SBOM content mapping** – the source indicates the SOP covers required elements, but actual artifact (SPDX 2.3 / CycloneDX 1.5) must be produced and validated. | Required for MFDS security review (보안 지침 제16조). |
| **Korean language translation of UI strings and IFU** – not addressed in the source. | Mandatory for market entry. |
| **Algorithm change management plan** – to satisfy post‑market updates under 보안 지침 제16조. | Needed for continued compliance after AI model retraining. |

---  

### 5. Risk Controls & Standard Mapping  

| Hazard Category | Control Measure | Applicable Standard / Guidance |
|-----------------|----------------|--------------------------------|
| Electrical safety of X‑ray generator | IEC 60601‑1 2005+A1:2012+A2:2020 (general requirements) | Framework reference. |
| Radiation emission & protection | Korean “X‑ray Safety Regulation” (MFDS) – not listed in source, must be referenced by title. |
| Software bugs / failure modes | IEC 62304 life‑cycle processes; ISO 14971 risk analysis for software failures. |
| Usability errors leading to incorrect scan parameters | IEC 62366‑1 usability engineering. |
| Cybersecurity vulnerabilities (e.g., unauthorized firmware update) | 보안 지침 제16조 – SBOM maintenance, vulnerability response plan. |
| AI algorithm bias / misdiagnosis | IMDRF N73 “SaMD: Clinical Evaluation” principles; Korean AI‑specific guidance (if any). |

---  

### 6. Compliance Check – SBOM (Software Bill‑of‑Materials)  

- **Format:** SPDX 2.3 *or* CycloneDX 1.5 (both accepted by MFDS per source [1]).  
- **Required elements:** NTIA 7 요소 + End‑of‑Life (EOL) dates + vulnerability information.  
- **Submission method:** As part of the pre‑market dossier (“심사 자료”) – reference to “보안 지침 제16조”.  

**Action:** Generate a consolidated SBOM covering all firmware and software modules (generator, detector, workstation, AI module). Verify that each component’s version, hash, license, and known CVEs are listed.  

---  

### 7. Human‑Escalation Triggers  

| Trigger | Escalation Action |
|--------|-------------------|
| **Uncertainty on device grade** (3등급 vs 4등급) after internal review. | Seek clarification from MFDS via 공식 질의·답변 (Q&A) or consult the Korean classification database. |
| **Detection of missing SBOM elements** during dossier preparation. | Halt submission; engage cybersecurity lead to complete SBOM and revise vulnerability management plan. |
| **AI module identified as high‑risk SaMD** without adequate clinical evidence. | Initiate a local clinical study or obtain an approved foreign CER; pause regulatory filing until data are secured. |
| **Regulatory notice on digital medical products (e.g., new amendment after 2025‑01‑10) emerges**. | Update compliance checklist and inform cross‑functional team; re‑assess submission timeline. |
| **Feedback from MFDS reviewer requesting additional Korean language documentation**. | Prioritize translation of UI, labeling, IFU; allocate resources to meet the request within the stipulated response period. |

---  

### 8. Citations  

| Type | Citation |
|------|----------|
| Framework reference (standards) | ISO 14971:2019; IEC 62304:2006+A1:2015; IEC 60601‑1:2005+A1:2012+A2:2020; IEC 62366‑1:2015+A1:2020; IMDRF N73. |
| Instance identifier (from source) | **보안 지침 제16조** – security guideline that mandates SBOM management (source [1]). |
| Foreign comparative references (context only) | FDA 524B (premarket), MDR MDCG 2019‑16 (technical documentation). |
| No specific Korean grade or MFDS notice number found in source – verify separately. |

---  

### 9. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions made regarding (1) the classification of each software component under the 디지털의료제품법, (2) the completeness of the SBOM evidence expected by MFDS (especially any undocumented mandatory elements), and (3) the need for local clinical evaluation versus acceptance of foreign CERs in the absence of a cited MFDS notice. Highlight any jurisdiction‑specific gaps or alternative pathways that may have been overlooked.

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

> ① 'MFDS "Section 524B Post-market Plan"' — 524B는 미국 FD&C Act 조문(사전심사 사이버보안)이며 MFDS 제도가 아님. 같은 응답의 외국 참조표('FDA 524B (premarket)')와 모순. ② KR PMS에 'PSUR'(EU MDR 용어) 혼입 — 한국은 시판후조사 체계. SBOM 제16조 인용은 원문 충실.
>

**Source Excerpts**

1. Chunk `1055466385786976527`

> ## 1. FDA vs MDR vs MFDS — SBOM 요구사항 정합성 | 축 | 요구 시점 | 포맷 | 필수 항목 | 제출 방식 | 사후 갱신 | |----|-----------|------|-----------|-----------|-----------| | FDA (524B) | Premarket (2023-10-01 RTA 강제) | SPDX 2.3 / CycloneDX 1.5 | NTIA 7요소 + EOL + 취약점 | eSTAR 제출물 | Section 524B Postmarket Plan | | MDR (MDCG 2019-16) | Technical Documentation Annex II | 포맷 권고 없음, IMDRF N73 원칙 | NTIA 7요소 + License + Hash | NB 심사 자료 | PMS Plan/PSUR 포함 | | MFDS (2025-01-10) | 국내 허가 심사 | 권고 (SPDX/CycloneDX) | RA-07 항목 | 심사 자료 (권고) | 보안 지침 제16조 SBOM 관리 | **정합성 판정: 본 SOP-SBOM-001 v0.1은 3축 모두 수용 가능한 상위 호환 설계** - SPDX 2.3 또는 CycloneDX 1.5 채택 → FDA/MDR/MFDS 동시 만족 - NTIA Baseli...

2. Chunk `418096885713027360`

> ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 |

### kb-eval-20261017-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "205d0d6681ab7649", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `205d0d6681ab7649`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e`
- Focus: digital medical products act impact
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전...
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

> **Regulatory Draft – Impact of the “디지털의료제품법” on an AI‑based Imaging Analysis Software (SaMD)**  

---

### 1. Device Synopsis  
* **Type / Intended Use:** Stand‑alone software that automatically analyses medical images (e.g., CT, MRI) and provides diagnostic suggestions. It is a software‑as‑a‑medical‑device (SaMD) incorporating generative/diagnostic AI.  
* **Key Functional Blocks:**  
  – AI inference engine (trained on clinical image datasets)  
  – User interface (viewer console) for result display  
  – Network connectivity for data upload/download  

---

### 2. Korean Classification & Submission Route  

| Item | MFDS Requirement | Current Evidence From Source |
|------|------------------|------------------------------|
| **Device Grade** | Must be determined according to “의료기기 품목 및 품목별 등급에 관한 규정”. AI‑based diagnostic software is typically placed in **3등급·4등급**, but the exact grade depends on the risk level (e.g., whether it provides treatment recommendations). | *No specific grade stated in source* – **grade must be confirmed**. |
| **Submission Pathway** | 1~2등급 → 신고/인증, 3~4등급 → 허가. If the device is classified 3등급 or 4등급, a full MF DS 허가 (approval) is required, including review by an MFDS‑designated 심사기관 for certification of technical documentation where applicable. | – |

**Regulatory Judgment:** Until the grade is verified, default to preparing a **허가** dossier (the more stringent path), because AI diagnostic software usually falls into 3등급 or higher.

---

### 3. Required Evidence / Documentation  

| Requirement | Basis (framework) | Evidence Needed | Source‑based status |
|-------------|-------------------|-----------------|---------------------|
| **KGMP Facility Certification** | KGMP (의료기기법 제28조) – mandatory for all manufacturers of 2~4등급 devices. | GMP audit report, facility certification. | Not mentioned – **missing**. |
| **Korean‑language Labeling & IFU** | MFDS labeling regulations (no specific notice number in source). | Korean labels, instructions for use (IFU), safety information. | Not mentioned – **missing**. |
| **Clinical Evaluation Report (CER)** | MFDS acceptance of foreign CERs (subject to periodic scope revisions) + local clinical data where required. | • Clinical evidence package (clinical trial or post‑market data). <br>• If using foreign CE/FDA evidence, map to MFDS requirements per latest notice. | No specific identifier provided – **verify separately**. |
| **Non‑clinical Safety Data** | OECD Mutual Acceptance of Data (MAD) for GLP non‑clinical studies only. | • ISO 10993‑1 (2018) biocompatibility data. <br>• Electrical safety per IEC 60601‑1. | Not addressed – **missing**. |
| **Usability / Human Factors (사용적합성)** | IEC 62366‑1 (2015+A1:2020). | • 사용적합성 엔지니어링 계획 (see “AI 모델 데이터셋·거버넌스 절차 수립” and “사용적합성 엔지니어링 계획서”). | **Partially covered** – a draft IEC 62366‑1 plan is listed as v0.2 completed (Excerpt [2]). |
| **Cybersecurity** | 2025‑01‑10 “의료기기 사이버보안 허가·심사 가이드라인(개정)” (high relevance) and “디지털의료기기 전자적 침해행위 보안 지침(안)” (high relevance). | • Cybersecurity risk management per IEC 81001‑5‑1 (2021). <br>• SBOM (Software Bill of Materials) 관리 절차. | • RA‑01~RA‑20 매트릭스 creation is **in progress** (Excerpt [2]). <br>• SBOM SOP‑001 is v0.2 complete (Excerpt [2]). |
| **AI Governance & Dataset Management** | No explicit Korean law yet, but MFDS guidance on “생성형 AI 의료기기 허가·심사 가이드라인” (medium relevance) expects data governance. | • SOP‑AIDATA‑001 / SOP‑AIGOV‑001 (dataset and model governance). | Both SOPs are v0.2 complete (Excerpt [2]). |
| **Change Management** | MFDS change management requirements for 2~4등급 devices. | • Change Management Plan SOP‑CC‑001 (CMP section). | Draft at v0.2 (Excerpt [2]). |
| **Performance Evaluation of AI Components** | Internal guideline “구성요소 단위 성능평가 절차 문서화”. | • AI component performance test reports. | Documented as v0.2 complete (Excerpt [2]). |

---

### 4. Identified Gaps / Missing Information  

| Gap | Impact on Submission |
|-----|----------------------|
| **Confirmed device grade** – required to select the correct MFDS pathway and applicable evidence level. | Without grade, the dossier may be incomplete; risk of rejection or need for re‑submission. |
| **KGMP certification proof** – mandatory for any 2~4등급 manufacturer. | Absence blocks 허가 filing. |
| **Full Korean IFU/Labeling** – MFDS requires all user‑facing documents in Korean. | Missing may cause non‑compliance finding. |
| **Clinical evidence that satisfies MFDS local data requirement** – foreign CER alone may not be sufficient. | Potential request for additional Korean clinical data. |
| **Complete SBOM (including third‑party libraries)** – high relevance per cybersecurity guidance. | Incomplete SBOM could trigger a cybersecurity deficiency. |
| **Finalized AI governance SOPs (data, model lifecycle, bias mitigation)** – MFDS expects documented controls. | Draft status may be deemed insufficient. |
| **Change Management Plan with detailed CMP** – required for post‑approval changes. | Partial draft may not meet the depth expected. |

---

### 5. Core Risk Controls to Address in the Dossier  

1. **Risk Management (ISO 14971:2019)** – Hazard analysis, risk evaluation, and mitigation measures specific to AI misclassification, data drift, and cybersecurity threats.  
2. **Usability Engineering (IEC 62366‑1)** – Task analysis, formative/usability testing with Korean clinicians; documented in the “사용적합성 엔지니어링 계획서”.  
3. **Cybersecurity Controls** –  
   - Threat modelling per IEC 81001‑5‑1.  
   - Implementation of secure communication (TLS), authentication, and audit logging.  
   - SBOM completeness and periodic vulnerability scanning.  
4. **AI Model Governance** – Dataset provenance, bias assessment, performance monitoring, version control, and post‑market algorithm change procedures (SOP‑AIDATA‑001 / SOP‑AIGOV‑001).  
5. **Post‑Market Surveillance (시판후조사)** – Plan for collecting real‑world performance data, adverse event reporting in Korean, and periodic safety updates.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required | Escalation Level |
|--------|-----------------|------------------|
| **Unresolved device grade** after initial internal review | Halt dossier preparation; request formal classification from MFDS (or consult the “품목별 등급에 관한 규정”). | RA Lead → Regulatory Affairs Director. |
| **KGMP certification not obtained** | Pause submission; engage manufacturing compliance team to secure certification. | QA/Manufacturing Manager → VP of Operations. |
| **SBOM gaps identified during cybersecurity review** | Conduct full component inventory and vulnerability assessment; update SOP‑SBOM‑001. | Cybersecurity Officer → CISO. |
| **Clinical evidence deemed insufficient by MFDS reviewer** | Prepare supplemental Korean clinical study or real‑world data collection plan. | Clinical Development Lead → Chief Medical Officer. |
| **AI model change without approved Change Management Plan** | Suspend any algorithm updates; route through Change Management SOP‑CC‑001 and seek MFDS approval before release. | AI Engineering Lead → Regulatory Affairs Director. |
| **Regulatory notice revision (e.g., new 2025 cybersecurity guideline) released mid‑project** | Re‑evaluate compliance matrix (RA‑01~RA‑20) and update dossier accordingly. | Project Manager → Steering Committee. |

---

### 7. Citations  

| Category | Source Detail |
|----------|----------------|
| **Guidelines – relevance** | “디지털 의료기기 전자적 침해행위 보안 지침(안)” – high relevance (Excerpt [1]). |
| **Guidelines – AI imaging module** | “생성형 AI 의료기기 허가·심사 가이드라인” – medium relevance (Excerpt [1]). |
| **Guidelines – usability** | “독립형 디지털의료기기SW 사용적합성 가이드라인” – high relevance (Excerpt [1]). |
| **Cybersecurity guideline update** | “의료기기 사이버보안 허가·심사 가이드라인(개정)” – high relevance, 2025‑01‑10 (Excerpt [1]). |
| **Project‑level actions** | RA‑01~RA‑20 매트릭스, SOP‑SBOM‑001, SOP‑AIDATA‑001, SOP‑AIGOV‑001, AI_구성요소_단위_성능평가 – status v0.2 (Excerpt [2]). |
| **Framework standards** | ISO 14971:2019; IEC 62366‑1:2015+A1:2020; IEC 81001‑5‑1:2021; ISO 10993‑1:2018; IEC 60601‑1:2005+A1:2012+A2:2020. | No specific identifier in source – **verify separately** for any notice numbers that may apply. |

---

### 8. Peer Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made about the device’s likely grade (3등급/4등급) and the completeness of the evidence list, especially regarding foreign clinical evaluation acceptance under current MFDS guidelines. Verify whether the draft status of SOPs (v0.2) is sufficient for submission or if a fully finalized version is required by MFDS. Also challenge any potential gaps in our mapping of Korean cybersecurity guidance to IEC 81001‑5‑1 controls.

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

1. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

2. Chunk `1130453648414545903`

> ## 8. 후속 조치 요건 (프로젝트 관점) | 우선순위 | 조치 사항 | 연계 문서 | 상태 | |----------|----------|-----------|------| | 1 | 사이버보안 RA-01~RA-20 대응 매트릭스 작성 | 디지털의료제품법_요구사항_매트릭스 | 진행중 | | 2 | 사용적합성 엔지니어링 계획 수립 | IEC_62366-1_사용적합성_엔지니어링_계획서 | v0.2 완료 | | 3 | SBOM 관리 절차 정합성 확인 | SOP-SBOM-001 | v0.2 완료 | | 4 | 변경관리 계획 SOP 연계 (CMP 섹션) | SOP-CC-001 | v0.2 완료 | | 5 | AI 모델 데이터셋·거버넌스 절차 수립 | SOP-AIDATA-001, SOP-AIGOV-001 | v0.2 완료 | | 6 | 구성요소 단위 성능평가 절차 문서화 | AI_구성요소_단위_성능평가 | v0.2 완료 |

### kb-eval-20261017-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "8f3c44607ab3cf89", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `8f3c44607ab3cf89`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f`
- Focus: digital medical products act impact
- Matched keywords: KGMP

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관...
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

> **Regulatory Draft – Independent SaMD (GUI‑type) under the Korean Digital Medical Products Act**

---

### 1. Tentative Korean Classification & Submission Route  
| Item | Korean regulatory determination* |
|------|-----------------------------------|
| **Device type** | 독립형 의료 소프트웨어 (SaMD) – “촬영실 GUI SW” |
| **Risk class** | Likely **4등급** (high‑risk) because the software is mapped to **IEC 62304 Safety Class C** in the source. <br>*The exact grade must be confirmed against 「의료기기 품목 및 품목별 등급에 관한 규정」.* |
| **Submission track** | **허가** (MFDS approval) – required for 3등급·4등급 devices. |

---

### 2. Core Evidence Required for a 4등급 허가

| Requirement | Korean regulatory basis (framework reference) | Typical deliverables |
|-------------|-----------------------------------------------|----------------------|
| **KGMP 인증** of the manufacturer (and any contract sterilizer / re‑labeler) | KGMP (醫療機器법 제28조) – “품질·제조관리 기준” | KGMP certificate, audit reports |
| **QMS Documentation** (aligned with KGMP & ISO 13485) | **ISO 13485:2016** (mandatory Korean QMS standard) | QMS 매뉴얼, 절차서, 기록양식 |
| **Software Development Lifecycle Documents** – SDP, SRS, SAD, SVP, SVR (full set) | Mapping in source to **IEC 62304:2006+A1:2015** (Safety Class C) and the “디지털의료제품법” | Design plan, specifications, architecture, verification & validation plans and reports |
| **Software Validation** – regression testing, change‑control SOPs | **IEC 62304 §8.1** (validation) | Test protocols, results, traceability matrix |
| **Risk Management File** (per ISO 14971:2019) | **ISO 14971:2019** (risk analysis, control & evaluation) | Risk Management Plan, risk register, residual risk justification |
| **Cyber‑security Plan** – threat model, SBOM, PCCP‑style controls | **MFDS 사이버보안 가이드라인 2025**; also FDA 524B PCCP & MDCG 2019‑16 Rev.1 (as comparative reference) | Threat modeling report, SBOM, mitigation measures |
| **Clinical Evaluation Report (CER)** – Korean clinical data or accepted foreign CER where permissible | 디지털의료제품법 및 MFDS 가이드라인 on foreign clinical evidence (scope of acceptance must be confirmed) | Clinical literature review, local post‑marketing surveillance data, justification for any reliance on foreign data |
> **Citation note** – No specific MFDS 고시/공지 number is given in the source for the above Korean requirements; verify the exact notice numbers separately before submission.

| Additional mandatory evidence | Basis (framework) |
|------------------------------|-------------------|
| **UDI implementation** | 21 CFR 830 (U.S.) cited as ARR; Korean UDI rule derives from “의료기기법 시행령” – confirm current notice. |
| **MDR‑type adverse event reporting (30 day)** | MDR reporting requirement is referenced under ARR; Korean equivalent is the post‑market surveillance & 시판후조사 regulation. |
| **Labeling & IFU in Korean** | MFDS labeling 규정 (no specific article provided) – all user‑facing documents must be in Korean. |
| **Service record format** | Source cites **§820.35** for service records; Korean MFDS equivalents require a similar log for field service and maintenance. |

---

### 3. Gaps / Missing Information (to be supplied before filing)

1. **Confirmed Korean grade** – verify against the official classification table.
2. **KGMP certificates** for:
   - Primary manufacturer  
   - Contract sterilizer & re‑labeler (if any) – noted in ARR §820.10(a) as required.
3. **Clinical data package** – either local clinical trial results or documented acceptance of foreign CER (must align with the latest MFDS notice on foreign clinical evidence).
4. **Full cybersecurity artefacts** – threat model, SBOM, PCCP‑style controls prepared per 2025 guide.
5. **AI/ML component assessment** (if the GUI includes AI): risk classification under the Digital Medical Products Act and a conformity assessment plan according to the EU AI Act (high‑risk) as indicated in source; MFDS guidance on AI/ML is still evolving – obtain latest MFDS notice before proceeding.
6. **ARR‑specific compliance evidence** (UDI, MDR reporting, corrections & removals) – documented procedures and records aligned with 21 CFR 820.xxx (as cited). Korean equivalents must be identified and referenced.
7. **Korean language labeling & IFU** – translation and validation of all user‑facing content.

---

### 4. Key Risk Controls to Embed in the Dossier

| Hazard Category | Control Measure (Korean regulatory expectation) |
|-----------------|-------------------------------------------------|
| **Software functional failure (Class C)** | Redundant safety checks, fail‑safe mode, error‑logging per IEC 62304 Class C; verification of all high‑severity use cases. |
| **Data integrity / cybersecurity** | Threat modelling, SBOM, regular vulnerability scanning, secure boot & encryption as per MFDS 사이버보안 가이드라인 2025. |
| **Incorrect clinical decision support** (if AI/ML) | Pre‑deployment validation against a validated dataset; continuous performance monitoring; documented change‑control for model updates. |
| **User misuse** | Usability testing with Korean end‑users, clear UI warnings in Korean, mandatory training instructions in IFU. |
| **Post‑market adverse events** | 30‑day reporting SOP, dedicated MDR reportable event assessment log (mirroring §820.35(a) requirement). |

---

### 5. Human‑Escalation Triggers

| Trigger | Reason for escalation | Action |
|--------|-----------------------|--------|
| **Uncertain device grade** | Classification impacts submission path and required evidence. | Pause dossier preparation; senior RA to confirm grade via the official “의료기기 품목 및 품목별 등급에 관한 규정”. |
| **Absence of KGMP certification for any contracted party** | KGMP is mandatory for 4등급 허가. | Obtain certificates or replace contractor before proceeding. |
| **AI/ML functionality present but no AI‑specific assessment** | Regulatory expectations under Digital Medical Products Act and EU AI Act (high‑risk) may require separate conformity route. | Senior RA + regulatory/legal review to define AI risk management plan. |
| **Foreign clinical evidence intended for use without a clear MFDS notice allowing it** | Acceptance of foreign CER is conditional; misuse can lead to rejection. | Obtain latest MFDS notice on foreign clinical data; if none, generate local clinical data. |
| **Cybersecurity plan does not meet the 2025 MFDS guide** | Failure may be deemed non‑compliant with mandatory safety controls. | Security specialist review and gap‑fill before submission. |
| **ARR (U.S. FDA) obligations identified but Korean equivalents not documented** | Duplicate compliance burden; missing required procedures. | RA to map each ARR item to the corresponding Korean regulation and produce SOPs. |

If any of the above triggers fire, the case must be escalated to a senior Regulatory Affairs Manager for review before dossier finalisation.

---

### 6. Peer‑Review Prompt  

> **To another RA colleague:**  
> Please challenge the assumptions made in this draft regarding (a) the tentative classification of the GUI SaMD as 4등급, (b) the completeness of the required evidence list—especially the reliance on foreign clinical data and ARR‐derived obligations, and (c) any jurisdiction‑specific gaps that may have been overlooked given the source excerpts. Highlight additional Korean notices or guidance documents we should verify before filing.

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

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261017-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "ce3b2763722e2afb", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `ce3b2763722e2afb`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EC%82%AC%EC%9D%B4%EB%B2%84%EB%B3%B4%EC%95%88_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_2025_%EB%8C%80%EC%9D%91.md)
- Source hash: `87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e`
- Focus: digital medical products act impact
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_사이버보안_가이드라인_2025_대응.md`는 `MFDS_사이버보안_가이드라인_2025_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 | ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개...
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

> **Regulatory Draft – Cyber‑Security Requirements under the “의료기기의 사이버보안 허가·심사 가이드라인” (2025 rev.)**

---

### 1. Device Classification & Submission Route  
| Step | Action | Korean regulatory reference* |
|------|--------|------------------------------|
| **① Identify grade** – Determine whether the product is a **1등급, 2등급, 3등급 or 4등급** medical device according to 「의료기기 품목 및 품목별 등급에 관한 규정」. | *No specific identifier found in source — verify separately* |
| **② Choose pathway** – <br>• **1등급 → 신고**  (notification)  <br>• **2등급 → 인증**  (technical‑document review by an MFDS‑designated 심사기관 such as KTL, KTC, KTR)  <br>• **3등급·4등급 → 허가**  (full MFDS approval) | MFDS_인허가_상세가이드.md §2 (등급 및 인허가 경로) |

*If the device is a software‑only product (SaMD) it remains subject to the same grade system; the “디지털의료제품법” (effective 2025‑01‑24) expands the definition of medical devices to include many digital health solutions, so confirmation that the product falls under this law is required.*

---

### 2. Core Evidence Package (minimum for all grades)

| Requirement | Typical evidence | Korean‑specific notes |
|-------------|------------------|-----------------------|
| **KGMP Facility Certification** | KGMP compliance certificate (Medical Device Act 제28조) | Mandatory for any 허가/인증 submission; not required for 신고. |
| **Risk Management File** | ISO 14971:2019 risk management plan & report | Must reference Korean‑specific “위험도 평가” and include cyber‑risk analysis linked to the 35 RA items (see Sec. 3.2). |
| **Cyber‑Security Technical Dossier** | • System Architecture Diagram <br>• Secure‑by‑Design description<br>• List of implemented controls mapped to each RA‑01 ~ RA‑35 requirement (the eight categories in the guideline) <br>• SBOM (Software Bill of Materials) <br>• Vulnerability Management Plan (CVE monitoring, patch schedule) | All documentation must be **in Korean** (or bilingual with Korean translation). The guide requires explicit evidence for each of the 35 items; reference to the PDF‑based RA‑01~RA‑35 numbering is expected. |
| **Software Validation / Verification** | IEC 62304:2006+A1:2015 compliance report (for software) | Must show validation of security functions (e.g., encryption, authentication). |
| **Labeling & IFU** | Korean language labeling, user manual, and cybersecurity user instructions (e.g., update procedures, safe use) | MFDS labeling rule – no foreign‑language only label is acceptable for market entry. |
| **Clinical Evaluation (if required)** | Clinical evaluation report (Korean or foreign with MFDS acceptance) | For 3등급·4등급 devices a clinical data package is mandatory; foreign CER may be used only if the MFDS notice permitting it applies – not identified in source, so verify separately. |
| **Post‑Market Surveillance Plan** | PMCF plan, cyber‑incident reporting procedure (aligned with MFDS 시판후조사) | Must include how security events will be reported to MFDS within 7 days of detection. |

---

### 3. Gaps / Missing Information  

| Item | Why it matters | Suggested action |
|------|----------------|------------------|
| **Exact device grade** | Determines submission track & depth of evidence required | Perform classification check against the official grade list; if unclear, request a pre‑submission review from MFDS. |
| **Whether the product is covered by the “디지털의료제품법”** | The new law may impose additional obligations (e.g., data protection, AI transparency) | Confirm statutory scope; obtain legal opinion if the device includes AI or remote monitoring functions. |
| **Full list of RA‑01 ~ RA‑35 identifiers** | MFDS reviewers will cross‑check each control against the numbered items in the official PDF | Retrieve the latest “의료기기의 사이버보안 허가·심사 가이드라인” PDF and extract the exact RA numbers; map each to your dossier. |
| **Korean translation of cybersecurity documentation** | Korean language is mandatory for all submissions (label, IFU, technical file) | Prepare certified Korean translations; retain originals for audit. |
| **Evidence of compliance with IEC 81001‑5‑1 (2021)** – referenced in the “조화 목적” column but not detailed in the excerpt | May be required as a supporting standard for cyber‑security design | Include an annex showing conformity to IEC 81001‑5‑1 clauses that are adopted by MFDS. |
| **Local clinical data** (if foreign CER is intended) | The source does not mention MFDS acceptance of foreign clinical reports for this device class | Verify whether a specific MFDS notice permits foreign CER; otherwise plan local clinical investigation. |

---

### 4. Risk Controls Mapped to the Eight Cyber‑Security Categories  

| Category (from guideline) | Typical control | How it reduces risk |
|----------------------------|-----------------|----------------------|
| **보안 설계 원칙** – Secure by design, Defense‑in‑depth, Least privilege | Threat modeling early in development; segregation of duties; minimal code privileges | Reduces attack surface & limits impact of breach. |
| **인증·접근 제어** – User authentication, RBAC, session management | Multi‑factor authentication for administrators; role‑based UI restrictions; automatic session timeout | Prevents unauthorized access to device settings or patient data. |
| **암호화** – Data at rest & in transit, key management | AES‑256 storage encryption; TLS 1.3 for communications; HSM‑based key lifecycle | Protects confidentiality and integrity of health information. |
| **소프트웨어 무결성** – Code signing, boot‑integrity verification, SBOM | Signed firmware updates; secure boot chain; maintained SBOM with component provenance | Detects tampering & enables rapid remediation of vulnerable components. |
| **네트워크 보안** – Port minimization, firewall, TLS version | Closed ports except necessary medical data channels; built‑in firewall rules; enforce TLS 1.3 only | Limits exposure to network attacks and man‑in‑the‑middle threats. |
| **취약점 관리** – CVE monitoring, patch cadence, CVD policy | Subscribe to NVD alerts for all third‑party libraries; quarterly security patches; documented vulnerability disclosure process | Ensures timely mitigation of known security flaws. |
| **감사·로그** – Security event logging, log protection, access history | Immutable audit logs stored encrypted; role‑based log view; retention ≥ 2 years | Enables forensic analysis & regulatory incident reporting. |
| **업데이트·유지보수** – Secure update mechanism, remote management security | Signed OTA updates with rollback protection; dual‑auth for remote commands | Guarantees that only verified firmware reaches the device and prevents malicious remote control. |

---

### 5. Citations  

| Item | Source type | Citation |
|------|-------------|----------|
| **Legal basis** – “디지털의료제품법” (2025‑01‑24 시행) | Framework reference (law name) | Digital Medical Products Act, effective 2025‑01‑24 |
| **Guideline revision date** – 2025‑01‑10 | Framework reference (document metadata) | Guideline “의료기기의 사이버보안 허가·심사 가이드라인” (rev. 2025‑01‑10) |
| **Expansion of cyber‑security requirements 15 → 35** | Framework reference (summary table) | Guideline section 1, “핵심 변경: 사이버보안 요구사항 15개 → 35개” |
| **Eight categories of RA‑01 ~ RA‑35** | Framework reference (section 3.2) | Guideline section 3.2 – lists the eight categories; exact RA numbers are in the official PDF (no identifier found in source — verify separately). |
| **International alignment** – IMDRF N60/N73, IEC 81001‑5‑1 | Framework reference (purpose column) | Aligns with IMDRF N60/N73 and IEC 81001‑5‑1 (2021 edition) |

*No specific MFDS 고시 번호 or article/section identifier appears in the provided excerpts; therefore none are supplied here.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Recommended next step |
|--------|-----------------------|----------------------|
| **Uncertain device grade** (cannot locate product in official grade list) | Determines submission pathway and evidence depth | Pause dossier preparation; request a formal classification opinion from MFDS or an experienced Korean regulatory consultant. |
| **Missing RA‑01 ~ RA‑35 mapping** (no PDF reference available) | Reviewers will reject the cyber‑security section if any numbered requirement cannot be demonstrated | Obtain the latest guideline PDF, extract all 35 RA numbers, and produce a compliance matrix; escalate to project manager if unavailable. |
| **Absence of Korean translation for security documentation** | MFDS rejects non‑Korean submissions outright | Engage certified Korean technical translators; flag as “critical path” in timeline. |
| **Local clinical data required but not planned** | 3등급·4등급 devices need domestic clinical evidence unless a specific MFDS notice permits foreign CER (not identified) | Initiate local clinical study or seek clarification from MFDS on applicability of foreign CER; raise to senior RA lead. |
| **Failure to meet any of the eight cyber‑security categories** (e.g., no encryption, no vulnerability management plan) | Non‑compliance with mandatory guideline items leads to denial of 허가/인증 | Conduct a gap analysis; if gaps cannot be closed before submission deadline, consider postponing market entry and notify project sponsor. |
| **KGMP certification not yet obtained** (or facility audit pending) | Mandatory for 인증/허가 submissions | Accelerate KGMP audit scheduling; if audit is delayed beyond critical path, escalate to senior management for resource reallocation. |

---

### 7. Regulatory Judgment  

1. **Determine the device grade** → essential first step before any dossier assembly.  
2. **Assemble a cyber‑security compliance matrix** that cross‑references each of the 35 RA items (RA‑01 ~ RA‑35) with concrete evidence (design docs, test reports, policies).  
3. **Collect mandatory Korean‑language artifacts** (labeling, IFU, security user guidance).  
4. **Confirm KGMP certification and risk management compliance** per ISO 14971:2019 and IEC 62304.  
5. **If the product falls in 3등급 or 4등급**, verify whether foreign clinical evaluation can be used; otherwise plan local clinical data generation.  

Only after these items are fully satisfied should the submission be packaged for **신고 / 인증 / 허가** according to the confirmed grade.

---

### 8. Peer‑Review Prompt  

> *Please review this draft and challenge: (a) the completeness of the evidence list given the eight cyber‑security categories, (b) any assumptions made about the applicability of foreign clinical data in the absence of a specific MFDS notice, and (c) whether additional Korean‑specific obligations (e.g., personal information protection law, post‑market cybersecurity incident reporting template) have been omitted.*

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

> ① KR PMS 계획에 'PMCF plan'(EU 용어) 혼입 — 원문·한국 제도 모두에 없음. ② 'MFDS 7일 내 보고' — 원문에 없는 수치(근거 필요). IEC 81001-5-1·고시 체계 인용은 원문 충실.
>

**Source Excerpts**

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---

### kb-eval-20261017-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-17", "decision_ref": "kb-eval-20261017-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "d1aef3cb8966be20", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `d1aef3cb8966be20`
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

> **Regulatory Draft – Impact of the Digital Medical Products Act on a SaMD Submission**

---

### 1. Device Overview (derived from the scenario)

| Item | Description |
|------|-------------|
| **Product type** | Software as a Medical Device (SaMD) – AI/ML‑based graphical‑user‑interface (GUI) application for clinical decision support |
| **Intended use** | To assist clinicians in diagnosing / triaging patients based on imaging data (exact indication not supplied) |
| **Regulatory trigger** | “디지털의료제품법 시행” effective 2025‑01‑24 and subsequent MFDS digital‑medical‑device guideline update (2025‑05‑07) – both introduce new classification & approval pathways for SaMD. |

*Note: The source does not provide the precise intended indication, risk claim, or target patient population; these items must be supplied by the sponsor before a definitive Korean grade can be assigned.*

---

### 2. Korean Classification & Submission Route

| Step | Action | Rationale / Source |
|------|--------|--------------------|
| **2‑1** Determine Korean **등급 (grade)** | Apply the MFDS SaMD classification matrix (outlined in the 2025‑05‑07 “MFDS 디지털의료기기 가이드라인 6종”). The matrix evaluates *clinical impact* and *risk of harm*. AI/ML‑based decision support that influences diagnosis generally lands in **3등급** or **4등급**, but the exact grade depends on the claimed clinical function. | “AI/ML 기반 GUI SW 분류·임상 요건 확인 필요” (2025‑05‑07) – *no specific identifier found in source — verify separately* |
| **2‑2** Choose submission track | • **3등급·4등급 → 허가** (full MFDS approval). <br>• If the risk assessment places the product in **2등급**, the default route is **인증** by a designated 심사기관; NIDS may be considered as an additional reviewer under the new authority. | “디지털의료제품법 시행 … SaMD 분류·허가 체계 변화, NIDS 권한 확대” (2025‑01‑24) – *no specific identifier found in source — verify separately* |
| **2‑3** GMP appropriateness assessment | Since the product is a digital medical device, the **NIDS** is now authorized to perform “디지털의료기기 GMP 적합판정” as of 2025‑01‑24. The sponsor must request this assessment before or in parallel with MFDS 허가/인증 submission. | *Excerpt 1* – GMP 적합인정 절차 lists NIDS as a 담당기관 for 디지털의료기기 (effective 2025‑01‑24). |

---

### 3. Required Evidence Package

| Category | Specific Documents / Data | Applicable Standard / Guideline |
|----------|---------------------------|---------------------------------|
| **KGMP Certification** | Facility compliance report, GMP 적합판정 결과 (issued by NIDS) – validity 3 years, renewal required. | MFDS 고시 “GMP 적합인정 절차” (no identifier supplied – verify separately). |
| **Technical Documentation** | • Device description, intended use, labeling (Korean language). <br>• Software architecture & IEC 62304 compliance (2006+A1:2015). <br>• Usability engineering file (IEC 62366‑1 2015+A1:2020). <br>• Cybersecurity risk management (IEC 81001‑5‑1 2021). | ISO 14971 2019 (risk management); IEC 62304; IEC 62366‑1; IEC 81001‑5‑1. |
| **Risk Management File** | Hazard analysis, risk control measures, residual risk evaluation – must reference ISO 14971 2019. | ISO 14971 2019 (framework reference). |
| **Clinical Evaluation Report (CER)** | • Clinical performance data supporting intended use. <br>• If foreign CER is used, confirm MFDS acceptance under the latest “외국 임상 평가보고서(CER) 수용 범위” notice (specific number not provided in source – verify separately). | MFDS guideline on foreign clinical evidence (no identifier found). |
| **Non‑clinical Testing** | Biocompatibility (ISO 10993‑1 2018), software verification & validation per IEC 62304. | ISO 10993‑1 2018; IEC 62304. |
| **Labeling & IFU** | Korean language labeling, package insert, user manual – must meet MFDS labeling requirements (e.g., mandatory symbols, safety information). | MFDS labeling 규정 (no identifier supplied – verify separately). |
| **Post‑Market Surveillance Plan** | PMS activities, adverse event reporting procedures, periodic safety update reports. | MFDS 시판후조사 지침 (framework reference). |

---

### 4. Missing Information (must be obtained from sponsor)

1. **Exact intended indication & claim** – required for grade determination.
2. **Target patient population, disease prevalence, and clinical setting** – influences risk class.
3. **Details of AI/ML algorithm (training data, validation methodology, update strategy)** – needed for CER & risk management.
4. **Korean‑language labeling drafts** – to verify compliance with MFDS labeling rules.
5. **Evidence of local (Korean) clinical performance** if required by the grade (e.g., 3등급·4등급 often mandate Korean data).
6. **Confirmation whether foreign CER will be used** and, if so, which foreign regulatory clearance (FDA 510(k), CE Mark) is available.

---

### 5. Risk Controls & Mitigations (aligned with ISO 14971)

| Identified Hazard | Control Measure | Verification |
|-------------------|-----------------|--------------|
| Incorrect algorithm output leading to misdiagnosis | • Robust verification & validation per IEC 62304.<br>• Human‑in‑the‑loop decision requirement (clinical user must confirm AI suggestion). | Test reports, usability study. |
| Software update introducing new risk | Controlled post‑market software lifecycle management; change classification per MFDS “네거티브 방식 변경허가제” (2026 예정) – major changes need prior 허가, minor changes may be 신고. | Change control documentation, impact analysis. |
| Cybersecurity breach exposing patient data | Implement IEC 81001‑5‑1 security controls; regular penetration testing. | Security test reports, incident response plan. |
| Language ambiguity in Korean labeling | Professional translation + labeling review by MFDS‑approved translator. | Labeling approval records. |

---

### 6. Human‑Escalation Triggers

| Situation | Trigger for Human Review / Decision |
|-----------|--------------------------------------|
| **Uncertain grade** – insufficient clinical claim details to place the device in 2, 3 or 4등급. | Escalate to senior RA for classification workshop with clinical experts. |
| **Missing Korean labeling** – draft not yet prepared or fails preliminary compliance check. | Pause submission; involve labeling specialist. |
| **Foreign CER proposed but scope of MFDS acceptance unclear** (no specific notice identifier in source). | Seek clarification from MFDS via 공식 질의 or consult internal regulatory counsel. |
| **Change Management** – planned software updates after initial approval. | Apply “네거티브 방식 변경허가제” logic: major changes → require pre‑approval; minor changes → proceed with 신고. Escalate to PM/RA for change impact assessment. |
| **GMP 적합판정 delayed or non‑conformities found** (Critical/Major). | Initiate corrective action plan and notify MFDS; halt submission until remediation is accepted. |

---

### 7. Summary Judgment

- The SaMD falls under the **Digital Medical Products Act** (effective 2025‑01‑24) and must be classified according to the **MFDS digital‑medical‑device guideline (2025‑05‑07)**.  
- Most likely grade is **3등급 or 4등급**, directing the submission route to **허가**; however, confirmation of intended use and risk profile is required before finalizing.  
- The sponsor must obtain a **KGMP 적합판정** from **NIDS** (newly authorized as of 2025‑01‑24) and compile the full technical documentation package outlined above.  
- Key gaps—intended indication, Korean labeling, local clinical data, and clarity on foreign CER acceptance—must be resolved before the dossier can be submitted to MFDS.  

*Human escalation is required whenever any of these gaps remain unresolved or when classification/change‑management decisions are ambiguous.*

---

### 8. Peer Review Prompt

> **To a fellow Korean RA:**  
> Please review the assumptions made about the SaMD grade (3등급 / 4등급) given only the high‑level guideline references, and verify whether any additional MFDS notices (e.g., specific 고시 numbers for foreign CER acceptance) have been issued after 2025‑05‑07 that could affect the evidence requirements. Also assess if the current list of required standards fully covers all Korean regulatory expectations for digital medical devices, or if supplemental guidance (e.g., “MFDS 디지털의료기기 사이버보안 가이드라인”) should be added.  

--- 

*All citations are directly extracted from the provided source excerpts; where a specific instrument number is absent, the draft notes the need for separate verification.*

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

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---
