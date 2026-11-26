# KB Eval Checksheet - 2026-11-26 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261126-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "e2d226a6a48b9b09", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "757e3b0039fbc8900d0917e9ebdd32c0ded796618813c51039ed63b34e627e31"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `e2d226a6a48b9b09`
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

> **Regulatory Draft – QMSR & Design‑Control Readiness Assessment**  

---

### 1. Bottom Line (Classification & Submission Pathway)  
| Item | Determination | Rationale |
|------|---------------|-----------|
| **Device class** | **Class II (510(k) required)** | No predicate or device description is supplied in the source, but the presence of X‑ray field‑service SOPs and UDI requirements indicates a regulated medical device that falls under 21 CFR Part 820. Most imaging / diagnostic devices are Class II; absent evidence of “low‑risk” exemption, the safest assumption is 510(k). |
| **Regulatory route** | **Premarket Notification (510(k))** | The device will need to demonstrate substantial equivalence to a cleared predicate after establishing a compliant QMSR and complete design‑control documentation. No indication that a De Novo or PMA pathway is required. |

---

### 2. Required Evidence for Submission  

| Area | Specific Deliverable | Supporting Regulation / Standard (framework) |
|------|---------------------|-----------------------------------------------|
| **Quality Management System** | • Updated SOPs covering records, complaints, UDI, service and audit as listed in the source (SOP‑DOC‑001, SOP‑PMS‑001, SOP‑TRC‑001/UDI‑001, SOP‑SVC‑001, SOP‑IA‑001). <br>• Evidence of ISO 13485:2016 implementation with **§4.2.5** (record management) satisfied *and* the FDA‑specific additions in **21 CFR §820.35(a‑d)** met. | 21 CFR Part 820 (QMSR); ISO 13485:2016 §4.2.5 (baseline). |
| **Design Controls** | • Design & Development Plan (Design Planning, Input, Output, Verification, Validation, Transfer) <br>• Design History File (DHF) linking each design output to verification/validation results <br>• Risk Management File (ISO 14971:2019) with risk analysis, evaluation and mitigations fully documented. | 21 CFR §820.30 (Design Controls – withdrawn but incorporated by reference into QMSR); ISO 14971:2019 (risk management). |
| **UDI Compliance** | • UDI issuance record per **§820.35(c)** <br>• GUDID submission & maintenance evidence under **21 CFR Part 830** (format, agency accreditation, and database entry) | 21 CFR Part 801 §§801.20‑801.50 (label placement); 21 CFR Part 830 (UDI system). |
| **Complaint & MDR Handling** | • Complaint handling SOP matching **§820.35(a)** <br>• MDR decision‑tree records referencing **§803.50** and **§803.53** triggers (as included in SOP‑PMS‑001) <br>• Full traceability of complaint → investigation → corrective action. | 21 CFR §803 (MDR). |
| **Service Records** | • Service documentation form with the six required items per **§820.35(b)** (captured in SOP‑SVC‑001) for each X‑ray field service event. | 21 CFR §820.35(b). |
| **Electronic Records (Part 11)** | • Separate mention in SOP‑DOC‑001 that Part 11 controls are documented *outside* §820.35. Provide validation of the electronic system used for record keeping. | 21 CFR Part 11. |
| **Labeling** | • Labels showing UDI in both plain‑text and AIDC format per **21 CFR §801.20‑§801.45** <br>• Full labeling statement meeting §801.5 (Contents) and any device‑specific requirements (e.g., IEC 60601‑1 for X‑ray). | 21 CFR Part 801. |
| **Post‑Market Surveillance** | • Procedure for trend analysis and voluntary corrective actions under **§820.35(d)** (confidentiality, data integrity) <br>• Record of annual MDR summary as per FDA guidance. | 21 CFR §820.35(d). |

---

### 3. Gaps / Missing Information  

| Gap | Impact on Clearance | Recommended Action |
|-----|--------------------|-------------------|
| **Design‑control artifacts** – No evidence that a Design History File exists or that design inputs/outputs are formally linked to verification/validation activities. | Failure to meet design‑control requirement; 510(k) deficiency. | Author a DHF and populate it before submission. |
| **Risk Management File** – ISO 14971:2019 analysis not referenced in the source. | Incomplete risk justification; FDA will issue an AI (Additional Information). | Conduct full risk analysis, update DMR accordingly. |
| **UDI System Evidence** – Only SOPs mention UDI; no GUDID submission proof. | Non‑compliance with §820.35(c) and Part 830; possible 510(k) hold. | Generate and submit device entry to the Global Unique Device Identification Database (GUDID). |
| **Electronic Record Validation (Part 11)** – SOP‑DOC‑001 separates Part 11 but no validation report is cited. | Records may be deemed non‑compliant; audit finding. | Perform Part 11 validation of all electronic QMS modules; attach validation summary. |
| **Labeling compliance** – No explicit label mock‑up showing UDI placement per §801.20+. | Labeling deficiency; FDA will request revision. | Produce a full label package and conduct internal labeling review. |
| **Post‑Market Surveillance Plan** – Only MDR decision tree is mentioned; no systematic PMS plan. | Insufficient for ongoing compliance; may affect 510(k) if significant risks exist. | Draft a formal Post‑Market Surveillance (PMS) plan aligned with §820.35(d). |

---

### 4. Risk Controls (Proposed Mitigations)

| Control | Target Requirement | Implementation Note |
|---------|-------------------|---------------------|
| **Design for Safety** | IEC 60601‑1 (X‑ray safety) & IEC 62366‑1 (Usability) | Integrate safety and usability testing into verification. |
| **Predetermined Change Control Plan (PCCP)** (if AI/ML components present) | FDA Guidance Dec 2024 | Define allowable post‑market algorithm updates, document in design plan. |
| **Documentation Integrity** | §820.35(d) confidentiality & data integrity | Enforce read‑only archives for DHF and complaint files; audit trail enabled. |
| **Service Traceability** | §820.35(b) service record completeness | Use electronic service log with mandatory fields; periodic review. |
| **UDI Linking** | §820.35(c) & Part 830 | Embed UDI in every device label, packaging, and associated software configuration files. |

---

### 5. Citations (as required by source)

| Requirement | Source‑derived Identifier |
|-------------|---------------------------|
| Additional QMSR record‑management requirements – **§820.35(a)(b)(c)(d)** | Appears in excerpt [1] & SOP list [2]. |
| SOP‑DOC‑001 amendment adding “§820.35(a)(b)(c)(d) additional requirements” | Excerpt [2]. |
| UDI record‑management addition – **§820.35(c)** + 21 CFR Part 830 | Excerpt [2]. |
| Service record form with six items – **§820.35(b)** | Excerpt [2]. |
| MDR decision‑tree triggers – **§803.50** and **§803.53** | Excerpt [2]. |

*Framework references (no instance identifiers required):*  
- 21 CFR Part 820 (QMSR) – effective 2026‑02‑02, incorporates ISO 13485:2016.  
- ISO 13485:2016 §4.2.5 (record management).  
- ISO 14971:2019 (risk management).  
- 21 CFR Part 801 (§801.20‑§801.45 – UDI label placement).  
- 21 CFR Part 830 (UDI system).  

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason | Action |
|--------|--------|--------|
| **Missing DHF or incomplete design‑control documentation** | Prevents demonstration of substantial equivalence. | Escalate to Design Engineering Lead for immediate DHF creation; pause submission preparation. |
| **No validated Part 11 evidence** | Risk of non‑compliant electronic records. | Notify IT/QA and require validation report before final sign‑off. |
| **UDI/GUDID entry not submitted or pending** | Violates §820.35(c) & Part 830; can cause FDA hold. | Escalate to Regulatory Operations for GUDID submission; track status weekly. |
| **Complaint handling SOP fails to capture MDR decision‑tree outcomes** | Inadequate post‑market data flow, may trigger FDA AI on MDR reporting. | Raise to QA Manager; enforce corrective action plan and re‑train staff. |
| **Labeling package missing UDI placement per §801.20** | Labeling deficiency leading to 510(k) refusal. | Engage Labeling Specialist to produce compliant label; hold submission until complete. |
| **Risk analysis not aligned with ISO 14971:2019** | Insufficient risk justification. | Pull in Risk Management Team for gap analysis; defer submission. |

---

### 7. Peer‑Review Prompt  

> *Colleague, please review the assumptions made about device classification (Class II/510(k)), the completeness of design‑control artifacts, and any jurisdiction‑specific gaps (e.g., whether additional EU/MDR references in SOP‑PMS‑001 have been incorrectly carried into a US submission). Confirm that all cited CFR sections are accurate and that no invented identifiers were introduced.*

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

> '21 CFR §820.30 (Design Controls – withdrawn but incorporated by reference into QMSR)' — §820.30은 폐지됐고 ISO 13485 §7.3이 편입되는 것(§820.30 자체가 편입되는 게 아님 — 오서술 결합 잔존, 계열 4회차). 나머지 우수(§820.35(a)-(d)·§803.50/53·Part 11·ISO 13485 §4.2.5 전부 정확).

**Source Excerpts**

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `130165779856845378`

> ### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영) | SOP | 갱신 내용 | 담당 | 판정 기준 | |-----|----------|------|----------| | SOP-DOC-001 | §3에 "미국 시장 적용 시 §820.35(a)(b)(c)(d) 추가요건" 절 신설, Part 11은 §820.35 외부로 별도 절 분리 | QA | 기록관리 절차에 불만/서비스/UDI/기밀성·Part 11 분리 기재 여부 | | SOP-PMS-001 | MDR 결정 트리(§803.50 30cd / §803.53 5wd 트리거 기준) + 미보고 사유 양식 첨부 | QA/RA | 불만 → MDR 판정 → 기록 흐름 완비 여부 | | SOP-TRC-001 / SOP-UDI-001 | UDI 기록관리 절 추가 — **§820.35(c)** + 21 CFR Part 830 | RA | GUDID 제출·갱신 기록 체계 구축 여부 | | SOP-SVC-001 (신설/갱신) | **§820.35(b)** 6항목 서비스 기록 양식 도입 | Service/QA | X-ray 출장정비 기록 6항목 완결성 | | SOP-IA-001 | 감사보고서 작성 기준에 "외부 열람 대비 객관적 증거 인용" 항목 추가 | QA | 보고서 품질 기준 갱신 여부 |

### kb-eval-20261126-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_us-002", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "393ab279e7334e8f", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `393ab279e7334e8f`
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

> **Regulatory Draft – Imaging‑Room GUI Software (SaMD)  
Primary focus: QMSR & Design‑Control readiness**

---

### 1. Device Classification & Submission Pathway  

| Item | Determination | Rationale / Citation |
|------|---------------|----------------------|
| **Device type** | Stand‑alone medical imaging software (GUI for acquisition room) – SaMD | Source [2] describes “촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어)” |
| **Regulatory panel** | 21 CFR Part 892 – Radiology / Imaging devices | Part 892 covers imaging systems; the software provides image acquisition/management functions. |
| **Class** | Class II | Most medical‑image management and processing systems are classified as Class II under **§892.2050** (Medical image management and processing system). No contradictory source found – verify against FDA product classification database. |
| **Submission route** | 510(k) Premarket Notification | Predicate devices exist for imaging‑room GUIs; therefore a traditional 510(k) is the fastest credible pathway. If no suitable predicate can be identified, consider De Novo (Class II to Class I/II). |

---

### 2. Required Evidence Package (510(k) Minimum)

| Category | Required Items | Reference |
|----------|----------------|-----------|
| **Device Description & Intended Use** | Full label, instructions for use (IFU), and a clear statement of the software’s clinical function (e.g., “provides real‑time display & basic post‑processing of X‑ray images”). | 21 CFR 807.92 |
| **Predicate Comparison** | Side‑by‑side table showing technological characteristics, performance, and intended use versus selected predicate(s). | 21 CFR 807.92(b) |
| **Design Controls (Software)** | • Software Development Plan (SDP) – IEC 62304 <br>• Software Requirements Specification (SRS) <br>• Software Architecture Design (SAD) <br>• Software Verification Plan/Report (SVP/SVR) <br>• Traceability matrix linking requirements → design → verification. | IEC 62304 §8.1 (cited in Source [2]) |
| **Risk Management** | ISO 14971:2019 risk analysis, risk control report, and residual risk evaluation. | ISO 14971 2019 (framework) |
| **Verification & Validation** | Unit test reports, integration tests, system validation (including clinical performance if applicable). Regression‑test automation per source [2]. | IEC 62304 §8.1 |
| **Cybersecurity** | Threat Model, SBOM, and a Predetermined Change Control Plan (PCCP) per FDA Final Guidance 2024‑12‑03. | Source [2] – “FDA PCCP” |
| **AI/ML (if applicable)** | Documentation of the algorithm, training data set description, performance monitoring plan, and a completed PCCP covering pre‑determined changes. | FDA PCCP (2024‑12‑03 Final) |
| **QMSR Compliance Evidence** | • QMS Manual showing incorporation of ISO 13485:2016 clauses (design controls → ISO 13485 §7.3; production → §7.5). <br>• SOPs for complaint handling, service record keeping, and internal audit per **§820.35(a)** and **§820.10(b)** (ARR integration). | Source [1] – ARR (§820.10(b)), Complaint file enhancement (§820.35(a)) |
| **UDI Assignment** | Device Identifier (DI) & Production Identifier (PI) generated per 21 CFR 830; label placement per 21 CFR 801 Subpart B (§801.20 onward). | 21 CFR 830, 21 CFR 801 Subpart B |
| **MDR & Reporting** | MDR (Medical Device Reporting) procedures for “reportable” events and a correction/removal plan per **§820.35(a)** and **§803**, **§806**. | Source [1] – MDR reporting requirement linked to complaint file (§820.35(a)) |

---

### 3. Gaps / Missing Information (to be supplied before submission)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended‑use statement** | Determines classification & predicate search. | Draft and confirm with product engineering. |
| **Predicate device identifiers** | Required for 510(k) comparison table. | Perform FDA database search; if none, prepare De Novo justification. |
| **Full software development lifecycle artifacts (SDP, SRS, SAD, SVP/SVR)** | Essential to demonstrate compliance with IEC 62304 and FDA design‑control expectations. | Collect from engineering; verify completeness. |
| **Risk Management file (ISO 14971) & residual risk assessment** | Needed for 510(k) safety summary. | Conduct hazard analysis if not already done. |
| **Cybersecurity Threat Model & SBOM** | Required for PCCP and FDA’s pre‑market expectations on SaMD security. | Generate; map to mitigation controls. |
| **PCCP (Predetermined Change Control Plan)** | Needed when AI/ML or software updates are anticipated. | Draft according to FDA Final Guidance 2024‑12‑03. |
| **UDI labeling mock‑up** | Must show compliance with label placement (§801.20+) and data format (§830.20). | Prepare graphics; run internal verification. |
| **Service record template & SOP** | Required under **§820.35** for post‑market service documentation. | Draft SOP, align with QMSR. |
| **Internal audit report (FDA inspector access)** | Source [1] notes that FDA may request audit reports; must be prepared and not classified as “non‑public”. | Schedule audit; ensure reports are complete and available. |

*No specific identifier (e.g., 510(k) number, decree) appears in the source excerpts – verify separately.*

---

### 4. Key Risk Controls to Highlight

| Control | Source / Standard |
|---------|-------------------|
| **Design control & verification** – traceability matrix linking user needs → software requirements → verification tests. | IEC 62304 §8.1; ISO 13485 §7.3 (design controls). |
| **Risk mitigation** – apply ISO 14971:2019 risk control hierarchy (inherently safe design, protective measures, information). | ISO 14971 2019. |
> **Cybersecurity** – threat modeling, secure coding standards, periodic vulnerability scanning, and a PCCP that pre‑authorises safe software updates. | FDA PCCP (2024‑12‑03), Source [2]. |
| **Complaint handling & MDR reporting** – SOP ensuring each complaint is evaluated for reportability per 21 CFR 803; record decision in complaint file as required by §820.35(a). | Source [1] – “불만 파일 강화” (§820.35(a)). |
| **UDI generation & label placement** – DI/PI creation per 21 CFR 830, printed on the device label per 21 CFR 801 Subpart B (§801.20 onward). | 21 CFR 830; 21 CFR 801 Subpart B. |
| **Service record keeping** – documentation of every maintenance or repair event, stored per §820.35. | Source [1] – “서비스 기록” (§820.35). |

---

### 5. Human‑Escalation Triggers  

| Situation | Who to Escalate To | Reason / Timing |
|-----------|-------------------|-----------------|
| **No suitable predicate identified after exhaustive FDA database search** | Senior Regulatory Affairs Manager / Legal counsel | Must decide on De Novo pathway or alternative market strategy (≥10 business days after final search). |
| **QMSR non‑conformity discovered during internal audit (e.g., missing ARR activities, inadequate complaint file)** | QMS Lead & Quality Assurance Director | Immediate corrective action; potential FDA inspection impact. |
| **Incomplete cybersecurity documentation or inability to produce a PCCP** | Cybersecurity / Software Engineering Lead + RA lead | Needed before 510(k) submission; risk of FDA request for additional information (AI). |
| **UDI implementation gaps (e.g., labeling not compliant with §801.20)** | Labeling & Packaging Manager | Must be resolved before filing; otherwise FDA will issue a non‑conformity. |
| **Unexpected MDR reportable event discovered post‑market** | Post‑Market Surveillance Team, RA Manager | 30‑day reporting to FDA required; coordinate with QA to ensure timely submission (21 CFR 803). |
| **Regulatory counsel request for clarification on the applicability of new QMSR provisions (e.g., contract sterilizer scope)** | Regulatory Counsel / Senior RA | Interpretation may affect scope of QMS; escalation ensures correct implementation. |

---

### 6. Peer‑Review Prompt  

> *Colleague, please review the assumptions above: (1) classification as Class II under §892.2050; (2) reliance on a traditional 510(k) route and the completeness of the predicate search plan; (3) coverage of QMSR obligations (ARR integration, complaint file enhancement, service records, internal audit visibility); and (4) identification of any jurisdiction‑specific gaps not captured from the source material (e.g., state‑level licensing, export controls). Provide feedback on missing artifacts or alternative regulatory pathways.* 

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
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> §807.92 오인용 2건: 'Device Description & Intended Use → 21 CFR 807.92'·'Predicate Comparison → 807.92(b)' — 내용 요건은 §807.87, §807.92는 510(k) Summary 포맷(계열 재발). QMSR §7.3/§7.5·UDI·PCCP는 정확.

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261126-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "fecbc6a4ed086294", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "ace8476c9535cd1cadac8d64a788cb46b3d78a905da01c1e1dfc3e038615f0f4"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `fecbc6a4ed086294`
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

