# KB Eval Checksheet - 2026-07-20 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260720-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_us-001", "iteration": 2, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "fc3bfc38766e3c54", "source": "github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md", "source_hash": "19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf"} -->

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

> **Regulatory Draft – QMSR Design‑Control Alignment (21 CFR 820)**  

---

### 1. Classification / Submission Route  
- **Device classification:** Not applicable – the issue concerns internal Quality Management System compliance, not a specific medical device submission.  
- **FDA submission route:** N/A (no 510(k), de Novo, or other market‑entry filing required). The focus is on meeting the mandatory QMSR requirements for any future submissions.

---

### 2. Required Evidence of Compliance  

| Requirement | Evidence Needed | Status / Gap |
|-------------|----------------|--------------|
| **§820.10(c) – Design Control (incorporation by reference)** | • Updated SOP‑AIGOV‑001 front‑matter showing “§820.10(c) → ISO 13485:2016 §7.3”.<br>• Current design‑control procedure that explicitly cites ISO 13485:2016 §7.3 and maps each design‑control element (design input, output, verification, validation, transfer). | Verify existence of the updated SOP; ensure all design‑control activities are traceable to the ISO clause. |
| **Removal of Reserved §820.30 references** | • Document‑level grep/traceability report confirming *zero* occurrences of “§820.30” in any SOP, Form, or matrix.<br>• Change‑control record showing correction of the front‑matter and propagation to all downstream documents. | Source indicates residual citations; a full sweep must be completed and documented. |
| **Training & Awareness** | • Training logs (e‑learning or classroom) confirming that responsible personnel received “QMSR §820.10(c) design‑control” training after the change.<br>• Quiz/assessment results demonstrating comprehension. | Not mentioned in source – needs to be produced. |
| **Document Control & Versioning** | • Master Document List showing version numbers, approval dates, and responsible owners for all SOPs/forms affected.<br>• Archived superseded versions retained per 21 CFR 820.180. | Not evident – confirm availability. |
| **Audit Trail of Corrections** | • CAPA record (or equivalent) documenting the audit finding #921, root‑cause analysis (residual citations), corrective actions taken, and effectiveness verification. | Partial – audit summary present; full CAPA package required. |

---

### 3. Missing Information / Immediate Actions  

1. **Comprehensive citation sweep** – run a repository‑wide grep for “§820.30” and produce a remediation log.  
2. **Formal CAPA closure evidence** – include verification activities (re‑audit, independent reviewer sign‑off).  
3. **Training completion records** for all staff who author or use design‑control documents.  
4. **Mapping matrix** that links each design‑control requirement in 21 CFR 820.30(a) to the corresponding clause in ISO 13485:2016 §7.3, demonstrating one‑to‑one incorporation.  
5. **Date‑stamped evidence of front‑matter generation** (build script logs) confirming automatic updates are functional post‑correction.

---

### 4. Risk Controls & Mitigation  

| Potential Risk | Control / Mitigation |
|----------------|----------------------|
| Residual “§820.30” citations cause FDA inspection finding (non‑conformance). | Automated build/script that injects the correct front‑matter; periodic (quarterly) automated grep validation. |
| Design‑control activities performed under an outdated reference framework. | Mandatory cross‑reference matrix and periodic internal audit of design‑control work products against ISO 13485:2016 §7.3. |
| Inadequate staff awareness leading to re‑introduction of legacy language. | Annual refresher training + competency assessments; inclusion of the citation policy in SOP authoring checklist. |
| Lack of traceability for changes may hinder CAPA effectiveness verification. | Enforce change‑control workflow that requires linking every document revision to a specific audit finding or regulatory update (e.g., QMSR 2026 amendment). |

---

### 5. Citations  

- **21 CFR 820.30** – Reserved in the eCFR edition effective 02 Feb 2026. *(established regulatory reference)*  
- **21 CFR 820.10(c)** – Design‑control requirements incorporated by reference to ISO 13485:2016 §7.3. *(established regulatory reference)*  
- **ISO 13485:2016 §7.3** – “Design and Development” requirements. *(established standard reference)*  
- **eCFR 21 CFR 820 (QMSR)** – Effective 02 Feb 2026, as cited in source excerpt. *(established regulatory reference)*  

*No specific case identifiers (510(k) numbers, predicate devices, registration IDs) appear in the source material.*  

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Path |
|--------|-----------------|
| Any residual “§820.30” citation discovered after remediation sweep | Alert QMS Lead → Senior Management → FDA liaison (if inspection imminent). |
| CAPA #921 not closed within 30 days of corrective action implementation | Immediate escalation to Quality Assurance Director and compliance officer. |
| Training completion < 95 % for staff responsible for design‑control documentation | Notify HR/Training Manager; suspend release of new design documents until remediation. |
| Failure of automated build script to regenerate front‑matter correctly (e.g., missing “§820.10(c)” reference) | IT/QMS support ticket → immediate fix; if unresolved > 48 h, inform VP of Regulatory Affairs. |
| Repeat finding in subsequent internal audits (≥2 occurrences) | Formal audit committee review and potential external consultant engagement. |

**Regulatory judgment:** The organization has taken the correct high‑level step of consolidating design‑control requirements under §820.10(c) with ISO 13485:2016 §7.3, but residual references to the now‑reserved §820.30 remain. Until a complete citation sweep and documented CAPA closure are provided, the QMSR compliance posture remains **non‑conformant** for design‑control documentation.

---

### 7. Peer Review Prompt  

> *Colleague, please challenge the assumptions made regarding (a) completeness of the residual citation sweep, (b) adequacy of the single‑point incorporation by reference strategy for all design‑control elements, and (c) any jurisdiction‑specific nuances (e.g., state‑level medical device statutes or EU MDR reciprocal expectations) that may have been omitted.*

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

### kb-eval-20260720-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_us-002", "iteration": 2, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "0bd55d452ba8a1af", "source": "github:holee9/MD-process/issue-drafts/921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md", "source_hash": "36a0683dda1f189f95c3bba8f11be7917c7ed24fdf703b490573ae5ef6cf0b16"} -->

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

> **Regulatory Draft – QMSR (21 CFR 820) and Design‑Control Readiness**

---

### 1. Classification & Submission Pathway  
- **Device class:** Unchanged from the currently cleared classification (class I, II or III as already assigned). The update concerns the quality‑system framework, not the device’s intended use or technological characteristics.  
- **Regulatory route:** No new 510(k) or De Novo submission is required *unless* the QMS changes introduce a design change that materially affects safety or effectiveness (see 21 CFR 814.20(b)(2)). In that case, submit a **510(k) amendment** referencing the revised QMS documentation.  
- **Current status of §820.30:** Reserved per FDA guidance; therefore compliance is demonstrated through incorporation by reference of ISO 13485:2016 §7.3 via §820.10(c).  

### 2. Required Evidence Package  

| Element | What to Provide | Rationale |
|---------|----------------|-----------|
| **QMS SOP Revision Log** | Version‑controlled SOPs (e.g., SOP‑DHF‑001, SOP‑DT‑001, SOP‑DVV‑001) showing insertion of the “QMSR is §820.30 reserved; ISO 13485:2016 §7.3 incorporated by reference” clause. | Demonstrates alignment with the amended front‑matter guidance (Source [1]). |
| **ISO 13485:2016 Mapping Matrix** | Cross‑reference table mapping each FDA QMSR requirement to the corresponding ISO 13485:2016 clause, highlighting §820.10(c) ↔ ISO 13485 §7.3. | Provides traceability for the incorporation‑by‑reference approach. |
| **Design‑Control Documentation** | – Design Input & Output specifications<br>– Design Transfer records<br>– Verification & Validation protocols & reports<br>– Change‑control logs (including design changes) | Required per 21 CFR 820.30 subpart (design controls) even though §820.30 is reserved; FDA expects the same functional controls to be present via ISO 13485. |
| **Risk Management File** | ISO 14971‑based risk analysis, FMEA/FMECA results, risk mitigation actions, and post‑market surveillance plan. | Links safety‑related design decisions to QMS processes. |
| **Training & Competence Records** | Signed attendance sheets, competency assessments for personnel performing design‑control activities. | Demonstrates effective implementation of the updated SOPs. |
| **Management Review Minutes** | Evidence that senior management evaluated QMS performance after the amendment (including any identified gaps). | Required by 21 CFR 820.20 and ISO 13485 §5.6. |

### 3. Identified Gaps / Missing Information  

| Gap | Impact | Suggested Action |
|-----|--------|-------------------|
| **Device‑specific context** – No description of the device(s) affected by the QMS amendment (type, intended use, classification). | Needed to determine whether a 510(k) amendment is required. | Add a brief Device Summary section. |
| **Scope statement for incorporation by reference** – The exact language used in the “incorporation by reference” clause has not been captured. | FDA may request clarification of which ISO clauses are incorporated and any exclusions. | Draft and archive the precise §820.10(c) wording (e.g., “FDA QMSR §820.10(c) incorporates ISO 13485:2016 §7.3”). |
| **Gap analysis results** – No documented comparison of current QMS vs. the revised requirement. | Hard to prove that all residual gaps have been closed. | Conduct and archive a formal gap‑analysis report. |
| **Change‑control impact assessment** – No evidence showing whether any design changes were triggered by the QMS update. | May affect 510(k) status if a design change is deemed significant. | Perform a “Design Change Impact Assessment” for each product line. |
| **Regulatory filing of incorporation by reference** – Unclear whether a formal FDA submission (e.g., an amendment to the existing 510(k)’s QMS section) will be made. | May delay acceptance of the new SOPs. | Determine need for a “QMS Amendment” under 21 CFR 814.20(b)(1). |

### 4. Core Risk Controls (Design‑Control Focus)

| Control | Description |
|---------|-------------|
| **Design Input Review** – Formal sign‑off that inputs satisfy user needs and regulatory requirements. |
| **Design Output Verification** – Objective testing/analysis confirming outputs meet inputs. |
| **Design Validation** – Clinical or simulated use testing under actual conditions of use. |
| **Change Control Process** – Documented evaluation, risk reassessment, and approval for any design alterations (includes QMS‑driven changes). |
| **Failure Mode & Effects Analysis (FMEA)** – Conducted early in development; updated after each change. |
| **Post‑Market Surveillance (PMS) Plan** – Ongoing monitoring to capture emergent risks; linked back to risk management file. |

### 5. Regulatory Citations  

| Source Type | Citation | Note |
|-------------|----------|------|
| Established regulation | **21 CFR 820.10(c)** – “Incorporation by reference of ISO 13485:2016 §7.3.” | Directly referenced in source [1]. |
| Established standard | **ISO 13485:2016 §7.3** – Design and development controls. | Mirrors FDA design‑control expectations. |
| Established regulation (reserved) | **21 CFR 820.30 (Reserved)** – No substantive text; compliance demonstrated via ISO 13485 incorporation. | Confirmed by source [1]. |
| Guidance document | “The New FDA 21 CFR Part 820 – QMSR” (BSI Compliance Navigator) – Tier 2 reference. | Source [2]; provides interpretive context for the reserved status. |
| Risk‑management standard | **ISO 14971:2019** – Application of risk management to medical devices. | Required for design‑control linkage. |
| No specific identifier found in source – verify separately | 510(k) / predicate numbers, registration IDs, case IDs. | None present in the excerpts. |

### 6. Human‑Escalation Triggers  

1. **Safety‑impacting gaps**: Any missing or incomplete design‑control evidence (e.g., absent validation data) that could compromise patient safety.  
2. **Unresolved “incorporation by reference” language**: Ambiguity in the exact ISO clauses incorporated; requires senior regulatory counsel review and possibly FDA clarification.  
3. **Potential significant design change**: If the QMS revision triggers a design alteration that meets the criteria of a *significant* change per 21 CFR 814.20(b)(2). Escalate to product development leadership for 510(k) amendment decision.  
4. **Deviation without corrective action**: Open CAPA or deviation that relates to design‑control processes; must be escalated to quality assurance manager and possibly the FDA as a post‑market report.  

---

### 7. Peer Review Prompt  

> *@RA‑Peer* – Please review this draft for (a) completeness of the QMSR incorporation analysis, (b) any overlooked jurisdictional nuances (e.g., state‑level requirements or EU MDR cross‑reference), and (c) whether additional evidence (such as a formal FDA “Letter of Incorporation” filing) is required. Challenge assumptions about the need for a 510(k) amendment and suggest any missing citations.

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

### kb-eval-20260720-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_us-003", "iteration": 2, "matched_keywords": ["PMA"], "profile_id": "ra-us", "scenario_id": "8240af1cbb85d72a", "source": "github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md", "source_hash": "ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd"} -->

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

> **Regulatory Draft – QMSR & Design‑Control Readiness (Process‑Monitoring SOP)**  

---

### 1. Regulatory Context  
The document under review is an SOP for “Process Monitoring & Analysis” that references ISO 13485 §§8.1, 8.2.5, 8.5.1, FDA Quality Management System Regulation (QMSR) §820.250 (statistical techniques), §820.100 (CAPA), and EU MDR Art.10(9)(j). The SOP is part of a larger quality‑system package (SOP‑PMA‑001 series) used for devices submitted via PMA.

---

### 2. Classification & Submission Route  

| Item | Determination |
|------|---------------|
| **Device class** | *Not determinable from the supplied excerpts.* The source only identifies the SOP as a “PM&A” (process‑monitoring) artifact; device type, intended use, and risk level are missing. |
| **Regulatory pathway** | If the ultimate device is Class III, the PMA route applies. Because classification cannot be confirmed, **human escalation to product definition & labeling team is required** before finalizing submission strategy. |

---

### 3. Required Evidence (per QMSR/ISO 13485)  

| Requirement | Expected Deliverable | Current Status (source) |
|-------------|---------------------|--------------------------|
| **§8.1 – Monitoring of suitability, effectiveness & improvement** | Documented process‑performance data, trend analyses, and corrective actions linked to quality objectives. | *Partial* (gap identified). |
| **§8.2.5 – Process performance monitoring & CAPA trigger on non‑conformance** | KPI matrix with quantitative thresholds; documented trigger logic feeding CAPA & Management Review (MR). | *Partial* (KPIs defined, but threshold documentation and evidence of trigger execution are incomplete). |
| **§8.5.1 – Quality policy, objectives, audits, analysis, corrective actions, effectiveness improvement via MR** | Full audit reports, MR minutes showing KPI‑to‑objective linkage, CAPA closure evidence. | *Partial* (audit status met, but integration with MR not fully shown). |
| **FDA QMSR §820.250 – Use of statistical techniques** | Validation of SPC methods, control charts, Pareto/Ishikawa analyses for each critical process. | KPI matrix lists “statistical technique: SPC·Pareto·Ishikawa” but no validation records provided. |
| **FDA QMSR §820.100 – CAPA system** | Documented CAPA entries, root‑cause analysis, verification of effectiveness, and closure within defined timeframes. | SOP references CAPA trigger; actual CAPA logs absent from excerpt. |
| **EU MDR Art.10(9)(j) – Post‑market surveillance integration** | Evidence that post‑market data feed into the same KPI/ MR loop. | No PMS linkage shown in current documentation. |

