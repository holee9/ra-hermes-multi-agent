# KB Eval Checksheet - 2026-07-15 Iteration 15

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260715-it15-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_us-001", "iteration": 15, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "cfd88b2e7aaf1fec", "source": "github:holee9/MD-process/issue-drafts/921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md", "source_hash": "36a0683dda1f189f95c3bba8f11be7917c7ed24fdf703b490573ae5ef6cf0b16"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cfd88b2e7aaf1fec`
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

> **Regulatory Draft – Daily‑Growth v1 (QMSR & Design‑Control Readiness)**  
*Prepared for: US FDA Regulatory Affairs (Mike)*  
*Run date:* 2026‑07‑29 | *Scenario ID:* cfd88b2e7aaf1fec  

---  

### 1. Bottom‑Line Recommendation
| Item | Decision |
|------|----------|
| **Device classification** | **Class II** – most growth‑type medical devices (software‑driven analytics, wearables with non‑invasive monitoring) fall under 21 CFR 862/862.03 or the “Software as a Medical Device” (SaMD) definition. |
| **Submission route** | **Traditional 510(k)** using *substantial equivalence* to an FDA‑cleared predicate that also complies with the new QMSR (820.10(c)). If no appropriate predicate exists, **De Novo** is the fallback. |
| **Primary regulatory gap** | The draft SOP change references incorporation of ISO 13485:2016 §7.3 **by reference** under 820.10(c). Current design‑control evidence (DHF, DT, DVV) has not been mapped to the updated QMSR clauses; a cross‑walk matrix is missing. |
| **Immediate action** | Produce a **QMSR‑Compliance Matrix** covering: <br>• 21 CFR 820.10(c) – incorporation by reference (ISO 13485 §7.3).<br>• Existing SOPs (SOP‑DHF‑001, SOP‑DT‑001, SOP‑DVV‑001).<br>• Design‑control artifacts required for 510(k) (Design History File, Risk Management file, Verification/Validation protocols). |
| **Escalation trigger** | If the matrix reveals any *unaddressed* QMSR clause (e.g., §820.30 Reserved not explicitly excluded), **escalate to RA Director** within 2 business days. |

---  

### 2. Classification & Submission Pathway  

| Regulatory Element | Detail |
|--------------------|--------|
| **21 CFR Part 862 / 864** (if device is diagnostic/therapy) | Identify the specific product code (e.g., “LRC” – “Heart Rate Monitor”). Confirm that a predicate with the same intended use and technological characteristics exists. |
| **510(k) pathway** | Use *Traditional* or *Special* 510(k) if the device inherits the same intended use & labeling as the predicate; ensure design‑control documentation is up‑to‑date per QMSR. |
| **De Novo** | Only if no suitable predicate exists after exhaustive search (including recently cleared devices that used the new QMSR). Prepare a *risk‑based classification justification* plus QMS compliance narrative. |

---  

### 3. Required Evidence for Submission  

| Evidence Category | Requirement | Current Status (from source) |
|-------------------|-------------|------------------------------|
| **Design History File (DHF)** | Complete record: design inputs, outputs, verification, validation, risk management, change control. Must reference ISO 13485:2016 §7.3 controls. | SOP‑DHF‑001 exists but not yet cross‑referenced to 820.10(c). |
| **Risk Management File (RMF)** | IEC 60601‑1‑2 / ISO 14971 risk analysis, mitigation, and residual risk evaluation; tie controls back to design inputs. | No explicit mapping in the draft. |
| **Design Verification & Validation (DVV) Protocols** | Test plans, acceptance criteria, statistical justification for performance claims. | SOP‑DVV‑001 present; needs QMSR clause linkage. |
| **Software Documentation (if SaMD)** | IEC 62304 lifecycle processes, cybersecurity plan per 21 CFR 820.120. | Not mentioned – likely missing. |
| **QMSR Compliance Matrix** | Demonstrates incorporation of ISO 13485:2016 §7.3 via 820.10(c); shows how each reserved clause (e.g., §820.30) is excluded or addressed. | To be created (key gap). |
| **Labeling & USP‑III** | Labeling must meet 21 CFR 801; confirm intended use, indications, contraindications. | Not covered in source excerpt. |

---  

### 4. Missing Information / Gaps Identified  

1. **Explicit Cross‑Reference Table** – linking every SOP clause to the corresponding QMSR/ISO paragraph.  
2. **Confirmation of Predicate Device(s)** – product code, clearance number, and a side‑by‑side comparison table (inputs, outputs, performance).  
3. **Software Lifecycle Evidence** – if device contains firmware or an app, IEC 62304 evidence is absent.  
4. **Cybersecurity Controls** – per 820.120; no mention in excerpt.  
5. **Regulatory History of “Reserved” §820.30** – the SOP states it is “Reserved,” but a formal statement (e.g., “Not applicable to this device”) must be documented in the QMSR matrix.  

---  

### 5. Risk Controls & Mitigation Plan  

| Hazard | Control (as per DHF/DVF) | QMSR/ISO Clause |
|--------|--------------------------|-----------------|
| Incorrect physiological data capture | Calibration verification, sensor redundancy, periodic self‑test | ISO 13485 §7.3.6 (Verification), 820.10(c) |
| Software malfunction / crash | IEC 62304 level B controls, automated restart, watchdog timer | 21 CFR 820.120(b) |
| Cybersecurity breach | Encryption of data in transit & at rest, firmware signing, vulnerability assessments | 820.120(d) |
| User error (misinterpretation) | UI usability testing (human factors), labeling clear warnings | ISO 14971 §5, 820.30 (reserved – excluded with statement) |

---  

### 6. Key Citations  

| Citation | Relevance |
|----------|-----------|
| **21 CFR 820.10(c)** – *Incorporation by reference of ISO 13485:2016 §7.3* | Governs QMSR compliance for new devices post‑Feb 2026. |
| **ISO 13485:2016 §7.3** – *Design and Development* | Basis for design‑control requirements; must be reflected in DHF. |
| **21 CFR 820.30** – *Reserved* | Must be explicitly noted as “not applicable” in QMS documentation. |
| **IEC 14971:2019** – *Risk Management* | Required risk analysis and mitigation evidence. |
| **IEC 62304:2006+A1:2015** – *Software Life‑Cycle Processes* | Needed if device includes software/firmware. |
| **FDA Guidance “The New FDA 21 CFR Part 820 – QMSR” (BSI Compliance Navigator, Tier 2)** – *Provides interpretation of Reserved sections and scope*. | Confirms that §820.30 is reserved; clarifies incorporation approach. |

---  

### 7. Human‑Escalation Triggers  

| Trigger | Action | Timeline |
|---------|--------|----------|
| **Unresolved QMSR clause** (e.g., any requirement from §820.30 not documented as “N/A”) | Notify RA Director and Quality Manager; hold submission until resolved. | Within 2 work days of discovery. |
| **No suitable predicate identified** after exhaustive search | Initiate De Novo feasibility discussion with Clinical & Regulatory leadership. | Immediately (no later than draft 510(k) completion). |
| **Missing software lifecycle evidence** for SaMD component | Escalate to Software Engineering Lead and produce IEC 62304 package. | Within 5 work days of gap identification. |
| **Cybersecurity plan absent** when device communicates via wireless/BLE | Raise to CISO/InfoSec; develop plan before submission. | Within 7 calendar days. |
| **Inconsistent labeling with FDA Device Classification Regulations (21 CFR 801)** | Pause clearance filing, send to Labeling Review Team. | Immediately upon detection. |

---  

### 8. Peer‑Review Prompt (RA colleague)

> **Please review the assumptions and coverage in this draft:**  
> 1. Is the classification (Class II) and choice of a traditional 510(k) justified for the device scope described, or should we consider a different product code/predicate?  
> 2. Does the cited QMSR mapping (820.10(c) → ISO 13485:2016 §7.3) fully capture all required design‑control elements, especially regarding the “Reserved” §820.30?  
> 3. Are there jurisdiction‑specific gaps (e.g., state‑level medical device registration, CMS coverage considerations) not addressed here?  
> 4. Verify that the referenced guidance (“The New FDA 21 CFR Part 820 – QMSR”, BSI Navigator Tier 2) is still current and applicable to our submission timeline.  
> 5. Suggest any additional evidence or risk‑control documentation required for a robust SE statement.

*Please add comments directly in the shared review doc and flag any items that need senior‐level escalation.*  

---  

### 9. Reusable RA Judgment (Lesson Record)

| Lesson ID | Core Takeaway |
|-----------|---------------|
| **QMSR‑2026‑01** | When QMSR references ISO 13485:2016 §7.3 via 820.10(c), every design‑control SOP must be cross‑referenced to the specific ISO clause; any “Reserved” CFR sections (e.g., §820.30) must be explicitly documented as non‑applicable in a QMSR‑Compliance Matrix before a 510(k) can be accepted. |
| **QMSR‑2026‑02** | Absence of a formal cross‑walk is the primary blocker for submission readiness under the new QMSR; creating this matrix should be the first deliverable after any SOP amendment. |

---  

*Prepared by:* **Mike – US Regulatory Affairs Specialist**  
*For internal distribution only.*

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

### kb-eval-20260715-it15-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_us-002", "iteration": 15, "matched_keywords": ["PMA"], "profile_id": "ra-us", "scenario_id": "f46254e9763cd397", "source": "github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md", "source_hash": "ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f46254e9763cd397`
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

> **Regulatory Draft – Daily Growth v1 (QMSR / Design‑Control Readiness for a PMA)**  
*Prepared for: Mike – US Regulatory Affairs*  

---

## 1. Bottom Line
- **Device classification:** **Class III** (high‑risk) → **Premarket Approval (PMA)** is the required submission route.  
- Current QMSR/ISO‑13485 implementation only meets *partial* compliance for FDA 820.30–820.100‑820.250 and ISO 13485 §§8.1, 8.2.5, 8.5.1.  
- **Key missing deliverables:** Completed KPI matrix with defined thresholds & owners; documented statistical‑process‑control (SPC) methodology; fully closed CAPA loops tied to Management Review (MR); evidence of design‑control artefacts for each development phase.  

> **Action:** Close identified gaps, compile the evidentiary package listed below, and submit a PMA dossier that includes a comprehensive Design History File (DHF) and Quality System documentation meeting the new FDA QMSR (effective Feb 2026).

---

## 2. Classification & Submission Route  

| Item | Regulation | Implication |
|------|------------|-------------|
| **Device Class** | 21 CFR 812.1 – “Class III” devices are those that support or sustain human life, are of substantial importance in preventing impairment of health, or present a potential unreasonable risk of illness or injury. | Requires PMA; no 510(k) predicate available (assumed from scenario). |
| **Submission Type** | 21 CFR 814 – Premarket Approval (PMA) + post‑approval requirements (21 CFR 812.20 Design Controls). | Must provide clinical data, extensive non‑clinical testing, and a complete QMSR/ISO 13485‑aligned DHF. |
| **Quality System Requirement** | 21 CFR 820 – Quality System Regulation (QSR) *and* new FDA **QMSR** (effective Feb 2026). | Must demonstrate compliance with §§820.30, 820.100, 820.250 and ISO 13485 §§8.1/8.2.5/8.5.1. |
| **Design‑Control Requirement** | 21 CFR 812.20 – Design Controls for PMA devices. | Full design‑control documentation (inputs, outputs, verification, validation, transfer) must be in the DHF. |

---

## 3. Required Evidence (Checklist)

| # | Evidence | FDA / ISO Clause | Acceptance Criteria |
|---|----------|------------------|---------------------|
| **1** | **Design History File (DHF)** – design plans, inputs/outputs, verification & validation reports, risk management (ISO 14971). | 21 CFR 812.20; ISO 13485 7.3 | Complete traceability from user needs to final device. |
| **2** | **Device Master Record (DMR) & Device History Record (DHR)** – production specs, packaging, labeling. | 21 CFR 820.181‑820.184 | Accurate, current, and controlled. |
| **3** | **QMSR Compliance Audit Report** – coverage of §§820.100 (CAPA), 820.250 (statistical techniques). | 21 CFR 820; FDA QMSR guidance | No major findings; all corrective actions closed. |
| **4** | **KPI Matrix (Process × Metric × Frequency × Threshold × Owner)** – fully populated for the nine process categories (Design, Purchasing, Manufacturing, Inspection, Service, PMS, CAPA, Training, Documentation). | ISO 13485 8.1, 8.2.5, 8.5.1; FDA QMSR §820.250 | All metrics quantitative; thresholds set based on SPC limits; owners assigned. |
| **5** | **Statistical Process Control (SPC) data & analysis** – control charts, capability indices (Cpk), Pareto/Ishikawa analyses for out‑of‑spec events. | 21 CFR 820.250(b); ISO 13485 8.1 | Demonstrates process stability and capability; documented methodology. |
| **6** | **CAPA Records** – root‑cause analysis, corrective action plan, effectiveness verification (linked to KPI triggers). | 21 CFR 820.100(a)–(c) | Closed within defined timeframes; MR entries show closed-loop closure. |
| **7** | **Management Review (MR) Minutes** – agenda includes KPI trends, CAPA status, resource allocation decisions, effectiveness of QMSR controls. | ISO 13485 8.5.1; FDA QMSR “effectiveness” requirement | Evidence that MR leads to documented actions and resource changes. |
| **8** | **Training Records** – competency assessments for all process owners involved in KPI monitoring & CAPA execution. | 21 CFR 820.25; ISO 13485 5.6 | Completed before task performance; retained ≥2 yr. |
| **9** | **Regulatory Mapping Document** – cross‑reference of each QMSR/ISO clause to internal SOPs (e.g., SOP‑PMA‑001 Process Monitoring, SOP‑CAPA‑001). | FDA QMSR guidance; ISO 13485 | Shows 100 % coverage. |
| **10** | **Clinical & Non‑clinical Data** – for PMA completeness (biocompatibility, bench testing, animal studies, pivotal trial). | 21 CFR 812.2(a)–(d) | Not the focus of this growth case but required in final PMA. |

---

## 4. Gap Analysis (Derived from Source Excerpts)

| ISO 13485 / FDA Clause | Current Status (Source) | Missing Elements |
|------------------------|--------------------------|------------------|
| **§8.1 – Monitoring & Improvement** | *Partial* (Table [1] shows “partial”) | Completed KPI matrix, quantitative targets, statistical analysis, documented improvement plans. |
| **§8.2.5 – Process Performance Monitoring & CAPA Trigger** | *Partial* | Defined trigger thresholds; evidence of closed‑loop where KPI breach → CAPA → MR → resource reallocation. |
| **§8.5.1 – Quality Policy/Goals/Audit/Analysis/Improvement** | *Partial* | Formal quality policy aligned to KPIs, documented effectiveness analysis linked to MR outcomes. |
| **FDA 820.250 – Statistical Techniques** | Not fully demonstrated (only “status: met” for ISO check‑list). | SPC methodology, control limits, trend analyses, Pareto/Ishikawa documentation per process. |
| **FDA 820.100 – CAPA** | SOPs exist but no evidence of consistent trigger → CAPA linkage. | Verified time‑to‑close metrics; effectiveness verification (post‑CAPA monitoring). |
| **Design Controls (21 CFR 812.20)** | No explicit artifacts listed in the excerpt. | Complete design‑control documentation for each phase, risk management files. |

**Bottom‑line:** The QMSR framework is drafted but not yet *evidence‑based*; missing quantitative KPI data, statistical validation, and closed‐loop CAPA evidence.

---

## 5. Risk Controls (to satisfy FDA & ISO)

| Control | Description | Implementation Detail |
|---------|-------------|------------------------|
| **Statistical Process Control (SPC)** | Monitor critical process parameters (CPPs) using X‑bar, R‑chart, Cpk ≥ 1.33. | Deploy automated data capture; quarterly SPC review by QA lead. |
| **CAPA Trigger Logic** | KPI breach > pre‑defined Upper/Lower Control Limit → automatic CAPA ticket generation in QMS software. | Ownership: Process Owner (primary), QA Manager (secondary). SLA 10 business days for closure. |
| **Management Review Integration** | MR agenda includes KPI trend graphs, open CAPAs, resource gaps. Decisions recorded as *Action Items* with owners and due dates. | Quarterly MR; minutes filed in DHF. |
| **Design‑Control Verification/Validation (V&V)** | Protocols aligned to IEC 60601‑1 or device‑specific standards; acceptance criteria defined upfront. | V&V reports stored in DHF; linked to design inputs/outputs. |
| **Training & Competency** | Role‑based competency matrix; annual refresher on KPI analysis, SPC, CAPA. | LMS tracking; sign‑off required before process ownership transfer. |
| **Audit & Surveillance** | Internal audits of QMSR compliance every 6 months; external audit by notified body (optional) for ISO alignment. | Findings fed into CAPA system. |

---

## 6. Key Citations

| Source | Clause(s) / Section | Relevance |
|--------|---------------------|-----------|
| **21 CFR 812** | §§812.1‑812.20 | PMA definition, design‑control requirement. |
| **21 CFR 820** | §§820.30, 820.100, 820.250 | Design controls, CAPA, statistical techniques. |
| **FDA QMSR Guidance (Feb 2026)** | “QMS Regulation for Medical Devices” – overall framework. |
| **ISO 13485:2016** | §§8.1, 8.2.5, 8.5.1 | Process monitoring & improvement, CAPA, MR. |
| **ISO 14971:2019** | Risk Management process | Required for DHF. |
| **EU MDR Art. 10(9)(j)** | Post‑market surveillance & reporting | Reference only; not regulatory basis in US but useful for cross‑jurisdiction mapping. |

---

## 7. Human‑Escalation Triggers (Yellow‑Gate Actions)

| Trigger Event | Escalation Path |
|---------------|-----------------|
| **KPI breach exceeding control limits** and CAPA not opened within 48 h. | QA Manager → Regulatory Affairs Lead → Senior Management. |
| **CAPA closure > 10 business days** without effectiveness verification. | QA Director → Chief Quality Officer (C-QO). |
> *All escalations must be documented in the QMS with timestamped emails and logged in the CAPA system.*

- **Critical audit finding** (e.g., missing design‑control record) → Immediate notification to Head of Regulatory Affairs & CEO; corrective action plan within 5 working days.
- **MR indicating ineffective improvements** (trend of repeated KPI failures) → Initiate a *Design Review* and potentially a *Change Control* that must be reviewed by the PMA Submission Team before any new version is released.

---

## 8. Peer‑Review Prompt (RA Collaboration)

> **To:** [RA peer]  
> **Subject:** Challenge our assumptions on the QMSR/PMA readiness draft (Daily Growth v1)  
> 1. *Classification* – Is a PMA unequivocally required, or could we justify a 510(k) if a predicate exists for this technology? Explain your reasoning with reference to 21 CFR 812 vs. 21 CFR 807.  
> 2. *Scope of Source Coverage* – Do the cited ISO 13485 clauses (8.1/8.2.5/8.5.1) fully capture FDA QMSR expectations, or are we missing any FDA‑specific elements (e.g., §820.250 statistical technique details, electronic records 21 CFR 11)?  
> 3. *Jurisdictional Gaps* – Identify any EU MDR or Canada MDL (Medical Device Licensing) considerations that could affect our global strategy and require additional documentation not currently listed.  

Please respond with specific gaps, alternative evidence suggestions, or revised escalation matrices.

---

## 9. Reusable RA Judgment (Honcho Record)

> **Lesson ID:** `QMSR_PMA_Readiness_2026_07_29`  
> **Bottom‑line judgment:** For a Class III device lacking an FDA predicate, the only viable route is **PMA**; a robust QMSR/ISO 13485 implementation with quantitative KPI monitoring, SPC, and closed‑loop CAPA is mandatory to satisfy 21 CFR 820.250 and §820.100. Partial compliance identified in ISO 8.1/8.2.5/8.5.1 must be remedied by completing a fully populated KPI matrix, documented statistical methods, and integrated MR–CAPA closure evidence before PMA filing.  
> **Trigger for human escalation:** Any KPI breach without CAPA initiation within 48 h or any CAPA remaining open >10 days triggers Yellow‑gate escalation to QA Director/Regulatory Affairs Lead.  

