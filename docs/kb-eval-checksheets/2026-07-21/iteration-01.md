# KB Eval Checksheet - 2026-07-21 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260721-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_us-001", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "fc3bfc38766e3c54", "source": "github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md", "source_hash": "19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf"} -->

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

> **Regulatory Draft – QMSR (21 CFR §820) Design‑Control Alignment**

---

### 1. Classification / Submission Route  
* **Device classification:** *Not determinable from the source material.* No device description or intended use is provided; therefore no FDA product code, class, or 510(k)/PMA pathway can be assigned at this stage.  
* **Regulatory implication:** The primary focus is internal compliance with the Quality Management System Regulation (QMSR) that will support any future 510(k) submission. The organization must first achieve full design‑control conformity before a substantive submission route can be selected.

---

### 2. Required Evidence of Compliance  

| Requirement | Evidence to Provide | Current Status (per source) |
|-------------|--------------------|----------------------------|
| **Design‑control reference** – incorporation by reference of ISO 13485:2016 §7.3 in place of the reserved 21 CFR §820.30 | • Updated SOP/FORM front‑matter showing “§820.10(c) → ISO 13485:2016 §7.3”<br>• Change‑control record documenting the amendment (audit #921, 2026‑06‑26) | Implemented for SOP‑AIGOV‑001; **residual citations** of §820.30 subsections remain across other SOPs/forms (identified by grep). |
| **Document control & traceability matrix** linking each design‑control activity to the governing regulation (ISO 13485:2016 §7.3) | • Master Design‑Control Matrix (inputs, outputs, verification, validation)<br>• Mapping table showing every document’s regulatory citation | Not yet demonstrated; matrix still references outdated §820.30 subsections. |
| **Risk Management file** per ISO 14971 (risk analysis, mitigation, residual risk evaluation) | • Risk Management Plan<br>• FMEAs and associated design‑control records | No evidence cited in source. |
| **Training records** confirming staff awareness of the new citation pathway (§820.10(c) → ISO 13485:2016 §7.3) | • Attendance logs, training materials, competency assessments | Not addressed in source. |
| **Internal audit report** post‑implementation confirming no remaining §820.30 citations | • Audit checklist results, corrective‑action log, final closure sign‑off | Audit #921 identified the issue; remediation incomplete. |

---

### 3. Missing Information / Gaps  

1. **Comprehensive inventory of all SOPs/forms** that still contain “§820.30” references (the source only flags “distributed residual citations”). A definitive list is required to plan corrective actions.  
2. **Evidence of redesign or re‑validation** for any design outputs that were originally justified under the now‑reserved §820.30. If those activities relied on the old citation, updated justification must be documented.  
3. **Verification that ISO 13485:2016 §7.3 incorporation** meets FDA expectations (e.g., that the referenced clause fully covers design‑control requirements). A cross‑walk mapping each design‑control element to the exact ISO text is advisable.  
4. **Risk‑control documentation** showing how the regulatory‑reference error could affect product safety/efficacy (e.g., potential for unverified design decisions).  
5. **Change‑Control Plan** (Predetermined Change Control Plan – PCCP) if any AI/ML components are involved; not mentioned in source but may be required for future submissions.

---

### 4. Risk Controls (to mitigate non‑conformity)

| Risk | Control Measure |
|------|-----------------|
| Use of outdated regulatory citations leads to FDA inspection findings | • Implement a **Citation Governance Procedure**: automated script verifies that every SOP/form cites only §820.10(c) or ISO 13485:2016 §7.3. |
| Design‑control activities performed under an invalid reference may produce undocumented design decisions | • Conduct **Design‑Control Re‑verification** for all open design projects, linking each activity to the updated citation. |
| Incomplete documentation hampers future 510(k) submission | • Establish a **Design‑Control Traceability Matrix** (inputs → outputs → verification/validation → regulatory reference). |
| Staff unaware of new reference pathway could re‑introduce §820.30 citations | • Mandatory **Regulatory Reference Training** and annual refresher; track completion in LMS. |
| Residual citations persist after remediation, leading to audit repeat findings | • Perform a **Post‑Remediation Audit** (independent QA) before final closure; any remaining §820.30 references trigger immediate escalation. |

---

### 5. Citations  

* **21 CFR §820.30** – Reserved (effective 2026‑02‑02).  
* **21 CFR §820.10(c)** – Design control requirements now incorporated by reference to ISO 13485:2016 §7.3.  
* **ISO 13485:2016, §7.3** – Design and development; incorporation by reference accepted by FDA for QMSR compliance.

*(All citations are established regulatory references; no case‑level identifiers appear in the source.)*

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Path |
|--------|-----------------|
| **Residual §820.30 citations** detected after the remediation script runs | Notify QA Manager → Senior Regulatory Affairs Director (within 1 business day). |
| **Design‑control verification gaps** (e.g., missing mapping to ISO 13485:2016 §7.3) | Raise a Corrective‑Action Request (CAR) to Engineering Lead; if not closed in 10 days, elevate to VP of R&D. |
| **Risk Management file absent or incomplete** for any active project | Immediate escalation to the Risk Management Team Lead and Chief Medical Officer. |
| **Training compliance < 90 %** for updated citation procedure | Report to HR Compliance Officer and halt release of new SOPs until remedied. |
| **Audit #921 closure not achieved within 30 days** of audit date (2026‑06‑26) | Formal escalation to the Executive Steering Committee, with a remediation plan and timeline. |

---

### 7. Judgment & Next Steps  

- **Judgment:** The organization has partially updated its design‑control regulatory reference but **has not achieved full QMSR alignment**; residual §820.30 citations remain, and supporting evidence (traceability matrix, risk files, training records) is missing. Until these gaps are closed, any future 510(k) submission would be at risk for non‑conformity findings.

- **Immediate actions:**  
  1. Generate a master list of all SOPs/forms containing “§820.30”.  
  2. Amend each document to reference only §820.10(c) → ISO 13485:2016 §7.3.  
  3. Populate and approve a Design‑Control Traceability Matrix.  
  4. Compile risk‑management documentation for all open design projects.  
  5. Conduct a post‑remediation internal audit; if any citation persists, trigger the escalation path above.

---

### 8. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions that (i) ISO 13485:2016 §7.3 fully satisfies FDA’s design‑control requirements in lieu of the reserved §820.30, and (ii) that a simple citation change alone suffices without re‑verification of prior design decisions. Identify any jurisdictional nuances (e.g., state‑specific medical device statutes) or additional documentation gaps not covered above.

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

1. Chunk `1123403925433224246`

> `00_프로젝트관리/문서_매트릭스.md` 의 §820.30 표기는 본 SOP/Form frontmatter에서 자동 생성되므로 위 frontmatter 정정 후 빌드 스크립트로 자동 갱신됨.

2. Chunk `152477499522968513`

> ## 배경 audit #921(2026-06-26) 종결 과정에서 SOP-AIGOV-001 frontmatter "FDA QMSR §820.30/ISO13485 §7.3"를 "§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30은 Reserved)"로 정정하였으나, **동일한 §820.30 subsection-letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스 전반에 분산 잔존**함을 grep 점검에서 확인. eCFR 21 CFR Part 820(QMSR, 2026-02-02 시행) §820.30은 본문 전체가 Reserved이고, 설계관리 요구는 §820.10(c)가 ISO 13485:2016 §7.3을 incorporation by reference로 끌어오는 단일 경로로 일원화되었다.

### kb-eval-20260721-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_us-002", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "0bd55d452ba8a1af", "source": "github:holee9/MD-process/issue-drafts/921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md", "source_hash": "36a0683dda1f189f95c3bba8f11be7917c7ed24fdf703b490573ae5ef6cf0b16"} -->

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

> **Regulatory Draft – QMSR & Design‑Control Readiness Assessment**

| Item | Judgment / Requirement | Regulatory Basis |
|------|------------------------|-------------------|
| **1. Classification & Submission Pathway** | No device‐specific 510(k) or PMA is implicated in the excerpt; the focus is on internal quality‑system compliance. Consequently, no pre‑market submission route is triggered at this stage. | 21 CFR §820 (Quality System Regulation) governs QMSR; classification decisions are made per 21 CFR §807 & device‑specific panels, which are absent from the source. |
| **2. Applicable Regulatory Text** | The organization must apply **FDA QMSR §820.10(c)** – “Incorporation by reference of ISO 13485:2016 §7.3” – and treat **§820.30** as *Reserved*. | 21 CFR §820.10(c) (effective Feb 2026) incorporates ISO 13485:2016 §7.3 for design‑control requirements; §820.30 is explicitly Reserved (no enforcement). |
| **3. Evidence of Compliance Needed** | • Updated SOP front‑matter showing the change from “FDA QMSR §820.30/ISO 13485 §7.3” to **“FDA QMSR §820.10(c) → ISO 13485:2016 §7.3”** (or “incorporation by reference”).  <br>• Revised SOP header/introduction containing a statement that *QMSR is applied under §820.30 Reserved and design‑control requirements are satisfied by ISO 13485 §7.3*.  <br>• Cross‑referenced sister SOPs (SOP‑DHF‑001, SOP‑DT‑001, SOP‑DVV‑001) demonstrating that all design‑management activities map to the incorporated ISO clause.  <br>• Traceability matrix linking design inputs/outputs, verification, validation, risk analysis, and DHF entries to ISO 13485 §7.3 requirements.  <br>• Change‑control records showing adherence to the **Predetermined Change Control Plan (PCCP)** if any AI/ML components are present. | • 21 CFR §820.10(c) – incorporation by reference.<br>• ISO 13485:2016 §7.3 – design and development planning, inputs, outputs, verification, validation, review, transfer.<br>• FDA Guidance on **Predetermined Change Control Plan (PCCP)** (Dec 2024) for AI/ML changes where applicable. |
| **4. Missing Information / Gaps** | 1. **Device scope** – Which FDA‑registered devices will be covered by the QMSR amendment?  <br>2. **UDI plan** – No reference to Part 830 labeling requirements; needed if new or revised devices are introduced.  <br>3. **Risk‑management integration** – Explicit linkage to ISO 14971 (risk analysis, controls) is not shown in the excerpt.  <br>4. **Verification of “Reserved” handling** – Confirmation that no process currently relies on §820.30; must be documented. | • Device‑specific sections of 21 CFR §892 (if imaging) or other panels would dictate additional submission obligations.<br>• 21 CFR §830.10 onward for UDI labeling.<br>• ISO 14971:2019 required for risk controls under QMSR. |
| **5. Core Risk Controls to Implement** | • **Design‑control procedures** meeting ISO 13485 §7.3 (design planning, inputs, outputs, review, verification, validation).  <br>• **Risk Management File** per ISO 14971, linked to design history file entries.  <br>• **Change‑Control System** with documented PCCP for AI/ML updates; otherwise standard change‑control per §820.30 (Reserved) but reflected in SOPs.  <br>• **Document Control & Record Retention** per §820.180–§820.210, ensuring all referenced SOPs and DHF records are immutable. | • ISO 13485:2016 §7.3.<br>• ISO 14971:2019.<br>• FDA QMSR §§820.30 (Reserved) & 820.10(c). |
| **6. Human‑Escalation Triggers** | • **Unresolved Reserved Section Issue:** If any process still cites §820.30 as operative, the QA Manager must raise a corrective action within 5 business days. <br>• **Missing Device Scope Definition:** Absence of a device list triggers an immediate review by Regulatory Affairs Lead before any submission is prepared. <br>• **UDI Gap Identified:** Discovery that upcoming devices lack UDI labeling plans escalates to the Compliance Officer for Part 830 implementation. <br>• **Risk‑Management Deficiency:** Any DHF entry lacking a linked risk control must be flagged to the Design Engineer and QA for remediation within 10 days. | Internal escalation policy; not directly codified but derived from QMSR expectations of timely corrective actions (21 CFR §820.100). |
| **7. Recommended Immediate Actions** | 1. Publish the revised SOP front‑matter and header language as described in excerpt [1]. <br>2. Conduct a scope‑definition workshop to list all devices under QMSR amendment. <br>3. Draft a UDI implementation plan (Part 830) for any new or modified devices. <br>4. Map existing DHF entries to ISO 13485 §7.3 and ISO 14971 controls; record gaps. | – |

---

**Peer‑Review Prompt**

*“@RA‑colleague, please review the assumptions above: (a) that no 510(k)/PMA pathway is required based solely on the QMSR amendment, (b) that incorporating ISO 13485 §7.3 via §820.10(c) fully satisfies FDA design‑control expectations, and (c) that the identified missing items (device scope, UDI plan, risk‑management linkage) capture all jurisdiction‑specific gaps for a 2026‑compliant QMSR program.”*

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

### kb-eval-20260721-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_us-003", "iteration": 1, "matched_keywords": ["PMA"], "profile_id": "ra-us", "scenario_id": "8240af1cbb85d72a", "source": "github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md", "source_hash": "ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd"} -->

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

> **Regulatory Draft – QMSR & Design‑Control Readiness for a PMA‑Targeted Device**

---

### 1. Classification / Submission Route  
- **Likely pathway:** Premarket Approval (PMA) – Class III device (the SOP title contains “PMA”).  
- **Regulatory basis:** 21 CFR §814 (PMA); QMS requirements governed by the new FDA Quality Management System Regulation (QMSR), 21 CFR §820, effective Feb 2026 and aligned with ISO 13485.  

> *No device‑specific identifier (e.g., 510(k) number or PMA reference) appears in the source – verify separately.*

---

### 2. Evidence Required to Satisfy QMSR & Design‑Control

| Element | What must be submitted / retained | Relevant regulatory citation |
|---------|-----------------------------------|------------------------------|
| **Quality System Documentation** | Fully implemented ISO 13485‑aligned QMS (procedures, work instructions) covering design, purchasing, manufacturing, inspection, service, PMS, CAPA, training, document control. | 21 CFR §820; EU MDR Art.10(9)(j) |
| **Process‑Monitoring KPI Matrix** | Complete set of KPIs for the nine core processes (design, purchase, manufacture, inspection, service, PMS, CAPA, education, documentation). Each KPI must include: metric, frequency, threshold, owner, data‑collection method, statistical technique (e.g., SPC), and linkage to corrective actions. | 21 CFR §820.250 (use of statistical techniques) |
| **Statistical Analysis Plan** | Detailed SOPs describing the use of Statistical Process Control, Pareto analysis, Ishikawa (cause‑and‑effect) diagrams for trend detection and CAPA triggering. | 21 CFR §820.250 |
| **CAPA Records** | Documented root‑cause analyses, corrective/ preventive actions, verification of effectiveness, and closure loop tying KPI breaches to CAPA initiation per §8.2.5 and §820.100 (CAPA). | 21 CFR §820.100; ISO 13485 §8.2.5 |
| **Management Review (MR) Minutes** | Records demonstrating that MR integrates KPI trends, CAPA status, resource reallocation decisions, and effectiveness of quality objectives per §8.5.1. | 21 CFR §820.20 (Management Review); ISO 13485 §8.5.1 |
| **Risk Management File** | ISO 14971‑based risk analysis (FMEA/FMECA), risk control measures, and post‑market surveillance plans linked to KPI outcomes. | ISO 14971; FDA guidance on Risk Management for PMA |
| **Design History File (DHF) / Device Master Record (DMR)** | Complete design input/outputs, verification & validation reports, traceability matrices, software documentation (if applicable), and any Predetermined Change Control Plan (PCCP) if AI/ML functions are present. | 21 CFR §820.30 (Design Controls); FDA “Predetermined Change Control Plan” guidance Dec‑2024 |

---

### 3. Missing Information – Gaps to Fill Before Submission  

| Gap | Why it matters |
|-----|----------------|
| **Specific device description & intended use** | Required to determine classification, predicate analysis, and performance testing scope. |
| **Risk classification (ISO 14971 severity/likelihood)** | Needed for risk control justification and PMA safety/effectiveness narrative. |
| **Performance / Bench‑test data** | Essential for demonstrating substantial equivalence of function (for PMA: effectiveness & safety). |
| **Clinical data plan or results** | PMA generally requires clinical evidence; absent in the excerpt. |
| **UDI strategy (labeling, GUDID submission)** | Must meet 21 CFR §830 requirements before market entry. |
| **Software documentation (if software‑driven) & AI/ML change‑control plan** | Required under QMSR §820.* and FDA’s PCCP guidance if applicable. |
| **EU MDR post‑market surveillance (PMS) plan** | If marketed in EU, Art.10(9)(j) compliance must be demonstrated. |

*All above items are not addressed in the source excerpt – verify separately.*

---

### 4. Risk Controls Embedded in the SOP  

1. **Statistical Monitoring (SPC)** – early detection of process drift → triggers CAPA before patient impact.  
2. **CAPA Trigger Thresholds** – defined KPI limits create deterministic trigger points, minimizing ambiguity.  
3. **Management Review Loop** – ensures top‑down oversight and resource reallocation to address systemic risks.  
4. **Linkage to MR Effectiveness Measures** – closed‑loop verification of corrective actions per ISO 13485 §8.5.1.  

*Additional FDA‑required controls (e.g., design validation, device safety testing) remain outside the SOP’s scope and must be supplied elsewhere.*

---

### 5. Citations (Established Regulatory References)

- **21 CFR §820.100** – Corrective and Preventive Action (CAPA) system.  
- **21 CFR §820.250** – Use of statistical techniques for process control.  
- **21 CFR §820.20** – Management Review requirements.  
- **21 CFR §820.30** – Design Control requirements (relevant to DHF/DMR).  
- **21 CFR §814** – Premarket Approval (PMA) pathway.  
- **EU MDR Art.10(9)(j)** – Post‑market surveillance and quality system obligations.  
- **ISO 13485:2016 §8.1, §8.2.5, §8.5.1** – Corresponding clauses for monitoring, CAPA, and management review (as mapped in source).  

*No case‑level identifiers (e.g., 510(k) numbers) appear in the provided excerpts – verify separately.*

---

### 6. Human‑Escalation Triggers

| Trigger | Action |
|--------|--------|
| **KPI breach exceeding defined threshold** | Immediate CAPA initiation; notify Quality Manager and Project Lead. |
| **Failure to close CAPA within predefined time window** | Escalate to Director of Regulatory Affairs / senior management. |
| **Inadequate data collection or statistical analysis method not validated** | Halt submission preparation; require QMS audit and corrective action. |
| **Missing any of the evidence items listed in Section 2** | Pause PMA filing; schedule cross‑functional review before proceeding. |
| **Regulatory inspection finding a non‑conformance with QMSR §§820.* or ISO 13485** | Activate containment, root‑cause analysis, and full‑scale corrective plan; report to FDA as required under 21 CFR §820.100/803. |

---

### 7. Peer‑Review Prompt  

> **@RA‑Peer:** Please challenge the assumptions that (a) the SOP is intended exclusively for a PMA‐type device, (b) the KPI matrix alone satisfies QMSR statistical technique requirements, and (c) the listed citations fully cover all regulatory gaps for an EU MDR submission. Identify any jurisdiction‑specific elements we may have omitted or mis‑interpreted.

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

1. Chunk `1039190717614682920`

> ## 갭 내용 | 조항 | 요구사항 | 현재 상태 | |------|----------|-----------| | §8.1 | 적합성·효과성·개선 모니터링·분석·개선 계획 | partial | | §8.2.5 | 프로세스 성과 모니터링·미달 시 CAPA 트리거 | partial | | §8.5.1 | 품질정책·목표·감사·분석·시정·MR 통한 효과성 개선 | partial |

2. Chunk `611272139046336025`

> ## Definition of Done - [ ] `02_품질경영시스템_QMS/SOP-PMA-001_프로세스_모니터링_분석_절차.md` 신규 (v0.1) - 프로세스 카탈로그(설계·구매·제조·검사·서비스·PMS·CAPA·교육·문서) — 9개 - KPI 매트릭스(프로세스 × 측정지표 × 주기 × 임계치 × 소유자) — 정량 - 데이터 수집·분석 방법(통계기법: SPC·Pareto·Ishikawa) - 미달 시 트리거(CAPA·MR 입력·자원 재배치) 폐쇄루프 - §8.5.1 효과성 측정 연계(품질목표→KPI→MR) - [ ] `02_품질경영시스템_QMS/F-PMA-001_KPI_매트릭스.md` 신규 — 27개 셀(9프로세스×3차원) - [ ] CHK-ISO13485-001 ISO-8.1/8.2.5/8.5.1 `status: met` 갱신 - [ ] SOP-MR-001/SOP-CAPA-001/F-MR-001 정합성 — KPI ↔ MR 입력 ↔ CAPA 트리거 - [ ] 규제 매핑: ISO 13485 §8.1/8.2.5/8.5.1, FDA QMSR §820.250(통계기법)·§820.100(CAPA), EU MDR Art.10(9)(j) - [ ] 적대적 자기검토(심사관 모드)

### kb-eval-20260721-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "df75bd468a439495", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

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

> **Regulatory Draft – X‑ray Imaging System (2026 QMSR Readiness)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|---------------|
| **Product type** | X‑ray diagnostic imaging system (hardware + associated software) |
| **CFR Part** | **Part 892 – Radiology / Imaging Devices** (radiation‑emitting equipment) |
| **Class** | **Class II** (most general‑purpose X‑ray systems are classified II with special controls; confirm against the FDA product classification database) |
| **Premarket pathway** | 510(k) – Traditional or Special 510(k) (if design changes are limited to previously cleared features). A De Novo is not required unless no predicate exists. |

*Citation*: Part 892 governs X‑ray imaging devices (FDA “Radiology / imaging devices” mapping).

---

### 2. Applicable Regulatory Requirements  

| Area | Core Requirement | FDA Reference |
|------|------------------|---------------|
| **Quality Management System** | Full QMS complying with the new **QMSR** (21 CFR 820) – includes all ISO 13485:2016 elements **plus** additional record‑keeping obligations from §820.35. | 21 CFR 820; **§820.35** (record management) |
| **Design Controls** | Design Input, Output, Review, Verification, Validation, Transfer, and Change Management per §820.30. | 21 CFR 820.30 |
| **Risk Management** | Hazard analysis (FMEA/FMECA), risk control implementation, residual risk evaluation; must be documented in the design history file (DHF). | 21 CFR 820.30(b) & FDA guidance on “Medical Device Design‑Control Guidance” |
| **Software (if any)** | Validation per §820.70, compliance with 21 CFR Part 11 for electronic records, and if AI/ML features are present – a Predetermined Change Control Plan (PCCP). | 21 CFR 820.70; **Predetermined Change Control Plan (PCCP)** guidance Dec‑2024 |
| **UDI** | Assign a UDI per Part 830; label must bear the UDI and be submitted to GUDID. | 21 CFR §830.10–§830.60 |
| **Medical Device Reporting (MDR)** | Establish procedures for adverse event reporting. | 21 CFR 803 |
| **Labeling** | Conform to §801 labeling requirements, including intended use, contraindications, and radiation safety information. | 21 CFR 801 |

---

### 3. Evidence Required for 510(k) Submission  

1. **Device Description & Intended Use Statement** – clear, concise narrative.  
2. **Predicate Comparison Table** – side‑by‑side comparison of technological characteristics, performance testing, and labeling with the selected predicate (e.g., K1234567). *No specific identifier found in source – verify separately.*  
3. **Performance Testing** – 
   - Electrical safety (IEC 60601‑1)  
   - Radiation output & beam quality (ANSI ASHRAE standards)  
   - Image quality metrics (MTF, DQE)  
4. **Software Validation Report** (if software present).  
5. **Design History File (DHF)** – includes design inputs/outputs, verification/validation protocols & reports, risk analysis (FMEA), and traceability matrix.  
6. **QMS Documentation** – 
   - Copy of the QMS manual showing incorporation of ISO 13485:2016 **§4.2.5** *and* additional controls required by **§820.35** (record‑management procedures, audit logs).  
   - SOPs referenced in the source (e.g., F‑QMSR‑REC‑001).  
7. **UDI Assignment Package** – label artwork, device identifier, packaging diagram.  
8. **MDR & PSUR Procedures** – copies of SOPs for adverse event handling and periodic safety updates.  

---

### 4. Gaps / Missing Information (as identified from source)  

| Gap | Why it matters | Suggested action |
|-----|----------------|-----------------|
| **Explicit mapping of ISO 13485 §4.2.5 to FDA §820.35** – the source notes a “difference table” but does not provide the completed table. | Demonstrates compliance with added U.S. record‑keeping requirements (e.g., retention periods, electronic audit trails). | Complete the difference matrix; embed it in the QMS manual and attach as an appendix to the 510(k). |
| **Design Control Evidence** – no mention of design verification/validation protocols, risk analysis artifacts, or traceability matrices. | Required by §820.30 for Class II devices. | Generate and archive the DHF elements; ensure they are cross‑referenced in the submission. |
| **UDI Implementation Plan** – source lists Part 830 applicability but no concrete UDI assignment details. | Mandatory for market entry after Feb 2026 QMSR effective date. | Draft a UDI labeling plan, submit registration to GUDID, and attach proof of label compliance. |
| **Software Pre‑market Validation** (if software present) – absence of Part 11 compliance evidence and potential PCCP. | Needed for any electronic records or AI/ML functions. | Conduct 21 CFR Part 11 validation; develop a Predetermined Change Control Plan if applicable. |
| **Predicate Device Confirmation** – no predicate identifier supplied in the source excerpt. | Essential to justify substantial equivalence. | Perform a market search, select an FDA‑cleared X‑ray system of similar indications, and document the comparison. |

---

### 5. Risk Controls & Mitigation (aligned with QMSR)  

| Control | Description | Regulatory Basis |
|---------|-------------|------------------|
| **Risk Management File** – FMEA/FMECA covering radiation exposure, electrical hazards, software failures. | Documents hazard identification, severity/occurrence ratings, and mitigations. | 21 CFR 820.30(b); ISO 14971 (incorporated by reference). |
| **Design Verification/Validation Protocols** – test plans with acceptance criteria for both hardware and software. | Ensures design outputs meet inputs and intended use. | §820.30(c) & (d). |
| **Change Control Process** – documented change evaluation, impact analysis, and PCCP (if AI/ML). | Controls post‑market modifications without additional submissions. | **Predetermined Change Control Plan (PCCP)** guidance Dec 2024; §820.30(e). |
| **Record Retention & Traceability** – electronic QMS with audit trails satisfying §820.35 and ISO 13485 §4.2.5. | Guarantees integrity of design history, complaints, and adverse event records. | §820.35 (additional to ISO 13485 §4.2.5). |
| **Training & Competency** – SOP‑based training logs for personnel handling radiation safety and QMS activities. | Demonstrates staff qualification. | §820.25 (training). |

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required | Escalation Level |
|---------|-----------------|------------------|
| **Missing or incomplete DHF elements** (e.g., absent design verification report) | Pause submission; assign to Design Engineer & QA for completion. | RA Lead → Senior Management if not resolved within 2 weeks. |
| **Failure to map ISO 13485 §4.2.5 to FDA §820.35** | Require QMS specialist to finalize the difference matrix and update SOP‑F‑QMSR‑REC‑001. | QA Manager → Regulatory Affairs Director. |
| **UDI non‑compliance (label missing UDI or GUDID registration incomplete)** | Suspend product release; engage labeling team for corrective action. | Labeling Lead → VP of Regulatory Operations. |
| **Unresolved predicate comparison** (no clear cleared device) | Conduct new predicate search, possibly consider De Novo pathway. | RA Manager → Head of Regulatory Strategy. |
| **Significant residual risk identified in FMEA that exceeds acceptable level** | Initiate risk mitigation plan; may require redesign or enhanced safety testing. | Risk Management Lead → Chief Clinical Officer. |
| **Regulatory guidance updates (e.g., new PCCP requirements) after submission filing** | Review impact; submit post‑market supplement if needed. | Regulatory Affairs Team → FDA liaison. |

---

### 7. Summary Judgment  

- The X‑ray imaging system is a **Class II device governed by 21 CFR Part 892**, requiring a **traditional 510(k) submission** with a well‑documented design history file.
- Compliance must satisfy **both ISO 13485:2016 §4.2.5** and the **enhanced FDA QMSR record‑keeping in §820.35**; meeting only the ISO baseline is insufficient (source excerpt 1).
- The current documentation set described in the source lacks concrete evidence of design controls, predicate comparison, UDI implementation, and the detailed difference matrix between ISO 13485 and FDA requirements.
- Addressing these gaps, completing the QMSR‑specific records, and establishing the risk management artifacts will render the submission **regulatory‑ready**.

*Human escalation is triggered whenever any of the above gaps persist or when new regulatory changes arise before filing.*

---

### 8. Peer Review Prompt  

> *Please review this draft for (a) completeness of the QMSR vs. ISO 13485 gap analysis, (b) adequacy of identified missing evidence relative to FDA 510(k) expectations, and (c) any jurisdiction‑specific considerations that may have been omitted (e.g., state radiation licensing, export controls).*

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

### kb-eval-20260721-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_us-005", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "514c6cfbfba3b17c", "source": "github:holee9/MD-process/issue-drafts/972_AUDIT_검사개요_QMSR_미존재_820_70i_820_180c_잔존.md", "source_hash": "68137c31d0bd41666dcdfd9887be904b6e42d861b4e11f275b302ff1f96e9b5f"} -->

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

---

### 1. Likely Regulatory Classification / Submission Pathway  

| Device Context (assumed) | Typical FDA Class* | Preferred Premarket Path |
|--------------------------|--------------------|---------------------------|
| Moderate‑risk medical device (e.g., imaging software, diagnostic hardware) | **Class II** – regulated under 21 CFR 820 (QMSR) and subject to general controls plus special controls. | **510(k) Premarket Notification** (substantial equivalence). |
| Novel / high‑risk technology with no predicate | Class III or novel Class II | **De Novo Classification Request** (if no predicate) or **PMA** for Class III. |

\*If the device is a low‑risk Class I exempt, QMSR does not apply; otherwise QMSR is mandatory.

---

### 2. Core Regulatory Requirements – Evidence Checklist  

| Requirement | What to Submit / Demonstrate | CFR/Standard Reference |
|-------------|------------------------------|------------------------|
| **QMS Scope & Structure** | Fully implemented QMS covering §§ 820.1, 820.3, 820.7, 820.10, 820.35, 820.45. Documented policies, procedures, and responsibilities. | 21 CFR 820.1‑820.45 (current sections) |
| **Design Control** | Design & Development Plan; Design History File (DHF) with design inputs, outputs, verification, validation, risk management files. | 21 CFR 820.30 (reserved – not required); see ISO 13485:2016 §4.1.6 as the current basis for design control evidence. |
| **Software Validation** | Validation of any automated manufacturing or process software per **ISO 13485:2016 §4.1.6** (since §820.70(i) is no longer in effect). Include validation protocol, test data, and acceptance criteria. | ISO 13485:2016 §4.1.6 |
| **Record‑Keeping** | Device Master Record (DMR), Device History Record (DHR), and all required production records. Note that **§820.180** has been removed; therefore no “record” clause exists under that number. | 21 CFR 820.180 (deleted) – use current QMSR record‑keeping provisions in §§ 820.70‑820.100. |
| **Risk Management** | ISO 14971:2019 risk analysis, mitigation, and residual risk evaluation integrated into DHF. Include post‑market surveillance plan if required. | ISO 14971:2019 |
| **UDI Implementation** | Label & packaging must contain a UDI; device listing in GUDID as per 21 CFR 830.10 onward. | 21 CFR 830.10‑830.60 |
| **Training & Competency** | Documentation of personnel training for QMS processes, software use, and GMP practices. | 21 CFR 820.25 (training) |

---

### 3. Gaps Identified in Source Materials  

| Missing / Inaccurate Element | Impact on Submission | Immediate Action |
|------------------------------|----------------------|------------------|
| **§820.70(i) & §820.180 cited as current** – both are obsolete (removed from QMSR). | Misleading compliance statements; could trigger FDA “non‑conformity” during audit. | Remove or re‑frame these references; replace with ISO 13485:2016 software validation requirements. |
| **Reserved Sections (820.5, 820.20‑30, 820.40, Subparts C‑O)** listed as active. | Over‑documentation of non‑existent controls; risk of audit findings for “unnecessary” procedures. | Clarify that these sections are reserved and not applicable; focus on the six active §§ noted above. |
| **No evidence of implementation of ISO 13485:2016 §4.1.6** (IBR via §§ 820.7/ 820.10). | Design‑control compliance cannot be demonstrated. | Prepare a cross‑walk showing how QMS processes satisfy ISO 13485:2016 requirements. |
| **Audit findings #951, #967 referencing “04 카테고리 820.x 전수 오귀속”** – indicates uncategorized residues of obsolete clauses. | Indicates lingering legacy documentation that may be challenged as non‑conformant. | Conduct a *gap‑closure* review to purge or reclassify any residual references to deleted sections. |
| **Lack of explicit DHF/DMR linkage** in the excerpt. | Insufficient design history for 510(k) substantive review. | Compile and hyperlink all design documents, verification/validation reports, risk analysis, and labeling artifacts into a complete DHF. |

---

### 4. Risk Controls – Design‑Control Perspective  

| Control | Application |
|---------|-------------|
| **Design Input Verification** | Ensure inputs trace to user needs & intended use; link to risk control measures (ISO 14971). |
| **Design Output Validation** | Perform end‑to‑end validation in simulated/clinical environment; document acceptance criteria. |
| **Change Management** | Adopt a *Predetermined Change Control Plan (PCCP)* for AI/ML updates (FDA Guidance Dec 2024) where relevant. |
| **Software Lifecycle** | Follow IEC 62304 (if software‑intensive) in conjunction with ISO 13485:2016 validation requirements. |
| **Manufacturing Process Validation** | For automated processes, execute process qualification (IQ/OQ/PQ) and maintain records per current QMSR. |

---

### 5. Human‑Escalation Triggers  

| Situation | Who Must Be Notified / Action |
|-----------|------------------------------|
| **Discovery of obsolete CFR citations (e.g., §§ 820.70(i), 820.180)** | Senior QA Manager – initiate corrective action plan within 10 business days. |
| **Incomplete DHF or missing risk analysis** | Project Lead & Regulatory Affairs Director – hold a design‑control review meeting; pause submission until resolved. |
> **Regulatory Decision:** *Assuming the device is Class II, a 510(k) pathway is appropriate. Current QMSR evidence is incomplete due to outdated section citations and absent ISO 13485:2016 cross‑walks. The firm must (1) purge references to deleted CFR sections, (2) document software validation per ISO 13485, (3) assemble a complete DHF/DVR package, and (4) verify UDI compliance before filing.*  

If any of the above gaps remain after 30 days, **escalate to Deputy Director of Regulatory Affairs** for risk‑based decision on whether to defer submission.

---

### 6. Peer‑Review Prompt  

> **To:** RA Team – please challenge the assumptions made in this draft:  
> - Is the classification inference (Class II) appropriate without a defined intended use?  
> - Have we captured all current QMSR sections that may affect design control (e.g., any post‑Feb 2026 amendments)?  
> - Are there jurisdiction‑specific considerations (e.g., state‑level reporting, EU MDR equivalence) that need inclusion for a global submission strategy?  

Please provide comments or additional evidence requirements.

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

### kb-eval-20260721-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b72e0247925ae150", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

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

> **PMS & PMCF Planning – X‑ray Detector (Class IIa), Handheld X‑ray Source (Class IIb) and GUI SaMD (Class IIa)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Device | MDR Rule (Annex VIII) | Class | Evidence required for classification | Typical conformity‑assessment route |
|--------|----------------------|-------|---------------------------------------|-------------------------------------|
| X‑ray detector (image‑recording component) | **Rule 17** – devices specifically intended for recording diagnostic images generated by X‑ray radiation | **IIa** | Confirmation that the intended purpose is “recording/producing a diagnostic image” and that no therapeutic function is claimed. | **Annex IX** – assessment of quality‑management system + technical documentation (including CER, RMF). |
| Handheld X‑ray source (emits ionising radiation for diagnosis) | **Rule 10** – active devices that emit ionising radiation for diagnostic radiology | **IIb** | Demonstration of intended diagnostic use, emitted radiation characteristics and safety controls. | **Annex IX** (full device) – QMS + technical documentation; a type‑examination (Annex X) may be used for the X‑ray source component if supplied separately. |
| GUI software (SaMD that provides diagnostic information) | **Rule 11** – software providing information used for diagnostic decisions, with no life‑threatening impact expected | **IIa** | Intended purpose described as “providing image display and interpretation support”. | **Annex IX** – QMS + technical documentation; software‑specific modules (IEC 62304, IEC 62366) are part of the TD. |

*All classifications cite **Annex VIII** of MDR 2017/745.*

---

### 2. Post‑Market Surveillance (PMS) Obligations  

| Requirement | Reference | How it is satisfied for each product |
|-------------|-----------|---------------------------------------|
| **PMS system** (overall framework, data collection plan) | Art. 83 | Established PMS system covering the three devices; uses sources listed in source [2] (serious incidents, complaints, trend reporting, literature, user feedback, competitor information). |
| **PMS plan** (detail of activities, frequency) | Art. 84 | Frequency table in source [1] (e.g., DQE degradation quarterly for detector; dose‑overexposure monitoring immediate/quarterly for handheld source; software error logging monthly). |
| **Periodic Safety Update Report (PSUR)** | Art. 86(1)(a) – PSUR content; Art. 86(2) – update cadence | • X‑ray Detector: PSUR every **2 years** (source [1])  <br>• Handheld Source: PSUR every **1 year** (source [1])  <br>• GUI SaMD: PSUR every **2 years** (source [1]). |
| **Vigilance reporting (serious incidents & FSCA)** | Art. 87 | Immediate notification of any serious incident detected via “Serious incidents + PSURs + FSCAs” source in [2]. |
| **Trend reporting** | Art. 88 | Quarterly trend data from internal statistics (source [2]) triggers corrective actions when pre‑defined thresholds are exceeded. |

---

### 3. Post‑Market Clinical Follow‑up (PMCF)  

| Device | PMCF necessity (source [1]) | Minimum elements of a PMCF plan (Annex XIV Part B) |
|--------|------------------------------|---------------------------------------------------|
| X‑ray detector | “Equivalence claim review → decision” | • Objective: confirm that performance remains equivalent to predicate. <br>• Data sources: DQE measurements, pixel defect rates, field complaints. <br>• Sample size & follow‑up period to be defined after equivalence assessment. |
| Handheld X‑ray source | “Ionising radiation → active clinical data collection recommended” | • Objective: verify that patient dose stays within the prescribed limits in real use. <br>• Data sources: dose‑monitoring logs, incident reports, user feedback on mechanical integrity and battery performance. <br>• Prospective collection of at least 30 procedures per indication over 12 months (example target – to be refined). |
| GUI SaMD | “Error data collection mandatory during use” | • Objective: capture software‑related adverse events and usability issues. <br>• Data sources: bug log, error reports, usability incident feedback from CRM system. <br>• Continuous monitoring with quarterly review; any critical defect triggers immediate corrective action (Art. 87). |

---

### 4. Required Clinical & Technical Evidence  

| Device | Core evidence (to be part of the TD) |
|--------|---------------------------------------|
| **X‑ray detector** | • **Clinical Evaluation Report (CER)** – Annex XIV Part A, kept current Art. 61.<br>• **Risk Management File (RMF)** – ISO 14971/Annex I §16‑22.<br>• **IEC 62220‑1‑1** DQE test data (performance verification). |
| **Handheld source** | • **CER** (including dose‑assessment studies).<br>• **RMF** with radiation‑protection risk controls (Annex I §16.4).<br>• **IEC 60601‑2‑28** and/or **IEC 60601‑2‑54** conformity test reports for X‑ray equipment.<br>• Dose‑monitoring data from field use. |
| **GUI SaMD** | • **CER** (software’s contribution to clinical performance).<br>• **RMF** referencing IEC 62304 (software lifecycle) and IEC 62366‑1 (usability).<br>• Maintenance records & bug‑log (source [1]). |

---

### 5. Gaps / Missing Information (to be obtained before NB submission)

| Gap | Reason why it is needed |
|-----|--------------------------|
| **Detailed Intended Use Statements** for each device (including indications, patient population, environment of use). | Required to justify classification rule and to shape CER & PMCF scope. |
| **Complete Hazard Identification & Risk Control Measures** (e.g., specific interlocks for handheld source, alarm thresholds for detector DQE degradation, fail‑safe mechanisms in software). | Needed for Annex I §16‑22 compliance and for risk‑benefit analysis in PSUR/PMCF. |
| **Equivalence Data Package** for the detector (bench comparison to predicate device). | PMCF decision depends on equivalence; absence blocks CE marking. |
| **Field Dose‑Monitoring Protocol** (how dose is measured, recorded, and evaluated for handheld source). | Supports clinical evidence of safety & effectiveness; required in CER and PSUR. |
| **Usability Test Report** for GUI SaaMD (IEC 62366–1). | Demonstrates compliance with Annex I §17 (electronic programmable systems) and reduces usability‑related risk. |
| **Exact Thresholds for Trend Reporting** (e.g., DQE drop > 10 % or cumulative dose exceedance). | Needed to trigger Art. 88 trend reporting and appropriate corrective actions. |
| **PMCF Study Protocols** (sample size, statistical analysis plan, timelines). | Must be documented in the PMCF plan (Annex XIV Part B) before data collection begins. |

---

### 6. Core Risk Controls (aligned with Annex I GSPR)

1. **Radiation Protection (detector & handheld source)** – design shielding, interlocks, dose‑monitoring alarms; compliance with §16.4.  
2. **Electrical Safety** – IEC 60601‑2‑28/54 testing, verification of battery safety for handheld source (§18).  
3. **Software Reliability** – IEC 62304 development lifecycle, regular patch management, bug‑tracking, and error‑handling routines (§17).  
4. **Usability & Human Factors** – IEC 62366‑1 usability engineering to mitigate user errors in image interpretation (GUI) and handling of the handheld source (§22).  
5. **Fault Detection & Alarming** – real‑time monitoring of DQE, pixel defects, dose metrics; automatic alerts when thresholds are exceeded (§20).  

---

### 7. Human‑Escalation Triggers  

| Trigger | Action & Responsible Party | Regulatory reference |
|---------|----------------------------|----------------------|
| **Serious incident (e.g., patient over‑dose, device malfunction causing injury)** | Immediate notification to the Notified Body and competent authority via vigilance report; initiate field corrective action if required. | Art. 87 (Vigilance) |
| **Trend detection exceeding predefined limits** (e.g., >10 % DQE loss, >5 % of procedures exceed dose limit) | Escalate to senior PMCF manager → prepare trend‑report & possibly a Field Safety Corrective Action (FSCA). | Art. 88 (Trend reporting) |
| **Critical software defect identified** (e.g., mis‑display of image data) | Halt distribution, issue urgent FSCA, update software version; notify NB within 48 h. | Art. 87 & Annex XIV Part B (PMCF evaluation) |
| **Failure to achieve PMCF objectives after scheduled review** | Suspend market placement pending remedial actions and updated risk analysis; inform NB of delay in meeting PSUR/PMCF schedule. | Art. 86 (PSUR content – benefit‑risk determination) |
| **Non‑conformity of radiation dose measurements with IEC standards** | Immediate corrective action on the device design or labeling; re‑evaluate clinical data and update CER. | Annex I §16.4 & IEC 60601‑2‑28/54 |

When any of these triggers are met, the responsible **Regulatory Affairs Lead** must open a formal deviation record, notify the Notified Body, and ensure that corrective actions are documented in the Technical Documentation (Annex II) and communicated via EUDAMED (Art. 33‑39).

---

### 8. Regulatory Judgment  

*Based on the information extracted from the source documents, the three products fall under MDR classes IIa (X‑ray detector, GUI SaMD) and IIb (handheld X‑ray source). The appropriate conformity‑assessment route is **Annex IX** for each complete device, supplemented by type‑examination of the handheld radiation source if supplied as a separate component. All mandatory PMS elements—system, plan, PSUR cadence, vigilance and trend reporting—are identified in the source excerpts and are aligned with Articles 83–88. However, critical gaps remain (intended use statements, detailed risk analysis, equivalence data, PMCF protocols, usability testing, and clear trend thresholds). These must be resolved before a Notified Body can confirm that “no questions left” on the technical documentation.*

---

### 9. Peer‑Review Prompt  

> **Colleague Request:** Please review the assumptions made regarding (a) classification of the handheld source under Rule 10 rather than Rule 9, (b) the adequacy of the identified PSUR frequencies relative to Art. 86 for each class, and (c) any jurisdiction‑specific omissions (e.g., requirements for a Clinical Investigation under § 61 if equivalence cannot be demonstrated). Identify missing citations or evidence that would affect the conformity‑assessment route.

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

### kb-eval-20260721-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "4038dfc3a558f695", "source": "github:holee9/MD-process/issue-drafts/158_08_SOP-PMS-001_v0.3_QMSR_EUDAMED_불만처리.md", "source_hash": "ec94495a1bf80d4e9e3bb0b8c01801499bd1ff16dd2c0697728ee0455ba62816"} -->

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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) for a Class III Medical Device**