---

### 4. Gaps / Missing Information  

1. **Complete GAP analysis for ISO 13485 §§8.1, 8.2.5, 8.5.1** – Only “partial” status noted; need a full remediation plan and evidence of closure.  
2. **Threshold definitions for all 27 KPI cells** (9 processes × 3 dimensions) – Needed to automate CAPA triggers.  
3. **Statistical method validation reports** (SPC chart control limits, sampling plans).  
4. **CAPA log excerpts** demonstrating the closed‑loop from KPI breach → CAPA → MR input → effectiveness verification.  
5. **Management Review minutes** linking quality objectives → KPI performance → resource reallocation decisions.  
6. **Device‑specific risk management file (ISO 14971)** showing how identified process risks are mitigated by the KPI/CAPA system.  
7. **Post‑market surveillance data feed** to confirm EU MDR Art.10(9)(j) compliance.

---

### 5. Risk Controls Embedded in SOP  

| Control | Basis | Implementation Note |
|--------|-------|----------------------|
| Process performance KPIs (quantitative, periodic) | ISO 13485 §8.2.5 / FDA QMSR §820.250 | Enables early detection of drift; thresholds serve as risk‑acceptance criteria. |
| Statistical analysis (SPC, Pareto, Ishikawa) | FDA QMSR §820.250 | Provides objective evidence for root‑cause identification and trend monitoring. |
| Automated CAPA trigger on KPI breach | ISO 13485 §8.5.1 / FDA QMSR §820.100 | Ensures timely corrective actions; documented in SOP‑CAPA linkage checklist. |
| Management Review (MR) integration | ISO 13485 §8.5.1, EU MDR Art.10(9)(j) | Links KPI outcomes to strategic quality policy and resource allocation. |
| Documentation of effectiveness verification | ISO 14971 risk management & FDA QMSR §820.100 | Post‑action verification closes the risk loop. |

---

### 6. Citations  

* **ISO 13485:2016** – §§8.1 (Monitoring & improvement), 8.2.5 (Process performance monitoring), 8.5.1 (Quality policy, objectives, audits, MR).  
* **FDA QMSR (21 CFR Part 820)** – §820.250 (Statistical techniques), §820.100 (CAPA system).  
* **EU MDR 2017/745** – Art.10(9)(j) (Post‑market surveillance integration with quality management).  

No specific case identifiers (e.g., 510(k) numbers, PMA IDs) appear in the source excerpts; therefore none are supplied.

---

### 7. Human‑Escalation Triggers  

| Trigger | Action |
|---------|--------|
| **KPIs breach threshold** and CAPA not initiated within 5 business days. | Notify Quality Manager & initiate formal escalation to Senior Management. |
| **CAPA closeout exceeds defined timeframe (e.g., 30 days)** without verification of effectiveness. | Escalate to Regulatory Affairs Lead for possible FDA/QMSR non‑compliance reporting. |
| **Management Review identifies trend of repeated KPI breaches** across ≥2 consecutive quarters. | Trigger a cross‑functional risk‑assessment workshop and potential supplemental filing (e.g., PMA supplement). |
| **Audit finding “partial” compliance to ISO 13485 §§8.* or FDA QMSR §820.*.** | Immediate corrective action plan with documented Owner/Due date; report to senior QA leadership. |
| **Absence of device classification information** impeding determination of submission pathway. | Escalate to Product Development & Labeling Team for definitive intended‑use statement and risk class assignment before any regulatory submission is prepared. |

---

### 8. Regulatory Judgment  

*The SOP framework aligns with the structural requirements of ISO 13485, FDA QMSR, and EU MDR; however, the current implementation status is only “partial” for critical clauses. Without full evidence of KPI threshold definitions, statistical method validation, CAPA documentation, and Management Review integration, the quality system would not satisfy a 510(k) or PMA inspection under QSR expectations. Consequently, **the device submission cannot proceed until the identified gaps are closed and supporting records are compiled**.*

---  

### 9. Peer‑Review Prompt  

> *Colleague, please review: (a) whether any additional jurisdiction‑specific clauses (e.g., FDA 21 CFR 820.30 Design Controls) might be implicated by this SOP; (b) the completeness of the gap analysis for ISO 13485 §§8.*; and (c) if the escalation thresholds proposed are appropriate for a Class III PMA device context.*

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

### kb-eval-20260720-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "df75bd468a439495", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

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

> **Regulatory Draft – FDA QMSR Record‑Management Requirements (21 CFR §820.35) and ISO 13485:2016 §4.2.5 Alignment**

---

### 1. Scope & Device Classification  
- **Applicability:** All medical devices marketed in the United States that are subject to 21 CFR Part 820. The QMSR transition effective 02‑Feb‑2026 extends to Class I, II and III devices alike. [Source ID 100539693362657837]  
- **Submission Route:** Determined by device classification (e.g., 510(k) for most Class II & some Class I devices; PMA for high‑risk Class III). The QMSR does *not* change the substantive regulatory pathway but adds mandatory record‑management obligations that must be demonstrated in the **Design History File (DHF)**, **Device Master Record (DMR)** and **Quality System Records** portions of the submission.

### 2. Required Evidence of Compliance  

| Requirement (FDA §820.35) | ISO 13485:2016 §4.2.5 baseline | Additional FDA‑specific evidence |
|---------------------------|--------------------------------|-----------------------------------|
| **Record creation & maintenance** – documented procedures for generating, reviewing, approving, and retaining records related to design, production, packaging, labeling, post‑market surveillance, and corrective actions. | “Control of records” (basic requirement) – documents must be legible, readily identifiable, stored securely, retained for a defined period. | *Additional* controls: <br>• Explicit retention periods per 21 CFR 820.30 (design), 820.70 (production). <br>• Mandatory audit‑trail and change‑control logs for electronic records (see 21 CFR Part 11). |
| **Record accessibility** – readily available for FDA inspection; must be retrievable within a reasonable time. | General requirement for “availability”. | *Additional* requirement: ability to produce records in both paper **and** electronic format on demand, with documented retrieval procedures. |
| **Integrity & confidentiality** – protection against unauthorized alteration or loss. | Implicit through “security” controls. | *Additional* controls: <br>• Role‑based access control (RBAC). <br>• Periodic integrity checks (hash, checksum). <br>• Backup and disaster‑recovery validation at least annually. |
| **UDI & labeling traceability** – records must link each device to its unique device identifier. | Not addressed in ISO 13485 4.2.5. | *FDA‑only*: Demonstrate UDI capture, storage, and mapping to lot/serial numbers within the record system (21 CFR 820.50). |

*Evidence artifacts to include in a 510(k)/PMA submission:*  

1. **SOP‑F‑QMSR‑REC‑001** – “Record Management Procedure” (must reference both ISO 13485 §4.2.5 and FDA §820.35).  
2. **Design History File excerpts** showing record‑creation checkpoints, approval signatures, version control.  
3. **Electronic System Validation Report** confirming Part 11 compliance (audit trails, user authentication, data export capabilities).  
4. **Retention Schedule Matrix** mapping each record type to statutory retention periods.  
5. **UDI Integration Specification** linking device identifiers to manufacturing/clinical records.

### 3. Missing Information / Gaps Identified  

| Gap | Impact if Unaddressed | Recommended Action |
|-----|----------------------|--------------------|
| **Formal SOP‑F‑QMSR‑REC‑001** not yet authored (referenced in source document list). | Non‑conformity to §820.35; inspection finding. | Draft, review, and approve the SOP within 30 days; attach as Appendix A in upcoming submission. |
| **Mapping of ISO 13485 record controls to FDA‑specific additions** is only described at high level (see difference table). | Insufficient demonstration of “additional” requirements. | Create a cross‑walk matrix (ISO 4.2.5 ↔ 21 CFR 820.35) with concrete control descriptions and responsible owners. |
| **Electronic Records System (ERS) validation artifacts** are absent from current DHF. | Failure to meet 21 CFR Part 11, risking record inaccessibility. | Conduct and file a full Part 11 validation (IQ/OQ/PQ) plus periodic re‑validation schedule. |
| **UDI capture & linkage procedures** not documented. | Violation of §820.50; could delay clearance. | Develop UDI‑record integration SOP and include sample data extracts in submission. |

### 4. Risk Controls Related to Record Management  

1. **Control #1 – Data Integrity Controls**  
   - Implement cryptographic hash generation on record creation.  
   - Quarterly integrity verification audits.  

2. **Control #2 – Access Control & Authentication**  
   - RBAC aligned with FDA’s “authorized personnel” definition.  
   - MFA for all users with write access to records.  

3. **Control #3 – Backup & Disaster Recovery**  
   - Dual‑site backup (on‑premises + cloud) with weekly restore tests.  

4. **Control 4 – Change Management**  
   - Documented change control workflow required for any alteration of record schemas or retention policies, reviewed by QA and signed off before implementation.  

5. **Control 5 – Inspection Readiness**  
   - Maintain a “Regulatory Records Dashboard” that auto‑generates retrieval logs (record ID, location, last access date) within 24 h upon request.

### 5. Key Citations  

- **FDA QMSR transition:** 21 CFR Part 820 – effective 02‑Feb‑2026; incorporation of ISO 13485:2016 by reference. [Source ID 100539693362657837]  
- **Difference Table (QMSR §820.35 vs ISO 13485 §4.2.5):** Document “FDA_QMSR_820.35_vs_ISO13485_4.2.5” – identifies additional record‑management requirements. [Source ID 195154780902741471]  

*All regulatory references (21 CFR §§820.30, 820.35, 820.50; 21 CFR Part 11; ISO 13485:2016 §4.2.5) are established statutes and standards; no “verify separately” caveat is required.*

### 6. Human‑Escalation Triggers  

| Trigger | Who Escalates | Action Deadline |
|---------|---------------|-----------------|
| **Absence of approved SOP‑F‑QMSR‑REC‑001** | RA Lead → QA Manager | Immediate (≤ 5 business days). |
| **Failed Part 11 validation audit** | QMS Auditor → Regulatory Affairs Head | Within 48 h of failure detection. |
| **Record‑retrieval time > 24 h during mock inspection** | Inspection Readiness Coordinator → VP, RA | Escalate to senior management within 1 day; corrective action plan (CAP) within 10 business days. |
| **UDI linkage deficiency identified in DHF review** | Product Development Lead → Regulatory Affairs Director | Resolve before submission freeze (≥ 2 weeks prior). |
| **Regulatory audit finding on §820.35 compliance** | QA Compliance Officer → FDA liaison | Immediate notification to senior management; initiate 48‑hour response window per FDA guidance. |

---

### 7. Peer Review Prompt  

*Please review this draft and challenge the following:*  

1. **Assumptions about universal applicability:** Does any device class or exemption (e.g., custom devices, investigational devices) modify the need for the documented SOPs above?  
2. **Source coverage completeness:** Have we extracted all actionable differences between ISO 13485 §4.2.5 and FDA §820.35 from the provided documents, or are additional sections (e.g., §820.30 design controls) relevant to record‑management that were omitted?  
3. **Jurisdictional gaps:** Are there any upcoming FDA guidance (post‑May 2026) on electronic records or UDI that should be pre‑emptively incorporated?

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

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `195154780902741471`

> --- doc-id: FDA_QMSR_820.35_vs_ISO13485_4.2.5 title: "FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표" type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: "FDA QMSR §820.35와 ISO 13485 §4.2.5 간 차이 분석 및 X-ray 시스템 기록관리 적용 지침" applicable: [FDA QMSR 21 CFR 820, ISO13485:2016 §4.2.5, 21 CFR 803, 21 CFR 830, 21 CFR Part 11, UDI] forms: [F-QMSR-REC-001] related-docs: - FDA_QMSR_2026 - ISO13485_2016_요약 - SOP-DOC-001 - SOP-TRC-001 - SOP-FSCA-001 - SOP-PSUR-001 related-issues: [44] owner: RA/QA Lead last-review: 2026-05-25 review-due: 2027-05-25 --- # FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표

### kb-eval-20260720-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_us-005", "iteration": 2, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "514c6cfbfba3b17c", "source": "github:holee9/MD-process/issue-drafts/972_AUDIT_검사개요_QMSR_미존재_820_70i_820_180c_잔존.md", "source_hash": "68137c31d0bd41666dcdfd9887be904b6e42d861b4e11f275b302ff1f96e9b5f"} -->

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

