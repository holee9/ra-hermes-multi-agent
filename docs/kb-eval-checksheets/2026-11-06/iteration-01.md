# KB Eval Checksheet - 2026-11-06 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261106-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "97a2d4d59ee46d83", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "757e3b0039fbc8900d0917e9ebdd32c0ded796618813c51039ed63b34e627e31"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `97a2d4d59ee46d83`
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

> **Regulatory Draft – QMSR Compliance & 510(k) Readiness Assessment**

---

### 1. Classification & Preferred Submission Route  
| Item | Recommendation |
|------|----------------|
| **Device class** | Determine by FDA product‑code search (most imaging, diagnostic or service‑related devices fall in **Class II**). |
| **Submission type** | **Premarket notification (510(k))** is the fastest credible route for a Class II device unless a novel technology or lack of predicate forces a **De Novo** request. |

> *Bottom line*: Identify the product code today; if a legally marketed predicate exists, prepare a traditional 510(k). If none exist, plan a De Novo submission.

---

### 2. Evidence Required for 510(k) (or De Novo) Submission  

| Category | Minimum content | Rationale / regulation |
|----------|----------------|------------------------|
| **Device description & intended use** | Clear statement of function, indications, patient population, and environment of use. | Needed for classification & predicate comparison (21 CFR 807). |
| **Predicate device(s)** | 510(k) numbers, registration numbers, and a side‑by‑side table of technological characteristics. | Establishes substantial equivalence (21 CFR 807.92). |
| **Design History File (DHF)** | Design inputs, outputs, verification/validation reports, risk analysis, change control records. | Required by 21 CFR 820 subpart D; risk‑based design controls per ISO 14971 (2019) – *framework reference only*. |
| **Risk Management File** | ISO 14971:2019 risk analysis, risk evaluation, risk control measures, residual risk assessment, and post‑market surveillance plan. | No specific identifier in source – verify separately. |
| **Labeling & IFU** | Label text, symbols, UDI placement (plain‑text & AIDC), instructions for use. | UDI labeling requirement resides in 21 CFR 801.20+; device‑specific labeling per 21 CFR 801. |
| **QMSR compliance evidence** *(see §820.35 below)* | • Records of design controls<br>• Service record forms (6 items) <br>• Complaint handling & MDR decision tree<br>• UDI issuance and GUDID submission logs | Demonstrates adherence to the FDA‑specific additions to ISO 13485 (§4.2.5). |
| **Software documentation** *(if applicable)* | Software description, architecture, verification/validation, PCCP (Predetermined Change Control Plan) if AI/ML. | Required by 21 CFR 820.30 and December 2024 FDA guidance on AI/ML. |
| **Clinical data** *(if required)* | Clinical performance study report or literature support confirming safety/effectiveness. | Needed only when substantial equivalence cannot be demonstrated solely on bench testing. |

---

### 3. Identified Gaps / Missing Information  

