# KB Eval Checksheet - 2026-10-29 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261029-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "81344a4f9f7d3e1b", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "757e3b0039fbc8900d0917e9ebdd32c0ded796618813c51039ed63b34e627e31"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `81344a4f9f7d3e1b`
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

> **Regulatory Assessment – QMSR (21 CFR Part 820) Compliance Draft**

---

### 1. Classification & Submission Route  
* **Current status:** The source material provides only QMS‑related information; it does not disclose the device’s intended use, technology, or predicate.  
* **Judgment:** *Classification cannot be determined from the available excerpts.* A classification determination (e.g., Class II §892.2050) is required before selecting a 510(k), De Novo, or other pathway.  

**Escalation trigger – Classification Gap** → *RA/CM must obtain the device description and intended use to perform a proper class‑determination analysis.*

---

### 2. Required Evidence for QMSR (21 CFR Part 820) Readiness  

| Requirement | Evidence Needed | Source citation |
|-------------|-----------------|-----------------|
| **Record‑management basic requirement** – ISO 13485 §4.2.5 (records control) | • Documented SOP that defines creation, review, approval, storage, retrieval and disposition of records.<br>• Training logs confirming staff awareness. | “ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**” – Excerpt [1] |
| **Additional QMSR record‑management requirements** – 21 CFR 820.35(a‑d) | • SOP‑DOC‑001 (updated to reference §§ 820.35(a‑d)).<br>• Evidence that each clause is addressed: <br>&nbsp;• (a) Document control & change management.<br>&nbsp;• (b) Service/maintenance records (6 items).<br>&nbsp;• (c) UDI record‑keeping.<br>&nbsp;• (d) Retention periods, backup, and security. | “§820.35(a)(b)(c)(d) 추가요건” – Excerpt [1]; SOP updates listed in Excerpt [2] |
| **Electronic records & signatures** – 21 CFR Part 11 (separate from §820.35) | • SOP‑DOC‑001 indicating that Part 11 is treated as a distinct clause.<br>• Validation reports for electronic systems, audit trails, and access controls. | “Part 11은 §820.35 외부로 별도 절 분리” – Excerpt [2] |
| **UDI implementation** – 21 CFR §§ 820.35(c) & Part 830 (GUDID) | • SOP‑TRC‑001 / SOP‑UDI‑001 containing UDI generation, labeling, and submission procedures.<br>• Records of GUDID submissions/updates. | “§820.35(c) + 21 CFR Part 830” – Excerpt [2] |
| **Service & maintenance documentation** – 21 CFR §820.35(b) (6‑item service record) | • SOP‑SVC‑001 (new/updated) with the six required fields for X‑ray field service.<br>• Completed service forms for each performed maintenance event. | “§820.35(b) 6항목 서비스 기록 양식 도입” – Excerpt [2] |
| **Complaint handling & MDR decision tree** – 21 CFR §§ 803.50, 803.53 | • SOP‑PMS‑001 with the MDR (Medical Device Reporting) decision tree referencing the cited sections.<br>• Completed complaint forms showing trigger assessment and reporting flow. | “§803.50 30cd / §803.53 5wd 트리거 기준” – Excerpt [2] |
| **Audit & external review evidence** – Objective documentation per ISO 13485 §4.2.5 | • SOP‑IA‑001 including the new “objective evidence for external inspection” clause.<br>• Internal audit reports and corrective‑action records demonstrating compliance. | “외부 열람 대비 객관적 증거 인용” – Excerpt [2] |

---

### 3. Identified Missing Information / Gaps  

| Gap | Impact on QMSR compliance |
|-----|---------------------------|
| **Device classification & intended use** not provided → cannot confirm the correct FDA submission pathway (510(k), De Novo, etc.). |
| **No traceable evidence that SOP‑DOC‑001 has been fully revised and approved** to incorporate §§ 820.35(a‑d). |
| **UDI lifecycle records absent** – no proof of GUDID entry or maintenance. |
| **Service record samples not supplied** – cannot verify the six required data elements. |
| **Complaint handling logs missing** – MDR decision tree usage not demonstrated. |
| **Part 11 system validation artifacts not referenced** – risk to electronic‑record integrity. |
| **Training records for all new/updated SOPs** are not cited. |

**Escalation trigger – Evidence Gap** → *RA must request the above documentation from QA/Engineering before a QMSR audit can be considered complete.*

---

### 4. Risk Controls (Design‑Control Perspective)  

| Control Area | Reasoning | Reference |
|--------------|-----------|-----------|
| **Record integrity & confidentiality** – enforce Part 11 controls (access, audit trail, electronic signatures). | Prevents unauthorized alteration of design history and device master records. | Excerpt [2] (Part 11 separation) |
| **UDI traceability** – maintain forward/ backward linkage between label, packaging, and device master record. | Enables rapid recall or field correction under 21 CFR 806. | §§ 820.35(c), Part 830 |
| **Service safety** – capture complete maintenance data (6 items) for each X‑ray service event. | Supports post‑market surveillance and minimizes equipment failure risk. | §820.35(b) |
| **Complaint triage & MDR decision tree** – systematic determination of reportability. | Ensures timely FDA reporting and compliance with §§ 803.50/803.53. | Excerpt [2] |
| **Document control (change management)** – address §820.35(a) requirements for controlled revisions, versioning, and distribution lists. | Reduces risk of obsolete procedures being used in the field. | Excerpt [1] |
| **External audit evidence** – maintain objective proof of compliance ready for FDA inspection. | Demonstrates adherence to ISO 13485 §4.2.5 and 21 CFR 820 overall. | Excerpt [2] |

---

### 5. Regulatory Citations (as appearing in source)  

| Regulation / Standard | Section / Clause (exact as in source) |
|-----------------------|----------------------------------------|
| 21 CFR Part 820 – QMSR | §820.35(a)(b)(c)(d) |
| 21 CFR Part 11 – Electronic Records | mentioned as “Part 11” (separate clause) |
| 21 CFR Part 830 – UDI | referenced together with §820.35(c) |
| 21 CFR §§ 803.50, 803.53 – MDR decision tree | cited verbatim |
| ISO 13485:2016 – Records management | §4.2.5 (basic requirement) |

*No device‑specific clearance numbers or external decree identifiers were present in the excerpts; therefore none are listed.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required | Responsible Party |
|---------|-----------------|-------------------|
| **Absence of device classification** | Obtain intended use, technology description, and perform class determination (21 CFR 862 vs 892 as appropriate). | Product Development / RA Lead |
| **SOP‑DOC‑001 not fully updated for §§ 820.35(a‑d)** | Review, approve, and distribute revised SOP; capture change control record. | QA Manager |
| **No GUDID submission evidence** | Collect or generate UDI data package; submit to FDA’s GUDID and retain proof of submission. | Regulatory Affairs |
| **Service records lacking required 6 fields** | Conduct a sample audit of field‑service logs; remediate missing data. | Service Engineer / QA |
| **Complaint handling not aligned with MDR decision tree** | Perform gap analysis on complaint forms; re‑train staff on reporting thresholds. | RA & Quality |
| **Part 11 validation artifacts unavailable** | Execute or locate system validation, create a summary report, and file in QMS. | IT/Quality Systems |
| **Training records for new SOPs missing** | Schedule and document training; capture attendance signatures. | HR / QA |

Each trigger should be logged in the QMS deviation/NC database and escalated to senior management if not closed within 10 working days.

---

### 7. Peer‑Review Prompt  

*“Please review the assumptions above, especially the inference that §820.35(a‑d) are the only additional QMSR clauses needing SOP updates. Verify whether any other newly effective QMSR provisions (e.g., risk‑management integration per §820.30) apply to our device class, and assess if the current source coverage adequately captures all required evidence for a 510(k)–type submission.”*

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

>

**Source Excerpts**

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `130165779856845378`

> ### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영) | SOP | 갱신 내용 | 담당 | 판정 기준 | |-----|----------|------|----------| | SOP-DOC-001 | §3에 "미국 시장 적용 시 §820.35(a)(b)(c)(d) 추가요건" 절 신설, Part 11은 §820.35 외부로 별도 절 분리 | QA | 기록관리 절차에 불만/서비스/UDI/기밀성·Part 11 분리 기재 여부 | | SOP-PMS-001 | MDR 결정 트리(§803.50 30cd / §803.53 5wd 트리거 기준) + 미보고 사유 양식 첨부 | QA/RA | 불만 → MDR 판정 → 기록 흐름 완비 여부 | | SOP-TRC-001 / SOP-UDI-001 | UDI 기록관리 절 추가 — **§820.35(c)** + 21 CFR Part 830 | RA | GUDID 제출·갱신 기록 체계 구축 여부 | | SOP-SVC-001 (신설/갱신) | **§820.35(b)** 6항목 서비스 기록 양식 도입 | Service/QA | X-ray 출장정비 기록 6항목 완결성 | | SOP-IA-001 | 감사보고서 작성 기준에 "외부 열람 대비 객관적 증거 인용" 항목 추가 | QA | 보고서 품질 기준 갱신 여부 |

### kb-eval-20261029-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_us-002", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "a004f78fa0ea8810", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `a004f78fa0ea8810`
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

> **Regulatory Draft – GUI‑based Imaging Software (SaMD) – Design‑Control & QMSR Readiness**

---

### 1. Device Description & FDA Classification  
| Item | Detail |
|------|--------|
| **Product** | Stand‑alone graphical user‑interface software that controls image acquisition and basic processing in a radiology suite (SaMD). |
| **Intended Use** | “To provide the operator with real‑time view, control of exposure parameters, and immediate post‑acquisition review of X‑ray/CT images.” *(statement to be supplied by sponsor)* |
| **CFR Classification** | Class II – *Medical image management and processing system* → **21 CFR §892.2050** (Class II). |
| **Regulatory Pathway** | Traditional 510(k) demonstrating substantial equivalence to a cleared predicate (e.g., K123456 – “XYZ Imaging Workstation”, cleared under §892.2050). |

---

### 2. Submission‑Route & Core Evidence Required  

| Requirement | Evidence Needed | Source / Citation |
|-------------|----------------|-------------------|
| **Device Description & Predicate Comparison** | Detailed description, labeling draft, and side‑by‑side comparison with a predicate cleared under §892.2050. | Framework reference – 21 CFR §892.2050 (no specific identifier in source). |
| **Design Controls (21 CFR 820)** | • Design History File (DHF) with SOPs for design input, output, review, verification, validation.<br>• Software Development Plan (SDP), Software Requirements Spec (SRS), Software Architecture Doc (SAD), Verification Plan (SVP), Validation Report (SVR). | Mapping table in source [2] – “SW 개발 수명주기 … SDP·SRS·SAD·SVP·SVR 전 문서 필수”. |
| **Software Lifecycle & Safety Class** | IEC 62304 compliance, Safety Class C implementation, verification per §8.1. | Source [2] – “IEC 62304 §8.1” (software validation). |
| **Risk Management** | ISO 14971:2019 risk management file (risk analysis, evaluation, control measures, post‑market monitoring). | Framework reference – ISO 14971 (no specific identifier in source). |
| **Cybersecurity & Change Control** | • Threat model & SBOM.<br>• Predetermined Change Control Plan (PCCP) per FDA Final Guidance (Dec 2024).<br>• Alignment with MDR‑related guidance if marketed abroad. | Source [2] – “FDA 524B PCCP” and “PCCP(FDA)” entries. |
| **UDI Assignment** | Device identifier, production identifiers, label & packaging integration per 21 CFR §830.10 onward. | Framework reference – 21 CFR §830 (no specific source identifier). |
| **Complaint Handling & MDR Reporting** | Complaint handling SOP integrated with ARR; record of determination whether a complaint is reportable under 21 CFR §803. | Source [1] – “불만 파일 강화” → §820.35(a) and “MDR reporting(21 CFR 803)” in ARR row. |
| **Service Records** | SOP for service performance documentation; service reports per §820.35. | Source [1] – “서비스 기록” → §820.35. |
| **QMSR‑Specific Procedures (Effective Feb 2026)** | *ARR* compliance activities, internal audit accessibility, inclusion of contract sterilizers/relabelers where applicable. | Source [1] – ARR row (§820.10(b)), Internal audit row (§820 전반), Contract sterilizer row (§820.10(a)). |
| **QMS Documentation** | Updated Quality Manual, SOPs reflecting QMSR expansion (ARR, internal audit openness, external party scope). | Source [1] – multiple rows referencing §820 sections. |

---

### 3. Gaps / Missing Information  

| Gap | Why it matters |
|-----|----------------|
| **Explicit Intended Use Statement** | Required for predicates and labeling; not present in source. |
| **Predicate Device Number(s)** | Needed to build substantial‑equivalence argument (no identifier supplied). |
| **Labeling Mock‑up (including UDI)** | FDA review of label/IFU is mandatory; absent from current data. |
| **Complete Risk Management File** | Only references to ISO 14971; actual risk analysis, mitigations, and residual risk evaluation must be provided. |
| **PCCP Documentation (if AI/ML present)** | Source notes PCCP relevance but no concrete plan submitted. |
| **Post‑Market Surveillance Plan** – MDR‑reportable complaint decision flow & 30‑day reporting process. | Required under ARR and §820.35(a); details missing. |
| **Contract Sterilizer/Re‑labeler Agreements** (if any) | QMSR scope now includes these parties (§820.10(a)) – evidence of qualified agreements not shown. |
| **Software Validation Report (SVR) with statistical data** | Needed to demonstrate that verification/validation meet IEC 62304 Class C criteria; not in source excerpt. |

---

### 4. Key Risk Controls (Design‑Control Perspective)

1. **Hazard Identification & Mitigation** – per ISO 14971, documented in risk management file.  
2. **Software Safety Measures** – IEC 62304 Class C controls: fail‑safe modes, error handling, watchdog timers.  
3. **Cybersecurity Controls** – Threat model, SBOM, encryption, authentication; governed by FDA PCCP.  
4. **Usability & Human Factors** – Validation of GUI to prevent user errors (e.g., incorrect exposure settings).  
5. **Complaint‑Driven Risk Re‑assessment** – Integration of complaint analysis with risk file per ARR and §820.35(a).  

---

### 5. QMSR Compliance Checklist (per source [1])

| QMSR Element | Required Action |
|--------------|-----------------|
| **ARR integration** | Incorporate UDI, MDR reporting (21 CFR §803), Corrections & Removals (21 CFR §806) into all QMS procedures. |
| **Complaint File Enhancement** | Record determination of reportability for each complaint; align with §820.35(a). |
| **Service Record Documentation** | Capture service performance data per §820.35. |
| **Internal Audit Transparency** | Ensure audit reports are available to FDA investigators (removal of “non‑disclosure” exemption). |
| **External Party Scope Expansion** | Include contract sterilizers/relabelers in QMSR scope; maintain supplier qualification records (§820.10(a)). |

---

### 6. Human‑Escalation Triggers  

| Situation | Escalation to Senior RA / Regulatory Lead |
|-----------|--------------------------------------------|
| No **predicate device number** identified within 5 business days of draft submission preparation. |
| ARR‑related activities (UDI, MDR reporting) not fully documented in QMS procedures. |
| Absence of a **PCCP** when AI/ML functionality is confirmed. |
| Incomplete or missing **risk management file** after design freeze. |
| Failure to produce a **labeling draft with UDI** before 510(k) submission packaging deadline. |
| Internal audit reveals non‑conformance in any QMSR‑required SOP (e.g., §820.35 complaint handling). |
| Contract sterilizer/relabeler agreements not evidencing qualification per §820.10(a). |

When any trigger occurs, the RA team should:  
1. Issue a **Risk/Issue Log** entry with impact assessment.  
2. Convene an **Regulatory Review Meeting** within 3 working days.  
3. Suspend further submission activities until corrective actions are documented and approved.

---

### 7. Peer‑Review Request  

> *Please review the assumptions above, especially:*  
> - The classification under §892.2050 (are there any functional nuances that could shift the device to a different FDA product code?).  
> - Completeness of the QMSR mapping – does the internal audit “non‑disclosure” exemption removal fully satisfy the source’s note on “FDA 실사관이 내부감사 보고서 열람 가능”?  
> - Whether any additional MDR‑related obligations (e.g., 30‑day reporting for software) need to be captured beyond what is cited.  

Your feedback will ensure jurisdictional gaps are closed before finalizing the 510(k) package.

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

>

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261029-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_us-003", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "7b1bf4115c8de42f", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md", "source_hash": "5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `7b1bf4115c8de42f`
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

### 1 Classification & Submission Route  

| Device element | Likely FDA class* | Recommended pathway |
|----------------|------------------|---------------------|
| AI/ML–driven software that performs a medical purpose (diagnostic, triage, or treatment recommendation) – no explicit hardware | **Class II** (non‑invasive SaMD) – most AI/ML diagnostic tools fall under 21 CFR 892.2050 (Medical image management and processing system) or the general “Software as a Medical Device” risk‑based classification guidance. | **510(k) Premarket Notification** (substantive equivalence to a predicate device). If no suitable predicate exists, consider **De Novo** (Class II) after completing an FDA‐accepted risk analysis and validation package. |

\*Classification is inferred from the “AI/ML 기기” description in the source; the exact indication for use must be supplied before a final class can be locked‑in.

---

### 2 Required Evidence Package  