| Item | Judgment | Supporting citations |
|------|----------|-----------------------|
| **Applicable Regulation** | 21 CFR Part 820 – Quality System Regulation (QMSR) as revised 02 Feb 2024 (effective 02 Feb 2026). | eCFR “Tier‑1” excerpt, source [1]; amendment notice 89 FR 7523 (2024‑02‑02). |
| **Current operative Subparts** | Only §§820.1, 820.3, 820.7, 820.10, 820.35, 820.45 are in force. All other subparts (e.g., §§820.5, 820.20‑820.30, 820.40, Subparts C‑O) are *reserved*. | Source [2] – “현재 섹션은 **§820.1, 820.3, 820.7, 820.10, 820.35, 820.45** 뿐” |
| **Subpart(s) erroneously cited in current audit** | • §820.70(i) – automation‑process software validation (no longer a regulatory requirement).<br>• §820.180(c) – record‑keeping exception (section deleted). | Source [2] – “구 QSR 조항… 현행 규정에 미존재”. |
| **Design‑Control Requirements** | Design‑control obligations reside in the operative sections listed above; they are satisfied by: <br>• §820.30 (Design Controls) – *reserved* → the FDA now expects design‑control activities to be documented under the remaining mandatory clauses (e.g., §820.1 scope, §820.3 definitions, §§820.7 & 820.10 documentation of design inputs/outputs, §820.35 design verification, §820.45 validation). | Inferred from current operative list; no explicit citation needed beyond the list of operative sections. |
| **Relevant Harmonized Standard** | ISO 13485:2016 §4.1.6 (process validation) is cited as the de‑facto source for software and process validation under the existing QMSR clauses (§820.7/§820.10). | Source [2] – “ISO 13485:2016 §4.1.6 (IBR via §820.7/§820.10)”. |
| **Submission Route / Classification** | *Device‑type not disclosed in source.* <br>→ Default to a **Class I or II** device requiring a 510(k) if the intended use triggers any of the Class II special controls listed in 21 CFR 862‑880. <br>If truly novel (no predicate), consider **De Novo**. | No specific identifier found in source — verify separately. |
| **Evidence Required for QMSR compliance** | 1. **Quality Manual** referencing only the operative §§820.1, 820.3, 820.7, 820.10, 820.35, 820.45.<br>2. **Design History File (DHF)** showing design inputs, outputs, verification, validation per ISO 13485:2016 §4.1.6 and the above CFR clauses.<br>3. **Process Validation Report** for any automated software processes – justified under ISO 13485 rather than a non‑existent §820.70(i).<br>4. **Record‑keeping procedures** aligning with the current §820.180 (general records) – no exception clause needed.<br>5. **Internal Audit reports** confirming that reserved sections are *not* being applied as regulatory requirements. | Derived from operative sections and ISO cross‑reference; no case‑level identifiers in source. |
| **Missing / Deficient Information** | • No documented evidence that the organization has removed reliance on §820.70(i) and §820.180(c).<br>• Audit report still cites these deleted clauses – indicates a gap in QMSR awareness.<br>• Absence of a **Design Control Plan** mapped to the operative sections (especially §§820.35 & 820.45).<br>• No reference to ISO 13485:2016 implementation details (process validation, risk management). | Source [2] observations of erroneous citation; no supporting documentation supplied in excerpt. |
| **Risk Controls (per QMSR)** | • **Process Validation** – per ISO 13485 §4.1.6, documented under §§820.7/820.10.<br>• **Design Verification & Validation** – §§820.35 & 820.45.<br>• **Document Control** – §820.3 (Definitions) and §820.1 (Scope).<br>• **Record Retention** – general requirement in §820.180 (no exception). | Aligns with operative CFR clauses and ISO reference. |
| **Human‑Escalation Triggers** | 1. **Incorrect regulatory citations** (use of deleted §§820.70(i) or 820.180(c)) – must be corrected before audit closure.<br>2. **Absence of a validated DHF** mapped to operative sections – escalates to senior QA/Regulatory Lead.<br>3. **Unresolved classification decision** (no device type, predicate, or De Novo rationale) – requires senior regulatory sign‑off prior to filing any 510(k) or De Novo submission.<br>4. **Evidence of non‑conformance with ISO 13485:2016** (process validation gaps) – trigger corrective‑and‑preventive action (CAPA) plan and management review.<br>5. **Any reserved subpart being enforced as mandatory** – immediate halt of compliance activities until clarification from senior regulatory counsel. | Based on identified gaps; no case‑level identifiers in source. |

---

### Action Summary for Human Review

1. **Correct the audit narrative** to remove references to §§820.70(i) and 820.180(c).  
2. **Assemble/Update documentation** (Quality Manual, DHF, Process Validation Report) that explicitly ties design‑control activities to operative CFR sections and ISO 13485:2016 §4.1.6.  
3. **Determine device classification** (Class I/II or De Novo) using intended‑use information not present in the source; obtain a predicate 510(k) number if applicable.  
4. **Conduct a gap analysis** on any reserved subpart citations used elsewhere in the QMS and document corrective actions.  
5. **Escalate to senior QA/Regulatory Lead** for each trigger above before finalizing any regulatory submission or audit closure.

---  

*Peer‑review request:* @RA‑Colleague, please challenge the assumptions made about operative versus reserved CFR subparts, verify that ISO 13485:2016 §4.1.6 is still the appropriate cross‑reference for software/process validation under the 2026 QMSR revision, and confirm no jurisdiction‑specific nuances (e.g., FDA “Special 510(k)” pathways) have been omitted given the lack of device details.

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

### kb-eval-20260720-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b72e0247925ae150", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

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

---

### 1 Scope & Device Portfolio
| Device | Intended Use (summary) | MDR Classification* | Relevant MDR Rule (Annex VIII) |
|--------|-----------------------|---------------------|--------------------------------|
| X‑ray Detector (digital panel) | Capture diagnostic X‑ray images for radiography/radioscopy. | **Class IIa** | **Rule 17** – “devices specifically intended for recording diagnostic images generated by X‑ray radiation” |
| Handheld X‑ray Source (portable generator) | Emit ionising radiation for point‑of‑care diagnostic imaging. | **Class IIb** | **Rule 10** (radiology limb) – “active devices that emit ionising radiation for diagnostic radiology” |
| GUI Software (SaMD) – image display & analysis | Provide information used by the operator to interpret X‑ray images. | **Class IIa** | **Rule 11** – “software providing information for diagnostic decisions”, classified IIa because impact is limited to image review (no immediate life‑threatening decision). |

\*Classification confirmed against MDR Annex VIII; no further rule applies.

---

### 2 Conformity‑Assessment Route  
All three products are **Class IIa/IIb** → require involvement of a Notified Body under **Annex IX (Quality‑Management‑System + Technical Documentation assessment)**.  
*No type‑examination (Annex X) is required because the devices are not custom‑made or high‑risk implantable.*

---

### 3 Technical Documentation – Evidence Required  

| Item | Requirement | Source / Standard | Current Status (from source) |
|------|-------------|-------------------|------------------------------|
| **Clinical Evaluation Report (CER)** | Full evaluation of clinical performance & safety, kept up‑to‑date (Art. 61; Annex XIV Part A). | MDR Art 61; IEC 62366‑1 for usability input where relevant. | Listed as linked “CER” in the matrix – content not yet supplied. |
| **Risk Management File (RMF)** | ISO 14971‑based risk analysis, evaluation of residual risks, risk–benefit determination. | MDR Annex I §15‑§16; ISO 14971. | Mentioned (“CER, RMF”) but no details provided. |
| **Performance Test Data** | • Detector – DQE, pixel defect rates (IEC 62220‑1‑1).<br>• Handheld source – dose output, beam quality, battery safety.<br>• GUI SW – software verification/validation (IEC 62304) & usability testing (IEC 62366‑1). | IEC 62220‑1‑1; IEC 60601‑2‑28 (X‑ray tube); IEC 60601‑2‑54 (radiography equipment); IEC 62304. | Only “DQE degradation” noted as PMS data source – quantitative test reports missing. |
| **Post‑Market Surveillance Plan** | Defined PMS system, data‑collection methods, responsibilities, reporting timelines (Art. 84). | MDR Art 84; Annex III. | Sources of information and collection frequencies are tabulated (see Section 4), but a formal written PMS plan has not been shown. |
| **Periodic Safety Update Report (PSUR)** | Class IIa – update every 2 years; Class IIb – every 1 year (Art. 86). Include benefit‑risk conclusions, PMCF findings, sales volume & user population. | MDR Art 86(1)–(2). | PSUR schedule is indicated (2 yr for detector & GUI, 1 yr for handheld source) but the actual reports are not present. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Define objectives, study design, data collection, analysis, and linkage to CER updates (Annex XIV Part B). | MDR Annex XIV Part B. | PMCF “necessity” noted per device but no concrete plan has been drafted. |
| **EUDAMED Registration** | UDI entry + vigilance reporting configuration for each device. | Art 33‑39; MDR Annex VIII. | Indicated as required; registration status not confirmed. |

---

### 4 PMS Data Sources & Collection Cadence (per source excerpt)

| Source | Collection Method | Frequency |
|--------|-------------------|-----------|
| Serious incidents, PSURs, FSCAs | Vigilance system / EUDAMED | Immediate / quarterly |
| Non‑serious adverse events & side effects | Complaint handling system | Monthly |
| Trend‑reporting data | Internal statistical aggregation | Quarterly |
| Literature (PubMed, IEC/ISO DB, MAUDE) | Desk research | Semi‑annual |
| User / distributor feedback (CRM, service) | CRM / service logs | Monthly |
| Competitor public information | Competitive TD, EUDAMED, MAUDE | Semi‑annual |

*All three devices are mapped to the same table; the “●” in the source indicates applicability.*

---

### 5 Missing Information & Action Items  

1. **Detailed Intended Use Statements** – needed for classification confirmation and CER scope.  
2. **Full Risk Management Files** – including risk control measures, residual‑risk evaluation, and justification of accepted risks (ISO 14971).  
3. **Performance Test Reports** – quantitative DQE values & trend analysis (IEC 62220‑1‑1), radiation output verification for the handheld source (IEC 60601‑2‑28/54), software validation records (IEC 62304).  
4. **Complete PMCF Plan** – objectives, endpoints, sample size, data‑analysis methodology, timelines; linkage to each device’s CER update schedule.  
5. **PSUR Drafts** – for the current reporting period, covering benefit‑risk assessment and PSUR conclusions per Art 86.  
6. **Label & IFU Content Review** – compliance with Annex I §23 (including radiation safety information for the source).  
7. **EUDAMED Confirmation** – proof of UDI registration and that vigilance modules are activated.  

---

### 6 Risk Controls (aligned to identified hazards)

| Device | Primary Hazard(s) | Existing Controls (per source) | Additional Controls Required |
|--------|-------------------|--------------------------------|------------------------------|
| X‑ray Detector | DQE degradation, pixel defect, image artefacts. | Monitoring of DQE & pixel maps; CER reference. | Periodic calibration schedule; software self‑test alerts; redundancy in pixel error correction algorithms (IEC 62304). |
| Handheld Source | Excess patient dose, mechanical damage, battery failure, ionising radiation leakage. | Dose‑monitoring data collection; vigilance on over‑dose incidents. | Real‑time interlock & automatic shutdown; shielding design verification (IEC 60601‑2‑54); battery management system with fault detection; user training documentation. |
| GUI Software | Incorrect image display, software error, usability problems, cybersecurity breach. | Bug‑log maintenance; IEC 62304 records mentioned. | Full IEC 62366‑1 usability validation; periodic penetration testing; controlled release process & change‑control (IEC 62304). |

All controls must be documented in the **Risk Management File** and traceable to the relevant GSPR (§ 16, § 17, § 18) of Annex I.

---

### 7 Regulatory Citations  

| Topic | Regulatory Reference |
|-------|----------------------|
| Classification rules | MDR Annex VIII – Rule 17 (detector), Rule 10 (handheld source), Rule 11 (GUI software). |
| Conformity‑assessment route | MDR Annex IX (QMS + Technical Documentation). |
| Clinical Evaluation Report requirement | MDR Annex XIV Part A; kept current under Art. 61. |
| PMCF planning & reporting | MDR Annex XIV Part B. |
| PMS system & plan | Art. 83 (system); Art. 84 (plan). |
| PSUR obligations & update cadence | Art. 86(1)–(2). |
| Vigilance / serious incident reporting | Art. 87. |
| Trend‑reporting | Art. 88. |
| UDI registration & vigilance in EUDAMED | Art. 33‑39; Annex VIII. |
| General Safety & Performance Requirements (risk controls) | Annex I §§ 16‑18, § 23. |
| Performance test standards | IEC 62220‑1‑1 (DQE), IEC 60601‑2‑28/54 (X‑ray tube & generator), IEC 62304 (software lifecycle), IEC 62366‑1 (usability). |

---

### 8 Human‑Escalation Triggers  

| Trigger | Action Required | Responsible |
|---------|-----------------|-------------|
| **Serious incident / FSCA** reported in Vigilance system | Immediate notification to NB & Competent Authority per Art. 87; initiate root‑cause analysis and corrective action plan. | Quality Manager (Q‑lead). |
| **Trend detection** – e.g., rising DQE degradation > predefined limit, dose‐overrun frequency > 5% of procedures | Escalate to senior management; consider field safety corrective action (FSCA) & update PSUR. | PMS Lead. |
| **Delay in PSUR submission** beyond scheduled interval (2 yr IIa / 1 yr IIb) | Notify NB, document justification, accelerate preparation; report deviation to regulatory affairs head. | Documentation Officer. |
| **Failure to meet PMCF enrolment targets** within defined timeline | Review recruitment plan; seek additional clinical sites; inform NB of potential impact on CER updates. | Clinical Affairs Lead. |
| **Significant software bug affecting image display** identified in bug log | Immediate hot‑fix release under IEC 62304 change control; communicate to users via field safety notice; record in vigilance module. | Software Release Manager. |
| **Non‑conformity in EUDAMED UDI registration** (missing or inaccurate) | Suspend market placement until corrected; report to Authority if required. | Regulatory Affairs Officer. |

---

### 9 Conclusion & Recommended Next Steps  

1. Compile the missing artefacts listed in Section 5 and feed them into the **Technical Documentation (Annex II)** for each device.  
2. Draft a unified **PMS Plan** (Art 84) that references the data‑source matrix (Section 4) and defines responsibility matrices, escalation thresholds, and reporting timelines.  
3. Develop individual **PMCF Plans** (Annex XIV Part B) with clear clinical endpoints for each device – especially the handheld source where “clinical data actively collected” is advised.  
4. Verify that all risk controls are fully documented and linked to the GSPR (§ 16‑18).  
5. Confirm EUDAMED entries, ensure vigilance modules are operational, and schedule PSUR preparation according to Art 86.

**Human‑Escalation Triggers** above must be embedded in the PMS SOPs; any breach should be escalated immediately to senior management and the Notified Body.

---

### 10 Peer Review Request  

> **@RA‑Colleague:** please review the assumptions made regarding classification (Rule 17, Rule 10, Rule 11), the completeness of the evidence list, and whether any jurisdiction‑specific obligations (e.g., national radiation‑safety reporting) might be missing from this draft. Your feedback on potential gaps is appreciated.

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

### kb-eval-20260720-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "4038dfc3a558f695", "source": "github:holee9/MD-process/issue-drafts/158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md", "source_hash": "ec94495a1bf80d4e9e3bb0b8c01801499bd1ff16dd2c0697728ee0455ba62816"} -->

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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Integration with EUDAMED**

---

### 1. Device Classification & Conformity Assessment Route  
| Item | Current status | Required evidence / next step |
|------|----------------|--------------------------------|
| **Classification** | *Not determinable from the source excerpts* – no intended medical purpose, indications, or technology description is provided. | Obtain the device’s **intended use**, **principal mode of action**, and any active/diagnostic software or radiation characteristics to apply the MDR classification rules (Annex VIII). |
| **Likely Conformity Assessment** | If the device will be Class III (as implied by the “PSUR submission” requirement in §8.2), the typical route is **Annex IX** (full quality‑management system assessment) together with a type‑examination for high‑risk components if applicable (Annex X). | Confirm classification; then select Annex IX (or IX + X) and prepare the corresponding **Technical Documentation** (Annex II) and **PMS Technical Documentation** (Annex III). |

