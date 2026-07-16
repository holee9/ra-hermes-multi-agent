# KB Eval Checksheet - 2026-07-17 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260717-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_us-001", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "a7cfbbe928232419", "source": "github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md", "source_hash": "19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `a7cfbbe928232419`
- Source: `github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_%C2%A7820.30_subsection_citations_systemic.md)
- Source hash: `19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md`는 `238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: `00_프로젝트관리/문서_매트릭스.md` 의 §820.30 표기는 본 SOP/Form frontmatter에서 자동 생성되므로 위 frontmatter 정정 후 빌드 스크립트로 자동 갱신됨. ## 배경 audit #921(2026-06-26) 종결 과정에서 SOP-AIGOV-001 frontmatter "FDA QMSR §820.30/ISO13485 §7.3"를 "§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30은 Reserved)"로 정정하였으나, **동일한 §820.30 subsection-letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스...
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

> **Regulatory Draft – QMSR (21 CFR Part 820) Design‑Control Alignment**  

---

### 1. Classification / Submission Route  
- **Device status:** No new device introduction identified in the source material; the issue concerns internal quality‑system documentation for an already cleared/registered product line.  
- **Regulatory pathway:** No additional 510(k), De Novo, or PMA filing required. The activity is a **post‑approval QMSR compliance remediation** that must be documented in the firm’s Quality Management System (QMS) and reported as part of routine FDA inspections or Form 483 follow‑up.

### 2. Required Evidence to Close the Audit Finding  
| Requirement | Description | Acceptable Evidence |
|-------------|------------|---------------------|
| **Correct citation of design‑control requirement** | All SOPs, Forms, and Matrix documents must reference **§820.10(c) (incorporating ISO 13485:2016 §7.3)** – not the reserved **§820.30**. | • Updated front‑matter screenshots showing “§820.10(c) → ISO 13485:2016 §7.3”. <br>• Revision control logs (eCFR‐based version numbers). |
| **Comprehensive inventory of affected documents** | Identify every SOP, Form, and Matrix that still contains a §820.30 subsection‑letter citation. | • Master spreadsheet listing document ID, title, location, original citation, new citation, revision date, and reviewer. |
| **Change control & CAPA closure** | Execute a Change Control (CC) that captures the edit, approval workflow, and implementation date; close the associated Corrective Action/Preventive Action (CAPA). | • CC record with signatures from QA Manager, RA Lead, and Document Control. <br>• CAPA closure report indicating “Root cause = legacy citation pattern”, corrective action = “global find‑replace & re‑release”. |
| **Training verification** | Personnel who author or maintain QMS documentation must be trained on the new citation rule. | • Training attendance list, LMS completion certificate, and post‑training assessment results. |
| **Regulatory submission (if required)** | None expected unless the change constitutes a “design change” that impacts device labeling/indications. In such case, assess whether a 510(k) amendment is needed. | – |

### 3. Missing Information / Gaps Identified  
1. **Full scope of residual §820.30 citations** – only a grep check was mentioned; the exact count and location list are absent.  
2. **Timeline for remediation** – no target dates (e.g., “all updates completed within 30 days”).  
3. **CAPA number/linkage** – audit reference #921 is noted, but the formal CAPA identifier is not provided.  
4. **Impact assessment** – whether any cited §820.30 references affect released devices’ design‑control records or risk management files has not been evaluated.  

### 4. Risk Controls & Mitigation Measures  
| Risk | Potential Impact | Control / Mitigation |
|------|------------------|----------------------|
| Continued use of reserved §820.30 citations | FDA may deem QMS non‑compliant → Form 483, Warning Letter, possible product hold. | • Global document search and automated replacement to §820.10(c). <br>• Periodic (quarterly) audit of design‑control references. |
| Incomplete inventory leading to missed documents | Hidden non‑conformities escape detection. | • Maintain a living “Citation Registry” in the QMS database; cross‑reference with Document Control master list. |
| Training gaps → re‑introduction of legacy citations | Recurrence of the problem after personnel turnover. | • Include citation rule in SOP authoring training curriculum; add to annual competency assessment. |
| Change control not linked to device DMRs (Design History File) | Design‑control records become inconsistent with FDA expectations for a design history. | • Map each updated SOP/Form to affected Device Master Records (DMRs); attach CC record as an annex. |

### 5. Key Regulatory Citations  
- **eCFR 21 CFR Part 820** – Quality System Regulation, effective 2 Feb 2026. <br> • §820.30 is fully **Reserved** (no substantive requirements). <br> • Design‑control requirements are now located in **§820.10(c)** which incorporates **ISO 13485:2016 §7.3** by reference.  
- **ISO 13485:2016**, Clause 7.3 – Design and Development.  

*No specific 510(k) or predicate identifiers appear in the source excerpts.*  

### 6. Human‑Escalation Triggers  
| Trigger | Action & Owner |
|---------|----------------|
| **Residual §820.30 citations > 0 after remediation deadline** | Immediate escalation to **QA Manager** for root‑cause re‑evaluation; if not resolved within an additional 7 days, forward to **Regulatory Affairs Director**. |
| **CAPA #921 remains open > 30 days post‑audit** | Notify **Chief Compliance Officer** and schedule a cross‑functional review meeting. |
| **Training completion < 95 % for affected personnel** | Escalate to **HR/Training Lead**; impose temporary hold on any new SOP releases until remediation. |
| **FDA inspection discovers non‑conformity related to this issue** | Activate **Regulatory Incident Response Plan**, involve Legal and senior leadership within 24 hours. |

---

### 7. Next Steps (Action Items)  
1. Execute a **full-text search** across the QMS repository for “§820.30” and capture all hits in an audit‑trackable spreadsheet. *(Owner: Document Control, due 2026‑07‑31)*  
2. Issue a **Change Control** to replace each citation with “§820.10(c) → ISO 13485:2016 §7.3”. Include versioning and approval signatures. *(Owner: QA Manager, due 2026‑08‑15)*  
3. Close **CAPA #921** by attaching the updated documents, evidence of search results, and training records. *(Owner: Regulatory Affairs Lead, due 2026‑08‑20)*  
4. Schedule a **quarterly compliance check** to verify that no new §820.30 references reappear. *(Owner: QA Manager, start 2026‑09‑01)*  

---

### Peer Review Prompt  
> @RegAffPeer – Please review this draft and challenge the following:  
> 1. Are we certain that no device‐specific 510(k) amendment is required for the citation change? (Consider any DMRs tied to design control).  
> 2. Does the scope of the grep check fully capture embedded citations in non‑textual assets (e.g., PDFs, Excel matrices)?  
> 3. Are there any jurisdictional nuances (e.g., EU MDR Annex 4) that we should note given our cross‑border product portfolio?  

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

1. Chunk `1123403925433224246`

> `00_프로젝트관리/문서_매트릭스.md` 의 §820.30 표기는 본 SOP/Form frontmatter에서 자동 생성되므로 위 frontmatter 정정 후 빌드 스크립트로 자동 갱신됨.

2. Chunk `152477499522968513`

> ## 배경 audit #921(2026-06-26) 종결 과정에서 SOP-AIGOV-001 frontmatter "FDA QMSR §820.30/ISO13485 §7.3"를 "§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30은 Reserved)"로 정정하였으나, **동일한 §820.30 subsection-letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스 전반에 분산 잔존**함을 grep 점검에서 확인. eCFR 21 CFR Part 820(QMSR, 2026-02-02 시행) §820.30은 본문 전체가 Reserved이고, 설계관리 요구는 §820.10(c)가 ISO 13485:2016 §7.3을 incorporation by reference로 끌어오는 단일 경로로 일원화되었다.

### kb-eval-20260717-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_us-002", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "8ce24ca4b172110f", "source": "github:holee9/MD-process/issue-drafts/921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md", "source_hash": "36a0683dda1f189f95c3bba8f11be7917c7ed24fdf703b490573ae5ef6cf0b16"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `8ce24ca4b172110f`
- Source: `github:holee9/MD-process/issue-drafts/921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_%EC%9D%B8%EC%9A%A9%EB%B6%80%EC%A0%95%ED%99%95.md)
- Source hash: `36a0683dda1f189f95c3bba8f11be7917c7ed24fdf703b490573ae5ef6cf0b16`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md`는 `921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 권고 수정 1. frontmatter `applicable:` — - 변경 전: `FDA QMSR §820.30/ISO13485 §7.3` - 변경 후: **`FDA QMSR §820.10(c) → ISO 13485:2016 §7.3`** (또는 `FDA QMSR §820.10(c) (incorporation by reference) — ISO 13485:2016 §7.3`) 2. §3.2 헤더 또는 도입문에 "QMSR는 §820.30을 Reserved 처리하고 ISO 13485:2016 §7.3를 incorporation by reference로 적용" 단서 1줄 추가. 3. 사내 자매문서 SOP-DHF-001, SOP-DT...
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

### 1. Likely FDA Submission Pathway  
- **Pathway:** 510(k) (Traditional or Special) **or** De Novo if no predicate exists.  
- **Rationale:** All commercial medical devices in the U.S. must demonstrate compliance with the Quality Management System Regulation (QMSR) – 21 CFR 820 – as part of any pre‑market submission. The excerpt explicitly references applying QMSR via incorporation by reference of ISO 13485:2016 §7.3, which is required for both 510(k) and De Novo dossiers.  

> **Citation:** Source [1] – amendment to front‑matter indicating “FDA QMSR §820.10(c) → ISO 13485:2016 §7.3”.

*No device‑specific classification (Class I–III) appears in the source; it must be derived from the intended use and risk profile after a product description is supplied.*

---

### 2. Required Evidentiary Package for Submission  

| Requirement | Description | Evidence Needed |
|-------------|--------------|-----------------|
| **QMS Conformance** | Incorporate FDA QMSR by reference to ISO 13485:2016 §7.3 (design‑control clause). | • Updated SOPs showing “FDA QMSR §820.10(c) → ISO 13485:2016 §7.3” adoption (see Source [1]).<br>• Current QMS audit report confirming all required clauses are in place. |
| **Design History File (DHF)** | Complete DHF per 21 CFR 820.30 and ISO 13485 §7.3 covering design inputs, outputs, verification, validation, risk analysis, and change control. | • DHF index with traceability matrix.<br>• Design‑input validation reports.<br>• Verification & validation protocols/results. |
| **Risk Management** | Perform risk analysis per ISO 14971, link identified hazards to design controls. | • Hazard analysis report (HRA) showing mitigation via design controls referenced in DHF. |
| **Labeling/Intended Use Statement** | Clear labeling that matches the device’s intended use and predicate comparison. | • Draft 510(k) label & instructions for use (IFU). |
| **Predicate Device Evidence** (for 510(k)) | Demonstrate substantial equivalence to a legally marketed device. | • Predicate identification, classification, regulation number, and side‑by‑side comparison table. *(Not present in source; must be supplied.)* |

---

### 3. Identified Gaps / Missing Information  

| Gap | Why It Matters | Action |
|-----|----------------|--------|
| **Device Description & Intended Use** | Determines classification and predicate search. | Obtain product brief from engineering/marketing. |
| **Predicate Device Identification** | Required for traditional 510(k) submission. | Conduct regulatory search; document 510(k) number, regulation class, and indications. |
| **Evidence of Full QMS Implementation** | Source only shows amendment to documentation language; does not prove execution. | Provide latest internal audit report or FDA inspection readiness checklist. |
| **Risk Management Documentation (ISO 14971)** | Needed to link hazards to design controls. | Submit HRA & risk control plan. |
| **Design Control SOPs referenced in “SOP‑DHF‑001, SOP‑DT‑001, SOP‑DVV‑001”** | Confirmation that all design‑control processes are covered. | Provide copies or summaries of these SOPs with traceability to ISO 13485 §7.3. |
| **Regulatory Strategy Decision (510(k) vs De Novo)** | Impacts data package size & content. | Clarify if a predicate exists; otherwise plan for De Novo. |

---

### 4. Key Risk Controls Related to QMSR Alignment  

1. **Incorporation‑by‑Reference Control** – Ensure every design‐control activity (input, output, verification, validation) is explicitly mapped to ISO 13485:2016 §7.3 clauses.  
2. **Change Management** – SOP‑DT‑001 must capture design changes with risk re‑assessment and QMS impact analysis.  
3. **Document Control** – SOP‑DVV‑001 to guarantee versioning, approvals, and secure storage of DHF artifacts.  
4. **Training & Competency** – Record staff training on the revised QMSR reference (§820.10(c)).  

---

### 5. Citations (per source)

| Source | Relevant Content |
|--------|-------------------|
| **[1] Chunk 1097299844760913437** | Amendment: “FDA QMSR §820.10(c) → ISO 13485:2016 §7.3” and inclusion of design‑control SOPs (SOP‑DHF‑001, SOP‑DT‑001, SOP‑DVV‑001). |
| **[2] Chunk 256687378158019657** | Reference to “The New FDA 21 CFR Part 820 – QMSR” as a Tier 2 guidance resource. |

*No specific 510(k) numbers, predicate identifiers, or registration numbers appear in the supplied excerpts.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Condition | Recommended Escalation |
|---------|-----------|------------------------|
| **Missing Device Description / Intended Use** | No product brief received after initial request (48 h). | Escalate to Project Lead (Regulatory Manager). |
| **No Predicate Identified** | Predicate search yields <1 viable candidate within 5 business days. | Flag to Senior Regulatory Affairs for De Novo feasibility assessment. |
| **QMS Audit Gap** | Internal audit indicates non‑conformance to §820.10(c) reference. | Immediate notification to Quality Assurance Director and corrective action plan initiation. |
| **Risk Management Incomplete** | HRA not linked to design controls after 7 days of deadline. | Escalate to Chief Engineering Officer for risk mitigation resources. |
| **Regulatory Timeline Threat** | Submission package >30 % incomplete past planned submission date. | Notify Regulatory Affairs VP and request additional staff support. |

---

### 7. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made in this draft, specifically:  
> 1. The interpretation that §820.10(c) incorporation by reference of ISO 13485:2016 §7.3 suffices for all design‑control requirements across device classes.  
> 2. Whether any additional FDA guidance (e.g., “QMSR Reserved” discussion in Tier 2 resources) imposes further evidentiary obligations not captured above.  
> 3. Potential jurisdictional gaps—does the current analysis address post‑market surveillance expectations under the new QMSR framework?  
> Provide any missing citations, regulatory nuances, or alternative pathway considerations (e.g., Special 510(k) for design changes).  

--- 

*Prepared by:* **Mike – US Regulatory Affairs Specialist**  
*Date:* 2026‑07‑17.

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

1. Chunk `1097299844760913437`

> ## 권고 수정 1. frontmatter `applicable:` — - 변경 전: `FDA QMSR §820.30/ISO13485 §7.3` - 변경 후: **`FDA QMSR §820.10(c) → ISO 13485:2016 §7.3`** (또는 `FDA QMSR §820.10(c) (incorporation by reference) — ISO 13485:2016 §7.3`) 2. §3.2 헤더 또는 도입문에 "QMSR는 §820.30을 Reserved 처리하고 ISO 13485:2016 §7.3를 incorporation by reference로 적용" 단서 1줄 추가. 3. 사내 자매문서 SOP-DHF-001, SOP-DT-001, SOP-DVV-001 등 설계관리 인용 일괄 점검(파급 확인).

2. Chunk `256687378158019657`

> ## Tier 2 (보조) - BSI Compliance Navigator "The New FDA 21 CFR Part 820 – QMSR" (Reserved 처리 설명, 범위 확인용)

### kb-eval-20260717-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_us-003", "iteration": 1, "matched_keywords": ["PMA"], "profile_id": "ra-us", "scenario_id": "85724102009d170d", "source": "github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md", "source_hash": "ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `85724102009d170d`
- Source: `github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/229_02_SOP-PMA-001_%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81_KPI%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4_8.1_8.2.5_8.5.1.md)
- Source hash: `ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd`
- Focus: QMSR and design-control readiness
- Matched keywords: PMA

**Source Summary**