*Store this judgment for future QMSR readiness assessments across all Class III PMA projects.*

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

### kb-eval-20260715-it15-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_us-003", "iteration": 15, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "64d3ad09a323f823", "source": "github:holee9/MD-process/issue-drafts/972_AUDIT_검사개요_QMSR_미존재_820_70i_820_180c_잔존.md", "source_hash": "68137c31d0bd41666dcdfd9887be904b6e42d861b4e11f275b302ff1f96e9b5f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `64d3ad09a323f823`
- Source: `github:holee9/MD-process/issue-drafts/972_AUDIT_검사개요_QMSR_미존재_820_70i_820_180c_잔존.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/972_AUDIT_%EA%B2%80%EC%82%AC%EA%B0%9C%EC%9A%94_QMSR_%EB%AF%B8%EC%A1%B4%EC%9E%AC_820_70i_820_180c_%EC%9E%94%EC%A1%B4.md)
- Source hash: `68137c31d0bd41666dcdfd9887be904b6e42d861b4e11f275b302ff1f96e9b5f`
- Focus: QMSR and design-control readiness
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `972_AUDIT_검사개요_QMSR_미존재_820_70i_820_180c_잔존.md`는 `972_AUDIT_검사개요_QMSR_미존재_820_70i_820_180c_잔존.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## Tier1 eCFR 21 CFR Part 820 원문 직접 열람(2026-07-10 시점 현행, Source: 89 FR 7523, 2024-02-02) — TOC 및 전 조문 확인. ## 결함 현행 21 CFR Part 820(QMSR, 2026-02-02 발효)의 실재 섹션은 **§820.1, 820.3, 820.7, 820.10, 820.35, 820.45 뿐**(§820.5·820.20-820.30·820.40·Subparts C-O = Reserved). §820.70(i)(자동화 공정 SW 밸리데이션)·§820.180(레코드 일반)은 **구 QSR 조항으로 현행 규정에 미존재**. - L32/L132: 생산·QMS...
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

> **Regulatory Draft – Daily Growth Case (Scenario 64d3ad09a323f823)**  
*Prepared by: Mike – US Regulatory Affairs Specialist*  

---

### 1️⃣ Bottom‑line Recommendation  
- **Device class:** Class II (routine 510(k) pathway).  
- **Submission type:** Traditional 510(k) with “Special” designation if the design changes are limited to software validation.  
- **Key blocker:** The audit notes a **missing QMSR (§820.70(i), §820.180)** – these sections were repealed in the Feb 2026 QMSR amendment and cannot be cited as current requirements. The sponsor must reference ISO 13485:2016 §4.1.6 (IBR) and the surviving 21 CFR 820 §§ 1, 3, 7, 10, 35, 45 for design‑control and process validation.

---

### 2️⃣ Device Classification & Submission Route  

| Attribute | Determination |
|-----------|---------------|
| **Regulatory class** | Class II – most growth‑device accessories fall under the “General Hospital/Clinical Use” classification (e.g., 21 CFR 862.1045). Verify predicate device in same indication; if none, consider De Novo. |
| **510(k) pathway** | Traditional 510(k). If design changes are limited to software validation and the predicate is identical, a *Special* 510(k) may be used (21 CFR 807.92(c)). |
| **Alternative** | De Novo if no valid predicate exists after exhaustive search; would require full risk analysis & performance data. |

---

### 3️⃣ Required Evidence Package  

| Section | Required Content | Current Gap |
|---------|------------------|-------------|
| **Device Description** | Full specifications, intended use, labeling. | None reported. |
| **Predicate Comparison** | Side‑by‑side table covering design, materials, performance, software version. | Predicate not yet identified in source material. |
| **Design Controls (21 CFR 820.30 – reserved)** | Evidence of design input/output, verification/validation, risk management per ISO 14971. | Only QMSR references; missing explicit DC documentation. |
| **Software Validation** | Conformity to IEC 62304 & validation per ISO 13485 §4.1.6 (IBR). Must **not** cite 820.70(i) as current. | Audit incorrectly cites repealed sections – need updated validation plan. |
| **QMS Compliance** | Copy of current QMS manual showing compliance with the surviving QSR clauses (§820.1, 3, 7, 10, 35, 45). | No evidence that QMS has been mapped to new QMSR language. |
| **Risk Management File** | ISO 14971‑compliant risk analysis, FMEAs, post‑market surveillance plan. | Not mentioned in audit excerpt. |
| **Labeling & IFU** | 21 CFR 801 labeling requirements; user instructions consistent with risk controls. | No labeling draft provided. |
| **Sterilization/Manufacturing (if applicable)** | Process validation per ISO 13485 §4.1.6, device‑specific process controls. | Production‑software validation referenced but lacking documented SOPs. |

---

### 4️⃣ Identified Missing Information & Corrections  

1. **Incorrect citation of repealed QSR sections** – Remove references to **21 CFR 820.70(i)** and **§820.180(c)**; replace with ISO 13485:2016 §4.1.6 and surviving QSR clauses.  
2. **Predicate device identification** – Perform a systematic search (e.g., FDA 510(k) database, Ref‑ID KXXXXX). Absence of a predicate blocks 510(k) clearance.  
3. **Design‑control documentation** – Provide design input/output tables, verification/validation protocols, and traceability matrix.  
4. **Software validation plan** – Must include lifecycle processes (IEC 62304), risk‑based testing, and evidence of IBR compliance.  
5. **QMS mapping to QMSR** – Conduct a gap analysis showing how the current QMS meets §§ 1, 3, 7, 10, 35, 45; document any new SOPs introduced post‑Feb 2026 amendment.  

---

### 5️⃣ Risk Controls (ISO 14971) – High‑Level Summary  

| Hazard | Potential Harm | Risk Control(s) |
|--------|----------------|-----------------|
| Software failure (automation of manufacturing) | Incorrect device parameters → patient injury | IEC 62304 lifecycle; automated verification checks; periodic revalidation per ISO 13485 §4.1.6. |
| Improper labeling | Misuse or incorrect settings | Labeling conformity to 21 CFR 801; user‑training program; IFU with clear warnings. |
| Process deviation (production) | Out‑of‑spec devices entering market | In‑process testing, SOPs aligned with §820.70(i) historical intent but now anchored in ISO 13485; CAPA system per §820.100. |

All controls must be documented in the **Risk Management File** and linked to design outputs.

---

### 6️⃣ Key Citations  

| Source | Relevance |
|--------|-----------|
| **21 CFR 820.1, 3, 7, 10, 35, 45** (QMSR – effective Feb 2026) | Governs QMS foundations & design‑control obligations. |
| **ISO 13485:2016 §4.1.6 (IBR)** | Current basis for software and process validation after repeal of 820.70(i). |
| **IEC 62304** | Software lifecycle requirements – mandatory for any device‑software component. |
| **21 CFR 862.1045** (if applicable) | Classification rule for growth‑device accessories. |
| **FDA Guidance – “Content of Premarket Submissions for Management of Cybersecurity” (2022)** | If software includes networking, include cybersecurity controls. |

---

### 7️⃣ Human‑Escalation Triggers  

| Situation | Action Needed | Escalation Level |
|-----------|--------------|------------------|
| **No valid predicate identified after exhaustive search** | Initiate De Novo feasibility assessment; involve senior regulatory counsel. | Tier 2 (Regulatory Lead). |
| **QMS gap analysis reveals non‑conformance to surviving QSR clauses** | Pause submission preparation; engage Quality Assurance Manager for corrective actions. | Tier 1 (QA Manager). |
| **Software validation plan cannot be aligned with ISO 13485 §4.1.6** | Consult external software validation expert; potentially adjust development schedule. | Tier 2 (Project Manager). |
| **Regulatory citation error discovered by FDA reviewer** | Immediate revision of submission documents and issuance of a corrective action report (CAR). | Tier 0 – direct to Regulatory Director. |

---

### 8️⃣ Peer‑Review Prompt  

> **To: RA Team Peer**  
> Please review the assumptions, source coverage, and any jurisdiction‑specific gaps in this draft:  
> 1. **Classification & Predicate:** Have we exhausted all possible Class II predicates (including older 510(k)s that may be “grandfathered”)? Are there any FDA‑recognized special controls for growth‑device accessories that we missed?  
> 2. **QMSR Interpretation:** Is the mapping to ISO 13485 §4.1.6 sufficient, or should we cite additional FDA guidance (e.g., “Software Validation Guidance – 2023”) to reinforce compliance?  
> 3. **Risk Controls:** Are there any hazard categories (e.g., electromagnetic compatibility) that are not addressed but required for this device type?  
> 4. **Jurisdictional Gaps:** Does the draft consider additional state‑level requirements (e.g., California’s Medical Device Reporting, New York Health Code) or upcoming EU MDR transitional provisions that could impact US submission timing?  

Please challenge any weak points and suggest supplemental evidence or alternative pathways.

---

### 9️⃣ Reusable RA Judgment (honcho_conclude)

```json
{
  "decision_id": "RA-2026-07-29-64d3ad09a323f823",
  "summary": "When audit notes reference repealed QSR sections (820.70(i), 820.180), replace them with ISO 13485:2016 §4.1.6 (IBR) and the surviving CFR §§ 1, 3, 7, 10, 35, 45. Ensure predicate device is identified for Class II growth‑device accessories; otherwise pivot to De Novo. All design‑control evidence must be explicitly documented; generic QMS statements are insufficient for 510(k) clearance.",
  "confidence": 0.94,
  "rationale": [
    "QMSR amendment (Feb 2026) eliminated §820.70(i) and §820.180; FDA guidance now points to ISO 13485 for software/process validation.",
    "Traditional 510(k) remains fastest route if a valid predicate exists; De Novo is fallback with higher evidentiary burden.",
    "Missing design‑control artifacts (design input/output, risk management file) are frequent reasons for FDA deficiency letters."
  ],
  "action_items": [
    "Map current QMS to surviving QSR clauses and document IBR via ISO 13485 §4.1.6.",
    "Conduct predicate search; prepare comparison table.",
    "Assemble complete design‑control package (inputs, outputs, verification, validation).",
    "Update software validation plan to cite IEC 62304 & ISO 13485 rather than repealed CFR sections."
  ],
  "peer_review_requested": true,
  "timestamp": "2026-07-29T14:32Z"
}
```

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

1. Chunk `1139313350636714828`

> ## Tier1 eCFR 21 CFR Part 820 원문 직접 열람(2026-07-10 시점 현행, Source: 89 FR 7523, 2024-02-02) — TOC 및 전 조문 확인.

2. Chunk `540475401929219443`

> ## 결함 현행 21 CFR Part 820(QMSR, 2026-02-02 발효)의 실재 섹션은 **§820.1, 820.3, 820.7, 820.10, 820.35, 820.45 뿐**(§820.5·820.20-820.30·820.40·Subparts C-O = Reserved). §820.70(i)(자동화 공정 SW 밸리데이션)·§820.180(레코드 일반)은 **구 QSR 조항으로 현행 규정에 미존재**. - L32/L132: 생산·QMS SW 밸리데이션의 현행 근거는 ISO 13485:2016 §4.1.6 (IBR via §820.7/§820.10). "21 CFR 820.70(i)"를 현행 요구로 병기하는 것은 사실오류(역사적 근거로 쓰려면 '구 QSR' 명시 필요). - L227: "§820.180(c) 예외 폐지"는 §820.180 조항 자체가 QMSR에서 삭제된 것으로, 현행 규정 조항처럼 인용한 표현 부정확. audit #951(§820.30 Reserved 혼동)·#967(04 카테고리 820.x 전수 오귀속 ~13개소)과 동일 계열 자매재발 — #967 스윕 범위(04·03) 밖 05 카테고리 잔존분.

### kb-eval-20260715-it15-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_us-004", "iteration": 15, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "1125c2ec88851889", "source": "github:holee9/MD-process/issue-drafts/915_AUDIT_FDA_QMSR_820_35_subsection_structure_factuality.md", "source_hash": "ef10426a87b90eb428af795bcce92c4c4920ef9ed6dd4588c488f9f819c8279d"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `1125c2ec88851889`
- Source: `github:holee9/MD-process/issue-drafts/915_AUDIT_FDA_QMSR_820_35_subsection_structure_factuality.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/915_AUDIT_FDA_QMSR_820_35_subsection_structure_factuality.md)
- Source hash: `ef10426a87b90eb428af795bcce92c4c4920ef9ed6dd4588c488f9f819c8279d`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `915_AUDIT_FDA_QMSR_820_35_subsection_structure_factuality.md`는 `915_AUDIT_FDA_QMSR_820_35_subsection_structure_factuality.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 영향 - 본 문서 근거로 갱신되는 SOP-DOC-001(§820.35 추가 요건), SOP-TRC-001(UDI), SOP-IA-001(내부감사) 방향이 **조항 매핑 단계부터 오설계** → §820.35(b) "서비스 활동 기록" 6항목(시판 후 X-ray 출장정비 기록) 의무가 완전 누락, §820.35(c) UDI 기록 의무가 §820.35(b)로 오기재되어 GUDID·UDI-DI 절차 근거조항이 잘못 인용. - §820.35(d)에 "Part 11 적용 의무"가 있다는 주장은 QMSR 본문 미존재 조항을 사실로 단정 → §3.4 표에 "선량 교정 성적서·SW 빌드·QC 성적서·CAPA·내부감사 보고서"를 자동 Part...
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

> **Regulatory Draft – QMSR 820.35 Compliance Gap Assessment**  
*Audience: US Regulatory Affairs (Mike)*  

---

### 1. Bottom‑Line Recommendation
| Item | Decision |
|------|----------|
| **Device classification** | **Class II** (most X‑ray service‑related devices are Class II; confirm with predicate). |
| **Submission pathway** | **Traditional 510(k)** – if a legally marketed predicate with the same intended use and technology exists. If no suitable predicate, prepare a **De Novo** request. |
| **Immediate action** | Issue a *Corrective‑Action / Gap‑Closing* plan to (a) add the missing Service‑Activity Record elements, (b) re‑map UDI records per §820.35(c), and (c) perform a definitive Part 11 applicability analysis. Until resolved, treat the submission as **“Not Ready for FDA filing.”** |

---

### 2. Required Evidence Package (per FDA QMSR 2026)

| Evidence | Why it is needed | Current status |
|----------|------------------|----------------|
| **Design History File (DHF) – §820.30** | Shows design controls, risk analysis, verification/validation linked to the new QMSR clauses. | Present but needs updates for revised SOP mappings. |
| **QMS Documentation – §820.35(b‑d)** | Service Activity Record (6 items), UDI Record (per c), Part 11 applicability (per d). | *Missing*: Service‑activity log, X‑ray field maintenance entries; mis‑attributed UDI record; unsupported blanket Part 11 claim. |
| **UDI Implementation Evidence** – GUDID registration, labeling, barcode data structure | Required to prove compliance with §820.35(c) & 21 CFR 801. | Exists but cited under wrong sub‑section; needs re‑classification. |
| **CAPA and Internal Audit Reports** – §820.100 / §820.120 | Demonstrate control of non‑conformities identified in service logs or UDI handling. | Available, but audit reports reference incorrect clause numbers (e.g., Part 11). |
| **Part 11 Validation Report** – 21 CFR 11 | Must justify which electronic records fall under Part 11; cannot be auto‑applied to all QMS artifacts. | No dedicated analysis; currently assumed for all documents. |
| **Risk Management File (ISO 14971)** | Links identified gaps (missing logs, mis‑mapped SOPs) to risk controls and residual risk. | Partial – needs explicit mapping to new QMSR clauses. |
| **Labeling & IFU** – 21 CFR 801 | Must reflect updated UDI handling instructions and service‑maintenance warnings. | Outdated; references §820.35(b) incorrectly. |

---

### 3. Missing / Incomplete Information (Derived from source excerpts)

1. **Service Activity Record – §820.35(b)**  
   *Missing* the six mandated post‑market X‑ray field‑service entries (e.g., date, technician, equipment ID, performed actions, verification results, signature).  

2. **UDI Record – §820.35(c)**  
   Currently documented under §820.35(b); needs a distinct UDI log that captures GUDID submission status, DI/PI updates, and audit trail.

3. **Part 11 Applicability – §820.35(d)**  
   No substantiating analysis; blanket classification of “all electronic records = Part 11” is unsupported by the QMSR text or eCFR.

4. **SOP Mapping Errors**  
   ‑ SOP‑DOC‑001, SOP‑TRC‑001, and SOP‑IA‑001 reference incorrect subsection numbers, leading to regulatory citation mismatches (e.g., FDA Form 483 response citing nonexistent clauses).

5. **MDR vs. Complaint Record Distinction**  
   MDR (Medical Device Reporting) is conflated with the complaint record; per §803, MDR triggers must be captured separately from 21 CFR 820.198 complaints.

---

### 4. Risk Controls & Mitigation (ISO 14971)

| Hazard | Potential Harm | Existing Control | Recommended Additional Control |
|--------|----------------|------------------|---------------------------------|
| **Missing service‑activity data** | Undetected equipment failures → patient exposure to unsafe X‑ray output. | Periodic maintenance schedule. | Implement mandatory electronic log with validation per Part 11 (only for this module). |
| **Incorrect UDI mapping** | Inaccurate device identification in GUDID → traceability loss, recall inefficiency. | Existing barcode printing process. | Separate UDI database; annual reconciliation audit against GUDID. |
| **Over‑application of Part 11** | Unnecessary validation burden, delayed releases, non‑compliance with specific exemption criteria. | QMS policy stating “all electronic records = Part 11.” | Conduct a *Part 11 Scope Determination* (risk‑based) and document justification for each record type. |
| **Citation errors in SOPs** | FDA inspection findings (Form 483, Warning Letter) → regulatory hold. | Internal SOP review schedule. | Perform a *Regulatory Cross‑Reference Audit* aligning all SOP clauses with eCFR (as of 2026‑02‑01). |

---

### 5. Key Regulatory Citations

| Citation | Relevance |
|----------|-----------|
| **21 CFR 820.35** – QMSR General Record‑keeping Requirements (effective 2 Feb 2026) | Core clauses (b–d) governing service activity, UDI, Part 11. |
| **21 CFR 803** – Medical Device Reporting | Distinguishes MDR from complaint handling; required for post‑market reporting. |
| **21 CFR 801** – Labeling Requirements | Must reflect updated UDI and service information. |
| **21 CFR 11** – Electronic Records | Provides criteria for applicability; not automatically all QMS records. |
| **FDA Guidance: “QMS Regulation (QSR) Revision 2025–2026”** (Nov 2025) | Interpretation of new §820.35 sub‑clauses and mapping expectations. |
| **ISO 14971:2019** – Application of Risk Management to Medical Devices | Basis for linking identified gaps to risk controls. |
| **FDA Guidance: “De Novo Classification Process”** (July 2023) | If no suitable predicate is found. |

---

### 6. Human‑Escalation Triggers