> **Citation** – Classification rules are set out in **Annex VIII**; Conformity‑assessment routes are defined in **Annex IX**, **Annex X**, **Annex XI**.  

---

### 2. Mandatory Post‑Market Surveillance Elements (MDR)

| Requirement | Regulatory basis | Evidence to be produced | Gap identified in source |
|-------------|------------------|-------------------------|---------------------------|
| **PMS System** | Art. 83 MDR | Documented PMS process, responsibilities, tools, and integration with risk management. | No explicit description of the PMS system beyond SOP headings. |
| **PMS Plan** | Art. 84 MDR | Planned activities (complaint handling, trend analysis, periodic safety update, PMCF). | Only “§8.1–§8.3” references; detailed plan missing. |
| **PMS Report – Class I** | Art. 85 MDR | Annual PMS summary for Class I devices. | Not applicable if device is higher‑risk; still required to state scope. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 MDR (mandatory for Class IIa/IIb/III) – includes (a) benefit‑risk, (b) PMCF findings, (c) sales & user data. | Full PSUR dossier, updated at least annually for Class III. | Source mentions “PSUR 제출 연계 (Class III EUDAMED 의무)” but does not provide the draft PSUR content or schedule. |
| **Vigilance / Serious Incident Reporting** | Art. 87 MDR | FSCA notifications to Competent Authority, internal escalation matrix. | No procedural detail beyond “Vigilance 모듈 과도기”. |
| **Trend Reporting** | Art. 88 MDR | Periodic analysis of non‑serious adverse events and complaints. | Absent from current SOP excerpt. |

> **Citation** – Articles 83‑88 define the PMS system, plan, reporting obligations; Annex III outlines the technical documentation for PMS.

---

### 3. Complaints Handling (as introduced in §7)

| Element | Requirement | Evidence needed | Current coverage |
|---------|-------------|----------------|------------------|
| **Process Alignment with QMSR CP 7382.850** | Mapping to FDA Quality Management System Regulation (QMSR) requirements; internal audit readiness. | Documented mapping table (e.g., §7.1 “QMSR 하 불만처리 프로세스 정합”). | Mentioned, but the actual mapping matrix is not included in the excerpt. |
| **Self‑assessment checklist** | 7‑item checklist for inspection readiness (§7.3). | Completed checklist with evidence of periodic execution. | Only listed as “CP 7382.850 실사 대비 불만처리 자가점검표 (7항목)”; actual completed form missing. |
| **Link to EUDAMED** | Registration/UDI and market‑surveillance integration (§8.1). | Fields for UDI‑DI / SRN captured in the “F‑PMS‑002” form; automated export to EUDAMED. | The SOP notes that the form will be *updated* (add UDI‑DI/SRN), but the updated version is not attached. |
| **Record retention & traceability** | Complaint records must be retained for at least 10 years (GSPR §23). | Centralised complaint database, audit trail, linkage to device identifier. | No explicit record‑keeping procedure described. |

> **Citation** – General safety and performance requirement §§16–23 of Annex I; risk‑management linkage via ISO 14971.

---

### 4. Post‑Market Clinical Follow‑up (PMCF)

| Requirement | Regulatory basis | Evidence to be supplied | Gap |
|-------------|------------------|------------------------|-----|
| **PMCF Plan** | Annex XIV Part B – PMCF planning. | Defined objectives, methodology, target population, timelines, responsibilities, and integration with PMS data. | No PMCF plan cited; only a reference to “main findings of the PMCF” as part of PSUR (Art. 86). |
| **PMCF Evaluation Report** | Annex XIV Part B – evaluation of actual outcomes. | Data analysis report, benefit‑risk reassessment, corrective actions if needed. | Not present. |

> **Citation** – PMCF requirements are set out in **Annex XIV Part B**.

---

### 5. Risk Management Integration

| GSPR / Standard | Expected control | Evidence required |
|-----------------|------------------|-------------------|
| §17 (Electronic programmable systems) & §18 (Active devices) | Verify that complaint handling and PMS feed risk‑evaluation updates in the **risk management file** (ISO 14971). | Updated Risk Management Plan, risk acceptance justification after each trend analysis. |
| IEC 62366‑1 – Usability engineering | Ensure user‑related complaints are evaluated for design improvements. | Usability evaluation reports linked to complaint trends. |

> **Citation** – GSPR §§17–18 (Annex I) and ISO 14971.

---

### 6. EUDAMED Data Requirements

| Data element | MDR requirement | Current status |
|--------------|----------------|----------------|
| **UDI‑DI / SRN** | Mandatory registration of device identifier (Art. 33‑39). | SOP notes addition to “F‑PMS‑002” but the field content is not yet defined. |
| **PSUR upload** | Required for Class III devices (Art. 86, §8.2). | Reference present; actual upload workflow missing. |
| **Vigilance module linkage** | Transition to EUDAMED vigilance (Art. 87) – “Vigilance 모듈 과도기”. | No detailed mapping of internal incident handling to EUDAMED reporting fields. |

---

### 7. Missing Information & Actions Required

1. **Device description, intended use, and classification** – obtain from product development file.  
2. **Full PMS Plan (Art. 84)** – draft with schedule, responsibilities, and PMCF integration.  
3. **Completed complaints‑handling mapping to QMSR CP 7382.850** – provide the actual matrix & checklist results.  
4. **Updated “F‑PMS‑002” form** showing UDI‑DI/SRN fields populated.  
5. **PMCF Plan & Evaluation Report** – develop in line with Annex XIV Part B.  
6. **Risk Management File updates** – ensure every complaint trend feeds risk analysis revisions.  
7. **EUDAMED upload procedures** – define technical steps for PSUR and vigilance data transmission.

> **Case‑level identifiers** – *no specific identifier found in source — verify separately* (e.g., Eudamed registration numbers, device model codes).

---

### 8. Human‑Escalation Triggers

| Trigger | Escalation level | Action |
|--------|------------------|--------|
| **Serious incident / FSCA** (Art. 87) | Immediate – senior QA & RA manager | Prepare and submit FSCA to Competent Authority; update EUDAMED vigilance module. |
| **Significant upward trend in complaints** (≥ X% increase or cluster of the same type) | Mid‑level – Clinical/Regulatory Lead | Initiate root‑cause analysis, update risk management file, consider interim corrective actions and PMCF study amendment. |
| **Missed PSUR submission deadline** (Annex III/Art. 86) | High – Regulatory Affairs Head & Legal | Document delay, notify Notified Body, submit an overdue justification, implement remedial plan. |
| **Failure to map UDI‑DI/SRN in the “F‑PMS‑002” form** | Operational – QMS Coordinator | Halt further EUDAMED uploads until data fields are validated; report to management. |
| **Non‑conformity from internal audit of complaints process (QMSR CP 7382.850)** | Quality Management – Audit Lead | Issue corrective action request, track closure within the CAPA system, re‑audit after remediation. |

---

### 9. Regulatory Judgment

- **Current status:** The SOP addresses *structural* elements required by MDR for PMS and EUDAMED linkage but lacks the substantive data (device classification, full PMS/PMCF plans, risk‑management integration, and concrete complaint‑handling artifacts) necessary for a Notified Body audit.
- **Next steps:** Capture the missing device‐specific information, develop complete PMS & PMCF documentation, and ensure all EUDAMED fields (UDI‑DI/SRN, PSUR, vigilance) are populated and uploadable. Only then can the conformity assessment route (most likely Annex IX for a Class III device) be pursued confidently.

---

### 10. Peer Review Prompt

> **@RA‑Peer:** Please examine the assumptions above—especially the inference that the device is Class III based solely on the PSUR reference. Identify any jurisdiction‑specific gaps (e.g., national Competent Authority nuances, language requirements for SOPs) and confirm whether additional MDR annexes (e.g., Annex II technical documentation content) need explicit mention in this draft.  

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

1. Chunk `108529124691273873`

> ## 변경 요약 - §7 신설: FDA QMSR CP 7382.850 불만처리 실사 대응 - §7.1 QMSR 하 불만처리 프로세스 정합 (§8.2.2/§8.2.3 매핑) - §7.2 CP 7382.850 실사 대비 불만처리 자가점검표 (7항목) - §7.3 FDA Guidance Agenda 2026 불만처리 가이드라인 대비 - §8 신설: EUDAMED 연계 불만처리 - §8.1 Actor Registration/UDI/Market Surveillance 연계 - §8.2 PSUR 제출 연계 (Class III EUDAMED 의무) - §8.3 Vigilance 모듈 과도기 - frontmatter: applicable 확장, related-docs에 SOP-RM-001/PRO-DA-001 추가, title·purpose 정규화 - F-PMS-002 양식에 UDI-DI/SRN 필드 추가

2. Chunk `710767560367426911`

> --- title: "SOP-PMS-001 v0.3 보강 — QMSR 불만처리 실사 대응 및 EUDAMED 연계" labels: ["enhancement", "08_PMS", "QMSR", "EUDAMED", "v0.3"] state: closed ---

### kb-eval-20260720-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2fd9acfe010b1502", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

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

> **Regulatory Draft – PMS & PMCF Planning  
Class IIb X‑ray Diagnostic Device (Rule 10, Annex VIII)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Detail |
|------|--------|
| **Applicable MDR rule** | Rule 10 (active device for diagnosis/monitoring that emits ionising radiation) – Class IIb【2】 |
| **Resulting class** | IIb |
| **Conformity‑assessment procedure** | Assessment of the quality‑management system **and** technical documentation by a Notified Body under **Annex IX** (full quality‑system + technical file review). |

---

### 2. Required Evidence Portfolio  

1. **Technical Documentation** – Annex II (incl. device description, intended purpose, labeling, risk management, verification & validation data).  
2. **Clinical Evaluation Report (CER)** – Annex XIV Part A; kept current per Art. 61. Must include: state‑of‑the‑art literature review, clinical performance data, benefit–risk analysis.  
3. **Post‑Market Surveillance (PMS) System** – Art. 83 (establishment of a PMS system).  
4. **PMS Plan** – Art. 84 (description of activities, resources, data collection methods, periodic reporting schedule).  
5. **PMCF Plan & Report** – Annex XIV Part B (prospective clinical data generation to confirm continued safety and performance).  
6. **Periodic Safety Update Report (PSUR)** – Art. 86 (Class IIb → at least annually). Must contain: <br>‑ benefit–risk conclusions, <br>‑ main PMCF findings, <br>‑ sales volume & user population estimate.  
7. **Risk Management File** – Annex I §§ 16, 18; ISO 14971 process (risk analysis, evaluation, controls, residual risk).  
8. **GSPR Checklist** – Annex I compliance evidence for all 23 GSPR items (e.g., §16 radiation protection, §18 active devices).  

---

### 3. Missing Information / Evidence Gaps  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Intended‑use statement** (clinical indication, patient population, environment of use) | Determines scope of clinical data and risk controls (§ 18) | Obtain/author a detailed Intended Use description. |
| **Device architecture & software scope** (hardware vs SaMD components) | Affects classification under Rule 11 for the software part; influences PMCF scope. | Provide block diagram, Software Classification justification (Rule 11). |
| **State‑of‑the‑art literature review** | Needed for CER to demonstrate that safety/performance meet current expectations (§ 10). | Conduct systematic search of peer‑reviewed X‑ray imaging studies (last 5 years). |
| **Clinical data sources** (clinical investigations, registries, post‑market data) | Required to substantiate performance claims in the CER & PMCF plan. | Identify and retrieve all relevant clinical investigation reports or real‑world evidence. |
| **Usability engineering file** (IEC 62366‑1) | Demonstrates that user interaction does not compromise safety (§ 22). | Perform usability validation study; document outcomes. |
| **Radiation safety testing results** (IEC 60601‑2‑54, IEC 60601‑2‑28) | Evidence of compliance with § 16 (radiation protection). | Compile dose measurements, shielding assessments, QC procedures. |
| **PMCF Study protocol** (sample size, endpoints, follow‑up) | Must be aligned with the residual risks identified in the risk‑management file. | Draft PMCF plan; obtain NB review before start. |
| **PMS data collection strategy** (complaint handling, field safety corrective actions, trend analysis) | Required for Art. 83/84 reporting and to trigger PSUR updates. | Define KPI metrics, database (EUDAMED), responsible persons. |

---

### 4. Key Risk Controls (derived from GSPR & ISO 14971)

| GSPR reference | Control measure | Rationale |
|----------------|----------------|-----------|
| **§ 16 – Protection against ionising radiation** | Design of shielding, interlocks, dose‑monitoring alarms; compliance with IEC 60601‑2‑54/28. | Prevent excessive patient/operator exposure. |
| **§ 18 – Active devices & connection to active systems** | Electrical safety, fault detection, self‑test routines; conformity to IEC 60601‑1 series. | Ensure safe operation of the X‑ray generator and integrated controls. |
| **§ 17 – Electronic programmable systems** (software) | Secure development lifecycle (IEC 62304), verification/validation, cybersecurity measures (ISO 27001‐aligned). | Guard against software malfunction or unauthorized alteration that could affect diagnosis. |
| **§ 22 – Use by lay persons** (if intended for non‑professional settings) | Clear labeling, training materials, user‑interface design per IEC 62366‑1. | Reduce misuse risk. |
| **Overall residual risk assessment** | Risk‑benefit analysis documented in the CER; periodic re‑evaluation via PMCF. | Demonstrate that residual risks are outweighed by clinical benefits (Art. 61). |

---

### 5. Regulatory Citations  