### 1. Device Classification & Submission Route  
| Item | Current Status | Action Required |
|------|----------------|-----------------|
| **Intended use / indication** | *Not provided* | Obtain a concise statement of intended use, target patient population, and clinical claims. |
| **Device type (e.g., imaging, diagnostic, software)** | *Not provided* | Identify the functional category to map to the correct CFR‑part panel (e.g., Part 892 for radiology). |
| **Classification (Class I–III)** | *Undetermined* – depends on intended use & risk profile. | Perform a classification analysis using 21 CFR 862/892 etc. and confirm with FDA’s product classification database. |
| **Proposed submission** | *Assumed 510(k) for most Class II devices* – but could be De Novo (if novel) or PMA (if Class III). | Once class is known, select the appropriate pathway: <br>• Class I → may be exempt from 510(k). <br>• Class II → 510(k) required. <br>• Class III → PMA or De Novo if no predicate. |

**Bottom line:** *Classification cannot be finalized until the device’s intended use and risk level are supplied.* Until then, the submission route remains provisional.

---

### 2. QMSR Compliance – Evidence Required (effective 02‑Feb‑2026)  

| Requirement | Supporting Document / Artifact | CFR/Standard Reference* |
|-------------|--------------------------------|--------------------------|
| **Quality Management System (QMS) Manual** that aligns with ISO 13485:2016 (incorporated by reference). | SOPs, procedures, work instructions covering all QMS elements. | 21 CFR 820 (effective 2026‑02‑02) – see source [2]; ISO 13485 (2016) |
| **Design Controls** – design planning, inputs, outputs, verification, validation, transfer, and change control. | Design History File (DHF) with design plans, input/output matrices, verification & validation reports. | Design‑control mapping → ISO 13485 §7.3 (design controls). |
| **Risk Management** – risk analysis, evaluation, mitigation, and residual‑risk acceptability. | Risk Management File complying with ISO 14971 (2019). | ISO 14971 (2019) – no specific identifier in source. |
| **Production & Process Controls** (process validation, equipment maintenance, sterilization). | Process Validation Protocols/Reports; Equipment Maintenance Records. | ISO 13485 §7.5 (production controls). |
| **Complaint Handling & Reporting** – collection, evaluation, trending, corrective‑action initiation. | Complaint files, CAPA logs, and FDA‑specific record‑control per §820.35. | 21 CFR 820 §820.35 (record control); ISO 13485 §8.2.2 (complaint handling). |
| **Document & Record Control** – document approval, revision history, retention schedule. | Document‑control SOPs and master records. | 21 CFR 820 §820.10 (applicability) + §820.35 (records). |
| **UDI System** – label placement of plain‑text & AIDC barcode; GUDID submission. | Label mock‑ups, UDI Allocation Documentation, GUDID entry confirmation. | 21 CFR 801 §801.20+ (label) & 21 CFR 830 §830.20/§830.300‑360 (UDI system). |
| **Software Lifecycle** (if applicable) – IEC 62304 compliance, verification/validation, cybersecurity controls. | Software Development Plan, source code repository logs, security risk assessment. | IEC 62304 (2006+A1:2015); IEC 62366‑1 (2015+A1:2020). |
| **Human Factors / Usability Engineering** (if applicable) – IEC 62366‑1 evidence. | Usability Validation Report, formative/summative test data. | IEC 62366‑1 (2015+A1:2020). |

\*Framework references are stated as facts; no “verify” caveat required.

---

### 3. Design‑Control Readiness – What Must Be in Place  

| Element | Current Evidence (from source) | Gap / Needed Action |
|---------|--------------------------------|---------------------|
| **Design Plan** | *Not described* | Draft a design‑plan document that outlines all planned activities, responsibilities, and milestones. |
| **Design Input Traceability** | *Missing* | Create an input matrix linking clinical requirements to specifications. |
| **Design Output Documentation** | *Missing* | Capture final specifications, drawings, software code listings, labeling texts. |
| **Verification & Validation Protocols/Reports** | *Missing* | Develop test protocols; conduct verification (unit, integration) and validation (clinical/ simulated use). |
| **Change‑Control Procedure** | *Absent* | Implement a Predetermined Change Control Plan (PCCP) for AI/ML updates or major design changes. |
| **Risk Management File** | *Not referenced* | Assemble a complete ISO 14971 risk file. |
| **Usability Engineering File** (if UI‑based) | *Not referenced* | Conduct usability studies per IEC 62366‑1 and archive results. |

---

### 4. Identified Missing Information  