| Evidence | Regulatory basis (framework citation) | Typical content |
|----------|----------------------------------------|-----------------|
| **Device Description & Indications for Use** | 21 CFR 807.92 – contents of a 510(k) | Clear statement of the medical purpose, patient population, and clinical context. |
| **Design History File (DHF)** | 21 CFR 820.30(a) – design control record | All design inputs, outputs, verification, validation, risk management files, change records, and traceability matrices. |
| **Risk Management** | ISO 14971:2019 (harmonized) & 21 CFR 820.30(e) | Hazard identification, risk analysis, mitigation, residual‑risk evaluation; AI/ML specific hazards (e.g., model drift). |
| **Software Development & Validation** | IEC 62304:2006+A1:2015 (state‑of‑the‑art) & 21 CFR 820.30(c) | Software development plan, architecture, coding standards, unit/integration testing, verification of each software requirement. |
| **Usability Engineering** | IEC 62366‑1:2015+A1:2020 (state‑of‑the‑art) | Human factors analysis, formative/usability validation studies, labeling usability. |
| **Cybersecurity & AI/ML Change Control** | FDA “Predetermined Change Control Plan (PCCP)” guidance (Dec 2024) | Pre‑specified change categories, monitoring plan, post‑market performance data collection. |
| **Biocompatibility (if device contacts patient)** | ISO 10993‑1:2018 (harmonized) | Cytotoxicity, sensitization, irritation, and any applicable animal or clinical data. |
| **Performance Testing / Clinical Evidence** | 21 CFR 820.30(b); FDA guidance on SaMD validation | Bench testing, analytical performance, clinical simulation, or clinical study results demonstrating safety/effectiveness for the stated indication. |
| **Labeling & IFU** | 21 CFR 801 – labeling requirements; 21 CFR 830 – UDI labeling | Product label, instructions for use, symbols per ISO 15223‑1:2021, and a fully populated UDI on the device label/ packaging. |
| **UDI Master Record & Distribution** | 21 CFR 820.35(b) (Device Master Record) + 21 CFR 830 – UDI system | SOP for maintaining a unified UDI Data Record (UDR), GUDID submission, and traceability to each device batch/lot. |
| **Quality Management System (QMS)** | 21 CFR 820 (effective Feb 2026) – QMSR, ISO 13485:2016 (harmonized) | Full QMS documentation, internal audit reports, corrective‑and‑preventive actions (CAPA), management review minutes. |

> **Note:** All cited standards are listed as *framework references*; they require no separate verification tag.

---

### 3 Missing / Incomplete Information (Gap Summary)

| Gap identified in source | Required action |
|--------------------------|-----------------|
| No SOP template for **MDR decision‑document** (EU specific) – not required by FDA but the underlying decision logic should be captured in a *Design Decision Record* within the DHF. | Create “Design Decision Record” SOP; map to 21 CFR 820.30(a). |
| **UDI master record fragmentation** – source mentions an SOP draft referencing §820.35(b) + 21 CFR 830 + EU MDR Art.27. | Finalize a consolidated UDI Data Record (UDR) SOP that satisfies 21 CFR 820.35(b) and Part 830 labeling/ GUDID requirements; EU reference can be omitted for US submissions. |
| **Internal audit report narrative level** – “objective evidence required” not yet standardized. | Adopt a template that links audit findings to specific CFR/QMS clauses (e.g., non‑conformance → 820.100 CAPA). |
| **Electronic signature scope ambiguous** – Part 11 applicability undefined. | Issue SOP‑QM‑IT‑001 defining the scope of FDA 21 CFR Part 11 for electronic signatures on design documents, batch records, and DHF entries. |
| **AI/ML change‑control framework absent** – source notes no OJEU/MDCG listing. | Develop a Predetermined Change Control Plan (PCCP) per the Dec 2024 FDA guidance; include categories of allowable changes without additional 510(k). |
| **Intended use / indication for use not provided** – essential for classification and predicate identification. | Draft a concise “Indications for Use” statement supported by clinical/benchmark data. |
| **Predicate device (if pursuing 510(k)) not identified** – required to establish substantial equivalence. | Conduct a market search; select a cleared device with the same intended purpose, technology, and performance characteristics; include comparison matrix in the submission. |

*No specific instance identifiers (e.g., clearance numbers, docket IDs) appear in the source excerpts – verify separately.*

---

### 4 Key Risk Controls & Documentation

| Control | Source / Standard | Implementation evidence |
|--------|-------------------|--------------------------|
| **Hazard analysis & risk mitigation** | ISO 14971:2019 (harmonized) | Risk Management File with FMEA/FMECA, residual‑risk acceptability justification. |
| **Software safety classification & verification** | IEC 62304:2006+A1:2015 | Software Development Plan, unit/integration test reports, code review logs. |
| **Usability validation** | IEC 62366‑1:2015+A1:2020 | Human factors engineering report; formative and summative usability study data. |
| **Predetermined Change Control Plan (PCCP)** | FDA PCCP guidance Dec 2024 | Documented change categories, monitoring plan, post‑market performance metrics. |
| **UDI labeling compliance** | 21 CFR 830 & §820.35(b) | Completed UDI label artwork, GUDID upload confirmation, SOP for UDR maintenance. |
| **CAPA effectiveness verification** | 21 CFR 820.100(a) | CAPA records with root‑cause analysis and follow‑up verification results. |

---

### 5 Human‑Escalation Triggers  

| Trigger condition | Action & Responsible role |
|-------------------|----------------------------|
| **Absence of a finalized Indications for Use** (or ambiguous language). | Pause submission preparation; RA lead to request clinical/marketing team clarification – *escalate to Project Manager*. |
| **No identified predicate device for 510(k)** after market search. | Initiate De Novo feasibility review – *escalate to Regulatory Strategy Lead*. |
| **UDI Data Record SOP not approved** (draft only). | Hold 510(k) assembly; Quality Engineer must obtain QMS manager sign‑off – *escalate to QA Director*. |
| **PCCP undefined for AI/ML model updates**. | Risk Management team must draft PCCP before any software release – *escalate to Head of Software Engineering*. |
| **Electronic Signature scope still “ambiguous”** after SOP‑QM‑IT‑001 draft. | Conduct Part 11 compliance audit; if unresolved, halt DHF entries that rely on e‑signatures – *escalate to Compliance Officer*. |
| **Internal audit findings > 2 non‑conformities in QMSR**. | Initiate CAPA; senior QA must review before submission packaging – *escalate to VP of Quality*. |

When any trigger is met, the regulatory team should log the issue in the project risk register and notify the designated escalation point promptly.

---

### 6 Conclusion & Next Steps  

1. **Finalize core submission artifacts** (Indications for Use, DHF, Risk Management File, PCCP, UDI SOP).  
2. **Select/confirm predicate device** or prepare De Novo justification.  
3. **Close identified gaps** per the table above; obtain cross‑functional sign‑offs.  
4. **Assemble 510(k) package** (or De Novo request) and submit to FDA with all required evidence.  

---

### Peer Review Prompt  

> *Colleague, please review the assumptions made about device classification, the completeness of the evidence matrix, and any jurisdictional gaps (e.g., EU‑specific MDR references that were omitted). Highlight any missing regulatory citations or alternative pathways you consider appropriate.*

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

>

**Source Excerpts**

1. Chunk `1061533089543682126`

> ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적용 | | AI/ML 기기 | OJEU/MDCG 단독 등재 없음 → EU AI Act 병행 필요(후속 과제) | | 운영 영향 | 체크리스트에 H/S 컬럼 신설, 개정판 번호(A11, A1, A2) 기재 의무화 |

2. Chunk `1066441905930561439`

> ### Gap → 조치 | Gap | 조치 | |-----|------| | 국내 SOP에 MDR 결정문서 양식 부재 | 양식 ML-MDR-001 초안(보고/미보고 결정트리) 신설 | | UDI 마스터 레코드 단편화 | UDR(UDI Data Record) 통합 관리 SOP 초안 (§820.35(b) + 21 CFR 830 + EU MDR Art.27) | | 내부감사 보고서 서술 수준 | "외부감사 대응 수준" 템플릿 개정 (객관적 증거 필수 인용) | | 전자서명 범위 모호 | Part 11 적용범위 정의 문서(QM-IT-001) 초안 예정 |

### kb-eval-20261029-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "QSR"], "profile_id": "ra-us", "scenario_id": "b02c59dedb079e1c", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/QSR_21CFR820/README.md", "source_hash": "5250406488094d588d38eb1e45c2d8d4b90f093334322d2ded3d50d3a2e72871"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `b02c59dedb079e1c`
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

> **Regulatory Draft – Diagnostic X‑Ray Imaging System  
Focus: 2026 QMSR (21 CFR 820) and Design‑Control Readiness**

---

### 1. Classification & Submission Route  

| Item | Determination |
|------|----------------|
| **Device class** | Likely **Class II** under **21 CFR Part 892 – Radiology / Imaging Devices** (diagnostic X‑ray system). The exact sub‑section (e.g., §892.2000 series) must be verified against the FDA product code list. |
| **Premarket pathway** | **510(k) – Traditional Premarket Notification** (substantial equivalence to a cleared predicate X‑ray system). If no suitable predicate exists, consider a **De Novo Classification Request**. |
| **Regulatory citations** | • 21 CFR Part 820 – Quality Management System Regulation (QMSR) – effective 2 Feb 2026 (aligned with ISO 13485:2016). <br>• 21 CFR Parts 1020.30–1020.32 – Performance Standards for Diagnostic X‑ray Systems.<br>• 21 CFR Part 1002 – Records & Reports for Radiation‑Emitting Products.<br>• 21 CFR Part 1040 – Light‑Emitting Product standards (relevant only if device incorporates such components). |

---

### 2. Required Evidence Package  

| Category | Specific Deliverables |
|----------|----------------------|
| **Device Description & Intended Use** | Full narrative, indications, user environment, patient population. |
| **Design History File (DHF)** | All design‑control records per QMSR: design inputs, outputs, verification, validation, risk management files, change‑control plan (if AI/ML components – Predetermined Change Control Plan). |
| **Risk Management** | ISO 14971:2019 risk analysis & evaluation; identified radiation hazards; mitigations (shielding, interlocks, dose‑monitoring). |
| **Performance Testing (Radiation)** | • Conformance to 21 CFR 1020.30–1020.32 (output, beam quality, exposure reproducibility). <br>• Acceptance testing report and statistical analysis of repeatability. |
| **Electrical Safety & EMC** | IEC 60601‑1:2005+A1:2012+A2:2020 compliance data (if applicable). |
| **Software/ Firmware (if any)** | IEC 62304:2006+A1:2015 life‑cycle documentation; verification and validation results. |
| **Labeling & IFU** | Draft labeling meeting 21 CFR Part 801; includes UDI per 21 CFR Part 830. |
| **Sterilization / Biocompatibility (if applicable)** | ISO 10993‑1:2018 test reports for any patient‑contacting components. |
| **Predicate Comparison** | Table of similarities/differences to selected cleared X‑ray system(s) (e.g., 510(k) KXXXXX). |
| **Regulatory Submissions** | Completed 510(k) covering all sections above; electronic Common Technical Document (eCTD) format. |

*All documents must be signed and dated per QMSR requirements.*

---

### 3. Missing Information – “Gap” Checklist  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact FDA product code / classification sub‑section** | Determines whether Class II or III & required controls. | Verify against the FDA Product Classification Database; if ambiguous, request clarification (FDA‑RTA). |
| **Predicate device identification** | Needed for 510(k) substantial equivalence claim. | Perform market search; select a cleared X‑ray system with matching intended use and technology. |
| **Complete DHF entries for design inputs/outputs** | QMSR demands traceability from user needs to final product. | Populate missing design input specifications (e.g., dose limits, image quality metrics). |
| **Radiation performance data** | Must satisfy 21 CFR 1020.30‑32 standards. | Conduct bench testing; compile test reports. |
| **UDI strategy** | Required under 21 CFR Part 830 for all Class II devices. | Define issuing agency, label format, and submit to GUDID. |
| **Predetermined Change Control Plan (PCCP)** *if AI/ML* | FDA guidance (Dec 2024) mandates a PCCP for post‑market changes. | Draft PCCP outlining anticipated algorithm updates. |
| **Clinical evidence** (if claimed performance exceeds predicate) | May be required to support safety/effectiveness. | Plan and execute a limited clinical study or use existing literature. |

---

### 4. Core Risk Controls (derived from ISO 14971 & radiation standards)

1. **Shielding & Collimation** – Physical barriers meeting 1020.30 dose‑distribution limits.
2. **Interlock System** – Prevents X‑ray generation when protective shields are open; verified per IEC 60601‑1 safety requirements.
3. **Dosimetry Alarms** – Real‑time monitoring; automatic shutdown if dose exceeds preset threshold.
4. **Fail‑Safe Power Supply** – Redundant power cutoff to avoid unintended emission.
5. **User Training & Access Controls** – Role‑based authentication for operation; documented in training records (QMSR §820.25).
6. **Software Validation** – Verify that image processing does not alter diagnostic information; adhere to IEC 62366‑1 usability engineering.

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger Threshold | Escalation Path |
|-----------|-------------------|-----------------|
| **Unresolved classification ambiguity** | No FDA product code identified after database search. | Notify senior Regulatory Affairs Manager; consider filing a Refuse‑to‑Accept (RTA) checklist inquiry with FDA. |
| **Missing predicate device** | No cleared X‑ray system matches intended use/technology. | Escalate to leadership for De Novo strategy decision. |
| **Failure to meet 1020.30‑32 performance criteria** | Test results outside acceptable limits. | Halt submission; convene cross‑functional engineering review and risk reassessment before resubmission. |
| **Incomplete DHF (design‑control gaps)** | Any required element absent per QMSR §820.30. | Issue internal non‑conformance; require corrective action plan from design team before 510(k) compilation. |
| **UDI label non‑compliance** | Label missing required UDI fields or GUDID entry rejected. | Immediate remedial redesign of labeling; involve Quality Assurance lead for FDA liaison. |
| **Regulatory deadline missed (e.g., QMSR effective date)** | Submission planned after 2 Feb 2026 without compliant QMSR. | Escalate to Compliance Officer for interim corrective measures or defer market launch. |

---

### 6. Bottom‑Line Regulatory Judgment  

- The device is a **Class II diagnostic X‑ray system** requiring a **traditional 510(k)** submission, provided an appropriate predicate exists.
- **All QMSR (21 CFR 820) design‑control artifacts must be complete and aligned with ISO 13485:2016** before filing.
- **Radiation performance evidence per 21 CFR 1020.30–1020.32 is a non‑negotiable prerequisite**; without it the submission cannot proceed.
- Any identified gaps (classification, predicate, DHF completeness, UDI strategy) must be resolved or formally escalated as outlined above before the 510(k) dossier can be finalized.

---

### 7. Peer Review Prompt  

> **To: Regulatory Affairs Team – Peer Reviewer**  
> Please challenge the assumptions made in this draft regarding (1) the classification under Part 892, (2) the adequacy of the identified predicate search approach, and (3) any jurisdiction‑specific gaps (e.g., UDI issuance, radiation‑record reporting per Part 1002). Highlight missing source evidence or alternative regulatory pathways that may apply.

---

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

> 진단용 X-ray 시스템 분류 예시로 "§892.2000 series" 제시 — 892.2000번대는 영상관리/PACS 계열이며 진단 X-ray 시스템은 §892.1650 계열. 예시 포인터 오안내 ("verify" 헤지는 있으나 예시 자체가 잘못된 방향).

**Source Excerpts**

1. Chunk `136831192110451403`

> ## 추가 규제 (X-ray 관련) - **21 CFR Part 1020.30 ~ 1020.32**: Radiation Control – Performance Standards for Diagnostic X-ray Systems - **21 CFR Part 1002**: Records and Reports (Radiation-Emitting Products) - **21 CFR Part 1040**: Performance Standards for Light-Emitting Products (관련 시)

2. Chunk `18877965943708175`

> ## 현황 - 기존 QSR(21 CFR 820)은 2024년 공표된 Quality Management System Regulation (QMSR)으로 개정됨. - **시행일: 2026년 2월 2일** → ISO 13485:2016과 정합화.

### kb-eval-20261029-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "1e88067737fd137d", "source": "github:holee9/MD-process/03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md", "source_hash": "8ae673fb6f1587e4dc2d26f9f4b3680719f501c71d0ce6d5450609814a7d126e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `1e88067737fd137d`
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

> **Regulatory Draft – QMSR Compliance and 510(k) Submission Readiness**

---

### 1. Bottom‑Line Assessment  
- **Current status:** The SOP for SBOM generation (SOP‑SBOM‑001) aligns with the FDA Quality Management System Regulation (QMSR, effective 02 Feb 2026) and ISO 13485:2016 record‑management requirement (§4.2.5).  
- **Next regulatory step:** Determine the device’s classification and intended use to select the appropriate pre‑market pathway (most likely a 510(k) for a Class II medical device; De Novo only if no predicate exists).  

---

### 2. Classification & Submission Route (to be confirmed)

| Item | Current Evidence | Action Required |
|------|------------------|-----------------|
| **Device type / intended use** | Not provided in source excerpt. | Obtain product description, indications, and user environment. |
| **Regulatory panel** | Unclear – could fall under imaging (§892), clinical chemistry (§862), or general medical device (§820). | Map the device function to the correct 21 CFR part; confirm with senior RA. |
| **Likely classification** | Assuming a software‑enabled, non‑invasive device → Class II (most 510(k)‑eligible). | Verify against FDA product codes and classification database. |
| **Submission route** | Pending classification. | If Class II → prepare 510(k); if novel with no predicate → consider De Novo. |

*If the device is a software medical image management system, the applicable regulation would be **21 CFR Part 892 §892.2050 (Class II)**; otherwise use the panel identified in the classification step.*

---

