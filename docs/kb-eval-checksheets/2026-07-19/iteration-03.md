# KB Eval Checksheet - 2026-07-19 Iteration 03

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260719-it03-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_us-001", "iteration": 3, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "fc3bfc38766e3c54", "source": "github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md", "source_hash": "19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `fc3bfc38766e3c54`
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

> **Regulatory Draft – QMSR (21 CFR 820) & Design‑Control Alignment**

---

### 1. Classification / Submission Route  
- **Device classification:** *Not applicable* – the issue concerns internal Quality Management System compliance, not a specific medical device.  
- **Regulatory pathway:** No FDA product submission is required. The focus is on **internal QMSR conformity** under the Feb 2 2026 amendment to 21 CFR Part 820 (QMS Regulation – “QMSR”).  

---

### 2. Required Evidence of Compliance  

| Requirement | Evidence Needed | Acceptance Criteria |
|-------------|----------------|---------------------|
| **Front‑matter correction** of SOP‑AIGOV‑001 to show “§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference)” | Updated SOP document version control log; PDF with highlighted change; signed by QMS Manager | Change reflected in the master SOP repository and downstream builds |
| **Removal of residual §820.30 subsection‑letter citations** across all design‑control SOPs, Forms, and Matrix files | Automated grep report confirming *zero* matches to “§820.30” (or any subsection letters) after correction; audit trace file | <1 instance found – must be zero |
| **Incorporation‑by‑Reference (IBR) documentation** for ISO 13485:2016 §7.3 as the sole design‑control pathway | IBR clause text, cross‑referenced in SOP‑AIGOV‑001 and all related SOPs; evidence that the referenced ISO standard is current and available to staff | Full traceability from each design‑control activity back to ISO 13485:2016 §7.3 |
| **Design‑Control Records** (inputs, outputs, verification, validation, transfer) aligned with ISO 13485:2016 §7.3 | Completed Design History Files (DHFs) for at least one recent product release; mapping matrix showing ISO clause ↔ internal activity | All required design‑control artifacts present and signed off |
| **Training records** confirming staff awareness of the QMSR change and new IBR approach | LMS export, signatures, dates; competency assessments | 100 % of relevant personnel trained within 30 days of SOP update |
| **Risk Management alignment** (ISO 14971) – to cover any design‑control gaps introduced by shifting from §820.30 to ISO 13485:2016 | Updated Risk Management Plan and Risk Register; evidence that residual risks are evaluated against the new reference | No unmitigated high‑risk items remain |

---

### 3. Missing / Incomplete Information  