1. **Device description & intended use** – required for classification, predicate search, labeling, and QMS scope.  
2. **Regulatory class determination** – cannot assign submission route without it.  
3. **Predicate device(s) (if pursuing 510(k))** – need FDA‑cleared identifiers (e.g., K#####).  
4. **Specific design‑control artifacts** – DHF components listed above are absent.  
5. **Risk‑management outputs** – ISO 14971 file not mentioned.  
6. **UDI allocation and labeling mock‑ups** – needed for Part 801/830 compliance.  

*Until these items are supplied, a definitive regulatory submission plan cannot be finalized.*

---

### 5. Recommended Risk Controls (US‑focused)  

| Control | Standard / CFR Basis | Implementation Note |
|---------|----------------------|---------------------|
| **Design Input Verification** | ISO 13485 §7.3; 21 CFR 820 §820.30 (withdrawn, now covered by ISO reference). | Tie each input to a verification test. |
| **Process Validation** | ISO 13485 §7.5; 21 CFR 820 §820.75 (production validation). | Document validation for sterilization, software build, etc. |
| **Complaint Handling & CAPA** | §820.35 (records); ISO 13485 §8.2.2. | Establish a closed‑loop system; trend analysis. |
| **UDI Assignment & Labeling** | 21 CFR 801 §801.20+; 21 CFR 830 §830.20. | Ensure label carries both plain‑text and barcode. |
| **Software Lifecycle Management** | IEC 62304; PCCP (FDA guidance Dec 2024). | Use version control, traceability matrix, and pre‑authorized change plan. |
| **Human Factors / Usability** | IEC 62366‑1. | Conduct formative/usability testing early. |
| **Cybersecurity Controls** (if applicable) | FDA Guidance “Content of Premarket Submissions for Management of Cybersecurity” – no CFR citation needed. | Risk assessment, threat modeling, mitigation plan. |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger | Escalation Path |
|-----------|---------|-----------------|
| **Classification unknown** (no intended use/indication) | Immediate pause on any submission planning. | Notify Lead Regulatory Affairs & Project Manager for clarification before proceeding. |
| **Missing predicate information** (for 510(k)) | Cannot complete substantial‑equivalence argument. | Escalate to Senior RA to conduct market research or consider De Novo route. |
| **QMS documentation gaps** (e.g., no DHF, risk file) | Non‑compliance with QMSR requirements. | Raise a CAPA; senior QA/RA sign‑off required before FDA interaction. |
| **UDI labeling not demonstrated** | Potential 510(k) “labeling” deficiency. | Forward to Labeling & Packaging team; senior RA approval needed. |
| **Predetermined Change Control Plan absent for AI/ML device** | FDA may reject change‑control strategy. | Escalate to Chief Technology Officer & Regulatory Lead to draft PCCP. |
| **Any FDA additional requirement identified in the Federal Register notices (2024‑01709, 2025‑21955) not addressed** | Compliance risk. | Immediate review by RA leadership and update of QMS SOPs. |

---

### 7. References  

* **21 CFR Part 820 – Quality Management System Regulation (QMSR)** – effective 02‑Feb‑2026 (source [2]).  
* **Federal Register 2024‑01709** – final rule promulgation (source [2]).  
* **Federal Register 2025‑21955** – technical amendment (source [2]).  
* **FDA QMSR official guidance pages** – fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr (source [1]).  
* **ISO 13485:2016**, incorporated by reference in QMSR.  
* **ISO 14971:2019** – risk management.  
* **IEC 62304 2006+A1:2015** – software lifecycle.  
* **IEC 62366‑1 2015+A1:2020** – usability engineering.  
* **Predetermined Change Control Plan (PCCP) Guidance**, FDA Dec 2024.

---

### 8. Peer Review Prompt  

> *Colleague, please review the assumptions above—particularly the inference that the device will likely follow a 510(k) route once classified as Class II, and the completeness of the QMSR evidence checklist. Verify whether any additional FDA‑specific clauses from the 2025 technical amendment (FR 2025‑21955) affect design‑control documentation or record‑keeping beyond what is captured here.*  

---

### 9. Reusable RA Judgment (Lesson Learned)

**When a device dossier lacks a clear intended use and classification, halt all submission planning until that information is supplied; QMSR compliance (ISO 13485:2016 incorporation) applies universally to any marketed device after 02‑Feb‑2026, but the specific design‑control artifacts required for a 510(k), De Novo, or PMA depend on the final classification.**

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

> '21 CFR 820 §820.30 (withdrawn, now covered by ISO reference)' — 폐지 조항 나열 잔존(계열 4회차, 인지 표기형). QMSR §7.3/§7.5/§8.2.2+§820.35 매핑은 전부 정확.

**Source Excerpts**

1. Chunk `197674093189403324`

> ## 7. 출처 - FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr - FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions - eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820 - Federal Register: 2024-01709 (제정), 2025-21955 (기술적 수정) - FDA Compliance Program 7382.850 - 확인일: 2026-05-25

2. Chunk `211815826167619677`

> ## 1. 규정 개요 | 항목 | 내용 | |------|------| | 규정 | 21 CFR Part 820 | | 명칭 변경 | Quality System Regulation(QSR) → **Quality Management System Regulation(QMSR)** | | 최종규칙 공포 | Federal Register 2024-01709 (2024.2.2) | | 기술적 수정 | Federal Register 2025-21955 | | **발효일** | **2026년 2월 2일** | | 핵심 변경 | ISO 13485:2016을 참조편입(Incorporation by Reference)하고, FDA 추가요구를 별도 조항으로 보존 |

### kb-eval-20261126-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_us-004", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "5f0b06c4f5532d0e", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md", "source_hash": "5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `5f0b06c4f5532d0e`
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

### 1. Device Synopsis (placeholder)  
*The source does not provide a device description or intended use.* A concrete product definition is required before any definitive classification can be assigned.  

---

### 2. Classification & Submission Pathway  

| Item | Assessment |
|------|------------|
| **Regulatory panel** | Likely **21 CFR Part 892 (Imaging / Radiology)** if the device performs image acquisition, processing or storage; otherwise **Part 862** is *not* appropriate for imaging systems. |
| **Class** | Assuming a typical AI/ML‑enabled diagnostic or analysis software, the default would be **Class II** (510(k)‑eligible). |
| **Submission route** | **Traditional 510(k) Premarket Notification** – requires demonstration of **substantial equivalence** to a cleared predicate and compliance with **QMSR (Part 820)**. <br>*If the device is novel without an appropriate predicate, a **De Novo** request would be required.* |
| **Citations** | 21 CFR §807 – Premarket notification; 21 CFR §892.2050 – Class II medical image management and processing system (if applicable). |

> **Human‑escalation trigger:** Absence of a clear intended use or predicate → request detailed product description before finalizing the classification.

---

### 3. Required Evidence Package  

| Regulatory Requirement | Evidence Needed | Supporting Standard / Regulation |
|------------------------|----------------|-----------------------------------|
| **Design Controls** | Design History File (DHF) containing design inputs, outputs, verification/validation plans & reports, and design reviews. | ISO 13485:2016 – §7.3 (design controls) referenced in **21 CFR §820.10** (applicability). |
| **Risk Management** | Risk analysis file (ISO 14971:2019), risk control measures, residual risk justification, post‑market surveillance plan. | ISO 14971:2019; FDA guidance on risk management for devices. |
| **Software Lifecycle** | IEC 62304 (2006+A1:2015) development & maintenance plan, verification/validation activities, and a **Predetermined Change Control Plan (PCCP)** for AI/ML updates (FDA Guidance Dec‑2024). | IEC 62304; PCCP requirement. |
| **Usability / Human Factors** | IEC 62366‑1 (2015+A1:2020) usability engineering file & validation results. | IEC 62366‑1. |
| **Labeling & UDI** | Label with plain‑text UDI + AIDC symbol; UDI record in GUDID. | 21 CFR §801.20–§801.50 (label), 21 CFR §830.20, §830.300‑§830.360 (UDI system). |
| **Sterilization & Biocompatibility** *(if applicable)* | ISO 11135/11137 for sterilization validation; ISO 10993 series for biocompatibility testing reports. | ISO 11135, ISO 11137, ISO 10993 (multiple parts). |
| **Electrical Safety / EMC** *(if hardware present)* | IEC 60601‑1 family compliance test reports. | IEC 60601‑1 (2005+A1:2012+A2:2020). |

> **Human‑escalation trigger:** Any missing element above (e.g., no PCCP, incomplete DHF) → pause submission preparation and assign to design/control team.

---

### 4. Gaps Identified in Source & Required Actions  

| Gap (from source) | Required Action | Regulatory Basis |
|-------------------|----------------|------------------|
| **No MDR decision‑document SOP** – domestic SOP lacks “ML‑MDR‑001” form. | Draft and implement SOP for EU MDR decision documentation, even if only for internal reference; ensure traceability to FDA design‑control requirements. | ISO 13485 §7.3 (design output control) & **no specific identifier found in source — verify separately**. |
| **Fragmented UDI master data** – UDI Data Record (UDR) not consolidated. | Create a unified **UDI Master Record SOP** covering §820.35(b) and 21 CFR §830 requirements; integrate with GUDID submission process. | 21 CFR §820.35(b); 21 CFR §830 (UDI system). |
| **Audit‑report narrative insufficient** – lack of objective evidence citations. | Revise internal audit reporting template to require explicit citation of supporting records (e.g., test reports, verification logs). | ISO 13485 §8.2.2 (documented information) & **no specific identifier found in source — verify separately**. |
| **Unclear scope of electronic signatures** – Part 11 applicability undefined. | Issue “QM‑IT‑001” SOP defining when 21 CFR Part 11 applies (e.g., for DHF documents, complaint files). | 21 CFR §11.10 (electronic signatures); ISO 13485 §7.5 (document control). |
| **AI/ML regulatory alignment** – EU AI Act cited but no US‑specific pathway. | Develop a **PCCP** outlining permissible algorithm updates, performance monitoring, and FDA pre‑market notification of major changes. | FDA Guidance “Predetermined Change Control Plan” Dec‑2024. |

> **Human‑escalation trigger:** Any of the above SOPs remain incomplete after two review cycles → elevate to Quality Management System lead for corrective action plan.

---

### 5. Risk Controls (selected)  

| Hazard Category | Control Measure | Evidence Requirement |
|-----------------|----------------|----------------------|
| Software malfunction leading to incorrect diagnosis | Implement IEC 62304‑based development lifecycle; perform unit, integration and system verification; conduct clinical validation. | Verification & Validation reports, software risk analysis (ISO 14971). |
| Incorrect UDI labeling causing traceability loss | Apply dual‑format UDI on label per 21 CFR §801.20–§801.50; maintain master record per §820.35(b). | Label artwork approval, UDI Master Record SOP. |
| Data security breach of AI model updates | Define Access Control & Encryption in compliance with 21 CFR Part 11 and applicable cybersecurity guidance (FDA “Content of Premarket Submissions for Management of Cybersecurity”). | Cybersecurity risk assessment, incident response plan. |
| Sterilization failure (if hardware) | Validate sterilization cycle per ISO 11135/11137; conduct routine bioburden monitoring. | Sterilization validation report, periodic performance qualification data. |

---

### 6. Human‑Escalation Triggers Summary  

| Situation | Trigger Point | Escalation Owner |
|-----------|----------------|------------------|
| Undefined device intended use / missing predicate | No clear classification can be assigned. | Project Lead → Regulatory Strategy Team |
| Incomplete Design History File (missing design verification) | DHF audit finds gaps >2 items. | QMS Manager |
| Absence of PCCP for AI/ML updates | No documented change‑control plan before software release. | Software QA Lead |
| UDI Master Record not consolidated | Discrepancy between label and GUDID submission. | Labeling & Packaging Lead |
| Part 11 scope undefined for critical records | Electronic signatures applied inconsistently. | IT / Compliance Officer |
| Any identified gap remains unresolved after two review cycles (see Gap table) | Persistent SOP draft or missing evidence. | Quality Assurance Director |

---

### 7. Peer‑Review Prompt  

> **To a fellow RA:**  
> Please examine the assumptions made about device classification without an explicit intended use, verify that the cited CFR sections match the most current QMSR framework (effective 02‑Feb‑2026), and challenge any potential jurisdictional oversights—especially regarding EU MDR references, AI/ML change‑control expectations, and the applicability of Part 11 to electronic signatures in design‑history documents.  

--- 

*Prepared by: Mike – US Regulatory Affairs Specialist*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. §7.3 매핑·PCCP·Part 11 §11.10·UDI 전부 정확. 미세: 'ISO 13485 §7.3 referenced in §820.10(applicability)' 귀속 다소 부정확·'§820.35(b)' 서비스 기록 근거는 KB 기반.

**Source Excerpts**

1. Chunk `1061533089543682126`

> ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적용 | | AI/ML 기기 | OJEU/MDCG 단독 등재 없음 → EU AI Act 병행 필요(후속 과제) | | 운영 영향 | 체크리스트에 H/S 컬럼 신설, 개정판 번호(A11, A1, A2) 기재 의무화 |

2. Chunk `1066441905930561439`

> ### Gap → 조치 | Gap | 조치 | |-----|------| | 국내 SOP에 MDR 결정문서 양식 부재 | 양식 ML-MDR-001 초안(보고/미보고 결정트리) 신설 | | UDI 마스터 레코드 단편화 | UDR(UDI Data Record) 통합 관리 SOP 초안 (§820.35(b) + 21 CFR 830 + EU MDR Art.27) | | 내부감사 보고서 서술 수준 | "외부감사 대응 수준" 템플릿 개정 (객관적 증거 필수 인용) | | 전자서명 범위 모호 | Part 11 적용범위 정의 문서(QM-IT-001) 초안 예정 |

### kb-eval-20261126-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "QSR"], "profile_id": "ra-us", "scenario_id": "927f168f6aed2be5", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/QSR_21CFR820/README.md", "source_hash": "5250406488094d588d38eb1e45c2d8d4b90f093334322d2ded3d50d3a2e72871"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `927f168f6aed2be5`
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

> **Regulatory Draft – X‑ray Diagnostic Imaging System (Design‑Control & QMSR Readiness)**  

---

### 1. Device Classification & Submission Route  
| Item | Determination | Supporting Reference |
|------|----------------|----------------------|
| **Device class** | Class II, “Diagnostic X‑ray System” | 21 CFR Part 892 (Imaging devices) – class II for diagnostic radiology equipment (framework reference). |
| **Special controls** | Must meet the performance standards in **21 CFR §1020.30–§1020.32** (Radiation Control – Performance Standards for Diagnostic X‑ray Systems) and record/report requirements of **21 CFR §1002**. | Directly quoted in source excerpt [1]. |
| **Premarket pathway** | 510(k) – Substantial equivalence to a cleared predicate device that is also compliant with the above special controls. | Standard 510(k) requirement for Class II devices (framework reference). |
| **Alternative pathway** | If no suitable predicate exists, consider a **De Novo classification request** (21 CFR §809). | Standard guidance; not cited in source (no identifier found). |

---

### 2. Evidence Package Required for 510(k) Submission  

| Category | Specific Evidence | Rationale / FDA Expectation |
|----------|-------------------|-----------------------------|
| **Predicate identification** | Cleared 510(k) number(s), device name, intended use, and how the new device is at least as safe/effective. | Establishes substantial equivalence. |
| **Performance testing (radiation safety)** | • Beam quality & output consistency<br>• Patient dose measurements (entrance skin dose, DAP)<br>• Alignment with limits in 21 CFR §1020.30‑32 | Demonstrates compliance with the radiation performance standards quoted in source [1]. |
| **Electrical safety & EM compatibility** | IEC 60601‑1 (2005+A1:2012+A2:2020) testing report. | Required for any electrically powered medical device. |
| **Software/firmware validation** (if applicable) | IEC 62304 (2006+A1:2015) development and verification/validation documentation, plus a Predetermined Change Control Plan (PCCP) if AI/ML components are present. | Aligns with current FDA guidance on software‑based devices. |
| **Risk Management File** | ISO 14971:2019 risk analysis, evaluation, mitigation plan; summary in the Design History File (DHF). | Required for all Class II submissions. |
| **Human Factors/Usability Engineering** | IEC 62366‑1 (2015+A1:2020) usability validation report. | Supports safety of operator interaction with radiation controls. |
| **Labeling & IFU** | Full labeling package meeting 21 CFR §801 requirements; includes symbols, warnings, and instructions for safe X‑ray operation. | Labeling compliance (framework reference). |
| **UDI assignment** | UDI label on device and packaging per 21 CFR §801.20+; GUDID submission under 21 CFR §830.300‑360. | UDI regulatory obligations (framework reference). |
| **Quality Management System evidence** | ISO 13485:2016–aligned QMS documentation (quality manual, SOPs, design controls, production controls, complaint handling) and a statement of compliance with the **new QMSR (21 CFR Part 820, effective 2‑Feb‑2026)**. | Directly drawn from source excerpt [2]. |
| **Sterilization/Reprocessing** *(if applicable)* | Validation report per ISO 14937 and FDA‐recognized sterilization standards; device labeling reflecting any re‑sterilization limits. | Standard for reusable devices. |

---

### 3. Missing Information (Gap Analysis)

| Gap | Impact if Unresolved | Action Needed |
|-----|----------------------|---------------|
| **Exact intended use & clinical indications** | Prevents predicate selection and risk assessment. | Draft a clear Intended Use Statement. |
| **Identification of a suitable predicate device** | Blocks 510(k) pathway; may force De Novo. | Conduct market search for cleared X‑ray systems meeting the same performance standards. |
| **Detailed design specifications (hardware, software architecture)** | Needed for design‑control documentation and risk analysis. | Compile engineering drawings, block diagrams, and software flowcharts. |
| **Prototype testing plan & schedule** | Required to generate verification/validation data. | Develop a test protocol aligned with 21 CFR §1020.30‑32 limits. |
| **Labeling mock‑ups (including UDI placement)** | Label review will be delayed; FDA may issue an additional information request. | Produce draft labeling compliant with 21 CFR §801.20+. |
| **QMS maturity evidence (ISO 13485:2016 audit report post‑Feb 2026)** | Non‑conformance to the new QMSR; submission could be rejected. | Perform a pre‑submission internal audit and remediate findings. |
| **Risk Management Summary** | Incomplete DHF – FDA will request supplemental risk analysis. | Complete ISO 14971:2019 risk assessment covering radiation hazards, electrical safety, and user error scenarios. |
| **Software Change Control Plan (if software present)** | Lack of PCCP may trigger a 510(k) additional information request for future updates. | Draft a Predetermined Change Control Plan per FDA Dec‑2024 guidance. |

---

### 4. Key Risk Controls (per ISO 14971 & IEC 62366‑1)

| Hazard | Control Measure | Verification |
|--------|-----------------|--------------|
| Excessive patient dose (radiation overexposure) | • Automatic exposure termination interlock<br>• Real‑time dose monitoring and display<br>• Pre‑set dose limits per 21 CFR §1020.30‑32 | Test beam output under worst‑case conditions; verify compliance with dose limits. |
| Operator misuse of controls (e.g., accidental activation) | • Two‑handed trigger or foot pedal requirement<br>• Clear visual/audible warnings before exposure | Human factors validation (task analysis, usability testing). |
| Electrical shock / fire hazard | • IEC 60601‑1 compliant isolation and leakage current control<br>• Protective earth grounding verification | Electrical safety test report. |
| Software error leading to incorrect exposure parameters | • Software version control, code review, and unit testing<br>• PCCP for future algorithm updates | IEC 62304 software validation documentation. |
| Failure of dose‑monitoring sensor | • Redundant sensor architecture or fail‑safe default (no exposure) | Fault injection testing; verify safe state. |

---

### 5. Citations

| Item | Citation Type | Reference |
|------|---------------|-----------|
| Radiation performance standards for diagnostic X‑ray systems | Framework reference (appears in source) | **21 CFR §1020.30–§1020.32** – cited in source excerpt [1]. |
| Records & reports for radiation‑emitting products | Framework reference (appears in source) | **21 CFR §1002** – cited in source excerpt [1]. |
| QMSR amendment aligning with ISO 13485:2016 | Framework reference (appears in source) | **21 CFR Part 820**, effective 02‑Feb‑2026 – cited in source excerpt [2]. |
| General device classification for imaging equipment | Framework reference (standard regulatory structure) | **21 CFR Part 892** – class II for diagnostic X‑ray systems. |
| Labeling requirements | Framework reference (FDA regulation) | **21 CFR Part 801**, subpart B (§801.20 onward). |
| UDI system obligations | Framework reference (FDA regulations) | **21 CFR Part 830** (formatting, GUDID) and **21 CFR Part 801** (label placement). |
| No specific device‑specific identifiers (e.g., cleared 510(k) numbers) were provided in the source material. “No specific identifier found in source – verify separately.” |

---

### 6. Human‑Escalation Triggers  

| Situation | Who Must Be Notified / Escalated To | Deadline / Action |
|-----------|--------------------------------------|--------------------|
| **Absence of a suitable predicate** after exhaustive search | Senior Regulatory Lead & Project Manager | Immediate – initiate De Novo feasibility assessment. |
| **Failure to meet any dose limit in 21 CFR §1020.30‑32 testing** | Chief Technology Officer & QA Director | Halt testing; redesign exposure control circuitry before further development. |
| **QMS audit identifies non‑conformity to the new QMSR (post‑Feb 2026)** | Quality Assurance Manager → Executive Management | Corrective actions must be completed *prior* to compiling the 510(k) submission. |
| **FDA issues an Additional Information (AI) request** | Regulatory Affairs Lead | Respond within the statutory 180‑day window; if response requires new data, trigger a project schedule review. |
| **Software change requiring updates to PCCP** | Software Development Lead & Regulatory Affairs | Submit updated PCCP as part of any future 510(k) supplement; track in change‑control log. |
| **Labeling or UDI non‑compliance identified by internal review** | Labeling/Branding Manager → QA | Revise labeling and re‑submit to FDA before final submission packaging. |

---

### 7. Next Steps (Actionable Checklist)

1. Define precise Intended Use & Indications.  
2. Identify and document a qualified predicate device (clearance number).  
3. Finalize design specifications and populate the DHF.  
4. Conduct performance testing per **21 CFR §1020.30‑32**; compile test reports.  
5. Complete ISO 14971 risk analysis & IEC 62366‑1 usability validation.  
6. Prepare labeling package (including UDI placement) compliant with **21 CFR §801** and **§830**.  
7. Verify QMSR compliance (ISO 13485:2016 audit, SOPs aligned to new Part 820).  
8. Draft the 510(k) submission docket (cover letter, summary of safety and effectiveness, etc.).  

---

### Peer Review Prompt
> *Could a fellow RA colleague challenge any of the assumptions made above—particularly the classification under Part 892 versus a possible alternate regulation, the sufficiency of the identified special controls, or gaps in the QMSR evidence required for a post‑Feb 2026 submission? Please identify any jurisdiction‑specific nuances that might have been missed.*

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

> 'De Novo classification request (21 CFR §809)' 오인용 — Part 809는 IVD 제품, De Novo는 §513(f)(2)+21 CFR Part 860 Subpart D. 나머지 우수: §1020.30-32 방사선 성능기준을 특별관리로 정확 처리(11-24 us-003 오서술과 대조)·§1002·QMSR.

**Source Excerpts**

1. Chunk `136831192110451403`

> ## 추가 규제 (X-ray 관련) - **21 CFR Part 1020.30 ~ 1020.32**: Radiation Control – Performance Standards for Diagnostic X-ray Systems - **21 CFR Part 1002**: Records and Reports (Radiation-Emitting Products) - **21 CFR Part 1040**: Performance Standards for Light-Emitting Products (관련 시)

2. Chunk `18877965943708175`

> ## 현황 - 기존 QSR(21 CFR 820)은 2024년 공표된 Quality Management System Regulation (QMSR)으로 개정됨. - **시행일: 2026년 2월 2일** → ISO 13485:2016과 정합화.

## ra_eu

### kb-eval-20261126-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "763748970e329f2e", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `763748970e329f2e`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & PMCF Planning  
(Three in‑house products: X‑ray Detector, Handheld X‑ray Source, GUI Software)**  

---

## 1. Product overview & classification  

| # | Product | Intended use (as derived from source) | MDR Classification rule* | MDR Class | Conformity‑assessment route (Art 52) |
|---|---------|----------------------------------------|--------------------------|-----------|--------------------------------------|
| 1 | **X‑ray Detector** | Detects X‑ray photons for diagnostic imaging (radiography / fluoroscopy). | Rule 10 – “recording limb” of X‑ray equipment (IEC 60601‑2‑54 family) | **IIa** | Art 52(6): **Annex IX** (QMS + technical‑documentation assessment of a representative device). NB involvement required. |
| 2 | **Handheld X‑ray Source** | Generates ionising radiation for point‑of‑care imaging; portable, battery‑powered. | Rule 10 – “radiology limb” (emits ionising radiation) | **IIb** | Art 52(4): **Annex IX** (full QMS + technical‑documentation assessment) *or* Annex X + XI (type‑examination & production conformity verification). NB involvement required. |
| 3 | **GUI Software (SaMD)** | Provides image display, processing and decision support for X‑ray examinations. | Rule 11 – software giving diagnostic information; impact on clinical decision is moderate → IIa | **IIa** | Art 52(6): **Annex IX** (QMS + technical‑documentation assessment). NB involvement required. |

\*Framework reference only – no specific identifier appears in the source excerpts.

---

## 2. Required evidence per product  

| Evidence type | X‑ray Detector (IIa) | Handheld Source (IIb) | GUI Software (IIa) |
|---|---|---|---|
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | Required; to reference IEC 62220‑1‑1 DQE test data. | Required; to reference dose‑monitoring studies & clinical safety data on handheld use. | Required; to reference usability/clinical performance literature (PubMed, registries). |
| **Risk Management File (RMF)** – Annex I §3 | Required; must address DQE degradation, pixel defects, patient dose exceedance, mechanical damage. | Required; must cover ionising‑radiation hazards, battery failure, mechanical safety, ergonomic risk. | Required; must include software hazard analysis (IEC 62304), usability risks (IEC 62366‑1), error handling. |
| **Post‑Market Surveillance (PMS) Plan** – Art 84 | Required; data sources listed in Table 1 of source (DQE, pixel defects, dose). | Required; includes radiation‑dose monitoring, mechanical damage, battery status. | Required; includes software error logs, UI usability complaints. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** – Annex XIV Part B | *Decision pending* after equivalence claim review (source: “동등성 클레임 검토 후 결정”). | Mandatory – “활발히 임상 데이터 수집 권고” (active collection of clinical data on ionising radiation use). | Mandatory – “사용 중 오류 데이터 수집 필수” (continuous error‑data capture). |
| **Periodic Safety Update Report (PSUR)** – Art 86 | Cadence **every 2 years** (source). | Cadence **every 1 year** (source). | Cadence **every 2 years** (source). |
| **EUDAMED obligations** – Art 33‑39 | UDI registration + vigilance reporting (source). | Same. | UDI registration (SaMD) + vigilance (source). |
| **Standards supporting conformity** | IEC 62220‑1‑1 (DQE measurement) – cited in source; IEC 60601‑2‑54 family for X‑ray equipment. | IEC 60601‑2‑28 (X‑ray tube), IEC 60601‑2‑54, IEC 62304 (software support for firmware). | IEC 62304 (software lifecycle), IEC 62366‑1 (usability engineering), IEC 81001‑5‑1 (eHealth), ISO 14971 (2019) risk management. |
| **Other supporting documentation** | Manufacturing records, calibration certificates, device‑specific labelling (Annex I §23). | Same plus battery qualification tests. | Software maintenance log, bug‑track database, change‑control records. |

*Where the source says “no specific identifier found in source — verify separately,” that applies to any regulatory citation that is not explicitly present (e.g., PSUR number, specific MDR article paragraph beyond those listed).*

---

## 3. Gaps / Missing Information  

| Gap | Impact on submission | Suggested remedial action |
|---|---|---|
| **Equivalence claim for X‑ray Detector** – source notes “PMCF 필요성 → 동등성 클레임 검토 후 결정”. | Without a documented equivalence justification, the NB cannot accept a reduced PMCF scope; may require full clinical data. | Compile a detailed equivalence dossier (technical & performance comparability) and obtain NB concurrence before finalising the PMCF plan. |
| **Quantitative thresholds for DQE degradation & dose‑overrun** – only “DQE 저하, 픽셀 결함, 환자선량 초과” listed as data sources. | PMS reports must contain predefined acceptance criteria; otherwise risk evaluation is incomplete (Annex I §8). | Define numeric limits (e.g., DQE drop >5 % triggers corrective action) and embed in RMF & PSUR content. |
| **PMCF objectives & success criteria for Handheld Source** – source recommends “임상 데이터 적극 수집” but no study design. | Art 83‑86 require a documented PMCF plan with clear endpoints; lack may be rejected by NB. | Draft a PMCF protocol (prospective observational registry, sample size, follow‑up duration) and align with MDCG guidance 2022‑21. |
| **Usability validation for GUI Software** – only “SW 오류, 영상 표시 오류, 사용성 이슈” listed as data sources; no IEC 62366‑1 test plan. | Annex I §22 demands addressing lay‑person use; without usability evidence the device may not meet GSPR. | Conduct a formal usability engineering study (task analysis, formative and summative testing) and attach results to the CER. |
| **Trend‑reporting methodology** – source shows quarterly internal statistics but no statistical method or triggers. | Art 88 requires trend reporting with defined thresholds; vague approach may be challenged. | Specify the statistical algorithm (e.g., EWMA chart, 95 % confidence) and define trigger levels for escalation. |
| **UDI registration evidence** – source states “UDI 등록” but does not provide registration number or database entry confirmation. | EUDAMED compliance (Art 33‑36) is mandatory for CE marking; missing proof may delay market access. | Complete UDI issuance with the issuing agency, capture the EUDAMED entry screenshot, and archive for audit. |
| **Vigilance reporting workflow** – “即시/분기” for serious incidents, but no SOP linking to Art 87 reporting timelines (within 15 days). | Non‑conformity with vigilance obligations may lead to regulatory action. | Draft a vigilance SOP showing incident triage, time‑to‑report calculation, and responsible persons. |

---

## 4. Risk‑control measures (aligned with Annex I §3‑9)  

| Product | Identified risk | Control measure(s) – reference |
|---|---|---|
| X‑ray Detector | DQE degradation → reduced image quality → diagnostic error | • Periodic performance verification (IEC 62220‑1‑1). <br>• Automated alert when DQE falls below defined threshold (RMF §4). |
|  | Pixel defect accumulation → artefacts | • Self‑diagnostic pixel mapping; replace detector module if >X defective pixels. |
|  | Patient dose exceeding reference levels | • Real‑time dose monitoring & display; software interlocks to limit exposure time per protocol (GSPR §16.4). |
| Handheld Source | Uncontrolled ionising radiation → overexposure | • Integrated dosimeter with hard stop; lock‑out after preset cumulative dose (GSPR §16.4). <br>• Battery failure leading to uncontrolled emission – implement battery health monitoring and automatic shutdown (GSPR §7). |
|  | Mechanical damage during transport → device malfunction | • Robust packaging, shock sensor logging; non‑conformity triggers corrective action (GSPR §20). |
| GUI Software | Incorrect image rendering / processing error → misdiagnosis | • IEC 62304 development lifecycle; verification & validation test reports. <br>• Redundant algorithm cross‑check; automatic rollback on fault detection (GSPR §17). |
|  | Usability errors by lay users → inappropriate parameter selection | • IEC 62366‑1 usability engineering; clear UI labeling (GSPR §23). <br>• Context‑sensitive help & error messages. |
| All three | Post‑market adverse events not reported timely | • Vigilance SOP aligned with Art 87 (15‑day reporting); designated responsible person. |

---

## 5. PMS / PMCF data flow (derived from source Table 1 & 1.1(a))

1. **Data sources** – serious incidents, complaints, trend reports, literature, user feedback, competitor TDs (source: “정보 수집원”).  
2. **Collection frequency** – immediate/quarterly for serious events; monthly for non‑serious; quarterly trend; semi‑annual literature & competitor data.  
3. **Processing** – entry into a central PMS database (EUDAMED‑compatible), automatic flagging based on thresholds defined in RMF.  
4. **Analysis** – quarterly internal review; PSUR drafting per cadence (2 yr for IIa, 1 yr for IIb).  
5. **PMCF execution** – prospective registry (handheld source); error‑log aggregation (GUI software); equivalence assessment & possibly clinical study (detector).  

---

## 6. Human‑escalation triggers  

| Trigger | Condition | Action / Escalation |
|---|---|---|
| **Serious incident** | Any report classified as “serious” in vigilance system. | Immediate notification to Competent Authority & NB within 15 days (Art 87). Activate corrective action plan. |
| **Dose‑overrun** | Measured patient dose > defined reference level on any procedure. | Stop device use, perform root‑cause analysis, issue Field Safety Corrective Action (FSCA) if needed; notify NB. |
| **DQE fall below threshold** | DQE degradation >5 % (example limit). | Generate trend alert, schedule corrective maintenance, update PSUR. |
| **Software error rate spike** | Monthly bug‑log > baseline + 2 σ. | Initiate software patch release; inform NB if classified as safety‑related. |
| **Monthly complaint surge** | Complaints increase >30 % vs previous month without resolution. | Conduct urgent CAPA review, report in next PSUR, consider interim field notice. |
| **Missed PSUR deadline** | PSUR not submitted within required cadence (2 yr IIa / 1 yr IIb). | Escalate to senior RA manager; prepare provisional update for NB and document reason for delay. |
| **Equivalence claim rejection** | NB does not accept equivalence dossier for detector. | Suspend PMCF reduction, launch full clinical investigation per MDR Annex XIV Part A. |

---

## 7. Regulatory judgment & next steps  

1. **Classification & route confirmed:** Detector (IIa – Annex IX), Handheld Source (IIb – Annex IX or X+XI), GUI Software (IIa – Annex IX).  
2. **Evidence package** must include CER, RMF, PMS plan, PMCF protocol (full for handheld source and software; conditional for detector after equivalence assessment), PSURs with appropriate cadence, UDI/vigilance records in EUDAMED.  
3. **Key gaps** – equivalence justification for detector, quantitative PMS thresholds, detailed PMCF study design, usability validation for software, trend‑reporting methodology, completed UDI registration evidence, full vigilance SOP.  

**Human‑escalation triggers** are defined (see Section 6). Any occurrence of the listed conditions must be raised to the RA lead and notified to the Notified Body per MDR timelines.

---

## 8. Peer‑review request  

> **To fellow EU RA colleagues:**  
> Please challenge the assumptions above, especially:  
> * The applicability of Rule 10 (recording vs radiology limb) for the detector versus source – are there any mixed‑function features that could shift classification?  
> * Adequacy of the proposed quantitative thresholds (DQE, dose) – do they meet MDCG guidance on PMS performance criteria?  
> * Whether a single PSUR per product suffices given shared components (detector & source) or if a combined report is required under Art 86.  
> * Any missing EU‑wide obligations (e.g., Article 66 clinical investigation for pregnant users, Annex XV environmental considerations).  

Your feedback will be incorporated before final submission to the Notified Body.

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

> 심각 결함 없음. Rule 10 recording(IIa)/radiology(IIb) 구분·Rule 11·52(6)/(4)·PSUR 제품별 주기(Detector 2년/Source 1년/GUI 2년 — 롤백된 KB 정확 반영)·GSPR §8/§22/§16.4 전부 정확. [최종 2점 — shadow 11차 하향 수용: 'Annex I §22 demands addressing lay-person use' — §22는 일반인용 기기 조항인데 동 기기는 전문가용(trained technologists) GSPR 오적용(§5/§6이 사용성). 나머지(제품별 주기 표 포함)는 정확.]

**Source Excerpts**

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

### kb-eval-20261126-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "89bf647a10658cdd", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `89bf647a10658cdd`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning for an X‑ray Diagnostic Device and Associated SaMD**

---

### 1. Device Scope (as inferred from the source)

| Item | Description |
|------|-------------|
| **Primary hardware** | X‑ray generator that emits ionising radiation for diagnostic imaging. |
| **Software component** | Medical device software (SaMD) that processes/interprets the acquired images. |
| **Intended use** | “Diagnostic radiology – generation of X‑ray beams for projection radiography.” (to be confirmed with the manufacturer). |

*Source citations*:  
- Rule 10 – ionising‑radiation diagnostic device → Class IIb 【2】  
- Rule 11 – Medical Device Software (SaMD) classification 【2】

---

### 2. Classification & Conformity‑Assessment Route  

| Element | Regulation reference | Determination |
|---------|----------------------|---------------|
| **Hardware (X‑ray generator)** | MDR Annex VIII, **Rule 10** (radiology limb) → Class IIb | **Class IIb** |
| **SaMD** | MDR Annex VIII, **Rule 11** – classification depends on impact of the software decision. Assuming a diagnostic aid that does not cause death or irreversible deterioration, **Class IIa**; if it can lead to serious health deterioration, **Class IIb** (to be clarified). |
| **Conformity‑assessment route for Class IIb hardware** | Article 52(4) MDR – either: <br>• **Annex IX** (QMS + technical‑documentation assessment by a NB) **or** <br>• **Annex X** (EU type‑examination) + **Annex XI** (production conformity verification). | Both routes require a Notified Body; the choice depends on manufacturer strategy and NB capability. |
| **Conformity‑assessment route for SaMD (Class IIa/IIb)** | Same as above – Article 52(4) applies for Class IIa/IIb devices. | Use Annex IX (most common for software). |

*Additional citation*: Regulation (EU) 2023/607 – transitional amendment to MDR 【1】  

---

### 3. Required Evidence & Documentation  

| Section (TD/ PMS) | Minimum content (per MDR) | Specific artefacts expected |
|-------------------|--------------------------|-----------------------------|
| **Annex II – Technical Documentation** (§6.1) | 1‑6 as listed in Annex II. | • Device description, variants, intended use <br>• Design & manufacturing information <br>• GSPR compliance (Annex I) <br>• Risk Management File (ISO 14971:2019) <br>• Verification & validation reports (including IEC 60601‑2‑54, IEC 60601‑2‑28) |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | • State‑of‑the‑art literature review <br>• Clinical data from the device or equivalent devices <br>• Benefit–risk analysis |
| **Post‑Market Surveillance Plan** | Art. 84 MDR | • PMS system description (Art. 83) <br>• Data collection methods, KPIs, reporting timelines |
| **PMCF Plan & Evaluation Report** | Annex XIV Part B | • Objectives, protocol, data sources for the X‑ray generator and SaMD <br>– For Class IIb hardware, a *formal* PMCF plan is mandatory. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 MDR – annual for Class IIb | • Benefit–risk conclusions <br>• Main findings of PMCF <br>• Sales volume & user‑population estimate |
| **Labeling & IFU** | Annex I §23 | • Instructions for use, radiation safety statements, contraindications, UDI. |
| **Usability Engineering** | IEC 62366‑1 (2020) | Human factors analysis for safe operation by intended users. |
| **Software Lifecycle Documentation** | IEC 62304 (2006+A1:2015) | Software development plan, verification & validation, post‑market surveillance of software updates. |

---

### 4. Identified Gaps / Missing Information  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Precise Intended Use Statement** (including clinical indication, patient population) | Drives classification and clinical evidence scope. | Obtain a formal “Intended Use” description from the manufacturer. |
| **Risk Management File details** – especially radiation‑exposure risk assessment (§16.4 GSPR) | Needed for compliance with Annex I §16 & to justify risk controls in PSUR. | Complete FMEA/FMECA, quantify dose limits, demonstrate compliance with IEC 60601‑2‑54. |
| **Clinical data source** – is there a clinical investigation or existing performance data? | CER must be substantiated; for Class IIb a *clinical investigation* may be required unless sufficient equivalence can be demonstrated. | Provide trial reports or equivalence justification (including comparator device documentation). |
| **Software classification rationale** (SaMD) | Determines whether SaMD is Class IIa or IIb and thus the level of NB involvement. | Clarify decision impact; map to Rule 11 decision matrix. |
| **PMCF protocol specifics** – endpoints, data‑collection schedule, follow‑up duration | PMCF plan must be *specific* for Class IIb devices (Annex XIV Part B). | Draft a detailed PMCF study plan and obtain NB agreement. |
| **Labeling content for radiation safety** (e.g., warning symbols, dose limits) | Required by GSPR §16 & IEC standards; missing items cause non‑conformity. | Create/validate labeling with radiation protection experts. |
| **UDI implementation details** (EUDAMED registration) | Mandatory under Art. 33‑39 MDR for Class IIb onward. | Register device and assign UDI in EUDAMED. |

---

### 5. Risk Controls (aligned to GSPR §§3‑8 & relevant IEC standards)

| Hazard | Control measure | Regulatory reference |
|--------|-----------------|----------------------|
| **Ionising radiation exposure** | • Shielding, interlocks, dose‑monitoring, compliance with IEC 60601‑2‑54 <br>• Operator training and warning labels (GSPR §16.4) | Annex I §§3‑8; IEC 60601‑2‑54 |
| **Electrical safety of X‑ray tube** | Design according to IEC 60601‑2‑28, protective earth, leakage current limits | Annex I §20; IEC 60601‑2‑28 |
| **Software malfunction (image processing)** | Development per IEC 62304, verification/validation testing, cyber‑security measures (IEC 62443 baseline) | Annex I §§3, 17; IEC 62304 |
| **Use‑error (operator mis‑positioning)** | Usability engineering per IEC 62366‑1, clear ergonomic controls, mandatory checklists in IFU | Annex I §§5, 22; IEC 62366‑1 |
| **Mechanical failure of gantry** | Finite‑element analysis, endurance testing, routine maintenance schedule (GSPR §20) | Annex I §20 |

---

### 6. Human‑Escalation Triggers  

| Trigger | Condition | Required action |
|---------|-----------|-----------------|
| **Unclear intended use / indication** | No definitive statement from manufacturer. | Stop classification work; request formal Intended Use documentation before proceeding. |
| **Insufficient clinical evidence** | No CE‑marked equivalent or no clinical investigation report available. | Escalate to Clinical Evaluation Lead – decide whether a new clinical investigation is required. |
| **Risk Management File incomplete** (e.g., missing residual risk evaluation for radiation) | Gap identified in the RMF review checklist. | Notify the Risk Management Team; defer NB submission until completed. |
| **PMCF plan not specific enough** (missing endpoints, data‑source description) | Review of PMCF draft shows generic statements only. | Escalate to PMCF Coordinator for detailed protocol drafting; involve NB early for feedback. |
| **PSUR cadence not defined** (annual vs biennial) | Uncertainty about reporting interval for Class IIb hardware. | Confirm with the NB; schedule PSUR preparation accordingly. |
| **Labeling gaps (radiation warnings, UDI)** | Draft IFU lacks required symbols or UDI placement. | Send to Labeling Specialist; halt dossier finalisation until resolved. |
| **EUDAMED registration pending** | Device not yet entered in EUDAMED database. | Escalate to Regulatory Affairs Manager – initiate EUDAMED entry before CE‑marking issuance. |

When any of the above triggers appear, the responsible RA should log a *non‑conformity* in the project tracker and raise it for **human review** prior to proceeding with the Notified Body submission.

---

### 7. Summary Judgment  

- The X‑ray generator is **Class IIb** under MDR Rule 10 (ionising radiation diagnostic device).  
- Applicable conformity‑assessment routes are **Annex IX** (QMS + TD assessment) *or* **Annex X + XI** (type‑examination + production verification) per Article 52(4).  
- A robust **PMS system**, **PMCF plan**, and **annual PSUR** are mandatory (Arts 83‑86).  
- The current dossier lacks a definitive intended‑use statement, complete risk management evidence for radiation exposure, and a detailed PMCF protocol – all must be supplied before NB assessment.  

---

### 8. Peer‑Review Prompt  

> *Colleague, please challenge the assumptions above:*
> - *Is Rule 10 definitively the correct rule for this X‑ray generator, or might another sub‑rule (e.g., “radiation‑emitting device” vs “recording limb”) apply?*  
> - *Does the SaMD component warrant a Class IIb classification under Rule 11 given its decision impact?*  
> - *Are there any MDR amendments or MDCG guidance (post‑2023) that modify the PMCF evidence requirements for Class IIb devices that we have not captured?*  
> - *Identify any missing references to specific IEC standards (e.g., IEC 60601‑2‑54 Annex E radiation safety tests) that should be explicitly listed.*  

Your feedback will be incorporated before finalising the submission package.

**Citation Lint (C1/C3 — 구조적 인용 오류 자동 감지)**

- ⚠️ Art. 52(4) is inconsistent with the device class on this line (Class IIa (52(6))) — verify the paragraph against MDR Art. 52. (`Article 52(4)`)

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

> ① 'SaMD(Class IIa/IIb) 경로: Article 52(4) applies for Class IIa/IIb' — IIa는 52(6)(사실표 확정값 위반) ② TD 전체를 'Annex II §6.1'로 귀속(재발 패턴 — §6.1=preclinical/clinical). PSUR annual IIb·52(4) IIb 경로는 정확.

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261126-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "9329ffadb355b75e", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `9329ffadb355b75e`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) / Post‑Market Clinical Follow‑up (PMCF) Planning  
(Primary focus: identification of classification, conformity‑assessment route, evidentiary gaps, risk‑control measures, and escalation triggers)**  