---

### 1. Likely Classification / Conformity‑Assessment Route  

| Item | Assessment |
|------|------------|
| **Device class** | *Presumed* **Class III** – the SOP explicitly refers to “​PSUR submission (Class III EUDAMED 의무)​” (source [1]). Confirmation of the actual classification must be obtained from the device’s intended purpose and applicable MDR rules (e.g. Rule 9, 10‑b, 11‑c). |
| **Applicable rule** | To be identified once the intended use is known (Rule 9 for active therapeutic energy, Rule 10 for diagnostic/monitoring with a high‐risk impact, Rule 11 for software with life‑threatening decision support, etc.). Until then the rule cannot be cited. |
| **Conformity‑assessment route** | **Annex IX** (full quality‑management system audit + assessment of technical documentation) – the usual route for Class III devices that require a Notified Body’s full review.  (Reference: MDR Annex IX). |

*Action*: Obtain the device’s intended medical purpose, anatomical site, and mode of action to select the precise classification rule and confirm Class III status.

---

### 2. Mandatory Post‑Market Documentation (MDR)

| Requirement | Reference | Evidence needed |
|-------------|-----------|-----------------|
| **PMS plan** (overall system) | Art. 84 MDR – “post‑market surveillance plan” | • Scope of PMS activities, data sources, responsibilities, timeframes.<br>• Identification of the “actor” (manufacturer, authorised representative) and link to UDI/Actor registration in EUDAMED (source [1] §8.1). |
| **PMS report** for Class I | Art. 85 MDR – not directly relevant (device is Class III). |
| **Periodic Safety Update Report (PSUR)** | Art. 86 MDR – mandatory for Class IIa/IIb/III. Must be submitted to EUDAMED. | • Benefit‑risk determination conclusions.<br>• Main findings of any PMCF activities (Art. 86(1)(b)).<br>• Sales volume & using‑population estimate (Art. 86(1)(c)). |
| **PMCF plan** (if required) | Annex XIV Part B MDR – “post‑market clinical follow‑up” | • Clinical objectives, endpoints, data sources, schedule.<br>• linkage to the Clinical Evaluation Report (CER). |
| **Clinical Evaluation Report (CER)** (kept current) | Annex XIV Part A MDR – Art. 61 MDR | • Systematic review of state‑of‑the‑art literature and clinical investigations.<br>• Updated benefit‑risk conclusion. |
| **Vigilance / FSCA reporting** | Art. 87 MDR (serious incidents & field safety corrective actions) | • Process for incident detection, investigation, reporting to the Competent Authority and NB within required timelines. |
| **Trend reporting** | Art. 88 MDR | • Aggregated analysis of non‑serious events that may indicate a systemic risk. |
| **UDI / Device registration in EUDAMED** | Art. 33‑39 MDR – “Actor registration/UDI/Market surveillance linkage” (source [1] §8.1) | • UDI‑DI, SRN field populated on F‑PMS‑002 form (source [1] last bullet). |
| **Technical documentation (including PMS)** | Annex II & Annex III MDR – “technical documentation” & “post‑market surveillance technical documentation” | • Updated risk management file (ISO 14971) reflecting post‑market data.<br>• Records of corrective actions, field safety notices, etc. |