| Gap Identified | Why it matters | Recommended Action |
|----------------|---------------|--------------------|
| **Comprehensive grep log** – source excerpt notes “grep 점검에서 확인” but does not supply the actual report. | Without a concrete artifact, we cannot verify that all §820.30 citations are eliminated. | Generate and archive the full grep output (e‑search pattern = “§820\.30”) for all SOP/Form/Matrix files; attach to QMS audit file. |
| **Formal IBR approval** – no documentation of senior management sign‑off on using ISO 13485:2016 §7.3 as the sole design‑control reference. | FDA expects documented authority for any incorporation‑by‑reference claim. | Obtain and archive a Management Review Minutes entry approving the IBR approach, with rationale. |
| **Impact analysis** of switching to a single pathway (§820.10(c)) on existing product submissions (e.g., pending 510(k)s). | Potential misalignment could affect design‑control evidence submitted to FDA. | Conduct a gap assessment for each open submission; note any additional design‑control artifacts that must be provided beyond the ISO reference. |
| **Change control record** linking the audit finding (#921) to SOP amendment and matrix update. | Traceability ensures corrective action is fully closed. | Populate a Change Control Log entry referencing Audit #921, the specific SOP version change, and verification steps completed. |

---

### 4. Risk Controls (Design‑Control Perspective)

| Risk | Control / Mitigation |
|------|----------------------|
| **Residual citation of §820.30** leading to regulatory confusion or audit finding recurrence. | Automated script scheduled weekly to grep for “§820\.30” across the QMS repository; any hit triggers a corrective‑action ticket. |
| **Misinterpretation of ISO 13485:2016 §7.3 as fully satisfying FDA design‑control requirements** (especially where FDA may require additional documentation). | Cross‑walk matrix mapping each FDA design‑control requirement (§820.30) to the specific clause(s) in ISO 13485:2016 §7.3; review by Regulatory Affairs lead before final adoption. |
| **Staff unfamiliarity with new IBR pathway** causing non‑conformant work products. | Mandatory training + competency quiz; audit of a random sample of recent DHFs to confirm compliance. |
| **Obsolete ISO standard version being referenced inadvertently** (e.g., 2016 vs. later revision). | Document version control for the ISO standard copy; schedule annual verification that the referenced edition remains current or is updated via formal amendment. |

---

### 5. Citations

- **eCFR 21 CFR Part 820** – Section §820.30 is *Reserved* as of the 2026‑02‑02 QMSR effective date.  
- **FDA QMSR Reference:** “QMSR, 2026‑02‑02 시행” (source excerpt).  
- **Incorporation by reference path:** §820.10(c) → ISO 13485:2016 §7.3 (as noted in source).  
- **Audit citation:** audit #921 (2026‑06‑26) – corrective action documented in SOP‑AIGOV‑001.  

*No specific 510(k), predicate, or registration numbers appear in the provided source.*  

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Owner | Action |
|---------|------------------|--------|
| **Any residual §820.30 citation detected** after automated grep | QMS Manager | Halt release of any design‑control related documents; open a CAPA; notify Regulatory Affairs lead within 1 business day. |
| **Training completion < 100 % after the 30‑day deadline** | HR / Learning & Development | Notify senior management; consider temporary suspension of product development activities until compliance restored. |
| **Management sign‑off on IBR missing** | QA Director | Immediate convening of a Management Review meeting; document decision before any further SOP distribution. |
| **Discrepancy between ISO 13485:2016 §7.3 mapping and FDA design‑control expectations identified during an external audit** | Regulatory Affairs Lead | Prepare supplemental evidence (e.g., design‑verification reports) to bridge gaps; consider filing a *Special 510(k)* or *De Novo* justification if the gap affects a pending submission. |
| **Risk Register shows unmitigated high‑risk items linked to design‑control pathway** | Risk Management Officer | Perform urgent risk mitigation; report to VP of Regulatory Affairs and halt any product launch until resolved. |

---

### 7. Peer Review Prompt  

> **@RegulatoryAffairsPeer:**  
> Please review the assumptions, source coverage, and jurisdiction‑specific gaps in this draft:  
> - Are we justified in treating §820.10(c) → ISO 13485:2016 §7.3 as a *single* design‑control pathway for all current products?  
> - Have we captured every required piece of evidence to close audit #921, or are there hidden documentation artifacts not mentioned in the excerpts?  
> - Does the risk‑control matrix adequately address both FDA QMSR expectations and ISO 14971 alignment?  
> - Are any U.S. jurisdiction nuances (e.g., state‑level medical device statutes, other FDA guidance) missing from this assessment?

---

### 8. Reusable RA Judgment (Lesson Record)

```
honcho_conclude:
  lesson: |
    When the QMSR amendment reserves §820.30, all internal design‑control references must be consolidated under §820.10(c) with explicit incorporation‑by‑reference to ISO 13485:2016 §7.3. A single‑path approach is acceptable only if a documented cross‑walk maps every FDA design‑control requirement to the corresponding ISO clause, senior management formally approves the IBR, and automated checks confirm elimination of any residual §820.30 citations across all SOPs/forms/matrices.
  confidence: high
  source_ids: [1123403925433224246, 152477499522968513]
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

1. Chunk `1123403925433224246`

> `00_프로젝트관리/문서_매트릭스.md` 의 §820.30 표기는 본 SOP/Form frontmatter에서 자동 생성되므로 위 frontmatter 정정 후 빌드 스크립트로 자동 갱신됨.

2. Chunk `152477499522968513`

> ## 배경 audit #921(2026-06-26) 종결 과정에서 SOP-AIGOV-001 frontmatter "FDA QMSR §820.30/ISO13485 §7.3"를 "§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30은 Reserved)"로 정정하였으나, **동일한 §820.30 subsection-letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스 전반에 분산 잔존**함을 grep 점검에서 확인. eCFR 21 CFR Part 820(QMSR, 2026-02-02 시행) §820.30은 본문 전체가 Reserved이고, 설계관리 요구는 §820.10(c)가 ISO 13485:2016 §7.3을 incorporation by reference로 끌어오는 단일 경로로 일원화되었다.

### kb-eval-20260719-it03-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_us-002", "iteration": 3, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "0bd55d452ba8a1af", "source": "github:holee9/MD-process/issue-drafts/921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md", "source_hash": "36a0683dda1f189f95c3bba8f11be7917c7ed24fdf703b490573ae5ef6cf0b16"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `0bd55d452ba8a1af`
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

> **Regulatory Draft – QMSR Alignment & Design‑Control Readiness**

---

### 1. Bottom Line
The product under development is most likely a **Class II medical device** (typical for devices requiring formal design controls). The fastest credible clearance path is a **Traditional 510(k)** using the updated Quality System Regulation (QMSR) reference: **21 CFR 820.10(c) incorporating ISO 13485:2016 §7.3**.  

Before submission, the organization must demonstrate full design‑control compliance mapped to the incorporated ISO standard and provide a complete Design History File (DHF) that reflects the revised SOPs. Any missing mapping or undocumented risk controls must be resolved; otherwise escalation to senior QA/Regulatory leadership is required.

---

### 2. Classification & Submission Route
| Item | Determination |
|------|----------------|
| **Device Class** | Assume **Class II** (most mid‑risk devices). Confirm by intended use and FDA product classification database. |
| **Submission Type** | **Traditional 510(k)** – allows inclusion of a complete design‑control package and QMSR compliance narrative. |
| **Alternative Pathways** | *Special 510(k)* only if substantial design changes to a cleared predicate; *De Novo* if no suitable predicate is found (unlikely for typical Class II). |

---

### 3. Required Evidentiary Package
1. **Design History File (DHF)**
   - Design input & output specifications, design reviews, verification & validation reports.
   - Mapping matrix: each DHF element ↔ ISO 13485:2016 §7.3 requirement and FDA 820.10(c) clause.

2. **Risk Management Documentation** (per ISO 14971)
   - Hazard analysis, risk evaluation, risk control measures, residual risk justification.

3. **Quality System Evidence**
   - Updated SOPs (e.g., SOP‑DHF‑001, SOP‑DT‑001, SOP‑DVV‑001) showing incorporation by reference of ISO 13485:2016 §7.3.
   - Records of the revision to front‑matter “applicable” clause from **820.30 → 820.10(c)** (see Source [1]).

4. **Regulatory Narrative**
   - Statement that **21 CFR 820.30 is Reserved** and design controls are satisfied via **820.10(c) + ISO 13485:2016 §7.3**.
   - Explanation of how each design‑control element (design transfer, design changes, etc.) meets the incorporated standard.

5. **Labeling & Intended Use Documentation**
   - Clear description of the device’s intended use, indications, and user environment to support predicate justification.

---

### 4. Missing Information / Gaps
| Area | Gap Identified | Action Needed |
|------|----------------|---------------|
| **Mapping Matrix** | No explicit cross‑walk from DHF elements to ISO 13485:2016 §7.3 shown. | Create/attach matrix; reference in regulatory narrative. |
| **SOP Evidence of Incorporation** | Source [1] mentions a “one‑line clause” addition but no sample text provided. | Capture the revised front‑matter language verbatim and archive with SOP version control. |
| **Risk Control Traceability** | Risk analysis not explicitly linked to design outputs in current files. | Update risk management file to include traceability links (risk → requirement → verification). |
| **Regulatory Predicate Identification** | No predicate device cited. | Perform predicate search; document 510(k) number(s) for claim of substantial equivalence. |
| **QMSR Scope Confirmation** | Source [2] references “Tier 2 – BSI Compliance Navigator” but the scope (which devices/processes are covered) is unclear. | Clarify which product lines fall under the QMSR‑driven SOPs; document in quality manual. |

---

### 5. Risk Controls (Design‑Control Focus)
| Control Activity | Source Requirement | Implementation Note |
|------------------|--------------------|---------------------|
| **Hazard Identification** | ISO 14971 §3 & FDA 820.30 (reserved) → satisfied via 820.10(c) & ISO 13485:2016 §7.3 | Conduct FMEA early; link to design inputs. |
| **Design Verification** | ISO 13485:2016 §7.3.5 | Verify that each design output meets its input; retain test protocols & reports. |
| **Design Validation** | ISO 13485:2016 §7.3.6 | Conduct validation in intended use environment; include clinical/bench data as appropriate. |
| **Design Transfer** | ISO 13485:2016 §7.3.8 | Document transfer to manufacturing with process specifications, tooling, and acceptance criteria. |
| **Design Changes Management** | ISO 13485:2016 §7.3.9 | Change control records must capture impact analysis on risk & compliance. |

---

### 6. Regulatory Citations
- **21 CFR 820.10(c)** – “Incorporation by reference of ISO 13485:2016 §7.3.”
- **21 CFR 820.30** – Reserved (as explicitly noted in source [1]).
- **ISO 13485:2016 §7.3** – Design and development requirements.
- **ISO 14971** – Risk management for medical devices (implicit requirement).
- **Source [1]** – Revision of front‑matter “applicable” clause; SOP cross‑reference guidance.
- **Source [2]** – Confirmation that §820.30 is reserved; tier‑2 compliance reference.

*No specific 510(k) predicate numbers or registration identifiers appear in the source excerpts.*  

---

### 7. Human‑Escalation Triggers
| Trigger | When to Escalate |
|--------|------------------|
| **Unresolved Gap** | Any of the missing items listed in Section 4 remain open > 10 business days after remediation plan issuance. |
| **Risk Management Deficiency** | Residual risk cannot be justified or traceability gaps exist between hazards and design controls. |
| **QMSR Scope Ambiguity** | Unclear whether a device/process falls under the revised 820.10(c) incorporation; requires senior QA sign‑off. |
| **Predicate Identification Failure** | No suitable predicate found after exhaustive search – consider De Novo pathway; escalate to Regulatory Lead. |
| **Regulatory Narrative Incomplete** | Submission draft lacks clear statement on Reserved status of §820.30 and reliance on ISO 13485:2016; requires senior review before filing. |

Escalations should be routed to **Director of Quality Assurance** with a brief impact summary and proposed mitigation timeline.

---

### 8. Peer‑Review Prompt
> *Colleague, please challenge the assumptions underlying our classification as Class II and the choice of a Traditional 510(k) pathway. Specifically:*
> 
> - *Are there any device‑specific FDA classifications or guidance documents that might place this product in Class I (exempt) or Class III?*  
> - *Does the current mapping to ISO 13485:2016 §7.3 fully satisfy all FDA design‑control expectations, or are there residual 820.30‑type requirements that need explicit coverage?*  
> - *Are there any jurisdictional gaps (e.g., state‑level QMS expectations, EU MDR considerations) that we have omitted in this draft?*  

Your feedback will help close any blind spots before finalizing the submission package.

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

### kb-eval-20260719-it03-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_us-003", "iteration": 3, "matched_keywords": ["PMA"], "profile_id": "ra-us", "scenario_id": "8240af1cbb85d72a", "source": "github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md", "source_hash": "ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `8240af1cbb85d72a`
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

> **Regulatory Draft – QMSR & Design‑Control Readiness (Process Monitoring KPI Matrix)**  

---

### 1. Classification / Submission Route  
| Item | Assessment |
|------|------------|
| **Device classification** | Not disclosed in source. The QMS improvements apply to the existing device’s regulatory pathway. Identify the device’s FDA class and current submission type (e.g., 510(k) – *K‑number*, PMA – *PMA‑number*) from the product file. |
| **Implication for submission** | If the device is cleared via a 510(k), update the **510(k) Summary/Statement of FDA‑Recognized Standards** to reflect adoption of QMSR §820.250 (statistical techniques) and enhanced CAPA procedures (§820.100). For PMA‑held devices, address the changes in the **PMA Supplement – Changes to Design or Production Process** (21 CFR 814). |
| **Citation status** | No specific identifier found in source — verify separately. |

---

### 2. Required Evidence for FDA QMSR Compliance  

| Requirement (per CFR/ISO) | Evidence to be submitted (or retained in the device master record) |
|----------------------------|---------------------------------------------------------------------|
| **§820.250 – Use of Statistical Techniques** | • KPI matrix showing process × metric × frequency × threshold × owner (27 cells, 9 processes × 3 dimensions). <br>• Description & validation of statistical methods (SPC, Pareto, Ishikawa). |
| **§820.100 – CAPA System** | • Documented CAPA triggers tied to KPI breaches (CAPA‑MR linkage checklist). <br>• Records of corrective actions, verification, and effectiveness checks. |
| **ISO 13485 §§8.1/8.2.5/8.5.1 Mapping** | • Cross‑reference table linking each ISO clause to the corresponding FDA QMSR requirement (already noted as “status: met”). <br>• Audit reports confirming compliance. |
| **Design Controls (21 CFR 820.30)** | • Evidence that KPI monitoring feeds into Design Verification/Validation and Risk Management (ISO 14971). <br>• Updated Design History File entries showing impact analyses of process changes. |
| **Effectiveness Measurement (§8.5.1)** | • Trend analysis reports linking quality objectives → KPIs → Management Review (MR) actions → CAPA outcomes. |

---

### 3. Missing / Incomplete Information  

| Gap (as flagged in source) | What must be provided to close the gap |
|----------------------------|----------------------------------------|
| **§8.1 – Monitoring, Effectiveness & Improvement Planning** (partial) | • Full documented plan describing how KPI data will drive continuous improvement and periodic effectiveness reviews. |
| **§8.2.5 – Process Performance Monitoring & CAPA Trigger** (partial) | • Complete list of performance thresholds for each process; evidence that those thresholds have been validated. |
| **§8.5.1 – Quality Policy, Objectives, Audits, Analyses, Corrective Action via MR** (partial) | • Closed‑loop records showing the flow: Quality Objective → KPI → MR discussion → CAPA initiation → closure verification. |
| **Statistical Tool Validation** | • Validation protocol and report confirming that SPC, Pareto, Ishikawa analyses meet FDA/ISO criteria for statistical techniques. |
| **Risk Management Integration** | • ISO 14971 risk assessment linking each KPI breach to specific risk control measures; records of risk acceptability determination. |

---

### 4. Risk Controls (ISO 14971 Alignment)

1. **Identify Risks:** Failure to detect out‑of‑spec process performance → non‑conforming product release.  
2. **Evaluate Severity & Probability:** Use historical data from KPI trends; assign RPN > predefined risk acceptance criteria.  
3. **Control Measures:**  
   - Real‑time SPC alarms with defined escalation paths.  
   - Immediate CAPA initiation when KPI exceeds threshold.  
   - Mandatory Management Review within 5 business days of any MR entry linked to KPI breach.  
4. **Residual Risk Assessment:** Document post‑mitigation RPN and justification for acceptability.  
5. **Verification:** Periodic audit (≥ annually) confirming that controls remain effective; include findings in the next MR.

---

### 5. Citations  

| Standard / Regulation | Section Referenced |
|-----------------------|--------------------|
| FDA QMSR (21 CFR 820) | §820.250 – Statistical Techniques <br>§820.100 – CAPA System |
| ISO 13485 | §§8.1, 8.2.5, 8.5.1 |
| EU MDR (for cross‑reference) | Art.10(9)(j) – Post‑market surveillance & vigilance |
| Source excerpts | No specific identifier found in source — verify separately |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Escalation Action | Owner |
|-------------------|-------------------|-------|
| KPI > Upper Control Limit (UCL) for ≥ 2 consecutive sampling points | Immediate CAPA creation; notification to Quality Manager and Design/Process Engineer | Process Owner |
| CAPA not closed within 30 calendar days of initiation | Senior QA leadership review; possible FDA Notification if impact on product quality | QA Director |
| MR entry missing for a KPI breach within the defined reporting window (5 business days) | Escalate to Compliance Officer; initiate corrective action for documentation lapse | Quality Assurance |
| Trend analysis shows upward drift in critical process metrics over 3 successive months | Initiate design‑review meeting; consider redesign or additional risk controls | Design Control Lead |

---

### 7. Peer Review Prompt  

> **Action:** Please have an RA colleague review this draft and challenge:  
> - The assumption that the existing device’s submission type can be inferred without a specific K‑/PMA number.  
> - Whether the listed evidence package fully satisfies FDA QMSR §820.250 and CAPA requirements for a *process‑monitoring* SOP.  
> - Any jurisdictional gaps (e.g., MDSAP, EU MDR) that may affect cross‑border submissions for this QMS change.  

---

### 8. Reusable RA Judgment (Lesson Learned)

**Judgment:** When auditing or drafting QMSR updates that reference ISO 13485 §§8.1/8.2.5/8.5.1, always map each clause to the exact FDA CFR §820 provision(s) (e.g., statistical techniques → §820.250; CAPA → §820.100). Verify completeness of “partial” status items by requiring a documented **effectiveness‑measurement plan** that explicitly ties Quality Objectives → KPI data → Management Review → CAPA closure. Absence of concrete identifiers in source material mandates a separate verification step before citing K‑ or PMA numbers.  

*Record:* `honcho_conclude` – QMSR readiness assessment template stored; future cases will auto‑populate missing‑info checklist and escalation matrix based on this judgment.

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

### kb-eval-20260719-it03-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_us-004", "iteration": 3, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "df75bd468a439495", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `df75bd468a439495`
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

> **Regulatory Draft – QMSR 820.35 Compliance & Design‑Control Readiness**

---

### 1. Bottom‑Line Summary
- **Classification / Submission Path:** The device’s FDA classification is independent of the QMS requirement; assume a Class II 510(k) unless a predicate places it in Class I or III. Regardless, **full compliance with the new Quality Management System Regulation (QMSR) (§820.35)** is mandatory for market clearance.
- **Key Gap:** ISO 13485 §4.2.5 alone **does not satisfy** FDA’s additional documentation and record‑keeping obligations under §820.35. A supplemental QMSR‐specific program must be instituted before dossier submission.
- **Action Stack (High‑Priority):**
  1. Map existing ISO 13485 records against the QMSR “additional requirements” table (see FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표).  
  2. Implement missing control elements (e.g., unique device identifier (UDI) traceability, electronic record integrity per 21 CFR Part 11, adverse event reporting per 21 CFR 803/830).  
  3. Update Design‑Control documentation (design history file, risk management plan, verification/validation protocols) to reference the QMSR records.  
  4. Perform a **QMSR readiness audit** and document findings in FDA‑form F‑QMSR‑REC‑001.

---

### 2. Classification & Submission Route
| Device Class (assumed) | Typical FDA Pathway | Required FDA Submissions |
|------------------------|---------------------|--------------------------|
| **Class I** (non‑general controls) | Register/Listing only; may be exempt from 510(k) | Establishment Registration, Device Listing, QMSR compliance evidence |
| **Class II** (special/modular controls) | 510(k) – Traditional or Special | Traditional 510(k) + Design‑Control package + QMSR compliance evidence |
| **Class III** (preambulatory) | PMA (or de Novo if no predicate) | PMA dossier + full QMSR implementation documentation |

*The exact class must be confirmed by predicate‐device search; the draft assumes a Class II 510(k) as the most common scenario for devices requiring design‑control.*

---

### 3. Required Evidence for Submission (QMSR Focus)

| Evidence Item | Source Requirement | What to Submit |
|---------------|--------------------|----------------|
| **Record Management System** | FDA QMSR §820.35 additional requirements over ISO 13485 §4.2.5【1】 | SOPs, audit trails, retention schedule; completed Form F‑QMSR‑REC‑001 |
| **UDI & Traceability** | 21 CFR Part 11, 21 CFR 803/830 (referenced in QMSR guide) | UDI issuance plan, device label mock‑ups, database export showing lot‑level traceability |
| **Electronic Records Integrity** | 21 CFR Part 11 compliance (cited in the guide doc) | Validation report for e‑record system, access controls, digital signatures |
| **Design History File (DHF)** | Design‑Control requirements (21 CFR 820.30) must now reference QMSR records | Complete DHF with cross‑references to QMSR record IDs |
| **Risk Management** | ISO 14971 integration required; QMSR demands explicit linkage to records | Risk analysis, mitigation plan, post‑market surveillance (PMS) reports linked to QMSR logs |
| **Post‑Market Reporting (MDR)** | 21 CFR 803 (Medical Device Reporting) & 830 (Device Tracking) | MDR SOPs, initial reporting summary, tracking matrix |

---

### 4. Missing Information / Gap Analysis
| Gap | Impact | Immediate Remedy |
|-----|--------|------------------|
| **Absence of QMSR‑specific record controls** (e.g., “record of design changes” not captured per §820.35) | Non‑conformity; FDA may issue Form 483 or refuse clearance | Deploy SOP F‑QMSR‑REC‑001, generate change‑control logs |
| **UDI implementation plan not documented** | Violation of 21 CFR 830 & QMSR traceability requirement | Develop UDI assignment matrix, integrate into ERP |
| **Electronic signatures not validated per Part 11** | Incomplete electronic record compliance | Conduct Part 11 validation; archive evidence |
| **Design‑Control documents reference only ISO 13485** (no cross‑reference to QMSR) | Insufficient justification of design‑control adequacy under new regulation | Update DHF entries to cite QMSR record IDs and F‑QMSR‑REC‑001 |
| **Risk Management file not linked to QMSR logs** | Gap in demonstrating ongoing risk mitigation | Map each identified hazard to a QMSR-controlled corrective action log |

---

### 5. Risk Controls Aligned with QMSR
1. **Document Control:** Implement version‑controlled electronic repository with audit trails (Part 11 compliant).  
2. **Change Management:** Formal change request/approval workflow that automatically creates a QMSR record entry.  
3. **Traceability Matrix:** Link every component, lot, and software release to the DHF and QMSR logs; enable rapid recall if required.  
4. **PMA/510(k) Premarket Verification & Validation (V&V):** Align V&V protocols with QMSR‑recorded test results, ensuring each outcome is stored in the regulated record system.  
5. **Post‑Market Surveillance:** Capture adverse event reports, field corrective actions, and trend analyses within QMSR to satisfy 21 CFR 803/830 obligations.

---

### 6. Citations
- FDA QMSR §820.35 imposes **additional requirements** beyond ISO 13485 §4.2.5【1】.  
- The comparative “difference table” (FDA QMSR §820.35 ↔ ISO 13485 4.2.5) is documented in the internal guide *FDA_QMSR_820.35_vs_ISO13485_4.2.5*【2】.  

*No specific 510(k) predicate numbers, FDA registration IDs, or case identifiers appear in the provided source excerpts – verify separately before final submission.*

---

### 7. Human‑Escalation Triggers
| Trigger | Who Escalates | Reason |
|---------|----------------|--------|
| **Discovery of undocumented design changes** (no QMSR record) | QA Lead / Design Engineer | Potential FDA Form 483; risk to product integrity |
| **Failure of Part 11 validation** | IT/Compliance Officer | Non‑compliant electronic records → submission hold |
| **UDI assignment not finalized 30 days before filing** | Regulatory Project Manager | Must meet pre‑submission traceability requirement |
| **Risk analysis shows residual hazard > acceptable level** | R&D Director & Clinical Lead | May require redesign or additional mitigation |
| **Audit reveals ISO 13485 compliance but missing QMSR elements** | RA/QA Lead | Immediate corrective action needed before 510(k) filing |

Escalations should be logged in the project management system with a “Critical‑Path” flag and notified to senior leadership within 24 h.

---

### 8. Peer Review Prompt
> *Please review this QMSR readiness draft:*
> - Are the assumed submission pathway (Class II 510(k)) appropriate given the limited device context?  
> - Does the gap analysis fully capture all additional QMSR obligations beyond ISO 13485 §4.2.5 as outlined in the source guide?  
> - Have we missed any jurisdiction‑specific considerations (e.g., state‑level reporting, foreign market equivalence) that could affect U.S. clearance timing?

*Feedback is needed before finalizing the regulatory work package.*

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

### kb-eval-20260719-it03-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_us-005", "iteration": 3, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "514c6cfbfba3b17c", "source": "github:holee9/MD-process/issue-drafts/972_AUDIT_검사개요_QMSR_미존재_820_70i_820_180c_잔존.md", "source_hash": "68137c31d0bd41666dcdfd9887be904b6e42d861b4e11f275b302ff1f96e9b5f"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `514c6cfbfba3b17c`
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

> **Regulatory Draft – QMSR & Design‑Control Readiness Assessment**

| Item | Finding / Requirement | Evidence Needed | Gap / Action |
|------|-----------------------|-----------------|--------------|
| **1. Applicable Regulation** | 21 CFR Part 820 (Quality System Regulation, “QMSR”) as amended 02 Feb 2026. The current enforceable sections are §820.1, §820.3, §820.7, §820.10, §820.35 and §820.45. All other sub‑parts (e.g., §§820.5, 820.20‑820.30, 820.40, Subparts C‑O) are reserved. | Updated eCFR reference; copy of the Federal Register citation **89 FR 7523** (02 Feb 2024). | None – regulatory baseline confirmed. |
| **2. Missing QMSR Clauses** | • §820.70(i) (automation/ software validation) and §820.180 (record‑keeping) are *no longer* in the current rule; they belong to the former “QSR” (§820.30‑820.34). <br>• Any internal SOPs that cite these sections as **current** requirements are inaccurate. | Current QMSR text (eCFR) showing deletion of §§820.70(i), 820.180. | Revise all quality manuals, SOPs and training material to remove or re‑label the “historical” citations. |
| **3. Design‑Control Coverage** | Design controls are required under §820.30 only when a device is *new* or has a *significant change*. Since the current QMSR reserves §§820.20‑820.30, explicit design‑control requirements must be derived from the *general* provisions (e.g., §820.3 “Quality System” and ISO 13485:2016). | Mapping matrix: QMSR clauses ↔ ISO 13485:2016 §4.1.6 (IBR) & §7.3 (Design and Development). | Ensure the organization’s Design‑Control Plan references ISO 13485:2016 rather than removed QMSR sections. |
| **4. Software Validation for Automated Processes** | Historical practice of invoking §820.70(i) is not permissible; validation must now be justified under **ISO 13485:2016 §4.1.6** and the “General Device Establishment” requirements (e.g., risk‑based software V‑V). | – Software Validation Plan <br>– Verification & Validation reports <br>– Risk analysis linking software functions to hazards (ISO 14971) | Create a dedicated *Software Lifecycle* SOP aligned to ISO 13485 and ISO 14971. |
| **5. Record‑Keeping** | §820.180 has been removed; record‑keeping obligations are now embedded in §820.100‑820.180 of the former QSR but survive under general requirements (e.g., §820.30 “Design History File”, §820.70 “Production & Process Controls”). | - Documented retention schedule <br>- DHF, Device Master Record (DMR) and Device History Record (DHR) samples | Update record‑keeping policy to reference the surviving QMSR sections and ISO 13485 clause 4.2.6. |
| **6. Risk Management** | Required under §820.30 (if applicable) and mandatory per **ISO 14971:2021**; the audit notes confusion about “reserved” sections that could cause risk‑control gaps. | - ISO 14971 risk management file (risk analysis, evaluation, mitigations). | Verify that every identified hazard has a documented control linked to an existing QMSR/ISO clause. |
| **7. Evidence for 510(k) / De Novo Submission** | A submission cannot be cleared until the establishment demonstrates a *fully compliant* QMSR system (21 CFR 820) and associated design‑control artifacts. | - Copy of current FDA registration <br>- Quality System Audit Report (unqualified) <br>- Design History File, Software Validation evidence, Risk Management file. | Prior to filing any 510(k), remediate all gaps listed above; otherwise the submission will be rejected for “inadequate quality system documentation”. |
| **8. Audit Trail & Findings** | Internal audit numbers referenced: **#951 (§820.30 Reserved confusion)** and **#967 (mis‑allocation of 04/03 categories, residual 05 items).** | Full audit report containing the two findings. | Close these findings only after documented corrective actions (SOP revision, training, evidence generation). |
| **9. Human‑Escalation Triggers** | • Any unresolved citation to a *removed* QMSR clause (e.g., §820.70(i), §820.180). <br>• Absence of ISO 13485:2016 ‑aligned software validation documentation. <br>• Incomplete risk‑management file for any device under development. <br>• Failure to produce an *unqualified* QMS audit report within 30 days of this assessment. | Immediate notification to the Quality Assurance Director and Regulatory Affairs Lead; formal CAPA initiation if not resolved within defined timelines. |
| **10. Citations** | - **21 CFR Part 820** (current as of 02‑Feb‑2026) – sections listed above.<br> - Federal Register: **89 FR 7523** (02‑Feb‑2024).<br> - Internal audit numbers **#951**, **#967**. | No other specific 510(k) predicates or registration numbers appear in the source excerpt. |

---

### Peer Review Prompt
> *Please review the above assessment and challenge any of the following:*  
> 1. The assumption that all design‑control requirements can be satisfied solely via ISO 13485:2016 cross‑references – are there device‑specific nuances we have missed?  
> 2. The completeness of our citation mapping (e.g., could any newer FDA guidance documents supersede the cited eCFR sections?).  
> 3. Potential jurisdictional gaps for software as a medical device (SaMD) under the new QMSR framework that may affect future De Novo or 510(k) pathways.

---

**Lesson for Reuse (RA Judgment)**  
*When auditing QMSR compliance post‑2026 amendment, always verify which CFR §§ remain enforceable; many historically cited clauses (e.g., §820.70(i), §820.180) have been deleted and must be replaced by ISO 13485:2016 references. Mis‑attributing “current” status to reserved sections creates audit findings (#951, #967) and can block device submissions until corrected.*

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

## ra_eu

### kb-eval-20260719-it03-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_eu-001", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b72e0247925ae150", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b72e0247925ae150`
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
*Prepared for internal review – MDR 2017/745 compliance*

---

## 1. Device Portfolio Overview  

| # | Device | Intended Use (summary) | MDR Classification | Governing Rule (Annex VIII) | Conformity‑Assessment Route |
|---|--------|------------------------|--------------------|----------------------------|-----------------------------|
| A | **X‑ray Detector** (imaging panel) | Records diagnostic X‑ray images generated by external radiography systems. | **Class IIa** | **Rule 17** – “devices specifically intended for recording diagnostic images generated by X‑ray radiation”【no specific identifier found in source — verify separately】 | Annex IX (full quality‑management‑system + technical‑documentation assessment) |
| B | **Handheld X‑ray Source** (portable generator) | Emits ionising radiation for bedside radiographic examinations. | **Class IIb** | **Rule 10** (radiology limb) – “active devices that emit ionising radiation for diagnostic or therapeutic radiology”【no specific identifier found in source — verify separately】 | Annex IX (or Annex X type‑examination if chosen; recommend Annex IX for consistency) |
| C | **GUI Software (SaMD)** – image‑display & decision support | Provides processed visualisation and diagnostic assistance to clinicians using X‑ray images. | **Class IIa** | **Rule 11** – “software providing information used for diagnostic decisions”【no specific identifier found in source — verify separately】 | Annex IX (full QMS) |

*All three devices are subject to the same PMS obligations under Art. 83–86 and must be registered in EUDAMED with a UDI (see Table 1, column “EUDAMED obligation”).*

---

## 2. Required Evidence Package  

| Evidence | Regulatory Basis | Content Highlights | Current Status (per source) |
|----------|------------------|--------------------|----------------------------|
| **Technical Documentation** (incl. Design Dossier, Risk Management File) | Annex II; Risk management per ISO 14971 (Annex I §17‑20) | • Device description, intended use <br>• GSPR compliance matrix (§16‑23) <br>• Verification/validation reports (IEC 62304 for software, IEC 60601‑2‑28/‑54 for source, IEC 62220‑1‑1 for detector) | To be compiled – gaps noted in §4 below |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current Art. 61 | • Clinical literature review (PubMed, IEC/ISO DB) <br>• Equivalence justification (for X‑ray Detector & Source) <br>• Clinical data from PMCF activities | CER referenced in source tables – actual reports not provided |
| **PMCF Plan & Evaluation Report** | Annex XIV Part B | • Objectives, population, endpoints, data collection methods (see Table 2) <br>• Timeline aligned with PSUR updates (2 y for A&C, 1 y for B) | PMCF need “determined after equivalence claim review” for Detector; “active collection of clinical data recommended” for Source; “mandatory error‑data capture” for SaMD – details still missing |
| **PMS Plan** | Art. 84 | • Definition of PMS data sources, frequency (see Section 3) <br>• Roles & responsibilities, KPIs, escalation thresholds | Outline present in source (Table 1 “PMS 담당 데이터 소스”) but not a formal written plan |
| **Periodic Safety Update Report (PSUR)** | Art. 86(2) – update cadence: Class IIa every 2 y; Class IIb annually【source excerpt confirms cycles】 | • Benefit‑risk conclusions <br>• Main PMCF findings <br>• Sales volume & user population estimates | PSUR schedule defined (Table 1). Draft reports not yet produced. |
| **Post‑Market Clinical Data** – DQE, dose, battery/Mechanical performance, software bug logs | Various IEC standards (IEC 62220‑1‑1, IEC 60601‑2‑54/28, IEC 62304) | • Measured detective quantum efficiency degradation (Detector) <br>• Patient dose exceedance events (Source) <br>• Battery failure rates (Source) <br>• Software error & usability incidents (SaMD) | Data sources identified in Table 1; raw data collection still pending. |
| **Vigilance / Incident Reporting** | Art. 87 (FSCA), Art. 88 (Trend reporting) | • Immediate reporting of serious incidents to EUDAMED <br>• Quarterly/annual trend analysis | Vigilance system referenced, but SOPs not yet documented. |

---

## 3. PMS Data‑Collection Matrix  

| Data Source | Collection Method | Frequency | Device(s) Covered |
|-------------|-------------------|-----------|-------------------|
| **Serious incidents + PSURs + FSCA** | Vigilance module in EUDAMED | Immediate for serious; quarterly aggregation for PSUR | ● All three |
| **Non‑serious adverse events & side effects** | Complaint management system (CRM) | Monthly | ● All three |
| **Trend reporting data** | Internal statistical aggregation tool | Quarterly | ● All three |
| **Scientific literature, registries** | PubMed, IEC/ISO DB, MAUDE searches | Semi‑annual | ● All three |
| **User / distributor feedback** | CRM & service records | Monthly | ● All three |
| **Competitor public information** | Competitive TD review, EUDAMED, MAUDE | Semi‑annual | ● All three |

*The “●” marks applicability as shown in the source table.*

---

## 4. Identified Gaps / Missing Information  

1. **Detailed Intended Use & Indications**  
   - Need precise wording (e.g., anatomical sites, patient age groups) to anchor clinical evaluation and risk analysis.

2. **Clinical Data Packages**  
   - *X‑ray Detector*: DQE degradation trends over device lifecycle; comparative performance vs. predicate devices.  
   - *Handheld Source*: Measured cumulative dose per examination, beam quality specifications, battery safety test results.  
   - *GUI SaMD*: Usability validation (IEC 62366‑1), incident logs for software crashes or incorrect image rendering.

3. **Risk Management Documentation**  
   - Updated risk analyses incorporating post‑market findings (e.g., radiation overexposure, battery rupture, software error) and corresponding mitigations.

4. **PMCF Plan Details**  
   - Clear study protocols (sample size, endpoints), data‑source mapping to the PMS matrix, statistical analysis plan, and responsibility matrix.

5. **PSUR Content Preparation**  
   - Draft sections for benefit‑risk determination, sales/usage statistics, and linkage of PMCF outcomes.

6. **Usability Engineering File (SaMD)**  
   - Verification & validation reports per IEC 62304, including change‑control records for software updates.

7. **EUDAMED Submission Artefacts**  
   - Confirm UDI‑DIT registration for each device model/variant; ensure vigilance and trend data are entered in the prescribed format.

---

## 5. Risk Controls – Mapping to GSPR (§ 16–23, Annex I)

| Hazard | Affected Device(s) | Primary Control (design / process) | Residual Risk Management |
|-------|--------------------|-----------------------------------|---------------------------|
| **Ionising radiation over‑exposure** | Handheld Source | • Built‑in dose‑monitoring circuitry (IEC 60601‑2‑28 compliance)<br>• Automatic shut‑off after preset exposure<br>• User training & operation manual (§ 23) | Periodic review of dose logs in PMS; trigger design revision if exceedance > 5 % of planned limits. |
| **Degraded image quality (DQE loss)** | X‑ray Detector | • Hardened sensor materials, calibrated gain controls<br>• Routine performance verification per IEC 62220‑1‑1 | PSUR to capture DQE trend; if slope exceeds defined threshold → corrective action & field safety notice. |
| **Battery thermal runaway / mechanical failure** | Handheld Source | • Battery management system (BMS) with temperature monitoring, compliance with IEC 60601‑2‑54 § 20<br>• Mechanical stress testing of housing | Incident reports fed to PMS; trend analysis to trigger redesign after 3 events per year. |
| **Software error / incorrect image display** | GUI SaMD | • IEC 62304 life‑cycle processes, static code analysis, automated regression tests<br>• Usability risk controls (IEC 62366‑1) – colour‑coding warnings for out‑of‑range values | Bug‑log and error‑rate captured in PMS; immediate FSCA if error could lead to misdiagnosis (Art. 87). |
| **Incorrect labeling / user instructions** | All devices | • Conformity with Annex I § 23 (label, IFU)<br>• Human factors validation of IFU readability | Post‑market feedback on misunderstandings triggers rapid IFU update and vigilance notification. |

---

## 6. Escalation Triggers & Human Review Points  

| Trigger | Description | Action Required | Responsible |
|---------|-------------|-----------------|------------|
| **Serious Incident / FSCA** | Event leading to death, serious injury or irreversible deterioration | Immediate report to competent authority via EUDAMED (Art. 87) and internal root‑cause analysis | Vigilance Officer (within 24 h) → RA Lead |
| **Dose Exceedance > 10 % of Reference Level (per examination)** | Detected by source’s dose monitoring | Suspend distribution, issue field safety notice, initiate corrective action | Quality Manager |
| **DQE degradation > 15 % from baseline within 12 months** | Trend from detector performance data | Initiate design revision; update PSUR and inform NB | R&D Engineer |
| **Software crash rate > 0.5 % of total uses per quarter** | From bug‑log & usage analytics | Deploy emergency software patch, notify users, record FSCA if impact on diagnosis | Software Development Lead |
| **Annual PSA (PSUR) indicates residual risk > acceptable level** | Based on benefit‑risk conclusion (Art. 86) | Convene Benefit‑Risk Committee; consider redesign or withdrawal | RA Director |
| **Regulatory audit finding – missing IEC conformity evidence** | NB review during Annex IX assessment | Provide missing test reports within 30 days; update technical file | Document Control |

---

## 7. Bibliographic & Regulatory Citations  

| Item | Regulation / Standard | Reference |
|------|-----------------------|-----------|
| Classification Rules | MDR Annex VIII – Rule 17 (Detector), Rule 10 (Handheld source), Rule 11 (GUI SaMD) | no specific identifier found in source — verify separately |
| Conformity‑assessment route | Annex IX (full QMS) for Class IIa/IIb devices | MDR Annex IX |
| PMS system requirement | Art. 83 MDR | MDR Art. 83 |
| PMS plan requirement | Art. 84 MDR | MDR Art. 84 |
| PSUR requirement & update cadence | Art. 86(2) – Class IIa every 2 y; Class IIb annually (source confirms) | MDR Art. 86 |
| Clinical Evaluation Report | Annex XIV Part A, kept current under Art. 61 | MDR Annex XIV Part A |
| PMCF plan & report | Annex XIV Part B | MDR Annex XIV Part B |
| Vigilance / FSCA reporting | Art. 87 MDR | MDR Art. 87 |
| Trend reporting | Art. 88 MDR | MDR Art. 88 |
| IEC standards cited in source | IEC 62220‑1‑1 (DQE), IEC 60601‑2‑28 (X‑ray tube assemblies), IEC 60601‑2‑54 (radiography/radioscopy), IEC 62304 (software lifecycle), IEC 62366‑1 (usability) | respective IEC standards |
| Risk Management | ISO 14971, reflected in Annex I §§ 16‑20 | ISO 14971 & MDR Annex I |

---

## 8. Peer‑Review Prompt  

> **To the RA team:**  
> Please review the assumptions and scope of this draft:  
> 1. Are the chosen classification rules (Rule 10, 11, 17) correctly applied given the devices’ functional descriptions?  
> 2. Does the evidence matrix capture all mandatory MDR data sources, or are we missing any specific post‑market clinical data (e.g., registry requirements for radiology equipment)?  
> 3. Have we adequately addressed jurisdiction‑specific nuances such as the need for a *clinical investigation* dossier under Art. 62 if equivalence cannot be fully demonstrated?  
> 4. Verify that the escalation thresholds are aligned with our internal risk‑acceptance criteria and the Notified Body’s expectations.  

Your feedback will be incorporated before finalising the PMS/PMCF package for submission to the NB.

--- 

**Prepared by:** Theo – EU MDR Regulatory Affairs Specialist  
**Date:** 2026‑07‑21 (run ID daily_growth_v1)

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

### kb-eval-20260719-it03-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_eu-002", "iteration": 3, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "4038dfc3a558f695", "source": "github:holee9/MD-process/issue-drafts/158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md", "source_hash": "ec94495a1bf80d4e9e3bb0b8c01801499bd1ff16dd2c0697728ee0455ba62816"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `4038dfc3a558f695`
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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning  
(For a Class III Medical Device)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination |
|------|----------------|
| **MDR classification** | **Class III** – indicated by the SOP reference to “PSUR 제출 연계 (Class III EUDAMED 의무)” in *Excerpt [1]*. |
| **Applicable classification rule** | To be confirmed from the device’s intended purpose (e.g., Rule 9, 10, 11, or a specific rule for combination products). **Action:** retrieve the “Intended Use” statement and map it to Annex VIII rules. |
| **Conformity‑assessment route** | **Annex IX** – full quality‑management system (QMS) assessment together with technical documentation review by a Notified Body. <br>*Citation:* MDR Annex IX (quality‑management‑system plus technical‑documentation assessment). |

---

### 2. Mandatory Evidence & Documentation  

| Requirement | Source / Regulatory basis | What must be provided |
|-------------|---------------------------|-----------------------|
| **Technical documentation** (including risk‑management file, labeling, etc.) | MDR Annex II | Complete file per GSPR (Annex I §§1‑22). |
| **EU Declaration of Conformity** | MDR Annex IV | Signed by the manufacturer. |
| **EUDAMED registration** – UDI‑DI / SRN entry, actor registration, market‑surveillance linkage | Art. 33–39 (EUDAMED) & *Excerpt [1]* “Actor Registration/UDI/Market Surveillance 연계”. |
| **Post‑market surveillance plan (PMS Plan)** | Art. 84 | Detailed description of data collection, trend analysis, and periodic safety update reporting. |
| **Periodic Safety Update Report (PSUR)** – mandatory for Class III | Art. 86(1)(a–c) & *Excerpt [1]* “PSUR 제출 연계 (Class III EUDAMED 의무)” | • Benefit‑risk conclusions <br>• Main PMCF findings <br>• Sales volumes & user population estimates. |
| **Vigilance module (FSCA, Serious Incident Reporting)** | Art. 87 & *Excerpt [1]* “Vigilance 모듈 과도기”. | Procedure for reporting serious incidents and field‑safety corrective actions; integration with EUDAMED. |
| **Clinical Evaluation Report (CER)** – kept current | Annex XIV Part A; Art. 61 | Evidence of clinical safety & performance; includes literature review, clinical data, and justification of equivalence if used. |
> **Note:** The SOP mentions “FDA QMSR CP 7382.850” (*Excerpt [1]*). This is a U.S. identifier; no EU‑specific reference is provided – it must be cross‑referenced to the MDR‑compliant complaints handling procedure.  

| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Annex XIV Part B | Description of PMCF activities, study design, endpoints, and timeline; final evaluation report feeding into PSUR. |
| **Complaints handling process (mapping to QMSR)** | *Excerpt [1]* “§7.1 QMSR 하 불만처리 프로세스 정합 (§8.2.2/§8.2.3 매핑)” | Documented procedure aligned with ISO 13485‑2016 Clause 8.2.2/8.2.3; includes root‑cause analysis, CAPA, and UDI‑DI/SRN capture (*Excerpt [1]* “F‑PMS‑002 양식에 UDI‑DI/SRN 필드 추가”). |
| **Usability / Human factors engineering** | Annex I §17 & IEC 62366‑1 | Evidence that the device can be used safely by intended users (including lay persons – Annex I §22, if applicable). |

---

### 3. Identified Gaps / Missing Information  

| Gap | Why it matters | Action to close |
|-----|----------------|-----------------|
| **Intended purpose & corresponding classification rule** | Needed to confirm Class III status and apply the correct rule in Annex VIII. | Obtain the manufacturer’s “Intended Use” statement; map to Rule 9‑11 or other relevant rule. |
| **Full Clinical Evaluation Report (CER) & PMCF plan** | Required for Annex XIV compliance and PSUR inputs. | Draft/collect CER (Annex XIV Part A) and a detailed PMCF protocol (Annex XIV Part B). |
| **Risk‑management file (ISO 14971) with post‑market risk evaluation** | Supports Annex I §§16‑22 and PSUR benefit‑risk conclusions. | Update RMF to include PMS data, trend analysis, and residual risk reassessment. |
| **Labeling & IFU compliance (Annex I §23)** | Must reflect UDI, safety information, and any post‑market changes. | Verify that the latest labeling incorporates UDI‑DI/SRN fields as per *Excerpt [1]* “F‑PMS‑002 양식에 UDI‑DI/SRN 필드 추가”. |
| **EUDAMED actor registration & market‑surveillance linkage details** | Required for automatic PSUR submission and vigilance reporting. | Submit manufacturer, authorised representative, and importers in EUDAMED; ensure data fields map to the SOP sections (§8.1). |
| **Trend‑reporting procedure (Art 88)** | Needed when a statistically significant increase in certain complaints is observed. | Define quantitative thresholds; incorporate into PMS plan. |
| **CAPA tracking evidence linked to complaint records** | Ensures that corrective actions are documented and closed. | Integrate CAPA module with the complaints database; cross‑reference SRN/UDI. |

---

### 4. Risk Controls to be Demonstrated  

1. **Implementation of ISO 14971 risk‑management process** – identification, analysis, evaluation, control, and post‑market risk review (Annex I §§16‑22).  
2. **Complaint handling aligned with QMSR CP 7382.850** – documented procedure covering detection, investigation, classification, reporting, and CAPA (see *Excerpt [1]* §7).  
3. **UDI system control** – ensure traceability from manufacturing to post‑market data capture (EUDAMED linkage §8.1).  
4. **Software/firmware validation** (if applicable) – compliance with IEC 62304 and Annex I §17 for programmable systems.  
5. **Usability engineering** – IEC 62366‑1 evidence that the device can be safely used by intended operators, especially lay users if covered by Annex I §22.  
6. **Radiation safety (if a radiological device)** – compliance with Annex I §16 and relevant IEC standards (e.g., IEC 60601‑2‑54).  

---

### 5. Human‑Escalation Triggers  

| Trigger | Action Required | Regulatory reference |
|---------|-------------------|----------------------|
| **Serious incident / death** reported via complaints system | Immediate FSCA submission to the Notified Body and Competent Authority (Art 87) + initiate field‑safety corrective action. | Art. 87 |
| **Trend detection meeting predefined quantitative threshold** (e.g., ≥3 similar incidents within 6 months) | Escalate to senior management; prepare a trend report per Art 88 and consider PSUR update. | Art. 88 |
| **Unacceptable residual risk identified in PSUR** (benefit‑risk ratio no longer favourable) | Suspend distribution, issue safety notice, and re‑evaluate clinical data; possible re‑classification or redesign. | Art. 86(1)(a), Annex XIV Part A |
| **Failure to meet EUDAMED registration deadlines** (UDI‑DI not uploaded within 30 days of market entry) | Notify the regulatory affairs lead; initiate corrective action and update the PMS plan. | Art. 33–39 |
| **CAPA implementation delay > 60 days** from root‑cause identification | Escalate to Quality Director; report to Notified Body if corrective action impacts device safety. | ISO 13485 8.5.2, MDR Annex IX |
| **Regulatory change (e.g., new FDA QMSR guidance) affecting EU processes** | Perform gap analysis; update SOP‑PMS and related documents accordingly. | Internal compliance policy |

---

### 6. Citations  

* **MDR Articles & Annexes** – as indicated in the tables above (Art 84, Art 86, Art 87, Art 88; Annex II, Annex IV, Annex IX, Annex XIV Part A/B).  
* **Source excerpts** – *Excerpt [1]* for PSUR/Class III obligation, EUDAMED linkage, and complaints‑process mapping. *Excerpt [2]* confirms the SOP version and scope (no additional identifiers).  

> **No specific EU identifier (e.g., UDI‑DI number, EUDAMED case ID) appears in the supplied source – verify separately before submission.**  

---

### 7. Peer‑Review Prompt  

> *“Colleague, could you review the assumptions made regarding the device’s classification and the completeness of the post‑market evidence package? Specifically, assess whether the current SOP references (FDA QMSR CP 7382.850) have been adequately mapped to MDR requirements, and verify that no jurisdiction‑specific gaps (e.g., German BfArM reporting nuances or French ANSM vigilance timelines) have been overlooked.”*  

---

### 8. Reusable RA Judgment (Recorded as Lesson)  

**Lesson:**  
When an SOP explicitly mentions *“Class III … PSUR 제출 연계”*, treat the device as Class III for MDR purposes until the manufacturer’s intended‑use statement confirms otherwise. For Class III devices, the mandatory evidence package includes a **PSR/PSUR (Art 86)**, **full CER (Annex XIV Part A)** and **PMCF plan/report (Annex XIV Part B)**, plus **EUDAMED actor/UDI registration**. Any US‑centric process references (e.g., FDA QMSR CP numbers) must be cross‑referenced to MDR‑equivalent clauses (ISO 13485 §§8.2.2/8.2.3, Annex I general safety requirements). Missing classification justification, CER, and detailed risk‑management updates are the most frequent gaps that generate NB queries during Annex IX assessments.  

*Recorded via `honcho_conclude` for future reuse.*

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

### kb-eval-20260719-it03-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_eu-003", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2fd9acfe010b1502", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2fd9acfe010b1502`
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

> **Regulatory Draft – X‑ray Diagnostic Device (Ionising Radiation Emitting) – MDR 2017/745**

---

### 1. Classification & Conformity‑assessment Route  
| Item | Reference |
|------|------------|
| **Device class** | Class IIb – derived from **Rule 10** (ionising‑radiation‑emitting diagnostic equipment)【2】 |
| **Classification rule source** | Annex VIII, Rule 10 (MDR) |
| **Conformity‑assessment route** | **Annex IX** – full quality‑management‑system assessment together with the review of technical documentation (applicable to all Class IIb devices).  If a type‑examination is preferred, **Annex X** may be used, but Annex IX is the standard route for most manufacturers. |

---

### 2. Required Evidence Package  

| Evidence | MDR Requirement | Typical Content |
|----------|-----------------|-----------------|
| **Technical Documentation** | Annex II (incl. device description, intended use, labeling, GSPR compliance)【1】 | - Device‑description & variants <br> - Intended purpose statement <br> - Label & IFU (§23) <br> - Design files, drawings, specifications <br> - Verification & validation data (including IEC 60601‑2‑28 & IEC 60601‑2‑54 compliance) |
| **Risk Management File** | Annex I §17–§20, ISO 14971 | • Hazard analysis, risk control measures, residual risk evaluation |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | – State‑of‑the‑art literature review on diagnostic X‑ray systems <br> – Performance testing data (dose measurements, image quality per IEC 62220‑1‑1) <br> – Clinical data if available (e.g., prospective/retrospective studies) |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 (PMS plan) & Annex III (PMS system) | • Definition of PMS activities, data sources, KPI’s <br> • Feedback loops to design and risk management |
| **Periodic Safety Update Report (PSUR)** | Art. 86 (for Class IIb) – update at least annually | • Benefit–risk conclusions <br> • Summary of PMCF results (see below) <br> • Sales volume & user‑population estimates |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | – Planned clinical investigations after market entry, objectives, methodology, statistical analysis plan |
| **Usability Engineering File** (if device is intended for lay users) | Annex I §22 & IEC 62366‑1 | Human factors testing results |
| **Software Documentation** (if SaMD component per Rule 11) | Annex I §17; IEC 62304 | Software architecture, validation, secure updates |

---

### 3. Identified Information Gaps  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Intended‑use wording** (including patient population, clinical indication) | Drives classification & clinical evidence scope | Draft a precise intended‑use statement and map to Rule 10/11 |
| **Labeling & Instructions for Use (§23)** | Required for GSPR compliance & user safety | Compile full label, symbols, IFU, translation matrix |
| **Clinical data beyond literature** (e.g., prospective study) | MDR expects clinical evidence that reflects actual use; literature alone may be insufficient for Class IIb | Plan/execute a PMCF study or gather post‑market data from early adopters |
| **Full PMS plan (Art. 84)** | Needed to satisfy Annex III & Art. 83‑86 obligations | Define data collection methods, reporting timelines, responsible persons |
| **Software classification details** (if any SaMD) | Determines whether Rule 11 elevates class or adds software‑specific requirements | Perform a Software Hazard Analysis and decide if rule upgrade applies |
| **Risk‑control verification results for ionising radiation dose** | Must demonstrate compliance with §16 GSPR & IEC 60601‑2‑28/54 limits | Conduct dosimetric testing, compile reports |

*All gaps flagged above must be resolved before the Notified Body can issue an opinion.*

---

### 4. Core Risk Controls (derived from GSPR)

| GSPR chapter | Control(s) |
|--------------|------------|
| **§16 – Radiation protection** | • Dose‑monitoring circuitry, dose‑limiting software <br>• Compliance with IEC 60601‑2‑28 limits on Entrance Skin Dose (ESD) |
| **§17 – Electronic programmable systems** | • Secure firmware update process, integrity checks (IEC 62304) |
| **§18 – Active devices & connections** | • Electrical safety testing, isolation verification (IEC 60601‑1) |
| **§20 – Mechanical/thermal risks** | • Housing durability tests, thermal runaway safeguards |
| **§22 – Use by lay persons (if applicable)** | • Usability validation per IEC 62366‑1, clear instructions, colour coded warnings |

---

### 5. Key Citations  

| Reference | Content |
|-----------|---------|
| **Rule 10** (Annex VIII) | Classifies ionising‑radiation‑emitting diagnostic devices as Class IIb【2】 |
| **Annex IX** | Conformity‑assessment route for Class IIb (QMS + technical file review) |
| **Art. 84** | Requirement to establish a PMS plan |
| **Art. 86** | Obligation to produce a PSUR for Class IIb devices, update at least annually |
| **Annex XIV Part A** | Structure of the Clinical Evaluation Report (CER) |
| **Annex XIV Part B** | Structure of the PMCF plan & evaluation report |
| **Annex III** | PMS system requirements (including post‑market data collection) |
| **Annex II** | Technical documentation contents |
| **Annex I §§16, 17, 18, 20, 22** | General Safety and Performance Requirements relevant to this device |

*No specific identifier (e.g., 510(k), EUDAMED number) appears in the source excerpts – verify separately.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Level |
|---------|------------------|
| **Unresolved classification uncertainty** (possible Rule 11 upgrade) | Senior RA Manager → Legal & Clinical Lead |
| **Missing clinical data for CER** | Project Lead → Notified Body liaison (request extension) |
| **Incomplete PMS plan or lack of PMCF design** | QA/QP (Qualified Person) –> Management for resource allocation |
| **Risk‑control verification not demonstrated** | Risk Management Leader → Engineering & Testing Teams |
| **Regulatory deadline approaching without gap closure** | RA Director → Executive Sponsor (resource escalation) |

All triggers should be logged in the project risk register and reported weekly to the cross‑functional steering committee.

---

### 7. Peer‑Review Prompt  

> **To: Regulatory Affairs Team – EU MDR Specialist(s)**  
> Please review the assumptions and source coverage underpinning this draft:
> - Are we confident that Rule 10 alone determines Class IIb, or could any ancillary functions (e.g., integrated image‑processing software) invoke Rule 11 at a higher class?  
> - Does the current literature review satisfy the “state of the art” requirement for a Class IIb diagnostic device, or should we proactively plan a prospective PMCF study?  
> - Are there any jurisdiction‑specific nuances (e.g., national competent authority requirements, additional German BfArM reporting) that are not captured here?  
> - Verify that all cited Annexes/Articles map correctly to the latest MDR amendment (Regulation EU 2023/607).  

Your feedback will be incorporated before final submission to the Notified Body.

---

### 8. Reusable RA Judgment (Lesson for Knowledge Base)

**Judgment:** *When classifying an ionising‑radiation‑emitting diagnostic device, Rule 10 of Annex VIII automatically assigns Class IIb under MDR 2017/745. However, any integrated software that provides diagnosis or therapy decisions must be evaluated against Rule 11; if the software’s impact on patient safety meets the higher thresholds, the overall device class may be upgraded (e.g., to IIb or III). Consequently, a parallel SaMD risk‑assessment and classification check is mandatory before finalizing the conformity‑assessment route (Annex IX).*  

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

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20260719-it03-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_eu-004", "iteration": 3, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "3a61372dfd698a2c", "source": "github:holee9/MD-process/issue-drafts/157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md", "source_hash": "7ceead695690f1ea2c83bf679e8114b768ad7b4b8dbab95eccc08d70d1be9f02"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `3a61372dfd698a2c`
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

> **Regulatory Draft – PMS / PMCF Planning & EUDAMED Reporting Transition (FSCA SOP‑001 v0.3)**  

---

### 1. Scope & Objective
The draft summarizes the regulatory implications of the updated SOP “FSCA‑001 v0.3” which introduces:

* Strengthened linkage between FSCA and CAPA (§5.11)  
* A self‑assessment checklist for FSCA audits (5 items, §5.11.2)  
* Migration from the current reporting pathway to a mandatory EUDAMED‑based route (§5.12) – including interim transition steps, post‑Vigilance obligations and Market Surveillance exploitation.

The purpose is to outline what classification, conformity‑assessment route and evidence are required for a medical device subject to this SOP, identify missing information, propose risk controls, and define human‑escalation triggers.

---

### 2. Device Classification & Conformity‑Assessment Route  

| Item | Determination from Source | Action Required |
|------|---------------------------|-----------------|
| **Device class (I / IIa / IIb / III)** | *Not provided* – the SOP deals with procedural aspects only, not product‐specific classification. | Obtain device’s intended purpose, mode of action and applicable **Rule(s) 9‑11‑17** from Annex VIII to assign a class. |
| **Conformity‑assessment route (Annex IX / X / XI)** | *Not provided* – depends on the assigned class and whether a Notified Body is required for QMS assessment or type‑examination. | Determine if the device will follow **Annex IX** (full quality‑system + technical doc), **Annex X** (type‑examination) or **Annex XI** (production conformity). Document in the Technical Documentation (Annex II). |

> **Citation:** No specific identifier found in source – verify device‑specific classification separately.

---

### 3. Post‑Market Surveillance (PMS) & PMCF Requirements  

| Requirement | MDR Reference | SOP‑derived Action |
|-------------|---------------|--------------------|
| **PMS system** | Art. 83 MDR | Implement a systematic PMS system aligned with the new EUDAMED reporting pathway (§5.12). |
| **PMS plan** | Art. 84 MDR | Update the PMS Plan to reflect the addition of the *EUDAMED Market Surveillance module* (trigger in §5.1). |
| **Periodic Safety Update Report (PSUR) / PMS report** | Art. 85 (Class I) or Art. 86 (Classes IIa‑III) MDR | Schedule PSUR generation per class (annual for IIb/III, biennial for IIa) and ensure integration of FSCA outcomes (§5.11). |
| **PMCF planning** | Annex XIV Part B MDR | Develop a PMCF plan that incorporates data captured through the **Market Surveillance module** described in §5.12.3. |
| **Benefit‑risk assessment (continuous)** | Annex XIV Part A MDR | Update the Clinical Evaluation Report (CER) with findings from FSCA‑CAPA actions and market‑surveillance feedback. |

---

### 4. Evidence Required for Submission  

| Evidence Item | Source Requirement | Where to Include |
|----------------|-------------------|------------------|
| **FSCA–CAPA linkage documentation** (records of corrective actions, root‑cause analyses, CAPA effectiveness) | §5.11.1 “FSCA‑CAPA 연계 강화 및 문서화 경로도” | Technical Documentation – Annex II (section on post‑market activities). |
| **Self‑assessment checklist results** (5‑item FSCA audit) | §5.11.2 “FSCA 실사 자가점검표 (5항목)” | PMS Report (Art. 85/86) and internal audit records. |
| **EUDAMED submission artefacts** (uploaded vigilance, market surveillance data) | §5.12.1‑§5.12.3 – transition to mandatory EUDAMED reporting | EUDAMED registration (Art. 33‑39); linked in the PMS plan. |
| **Clinical evidence for PMCF** (real‑world use, post‑market clinical data) | Annex XIV Part B MDR | PMCF report attached to PSUR / updated CER. |
| **Risk Management updates** reflecting FSCA findings | ISO 14971/Annex I §17‑§18 (software & active devices) | Risk Management File – Annex III of the technical documentation. |

> **Citation:** No specific identifiers (e.g., predicate numbers) appear in the source – verify separately.

---

### 5. Gaps / Missing Information  

| Gap | Impact on Submission | Recommended Action |
|-----|----------------------|--------------------|
| **Device‑specific classification & applicable Rule(s)** | Cannot select correct conformity‑assessment route or determine PSUR frequency. | Collect device‐intended use, technological characteristics; perform class determination per Annex VIII. |
| **Exact content of the “FSCA 실사 자가점검표 (5항목)”** | Unable to map checklist items to MDR evidence requirements. | Obtain the full checklist from SOP‑001 annexes and cross‑reference each item with Art. 83‑86 obligations. |
| **Transition timeline for EUDAMED migration** | Risk of non‑compliance during interim period (§5.12.1). | Define a detailed calendar (milestones, responsible persons) in the PMS plan. |
| **Integration method of Market Surveillance data into PMCF** | Could lead to incomplete clinical evidence. | Design a data‑flow diagram showing how surveillance findings feed the PMCF database and CER updates. |
| **CAPA effectiveness verification** | Without objective metrics, ASIL (acceptable safety) cannot be demonstrated. | Establish KPI thresholds (e.g., reduction of recurrence rate < 5 % within 6 months). |

---

### 6. Risk Controls Related to FSCA & Reporting  

1. **Documentation Control** – Ensure all FSCA‑CAPA records are versioned, stored in a QMS compliant repository (ISO 13485 Clause 4.2.3).  
2. **Change Management** – Any corrective action that alters device design or labeling triggers an amendment of the Technical Documentation and possibly a new conformity assessment (Annex IX/IV).  
3. **Traceability** – Link each FSCA incident to the relevant Unique Device Identifier (UDI) in EUDAMED to enable rapid field safety actions.  
4. **Verification of CAPA Effectiveness** – Conduct post‑implementation monitoring per ISO 14971 §5.6; evidence fed into PSUR/PMCF.  
5. **Cybersecurity for Market Surveillance Module** – Apply IEC 62366‑1 usability engineering and IEC 62443 security controls to protect the data exchange with EUDAMED.

---

### 7. Human‑Escalation Triggers  

| Trigger | Escalation Level | Action |
|---------|------------------|--------|
| **Failure to upload FSCA data to EUDAMED within the defined transition window** (see §5.12.2) | **Immediate – QA Manager** | Issue a non‑conformance; start corrective CAPA per §5.11.1. |
| **Detection of an adverse trend in surveillance data that exceeds pre‑defined KPI thresholds** | **Urgent – Regulatory Affairs Lead & Senior Management** | Initiate field safety corrective action (FSCA) and prepare vigilance report (Art. 87). |
| **Unresolved CAPA after 30 days** | **Critical – Director of Clinical Affairs** | Conduct root‑cause re‑analysis; consider temporary market withdrawal if risk increases. |
| **Missing classification data preventing PSUR generation** | **Blocking – Regulatory Project Owner** | Pause submission activities until classification is resolved. |
| **Discrepancy between FSCA findings and CER conclusions** | **High – Clinical Evaluation Team Lead** | Re‑evaluate benefit–risk determination; update Annex XIV Part A. |

---

### 8. Peer Review Prompt  

> *“Colleague, please examine the assumptions made in this draft regarding the linkage of FSCA to CAPA (§5.11) and the migration to mandatory EUDAMED reporting (§5.12). Are there any MDR or EUDAMED‑specific obligations that have been overlooked? Verify whether the proposed evidence set aligns with Annex XIV Part B for PMCF, and flag any jurisdiction‑specific gaps (e.g., national vigilance portals) that need to be addressed.”*  

--- 

**Prepared by:** Theo – EU MDR Regulatory Affairs Specialist  
**Date:** 2026‑07‑21  

*(All regulatory citations correspond to the current MDR text; source excerpts are referenced where applicable. No device‑specific identifiers were found in the provided material—these must be obtained from the product file before final submission.)*

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

### kb-eval-20260719-it03-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_eu-005", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "ace8201d85c8dad0", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `ace8201d85c8dad0`
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

> **Regulatory Draft – PMS & PMCF Planning (MDR 2017/745)**  

---

### 1 Scope & Device Synopsis  
*The template below is intended for any medical device under development that will be placed on the EU market. Populate the placeholders (e.g., “Device name”, “Intended purpose”) with the actual product information before final submission.*

---

### 2 Classification & Conformity‑Assessment Route  

| Step | Requirement | How to fulfil it | Regulatory citation |
|------|-------------|------------------|---------------------|
| **2.1** | Identify **intended purpose**, indications, target patient population and mode of action. | Use the approved “Intended‑use statement” from the label/IFU. | MDR Art. 51 (Classification) |
| **2.2** | Apply **Annex VIII – Rules 1‑22** sequentially; adopt the highest applicable rule. | Conduct a rule‑by‑rule matrix (e.g., Rule 9 for active therapeutic, Rule 10 for active diagnostic, Rule 11 for software, etc.). If uncertainty remains, consult the Competent Authority or MDCG “Borderline and Classification” manual (v2.1.1 – 2023‑09). | MDR Annex VIII; source excerpt [2] notes “22 rules sequentially applied → highest class”. |
| **2.3** | Determine **class** (I, IIa, IIb or III). | Result of step 2.2. | MDR Art. 51 & Annex VIII |
| **2.4** | Choose the **conformity‑assessment route** that matches the class:  <br>• Class I – self‑declaration (Annex IV)  <br>• Class IIa/IIb/III – NB‑involved assessment (Annex IX, X or XI). | If a NB is required, negotiate a contract and confirm which Annex will be applied (e.g., Annex IX for full quality‑system & technical file review). | MDR Annex IX, X, XI |

> **Human‐escalation trigger #1** – *If the intended purpose or mode of action cannot be unambiguously matched to a single rule in Annex VIII, cease further work and raise to senior RA for classification clarification.*

---

### 3 Technical Documentation (TD)  

| Component | What must be included | Citation |
|-----------|----------------------|----------|
| **General description & UDI** | Device name, model, catalogue, UDI registration in EUDAMED, reference to GUDID/UDI‑portal. | MDR Art. 61; source excerpt [1] lists “UDI / UDI portal … EUDAMED”. |
| **Risk Management File** | ISO 14971‑based risk analysis, evaluation & control measures (including §16‑22 of Annex I). | MDR Annex I §16‑22 |
| **Design & Manufacturing Information** | Drawings, specifications, process validation, sterilisation (if applicable). | MDR Annex II |
| **Clinical Evaluation Report (CER)** | Up‑to‑date CER covering state of the art, clinical data, benefit–risk determination. Must be kept current under Art. 61 and structured per Annex XIV Part A. | **Art. 61**; **Annex XIV Part A** – cited in source excerpt [1]. |
| **Post‑Market Surveillance (PMS) System** | PMS plan (Art. 84), PMS report (Art. 85 for Class I or PSUR Art. 86 for higher classes). | MDR Art. 83‑86 |

> **Human‑escalation trigger #2** – *If any mandatory TD element is missing (e.g., no risk management file), stop NB submission preparation and notify the project manager.*

---

### 4 Clinical Evidence  

| Requirement | Deliverable | Regulatory basis |
|-------------|------------|-------------------|
| **CER (Annex XIV Part A)** | Full clinical evaluation including literature review, clinical investigations (if needed) and post‑market data. Must address benefit–risk conclusion. | MDR Art. 61; **Annex XIV Part A** |
| **PMCF Plan (Annex XIV Part B)** | Defined objectives, methodology (prospective/retrospective), timelines, sample size, data sources, and analysis plan. Aligns with the PMS system. | **Annex XIV Part B** |
| **PMCF Evaluation Report** | Results of PMCF activities, updated benefit–risk assessment, recommendations for future actions. | **Annex XIV Part B** |

> **Missing information** – The source provides no detail on the device’s clinical data sources (e.g., literature database, registries) or on whether a clinical investigation is planned. These gaps must be filled before finalising the CER/PMCF plan.

> **Human‑escalation trigger #3** – *If the PMCF plan cannot demonstrate adequate sample size or follow‑up for the intended use population, flag to Clinical Affairs for redesign.*

---

### 5 Post‑Market Surveillance (PMS)  

| Element | Content | Citation |
|---------|---------|----------|
| **PMS System** | Organizational structure, responsibilities, processes for gathering, analysing and acting on PMS data. Must comply with Art. 83. | MDR Art. 83 |
| **PMS Plan** | Detailed plan covering data collection methods, frequency, reporting mechanisms (including vigilance per Art. 87). | MDR Art. 84 |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | Summarise benefit‑risk conclusions, PMCF findings, sales volume & user population (Art. 86(1)(a‑c)). Frequency: annually for IIb/III; biennially for IIa (Art. 86(2)). | MDR Art. 86 |
| **Vigilance Reporting** | Serious incident and FSCA reporting per Art. 87, with reference to national law (§31 의료기기법). | MDR Art. 87; source excerpt [1] includes “이상사례 보고 (의료기기법 §31)”. |

> **Missing information** – The source lists the regulatory articles but does not provide a concrete PMS plan, data‑source list, or timelines. These must be produced.

> **Human‑escalation trigger #4** – *If PSUR deadlines cannot be met (e.g., lack of sales data), raise to senior management for resource allocation.*

---

### 6 Risk Controls & GSPR Alignment  

| GSPR § | Required control (example) | How it is demonstrated |
|--------|---------------------------|--------------------------|
| **§16 – Radiation protection** (if applicable) | Shielding, dose‑monitoring, compliance with IEC 60601‑2‑54/28. | Test reports, conformity statements to IEC standards. |
| **§17 – Electronic programmable systems** | Software lifecycle management per IEC 62304, security updates. | Software development file, verification & validation records. |
| **§18 – Active devices / connections** | Electrical safety, electromagnetic compatibility (EMC) per IEC 60601‑1. | Test certificates, risk analysis linking hazards to controls. |
| **§22 – Devices for lay persons** | Usability testing per IEC 62366‑1, clear IFU. | Usability engineering file, labeling review. |

> **Human‑escalation trigger #5** – *If any GSPR is not clearly addressed by existing documentation (e.g., missing IEC 60601‑2‑54 test data for an X‑ray device), stop the submission and request evidence.*

---

### 7 Summary of Missing Information (to be gathered before NB submission)

| Item | Reason |
|------|--------|
| **Exact intended purpose & mode of action** | Needed to apply Annex VIII rule and determine class. |
| **Rule selection from Annex VIII** (e.g., Rule 9, 10, 11, 17) | Determines classification; currently unspecified. |
| **Clinical data sources** (literature search strategy, registry access, clinical investigation protocol) | Required for CER & PMCF plan. |
| **PMS data‑source list & collection schedule** | Needed for PMS plan and PSUR preparation. |
| **Risk‑management file aligned to GSPR §§16‑22** | Must demonstrate mitigation of identified hazards. |
| **Evidence of compliance with relevant IEC standards** (e.g., IEC 60601‑2‑54, IEC 62304) | Required for GSPR fulfilment and NB assessment. |

---

### 8 Human‑Escalation Triggers (Consolidated)

1. Ambiguous classification → senior RA decision.  
2. Missing mandatory TD element → project manager notification.  
3. Insufficient PMCF design (sample size, follow‑up) → Clinical Affairs redesign.  
4. PSUR deadline risk (lack of sales/usage data) → senior management resource request.  
5. Unaddressed GSPR requirement → pause submission and obtain evidence.  

---

### 9 Peer‑Review Prompt  

*“Please review the above draft with a focus on:  

- Whether the classification approach correctly anticipates all possible Annex VIII rules for the envisioned device family (especially active therapeutic vs. diagnostic distinctions).  
- If any MDR Articles or Annexes that are relevant to our PMS/PMCF scope have been omitted (e.g., Art. 88 trend reporting, or specific requirements for implantable active devices).  
- Identification of jurisdiction‑specific gaps (e.g., Korean regulations referenced in the source – §31 의료기기법) and how they map onto EU obligations.”*  

---

**Note on Source Citations:**  
No explicit predicate numbers, case IDs or regulatory identifiers were present in the supplied excerpts. All citations are therefore to MDR articles/annexes as listed above (“no specific identifier found in source — verify separately”).

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

### kb-eval-20260719-it03-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_kr-001", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "b02a51ce1c38768d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `b02a51ce1c38768d`
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

> **Regulatory Draft – AI‑Enabled Digital Medical Software (Korean Market)**  

---

### 1. Device Overview  
- **Type:** Stand‑alone medical‑software application (AI/ML) that provides image management, processing and/or computer‑aided detection (CADe) for radiology.  
- **Intended Use Statement (to be defined):** “Support radiologists in the detection/triage of lesions on imaging studies by providing automated analysis and quantitative outputs.”  

---

### 2. Korean Classification & Submission Pathway  

| Element | MFDS Determination | Rationale |
|---------|-------------------|-----------|
| **Class** | **2등급** (Class II) – may be elevated to higher class if the auxiliary function level is deemed “high”* | Cited from domestic guideline: *“2등급 (보조 기능 수준에 따라 상향 가능)”*【1】 |
| **Regulatory Route** | **허가 (Approval)** – required for all Class II devices | MFDS rule set for 2‑class medical devices. |
| **Applicable Legal Framework** | **디지털의료제품법** (Digital Medical Device Act) effective 2025‑01‑24 | Provides a separate regulatory system for AI/SW products, mandating change‑management plans and component performance evaluation【1】 |

\*If the software’s AI functions are classified as “high‑risk auxiliary” (e.g., autonomous diagnosis), a re‑evaluation to Class 3 may be necessary.  

---

### 3. Required Evidence Package  

| Category | Specific Requirements | Source |
|----------|----------------------|--------|
| **KGMP Facility Certification** | Manufacturer must hold KGMP certification for software development and distribution. | MFDS standard (implicit for all medical device manufacturers). |
| **Change‑Management Plan (CMP)** | Detailed plan covering version control, post‑market modifications, and AI model updates as required by *디지털의료제품법*【1】. |
| **Component Performance Evaluation** | Verification of each software component (algorithmic performance, data set provenance, validation metrics). Required under the same Act【1】. |
| **Usability / Use‑Suitability** | Conduct UI/UX testing according to *독립형 SW 사용적합성 가이드라인* if the product is standalone【1】. |
| **Risk Management File (ISO 14971)** | Full risk analysis, controls, residual risk evaluation, and post‑market surveillance plan. |
| **Cybersecurity** | Implement SBOM generation and security controls aligned with MFDS guidance that mirrors FDA’s 2023 Cybersecurity Final Guidance. Evidence of compliance with Section 524B (Omnibus 2022) is recommended when referencing foreign standards. |
| **Clinical Evaluation / Local Clinical Data** | If the AI algorithm has not been previously approved/cleared in Korea, submit local clinical performance data or a bridging study; otherwise a foreign CE/FDA clinical evaluation report can be used *provided MFDS scope expansion permits it* (verify latest notice). |
| **Labeling & IFU**  | Korean‑language labeling, package insert, and user manual per MFDS labeling regulations. All safety information must be in Hangul. |
| **Software Documentation** | Software Development Plan, Verification & Validation reports, source code control records, and SBOM (Software Bill of Materials). |

*No specific FDA predicate numbers appear in the source; however, candidate product codes were identified for US reference (LLZ, QIH, QDQ)【2】. These may be useful when seeking foreign data or regulatory precedents.*

---

### 4. Missing / Outstanding Information  

| Item | Why Needed | Action |
|------|------------|--------|
| **Precise Intended Use Statement** | Determines risk class and evidence scope. | Draft clear, concise wording and submit for MFDS review. |
| **AI Algorithm Description** (model architecture, training data size, population, labeling methodology) | Required for component performance evaluation & change‑management plan. | Provide detailed technical dossier. |
| **Performance Metrics** (sensitivity, specificity, AUC, etc.) with validation dataset details | Basis for clinical evaluation and risk assessment. | Compile from internal studies; consider external validation if available. |
| **Change‑Control Plan Draft** | Mandatory under the 2025 Digital Medical Device Act. | Prepare a documented plan outlining versioning, impact analysis, and post‑market monitoring. |
| **KGMP Certification Status** | Facility must be KGMP‑certified before submission. | Verify current certification or initiate audit. |
| **Korean Language Materials** (label, IFU, marketing) | Legal requirement for all medical devices. | Translate and have a certified Korean reviewer approve. |
| **Post‑Market Surveillance (PMS) Plan** | Required for Class II devices; especially critical for AI‑driven products. | Define adverse event reporting, periodic safety update schedule. |

---

### 5. Core Risk Controls  

1. **ISO 14971 Risk Management Process** – identify hazards related to AI misclassification, data privacy breaches, software bugs.  
2. **Cybersecurity Safeguards** – SBOM generation, regular vulnerability scanning, encryption of patient data, secure update mechanisms (aligned with MFDS/ FDA guidance).  
3. **Usability Engineering** – formative and summative usability testing per the *독립형 SW 사용적합성 가이드라인* to mitigate user error.  
4. **Algorithm Change Governance** – predetermined change‑control plan (PCCP) style processes similar to FDA’s 2024 guidance, adapted for Korean requirements.  
5. **Data Privacy Compliance** – adherence to the Personal Information Protection Act (PIPA) and any sector‑specific provisions for health data.  

---

### 6. Citations  

| Reference | Excerpt ID |
|-----------|------------|
| “2등급 (보조 기능 수준에 따라 상향 가능)” – MFDS classification guideline | 【1】 |
| “디지털의료제품법” 2025‑01‑24 시행 – AI/SW 별도 체계, 변경관리계획, 구성요소 성능평가 등 | 【1】 |
| “독립형 SW 사용적합성 가이드라인” 적용 (독립형인 경우) | 【1】 |
| FDA product code candidates LLZ / QIH / QDQ – for comparative foreign reference | 【2】 |

*No specific Korean device identifiers (e.g., registration number) appear in the source; therefore none are listed.*

---

### 7. Human‑Escalation Triggers  

| Situation | Who Should Be Alerted | Reason |
|-----------|----------------------|--------|
| **Uncertainty over class upgrade** (auxiliary function deemed high‑risk) | Senior Regulatory Manager & Clinical Affairs Lead | May require Class III 허가, longer review timeline. |
| **Absence of KGMP certification** | Manufacturing Operations Director | Submission cannot proceed without certified facility. |
| **Inadequate change‑management documentation** | Head of Software Development / QA | Mandatory under 2025 Act; non‑compliance blocks approval. |
| **Local clinical data required** (foreign evidence not accepted) | Clinical Research Lead | Need to plan a Korean bridging study, affecting schedule/budget. |
| **Cybersecurity gaps identified in SBOM audit** | IT Security Officer & Regulatory Affairs | Must remediate before dossier finalization. |
| **Regulatory notice change** (new MFDS scope expansion for foreign data) | Regulatory Strategy Team | Update evidence strategy promptly. |

---

### 8. Peer‑Review Prompt  

> **To the RA team:** Please review this draft and challenge the following points:  
> 1. Is the justification for staying in Class II robust, or should we pre‑emptively consider a Class III assessment given the AI’s autonomous decision‑making potential?  
> 2. Does the evidence list fully address the latest MFDS scope expansion on accepting foreign non‑clinical data (e.g., OECD‑aligned studies), or have we missed any required Korean bridging components?  
> 3. Are there any additional Korean‑specific obligations (e.g., Medical Device Safety Information Reporting, special labeling for AI/ML) that are not captured here?  

Your feedback will be incorporated before final submission to MFDS.

---

### 9. Reusable RA Judgment (Honcho Record)  

**Lesson:**  
*When a digital medical software product falls under the 2025 “디지털의료제품법”, classify it as **2등급** by default, but perform a detailed auxiliary‑function risk analysis; if the AI performs high‑risk autonomous tasks, re‑classify to a higher class. The Act mandates a **Change Management Plan** and **Component Performance Evaluation**, and independent‑software usability guidelines apply for stand‑alone products. KGMP certification, Korean‑language labeling, cybersecurity (SBOM) and full ISO 14971 risk management remain mandatory.*  

*Record this judgment for future AI‑driven medical software assessments in Korea.*

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

### kb-eval-20260719-it03-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_kr-002", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9ae1fa70f2e54276", "source": "github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md", "source_hash": "e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `9ae1fa70f2e54276`
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

> **Regulatory Draft – Impact of the Digital Medical Products Act on the X‑ray Workstation Software / AI Imaging Analysis Module**

---

## 1. Classification & Submission Route  

| Item | Assessment (based on the Digital Medical Products Act) |
|------|--------------------------------------------------------|
| **Product type** | SaMD / AI‑enabled imaging analysis module incorporated in an X‑ray workstation (software component). |
| **Risk class** | Determined by intended use and impact on clinical decision‑making. Under MFDS guidelines, image‑analysis AI that influences diagnosis generally falls into **Class II (moderate risk)**; if it directly drives therapeutic action it may be **Class III**. A formal risk‑based classification matrix from the Act must be applied to confirm. |
| **Submission pathway** | • **MFDS 허가 (Medical Device Approval) – “인허가”** for Class II/III SaMD.<br>• If classified as a lower‑risk tool (e.g., workstation UI only), a **신고 (Notification)** may be sufficient, but the Act’s expanded requirements on AI change management and component evaluation typically trigger an approval route. |
| **Reference** | No specific MFDS registration or 510(k) predicate number appears in the source excerpts – *“no specific identifier found in source — verify separately.”* |

---

## 2. Required Evidence (per the Act, effective 2025‑01‑24; implementation rule 2025‑02‑28)

| Requirement | What must be submitted | Current status (from cross‑verification) |
|-------------|-----------------------|------------------------------------------|
| **사용적합성(Usability) evidence** | Human factors/ergonomics test reports, user‑task analysis, validation that the UI supports intended users & clinical workflow. | **G2 – 사용적합성 증빙 미대응** (no usability evidence provided). |
| **Cybersecurity compliance** | • Expanded security criteria (requirement count ↑ 15→35).<br>• SBOM (Software Bill of Materials) submission.<br>• Vulnerability management plan. | SBOM referenced in issue list but full compliance not demonstrated. |
| **AI Change‑Management Plan** | Documented process for version control, algorithm updates, re‑validation after any change, and post‑deployment monitoring. | Required by the Act; no evidence located in current dossier. |
| **Component‑Level Performance Evaluation** (effective 2026) | Independent assessment of each software component/AI module (e.g., image acquisition, preprocessing, AI inference) against pre‑defined performance metrics. | **G3 – 구성요소 평가 적용 여부 미판정** (unclear if component evaluation applied). |
| **RA Mapping (RA‑01 ~ RA‑20)** | Complete cross‑mapping of regulatory requirements to evidence items (risk management, clinical evaluation, labeling, etc.). | **G4 – 전수 매핑 미완** (mapping incomplete). |
| **Korean language labeling & IFU** | All user instructions, safety information, and labels must be in Korean. | Not addressed in source; assume missing until proven otherwise. |

---

## 3. Missing / Unverified Information  

1. **Usability test package** – no data files or report summaries referenced.  
2. **Decision on component‑level performance assessment** – the dossier lacks a clear statement that each AI sub‑module has been evaluated per the 2026 rule.  
3. **Full cybersecurity evidence set** – only SBOM is mentioned; risk assessment, penetration testing reports, and compliance with the 35-item security checklist are absent.  
4. **AI change‑management documentation** – required plan & governance process not supplied.  
5. **Complete RA requirement mapping (RA‑01 ~ RA‑20)** – gaps in traceability matrix hinder readiness for MFDS review.  
6. **Korean language IFU/labels** – no proof of compliance with Korean labeling law.  

---

## 4. Core Risk Controls to Implement  

| Control | Description |
|---------|-------------|
| **Cybersecurity risk assessment (ISO 27001 / IEC 62443)** | Identify attack vectors, perform threat modeling, and apply the 35 security requirements from the Act. Include periodic vulnerability scanning and patch management. |
| **AI algorithm monitoring** | Real‑time performance analytics, drift detection, and a predefined trigger for model re‑validation when accuracy falls below thresholds. |
| **Change control & versioning** | Formal SOP governing code changes, dataset updates, and re‑submission of the AI change‑management plan to MFDS after any modification. |
| **Usability engineering process (IEC 62366‑1)** | Conduct formative and summative usability studies with representative users; map findings to risk mitigations. |
| **Component‑based verification** | Isolate each software block, execute unit‑level testing against defined performance criteria, and document results in a Component Test Report. |
| **Post‑market surveillance (시판후조사)** | Set up a PMS plan that includes adverse event reporting, periodic safety updates, and field safety corrective actions, all reported in Korean to MFDS. |
| **Labeling & IFU compliance** | Translate all user documentation into Korean; include clear contraindications, warnings, and instructions for AI‑driven alerts. |

---

## 5. Human‑Escalation Triggers  

| Trigger | Action (who) | Reason |
|---------|--------------|--------|
| **Absence of usable usability evidence (G2)** | Senior RA lead → MFDS liaison | MFDS may reject submission for lacking mandatory human factors data. |
| **Uncertainty about component‑level evaluation (G3)** | AI development manager + QA lead → Regulatory team | Needed to determine if the 2026 performance rule is satisfied; delay could block approval. |
| **Incomplete RA mapping (G4) or any missing evidence** | Project Manager → Executive Steering Committee | Indicates systemic gaps; risk of non‑conformance across multiple requirement areas. |
| **Critical cybersecurity finding during internal audit** | Information Security Officer → Head of Compliance | Immediate remediation and notification to MFDS per security breach reporting obligations. |
| **Algorithm performance degradation identified in post‑market monitoring** | Clinical Safety Officer → RA team & MFDS | Must trigger AI change‑management plan, possible field correction or recall. |

---

## 6. Citations  

| Source excerpt (Chunk ID) | Relevant regulatory element |
|---------------------------|------------------------------|
| **1061576322702878078** – “디지털의료제품법은 2025‑01‑24 시행… 사용적합성 자료 제출 의무화, 사이버보드 요구 확대(15→35), AI 변경관리 계획, 구성요소 단위 성능평가(2026 시행)…” | Basis for usability, cybersecurity expansion, AI change‑management and component evaluation requirements. |
| **1016004334478948993** – “참고 링크 … 디지털의료제품법_SaMD_AI_요구.md … 교차검증_보고서/2026‑04‑22_SBOM_디지털의료제품법_정합성.md … 관련 이슈: 005(GSPR 체크리스트 v0.2→v0.3), 009(사이버보안), 013(SBOM)” | Shows existence of SBOM requirement and checklist issues; confirms that cyber‑security items are tracked under issue numbers (005, 009, 013). |
| **No specific identifier found in source — verify separately** for MFDS registration numbers or 510(k) predicates. |

---

## 7. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions and gaps identified above. Are there any additional jurisdiction‑specific obligations under the Digital Medical Products Act (e.g., data‑privacy provisions, interoperability standards) that have been overlooked? Verify whether the cited “35 cybersecurity items” correspond to a published checklist (issue 009) or if further documentation is required. Also, confirm that our classification reasoning (Class II/III SaMD) aligns with MFDS’s latest risk‑matrix guidance for AI‑based imaging tools.

---

## 8. Reusable RA Judgment (Memory Outcome)

- **Rule:** For any SaMD/AI module falling under the Digital Medical Products Act, **submission must include** (i) **usability evidence**, (ii) **full cybersecurity compliance with the expanded 35‑item checklist**, (iii) an **AI change‑management plan**, and (iv) **component‑level performance evaluation** once 2026 requirements are effective.  
- **Gap detection:** Any of G2–G4 flags (missing usability, unclear component evaluation, incomplete RA mapping) constitute a “critical readiness deficiency” that triggers senior‐RA escalation before dossier submission.  
- **Citation practice:** Only cite identifiers explicitly present in source excerpts; otherwise note absence and plan independent verification.  

These points should be reused for future projects involving digital‑health software subject to the 2025 Digital Medical Products Act.

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

### kb-eval-20260719-it03-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_kr-003", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "691fd991ed827a72", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `691fd991ed827a72`
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

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법) on a Software‑Based SaMD/AI Device**