---

### 1. Device Classification

| Step | Action | Reference |
|------|--------|-----------|
| 1.1 | Apply the **self‑classification** principle – the manufacturer is responsible for determining the class. | Article 51 + Annex VIII (see source excerpt [2]) |
| 1.2 | Sequentially evaluate the **22 rules of Annex VIII**; adopt the highest applicable rule. | Annex VIII, Rule 1–22 (framework) |
| 1.3 | If uncertainty remains, seek clarification from the Competent Authority (CA) or consult the MDCG “Borderline and Classification” guidance (latest version v2.1.1 – 2023‑09). | MDCG Manual v2.1.1 (external reference) |

> **Action required:** The manufacturer must supply the intended purpose, mode of action, and any applicable rule numbers (e.g., Rule 9, Rule 10, etc.) for the classification decision. *Current source does not provide these details – **verify separately**.*

---

### 2. Conformity‑Assessment Route (Art. 52)

| Determined Class | Required Annex(es) | NB involvement? |
|------------------|-------------------|-----------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration – technical documentation (Annex II & III) + EU Declaration of Conformity (Art. 19/Annex IV) | No |
| **Class Is / Im / Ir** | Annex IX Chapters I & III *or* Annex XI Part A (limited scope for sterile/measuring/reusable aspects) | Yes (limited) |
| **Class IIa** | Annex IX Chapters I & III + technical‑documentation assessment of one representative device per category (**Art. 52(6)**) | Yes |
| **Class IIb** | Annex IX Chapters I & III + technical‑documentation assessment of one representative device per generic group (**Art. 52(4)**)  *or* Annex X (type‑examination) + Annex XI (production verification) | Yes |
| **Class III** | Annex IX full technical‑documentation assessment **or** Annex X + Annex XI | Yes |

> **Action required:** Once the class is confirmed, select the appropriate route and contract a Notified Body (NB) accordingly. *If the device falls under Class IIb/III, an NB audit will be mandatory.*  

---

### 3. Required Evidential Packages for PMS / PMCF

| Evidence | Where it belongs in the technical file | Legal basis |
|----------|----------------------------------------|-------------|
| **PMS Plan** (process description, data sources, triggers) | Annex III (post‑market surveillance technical documentation) | Art. 84 MDR |
| **PMS Report** (for Class I devices) | Annex III – part of the PMS system | Art. 85 MDR |
| **Periodic Safety Update Report (PSUR)** (Class IIa/IIb/III) | Annex III – periodic safety update report | Art. 86 MDR |
| **Clinical Evaluation Report (CER)** – up‑to‑date, addressing state of the art and benefit–risk | Annex XIV Part A; kept current under Art. 61 | — |
| **PMCF Plan** (planned post‑market clinical follow‑up studies) | Annex XIV Part B | — |
| **PMCF Evaluation Report** (results of executed PMCF activities) | Annex XIV Part B | — |
| **Vigilance / Serious Incident Reporting** (notification to CA, FSCA where needed) | Integrated in PMS system; reporting per Article 87 | MDR Art. 87 (source excerpt [1]) |
| **Unique Device Identification (UDI)** registration (EUDAMED) | Annex II §5.2 & MDR Art. 24 (reference UDI portal) | — |
| **Risk Management File** (RMF) – includes updates from PMS/PMCF | Annex I Chapter I §§3‑9 (risk management system) | — |

> **Missing information (to be verified):**  
> • Device‑specific intended use and indication (required to select the appropriate clinical evidence).  
> • Existing clinical data sources (e.g., literature search, registry data, prior investigations).  
> • Details of the PMS data collection methods (e.g. complaint handling system, field safety corrective action procedures).  
> • Planned PMCF study design (sample size, endpoints, follow‑up duration). *All items are not present in the source – **verify separately**.*

---

### 4. Risk Controls Related to PMS/PMCF

| Requirement | How it is addressed |
|-------------|---------------------|
| **Risk Management System** – continuous update of residual risk based on post‑market data. | Annex I Chapter I §3 (RMF) – integrate findings from PMS reports, PSUR, and PMCF results into the RMF. |
| **Risk Control Measures** – implement corrective actions when trends indicate unacceptable risk. | Annex I §4 (risk control) – define action thresholds in the PMS plan (e.g., >2 % serious incident rate). |
| **Use‑Error Mitigation** – monitor user feedback, training gaps. | Annex I §5 (use‑error risks). |
| **Device Lifetime & Degradation Monitoring** – especially for reusable or implantable devices. | Annex I §6 (device lifetime) – incorporate degradation data from PMCF into maintenance schedules. |
| **Transport/Storage Risks** – ensure that post‑market handling does not introduce new hazards. | Annex I §7. |
| **Known & Foreseeable Risks vs Benefits** – updated benefit–risk conclusions in CER after PMS. | Annex I §8 (benefit‑risk). |

