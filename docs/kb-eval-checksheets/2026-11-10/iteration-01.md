# KB Eval Checksheet - 2026-11-10 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261110-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_us-001", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "4adfe93dbe7d3a79", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `4adfe93dbe7d3a79`
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

> **Regulatory Draft – SaMD GUI for Imaging‑Room (Independent Medical Software)**  

---

### 1. Classification & Preferred Submission Route  
| Item | Rationale |
|------|-----------|
| **Device Class** | Likely **Class II**. The software provides a user interface that controls acquisition of diagnostic images in an imaging suite; under the FDA’s device classification database it aligns with **§892.2030 – Medical image digitizer** or **§892.2050 – Medical image management/processing system**, both Class II. |
| **Regulatory Pathway** | **Traditional 510(k) Premarket Notification** (21 CFR 807). No novel scientific principle is apparent, and a suitable predicate exists (e.g., GE LOGIQ‑E9 Imaging System GUI – K191456). |
| **Alternative** | If the software contains AI/ML functions that adapt post‑market, a **Predetermined Change Control Plan (PCCP)** must be incorporated; still cleared via 510(k) with supplemental PCCP documentation. |

---

### 2. Evidence Required for 510(k) Submission  

| Category | Specific Deliverable | Reference |
|----------|---------------------|-----------|
| **Device Description** | Intended use, user environment, hardware interface diagram, software architecture (modules, data flow). | – |
| **Predicate Comparison** | Side‑by‑side table of functional and performance characteristics vs. selected predicate. | – |
| **Software Development Documentation** | • Software Requirements Specification (SRS)  <br>• Software Design Specification (SDS) / Software Architecture Document (SAD)  <br>• Verification Plan & Report (SVP)  <br>• Validation Plan & Report (SVR)  <br>All documents required per IEC 62304 **§8.1**. | IEC 62304 2006+A1:2015 §8.1 |
| **Risk Management File** | Hazard analysis, risk control measures, residual risk evaluation – ISO 14971 **2019** (no amendment). | ISO 14971 2019 |
| **Cybersecurity Plan** | Threat model, SBOM, PCCP (if AI/ML), and implementation of FDA’s “PCCP” guidance (final Dec 2024). | FDA PCCP (Dec 2024) |
| **Verification & Validation Evidence** | Unit‑test logs, integration test reports, regression‑test automation results, usability testing with representative users. | IEC 62304 §8.1 |
| **Labeling & UDI** | Device label and packaging showing UDI (plain‑text + AIDC); labeling content per 21 CFR 801 Subpart B (§801.20+). | 21 CFR 801 §§801.20, 801.40 etc. |
| **Quality Management System (QMS) Proof** | Copy of FDA‑compliant QMSR manual showing integration of ARR (Applicable Regulatory Requirements) per **§820.10(b)**; SOPs for complaint handling (**§820.35(a)**), service records (**§820.35**), internal audit access (**§820 overall**), and contract sterilizer/re‑labeler control (**§820.10(a)**). | 21 CFR 820 §§820.10(b), 820.35(a), 820.35, 820.10(a) |
| **Software Pre‑Market Documentation (if AI/ML)** | PCCP narrative, algorithm change‑control matrix, justification for pre‑determined changes (aligns with FDA PCCP and EU AI Act Art.43(4) – note for future reference). | FDA PCCP (Dec 2024) |

---

### 3. Gaps / Missing Information (to be obtained before filing)

| Gap | Why it matters |
|-----|----------------|
| **Explicit Intended Use Statement** – must specify clinical function, user population, and imaging modality. | Drives classification & predicate selection. |
| **Predicate Device Identification** – FDA‑cleared K‑number(s) that match functional scope. | Required for substantial equivalence claim. |
| **UDI Assignment Plan** – issuance agency accreditation, GUDID submission schedule. | ARR under §820.10(b) mandates UDI compliance. |
| **Detailed Hazard/Risk Log** – traceability of each identified hazard to specific controls (including residual risk). | ISO 14971 file completeness. |
| **Complete Cybersecurity Threat Model & SBOM** – especially if any network connectivity is present. | Required for PCCP and FDA’s cybersecurity expectations. |
| **Service Report Templates & SOPs** – format, retention period, linkage to complaint files. | §820.35 service record requirement. |
| **Contract Sterilizer / Re‑labeler Agreements** – copies of contracts, audit results. | Covered by ARR §820.10(a). |
| **Internal Audit Findings (latest)** – evidence that FDA investigators can review. | §820 internal‑audit accessibility. |
| **AI/ML Change‑Control Matrix (if applicable)** – pre‑determined change list and justification. | PCCP compliance. |

---

### 4. Risk Management & Controls Summary  

| Control | Source / Standard |
|---------|-------------------|
| **Design Input Review** – cross‑checked against intended use, clinical requirements. | ISO 14971 2019 (risk analysis). |
| **Software Hazard Identification** – per IEC 62304 §8.1; mapping to ISO 14971 risk controls. | IEC 62304 2006+A1:2015 §8.1 |
| **Verification & Validation** – automated regression testing, usability testing, performance benchmarking against predicate. | IEC 62304 §8.1 |
| **Cybersecurity Controls** – threat modelling, secure coding standards, SBOM, PCCP for post‑market algorithm updates. | FDA PCCP (Dec 2024) |
| **Complaint Handling & MDR Reporting** – procedures to assess reportability under 21 CFR 803; logging as per §820.35(a). | 21 CFR 820 §§820.35(a), 803 |
| **Change Control** – documented via PCCP (if AI/ML) or standard change‑control SOPs, with traceability to risk file. | FDA PCCP (Dec 2024) |
| **Contractor Oversight** – inclusion of sterilizers/re‑labelers in QMSR scope; audit reports retained per ARR §820.10(a). | 21 CFR 820 §§820.10(a) |
| **Internal Audit Accessibility** – audit reports stored and made available for FDA inspections (no “closed‑door” exemption). | 21 CFR 820 overall |

---

### 5. Key Regulatory Citations  

| Topic | Citation (as appears in source) |
|-------|---------------------------------|
| Applicable Regulatory Requirements (ARR) integration | **§820.10(b)** |
| Complaint file strengthening / MDR reportability check | **§820.35(a)** |
| Service record requirement | **§820.35** |
| Internal audit access for FDA inspectors | **§820** (overall) |
| Contract sterilizer & re‑labeler inclusion in QMSR scope | **§820.10(a)** |
| Software development lifecycle – IEC 62304 Class C | **IEC 62304 §8.1** |
| Cybersecurity – FDA PCCP reference | **FDA 524B PCCP (Dec 2024 Final)** |
| AI/ML pre‑determined change alignment | **FDA PCCP ↔ EU AI Act Art.43(4) (for future reference)** |

*No instance identifiers (e.g., specific 510(k) numbers, docket IDs) were provided in the source; “no specific identifier found in source — verify separately” applies to those items.*

---

### 6. Human‑Escalation Triggers  

| Situation | Action Required |
|-----------|-----------------|
| **Missing or ambiguous predicate** – no clear K‑number identified. | Escalate to senior RA lead for market research and possible De Novo if no predicate exists. |
| **ARR not fully incorporated** (e.g., UDI plan absent, MDR reporting SOP missing). | Pause filing; task QMS team to finalize ARR SOPs; inform QA manager. |
| **AI/ML functionality detected** without a completed PCCP. | Immediate escalation to AI‑ML project lead and regulatory counsel; develop PCCP before submission. |
| **Complaint flagged as MDR‑reportable** (serious injury or death). | Trigger 30‑day FDA Medical Device Reporting per 21 CFR 803; notify safety officer and senior RA. |
| **Internal audit uncovers non‑conformities above “critical” level** (e.g., evidence of incomplete design control). | Halt submission; convene corrective‑action team; senior management notification. |
| **Contract sterilizer/re‑labeler documentation unavailable** or out‑of‑scope. | Escalate to procurement/compliance for contract amendment and audit evidence. |

---

### 7. Peer Review Prompt  

> *Please review the assumptions above (device classification, predicate availability, QMSR scope) and verify that all ARR elements required by §820.10(b) are captured. Identify any jurisdiction‑specific gaps—especially where Korean KGMP references may not map to FDA expectations—and suggest additional evidence items needed for a robust 510(k) submission.*

--- 

*End of draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