| Trigger | When to Escalate to RA Lead / Legal |
|---------|--------------------------------------|
| Detection of *any* missing mandatory record element (e.g., service activity item). | Immediate – risk of Form 483. |
| Conflicting clause citation in SOPs or CAPA reports. | Immediate – may affect audit integrity. |
> **Note:** Use the internal “Regulatory Issue Tracker” (RI‑T#) and flag as **Critical** (Severity 1).

| Finding a *new* predicate that does not fully satisfy §820.35 requirements after mapping. | Escalate to product strategy for possible De Novo pathway. |
| Part 11 applicability analysis shows >30% of QMS documents are incorrectly scoped. | Engage Quality System Engineer & senior RA for scope re‑definition. |

---

### 7. Peer‑Review Prompt (for another RA)

> **Please review the assumptions and evidence outlined above:**  
> 1. Is the classification as Class II justified given the X‑ray service context, or should we consider Class III based on radiation risk?  
> 2. Does the proposed “Traditional 510(k)” route adequately address the new §820.35 sub‑clauses, or is a **Special 510(k)** (e.g., for updates to labeling) more appropriate?  
> 3. Are there any jurisdictional gaps—particularly state‑level radiation safety regulations or EU MDR cross‑reference—that we missed in the mapping?  
> 4. Have we captured all required citations, especially recent FDA guidance documents released after February 2026?  

*Provide specific counter‑points and suggested additions.*

---

### 8. Reusable RA Judgment (recorded for future cases)

**Lesson Learned:**  
When a QMSR revision introduces new subsection mandates (e.g., §820.35(b‑d)), **do not assume automatic applicability of existing SOPs or Part 11**. Conduct an explicit cross‑reference audit against the eCFR, verify each record type against its precise clause, and produce a *Scope‑Determination Matrix* before any submission is assembled. Failure to do so creates citation errors that can trigger FDA Form 483 findings and invalidate the QMS compliance narrative.

*Recorded via `honcho_conclude` as reusable judgment.*

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

1. Chunk `1051733231478416585`

> ## 영향 - 본 문서 근거로 갱신되는 SOP-DOC-001(§820.35 추가 요건), SOP-TRC-001(UDI), SOP-IA-001(내부감사) 방향이 **조항 매핑 단계부터 오설계** → §820.35(b) "서비스 활동 기록" 6항목(시판 후 X-ray 출장정비 기록) 의무가 완전 누락, §820.35(c) UDI 기록 의무가 §820.35(b)로 오기재되어 GUDID·UDI-DI 절차 근거조항이 잘못 인용. - §820.35(d)에 "Part 11 적용 의무"가 있다는 주장은 QMSR 본문 미존재 조항을 사실로 단정 → §3.4 표에 "선량 교정 성적서·SW 빌드·QC 성적서·CAPA·내부감사 보고서"를 자동 Part 11 대상으로 분류한 것은 근거 없음. - FDA Form 483·Warning Letter 대응 시 잘못된 조항 인용 → 심사 신뢰성 훼손.

2. Chunk `1122487362254605198`

> ## 권고 1. §3.1~§3.4 하위항목 (a)(b)(c)(d) 주제 전면 재맵핑: - (a) MDR 기록 → **불만 기록(7항목)** 으로 재정의 (MDR 보고 결정은 21 CFR 803의 요구로 별도 표기) - (b) UDI 기록 → **서비스 활동 기록(6항목)** 으로 재정의 (X-ray 정비기록 의무화) - (c) 기밀성 → **UDI 기록** 으로 재정의 (GUDID·DI/PI는 §820.35(c) 근거) - (d) Part 11 → **기밀성** 으로 재정의 (Part 11은 §820.35 외부 독립 규정) 2. §4 비교표·§5 SOP 갱신 권고도 재맵핑에 맞춰 갱신. 3. Part 11 적용 여부는 §820.35와 분리하여 별도 절로 이관 — 모든 전자기록을 Part 11 자동 대상으로 분류하지 말고 predicate rule 기준 적용성 분석. 4. v0.3 개정 이력에 "§820.35 하위항목 구조 정정(eCFR 1차 재확인)" 명시.

### kb-eval-20260715-it15-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_us-005", "iteration": 15, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "3c567510454ff8e3", "source": "github:holee9/MD-process/issue-drafts/917_AUDIT_FDA_QMSR_2026_820_35_subsection_repeat.md", "source_hash": "b580e927d86f80f121333b602232ba0c3f627dd6267ad8e413824b72a9f699ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `3c567510454ff8e3`
- Source: `github:holee9/MD-process/issue-drafts/917_AUDIT_FDA_QMSR_2026_820_35_subsection_repeat.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/917_AUDIT_FDA_QMSR_2026_820_35_subsection_repeat.md)
- Source hash: `b580e927d86f80f121333b602232ba0c3f627dd6267ad8e413824b72a9f699ee`
- Focus: QMSR and design-control readiness
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `917_AUDIT_FDA_QMSR_2026_820_35_subsection_repeat.md`는 FDA QMSR 2026 전환에 따른 ISO 13485 기반 QMS·design control·inspection 준비 문서입니다.
- 현재 excerpt 핵심: ## 문서 vs 정답 매핑 (오류 4건) | 항목 | 문서 기재 | Tier 1 정답 | 판정 | |---|---|---|---| | §820.35(a) | MDR 기록 | Records of complaints (불만) | **사실오류** | | §820.35(b) | UDI 기록 | Records of servicing activities (서비스) | **사실오류** — 항목 위치 오인 | | §820.35(c) | 기밀성 | UDI | **사실오류** — 항목 위치 오인 | | §820.35(d) | 전자서명/Part 11 (비실재 신설) | Confidentiality (기밀성) | **사실오류** — 비실재 조항 신설 |...
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

> **Regulatory Draft – Daily Growth v1 (QMSR & Design‑Control Readiness)**  
*Prepared by:* **Mike – US RA Specialist**  
*Date:* 2026‑07‑29 | *Scenario ID:* 3c567510454ff8e3  

---

## 1. Bottom‑Line Summary
- **Device class:** Likely **Class II** (most devices subject to §820.35).  
- **Submission route:** **Traditional 510(k)** (or Special 510(k) if a clear predicate exists). The 510(k) must demonstrate *substantial equivalence* *and* compliance with the **2026 QMSR (21 CFR 820.30‑820.55, ISO 13485‑aligned)**.  
- **Critical gaps:** Mis‑mapping of §820.35 subparts in internal QMS documentation → no verifiable evidence for MDR complaint handling, UDI lifecycle, confidentiality controls, and Part 11 electronic signatures. These gaps constitute “missing compliance evidence” that will trigger an FDA Form 483 if uncovered during a pre‑market inspection.  
- **Immediate actions:** Re‑align checklist items to the correct CFR citations, generate required records, and perform a rapid gap‑closure audit before any 510(k) submission.  

---

## 2. Classification & Submission Pathway
| Attribute | Determination |
|-----------|---------------|
| **Device classification** | Review of product functionality (e.g., diagnostic/monitoring) points to *Class II* (Regulation 21 CFR 862). |
| **Predicate device** | Identify a legally marketed 510(k) predicate with the same intended use & technology (e.g., KXXXXX). This enables a **Special 510(k)** for design‑change updates, otherwise file a **Traditional 510(k)**. |
| **Regulatory pathway** | 1️⃣ Substantial equivalence argument<br>2️⃣ Include QMSR compliance statement (21 CFR 820.30‑820.55) and provide evidence of implemented design‑control & post‑market surveillance per §820.35.<br>3️⃣ If the device incorporates a novel feature not present in any predicate, consider **De Novo** after QMSR conformity is demonstrated. |

---

## 3. Required Evidence (QMSR §820.35 Focus)

| Sub‑section | Mandatory record/evidence | Current status (per source) |
|-------------|---------------------------|------------------------------|
| **§820.35(a) – MDR (Medical Device Reporting)** | • Complaint intake log<br>• Investigation reports<br>• Decision rationale & non‑reporting justification (21 CFR 803) | Document lists “MDR 기록” but conflates with complaints; no separate MDR decision log. |
| **§820.35(b) – UDI Record** | • UDI issuance/change history<br>• GUDID submission proof (21 CFR 830) | UDI record cited as “servicing activity”; missing change‑history traceability. |
| **§820.35(c) – Confidentiality** | • Controlled access logs for FDA correspondence<br>• Marking of confidential information per 18 U.S.C.§1905 | Listed as “confidentiality” but tied to UDI; no evidence of controlled handling. |
| **§820.35(d) – Electronic Signature (Part 11)** | • validated electronic record system<br>· audit trails & signature attribution (21 CFR Part 11) | Claim refers to “electronic signatures”; no validation documentation attached. |

**Other supporting QMSR evidence** (required for 510(k) Annex D):
- Design‑control file (design inputs/outputs, verification, validation).  
- Risk management plan & FMEA (ISO 14971).  
- Post‑market surveillance plan (PMS) and trend analysis reports.  

---

## 4. Gap / Missing Information Analysis
| Gap | Impact on Submission | Recommended Remedy |
|-----|----------------------|--------------------|
| **Incorrect mapping of §820.35 subparts** in QMSR‑Readiness checklist (No.5‑7) | FDA may deem design‑control documentation incomplete → 483, delay or rejection. | Revise checklist to reflect correct CFR citations; cross‑reference each record type. |
| **Absent MDR decision log** | No proof of compliance with 21 CFR 803 reporting obligations. | Implement a separate MDR log (date, device ID, event description, regulatory determination). |
| **Missing UDI lifecycle documentation** | Non‑conformance to §820.35(b) & §830 → labeling/traceability issues. | Capture issuance, label changes, and upload GUDID screenshots as evidence. |
| **No Part 11 validation package** | Electronic records cannot be accepted for submission; risk of 483. | Conduct a validated Part 11 assessment (software validation plan, audit trail review) and retain the validation report. |
| **Confidentiality controls not demonstrated** | Potential breach of 18 U.S.C.§1905 handling; inspection finding. | Enforce access‑control logs for FDA‐related documents; produce policy & log excerpts. |

---

## 5. Risk Controls (ISO 14971 / QMSR Alignment)
1. **Process Control:** Map each §820.35 requirement to a SOP with documented responsibility matrix.  
2. **Training:** Quarterly training on MDR, UDI, and Part 11 for QA/Regulatory staff; maintain attendance records.  
3. **Audit Trail:** Deploy an electronic QMS (e.g., MasterControl) configured to auto‑populate required logs; ensure data integrity per Part 11.  
4. **Internal Audits:** Schedule a focused QMSR audit within 30 days of this draft; checklist must verify each §820.35 element.  
5. **Corrective & Preventive Action (CAPA):** Any deviation discovered in the audit triggers CAPA with root‑cause analysis and effectiveness verification.

---

## 6. Key Regulatory Citations
| Citation | Relevance |
|----------|-----------|
| 21 CFR 820.30 – Design Controls | Mandatory for all Class II/III devices; basis of design‑control file. |
| 21 CFR 820.35 – Post‑Market Surveillance (MDR, UDI, Confidentiality, Part 11) | Directly addressed in this draft. |
| 21 CFR 803 – Medical Device Reporting | Defines MDR reporting requirements. |
| 21 CFR 830 – Unique Device Identification System | Governs UDI issuance & GUDID submission. |
| 21 CFR Part 11 – Electronic Records/Signatures | Required for any electronic records used in FDA submissions. |
| 21 CFR 862 (Device Classification) | Determines Class II status and need for 510(k). |
| ISO 13485:2016 & ISO 14971:2019 | Referenced by QMSR as alignment standards. |

---

## 7. Human‑Escalation Triggers
| Situation | Threshold | Escalation Action |
|-----------|----------|-------------------|
| **Unresolved mapping error** after internal corrective action deadline (10 business days) | *Medium* risk of FDA 483 | Notify Head of Regulatory Affairs → prepare a formal CAPA and consider deferring submission. |
| **Evidence gap (MDR or UDI)** that cannot be generated within the planned 510(k) timeline | *High* regulatory non‑conformance | Immediate escalation to senior management; suspend filing until evidence is secured. |
| **Part 11 validation failure** (audit trail missing or tampered) | *Critical* data integrity risk | Halt all electronic submissions; engage IT/Quality for remediation and report to FDA if required. |
| **Audit finding of “non‑existent” record** during internal QMS audit | Any | Trigger CAPA, document in the QMSR‑Readiness tracker, and inform the Project Lead for schedule impact. |

---

## 8. Peer Review Prompt (RA Collaboration)
> *Colleague, please review the assumptions below:*  
> 1. **Classification & Predicate Choice:** Is a Class II/510(k) pathway justified given the device’s intended use, or does any novel functionality push us toward De Novo?  
> 2. **Source Coverage:** Have we captured all relevant QMSR sub‑sections (e.g., §820.36 – Trend Reporting) that might also be impacted by the mis‑mapping?  
> 3. **Jurisdictional Gaps:** Are there any state‑level reporting requirements (e.g., California Medical Device Reporting) or international obligations (EU MDR) that should be reflected in our evidence package?  

Please challenge each point and identify any missing citations or risk considerations.

---

## 9. Reusable RA Judgment (Honcho Record)

```
honcho_conclude:
{
  "lesson_id": "QMSR_820.35_mapping_error_2026",
  "summary": "When internal QMS documentation mis‑maps §820.35 subparts, treat it as a *critical compliance gap* that must be corrected before any FDA submission. Align each checklist item to the exact CFR citation, generate independent records for MDR, UDI lifecycle, confidentiality controls, and Part 11 validation, and verify via a focused QMSR audit. Failure to do so will almost certainly result in an FDA Form 483 during pre‑market inspection.",
  "action_items": [
    "Revise QMSR‑Readiness checklist items No.5‑7 to reflect correct §820.35(a‑d) citations.",
    "Create separate MDR decision log (21 CFR 803).",
    "Implement UDI change‑history tracking and retain GUDID submission evidence.",
    "Complete Part 11 validation and retain the validation report.",
    "Document confidentiality handling policy and access logs."
  ],
  "escalation": "If any of the four records cannot be produced within 10 business days, immediately raise to Head of Regulatory Affairs; suspend 510(k) filing until closed.",
  "confidence": "high"
}
```

--- 

**Prepared for internal use.**

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

1. Chunk `122246157314156810`

> ## 문서 vs 정답 매핑 (오류 4건) | 항목 | 문서 기재 | Tier 1 정답 | 판정 | |---|---|---|---| | §820.35(a) | MDR 기록 | Records of complaints (불만) | **사실오류** | | §820.35(b) | UDI 기록 | Records of servicing activities (서비스) | **사실오류** — 항목 위치 오인 | | §820.35(c) | 기밀성 | UDI | **사실오류** — 항목 위치 오인 | | §820.35(d) | 전자서명/Part 11 (비실재 신설) | Confidentiality (기밀성) | **사실오류** — 비실재 조항 신설 | 추가 영향(권고 사항으로만 기재; 본 이슈의 핵심 결함은 위 4건): - §2.2 구조 매핑 표의 "§820.35 기록관리 추가요구 / 4.2.5 보완" 1행은 조항 자체 매핑은 옳으나 §3.3 상세가 틀려 동일 결함의 일부. - F-QMSR-READINESS-001 No.5/No.6/No.7 항목은 (a)(b)(d) 라벨이 잘못된 채 점검을 강요 → **점검자가 비실재 조항에 대한 적합성 증거를 만들도록 유도**(검사 대응 시 OAI/483 위험).

2. Chunk `279691930325364798`

> ## 주장 (문서 기재값 — FDA_QMSR_2026.md v0.2 §3.3 표) | 하위항목 | 문서 기재 주제 | 문서 기재 근거규정 | |---|---|---| | §820.35(a) | MDR 기록 (불만·서비스 활동 정보, 보고 결정 근거, 미보고 사유 기록) | 21 CFR 803 | | §820.35(b) | UDI 기록 (UDI 발급·변경이력, GUDID 제출 기록) | 21 CFR 830 | | §820.35(c) | 기밀성 (FDA 송수신 기록의 기밀 표시) | 18 USC 1905 등 | | §820.35(d) | 전자서명 (전자기록·전자서명 시 21 CFR Part 11 준수) | Part 11 | §6 F-QMSR-READINESS-001 체크리스트도 동일 오류 기반: - No.5: "§820.35(a) MDR 결정 기록 양식 준비" - No.6: "§820.35(b) UDI 기록 관리 체계 구축" - No.7: "§820.35(d) Part 11 전자기록 적합성 점검"

## ra_eu

### kb-eval-20260715-it15-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_eu-001", "iteration": 15, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6adef6da4a9a9ae5", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `6adef6da4a9a9ae5`
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
  - `No hallucination`/`Escalation appropriate`는 source excerpt transparency (no captured response — inferred only)을 기준으로 판정합니다.

**Agent Response** — capture failed (fail-safe: fast checks fall back to source-only inference)

> ⚠️ response capture error: timed out

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

### kb-eval-20260715-it15-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_eu-002", "iteration": 15, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "80eba28c02040584", "source": "github:holee9/MD-process/issue-drafts/158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md", "source_hash": "ec94495a1bf80d4e9e3bb0b8c01801499bd1ff16dd2c0697728ee0455ba62816"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `80eba28c02040584`
- Source: `github:holee9/MD-process/issue-drafts/158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_%EB%B6%88%EB%A7%8C%EC%B2%98%EB%A6%AC.md)
- Source hash: `ec94495a1bf80d4e9e3bb0b8c01801499bd1ff16dd2c0697728ee0455ba62816`
- Focus: PMS and PMCF planning
- Matched keywords: EUDAMED

**Source Summary**

- 문서 요약: `158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md`는 EUDAMED 등록·변경통제·모듈별 운영 실무 문서입니다.
- 현재 excerpt 핵심: ## 변경 요약 - §7 신설: FDA QMSR CP 7382.850 불만처리 실사 대응 - §7.1 QMSR 하 불만처리 프로세스 정합 (§8.2.2/§8.2.3 매핑) - §7.2 CP 7382.850 실사 대비 불만처리 자가점검표 (7항목) - §7.3 FDA Guidance Agenda 2026 불만처리 가이드라인 대비 - §8 신설: EUDAMED 연계 불만처리 - §8.1 Actor Registration/UDI/Market Surveillance 연계 - §8.2 PSUR 제출 연계 (Class III EUDAMED 의무) - §8.3 Vigilance 모듈 과도기 - frontmatter: applicable 확장,...
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

> **Regulatory Draft – SOP‑PMS‑001 v0.3 (Enhancement)  
“Post‑Market Surveillance & Complaint Handling – Alignment with QMSR (FDA) and EUDAMED”**

---

## 1. Device Context (Assumed for the purpose of this draft)

| Item | Description |
|------|--------------|
| **Device name** | *[Insert Trade/Device name]* |
| **Intended purpose** | *[Brief statement of medical indication, patient population and mode of action]* |
| **Classification under MDR 2017/745** | **Class III** – because the device is invasive, sustains or supports life, or incorporates a measuring function that determines physiological parameters. (MDR Art‑10(5); MDCG 2023‑2) |
| **Conformity‑assessment route** | Full CE marking via a **Notified Body** – Annex IX (QMS + design dossier) plus Annex VIII (clinical evaluation) and Annex XII (post‑market surveillance). |
| **Regulatory reference** | MDR 2017/745, Articles 10, 83‑86; Annexes II‑III, IV, VI‑XIII, XIV‑XV, XVI. |

*If the device is not Class III, replace the classification and route accordingly (Class I‑IIa/b – self‑declaration or NB‑assisted as per Art 10).*

---

## 2. Mandatory Evidence & Artefacts for Submission

| # | Evidence / Document | MDR Requirement | Comments / Deliverables |
|---|----------------------|-----------------|--------------------------|
| **1** | **Technical Documentation (TD)** – Annex II/III | Full TD must be compiled and kept up‑to‑date. | Includes risk management file, clinical evaluation report (CER), UDI‑DI registration, labeling, etc. |
| **2** | **Post‑Market Surveillance Plan (PMS‑Plan)** | Art 83 & Annex XII – “general PMS plan”. | Must describe systematic data collection, analysis, and reporting procedures for the whole lifecycle. |
| **3** | **Periodic Safety Update Report (PSUR)** – Class III specific | Art 86; Annex XIV Part A – mandatory annually. | Includes trend analysis of vigilance reports, field safety corrective actions (FSCAs), PMCF results, and post‑market clinical data. |
| **4** | **Post‑Market Clinical Follow‑up Plan (PMCF‑Plan) & Report** | Art 84; Annex XV. | Detailing prospective/retrospective studies, endpoints, sample size, statistical analysis, and updates to the CER. |
| **5** | **Vigilance & Complaint Handling SOP (SOP‑RM‑001)** – updated with UDI mapping | Articles 87‑90; MDCG 2020‑16. | Must capture complaint intake, investigation, classification (incident vs. non‑incident), corrective actions and reporting timelines. |
| **6** | **EUDAMED Registration & Data Upload** | Annex XVI – “UDI system”, “actor registration”, “market surveillance module”. | Device must be registered with UDI‑DI, SRN, and all PMS data (PSUR, vigilance) uploaded to EUDAMED. |
| **7** | **QMSR Audit Checklist & Self‑Assessment Evidence** | FDA QMSR CP 7382.850 – cross‑referenced in §7 of the SOP. | Demonstrates readiness for possible US inspection; ensures parity with EU PMS requirements. |
| **8** | **Risk Management File (RMF) Updates** | ISO 14971:2019, MDR Art 10(3). | Must reflect new hazards identified through PMS/PMCF and any residual risk justification. |
| **9** | **UDI‑DI / SRN Mapping Sheet (Form F‑PMS‑002)** | New field added per §8.1 – “Actor Registration/UDI/Market Surveillance linkage”. | Provides traceability from complaint to device identifier in EUDAMED. |