- 문서 요약: `229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md`는 `229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 갭 내용 | 조항 | 요구사항 | 현재 상태 | |------|----------|-----------| | §8.1 | 적합성·효과성·개선 모니터링·분석·개선 계획 | partial | | §8.2.5 | 프로세스 성과 모니터링·미달 시 CAPA 트리거 | partial | | §8.5.1 | 품질정책·목표·감사·분석·시정·MR 통한 효과성 개선 | partial | ## Definition of Done - [ ] `02_품질경영시스템_QMS/SOP-PMA-001_프로세스_모니터링_분석_절차.md` 신규 (v0.1) - 프로세스 카탈로그(설계·구매·제조·검사·서비스·PMS·CAPA·교육·문서) — 9개 - KPI 매트릭스(...
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

### 1. Bottom‑Line Assessment  
- **Current status:** Partial compliance with ISO 13485 §§8.1, 8.2.5, 8.5.1 and FDA Quality Management System Regulation (QMSR) §§820.250 (statistical techniques) & §820.100 (CAPA).   
- **Immediate need:** Complete the KPI‑matrix, close the loop between KPIs → MR → CAPA, and document statistical validation before any 510(k) or PMA submission can be considered “ready” for FDA review.

---

### 2. Classification / Submission Route (Assumed)

| Device Context (from SOP name) | Likely FDA Class* | Recommended Pathway |
|--------------------------------|-------------------|---------------------|
| **PMA‑related** process monitoring SOP (SOP‑PMA‑001) | Class III (high‑risk) – requires PMA | Full PMA dossier including robust QMSR compliance evidence |

\*Class determination is speculative; a definitive classification requires the device’s intended use, indications, and predicate/novelty analysis.  

---

### 3. Required Evidence for Submission

| Requirement | Description | Source Reference |
|-------------|-------------|------------------|
| **QMS Policy & Objectives** (ISO 13485 §8.5.1) | Formal quality policy, measurable objectives, internal audit plan, MR effectiveness assessment. | Excerpt [1] – §8.5.1 “품질정책·목표·감사·분석·시정·MR 통한 효과성 개선” (partial) |
| **Process KPI Matrix** | 9‑process catalog × 3 dimensions = 27 cells; each KPI with measurement method, frequency, threshold, owner, and statistical analysis plan (SPC, Pareto, Ishikawa). | Excerpt [2] – “KPI 매트릭스(프로세스 × 측정지표 × 주기 × 임계치 × 소유자) — 정량” |
| **Statistical Technique Validation** | Documented use of SPC (control limits), justification of control chart types, verification that methods meet FDA QMSR §820.250. | Excerpt [2] – “데이터 수집·분석 방법(통계기법: SPC·Pareto·Ishikawa)” |
| **CAPA Trigger Logic** | Explicit linkage: KPI breach → CAPA initiation → MR entry → resource reallocation; include timing metrics and closure criteria. | Excerpt [2] – “미달 시 트리거(CAPA·MR 입력·자원 재배치) 폐쇄루프” |
| **Design‑Control Integration** | Show how process monitoring outputs feed back into design controls (e.g., risk management, verification/validation). | Implicit in “품질목표→KPI→MR” loop; no direct citation. |
| **Training Records** | Evidence that owners and staff are trained on KPI measurement, statistical methods, CAPA procedures. | Not present – identified as missing. |
| **Internal Audit Reports** | Audits covering §§8.1/8.2.5/8.5.1 with findings, corrective actions, effectiveness verification. | Excerpt [2] – “ISO‑8.1/8.2.5/8.5.1 `status: met` 갱신” (but only status, not full report). |
| **Regulatory Mapping Document** | Table linking ISO 13485 clauses to FDA QMSR sections and EU MDR Art.10(9)(j). Already drafted (see Excerpt [2]). | Excerpt [2] – “규제 매핑: ISO 13485 §8.1/8.2.5/8.5.1, FDA QMSR §820.250·§820.100, EU MDR Art.10(9)(j)” |

*No specific PMA/510(k) predicate numbers appear in the source – verify separately.*

---

### 4. Missing / Incomplete Information  

| Gap | Action Required |
|-----|-----------------|
| **KPI Completion** – only “partial” status for §8.1, §8.2.5, §8.5.1. | Define all KPI thresholds, owners, and measurement methods; achieve 100 % coverage. |
| **Statistical Validation Evidence** – method description present but no validation data. | Perform and document validation of SPC rules (type‑I/II error rates) per §820.250. |
| **CAPA Closure Timelines** – trigger logic defined, but no documented timelines or effectiveness metrics. | Establish measurable CAPA closure windows (e.g., 30 days) and link to MR effectiveness verification. |
| **Training Records** – not referenced. | Generate training matrices, attendance logs, competency assessments for all process owners. |
| **Audit Traceability** – status “met” but full audit reports missing. | Conduct internal audits covering each ISO 13485 clause; archive findings & corrective actions. |
| **Risk Management Integration** – no explicit FMEA or risk analysis linking KPI failures to device‑level risks. | Perform process‑level FMEA; map high‑risk KPI breaches to design‑control risk mitigations. |

---

### 5. Risk Controls (Design‑Control Lens)

1. **Process‑Level Risk Analysis** – FMEA for each of the nine processes; identify severity, occurrence, detection scores.
2. **KPI‑Driven Monitoring** – Real‑time SPC charts with automatic alerts when trends exceed control limits.
3. **Automated CAPA Trigger** – Pre‑programmed workflow: KPI breach → CAPA creation → MR entry → notification to owner.
4. **Resource Reallocation Protocol** – Define thresholds that mandate additional staffing or equipment to remediate recurring deviations.
5. **Effectiveness Verification** – Post‑CAPA MR review linked back to original KPI trend; demonstrate statistical shift back within acceptable limits before closure.
6. **Design‑Control Feedback Loop** – Document any process improvement affecting design inputs/outputs (e.g., change in manufacturing tolerance resulting from KPI analysis).

All controls map to FDA QMSR §§820.30 (Design Controls) and §820.100 (CAPA), as well as ISO 13485 §§7.1 (Risk Management) & 8.2 (Process Validation).

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Level | Documentation |
|--------|------------------|---------------|
| KPI exceeds predefined control limit for >2 consecutive measurements | QMS Manager → Senior Management | KPI trend chart, CAPA initiation log |
| CAPA not closed within defined timeframe (e.g., 30 days) | Quality Assurance Director | CAPA tracker report |
| MR entered without linkage to a KPI breach or design‑control change | QA Lead → Regulatory Affairs | MR form audit trail |
| Internal audit finding on §8.1/§8.2.5/§8.5.1 non‑conformance | QA Manager → Executive Sponsor | Audit report & corrective action plan |
| Statistical method validation fails (e.g., Type I error >5 %) | Statistician Lead → Regulatory Affairs | Validation protocol & summary |

Escalations should be recorded in the QMS change control system with timestamps and responsible parties.

---

### 7. Peer‑Review Prompt  

> **TO:** RA Team – Quality/Regulatory Review  
> **Subject:** Challenge of Assumptions & Gaps in QMSR Readiness Draft (SOP‑PMA‑001)  
> Please review the assumptions made regarding:  
> 1. The inferred Class III / PMA pathway without explicit device indication data.  
> 2. Completeness of KPI mapping to all required ISO 13485 and FDA QMSR clauses.  
> 3. Sufficiency of statistical validation evidence as described.  
> 4. Potential EU MDR or other jurisdictional considerations not covered by the current source excerpts.  

Provide comments on any overlooked regulatory requirements, missing documentation, or alternative escalation criteria.

---

### 8. Reusable RA Judgment (Recorded for Future Cases)

**Judgment ID:** QMSR‑Readiness‑2026‑07‑17  
**Key Takeaway:** When a SOP references ISO 13485 §§8.1/8.2.5/8.5.1 and maps to FDA QMSR §§820.250 & §820.100, treat “partial” status as a red flag; require **full KPI definition**, **statistical method validation**, **complete CAPA‑MR linkage**, and **documented training/audit evidence** before proceeding with any high‑risk (Class III) submission such as a PMA. Absence of explicit predicate identifiers in source material mandates *external verification* prior to inclusion in the submission docket.

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

1. Chunk `1039190717614682920`

> ## 갭 내용 | 조항 | 요구사항 | 현재 상태 | |------|----------|-----------| | §8.1 | 적합성·효과성·개선 모니터링·분석·개선 계획 | partial | | §8.2.5 | 프로세스 성과 모니터링·미달 시 CAPA 트리거 | partial | | §8.5.1 | 품질정책·목표·감사·분석·시정·MR 통한 효과성 개선 | partial |

2. Chunk `611272139046336025`

> ## Definition of Done - [ ] `02_품질경영시스템_QMS/SOP-PMA-001_프로세스_모니터링_분석_절차.md` 신규 (v0.1) - 프로세스 카탈로그(설계·구매·제조·검사·서비스·PMS·CAPA·교육·문서) — 9개 - KPI 매트릭스(프로세스 × 측정지표 × 주기 × 임계치 × 소유자) — 정량 - 데이터 수집·분석 방법(통계기법: SPC·Pareto·Ishikawa) - 미달 시 트리거(CAPA·MR 입력·자원 재배치) 폐쇄루프 - §8.5.1 효과성 측정 연계(품질목표→KPI→MR) - [ ] `02_품질경영시스템_QMS/F-PMA-001_KPI_매트릭스.md` 신규 — 27개 셀(9프로세스×3차원) - [ ] CHK-ISO13485-001 ISO-8.1/8.2.5/8.5.1 `status: met` 갱신 - [ ] SOP-MR-001/SOP-CAPA-001/F-MR-001 정합성 — KPI ↔ MR 입력 ↔ CAPA 트리거 - [ ] 규제 매핑: ISO 13485 §8.1/8.2.5/8.5.1, FDA QMSR §820.250(통계기법)·§820.100(CAPA), EU MDR Art.10(9)(j) - [ ] 적대적 자기검토(심사관 모드)

### kb-eval-20260717-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "67a0ba7fa7d4fc3a", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "8049315bab61421790bb62b12e868c8a33a7bdd1f4b989a98ed1c61790bf7f53"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `67a0ba7fa7d4fc3a`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_2026.md)
- Source hash: `8049315bab61421790bb62b12e868c8a33a7bdd1f4b989a98ed1c61790bf7f53`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_2026.md`는 FDA QMSR 2026 전환에 따른 ISO 13485 기반 QMS·design control·inspection 준비 문서입니다.
- 현재 excerpt 핵심: ### 2.2 구조 매핑 | QMSR (21 CFR 820) | 내용 | 대응 ISO 13485 조항 | |-------------------|------|-------------------| | §820.1 | 범위 | — | | §820.3 | 정의 | ISO 13485 §3 + 추가 정의 | | §820.10 | ISO 13485 참조편입 선언 | 4~8 전체 | | §820.20 | 경영검토 추가 입력 | 5.6 보완 | | §820.25 | 라벨링·포장 관리 | 7.5 보완 | | §820.30 | 설계관리 유지 (Class I 면제 외) | 7.3 보완 | | §820.35 | 기록관리 추가요구 | 4.2.5 보완 | |...
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

> **Regulatory Draft – QMSR (21 CFR 820) Compliance & Design‑Control Readiness**  

---

### 1. Likely Classification / Submission Route  
| Device Type* | FDA Class | Typical 510(k) Path | Design‑Control Requirement |
|--------------|-----------|----------------------|----------------------------|
| Class I (non‑exempt) | I | Registration only; **no** 510(k) required | No formal design‑control files required, but QMSR still applies. |
| Class I (exempt) | I* | None (registration & listing only) | Design‑control not mandatory – only basic QMSR elements. |
| Class II / III | II or III | **Traditional 510(k)** (or **Special/Modernized** if substantial equivalence exists). | Full design‑control (21 CFR 820.30) required, plus risk management per ISO 14971. |

\*The actual class depends on the device’s intended use and predicate status – this draft assumes a **Class II** surgical instrument as a common example; adjust accordingly.

---

### 2. Required Evidence for QMSR Alignment  

| CFR §820 Section | Mapping to ISO 13485 (per source) | Documentation Needed |
|------------------|-----------------------------------|-----------------------|
| **§820.1 – Scope** | — | Statement of scope covering all device families. |
| **§820.3 – Definitions** | ISO 13485 §3 + FDA additions | Glossary aligning FDA terms to ISO definitions. |
| **§820.10 – Incorporation by Reference** | §§4‑8 (ISO) | List of ISO standards incorporated; evidencing cross‑reference. |
| **§820.20 – Management Review** | §5.6 (ISO) | Minutes, action items, and effectiveness assessments. |
| **§820.25 – Labeling & Packaging Control** | §7.5 (ISO) | Label/Packaging procedures, artwork approvals, traceability matrices. |
| **§820.30 – Design Controls** *(required for Class II/III)* | §7.3 (ISO) – **requires supplemental evidence** | *Design History File* containing: user needs, design inputs, risk analysis, verification & validation protocols/results, design reviews, change control records. |
| **§820.35 – Document Control** | §4.2.5 (ISO) | Document‑control SOPs, master record index, retention schedule. |
| **§820.45 – Device Identification Inspection** | New (§) | Procedure for final device inspection and unique identifier verification. |
| **§820.198 – Complaint Handling** | §8.2.2 (ISO) | Complaint handling SOP, investigation logs, trend analysis. |

*All above items must be retained per the QMSR record‑keeping requirements (electronic or paper).*

---

### 3. Missing Information / Gaps to Address  

| Gap | Why It Matters | Action Needed |
|-----|----------------|---------------|
| **Intended Use & Predicate Device(s)** | Determines classification and 510(k) strategy. | Define indication, target patient population, and identify a legally marketed predicate (if any). |
| **Risk Management Plan (ISO 14971)** | QMSR expects risk controls to be demonstrated; mandatory for Class II/III. | Produce a documented risk analysis, evaluation of residual risk, and mitigation measures. |
| **Traceability Matrix (Design ↔ Requirements ↔ Verification)** | Required for design‑control compliance (820.30). | Map each design input to verification test and acceptance criteria. |
| **Labeling & Packaging Specifications** | §820.25 demands control; missing in source table. | Develop SOPs, artwork approvals, barcode/UDI procedures, and packaging integrity testing. |
| **Post‑Market Surveillance / PMS Plan** | QMSR expects ongoing monitoring (though not explicit in the excerpt). | Draft a PMS plan with periodic safety reporting and trend analysis. |
| **Electronic QMS System Validation** | If using software for records, 820.180 (confidentiality) still applies; source notes repeal but validation is best practice. | Validate electronic system for integrity, security, backup, and audit trails. |

---

### 4. Core Risk Controls to Implement  

1. **Design Input Review & Approval** – documented peer review before downstream work.  
2. **Design Verification/Validation (V&V)** – test protocols aligned with user needs; statistical acceptance criteria.  
3. **Change Control** – formal change request, impact analysis, and re‑verification where applicable.  
4. **Production Process Controls** – in‑process inspections, process capability studies (Cp/Cpk).  
5. **Device Identification & Unique Device Identifier (UDI)** – ensure each unit is readable at final inspection (820.45).  
6. **Complaint Management & CAPA Loop** – root‑cause analysis and corrective actions fed back to design/production.  

---

### 5. Citations (as required)  

| Source | Relevant Content |
|--------|------------------|
| **Source Excerpt [1]** – Structure mapping table | Provides the direct §820–ISO 13485 cross‑reference used above. |
| **Source Excerpt [2]** – FDA QMSR official guidance URLs, Federal Register notices (2024‑01709, 2025‑21955) | Confirms regulatory basis for QMSR and latest amendments (effective 02‑Feb‑2026). |

*No specific identifier (e.g., 510(k) number or predicate device K‑number) appears in the source excerpts – verify separately.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Target | Timing |
|---------|-------------------|--------|
| **Insufficient design‑control documentation** (missing DHF elements) | Senior Design Engineer / QA Manager | Immediately upon discovery during internal audit. |
| **Failure to demonstrate compliance with a new §820 section (e.g., §820.45 device identification)** | Regulatory Affairs Lead & Compliance Officer | Within 5 working days of notice. |
| **Unresolved FDA Form 483 observations** (related to QMSR) | Director, Regulatory Affairs & Executive Management | Within 48 hours of receipt. |
| **Critical deviation in risk‑mitigation effectiveness** (residual risk > acceptable) | Chief Clinical Officer & Head of R&D | At the moment of risk assessment sign‑off. |
| **Inability to produce required records for an FDA inspection** | Legal Counsel & Corporate Compliance | Prior to inspection notice; activate contingency plan. |

---

### 7. Peer Review Prompt  

> *Colleague, please review this draft and challenge the following:*  
> - Are the classification assumptions appropriate for our device family?  
> - Does the mapping table fully capture all §820 sections that are newly emphasized under QMSR (e.g., any post‑2025 amendments not captured in the source)?  
> - Have we identified all jurisdiction‑specific gaps, such as UDI requirements or FDA Compliance Program 7382.850 implications?  

---

### 8. Reusable RA Judgment (Honcho Entry)  