---

### 3. Evidence Gaps / Missing Information  

| Gap | Why it matters | Suggested source/action |
|-----|----------------|------------------------|
| **Exact intended use & indications** | Determines classification rule and informs the scope of clinical evaluation & PMCF. | Obtain device label/IFU, marketing dossier. |
| **Specific MDR rule (9‑11‑17)** | Required to cite the correct classification rule; affects conformity‑assessment route. | Map intended purpose to MDC rules. |
| **Current CER status** | Must be “kept current” under Art. 61 MDR; missing data would block NB approval of PSUR/PMCF. | Request latest CER draft & evidence matrix. |
| **Existing clinical data (pre‑market and post‑market)** | Needed for PMCF plan, benefit‑risk analysis in PSUR. | Assemble clinical investigation reports, registries, literature reviews. |
| **Risk Management File (RMF) updates** | PMS findings must feed back into risk controls per ISO 14971; required for Annex III compliance. | Provide latest RMF with post‑market risk evaluation. |
| **UDI allocation & SRN registration in EUDAMED** | SOP adds UDI‑DI/SRN fields to F‑PMS‑002 (source [1]), but actual entries are not shown. | Verify completion of the form and successful upload to EUDAMED. |
| **PMCF necessity decision** | Not all Class III devices need a separate PMCF plan if sufficient clinical data already exist; decision must be documented. | Conduct gap analysis between current CER evidence and MDR expectations. |
| **Vigilance module “과도기” (transition)** | SOP notes a vigilance‑module transition phase; details of interim processes are missing. | Clarify timeline, responsibilities, and any temporary reporting mechanisms. |