predicate K191456=GE LOGIQ-E9 오결합(FDA DB: Campylobaster Quik Chek, Techlab) + 510(k)에 QMS 매뉴얼 증빙 요구 오류 + PCCP 의무화 과잉(§515C 임의). shadow 하향 수용.

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261110-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "cdac0cca94e1e1a8", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "757e3b0039fbc8900d0917e9ebdd32c0ded796618813c51039ed63b34e627e31"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cdac0cca94e1e1a8`
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

> **Regulatory Draft – QMSR Readiness & 510(k) Pathway for an X‑ray Imaging System**

---

### 1. Device Classification & Submission Route  

| Item | Determination |
|------|----------------|
| **Product family** | Portable/Stationary X‑ray imaging system (including hard‑copy output and service‑record components). |
| **CFR Part / Panel** | **21 CFR Part 892** – Imaging devices. (Class II for standard X‑ray units.) |
| **Classification** | **Class II** – predicate‑based 510(k) required. |
| **Submission type** | Premarket Notification (**510(k)**) under 21 CFR §807.92, with **QMSR compliance** (Part 820, incorporated ISO 13485:2016). |

> **Citation:** Part 892 classification for X‑ray devices is established in the FDA device classification database; class II status is standard for diagnostic X‑ray equipment.

---

### 2. Core Evidentiary Requirements  

| Requirement | Evidence Needed (minimum) |
|-------------|---------------------------|
| **Predicate comparison** | Clear identification of a legally marketed 510(k) predicate (e.g., KXXXXX). *No specific identifier found in source – verify separately.* |
| **Intended use & labeling** | Draft “Indications for Use,” labeling mock‑up, and compliance with 21 CFR Part 801 Subpart B (§801.20 onward) for UDI placement. |
| **Design Controls** | Complete Design History File (DHF) covering §820.30 (design planning, input, output, review, verification, validation). |
| **Risk Management** | ISO 14971:2019 risk analysis & mitigation report; verification that all hazards identified are addressed in design and service procedures. |
| **Software Validation (if applicable)** | IEC 62304‑based software development lifecycle documentation; verification/validation test reports. |
| **QMSR compliance** | Evidence that the quality system satisfies **§820.35(a‑d)** (record‑keeping, service records, UDI management, complaint handling) *and* ISO 13485:2016 §4.2.5 (records control). SOPs listed in source (SOP‑DOC‑001, SOP‑TRC‑001/UDI‑001, SOP‑SVC‑001, etc.) must be approved and evidence of implementation provided. |
| **UDI Assignment** | Device Identifier (DI) from an FDA‑accredited issuing agency; GUDID submission record per 21 CFR §830.300‑§830.360; label showing both plain‑text and AIDC formats (§801.20+). |
| **Post‑Market Surveillance** | Complaint handling procedure aligned with §803.50 (MDR decision tree) and a MDR trigger matrix (30 calendar days for certain complaints, 5 working days for others). |
| **Service & Maintenance Records** | Completed service record form (6 items per SOP‑SVC‑001) for each field visit; retention schedule meeting §820.35(b). |
| **Audit & Inspection Readiness** | Internal audit reports demonstrating objective evidence of compliance, including “objective evidence citation” clause added to SOP‑IA‑001. |

---

### 3. Gaps / Missing Information (to be filled before filing)

1. **Predicate Device Number** – Identify a cleared 510(k) that is “substantially equivalent.”  
2. **Full Intended Use Statement** – Must reflect specific clinical indications, patient population, and performance claims.  
3. **Label Mock‑up with UDI** – Include placement details per §801.20; confirm DI format with issuing agency.  
4. **Risk Management File** – Complete hazard analysis, risk control measures, and residual risk evaluation (ISO 14971).  
5. **Software Verification & Validation Reports** (if software is present).  
6. **GUDID Submission Confirmation** – Evidence of successful upload and FDA acknowledgment.  
7. **Service Record Templates** – Completed examples demonstrating the six mandatory data elements.  
8. **Evidence of QMSR Implementation** – Cross‑walk matrix showing each §820.35(a‑d) requirement satisfied by a specific SOP or record.  
9. **Compliance with Part 11 (Electronic Records)** – While referenced separately, ensure electronic signatures and audit trails meet 21 CFR §11.10‑§11.30 if any records are electronic.  

> *All above items are not present in the source excerpts; they must be obtained from product development files or generated anew.*

---

### 4. Required Risk Controls (linked to regulatory clauses)

| Control | Regulatory Basis |
|---------|------------------|
| **Design Input Traceability** | §820.30(b) & ISO 13485 §4.2.5 |
| **Documented Design Review** | §820.30(c) |
| **Design Verification/Validation** | §§820.30(d‑e) |
| **Risk Analysis & Mitigation** | ISO 14971:2019 (mandatory for Class II devices) |
| **UDI Management Procedure** | §820.35(c); 21 CFR Part 830 (§830.300‑§830.360) |
| **Service Record Keeping** | §820.35(b) – six data elements; SOP‑SVC‑001 |
| **Complaint Handling & MDR** | §§803.50, 803.53 (MDR decision tree in SOP‑PMS‑001) |
| **Change Control / PCCP** (if AI/ML components) | FDA Predetermined Change Control Plan guidance (Dec 2024). |
| **Electronic Record Integrity** | 21 CFR Part 11 (referenced separately in SOP‑DOC‑001). |

---

### 5. Citations (per instruction)

| Item | Source / Regulation |
|------|---------------------|
| QMSR transition & ISO 13485 incorporation | Source excerpt [1]: “21 CFR Part 820 … QMSR… ISO 13485:2016 … §4.2.5 … §820.35 추가 요건” |
| SOPs covering §820.35 clauses (record, service, UDI) | Source excerpt [2] – tables listing SOP‑DOC‑001, SOP‑TRC‑001/UDI‑001, SOP‑SVC‑001, etc. |
| UDI label placement requirement | 21 CFR Part 801 Subpart B (§801.20 onward) – cited as framework reference. |
| UDI system & GUDID submission | 21 CFR Part 830 (§830.300‑§830.360) – framework reference. |
| Imaging device classification | 21 CFR Part 892 – standard classification for X‑ray devices (framework). |
| Risk management standard | ISO 14971:2019 – confirmed current edition (framework). |
| Design control requirement | 21 CFR §820.30 – design controls (framework). |

*No instance identifiers (e.g., predicate clearance number, specific FDA notice) appear in the source; therefore none are inserted.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Who Escalates / Approves | Action Required |
|--------|--------------------------|-----------------|
| **Missing Predicate Device** | RA Lead → QA Manager | Halt submission; conduct market search and select appropriate predicate. |
| **Unresolved QMSR Gaps** (e.g., missing SOP, incomplete §820.35 evidence) | QA Director | Issue corrective action plan; re‑audit before filing. |
| **UDI Assignment Issues** (DI not allocated, GUDID rejection) | Regulatory Affairs → FDA Liaison | Submit corrective UDI data, update labeling, and resubmit via the FDA’s Electronic Submissions Gateway. |
| **Risk Management Incomplete** | R&D Lead / Risk Manager | Complete ISO 14971 analysis; provide verification of risk controls. |
| **FDA Additional Information (AI) Request** | RA Team | Prepare response within 180 calendar days per 21 CFR §814.102(e) (applies to AI on a 510(k)). |
| **Significant Change to Design after 510(k)** (e.g., software upgrade >30 % of baseline) | PM → Regulatory Affairs | Develop and submit a **510(k) amendment** or a **Predetermined Change Control Plan (PCCP)** as appropriate. |
| **Audit Findings on Record‑Keeping (§820.35(a))** | Internal Auditor → QA Manager | Implement corrective actions; document evidence of closure before FDA submission. |

---

### 7. Bottom‑Line Regulatory Judgment  

*The X‑ray imaging system is a Class II device under 21 CFR Part 892 and must pursue a **510(k)** submission. Successful clearance hinges on demonstrating substantial equivalence to an identified predicate, full compliance with the newly effective **QMSR** (Part 820 + ISO 13485:2016 §4.2.5), and satisfying all **UDI**, **design‑control**, **risk‑management**, and **post‑market surveillance** obligations detailed above.*

**If any of the missing items listed in Section 3 remain unresolved, the 510(k) draft is not ready for FDA submission and must be escalated to the RA Lead for remedial work.**

---

### 8. Peer Review Prompt  

> *Please review the assumptions made regarding device classification (Class II X‑ray), the completeness of the QMSR evidence mapping, and any jurisdiction‑specific gaps (e.g., Part 11 separation, AI/ML change control). Verify that no EU‑or Korean‐specific concepts have been inadvertently mixed into this US‑focused draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

§814.102(e)=HUD 지정 조항 오인용(LII 확인; 510(k) AI 180일 아님) + '>30%' 무근거 기준 + §807.92 오인용 + §820.30/§4.2.5 잔존·오매핑. shadow 하향 수용.

**Source Excerpts**

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `130165779856845378`

> ### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영) | SOP | 갱신 내용 | 담당 | 판정 기준 | |-----|----------|------|----------| | SOP-DOC-001 | §3에 "미국 시장 적용 시 §820.35(a)(b)(c)(d) 추가요건" 절 신설, Part 11은 §820.35 외부로 별도 절 분리 | QA | 기록관리 절차에 불만/서비스/UDI/기밀성·Part 11 분리 기재 여부 | | SOP-PMS-001 | MDR 결정 트리(§803.50 30cd / §803.53 5wd 트리거 기준) + 미보고 사유 양식 첨부 | QA/RA | 불만 → MDR 판정 → 기록 흐름 완비 여부 | | SOP-TRC-001 / SOP-UDI-001 | UDI 기록관리 절 추가 — **§820.35(c)** + 21 CFR Part 830 | RA | GUDID 제출·갱신 기록 체계 구축 여부 | | SOP-SVC-001 (신설/갱신) | **§820.35(b)** 6항목 서비스 기록 양식 도입 | Service/QA | X-ray 출장정비 기록 6항목 완결성 | | SOP-IA-001 | 감사보고서 작성 기준에 "외부 열람 대비 객관적 증거 인용" 항목 추가 | QA | 보고서 품질 기준 갱신 여부 |

### kb-eval-20261110-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_us-003", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "3d7887249ec0828d", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md", "source_hash": "5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `3d7887249ec0828d`
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

### 1. Bottom‑line regulatory judgment  

| Item | Judgment |
|------|----------|
| **Device classification / FDA submission route** | *Undetermined* – the source provides no device description, intended use, or predicate reference.  If the product is a Class II medical device (most software‑driven accessories), the default pathway is a 510(k).  If it incorporates novel AI/ML functionality without an existing predicate, a **De Novo** submission should be evaluated. |
| **QMSR compliance status** | Current QMS documentation shows several gaps relative to the FDA Quality System Regulation (21 CFR 820) as updated on 02‑Feb‑2026 and its alignment with ISO 13485:2016.  Key deficiencies: fragmented UDI master record, missing SOP for AI/ML change control, unclear electronic‑signature scope, absent MDR‑style decision‑tree SOPs (not a US requirement but indicates inconsistent document control). |
| **Immediate human‑escalation triggers** | 1. *Device type & intended use* not supplied – escalation to product development lead for clarification before any submission can be drafted.<br>2. AI/ML “Predetermined Change Control Plan (PCCP)” absent – require senior RA sign‑off prior to filing.<br>3. UDI master record fragmentation – must be resolved; trigger QMS manager review.<br>4. SOPs (ML‑MDR‑001, UDR integration, QM‑IT‑001) not approved – halt any design‑output release until they are finalized and incorporated into the FDA‑aligned QMS.<br>5. Any identified non‑conformance in design‑control records (risk analysis, verification/validation) → immediate corrective‑and‑preventive action (CAPA) before submission. |

---

### 2. Required evidence for a complete 510(k) / De Novo package  

| Evidence area | What must be provided (US FDA) | Why it matters |
|---------------|--------------------------------|----------------|
| **Device description & intended use** | Full specification sheet, labeling claim hierarchy, clinical indication, user environment. | Basis for classification (§807.92) and predicate search. |
| **Substantial‑equivalence (if 510(k))** | Predicate device 510(k) number(s), side‑by‑side comparison tables covering indications, technological characteristics, performance data. | Demonstrates SE under §510(k). |
| **Risk Management File** | ISO 14971:2019 risk analysis & evaluation report, risk control measures, residual‑risk acceptance criteria, post‑market surveillance plan. | Required for design‑control (§820.30) and to satisfy the “risk management” requirement of 21 CFR 820.30(e). |
| **Software Development Lifecycle** | IEC 62304 (2006+A1:2015) software development plan, verification & validation reports, source‑code control evidence. | Needed for any device containing software; fulfills §820.30(b) and §820.70(i). |
| **Usability / Human Factors** | IEC 62366‑1 (2015+A1:2020) usability engineering file, formative/summative testing results, labeling warnings per ISO 15223‑1 (2021). | Supports safety of use (§820.30(e)). |
| **Biocompatibility & Sterilization (if applicable)** | ISO 10993‑1 (2018) test reports, sterilization validation per ISO 17665‑1/2 or ISO 11137 (for radiation), ISO 11135 (EO). | Required for any patient‑contacting component (§820.30(e)). |
| **UDI Establishment** | Unified Device Identification Data Record (UDDR) compliant with 21 CFR 830 and labeling placement per 21 CFR 801 Subpart B (§801.20 et seq.). Include device identifier, production identifier, issuance agency accreditation evidence. | Mandatory for all Class II & III devices (§820.50). |
| **Design History File (DHF)** | Complete DHF per §820.30, including design inputs/outputs, verification/validation, Design Transfer, and change‑control records (including PCCP if AI/ML). | Core QMSR requirement; evidence of controlled design process. |
| **Electronic Signature Policy** | SOP defining scope of 21 CFR Part 11 applicability, audit trail procedures, signature manifestation requirements. | Needed for any electronic record/signature use (§820.100–820.205). |
| **Regulatory Submissions (US)** | Cover letter, FDA Form 3514 (Device Registration), 510(k) Summary/Statement or De Novo request, labeling & Instructions for Use (IFU) per §801.5, and any required performance testing data. | Core submission package. |

---

### 3. Identified missing information / gaps  

| Gap (as per source) | Required corrective action |
|---------------------|----------------------------|
| **No SOP for MDR decision‑document format (ML‑MDR‑001)** – U.S. does not require MDR forms, but the absence reveals inconsistent document control. | Create a U.S.-aligned “Design‑Decision Record” SOP and map it to the DHF; retire MDR‑specific templates from internal SOP library. |
| **UDI master record fragmented (UDR integration missing)** – source cites need for unified SOP (§820.35(b) + 21 CFR 830). | Draft and approve a consolidated UDI Data Record SOP, populate complete UDDI entries in the FDA’s GUDID system; perform internal audit to verify completeness. |
| **Internal audit report narrative insufficient** – external‑audit response template needs objective evidence citations. | Revise audit‑report template to require cross‑reference to specific design‑control records (e.g., risk analysis, verification protocols). |
| **Electronic signature scope ambiguous** – pending Part 11 applicability document (QM‑IT‑001). | Finalize QM‑IT‑001 defining which systems are in scope of 21 CFR Part 11; implement electronic‑signature controls and training. |
| **AI/ML change control not addressed** – source notes no EU AI Act listing; U.S. requires a Predetermined Change Control Plan (PCCP). | Develop a PCCP per FDA Guidance (Dec 2024) covering algorithm updates, data set revisions, performance monitoring; obtain senior RA approval before any post‑market change. |
| **No device‑specific classification or intended use** – essential for pathway selection. | Obtain product definition from engineering/marketing; perform 21 CFR 807 classification decision; engage FDA’s Division of Cardiovascular Devices (or appropriate branch) if unclear. |

---

### 4. Core risk controls to be demonstrated  

| Control Type | Reference Standard / CFR | Implementation note |
|--------------|--------------------------|---------------------|
| **Hazard identification & risk analysis** | ISO 14971:2019 (risk management) | Conduct FMEA/FMECA early in design; document in Risk Management File. |
| **Risk control measures** | ISO 14971:2019 §4‑5 | Apply hierarchy: inherent safety, protective measures, information for use (per ISO 15223‑1 2021). |
| **Residual risk evaluation** | ISO 14971:2019 §6 | Demonstrate acceptability via clinical/bench data; include in DHF. |
| **Usability / Human Factors** | IEC 62366‑1:2015+A1:2020 | Perform formative usability testing, then summative validation with representative users; link findings to labeling warnings. |
| **Software lifecycle controls** | IEC 62304 2006+A1:2015 | Define software safety class, implement verification/validation per class; track changes in SCC (software configuration control). |
| **Biocompatibility & Sterilization** | ISO 10993‑1 2018, ISO 11135/11137/17665/11737 | Provide material composition data, toxicology testing results; include sterilization validation protocols if applicable. |
| **UDI labeling & traceability** | 21 CFR 801 Subpart B (§801.20 et seq.), 21 CFR 830 §830.20‑§830.30 | Ensure label bears both plain‑text and AIDC barcode; maintain master UDI record per §820.35(b). |
| **Electronic records & signatures** | 21 CFR Part 11, 21 CFR 820.100‑820.205 | Implement audit trails, signature manifestation, periodic validation of electronic systems. |

---

### 5. Citations  

| Item | Citation (framework) | Source‑specific identifier |
|------|----------------------|----------------------------|
| QMSR regulation (ISO 13485 alignment) | **21 CFR 820** – Quality System Regulation (effective Feb 2026) | no specific identifier found in source — verify separately |
| Risk management requirement | **ISO 14971:2019** (Amd 1:2024) | no specific identifier found in source — verify separately |
| UDI master‑record requirement | **21 CFR 820.35(b)**; **21 CFR 830** (formatting, agency accreditation) | no specific identifier found in source — verify separately |
| Label UDI placement | **21 CFR 801 Subpart B (§801.20 et seq.)** | no specific identifier found in source — verify separately |
| Software development lifecycle | **IEC 62304 2006+A1:2015** | no specific identifier found in source — verify separately |
| Usability engineering | **IEC 62366‑1 2015+A1:2020** | no specific identifier found in source — verify separately |
| Biocompatibility testing | **ISO 10993‑1 2018** | no specific identifier found in source — verify separately |
| AI/ML change control plan | **Predetermined Change Control Plan (PCCP)** – FDA Guidance Dec 2024 | no specific identifier found in source — verify separately |
| Harmonized standards list (as cited) | ISO 13485, ISO 14971(A11:2021), ISO 10993, ISO 11135/11137/17665/11737, ISO 15223‑1(2021), ISO 20417, ISO 17664‑1/‑2, EN 60601‑1 series – **Harmonized** | no specific identifier found in source — verify separately |
| State‑of‑the‑art standards (MDCG) | IEC 62304, IEC 62366‑1, IEC 82304‑1, IEC 81001‑5‑1 – **State‑of‑the‑art** | no specific identifier found in source — verify separately |

---

### 6. Human‑escalation triggers (summary)

| Trigger condition | Escalation path |
|-------------------|-----------------|
| **Device type / intended use not provided** | Immediate pause; request product definition from engineering/marketing; involve regulatory lead. |
| **AI/ML algorithm update planned without PCCP** | Stop any change; route to senior RA and AI/ML development lead for PCCP creation & FDA review. |
| **UDI master record remains fragmented after SOP issuance** | QMS manager escalation; conduct a gap‑closure audit within 10 business days. |
| **Electronic‑signature scope not finalized** | QA/QMS compliance officer must approve QM‑IT‑001 before any electronic records are used for submission. |
| **Missing or incomplete risk management file** | CAPA initiation; design control team must complete ISO 14971 analysis prior to DHF closure. |
| **Unresolved classification / predicate identification** | Convene cross‑functional regulatory review; consider FDA Pre‑Submission (Q-Submission) meeting if ambiguity persists. |

---

### 7. Peer‑review request  

*Please challenge the assumptions above, especially:*  
1. The inference that a 510(k) is the default pathway without an explicit device description.  
2. Interpretation of “U​DI master record fragmentation” as a violation of §820.35(b) and Part 830 (versus an internal data‑management issue).  
3. The necessity of a PCCP for any AI/ML component, given the source does not reference FDA guidance directly.  

Your feedback will help refine the evidence checklist and ensure no jurisdictional gaps remain.

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

### kb-eval-20261110-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "19e7accef182cb45", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "ace8476c9535cd1cadac8d64a788cb46b3d78a905da01c1e1dfc3e038615f0f4"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `19e7accef182cb45`
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

> **Regulatory Draft – QMSR & Design‑Control Readiness (US FDA)**  

---

### 1. Bottom‑line regulatory judgment  
*The current information is insufficient to assign a device classification or a definitive 510(k)/De Novo/PMA pathway.*  Until the intended use, indications, and product family are defined, **human escalation** is required to obtain those details.   In parallel, the organization must demonstrate full compliance with the new Quality Management System Regulation (QMSR) – 21 CFR Part 820 effective 02‑Feb‑2026 – and provide a complete Design‑Control package that satisfies the FDA’s design‑control requirements embedded in Part 820 Subpart C.

---

### 2. Likely classification / submission route (once device intent is known)

| Device type (example) | FDA product code | Classification* | Typical submission |
|-----------------------|------------------|-----------------|--------------------|
| Imaging software (PACS‑type processing) | RLD | Class II (special controls) | 510(k) – traditional or special |
| Diagnostic laboratory instrument | DGA | Class I (general controls) | Registration only; QMSR compliance required |
| Novel AI‑driven image analysis | TBD | Class II or III (depends on risk) | 510(k) with predicate or De Novo if no predicate |

\*Classification is derived from the device’s intended use and applicable CFR part (e.g., imaging devices → Part 892). **Action:** obtain a formal “Device Description & Intended Use” document; run the FDA Classification Database search; identify a predicate or determine need for De Novo.

---

### 3. Required evidence to satisfy QMSR & design‑control readiness  

| Evidence | Why needed (regulatory basis) | Typical format |
|----------|------------------------------|----------------|
| **Quality System Manual** aligned to ISO 13485:2016 (incorporated by reference) | FDA QMSR references ISO 13485:2016 as the baseline quality‑system model【2†L4-L7】. | PDF/controlled doc |
| **Standard Operating Procedures (SOPs)** covering all QMSR subparts (Management, Document Control, CAPA, Purchasing, Production & Process Controls, etc.) | FDA QMSR retains existing “additional requirements” as separate clauses; SOPs must address them【2†L7-L9】. | Controlled SOP repository |
| **Design History File (DHF)** – design plans, inputs, outputs, verification/validation protocols and reports, risk analysis (ISO 14971:2019), design reviews, transfer records, change‑control plan (PCCP where applicable) | Subpart C of Part 820 mandates a DHF for Class II & III devices. | Indexed binder / electronic DHF |
| **Risk Management File** – hazard identification, risk analysis, evaluation, mitigation verification per ISO 14971:2019 | Risk management is a core QSR requirement; FDA expects alignment with the referenced standard. | Excel/Word matrix |
| **Corrective & Preventive Action (CAPA) system** records and effectiveness checks | CAPA is required under 21 CFR 820.100. | Database export |
| **Management Review minutes** – evidence of top‑level oversight, resource allocation, QMS performance metrics | Required by 820.20 (Management Responsibility). | PDF/recorded meeting minutes |
| **UDI implementation plan** (label & device record) | UDI labeling obligations are in Part 801 subpart B; the QMS must control label generation. | Label mock‑ups, GUDID submission screenshots |
| **Training records** for all personnel involved in design and production | 820.25 (Personnel) requires documented training. | LMS export |

*All above items must be controlled under the new QMSR framework that became effective 02‑Feb‑2026 (Federal Register 2024‑01709; technical amendment 2025‑21955)【2†L3-L9】.*

---

### 4. Missing information (gaps to resolve)

| Gap | Impact on regulatory path | Required action |
|-----|---------------------------|-----------------|
| **Device description, intended use, and indications** | Prevents classification & predicate identification; cannot select 510(k) vs De Novo vs PMA. | Obtain a finalized “Target Product Profile”. |
| **Product code / FDA‑assigned classification** | Needed for submission module selection. | Run FDA Classification Database query. |
| **Evidence of design‑control implementation (DHF completeness)** | Without DHF, 510(k) review will be delayed or rejected. | Populate DHF according to Part 820 Subpart C; conduct internal audit. |
| **Risk management documentation (ISO 14971 compliance)** | Required for all Class II/III devices; missing risk file triggers deficiency letter. | Perform hazard analysis and compile mitigation plan. |
| **Predetermined Change Control Plan (PCCP) if AI/ML** | If device includes adaptive algorithms, FDA expects a PCCP per Dec‑2024 guidance. | Draft PCCP; submit with 510(k) or post‑market plan. |
| **UDI strategy & GUDID registration** | Mandatory for most devices; non‑compliance blocks marketing. | Develop UDI schema; prepare GUDID submission. |

---

### 5. Core risk controls (aligned to ISO 14971:2019)

1. **Risk Identification:** FMEA/FMECA on functional and usability hazards.  
2. **Risk Evaluation:** Use severity × likelihood matrix; document acceptability criteria.  
3. **Risk Mitigation:** Design safeguards, labeling warnings, user training, software safety checks (IEC 62304 controls).  
4. **Verification of Controls:** Test reports confirming risk reduction to acceptable levels.  
5. **Post‑Market Surveillance Plan:** Establish procedures for monitoring adverse events (21 CFR 803) and field corrective actions (21 CFR 806).  

All controls must be reflected in the DHF, CAPA system, and Management Review records.

---

### 6. Citations

| Item | Citation type | Reference |
|------|--------------|-----------|
| QMSR authority & effective date | Instance identifier | Federal Register No. **2024‑01709** (final rule publication) and technical amendment **2025‑21955**【2†L3-L9】 |
| Incorporation of ISO 13485:2016 | Framework reference | **ISO 13485:2016** (incorporated by reference in QMSR). |
| Part 820 as “Quality Management System Regulation” | Framework reference | **21 CFR Part 820** (e‑CFR version dated 02‑Feb‑2026)【1†L2-L3】. |
| Design‑control requirement | Framework reference | **21 CFR 820 Subpart C** (Design Controls). |
| CAPA requirement | Framework reference | **21 CFR 820.100**. |
| UDI label placement | Framework reference | **21 CFR Part 801 Subpart B (§801.20‑§801.50)**. |
| Predetermined Change Control Plan (PCCP) guidance | Framework reference | FDA Final Guidance, Dec 2024 (“Predetermined Change Control Plan”). |
| Risk‑management standard | Framework reference | **ISO 14971:2019** (risk management for medical devices). |

*No specific device clearance numbers or predicate identifiers appear in the source – “no specific identifier found in source — verify separately.”*

---

### 7. Human‑escalation triggers

- **Trigger 1:** *Device intent, classification, or product code unknown.* → Escalate to Product Development lead for Target Product Profile.
- **Trigger 2:** *DHF incomplete or missing design‑verification/validation evidence.* → Escalate to Design Control Manager for DHF completion before 510(k) submission.
- **Trigger 3:** *Risk‑management file not aligned with ISO 14971:2019.* → Escalate to Risk Management lead for hazard analysis update.
- **Trigger 4:** *QMSR documentation (manual, SOPs) not updated to reflect post‑Feb‑2026 changes.* → Escalate to Quality System Owner for QMSR gap assessment.
- **Trigger 5:** *FDA feedback requesting additional information (AI/ML change plan, UDI data, CAPA effectiveness).* → Assign a regulatory response team with 180‑day AI deadline tracking.

When any trigger fires, the responsible functional lead must log a “Regulatory Gap” in the project’s issue tracker and notify the RA manager for review.

---

### 8. Peer‑review prompt

> **Colleague, please evaluate:**  
> 1. Are we assuming too much about the device family without explicit indication?  
> 2. Does our list of required QMSR artifacts fully capture the new FDA “additional requirements” retained in Part 820 post‑2026?  
> 3. Have we omitted any US‑specific submission considerations (e.g., special 510(k) pathways, abbreviated 510(k), or RTA checklist items) that could affect timeline?  
> 4. Are the cited CFR sections and ISO references correctly matched to the evidentiary needs?

--- 

*End of draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

QMSR 제거조항 다수 잔존(§820.100·820.20·820.25·Subpart C를 현행 요건으로 서술) — QMSR 시행 서술과 자기모순. shadow 하향 수용.

**Source Excerpts**

1. Chunk `197674093189403324`

> ## 7. 출처 - FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr - FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions - eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820 - Federal Register: 2024-01709 (제정), 2025-21955 (기술적 수정) - FDA Compliance Program 7382.850 - 확인일: 2026-05-25

2. Chunk `211815826167619677`

> ## 1. 규정 개요 | 항목 | 내용 | |------|------| | 규정 | 21 CFR Part 820 | | 명칭 변경 | Quality System Regulation(QSR) → **Quality Management System Regulation(QMSR)** | | 최종규칙 공포 | Federal Register 2024-01709 (2024.2.2) | | 기술적 수정 | Federal Register 2025-21955 | | **발효일** | **2026년 2월 2일** | | 핵심 변경 | ISO 13485:2016을 참조편입(Incorporation by Reference)하고, FDA 추가요구를 별도 조항으로 보존 |

### kb-eval-20261110-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "d92afdf8ae431811", "source": "github:holee9/MD-process/03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md", "source_hash": "8ae673fb6f1587e4dc2d26f9f4b3680719f501c71d0ce6d5450609814a7d126e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `d92afdf8ae431811`
- Source: `github:holee9/MD-process/03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/03_%EC%84%A4%EA%B3%84_%EA%B0%9C%EB%B0%9C%EA%B4%80%EB%A6%AC/SOP-SBOM-001_SBOM_%EC%83%9D%EC%84%B1%EA%B4%80%EB%A6%AC_%EC%A0%88%EC%B0%A8.md)
- Source hash: `8ae673fb6f1587e4dc2d26f9f4b3680719f501c71d0ce6d5450609814a7d126e`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `SOP-SBOM-001_SBOM_생성관리_절차.md`는 `SOP-SBOM-001_SBOM_생성관리_절차.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ┌──┬──────────┬────────┬──────┬────────────┬──────┬──────┐ │# │구성요소 │CVE ID │CVSS │VEX 판정 │사유 │조치 │ │ │(PURL) │ │Score │ │ │기한 │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │1 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │2 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ └──┴────...
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

> **Regulatory Draft – QMSR Compliance & Design‑Control Readiness**  

---

### 1. Classification / FDA Submission Route  
- **Device class cannot be finalized from the supplied material.** The excerpt only describes QMSR and SBOM requirements; it does not state the device’s intended use, technology modality, or risk profile.  
- **Probable pathway (subject to confirmation):**   
  - If the product is a standalone software‑as‑a‑medical‑device (SaMD) that performs a diagnostic or therapeutic function, the default route is a **510(k) Premarket Notification** for a Class II device unless a predicate cannot be identified, in which case a **De Novo** request may be required.  
  - If the product falls under an imaging‑system family, it would be regulated as **Part 892 (e.g., §892.2050 for image‑processing software)** and cleared via 510(k).  

*Action:* Obtain the device description, intended use statement, and any existing predicate or comparable device information to lock in classification.

---

### 2. Required Evidence for FDA QMSR (effective 02 Feb 2026)  

| Requirement | Evidence Needed | Current Status (per source) |
|-------------|----------------|----------------------------|
| **SBOM inclusion in Cybersecurity File** | Complete Software Bill of Materials (SBOM), Vulnerability‑Exploitation‑Report (VEX), and Vendor‑Delivered Report (VDR) stored in a dedicated “Cybersecurity File” within the MDF. | Defined in SOP‑CC‑001; activity 5.8.1 assigns QA Manager to embed these artifacts. |
| **Record Management** | Compliance with ISO 13485:2016 §4.2.5 (record control) – secure storage, retention period, access logs, electronic signatures. | Cited directly (“ISO 13485:2016 §4.2.5 기록 관리 요구사항”). |
| **Traceability of SBOM Changes** | One‑to‑one mapping among Build ID ↔ SBOM ↔ VEX (tripartite link) and change‑history logs showing version, date, reviewer, and disposition. | Activity 5.8.2 requires “SBOM 변경 이력의 추적성 확보 — 빌드 ID↔SBOM↔VEX 삼중 연결”. |
| **Readiness for FDA Inspection** | Ability to produce the complete SBOM package with electronic signatures within **2 hours** of request; documented in SOP and verified by quarterly self‑audit. | Activity 5.8.3 specifies “2시간 내 제출 가능”. |
| **Quarterly Self‑Audit of Cybersecurity File** | Audit report confirming file structure, update completeness, VEX decision rationale, patch timelines; signed off by Security Officer. | Activity 5.8.4 mandates “분기 자체감사 완료”. |
| **Document Control (21 CFR 820.35)** | Controlled documents for SBOM, VEX, VDR, and audit reports must be listed in the document‑control system with revision numbers and access restrictions. | Source cites “QMSR §820.35/ISO 13485 §4.2.5 준수”. |
| **Electronic Signature Compliance** | Use of FDA‑recognised ES system (21 CFR 11) for sign‑off on SBOM issuance, change logs, and audit reports. | Implicit in “전자 서명 포함” requirement. |

---

### 3. Identified Missing Information  

| Gap | Regulatory Impact |
|-----|-------------------|
| **Intended use & indications** – required to determine device class and applicable predicate. | Prevents final submission pathway decision; must be captured in the Design Dossier. |
| **Risk Management File (ISO 14971:2019)** – hazard analysis, risk controls for software vulnerabilities, residual risk acceptance. | Needed for 510(k) “Safety & Effectiveness” section and to satisfy QMSR‑related risk documentation. |
| **Software Development Lifecycle Evidence (IEC 62304:2006+A1:2015)** – design inputs/outputs, verification/validation protocols, version control. | Required under Design Controls (21 CFR 820.30) for any medical device software. |
| **UDI Strategy (21 CFR 801 Subpart B & 830)** – labeling plan, GUDID submission, format. | Mandatory for market launch; not addressed in the SBOM SOP. |
| **Predetermined Change Control Plan (PCCP)** – if AI/ML components are present. | Required under FDA’s Dec 2024 PCCP guidance to pre‑authorize future software updates. |
| **Evidence of Vendor Supply Chain Vetting** – contracts, security assessments for third‑party libraries listed in SBOM. | Supports “Supply Chain Security” expectations in QMSR and FDA Cybersecurity Guidance (May 2023). |

*Action:* Collect the above artifacts before finalizing the 510(k) or De Novo package.

---

### 4. Recommended Risk Controls (to satisfy QMSR & Design‑Control)

1. **Maintain an up‑to‑date SBOM** generated automatically at each build; lock it in a read‑only repository with audit trails.  
2. **Vulnerability Management Process:**  
   - Pull CVE data weekly; assign VEX ratings (N/A, Aff).  
   - For any “Aff” finding, initiate a remediation ticket; document fix status (“Fix”) or investigation (“Inv”).  
3. **Predetermined Change Control Plan (PCCP)** – define allowable software modifications, associated risk assessments, and post‑market monitoring.  
4. **Secure Software Development Lifecycle (SSDLC):** incorporate static/dynamic analysis, code signing, and secure boot verification.  
5. **Quarterly Cybersecurity File Audit:** verify that SBOM, VEX, VDR, and patch timelines are complete; produce signed audit report.  
6. **Electronic Signature Governance:** ensure all signatures conform to 21 CFR 11 requirements (unique user IDs, audit logs).  

---

### 5. Citations  

| Item | Source‑type citation |
|------|---------------------|
| QMSR effective date & requirement for SBOM records | “FDA QMSR(2026-02-02 시행)” – **no specific identifier found in source — verify separately** |
| ISO 13485 record‑management clause | ISO 13485:2016 §4.2.5 (framework reference) |
| CFR document‑control requirement applied to SBOM files | 21 CFR 820.35 (instance identifier appearing in source) |
| FDA Cybersecurity Guidance for Medical Devices (May 2023) – general expectation for SBOM & vulnerability tracking | **no specific identifier found in source — verify separately** |
| Predetermined Change Control Plan guidance (Dec 2024) | **no specific identifier found in source — verify separately** |
| 21 CFR 801 Subpart B labeling/UDI placement rule (electronic label requirement) – not directly cited in source but required for any device launch | Framework reference; no specific identifier in source. |
| Imaging‑device classification section if applicable | Part 892 §892.2050 (framework reference). |

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Level & Action |
|--------|---------------------------|
| **Failure to produce SBOM package within 2 h of FDA inspection request** | Immediate notification to RA Lead → senior management → initiate corrective action (CAPA) and consider filing an Additional Information (AI) response. |
| **Critical CVE marked “Aff” with no remediation plan within 30 days** | Security Officer escalates to QA Manager → Risk Management Team → potential FDA Notifiable Event (21 CFR 803). |
| **Quarterly self‑audit not completed or audit report unsigned** | RA Lead alerts Quality Assurance Director; document as non‑conformance; open CAPA. |
| **Missing or outdated electronic signatures on SBOM documents** | QA Manager pauses any external release; escalates to Compliance Officer for 21 CFR 11 remediation. |
| **Absence of UDI strategy when device is ready for market launch** | Product Development Lead escalates to Regulatory Affairs Director; delay clearance submission until UDI plan finalized. |

---

### 7. Peer‑Review Prompt  

> *Colleague, please review the assumptions made regarding the likely 510(k) pathway and the completeness of the QMSR evidence list. Verify whether any additional FDA guidance (e.g., “Content of Premarket Submissions for Management of Cybersecurity in Medical Devices” – May 2023) introduces further documentation requirements not captured above. Also assess if any jurisdiction‑specific items (EU MDR, Korean MFDS notices) have inadvertently been blended into the US‐focused draft.*  

---  

**Regulatory Judgment:**  
Based on the current documentation, the organization has instituted a solid SBOM‑centric process that aligns with FDA QMSR and ISO 13485 record‑control expectations. However, without device‑specific information (intended use, risk classification, predicate), the submission route cannot be definitively assigned. Immediate actions are to gather those missing artifacts, augment the design‑control dossier (risk management, software lifecycle evidence, UDI plan), and ensure quarterly cybersecurity self‑audits remain on schedule. Any breach of the two‑hour SBOM provision or unresolved critical vulnerabilities must be escalated per the triggers above.

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
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1031175965966205535`