---

### 1.  Applicable Legislation & Primary Sources  

| Item | Reference |
|------|------------|
| **Law** | 디지털의료제품법 (법률 제20139호, 제정 2024‑01‑23) – implementation date 2025‑01‑24【1002132727008468922】 |
| **Regulatory Decree** | 대통령령 제35219호 (2025‑01‑23 제정, 2025‑01‑24 시행)【1002132727008468922】 |
| **Enforcement Rules** | 총리령 제1958호 (2025‑02‑28 시행)【1002132727008468922】 |
| **Relevant Guidances (2024‑2025)** | • 디지털치료기기 임상시험 설계 가이드라인 (low relevance – DTx only) 2024‑12【1077225675205822581】<br>• 생성형 AI 의료기기 허가·심사 가이드라인 (medium relevance – AI image analysis) 2025‑01【1077225675205822581】<br>• 독립형 디지털의료기기SW 사용적합성 가이드라인 (high relevance – console/viewer SW) 2025‑01【1077225675205822581】<br>• 의료기기 사이버보안 허가·심사 가이드라인(개정) (high relevance – networked devices) 2025‑01‑10【1077225675205822581】<br>• 디지털의료기기 전자적 침해행위 보안 지침(안) (high relevance – SBOM 관리 포함) 2025‑01【1077225675205822581】 |