```
honcho_conclude:
  lesson: |
    For any new device development after Feb 2026, QMSR (21 CFR 820) now requires explicit mapping of each FDA quality‑system clause to ISO 13485 clauses. Design controls (§820.30) remain mandatory for Class II/III devices; therefore a complete DHF must be prepared even when the device is exempt from 510(k). Missing predicate identification, risk‑management plan (ISO 14971), and traceability matrices are the most common gaps that trigger human escalation. Cite only identifiers present in source material; otherwise note “no specific identifier found in source — verify separately.”
  confidence: high
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

1. Chunk `1041077994247338699`

> ### 2.2 구조 매핑 | QMSR (21 CFR 820) | 내용 | 대응 ISO 13485 조항 | |-------------------|------|-------------------| | §820.1 | 범위 | — | | §820.3 | 정의 | ISO 13485 §3 + 추가 정의 | | §820.10 | ISO 13485 참조편입 선언 | 4~8 전체 | | §820.20 | 경영검토 추가 입력 | 5.6 보완 | | §820.25 | 라벨링·포장 관리 | 7.5 보완 | | §820.30 | 설계관리 유지 (Class I 면제 외) | 7.3 보완 | | §820.35 | 기록관리 추가요구 | 4.2.5 보완 | | §820.45 | 기기 표시 검사 | 신설 | | §820.180 | (폐지) 기밀성 예외 | — | | §820.198 | 불만처리 추가 | 8.2.2 보완 |

2. Chunk `197674093189403324`

> ## 7. 출처 - FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr - FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions - eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820 - Federal Register: 2024-01709 (제정), 2025-21955 (기술적 수정) - FDA Compliance Program 7382.850 - 확인일: 2026-05-25

### kb-eval-20260717-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "859740700145052c", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `859740700145052c`
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

> **Regulatory Draft – QMSR Compliance & 510(k) Strategy for an X‑ray System (Design‑Control Readiness)**  

---

### 1. Device Classification & Submission Route  
| Item | Determination |
|------|----------------|
| **Device class** | Likely **Class II** (radiology imaging equipment) under 21 CFR 862. “X‑ray system” is commonly classified as Class II with special controls (e.g., radiation safety, performance standards). |
| **Regulatory pathway** | **Traditional 510(k)** demonstrating substantial equivalence to a legally marketed predicate device. A **Special 510(k)** may be viable if the submission concerns only design‑control updates that are within the scope of an existing cleared device and no new intended uses are introduced. |
| **Predicate identification** | No specific K‑numbers appear in the source material – **verify separately** by searching the FDA’s 510(k) database for X‑ray systems with the same indication, technology, and performance characteristics. |
| **Alternative route (if novel)** | If the device incorporates a fundamentally new technology not covered by an existing predicate, consider **De Novo classification** after preparing a robust risk analysis and performance data package. |

---

### 2. Required Evidence for Submission  

| Requirement | What to Provide | Source‑based Note |
|-------------|----------------|--------------------|
| **Device Description & Intended Use** | Clear statement of clinical purpose, anatomical site, patient population, and operating environment. | – |
| **Design History File (DHF)** | Complete documentation of design inputs, outputs, verification/validation, risk management (ISO 14971), and design changes. Must be traceable to QMSR record‑control requirements. | ISO 13485 §4.2.5 is **baseline**, but FDA §820.35 adds **additional** records – see source [1]. |
| **Device Master Record (DMR)** | All production, labeling, packaging, and process specifications required for commercial manufacturing. Include record‑control SOPs that meet QMSR §820.35. | Source [2] defines the “FDA QMSR ↔ ISO 13485” diff table – use form **F‑QMSR‑REC‑001** to demonstrate compliance. |
| **Labeling & UDI** | Full labeling set (IFU, safety labels) and integration of a Unique Device Identifier compliant with 21 CFR 830. | Source [2] lists UDI as a relevant requirement. |
| **Performance Testing** | Bench‑top functional testing, radiation output measurements, imaging quality assessment, and any software verification if applicable. | Standard for Class II radiology devices. |
| **Sterilization / Biocompatibility (if applicable)** | Validation reports per ISO 10993 & relevant USP/ISO sterilization standards. | – |
| **Software Validation (if software‑controlled)** | Evidence that software meets 21 CFR 820.30(c) and Part 11 electronic record controls, if electronic records are used for device operation or logging. | Source [2] references 21 CFR Part 11 as a related regulation. |
| **QMSR‑Specific Records** | • SOPs for record creation, review, approval, distribution, retention (≥10 years per §820.180).<br>• Controlled forms (e.g., **F‑QMSR‑REC‑001**) demonstrating compliance with the “additional requirements” of §820.35.<br>• Documentation of how ISO 13485 §4.2.5 records map to FDA‑required elements. | Directly derived from source [1] & [2]. |
| **Risk Management File** | ISO 14971 risk analysis, mitigation plan, and residual risk evaluation linked to record‑control procedures. | – |

---

### 3. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Recommended Action |
|-----|----------------------|--------------------|
| **Absence of QMSR‑specific SOPs** (record creation, review, retention) | Non‑conformance to §820.35 → FDA may issue Form 483 or require additional information. | Draft and implement SOPs; populate using template **F‑QMSR‑REC‑001** from source [2]. |
| **No documented mapping of ISO 13485 §4.2.5 records to FDA §820.35** | Incomplete demonstration of “additional” requirements beyond the baseline ISO standard. | Create a cross‑walk matrix (ISO record → FDA required element). |
| **Electronic record controls not addressed** (Part 11) | If DHR/DMR are electronic, lack of Part 111 compliance is a regulatory deficiency. | Conduct Part 11 validation; include audit trail, access control, and data integrity evidence. |
| **UDI implementation plan missing** | Required by 21 CFR 830 for Class II devices. | Develop UDI labeling, database submission to GUDID, and SOPs for UDI assignment/maintenance. |
| **Risk management file not linked to record‑control** | Weak justification that records support traceability of risk mitigations. | Update ISO 14971 file to reference specific QMSR records (e.g., design verification reports). |
| **No identified predicate device** | Cannot complete 510(k) without a clear predicate. | Search FDA 510(k) database; select the most appropriate device and document its K‑number(s). |

---

### 4. Risk Controls Related to Records Management  

1. **Traceability Control** – Ensure every design input, verification/validation result, and risk mitigation is traceable through controlled records (DHF → DMR).  
2. **Data Integrity Assurance** – Apply Part 11 controls: electronic signatures, audit trails, periodic data integrity checks.  
3. **Retention & Availability** – Retain all required records for ≥10 years (or the life of the device, whichever is longer) and ensure they are readily accessible for FDA inspection.  
4. **Change Management** – Formal change‑control process that updates both ISO 13485 records and QMSR‑specific documentation simultaneously.  
5. **Audit & Review** – Quarterly internal audits of record‑control procedures; corrective actions documented in CAPA system.  

---

### 5. Citations (as required by the source)  

| Source | Key Point Cited |
|--------|-----------------|
| **Chunk 100539693362657837** | “21 CFR Part 820 transitioned to QMSR on 2026‑02‑02; ISO 13485 §4.2.5 is a **basic requirement**, but FDA §820.35 imposes **additional** requirements.” |
| **Chunk 195154780902741471** | Provides the “FDA QMSR ↔ ISO 13485 diff table” and references forms such as **F‑QMSR‑REC‑001**; lists related regulations (21 CFR 803, 830, Part 11, UDI). |
| **Predicate identifiers** | *no specific identifier found in source — verify separately* |

---

### 6. Human‑Escalation Triggers  

| Situation | When to Escalate to Senior RA / Management |
|-----------|--------------------------------------------|
| **Absence of a validated predicate device** – submission cannot proceed until identified. |
| **Failure to produce QMSR‑specific SOPs or record‑control evidence** after 2 weeks of effort. |
| **Part 11 gaps uncovered during electronic DHR/DMR audit** (e.g., missing audit trail). |
| **UDI integration plan not finalized 30 days before filing**. |
| **Significant residual risk remains unmitigated in the ISO 14971 file** linked to inadequate records. |
| **Regulatory authority feedback indicating non‑conformance to §820.35** during pre‑submission meeting or review. |

---

### 7. Peer Review Prompt  

> **Request:** Please review this draft for (a) completeness of QMSR vs ISO 13485 coverage, (b) adequacy of the identified evidence list, and (c) any jurisdictional gaps (e.g., state radiation safety regulations, CMS requirements) that have been omitted. Challenge assumptions about the predicate selection process and suggest additional sources or templates that could strengthen our record‑control justification.

---

### 8. Reusable RA Judgment (Memory Record)  

```json
{
  "honcho_conclude": {
    "lesson_key": "QMSR_vs_ISO13485_records",
    "summary": "For US medical devices, ISO 13485 §4.2.5 satisfies the baseline record‑management requirement but is **insufficient** alone after the QMSR transition (21 CFR 820.35). A compliant submission must provide a cross‑walk to FDA’s additional requirements, implement SOPs/forms (e.g., F‑QMSR‑REC‑001), and address Part 11, UDI, and retention rules. Missing any of these elements is a likely cause for FDA Form 483 or delay.",
    "actions": [
      "Create QMSR‑specific record control SOPs referencing the diff table (source [2]).",
      "Map ISO 13485 records to §820.35 requirements.",
      "Validate electronic records per Part 11 before filing.",
      "Identify and document a Class II X‑ray predicate device (K number)."
    ],
    "confidence": 0.93,
    "source_refs": ["100539693362657837", "195154780902741471"]
  }
}
```

---  

*Prepared by Mike – US FDA Regulatory Affairs Specialist.*

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

## ra_eu

### kb-eval-20260717-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b66b7c0dd94542fb", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b66b7c0dd94542fb`
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

---

### 1. Product Overview & Classification  

| Product | Intended Use (summary) | MDR classification* | Annex VIII rule(s) applied |
|---------|------------------------|---------------------|-----------------------------|
| **X‑ray Detector** | Detects ionising radiation and converts it into a digital image for diagnostic radiology | Class IIa | Rule 10 (active device for the purpose of diagnosis) – confirmed by the manufacturer’s internal mapping. |
| **Handheld X‑ray Source** | Portable source that emits therapeutic/diagnostic ionising radiation | Class IIb | Rule 9 (active therapeutic device or active device controlling a therapeutic function). |
| **GUI Software (SaMD)** | Visualises, processes and annotates image data from the detector; provides decision support to the user | Class IIa | Rule 11 (software that drives or influences the performance of a medical device) – SaMD classification as per MDCG guidance. |

\*Classification is based on the mapping indicated in source excerpt [1] and verified against **Annex VIII** of MDR 2017/745.

---

### 2. Conformity‑Assessment Route  

All three devices are **Class IIa / IIb** → require a **Notified Body (NB)** assessment under **Annex IX** (quality‑management‑system based conformity assessment). No type‑examination (Annex X/XI) is needed unless the NB specifically requires it for certain high‑risk aspects.

> **Citation:** MDR Art. 52(2) + Annex IX (QMS‑based route).

---

### 3. Required Evidence Packages (Technical Documentation)

| Evidence | X‑ray Detector | Handheld Source | GUI Software |
|----------|----------------|-----------------|--------------|
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | ✓ (must include state‑of‑the‑art literature, clinical data, risk‑benefit analysis) | ✓ | ✓ |
| **Risk Management File (RMF)** – ISO 14971 + MDR Art. 10(9) | ✓ (includes DQE degradation & pixel defect controls) | ✓ (dose‑overrun, mechanical failure, battery health) | ✓ (software error, usability, cybersecurity) |
| **IEC Test Data** | IEC 62220‑1‑1 performance data (DQE, linearity) | IEC 60601‑2‑XX (radiation safety testing) | IEC 62304 lifecycle records + bug logs |
| **Post‑Market Surveillance Plan (PMS‑Plan)** – Art. 84 | ✓ (see §3) | ✓ | ✓ |
| **Periodic Safety Update Report (PSUR)** – Art. 85/86 | 2‑year cycle (Class IIa) | 1‑year cycle (Class IIb) | 2‑year cycle (Class IIa) |
| **Post‑Market Clinical Follow‑up Plan & Report** – Annex XIV Part B | Determined after equivalence claim review (see §4) | Mandatory clinical data collection on ionising radiation exposure | Mandatory error‑data capture during routine use |

All evidence must be uploaded to **EUDAMED** (UDI registration + Vigilance reporting) as indicated in source excerpt [1].

---

### 4. PMS System – Core Elements (Art. 83 & Art. 84)

| Element | Description | Frequency (as per source) |
|---------|--------------|---------------------------|
| **Data Sources** (see source [2]) | - Serious incidents / PSURs (vigilance, EUDAMED)  <br> - Non‑serious incidents & side‑effects (complaint system)  <br> - Trend reporting (internal statistics)  <br> - Scientific literature & registries (PubMed, IEC/ISO DB, MAUDE)  <br> - User/importer feedback (CRM)  <br> - Competitor public data | Immediate / Quarterly for serious incidents; Monthly for complaints & user feedback; Quarterly for trends; Semi‑annual for literature and competitor data. |
| **PMS Activities** | • Monitoring of DQE, pixel defect rates (Detector) <br>• Dose‑overrun and mechanical integrity checks (Handheld source) <br>• Software error logs, usability issue tracking (GUI) | Aligned with the above collection frequencies. |
| **Evaluation & Trend Analysis** | Apply statistical tools to detect upward trends in: • Patient dose exceedance • Device performance degradation • Software malfunction rates | Quarterly review; escalation if trend exceeds pre‑defined limits (see §6). |
| **Corrective/Preventive Actions (CAPA)** | Defined per RMF; linked to identified non‑conformities; documented in PMS‑Report & fed into next design iteration. | Within 30 days of detection for serious findings; 90 days for non‑serious trends. |

> **Citation:** MDR Art. 83 (PMS system) & Art. 84 (PMS plan).

---

### 5. PMCF Planning (Annex XIV Part B)

| Product | Need for PMCF | Planned Clinical Evidence | Key Activities |
|---------|----------------|--------------------------|----------------|
| **X‑ray Detector** | *Conditional* – decision after equivalence claim review (source [1]) | • Limited prospective clinical study to confirm DQE stability over the device life‑cycle. <br>• Retrospective registry analysis of image quality outcomes. | • Define primary endpoint: ≥ 95 % images meet ISO‑defined DQE threshold. <br>• Enrol 30 sites, 200 examinations total within 12 months. |
| **Handheld X‑ray Source** | **Required** – ionising radiation => “clinical data actively collected” (source [1]) | • Prospective dose‑monitoring study comparing measured patient skin dose against predefined limits. <br>• Human factors assessment on handling safety. | • Deploy built‑in dosimeter; collect per‑procedure dose data for 500 procedures across 10 institutions. |
| **GUI Software** (SaMD) | **Mandatory** – “error data collection during use” (source [1]) | • Real‑world usage analytics (error logs, crash reports). <br>• Usability testing with end‑users (clinicians, technologists). | • Implement automatic logging of all software exceptions; quarterly aggregation for trend analysis. |
| **Common PMCF Deliverables** | • PMCF Plan (objectives, methodology, timelines) – Annex XIV Part B. <br>• PMCF Evaluation Report (conclusions, impact on risk‑benefit) – Annex XIV Part B. | • Integration of findings into updated CER & RMF. | • Updated documentation submitted to NB as part of periodic conformity renewal. |

> **Citation:** MDR Annex XIV Part B (PMCF plan & evaluation report).

---

### 6. Identified Gaps / Missing Information  

| Gap | Impact on Compliance | Required Action |
|-----|----------------------|-----------------|
| **Equivalence claim justification** for X‑ray Detector – only “review after equivalence” is mentioned; no supporting data set identified. | Prevents final decision on PMCF necessity and may affect classification verification. | Provide detailed comparison matrix (specifications, performance, clinical data) vs predicate device(s). |
| **Specific performance objectives & acceptance criteria** for each PMS metric (e.g., DQE degradation threshold, dose‑overrun limit). | Cannot close CAPA loops or trigger trend alerts reliably. | Define quantitative limits in the PMS‑Plan and embed into monitoring software. |
| **PMCF study protocols** (sample size calculations, statistical analysis plan) are missing for Handheld Source & X‑ray Detector. | NB will request detailed protocol before approval of PMCF evidence. | Draft full clinical investigation plans; obtain ethics approvals where required. |
| **Cybersecurity risk controls** for GUI Software – only “error data collection” is noted; no mention of threat analysis, patch management. | May be non‑conformant with Art. 10(9) (risk management). | Conduct ISO 14971‑aligned cybersecurity risk assessment; document mitigation measures. |
| **EUDAMED data fields** – UDI registration confirmed, but vigilance reporting workflow not fully described. | Incomplete post‑market vigilance could breach Art. 87/88 obligations. | Map internal incident handling to EUDAMED vigilance modules; assign responsible person. |

---

### 7. Risk Controls Linked to PMS / PMCF  

| Hazard | Control (pre‑market) | Post‑Market Surveillance Confirmation |
|--------|----------------------|---------------------------------------|
| **DQE degradation** (X‑ray Detector) | IEC 62220‑1‑1 testing; built‑in performance self‑check. | Quarterly DQE trend analysis; trigger alarm if > 10 % drop vs baseline. |
| **Patient dose exceedance** (Handheld Source) | Integrated dosimeter with hard stop; pre‑programmed exposure limits. | Real‑time dose logging to PMS database; immediate reporting if limit exceeded. |
| **Battery failure / overheating** (Handheld Source) | Battery management system, thermal cut‑off. | Monthly battery health metrics; trend analysis for early wear detection. |
| **Software crash / incorrect image rendering** (GUI) | IEC 62304 development lifecycle, unit/integration testing. | Automatic error log upload; monthly aggregation of crash frequency; root‑cause CAPA. |
| **Usability errors leading to misinterpretation** (All) | Human factors validation during design verification. | Post‑market usability feedback via CRM & complaints; periodic usability re‑evaluation (PMCF). |