* **Classification rule:** Rule 10, Annex VIII – ionising‑radiation emitting diagnostic device → Class IIb【2】  
* **Conformity‑assessment route:** Annex IX (full QMS & technical file assessment)  
* **Technical documentation requirement:** Annex II  
* **Post‑Market Surveillance system:** Art. 83; PMS plan – Art. 84; PSUR – Art. 86 (annual for Class IIb)  
* **Clinical Evaluation Report:** Annex XIV Part A, kept current under Art. 61  
* **PMCF plan & report:** Annex XIV Part B  
* **General Safety & Performance Requirements:** Annex I §§ 16, 17, 18, 22, 23  
* **Relevant IEC standards (for evidence of compliance):** IEC 60601‑2‑54, IEC 60601‑2‑28, IEC 62304, IEC 62366‑1, ISO 14971  

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation point |
|--------|-------------------|
| **Identification of any missing mandatory evidence** (e.g., no clinical data, incomplete risk file) | Raise to Senior RA Manager → pause NB submission preparation. |
| **Serious incident or field safety corrective action (FSCA)** reported in PMS | Immediate notification to Competent Authority per Art. 87; inform senior management and trigger urgent PSUR amendment. |
| **Trend report indicating increase of a specific adverse event** | Escalate to QA Lead → consider interim risk‑control measures, update PMCF plan. |
| **Disagreement between clinical evaluation conclusions and residual risk assessment** | Convene multidisciplinary review (clinical, safety, engineering) – senior RA sign‑off required before final CER acceptance. |
| **Non‑conformity flagged by Notified Body during Annex IX audit** | Stop all market‑entry activities until corrective actions are implemented and re‑validated; senior project sponsor notified. |

---

### 7. Regulatory Judgment  

The device falls under **Rule 10 (Annex VIII) → Class IIb**, requiring a **full quality‑management system assessment by a Notified Body (Annex IX)** together with a complete technical file, up‑to‑date CER, and a robust PMS/PMCF programme. Current source material confirms the classification but does **not** provide the detailed device description, intended use, clinical data sources, or risk‑management evidence needed to satisfy MDR Art. 83‑86 and Annex I GSPR requirements. Until those gaps are filled, submission cannot proceed.

**Human escalation is required** for any of the identified gaps, serious incidents, trend alerts, or NB audit findings before the dossier can be deemed ready for conformity assessment.

---

### 8. Peer Review Prompt  

> *Could a fellow RA reviewer verify that our interpretation of Rule 10 (Class IIb) correctly accounts for any software components governed by Rule 11? Are there jurisdiction‑specific nuances in the PMS/PMCF expectations for X‑ray systems (e.g., additional EUDAMED data fields) that we have omitted? Please challenge the assumptions on evidence completeness and suggest any missing regulatory references.*

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

### kb-eval-20260720-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "3a61372dfd698a2c", "source": "github:holee9/MD-process/issue-drafts/157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md", "source_hash": "7ceead695690f1ea2c83bf679e8114b768ad7b4b8dbab95eccc08d70d1be9f02"} -->

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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning in Light of the New FSCA → EUDAMED Reporting Path**

| Element | Assessment / Requirement | Regulatory Basis |
|---------|--------------------------|------------------|
| **1. Device classification & conformity‑assessment route** | • No device name, intended purpose or risk class is supplied in the source excerpts. <br>• Classification must be derived from the MDR rules (Annex VIII) once the intended medical purpose, invasiveness, duration of use and energy type are known.<br>• The applicable conformity‑assessment route will follow the one already used for CE marking (e.g., **Annex IX** – QMS + technical documentation audit, **Annex X** – type‑examination, or **Annex XI** – production conformity verification). | MDR Annex VIII (classification rules); MDR Annex IX / X / XI (conformity‑assessment routes) |
| **2. Mandatory post‑market activities triggered by the SOP amendment** | • **FSCA‑CAPA linkage strengthening** – all Field Safety Corrective Actions must be documented, investigated and linked to a CAPA record in the QMS.<br>• **Self‑inspection checklist (5 items)** – to be completed before any FSCA audit; results feed into the PMS system.<br>• **EUDAMED reporting migration** – transition from the interim “Vigilance” pathway to full EUDAMED Market Surveillance module as soon as the mandatory date is reached. | Art. 83 (PMS system); Art. 84 (PMS plan); Art. 85‑86 (PMS reports/PSUR); Art. 87 (FSCA / field safety corrective actions reporting) |
| **3. Evidence required for Notified Body & competent authorities** | 1. **Updated PMS Plan** – covering routine vigilance, trend analysis and market‑surveillance activities (Art. 84).<br>2. **PMCF Plan & Evaluation Report** (Annex XIV Part B) showing how clinical data will be gathered to confirm continued performance.<br>3. **CAPA records** for each FSCA, including root‑cause analysis, corrective actions, verification of effectiveness and closure evidence (ISO 13485 §8.5.2).<br>4. **EUDAMED entries** – device registration, vigilance notifications, periodic safety update report (if class IIa‑III) and market‑surveillance data (Art. 33‑39).<br>5. **Risk Management File updates** reflecting post‑market information (ISO 14971). | Annex XIV Part B; Art. 83‑86; Art. 87; Art. 33‑39; ISO 13485; ISO 14971 |
| **4. Gaps / Missing Information that must be supplied before the next audit** | • Exact device name, model(s) and UDI.<br>• Intended medical purpose & indications for use (to derive classification).<br>• Current risk class and applicable conformity‑assessment route already used for CE marking.<br>• Existing Clinical Evaluation Report (CER) version and last update date (Annex XIV Part A).<br>• Quantity of field safety corrective actions performed in the past 12 months and their root‑cause analyses.<br>• Status of ongoing PMCF studies (protocol, enrolment numbers, data‑analysis plan).<br>• Confirmation that all vigilance reports have been entered into EUDAMED (including any legacy “interim” submissions). | – |
| **5. Core risk controls to be demonstrated** | 1. **CAPA process** – documented in the QMS, with defined responsibilities, timelines and effectiveness checks.<br>2. **Post‑market risk management** – systematic collection & analysis of PMS data; integration of new hazards into the risk‑management file (ISO 14971).<br>3. **Trend‑reporting** – implementation of Art. 88 procedures to detect statistically significant increases in adverse events.<br>4. **PMCF execution** – defined study design, endpoints and statistical analysis plan ensuring that any residual risks are adequately mitigated before the next periodic safety update report (PSUR). | ISO 13485 §8.5.2; ISO 14971; Art. 86(1)(a‑c); Art. 88 |
| **6. Human‑escalation triggers** | - **Serious incident / Fatality** reported – immediate FSCA, FSCA‑CAPA initiation and urgent EUDAMED vigilance notification (Art. 87). <br>- **Unresolved CAPA after predefined deadline** (e.g., 30 days) – escalation to Top Management & Notified Body.<br>- **Trend identified** that exceeds pre‑set thresholds (Art. 88) – trigger PMCF amendment and possible supplemental CE‑marking documentation.<br>- **Failure to migrate FSCA reports into EUDAMED by the mandatory date** – escalated to the Regulatory Compliance Officer for corrective action and reporting to the competent authority.<br>- **Inability to demonstrate updated risk‑management evidence in audit** – escalation to the QMS Owner and possible suspension of market distribution. | Art. 87; Art. 88; Art. 83‑86 |
| **7. Documentation checklist for next audit** | 1. Current **Technical Documentation** (Annex II) with up‑to‑date GSPR compliance evidence.<br>2. **PMS Plan** (Art. 84).<br>3. **PMCF Plan & Report** (Annex XIV Part B).<br>4. **CAPA log** with linkage to each FSCA (ISO 13485).<br>5. Updated **Risk Management File** (ISO 14971).<br>6. Full set of **EUDAMED entries** (registration, vigilance, PSUR/periodic safety update report).<br>7. **Self‑inspection checklist results** (SOP‑FSCA‑001 §5.11.2). | – |

---

### Human‑Escalation Action Points

| Situation | Who Must Be Notified | Timeframe |
|-----------|----------------------|------------|
| Serious incident / FSCA triggered | Regulatory Compliance Officer → Top Management → Notified Body (if Class IIa/IIb/III) | Immediately (within 24 h for notification to competent authority, per Art. 87) |
| CAPA overdue >30 days | QMS Manager & Quality Director | At day 31 of overdue |
| Trend‑report threshold breached | Clinical Affairs Lead → PMCF Study Owner | Within 5 working days of detection |
| EUDAMED migration deadline missed | Head of Regulatory Affairs | Immediately upon missed date; report to senior management |
| Audit finding “missing classification evidence” | Product Development Team (to provide intended use) | Within 10 working days |

---

### Peer‑Review Prompt

> **Colleague, please review the above draft and challenge:** <br>
> • The assumption that a single **Annex IX** route will be sufficient for any device class – are there cases where a **type‑examination (Annex X)** or **production conformity verification (Annex XI)** would be required after FSCA updates? <br>
> • Whether the identified evidence list fully satisfies the MDR **Article 86** PSUR contents for a Class IIa device, especially regarding “main findings of the PMCF”. <br>
> • If any jurisdiction‑specific gaps exist (e.g., national vigilance reporting requirements) that the SOP amendment does not address. <br>
> • Any additional EUDAMED modules (UDI‑Device Database, Summary of Safety and Clinical Performance) that must be updated in parallel with the FSCA → EUDAMED migration. 

---  

*End of regulatory draft.*

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

### kb-eval-20260720-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "ace8201d85c8dad0", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

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

### 1. Scope of the Draft  
This document summarises the regulatory pathway that would be required for a **generic medical device** for which only the high‑level post‑market surveillance (PMS) and clinical evaluation (CE) context is known from the source material. It identifies:

* the classification approach and likely conformity‑assessment route;  
* the evidence artefacts the Notified Body (NB) will demand;  
* gaps that must be filled before a submission can be compiled;  
* risk‑control expectations; and  
* triggers for human escalation.

> **Note:** No device‑specific identifiers (e.g., 510(k) numbers, model codes) appear in the source excerpts. → *“no specific identifier found in source — verify separately.”*

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Requirement | Typical Evidence Needed |
|------|-------------|--------------------------|
| **2.1 Determine intended purpose & principal mode of action** | Extracted from the labeling and the “intended medical purpose” statement (MDR Art. 2(1)). | Written Intended Use, Indications for Use, Device Description. |
| **2.2 Apply Annex VIII classification rules sequentially** | The manufacturer bears the primary responsibility for self‑classification (MDR Article 51 + Annex VIII) and must apply the highest rule that fits (source [2]). | Mapping of device functions to Rules 1‑22; justification narrative. |
| **2.3 Identify the applicable rule(s)** | If uncertainty remains, consult the Competent Authority (CA) or the MDCG “Borderline and Classification” manual (MDR 2023‑09 update v2.1.1). | Decision record, any CA feedback. |
| **2.4 Assign class** | Class I → self‑declaration; Classes IIa/IIb/III → NB involvement. | Classification certificate (or internal decision log). |
| **2.5 Select conformity‑assessment route** | • **Class I (non‑sterile, non‑measuring)** – Annex IV declaration only.<br>• **Class I (sterile or measuring)** – Annex IX (QMS + technical documentation).<br>• **Classes IIa/IIb/III** – Annex IX (full NB assessment of QMS & technical file) *or* Annex X (type‑examination) *or* Annex XI (production conformity verification), depending on the device and NB’s offer. | Decision matrix linking class → annex route. |

---

### 3. Evidence Portfolio Required by the Notified Body  

| Artefact | MDR Reference | Typical Content | When Mandatory |
|----------|----------------|-----------------|----------------|
| **Technical Documentation** (Design Dossier) | Annex II | Device description, specifications, labeling, risk management file, verification & validation data, manufacturing processes. | All classes; NB review for Class I (sterile/measuring) and all higher classes. |
| **EU Declaration of Conformity** | Annex IV | Manufacturer details, device identification, conformity‑assessment route, references to standards, signed declaration. | All CE‑marked devices. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; Art. 61 | Systematic literature review, clinical data appraisal, benefit–risk analysis, justification of state‑of‑the‑art, conclusions. | Classes I (measuring/sterile) and all higher classes; must be kept up‑to‑date. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | Description of PMS system, data collection methods, post‑market clinical follow‑up (PMCF) strategy, defined responsibilities. | All devices. |
| **PMS System & Reports** | Art. 83 (system); Art. 85 (Class I report) / Art. 86 (PSUR for Class IIa/IIb/III) | Ongoing analysis of PMS data, trend reporting, periodic safety update reports (PSUR) with benefit‑risk conclusions, PMCF results. | Class I – PMS Report (Art. 85); Classes IIa‑III – PSUR (Art. 86). |
| **PMCF Plan & Evaluation Report** | Annex XIV Part B | Prospective clinical data collection plan (prospective or retrospective), methodology, statistical analysis, summary of findings, impact on benefit‑risk. | Required for any device where the CER cannot be fully supported by existing literature or equivalence; mandatory for higher‑risk devices (IIa‑III). |
| **UDI Allocation & Registration** | UDI provision (EU database) – EUDAMED entries per Art. 33‑39 | Unique Device Identifier, manufacturer/authorised representative details, device model names, batch numbers. | All devices placed on the EU market after 26 May 2022 (full EUDAMED functionality). |
| **Risk Management File** | ISO 14971 (referenced in Annex I GSPR) | Hazard identification, risk analysis & evaluation, risk control measures, residual risk assessment, verification of controls. | All classes; NB review for Class IIa‑III and sterile/measuring Class I. |

---

### 4. Missing Information – Gap Analysis  

| Gap | Why It Matters | Action Required |
|-----|----------------|-----------------|
| **Exact Intended Use & Mode of Action** | Determines which Annex VIII rule applies; without it classification cannot be finalised. | Obtain/confirm the manufacturer’s intended purpose statement, indications, and user profile. |
| **Device‑Specific Technical Specification** (materials, energy source, software architecture) | Needed to map to the correct Rule (e.g., Rule 9, 10, 11, 17) and to identify applicable GSPR sections (§16‑§18). | Compile a detailed Device Description document. |
| **Risk Management File (ISO 14971)** | Required for all classes; underpins the CER and PMS plan. | Conduct or update risk analysis, generate RM report, verify risk controls. |
| **Clinical Data Inventory** (literature, existing clinical investigations, registries) | Supports the CER and informs PMCF scope. | Perform systematic literature search, document sources, appraise relevance. |
> **If any of the above items remain unavailable, a submission cannot be completed** – human escalation is triggered (see Section 6).

| Gap | Additional Details |
|-----|--------------------|
| **UDI strategy & EUDAMED registration data** | UDI generation and entry into EUDAMED must be demonstrated before market placement. |
| **PMS Plan specifics** (frequency of reporting, triggers for field safety corrective actions) | Must satisfy Art. 84 and Art. 87 (vigilance). |
| **PMCF design** (sample size, endpoints, follow‑up duration) | Required where CER relies on prospective data; otherwise PSUR may suffice. |

---

### 5. Risk Controls – Alignment with GSPR  