| Gap | Impact | Action Required |
|-----|--------|-----------------|
| **Device classification & predicate** | Cannot finalize submission pathway. | Perform FDA product‑code lookup; identify at least one cleared 510(k) predicate (e.g., K#######). |
| **Intended use statement** | Needed for labeling, risk analysis, and classification. | Draft a concise indication‑for‑use paragraph. |
| **Risk management documentation** | No source identifier provided – must be prepared de novo. | Conduct ISO 14971:2019 risk assessment; tie controls to design outputs. |
| **Design control records** (verification, validation) | Only ISO 13485 §4.2.5 satisfied; FDA demands additional §§820.35(a‑d). | Populate DHF with the extra record elements listed in §820.35 (see Section 4). |
| **UDI issuance & GUDID submission log** | Required for market entry; source only references internal SOPs. | Obtain a UDI from an accredited issuing agency, submit to GUDID, archive confirmation receipts. |
| **Service record completeness** | SOP‑SVC‑001 calls for six‑item service logs; missing data will block compliance. | Implement the service record form and train field engineers. |
| **MDR decision tree & complaint handling** | SOP‑PMS‑001 references §§803.50/803.53 triggers; not yet documented. | Map complaints to the MDR tree, ensure records capture trigger rationale. |

---

### 4. Risk Controls Related to QMSR (21 CFR 820.35)

| §820.35 Sub‑clause | Required Control | Evidence Needed |
|--------------------|------------------|-----------------|
| **(a) Documentation of design changes** | Record *what* was changed, *why*, *who approved*, and *impact on device*. | Change‑control log (design change request & approval). |
| **(b) Service record requirements** – 6 mandatory items (date, location, service performed, person performing, verification result, signature). | Completed **SOP‑SVC‑001** service form for every field maintenance event. | Sample of filled‐out service records; traceability to device serial/UDI. |
| **(c) UDI record management** | Capture issuance date, issuing agency, GUDID submission ID, and any updates. | Log per **SOP‑TRC‑001 / SOP‑UDI‑001** showing GUDID entry timestamps. |
| **(d) Complaint handling & MDR decision tree** | Document complaint source, evaluation outcome, MDR trigger (if §803.50 or §803.53 applies), and corrective action. | Completed **SOP‑PMS‑001** forms with attached MDR tree screenshots. |

> *Source citation*: The above sub‑clauses are explicitly called out in the internal SOP matrix (Chunk [2]) as “§820.35(a)(b)(c)(d) 추가요건”.  

---

### 5. Human‑Escalation Triggers  

| Trigger | Who Escalates | Action |
|---------|----------------|--------|
| **Missing or incomplete service record** (any of the six items absent) | QA/Service Engineer → RA Manager | Halt further device shipments until records are completed and audited. |
| **UDI/GUDID submission failure** (no confirmation receipt within 10 business days) | Regulatory Affairs → Senior Management | Initiate corrective action plan; consider temporary market hold. |
| **Complaint that maps to an MDR trigger (§803.50 or §803.53)** | Complaint handling team → RA Lead | Open a 510(k) supplement or voluntary correction under 21 CFR 806, as appropriate. |
| **Design change without documented §820.35(a) entry** | Design Engineer → QA Director | Suspend implementation of the change; conduct root‑cause review. |
| **Risk analysis shows residual risk > acceptable** | Risk Management Lead → RA & Clinical Team | Conduct additional verification/validation or redesign before submission. |

---

### 6. Citations  

| Requirement | Source citation |
|-------------|-----------------|
| ISO 13485:2016 incorporation by reference and basic record‑management requirement (§4.2.5) – *framework reference* | ISO 13485 §4.2.5 (no specific identifier in source). |
| FDA additional QMSR requirements beyond ISO 13485 (§820.35) – **a–d** sub‑clauses | “§820.35(a)(b)(c)(d) 추가요건” (Chunk [2]). |
| Service record SOP requirement (six items) | SOP‑SVC‑001 entry referencing **§820.35(b)** (Chunk [2]). |
| UDI record‑management SOP linking to **§820.35(c)** and 21 CFR Part 830 | SOP‑TRC‑001 / SOP‑UDI‑001 entry (Chunk [2]). |
| MDR decision‑tree triggers citing **§803.50** and **§803.53** | SOP‑PMS‑001 entry (Chunk [2]). |
| General QMSR transition date (02 Feb 2026) and ISO 13485 incorporation | “21 CFR Part 820이 2026‑02‑02부터 QMSR로 전환…ISO 13485:2016이 참조편입” (Chunk [1]). |

*All other regulatory references (e.g., 21 CFR 807, 21 CFR 801.20+, ISO 14971:2019) are framework citations and do not require source‑specific identifiers.*

---

### 7. Peer‑Review Prompt  

> **To RA peer:** Please challenge the assumptions made about classification determination without a device description, verify that the listed QMSR record elements (service log, UDI log, MDR tree) fully satisfy §820.35, and confirm whether any additional FDA‑specific documentation (e.g., Design Transfer Plan per 21 CFR 820.30) is missing for a complete 510(k) package.

--- 

*End of draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> §820.35 하위문자 오배치 — (a)를 "design changes", (d)를 complaint/MDR로 매핑했으나 KB(동일 회차 us-002 소스)는 §820.35(a)=불만 파일(구 §820.198 이관)·§820.35(c)=UDI 기록. (a)/(d) 세부 매핑은 소스에 없는 창작.

**Source Excerpts**

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `130165779856845378`

> ### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영) | SOP | 갱신 내용 | 담당 | 판정 기준 | |-----|----------|------|----------| | SOP-DOC-001 | §3에 "미국 시장 적용 시 §820.35(a)(b)(c)(d) 추가요건" 절 신설, Part 11은 §820.35 외부로 별도 절 분리 | QA | 기록관리 절차에 불만/서비스/UDI/기밀성·Part 11 분리 기재 여부 | | SOP-PMS-001 | MDR 결정 트리(§803.50 30cd / §803.53 5wd 트리거 기준) + 미보고 사유 양식 첨부 | QA/RA | 불만 → MDR 판정 → 기록 흐름 완비 여부 | | SOP-TRC-001 / SOP-UDI-001 | UDI 기록관리 절 추가 — **§820.35(c)** + 21 CFR Part 830 | RA | GUDID 제출·갱신 기록 체계 구축 여부 | | SOP-SVC-001 (신설/갱신) | **§820.35(b)** 6항목 서비스 기록 양식 도입 | Service/QA | X-ray 출장정비 기록 6항목 완결성 | | SOP-IA-001 | 감사보고서 작성 기준에 "외부 열람 대비 객관적 증거 인용" 항목 추가 | QA | 보고서 품질 기준 갱신 여부 |

### kb-eval-20261106-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_us-002", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "1501ff638a236318", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `1501ff638a236318`
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

> **Regulatory Draft – Imaging‑Room GUI Software (SaMD)**  

---

### 1. Bottom‑line determination  
- **Fastest credible pathway:** 510(k) pre‑market notification (21 CFR §807).  
- **Probable classification:** Class II, regulated under **21 CFR Part 892** – most comparable predicate is a *Medical image management and processing system* (**§892.2050**) because the software controls acquisition, storage and basic processing of radiologic images.  

---

### 2. Required evidence (with citation)  

| Evidence | Requirement & Source |
|----------|-----------------------|
| **QMS compliance** – full QMSR (ISO 13485‑aligned) with documented procedures for ARR, complaint handling, service records and internal audit. | §820.10(b) (ARR); §820.35(a) (complaint file detail); §820.35 (service record); “§820 … whole part” (internal audit). |
| **UDI implementation** – label & packaging carry a UDI in plain‑text and AIDC form; GUDID submission. | Label placement: 21 CFR Part 801 §§801.20‑801.50. System formatting: 21 CFR Part 830 §830.20. |
| **Software Development Lifecycle** – documented SDP, SRS, SAD, SVP, SVR; conformance to IEC 62304 **Class C** (risk class). | IEC 62304 §8.1 (software validation) referenced in source. |
| **Risk Management** – ISO 14971:2019 risk analysis, evaluation and mitigation file (including UI‑error hazards). | ISO 14971 (framework reference). |
| **Usability/Human Factors** – IEC 62366‑1 activities; UI mock‑up testing to demonstrate safe use. | IEC 62366‑1 (framework reference). |
| **Cybersecurity & Change‑Control Plan** – Threat model, SBOM, FDA *Predetermined Change Control Plan* (PCCP) covering any post‑market software updates or AI/ML re‑training. | FDA PCCP (Final guidance Dec 2024) as cited in source; MDCG 2019‑16 Rev.1 for comparison. |
| **AI/ML (if applicable)** – Algorithm description, training data set summary, performance metrics, and a completed FDA PCCP that justifies “no further re‑assessment” for predetermined changes. | Source notes AI/ML link to FDA PCCP (2024‑12‑03) and EU AI Act Art 43(4). |
| **Labeling** – INDICATIONS & USAGE, contraindications, warnings, UDI, storage & handling, software version, installation/operator instructions. | 21 CFR Part 801 labeling requirements (framework reference). |
| **Service & Complaint Records** – System to capture service actions and determine reportability under Medical Device Reporting (MDR). | §820.35 (service record); MDR reporting requirement = 21 CFR Part 803. |
| **Regulatory‑reportable adverse events** – Procedure to assess complaint for MDRS (30‑day) reporting. | Source cites “MDR 30일” and 21 CFR Part 803. |
| **Contract sterilization / relabeling controls** – Though not directly applicable, QMSR must cover any contracted OEM or re‑labeler if the software is distributed pre‑installed on hardware. | §820.10(a) (contracted services). |

---

### 3. Missing information (must be supplied before 510(k) compilation)

| Gap | Why needed |
|-----|------------|
| **Intended Use Statement** – precise claim language, clinical context, and user population. | Determines predicate device match and class. |
| **Predicate Device(s)** – 510(k) numbers and comparison matrix (substantial equivalence). | Required for 510(k) submission. |
| **Detailed Hazard Analysis Summary** – link to risk control measures; completeness of ISO 14971 file. | To satisfy §820.30(c) design controls & risk management. |
| **Full Cybersecurity Threat Model** – identified threats, mitigations, and monitoring plan. | Needed for PCCP and FDA review under 21 CFR §820.30(f). |
| **AI/ML Change‑Control Plan (if AI/ML present)** – documented predetermined changes list. | Required by FDA PCCP guidance; omission blocks clearance. |
| **Usability Engineering Report** – formative & summative testing results, identified use errors and mitigations. | Supports IEC 62366‑1 compliance and FDA usability expectations. |
| **Label Drafts with UDI placement** – exact label artwork showing plain‑text and barcode. | Required for 21 CFR Part 801 & Part 830 submissions. |
| **Service/Installation Instructions** – detailed SOPs for end‑user installation, calibration, maintenance. | Linked to §820.35 service record requirement. |
| **Contractor Qualification Evidence** (if outsourced sterilization/relabeling) – audit reports, agreements. | Meets §820.10(a) expanded QMSR scope. |

---

### 4. Risk Controls Synopsis  

| Hazard | Control(s) | Standard / CFR reference |
|--------|------------|---------------------------|
| Incorrect imaging parameter entry → patient over‑exposure | Input validation, mandatory dose limits, real‑time alerts; usability testing to confirm comprehension. | IEC 62304 §8.1 (validation); IEC 62366‑1 (usability); 21 CFR §820.30(c) |
| Unauthorized software modification → security breach | PCCP‐approved change workflow, digital signatures, SBOM tracking, role‑based access control. | FDA PCCP (2024‑12‑03); §820.30(f) (cybersecurity). |
| Software crash / loss of image data | Watch‑dog timer, automatic save & backup, fault‑tolerant architecture; regression test suite. | IEC 62304 §8.1; §820.70(i) (software validation). |
| Misinterpretation of UI icons → incorrect clinical action | Standardized iconography, user training module, post‑market user feedback loop. | IEC 62366‑1; 21 CFR §820.30(c). |

---

### 5. Human‑Escalation Triggers  

| Situation | Action Required (Human) |
|-----------|--------------------------|
| **Absence of any required document** (e.g., PCCP, risk analysis, UDI plan). | Pause submission; raise to RA lead for gap closure before filing. |
| **FDA Additional Information (AI) request exceeds 180 calendar days or contains “Refuse‑to‑Accept” (RTA) findings.** | Escalate to senior regulatory manager and legal for response strategy. |
| **Internal audit reveals non‑conformance with QMSR §§820.10–820.35** (e.g., missing ARR evidence). | Immediate corrective action plan; notify Quality Director. |
| **AI/ML algorithm change outside predetermined list in PCCP.** | Stop deployment; submit supplemental 510(k) or De Novo if risk class changes. |
| **Complaint judged MDR‑reportable but not logged within 30 days.** | Trigger field safety notice (voluntary correction/removal) under 21 CFR Part 806 & notify FDA via MedWatch. |
| **Contracted sterilizer/relabeler fails audit of QMSR compliance.** | Suspend distribution from that contractor; engage Quality Assurance for re‑qualification. |

---

### 6. Peer‑review prompt  

> *Please review the above assumptions on device classification, the selected predicate approach, and the completeness of the evidence checklist (especially the interplay between QMSR §§820.10‑820.35 and FDA PCCP requirements). Identify any jurisdiction‑specific gaps (e.g., UDI labeling details, MDR reporting process) that may affect the 510(k) strategy.*  

--- 

*End of draft – all citations are drawn directly from the source excerpts or established framework references; no invented identifiers have been introduced.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> QMSR 시행(2026-02-02) 후 맥락에 구 QSR §820.70(i) 잔존 인용(해당 항목은 생산용 SW 밸리데이션)·§820.30(c)/(f) 단락 의미 오배치 경향. UDI 801.20/830.20 분할·§820.35(a)/(b)·§820.10(a)/(b) 소스 매핑은 정확.

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261106-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "75c8fba6e4c134c2", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "ace8476c9535cd1cadac8d64a788cb46b3d78a905da01c1e1dfc3e038615f0f4"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `75c8fba6e4c134c2`
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

> **Regulatory Draft – QMSR & Design‑Control Readiness Assessment**

| Item | Finding / Requirement | Evidence Needed | Current Gap (per source) | Citation |
|------|-----------------------|----------------|--------------------------|----------|
| **Regulatory framework** | The Quality System Regulation has been renamed **Quality Management System Regulation (QMSR)** and is effective 2 Feb 2026. ISO 13485:2016 is incorporated by reference; FDA‑specific addenda are retained in separate §§. | Copy of the final rule (Federal Register 2024‑01709) and technical amendment (Federal Register 2025‑21955); latest eCFR text for 21 CFR Part 820 (as of 02‑Feb‑2026). | None – framework is documented in source. | Federal Register 2024‑01709; 2025‑21955; eCFR 21 CFR Part 820 |
| **Applicable classification / submission route** | Determination of device class (I, II, III) and 510(k) vs PMA pathway is *device‑specific* and must be derived from the intended use and applicable product code. QMSR applies to **all** FDA‑regulated medical devices regardless of class. | Device description, intended use statement, predicate/device classification analysis. | No device information provided; classification cannot be assigned at this stage. | – (no specific identifier in source – verify separately) |
| **Design‑Control requirement** | 21 CFR §820.30 mandates a Design History File (DHF), design planning, inputs, outputs, verification, validation, transfer, and changes. | Complete DHF indexed to each design phase; documented design plans, risk analysis, verification & validation protocols/reports; design change records. | No DHF or design‑control artifacts referenced in source. | 21 CFR §820.30 (framework) |
| **Risk Management** | FDA expects ISO 14971:2019‐based risk management integrated with design controls. | Risk Management Plan, Hazard analyses, FMEA/FMECA, Risk Control measures, residual risk evaluation, post‑market risk monitoring plan. | No risk‑management documentation cited. | ISO 14971:2019 (framework) |
| **Process Validation & Software** (if applicable) | For software/AI devices, a Predetermined Change Control Plan (PCCP) is required per FDA guidance (Dec 2024). | PCCP document, change‑control workflow, validation of algorithm updates. | No mention of PCCP or software‑specific controls. | Predetermined Change Control Plan (PCCP) – final guidance Dec 2024 |
| **Quality Management System documentation** | Required QMS documents: Quality Manual, SOPs, work instructions, records, internal audit program, CAPA system, management review minutes. | Current version of each SOP (e.g., SOP‑RA‑002, SOP‑CA‑001 etc.), evidence of implementation (training records, audit findings). | Source only lists sample SOP naming conventions; actual documents not provided. | No specific identifier found in source – verify separately |
| **UDI compliance** | Device labeling must include a UDI per 21 CFR §801.20 et seq.; the UDI system itself is governed by 21 CFR §830. | Label artwork showing plain‑text and AIDC barcode; GUDID submission confirmation. | No label or UDI evidence supplied. | 21 CFR §801.20 (framework) |
| **Post‑market surveillance** | For Class II/III devices, a corrective‑and‑preventive action (CAPA) system and reporting per 21 CFR §803 (MDR) & §806 (corrections/removals). | CAPA records, MDRO reports, field safety notices. | Not addressed in source. | No specific identifier found in source – verify separately |

### Human‑Escalation Triggers
| Trigger | Condition | Action |
|--------|-----------|--------|
| **Missing Device Definition** | No intended use or device class supplied. | RA lead must request product description from engineering; pause QMSR readiness assessment until received. |
| **Absent DHF / Design Controls** | No design‑history artifacts present. | Escalate to Engineering Manager & Quality Director for immediate compilation of DHF; flag to senior management if >10 business days delay. |
| **Risk Management Gap** | Risk analysis not documented or not tied to ISO 14971. | Issue a non‑conformance in CAPA system; require corrective plan within 15 days; notify Regulatory Affairs VP. |
| **UDI & Labeling Deficiency** | No label with UDI supplied for device(s). | Notify Marketing/Labeling team; if deadline >30 days, raise to Compliance Officer. |
| **PCCP Requirement (AI/ML)** | Device uses adaptive algorithm but lacks PCCP. | Immediate escalation to Software Lead and Regulatory Affairs for PCCP drafting; report to senior management. |
| **Audit Findings** | Internal audit uncovers any of the above gaps. | Record finding, assign corrective action owner, elevate to Quality Management Review meeting. |

---

#### Peer‑Review Prompt
*“Colleague, please review the assumptions made about the applicability of ISO 14971 risk management and the need for a Predetermined Change Control Plan (PCCP). Verify whether any FDA‑specific addenda in Federal Register 2025‑21955 impose additional design‑control or documentation requirements beyond the standard 21 CFR §820.30 provisions. Also assess if there are jurisdictional gaps—e.g., missing UDI citation details or post‑market surveillance obligations—that should be incorporated for a complete QMSR readiness package.”*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> [최종(shadow 수용) 3→2] ① "21 CFR §820.30 mandates a DHF…" — QMSR 시행(2026-02-02) 후 구 §820.30 제거·ISO 13485 §7.3 IBR 전환 맥락의 잔존 인용(11-02 확립 계열) ② "PCCP is required per FDA guidance" — PCCP 가이던스(2024-12)는 자발적 권고·의무 아님. 그 외 FR 번호·UDI 분할·헤징은 정상.

**Source Excerpts**

1. Chunk `197674093189403324`

> ## 7. 출처 - FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr - FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions - eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820 - Federal Register: 2024-01709 (제정), 2025-21955 (기술적 수정) - FDA Compliance Program 7382.850 - 확인일: 2026-05-25

2. Chunk `211815826167619677`

> ## 1. 규정 개요 | 항목 | 내용 | |------|------| | 규정 | 21 CFR Part 820 | | 명칭 변경 | Quality System Regulation(QSR) → **Quality Management System Regulation(QMSR)** | | 최종규칙 공포 | Federal Register 2024-01709 (2024.2.2) | | 기술적 수정 | Federal Register 2025-21955 | | **발효일** | **2026년 2월 2일** | | 핵심 변경 | ISO 13485:2016을 참조편입(Incorporation by Reference)하고, FDA 추가요구를 별도 조항으로 보존 |

### kb-eval-20261106-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "QSR"], "profile_id": "ra-us", "scenario_id": "d8ccffa24b837a6e", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/QSR_21CFR820/README.md", "source_hash": "5250406488094d588d38eb1e45c2d8d4b90f093334322d2ded3d50d3a2e72871"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `d8ccffa24b837a6e`
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

> **Regulatory Draft – Diagnostic X‑ray System (Radiation‑Emitting Device)**  

---

### 1. Regulatory Classification & Submission Route  
| Item | Determination | Basis |
|------|----------------|-------|
| **Device class** | Class II (special controls) | Diagnostic X‑ray equipment is regulated under **21 CFR Part 1020** (Performance Standards for Diagnostic X‑ray Systems). FDA’s classification database lists this hardware as Class II with special control requirements. *(no specific identifier found in source — verify separately)* |
| **Primary submission pathway** | Traditional **510(k) Premarket Notification** – demonstrate substantial equivalence to a cleared predicate diagnostic X‑ray system (e.g., product code *NRG*). | 21 CFR §807 (premarket notification) applies to Class II devices. |
| **Alternative pathway** | **De Novo** if no suitable predicate exists (or if the device incorporates novel features not covered by existing special controls). | FDA guidance on De Novo classification for novel Class I/II devices. |

---

### 2. Core Regulatory Requirements & Evidence Package  

| Requirement | Expected evidence | Relevant citations |
|-------------|-------------------|--------------------|
| **Device description & intended use** | Detailed narrative, indications, user population, clinical environment. | No specific identifier found in source — verify separately |
| **Predicate device identification** | 510(k) number, product code, manufacturer, clearance date. | No specific identifier found in source — verify separately |
| **Performance testing (radiation safety)** | • Dose output, HVL, beam alignment, field uniformity <br>• Compliance with **21 CFR Part 1020.30‑32** (performance standards) <br>• IEC 60601‑1 (general safety) & IEC 60601‑2‑22 (radiology equipment) test reports. | **21 CFR Part 1020.30‑32** |
| **Image quality validation** (if applicable) | • Spatial resolution, contrast detail, detective quantum efficiency; comparison to predicate. | No specific identifier found in source — verify separately |
| **Electrical & EMC compliance** | Test reports per IEC 60601‑1 (including A/B testing), IEC 61000 series for EMI/EMC. | No specific identifier found in source — verify separately |
| **Risk Management** | ISO 14971:2019 risk analysis file, risk control measures, residual risk evaluation. | **ISO 14971:2019** (framework reference) |
| **Software lifecycle (if software present)** | IEC 62304:2006+A1:2015 development plan, verification/validation reports. | **IEC 62304:2006+A1:2015** |
| **Labeling & UDI** | • Full labeling package (IFU, safety warnings) <br>• UDI on label and packaging per **21 CFR Part 801 Subpart B (§801.20+)** and device‑specific identifier format per **21 CFR Part 830 §830.20**. | **21 CFR Part 801 §§801.20‑801.50**, **21 CFR Part 830 §830.20** |
| **Quality Management System (QMS) compliance** | Demonstration of conformity to the updated **Quality Management System Regulation (QMSR)** effective 2026‑02‑02, aligned with **ISO 13485:2016**. Includes SOPs, CAPA, design control records, management reviews, etc. | **21 CFR Part 820** (as revised by QMSR) – *no specific identifier in source; see source note on amendment* |
| **Radiation‑emitting product records & reporting** | Procedures for recordkeeping per **21 CFR Part 1002** (radiation‑emitting products). | **21 CFR Part 1002** |
| **Light‑emitting component compliance** (if device includes visible light sources) | Conformance to **21 CFR Part 1040** for Light‑Emitting Products. | **21 CFR Part 1040** |

---

### 3. Gaps / Missing Information (to be clarified before filing)

| Gap | Why needed | Action |
|-----|------------|--------|
| Exact **intended use statement** and claim language | Drives predicate selection & labeling. | Obtain from product development lead. |
| Identified **predicate device(s)** with 510(k) numbers | Required for substantial‑equivalence argument. | Search FDA’s 510(k) database; document selection rationale. |
| Complete **performance test data** (dose, HVL, beam geometry) | Must meet Part 1020 performance standards. | Conduct or compile test reports; compare against predicate. |
| **Risk Management File** (hazard analysis, risk controls) | FDA expects ISO 14971‑based RM. | Prepare / update RM documentation. |
| **QMSR implementation evidence** (ISO 13485:2016‑aligned SOPs, CAPA records) | New QMSR became effective 2026‑02‑02; must be in place for submission. | Perform gap analysis, issue missing SOPs, document compliance. |
| **Labeling draft with UDI placement** | UDI must appear on device label per Part 801; GUDID submission required under Part 830. | Prepare labeling mock‑up; create/submit GUDID entry. |
| **Software development documentation** (if software is embedded) | Required by IEC 62304 and FDA’s software guidance. | Compile design history file for software module. |
| **Sterilization validation** (if device marketed sterile) | Needed for claim of sterility; not covered in source excerpts. | Perform sterility assurance level (SAL) studies or provide justification for non‑sterile marketing. |

---

### 4. Recommended Risk Controls (aligned to identified hazards)

| Hazard | Control(s) | Verification |
|--------|------------|---------------|
| Excessive radiation dose to patient/operator | • Automatic exposure control (AEC) <br>• Interlock system that disables X‑ray generation if safety door open <br>• Dose monitoring & display | Test interlock functionality; validate AEC algorithm. |
| Beam misalignment / poor image quality | • Calibration routine per IEC 60601‑2‑22 <br>• Periodic QA program (monthly output checks) | Document calibration certificates; QA logs. |
| Electrical shock / fire | • Ground fault circuit interrupter (GFCI) <br>• Compliance with IEC 60601‑1 safety requirements | Electrical safety test reports. |
| Software malfunction (if applicable) | • Version control, change management via **Predetermined Change Control Plan (PCCP)** <br>• Fail‑safe mode on software error | Verify PCCP is in place; run software verification tests. |
| User error (mis‑setting parameters) | • Human‑factors‑based UI design <br>• On‑screen prompts & warnings <br>• Training program and user manual | Conduct usability testing per IEC 62366‑1. |

---

### 5. Human‑Escalation Triggers  

| Situation | Escalation to senior RA / regulatory counsel |
|-----------|---------------------------------------------|
| **No suitable predicate** identified after exhaustive search. | Initiate De Novo feasibility assessment. |
| **QMSR gap**: critical SOPs missing (e.g., design control, CAPA) that prevent submission readiness. | Immediate escalation for QMS remediation plan and timeline. |
| **Failure to meet Part 1020 performance criteria** in testing (dose > limits). | Escalate to engineering leadership; consider redesign before filing. |
| **UDI/GUDID non‑compliance** (e.g., label design does not accommodate required UDI format). | Escalate to labeling/graphics team and regulatory for corrective action. |
| **FDA Additional Information (AI) request exceeds 30 days resolution window** or requires new clinical data. | Notify project manager; consider timeline impact and resource allocation. |
| **Discovery of a new applicable special control** not captured in current submission package. | Escalate to senior RA for amendment strategy. |

---

### 6. Peer‑Review Prompt  

> *“Colleague, please review the assumptions made above regarding (1) classification as Class II under Part 1020, (2) reliance on a traditional 510(k) pathway versus De Novo, and (3) the completeness of the QMSR evidence checklist. Identify any gaps in jurisdiction‑specific coverage—especially relating to recent QMSR implementation dates or additional special controls that may apply to diagnostic X‑ray systems.”*  

--- 

**End of Draft**

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> ① Part 1020을 분류 근거로 오인 — 1020은 방사선 성능기준(분류는 Part 892) ② "IEC 60601-2-22 (radiology equipment)" — KB 전체 무출연, X-ray 계열 특수표준은 60601-2-28(발생장치)·2-54(촬영·투시) — 10-28 us-005 60601-2-54 주제 오독과 동일 계열.

**Source Excerpts**

1. Chunk `136831192110451403`

> ## 추가 규제 (X-ray 관련) - **21 CFR Part 1020.30 ~ 1020.32**: Radiation Control – Performance Standards for Diagnostic X-ray Systems - **21 CFR Part 1002**: Records and Reports (Radiation-Emitting Products) - **21 CFR Part 1040**: Performance Standards for Light-Emitting Products (관련 시)

2. Chunk `18877965943708175`

> ## 현황 - 기존 QSR(21 CFR 820)은 2024년 공표된 Quality Management System Regulation (QMSR)으로 개정됨. - **시행일: 2026년 2월 2일** → ISO 13485:2016과 정합화.

### kb-eval-20261106-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "c63cafac39b81151", "source": "github:holee9/MD-process/03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md", "source_hash": "8ae673fb6f1587e4dc2d26f9f4b3680719f501c71d0ce6d5450609814a7d126e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c63cafac39b81151`
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

> **Regulatory Draft – SBOM Compliance under the FDA QMSR (2026‑02‑02)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Current Status | Comment |
|------|----------------|---------|
| **Device type / intended use** | *Not provided in source* | Required to place the product in a CFR part (e.g., Part 892 for imaging, Part 862 for clinical chemistry). Until clarified, classification cannot be assigned. |
| **Proposed regulatory class** | TBD – assume existing 510(k) clearance if the device is already on the market; otherwise determine class per 21 CFR §807.92 after defining intended use. | A definitive classification hinges on the missing device description. |
| **Submission route** | • If Class II with an accepted predicate → traditional 510(k). <br>• If no suitable predicate or novel cybersecurity approach → consider De Novo (21 CFR §814.126) before a future 510(k). | Decision deferred until classification is known. |

---

### 2. Required Evidence to Satisfy QMSR (FDA Quality Management System Regulation)  

| Requirement (per FDA QMSR & ISO 13485) | Evidentiary Element | Source / Citation |
|----------------------------------------|----------------------|-------------------|
| **Record‑keeping for SBOM** | • Full Software Bill of Materials (SBOM) <br>• Associated Vulnerability Exchange (VEX) statements <br>• Vulnerability Disclosure Report (VDR) | FDA QMSR 2026‑02‑02; 21 CFR §820.35 (Document Control); ISO 13485:2016 §4.2.5 (Record Management). |
| **Inclusion in Cybersecurity File** | SBOM, VEX, VDR stored in a dedicated “Cybersecurity File” within the Master Device File (MDF) | Same as above. |
| **Traceability of SBOM changes** | Mapping table linking Build ID ↔ SBOM version ↔ VEX entry (1:1:1 relationship) | SOP‑CC‑001 (change‑control entry counts) – internal reference; QMSR §820.35. |
| **Electronic signature & readiness for FDA inspection** | Electronic signatures on SBOM documents; ability to produce SBOM within 2 h of request | FDA QMSR requirement; “2시간 내 제출 가능” in source. |
| **Quarterly self‑audit** | Completed audit report confirming the above items, signed by Security Officer | Source lists “분기 자체감사 완료”. |
| **Patch timeline documentation** | Dates of vulnerability identification, patch release, and SBOM update | Required for “패치 타임라인 문서화”. |

---

### 3. Missing Information (Gap Analysis)  

| Gap | Why it matters | Action needed |
|-----|----------------|--------------|
| **Device description, intended use & regulatory class** | Determines CFR part, classification, and submission pathway. | RA Lead to obtain product spec sheet / labeling. |
| **Predicate device (if 510(k) route)** | Needed for substantial‑equivalence claim. | Identify existing cleared device; capture 510(k) number. |
| **Risk Management File (ISO 14971:2019)** – linkage of SBOM vulnerabilities to risk controls. | Demonstrates that identified software risks are mitigated per the risk management process. | Update RMF with hazard analysis for each listed component. |
| **Predetermined Change Control Plan (PCCP) if AI/ML components exist** | Required for pre‑authorized post‑market changes under FDA guidance (Dec 2024). | Develop PCCP or confirm it is not applicable. |
| **UDI labeling compliance (21 CFR §801.20 et seq.)** | UDI must appear on label/device packaging; SBOM does not affect this but overall QMSR compliance includes labeling. | Verify UDI placement; incorporate if missing. |
| **Evidence of electronic signature validation** | Must satisfy 21 CFR §820.30 (Design Controls) and Part 11 (Electronic Records). | Provide audit trail screenshots or system validation summary. |

---

### 4. Risk Controls Related to SBOM & Cybersecurity  

1. **SBOM Generation Procedure** – ensures complete component list for each software release.  
2. **VEX Review Process** – triage affected components; assign severity (Critical/High/Medium/Low) and define remediation timelines.  
3. **Patch Management / Update Mechanism** – timely deployment of fixes; documented in “패치 타임라인”.  
4. **Change‑Control Integration** – SBOM change entries trigger a review under the device’s Change Control SOP (e.g., SOP‑CC‑001).  
5. **Predetermined Change Control Plan (PCCP)** – if AI/ML, pre‑authorizes future algorithm updates while preserving SBOM integrity.  
6. **Quarterly Self‑Audit** – verifies that the Cybersecurity File remains current; non‑conformities trigger corrective actions per 21 CFR §820.100.  

---

### 5. Citations (per rules)  

- **FDA QMSR** (effective 2026‑02‑02).  
- **21 CFR Part 820 §820.35** – Document control & record keeping. *(Framework reference – no verification caveat needed)*  
- **ISO 13485:2016 §4.2.5** – Records management requirements. *(Framework reference)*  
- **ISO 14971:2019** – Risk management (risk‑based mapping of SBOM findings). *(Framework reference)*  
- **Predetermined Change Control Plan (PCCP)** – FDA Guidance, Dec 2024. *(Framework reference)*  

*No specific device numbers, docket IDs, or article/section identifiers were present in the source excerpts; therefore none are listed.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Who Escalates | Immediate Action |
|---------|---------------|------------------|
| **Inability to produce SBOM within 2 h** (e.g., missing electronic signature or incomplete file) | QA Manager / RA Lead | Notify Senior Management; prepare a corrective action plan and consider filing a 510(k) supplement (if already cleared) or a De Novo request for new cybersecurity claims. |
| **Critical vulnerability identified without an available fix** | Security Officer | Initiate field‑correction/field‑removal protocol under 21 CFR §806; submit FDA Medical Device Reporting (MDR) as required (§803). |
| **Quarterly self‑audit yields non‑conformance** | QA Manager | Open a CAPA, document in the QMS, and report to the Quality Executive. |
| **Missing mapping between SBOM entries and risk controls** | RA Lead | Amend the Risk Management File; if impact is material, consider an Additional Information (AI) request to FDA for clarification before next inspection. |
| **Discovery of undocumented third‑party component in software build** | Software Development Lead | Halt release, perform root‑cause analysis, update SBOM and VEX, and inform Quality Assurance for re‑audit. |

---

### 7. Regulatory Judgment  

- **Classification & submission pathway cannot be finalized until the device’s intended use and regulatory class are defined.**  
- **All QMSR‑mandated SBOM evidences listed above must be generated, maintained in a Cybersecurity File within the MDF, and be instantly retrievable for FDA inspection.**  
- **Any failure to meet the 2‑hour SBOM availability requirement or to remediate critical vulnerabilities constitutes an escalation trigger that should be raised to senior leadership and addressed through CAPA/field action procedures.**  

---

### 8. Peer Review Prompt  

> *Colleague, please review: (1) the assumption that a traditional 510(k) route is appropriate pending classification; (2) completeness of the required evidence checklist against current FDA QMSR guidance; and (3) whether any jurisdiction‑specific gaps—particularly around UDI labeling or PCCP applicability—have been overlooked.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> [최종(shadow 수용) 2→1·예외 발동] ① focus(QMSR·design-control readiness) 대비 510(k)/De Novo 경로 서술 편중, design-control 준비성 미다룸 ② §807.92 오인용(등급결정 근거 아님·계열 6회차) ③ §820.100 CAPA — QMSR 제거 조항 ④ "De Novo §814.126" 비존재(De Novo는 Part 860 Subpart D) ⑤ §820.35 "Document Control" 명칭 오기(Control of records). 소스 기반 항목(2시간 SBOM·분기 자체감사)은 충실.

**Source Excerpts**

1. Chunk `1031175965966205535`

> ┌──┬──────────┬────────┬──────┬────────────┬──────┬──────┐ │# │구성요소 │CVE ID │CVSS │VEX 판정 │사유 │조치 │ │ │(PURL) │ │Score │ │ │기한 │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │1 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ ├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤ │2 │ │ │ │□N/A □Aff │ │ │ │ │ │ │ │□Fix □Inv │ │ │ └──┴──────────┴────────┴──────┴────────────┴──────┴──────┘ (N/A=not_affected, Aff=affected, Fix=fixed, Inv=under_investigation) 총 취약점: __건 Critical: __ High: __ Medium: __ Low: __ 변경관리 진입 건수: __건 (SOP-CC-001) 승인: Security Officer ___________ 일자: ____-__-__ ```

2. Chunk `1070786144928344628`

> ### 5.8 QMSR 실사 대응 — SBOM 기록 요구사항 (v0.3 신설) FDA QMSR(2026-02-02 시행)에 따라 SBOM 관련 기록은 ISO 13485:2016 §4.2.5 기록 관리 요구사항을 준수해야 한다. | 단계 | 수행자 | 활동 | 판정 기준 | |------|--------|------|-----------| | 5.8.1 | QA Manager | SBOM·VEX·VDR을 MDF 내 사이버보안 파일(Cybersecurity File)로 편입 | QMSR §820.35/ISO 13485 §4.2.5 준수 | | 5.8.2 | QA Manager | SBOM 변경 이력의 추적성 확보 — 빌드 ID↔SBOM↔VEX 삼중 연결 | 1:1:1 대응 확인 | | 5.8.3 | RA Lead | FDA 실사 시 SBOM 즉시 제시 가능 상태 유지 (전자 서명 포함) | 2시간 내 제출 가능 | | 5.8.4 | Security Officer | QMSR 감사 관점 자체 점검 — SBOM 갱신 이력, VEX 판정 근거, 패치 타임라인 문서화 | 분기 자체감사 완료 | **QMSR 실사 체크포인트:** - 사이버보안 파일(Cybersecurity File)이 MDF 내 독립 섹션으로 구성되어 있는가? - SBOM이 최신 릴리스...

## ra_eu

### kb-eval-20261106-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "68b271ad426f8222", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `68b271ad426f8222`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning**  
*Products: X‑ray Detector (Class IIa), Handheld X‑ray Source (Class IIb), GUI Software (SaMD, Class IIa)*  

---

## 1. Device Classification & Conformity Assessment Route  

| Product | MDR rule applied* | Resulting class | Art. 52 route | Notified Body involvement |
|---------|-------------------|------------------|---------------|---------------------------|
| X‑ray Detector (imaging sensor) | Rule 17 – “devices specifically intended for recording diagnostic images generated by X‑ray radiation” | **IIa** | **Art. 52(6)** – Annex IX (QMS + technical‑documentation assessment of one representative device per generic group) | NB required (full Annex IX assessment) |
| Handheld X‑ray Source (emits ionising radiation) | Rule 10 (active device that emits ionising radiation for diagnostic radiology) → **IIb** | **IIb** | **Art. 52(4)** – either Annex IX (full QMS + technical‑documentation assessment) *or* Annex X + XI (type‑examination + production conformity verification) | NB required (Annex IX or X + XI) |
| GUI Software (SaMD that provides image display/interpretation) | Rule 11 – “software providing information used for diagnostic decisions” (impact on diagnosis is moderate) | **IIa** | **Art. 52(6)** – Annex IX (QMS + technical‑documentation assessment) | NB required |

\*Rule numbers are taken from the MDR classification matrix (Annex VIII, Rules 9–11, 17).

---

## 2. Required Evidence for Technical Documentation (Annex II §6.1)

| Product | Mandatory annexes/evidence (as per source) | Gaps / Missing items |
|---------|--------------------------------------------|----------------------|
| **X‑ray Detector** | • Clinical Evaluation Report (CER) <br>• Risk Management File (RMF) <br>• IEC 62220‑1‑1 test data (Detective Quantum Efficiency – DQE) | – No latest DQE trend analysis (source lists “DQE 저하” as a PMS data source but no quantitative baseline). <br>– No documented PMCF plan; only “동등성 클레임 검토 후 결정”. |
| **Handheld X‑ray Source** | • CER <br>• RMF <br>• Radiation dose‑monitoring data (ionising radiation) | – PMCF is only “이온화 방사선 → 임상 데이터 적극 수집 권고” – lacks a formal PMCF protocol with objectives, endpoint definitions and sample size. |
| **GUI Software** (SaMD) | • CER <br>• RMF <br>• IEC 62304 maintenance records & bug‑log | – Explicit usability/clinical performance data required for SaMD (ISO 14971 risk control of use errors not demonstrated). <br>– No PMCF plan; source says “사용 중 오류 데이터 수집 필수” but does not specify collection method, frequency or analysis. |

---

## 3. Post‑Market Surveillance System (Art. 83) & Plan (Art. 84)

**Common data sources (source [2] – “정보 수집원”)**

| Source | Collection method | Frequency |
|--------|-------------------|-----------|
| Serious incidents, PSURs, FSCAs | Vigilance system (EUDAMED) | Immediate / quarterly |
| Non‑serious adverse events & side‑effects | Complaint management system | Monthly |
| Trend‑reporting data | Internal statistics aggregation | Quarterly |
| Literature & registries (PubMed, IEC/ISO DB, MAUDE) | Desk research | Semi‑annual |
| User / distributor feedback | CRM / service data | Monthly |
> “●” indicates applicability to all three products (source [2]).

**Product‑specific PMS considerations**

| Product | PSUR update cadence (source [1]) | Key PMS signals to monitor |
|---------|----------------------------------|-----------------------------|
| X‑ray Detector (IIa) | **Every 2 years** | DQE degradation, pixel defects, patient dose exceedance |
| Handheld Source (IIb) | **Every 1 year** (per source [1]) | Dose over‑run, mechanical damage, battery anomalies |
| GUI Software (IIa) | **Every 2 years** | Software errors, image display faults, usability issues |

**Required PMS documentation**

* Annex III – PMS Technical Documentation must contain:  
  - PMS plan (Art. 84) referencing all sources above.  
  – Periodic Safety Update Report (PSUR) per Art. 86 (IIa/IIb → ≤ 2 yr, IIb device with annual cadence justified by higher risk).  

* For the Handheld Source (class IIb), an **annual PSUR** is mandatory (Art. 86(1)/(2)). The source already specifies a 1‑year cycle – this aligns with Art. 86.

---

## 4. Post‑Market Clinical Follow‑up (PMCF) Requirements (Annex XIV Part B)

| Product | PMCF necessity (source [1]) | Minimum elements to be defined |
|---------|------------------------------|---------------------------------|
| X‑ray Detector | “동등성 클레임 검토 후 결정” – PMCF may be waived if equivalence with a predicate can be demonstrably proven. | • Equivalence justification (comparative bench testing, literature). <br>• Residual clinical data gap analysis. |
| Handheld Source | “이온화 방사선 → 임상 데이터 적극 수집 권고” – PMCF **recommended**. | • Clinical performance endpoints (dose accuracy, safety). <br>• Target sample size & follow‑up period. <br>• Data collection plan (registry vs prospective study). |
| GUI Software | “SaMD → 사용 중 오류 데이터 수집 필수” – PMCF **required** for SaMD. | • Real‑world usage data (error logs, usability incidents). <br>• Clinical impact of software‑driven decisions. <br>• Periodic analysis & risk reassessment per ISO 14971. |

*All PMCF plans must be kept current under Art. 61 and referenced in the CER (Annex XIV Part A).*

---

## 5. Risk Controls – Alignment with GSPR (Annex I §§3‑9, 16, 17, 18)

| Product | Relevant GSPR clauses | Existing evidence | Remaining control actions |
|---------|-----------------------|-------------------|----------------------------|
| X‑ray Detector | §16 (radiation protection), §23 (labeling) | RMF present, DQE test data pending | • Verify radiation dose monitoring meets §16.4.<br>• Update labeling with performance limits for DQE and pixel defects. |
| Handheld Source | §§16 (ionising radiation), 18 (active devices), 23 (instructions) | RMF & dose‑monitoring data exist, but no systematic PMCF | • Implement risk control for battery failure (§7). <br>• Define user‑error safeguards per §5 (use‑error risks). |
| GUI Software | §§17 (electronic programmable systems), 23 (information supplied) | IEC 62304 maintenance records available | • Conduct usability engineering per IEC 62366‑1 to satisfy §22 (lay‑person use). <br>• Add software error handling & mitigation strategies in RMF. |

All three products must demonstrate **residual risk ≤ risk acceptability criteria** (Annex I §3) and maintain a **Risk Management File** per ISO 14971:2019.

---

## 6. EUDAMED Registration Requirements

* All three devices require UDI registration + vigilance reporting (source [1] – “UDI 등록 + Vigilance 보고”).  
* For the SaMD, UDI registration follows the same rules but must also reference software versioning in the device identifier (no specific source detail – *verify separately*).

---

## 7. Missing Information & Immediate Action Items

| Item | Why it is needed | Impact if not addressed |
|------|------------------|--------------------------|
| **Up‑to‑date DQE trend data** for X‑ray Detector | Supports GSPR §16 and PSUR risk analysis | Incomplete PMS → NB may request additional evidence |
| **Formal PMCF protocol** for Handheld Source & GUI Software | Required by Annex XIV Part B; critical for Class IIb/IIa SaMD | Non‑compliance with Art. 61 → CE mark could be suspended |
| **Equivalence justification dossier** (benchmark data) for X‑ray Detector | Determines whether PMCF can be waived | Absence leads to unnecessary PMCF and timeline delays |
| **Usability test reports** (IEC 62366‑1) for GUI Software | Addresses GSPR §§22 & §5 (use‑error) | Potential safety‑related non‑conformities in NB audit |
| **Annual PSUR preparation schedule** for Handheld Source | Aligns with Art. 86(2) annual requirement for Class IIb | Missed PSUR → vigilance non‑compliance |
| **Clear mapping of data sources to PMS activities** (e.g., linking complaint system metrics to specific risk controls) | Ensures traceability and completeness of PMS plan (Art. 84) | Weak audit trail, possible NB findings |

---

## 8. Human‑Escalation Triggers  

1. **Classification Discrepancy** – If any product is later deemed to fall under a different rule/class (e.g., Detector re‑evaluated as Rule 9 → Class IIb), the conformity route must be revised; trigger senior RA review.  
2. **Evidence Gaps** – Absence of DQE data, PMCF protocol, or usability reports should be escalated to product development / clinical team for immediate generation.  
3. **EUDAMED Registration Failure** – Any missing UDI or vigilance linkage must be flagged to the regulatory operations lead.  
4. **NB Audit Findings** – Early detection of non‑conformities (e.g., incomplete RMF) should be raised to quality assurance manager.  
5. **Regulatory Deadline Misses** – PSUR not ready before the stipulated 2‑yr or 1‑yr cut‑off must trigger a project‑management escalation.

---

## 9. Peer Review Prompt  

> *Colleague, please challenge the following assumptions and identify any jurisdictional gaps:*
> 
> - The classification of the Handheld X‑ray Source under Rule 10 (IIb) – could any auxiliary functions push it to Rule 9 or higher?  
> - Adequacy of the “동등성 클레임 검토 후 결정” approach for waiving PMCF on the Detector; does current MDR guidance allow a waiver solely on equivalence without additional clinical data?  
> - Completeness of PMS source mapping – are there any mandatory EU‑wide data sources (e.g., EUDAMED trend reporting) not reflected in the table?  
> - Alignment of PSUR cadence for Class IIb devices with Art. 86(2); does a 1‑year update satisfy all required content (benefit–risk, PMCF, sales volume)?  

Please provide feedback on any missing citations, risk‑control items, or documentation elements that could affect NB acceptance.

---

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> PSUR IIb 변형 재발 — "annual PSUR is mandatory (Art. 86(1)/(2))"·"Art. 86(2) annual requirement for Class IIb"는 법률 오귀속: 원문 86(1)은 IIb 최대 2년, 연간은 III·이식형. 소스의 자사 1년 주기를 법 의무로 승격(같은 응답에 ≤2yr 정확 서술도 있어 자기모순). PSUR 계열 종결(11-05) 대비 변형 재발 관찰 필요.

**Source Excerpts**

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

### kb-eval-20261106-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "1bc31feaca3ea1cd", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `1bc31feaca3ea1cd`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & PMCF Planning for an X‑ray Diagnostic Device (and associated SaMD)**  

---

### 1. Device Overview (as inferred from source)

| Item | Current knowledge (source) |
|------|----------------------------|
| **Technology** | Ionising‑radiation–emitting diagnostic equipment (X‑ray generator). |
| **Software component** | Medical device software (SaMD) that processes the X‑ray images. |
| **Regulatory excerpt** | “Rule 10: ionising‑radiation‑emitting diagnostic devices → Class IIb” & “Rule 11: SaMD classification”. (Source [2]) |

> **Note:** A complete device description, intended use wording, user group, and labeling have not been provided – these will be required for the technical documentation.

---

### 2. Classification & Conformity‑Assessment Route  

| Aspect | Determination |
|--------|----------------|
| **Classification rule** | **Rule 10** (active diagnostic device that emits ionising radiation) → **Class IIb** (Source [2]). |
| **Software classification** | Apply **Rule 11** to the SaMD; preliminary assumption is **Class IIa or IIb** depending on the impact of the diagnostic decision. A detailed software risk analysis is required before final class assignment. |
| **Conformity‑assessment route** | Under **Article 52(4) MDR 2017/745**, a Class IIb device may follow either: <br>1. **Annex IX** – full quality‑management system assessment + technical‑documentation examination by a Notified Body, **or** <br>2. **Annex X + Annex XI** – EU type‑examination (Annex X) combined with Production Conformity Verification (Annex XI). |
| **Notified‑Body involvement** | Mandatory for both routes; selection must be documented in the EU Declaration of Conformity (Art. 19, Annex IV). |

---

### 3. Required Evidence & Documentation  

| Section of MDR | Required Artefact(s) | Key Content (high‑level) |
|----------------|----------------------|--------------------------|
| **Annex II – Technical documentation** (§6.1) | • Device description and specification<br>• Intended purpose & labeling (Annex I §23)<br>• Design & manufacturing information<br>• Risk Management File (ISO 14971:2019) <br>• Clinical Evaluation Report (CER) – Annex XIV Part A, kept current (Art. 61) <br>• PMCF plan & evaluation report – Annex XIV Part B |
| **Annex I – GSPR** | • Checklist compliance for all 23 requirements (source mentions “GSPR checklist‑based conformity assessment” – Source [2])<br>• Specific items: <br> – §16 (radiation safety) <br> – §17/§18 (software & active devices) |
| **Annex III – PMS technical documentation** | • PMS system (Art. 83)<br>• PMS plan (Art. 84) – includes routine reporting, trend analysis, and field safety corrective actions (FSCA) per Art. 87<br>• PSUR for Class IIb (Art. 86) – to be updated at least every **2 years** |
| **Standards supporting evidence** | • ISO 14971:2019 (risk management)<br>• IEC 60601‑2‑54 (X‑ray equipment safety)<br>• IEC 62304 (software lifecycle)<br>• IEC 62366‑1 (usability engineering) |
| **Clinical data** | • Clinical performance data from either a systematic literature review (state of the art) or a clinical investigation (if required). <br>• For SaMD, validation of diagnostic algorithm against a reference comparator. |

---

### 4. Gaps / Missing Information (to be addressed before NB submission)

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Exact intended use statement** | Drives classification, risk analysis & clinical evaluation scope. | Draft a concise Intended Use description and submit for internal review. |
| **Full device architecture (hardware + software)** | Needed to populate Annex II §1‑3 and to assess software risk (Rule 11). | Produce block diagram & interface matrix; identify safety‑critical functions. |
| **Labeling / IFU** (incl. §§23) | Required for GSPR compliance & Declaration of Conformity. | Draft labeling in accordance with Annex I §23, translate into required languages. |
| **Clinical evidence** – literature search results, device‑specific performance data | Needed for CER and to justify any deviation from the state of the art. | Conduct systematic review; plan/execute a clinical investigation if gaps remain. |
| **Radiation safety testing report** (dose measurements, shielding) | Directly linked to Annex I §16 & IEC 60601‑2‑54 compliance. | Commission testing in an accredited lab; attach test reports. |
| **Software risk classification justification** (Rule 11) | Determines whether the SaMD requires a separate NB assessment or can be bundled. | Perform software risk analysis per ISO 14971 and map to Rule 11 decision tree. |
| **PMCF plan details** – study design, endpoints, population size | Required for Annex XIV Part B and later PSUR updates. | Draft PMCF protocol; identify data sources (registries, post‑market use). |
| **Usability engineering file** (IEC 62366‑1) | Supports risk control for user error (§5). | Conduct usability test with representative users; document findings. |

---

### 5. Core Risk Controls (illustrative)

| Hazard area | Applicable GSPR clause(s) & Standard(s) | Example control measures |
|-------------|----------------------------------------|--------------------------|
| **Ionising radiation exposure** | Annex I §16; IEC 60601‑2‑54 | • Automatic dose limiting circuitry <br>• Shielding verification <br>• Interlock to prevent accidental emission |
| **Electrical safety & EMC** | Annex I §§18, 20; IEC 60601‑2‑54 | • CE marking for electrical safety <br>• Conducted and radiated emissions testing |
| **Software malfunction / diagnostic error** | Annex I §17/§18; IEC 62304; Rule 11 | • Software development lifecycle (SRS, verification, validation) <br>• Independent code review & static analysis <br>• Fail‑safe mode & alarm for out‑of‑range results |
| **Use‑error** | Annex I §5 | • Human factors engineering (IEC 62366‑1) <br>• Clear labeling & IFU, pictograms <br>• Training program for operators |
| **Device lifecycle / ageing** | Annex I §6 | • Periodic performance verification per maintenance schedule <br>• Replaceable X‑ray tube with usage tracking |

All risk controls must be recorded in the **Risk Management File** (ISO 14971:2019) and demonstrated to achieve compliance with the relevant GSPR clauses.

---

### 6. Human‑Escalation Triggers  

| Trigger | When it occurs | Required human action |
|---------|----------------|-----------------------|
| **Unresolved classification ambiguity** (e.g., SaMD risk class unclear) | During preliminary assessment of Rule 11 applicability | Convene a classification board; obtain senior RA sign‑off before NB dossier finalisation. |
| **Missing clinical evidence for primary intended use** | If literature review yields insufficient data or no suitable equivalence study | Pause submission; plan and execute a targeted clinical investigation. |
| **Failure to meet PSUR update schedule** (≥ 2 years for Class IIb) | Approaching deadline without updated PSUR | Senior PMO must allocate resources to generate the PSUR; delay any new market activities until completed. |
| **Non‑conformity with GSPR checklist** (e.g., radiation safety test not available) | During internal gap analysis of Annex I compliance | Immediate corrective action plan; senior QA approval before proceeding to NB audit. |
| **Notified Body request for additional data** | After NB review of the technical documentation | Assign a project lead to coordinate evidence gathering; senior management must approve budget & timeline extensions. |

Each trigger should be logged in the project’s risk‑register and escalated per the company’s internal escalation matrix.

---

### 7. Peer‑Review Prompt  

> **To RA peer:** Please review the assumptions made about the device’s classification (Rule 10 for the X‑ray generator, Rule 11 for the SaMD) and the suggested conformity‑assessment routes. Confirm that all MDR citations are appropriate and identify any jurisdiction‑specific gaps—particularly concerning the latest amendments introduced by Regulation (EU) 2023/607 or any national transposition nuances that may affect PMS/PMCF obligations.

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
- [x] Human correction needed

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

### kb-eval-20261106-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "74646c501b8f9a06", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `74646c501b8f9a06`
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

> **Regulatory Draft – PMS / PMCF Planning (MDR 2017/745)**  

---

### 1. Scope & Current Knowledge  
*The source material provides only generic procedural references (e.g., “Article 61, MDR Annex XIV”, “MDR Art. 87”) and no concrete device description.*  
Consequently the classification, conformity‑assessment route, and evidence base **cannot be finalised** until the following product‑specific information is supplied by the manufacturer.

---

### 2. Required Information from the Manufacturer  

| Item | Why it is needed (regulatory basis) | Missing? |
|------|--------------------------------------|----------|
| **Intended purpose / indication(s)** | Drives classification under Art 51 + Annex VIII; defines clinical evaluation scope (Annex XIV Part A). | ✔︎ – not in source |
| **Device description & principle of operation** | Needed to map to a specific rule (e.g., Rule 9‑11, Rule 17) and to identify if the device is active, invasive, implantable, measuring, sterile, etc. | ✔︎ |
| **User group (patient vs health‑professional, lay‑person)** | Affects GSPR §22 & classification nuances. | ✔︎ |
| **Risk class determination** (rule number) | Determines which conformity‑assessment route applies (Art 52). | ✔︎ |
| **Manufacturing process & materials** | Required for Annex II §§2–3 and risk‑control measures (§4‑8 GSPR). | ✔︎ |
| **Labeling & IFU content** | Must satisfy Annex I §23; influences PMS data capture. | ✔︎ |
| **Status of UDI allocation** (UDI‑DR, EUDAMED entry) | MDR Art 27/28; source mentions “UDI 포털”, but the actual device identifier is required. | Partial – only generic portals listed |
| **Authorized Representative details** (if non‑EU manufacturer) | Required by Art 11 for all devices placed on the EU market. | ✔︎ – reference to AR in source, but no data |
| **Existing clinical data / literature** | Basis for CER (Annex XIV Part A) and/or justification of equivalence. | ✔︎ |
| **Planned PMCF activities** (study design, endpoints, timeline) | Required by Annex XIV Part B; feeds PSUR/PMCF report. | ✔︎ |
| **Post‑market surveillance (PMS) system description** | MDR Art 83 (system), Art 84 (plan). | ✔︎ – only generic mention of vigilance (Art 87). |
| **Sales volume & user population estimate** | Needed for PSUR content (Art 86 (1)(c)). | ✔︎ – not provided |

*Until the above items are supplied, the regulatory pathway remains “to be determined”.*

---

### 3. Preliminary Classification Approach  

1. **Apply Article 51 + Annex VIII sequentially** – the highest‑scoring rule determines the class (source [2]).  
2. **Use MDCG Manual on Borderline and Classification (v2.1.1, Sep 2023)** for ambiguous cases (source [2] notes this manual).  

> *If the device is an active therapeutic system delivering energy → likely Rule 9 (class IIa/IIb).  
> If it is diagnostic software influencing treatment decisions → Rule 11 (class IIa/IIb/III).  
> If it is a sterile, measuring instrument → apply Rules 1‑4 for Class Is/Im.  

*The exact rule number can only be assigned after the intended purpose and technical characteristics are known.*

---

### 4. Conformity‑Assessment Route (once class is fixed)

| MDR Class | Reference (Art 52) | Required NB involvement | Typical route |
|-----------|-------------------|------------------------|---------------|
| **I** (non‑sterile, non‑measuring) | Art 52(7) – self‑declaration | No NB | Technical documentation (Annex II) + EU DoC (Art 19/Annex IV) |
| **Is / Im / Ir** | Art 52(7) – limited NB scope | Yes (NB for sterile/measuring/reusable aspects only) | Annex IX Chapters I & III or Annex XI Part A |
| **IIa** | Art 52(6) | Yes | Annex IX (QMS + technical‑doc assessment) *or* Annex II/III + Annex XI §10 |
| **IIb** | Art 52(4) | Yes | Annex IX (full QMS + doc assessment) *or* Annex X + Annex XI |
| **III** | Art 52(3) | Yes | Annex IX (full assessment) *or* Annex X + Annex XI |

> The specific route will be confirmed after the class is known.

---

### 5. Evidence Package Required for Submission  

1. **Technical Documentation** – Annex II §§1‑6 (device description, design & manufacturing, GSPR compliance, risk management, verification & validation).  
2. **EU Declaration of Conformity** – Art 19; content per Annex IV.  
3. **Clinical Evaluation Report (CER)** – Annex XIV Part A; must be kept current (Art 61).  
4. **PMCF Plan & PMCF Evaluation Report** – Annex XIV Part B.  
5. **Post‑Market Surveillance (PMS) System** – Art 83; PMS plan – Art 84.  
6. **Periodic Safety Update Report (PSUR)** for classes IIa/IIb/III – Art 86 (frequency: ≤2 yr for IIa/IIb, annually for III/implantables).  
7. **Vigilance & Incident Reporting** – MDR Art 87 (source [1] mentions this).  
8. **UDI Registration in EUDAMED** – per Art 27‑28; linkage to UDI‑DR (source [1] lists “EUDAMED UDI/DEV”).  
9. **Authorized Representative Documentation** – Art 11 (source [1] refers to AR).  

*All above must be compiled in the format required by the Notified Body and uploaded to EUDAMED where applicable.*

---

### 6. Risk Management & Controls (pre‑submission)  

| GSPR § | Requirement (summary) | Typical evidence |
|--------|-----------------------|------------------|
| §3 (risk management system) | ISO 14971‑based RMF; risk analysis, evaluation, control, residual‑risk acceptability. | RMF file, risk‑control measures matrix |
| §4 – §8 | Demonstrate that identified risks are mitigated, usability errors addressed, device lifetime defined, transport/storage safety ensured, benefit–risk balance favourable. | Verification & validation reports, usability engineering (IEC 62366‑1), reliability data |
| §16 (radiation) *if applicable* | Protection against ionising radiation; compliance with IEC 60601‑2‑54/28/44 as appropriate. | Test reports, shielding calculations |
| §17 – §19 (software & active devices) | Secure software lifecycle (IEC 62304), safety functions documented, active implantable considerations. | Software development file, firmware validation |

*If any of the above GSPR sections cannot be demonstrated with current documentation, a gap must be recorded and mitigated before NB assessment.*

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Missing intended purpose / device description** | Pause classification; request detailed product dossier from manufacturer. |
| **No clinical data or literature review** | Escalate to Clinical Evaluation Lead – initiate literature search or plan equivalence study. |
| **Absence of PMCF plan** (or unclear endpoints) | Notify Project Manager – develop a PMCF protocol compliant with Annex XIV Part B. |
| **PMS system not defined** | Raise with Quality/Regulatory for Art 83/84 compliance; prepare PMS SOPs. |
| **UDI not allocated in EUDAMED** | Escalate to Regulatory Operations – complete UDI registration before market entry. |
| **Unclear classification after rule mapping** | Seek advice from Competent Authority or consult MDCG Manual (v2.1.1). |
| **Evidence gaps in risk management (e.g., no usability testing)** | Trigger Risk Management Review; involve Usability Engineer. |
| **NB contract not identified for Class IIa‑III** | Initiate NB selection process; document justification. |

When any of the above triggers are hit, the responsible team member must log a **“Regulatory Open Issue”** in the project tracker and notify the RA lead for resolution before any submission can be compiled.

---

### 8. Peer‑Review Prompt  

> *Colleague, please review the assumptions made about classification pathways and evidence requirements. In particular: (a) verify that the referenced MDCG Manual version (v2.1.1, Sep 2023) is the latest guidance for borderline cases; (b) confirm whether any additional EU‑specific clinical‑investigation obligations (Art 62–63) might apply given the device’s expected class; and (c) identify any jurisdiction‑specific gaps that could arise from the Korean references present in the source (e.g., “의료기기법 §31”).*  

--- 

**End of Draft**.

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
- [x] Human correction needed

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

### kb-eval-20261106-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6278a1bc79ba23a6", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `6278a1bc79ba23a6`
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

> **Regulatory Draft – X‑ray Imaging System (diagnostic radiology)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Reference |
|------|------------|
| **MDR Rule** | **Rule 10** – “Active devices for diagnosis and monitoring that emit ionising radiation” (Annex VIII, rule 10) |
| **Resulting Class** | **Class IIb** (active X‑ray source dominates the classification) |
| **Applicable Art. 52 paragraph** | **Art. 52(4)** – devices of class IIb must follow either **Annex IX** (full QMS + technical‑documentation assessment) *or* **Annex X + Annex XI** (type‑examination plus production conformity verification). |
| **Suggested route for this project** | **Annex IX** – enables a single‑step audit of the Quality Management System (ISO 13485:2016) together with the complete technical documentation. |

---

### 2. Minimum Evidence Package Required for NB Submission  

| Technical Documentation Section (Annex II §1‑6) | Required artefact(s) | MDR citation |
|-----------------------------------------------|----------------------|--------------|
| **Device description & intended purpose** | Detailed device summary, labeling, indications, contraindications, user environment | Annex II §1; GSPR mapping (§3‑9) |
| **Manufacturer information** | Legal entity, address, UDI system set‑up (EUDAMED), PRRC appointment | Art. 10(9); Art. 33‑39 (EUDAMED) |
| **Design & manufacturing information** | Design drawings, bill of materials, manufacturing process flow chart, verification & validation reports (including IEC 60601‑2‑54 compliance for radiography) | Annex II §3; ISO 14971:2019 risk management integration |
| **General Safety & Performance Requirements (GSPR) mapping** | Completed GSPR checklist (F‑MDR‑TD‑CHK‑001 as per source [1]) with justification of conformity | Annex I §§1‑23; source [1] – “GSPR 적합성 보고서” |
| **Benefit–risk analysis & Risk Management File (RMF)** | ISO 14971:2019 risk management report, residual‑risk evaluation, risk control measures for radiation exposure (§16), electrical safety (§20) and software usability (§17) | Annex I §3; ISO 14971 reference |
| **Verification & Validation (V&V)** | Test reports (IEC 60601‑1, IEC 60601‑2‑54), performance testing, sterility/cleanliness if applicable, software verification (IEC 62304) | Annex II §5 |
| **Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data from comparable devices, post‑market clinical follow‑up (PMCF) plan & results (Annex XIV Part A) | Annex XIV Part A; source [1] – “임상평가 보고서(CER) 작성·갱신” |
| **Post‑Market Surveillance (PMS) Plan** | PMS system description, proactive activities, periodic safety update report (PSUR) schedule (Art. 84) | Art. 84; source [1] – “PMS 계획서 작성” |
| **PMCF Plan & Report** | Detailed PMCF study protocol, data collection tools, interim analysis, final evaluation (Annex XIV Part B) | Annex XIV Part B |
| **Declaration of Conformity (DoC)** | Signed DoC meeting Art. 19 content requirements (Annex IV) and referencing the applicable assessment route (Annex IX) | Art. 19; Annex IV |
| **EUDAMED Registration Records** | UDI‑DI, device identifiers, manufacturer & authorised representative entries, SN/lot traceability | Art. 33‑39 |

---

### 3. Gaps Identified in the Current Source Material  

| Missing / Incomplete Item | Why it is required | Impact on NB submission |
|----------------------------|--------------------|--------------------------|
| **Detailed device description & intended use statement** (incl. indication, patient population) | Basis for classification and GSPR fulfilment | Cannot confirm Rule 10 applicability; Classification may be challenged |
| **Labeling and IFU details (Annex I §23)** | Mandatory for conformity assessment & user safety | Lack will trigger NB request for additional documentation |
| **Quantitative risk assessment results** (e.g., estimated radiation dose, safety factors) | Needed to demonstrate compliance with GSPR §§16‑20 and ISO 14971 residual‑risk acceptance | NB may reject the RMF as incomplete |
| **Clinical data summary & justification of equivalence** | Required for CER under Annex XIV Part A | Absence will prevent finalisation of the CER |
| **PMCF methodology (sample size, follow‑up duration, endpoints)** | Needed to satisfy Art. 61/62 updates and Annex XIV Part B | Without it, PSUR cannot be compiled correctly |
| **PMS plan specifics (data sources, trigger thresholds, reporting cadence)** | Art. 84 demands a documented PMS system | NB will mark the PMS plan as insufficient |
| **UDI‑DI allocation & EUDAMED registration status** | Mandatory for market entry under Art. 33‑39 | Missing leads to non‑compliance with traceability obligations |
| **PRRC (Person Responsible for Regulatory Compliance) appointment evidence** | Required by Art. 10(9) | NB will request proof of PRRC competency |
| **Verification & Validation test reports against IEC 60601‑2‑54 and IEC 62304** | Demonstrates conformity with essential safety requirements | Absence is a critical non‑conformity |

---

### 4. Recommended Risk Controls (aligned to GSPR)

| Hazard | Relevant GSPR § | Control measure(s) |
|--------|------------------|--------------------|
| **Ionising radiation exposure** (excess dose, accidental emission) | § 16 (Radiation protection) | - Engineering controls: interlocks, automatic shut‑off, dose‑monitoring sensors.<br>- Administrative: training, SOPs for beam activation.<br>- Verification: compliance with IEC 60601‑2‑54 radiation safety tests. |
| **Electrical shock / fire** | § 20 (Mechanical & thermal risks) | - Dual‑redundant earth‑grounding, leakage‑current testing (IEC 60601‑1).<br>- Protective enclosure, temperature monitoring. |
| **Software malfunction leading to diagnostic error** | § 17 (Electronic programmable systems) | - IEC 62304 compliant software life‑cycle.<br>- Usability engineering per IEC 62366‑1.<br>- Fail‑safe mode & alarm functions. |
| **User misuse / use‑error** | § 5 (Use‑error risks) | - Human factors analysis, clear IFU graphics.<br>- Training program for operators.<br>- Physical keying / device lockout to prevent unintended operation. |
| **Mechanical failure of moving parts (e.g., collimator)** | § 20 & § 22 (Lay‑person use) | - Robust design verification, periodic maintenance schedule, clear user warnings. |

All controls must be documented in the **Risk Management File** and linked to the corresponding GSPR items throughout the technical documentation.

---

### 5. Human‑Escalation Triggers  

| Trigger condition | Action required (who) |
|-------------------|-----------------------|
| **Incomplete device description / intended use** | Senior RA Lead must obtain a formal specification sheet from R&D before any classification can be finalised. |
| **Missing or outdated CER** | Clinical affairs must deliver an updated CER (including state‑of‑the‑art literature) within 10 working days; escalation to Head of Clinical when data gap persists >2 weeks. |
| **Absence of PMCF plan details** | PMCF coordinator must draft a full protocol; project manager escalates to RA Director if not supplied within the next sprint. |
| **No PRRC appointment evidence** | Compliance officer must verify PRRC qualification; escalation to Quality Manager if unresolved before NB audit scheduling. |
| **EUDAMED registration incomplete (UDI, device class)** | IT & regulatory data‑management team to complete entries; delay >5 business days triggers notification to the Regulatory Steering Committee. |
| **Significant residual risk identified without adequate mitigation** | Risk manager must present a corrective‑action plan; if unresolved within 15 days, escalation to Chief Technical Officer (CTO). |

---

### 6. Peer‑Review Prompt  

> *@RA‑Peer:* Please review the assumptions made regarding:
> - The classification of the X‑ray system solely on Rule 10 without explicit device specifications.
> - The completeness of the evidence list given that the source material only references internal process steps (F‑MDR‑TD‑CHK‑001) and a generic MDR guide.
> - Any jurisdiction‑specific items that may have been omitted (e.g., UDI‑DI format, specific IEC 60601‑2‑54 test reports).
> Your feedback on missing artefacts or alternative assessment routes (Annex X + XI) is welcome.

---

**Regulatory Judgment**  

- The device under review is **Class IIb** per MDR **Rule 10**; the appropriate conformity‑assessment route is **Art. 52(4) – Annex IX** (or optionally Annex X + XI).  
- A full technical documentation package as enumerated in Section 2 must be assembled, with particular attention to the gaps highlighted in Section 3.  
- Until those gaps are closed and the required artefacts (CER, PMCF plan, PMS plan, RMF, UDI registration, PRRC evidence) are available, **submission to a Notified Body cannot proceed**.  

Escalation points are listed in Section 5; they must be monitored continuously to avoid delays in the NB audit schedule.

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 식별자 오배치 3건 — ① V&V→Annex II §5(정확히는 §6, §5는 benefit-risk/RMF) ② PSUR→Art. 84(정확히는 Art. 86) ③ PRRC→Art. 10(9)(정확히는 Art. 15, 10(9)는 QMS). 본론(Rule 10→IIb·52(4)·Annex IX/X+XI)은 정확.

**Source Excerpts**

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `1072636411107495596`

> --- doc-id: EU_MDR_2017_745 title: "EU MDR — Regulation (EU) 2017/745 요약 및 적용 지침" type: Guide version: v0.3.1 status: draft category: 01_법규_규제 purpose: "EU MDR 2017/745 핵심 요구사항, 2026 일정, 기술문서 구성 및 X-ray 시스템 적용 지침" applicable: [EU MDR 2017/745, EU MDR GSPR Annex I, ISO13485:2016, ISO14971:2019, IEC 62304, IEC 60601-1, IEC 60601-2-54, UDI] forms: [F-MDR-TD-CHK-001] related-docs: - GSPR_정합표준_매핑표 - GSPR_체크리스트_v0.2_템플릿 - PRRC_역할_및_한미_대응자_매핑 - EU_AI_Act_MDR_중첩적용_매핑 - ISO13485_2016_요약 - SOP-CC-001 - SOP-PSUR-001 - SOP-FSCA-001 - TF-TD-001 related-issues: [4, 5, 22, 33, 989] owner: RA/QA Lead last-review: 2026-07-23 review-due: 2027-06-09 --- # EU...

### kb-eval-20261106-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "cee441505555d62e", "source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md", "source_hash": "62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `cee441505555d62e`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) / Post‑Market Clinical Follow‑up (PMCF) Planning  
(aimed at a generic medical device that is to be placed on the EU market under MDR 2017/745)**  

---

### 1. Device Overview – information gaps
| Item | What is required | Current status (based on supplied source) |
|------|------------------|-------------------------------------------|
| **Intended purpose / indication** | Precise clinical claim, patient population, mode of action | *Not provided* – needed to select a classification rule (Annex VIII). |
| **Device family & variants** | Model‑level identification (UDI‑DI) and versioning (Basic UDI‑DI) | Only the structure of the UDI is described in the source (see §3‑2‑A); actual identifiers are missing. |
| **Risk classification** | Apply the appropriate rule(s) from Annex VIII (e.g., Rule 9, 10, 11, 17 etc.) and determine Class I–III. | *Not provided* – cannot decide which conformity‑assessment route applies (Art. 52). |
| **Manufacturing / QMS scope** | ISO 13485:2016‑compliant quality management system, plus any sterile/measuring/reusable aspects that would invoke a limited NB audit (Art. 52(7)). | Not mentioned. |
| **Clinical evidence already available** | Clinical Evaluation Report (CER) – Annex XIV Part A – or an existing PMCF study. | No CER/PMCF data cited. |

*Action*: Obtain the above missing items before any further regulatory pathway work can be finalised.

---

### 2. Classification & Conformity‑Assessment Route (once intended use is known)

| Determined Class | Relevant MDR provision (Art. 52) | NB involvement |
|------------------|----------------------------------|----------------|
| **Class I** (non‑sterile, non‑measuring, non‑reusable surgical) | Art. 52(7): self‑declaration – technical documentation (Annex II & III) + EU Declaration of Conformity (Art. 19, Annex IV). *No NB* required. |
| **Class Is / Im / Ir** | Art. 52(7): limited NB audit for sterile/measuring/reusable aspects – Annex IX Chapters I & III or Annex XI Part A (limited scope). |
| **Class IIa** | Art. 52(6): full QMS + technical‑documentation assessment by NB (Annex IX Chapters I & III + §4) *or* alternative route via Annex II + III plus production conformity verification (Annex XI §10). |
| **Class IIb** | Art. 52(4): full QMS + technical‑documentation assessment by NB (Annex IX Chapters I & III + §4) *or* type‑examination (Annex X) together with production conformity verification (Annex XI). |
| **Class III** | Art. 52(3): full QMS + technical‑documentation assessment by NB (Annex IX) *or* type‑examination (Annex X) + production conformity verification (Annex XI). |

> **Citation:** MDR 2017/745, Art. 52 (classification‑specific routes); Annex VIII (rules); Annex IX, X, XI (assessment routes); Art. 19 & Annex IV (EU Declaration of Conformity).

*Note*: Until the classification is resolved, none of the subsequent PMS/PMCF obligations can be timed correctly.

---

### 3. Post‑Market Surveillance Requirements (class‑dependent)

| Requirement | MDR provision | What must be produced | When / cadence |
|-------------|----------------|----------------------|---------------|
| **PMS system** | Art. 83 | Documented organisational & procedural framework for continuous PMS (incl. vigilance, trend reporting). | Ongoing from market entry. |
| **PMS plan** | Art. 84 | Detailed description of data‑collection methods, sources, responsibilities, and analysis procedures. Must reference the risk management file (Annex I §3) and clinical evaluation update cycle. | At least once before first device placed on market; reviewed regularly. |
| **PMS report (Class I)** | Art. 85 | Summarised findings of PMS activities, any corrective actions, trend analysis. | Annually. |
| **Periodic Safety Update Report – PSUR (Classes IIa‑III)** | Art. 86(1) & (2) | • Conclusions of benefit–risk determination.<br>• Main PMCF findings.<br>• Sales volume & user population estimate. | Class IIa/IIb: every **2 years**; Class III / implantable: at least **annually**. |
| **PMCF plan & evaluation report** | Annex XIV Part B | Forward‑looking clinical follow‑up plan (study design, endpoints); after execution, a PMCF evaluation report summarising results and impact on risk‑benefit. | Integrated into PMS plan; updated as new data become available. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (kept current under Art. 61) | State‑of‑the‑art literature review, clinical data summary, benefit–risk analysis. | Updated whenever new clinical information arises or at least every 2 years for most devices. |
| **Vigilance / Incident reporting** | Art. 87 & Art. 88 (trend reporting) | Immediate notification of serious incidents and field safety corrective actions; periodic trend reports to the Competent Authority. | As required by severity; trend reports annually. |

> **Citation:** MDR 2017/745, Arts 83‑88; Annex XIV Part A/B; Art. 61 (CER update); Art. 19 & Annex IV (DoC).

---

### 4. Evidence Package Required for PMS / PMCF

| Evidence Item | Source / Standard | Reason for inclusion |
|---------------|-------------------|----------------------|
| **Risk Management File (RMF)** – updated to include post‑market risk data. | ISO 14971:2019 (Annex I §3) | Demonstrates continuous risk assessment in line with GSPR §3‑9. |
| **Updated Clinical Evaluation Report** (or interim updates). | Annex XIV Part A; Art. 61 | Shows that clinical evidence remains sufficient for the intended purpose. |
| **PMCF Study Protocol** (if required) and final evaluation report. | Annex XIV Part B | Provides prospective clinical data to confirm safety & performance, especially for higher‑risk classes. |
| **PMS Plan & Report / PSUR** (depending on class). | Art. 84, 85, 86 | Documents systematic collection/analysis of post‑market data and conclusions. |
| **Vigilance records** – serious incident notifications, field safety corrective actions. | Art. 87; national competent authority portals | Required for trend analysis and regulatory reporting. |
| **EUDAMED registration data** – Actor (SRN), Device (UDI/DEV) modules completed with Basic UDI‑DI & UDI‑DI. | Source excerpt §3‑2‑A/B (structure of UDI); MDR Art. 33‑39 (EUDAMED obligations). | Enables searchable public transparency and links to PMS data. |
| **Labeling / IFU updates** reflecting any post‑market changes. | Annex I §23; Art. 10(9) (QMS) | Ensures users receive current safety information. |

---

### 5. Risk Controls Related to Post‑Market Activities

1. **Integrate PMS outputs into the risk management process** – each identified trend or incident must be assessed for residual risk and, where necessary, trigger risk‑control measures (Annex I §3‑9).  
2. **Implement corrective actions** (design changes, updated labeling, user training) as soon as a safety issue is confirmed (Art. 83/84).  
3. **Maintain traceability of UDI to batch/lot numbers** – required for rapid field actions (see UDI structure in source §3‑2‑A).  
4. **Usability engineering updates** where post‑market data reveal use‑error hazards (Annex I §5; IEC 62366‑1:2020).  

---

### 6. Missing Information – What Must Be Obtained Before Proceeding

| Gap | Why it matters | Suggested source/action |
|-----|----------------|--------------------------|
| **Exact intended medical purpose & indication** | Drives classification rule (Annex VIII) and clinical evidence scope. | Obtain from product specification / marketing dossier. |
| **Device class determination** | Determines conformity‑assessment route, NB involvement, PSUR cadence, PMCF necessity. | Apply Annex VIII rules once purpose is known. |
| **UDI‑DI & Basic UDI‑DI values** (including GS1, HIBCC or ICCBBA code) | Required for EUDAMED Module 2 registration; enables traceability. | Request from labeling team / UDI issuing agency. |
| **Existing clinical data (pre‑market studies, literature)** | Basis of initial CER and informs whether PMCF is mandatory. | Compile all available clinical investigations and SOTA literature. |
| **QMS scope & certification status** (ISO 13485:2016) | Determines if NB audit will be needed for the selected route. | Verify current ISO 13485 certificate. |
| **Planned PMS data sources** (registries, complaints database, post‑market studies) | Must be described in PMS plan (Art. 84). | Draft a data‑collection matrix. |

*If any of these items remain unavailable, the regulatory submission cannot advance to the next stage.*

---

### 7. Human‑Escalation Triggers

| Situation | Trigger for escalation to senior RA / management |
|-----------|---------------------------------------------------|
| **Unresolved classification** after three attempts to map intended use → *Escalate* to senior RA for rule interpretation (Annex VIII) and possible consultation with the Competent Authority. |
| **Missing or incomplete UDI data** that prevents EUDAMED Module 2 completion before market launch → *Escalate* to project lead & legal for timeline impact. |
| **PMS plan not aligned with device class** (e.g., PSUR cadence set incorrectly) → *Escalate* to QA/QMS manager for corrective planning. |
| **No clinical evidence available** for a Class IIb/III device → *Escalate* to development team to initiate a PMCF study or obtain additional pre‑market data. |
| **Adverse trend identified** in vigilance that may affect the benefit–risk conclusion → Immediate escalation to safety officer and, if serious enough, trigger field safety corrective action per Art. 87. |

---

### 8. Summary Judgment (to be confirmed after missing items are supplied)

* Pending acquisition of intended purpose, classification rule, UDI identifiers, and existing clinical data, the device will require:  

- A **full QMS‑based conformity assessment** (Annex IX) for Classes IIa–III, or a **self‑declaration** (Art. 52(7)) if Class I.  
- **PMS system & plan** per Arts 83‑84, with a **PSUR** (Art. 86) for any device of Class IIa or higher.  
- A **PMCF plan and evaluation report** (Annex XIV Part B) where the benefit–risk conclusion cannot be supported solely by pre‑market evidence.  

All documentation must be uploaded to **EUDAMED** (Actor SRN, Device UDI/DEV modules) in line with the timelines indicated in the source (module 5 expected Q2 2027).  

The next concrete step is to collect the missing information listed in Section 6; once obtained, a definitive classification and conformity‑assessment route can be confirmed, allowing finalisation of the PMS/PMCF package.  

---  

**Peer Review Prompt**

> *Could another RA specialist review the assumptions made about the need for a PMCF plan (Annex XIV Part B) given the unknown clinical evidence level? Are there any MDR provisions or recent guidance that might allow an exemption or alternative approach for certain Class IIa devices, and have we fully captured the EUDAMED registration dependencies outlined in the source?*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> [최종(shadow 부분수용) 3→2] 주기 정밀도 결함 3건 — ① Art.85 PMS보고서 "Annually"(원문 "as necessary") ② Art.88 트렌드보고 "annually"(원문: 유의미한 증가 시) ③ CER "at least every 2 years"(MDR 고정 주기 아님). 단 shadow의 Art.52 매핑·PSUR IIb=연간 이의는 원문/KB 확정값과 불일치 — 기각(5회차 연속 shadow 오류).

**Source Excerpts**

1. Chunk `1048620351506847107`

> ### 5-A. 데이터베이스 등록 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR (EU) | |---|---|---|---| | 등록 DB | GUDID (FDA UDI DB) | UDI포털 (mfds.go.kr) | EUDAMED | | 의무화 시점 | 등급별 단계적 완료 | 2025 기준 진행 중 | 2026-05-28 (4개 모듈) | | 경제주체 등록 | FDA Establishment Registration (21 CFR 807) | 의료기기 제조업 허가 | SRN (Actor Module) | | 기기 등록 | 510(k)/PMA cleared → GUDID | 허가/인증/신고 후 UDI포털 | EUDAMED UDI/DEV | | UDI 발급기관 | GS1, HIBCC, ICCBBA | GS1(의무), HIBCC(가능) | GS1, HIBCC, ICCBBA | | Vigilance 보고 | eMDR (FDA MedWatch) | 이상사례 포털 | Module 5 (~Q2 2027) |

2. Chunk `1068273778649251618`

> ### Module 2: UDI/Device Registration (UDI/DEV) — UDI 및 기기 등록 #### 3-2-A. UDI 구조 ``` UDI = UDI-DI (고정) + UDI-PI (가변) Basic UDI-DI (레거시 식별자) └── UDI-DI (모델별) └── UDI-PI (생산 로트/일련번호) ``` - **Basic UDI-DI**: 동일 기기 군/버전을 식별하는 핵심 레퍼런스. EUDAMED에서 Globally Unique해야 함. - **UDI-DI**: 특정 버전/제품 모델 식별. - 발급 기관: GS1, HIBCC, ICCBBA 중 선택. #### 3-2-B. 등록 데이터 항목 (주요)

## ra_kr

### kb-eval-20261106-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "fb9280225f6ebcba", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "00026234f8ec1153306309dc7c82b355b5fdfc4d7a5de00dbd5247374b13eccb"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `fb9280225f6ebcba`
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

> **Regulatory Draft – Digital Medical Device Classification & Submission for X‑ray System under 디지털의료제품법**

---

### 1. Scope of the Assessment
The product family consists of:

| Component | Likelihood of being a “디지털 의료기기” (digital medical device) according to the source table |
|-----------|------------------------------------------------------|
| Generator firmware | X – not applicable (hardware control only, no network) |
| Detector firmware   | △ – may become applicable if network‑enabled |
| Acquisition Workstation Software | ○ – standalone software with network connectivity and AI capability → **SaMD** |
| Post‑processing / AI analysis module | ○ (if AI is used) → **SaMD + AI** |
| DICOM transmission / PACS interface | △ – communication function; needs boundary review |

The assessment therefore focuses on the **Acquisition Workstation SW** and the **AI analysis module**, which are classified as Software‑as‑a‑Medical‑Device (SaMD) with possible AI functions.

---

### 2. Korean Classification & Submission Route  

| Korean grade | Typical product group | Applicable route for this X‑ray system |
|--------------|----------------------|----------------------------------------|
| **1등급**    | Low‑risk, non‑critical | 신고 (notification) – not applicable here |
| **2등급**    | Moderate risk, limited function | 인증 (technical‑document review by MFDS‑designated 심사기관) – not appropriate for diagnostic imaging with AI |
| **3등급·4등급** | High‑risk / therapeutic or diagnostic devices | 허가 (full MFDS approval) – **recommended** |

*Rationale*: Diagnostic X‑ray imaging combined with AI analysis is considered high risk under the Korean Medical Device Act and the 디지털의료제품법. The default grade for such SaMD is **4등급**, requiring a **허가** submission.

> **Citation**: No specific 고시 or 조항 number is supplied in the source material – verify separately against 「의료기기 품목 및 품목별 등급에 관한 규정」.

---

### 3. Required Evidence for 허가 (4등급)

| Category | Korean requirement | International counterpart | Notes |
|----------|-------------------|---------------------------|-------|
| **Risk Management** | ISO 14971 (2019) risk analysis & mitigation file, with Korean translation of risk acceptability criteria | FDA 21 CFR 820.30; EU MDR Annex I | Must address AI‑related hazards and cybersecurity risks |
| **Software Lifecycle** | IEC 62304 (2006+A1:2015) compliance – software development plan, verification/validation reports | FDA’s “Software Precertification” guidance; EU MDCG 2020‑16 | Include version control & change management |
| **Cybersecurity / SBOM** | MFDS 보안지침 **제16조** (SBOM 관리) – submission of a Software Bill of Materials in SPDX 2.3 or CycloneDX 1.5 format; RA‑07 항목 checklist | FDA 524B post‑market plan; EU MDR technical documentation Annex II (NTIA 7 elements) | The SOP‑SBOM‑001 v0.1 already satisfies the “상위 호환 설계” |
| **Clinical Evaluation** | Local clinical data or foreign CER accepted under MFDS mutual‑acceptance policy (non‑clinical GLP data only); Korean language summary of performance | FDA 510(k) predicate & PMA; EU MDR clinical evaluation report | If foreign CE/ FDA clearance is used, confirm that MFDS accepts the specific CER (requires case‑by‑case verification) |
| **KGMP Facility Certification** | Manufacturing site for hardware must hold KGMP certification (medical device law 제28조) | ISO 13485 (2016) – QMSR not applicable in Korea | Applies to generator, detector, and any hardware components |
| **Labeling & IFU** | All labeling, box labels, and Instructions for Use must be in Korean; include CE/ FDA symbols only if expressly permitted | FDA labeling requirements; EU MDR labeling | Include “디지털 의료기기” designation where appropriate |
| **Post‑Market Surveillance (PMS)** | MFDS PMS plan per the “보안 지침 제16조” and standard surveillance activities (시판후조사) | FDA Post‑Marketing Requirements; EU MDR PSUR/PMCF | Must reference SBOM update schedule |

---

### 4. Evidentiary Gaps Identified

| Missing Item | Why it is needed | Suggested source/action |
|--------------|-----------------|-------------------------|
| **Exact Korean grade (1~4등급) determination** | Required to select 허가 pathway | Conduct official grading check via MFDS “품목 및 등급 확인” portal |
| **Local clinical performance data for AI module** | MFDS may require domestic evidence for diagnostic AI | Design a pilot study in Korean institutions; summarize results in Korean |
| **Korean language IFU and labeling set** | Mandatory for market entry | Translate existing documents, obtain certified translation |
| **KGMP certification proof for hardware manufacturing site** | Required for any device containing regulated hardware | Apply for KGMP audit or confirm existing certificate validity |
| **Detailed SBOM for all firmware components (including detector firmware if network‑enabled)** | MFDS 보안지침 제16조 demands complete SBOM | Generate SPDX 2.3 file covering all binaries; map to RA‑07 항목 |
| **AI algorithm change‑management plan** (model updates) | To satisfy post‑market cybersecurity & AI governance | Draft SOP describing version control, re‑validation triggers, and notification process |

---

### 5. Risk Controls & Mitigations

1. **Hazard Identification (ISO 14971)** – list hardware failures, software bugs, AI misdiagnosis, data leakage.
2. **Cybersecurity Controls** – implement network segmentation, authentication, regular vulnerability scanning; maintain SBOM for traceability of third‑party components.
3. **AI Transparency Measures** – provide explainable output, human‑in‑the‑loop requirement, performance thresholds; document training data provenance.
4. **Human‑Oversight Triggers** – define situations where AI output must be reviewed by a qualified radiologist before clinical decision (e.g., confidence < 90 % or detection of novel pathology).
5. **Post‑Market Update Process** – schedule SBOM revision at each software release; submit change notification to MFDS per 보안지침 제16조.

---

### 6. Human‑Escalation Triggers  

| Situation | Reason for escalation |
|-----------|-----------------------|
| Uncertainty about the **exact Korean grade (1~4등급)** | Misclassification leads to incorrect submission route |
| Lack of **local clinical evidence** for AI performance | Potential rejection or additional data request |
| Incomplete **SBOM** (missing third‑party libraries) | Non‑compliance with 보안지침 제16조 may halt approval |
| Absence of **KGMP certification** for any hardware component | Manufacturing site audit failure |
| Missing **Korean language labeling/IFU** | Regulatory breach; product cannot be marketed |
| Ambiguous **AI risk categorization** (e.g., “SaMD + AI” vs. “low‑risk software”) | May affect grade and required clinical data |
| Any **conflict between international standards** adopted (SPDX 2.3 vs. CycloneDX 1.5) without clear justification in the SBOM SOP | Needs clarification to satisfy MFDS reviewers |

When any trigger is hit, a senior RA or regulatory affairs manager must be consulted before proceeding with dossier preparation.

---

### 7. Peer‑Review Prompt  

*“Please review this draft and challenge:  
- The assumption that the acquisition workstation and AI analysis module fall under 4등급; could they be re‑graded as 3등급 based on functional risk?  
- Whether the current evidence list sufficiently satisfies MFDS’s SBOM requirement (보안지침 제16조) or if additional artefacts are needed.  
- Any overlooked Korean‑specific obligations (e.g., mandatory conformity assessment by a designated 심사기관 for certain software modules).”*  

--- 

**End of Draft**

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> "The default grade for such SaMD is 4등급" — 소스에 등급 정보 없음(스스로 verify separately 명시), 근거 없는 default 단정. KGMP 제28조·보안지침 제16조·SPDX/CycloneDX는 소스 정확 반영.

**Source Excerpts**

1. Chunk `1055466385786976527`

> ## 1. FDA vs MDR vs MFDS — SBOM 요구사항 정합성 | 축 | 요구 시점 | 포맷 | 필수 항목 | 제출 방식 | 사후 갱신 | |----|-----------|------|-----------|-----------|-----------| | FDA (524B) | Premarket (2023-10-01 RTA 강제) | SPDX 2.3 / CycloneDX 1.5 | NTIA 7요소 + EOL + 취약점 | eSTAR 제출물 | Section 524B Postmarket Plan | | MDR (MDCG 2019-16) | Technical Documentation Annex II | 포맷 권고 없음, IMDRF N73 원칙 | NTIA 7요소 + License + Hash | NB 심사 자료 | PMS Plan/PSUR 포함 | | MFDS (2025-01-10) | 국내 허가 심사 | 권고 (SPDX/CycloneDX) | RA-07 항목 | 심사 자료 (권고) | 보안 지침 제16조 SBOM 관리 | **정합성 판정: 본 SOP-SBOM-001 v0.1은 3축 모두 수용 가능한 상위 호환 설계** - SPDX 2.3 또는 CycloneDX 1.5 채택 → FDA/MDR/MFDS 동시 만족 - NTIA Baseli...

2. Chunk `418096885713027360`

> ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 |

### kb-eval-20261106-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "f8598240ba8ac260", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f8598240ba8ac260`
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

> **Regulatory Draft for “촬영실 GUI SW” (Standalone SaMD)**  

---

### 1. Device Classification & Submission Route  
| Item | Determination | Rationale / Source |
|------|---------------|--------------------|
| **Korean grade** | *To be confirmed* – likely **2등급** or **3등급/4등급** depending on the intended clinical function (e.g., image acquisition control vs. diagnostic interpretation). | The exact grade must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS_인허가_상세가이드.md §2). No specific grade appears in the provided excerpts. |
| **Submission track** | • If **2등급** → **인증** (technical‑documentation review by an MFDS‑designated 심사기관). <br>• If **3등급·4등급** → **허가** (full MFDS approval). | Korean pathway follows the hard‑classification rule set out in the MFDS guidance. |