### 3. Evidence Required for QMSR‑Compliant 510(k)  

| Requirement | Expected Artefact | Source Basis |
|-------------|-------------------|--------------|
| **SBOM with VEX & VDR** (including build ID ↔ SBOM ↔ VEX linkage) | Exportable SBOM file, Vulnerability Exploitability eXchange (VEX) report, Vendor‑Declared Remediation (VDR) document; electronic signature. | SOP‑SBOM‑001 steps 5.8.1–5.8.3; QMSR §820.35 / ISO 13485 §4.2.5 |
| **Cybersecurity File** (stand‑alone section in the MDF) | Consolidated “Cybersecurity File” containing SBOM, VEX, VDR, patch timelines, and audit records. | Step 5.8.1 & 5.8.4 |
| **Traceability Matrix** linking each software component to design controls, risk controls, and verification activities | Cross‑referencing matrix (Component ↔ Design Input ↔ Risk Control ↔ Verification). | Implied by “SBOM 변경 이력의 추적성 확보 — 빌드 ID↔SBOM↔VEX 삼중 연결” |
| **Electronic Signature** confirming SBOM integrity at submission time | Signed PDF or secure repository entry (e.g., FDA‑approved e‑signature system). | Step 5.8.3 (“전자 서명 포함”) |
| **Quarterly Self‑Audit Report** on QMSR compliance | Audit checklist, findings, corrective actions; signed by Security Officer. | Step 5.8.4 (“분기 자체감사 완료”) |
| **Risk Management File** (ISO 14971:2019) | Hazard analysis, risk control measures, post‑market surveillance plan. | Required for any 510(k); not present in excerpt – gap. |
| **Design History File (DHF)** | Design inputs/outputs, verification & validation reports, software development lifecycle documentation (IEC 62304). | Standard 510(k) requirement – gap. |

---

### 4. Missing Information / Gaps  

| Gap | Why Critical | Suggested Action |
|-----|--------------|------------------|
| **Device classification & predicate** | Determines submission type and required FDA guidance references. | Conduct product‑code lookup; engage senior RA for classification decision. |
| **Labeling & Instructions for Use (IFU)** | Required under 21 CFR §801 for clearance. | Draft labeling aligned to device claim; map to SBOM disclosures if needed. |
| **Risk Management (ISO 14971) documentation** | Demonstrates safety of software components and mitigation of identified vulnerabilities. | Compile FMEA/FMECA, residual risk justification. |
| **Software Development Lifecycle evidence (IEC 62304)** | Needed for any software‑based device to show controlled development. | Produce plan, unit/integration/verification test reports. |
| **UUDI & GUDID entry** | Mandatory under 21 CFR §830 for marketable devices. | Allocate Device Identifier; register in FDA GUDID. |
| **Post‑market Surveillance (PMS) Plan** | Required for 510(k) submissions of software with cybersecurity impact. | Outline monitoring, vulnerability response timeline, and reporting process. |
| **Evidence that SBOM can be presented within the 2‑hour window** | FDA inspection checkpoint; failure could trigger refusal to accept. | Conduct mock audit; document retrieval workflow and electronic signature log. |

---

### 5. Risk Controls (mapping to ISO 14971 & QMSR)

| Hazard / Vulnerability | Control Mechanism | Verification |
|------------------------|-------------------|--------------|
| **Component‑level vulnerabilities** (identified via VEX) | Regular SBOM updates, patch management, and documented remediation (VDR). | Quarterly self‑audit; automated vulnerability scanner feed into SBOM. |
| **Loss of traceability between build ID & SBOM** | Mandatory 1:1:1 mapping captured in the Cybersecurity File. | Audit check – “SBOM 변경 이력의 추적성 확보”. |
| **Unauthorised modification of SBOM** | Role‑based access control, electronic signatures, change‑control logs (PCCP). | Review of audit trails; penetration testing of file repository. |
| **Delayed response to critical CVEs** | Pre‑determined Change Control Plan (PCCP) with defined timelines (<48 h for critical). | Record of time stamps from CVE receipt to patch deployment. |
| **Regulatory non‑compliance during FDA inspection** | Internal QMSR audit schedule; readiness checklist aligned to §820.35. | Mock inspection results documentation. |

---

### 6. Key Citations  

| Citation Type | Reference |
|---------------|-----------|
| **Framework (CFR / ISO)** | 21 CFR §820.35 (QMSR record‑keeping) – aligns with FDA QMSR effective 02 Feb 2026. |
| **Framework** | ISO 13485:2016 §4.2.5 – Record Management requirements. |
| **Framework** | ISO 14971:2019 – Risk Management for medical devices. |
| **Framework** | IEC 62304 (2006+A1:2015) – Software life‑cycle processes (implicit requirement). |
| **Source excerpt** | SOP‑SBOM‑001, Section 5.8 “QMSR 실사 대응 — SBOM 기록 요구사항” – outlines activities 5.8.1–5.8.4 and the 2‑hour submission checkpoint. (no specific CFR/section identifier supplied in source). |
| **Source excerpt** | Table of vulnerability tracking (Chunk 1031175965966205535) – shows CVE, CVSS, VEX decision fields; confirms need for “Fix / Investigation” status tracking. |

*No instance‑specific identifiers (e.g., 510(k) numbers) appear in the provided excerpts — “no specific identifier found in source — verify separately.”*

---

### 7. Human‑Escalation Triggers  

| Trigger | Condition | Escalation Path |
|--------|-----------|-----------------|
| **Classification uncertainty** | Device type or intended use cannot be mapped to a CFR panel within 5 business days of this draft. | RA Lead → Senior Regulatory Manager (decision on 510(k) vs De Novo). |
| **SBOM retrieval time >2 h** | Mock inspection shows >2 h delay to produce SBOM with electronic signature. | QA Manager → Immediate corrective action; report to Security Officer and Regulatory Affairs Director. |
| **Critical/high CVE not mitigated within 48 h** | VEX status remains “Affected” without remediation plan after 48 h. | Security Officer → Initiate PCCP; notify FDA via voluntary notification under 21 CFR §806 if required. |
| **Quarterly self‑audit finds non‑conformance** | Any finding rated “major” or “critical”. | QA Manager → CAPA initiation; inform RA Lead for impact on submission timetable. |
| **Missing risk‑management documentation** | Absence of ISO 14971 file at the time of 510(k) compilation. | RA Lead → Pause submission preparation; engage Risk Management Team. |
| **UDI/ GUDID registration gap** | Device slated for market launch without a registered UDI. | Regulatory Affairs Director → Trigger urgent coordination with FDA‑GUDID team. |

---

### 8. Peer Review Prompt  

> *Please review the assumptions made above, especially the inferred Class II status and the mapping to 21 CFR Part 892 §892.2050. Verify that all required QMSR artifacts (SBOM, VEX, VDR, Cybersecurity File) are captured in the current SOP scope, and flag any jurisdiction‑specific gaps (e.g., missing IEC 62304 evidence or UDI registration). Also assess whether the 2‑hour SBOM submission checkpoint aligns with FDA inspection expectations under QMSR §820.35.*

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

>

**Source Excerpts**

1. Chunk `1031175965966205535`

> ┌──┬──────────┬────────┬──────┬────────────┬──────┬──────┐ │# │구성요소 │CVE ID │CVSS │VEX 판정 │사유 │조치 │ │ │(PURL) │ │Score │ │ │기한 │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │1 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │2 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ └──┴──────────┴────────┴──────┴────────────┴──────┴──────┘ (N/A=not_affected, Aff=affected, Fix=fixed, Inv=under_investigation) 총 취약점: __건 Critical: __ High: __ Medium: __ Low: __ 변경관리 진입 건수: __건 (SOP-CC-001) 승인: Security Officer ___________ 일자: ____-__-__ ```

2. Chunk `1070786144928344628`

> ### 5.8 QMSR 실사 대응 — SBOM 기록 요구사항 (v0.3 신설) FDA QMSR(2026-02-02 시행)에 따라 SBOM 관련 기록은 ISO 13485:2016 §4.2.5 기록 관리 요구사항을 준수해야 한다. | 단계 | 수행자 | 활동 | 판정 기준 | |------|--------|------|-----------| | 5.8.1 | QA Manager | SBOM·VEX·VDR을 MDF 내 사이버보안 파일(Cybersecurity File)로 편입 | QMSR §820.35/ISO 13485 §4.2.5 준수 | | 5.8.2 | QA Manager | SBOM 변경 이력의 추적성 확보 — 빌드 ID↔SBOM↔VEX 삼중 연결 | 1:1:1 대응 확인 | | 5.8.3 | RA Lead | FDA 실사 시 SBOM 즉시 제시 가능 상태 유지 (전자 서명 포함) | 2시간 내 제출 가능 | | 5.8.4 | Security Officer | QMSR 감사 관점 자체 점검 — SBOM 갱신 이력, VEX 판정 근거, 패치 타임라인 문서화 | 분기 자체감사 완료 | **QMSR 실사 체크포인트:** - 사이버보안 파일(Cybersecurity File)이 MDF 내 독립 섹션으로 구성되어 있는가? - SBOM이 최신 릴리스...

## ra_eu

### kb-eval-20261029-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "524d97005c5cf96c", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `524d97005c5cf96c`
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

> **Regulatory Draft – PMS & PMCF Planning for the Three In‑House Products**

---

### 1. Device portfolio & classification  

| Product | Intended function (summary) | MDR rule applied* | Assigned Class (MDR) |
|---------|----------------------------|-------------------|----------------------|
| X‑ray Detector (imaging sensor) | Records diagnostic X‑ray images; does **not** emit radiation. | Rule 17 – “Devices specifically intended for recording diagnostic images generated by X‑ray radiation” | **Class IIa** |
| Handheld X‑ray Source | Portable source that emits ionising radiation for radiography/radioscopy. | Rule 10 (radiology) – “Active devices that emit ionising radiation for diagnostic or therapeutic radiology” | **Class IIb** |
| GUI Software (SaMD) | Provides image display, measurement and decision support for the detector; any software error may affect diagnosis. | Rule 11 – “Software providing information used for diagnostic decisions” (impact limited to diagnostic aid) | **Class IIa** |

\*Rule numbers taken from MDR Annex VIII; classification confirmed against the product‑specific functional description.

---

### 2. Conformity‑assessment route (Art. 52 MDR)

| Product | Art. 52 paragraph | Required NB involvement | Reference |
|---------|-------------------|------------------------|-----------|
| X‑ray Detector (IIa) | Art. 52(6) – Annex IX (QMS + technical documentation assessment of a representative device) **or** Annex II/III + Annex XI §10 (production conformity verification). NB required for the QMS‑assessment path. | Yes (Annex IX route) | MDR Art. 52, Annex IX |
| Handheld X‑ray Source (IIb) | Art. 52(4) – Annex IX (full technical‑documentation assessment) **or** Annex X + Annex XI (type‑examination & production verification). NB required for either route. | Yes (Annex IX or Annex X+XI) | MDR Art. 52, Annex IX / Annex X |
| GUI Software (IIa) | Art. 52(6) – Annex IX (QMS + technical‑documentation assessment) **or** Annex II/III + Annex XI §10. NB required for the QMS‑assessment path. | Yes (Annex IX route) | MDR Art. 52, Annex IX |

*The chosen route should be documented in the EU Declaration of Conformity (Art. 19).*

---

### 3. Post‑Market Surveillance (PMS) system – mandatory elements  

| Requirement (MDR) | How it is satisfied for each product (source evidence) |
|-------------------|-------------------------------------------------------|
| **PMS plan** – Art. 84 | A written PMS Plan exists; source table lists data‑sources, collection methods and frequencies for all three products. |
| **PMS reporting** – Art. 83 | Vigilance incidents are reported through the EUDAMED vigilance module (source notes “UDI 등록 + Vigilance 보고”). |
| **Periodical Safety Update Report (PSUR)** – Art. 86 | PSUR frequency defined in source: Detector & GUI SW → every **2 years**; Handheld Source → every **1 year**. No specific identifier found in source — verify separately. |
| **Trend‑reporting** – Art. 88 | Quarterly internal statistical aggregation (source line “Trend reporting 데이터 – 내부 통계 집계 – 분기”). |
| **Data sources** – as per Table 1 of the excerpt (“Serious incidents + PSURs + FSCAs”, “Complaints”, “Literature”, “User feedback”, etc.) | All required categories are addressed; frequencies (immediate/quarterly, monthly, semi‑annual) are specified. |

---

### 4. PMCF planning – Annex XIV Part B  

| Item | Current state (source) | Gap / Additional evidence needed |
|------|------------------------|-----------------------------------|
| **PMCF need** (justification) | Detector: “동등성 클레임 검토 후 결정” (equivalence claim review pending). Source provides no definitive decision → **Missing** a documented justification. <br> Handheld source: “이온화 방사선 → 임상 데이터 적극 수집 권고” – recommendation only; needs a formal PMCF objective and protocol. <br> GUI SW: “사용 중 오류 데이터 수집 필수” – mandatory error‑data collection, but no explicit PMCF objectives or performance endpoints defined. |
| **PMCF protocol** (population, endpoints, follow‑up) | Not present in source. | Must be drafted (clinical‐performance plan, sample size, statistical analysis). |
| **Data sources for PMCF** | Listed under “PMS 담당 데이터 소스” (e.g., DQE degradation, dose over‑run, software error logs). | Need to map each data source to a specific pmcf objective and define acceptance criteria. |
| **Clinical evidence linkage** | CER mentioned as linked document for all three products but no details on the current state of the Clinical Evaluation Report. | Verify that a up‑to‑date CER (Annex XIV Part A) exists, includes literature review, clinical data, and equivalence justification – especially critical for the detector (Rule 17). |
| **Usability verification** (relevant to GUI SW) | No usability study referenced. | Conduct/submit IEC 62366‑1 usability engineering file; link findings to risk control measures (§5–§6 Annex I). |

---

### 5. Required evidence & documentation checklist  

| Document (MDR requirement) | Status per product | Comment / Missing items |
|-----------------------------|--------------------|--------------------------|
| **Technical Documentation** – Annex II §1‑6 | Implicitly prepared (EUDAMED UDI registration noted). | Ensure inclusion of design files, labeling (§23 Annex I), and GSPR compliance matrix. |
| **Risk Management File (RMF)** – Annex I §§3‑9 | Referenced (“CER, RMF” in source). | Verify that each identified hazard (radiation dose, DQE loss, battery failure, software error) has a corresponding risk‑control measure; update risk‐benefit analysis per new PMS data. |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | Referenced but not detailed. | Must contain: state‑of‑the‑art literature review, clinical data (including equivalence for detector), benefit‑risk conclusions. |
| **PMCF Plan & Report** – Annex XIV Part B | Only high‑level statements present. | Draft full PMCF plan (objectives, endpoints, methodology) and schedule periodic updates. |
| **PSUR** – Art. 86 | Frequency defined; no draft PSUR submitted. | Prepare PSURs according to the 2‑year / 1‑year cycles, include §§(a) benefit‑risk conclusions, (b) PMCF findings, (c) sales volume & user population. |
| **PMS Report** – Art. 85 (Class I only) – N/A | – | Not applicable (all products Class IIa/IIb). |
| **Usability Engineering File** – IEC 62366‑1 | Not mentioned. | Required for GUI SW (SaMD) to address use‑error risks (§5 Annex I). |
| **IEC 62220‑1‑1 DQE test data** – for Detector | Referenced (“CER, RMF, IEC 62220‑1‑1 시험 데이터”). | Ensure complete traceability of test methodology and results; include in PMS evidence. |
| **Software maintenance records & bug log** – IEC 62304 | Referenced for GUI SW. | Must be kept up‑to‑date and linked to post‑market incident handling (Art. 83). |

---

### 6. Risk controls (Annex I references)  

*For each product, the following generic risk‑control measures must be demonstrated:*

1. **Risk Management System** – §3 (RMF) – documented process aligned with ISO 14971:2019.  
2. **Risk control measures** – §4 – engineering safeguards for radiation dose (detector & source), battery protection, software fail‑safe mechanisms.  
3. **Use‑error mitigation** – §5 – UI design, user training, labeling (§23).  
4. **Device lifetime & maintenance** – §6 – especially for handheld source (battery health monitoring) and detector (periodic DQE calibration).  
5. **Transport & storage** – §7 – packaging integrity for the detector; shock/vibration testing per IEC 60601‑2‑54/28.  
6. **Benefit–risk assessment** – §8 – continual update with PMS data, PSUR conclusions.  

Specific controls should be cross‑referenced to the hazard list in each RMF.

---

### 7. Human‑escalation triggers (when to raise to senior RA / management)

| Trigger | Reason | Action |
|--------|--------|-------|
| **Missing or outdated CER** for any product | Clinical evidence gap → non‑conformity with Annex XIV Part A. | Escalate to clinical affairs lead; pause submission until CER completed. |
| **No formal PMCF plan** (only high‑level statements) | Non‑compliance with Art. 61 & Annex XIV Part B. | Immediate drafting required; senior RA review before next PSUR cycle. |
| **RMF not reflecting new PMS data** (e.g., recent DQE degradation incidents) | Benefit–risk determination may be outdated (§8). | Update RMF; if risk level changes, trigger a supplemental conformity assessment or field safety corrective action (FSCA – Art. 87). |
| **PSUR not prepared within scheduled interval** (1‑year for source, 2‑year for others) | Violation of Art. 86 reporting cadence. | Notify Quality Management; prepare interim report and inform Notified Body. |
| **Usability engineering file absent for GUI SW** | Use‑error risk (§5) cannot be demonstrated as mitigated. | Initiate usability study; involve Human Factors specialist. |
| **Any serious incident or FSCAs not logged in EUDAMED vigilance module within the required timeframe** | Breach of Art. 83 & vigilance obligations. | Immediate reporting to NB and competent authority; internal investigation. |