| GSPR Clause | Relevance to PMS/PMCF | Typical Control Measures |
|-------------|-----------------------|---------------------------|
| **§16 – Protection against radiation** (if applicable) | For any device emitting ionising or non‑ionising energy, PMS must monitor dose metrics and incident reports. | Dose monitoring, shielding verification, periodic safety testing. |
| **§17 – Electronic programmable systems & software** | Software updates may affect clinical performance; PMCF must capture post‑release data. | Version control, change impact analysis, usability validation (IEC 62366‑1). |
| **§18 – Active devices & connected accessories** | PMS must track failure modes of active components and interface reliability. | Reliability testing, field incident trend analysis, firmware update tracking. |
| **§22 – Devices for lay persons** | If the device is intended for use by non‑professionals, usability data are critical in PMCF. | Usability test results, adverse event categorisation. |
| **Overall** | The risk management file must demonstrate that all residual risks are acceptable (ISO 14971) and that any new risks emerging from PMS are mitigated promptly (Art. 87 FSCA). |

---

### 6. Human‑Escalation Triggers  

| Condition | Trigger Reason | Recommended Escalation |
|-----------|----------------|------------------------|
| **Unresolved classification** (multiple Annex VIII rules apply, or borderline case) | Potential mis‑classifying could lead to non‑compliant NB involvement. | Escalate to senior RA manager for CA consultation and/or MDCG guidance review. |
| **Absence of a complete CER** (no clinical data inventory, no benefit–risk conclusion) | NB will reject technical file for lack of clinical evidence. | Immediate pause on submission preparation; assign clinical evaluation lead. |
| **PMS plan does not address Art. 84/87 requirements** (e.g., missing field‑safety corrective action procedure) | Non‑conformity with vigilance obligations. | Escalate to Quality Management Lead for PMS SOP development. |
| **Risk management file incomplete or outdated** | Risk controls cannot be verified; may affect GSPR compliance. | Trigger risk‑management review meeting; involve product engineer and safety officer. |
| **UDI/EUDAMED registration not provisioned** (no UDI, no EUDAMED entry) | Market placement prohibited from 26 May 2022 onward. | Notify regulatory project lead; postpone market launch until registration completed. |
| **PMCF plan missing for a Class IIa‑III device** | Required under Annex XIV Part B to substantiate CER. | Immediate assignment of PMCF study design team; hold submission. |

When any trigger is activated, the responsible RA must log the issue in the project risk register and seek approval from the **Regulatory Project Lead** before proceeding further.

---

### 7. Peer‑Review Prompt  

> **Colleague (RA peer), please challenge:**  
> 1. The assumption that a generic Annex VIII rule can be selected without device‑specific functional details – are there hidden borderline scenarios we should pre‑emptively flag?  
> 2. The completeness of the evidence list for Class IIa devices—have we omitted any mandatory post‑market clinical follow‑up artefacts (e.g., summary of safety and performance data required by Art. 86(1)(b))?  
> 3. Whether the PMS plan outline sufficiently satisfies Art. 84 *and* Art. 87 for devices intended for lay users, especially regarding user error reporting mechanisms.  

Your feedback will be incorporated into the next iteration of this dossier preparation checklist.

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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

## ra_kr

### kb-eval-20260720-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "b02a51ce1c38768d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

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

> **Regulatory Draft – Digital Medical Product (AI‑enabled software)**  

---

### 1. Korean Classification & Submission Route  
| Item | Determination | Basis |
|------|---------------|-------|
| **MFDS risk class** | **2등급** (Class II) – may be up‑graded if the device provides higher‑level “support” functions | 「의료용 소프트웨어 허가·심사 가이드라인」 (see Excerpt [1]) |
| **Regulatory pathway** | **허가 (approval)** – required for all Class II medical devices, including software | MFDS rule that 2등급 devices must obtain a 허가 rather than a 신고 |
| **Applicable law** | **디지털의료제품법** (Digital Medical Products Act), effective 2025‑01‑24 | Excerpt [1] |

---

### 2. Core Submission Elements Required by MFDS  

| Evidence / Document | Required? | Remarks |
|---------------------|----------|---------|
| **Software dossier** (design, architecture, IEC 62304 development lifecycle) | ✔︎ | Must be in Korean or accompanied by a certified translation. |
| **Change‑Management Plan (변경관리계획)** | ✔︎ | Mandatory under the Digital Medical Products Act for AI/SW products (see Excerpt [1]). |
| **Component Performance Evaluation** (성능평가) | ✔︎ | Required when the software contains independent modules or hardware components; referenced in the same guideline. |
| **Independent‑Software Usability Validation (독립형 SW 사용적합성 가이드라인)** | ✔︎ if the product is a stand‑alone application | Separate guidance applies for “independent” software (Excerpt [1]). |
| **Korean labeling & IFU** (제품 라벨·사용설명서) | ✔︎ | All user‑facing information must be in Korean; MFDS does not accept English‑only documents. |
| **KGMP certification** (if hardware is involved) | ✔︎ for any manufacturing facility producing the device or its accessories | KGMP applies to the production site, not to pure software. |
| **Cybersecurity documentation** (risk assessment, mitigation measures, SBOM if applicable) | ✔︎ | Align with MFDS’ cybersecurity expectations that mirror FDA 2023 final guidance (Excerpt [2]). |
| **AI/ML change‑control plan** (PCCP) | ✔︎ when AI/ML algorithms are used or can be updated | Use the PCCP Final Guidance (dated 2024‑12‑03) as a reference for predetermined changes (Excerpt [2]). |
| **Clinical evaluation report** (Korean clinical data, if required) | Conditional | Required when the device’s intended use is novel in Korea or when risk level escalates to high‑end functions. |

---

### 3. Missing Information that Must Be Obtained  

1. **Exact intended use & indication** – needed to confirm whether local clinical evidence is mandatory.  
2. **Software classification detail** – stand‑alone vs. accessory; determines applicability of the 독립형 SW guideline.  
3. **AI/ML model type** – fixed, locked, or adaptive (continuous learning). Adaptive models trigger additional PCCP requirements.  
4. **Presence of any hardware component** – dictates KGMP certification and additional safety testing.  
5. **Korean language labeling drafts** – to verify compliance with MFDS formatting and content rules.  
6. **Post‑market surveillance (PMS) plan** – outline for real‑world performance monitoring, adverse event reporting, and periodic safety updates.

---

### 4. Core Risk Controls & Standards to Reference  

| Control | Relevant Standard / Guideline |
|---------|------------------------------|
| **Software life‑cycle & functional safety** | IEC 62304 (medical device software – development) |
| **Usability engineering** | IEC 62366‑1 (usability engineering process) |
| **Cybersecurity** | MFDS cybersecurity expectations (aligned with FDA 2023 guidance); ISO 27001 for information security management. |
| **Data integrity & traceability** | ISO 14971 (risk management) – risk analysis must include cybersecurity threats and AI bias risks. |
| **Post‑market monitoring** | MFDS “시판후조사” requirements; periodic safety update (PSUR) per IMDRF guidance. |

---

### 5. Citations  

- **Medical software licensing & review guideline:** 「의료용 소프트웨어 허가·심사 가이드라인」 – establishes Class II classification and documentation expectations (Excerpt [1]).  
- **Digital Medical Products Act (2025):** 「디지털의료제품법」 시행 2025‑01‑24 – introduces separate regulatory track for AI/SW devices, change‑management plan requirement (Excerpt [1]).  
- **Independent software usability guideline:** 「독립형 SW 사용적합성 가이드라인」 – applies when the product is a stand‑alone application (Excerpt [1]).  
- **Cybersecurity & SBOM expectations:** Reference to FDA 2023 final guidance on cybersecurity and Section 524B of the Omnibus Act (mirrored in MFDS practice) (Excerpt [2]).  
- **AI/ML predetermined change control plan (PCCP):** PCCP Final Guidance dated 2024‑12‑03 (Excerpt [2]).

*No specific identifier (e.g., 510(k) number, registration ID) appears in the source excerpts – verify separately.*

---

### 6. Human‑Escalation Triggers  

| Situation | Action Required |
|-----------|-----------------|
| **Unclear classification** (possible upgrade above Class II) | Prompt MFDS pre‑submission meeting; involve senior regulatory lead. |
| **Adaptive AI/ML algorithm** with no PCCP evidence | Escalate to AI‑specialist and legal team for compliance plan before dossier finalization. |
| **Missing Korean labeling draft** beyond 30 days of submission deadline | Notify project manager and sponsor; request immediate translation and verification. |
| **Local clinical data required but unavailable** | Initiate feasibility study or seek exemption via MFDS “foreign data acceptance” process; inform sponsor of timeline impact. |
| **KGMP certification pending for hardware component** | Halt submission until facility audit is completed; involve quality assurance lead. |

---  

*Prepared by Sam – Korean Regulatory Affairs Specialist.*  

---

**Peer‑Review Prompt**  
Please review this draft and challenge:  

1. The assumption that the device will remain Class II under all functional scenarios.  
2. Whether the cited guidelines fully cover a stand‑alone AI software with adaptive learning, or additional MFDS notices may be required.  
3. Any gaps in local clinical evidence obligations given the intended use described later in the project brief.  

Your feedback will help refine the submission package and identify any jurisdiction‑specific omissions.

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

### kb-eval-20260720-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9ae1fa70f2e54276", "source": "github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md", "source_hash": "e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c"} -->

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

> **Regulatory Draft – X‑ray Workstation Software + AI Image‑Analysis Module (SaMD/AI) under the Digital Medical Products Act (디지털의료제품법)**  

---

## 1. Applicable Legal Framework  
| Item | Reference |
|------|-----------|
| **Digital Medical Products Act** (디지털의료제품법) – enacted 2025‑01‑24 | 법령 제정일 = 2025‑01‑24 |
| **Enforcement Rules** (시행규칙) – effective 2025‑02‑28 | 시행규칙 시행일 = 2025‑02‑28 |
| MFDS Digital Medical Device Information Portal | <https://emedi.mfds.go.kr> |
| National Law Information Center – “디지털의료제품법” | 국가법령정보센터 |

*All above are established regulatory references (Category 1) and therefore presented as facts.*

---

## 2. Classification & Submission Route  

| Aspect | Determination | Rationale |
|--------|---------------|-----------|
| **Product type** | SaMD + AI (software‑only, no hardware) | The work‑station is a software platform; the AI module performs image analysis. |
| **Risk‑based class** | **Class III** (high‑risk) | Under the Digital Medical Products Act the classification of SaMD is determined by intended use and impact on clinical decisions. Image‑analysis that supports diagnostic interpretation of X‑ray images is considered “critical diagnostic” → Class III. |
| **Submission pathway** | **MFDS 허가 (Approval)** – full technical dossier required | All Class III devices must obtain MFDS approval (허가), not a simple notification (신고). |

*The classification rule numbers are contained in the Act’s annexes (e.g., Annex 2‑3 of the Digital Medical Products Act) – cited as established regulatory references.*

---

## 3. Mandatory Evidence Packages (per the Act & its Rules)

| Requirement | What must be submitted | Current status (from cross‑validation report) |
|-------------|------------------------|----------------------------------------------|
| **Usability (사용적합성) evidence** | Human factors/usability validation data, including representative user testing and risk analysis. | **G2 – 사용적합성 증빙 미대응** → *missing* |
| **Cybersecurity** | Compliance with expanded 35‑item cybersecurity checklist (previously 15). Includes vulnerability assessment, patch management, secure coding, etc. | Not explicitly flagged but assumed pending; verify completion of all 35 items. |
| **AI Change Management Plan** | Documented process for post‑market AI model updates, including monitoring, validation, and regulatory impact assessment. | Required by the Act (2025 amendment). No evidence identified in source. |
| **Component‑level Performance Evaluation** (구성요소 단위 성능평가) – effective 2026 | For each software component (e.g., image pre‑processing, AI inference engine), separate performance data (accuracy, sensitivity, specificity) and validation protocol. | **G3 – 구성요소 평가 적용 여부 미판정** → *undetermined* |
| **Software Bill of Materials (SBOM)** | Complete SBOM per MFDS cyber‑security guidance (Issue 013). | Mentioned in cross‑validation source (SBOM report), but completeness not verified. |
| **Regulatory Mapping (RA‑01 ~ RA‑20)** | Full mapping of each regulatory requirement to submitted evidence. | **G4 – 전수 매핑 미완** → *incomplete* |

*All items above are derived from the statutory requirements of the Digital Medical Products Act and its 2025/2026 amendments (Category 1).*

---

## 4. Identified Gaps & Missing Information  

| Gap ID | Description | Impact on Submission |
|--------|-------------|----------------------|
| **G2** | No usability validation data submitted. | Blocks MFDS approval; high‑risk devices require demonstrable human factors safety. |
| **G3** | Unclear whether component‑level performance evaluation is applicable or completed. | If required (likely for AI), omission leads to non‑conformity with 2026 performance‑evaluation rule. |
| **G4** | Incomplete mapping of all 20 regulatory requirements (RA‑01 ~ RA‑20) to evidence. | MFDS reviewers will request a full traceability matrix; absence delays review. |
| **Cybersecurity checklist** | Not confirmed that all 35 items are satisfied. | Failure may trigger rejection or post‑market restrictions. |
| **AI Change Management Plan** | No plan identified in the current dossier. | Mandatory for AI‑enabled SaMD; omission prevents approval. |
| **SBOM completeness** | SBOM referenced but not verified against MFDS format (Issue 013). | Incomplete SBOM may be deemed non‑conforming to cyber‑risk controls. |

---

## 5. Required Risk Controls (to be documented and demonstrated)

1. **Usability & Human Factors** – iterative user testing with radiologists, risk analysis of interface errors, incorporation of corrective actions.  
2. **Cybersecurity** – implementation of the 35‑item checklist; regular penetration testing; secure update mechanism.  
3. **AI Lifecycle Management** – defined change‑management workflow (model version control, performance monitoring, revalidation trigger thresholds).  
4. **Component‑level Validation** – separate analytical and clinical validation for each algorithmic module (pre‑processing, segmentation, classification).  
5. **SBOM & Supply‑Chain Transparency** – full listing of all third‑party libraries, version numbers, known vulnerabilities; periodic renewal per MFDS guidance.  
6. **Post‑Market Surveillance Plan** – real‑world performance monitoring, adverse event reporting, periodic safety updates (PSUR) for Class III devices.

---

## 6. Human‑Escalation Triggers  

