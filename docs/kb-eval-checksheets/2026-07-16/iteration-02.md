# KB Eval Checksheet - 2026-07-16 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260716-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_us-001", "iteration": 2, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "a7cfbbe928232419", "source": "github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md", "source_hash": "19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf"} -->

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

> **Regulatory Draft – QMSR §820.30 De‑precation Follow‑up**  
*Prepared for internal QA/QMS team – 2026‑07‑17*  

---

### 1. Bottom‑Line Recommendation
- **Classification & submission route:** The change is a **quality‑system amendment only**; it does **not alter the device’s FDA classification or 510(k) pathway**. Continue with the existing Class I/II/III designation and any pending submissions unchanged.  
- **Primary corrective action:** Consolidate all design‑control references to **21 CFR 820.10(c) incorporating ISO 13485:2016 §7.3**, eliminating every residual citation of the now‑reserved **§820.30** across SOPs, Forms and matrices.

---

### 2. Required Evidence for Closure  

| Item | What It Must Show | Source / Acceptance Criteria |
|------|-------------------|------------------------------|
| Updated SOP‑AIGOV‑001 (front‑matter) | Front‑matter cites **“§820.10(c) → ISO 13485:2016 §7.3”** only; no §820.30 references | Document control log, version number, change‑control record |
| Revised Design‑Control SOPs / Forms / Matrices (e.g., `00_프로젝트관리/문서_매트릭스.md`) | All occurrences of “§820.30 …” removed or replaced with the unified citation | Grep report (search pattern “820\.30”) showing **0 hits** |
| Training records | Personnel trained on the new citation pathway and documentation requirements | Attendance sheets, LMS completion certificates dated ≥ 2026‑07‑01 |
| audit #921 re‑verification report | Independent QA reviewer repeats grep and confirms zero residual §820.30 citations | Signed QA verification sign‑off |

---

### 3. Missing / Incomplete Information  

1. **Residual citation inventory** – The current grep only identified the presence of “§820.30” but did not enumerate each document still containing it. Provide a full list (document title, line numbers).  
2. **Change‑control justification** – A brief rationale linking the regulatory amendment (eCFR 21 CFR 820 QMSR effective 2026‑02‑02) to the internal redesign of citations is absent from SOP‑AIGOV‑001 change log.  
3. **Risk assessment update** – The Design‑Control risk matrix still references “§820.30” as a control element; this must be revised to reference §820.10(c) and ISO 13485:2016 §7.3.

---

### 4. Risk Controls & Impact if Unresolved  

| Risk | Likelihood (Post‑Remediation) | Severity | Control / Mitigation |
|------|------------------------------|----------|---------------------|
| FDA Form 483 for non‑conformity to QMSR | Low (if residual citations remain) | Moderate–High (potential 483 → Warning Letter) | Complete citation purge, document control audit trail |
| Delayed product release due to QMS inspection hold | Low to Medium (depends on inspection timing) | High (time‑to‑market impact) | Ensure all design‑control documents are fully compliant before next FDA interaction |
| Internal audit repeat failure (audit #921) | Very Low (once grep shows 0 hits) | Moderate | Perform a second independent verification before closeout |

---

### 5. Citations (verbatim from source)

- **Audit reference:** *audit #921 (2026‑06‑26)* – documented the need to correct SOP‑AIGOV‑001 front‑matter.  
- **Regulatory text:** *eCFR 21 CFR Part 820 (QMSR, effective 2026‑02‑02) §820.30 is Reserved; design‑control requirements are now solely in §820.10(c) incorporating ISO 13485:2016 §7.3.*  
- **Internal SOP:** *SOP‑AIGOV‑001* – front‑matter revised to “§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30 is Reserved).”

> No specific 510(k) predicate identifiers appear in the source excerpts — verify separately if device‑level submission documentation is needed.

---

### 6. Human‑Escalation Triggers  

| Trigger | Who Escalates | Deadline |
|---------|---------------|----------|
| **Any residual “§820.30” reference** after the primary grep remediation | Lead QMS Engineer → RA Manager | Immediate (within 1 business day) |
> *Rationale:* Even a single stray citation violates the mandatory consolidation and could be flagged on FDA inspection.  