All controls must be reflected in the **Risk Management File**, updated after each PMS/PMCF cycle per MDR Art. 10(9).

---

### 8. Human‑Escalation Triggers  

| Trigger | Why it matters | Who should act & timeframe |
|---------|----------------|----------------------------|
| **PSUR not submitted on schedule** (2 yr for Class IIa, 1 yr for IIb) | Regulatory non‑conformance → potential market suspension. | RA Lead – raise to Management within 5 working days of missed deadline; initiate corrective plan. |
| **Trend analysis shows > 15 % increase in dose‑overrun incidents** (Handheld Source) | Indicates possible design or usage issue affecting patient safety. | Clinical Safety Officer – immediate investigation, report to NB within 10 days, implement interim mitigation. |
| **Software error rate exceeds predefined threshold (e.g., > 0.5 % of sessions)** | Could affect diagnostic decisions → breach of risk‑benefit balance. | Software QA Lead – issue hot‑fix, update IEC 62304 records, notify vigilance team. |
| **Equivalence claim for X‑ray Detector cannot be substantiated** | Classification/PMCF decision uncertain; may require re‑classification. | RA Manager – convene cross‑functional review, possibly submit new classification justification to NB. |
| **Significant adverse trend in literature (new safety signal)** | External evidence may change state‑of‑the‑art. | Medical Affairs – conduct rapid literature review, update CER and RMF accordingly. |

---

### 9. Summary of Deliverables for the Next Cycle  

1. **Finalize PMS Plan** (Art. 84) – include detailed metrics, thresholds, responsible persons.  
2. **Complete PMCF Plans & Protocols** (Annex XIV Part B) for all three devices; obtain ethics approvals where required.  
3. **Update CERs** (Annex XIV Part A) with latest literature and clinical data (including PMCF outcomes).  
4. **Refresh Risk Management Files** – integrate PMS findings, new risk controls, and cybersecurity assessment for the GUI.  
5. **Prepare PSURs** – schedule according to product class; ensure data completeness before submission to NB/EUDAMED.  

All above tasks must be logged in the internal quality‑management system and tracked against the **EUDAMED** vigilance module.

---

### 10. Peer‑Review Prompt  

> *Colleagues, please review this draft focusing on:*  
> 1. **Assumptions about classification** – are Rule 9/10/11 correctly applied given the limited product description?  
> 2. **Source coverage** – does the mapping of data sources (serious incidents, complaints, literature, competitor data) fully reflect the excerpts provided, or are any required sources missing?  
> 3. **Jurisdictional gaps** – have we captured all MDR‑specific obligations (e.g., Art. 90 for vigilance, coordination with national Competent Authorities) that might affect PMS/PMCF in the EU context?  

Your feedback will be used to close any remaining evidence gaps before submission to the Notified Body.

---

### 11. Identifier Availability  

*No specific regulatory identifiers (e.g., 510(k) numbers, predicate device references, EUDAMED registration IDs) appear verbatim in the source excerpts provided.* Verify such identifiers separately and insert them where required in final documentation.

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

### kb-eval-20260717-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e0a28ad294f2e438", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e0a28ad294f2e438`
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

> **Regulatory Draft – Classification, Conformity‑Assessment Route & Post‑Market Surveillance (PMS) / Post‑Market Clinical Follow‑up (PMCF) Planning**

---

## 1. Device Scope – Information Gaps (to be supplied by the project team)

| Required element | Why it is needed | Current status |
|------------------|-----------------|----------------|
| **Intended purpose / indication** | Drives classification (Art. 51 + Annex VIII) and determines clinical‑evaluation scope (Annex XIV Part A). | *Missing – request detailed IFU/label wording.* |
| **Device description & technology type** (e.g., active therapeutic, diagnostic, software, accessory) | Determines which rule(s) of Annex VIII apply; influences whether a “device for recording images” (Rule 17) or “active therapeutic device” (Rule 9) is appropriate. | *Missing – request design dossier.* |
| **Risk classification** (class I, Is, Im, IIa, IIb, III) | Determines required conformity‑assessment route (Annex IX, X, XI) and whether a PMS plan alone (Art. 83‑86) or a full PSUR (Art. 86) is mandatory. | *Missing – to be derived after rule analysis.* |
| **Manufacturer‑controlled QMS** (ISO 14971, ISO 13485 status) | Required for Annex IX route and for integrating risk‑management outputs into PMS/PMCF. | *Missing – confirm certificate validity.* |
| **Clinical data already available** (clinical literature, pre‑market clinical investigation, post‑market data) | Needed to populate the Clinical Evaluation Report (CER) (Annex XIV Part A) and to decide PMCF scope (Annex XIV Part B). | *Missing – request summary of existing evidence.* |
| **Intended EU market(s)** (EU Member State, intended UDI system) | Determines need for UDI registration in EUDAMED (Art. 33‑39) and the applicable import/authorized‑representative arrangements (Art. 11). | *Partial – source mentions “Authorized Rep.” but no device‑specific details.* |
| **Existing US regulatory status** (510(k) exemption, FDA registration) | Helpful for cross‑border reference but not a prerequisite for EU MDR compliance. | Source lists “US Agent (510(k) 면제 외)” but no identifier; **no specific identifier found in source — verify separately**. |

> **Action:** The project lead must provide the missing items before any classification decision can be finalised.

---

## 2. Preliminary Classification Pathway (Art 51 + Annex VIII)

1. **Apply rules sequentially (Annex VIII, 22 rules).**  
   - Start with Rule 1 and proceed until a rule matches; apply the highest class resulting from any matching rule.  
   - If uncertainty remains after rule‑by‑rule analysis, consult the **Competent Authority (CA)** or the MDCG “Manual on Borderline and Classification” (latest version v2.1.1, 2023‑09) – as indicated in source excerpt [2].

2. **Key decision points to capture from missing information:**
   - Does the device **administer/transfer energy**? → Rule 9 (active therapeutic) or Rule 10 (active diagnostic).  
   - Is it a **radiological imaging recorder**? → Rule 17 may apply.  
   – Is it an **invasive instrument** without active components? → Rules 2‑5 could be relevant.  

> **Outcome Expectation:**  
- **Class I (non‑sterile, non‑measuring)** → Self‑declaration; minimal PMS (Art. 83) and no NB involvement.  
- **Class Is / Im** → Requires a QMS audit under **Annex IX** (module B).  
- **Classes IIa/IIb/III** → Require **NB‑based conformity assessment** (Annex IX + possible Annex X/ XI modules, depending on whether the device is a “product of a special nature” or requires type‑examination).  

---

## 3. Conformity‑Assessment Route & Required Evidence

| Classification | Core MDR Pathway | Mandatory Deliverables |
|----------------|------------------|------------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration; Annex IV EC Declaration of Conformity | • Technical Documentation (Annex II)  <br>• Risk Management File (ISO 14971)  <br>• Clinical Evaluation Report – **Annex XIV Part A** (Art. 61) |
| **Class Is / Im** | **Annex IX** (QMS audit, Module B) + EC Declaration of Conformity | • All items above plus:  <br>• QMS certificate (ISO 13485)  <br>• PMS System (Art. 83)  <br>• Periodic Safety Update Report **only if class Is/Im and higher‑risk** (Art. 86 applies to IIb/III; for Is/Im a PMCF summary suffices). |
| **Class IIa / IIb / III** | **Annex IX** + *if applicable* Annex X (type‑examination) and/or Annex XI (product verification) – depending on “special nature” or “critical” device status. | • All of the above, plus:  <br>• NB‑issued CE certificate  <br>• **PMCF Plan & PMCF Evaluation Report** – **Annex XIV Part B**  <br>• PSUR (Art. 86) for IIb/III classes  <br>• UDI registration in EUDAMED (Art. 33‑39). |

### Clinical Evidence Requirements (Annex XIV Part A)

1. **Clinical Evaluation Report (CER)** – must address:
   - State‑of‑the‑art literature review (systematic search, inclusion/exclusion criteria).  
   - Clinical data from pre‑market investigations, if any.  
   - Post‑market clinical follow‑up data (if device already on market).  

2. **PMCF Plan (Annex XIV Part B)** – outlines:
   - Objectives & endpoints aligned with residual risks identified in the risk‑management file.  
   - Methods (e.g., registries, continued investigations, literature monitoring).  
   - Schedule and responsibilities.  

3. **Evidence Gap Management** – any missing clinical data must be addressed through a *post‑market clinical investigation* (Art. 78‑80) or additional PMCF activities before final CE marking.

### Post‑Market Surveillance System

- **PMS Plan** – Art. 83. Must be documented, proportionate to risk class, and integrated with the QMS.
- **Periodic Safety Update Report (PSUR)** – Art. 86 for Class IIb/III devices; includes cumulative safety data, trend analysis, and PMS outcomes.
- **Vigilance Reporting** – Art. 87 (serious incidents) plus national reporting obligations (e.g., Korean “이상사례 보고” referenced in source [1]).

---

## 4. Risk Controls & Integration with PMS/PMCF

| Control | Where it appears | How it ties to post‑market activities |
|---------|-----------------|---------------------------------------|
| **Risk Management File** (ISO 14971) | Annex I General Safety & Performance Requirements; mandatory for all devices. | Provides the baseline risk register that drives PMS metrics and PMCF objectives. |
| **Usability Engineering / Human Factors** | Annex I‑§21 (usability). | Should be validated pre‑market; post‑market usability data feed back into risk reduction actions. |
| **Software Lifecycle Processes** (if applicable) | IEC 62304 referenced in Annex I‑§23. | Updates captured via PMS change‑control and PMCF monitoring of software performance. |
| **Labeling & IFU Controls** | Annex I‑§23 (labeling). | Changes triggered by post‑market findings must be reflected in updated UDI labels (UDI portal noted in source [1]). |

---

## 5. Human‑Escalation Triggers

| Trigger condition | Required action |
|-------------------|-----------------|
| **Classification ambiguity** after rule‑by‑rule analysis or borderline device – e.g., possible Rule 9 vs Rule 17 application. | Escalate to senior regulatory lead and/or request formal classification advice from the Competent Authority (CA) per source [2]. |
| **Insufficient clinical evidence** to satisfy Annex XIV Part A (no adequate literature or post‑market data). | Initiate a dedicated Clinical Investigation (Art. 78‑80) or expand PMCF plan; pause CE marking submission until gap closed. |
| **PMS system not fully defined** (missing procedures for trend analysis, vigilance handling, or PSUR generation). | Convene cross‑functional PMS working group; issue interim SOPs and schedule external audit of PMS before NB audit. |
| **QMS certification expired or not yet obtained** for Class Is/Im or higher. | Suspend conformity‑assessment activities until ISO 13485 renewal is confirmed. |
| **UDI registration incomplete** (no entry in EUDAMED, missing GUDID mapping). | Submit UDI data via the EUDAMED portal; verify against national UDI system (Korean “UDI 포털” cited in source [1]). |
| **NB contract budget not secured** (cost ranges shown in source [1] – €10‑100 k+). | Obtain finance approval or consider alternative NB; flag to project management. |

---

## 6. Summary of Immediate Next Steps

1. **Collect missing device‑specific information** (intended use, technology type, risk classification basis).  
2. **Perform rule‑by‑rule classification** using Annex VIII (apply highest‑class rule). Document the reasoning and any CA consultation needed.  
3. **Draft the initial Technical Documentation outline**, incorporating placeholders for CER, PMCF plan, PMS system, and UDI registration.  
4. **Validate QMS status** (ISO 13485) and schedule NB audit timeline according to the eventual class.  
5. **Map out a provisional PMCF study design** aligned with residual risks identified in the risk‑management file.  

---

## 7. Peer Review Prompt

*Please review the assumptions and coverage below:*

- **Assumption:** The classification can be determined solely from the intended purpose and technology type once supplied. Are there any product‑specific nuances (e.g., “accessories for a class III device”) that could elevate the classification independently?  
- **Source Coverage:** The excerpts provide only high‑level references to MDR articles/annexes, UDI portals, and classification guidance. Is additional guidance needed from MDCG documents (e.g., Guidance 2023‑01 on borderline devices) or national competent authority templates?  
- **Jurisdiction Gaps:** While the Korean “이상사례 보고” and US Agent notes appear, we have not addressed potential requirements for simultaneous FDA 510(k) clearance if the device is marketed in the USA. Should a cross‑reference strategy be added to anticipate future global submissions?

*Kindly challenge any gaps or propose refinements.*

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

### kb-eval-20260717-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c944e4d14fb0a40a", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c944e4d14fb0a40a`
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
*Prepared for internal review – MDR 2017/745 compliance assessment*  

---

## 1. Device Portfolio Overview  

| # | Product | Tentative MDR classification* | Required PMS Report type | PMCF method (source) |
|---|---------|-----------------------------|--------------------------|----------------------|
| 1 | **X‑ray Detector** (hardware) | Class IIa/IIb (active therapeutic) | PSUR **annual** / **2‑year** cycle (Art. 86 for higher‑risk) | Usability evaluation (IEC 62366) + real‑world error data collection |
| 2 | **Handheld X‑ray Source** (hardware) | Class IIb (active therapeutic) | PSUR **annual** (Art. 86) | Same as #1 |
| 3 | **Imaging Suite GUI Software (SaMD)** | Class IIa – MDR § 22 (software) | PSUR **2‑year** cycle (Art. 85, lower‑risk) | Usability evaluation (IEC 62366) + real‑world error data collection |

\*Classification is based on the “MDR 등급 (추정)” column in source [2]. Formal classification must be confirmed by applying the relevant **Annex VIII** rules (Rule 9 for active therapeutic devices, Rule 11/12 for SaMD).  

---

## 2. Submission & Conformity‑Assessment Route  

| Device | MDR Annex(es) applicable | NB involvement required? |
|--------|--------------------------|---------------------------|
| X‑ray Detector – Class IIa/IIb | **Annex IX** (QMS‑based assessment) *or* **Annex X+XI** (type‑examination + product verification) – whichever the NB selects. | **Yes** – a Notified Body must audit the QMS and issue the CE certificate. |
| Handheld X‑ray Source – Class IIb | Same as above (Annex IX or Annex X+XI). | **Yes** |
| SaMD – Class IIa | **Annex IX** (full quality‑management system) is typical for Class IIa software. | **Yes** |

> **Citation:** Conformity‑assessment routes are defined in MDR **Annex IX** (QMS‑based) and **Annex X/ XI** (type‑examination + product verification).  

---

## 3. Evidence Package Required for CE Marking  

| Evidence | What it must contain | Relevant MDR reference |
|----------|---------------------|------------------------|
| **Technical Documentation** (including device description, intended purpose, labeling) | Complete device tree, UDI, risk classification rationale, applicable standards list | **Annex II** (general format) |
| **Risk Management File** | ISO 14971‑based analysis, risk control measures for SW errors, data loss, cyber‑security threats | **Annex I**, § 10 (risk management) |
| **Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical performance data, benefit–risk analysis. Must be aligned with **Annex XIV Part A** (updated via Art. 61). | **Annex XIV Part A** |
| **PMCF Plan & Evaluation Report** | Defined objectives, data sources (bug reports, CVE/NIST NVD), usability testing (IEC 62366), schedule, endpoints; final evaluation demonstrating continued conformity. | **Annex XIV Part B** |
| **PMS Plan** | System for systematic collection & analysis of post‑market data, including PSUR preparation. Must meet **Art. 84**. | **Art. 84** |
| **Periodic Safety Update Report (PSUR)** | For Class IIb devices – annual report; for Class IIa – every 2 years. Content: trend analysis, PMS results, PMCF outcomes, risk‑benefit updates. | **Art. 86** (higher‑risk) / **Art. 85** (lower‑risk) |
| **Software Development & Cybersecurity Documentation** | IEC 62304 compliance, security lifecycle per MDCG 2021‑6, evidence of vulnerability monitoring (CVE/NIST NVD). | **MDCG 2019‑16 Rev.1**, **MDCG 2021‑6**; link to MDR via Annex I requirements for safety and performance. |

---

## 4. Identified Information Gaps  