*Human‑escalation trigger:* If the intended use suggests a diagnostic or therapeutic claim that pushes the device into 3등급/4등급, senior RA must confirm grade and prepare for 허가.

---

### 2. Core Regulatory Evidence Required  

| Evidence Category | Specific Items (Korean requirement) | Mapping to International Standards / Guidance |
|-------------------|--------------------------------------|------------------------------------------------|
| **Quality Management System** | KGMP 인증 (의료기기법 제28조) – facility‑level certification; QMS procedures must incorporate **ARR (Applicable Regulatory Requirements)** as described in the source. | ISO 13485 (2016) – required but insufficient alone (see source §820.10(b)). |
| **Software Development Lifecycle** | Full software documentation bundle: SDP, SRS, SAD, SVP, SVR; conformance to IEC 62304 Safety Class C. | IEC 62304 (2006+A1:2015) §8.1 (software validation). |
| **Cybersecurity** | Threat model, SBOM, PCCP (Pre‑Market Cybersecurity Plan) as per MFDS 사이버보안 가이드라인 2025. | FDA 524B (PCCP); MDCG 2019‑16 Rev.1; EU AI Act references for high‑risk AI/ML. |
| **AI/ML Component (if applicable)** | Documentation of algorithm change management, performance monitoring plan, and pre‑market assessment per 디지털의료제품법. | FDA PCCP (2024‑12‑03 Final); EU AI Act Art.43(4) – note future 2027 requirements. |
| **Clinical Evaluation** | Clinical evaluation report (CER) or Korean clinical data supporting safety & performance, especially if classified as 3등급/4등급. | MFDS accepts foreign CER when aligned with local risk profile – separate from OECD‑MAD (non‑clinical only). |
| **UDI / Labeling** | Korean language labeling, IFU, and UDI assignment per MFDS 고시 (no specific number in source – verify separately). | 21 CFR 830 (UDI) for reference only; not sufficient alone. |
| **Post‑Market Surveillance (PMS)** | Complaint handling procedure (MFDS 보고), service record keeping, and 30‑day MDR reporting as required. | MFDS 고시 §820.35(a) & §820.35 – detailed complaint assessment. |
| **Sterilization / Re‑labeling Contracts** (if any) | Contractual QMS scope covering contract sterilizers, re‑labelers per §820.10(a). | Aligns with expanded QMSR scope in source. |