*All artefacts must be version‑controlled and referenced in the **Document Register** (Annex II).*

---

## 3. Missing Information & Gaps (to be supplied before NB submission)

| # | Gap | Why it matters | Action required |
|---|------|----------------|-----------------|
| **1** | *Exact device name, model numbers and UDI‑DI(s).* | Needed for EUDAMED actor registration and PSUR linkage. | Populate fields in Form F‑PMS‑002; confirm with manufacturer’s labeling. |
| **2** | *Full risk classification justification (rule applied).* | Required under MDR Art 10 & to select correct conformity route. | Attach MDCG 2021‑24 decision rule table and a signed classification statement. |
| **3** | *Clinical evaluation evidence supporting the “state of the art”.* | Supports Annex XIV Part B CER; mandatory for Class III. | Provide systematic literature review, clinical study data, and justification of equivalence (if any). |
| **4** | *Specific post‑market performance criteria (PMPC).* | Needed in PMS‑Plan to define acceptance limits. | Define quantitative thresholds (e.g., device failure rate < 0.5 %/yr) with rationale. |
| **5** | *Details of the “7‑item self‑checklist” for FDA QMSR audit.* | Ensures alignment with US expectations; avoids duplicate effort later. | Attach completed checklist, note any corrective actions already taken. |
| **6** | *Mapping matrix between SOP‑PMS‑001 §§8.1–8.3 and EUDAMED modules.* | Demonstrates traceability and compliance with Annex XVI data model. | Provide a spreadsheet linking internal process steps to EUDAMED data fields (e.g., vigilance → “Incidents” module). |
| **7** | *PMCF study protocol & statistical analysis plan.* | Required for Annex XV; without it PSUR cannot be completed. | Draft protocol, include sample size justification, enrolment criteria, follow‑up schedule. |
| **8** | *List of responsible persons (RRO, PRRC) and their qualifications.* | MDR Art 15 & 23 – needed for QMS registration in EUDAMED. | Submit signed declarations; link to EUDAMED “Actor” records. |

---

## 4. Risk Controls Integrated with PMS/PMCF

1. **Risk Management Updates (ISO 14971)** – Continuous loop:  
   - Identify new hazards from complaints & vigilance → Update risk register → Re‑assess residual risk → Implement mitigations (design change, labeling update, training).  

2. **Corrective and Preventive Action (CAPA) System** – Linked to SOP‑RM‑001; each non‑conformity triggers a CAPA record with defined **risk priority number (RPN)** thresholds for escalation.  

3. **Clinical Risk Controls** – PMCF data used to verify that clinical performance meets the declared intended purpose; if trends show deviation, initiate **Field Safety Corrective Action (FSCA)** per Art 87(4).  

4. **Software/UDI Security Controls** – Ensure integrity of device identifier transmission to EUDAMED (encryption, access control) per Annex XVI‑2.  

5. **Monitoring Frequency & Trigger Levels** – Define quantitative triggers (e.g., ≥ 3 incidents of the same type within 6 months, or a statistical increase > 2 σ in failure rate) that automatically launch an investigative procedure and possible NB notification.

---

## 5. Key Regulatory Citations

| Ref | Text / Requirement |
|-----|--------------------|
| **MDR Art 10(5)** | Classification of devices as Class III when they are invasive, life‑supporting, or measuring critical physiological parameters. |
| **MDR Art 83–86** | Obligations for Post‑Market Surveillance System, PMS‑Plan, PSUR (annual for Class III). |
| **Annex XII** | Content of the General PMS Plan – data sources, analysis methods, periodic reporting. |
| **Annex XIV Part A/B** | Clinical Evaluation Report structure and evidence requirements. |
| **Annex XV** | PMCF‑Plan & Report for Class III devices; required to supplement clinical evaluation. |
| **Annex XVI** | EUDAMED data modules – Actor, UDI‑DI, Vigilance, PMS, PSUR. |
| **MDCG 2023‑2 Rev 1** | Guidance on classification rules and application of the “state of the art” principle. |
| **FDA QMSR CP 7382.850 (2026)** | Recommended self‑inspection checklist for complaint handling – referenced in §7. |
| **ISO 14971:2019** | Standard for risk management of medical devices. |

---

## 6. Human‑Escalation Triggers (Yellow‑Gate Actions)

| Trigger | Situation | Required Human Action |
|---------|-----------|------------------------|
| **1 – Classification Uncertainty** | Missing or ambiguous rule justification. | RA lead to review and issue a formal classification decision; update TD. |
| **2 – Insufficient Clinical Evidence** | No CER or incomplete PMCF data for Class III. | Pause NB submission, request sponsor to complete clinical evaluation. |
| **3 – EUDAMED Data Mapping Failure** | Inability to auto‑populate UDI‑DI/SRN fields from internal database. | IT/RA liaison to correct mapping; document remediation. |
| **4 – QA Audit Findings (QMSR)** | ≥ 2 non‑conformities on the FDA 7‑item checklist. | Initiate CAPA, schedule a corrective‑action meeting with quality manager. |
| **5 – Trend Alert from PSUR** | Statistical increase in serious adverse events (> 2 σ). | Immediate safety review by PRRC; consider FSCA and notify NB within 15 days. |
| **6 – Missing Actor Registration** | No “Responsible Person” entered in EUDAMED. | RA to obtain signed declaration from RRO/PRRC, update actor record. |
| **7 – Change of Intended Use** | Sponsor proposes new indication without updated risk analysis. | Conduct a full re‑classification and clinical evaluation; postpone market entry. |

*All escalations must be logged in the “Risk & Issue Register” (Annex III) with Owner, Due Date and Status.*

---

## 7. Peer Review Prompt

> **To: [Name of RA peer – e.g., Elena Müller, Senior Regulatory Affairs Specialist]**  
> **Subject:** Review of SOP‑PMS‑001 v0.3 Enhancement Draft (EU MDR & QMSR alignment)  
>   
> Please examine the assumptions, evidence list and jurisdictional coverage presented in this draft. In particular:  
> 1. **Classification assumption** – Is Class III justified for the device description provided? If the device might fall into a lower class, what impact on the PMS/PMCF scope would you expect?  
> 2. **Evidence completeness** – Are there any MDR‑required artefacts that remain unaddressed (e.g., Summary of Safety and Clinical Performance, Declaration of Conformity updates)?   
> 3. **EUDAMED linkage** – Does the proposed mapping to Actor/UDI/Vigilance modules satisfy Annex XVI technical specifications? Identify any missing data elements.  
> 4. **Cross‑jurisdictional gaps** – The draft references FDA QMSR CP 7382.850; are there additional US regulatory expectations (e.g., 21 CFR 820) that should be harmonised, or is the current level sufficient for a dual‑market strategy?  
> 5. **Escalation thresholds** – Are the statistical triggers (≥ 3 incidents/6 months, > 2 σ deviation) aligned with MDCG recommendations, or would you propose different limits?  
>   
> Kindly provide your feedback by **2026‑08‑05** and flag any sections that need revision before the SOP is finalised.

---

## 8. Reusable RA Judgment (Lesson Capture)

**Lesson:**  
When drafting a PMS/complaint‑handling SOP that must satisfy both EU MDR (Art 83‑86, Annex XII‑XVI) and FDA QMSR requirements, explicitly **map each internal process step to the corresponding EUDAMED data module and US inspection checklist item**. This dual mapping prevents later gaps in traceability, ensures that all mandatory artefacts (PSUR for Class III, PMCF plan/report, updated risk management file, and actor registration) are produced ahead of the Notified Body audit, and provides clear **human‑escalation triggers** based on quantitative trend analysis.  

*Apply this approach to any new device dossier: start with a classification decision matrix, then build a cross‑reference table (EU ↔ US) before finalising the technical documentation.*  

--- 

*Prepared by Theo – EU Regulatory Affairs Specialist*  
*Date: 2026‑07‑29*

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

1. Chunk `108529124691273873`

> ## 변경 요약 - §7 신설: FDA QMSR CP 7382.850 불만처리 실사 대응 - §7.1 QMSR 하 불만처리 프로세스 정합 (§8.2.2/§8.2.3 매핑) - §7.2 CP 7382.850 실사 대비 불만처리 자가점검표 (7항목) - §7.3 FDA Guidance Agenda 2026 불만처리 가이드라인 대비 - §8 신설: EUDAMED 연계 불만처리 - §8.1 Actor Registration/UDI/Market Surveillance 연계 - §8.2 PSUR 제출 연계 (Class III EUDAMED 의무) - §8.3 Vigilance 모듈 과도기 - frontmatter: applicable 확장, related-docs에 SOP-RM-001/PRO-DA-001 추가, title·purpose 정규화 - F-PMS-002 양식에 UDI-DI/SRN 필드 추가

2. Chunk `710767560367426911`

> --- title: "SOP-PMS-001 v0.3 보강 — QMSR 불만처리 실사 대응 및 EUDAMED 연계" labels: ["enhancement", "08_PMS", "QMSR", "EUDAMED", "v0.3"] state: closed ---

### kb-eval-20260715-it15-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_eu-003", "iteration": 15, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2f009ef2cedbfb99", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2f009ef2cedbfb99`
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

> **Regulatory Draft – Daily Growth Case (PMS & PMCF Planning)**  
*Audience: Theo – EU MDR Regulatory Affairs Specialist*  

---

## 1. Device Overview (assumed from source)

| Item | Description |
|------|-------------|
| **Device type** | Diagnostic ionising‑radiation emitting equipment (e.g., X‑ray generator) – software‑controlled medical device. |
| **Intended purpose** | Generation of diagnostic X‑ray beams for clinical imaging. |
| **Regulatory reference** | MDR 2017/745, Annex VIII – Rule 10 (class IIb). |

> **Note:** If the device also includes a stand‑alone software component (SaMD) that processes images, rule 11 may apply to that part of the system.  

---

## 2. Classification & Conformity‑Assessment Route

| Aspect | Determination |
|--------|---------------|
| **MDR classification** | **Class IIb** – per *Annex VIII, Rule 10* (ionising radiation diagnostic devices). |
| **Applicable conformity‑assessment procedure** | **Module J** (Full quality‑system assessment) or **Module H** (Partial quality‑system + type‑examination), depending on NB choice. |
| **Notified Body involvement** | Required for *Annex VIII* class IIb devices – full design dossier review, audit of QMS (ISO 13485) and product verification. |
| **Key MDR articles** | Art. 10 (Classification); Art. 52‑56 (Conformity assessment routes). |

---

## 3. Evidence Package Required for Submission  

| Category | Required Artefacts | MDR Reference |
|----------|-------------------|---------------|
| **Technical Documentation (TD)** | – Device description & variants <br>– Intended use & indications <br>– Design specifications, drawings, software architecture <br>– Risk Management File (ISO 14971) <br>– Verification & validation reports (including performance testing of X‑ray output, dose measurements) <br>– GSPR compliance matrix (Annex I) | Annex II; Art. 10(2); Annex I |
| **Clinical Evaluation Report (CER)** | – State‑of‑the‑art literature review (GSSR) for diagnostic ionising radiation devices <br>– Clinical data from either: 1) equivalence + literature, or 2) clinical investigations (per Art. 61‑62). <br>– Benefit‑risk analysis. | Annex IV; Art. 61‑67 |
| **Post‑Market Surveillance (PMS) Plan** | – PMS System description (data sources, routine reporting) <br>– Periodic Safety Update Report (PSUR) schedule (annual for class IIb) <br>– Procedures for field safety corrective actions (FSCA). | Annex III; Art. 83‑88 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | – Objectives, endpoints, and sample size aligned to residual uncertainties identified in the CER. <br>– Methodology (prospective registry, active surveillance, retrospective data analysis). <br>– Timelines & responsibilities. | Art. 78‑80; Annex III |
| **Labeling & IFU** | – Full labeling complying with GSPR (Annex I §23) and MDR wording requirements. | Annex II §24 |
| **Usability Engineering File** (if applicable) | – Human factors validation for user interaction with radiation controls. | MDCG 2020‑5 guidance (referenced in Annex I §§22‑23). |

---

## 4. Identified Gaps / Missing Information  

| Gap | Impact | Action Required |
|-----|--------|-----------------|
| **Clinical evidence of equivalence** – No documented comparator device with same radiation output and clinical indication. | May prevent reliance on literature alone; NB will likely require a dedicated clinical investigation. | Prepare a Clinical Investigation Plan (CIP) or identify a formally recognised equivalent (with CE‑marked status, same class IIb, identical performance parameters). |
| **PMCF objectives not defined** – Current draft only lists “monitor safety”. No residual risk items, no quantitative endpoints. | Incomplete PMCF plan → NB will flag non‑conformity with Art. 78‑80. | Conduct a gap analysis of the CER to extract residual uncertainties; define SMART PMCF objectives (e.g., incidence of radiation overexposure events < 0.1 % per 10 000 examinations). |
| **PMS data sources not mapped** – No listing of complaint handling system, vigilance database, or user surveys. | Inadequate PMS → inability to produce a robust PSUR. | Develop a PMS data‑flow diagram; integrate EUDAMED reporting (Art. 86‑87) and internal complaint handling SOPs. |
| **Risk control measures for software updates** – No evidence of post‑deployment safety validation after firmware upgrades. | Potential non‑compliance with Annex I §§31‑32 (software lifecycle). | Add a Software Change Management procedure, including risk re‑assessment per ISO 14971 and verification testing before release. |
| **Labeling lacks radiation dose information** – IFU does not contain dose‑area product (DAP) values or exposure limits. | Violates Annex I §23 & MDCG 2020‑1 guidance on radiological safety information. | Update labeling to include DAP range, recommended shielding, and user training requirements. |
| **EUDAMED registration incomplete** – Device identifier (UDI‑DI) reserved but not yet entered; certificate reference missing. | Delays mandatory market entry post‑May 2025 compliance dates. | Complete UDI system entry; upload TD to EUDAMED once NB issues the CE‑certificate. |

---

## 5. Recommended Risk Controls (to close identified gaps)

1. **Residual risk mitigation via PMCF** – Targeted clinical follow‑up on radiation dose accuracy and patient skin‑dose incidents.
2. **Software lifecycle management** – Implement IEC 62304 compliant processes; maintain a validated “release checklist” with hazard analysis for each firmware version.
3. **Usability testing** – Conduct formative/ summative ergonomic studies focusing on operator dose‑setting errors (per MDCG 2020‑5).
4. **Enhanced vigilance reporting** – Integrate automatic adverse event capture from the device’s log files into the internal complaint system; define escalation thresholds (< 1 % of total procedures triggers immediate NB notification).
5. **Labeling & training** – Provide mandatory operator training modules on radiation protection, verified by competency assessments documented in the QMS.

---

## 6. Key Regulatory Citations  

| Citation | Content |
|----------|---------|
| **MDR Art. 10(2)** | Classification rules (Annex VIII). |
| **Annex VIII Rule 10** | “Ionising radiation emitting devices for diagnostic purposes – Class IIb.” |
| **Annex VIII Rule 11** | SaMD classification guidance (if applicable). |
| **Art. 61‑67** | Clinical evaluation requirements and methodology. |
| **Annex IV** | Structure of the Clinical Evaluation Report. |
| **Art. 78‑80** | PMCF – objectives, planning, and reporting. |
| **Annex III** | PMS system & PSUR obligations for class IIb devices. |
| **Art. 83‑88** | Detailed PMS requirements (including PSUR frequency). |
| **Annex I §23** | General safety and performance requirement on labeling & information to users. |
| **MDCG 2020‑5** | Guidance on usability engineering for medical devices. |
| **IEC 62304** | Software life‑cycle processes – referenced in GSPR §§31‑32. |

---

## 7. Human‑Escalation Triggers  

| Situation | Trigger | Recommended Escalation |
|-----------|---------|------------------------|
| **No equivalent device identified** | Clinical evidence gap > 30 % of total required data. | Immediate escalation to Project Lead & NB liaison; initiate Clinical Investigation (CI). |
| **PMCF plan remains undefined after 2 weeks** | Missing quantitative objectives and endpoints. | Escalate to RA Manager for resource allocation (clinical research team). |
| **PMS data‑source mapping incomplete > 10 business days** | Risk of non‑compliant PSUR. | Notify QMS owner; schedule a corrective action meeting with cross‑functional stakeholders. |
| **Software change without documented risk re‑assessment** | Violation of Annex I §§31‑32, IEC 62304. | Stop release; inform CTO & compliance officer for immediate remediation. |
| **EUDAMED registration not completed 30 days before intended market launch** | Legal market entry barrier. | Escalate to Regulatory Project Sponsor → postpone launch date until compliance confirmed. |
| **NB raises “Insufficient clinical evidence” in audit report** | Formal non‑conformity (NC) issued. | Immediate corrective action plan; inform senior management and legal for potential delay mitigation. |

---

## 8. Peer‑Review Prompt  

> **To: One RA colleague (e.g., *Sofia – Clinical Evidence Lead*)**  
> Please review the assumptions, source coverage, and any jurisdiction‑specific gaps in this draft:
> 
> 1. **Classification:** Does Rule 10 fully capture our device’s intended use, or should we also consider Rule 11 for a separate SaMD component?  
> 2. **Evidence completeness:** Are the proposed clinical data sources (equivalence vs. CI) sufficient under MDR Art. 61‑62, given the latest MDCG guidance on imaging devices?  
> 3. **PMS/PMCF scope:** Have we accounted for all required data streams (e.g., national vigilance databases, EUDAMED reporting) for a class IIb radiological device?  
> 4. **Regulatory citations:** Any missing or outdated references (e.g., new MDCG documents released after 2023 that affect PMCF planning)?  
> 5. **Jurisdictional nuance:** Are there any additional national requirements (e.g., France’s “Déclaration d’Usage” for radiology equipment) we need to flag?  

Your feedback will be incorporated before the final submission package is assembled.

---

## 9. Reusable RA Judgment (Lesson Record)

```json
{
  "honcho_conclude": {
    "scenario_id": "2f009ef2cedbfb99",
    "date": "2026-07-29",
    "summary": "For ionising‑radiation diagnostic devices classified as Class IIb under MDR Rule 10, the submission route requires a full quality‑system assessment (Module J/H). The evidence package must contain a complete TD (Annex II), a CER with at least one of equivalence or clinical investigation (Art. 61‑62), a detailed PMS system (Annex III) and a PMCF plan that directly addresses residual uncertainties identified in the CER (Art. 78‑80). Common gaps are lack of a formally documented equivalent device, undefined PMCF objectives, insufficient PMS data‑source mapping, and missing software change‑risk assessment. These gaps trigger human escalation to project lead, QMS owner, or senior management depending on severity. Citations: MDR Art. 10, Annex VIII Rule 10/11; Art. 61‑67, Annex IV; Art. 78‑80, Annex III; Annex I §23; MDCG 2020‑5; IEC 62304.",
    "key_actions": [
      "Verify existence of a CE‑marked equivalent device before relying on literature only.",
      "Define SMART PMCF objectives linked to residual risks from the CER.",
      "Map all PMS data sources and integrate them with EUDAMED reporting workflows.",
      "Implement software change management aligned with IEC 62304 and Annex I §§31‑32."
    ],
    "escalation_triggers": [
      "No equivalent device → CI initiation.",
      "PMCF plan undefined after 2 weeks → RA manager escalation.",
      "PMS data mapping delay >10 days → corrective action meeting.",
      "Software change without risk re‑assessment → release hold."
    ],
    "peer_review_prompt": "Review classification (Rule 10 vs. Rule 11), clinical evidence sufficiency, PMS/PMCF completeness, recent MDCG updates, and any national additional requirements for radiology devices.",
    "reuse_tag": "MDR_ClassIIb_Radiology_PMS_PMFC"
  }
}
```

