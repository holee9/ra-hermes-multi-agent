# KB Eval Checksheet - 2026-07-24 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260724-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "64feae2a34a29c41", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `64feae2a34a29c41`
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

> **Regulatory Draft – Evidence‑Gap Assessment for Premarket Submission**

---

### 1. Bottom‑Line Recommendation
| Device type (pending final determination) | Most likely regulatory route |
|---|---|
| **Class I–II imaging or software system** (e.g., PACS‑type processing, image storage, communication) – see 21 CFR §892.2050 etc. | **510(k) – Substantial equivalence** (predicate required). |
| **Novel Class I–II device with no appropriate predicate** | **De Novo request** (classification by FDA; clinical data “if applicable”). |
| **Class III high‑risk device** (e.g., active implantable imaging system, radiation‑emitting therapeutic) | **PMA** – full clinical investigation required. |

*Proceed with the 510(k) pathway unless a suitable predicate cannot be identified or the device introduces new technological characteristics that preclude substantial equivalence.*

---

### 2. Required Evidence per Pathway (derived from source)

| Requirement | 510(k) | De Novo | PMA |
|---|---|---|---|
| **Legal basis** | FD&C Act §510(k), 21 CFR §807 | FD&C Act §513(f)(2), 21 CFR §860 | FD&C Act §515, 21 CFR §814 |
| **Class** | Class I–II (principal) | Class I–II (new device) | Class III |
| **Predicate Device** | Mandatory | Not required | Not required |
| **Clinical Data** | Conditional – see “§3 reference” in guidance* | “If applicable” – case‑by‑case | Mandatory |
| **Review Time Goal** | 90 days | ~150 days | ~180 days |
| **eSTAR Reporting** | Required (from 2023‑10‑01) | Required (from 2025‑10‑01) | Not applicable |
| **User Fee FY 2025** | ≈ $22,171 | ≈ $46,875 | ≈ $438,330 |

*Source: Table in excerpt [2].

---

### 3. Evidence Gaps Typically Encountered (what to verify)

| Gap | Why it matters | Action needed |
|---|---|---|
| **Intended Use Statement** | Drives classification & predicate search. | Draft a concise indication/indications for use; map to FDA product code. |
| **Predicate Device Identification** | Required for 510(k). Must match intended use, technology, and performance. | Perform a thorough predicate hunt (FDA‑searchable database) and prepare a side‑by‑side comparison table. |
| **Risk Management Documentation** *(ISO 14971 / FDA risk analysis)* | Demonstrates mitigation of identified hazards; required for all classes. | Provide a Risk Management File with hazard list, severity/likelihood scoring, and control measures. |
| **Software Validation (if applicable)** | Needed for imaging processing or AI/ML modules under 21 CFR §820.30 & PCCP guidance. | Submit verification/validation reports; if AI/ML, include a Predetermined Change Control Plan (PCCP). |
| **Clinical Data Justification** | For 510(k) the FDA may still require clinical data when substantial equivalence is not evident. | Prepare a Clinical Evaluation Report (CER) with literature review and/or propose a limited clinical study; include justification for waiver if none are submitted. |
| **Quality Management System (QMSR) Compliance** | Effective 2026‑02, aligns with ISO 13485. Required for all submissions. | Provide an updated QMS audit report showing compliance with 21 CFR §820 and the new QMSR provisions. |
| **UDI Configuration** | Mandatory under 21 CFR §830 (label, packaging, GUDID). | Generate a UDI‑DI and include label artwork; ensure data are uploaded to the Global UDI Database. |
| **Labeling & IFU Content** | Must meet 21 CFR §801. | Draft labeling with intended use, warnings, contraindications, and instructions for use; include appropriate symbols for imaging devices (e.g., IEC 60601‑2‑37). |

*If any of the above items cannot be supplied at the time of submission, flag as an evidence gap.*

---

### 4. Risk Controls to Highlight in Submission

| Control | Applicable Regulation |
|---|---|
| **Design Controls** (design input, output, verification, validation) | 21 CFR §820.30 |
| **Software Lifecycle Processes** (if software‑based) | 21 CFR §820.70(i); PCCP guidance (Dec 2024). |
| **Sterility Assurance (where relevant)** | 21 CFR §820.64 |
| **Electrical Safety & EMC** (imaging equipment) | IEC 60601‑1 series; referenced in FDA guidance for radiology devices. |
| **Human Factors Engineering** | 21 CFR §820.70(g) / FDA Human Factors Guidance. |
| **Post‑Market Surveillance Plan** (including MDR reporting) | 21 CFR §803 & §806 |

---

### 5. Citations

*Framework references (facts, no verification caveat):*

- FD&C Act §§510(k), 513(f)(2), 515; 21 CFR §§807, 860, 814 – legal bases for each pathway.  
- 21 CFR §820 – Quality System Regulation (QMSR).  
- 21 CFR §830 – Unique Device Identification requirements.  
- 21 CFR §892.2050 – Class II medical image management/processing systems (if device falls there).  

*Instance identifiers directly from source excerpts:*

- Table of “Regulatory basis per pathway” (excerpt [2]) – provides class, predicate need, clinical data requirement, review time, eSTAR dates, user fee.  
- FDA guidance URLs listed in excerpt [1] (e.g., guidance‑submission‑510ks‑solid‑state‑x‑ray‑imaging‑devices) – refer to the clinical‑data decision framework.

*No specific identifier was supplied for individual risk‑control standards or UDI implementation steps; note: “no specific identifier found in source — verify separately.”*

---

### 6. Human‑Escalation Triggers

| Trigger | Reason for escalation |
|---|---|
| **Uncertain classification** (e.g., device could be Class II or III) | Require senior RA sign‑off and possibly a pre‑submission meeting with FDA. |
| **Missing predicate** after exhaustive search | Consider De Novo route; involve product development lead to assess redesign feasibility. |
| **Clinical data requirement not satisfied** (FDA likely to request) | Escalate to Clinical Affairs for study design or literature review plan. |
| **QMSR non‑compliance evidence** (audit gaps, missing procedures) | Immediate escalation to Quality Assurance manager; cannot submit without compliance. |
| **UDI/GUDID data absent** | Flag to Regulatory Operations – labeling & IT teams must deliver before submission. |
| **PCCP not prepared for AI/ML component** (if applicable) | Escalate to Software Engineering lead; FDA may reject or request a supplemental PCCP. |
| **Regulatory fee budget out of scope** | Notify Finance/Project Management for FY 2025 fee approval. |

When any trigger occurs, the responsible functional owner must be notified and a remediation plan documented before proceeding to submission compilation.

---

### 7. Peer‑Review Prompt

> **RA Peer Review Request:** Please challenge the assumptions above regarding (a) classification of the device under Part 892 versus other panels, (b) completeness of the predicate‑device search methodology, and (c) any jurisdiction‑specific gaps (e.g., state‑level registration, post‑market surveillance obligations) that may not be captured in the provided source excerpts.

--- 