*Human‑escalation trigger:* Any missing element above (e.g., no AI/ML risk management plan when the software includes AI) must be escalated to a senior RA or the digital‑medical‑product specialist.

---

### 3. Missing Information & Gap Analysis  

| Gap | Why It Matters | Action |
|-----|----------------|--------|
| **Exact intended use & risk classification** | Determines grade (2등급 vs. 3/4등급) and submission track. | Obtain a detailed Use‑Case Description from product team; perform Korean risk classification per 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **Clinical evidence** | Required for ≥ 2등급 devices, especially if diagnostic claim. | Identify existing foreign CE/FDA clearance (if any) and evaluate acceptability under MFDS; plan local clinical study if needed. |
| **Korean‑language labeling & IFU** | Mandatory for market entry. | Draft Korean label/IFU and submit to MFDS for review. |
| **UDI assignment strategy** | UDI is now required for most devices (MFDS 고시). | Determine device identifier, register with KTR (Korea Telecom Registry), and embed in labeling. |
| **AI/ML change‑management documentation** (if AI present) | Needed to satisfy both MFDS 디지털의료제품법 and upcoming EU AI Act alignment. | Prepare algorithm version control, performance monitoring plan, and pre‑market assessment report. |
| **Cybersecurity implementation details** | Must align with MFDS 사이버보안 가이드라인 2025; insufficient documentation can delay review. | Develop threat model, SBOM, PCCP, and conduct penetration testing; retain evidence for submission. |