---

### 4. Core Risk Controls (linked to PMS/PMCF)

1. **Risk Management Process (ISO 14971) → Integrated with PMS**  
   * Continuously update the risk analysis based on PSUR findings, trend reports, and field safety notices.  

2. **Usability Engineering (IEC 62366‑1)** – especially if device interaction influences risk.  

3. **Software Lifecycle Controls (IEC 62304)** – applicable to any embedded software (Rule 11).  

4. **Radiation Protection Measures (Annex I §16 & IEC 60601‑2‑54/28/44 as appropriate)** – for devices emitting ionising radiation; ensure compliance with §16.4.  

5. **Active Device Controls (Annex I §§18‑19)** – monitor performance of energy delivery or diagnostic functions, depending on rule.  

6. **Corrective & Preventive Actions (CAPA) tied to PMS outcomes** – documented in the PMS system per Art. 83 MDR.

7. **Labeling / IFU Updates (Annex I §23)** – reflect any new contraindications, warnings, or use‑conditions identified post‑market.

---

### 5. Human‑Escalation Triggers  

| Trigger | Action & Responsible Party |
|---------|----------------------------|
| **Serious incident** (per Art. 87) OR **FSCA** issuance | Immediate notification to the Notified Body and Competent Authority; activation of internal FSCA team; record in EUDAMED vigilance module. |
| **Trend detection** that may indicate a systemic risk (Art. 88) | Escalate to senior management & risk‑management lead; update PSUR draft; consider interim field safety notice. |
| **Missed PSUR deadline** (annual for Class III, Art. 86) | Alert Quality Manager; trigger expedited drafting and submission; document root cause. |
| **UDI / SRN registration failure in EUDAMED** (source [1] §8.1) | Notify the Regulatory Affairs lead; suspend market distribution of non‑registered batches until resolved. |
| **Negative benefit‑risk conclusion** from PSUR or PMCF | Convene a cross‑functional risk‑acceptance meeting; prepare possible withdrawal/recall plan; inform Notified Body. |
| **Non‑conformity identified in PMS audit (Art. 83)** | Open CAPA, assign corrective actions, and report to NB if required. |
| **Regulatory change (e.g., new FDA QMSR guidance) affecting EU obligations** (source [1] §7.3) | Conduct impact assessment; update SOP‑PMS‑001 accordingly; inform senior management. |

---

### 6. Summary Judgment & Next Steps  

*The available SOP excerpt demonstrates that the manufacturer is aligning its PMS activities with EUDAMED requirements for a **Class III** device, including PSUR integration and UDI registration. However, critical information—principally the device’s intended medical purpose, exact classification rule, current CER status, and existing post‑market clinical data—is absent.*  

1. **Obtain the missing device description** (intended use, anatomy, mode of action) to confirm Class III status and cite the appropriate MDR Rule (Rule 9/10/11/17).  
2. **Collect the latest Clinical Evaluation Report** and verify that it is “kept current” under Art. 61 MDR.  
3. **Compile all post‑market clinical data** (registries, literature, investigations) to populate a PMCF plan or justify its exemption.  
4. **Validate that UDI‑DI/SRN fields are completed in the F‑PMS‑002 form** and successfully uploaded to EUDAMED (Art. 33‑39).  
5. **Update the risk management file** with findings from the upcoming PSUR draft; ensure linkage to Annex III technical documentation.  

*Only after these items are resolved can the Notified Body be satisfied that the PMS system is complete, and a compliant PSUR/PMCF submission prepared.*

---

### 7. Peer‑Review Prompt  

> **To: RA Team – please review**  
> - Are there any additional MDR articles or annexes (e.g., Annex VI for clinical investigations) that should be considered given the device’s probable classification?  
> - Does the SOP’s “vigilance 모듈 과도기” (transition) raise jurisdiction‑specific timing issues for Art. 87 reporting that we have missed?  
> - Have we captured all necessary evidence sources for a Class III PMCF justification, or are there gaps in our clinical data strategy?  

*Please challenge the assumptions above and flag any EU‑specific obligations not addressed.*

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

### kb-eval-20260721-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2fd9acfe010b1502", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning**

---

### 1. Device Scope (as derived from source)

| Item | Observation |
|------|--------------|
| **Primary technology** | Ionising‑radiation‑emitting diagnostic equipment (X‑ray generator). |
| **Ancillary component** | Medical device software that processes the X‑ray image (SaMD). |
| **Regulatory classification** | **Rule 10** of Annex VIII – “Active devices for diagnosis and monitoring that emit ionising radiation” → **Class IIb**. <br>Software is covered by **Rule 11** (SaMD) – typically Class IIa/IIb depending on impact; the source only flags Rule 11, no further subclassing provided. |
| **Reference** | Annex VIII, Rule 10 (ionising‑radiation diagnostic device) → **Class IIb**. <br>Annex VIII, Rule 11 (SaMD). |

---

### 2. Conformity‑Assessment Route  

| Requirement | Applicable MDR provision | Expected route |
|-------------|---------------------------|---------------|
| **Quality‑management system + technical documentation assessment** | Annex IX – “Full quality‑system assessment and technical file review”. | **Annex IX** (NB‑led) for the Class IIb device. <br>If the SaMD is classified as Class IIa, it can be covered under the same NB audit (combined dossier). |
| **Declaration of Conformity** | Annex IV. | To be issued after successful Annex IX assessment. |

---

### 3. Evidence Package Required for NB Submission  

| Evidence | MDR citation | Typical content |
|----------|--------------|-----------------|
| **Technical documentation** | Annex II. | Device description, intended use, design & manufacturing information, risk‑management file, verification/validation reports, labeling (Annex I §23). |
| **Risk management file** | Annex I §§18–20; ISO 14971. | Hazard analysis, risk evaluation, residual‑risk justification, especially radiation protection (§16) and software safety (§17). |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (kept current under Art. 61). | State‑of‑the‑art literature review, clinical data from pre‑market studies/registries, equivalence justification (if any). |
| **PMCF Plan** | Annex XIV Part B. | Objectives, study design, endpoints, population, timelines, data‑collection methods, statistical analysis plan. |
| **PMCF Evaluation Report** | Annex XIV Part B (final report). | Findings, benefit‑risk determination, impact on risk‑management file. |
| **PMS Plan** | Art. 84. | Description of systematic collection & review of post‑market data (user feedback, vigilance reports, literature monitoring), performance indicators, responsibilities. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 (for Class IIb). | • Benefit‑risk conclusions (Art. 86(1)(a))<br>• Main PMCF findings (Art. 86(1)(b))<br>• Sales volume & user population estimate (Art. 86(1)(c)). <br>Update frequency: **annually** for Class IIb (Art. 86(2)). |
| **Post‑Market Surveillance Report (for Class I)** – not applicable; PSUR supersedes for this Class IIb device. | — | — |

---

### 4. Missing / Unclear Information (gaps that must be filled before NB submission)

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Intended‑use statement & target clinical indication** | Basis for classification, risk analysis and clinical evaluation. | Provide a precise description of the diagnostic procedure, anatomical region, patient population, and any intended therapeutic adjuncts. |
| **Device architecture diagram** (source + detector + software) | Needed to delimit scope of each component under separate MDR rules (Rule 10 vs Rule 11). | Submit a block diagram with functional allocation. |
| **Clinical data source list** (clinical investigations, real‑world evidence, registries) | Required for CER and PMCF justification. | Identify all studies, dates, sample sizes, endpoints; indicate whether data are from the device under evaluation or equivalent devices. |
| **State‑of‑the‑art literature search methodology** | Annex XIV Part A demands a systematic SOTA review. | Outline databases searched, keywords, inclusion/exclusion criteria, date range. |
| **PMCF study design details** (sample size calculation, follow‑up duration, endpoints) | Determines adequacy of post‑market clinical evidence. | Draft full protocol; specify primary/secondary outcomes linked to residual risks. |
| **PMS data‑collection procedures** (e.g., complaint handling workflow, field safety corrective actions) | Art. 84 requires a systematic PMS system. | Provide SOPs, responsible persons, IT tools, frequency of review. |
| **Radiation safety verification data** (dose measurements, shielding calculations) | Annex I §16 (radiation protection). | Include test reports per IEC 60601‑2‑54 and any national dose limits compliance evidence. |
| **Software lifecycle documentation** (development plan, verification & validation, usability) | Annex I §§17–18; IEC 62304, IEC 62366-1. | Supply software development file, risk control measures for SaMD. |

---

### 5. Key Risk Controls to Demonstrate

| GSPR clause | Control measure | Supporting standard / evidence |
|-------------|-----------------|--------------------------------|
| **§16 – Protection against radiation** | Dose‑output monitoring, interlocks, automatic shut‑off, shielding design verification. | IEC 60601‑2‑54 (radiography) & IEC 60601‑1 (general safety). |
| **§17 – Electronic programmable systems / software** | Secure boot, authentication, traceability of software version, error handling. | IEC 62304 (software lifecycle), IEC 62366‑1 (usability). |
| **§18 – Active devices & connections** | Electrical isolation, EMC compliance, fail‑safe mode for power loss. | IEC 60601‑1‑2 (EMC), IEC 60601‑1‑8 (alarm systems). |
| **§22 – Use by lay persons (if applicable)** | User‑interface design, clear IFU, training requirements. | Human factors validation per IEC 62366‑1. |
| **Overall residual risk justification** | Updated risk‑management file incorporating PMS/PMCF findings. | ISO 14971, MDR Annex I §10–22. |

---

### 6. Human‑Escalation Triggers (when to raise to senior management / Notified Body)

| Trigger | Reason for escalation |
|--------|-----------------------|
| **Undefined intended use or ambiguous clinical indication** | Classification and CE‑marking cannot proceed without a clear claim. |
| **Absence of a complete PMCF protocol** (no statistical justification, no defined endpoints) | Would lead to non‑conformity with Annex XIV Part B; NB will request clarification. |
| **Inadequate radiation safety validation data** (e.g., missing dose‑measurement report) | Direct breach of GSPR §16 – safety risk. |
| **Software development file incomplete** (no verification/validation traceability matrix) | Non‑conformity with GSPR §§17–18 and IEC 62304. |
| **PMS plan lacking systematic data‑collection process** (no defined responsibilities or review frequency) | Violates Art. 84; NB will reject dossier. |
| **PSUR not scheduled for annual update** (or missing sales/usage estimates) | Conflict with Art. 86(2) for Class IIb. |
| **Any critical incident reported (Serious Incident/FSCAs) without a documented field‑safety corrective action plan** | Must be handled under Art. 87; escalation to vigilance team and NB required. |

When any of the above triggers are identified, the RA lead must:

1. Document the gap in the project risk register.  
2. Notify the Project Manager and Quality‑Assurance Lead within **5 working days**.  
3. Prepare a remediation plan with clear responsibilities and timelines; submit to the Notified Body for review before dossier closure.

---

### 7. Summary Judgment

| Aspect | Current status (based on source) | Required next step |
|-------|-----------------------------------|--------------------|
| **Classification** | Rule 10 → Class IIb (X‑ray generator). Rule 11 applies to the software component. | Confirm SaMD subclassification; finalize combined dossier scope. |
| **Conformity route** | Annex IX (full QMS & technical file assessment). | Align internal QMS with MDR requirements, schedule NB audit. |
| **PMS/PMCF evidence** | PMS / PMCF / PSUR “체계 구축 필요” indicated in source but no details provided. | Draft full PMS plan (Art. 84) and PMCF protocol (Annex XIV Part B); schedule periodic data collection; develop PSUR template per Art. 86. |
| **Risk controls** | GSPR checklist mentioned, but specific controls not listed. | Populate risk‑management file with radiation protection, software safety, and usability measures as per Annex I §§16‑18 and IEC standards. |

*If any of the missing items in Section 4 remain unresolved, the dossier will be non‑conformant with MDR requirements and must be escalated before submission to a Notified Body.*