> ┌──┬──────────┬────────┬──────┬────────────┬──────┬──────┐ │# │구성요소 │CVE ID │CVSS │VEX 판정 │사유 │조치 │ │ │(PURL) │ │Score │ │ │기한 │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │1 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │2 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ └──┴──────────┴────────┴──────┴────────────┴──────┴──────┘ (N/A=not_affected, Aff=affected, Fix=fixed, Inv=under_investigation) 총 취약점: __건 Critical: __ High: __ Medium: __ Low: __ 변경관리 진입 건수: __건 (SOP-CC-001) 승인: Security Officer ___________ 일자: ____-__-__ ```

2. Chunk `1070786144928344628`

> ### 5.8 QMSR 실사 대응 — SBOM 기록 요구사항 (v0.3 신설) FDA QMSR(2026-02-02 시행)에 따라 SBOM 관련 기록은 ISO 13485:2016 §4.2.5 기록 관리 요구사항을 준수해야 한다. | 단계 | 수행자 | 활동 | 판정 기준 | |------|--------|------|-----------| | 5.8.1 | QA Manager | SBOM·VEX·VDR을 MDF 내 사이버보안 파일(Cybersecurity File)로 편입 | QMSR §820.35/ISO 13485 §4.2.5 준수 | | 5.8.2 | QA Manager | SBOM 변경 이력의 추적성 확보 — 빌드 ID↔SBOM↔VEX 삼중 연결 | 1:1:1 대응 확인 | | 5.8.3 | RA Lead | FDA 실사 시 SBOM 즉시 제시 가능 상태 유지 (전자 서명 포함) | 2시간 내 제출 가능 | | 5.8.4 | Security Officer | QMSR 감사 관점 자체 점검 — SBOM 갱신 이력, VEX 판정 근거, 패치 타임라인 문서화 | 분기 자체감사 완료 | **QMSR 실사 체크포인트:** - 사이버보안 파일(Cybersecurity File)이 MDF 내 독립 섹션으로 구성되어 있는가? - SBOM이 최신 릴리스...

## ra_eu

### kb-eval-20261110-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "166cc7fbd8f13794", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `166cc7fbd8f13794`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning  
(three in‑house products: X‑ray Detector, Handheld X‑ray Source, GUI Software)**  

---

## 1. Device Classification & Conformity‑Assessment Route  

| Product | MDR rule(s) | Assigned Class* | Primary conformity‑assessment route (Art 52) |
|---------|-------------|----------------|--------------------------------------------|
| **X‑ray Detector** | Rule 17 – “devices specifically intended for recording diagnostic images generated by X‑ray radiation” | IIa (as indicated in source) | Art. 52(6): **Annex IX** (full quality‑management‑system + technical‑documentation assessment of one representative device). |
| **Handheld X‑ray Source** | Rule 10 – “active devices that emit ionising radiation for diagnostic or therapeutic radiology” | IIb (as indicated in source) | Art. 52(4): **Annex IX** (full QMS & technical‑documentation assessment) *or* the alternative route **Annex X + Annex XI** (type‑examination + production conformity verification). |
| **GUI Software (SaMD)** | Rule 11 – “software providing information used for diagnostic or therapeutic decisions” (diagnostic decision impact ≤ serious deterioration) | IIa | Art. 52(6): **Annex IX** (same as the Detector). |

\*The classification stated in the source table is taken as authoritative; it aligns with the MDR rules cited above.

---

## 2. PMS System Requirements (Art 83‑85, Annex III)

| Requirement | How it will be satisfied for each product |
|-------------|-------------------------------------------|
| **PMS system** – establishment of procedures, responsibility and resources (Art 83) | Implement a single PMS SOP covering all three devices; assign a Product‑Specific PMS Lead per device. |
| **PMS plan** – defined data sources, frequency & analysis methods (Art 84) | Use the “Sources of Information” matrix from source [2] as the baseline and expand with quantitative thresholds (e.g., DQE < 85 % triggers investigation). |
| **Periodic Safety Update Report (PSUR)** – content & update cadence (Art 86) | *X‑ray Detector* – PSUR every 2 years (source [1]). <br>*Handheld Source* – PSUR every 1 year (source [1]). <br>*GUI Software* – PSUR every 2 years (source [1]). The PSUR will contain: (a) benefit‑risk conclusions, (b) main PMCF findings, (c) sales volume & user population (Art 86(1)). |
| **Class I PMS report** – not applicable (all devices are IIa/IIb). | — |

---

## 3. Required Clinical Evidence & PMCF Planning  

### 3.1 X‑ray Detector (Class IIa)

| Evidence required (per Annex XIV Part A) | Current status | Gap |
|------------------------------------------|----------------|-----|
| **Clinical Evaluation Report (CER)** – includes state‑of‑the‑art literature, bench test data and a justification of equivalence to predicate devices. | CER referenced in source [1] (“CER, RMF, IEC 62220‑1‑1 test data”). | No detailed equivalence analysis provided; need documented comparator device dossier. |
| **PMCF** – “equivalence claim review” (source [1]) → requires post‑market clinical data that confirms performance comparable to the claimed predicate. | Sources identified: DQE degradation, pixel defect trends, patient dose over‑exposure (source [1] & [2]). | No defined PMCF protocol (sample size, follow‑up period, statistical analysis). |
| **Risk‑control verification** – link between residual risk from image‑quality loss and clinical impact. | RMF exists (source [1]) but no post‑market risk‑control verification plan. | Need explicit risk‑acceptance criteria for DQE decline, defect rate thresholds, and corresponding corrective actions. |

### 3.2 Handheld X‑ray Source (Class IIb)

| Evidence required | Current status | Gap |
|-------------------|----------------|-----|
| **CER** – must address ionising‑radiation safety, dose‑monitoring performance, and ergonomics. | CER referenced in source [1] (“CER, RMF, radiation‑dose monitoring data”). | No quantitative clinical data on operator dose or patient over‑exposure collected yet. |
| **PMCF** – “clinical data actively collected” (source [1]) due to ionising‑radiation risk. | Identified PMS data sources: dose over‑exposure incidents, mechanical damage, battery anomalies (source [2]). | No prospective clinical study plan (e.g., registry of procedures, cumulative dose per operator). |
| **Risk‑control verification** – must demonstrate effectiveness of built‑in dose‑limiting algorithms and battery safety measures. | RMF exists but no post‑market validation evidence. | Need a defined testing protocol for alarm thresholds and battery health monitoring in the field. |

### 3.3 GUI Software (SaMD, Class IIa)

| Evidence required | Current status | Gap |
|-------------------|----------------|-----|
| **CER** – must show clinical relevance of diagnostic output, usability safety, and conformity with IEC 62304/IEC 62366‑1. | CER referenced in source [1] (“CER, IEC 62304 maintenance records, bug log”). | No documented clinical performance study linking software read‑out to patient outcomes. |
| **PMCF** – “mandatory error data collection during use” (source [1]). | Sources identified: software errors, image display errors, usability issues (source [2]). | No defined PMCF protocol (e.g., number of incidents required before a trend is declared, corrective‑action timeline). |
| **Risk‑control verification** – usability validation per IEC 62366‑1 and post‑market software updates traceability. | RMF exists; bug log maintained (source [1]). | No formal “post‑market usability monitoring” plan (e.g., periodic heuristic evaluation, user survey schedule). |

---

## 4. Missing Information & Action Items  

| Item | Why it is required | Who must provide / verify |
|------|-------------------|---------------------------|
| **Detailed PMCF protocols** for each device (objective, population, sample size, endpoints, statistical analysis) | Required by Annex XIV Part B; without them the NB will request a “PMCF plan” before CE marking is granted. | RA lead drafts; Clinical/biostatistics team validates; NB review. |
| **Equivalence justification dossier** for X‑ray Detector (predicate device identification, technical & clinical similarity) | Basis of the equivalence claim mentioned in source [1]; needed for CER and for the NB’s assessment of conformity. | Product engineering + Clinical Affairs. |
| **Prospective registry design** for Handheld Source (operator dose tracking, adverse event capture) | Supports “active collection of clinical data” required by Art 84/Annex XIV Part B for Class IIb radiation devices. | Clinical team; IT systems. |
| **Usability‑evaluation plan & post‑market usability metrics** for GUI Software | Required to fulfil IEC 62366‑1 compliance and to substantiate the risk‑control verification of use‑error risks (Annex I §5). | UX/Usability specialist. |
| **Verification of risk‑control effectiveness (post‑market)** – e.g., DQE trend thresholds, dose‑limiting alarm performance, battery health alerts | Supports ongoing compliance with Annex I §§3–8 and the “risk control” requirement of the RMF; needed for PSUR conclusions. | Risk‑Management team (ISO 14971). |
| **EUDAMED entry – UDI registration & vigilance linkage** (already noted in source [1]) | Mandatory under Art 33‑39; must be live before first market launch. | Regulatory affairs / EUDAMED liaison. |
| **PSUR templates aligned with Art 86 content** and schedule confirmation (2 yr/1 yr) | Ensures PSURs will contain the required three elements: benefit‑risk conclusion, PMCF findings, sales & population data. | Documentation team; NB sign‑off on template. |

---

## 5. Risk Controls to be Demonstrated in PMS  