*Human‑escalation trigger:* If any of these gaps cannot be closed within the planned timeline, raise a risk‑based escalation to project management and senior regulatory leadership.

---

### 4. Primary Risk Controls (per IEC 62304 & KGMP)

1. **Software Lifecycle Management** – Mandatory adherence to IEC 62304 Class C processes; includes requirement management, design verification/validation, configuration management, and change control.
2. **Validation Testing** – Automated regression test suite covering all functional requirements; documented in SVR.
3. **Cybersecurity Measures** – Threat modeling, SBOM generation, PCCP implementation, regular vulnerability scanning; records stored per MFDS cyber‑security guide.
4. **AI/ML Governance** (if applicable) – Pre‑market algorithm assessment, post‑market performance monitoring, and a clear “stop‑gap” rollback plan.
5. **Complaint & Service Records** – Integrated with MFDS MDR reporting workflow; complaints evaluated for reportability within 30 days.
6. **Contractor Oversight** – QC/QA procedures extended to contract sterilizers/re‑labelers; audit rights per §820.10(a).

---

### 5. Citations  

| Type | Citation |
|------|----------|
| **Framework references (no specific identifier needed)** | ISO 13485 (2016); IEC 62304 (2006+A1:2015) §§8.1; MFDS 사이버보안 가이드라인 2025; 디지털의료제품법 (digital medical product law). |
| **Instance identifiers** | *No specific identifier (e.g., MFDS 고시 number, § clause) appears in the provided excerpts – verify separately.* |