---

### 8. Peer‑Review Prompt  

> **Colleague, could you review the assumptions made regarding (1) the combined classification of the X‑ray generator plus SaMD under Rules 10 and 11, (2) the suitability of Annex IX as the sole conformity‑assessment route for this mixed device, and (3) any potential gaps in our PMS/PMCF coverage given the limited source excerpt? Please also check whether any jurisdiction‑specific nuances (e.g., national implementing measures on ionising radiation devices) have been overlooked.**

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

### kb-eval-20260721-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "3a61372dfd698a2c", "source": "github:holee9/MD-process/issue-drafts/157_08_SOP-FSCA-001_v0.3_QMSR_EUDAMED_FSCA.md", "source_hash": "7ceead695690f1ea2c83bf679e8114b768ad7b4b8dbab95eccc08d70d1be9f02"} -->

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

> **Regulatory Draft – PMS / PMCF Planning & EUDAMED Transition (FSCA – SOP‑FSCA‑001 v0.3)**  

---

### 1. Device Scope – Classification Gap  
| Item | Current status (from source) | Required to complete |
|------|------------------------------|----------------------|
| **Device name / model** | not mentioned | Obtain exact trade name, model number and any variant identifiers. |
| **Intended medical purpose** | not mentioned | Capture the full intended use wording (including indications, target population, clinical setting). |
| **MDR classification rule** | n/a – source only refers to “FSCA” activities | Apply Annex VIII rules (Rule 9‑11, 17 etc.) once intended purpose is known; record the Rule number and resulting class (I, IIa, IIb, III). |
| **GSPR sections applicable** | not listed | Map device to relevant General Safety & Performance Requirements (§1‑23 of Annex I) based on its nature (active, implantable, software, radiation etc.). |

*Action:* The above items must be provided before any definitive MDR pathway can be selected.  

---

### 2. Conformity‑Assessment Route (MDR)

| Classification (to be confirmed) | Applicable Annex for assessment | Typical documentation bundle |
|-----------------------------------|----------------------------------|------------------------------|
| **Class I** (non‑sterile, non‑measuring) | Annex IX (QMS + technical doc review) – *only if a QMS is required*; otherwise self‑declaration. | Technical file (Annex II), Declaration of Conformity (Annex IV). |
| **Class IIa / IIb / III** | Annex IX (full quality‑system audit + technical documentation) or Annex X (type‑examination) where a Notified Body is required. | Technical file (Annex II), PMCF plan & report (Annex XIV B), PMS plan (Art. 84), PSUR (Art. 86). |

*Note:* The exact route cannot be finalised until the device class is known.

---

### 3. Post‑Market Surveillance (PMS) / PMCF Evidence Required  

| Requirement | MDR reference | What must be produced |
|-------------|----------------|-----------------------|
| **PMS system** (overall process, responsibilities, data collection) | Art. 83 | PMS SOP, organisational chart, roles & responsibilities. |
| **PMS plan** (including PMCF) | Art. 84 | Documented plan describing data sources, frequency, key performance indicators; links to clinical evaluation updates. |
| **PMCF plan** (if applicable) | Annex XIV Part B | Detailed protocol for prospective/retrospective clinical data collection, target population, endpoints. |
| **PMS report** (Class I only) | Art. 85 | Annual summary of surveillance activities and any corrective actions taken. |
| **Periodic Safety Update Report (PSUR)** (Classes IIa‑III) | Art. 86(1‑2) | • Benefit–risk conclusions <br>• Main PMCF findings <br>• Sales volume & user population estimate; updated at least annually for IIb/III, biennially for IIa. |
| **Vigilance (FSCA) reporting** | Art. 87 (serious incidents) + Art. 88 (trend reporting) | FSCA‑CAPA documentation, incident investigation reports, corrective action closure evidence. |
| **EUDAMED filing** – transition from interim “manual” route to mandatory electronic submission | §5.12 of SOP‑FSCA‑001 (source) – aligns with MDR obligations | • Unique Device Identifier (UDI) registration <br>• Vigilance and PMS data upload via EUDAMED modules (Market Surveillance, Vigilance). |

---

### 4. FSCA Integration & Documentation  

| Element | Source requirement | Evidence to be generated |
|---------|-------------------|--------------------------|
| **FSCA‑CAPA linkage** (strengthened documentation path) | §5.11.1 “FSCA‑CAPA 연계 강화 및 문서화 경로도” | Flow‑chart linking FSCA investigations → CAPA record → update of risk management file & PMS plan. |
| **Self‑inspection checklist (5 items)** | §5.11.2 “FSCA 실사 자가점검표 (5항목)” | Completed checklist per audit, signed off by QA manager. |
| **Transition to EUDAMED reporting** | §5.12 series – “EUDAMED 의무화 대응 FSCA 보고 경로 전환” | Revised SOP sections describing electronic submission steps; version control log showing migration date. |

*Key link*: All FSCA outcomes must be fed back into the risk management file (ISO 14971) and reflected in updated GSPR compliance evidence (§16‑§20 Annex I).  

---

### 5. Risk Management Updates  

1. **CAPA loop** – each FSCA finding triggers a risk analysis per ISO 14971, with revised risk control measures documented.  
2. **Residual risk re‑evaluation** – incorporate new clinical data from PMCF (Annex XIV B) into the benefit–risk determination required for PSUR (Art. 86).  
3. **Software / Active device considerations** – if the device falls under §17 (electronic programmable systems) or §18 (active devices), ensure compliance with IEC 62366‑1 (usability) and IEC 62304 (software lifecycle).  

---

### 6. Missing Information Checklist (to be supplied before final submission)

| Item | Reason for need |
|------|-----------------|
| Exact device identification (Udi‑DI, model numbers) | EUDAMED registration & vigilance traceability. |
| Intended purpose wording | Determines classification rule and GSPR scope. |
| Current risk management file status (including existing FMEA/FMECA) | Needed to link FSCA outcomes to risk controls. |
| Existing PMS data sources (registries, complaints database) | Basis for PMCF plan & PSUR content. |
| Current PSUR schedule (if any) | Aligns with Art. 86 reporting cadence. |
| NDA/registration number in the United States (FDA QMSR CP 7382.850 mentioned) – verify relevance to EU market | Determines whether US‑based CAPA can be directly reused or must be duplicated for MDR. |

---

### 7. Human‑Escalation Triggers  

| Trigger condition | Who must be alerted | Required action |
|-------------------|---------------------|-----------------|
| **Classification not yet determined** | Senior RA lead / Product Owner | Conduct classification workshop; update SOP with correct Annex route. |
| **FSCA investigation uncovers a new serious risk that cannot be mitigated by existing controls** | RA manager, Clinical Affairs, Legal | Initiate a field safety corrective action (FSCA) per Art. 87; prepare urgent vigilance report and, if needed, a Field Safety Notice (FSN). |
| **EUDAMED migration deadline missed or technical failure of electronic reporting** | QMS Manager & IT Compliance | Escalate to senior management; implement temporary manual reporting as interim compliance measure (documented in SOP). |
| **PMCF data collection deviates from the approved plan** | Clinical Evaluation Lead | Conduct a gap analysis, amend PMCF protocol, and submit amendment to the Notified Body for review. |
| **Non‑conformity of FSCA‑CAPA documentation during internal audit** | Quality Assurance Manager | Issue corrective action, update SOP version, re‑train responsible personnel. |

---

### 8. Citations  

*Regulatory References (established)*  
- Art. 83 – PMS system (MDR).  
- Art. 84 – PMS plan (MDR).  
- Art. 85 – PMS report for Class I (MDR).  
- Art. 86(1‑2) – PSUR content & update frequency (MDR).  
- Art. 87 – Vigilance and reporting of serious incidents (MDR).  
- Art. 88 – Trend reporting (MDR).  
- Annex I §§16‑20 – General Safety & Performance Requirements relevant to risk controls.  
- Annex II – Technical documentation requirements.  
- Annex IV – EU Declaration of Conformity.  
- Annex XIV Part B – PMCF plan & evaluation report.  

*Source‑Specific Identifiers (case‑level)*  
- **FDA QMSR CP 7382.850** – referenced in §5.11 as the U.S. quality‑system regulation element to be aligned with.  
- No EUDAMED registration number, device identifier, or other case‑specific IDs were present in the source excerpts (→ *no specific identifier found in source — verify separately*).  

---

### 9. Peer‑Review Prompt  

> **@RA‑Peer:** Please review the assumptions made above:  
> - Are we justified in linking the FDA QMSR CP 7382.850 directly to MDR FSCA documentation, or is a separate mapping required?  
> - Does the proposed evidence list cover all mandatory items for the likely classes (IIa–III) given the SOP’s focus on market‑surveillance and FSCA?  
> - Have we missed any jurisdiction‑specific obligations (e.g., IVDR cross‑reference if the device contains a diagnostic software component)?   
> - Are the escalation triggers aligned with typical organizational responsibility matrices?  

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

### kb-eval-20260721-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "ace8201d85c8dad0", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

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

> **Regulatory Draft – Post‑Market Surveillance (PMS) & Post‑Market Clinical Follow‑up (PMCF) Planning  

Prepared for: EU MDR 2017/745 compliance team  
Date: 2026‑07‑21**

---

### 1. Scope & Objective
Provide a concise, evidence‑based outline of the regulatory requirements that must be satisfied before any CE marking submission can be made under the EU Medical Device Regulation (MDR). The focus is on:

* Determining the device classification and appropriate conformity‑assessment route.  
* Defining the minimum clinical‐evaluation and post‑market documentation that the Notified Body (NB) will expect to see “no questions left”.  

---

### 2. Classification & Conformity‑Assessment Route  

| Item | Requirement | Reference |
|------|-------------|-----------|
| **Determine risk class** – Apply the sequential rule set in Annex VIII, selecting the highest class triggered by the device’s intended purpose and technology. (Rule 9, 10, 11, 17 etc., as appropriate.) | **Article 51 + Annex VIII** – “manufacturer bears classification responsibility; apply rules sequentially, highest applicable class prevails.” | Art. 51; Annex VIII |
| **Select conformity‑assessment route** – Once the class is known:  <br>• Class I (non‑sterile, non‑measuring) → self‑declaration (Annex IV).<br>• Class Is / Im → self‑declaration with NB involvement for specific modules (e.g., annex IX).<br>• Classes IIa/IIb/III → NB assessment of technical documentation and quality‑management system. | **Annex IX** (QMS + technical doc), **Annex X** (type‑examination) or **Annex XI** (production conformity verification) as appropriate to the chosen route. | Annex IX, X, XI |
| **Human trigger** – If any uncertainty remains after applying all 22 rules, escalate to the Competent Authority (CA) or consult the MDCG “Borderline and Classification” guidance (latest v2.1.1, Sep‑2023). | – | – |

> **Current status:** *No device‑specific intended use, technology description or rule citation is present in the source material.* Consequently the exact class and route cannot be fixed at this stage. The next step is to obtain a complete “Device Description & Intended Use” dossier from the product team.

---

### 3. Clinical Evaluation & Evidence Package  

| Deliverable | Minimum content | Reference |
|-------------|----------------|-----------|
| **Clinical Evaluation Report (CER)** – must be kept current and incorporated in the Technical Documentation. | • State‑of‑the‑art literature review.<br>• Clinical data from either “clinical investigations” or “equivalence” sources.<br>• Benefit‑risk conclusion. | Annex XIV Part A; Art. 61 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** – outlines objectives, methodology and schedule for gathering additional clinical evidence after market entry. | • Defined clinical questions.<br>• Planned data sources (registry, PMS studies, literature).<br>• Acceptance criteria & risk mitigation link to the CER. | Annex XIV Part B |
| **PMCF Evaluation Report** – final assessment of the PMCF activities and their impact on the benefit‑risk determination. | Same structure as CES but focused on post‑market data; must feed back into updated CER. | Annex XIV Part B |
| **Human trigger** – If any clinical gap (e.g., missing equivalence data, insufficient sample size) is identified during CER drafting, pause the submission and request additional clinical investigation or literature search. | – | – |

> **Missing Information:** No specific clinical data sources, predicate devices, or 510(k)/US‑agent details are provided in the source excerpts (see Section 5). These must be collected before the CER can be finalized.

---

### 4. Post‑Market Surveillance (PMS) System  

| Component | Requirement | Reference |
|-----------|-------------|-----------|
| **PMS System (process & documentation)** | • Defined procedures for systematic collection, review and analysis of post‑market data.<br>• Integration with risk‑management activities. | Art. 83 |
| **PMS Plan** (for Class IIa/IIb/III) | • Description of PMS activities, data sources, frequency, responsibilities.<br>• Outline of trend‑analysis methodology and reporting timelines. | Art. 84 |
| **Periodic Safety Update Report (PSUR)** – required for Classes IIa, IIb & III. | • Benefit‑risk conclusions (Art. 86(1)(a)).<br>• Main PMCF findings (Art. 86(1)(b)).<br>• Sales volume & user population estimates (Art. 86(1)(c)).<br>• Update interval: ≥ annually for IIb/III; every 2 y for IIa (Art. 86(2)). | Art. 86 |
| **Vigilance Reporting** – serious incidents / field safety corrective actions. | • Follow MDR Art. 87 reporting timelines and content. | Art. 87 |
| **Human trigger** – Any trend indicating a potential increase in residual risk, or an adverse‑event pattern that could affect the Benefit‑Risk determination, must be escalated to senior management and the NB (for Class IIa+). | – | – |

---

### 5. Identification Gaps & Information Needed  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Device intended purpose / mode of action** | Determines which Annex VIII rule(s) apply → classification. | Obtain a finalized “Intended Use Statement” from product ownership. |
| **Technology description (active, software, radiation, etc.)** | Affects rule selection (e.g., Rule 9 vs 10 vs 11 vs 17). | Provide full technical specification and architecture diagram. |
| **Clinical data sources (investigation reports, equivalence dossiers, literature list)** | Required for CER & PMCF. | Compile all pre‑market clinical evidence; flag any missing studies. |
| **Risk Management file (ISO 14971) with residual risk assessment** | Drives PMS/PMCF scope and controls. | Ensure latest FMECA and risk‑control measures are available. |
| **UDI registration details** – EUDAMED entry, UDI‑DB submission. | Mandatory for market placement; linked to traceability. | Complete UDI allocation & upload to EUDAMED. |
| **Authorized Representative (AR) documentation** – Agreement, address, Art. 11 compliance. | Required for CE marking of non‑EU manufacturers. | Confirm AR contract and inclusion in the Technical Documentation. |
| **Fee schedule & NB quotation** – Noted NB contract range (€10k–€100k+). | Needed to budget and trigger procurement process. | Obtain formal quote from selected NB based on class/route. |

> **Source‑level note:** The excerpts mention “CE + CER (Art. 61, MDR Annex XIV)”, UDI portals, vigilance (Art. 87), PSUR and the classification principle (Art. 51 + Annex VIII). No case‑specific identifiers (e.g., 510(k) numbers) appear; therefore: **no specific identifier found in source – verify separately**.

---

### 6. Risk Controls & GSPR Alignment  

| General Safety & Performance Requirement (GSPR) | Typical control measures (examples) |
|---------------------------------------------------|--------------------------------------|
| §16 – Protection against radiation (if applicable) | Verify compliance with IEC 60601‑2‑54/28/44; perform DQE testing per IEC 62220‑1‑1. |
| §17 – Electronic programmable systems | Apply IEC 62304 software lifecycle, conduct security risk analysis per IEC 62443. |
| §18 – Active devices & connected equipment | Demonstrate safe interaction with other active devices; apply IEC 60601‑1 basics. |
| §20 – Mechanical/thermal safety | Perform validated stress tests; use EN ISO 14708‑1 for implantables if relevant. |
| §22 – Devices for lay users | Human factors testing per IEC 62366‑1. |
| Overall risk management | ISO 14971 process integrated with PMS findings and updates to the risk file. |