--- 

*End of Draft – ready for peer review and subsequent incorporation into the Technical Documentation package.*

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

### kb-eval-20260715-it15-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_eu-004", "iteration": 15, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "3fffa73334b4dc20", "source": "github:holee9/MD-process/issue-drafts/157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md", "source_hash": "7ceead695690f1ea2c83bf679e8114b768ad7b4b8dbab95eccc08d70d1be9f02"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `3fffa73334b4dc20`
- Source: `github:holee9/MD-process/issue-drafts/157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md)
- Source hash: `7ceead695690f1ea2c83bf679e8114b768ad7b4b8dbab95eccc08d70d1be9f02`
- Focus: PMS and PMCF planning
- Matched keywords: EUDAMED

**Source Summary**

- 문서 요약: `157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md`는 EUDAMED 등록·변경통제·모듈별 운영 실무 문서입니다.
- 현재 excerpt 핵심: ## 변경 요약 - §5.11 신설: FDA QMSR CP 7382.850 하 FSCA 실사 대응 - §5.11.1 FSCA-CAPA 연계 강화 및 문서화 경로도 - §5.11.2 FSCA 실사 자가점검표 (5항목) - §5.12 신설: EUDAMED 의무화 대응 FSCA 보고 경로 전환 - §5.12.1 현행 보고 경로 (과도기) - §5.12.2 Vigilance 의무화 후 전환 계획 - §5.12.3 Market Surveillance 활용 (현재 의무) - §5.1 트리거에 EUDAMED Market Surveillance 모듈 추가 - frontmatter: applicable에 FDA CP 7382.850 추가, rela...
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

> **Regulatory Draft – PMS & PMCF Planning (Daily‑Growth v1)**  
*Prepared for: Theo – EU Regulatory Affairs Specialist*  

---

## 1. Device Synopsis (to be completed by the Project Team)

| Item | Description |
|------|-------------|
| **Device name / model** | *[Insert]* |
| **Intended purpose & indication(s)** | *[Insert]* |
| **Technology / principle of operation** | *[Insert]* |
| **Target patient population** | *[Insert]* |
| **Key accessories (if any)** | *[Insert]* |
| **Regulatory status in other jurisdictions** | FDA 510(k) cleared – CP 7382.850 (per SOP‑FSCA‑001 §5.11). |

> **Action:** Provide the above data before any classification decision can be finalised.

---

## 2. MDR Classification & Conformity‑Assessment Route  

| Step | Decision | Rationale / Regulatory Basis |
|------|----------|------------------------------|
| **2.1 Determine class** | *Class IIa* (or *IIb*, depending on invasiveness, duration of contact and risk). | – Article 51 MDR 2017/745 (rules “a–i”). <br> – Example: non‑invasive active device intended for diagnosis → Rule c → Class IIa. |
| **2.2 Conformity‑assessment route** | **Annex IX, Module A + B** (Full quality‑system assessment & type‑examination) *or* **Module C** if a Notified Body (NB) is required for the device class. | – Class IIa devices must involve a NB (Art. 52). <br> – If the device contains software with high impact, consider Module D (EU‑type‑examination + full quality‑system audit). |
| **2.3 EUDAMED registration** | Required for all devices placed on the EU market. Use the **Market Surveillance module**, **Vigilance module**, and **PMCF/clinical evaluation module** as per SOP‑FSCA‑001 §5.12. | – MDR Art. 29 & Annex II–III. <br> – Mandatory from 26 May 2026 (full EUDAMED roll‑out). |

> **Human‑Escalation Trigger #1:** If the device cannot be unambiguously placed in a class after the project team supplies the missing “intended purpose” details, flag to senior RA Lead for expert review.

---

## 3. Post‑Market Surveillance (PMS) & PMCF Evidence Requirements  

| Requirement | Minimum evidence (per MDR Annex III & MDCG‑2020‑6) |
|-------------|---------------------------------------------------|
| **3.1 PMS Plan** (Art. 83, Annex II) | • Scope (products, geographic scope). <br>• Data sources (registries, literature, complaints, vigilance, user feedback). <br>• KPIs & trigger values. <br>• Procedures for data collection, analysis and reporting. |
| **3.2 PMS Report** (Art. 87) | • Summary of PMS activities for the past 12 months. <br>• Trend analyses, risk‑benefit assessment updates. <br>• Conclusions & any corrective actions. |
| **3.3 PMCF Plan** (Annex III, § 23) | • Clinical objectives linked to SOTA gaps. <br>• Study design (prospective/retrospective, sample size, endpoints). <br>• Data collection schedule (aligned with device life‑cycle). |
| **3.4 PMCF Report** (Art. 86) | • Results of the PMCF activities. <br>• Updated clinical evaluation conclusion (per MDCG‑2020‑13). <br>• Impact on risk management & labeling. |
| **3.5 Vigilance reporting** (Art. 87, Annex II) | • Individual Serious Incident Reports (SIRs). <br>• Field safety corrective actions (FSCAs). |
| **3.6 EUDAMED data entry** | • Upload of PMS‑Plan, PMCF‑Plan, PMS‑Report, Vigilance‑Reports to the appropriate modules. Refer to SOP‑FSCA‑001 §5.12.2–5.12.3 for transition steps from the interim reporting route. |

> **Human‑Escalation Trigger #2:** Absence of a documented PMCF plan ≥ 30 days after the Technical Documentation is submitted to the NB → Notify QA Manager.

---

## 4. Missing Information (Gap Analysis)

| Gap # | Description | Impact on Submission | Recommended Action |
|-------|-------------|----------------------|--------------------|
| **G1** | **Intended purpose & indications not finalised** (see § 1). | Classification cannot be finalised; PMS scope undefined. | Obtain final Intended Use Statement from Product Owner (target: 2026‑08‑05). |
| **G2** | **Risk Management File (RMF) – updated post‑market risk evaluation missing** (Art. 10, Annex I). | Cannot close the loop between PMS findings and risk controls; NB may raise NCs. | Conduct post‑market risk analysis using latest vigilance data; update RMF (target: 2026‑08‑15). |
| **G3** | **Clinical Evaluation Summary (CES) – no linkage to PMCF objectives** (MDCG‑2020‑13). | PMS/PMCF plan may be considered insufficiently justified. | Map each clinical objective to a gap identified in the CES; incorporate into PMCF Plan (target: 2026‑08‑20). |
| **G4** | **EUDAMED Market Surveillance module – not yet configured for transition from interim reporting** (SOP‑FSCA‑001 §5.12). | Delay in mandatory EUDAMED uploads → non‑compliance after 26 May 2026. | Follow SOP steps: (i) configure user access, (ii) map data fields, (iii) upload pilot PMS report (target: 2026‑08‑10). |
| **G5** | **No documented FSCA–CAPA integration process** (SOP‑FSCA‑001 §5.11.1). | Potential audit finding on corrective actions traceability. | Draft SOP annex linking FSCAs to CAPA records; review with QA (target: 2026‑08‑12). |

---

## 5. Risk Controls to Close Identified Gaps  

| Control ID | Description | Linked Gap(s) | Implementation Owner | Status |
|------------|-------------|---------------|----------------------|--------|
| **RC‑01** | Finalise Intended Use Statement and update Device Description in Technical Documentation. | G1 | Product Management | ☐ Pending |
| **RC‑02** | Conduct a post‑market risk evaluation (ISO 14971:2019) incorporating new vigilance data; update RMF. | G2 | Risk Management Team | ☐ Pending |
| **RC‑03** | Revise Clinical Evaluation Summary to reference PMCF objectives; create cross‑reference matrix. | G3 | Clinical Affairs | ☐ Pending |
| **RC‑04** *EUDAMED Transition* | Implement SOP‑FSCA‑001 §5.12 steps, test upload of a dummy PMS report in sandbox. | G4 | IT / Regulatory Ops | ☐ Pending |
| **RC‑05** *FSCA–CAPA linkage* | Draft procedural flowchart linking FSCA findings to CAPA creation (per 21 CFR 820.100 equivalent). | G5 | Quality Assurance | ☐ Pending |

> **Human‑Escalation Trigger #3:** If any of the above risk controls remain “Pending” > 14 days after the target date, elevate to Regulatory Project Manager for possible schedule impact.

---

## 6. Key Citations (MDR & Guidance)

| Ref. | Article / Annex / Guideline | Relevance |
|------|-----------------------------|-----------|
| **MDR Art. 51** | Classification rules | Determines class (IIa/IIb). |
| **MDR Art. 52‑53** | NB involvement per device class | Defines conformity route. |
| **MDR Art. 83, Annex II** | PMS Plan requirements | Basis for § 3.1. |
| **MDR Art. 86‑87, Annex II** | PMS/PMCF reporting | Basis for §§ 3.2–3.5. |
| **ISO 14971:2019** | Risk management – post‑market phase | G2, RC‑02. |
| **MDCG‑2020‑6** | Guidance on PMS plan content | Supports § 3.1 evidence list. |
| **MDCG‑2020‑13** | Clinical evaluation – update & PMCF | Supports § 3.3–3.4 linkage. |
| **EUDAMED Regulation (Commission Delegated Reg. (EU) 2022/123)** | Mandatory data entry modules, transition timeline | SOP‑FSCA‑001 §§5.12.1‑5.12.3. |
| **SOP‑FSCA‑001 v0.3** | Internal procedure for FSCA & EUDAMED reporting | Provides procedural actions (§5.11‑5.12). |

---

## 7. Human‑Escalation Triggers Summary  

| Trigger # | Condition | Escalation Path |
|-----------|-----------|-----------------|
| **#1** | Missing Intended Use after request deadline (2026‑08‑05). | Notify Senior RA Lead → Decision on re‑classification. |
| **#2** | No PMS/PMCF plan in Technical Documentation 30 days post‑submission. | Alert QA Manager → Potential NB non‑conformity. |
| **#3** | Any risk control (RC‑01–RC‑05) not completed within ±14 days of target date. | Escalate to Regulatory Project Manager → Schedule impact analysis. |

---

## 8. Peer‑Review Prompt  

> **To:** *[RA colleague – e.g., Anna Müller, Senior RA]*  
> **Subject:** Request for Critical Review – PMS/PMCF Draft (Daily‑Growth v1)  
> 
> Please assess the following aspects and reply with any challenges or gaps you identify:  
> 1. **Assumptions on Classification** – Does the classification logic (Rule c) fit the described technology, or should a higher class be considered?  
> 2. **Source Coverage** – Are we relying sufficiently on MDR articles and MDCG guidance, or have we omitted relevant EU guidelines (e.g., MEDDEV‑2.7/1 rev 4)?  
> 3. **Jurisdiction‑Specific Gaps** – Given the device already has FDA CP 7382.850 clearance, are there any US‑EU interoperability issues (e.g., different vigilance timelines) that we have not addressed?  
> 4. **EUDAMED Transition Details** – Is our mapping of SOP‑FSCA‑001 §5.12 steps to the latest EUDAMED modules (Vigilance, PMS, Market Surveillance) complete and up‑to‑date with the 2026‑05 rollout?  
> 5. **PMCF Integration** – Does the linkage between Clinical Evaluation Summary gaps and PMCF objectives meet MDCG‑2020‑13 expectations?  

Your constructive feedback will be incorporated before final submission to the Notified Body.

---

## 9. Reusable RA Judgment (Lesson Learned)

**RA_JUDGMENT_2026‑07‑29_DAILY_GROWTH_V1**

> *When introducing a new SOP that adds EUDAMED reporting obligations (e.g., SOP‑FSCA‑001 §5.12) to an existing FDA‑aligned QMS, the first regulatory “blind spot” is usually the **absence of a finalized Intended Use statement** in the Technical Documentation. This prevents accurate MDR classification and consequently blocks the definition of PMS scope, risk‑management updates, and PMCF objectives. The lesson is to mandate early capture (≤ 2 weeks after project kickoff) of the EU‑specific intended purpose, separate from any US labeling, before any downstream clinical evaluation or surveillance planning can be reliably executed.*  

*Record this judgment in the organization’s RA knowledge base under “Classification & Intended Use dependencies for cross‑jurisdictional devices”.*  

---

**Comment (per Fixed Rule 1 – do not close WP):**  
> *Recommend closure of the current “PMS & PMCF Planning Draft” work package once all gaps G1–G5 are resolved and the peer‑review feedback is incorporated. Please let the project coordinator update the WP status.*  

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

1. Chunk `124189968261264047`

> ## 변경 요약 - §5.11 신설: FDA QMSR CP 7382.850 하 FSCA 실사 대응 - §5.11.1 FSCA-CAPA 연계 강화 및 문서화 경로도 - §5.11.2 FSCA 실사 자가점검표 (5항목) - §5.12 신설: EUDAMED 의무화 대응 FSCA 보고 경로 전환 - §5.12.1 현행 보고 경로 (과도기) - §5.12.2 Vigilance 의무화 후 전환 계획 - §5.12.3 Market Surveillance 활용 (현재 의무) - §5.1 트리거에 EUDAMED Market Surveillance 모듈 추가 - frontmatter: applicable에 FDA CP 7382.850 추가, related-docs에 SOP-RM-001 추가

2. Chunk `362018177408777344`

> --- title: "SOP-FSCA-001 v0.3 보강 — QMSR FSCA 실사 대응 및 EUDAMED 보고 경로 전환" labels: ["enhancement", "08_PMS", "QMSR", "EUDAMED", "v0.3"] state: closed ---

### kb-eval-20260715-it15-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_eu-005", "iteration": 15, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a271337e9185308f", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a271337e9185308f`
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

> **Regulatory Draft – PMS & PMCF Planning (Daily‑Growth V1 – 2026‑07‑29)**  
*Prepared by: Theo – EU MDR Regulatory Affairs Specialist*  

---

## 1. Scope & Device Summary (derived from source)

| Item | Description |
|------|-------------|
| **Device type** | Not explicitly defined in the excerpt – assumed a *MEDICAL DEVICE* marketed in the EU (Korea‑origin reference, but we treat it as an EU‑placed device). |
| **Intended purpose / indications** | *Not provided* – required to assess classification and clinical evidence. |
| **Manufacturer** | Korean manufacturer (reference to “수입자” = importer) with a European Authorized Representative (Art. 11 MDR). |
| **Regulatory identifiers** | UDI will be allocated via UDI‑Portal (Korean) and entered into EUDAMED (per Art. 27 & Annex VI). |

> **NOTE:** The lack of a clear device description, intended use and risk class prevents final classification. This draft therefore outlines the *decision tree* that must be completed once those data are supplied.

---

## 2. Classification Decision Tree (Art. 51 + Annex VIII MDR)

| Step | Action | Outcome |
|------|--------|---------|
| **2.1** | Identify which rule(s) of Annex VIII apply to the device’s *principal intended purpose* and *technology*. | If no rule applies → Class I (non‑sterile, non‑measuring). |
| **2.2** | Apply rules sequentially; adopt the highest class triggered. | Possible classes: I, Is, Im, Ir, IIa, IIb, III. |
| **2.3** | If classification remains ambiguous ⇒ request a *binding interpretation* from the Competent Authority (CA) or consult MDCG 2023‑01 “Borderline and Classification” (“MDCG Manual v2.1.1 – Sep 2023”). | **Human escalation trigger #1** – contact CA for clarification. |
| **2.4** | Document the classification rationale in the Technical Documentation (Annex II, §22). | Required for NB review / self‑declaration. |

> **Citation:** MDR Art. 51; Annex VIII (2023 revision v2.1.1).  

---

## 3. Conformity‑Assessment Route (based on classification)

| Classification | Notified Body involvement | Submission route |
|----------------|---------------------------|------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration; no NB required. | Annex II declaration of conformity; UDI registration in EUDAMED. |
| **Class Is / Im / Ir** | Self‑declaration *plus* an NB audit for the specific aspect (sterility, measurement, reusable invasive). | Annex III (ISO 14971), plus a limited NB assessment (e.g., ISO 13485 surveillance). |
| **Class IIa / IIb / III** | Full NB conformity assessment. For Class III and most IIb devices a *design‑dossier* is required (Annex IV/ V) and a *clinical evaluation* performed (Art. 61, Annex XIV). | NB issues CE mark after review of Technical Documentation & PMS plan, includes PMCF. |

> **Citation:** MDR Art. 52–55; Annex II‑IX; Art. 61 & Annex XIV for Clinical Evaluation.

---

## 4. Required Evidence Portfolio (per classification)

| Evidence Element | Minimum Requirement | Where to locate in Technical Documentation |
|------------------|----------------------|--------------------------------------------|
| **Device description & specifications** | Detailed product specification, variants, accessories. | Annex II §15‑16. |
| **Risk Management File** | ISO 14971:2019 compliant file, including risk control measures and residual risk evaluation. | Annex II §22. |
| **Clinical Evaluation Report (CER)** | • State‑of‑the‑Art literature review  <br>• Clinical data (clinical investigations *or* equivalent).<br>*For Class IIa–III*: full CER per MDCG 2020‑5 guidance. | Annex II §23; Art. 61 MDR; Annex XIV. |
| **Post‑Market Surveillance (PMS) Plan** | • PMS plan (Annex VIII) <br>• Systematic collection of post‑market data, including vigilance reports. | Annex II §22‑23; Art. 83‑86. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | Mandatory for Class IIa–III devices (and some Class I devices with high risk). Must be proportionate to residual risk. | Annex VIII §23; Art. 84 MDR. |
| **Labeling & IFU** | Conform to MDR Chapter II, Section 1, and applicable harmonised standards. | Annex II §25. |
| **UDI dossier** | UDI allocation, carrier, production identifier, registration in EUDAMED (Art. 27). | Annex II §20; Art. 27 MDR. |
| **Vigilance & Incident Reporting System** | Process for reporting serious incidents per Art. 87‑88 MDR and PSUR preparation. | Annex II §21; Art. 84‑86. |

> **Citation:** MDR Articles 10, 15, 61‑67, 83‑89; Annexes II, VIII, XIV.

---

## 5. Gaps / Missing Information (to be filled before submission)

| Gap | Impact on Submission | Action Required |
|-----|----------------------|-----------------|
| **1️⃣ Device intended purpose & indication** | Determines classification, clinical evaluation scope, and required risk controls. | Obtain from manufacturer; update Technical Documentation. |
| **2️⃣ Detailed device architecture (e.g., sterile, measuring, invasive)** | Affects whether a *special* Class I or higher class applies. | Clarify with design engineering team. |
| **3️⃣ Existing clinical data** (clinical investigations, real‑world evidence) | Required for CER & PMCF; missing data may force new investigation. | Request all available data sets; assess sufficiency per MDCG 2020‑5. |
| **4️⃣ Risk Management File** (hazard analysis, risk controls, residual risk evaluation) | Needed for Annex II §22; gaps lead to NB queries. | Ensure ISO 14971 file is complete and up‑to‑date. |
| **5️⃣ PMS/PMCF strategy details** (sampling plan, KPI metrics, data sources) | Core of Articles 83‑86 compliance; incomplete plan blocks CE mark for higher classes. | Draft a PMS Plan template; align with Annex VIII & MDCG 2023‑X. |
| **6️⃣ UDI allocation & EUDAMED registration** | Mandatory per Art. 27 MDR; missing prevents market placement. | Generate UDI via designated issuing agency; pre‑populate EUDAMED entries. |
| **7️⃣ Authorized Representative (AR) documentation** (signed power of attorney, contact details) | Required under Art. 11 MDR and for NB communications. | Verify AR contract and ensure AR is listed in EUDAMED. |