---

### 6. Human‑Escalation Triggers Summary  

- **Uncertain Korean grade** → senior RA review before initiating submission.  
- **Missing clinical evaluation or local data** for a ≥ 2등급 claim.  
- **AI/ML functionality detected without documented risk management**.  
- **Cybersecurity evidence insufficient to satisfy MFDS 2025 guideline**.  
- **Labeling / UDI not prepared in Korean**.  
- **Contractor scope (sterilizer/re‑labeler) not covered by QMS**.  

When any trigger is hit, the case should be flagged for immediate senior regulatory oversight and possible project timeline adjustment.

---

### 7. Peer Review Prompt  

> *Colleague RA, please review the assumptions made about the device’s risk class and the adequacy of the identified evidence gaps. In particular, assess whether the mapping to MFDS cyber‑security guidance 2025 is complete, and confirm that no applicable foreign clinical evaluation (FDA 510(k) or CE) has been omitted from our evidence list.*  

--- 

*End of draft.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> ① "register with KTR (Korea Telecom Registry)" — KB 무출연 창작(국내 UDI는 GS1 의무 발급·UDI포털 등록) ② PCCP를 "Pre-Market Cybersecurity Plan"으로 오확장(같은 응답의 FDA PCCP=Predetermined Change Control Plan과 자기모순) ③ "MFDS 고시 §820.35(a)" 관할 혼입 표현(§820.35는 US CFR).

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261106-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "98d1efa0c7461f5c", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `98d1efa0c7461f5c`
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