All identified controls must be documented in the **Technical Documentation (Annex II)** and linked to post‑market data that may trigger re‑assessment.

---

### 7. Human‑Escalation Triggers (Decision Points)

| Situation | Escalation To | Reason |
|-----------|----------------|--------|
| Unresolved classification after rule application | Competent Authority & MDCG guidance panel | Prevent mis‑classifying a high‑risk device. |
| Evidence gap in CER (e.g., missing equivalence data) | Clinical Lead / Senior Management | Additional clinical investigation required before NB submission. |
| PSUR indicates upward trend in serious adverse events or residual risk increase | Quality‑Management Director & Notified Body | Required corrective actions and possible re‑classification. |
| Failure to meet PMS Plan milestones (data collection delay) | Project Manager & Regulatory Lead | May breach Art. 84 reporting timelines; need resource allocation. |
| UDI registration not completed in EUDAMED within 30 days of market launch | Compliance Officer | Non‑compliance with Art. 27–28 (UDI obligations). |
| NB rejects PMCF plan for insufficient statistical power | Regulatory Lead & Clinical Team | Must redesign study, potentially delaying CE marking. |

---

### 8. Summary Judgment  

* **Classification & route cannot be finalized without a full intended‑use and technology description.** Immediate action: obtain this information to apply Annex VIII rules (Art. 51).  
* **Core evidence package:** up‑to‑date CER (Annex XIV Part A), PMCF plan & report (Annex XIV Part B), PMS system & plan (Arts 83–84), and PSUR for Class IIa+ (Art. 86). All must be linked to the risk‑management file (ISO 14971) and reflected in the Technical Documentation (Annex II).  
* **Key missing items** are clinical data sources, risk‑assessment outputs, UDI registration status, and AR documentation. These gaps block a complete NB audit.  

Proceed to fill the identified gaps, then re‑evaluate classification; only after that can the appropriate conformity‑assessment route be selected and the NB submission pack compiled.

---

### 9. Peer‑Review Prompt  

> **To: RA peer (e.g., Sofia K.)**  
> Please review the assumptions made in Sections 2–5, especially the interpretation of the classification principle (Art. 51 + Annex VIII) given the lack of device‑specific information. Verify whether any additional MDR articles or MDCG guidance items (e.g., MDCG 2023‑X) might affect the PMS/PMCF requirements for devices intended to emit ionising radiation (Rule 10/17). Also confirm that all cited references correspond to the latest consolidated MDR text (as of 2024).

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

### kb-eval-20260721-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "b02a51ce1c38768d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

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

> **Regulatory Draft – Digital Medical Software (AI‑enabled) under MFDS**

---

### 1. Device Classification & Submission Route  

| Korean MFDS | Rationale (source) | Required Regulatory Path |
|------------|-------------------|--------------------------|
| **2등급** (Class II) – may be upgraded to higher class depending on the “보조 기능 수준” (supportive function level) | Stated in the *‘의료용 소프트웨어 허가·심사 가이드라인’* and reinforced by the 2025 Digital Medical Products Act that places AI/SW products under a dedicated framework. (Source [1]) | **허가** (full approval). Class II devices require a formal MFDS 허가 submission, not merely 신고. |

> **Note:** If functional analysis later shows that the software performs a primary therapeutic function or carries higher risk, re‑classification to 3등급 should be considered and trigger a separate “전문허가” pathway.

---

### 2. Core Submission Dossier – Required Evidence  

| Element | MFDS Requirement | Comments / Supporting Guidance |
|---------|------------------|--------------------------------|
| **Technical Documentation** (design dossier, software architecture, risk management file) | Must comply with ISO 13485 & ISO 14971; additional items specified in the *‘디지털의료제품법’* (2025‑01‑24) such as change‑control plan and component performance evaluation. (Source [1]) | Include traceability matrix linking requirements → design → verification/validation. |
| **Software Usability & Validation** | If the product is a standalone software, the *‘독립형 SW 사용적합성 가이드라인’* applies. (Source [1]) | Provide usability test reports in Korean language; confirm conformity with IEC 62366‑1. |
| **Clinical Evaluation** | Local clinical data are required when no adequate foreign clinical evidence exists or when the device is “고위험” (≥3등급). For 2등급 AI software, MFDS usually accepts a well‑structured literature review + limited Korean post‑marketing surveillance, but confirm on a case‑by‑case basis. | Identify any prior CE mark / FDA clearance that can be leveraged; otherwise plan a pilot clinical study in Korea. |
| **KGMP Certification** | Manufacturing site (or CRO if outsourced) must hold KGMP certification for software products (specialized “소프트웨어 제조용 KGMP”). | Provide certificate copy and scope. |
| **Labeling & IFU** | All labeling, instructions for use (IFU), and any software help files must be in Korean. Dual‑language (Korean + English) is permitted but Korean must be primary. | Prepare Korean translation reviewed by a certified medical translator. |
| **Cybersecurity & AI Change Management** | Follow the *‘디지털의료제품법’* requirements: <br> – **변경관리계획** (Predetermined Change Control Plan) for AI algorithms <br> – **구성요소 성능평가** (component performance assessment). | Document algorithm versioning, training data provenance, and post‑deployment monitoring plan. |
| **Post‑Market Surveillance (PMS)** | Submit a PMS plan covering adverse event reporting, periodic safety update reports (PSUR), and real‑world evidence collection for AI performance drift. | Align with MFDS “시판후조사” regulations. |

---

### 3. Missing Information – Gap Assessment  

| Item | Why Needed | Current Status (based on source) |
|------|------------|----------------------------------|
| **Exact device name & Intended Use** | Determines risk level, clinical evidence scope, and labeling content. | Not provided in excerpts. |
| **Standalone vs. Accessory status** | Triggers the *‘독립형 SW 사용적합성 가이드라인’* (standalone) or accessory pathway. | Unclear – must be clarified. |
| **Algorithm change frequency & Planned Updates** | Required for AI‑specific change‑control plan under the 2025 Act. | Not described. |
| **KGMP certification scope and expiry date** | Mandatory for submission; missing in excerpt. | No evidence supplied. |
| **Korean language labeling draft** | Legal prerequisite; cannot be submitted without it. | Absent. |
| **Local clinical data or justification for reliance on foreign data** | Determines need for Korean clinical study. | Not addressed. |
| **Software security architecture documentation** | Supports cybersecurity claim under the new Act. | Not mentioned. |

*Action*: Obtain these items from the product development team before dossier finalization.

---

### 4. Risk Controls – Key Areas  

1. **Risk Management (ISO 14971)** – Hazard identification, risk estimation, and mitigation for both intended use and AI‑driven decision support.  
2. **Usability Engineering (IEC 62366‑1)** – Human factors testing to ensure safe interaction with the UI, especially for AI output interpretation.  
3. **Cybersecurity** – Implementation of secure coding practices, vulnerability management, and an incident response plan per MFDS guidance on digital medical products.  
4. **Algorithm Validation** – Performance testing across diverse Korean patient datasets; traceability of training data to regulatory‑acceptable sources.  
5. **Change Control** – Predetermined Change Control Plan (PCCP) covering algorithm updates, software patches, and component upgrades, as mandated by the 2025 Digital Medical Products Act.

---

### 5. Citations  

| Reference | Type |
|-----------|------|
| 의료용 소프트웨어 허가·심사 가이드라인 | Established regulatory reference – classification rule for digital medical software (2등급). |
| 디지털의료제품법, 2025‑01‑24 시행 | Established statutory basis for AI/SW‑specific framework (change‑control, component performance evaluation). |
| 독립형 SW 사용적합성 가이드라인 | Established guidance for standalone software usability validation. |

*No specific identifier (e.g., K‑number, FDA 510(k) number) appears in the source excerpts – verify separately if needed.*

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Recommended Action |
|-------------------|---------------------|
| **Unclear classification** – evidence suggests potential upgrade to 3등급 (e.g., primary therapeutic function). | Escalate to senior RA/MD for re‑classification review and possible shift to “전문허가”. |
| **Incomplete KGMP certification or out‑of‑date scope** | Suspend submission until a valid certificate is obtained; notify Quality Assurance. |
| **Missing Korean labeling / IFU** | Halt dossier assembly; request certified translation before proceeding. |
| **Absence of AI change‑control plan** | Require immediate development of PCCP; involve software engineering lead. |
| **No local clinical data justification** | Engage Clinical Affairs to generate a feasibility study or literature review; if unavailable, seek MFDS pre‑submission meeting. |
| **Cybersecurity documentation not aligned with MFDS guidance** | Conduct security gap analysis and remediate before filing. |

---

### 7. Regulatory Judgment  

Based on the available excerpts, the digital medical software should be classified as **MFNS Class II (2등급)** and pursued via a **허가 (full approval) submission**. The dossier must incorporate technical documentation, KGMP certification, Korean‑language labeling, usability validation per the independent‑software guideline, an AI‑specific change‑control plan, and a robust risk management & cybersecurity package.  

All identified gaps—particularly device description, intended use, standalone status, KGMP scope, local clinical evidence justification, and AI change‑management details—must be resolved prior to filing. Any of the listed escalation triggers should prompt immediate senior RA involvement.

---

**Peer Review Prompt**

> *@RA‑Colleague*: Please review the assumptions regarding (1) the applicability of the independent‑software usability guideline without a clear “standalone” statement, (2) the sufficiency of foreign clinical evidence for a Class II AI software under the 2025 Digital Medical Products Act, and (3) any additional Korean‑specific obligations that may have been omitted (e.g., mandatory post‑approval safety monitoring frequency). Highlight any jurisdictional gaps or source coverage issues.

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

### kb-eval-20260721-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9ae1fa70f2e54276", "source": "github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md", "source_hash": "e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c"} -->

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

> **Regulatory Draft – Impact of the Korean Digital Medical Products Act on an X‑ray Workstation Software + AI Image‑Analysis Module**

---

### 1. Device Overview (as described in the source)

| Element | Description |
|--------|-------------|
| **Product family** | X‑ray workstation software together with an AI‑driven image‑analysis module (potentially SaMD). |
| **Intended use** | Assist radiologists/clinicians in interpreting X‑ray images; provide diagnostic suggestions or quantitative measurements. |
| **Regulatory context** | Subject to the Digital Medical Products Act (디지털의료제품법) – effective 2025‑01‑24, with its implementation regulation (시행규칙) dated 2025‑02‑28. The act now mandates: <br>• Submission of usability (사용적합성) evidence.<br>• Expanded cybersecurity requirements (from 15 to 35 checklist items).<br>• An AI change‑management plan.<br>• Component‑level performance evaluation beginning in 2026. |

---

### 2. Classification & Submission Route

| Decision point | Reasoning |
|----------------|-----------|
| **Risk class** | Under the Digital Medical Products Act, software that provides diagnostic or treatment recommendations is typically placed in **Class II** (moderate risk) when it influences clinical decision‑making but does not directly dictate therapy. If the AI module performs autonomous diagnosis without clinician oversight, a **Class III** rating may be required. The source does not specify the exact intended user interaction; therefore, adopt a *conservative* approach and prepare for **Class III** submission (MFDS “high‑risk” pathway). |
| **Submission type** | For Class II – **“통합허가(통합신고)”** is possible if the hardware component already holds a MFDS licence. <br>For Class III – a **full “허가”** (approval) dossier is required, including technical documentation, risk management file, clinical evaluation, and post‑market surveillance plan. |
| **Reference** | Digital Medical Products Act (디지털의료제품법), 시행 2025‑01‑24; Implementation regulation (시행규칙) 2025‑02‑28 – classification criteria are set out in the act’s “분류” provisions. |

---

### 3. Required Evidence (per the new law)

| Evidence Category | Requirement under the Act | Status from source |
|-------------------|---------------------------|--------------------|
| **Usability / Human Factors** | Submission of *사용적합성* documentation proving that intended users can safely and effectively operate the software. The act makes this **mandatory** for all digital medical products. | **Missing** – G2 finding (“사용적합성 증빙 미대응”). |
| **Cybersecurity** | Expanded checklist (35 items). Must include vulnerability management, secure data transmission, authentication, audit‑logging, and a **Software Bill of Materials (SBOM)**. | SBOM referenced in source; cyber‑security items likely incomplete – G4 mapping not finished. |
| **AI Change‑Management Plan** | Continuous monitoring & control plan for AI model updates, including documentation of drift detection, re‑training procedures, and impact assessment on safety/efficacy. | Implicitly required by the act; no evidence presented in source. |
| **Component‑Level Performance Evaluation** | Beginning 2026, each functional component (e.g., image preprocessing, AI inference engine) must be evaluated individually for accuracy, robustness, and failure modes. | **Missing** – G3 finding (“구성요소 평가 적용 여부 미판정”). |
| **Clinical Evaluation** | Clinical data demonstrating safety/effectiveness in the Korean population. Foreign clinical evidence can be used if it meets MFDS equivalence criteria (e.g., same indication, comparable patient demographics). | No specific clinical evidence cited; needs to be generated or mapped. |
| **Regulatory Mapping (RA‑01 ~ RA‑20)** | Full traceability matrix linking each regulatory requirement to the submitted artifact. | **Missing** – G4 finding (“전수 매핑 미완”). |
| **SBOM** | Detailed inventory of all software components, versions, and licenses, uploaded through MFDS portal as per 009 (사이버보안) and 013 (SBOM) issues. | SBOM referenced in source; completeness not verified. |

---

### 4. Gaps / Missing Information (Action Items)

| Gap | Why it matters | Suggested remediation |
|-----|----------------|-----------------------|
| **Usability evidence (G2)** | Without proof of user suitability the dossier will be rejected outright under the act. | Conduct a formal human‑factors validation study per IEC 62366‑1, produce usability test reports in Korean. |
| **Component performance assessment (G3)** | Component‑level evaluation is now a statutory requirement; missing data prevents classification as compliant. | Define each software component; perform verification/validation per IEC 60812 and document results. |
| **Full RA‑01 ~ RA‑20 mapping (G4)** | MFDS requires a complete traceability matrix for inspection. Incomplete mapping will trigger deficiency letters. | Populate the matrix with links to design history file, risk management file, verification reports, etc., all in Korean. |
| **Cybersecurity checklist coverage** | The act’s 35‑item list includes SBOM, encryption standards, and incident response; incomplete items lead to non‑conformity findings. | Conduct a gap analysis against the MFDS cybersecurity guideline (issue 009) and remediate missing controls. |
| **AI change‑management plan** | AI model drift can introduce safety risks post‑approval; MFDS expects an ongoing control process. | Draft SOPs for monitoring performance metrics, trigger thresholds, re‑validation procedures, and document version control. |
| **Clinical evidence** | Required to substantiate safety/efficacy for the Korean market; foreign data alone may be insufficient. | Generate Korean clinical trial data or provide a justification for reliance on FDA/EU CE data with bridging study plan. |
| **Korean‑language labeling & IFU** | All user‑facing documents must be in Korean per MFDS labeling rule. | Translate UI, labels, and IFU; obtain linguistic validation. |

---

### 5. Risk Controls & Mitigation (aligned to ISO 14971)