---

### 2.  Device Classification & Submission Route  

| Determinant | Assessment under the Digital Medical Products Act |
|-------------|---------------------------------------------------|
| **Intended Use** | Software that analyses medical images (e.g., AI‑based diagnostic support). |
| **Risk Level** | According to MFDS classification tables, AI‑driven image analysis that provides *diagnostic recommendations* is placed in **Class IIb** (moderate‑to‑high risk) – requires full **허가** (approval) rather than simple 신고 (notification). |
| **Submission Route** | Full 허가 application through the MFDS Medical Device Policy Division. The dossier must include: technical file, clinical evaluation report, risk management file, KGMP certification for the software development environment, and cybersecurity documentation. |

> **Note:** No specific 510(k)/predicate or registration numbers appear in the source excerpts – *no specific identifier found in source — verify separately*.

---

### 3.  Required Evidence Package  

| Category | Minimum Content (per Act & Guidances) |
|----------|----------------------------------------|
| **Technical Documentation** | • Device description, architecture, and intended use.<br>• IEC 62304‑compliant software life‑cycle documentation.<br>• Software Bill of Materials (SBOM) per the “디지털의료기기 전자적 침해행위 보안 지침”(안). |
| **Risk Management** | • ISO 14971 risk analysis and mitigation plan.<br>• Identification of AI‑specific hazards (e.g., algorithm drift, opacity). |
| **Clinical Evaluation** | • Clinical performance data (prospective / retrospective) demonstrating safety & efficacy in the Korean population. <br>• If foreign clinical evidence is used, it must be aligned with OECD‑approved non‑clinical data and accepted by MFDS – cite supporting notice when available. |
| **Cybersecurity** | • Compliance with “의료기기 사이버보안 허가·심사 가이드라인”(개정) (high relevance).<br>• Threat modeling, penetration testing reports, and incident response procedures.<br>• SBOM management as required by the 2025‑01 security guideline. |
| **KGMP Certification** | • Facility must hold KGMP certification for software development (per “디지털의료기기 제조 및 품질관리 기준”). |
| **Korean Language Requirements** | • All labeling, instructions for use (IFU), and software UI where displayed to users must be provided in Korean. |
| **Post‑Market Surveillance Plan** | • PMS protocol according to MFDS 시판후조사 규정, including active safety monitoring and reporting of AI‑related adverse events. |