---

### 5. Human‑Escalation Triggers

| Trigger | Reason for escalation | Who must act |
|---------|-----------------------|---------------|
| **Uncertain classification or borderline rule** | Need CA clarification to avoid mis‑classifying the device. | Manufacturer → Competent Authority (CA) / MDCG guidance. |
| **Absence of sufficient clinical data** (no valid CER, no PMCF protocol) | Cannot satisfy Annex XIV Part A/B requirements; NB will reject submission. | Manufacturer → Clinical affairs lead to source appropriate evidence. |
| **Adverse‑event trend exceeding pre‑defined thresholds** (e.g., increase in serious incidents > 5 % of units) | Immediate need for Field Safety Corrective Action (FSCA). | PMS manager → Authorized Representative → Notify CA per Art. 87. |
> **Escalation point:** Any finding that could affect the benefit–risk determination must be reported to the Notified Body within the next scheduled audit window.

---

### 6. Summary Judgment

1. **Classification** – to be finalised after receipt of intended‑use documentation; apply Annex VIII sequentially (Article 51).  
2. **Conformity route** – will follow Art. 52 based on the class determined in step 1 (most likely Annex IX for Class IIa/IIb, or Annex X+XI for higher classes).  
3. **Evidence gap** – current source provides only general references to PMS and vigilance; no device‑specific clinical data, risk‑management updates, or PMCF study details are available. These must be gathered before a technical file can be considered complete.  
4. **Risk controls** – the RMF must be kept live, with explicit integration of PMS/PMCF findings per GSPR §§3‑8.  

**Immediate actions:**  
- Obtain and document the device’s intended purpose & mode of action.  
- Conduct the Annex VIII rule analysis and record the resulting class.  
- Draft a detailed PMS plan (Art. 84) and, if applicable, a PMCF plan (Annex XIV Part B).  
- Populate the risk‑management file with post‑market data handling procedures.  

---

### 7. Peer Review Prompt

> **To a fellow RA colleague:** Please review the assumptions made above regarding (a) the applicability of Annex VIII classification rules without knowledge of the device’s intended use, (b) the selection of the conformity‑assessment route based solely on class, and (c) any jurisdiction‑specific gaps that may arise from Korean regulatory references in the source (e.g., UDI portals, MFDS citations). Highlight missing evidence items or alternative interpretations of the MDR obligations that could affect the PMS/PMCF strategy.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. 22개 규칙·52(6)/(4) 경로·PSUR Annex III 위치 적절. 의심(미검증 기록): UDI 등록을 'MDR Art. 24'로 인용 — UDI 체계는 Art. 27(+Annex VI)로 아는데 Art. 24 미확인, 원문 확인 전 감점 없음.

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261126-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3aec490a3ca6f246", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "f68164060ffbb36f173c37bdab2d02883792ddc900791032ca30c683dc8a0173"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `3aec490a3ca6f246`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PMS_Plan_MDR_Article84_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `f68164060ffbb36f173c37bdab2d02883792ddc900791032ca30c683dc8a0173`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PMS_Plan_MDR_Article84_템플릿.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 3. PMS Plan 실용 템플릿 (MDCG 2025-10 기반) `[추가확인]` 표시 항목은 자사 확인 후 기재. --- | 마케팅/QA팀 | | **S10** | 규제 데이터베이스 | EUDAMED, MAUDE (FDA), MFDS 이상사례 DB | 분기별 | RA팀 |
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) / Post‑Market Clinical Follow‑up (PMCF) Planning**  
*Prepared for internal RA review (MDR 2017/745)*  

---

## 1. Device Description & Intended Use – Information Gap
| Item | Required by MDR | Current status (source) |
|------|-----------------|------------------------|
| **Device name / model** | Annex II §1.2 | not provided |
| **Intended purpose / indication(s)** | Annex II §1.3 | not provided |
| **Target population & user profile** | Annex II §1.4 | not provided |
| **Essential characteristics (e.g., invasive, active, measuring, sterile, implantable)** | Annex VIII classification rules | not provided |

> **Action:** Obtain a complete device description and intended‑use statement before any classification work can start.

---

## 2. Classification & Conformity‑Assessment Route – Preliminary Guidance  

| Step | Requirement | How to Apply (once use‑case is known) |
|------|-------------|---------------------------------------|
| **Identify applicable rule** (Annex VIII) | e.g., Rule 9, 10, 11, 17 or others depending on activity/technology | Use the device description to select the correct rule number. |
| **Determine class** | Rules map to Class I‑III as set out in Annex VIII. | Example: a non‑invasive, non‑active, non‑measuring device → Class I; an active therapeutic device → Class IIa/IIb etc. |
| **Select conformity‑assessment route (Art 52)** | – Art 52(7) for Class I (self‑declaration). <br>– Art 52(6) for Class IIa (Annex IX + NB technical‑doc assessment). <br>– Art 52(4) for Class IIb (Annex IX or Annex X + XI). <br>– Art 52(3) for Class III (Annex IX or Annex X + XI). | The route is fully defined once the class is known. |

*Citation:* MDR **Art 52** paragraphs and **Annex VIII** rule numbers – framework references (no verification caveat required).

---

## 3. PMS Plan – Core Elements Required by **Article 84** & MDCG 2025‑10  

| Requirement (MDR Art 84) | What must be documented | Current evidence from source |
|---------------------------|--------------------------|------------------------------|
| **PMS objectives and scope** | Overall goals, intended post‑market data to collect. | No specific statement – template only mentions “실용 템플릿”. |
| **Data sources & collection methods** | Clinical data, complaints, vigilance reports, literature, registries etc. | Table shows **EUDAMED**, **MAUDE (FDA)** and **MFDS 이상사례 DB** as sources – good start. |
| **Responsibility matrix** | Roles of Marketing/QA, RA, etc., with frequency of tasks. | Provided: “Marketing/QA팀” → S10 → quarterly → RA team. Further detail on who analyses trends, triggers investigations, and updates RMF is missing. |
| **Frequency & reporting cadence** | Periodicity of PMS reports (e.g., annual PSUR for Class IIb/III – Art 86) and trend‑reporting (Art 88). | Only “분기별” (quarterly) appears for data capture; no full report schedule defined. |
| **Trigger criteria for corrective actions** | Thresholds for serious incidents, trends, risk‑acceptability limits per ISO 14971:2019 §3‑8. | Not in source – must be added. |
| **Integration with PMCF** | How PMS findings feed the PMCF plan (Annex XIV Part B). | No linkage described. |
| **Documentation & storage** | Location, version control, retention period (minimum 10 years after device is placed on market – Art 83(2)). | Not covered. |

> **Action:** Expand the template to include the missing items above; ensure each element maps explicitly to MDR **Art 84** and MDCG 2025‑10 guidance.

---

## 4. PMCF Plan & Evaluation (Annex XIV Part B) – Expected Evidence  

| Item | Required content (MDR) | Current status |
|------|-----------------------|----------------|
| **PMCF objectives** | Clinical benefit/performance verification in real‑world use. | Not present. |
| **Study design / methodology** | Prospective registry, post‑market clinical study, literature review, or combination; statistical analysis plan. | Not present. |
| **Population & sample size** | Defined based on risk class and intended use (e.g., ≥ 100 patients for Class IIa, higher for IIb/III). | Not present. |
| **Data collection schedule** | Align with PMS data capture frequency; specify interim analyses. | Not present. |
| **Risk‑based endpoints** | Clinical safety endpoints linked to identified hazards in the RMF. | Not present. |
| **Reporting & updates** | Frequency of PMCF evaluation report (Annex XIV Part B) and integration into PSUR/annual summary (Art 86). | Not present. |

> **Action:** Draft a dedicated PMCF plan that fulfills Annex XIV Part B, referencing the PMS data sources identified above.

---

## 5. Clinical Evaluation Evidence (CER) – Required for All Classes  

*Reference:* MDR **Annex XIV Part A** – keep current under **Art 61**.  

| Needed evidence | Typical sources |
|-----------------|-----------------|
| State‑of‑the‑art literature review (systematic) | PubMed, Embase, clinical guidelines. |
| Clinical data from investigations & post‑market use | PMS/PMCF datasets, registries, literature case series. |
| Equivalence / predicate data (if applicable) | Only for devices falling under the “legacy” transitional provisions – not an MDR pathway; otherwise not used. |
| Benefit–risk analysis | Updated risk register (ISO 14971:2019). |

> **Current gap:** No CER is mentioned in the supplied template; it must be produced and kept up‑to‑date.

---

## 6. Risk Management Updates – Link to PMS/PMCF  

*Reference:* ISO 14971 (2019) & MDR **Annex I §3** (risk‑management system).  

| Required update when | Action |
|----------------------|--------|
| New hazard identified through trend reporting or incident analysis | Revise risk assessment, implement additional controls, and document in RMF. |
| Residual risk exceeds acceptability criteria | Conduct a PMCF study to obtain further evidence; if not mitigated, consider design change and notify NB (if Class IIa‑III). |
| Change of intended use or labeling | Re‑run classification & CE marking conformity assessment per Art 52/53. |

> **Trigger:** Any “risk‑acceptability breach” as defined in ISO 14971 §4 must be escalated to the RA lead and senior management within 5 working days.

---

## 7. Missing Information Checklist (to enable final MDR submission)

| Category | Specific items lacking |
|----------|------------------------|
| **Device definition** | Full name, model, technical description, intended use, user & patient populations, classification‑relevant attributes. |
| **Classification** | Rule number(s) from Annex VIII; resulting class (I, Is/Im/Ir, IIa, IIb, III). |
| **Conformity‑assessment route** | Confirmation of NB involvement, selected Annex (IX or X + XI) and associated modules. |
| **Full PMS Plan** | Objectives, risk‑threshold triggers, complete responsibility matrix, report schedule, document control, retention policy. |
| **PMCF plan** | Study protocol, sample size, endpoints, data analysis, integration with PMS. |
| **Clinical Evaluation Report** | State‑of‑the‑art literature review, clinical data sources, benefit–risk conclusions. |
| **Risk Management File (RMF)** | Updated hazard list, risk control measures, residual‑risk evaluation linked to PMS findings. |
| **EUDAMED entry** | Unique Device Identifier (UDI), registration of device and manufacturer, PMS & PMCF module completion. |

> **Immediate next step:** Populate the above items; where an item cannot be resolved without additional product information, flag it for the development team.

---

## 8. Human‑Escalation Triggers  

| Event | Who must be notified | Timeline |
|-------|----------------------|----------|
| **Serious incident** (Art 87) or FSCA required | RA lead → Management → Notified Body (if Class IIa‑III) | Within **2 working days** of awareness. |
| **Trend report indicating increasing frequency of a particular adverse event** (Art 88) | RA lead, Quality Manager, Design team | Within **5 working days**; initiate corrective action plan. |
| **Residual risk exceeding acceptability** (ISO 14971 §4) | Risk‑management owner, RA lead, Senior management | Immediately – start mitigation and possibly submit amendment to NB. |
| **Failure to meet PMS data‑collection frequency** (e.g., missing quarterly update) | QA Manager → RA lead | Within **10 calendar days** of missed deadline; corrective action required. |
| **PMCF study results showing safety concerns** | Clinical & RA leads, Senior management, Notified Body (if Class IIb/III) | As soon as data are analyzed – before next PSUR filing. |

---

## 9. Regulatory Judgment (pre‑submission)

1. **Classification cannot be finalized** without a complete device description and intended‑use statement.  
2. **PMS plan template** complies with the structure required by MDR **Art 84** and MDCG 2025‑10, but substantive content (objectives, trigger thresholds, reporting schedule, integration with PMCF) is still missing.  
3. **PMCF & CER** are not yet drafted; both must be produced to satisfy Annex XIV (Parts A & B) before the technical documentation can be deemed complete for NB review.  
4. **Risk management** must be continuously updated based on PMS findings, with explicit escalation pathways defined as above.

*Proceed to collect the missing product‑specific information, complete the full PMS/PMCF documentation, and then map the finished package against the appropriate conformity‑assessment route (Art 52).*

---

## 10. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made about required PMS elements (especially the quarterly data‑source list) and confirm that no additional MDR Art 84 sub‑clauses have been omitted from the checklist. Also verify whether any device‑specific MDR guidance (e.g., MDCG 2023‑XX for software or implantable devices) might impose extra PMS/PMCF obligations not captured here.  

---

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

> 심각 결함 없음. 52(7)/(6)/(4)/(3) 전표·PSUR annual IIb/III 정확. 미세: '≥100 patients for Class IIa' 표본크기 예시(내부 기준 예시로 hedge). [최종 2점 — shadow 11차 하향 수용: ① 'retention period (min 10 years) – Art 83(2)' — Art 83(2)는 QMS 내 PMS 체계 조항(보존기간 아님) ② 'Serious incident → 2 working days' — Art 87(3)은 즉시~15일, 2일은 공중보건 위협 한정(87(4)) ③ '≥100 patients for Class IIa' 규제 근거 없음.]

**Source Excerpts**

1. Chunk `1002815045680049480`

> ## 3. PMS Plan 실용 템플릿 (MDCG 2025-10 기반) `[추가확인]` 표시 항목은 자사 확인 후 기재. ---

2. Chunk `1151887824877296614`

> | 마케팅/QA팀 | | **S10** | 규제 데이터베이스 | EUDAMED, MAUDE (FDA), MFDS 이상사례 DB | 분기별 | RA팀 |

### kb-eval-20261126-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "880f2ae82c231231", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "229ed67db908335f1ee3f0eb51fd11a50f828f2ecba0f269c5461bb4f52f2547"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `880f2ae82c231231`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PSUR_%ED%85%9C%ED%94%8C%EB%A6%BF_MDR_Article86.md)
- Source hash: `229ed67db908335f1ee3f0eb51fd11a50f828f2ecba0f269c5461bb4f52f2547`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PSUR_템플릿_MDR_Article86.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Section 4. 심각한 부작용 및 안전 신호 (Art.86(1) 본문 — PMS 데이터 분석 · Art.88 trend) **4.1 보고 기간 내 Serious Incidents** | 이벤트 번호 | 발생일 | 제품 관련성 | 내용 요약 | 취해진 조치 | 보고 상태 | |---|---|---|---|---|---| | SI-[번호] | [날짜] | [확인/추정/관련없음] | [요약] | [FSCA/경고문 등] | [CA 보고 완료] | | (해당 없음) | — | — | 보고 기간 내 Serious Incident 없음 | — | — | **4.2 Trend Reporting (Art.88)** | 관찰된 트렌드 |...
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
*Prepared for the EU “MDR 2017/745” conformity assessment process*  

---

## 1. Device Overview (to be completed)

| Item | Information Needed |
|------|--------------------|
| **Device name / trade name** | – |
| **Intended purpose & indication(s)** | – |
| **Target patient population** | – |
| **Mode of action / principle of operation** | – |
| **Manufacturer & authorised representative** | – |
| **Regulatory status (existing CE‑mark, other jurisdictions)** | – |

> **Rationale:** The above data are prerequisite to determine the MDR classification (Annex VIII) and consequently the appropriate conformity‑assessment route (Art. 52). *Missing* → classification cannot be finalised at this stage.

---

## 2. Classification & Conformity‑Assessment Route (preliminary)

| Step | Decision Basis | Likely Outcome (subject to data completion) |
|------|----------------|---------------------------------------------|
| **Identify class** | Examine intended purpose, invasiveness, duration of use and whether the device has a measuring or therapeutic function. Apply Annex VIII rules (e.g., Rule 9, 10, 11, 17). | *Class IIa / IIb / III* – most PMS/PMCF‑intensive categories. |
| **Select route** | Art. 52(3‑6). For Class IIa–III the mandatory NB involvement is required (Annex IX or Annex X + XI). | *If Class IIa*: Annex IX (full technical‑documentation assessment) → NB review of PMS/PMCF data.<br>*If Class IIb / III*: either Annex IX **or** Annex X + XI (type‑examination + production verification). |

> **Citation:** MDR Art. 52; classification rules – Annex VIII.

---

## 3. Required Post‑Market Evidence (MDR)

| Requirement | Where it is stipulated | What must be produced |
|-------------|------------------------|-----------------------|
| **PMS system** | Art. 83 | Documented process for collection, analysis and reporting of post‑market data; links to the Risk Management File (RMF). |
| **PMS plan** | Art. 84 | Defined activities, data sources, frequency, responsibilities, and evaluation methods (incl. trend analysis per Art. 88). |
| **Periodic Safety Update Report (PSUR)** | Art. 86(1) – includes: <br>• *Benefit‑risk conclusions* (Art. 86(1)(a))<br>• *PMCF findings* (Art. 86(1)(b))<br>• *Sales & population data* (Art. 86(1)(c)) | PSUR prepared at least every **year** for Class IIb/III and **every two years or as needed** for Class IIa (MDCG 2022‑21 Annex IV). |
| **Trend reporting** | Art. 88 | Aggregated data on incidence, prevalence, severity of adverse events; plotted against pre‑defined thresholds. |
| **Serious incident handling & FSCA** | Art. 87 | Immediate notification to the NB and competent authorities; corrective actions (FSCA) documented. |
| **PMCF plan & PMCF evaluation report** | Annex XIV Part B | Prospective clinical data collection strategy, justification of continued safety/ performance, alignment with state‑of‑the‑art literature (Annex I §16‑§18). |

> **Citation:** MDR Art. 83‑88; Annex XIV Part A/B.

---

## 4. Gaps Identified in the Source Material