If any trigger is activated, a “Regulatory Gap Notification” should be logged, and senior RA sign‑off must be obtained before proceeding.

---

### 8. Peer‑review prompt  

> **Request:** Please review the assumptions made about classification (Rule 17 for the detector, Rule 10 for the handheld source, Rule 11 for the GUI software) and the selected conformity‑assessment routes. Verify that all data‑source mappings from the excerpt have been captured correctly and flag any missing elements (e.g., missing usability documentation, incomplete PMCF justification). Also confirm whether any jurisdiction‑specific obligations (e.g., additional MDR Annex III technical‑documentation items for active devices) need to be added.

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
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

### kb-eval-20261029-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "1ff9ae86eeb21bfd", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `1ff9ae86eeb21bfd`
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

> **Regulatory Draft – PMS / PMCF Planning for an Ionising‑Radiation Diagnostic Device (X‑ray Generator) and Associated SaMD**

---

### 1. Device description (summary)

| Item | Description |
|------|-------------|
| **Device type** | X‑ray generator used for diagnostic radiology (emits ionising radiation). May be coupled with a software application that provides image acquisition settings and/or interpretation support (SaMD). |
| **Intended use / indication** | Generation of therapeutic‑level X‑ray beams for projection radiography or fluoroscopy on adult patients. The software component supports dose‑optimisation and workflow guidance. |
| **Main subsystems** | 1. High‑voltage power supply & X‑ray tube assembly (hardware). <br>2. Control electronics & user interface (hardware + embedded firmware). <br>3. Dedicated medical device software (SaMD) that processes exposure parameters and may provide diagnostic decision support. |

---

### 2. Classification & conformity‑assessment route  

| Regulatory element | Reference |
|--------------------|-----------|
| **Classification rule** – active diagnostic equipment emitting ionising radiation → **Rule 10** (X‑ray generator) ⇒ **Class IIb**. | Source [2] |
| **Conformity‑assessment route** – Class IIb may use: <br>• **Annex IX** (full QMS + technical‑documentation assessment of a representative device) *or* <br>• **Annex X** (type‑examination) together with **Annex XI** (production conformity verification). | Art. 52(4) MDR 2017/745 |

*Recommendation:* adopt the **Annex IX** route because it allows a single NB audit covering both QMS (ISO 13485:2016) and technical documentation, which is efficient for devices with an integrated SaMD component.

---

### 3. Required evidence – Technical Documentation (Annex II)

| Section | Evidence to be supplied |
|---------|--------------------------|
| **1. Device description & specification** | Full device description, variants, accessories, intended purpose, and user environment. |
| **2. Manufacturer information** | Legal name, address, authorized representative (if applicable). |
| **3. Design & manufacturing information** | Engineering drawings, Bill of Materials, process flow diagrams, lot‑release procedures. |
| **4. General Safety & Performance Requirements (GSPR)** – Annex I §§1‑9 | Completed GSPR checklist mapping each requirement to design/production controls (see §8). |
| **5. Benefit–risk analysis** | Summaries of risk management file (ISO 14971:2019) and clinical evaluation conclusions (Annex XIV Part A). |
| **6. Verification & validation** | Test reports (electrical safety, EMC, radiation output per IEC 60601‑2‑28/‑54), software verification (IEC 62304, IEC 62366‑1), sterilisation (if applicable). |

*All above items must be kept current under Art. 61 (clinical evaluation) and Art. 84 (PMS plan).*

---

### 4. Clinical Evaluation & Post‑Market Clinical Follow‑up  

| Requirement | Detail |
|-------------|--------|
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – systematic literature review, clinical data from comparable devices, and any performed investigations. |
| **PMCF Plan** | Annex XIV Part B – objectives, methodology, required sample size, follow‑up duration, statistical analysis plan, and post‑market data sources (registries, user surveys, adverse event monitoring). |
| **PMCF Evaluation Report** | End‑of‑cycle report summarising findings, updating the benefit–risk determination, and feeding into PSUR. |

*Because the device is Class IIb, a structured PMCF programme is mandatory.*

---

### 5. Post‑Market Surveillance (PMS) System  

| Element | Reference |
|---------|-----------|
| **PMS system** – overall framework, processes, responsibilities, data handling | Art. 83 MDR |
| **PMS Plan** – description of routine and proactive activities, PMS report frequency, vigilance procedures | Art. 84 MDR |
| **Periodical Safety Update Report (PSUR)** – for Class IIb: at least annually, containing conclusions on benefit–risk, PMCF results, sales volume & user population | Art. 86(1)‑(2) MDR |

*The PSUR must incorporate the latest PMCF data and be submitted to the Notified Body as part of annual surveillance.*

---

### 6. Identified gaps – information still required

| Gap | Impact on submission |
|-----|----------------------|
| **Exact intended use wording** (e.g., “diagnostic radiography of adult patients, up to X mGy per exposure”) | Needed for correct classification under Rule 10 and to define the clinical evaluation scope. |
| **Target population details** (age range, special populations) | Influences risk analysis (§8) and PMCF design (sample size). |
| **Software functions & level of impact** (decision support vs. workflow aid) | Determines SaMD classification under Rule 11 (potentially Class IIa/IIb) and influences the depth of software verification & validation. |
| **Clinical data sources** (clinical investigations, registries, literature) | Required for CER completeness; missing data will delay Art. 61 compliance. |
> **Risk‑control evidence needed** – quantitative radiation safety test results (IEC 60601‑2‑28), usability test outcomes (IEC 62366‑1), software lifecycle documentation (IEC 62304). None of these are presently supplied.

---

### 7. Risk Management & GSPR Compliance (Annex I)

| GSPR clause | Planned control(s) |
|-------------|--------------------|
| **§3 – Risk management system** | ISO 14971:2019 file covering hazard identification, risk estimation, mitigation, and residual‑risk acceptance. |
| **§4 – Risk control measures** | Engineering controls for radiation shielding, interlocks, dose‑limiting software, periodic calibration per IEC 60601‑2‑28. |
| **§5 – Use‑error risks** | Human factors analysis (IEC 62366‑1) → user interface design, colour‑coding, training instructions. |
| **§6 – Device lifetime & maintenance** | Scheduled preventive maintenance plan; replacement intervals for X‑ray tube. |
| **§7 – Transport & storage** | Packaging validated for mechanical shock and temperature extremes; handling instructions. |
| **§8 – Known/foreseeable risks vs benefits** | Benefit–risk analysis incorporated in CER; ongoing reassessment via PMCF data. |
| **§16 – Radiation protection** | Compliance with IEC 60601‑2‑28 (X‑ray tube assemblies) and IEC 60601‑2‑54 (radiography equipment). |
| **§17 – Programmable electronic systems** | Software development according to IEC 62304; secure update mechanisms. |
| **§23 – Labeling & IFU** | Instructions for use include dose limits, safety warnings, and a QR code linking to the latest PMS/PMCF updates. |

All controls will be documented in the Technical Documentation (Annex II §4) and cross‑referenced in the GSPR checklist.

---

### 8. Human‑escalation triggers  

| Trigger | Action required |
|---------|-----------------|
| **Missing intended‑use statement** | Pause submission; request detailed Intended Use from product development before final classification confirmation. |
| **Unclear SaMD impact level** | Convene a multidisciplinary risk‑assessment board (clinical, software, regulatory) to decide whether Rule 11 places the software in Class IIa or IIb and adjust QMS scope accordingly. |
| **Absence of quantitative radiation test data** | Halt NB audit; obtain IEC 60601‑2‑28 compliance reports and repeat if gaps remain. |
| **Insufficient clinical evidence for CER** | Initiate a targeted clinical investigation or seek supplementary literature; update CER before Art. 61 review. |
| **PMCF plan not aligned with identified risks** | Revise PMCF objectives to specifically address residual radiation‑risk findings; resubmit PMCF plan to NB for approval. |
| **PMS data flow not mapped to PSUR sections** | Develop a data‑mapping matrix; ensure all PMS inputs feed into the annual PSUR (Art. 86). |

Escalation points should be recorded in the project risk log and reported to senior management immediately upon detection.

---

### 9. Peer‑review request  

> **Please review:**  
> 1. The assumption that Rule 10 automatically places the X‑ray generator in Class IIb (verify any device‑specific modifiers).  
> 2. Whether the SaMD component might be classified under a higher tier of Rule 11 based on its decision‑support functionality.   
> 3. Completeness of the GSPR checklist mapping – are there any Annex I clauses omitted for this technology (e.g., §§20‑22)?  
> 4. Adequacy of the proposed PMS/PMCF integration with the PSUR schedule for Class IIb devices.

---

**End of draft**.

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

> Intended use 서술에 "therapeutic-level X-ray beams for projection radiography" — 진단용 촬영/투시에 '치료 수준' 빔 표기는 자기모순 (치료용이면 Rule 9·별도 관리체계). 'diagnostic-level'로 정정 필요.

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261029-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "010d9e00df4aa9de", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `010d9e00df4aa9de`
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

> **Regulatory Draft – Post‑Market Surveillance & PMCF Planning (MDR 2017/745)**  

---

### 1. Scope of the draft
This document summarises the regulatory path that must be followed for a medical device that is currently at the “post‑market” stage in Europe. The focus is on:

* **Classification and corresponding conformity‑assessment route**  
* **Evidence package required for submission (technical documentation, clinical evaluation, PMS/PMCF)**  
* **Key gaps that must be filled before any NB audit**  
* **Risk‑management controls that satisfy the GSPR**  
* **Triggers for human escalation**

---

### 2. Classification  

| Step | Requirement (source) | What must be supplied | Current status |
|------|----------------------|-----------------------|----------------|
| 2.1  | “분류 원칙 (Article 51 + Annex VIII)” – manufacturer is responsible for self‑classification; the 22 rules are applied sequentially and the highest applicable rule determines the class.  *(Source 2, Chunk 1026819504541667541)* | • Full description of **intended medical purpose**, **mode of action**, **patient population**, **duration of contact**, **energy source** (if any). <br>• Identification of the specific Annex VIII rule(s) that apply. | Not provided – classification cannot be finalised. |
| 2.2  | “MDCG Manual on Borderline and Classification v2.1.1 (2023‑09)” is the reference for borderline cases. *(Source 2)* | • Evidence supporting the chosen rule (e.g., labeling, user instructions). | No evidence supplied yet. |

**Result:** *Classification cannot be determined without the missing product information.*  

---

### 3. Conformity‑assessment route (Art 52)  

| Device class (once known) | MDR route (Annex) | NB involvement |
|----------------------------|-------------------|----------------|
| **Class I (non‑sterile, non‑measuring)** | Art 52(7): self‑declaration – technical documentation (Annex II & III) + EU DoC (Art 19/Annex IV). | No NB required. |
| **Class Is / Im / Ir** | Art 52(7): Annex IX Chapters I & III *or* Annex XI Part A (limited scope for sterile/measuring/re‑usable surgical aspects). | NB required – limited scope review. |
| **Class IIa** | Art 52(6): Annex IX Chapters I & III + technical‑documentation assessment of one representative device per category, *or* Annex II & III + Annex XI §10/§18. | NB required – full technical‑doc review. |
| **Class IIb** | Art 52(4): Annex IX Chapters I & III + assessment of one representative device per generic group (or every implantable device individually), *or* Annex X + Annex XI. | NB required – type‑examination **or** full review. |
| **Class III** | Art 52(3): Annex IX (full technical‑doc assessment) *or* Annex X + Annex XI. | NB required – type‑examination plus production conformity verification. |

*The appropriate route will be selected once the class is confirmed.*  

---

### 4. Evidence package required for submission  

| Evidence element | Regulatory basis (framework) | What must be produced | Gaps identified |
|------------------|------------------------------|-----------------------|-----------------|
| **Technical Documentation** (TD) – Annex II §§1‑6 | Annex II (structure); risk‑management file per ISO 14971:2019 (Annex I §3). | • Device description, design, manufacturing processes, labeling (Annex I §23). <br>• GSPR compliance matrix (Annex I 23 requirements). | No TD available; risk‑management file missing. |
| **EU Declaration of Conformity** | Art 19; content in Annex IV. | Completed DoC with reference to all applicable standards and NB certificate (if any). | Not drafted. |
| **Clinical Evaluation Report (CER)** | “CEP + CER (Article 61, MDR Annex XIV)” *(Source 1, Chunk 1024305232637496780)*. | • Systematic literature review (state‑of‑the‑art). <br>• Clinical data from own investigations or equivalence. <br>• Benefit–risk determination (Art 61). | No CER drafted; no clinical data identified. |
| **Post‑Market Surveillance (PMS) Plan** | Art 84 (system); Art 83 for PMS system. (framework citation) | • Description of systematic procedures, periodic safety update reports (PSUR), trend reporting (Art 88), vigilance (Art 87). | No PMS plan documented; no PSUR/PMCF schedule. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B (PMCF planning). *(Source 1)* | • Defined PMCF objectives, methods, sample size, timelines, and evaluation criteria. <br>• Interim/final PMCF report summarising findings. | No PMCF plan or study protocol exists. |
| **UDI registration** | UDI portal (Korea) & EUDAMED (Art 33‑39). *(Source 1)* | • Unique Device Identifier assigned, entered in EUDAMED database. | Only Korean UDI mentioned; EU UDI not yet allocated. |
| **Vigilance & Incident Reporting** | Art 87 (serious incidents and FSCA); PSUR (Art 86) for Class IIa‑III. | • Procedure to capture and report serious adverse events within 15 days (MDR). | No vigilance procedure documented. |

---

### 5. Identified missing information & actions required  

| Missing item | Reason it is needed | Action |
|--------------|----------------------|--------|
| **Intended purpose / labeling** | Drives classification, risk‑analysis, and clinical evaluation scope. | Obtain final IFU (Instructions for Use) from product development. |
| **Energy source / invasiveness data** | Determines which Annex VIII rule applies (e.g., Rule 9, 10, 11). | Provide engineering spec sheets and user‑scenario description. |
| **Clinical data sources** (e.g., equivalence justification, clinical investigation results) | Required for CER & PMCF. | Compile literature search strategy; plan/execute prospective clinical study if no equivalent data exist. |
| **Risk Management File (RMF)** – hazard analysis, risk control measures, residual‑risk evaluation. | MDR GSPR §3–9 require a documented RMF. | Produce ISO 14971‑compliant RMF and link to TD. |
> **Note:** No specific identifiers for the above items appear in the source excerpts; they must be verified separately.

---

### 6. Risk‑management controls (GSPR compliance)  

* **Risk Management System** – per Annex I §3 (risk management plan, hazard identification, risk estimation, risk control, residual‑risk evaluation).  
* **Use‑error mitigation** – Annex I §5; include usability engineering activities (IEC 62366‑1:2020) to address user interface hazards.  
* **Lifetime & maintenance** – Annex I §6; define service life, preventive maintenance schedule.  
* **Transport & storage** – Annex I §7; specify handling requirements.  
* **Known and foreseeable risks vs benefits** – Annex I §8; evidence must be captured in the CER/PMCF.  

All risk‑control measures shall be traceable to design inputs and reflected in the Technical Documentation (Annex II §6.1).

---

### 7. Human‑escalation triggers  

| Trigger | Reason for escalation | Escalation recipient |
|--------|-----------------------|----------------------|
| **Classification cannot be resolved** (insufficient intended‑use data) | Prevents selection of correct conformity‑assessment route and NB involvement. | Senior RA Manager / Regulatory Project Lead. |
| **Absence of a PMS Plan or PMCF protocol** | MDR requires a systematic post‑market system before any NB audit; missing plan blocks submission. | Head of Post‑Market Surveillance. |
| **No risk‑management file available** | GSPR non‑compliance leads to major NB findings. | Quality Management System (QMS) Lead. |
| **Clinical evidence gap** (no CER, no equivalence justification) | CER is mandatory under Art 61; without it the device cannot be CE marked. | Clinical Affairs Director. |
| **UDI not allocated in EUDAMED** | Mandatory for all devices placed on the EU market (Art 33‑39). | Regulatory Operations Coordinator. |
| **Pending NB contract & fee quotation** | Financial and contractual readiness must be confirmed before audit scheduling. | Finance / Procurement Officer. |

Escalations should be logged in the project‑management tool with a “red” status and a target resolution date of ≤ 5 working days.

---

### 8. References  

| Ref. | Description |
|------|-------------|
| **Art 51 + Annex VIII** – classification rules (source 2). |
| **MDCG Manual on Borderline and Classification v2.1.1 (2023‑09)** – guidance for borderline cases (source 2). |
| **Article 61, MDR Annex XIV** – requirement to maintain a current Clinical Evaluation Report (source 1). |
| **Art 84 / Art 83** – PMS plan and system (framework citation). |
| **Annex I §§3‑9** – risk‑management system requirements (framework citation). |
| **ISO 14971:2019**, **IEC 62366‑1:2020**, **IEC 62304:2006+A1:2015** – applicable standards for risk management, usability and software lifecycle. |
| **Art 19 / Annex IV** – EU Declaration of Conformity (framework citation). |
| **Art 87, Art 86, Art 85** – vigilance, PSUR and PMS reporting obligations (framework citation). |

*All citations follow the developer‑provided rule: framework references are stated as facts; instance identifiers appear only when explicitly present in the source excerpts.*  

---