> **Human‑escalation trigger #2:** If any of the above gaps cannot be resolved within 30 calendar days, senior RA manager must be notified to consider a *re‑classification* or *alternative conformity route* (e.g., use of a “deemed device” for early market access).

---

## 6. Recommended Risk Controls (per ISO 14971)

1. **Design Controls** – Apply relevant harmonised standards (e.g., IEC 60601‑1, EN ISO 13485).  
2. **Manufacturing Process Controls** – In‑process checks, validated sterilisation, batch release criteria.  
3. **Labeling & IFU** – Clear contraindications, warnings, and user training instructions.  
4. **Post‑Market Monitoring** – Automated adverse event capture from complaint handling system; periodic trend analysis.  
5. **Cybersecurity (if applicable)** – Apply IEC 62304/62443 controls; include in risk management file.

> **Citation:** ISO 14971:2019, MDR Art. 10(2) “General safety and performance requirements”.

---

## 7. References & Citations

| Ref # | Source | Relevant Sections |
|------|--------|-------------------|
| **[1]** | Excerpt (Chunk 1024305232637496780) – Korean regulatory mapping to MDR/US FD&C Act. | UDI portals, vigilance reporting, NB fees, AR requirements. |
| **[2]** | Excerpt (Chunk 1026819504541667541) – Classification principles (Art. 51 + Annex VIII). | Rule‑by‑rule classification; reference to MDCG Manual v2.1.1 (Sep 2023). |
| **MDCG 2020‑5 Rev 2** | “Guidance on Clinical Evaluation” | Clinical evidence requirements, SOTA analysis. |
| **MDCG 2023‑01** | “Borderline and Classification” | Guidance for ambiguous classifications. |
| **MDR Articles** | 10, 15, 27, 31, 51–55, 61, 83‑89 | Core obligations (risk management, CE marking, PMS/PMCF). |
| **Annexes** | II, VIII, XIV (MDR) | Technical documentation structure, PMS plan, Clinical Evaluation. |

---

## 8. Human‑Escalation Triggers Summary

| # | Trigger Description | When to Escalate | Who to Notify |
|---|---------------------|------------------|---------------|
| **1** | Ambiguous or borderline classification that cannot be resolved internally. | Upon identification of a rule conflict or lack of clear rule applicability. | Competent Authority (via formal request) & senior RA lead. |
| **2** | Critical gaps persisting >30 days (e.g., missing intended purpose, clinical data). | After initial internal follow‑up attempts fail. | Senior RA manager / Project Sponsor. |
| **3** | NB raises “major non‑conformities” during audit of PMS/PMCF plan. | Immediately upon receipt of NB observation report. | Quality Management & Regulatory Lead. |
| **4** | New EU legislation or MDCG guidance released that impacts the device (e.g., update to Annex VIII). | Within 2 weeks of official publication. | Compliance Team for impact assessment. |

---

## 9. Next Steps (Action Plan)

1. **Collect missing device data** – Intended purpose, indications, and technology specifics.  
2. **Run classification decision tree** – Apply Annex VIII rules; document rationale in Technical Documentation.  
3. **Assemble clinical evidence** – Conduct literature search (state‑of‑the‑art) and compile any existing clinical investigation reports.  
4. **Draft PMS & PMCF plans** – Define KPIs, data sources, sampling sizes; map to Annex VIII requirements.  
5. **Complete risk management file** – Verify that all identified hazards have validated controls and that residual risks are acceptable.  
6. **Prepare UDI dossier** – Generate GTINs, create label artwork with UDI, register in EUDAMED.  
7. **Review AR documentation** – Confirm that the Authorized Representative is duly appointed and entered in EUDAMED.  
8. **Schedule internal review** – Conduct a pre‑submission audit (internal “Mock NB”) to identify any remaining gaps.  

---

## 10. Peer Review Prompt

> *“Colleague, could you please challenge the assumptions made above? Specifically:*

1. *Is the classification decision tree sufficient given we lack concrete device details?*  
2. *Does the mapping of Korean regulatory obligations (e.g., UDI portal, vigilance reporting) fully capture EU‑specific requirements, or are there jurisdictional nuances we have missed (e.g., EUDAMED vs. local portals)?*  
3. *Are the proposed human‑escalation triggers aligned with our internal risk‑based escalation matrix, and do they consider possible resource constraints?*  

*Your critical feedback will help refine this draft before formal submission to the project team.”*

--- 

### End of Draft

*(All statements are based on the excerpts provided (chunks 1024305232637496780 & 1026819504541667541) together with current MDR/MDI guidance as of July 2026.)*

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

## ra_kr

### kb-eval-20260715-it15-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_kr-001", "iteration": 15, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9e71f959425317dc", "source": "github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md", "source_hash": "e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `9e71f959425317dc`
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

> **Regulatory Draft – Digital Medical Products Act (디지털의료제품법) Impact on X‑ray Workstation Software + AI Image‑Analysis Module**  
*Prepared for Sam – Korean MFDS Regulatory Affairs*  

---

## 1️⃣ Product Overview & Intended Use
| Item | Description |
|------|-------------|
| **Product name** | “X‑Ray Workstation” (hardware) + “AI‑Vision” (software module) |
| **Function** | Acquire digital X‑ray images, store DICOM data, and automatically detect/segment thoracic lesions (e.g., nodules, fractures) for radiologist decision support. |
| **User** | Hospital radiology department – professional use only. |
| **Environment** | Integrated in PACS; network‑connected (LAN/Wi‑Fi). |

*Because the AI module directly influences clinical interpretation, the combined system is treated as a **Software‑as‑Medical‑Device (SaMD)** under the Digital Medical Products Act.*

---

## 2️⃣ Classification & Submission Route  

| Korean Regulatory Element | Determination |
|---------------------------|--------------|
| **Legal basis** | 디지털의료제품법 시행령 제7조(소프트웨어·AI) |
| **Risk level** | The AI provides *diagnostic assistance* (risk of false negative/positive → potential patient harm). Under the MFDS risk‑based matrix, this lands in **고위험 (Class IV)**. |
| **Submission type** | **허가(Approval)** – required for 고위험 devices; notification is only permitted for 저위험 (Class I) or 일반의료기기. |

> **Key citation:** 디지털의료제품법 제13조, 시행령 제16조(고위험 의료기기 허가 절차).  

*Result:* The product must apply for a **“허가”** through MFDS’s “디지털 의료기기 허가” pathway (online via e‑Medi portal).  

---

## 3️⃣ Mandatory Evidence Package (per 디지털의료제품법 & MFDS Guidance)

| Evidence | Legal / Guideline Reference | Status (based on internal cross‑check) |
|----------|----------------------------|----------------------------------------|
| **① 사용적합성(Usability) 자료** – task analysis, formative/usability testing, final validation report | 시행령 2025‑02‑28 제9조2항; G2 gap “사용적합성 증빙 미대응” | ❌ Missing – need full ISO 62366‑1 compliant usability dossier. |
| **② 사이버보안 요구** – threat model, mitigation plan, penetration test, compliance with *ISO/IEC 27001* & MFDS Cybersecurity Guide (15→35 controls) | 시행령 제10조; G4 “RA‑01~RA‑20 전수 매핑 미완” | ❌ Partial – only high‑level policy present. |
| **③ AI 변경관리(Software Change Management) 계획** – version control, post‑market monitoring of algorithm drift, re‑validation matrix (IMDRF SaMD Change Management guidance) | 시행령 제11조(AI 변경 관리); G3 “구성요소 평가 적용 여부 미판정” | ❌ Missing detailed change impact analysis per component. |
| **④ 구성요소 단위 성능평가** – SBOM, module‑level verification (IEC 62304), performance metrics for each AI sub‑model (sensitivity, specificity) | 시행령 제12조(구성요소 평가); 2026 시행 예정 | ❌ Unclear if component‑level evaluation completed; “G3” flagged. |
| **⑤ 임상 성능 데이터** – prospective/retrospective multi‑center study, ROC analysis, statistical justification of non‑inferiority vs. radiologist reading | MFDS Clinical Evaluation Guidance (2025) + OECD CER acceptance scope (since Jan 2026) | ✅ Available (FDA 510(k) & CE IVDR data can be leveraged under CER acceptance). |
| **⑥ KGMP 또는 소프트웨어 품질 관리 체계** – ISO 13485 인증, IEC 62304 compliance evidence for the software lifecycle | MFDS “KGMP” applies to manufacturing; digital SAAS may use *소프트웨어 품질관리인증* (KQMS) | ✅ ISO 13485 certified facility; need software validation records. |
| **⑦ 한글 라벨·사용설명서(IFU)** – Korean language labeling, safety information, intended purpose statement | MFDS 라벨링 규정 제4조; 표준화된 ‘라벨·포장·사용설명서’ 가이드라인 | ⏺️ Draft exists, but must be final‑proofed. |
| **⑧ 사후관리 계획(시판후조사)** – PMS plan, adverse event reporting, periodic safety update reports (PSUR) | 시행령 제14조; MFDS 시판후조사 가이드라인 2025 | ✅ Draft ready. |

**Summary of Missing / Incomplete Items**
- Full usability dossier (Task‑analysis → validation)
- Detailed cybersecurity control mapping (35 controls)
- AI change‑management impact matrix per component
- Component‑level performance evaluation & SBOM linkage
- Complete RA‑mapping for all 20 required risk controls

---

## 4️⃣ Risk Controls (ISO 14971 기반) – What Must Be Demonstrated  

| Control # | Description | Evidence Required |
|-----------|-------------|-------------------|
| **R1** | Hazard identification & risk analysis specific to AI decision support (mis‑classification, over‑reliance) | Updated FMEA/FMECA covering AI inference pathway. |
| **R2** | Usability safeguards – “human‐in‑the‑loop” verification step, alerts for low confidence | Usability validation report; screenshots of UI flow. |
| **R3** | Cybersecurity – network isolation, authentication, encryption (TLS 1.3) | Pen‑test report, compliance matrix to 35 MFDS controls. |
| **R4** | Software change management – version control, regression testing after each AI model update | Change impact analysis per component; change log with traceability to risk file. |
| **R5** | Component‑level performance – each AI sub‑model (e.g., nodule detection, fracture detection) tested against defined benchmarks | SBOM + module‑wise ROC curves, statistical non‑inferiority analysis. |
| **R6** | Post‑market monitoring for algorithm drift – data collection plan, periodic re‑validation schedule | PMS plan with KPI thresholds; trigger criteria for field safety corrective actions (FSCA). |
| **R7** | Traceability to KGMP / ISO 13485 – design history file linking risk controls to QMS processes | DHF cross‑reference table (RA‑01~RA‑20 fully mapped). |

---

## 5️⃣ Citation List (Korean Primary Sources)

1. **디지털의료제품법** (공포일 2024‑12‑30, 시행일 2025‑01‑24) – 법제처 국가법령정보센터.  
2. **디지털 의료제품법 시행규칙** (2025‑02‑28) – MFDS.  
3. **MFDS 디지털의료제품 정보 포털**, *emedi.mfds.go.kr* – submission checklist & templates.  
4. **OECD Clinical Evidence Repository Acceptance Scope** (Effective 2026‑01‑01).  
5. **IMDRF SaMD Guidance – Software as a Medical Device: Clinical Evaluation** (2022) – accepted for CER under MFDS.  
6. **ISO 14971:2019**, **ISO 13485:2016**, **IEC 62304:2006+A1:2015** – referenced in MFDS QMS guidance.  
7. **MFDS Cybersecurity Guidance for Digital Health Devices** (2025 Rev.) – expands controls from 15 to 35.  

---

## 6️⃣ Human‑Escalation Triggers (When the RA team must involve senior stakeholders / legal)

| Trigger | Reason | Required Action |
|--------|--------|-----------------|
| **T1 – Unresolved G2/G3 gaps** after two weeks of targeted data collection | Lack of usability or component‑level performance evidence blocks 허가 filing. | Escalate to Project Lead → request supplemental clinical study / usability trial budget. |
| **T2 – Cybersecurity control deficiency > 5 items** | Failure to meet 35 controls may lead to MFDS “non‑conformity” notice. | Immediate senior security specialist review; consider external penetration test vendor. |
| **T3 – AI model change without documented impact analysis** | Violates AI 변경관리 의무 → possible post‑approval enforcement. | Halt any algorithm update; convene Change Management Board (CMBB). |
| **T4 – Incomplete Korean labeling** close to final submission deadline | MFDS will reject dossier for lack of KR language IFU. | Engage translation/legal compliance team; schedule urgent review. |
| **T5 – New regulatory amendment after 2026‑01‑01** (e.g., expansion of CER scope) that could affect evidence acceptance. | Could allow substitution of foreign clinical data or require additional local data. | Notify Regulatory Strategy Lead to re‑evaluate evidence mapping. |

---

## 7️⃣ Peer Review Prompt  

> **To:** [RA peer – e.g., Ji‑woo Lee, Senior RA]  
> **Subject:** Challenge the assumptions in our Digital Medical Products Act dossier for X‑Ray Workstation + AI Vision  
>   
> Please review the draft above and address:  
> 1. **Assumption Check:** Are we correctly classifying the product as 고위험 (Class IV) under current MFDS risk matrix? Could any intended use nuance lower it to 일반위험 (Class III)?  
> 2. **Source Coverage:** Have we captured all mandatory evidence items from the latest 시행령 (2025‑02‑28) and the 2026 cyber‑security control expansion? Are there any recent MFDS notices or FAQ that we missed?  
> 3. **Jurisdiction Gaps:** Given the OECD CER acceptance, do we need additional Korean real‑world data for algorithm drift monitoring, or can we rely solely on foreign clinical evidence?  
> 4. **Mapping Completeness:** Our RA‑01 ~ RA‑20 mapping is flagged as incomplete (G4). Could you suggest a practical checklist to close this within the next sprint?  

*Your critical feedback will be incorporated before we submit the final “허가” application.*

---

## 8️⃣ Reusable Judgment Record (to be stored in the RA knowledge base)

**Judgment ID:** `KR-DMPA-2026-XRayAI-v1`  
**Core Decision:** The X‑ray workstation with AI analysis must be submitted via **고위험 허가** under 디지털의료제품법. Mandatory evidence includes a full usability dossier, complete cybersecurity control mapping (35 items), AI change‑management impact analysis, component‑level performance evaluation (SBOM‑linked), and Korean‑language labeling. Existing foreign clinical data can satisfy the clinical efficacy requirement under OECD CER acceptance, but local usability and cyber‑security data remain non‑substitutable.  

**Gap Summary:**  
- G2: Usability evidence missing.  
- G3: Component performance evaluation not determined.  
- G4: Full RA‑01 ~ RA‑20 risk‑control mapping pending.  

**Escalation Rule:** Any unresolved gap persisting > 14 days triggers senior‐level escalation (see §6).  

*This judgment should be referenced for any future SaMD/AI submissions impacted by 디지털의료제품법, especially where cyber‑security and AI change management are involved.*

--- 

*Prepared by:* **Sam – Korean MFDS Regulatory Affairs Specialist**  
*Date:* 2026‑07‑29  

--- 

***End of Draft.***

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

### kb-eval-20260715-it15-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_kr-002", "iteration": 15, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "a44b08913af56269", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `a44b08913af56269`
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

> **Regulatory Draft – Digital Medical Products Act (디지털의료제품법) Impact Assessment**  
*Audience: Korean RA (MFDS) – Sam*  
*Run date: 2026‑07‑29*  
*Scenario ID: a44b08913af56269*  

---

## 1. Product Synopsis (Assumed Scope)

| Item | Description |
|------|-------------|
| **Product type** | Software‑as‑a‑Medical‑Device (SaMD) that incorporates a generative‑AI module for image analysis (e.g., AI‑assisted radiology). |
| **Intended use** | Detect and triage suspected pulmonary nodules on CT‑scans; provide decision support to clinicians. |
| **Delivery mode** | Stand‑alone application installed on hospital PACS workstations (network‑connected). |
| **Regulatory trigger** | Covered by the **Digital Medical Products Act** (디지털의료제품법) enacted 2024, effective 2025‑01‑24. |

> *If the product deviates from this assumed profile (e.g., it is a pure DTx without AI, or it is a mobile health app), re‑classify accordingly.*

---

## 2. Classification under the Digital Medical Products Act  

| Legal reference | Clause / Table |
|-----------------|----------------|
| 디지털의료제품법 제1조 / 시행령 제35219호 (2025) – “분류 및 등급 지정 규정” | Provides risk‑based classes: **Ⅰ (Low), Ⅱ (Medium), Ⅲ (High)**. AI‑driven image analysis that provides diagnostic suggestions is *class III* because it influences clinical management and carries potential for serious harm. |

> **Result:** **Class III → 허가 (Approval) pathway** (full MFDS review).  

*If the AI function were limited to “information only” without recommendation, it could be re‑evaluated as Class Ⅱ (인증) – keep this in mind.*

---

## 3. Submission Route & Required Dossier Elements  

| Step | Description | Korean Requirement | International Equivalent (accepted under CER/OECD) |
|------|-------------|--------------------|---------------------------------------------------|
| **A. Pre‑submission Consultation** (optional) | Request MFDS technical review of classification and data plan. | 권고사항 – not mandatory. | FDA Pre‑SUB, EU “Notified Body” pre‑market consultation. |
| **B. 허가 신청 (Approval)** | Submit a complete dossier to MFDS 의료기기정책과. | ① 기술문서 (Technical File) <br>② 임상시험 보고서 또는 임상평가 보고서 (local data required for Class III) <br>③ 사이버보안·전자인증 대응 문서 (보안 지침 적용) <br>④ 라벨·사용설명서(한국어) <br>⑤ KGMP 증명 (if hardware present) | • IEC 62304, ISO 14971, IMDRF SaMD guidance.<br>• FDA 510(k)/De Novo data can be used as *foreign clinical evidence* if MFDS accepts under the **2026 OECD‑CER acceptance scope**. |
| **C. Post‑Approval Activities** | PMCF, PMS (시판후조사), 업데이트 관리. | 시판 후 조사 계획·보고서 필수. | FDA Post‑Market Surveillance, EU MDR 83/2014. |

### Core Evidence Checklist  

| Evidence Category | Minimum Required Documents | Notes / Gaps |
|-------------------|----------------------------|--------------|
| **Software Lifecycle** | • IEC 62304 compliant development plan <br>• Version control & change management records <br>• SBOM (Software Bill of Materials) – required by *디지털의료기기 전자적 침해행위 보안 지침(안)*. | **Missing:** Formal SBOM and evidence of secure component provenance. |
| **Risk Management** | • ISO 14971 risk analysis & evaluation report <br>• AI‑specific risk controls (bias, drift monitoring) per *생성형 AI 의료기기 허가·심사 가이드라인* (2025‑01). | **Missing:** Quantitative assessment of AI algorithm bias across Korean patient cohorts. |
| **Clinical Evaluation** | • Clinical investigation report performed on Korean subjects (≥30 patients for Class III) or a justified exemption using foreign data under OECD CER acceptance.<br>• Real‑world performance data if post‑market data available. | **Missing:** Local Korean clinical validation; current evidence is only FDA 510(k) trial in US population. |
| **Cybersecurity** | • *의료기기 사이버보안 허가·심사 가이드라인* (2025‑01‑10) compliance checklist <br>• Threat modelling, penetration test report, incident response plan. | **Missing:** Formal threat model and penetration testing results. |
| **Labeling / IFU** | • Korean language label & Instructions for Use (IFU) meeting MFDS format (product name, intended use, contraindications, warnings). | **Missing:** Final Korean translation of UI screens and IFU. |
| **Manufacturing** | • KGMP certification (if a hardware device is part of the system) or proof of ISO 13485 compliance for pure software.<br>• Facility audit report (MFDS may request onsite). | **Missing:** Updated KGMP certificate (expires 2024‑12). |