| Hazard (derived from sources) | Control(s) implemented pre‑market | Post‑market verification needed |
|-------------------------------|-----------------------------------|---------------------------------|
| **DQE degradation / pixel defects** (Detector) | Design tolerance, automatic calibration algorithm, preventive maintenance schedule. | Trend monitoring of DQE values; trigger corrective action if > 5 % drop over 6 months. |
| **Patient dose‑overexposure** (Handheld Source) | Built‑in dose‐limit circuitry, operator interlocks, pre‑set exposure parameters. | Record all dose‑overexposure incidents from vigilance system; compare frequency to acceptability criteria (< 1 % of procedures). |
| **Mechanical damage / battery failure** (Source) | Robust housing, shock‑absorbing mount, battery management system with state‑of‑charge monitoring. | Quarterly analysis of service reports; replace batteries after specified cycles. |
| **Software errors & image‑display anomalies** (GUI) | IEC 62304 compliant development lifecycle, automated regression test suite, runtime error logging. | Monthly bug‑log review; severity classification and trend analysis; issue patches within 30 days for high‑severity bugs. |
| **Usability/use‑error risks** (All) | Human factors engineering per IEC 62366‑1, labeling per Annex I §23. | Annual usability survey of end users; record any “use error” complaints and feed back to design changes. |

All controls are documented in the Risk Management File (RMF) as required by **Annex I Chapter I §3** (risk‑management system) and verified during PMS according to **Art 83–86**.

---

## 6. Regulatory Judgment & Human‑Escalation Triggers  

| Trigger | Description | Escalation action |
|---------|-------------|-------------------|
| **Absence of PMCF protocol** for any product | NB will reject the technical‑documentation assessment until a complete PMCF plan (Annex XIV Part B) is supplied. | Immediate RA senior review; initiate draft PMCF plan and request Clinical Lead input – *stop* further CE‑marking submission until resolved. |
| **Equivalence claim not substantiated** (Detector) | Without documented equivalence, the CER cannot satisfy Annex XIV Part A. | Raise to Product Manager & Engineering Lead; schedule a gap‑analysis workshop within 5 working days. |
| **Missing post‑market risk‑control verification data** (all devices) | Required for PSUR conclusions and ongoing compliance with Annex I §3–8. | Notify Risk‑Management Owner; generate an Action‑Item log; deadline ≤ 2 weeks. |
| **EUDAMED UDI / vigilance linkage not live** | Non‑compliance with Art 33‑39 will block market entry in the EU. | Escalate to Regulatory Operations Lead; halt any distribution until registration confirmed. |
| **PSUR cadence mismatch** (e.g., source set to 1 yr but NB expects 2 yr for Class IIb) | Incorrect update interval could be deemed non‑conformant with Art 86. | Verify NB requirement; adjust schedule and document justification. |

If any of the above triggers are identified during internal review, the case must be **escalated to the senior RA manager** for approval before proceeding to the Notified Body.

---

## 7. Peer‑Review Prompt  

> *Colleague, please challenge the assumptions made in this draft:*
> 
> - Are the MDR rule citations (Rule 17, 10, 11) correctly matched to the three devices?  
> - Does the suggested conformity‑assessment route (Annex IX for IIa and IIb) align with current NB practice for radiation equipment, or should we recommend the Annex X + XI alternative for the Handheld Source?  
> - Have we captured all required data sources for PMS as per Art 84, especially regarding “trend reporting” and “competitor public information”?  
> - Are there any jurisdiction‑specific obligations (e.g., specific radiation‑protection standards) that are missing from the risk‑control section?  

Your feedback will be incorporated before finalising the submission package.

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
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

### kb-eval-20261110-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "954eb1d2bbaa568f", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `954eb1d2bbaa568f`
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

> **Regulatory Draft – X‑ray Diagnostic Device (Ionising‑Radiation Emitting) – EU MDR 2017/745**

---

### 1. Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|--------------|-------------------|
| **Applicable classification rule** | **Rule 10** (ionising‑radiation emitting diagnostic device) → **Class IIb** | Annex VIII – Rule 10 (source excerpt [2]) |
| **Conformity‑assessment route** | Either<br>① **Annex X** (type‑examination) + **Annex XI** (production‑conformity verification)<br>or<br>② **Annex IX** (full quality‑management & technical‑documentation assessment) | Article 52(4) MDR 2017/745 – Class IIb may follow Annex X + XI *or* Annex IX |

*Recommendation*: Use the **type‑examination route (Annex X + XI)** because X‑ray equipment is a high‑risk, safety‑critical device; this path allows a dedicated type‑examination certificate for radiation performance and safety.

---

### 2. Required Evidence & Documentation  

| Section | Minimum content | Where it belongs in the Technical Documentation (Annex II §6.1) |
|---------|----------------|--------------------------------------------------------------|
| **Device description & intended purpose** | Full description, indications, contraindications, user profile, clinical environment. | Annex II §1 |
| **Labeling & IFU** | Labels, instructions for use, symbols per Annex I §23 (including radiation warnings). | Annex II §2 |
| **Design & manufacturing information** | Process flow, materials, component specifications, sterilisation (if applicable), assembly controls. | Annex II §3 |
| **General Safety & Performance Requirements (GSPR) compliance** | Evidence of fulfilment of all 23 GSPR items – especially §§ 16 (radiation protection), 18 (active devices), 22 (lay‑person use). | Annex II §4 |
| **Risk Management File** | Risk analysis, risk evaluation, risk control measures, residual risk assessment in line with ISO 14971:2019. | Annex II §5 |
| **Verification & Validation** <br>• Electrical safety & performance (IEC 60601‑2‑54, IEC 60601‑2‑28) <br>• Radiation output testing, dose measurements, DQE (IEC 62220‑1‑1) | Test reports, validation protocols, acceptance criteria. | Annex II §6 |
| **Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical investigation data (if needed), benefit‑risk analysis – kept current under Art. 61, structured per Annex XIV Part A. | Annex II §6.1 (clinical evaluation) |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Planned prospective studies, methodology, endpoints, timeline; final PMCF evaluation report – Annex XIV Part B. | Annex III (post‑market surveillance technical documentation) |
| **PMS System & Plan** | PMS procedures (Art. 83), PMS plan (Art. 84). For Class IIb the system must feed into a Periodic Safety Update Report (PSUR) – Art. 86. | Annex III §1‑3 |
| **Periodic Safety Update Report (PSUR)** | Updated benefit‑risk conclusions, PMCF findings, sales volume & user population – prepared at least **every two years** for Class IIb (Art. 86(1)/(2)). | Annex III §4 |

---

### 3. Gaps / Missing Information (to be supplied before NB submission)

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Exact intended use statement** (clinical indication, patient population) | Drives classification confirmation and clinical‑evaluation scope. | Provide a concise Intended Use description. |
| **Full risk management file** – especially residual risk evaluation for radiation exposure & software hazards (if SaMD component). | Required to demonstrate compliance with GSPR §§ 16, 18, 22 and ISO 14971. | Complete FMEA/FMECA, calculate dose limits, document mitigations. |
| **Clinical data** – either a robust literature review or a dedicated clinical investigation report. | Needed for the CER (Annex XIV Part A). | Conduct systematic literature search; if insufficient, plan a post‑market clinical investigation. |
| **PMCF plan details** – study design, sample size, follow‑up period, responsible parties. | PSUR cannot be compiled without an active PMCF programme (Art. 86). | Draft a PMCF protocol aligned with the device’s risk profile. |
| **Labeling draft & IFU** – especially radiation safety information and user instructions for lay‑person handling if applicable. | Must satisfy Annex I §23 and GSPR §22. | Produce final labelling package, run usability testing per IEC 62366‑1. |
| **UDI implementation evidence** (EUDAMED registration) | Mandatory for Class IIb devices (Art. 33‑39). | Assign a UDI, register device & all variants in EUDAMED. |
| **Software documentation (if applicable)** – software architecture, verification, validation per IEC 62304. | Required when Rule 11 applies to SaMD components. | Compile Software Development File (SDF) and confirm classification for each software element. |
| **Electrical safety & EMC test reports** aligned with IEC 60601‑2‑54/28 | Demonstrates compliance with GSPR §16 and Annex II verification requirements. | Perform or collect accredited test certificates. |

---

### 4. Key Risk Controls (derived from the RMF)

1. **Radiation protection** – design shielding, automatic exposure control, dose‑monitoring alarms (GSPR §16).  
2. **Active device safety** – fail‑safe modes, watchdog timers, emergency stop (GSPR §18).  
3. **Usability & use‑error mitigation** – user‑interface design validated per IEC 62366‑1; labelling warnings for lay users (GSPR §22).  
4. **Software hazard controls** – classification‑appropriate verification/validation, secure updates, error handling (IEC 62304).  
5. **Electrical safety & EMC** – compliance with IEC 60601‑2 series, protective earth, isolation (GSPR §20).  
6. **Residual risk communication** – IFU includes explicit statement of remaining radiation risks vs benefits (GSPR §8).

---

### 5. Regulatory Citations  

| Topic | Citation |
|-------|----------|
| Classification rule for ionising‑radiation diagnostic device | Rule 10, Annex VIII MDR 2017/745 (source [2]) |
| Conformity‑assessment routes for Class IIb | Art. 52(4) MDR – either Annex X + XI **or** Annex IX (framework reference) |
| Clinical evaluation requirement | Annex XIV Part A; kept current under Art. 61 |
| PMCF plan & report | Annex XIV Part B |
| PMS system & plan | Art. 83 (system), Art. 84 (plan) |
| PSUR frequency for Class IIb | Art. 86(1)/(2) – at least every **two years** |
| GSPR references for radiation, active devices and lay‑person use | Annex I §§ 16, 18, 22 |
| Technical documentation structure | Annex II §1‑6 (incl. clinical evaluation & PMCF in §6.1) |
| Post‑market surveillance technical file | Annex III |
| ISO risk‑management standard | ISO 14971:2019 (framework reference) |
| IEC standards for X‑ray equipment | IEC 60601‑2‑54, IEC 60601‑2‑28 (device safety & tube assemblies) |
| Software life‑cycle standard (if SaMD present) | IEC 62304 2006+A1:2015 |

*All framework citations are stated directly from the MDR; no instance identifiers were present in the source excerpts.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation |
|--------|-----------------------|
| **Unresolved classification doubt** (e.g., device includes both imaging and therapeutic functions) | Requires senior RA sign‑off & possibly a pre‑submission advice to the Notified Body. |
| **Missing or insufficient clinical evidence** (no adequate literature, no investigation data) | Must pause submission; initiate clinical study plan before proceeding. |
| **Incomplete risk management file** (unaddressed radiation dose residual risk) | Immediate remediation required – cannot meet GSPR §16. |
| **PMCF plan not approved by the manufacturer’s Clinical Evaluation Committee** | Needs senior clinical review before NB assessment can start. |
| **Labeling or IFU fails usability testing** | Re‑work labeling; trigger design‑verification loop. |
| **EUDAMED registration incomplete (UDI, device model details)** | Blocked from entering conformity‑assessment dossier – ask IT/Regulatory Ops to finalize. |
| **Discrepancy between Annex X type‑examination report and internal validation data** | Must be resolved with the Notified Body; possibly trigger a re‑test. |

When any of these triggers arise, the RA team should:

1. Log the issue in the project’s risk register (Art. 10(9) MDR – QMS obligations).  
2. Notify the Project Lead and, where appropriate, schedule a **Regulatory Review Meeting** with senior RA and Clinical experts.  
3. Document the decision‑making process and corrective actions per ISO 14971 (risk management review).

---

### 7. Peer‑Review Prompt  

> *Colleague, please examine the assumptions above:*
> 
> 1. **Classification & route choice** – does Rule 10 unequivocally place this X‑ray system in Class IIb, or are any ancillary software functions (Rule 11) that could bump it to a higher class?  
> 2. **Evidence completeness** – have we identified all mandatory clinical‑evaluation inputs for an ionising‑radiation device under Annex XIV Part A?  
> 3. **PMS/PMCF scope** – is the proposed PSUR frequency (every two years) fully aligned with Art. 86 for this class, considering any implantable components?  
> 4. **Standards mapping** – are there additional IEC standards (e.g., IEC 60601‑2‑44 for CT if relevant) that must be referenced given the device’s intended modalities?  

Please provide feedback on any gaps or jurisdiction‑specific nuances that may affect the upcoming Notified Body audit.

--- 

*End of draft.*

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

### kb-eval-20261110-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2a3d9133249b9cb4", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2a3d9133249b9cb4`
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

### 1. Device‐level assumptions (to be confirmed)

| Item | Current status | Gap / Action |
|------|----------------|--------------|
| **Intended purpose / indication** | Not supplied in source | Obtain a clear, manufacturer‑approved Intended Use Statement (IUS). |
| **Technological description & accessories** | Missing | Request detailed device architecture, materials, software/firmware versioning. |
| **Risk classification rule** | Unknown – requires application of Annex VIII rules | Conduct classification workshop with the OEM; record the specific Rule(s) applied (e.g., Rule 9, 10, 11, 17). |
| **Intended user & environment** | Not identified | Clarify whether device is for professional or lay‑person use, sterile/measuring/reusable aspects. |

> **Human escalation trigger 1:** If any of the above items cannot be supplied within 5 working days, pause preparation of the Technical Documentation (TD) and notify the Project Lead.

---

### 2. Classification & Conformity‑Assessment Route  

| Regulatory reference | Required determination |
|----------------------|------------------------|
| **Article 51 + Annex VIII** – classification principles (self‑classification by the manufacturer)【2】 | Apply the 22 sequential rules; select the highest class reached. |
| **Art. 52(…)** – route selection once class is known | • Class I → self‑declaration (no NB).<br>• Is / Im / Ir → Annex IX (QMS) or Annex XI Part A (sterile/measuring).<br>• Class IIa → Annex IX (full TD assessment) **or** Annex II/III + Annex XI §10.<br>• Class IIb → Annex IX (full TD assessment) **or** Annex X + Annex XI.<br>• Class III → Annex IX (full TD assessment) **or** Annex X + Annex XI. |

> **Human escalation trigger 2:** If the device lands in Class IIb or III, a Notified Body (NB) must be engaged early to negotiate the preferred route and budget; raise this with the regulatory manager within 3 working days of classification.

---

### 3. PMS & PMCF Obligations  

| Requirement | Regulatory source | Evidence needed |
|-------------|-------------------|-----------------|
| **PMS system** (process, resources, responsibilities) | Art. 83 MDR | SOPs for monitoring, complaint handling, trend analysis; organisational chart showing PMS responsibility. |
| **PMS plan** (pre‑market to post‑market transition) | Art. 84 MDR | Documented plan covering data sources, frequency of review, key performance indicators. |
| **PMS report** (Class I) or **PSUR** (Class IIa/IIb/III) | Art. 85 & Art. 86 MDR | • Class I → annual PMS report.<br>• Class IIa/IIb → PSUR every 2 years; Class III/implantables → PSUR annually (Art. 86(1)/(2)). |
| **Clinical Evaluation Report (CER)** – kept up‑to‑date | Article 61 & Annex XIV Part A MDR | Current CER integrating literature review, clinical data, and benefit–risk analysis. |
| **PMCF plan** (if required) | Annex XIV Part B MDR | Detailed plan of post‑market clinical investigations, subject numbers, endpoints, timelines. |
| **PMCF evaluation report** (upon completion) | Annex XIV Part B MDR | Conclusions on device performance, updates to CER. |
| **Vigilance / Serious Incident Reporting** | MDR Art. 87 & Korean “의료기기법 §31” (source excerpt) | Procedure for reporting serious incidents to the Competent Authority; link to MedWatch/21 CFR 803 where applicable. |
| **UDI registration** | EUDAMED UDI/DEV portal (source excerpt) | Assigned device identifier entered in EUDAMED, with corresponding labeling updates. |

> **Human escalation trigger 3:** If any of the above documents cannot be completed before the NB audit window (typically 30 days prior), issue a risk‑based deviation request to senior management.

---

### 4. Required Supporting Evidence & Documentation  

1. **Technical Documentation (Annex II §1‑6)** – complete files, including design specifications, manufacturing processes, and GSPR compliance.  
2. **Risk Management File** – ISO 14971:2019 compliant risk analysis, evaluation of residual risks (§3 risk management system) and verification of risk controls (§4‑8).  
3. **Clinical Evidence** – literature search (state‑of‑the‑art), clinical trial data where available, or justified equivalence (no “predicate” claim under MDR).  
4. **Usability Engineering File** – IEC 62366‑1:2020 results addressing §22 of Annex I (use by lay persons if applicable).  
5. **Software Documentation** (if software is a device) – IEC 62304:2006+A1:2015 lifecycle documentation, classification per Rule 11.  
6. **Radiation Protection Evidence** (if emitting ionising radiation) – IEC 60601‑2‑54 & §16 of Annex I.  

> **Human escalation trigger 4:** Any missing ISO/IEC standard reference or outdated edition must be escalated to the quality manager for immediate procurement of latest standards; deadline: 7 calendar days.

---

### 5. Gap Summary (What is Still Needed)

| Gap | Why it matters | Planned action |
|-----|----------------|----------------|
| **Exact classification rule** (e.g., Rule 9, 10, 11, 17) | Determines NB involvement & post‑market reporting cadence | Conduct device‑function workshop → document rule applied. |
| **Intended use statement & user profile** | Drives risk analysis, GSPR §§22‑23 and PMS data sources | Request from OEM; update labeling draft. |
| **Clinical data package** (e.g., clinical investigation reports, post‑market data) | Needed for CER & PMCF plan justification | Compile all existing studies; identify data gaps. |
| **PMS/PMCF detailed schedule** (frequency of literature review, sentinel site monitoring) | Required to satisfy Art. 84/86 and Annex XIV | Draft timetable; circulate for stakeholder sign‑off. |
| **Risk control measures linked to residual risk** (e.g., protective labeling, software safety features) | Evidence for compliance with Annex I §§3‑9 | Map each identified hazard to a specific control; verify via verification/validation reports. |
| **UDI registration in EUDAMED** (device identifier not yet entered) | Mandatory for market access and traceability | Submit device model(s) to EUDAMED; confirm entry. |

---

### 6. Risk Controls – Mapping to Annex I

| Hazard / Residual Risk | Control measure (existing or needed) | Annex I reference |
|------------------------|--------------------------------------|-------------------|
| Use‑error by lay persons (if applicable) | Instruction for use with pictograms, training program | §22 |
| Sterility breach (Is/Im) | Validated aseptic manufacturing, QC sterility testing | §3 (risk management), §4 (risk control) |
| Software decision error (Rule 11) | IEC 62304 development lifecycle, verification of algorithm, fallback mode | §17 (electronic programmable systems) |
| Radiation over‑exposure (if X‑ray component) | Compliance with IEC 60601‑2‑54, built‑in dose limits, interlocks | §16.4 (protection against radiation) |
| Mechanical failure (e.g., moving parts) | Finite‑element analysis, durability testing, post‑market wear monitoring | §20 (mechanical/thermal risks) |