> **Regulatory Draft – AI‑Enabled Digital Therapeutic Software (SaMD) under the 디지털의료제품법**  

---

### 1. Device Classification & Submission Route  
| Korean Grade | Typical Pathway | Likely applicability to an AI‑driven therapeutic software* |
|--------------|----------------|-----------------------------------------------------------|
| **1등급** → 신고 | Notification (신고) | Only if the device is low‑risk, non‑invasive and does not provide diagnosis or treatment advice. Unlikely for a therapeutic AI module. |
| **2등급** → 인증 | Certification by an MFDS‑designated 심사기관 (e.g., KTL, KTC) | Applies to moderate risk devices that perform basic health‑information functions. If the software only delivers educational content and does not claim clinical efficacy, 2등급 may be appropriate. |
| **3등급·4등급** → 허가 | Full MFDS approval (허가) | Required when the AI module performs autonomous diagnosis, treatment recommendation, or risk‑based patient management – typical for therapeutic SaaS that influences clinical decisions. |

\*The exact grade must be confirmed against **「의료기기 품목 및 품목별 등급에 관한 규정」** (MFDS_인허가_상세가이드.md §2).  

**Current presumption:** The AI‑based therapeutic software is a **3등급** device → submission via **허가**.  

---

### 2. Core Evidentiary Requirements  

| Requirement | Basis (framework) | Source‑derived citation* | What must be provided |
|-------------|-------------------|--------------------------|-----------------------|
| **Risk Management** | ISO 14971:2019 (risk analysis, control, residual risk evaluation) | no specific identifier found in source — verify separately | Full RM plan, hazard list, risk control measures (including AI‑specific uncertainties). |
| **Usability / Human Factors Engineering** | IEC 62366‑1:2015+A1:2020 | no specific identifier found in source — verify separately | IEC 62366‑1 기반 사용적합성 엔지니어링 계획 (see Action 2, “사용적합성 엔지니어링 계획 수립”). |
| **Cybersecurity** | MFDS 고시 “디지털의료기기 사이버보안 허가·심사 가이드라인(개정)” (2025‑01‑10) – high relevance | no specific identifier found in source — verify separately | Completion of RA‑01 ~ RA‑20 매트릭스, SBOM 관리 SOP, ongoing vulnerability monitoring. |
| **Software Bill of Materials (SBOM)** | MFDS 고시 “디지털의료기기 전자적 침해행위 보안 지침(안)” (2025‑01) – high relevance | no specific identifier found in source — verify separately | SOP‑SBOM‑001 (validated), linkage to cybersecurity matrix. |
| **AI Model Governance & Dataset Documentation** | MFDS 고시 “생성형 AI 의료기기 허가·심사 가이드라인” (2025‑01) – medium relevance | no specific identifier found in source — verify separately | SOP‑AIDATA‑001, SOP‑AIGOV‑001 covering dataset provenance, bias mitigation, model versioning. |
| **Performance Evaluation of AI Components** | MFDS “디지털의료제품법” (Digital Medical Products Act) – generic requirement for SaMD performance | no specific identifier found in source — verify separately | Validation reports for each AI component (AI_구성요소_단위_성능평가). |
| **Clinical Evaluation / Local Clinical Data** | MFDS “의료기기 임상시험 설계 가이드라인” (2024‑12) – low relevance but still required for therapeutic claims | no specific identifier found in source — verify separately | Clinical evidence package (local or acceptable foreign CER mapped per MFDS MAD policy). |
| **KGMP Facility Certification** (if device is manufactured in Korea) | KGMP (의료기기법 제28조) – mandatory for 2~4등급 | no specific identifier found in source — verify separately | Certificate of compliance, audit reports. |
| **Korean Language Labeling & IFU** | MFDS labeling regulation (K‑IFU requirements) – mandatory for all grades | no specific identifier found in source — verify separately | All user‑visible information in Korean, including risk statements and instructions. |

\*Only framework references are listed without a specific notice number because the excerpt does not contain any concrete instrument identifiers.

---

### 3. Evidentiary Gaps & Missing Information  

| Gap | Why it matters | Suggested Action |
|-----|----------------|------------------|
| **Exact intended use & indication** | Drives classification, clinical evidence scope, and risk level. | Obtain a definitive Intended Use Statement (including patient population, therapeutic purpose). |
| **Risk classification justification** | Needed for the submission dossier and to select the correct pathway. | Perform a formal risk‑class determination per MFDS 규정; document supporting analysis. |
| **Local clinical data or mapped foreign CER** | Therapeutic claims generally require Korean‑origin clinical evidence unless MFDS accepts foreign CER under its MAD policy (non‑clinical only) – separate from AI model validation. | Conduct a Korean pilot study or prepare a robust justification for using an FDA/CE‑cleared comparator, citing the latest MFDS notice on foreign clinical data acceptance (verify separately). |
| **Complete cybersecurity matrix (RA‑01 ~ RA‑20)** | Required by 2025‑01‑10 guideline; incomplete coverage may block approval. | Finalize and sign off the matrix; link each item to SOPs (SBOM, vulnerability response). |
| **Change Management Plan (CMP) linkage** | Mandatory for post‑market changes, especially AI model updates. | Integrate CMP sections with SOP‑CC‑001; include AI‑specific update procedures. |
| **Manufacturing location & KGMP status** | If any component is produced abroad, MFDS may still require domestic KGMP certification or a special import permit. | Determine manufacturing flow and secure appropriate KGMP documentation or import clearance. |
| **Korean IFU translation proof** | Non‑Korean labeling leads to non‑compliance regardless of technical dossier quality. | Prepare Korean draft IFU; conduct linguistic review by certified translator. |

---

### 4. Core Risk Controls (as reflected in the required evidence)  

1. **Cybersecurity Controls** – RA‑01 ~ RA‑20 matrix, SBOM, regular penetration testing, secure OTA update mechanism.  
2. **Usability Engineering** – IEC 62366‑1 based user‑task analysis, formative & summative usability tests with target users.  
3. **AI Model Governance** – Dataset provenance SOPs, bias assessment, model version control, explainability documentation.  
4. **Change Management** – Formal CMP covering software patches, AI retraining cycles, impact assessment before release.  
5. **Clinical Performance Monitoring** – Post‑market performance data collection (PMS) plan aligned with MFDS post‑approval surveillance requirements.  

---

### 5. Human‑Escalation Triggers  

| Trigger | Situation | Escalation Target |
|--------|-----------|--------------------|
| **Unresolved classification uncertainty** | Unable to confirm whether the device is 2등급 or 3등급 after risk analysis. | Senior RA / MFDS pre‑submission consultation. |
| **Insufficient local clinical evidence** | No Korean trial data and no valid foreign CER mapping available. | Clinical development lead & regulatory affairs manager for study planning. |
| **Cybersecurity matrix incomplete** | Any of the RA‑01 ~ RA‑20 items remain “in progress”. | Information security officer; halt submission until closure. |
| **KGMP gap (manufacturing)** | Facility not KGMP certified and no import exemption secured. | Manufacturing compliance lead for facility audit or licensing. |
| **Korean labeling missing** | Draft IFU lacks Korean translation or fails to meet MFDS labeling format. | Medical writing & translation team; stop regulatory filing. |
| **AI model update without CMP linkage** | New model version is planned but change‑management SOP not updated. | AI development lead; trigger review of CMP before deployment. |

If any trigger materializes, the project should be placed on “hold” status pending resolution and a formal risk‑based decision documented.

---

### 6. Summary Judgment  

- **Presumed classification:** 3등급 → submission via **허가** (full MFDS approval).  
- **Key dossier elements:** risk management (ISO 14971), usability engineering (IEC 62366‑1), cybersecurity matrix (RA‑01~RA‑20) per 2025‑01‑10 guideline, SBOM SOP, AI model governance SOPs, performance evaluation of AI components, KGMP certification (if domestic manufacturing), Korean labeling/IFU, and sufficient clinical evidence (local or mapped foreign).  
- **Critical gaps** – definitive intended use/indication, risk classification justification, local clinical data or validated foreign CER mapping, complete cybersecurity matrix, change‑management plan integration, KGMP status, Korean IFU.  

These gaps must be closed before the dossier can be compiled for MFDS 허가 review.

---

### 7. Peer Review Prompt  

> **@RA‑Colleague:**  
> Please challenge the assumptions above: (1) the presumed 3등급 classification without a concrete intended use statement; (2) reliance on foreign clinical data under the current MFDS foreign‑CER acceptance policy; and (3) the completeness of the cybersecurity controls given only high‑level guideline references. Identify any additional Korean‐specific obligations that may have been missed, especially regarding post‑market surveillance or AI lifecycle management under the 디지털의료제품법.  

---

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> "Current presumption: 3등급 → 허가" — 소스에 근거 없는 등급 전제(치료 AI=3등급 통상성은 있으나 단정 근거 미제시, peer-review로 헤징). RA-01~20·SOP 체계·가이드라인 2025-01-10 등 소스 반영은 충실.

**Source Excerpts**

1. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

2. Chunk `1130453648414545903`

> ## 8. 후속 조치 요건 (프로젝트 관점) | 우선순위 | 조치 사항 | 연계 문서 | 상태 | |----------|----------|-----------|------| | 1 | 사이버보안 RA-01~RA-20 대응 매트릭스 작성 | 디지털의료제품법_요구사항_매트릭스 | 진행중 | | 2 | 사용적합성 엔지니어링 계획 수립 | IEC_62366-1_사용적합성_엔지니어링_계획서 | v0.2 완료 | | 3 | SBOM 관리 절차 정합성 확인 | SOP-SBOM-001 | v0.2 완료 | | 4 | 변경관리 계획 SOP 연계 (CMP 섹션) | SOP-CC-001 | v0.2 완료 | | 5 | AI 모델 데이터셋·거버넌스 절차 수립 | SOP-AIDATA-001, SOP-AIGOV-001 | v0.2 완료 | | 6 | 구성요소 단위 성능평가 절차 문서화 | AI_구성요소_단위_성능평가 | v0.2 완료 |

### kb-eval-20261106-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "ddf6195bdee43a9b", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `ddf6195bdee43a9b`
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

> **Regulatory Draft – Impact of the “의료기기의 사이버보안 허가·심사 가이드라인” (2025  revision) on a Digital Medical Device**

---

### 1. Korean Classification & Submission Route  

| Step | Requirement | Current Guidance |
|------|-------------|------------------|
| **Device grade** | Must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」. For software that performs clinical functions, or that connects to networks and stores/ transmits patient data, the most common grades are **2등급**, **3등급** or **4등급**. | *No grade is stated in the source; verify separately.* |
| **Submission track** | <ul><li>1등급 → 신고</li><li>2등급 → 인증 (MFDS‑designated 심사기관 review of technical documentation)</li><li>3·4등급 → 허가 (full MFDS approval)</li></ul> | *Use the grade determined above to select the appropriate track.* |