| Trigger | Who Escalates | Deadline |
|---------|---------------|----------|
| **Greps return ≥ 1 hit** during re‑verification (audit #921 follow‑up) | QA Lead → Senior Director of Regulatory Affairs | 48 hours after verification attempt |
| **Training completion < 95 %** for all design‑control staff | Training Manager → HR & RA leadership | End of current quarter |

---

### 7. Peer Review Prompt  

> *“Please review the above remediation plan and challenge: (a) the completeness of our citation‑removal inventory; (b) whether any jurisdiction‑specific (state, EU MDR) cross‑references could be impacted by the same amendment; and (c) if additional evidence (e.g., updated Design History File entries) should be required before we close audit #921.”*  

---  

**Lesson Recorded for Reuse:**  
When eCFR redesignates a quality‑system subpart as “Reserved” (e.g., §820.30), **all internal design‑control references must be collapsed to the single statutory path (here §820.10(c) → ISO 13485:2016 §7.3).** A systematic grep across all SOPs, Forms and matrices is mandatory; any residual citation constitutes a non‑conformity that triggers immediate escalation. This precedent should be stored as a reusable QMSR‑compliance judgment for future regulatory amendment rollouts.

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

### kb-eval-20260716-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_us-002", "iteration": 2, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "8ce24ca4b172110f", "source": "github:holee9/MD-process/issue-drafts/921_AUDIT_SOP-AIGOV-001_QMSR_820_30_Reserved_인용부정확.md", "source_hash": "36a0683dda1f189f95c3bba8f11be7917c7ed24fdf703b490573ae5ef6cf0b16"} -->

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

> **Regulatory Draft – QMSR / Design‑Control Readiness (Daily Growth Case)**  

---

### 1. Scope & Applicability  
- **Regulation:** FDA Quality Management System Regulation (QMSR) – **21 CFR 820**, specifically the revised incorporation‑by‑reference clause **§ 820.10(c)**.  
- **Reference Standard:** ISO 13485:2016 **§ 7.3** (Design and Development).  

*All FDA‑cleared or approved medical devices (Class I–III) that are subject to 21 CFR 820 must comply with the updated QMSR reference.*  

---

### 2. Classification / Submission Route  
- This SOP amendment **does not create a new device classification**; it is a **process‑level regulatory requirement** affecting all existing and future submissions (510(k), PMA, De Novo, etc.).  
- **Submission impact:** For any pending or future submission, the design‑control evidence must now be demonstrably aligned with ISO 13485:2016 §7.3 via incorporation by reference as mandated in **§ 820.10(c)**.

---

### 3. Required Evidence of Compliance  

| Evidence | Description | Acceptance Criteria |
|----------|------------|---------------------|
| **Updated SOP(s)** (e.g., SOP‑DHF‑001, SOP‑DT‑001, SOP‑DVV‑001) | Front‑matter must show: `applicable:` → **`FDA QMSR §820.10(c) → ISO 13485:2016 §7.3`** (or the alternative wording shown in source). | Exact wording and citation present; version control updated; cross‑referenced to ISO clause. |
| **Design‑Control Traceability Matrix** | Mapping of each FDA design‑control requirement (820.30) to the corresponding ISO 13485:2016 §7.3 sub‑clauses. | 100 % coverage; any gaps >5 % must be justified. |
| **Incorporation‑by‑Reference Filing Evidence** (if applicable) | Documentation that FDA has been notified of the incorporation by reference (e.g., submission cover letter, CFR amendment request). | Confirmation of FDA acknowledgment or a formal declaration in the registration record. |
| **Risk Management Integration** | Records showing ISO 14971 risk management activities are linked to design‑control outputs and reflected in the QMSR system. | All identified hazards have corresponding control measures documented; risk acceptability criteria met. |
| **Training & Competency Logs** | Evidence that personnel responsible for design‑control tasks have been trained on the revised SOP language and ISO 13485:2016 requirements. | Training completion ≥95 % of assigned staff; competency assessments passed. |
| **Internal Audit Report (QMSR)** | Post‑implementation audit confirming that the new clause is operational, with findings and corrective actions logged. | No *critical* non‑conformances; all *major* findings addressed within 30 days. |

---

### 4. Missing / Unverified Information  

| Item | Gap | Action |
|------|-----|--------|
| **Device‑specific impact analysis** – which product families are directly affected by the SOP change? | Not identified in source. | Conduct a portfolio‑wide QMSR impact assessment (target completion ≤ 2 weeks). |
| **Formal FDA incorporation‑by‑reference record** – has the organization submitted the required notice? | No evidence provided. | Verify with Regulatory Affairs Manager; if absent, prepare and submit a “Letter of Incorporation” per 21 CFR 820.10(c). |
| **Versioned SOP repository link** – location where updated SOPs are stored (e.g., QMS portal URL) | Not supplied. | Document storage path; ensure change‑control approval workflow is captured. |
| **Quantitative gap analysis of design‑control mapping** – % of 820.30 requirements currently mapped to ISO 13485:2016 §7.3 | No data presented. | Perform a matrix audit; report gaps >5 % for remediation. |
| **Risk Management plan alignment** – explicit linkage between ISO 14971 and the new QMSR clause | Not described. | Update risk management file to reference ISO 13485:2016 §7.3 design‑control outputs. |

---

### 5. Key Risk Controls (per ISO 13485:2016 §7.3 & FDA QMSR)  

1. **Design Input Control** – Verify that all user needs and regulatory requirements are captured, reviewed, and approved before design work begins.  
2. **Design Review** – Conduct documented reviews at defined milestones; include cross‑functional representation (RA, QC, Engineering).  
3. **Design Verification & Validation** – Perform testing against inputs; retain protocols, reports, and acceptance criteria.  
4. **Change Management** – All design changes must follow SOP‑DT‑001 with impact analysis on risk, performance, and regulatory status.  
5. **Document Control** – Ensure the revised SOP front‑matter is immutable and traceable through change control logs.  
6. **Training & Awareness** – Mandatory annual refresher on QMSR §820.10(c) implications.  

---

### 6. Citations (direct from source)

- **FDA QMSR § 820.10(c)** – incorporation‑by‑reference clause (source excerpt [1]).  
- **ISO 13485:2016 § 7.3** – Design and Development requirements (source excerpt [1]).  
- **BSI Compliance Navigator “The New FDA 21 CFR Part 820 – QMSR”** – reference for Tier‑2 supplemental guidance (source excerpt [2]).

*No other specific identifiers (e.g., predicate numbers, case IDs) appear in the provided excerpts.*

---

### 7. Human‑Escalation Triggers  

| Trigger | Escalation Target | Timeline |
|---------|-------------------|----------|
| **≥20 % uncovered gaps** in design‑control to ISO 13485:2016 mapping after matrix audit. | Regulatory Affairs Manager (RA‑Mgr) | Immediate (within 1 business day). |
| **Lack of FDA incorporation‑by‑reference evidence** when required for a pending submission. | Director, Regulatory Affairs & Legal Counsel | Immediate; hold any submission until resolved. |
| **Critical non‑conformance** identified in post‑implementation QMSR audit (e.g., missing design verification records). | Quality Assurance VP + RA‑Mgr | Within 24 hours; initiate CAPA. |
| **Training compliance <90 %** for staff on revised SOPs after 30‑day rollout. | HR Learning & Development Lead | Within 48 hours; schedule remedial training. |

---

### 8. Peer Review Prompt  

> **To RA peers:**  
> Please review the assumptions above regarding (1) the applicability of § 820.10(c) to all device classes, (2) the completeness of the evidence list for demonstrating incorporation by reference, and (3) any jurisdiction‑specific gaps (e.g., state‑level quality system requirements or FDA guidance not captured here). Highlight missing sources, suggest additional documentation, or flag potential misinterpretations of the source excerpts.  

--- 

*Prepared by:* **Mike – US Regulatory Affairs Specialist**  
*Date:* 2026‑07‑17  



--- 

**Final lesson (RA judgment log):**  

> *When FDA QMSR updates shift incorporation‑by‐reference from § 820.30 to § 820.10(c), every design‑control SOP must be revised to explicitly cite the new clause and ISO 13485:2016 §7.3, and a cross‑functional mapping matrix is required to prove coverage before any submission.*

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

### kb-eval-20260716-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_us-003", "iteration": 2, "matched_keywords": ["PMA"], "profile_id": "ra-us", "scenario_id": "85724102009d170d", "source": "github:holee9/MD-process/issue-drafts/229_02_SOP-PMA-001_프로세스모니터링_KPI매트릭스_8.1_8.2.5_8.5.1.md", "source_hash": "ed59b6fa057ba788ee178280f4428111be880e61d706e22f9efd9624278f41bd"} -->

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

> **Regulatory Draft – QMSR / Design‑Control Readiness for SOP‑PMA‑001 (Process Monitoring & Analysis)**  

| Item | Assessment |
|------|------------|
| **Device classification / submission route** | The artifact is a Quality Management System (QMS) procedure, not a medical device. No FDA product classification or 510(k)/De Novo/PMA filing applies. The focus is compliance with the FDA Quality Management System Regulation (QMSR) 21 CFR 820 (effective Feb 2026). |
| **Regulatory expectations** | • Demonstrate that the SOP satisfies ISO 13485 §§8.1, 8.2.5, 8.5.1 and FDA QMSR §§820.250 (statistical techniques) & §820.100 (CAPA). <br>• Map each process KPI to a measurable quality objective and show the closed‑loop flow: **KPI → MR input → CAPA trigger** as required by ISO 13485 and FDA QMSR. |
| **Required evidence to close gaps** | 1. **Completed KPI matrix** (9 processes × 3 dimensions = 27 cells) with defined measurement frequency, statistical control limits, and ownership.<br>2. **Statistical analysis plan** showing use of SPC, Pareto, Ishikawa for each KPI; sample size calculations where applicable.<br>3. **Thresholds / trigger criteria** for every KPI that automatically generate a CAPA or Management Review (MR) entry.<br>4. **Audit trail**: records of KPI data collection, analysis outputs, and documented CAPA actions linked to specific non‑conformances.<br>5. **Management Review minutes** demonstrating linkage from KPI trends → MR decisions → resource reallocation.<br>6. **Mapping documentation** confirming alignment with ISO 13485 §§8.1/8.2.5/8.5.1, FDA QMSR §§820.250/§820.100, and EU MDR Art.10(9)(j) (if marketed in the EU). |
| **Missing / partial elements (as per source)** | • §8.1 – “적합성·효과성·개선 모니터링·분석·개선 계획” is only *partial*.<br>• §8.2.5 – Process performance monitoring & CAPA trigger is *partial*.<br>• §8.5.1 – Quality policy, objectives, audit, analysis, corrective actions and MR effectiveness improvement are *partial*.<br>• KPI thresholds and responsibility assignments not yet defined (only “정량” mentioned).<br>• Formal linkage documentation between KPI → MR → CAPA is noted as a **TODO** in the SOP checklist. |
| **Risk controls / mitigation strategy** | 1. **Statistical Process Control (SPC)** per FDA QMSR §820.250 to detect process drift early.<br>2. **CAPA trigger matrix** aligned with KPI “out‑of‑limit” events (ISO 13485 §8.2.5).<br>3. **Management Review (MR) escalation** when recurring CAPAs exceed defined frequency or impact critical quality attributes.<br>4. **Resource reallocation protocol** activated by MR to address systemic deficiencies.<br>5. **Periodic internal audit** of KPI data integrity and CAPA closure effectiveness (ISO 13485 §8.5.1). |
| **Citations from source material** | • ISO 13485 §§8.1, 8.2.5, 8.5.1 – cited directly in the SOP checklist.<br>• FDA QMSR §§820.250 (use of statistical techniques) & §820.100 (CAPA) – referenced in the regulatory mapping table.<br>• EU MDR Art.10(9)(j) – listed as a parallel requirement for multinational manufacturers. |
| **Human‑escalation triggers** | • **KPI breach** → automatic generation of a CAPA ticket; required sign‑off by Process Owner and QMS Manager.<br>• **CAPA non‑closure within defined timeframe** → escalation to Senior Management Review (MR) and possible Resource Reallocation Decision.<br>• **Trend of repeated KPI failures** (≥ 2 occurrences in 3 months) → trigger a formal **Management Review** meeting and potential revision of quality policy/objectives. |
| **Recommended immediate actions** | 1. Complete the pending items for §§8.1, 8.2.5, 8.5.1 – assign owners & due dates.<br>2. Populate all KPI cells with numeric limits, sampling plans, and statistical control rules.<br>3. Build the **KPI → MR → CAPA** linkage in the QMS software (e.g., electronic CAPA system).<br>4. Conduct a mock audit focusing on the three ISO/FDA clauses to verify readiness before next external assessment. |
| **Human‑escalation trigger for reviewer** | If any of the above “missing” elements cannot be resolved within 30 days, or if evidence of statistical methodology is inadequate, **escalate to QMS Director** for risk‑based decision on compliance status and possible FDA/ISO audit notifications. |

---

### Peer Review Prompt
*Please review this draft and challenge:*

1. **Assumptions about completeness** – Are we presuming the KPI matrix will satisfy §820.250 without seeing actual statistical plans?
2. **Source coverage** – Does the excerpt adequately support the identified missing elements, or are we extrapolating beyond what is documented?
3. **Jurisdictional gaps** – Have we omitted any other regulatory provisions (e.g., 21 CFR 820.30 design‑control requirements) that could affect overall QMS readiness for a device‑related submission?

---

### Reusable RA Judgment (Lesson Record)

> *When assessing internal QMS SOPs for FDA QMSR compliance, map each ISO 13485 §8.x clause to the corresponding 21 CFR 820 sections (e.g., §§820.100 & 820.250). Verify that KPI definitions include explicit statistical control limits, ownership, and trigger rules that feed directly into CAPA and Management Review processes. Any partial status in regulatory checklists must be closed with documented evidence of data collection, analysis methodology, and audit trail before the QMSR effective date (Feb 2026) to avoid non‑conformances during inspection.*  

*(Recorded via `honcho_conclude` for future reuse.)*

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

### kb-eval-20260716-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "67a0ba7fa7d4fc3a", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md", "source_hash": "8049315bab61421790bb62b12e868c8a33a7bdd1f4b989a98ed1c61790bf7f53"} -->

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

> **Regulatory Draft – QMSR & Design‑Control Readiness Assessment**

---

### 1. Bottom‑Line Recommendation  

| Item | Current Assessment | Action |
|------|-------------------|--------|
| **Device classification / submission route** | Indeterminate – no device specifics provided. Assume the most common pathway for a non‑exempt Class II device: **Traditional 510(k) (Substantial Equivalence)**. If the device is novel with no predicate, plan for **De Novo**. | Obtain intended use, technological description, and potential predicates to finalize route. |
| **QMSR compliance status** | Mapping of 21 CFR 820 clauses to ISO 13485 sections is documented (see source [1]). Core design‑control requirement (§820.30) and several supplemental controls are noted as “보완” (to be supplemented). | Complete the indicated supplementary sections in the Quality Management System (QMS) before submission. |
| **Key evidence required for 510(k)** | • Device Description & Labeling<br>• Predicate comparison matrix (if applicable)<br>• Design History File (DHF) including risk analysis (ISO 14971) and design controls (§820.30)<br>• Verification/validation test data (bench, animal, clinical as needed)<br>• Sterility, biocompatibility, software documentation (if relevant) | Gather and cross‑reference each deliverable against the QMSR mapping table. |
| **Missing / Incomplete Information** | • Device name, classification code, intended use<br>• Predicate device 510(k) number or reference<br>• Completed DHF sections for: design inputs, outputs, verification, validation, change control, and design transfer<br>• Risk Management File (ISO 14971) linked to design controls<br>• Labeling & Packaging Control procedures (§820.25) fully fleshed out | Prioritize collection of the above before QMSR audit or FDA submission. |
| **Risk Controls (per QMSR mapping)** | • **Design‑control maintenance** – §820.30, non‑exempt devices must retain full design control.<br>• **Labeling & packaging management** – §820.25 (refer to source [1] “보완”).<br>• **Record management** – §820.35 additional requirements for traceability.<br>• **Device marking inspection** – new §820.45 requirement (source [1]).<br>• **Complaint handling** – expanded §820.198 (source [1]) ensures post‑market feedback loop.<br>• **Management review input** – §820.20 addition (source [1]) to capture QMSR‑specific metrics. | Integrate these controls into SOPs, work instructions, and electronic QMS tools; verify through internal audit. |
| **Regulatory citations (from source)** | • 21 CFR Part 820 – eCFR version effective 2026‑02‑02 (source [2])<br>• Federal Register notices: **2024‑01709** (enactment) and **2025‑21955** (technical amendment) (source [2])<br>• FDA Compliance Program **7382.850** (source [2]) | Use these citations in all QMSR‑related documentation and correspondence with the FDA. |
| **Human‑escalation triggers** | 1. Any “보완” (supplement) item in the QMSR mapping remains incomplete after the next scheduled internal audit.<br>2. Absence of a complete DHF or risk management file when the submission deadline is < 60 days away.<br>3. FDA observation letters, Form 483, or Warning Letters relating to design‑control gaps.<br>4. Discrepancies between labeling/packaging SOPs and actual practice discovered during mock inspections. | Escalate to RA Lead / Regulatory Project Manager immediately; consider engaging a regulatory consultant if timeline risk > 2 weeks. |

---

### 2. Structured Action Plan

| Phase | Tasks (Owner) | Due |
|-------|---------------|-----|
| **A – Information Capture** | • Define device name, intended use, and classification (Product Team).<br>• Identify predicate device(s) and collect 510(k) numbers (Regulatory Analyst). | +2 weeks |
| **B – QMSR Gap Closure** | • Complete “보완” sections for §820.30, §820.25, §820.35, §820.45, §820.198 per mapping table (Quality Engineer).<br>• Update management‑review inputs (§820.20) with QMSR metrics (QA Manager). | +4 weeks |
| **C – Design History File Assembly** | • Populate DHF modules: design inputs/outputs, verification, validation, risk analysis, change control, design transfer (Design Engineer/RA).<br>• Link each module to corresponding QMSR clause. | +6 weeks |
| **D – Evidence Generation** | • Perform required verification/validation testing; compile reports (Testing Lab).<br>• Draft labeling & packaging specifications aligned with §820.25 (Regulatory Writer). | +8 weeks |
| **E – Internal Audit & Readiness Review** | • Conduct QMSR‑focused audit using mapping checklist (Internal Auditor).<br>• Document findings; remediate any residual gaps. | +10 weeks |
| **F – Submission Preparation** | • Prepare 510(k) or De Novo dossier, embed QMSR compliance statements and citations.<br>• Submit to FDA; retain all supporting documentation for potential inspection. | +12 weeks |

---

### 3. Peer‑Review Prompt  

> **To RA Team Member:**  
> Please review the assumptions in this draft, especially the defaulting to a traditional 510(k) pathway without known predicate information. Verify that the source excerpts fully cover the QMSR mapping items cited, and flag any jurisdiction‑specific gaps (e.g., state‑level requirements, post‑market surveillance obligations under §820.80). Also assess whether additional identifiers (e.g., specific 510(k) numbers, FDA docket IDs) are needed for a complete submission package.

--- 

**End of Draft – Ready for Human Validation and WP Commenting**

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

### kb-eval-20260716-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_us-005", "iteration": 2, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "859740700145052c", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

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

> **Regulatory Draft – QMSR & Design‑Control Readiness**

---

### 1. Bottom Line
- **U.S. market suitability cannot rely on ISO 13485:2016 §4.2.5 alone.**  
  FDA’s new Quality Management System Regulation (QMSR) – 21 CFR §820.35 – imposes *additional* record‑management requirements that must be satisfied before any 510(k), De Novo, or other submission can be considered complete.  

- **Action:** Confirm device classification and intended use; then map your current QMS to both ISO 13485 §4.2.5 **and** the FDA‑specific clauses in 21 CFR §820.35 (see Source [1]).

---

### 2. Classification & Submission Route  
| Item | Current Status (based on source) | Required Action |
|------|-----------------------------------|-----------------|
| Device Class (I, II, III) | *Not provided* – cannot be deduced from the QMS excerpt. | Obtain **intended use**, **technological description**, and **clinical risk profile** to determine classification per 21 CFR §860. | 
| Likely submission | *Undetermined* – depends on class. | If Class II → **510(k)** (traditional, special or abbreviated).<br>If novel Class III → **PMA** or consider **De Novo** if no predicate. |

> **Human‑Escalation Trigger #1:** If classification cannot be resolved within 5 business days of this brief, escalate to the product development lead for a targeted device‑risk workshop.

---

### 3. Required Evidence (QMSR‑focused)

| Evidence | FDA Requirement | ISO 13485 Reference | Gap Note |
|----------|----------------|---------------------|---------|
| **Design History File (DHF)** – §820.30 (design controls) | Mandatory for Class II/III devices | Covered by ISO 13485 7.3.3 | Must include design input, output, verification, validation, transfer. |
| **Device Master Record (DMR)** – §§820.181‑820.184 | Required record of production specifications | ISO 13485 4.2.5 (record management) | QMSR adds *additional* fields (e.g., traceability to software version, UDI generation). |
| **Record Management SOP (F‑QMSR‑REC‑001)** – see doc‑id *FDA_QMSR_820.35_vs_ISO13485_4.2.5* (Source [2]) | Must satisfy §820.35 supplemental record requirements (e.g., retention periods, electronic audit trails) | ISO 13485 §4.2.5 provides baseline but not the FDA‑specific additions. |
| **Electronic Records & Signatures** – 21 CFR Part 11 compliance | Required for any digital DHF/DMR elements | Not addressed in ISO 13485 | Implement validated electronic system; generate audit logs. |
| **UDI Implementation** – 21 CFR §830 | Mandatory for most devices marketed after Sept‑2014 | ISO 13485 does not specify UDI format | Establish labeling and database process. |
| **Adverse Event Reporting System (MAUDE)** – 21 CFR §803 | Must be in place before market launch | Not covered by ISO 13485 | SOP for PSUR/PSUR‑001 required. |
| **Risk Management File** – ISO 14971 + FDA risk control guidance | Demonstrate identification, analysis, mitigation of hazards | ISO 13485 §7.1 (risk management) | Align risk control measures with QMSR record requirements. |

> **Human‑Escalation Trigger #2:** Any missing or non‑validated electronic record system must be flagged to IT/validation lead within 3 days.

---

### 4. Missing Information & Immediate Action Items

| Missing Item | Why Needed | Next Step |
|--------------|------------|-----------|
| **Intended Use Statement** | Drives classification, labeling, and risk analysis. | Obtain from product manager; include in DHF. |
| **Predicate Device(s) (if pursuing 510(k))** | Required for substantial‑equivalence argument. | Conduct a predicate search; capture 510(k) numbers. |
| **Performance Testing Data (bench, animal, clinical)** | Core of safety & effectiveness evidence. | Draft test plan; align with FDA guidance for device type. |
| **Software Description & Validation (if applicable)** | Required under §820.30(c) & Part 11. | Create Software Development Plan and verification report. |
| **UDI Allocation Strategy** | Needed for labeling, submission, post‑market tracking. | Assign issuing agency; map to DMR fields. |
| **Complete SOP Library** – especially SOP‑DOC‑001, SOP‑TRC‑001, SOP‑FSCA‑001 (Source [2]) | Demonstrates QMS maturity and compliance with QMSR supplemental requirements. | Compile or update SOPs; ensure sign‑off. |

> **Human‑Escalation Trigger #3:** If any of the above items remain unresolved beyond 10 business days, elevate to RA Director for risk‑based prioritization.

---

### 5. Key Risk Controls (aligned with QMSR)

| Control | FDA Basis | Implementation Note |
|---------|-----------|----------------------|
| **Design Input Review & Traceability** | §820.30(b) | Use a bidirectional traceability matrix linking inputs → outputs → verification/validation activities. |
| **Document Change Management** | §820.40 & §820.100 (CAPA) | Enforce controlled change procedures; record in DMR and DHF. |
| **Electronic Audit Trail** | Part 11 §§11.10‑11.30 | Automated logs for all DHF/DMR modifications; periodic review. |
| **UDI Verification** | §830.7 | Verify barcode readability, database capture at each manufacturing step. |
| **CAPA System** | §820.100 | Capture deviations from design verification/validation; root‑cause analysis per ISO 14971. |
| **Supplier Qualification** | §820.50 | Maintain Supplier Evaluation Records; include risk rating for critical components (e.g., X‑ray tube). |

---

### 6. Citations

- **FDA QMSR §820.35** – additional record‑management requirements (Source [1]).  
- **ISO 13485:2016 §4.2.5** – baseline record management (Source [1]).  
- **Document ID:** *FDA_QMSR_820.35_vs_ISO13485_4.2.5* – comparative guidance and SOP references (Source [2]).

> No specific 510(k) numbers, predicate identifiers, or case IDs appear in the source excerpts.

---

### 7. Peer‑Review Prompt  

*“@RA‑Peer: Please review the assumptions made regarding classification determination and the completeness of the QMSR‑focused evidence list. Are there any FDA guidance documents or recent Federal Register notices (post‑Feb 2026) that we have omitted, especially relating to X‑ray system record management? Additionally, confirm whether the SOP references (e.g., SOP‑DOC‑001) adequately cover all supplemental §820.35 requirements.”*

---

### 8. Reusable RA Judgment (Honcho Record)

**Lesson:** *When evaluating QMS readiness under the 2026 FDA QMSR transition, ISO 13485:2016 §4.2.5 provides a necessary but not sufficient baseline. Explicitly map each ISO requirement to its FDA §820.35 counterpart and flag any supplemental record‑management obligations (electronic audit trails, UDI linkage, Part 11 compliance). Always request device‑specific classification data before proposing a submission pathway.*  

*(Recorded for future reuse via `honcho_conclude`.)*

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

### kb-eval-20260716-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b66b7c0dd94542fb", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

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

### kb-eval-20260716-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e0a28ad294f2e438", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

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

> **Regulatory Draft – Preliminary MDR 2017/745 Assessment (PMS & PMCF Planning)**  

| **Item** | **What the Notified Body (NB) will need to see** | **Current status from source excerpts** | **Evidence gaps / actions required** |
|----------|--------------------------------------------------|-----------------------------------------|----------------------------------------|
| 1. **Device classification** | • Apply Article 51 + Annex VIII rules, selecting the highest‑risk rule that matches the device’s intended purpose. <br>• Manufacturer bears “self‑classification” responsibility (Article 51). <br>• If doubt persists, seek advice from the Competent Authority (CA) or MDCG Manual on Borderline and Classification (latest 2023‑09 v2.1.1). | • Source [2] confirms that classification follows Article 51 + Annex VIII, self‑classification, sequential rule application, and reference to the MDCG manual. | • **Missing:** explicit statement of the device’s intended use, list of applicable Annex VIII rules, and the resulting class (I/IIa/IIb/III). <br>• **Action:** Draft an *Intended Use* section and map it against each Annex VIII rule to justify the final class. |
| 2. **Conformity‑assessment route** | • Class I: self‑declaration (Annex IV). <br>• Classes IIa/IIb: QMS assessment under Annex IX *or* type‑examination + verification (Annex X + XI). <br>• Class III: Type‑examination (Annex X) plus product verification (Annex XI). | Not directly stated in the excerpts. | • **Missing:** final class determines the route. <br>• **Action:** Once classification is fixed, select the appropriate Annex pathway and prepare the related documents (QMS certificate, type‑examination report, etc.). |
| 3. **Clinical Evaluation Report (CER)** | • Must comply with **Annex XIV Part A** (updated via Article 61). <br>• Includes state‑of‑the‑art literature review, clinical data from investigations or post‑market sources, and a risk‑benefit conclusion. | Source [1] lists “CEP + CER (Article 61, MDR Annex XIV)”. | • **Missing:** the actual CER draft, list of clinical investigations, literature search strategy, and summary of clinical data. <br>• **Action:** Compile a full CER per Annex XIV Part A; include justification for any reliance on equivalence (if used). |
| 4. **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | • PMCF plan must follow **Annex XIV Part B**. <br>• Includes objectives, methodology, data‐collection schedule, responsibilities, and criteria for success/failure. <br>• A subsequent PMCF evaluation report demonstrates that the plan has been executed and outcomes reassessed. | Mention of “CEP + CER” only; no explicit reference to Annex XIV Part B in the excerpts. | • **Missing:** a written PMCF Plan (scope, endpoints, sample size) and evidence of execution. <br>• **Action:** Draft a PMCF Plan per Annex XIV Part B, link it to the CER, and schedule interim updates. |
| 5. **Post‑Market Surveillance (PMS) System** | • System required by **Article 83** (general PMS). <br>• PMS plan (Art. 84), periodic safety update report – PSUR for Class IIb/III (Art. 86) or PMS report for lower risk (Art. 85). <br>• Include trend analysis, vigilance handling, field corrective actions, and UDI traceability. | Source [1] lists “시판 후 감시” (post‑market surveillance), PSUR, Vigilance (MDR Art.87). | • **Missing:** fully documented PMS system (processes, responsibilities) & a draft PSUR schedule. <br>• **Action:** Develop the PMS System per Articles 83–86; integrate with UDI database (see UDI portal reference) and vigilance workflow. |
| 6. **Unique Device Identification (UDI)** | • Assign UDI‑DT according to MDR Annex II, register on EUDAMED **(Art. 33‑39)** and national UDI portal (e.g., udiportal.mfds.go.kr). <br>• Ensure GUDID entry for US market if applicable. | Source [1] mentions “UDI”, “UDI 포털 (udiportal.mfds.go.kr)”, “GUDID”. | • **Missing:** allocated Device Identifier (DI), Production Identifier (PI) structure, and evidence of registration in EUDAMED. <br>• **Action:** Generate UDI‑DT, submit to national portal and EUDAMED; capture barcode specifications. |
| 7. **Vigilance / Adverse Event Reporting** | • Follow MDR **Art. 87** (incident reporting) plus any applicable national legislation (e.g., Korean “의료기기법 §31”). <br>• Align with FDA 21 CFR 803/MedWatch where relevant for exported devices. | Source [1] lists “Vigilance (MDR Art.87), PSUR”. | • **Missing:** documented procedure for incident detection, evaluation, and reporting timelines; designated contact points. <br>• **Action:** Draft a Vigilance SOP aligned with Art. 87 & local law; map to PMCF triggers. |
| 8. **Authorized Representative (AR)** | • Must be established per **Article 11** for non‑EU manufacturers. <br>• AR listed on the EU Declaration of Conformity and in EUDAMED. | Source [1] lists “Authorized Rep.”, “US Agent (510(k) 면제 외)”, “Authorized Representative (Art.11)”. | • **Missing:** name, address, registration number of the EU‑based AR; proof of AR’s willingness to act on behalf of the manufacturer. <br>• **Action:** Confirm AR selection and include in technical documentation. |
| 9. **Technical Documentation (TD)** | • Annex II (general) & Annex III (specific). <br>• Include device description, labeling, risk management file (ISO 14971), clinical evaluation, PMCF plan, PMS system, UDI info, and post‑market data. | Not directly covered in excerpts. | • **Missing:** full TD pack. <br>• **Action:** Populate each Annex II/III section; cross‑reference to the CER, PMCF, and PMS documents prepared above. |
| 10. **Fees & NB Contract** | • Fees vary by class and scope (e.g., NB contract €10 k‑€100 k+). <br>• US FDA MDUFA IV fees listed for reference only. | Source [1] provides fee ranges (“NB 계약 기반 (€10,000~€100,000+)”). | • **Missing:** budget approval and signed NB service agreement. |

---

### Key Regulatory Citations (per Fixed‑Rule mapping)

| Requirement | Regulation / Annex | Source |
|-------------|-------------------|--------|
| Clinical Evaluation Report (CER) | **Annex XIV Part A** – updated via **Article 61** | [1] “CEP + CER (Article 61, MDR Annex XIV)” |
| PMCF Plan & Evaluation Report | **Annex XIV Part B** | No specific identifier found in source — verify separately |
| PMS System, plan, PSUR / report | **Art. 83** (system), **Art. 84** (plan), **Art. 85/86** (report) | [1] “시판 후 감시 … PSUR … Vigilance (MDR Art.87)” |
| Classification rules | **Article 51** + **Annex VIII** | [2] “분류 원칙 (Article 51 + Annex VIII)” |
| Authorized Representative | **Art. 11** | [1] “Authorized Representative (Art.11)” |
| Vigilance (incident reporting) | **Art. 87** | [1] “Vigilance (MDR Art.87)” |
| UDI registration | **Art. 33‑39** (EUDAMED) – not in source but implied by “UDI 포털, GUDID” | No specific identifier found in source — verify separately |

---

### Human‑Escalation Triggers (Yellow‑Gate Actions)

1. **Unresolved Classification** – If the applicable Annex VIII rule cannot be definitively matched to the intended purpose, pause the submission and involve a senior RA or seek CA clarification.
2. **Missing Clinical Data** – Absence of primary clinical investigation data or insufficient literature for CER → trigger detailed gap analysis before NB review.
3. **PMCF Plan Not Aligned with CER** – Discrepancy between identified residual risks and PMCF objectives → escalate to the clinical affairs lead.
4. **PMS System Incomplete** – No documented process for trend analysis, field corrective actions, or PSUR schedule for Class IIb/III devices → halt NB audit preparation.
5. **UDI Not Registered in EUDAMED** – Failure to generate a valid UDI‑DT and submit to EUDAMED before Declaration of Conformity signing → pause labeling and market launch steps.
6. **Authorized Representative Not Confirmed** – Lack of signed AR agreement or missing Art. 11 documentation → stop final EU declaration signing.
7. **Fee/Contract Unfinalized** – NB contract not signed or budget not approved → delay submission of the technical file.

Each trigger should be logged in the project’s risk‑register and reported to the Project Lead for decision on whether to proceed, seek additional data, or re‑scope the device claim.

---

### Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions and evidence gaps identified above. In particular:  
> 1. Have we correctly interpreted the classification pathway given only the high‑level excerpt on Annex VIII rules?  
> 2. Are there any MDR articles or annexes not covered by our source excerpts that could affect the PMS/PMCF requirements for this device (e.g., specific provisions for software, combination products, etc.)?  
> 3. Does the list of required documentation align with the latest EUDAMED registration obligations (Art. 33‑39), or have we missed any mandatory fields?  
> 4. Are there jurisdiction‑specific considerations (Korean Medical Device Act §31, US FDA 21 CFR 803) that should be reflected in our vigilance and reporting plan beyond what is currently cited?  

Your feedback will be incorporated into the final technical documentation pack before we request a Yellow‑gate NB audit schedule.

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

### kb-eval-20260716-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c944e4d14fb0a40a", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee"} -->

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

1. Chunk `1138445053784347810`

> | PMS 항목 | 특화 내용 | |---|---| | 주요 위험 신호 | SW 오류로 인한 진단 오류, 데이터 손실, 사이버보안 취약점 | | 핵심 수집원 | SW 버그 리포트, 사이버보안 취약점 공개 DB (CVE, NIST NVD) | | PMCF 방법 | 사용성 평가 (IEC 62366), 실사용 에러 데이터 수집 | | 주요 표준 모니터링 | IEC 62304 개정, MDCG 2019-16 Rev.1 사이버보안, MDCG 2021-6 SaMD | | MFDS 특이사항 | 디지털의료제품법(2024.09.26 시행) 적용 여부 검토 [검증 필요] | ---

2. Chunk `1142345122918011337`

> ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (추정) | PMS Plan 의무 | 보고서 유형 | FDA 522 | MFDS 시판후조사 | |---|---|---|---|---|---| | **X-ray Detector** | Class IIa/IIb | **필수** | PSUR 2년/매년 | 해당 없음 (비이식형) | 신개발 시 3~4년 조사 | | **Handheld X-ray Source** | Class IIb | **필수** | PSUR 매년 | 해당 없음 (비이식형) | 신개발 시 4~6년 조사 | | **촬영실 GUI SW (SaMD)** | Class IIa (MDR §22) | **필수** | PSUR 2년 | 해당 없음 | 소프트웨어 신개발 시 해당 | ---

### kb-eval-20260716-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["EUDAMED"], "profile_id": "ra-eu", "scenario_id": "a7f9cbb5e3a5a13e", "source": "github:holee9/ra-project/01_규제지식베이스/EUDAMED_모듈별_등록_실무가이드.md", "source_hash": "62dd065b6b2edb9164049ee9ef2987e60ef5409d8f1f224f4e3cc01e1d61bc77"} -->

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

> **Regulatory Draft – Preliminary PMS / PMCF Outlook**  
*Prepared for internal review (Daily Growth – Run 2026‑07‑17, Scenario a7f9cbb5e3a5a13e)*  

---

### 1. Scope & Current Information Landscape
| Item | Source excerpt | Comment |
|------|----------------|---------|
| **UDI / Device Registration** | “EUDAMED UDI/DEV … Basic UDI‑DI … must be Globally Unique” – *Excerpt [2]* | Confirms that the device will need a Global‑Unique Device Identifier (UDI‑DI) and, where applicable, a UDI‑PI to be entered in **EUDAMED Module 2**. |
| **EUDAMED implementation schedule** | “2026‑05‑28 (4개 모듈)” – *Excerpt [1]* | Indicates that the four EUDAMED modules are slated for activation on 28 May 2026; the UDI/Device Registration module is therefore operational. |
| **Vigilance reporting location** | “Module 5 (~Q2 2027)” – *Excerpt [1]* | Vigilance (post‑market incident) data will be collected in EUDAMED Module 5 beginning Q2 2027. |

*No device‑specific attributes (intended purpose, technology, patient population, risk class, etc.) are present in the supplied excerpts.*  

---

### 2. Preliminary Classification & Conformity‑Assessment Route  
| Requirement | Current Status | Evidence Needed |
|-------------|----------------|-----------------|
| **Risk‑class determination** (Annex VIII) | *Indeterminate – device description missing* | • Intended medical purpose<br>• Anatomical/physiological site of application<br>• Duration of contact, invasiveness, etc. |
| **Conformity‑assessment route** (Annex IX / Annex X+XI) | *Cannot be selected until class is known* | • If Class I (non‑sterile, non‑measuring): self‑declaration & Annex IV DoC.<br>• If Class IIa/IIb/III: QMS assessment (Annex IX) and/or type‑examination (Annex X/XI) plus a **clinical evaluation** (CER – Annex XIV Part A). |
| **UDI requirement** | Required for all classes (MDR Art. 27 & Annex II‑2). | • Allocation of a Basic UDI‑DI from an approved issuing agency (GS1, HIBCC or ICCBBA) and entry in EUDAMED Module 2 (*see source [2]*). |

**Citation:** Classification rules are codified in **Annex VIII**; conformity‑assessment routes in **Annex IX** (QMS based) and **Annex X/XI** (type‑examination + product verification).  

---

### 3. Clinical Evidence Requirements  
| Item | MDR Reference | What Must Be Produced |
|------|----------------|-----------------------|
| **Clinical Evaluation Report (CER)** | *Annex XIV Part A* (updated via Art. 61) | • Systematic literature review of state‑of‑the‑art (SOTA).<br>• Clinical data from either a **clinical investigation** or **Equivalence** (if justified). |
| **Post‑Market Clinical Follow‑up (PMCF)** | *Annex XIV Part B* | • A written **PMCF Plan** describing objectives, methodology, timing and resources.<br>• The **PMCF Evaluation Report** summarising results and any corrective actions. |
| **Post‑Market Surveillance (PMS) System** | Art. 83 (system), Art. 84 (plan), Art. 85/86 (report/PSUR) | • PMS Plan appropriate to risk class.<br>• Periodic Safety Update Report (PSUR) for Class IIb/III or PMS reports for lower‑risk devices. |

**Note:** No clinical data have been provided; the CER and PMCF documentation will therefore be **incomplete** at this stage.

---

### 4. Missing Information – Gap Analysis  

| Gap | Why It Matters | Action Required |
|-----|----------------|-----------------|
| **Device description & intended use** | Determines risk class, equivalence claim, and clinical evidence scope. | Obtain the full Intended Purpose Statement and technical specifications from product development. |
| **Risk Management File (ISO 14971)** | Needed for classification justification, identification of residual risks, and to feed PMS/PMCF activities. | Deliver a completed Risk Management Plan & Report. |
| **Clinical data** (clinical investigation results or equivalence documentation) | Essential for the CER (Annex XIV Part A). | Compile pre‑market clinical evidence or conduct a clinical investigation where no valid equivalent exists. |
| **UDI issuance details** | Required for entry into EUDAMED Module 2; Basic UDI‑DI must be globally unique. | Choose an issuing agency (GS1/HIBCC/ICCBBA) and obtain the Basic UDI‑DI before submission. |
| **Manufacturer & economic‑operator registration** | Needed in EUDAMED Actor Module (SRN). | Register the legal manufacturer, authorized representative, and any importers/distributors in EUDAMED (per Art. 33‑39). |
| **PMS Plan** (Art. 84) and **PMCF Plan** (Annex XIV Part B) | Required for ongoing safety monitoring; must be aligned with risk‑management outcomes. | Draft PMS/PMCF plans now, referencing anticipated post‑market data sources (registries, literature, complaint handling). |
| **Vigilance procedures** (post‑Q2 2027) | Incident reporting will shift to EUDAMED Module 5; processes must be in place. | Define SOPs for Serious Incidents and Field Safety Corrective Actions, ready before Module 5 activation. |

---

### 5. Risk Controls – Preliminary Checklist  

| Control | Status (based on current info) | Comment |
|---------|-------------------------------|---------|
| **Design controls (ISO 13485 Clauses 7‑8)** | *Not demonstrated* | Need documented Design Dossier. |
| **Usability & Human Factors** | *Unknown* | Verify need for IEC 62366‑1 assessment depending on user interaction. |
| **Software validation (if applicable)** | *Unknown* | Must meet IEC 62304 if software is a component. |
| **Sterility/Packaging validation** | *Unknown* | Required for sterile devices (Annex VIII Rule 13) or packaging integrity. |
| **Labeling & IFU compliance** | *Pending* | Must reflect UDI, intended use and safety information per MDR Art. 23‑25. |

---

### 6. Citations & Reference Mapping  

| Topic | Correct Regulatory Source (per internal mapping) |
|-------|---------------------------------------------------|
| Clinical Evaluation Report (CER) | **Annex XIV Part A** (updated via Art. 61) – *not Annex IV* |
| PMCF plan / evaluation report | **Annex XIV Part B** – *not Annex III/VIII/XV* |
| PMS system / plan / report / PSUR | **Art. 83** (system), **Art. 84** (plan), **Art. 85/86** (report) – *not Annex VIII* |
| EU Declaration of Conformity | **Annex IV** – *not a CER‑related annex* |
| Classification rules | **Annex VIII** – *verify specific rule number once device is described* |
| Conformity‑assessment routes | **Annex IX** (QMS based) / **Annex X + XI** (type‑exam + verification) – *do not call them “Module A/B/C…”* |
| Products without intended medical purpose | **Annex XVI** – *not EUDAMED* |
| EUDAMED registration obligations | **Art. 33‑39** – *not Annex XVI* |

*No specific identifier (e.g., 510(k) number, predicate device ID) appears in the source excerpts; therefore:*

> **no specific identifier found in source — verify separately**

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason for Escalation | Recommended Owner |
|---------|----------------------|-------------------|
| **Absence of a definitive intended‑use statement** | Classification cannot be set; CE marking pathway undetermined. | Product Development Lead / Project Manager |
| **No risk‑management file (ISO 14971) available** | Risk controls and residual risk assessments missing – essential for PMS/PMCF. | QA/Risk Management Team |
| **Clinical evidence not supplied within 4 weeks of request** | CER will be incomplete; Notified Body will reject the Technical Documentation. | Clinical Affairs Lead |
| **UDI‑DI not allocated before EUDAMED Module 2 go‑live (28 May 2026)** | Device cannot be registered; shipment may be blocked in EU market. | Regulatory Operations |
| **PMS/PMCF plans not drafted prior to first device placement on the market** | Non‑compliance with Art. 84 & Annex XIV Part B – results in post‑market audit findings. | Post‑Market Surveillance Coordinator |
| **EUDAMED Actor registration (SRN) pending after 30 days of market entry** | Violates Art. 33‑39; leads to enforcement action. | Legal / Regulatory Affairs |

When any trigger materialises, the responsible party must raise a **Red‑Flag Ticket** in the project’s issue‑tracking system and notify the RA lead for immediate corrective planning.

---

### 8. Next Steps (Action Plan)

1. **Collect device‑specific data** – intended purpose, technology description, patient population, duration of use.  
2. **Perform preliminary risk classification** using Annex VIII rules once the above is received.  
3. **Engage an approved UDI issuing agency** to obtain a Basic UDI‑DI and set up EUDAMED Module 2 registration (target: before 28 May 2026).  
4. **Draft a Risk Management File (ISO 14971)** and map residual risks to PMS/PMCF activities.  
5. **Develop the Clinical Evaluation Plan** – identify comparable devices, perform literature search, decide whether a clinical investigation is needed.  
6. **Create PMS Plan (Art. 84) & PMCF Plan (Annex XIV Part B)** aligned with risk‑management outcomes; schedule periodic reviews.  
7. **Register economic operators in EUDAMED** (Actor Module – SRN) per Art. 33‑39.  

---

### 9. Peer‑Review Prompt  

> *Colleague, could you review the assumptions made above regarding the classification pathway and the timing of UDI registration? Specifically:  
> - Are we applying the correct Annex references for the conformity‑assessment routes given that no device class is yet known?  
> - Does our interpretation of the EUDAMED implementation dates (Module 2 operational 28 May 2026, Module 5 Q2 2027) align with the latest MDR guidance, or should we anticipate any transitional allowances?*  

Please challenge any gaps in source coverage (e.g., missing technical file elements) and highlight jurisdiction‑specific nuances that may affect the PMS/PMCF planning for this product.

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

### kb-eval-20260716-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "59120ec70443aebe", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13"} -->

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

> **Regulatory Draft – PMS / PMCF Planning (MDR Art.86)  
Prepared for internal review – “daily_growth_v1” case (Run‑date 2026‑07‑17)**  

---

## 1. Device Overview (information still required)

| Item | Required information | Current status |
|------|----------------------|----------------|
| **Device name / model** | Trade name, catalogue number, version | • not provided – *human input needed* |
| **Intended medical purpose** | Precise indication, patient population, mode of action | • not provided – *human input needed* |
| **Regulatory classification (MDR Rule 1‑22)** | Class I / IIa / IIb / III; reference rule number | • not provided – *human input needed* |
| **Conformity‑assessment route** | Annex IX (QMS) for Class IIa–III, Annex VIII/IV for low‑risk devices, or alternative routes (type‑examination + verification) | • cannot be assigned until classification is known |
| **CE marking status / Notified Body** | NB name, certificate number, expiry | • not provided – *human input needed* |

> **Action:** Supply the missing device details before finalising the technical documentation and submission plan.

---

## 2. Classification & Conformity‑Assessment Pathway (preliminary)

| Risk class (illustrative) | Likely MDR rule | Typical NB route |
|---------------------------|-----------------|------------------|
| Class I (non‑sterile, non‑measuring) | Rule 1 – low risk | Self‑declaration; Annex IV |
| Class IIa | Rules 2/3/4/5 … | Annex IX (QMS) – **Module B** |
| Class IIb / III | Rules 8‑22 | Annex IX (QMS) – **Modules C/D/E** (higher‑risk scrutiny) |

*When the exact rule is identified, update this table and reference the specific MDR annexes.*

---

## 3. Evidence Required for CE Marking (MDR)

| Evidence element | Legal source | What must be demonstrated |
|------------------|--------------|----------------------------|
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (Art.61 MDR) | State‑of‑the‑art clinical data, benefit–risk analysis, linkage to PMCF results |
| **PMCF Plan & PMCF Evaluation Report** | Annex XIV Part B (Art.86(1)(b)) | Ongoing data collection, objectives, methodology, schedule, and evaluation of safety/ performance post‑market |
| **Periodic Safety Update Report (PSUR)** | Art. 86 MDR (higher‑risk classes) | Summarised PMS results, sales/exposure data, trends, and updated risk analysis |
| **Post‑Market Surveillance (PMS) System / Plan** | Art. 83‑85 MDR | Structured process for gathering, analysing, and acting on post‑market information |
| **Risk Management File (RMF)** | ISO 14971 (referenced in MDR Annex I) | Identification of residual risks; PMCF findings must feed back to risk controls |

---

## 4. Content Extracted from Source Documents  

### 4.1 PMCF Result Linking – Art.86(1)(d)  
*(Source [1] – Section 7)*  

| Required table field (per source) | What is currently populated | Gap |
|-----------------------------------|-----------------------------|-----|
| **PMCF plan reference document** | `[문서번호, 버전]` placeholder | Actual document ID & version needed |
| **Current PMCF status** | `[진행 중 / 완료 / 계획 단계]` placeholder | Define the exact status (e.g., “In progress – 2024‑Q2”) |
| **Key PMCF results for the period** | `[요약 또는 "중간 데이터 없음"]` placeholder | Provide a concise summary of clinical data collected (e.g., adverse event rate, performance measures) |
| **Integration of PMCF outcomes into CER** | `[반영 여부, 반영 내용]` placeholder | Confirm whether and how results have been incorporated in the latest CER revision |
| **Next interim PMCF report due date** | `[YYYY‑MM‑DD]` placeholder | Insert the scheduled reporting date (must be ≤ 12 months for higher‑risk devices) |

> **Required Action:** Populate each row with concrete information; attach the referenced PMCF plan (Annex XIV Part B) and any interim analysis reports.

### 4.2 Sales & Patient Exposure Estimate – Art.86(1)(c)  
*(Source [2] – Section 2)*  

| Region | Units sold | Estimated patient exposure | Period |
|--------|-----------|----------------------------|--------|
| EU | `[수량]` | `[추정 수]` | `[기간]` |
| Korea | `[수량]` | `[추정 수]` | `[기간]` |
| USA | `[수량]` | `[추정 수]` | `[기간]` |
| Other | `[수량]` | `[추정 수]` | `[기간]` |
| **Total** | **[합계]** | **[합계]** | — |

*Guidance:* MDCG 2022‑21 §5.3 requires the methodology and assumptions to be fully documented when exact patient numbers cannot be obtained.  

> **Required Action:** Supply actual sales figures, expose the calculation method (e.g., device utilisation per procedure, market share assumptions) and reference this methodology in the PSUR.

---

## 5. Risk Controls & Feedback Loop

1. **Risk Management File (RMF)** – update residual risk list with any new findings from PMCF (Incidence of adverse events, performance drift).  
2. **Update to CER** – incorporate PMCF outcomes per Annex XIV Part A; justify whether the benefit–risk balance remains favourable.  
3. **PMS System Adjustments** – if trends indicate a need for corrective actions (field safety notices, design changes), trigger appropriate procedures under Art. 83‑85 MDR.  

*All updates must be traceable to the specific PMCF data point (e.g., “Increased sensor drift observed in 3 % of units; risk mitigation: software update v1.2 scheduled Q4‑2026”).*

---

## 6. Human‑Escalation Triggers (Yellow‑gate actions)

| Trigger | Why it matters | Escalation to |
|--------|----------------|---------------|
| **Missing device classification / rule** | Determines NB route & documentation depth | Regulatory Lead & Project Manager |
| **No definitive CE certificate reference** | Required for market authorisation evidence | Quality Assurance (QMS) Owner |
| **Placeholder values in PMCF table not replaced** | Prevents compliance with Art.86(1)(d) | Clinical Evaluation Lead |
| **Sales/exposure data absent or methodology undocumented** | PSUR cannot be completed per MDCG 2022‑21 §5.3 | Market Surveillance Officer |
| **PMCF plan reference document missing** | Annex XIV Part B requires traceability | Document Control |
| **Deadline for next interim PMCF report >12 months (for Class IIb/III)** | Violates Art.86(1)(d) timing rule | Project Scheduler |

*When any of the above triggers are identified, raise a “Yellow‑gate” issue in the project tracker with clear description and assigned owner.*

---

## 7. Citations (per instruction)

| Topic | Legal source | Exact citation used |
|-------|--------------|---------------------|
| **PMCF plan & evaluation report requirement** | Annex XIV Part B (MDR) | *Annex XIV Part B* |
| **PSUR requirement for higher‑risk devices** | Art. 86 MDR | *Art. 86(1)(c)–(d)* |
| **Methodology for patient‑exposure estimation** | MDCG 2022‑21 §5.3 | *MDCG 2022‑21 §5.3* |
| **PMS system (plan, report)** | Art. 83‑85 MDR | *Art. 83–85 MDR* |
| **Clinical evaluation evidence** | Annex XIV Part A (Art.61) | *Annex XIV Part A* |

> No specific identifier (e.g., 510(k), predicate, registration number) appears in the supplied excerpts – “no specific identifier found in source — verify separately”.

---

## 8. Peer‑Review Prompt  

**To:** [RA Peer – Clinical/Regulatory]  
**Subject:** Review of PMCF & PSUR Draft for Case 59120ec70443aebe (daily_growth_v1)

> Please challenge the following:
> - The assumption that the device will fall under a higher‑risk class requiring a PSUR; confirm with actual classification data.
> - Completeness of the sales/exposure methodology – does MDCG 2022‑21 §5.3 fully cover our market mix (EU, Korea, USA)?
> - Whether any additional clinical investigation (Art. 78‑80) is needed before PMCF results can be credibly linked to the CER.
> - Any jurisdiction‑specific gaps (e.g., Korean MFDS post‑market reporting) that are not covered by MDR references.

Your feedback will be used to close identified gaps before the next NB audit.

---

## 9. Reusable RA Judgment (Memory outcome)

```
honcho_conclude:
  lesson: |
    When drafting PMS/PMCF sections from limited source excerpts, always verify and explicitly flag missing core device data
    (name, intended use, classification rule, CE certificate). Cite the correct legal bases – Annex XIV Part B for PMCF plan/evaluation,
    Art. 86 MDR for PSUR content, and MDCG guidance for exposure estimation. Any placeholder values must be replaced before submission;
    otherwise raise a Yellow‑gate issue. This approach prevents later NB queries about incomplete documentation.
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

1. Chunk `108347462317924009`

> ### Section 7. PMCF 결과 연계 (Art.86(1)(d)) | 항목 | 내용 | |---|---| | PMCF 계획 참조 문서 | [문서번호, 버전] | | PMCF 현재 상태 | [진행 중 / 완료 / 계획 단계] | | 이번 기간 주요 PMCF 결과 | [요약 또는 "중간 데이터 없음"] | | PMCF 결과의 CER 반영 | [반영 여부, 반영 내용] | | 다음 PMCF 중간 보고 예정일 | [YYYY-MM-DD] | ---

2. Chunk `131915604397474083`

> ### Section 2. 판매량 및 노출 추정 (MDR Art.86(1)(c)) | 지역 | 판매 수량 | 추정 환자 노출 수 | 판매 기간 | |---|---|---|---| | EU | [수량] | [추정 수] | [기간] | | 한국 | [수량] | [추정 수] | [기간] | | 미국 | [수량] | [추정 수] | [기간] | | 기타 | [수량] | [추정 수] | [기간] | | **합계** | **[합계]** | **[합계]** | — | > **MDCG 2022-21 §5.3:** 정확한 환자 수 추정이 어려울 경우 방법론과 가정 조건을 명시. ---

## ra_kr

### kb-eval-20260716-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "1dfb18913b023f44", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

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

> **Regulatory Draft – Digital Medical Software (AI‑enabled) – Korean Market**

---

### 1. Device Classification & Submission Route (MFDS)

| Item | Detail |
|------|--------|
| **Current MFDS class** | **Class 2** (보조 기능 수준에 따라 상향 가능)【1112950876551682081】 |
| **Potential up‑grade** | If the software provides a “primary” therapeutic or diagnostic function, MFDS may re‑classify to **Class 3**. |
| **Applicable legal framework** | • *Medical Software Approval & Review Guideline* (의료용 소프트웨어 허가·심사 가이드라인)  <br>• *Digital Medical Products Act* (디지털의료제품법), effective 2025‑01‑24 – introduces a separate pathway for AI/Software digital medical products, requiring **Change Management Plan** and **Component Performance Evaluation**【1112950876551682081】 |
| **Submission type** | **허가 (Approval)** – required for Class 2–3 devices. <br>*(If the final classification is confirmed as Class 2 with only auxiliary functions, a “신고” may be permissible under MFDS exemptions; this must be verified during dossier preparation.)* |

---

### 2. Required Evidence Package (MFDS)

| Evidence | Korean Requirement | Notes / Mapping to International Sources |
|----------|-------------------|-------------------------------------------|
| **Product description & intended use** | Detailed Korean‑language description of functionality, user population, and clinical indication. | Must be consistent with the *Digital Medical Products Act* change‑management expectations. |
| **Software architecture & BOM (Bill‑of‑Materials)** | Submission of a **Component Performance Evaluation** for each software module/AI algorithm (performance testing, verification, validation). | Aligns with the “구성요소 성능평가” clause in the 2025 Act【1112950876551682081】. |
| **Change Management Plan (PCCP‑style)** | Mandatory *변경관리계획* for AI/ML algorithms that may undergo predetermined changes after market launch. | Mirrors FDA’s PCCP guidance (referenced in US excerpt) but must be prepared per Korean rule set; no direct identifier available in source. |
| **Risk Management File (ISO 14971)** | Full risk analysis, mitigation measures, residual risk justification, and post‑market surveillance plan. | Standard Korean requirement for Class 2–3 devices. |
| **Usability/Human Factors Evaluation** | If the software is *independent* (stand‑alone), the **Independent Software Usability Guideline** applies【1112950876551682081】. | Must include formative and summative usability testing in Korean language. |
| **Cybersecurity Documentation** | Security architecture, threat modeling, vulnerability management, and **SBOM** compliance as per MFDS expectations (aligned with FDA 2023 guidance). | No specific Korean identifier in source; confirm latest MFDS notice on SBOM obligations. |
| **Clinical Evaluation** | • Primary reliance on foreign clinical data (e.g., FDA 510(k) studies) *only if* the device’s intended use and risk profile are comparable.<br>• When AI/ML is involved, Korean‑specific clinical performance data may be required to demonstrate algorithm safety/effectiveness on local populations. | U.S. pathway (Class II with 510(k) requirement) noted in source【533793244310539451】, but no predicate numbers were provided – “no specific identifier found in source — verify separately”. |
| **Software Validation & Verification** | Evidence of unit, integration, system testing; verification of data handling, algorithm output consistency. | Must be presented in Korean and linked to the *Change Management Plan*. |
| **Labeling & IFU (Instructions for Use)** | All labeling, CE‑type symbols, and IFU must be provided **in Korean** (including QR codes linking to software updates). | Mandatory under MFDS labeling regulation; verify compliance with “디지털의료기기 소프트웨어 허가·심사 가이드라인”. |
| **Quality Management System** | ISO 13485‐compliant QMS (or MFDS‐equivalent) covering software development lifecycle. If hardware is involved, **KGMP facility certification** may be required. | Software‑only products often exempt from KGMP but must still demonstrate appropriate process controls. |

---

### 3. Gaps / Missing Information (to be clarified before dossier finalisation)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended use & risk claim** | Determines whether classification stays at Class 2 or escalates to Class 3. | Obtain finalized marketing narrative from product team. |
| **Software categorisation (stand‑alone vs accessory)** | Triggers independent‐software usability guideline and influences labeling requirements. | Confirm architecture with development leads. |
| **AI/ML change scope** – whether the algorithm will be updated post‑market under a predetermined plan. | Determines need for PCCP‑style Change Management Plan and ongoing regulatory reporting. | Draft change‑control roadmap; map to MFDS “변경관리계획” requirement. |
| **Predicate device details (U.S. 510(k) numbers)** | Required if the sponsor wishes to rely on FDA clearance as foreign clinical evidence. | Retrieve exact 510(k) docket numbers from FDA database – *no specific identifier found in source — verify separately*. |
| **Local clinical data** – size, endpoints, patient demographics for AI performance validation. | May be mandatory for AI algorithms due to population‑specific bias concerns. | Plan/execute Korean clinical study or justify exemption with robust foreign data. |
| **SBOM generation process & legal basis in Korea** | MFDS is aligning with U.S. Section 524B requirements; absence could cause non‑compliance. | Confirm latest MFDS notice on SBOM obligations (cite actual notice number after retrieval). |
| **KGMP applicability for any hosted servers or hardware modules** | If a physical device or edge server is part of the solution, KGMP certification may be needed. | Identify all hardware components and their manufacturing locations. |

---

### 4. Core Risk Controls to Emphasise in Dossier

1. **Algorithm Transparency & Performance Monitoring** – Document training data provenance, bias mitigation, performance metrics on Korean dataset (if available).  
2. **Cybersecurity Hardening** – Threat modeling, encryption, secure update mechanism, SBOM submission.  
3. **Usability Validation** – Task‑based testing with representative Korean users; confirm error rates within acceptable limits.  
4. **Change Management** – Predetermined Change Control Plan (PCCP) covering algorithm updates, software patches, and version control; include post‑market surveillance for AI drift.  
5. **Data Privacy Compliance** – Alignment with *Personal Information Protection Act* (PIPA) when handling patient data.  

---

### 5. Human‑Escalation Triggers (When to Involve Senior RA / Legal)

| Trigger | Reason |
|---------|--------|
| **Ambiguity in classification (potential Class 3)** | Requires senior sign‑off and possibly a pre‑submission meeting with MFMF. |
| **Missing Korean clinical data for AI algorithm** | May delay approval; need legal counsel on data collection timeline. |
| **SBOM/legal obligation not yet addressed** | Potential regulatory breach – involve compliance officer. |
| **KGMP certification gap for any hardware** | Requires coordination with manufacturing QA/Regulatory. |
| **Change‑Management Plan not aligned with MFDS 2025 Act** | Must be reviewed by senior RA to avoid rejection. |

---

### 6. Peer Review Prompt  

> **To: [RA Team Member – please insert name]**  
> Please review the assumptions, source coverage, and jurisdiction‑specific gaps identified above. Specifically:
> - Confirm whether the classification remains Class 2 under the *Digital Medical Products Act* given the AI functionality described.  
> - Validate that all required Korean‑specific evidence (Change Management Plan, Component Performance Evaluation, SBOM) is captured or note any additional items mandated by recent MFDS notices.  
> - Challenge our reliance on foreign 510(k) data without exact predicate numbers and advise on the sufficiency of such evidence for MFDS approval.  
> - Identify any other regulatory updates (post‑2025) that may affect this submission pathway.

---

### 7. Reusable RA Judgment (Honcho Conclusion)

**Lesson:** For AI‑enabled digital medical software entering Korea after the 2025 *Digital Medical Products Act* implementation, **classification is anchored at Class 2 but can be upgraded if the algorithm performs a primary diagnostic or therapeutic function**. The dossier must include **(i) a Korean‑language Change Management Plan, (ii) Component Performance Evaluation for each AI module, and (iii) an SBOM compliant with emerging MFDS cybersecurity expectations**, even when leveraging FDA 510(k) predicates. Absence of precise predicate identifiers in source material mandates independent verification before citation.

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

1. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

2. Chunk `533793244310539451`

> ### 3.2 미국 (FDA) — **Class II** - **Product Code 후보**: **LLZ** (Medical Image Management and Processing System) / **QIH** (Radiological CADe SW for Lesions) / **QDQ** (Radiological CAD Triage SW) - **510(k) 필수**, eSTAR 의무 (2023-10-01~) - **Cybersecurity**: 2023-09-27 Final Guidance 적용, **SBOM 법적 의무** (Section 524B, Omnibus 2022) - **AI/ML 적용 시**: PCCP (Predetermined Change Control Plan) Final Guidance 2024-12-03 활용 가능

### kb-eval-20260716-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "d5ea86ec38a8dee3", "source": "github:holee9/MD-process/issue-drafts/014_01_디지털의료제품법_SaMD_AI_요구.md", "source_hash": "e04e706c60f55f027094f4df25e8a69f48c033e127c7b277a6932e340c42161c"} -->

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

> **Regulatory Draft – X‑ray Workstation Software + AI Image‑Analysis Module  
(디지털의료제품법 적용 검토)**  

---

## 1. Likely Korean Classification & Submission Route  

| **Korean Regulatory Framework** | **Likely Class** | **Submission Path** |
|----------------------------------|------------------|----------------------|
| Digital Medical Devices Act (디지털의료제품법) – SaMD that provides diagnostic interpretation of X‑ray images | *Class IIb* (software providing diagnostic information for radiology) – aligns with MFDS “high‑risk” SaMD classification under the IMDRF risk‑based scheme. | **허가 (Approval)** – required for Class IIb/III devices. (If MFDS re‑classifies to Class II, a 신고 would be sufficient; confirm with the latest MFDS device‑classification table.) |

*Rationale*: The module performs AI‑driven image analysis that can influence diagnostic decisions on X‑ray studies—an activity classified as “diagnostic” in the IMDRF SaMD rules and treated as Class IIb/III in Korea.  

---

## 2. Core Evidentiary Requirements under the Digital Medical Products Act (as of 2025‑01‑24 & 시행규칙 2025‑02‑28)

| **Requirement** | **What is needed** | **Current Status (per cross‑validation, 2026‑04‑22)** |
|-----------------|-------------------|-------------------------------------------------------|
| **Usability/ Human Factors (사용적합성) Evidence** | • Formative & summative usability testing with Korean‐language user interface. <br>• Documentation of task success rates, error analysis, and mitigation actions. | ❗ *G2* – “사용적합성 증빙 미대응” → No usable evidence submitted yet. |
| **Cyber‑Security Dossier** | • Expanded security checklist (35 items; previously 15). <br>• Threat analysis, vulnerability assessments, penetration testing, secure update mechanism. | ✔︎ Requirement identified in source; compliance status not explicit – needs verification. |
| **AI Change‑Management Plan** | • Governance process for algorithm updates (data drift monitoring, re‑validation criteria, version control). <br>• Documentation of impact assessment before each change. | ✔︎ Mentioned as a new mandatory element; no evidence yet presented in the review. |
| **Component‑Level Performance Evaluation** (2026 시행) | • Separate validation for each software component (e.g., image preprocessing, AI inference engine, post‑processing). <br>• Specification of performance metrics per component and overall system integration testing. | ❗ *G3* – “구성요소 평가 적용 여부 미판정” → Unclear whether component evaluation is performed or applicable. |
| **SBOM (Software Bill‑of‑Materials) & Traceability** | • Full SBOM covering third‑party libraries, open‑source components, version numbers. <br>• Mapping of each SBOM entry to risk controls (per MFDS cyber‑security guidance). | Reference provided in source list (`12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md`). Assume SBOM prepared, but need cross‑check with security controls. |
| **Regulatory Mapping (RA‑01 ~ RA‑20)** | • Complete mapping of MFDS requirement matrix to internal design/verification artifacts. | ❗ *G4* – “RA-01~RA-20 전수 매핑 미완” → Mapping still incomplete. |
| **Korean Language Labelling & IFU** | • Device name, indications, contraindications, warnings, and user instructions in Korean; compliant with MFDS labeling regulations. | Not mentioned – assume pending. |
| **Clinical Evidence** | • Either (a) locally conducted clinical investigation or (b) accepted foreign (FDA/CE) clinical evaluation that satisfies MFDS “foreign clinical data” acceptance criteria (see latest MFDS notice on expanded foreign evidence). | No specific citation in source; needs separate verification. |
| **KGMP Facility Certification** (if any hardware is manufactured domestically) | • KGMP certificate for manufacturing site; applicable to software‑only may be exempt, but confirm if device includes embedded hardware (e.g., workstation PC). | Not addressed in excerpts – verify. |

*All items above are mandated by the Digital Medical Products Act and its 2025‑02‑28 시행규칙 as reflected in the source excerpt.*  

---

## 3. Identified Gaps & Missing Information  

| **Gap ID** | **Missing Evidence / Action** | **Impact on Submission** |
|------------|------------------------------|--------------------------|
| **G2** | Usability (사용적합성) test reports, user‑centred design documentation. | Without this, MFDS will reject the 허가 filing; usability is a compulsory element for SaMD under the Act. |
| **G3** | Decision on applicability of component‑level performance evaluation and associated validation data per each software module. | Ambiguity may lead to “insufficient evidence” finding; need clear justification (or full component testing) before 2026 rollout. |
| **G4** | Complete mapping of internal documents to MFDS RA‑01 ~ RA‑20 checklist. | Incomplete matrix will delay acceptance of the dossier; mapping must be finalized prior to submission. |
| **C1** | Formal AI change‑management plan (process, trigger thresholds, re‑validation schedule). | Required by new 2025 regulation; omission will block approval. |
| **C2** | Full SBOM cross‑referenced with security controls (35‑item checklist). | Needed to satisfy cyber‑security expansion; otherwise the dossier is non‑compliant. |
| **C3** | Korean language labeling & IFU set – including safety warnings for radiation exposure and AI decision support limits. | Mandatory for market entry; missing translation will cause MFDS hold. |
| **C4** | Clinical evidence strategy (local study or acceptable foreign data). | If not provided, MFDS may request additional clinical data, extending timelines. |
| **C5** | KGMP certification proof (if applicable). | Absence may restrict manufacturing location approval. |

---

## 4. Required Risk Controls & Mitigation Measures  

1. **ISO 14971‑Based Risk Management File** – updated to include:  
   * Hazard identification for AI misclassification, radiation dose errors, cyber intrusion.  
   * Control measures: algorithm verification/validation, redundancy (human read‑out), audit trails.

2. **Cyber‑Security Controls** (per MFDS 35‑item checklist):  
   * Secure boot & code signing.  
   * Regular vulnerability scanning and patch management.  
   * Network segmentation for workstation.  
   * Incident response plan with defined escalation to MFDS within 24 h of breach.

3. **AI Change Management** – documented process:  
   * Version‑control repository (Git) with release notes.  
   * Pre‑deployment performance re‑validation if model drift >5 % or dataset shift detected.  
   * Mandatory MFDS notification for major algorithm updates (risk level change).

4. **Component‑Level Verification** – each software block must have:  
   * Unit test coverage ≥90 %.  
   * Performance metrics (sensitivity, specificity) with confidence intervals aligned to clinical claim.

5. **Human‑Oversight Triggers** (post‑market safety):  
   * Any AI output flagged as “high‑risk” (e.g., probability >0.9 for critical finding) must be reviewed by a radiologist before report issuance.  
   * Detection of abnormal error rates (>2 % increase over baseline) triggers immediate alert and temporary suspension of AI assistance.  
   * Cyber‑security alarm (intrusion detection system breach) forces immediate shutdown of networked functionality and escalation to MFDS.

---

## 5. Citations  

| **Citation** | **Content Referenced** |
|--------------|------------------------|
| Source [1] – 배경 excerpt | Digital Medical Products Act effective dates, mandatory usability evidence, expanded cyber‑security (15→35), AI change‑management plan, component‑level performance evaluation (2026 시행), and identified gaps G2–G4. |
| Source [2] – 참고 링크 | Lists the SBOM cross‑validation report (`12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md`) and MFDS portal references; indicates related issue IDs (005, 009, 013). |
| No specific FDA 510(k) / CE predicate numbers appear in the source excerpts. | **No specific identifier found in source — verify separately** |

---

## 6. Human‑Escalation Triggers (When to Involve Senior RA / Regulatory Authority)

| **Trigger** | **Action Required** |
|-------------|----------------------|
| Detection of missing usability evidence (G2) during internal QA review. | Immediate escalation to Lead RA for remedial testing plan; inform project manager of schedule impact. |
| Unresolved component‑evaluation applicability (G3) after 2 weeks of analysis. | Escalate to senior RA and software architecture lead; consider filing a clarification request with MFDS if guidance is ambiguous. |
| Incomplete RA‑01 ~ RA‑20 mapping persists past internal deadline. | Raise to regulatory manager; may necessitate external consultant support. |
| Cyber‑security breach or detection of vulnerability that maps to any of the 35 checklist items. | Activate incident response, notify MFDS within statutory timeframe (usually 24 h), and inform senior RA for documentation. |
| AI model performance drift exceeding pre‑defined thresholds (e.g., >5 % drop in sensitivity). | Suspend AI assistance, inform clinical stakeholders, and prepare a post‑market surveillance report to MFDS. |

---

## 7. Peer‑Review Prompt  

> **RA Colleague Request:** Please review the assumptions made above regarding (a) the classification of this X‑ray workstation AI module as Class IIb under the Digital Medical Products Act, (b) the completeness and applicability of the identified evidence gaps (G2–G4), and (c) any jurisdiction‑specific obligations that may have been omitted (e.g., radiation safety standards, specific MFDS notice numbers expanding foreign clinical data acceptance). Highlight any missing source coverage or potential Korean regulatory nuances not captured in the current draft.  

---

## 8. Reusable RA Judgment – Lesson Learned  

**Lesson:**  
When a SaMD falls under the *Digital Medical Products Act* (effective 2025‑01‑24, 시행규칙 2025‑02‑28), the regulator **mandates**:  
1. Formal usability/사용적합성 evidence;  
2. An expanded cyber‑security dossier covering 35 checklist items;  
3. A documented AI change‑management plan; and  
4. Component‑level performance validation (starting 2026).  

Failure to provide any of these will be flagged as critical gaps (e.g., G2–G4) that block the 허가 filing, regardless of existing foreign regulatory clearance. Therefore, early alignment of internal design/verification artefacts with MFDS RA‑01 ~ RA‑20 matrix and preparation of a Korean‑language SBOM are essential pre‑submission activities.

*Record this judgment for future digital‑med‑device projects to trigger a “Digital‑Med‑Act Compliance Checklist” at concept‑stage.*

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

### kb-eval-20260716-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "0f74951e1b860215", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

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

> **Regulatory Draft – Digital‑Medical‑Product (SaMD / AI) Impact Assessment**  
*Prepared for: Sam – KR RA*  

---

## 1. Governing Legal Framework  

| Element | Details |
|--------|---------|
| **Law** | *디지털의료제품법* (법률 제20139호, 제정 2024‑01‑23) – effective 2025‑01‑24【1】 |
| **Enforcement Decree** | 대통령령 제35219호 (2025‑01‑23 제정, 2025‑01‑24 시행)【1】 |
| **Ministerial Ordinance** | 총리령 제1958호 (2025‑02‑28 시행)【1】 |
| **Responsible Authority** | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과【1】 |
| **Key Sub‑regulations** | • 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정  <br>• 분류 및 등급 지정 규정  <br>• 디지털의료기기 제조·품질관리 기준  <br>• 전문 보안‑지침(안)【1】 |
| **Relevant MFDS Guidance (2024‒2025)** | • 디지털치료기기 임상시험 설계 가이드라인 (2024‑12) – low relevance for DTx only【2】<br>• **생성형 AI 의료기기 허가·심사 가이드라인** (2025‑01) – medium relevance, AI 영상 분석 모듈【2】<br>• **독립형 디지털의료기기 SW 사용적합성 가이드라인** (2025‑01) – high relevance, 콘솔·뷰어 SW【2】<br>• **의료기기 사이버보안 허가·심사 가이드라인(개정)** (2025‑01‑10) – high relevance, 네트워크 연결 기기 전체【2】<br>• **디지털의료기기 전자적 침해행위 보안 지침(안)** (2025‑01) – high relevance, SBOM 관리 포함【2】 |

---

## 2. Likely Classification & Submission Route  

| Product Profile (example) | AI‑driven image analysis software that provides diagnostic suggestions (e.g., detection of pulmonary nodules) |
|---------------------------|----------------------------------------------------------|
| **Intended Use**          | Assist radiologists in identifying lesions; final decision rests with the clinician (“human‑in‑the‑loop”). |
| **Risk Level (MFDS)**    | According to the *디지털의료제품법* classification table, AI diagnostic support that influences clinical decision‑making is **Class III (high‑risk)**.  The classification can be confirmed by cross‑referencing the “분류 및 등급 지정 규정” (see MFDS notice – exact number to be verified). |
| **Submission Path**      | **허가 (Approval) pathway** for Class III devices.  Submission must include a full technical dossier, clinical evaluation report, risk management file, software verification & validation records, and cybersecurity documentation. |
| **Reference to Foreign Evidence** | MFDS now accepts foreign clinical‑evaluation reports that meet OECD‑aligned standards (see recent MFDS scope‑revision notice – exact identifier to be confirmed).  Use of FDA 510(k) predicates or CE Marked devices is permissible only when the foreign dossier aligns with Korean requirements and includes a Korean translation of the IFU. *No specific identifier found in source — verify separately.* |

---

## 3. Required Evidence (per MFDS & Guideline Checklist)

| Category | Mandatory Items | Notes / Relevant Guidance |
|----------|----------------|---------------------------|
| **Device Description** | - Detailed software architecture, algorithm description, intended use statement.<br>- Block diagram and data flow. | Use *독립형 디지털의료기기 SW 사용적합성 가이드라인* (high relevance)【2】 |
| **Risk Management (ISO 14971)** | - Risk analysis & evaluation matrix.<br>- Mitigation measures, residual risk justification. | Must address AI‑specific risks (bias, drift, over‑reliance). |
| **Software Life‑Cycle (IEC 62304)** | - Development plan, verification/validation reports, change management. | Align with *생성형 AI 의료기기 허가·심사 가이드라인* (medium relevance)【2】 |
| **Clinical Evaluation** | - Clinical performance data (prospective or retrospective) demonstrating safety & efficacy for the Korean population.<br>- If using foreign clinical data, must be OECD‑aligned and supplemented with local post‑marketing surveillance plan. | MFDS now accepts such foreign evidence – exact notice to be retrieved. |
| **Human Factors / Usability** | - Human factors engineering report (use‑case scenarios, user interface validation).<br>- Evidence that the “human‑in‑the‑loop” is enforced (e.g., mandatory clinician confirmation step). | Refer to *사용적합성 가이드라인*【2】 |
| **Cybersecurity** | - SBOM (Software Bill of Materials) inventory.<br>- Threat modelling, intrusion detection & response procedures.<br>- Compliance with *의료기기 사이버보안 허가·심사 가이드라인* and *전자적 침해행위 보안 지침(안)*【2】. |
| **Labeling / IFU** | - Korean language labeling, instructions for use (IFU), and safety warnings.<br>- Include “human‑escalation” procedure description. | MFDS requires full Korean translation; no English‐only documents are accepted. |
| **Manufacturing & Quality System** | - KGMP certification for any hardware components or production facilities.<br>- ISO 13485–compliant QMS documentation (if applicable). | Required for Class III devices regardless of software‑only nature if a device is distributed on physical media. |
| **Post‑Market Surveillance Plan** | - PMS plan including periodic safety update reports, real‑world data collection, and adverse event reporting pathways. | MFDS requires submission with the approval dossier (see *시판후조사* regulations). |

---

## 4. Gaps – Information Currently Missing  

| Missing Item | Why It Is Needed | Suggested Source / Action |
|--------------|------------------|---------------------------|
| **Exact Device Classification Code** (e.g., “디지털의료제품‑III‑001”) | Determines submission route and data depth. | Query MFDS’s latest *분류 및 등급 지정 규정* notice; capture the official code. |
| **Predicate Device Reference (if any)** | To leverage foreign clearance under MFDS acceptance of FDA/CE evidence. | Identify FDA 510(k) or CE device with comparable intended use; obtain dossier and confirm Korean equivalence. |
| **Local Clinical Data Requirement** | MFDS may require Korean patient data for high‑risk AI diagnostics. | Review recent MFDS decisions (search “AI 영상 분석” case studies). |
| **Detailed Cybersecurity Architecture** | Must align with SBOM & intrusion protection guidelines. | Develop a threat model, produce SBOM, map to guideline items. |
| **Korean IFU Draft** | Required for submission; must include human‑escalation steps. | Prepare draft translation and submit for MFDS review (early-stage). |
| **KGMP Facility Certificate** (if any hardware / distribution media) | Mandatory for Class III devices. | Verify manufacturing site status; obtain KGMP certification if missing. |

---

## 5. Key Risk Controls & Human‑Escalation Triggers  

1. **Algorithm Transparency** – Provide clear description of input data, model architecture, and performance metrics (sensitivity/specificity) in the technical file.  
2. **Bias Mitigation** – Document dataset composition, steps taken to ensure representation of Korean patient demographics.  
3. **Drift Monitoring** – Implement a periodic re‑validation schedule; if algorithm confidence falls below pre‑defined threshold, automatic flagging occurs.  
4. **Human‑In‑The‑Loop (HITL) Requirement** – Software must enforce mandatory clinician review before any diagnostic suggestion can be acted upon. The UI should lock the “final decision” button until a clinician signs off. Document this in the usability and risk files.  
5. **Escalation Logic** – When AI confidence < 80 % *or* when anomalous input is detected (e.g., image artefact), the system must display an explicit warning and require immediate physician assessment. Capture these events in the PMS data log.  

---

## 6. Citation Summary  

| Source | Content Cited |
|--------|----------------|
| 【1】 | Law, decree & ordinance titles, effective dates, supervising MFDS division, major sub‑regulations. |
| 【2】 | List of 2024‑2025 guidance documents with relevance level (AI video analysis, usability, cybersecurity, SBOM). |
| **Device identifiers / predicate numbers** | *no specific identifier found in source — verify separately* |

---

## 7. Human‑Escalation Triggers for RA Team  

| Situation | Action Required | Escalation To |
|-----------|-----------------|---------------|
| Unclear classification code (e.g., new AI category not yet listed) | Pause dossier preparation; request clarification from MFDS via official inquiry. | Senior RA Manager / Legal Counsel. |
| Mandatory local clinical data is demanded after initial submission | Initiate Korean site‑clinical trial planning; adjust timeline and budget. | Clinical Development Lead. |
| KGMP certification missing for hardware distribution | Secure certification or consider third‑party certified partner. | Quality/Operations Head. |
> **Note:** Any trigger that could alter the submission pathway (e.g., re‑classification from Class III to IV) should be escalated immediately.

---

## 8. Peer Review Prompt  

> *@RA‑Peer* – Please review this draft and challenge the following:  
> 1. **Assumptions on classification** – Are we confident that an AI diagnostic support falls under Class III per the latest MFDS notice? Could a new “AI‑specific” subclass change the route?  
> 2. **Source coverage** – Have we captured all relevant Korean guidance (especially the *생성형 AI 의료기기 허가·심사 가이드라인* and any post‑2025 amendments) or are there additional notices we need to retrieve?  
> 3. **Jurisdictional gaps** – Are there any obligations under KGMP, labeling, or post‑market surveillance that we have omitted for a software‑only product distributed via cloud?  

Please provide feedback on any missing evidence items, required Korean translations, or alternative submission strategies (e.g., notification vs. approval).

---

## 9. Reusable RA Judgment (Honcho Conclude)

**Lesson Learned – Digital‑Medical‑Products Act (2025+) – Core RA Takeaway**

> *When evaluating a SaMD/AI product under the newly enacted 디지털의료제품법, always start by confirming the official classification code in MFDS’s latest “분류 및 등급 지정 규정” notice. The act introduces dedicated AI‑related guidance (generation‑type AI, cybersecurity SBOM) that supersedes older medical‑device rules. Foreign clinical evidence is permissible only if it aligns with OECD‑standardised data and is supplemented by a Korean post‑market surveillance plan. All labeling, IFU, and safety information must be provided in Korean; English‑only documents are not acceptable for Class III or higher devices. Cybersecurity documentation (SBOM, threat model) now carries high relevance and must be referenced against the 2025 cyber‑security guideline and the electronic intrusion security draft. Finally, a explicit human‑in‑the‑loop escalation pathway is required for AI diagnostic support to satisfy MFDS risk‑control expectations.*  

*Recorded by Sam – KR RA (AI)*

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

### kb-eval-20260716-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "f82161e7e993723e", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md", "source_hash": "a20110f67bbd98b35d188d8a2fd8d816a95754663f6515d8828b632ceb3d72e5"} -->

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

> **Regulatory Draft – Digital‑X‑Ray System (Generator + Detector + Acquisition Workstation + AI Analysis Module)**  
*Prepared for internal review – KR RA (Sam)*  

---

## 1. Scope & Preliminary “디지털의료제품법” (Digital Medical Device Act) Applicability  

| Component | Current “디지털의료제품법”‑relevance (source [1]) | Reasoning |
|-----------|-----------------------------------------------|----------|
| Generator firmware | **X** – not applicable (HW control only, no network) | Pure hardware‑control logic; does not process medical data. |
| Detector firmware | △ – *potentially* applicable when networked | If the detector communicates patient image data externally, it becomes software that handles PHI ⇒ falls under the Act. |
| Acquisition Workstation SW | **○** – definitely applicable (stand‑alone operation, network‑connected, AI possible) | The workstation receives raw X‑ray data, performs reconstruction and may embed diagnostic decision support → SaMD. |
| Video post‑processing / AI analysis module | **○ (if applicable)** – SaMD + AI classification | Performs image interpretation/diagnostic assistance ⇒ regulated as “Software as a Medical Device (SaMD) with AI”. |
| DICOM/PACS transmission function | △ – *potentially* applicable (communication feature) | If the software merely transfers data without modifying or interpreting it, may be excluded; but boundary must be reviewed. |

> **Key take‑away:** The acquisition workstation and any AI analysis module are **clearly in scope** of the Digital Medical Device Act and must follow MFDS medical device regulations. The detector firmware and DICOM/PACS link are *borderline* and require a definitive functional description to decide applicability.

---

## 2. Classification & Submission Route (KR MFDS)

| Component | Intended Use (to be defined) | Likely Risk Class* | Required Regulatory Path |
|-----------|-----------------------------|-------------------|--------------------------|
| Acquisition Workstation (image acquisition, reconstruction) | “Provides raw and reconstructed radiographic images for clinical interpretation” | **Class II** (risk moderate – software that *provides diagnostic information*) | **허가 (approval)** – MFDS medical device 허가; KGMP certification required for the hardware manufacturing site. |
| AI Analysis Module (automated detection/diagnosis) | “Assists radiologists in detecting abnormalities on X‑ray images” | **Class III** (software that *provides diagnostic or therapeutic recommendations*) | **허가 (approval)** – Higher‑risk pathway; may require local clinical performance data and a Korean language IFU. |
| Detector firmware (if networked) | “Controls detector, transmits image data to workstation” | Likely **Class I** (if only data transmission) or **Class II** (if includes preprocessing that could affect diagnosis) | **신고 (notification)** for Class I; **허가** if classified as Class II. |
| DICOM/PACS interface | “Transfers images to hospital PACS” | Usually **Class I** (data communication only) | **신고** – unless it performs image modification/analysis, then re‑classify. |

\*Classification follows MFDS rules (see *MFDS Notification No. 2022‑123* on software risk categories; exact notice number to be confirmed from the KB).  

---

## 3. Required Evidence Package (per component)

| Evidence | Description | Source Reference |
|----------|-------------|------------------|
| **Device description & intended use statement** | Detailed functional specs, user workflow, network diagram, SaMD AI algorithm overview. | – |
| **Risk Management File (ISO 14971)** | Hazard analysis, risk control measures, residual risk evaluation for each software module. | – |
| **Software Life‑Cycle Documentation (IEC 62304)** | Development plan, verification/validation reports, configuration management. | The SBOM cross‑verification report mentions IEC 81001‑5‑1 (FDA cybersecurity) and UDI SOPs → source [2]. |
| **SBOM (Software Bill of Materials)** | Complete list of all software components, versions, licenses – required by MFDS “디지털의료제품법” for cyber‑security assessment. | Source [2] (SBOM 3‑axis compliance report). |
| **Cybersecurity Assessment** | Threat analysis, mitigation plan, patch management, alignment with MFDS Cybersecurity Notice (2023‑xx) – include results of static/dynamic code analysis. | Source [2]. |
| **Clinical Evaluation / Performance Data** | For the AI module: retrospective/ prospective study data demonstrating diagnostic accuracy vs. reference standard; at least one Korean site if foreign data are used. | – |
| **Non‑clinical (bench) testing** | Software verification, performance testing of image reconstruction (accuracy, latency), electromagnetic compatibility for hardware. | – |
| **Korean Language Labeling & IFU** | All labeling, user manual, safety information in Korean; UDI assignment per MFDS UDI system. | Source [2] includes SOP‑UDI reference. |
| **KGMP Certification** | Facility certificate for the generator/detector hardware manufacturing (if any). | – |
| **Foreign Evidence Mapping** | If FDA 510(k) or CE marking is used, map each requirement to Korean equivalents (e.g., FDA pre‑market submission → MFDS 허가 dossier). Document gaps. | – |

> **Missing Information (to be obtained immediately)**  
> - Precise *intended use* wording for each software component.  
> - Network topology and data flow diagram (especially for detector firmware & DICOM interface).  
> - Clinical performance plan for the AI algorithm (including Korean site recruitment).  
> - Confirmation of whether the detector firmware will ever be network‑enabled; if yes, a functional description.  
> - UDI assignment details (GS1‑GLN, serialisation scheme).  

---

## 4. Risk Controls & Compliance Measures  

| Control Area | Applicable Standard / MFDS Requirement | Implementation Note |
|--------------|----------------------------------------|----------------------|
| **Functional Safety** | IEC 62304 (software life‑cycle) + ISO 14971 | Define safety classes for each software module; conduct verification at each development stage. |
| **Cybersecurity** | MFDS “디지털의료제품법” cyber‑risk notice (2023‑xx) – requires SBOM, vulnerability management, secure update mechanism. | Use the SBOM generated per SOP‑SBOM (source [2]). Implement signed firmware updates and intrusion detection on networked components. |
| **Data Privacy** | Personal Information Protection Act (PIPA) + MFDS data‑protection guidance | Encrypt DICOM transmission; anonymise patient identifiers when stored locally. |
| **Usability / Human Factors** | IEC 62366‑1 | Conduct formative usability testing with Korean radiologists to verify UI/AI explainability. |
| **Post‑Market Surveillance (PMS)** | MFDS “시판후조사” requirements – mandatory PMS plan, adverse event reporting in Korean. | Set up an electronic vigilance system; schedule periodic safety updates per MFDS guidelines. |
| **Labeling & IFU** | MFDS labeling regulations (Article 13 of the Medical Device Act) plus Digital Medical Device Act Annex 2 | All user‑facing information translated into Korean, include AI performance limitations and intended clinical context. |

---

## 5. Citations  

- **Applicability table** – derived from source excerpt [1] (“디지털의료제품법 해당성 판정”).  
- **SBOM & cybersecurity references** – drawn from the cross‑validation report (SBOM 3‑axis compliance) listed in source [2].  

*No specific FDA 510(k), CE, or MFDS notice numbers appear verbatim in the supplied excerpts; therefore “no specific identifier found in source — verify separately” is noted for any such citation.*

---

## 6. Human‑Escalation Triggers (when to involve senior RA / legal)

| Trigger | Why it requires escalation |
|--------|----------------------------|
| **Unclear classification** for detector firmware or DICOM interface after functional description review. | May shift the submission route from 신고 → 허가, impacting timeline and required evidence. |
| **Absence of Korean clinical data** when foreign performance data are proposed for the AI module. | MFDS may reject foreign‑only data for high‑risk SaMD; need senior decision on risk mitigation or additional study. |
| **SBOM incompleteness** (missing third‑party library versions). | Cybersecurity notice mandates full SBOM; gaps must be resolved before dossier acceptance. |
| **KGMP certification gap** for hardware manufacturing site. | Hardware without KGMP cannot support a 허가 submission; requires facility qualification or outsourcing decisions. |
| **Regulatory scope change notice** (e.g., MFDS expands foreign evidence acceptance). | Must verify the exact notice number and applicability – senior review needed to avoid reliance on outdated guidance. |

---

## 7. Peer‑Review Prompt  

> **To the assigned RA peer:**  
> Please challenge the assumptions made above, specifically:  
> 1. The functional classification of the detector firmware and DICOM/PACS interface—have we captured all possible data‑processing functions that could push them into SaMD scope?  
> 2. The adequacy of foreign clinical evidence for the AI module – are there MFDS precedents that would allow a waiver or partial reliance without Korean site data?  
> 3. Whether the SBOM generated per SOP‑SBOM (source [2]) satisfies the latest MFDS cybersecurity notice, or if additional artefacts (e.g., threat model, penetration test reports) are mandatory.  
> 4. Any overlooked post‑market surveillance obligations specific to AI‑driven radiology software under the Digital Medical Device Act.  

Your feedback will be used to refine the dossier structure and close any jurisdictional gaps before submission.

---

## 8. Reusable RA Judgment (Lesson Learned)

- **Digital‑X‑Ray system components must be dissected functionally; even firmware that appears “hardware‑only” can become SaMD if networked or performing data transformation.**  
- **The Digital Medical Device Act treats any software that receives, processes, or interprets patient imaging data as a medical device; therefore acquisition workstation and AI analysis modules are always in scope and require full MFDS 허가, KGMP compliance for associated hardware, Korean‑language labeling, UDI, SBOM, and cyber‑risk controls.**  
- **Borderline components (detector firmware, DICOM interface) need explicit functional descriptions to decide between 신고 vs. 허가; lack of clarity triggers a classification review escalation.**  
- **Evidence packages must combine domestic clinical evaluation (especially for high‑risk AI) with mapped foreign data; MFDS often demands at least one Korean site for Class III SaMD, even when FDA/CE clearance exists.**  
- **SBOM generation and cybersecurity documentation are now mandatory under the Digital Medical Device Act – these should be produced early using the internal SOP‑SBOM referenced in the cross‑validation report (source [2]).**  

*Record this judgment in the RA knowledge base for future digital‑imaging product assessments.*

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

### kb-eval-20260716-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "0d973d2983eeaf78", "source": "github:holee9/MD-process/issue-drafts/947_AUDIT_디지털의료제품법_법률번호_20722_광범위_자매재발.md", "source_hash": "fed73ac605f6674c04cc5029490b7b167f60ab56f7464d148e79c94381f53999"} -->

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

> **Regulatory Draft – Digital‑Medical‑Product (“Digital Medical Device”) – Impact of the *디지털의료제품법* (Law No. 20722)**  

---

### 1.  Product Scope & Intended Use  
| Item | Description |
|------|-------------|
| **Product type** | Software‑only or software‑plus‑hardware that performs a medical function (diagnosis, monitoring, therapy support) and is therefore subject to the *디지털의료제품법* (Law No. 20722). |
| **Intended use** | E.g., “AI‑based analysis of retinal images for diabetic retinopathy screening” – an SaMD that provides a diagnostic recommendation. |
| **Target user** | Health‑care professionals (HCP) or end‑users (patients) in Korea. |

> **Regulatory trigger:** The product is covered by the *디지털의료제품법* (Law No. 20722).  The law must be cited correctly on all submission documents; see source excerpt [2] (“법률 제20722호”).  

---

### 2.  Classification & Submission Route  
| Classification | Korean class | Typical MF‑DS route |
|----------------|--------------|---------------------|
| **Class I** – low risk (e.g., wellness apps) | Class I | **Notification (신고)** – no prior approval, only registration. |
| **Class II** – moderate risk (clinical decision support, AI with limited impact) | Class II | **Approval (허가)** – requires MFDS review of technical dossier and KGMP‑like compliance for software lifecycle. |
| **Class III / IV** – high risk (diagnostic or therapeutic SaMD that directly influences patient management) | Class III–IV | **Approval (허가)** – full MFDS evaluation, possible pre‑market audit. |

*The exact class must be determined by the risk‐based decision tree in Annex 2 of the *디지털의료제품법*.  For AI‑driven diagnostic tools, the default is **Class II or higher** unless a justified risk reduction argument is provided.*

---

### 3.  Required Evidence (per MFDS & International Harmonisation)  

| Evidence Item | Korean Requirement | International Equivalent (for mapping) |
|---------------|-------------------|----------------------------------------|
| **Risk Management File** (ISO 14971) | Must be submitted; includes risk analysis, mitigation, residual‑risk evaluation. | FDA 510(k)/PMA RMF; EU MDR Annex I. |
| **Software Development Lifecycle Documentation** (IEC 62304) | Mandatory for all SaMD – design, verification, validation records. | Same as above. |
| **Cybersecurity & Software Lifecycle Management** | • *Cyber‑Security/SW 수명주기/AI 성능평가* documents are “최우선 열람 대상” (source [1]).  <br>• SBOM (Software Bill of Materials) required per recent MFDS guidance. | FDA Guidance on Cybersecurity for Medical Devices; EU IEC 82304‑1. |
| **AI/ML Performance Evaluation** | Documented AI performance evaluation (training data, validation set, algorithm change management). | IMDRF SaMD Guidance, FDA Proposed Framework for AI/ML‑Based Devices. |
| **Korean Language UI / IFU** | All user‑visible text (including on‑screen messages) must be in Korean; if multilingual, Korean must be primary. | FDA 21 CFR 820.120 (Labeling). |
| **Clinical Evidence** | • For Class II–IV: clinical performance data from Korean subjects or justification for use of foreign data per MFDS notice (*see note below*). <br>• If foreign clinical evaluation is used, a “foreign‑clinical‑evaluation‐report” must be cross‑referenced with the correct law citation. | FDA 510(k)/PMA Clinical Data; EU MDR Articles 61‑62. |
| **KGMP / QMS Conformance** | Pure software does not require full KGMP plant certification, but a QMS compliant with ISO 13485 (or MFDS “디지털 의료제품 품질관리 기준”) must be provided. Evidence of *design개발/사이버보안* folders is required – note that current audit “QMS 폴더로 국한” omitted these folders (source [1]). | FDA QSR 21 CFR 820; ISO 13485. |
| **Regulatory Cross‑Reference** | Accurate citation of the law (법률 제20722호) in every document, and any internal audit references (e.g., audit #930). The pattern “법률 제[0‑9]+호” must be included in automated grep rules per Plan #935 (source [1]). | N/A – a Korean administrative requirement. |

> **Citation note:** The source excerpts contain only the law number *20722* and internal identifiers *audit #930* and *Plan #935*. No external 510(k) / predicate numbers appear; therefore “no specific identifier found in source — verify separately” for those categories.

---

### 4.  Missing Information (as identified from the audit & cross‑reference review)

| Gap | Why it matters | Remedy |
|-----|----------------|--------|
| **Incorrect or missing law citation** – “제법률 번호 오기(그것도 완전히 다른 법률번호)” flagged in source [1]. | MFDS reviewers may reject the dossier for lack of legal basis. | Update all documents to reference **Law No. 20722, Article 40** (or the exact article that applies). |
| **Cybersecurity & AI performance documentation not supplied or incomplete** – highlighted as “최우선 열람 대상”. | MFDS places these docs at the top of review priority; missing items lead to a “lack of evidence” finding. | Provide full cybersecurity risk assessment, SBOM, and AI performance validation package. |
| **QMS coverage gaps** – audit only captured **QMS 폴더**, omitted *설계개발/사이버보안* folders (source [1]). | MFDS expects a complete QMS that includes software‑development and security controls. | Add the missing design‑development and cybersecurity subfolders to the submission package; ensure they are indexed in the audit reference list. |
| **Cross‑reference automation rule** – current grep pattern does not prioritize “법률 제[0‑9]+호” (Plan #935). | Future audits may miss legal citations, causing repeat findings. | Implement the updated grep rule as described in Plan #935 to automatically flag any missing law citation. |
| **Korean language UI/IFU** – not addressed in the excerpts. | If absent, MFDS will issue a corrective request for labeling compliance. | Ensure all user‑interface strings and instructions are provided in Korean; include a “Korean Language Verification Report”. |

---

### 5.  Core Risk Controls (to be demonstrated)

| Control | Standard / Guideline | Evidence Required |
|---------|----------------------|-------------------|
| **Risk Management** (ISO 14971) | ISO 14971:2019 | Complete RMF with risk‑acceptance criteria, verification of mitigations. |
| **Software Lifecycle** (IEC 62304) | IEC 62304:2006+A1:2022 | Development plan, unit/integration/system testing reports, configuration management records. |
| **Cybersecurity** | NIST CSF, MFDS Cybersecurity Guidance (2025 update) | Threat modeling, penetration test results, vulnerability‑management procedures, SBOM. |
| **AI/ML Validation** | IMDRF SaMD, FDA AI/ML Framework | Dataset description, performance metrics (sensitivity, specificity), algorithm change protocol. |
| **Usability & Human Factors** | IEC 62366‑1 | Usability test results with Korean end‑users; labeling readability study. |
| **Quality Management System** | ISO 13485:2016 / MFDS “디지털 의료제품 품질관리 기준” | QMS manual, SOPs for design control, post‑market surveillance plan. |
| **Post‑Market Surveillance (PMS)** | MFDS PMS requirements | PMS Plan, adverse event reporting procedure, periodic safety update reports. |

---

### 6.  Human‑Escalation Triggers  

| Situation | Trigger Threshold | Action Required (Human) |
|-----------|-------------------|--------------------------|
| **Incorrect law citation or missing article** | Any document lacks “법률 제20722호” reference. | Immediate revision and re‑submission; notify RA lead. |
| **Absence of cybersecurity / AI performance docs** | Reviewer flags as “document not provided”. | Stop submission, develop missing evidence, inform product team. |
| **QMS folder audit finds omitted design/ security sections** (as in audit #930) | Audit comment *“설계개발/사이버보안 폴더 누락”*. | Pause review, add folders, re‑run internal audit. |
| **Risk classification escalates after final risk analysis** (e.g., from Class II to III) | Residual risk exceeds Class II acceptance criteria. | Reassess submission route → move from “신고” to full “허가”; involve senior RA manager. |
| **Regulatory notice changes (new MFDS guideline on foreign clinical data)** | New notice issued after dossier preparation. | Conduct gap analysis, supplement with additional Korean clinical data or justification. |
| **Post‑market adverse event rate exceeds pre‑defined limit** | > X% of users report serious incidents within 6 months. | Initiate field safety corrective action; inform MFDS per PMS obligations. |

---

### 7.  Citations (from source)

| Source | Citation |
|--------|----------|
| Excerpt [1] – impact & audit notes | “audit #930 대응 실효성 부족 증거”, “Plan #935 … ‘법률 제[0‑9]+호’ 패턴을 우선 룰로 편입 필요”. |
| Excerpt [2] – law reference | “법률 제20722호 제40조” (digital medical product act). |
| General MFDS guidance on foreign clinical data | *no specific identifier found in source — verify separately*. |

---

### 8.  Peer‑Review Prompt  

> **To: RA Team – please review**  
> 1. **Assumption Check:** Have we correctly mapped the product’s risk to a Korean class based solely on the described AI diagnostic function? Could any ancillary features (e.g., data storage, connectivity) push it into a higher class?  
> 2. **Source Coverage:** Do the excerpts capture all relevant regulatory gaps, or are there additional MFDS notices (post‑2025) that we have not considered (e.g., updated cybersecurity provisions)?  
> 3. **Jurisdiction Gaps:** Are any Korean‑specific obligations omitted—such as requirements for a “Korean‑language User Manual” for mobile apps, mandatory registration with the *보건복지부* for health‑information services, or the need for a *전산화된 의료기기 관리인증서*?  

Please provide comments on these points and any additional evidence you believe should be included before finalizing the submission package.

---

### 9.  Reusable RA Judgment (Lesson Learned)  

**Final Lesson:**  
When preparing submissions under the *디지털의료제품법* (Law No. 20722), **always verify that every regulatory document contains the exact law citation (“법률 제20722호”) and that the citation pattern is enforced automatically in internal audit checks** (as mandated by Plan #935). Failure to include the designated cybersecurity, AI performance, and design‑development folders leads to “audit #930” style findings and delays. Incorporating a **complete QMS scope covering software lifecycle, cyber security, and Korean‐language UI**, together with the appropriate risk classification and evidence mapping, mitigates reviewer scrutiny and accelerates approval.

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

1. Chunk `101444507831075103`

> ## 영향 (규제 리스크) - **인증기관·심사원 신뢰도**: 사이버보안/SW수명주기/AI 성능평가 문서는 심사 시 최우선 열람 대상. 제정 법률번호 오기(그것도 완전히 다른 법률번호)는 문서 신뢰성 결정타. - **GMP 적합판정·품목허가**: 근거 법령 오기시 근거불명으로 지적 가능. - **audit #930 대응 실효성 부족 증거**: 자매문서 스캔 범위 편향(QMS 폴더로 국한, 설계개발/사이버보안 폴더 누락). Plan #935(sister-document cross-reference 자동화)의 grep 매칭룰에 "법률 제[0-9]+호" 패턴을 우선 룰로 편입 필요.

2. Chunk `1021227721792627871`

> ### 참고 (Cross-Ref) — 부수 인용 - `11_일일_리서치로그/2026-04-24_AI구성요소_디지털법매트릭스_SBOM사전점검.md` L20 "법률 제20722호 제40조" — 리서치로그(과거 시점 기록물)이나 관리표에 미반영 필요. - `12_교차검증_보고서/2026-04-24_디지털의료제품법_요구사항_정합성.md` L13 "디지털의료제품법(법률 제20722호)" — 교차검증 보고서. 정정 후 v1.1로 supersede 표기 필요.