*End of draft.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 15/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,921자 | — |
| 규제 식별자 인용 | 15개 | — |
| source excerpt 근거 일치 | **3/15 (20%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 12개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §892.2050`, `21 CFR §820.30`, `21 CFR §820`, `21 CFR §830`, `21 CFR §801`, `21 CFR §820.70`, `21 CFR §820.64`, `21 CFR §803`, `Part 892`
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

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20260724-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "56f0a9dd295f8e5c", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md", "source_hash": "b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `56f0a9dd295f8e5c`
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

> **Regulatory Draft – 510(k) Pathway for the (Unnamed) Medical Imaging Software System**

---

### 1. Device Overview & Intended Use  
*Brief description*: A software‑only medical image management and processing system that performs DICOM import, storage, compression, basic quantitative analysis, and export to PACS/RIS. Intended for use by radiologists in the diagnosis of adult patients.

---

### 2. Classification & Submission Route  

| Item | Determination | Rationale |
|------|---------------|-----------|
| **Regulatory class** | **Class II** (Imaging‑software) | The device falls under **21 CFR §892.2050**, which governs “Medical image management and processing systems” (class II). |
| **Premarket pathway** | Traditional 510(k) – substantial equivalence | No novel claims; functional similarity to cleared predicates enables a standard 510(k). |
| **Predicate candidates** *(example)* | • K091123 – “XYZ Image Viewer” (cleared 2020) <br>• K092345 – “ABC PACS Processor” (cleared 2021) | Both are Class II imaging‑software devices cleared under §892.2050. |

**Citations**  
- Classification rule: **21 CFR §892.2050** (class II).  
- Submission content requirements: **21 CFR §§807.92–§807.100** (traditional 510(k) contents).  

*No specific instance identifiers appear in the source material; verify predicate numbers separately.*

---

### 3. Evidence Required for a Complete 510(k)

| Requirement | Minimum Content | Supporting Standard / Guidance |
|-------------|----------------|--------------------------------|
| **Device Description** | Architecture, hardware (if any), software modules, user interface flows. | 21 CFR §807.92(b)(1). |
| **Predicate Comparison Table** | Side‑by‑side comparison of intended use, technological characteristics, performance specifications. | 21 CFR §807.91(c). |
| **Risk Management File** | Hazard analysis & risk evaluation per **ISO 14971:2019**, identification of mitigations, residual risk justification. | 21 CFR §§820.30, 21 CFR 892.2050 (risk‑based classification). |
| **Software Verification/Validation** | Unit, integration, system testing; verification of algorithms against specifications; validation using representative clinical data sets. | FDA Guidance “Design Considerations for Software Contained in Medical Devices” (Sept 2022); ISO 62304. |
| **Performance Testing** | Accuracy & precision of quantitative measurements, image distortion limits, DICOM compliance, throughput benchmarking vs. predicate. | 21 CFR §892.2050 performance expectations; FDA guidance “Medical Device Clinical Decision Support Software” (May 2023). |
| **Clinical Evaluation / Equivalence** | Literature review or limited clinical study demonstrating that the software’s output is clinically equivalent to the predicate(s). | EU MDR experience (deficiency note) indicates GSPR evidence and CE‑type clinical evaluation were insufficient – same level of rigor required for FDA. |
| **Labeling & IFU** | Intended use statement, contraindications, warnings/precautions, user training requirements. | 21 CFR §801.5. |
| **UDI Implementation Plan** | Device identifier format, labeling placement, GUDID submission plan. | **21 CFR §§830.10–830.60** (no specific subsection in source). |
| **Post‑Market Surveillance / PMCF Plan** | Ongoing performance monitoring, adverse event reporting procedures, periodic safety update schedule. | EU MDR note highlighted “PMCF 계획 미비” – FDA expects a post‑market surveillance plan consistent with 21 CFR §822.20. |
| **Predetermined Change Control Plan (PCCP)** *(if AI/ML updates anticipated)* | Description of planned algorithm modifications, justification for pre‑authorized changes, submission timeline. | Final guidance “Predetermined Change Control Plan for Artificial Intelligence/Machine Learning–Based Software as a Medical Device” (Dec 2024). |

---

### 4. Gaps Identified from Source Material  

| Gap | What the source flags | Required corrective action |
|-----|----------------------|----------------------------|
| **GSPR (General Safety & Performance Requirements) evidence** | “입증 근거 부족” – insufficient proof of compliance. | Provide detailed ISO 14971 risk file, verification/validation data, and conformance to FDA’s equivalent safety performance expectations. |
| **Clinical Evaluation / Equivalence** | “Clinical Evaluation 동등성 불충분.” | Expand predicate comparison with quantitative clinical data or literature demonstrating non‑inferiority. |
| **PMCF (Post‑Market Clinical Follow‑up) Plan** | “PMCF 계획 미비.” | Submit a post‑market surveillance plan outlining methodology, metrics, and reporting cadence. |
| **Risk Management Documentation** | “위험관리파일 ISO 14971 부적합.” | Revise risk management file to meet ISO 14971:2019 structure; include risk acceptability criteria and verification of mitigations. |

*No specific identifier (e.g., FDA AI request number) appears in the source; note for later verification.*

---

### 5. Risk Controls & Quality System Alignment  

1. **ISO 14971‑based risk management** – hazard identification, evaluation, mitigation, residual risk assessment.  
2. **ISO 13485/QMSR (21 CFR Part 820)** – documented design controls, supplier qualification, CAPA processes.  
3. **Predetermined Change Control Plan (PCCP)** – for AI/ML algorithm updates; aligns with the December 2024 FDA guidance.  
4. **Software life‑cycle (ISO 62304)** – development phases, verification/validation checkpoints, maintenance procedures.  

All controls must be traceable in the design history file (DHF) and reflected in the 510(k) submission.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required |
|--------|-----------------|
| **FDA Additional Information (AI) request** – any clause referencing “Additional Information” in the source (e.g., FDA Guidance Oct 2022). | Pause submission; convene cross‑functional team to draft a response within the FDA‑specified deadline. Escalate to RA Lead and Project Manager for resource allocation. |
| **Deficiency letter from Notified Body (NB) – GSPR, Clinical Evaluation, PMCF** | Mirror US review: treat as “FDA deficiency” – prepare corrective action plan; route to senior regulatory counsel before resubmission. |
| **Unresolved risk analysis gaps after internal audit** | Immediate escalation to Quality System Manager; halt submission until risk file is compliant with ISO 14971 and 21 CFR Part 820. |
| **Predetermined Change Control Plan not approved prior to algorithm update** | Halt software release; trigger change‑control review meeting; inform senior management of compliance breach. |

Escalations should be documented in the project’s issue‑tracking system and communicated to the sponsor within 24 hours of detection.

---

### 7. Summary Judgment  

- The product is a **Class II imaging‑software device** under **21 CFR §892.2050**; a **traditional 510(k)** is the appropriate pathway.  
- Current evidence gaps (GSPR, clinical equivalence, PMCF, risk file) must be addressed before filing to avoid FDA AI or deficiency letters.  
- Implement ISO‑aligned risk controls and a PCCP if AI/ML components are present.  

**Human‑escalation triggers** have been listed; any occurrence should invoke immediate senior‐level review.

---

### 8. Peer Review Prompt  

> **To RA peers:** Please challenge the assumptions made about predicate selection, the completeness of the identified evidence gaps, and the applicability of EU MDR deficiency themes to FDA requirements. Confirm whether additional FDA‑specific identifiers (e.g., specific AI guidance documents or MDUFA V commitment letters) are required for this submission, and flag any jurisdictional nuances that may have been missed.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 14/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,732자 | — |
| 규제 식별자 인용 | 11개 | — |
| source excerpt 근거 일치 | **1/11 (9%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 10개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §892.2050`, `K091123`, `K092345`, `21 CFR §807.92`, `21 CFR §807.91`, `ISO 62304`, `21 CFR §801.5`, `21 CFR §822.20`, `21 CFR Part 820`
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

1. Chunk `1062884112493939033`

> ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합

2. Chunk `1076622801663602202`

> > 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: https://www.fda.gov/media/73507/download (FDA Guidance: FDA and Industry Actions on 510(k) Submissions, Oct 2022) | https://medicaldeviceacademy.com/additional-information-request/ | https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process | MDUFA V Commitment Letter https://www.fda.gov/media/158308/download # FDA Additional Information (AI) 대응 전략 및 샘플 답변 체계

### kb-eval-20260724-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "d2d1345b8aac7f73", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `d2d1345b8aac7f73`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_01_Device_Description_IFU.md)
- Source hash: `70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_01_Device_Description_IFU.md`는 FDA eSTAR device description 및 IFU 작성에 필요한 제품 설명·표시 정보 문서입니다.
- 현재 excerpt 핵심: ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA For...
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

> **Regulatory Draft – Imaging‑Acquisition GUI Software (Radiology)**  

---

### 1. Classification & Submission Pathway  

| Element | Determination |
|---|---|
| **Device family** | Radiology / imaging acquisition and management software (GUI) |
| **CFR Part** | **21 CFR Part 892** (Imaging devices) – source confirms imaging devices belong here. |
| **Specific class** | Likely **Class II**, “Medical image management and processing system” – §892.2050 (per Part 892 schedule).|
| **Regulatory route** | **Traditional 510(k)** (substantial‑equivalence) using the eSTAR template (2023 revision). |
| **Predicate device** | To be identified; must match functional scope (“acquire, review, and manage digital radiographic images”) and risk profile. |

*If no suitable predicate is found, a **De Novo** submission would become necessary.*  

---

### 2. Core Submission Evidence Required (per source)

| Requirement | Source citation | Comments / evidence needed |
|---|---|---|
| **Electronic submission format** | FDA “Electronic Submission Template for Medical Device 510(k) Submissions” (eSTAR v5.x, final 2023) – no specific identifier found in source — verify separately. | Complete eSTAR‑formatted sections: Cover Letter, Indications for Use (Form 3881), Device Description, etc. |
| **Traditional/Abbreviated 510(k) format** | FDA Guidance “Format for Traditional and Abbreviated 510(k)s” (2019‑09‑13 Final). | Follow the prescribed order of sections; include Summary per §807.92. |
| **Device description** – software architecture, OS/hardware mins, DICOM node list, SOUP inventory, IEC 62304 safety class, cybersecurity features. | Section 4.3 “촬영실 GUI SW (영상 획득·검사 제어 SW)” – no specific identifier found in source — verify separately. | Provide detailed diagrams, module descriptions, versioning of compatible detectors/generators, DICOM conformance statement, security plan, and IEC 62304 classification (A/B/C). |
| **Indications for Use** (English) | FDA Guidance “General/Specific Intended Use” (1998 Final) – no specific identifier found in source — verify separately. | Use Form 3881; language must avoid diagnostic claims (“review” vs. “diagnosis”). |
| **Performance testing** (functional, safety, usability, interoperability) | Not listed in excerpt – gap identified. | • Image acquisition accuracy & timing<br>• DICOM communication validation (SCU/MPPS etc.)<br>• Usability testing with trained technologists<br>• Cybersecurity penetration test results |
| **Labeling** (Labels, IFU, UDI) | 21 CFR §801 (Labeling) – not quoted in source; flag for verification. | Include all required labeling elements, UDI per 21 CFR §830.10‑§830.60, and FDA Form 3881 content. |
| **Quality System** | 21 CFR Part 820 (QMSR) – effective Feb 2026; ISO 13485 alignment. | Evidence of a compliant QMS: design controls, risk management (ISO 14971), software development lifecycle (IEC 62304). |
| **Regulatory identifiers & submission forms** | FDA Form 3881 – no specific identifier found in source — verify separately. | Populate and attach to the 510(k). |

---

### 3. Evidentiary Gaps Identified  

| Gap | Why it matters | Suggested remedial action |
|---|---|---|
| **Predicate device** not yet selected. | Substantial‑equivalence claim hinges on a clear predicate with matching intended use and technology. | Conduct predicate search (FDA 510(k) database) for Class II imaging acquisition software; document comparability table. |
| **Performance test data** absent. | FDA requires bench, interoperability, and usability data to demonstrate safety & effectiveness. | Generate functional test protocols (e.g., DICOM conformance), conduct user‑centered usability study, compile results in the “Performance Testing” section. |
| **Usability/Human Factors** not described. | Imaging acquisition UI must be safe for trained technologists; ISO 14971 risk analysis depends on use errors. | Perform a validated formative and summative usability evaluation (per IEC 62366‑1). |
| **Cybersecurity evidence** only high‑level “features”. | §820.30(c) demands documented security controls; recent guidance stresses explicit mitigation plans. | Provide detailed Security Plan, threat analysis, and results of vulnerability assessment. |
| **SOUP inventory** lacking details (version, supplier, justification). | IEC 62304 requires traceability of off‑the‑shelf components. | Compile a SOUP list with version numbers, licensing, risk controls, and mitigation actions. |
| **UDI compliance plan** not mentioned. | §830.10‑§830.60 obligates UDI on label & packaging; GUDID entry required before market launch. | Draft UDI assignment strategy, select issuing agency, prepare GUDID submission package. |
| **QMSR (Part 820) evidence** absent. | New QMSR (effective Feb 2026) supersedes legacy 21 CFR 820 requirements; ISO 13485 alignment must be demonstrated. | Include Design History File (DHF), Device Master Record (DMR) excerpts, and audit reports confirming compliance with the updated Part 820. |
| **Predetermined Change Control Plan (PCCP)** – only relevant if AI/ML features exist. | No AI claim in excerpt; but if future updates add ML‑based image analysis, a PCCP will be mandatory per FDA Dec 2024 guidance. | Document current scope (no AI); monitor roadmap for any algorithmic changes and prepare a PCCP if required later. |

---

### 4. Risk Controls & Standards to Reference  

| Control / Standard | Application |
|---|---|
| **IEC 62304** – Software life‑cycle processes; assign safety class (A/B/C) as per software function (acquisition = Class C likely). |
| **ISO 14971** – Risk management file: hazard identification, risk analysis, evaluation, mitigation for imaging acquisition errors and cybersecurity threats. |
| **IEC 62366‑1** – Usability engineering process for UI design; include use case scenarios in the 510(k). |
| **NIST SP 800‑53 / FDA Cybersecurity Guidance (2023)** – Map to required security controls (encryption, authentication, audit logging). |
| **FDA Guidance “General/Specific Intended Use”** – Ensure language does not imply diagnostic intent; keep classification within Class II. |
| **21 CFR §807.87 & §807.92** – Provide mandatory submission content and summary format. |
| **21 CFR Part 820 (QMSR)** – Demonstrate design controls, document control, CAPA, post‑market surveillance plans. |
| **21 CFR Part 830** – UDI assignment & GUDID entry. |

---

### 5. Human‑Escalation Triggers  

1. **Predicate Uncertainty** – If a suitable predicate cannot be identified within 10 business days, flag for senior RA review and consider De Novo pathway.  
2. **Performance Data Deficiency** – Absence of validated functional or interoperability testing beyond the internal “quick test” level triggers escalation to engineering leadership; must be resolved before submission draft lock.  
3. **Regulatory Classification Dispute** – Any indication that FDA might view the software as a diagnostic device (e.g., wording “interpretation”) requires senior RA sign‑off and possibly a pre‑submission meeting request.  
4. **QMSR Non‑Compliance** – If audit of the current QMS shows gaps with the new Part 820 (effective Feb 2026), escalation to quality assurance manager is mandatory; submission cannot proceed until remediation.  
5. **UDI/Labeling Gaps** – Missing UDI strategy or incomplete labeling triggers immediate hold on final 510(k) package.  
6. **Cybersecurity Findings** – Any critical vulnerability uncovered during assessment must be reported to the product security officer and risk mitigation plan revised before filing.  

---

### 6. Bottom‑Line Recommendation  

- Proceed with a **Traditional Class II 510(k)** under **21 CFR Part 892 §892.2050**, provided a suitable predicate is secured and all performance, usability, cybersecurity, SOUP, labeling, UDI, and QMSR evidence are compiled per the citations above.  
- Prioritize closing the evidentiary gaps (performance testing, usability, predicate identification) within the next 3‑4 weeks; otherwise move to senior RA escalation as listed.

---

### 7. Peer Review Prompt  

> **To fellow RA colleagues:** Please challenge the assumptions made regarding (a) the appropriateness of a Class II 510(k) versus potential De Novo classification, (b) completeness of the identified evidence gaps given the limited source excerpt, and (c) any jurisdiction‑specific nuances (e.g., state‑level reporting or recent guidance updates) that may have been overlooked.  

--- 

*End of draft.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 13/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,535자 | — |
| 규제 식별자 인용 | 13개 | — |
| source excerpt 근거 일치 | **2/13 (15%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 11개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR Part 892`, `Part 892`, `21 CFR §801`, `21 CFR §830.10`, `21 CFR Part 820`, `Part 820`, `21 CFR 820`, `21 CFR Part 830`
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

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

### kb-eval-20260724-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "85c0ee79c16fe2d9", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_PreSubmission_QSub_가이드.md", "source_hash": "417191845804e82051a123525f91ed116a02c2eba4f516018604d1460525c8f5"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `85c0ee79c16fe2d9`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_PreSubmission_QSub_가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/FDA_PreSubmission_QSub_%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `417191845804e82051a123525f91ed116a02c2eba4f516018604d1460525c8f5`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `FDA_PreSubmission_QSub_가이드.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 3.1 Cover Letter (표지 서한) | 필드 | 내용 | |---|---| | 제목 | "Pre-Submission for [Device Name]" | | 회사명, 주소 | 정식 등록 정보 | | Primary Contact | 이름, 직함, 전화, 이메일 | | Regulatory Contact | 담당 RA 담당자 | | 제출 목적 | 한 문단 (어떤 피드백이 필요한가) | | 계획 중인 제출 유형 | 예: "510(k) 제출 예정" / "IDE 신청 전 SRD 요청" | | 회의 요청 여부 | 서면 피드백만 / 회의 병행 중 선택 | ## 7. 3개 지역 Pre-Sub 동등 제도 비교 | 항목 | FDA (미...
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

> **Regulatory Draft – Pre‑Submission (Q‑Sub) Planning for an X‑ray Imaging Device**

---

### 1. Classification & Primary Submission Pathway  

| Item | Determination |
|------|----------------|
| **Device family** | X‑ray radiology system (hardware + image processing software). |
| **CFR Part** | **21 CFR §892** – Radiology / Imaging devices. |
| **Specific class** | Likely **Class II**, regulated under **§892.2050** for “Medical image management and processing systems” (or the appropriate subsection for the hardware portion). |
| **Primary FDA submission** | 510(k) Premarket Notification, to be filed **6–12 months** after a Pre‑Submission (Q‑Sub) meeting per industry best practice (see source excerpt note on “FDA: 510(k) 제출 6~12개월 전 Pre‑Sub”). |
| **Regulatory program for early interaction** | FDA **Pre‑Submission (Q‑Sub)** via the CDRH Portal (PreSTAR). |

> *Framework citation*: 21 CFR §807.92 (requirements for a 510(k) submission); 21 CFR §820 (Quality Management System Regulation, effective Feb 2026); 21 CFR §830 (UDI requirements).  
> *No specific identifier found in source – verify separately* for the precise §892 subsection that matches the exact device function (e.g., hardware vs. software).

---

### 2. Evidence Package Required for a 510(k)

| Evidence | Typical content | Gap flag (based on current information) |
|----------|----------------|-----------------------------------------|
| **Cover Letter** (see source Sec 3.1) | Title, company info, primary contact, regulatory contact, purpose of submission, planned submission type, meeting request option. | – Device name & intended use missing; – No indication whether a meeting is desired. |
| **Device Description / Indications for Use** | Detailed description, schematics, software architecture, labeling excerpts. | – Not provided in source. |
| **Predicate Comparison (Substantial Equivalence)** | Table of predicates with 510(k) numbers, device classification, intended use, technological characteristics. | – No predicate identified. |
| **Performance Testing** | • *Bench*: electrical safety, electromagnetic compatibility, mechanical durability.<br>• *Radiation Safety*: dose measurements, beam quality (IEC 60601‑2‑XX).<br>• *Software Validation* (if applicable): verification/validation per IEC 62304, risk controls per ISO 14971. | – No data presented; test protocols missing. |
| **Risk Management File** | ISO 14971‑based analysis, hazard list, mitigations, residual risk evaluation, and linkage to design outputs. | – Not mentioned. |
| **Design History File (DHF)** | Project plans, design inputs/outputs, verification & validation records, change control logs. | – No DHF referenced. |
| **Labeling** | Instructions for Use (IFU), labeling graphics, safety warnings, UDI placement per §830.10‑§830.60. | – Absent. |
| **UDI Implementation Plan** | Device Identifier (DI) & Production Identifier (PI) format, GUDID submission schedule. | – No UDI plan cited. |
| **Quality System Evidence** | Current QMS certification to ISO 13485, compliance with updated **QMSR (21 CFR §820)**. | – Unclear if QMSR documentation exists. |
| **Sterility / Biocompatibility (if applicable)** | ASTM/FDA guidance for any patient‑contact components. | – Not addressed. |

---

### 3. Key Risk Controls & Regulatory References  

| Control Area | Requirement | Reference |
|--------------|-------------|-----------|
| **Radiation Safety** | Output dose, beam quality, shielding, compliance with IEC 60601‑2‑XX and FDA guidance for X‑ray devices. | No specific identifier found in source – verify separately (FDA Guidance “Medical Imaging Device Radiation Dose Guidance”). |
| **Software** (if image processing) | Development lifecycle per IEC 62304; verification & validation; cybersecurity per FDA “Postmarket Management of Cybersecurity” guidance. | No specific identifier found – verify separately. |
| **General Risk Management** | ISO 14971 risk analysis, integration with design controls. | 21 CFR §820.30 (Design controls). |
| **Predetermined Change Control Plan (PCCP)** | If AI/ML functionality exists, a PCCP must be defined per FDA Final Guidance Dec 2024. | No specific identifier found – verify separately. |

---

### 4. Missing Information & Actions Required  

1. **Device Name & Trade/Model Number** – Insert into cover letter and all downstream documentation.  
2. **Intended Use Statement** – Precise clinical indication, patient population, and anatomical site.  
3. **Predicate Device(s)** – Identify at least one legally marketed 510(k) with a matching classification; provide 510(k) numbers.  
4. **Complete Test Protocols & Results** – Bench, radiation, software validation.  
5. **Risk Management File (ISO 14971)** – Hazard analysis and mitigations linked to design outputs.  
6. **UDI Strategy** – DI/PI format, issuance authority, GUDID registration plan.  
7. **QMSR Compliance Evidence** – ISO 13485 certification or internal audit results confirming alignment with 21 CFR §820 (effective Feb 2026).  
8. **Cover Letter Decision** – Confirm whether a meeting is requested (e.g., “meeting request: yes, prefer virtual conference”) to trigger the 100‑day response timeline.

---

### 5. Human‑Escalation Triggers  

| Trigger | Reason | Recommended Action |
|---------|--------|---------------------|
| **No predicate identified** | Substantial equivalence cannot be demonstrated without a clear comparator. | Pause Q‑Sub preparation; task senior regulatory lead to conduct market search and select appropriate predicate(s). |
| **Incomplete risk management file** | FDA will reject 510(k) if residual risks are not adequately addressed. | Escalate to risk management team – require completed ISO 14971 dossier before submission. |
| **UDI plan absent** | Non‑compliance with §830 may delay clearance and affect post‑market tracking. | Assign UDI specialist; develop a timeline aligned with 510(k) filing. |
| **QMSR evidence missing** | New QMS regulation (effective Feb 2026) is mandatory for all submissions after that date. | Alert QA manager to confirm ISO 13485/QMSR compliance, obtain audit reports. |
| **Radiation safety data not available** | X‑ray devices are subject to strict dose limits; missing data = FDA may issue a complete response request (CRR). | Initiate radiation testing program; involve medical physicist. |
| **Cover letter lacks meeting request decision** | Determines whether the 100‑day written response or optional meeting applies, impacting timeline. | Clarify with project sponsor; update cover letter accordingly. |

If any of the above triggers arise, **escalate to senior regulatory manager (Level 2)** for review and resource allocation before proceeding with the Q‑Sub submission.

---

### 6. Peer Review Prompt  

> *“Please challenge the assumptions made regarding device classification under §892.2050, the completeness of the evidence checklist, and any jurisdiction‑specific gaps identified in the pre‑submission plan. Confirm whether additional FDA guidance documents (e.g., ‘Medical Imaging Device Radiation Dose Guidance’, IEC 60601‑2‑XX references) should be explicitly cited or incorporated.”*  

--- 

**End of Draft**

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 12/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,242자 | — |
| 규제 식별자 인용 | 9개 | — |
| source excerpt 근거 일치 | **0/9 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 9개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §892`, `21 CFR §807.92`, `21 CFR §820`, `21 CFR §830`, `21 CFR §820.30`
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

1. Chunk `124523812258860464`

> ### 3.1 Cover Letter (표지 서한) | 필드 | 내용 | |---|---| | 제목 | "Pre-Submission for [Device Name]" | | 회사명, 주소 | 정식 등록 정보 | | Primary Contact | 이름, 직함, 전화, 이메일 | | Regulatory Contact | 담당 RA 담당자 | | 제출 목적 | 한 문단 (어떤 피드백이 필요한가) | | 계획 중인 제출 유형 | 예: "510(k) 제출 예정" / "IDE 신청 전 SRD 요청" | | 회의 요청 여부 | 서면 피드백만 / 회의 병행 중 선택 |

2. Chunk `367708542439035920`

> ## 7. 3개 지역 Pre-Sub 동등 제도 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR/NB (유럽) | |---|---|---|---| | 제도명 | Pre-Submission (Q-Sub) | 사전상담 (제조·수입업 허가 전 상담) | NB Early Dialogue / Scientific Advice | | 법적 구속력 | 없음 (non-binding) | 없음 (참고 의견) | 없음 (NB opinion) | | 응답 목표 | 70일 (서면) / 100일 (회의) | 명시 없음 (통상 수 주) | NB별 상이 (30~90일) | | 비용 | 무료 (PDUFA/MDUFA 포함) | 무료 | NB 과금 (별도 견적) | | 온라인 제출 | CDRH Portal (PreSTAR) | 민원24 / 온라인 신청 [검증 필요] | NB 시스템별 상이 | | 제출 빈도 제한 | 없음 (단, 과도한 중복 질문 지양 권고) | 없음 | NB별 상이 | | X-ray 특이사항 | CDRH 방사선 부서(OSB) 담당 | 의료기기안전국 체외진단기기과 [검증 필요] | NB 방사선 전문 심사관 배정 | **자사 행동 지시 (3개 지역)**: - **FDA**: 510(k) 제출 6~12개월 전 Pre-Sub 1회 필수 고려 (시험...

### kb-eval-20260724-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "164066096f05c2ab", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `164066096f05c2ab`
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

> **Regulatory Draft – “촬영실 GUI Software (영상 처리·표시 소프트웨어)”**

---

### 1. Bottom‑line regulatory pathway  
| Item | Determination |
|------|----------------|
| **Device type** | Software as a Medical Device (SaMD) that performs image processing/display for radiology. |
| **Regulatory class** | Class II – “Image Processing Software” (21 CFR §892.2050). |
| **Premarket submission** | 510(k) using the standard eSTAR format; include a complete Section G (Performance Testing – Software). |
| **Relevant statutes & guidance** | • 21 CFR §892.2050 (class determination) <br>• FDA Guidance: *Content of Premarket Submissions for Device Software Functions* (2023‑06‑14) <br>• FDA Guidance: *Cybersecurity in Medical Devices* (2023‑09‑27) <br>• IEC 62304:2006+A1:2015 (software lifecycle). |

*No specific predicate number appears in the source – verify separately before finalizing the 510(k).*  

---

### 2. Evidence required for a complete 510(k) eSTAR submission  

| Category | Required artifact(s) | Source‑derived note |
|----------|----------------------|---------------------|
| **Executive summary** | High‑level description, intended use, risk classification, and claim of substantial equivalence. | – |
| **Software Requirements Specification (SRS)** | Functional & non‑functional requirements, including security and interoperability. | Listed in the eSTAR Section G file tree. |
| **Software Design Specification (SDS)** | Architecture diagram, module description, data flow, interface specs. | Listed in the eSTAR Section G file tree. |
| **Risk Management** | IEC 62304‑based risk classification table; hazard analysis; mitigation plan. | Table A/B/C provided (excerpt [1]). |
| **Verification & Validation Plan/Report** | Test protocols and results for unit, integration, system, performance, and usability testing. | Files “Software_Validation_Plan.pdf”, “Software_Validation_Report.pdf” plus sub‑folders of test results (excerpt [2]). |
| **Traceability Matrix** | Mapping from requirements → design → verification → validation. | File “Requirements_Traceability_Matrix.xlsx”. |
| **Performance Test Results** | Quantitative metrics for image processing accuracy, latency, display fidelity; statistical analysis. | Folder “Performance_Test_Results/” (excerpt [2]). |
| **Defect & Anomaly Log** | Complete list of identified defects, root‑cause analyses, corrective actions, and final resolution status. | File “Anomaly_Log_and_Resolution.xlsx”. |
| **Cybersecurity Evidence** | Threat analysis, mitigation controls, software update strategy, and any Predetermined Change Control Plan (PCCP) if AI/ML features exist. | Guidance cited but no artifact listed – gap identified. |
| **Labeling & IFU** | Full labeling package conforming to 21 CFR §801 (including UDI per 21 CFR §830). | Not mentioned in source – gap identified. |
| **Quality Management System (QMS) compliance** | Evidence of ISO 13485‑aligned QMS under 21 CFR §820 (effective Feb 2026). | Not referenced – gap identified. |

---

### 3. Gaps / Missing Information (Evidence shortfalls)

1. **Predicate device identification** – no cleared 510(k) number provided to support substantial equivalence.  
2. **Cybersecurity documentation** – only guidance references; there is no threat model, mitigation plan, or PCCP described.  
3. **UDI implementation** – labeling files and GUDID submission evidence are absent.  
4. **QMSR (21 CFR §820) compliance evidence** – process certificates, SOPs, CAPA records not listed.  
5. **Clinical performance data** (if intended for diagnostic use) – no clinical validation or comparison study cited.  
6. **Software classification justification** – while IEC 62304 class table is shown, a narrative linking the device’s specific functionality to Class B (or C if severe risk) is required.  

*All items above are “no specific identifier found in source — verify separately.”*

---

### 4. Risk Controls (per IEC 62304 & FDA guidance)

| Hazard | Potential harm | Control measure (as evidenced) |
|--------|----------------|--------------------------------|
| Software malfunction → incorrect image rendering | Misinterpretation of clinical images – moderate to severe injury | • Classified as Class B (basic DICOM viewer + processing) per table; risk mitigated by robust unit/integration testing (test result folders). |
| Unauthorized access / malware injection | Data breach, patient privacy violation | • Cybersecurity guidance cited; need to provide encryption, authentication, and audit‑trail controls (gap). |
| Update‑related failure (post‑market change) | Loss of functionality after software patch | • Implementation of a Predetermined Change Control Plan (PCCP) required for any future AI/ML updates (not yet documented). |
| Incorrect anomaly handling → unresolved defect persists in field | Potential injury if defect affects diagnostic display | • Defect log & resolution matrix provided; must show closure verification and CAPA linkage to QMS (gap: QMS evidence). |

---

### 5. Citations

*Framework references (no verify caveat)*  
- 21 CFR §892.2050 – Class II “Image Processing Software”.  
- FDA Guidance *Content of Premarket Submissions for Device Software Functions* (2023‑06‑14).  
- FDA Guidance *Cybersecurity in Medical Devices* (2023‑09‑27).  
- IEC 62304:2006+A1:2015 – software lifecycle processes.  

*Source‑derived identifiers*  
- 21 CFR §892.2050 – appears in excerpt [1].  
- eSTAR Section G file list – appears in excerpt [2].

All other regulatory citations (e.g., 21 CFR §820, §801, §830) are standard framework references; no specific paragraph numbers were supplied by the source.

---

### 6. Human‑Escalation Triggers

| Trigger | Action |
|---------|--------|
| **Missing predicate 510(k)** | Pause submission; senior RA to locate an appropriate cleared device and draft substantial‑equivalence argument. |
| **Absence of cybersecurity evidence or PCCP** | Escalate to Cybersecurity Lead – develop threat model, mitigation plan, and (if applicable) a Predetermined Change Control Plan before filing. |
| **No UDI/Labeling package** | Notify Labeling & Regulatory Affairs Manager to prepare FDA‑compliant labeling and GUDID submission. |
| **QMSR compliance not demonstrated** | Escalate to Quality Assurance – produce ISO 13485/QMS certificates, SOPs, CAPA evidence. |
| **Risk class determined as C (severe harm)** | Require additional bench or possibly limited clinical validation; senior RA and Clinical Affairs must review before proceeding. |
| **Any identified high‑severity defect in Anomaly Log** | Immediate CAPA initiation and FDA MDR reporting per 21 CFR §803 if the defect could cause serious injury. |

When any of these triggers are hit, the work package should be flagged for human review; no automatic closure is performed.

---

### 7. Peer‑review prompt  

*@RA‑Peer:* Please challenge the assumptions above:  
1. Is the classification as Class II under §892.2050 appropriate given only “basic processing” functions?  
2. Are there any FDA‑recognised predicates for GUI‑type image‑processing software that we may have overlooked in the source material?  
3. Does the current evidence list satisfy the “Performance Testing – Software” requirements of eSTAR without additional clinical data?  
4. Identify any jurisdiction‑specific gaps (e.g., UDI, QMSR) that could impede filing under the new 2026 QMS regulation.

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 11/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,453자 | — |
| 규제 식별자 인용 | 7개 | — |
| source excerpt 근거 일치 | **2/7 (28%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 5개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §801`, `21 CFR §830`, `21 CFR §820`, `21 CFR §803`
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

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

## ra_eu

### kb-eval-20260724-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "b6dea4f737f3e163", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b6dea4f737f3e163`
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

> **Regulatory Gap‑Analysis Draft – Clinical Evaluation & Conformity Assessment**

---

### 1. Device Scope (information required to set the regulatory pathway)

| Item | Current status | What is missing | Impact on classification / route |
|------|----------------|-----------------|-----------------------------------|
| **Intended medical purpose** (diagnosis, therapy, monitoring…) | Not provided in source | Precise wording of label/IFU and any claimed indications | Determines the applicable **Rule 9‑12‑17** (Annex VIII) and thus the device class |
| **Mode of action** – active vs. passive, invasive vs. non‑invasive, duration of use | Not provided | Whether the device delivers energy, is implanted, or is for transient contact | Required to select the correct **Rule** (e.g., Rule 9, 10, 11, 17) and class |
| **Target user type** – professional health‑care personnel vs. lay person | Source notes “**동일한 사용자 유형** (same kind of user)” as an *additional MDR requirement* but does not give the device’s user group | Confirmation whether the device is intended for HCPs only, lay users, or both | Affects equivalence eligibility (see § 22 GSPR) and may shift classification under Rule 9/10 when a lay‑person use is involved |
| **Anatomical site / clinical condition** – same body part & disease severity | Source states “same body part” and “identical clinical state (including severity & stage)” as required for equivalence | Exact anatomical location, disease name, staging criteria | Needed to justify equivalence with a predicate device |
| **Sterility/Measuring function/Re‑usable surgical instrument** | Not indicated | Whether the device is sterile, measuring or reusable surgical | Determines whether **Is / Im / Ir** sub‑class (Art. 52(7)) applies and whether NB involvement is limited |

*Human escalation trigger*: **Any of the above items remains undefined → classification cannot be finalised; pause any CE submission preparation until clarified.**

---

### 2. Determination of Device Class & Conformity Assessment Route  

| Hypothetical class (once intent known) | Art. 52 reference | Mandatory NB involvement | MDR route (Annex number) |
|----------------------------------------|-------------------|--------------------------|---------------------------|
| **Class I** (non‑sterile, non‑measuring, non‑reusable surgical) | Art. 52(7) | No NB required | Self‑declaration; Technical Documentation per **Annex II & III**, EU Declaration of Conformity **Annex IV** |
| **Class Is / Im / Ir** (sterile, measuring, reusable instrument) | Art. 52(7) | Yes – limited scope NB review (Annex IX Chapters I & III or Annex XI Part A) | Same as Class I but with NB audit of the specific aspect |
| **Class IIa** | Art. 52(6) | Yes – full NB assessment | **Annex IX** (Chapters I & III + §4 technical‑doc assessment of one representative device) *or* **Annex II & III** plus **Annex XI §§10/18** |
| **Class IIb** | Art. 52(4) | Yes – full NB assessment | **Annex IX** (full technical‑doc assessment, possibly per generic group) *or* **Annex X** (type‑examination) + **Annex XI** |
| **Class III** | Art. 52(3) | Yes – full NB assessment | **Annex IX** (full assessment) *or* **Annex X** + **Annex XI** |

*Human escalation trigger*: **If the intended purpose places the device in Class IIa‑III, a Notified Body must be engaged immediately; delay any further documentation until NB is selected.**

---

### 3. Clinical Evaluation Evidence Requirements (MDR)

| Requirement | Source / Citation | What must be provided |
|-------------|-------------------|------------------------|
| **Clinical Evaluation Report (CER)** – complete and kept current | **Annex XIV Part A**; Article 61 MDR | • Systematic literature review <br>• Clinical data from the device or equivalent devices <br>• Benefit‑risk analysis |
| **Equivalence justification** – same clinical state, same body part, similar patient group, *same user type* (new MDR addition) | MDCG 2020‑5 (Equivalence) – cited in source | • Detailed comparison table with predicate device(s) covering: intended purpose, indications, patient demographics, user profile, and performance claims |
| **Sufficiency of clinical evidence** – per MDCG 2020‑6 | MDCG 2020‑6 (Sufficient Clinical Evidence) – cited in source | • Evidence that the aggregate data (clinical investigations, PMS data, literature) meets the “sufficient” threshold for the claim |
| **Exemptions under Article 61(4‑6)** (e.g., low‑risk devices) | MDCG 2023‑7 – cited in source | • Justification why the device qualifies for exemption; supporting risk classification and GSPR compliance |
| **CER content guidance** | MDCG 2024‑3 – cited in source | • Structure of the CER (clinical background, clinical data, analysis, conclusions) – used as a checklist |

*Human escalation trigger*: **If any equivalence element (user type, body part, patient group) is missing or ambiguous → CER cannot be accepted; request clarification from the device development team.**

---

### 4. Post‑Market Surveillance (PMS) Obligations  

| Obligation | MDR Article / Annex | Required artefacts |
|------------|---------------------|--------------------|
| **PMS system** (process & resources) | Art. 83 MDR | Integrated PMS plan, SOPs, and assigned responsibilities |
| **PMS Plan** (scope, data sources, periodicity) | Art. 84 MDR | Documented plan aligned with device class |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | Art. 86 MDR (annual for IIb/III, biennial for IIa) | • Benefit‑risk conclusions <br>• PMCF results <br>• Sales & user population data |
| **PMS report** – for Class I | Art. 85 MDR | Summary of PMS activities and any corrective actions |

*Human escalation trigger*: **Absence of a PSUR or PSA plan for a Class IIa‑III device → non‑compliance; pause CE marking steps until PMS documentation is drafted.**

---

### 5. Risk Management & GSPR Alignment  

| GSPR Section | Relevance to Clinical Evaluation Gap | Evidence needed |
|--------------|--------------------------------------|-----------------|
| **§ 16 – protection against radiation** (if applicable) | Needed when the device emits ionising radiation (Rule 10) | Radiation safety testing reports, compliance with IEC 60601‑2‑54/28 etc. |
| **§ 17 – electronic programmable systems / software** | Required for devices with embedded software (Rule 11) | Software life‑cycle file per IEC 62304, cybersecurity assessment |
| **§ 18 – active devices & connections** | Applies if device is active (Rule 9/10) | Verification of electrical safety, performance validation |
| **§ 22 – intended user type** | Directly ties to the “same user type” equivalence criterion highlighted in source excerpt 1 | User‑interface risk analysis showing suitability for HCPs vs. lay users |
| **§ 23 – labeling & IFU** | Must reflect actual clinical performance and user group | Draft labels, instructions for use, claim justification |

*Human escalation trigger*: **If any of the above GSPR evidence is missing or not linked to clinical data → risk management file incomplete; require immediate generation before NB audit.**

---

### 6. Summary Judgment & Action Items  

1. **Classification cannot be finalised** until the intended medical purpose, mode of action, anatomical site, patient population, and user type are clearly documented.  
2. **Equivalence dossier is incomplete** – the source explicitly adds *same user type* as an MDR‑only requirement; you must capture whether the device is for HCPs only or also for lay users.  
3. **Clinical Evidence Gap** – no clinical investigation data, literature search results, or PMS data have been supplied. Without these, the CER cannot satisfy Annex XIV Part A nor MDCG 2020‑6.  
4. **PMS & PSUR Documents missing** for any Class IIa/IIb/III device; prepare a PMS plan (Art. 84) and schedule PSURs (Art. 86).  
5. **Risk Management documentation must reference the relevant GSPR sections**, especially § 22 for user type, to close the equivalence loop.  

**Immediate human escalation triggers**

- **Trigger 1 – Undefined Intended Use / User Type:** Halt any CE‑marking work until the product owner supplies a definitive intended purpose and target user description.  
- **Trigger 2 – Missing Clinical Data:** Stop drafting the CER; request clinical investigation reports, PMS data, or a systematic literature review.  
- **Trigger 3 – Classification Unknown:** Engage a regulatory specialist to run an Annex VIII rule analysis once the above inputs are available; schedule NB involvement if Class IIa/IIb/III is likely.  
- **Trigger 4 – Absent PMS Framework:** For any device beyond Class I, mandate creation of a PMS plan and PSUR schedule before proceeding to Notified Body assessment.

---

### 7. Peer‑Review Prompt  

> **Colleague, please review the assumptions made above:**  
> - Are the equivalence criteria (same clinical state, same body part, similar patient group, *same user type*) correctly interpreted from the source?  
> - Does the proposed classification matrix align with the device’s likely intended purpose, or are additional Rule references needed?  
> - Have we captured all MDR post‑market obligations for the anticipated class?  
> - Identify any jurisdiction‑specific gaps (e.g., Korean MFDS reference in the source) that may affect our CE‑marking strategy.  

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 45/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,398자 | — |
| 규제 식별자 인용 | 15개 | — |
| source excerpt 근거 일치 | **4/15 (26%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 11개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art. 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Art. 85` | MDR Article 85 | Post-market surveillance report (Class I) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

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

1. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

2. Chunk `1090731331984830062`

> > 최종 갱신: 2026-05-18 (자동보강 #52) > 근거: MDR Regulation (EU) 2017/745 Article 61 & Annex XIV | MDCG 2020-5 (Equivalence, Apr 2020) | MDCG 2020-6 (Sufficient Clinical Evidence, Apr 2020) | MDCG 2023-7 (Article 61(4)-(6) Exemptions, Dec 2023) | MDCG 2024-3 (CER Content) | FDA 510(k) Program Guidance (Jul 2014) | FDA Best Practices for Predicate Device Selection (Oct 2023 Draft) | MFDS 의료기기 허가·신고·심사 등에 관한 규정 (고시 제2024-88호) # Clinical Evaluation (MDR) 심화 — 동등성·충분성 기준

### kb-eval-20260724-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7f031b9b3ec42e2c", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7f031b9b3ec42e2c`
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

> **Regulatory Draft: Clinical‑Evidence Gap Analysis for PSUR (MDR Art 86)**  

---

### 1. Device identification – information needed  
| Item | Current status | Comment |
|------|----------------|---------|
| Trade name / model | **missing** | Required to locate the device in EUDAMED and to verify its classification. |
| Intended purpose & indication | **missing** | Determines which classification rule (Annex VIII) applies. |
| Device type (active, implantable, software, etc.) | **missing** | Affects risk class and the applicable conformity‑assessment route (Art 52). |

> **Action:** Obtain the above data from the product team before any further regulatory conclusion can be drawn.

---

### 2. Likely classification & conformity‑assessment route  

| Potential class | Applicable MDR rule(s) (Annex VIII) | Conformity‑assessment route (Art 52) |
|-----------------|--------------------------------------|--------------------------------------|
| **IIa** | Rule 9, 10, 11 or 17 – depending on the active/diagnostic nature (requires device description). | Art 52(6): Annex IX (chapters I & III) **or** Annex II + III together with Annex XI §§10‑18. |
| **IIb** | Rule 9, 10 (ionising radiation) or Rule 17 (imaging software). | Art 52(4): Annex IX (full technical documentation) **or** Annex X + Annex XI. |
| **III** | Rule 9 (high‑risk therapeutic) or Rule 11 (software with life‑threatening impact). | Art 52(3): Annex IX (full assessment) **or** Annex X + Annex XI. |

*Because a Periodic Safety Update Report (PSUR) is required, the device must be at least Class IIa.*  
> **Human trigger:** If classification cannot be confirmed within 5 working days of this draft, escalation to the product‑owner for clarification is mandatory.

---

### 3. Required evidence for the PSUR (Art 86 MDR)

| Requirement (Art 86(1)) | Evidence to be supplied | Source excerpt |
|--------------------------|------------------------|----------------|
| **(a) Sales volume & estimated patient exposure** – §‑c | • Quantified sales per region (EU, Korea, US, other). <br>• Methodology and assumptions for converting sales units into patient exposures (e.g., devices sold vs. patients treated). | Excerpt [2] – “판매량 및 노출 추정 (MDR Art.86(1)(c))”. |
| **(b) Post‑market clinical follow‑up (PMCF) results** – §‑d | • Reference to the approved PMCF plan (document number & version). <br>• Current status of the PMCF (ongoing, completed, planning stage). <br>• Summarised interim results for the reporting period. <br>• Statement on how these results have been incorporated into the Clinical Evaluation Report (CER). | Excerpt [1] – “PMCF 결과 연계 (Art.86(1)(d))”. |
| **(c) Benefit–risk determination** – §‑a | • Updated benefit‑risk analysis reflecting new clinical data, adverse events, and any changes in intended use. | No specific identifier found in source — verify separately. |
| **(d) Summary of PMS activities** – §‑b | • Reference to the PMS plan (Art 84). <br>• Description of any field safety corrective actions (FSCA) taken. | No specific identifier found in source — verify separately. |

Additional mandatory annexes for a complete PSUR:  

* Annex XII (if applicable) – Summary of Clinical Evaluation (Annex XIV Part A).  
* Annex XIII – PMCF plan & evaluation report (Annex XIV Part B).  

---

### 4. Gap analysis – missing or incomplete information

| Gap | Description | Impact on PSUR completeness |
|-----|-------------|------------------------------|
| **Sales figures** | No quantitative values for EU, Korea, US, other markets. | Prevents fulfilment of Art 86(1)(c). |
| **Patient‑exposure methodology** | No documented assumptions or calculation method per MDCG 2022‑21 §5.3 (source citation). | Risk of non‑conformity; regulator may request justification. |
| **PMCF plan reference** | Only placeholder “[문서번호, 버전]”. | Prevents traceability to the approved PMCF plan required by Art 86(1)(d) and Annex XIV Part B. |
| **PMCF status** | Placeholder “[진행 중 / 완료 / 계획 단계]” – not filled. | Cannot assess whether sufficient clinical data exist for the CER update. |
| **Interim PMCF results** | Placeholder “[요약 또는 "중간 데이터 없음"]”. | Absence of clinical evidence may lead to an inconclusive benefit‑risk assessment. |
| **PMCF integration into CER** | Placeholder “[반영 여부, 반영 내용]” – not detailed. | Required by Art 86(1)(d); missing linkage compromises the CER’s currency. |
| **Next PMCF interim report date** | Placeholder “[YYYY-MM-DD]”. | Without a scheduled date, future compliance cannot be demonstrated. |
| **Device‑specific classification data** | No rule reference or intended use description. | Prevents selection of correct conformity‑assessment route (Art 52). |

> **Human trigger:** If any of the above gaps remain unresolved after a 10‑day review period, the PSUR draft must be halted and escalated to the Clinical & Regulatory Lead for data collection.

---

### 5. Risk‑management implications

| Action | Rationale | Relevant MDR provision |
|--------|-----------|-------------------------|
| **Update risk management file** (ISO 14971) with new hazards identified from PMCF results. | New clinical findings may reveal previously unrecognised risks or change the severity/probability assessment. | Annex I §9‑10 (risk management). |
| **Re‑evaluate residual risk & benefit–risk ratio** in light of interim PSUR data. | Required for Art 86(1)(a) and to justify continued market placement. | Annex XIV Part A (CER). |
| **Implement corrective actions** if adverse trends are identified (e.g., increased field incidents). | Must be documented in the PMS system (Art 83) and reflected in the PSUR. | Art 87 (trend reporting) & Art 88 (FSCA). |
| **Verify that updated risk controls are communicated** to users via labeling updates (Annex I §23). | Ensures compliance with information‑supplied requirements. | Annex I Chapter III (§23). |

---

### 6. Citations

* MDR **Art 86(1)(c)** – sales volume & patient exposure (source [2]).  
* MDR **Art 86(1)(d)** – PMCF results linkage (source [1]).  
* **MDCG 2022‑21 §5.3** – guidance on methodology and assumptions for patient‑exposure estimates (referenced in source [2]).  
* MDR **Annex XIV Part A** – Clinical Evaluation Report requirements (framework reference).  
* MDR **Annex XIV Part B** – PMCF plan & evaluation report (framework reference).  
* MDR **Art 83/84/85/86/87/88** – post‑market surveillance system, plan, reports and trend reporting (framework references).  
* ISO 14971 – risk management process (framework reference).

---

### 7. Human‑escalation triggers  

| Trigger | Condition | Escalation path |
|---------|-----------|-----------------|
| **Incomplete sales/exposure data** | Any region cell remains empty or contains placeholder text. | Notify Product Management → deadline 5 working days; if not met, raise to Head of Regulatory Affairs. |
| **Unfilled PMCF details** (plan ref., status, results, CER integration, next report date) | Presence of “[ ]” placeholders after review. | Immediate escalation to Clinical Lead for data provision within 3 working days. |
| **Absence of classification information** | No rule or class identified after initial assessment. | Escalate to Device Development Team – classification workshop required; deadline 7 days. |
| **Evidence of serious incidents or FSCA not captured** | No mention in the draft but known from vigilance logs. | Trigger urgent review by Safety‑Monitoring Committee and report under Art 87 within 24 h. |
| **Approaching PSUR reporting deadline without complete data** | Less than 30 days to next scheduled PSUR submission. | Escalate to Project Manager – resource allocation for rapid data collection; if still incomplete, consider provisional submission with justification per MDCG guidance. |

---

### 8. Peer‑review prompt  

*“@RA‑Colleague, please challenge the assumptions made above regarding (i) the inferred class based solely on PSUR requirement, (ii) the completeness of the evidence checklist derived from the two source excerpts, and (iii) any jurisdiction‑specific gaps that may exist for non‑EU sales regions (Korea, US). Identify missing regulatory citations or alternative MDR provisions that should be addressed.”*  

--- 

**Regulatory judgment:**  
The current PSUR draft lacks critical quantitative data (sales, patient exposure), a fully identified PMCF plan and its interim results, and essential device classification information. Until these gaps are closed, the PSUR cannot satisfy MDR Art 86(1) requirements and would be rejected by the Notified Body. Immediate data collection and clarification of the device’s intended use/classification are required, with escalation triggers defined above to ensure timely remediation.

**Citation Lint (C1 — 구조적 인용 오류 자동 감지)**

- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art.86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86(1)(d)`)

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 44/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,150자 | — |
| 규제 식별자 인용 | 16개 | — |
| source excerpt 근거 일치 | **1/16 (6%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 15개 | `No hallucination` |
| C1 린터 구조 오류 | 12건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

⚠️ **C1 구조 오류** (존재할 수 없는 하위 식별자 — Score 1 후보):
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Art 84` | MDR Article 84 | Post-market surveillance plan |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `Art 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art 87` | MDR Article 87 | Reporting of serious incidents and field safety corrective actions |
| `Art 88` | MDR Article 88 | Trend reporting |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Annex XII`, `Annex XIII`
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

1. Chunk `108347462317924009`

> ### Section 7. PMCF 결과 연계 (Art.86(1)(d)) | 항목 | 내용 | |---|---| | PMCF 계획 참조 문서 | [문서번호, 버전] | | PMCF 현재 상태 | [진행 중 / 완료 / 계획 단계] | | 이번 기간 주요 PMCF 결과 | [요약 또는 "중간 데이터 없음"] | | PMCF 결과의 CER 반영 | [반영 여부, 반영 내용] | | 다음 PMCF 중간 보고 예정일 | [YYYY-MM-DD] | ---

2. Chunk `131915604397474083`

> ### Section 2. 판매량 및 노출 추정 (MDR Art.86(1)(c)) | 지역 | 판매 수량 | 추정 환자 노출 수 | 판매 기간 | |---|---|---|---| | EU | [수량] | [추정 수] | [기간] | | 한국 | [수량] | [추정 수] | [기간] | | 미국 | [수량] | [추정 수] | [기간] | | 기타 | [수량] | [추정 수] | [기간] | | **합계** | **[합계]** | **[합계]** | — | > **MDCG 2022-21 §5.3:** 정확한 환자 수 추정이 어려울 경우 방법론과 가정 조건을 명시. ---

### kb-eval-20260724-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "83356594e071d8f8", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `83356594e071d8f8`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & PMCF Evaluation Report (MDR 2017/745)**  

---

### 1. Device Classification & Conformity‑Assessment Route  
| Item | Assessment | Regulatory basis |
|------|------------|------------------|
| **Intended purpose / mode of action** – not supplied in the source material. | *Classification cannot be confirmed until intended use (therapeutic, diagnostic, active‑software etc.) and patient population are defined.* | MDR Annex VIII (classification rules). The appropriate rule (e.g., Rule 9, 10, 11 or 17) must be applied once the purpose is known. |
| **Provisional class** – assume *Class IIa* for a non‑implantable active device unless the intended use indicates higher risk (e.g., energy delivery that could cause hazardous situations → Rule 9/10 ⇒ Class IIb). | The provisional class determines the minimum conformity‑assessment route. | Art. 52(6) – **Annex IX** (technical‑documentation assessment + QMS) *or* Annex II + III together with **Annex XI** §10 (production‑conformity verification). |
| **Conformity‑assessment route** – *full technical‑documentation assessment (Annex IX)* is the default for Class IIa/IIb devices. | The Notified Body will review the Technical Documentation (Annex II) together with the PMS system (Annex III) and the PMCF Evaluation Report (Annex XIV Part B). | Art. 52(6) & Annex IX; MDR requirement to keep the Clinical‑Evaluation Report up‑to‑date (Art. 61, Annex XIV Part A). |

> **Human‑escalation trigger #1** – *If the intended use cannot be clarified within 10 working days, elevate to senior RA manager for classification decision and possible NB consultation.*  

---

### 2. Required Evidence for Clinical Evaluation (CER) & PMCF  
| Evidence type | What must be provided | Where it is recorded |
|---------------|----------------------|----------------------|
| **Scientific/clinical literature** – systematic review of state‑of‑the‑art (SOTA). | Full search strategy, inclusion/exclusion criteria, critical appraisal – demonstrating clinical performance and safety. | CER (Annex XIV Part A) |
| **Clinical data from the device itself** – post‑market surveillance & PMCF. | Raw patient data, source documents, statistical analysis, summary of adverse events. | PMCF plan (Annex XIV Part B) and **PMCF Evaluation Report** (see §5.2 below). |
| **Equivalence / comparator data** – clinical data from “same” or “similar” devices. | Identification of predicate devices, justification of similarity, extracted performance results. | Section D of the PMCF Evaluation Report (mandatory per source). |
| **Risk‑management linkage** – impact of new clinical evidence on the Risk Management File (RMF) and SSCP. | Updated risk analysis, residual‑risk evaluation, mitigation actions. | Section E of the PMCF Evaluation Report; also reflected in the updated RMF (ISO 14971). |
| **Standards & guidance applied** – harmonised standards (e.g., IEC 60601‑2‑54 for radiography) and MDCG guidances. | List of standards with edition/date that were used to demonstrate conformity. | Section F of the PMCF Evaluation Report; cross‑referenced in Technical Documentation (Annex II). |
| **Conclusions & corrective actions** – overall assessment against PMCF objectives. | Statement whether clinical benefit outweighs risk, and if any preventive or corrective measures are required. | Section G of the PMCF Evaluation Report. |

> **Human‑escalation trigger #2** – *If any mandatory evidence (e.g., raw clinical data or equivalence justification) is missing after a 15‑day remediation period, flag for NB review and possible delay of conformity assessment.*  

---

### 3. Gap Analysis – Missing Information (Based on Source Excerpts)  
| Required item | Current status (from source) | Gap |
|---------------|------------------------------|-----|
| **Clinical target anatomy / indication** (“임상적 적용 부위”) | Listed as “same 필수” but no actual description provided. | *Specify anatomical site(s) and therapeutic/diagnostic intent.* |
| **Intended patient population** (“임상적 대상 집단”) | Placeholder only. | *Define age range, disease state, comorbidities.* |
| **User type** (“임상적 사용자 유형”) | Not detailed. | *Identify professional user vs lay‑person (Annex I §22).* |
| **Core clinical performance endpoints** (“임상적 핵심 성능”) | No data supplied. | *Define measurable performance criteria (sensitivity, specificity, accuracy, etc.).* |
| **PMCF Evaluation Report – Sections A–G** | Table lists mandatory sections but content is absent. | *Populate each section with the required information (manufacturer contact, device description, results of PMCF activities, equivalence evaluation, impact on CER/RMF/SSCP, applied standards/guidance, overall conclusion).* |
| **Link to Technical Documentation** – impact of clinical data on GSPRs (§10‑§20). | Not addressed. | *Map each new clinical finding to the relevant General Safety & Performance Requirement.* |
| **Post‑Market Surveillance (PMS) plan & system** (Art. 84/83) | No reference in source. | *Develop PMS plan, define data collection schedule, reporting procedures.* |
| **Periodicity of PSUR / PMS report** (Art. 86) – not mentioned. | Missing. | *Determine reporting frequency based on class; for Class IIa at least every 2 years.* |

> **Human‑escalation trigger #3** – *If any of the above gaps remain unresolved after a joint cross‑functional review (RA, Clinical, R&D) within 20 working days, issue a “Clinical Evidence Deficiency Notice” to project leadership and pause CE marking submission.*  

---

### 4. Risk Controls & GSPR Alignment  
| GSPR clause | Relevant risk control (example) | Reference |
|-------------|--------------------------------|-----------|
| **§16 – Protection against radiation** (if device emits ionising radiation) | Engineering shielding, interlock systems, dose‑monitoring software. | MDR Annex I §16; IEC 60601‑2‑54 (when applicable). |
| **§17 – Electronic programmable systems** | Secure software development lifecycle, validation per IEC 62304. | MDR Annex I §17; ISO 14971 risk controls for software. |
| **§18 – Active devices** | Redundant safety circuits, alarm limits, verification of energy delivery. | MDR Annex I §18. |
| **§20 – Mechanical/thermal risks** | Material selection, burst‑pressure testing, user‑interface ergonomics (IEC 62366‑1). | MDR Annex I §20. |
| **§22 – Use by lay persons** (if applicable) | Mandatory training, clear labeling, limited functionality for untrained users. | MDR Annex I §22; labeling per Annex I §23. |

All risk controls must be documented in the **Risk Management File** and reflected in the **Clinical Evaluation Report** when new clinical evidence modifies residual‑risk assessment (Section E of PMCF Evaluation Report).

---

### 5. Citation Summary  

| Item | Source citation (per rules) |
|------|-----------------------------|
| Clinical‑Evaluation Report requirement – keep current | Annex XIV Part A; Art. 61 (framework reference). |
| PMCF plan / evaluation report mandatory content | No specific identifier found in source — verify separately (source provides a table of sections A–G, but no formal MDCG document number). |
| Classification rules (Rule 9/10/11/17) | MDR Annex VIII – Rule numbers (framework reference). |
| Conformity‑assessment routes per class | Art. 52(3‑7) and Annex IX / X / XI (framework reference). |
| PMS system & reporting obligations | Art. 83–86 (framework references). |
| GSPR clauses cited (§16, §17, §18, §20, §22, §23) | MDR Annex I (framework reference). |
| Harmonised standards for X‑ray devices (example) | IEC 60601‑2‑54, IEC 60601‑2‑28 (framework reference). |

---

### 6. Human‑Escalation Triggers – Summary  

1. **Classification uncertainty** – elevate after 10 days if intended use remains undefined.  
2. **Missing mandatory clinical evidence** – flag after 15 days; involve Notified Body if critical.  
3. **Unaddressed gaps in PMCF Evaluation Report (A‑G)** – issue deficiency notice after 20 days; halt submission.  
4. **Adverse trend or negative PMCF outcome** – immediate notification to senior RA and quality manager; trigger corrective‑action plan per Art. 83/84.  

---

### 7. Next Steps for the Project Team  

1. **Obtain complete device description** (intended purpose, target anatomy, user group).  
2. **Populate PMCF Evaluation Report sections A–G** with concrete data.  
3. **Conduct a systematic literature review** to fill the SOTA gap.  
4. **Map clinical evidence to GSPRs** and update RMF/SSCP accordingly.  
5. **Finalize PMS plan & schedule** (Art. 84) and define PSUR frequency (Art. 86).  

---

#### Peer‑Review Prompt  
*Please review this draft for:*

- **Assumption validity** – Are the provisional classification and risk‑control suggestions appropriate given limited device information?  
- **Source coverage** – Does the gap analysis capture all mandatory elements from the MDCG guidance excerpt, or are additional items required?  
- **Jurisdictional completeness** – Have any EU‑specific nuances (e.g., EUDAMED registration Art. 33‑39) been omitted that could affect the submission timeline?  

*Your feedback will be incorporated before the final CE‑marking dossier is compiled.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 43/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,250자 | — |
| 규제 식별자 인용 | 17개 | — |
| source excerpt 근거 일치 | **0/17 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 17개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art. 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Annex III` | MDR Annex III | Technical documentation on post-market surveillance |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

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

1. Chunk `1032759063790726230`

> │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ```

2. Chunk `1132312459160211217`

> ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과 (데이터 수집 결과, 긍정·부정 포함, 편차 근거) | | D | 동등·유사 기기 임상데이터 평가 결과 | | E | 기술문서에 대한 결과의 영향 (CER, Risk Management File, SSCP 각각 명시) | | F | 적용된 CS, 조화표준, 가이던스 | | G | 종합 결론 (PMCF 목적 대비 결과, 예방·시정 조치 필요성) |

### kb-eval-20260724-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "fa90ff878ef527e7", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `fa90ff878ef527e7`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter |...
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

> **Regulatory Draft – Clinical Evaluation Gap Analysis for a Diagnostic‑Radiology X‑ray System (MDR)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Device type** | Active device that emits ionising radiation for diagnostic radiology and incorporates a detector and image‑processing software. | – |
| **MDR classification rule** | **Rule 10 (Active devices for diagnosis/monitoring)** → **Class IIb** (because the emitted ionising radiation can pose a hazardous situation). | MDR Annex VIII, Rule 10 |
| **Conformity‑assessment route** | Primary route: **Annex IX** – full technical‑documentation assessment by a Notified Body (NB) together with an EU Declaration of Conformity (Annex IV). Alternative (if chosen by the sponsor): **Annex X** type‑examination + **Annex XI** production conformity verification. | MDR Art. 52(4) – Class IIb; see Annex IX, Annex X and Annex XI |

*Decision:* The deficiency letter under review originates from an NB that is already assessing the technical documentation (CER, TD). This indicates the sponsor has elected the **Annex IX** route.

---

### 2. Evidence Required for a Complete Submission  

| Category | Minimum artefacts required (MDR) | Why needed / reference |
|----------|-----------------------------------|------------------------|
| **Clinical Evaluation Report (CER)** | – Current CER (updated to reflect latest clinical data). <br>– Clinical equivalence justification with a predicate device. | Annex XIV Part A; kept up‑to‑date under Art. 61. |
| **Clinical Data Supporting Equivalence** | • Test report showing detective quantum efficiency DQE ≥ 65 % (e.g., *TR‑2024‑015*, IEC 62220‑1‑1). <br>• Comparative performance data for image quality, dose metrics, and safety. | Clinical equivalence clause in the source excerpt; MDR Art. 61(2) & Annex XIV Part A. |
| **Post‑Market Surveillance (PMS) System** | • PMS plan (Art. 84). <br>• PMS report/PSUR (Art. 86) – annual for Class IIb. | Art. 83–86 MDR. |
| **Post‑Market Clinical Follow‑up (PMCF)** | PMCF Plan and Interim/FInal Evaluation Report (Annex XIV Part B). | Annex XIV Part B. |
| **Risk Management File** | Full risk analysis, evaluation of residual risks and benefit–risk determination (ISO 14971) covering radiation protection (§16 GSPR), active‑device control (§18 GSPR), software safety (§17 GSPR). | Annex I §§ 16, 17, 18; ISO 14971. |
| **Labeling & IFU** | Labels and Instructions for Use complying with Annex I §23 (including radiation safety information, contraindications, user training). | Annex I §23. |
| **Technical Documentation** | Complete device description, design dossier, verification/validation reports, IEC conformity‑assessment certificates (e.g., IEC 60601‑2‑28 / 60601‑2‑54), software lifecycle documentation (IEC 62304) and usability engineering (IEC 62366‑1). | Annex II. |
| **Quality Management System** | Certified ISO 13485:2016 QMS, plus evidence of NB‑reviewed NC resolution where applicable. | Annex IX Chapters I & III; EU Declaration of Conformity (Annex IV). |

---

### 3. Gaps Identified in the Current Submission  

| Gap | What is missing / insufficient | Impact on assessment |
|-----|--------------------------------|----------------------|
| **Clinical equivalence justification** | Only DQE ≥ 65 % is cited (see source excerpt [1]); no data on dose‑area product, image‑quality scores, or clinical outcomes. | NB will likely request additional comparative clinical data to satisfy Annex XIV Part A. |
| **PMCF evidence** | No PMCF plan or interim report referenced. | Required by Annex XIV Part B; absence blocks final conformity assessment. |
| **PMS documentation** | PMS plan and PSUR not supplied. | Art. 84–86 require a functional PMS system for Class IIb. |
| **Risk analysis of radiation exposure** | No explicit reference to GSPR §16 (radiation protection) or verification against IEC 60601‑2‑28/54 standards. | Risk controls cannot be demonstrated; NB will request a dedicated risk assessment report. |
| **Software lifecycle documentation** | If image‑processing software is part of the system, no IEC 62304 compliance evidence shown. | Needed for GSPR §17 and Annex XIV Part A clinical data on software performance. |
| **Usability/Human factors** | No IEC 62366‑1 usability engineering file cited. | Required to address user errors that could increase radiation dose (GSPR §22). |
| **Labeling compliance** | No Annex I §23‑compliant labeling package attached. | NB will reject the device until labeling is provided. |
| **QMS NC closure evidence** | Table [2] lists “CER, TD, QMS NC” as typical deficiency types but does not provide updated NC resolution records. | Outstanding NCs must be closed before final conformity verification (Annex IX). |

*Note:* The source table [2] also indicates the procedural environment (e.g., Structured Dialogue under Art. 7 MDR 2026/977) – this should be used for any clarification requests.

---

### 4. Required Risk Controls / Mitigations  

| Hazard area | Control measures (to be documented) |
|-------------|--------------------------------------|
| **Radiation protection** | • Shielding design meeting IEC 60601‑2‑28 limits.<br>• Dose monitoring and alarm functions (GSPR §16.4).<br>• Periodic dose‑audit procedures in PMS plan. |
| **Active device malfunction** | Redundant safety interlocks, self‑test routines, and fault‑diagnostic displays (GSPR §§ 18, 19). |
| **Software errors** | IEC 62304 lifecycle management, verification/validation against clinical performance criteria, post‑release updates logged in PMCF. |
| **User error / misuse** | Usability engineering according to IEC 62366‑1; clear IFU warnings for lay‑person use (GSPR §22). |
| **Residual risk / benefit–risk** | Documented residual risk analysis with justification that benefits outweigh remaining risks (Art. 61(2)(c), Annex XIV Part A). |

All controls must be traceable to the risk management file and reflected in the PMS/PMCF activities.

---

### 5. Citations  

| Source type | Citation |
|-------------|----------|
| **Framework references** | MDR Annex VIII Rule 10 (device classification); MDR Art. 52(4) (Conformity‑assessment route for Class IIb); MDR Annex XIV Part A & B (clinical evaluation and PMCF requirements); MDR Annex I §§ 16, 17, 18, 22, 23; MDR Art. 83–86 (PMS system/report). |
| **Instance identifiers from source** | DQE requirement reference: *Test Report TR‑2024‑015*, IEC 62220‑1‑1 (source [1]). <br>Deficiency‑letter regulatory basis: “MDR Annex VII + 2026/977” (source [2]). |
| **No specific identifier found in source — verify separately** | – (All framework citations are standard; no additional case‑specific regulation numbers were provided.) |

---

### 6. Human‑Escalation Triggers  

1. **Missing Clinical Evidence** – If the sponsor does not supply comparative clinical data beyond DQE ≥ 65 % within the agreed NB response window, the NB must issue an *Additional Information (AI) Request* under the Structured Dialogue procedure (Art. 7 MDR 2026/977). Failure to respond → assessment termination (source [2] “미응답 시 – 평가 종료 / 불승인”).  

2. **Unresolved QMS Non‑Conformities** – Any outstanding NCs listed in the deficiency letter must be closed before the next audit checkpoint; otherwise, the NB should place a *clock‑stop* on the dossier (source [2] “Clock‑stop – 예 (NB 요청 당일 stop…)”).  

3. **PMS/PMCF Gap** – Absence of an approved PMS plan or PMCF report triggers a mandatory halt in the conformity assessment until those documents are submitted, per Art. 83–86.  

4. **Risk‑Management Deficiency** – If radiation‑protection risk controls (GSPR §16) are not demonstrated, the NB must request a supplemental risk‑analysis addendum; non‑delivery within 60 days leads to an evaluation halt (source [2] “답변 기한 – NB와 합의 (법정 상한 없음)”).  

5. **Labeling Non‑Compliance** – Missing Annex I §23 labeling forces the NB to reject the EU Declaration of Conformity; sponsor must provide corrected IFU before any CE marking can be issued.

*Action required:* The sponsor should prepare a consolidated response package addressing all gaps, referenced to the above evidence list, and submit it within the agreed NB‑response timeline. The project lead must monitor the clock‑stop status and escalate to senior regulatory management if the NB signals an impending assessment termination.

---

**Peer‑review prompt (for another RA colleague):**  

> *Please review the classification logic (Rule 10 → Class IIb) and the selected conformity‑assessment route. Confirm that all MDR citation references are appropriate, and verify whether any additional IEC standards (e.g., IEC 60601‑2‑54 for radiography) should be explicitly required in the evidence list.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 42/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,852자 | — |
| 규제 식별자 인용 | 21개 | — |
| source excerpt 근거 일치 | **3/21 (14%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 18개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Art. 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

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

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1014893419282866507`

> | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter | 보완 요청 | Additional Information (AI) Request | | 근거 법령 | MDR Annex VII + 2026/977 | 의료기기법 §12 + 허가·신고·심사 규정 | 21 CFR 807 + FDA Review Policy | | 답변 기한 | NB와 합의 (법정 상한 없음) | 1차 60일, 2차 60일 | 180일 (타임라인 기산일부터) | | 최대 중단 횟수 | 4회 (product verification 기준) | 2차까지 (실질 2회) | 제한 없음 (Interactive Review 가능) | | Clock-stop | 예 (NB 요청 당일 stop, 제출 익일 resume) | 예 (보완 기간 제외) | 예 (AI 발송일부터 stop) | | 미응답 시 | 평가 종료 / 불승인 | 취하 간주 | 허가 거부 | | 사전 대화 창구 | Structured Dialogue (Art.7, 2026/977) | 상담제도 (비공식) | Pre-Sub (Q-Sub) (공식, 문서화) | | 주요 결함 유형 | CER, TD, QMS NC, Labelin...

### kb-eval-20260724-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a345d6f5f951e29c", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "209487b4b22e96052be65198c3a3ed54cef6303dd563722b36bf9c98910a1cf9"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a345d6f5f951e29c`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & MDR Submission Planning**

---

### 1. Device Synopsis (required to proceed)

| Item | Status / Comment |
|------|-------------------|
| **Device name / model** | *Not supplied* – cannot map to a classification rule. |
| **Intended purpose / indication** | *Missing* – essential for determining the applicable Rule 9‑11, 17 etc. |
| **Key functions (active/diagnostic/therapeutic, software, radiation)** | *Missing* – needed to decide whether Rule 9, 10, 11 or 17 applies. |
| **Target market (EU only / other regions)** | Unknown; impacts need for an EU authorised representative (Art. 11). |

> **Human‑escalation trigger:** If any of the above items remain unavailable after 5 working days, pause all MDR preparation and request a full product description from R&D/Marketing.

---

### 2. Preliminary Classification Pathway  

1. **Collect intended‑use information** → map to an MDR classification rule (Annex VIII).  
   * Example:  
     - Active therapeutic device → **Rule 9** (Class IIa or IIb)  
     - Active diagnostic/monitoring device → **Rule 10** (Class IIa or IIb)  
     – Software providing diagnostic info → **Rule 11** (Class IIa‑III)  
     – X‑ray imaging system components → **Rule 10, 17, 11** as appropriate.  

2. **Determine device class** based on risk level indicated in the rule. Use the decision matrix in Annex VIII.

> **Human‑escalation trigger:** If after mapping the device still falls into more than one possible class (e.g., borderline IIa/IIb), convene a classification review board with clinical, R&D and RA leads.

---

### 3. Conformity‑Assessment Route (once class is known)

| Class | MDR route (Art 52) | Notified Body involvement |
|-------|-------------------|----------------------------|
| **I** (non‑sterile, non‑measuring) | Art. 52(7): self‑declaration – Technical documentation (Annex II & III) + EU Declaration of Conformity (Annex IV) | No |
| **Is / Im / Ir** | Art. 52(7): Annex IX Chap. I & III *or* Annex XI Part A – limited NB scope | Yes (limited) |
| **IIa** | Art. 52(6): Annex IX Chap. I & III + technical‑documentation assessment of a representative device (Annex IX §4) **or** Annex II & III + Annex XI §§10/18 | Yes |
| **IIb** | Art. 52(4): Annex IX Chap. I & III + technical‑documentation assessment of each generic group (Annex IX §4) **or** Annex X + Annex XI | Yes |
| **III** | Art. 52(3): Full technical‑documentation assessment under Annex IX **or** Annex X + Annex XI | Yes |

> **Human‑escalation trigger:** When class is IIa or higher, the RA lead must issue a formal NB‑engagement plan within 3 working days.

---

### 4. Evidence Package Required by MDR  

| Evidence Item | Regulatory Source (framework) | Current Status (per source excerpts) | Gap |
|---------------|------------------------------|--------------------------------------|-----|
| **Technical Documentation** (Design Dossier, “TD”) – Annex II & III | Annex II (technical file); Annex III (PMS technical documentation) | Step 1–7 of the TD creation workflow are defined in source [1]; however actual artefacts (design files, V&V reports) are not supplied. | • Collect complete design specifications, manufacturing processes, verification & validation data.<br>• Populate GSPR‑mapping report (source [1] step 3). |
| **GSPR Mapping Report** | Annex I §§10‑22 (General Safety & Performance Requirements) – mapping via “GSPR checklist” | Planned in source [1] step 3, but no evidence of completion. | • Perform and document full GSPR compliance verification. |
| **Risk Management File** | ISO 14971; Annex I §16‑22 | Step 5 of workflow (source [1]) indicates risk file will be integrated, but actual RM report missing. | • Provide hazard analysis, risk evaluation, risk control measures, residual risk justification. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | Step 4 of workflow (source [1]) calls for CER authoring, but no data supplied. | • Conduct systematic literature review, collect clinical performance and safety data.<br>• Identify any missing post‑market clinical follow‑up (PMCF) evidence. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84; Annex III (if applicable) | Step 6 of workflow (source [1]) defines PMS plan creation, but no draft exists. | • Define systematic PMS activities, data sources, periodic safety update reports (PSUR). |
| **PMCF Plan & Evaluation Report** | Annex XIV Part B | Not mentioned in source – must be prepared for Class IIa+ devices. | • Develop a PMCF study protocol aligned with the identified clinical gaps. |
| **Labeling & IFU** | Annex I §23 (information supplied) | No mention in source excerpts. | • Produce labels, CE marking declaration, Instructions for Use (IFU) in required languages. |
| **UDI‑Device Registration in EUDAMED** | Art. 33‑39 (EUDAMED database) | Not referenced. | • Obtain a UDI issuing agency code and register device identifiers. |
| **EU Representative (if non‑EU manufacturer)** | Art. 11 (Economic Operator – EU representative) | Economic operator matrix (source [2]) lists the role but no confirmation of appointment. | • Confirm PRRC designation and appoint an Authorized Representative where required. |

---

### 5. Risk Controls & Mitigation Actions  

| Hazard / Risk | Control (from risk management) | Reference Clause |
|---------------|--------------------------------|------------------|
| **Residual clinical risk** | Conduct PMCF to confirm benefit‑risk balance; update CER accordingly. | Art. 61, Annex XIV Part A |
| **Non‑conformity of labeling (CE mark/UDI)** | Implement a label verification checklist aligned with Annex I §23. | Annex I §23 |
| **Inadequate PMS data capture** | Deploy an electronic vigilance system complying with Art. 83; schedule annual PSUR (Art. 86). | Art. 83, Art. 86 |
| **Software safety (if applicable)** | Follow IEC 62304 lifecycle and IEC 62366‑1 usability engineering. | No specific identifier in source – verify separately |
| **Radiation protection (if X‑ray component)** | Apply IEC 60601‑2‑54/28 etc., ensure compliance with Annex I §16.4. | No specific identifier in source – verify separately |

> **Human‑escalation trigger:** If any high‑severity hazard lacks a verified control measure, the RA lead must raise a “Risk Control Deficiency” to senior management within 2 working days.

---

### 6. Summary Judgment & Next Steps  

1. **Classification cannot be finalised** without explicit intended‑use and functional description.  
2. **Technical documentation framework is defined** (source [1]), but all underlying artefacts remain incomplete.  
3. **Economic‑operator responsibilities are outlined** (source [2]); verification of PRRC/Authorized Representative appointment is pending.  

> **Immediate actions required:**  
- Obtain a complete product description (intended use, active functions, software/systems).  
- Gather design files, V&V results, and initial risk analysis from R&D.  
- Draft the GSPR mapping matrix and confirm completion.  
- Verify whether an EU representative is needed; if so, appoint and document.  

If any of these items cannot be supplied within the stipulated time‑frames (5 working days for product description; 10 working days for design & risk artefacts), **escalate to senior RA management** to consider postponement of the MDR submission schedule.

---

### 7. Peer‑Review Prompt  

> *Please review this gap analysis and challenge the assumptions made regarding the classification pathway, the completeness of the evidence list, and any jurisdiction‑specific obligations that may have been overlooked (e.g., specific IEC standards for radiation devices, national vigilance reporting nuances). Identify any missing regulatory citations or additional documentation that should be incorporated before proceeding to NB engagement.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 41/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,917자 | — |
| 규제 식별자 인용 | 20개 | — |
| source excerpt 근거 일치 | **1/20 (5%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 19개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex III` | MDR Annex III | Technical documentation on post-market surveillance |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 33` | MDR Article 33 | European database on medical devices (Eudamed) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

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

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `24104208734622027`

> ## 3. 경제운영자(Economic Operator) 역할 정의 | 역할 | MDR 조항 | 핵심 의무 | 자사 해당 여부 | |------|----------|----------|--------------| | 제조자(Manufacturer) | Art. 10 | 기술문서, QMS, UDI, PMS, Vigilance, PRRC 지정 | ☐ | | 수권대리인(AR) | Art. 11 | EU 내 제조자 대리, 당국 연락창구 | ☐ (비EU 제조사 필수) | | 수입업자(Importer) | Art. 13 | CE 마크·UDI 확인, 보관조건 준수, 불만 전달 | ☐ | | 유통업자(Distributor) | Art. 14 | CE 마크·라벨 확인, 보관·운송 조건 준수 | ☐ |

## ra_kr

### kb-eval-20260724-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "08aa0ca26cb2ad74", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `08aa0ca26cb2ad74`
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

> **Regulatory Draft – KGMP Evidence Readiness (Korean MFDS)**  

---

### 1. Device Classification & Submission Route  
| Item | Determination | Basis / Citation |
|------|---------------|------------------|
| **Risk class** | *Undetermined – requires device‑type, intended use and risk analysis* | No specific identifier found in source — verify separately |
| **Submission pathway** | • Class I (low‑risk) → **신고 (notification)**  <br>• Class II–IV (medium to high‑risk) → **허가 (approval)**  | Korean Medical Device Act (MDA) classification rules – framework reference |

*Action*: Obtain the device’s intended use, labeling claims and risk‐based classification from the manufacturer to select the correct MFDS pathway.

---

### 2. Required Evidence for KGMP Compliance  

| Requirement | What Must Be Submitted | Source‑Based Reference |
|-------------|-----------------------|------------------------|
| **KGMP facility certification** (ISO 13485‑aligned) | • Current KGMP certificate issued by MFDS <br>• Evidence of ISO 13485:2016 compliance, if applicable | No specific identifier found in source — verify separately |
| **Production & Service Records** | Detailed service records as required by **§820.35** (FDA QSR) – Korean equivalent is reflected in the KGMP QMS requirements | §820.35 (cited from excerpt [1]) |
| **Complaint Handling / Feedback** | Record of complaint completion per **§820.20** (FDA QSR) and MDR Articles 83‑86 for post‑market surveillance data collection | §820.20 (excerpt [1]); MDR Art. 83~86 (excerpt [1]) |
| **Non‑conforming Product Management** | Non‑conformance reports, corrective actions, and disposition records as required by ISO 13485 clause 8.3 (aligned with KGMP) | “ISO 동일” – indicates direct mapping to ISO 13485 (excerpt [1]) |
| **Post‑Market Surveillance (PMS) Data** | PSUR/PMSR data feeds, linked to the device’s risk class and MDR Annex IX §3.2 acceptance of MDSAP audits | MDR Annex IX §3.2 (excerpt [2]); “PSUR/PMSR 연동” (excerpt [1]) |
| **Process Monitoring & Measurement Equipment Management** | Calibrated measurement equipment logs per ISO 13485 clause 7.6 / FDA **§820.72** (not shown but implied by “ISO 동일”) | “ISO 동일” for 7.6 (excerpt [1]) |
| **Internal Audits** | Audit reports satisfying the MFDS expectation that FDA‑type inspections are no longer an exception (see **FDA QSR §820.180(c)** removal) | “FDA 실사 대상 (구 QSR §820.180(c) 예외 삭제)” (excerpt [1]) |
| **MDSAP Acceptance** | If using an MDSAP‑certified site, include the MDSAP audit report as a substitute for on‑site MFDS inspection per MDR Annex IX §3.2 | “MDSAP 수용 (실사 대체 가능) – MDR Annex IX §3.2” (excerpt [2]) |

*Note*: Where the source simply states “ISO 동일”, it denotes that Korean KGMP aligns directly with the corresponding ISO 13485 clause; therefore no separate Korean‑specific citation is required.

---

### 3. Missing Information & Gaps  

| Gap | Why It Matters (Korean Context) | Required Action |
|-----|--------------------------------|-----------------|
| **Device name, model, intended use** | Determines risk class and whether a clinical evaluation or local trial is needed. | Request from sponsor/manufacturer. |
| **Risk classification decision** | Impacts submission type (신고 vs 허가) and depth of clinical evidence required. | Obtain a completed Korean risk‑classification worksheet. |
| **Local language labeling & IFU** | MFDS mandates all labeling, package inserts and user manuals be in Korean. | Provide drafts for review; confirm conformity with MFDS labeling notice (specific number to be verified). |
| **Local clinical data requirement** | For Class II–IV devices, MFDS often requires Korean clinical evidence unless an exemption is granted via mutual acceptance of foreign CERs (MAD). | Verify whether the device can rely on a foreign Clinical Evaluation Report; if not, plan local study. |
| **KGMP certificate issuance date & validity** | MFDS will reject out‑of‑date certificates. | Supply current KGMP certificate copy. |
| **MDSAP scope coverage** | Not all MDSAP audit scopes are accepted for every device type. | Confirm that the MDSAP audit includes relevant processes (production, post‑market). |

---

### 4. Key Risk Controls to Highlight in Submission  

1. **Design Transfer & Process Validation** – documented per ISO 13485 clause 7.5 and MFDS QMS requirements.  
2. **Supplier Qualification & Purchasing Control** – aligned with FDA §820.50 (implied by “7.4 구매”).  
3. **Measurement Equipment Calibration** – traceability records as per ISO 13485 clause 7.6.  
4. **Post‑Market Surveillance System** – PSUR/PMSR generation feeding back into risk management (MDR Annex IX §3.2).  
5. **Complaint Investigation & Trending** – complete records at complaint closure per FDA §820.20 and MDR Art. 83‑86.  

---

### 5. Human‑Escalation Triggers  

| Trigger | Escalation To | Reason |
|---------|---------------|--------|
| No KGMP certificate supplied or certificate expired > 6 months | MFDS Liaison / Senior RA Lead | Submission will be non‑compliant. |
| Risk class cannot be confirmed after 5 business days of request | Project Manager & Regulatory Strategy Team | Classification determines the entire regulatory route. |
| Local Korean labeling not provided within review window (7 days) | Quality Assurance – Labeling Specialist | MFDS rejects dossiers lacking Korean language labeling. |
| MDSAP audit scope insufficient for required processes (e.g., no post‑market surveillance evidence) | Senior QA Auditor & External Audit Coordinator | Need to schedule supplemental on‑site MFDS inspection or obtain additional audit reports. |
| Unclear if foreign Clinical Evaluation Report can be accepted under MFDS mutual‑acceptance policy | Regulatory Affairs – International Evidence Lead | Potential need for local clinical data, which impacts timelines and budget. |

---

### 6. Summary Judgment  

- **Classification & submission route cannot be finalized** until device‑specific information (intended use, risk class) is obtained.  
- **KGMP evidence package must include:** current KGMP certificate, ISO 13485‑aligned QMS documentation covering purchasing, production, measurement equipment, non‑conformance, internal audit, and post‑market surveillance; any applicable MDSAP audit report; complaint handling records meeting §820.20; service records per §820.35; and Korean language labeling documents.  
- **Immediate human actions** focus on gathering missing device details, confirming local clinical data needs, and ensuring the KGMP certificate is valid.

---

### 7. Peer Review Prompt  

> *@RA‑Peer:* Please examine the assumptions made about the mapping of “ISO 동일” to the specific Korean QMS clauses, verify that MDR Annex IX §3.2 truly allows MDSAP audit substitution for all device categories, and identify any jurisdiction‑specific gaps (e.g., MFDS 고시 numbers for labeling or post‑market reporting) not covered by the provided source excerpts.  

--- 

*End of draft.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 30/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,017자 | — |
| 규제 식별자 인용 | 3개 | — |
| source excerpt 근거 일치 | **2/3 (66%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 1개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

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

1. Chunk `1012828200772392062`

> II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동일 | **FDA 실사 대상** (구 QSR §820.180(c) 예외 삭제) | NB 불시 감사 대상 | | **8.2.3 공정 모니터링** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.3 부적합 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.4 데이터 분석** | ISO 동일 | ISO 동일 | PSUR/PMSR 작성 근거 데이터 | | **8.5 개선** | ISO 동일 | ISO 동일 | ISO 동일 |

2. Chunk `1037950769042691196`

> MDSAP 수용 (실사 대체 가능) | MDR Annex IX §3.2 — MDSAP 부분 수용 |

### kb-eval-20260724-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "74ad579a8baaae6c", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "6e09bc3b8dcd278f80184587a5eaba125f19dbc86c1b2ce2f24b76bdc503c9a0"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `74ad579a8baaae6c`
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

> **KGMP Evidence‑Readiness & MFDS Submission Draft (Device‑agnostic)**  

---

### 1. Preliminary Classification & Submission Route  

| Decision point | Requirement | What is needed from sponsor | Current status |
|----------------|-------------|----------------------------|----------------|
| **Intended use / target patient population** | Determines risk class according to the “품목군 분류” matrix (now 64 categories per 고시 제2025‑22호). | Detailed description of therapeutic/diagnostic function, site of use, duration of contact. | *Missing – sponsor must provide.* |
| **Device type** | If it is a **융복합의료기기** (convergent device) and the primary function is medical, it is subject to full MF DS review per 고시 제2025‑22호. | Clarify whether the product’s principal function is medical or non‑medical (e.g., consumer). | *Missing – sponsor must clarify.* |
| **Risk level** | Apply Korean classification rules (same logic as EU MDR Annex VIII) to assign Class I, II, III or IV. | Risk analysis data (hazard identification, severity, probability). | *Pending.* |
| **Resulting pathway** | • **Class I (non‑high risk)** – Notification (신고).  <br>• **Class II–IV** – Full approval (허가) with KGMP certification required. | Classification outcome drives whether a “신고서” or a full “허가 신청서” is prepared. | *To be determined after classification.* |

*If classification cannot be resolved from the information above, the case must be escalated to senior RA for expert adjudication.*

---

### 2. Required Evidence Package (KGMP‑focused)

| Evidence | Korean regulatory basis | International equivalent | Status / Gap |
|----------|------------------------|---------------------------|--------------|
| **KGMP facility certification** | MFDS 고시 제2025‑22호 – KGMP (품목군) compliance required for Class II–IV devices. | ISO 13485:2016 QMS alignment; “GMP” mapping in the MFDS guide (see source [1]). | Facility audit report needed; *missing.* |
| **Quality Management System documentation** | Same notice – 30‑item procedure mapping required (SOP‑CC‑001 … SOP‑NC‑001). | ISO 13485:2016 clauses 4–8. | SOP list referenced in source [1]; actual documents not supplied – *missing.* |
| **Software Validation** (if applicable) | IEC 62304 fully incorporated per 고시 제2025‑22호 (formerly “참조 일부”). | IEC 62304:2006+A1. | Validation plan & reports required; sponsor must confirm software scope – *missing if device includes software.* |
| **Cybersecurity Management** (if applicable) | Cybersecurity requirement may be invoked per 고시 제2025‑22호 (부속서 참조). | IEC 62443 series, FDA “Content of Pre‑market Submissions for Management of Cybersecurity”. | Security risk assessment & mitigation plan required – *missing if device connects to network.* |
| **Risk Management File** | ISO 14971‑based file, referenced implicitly through KGMP mapping. | ISO 14971:2019. | FMEA/FMECA, risk control summary – *missing.* |
| **Labeling & IFU (Korean language)** | Mandatory Korean labeling per MFDS labeling rules (no specific notice number in source). | MDR Annex II/III; FDA 21 CFR 801. | Draft Korean label and IFU required – *missing.* |
| **Clinical Evidence** | For Class II‑IV, local clinical data may be required unless MFDS accepts foreign Clinical Evaluation Report (CER) under its periodic scope expansion. | EU MDR § 61(8); FDA 510(k) predicate. | Determine whether foreign CER can be used; sponsor must provide any existing FDA/CE documentation – *missing.* |
| **Non‑clinical GLP safety data** | MFDS accepts OECD‑MAD (Mutual Acceptance of Data) for non‑clinical studies if the study complies with GLP. | OECD GD 151. | If foreign animal toxicology exists, confirm GLP compliance – *missing.* |

---

### 3. Identified Missing Information & Immediate Actions  

| Gap | Required Action | Escalation Trigger |
|-----|-----------------|--------------------|
| **Intended use / primary function** | Obtain a clear indication statement from sponsor. | If not received within 5 business days, raise to Project Lead (risk of classification delay). |
| **Device classification outcome** | Perform risk‑based class determination using Korean “품목군” matrix. | Unresolved classification after sponsor clarification → senior RA review. |
| **KGMP audit report** | Schedule on‑site audit or accept third‑party certification evidence. | Failure to secure KGMP certificate within 30 days of submission start → project timeline flag. |
| **Software scope** | Confirm presence/absence of software; collect IEC 62304 development lifecycle documentation. | Missing software validation plan for a device that contains software → stop‑release hold and senior QA involvement. |
| **Cybersecurity** | Determine connectivity; if applicable, draft cybersecurity management plan. | No cyber risk assessment for an internet‑connected device → immediate escalation to CISO/PM. |
| **Korean labeling & IFU** | Translate and format according to MFDS labeling rules. | Absence of Korean label 10 days before dossier lock → regulatory hold. |
| **Clinical data strategy** | Decide on local trial vs. foreign CER acceptance; gather supporting documentation. | Inability to justify use of foreign CER → escalation to Clinical Affairs for possible local study design. |

---

### 4. Risk Controls Aligned with MFDS Requirements  

1. **Risk Management (ISO 14971)** – Perform hazard analysis, determine risk acceptability criteria, implement control measures; document in a Risk Management File.  
2. **Software Lifecycle (IEC 62304)** – Apply full development lifecycle, verification & validation activities, classification of software safety class.  
3. **Cybersecurity** – Conduct threat modeling, establish vulnerability management process, apply updates/patches per MFDS cyber‑security annex (부속서).  
4. **KGMP Process Controls** – Implement the 30 SOPs mapped in the MFDS guide (source [1]), maintain document control, change control, CAPA, non‑conformance handling.  
5. **Post‑Market Surveillance (PMS)** – Set up PMS plan per MFDS “시판후조사” requirements; include periodic safety update reports.  

---

### 5. Citation Summary  

| Item | Citation Type | Reference |
|------|---------------|-----------|
| KGMP & SOP mapping guidance | Framework reference (general) | ISO 13485:2016, MFDS guide (source [1]) |
| Revised GMP notice – expanded item groups, convergent device clarification, multi‑review, document simplification, IEC 62304 full adoption, cyber‑security optional clause | Instance identifier (specific notice number) | 고시 제2025‑22호 (source [2]) |
| Software validation standard | Framework reference | IEC 62304:2006+A1 |
| Cybersecurity guidance (부속서) | Framework reference – no specific notice number in source | MFDS cyber‑security annex (referenced in 고시 제2025‑22호) |
| OECD mutual acceptance of non‑clinical data | Framework reference | OECD GD 151 (not quoted in source) |
| Korean labeling requirement | Framework reference – not numbered in source | MFDS labeling regulations (general) |

*No other specific regulatory‑instrument numbers appear in the provided excerpts; where a concrete identifier is required, “no specific identifier found in source — verify separately” has been noted.*

---

### 6. Human‑Escalation Triggers  

| Condition | Who to Notify | Reason |
|-----------|---------------|--------|
| Classification cannot be finalized after sponsor clarification | Senior RA / Project Manager | Prevents downstream submission errors and timing risks. |
| KGMP certification not secured within planned timeline | QA Lead & Regulatory Director | Essential for Class II‑IV approval; missing KGMP blocks filing. |
| Software present but IEC 62304 evidence absent | Software Development Lead & QA | Non‑compliance with 고시 제2025‑22호 software clause. |
| Device is networked and no cyber‑risk plan exists | CISO / PM | MFDS may require cyber‑security controls; non‑compliance leads to rejection. |
| Local clinical data required but foreign CER not accepted | Clinical Affairs & Regulatory Lead | Determines need for additional trial, impacts schedule and budget. |
| Korean labeling/IFU not ready 10 days before dossier lock | Marketing / Legal | Failure to meet MFDS language requirement results in filing refusal. |

---

### 7. Peer‑Review Prompt  

> **To the next RA reviewer:**  
> Please challenge the assumptions made above regarding (1) the applicability of 고시 제2025‑22호 to convergent devices without explicit functional clarification, (2) the sufficiency of referencing OECD‑MAD for non‑clinical data in the absence of a cited MFDS notice number, and (3) any potential gaps where Korean‑specific obligations (e.g., detailed labeling elements, mandatory post‑market reporting formats) may have been overlooked given the limited source excerpts. Provide suggestions on additional source material that should be consulted to close these gaps.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 29/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,884자 | — |
| 규제 식별자 인용 | 7개 | — |
| source excerpt 근거 일치 | **2/7 (28%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 5개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex II` | MDR Annex II | Technical documentation |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `IEC 62443`, `21 CFR 801`
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

1. Chunk `107140411445338936`

> --- doc-id: MFDS_의료기기_제조_및_품질관리_기준 title: 의료기기 제조 및 품질관리 기준 (MFDS) (v0.2) type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: MFDS GMP 고시 요구사항 해설 및 ISO 13485 정합 매핑, 문서화 30대 절차 매핑 applicable: [ISO13485:2016, MFDS, FDA QMSR, EU MDR 2017/745] forms: [] related-docs: [SOP-CC-001, SOP-MFG-001, SOP-MFG-002, SOP-UDI-001, SOP-PMS-001, SOP-TRN-001, SOP-SUP-001, SOP-NC-001, SOP-CAPA-001, SOP-IA-001, SOP-MR-001, PRO-CRP-001] related-issues: [33] owner: RA/QA Lead last-review: 2026-05-14 review-due: 2027-05-07 --- # 의료기기 제조 및 품질관리 기준 (MFDS) — v0.2 > v0.2 — 2026-05-07: GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려...

2. Chunk `1127747106119376174`

> ## 2. 최신 개정 핵심 (고시 제2025-22호) | 항목 | 종전 | 개정 | |------|------|------| | 품목군 분류 | 26개 | 64개 | | 융복합의료기기 | 불명확 | 주된 기능이 의료기기이면 심사대상 명확화 | | 심사체계 | 복수심사 | 품질관리심사기관 단독심사 가능 | | 제출자료 | 광범위 | 간소화 | | SW 밸리데이션 | IEC 62304 참조 일부 | IEC 62304:2006+A1 전면 참조 편입 | | 사이버보안 | 미규정 | 적용 가능 시 사이버보안 관리 요구 (부속서 참조) |

### kb-eval-20260724-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "2a4e0f254c680e06", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2a4e0f254c680e06`
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

> **Regulatory Draft – KG GMP Evidence Readiness for a New Medical Device (Korea)**  

---

### 1. Device Classification & Submission Route  
| Item | Reasoning / Reference |
|------|------------------------|
| **Classification rule** | Apply the MFDS “의료기기 등급 분류 기준” (Medical‑Device Classification Criteria). The rule is selected based on the device’s intended purpose, invasiveness, and duration of use. *No specific classification rule number appears in the source excerpts; verify the applicable rule (e.g., 제1조‑제2항, “Class II – active devices”) separately.* |
| **Submission pathway** | • **Class I** – Notification (신고)  <br>• **Class II** – Certification (인증)  <br>• **Class III/IV** – Authorization (허가).  The pathway is determined by the classification outcome. *The source only lists “GMP 심사·평가 등에 관한 규정” as the governing regulation; no exact notice number is supplied, so confirm the current MFDS 고시 number for the submission type.* |

---

### 2. Required Evidence Package (KG GMP Focus)

| Evidence | Korean regulatory requirement | Typical international counterpart | Source citation |
|----------|------------------------------|-----------------------------------|-----------------|
| **KG GMP Certificate** | Must submit a valid KG GMP certification per the *“의료기기 제조 및 품질관리 기준”* (GMP standards). | ISO 13485:2016 compliance and FDA’s QSR. | No specific notice number found in source — verify separately. |
| **Technical Documentation (Tech‑doc)** | Includes design dossier, risk management file, validation/verification reports, labeling & IFU in Korean. Required under the “의료기기 GMP 심사·평가 등에 관한 규정”. | EU MDCG‑2020‑6 / FDA 510(k) Technical File. | No specific notice number found in source — verify separately. |
| **Clinical Evaluation Report (CER)** | If a Class II–IV device, Korean law demands a clinical evaluation that may incorporate foreign clinical data *only when the MFDS has accepted such evidence* (see ongoing scope expansions). | FDA 510(k) predicate use; EU CE Clinical Evaluation. | No specific notice number found in source — verify separately. |
| **Korean‑language Labeling & IFU** | All labeling, instructions for use, and package inserts must be provided in Korean per the MFDS labeling rules. | IEC 60601‑1‑2 (if applicable) + EU MDR Annex II. | No specific notice number found in source — verify separately. |
| **Risk Management File** | Conduct risk analysis per ISO 14971 and submit the file with the GMP audit checklist. | ISO 14971:2019. | No specific notice number found in source — verify separately. |
| **Post‑Market Surveillance (PMS) Plan** | Required for Class II–IV devices; must align with MFDS “시판후조사” obligations. | EU MDR Post‑Market Surveillance Plan; FDA Post‑Marketing Requirements. | No specific notice number found in source — verify separately. |

---

### 3. Gaps – Information Missing from Current Dossier  

| Missing Item | Why it matters (Korean requirement) | Suggested Action |
|--------------|--------------------------------------|------------------|
| **Exact classification rule & class** | Determines submission route and depth of clinical evidence required. | Perform a classification matrix check using MFDS criteria; obtain the specific 조/항 reference. |
| **Device‑specific intended use statement in Korean** | Required for labeling, risk management, and clinical evaluation scope. | Draft a concise Korean Intended Use description and attach to technical file. |
| **Foreign clinical data acceptance confirmation** | MFDS may accept FDA 510(k) or CE clinical data only if covered by the latest “foreign clinical evidence” notice. | Verify the latest MFDS 고시 that expands foreign CER acceptance; cite the notice number when obtained. |
| **KG GMP certification copy** | Mandatory for GMP audit submission checklist. | Obtain and attach current KG GMP certificate (validity ≥ 2 years). |
| **Full labeling set in Korean** | Non‑compliant language triggers rejection. | Prepare label, packaging, IFU in Korean; include translation verification log. |
| **Risk Management File (ISO 14971) evidence of conformity** | Required for PMS and safety evaluation. | Compile risk analysis, mitigation plans, residual risk justification. |
| **PMS Plan & Reporting Procedures** | Needed for Class II–IV devices under MFDS post‑market rules. | Draft PMS plan referencing MFDS “시판후조사” guidelines; include reporting timelines. |

---

### 4. Core Risk Controls (to be reflected in the dossier)

1. **Design‑out Risk Mitigation** – Apply failure mode and effects analysis (FMEA) during design phase.  
2. **Protective Measures** – Include hardware or software safeguards as required by ISO 14971.  
3. **User Training & Instructions** – Provide Korean user manuals that describe safe use, contraindications, and maintenance.  
4. **Post‑Market Monitoring** – Implement a real‑time adverse event reporting system linked to MFDS “시판후조사”.  

---

### 5. Citations (per the source excerpts)

| Citation | Type |
|----------|------|
| 「의료기기 제조 및 품질관리 기준」 (고시) – referenced as core GMP document in Chunk 341244002941932847 and Chunk 634338496332185325. | Framework reference (no specific notice number supplied). |
| 「의료기기 GMP 심사·평가 등에 관한 규정」 mentioned in both source chunks as the governing regulation for KG GMP review. | Framework reference (no specific identifier provided). |

*All other identifiers (e.g., 고시 번호, 조/항 numbers) are **not** present in the source excerpts; they must be retrieved from the latest MFDS publications before final submission.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation |
|---------|------------------------|
| **Uncertain device classification** – No clear rule or class identified. | Require senior RA to confirm classification and appropriate submission route. |
| **Missing KG GMP certificate** – Dossier lacks a current certification. | Pause submission; engage Quality/Manufacturing to obtain the certificate. |
| **Foreign clinical data acceptance unclear** – Recent MFDS scope change not verified. | Senior regulatory counsel must check latest 고시 for foreign CER acceptance before proceeding. |
| **Labeling not fully Korean or incomplete** – Potential rejection risk. | Escalate to Localization team & Legal for compliance review. |
| **PMS plan absent or insufficient for Class II–IV** – Post‑market obligations unmet. | Trigger Quality Assurance lead to develop a compliant PMS program. |
| **Regulatory notice number required but not found** – Any requirement citing a specific 고시/조/항 without a known identifier. | RA manager must retrieve the exact notice number from MFDS database before final filing. |

---

### 7. Peer‑Review Prompt  

> **To a fellow Korean RA:**  
> Please examine the assumptions made above regarding (a) the classification approach using MFDS criteria, (b) the completeness of the KG GMP evidence list given only the two source chunks, and (c) any jurisdiction‑specific gaps—particularly around foreign clinical data acceptance and labeling language requirements. Highlight any missing documents or alternative interpretations that could affect our submission strategy.

--- 

*End of draft.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 28/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,213자 | — |
| 규제 식별자 인용 | 4개 | — |
| source excerpt 근거 일치 | **0/4 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 4개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `Annex II` | MDR Annex II | Technical documentation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

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

1. Chunk `341244002941932847`

> ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트

2. Chunk `634338496332185325`

> ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)

### kb-eval-20260724-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "859601ccc1f53851", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md", "source_hash": "eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `859601ccc1f53851`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-24_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EC%A0%95%ED%95%A9%EC%84%B1.md)
- Source hash: `eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240`
- Focus: KGMP evidence readiness
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `2026-04-24_디지털의료제품법_요구사항_정합성.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버 ### 3.2 불일치·공백 항목...
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

> **Regulatory Draft – Digital Medical Device (Software‑Based) – KGMP Evidence Readiness**

---

### 1. Classification & Submission Route  

| Item | Korean regulatory basis | Likely outcome | Comments / actions |
|------|------------------------|----------------|-------------------|
| **Device class** | MFDS ‘의료기기법’ classification rules (risk‑based, §5) together with the ‘디지털의료제품법’ for software functions. | *To be confirmed* – if the software is used for diagnosis or monitoring of a physiological parameter it will fall at least in **Class II**; higher risk functions (e.g., therapy recommendation, invasive data handling) may require **Class III**. | • Perform a detailed intended‑use analysis.<br>• Map functional blocks to the MFDS classification matrix (no specific identifier found in source – verify separately). |
| **Submission pathway** | For Class I & II: “신고” (notification); for Class III & IV: “허가” (approval) with full dossier. | *To be determined* after classification decision. | • If Class II, prepare a Korean notification package (품질·안전성 신고).<br>• If Class III, prepare an approval dossier (허가 신청) including GMP certification, clinical evidence, and risk‑management file. |

---

### 2. Evidence Required for a Complete KGMP‑Ready Dossier  

| Requirement | Source citation (as presented) | What must be supplied |
|-------------|------------------------------|-----------------------|
| **KGMP facility certification** | *No specific identifier found in source – verify separately.* (MFDS ‘제조·품질관리 기준’). | Current KGMP certificate, scope of certified processes, and any recent audit reports. |
| **Software Bill‑of‑Materials (SBOM)** | MFDS 보안지침 **제16조** (matched to FDA §524B & MDR Annex I §17.4) – *see DR‑09*. | SBOM meeting the security guideline; version control, component provenance, and vulnerability assessment. |
| **Post‑Market Surveillance (PMS) Plan** | PMS 고시 (referenced in DR‑14) – *no specific notice number supplied*; therefore “verify separately”. | Written PMS SOP, adverse event reporting timeline, and alignment with MFDS PMS regulations. |
| **Unique Device Identification (UDI)** | Medical Device Act + Digital Healthcare Act together (DR‑19). | UDI allocation plan, labeling in Korean, database entry per MFDS UDI specifications. |
| **Risk Management File** | ISO 14971 (full coverage noted in DR‑21). | Complete risk management dossier: hazard analysis, risk evaluation, mitigation measures, and post‑market risk‑control activities. |
| **Software Lifecycle Documentation** | IEC 62304 (fully covered – DR‑22). | Software development plan, verification/validation reports, configuration management, and maintenance procedures. |
| **Usability / Human Factors Evaluation** | IEC 62366‑1 template missing (DR‑06) → *gap*; no concrete citation in source. | Planned usability engineering file, formative/summative testing results, UI design rationale. |
| **Data Integrity Controls (ALCOA+)** | No SOP present (DR‑31) – gap. | SOP describing data capture, storage, traceability, and audit trail meeting ALCOA+ principles. |
| **AI Explainability & Fairness Documentation** | Missing AI explanation / fairness assessment (DR‑32/33). | Model documentation, bias mitigation strategy, explainability report per MFDS AI guidance (if applicable). |
| **Autonomous Performance Certification Playbook** | Absent (DR‑15) – gap. | Regulatory playbook describing autonomous functions, safety case, and verification of self‑learning capabilities. |
| **Drift & Post‑Learning Governance** | No governance framework (DR‑35) – gap. | Procedure for monitoring model drift, re‑validation triggers, and corrective action plan. |
| **Component Performance Evaluation SOP** | Absent (DR‑05) – gap. | SOP describing verification of each software component against performance specifications. |
| **Digital Device Labeling Template** | Missing Korean labeling template (DR‑10). | Completed label draft in Korean covering device name, intended use, UDI, warnings, and manufacturer information. |
| **Independent Software Suitability Evaluation** | Absent (DR‑11). | Independent assessment report confirming that the software meets its intended clinical purpose. |
| **GMP Application Draft** | Partial – GMP suitability assessment draft not prepared (DR‑02). | Completed GMP applicability questionnaire & justification for exemption or inclusion. |
| **PCCP Decision Tree** | Partial – decision tree undecided (DR‑04). | Documented pathway for classifying the product under either medical device law or digital health law. |

---

### 3. Gap Summary (Missing / Incomplete Items)

| DR ID | Nature of Gap | Priority* |
|------|---------------|----------|
| **DR‑05** | No component performance evaluation SOP | **P0** |
| **DR‑10** | Digital medical device labeling template not created (Korean) | P1 |
| **DR‑11** | Independent software suitability assessment missing | P1 |
| **DR‑15** | Autonomous performance certification playbook absent | **P0** |
| **DR‑31** | Data integrity (ALCOA+) SOP missing | P1 |
| **DR‑32/33** | AI explainability & fairness documentation lacking | P1 |
| **DR‑35** | Post‑learning drift governance not defined | **P0** |
| **DR‑02** | Draft GMP suitability assessment not finished | P1 |
| **DR‑04** | PCCP decision tree not finalized | P1 |
| **DR‑06** | IEC 62366‑1 usability plan template missing | P1 |

\*Priority codes as per source: **P0** = critical, immediate remediation; **P1** = important but can be addressed after P0 items.

---

### 4. Core Risk Controls (Mapped to ISO 14971)

| Hazard Area | Control Measure | Evidence Required |
|------------|-----------------|-------------------|
| **Cybersecurity / Vulnerabilities** | SBOM + vulnerability management per MFDS 보안지침 제16조 | SBOM document, patch‑management schedule, penetration test report. |
| **Software Errors & Failures** | IEC 62304 lifecycle controls; unit/integration testing logs | Development plan, verification reports, regression testing records. |
| **Data Integrity (ALCOA+)** | SOP for data capture, storage, audit trail (gap DR‑31) | Completed SOP, sample database logs demonstrating traceability. |
| **AI/ML Model Drift** | Governance process for monitoring drift & re‑training (gap DR‑35) | Drift‑detection algorithm description, scheduled performance review calendar. |
| **Usability Risks** | Human factors engineering per IEC 62366‑1 (gap DR‑06) | Usability plan, mock‑up testing outcomes, corrective action logs. |
| **Labeling & User Information** | Korean labeling template (gap DR‑10) compliant with MFDS labeling rules | Final label graphic, IFU in Korean, verification checklist. |
| **Clinical Performance** | Independent suitability assessment (gap DR‑11) and clinical validation (if Class III) | Clinical evaluation report, comparator study data, predicate device justification. |

---

### 5. Human‑Escalation Triggers  

| Trigger | Reason | Escalation path |
|---------|--------|-----------------|
| **Any P0 gap remains unresolved > 7 calendar days** (DR‑05, DR‑15, DR‑35) | Direct impact on safety & regulatory acceptability. | Immediate notification to Senior RA Manager and Project Lead; create corrective work package with “Urgent” flag. |
| **GMP applicability draft missing (DR‑02)** | Prevents KGMP certification submission. | Escalate to Quality Assurance Director for rapid review and sign‑off. |
| **Absence of UDI plan** (required by 의료기기법 & 디지털의료제품법) | Blocks labeling compliance. | Notify Regulatory Compliance Officer; schedule cross‑functional meeting within 3 days. |
| **AI/ML explainability gaps (DR‑32/33)** when the device employs autonomous decision making | Potential regulatory rejection under MFDS AI guidance (if applicable). | Raise to AI Governance Lead and Senior RA for risk‑based impact assessment. |
| **Post‑market surveillance plan not yet drafted** (PMS 고시) | Legal requirement for all digital health products. | Alert Post‑Market Surveillance Team; set deadline aligned with submission timeline. |

If any of the above triggers are activated, the responsible RA must log an “Escalation Record” in the project’s quality management system and obtain written acknowledgment from the designated authority before proceeding.

---

### 6. Action Summary  

| Immediate (≤ 7 days) | Short‑Term (≤ 30 days) | Long‑Term |
|----------------------|------------------------|-----------|
| – Finalize SBOM & submit to MFDS (DR‑09).<br>– Draft and approve UDI allocation plan (DR‑19).<br>– Close P0 gaps: component SOP (DR‑05), autonomous playbook (DR‑15), drift governance (DR‑35). | – Create Korean labeling template (DR‑10).<br>– Write ALCOA+ data integrity SOP (DR‑31).<br>– Produce AI explainability & fairness doc (DR‑32/33).<br>– Complete IEC 62366‑1 usability plan (DR‑06). | – Establish continuous monitoring of regulatory updates (e.g., future MFDS notices expanding foreign evidence acceptance).<br>– Periodic internal audit of KGMP compliance. |

---

### 7. Peer Review Prompt  

*“@RA‑Team, please review the assumptions underlying the classification decision and the completeness of the listed evidence gaps. Are there any jurisdiction‑specific obligations (e.g., digital‑health specific privacy provisions or recent MFDS notices on foreign clinical data) that are not captured in this draft? Additionally, confirm whether the priority assignments (P0 vs P1) align with our internal risk‑ranking matrix.”*

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 27/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,468자 | — |
| 규제 식별자 인용 | 4개 | — |
| source excerpt 근거 일치 | **4/4 (100%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 0개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 낮음**

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

1. Chunk `1091162552456558927`

> ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버

2. Chunk `434223568197517474`

> ### 3.2 불일치·공백 항목 | Req-ID | 불일치 유형 | 내용 | 우선도 | |---|---|---|---| | DR-05 | 공백 | 구성요소 성능평가 SOP 부재 | P0 | | DR-10 | 공백 | 디지털의료기기 표시기재 템플릿 미작성 | P1 | | DR-11 | 공백 | 독립형 SW 사용적합성 평가 절차 부재 | P1 | | DR-15 | 공백 | 자율성능인증 신청 플레이북 부재 | P0 | | DR-31 | 공백 | 데이터 무결성(ALCOA+) SOP 부재 | P1 | | DR-32/33 | 공백 | AI 설명성·공정성 평가 문서 없음 | P1 | | DR-35 | 공백 | 사후학습·드리프트 거버넌스 없음 | P0 | | DR-02 | 부분 | GMP 적합판정 신청서 초안 미작성 | P1 | | DR-04 | 부분 | PCCP 결정트리 미확정 | P1 | | DR-06 | 부분 | IEC 62366-1 사용적합성 계획서 템플릿 미정 | P1 |

### kb-eval-20260724-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "958f279c248694eb", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `958f279c248694eb`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건...
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

> **Regulatory Draft – Digital Medical Device (GUI‑type Software) – Korean Market**

---

### 1. Regulatory Context & Governing Instruments  

| Item | Source citation |
|------|-----------------|
| MFDS 고시 “디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정” (procedure, documentation, evaluation criteria) | **제2025‑25호** (effective 2025‑04‑15) |
| MFDS 고시 “디지털의료기기의 분류 및 등급 지정 등에 관한 규정” (classification scheme, grade criteria) | **제2025‑23호** (effective 2025‑04‑07) |
| Digital GMP (디지털 GMP 고시) – eight type‑group requirements (including AI/ML) | *Separate 고시* (planned implementation within 2025) – no specific 번호 in source; **verify separately** |
| Amendment to the Enforcement Rules of the Digital Medical Device Act (총리령) | **제2088호** (amended 2026‑01‑23) |

*Framework references* such as “MFDS 고시”, “디지털의료제품법 시행규칙”, and ISO/IEC standards for software life‑cycle (e.g., IEC 62304, IEC 82304‑2) are mentioned to the extent they are established regulatory foundations; no specific clause numbers are required here.

---

### 2. Classification & Submission Route  

| Step | Decision criteria | Outcome |
|------|-------------------|---------|
| **2‑1** Determine intended use & device functionality (GUI that displays patient data, provides decision support but does not make autonomous therapeutic decisions). | Refer to 고시 **제2025‑23호**, which defines class Ⅰ, II, III based on risk impact of software functions. GUI‑type diagnostic/monitoring software without direct therapeutic action typically falls into **Class Ⅱ** (moderate risk) if it provides clinical information that may influence treatment. | **Proposed classification: Class Ⅱ digital medical device** |
| **2‑2** Select regulatory pathway based on class. | MFDS allows three routes for digital products: 허가 (approval), 인증 (certification), 신고 (notification). For Class Ⅱ the standard route is **허가** (marketing authorization) with a full dossier; 신고 applies only to Class Ⅰ low‑risk software. | **Submission route: 허가 (MFDS approval)** |
| **2‑3** Identify applicable dossier template. | 고시 **제2025‑25호** prescribes the required document package for 허가, including technical file, risk management file, clinical evaluation report, and software verification/validation evidence. | Use the “디지털 의료제품 허가 서류” checklist from 고시 제2025‑25호. |

---

### 3. Required Evidence (per 고시 제2025‑25호)  

| Evidence Category | Specific items | Status / Gap |
|-------------------|----------------|--------------|
| **Quality Management System** | KGMP certification for the software type (Digital GMP). Proof of compliance with the eight type‑group GMP requirements (including AI/ML validation if applicable). | *Pending*: Digital GMP 고시 not yet finalised; need confirmation of implementation timeline and certification body. |
| **Software Documentation** | - Software Requirements Specification (SRS) <br> - Architecture Design Document <br> - Source code management plan <br> - IEC 62304‑aligned development lifecycle records <br> - Traceability matrix (requirements ↔ design ↔ verification). | Available – confirm completeness and Korean language translation. |
| **Risk Management** | ISO 14971‑based risk analysis, risk evaluation, residual risk assessment, and post‑market risk plan. Include cybersecurity threat model (per MFDS guidance on digital product security). | Missing: Detailed cybersecurity threat analysis and mitigation plan. |
| **Clinical Evaluation** | Clinical Evaluation Report (CER) that demonstrates safety & performance. Accepted foreign evidence may be used if the MFDS has issued a mutual acceptance notice for the specific clinical data set (e.g., FDA 510(k) predicate or EU CE‑marked device). Must include Korean translation of key conclusions. | Gap: No local clinical data; need to confirm whether existing foreign CER can be leveraged under current MFDS scope (see MFDS periodic “foreign clinical evidence” notices – verify separately). |
| **Usability / Human Factors** | Validation study demonstrating safe use by target users in Korean clinical settings, including UI localization. | Pending: Korean‑language usability test plan and results. |
| **Labeling & IFU** | Full product label, package insert, and Instructions for Use in Korean (per MFDS labeling regulations). Must include safety symbols, storage conditions, and disposal instructions. | Draft available – requires final review by a certified Korean translator. |
| **Software Verification/Validation** | Unit testing, integration testing, system testing reports; performance verification (e.g., latency, accuracy of displayed data). | Available – confirm coverage of AI/ML components if present. |
| **Post‑Market Surveillance (PMS) Plan** | MFDS‑required PMS activities: periodic safety update report, field corrective actions, incident reporting process. | Drafted – need alignment with MFDS 6‑type guideline updates (post‑2025). |

---

### 4. Identified Missing Information & Immediate Actions  

| Missing Item | Reason it is Required | Action |
|--------------|----------------------|--------|
| **Formal KGMP certificate** for the software type | Digital GMP 고시 mandates certification before 허가 submission. | Track implementation schedule (see Monitoring Point 1, “디지털 GMP 고시 시행” – quarterly check) and arrange audit with an authorized KGMP body as soon as the 고시 is published. |
| **Cybersecurity threat model** | MFDS guidance expects explicit controls for data integrity & patient safety in digital products. | Develop a threat analysis per NIST SP 800‑53 or ISO 27001, map mitigations to risk management file; obtain Korean‑language summary. |
| **Local clinical evidence or confirmed acceptance of foreign CER** | Class Ⅱ 허가 requires demonstrable safety/performance data relevant to Korean population unless a MFDS notice explicitly permits reliance on foreign data. | Search MFDS website for the latest “foreign clinical evaluation acceptance” notice (monitoring point 2); if absent, plan a small‑scale Korean clinical usability study. |
| **Korean translation of all technical documents** | All submission dossiers must be submitted in Korean or accompanied by certified translations. | Engage a qualified medical‑device translator; create a translation verification checklist. |
| **Updated labeling per 2026‑01‑23 amendment (총리령 제2088호)** | The recent amendment may introduce new labeling symbols or warnings for digital products. | Review the amendment text; update label drafts accordingly. |
| **Confirmation of submission category (허가 vs 인증)** | Mis‑classifying the route leads to re‑submission and delay. | Conduct a final classification workshop with the product team using 고시 제2025‑23호 criteria; document decision rationale. |

---

### 5. Risk Controls & Mitigation Measures  

| Identified Risk | Control (Design / Process) | Verification |
|-----------------|----------------------------|--------------|
| Incorrect or ambiguous UI leading to user error | Conduct Korean usability testing with target clinicians; implement UI validation rules (e.g., mandatory confirmation dialogs). | Usability test report, IEC 62366‑1 compliance. |
| Data breach / unauthorized access | Implement role‑based authentication, encrypt data at rest/transit per MFDS cybersecurity guidelines; conduct penetration testing. | Pen‑test report, security architecture review. |
| Software malfunction (crash, latency) affecting clinical decision | Apply IEC 62304‐aligned verification/validation; include watchdog timers and fail‑safe modes. | Verification logs, performance benchmarks. |
| Post‑market adverse events not reported in time | Establish SOP for incident detection, internal reporting within 24 h, MFDS notification within required timeframe (typically 7 days). | PMS procedure documentation, audit trail of incidents. |

---

### 6. Monitoring Points & Ongoing Surveillance  

| Monitoring Point | Frequency | Action Required |
|------------------|-----------|-----------------|
| **Digital GMP 고시 시행** – final publication and enforcement schedule | Quarterly | Verify that KGMP certification is obtained before dossier submission. |
| **총리령 제2088호 amendment implementation** (labeling, classification updates) | As‑soon‑as‑available (monitor MFDS website) | Update labeling & classification rationale if new clauses affect the product. |
| **MFDS 6종 가이드라인 후속 개정** – safety and PMS guidance after 2025 | Quarterly | Review updated guide‑lines; refresh PMS plan accordingly. |
| **Additional guideline issuance** (e.g., AI/ML specific) | Monthly check on mfds.go.kr | Incorporate any new requirements into the technical file before final submission. |

---

### 7. Human‑Escalation Triggers  

1. **Classification Ambiguity** – If, after applying 고시 제2025‑23호 criteria, the device could be interpreted as Class Ⅰ or II, a senior RA manager must review and seek MFDS clarification (written inquiry).  
2. **KGMP Certification Gap** – Absence of a valid Digital GMP certificate when the 고시 is in force → escalation to Quality & Compliance leadership for immediate audit planning.  
3. **Foreign Clinical Evidence Rejection** – If MFDS communication indicates foreign CER cannot be used → escalation to clinical development team to design a Korean‑focused clinical study.  
4. **Cybersecurity Deficiency** – Any unresolved high‑severity vulnerability identified in penetration testing must be escalated to the product security lead and postponed submission until mitigation is verified.  
5. **Regulatory Change Notice** – Publication of a new amendment (e.g., further changes to 총리령 제2088호) within 30 days of planned submission → pause submission, inform project manager, and update dossier accordingly.

---

### 8. Reusable RA Judgment (Lesson Learned)

> **When preparing a Korean 허가 dossier for GUI‑type digital medical software, the first decisive step is to verify classification under MFDS 고시 **제2025‑23호**; this determines whether a full 허가 submission is required. Once classified as Class Ⅱ, the complete evidence set prescribed in **고시 제2025‑25호** must be assembled, with particular attention to (a) Digital GMP certification (pending implementation), (b) Korean‑language documentation, and (c) validated acceptance of any foreign clinical data under the latest MFDS “foreign clinical evidence” notice. Continuous monitoring of the quarterly “디지털 GMP 고시 시행”, the amendment **총리령 제2088호**, and MFDS 6‑type guideline updates is essential to flag gaps early and trigger escalation before submission deadlines.**  

---

### 9. Peer Review Prompt

> *Please review this draft and challenge any assumptions regarding (1) the applicability of 고시 제2025‑23호 classification rules to our GUI software, (2) the sufficiency of foreign clinical evidence without a specific MFDS acceptance notice, and (3) the completeness of the risk control matrix given emerging cybersecurity expectations in Korea. Highlight any jurisdiction‑specific gaps that may have been overlooked.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 26/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 10,980자 | — |
| 규제 식별자 인용 | 5개 | — |
| source excerpt 근거 일치 | **0/5 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 5개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `IEC 82304`, `ISO 27001`
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

1. Chunk `1131342938714268388`

> ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건 (AI/ML 포함) | SW GMP 적용 기준 | ---

2. Chunk `385578214769089426`

> ## 5. 모니터링 포인트 | 항목 | 상태 | 확인 주기 | |---|---|---| | 디지털 GMP 고시 시행 | 2025년 내 예정 [검증 필요] | 분기별 확인 | | 디지털의료제품법 시행규칙 개정 (총리령 제2088호) | 2026-01-23 개정 완료 | — | | 추가 가이드라인 제정 | 지속 예고 중 | 월별 mfds.go.kr 확인 | | MFDS 6종 가이드라인 후속 개정 | 2025년 이후 수시 | 분기별 확인 | ---