> **Human escalation trigger 5:** Any identified control that cannot be demonstrated by existing validation data must be escalated to engineering for remedial design or additional verification within 10 working days.

---

### 7. Human‑Escalation Triggers Summary  

| Trigger # | Condition | Escalation recipient | Timeline |
|-----------|-----------|----------------------|----------|
| 1 | Missing intended use / device description | Project Lead | ≤5 days |
| 2 | Classification results in Class IIb/III (NB required) | Regulatory Manager | ≤3 days |
| 3 | PMS/PMCF documents not ready before NB audit window | Senior Management | Immediate (as soon as gap identified) |
| 4 | Out‑of‑date or missing ISO/IEC standards | Quality Manager | ≤7 days |
| 5 | Unverified risk control (no supporting data) | Engineering Lead | ≤10 days |

---

### 8. Peer‑Review Prompt  

*“@RA‑Peer, please review the assumptions made regarding classification (Rule identification), completeness of the PMS/PMCF evidence list, and any jurisdiction‑specific gaps (e.g., Korean “의료기기법 §31” vs. EU MDR). Verify that all cited regulatory provisions correspond to the source excerpts and flag any missing items that could impede the Notified Body’s assessment.”*

--- 

*Prepared by Theo – EU RA Specialist*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
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

### kb-eval-20261110-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "ecf270d94c4ade97", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_Vigilance_Serious_Incident_판정기준.md", "source_hash": "658a335222dbeb042ba862855e6916b3dad30abb6e2047ab0d19d0b2e6897f2a"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `ecf270d94c4ade97`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_Vigilance_Serious_Incident_판정기준.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_Vigilance_Serious_Incident_%ED%8C%90%EC%A0%95%EA%B8%B0%EC%A4%80.md)
- Source hash: `658a335222dbeb042ba862855e6916b3dad30abb6e2047ab0d19d0b2e6897f2a`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_Vigilance_Serious_Incident_판정기준.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 4. 보고 방법 (EUDAMED Vigilance Module) | 단계 | 내용 | |---|---| | **Initial Report** | EUDAMED에 Serious Incident 초기 보고. 모든 필드 완성 불요, 인식 즉시 제출. | | **Follow-up Report** | 추가 조사 결과 업데이트. 여러 차례 제출 가능. | | **Final Report** | 조사 완료 후 Root Cause, 시정 조치, 재발 방지 계획 포함. | | **보고 대상 CA** | 기기가 판매된 EU Member State(들)의 Competent Authority | | **EUDAMED 접근** | 제조사 → EUDAM...
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

> **Regulatory Draft – Hand‑held X‑ray Source (Active Device emitting ionising radiation)**  

---

### 1. Device Classification & Conformity‑Assessment Route  
| Item | Reference |
|------|------------|
| **MDR Rule** – Active device that emits ionising radiation for diagnostic use → **Rule 10** (Annex VIII) | MDR Annex VIII, Rule 10 |
| **Resulting Class** – **Class IIb** (Rule 10‑IIb because the emitted radiation can cause a serious hazard to patients/operators) | MDR Annex VIII, Rule 10 |
| **Conformity‑assessment routes (Art. 52)**  <br>• **Route A:** Full QMS + technical‑documentation assessment – **Annex IX** (single NB audit)  <br>• **Route B:** Type‑examination **(Annex X)** + production conformity verification **(Annex XI)** | Art. 52(4) & Art. 52(3); Annex IX; Annex X + XI |

*The manufacturer may choose either route A (Annex IX) or route B (Annex X + XI). The selected NB must be notified for Class IIb devices.*

---

### 2. Core Evidence Required for the Chosen Route  

| Evidence | Where it belongs in the Technical Documentation (Annex II §6.1) | Relevant Regulation / Standard |
|----------|--------------------------------------------------------------|--------------------------------|
| **Device description & intended purpose** (including radiation output, beam geometry, battery type, operating modes) | Annex II §1 – device description | MDR §10(9) |
| **Design‑manufacturing information** (materials, assembly, electrical safety, shielding calculations) | Annex II §2 – design and manufacturing | MDR §10(11) |
| **General Safety & Performance Requirements (GSPR) compliance** – especially §§16 (radiation protection), 18 (active devices), 23 (labelling) | Annex II §4 – verification of GSPR | MDR Annex I §§16, 18, 23 |
| **Risk Management File** (ISO 14971:2019) – hazard identification, risk evaluation, radiation‑dose control measures, residual‑risk acceptance criteria | Annex II §5 – risk management | ISO 14971 2019; MDR §10(10) |
| **Clinical Evaluation Report (CER)** – state‑of‑the‑art literature on diagnostic accuracy, dose‑performance, comparative devices | Annex XIV Part A (kept current under Art. 61) | MDR Annex XIV Part A |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Evaluation Report** – prospective data collection on radiation dose, device reliability, user errors | Annex XIV Part B | MDR Annex XIV Part B |
| **Post‑Market Surveillance (PMS) System** – description of processes, reporting flow‑chart, and SAR handling | Art. 83 (system) + Art. 84 (plan) | MDR Art. 83–84 |
| **Periodic Safety Update Report (PSUR)** – every 2 years for Class IIb (benefit‑risk conclusions, PMCF results, sales/usage data) | Art. 86(1)(a‑c) | MDR Art. 86 |
| **Vigilance / Serious Incident reporting** – documented procedure, SRN registration in EUDAMED Vigilance Module | Art. 87 (serious incident & FSCA reporting) + EUDAMED vigilance module description (source excerpt) | MDR Art. 87; source [1] |
| **Labeling & IFU** – instructions, radiation safety warnings, user training information | Annex I §23 (information supplied with the device) | MDR Annex I §23 |

---

### 3. Gaps / Missing Information (to be obtained before NB submission)

| Gap | Why it matters | Suggested source of data |
|-----|----------------|--------------------------|
| **Exact intended use statement** (diagnostic imaging of which anatomical region, patient population, clinical setting) | Needed for classification rule application and CER scope | Technical specification / marketing dossier |
| **Quantitative radiation output (mGy · cm²), beam quality, shielding design calculations** | Required to demonstrate compliance with GSPR §16 and IEC 60601‑2‑54 | Engineering test reports, Monte‑Carlo simulations |
| **Clinical performance data** (sensitivity/specificity, image quality scores vs. predicate) | Forms the core of the CER & supports benefit‑risk | Clinical study protocol + results |
| **PMCF plan details** – number of devices in use, follow‑up duration, data collection method | PSUR must reference PMCF outcomes (Art. 86) | PMCF protocol draft |
| **Labeling drafts** (including radiation warnings, user training instructions) | Must satisfy Annex I §23 & ensure safe use (§5 risk control) | Draft IFU and label art |
| **PMS plan – trend‑analysis methodology** | Required for Art. 84 & PSUR generation | PMS SOPs |
| **Evidence of compliance with IEC 60601‑2‑54 (or relevant IEC standard)** | Demonstrates conformity to essential safety requirements for radiographic equipment | Test certificates, declaration of conformity to IEC standards |

*If any of the above remain unavailable at the time of NB audit, a “non‑conformity” will be raised and the submission cannot be accepted.*

---

### 4. Risk Controls (derived from ISO 14971 & GSPR)

| Hazard | Control(s) | Regulatory basis |
|--------|------------|-------------------|
| **Excessive radiation emission** (patient/operator over‑exposure) | • Built‑in dose‐limiting circuitry <br>• Real‑time dosimetry with alarm<br>• Mandatory pre‑use safety checklists<br>• Shielded housing & interlocks | GSPR §16; ISO 14971 risk control |
| **Battery thermal runaway (over‑heat, fire)** | • Battery management system (BMS) with temperature cut‑off <br>• Protective casing, venting design <br>• User training on charging procedures | GSPR §5 (use‑error), §8 (foreseeable risks) |
| **Device drop → mechanical damage** | • Ruggedised housing to IEC 60601‑2‑54 drop requirements <br>• Drop‑test validation reports | IEC 60601‑2‑54; GSPR §§20, 22 |
| **Incorrect set‑up leading to mis‑aimed radiation** | • Ergonomic hand‑grip with visual alignment aids <br>• Software‑driven lockout if positioning parameters out of range | GSPR §17 (electronic programmable systems), §18 (active devices) |
| **Software error affecting dosage calculation** | • IEC 62304 software lifecycle management; verification & validation test matrix<br>• Periodic firmware updates with traceability | GSPR §§17, 18; IEC 62304 |

---

### 5. Vigilance Reporting – Process Flow (derived from source)

1. **Incident detection** (e.g., radiation leak, over‑exposure, battery fire).  
2. **Initial Report** to EUDAMED Vigilance Module – SRN registration mandatory (source [1]). No full field completion required; submitted immediately upon recognition.  
3. **Follow‑up Reports** as further investigation results become available (multiple submissions allowed).  
4. **Final Report** – includes root‑cause analysis, corrective actions, and recurrence‑prevention plan.  

*Reporting deadlines (from source [2]):*  

| Incident type | Reporting deadline |
|---------------|-------------------|
| Radiation leak → immediate staff exposure | **2 days** (+ FSCA *immediately*) |
| Device malfunction → patient over‑exposure | **2 days** |
| Battery overheating → user burn injury | **10 days** |
| Device drop with no patient impact | No report required |

*No specific regulatory identifier is provided for these deadlines in the source – verify separately.*  

---

### 6. Human‑Escalation Triggers (when to raise to senior RA / management)

| Trigger | Reason & Required Action |
|---------|---------------------------|
| **Missing intended‑use statement or incomplete radiation output data** | Cannot finalize classification & CER → pause submission, inform product development for clarification. |
| **Absence of a PMCF plan or evidence that it covers the identified residual risks** | PSUR would be non‑compliant (Art. 86) → immediate escalation to clinical affairs and senior RA. |
| **Failure to register an SRN in EUDAMED before first market release** | Violates Art. 87 & source [1] – legal breach; stop distribution, notify compliance officer. |
| **Serious incident meeting “radiation leak” or “patient over‑exposure” criteria** | Mandatory 2‑day report + FSCA → trigger internal urgent response team, prepare initial and follow‑up reports, inform NB within the same timeframe. |
| **PSUR not updated within the two‑year cycle for a Class IIb device** | Non‑conformity with Art. 86 – escalates to Quality Management review & possible NB re‑audit. |
| **Risk‑control measures not verified against IEC 60601‑2‑54 test data** | GSPR §16 non‑compliance – stop conformity assessment, request additional testing. |

If any of the above triggers occur, the RA must:
1. Log the issue in the device risk register.  
2. Notify the Quality Management System (QMS) manager and the Project Lead within 24 h.  
3. Prepare a corrective‑action plan and, where required, inform the Notified Body before proceeding further.

---

### 7. Summary Judgment  

| Item | Decision |
|------|----------|
| **Classification** | Class IIb (Rule 10) – MDR Annex VIII |
| **Conformity route** | Choose either Annex IX (full QMS & technical‑doc audit) *or* Annex X + XI (type‑examination + production conformity verification) per Art. 52. |
| **Key evidence needed** | Complete Technical Documentation (Annex II), CER, PMCF plan, PMS system (Art. 83‑86), vigilance procedures with SRN registration (source [1]), compliance to IEC 60601‑2‑54 & ISO 14971. |
| **Current gaps** | Intended use definition, quantitative radiation data, clinical performance results, detailed PMCF and labeling drafts, IEC test certificates. |
| **Risk controls** | Radiation dose limiting, battery management, ergonomic design, software validation – aligned with GSPR §§16, 17, 18. |
| **Escalation points** | Missing core evidence, breach of reporting deadlines (2 days/10 days), PSUR lapse, non‑registration in EUDAMED. |

---

### 8. Peer‑Review Prompt  

> *Colleague, please review the assumptions made about the classification rule and the chosen conformity routes, verify that all required MDR citations are appropriate for a handheld X‑ray source, and check whether any additional IEC standards (e.g., IEC 60601‑1‑2 for electromagnetic compatibility) should be listed. Also confirm if the incident‑reporting timeframes taken from the source need alignment with Art. 87 or other MDR provisions.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1021369192354279182`

> ## 4. 보고 방법 (EUDAMED Vigilance Module) | 단계 | 내용 | |---|---| | **Initial Report** | EUDAMED에 Serious Incident 초기 보고. 모든 필드 완성 불요, 인식 즉시 제출. | | **Follow-up Report** | 추가 조사 결과 업데이트. 여러 차례 제출 가능. | | **Final Report** | 조사 완료 후 Root Cause, 시정 조치, 재발 방지 계획 포함. | | **보고 대상 CA** | 기기가 판매된 EU Member State(들)의 Competent Authority | | **EUDAMED 접근** | 제조사 → EUDAMED Vigilance Module (SRN 등록 필수) | ---

2. Chunk `1090650074354265530`

> ### 6.2 Handheld X-ray Source | 시나리오 | Serious Incident? | 보고 기한 | |---|---|---| | 방사선 누설 → 의료인 피폭 (즉각 위협) | ✅ | **2일** + FSCA 즉시 | | 기기 오작동 → 방사선 노출 과다 (환자) | ✅ | **2일** | | 배터리 과열 → 사용자 화상 | ✅ | 10일 | | 기기 낙하 → 손상 (환자 영향 없음) | ❌ | 보고 불요 |

### kb-eval-20261110-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "cba6f5ef35910291", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "eb4c9a22b20b0a1d5596a1d52e576d1579c10df62ed295d604c8c3120ca09417"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `cba6f5ef35910291`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning  
(derived from the “daily_growth_v1” run, source : GitHub – `04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md`)**

---

## 1. Scope & Objective
The purpose of this draft is to:

1. **Identify the MDR classification and the applicable conformity‑assessment route** for each of the three X‑ray‑related products listed in the source matrix.  
2. **Define the evidence package** that a Notified Body (NB) will require to accept the technical documentation.  
3. **Highlight missing information / gaps** that must be supplied before submission.  
4. **Outline risk‑control measures linked to the General Safety and Performance Requirements (GSPR)**.  
5. **Enumerate human‑escalation triggers** for when a review or stop‑gap decision is required.

All citations follow the framework‑reference rule (classification rules, Annex/Article numbers, ISO/IEC standards). No instance‑specific identifiers are invented – where the source does not give a concrete number we note “no specific identifier found in source — verify separately”.

---

## 2. Product‑by‑Product Regulatory Assessment

| # | Product | Likely MDR Classification (rule) | Conformity‑Assessment Route (Art. 52) | Core Evidence Required* | Key Citations |
|---|---------|----------------------------------|---------------------------------------|--------------------------|---------------|
| **1** | **X‑ray Detector (diagnostic image recorder)** | Class **IIa** – *Rule 17* (device for recording X‑ray images)  <br>*Source lists “Class IIa/IIb” → the lower class is justified by Rule 17; upgrade to IIb only if combined with a therapeutic function.* | • **Art. 52(6)** – Annex IX (QMS + technical‑documentation assessment of one representative device)  <br>• Alternative: Annex II + III + Annex XI §10 (if the manufacturer prefers the “self‑assessment” route for Class IIa) | • Clinical Evaluation Report (CER) – Annex XIV Part A  <br>• PMCF Plan & report – Annex XIV Part B  <br>• PMS Plan – Art. 84  <br>• PSUR (frequency “every 2 years” as per source) – Art. 86(1)/(2)  <br>• Risk Management File (ISO 14971:2019)  <br>• Performance testing per IEC 60601‑2‑54 & IEC 60601‑2‑28  | **Rule 17**; **Art. 52(6)**; **Annex IX**, **Annex XIV Part A/B**; **Art. 84**, **Art. 86**; **ISO 14971:2019**; **IEC 60601‑2‑54**, **IEC 60601‑2‑28** |
| **2** | **Handheld X‑ray Source (emits ionising radiation for diagnostic use)** | Class **IIb** – *Rule 10* (active device emitting ionising radiation)  <br>*(Source already assigns “Class IIb”.)* | • **Art. 52(4)** – either:  <br> – Annex IX (full QMS + technical‑documentation assessment)  <br> – or Annex X + Annex XI (type‑examination + production conformity verification).  The NB will usually request the **Annex IX** route for a single device family. | • CER – Annex XIV Part A  <br>• PMCF Plan & report – Annex XIV Part B  <br>• PMS Plan – Art. 84  <br>• PSUR (annual frequency per source) – Art. 86(1)/(2)  <br>• Risk Management File – ISO 14971:2019  <br>• Safety‑design testing per IEC 60601‑2‑28 (X‑ray tube assembly) & IEC 60601‑2‑54 (radiography equipment) | **Rule 10**; **Art. 52(4)**; **Annex IX** OR **Annex X + XI**; **Art. 84**, **Art. 86**; **ISO 14971:2019**; **IEC 60601‑2‑28**, **IEC 60601‑2‑54** |
| **3** | **“촬영실” GUI Software (SaMD) – image‑viewing/interpretation tool** | Class **IIa** – *Rule 11* (software providing information for diagnostic decisions).  <br>*(Source cites “Class IIa (MDR §22)”. The reference to §22 is the GSPR clause on devices intended for lay persons; it does not define class. Classification follows Rule 11.)* | • **Art. 52(6)** – Annex IX (QMS + technical‑documentation assessment of one representative device).  <br>• For SaMD, a *software life‑cycle* dossier (IEC 62304) is mandatory and forms part of the technical documentation. | • CER – Annex XIV Part A  <br>• PMCF Plan & report – Annex XIV Part B (especially usability/clinical validation)  <br>• PMS Plan – Art. 84  <br>• PSUR (every 2 years per source) – Art. 86  <br>• Risk Management File – ISO 14971:2019 (including software‑specific hazard analysis)  <br>• Software development dossier – IEC 62304 (2006+A1:2015)  <br>• Usability engineering file – IEC 62366‑1 (2015+A1:2020) | **Rule 11**; **Art. 52(6)**; **Annex IX**; **Annex XIV Part A/B**; **Art. 84**, **Art. 86**; **ISO 14971:2019**; **IEC 62304**, **IEC 62366‑1** |

\* *Evidence required for the NB to demonstrate conformity with the GSPR, as listed in Annex II §6.1 (clinical evaluation & PMCF) and Annex III (post‑market surveillance).*

---

## 3. Common Documentation Gaps (derived from source matrix)

| Gap | Why it matters (regulatory impact) | Evidence needed to close gap |
|-----|------------------------------------|------------------------------|
| **Intended purpose / indication** (exact clinical claim) | Determines the classification rule, risk profile and required clinical data. | Precise Intended‑Use Statement; Indications list; User population description. |
| **Complete device description & variant matrix** | Needed for Annex II §1–3 and to justify classification per Rule 9‑11‑17. | Technical specifications, design drawings, bill of materials, software versioning. |
| **Risk Management File (RMF) – ISO 14971** | Supports GSPR §§3‑9; necessary for NB review. | Hazard identification, risk evaluation, residual‑risk acceptability justification, risk‑control measures, verification results. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A requirement; basis for CE marking. | State‑of‑the‑art literature review, clinical data (pre‑market studies, existing device data), benefit–risk analysis. |
| **PMCF Plan & interim reports** | Annex XIV Part B – mandatory for Class IIa‑III devices. | Defined objectives, methodology, data sources, timelines, reporting structure. |
| **Usability / Human Factors evidence (for SaMD & handheld source)** | GSPR §22 (lay‑person use) and IEC 62366‑1 compliance. | Usability test protocol & results, formative/summative evaluations. |
| **Performance testing against IEC standards** | Demonstrates conformity with essential safety requirements (e.g., IEC 60601‑2‑54 for X‑ray detector). | Test reports, calibration certificates, DICOM interoperability evidence. |
| **Labeling & IFU (Annex I §23)** | Required for market placement; must reflect risk controls and intended use. | Draft Labels, Instructions for Use, safety notices, CE marking graphics. |
| **EU Declaration of Conformity (DoC) content** | Art. 19 & Annex IV – final compliance statement. | Completed DoC with referenced standards, NB certificate number, device identifier. |
| **EUDAMED registration details** | Art. 33‑39 – mandatory for all CE‑marked devices. | Unique Device Identifier (UDI), manufacturer & authorised representative data, notified body identification. |
| **Post‑Market Surveillance (PMS) Plan completeness (Art. 84)** | Source only shows a template; actual plan must address:  <br>• Data collection sources  <br>• Trend analysis  <br>• Periodic safety update report (PSUR) schedule | Fully populated PMS Plan with responsible persons, data‑flow diagram, trigger thresholds. |
| **PSUR content & timing** | Art. 86(1)/(2); source provides frequency only – the substantive content must be prepared. | PSUR draft covering sales volume, incident trends, PMCF results, benefit–risk conclusions. |

---

## 4. Risk‑Control Summary (aligned with GSPR)

| GSPR § | Typical hazard for each product | Control measure (evidence) |
|--------|--------------------------------|----------------------------|
| **§3 – Risk Management System** | All devices – residual risk not acceptable without controls | ISO 14971 RMF (risk analysis, evaluation, verification). |
| **§4 – Risk control measures** | X‑ray detector: radiation scattering; Handheld source: accidental exposure; SaMD: misinterpretation of images. | Design safeguards (shielding, interlocks), software validation, alarm limits, user training. |
| **§5 – Use‑error related hazards** | Incorrect positioning of handheld source; wrong settings on GUI. | Human‑factors testing (IEC 62366‑1), clear UI design, warning labels, lock‑out procedures. |
| **§6 – Device lifetime & maintenance** | Detector degradation; tube wear for source. | Defined maintenance schedule, performance verification after defined usage cycles, calibration logs. |
| **§7 – Transport & storage** | Physical damage to detector, source leakage during transport. | Protective packaging, transport risk assessment, environmental specifications. |
| **§8 – Benefit–risk analysis** | Must be documented in CER/PMCF report. | Evidence of clinical benefit (diagnostic accuracy), quantified residual risk below acceptable thresholds. |
| **§16 – Radiation protection** | Applicable to detector and source. | Compliance with IEC 60601‑2‑54, IEC 60601‑2‑28; dose‑measurement verification; shielding calculations. |
| **§17 – Electronic programmable systems** | SaMD & source controller firmware upgrades. | Secure software development lifecycle (IEC 62304), version control, cybersecurity assessment. |
| **§22 – Devices for lay persons** | GUI may be used by non‑expert staff in imaging rooms. | Usability testing, simplified IFU, training modules. |

All controls must be traceable to the corresponding GSPR clause in the Technical Documentation (Annex II §5).

---

## 5. Human‑Escalation Triggers

| Trigger | Reason for escalation | Immediate action |
|---------|-----------------------|------------------|
| **Classification uncertainty** (e.g., X‑ray Detector listed as “Class IIa/IIb”) | Wrong classification leads to inappropriate NB route and non‑conformity findings. | Convene a *Classification Review Board* with regulatory, clinical, and engineering experts; document decision; update all downstream documents. |
| **Missing intended‑use statement or ambiguous claim** | Prevents proper risk analysis and clinical evaluation scope. | Halt submission preparation; request definitive marketing authorisation wording from product management. |
| **Insufficient clinical data for CER (e.g., no pre‑market study for SaMD)** | NB will reject the technical file. | Initiate a feasibility study or literature search; consider performing a small‑scale clinical investigation (Annex X). |
| **PMS Plan not populated with actual data sources** | Art. 84 requires an operational PMS system before CE marking can be issued. | Pause CE‑marking timeline; assign a PMS lead to complete the plan and define data‑collection responsibilities. |
| **Failure to meet PSUR frequency (e.g., annual for Handheld source) or missing content** | Non‑compliance with Art. 86 → possible suspension of certificate. | Schedule urgent drafting of PSUR; allocate resources for data extraction from vigilance system. |
| **NB audit raises non‑conformities in QMS (Annex IX)** | Direct impact on conformity assessment outcome. | Trigger corrective‑and‑preventive action (CAPA) process; involve Quality Manager and senior management. |
| **Usability testing reveals critical use‑error** | Violation of GSPR §5/§22; safety risk. | Suspend market release; redesign UI or add training; re‑run usability validation before proceeding. |

Escalations must be logged in the project’s risk register (ISO 14971) and communicated to senior management and the authorised representative.

---

## 6. Peer‑Review Request

> **Action:** Please have a fellow Regulatory Affairs colleague review this draft, focusing on:
> 
> 1. **Assumptions about classification** – Are Rule 17 for the detector, Rule 10 for the handheld source, and Rule 11 for the SaMD definitively appropriate given the limited product description?
> 2. **Completeness of the evidence checklist** – Is any mandatory MDR element (e.g., environmental impact assessment, cybersecurity considerations) missing for these devices?
> 3. **Jurisdiction‑specific gaps** – Does the draft adequately separate EU requirements from extraneous references (FDA 522, MFDS) while still noting their presence in the source matrix?

Feedback should be added as comments or a separate annotation document.

---

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
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1002815045680049480`