| Gap | Why it matters | How to close |
|-----|----------------|--------------|
| **Exact Intended Medical Purpose & Indications** (e.g., diagnostic vs therapeutic use) | Determines the correct *Annex VIII* rule and classification; influences clinical data requirements. | Obtain a finalized “Intended Use Statement” from product management; map to MDR rules. |
| **Clinical Data for X‑ray Detector / Handheld Source** (performance, accuracy, radiation dose) | Needed for CER (Annex XIV Part A) and PMCF baseline. | Conduct/collect clinical investigations or compile existing data from FDA 522 filings if applicable under EU equivalence justification. |
| **Software Architecture & Update Mechanism** | Required for IEC 62304‑based risk management, cyber‑security controls, and PMCF data capture (error logs). | Provide a detailed software design dossier; include versioning/patch process. |
| **Cyber‑Security Vulnerability Monitoring Plan** (frequency of CVE checks, response timelines) | Directly feeds PMS & PMCF risk mitigation for identified “major risk signals” (SW error, data loss). | Define SOPs referencing MDCG 2021‑6; integrate into PMS plan (Art. 84). |
| **Translation of Korean MFDS Requirements** (digital medical product law 2024) | May affect market launch timeline in Korea and EU‐Korea mutual recognition discussions. | Clarify applicability; if required, align MFDS post‑market obligations with EU PMS/PMCF to avoid duplicate efforts. |
| **Usability Test Protocols & Acceptance Criteria** (IEC 62366) | Supports PMCF evidence that the GUI does not introduce use errors leading to misdiagnosis. | Draft protocol, recruit representative user group, document findings. |

---

## 5. Risk‑Control Measures (pre‑market & post‑market)

| Hazard | Pre‑market control | Post‑market surveillance / PMCF |
|--------|-------------------|---------------------------------|
| **Software error → diagnostic misinterpretation** | IEC 62304 development lifecycle, verification/validation per IEC 82304‑1, usability testing (IEC 62366). | Continuous collection of bug reports; trend analysis in PSUR; periodic re‑evaluation via PMCF. |
| **Data loss / integrity breach** | Secure data storage architecture, redundancy, encryption, audit logs. | Monitor CVE/NIST NVD feeds; implement security patches; record incidents in PMS database. |
| **Cyber‑security vulnerability (unauthorised access)** | Threat modelling (MDCG 2021‑6), secure boot, network segmentation. | Real‑time vulnerability scanning; incident response SOPs; annual security review incorporated into PSUR. |
| **Radiation over‑exposure (handheld source)** | Built‑in dose limiting firmware, hardware interlocks, user training. | Capture dose metrics in field use logs; analyse trends for out‑liers; update PMCF objectives accordingly. |

All controls must be documented in the **Risk Management File** and reflected in the **PMS Plan** (Art 84).  

---

## 6. Human‑Escalation Triggers  

| Trigger | Action Required | Responsible Party |
|---------|-----------------|--------------------|
| **Missing intended‑use statement or ambiguous indication** | Pause CE‑marking dossier finalisation; request clarification from product owner. | Regulatory Affairs Lead |
| **Absence of clinical performance data for X‑ray hardware** | Initiate a supplementary clinical investigation or gather real‑world evidence before CER sign‑off. | Clinical Evaluation Team |
| **No documented cyber‑security monitoring SOP** | Draft and approve SOP; link to PMS database; update PMCF plan. | IT Security / QA |
| **PSUR schedule not aligned with device risk class (e.g., annual for Class IIa)** | Re‑schedule PSUR per Art 85/86; inform NB of revised timeline. | Post‑Market Surveillance Manager |
| **Unresolved Korean MFDS applicability** | Conduct regulatory gap analysis; decide whether dual PMS programmes are needed. | International Regulatory Coordinator |
| **PMCF data collection not yet operational (no bug‑report pipeline)** | Deploy issue‑tracking system; train field service teams to log events. | Clinical Support / PMCF Lead |

When any trigger is hit, the responsible party must **escalate to the RA manager** and document the decision in the project risk register before proceeding.

---

## 7. Peer‑Review Prompt  

> *“Colleague, please review the assumptions and coverage in this draft:  
> - Are the tentative MDR classifications (Class IIa/IIb) justified given the available product descriptions?  
> - Does the evidence matrix include all mandatory items for a CE marking under MDR, especially regarding clinical evaluation and cybersecurity?  
> - Have we accounted for any jurisdiction‑specific gaps (e.g., Korean MFDS obligations) that could impact our EU submission timeline?  
> – Suggest additional sources or standards that should be referenced.”*  

---

## 8. Reusable RA Judgment (Lesson Log)

**Judgment ID:** `RA_JNL_20260717_PMS_PM_CF`  

**Key Take‑away:**  
When drafting PMS/PMCF plans for mixed hardware‑software radiology products under MDR, always:

1. **Confirm classification against Annex VIII rules before assigning submission routes.**  
2. **Map each identified risk signal to a concrete post‑market control (e.g., CVE monitoring → Art 84 PMS plan, cybersecurity SOP).**  
3. **Catalogue required evidence per the exact MDR references: CER (Annex XIV Part A), PMCF (Annex XIV Part B), PMS Plan (Art 84), PSUR (Art 85/86).**  
4. **Flag any non‑EU regulatory touchpoints (e.g., MFDS) as separate gaps; do not assume they satisfy EU obligations.**  

*Log recorded via `honcho_conclude` for future reuse.*

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

### kb-eval-20260717-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "a7f9cbb5e3a5a13e", "source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md", "source_hash": "62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a7f9cbb5e3a5a13e`
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

> **Regulatory Draft – PMS & PMCF Planning (EU MDR 2017/745)**  

---

### 1. Device Classification & Conformity‑Assessment Route  
| Item | Assessment (what must be confirmed) |
|------|--------------------------------------|
| **Intended medical purpose / indications** | Must be obtained from the manufacturer – defines whether the device is a ***medical* device** or falls under Annex XVI (no intended medical purpose). |
| **Risk‑class determination** | Apply MDR Annex VIII classification rules (e.g., Rule 9, 10, 17 etc.) based on invasiveness, duration of use & energy. *Classification cannot be finalised until the intended use is known.* |
| **Conformity‑assessment route** | • **Class I (non‑sterile, non‑measuring)** – self‑declaration (Annex IV) → EUDAMED registration only.  <br>• **Class IIa/IIb/III** – **Annex IX** (QMS‑based route) *or* **Annex X + XI** (type‑examination & product verification) depending on the presence of a “hazardous” constituent or higher risk. The exact module (A, B, … G) must be chosen after classification is confirmed. |

> **Citation:** Classification rules are in MDR Annex VIII (see reference table). Conformity‑assessment routes are defined in MDR Annex IX and Annex X/XI (do not mix with NLF module lettering).

---

### 2. Required Evidence for PMS & PMCF  

| Evidence | Regulatory source | What must be supplied |
|----------|-------------------|-----------------------|
| **UDI registration data** (UDI‑DI, UDI‑PI, issuing agency) | MDR – EUDAMED Module 2 (UDI/DEV) – see source excerpt **[2]** | • Basic UDI‑DI (globally unique)<br>• Device model‑specific UDI‑DI<br>• Production identifier (UDI‑PI)<br>• Issuing agency (GS1, HIBCC or ICCBBA) |
| **PMS System description** | Art. 83 MDR (system) | • Description of the PMS process, responsibilities, data sources, and post‑market reporting mechanisms |
| **PMS Plan** | Art. 84 MDR | • Schedule of routine activities (e.g., trend analysis, vigilance handling)<br>• Defined “trigger” levels for corrective actions |
| **Periodic Safety Update Report (PSUR)** – required for Class IIb & III | Art. 86 MDR (higher‑risk) | • Summarised safety and performance data covering the previous reporting period |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | Annex XIV Part B MDR | • Study design, endpoints, sample size, follow‑up schedule, statistical methods<br>• Link to identified residual risks from the risk‑management file |
| **PMCF Evaluation Report** | Annex XIV Part B MDR | • Results of PMCF activities, analysis against benefit‑risk conclusions, updates to Clinical Evaluation Report (CER) |
| **Clinical Evaluation Report (CER)** – baseline & updated | Annex XIV Part A MDR (updated via Art. 61) | • State‑of‑the‑Art literature review<br>• Clinical data (pre‑market + PMCF)<br>• Benefit‑risk determination |
| **Risk Management File** (including risk controls and residual risk evaluation) | Annex I (GSPR) – implemented per ISO 14971 | • Hazard identification, risk analysis, mitigations, verification of effectiveness, benefit‑risk conclusion |

---

### 3. Gaps / Missing Information (to be obtained before submission)

| Missing Item | Why it is needed | Where to capture it |
|--------------|-----------------|----------------------|
| **Exact intended purpose & indications** | Drives classification, clinical evaluation scope and PMCF objectives | Technical Documentation – “Intended Purpose” section |
| **Device description (materials, energy source, accessories)** | Required for UDI‑DI definition & risk analysis | Labeling & Device Description Annex |
| **Classification rule(s) applied** | Determines conformity‑assessment route & mandatory post‑market deliverables (e.g., PSUR) | MDR Annex VIII – Classification justification |
| **Manufacturer’s QMS certificate (if Class IIa/IIb/III)** | Needed for Annex IX route (or for type‑examination) | Quality Management System documentation |
| **Clinical data sources (pre‑market studies, literature, registries)** | Basis of CER & PMCF plan | Clinical Evaluation Report (Annex XIV Part A) |
> **Citation:** The source excerpts only cover EUDAMED UDI registration ([2]) and a high‑level DB comparison ([1]); they do not contain device‑specific identifiers or classification details. *“no specific identifier found in source — verify separately.”*

---

### 4. Core Risk Controls (to be reflected in the Technical Documentation)

1. **Risk Management Process** – ISO 14971 compliant, covering: hazard identification, risk analysis, evaluation of acceptability, implementation of control measures, verification of controls, and post‑market benefit‑risk assessment.  
2. **Labeling & Instructions for Use (IFU)** – Conform to Annex I §23 (labeling requirements) ensuring that any residual risks are clearly communicated to the user.  
3. **PMS Monitoring** – Continuous collection of field performance data, adverse events, and trend analysis as defined in Art. 84.  
4. **PMCF Activities** – Targeted follow‑up on identified residual risks; results feed back into risk management updates (Art. 61/Annex XIV Part B).  

---

### 5. Human‑Escalation Triggers (Yellow‑gate actions)

| Trigger | Action Required | Responsible Role |
|---------|-----------------|-------------------|
| **Classification uncertainty** (e.g., rule overlap) | Halt filing; request senior regulatory review & classification decision memo | Regulatory Lead |
| **Missing UDI‑DI uniqueness verification** | Pause EUDAMED registration until global uniqueness confirmed by issuing agency | QMS Manager / UDI Coordinator |
| **Absence of PMCF plan for Class IIb/III** | Escalate to Clinical Affairs; develop & approve PMCF protocol before Annex XIV Part B submission | Clinical Lead |
| **Significant adverse‑event trend detected in PMS data** | Immediate safety notice, corrective action plan, and possible NR (Notified Body) notification | Vigilance Officer |
| **Failure of any QMS audit finding** | Suspend conformity‑assessment activities until remediation; inform Notified Body if applicable | Quality Manager |

---

### 6. Peer‑Review Prompt  

> *“@RA‑Peer: Please review the assumptions made above, especially the default classification pathways and the completeness of the evidence list. Are there any jurisdiction‑specific nuances (e.g., national UDI portal requirements, additional post‑market reporting obligations in specific Member States) that we have omitted? Also verify whether the cited source excerpts fully support the stated EUDAMED registration steps for Modules 2–5.”*

---

### 7. Lesson Learned – Reusable RA Judgment  

- **Never assume classification without an explicit intended‑use statement; always request a formal “Intended Purpose” declaration before proceeding with any PMS/PMCF planning.**  
- **EUDAMED Module 2 (UDI/DEV) registration is mandatory for every MDR device, and its data fields must be exactly aligned with the issuing agency’s syntax (Basic UDI‑DI, UDI‑DI, UDI‑PI). Missing or improperly formatted entries will block downstream PMS module activation.**  
- **Linking PMCF outcomes back to the risk‑management file is not optional – it satisfies both Art. 61 updates and the residual‑risk justification required for the PSUR (Art. 86) of higher‑risk devices.**  

--- 

*Prepared by Theo – EU Regulatory Affairs Specialist (MDR)*

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

### kb-eval-20260717-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "59120ec70443aebe", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `59120ec70443aebe`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PSUR_%ED%85%9C%ED%94%8C%EB%A6%BF_MDR_Article86.md)
- Source hash: `6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13`
- Focus: PMS and PMCF planning
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PSUR_템플릿_MDR_Article86.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Section 7. PMCF 결과 연계 (Art.86(1)(d)) | 항목 | 내용 | |---|---| | PMCF 계획 참조 문서 | [문서번호, 버전] | | PMCF 현재 상태 | [진행 중 / 완료 / 계획 단계] | | 이번 기간 주요 PMCF 결과 | [요약 또는 "중간 데이터 없음"] | | PMCF 결과의 CER 반영 | [반영 여부, 반영 내용] | | 다음 PMCF 중간 보고 예정일 | [YYYY-MM-DD] | --- ### Section 2. 판매량 및 노출 추정 (MDR Art.86(1)(c)) | 지역 | 판매 수량 | 추정 환자 노출 수 | 판매 기간 | |---|---|---|---| | EU...
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

### 1. Device Overview (Information Required)
| Item | Current Status | Comments / Evidence Needed |
|------|----------------|----------------------------|
| **Device name / model** | – | Obtain exact commercial name and model numbers. |
| **Intended medical purpose & indication(s)** | – | Needed to determine classification (Annex VIII) and applicable conformity‑assessment route. |
| **Target patient population** | – | Required for exposure estimates and risk‑benefit assessment. |
| **Date of first EU market placement** | – | Determines PMS reporting timelines (Art 83‑86). |

> **Human‑escalation trigger #1:** If any of the above items remain unavailable after the next 5 business days, halt preparation of the Technical Documentation and notify the Project Lead.

---

### 2. Classification & Conformity‑Assessment Route  
| Criterion | Assessment | Evidence Required |
|-----------|------------|-------------------|
| **MDR classification rule (Annex VIII)** | *Cannot be assigned* – intended purpose missing. | • Full Intended Use Statement <br>• Device description, mode of action, and energy source (if active). |
| **Conformity‑assessment route** | Dependent on classification & risk class: <br>– Class I (non‑sterile, non‑measuring) → self‑declaration (Annex IV). <br>– Higher classes → Notified Body (NB) audit (Annex IX for QMS; Annex X/XI for type‑examination). | • Classification decision memo.<br>• Relevant NB module(s) selected. |

> **Human‑escalation trigger #2:** If classification cannot be established within 10 days, involve the Regulatory Strategy Lead to reassess scope and potential need for a new NB.

---

### 3. PMS System (Art 83‑86 MDR)

| Requirement | Current Evidence (from source) | Gap / Action |
|-------------|--------------------------------|--------------|
| **PMS Plan** (Art 84) | – | Draft plan covering: <br>• Defined procedures for collection, analysis & reporting of post‑market data.<br>• Trigger levels for safety actions. |
| **Periodic Safety Update Report (PSUR)** (Art 86) for Class IIa–III devices | Section 2 provides a template for *sales volume* and *patient exposure* estimates (Art. 86(1)(c)). | • Populate with actual sales figures per region.<br>• Document methodology & assumptions as required by **MDCG 2022‑21 §5.3**. |
| **PMCF Results Integration** (Art. 86(1)(d)) | Section 7 gives a table structure for reporting PMCF outcomes. | • Insert concrete data: <br> – Reference to the approved PMCF plan (Annex XIV Part B).<br> – Status of ongoing activities.<br> – Summary of interim findings and how they are reflected in the Clinical Evaluation Report (CER) (Annex XIV Part A). |
| **Interim Reporting Schedule** | Placeholder “다음 PMCF 중간 보고 예정일” present. | • Define exact dates for each interim report per the PMCF plan. |

> **Human‑escalation trigger #3:** If any sales/exposure estimate is missing or methodology not documented, flag to the Market Access team; incomplete PSUR may cause NB non‑conformity findings.

---

### 4. PMCF Planning (Annex XIV Part B)

| Element | Required Content | Current Status |
|---------|------------------|----------------|
| **PMCF Plan reference** (Art. 86(1)(d), Table in Section 7) | • Document number & version. | – (to be supplied). |
| **Current PMCF status** | “진행 중 / 완료 / 계획 단계”. | Placeholder only. |
| **Key interim results of the reporting period** | Concise summary or ‘중간 데이터 없음’. | Empty – need data. |
| **Incorporation of PMCF outcomes into CER** (Art. 86(1)(d)) | Indicate whether *and how* results have been used to update the CER (e.g., new safety signals, performance trends). | Not yet documented. |
| **Date of next interim PMCF report** | Specific YYYY‑MM‑DD. | Placeholder only. |

> **Human‑escalation trigger #4:** Absence of a validated PMCF plan or missing linkage to the CER must be escalated to the Clinical Affairs Lead for immediate development.

---

### 5. Required Evidence – Checklist (per MDR)