| Hazard | Control (pre‑market) | Post‑market surveillance |
|--------|----------------------|---------------------------|
| **Misinterpretation of AI output** | • UI design with clear visual cues (confidence scores).<br>• Human‑in‑the‑loop requirement stated in Intended Use. | Collect adverse event reports related to diagnostic disagreement; periodic performance audits. |
| **Cybersecurity breach** | • Secure coding, regular penetration testing.<br>• SBOM for vulnerability tracking.<br>• Encryption of PHI at rest/in transit. | Continuous monitoring via MFDS cyber‑risk reporting portal; incident response plan activated on detection. |
| **AI model drift** | • Baseline performance validation using a representative Korean dataset.<br>• Defined change‑management thresholds. | Quarterly re‑evaluation of model outputs against ground truth; update plan submitted to MFDS when threshold exceeded. |
| **Usability errors** | • Human‑factors testing with target user group (radiologists).<br>• Error‐prevention features (e.g., confirm dialogs). | Post‑market usability feedback collected through surveys and field observations. |

---

### 6. Human‑Escalation Triggers

| Trigger | Who should be alerted | Action |
|---------|----------------------|--------|
| **Usability evidence not submitted by deadline** | RA lead & Project Manager | Pause submission; initiate rapid human‑factors test. |
| **Cybersecurity checklist score < 80 %** | CISO & Regulatory Affairs | Immediate remediation sprint; report to MFDS if any critical vulnerability is identified. |
| **AI performance degradation > 5 % from baseline** | AI development team, Clinical Lead | Trigger change‑management SOP; prepare supplemental evidence for MFDS. |
| **Regulatory mapping incomplete (RA‑01 ~ RA‑20) after internal audit** | QA Manager | Conduct gap‑fill workshop; issue “stop‑go” decision before dossier assembly. |
| **MFDS deficiency letter received** | Regulatory Affairs & Legal | Convene cross‑functional response team within 3 business days; prepare corrective action plan and revised submission package. |

---

### 7. References (established regulatory sources)

* 디지털의료제품법, 시행일 2025‑01‑24.  
* 디지털의료제품법 시행규칙, 시행일 2025‑02‑28.  
* MFDS “디지털의료제품 정보 포털” (emedi.mfds.go.kr).  
* 국가법령정보센터 – 「디지털의료제품법」.  
* Korean MFDS cybersecurity guidance (Issue 009) and SBOM guidance (Issue 013).  
* IEC 62366‑1: Medical device usability engineering.  
* ISO 14971: Application of risk management to medical devices.  

*(All references are drawn from publicly available Korean regulations; no case‑specific identifiers were present in the source excerpts.)*

---

### 8. Peer Review Prompt

> **To a fellow RA colleague:** Please review this draft and challenge any assumptions made about (a) the expected risk class for an AI‑enabled X‑ray workstation, (b) the completeness of the listed evidence requirements under the Digital Medical Products Act, and (c) potential jurisdictional gaps such as Korean‑language labeling or local clinical data needs that may have been overlooked. Suggest additional sources or clarification points needed before finalizing the submission plan.

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

### kb-eval-20260721-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "691fd991ed827a72", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

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

> **Regulatory Draft – Digital Medical Products Act (디지털의료제품법) Impact Assessment**

---

### 1. Applicable Legal Framework  

| Element | Reference |
|---|---|
| **Law** | 디지털의료제품법 (법률 제 20139호, 시행일 2025‑01‑24)【1002132727008468922】 |
| **Enforcement Decree** | 대통령령 제 35219호 (2025‑01‑23 제정, 2025‑01‑24 시행)【1002132727008468922】 |
| **Enforcement Regulation** | 총리령 제 1958호 (2025‑02‑28 시행)【1002132727008468922】 |
| **Regulatory Authority** | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과【1002132727008468922】 |
| **Key Sub‑regulations (고시)** | - “디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정”<br>- “분류 및 등급 지정 규정”<br>- “디지털의료기기 제조 및 품질관리 기준”<br>- “디지털의료기기 전자적 침해행위 보안 지침(안)”【1002132727008468922】 |
| **Recent Guidance (2024‑2025)** | - 디지털치료기기 임상시험 설계 가이드라인 (2024‑12) – relevance = 낮음, 적용 대상 = DTx 전용<br>- 생성형 AI 의료기기 허가·심사 가이드라인 (2025‑01) – relevance = 중, 적용 대상 = AI 영상 분석 모듈<br>- 독립형 디지털의료기기SW 사용적합성 가이드라인 (2025‑01) – relevance = 높음, 적용 대상 = 콘솔 SW, 뷰어 SW<br>- 의료기기 사이버보안 허가·심사 가이드라인(개정) (2025‑01‑10) – relevance = 높음, 적용 대상 = 네트워크 연결 기기 전체<br>- 디지털의료기기 전자적 침해행위 보안 지침(안) (2025‑01) – relevance = 높음, 적용 대상 = SBOM 관리 포함【1077225675205822581】 |

---

### 2. Product Scope & Intended Use  

| Question | Answer |
|---|---|
| **Is the product a SaMD / AI‑based medical device?** | Yes – falls under “AI 영상 분석 모듈” or “콘솔 SW/뷰어 SW” depending on UI and integration level (see relevant 2025‑01 guidelines). |
| **Primary Intended Use** | Clinical decision support for imaging interpretation (AI‑based) *or* standalone digital therapeutic (DTx) – to be clarified by the sponsor. |

---

### 3. Classification & Submission Route  

| Step | Determination | Rationale / Reference |
|---|---|---|
| **Risk Class** | **Class III** (medium–high risk) for AI‑based diagnostic support that influences treatment decisions, or **Class II** if the function is limited to information provision without direct therapeutic impact. The MFDS “분류 및 등급 지정 규정” (sub‑regulation) provides the decision tree; AI‑based image analysis typically lands in Class III when it directly affects clinical management. | MFDS classification rules (KGMP‐aligned) – see “디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정”. |
| **Submission Type** | - **Class III → 허가 (approval)**  <br>- **Class II → 인증/신고 (certification or notification)** depending on whether the device is “전기·전자‑제어형” vs. “소프트웨어 전용”. | MFDS approval vs. certification pathways are delineated in the same 고시. |
| **Foreign Evidence Acceptance** | - FDA 510(k) / PMA, CE Marking, or OECD‑aligned non‑clinical data can be used *provided* they satisfy Korean language translation and local clinical relevance (MFDS periodically expands accepted foreign evidence – latest notice to be verified). | MFDS practice under the Digital Medical Products Act; see recent guideline updates (2025‑01 “생성형 AI 의료기기 허가·심사 가이드라인”). |

**Action:** Confirm exact class via MFDS classification matrix once intended use and risk impact are finalized.

---

### 4. Required Evidence Package  

| Category | Minimum Requirement (Korean law/guideline) | Notes / Gaps |
|---|---|---|
| **Technical Documentation** | - Design Dossier (설계서), Software Description, Architecture Diagram, Verification & Validation reports <br> - Use‑related risk analysis per IEC 62304 and ISO 14971 (Korean translation required). | No specific “validation plan” excerpt found – verify sponsor’s documentation. |
| **Non‑clinical (Bench) Data** | • Performance evaluation (accuracy, sensitivity/specificity) using representative data sets. <br>• Security & resilience testing per “디지털의료기기 전자적 침해행위 보안 지침(안)” (SBOM management required). | Specific test protocol format not described in source – confirm with the 2025‑01 cyber‑security guideline. |
| **Clinical Evidence** | • Local clinical trial data *or* an accepted foreign clinical evaluation report that has been Korean‑translated and meets MFDS “임상시험 설계 가이드라인” (relevance = 낮음 for DTx, but higher for AI diagnostics). <br>• Post‑market surveillance plan. | No local clinical study identifier appears in source – **no specific identifier found in source — verify separately**. |
| **Quality Management System** | • KGMP certification of manufacturing site (ISO 13485‑based) with MFDS inspection record. | Confirm that the manufacturer holds a current KGMP certificate. |
| **Labeling & IFU** | • All labeling, user manuals, and software instructions must be in Korean (including risk information, intended use, contraindications). <br>• CE/US labels are optional but must be accompanied by Korean equivalents. | No language‑specific excerpt provided – treat as mandatory per MFDS regulation. |
| **Software Lifecycle & Post‑Market Surveillance** | • Conformity to “독립형 디지털의료기기SW 사용적합성 가이드라인” (high relevance) for UI/UX validation.<br>• Cybersecurity maintenance plan per 2025‑01 cyber‑security guideline. | No explicit reference to post‑market data collection frequency – sponsor must define. |

---

### 5. Missing Information & Open Items  

| Item | Why It Matters | Current Status |
|---|---|---|
| **Exact Intended Use Statement** | Drives classification and clinical evidence scope. | Not present in excerpt – sponsor must provide. |
| **Local Clinical Data or Accepted Foreign CE/510(k) Reference** | Required for high‑risk AI devices unless a waiver is granted. | No identifier found – **no specific identifier found in source — verify separately**. |
| **KGMP Certificate Number & Inspection Report** | Mandatory for any device entering Korean market. | Not excerpted – request from sponsor. |
| **SBOM (Software Bill of Materials) Management Plan** | Required under “디지털의료기기 전자적 침해행위 보안 지침(안)”. | No detail in source – request documentation. |
| **Risk Management File (ISO 14971)** | Needed for class‑II/III devices to demonstrate mitigation of identified hazards. | Not shown – sponsor must submit. |
| **Korean Language Translation Verification** | All submission documents, labeling and IFU must be Korean‑language compliant. | Not covered in excerpt – confirm translation quality. |

---

### 6. Core Risk Controls (per MFDS & International Standards)  

1. **Algorithm Transparency & Explainability** – Document model architecture, training data provenance, version control.  
2. **Performance Validation** – Independent test set reflecting Korean patient demographics; statistical analysis per “AI 영상 분석 모듈” guidance.  
3. **Cybersecurity Hardening** – SBOM, regular vulnerability scanning, secure update mechanism (per 2025‑01 cyber‑security guideline).  
4. **Usability Engineering** – Conform to the “독립형 디지털의료기기SW 사용적합성 가이드라인” for UI validation with Korean end‑users.  
5. **Post‑Market Surveillance** – Real‑world performance monitoring, adverse event reporting system aligned with MFDS 시판후조사 요구사항.

---

### 7. Human‑Escalation Triggers  

| Trigger | Condition | Escalation Action |
|---|---|---|
| **Unclear Classification** | Intended use or risk impact ambiguous after sponsor clarification. | Prompt senior RA (Class III specialist) for MFDS pre‑submission consultation. |
| **Missing Local Clinical Evidence** | No Korean clinical data and no accepted foreign CE/510(k) reference is provided. | Escalate to regulatory strategy lead to decide on conducting a local pilot study or seeking a waiver. |
| **KGMP Certification Gap** | Manufacturer lacks current KGMP certificate or inspection report. | Pause submission; engage quality assurance team to obtain certification before proceeding. |
| **Non‑Compliance with Security Guideline** | SBOM or cyber‑security plan absent or inadequate. | Immediate review by MFDS‐designated cybersecurity expert; may require redesign of update mechanism. |
| **Labeling/IFU Language Deficiency** | Korean translations incomplete or inconsistent. | Route to linguistic compliance specialist for verification before dossier finalization. |

---

### 8. Summary Judgment  

- The product is subject to the **Digital Medical Products Act** and its accompanying 고시 and guidelines.
- **Likely classification:** Class III (high‑risk AI diagnostic) → **허가 (approval)** pathway, unless a limited “information only” claim can be substantiated, which would shift it to Class II → 인증/신고.
- The sponsor must furnish **complete technical documentation**, **KGMP certification**, **Korean‑language labeling**, **SBOM & cybersecurity controls**, and **clinical evidence** (local or adequately translated foreign data).  
- Current gaps: precise intended use, local clinical data reference, KGMP certificate details, SBOM management plan, Korean translation verification.

Proceed to collect the missing items; if any trigger above occurs, elevate to senior RA/strategy lead before dossier assembly.

---

### 9. Peer‑Review Prompt  

> **@RA‑Peer:**  
> Please review the assumptions made regarding risk classification (Class III vs. Class II), the applicability of the 2025‑01 AI‑specific guidance, and any potential jurisdictional gaps—particularly around the use of foreign clinical evaluation reports under the Digital Medical Products Act. Highlight any overlooked Korean regulatory nuance or missing citation that could affect the submission strategy.

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

### kb-eval-20260721-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "5d021441b22a8fa1", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "a20110f67bbd98b35d188d8a2fd8d816a95754663f6515d8828b632ceb3d72e5"} -->

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

> **Regulatory Assessment Draft – X‑ray System under the Digital Medical Device Act (디지털의료제품법)**  

---

### 1. Scope & Applicability  
The project contains four software–hardware elements (Generator firmware, Detector firmware, Acquisition Workstation software, Image post‑processing + AI module) that interact with an X‑ray imaging chain. According to the cross‑verification table (source [1]), the following components are deemed *potentially* subject to the Digital Medical Device Act:

| Component | Applicability under 디지털의료제품법 |
|-----------|-----------------------------------|
| Generator firmware | **X** – hardware‑control only, no network connection → not covered. |
| Detector firmware   | △ – network connectivity *could* trigger coverage; pending clarification. |
| Acquisition Workstation SW | ○ – standalone operation, networked, AI‑capable → **covered** (SaMD). |
| Image post‑processing + AI module | ○ (if applicable) – SaMD + AI → **covered**. |
| DICOM transfer / PACS interface | △ – communication function; requires boundary analysis to decide if independent software. |

Consequently, the **Acquisition Workstation and the AI‑enabled post‑processing module are prima facie Digital Medical Devices (SaMD) under the Act**. The Detector firmware may become covered if future design changes add networked functions.

---

### 2. Classification & Submission Route  

| Item | Regulatory Class (디지털의료제품법) | Recommended Korean MFDS pathway |
|------|----------------------------------|---------------------------------|
| Acquisition Workstation SW (stand‑alone, AI) | **Class III** – SaMD with AI that influences diagnostic interpretation (MFDS “AI/ML‑enabled SaMD” guidance). | **허가 (Approval)** – Full technical dossier required. |
| Image post‑processing + AI module | **Class II–III** (depends on risk of clinical decision impact; default to Class III for safety margin). | **허가** if classified as III; otherwise **신고** for Class II, but we recommend the more stringent pathway given AI involvement. |
| Detector firmware (if networked) | Potentially **Class II** (hardware‑control with connectivity). | **신고** – Notification sufficient for low‑to‑moderate risk devices, pending final determination. |

*No specific MFDS case identifier (e.g., 510(k), predicate number) appears in the source excerpts; therefore:*

> **no specific identifier found in source — verify separately**

---

### 3. Required Evidence Package  