> ## 3. PMS Plan 실용 템플릿 (MDCG 2025-10 기반) `[추가확인]` 표시 항목은 자사 확인 후 기재. ---

2. Chunk `1142345122918011337`

> ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (추정) | PMS Plan 의무 | 보고서 유형 | FDA 522 | MFDS 시판후조사 | |---|---|---|---|---|---| | **X-ray Detector** | Class IIa/IIb | **필수** | PSUR 2년/매년 | 해당 없음 (비이식형) | 신개발 시 3~4년 조사 | | **Handheld X-ray Source** | Class IIb | **필수** | PSUR 매년 | 해당 없음 (비이식형) | 신개발 시 4~6년 조사 | | **촬영실 GUI SW (SaMD)** | Class IIa (MDR §22) | **필수** | PSUR 2년 | 해당 없음 | 소프트웨어 신개발 시 해당 | ---

## ra_kr

### kb-eval-20261110-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "2736235b59aa47de", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "00026234f8ec1153306309dc7c82b355b5fdfc4d7a5de00dbd5247374b13eccb"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2736235b59aa47de`
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

> **Regulatory Draft – Impact of the Korean Digital Medical Devices Act (디지털의료제품법) on the X‑ray System Project**

---

### 1. Product Scope & Functional Decomposition
| Component | Current Functionality | Preliminary Digital‑Medical‑Device Determination* |
|-----------|----------------------|---------------------------------------------------|
| **Generator firmware** | Hardware‑control only, no network connectivity | Not a digital medical device (X) |
| **Detector firmware** | Firmware for detector; may be network‑enabled in some configurations | Potentially applicable when networked (△) |
| **Acquisition Workstation Software** | Stand‑alone operation, network capable, includes AI‑assisted image acquisition | Digital medical device (○) |
| **Image‑post‑processing & AI analysis module** | Performs automated interpretation / diagnosis support | SaMD + AI (○) – falls under 디지털의료제품법 |
| **DICOM transmission / PACS interface** | Data exchange function; may be implemented as independent software | Possibly applicable when realized as standalone SW (△) |

\*Based on the provisional matrix in source excerpt [2].

---

### 2. Regulatory Applicability

| Legal Framework | Relevance to Project |
|-----------------|----------------------|
| **디지털의료제품법** (Digital Medical Devices Act) | Applies to any software or device that performs medical functions, including AI‑driven diagnosis and network‑enabled image acquisition. The Acquisition Workstation SW and the AI analysis module are clearly within scope; the Detector firmware may become in‑scope if networked. |
| **Medical Device Law (의료기기법)** | Governs hardware elements that are classified as medical devices (e.g., X‑ray generator, detector). Classification must be confirmed against 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **MFDS SBOM Guidance** (effective 2025‑01‑10) | Requires submission of a Software Bill of Materials (SBOM) in SPDX 2.3 or CycloneDX 1.5 format, covering the NTIA 7 elements plus EOL and vulnerability data. The guidance is cited in source excerpt [1] (MFDS 2025‑01‑10; 보안지침 제16조). |
| **ISO/IEC Standards** | • ISO 14971:2019 – Risk Management <br>• ISO 13485:2016 – QMS for KGMP certification <br>• IEC 62304:2006+A1:2015 – Software Lifecycle Processes (mandatory for SaMD) |

---

### 3. Classification & Submission Route (Korean Grades)

| Component | Tentative Grade¹ | Required MFDS Pathway |
|-----------|------------------|------------------------|
| Generator firmware / hardware | **1등급** (non‑medical or minimal risk) → 신고 (notification) *if classified as a medical device* |
| Detector firmware (networked) | **2등급** – likely requires 인증 (technical‑document review by MFDS‑designated 심사기관) |
| Acquisition Workstation SW | **3등급·4등급** – SaMD with AI functions generally fall into 3등급 or higher, thus 허가 (full approval) is expected |
| AI analysis module | Same as above – **3등급·4등급**, 허가 route |
| DICOM/PACS interface | **2등급** (if considered a medical device software) → 인증 |

¹ The exact grade must be verified against the current 「의료기기 품목 및 품목별 등급에 관한 규정」. No specific grade appears in the source excerpts; therefore, the above are provisional assessments.

---

### 4. Required Evidence Package

| Requirement | Evidence Needed | Source / Reference |
|-------------|-----------------|---------------------|
| **SBOM** (for all software components) | SPDX 2.3 or CycloneDX 1.5 file including NTIA 7 elements, EOL dates, known vulnerabilities | MFDS 2025‑01‑10 guidance; 보안지침 제16조 |
| **Risk Management File** | ISO 14971‑based risk analysis, hazard log, mitigation verification; for AI module include post‑market performance monitoring plan (PMCF) | ISO 14971:2019 (framework reference) |
| **Software Life‑Cycle Documentation** | IEC 62304 compliance evidence (planning, development, verification, maintenance); version control & change management records | IEC 62304:2006+A1:2015 |
| **Clinical Evaluation** | For AI analysis module, a clinical evaluation report (CER) demonstrating safety/efficacy in Korean population; if foreign data are used, confirm MFDS acceptance of overseas CERs per latest notice (requires verification) | 디지털의료제품법 & MFDS 고시 (no specific identifier provided – verify separately) |
| **KGMP / QMS Certification** | For hardware items classified as medical devices (generator, detector), KGMP facility certification and ISO 13485‑based quality system documentation | KGMP legislation (framework reference) |
| **Labeling & IFU** | Korean language labeling, user manual, and for software a clear description of intended use, contraindications, and user responsibilities | MFDS labeling requirement (no specific article cited – verify separately) |
| **Cybersecurity Plan** | Alignment with MFDS 보안지침 제16조; include vulnerability management, incident response, and periodic SBOM updates | 보안지침 제16조 (instance identifier from source [1]) |

---

### 5. Identified Gaps / Missing Information

| Gap | Impact if Unaddressed |
|-----|-----------------------|
| **Exact device grade** for each component | Incorrect submission pathway; possible re‑submission or regulatory delay |
| **Local clinical data for AI module** (Korean patient cohort) | MFDS may reject foreign CER; may require additional local study |
| **KGMP certification evidence for hardware** (if any component falls under 1~4등급) | Failure to meet manufacturing compliance → 허가 denial |
| **Complete SBOM covering all third‑party libraries** (including version hashes) | Non‑conformity with MFDS SBOM guidance; security assessment may be rejected |
| **Detailed cybersecurity incident response plan** | Insufficient for 보안지침 제16조 compliance; could trigger post‑market enforcement |
| **Korean‑language labeling and IFU for software** | Violates label language requirement; product cannot be marketed |

---

### 6. Core Risk Controls (to be incorporated)

1. **Risk Management** – Full ISO 14971 process with regular updates as AI model evolves.
2. **Software Lifecycle** – IEC 62304‑compliant development, configuration management, and traceability matrix linking requirements to code modules.
3. **Cybersecurity** – Adopt a “defense‑in‑depth” architecture; maintain up‑to‑date SBOM; conduct periodic vulnerability scans; implement secure OTA update mechanism.
4. **Clinical Performance Monitoring** – PMCF plan for AI module with real‑world data collection, drift detection, and corrective action thresholds.
5. **Quality Management System** – KGMP/ISO 13485 certified QMS at the manufacturing site; routine internal audits.
6. **User Training & Instructions** – Korean IFU detailing proper network configuration, maintenance of SBOM, and reporting of adverse events.

---

### 7. Citations

| Item | Citation Type | Reference |
|------|--------------|-----------|
| MFDS SBOM guidance (date) | Instance identifier | MFDS 2025‑01‑10; 보안지침 제16조 (source [1]) |
| NTIA 7 elements + EOL + vulnerability requirement | Framework reference | NB – derived from source matrix, no specific instrument number |
| SPDX 2.3 / CycloneDX 1.5 recommendation | Framework reference | Source [1] “SPDX 2.3 또는 CycloneDX 1.5 채택” |
| Digital‑Medical‑Device applicability matrix (X‑ray system) | Instance identifier | Table in source [2] (no specific article number) – *no specific identifier found in source — verify separately* |
| ISO 14971:2019, ISO 13485:2016, IEC 62304:2006+A1:2015 | Framework references | Standard editions listed in the verified reference table |

---

### 8. Human‑Escalation Triggers

| Trigger Condition | Action Required |
|-------------------|------------------|
| **Uncertain device grade** after review of 「의료기기 품목 및 품목별 등급에 관한 규정」 | Escalate to senior RA for definitive classification decision before dossier finalization. |
| **Missing or incomplete SBOM** (e.g., lacking NTIA 7 elements) | Pause submission; request development team to produce compliant SBOM; notify project manager. |
| **Foreign clinical evidence is the sole basis for AI module safety** without confirmed MFDS acceptance | Initiate a feasibility study for Korean‑subject data; involve clinical affairs lead. |
| **Security vulnerability identified post‑submission** that impacts any listed component | Activate cybersecurity incident response; prepare amendment dossier (supplement SBOM, patch plan) and submit to MFDS as per 보안지침 제16조. |
| **Change in AI algorithm performance after market launch** (drift beyond predefined limits) | Trigger PMCF corrective action workflow; draft supplemental approval package for MFDS. |
| **KGMP certification not yet granted for hardware manufacturer** | Halt any hardware‑related filing until KGMP audit is passed; inform manufacturing QA. |

---

### 9. Reusable RA Judgment (Lesson Learned)

- **Digital‑medical‑device scope must be assessed at the component level**; network connectivity and AI capability are decisive factors under 디지털의료제품법.
- **MFDS SBOM guidance (2025‑01‑10, 보안지침 제16조) aligns with both FDA 524B and EU MDR requirements**, allowing a single SPDX 2.3 or CycloneDX 1.5 file to satisfy all three regimes.
- **Classification grades in Korea are independent of foreign class nomenclature**; always reference the Korean “1등급·2등급·3등급·4등급” system and verify against the official 규정 before selecting 신고/인증/허가 pathways.
- **Risk management, cybersecurity, and clinical evaluation are inseparable for SaMD with AI**, and must be documented in Korean‑language deliverables to meet MFDS expectations.  

---  

**Peer Review Prompt**

> Please review the above draft:  
> • Are the assumptions about component applicability under 디지털의료제품법 fully supported by the source excerpts?  
> • Is the coverage of SBOM requirements (format, content, timing) adequate given the MFDS guidance cited?  
> • Identify any jurisdiction‑specific gaps (e.g., local clinical data, KGMP evidence) that may need additional sources or clarification.

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
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

Generator 하드웨어 1등급 신고 안내 오류(X-ray 발생장치는 2~3등급) + 디지털의료제품법 범위 과잉 일반화. shadow 하향 수용.

**Source Excerpts**

1. Chunk `1055466385786976527`

> ## 1. FDA vs MDR vs MFDS — SBOM 요구사항 정합성 | 축 | 요구 시점 | 포맷 | 필수 항목 | 제출 방식 | 사후 갱신 | |----|-----------|------|-----------|-----------|-----------| | FDA (524B) | Premarket (2023-10-01 RTA 강제) | SPDX 2.3 / CycloneDX 1.5 | NTIA 7요소 + EOL + 취약점 | eSTAR 제출물 | Section 524B Postmarket Plan | | MDR (MDCG 2019-16) | Technical Documentation Annex II | 포맷 권고 없음, IMDRF N73 원칙 | NTIA 7요소 + License + Hash | NB 심사 자료 | PMS Plan/PSUR 포함 | | MFDS (2025-01-10) | 국내 허가 심사 | 권고 (SPDX/CycloneDX) | RA-07 항목 | 심사 자료 (권고) | 보안 지침 제16조 SBOM 관리 | **정합성 판정: 본 SOP-SBOM-001 v0.1은 3축 모두 수용 가능한 상위 호환 설계** - SPDX 2.3 또는 CycloneDX 1.5 채택 → FDA/MDR/MFDS 동시 만족 - NTIA Baseli...

2. Chunk `418096885713027360`

> ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 |

### kb-eval-20261110-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "cf93a03c01100bde", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `cf93a03c01100bde`
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

> **Regulatory Draft – Independent Imaging‑Room GUI Software (SaMD)  
Digital Medical Product – Impact of the Digital‑Medical‑Products Act**

---

## 1. Korean Regulatory Classification & Submission Route  