| Evidence Item | Reference (MDR) | Present? | Comment |
|---------------|------------------|----------|---------|
| **Technical Documentation** (Annex II/III) | – | No | Need full file. |
| **Risk Management File** (ISO 14971 & Art 10) | Annex I, GSRS | No | Must include post‑market risk evaluation updates. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A | Partial – PMCF linkage missing. | Update after PMCF data are incorporated. |
| **PMCF Plan & Reports** | Annex XIV Part B | Skeleton present; content missing. | Populate with actual study design, endpoints, schedule. |
| **PMS Plan & PSUR (or PMS Report for lower‑risk)** | Arts 83‑86 | Template exists; data absent. | Fill in sales/exposure numbers and methodology per MDCG 2022‑21 §5.3. |
| **Post‑Market Clinical Follow‑up Evaluation** | Art 86(1)(d) | No | Must be produced after each PMCF interim report. |
| **Declaration of Conformity (DoC)** | Annex IV | – | Dependent on completed conformity assessment. |

---

### 6. Risk Controls & Post‑Market Risk Management  
1. **Update risk management file** with any new hazards identified from PMCF or PMS data (Art 10, ISO 14971).  
2. **Implement corrective actions** promptly if safety signals exceed predefined trigger levels (e.g., >5% serious adverse event increase).  
3. **Re‑evaluate residual risk** in light of cumulative exposure estimates; adjust benefit–risk justification in the CER.  

> **Human‑escalation trigger #5:** Any identified trend that could alter the device’s intended use, safety profile, or classification must be escalated to the Quality & Safety Committee within 48 hours.

---

### 7. citations

| Topic | Citation |
|-------|----------|
| PMCF reporting requirements (Art 86(1)(d)) | **MDR Art. 86(1)(d)** – source excerpt [1] |
| Sales‑volume & patient‑exposure estimates (Art 86(1)(c)) | **MDR Art. 86(1)(c)** – source excerpt [2]; **MDCG 2022‑21 §5.3** for methodology guidance (mentioned in excerpt). |
| PMCF plan location in the MDR | **Annex XIV Part B** (PMCF planning) – per regulatory mapping table. |
| PMS system obligations | **Art. 83–86 MDR** (system, plan, report, PSUR). |
| Classification rules source | **Annex VIII MDR** – required for classification decision (no specific rule can be applied yet). |
| Clinical Evaluation Report location | **Annex XIV Part A** – CER requirement. |
| Risk‑management basis | **Annex I MDR**, implemented via **ISO 14971**. |

*No specific identifier (e.g., 510(k)/predicate/registration number) appears in the provided source excerpts — verify separately.*

---

### 8. Human‑Escalation Summary  

| # | Condition | Responsible Role | Deadline |
|---|-----------|------------------|----------|
| 1 | Missing device name, intended use, or indication | Project Manager / Product Owner | +5 business days |
| 2 | Classification cannot be determined | Regulatory Strategy Lead | +10 days |
| 3 | Sales/exposure data or methodology absent in PSUR draft | Market Access Analyst | Immediate (as soon as data become available) |
| 4 | No validated PMCF plan or CER linkage | Clinical Affairs Lead | +7 days |
| 5 | New safety signal or risk‑benefit shift identified | Quality & Safety Committee | Within 48 h of detection |

---

### 9. Peer‑Review Prompt  

> **To the RA team:**  
> Please review this draft and challenge any assumptions made about the scope of required PMS/PMCF evidence, especially:  
> * Whether the template sections from Sections 2 and 7 fully satisfy Art 86(1)(c) & (d).  
> * If additional data sources (e.g., EU vigilance database, EUDAMED submissions) should be referenced.  
> * Any jurisdiction‑specific gaps—for example, whether the Korean market exposure estimate needs separate local reporting per MFDS requirements.  

Your feedback will help close any remaining documentation gaps before we move to the NB audit preparation stage.

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

## ra_kr

### kb-eval-20260717-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "1dfb18913b023f44", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `1dfb18913b023f44`
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

> **Regulatory Draft – Digital Medical Software (AI‑Enabled) – Korean MF DS Pathway**

---

### 1. Product Overview  
| Item | Description |
|------|-------------|
| **Product type** | Stand‑alone medical software (independent‑type) incorporating AI/ML algorithms for image analysis (e.g., lesion detection or triage). |
| **Intended use** | Assist clinicians in interpreting radiologic images; provides decision support but does not replace a qualified physician’s judgment. |
| **Key functionalities** | • Image acquisition interface  <br>• AI‑based lesion detection/triage   <br>• Output of diagnostic suggestions on DICOM workstations |

*The precise claim (assistive vs diagnostic) must be clarified before final classification.*

---

### 2. Applicable Korean Classification & Submission Route  

| Regulation / Guideline | Relevant Extracted Source | Interpretation |
|------------------------|---------------------------|----------------|
| **디지털의료제품법** (Digital Medical Products Act) – effective 2024‑01‑24 (2025‑01‑24 implementation) | 【1112950876551682081】 | Introduces a separate framework for AI/SW‑based digital medical products, requiring change‑management plans and component performance evaluation. |
| **의료용 소프트웨어 허가·심사 가이드라인** & **독립형 SW 사용적합성 가이드라인** | 【1112950876551682081】 | Stand‑alone software is classified as *2등급* (Class II) but may be upgraded depending on the level of assistive function. |
| **MFDS “허가” vs “신고”** | Implicit from 2등급 classification | Class II digital medical products require a formal **허가** (approval) submission, not a simple 신고 (notification). |

> **Result:** The product falls under **Class II (2등급)** in Korea and must pursue a **허가** pathway.  

*If the AI claims are elevated to diagnostic (i.e., primary decision‑making), reassess for possible 3등급 classification.*

---

### 3. Required Evidence Package (Korean MFDS)

| Evidence Category | Specific Korean Requirements | Comments / Mapping |
|-------------------|------------------------------|--------------------|
| **Technical Documentation** | • Software Description, Architecture Diagram  <br>• Algorithm description, training data summary  <br>• Change Management Plan (관리계획) per 디지털의료제품법  <br>• Component Performance Evaluation (구성요소 성능평가) | Aligns with “변경관리계획, 구성요소 성능평가” cited in the guideline 【1112950876551682081】. |
| **Risk Management** | IEC 62304‑based software life‑cycle; IEC 60601‑1‑2 for electromagnetic safety if hardware integrated; Korean MFDS risk analysis template. | Mandatory for all Class II devices. |
| **Clinical Evaluation** | • Clinical performance data (local or foreign) demonstrating intended use. <br>• If the claim is “assistive,” foreign clinical evaluation may be acceptable, but MFDS often requires *Korean‑language* summary and justification of external data relevance. | No explicit exemption in source – treat as required. |
| **KGMP Facility Certification** | Manufacturer’s production site must hold KGMP (Korean Good Manufacturing Practice) certification for software development & distribution. | Required for 허가 submissions. |
| **Labeling / IFU** | All labeling, instructions for use, and safety information must be provided in **Korean**; include CE/FDA clearance statements only if they meet Korean translation standards. | Language requirement is non‑negotiable. |
| **Cybersecurity & SBOM** | While the 2023 FDA SBOM mandate does not directly apply in Korea, MFDS expects a **cybersecurity risk assessment** and **software bill of materials** for AI‑enabled products under the new digital medical product framework. | Inference from US guidance; include to satisfy MFDS scrutiny. |
| **Post‑Market Surveillance (PMS) Plan** | • Periodic safety update reports (시판후조사) <br>• Real‑world performance monitoring, especially for AI drift. | Required for Class II 허가 products. |

> **Citation Note:** No specific MFDS case numbers or registration identifiers appear in the source excerpts; therefore: *no specific identifier found in source — verify separately*.

---

### 4. Missing / Clarification Needed  

| Item | Why it is needed | Action |
|------|------------------|--------|
| Detailed **intended use statement** (assistive vs diagnostic) | Determines whether 2등급 or higher classification applies. | Obtain exact wording from product marketing. |
| **Algorithm change control scope** (frequency, magnitude of updates) | The digital medical product law requires a *Predetermined Change Control Plan* for AI/ML models; MFDS will assess if updates stay within the approved scope. | Provide a written PCCP draft (referencing FDA guidance as a model). |
| **Training data provenance** (origin, representativeness of Korean population) | To justify reliance on foreign clinical data or to decide if local validation is mandatory. | Supply dataset description and any localized performance results. |
| **Korean language labeling** drafts | MFDS reviews language compliance early in the dossier. | Prepare Korean translations for label, IFU, marketing materials. |
| **KGMP certification status** of development site(s) | Mandatory for 허가; must be included in submission package. | Confirm current KGMP certificate or initiate certification. |

---

### 5. Core Risk Controls (to be documented)

1. **Software Life‑Cycle Management** – IEC 62304 compliance, version control, validated verification/validation activities.  
2. **AI Model Governance** – PCCP outlining permissible model updates; continuous performance monitoring; drift detection algorithms.  
3. **Cybersecurity Measures** – Threat modeling, secure coding standards, regular penetration testing, SBOM inventory.  
4. **Data Privacy** – Compliance with Korea’s Personal Information Protection Act (PIPA) for patient image data.  
5. **Human Factors/Human‑Machine Interface** – Usability testing to ensure clinicians understand AI output limits.  

---

### 6. Human‑Escalation Triggers  

| Trigger | Description | Escalation Path |
|--------|-------------|-----------------|
| **Classification dispute** (evidence suggests > 2등급) | If clinical claim or AI performance indicates primary diagnostic role. | Senior RA lead + legal review before dossier finalization. |
| **Insufficient local clinical data** | MFDS requests Korean‑specific validation that is not yet available. | Pause submission; engage CRO for local study, inform project sponsor. |
| **Change Management breach** | Planned AI model update exceeds scope of approved PCCP. | Immediate risk assessment by QA, submit amendment to MFDS. |
| **KGMP non‑compliance detected** | Audit reveals gaps in software development processes. | Halt submission; corrective actions and re‑certification before resubmission. |
| **Labeling language issue** | Korean labeling fails readability or regulatory wording check. | Translate/review with certified medical translator; legal sign‑off required. |

---

### 7. Citations  

* Classification & digital product framework – **디지털의료제품법**, “2등급” guidance, and software suitability guidelines: 【1112950876551682081】  
* U.S. FDA comparator information (for reference only): 【533793244310539451】

---

### 8. Peer‑Review Prompt  

> **To the RA team:** Please review this draft and challenge the following points:  
> 1. Are we correctly interpreting the “2등급” classification given the AI assistive claim, or should a higher class be presumed?  
> 2. Does the evidence list fully capture MFDS expectations for AI‑enabled software under the 2025 Digital Medical Products Act, especially regarding change‑control and component performance evaluation?  
> 3. Have we identified all jurisdiction‑specific gaps (e.g., Korean language requirements, KGMP certification) that could halt the submission if overlooked?

---

### 9. Reusable RA Judgment (Lesson Record)  

**Lesson:** When a stand‑alone AI/ML medical software is slated for the Korean market under the post‑2025 **디지털의료제품법**, classify it as **Class II (2등급)** by default, but verify that the intended use remains assistive. The submission must include:  
- A written **Change Management Plan** and **Component Performance Evaluation** per the digital product guidelines,   
- Full **KGMP certification**,   
- Korean‑language labeling/IFU, and   
- Robust **risk management** aligned with IEC 62304 plus a dedicated AI governance (PCCP).  

If any of these elements are missing or ambiguous—particularly the intended use statement or AI change scope—the dossier should be paused for clarification before MFDS 허가 submission.

*Recorded via `honcho_conclude` for future reference.*

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

### kb-eval-20260717-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "d5ea86ec38a8dee3", "source": "github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md", "source_hash": "e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `d5ea86ec38a8dee3`
- Source: `github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/014_01_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `014_01_디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 배경 디지털의료제품법은 2025-01-24 시행, 시행규칙 2025-02-28 현행. 사용적합성 자료 제출 의무화, 사이버보안 요구 확대(15→35), AI 변경관리 계획, 구성요소 단위 성능평가(2026 시행) 등 본 프로젝트(X-ray Workstation SW·AI 영상분석 모듈 가능성)에 직접 영향. 2026-04-22 교차검증에서 G2(사용적합성 증빙 미대응), G3(구성요소 평가 적용 여부 미판정), G4(RA-01~RA-20 전수 매핑 미완) 도출. ## 참고 링크 - `01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md` - `12_교차검증_보고서/2026-04-22_SBOM_디지털의료제...
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

> **Regulatory Draft – X‑ray Workstation Software & AI Imaging Analysis Module  
Impact of the Korean “Digital Medical Products Act” (디지털의료제품법) and its Enforcement Rules**

---

### 1. Classification & Submission Route  

| Item | MFDS Requirement | Likely Outcome for the Project |
|------|------------------|--------------------------------|
| **Product Type** | Software‑as‑Medical‑Device (SaMD) with integrated AI (영상분석 모듈) used in an X‑ray workstation | SaMD – AI‑driven diagnostic support |
| **Risk Class** (per “Digital Medical Products Act” & MFDS guidelines) | • Class I – low risk, no invasive function  <br>• Class IIa/IIb – moderate risk (diagnostic assistance, imaging analysis) <br>• Class III – high risk (critical diagnostic impact) | The AI‑based image analysis influencing clinical decisions typically falls into **Class IIb** or **Class III**. MFDS usually requires **허가 (approval)** for Class IIb/III SaMD. |
| **Submission Pathway** | • *신고* – for Class I <br>• *허가(인증)* – for Class IIa‑III | **MFDS 허가** (full approval) is expected. The dossier must be submitted to the MFDS “디지털의료제품 정보 포털” (emedi.mfds.go.kr). |
| **Facility Requirement** | KGMP certification or ISO 13485‑compliant quality system for software development | The developer’s site must hold a **KGMP certificate** (or an internationally recognized ISO 13485 certification accepted by MFDS) before submission. |

---

### 2. Required Evidence (per the Act & Enforcement Rules, effective 2025–02‑28)

| Evidence | MFDS Expectation | Status in Source |
|----------|------------------|-------------------|
| **Usability / 사용적합성 자료** | Full usability test reports demonstrating safe and intended use by target users. Mandatory under the Act (see “사용적합성 자료 제출 의무화”). | **Missing** – G2 identified as “사용적합성 증빙 미대응”【1】 |
| **Cybersecurity Controls** | Expanded checklist (35 items) covering threat modeling, data protection, secure updates, encryption, incident response. | **Partial** – referenced as expanded requirement; actual compliance not confirmed in source. |
| **AI Change‑Management Plan** | Documented process for version control, training data traceability, performance monitoring after each AI update. | Required by the Act (mentioned). No evidence presented in source. |
| **Component‑Level Performance Evaluation** | Individual assessment of each software component (e.g., image preprocessing, AI inference engine) per 2026 enforcement schedule. | **Missing/Undetermined** – G3 notes “구성요소 평가 적용 여부 미판정”【1】 |
| **Software Bill of Materials (SBOM)** | Complete inventory of all third‑party libraries, licenses, and version numbers; must be submitted with the dossier. | Reference to SBOM in cross‑validation report 【2】 but no confirmation that a final SBOM is ready. |
| **Risk Management File** (ISO 14971) | Updated for AI lifecycle, including data drift monitoring, post‑market performance surveillance, and risk‐benefit analysis. | Not mentioned; assumed required. |
| **Clinical Evidence** | Either: <br>• Local clinical trial data meeting Korean ethical standards **or** <br>• Accepted foreign clinical evaluation (FDA 510(k) or CE‑marked) *plus* additional Korean bridging data if MFDS requires. | No specific identifiers (e.g., 510(k) numbers) found in source – verify separately. |
| **Labeling & IFU** | All labeling, instructions for use and safety information must be provided in **Korean**. | Not addressed in source; needs preparation. |
| **Post‑Market Surveillance Plan** | Ongoing monitoring, adverse event reporting, periodic safety update reports (PSUR). | Required but not evidenced. |

---

### 3. Gaps Identified from Cross‑Validation (2026‑04‑22)

| Gap Code | Description | Immediate Action Needed |
|----------|-------------|--------------------------|
| **G2** | No usability (사용적합성) evidence provided. | Conduct formal usability study with target users; compile report per MFDS template. |
| **G3** | Unclear whether component‑level performance evaluation has been applied. | Define each software module, prepare test protocols, and generate performance data for every component. |
| **G4** | Incomplete mapping of all regulatory requirements (RA‑01 ~ RA‑20) to project artifacts. | Create a traceability matrix linking each MFDS requirement to supporting documents; close all gaps before submission. |

---

### 4. Key Risk Controls & Mitigation Measures  

1. **Cybersecurity** – Implement the full 35‑item checklist (threat modeling, secure coding standards, regular penetration testing, encryption of DICOM data).  
2. **AI Lifecycle Management** – Maintain an AI change‑management log; enforce version control; perform re‑validation after any algorithm update.  
3. **SBOM Transparency** – Publish an up‑to‑date SBOM and conduct third‑party component vulnerability scanning (e.g., using NVD CVE database).  
4. **Usability Engineering** – Follow IEC 62366‑1 for user‑centered design; document task analysis, formative/usability testing results.  
5. **Component Performance** – Use unit‑test suites and performance benchmarks for each software block; include statistical confidence limits.  
6. **Post‑Market Surveillance (PMS)** – Set up automated adverse event capture from radiology information systems; schedule quarterly safety updates to MFDS.  