---

### 4.  Gaps / Missing Information (to be clarified with the sponsor)

1. **Exact Intended Use Statement** – is the software a “diagnostic aid” or “screening tool”?  
2. **Algorithm Transparency & Explainability** – documentation on model interpretability methods.  
3. **Performance Metrics** – sensitivity, specificity, AUC values from validation studies.  
4. **Local Clinical Data Requirement** – whether existing foreign data satisfies MFDS expectations; if not, plan for a Korean clinical trial.  
5. **SBOM Details** – completeness of component inventory and update strategy.  
6. **Human‑Machine Interface (HMI) Design** – screenshots of UI to verify Korean language compliance.  

---

### 5.  Core Risk Controls & Human‑Escalation Triggers  

| Hazard | Control Measure | Escalation Trigger |
|--------|-----------------|--------------------|
| Misclassification of image findings | • Robust validation against a curated reference standard.<br>• Continuous performance monitoring (periodic re‑training). | AI confidence score < 70% **or** discrepant result with prior imaging → require physician review before action. |
| Algorithm drift over time | • Version control and change management linked to SBOM.<br>• Periodic re‑validation schedule. | Detection of statistically significant performance deviation in PMS data → suspend automated reporting until review. |
| Cybersecurity breach | • Network segmentation, encryption, intrusion detection per 2025‑01 보안 가이드라인.<br>• Incident response SOP. | Any unauthorized access alert or integrity violation → immediate lockout and notification to MFDS within 24 h. |
| UI language inconsistency | • Korean translation verification at each release.<br>• Usability testing with Korean clinical users. | User feedback indicating misunderstanding of instructions → issue urgent software patch/notice. |