| Item | Assessment | Comment |
|------|------------|---------|
| **Device grade** | *Not specified in source* → must be confirmed by consulting 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS_인허가_상세가이드.md §2). | If the software is intended for diagnosis or therapy, Korean practice generally places it in **3등급·4등급 → 허가**. If only a support tool, it may be **2등급 → 인증**. |
| **Submission track** | Determined by confirmed grade: <br>‑ 1등급 → 신고  <br>‑ 2등급 → 인증 (MFDS‑designated 심사기관)  <br>‑ 3~4등급 → 허가 (MFDS 직접 승인) | **Human escalation trigger:** grade uncertain → pause submission preparation and request formal classification determination from MFDS. |

---

## 2. Required Evidence Package (Korean ‑ Korean‑language focus)

| Evidence Category | Korean Requirement | Mapping to Foreign / International Evidence | Source citation |
|-------------------|-------------------|--------------------------------------------|-----------------|
| **QMS compliance** | KGMP 인증 (의료기기법 제28조) – full QMS, internal audit records, management review minutes in Korean. | ISO 13485:2016 compliance is required but **insufficient alone**; must embed ARR activities (UDI, MDR‑type reporting, corrections & removals). | FDA CFR §820.10(b); §820.35(a) – cited as example of ARR requirement that MFDS also expects “ARR 준수 활동 통합”. |
| **Software lifecycle documentation** | • SW 개발 수명주기 문서 (SDP, SRS, SAD, SVP, SVR) <br>• 검증·확인 계획 및 결과 보고서 <br>• 변경 관리 SOP | IEC 62304:2006+A1:2015 §8.1 – Safety Class C (required for “촬영실 GUI SW”). | IEC 62304 §8.1 – framework reference. |
| **Cyber‑security** | MFDS 사이버보안 가이드라인 2025 – threat model, SBOM, PCCP integration; Korean language security plan and incident response flowchart. | FDA 524B (PCCP) & MDCG 2019‑16 Rev.1 used as supporting foreign evidence **only if MFDS accepts** (see §6). | No specific identifier in source – verify separately. |
| **AI/ML functionality (if present)** | Conformity assessment per 디지털의료제품법 + MFDS AI‑related guidance; Korean risk‑benefit analysis, explainability report. | EU AI Act Art. 43(4) & FDA PCCP 2024‑12‑03 Final can be submitted as supplementary foreign evidence **subject to MFDS acceptance of CER** (OECD MAD does not cover AI/ML). | No specific identifier in source – verify separately. |
| **Clinical Evidence** | • Korean clinical evaluation (if local data required for the grade) <br>• Foreign Clinical Evaluation Report (CER) accepted per MFDS notice (when allowed) | FDA 510(k) predicate, CE‑Mark technical file can be referenced **only if MFDS has issued a specific notice allowing foreign CER**. | No specific identifier in source – verify separately. |
| **Labeling & IFU** | All labeling, instructions for use, and software user manual must be in Korean; contain UDI (21 CFR 830 equivalent) and post‑market reporting contact. | FDA §820.120 (labeling) provides analogous structure but MFDS requires Korean translation. | No specific identifier in source – verify separately. |
| **Post‑Market Surveillance (시판후조사)** | PMS plan, periodic safety update, adverse event reporting system (30 일 내 보고). | MDR 30‑day report requirement referenced in excerpt (“불만 처리 → MFDS 보고 → MDR 30일…”). | FDA CFR §820.35 (service record) – cited as a comparative element. |
| **UDI implementation** | Registration of device with Korean UDI system; barcode/QR code on packaging, data submitted to MFDS DB. | FDA 21 CFR 830 – required separately in Korea. | No specific identifier in source – verify separately. |

---

## 3. Gaps / Missing Information (to be obtained before submission)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Confirmed device grade** (1‑4등급) | Determines submission track & depth of clinical evidence required. | Request formal classification from MFDS or perform self‑classification per 규정 and obtain confirmation. |
| **Korean‑language labeling & IFU drafts** | Mandatory for all grades; missing translation blocks approval. | Prepare Korean texts, include UDI, symbols, safety notices. |
| **Local clinical data (if required)** | Required when foreign CER not accepted or when high risk (≥3등급). | Conduct Korean pilot study or collect real‑world evidence per 디지털의료제품법. |
| **Detailed cyber‑security plan** aligned with MFDS 사이버보안 가이드라인 2025 | MFDS will audit this document; without it, QMS certification fails. | Develop threat model, SBOM, incident response SOP in Korean. |
| **AI/ML risk management dossier (if AI present)** | High‑risk AI devices need separate conformity assessment under 디지털의료제품법. | Produce explainability & performance monitoring plan. |
| **Internal audit reports** (including access for MFDS auditors) | FDA excerpt shows internal audit now visible to inspectors; Korean MFDS expects similar transparency. | Capture audit minutes, corrective actions; ensure availability in Korean. |
| **UDI registration evidence** | Required for all grades; absence delays market entry. | Submit UDI data to MFDS DB; retain certification of labeling. |
| **Post‑market safety update schedule** | PMS plan must be filed with MFDS; gaps cause non‑compliance. | Define reporting frequency, escalation thresholds. |

---

## 4. Key Risk Controls (mapped to Korean requirements)

1. **Software Development Lifecycle (SDLC) controls** – IEC 62304 Class C compliance, documented design inputs/outputs, verification & validation in KGMP QMS.
2. **Change Management** – SOP for software updates, regression‑test automation; documented in Korean change‑control logs.
3. **Cyber‑security safeguards** – Threat modeling, SBOM, periodic penetration testing per MFDS 사이버보안 가이드라인 2025.
4. **AI/ML monitoring** – Continuous performance monitoring, drift detection, re‑training procedures (if AI present).
5. **Complaint handling & MDR reporting** – Process to assess complaint for reportability within 30 days; records in Korean service logs.
6. **Internal audit & management review** – Records of audits and reviews stored and made accessible to MFDS inspectors (per FDA §820.180(c) analogy).
7. **UDI & traceability** – Barcode/QR code on device, linkage to manufacturing lot, maintained in KGMP batch records.

---

## 5. Human‑Escalation Triggers  

| Trigger | Situation | Required Action |
|--------|-----------|-----------------|
| **Uncertain device grade** | No clear grade from source; conflicting functional description. | Pause all downstream activities and submit a formal inquiry to MFDS (or consult regulatory counsel) for classification decision. |
| **Foreign evidence acceptance gap** | Need to rely on FDA 524B or EU AI Act but no MFDS notice confirming acceptance of such documents. | Escalate to senior RA lead; obtain MFDS guidance or supplemental local evidence before proceeding. |
| **Korean labeling draft not ready** | Korean translation incomplete after deadline for QMS audit. | Halt submission packaging; engage professional medical‑device translation service; document delay. |
| **Cyber‑security plan fails gap analysis** | Internal review identifies missing threat‑model components required by MFDS guideline 2025. | Escalate to CISO/Project Manager; allocate resources to remediate before KGMP audit. |
| **AI/ML risk assessment indicates high‑risk category** (per 디지털의료제품법) | Device re‑classified as 고위험 AI device. | Initiate additional conformity assessment, possibly a separate MFDS 허가 application; involve senior regulatory and legal teams. |
| **Post‑market surveillance plan not approved by internal QA** | PMS schedule conflicts with MFDS 30‑day reporting requirement. | Suspend market launch until PMS plan revised and signed off. |
| **Missing local clinical data** | FDA or CE evidence insufficient per MFDS notice; no Korean study available. | Escalate to clinical development team to design/execute required Korean study; pause submission. |

---

## 6. Citations  

| Item | Citation type | Source excerpt |
|------|--------------|----------------|
| ARR (Applicable Regulatory Requirements) – requirement to integrate UDI, MDR reporting, corrections & removals into QMS procedures. | Instance identifier (U.S. CFR) | §820.10(b) (excerpt [1]) |
| Complaint file enhancement – need to record MDR‑reportable status. | Instance identifier (U.S. CFR) | §820.35(a) (excerpt [1]) |
| Service record requirement. | Instance identifier (U.S. CFR) | §820.35 (excerpt [1]) |
| Internal audit visibility to regulators. | Instance identifier (U.S. CFR – general reference) | “§820 전반” (excerpt [1]) |
| Contract sterilizer & relabeler inclusion in QMS scope. | Instance identifier (U.S. CFR) | §820.10(a) (excerpt [1]) |
| SW development lifecycle mapping – IEC 62304 Safety Class C. | Framework reference (IEC standard) | IEC 62304 §8.1 (excerpt [2]) |
| Cyber‑security guidance – MFDS 사이버보안 가이드라인 2025. | Framework reference (MFDS guideline) | excerpt [2] |
| AI/ML function mapping – EU AI Act Art. 43(4). | Framework reference (EU regulation) | excerpt [2] |
| MDR 30‑day reporting mentioned in complaint handling row. | Framework reference (MDR) | “불만 처리 → MFDS 보고 → MDR 30일…” (excerpt [2]) |

*No specific Korean regulatory instrument numbers (e.g., 고시 제XXXX호, §23조) appear in the supplied excerpts; therefore they are omitted and flagged for separate verification.*

---

## 7. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review this draft and challenge the following points:  
> 1. The assumed need for Korean clinical data – could the device qualify for a “foreign CER accepted” pathway under any recent MFDS notice?  
> 2. Whether the mapping of FDA CFR sections to Korean ARR obligations is accurate, or if additional Korean-specific clauses (e.g., MFDS 고시 제2025‑22호) should be referenced.  
> 3. The classification inference for an imaging‑room GUI; are there precedents that would place it definitively in 2등급 → 인증 rather than higher grades?  
> 4. Any overlooked Korean‑language documentation (e.g., electronic submission format, e‑CTD requirements) that must be prepared before KGMP certification.  

Your feedback will determine if any gaps remain before we elevate this dossier to senior regulatory leadership.

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

### kb-eval-20261110-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "3de6ea24680df210", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `3de6ea24680df210`
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

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법) on Software‑Based AI/ML Devices**

---

### 1. Applicable Legal Framework  
- **Digital Medical Products Act (디지털의료제품법)** – governs “digital medical devices”, including standalone software (SaMD) and AI‑based image analysis modules.  
- Supporting MFDS guidance documents (2024‑2025) are listed in the source table [1]; the most relevant for a software‑centric product are:  

| Guideline (release) | Relevance | Targeted products |
|---|---|---|
| 디지털치료기기 임상시험 설계 가이드라인 (2024‑12) | 낮음 | DTx 전용 |
| **생성형 AI 의료기기 허가·심사 가이드라인** (2025‑01) | **중** | AI 영상 분석 모듈 |
| **독립형 디지털의료기기SW 사용적합성 가이드라인** (2025‑01) | **높음** | 콘솔 SW, 뷰어 SW |
| **의료기기 사이버보안 허가·심사 가이드라인(개정)** (2025‑01‑10) | **높음** | 네트워크 연결 기기 전체 |
| **디지털의료기기 전자적 침해행위 보안 지침(안)** (2025‑01) | **높음** | SBOM 관리 포함 |

*No specific MFDS notice numbers are provided in the source – verify the exact 고시 번호 separately before submission.*

---

### 2. Preliminary Device Description (placeholder)

| Attribute | Comment |
|---|---|
| **Product type** | Stand‑alone software that performs AI‑driven analysis of medical imaging (e.g., radiology, pathology). May also be bundled with a console/viewer application. |
| **Intended use** | Assist clinicians in diagnosis by providing image classification/segmentation outputs. No autonomous therapeutic decision making. |
| **Risk profile** | Software‑related hazards (incorrect output, data breach, algorithm drift) – typical for AI‑based diagnostic support tools. |

*Exact intended use statements are required to finalize classification.*

---

### 3. Classification & Submission Route  

| Korean grade (등급) | Typical devices in this grade | Submission pathway |
|---|---|---|
| **1등급** | Low‑risk, non‑invasive, no patient‑direct impact | 신고 (notification) |
| **2등급** | Moderate risk; many standalone SW fall here if clinical impact is limited | 인증 (technical‑document review by MFDS‑designated 심사기관) |
| **3등급·4등급** | High‑risk – AI that directly influences diagnosis/treatment decisions, or devices with invasive functions | 허가 (full MFDS approval) |

*Given the AI image‑analysis function, the device is likely to be classified as **3등급** or **4등급** under the Digital Medical Products Act. The final grade must be confirmed by consulting 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS 인허가_상세가이드.md §2).*

---

### 4. Required Submission Evidence  

| Evidence Category | Core items | Reference / Guideline |
|---|---|---|
| **Regulatory classification justification** | Risk analysis per ISO 14971:2019; mapping to MFDS grade criteria (no specific article number in source – verify separately) | ISO 14971 (2019) |
| **Clinical evaluation** | • Clinical performance data (local or acceptable foreign CER)<br>• If using foreign clinical data, confirm acceptance under MFDS’s OECD‑MAD scope (non‑clinical GLP only) and separate CER allowance (no single notice number in source) | 디지털의료제품법 (general requirement) |
| **Usability / Human factors** | IEC 62366‑1:2015+A1:2020 usability engineering plan (v0.2 completed – see SOP‑related entry in [2]) | IEC 62366‑1 |
| **Software validation & KGMP** | • Software Development Lifecycle documentation<br>• Verification & Validation reports per KGMP (의료기기법 제28조) | No specific identifier found – verify separately |
| **Cybersecurity** | • Cybersecurity risk assessment matrix (RA‑01 ~ RA‑20) – in progress per [2] <br>• SBOM management procedure (SOP‑SBOM‑001) – v0.2 completed <br>• Compliance with 2025‑01‑10 “의료기기 사이버보안 허가·심사 가이드라인” | 디지털의료제품법 관련 가이드라인 [1] |
| **AI model governance** | • Dataset description & provenance (SOP‑AIDATA‑001) <br>• Algorithm change management & performance monitoring plan (SOP‑AIGOV‑001) <br>• Component‑level performance evaluation (AI_구성요소_단위_성능평가) | SOPs listed in [2] |
| **Labeling & IFU** | Korean language labeling, symbols, and instructions for use per MFDS labeling rule (no specific article number in source – verify separately) | No specific identifier found – verify separately |
| **Post‑market surveillance (PMS)** | PMS plan, adverse event reporting, periodic safety update (Korean “시판후조사” requirements) | No specific identifier found – verify separately |

---

### 5. Gaps / Missing Information  

| Item | Why it is needed | Current status |
|---|---|---|
| **Exact intended use & claim wording** | Determines grade and clinical evidence scope | Not provided |
| **Confirmation of whether foreign clinical data can be leveraged** | Affects need for local trial (MFDS often requires Korean data for 3/4등급) | No specific guidance in source |
| **Full MFDS 고시 numbers for the cybersecurity and SBOM guidelines** | Required citations on submission forms | Not present – must be retrieved from MFDS Gazette |
| **Korean labeling text & packaging artwork** | Mandatory for all grades | Absent |
| **Risk management file (ISO 14971) with finalized hazard list** | Basis for classification & safety claim | Not yet compiled |

---

### 6. Key Risk Controls to Embed  

1. **Hazard analysis & risk mitigation** – ISO 14971‑based RMF covering software errors, AI misclassification, data integrity, and cybersecurity threats.  
2. **Usability engineering** – IEC 62366‑1 compliance; user interface validation with representative clinicians.  
3. **Cybersecurity architecture** – Network segmentation, encryption, authentication, regular vulnerability scanning; SBOM maintained and updated per the “디지털의료기기 전자적 침해행위 보안 지침”.  
4. **AI model monitoring** – Continuous performance tracking against ground‑truth datasets; drift detection triggers periodic re‑validation.  
5. **Change control** – Documented procedures (SOP‑CC‑001) for software updates, AI algorithm revisions, and SBOM amendments.  
6. **Post‑market surveillance** – Real‑world data collection, adverse event reporting, periodic safety update per MFDS PMS regulations.

---

### 7. Human‑Escalation Triggers  

| Trigger | Action & Responsible Role |
|---|---|
| **Uncertain grade (potential 3등급/4등급)** | Senior RA lead reviews risk file; if ≥3등급, initiate MFDS 허가 project charter and secure senior management approval. |
| **Missing Korean labeling** | Escalate to Regulatory Affairs – Language & Labeling Lead for immediate translation and review. |
| **Incomplete cybersecurity matrix (RA‑01 ~ RA‑20) or SBOM gaps** | Raise to CISO / Security Engineer; halt submission until full compliance with the 2025‑01‑10 cyber‑security guideline is documented. |
| **Insufficient clinical evidence for high grade** | Trigger Clinical Development Team to design local pilot study; pause MFDS 허가 dossier assembly. |
| **Algorithm change without governance SOP** | Stop any software release; convene AI Governance Committee to finalize SOP‑AIGOV‑001 before proceeding. |
| **Regulatory notice numbers not verified** | Regulatory compliance officer must retrieve exact 고시 번호 from the MFDS Gazette and update all submission references. |

---

### 8. Next Steps (Action Items)

1. Acquire the precise **MFDS 고시/notice numbers** for the cybersecurity, SBOM, and AI‑governance guidelines (search MFDS 공고 database).  
2. Finalize **intended use statement** and perform a formal **risk classification** per the Digital Medical Products Act.  
3. Complete the **cybersecurity RA matrix** (RA‑01 ~ RA‑20) and align it with the high‑relevance guidelines [1].  
4. Draft the **Korean labeling package** (user manual, IFU, packaging).  
5. Determine whether **foreign clinical data** can be accepted; if not, plan a Korean clinical trial.  

---

### Peer‑Review Prompt  

> *Colleague RA, please review this draft and challenge: (1) the assumption that the AI image‑analysis module will fall into 3등급/4등급 without an explicit claim analysis, (2) whether the source coverage of guidance documents fully addresses the required evidence for a SaMD under 디지털의료제품법, and (3) any jurisdiction‑specific gaps (e.g., missing 고시 번호, local clinical data obligations) that need to be filled before we can lock the submission strategy.*

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
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

등급 판정 근거를 디지털의료제품법으로 오귀속(등급은 의료기기법 규정 소관) — 제28조 이의는 기각(KB GMP_심사자료 정당). 부분 수용.

**Source Excerpts**

1. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

2. Chunk `1130453648414545903`

> ## 8. 후속 조치 요건 (프로젝트 관점) | 우선순위 | 조치 사항 | 연계 문서 | 상태 | |----------|----------|-----------|------| | 1 | 사이버보안 RA-01~RA-20 대응 매트릭스 작성 | 디지털의료제품법_요구사항_매트릭스 | 진행중 | | 2 | 사용적합성 엔지니어링 계획 수립 | IEC_62366-1_사용적합성_엔지니어링_계획서 | v0.2 완료 | | 3 | SBOM 관리 절차 정합성 확인 | SOP-SBOM-001 | v0.2 완료 | | 4 | 변경관리 계획 SOP 연계 (CMP 섹션) | SOP-CC-001 | v0.2 완료 | | 5 | AI 모델 데이터셋·거버넌스 절차 수립 | SOP-AIDATA-001, SOP-AIGOV-001 | v0.2 완료 | | 6 | 구성요소 단위 성능평가 절차 문서화 | AI_구성요소_단위_성능평가 | v0.2 완료 |