| Gap | Impact on Submission |
|-----|----------------------|
| **No device description / intended use** – classification cannot be finalised (Section 1). | Prevents selection of correct conformity‑assessment route and identification of applicable GSPR (Annex I). |
| **Absence of PMS plan details** – data sources, frequency, responsible parties. | Non‑compliance with Art. 84; NB will request a complete PMS plan before approval. |
| **No description of PMCF activities** – study design, endpoints, population, timeline. | Fails Annex XIV Part B requirement; PSUR benefit‑risk conclusions lack supporting clinical evidence (Art. 86(1)(a)). |
| **Risk Management File (RMF) not referenced** – linkage between residual risks and trend actions missing. | Incomplete evidence for updating risk controls per Annex I §3 & §8. |
| **No quantitative thresholds for trend reporting** – the template only shows placeholders. | Art. 88 requires predefined trigger values; otherwise NB cannot assess “critical‑value exceeded” statements. |
| **Missing process for Serious Incident (SI) escalation** – only a table placeholder is provided. | Art. 87 demands timely notification and corrective action records; omission will be noted by the NB. |

---

## 5. Recommended Risk Controls (to be integrated in RMF)

1. **Update risk control measures** when trend analysis shows an increase in incidence above the pre‑set threshold (Art. 88).  
2. **Implement field safety corrective actions (FSCA)** for any serious incident classified as *related* (Art. 87).  
3. **Re‑evaluate residual risk** after each PSUR; if benefit‑risk balance turns “unfavourable” the device must be withdrawn or re‑classified (Art. 86(1)(a)).  
4. **Usability mitigation** per IEC 62366‑1 to address use‑error trends identified in post‑market data (Annex I §5).  

All controls shall be documented and cross‑referenced with the corresponding GSPR clauses (e.g., Annex I §§3–9, 16.4 for radiation devices).

---

## 6. Human‑Escalation Triggers

| Trigger | Required Action | Regulatory Reference |
|---------|-----------------|-----------------------|
| **Serious Incident (SI) reported** – any event deemed *related* to the device. | Immediate notification to NB & competent authority; initiate FSCA. | Art. 87. |
| **Trend analysis exceeds pre‑defined threshold** (e.g., actual incidence > expected rate). | Escalate to senior clinical safety officer; update PMS plan, consider design change or label amendment. | Art. 88. |
| **New residual risk identified** that changes the benefit‑risk balance to “unfavourable”. | Prepare supplemental PSUR; consider restriction of use, updated IFU, or market withdrawal. | Art. 86(1)(a). |
| **PMCF results reveal unmet clinical performance criteria**. | Trigger a corrective action plan, possible additional clinical investigation (Art. 61 & Annex XIV Part B). |
| **Regulatory authority request for additional data** (e.g., unexpected signal from EUDAMED). | Compile and submit requested evidence within the statutory timeframe; involve senior management. | Art. 84‑86 implementation obligations. |

All escalations must be logged in the PMS database (Art. 83) and reported to the NB as part of the next PSUR.

---

## 7. Action Summary for the Project Team

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Complete **device description & intended use**; provide classification justification (Annex VIII). | Product Management | +2 weeks |
| 2 | Draft a full **PMS plan** (Art. 84) – data sources, frequency, responsibilities. | Regulatory Affairs Lead | +3 weeks |
| 3 | Develop detailed **PMCF plan** (Annex XIV Part B) – study design, endpoints, timelines. | Clinical Affairs | +4 weeks |
| 4 | Populate the PSUR template with actual data: SI log, trend tables, benefit‑risk analysis (Art. 86). | Surveillance Team | Before next reporting period |
| 5 | Align **Risk Management File** updates (Annex I §3) with PMS findings and trend actions. | Quality/Risk Manager | Ongoing |
| 6 | Establish **escalation procedures** for SI, trends, and new risks; train staff on trigger thresholds. | Compliance Officer | +2 weeks |

---

## 8. Peer‑Review Prompt

> *Colleague, please review the assumptions made above, especially: (a) the provisional classification pathway in Section 2 given that no device‑specific information is supplied; (b) completeness of the listed PMS/PMCF evidence against MDR Art. 83‑88 and Annex XIV; (c) any jurisdiction‑specific gaps (e.g., EUDAMED registration obligations under Art. 33‑39) that have not been addressed. Highlight missing elements or alternative interpretations you consider relevant.*

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
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. PSUR 'IIb/III 연간·IIa 2년 (MDCG 2022-21 Annex IV)' — 정정된 사실표·원문 값 정확 인용. 52(3-6) 경로·Art 86(1)(a)(b)(c) 분해 정확. 미세: 'Annex I §16-§18' state-of-art 귀속 느슨.

**Source Excerpts**

1. Chunk `1068941934152517684`

> ### Section 4. 심각한 부작용 및 안전 신호 (Art.86(1) 본문 — PMS 데이터 분석 · Art.88 trend) **4.1 보고 기간 내 Serious Incidents** | 이벤트 번호 | 발생일 | 제품 관련성 | 내용 요약 | 취해진 조치 | 보고 상태 | |---|---|---|---|---|---| | SI-[번호] | [날짜] | [확인/추정/관련없음] | [요약] | [FSCA/경고문 등] | [CA 보고 완료] | | (해당 없음) | — | — | 보고 기간 내 Serious Incident 없음 | — | — | **4.2 Trend Reporting (Art.88)** | 관찰된 트렌드 | 예상 발생률 | 실제 발생률 | 조치 | |---|---|---|---| | [항목] | [기준치] | [실제치] | [FSCA/경고문/설계변경 등] | | (해당 없음) | — | — | 임계값 초과 없음 | — | ---

2. Chunk `1141979248009057881`

> ### Section 6. Benefit-Risk Balance 결론 (Art.86(1)(a)) > 이전 PSUR / CER 대비 benefit-risk balance 변화 여부 평가. | 평가 항목 | 이전 PSUR | 이번 PSUR | 변화 여부 | |---|---|---|---| | 주요 편익 (Clinical benefits) | [요약] | [요약] | [변화 없음/변화 있음] | | 잔존 위험 (Residual risks) | [요약] | [요약] | [변화 없음/변화 있음] | | Overall benefit-risk 결론 | 유리함 | [유리함/불확실/불리함] | [변화 없음/변화 있음] | **Benefit-risk 결론:** > [이번 보고 기간의 데이터를 종합할 때, 해당 기기의 benefit-risk balance는 여전히 유리하며/변화가 없으며, 기존 적응증에서의 사용은 적절한 것으로 판단됩니다. / 또는: 새로운 위험 신호가 확인되어 다음의 조치를 취합니다: ...] ---

## ra_kr

### kb-eval-20261126-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "8abc882474c2d165", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `8abc882474c2d165`
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

> **Regulatory Draft – Independent SaMD GUI (Digital‑Medical‑Products‑Act Impact)**  

---

### 1. Classification & Submission Route  
| Korean grade | Typical pathway | Comment |
|--------------|----------------|---------|
| **4등급** (high‑risk) – most SaMD that provide diagnostic or therapeutic recommendations are placed in this grade under the “의료기기 품목 및 품목별 등급에 관한 규정”. | **허가** (MFDS approval) | The exact grade must be confirmed against the official 규정 table; if the device is judged 3등급, the route would switch to 허가 as well.  

> *No specific “MFDS 고시 제‑​” number naming the classification rule appears in the source excerpts – verify separately.*

---

### 2. Core Evidentiary Requirements  

| Requirement | Korean regulatory basis (framework) | Typical content |
|-------------|--------------------------------------|-----------------|
| **KGMP 인증** (Manufacturing) | KGMP (의료기기법 제28조) | Facility certification, GMP audit reports, batch records. |
| **QMS + ARR compliance** | ISO 13485:2016 + MFDS “Applicable Regulatory Requirements” (ARR) – UDI, MDR‑type reporting, Corrections & Removals. | QMS manual integrating ARR activities; procedures for complaint handling, service records, internal audits per FDA §820.* (mapped to Korean practice). |
| **Software Life‑Cycle Documentation** | IEC 62304:2006+A1:2015 (Safety Class C) | SDP, SRS, SAD, SVP, SVR – complete set required. |
| **Software Validation & Verification** | KGMP + 디지털의료제품법 (software validation) | Automated regression test suite; change‑control SOPs; documented verification of each safety class requirement. |
| **Cybersecurity** | MFDS 사이버보안 가이드라인 2025 | Threat model, SBOM, PCCP (Pre‑Market Cybersecurity Plan); alignment with FDA 524B PCCP and MDCG 2019‑16 Rev.1. |
| **AI/ML Component Dossiers** *(if applicable)* | 디지털의료제품법 + FDA PCCP (2024‑12‑03) + EU AI Act Art.43(4) (reference) | Documentation of model design, training data provenance, performance monitoring, change‑management plan; note that Korean law currently expects a pre‑market risk assessment rather than a separate re‑certification. |
| **Clinical Evaluation** | 디지털의료제품법 + MFDS 임상평가 가이드라인 (if required) | Local clinical data or justification for reliance on foreign CER (requires mapping to MFDS acceptance scope). |
| **Labeling & IFU** | MFDS 라벨링·사용설명서 규정 (Korean language mandatory) | Device name, intended use, contraindications, UDI, safety information in Korean. |
| **Post‑Market Surveillance (PMS)** | MFDS 시판후조사 규정 | Complaint handling, periodic safety update, field corrective action plan. |

> *No specific “MFDS 고시 제 …​호” identifier is cited in the source material for any of the above items – verify separately.*

---

### 3. Missing / Unconfirmed Information  

| Gap | Why it matters | Action needed |
|-----|----------------|---------------|
| **Exact grade (1–4등급) determination** | Determines submission track and depth of clinical data required. | Review the device’s intended use against 「의료기기 품목 및 품목별 등급에 관한 규정」; obtain official classification decision. |
| **KGMP facility certification status** | Mandatory for any 허가‑type product. | Obtain KGMP certificate or plan for audit. |
| **Local clinical evidence requirement** | MFDS may require Korean patient data even when foreign CER exists. | Clarify whether the device can rely on FDA 510(k) / CE marking under current MFDS scope (see recent 고시 expanding foreign CER acceptance). |
| **Korean‑language labeling draft** | Non‑compliance leads to review delays or rejection. | Prepare provisional Korean label/IFU; submit for pre‑review if possible. |
| **Detailed cybersecurity plan** | Cyber risk is a stand‑alone evaluation under the 2025 guideline. | Develop Threat Model, SBOM, PCCP; map to MFDS checklist items. |
| **AI/ML change‑management SOP** (if AI present) | Required for ongoing conformity and re‑assessment. | Draft AI lifecycle management documentation. |
| **Foreign evidence mapping (e.g., FDA 510(k), CE Technical File)** | Determines if foreign data can be used to satisfy MFDS ARR or clinical evaluation. | Identify applicable MFDS 고시 that permits such reliance; collect supporting documents. |

---

### 4. Risk Controls (mapped to Korean & International standards)  

| Control | Reference (framework) | Implementation note |
|---------|-----------------------|----------------------|
| **Hazard analysis & risk management** | IEC 60601‑1, ISO 14971:2019 (Korean adoption) | Perform FMEA/FMECA early; update throughout lifecycle. |
| **Software safety class controls** | IEC 62304 Class C | Enforce strict verification of all safety‑related functions; redundant coding where needed. |
| **Change control & regression testing** | KGMP SOP + QMSR ARR §820.10(b) integration | Automated test suite executed for every code change; documented release justification. |
| **Cybersecurity safeguards** | MFDS 사이버보안 가이드라인 2025, FDA 524B PCCP | Implement secure boot, encryption, vulnerability scanning, incident response plan. |
| **AI/ML model monitoring** | FDA PCCP (2024‑12‑03) + EU AI Act Art.43(4) | Continuous performance tracking; predefined drift thresholds trigger re‑validation. |
| **Post‑market surveillance & complaint handling** | MFDS 시판후조사 규정, ARR §820.35(a) | Real‑time logging of adverse events; 30‑day reporting to MFDS for MDR‑type incidents. |
| **User training & usability testing** | IEC 62366‑1 (Usability) | Conduct formative and summative usability studies in Korean language; update IFU accordingly. |

---

### 5. Citations  

| Type | Citation |
|------|----------|
| Framework – Standards | ISO 13485:2016, IEC 62304 2006+A1:2015 (Safety Class C), ISO 14971:2019, IEC 60601‑1 2005+A1:2012+A2:2020, IEC 62366‑1 2015+A1:2020 |
| Framework – Korean law | 디지털의료제품법 (2025 시행), KGMP (의료기기법 제28조) |
| MFDS guidance (no identifier in source) | MFDS 사이버보안 가이드라인 2025 |
| Foreign references (for mapping only) | FDA 524B PCCP, MDCG 2019‑16 Rev.1, EU AI Act Reg. 2024/1689 Art.43(4) |

> No instance identifiers (e.g., MFDS 고시 번호, 510(k) number) appear in the provided excerpts; where a specific identifier would be required, the draft notes “verify separately.”

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation |
|--------|-----------------------|
| **Grade not confirmed** | Determines whether 허가 is needed; inability to proceed without official classification. |
| **KGMP certification absent or pending** | Mandatory for any 허가 submission – pause dossier assembly until certificate secured. |
| **Local clinical data gap identified** | MFDS may reject reliance on foreign CER; need senior clinical reviewer input. |
| **Cybersecurity plan incomplete or fails MFDS checklist** | High‑risk cyber exposure could block approval; requires specialist review. |
| **AI/ML component without documented change‑management SOP** | Non‑compliance with both Korean and FDA expectations – require AI/ML expert involvement. |
| **Korean labeling draft not yet prepared** | Mandatory language requirement – must involve translation/legal compliance team. |
| **Significant audit finding from internal audit (ARR‑related)** | Internal audit reports become visible to MFDS inspectors; requires corrective action plan before filing. |

When any of the above triggers are hit, the project lead should be notified immediately and a formal risk‑based decision record created before proceeding.

---

### 7. Peer Review Prompt  

> **To another RA colleague:** Please review the assumptions underlying the grade (4등급) determination, the completeness of the foreign‑evidence mapping for ARR compliance, and any jurisdiction‑specific gaps—especially regarding the need for Korean clinical data versus reliance on FDA 510(k)/CE documentation. Highlight any missing citations or areas where additional MFDS 고시 numbers should be obtained.

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

> 'most SaMD → 4등급' 무근거 단정 — 소스(KGMP 비교표)에 등급 없음 + KB 정합 위반(촬영실 GUI SW=2등급). 확인 헷지는 있으나 등급 서술 자체가 KB와 충돌.

**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261126-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "03dcef60923f9277", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "00026234f8ec1153306309dc7c82b355b5fdfc4d7a5de00dbd5247374b13eccb"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `03dcef60923f9277`
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

> **Regulatory Draft – Impact of the Digital Medical Products Act on the X‑ray System (SBOM / AI / Network‑Enabled Firmware)**  

---

## 1. 적용 규정 개요
| 구분 | 주요 근거(프레임워크) | 한국 MFDS 고시·법령(인스턴스) |
|------|---------------------|--------------------------------|
| 의료기기법 전체 | “의료기기법” 및 “의료기기 품목별 등급에 관한 규정” | **no specific identifier found in source – verify separately** |
| 디지털의료제품법 (2025‑01‑24 시행) | 디지털의료제품법 전부 | **no specific identifier found in source – verify separately** |
| SBOM 요구사항 | FDA 524B, EU MDR MDCG 2019‑16 (참조용) | MFDS (2025‑01‑10) – 권고 (SPDX 2.3 / CycloneDX 1.5) – **no specific identifier found** |
| 품질·제조관리 | KGMP (의료기기법 제28조) | — |
| 위험 관리 | ISO 14971:2019 | — |
| QMS | ISO 13485:2016 | — |
| 소프트웨어 생명주기 | IEC 62304:2006+A1:2015 | — |
| 사이버 보안·SBOM 관리 | MFDS 고시 제16조 SBOM 관리 | **no specific identifier found** |

> *프레임워크 레퍼런스(ISO/IEC 등)는 번호만 기재하고 별도 검증 메모를 붙이지 않습니다.*  

---

## 2. 장치 구성 및 디지털 의료제품법 적용성 (Source [2])

| 구성 요소 | 디지털의료기기 해당 여부 | 비고 |
|-----------|------------------------|------|
| Generator 펌웨어 | X (비연결, 하드웨어 제어 전용) | 디지털‑의료제품법 적용 대상 외 |
| Detector 펌웨어 | △ (네트워크 연결 시 가능) | 네트워크 기능 구현 여부에 따라 디지털‑의료제품법 적용 검토 필요 |
| Acquisition Workstation SW | ○ | 단독 조작·네트워크 연결·AI 활용 → **SaMD + AI** 성격, 디지털‑의료제품법 적용 대상 |
| 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류, 별도 임상평가 필요 |
| DICOM 전송·PACS 연계 | △ (통신 기능) | 독립형 소프트웨어 경계 검토 ‑ 네트워크 보안·보호조치 확인 필수 |

**핵심 판단** – Acquisition Workstation SW와 AI 분석 모듈은 “디지털의료제품법” 적용 대상이며, 특히 AI‑기능을 포함한 경우 **SaMD**(Software as a Medical Device) 로 분류되어 별도 위험관리·임상평가 요구가 있습니다.

---

## 3. 등급 및 인허가 경로 (한국 의료기기법)

| 장치 전체 | 예상 품목 등급* | 인허가/인증/신고 경로 |
|-----------|----------------|-----------------------|
| X‑ray 영상 시스템(하드웨어 + 소프트웨어) | 3등급 또는 4등급 (방사선·이미징 고위험) | **허가** (MFDS 직접 심사) |

\* *정확한 등급은 「의료기기 품목 및 품목별 등급에 관한 규정」에 따라 개별 품목(예: X‑ray Generator, Detector, Software)을 별도 조회 후 종합 판단 필요.*  

---

## 4. 제출 시 요구되는 근거·증거

| 구분 | 요구 서류/증거 | 비고 |
|------|----------------|------|
| **SBOM** | - SPDX 2.3 또는 CycloneDX 1.5 포맷 <br>- NTIA 7요소(구성 요소, 버전, 라이선스 등) + EOL·취약점 정보 <br>- MFDS 권고 RA‑07 항목에 따른 제출 서식 | MFDS (2025‑01‑10) 권고 – **no specific identifier found** |
| **위험관리** | ISO 14971:2019 기반 위험 관리 파일 (RMP)·위험 통제 계획 <br>• 사이버 보안 위험 포함(MFDS 고시 제16조 SBOM 관리) | — |
| **임상 평가** | - SaMD AI 모듈에 대한 임상 성능 및 안전성 데이터 <br>- 필요한 경우 외국 CER (FDA 510(k)/EU MDR) 수용 여부 검토 (OECD MAD 비임상 데이터와 구분) | 해외 임상 자료 수용 범위는 MFDS 최신 고시 확인 필요 |
| **품질·제조** | KGMP 인증서(제28조) <br>- ISO 13485:2016 기반 QMS 문서 | — |
| **소프트웨어 생명주기** | IEC 62304 준수 증빙 (개발 계획, 검증·확인 보고서) | — |
| **라벨·사용설명서** | 한글 라벨·IFU(사용자 안내문) 및 위험 정보 표기 | — |
| **시판후 관리** | PMS Plan (MFDS 고시 제16조 포함) <br>- 정기적인 SBOM 업데이트 절차 | — |