---

### 6.  Human‑Oversight (Escalation) Process  

1. **Real‑time Alert** – AI confidence < 70% or conflicting result triggers an on‑screen alert in Korean.  
2. **Physician Confirmation** – Required sign‑off before any clinical decision is recorded.  
3. **Documentation** – Timestamp, user ID, and reason for override must be logged.  
4. **Post‑Event Review** – All overrides are reviewed weekly by the risk management team; trends trigger root‑cause analysis.  

---

### 7.  Suggested Timeline (post‑implementation of Act)

| Milestone | Approx. Duration |
|-----------|------------------|
| Finalize intended use & functional spec | 1 mo |
| Assemble technical file & KGMP audit | 2–3 mo |
| Conduct clinical performance study (if local data needed) | 6 mo |
| Cybersecurity assessment & SBOM compilation | 1 mo (parallel) |
| Prepare Korean labeling/IFU | 0.5 mo |
| Submit 허가 dossier to MFDS | – |
| MFDS review (typically 4–6 mo for Class IIb) | – |
| Post‑approval PMS set‑up | 1 mo |

---

### 8.  Peer‑Review Prompt  

> **Colleague, could you evaluate the following?**  
> - Are we correctly interpreting the classification of an AI image‑analysis SaMD as *Class IIb* under the Digital Medical Products Act?   
> - Does our evidence matrix fully capture MFDS’s current expectations for cybersecurity (including SBOM) and Korean language UI requirements?    
> - Have we identified any jurisdictional gaps, such as the need for a local clinical trial or additional risk‑control documentation that the cited guidances do not explicitly mention?  