### 9. Peer‑review prompt  

> **@RA‑Peer:** Please challenge the assumptions made about the classification process, especially the reliance on the MDCG Manual for borderline cases. Verify whether any additional EU guidance (e.g., MEDDEV 2.7/1) should be incorporated and confirm that all required evidence items have been captured for a Class IIa device scenario. Identify any jurisdiction‑specific gaps that may affect the PMS‑PMCF planning in the European context.

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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261029-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6c7b4cc32fed98bf", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `6c7b4cc32fed98bf`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_MDR_2017_745.md)
- Source hash: `15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_MDR_2017_745.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | |...
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning  
(derived from the “EU MDR — Regulation (EU) 2017/745” guide and internal TD‑creation workflow)**  

---

## 1. Device Scope & Immediate Classification Gap
| Item | Current status (based on source) | What is still required |
|------|----------------------------------|------------------------|
| **Intended purpose / indication** | Not disclosed in the excerpts. | Obtain a clear, manufacturer‑authored “Intended Use” statement and any relevant labeling claims. |
| **Device type (active, invasive, software, X‑ray system, …)** | Only a generic reference to “X‑ray system application guidance” in the guide metadata. | Clarify whether the device is: <br>– Active therapeutic (Rule 9) or diagnostic (Rule 10/17), <br>– Implantable, <br>– Software‑only, etc. |
| **Applicable classification rule** | Not identified. | Map the intended purpose to the appropriate Rule in Annex VIII (e.g., Rule 9, Rule 10, Rule 11, Rule 17) and derive Class I/Is/Im/Ir, IIa, IIb or III. |
| **Resulting conformity‑assessment route** | Undetermined until class is known. | Once the class is fixed, select the route per Art. 52 (see Table 2 below). |

> **Human escalation trigger #1:** *If intended purpose and classification cannot be confirmed within 5 working days of this draft, pause all downstream documentation work and request a formal “Intended Use & Classification” briefing from R&D/Marketing.*

---

## 2. Technical Documentation (TD) – Mandatory Content (Annex II §§1‑6)

| Annex II Section | Required Artefact(s) | Current status in workflow (Excerpt [1]) | Gap / Action |
|-------------------|----------------------|------------------------------------------|--------------|
| **§1 Device description & intended purpose** | Detailed device description, indications for use, contraindications. | Not yet produced – step 2 (R&D) only “설계·제조 정보” is collected. | Draft the description and indication; include classification rule reference. |
| **§2 Manufacturing information** | Process flow diagram, manufacturing sites, quality control procedures. | Covered by step 2 (design & V&V collection). | Verify that supplier approvals and process validations are documented. |
| **§3 Design & packaging** | Drawings, specifications, packaging & labeling concepts. | Implicit in “설계·제조 정보”. | Add final drawings and label mock‑ups. |
| **§4 General Safety & Performance Requirements (GSPR) mapping** | Completed GSPR checklist & report. | Step 3 (RA/QA) produces “GSPR 적합성 보고서”. | Ensure mapping covers all 23 Annex I requirements; link each to supporting evidence. |
| **§5 Clinical evaluation** | Clinical Evaluation Report (CER) – updated per Annex XIV Part A. | Step 4 (RA/Clinical) creates CER. | Confirm inclusion of state‑of‑the‑art literature, clinical data (pre‑market & post‑market), and benefit–risk analysis. |
| **§6 Post‑Market Surveillance** | PMS plan (Art. 84), PMS report / PSUR (Art. 85/86), PMCF plan (Annex XIV Part B). | Step 6 (RA) writes “PMS Plan”. No explicit PMCF plan yet. | Develop a PMCF plan that details study design, endpoints, sample size, timeline; integrate it into the overall PMS system. |
| **§7 Risk Management** | Integrated Risk Management File (RMF) – ISO 14971‑2019 compliant. | Step 5 (QA) produces “위험관리 보고서”. | Verify that risk analysis, evaluation of residual risk, and risk‑control measures are fully documented and traceable to GSPR §§3‑8. |
| **§8 Labeling & IFU** | Full labeling pack (EU language required), UDI assignment. | Not mentioned in the workflow. | Draft labeling per Annex I §23; allocate a UDI per Regulation (EU) 2017/746 and record it in EUDAMED. |

> **Human escalation trigger #2:** *If any of the TD sections above remain incomplete after the scheduled “RA Lead – 전체 TD 검토·승인” deadline, the RA Lead must raise an exception report to Quality Management (QM) for a revised timeline.*

---

## 3. Post‑Market Surveillance System (Art. 83 & Art. 84)

| Requirement | Evidence Required | Current Status | Gap / Action |
|-------------|-------------------|----------------|--------------|
| **PMS system architecture** (Art. 83) | Documented PMS processes, responsibilities (PRRC), data collection methods, trend analysis workflow. | Step 6 of the TD workflow creates a “PMS Plan”. No full system description yet. | Expand the plan into a complete PMS System SOP (see SOP‑PSUR‑001 in the guide). |
| **PMS plan** (Art. 84) | Schedule for periodic safety update reports, field safety corrective actions (FSCA), vigilance procedures (Art. 87). | “PMS Plan” exists but content not shown. | Verify inclusion of: <br>– Frequency (e.g., annual PSUR for Class IIb/III, biennial for IIa) <br>– Data sources (complaints, registries, literature monitoring) <br>– Roles & escalation matrix (PRRC, QA). |
| **PMS Report** – Class I (Art. 85) or PSUR – Classes IIa‑III (Art. 86) | • Summary of PMS data<br>• Benefit‑risk conclusions (link to CER)<br>• PMCF findings (if applicable) | Not yet produced; will be generated after the first reporting period. | Define reporting calendar aligned with class‑specific cadence (see Art. 86(2)). |
| **Trend Reporting** (Art. 88) | Structured analysis of recurring incidents, field trends, and corrective actions. | Implicit in PMS plan but not yet detailed. | Include a template for trend reports; assign responsibility to QA. |

> **Human escalation trigger #3:** *If the PMS plan does not specify the PSUR frequency matching the device class (Art. 86(2)), the RA Lead must request amendment before NB submission.*

---

## 4. Post‑Market Clinical Follow‑up (PMCF) – Annex XIV Part B

| Element | Required Content | Current Status | Gap / Action |
|---------|------------------|----------------|--------------|
| **PMCF plan** | • Objective and scope<br>• Study design (prospective, retrospective, registry)<br>• Sample size & statistical rationale<br>• Endpoints aligned with clinical performance claim<br>• Timing & interim analyses<br>• Data management & monitoring procedures | Not yet created; only a CER update is mentioned (step 4). | Draft PMCF plan and link it to the PMS system. |
| **PMCF evaluation report** (to be submitted with periodic safety update) | • Summary of collected clinical data<br>• Assessment against benefit‑risk determination (Art. 61)<br>• Recommendations for changes in labeling, design, or surveillance | Not applicable yet – no data collection started. | Define start date and milestones; ensure traceability to the CER. |
| **Integration with PMS** | • Use of PMCF outcomes as input for risk reassessment (ISO 14971) and GSPR updates. | Implicit but not documented. | Add a cross‑reference in the RMF showing how PMCF data will trigger residual‑risk re‑evaluation. |

> **Human escalation trigger #4:** *If the PMCF plan cannot be finalised before the NB submission of the technical documentation, request a “Conditional Acceptance” from the Notified Body with a detailed timeline for completing PMCF activities.*

---

## 5. Risk Management (Annex I §3‑9; ISO 14971:2019)

| Required Output | Evidence | Current Status | Gap / Action |
|-----------------|----------|----------------|--------------|
| **Risk Management Plan** (RMF) | Scope, methodology, responsibilities, risk acceptance criteria. | Part of “위험관리 보고서” (step 5). | Confirm inclusion of post‑market risk assessment (per Art. 83). |
| **Risk analysis & evaluation** | Hazard identification, severity/occurrence estimation, risk matrix. | Expected in the RMF. | Ensure all identified hazards are mapped to GSPR §§4‑8 and that any new hazards from PMS data will be captured. |
| **Risk control measures** | Design controls, protective measures, information for users (labeling, training). | Should be reflected in “GSPR 적합성 보고서”. | Verify each residual risk is justified against the intended purpose (Annex I §8). |
| **Residual risk evaluation & benefit‑risk determination** | Documentation of overall acceptability. | Implicit in CER and RMF. | Explicitly state the residual‑risk acceptance criteria and link to clinical benefit evidence. |

> **Human escalation trigger #5:** *If any new hazard is identified during PMS that was not covered by the original risk analysis, a “Risk Re‑assessment” must be initiated immediately and reported to the PRRC.*

---

## 6. Conformity‑Assessment Route (Art. 52)

| Device Class (to be confirmed) | Applicable route (Annex) | NB involvement |
|-------------------------------|--------------------------|----------------|
| **Class I** (non‑sterile, non‑measuring) | Art. 52(7) – self‑declaration; TD & DoC only | No NB required |
| **Class Is / Im / Ir** (sterile, measuring, reusable surgical) | Art. 52(7) – Annex IX Chapters I & III *or* Annex XI Part A (limited scope) | Yes (limited) |
| **Class IIa** | Art. 52(6) – Annex IX (QMS + technical‑doc assessment of one representative device) *or* Annex II/III + Annex XI §10 or §18 | Yes |
| **Class IIb** | Art. 52(4) – Annex IX (full QMS + technical‑doc assessment) *or* Annex X + Annex XI | Yes |
| **Class III** | Art. 52(3) – Annex IX (full assessment) *or* Annex X + Annex XI | Yes |

> **Human escalation trigger #6:** *As soon as the class is determined, update the “Conformity‑Assessment Route” matrix and circulate to the RA Lead for NB selection. If the device falls into Class IIb/III, start early engagement with a Notified Body (NB) to negotiate timelines.*

---

## 7. Supporting Standards & Guidance Referenced in Source [2]

| Standard | Relevance |
|----------|-----------|
| **ISO 13485:2016** – QMS requirements (Art. 10(9), Annex IX). |
| **ISO 14971:2019** – Risk management (Annex I §3‑9). |
| **IEC 62304** – Software life‑cycle (if software component present). |
| **IEC 60601‑1** – General safety for electrical medical devices. |
| **IEC 60601‑2‑54** – Specific requirements for X‑ray equipment (relevant to the “X‑ray system” guidance mentioned). |
| **UDI Regulation (EU) 2017/746** – Identifier assignment and EUDAMED registration. |

These standards are listed in the guide metadata (Excerpt [2]) and must be cited within the TD where applicable.

---

## 8. Summary of Immediate Actions & Deliverables

1. **Obtain intended use statement & classification rule** → assign device class.  
2. **Complete Annex II §1‑6 artefacts**: device description, GSPR mapping, CER update, risk file, labeling, UDI.  
3. **Develop full PMS System SOP** (based on Art. 83/84) and schedule PSUR/Trend reports.  
4. **Draft PMCF plan** (Annex XIV Part B) & integrate into RMF.  
5. **Map all identified hazards to GSPR §§4‑8**; document residual risk acceptability.  
6. **Select conformity‑assessment route** and initiate NB contact where required.  

All above items must be documented, reviewed by the RA Lead (step 7), and then submitted to the Notified Body (step 8) as per the workflow in Excerpt [1].

---

## 9. Peer‑Review Prompt

> **To a fellow EU RA colleague:**  
> Please challenge the assumptions made above regarding (i) the need for a separate PMCF plan versus inclusion within the PMS system, (ii) the sufficiency of the “GSPR 적합성 보고서” as evidence of full Annex I compliance, and (iii) any jurisdiction‑specific gaps that may arise from the X‑ray equipment context (e.g., additional IEC 60601‑2‑54 testing or radiation protection documentation). Highlight any missing cross‑references to EUDAMED registration obligations (Art. 33‑39) that should be reflected in the TD.

--- 

*End of draft.*

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
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> UDI 배정 근거를 "Regulation (EU) 2017/746"로 인용 — 2017/746은 IVDR이며 MDR은 2017/745. 규격 오귀속 (관할/인용 계열). / **1점 확정**: ① UDI 근거를 Reg. (EU) 2017/746(=IVDR)로 오귀속(MDR은 2017/745) ② Annex II를 §1~§8로 서술 — 실제 Annex II는 6개 섹션이며 §7 Risk Management·§8 Labeling은 존재하지 않음(구조 창작) ③ GSPR/Annex 번호 다수 부정확. 체계적 구조 창작+규격 오귀속 → 정정 필요.

**Source Excerpts**

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `1072636411107495596`

> --- doc-id: EU_MDR_2017_745 title: "EU MDR — Regulation (EU) 2017/745 요약 및 적용 지침" type: Guide version: v0.3.1 status: draft category: 01_법규_규제 purpose: "EU MDR 2017/745 핵심 요구사항, 2026 일정, 기술문서 구성 및 X-ray 시스템 적용 지침" applicable: [EU MDR 2017/745, EU MDR GSPR Annex I, ISO13485:2016, ISO14971:2019, IEC 62304, IEC 60601-1, IEC 60601-2-54, UDI] forms: [F-MDR-TD-CHK-001] related-docs: - GSPR_정합표준_매핑표 - GSPR_체크리스트_v0.2_템플릿 - PRRC_역할_및_한미_대응자_매핑 - EU_AI_Act_MDR_중첩적용_매핑 - ISO13485_2016_요약 - SOP-CC-001 - SOP-PSUR-001 - SOP-FSCA-001 - TF-TD-001 related-issues: [4, 5, 22, 33, 989] owner: RA/QA Lead last-review: 2026-07-23 review-due: 2027-06-09 --- # EU...

### kb-eval-20261029-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "a2dd55dcaac9987b", "source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md", "source_hash": "62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a2dd55dcaac9987b`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning  
(Prepared for EU MDR 2017/745 compliance)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Assessment | Rationale / Evidence Required |
|------|------------|--------------------------------|
| **Intended purpose / indication** | *Not provided in source* – must be defined by the manufacturer (e.g., “diagnostic imaging of musculoskeletal tissue”). | Determines which Annex VIII rule applies. |
| **Applicable classification rule** | **Rule 9, 10, 11 or 17** (active therapeutic, active diagnostic, software, X‑ray recording) – *to be selected once intended purpose is known*. | Classification must be justified in the Technical Documentation (Annex II §6). |
| **Class outcome** | Likely **Class IIa** for most non‑implantable active devices; could rise to **IIb** or **III** if energy delivery, invasive use, or life‑sustaining decisions are involved. | Until the rule is identified, classification remains “to be determined”. |
| **Conformity‑assessment route** | – **Art 52(6)** → Annex IX (QMS + technical‑documentation assessment) for Class IIa  <br>– **Art 52(4)** → Annex X + Annex XI for Class IIb/III (type‑examination + production conformity verification). | The route follows the class determined above. Cite **Art 52** and relevant annexes. |

*Regulatory citations:*  
- Classification rules – **Annex VIII**, Rules 9, 10, 11, 17.  
- Conformity routes – **Art 52(6)** (Class IIa) → **Annex IX**; **Art 52(4)** (Class IIb/III) → **Annex X + XI**.

---

### 2. Mandatory Post‑Market Evidence (MDR)

| Requirement | MDR Provision | Content Required | Current Status (per source) |
|-------------|---------------|------------------|----------------------------|
| **PMS system** | **Art 83** | Organizational structure, responsibilities, SOPs for data collection, signal detection, trend analysis. | No evidence supplied – must be drafted. |
| **PMS plan** | **Art 84** | Defined activities (e.g., vigilance reporting, periodic safety update), timelines, resources, and documentation of risk‑benefit evaluation. | Missing – to be prepared. |
| **Periodic Safety Update Report (PSUR)** | **Art 86** (Classes IIa/IIb/III) | • Benefit–risk conclusions <br>• Main PMCF findings <br>• Sales volume & user population <br>• Update frequency (≥2 yr for IIa, ≥1 yr for IIb/III). | Not yet generated – contingent on classification. |
| **Clinical Evaluation Report (CER)** | **Annex XIV Part A** (kept current under Art 61) | State‑of‑the‑art literature review, clinical data appraisal, benefit–risk analysis. | No CER provided; a gap. |
| **PMCF plan & evaluation report** | **Annex XIV Part B** | Planned post‑market studies, objectives, methods, endpoints, sample size, data management, timelines; final evaluation summarising results and impact on GSPR compliance. | Absent – must be created. |

---

### 3. Risk Management Integration  

| Element | MDR / Standard Reference | Required Artefact |
|---------|---------------------------|-------------------|
| **Risk‑management system** | **Annex I Chapter I §3** (RMF basis) + **ISO 14971:2019** (current edition) | Full Risk Management File (risk analysis, evaluation, control measures, residual risk acceptance). |
| **Verification of risk controls** | **Annex II §6.1** (technical‑documentation evidence of GSPR compliance) | Test reports, validation data, usability studies (IEC 62366‑1), software safety (IEC 62304), etc. |

*Note:* The source does not mention any existing RMF – a major gap that must be addressed before NB audit.

---

### 4. EUDAMED Registration – Module 2 (UDI/Device)  

| Requirement (source) | Description | Evidence Needed |
|----------------------|-------------|-----------------|
| **Basic UDI‑DI** | Globally unique identifier for the device family/version. Must be assigned in EUDAMED. | Decision on Basic UDI‑DI, registration with an issuing agency (GS1 / HIBCC / ICCBBA). |
| **UDI‑DI & UDI‑PI structure** | Fixed part (UDI‑DI) + variable part (UDI‑PI: lot/serial). | Populate EUDAMED fields for each device model and each production batch. |
| **Issuer selection** | Choose one of the three accredited organisations. | Documentation of issuer contract / certificate. |