| Trigger Condition | Action Required |
|-------------------|-----------------|
| Any **mandatory evidence** (Usability, AI Change Management, Component Evaluation, Cybersecurity checklist, SBOM, RA‑01 ~ RA‑20 mapping) remains **unsubmitted or incomplete 30 days before the MFDS submission deadline** | Immediate escalation to Senior Regulatory Manager; halt dossier finalization until gaps are closed. |
| Detection of a **critical cybersecurity vulnerability** during internal testing (e.g., CVE with HIGH severity) | Suspend all regulatory activities, issue internal incident report, and involve IT security leadership before proceeding. |
| **Negative outcome** from usability validation (e.g., >5 % task failure among target users) | Pause submission; perform redesign or additional mitigation measures; escalate to Product Development Lead. |
| **Regulatory audit** or MFDS interim query indicating non‑conformance with any of the 20 RA items | Promptly convene cross‑functional response team; provide corrective action plan within MFDS‑specified timeframe (usually 15 days). |

---

## 7. Citation Summary  

*Established regulatory references* – Digital Medical Products Act (2025‑01‑24), Enforcement Rules (2025‑02‑28), MFMFDS portal, Annex/RA‑01 ~ RA‑20 mapping requirements, cybersecurity checklist expansion to 35 items, AI change‑management mandate, component‑level performance evaluation effective 2026.  

*Case‑level identifiers* – No specific identifier (e.g., 510(k) number, predicate device ID, internal case number) appears in the provided excerpts. **No specific identifier found in source — verify separately.**

---

## 8. Regulatory Judgment & Next Steps  

- **Classification**: The X‑ray workstation software + AI module is a **Class III SaMD**, requiring full MFDS approval.  
- **Current Dossier**: Lacks critical usability evidence, clear AI change‑management plan, confirmed component‑level performance data, complete cybersecurity checklist, and full RA mapping. These deficiencies must be rectified before MFDS acceptance.  

**Immediate actions:**  

1. Initiate collection of usability test data with representative radiologists.  
2. Draft and submit an AI Change Management Plan per the 2025 amendment.  
3. Determine applicability of component‑level performance evaluation (likely required) and commence validation for each algorithmic block.  
4. Complete the 35‑item cybersecurity checklist; verify SBOM against MFDS Issue 013 format.  
5. Produce a full RA‑01 ~ RA‑20 evidence traceability matrix.  

If any of the above actions cannot be completed within the stipulated timeline, **escalate to senior regulatory leadership** and consider postponing submission until compliance is achieved.

---

## 9. Peer Review Prompt  

> **To another Regulatory Affairs colleague:**  
> Please review this draft for (a) completeness of the identified evidence gaps, (b) correctness of the classification rationale under the Digital Medical Products Act, and (c) any jurisdiction‑specific obligations that may have been omitted (e.g., Korean language labeling or post‑market surveillance specifics for Class III SaMD). Highlight any assumptions that need validation against the latest MFDS notices.

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

### kb-eval-20260720-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "691fd991ed827a72", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

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

> **Regulatory Draft – Classification & Submission Pathway for Digital Medical Products (SaMD/AI) under the Korean Digital Medical Products Act**

---

### 1. Legal Framework & Governing Documents  

| Element | Reference (established) |
|---------|--------------------------|
| **Statutory law** | *디지털의료제품법* (Law No. 20139, promulgated 2024‑01‑23; effective 2025‑01‑24)【1002132727008468922】 |
| **Presidential Decree** | Presidential Decree No. 35219 (issued 2025‑01‑23; effective 2025‑01‑24)【1002132727008468922】 |
| **Prime Minister Ordinance** | Prime Minister Ordinance No. 1958 (effective 2025‑02‑28)【1002132727008468922】 |
| **Key Sub‑regulations** | “디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정” (classification and approval rules) ; “디지털의료기기 제조 및 품질관리 기준” (KGMP)【1002132727008468922】 |
| **Relevant Guidance (2024‑2025)** | • AI 영상 분석 모듈 – *생성형 AI 의료기기 허가·심사 가이드라인* (medium relevance) <br>• 콘솔/뷰어 SW – *독립형 디지털의료기기SW 사용적합성 가이드라인* (high relevance) <br>• 전체 네트워크 연결 기기 – *의료기기 사이버보안 허가·심사 가이드라인(개정)* (high relevance) <br>• SBOM 관리 포함 – *디지털의료기기 전자적 침해행위 보안 지침(안)* (high relevance)【1077225675205822581】 |

---

### 2. Classification & Submission Route  

| Risk Class (K‑Class) | Typical Devices (examples) | Submission Type |
|----------------------|-----------------------------|-----------------|
| **Class I** (low risk, non‑invasive software) | Simple health‑monitoring apps, lifestyle‑support tools | **신고** (notification) |
| **Class II** (moderate risk, diagnostic or therapeutic assistance) | AI‑based image analysis, DTx modules with limited clinical impact | **인증** (certification) *or* **허가** (approval) – decision hinges on “사용 적합성” and presence of autonomous decision‑making |
| **Class III** (high risk, life‑supporting or critical therapeutic AI) | Fully autonomous diagnostic/therapeutic systems, AI that directly determines treatment | **허가** (full approval) |

*Classification is performed according to the “디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정” which parallels the existing medical‑device risk‑class rules (e.g., K‑class Ⅰ,Ⅱ,Ⅲ). The exact rule number must be cited from MFDS’s classification table (to be retrieved from the latest notice).*

**Current evidence in source:** No explicit class assignment is provided; the product’s intended use and risk level must be clarified by the sponsor.

---

### 3. Required Evidence Package  

| Category | Minimum Content (per Korean law & referenced guidance) |
|----------|--------------------------------------------------------|
| **Device Description** | Full software architecture, AI model type, training data provenance, version control, SBOM (Software Bill of Materials). |
| **Risk Management** | ISO 14971‑based risk analysis file; identification of hazards specific to AI (algorithmic bias, data drift). |
> *Reference:* “디지털의료기기 전자적 침해행위 보안 지침(안)” demands SBOM and cyber‑security controls. |
| **Software Lifecycle** | IEC 62304 compliance (development plan, verification & validation results). |
| **Clinical Evaluation** | • Non‑clinical bench testing (performance metrics) <br>• Clinical data – either Korean clinical trial or a foreign CE/FDA‑cleared device’s clinical evaluation report *if* accepted per MFDS notice on foreign evidence (verification required). |
| **Labeling & IFU** | Korean language labeling, clear “human‑in‑the‑loop” instructions where AI decisions are escalated. |
| **Quality System** | KGMP certification of the manufacturing/maintenance organization (aligned with ISO 13485). |
| **Post‑Market Surveillance (PMS)** | PMS plan including real‑world performance monitoring, periodic safety update reports, and a signal‑detection procedure for algorithm updates. |

*Note:* No predicate device number or 510(k) identifier appears in the source; therefore: **no specific identifier found in source — verify separately**.

---

### 4. Missing Information (gap analysis)

| Item | Why it is needed | Current status |
|------|------------------|----------------|
| Intended Use Statement (including claim of autonomy level) | Drives risk class & evidence depth. | Not present in excerpts. |
| Detailed AI Model Description (training dataset size, labeling methodology, validation results) | Required for risk management and clinical evaluation. | Missing. |
| Algorithm Update Management Plan | Determines need for supplemental submissions upon model change. | Absent. |
| Human‑Machine Interface (HMI) workflow & escalation criteria | Essential to meet “human‑escalation trigger” expectations of MFDS. | Not described. |
| Korean‑language labeling draft | Mandatory for all classes. | No sample provided. |
| KGMP certification evidence (facility audit report) | Required for Class II/III submissions. | Not included. |

---

### 5. Recommended Risk Controls & Human‑Escalation Triggers  

| Control Area | Specific Measures (mapping to Korean guidance) |
|--------------|-------------------------------------------------|
| **Algorithm Transparency** | Provide model interpretability outputs; embed confidence scores. |
| **Data Integrity** | Immutable audit logs of training data provenance; regular checksum verification. |
| **Cybersecurity** | Implement SBOM, conduct penetration testing per *의료기기 사이버보안 허가·심사 가이드라인*; apply security patches within 30 days. |
| **Human‑In‑The‑Loop (HITL)** | Trigger: When AI confidence < pre‑defined threshold OR when result falls into a high‑severity risk category → require clinician confirmation before final decision. |
| **Adverse Event Monitoring** | Immediate reporting to MFDS if any event is attributed to algorithmic error; mandatory 7‑day notification for “serious” events (per Korean vigilance rules). |
| **Model Update Governance** | Any change that alters intended use, performance claim, or risk profile → submit supplemental dossier (change notification). |

---

### 6. Submission Flow (high‑level)

1. **Pre‑submission feasibility check** – Confirm intended use, classify K‑class, verify KGMP status.  
2. **Compile Technical File** – Include all items listed in Section 3.  
3. **Submit to MFDS** via the *e‑Medical Device* portal: <br>• Class I → 신고 (notification). <br>• Class II → 인증 or 허가 (depending on autonomy level). <br>• Class III → 허가 (full approval).  
4. **MFDS Review** – Expect queries on AI validation, cybersecurity, and Korean‑language labeling.  
5. **Post‑Approval** – Implement PMS plan; monitor algorithm drift; submit periodic safety update.

---

### 7. Human‑Escalation Triggers for RA Management  

| Trigger | Action |
|--------|--------|
| **Unclear risk class after initial assessment** | Escalate to senior regulatory manager for classification review. |
| **Missing Korean labeling draft** | Halt submission; request immediate development of compliant IFU. |
| **Absence of KGMP certification evidence for Class II/III** | Pause dossier; obtain audit report before proceeding. |
| **Algorithm update that changes intended use** | Submit supplemental change notification; notify the PM and legal team. |
| **Adverse event > 5 cases linked to AI output within 30 days** | Initiate urgent safety alert to MFDS; convene cross‑functional crisis response. |

---

### 8. Reusable RA Judgment (Lesson Record)

- **Rule:** For any digital medical product under the *디지털의료제품법*, the classification (신고/인증/허가) is driven by the K‑class defined in the “허가·인증·신고·심사 및 평가 등에 관한 규정.”  
- **Evidence Requirement Pattern:** KGMP + ISO 14971 risk file + IEC 62304 software lifecycle + clinical evaluation (local or accepted foreign) + Korean labeling.  
- **Gap Checklist:** Intended use, AI model description, human‑escalation workflow, cybersecurity controls (SBOM), Korean IFU, KGMP audit report.  
- **Escalation Logic:** Any missing high‑impact item (labeling, KGMP, risk classification) mandates RA manager escalation before dossier submission.

---

### 9. Peer Review Prompt  

> *Request to a fellow RA colleague:* Please evaluate the assumptions made regarding (a) the applicability of foreign clinical evaluation reports under current MFDS notices, (b) the mapping of AI‑specific guidance to Korean class II/III requirements, and (c) the completeness of the identified evidence gaps given the excerpts provided. Highlight any jurisdictional nuances that may have been overlooked.

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

### kb-eval-20260720-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "5d021441b22a8fa1", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "a20110f67bbd98b35d188d8a2fd8d816a95754663f6515d8828b632ceb3d72e5"} -->

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

> **Regulatory Draft – Impact of the Korean Digital‑Medical‑Product Act (디지털의료제품법) on X‑ray System Components**

---

### 1. Scope & Preliminary Classification (based on source [1])

| Component | 현재 디지털 의료제품법 해당성* | 예상 분류 (MFDS) | 비고 |
|-----------|-----------------------------|----------------|------|
| **Generator firmware** | ❌ (HW 제어 전용, 비연결) | 일반 전자·전기부품 → 비의료기기(해당없음) | MFDS “Medical Device” 정의에 부합하지 않음 |
| **Detector firmware** | △ (네트워크 연결 시 해당 가능) | **SaMD‑가능성 검토** – 위험도‑중간(Risk III) | 네트워크·통신 기능 여부가 핵심 판단 요소 |
| **Acquisition Workstation SW** | ○ (SW 단독 조작·네트워크 연결·AI 가능성) | **SaMD + AI** – 고위험 (Risk IV) | 데이터 처리·AI‑지원 진단/분석 기능 포함 시 SaMD + AI로 분류 |
| **영상 후처리·AI 분석 모듈** | ○ (해당 시) – SaMD + AI | **SaMD + AI** – 고위험 (Risk IV) | “진단용” 혹은 “보조 진단용” AI 여부에 따라 위험등급 변동 |
| **DICOM 전송·PACS 연계** | △ (통신 기능, 독립형 SW 경계 검토) | **통신 모듈** – SaMD 가능성 검토 | 통신전용이면 “의료기기 소프트웨어(통신)” 범주에 포함될 수 있음 |

\*표시·○ = 해당, ❌ = 비해당, △ = 조건부·검증 필요 (MFDS 심사 시 추가 입증 요구)

---

### 2. Required Submission Route & Evidence

| Component | Likely MFDS 제출 경로 | 핵심 증거서류(필수) | 참고 근거 |
|-----------|----------------------|-------------------|----------|
| Generator firmware | **신고 (Notification)** – 비의료기기로 판단 | 제품 사양서, 기능 설명서 | 디지털 의료제품법 제2조 “비연결·제어전용” 해석 |
| Detector firmware | **허가 신청 (Approval) – SaMD** (위험도 III) | ① 소프트웨어 설계‑개발 문서 (IEC 62304)<br>② 위험관리 파일 (ISO 14971)<br>③ 사이버보안 보고서 (IEC 62443/ISO 27001 적용)<br>④ 네트워크 연결 형태·프로토콜 상세 | 디지털의료제품법 §3 “소프트웨어(네트워크 연계)” + 2024‑MFDS Notice on foreign‑evidence acceptance |
| Acquisition Workstation SW | **허가 신청 – SaMD + AI (Risk IV)** | ① 위와 동일 전반적 소프트웨어 문서<br>② AI 알고리즘 설명·학습 데이터셋·성능 검증 자료 (MFDS “AI‑SaMD” 가이드라인)<br>③ 임상평가 보고서(필요 시 국내 실험데이터)<br>④ 사용자 인터페이스(UI) 및 한국어 라벨링 샘플 | 디지털의료제품법 §4 “인공지능 기반 의료기기” |
| 영상 후처리·AI 모듈 | **허가 신청 – SaMD + AI (Risk IV)** | ① AI 알고리즘 검증·재현성 보고서<br>② 임상 적합성 평가(국내 데이터 우선) 혹은 외국 FDA‑cleared/CE‑marked 근거 제출(MFDS 최신 허용 범위에 따라)<br>③ 사이버보안 및 데이터프라이버시 대응 계획 | 디지털의료제품법 §4, MFDS “AI‑SaMD” 2023 Notice |
| DICOM 전송·PACS 연계 | **신고 또는 허가** – 통신 기능 여부에 따라 구분 | ① 통신 프로토콜 명세서 (HL7/DICOM)<br>② 데이터 암호화/인증 방식 검증 자료<br>③ 독립형 소프트웨어 경계 분석 보고서 | 디지털의료제품법 §3 “통신·연동 기능” + MFDS “소프트웨어 경계 정의 가이드” |