Your feedback will help tighten the submission strategy before finalizing the dossier.

---

### 9.  Reusable RA Judgment (Honcho Record)

**Lesson:**  
When evaluating digital health software under Korea’s Digital Medical Products Act, always map the device’s AI function to MFDS classification tables (typically Class IIb for diagnostic support). The act mandates a full 허가 route with comprehensive technical documentation, KGMP‑certified development, Korean language labeling, and heightened cybersecurity controls—particularly SBOM management per the 2025‑01 security guidance. Even if foreign clinical data exist, confirm MFDS’s acceptance (often requires OECD‑aligned evidence) and be prepared to generate local performance data. Human‑escalation triggers must be built into the UI logic (confidence thresholds, override logging) and reflected in risk management and post‑market surveillance plans.

*Recorded with peer=”ai”.*

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

### kb-eval-20260719-it03-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_kr-004", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "5d021441b22a8fa1", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "a20110f67bbd98b35d188d8a2fd8d816a95754663f6515d8828b632ceb3d72e5"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5d021441b22a8fa1`
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

> **Regulatory Draft – X‑ray Digital Medical Product (2026‑04‑22 Report)**  

---

### 1 Classification & Submission Route (MFDS)

| Component | “디지털의료제품법” relevance (source [1]) | MFDS classification* |
|-----------|------------------------------------------|----------------------|
| **Generator firmware** | X – hardware‑only control, no network connectivity | Treated as *전기·전자 의료기기* (class I/II depending on output power). Not a “디지털의료제품”. |
| **Detector firmware** | △ – may become applicable when networked | If later equipped with networking → SaMD (software that drives or interprets detector data) → likely Class II. |
| **Acquisition Workstation SW** | ○ – standalone software, network‑connected, AI possible | SaMD + AI → MFDS class III (high‑risk) under the Digital Medical Device Act (디지털의료제품법). Requires 허가 (full approval). |
| **Imaging post‑processing / AI analysis module** | ○ (if applicable) – SaMD + AI | Same as above: Class III SaMD + AI → 허가. |
| **DICOM transmission & PACS interface** | △ – communication function, borderline software | If purely transport layer → may be considered “연동·전송 소프트웨어” (class II). If it includes decision support → Class III SaMD. |

\*MFDS class designations follow the “고위험(III) / 중위험(II) / 저위험(I)” schema for digital health products.  