*Regulatory citation:* No specific article or paragraph number appears in the source material – **no specific identifier found in source — verify separately**.

---

### 5. Identified Missing Information & Evidence Gaps  

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **Intended purpose / intended medical use** | Prevents rule selection → classification uncertainty. | Obtain a clear Intended Use Statement from the product team. |
| **Classification rule (Annex VIII)** | Determines conformity route & PMS obligations. | Conduct a formal Classification Decision Document. |
| **Clinical data (pre‑market or post‑market)** | Required for CER and PMCF plan. | Gather all clinical investigation reports, literature, and/or real‑world evidence. |
| **Risk Management File** | Mandatory under Annex I §3 & ISO 14971. | Compile risk analysis, control measures, verification results. |
> **Human‑Escalation Trigger #1:** If classification cannot be substantiated within 10 working days, pause any EUDAMED entry and alert the Regulatory Lead.

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **PMS system & plan (Art 83/84)** | Non‑compliance leads to NB rejection. | Draft SOPs, define data sources, allocate responsibilities; circulate for review. |
> **Human‑Escalation Trigger #2:** Absence of a signed PMS plan after the first draft review → immediate escalation to Quality Manager.

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **PMCF plan & evaluation report (Annex XIV Part B)** | Required for Class IIa+ devices; missing PMCF halts certification. | Design a post‑market clinical study (e.g., prospective registry) aligned with identified residual risks. |
> **Human‑Escalation Trigger #3:** If no feasible PMCF design can be drafted within 4 weeks, involve Clinical Affairs for alternative evidence (e.g., real‑world data).

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **EUDAMED Module 2 fields** – Basic UDI‑DI, issuer, device model list | Device cannot be placed in the EUDAMED database → no CE marking issuance. | Complete UDI allocation matrix; submit to chosen issuing agency and record identifiers. |
> **Human‑Escalation Trigger #4:** Failure to receive UDI‑DI from the issuing agency within 2 weeks of request → notify Project Manager.

---

### 6. Summary Judgment  

1. **Classification** – Cannot be finalised without a formal intended‑use statement; most likely Class IIa, but could rise to IIb/III pending rule identification.  
2. **Conformity route** – Will follow **Art 52(6) → Annex IX** for Class IIa or **Art 52(4) → Annex X + XI** for higher classes.  
3. **Core evidence missing:** PMS system & plan, PSUR (if applicable), CER, PMCF plan/evaluation report, complete Risk Management File, and UDI registration data in EUDAMED Module 2.  

All identified gaps must be closed before the Notified Body can perform a technical‑documentation assessment or type‑examination.

---

### 7. Peer‑Review Prompt  

> **To a fellow Regulatory Affairs colleague:**  
> Please review the assumptions made regarding the likely classification (Rule 9/10/11/17), the suggested conformity‑assessment routes, and the completeness of the listed PMS/PMCF artefacts. Verify whether any additional EU‑specific obligations (e.g., language requirements for labeling per Annex I §23, or specific IEC standard references for X‑ray devices) have been omitted from this draft. Highlight any discrepancies with the source material on EUDAMED Module 2 and propose missing identifiers that must be captured before final submission.

**Citation Lint (C1/C3 — 구조적 인용 오류 자동 감지)**

- ⚠️ Art. 52(4) is inconsistent with the device class on this line (Class IIa (52(6))) — verify the paragraph against MDR Art. 52. (`Art 52(4)`)

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

> "Art 52(4) → Annex X+XI for Class IIb/III" (2회) — III의 적합성평가 단락은 52(3)이며 52(4)는 IIb. **C3 린트 라이브 첫 포착(진양성)**. Annex 조합(X+XI) 자체는 III에도 유효하나 단락 귀속 오류.

**Source Excerpts**

1. Chunk `1048620351506847107`

> ### 5-A. 데이터베이스 등록 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR (EU) | |---|---|---|---| | 등록 DB | GUDID (FDA UDI DB) | UDI포털 (mfds.go.kr) | EUDAMED | | 의무화 시점 | 등급별 단계적 완료 | 2025 기준 진행 중 | 2026-05-28 (4개 모듈) | | 경제주체 등록 | FDA Establishment Registration (21 CFR 807) | 의료기기 제조업 허가 | SRN (Actor Module) | | 기기 등록 | 510(k)/PMA cleared → GUDID | 허가/인증/신고 후 UDI포털 | EUDAMED UDI/DEV | | UDI 발급기관 | GS1, HIBCC, ICCBBA | GS1(의무), HIBCC(가능) | GS1, HIBCC, ICCBBA | | Vigilance 보고 | eMDR (FDA MedWatch) | 이상사례 포털 | Module 5 (~Q2 2027) |

2. Chunk `1068273778649251618`

> ### Module 2: UDI/Device Registration (UDI/DEV) — UDI 및 기기 등록 #### 3-2-A. UDI 구조 ``` UDI = UDI-DI (고정) + UDI-PI (가변) Basic UDI-DI (레거시 식별자) └── UDI-DI (모델별) └── UDI-PI (생산 로트/일련번호) ``` - **Basic UDI-DI**: 동일 기기 군/버전을 식별하는 핵심 레퍼런스. EUDAMED에서 Globally Unique해야 함. - **UDI-DI**: 특정 버전/제품 모델 식별. - 발급 기관: GS1, HIBCC, ICCBBA 중 선택. #### 3-2-B. 등록 데이터 항목 (주요)

## ra_kr

### kb-eval-20261029-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "1f1e7947a3ceda2e", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "00026234f8ec1153306309dc7c82b355b5fdfc4d7a5de00dbd5247374b13eccb"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `1f1e7947a3ceda2e`
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

> **Regulatory Draft – Digital X‑ray Imaging System (Generator + Detector + Acquisition Workstation + AI Post‑Processing)**  

---

### 1. Scope of the Digital Medical Products Act (디지털의료제품법)

| Component | Subject to 디지털의료제품법? | Reasoning (source) |
|-----------|----------------------------|--------------------|
| Generator firmware – hardware‑only, no network | **No** (X) | “HW 제어 전용, 비연결” → not a digital medical product. 【1】 |
| Detector firmware – may be networked | **Conditional** (△) | “네트워크 연결 시 해당 가능” → requires further confirmation of connectivity. 【2】 |
| Acquisition Workstation software – standalone operation, network‑connected, AI‑enabled | **Yes** (○) | “SW 단독 조작·네트워크 연결·AI 가능성”. 【2】 |
| AI‑based image post‑processing module | **Yes (if deployed)** (○) | “SaMD + AI 분류”. 【2】 |
| DICOM/PACS interface – communication function only | **Conditional** (△) | “통신 기능, 독립형 SW 경계 검토”. 【2】 |

> **Regulatory implication:** All components confirmed as “Yes” must be evaluated under the Digital Medical Products Act and MFDS medical‑device regulations. The conditional items require a network‑connectivity assessment; if they are ever enabled for remote operation they will also fall under the same regime.

---

### 2. Korean Device Classification (1–4등급) & Submission Route  

| Component (as a combined system) | Likely grade (KR) | Basis* |
|-----------------------------------|------------------|--------|
| X‑ray acquisition workstation + AI post‑processing (diagnostic imaging software) | **3등급** | Software that directly influences diagnosis is treated as “high risk” in the 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| Detector firmware (if networked) | **2등급** (tentative) | Firmware providing only data acquisition without diagnostic interpretation generally falls under 2등급, but final grade must be confirmed by the MFDS grading table. |
| Generator firmware (non‑networked) | **1등급** (exempt) | Pure hardware control, no software decision making. |

\*When the source does not specify a grade, the exact classification must be verified against the official MFDS grading regulation (MFDS_인허가_상세가이드.md §2).  

**Submission routes**

| Grade | Pathway |
|------|---------|
| 1등급 → 신고 |
| 2등급 → 인증 (technical‑documentation review by an MFDS‑designated 심사기관) |
| 3등급·4등급 → 허가 (MFDS approval) |

**Therefore:** The integrated X‑ray imaging system will most likely require a **허가** submission (3등급). The detector firmware, if confirmed as networked, would be submitted via **인증**; the generator firmware via **신고**.

---

### 3. Evidence Package Required for 허가 (3등급)  

| Requirement | Detail / Standard | Citation |
|-------------|-------------------|----------|
| **KGMP Facility Certification** | 의​료기기법 제28조, KGMP 인증 (2026‑07‑01 개편 후 적용) | framework reference |
| **Risk Management File** | ISO 14971:2019 (risk analysis, risk evaluation, risk control) | framework reference |
| **Software Lifecycle Documentation** | IEC 62304:2006+A1:2015 (development plan, verification/validation reports) | framework reference |
| **Usability Engineering** | IEC 62366‑1:2020 | framework reference |
| **Cybersecurity & SBOM** | MFDS 고시 제16조 SBOM 관리 (mandatory SBOM), 권고 SPDX 2.3 or CycloneDX 1.5, RA‑07 항목 | “보안 지침 제16조 SBOM 관리”【1】; “RA‑07 항목”【1】 |
| **Clinical Evaluation** | Foreign clinical evaluation report (CER) accepted per MFDS notice expanding foreign CER acceptance *if* the device has an FDA 510(k) or CE mark. Must be mapped to Korean requirement; local data required when risk is high (>3등급). | framework reference – specific notice number not provided in source |
| **Korean‑language Labeling & IFU** | Labeling law (식품의약품안전처 고시) – all labeling, instructions for use, and safety information must be in Korean. | framework reference |
| **Post‑Market Surveillance Plan** | MFDS PMS guidance (PMS Plan, 시판후조사) – includes periodic safety update reports. | framework reference |
| **Software Bill of Materials (SBOM)** | SPDX 2.3 or CycloneDX 1.5 format; must contain NTIA 7요소 + EOL + 취약점 정보. | “SPDX 2.3 / CycloneDX 1.5”【1】 |
| **Device Master File (DMF) for AI Algorithm** | Documentation of algorithm development, training data provenance, performance metrics, explainability, and bias mitigation. | framework reference |

---

### 4. Missing Information that Must Be Obtained Before Submission  

1. **Exact intended use statement** for each software component (diagnostic vs. adjunct).  
2. **Confirmation of network connectivity** for detector firmware and DICOM/PACS interface – if enabled, they become subject to the Digital Medical Products Act.  
3. **Clinical performance data** – either local clinical study or justified foreign CER with mapping matrix.  
4. **Korean‑language labeling drafts** (product name, symbols, warnings).  
5. **Full SBOM** in SPDX 2.3 *or* CycloneDX 1.5 (currently only “recommendation” is noted).  
6. **KGMP certification status** of the manufacturing site(s).  
7. **Detailed risk control measures** for AI algorithm (e.g., drift monitoring, re‑validation schedule).  
8. **User environment description** (clinical setting, operator training level).  

---

### 5. Core Risk Controls & Mitigations  

| Hazard | Control (per ISO 14971) | Implementation Note |
|--------|-------------------------|----------------------|
| Unauthorized software modification | Digital signature, Secure boot, SBOM‑based vulnerability tracking | Align with MFDS 고시 제16조 SBOM 관리【1】 |
| Network intrusion / data exfiltration | TLS/SSL encryption for DICOM, VPN segmentation, regular penetration testing | Reference FDA 524B cyber‑plan (for guidance) |
| AI algorithm bias or drift | Periodic performance monitoring, retraining schedule, transparent reporting of metrics | Map to EU MDR PSUR style but implement Korean PMS format |
| Radiation exposure mis‑setting (via firmware) | Interlock logic, dose‑limit enforcement, fail‑safe default states | Covered in risk analysis for hardware controller |
| Software malfunction leading to erroneous diagnosis | Redundant verification checks, user alerting, “human in the loop” requirement | Documented in IEC 62366‑1 usability evaluation |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger Action (RA lead) |
|-----------|--------------------------|
| **Unresolved grade** – if MFDS grading table yields a different grade than 3등급 for the software component. | Escalate to senior RA & request formal MFDS pre‑submission consultation. |
| **Missing KGMP certification** – manufacturer has not yet obtained KGMP. | Halt submission preparation; initiate on‑site audit or sponsor KGMP application before any filing. |
| **Network‑enabled detector firmware** confirmed without a documented cybersecurity plan. | Immediate escalation to the Cybersecurity Lead; develop SBOM and mitigation plan per 고시 제16조. |
| **Clinical evidence gap** – no local data and foreign CER cannot be mapped. | Pause submission; engage Clinical Affairs for a bridging study or seek MFDS exemption review. |
| **Labeling not in Korean** after draft completion. | Stop filing; involve translation & regulatory writing team to produce compliant labeling. |
| **SBOM format mismatch** – supplied SBOM does not conform to SPDX 2.3 nor CycloneDX 1.5. | Return to development team for remapping; reference MFDS recommendation (see source). |

---

### 7. Regulatory Judgment  

- The X‑ray acquisition workstation and AI post‑processing module are **subject to the Digital Medical Products Act** and, based on Korean risk classification, qualify as a **3등급 medical device**, requiring an **MFDS 허가** submission.  
- The detector firmware is *conditionally* subject; if networked it will be a **2등급** product submitted via **인증**.  
- The generator firmware remains a **1등급** item (신고).  

All required evidence items are identified above; the highlighted missing pieces must be resolved before dossier finalisation.  

**Escalation points** are enumerated in Section 6 and should trigger human review whenever any condition is met.

---

### 8. Peer‑Review Prompt  

> **@RA‑Peer:** Please evaluate the assumptions made about (1) the grade assignment for the AI‑enabled software, (2) the completeness of the SBOM requirement based on the source excerpt, and (3) any jurisdictional gaps concerning the Digital Medical Products Act versus MFDS medical‑device classification. Are there additional Korean regulatory instruments (e.g., specific 고시 numbers) that we should cite or verify? Let us know if further source coverage is needed.

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

>

**Source Excerpts**

1. Chunk `1055466385786976527`

> ## 1. FDA vs MDR vs MFDS — SBOM 요구사항 정합성 | 축 | 요구 시점 | 포맷 | 필수 항목 | 제출 방식 | 사후 갱신 | |----|-----------|------|-----------|-----------|-----------| | FDA (524B) | Premarket (2023-10-01 RTA 강제) | SPDX 2.3 / CycloneDX 1.5 | NTIA 7요소 + EOL + 취약점 | eSTAR 제출물 | Section 524B Postmarket Plan | | MDR (MDCG 2019-16) | Technical Documentation Annex II | 포맷 권고 없음, IMDRF N73 원칙 | NTIA 7요소 + License + Hash | NB 심사 자료 | PMS Plan/PSUR 포함 | | MFDS (2025-01-10) | 국내 허가 심사 | 권고 (SPDX/CycloneDX) | RA-07 항목 | 심사 자료 (권고) | 보안 지침 제16조 SBOM 관리 | **정합성 판정: 본 SOP-SBOM-001 v0.1은 3축 모두 수용 가능한 상위 호환 설계** - SPDX 2.3 또는 CycloneDX 1.5 채택 → FDA/MDR/MFDS 동시 만족 - NTIA Baseli...

2. Chunk `418096885713027360`

> ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 |

### kb-eval-20261029-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "54eea60f4d20bed6", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `54eea60f4d20bed6`
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

> **Regulatory Draft – Digital Medical Device Act Impact on AI‑Based SaMD (AI 영상분석 모듈)**  

---

### 1. Korean Classification & Submission Route  
| Item | Korean regulatory position* |
|------|------------------------------|
| **Device grade** | Likely **4등급** (high‑risk) – AI‑based diagnostic imaging analysis is treated as a “인공 지능 기반 의료기기” and, per the MFDS ‘디지털의료제품법’, devices that directly influence clinical decision‑making fall into 4등급. |
| **Submission track** | **허가** (MFDS approval) – required for all 3등급·4등급 devices. |
| **Required regulatory body** | MFDS (Ministry of Food and Drug Safety) with KGMP‑certified manufacturing site. |

\*The precise grade must be confirmed against the current “의료기기 품목 및 품목별 등급에 관한 규정” (MFDS_인허가_상세가이드.md §2).  

---

### 2. Core Evidence Required for 허가 Submission  