---

### 5. Human‑Escalation Triggers  

| Trigger | When to Escalate to Senior RA / Legal |
|---------|----------------------------------------|
| **Regulatory Gap** – Any of G2, G3, or G4 remain unresolved after the defined remediation deadline (e.g., 30 days). |
| **Cybersecurity Deficiency** – Failure to satisfy >5 items of the 35‑item checklist in a security audit. |
| **AI Model Drift** – Detected performance degradation ≥10 % from baseline during post‑market monitoring. |
| **Adverse Event Spike** – ≥2 serious device‑related incidents reported within a 30‑day window. |
| **Labeling Non‑Compliance** – Receipt of MFDS notice demanding Korean language revisions after submission. |
| **KGMP / ISO 13485 Gap** – Facility audit reveals missing certification or non‑conformities. |

---

### 6. Citations  

- Background & enforcement dates, usability obligation, cybersecurity expansion, AI change‑management plan, component evaluation schedule, and identified gaps (G2‑G4) are taken from **Excerpt [1]**【1】.  
- Reference links to MFDS portal, Korean law database, and issue checklists (GSPR, cyber, SBOM) are listed in **Excerpt [2]**【2】.  

> **No specific identifier found in source — verify separately** for any 510(k), predicate, or MFDS case numbers that may support the clinical evidence portion.

---

### 7. Peer‑Review Prompt (for a fellow RA)

> *Please review this draft and challenge the following:*  
> 1. **Assumptions on risk class:** Is the classification as Class IIb/III justified based on the limited functional description provided?  
> 2. **Scope of source coverage:** Do the excerpts capture all MFDS obligations (e.g., labeling, PMS) or are additional regulatory sections missing?  
> 3. **Jurisdiction‑specific gaps:** Are there Korean‑only requirements (such as mandatory local clinical validation for AI SaMD) that have not been addressed here?  

---

### 8. Reusable RA Judgment (Lesson Learned)

- **When a new Korean regulation (e.g., Digital Medical Products Act) introduces expanded obligations—usability evidence, cybersecurity checklists, AI change‑management, and component‑level assessment—any existing SaMD project must be re‑mapped against the full MFDS requirement list (RA‑01 ~ RA‑20).**  
- **Missing any of these evidences triggers a “G‑type” gap that must be closed before proceeding to 허가 submission; otherwise the dossier will be rejected in the pre‑review stage.**  
- **Always verify whether foreign clinical evidence is acceptable, and record that no specific identifiers were found in source material before citing them.**  

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

1. Chunk `1061576322702878078`

> ## 배경 디지털의료제품법은 2025-01-24 시행, 시행규칙 2025-02-28 현행. 사용적합성 자료 제출 의무화, 사이버보안 요구 확대(15→35), AI 변경관리 계획, 구성요소 단위 성능평가(2026 시행) 등 본 프로젝트(X-ray Workstation SW·AI 영상분석 모듈 가능성)에 직접 영향. 2026-04-22 교차검증에서 G2(사용적합성 증빙 미대응), G3(구성요소 평가 적용 여부 미판정), G4(RA-01~RA-20 전수 매핑 미완) 도출.

2. Chunk `1016004334478948993`

> ## 참고 링크 - `01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md` - `12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md` - MFDS 디지털의료제품 정보 포털 (emedi.mfds.go.kr) - 국가법령정보센터 「디지털의료제품법」 - 관련 이슈: 005(GSPR 체크리스트 v0.2→v0.3), 009(사이버보안), 013(SBOM)

### kb-eval-20260717-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "0f74951e1b860215", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `0f74951e1b860215`
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

> **Regulatory Draft – Impact of the “Digital Medical Products Act” (법률 제20139호) on a SaMD/AI‑based product**

---

### 1. Applicable Legal Framework  
| Element | Source |
|---|---|
| **Law** | 디지털의료제품법 (법률 제20139호, 2024‑01‑23) – 시행일 2025‑01‑24【1002132727008468922】 |
| **Enabling Decree** | 대통령령 제35219호 (2025‑01‑23 제정)【1002132727008468922】 |
| **Regulatory Rules** | 총리령 제1958호 (2025‑02‑28 시행)【1002132727008468922】 |
| **Key Sub‑regulations & Guidelines** | *디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정*, *분류 및 등급 지정 규정*, *디지털의료기기 제조·품질관리 기준*, *전산 침해 방지 보안 지침(안)*【1002132727008468922】 |
| **Relevant 2024‑2025 Guidance** | • “디지털치료기기 임상시험 설계 가이드라인” (2024‑12) – 낮음, DTx 전용<br>• “생성형 AI 의료기기 허가·심사 가이드라인” (2025‑01) – 중, AI 영상 분석 모듈<br>• “독립형 디지털의료기기SW 사용적합성 가이드라인” (2025‑01) – 높음, 콘솔/뷰어 SW<br>• “의료기기 사이버보안 허가·심사 가이드라인(개정)” (2025‑01‑10) – 높음, 네트워크 연결 기기 전체<br>• “디지털의료기기 전자적 침해행위 보안 지침(안)” (2025‑01) – 높음, SBOM 관리 포함【1077225675205822581】 |

---

### 2. Product Classification & Submission Pathway  

| Question | Determination |
|---|---|
| **Is the product a Medical Device?** | Yes – it is software that performs medical function (diagnostic/therapeutic) without being part of a physical device, thus falls under “디지털의료기기”. |
| **Classification (Class I‑III)** | The Act adopts risk‑based classification analogous to existing MFDS rules. For AI‑driven diagnostic software (e.g., image analysis), the default is **Class II** unless the algorithm determines life‑supporting or high‑risk therapy, which would push it to **Class III**. Confirmation requires a *risk‐based class determination matrix* from the “분류 및 등급 지정 규정”. |
| **Submission Route** | - **Class I** → 신고 (notification) <br> - **Class II** → 인증 (certification) – may require conformity assessment by an authorized body <br> - **Class III** → 허가 (approval) – full MFDS review. <br> *Assuming Class II, the route is “인증”.* |
| **Regulatory Reference** | 디지털의료제품법 및 그 시행령·시행규칙【1002132727008468922】 |

---

### 3. Required Evidentiary Package  

| Evidence Category | Specific Requirements (per Act & Guideline) | Source |
|---|---|---|
| **Device Description** | • Functional description, intended use, algorithm architecture, version control.<br>• Software bill of materials (SBOM) – required by “디지털의료기기 전자적 침해행위 보안 지침(안)”【1077225675205822581】 | Act & Security Guideline |
| **Risk Management** | • ISO 14971‑based risk analysis, with emphasis on AI‑related failure modes (bias, drift).<br>• Cybersecurity plan per “의료기기 사이버보안 허가·심사 가이드라인(개정)”【1077225675205822581】 | Security Guideline |
| **Clinical Evaluation** | • Clinical performance data – either from Korean patients or acceptable foreign clinical data aligned with MFDS guidance.<br>• If foreign data used, must map to locally relevant endpoints; otherwise local bridging study required. | General MFDS requirement (implicit) |
| **Non‑clinical Testing** | • Verification & validation per IEC 62304/IEC 82304‑1.<br>• Usability engineering per IEC 62366‑1 (especially for standalone UI). | Standard practice – no specific identifier in source |
| **Software Validation / Conformity Assessment** | • Use of the “독립형 디지털의료기기SW 사용적합성 가이드라인” (high relevance)【1077225675205822581】<br>• Evidence of compliance with Korean KGMP for software – may require a qualified‑person audit report. | Software Guide |
| **Labeling & IFU** | • All labeling, Instructions For Use (IFU), and promotional material must be in Korean language.<br>• Include safety information, intended use, contraindications, and post‑market surveillance contact. | MFDS language requirement (standard) |
| **Post‑Market Surveillance Plan** | • PMS plan outlining adverse event reporting, periodic safety update reports, and field corrective actions. | MFDS PMS rule (implicit) |

*No specific identifier (e.g., 510(k), CE‐Mark number) appears in the source excerpts – verify separately.*  

---

### 4. Missing Information / Gaps to Resolve  

| Item | Why Needed | Action |
|---|---|---|
| **Exact risk class** (I/II/III) per “분류 및 등급 지정 규정”. | Determines submission type and evidence depth. | Perform formal classification using MFDS matrix; document justification. |
| **Whether foreign clinical data will be accepted** – the Act allows OECD‑aligned foreign data, but confirmation of acceptable sources is required. | Impacts need for Korean bridge study. | Identify comparable foreign trials; request MFDS pre‑submission meeting to confirm acceptability. |
| **KGMP certification status of the software development environment** (e.g., ISO 13485 or MFDS‐approved KGMP). | Mandatory for Class II/III products. | Conduct gap analysis and obtain KGMP audit report if not already in place. |
| **Detailed SBOM and security threat model** – required by the “디지털의료기기 전자적 침해행위 보안 지침(안)”. | Addresses cyber‑risk obligations. | Prepare SBOM, conduct vulnerability assessment, map to security guideline checklist. |
| **Korean language IFU draft** – no evidence of translation shown. | Language compliance is non‑negotiable for MFDS review. | Produce Korean labeling/IFU; arrange professional medical translation and regulatory review. |
| **Post‑market surveillance (PMS) plan template** – specific to digital health devices. | Required for certification/허가. | Draft PMS plan aligning with MFDS “시판후조사” rules; include data collection, signal detection, and reporting timelines. |

---

### 5. Core Risk Controls (to be documented in the technical file)

| Control | Description |
|---|---|
| **Algorithm Governance** | Version control, change‑impact analysis, continuous performance monitoring, retraining protocol with pre‑defined drift thresholds. |
| **Cybersecurity** | Network segmentation, encryption of data at rest/in transit, regular penetration testing, incident response SOP (per 2025 security guideline). |
| **Usability Engineering** | Human factors validation with Korean end‑users; task analysis for UI error prevention. |
| **Fail‑Safe/Graceful Degradation** | When AI confidence < threshold → default to clinician review; clear alerts in IFU. |
| **Data Privacy** | Compliance with Personal Information Protection Act (PIPA) – de‑identification, consent management. |

---

### 6. Escalation Triggers for Human Review / MFDS Interaction  

| Trigger | Action Required |
|---|---|
| **Classification disagreement** (e.g., regulator suggests Class III but submitter prepared for Class II). | Suspend submission; conduct additional risk analysis; request pre‑submission meeting with MFDS. |
| **Foreign clinical data not accepted** after preliminary review. | Initiate local bridging study; update Clinical Evaluation Report (CER). |
| **KGMP audit failure or missing certificate**. | Pause submission; remediate manufacturing/QMS gaps; obtain KGMP certification before proceeding. |
| **Security vulnerability discovered post‑submission** that impacts the SBOM or threat model. | File urgent safety notice to MFDS, issue field corrective action, and update technical file. |
| **Labeling/IFU translation error identified during review**. | Immediately revise Korean materials; resubmit corrected labeling package. |
| **Unexpected adverse event trend in PMS data exceeding predefined threshold**. | Initiate field corrective action, notify MFDS within required timelines (7‑day serious report). |

---

### 7. Citations  

- 디지털의료제품법 (법률 제20139호), 시행일 2025‑01‑24【1002132727008468922】  
- 대통령령 제35219호 (시행일 2025‑01‑24)【1002132727008468922】  
- 총리령 제1958호 (시행일 2025‑02‑28)【1002132727008468922】  
- “생성형 AI 의료기기 허가·심사 가이드라인” (2025‑01) – 중·AI 영상 분석 모듈【1077225675205822581】  
- “독립형 디지털의료기기SW 사용적합성 가이드라인” (2025‑01) – 높음・콘솔 SW, 뷰어 SW【1077225675205822581】  
- “의료기기 사이버보안 허가·심사 가이드라인(개정)” (2025‑01‑10) – 높음・네트워크 연결 기기 전체【1077225675205822581】  
- “디지털의료기기 전자적 침해행위 보안 지침(안)” (2025‑01) – 높음・SBOM 관리 포함【1077225675205822581】  

*No specific identifier (e.g., 510(k), CE Mark, MFDS registration number) appears in the provided source excerpts—verify separately.*

---

### 8. Peer‑Review Prompt  

> **Colleague Review Requested:**  
> Please evaluate the assumptions and evidence gaps identified above, focusing on:  
> 1. Whether the classification rationale aligns with the latest “분류 및 등급 지정 규정”.  
> 2. The adequacy of foreign clinical data acceptance criteria under the Digital Medical Products Act (any recent MFDS notices not captured here).  
> 3. Completeness of the cybersecurity/SBOM controls relative to the 2025 security guideline.  
> 4. Any additional Korean‑specific obligations (e.g., post‑market surveillance reporting frequency, telemedicine integration) that might affect this submission pathway.  

---

### 9. Reusable RA Judgment (Lesson Capture)

**When evaluating a SaMD/AI product under Korea’s Digital Medical Products Act (법률 제20139호), always:**

1. **Map the product to the risk‑based classification matrix** defined in the “분류 및 등급 지정 규정” and confirm the submission route (신고 → 인증 → 허가).  
2. **Cross‑reference every foreign piece of evidence (clinical, non‑clinical, security) with the latest MFDS guidelines** (2024‑2025 series) to verify acceptance; when in doubt, request a pre‑submission meeting.  
3. **Prepare Korean‑language labeling/IFU and an SBOM‑driven cybersecurity dossier** as they are mandatory under the 2025 security guideline and “전자적 침해행위 보안 지침”.  
4. **Document KGMP compliance for software development** (ISO 13485 or MFDS‑approved) before filing any certification/허가 application.  

*These steps close the typical gaps that trigger escalation during Korean regulatory review of digital health devices.*

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

### kb-eval-20260717-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "f82161e7e993723e", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "a20110f67bbd98b35d188d8a2fd8d816a95754663f6515d8828b632ceb3d72e5"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f82161e7e993723e`
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

> **Regulatory Draft – Classification & Submission Pathway for the X‑ray Digital Medical Product (2026‑04‑22)**  

---

### 1. Scope of the digital medical product  

| Sub‑system | Digital‑medical‑product status* (per source [1]) | Rationale |
|------------|---------------------------------------------|-----------|
| **Generator firmware** | ❌ Not a digital medical device | Pure hardware control, no network/software interface. |
| **Detector firmware** | △ Potentially applicable | Becomes a DMP when the detector is network‑connected (e.g., remote configuration). |
| **Acquisition Workstation Software** | ○ Applicable | Stand‑alone software that can be operated independently, is network‑capable and may host AI functions. |
| **Image post‑processing / AI analysis module** | ○ Applicable (SaMD + AI) | Performs clinical interpretation; therefore qualifies as a *Software as a Medical Device* with AI. |
| **DICOM transmission / PACS interface** | △ Potentially applicable | Provides communication functions; classification depends on whether it performs any diagnostic processing. |

\*Legend: “○” = clearly within the Digital‑Medical‑Product Act (DMPA) scope, “△” = conditional – becomes in‑scope if network connectivity or clinical functionality is enabled, “❌” = outside DMPA scope.

**Result:** The product family contains at least one SaMD component (the acquisition workstation and/or AI analysis module). Consequently the overall system must be treated as a **digital medical device** under the Korean *Digital Medical Products Act* (“디지털의료제품법”).

---

### 2. Classification & Submission Route  

| Component | Likely MFDS class (per DMPA) | Submission type |
|-----------|-----------------------------|-----------------|
| Acquisition Workstation (SW) – no AI | Class I (low‑risk) **if** it only performs image acquisition and transfer | *Notification* (신고) |
| AI analysis module (SaMD + AI) | **Class II** (moderate risk) – typical for diagnostic decision support algorithms; could be Class III if algorithm determines therapeutic decisions or high‑impact diagnosis. | *Approval* (허가) – requires full dossier and MFDS review. |
| Detector firmware (if networked) | Same class as workstation (likely Class I/II) pending functional change. | Notification or Approval accordingly. |
| DICOM/PACS interface (if purely data transport) | Usually Class I; becomes Class II if it adds diagnostic interpretation. | Notification / Approval accordingly. |

*Because the AI module is the highest‑risk element, the **overall submission route** will be driven by its classification.*  

- **If classified as Class II:** Prepare a full *허가* dossier (device registration) including clinical evaluation, risk management, software lifecycle documentation, cybersecurity, and post‑market surveillance plan.  
- **If later re‑classified to Class III:** Additional evidence (e.g., pivotal clinical trial data, more extensive safety monitoring) will be required.

---

### 3. Core Evidence Required (per MFDS & DMPA)