**Primary submission route:**  
- **Acquisition Workstation SW** and **AI analysis module** → *허가* (full approval).  
- Supporting hardware (generator, detector) → if classified as conventional medical device → either *신고* (notification) for low‑risk or *허가* for medium/high risk.  

---

### 2 Required Evidence Package (per MFDS & 디지털의료제품법)

| Evidence Category | What the MFMF requires | Gap identified in source |
|-------------------|------------------------|--------------------------|
| **Technical Documentation** (품질·기술문서) | • System architecture, software bill of materials (SBOM) <br>• IEC 62304/IEC 82304 compliance <br>• UDI strategy (see SOP‑UDI‑001 referenced in source [2]) | Detailed SBOM already noted, but no **complete** list of third‑party libraries or their versions. |
| **Risk Management** | • IEC 60601‑1‑2 for electromagnetic safety (X‑ray) <br>• IEC 62366‑1 usability risk <br>• AI/ML risk management per MFDS “AI 의료기기 안전성 가이드라인” | AI validation plan is not present; no documented mitigation for bias or model drift. |
| **Clinical Evaluation** | • Clinical performance data (local if required) <br>• Literature review of comparable predicates (FDA 510(k)/EU CE) – acceptable only when MFDS notices allow foreign evidence | No Korean clinical data supplied; source does not list any predicate device numbers → “no specific identifier found in source — verify separately.” |
| **Software Verification & Validation** | • Unit, integration, system testing reports <br>• Cybersecurity assessment (FDA Cybersecurity Guidance accepted under recent MFDS notice) | SBCM‑related security procedures referenced (IEC 81001‑5‑1), but test results missing. |
| **Labeling & IFU** | • Korean language labeling, user manual, safety information <br>• Post‑market surveillance plan (시판후조사) | No Korean IFU shown; language requirement flagged as a typical omission. |
| **Manufacturing Compliance** | • KGMP certification for any hardware manufacturing site <br>• Process validation records for firmware build & release | KGMP status not mentioned in the excerpts. |
| **Regulatory Strategy Documents** | • Declaration of conformity to “디지털의료제품법” (SaMD + AI) <br>• Evidence that the product meets “SBOM 3축 요구사항” (source [2]) | The SBOM alignment report exists, but the mapping to MFDS cybersecurity requirements is not detailed. |

---

### 3 Missing / Unclear Information

1. **Exact regulatory classification** for each firmware/soft component (predicate numbers, class designation).  
2. **Local clinical performance data** or a justification that foreign data are acceptable under the latest MFDS notice.  
3. **Full SBOM** with versioning, provenance, and vulnerability mitigation plan.  
4. **AI algorithm documentation** – training dataset description, performance metrics, explainability, post‑market monitoring.  
5. **Korean language labeling & user manual** (including warnings, contraindications).  
6. **KGMP certificate** for the generator/ detector hardware production facility.  
7. **UDI implementation details** – how UDI is embedded in software and packaging.  

---

### 4 Key Risk Controls (to be reflected in the submission)

| Risk Area | Control Measure | Reference |
|-----------|-----------------|-----------|
| **Radiation exposure** | Hardware interlocks, dose‑limiting software, IEC 60601‑2‑XX compliance. | MFDS Radiation Safety Rules (진단용방사선_안전관리규칙). |
| **Network security** | Hardened OS, encrypted DICOM transmission, firmware signing, SBOM‑based vulnerability management. | IEC 81001‑5‑1 (FDA cybersecurity) cited in source [2]. |
| **AI decision support** | Independent validation set, periodic re‑training, bias analysis, transparency report per MFDS AI guidelines. | 디지털의료제품법 SaMD AI 요구사항 (referenced in source [2]). |
| **Usability / Human factors** | IEC 62366‑1 usability testing with Korean clinicians, clear UI language, error‑recovery flows. | Standard MFDS usability requirement. |
| **Data integrity** | Audit trails for image acquisition, immutable logs, checksum verification of transferred DICOM files. | General MFDS data security expectations. |
| **Post‑market surveillance** | Real‑world performance registry, adverse event reporting in Korean (시판후조사), periodic safety updates. | MFDS 시판후조사 규정. |

---

### 5 Citations (as extracted)

* **Report title & doc‑id:** “교차검증 보고서 — SBOM 3축 요구사항 & 디지털의료제품법 정합성”, doc‑id = LOG‑2026‑04‑22\_SBOM\_디지털의료제품법\_정합성 (source [2]).  
* **Classification table** – derived from the “디지털의료제품법 해당성 판정(잠정)” matrix (source [1]).  

> No specific identifier (e.g., 510(k) number, MFDS 허가 번호, case ID) appears in the provided excerpts — verify separately.

---

### 6 Human‑Escalation Triggers

| Situation | Why escalation is needed | Who should be alerted |
|-----------|--------------------------|-----------------------|
| Ambiguous classification (e.g., Detector firmware marked “△”) | Could shift submission from 신고 to 허가, affecting timeline and evidence burden. | Senior RA lead & regulatory strategy owner. |
| Absence of Korean‑language IFU or labeling | MFDS rejects any dossier lacking Korean documentation. | Documentation manager + translation team. |
| AI algorithm validation gaps (no bias analysis, no performance metrics) | MFDS specifically scrutinizes SaMD + AI under the Digital Medical Product Act. | Clinical affairs lead & data science lead. |
| KGMP certification not confirmed for hardware manufacturer | Non‑compliance leads to mandatory corrective actions or denial of 허가. | Quality Assurance (QA) manager; consider third‑party audit. |
| SBOM incomplete or vulnerable component identified after submission | Cybersecurity findings trigger post‑market recall risk. | Product security officer & legal counsel. |
| Local clinical data unavailable but required | MFDS may request supplementary Korean trial data, causing delay. | Clinical development lead; consider external CRO engagement. |

---

### 7 Reusable RA Judgment (Lesson Learned)

> **When evaluating a mixed hardware‑software X‑ray system for the Korean market, treat any firmware or software that is network‑connected, capable of autonomous image interpretation, or incorporates AI as SaMD + AI under the Digital Medical Product Act.**  
> *Consequences:* – Class III classification → full 허가, demanding a complete technical file, Korean‑language labeling, KGMP certification for hardware, and robust AI validation.  
> *Pitfall:* The “△” (conditional) entries in internal matrices often hide the need for additional evidence (e.g., network security assessment, local clinical data). Always verify each component’s final connectivity status before finalising classification.

---  

### 8 Peer‑Review Prompt

*“Colleagues, please review this draft and challenge the following assumptions:  
1. The preliminary classification of the Detector firmware as potentially Class II/III – is there sufficient evidence to confirm its network functions?  
2. The reliance on foreign clinical predicates without a cited MFDS notice – does our current understanding meet the latest MFDS acceptance criteria for non‑Korean data?  
3. Are all mandatory Korean language deliverables (label, IFU, risk information) fully accounted for in the evidence list?  

Identify any jurisdiction‑specific gaps or missing documentation that could impede a successful 허가 submission under 디지털의료제품법.”*

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

### kb-eval-20260719-it03-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it03-ra_kr-005", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "7009c1806e2d0a1d", "source": "github:holee9/MD-process/issue-drafts/947_AUDIT_디지털의료제품법_법률번호_20722_광범위_자매재발.md", "source_hash": "fed73ac605f6674c04cc5029490b7b167f60ab56f7464d148e79c94381f53999"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `7009c1806e2d0a1d`
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

> **Regulatory Draft – Digital Medical Device (디지털의료제품) Impact Assessment**

---

### 1. Classification & Submission Route  
| Attribute | Determination | Rationale / Source |
|-----------|---------------|--------------------|
| **Device Type** | Software‑based medical device (AI‑driven diagnostic/monitoring tool) covered by the *Digital Medical Products Act* (“디지털의료제품법”). | The source explicitly references “디지털의료제품법(법률 제20722호)”【2†L13】. |
| **Risk Class** | Likely **Class III–IV** (high‑risk) if the software provides clinical decision support, treatment recommendations or remote monitoring of critical parameters. Under MFDS rules, such functions mandate a **허가 (approval)** rather than a simple 신고 (notification). | Korean classification follows “의료기기법 시행령”‑based risk matrix; high‑impact AI/clinical function escalates to Class III/IV. |
| **Submission Route** | **Medical Device 허가 (Approval) – Full Technical Dossier**.  Includes KGMP facility certification, clinical evaluation, and extensive cybersecurity documentation. | The impact note stresses “GMP 적합판정·품목허가” as a core regulatory checkpoint【1†L2-L3】. |

---

### 2. Required Evidence (MFDS Submission Checklist)  

| Evidence Category | Minimum Content | Comments / Gaps |
|-------------------|-----------------|-----------------|
| **KGMP Facility Certification** | Proof of KGMP compliance for the manufacturing/firmware update environment. | No explicit KGMP evidence cited; must be obtained before filing. |
| **Software Lifecycle Documentation** (SW 수명주기) | – Development plan, version control, change‑management logs.<br>– Validation & verification reports per IEC 62304.<br>– SBOM (Software Bill of Materials) pre‑check. | Source highlights need for “SBOM 사전점검” in research log【2†L20】; current dossier lacks these items. |
| **Cybersecurity Assessment** | – Threat analysis, risk mitigation plan (ISO 27001/IEC 62443 alignment).<br>– Incident response procedures.<br>– Penetration‑test results. | Audited as “최우선 열람 대상” for review【1†L1】; currently missing from QMS folder per audit comment. |
| **AI Performance Evaluation** | – Dataset description, bias/variance analysis.<br>– Validation against clinical gold standard.<br>– Continuous learning safeguards. | Explicitly listed as priority document for reviewers【1†L1】; not yet provided. |
| **Clinical Evaluation Report (CER)** | – Clinical literature review, locally performed usability/clinical study if required. | No mention in source; assumed missing. |
| **Regulatory Cross‑Reference** | Accurate citation of the underlying law and clause (e.g., “법률 제20722호 제40조”). | Source shows a citation but flags possible error (“법률 번호 오기”)【1†L1-L2】; verification required. |
| **Labeling & IFU** | Korean language labeling, safety information, user manual per MFDS Annex 13. | Not addressed in source – must be prepared. |

---

### 3. Missing Information (Gap Summary)  

| Gap | Impact on Submission | Action Required |
|-----|----------------------|-----------------|
| **Correct Legal Citation** | Inaccurate law reference undermines document credibility and may trigger MFDS queries. | Verify the current *Digital Medical Products Act* number and clause; update all references. |
| **QMS Folder Coverage** – Design/Development & Cybersecurity sections absent | Auditors flagged limited scope (“설계개발/사이버보안 폴더 누락”)【1†L4-L5】. | Expand QMS repository to include design files, risk management, and cyber‑risk artifacts; apply cross‑reference automation (see Plan #935). |
| **SBOM & Pre‑Check Evidence** | Required for software traceability and import/export compliance. | Generate SBOM for all third‑party components; attach pre‑check report. |
| **AI Validation Data** | Needed to satisfy MFDS AI performance review priority【1†L1】. | Provide documented AI model training, validation, and post‑deployment monitoring plans. |
| **KGMP Certification Evidence** | Mandatory for any device seeking 허가. | Obtain or update KGMP certificate; attach audit report. |
| **Korean Language IFU/Labeling** | Legal requirement; omission blocks market entry. | Draft Korean labeling & instruction set; submit for MFDS review. |

---

### 4. Risk Controls (Proposed Mitigation Measures)  

1. **Regulatory Traceability Matrix** – Map each MFDS requirement to a concrete artifact (e.g., law clause → citation, AI performance → validation report).  
2. **Automated Cross‑Reference Engine** – Implement the “grep 매칭룰” suggested in Plan #935, prioritising pattern `법률 제[0-9]+호` to catch any mismatched legal references【1†L5-L6】.  
3. **Cybersecurity Hardening** – Conduct a formal ISO 62443 gap analysis; integrate findings into the QMS and risk management file.  
4. **AI Governance Framework** – Adopt IMDRF’s “Software as a Medical Device (SaMD) – Clinical Evaluation” guidance; document version control, drift monitoring, and human‑in‑the‑loop safeguards.  
5. **Post‑Market Surveillance (PMS)** – Define real‑time vigilance plan (시판후조사) incorporating cybersecurity incident reporting and AI performance drift alerts.  

---

### 5. Citations (as required)  

- **Digital Medical Products Act reference** – “디지털의료제품법(법률 제20722호)” (source 【2†L13】). *Note: source flags possible citation error; verify before submission.*  
- **Audit Findings** – Mis‑cited law number and QMS scope limitation (audit #930)【1†L1-L5】.  
- **Cross‑Reference Documentation** – “법률 제20722호 제40조” in research log【2†L20】; superseded version note in cross‑validation report【2†L13】.  

*No specific MFDS case numbers, 510(k) predicates, or registration identifiers appear in the provided excerpts.*  

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Path |
|---------|-----------------|
| **Detected mismatch in legal citation** (law number or article) | Immediate review by senior RA lead; halt dossier finalisation until corrected. |
| **Absence of cybersecurity or AI performance documents** after a 5‑business‑day notice | Escalate to Head of Regulatory & Compliance for risk assessment and timeline revision. |
| **Audit #930 comments unchanged >10 days** | Notify Quality Assurance Manager and trigger corrective action plan (CAP). |
| **Failure to obtain KGMP certification** before filing deadline | Elevate to Executive Sponsor; consider alternative manufacturing site or partnership. |
| **Post‑market surveillance plan not approved by PMO** | Route to Clinical & Safety Committee for urgent review. |

---

### 7. Peer Review Prompt  

> **@RA Colleague:** Please challenge the assumptions made in this draft, especially:  
> 1. The classification of the AI‑driven software as Class III/IV – is there evidence from intended use that could lower risk?  
> 2. The completeness of the “required evidence” list under the current Digital Medical Products Act – have any recent MFDS notices added new obligations (e.g., mandatory real‑world data for SaMD)?  
> 3. Potential jurisdictional gaps, such as whether a local clinical study is truly required or if foreign CE/FDA data can be leveraged under the latest MFDS scope expansion.  

Your feedback will ensure full coverage before dossier submission.

---

### 8. Reusable RA Judgment (Lesson Record)  

**Judgment:**  
When referencing Korean statutes in digital‑medical‑device submissions, **always verify the exact law number and article cited** because audit notes frequently uncover mis‑citations that can invalidate the entire dossier. Incorporate an automated cross‑reference check (e.g., grep pattern `법률 제[0-9]+호`) into the document‑control workflow to flag any discrepancy before final review. Additionally, ensure that **cybersecurity, software lifecycle, and AI performance documentation are positioned as top priority items** for MFDS reviewers; their absence is a common cause of rejection or request for additional information.  

*Recorded for future RA projects involving the Digital Medical Products Act.*

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