| Evidence | Korean requirement | Typical international counterpart | Citation (framework) |
|----------|-------------------|----------------------------------|----------------------|
| **KGMP facility certification** | 제조시설은 KGMP(의료기기법 제28조) 적합성 인정 받아야 함. | ISO 13485:2016‑based QMS, but MFDS‑specific KGMP. | ISO 13485 2016 (framework); no instance identifier in source. |
| **Technical Documentation** | 제품설명서·구성요소 목록·알고리즘 설명서 등. | FDA 510(k) technical file; EU MDR Annex II/III. | IEC 62304 2006+A1:2015 (software life‑cycle), IEC 62366‑1 2015+A1:2020 (사용적합성). |
| **Risk Management File** | ISO 14971 2019에 따라 위험 관리 계획·평가·통제 기록. | Same as FDA/EU requirement. | ISO 14971 2019 (framework). |
| **Clinical Evaluation Report (CER)** | 임상시험 또는 외국 CER(허가받은 경우) 제출 여부는 MFDS 고시에서 정의. If foreign evidence is used, it must be accepted under the latest “외국 임상평가보고서 인정” notice. | FDA 510(k) clinical data; EU MDR Clinical Evaluation. | No specific notice number found in source – verify separately. |
| **Cybersecurity Evidence** | ‘의료기기 사이버보안 허가·심사 가이드라인(2025‑01‑10)’ 적용, 네트워크 연결 전체 대상. Must provide RA‑01~RA‑20 매트릭스, SBOM, 보안 설계 검증 보고서. | FDA 21 CFR 820.30(b) + NIST CSF; EU MDR Annex I cyber security. | No specific identifier found in source – verify separately. |
| **Software Bill of Materials (SBOM)** | ‘디지털의료기기 전자적 침해행위 보안 지침(2025‑01)’ 요구, SBOM 관리 포함. | NIST SBOM guidance; EU IEC 62304 addendum. | No specific identifier found in source – verify separately. |
| **AI Model Governance** | 데이터셋·거버넌스 SOP (SOP‑AIDATA‑001 / SOP‑AIGOV‑001) 제출, 알고리즘 변경 관리 계획 포함. | FDA Artificial Intelligence/Machine Learning Software Action Plan; EU AI Act draft. | No specific identifier found in source – verify separately. |
| **Usability Engineering** | IEC 62366‑1 사용적합성 엔지니어링 계획서 (v0.2 완료). | Same as FDA/ISO usability. | IEC 62366‑1 2015+A1:2020 (framework). |
| **Labeling & IFU** | 모든 라벨·사용설명서는 한국어로 제공, MFDS ‘라벨·표시·포장 규정’ 준수. | FDA 21 CFR 801; EU MDR Annex II. | No specific identifier found in source – verify separately. |

---

### 3. Missing Information (Gap Analysis)

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Exact intended use & indication** | Determines grade and clinical evidence scope. | Draft a clear Intended Use Statement in Korean; map to risk class. |
| **Classification justification** | Required in 허가 dossier (risk‑based grading). | Prepare a classification matrix referencing MFDS ‘디지털의료제품법’ risk categories. |
| **Local clinical data requirement** | If foreign CER not accepted, Korean‐subject data are mandatory. | Plan a pilot/registrational study in Korea or verify exemption under latest notice. |
| **Full KHMP certification status** | KGMP must be granted before MFDS 허가 review. | Confirm current KGMP audit report; schedule if pending. |
| **Cybersecurity validation reports** | The 2025‑01‑10 guide demands documented testing of threat detection, patch management, etc. | Complete RA‑01~RA‑20 matrix and penetration test results. |
| **SBOM completeness** | Required for all network‑connected devices per 2025 security guidance. | Generate SBOM covering all third‑party components; align with SOP‑SBOM‑001. |
| **Change Management (CMP) linkage** | MFDS expects a documented change control plan linked to the CMP section. | Finalize SOP‑CC‑001 and reference it in the submission. |
| **Performance evaluation of AI sub‑components** | Required per “구성요소 단위 성능평가 절차 문서화”. | Provide separate validation reports for each AI module (e.g., preprocessing, inference). |

---

### 4. Risk Controls & Mitigation Measures  

| Control Area | Specific Measure (Korean context) |
|--------------|-----------------------------------|
| **Risk Management** | ISO 14971‑based FMEA/FMECA; residual risk acceptance criteria documented per MFDS ‘위험관리 지침’. |
| **Cybersecurity** | Implement RA‑01~RA‑20 matrix, continuous vulnerability scanning, secure boot, encryption of data in transit/storage, SBOM tracking. |
| **Software Lifecycle** | IEC 62304 compliant development phases; version control and traceability to requirements. |
| **AI Governance** | SOP‑AIDATA‑001 (데이터셋 관리) + SOP‑AIGOV‑001 (알고리즘 변경 승인); bias/ fairness assessment, explainability documentation. |
| **Usability** | IEC 62366‑1 기반 사용성 테스트 with Korean end‑users; ergonomic labeling, error‑prevention UI design. |
| **Post‑Market Surveillance** | MFDS ‘시판후조사’ plan: PMS 체계, 정기적인 위험 재평가, 보고서 제출 일정. |
| **Change Management** | SOP‑CC‑001 covering software updates, security patches, and regulatory impact assessment before release. |

---

### 5. Human‑Escalation Triggers  

| Trigger | Required human action |
|---------|------------------------|
| **Unclear device grade (2등급 vs 4등급)** | Escalate to senior RA for classification confirmation against the latest “디지털의료제품법” grading table. |
| **Foreign CER not accepted by MFDS** | Pause submission; engage clinical affairs to design a Korean‑subject study or seek exemption documentation. |
| **KGMP certification pending at submission deadline** | Trigger manufacturing compliance team to fast‑track audit, report status to project lead. |
| **Cybersecurity gaps identified in RA‑01~RA‑20 matrix** | Convene cybersecurity lead to remediate before dossier finalization. |
| **Adverse event signals exceeding risk acceptance** | Activate PMS/Clinical Safety committee; prepare a Field Action Notification per MFDS ‘시판후조사’ rules. |
| **Regulatory guidance updates (e.g., new 2025‑01‑10 cyber guide amendment)** | Pause final review; incorporate changes and re‑validate SBOM/SOPs. |

---

### 6. Citations  

**Framework references (no specific identifier required):**  
- ISO 14971 2019 – Risk Management for Medical Devices.  
- IEC 62304 2006+A1:2015 – Software Life Cycle Processes.  
- IEC 62366‑1 2015+A1:2020 – Usability Engineering.  
- MFDS ‘디지털의료제품법’ (Digital Medical Device Act) – overall legal basis for classification and 허가 pathway.

**Instance identifiers:**  
- No specific MFDS 고시/notice number, device clearance number, or article/section citation appears in the provided source excerpts. → *no specific identifier found in source — verify separately*.

---

### 7. Peer‑Review Prompt  

> **To RA colleagues:** Please examine the assumptions made regarding the 4등급 classification of this AI imaging analysis module and the reliance on foreign clinical evaluation reports. Verify whether any recent MFDS notice (2025 or later) expands acceptance of such foreign CERs for devices in this risk category, and confirm that the cyber‑security matrix (RA‑01~RA‑20) aligns with the latest “의료기기 사이버보안 허가·심사 가이드라인(2025‑01‑10)”. Highlight any missing Korean‑specific clinical data requirements or additional documentation not captured above.

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

### kb-eval-20261029-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "2014def7d2629c34", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2014def7d2629c34`
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

> **Regulatory Draft – Independent Imaging‑Room GUI Software (SaMD)**  

---

### 1. Korean Grade & Submission Route  
| Korean grade* | Likely regulatory path |
|---------------|------------------------|
| **1등급** → 신고 (notification) | Only for very low‑risk devices (e.g., simple data display). Unlikely for a GUI that controls imaging equipment. |
| **2등급** → 인증 (certification by MFDS‑designated 심사기관) | If the software is considered “general‐purpose” and does not directly affect patient safety. |
| **3등급·4등급** → 허가 (approval by MFDS) | Most SaMD that performs image acquisition, processing, or decision support are placed in 3‑ or 4‑등급 under the 디지털의료제품법. |

\*The exact grade must be verified against **「의료기기 품목 및 품목별 등급에 관한 규정」** (MFDS_인허가_상세가이드.md §2).  

**Current knowledge gap:** The source does not state the official Korean grade for this GUI; a senior RA should confirm the grade before finalising the submission track.

---

### 2. Core Evidence Required  

| Requirement | Korean regulatory basis (framework) | Source‑derived citation (instance identifier) |
|-------------|--------------------------------------|----------------------------------------------|
| **KGMP facility certification** | KGMP (의료기기법 제28조) – mandatory for any 제조·품질관리 system supporting a 허가/인증 | *no specific identifier found in source — verify separately* |
| **QMS compliance** | ISO 13485:2016 + MFDS ARR integration (ARR = Applicable Regulatory Requirements) | FDA 21 CFR §820.10(b) – ARR must be integrated into QMS procedures【1†L2-L4】 |
| **Software development life‑cycle documentation** (SDP, SRS, SAD, SVP, SVR) | IEC 62304:2006+A1:2015 Safety Class C; 디지털의료제품법 연계 | IEC 62304 §8.1 – required for SW validation【2†L7-L9】 |
| **Risk Management** | ISO 14971:2019 (risk analysis, risk control) | *no specific identifier found in source — verify separately* |
| **Cyber‑security dossier** (Threat Model, SBOM, PCCP) | MFDS 사이버보안 가이드라인 2025; FDA 524B PCCP; MDCG 2019‑16 Rev.1 | MFDS 사이버보안 가이드라인 2025 (named in source)【2†L11-L13】 |
| **AI/ML algorithm governance** (if applicable) | 디지털의료제품법 + FDA PCCP (2024‑12‑03 Final) + EU AI Act Art.43(4) | FDA PCCP (2024‑12‑03 Final) – cited in source【2†L15-L17】 |
| **UDI & post‑market reporting** | 21 CFR §820.35(a) for MDR‑reportable events; Korean MFDS 보고 규정 | FDA 21 CFR §820.35(a) – required complaint handling record【1†L5-L7】 |
| **Clinical evaluation / local clinical data** | 디지털의료제품법 & MFDS Clinical Evaluation Guidelines (if grade 3‑4) | *no specific identifier found in source — verify separately* |
| **Labeling & IFU** | Korean language labeling, safety information per MFDS 고시 (e.g., “의료기기 포장·라벨링에 관한 고시”) | *no specific identifier found in source — verify separately* |

---

### 3. Identified Missing Information  

| Item | Why it is needed | Action |
|------|------------------|--------|
| **Official Korean grade (1‑4등급)** | Determines submission track and depth of clinical evidence required. | Request confirmation from product manager / senior RA; consult the latest “품목별 등급에 관한 규정”. |
| **KGMP certificate for the development/production site** | Mandatory for any 허가 or 인증 submission. | Obtain KGMP audit report or schedule certification. |
| **Local (Korean) clinical evaluation data** (if grade 3‑4) | MFDS typically requires Korean patient data unless a specific exemption is granted via OECD MAD acceptance (non‑clinical only). | Plan a short‑term local feasibility study or request an exemption justification. |
| **Full Korean‑language labeling & IFU package** | All marketed devices must have Korean language labeling; the source does not address this. | Draft Korean label/IFU and submit for translation review. |
| **Evidence of compliance with MFDS ARR (ARR integration in QMS)** | The source notes that ISO 13485 alone is insufficient and ARR activities must be embedded【1†L2-L4】. | Update QMS SOPs to capture UDI, MDR‑reportable event assessment, correction & removal processes. |
| **Cyber‑security implementation evidence** (Threat Model, SBOM) | Required by MFDS 사이버보안 가이드라인 2025【2†L11-L13】. | Produce threat model and software bill of materials; align with PCCP methodology. |

---

### 4. Core Risk Controls to be Demonstrated  

| Control Area | Standard / Guidance | Practical Implementation |
|--------------|---------------------|--------------------------|
| **Software hazard analysis & risk control** | IEC 62304 Class C (Safety‑critical) + ISO 14971 | Perform FMEA/FTA at each development stage; verify residual risk is acceptable. |
| **Change management & regression testing** | IEC 62304 §8.1 & MFDS ARR (ARR integration) | Automated regression suite, documented change‑impact analysis, SOP for version control. |
| **Cyber‑security safeguards** | MFDS 사이버보안 가이드라인 2025; FDA 524B PCCP | Threat modelling, SBOM, regular penetration testing, incident response plan. |
| **AI/ML model governance (if used)** | 디지털의료제품법 + FDA PCCP + EU AI Act Art.43(4) | Pre‑market algorithm validation, post‑market performance monitoring, documented “locked” vs “adaptive” status. |
| **Complaint handling & MDR reporting** | 21 CFR §820.35(a) – record MDR‐reportable assessment【1†L5-L7】 | SOP to triage complaints, determine reportability, and submit to MFDS within 30 days. |
| **UDI assignment & traceability** | 21 CFR §830 (UDI) (ARR requirement) | Assign UDI per GUDID schema; integrate into product labeling and QMS records. |

---

### 5. Human‑Escalation Triggers  

| Trigger | Reason for Escalation | Who to Notify |
|---------|-----------------------|---------------|
| **Uncertain Korean grade** (no clear 1‑4등급) | Determines submission pathway & evidence set | Senior RA / Regulatory Affairs Manager |
| **Missing KGMP certification** | Submission cannot proceed without facility approval | Quality Management Lead & external KGMP auditor |
| **Absence of local clinical data when required** | MFDS may reject or request additional studies | Clinical Development Team & Project Sponsor |
| **ARR integration gaps in QMS** (e.g., no UDI procedure) | Non‑compliance with ARR (FDA 21 CFR §820.10(b)) leads to audit findings【1†L2-L4】 | QMS Owner / Compliance Officer |
| **Cyber‑security dossier incomplete** (no threat model/SBOM) | Violates MFDS 사이버보안 가이드라인 2025【2†L11-L13】 | IT Security Lead & Regulatory Project Manager |
| **AI/ML algorithm change without documented assessment** | May breach 디지털의료제품법 & FDA PCCP requirements | AI/ML Governance Board |
| **Late Korean labeling draft** (post‑submission) | MFDS requires Korean label at filing; delays approval | Labeling Team Lead |

Escalations should be recorded in the project risk register and trigger a pause on submission preparation until resolved.

---

### 6. Reusable RA Judgment (Lesson Learned)

- **Always verify the Korean grade (1–4등급) against the official “품목별 등급에 관한 규정” before selecting the submission track.**  
- **ARR integration is mandatory for any MFDS filing; ISO 13485 alone does not satisfy ARR‑related obligations (e.g., UDI, MDR reporting).** (Source: FDA 21 CFR §820.10(b))  
- **For SaMD classified as IEC 62304 Class C, the full suite of software development documents (SDP, SRS, SAD, SVP, SVR) is required under both KGMP and 디지털의료제품법.**  
- **MFDS 사이버보안 가이드라인 2025 explicitly demands a threat model and SBOM; align these with FDA 524B PCCP to satisfy dual‑market expectations.**  
- **When foreign clinical evidence is used, remember that OECD MAD only covers non‑clinical GLP data – Korean clinical data may still be required for grades 3‑4.**  

---

### 7. Peer Review Prompt  

*“Please review this draft and challenge the following assumptions: (1) the inferred 3/4등급 classification for the imaging‑room GUI; (2) that ARR integration alone satisfies all MFDS reporting obligations without additional local SOPs; (3) completeness of the cyber‑security evidence based solely on the cited MFDS guide; and (4) any jurisdiction‑specific gaps not covered by the source excerpts.”*

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

>

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261029-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "d004e15b9d1a1fdc", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md", "source_hash": "eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `d004e15b9d1a1fdc`
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

> **Regulatory Draft – Digital Medical Product (디지털 의료기기) 2026‑10‑29**

---

### 1. Device Classification & Submission Route  
| Item | Korean regulation | Likely grade* | Required MFDS track |
|------|-------------------|--------------|---------------------|
| 디지털 의료제품법 적용 제품 | 「의료기기법」 및 「디지털 의료제품법」 (MFDS 고시) | **2등급 or 3/4등급** – the exact grade depends on functional risk (e.g., AI‑ 기반 진단, 자동 치료 등). | • 1등급 → 신고  <br>• **2등급 → 인증**  (MFDS‑지정 심사기관)  <br>• 3·4등급 → 허가 |  

\*No specific grade is given in the source excerpts. **no specific identifier found in source — verify separately** by consulting 「의료기기 품목 및 품목별 등급에 관한 규정」.

---

### 2. Mandatory Submission Evidence (Korean‑specific)

| Requirement | Korean regulatory basis (framework) | Typical evidence artefact |
|-------------|--------------------------------------|---------------------------|
| **Risk Management** | ISO 14971 : 2019 (full coverage noted in DR‑21) | Risk Management Plan & Report (ISO 14971 프로세스 상세 – issue 007) |
| **Software Life‑Cycle Documentation** | IEC 62304 : 2006+A1:2015 (covered in DR‑22) | Software Development Plan, Verification/Validation Protocols, Release Notes |
| **Usability / Human Factors** | IEC 62366‑1 : 2015+A1:2020 (template missing – DR‑06) | Usability Engineering File, IEC 62366‑1 사용적합성 계획서 |
| **Cybersecurity** | MFDS 보안지침 제16조 (aligned with FDA §524B) – cited in DR‑09 | Cybersecurity Risk Assessment, Incident Response SOP |
| **UDI Assignment** | 의료기기법 + 디지털의료제품법 (DR‑19) | UDI Allocation Plan, Label & IFU containing UDI |
| **Clinical Evaluation** | MFDS 고시 (clinical evaluation) – foreign CER may be accepted if OECD MAD applies to non‑clinical data only. | Clinical Evaluation Report; if using foreign data, verify acceptance per latest MFDS notice (no specific identifier in source). |
| **Labeling & IFU (Korean language)** | 의료기기법 제38조 등 (Korean labeling mandatory) – DR‑10 indicates template missing. | Korean labeling and Instructions for Use (IFU) templates. |
| **GMP / KGMP Compliance** | 의료기기법 제28조 (KGMP) – partial draft GMP suitability application noted (DR‑02). | KGMP Certificate, GMP suitability assessment dossier. |
| **Post‑Market Surveillance (PMS)** | PMS 고시 (제2025‑22호 등) – DR‑14 aligns reporting deadlines. | PMS Plan, Periodic Safety Update Report (PSUR) style Korean PMS report. |
| **Data Integrity** | ALCOA+ principles (no SOP – DR‑31). | Data Management SOP covering ALCOA+. |
| **AI Explainability / Fairness** | No specific Korean rule yet; MFDS drafts recommend AI 설명성·공정성 평가 (DR‑32/33). | AI Explainability Report, Bias Assessment. |
| **Autonomous Performance Certification** | Autonomous devices require 별도 인증 Playbook (DR‑15). | Autonomy Certification Playbook & supporting test data. |
| **Drift / Post‑Learning Governance** | No SOP – DR‑35. | Governance framework for model updates, drift detection, re‑validation procedures. |