### kb-eval-20261110-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "e447239ab41b1c47", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `e447239ab41b1c47`
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

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법) on a SaMD‑type digital health solution**

---

### 1. Product Synopsis  
- **Intended use:** Software‑only medical device that provides diagnostic assistance based on AI/ML algorithms and presents results through a graphical user interface (GUI).  
- **Key characteristics:** No hardware component, operates on patient‑owned mobile devices, continuous updates to the algorithm are planned.

---

### 2. Korean Classification & Submission Route  

| Korean grade | Typical pathway | Preliminary finding for this SaMD |
|--------------|----------------|-------------------------------------|
| **1등급** – 신고 | Notification (신고) | Not applicable – software with diagnostic function exceeds low‑risk criteria. |
| **2등급** – 인증 | Certification by an MFDS‑designated 심사기관 (e.g., KTL, KTR…) | Possible only if the device is deemed “low‑to‑moderate risk” and does not fall under the new SaMD rules. The 2025 amendment to the Digital Medical Products Act explicitly changes SaMD classification; therefore a **2등급 인증** would be unlikely. |
| **3등급·4등급** – 허가 | Full MFDS approval (허가) | Most AI‑driven diagnostic software is now classified as **3등급 or 4등급**, requiring full 허가. The exact grade must be determined by applying the SaMD classification matrix in the “디지털의료제품법 시행” (effective 2025‑01‑24). No specific grade is stated in the source material, so **grade determination must be verified with the MFDS 규정**. |

> **Citation:** classification framework is derived from Korean law; see MFDS_인허가_상세가이드.md §2 (framework reference – no specific instrument number quoted in source).

---

### 3. Required Regulatory Evidence  

| Evidence Category | Typical Requirement under Korean Law | Gap / Action Needed |
|-------------------|---------------------------------------|---------------------|
| **KGMP compliance** | GMP 적합인정 required for manufacturing sites (including software development facilities). The process includes quality‑document review, on‑site audit, and issuance of a 3‑year certificate. | Identify the appropriate 심사기관; since **NIDS** now performs GMP 판정 for digital medical devices as of 2025‑01‑24【1】, NIDS must be considered when selecting the reviewing body. |
| **Technical Documentation (품질경영 시스템·기술문서)** | Detailed design dossier, risk management file (ISO 14971:2019), software lifecycle documentation (IEC 62304:2006+A1:2015). | Existing files may need updates to address AI/ML “continuous learning” aspects and the new Korean‑specific clinical evaluation expectations. |
| **Clinical Evaluation / Clinical Data** | For SaMD, MFDS now requires a dedicated clinical evaluation report (CER) that aligns with the AI/ML guidance released 2025‑05‑07【2】. Local Korean data are generally required for 3등급·4등급 devices unless an exemption is granted via OECD mutual acceptance of non‑clinical GLP data (MAD) – note that MAD covers **only non‑clinical** data, not clinical reports. | Determine whether foreign CERs (e.g., FDA 510(k) or EU CE technical files) can be partially accepted; if not, plan Korean post‑market or pre‑market clinical study. |
| **Software Validation & Cybersecurity** | Compliance with IEC 62366‑1:2020 (usability), IEC 81001‑5‑1:2021 (cybersecurity) and MFDS 사이버보안 가이드라인. The upcoming “autonomous performance certification” (2026 예정) will likely add a pre‑market security assessment. | Conduct a gap analysis against the current Korean cybersecurity guidelines; prepare for future autonomous certification requirements. |
| **Labeling & IFU** | All labeling, instructions for use, and marketing materials must be provided in Korean. The MFDS requires specific content items (e.g., intended purpose, contraindications) per the “디지털의료기기 가이드라인”. | Translate all user‑facing documents and verify inclusion of mandatory Korean language elements. |
| **Post‑Market Surveillance (시판후조사)** | Ongoing safety monitoring, adverse event reporting to MFDS, periodic safety update reports as required for 3등급·4등급 devices. | Develop a Korean‑language PMS plan aligned with MFDS 시판후조사 규정. |

> **Citation:** introduction of NIDS GMP role【1】; AI/ML GUI classification & clinical requirements in MFDS guideline amendment dated 2025‑05‑07【2】. No specific 고시 or 조항 numbers are supplied in the source – “no specific identifier found in source — verify separately”.

---

### 4. Missing Information / Open Questions  

| Item | Why it matters | Next step |
|------|----------------|-----------|
| **Exact Korean grade (3등급 vs 4등급)** | Determines depth of clinical evidence and review body. | Apply the SaMD classification matrix from the Digital Medical Products Act (effective 2025‑01‑24); request clarification from MFDS or a certified 심사기관. |
| **Whether foreign CER can be accepted** | Could reduce need for Korean clinical trial. | Submit a pre‑submission inquiry to MFDS citing OECD MAD scope (non‑clinical only) and ask about partial acceptance of foreign clinical data. |
| **Chosen GMP 심사기관** | NIDS now eligible, but other agencies still applicable. | Evaluate capacity of NIDS vs traditional agencies (KTL, KTR,…); decide based on timeline and expertise. |
| **Details of the upcoming autonomous performance certification scheme (2026 예정)** | May affect future submissions for updated algorithm versions. | Monitor MFDS announcements; incorporate a flexible “post‑approval change management” plan. |
| **Specific Korean labeling format requirements** | Non‑compliance leads to rejection at 허가 stage. | Obtain the latest MFDS 라벨링 가이드라인 (latest 고시) – currently not listed in source. |

---

### 5. Core Risk Controls (aligned with ISO 14971:2019)

1. **Algorithm Transparency & Explainability** – Document model architecture, training data sources, and validation metrics; provide a risk‑based justification for the level of clinical evidence required.  
2. **Continuous Learning Governance** – Define a change‑control process that distinguishes “important changes” (requiring pre‑approval) from “minor changes” (post‑market notification), reflecting the upcoming “negative‑pathway change approval” planned for 2026【2】.  
3. **Cybersecurity Defense in Depth** – Implement secure coding standards, regular penetration testing, and a vulnerability management plan per IEC 81001‑5‑1:2021 and MFDS cybersecurity guidance.  
4. **Usability Testing (IEC 62366‑1)** – Conduct formative and summative usability studies with Korean end‑users to mitigate use‑error risks.  
5. **Post‑Market Surveillance System** – Real‑time adverse event capture, trend analysis, and corrective action mechanisms aligned with MFDS 시판후조사 obligations.

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Responsible role |
|--------|-----------------------|------------------|
| **Unclear device grade** (cannot assign 3등급/4등급) | Grade determines the entire submission pathway; misclassification leads to regulatory rejection. | RA Lead → seek MF DS clarification. |
| **MFDS rejects foreign CER** | Necessitates rapid planning of a Korean clinical study, impacting timelines. | Clinical Development Manager → initiate local trial protocol. |
| **NIDS‑based GMP assessment not feasible within project timeline** | Could delay issuance of 적합인정서 (valid 3 years). | Project Manager → evaluate alternative 심사기관 and update schedule. |
| **Regulatory change notice on autonomous performance certification released** (post‑2026) | May require redesign of change‑management process for future algorithm updates. | Regulatory Strategy Lead → revise SOPs and inform product team. |
| **Cybersecurity audit identifies critical vulnerabilities** | Must be remedied before 허가 submission; non‑compliance can halt approval. | QA/Engineering → issue remediation plan and re‑test. |

---

### 7. References  

- **Framework references** – Korean device classification rules (MFDS_인허가_상세가이드.md §2); ISO 14971:2019; IEC 62304 (2006+A1:2015); IEC 62366‑1 (2020); IEC 81001‑5‑1 (2021).  
- **Source excerpts** – GMP 적합인정 절차 and NIDS role【1】; 2025–2026 regulatory change timeline, including Digital Medical Products Act enactment (2025‑01‑24) and MFDS AI/ML guideline amendment (2025‑05‑07)【2】.  
- **No specific 고시/조항 numbers** found in the provided source – “no specific identifier found in source — verify separately”.

---

### 8. Peer Review Prompt  

*“Please review this draft for any assumptions made about the SaMD classification under the Digital Medical Products Act, the applicability of foreign clinical evaluation reports, and the selection of a GMP 심사기관 (including NIDS). Are there additional Korean regulatory instruments or recent MFDS 고시 that should be referenced to close the identified gaps?”*

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
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

법 시행=개정(amendment) 오서술 + '2등급 인증 unlikely' 근거 없는 추론 단정. shadow 하향 수용.

**Source Excerpts**

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---

### kb-eval-20261110-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-10", "decision_ref": "kb-eval-20261110-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "5e38cfd3a482e9b5", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md", "source_hash": "eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5e38cfd3a482e9b5`
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

> **Regulatory Draft – Digital‑Medical Product Impact under the Korean 디지털의료제품법**

---

### 1. Classification & Submission Route  

| Item | Regulatory basis | Likely grade (Korean) | Submission track |
|------|------------------|----------------------|-------------------|
| Digital medical product that incorporates software, AI‑based decision support, and autonomous functionality | “디지털의료제품법” together with the **Medical Device Act** (의료기기법) – devices are classified according to risk level defined in 「의료기기 품목 및 품목별 등급에 관한 규정」. The source does not state a specific grade; the product appears to involve high‑risk functions (AI explainability, autonomous performance). | **3등급 or 4등급** is probable, but the exact grade must be confirmed from the official grade list. | For 3·4등급 devices the pathway is **허가** (MFDS approval) – full technical‑document review by MFDS.  

*If the product were determined to be a low‑risk software tool (e.g., only data collection), it could fall into 1등급 or 2등급, which would shift the route to 신고 or 인증 respectively. The definitive grade must be verified against the latest “의료기기 품목 및 품목별 등 gradation 규정”.*  

---

### 2. Required Evidence (as reflected in the source)  

| Requirement | Where it is satisfied (source) | Where a gap remains |
|-------------|--------------------------------|---------------------|
| **Security guidance compliance** – MFDS 보안지침 제16조 | ✅ Covered by DR‑09 (SBOM) – cross‑referenced to MFDS 보안지침 제16조. | — |
| **Software Bill of Materials (SBOM)** | ✅ DR‑09 verifies SBOM alignment with FDA §524B and MDR Annex I §17.4. | — |
| **Post‑Market Surveillance (PMS) reporting** | ✅ DR‑14 matches PMS 고시 timing. | — |
| **Unique Device Identification (UDI) system** | ✅ DR‑19 notes coverage by 의료기기법 + 디지털의료제품법 and SOP‑UDI(issue 002). | — |
| **Risk Management** – ISO 14971 process | ✅ DR‑21 references ISO 14971 (process detailed in issue 007). | — |
| **Software Lifecycle Documentation** – IEC 62304 | ✅ DR‑22 cites full coverage via SW lifecycle documents (issue 006). | — |
| **Usability Engineering** – IEC 62366‑1 plan | ❌ DR‑06 shows the template is *未定* (missing). |
| **Component Performance Evaluation SOP** | ❌ DR‑05 indicates a complete lack of such SOP. |
| **Labeling/Display Material Template for Digital Devices** | ❌ DR‑10 reports no Korean labeling template has been prepared. |
| **Independent Software Suitability Assessment Procedure** | ❌ DR‑11 notes the procedure is absent. |
| **Autonomous Performance Certification Playbook** | ❌ DR‑15 indicates this playbook is missing. |
| **Data Integrity (ALCOA+) SOP** | ❌ DR‑31 states no SOP exists. |
| **AI Explainability & Fairness Documentation** | ❌ DR‑32/33 confirm that AI explanation and fairness assessment documents are not present. |
| **Post‑Learning / Model Drift Governance** | ❌ DR‑35 notes the absence of a governance process. |
| **GMP suitability application draft (for manufacturing)** | Partial – DR‑02 shows the draft is missing. |
| **PCCP decision tree** | Partial – DR‑04 indicates it has not been finalized. |

*All items marked “✅” are considered fully covered per the source excerpts; items marked “❌” or “Partial” constitute gaps that must be remedied before submission.*

---

### 3. Core Risk Controls (to be documented)  

| Control | Regulatory anchor |
|--------|-------------------|
| **Risk Management File** – full ISO 14971‑based analysis, including risk acceptability criteria and residual risk evaluation. | ISO 14971 (2019 edition). |
| **Usability Engineering Plan & Evaluation** – IEC 62366‑1 (2020 amendment)–compliant activities for UI/UX of AI decision support. | IEC 62366‑1 (2020). |
| **Cybersecurity Controls** – implementation of SBOM, secure development lifecycle, and compliance with MFDS 보안지침 제16조. | MFDS 보안지침 제16조 (cited in source). |
| **Data Integrity Management** – ALCOA+ principles, SOP to ensure traceability and immutability of clinical and training data. | No specific identifier found in source — verify separately. |
| **AI Explainability & Fairness Framework** – documentation of model rationale, bias mitigation, and validation of explainability outputs. | No specific identifier found in source — verify separately. |
| **Post‑Learning Monitoring & Drift Governance** – periodic revalidation, trigger thresholds for drift, and SOP for model updates. | No specific identifier found in source — verify separately. |
| **GMP Compliance** – KGMP certification (or pre‑approval suitability assessment) for manufacturing of the software/firmware component. | No specific identifier found in source — verify separately. |
| **Labeling & IFU in Korean** – full Korean language labeling, package insert, and user manual complying with MFDS labeling requirements for digital devices. | No specific identifier found in source — verify separately. |

---

### 4. Missing Information / Gap Prioritisation  

| Priority (P) | Gap ID | Description | Immediate Action |
|--------------|--------|-------------|-----------------|
| **P0** | DR‑05 | Component performance evaluation SOP absent. | Develop and approve SOP; integrate into risk file. |
| **P0** | DR‑15 | Autonomous performance certification playbook missing. | Draft playbook, obtain internal review, align with MFDS autonomous device guidance (if any). |
| **P0** | DR‑35 | No post‑learning / drift governance process. | Establish governance framework; define monitoring metrics and escalation triggers. |
| **P1** | DR‑10 | Digital‑medical‑device labeling template not prepared. | Create Korean labeling template per MFDS 고시; include UDI, safety info, intended use. |
| **P1** | DR‑11 | Independent software suitability assessment procedure missing. | Define assessment workflow (verification/validation) and document. |
| **P1** | DR‑31 | Data integrity (ALCOA+) SOP absent. | Write SOP covering data capture, storage, audit trails. |
| **P1** | DR‑32/33 | AI explainability/fairness documentation missing. | Produce model explanation report and fairness assessment. |
| **P1** | DR‑06 | IEC 62366‑1 usability plan template not defined. | Develop usability engineering plan and associated templates. |
| **P1** | DR‑02 (partial) | GMP suitability application draft incomplete. | Finalize draft, submit for internal sign‑off before KGMP filing. |
| **P1** | DR‑04 (partial) | PCCP decision tree not finalized. | Complete decision tree, align with risk management outcomes. |

*P0 items should be addressed before any submission dossier is assembled; P1 items must be resolved in parallel to avoid delays during the MFDS review.*

---

### 5. Human‑Escalation Triggers  

| Trigger | Reason | Who must be notified |
|---------|--------|-----------------------|
| **Any P0 gap remains unresolved 14 days before planned submission** | High impact on safety and compliance; MFDO may reject dossier outright. | Project Lead → RA Director → CEO (if timeline at risk). |
| **Identification of a new regulatory notice that modifies MFDS 보안지침 제16조 or 디지털의료제품법 requirements** | Could introduce additional evidence obligations. | Regulatory Intelligence Lead → RA Team. |
| **Discovery during internal audit that any “partial” item (DR‑02, DR‑04) is actually non‑conforming** | Partial compliance may be treated as deficiency by MFDS. | Quality Management → GMP Compliance Officer. |
| **Regulatory authority feedback requiring supplemental AI explainability documentation** | Direct MFDS request overrides internal schedule. | RA Lead → Development Team (model owners). |
| **Failure to produce Korean labeling/IFU within the last 30 days before submission** | Legal requirement for market entry; missing label leads to non‑approval. | Labeling Specialist → Marketing & Regulatory Affairs. |

---

### 6. Citations  

| Reference type | Citation in draft |
|----------------|-------------------|
| **Framework references (no verify tag needed)** | ISO 14971 (2019 edition); IEC 62304 (2006+A1:2015); IEC 62366‑1 (2020 amendment). |
| **Instance identifier appearing in source** | MFDS 보안지침 제16조 – cited via DR‑09. |
| **Instance identifier not supplied in source** | “no specific identifier found in source — verify separately” is noted for data‑integrity SOP, AI explainability documentation, Korean labeling template, KGMP applicability, etc. |

---

### 7. Peer‑Review Prompt  

> *Please review the assumptions made about the likely device grade (3등급 or 4등급) and the consequent 허가 submission route. Verify whether any of the listed gaps might be re‑prioritised based on recent MFDS guidance (e.g., updated AI/ML guidance or revised security notice). Also assess if any additional evidence—such as a clinical evaluation report required under 디지털의료제품법 for autonomous functions—is missing from the current gap list.*  

---

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
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

DR-06 '부분'을 '공백(❌)'으로 오분류 — 원장 상태 왜곡(경미). shadow 하향 수용.

**Source Excerpts**

1. Chunk `1091162552456558927`

> ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버

2. Chunk `434223568197517474`

> ### 3.2 불일치·공백 항목 | Req-ID | 불일치 유형 | 내용 | 우선도 | |---|---|---|---| | DR-05 | 공백 | 구성요소 성능평가 SOP 부재 | P0 | | DR-10 | 공백 | 디지털의료기기 표시기재 템플릿 미작성 | P1 | | DR-11 | 공백 | 독립형 SW 사용적합성 평가 절차 부재 | P1 | | DR-15 | 공백 | 자율성능인증 신청 플레이북 부재 | P0 | | DR-31 | 공백 | 데이터 무결성(ALCOA+) SOP 부재 | P1 | | DR-32/33 | 공백 | AI 설명성·공정성 평가 문서 없음 | P1 | | DR-35 | 공백 | 사후학습·드리프트 거버넌스 없음 | P0 | | DR-02 | 부분 | GMP 적합판정 신청서 초안 미작성 | P1 | | DR-04 | 부분 | PCCP 결정트리 미확정 | P1 | | DR-06 | 부분 | IEC 62366-1 사용적합성 계획서 템플릿 미정 | P1 |