| Evidence Category | Specific Requirement | Typical Source |
|-------------------|----------------------|----------------|
| **Software Development Lifecycle** | IEC 62304‑based process; version control, configuration management. | SOP‑SBOM‑001 “SBOM 생성관리 절차” (referenced in source [2]). |
| **Risk Management** | ISO 14971 + MFDS guidance for SaMD/AI. Hazard analysis covering AI model drift, data integrity, and radiation exposure. | “진단용 방사선 안전관리 규칙” cited in source [2]. |
| **Cybersecurity** | MFDS Digital Medical Products Act cybersecurity provisions (see `IEC_81001-5-1_FDA_Cybersecurity_SW보안.md` referenced). Must document threat modelling, patch management, secure communications (TLS), and isolation of AI inference engine. | Source [2] includes the related SOP. |
| **Clinical Evaluation** | • Clinical performance data for AI algorithm (foreign CE‑marked or FDA‑cleared studies permissible if MFDS notice aligns – verify latest notice). <br>• Local clinical validation when AI influences diagnosis. | No specific identifier in source; must be obtained from sponsor’s dossier. |
| **Software Bill of Materials (SBOM)** | Complete SBOM covering all three “축” (components, dependencies, licenses) as per DMPA 3‑axis requirement. | Document `LOG-2026-04-22_SBOM_디지털의료제품법_정합성` (source [2]). |
| **Labeling & IFU** | Korean‑language labeling, UDI assignment, and user instructions complying with MFDS labeling rules. | Refer to MFDS labeling guidelines – not listed in source (need separate verification). |
| **Post‑Market Surveillance (PMS) Plan** | Ongoing safety monitoring, AI performance drift detection, incident reporting system. | Must be drafted per MFDS PMS requirements. |
| **KGMP** | Not required for pure SaMD, but any hardware requiring manufacturing under KGMP must hold certification. | No KGMP mention in source – verify hardware sub‑systems separately. |

---

### 4. Missing / Open Items (to be clarified before dossier finalisation)

1. **Final risk classification of the AI module** – need algorithm impact analysis to confirm Class II vs. Class III.  
2. **Local clinical data requirement** – does MFDS accept foreign CE/FDA evidence for this specific AI indication? (Check latest MFDS notice; none cited in source).  
3. **Network‑connection status of Detector firmware & DICOM/PACS module** – if they become networked, they shift from “❌/△” to “○”. Clarify intended architecture.  
4. **Detailed SBOM for each component** – source [2] confirms existence of an SBOM report but the actual list is not shown; must be supplied to MFDS.  
5. **Korean‑language IFU & labeling drafts** – required for any Class I‑III submission.  
6. **UDI strategy** – need a UDI assignment plan aligned with Korean UDI requirements (referenced in `SOP-UDI-001_UDI_통합관리_초안.md`).  

---

### 5. Key Risk Controls to Implement

| Hazard | Control Measure (per MFDS / IEC) |
|--------|-----------------------------------|
| **Incorrect AI diagnosis** | • Algorithm validation with diverse Korean patient data.<br>• Periodic performance monitoring & drift detection.<br>• Human‑in‑the‑loop review requirement. |
| **Cyber attack on networked firmware** | • Secure boot, signed firmware updates.<br>• TLS/HTTPS for all communications.<br>• Regular vulnerability scanning (aligned with IEC 81001‑5‑1). |
| **Radiation safety error (detector)** | • Compliance with “진단용 방사선 안전관리 규칙” – dose monitoring, interlock logic. |
| **Software version mismatch** | • SBOM‐driven dependency tracking; automated build reproducibility checks. |
| **Labeling mis‑interpretation** | • Korean language verification by native speaker; clear risk statements per MFDS labeling guide. |

---

### 6. Human‑Escalation Triggers (when RA team must raise to senior review)

| Trigger | Reason | Action |
|---------|--------|--------|
| **Reclassification of any component from “△” → “○”** (e.g., detector firmware becomes networked) | May increase overall device class and change submission route. | Immediate reassessment; senior RA sign‑off before dossier update. |
| **AI algorithm version change exceeding minor modification** (new data set, model architecture) | Requires new clinical performance evidence per MFDS AI guidelines. | Pause release; conduct supplemental validation; senior approval. |
| **Failure to provide complete SBOM** | MFDA DMPA mandates 3‑axis SBOM for SaMD – submission will be rejected. | Escalate to development lead for immediate remediation. |
| **Local clinical data not available but required** | Regulatory gap that could halt approval. | Engage sponsor/legal to arrange Korean study or request MFDS waiver; senior counsel review. |
| **Detected cybersecurity vulnerability in fielded devices** | Post‑market safety risk; mandatory reporting. | Trigger Incident Management SOP; notify MFDS within statutory timeframe (usually 48 h). |

---

### 7. Citations  

- Classification table and “디지털의료기기 해당?” assessment – source **Chunk 418096885713027360** (excerpt [1]).  
- Reference to SBOM‑related SOPs, AI requirements document, radiation safety rule, cybersecurity SOP – source **Chunk 437336887721584251** (excerpt [2]).  

*No specific MFDS docket numbers, 510(k) predicates, or CE identifiers appear in the provided excerpts; therefore no identifier is listed.*  

---

### 8. Peer‑Review Prompt  

> **To RA colleagues:**  
> Please review this draft and challenge the following points:  
> 1. Are we correctly interpreting the conditional (“△”) statuses for the detector firmware and DICOM/PACS interface under the Digital Medical Products Act?  
> 2. Have we captured all MFDS‑required evidence items for an AI‑enabled SaMD, or are there jurisdiction‑specific gaps (e.g., mandatory Korean clinical data) not reflected here?  
> 3. Does the risk‑control matrix align with the latest MFDS cybersecurity and radiation‑safety notices, or do you know of newer guidance that should be incorporated?  

---

### 9. Reusable RA Judgment (Lesson Record)

**Lesson ID:** KR‑DMPA‑2026‑01  
**Summary:** When a product family contains mixed hardware/firmware components, each sub‑system must be assessed individually for *digital medical product* status per the DMPA table (“디지털의료기기 해당?”). Any component with network connectivity or AI functionality triggers SaMD classification, and the highest‑risk element dictates the overall submission route (notification vs. approval). Evidence packages must include a complete SBOM (3‑axis), risk management per ISO 14971, cybersecurity documentation per IEC 81001‑5‑1, and local clinical validation for AI algorithms unless an MFDS notice explicitly accepts foreign data. Conditional components (“△”) require architectural confirmation; if they become active, the classification and submission pathway must be re‑evaluated immediately.  

*Recorded by:* Sam (Korean RA specialist) – **peer=ai**.

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

### kb-eval-20260717-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "0d973d2983eeaf78", "source": "github:holee9/MD-process/issue-drafts/947_AUDIT_디지털의료제품법_법률번호_20722_광범위_자매재발.md", "source_hash": "fed73ac605f6674c04cc5029490b7b167f60ab56f7464d148e79c94381f53999"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `0d973d2983eeaf78`
- Source: `github:holee9/MD-process/issue-drafts/947_AUDIT_디지털의료제품법_법률번호_20722_광범위_자매재발.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/947_AUDIT_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EB%B2%95%EB%A5%A0%EB%B2%88%ED%98%B8_20722_%EA%B4%91%EB%B2%94%EC%9C%84_%EC%9E%90%EB%A7%A4%EC%9E%AC%EB%B0%9C.md)
- Source hash: `fed73ac605f6674c04cc5029490b7b167f60ab56f7464d148e79c94381f53999`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `947_AUDIT_디지털의료제품법_법률번호_20722_광범위_자매재발.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 영향 (규제 리스크) - **인증기관·심사원 신뢰도**: 사이버보안/SW수명주기/AI 성능평가 문서는 심사 시 최우선 열람 대상. 제정 법률번호 오기(그것도 완전히 다른 법률번호)는 문서 신뢰성 결정타. - **GMP 적합판정·품목허가**: 근거 법령 오기시 근거불명으로 지적 가능. - **audit #930 대응 실효성 부족 증거**: 자매문서 스캔 범위 편향(QMS 폴더로 국한, 설계개발/사이버보안 폴더 누락). Plan #935(sister-document cross-reference 자동화)의 grep 매칭룰에 "법률 제[0-9]+호" 패턴을 우선 룰로 편입 필요. ### 참고 (Cross-Ref) — 부수 인용 - `...
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

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법, Law No. 20722) on a New SaMD Submission**

---

### 1. Product Classification & Submission Pathway  

| Attribute | Assessment |
|-----------|------------|
| **Product type** | Software as a Medical Device (SaMD) that provides diagnostic or therapeutic functions via AI algorithms. |
| **Risk class under MFDS** | Determined by intended use and impact on patient safety. <br>‑ *Class II* – General Diagnostic/Monitoring tools with low‑to‑moderate risk.<br>‑ *Class III* – Decision‑support AI that influences clinical treatment decisions.<br>‑ *Class IV* – Autonomous therapeutic AI. (Exact class must be confirmed by MFDS after classification review.) |
| **Regulatory route** | <ul><li>**Class II** → Notification (신고) with KGMP exemption if only software.</li><li>**Class III/IV** → Full 허가 (approval) requiring KGMP‑certified manufacturing environment for any related hardware or firmware, and submission of a detailed technical dossier.</li></ul> |
| **KGMP relevance** | Required when the product includes device‐related hardware or is produced in a facility that manufactures Class III/IV devices. Pure software may be exempt but must still comply with MFDS “Software Lifecycle Management” requirements. |

---

### 2. Core Evidence Package (per current Korean guidance)  

| Evidence Category | Required Content | Current Gap |
|-------------------|------------------|-------------|
| **Legal basis citation** | Correct reference to the Digital Medical Products Act – *법률 제 20722호* (article 40 for AI‑related provisions). | Source notes a mis‑cited law number in audit #930; the correct citation must be verified and reflected throughout all submission documents. |
| **Software lifecycle documentation** | IEC 62304–based development plan, verification/validation reports, change‑control logs, post‑market surveillance (PMS) plan. | No explicit mention in source – confirm completeness. |
| **Cybersecurity dossier** | • Threat analysis & risk mitigation plan<br>• Secure software update strategy<br>• SBOM (Software Bill of Materials) per the “디지털 의료제품법” SBOM pre‑check matrix referenced in the research log (`11_일일_리서치로그/...`). | Only a reference to an SBOM check list appears; full evidence not yet compiled. |
| **AI performance assessment** | • Dataset description, training/validation methodology<br>• Explainability & bias mitigation strategy<br>• Ongoing performance monitoring plan (per MFDS AI guidance). | No artifact cited – must be generated. |
| **Clinical evaluation** | • Clinical data (local or recognized foreign data that MFDS accepts under the latest notice)<br>• Benefit‑risk analysis aligned with article 40 of Law 20722. | Local clinical data not identified; need to confirm if foreign data can be leveraged under current MFDS scope expansion. |
| **Risk Management** | ISO 14971–compliant risk file, including cybersecurity and AI‑specific hazards. | Not referenced in source excerpts. |
| **Labeling & IFU (Korean language)** | Korean labeling, instructions for use, safety information, and declaration of compliance with the Digital Medical Products Act. | No evidence provided – must be prepared. |
| **Quality Management System (QMS) coverage** | Full MFDS‑approved QMS covering design/dev, cybersecurity, AI, and post‑market surveillance. Audit #930 flagged that the current audit scope omitted “Design Development / Cybersecurity” folders. | QMS documentation currently limited to a QMS folder; missing design & cyber folders must be added. |

---

### 3. Identified Missing Information & Action Items  

| Issue | Source Reference | Required Action |
|-------|------------------|-----------------|
| **Incorrect legal citation** – law number mis‑referenced in some documents (audit #930). | Excerpt [1] – “법률 제[0‑9]+호” pattern needs priority rule; audit notes an erroneous law number. | Verify the exact law reference (*법률 제20722호, article 40*) and update every regulatory document accordingly. |
| **Audit scope bias** – QMS audit only examined the QMS folder, omitting design development & cybersecurity folders. | Excerpt [1] – “설계개발/사이버보안 폴더 누락”. | Expand internal audit to include all relevant folders; ensure traceability to MFDS requirements for software lifecycle and cyber risk management. |
| **Superseded cross‑reference** – earlier research log cites the law but has not been updated after correction. | Excerpt [2] – “디지털의료제품법(법률 제20722호)” noted as superseded (v1.1). | Replace all legacy citations with the corrected version; document change in a revision log. |
| **SBOM pre‑check matrix** – referenced but not yet attached to submission. | Excerpt [2] – `11_일일_리서치로그/...` SBOM checklist. | Generate and attach a full SBOM compliant with MFDS cybersecurity expectations. |
| **AI performance documentation** – absent from current dossier. | None in source excerpts. | Prepare AI validation report, explainability analysis, and continuous monitoring plan. |

---

### 4. Key Risk Controls (aligned with Korean & International standards)

1. **Cybersecurity** – Adopt ISO/IEC 27001 controls; conduct regular penetration testing; enforce signed firmware updates.
2. **Software Validation** – Follow IEC 62304 lifecycle phases; maintain traceability matrix linking requirements → design → test results.
3. **AI Governance** – Implement IMDRF SaMD AI Algorithm Change Protocol (ALCP); document data provenance, bias mitigation, and post‑deployment performance monitoring.
4. **Human Factors** – Conduct usability testing in Korean clinical settings to ensure user interface clarity; incorporate feedback into IFU revisions.
5. **Post‑Market Surveillance** – MFDS‑required PMS plan with real‑time safety reporting (시판후조사) and periodic field safety corrective actions.

---

### 5. Citations

| Citation | Details |
|----------|---------|
| **Digital Medical Products Act** | “디지털의료제품법(법률 제20722호)”, specifically **Article 40** – source excerpt [2] (Cross‑Ref). |
| **Audit findings** | Audit #930 – mis‑cited law number and incomplete QMS folder coverage – source excerpt [1]. |
| **SBOM checklist reference** | `11_일일_리서치로그/2026-04-24_AI구성요소_디지털법매트릭스_SBOM사전점검.md` – source excerpt [2]; note that this file is a research log and not yet reflected in the official dossier. |
| **Identifier for foreign predicate/clearance** | *no specific identifier found in source — verify separately*. |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Reason & Escalation Path |
|-------------------|--------------------------|
| **Unresolved legal citation discrepancy** after two revision cycles | Escalate to Senior RA Manager → Legal Counsel for confirmation of the correct law reference. |
| **Inability to provide local clinical data within MFDS‑mandated timelines** (e.g., > 90 days) | Notify Project Lead & Regulatory Affairs Director; consider request for foreign data acceptance under latest MFDS notice. |
| **Audit #930 remediation not completed before submission deadline** | Elevate to Quality Assurance Head → initiate corrective action plan and request temporary extension from MFDS, if justified. |
| **AI performance gaps identified that could affect safety (e.g., bias risk > 5 %)** | Immediate escalation to Clinical Safety Officer and AI Governance Lead; pause submission until mitigation is documented. |
| **KGMP certification not secured for required hardware** | Notify Manufacturing Ops Lead; halt regulatory filing until KGMP audit passes. |

---

### 7. Peer‑Review Prompt  

> **Colleague, please review the following aspects of this draft:**  
> 1. **Assumptions about classification** – Is the inferred risk class (II vs III/IV) realistic based on the limited functional description? Should additional use‑case details be requested before finalizing the pathway?  
> 2. **Source coverage** – Do the excerpts adequately support all identified gaps, or are there other sections of the audit report that we might have missed (e.g., design history file, foreign clinical data acceptance)?  
> 3. **Jurisdiction‑specific gaps** – Are there any Korean regulatory nuances—such as mandatory pre‑market cybersecurity testing labs, or specific SBOM formatting requirements—that aren’t addressed here?  
> 4. **Evidence hierarchy** – Given MFDS’s recent notice expanding acceptable foreign clinical evidence, should we explicitly pursue a CE‑marked predicate or FDA 510(k) reference even though no identifier appears in the source?  

Please challenge any assumptions, suggest additional documentation needs, and flag any Korean‑specific compliance items that may still be absent. 

--- 

**End of Draft – Ready for internal review and incorporation of peer feedback.**

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

1. Chunk `101444507831075103`

> ## 영향 (규제 리스크) - **인증기관·심사원 신뢰도**: 사이버보안/SW수명주기/AI 성능평가 문서는 심사 시 최우선 열람 대상. 제정 법률번호 오기(그것도 완전히 다른 법률번호)는 문서 신뢰성 결정타. - **GMP 적합판정·품목허가**: 근거 법령 오기시 근거불명으로 지적 가능. - **audit #930 대응 실효성 부족 증거**: 자매문서 스캔 범위 편향(QMS 폴더로 국한, 설계개발/사이버보안 폴더 누락). Plan #935(sister-document cross-reference 자동화)의 grep 매칭룰에 "법률 제[0-9]+호" 패턴을 우선 룰로 편입 필요.

2. Chunk `1021227721792627871`

> ### 참고 (Cross-Ref) — 부수 인용 - `11_일일_리서치로그/2026-04-24_AI구성요소_디지털법매트릭스_SBOM사전점검.md` L20 "법률 제20722호 제40조" — 리서치로그(과거 시점 기록물)이나 관리표에 미반영 필요. - `12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md` L13 "디지털의료제품법(법률 제20722호)" — 교차검증 보고서. 정정 후 v1.1로 supersede 표기 필요.