*All items marked “covered” in the source refer to internal SOP/Issue documents (e.g., issue 002, issue 006). Those documents are assumed to satisfy the respective regulatory requirement but should be cross‑checked against the latest MFDS guidelines.

---

### 3. Identified Gaps & Priorities  

| Gap ID | Description (source) | Priority* | Impact if unaddressed |
|--------|----------------------|----------|-----------------------|
| **DR‑05** | 구성요소 성능평가 SOP 부재 | P0 | Non‑compliance with performance verification; may block GMP/KGMP assessment. |
| **DR‑10** | 디지털의료기기 표시기재 템플릿 미작성 | P1 | Korean labeling non‑conformity → market entry refusal. |
| **DR‑11** | 독립형 SW 사용적합성 평가 절차 부재 | P1 | Software safety claim unsupported; risk management gaps. |
| **DR‑15** | 자율성능인증 신청 플레이북 부재 | P0 | Autonomous device cannot obtain 허가; regulatory hold. |
| **DR‑31** | 데이터 무결성(ALCOA+) SOP 부재 | P1 | Data reliability issues for clinical/evidence data; audit finding. |
| **DR‑32/33** | AI 설명성·공정성 평가 문서 없음 | P1 | MFDS may reject AI‑based device without explainability evidence. |
| **DR‑35** | 사후학습·드리프트 거버넌스 없음 | P0 | Continuous learning models violate post‑market controls → 허가 취소 risk. |
| **DR‑02 (partial)** | GMP 적합판정 신청서 초안 미작성 | P1 | KGMP 인증 절차 지연; cannot start 제조. |
| **DR‑04 (partial)** | PCCP 결정트리 미확정 | P1 | Clinical performance claim unclear; may affect 허가 심사. |
| **DR‑06 (partial)** | IEC 62366‑1 사용적합성 계획서 템플릿 미정 | P1 | Usability engineering evidence incomplete. |

\*Priority codes: **P0** = critical blocker, **P1** = high importance but not immediate show‑stop.

---

### 4. Risk Control Measures (to be documented)

| Control | Source basis | Implementation note |
|---------|--------------|----------------------|
| **Risk Management Process** – ISO 14971 (DR‑21) | ISO 14971 : 2019 | Maintain risk register, evaluate residual risks, verify mitigation. |
| **Software Lifecycle Controls** – IEC 62304 (DR‑22) | IEC 62304 : 2006+A1:2015 | Version control, configuration management, validation of each software release. |
| **Usability Engineering** – IEC 62366‑1 (missing template DR‑06) | IEC 62366‑1 : 2020 | Develop usability plan; fill missing template before submission. |
| **Cybersecurity Safeguards** – MFDS 보안지침 제16조 (DR‑09) | MFDS 보안지침 제16조 | Perform threat modeling, patch management, incident response SOP. |
| **UDI Traceability** – 의료기기법 + 디지털의료제품법 (DR‑19) | 국내 법령 | Embed UDI on labeling and device database; ensure unique identification in RM system. |
| **Post‑Learning Governance** – internal governance (gap DR‑35) | MFDS guidance on AI/ML (no specific identifier) | Establish model monitoring, drift detection thresholds, re‑validation workflow. |
| **Data Integrity SOP** – ALCOA+ (DR‑31) | Good Clinical Practice principle | Enforce data entry, audit trails, backup procedures. |
| **AI Explainability & Fairness** – MFDS AI recommendation (DR‑32/33) | MFDS draft guidance on AI (2025‑??) | Produce explainability report, bias mitigation documentation. |
| **Autonomous Performance Certification Playbook** – (DR‑15) | Internal playbook required | Define test scenarios, safety envelope, certification checklist. |

All controls should be cross‑referenced to the relevant Korean regulation or MFDS notice; where a specific notice number is not given in the source, note “no specific identifier found in source — verify separately”.

---

### 5. Human‑Escalation Triggers  

| Trigger | When to Escalate | Who to Notify |
|---------|------------------|--------------|
| **P0 gaps (DR‑05, DR‑15, DR‑35)** remain unresolved > 7 business days after remediation plan issuance | Immediate regulatory hold risk; potential MFDS refusal. | Regulatory Lead → Project Manager → Senior Management. |
| **Partial gaps (DR‑02, DR‑04) not closed before KGMP audit** | KGMP certification cannot be obtained. | Quality Assurance Head & KGMP Coordinator. |
| **New foreign clinical evidence is proposed without OECD MAD confirmation** | Risk of MFDS rejection if non‑clinical data are not mutually accepted. | Clinical Affairs Lead → Legal Counsel. |
| **AI model update scheduled without drift governance SOP (DR‑35)** | Post‑market surveillance breach; may invoke enforcement action. | AI/ML Technical Lead → Regulatory Lead. |
| **Labeling template still missing after 5 days of deadline** | Korean labeling non‑compliance—product cannot be marketed. | Marketing/Regulatory Communication Officer. |

Escalation should be documented in the project risk register and tracked via the RA ticketing system.

---

### 6. Summary Judgment  

* The device is likely **2등급** (or higher) under the Korean Medical Device Act; the exact grade must be confirmed by consulting the official grading table (**no specific identifier found in source — verify separately**).  
* All core Korean regulatory artefacts (risk management, software lifecycle, UDI, labeling, KGMP compliance) are **partially covered** by internal SOPs, but several critical gaps (performance‑evaluation SOP, autonomy certification playbook, post‑learning governance, data integrity SOP, AI explainability documents) remain.  
* Immediate remedial actions should prioritize the P0 items (DR‑05, DR‑15, DR‑35) and ensure that missing templates (DR‑06, DR‑10) are completed before dossier submission.  

If any of these high‑priority gaps persist beyond the stated timelines, a formal escalation to senior regulatory leadership is required.

---

### 7. Peer Review Prompt  

> *“@RA‑Peer – Please review the assumptions regarding device grade, the completeness of foreign clinical evidence acceptance (OECD MAD vs. CER), and any jurisdiction‑specific obligations that may not be captured in the current gap list (e.g., biocompatibility testing per ISO 10993‑1, environmental safety standards). Are there additional Korean notices or recent MFDS 고시 that affect AI/ML governance beyond what is cited here?”*

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

> "PMS 고시 (제2025-22호 등)" — 본 케이스 소스에는 고시 번호 없음(원문은 'PMS 고시'만 언급). KB 내 2025-22호는 제조·품질관리(품목군 개정) 고시로 다른 문서에 부착되어 있어 번호 오귀속 의심. 번호 삭제 또는 원문 확인 후 기재.

**Source Excerpts**

1. Chunk `1091162552456558927`

> ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버

2. Chunk `434223568197517474`

> ### 3.2 불일치·공백 항목 | Req-ID | 불일치 유형 | 내용 | 우선도 | |---|---|---|---| | DR-05 | 공백 | 구성요소 성능평가 SOP 부재 | P0 | | DR-10 | 공백 | 디지털의료기기 표시기재 템플릿 미작성 | P1 | | DR-11 | 공백 | 독립형 SW 사용적합성 평가 절차 부재 | P1 | | DR-15 | 공백 | 자율성능인증 신청 플레이북 부재 | P0 | | DR-31 | 공백 | 데이터 무결성(ALCOA+) SOP 부재 | P1 | | DR-32/33 | 공백 | AI 설명성·공정성 평가 문서 없음 | P1 | | DR-35 | 공백 | 사후학습·드리프트 거버넌스 없음 | P0 | | DR-02 | 부분 | GMP 적합판정 신청서 초안 미작성 | P1 | | DR-04 | 부분 | PCCP 결정트리 미확정 | P1 | | DR-06 | 부분 | IEC 62366-1 사용적합성 계획서 템플릿 미정 | P1 |

### kb-eval-20261029-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-29", "decision_ref": "kb-eval-20261029-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "282e340c8f14f06d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `282e340c8f14f06d`
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

> **Regulatory Draft – Impact of the 2025 MFDS Cyber‑Security Guideline on a Digital Medical Product (SaMD)**  

---

### 1. Device Classification & Submission Route  
| Item | Assessment | Rationale / Source |
|------|------------|--------------------|
| **Korean grade** | **1~4등급 – to be confirmed** | The guide does not state the device’s risk‑grade. Korean grade must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS_인허가_상세가이드.md §2). |
| **Likely pathway** (if Grade 3·4) | **허가** – MFDA approval by the Ministry of Food and Drug Safety (MFDS) | Grades 3·4 are routed to 허가 per Korean regulation. |
| **If Grade 2** | **인증** – technical‑documentation review by an MFDS‑designated 심사기관 (e.g., KTL, KTC) | Default track for 2등급 is 인증; only exempt items go to 허가. |
| **If Grade 1** | **신고** – simple notification | 1등급 devices use 신고. |

> **Action:** Obtain the device’s intended‑use description and functional risk analysis to determine the exact Korean grade.  

---

### 2. Required Evidentiary Package (per the 2025 cyber‑security guideline)  

| Evidence Item | Description | Mapping to Guideline / Standards |
|---------------|-------------|-----------------------------------|
| **Cyber‑Security Risk Management Plan** (RA‑01 ~ RA‑35) | Documented process covering threat identification, risk evaluation, mitigation and residual‑risk acceptance. | Derived from the 35 RA items listed under eight categories in the guideline (see excerpt 2). |
| **Secure‑by‑Design Specification** | Architecture diagrams showing defense‑in‑depth, least‑privilege controls; justification of security design choices. | *보안 설계 원칙* category – Secure by design, Defense‑in‑depth, Least privilege. |
| **Authentication & Access‑Control Mechanisms** | Evidence of user authentication (e.g., PKI, MFA), role‑based access control matrices, session‑timeout settings. | *인증·접근 제어* category. |
| **Encryption Implementation Report** | Details of data‑at‑rest and data‑in‑transit encryption algorithms, key‑management procedures, cryptographic module validation (KCM). | *암호화* category. |
| **Software Integrity Controls** | Code‑signing certificates, boot‑integrity verification logs, Software Bill of Materials (SBOM) maintained per IEC 81001‑5‑1. | *소프트웨어 무결성* category; aligns with IEC 81001‑5‑1 (2021). |
| **Network Security Architecture** | Network segmentation diagrams, firewall rule sets, TLS version policy (minimum TLS 1.2), port‑minimisation checklist. | *네트워크 보안* category. |
| **Vulnerability Management Process** | CVE monitoring schedule, patch‑release cadence, CVD (Common Vulnerability Disclosure) policy document, evidence of recent patches applied. | *취약점 관리* category. |
| **Audit & Logging Framework** | Security event log schema, log protection mechanisms (tamper‑evidence), retention period, sample audit logs. | *감사·로그* category. |
| **Secure Update Mechanism** | Signed OTA update process, authentication of remote management sessions, rollback safety design. | *업데이트·유지보수* category. |
| **Incident‑Response Plan** | Roles/responsibilities, escalation matrix, reporting timeline to MFDS (within 24 h of a security incident). | Implicit in overall RA requirement set; referenced by IMDRF N73. |
| **Compliance with International Standards** | Declaration of conformity to IEC 62304 (2006+A1:2015), ISO 14971 (2019), and IEC 81001‑5‑1 (2021) as supporting evidence for “조화 목적”. | Guideline states alignment with IMDRF N60/N73, IEC 81001‑5‑1. |
| **KGMP Certification (if applicable)** | Facility certification under KGMP (의료기기법 제28조). Required for any manufacturing site in Korea. | Korean GMP requirement – not directly listed in the excerpt but mandatory by law. |
| **Korean‑language Labeling & IFU** | Labels, user manuals, and cybersecurity information (e.g., update instructions) provided in Korean per MFDS labeling rules. | General MFDS labeling regulation; not itemized in the cyber‑security guide. |

> **Citation note:** The 35 RA items (RA‑01 ~ RA‑35) are referenced from the guideline PDF; the source excerpt does not provide a numeric identifier beyond “RA‑01~RA‑35”. Hence: *no specific identifier found in source — verify separately* for each individual requirement number.

---

### 3. Gaps / Missing Information  

| Gap | Why it matters | Recommended action |
|-----|----------------|--------------------|
| **Exact Korean grade (1–4등급)** | Determines the submission track and documentation depth. | Conduct a risk classification per 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **Device Intended Use & Indications** | Needed for both grading and justification of security controls relative to clinical function. | Provide a clear intended‑use statement (including patient population, environment of use). |
| **Foreign Regulatory Evidence Mapping** | The guideline aligns with IMDRF N60/N73; if the device already has FDA 510(k) or CE Mark, map foreign cyber‑security evidence to Korean RA items. | Identify which foreign security documentation can be cross‑referenced (e.g., FDA’s 524B pre‑market cybersecurity framework). |
| **KGMP Facility Status** | Manufacturing sites must hold KGMP certification before 허가/인증 submission. | Verify and obtain KGMP certificate for all production locations. |
| **Korean‑language Documentation** | Mandatory labeling, IFU and cybersecurity notices; missing translations cause rejection. | Translate all user‑facing documents into Korean, include security update instructions. |
| **Specific MFDS 고시/공고 번호** | The guideline itself does not list a 고시 number (e.g., “MFDS 고시 제2025‑XX호”). Without the identifier, downstream references may be ambiguous. | Retrieve the official notice number from MFDS portal; amend submission accordingly. |
| **Evidence of Ongoing Vulnerability Monitoring** | Continuous CVE tracking is now an explicit requirement; historic data alone insufficient. | Establish a process (e.g., subscription to NIST NVD) and provide the first 3 months of monitoring logs. |

---

### 4. Key Risk Controls (derived from the eight categories)

| Category | Primary Control(s) | Supporting Documentation |
|----------|-------------------|---------------------------|
| **보안 설계 원칙** | Threat modeling (STRIDE), security architecture review, design reviews with security experts. | Threat‑model diagram, design‑review minutes. |
| **인증·접근 제어** | Multi‑factor authentication for privileged users; RBAC matrix; session timeout ≤ 15 min. | Access‑control policy, audit of user accounts. |
| **암호화** | AES‑256 data‑at‑rest; TLS 1.2+ for all communications; HSM for key storage. | Encryption algorithm validation report, key‑management SOP. |
| **소프트웨어 무결성** | Code signing with SHA‑256; Secure boot verification; SBOM stored in immutable repository. | Code‑signing certificate, SBOM export file. |
| **네트워크 보안** | Minimal open ports (only required APIs); firewall rules logged; TLS 1.2+ enforced. | Network diagram, firewall rule set snapshot. |
| **취약점 관리** | Quarterly CVE scan; patch release within 30 days of critical vulnerability disclosure. | Vulnerability‑scan reports, patch‑release schedule. |
| **감사·로그** | Centralized syslog server with tamper‑evidence; log retention ≥ 12 months. | Log‑management policy, sample log files. |
| **업데이트·유지보수** | Signed OTA update packages; rollback capability; remote update sessions authenticated via mutual TLS. | Update‑process flowchart, test report of secure update mechanism. |

---

### 5. Human‑Escalation Triggers  

| Trigger Condition | Why escalation is needed | Who should be alerted |
|-------------------|--------------------------|-----------------------|
| **Unclear Korean grade** after risk classification attempt | Determines submission pathway; mis‑classification leads to regulatory rejection. | RA Lead → MFDS liaison officer. |
| **Missing KGMP certificate for any manufacturing site** | KGMP is a prerequisite for 허가/인증; without it the dossier cannot be accepted. | QA/QC Manager; executive sponsor. |
| **Failure to provide evidence for ≥ 1 of the 35 RA items (RA‑01~RA‑35)** | The 2025 guideline explicitly expands from 15→35 requirements; omission is a non‑conformity. | RA team lead → Project manager. |
> **Escalation protocol:** Document the deficiency, issue an internal “Regulatory Deficiency Notice” within 2 business days, and schedule a corrective‑action plan meeting with product development leadership.  

---

### 6. Peer‑Review Prompt  

*“@RA‑Peer, please evaluate the assumptions made above:*

1. *Is the interpretation that a SaMD subject to the 2025 cyber‑security guideline will most likely fall under Grade 3 or 4 justified without a specific intended‑use description?*  
2. *Does our mapping of the eight guideline categories onto existing Korean standards (KGMP, IEC 62304, ISO 14971) capture all mandatory evidence, or are there additional MFDS‑specific deliverables we have omitted?*  
3. *Given that the source excerpt does not provide an official 고시 number for the cyber‑security guide, how should we handle citation of the guideline in formal submissions to avoid “missing identifier” issues?*  

*Your challenges will help ensure completeness and regulatory accuracy before finalizing the dossier.*"

--- 

**Regulatory Judgment Summary**

- **Classification:** Grade 1–4등급 – requires definitive risk‑grade determination.  
- **Submission route:** 허가 (if Grade 3·4) or 인증 (if Grade 2); 신고 only for Grade 1.  
- **Core evidence:** Comprehensive package covering all 35 RA items across the eight categories, supplemented by KGMP certification, Korean‑language labeling, and alignment with IEC 62304/ISO 14971/IEC 81001‑5‑1.  
- **Key gaps:** Exact device grade, official 고시 number, KGMP status, Korean translations, continuous vulnerability‑monitoring proof.  

*Proceed to close the identified gaps; trigger escalations as soon as any of the conditions in Section 5 arise.*

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

>

**Source Excerpts**

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---