---

### 2. Core Evidentiary Requirements  

| Evidence Category | What Must Be Submitted | Reference |
|-------------------|-----------------------|-----------|
| **KGMP Facility Certification** | Certificate of compliance with KGMP (의료기기법 제28조) for manufacturing site(s). | No specific identifier in source – verify separately. |
| **Risk Management File** | ISO 14971:2019‑based risk analysis, including identification of cybersecurity‑related hazards and mitigation measures. | Framework reference: ISO 14971:2019 (no amendment needed). |
| **Cybersecurity Technical Dossier** (mandatory under the 2025 guideline) | • System Architecture Diagram<br>• Secure‑by‑Design description (defense‑in‑depth, least‑privilege)<br>• Authentication & access‑control specifications<br>• Encryption methodology & key‑management plan<br>• Software integrity safeguards (code signing, boot‑integrity, SBOM)<br>• Network hardening measures (port reduction, firewall, TLS version)<br>• Vulnerability‑management process (CVE monitoring, patch schedule, CVD policy)<br>• Audit‑log specification (event logging, log protection, access history)<br>• Update & maintenance plan (secure OTA updates, remote‑management security) | Source [2] – 35 RA items grouped into eight categories. |
| **Compliance Mapping to International Standards** | Statement of conformity with IEC 81001‑5‑1:2021 and IMDRF N60/N73 cybersecurity controls. | Source [1] – “조화 목적” cites IEC 81001‑5‑1, IMDRF N60/N73. |
| **Clinical Evidence (if grade ≥3등급)** | Local clinical evaluation report or foreign CER accepted under MFDS scope (see latest MFDS notice on foreign clinical data acceptance). | No specific notice number appears in source – verify separately. |
| **Labeling & IFU** | Korean‑language labeling, instructions for use, and cybersecurity user guidance (e.g., password policy, update procedure). | No identifier in source – verify separately. |
| **Post‑Market Surveillance Plan** | PMS activities per MFDS 시판후조사 requirements; include cybersecurity incident monitoring and reporting. | Framework reference: MFDS 시판후조사 규정 (no specific article cited). |

---

### 3. Gaps / Missing Information  

| Gap | Impact | Suggested Action |
|-----|--------|------------------|
| **Device grade** not yet determined. | Unable to select 신고/인증/허가 pathway. | Conduct classification review against the Korean device‑grade table; involve product‑team and regulatory counsel. |
| **KGMP certificate** for manufacturing site(s). | Required for any submission beyond 1등급. | Obtain or update KGMP certification before dossier assembly. |
| **Local clinical data (if applicable)**. | MFDS may require Korean‐origin clinical evaluation for 3·4등급 devices. | Plan a Korean clinical study or identify acceptable foreign CER per MFDS guidance. |
| **Korean labeling & IFU** not prepared. | Non‑compliance with labeling law will delay approval. | Draft Korean label and user manual; include cybersecurity instructions. |
| **Detailed RA item numbers (RA‑01~RA‑35)** not provided in excerpt. | Reviewers may request exact mapping to guideline items. | Retrieve the official PDF of the guide and map each dossier element to RA‑01…RA‑35. |
| **Evidence of conformity with IEC 81001‑5‑1** (e.g., test reports). | Required for demonstrating alignment with international cybersecurity standards. | Conduct or commission compliance testing; include certificates/report excerpts. |

---

### 4. Required Risk Controls (derived from the eight RA categories)  

| Category | Control Example | Link to Requirement |
|----------|----------------|----------------------|
| **Secure Design** | Threat modeling during concept phase; apply defense‑in‑depth architecture. | Source [2] – “Secure by design, Defense-in-depth”. |
| **Authentication & Access** | Multi‑factor user authentication; role‑based access control; session timeout. | Source [2]. |
| **Encryption** | AES‑256 storage encryption; TLS 1.3 for data in transit; hardware security module for key management. | Source [2]. |
| **Software Integrity** | Code signing with a trusted certificate; Secure Boot verification; maintain SBOM. | Source [2]. |
| **Network Security** | Disable unused ports; firewall rules per least‑privilege; enforce TLS 1.3 only. | Source [2]. |
| **Vulnerability Management** | Subscribe to CVE feeds; quarterly patch releases; documented CVD (Common Vulnerabilities Disclosure) policy. | Source [2]. |
| **Audit & Logging** | Immutable audit log storage; retention ≥ 12 months; regular log review. | Source [2]. |
| **Update & Maintenance** | Authenticated OTA update mechanism; digital signature verification of firmware; remote‑management session encryption. | Source [2]. |

All controls must be documented in the risk management file (ISO 14971) and linked to residual risk acceptance criteria.

---

### 5. Citations  

| Item | Citation Type | Reference |
|------|--------------|-----------|
| Guideline amendment date & legal basis | Instance identifier (date only) | Source [1] – 개정일 2025‑01‑10, 법적 근거 「디지털의료제품법」(2025‑01‑24 시행). |
| Expansion to 35 cybersecurity requirements | Instance identifier (no specific number) | Source [2] – “35개 주요 카테고리”. |
| International standards referenced in Korean guideline | Framework reference | IEC 81001‑5‑1:2021; IMDRF N60/N73 (as noted in Source [1]). |
| ISO risk‑management standard | Framework reference | ISO 14971:2019. |

*No specific MFDS 고시/notice number or article section was provided in the excerpts; therefore “no specific identifier found in source — verify separately” applies to all such items.*

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Reason for Escalation | Recommended Owner |
|-------------------|-----------------------|-------------------|
| **Unresolved device grade** after classification review. | Determines submission route; risk of filing under wrong track. | RA Lead + Product Manager. |
| **Missing KGMP certification** at the time of dossier finalization. | Mandatory for any non‑1등급 submission. | Manufacturing QMS Owner. |
| **Absence of Korean labeling/IFU** in draft package. | Violates MFDS labeling law; will cause refusal. | Regulatory Documentation Specialist. |
| **Insufficient evidence of IEC 81001‑5‑1 conformity** (e.g., no test reports). | MFDS may reject on basis of inadequate cybersecurity justification. | Cybersecurity Engineer + QA. |
| **Pending local clinical data** for 3·4등급 device. | Data gap leads to non‑approval or request for additional studies. | Clinical Affairs Lead. |
| **Discrepancy between RA‑01~RA‑35 mapping and submitted evidence** identified by internal reviewer. | Reviewer comments must be addressed before MFDS submission. | Documentation Review Team. |

When any trigger fires, the responsible owner should raise a formal “Regulatory Gap” ticket in the project tracking system, with a target resolution date that allows at least a 2‑week buffer before the planned MFDS submission deadline.

---

### 7. Reusable RA Judgment (Lesson Learned)

> **For digital medical devices subject to the 2025 Korean Cybersecurity Guideline, the regulator expects a comprehensive, standards‑aligned cybersecurity dossier (35 RA items across eight categories) mapped to IEC 81001‑5‑1 and IMDRF N60/N73, together with the standard KGMP certification, ISO 14971 risk file, Korean labeling/IFU, and—if applicable—local clinical evidence. The device grade must be confirmed against the Korean device‑grade table before selecting 신고/인증/허가. Any missing element (KGMP, Korean language documents, IEC 81001‑5‑1 conformity proof, or local clinical data) should trigger an immediate human escalation to avoid MFDS refusal.**  

---

### 8. Peer Review Prompt  

*Please review the assumptions and coverage above:*  

- Have we correctly interpreted the classification implications for a software‑intensive medical device under the Digital Medical Products Act?  
- Are there any additional Korean regulatory instruments (e.g., recent MFDS notices on foreign clinical data acceptance) that should be referenced, given they were not present in the provided excerpts?  
- Does the risk‑control mapping fully satisfy both ISO 14971 and IEC 81001‑5‑1 expectations, or are further technical artefacts needed (e.g., penetration‑testing reports)?  

Your feedback will help refine the dossier checklist and escalation process.

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
- [x] Human correction needed

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

### kb-eval-20261106-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-06", "decision_ref": "kb-eval-20261106-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "f3171a7b9462357a", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f3171a7b9462357a`
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

> **Regulatory Draft – Impact of the 2025 Digital‑Medical‑Products Act (디지털의료제품법) on a SaMD Submission**

---

### 1. Device Overview  
- **Product type:** Software as a Medical Device (SaMD), potentially incorporating AI/ML algorithms.  
- **Intended use / indication:** *Not supplied in source – must be defined by sponsor.*  

---

### 2. Korean Regulatory Classification & Submission Route  

| Step | Requirement | MFDS pathway |
|------|-------------|--------------|
| **Determine grade (1~4등급)** | Apply the “의료기기 품목 및 품목별 등급에 관한 규정” to the device’s risk profile, indication, and intended user. The 2025‑01‑24 amendment to the Digital Medical Products Act introduced a revised SaMD classification scheme that may shift a product from **2등급** to **3등급·4등급** depending on algorithmic risk (e.g., “clinical decision support” vs. “diagnostic”). | • **1등급 → 신고**  <br>• **2등급 → 인증** (technical‑document review by an MFDS‑designated 심사기관) <br>• **3,4등급 → 허가** (full MFDS approval). |
| **Select 심사기관** | For KGMP certification, the list of accredited agencies includes KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea. Since 2025‑01‑24 the **NIDS** (National Institute for Digital Health) is also authorized to perform GMP appropriateness assessments for digital medical devices. | Choose any listed agency; inclusion of NIDS must be documented when preparing the GMP 적합인정 신청. |

> *Citation*: No specific MFDS 고시 or notice number appears in the source excerpts – **verify separately** for the exact instrument (e.g., “MFDS 고시 제2025‑XX호”) that introduced the SaMD classification change.

---

### 3. Mandatory Evidence Package  

| Category | Required Content | Basis |
|----------|-----------------|-------|
| **KGMP (GMP 적합인정) certificate** | • Application → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함통보 → 시정조치 제출 → 적합인정서 발급 (validity 3 yr). <br>• For digital devices, NIDS may act as the 심사기관. | Excerpt [1] – GMP 절차 description; NIDS role from same excerpt. |
| **Technical Documentation** | • Device description, hardware/software architecture, labeling & IFU (Korean language mandatory). <br>• Software Lifecycle documentation per IEC 62304:2006+A1:2015. | ISO/IEC standards are accepted framework references. |
| **Risk Management File** | • Risk analysis, evaluation, and control according to ISO 14971:2019. <br>• Cyber‑security plan referencing IEC 81001‑5‑1:2021 (MFDS 사이버보안 가이드라인). | Framework references – no source‑specific identifier required. |
| **Clinical Evaluation** | • Korean clinical data *or* a foreign Clinical Evaluation Report (CER) accepted under the current MFDS scope for non‑clinical GLP data (OECD MAD) and, separately, for clinical evidence if the MFDS notice permits it. The exact notice number must be confirmed. | No specific identifier in source – **verify separately**. |
| **AI/ML Specific Evidence** | • Algorithm description, training/validation dataset characteristics, performance metrics, and post‑market change management plan as required by the MFDS “디지털의료기기 가이드라인 6종” (issued 2025‑05‑07). | Citation of guideline date from excerpt [2]; specific guide numbers not provided – **verify separately**. |
| **Labeling & IFU** | • Korean language labeling, user manual, and safety information per MFDS 라벨링 규정. | Framework reference – standard regulatory requirement. |
| **Post‑Market Surveillance (PMS)** | • PMS 계획, adverse event reporting process, periodic safety update (Korean‑specific format). | MFDS PMS regulations; no source identifier supplied. |

---

### 4. Missing Information (must be obtained from sponsor)

1. **Exact intended use / indication** – needed to assign the correct grade (1~4등급).  
2. **Risk classification rationale** – how the device’s functionality maps onto the SaMD risk categories defined in the 2025 amendment.  
3‑4. **Software architecture details** – version control, change‑management process, AI/ML model lifecycle.  
5. **Clinical evidence strategy** – whether Korean clinical study is planned or a foreign CER will be submitted; justification for reliance on foreign data.  
6. **Manufacturing location & KGMP status** – confirmation of facility eligibility for NIDS assessment.  
7. **Labeling draft (Korean)** – to verify compliance with language and content rules.  

---

### 5. Core Risk Controls (to be addressed in the Risk Management File)

| Hazard | Control Measure | Verification |
|--------|-----------------|--------------|
| Software malfunction / incorrect output | Fault‑tolerant design, watchdog timers, regular software updates; IEC 62304 process controls. | Unit & integration testing, verification of code reviews. |
| AI/ML algorithm drift | Continuous performance monitoring, predefined change‑management trigger thresholds, retraining protocol. | Prospective validation on a hold‑out dataset; post‑market data review per MFDS AI/ML guidance. |
| Cybersecurity breach | Network segmentation, encryption, authentication, regular vulnerability scanning; IEC 81001‑5‑1 compliance. | Penetration testing reports, security incident response SOP. |
| User error due to UI design | Human factors engineering evaluation (IEC 62366‑1:2020), usability testing with target users in Korean language. | Usability test results, risk reduction analysis. |

---

### 6. Citations  

- **Framework references** (no verification caveat required):  
  - ISO 14971:2019 – Risk Management for Medical Devices.  
  - ISO 13485:2016 – QMS for medical device manufacturers.  
  - IEC 62304:2006+A1:2015 – Software life‑cycle processes.  
  - IEC 62366‑1:2020 – Usability engineering.  
  - IEC 81001‑5‑1:2021 – Cybersecurity.  

- **Instance identifiers** (must appear in source):  
  - GMP 적합판정 procedure and participating 심사기관 list – excerpt [1] (no instrument number).  
  - Digital Medical Products Act amendment dates (2025‑01‑24, 2025‑05‑07) and NIDS GMP role – excerpt [2] (no specific 고시/notice number).  

> **No specific MFDS 고시 or notice numbers are provided in the source excerpts; therefore “no specific identifier found in source — verify separately” is noted for each regulatory instrument that would normally be cited.**

---

### 7. Human‑Escalation Triggers  

| Situation | Action Required (Human Review) |
|-----------|---------------------------------|
| **Uncertain grade** after applying the SaMD risk matrix | Senior RA or MFDS liaison must confirm classification before dossier submission. |
| **KGMP certificate not yet issued** (facility still under inspection) | Pause submission; schedule follow‑up with selected 심사기관 (including NIDS if applicable). |
| **AI/ML algorithm change proposal exceeds pre‑approved scope** (e.g., new data source, model architecture) | Trigger a Change Management Review; obtain MFDS prior approval per the “네거티브 방식 변경허가제” (2026 예정). |
| **Adverse event signal detected** before PMCF completion | Initiate immediate safety communication to MFDS and conduct root‑cause analysis. |
| **Insufficient clinical evidence** – foreign CER not accepted or lacking Korean data | Escalate to Clinical Affairs lead to design a bridging study or obtain additional local data. |
| **Labeling draft fails Korean language review** | Send to linguistic compliance specialist for revision before filing. |

---

### 8. Regulatory Judgment (concise)

- The SaMD must first be **graded under the revised 2025 SaMD classification scheme**; likely it will fall into **2등급 or higher** given AI/ML functionality.  
- Accordingly, the submission route will be **인증 (for 2등급) or 허가 (for 3~4등급)**, with a required **KGMP 적합인정** performed by one of the accredited 심사기관—NIDS now eligible as of 2025‑01‑24.  
- The evidence package must contain the items listed in Section 3; any gaps in intended use definition, risk analysis, clinical data strategy, or Korean labeling must be resolved before dossier finalization.  
- **Human escalation** is mandatory whenever classification, KGMP status, AI/ML change scope, safety signals, or labeling compliance are uncertain.

---

### 9. Peer‑Review Prompt  

> *Colleague, please review the assumptions made about SaMD grade determination under the 2025 amendment and the reliance on NIDS for GMP assessment. Verify whether a specific MFDS 고시 number governing AI/ML clinical requirements exists in the latest guidance (e.g., “MFDS 고시 제2025‑XX호”) and flag any missing regulatory instruments that should be cited.*

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

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> [최종(shadow 수용) 3→2] ① "NIDS (National Institute for Digital Health)" 영문 확장 무근거(소스 무확장) ② "2025-01-24 개정이 SaMD 재분류 체계·2→3/4등급 시프트 도입" — 소스는 시행+영향 개요만 기술, 재분류 메커니즘은 과잉 서술. NIDS 역할·날짜·가이드라인 6종·네거티브 방식은 소스 일치.

**Source Excerpts**

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---