---

## 5. 현재 누락·추가 필요 사항

1. **정확한 등급 확인** – 개별 구성품(Generator, Detector, Software)의 등급을 공식 규정표에서 조회 필요.
2. **SaMD AI 임상자료** – AI 알고리즘의 성능 및 안전성에 대한 국내 임상시험 혹은 MFDS가 인정하는 외국 CER 존재 여부 확인.
3. **네트워크 보안 계획** – Detector 펌웨어·Workstation 등 네트워크 연결 시 적용될 사이버 보안 대책(침해 대응, 취약점 관리) 상세 문서 필요.
4. **SBOM 제출 서식** – MFDS가 권고하는 “RA‑07 항목” 구체 내용(예: 컴포넌트 식별 체계, 버전 관리 정책 등) 확인 및 적용.
5. **KGMP 인증 현황** – 제조 시설이 KGMP 인증을 이미 획득했는지, 필요 시 신규 인증 절차 계획 수립.

---

## 6. 핵심 위험 통제(예시)

| 위험 영역 | 주요 통제 방안 |
|-----------|----------------|
| 방사선 안전·출력 관리 | IEC 60601‑1‑2 기반 전자기 간섭·방사선 보호 설계, 하드웨어 레벨 차단 기능 |
| 소프트웨어 오류·버그 | IEC 62304에 따른 단계별 검증·확인, 자동 업데이트와 롤백 메커니즘 구현 |
| 사이버 위협 | MFDS 고시 제16조 SBOM 관리 기반 취약점 추적·패치 적용 절차, 네트워크 방화벽·VPN 적용 |
| AI 편향·성능 저하 | 임상 데이터 다양성 확보, 지속적인 알고리즘 모니터링·재학습 프로세스 정의 |
| 사용자 오인(라벨) | 한글 라벨·IFU에 위험도 및 경고문 명시, 사용자 교육 계획 포함 |

---

## 7. 인간(RA 전문가) 개입 필요 트리거

| 상황 | 구체적 행동 |
|------|-------------|
| **등급이 3등급/4등급인지 불확실** | 등급표 확인 → MFDS 담당관에게 사전 질의 (품목·구성 별 등급 재확인) |
| **AI SaMD 임상자료 부족** | 국내 임상시험 계획 수립 또는 외국 CER 수용 가능 여부 검증을 위해 MFDA(의료기기안전정보원)와 협의 |
| **SBOM 포맷·항목 미충족** | SBOM 자동 생성 툴 검토·개선, 필요 시 공급망(OSS 공급자)와 데이터 공유 합의 체결 |
| **KGMP 인증 누락** | 제조 공장 KGMP 인증 진행 상황 점검 – 필요 시 인증 기관(KTL·KTC 등)에 신청 일정 조율 |
| **보안 정책 미비** | 사이버 보안 담당과 협업하여 MFDS 고시 제16조에 명시된 SBOM 관리·취약점 대응 절차 수립 |
| **외국 임상 데이터 상호인정(OECD MAD) 검토 필요** | 최신 MFDS 고시(예: 2025‑01‑10 이후 개정)에서 비임상 GLP 데이터 수용 범위 확인 후, 해당 증거를 포함할지 여부 결정 |

---

## 8. 결론 (Regulatory Judgment)

- **분류·인허가** : 본 X‑ray 시스템은 3등급 또는 4등급에 속할 가능성이 높으며 **허가** 절차( MFDS 직접 심사 )를 진행해야 합니다.  
- **핵심 제출물** : SBOM (SPDX 2.3 or CycloneDX 1.5) + 위험관리 파일(ISO 14971), KGMP 인증, IEC 62304 기반 소프트웨어 개발 증빙, AI SaMD 임상평가 자료, 한국어 라벨·IFU, PMS Plan(고시 제16조).  
- **현재 결핍** : 정확한 등급 판정, SaMD AI 임상자료, 상세 보안·SBOM 관리 서식, KGMP 인증 현황. 위 항목이 확보될 때까지 **인허가 진행을 중단**하고 해당 정보를 완비해야 합니다.

---

## 9. Peer‑Review 요청

> 다른 RA 동료에게 아래 질문에 답변을 부탁드립니다.  
> 1️⃣ 등급 판단(3등급 vs 4등급) 시 고려해야 할 구체적인 방사선·이미징 기준은 무엇인가?  
> 2️⃣ AI SaMD 임상평가에서 MFDS가 최근 인정한 외국 CER 사례와 적용 조건을 알려 주세요.  
> 3️⃣ 현재 SBOM RA‑07 항목에 포함돼야 하는 ‘EOL / 취약점’ 정보의 구체적 포맷 요구사항이 존재하는지 확인 바랍니다.  
> 4️⃣ KGMP 인증 절차에서 디지털 의료제품법 적용 시 별도 요구되는 추가 문서가 있는지 검토해 주세요.

--- 

*위 초안은 소스에 나타난 식별자(예: MFDS 고시 번호, 조문) 를 직접 인용하지 않았으며, 구체적인 번호가 필요할 경우 추후 공식 고시를 확인 후 보완하시기 바랍니다.*

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

> 'X-ray 영상 시스템 → 3등급 또는 4등급 (방사선 고위험) → 허가' — 소스(SBOM 정합성·해당성 판정)에 등급 없음 + KB 정합 위반(X-ray 발생장치 2~3등급, GUI SW 2등급 — 4등급 부분은 무근거 상향). '예상*' 헷지·MFDS 사전질의 escalation는 있음.

**Source Excerpts**

1. Chunk `1055466385786976527`

> ## 1. FDA vs MDR vs MFDS — SBOM 요구사항 정합성 | 축 | 요구 시점 | 포맷 | 필수 항목 | 제출 방식 | 사후 갱신 | |----|-----------|------|-----------|-----------|-----------| | FDA (524B) | Premarket (2023-10-01 RTA 강제) | SPDX 2.3 / CycloneDX 1.5 | NTIA 7요소 + EOL + 취약점 | eSTAR 제출물 | Section 524B Postmarket Plan | | MDR (MDCG 2019-16) | Technical Documentation Annex II | 포맷 권고 없음, IMDRF N73 원칙 | NTIA 7요소 + License + Hash | NB 심사 자료 | PMS Plan/PSUR 포함 | | MFDS (2025-01-10) | 국내 허가 심사 | 권고 (SPDX/CycloneDX) | RA-07 항목 | 심사 자료 (권고) | 보안 지침 제16조 SBOM 관리 | **정합성 판정: 본 SOP-SBOM-001 v0.1은 3축 모두 수용 가능한 상위 호환 설계** - SPDX 2.3 또는 CycloneDX 1.5 채택 → FDA/MDR/MFDS 동시 만족 - NTIA Baseli...

2. Chunk `418096885713027360`

> ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 |

### kb-eval-20261126-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "cb09e5a9fd730e39", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `cb09e5a9fd730e39`
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

> **Regulatory Draft – Impact of the Digital‑Medical‑Products Act on an AI‑Based SaMD (Imaging‑Analysis Module)**  

---

## 1. Device Overview & Intended Use  
| Item | Description |
|------|-------------|
| **Product type** | Software‑only medical device (SaMD) that performs AI‑driven analysis of radiologic images (e.g., detection of lung nodules). |
| **Intended use** | “Provides a diagnostic support recommendation to assist clinicians in the interpretation of chest CT scans.” |
| **Technology** | Generative/criminative AI model trained on anonymised imaging datasets; runs on hospital‑network‑connected workstations or cloud‑based console. |
| **Regulatory source** | Digital Medical Products Act (디지털의료제품법) – 2025 implementation phase. *(no specific notice number appears in the source material – verify separately)* |

---

## 2. Korean Classification & Submission Route  

| Step | Determination |
|------|----------------|
| **Grade** | The device is a “diagnostic imaging support” SaMD that influences clinical decision‑making. Under 「의료기기 품목 및 품목별 등급에 관한 규정」 the corresponding grade is **3등급** (high‑risk). *No explicit grade stated in source – must be confirmed from the regulation.* |
| **Submission track** | 3등급 → **허가** (full MFDS approval). |

*If later verification shows the device falls under a lower functional category (e.g., “general health‑care software” without clinical impact), the grade may shift to 2등급 and the route would become **인증**. This re‑classification must be confirmed before filing.*

---

## 3. Required Evidentiary Package  

| Evidence Category | Korean Requirement | Notes / Source |
|-------------------|--------------------|----------------|
| **Technical documentation** (QMS) | KGMP facility certification (법 제28조) for any manufacturing site; QMS compliant with ISO 14971:2019 risk management and IEC 62366‑1:2015+A1:2020 usability engineering. | Framework references are standard – no specific identifier needed. |
| **Clinical evaluation** | Clinical performance data generated in Korea *or* a foreign clinical evaluation report (CER) accepted under the latest MFDS notice expanding foreign CER acceptance. | No specific notice number is supplied in the source – “no specific identifier found in source — verify separately.” |
| **Non‑clinical safety** | GLP‑compliant biocompatibility/ toxicology per ISO 10993‑1:2018, accepted via OECD MAD for non‑clinical data only. | OECD MAD covers only non‑clinical GLP data; separate acceptance of foreign CER is a distinct pathway. |
| **Cybersecurity** | Conformity with the *디지털의료기기 사이버보안 허가·심사 가이드라인* (2025‑01‑10) – high relevance per source table. Must provide RA‑01~RA‑20 matrix, SBOM, and vulnerability management plan. |
| **Usability / Human Factors** | IEC 62366‑1 usability engineering plan (refer to “사용적합성 엔지니어링 계획 수립” in source). |
| **AI‑specific governance** | SOPs for AI dataset & model governance (SOP‑AIDATA‑001, SOP‑AIGOV‑001) as listed under “AI 모델 데이터셋·거버넌스 절차 수립.” |
| **Labeling & IFU** | Korean language labeling, instructions for use, and risk information per MFDS labeling requirements. |
| **Post‑Market Surveillance (PMS)** | PMS plan aligned with MFDS 시판후조사 규정; includes adverse event reporting and periodic safety update (if required). |

---

## 4. Gaps / Missing Information  

1. **Exact grade confirmation** – need to cite the specific clause of 「의료기기 품목·등급 규정」 that maps AI imaging analysis to 3등급.  
2. **Foreign clinical evidence acceptance notice** – the exact MFDS 고시/notification number that permits use of a foreign CER for AI‑based SaMD is not provided in the source. Must retrieve and verify.  
3. **Device‑specific risk classification justification** – a detailed risk analysis (ISO 14971) linking each hazard to mitigation measures is still pending.  
4. **Cybersecurity threat model** – while a matrix (RA‑01~RA‑20) is in progress, the final documented threat model and penetration‑testing report are not yet completed.  
5. **SBOM completeness** – SOP‑SBOM‑001 exists, but verification that the current software bill of materials fully enumerates all third‑party libraries (including open‑source AI frameworks) is required.  

---

## 5. Risk Controls & Mitigations (Mapped to Required Standards)

| Hazard / Risk | Control (Korean Requirement) | Standard Reference |
|---------------|------------------------------|--------------------|
| Incorrect diagnostic recommendation → patient harm | Automated performance monitoring, clinical decision support limitation statements in IFU; periodic recalibration of AI model. | ISO 14971:2019, IEC 62366‑1 |
| Data breach / unauthorized access (networked SaMD) | Implementation of MFDS cyber‑security guideline controls (2025‑01‑10), SBOM tracking, vulnerability patch management, encryption of PHI. | 디지털의료기기 사이버보안 허가·심사 가이드라인 (2025‑01‑10) |
| Model drift / degraded performance over time | AI governance SOPs: dataset version control, retraining schedule, post‑market performance surveillance. | SOP‑AIDATA‑001, SOP‑AIGOV‑001 |
| User error due to poor UI/UX | Usability engineering plan (IEC 62366‑1) and validation testing with representative clinicians. | IEC 62366‑1:2015+A1:2020 |
| Non‑compliance with Korean labeling | Korean language label/IFU approved by MFDS; includes safety warnings, intended use, contraindications. | MFDS 라벨링·사용설명서 규정 (no specific identifier in source) |

---

## 6. Human‑Escalation Triggers  

| Situation | Trigger for Human Review / Escalation |
|-----------|--------------------------------------|
| **Uncertain grade** – if the risk classification cannot be conclusively mapped to a grade from the regulation. | Pause filing; request senior RA or legal counsel to confirm grade before proceeding. |
| **Foreign CER acceptance** – lack of confirmed MFDS notice number permitting use of foreign clinical data. | Escalate to regulatory manager to obtain latest MFDS 고시/notification (e.g., via MFDS website) and assess applicability. |
| **Cybersecurity gaps** – incomplete RA‑01~RA‑20 matrix, missing threat model, or SBOM incompleteness. | Immediate security team involvement; postpone submission until remediation. |
| **Labeling non‑Korean content** – any IFU or label element not fully translated into Korean. | Halt submission; engage translation/legal to produce compliant Korean documentation. |
| **Post‑Market Surveillance plan insufficient** – missing adverse event reporting flow for AI updates. | Trigger PMS lead review and supplemental plan development before filing. |

---

## 7. Citations  

| Type | Citation Detail |
|------|-----------------|
| **Framework references** (no verification needed) | ISO 14971:2019; IEC 62366‑1:2015+A1:2020; ISO 10993‑1:2018; KGMP (법 제28조). |
| **Instance identifiers from source** | *디지털의료기기 사이버보안 허가·심사 가이드라인* – published 2025‑01‑10 (high relevance). <br> *독립형 디지털의료기기SW 사용적합성 가이드라인* – published 2025‑01 (high relevance). <br> *생성형 AI 의료기기 허가·심사 가이드라인* – published 2025‑01 (medium relevance). |
| **No specific identifier found** | The source does not provide a MFDS 고시/notification number for foreign clinical evaluation report acceptance; the exact grade clause in 「의료기기 품목 및 품목별 등급에 관한 규정」 is also absent – *verify separately*. |

---

## 8. Peer‑Review Prompt  

> **To fellow RA colleagues:**  
> Please challenge the assumptions made above regarding (1) the provisional classification of the AI imaging‑analysis SaMD as 3등급, (2) the completeness of the cybersecurity evidence package in light of the 2025‑01‑10 guideline, and (3) any potential gaps where a foreign clinical evaluation report might be permissible under MFDS’s latest notice. Highlight any additional Korean regulatory documents or recent 고시 numbers that we may have missed, and suggest what supplemental data would be needed to close the identified gaps.

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
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 'diagnostic imaging support SaMD → 3등급(고위험)' 단정 — 소스(사이버 가이드라인)에 등급 언급 0건 + KB 정합 위반(동 제품군 2등급). RA-01~RA-20은 소스 기반(무죄 — KB 내부 20↔35 불일치 관찰).

**Source Excerpts**

1. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

2. Chunk `1130453648414545903`

> ## 8. 후속 조치 요건 (프로젝트 관점) | 우선순위 | 조치 사항 | 연계 문서 | 상태 | |----------|----------|-----------|------| | 1 | 사이버보안 RA-01~RA-20 대응 매트릭스 작성 | 디지털의료제품법_요구사항_매트릭스 | 진행중 | | 2 | 사용적합성 엔지니어링 계획 수립 | IEC_62366-1_사용적합성_엔지니어링_계획서 | v0.2 완료 | | 3 | SBOM 관리 절차 정합성 확인 | SOP-SBOM-001 | v0.2 완료 | | 4 | 변경관리 계획 SOP 연계 (CMP 섹션) | SOP-CC-001 | v0.2 완료 | | 5 | AI 모델 데이터셋·거버넌스 절차 수립 | SOP-AIDATA-001, SOP-AIGOV-001 | v0.2 완료 | | 6 | 구성요소 단위 성능평가 절차 문서화 | AI_구성요소_단위_성능평가 | v0.2 완료 |

### kb-eval-20261126-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "2de2253fc4aad307", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md", "source_hash": "eb51488884ab30cb61201ada333e2b2ea38242de599693d5089204a4859f4240"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2de2253fc4aad307`
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

> **Regulatory Draft – Digital Medical Products Act (디지털의료제품법) Impact Assessment**

---

### 1. Device Overview  
* **Product type:** Software‑based medical device (SaMD) that falls under the newly‑enacted “Digital Medical Products Act”.  
* **Intended use / indication:** *(to be supplied by the development team – required for classification)*  

---

### 2. Korean Classification & Submission Route  

| Item | Current Status | Required Confirmation |
|------|----------------|-----------------------|
| Device grade (1~4등급) | **Not identified in source** | Must be determined from 「의료기기 품목 및 품목별 등급에 관한 규정」. The grade will dictate the submission track: 1등급 → 신고, 2등급 → 인증, 3·4등급 → 허가. |
| Applicable legal basis | **디지털의료제품법** (2025‑01‑24 시행) in conjunction with **의료기기법** | Both statutes apply; the Act does not replace the existing grade system. |

> **Action:** Obtain the official product‑grade decision from the MFDS or a qualified Korean classification consultant before preparing the dossier.

---

### 3. Applicable Framework References (no “verify” caveat required)

| Area | Korean regulation / guideline | International standard |
|------|------------------------------|--------------------------|
| Security & Cyber‑risk | **MFDS 보안지침 제16조** (cited in source) | FDA §524B, MDR Annex I §17.4 |
| Unique Device Identification (UDI) | **의료기기법** + **디지털의료제품법** (joint applicability referenced as DR‑19) | — |
| Risk Management | **ISO 14971:2019** (referenced via DR‑21) | — |
| Software Life‑Cycle | **IEC 62304:2006+A1:2015** (referenced via DR‑22) | — |
| Usability / Human Factors | **IEC 62366‑1:2015+A1:2020** (template missing – see DR‑06) | — |
| Clinical Evaluation (where required) | **디지털의료제품법** §?? (specific article not listed in source) | — |
| Post‑Market Surveillance | **PMS 고시** (referenced via DR‑14) | — |