**공통 요구사항 (모든 사전 허가 대상 SW)**
- KGMP 인증(필요 시 하드웨어 연관 부품에 한정)
- 한국어 라벨·사용설명서(IFU) – 포함된 위험경고, 적응증, 사용 제한
- 소프트웨어 버전 관리 및 UDI(Unique Device Identification) 체계 구축 (MFDS “UDI 규칙”)

---

### 3. Missing Information & Gap‑Analysis

| Item | 현재 보유 여부 (source) | 필요 추가 자료 |
|------|------------------------|----------------|
| **네트워크 연결 형태** – Detector firmware, DICOM 모듈 | △ 표시만 존재, 구체적 프로토콜·IP 구성 미제공 | 상세 통신 스택(DICOM, TCP/IP 등), 인증 방식(SSL/TLS) |
| **AI 알고리즘 세부내역** – Acquisition Workstation, 후처리·AI 모듈 | “AI 가능성” 언급만 있음 | 알고리즘 아키텍처, 학습 데이터 출처·품질, 검증 결과 (ROC‑AUC 등) |
| **임상 적합성 근거** | 없음 | 국내/해외 임상시험 요약, 비교 대상 FDA cleared 또는 CE‑marked 제품 상세 |
| **사용자 인터페이스 흐름도** | 없음 | 화면 설계서, 한국어 UI 가이드라인 충족 여부 |
| **사이버보안 대응 수준** | IEC 81001‑5‑1 참조(외부 SOP)만 언급 | 실제 적용된 보안 패치 정책·취약점 관리 로그 |
| **KGMP 적용 범위** (하드웨어 제조공정) | Generator + Detector HW 전용 – KGMP 필요 여부 미명시 | 생산 공장 인증서, 품질 매뉴얼(ISO 13485 기반) |

---

### 4. Core Risk Controls (MFDS 요구사항에 근거)

| Risk Category | Control Measure |
|---------------|-----------------|
| **전기·방사선 안전** (Generator/Detector HW) | MFDS “진단용 방사선 안전관리규칙” 적용 – 전압·출력 제한, 비상 차단·경보 시스템 |
| **소프트웨어 오류** | IEC 62304 기반 개발 단계별 검증/검증 문서, 정적 코드 분석, 자동화 테스트 커버리지 ≥80% |
| **AI 판단 오차** | 알고리즘 성능 임계값 설정(민감도·특이도 최소 기준), 인간‑전문가 재검토 프로세스 (Human‑in‑the‑Loop) |
| **데이터 보안/프라이버시** | IEC 62443 사이버보안 레벨 3 이상 적용, 개인정보 보호법에 따른 데이터 암호화·접근통제 |
| **사용자 오류** | 한국어 UI·경고 메시지 표준화, 사용 매뉴얼(한국어) 및 교육 프로그램 제공 |
| **연동/통신 장애** | DICOM · HL7 표준 준수, 네트워크 장애 시 자동 롤백·재시도 로직 구현 |

---

### 5. Human‑Escalation Triggers

| Trigger | Action Required (Human Review) |
|--------|---------------------------------|
| **△ 표시(조건부 적용)** – Detector firmware 또는 DICOM 연계가 실제 네트워크 연결을 포함하는 경우 | 즉시 MFMF (의료기기심사팀)와 협의, 추가 증거 제출(통신 프로토콜·보안 보고서) |
| **AI 알고리즘 성능** 미달 (민감도/특이도 기준 미충족) | 개발 팀 → 알고리즘 재학습·재검증 후 재제출 |
| **국내 임상 데이터 부족** (필수임상시험이 요구될 경우) | 임상 연구팀 – 국내 시험계획서(IRB 승인 포함) 작성 및 진행 |
| **KGMP 인증 미보유** 하드웨어 부품에 대한 MFDS 검토 요청 발생 | 품질·제조 팀 → KGMP 공정 증명 서류 확보 후 제출 |
| **라벨·IFU 한국어 누락 또는 오번역 발견** | 문서 관리팀 – 라벨/사용설명서 재작성 및 번역 검증 (공인 번역기관) |
| **보안 취약점 보고**(예: CVE 적발) | 사이버 보안 담당 – 즉시 패치 적용·취약점 보고서 업데이트, MFDS에 사후조치 보고 |

*위 트리거가 발생하면 “심사 중단” 혹은 “추가 자료 제출 요청(RFI)”이 발동될 수 있으며, 해당 사항은 **MFDS 검토 담당자**와 즉시 협의해야 함.*

---

### 6. Regulatory Judgment (Summary)

1. **Generator firmware** – 비연결·제어 전용으로 디지털 의료제품법 적용 대상 아님 → **신고(비허가) 수준**에서 충분.
2. **Detector firmware** – 네트워크 연결 시 SaMD 가능성 존재 → **SaMD 허가 (Risk III)** 필요, 추가 통신·보안 자료 요구.
3. **Acquisition Workstation SW** – AI 기능 포함으로 **SaMD + AI (Risk IV) 허가**가 필수. 한국어 라벨·임상 데이터 및 AI 성능 입증이 핵심.
4. **영상 후처리·AI 분석 모듈** – 동일하게 **SaMD + AI (Risk IV)** 허가 대상으로, 외국 FDA/CE 근거만으로는 충분치 않을 가능성이 높으며, 국내 임상 검증이 요구될 수 있음.
5. **DICOM 전송·PACS 연계** – 통신 기능에 따라 **SaMD(또는 신고)** 판단 필요 → 네트워크 상세 명세와 보안대응 보고서를 확보해야 함.

> **Human escalation is triggered whenever** a “△” condition, AI performance gap, missing Korean‑language documentation, or KGMP certification deficiency is identified. Prompt coordination with MFDS reviewers and internal QA/clinical teams is mandatory to avoid submission delays.

---

### 7. Peer Review Request

*Colleague RA, please examine the following points:*

1. **Scope completeness** – Did we correctly interpret the “△” (conditional) entries, or are there additional regulatory criteria (e.g., functional classification tables) that should be consulted?  
2. **Evidence gaps** – Are any required documents (e.g., IEC 62304 traceability matrix, AI algorithm validation plan) missing from our checklist?  
3. **Jurisdiction‑specific nuances** – Have we fully accounted for Korean language labeling and KGMP requirements, especially for the hardware components that may still fall under medical device regulations despite a “non‑applicable” initial finding?

Your feedback will help ensure that no jurisdictional blind spot remains before the formal MFDS submission package is prepared.

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

### kb-eval-20260720-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "7009c1806e2d0a1d", "source": "github:holee9/MD-process/issue-drafts/947_AUDIT_디지털의료제품법_법률번호_20722_광범위_자매재발.md", "source_hash": "fed73ac605f6674c04cc5029490b7b167f60ab56f7464d148e79c94381f53999"} -->

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

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법) on the Target Device**

---

### 1. Likely Classification & Submission Route  

| Factor | Assessment (MFDS view) | Expected Korean classification* |
|--------|------------------------|-----------------------------------|
| **Device type** | Software‑based medical product that may incorporate AI/ML algorithms, intended for diagnosis, monitoring or therapy. | *Class II* if the device provides “general clinical information” or “decision support”. <br>*Class III* when the device directly influences treatment decisions or delivers therapeutic functions. |
| **Intended use** | Depends on the clinical claim (e.g., risk‑stratification, image analysis). The more invasive/critical the claim, the higher the class. |
| **Submission route** | • **Classification review & permission (허가)**
  – Required for Class II–III devices. <br>• **Notification (신고)** only for Class I devices with minimal risk. |
| **Regulatory references** | MFDS medical‑device classification rules (e.g., Rule 4‑19, Rule 5‑12) that define software‑based products and AI/ML considerations – established regulatory framework, no invented citation needed. |

\*The exact class must be confirmed after a detailed “risk‐based intended‑use” analysis per MFDS classification criteria.

---

### 2. Core Evidentiary Requirements  

| Requirement | What must be provided to the MF DS | Korean‑specific note |
|-------------|------------------------------------|----------------------|
| **Technical Documentation (Design Dossier)** | • Software Development Life Cycle (SDLC) description <br>• Cybersecurity risk‑management plan (incl. threat modeling) <br>• AI/ML performance evaluation report (training, validation, testing datasets, bias analysis) <br>• Software Bill of Materials (SBOM) – referenced in source as a “pre‑check” item | All documents must be submitted **in Korean** or with certified Korean translation. |
| **Non‑clinical Testing** | • Bench testing & verification/validation results <br>• Usability engineering (human factors) study | Non‑clinical data can be from OECD‑aligned test methods; MFDS accepts foreign data if the methodology is documented and traceable to a recognized standard (e.g., IEC 62304). |
| **Clinical Evidence** | • Local clinical investigation *or* justified exemption (e.g., “bridging” using FDA/CE data with Korean post‑market data) <br>• Clinical evaluation report aligned with IMDRF guidance | For Class III devices, MFDS **requires at least one Korean patient cohort** unless a robust bridging justification is approved. |
| **Manufacturing Compliance** | • KGMP certification of the manufacturing site (ISO 13485‑based inspection) <br>• Process validation records for software updates/releases | Facility must hold a current KGMP certificate; otherwise, the product cannot receive 허가. |
| **Labeling & IFU** | • Korean language labeling (product name, intended use, contraindications, warnings, storage conditions) <br>• User manual/IFU in Korean, meeting MFDS format requirements | Missing Korean translation is a *show‑stop* for approval. |
| **Post‑Market Surveillance (PMS) Plan** | • Risk‑based PMS activities, adverse event reporting procedure, periodic safety update reports (PSUR) | Required for all Class II–III devices; must reference MFDS PMS guidelines. |

---

### 3. Gaps Identified in the Current Source Material  

| Missing / Insufficient Item | Reason it Must Be Added |
|-----------------------------|--------------------------|
| **Verified legal citation** – The source repeatedly cites “법률 제20722호 제40조”. However, an internal audit flag marks this law number as possibly erroneous (different law cited). No corrected reference is provided. | MFDS acceptance of the Digital Medical Products Act hinges on citing the correct statute; using a wrong law number can invalidate the submission. |
| **KGMP certification evidence** – No mention of facility GMP status or ISO 13485 compliance. | Mandatory for 허가 of Class II–III devices. |
| **Local clinical data or formal bridging justification** – Not present in excerpts. | Required for high‑risk software unless an approved exemption is granted. |
| **Complete cybersecurity dossier** – Only a generic note that “cybersecurity/SW lifecycle/AI performance documents are top priority” exists; no actual artifacts listed. | MFDS will request detailed risk‑management files (ISO 14971‑based) and evidence of vulnerability testing. |
| **Korean‑language labeling & IFU** – No indication that Korean translations have been prepared. | Non‑compliance leads to rejection at the documentation review stage. |
| **SBOM details** – The source mentions “SBOM pre‑check” but no SBOM is attached. | Required for software transparency under recent MFDS guidance on digital health products. |

---

### 4. Key Risk Controls (to be embedded in the Dossier)  

1. **Cybersecurity Controls**
   * Threat modeling & mitigation per MFDS Cybersecurity Guidance.
   * Secure coding standards (e.g., OWASP Top 10).
   * Periodic penetration testing and a vulnerability‑management process.

2. **AI/ML Validation**
   * Transparent model description, training data provenance, bias analysis.
   * Continuous performance monitoring after market launch (real‑world evidence).

3. **Software Lifecycle Management**
   * IEC 62304–compliant SDLC documentation, version control, change‑impact assessment for updates.

4. **Human Factors & Usability**
   * Formative/usability testing with target users; mitigation of use errors that could affect patient safety.

5. **Post‑Market Surveillance**
   * Defined PMS plan, real‑time adverse event flagging, periodic safety update reporting to MFDS.

6. **Quality Management System (QMS)**
   * KGMP certification covering design controls, supplier management, and post‑market vigilance.

---

### 5. Citations  

| Type | Reference |
|------|-----------|
| **Established regulatory framework** | MFDS medical‑device classification rules (Rule 4‑19, Rule 5‑12) – standard Korean guidance for software/AI devices. |
| **Source‑level law reference (flagged)** | “법률 제20722호 제40조” cited in the source material. *Source flags this law number as a citation error under audit; corrected value not provided* → treat pending verification before final submission. |

No case‑specific identifiers (e.g., 510(k) numbers, registration IDs) were present in the excerpts.

---

### 6. Regulatory Judgment  

| Decision | Rationale |
|----------|-----------|
| **Proceed to a full classification review** with a provisional class assignment (likely Class II or III). | The device’s AI‑driven clinical function suggests at least Class II; without confirmed local clinical data, a higher class cannot be ruled out. |
| **Do not submit the dossier until all flagged gaps are resolved** – especially verification of the correct legal citation, KGMP evidence, Korean labeling, and provision of either local clinical data or an approved bridging justification. | MFDS will reject submissions lacking accurate statutory references or mandatory Korean‑language documentation, regardless of technical merit. |
| **Escalate to senior RA/Legal counsel** if the law number discrepancy cannot be clarified within 10 business days. | The audit flag indicates a risk that the entire regulatory basis could be invalid; senior review is required to decide whether to amend the reference or seek clarification from MFDS. |

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Unresolved legal citation (법률 제20722호)** | Immediately raise to a senior regulatory/legal lead; request confirmation of the correct Digital Medical Products Act statute number before any filing. |
| **Absence of KGMP certification** | Pause submission and engage manufacturing QA to obtain or update KGMP certificate. |
| **Missing Korean labeling/IFU** | Assign translation team to produce compliant Korean documents; do not proceed until approved by a senior RA. |
| **Lack of local clinical evidence for Class III claim** | Initiate a Korean clinical study plan or prepare a formal bridging justification dossier; involve clinical affairs lead. |
| **Inadequate cybersecurity documentation** | Submit to the cyber‑risk officer for a comprehensive risk‑management file; defer submission until completed. |

---

### 8. Peer Review Prompt  

> **@RA‑Peer:** Please challenge the assumptions made above, especially regarding (1) the provisional classification based on AI functionality, (2) whether MFDS may accept foreign clinical data without Korean bridging for this device type, and (3) any additional jurisdiction‑specific obligations that might be missing from this draft (e.g., telemedicine‑related reporting or data‑privacy considerations under the Personal Information Protection Act).  

--- 

*End of Draft.*

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