| Evidence Category | Requirement under 디지털의료제품법 / MFDS guidance | Status (based on source) |
|-------------------|----------------------------------------------------|--------------------------|
| **Software Bill of Materials (SBOM)** | Mandatory per “SBOM 3‑axis requirements” referenced in the cross‑validation report (source [2]). | SBOM to be produced for all software components. |
| **Risk Management File** (ISO 14971) | Required for every class; AI‑specific risk controls must be documented (MFDS AI SaMD guidance). | Not yet supplied – gap. |
| **Software Design Documentation** (IEC 62304) | Needed for SaMD; includes architecture, verification & validation plans. | Partial (generator firmware excluded). |
| **Clinical Evaluation** | Korean clinical data required for Class III devices unless a sufficient foreign CE/FDA clearance is acceptable under the latest MFDS notice expanding accepted foreign evidence (see MFDS “foreign clinical evaluation report” allowance). The source does not confirm such foreign clearance. | Missing local clinical evidence – gap. |
| **Cybersecurity Assessment** (IEC 82304‑1, FDA Cybersecurity Guidance) | Required for networked software; SBOM assists but a dedicated risk assessment is mandatory. | Not mentioned – gap. |
| **Radiation Safety Documentation** (방사선 안전관리규칙) | For any X‑ray related hardware, compliance with the “진단용 방사선 안전관리 규칙” must be demonstrated. Generator firmware excluded; Detector firmware may fall under it if networked. | Partial – only a reference to the rule in source [2]; detailed evidence not shown. |
| **Korean Language Labeling & IFU** | All labeling, instructions for use (IFU), and safety information must be provided in Korean per MFDS labeling regulations. | Not addressed in source – gap. |
| **KGMP Facility Certification** | Required for any hardware manufacturing (Generator, Detector). Software development can be performed under a certified quality system (ISO 13485). | Generator excluded; Detector status unclear – gap if networked. |

---

### 4. Missing Information & Immediate Actions  

1. **Clarify Detector Firmware Scope** – Determine whether the firmware will include network communication functions that would make it fall under 디지털의료제품법.  
2. **Finalize AI Functionality Definition** – Document intended clinical use of the AI module (diagnostic support vs. image enhancement) to lock classification.  
3. **Develop Complete SBOM** for all software artefacts (including third‑party libraries).  
4. **Prepare Full Risk Management File** with AI‑specific hazard analysis, mitigation strategies, and post‑market surveillance plan.  
5. **Obtain Clinical Evidence** – Either conduct a Korean clinical study or secure an acceptable foreign clinical evaluation report in line with the latest MFDS notice on foreign evidence acceptance.  
6. **Cybersecurity Dossier** – Perform threat modeling, penetration testing, and provide a cybersecurity risk mitigation plan.  
7. **Generate Korean‑language Labeling & IFU** – Include usage instructions, safety warnings, and disposal guidance.  
8. **Confirm KGMP Certification** for any hardware that will be produced in Korea (Detector if networked).  

---

### 5. Core Risk Controls (to be reflected in the dossier)  

| Hazard | Control Measure |
|--------|-----------------|
| Inappropriate AI diagnostic output | Independent validation set, continuous performance monitoring, explainability documentation. |
| Unauthorized remote access to workstation or firmware | Secure authentication, encrypted communication (TLS), regular patching per SBOM updates. |
| Radiation over‑exposure due to software error | Interlock logic verified per IEC 60601‑2‑33; periodic safety checks built into firmware. |
| Data integrity loss during DICOM/PACS transfer | End‑to‑end checksum verification, audit logs, compliant with Health‑IT standards (KISA). |
| Software malfunction leading to misinterpretation of images | Redundant processing pathways, graceful degradation, user alerts per ISO 14971 risk control hierarchy. |

---

### 6. Citations  

- **Digital Medical Device Act (디지털 의료제품법)** – governing authority for SaMD and AI‑enabled medical software in Korea.  
- **MFDS “AI/ML‑Enabled SaMD Guidance”** – classification of AI‑based software into Class III when influencing clinical decisions.  
- **방사선 안전관리규칙** – statutory safety management rules for diagnostic X‑ray devices.  
- **ISO 14971:2020**, **IEC 62304:2006**, **IEC 82304‑1** – internationally recognized standards referenced by MFDS for risk management, software life‑cycle, and cybersecurity.  

*No case‑level identifiers (e.g., predicate numbers) were identified in the provided source material.*

---

### 7. Human‑Escalation Triggers  

| Condition | Escalation Action |
|-----------|-------------------|
| **Unresolved classification** for Detector firmware after analysis → Notify senior RA manager to seek MFDS pre‑consultation. |
| **Absence of local clinical evidence** for a Class III device → Immediate escalation to Clinical Development lead and possibly the Project Sponsor for study planning. |
| **KGMP certification gap** for any hardware component intended for Korean market → Escalate to Quality Assurance for facility audit scheduling. |
| **Cybersecurity risk not mitigated** (e.g., open ports, outdated libraries) → Elevate to IT Security team and suspend submission preparation until remedied. |
| **Regulatory notice update** (new MFDS acceptance of foreign clinical data) that could alter evidence strategy → RA lead must review and decide on using foreign data; escalation if decision impacts timeline. |

---

### 8. Reusable RA Judgment (Memory Outcome)  

> For X‑ray imaging systems incorporating networked software and AI, the **Acquisition Workstation** and any **AI‑enabled post‑processing module** are classified as **Class III SaMD under the Digital Medical Device Act**, requiring full 허가 with a comprehensive dossier (SBOM, risk management, clinical evaluation, cybersecurity assessment, Korean labeling, and KGMP confirmation for related hardware). The **Detector firmware** is **conditionally covered**; its final classification hinges on whether network functions are implemented. Missing evidence areas—clinical data, complete SBOM, cybersecurity documentation, and Korean‑language labeling—must be addressed before dossier submission. Escalate any ambiguity in classification, evidence gaps, or regulatory notice changes to senior RA leadership for prompt resolution.

---

### 9. Peer Review Prompt  

> **Colleague – please review:**  
> • The assumption that the Acquisition Workstation and AI module default to Class III—are there MFDS precedents that could justify a lower class?  
> • Whether the cross‑validation table sufficiently determines “networked” status for the Detector firmware, or if additional design details are needed.  
> • If any recent MFDS notices (post‑April 2026) expand acceptance of foreign clinical data that we might leverage, and whether those notices have been captured in our source set.  
> • Identification of any Korean‐specific documentation (e.g., “기술규격서” or “안전성 검증 보고서”) that is currently missing from the evidence checklist.

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

1. Chunk `418096885713027360`

> ## 3. 본 프로젝트 X-ray 제품의 디지털의료제품법 해당성 판정(잠정) | 구성 | 디지털의료기기 해당? | 근거 | |------|---------------------|------| | Generator 펌웨어 | X | HW 제어 전용, 비연결 | | Detector 펌웨어 | △ | 네트워크 연결 시 해당 가능 | | Acquisition Workstation SW | ○ | SW 단독 조작·네트워크 연결·AI 가능성 | | 영상 후처리·AI 분석 모듈 | ○ (해당 시) | SaMD + AI 분류 | | DICOM 전송·PACS 연계 | △ | 통신 기능, 독립형 SW 경계 검토 |

2. Chunk `437336887721584251`

> --- doc-id: LOG-2026-04-22_SBOM_디지털의료제품법_정합성 title: 교차검증 보고서 — SBOM 3축 요구사항 & 디지털의료제품법 정합성 type: Report category: 12_교차검증_보고서 purpose: 교차검증 보고서 — SBOM 3축 요구사항 & 디지털의료제품법 정합성 관련 문서 last-review: 2026-04-22 --- # 교차검증 보고서 — SBOM 3축 요구사항 & 디지털의료제품법 정합성 일자: 2026-04-22 대상 문서: - `03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md` (v0.1) - `01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md` (v0.1) - `01_법규_규제/01_국내_MFDS/진단용방사선_안전관리규칙_개정이력.md` (v0.1) - 기존: `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md`, `06_문서_기록관리/SOP-UDI-001_UDI_통합관리_초안.md`

### kb-eval-20260721-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "7009c1806e2d0a1d", "source": "github:holee9/MD-process/issue-drafts/947_AUDIT_디지털의료제품법_법률번호_20722_광범위_자매재발.md", "source_hash": "fed73ac605f6674c04cc5029490b7b167f60ab56f7464d148e79c94381f53999"} -->

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

> **Regulatory Draft – Impact of the Digital Medical Products Act (디지털의료제품법) on a Software‑Based Medical Device**

---

### 1. Applicable Legal Framework  

| Regulation | Current Status in Source | Comment |
|------------|--------------------------|---------|
| **Digital Medical Products Act (디지털의료제품법)** – “Law No. 20722” | Cited repeatedly (e.g., “법률 제20722호”) but the source explicitly flags this citation as potentially erroneous (Audit #930). | The exact law number must be verified against the official MFDS Gazette before any formal submission. |
| **Medical Device Act (의료기기법)** | Governs all medical devices, including software classified as a “medical device.” | Standard reference – no verification needed. |
| **KGMP (Korean Good Manufacturing Practice) Regulation** | Required for the manufacture of class II–III devices and for any device that uses a certified QMS. | Established regulation (MFDS Notice No. 2023‑XX, see KGMP guidelines). |
| **Related MFDS Notices on Foreign Evidence Acceptance** | MFDS periodically expands acceptance of FDA/CE evidence for certain software categories. The exact notice number is not provided in the source and must be retrieved from the MFDS website before reliance. | Verify separately. |

---

### 2. Device Classification & Submission Route  

| Attribute | Determination Basis |
|-----------|---------------------|
| **Intended Use** (e.g., diagnostic decision support, AI‑based risk prediction) | If the software provides *clinical information* that influences patient management, it falls under “Software as a Medical Device” (SaMD). |
| **Risk Class** (per MFDS Classification Rule 9 for software) | - **Class I** – General wellness or low‑risk informational apps. <br> - **Class II** – Software that provides data interpretation but does not drive therapy. <br> - **Class III** – Software that directly drives therapeutic decisions or performs autonomous diagnosis. |
| **Proposed Class for this Device** | Based on the description (AI performance evaluation required, cyber‑security dossier demanded) → *likely Class II* (or Class III if autonomous). |
| **Submission Pathway** | - **Class I:** Notification (신고). <br> - **Class II/III:** Approval (허가) with full technical file and KGMP certification. |

*Citation:* MFDS Medical Device Classification Rule 9 (Software as a Medical Device) – established regulatory reference.

---

### 3. Required Evidence Package  

| Evidence Category | Specific Requirements | Status in Source |
|-------------------|-----------------------|------------------|
| **Technical Documentation** | - IEC 62304 (software life‑cycle). <br> - IEC 82304‑2 (health software safety). <br> - Detailed design and verification records. | Mentioned as “SW수명주기” documents; not yet supplied. |
| **Cybersecurity Dossier** | - Threat analysis, protection measures, incident response plan.<br> - SBOM (Software Bill of Materials) pre‑check. | Source flags need for SBOM (“SBOM 사전점검”) – missing. |
| **AI Performance Evaluation** | - Dataset description, training/validation methodology, bias mitigation, explainability report. | Required; “AI 성능평가 문서” noted as top priority in audit. |
| **Clinical Evidence** | - Local clinical data *or* accepted foreign clinical evaluation (FDA 510(k) / CE). <br> - Must align with the latest MFDS notice on foreign evidence for software. | No specific clinical data referenced; need to source appropriate studies. |
| **QMS Documentation** | - Design‑development, risk management (ISO 14971), post‑market surveillance plans. <br> - KGMP compliance certificates for manufacturing sites. | Audit #930 identified QMS folder omission (design / cybersecurity folders missing). |
| **Regulatory References** | - Correct citation of the Digital Medical Products Act (law number & article). | Law number currently flagged as possibly incorrect; requires legal verification. |

---

### 4. Gaps / Missing Information (as highlighted by source excerpts)

1. **Correct Statutory Citation** – “법률 제20722호” is flagged as a mis‑citation. Obtain the official law number and article(s) that govern digital medical products.  
2. **Complete QMS Documentation** – Current archive limited to “QMS 폴더”; design / development and cybersecurity folders are absent (Audit #930).  
3. **SBOM & Pre‑Check Evidence** – No SBOM provided; required per Digital Medical Products Act’s software supply‑chain transparency clause.  
4. **AI Validation Report** – Needs a dedicated AI performance evaluation dossier for MFDS review.  
5. **Cybersecurity Risk Management Plan** – Must be included with evidence of lifecycle monitoring.  
6. **Foreign Clinical Evidence Acceptance Notice** – Identify the latest MFDS notice that permits reliance on FDA/CE data for this device class; citation pending.

---

### 5. Recommended Risk Controls (aligned with Korean expectations)

| Control | Standard / Guideline | Rationale |
|--------|----------------------|-----------|
| **Risk Management Process** | ISO 14971 (Korean adoption) | Mandatory for all Class II/III devices. |
| **Software Life‑Cycle Processes** | IEC 62304 | Required for SaMD; covers planning, development, maintenance. |
| **Cybersecurity Measures** | MFDS Guidance on Medical Device Cybersecurity (2024) + NIST CSF mapping | Addresses audit focus on “cyber보안” documents. |
| **AI Transparency & Explainability** | IMDRF AI/ML SaMD Guideline (adopted by MFDS) | Supports AI performance evaluation and post‑market monitoring. |
| **Post‑Market Surveillance (PMS)** | MFDS PMS requirements for software (periodic safety update, incident reporting) | Ensures ongoing compliance after market entry. |
| **Supply‑Chain Transparency** | SBOM requirement per Digital Medical Products Act | Enables traceability of third‑party components. |

---

### 6. Citations

- **Established Regulatory References (no verification caveat):**  
  - MFDS Medical Device Classification Rule 9 – software risk class determination.  
  - KGMP Regulation – manufacturing compliance for Class II/III devices.  
  - ISO 14971, IEC 62304, IEC 82304‑2 – technical standards incorporated by reference in Korean law.

- **Case‑Level Identifiers (appear verbatim in source):**  
  - **Audit #930** – identified missing QMS folders and potential mis‑citation of the law number.  
  - **Plan #935** – suggested automation rule “법률 제[0‑9]+호” for cross‑reference scanning.  
  - **“법률 제20722호”** – cited in multiple source lines (e.g., L20, L13) but flagged as possibly erroneous; treat as a *suspect* identifier pending legal verification.

- **No specific FDA 510(k), EU CE, or internal case numbers were present in the excerpts.** → *no specific identifier found in source — verify separately.*

---

### 7. Human‑Escalation Triggers  

| Trigger | When to Escalate | Who Should Review |
|---------|------------------|-------------------|
| **Unverified statutory citation** – any reference to “법률 제20722호” must be confirmed before submission. | Immediate (legal & regulatory lead). |
| **Audit #930 findings not fully addressed** – missing design / cybersecurity QMS folders, incomplete evidence of SBOM and AI performance. | Senior RA manager + QA/QC lead. |
| **Absence of a current MFDS foreign‑evidence acceptance notice** – before relying on FDA/CE data for clinical justification. | Regulatory affairs director & external counsel (if needed). |
| **High‑risk classification (Class III) determination uncertainty** – if the AI algorithm is autonomous or directs therapy. | Clinical affairs + senior RA for risk re‑assessment. |
| **Cybersecurity dossier incomplete** – any gaps in threat analysis or incident response plan. | Information security officer & regulatory compliance lead. |

---

### 8. Reusable RA Judgment (Memory Record)

- **Lesson:** When source material flags a statutory citation as possibly erroneous (e.g., “법률 제20722호” in Audit #930), do **not** treat the cited number as definitive; instead, flag for independent legal verification and document the uncertainty explicitly.  
- **Action Pattern:** Add a cross‑reference rule (“법률 제[0‑9]+호”) to automated scanning tools (Plan #935) to catch similar mis‑citations early in future dossier reviews.

---

### 9. Peer Review Prompt  

> *@RA‑Peer:* Please examine the assumptions made regarding device risk class, the completeness of the required evidence list, and any jurisdiction‑specific gaps—particularly the need for a verified Digital Medical Products Act citation and the applicability of MFDS foreign‑evidence notices. Highlight any items that may have been overlooked or require additional source validation.

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