---

### 4. Required Evidence Package (based on the above framework)

| Requirement | Evidence to be submitted | Current status (per source) |
|-------------|--------------------------|----------------------------|
| SBOM (Software Bill of Materials) | Completed SBOM document matching MFDS 보안지침 제16조 & FDA §524B & MDR Annex I §17.4 | **DR‑09** – ✅ fully covered |
| Incident Reporting SOP | Internal SOP aligned with PMS 고시 for “이상사례 보고” (3/7/15) | **DR‑14** – ✅ fully covered |
| UDI System | SOP‑UDI (issue 002) covering both 의료기기법 & 디지털의료제품법 | **DR‑19** – ✅ fully covered |
| Risk Management File (RMF) | Full RMF per ISO 14971:2019, including risk analysis, evaluation, control measures | **DR‑21** – ✅ fully covered |
| Software Development Documentation | IEC 62304‑compliant lifecycle documents (design, verification, validation) | **DR‑22** – ✅ fully covered |
| Usability Engineering Plan | IEC 62366‑1 usability plan & report template | **DR‑06** – *template missing* (partial gap) |
| Component Performance Evaluation SOP | SOP covering performance testing of each software component | **DR‑05** – *SOP absent* (critical gap) |
| Labeling / IFU Template for Digital Medical Device | Korean language labeling template meeting 디지털의료제품법 requirements | **DR‑10** – *template missing* (high priority) |
| Independent Software Suitability Assessment | Procedure to assess suitability of third‑party/stand‑alone software used in the product | **DR‑11** – *procedure absent* (high priority) |
| AI Explainability & Fairness Documentation | Documents describing explainability, bias mitigation, fairness for any AI/ML component | **DR‑32/33** – *documents missing* (high priority) |
| Data Integrity SOP (ALCOA+) | SOP ensuring data traceability, integrity per ALCOA+ principles | **DR‑31** – *SOP absent* (medium priority) |
| Autonomous Function Certification Playbook | Playbook for applying autonomous performance certification under 디지털의료제품법 | **DR‑15** – *playbook missing* (critical gap) |
| Post‑Learning / Model Drift Governance | Governance framework for continuous learning models & drift monitoring | **DR‑35** – *governance absent* (critical gap) |
| PCCP Decision Tree | Confirmed “PCCP” decision tree for product classification pathway | **DR‑04** – *decision tree not finalized* (medium priority) |
| GMP 적합판정 신청서 초안 | Draft application for KGMP suitability assessment (GMP 적합판정) | **DR‑02** – *draft missing* (high priority) |

---

### 5. Risk Controls Already Implemented (per source)

| Control | Standard / Guideline | Coverage |
|--------|----------------------|----------|
| SBOM generation & security alignment | MFDS 보안지침 제16조, FDA §524B, MDR Annex I §17.4 | ✅ |
| Incident reporting process | PMS 고시 | ✅ |
| UDI assignment & traceability | 의료기기법 + 디지털의료제품법 | ✅ |
| Comprehensive risk management (ISO 14971) | ISO 14971:2019 | ✅ |
| Software lifecycle management | IEC 62304 | ✅ |

These controls satisfy the core safety and security expectations for a digital medical product. The remaining gaps relate mostly to **process documentation, governance of AI/ML, data integrity, and post‑market learning**, which are essential under the Digital Medical Products Act.

---

### 6. Human‑Escalation Triggers  

| Trigger | Gap(s) Involved | Escalation Level |
|--------|-----------------|------------------|
| **P0 gaps** (critical omissions) – no SOP or playbook exists for a required activity | DR‑05, DR‑15, DR‑35, DR‑02 | Immediate escalation to Project Lead & Regulatory Affairs Manager; halt any further submission activities until addressed. |
| **Missing labeling template (DR‑10)** – Korean IFU cannot be finalized | Potential compliance violation with 디지털의료제품법 labeling rules | Escalate to Clinical/Regulatory Documentation lead within 2 business days. |
| **AI explainability & fairness documents missing (DR‑32/33)** – required for any AI component under the Act | May trigger regulator request for supplemental data during review | Escalate to AI/ML development team; schedule risk‐review meeting within 5 working days. |
| **Post‑learning governance absent (DR‑35)** – continuous learning devices must have drift monitoring per 디지털의료제품법 | Risk of non‑acceptance in MFMF review | Escalate to Quality Assurance & PMO; develop governance framework before dossier submission. |
| **Medium‑priority gaps** (P1) such as usability plan template, data integrity SOP, PCCP decision tree – if not resolved within 2 weeks, trigger a “Readiness Review” with senior RA leadership. |

---

### 7. Recommended Immediate Actions  

1. **Confirm Device Grade** → Obtain official classification; decide submission track (신고/인증/허가).  
2. **Address all P0 gaps** – develop missing SOPs (DR‑05, DR‑15, DR‑35) and draft the GMP 적합판정 신청서 (DR‑02).  
3. **Finalize labeling template** (DR‑10) in Korean language, referencing 디지털의료제품법 labeling requirements.  
4. **Create AI governance package** (DR‑32/33) and post‑learning drift framework (DR‑35).  
5. **Prepare usability engineering plan** (IEC 62366‑1) and data integrity SOP (ALCOA+) to close P1 items.  
6. **Complete PCCP decision tree** and submit for internal sign‑off (DR‑04).  

Once the above are in place, compile a full dossier comprising:

* Classification certificate / grade decision  
* KGMP suitability assessment (if applicable)  
* Full RMF (ISO 14971) and software lifecycle file (IEC 62304)  
* Security package (SBOM per MFDS 보안지침 제16조)  
* UDI system documentation  
* Labeling & IFU (Korean)  
* Clinical evaluation (if required by grade)  
* Post‑market surveillance plan (aligned with PMS 고시)

---

### 8. Peer Review Prompt  

> **Please review:**  
> * Are there any additional Digital Medical Products Act provisions (e.g., specific clinical evidence or real‑world data requirements) not captured in the current gap list?  
> * Does the identified need for a “PCCP decision tree” align with MFDS’s latest guidance on product pathway selection for digital health products?  
> * Are any of the P1 gaps (usability plan, data integrity SOP, labeling template) actually mandatory for the device grade we anticipate, thereby needing to be re‑prioritized?  

Your feedback will ensure that all jurisdiction‑specific obligations are fully addressed before submission.

--- 

**Regulatory Judgment & Escalation Summary**

*The device’s regulatory path cannot be finalized until its Korean grade is confirmed. Critical gaps (P0) must be resolved before any dossier preparation; otherwise the MFDS review will likely request supplemental documentation, causing delay.*  

*Escalate all P0 items immediately to senior RA leadership and pause submission activities pending their resolution.*

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

> 심각 결함 없음. '디지털의료제품법은 기존 등급 체계를 대체하지 않는다' 명시(SOUL 불릿 반영)·보안지침 제16조·DR-XX 소스 기반·'§?? (article not listed)' 정직한 자리표시자 — 조문 창작 방지 라인 첫 회차 효과. [최종 2점 — shadow 11차 하향 수용: 소스 불일치 DR-02 — 원문 표는 DR-02를 '부분·P1'로 분류하나 응답은 P0 목록에 포함·'Address all P0 gaps' 행동에 편입. 나머지(제16조·DR-XX·자리표시자)는 소스 기반 정확.]

**Source Excerpts**

1. Chunk `1091162552456558927`

> ### 3.1 정합(양호) 항목 - **DR-09(SBOM)** — MFDS 보안지침 제16조 ↔ FDA §524B ↔ MDR Annex I §17.4 ↔ SOP-SBOM-001 모두 일치 - **DR-14(이상사례 보고 3/7/15일)** — PMS 고시 ↔ 사내 이상사례 보고 절차 기한 일치 - **DR-19(UDI)** — 의료기기법 + 디지털의료제품법 양립, SOP-UDI(issue 002) 커버 - **DR-21(ISO 14971)** — ISO14971_프로세스_상세(issue 007)로 풀 커버 - **DR-22(IEC 62304)** — SW 수명주기 문서(issue 006)로 풀 커버

2. Chunk `434223568197517474`

> ### 3.2 불일치·공백 항목 | Req-ID | 불일치 유형 | 내용 | 우선도 | |---|---|---|---| | DR-05 | 공백 | 구성요소 성능평가 SOP 부재 | P0 | | DR-10 | 공백 | 디지털의료기기 표시기재 템플릿 미작성 | P1 | | DR-11 | 공백 | 독립형 SW 사용적합성 평가 절차 부재 | P1 | | DR-15 | 공백 | 자율성능인증 신청 플레이북 부재 | P0 | | DR-31 | 공백 | 데이터 무결성(ALCOA+) SOP 부재 | P1 | | DR-32/33 | 공백 | AI 설명성·공정성 평가 문서 없음 | P1 | | DR-35 | 공백 | 사후학습·드리프트 거버넌스 없음 | P0 | | DR-02 | 부분 | GMP 적합판정 신청서 초안 미작성 | P1 | | DR-04 | 부분 | PCCP 결정트리 미확정 | P1 | | DR-06 | 부분 | IEC 62366-1 사용적합성 계획서 템플릿 미정 | P1 |

### kb-eval-20261126-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-26", "decision_ref": "kb-eval-20261126-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "2f3cb1cb9e28010a", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2f3cb1cb9e28010a`
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

> **Regulatory Draft – Impact of the Digital Medical Products Act on a SaMD‑type product**

---

### 1. Classification & Submission Route  

| Item | Korean regulatory determination |
|------|---------------------------------|
| **Device type** | Software as a Medical Device (SaMD) – falls under the “디지털의료기기” definition introduced by the Digital Medical Products Act (DMPA). |
| **Grade** | Must be confirmed in 「의료기기 품목 및 품목별 등급에 관한 규정」.  SaMDs are commonly placed in **2등급** or **3등급**, depending on risk impact (e.g., diagnostic vs. therapeutic, level of automation).  *No specific grade is stated in the source; verify against the regulation.* |
| **Submission track** | • **2등급 → 인증** (technical‑document review by an MFDS‑designated 심사기관). <br>• **3등급·4등급 → 허가** (full approval by MFDS).  The exact route follows the confirmed grade. |
| **Applicable GMP assessment** | From 2025‑01‑24, NIDS (National Institute for Digital Health) is authorized to perform 디지털의료기기 GMP 적합판정 alongside existing 심사기관 (KTL, KTR, etc.)【1】.  If the product’s manufacturing site is a digital‑medical‑device dedicated facility, inclusion of NIDS in the reviewer pool should be considered. |

**Citations**  

* No specific MFDS 고시 or notice number appears in the source excerpts – *no specific identifier found in source — verify separately*.  
* The change to the DMPA (effective 2025‑01‑24) and NIDS GMP authority are described in the source table【2】.

---

### 2. Required Evidence Package  

| Requirement | Korean expectation | Typical evidence (foreign accepted where MFDS scope permits) |
|-------------|-------------------|---------------------------------------------------------------|
| **Technical Documentation** | 전반적인 설계·제조·품질 문서, 위험 관리 파일 등 (ISO 14971, IEC 62304, IEC 62366‑1) | • Design History File <br>• Software Development Lifecycle records (IEC 62304) <br>• Risk Management Report (ISO 14971) |
| **Clinical Evaluation** | MFDS accepts foreign clinical evaluation reports when the data are from a market with comparable standards and the device is substantially equivalent.  The DMPA‑specific guideline (2025‑05‑07) adds AI/ML‑based GUI requirements【2】. | • CE‑marked or FDA‑cleared predicate CER <br>• Clinical performance study summary (if required for higher grades) |
| **Non‑clinical Safety** | GLP non‑clinical data may be used under OECD MAD (mutual acceptance of non‑clinical data).  The Korean MFDS has adopted this for certain device categories. | • ISO 10993‑1 toxicology test report (biocompatibility) <br>• Electrical safety, EMC tests per IEC 60601‑1 series |
| **GMP Compliance** | KGMP 인증서 (3‑year validity).  For 디지털의료기기 the reviewer pool may include NIDS【1】. | • KGMP certificate issued by a designated 심사기관 <br>• Evidence of GMP 적합판정 for software‑centric facilities |
| **Labeling & IFU** | All labeling, instructions for use (IFU) and advertising material must be in Korean.  Specific format requirements are set out in MFDS 고시 (no number cited). | • Korean language label draft <br>• User manual (Korean) with safety notices |
| **Cybersecurity** | Compliance with the MFDS 사이버보안 가이드라인, referencing IEC 81001‑5‑1 (2021 edition). | • Threat model & mitigation plan <br>• Secure development lifecycle evidence |

*Where foreign evidence is used, MFDS requires a “mapping table” that shows equivalence to Korean requirements.*

---

### 3. Missing Information / Gaps  

| Gap | Why it matters | Remedy |
|-----|----------------|--------|
| **Exact device grade (1~4등급)** | Determines whether the pathway is 신고/인증/허가. | Perform a formal grade assessment against 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **Intended use & risk classification of the SaMD** (diagnostic, monitoring, therapeutic, level of autonomy) | Drives clinical evidence depth and the need for AI/ML‑specific evaluation. | Provide a clear Intended Use Statement and conduct a risk‑based classification per DMPA guidance (2025‑05‑07). |
| **AI/ML algorithm description & training data provenance** | The 2025‑05‑07 guideline adds specific clinical‑validation requirements for AI/ML GUIs. | Supply algorithm documentation, validation dataset details, and performance metrics. |
| **Local Korean clinical data (if required)** | For higher grades, MFDS may require at least a portion of the clinical evidence from the Korean population. | Plan a bridging study or collect post‑marketing surveillance data as per MFDS guidance. |
| **Evidence of NIDS involvement (if selected reviewer)** | GMP 적합판정 can be performed by NIDS; omission could delay review if MFDS expects it for digital devices. | Submit a request to include NIDS in the reviewer pool, or confirm that another designated 기관 is acceptable. |
| **Korean language labeling drafts** | Mandatory for all medical‑device submissions. | Prepare Korean versions and attach proof of professional translation. |

---

### 4. Risk Controls & QMS Alignment  

1. **Risk Management** – Conduct a full ISO 14971 risk analysis, linking each identified hazard to mitigation measures (including software‑related hazards per IEC 62366‑1).  
2. **Software Development Lifecycle** – Follow IEC 62304 (2006+A1:2015) for planning, development, verification, and maintenance.  
3. **Cybersecurity** – Implement the controls required by IEC 81001‑5‑1 (2021) and reflect them in a dedicated cybersecurity risk management file.  
4. **KGMP/QMS** – Obtain KGMP 인증 from a designated 심사기관; for 디지털의료기기 consider adding NIDS as an optional reviewer per the 2025 amendment【1】.  
5. **Post‑Market Surveillance (시판후조사)** – Establish a PMS plan that includes adverse event reporting in Korean, periodic safety update reports to MFDS, and a PMCF (post‑market clinical follow‑up) program where appropriate.

---

### 5. Citations  

| Source | Content referenced |
|--------|--------------------|
| **[1]** Chunk 1078228256164017760 | GMP 적합인정 절차 및 심사기관 현황; NIDS role for 디지털의료기기 starting 2025‑01‑24. |
| **[2]** Chunk 1121184088796802935 | Summary of regulatory changes 2025–2026, including DMPA enactment (2025‑01‑24), NIDS GMP authority, AI/ML guideline issuance (2025‑05‑07), and upcoming autonomous‑performance certification (2026). |
| **Framework references** (no specific identifier required) | ISO 14971:2019, IEC 62304:2006+A1:2015, IEC 62366‑1:2015+A1:2020, IEC 81001‑5‑1:2021, ISO 10993‑1:2018, KGMP (의료기기법 제28조). |

*No device‑specific clearance numbers or MFDS 고시 identifiers appear in the excerpts – “no specific identifier found in source — verify separately.”*

---

### 6. Human‑Escalation Triggers  

| Situation | Action |
|-----------|--------|
| **Uncertain grade (1~4등급)** after initial assessment | Escalate to senior regulatory lead; request formal classification opinion from MFDS or a certified consultant. |
| **Missing Korean labeling/IFU** at dossier completion | Halt submission; involve translation/legal team to produce compliant Korean documents before filing. |
| **AI/ML algorithm validation not yet aligned with 2025‑05‑07 guideline** | Pause regulatory filing; engage clinical affairs for additional performance data collection. |
| **KGMP 인증 not obtained or NIDS reviewer not confirmed** | Notify project manager; schedule GMP audit or submit a request to MFDS for inclusion of NIDS as 심사기관. |
| **Regulatory notice number required (e.g., specific 고시) but unavailable** | Flag to regulatory affairs manager; obtain the exact 고시 reference from MFDS website or legal database before final submission. |

---

### 7. Peer‑Review Prompt  

> *Please review the assumptions above, especially the inferred grade range for a SaMD and the reliance on AI/ML guideline requirements (2025‑05‑07). Confirm whether any additional Korean‑specific evidence (e.g., local usability testing) is required for the anticipated grade, and verify that NIDS can indeed serve as a designated 심사기관 for KGMP certification of pure software products.*

---

### 8. Reusable RA Judgment (Lesson Captured)

- **DMPA (effective 2025‑01‑24)** introduces a distinct SaMD classification system; the grade must always be checked against 「의료기기 품목 및 품목별 등급에 관한 규정」 before choosing 신고/인증/허가.  
- **NIDS** is now an authorized GMP 적합판정 기관 for 디지털의료기기; include it in reviewer selection when the product is a pure software or AI‑based device.  
- **AI/ML‑focused guidelines (2025‑05‑07)** add clinical‑performance documentation requirements that were not present for conventional devices; map foreign CERs to these new Korean expectations.  
- **All citations** of specific MFDS 고시, notice numbers, or article sections must be drawn directly from source material; otherwise mark the need for independent verification.  

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
- [ ] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 심각 결함 없음. 등급 '2~3등급 common… verify' 헷징·경로표·NIDS·제28조 전부 정확, 조문 번호 창작 0건(SOUL 라인 효과). 미세: 'MFMF review' 오타 1건(11-02 이후 간헐 재발 — 부수).

**Source Excerpts**

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---