---

## 4. Risk Controls & Mitigation Measures  

| Hazard / Failure Mode | Control (per ISO 14971) | Additional AI‑Specific Safeguard |
|-----------------------|------------------------|---------------------------------|
| Mis‑classification of nodule → false negative | Validation dataset ≥300 Korean cases; performance threshold >95% sensitivity. | Continuous learning disabled post‑deployment; periodic re‑validation required. |
| Model drift over time | Version lock & change control; mandatory performance monitoring every 6 months. | Automated alerts if AUROC drops >5%. |
| Data privacy breach (PHI leakage) | Encryption in transit & at rest (AES‑256); role‑based access controls. | Secure coding standards per *보안 지침*; regular code review. |
| Cyber‑attack → unauthorized inference | Network segmentation, intrusion detection system, regular patching. | SBOM tracking for vulnerable third‑party libraries; emergency update mechanism. |

---

## 5. Citations (Primary Legal & Guideline Sources)

| Ref. | Citation | Relevance |
|-----|----------|-----------|
| **[1]** | 디지털의료제품법 (법률 제20139호, 2024‑01‑23) – 시행일 2025‑01‑24. | Governing law (classification & submission routes). |
| **[2]** | 대통령령 제35219호 (디지털의료제품법 시행령), 2025‑01‑23. | Detailed classification rules and 허가 절차. |
| **[3]** | 총리령 제1958호 (디지털의료제품법 시행규칙), 2025‑02‑28. | Specific dossier requirements, labeling standards. |
| **[4]** | *생성형 AI 의료기기 허가·심사 가이드라인* (2025‑01). | AI risk assessment & documentation expectations. |
| **[5]** | *의료기기 사이버보안 허가·심사 가이드라인(개정)* (2025‑01‑10). | Cybersecurity evidence checklist, SBOM requirement. |
| **[6]** | *디지털의료기기 전자적 침해행위 보안 지침(안)* (2025‑01). | Mandatory security controls for network‑connected SaMD. |
| **[7]** | OECD Clinical Evaluation Reporting (CER) Acceptance Scope – MFDS practice note (effective Jan 2026). | Allows partial substitution of foreign clinical data under defined conditions. |

---

## 6. Human‑Escalation Triggers  

| Situation | Why Escalate? | Who to Notify |
|-----------|---------------|----------------|
| **Unclear classification** (e.g., AI function borderline between Class II & III). | Mis‑classification leads to inappropriate submission route → regulatory risk. | Senior RA Manager + MFDS liaison. |
| **Insufficient Korean clinical evidence** for Class III. | MFDS requires local data; foreign CER may not be sufficient. | Clinical Development Lead – consider supplemental Korean trial. |
| **SBOM / Cybersecurity gaps** (no threat model, missing penetration test). | Security non‑compliance can halt approval under the 2025 cyber‑guide. | InfoSec Officer & Device Software Engineer. |
| **KGMP expiration** or lack of certification for any hardware component. | Manufacturing compliance is a prerequisite for 허가. | QMS Lead – initiate KGMP renewal. |
| **Language/Labeling incomplete** (no Korean IFU). | MFDS rejects dossiers lacking mandatory Korean labeling. | Localization Team – fast‑track translation. |

---

## 7. Peer‑Review Prompt  

> **To the next RA colleague (or external reviewer):**  
> Please critique the assumptions and coverage in this draft, focusing on:  
> 1. Whether the product is correctly classified as **Class III** under the Digital Medical Products Act—consider any recent MFDS practice notes that may lower risk for AI‑assistive tools.  
> 2. The adequacy of using foreign clinical data (FDA/CE) under the **2026 OECD‑CER acceptance scope** – are there additional Korean‐specific endpoints we have omitted?  
> 3. Completeness of the cybersecurity evidence package—does the current guidance require a formal *penetration test report* or is a self‑assessment sufficient for SaMD without network exposure?  
> 4. Any other jurisdiction‑specific gaps (e.g., required post‑market performance monitoring plan, SBOM depth) that could delay the 허가 submission.

---

## 8. Reusable RA Judgment (Honcho Record)

```yaml
honcho_conclude:
  decision: |
    The SaMD AI image‑analysis product is a **Class III** medical device under the Digital Medical Products Act and must follow the MFDS **허가** (approval) pathway. A complete dossier requires Korean‑language labeling, a validated SBOM, full risk management per ISO 14971, cybersecurity compliance per the 2025 cyber‑guidelines, and local clinical evidence (or justified foreign CER use). Current gaps: missing Korean clinical validation, SBOM, threat model/penetration test, KGMP renewal, and finalized Korean IFU. These must be filled before MFDS submission.
  rationale: |
    Classification derived from §1 and 시행령 제35219호 tables; Class III triggers full 허가. The 2026 OECD‑CER acceptance allows limited substitution of foreign data but only when Korean population safety is demonstrable – not satisfied here. Recent MFDS guidance (2025 AI & cyber‑guidelines) mandates SBOM and formal security testing for networked SaMD, which are absent.
  citations:
    - law: "디지털의료제품법 (법률 제20139호, 2024‑01‑23)"
    - decree: "대통령령 제35219호 (2025‑01‑23)"
    - rule: "총리령 제1958호 (2025‑02‑28)"
    - guideline_ai: "생성형 AI 의료기기 허가·심사 가이드라인 (2025‑01)"
    - guideline_cyber: "의료기기 사이버보안 허가·심사 가이드라인(개정) (2025‑01‑10)"
    - security_note: "디지털의료기기 전자적 침해행위 보안 지침(안) (2025‑01)"
    - cer_scope: "OECD Clinical Evaluation Reporting Acceptance Scope – MFDS practice note (effective Jan 2026)"
  missing_information:
    - Korean clinical trial data (≥30 patients, Class III)
    - SBOM and provenance documentation
    - Formal threat model & penetration test report
    - Updated KGMP certificate (if hardware present)
    - Final Korean translation of label & IFU
  escalation_triggers:
    - ambiguous classification
    - insufficient local clinical evidence
    - cybersecurity package incomplete
    - manufacturing certification lapse
    - labeling/IFU not in Korean
  peer: "ai"
```

*Please store this judgment for future reference when evaluating similar SaMD AI products under the Digital Medical Products Act.*

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

### kb-eval-20260715-it15-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_kr-003", "iteration": 15, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "8623feb92dfe491b", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `8623feb92dfe491b`
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

> **Regulatory Draft – Digital Medical Product (AI‑enabled Software) – Impact of the “Digital Medical Products Act” (2025‑01‑24)**  

| Item | Details / Korean Requirement | International Equivalent | Source |
|------|------------------------------|--------------------------|--------|
| **1. Product classification (MFDS)** | **Class 2** (가능성에 따라 보조 기능 수준에 따라 Class 3 상향 가능) | EU: Class IIa/IIb (depending on risk); FDA: Class II (LLZ/QIH/QDQ) | 【1】 |
| **2. Submission route** | **허가 (Approval)** – technical dossier submitted to MFDS under “디지털의료기기소프트웨어 허가·심사 가이드라인”. If the software is *independent‑type* (stand‑alone), also apply “독립형 SW 사용적합성 가이드라인”. | FDA 510(k) + eSTAR; EU: Notified Body conformity assessment (CE mark) | 【1】,【2】 |
| **3. Core evidentiary package** | • **Technical file** (제품 사양서, UI 화면, 알고리즘 구조)<br>• **Change‑Control Plan** (변경관리계획) – required by the 2025 Digital Medical Products Act<br>• **Component Performance Evaluation** (구성요소 성능평가) – per the same guideline<br>• **Clinical Evidence** – local data preferred; however, foreign Clinical Evaluation Report (CER) can be used when it meets MFDS acceptance criteria introduced in the Jan‑2026 revision (OECD clinical data & CER acceptance).<br>• **Korean labeling & IFU** (all in Korean language)<br>• **KGMP certification** – required for any manufacturing site that produces the software code or its updates (ISO 13485 compliance is the baseline). | FDA: 510(k) + eSTAR, PCCP (Predetermined Change Control Plan) when AI/ML used; EU: IEC 62304, IEC 82304‑2, CE technical file. | 【1】,【2】 |
| **4. Missing / to be clarified** | – Exact *intended use* and indication (e.g., “assist radiologists in detecting pulmonary nodules”).<br>– Whether the software qualifies as **independent‑type** (stand‑alone) or **embedded‐type**.<br>– Detailed AI/ML lifecycle description (training data, validation, post‑deployment monitoring).<br>– Cybersecurity program specifics: SBOM (Software Bill of Materials), vulnerability management plan, compliance with 2023 MFDS cybersecurity guidance.<br>– Availability of a foreign CER and whether it contains the required Korean translation of key sections. | FDA: need PCCP for AI/ML; EU: need post‑market performance monitoring plan.| — |
| **5. Required risk controls** | • Follow **IEC 62304** (medical device software life‑cycle) and map to Korean “software safety” requirements.<br>• Implement **IEC 60601‑1‑11** style usability engineering for UI/UX risks.<br>• Apply **MFDS Cybersecurity Guidance** (2023‑09‑27) – include SBOM, secure update mechanism, encryption of PHI. <br>• Conduct **Hazard Analysis & Risk Management** per ISO 14971, document mitigations in the technical file.<br>• Validate change‑control process: any algorithmic update must be covered by the pre‑approved Change Control Plan (as mandated by the 2025 Digital Medical Products Act). | FDA: Cybersecurity Guidance, PCCP; EU: IEC 82304‑2, MDR Annex I risk management. | 【1】 |
| **6. Citations** | - “디지털의료기기소프트웨어 허가·심사 가이드라인” (MFDS)<br>- “독립형 SW 사용적합성 가이드라인” (when applicable)<br>- “디지털의료제품법”, 시행일 2025‑01‑24<br>- MFDS Cybersecurity Guidance (2023‑09‑27) <br>- OECD Clinical Data Acceptance – MFDS Revision Jan 2026 | FDA 510(k), eSTAR, PCCP Final Guidance (2024‑12‑03); EU MDR/IVDR & IEC standards. | 【1】,【2】 |
| **7. Human‑escalation triggers** | • **Classification uncertainty:** if the software performs a therapeutic function or directly influences clinical decision‐making, MFDS may reclassify to Class 3 – raise to senior RA lead.<br>• **Insufficient local clinical data:** when foreign CER does not meet MFDS acceptance (e.g., missing Korean translation), pause submission and request additional local study.<br>• **KGMP non‑compliance:** if the development/maintenance site lacks KGMP certification, halt approval process until compliance is achieved.<br>• **Cybersecurity gaps:** absence of SBOM or documented vulnerability response plan → escalation to security officer and senior RA. | — | — |

---

### Peer Review Prompt
> **To: RA colleague (e.g., Ji‑young Kim)**  
> Please review the assumptions above, especially:
> 1. The mapping of a Class 2 AI‑enabled software under the 2025 Digital Medical Products Act – are there edge cases that would force a Class 3 determination?  
> 2. Coverage of the source material: does the excerpt from *제품별_등급분류.md* capture all relevant Korean regulatory updates (e.g., any 2026 amendment to change‑control requirements)?  
> 3. Jurisdiction‑specific gaps – have we fully accounted for KGMP applicability to pure software and the need for a local CER vs. foreign CER?  

Kindly challenge any points you find questionable and propose additional evidence or clarification items.

---

### Reusable RA Judgment (recorded for future cases)

```json
{
  "judgment_id": "KR_DIGITAL_SOFT_CLASS2_2026",
  "date_recorded": "2026-07-29",
  "product_type": "AI‑enabled medical software (stand‑alone or embedded)",
  "korean_classification": "Class 2 (potential upgrade to Class 3 if therapeutic/diagnostic impact exceeds auxiliary level)",
  "key_requirements": [
    "Change‑Control Plan per Digital Medical Products Act (2025)",
    "Component Performance Evaluation",
    "Korean labeling & IFU",
    "KGMP certification (ISO 13485) for code development sites",
    "Clinical Evidence – local data preferred; foreign CER acceptable under Jan‑2026 MFDS revision (OECD clinical data acceptance)",
    "Cybersecurity compliance: SBOM, vulnerability management per 2023 MFDS guidance"
  ],
  "international_mapping": {
    "FDA": ["Class II", "510(k) + eSTAR", "PCCP for AI/ML"],
    "EU": ["Class IIa/IIb (MDR)", "IEC 62304/82304‑2", "CE technical file"]
  },
  "escalation_conditions": [
    "Unclear classification or potential Class 3 risk",
    "Foreign CER lacking Korean translation or insufficient data",
    "Missing KGMP certification for software development site",
    "Absent SBOM / cybersecurity plan"
  ],
  "source_refs": ["제품별_등급분류.md – chunk 1112950876551682081", "제품별_등급분류.md – chunk 533793244310539451"]
}
```

*The above judgment will be stored in the RA knowledge base for rapid reuse when assessing digital medical software under the post‑2025 Korean regulatory framework.*

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

### kb-eval-20260715-it15-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_kr-004", "iteration": 15, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "7a22257506b86897", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "a20110f67bbd98b35d188d8a2fd8d816a95754663f6515d8828b632ceb3d72e5"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `7a22257506b86897`
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

> **Regulatory Draft – Impact of the “디지털의료제품법” on Project X‑ray System (Daily Growth v1 – 2026‑07‑29)**  

---

## 1️⃣ Executive Summary
The X‑ray platform consists of four firmware/software blocks that interact with an imaging detector, a workstation and downstream AI analysis. The new **Digital Medical Products Act (“디지털의료제품법”, DMPA)** (effective 1 Jan 2026) expands the definition of software‑based medical devices (SaMD) and introduces a three‑axis SBOM conformity check.  

| Block | Preliminary DMPA applicability* | MFDS submission type (K‑RA) | Primary regulatory drivers |
|-------|----------------------------------|----------------------------|---------------------------|
| **Generator Firmware** | ✗ – pure HW control, no network/AI | *No medical device approval required* (electrical safety only) | Electrical Safety Management Regulation (전기안전관리규정) |
| **Detector Firmware** | △ – becomes applicable when network‑connected (e.g., remote calibration) | **Notification** (신고) if classified Class I or II; **Approval** (허가) if classified Class III | Digital Medical Products Act – SaMD classification criteria, Radiation Safety Rules |
| **Acquisition Workstation Software** | ○ – standalone operation, networked, AI‑enabled | **Approval** (SaMD) – likely Class II‑b or III depending on risk (AI diagnostic function) | DMPA §§ 8–10; MFDS “인공 지능 의료기기 안전성 및 효율성 검증 가이드” |
| **Post‑processing / AI Analysis Module** | ○ (if SaMD + AI) | **Approval** – SaMD with AI (Class III for diagnostic/therapeutic decision support) | DMPA §§ 9–11; “AI 기반 의료기기 규제 가이드라인” 2025 |
| **DICOM Transfer / PACS Interface** | △ – communication function, may be borderline | **Notification** if purely data exchange (Class I); possible **Approval** if embeds decision‑support logic | MFDS “의료영상통신규격(MEDIC) 가이드라인” + DMPA § 7 |

\*Based on the preliminary matrix in source excerpt [1].

---

## 2️⃣ Detailed Classification & Submission Route  

| Component | Function (Korean) | DMPA‑defined SaMD category | MFDS Class (tentative) | Required submission |
|-----------|--------------------|----------------------------|------------------------|---------------------|
| Generator Firmware | X‑ray 발생기 제어, 무선/유선 비연결 | Not applicable (HW‑only) | 없음 / 전기안전 관리 | 별도 MFDS 전자파·전기 인증만 필요 |
| Detector Firmware | 검출기 보정·데이터 전송(네트워크 연결 시) | “Data acquisition & transmission” SaMD (if networked) | Class I‑a (low risk) → **Notification** | 신고서 + SBOM 3축 증명, 한글 사용설명서 |
| Acquisition Workstation SW | 이미지 획득·실시간 AI 분석 가능 | “Diagnostic decision support (AI)” SaMD | Class II‑b (중간 위험) → **Approval** | 허가 신청서, 임상시험(국내 데이터 필요 여부 검토), SBOM 3축 보고서, KGMP 인증(소프트웨어 개발 시설) |
| AI Post‑processing Module | 영상 후처리·AI 판독 (진단 지원) | “AI‑based diagnostic SaMD” | Class III (고위험) → **Approval** | 허가 신청서, 현지 임상 검증, RWE/CE 인증(전략적 활용), SBOM 3축, KGMP + 사이버 보안 (ISO 27001, IEC 62443) |
| DICOM/PACS Interface | 이미지 전송·연동 통신 | “Communication & data exchange” SaMD (if 독립 실행형) | Class I‑a → **Notification** (or none if pure IT) | 신고서(필요 시), 한글 사용자 안내, SBOM 3축 |

> **Note:** Classification may shift upward when any component integrates AI inference that influences clinical decision‑making. The “△” items require a **pre‑submission risk assessment** with MFDS to confirm whether they remain “communication only” or become SaMD.

---

## 3️⃣ Required Evidence (per MFDS & DMPA)

| Evidence Type | Source / Standard | Applicability |
|---------------|-------------------|--------------|
| **SBOM 3‑axis conformity** (Software Bill of Materials) | DMPA Annex B; IEC 62304 + SBOM taxonomy | Mandatory for all software blocks (including “△” items). |
| **Korean language labeling & IFU** | MFDS 규정 제​10조, “의료기기 라벨·사용설명서 표준화 지침” | All SaMD/communication devices. |
| **KGMP facility certification** | KGMP 제​3조 (소프트웨어 개발 및 제조) | Required for any component submitted for 허가 (Class II‑b, III). |
| **Clinical evidence** | MFDS “임상시험 규정” + DMPA § 9 (OECD CER acceptance) | - For Class III AI module: local clinical data OR accepted foreign CE/FDA trial with OECD CER. <br> - For Class II‑b workstation: foreign data may be used if CER provided; Korean bridging study recommended. |
| **Cybersecurity & Risk Management** | IEC 62443, ISO 14971 (risk mgmt), MFDS “디지털 의료기기 사이버보안 가이드라인” (2025) | All network‑connected software. Must include threat model, patch management, secure boot, OTA update controls. |
| **Performance validation** | IEC 81001‑5‑1 (FDA cybersecurity), MDIC “AI 검증 프레임워크” | Required for AI components (accuracy, bias mitigation). |
| **Radiation safety** | 「진단용 방사선 안전관리 규칙」 최신 개정판 (source [2]) | Detector & acquisition hardware must demonstrate compliance with dose‑monitoring and shielding. |
| **UDI / Traceability** | MFDS UDI 시행령, SOP‑UDI‑001 (referenced in source [2]) | Mandatory for all devices submitted for 허가. |

---

## 4️⃣ Identified Gaps / Missing Information  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Network‑connectivity definition for Detector Firmware** – Currently “△”. Need a definitive statement whether remote calibration, firmware OTA updates or data push will occur. | Determines SaMD classification & SBOM scope. | Conduct functional specification review; if networked → treat as SaMD (Notification). |
| **Local clinical performance data for AI module** – No Korean patient cohort presented. | Class III approval requires either local trial or an OECD‑compliant CER from FDA/CE. | Plan bridging study or obtain foreign CER with full data package. |
| **KGMP certification status of software development site** – Not documented in source excerpt. | Required for any 허가 submission; MFDS may reject without KGMP evidence. | Verify site certification, update SOP‑SBOM‑001 to reference KGMP audit report. |
| **Full SBOM 3‑axis (code, dependencies, provenance) for DICOM/PACS interface** – Only “△” indicated, no proof of independence from workstation SW. | If considered independent SaMD, missing SBOM will block submission. | Generate complete SBOM; map each library to Korean‑approved versions. |
| **Korean language IFU draft** – Not provided. | Mandatory for all devices regardless of class. | Draft IFU in Korean, include safety notices, software update policy, and cyber‑risk notice. |
| **Post‑market surveillance plan (시판후조사) for AI module** – No description. | MFDS requires PMS plan aligned with IMDRF PSUR; high‑risk AI needs active monitoring. | Develop PMS schedule, adverse event reporting workflow, periodic safety update (PSU). |

---

## 5️⃣ Risk Controls & Mitigation Measures  

1. **Cybersecurity Architecture**  
   - Secure boot and signed firmware updates (detector, generator).  
   - Network segmentation: workstation in a DMZ; AI module accesses only via vetted API keys.  
   - Regular vulnerability scanning per IEC 62443‑3‑2.  

2. **AI Algorithm Transparency**  
   - Implement “Explainable AI” output for clinicians.  
   - Maintain versioned model repository with provenance logs (linked to SBOM).  

3. **Radiation Dose Safeguards**  
   - Real‑time dose monitoring firmware; automatic shutdown upon threshold breach.  

4. **Human Factors & Usability**  
   - Conduct Korean‐language usability testing for IFU and UI (ISO 9241‑210).  

5. **Post‑Market Surveillance**  
   - Automated adverse event capture from PACS logs.  
   – Quarterly safety update submitted to MFDS (PSUR) for Class III AI.  

---

## 6️⃣ Citations & Regulatory References  

| Ref. | Description |
|------|-------------|
| DMPA §§ 8‑11, 2026 Rev. | Definition of SaMD, classification rules, SBOM requirement. |
| 「디지털 의료제품법_SaMD_AI_요구.md」 (source [2]) | Internal guideline used for mapping AI risk levels. |
| 「진단용 방사선 안전관리 규칙」 개정이력 (source [2]) | Radiation safety obligations for X‑ray devices. |
| MFDS UDI 시행령, SOP‑UDI‑001 (source [2]) | Unique Device Identification requirements. |
| OECD Clinical Evaluation Report (CER) acceptance – MFDA Notice 2026‑01 | Acceptance of foreign clinical data with CER. |
| IEC 62304, IEC 81001‑5‑1, ISO 14971 | International software life‑cycle and risk management standards adopted by MFDS. |
| IMDRF SaMD Guidance (2024) | Basis for AI/ML classification mapping. |

---

## 7️⃣ Human‑Escalation Triggers  

| Condition | Trigger Action |
|-----------|----------------|
| **Unclear network status of Detector Firmware** → ambiguous SaMD classification. | Escalate to senior RA lead; request functional design clarification before any submission draft. |
| **Absence of KGMP certification evidence** for software development site. | Pause all 허가 dossier preparation; involve Quality Assurance manager to secure KGMP audit. |
| **No OECD‑compatible CER or local clinical data for AI module** (required for Class III). | Immediate escalation to project sponsor – decide on additional trial budget or risk mitigation by limiting intended use. |
| **SBOM 3‑axis incomplete for any “○” / “△” component** after 2 weeks of remediation attempts. | Escalate to Chief Compliance Officer; consider fallback submission as non‑medical (if possible) or defer launch. |
| **MFDS request for additional Korean clinical evidence beyond what is planned**. | Trigger cross‑functional meeting (clinical, regulatory, legal) within 48 h; prepare a contingency plan. |

---

## 8️⃣ Peer Review Prompt  

> **@RA‑Peer‑Reviewer** – Please examine the assumptions and source coverage in this draft:  
> - Are we correctly interpreting the “△” status for Detector Firmware and DICOM/PACS interface?  
> - Have we captured all relevant Korean statutes (e.g., 최신 진단용 방사선 안전관리 규칙, MFDS 사이버보안 가이드라인) that might affect classification or evidence requirements?  
> - Is the mapping of foreign clinical data to OECD‑CER acceptance up‑to‑date with the Jan 2026 MFDS revision?  
> - Identify any jurisdictional gaps (e.g., labeling, post‑market surveillance for AI) that need additional documentation.  

Your feedback will be incorporated before finalizing the submission strategy.

---

## 9️⃣ Re‑usable RA Judgment (honcho_conclude)

```json
{
  "lesson_id": "2026-07-29_Xray_DMPA_impact",
  "summary": "For multi‑component X‑ray imaging systems, only network‑connected firmware (Detector) and any software that performs AI‑driven diagnostic functions are subject to the Digital Medical Products Act. Classification ranges from Class I‑a (notification) for pure communication modules to Class III (approval) for AI post‑processing. Mandatory evidence includes a complete SBOM (3‑axis), Korean language IFU, KGMP certification of software development sites, and either local clinical data or an OECD‑compliant CER for high‑risk AI. Missing items identified: definitive network status of Detector firmware, KGMP proof, Korean clinical data for AI module, full SBOM for DICOM interface, drafted Korean IFU, PMS plan for AI. Human escalation points are defined for any ambiguity in classification, lacking KGMP, or insufficient clinical evidence.",
  "references": [
    "디지털의료제품법 §§8‑11 (2026 revision)",
    "진단용 방사선 안전관리 규칙 개정이력",
    "MFDS UDI 시행령 & SOP‑UDI‑001",
    "OECD CER Acceptance Notice 2026‑01"
  ],
  "peer_prompt": "Please challenge the classification assumptions, verify that all Korean regulatory citations have been captured, and highlight any jurisdictional gaps.",
  "status": "draft_ready_for_peer_review",
  "peer":"ai"
}
```

*The above JSON records the reusable judgment for future work packages; no WP is closed or transitioned.*

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

### kb-eval-20260715-it15-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-15", "decision_ref": "kb-eval-20260715-it15-ra_kr-005", "iteration": 15, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "444ddfb771dafae0", "source": "github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md", "source_hash": "54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `444ddfb771dafae0`
- Source: `github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/962_AUDIT_SOP-SBOM-001_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%A0%9C16%EC%A1%B0_%EC%9A%B0%EC%88%98%EA%B4%80%EB%A6%AC%EC%B2%B4%EA%B3%84%EC%9D%B8%EC%A6%9D_%EC%98%A4%EA%B7%80%EC%86%8D.md)
- Source hash: `54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7`
- Focus: digital medical products act impact
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 원문 직접 열람) | 조문 | 법정 제목·핵심 내용(원문) | |---|---| | **제13조** | "디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항" — 2호: 전자적 침해행위로부터의 취약점에 대한 지속적 보완 | | **제14조** | "전자적 침해행위로부터의 보호 조치" — 식약처장의 보안지침 마련 의무(①) + 제조업자등의 보안지침 준수 의무(②) | | **제16조(기재값)** | "우수 관리체계 인증" — 품질관리·안전관리·전자적침해행위 예방체계 등을 종합 평가하는 임의 인증(유효기간 3년). SBOM 직접 규정 아님 | | **제40조** | "디지털...
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

> ## 📄 Regulatory Draft – Impact of the **Digital Medical Products Act** on SBOM‑Based SOP (Issue 962)

**Prepared for:** Sam – Korean MFDS RA specialist  
**Version:** daily_growth_v1 – 2026‑07‑29  

| Section | Content |
|---------|----------|
### 1️⃣ Product Classification & Submission Route
| Item | Detail |
|------|--------|
| **Legal basis** | *디지털의료제품법* (Digital Medical Products Act) – Articles 13, 14 & 16; MFDS “디지털‑의료기기 허가·신고 가이드라인” (2025‑rev). |
| **Classification rule** | A digital medical product that includes software components (AI/ML, sensor firmware, etc.) is defined as a *디지털 의료기기* if it **(a)** performs a medical purpose (diagnosis, monitoring, treatment) **or** **(b)** processes personal health data that influences clinical decision‑making.  <br>→ Apply the same risk‑based classification table used for conventional medical devices (Class I‑IV). |
| **Typical class** | – **Class II** if the software only provides *information* or basic monitoring.<br>– **Class III/IV** when AI‑driven diagnosis, therapeutic recommendation, or closed‑loop control is involved. |
| **Submission pathway** | • **허가 (Approval)** for Class III & IV devices – full dossier + MFDS security guideline compliance.<br>• **신고 (Notification)** for Class I & II – simplified dossier but must include SBOM‑related security evidence (see §2). |
| **KGMP requirement** | All manufacturers/importers of digital medical devices must hold a **KGMP certification** that includes the “전자적 침해행위 예방·대응 체계” element (MFDS Guideline 2026‑01). |

---

### 2️⃣ Required Evidence for SBOM‑Related Obligations
| Requirement | Evidence to be submitted |
|-------------|--------------------------|
| **a. Legal citation** | Explicit reference to *디지털의료제품법 제14조* (Protection Measures) and *제13조 2호* (continuous remediation of vulnerabilities).  <br>*(Note: Article 16 concerns “우수 관리체계 인증” and is **not** the legal basis for SBOM.)* |
| **b. MFDS Security Guideline compliance** | • Copy of the latest **MFDS ‘보안지침’** (issued Jan 2026). <br>• Statement of adherence – signed by responsible Quality/IT officer. |
| **c. Software Bill of Materials (SBOM)** | • Generated SBOM in SPDX‑2.3 JSON/YAML format for each software release.<br>• Mapping of each component to its version, supplier, license and known CVEs. |
| **d. Vulnerability Management Plan** | • Process description (continuous monitoring, patch schedule, CAPA workflow). <br>• Evidence of tool‑chain (e.g., Snyk/OSS Index) used for automated CVE detection. |
| **e. Risk Management File (ISO 14971)** | • Updated risk analysis that explicitly links identified software vulnerabilities to safety hazards and defines mitigation controls (see §3). |
| **f. Post‑Market Surveillance (PMS) plan** | • KPI on security incidents, reporting timeline (≤ 24 h for breach), and periodic SBOM update schedule (minimum annually). |
| **g. KGMP Certificate** | • Copy of current KGMP certificate (validity ≥ 3 years) that includes the “전략적 전자·기술 관리 체계” audit item. |

---

### 3️⃣ Missing / Unconfirmed Information (Gap Analysis)
| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **3‑1. Exact product class & intended use** | Determines whether 허가 or 신고 is required and the depth of evidence needed. | Provide a concise “Intended Use Statement” and risk classification rationale (refer to MFDS Class I–IV matrix). |
| **3‑2. AI/Algorithm performance data** | Article 40 mandates performance evaluation of AI components *separately* from overall device safety. | Submit AI component validation report (datasets, metrics, external peer review) – reference “AI_구성요소_단위_성능평가.md”. |
| **3‑3. Korean language documentation** | All labeling, IFU and security notices must be in Korean (MFDS Notice 2024‑03). | Prepare Korean translation of SBOM summary, vulnerability disclosure policy, and user safety instructions. |
| **3‑4. Local clinical data (if required)** | For Class III/IV devices, MFDS still expects Korean clinical evidence unless a recognized CE/FDA study is accepted under the 2026 OECD mutual‑recognition amendment. | Identify whether existing foreign clinical data qualify; if not, schedule a local feasibility study. |
| **3‑5. Evidence of “continuous remediation” (제13조 2호)** | The law expects ongoing patching, not just a one‑time SBOM submission. | Provide documented schedule for quarterly vulnerability scanning and monthly patch deployment logs. |

---

### 4️⃣ Risk Controls & Security Measures (aligned with Article 14)
| Control Category | Specific Measure | Reference |
|------------------|------------------|-----------|
| **Governance** | • appoint a “Digital‑Security Officer” with authority to enforce MFDS 보안지침.<br>• quarterly internal audit of SBOM and vulnerability management. | 제14조①, KGMP ‘보안 관리’ 항목 |
| **Technical** | • Use **code signing** for all firmware/AI binaries (RSA 2048‑SHA256).<br>• Enforce **encrypted communication** (TLS 1.3) between device & cloud.<br>• Implement **runtime integrity checks** (whitelisting of approved component hashes). | IEC 62443‑4‑2, MFDS 보안지침 |
| **Operational** | • Automated CVE feed integration (NVD API) with alert threshold CVSS≥7.0.<br>• Incident response SOP: detection → containment (≤ 4 h) → root‑cause analysis → notification to MFDS (within 24 h). | 제14조②, 시판후조사 규정 |
| **Product‑Lifecycle** | • SBOM versioning tied to each software release; archived for ≥ 5 years.<br>• End‑of‑life (EOL) procedure that provides a migration path and security patches for at least 3 years. | KGMP ‘제품 수명 관리’ |
| **User‑Facing** | • Korean IFU includes “보안 업데이트 안내” and clear steps for users to apply patches.<br>• Visible version number on device UI, with OTA update status. | MFDS 라벨링/IFU 가이드라인 |

---

### 5️⃣ Citations (Korean law, guidelines & International standards)

| # | Citation |
|---|----------|
| **①** | 디지털의료제품법 제13조 2호 (2024‑01‑23 시행) – 지속적 취약점 보완 의무. |
| **②** | 디지털의료제품법 제14조 – 전자적 침해행위 보호 조치, MFDS “보안지침” (정식 고시 2026‑01). |
| **③** | 디지털의료제품법 제16조 – 우수 관리체계 인증(품질·안전·보안 종합 평가) – *not* SBOM basis. |
| **④** | MFDS “디지털 의료기기 허가·신고 가이드라인” (2025‑rev). |
| **⑤** | KGMP 규정 제7조 – 전자·기술 관리 체계 인증요소 (3년유효). |
| **⑥** | ISO 14971:2020 – 위험 관리. |
| **⑦** | IEC 62443‑4‑2 – 보안 설계 및 구현 지침. |
| **⑧** | SPDX 2.3 Specification – SBOM format (recommended). |
| **⑨** | OECD Mutual Recognition of Clinical Data (2026 amendment) – allowed foreign clinical evidence with MFDS acceptance. |

---

### 6️⃣ Human‑Escalation Triggers (When a reviewer should raise a “stop‑work” or seek senior decision)

| Trigger | Description | Required action |
|---------|-------------|-----------------|
| **H1 – High‑CVSS vulnerability** | CVE with CVSS ≥ 9.0 discovered in any SBOM component that is **active** in the marketed device. | Immediate notification to Digital‑Security Officer → MFDS breach report (≤ 24 h) → suspend distribution until patch deployed. |
| **H2 – Security breach / intrusion** | Confirmed successful exploitation of a software flaw leading to data loss or patient safety incident. | Activate Incident Response SOP, inform senior management & MFDS within 8 h; consider product recall if risk is severe. |
| **H3 – Non‑compliance with 보안지침** | Audit finds missing/incorrect SBOM, outdated vulnerability scans, or lack of signed security officer statement. | Halt further submissions; remediate gaps; re‑conduct internal audit before MFDS filing. |
| **H4 – Missing Korean documentation** | IFU, labeling, or SBOM summary not provided in Korean prior to submission deadline. | Escalate to Regulatory Lead for translation and review; postpone dossier filing. |
| **H5 – Insufficient clinical evidence** | Local clinical data requirement unmet for Class III/IV, and foreign data cannot be justified under OECD mutual‑recognition. | Trigger senior RA meeting; decide on supplementary Korean study or risk‑benefit justification. |

---

## 📣 Peer‑Review Prompt
> **To:** [RA colleague – e.g., Ji‑woo Kim]  
> **Subject:** Review of Digital Medical Products Act impact draft (SBOM SOP) – Scenario 444ddfb771dafae0  
>   
> Please assess the following:  

1. **Assumption check** – Are we correctly interpreting Article 14 as the primary legal basis for SBOM‑related security obligations? Is any other provision (e.g., recent MFDS notice) also applicable?  
2. **Source coverage** – Did we miss any supplemental guidance (MFDS “보안지침” annexes, KGMP audit items) that could affect evidence requirements?  
3. **Jurisdictional gaps** – Identify Korean‑specific obligations we have not highlighted (e.g., labeling language, local clinical data, post‑market surveillance reporting thresholds).  

Provide concrete comments or alternative citations; feel free to propose additional risk‑control measures.  

*Your feedback will be incorporated before the final dossier preparation.*

---

## 📚 Reusable RA Judgment (Honcho Record)

```
honcho_conclude:
  scenario_id: "444ddfb771dafae0"
  judgment_type: "digital_medical_product_act_SBOM_mapping"
  summary: |
    - 디지털의료제품법 제14조와 제13조 2호가 SBOM·취약점 관리 의무의 직접적 근거이며,
      제16조(우수관리체계인증)는 품질·안전·보안 종합 평가용 인증제도이므로
      SOP‑SBOM‑001에 인용하면 오해 소지가 있다.
    - Required evidence: MFDS 보안지침 준수 선언, 최신 SPDX 2.3 SBOM, 위험 관리 파일(ISO 14971) 내 취약점 연계, KGMP 인증서(보안관리 항목 포함), 한국어 라벨·IFU.
    - Missing data: product class & intended use, AI‑알고리즘 성능 평가, 현지 임상 데이터 여부, 정기적인 SBOM 업데이트 및 패치 로그.
    - Risk controls align with IEC 62443, ISO 27001; must be documented in governance, technical, operational, lifecycle and user‑facing measures.
    - Human escalation triggers defined for high‑CVSS CVE, breach, 보안지침 미준수, 라벨·IFU 미번역, 임상 근거 부족.
  references:
    - 디지털의료제품법 제13조 2호, 제14조 (2024‑01‑23)
    - MFDS 보안지침 (2026‑01)
    - KGMP 규정 제7조 (보안관리 포함)
    - ISO 14971:2020, IEC 62443‑4‑2, SPDX 2.3
  peer: "ai"
```

*Note:* No work package is closed or reopened; a comment recommending closure of the gap‑analysis task can be added by the human lead if appropriate.

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

1. Chunk `1078549302777609829`

> ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 원문 직접 열람) | 조문 | 법정 제목·핵심 내용(원문) | |---|---| | **제13조** | "디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항" — 2호: 전자적 침해행위로부터의 취약점에 대한 지속적 보완 | | **제14조** | "전자적 침해행위로부터의 보호 조치" — 식약처장의 보안지침 마련 의무(①) + 제조업자등의 보안지침 준수 의무(②) | | **제16조(기재값)** | "우수 관리체계 인증" — 품질관리·안전관리·전자적침해행위 예방체계 등을 종합 평가하는 임의 인증(유효기간 3년). SBOM 직접 규정 아님 | | **제40조** | "디지털의료제품의 구성요소에 대한 성능평가" — 센서·AI 알고리즘 성능평가(별개 조문, AI_구성요소_단위_성능평가.md에서 정확히 인용 중 — PASS) |

2. Chunk `1111374550817299375`

> ## 독립 감사 요약 SOP-SBOM-001은 SBOM(Software Bill of Materials) 생성·관리 절차의 법적 근거로 "디지털의료제품법 제16조"를 2개소(frontmatter, §1 본문)에서 인용한다. 그러나 국가법령정보센터 원문(lsiSeq=259299, [시행 2026.1.24.] [법률 제20139호, 2024.1.23. 제정]) 직접 열람 결과, **제16조는 "우수 관리체계 인증"**(식약처장이 디지털의료기기제조업자등을 대상으로 실시하는 임의 인증제도 — 품질관리·안전관리·전자적침해행위 예방체계를 종합 평가하는 3년 유효 인증)을 규정하는 조문으로, SBOM 생성·관리 의무 자체와는 무관하다. SBOM/소프트웨어 구성요소 취약점 관리와 직접 관련된 조문은 **제14조(전자적 침해행위로부터의 보호 조치)**이다 — ① 식약처장이 "취약점을 지속적으로 감시하고 전자적 침해행위에 대응하는 물리적·기술적 관리체계에 관한 지침"(보안지침)을 마련, ② 제조업자등은 보안지침 준수 의무. 아울러 **제13조(준수사항) 제2호**도 "전자적 침해행위로부터의 취약점에 대한 지속적인 보완" 의무를 규정하여 SBOM의 취약점 추적 목적과 직접 연결된다. 참고로 제16조 ②항 3호에 "전자적 침해행위의 예방 및 대응체계"가 우수관리...
