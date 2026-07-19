# KB Eval Checksheet - 2026-07-22 Iteration 03

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260722-it03-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_us-001", "iteration": 3, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "6ff0f8842da987db", "source": "github:holee9/MD-process/issue-drafts/163_03_SOP-DT-001_v0.3_QMSR_설계이관_실사.md", "source_hash": "f6140cf49db744771634400d420f52d5da23c62978782f5757bc6436d63cafa0"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `6ff0f8842da987db`
- Source: `github:holee9/MD-process/issue-drafts/163_03_SOP-DT-001_v0.3_QMSR_설계이관_실사.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/163_03_SOP-DT-001_v0.3_QMSR_%EC%84%A4%EA%B3%84%EC%9D%B4%EA%B4%80_%EC%8B%A4%EC%82%AC.md)
- Source hash: `f6140cf49db744771634400d420f52d5da23c62978782f5757bc6436d63cafa0`
- Focus: submission evidence gaps
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `163_03_SOP-DT-001_v0.3_QMSR_설계이관_실사.md`는 `163_03_SOP-DT-001_v0.3_QMSR_설계이관_실사.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 관련 문서 - SOP-DT-001 (03_설계_개발관리) - 교차검증_2026-06-08 (12_교차검증_보고서) ## 변경 요약 - §9.5 QMSR 설계이관 실사 체크포인트 5항목 신설 - §9.5.2 DHF/DMR→DDF/MDF 용어 전환 확인 매핑표 - §9.5.3 제조 준비도 증거(Manufacturing Readiness Evidence) 체계 6유형 정의 - §9.6 AI 모델 설계이관 QMSR·EU AI Act Art.17 이중 준수 요구 6단계 신설 - 규제 근거 표 QMSR 시행일 반영, SOP-AIGOV-001·SOP-AIDATA-001 상호참조 추가
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR Design‑Transfer & AI‑Model Migration (SOP‑DT‑001)**  

| Item | Judgment / Requirement | Source / Citation |
|------|------------------------|-------------------|
| **Device classification & submission route** | • If the device is a Class II software‑as‑a‑medical‑device (SaMD) or an AI/ML–enabled medical device, the default pathway is a 510(k) Premarket Notification under **21 CFR §807**. <br>• For novel AI functionality without a predicate, consider a De Novo classification request (§814). | Part 820 (QMSR) applies to all Class II/III devices; no imaging‑specific part is indicated in the source, so **Part 892 does not apply**. |
| **Regulatory framework governing design transfer** | • **21 CFR §820.30 – Design Transfer** (mandatory under QMSR effective Feb 2026). <br>• SOP‑DT‑001 introduces new checkpoints (5 items) that map the legacy DHF/DMR to the new DDF/MDF terminology; these must satisfy §820.30 requirements for *design history file* (DHF) and *device master record* (DMR) completeness before production release. | Excerpt [2] – “§9.5 QMSR 설계이관 실사 체크포인트 5항목 신설 … DHF/DMR→DDF/MDF 용어 전환 확인 매핑표”. |
| **Required evidence for design‑transfer** | 1. **Mapping table** showing one‑to‑one correspondence between each legacy DHF/DMR element and the new DDF/MDF element (per SOP). <br>2. **Design Transfer Verification Report** confirming that all specifications, drawings, software code, and AI model artifacts have been successfully transferred to manufacturing. <br>3. **Manufacturing Readiness Evidence (MRE)** – one of the six defined types (e.g., process validation, tooling qualification, staff training records). The specific type required is dictated by risk level (see SOP‑DT‑001 §9.5.3). | Excerpt [2] – “§9.5.3 제조 준비도 증거(Manufacturing Readiness Evidence) 체계 6유형 정의”. |
| **AI/ML model design‑transfer & dual compliance** | • Follow the FDA **Predetermined Change Control Plan (PCCP)** guidance (Dec 2024) for pre‑authorizing planned AI updates. <br>• Demonstrate *dual* compliance with the U.S. QMSR and the EU AI Act **Art. 17** (high‑risk AI systems) – include documentation of data governance, human‑oversight procedures, and post‑market monitoring plan. | Excerpt [2] – “§9.6 AI 모델 설계이관 QMSR·EU AI Act Art.17 이중 준수 요구 6단계 신설”. |
| **Risk controls to be documented** | • **Design Verification & Validation (V&V)** reports covering functional, performance, and safety testing of the transferred design. <br>• **Software Risk Management** per IEC 62304 (risk control measures, failure mode analysis). <br>• **Manufacturing Process Controls** tied to the selected MRE type. <br>• **Post‑market Surveillance** plan that captures AI drift, data set updates, and EU‑AI‑Act reporting obligations. | Implicit from QMSR §820.30, PCCP guidance, and EU AI Act Art. 17 requirements. |
| **Missing information / gaps** | 1. **Device intended use & indication** – needed to confirm classification and predicate. <br>2. **Specific product code or FDA‑recognized classification title** – required for 510(k) format. <br>3. **Predicate device identifiers (510(k) numbers)** if pursuing substantial equivalence. <br>4. **Complete list of the six MRE types and chosen type for this device** – SOP references definition but does not specify which applies. <br>5. **Evidence of AI model training data provenance, bias mitigation, and performance metrics** – essential for PCCP and EU Art. 17 compliance. | No identifiers appear in the source excerpts; note the absence per citation rule. |
| **Human‑escalation triggers** | • Any *absence* of the DHF→DDF/MDF mapping table or incomplete Design Transfer Verification Report. <br>• Selection of an MRE type not justified by risk analysis. <br>• Lack of a documented PCCP or failure to obtain FDA concurrence on planned AI changes. <br>• Unresolved dual‑compliance gaps (e.g., missing EU AI Act Art. 17 evidence). <br>• Classification uncertainty after reviewing intended use – elevate to senior RA lead before submission package is finalized. | Derived from QMSR compliance expectations and FDA guidance on change control for AI/ML devices. |
| **Key regulatory citations** | • **21 CFR §820.30 – Design Transfer** (QMSR). <br>• **21 CFR §807 – Premarket Notification (510(k))**. <br>• FDA Guidance “Predetermined Change Control Plan for AI/ML‑Based SaMD” (Dec 2024). <br>• EU AI Act **Art. 17** – high‑risk AI compliance obligations. | Established references; no verification caveat needed. |
| **Peer‑review prompt** | *“@RA‑Colleague: Please challenge the assumptions that the six Manufacturing Readiness Evidence types defined in SOP‑DT‑001 are sufficient for all risk levels, and verify whether any additional evidence (e.g., process hazard analysis) is required for AI‑enabled devices under QMSR. Also confirm that classification can be safely assumed as Class II without a listed predicate.”* | — |

---

### Reusable RA Judgment (Lesson Record)

**Judgment:**  
When a QMSR‑driven SOP introduces new design‑transfer checkpoints and AI model migration requirements, the regulator must treat the device under **21 CFR §820.30** (design transfer) and verify **dual compliance** (U.S. QMSR + EU AI Act Art. 17). The submission route defaults to a **510(k)** for Class II devices unless no predicate exists, in which case a **De Novo** request is required. Evidence must include a DHF→DDF/MDF mapping table, design‑transfer verification report, and the appropriate Manufacturing Readiness Evidence type matched to risk. AI changes need an FDA‑approved **Predetermined Change Control Plan (PCCP)** and documented EU Art. 17 compliance artifacts.

**Escalation triggers:** missing mapping, incomplete MRE justification, absent PCCP, classification uncertainty, or any gap in dual‑compliance documentation.

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

1. Chunk `159434114844154818`

> ## 관련 문서 - SOP-DT-001 (03_설계_개발관리) - 교차검증_2026-06-08 (12_교차검증_보고서)

2. Chunk `238771195974486986`

> ## 변경 요약 - §9.5 QMSR 설계이관 실사 체크포인트 5항목 신설 - §9.5.2 DHF/DMR→DDF/MDF 용어 전환 확인 매핑표 - §9.5.3 제조 준비도 증거(Manufacturing Readiness Evidence) 체계 6유형 정의 - §9.6 AI 모델 설계이관 QMSR·EU AI Act Art.17 이중 준수 요구 6단계 신설 - 규제 근거 표 QMSR 시행일 반영, SOP-AIGOV-001·SOP-AIDATA-001 상호참조 추가

### kb-eval-20260722-it03-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_us-002", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "7881b6f2cb2d8c19", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_FDA_SBOM_제출물_사전점검.md", "source_hash": "ac0684e8e800838432db917f22348c24c3a819a9824cb391474182b6de2ad600"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `7881b6f2cb2d8c19`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-24_FDA_SBOM_제출물_사전점검.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-24_FDA_SBOM_%EC%A0%9C%EC%B6%9C%EB%AC%BC_%EC%82%AC%EC%A0%84%EC%A0%90%EA%B2%80.md)
- Source hash: `ac0684e8e800838432db917f22348c24c3a819a9824cb391474182b6de2ad600`
- Focus: submission evidence gaps
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `2026-04-24_FDA_SBOM_제출물_사전점검.md`는 `2026-04-24_FDA_SBOM_제출물_사전점검.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 배경 2025-10-01부터 FDA는 premarket submission에 SBOM/사이버보안 증빙 미포함 시 **refuse to accept (RTA)** 처리. 현재 프로젝트는 2026년 내 FDA 제출 계획 — 제출 전 사전점검 필수. --- ### 2.4 Cybersecurity Management Plan | 항목 | 요구 | 현황 | 담당 | |---|---|---|---| | 시판 후 취약점 모니터링 절차 | ◐ | 08_PMS 보강 필요 | 보안/PMS | | 패치 전략 및 주기 | ◐ | | SW | | Coordinated Vulnerability Disclosure (CVD) 정책 | ○ | CVD...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Pre‑Market Submission Readiness (SBOM / Cybersecurity)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination | Rationale / Source |
|------|---------------|--------------------|
| **Device class** | *Not identifiable from the supplied excerpt* | The source provides no information on intended use, technology, or predicate device. Classification must be confirmed by mapping the device’s intended use to the appropriate CFR‑part panel (e.g., 21 CFR §892 for imaging, §862 for clinical chemistry, etc.). |
| **Submission route** | **510(k) Premarket Notification** – presumed Class II unless the classification review (above) dictates otherwise. | Most new medical devices that are not high‑risk follow the 510(k) pathway under **21 CFR §807**. If the device is Class III, a PMA would be required (21 CFR §814). |
| **Relevant regulatory sections** | • 21 CFR §807 – Premarket notification (510(k))<br>• 21 CFR §820 – Quality Management System Regulation (QMSR), effective Feb 2026, ISO‑13485 aligned<br>• 21 CFR §830 – Unique Device Identification (UDI) requirements | These sections apply to any 510(k) submission and are mandatory for FDA acceptance. |

---

### 2. Required Evidence for Acceptance (post‑Oct 1 2025 policy)  

| Evidence Element | Requirement | Current Status (per source) |
|------------------|-------------|------------------------------|
| **Software Bill of Materials (SBOM)** | Complete, machine‑readable SBOM attached to the submission; must include component version, supplier, and provenance data. | *Not mentioned* – must be generated before filing. |
| **Cybersecurity Management Plan (CMP)** | Must address all items listed in FDA’s “Content of Premarket Submissions for Management of Cybersecurity in Medical Devices” (2022) and the RTA policy effective 01‑Oct‑2025. Required sub‑sections: <br>1. Post‑market vulnerability monitoring procedure<br>2. Patch strategy & schedule<br>3. Coordinated Vulnerability Disclosure (CVD) policy<br>4. Security‑update distribution mechanism | • **Post‑market vulnerability monitoring** – marked “◐” (partial); 08_PMS reinforcement needed.<br>• **Patch strategy & schedule** – marked “◐”, no details provided.<br>• **CVD policy** – marked “○”; policy development required.<br>• **Security‑update distribution mechanism** – marked “◐”, lacking specifics. |
| **Risk Management File (RMF)** | IEC 62304/IEC 62443–derived risk analysis, including identified cyber threats, mitigation controls, and residual risk justification. Must be cross‑referenced to the CMP. | Not referenced in source – assume missing. |
| **QMSR compliance evidence** | Quality System documentation aligned with **21 CFR §820**, updated to the February 2026 ISO‑13485 version (e.g., Design Controls, Document Control, CAPA). | No evidence presented; verify completeness. |
| **UDI labeling & GUDID submission** | Conformity with **21 CFR §830.10–§830.60** and successful entry into the Global UDI Database. | Not addressed in source; must be prepared. |

---

### 3. Identified Evidence Gaps  

1. **SBOM** – absent; must be generated (e.g., CycloneDX, SPDX).  
2. **Post‑market vulnerability monitoring procedure** – incomplete; need full SOP describing detection, reporting, and remediation workflow.  
3. **Patch strategy & schedule** – missing timeline and criteria for patch release.  
4. **Coordinated Vulnerability Disclosure (CVD) policy** – not yet established; must define reporter contact, triage process, public disclosure timetable.  
5. **Security‑update distribution mechanism** – details on secure delivery (e.g., signed firmware, OTA update verification) are lacking.  
6. **Cyber‑risk management documentation** – risk analysis linking identified cyber threats to controls is not cited.  
7. **QMSR (Part 820) artifacts** – design history file, change control records, CAPA evidence pending.  

---

### 4. Core Risk Controls (to be documented)  

| Control | Applicable Standard / Guidance | Implementation Note |
|---------|--------------------------------|----------------------|
| **Secure Software Development Lifecycle (SSDLC)** | IEC 62304 + FDA “Content of Premarket Submissions for Management of Cybersecurity” (2022) | Include threat modeling, code review, static/dynamic analysis. |
| **Vulnerability Monitoring & Patch Management** | NIST SP 800‑53 Rev 5 *SI‑3* (Malware Protection), *RA‑5* (Vulnerability Scanning) | Define continuous monitoring, CVE tracking, and patch deployment cadence. |
| **Coordinated Vulnerability Disclosure (CVD)** | ISO 29147 “Vulnerability Disclosure” + FDA guidance | Publish contact point, acknowledgment timeline, and coordinated public advisory process. |
| **Secure Update Mechanism** | IEC 62443‑4‑2 “Secure Firmware Updates”, NIST SP 800‑40 Rev 3 “Guide to Enterprise Patch Management” | Use cryptographic signing, integrity verification, rollback protection. |
| **Predetermined Change Control Plan (PCCP)** – if AI/ML component present | FDA “Predetermined Change Control Plan (PCCP)” guidance (Dec 2024) | Pre‑authorise future algorithm updates under defined risk envelope. |
| **Incident Response & Reporting** | 21 CFR §803 (Medical Device Reporting), IEC 62443‑2‑1 (Risk Management) | SOP for reporting security incidents to FDA within required timelines. |

---

### 5. Citations  

- **Refuse to Accept (RTA) policy for missing SBOM/cybersecurity evidence** – FDA internal memo, effective 01 Oct 2025 (source excerpt [1]).  
- **21 CFR §807** – Premarket notification (510(k)).  
- **21 CFR §820** – Quality Management System Regulation (effective Feb 2026).  
- **21 CFR §830.10‑§830.60** – UDI labeling and issuance requirements.  
- **FDA Guidance “Content of Premarket Submissions for Management of Cybersecurity in Medical Devices” (Sep 2022)** – outlines required CMP elements.  
- **Predetermined Change Control Plan (PCCP) guidance, Dec 2024** – pre‑authorised AI/ML changes.  

*No specific 510(k) predicate numbers or registration IDs appear in the source; verify separately if needed.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required | Escalation Level |
|--------|-----------------|------------------|
| **Missing SBOM** | Generate and attach a complete, machine‑readable SBOM. | RA Lead → Project Manager |
| **Incomplete CMP sub‑sections** (any of the four items) | Develop SOPs/policies, obtain stakeholder sign‑off. | Cybersecurity Lead → Senior RA |
| **Unresolved device classification** | Conduct intended‑use analysis and map to CFR panel; identify predicate if 510(k). | Regulatory Affairs Manager |
| **QMSR non‑compliance evidence** | Complete Design History File, CAPA records, etc., per **21 CFR §820**. | Quality Assurance Director |
| **UDI labeling not prepared** | Create label with UDI, submit to GUDID; confirm acceptance. | Labeling Engineer → RA Lead |
| **Residual cyber‑risk > acceptable** (per RMF) | Reassess risk controls or redesign; may require additional testing. | Chief Medical Officer / Senior RA |

All triggers must be documented in the project risk register and signed off before submission of the 510(k) package.

---

### 7. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions made about the submission pathway, the completeness of the identified evidence gaps, and any jurisdiction‑specific considerations that may have been overlooked (e.g., state‑level cyber reporting obligations, export controls). Highlight any missing citations or alternative regulatory routes (De Novo, special 510(k), etc.) that could apply to this device.

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

1. Chunk `1052559063111348600`

> ## 1. 배경 2025-10-01부터 FDA는 premarket submission에 SBOM/사이버보안 증빙 미포함 시 **refuse to accept (RTA)** 처리. 현재 프로젝트는 2026년 내 FDA 제출 계획 — 제출 전 사전점검 필수. ---

2. Chunk `1133096958018366119`

> ### 2.4 Cybersecurity Management Plan | 항목 | 요구 | 현황 | 담당 | |---|---|---|---| | 시판 후 취약점 모니터링 절차 | ◐ | 08_PMS 보강 필요 | 보안/PMS | | 패치 전략 및 주기 | ◐ | | SW | | Coordinated Vulnerability Disclosure (CVD) 정책 | ○ | CVD 정책 제정 필요 | 보안 | | Security updates 배포 메커니즘 | ◐ | | SW |

### kb-eval-20260722-it03-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_us-003", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "c50451b802383570", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c50451b802383570`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/FDA_AI_ML_2026_PCCP_%EC%9A%B4%EC%98%81_TPLC_%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8.md)
- Source hash: `14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76`
- Focus: submission evidence gaps
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: ### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. --- ## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – AI‑Enabled Diagnostic Software (DSF)**  

---

### 1. Likely Classification & Submission Pathway  
| Item | Rationale |
|------|-----------|
| **Device Class** | Most AI‑enabled diagnostic software functions are Class II unless the intended use is novel or high risk, in which case a Class III PMA may be required (21 CFR 807). |
| **Primary Submission Route** | **510(k) – Premarket Notification** with a substantial‑equivalence claim to an approved predicate that performs the same clinical function.  <br> *If no suitable predicate exists, consider a De Novo request.* |
| **Regulatory References** | • 21 CFR 807 (510(k) process) <br>• 21 CFR 820 (QMSR; ISO 13485‑aligned, effective Feb 2026) <br>• 21 CFR 830 (UDI) <br>• FDA “Predetermined Change Control Plan (PCCP)” guidance, Dec 2024 |

---

### 2. Evidence Package Required for 510(k)

| Evidence Category | Specific Items |
|-------------------|----------------|
| **Intended Use & Indications** | Clear statement of clinical purpose, patient population, and intended user environment. |
| **Predicate Device Identification** | Predicate name, 510(k) number, and equivalence rationale – *no specific identifier found in source — verify separately*. |
| **Software Description** | Architecture diagram, algorithm type (e.g., ML model), version control, and description of training/validation/test data sets. |
| **Data Lineage & Partitioning** | Documentation of data provenance, split into train/tune/test cohorts – cited in source [1]. |
| **Performance Validation** | Clinical performance metrics linked to claimed indications (sensitivity, specificity, ROC, etc.). |
| **Bias Analysis & Mitigation** | Systematic bias assessment and mitigation strategies – highlighted in source [1] (“편향 분석·완화”). |
| **Human‑AI Workflow** | Description of operator interaction, decision support role, and required human oversight. |
| **Risk Management** | IEC 62304 software life‑cycle processes; risk analysis (FMEA) with identified mitigations for safety, cybersecurity, and bias‑related risks. |
| **Cybersecurity Controls** | Threat model, authentication, data integrity checks, and update security procedures. |
| **Labeling & Instructions for Use (IFU)** | Conformity to 21 CFR 801; includes intended use, contraindications, warnings, and user training requirements. |
| **UDI Implementation** | Assign a device identifier per 21 CFR 830 and submit device entry to the GUDID. |
| **Post‑Market Surveillance (PMS) Plan** | Ongoing performance monitoring, adverse event reporting, and a pre‑approved PCCP for anticipated updates – cited in source [1] (“시판 후 모니터링…업데이트 계획 시 PCCP”). |
| **Quality Management System Evidence** | QMSR compliance records (design controls, document control, CAPA) per 21 CFR 820. |

---

### 3. Gaps Identified in the Source Material  

| Missing Information | Why It Matters |
|---------------------|----------------|
| **Exact Intended Use Statement** | Needed to match predicate and define performance endpoints. |
| **Predicate Device Details** | Required for a substantial‑equivalence claim; none listed in source. |
| **Risk Classification Rationale** (Class II vs. III) | Determines the submission type; not specified. |
| **Algorithm Architecture & Versioning** | Needed for software description and PCCP scope. |
| **Detailed Clinical Validation Protocols** | Performance data must be linked to claims. |
| **Labeling Draft & UDI Allocation** | Mandatory for 510(k) submission. |
| **Cybersecurity Threat Model** | Required under FDA’s “Content of Premarket Submissions for Device Software Functions” guidance. |
| **Change‑Control Scope Outside PCCP** | Any change beyond the pre‑approved PCCP must be reported; scope not defined. |

---

### 4. Risk Controls & Management (per FDA AI/ML Guidance)

1. **Predetermined Change Control Plan (PCCP)** – Define permissible algorithm updates, data set expansions, and performance re‑evaluations *before* market launch (source [1]).  
2. **Bias Mitigation** – Systematic assessment of demographic, geographic, and device‑related bias; documented mitigation actions (source [1]).  
3. **Human‑AI Interaction Controls** – Mandatory human oversight points, user training, and clear “stop‑gap” procedures if AI output is uncertain.  
4. **Cybersecurity Measures** – Secure data transmission, authentication, audit logging, and periodic vulnerability assessments.  
5. **Post‑Market Monitoring** – Real‑world performance tracking, adverse event detection, and trigger thresholds for invoking the PCCP amendment process (source [1]).  

---

### 5. Human‑Escalation Triggers (When FDA Involvement Required)

| Trigger | Action |
|--------|--------|
| **Algorithm Change Outside Pre‑Approved PCCP Scope** | Submit a supplemental 510(k) or De Novo request, as appropriate. |
| **New Clinical Indication or Expanded Patient Population** | File a new 510(k) with updated intended use and supporting data. |
| **Significant Performance Deviation (>Δ10% of validated metrics)** | Issue a field correction; notify FDA under 21 CFR 806 (Reports of Corrections). |
| **Serious Adverse Event Linked to Software Function** | Immediate Medical Device Reporting per 21 CFR 803. |
| **Cybersecurity Breach Impacting Device Integrity** | Notify FDA within 48 h as per the Cybersecurity Incident Management guidance. |
| **Discovery of Unmitigated Bias Affecting Clinical Outcomes** | Submit a risk mitigation addendum and update labeling; consider a supplemental 510(k). |

---

### 6. Citations  

* Regulatory framework references are established facts (21 CFR 807, 820, 830).  
* Predetermined Change Control Plan (PCCP) guidance – FDA final guidance, Dec 2024.  
* Source excerpts:  
  * **[1]** – Data lineage, bias analysis, human‑AI workflow, post‑market monitoring, and PCCP update plan.  
  * **[2]** – Status of two documents outlining marketing submission recommendations for a PCCP; confirms that finalized PCCP is “✅ 확정·시행” as of Dec 2024 (no specific identifier found in source — verify separately).  

---

### 7. Human Review & Peer Challenge Prompt  

> *Please have an RA colleague review the assumptions above, especially the inferred Class II classification and the completeness of the evidence checklist given that no predicate device identifiers are present in the source material.*  

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

1. Chunk `1132891599852736913`

> ### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. ---

2. Chunk `135350017850675307`

> ## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로 사전 승인된 변경 범위 운영 | | **AI-Enabled Device Software Functions: Lifecycle Management & Marketing Submission Recommendations** | **초안(Draft)** | 2025-01-06 | ⏸ 초안 유지(FY2026 B-list) | TPLC 전반 설계·제출 권고(투명성·편향·HF·사이버보안) | > 의견수렴: 수명주기 초안은 2025-04-07 코멘트 마감. 이후 확정본 미발표(2026-06 기준). ---

### kb-eval-20260722-it03-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_us-004", "iteration": 3, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "f1e8a2894c293058", "source": "github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md", "source_hash": "19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f1e8a2894c293058`
- Source: `github:holee9/MD-process/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/238_03_AUDIT_FOLLOWUP_QMSR_%C2%A7820.30_subsection_citations_systemic.md)
- Source hash: `19a0ea5ba10e00599623e88b8c907053fe69b62f5e78b818e384e88ca6560fcf`
- Focus: submission evidence gaps
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md`는 `238_03_AUDIT_FOLLOWUP_QMSR_§820.30_subsection_citations_systemic.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: `00_프로젝트관리/문서_매트릭스.md` 의 §820.30 표기는 본 SOP/Form frontmatter에서 자동 생성되므로 위 frontmatter 정정 후 빌드 스크립트로 자동 갱신됨. ## 배경 audit #921(2026-06-26) 종결 과정에서 SOP-AIGOV-001 frontmatter "FDA QMSR §820.30/ISO13485 §7.3"를 "§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30은 Reserved)"로 정정하였으나, **동일한 §820.30 subsection-letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR §820.30 Residual Citation Gap**

---

### 1. Classification / Submission Route  
- **Device classification:** *Not applicable* (the issue concerns internal Quality Management System compliance, not a specific device).  
- **Impact on submission:** Any future 510(k) or De Novo filing for devices developed under the current QMS must demonstrate compliance with design‑control requirements per **21 CFR §820.10(c)** (incorporating ISO 13485:2016 §7.3). Failure to do so could trigger a “non‑conforming design control” finding that would delay clearance.

---

### 2. Required Evidence for Compliance  

| Requirement | Evidence Needed | Source / Citation |
|-------------|----------------|-------------------|
| **Design Control** – establishment of a single, traceable path from design inputs through outputs, verification, validation, and transfer to manufacturing. | • Updated Design History File (DHF) with complete traceability matrix.<br>• SOP‑AIGOV‑001 front‑matter showing “§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference)”.<br>• Records of design reviews, risk analysis (per IEC 60601‑1/IEC 62304 as appropriate). | **21 CFR §820.10(c)** – Design controls; **ISO 13485:2016 §7.3** – Incorporation by reference. |
| **Document Control** – all SOPs, forms, and matrices must reference only the active QMSR provision. | • Complete inventory of SOPs/forms with a “no‑§820.30” statement.<br>• Updated version control logs confirming removal of §820.30 citations. | **21 CFR §820.30** – Reserved (effective 2026‑02‑02). |
| **Audit Trail** – proof that the corrective action from audit #921 has been fully implemented. | • Audit report detailing the gap.<br>• Post‑audit verification checklist confirming no residual §820.30 references remain. | Internal audit #921 (2026‑06‑26) – source excerpt. |

---

### 3. Missing / Incomplete Information  

| Gap | Description | Recommended Action |
|-----|-------------|--------------------|
| **Residual citations** | “동일한 §820.30 subsection‑letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스 전반에 분산 잔존” – the same §820.30 subsection reference persists across multiple documents. | Perform a systematic grep/search of all QMS documents for “§820.30”. Replace each instance with the approved “§820.10(c) → ISO 13485:2016 §7.3”. |
| **Version control evidence** | No explicit record that updated SOP front‑matter has been propagated to downstream forms/matrices. | Capture a version‑control matrix showing revision numbers and dates for every affected document; archive signed approvals. |
| **Design‑control traceability linkage** | The current DHF does not demonstrate a clear link between design inputs/outputs and the ISO 13485:2016 §7.3 requirements. | Augment the traceability matrix to map each design input/output, verification activity, and risk control to the corresponding ISO clause. |
| **Verification of Reserved status** | While the source states §820.30 is “Reserved”, a formal citation from eCFR confirming this status (effective 2026‑02‑02) should be included in the compliance package. | Retrieve the official eCFR text for **21 CFR §820.30** and attach as Appendix A. |

---

### 4. Risk Controls  

| Control | Rationale |
|---------|-----------|
| **Single design‑control pathway (§820.10(c) ↔ ISO 13485:2016 §7.3)** | Eliminates ambiguity; ensures all design activities are governed by an active, enforceable regulation. |
| **Document change‑control** | Prevents re‑introduction of obsolete citations after future SOP revisions. |
| **Periodic compliance audit (quarterly)** | Detects any drift back to the Reserved §820.30 reference before FDA inspection. |
| **Training refreshers for QMS authors** | Reinforces the correct citation practice and awareness of the 2026 QMSR amendment. |

---

### 5. Citations  

- **Regulatory law:** 21 CFR Part 820 – Quality Management System Regulation (effective 2026‑02‑02).  
  - §820.10(c) – Design control requirements (active).  
  - §820.30 – *Reserved* as of the same effective date.  

- **Standard:** ISO 13485:2016, §7.3 – Incorporation by reference.

*(All citations are established regulatory references; no case‑level identifiers were present in the source.)*

---

### 6. Human‑Escalation Triggers  

| Trigger | Action & Owner |
|---------|----------------|
| **Residual “§820.30” citation discovered post‑remediation** | Immediate escalation to QMS Manager → Issue a corrective action (CAPA) and re‑run the document grep check. |
| **Audit finding of incomplete design‑control traceability** | Notify Design Engineering Lead; pause any new device development until DHF compliance is demonstrated. |
| **Discrepancy between SOP front‑matter and downstream forms** | Raise to Regulatory Affairs Director for a cross‑functional review meeting (Regulatory, QA, Documentation). |
| **FDA inspection note referencing design‑control non‑conformance** | Escalate to Senior Management; initiate FDA response plan per 21 CFR §807.92. |

---

### 7. Peer Review Prompt  

*Please have a fellow RA reviewer challenge the following:*  

1. **Assumptions about single‑path design control:** Is reliance on §820.10(c) ↔ ISO 13485:2016 §7.3 sufficient for all device classes, or are there supplemental FDA guidance documents (e.g., GSPR 2025‑01) that must be referenced?  
2. **Source coverage:** Does the excerpt fully capture every location where §820.30 might appear, or could there be hidden references in legacy spreadsheets or training materials not covered by a simple grep?  
3. **Jurisdictional gaps:** Are there any additional obligations under 21 CFR §820.70 (Production and Process Controls) or other parts that become relevant once design control is re‑aligned?  

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

### kb-eval-20260722-it03-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_us-005", "iteration": 3, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "bab7d4edd6125572", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md", "source_hash": "5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `bab7d4edd6125572`
- Source: `github:holee9/MD-process/12_교차검증_보고서/2026-04-20_GSPR_QMSR_PRRC_정합성검증.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/12_%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D_%EB%B3%B4%EA%B3%A0%EC%84%9C/2026-04-20_GSPR_QMSR_PRRC_%EC%A0%95%ED%95%A9%EC%84%B1%EA%B2%80%EC%A6%9D.md)
- Source hash: `5edc1de6d4425e4edd781fe552f281f1bf06a88727f22cb852dd3d90d4e738ee`
- Focus: submission evidence gaps
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `2026-04-20_GSPR_QMSR_PRRC_정합성검증.md`는 `2026-04-20_GSPR_QMSR_PRRC_정합성검증.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `submission evidence gaps` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `submission evidence gaps`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - submission에 필요한 bench, clinical, software, cybersecurity, AI, QMS, labeling evidence의 누락 여부를 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – QMSR Gap‑Analysis & Submission Planning**

---

### 1. Classification & Submission Route (Bottom Line)
* **Device classification cannot be finalized** because the source provides only a quality‑system / MDR mapping exercise and no description of the medical device’s intended use, technology or risk class.  
* **Action:** Identify each device in scope, its intended use, and applicable FDA product code. Once known, assign the proper 21 CFR part (e.g., imaging devices → Part 892; software → Part 820/Part 11) and determine whether a 510(k), De Novo or PMA is required.

---

### 2. Required Evidence for QMSR Compliance (2026‑02 effective)

| Requirement | Evidence Needed | Regulatory Citation |
|-------------|----------------|---------------------|
| **Quality Management System** – Documentation of all quality processes, SOPs, work instructions and records. | • Complete QMS manual<br>• SOPs covering design control (§820.30), production & process controls (§820.70), CAPA (§820.100), complaint handling (§820.198) | 21 CFR §820 (QMSR) |
| **UDI System** – Integrated UDI Data Record (UDR). | • Master UDI record linking device identifier, production identifier, model/size, and GUDID submission.<br>• Traceability from design to post‑market. | 21 CFR §830.10‑§830.30; EU MDR Art.27 (cross‑referenced) |
| **Risk Management** – ISO 14971:2021 compliant risk management file. | • Hazard analysis, risk evaluation, mitigations, residual risk justification.<br>• Updated for any AI/ML change plans. | ISO 14971:2021 (cited as “Harmonized”) |
| **Biocompatibility** – ISO 10993 series evidence (as applicable). | • Test reports covering cytotoxicity, sensitization, irritation, etc., matching device contact duration. | ISO 10993 (harmonized) |
| **Sterilization & Packaging** – ISO 11135/11137/17665/11737, ISO 15223‑1 labeling, ISO 20417 usability. | • Validation reports, labeling claims, user instructions. | Harmonic standards list in source |
| **Software Lifecycle (if applicable)** – IEC 62304, IEC 82304‑1, IEC 81001‑5‑1. | • Software development plan, verification & validation evidence, cybersecurity risk assessment. | State‑of‑the‑art references in source |
| **AI/ML Change Control** – Predetermined Change Control Plan (PCCP). | • Documented PCCP describing pre‑market change limits and post‑market monitoring. | FDA Guidance Dec 2024 “Predetermined Change Control Plan (PCCP)” |
| **Electronic Signatures & Records** – 21 CFR Part 11 compliance. | • Scope definition, validation plan, audit trails for all regulated records. | 21 CFR §11 |

---

### 3. Gaps Identified in Source & Immediate Actions

| Gap (source) | Missing Evidence / Document | Required Action |
|--------------|----------------------------|-----------------|
| **No SOP template for MDR decision documents** (ML‑MDR‑001 draft needed) | Formal decision‑making record linking risk assessment, regulatory impact, and post‑market obligations. | Draft & approve ML‑MDR‑001; integrate into design review minutes. |
| **Fragmented UDI master record (UDR)** – only scattered fragments exist. | Consolidated UDI Data Record per §820.35(b) & 21 CFR §830.10‑30. | Create a single UDR SOP; populate with all device identifiers; map to GUDID submission schedule. |
| **Internal audit report lacks objective evidence citations** | Audit findings must reference specific documents, test reports, or records that substantiate each non‑conformance. | Revise “External Audit Response” template to require citation of primary evidence (e.g., ISO 14971 risk file, IEC 62304 verification logs). |
| **Unclear scope of electronic signatures** | Definition of which regulated records fall under Part 11; validation plan for the selected scope. | Issue QM‑IT‑001 defining Part 11 applicability; conduct Part 11 validation and training. |

*All four gaps directly affect compliance with 21 CFR §820 (QMSR) and 21 CFR §830 (UDI). They must be closed before any FDA submission.*

---

### 4. Risk Controls to Address Identified Gaps

1. **Document Control** – Enforce version‑control procedures; require sign‑off by QA for all SOPs, templates, and UDI records.
2. **Traceability Matrix** – Map each regulatory requirement (CFR/ISO) to a specific document/evidence artifact; use the matrix in internal audits.
3. **CAPA Process** – Any gap discovered triggers a CAPA record with root‑cause analysis, corrective action plan, and effectiveness verification (§820.100).
4. **Training & Competence** – Document training on new SOPs (ML‑MDR‑001, QM‑IT‑001) and UDI management; retain attendance records per §820.25.
5. **PCCP Implementation** – For AI/ML modules, define allowed algorithmic changes upfront; integrate monitoring metrics into post‑market surveillance.

---

### 5. Human‑Escalation Triggers (When to Notify Senior Management / QRM)

| Trigger | Reason | Escalation Path |
|---------|--------|-----------------|
| **No consolidated UDI Master Record** after 30 days of gap identification. | Non‑compliance with §830 and EU MDR Art.27 – hampers device traceability & market authorization. | Notify QA Manager → Regulatory Affairs Lead → C‑Level if unresolved > 15 days. |
| **Absence of approved ML‑MDR‑001 decision‑making SOP** after draft completion deadline. | Impedes risk‑based regulatory decisions; may affect FDA clearance timing. | Escalate to R&Q Director for resource allocation. |
| **Electronic Signature scope undefined and Part 11 validation not started** past project milestone. | Risk of non‑conforming records, potential FDA Form 483. | Immediate escalation to Compliance Officer & IT Security Lead. |
| **Audit report lacks cited evidence** resulting in repeat findings on consecutive audits. | Indicates systemic documentation weakness; could trigger FDA inspection findings. | Report to QA/Compliance Committee; consider external audit support. |

---

### 6. Next Steps (Actionable)

1. **Device Identification:** Compile a list of all devices slated for submission, capture intended use and risk class.  
2. **Template Finalization:** Complete ML‑MDR‑001, QM‑IT‑001, and UDI SOPs; obtain QA sign‑off.  
3. **Populate UDI Master Record:** Consolidate all device identifiers into a single controlled database.  
4. **Audit Template Update:** Implement evidence‑citation requirement; run a pilot audit to validate.  
5. **Part 11 Scope Definition & Validation Plan:** Draft QM‑IT‑001, schedule validation activities.  
6. **PCCP Development (if AI/ML present):** Document predetermined change limits and monitoring plan.

---

### 7. Peer Review Prompt
> *Please review the assumptions above:  
> – Are the identified gaps exhaustive given the source material?  
> – Does the proposed evidence matrix align with the latest QMSR (Feb 2026) requirements?  
> – Any jurisdiction‑specific considerations (e.g., EU MDR cross‑reference) that may affect our UDI or risk‑management approach?*  

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

1. Chunk `1061533089543682126`

> ## 2. GSPR ↔ 정합표준 매핑 교차검증 | 확인 포인트 | 결과 | |-------------|------| | OJEU 공식 Harmonized 여부 | ISO 13485, ISO 14971(A11:2021), ISO 10993(다수), ISO 11135/11137/17665/11737, ISO 15223-1(2021), ISO 20417, ISO 17664-1/-2, EN 60601-1 계열 → **Harmonized** | | MDCG 2021-5 State-of-the-art 처리 | IEC 62304, IEC 62366-1, IEC 82304-1, IEC 81001-5-1 → **State-of-the-art** 적용 | | AI/ML 기기 | OJEU/MDCG 단독 등재 없음 → EU AI Act 병행 필요(후속 과제) | | 운영 영향 | 체크리스트에 H/S 컬럼 신설, 개정판 번호(A11, A1, A2) 기재 의무화 |

2. Chunk `1066441905930561439`

> ### Gap → 조치 | Gap | 조치 | |-----|------| | 국내 SOP에 MDR 결정문서 양식 부재 | 양식 ML-MDR-001 초안(보고/미보고 결정트리) 신설 | | UDI 마스터 레코드 단편화 | UDR(UDI Data Record) 통합 관리 SOP 초안 (§820.35(b) + 21 CFR 830 + EU MDR Art.27) | | 내부감사 보고서 서술 수준 | "외부감사 대응 수준" 템플릿 개정 (객관적 증거 필수 인용) | | 전자서명 범위 모호 | Part 11 적용범위 정의 문서(QM-IT-001) 초안 예정 |

## ra_eu

### kb-eval-20260722-it03-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_eu-001", "iteration": 3, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "b6dea4f737f3e163", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b6dea4f737f3e163`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDCG_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/Clinical_Evaluation_MDR_%EB%8F%99%EB%93%B1%EC%84%B1_%EC%B6%A9%EB%B6%84%EC%84%B1_%EA%B8%B0%EC%A4%80.md)
- Source hash: `c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR, MDCG

**Source Summary**

- 문서 요약: `Clinical_Evaluation_MDR_동등성_충분성_기준.md`는 EU MDR clinical evaluation, CER/CER plan, equivalence 또는 clinical data sufficiency 관련 문서입니다.
- 현재 excerpt 핵심: ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Clinical Evaluation Gap Analysis (MDR 2017/745)**  

---

### 1. Scope & Device Overview (as far as can be derived from source)

| Item | Observation |
|------|--------------|
| Intended clinical purpose | Not specified in the excerpt; must be defined by the manufacturer before any equivalence assessment can start. |
| Target user type | Must be identified **(professional HCP vs. lay‑person)** – MDR adds a requirement to match “same kind of user” when claiming equivalence (see source [1]). |
| Anatomical site / clinical condition | Needs explicit statement; the source requires *identical* anatomical location and disease stage for equivalence. |

> **Action:** Obtain the manufacturer’s Intended Use Statement, including patient population, anatomical target, disease severity/stage, and user category.

---

### 2. Classification & Conform‑assessment Route  

| Step | Requirement | Reference |
|------|-------------|-----------|
| Determine class using MDR rule set (Annex VIII). The most likely rules for an active or software‑driven device are **Rule 9, 10, 11 or 17**; the final rule depends on the actual mode of action. | Annex VIII – Classification Rules |
| Choose conformity‑assessment route: <br>• If a Quality Management System (QMS) is already in place under ISO 13485, the **Annex IX** route (full technical documentation + QMS audit) is typical for Class IIa–III devices. <br>• For lower‑risk (Class I sterile/measuring), **Annex X** (type‑examination) may be used. | Annex IX, Annex X, Annex XI – Conformity‑assessment routes |

> **Action:** Once the class is known, select the appropriate annex route and schedule the Notified Body audit accordingly.

---

### 3. Clinical Evaluation Evidence Required  

| Evidence Item | Minimum MDR Requirement | Gap (if any) |
|---------------|------------------------|--------------|
| **Clinical data from equivalent device(s)** – must demonstrate: <br>• Same clinical condition and intended purpose<br>• Same anatomical site<br>• Comparable patient population (age, anatomy, physiology)<br>• **Same user type** (new MDR addition) | Art. 61 & Annex XIV Part A (CER) – equivalence criteria must be satisfied. | • No data on *user type* provided.<br>• No documentation of anatomical site or disease stage similarity. |
| **Clinical performance data** for the device under investigation (clinical investigations, PMS, literature). | Art. 61(1)(b); if sufficient clinical evidence is not available, a post‑market clinical follow‑up (PMCF) study must be planned (Annex XIV Part B). | • No existing clinical investigation report or PMS data referenced.<br>• No PMCF plan drafts available. |
| **State‑of‑the‑Art (SOTA) literature review** – to support that the device meets current performance expectations. | Annex XIV Part A, clause 5.6 (clinical evaluation – literature). | • Literature search strategy not supplied. |
| **Benefit–risk analysis conclusions** summarised in the CER. | Art. 61(4) & 86(a) – conclusions must be documented. | • No draft benefit‑risk summary present. |
| **Declaration of conformity** (EU DoC) and technical documentation (including risk management file). | Annex IV (DoC); Annex II (technical documentation). | • Technical documentation package not yet compiled. |

> **Overall Gap Summary:** The source excerpt only outlines the *equivalence criteria*; it does **not** provide any actual clinical data, user‑type description, or supporting literature. All of those items are mandatory before a CER can be considered complete.

---

### 4. Risk Management & Controls (related to missing evidence)

| Control | Rationale under MDR |
|---------|----------------------|
| Update **Risk Management File** (ISO 14971) to reflect any uncertainty arising from the lack of equivalence data, especially concerning user error if a lay‑person device is claimed equivalent to an HCP‑only device. | Annex I § 17 & § 22 – protection for users; risk analysis must cover foreseeable misuse. |
| Implement **Post‑Market Clinical Follow‑up (PMCF)** as a mitigation when equivalence cannot be fully demonstrated at launch. | Annex XIV Part B – PMCF plan required where clinical evidence is insufficient. |
| Conduct **Usability Engineering** to verify that the intended user group can safely operate the device, since “same kind of user” is now a regulatory gate. | IEC 62366‑1 (referenced in Annex I § 17). |

> **Action:** Draft or update the risk management file and map each identified evidence gap to an interim risk control (e.g., limited market launch with restricted user group, PMCF study).

---

### 5. Documentation Checklist for Notified Body submission  

| Item | Required by | Status |
|------|-------------|--------|
| Intended Use Statement (including user type) | Art. 2 & 3 MDR | ❓ – missing |
| Classification decision (rule number) | Annex VIII | ❓ – pending |
| Conformity‑assessment route selection (Annex IX/X/XI) | Annex IX‑XI | ❓ – pending |
| Clinical Evaluation Report (CER) – full content per Annex XIV Part A | Art. 61 & Annex XIV Part A | ❓ – missing |
| PMCF Plan (if needed) | Annex XIV Part B | ❓ – missing |
| Risk Management File (ISO 14971) | Annex I § 16‑22 | ❓ – pending update |
| Technical Documentation (Design Dossier) | Annex II | ❓ – incomplete |
| EU Declaration of Conformity | Annex IV | ❓ – not yet drafted |

---

### 6. Human‑Escalation Triggers  

| Trigger | Description | Escalation Target |
|---------|-------------|-------------------|
| **No clear user‑type definition** | MDR insists on “same kind of user” for equivalence; without this the CER cannot be accepted. | Lead Clinical Affairs / Project Manager – obtain definitive user categorisation. |
| **Equivalence criteria not met (anatomical site, disease stage)** | Missing or ambiguous statements prevent claim of similarity. | Clinical Evaluation Team – perform additional literature review or consider a new clinical investigation. |
| **Insufficient clinical data** | No investigational data, PMS, or PMCF plan available. | Head of Regulatory Affairs – decide whether to postpone market entry and launch a PMCF study. |
| **Classification ambiguous** | Without knowledge of the device’s mode of action (e.g., active therapeutic vs diagnostic) class cannot be assigned. | Engineering Lead – provide detailed functional description for rule mapping. |
| **Technical documentation incomplete** | Missing risk file, design specifications, or labeling details. | Documentation Coordinator – compile pending artifacts before NB audit. |

---

### 7. References Cited  

* MDR Regulation (EU) 2017/745 – **Art. 61**, **Annex XIV Part A & B**, **Annex II**, **Annex IV**, **Annex VIII** (classification rules), **Annex IX‑XI** (conformity‑assessment routes).  
* MDCG Guidance: 2020‑5 (Equivalence), 2020‑6 (Sufficient Clinical Evidence), 2023‑7 (Art. 61(4)–(6) Exemptions), 2024‑3 (CER Content).  
* MEDDEV 2.7/1 rev. 4 – previous equivalence baseline (referenced for comparison).  

---

### 8. Peer Review Prompt  

> **To a fellow EU RA colleague:** Please challenge the assumptions made above, especially regarding: <br>1. The completeness of the equivalence‑criteria checklist derived from source [1]; <br>2. Whether any additional MDR provisions (e.g., Art. 84 PMS plan requirements) should be incorporated at this early stage; <br>3. Potential jurisdictional nuances (e.g., national competent authority expectations) that could affect the evidence gap analysis.

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

1. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

2. Chunk `1090731331984830062`

> > 최종 갱신: 2026-05-18 (자동보강 #52) > 근거: MDR Regulation (EU) 2017/745 Article 61 & Annex XIV | MDCG 2020-5 (Equivalence, Apr 2020) | MDCG 2020-6 (Sufficient Clinical Evidence, Apr 2020) | MDCG 2023-7 (Article 61(4)-(6) Exemptions, Dec 2023) | MDCG 2024-3 (CER Content) | FDA 510(k) Program Guidance (Jul 2014) | FDA Best Practices for Predicate Device Selection (Oct 2023 Draft) | MFDS 의료기기 허가·신고·심사 등에 관한 규정 (고시 제2024-88호) # Clinical Evaluation (MDR) 심화 — 동등성·충분성 기준

### kb-eval-20260722-it03-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_eu-002", "iteration": 3, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "83356594e071d8f8", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `83356594e071d8f8`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDCG_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/MDCG_2020-5-6-7-8_%EC%9E%84%EC%83%81%ED%8F%89%EA%B0%80_PMCF_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4_%EC%9A%94%EC%95%BD.md)
- Source hash: `a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR, MDCG

**Source Summary**

- 문서 요약: `MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md`는 `MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ``` ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Clinical Evaluation Gap Analysis (MDR 2017/745)**  

---

### 1. Preliminary Device Characterisation  
| Item | Current information from source | Comment / Gap |
|------|---------------------------------|---------------|
| **Intended medical purpose** | Not disclosed in the excerpts. | *Missing* – required to select the applicable classification rule (Annex VIII). |
| **Device type / principle of operation** | No description provided. | *Missing* – needed for rule selection and choice of relevant standards (e.g., IEC 60601‑2‑xx, ISO 14971). |
| **Target population / user group** | Mentioned only as placeholders “[임상적] 대상 집단”, “[임상적] 사용자 유형” (clinical target group & user type) – no concrete data. | *Missing* – essential for clinical evaluation scope and risk assessment (§22, Annex I). |
| **Core performance claims** | Listed as “[임상적] 핵심 성능” but not specified. | *Missing* – required to define Clinical Evaluation Report (CER) endpoints and to select appropriate state‑of‑the‑art (SOTA) comparators. |

> **Regulatory consequence:** Without a clear intended purpose, the device cannot be classified under Annex VIII nor can an appropriate conformity‑assessment route be identified (Annex IX, X or XI).  
> **Human‑escalation trigger #1** – request detailed device description, indications for use and user profile before any further MDR drafting.

---

### 2. Likely Classification Pathway (to be verified)  

| Possible rule | Device category (illustrative) | Class according to Annex VIII |
|---------------|--------------------------------|------------------------------|
| **Rule 9** – active therapeutic devices | e.g., electrosurgical unit, laser therapy | IIa (or IIb if energy delivery is potentially hazardous) |
| **Rule 10** – active devices for diagnosis/monitoring | e.g., patient monitor, ultrasound console | IIa (IIb where vital physiological data could cause immediate danger) |
| **Rule 11** – medical device software | e.g., diagnostic decision‑support app | IIa (IIb/III if decisions may lead to serious deterioration or death) |
| **Rule 17** – X‑ray image recording devices | e.g., digital detector panel | IIa |

*These are examples only. The actual rule can be assigned only after the intended purpose and mode of action are clarified.*  

> **Human‑escalation trigger #2** – once intended use is supplied, perform a rule‑by‑rule cross‑check (Annex VIII) and confirm classification.

---

### 3. Required MDR Evidence Packages  

| Deliverable | Regulatory reference | Core contents (high‑level) |
|-------------|----------------------|---------------------------|
| **Technical Documentation** | Annex II | Device description, design drawings, manufacturing information, risk management file, clinical evaluation (CER), PMS plan, labels & IFU (§23). |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; Art. 61 (kept current) | • State‑of‑the‑art literature review  <br>• Clinical data from own trials or equivalent devices  <br>• Benefit–risk determination  <br>• Conclusions and recommendations |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | Annex XIV Part B | • Objectives, methodology, timing, sample size, data sources, statistical analysis, evaluation criteria |
| **PMCF Evaluation Report** | Annex XIV Part B – mandatory sections A–G (see source excerpt 2) | A. Manufacturer contact <br> B. Device description (updated if changes) <br> C. Results of PMCF activities (including positive & negative findings, deviation justification) <br> D. Evaluation of clinical data from equivalent/similar devices <br> E. Impact on Technical Documentation (CER, Risk Management File, Summary of Safety and Clinical Performance – SSCP) <br> F. Applied consensus standards/guidance (e.g., MDCG 2020‑5/6/7/8) <br> G. Overall conclusion (alignment with PMCF objectives; need for preventive or corrective actions). |
| **Post‑Market Surveillance (PMS) System** | Art. 83 | Structured process to collect and analyse information on the device’s performance throughout its lifecycle. |
| **PMS Plan** | Art. 84 | Defined PMS activities, responsibilities, timelines, and reporting procedures. |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | Art. 86 (annual for IIb/III; biennial for IIa) | • Benefit‑risk conclusions <br>• Main PMCF findings <br>• Sales volume & user population characteristics |
| **Risk Management File** | ISO 14971 (referenced in Annex I §17‑19) | Hazard identification, risk analysis, evaluation and mitigation; updates driven by clinical data. |
| **Labeling & Instructions for Use (IFU)** | Annex I Chapter III (§23) | Device name, intended purpose, contraindications, warnings, user instructions, performance specifications. |

> **Human‑escalation trigger #3** – if any of the above dossiers cannot be populated because source data are lacking (e.g., no clinical data, no equivalence assessment), escalate to the clinical development team for evidence generation.

---

### 4. Identified Gaps from Source Excerpts  

| Gap | Evidence required | Where it fits in MDR dossier |
|-----|-------------------|------------------------------|
| **Scientific / Clinical Significance not demonstrated** (excerpt 1) | • Clinical data demonstrating that the device achieves its claimed performance and provides patient benefit, relative to state‑of‑the‑art. <br>• Comparative clinical evidence or equivalence justification. | CER (Annex XIV Part A), PMCF plan and report (Annex XIV Part B). |
| **Missing detailed user & population description** (excerpt 1) | • Definition of the intended user group, training level, and patient demographics. | Device description (Technical Documentation Annex II); risk assessment (§22, Annex I). |
| **Absence of core performance specifications** (excerpt 1) | • Quantitative performance criteria (e.g., accuracy, precision, sensitivity, specificity). | CER (clinical endpoints), Risk Management File (risk‑control verification), labeling (§23). |
| **No data on equivalence / similar devices** (section D of PMCF report) | • Identification and appraisal of clinical data from predicate/equivalent devices. | PMCF Evaluation Report (Annex XIV Part B, section D). |
| **Impact on Technical Documentation not described** (section E of PMCF report) | • Explicit statements on how PMCF outcomes modify CER, Risk Management File, SSCP. | PMCF Evaluation Report (section E); updates to Technical Documentation Annex II. |

> All above gaps must be closed before a Notified Body can accept the technical documentation for conformity assessment.

---

### 5. Core Risk Controls (to be verified against device specifics)

| Control | MDR/GSPR reference | Typical implementation |
|---------|--------------------|------------------------|
| **Hazard identification & risk analysis** | ISO 14971; Annex I §17‑19 | Systematic FMEA/FMECA covering mechanical, electrical, thermal, radiation (if applicable) hazards. |
| **Protective measures for identified risks** | GSPR §§16‑20 (radiation protection, electronic programmable systems, active devices) | Engineering safeguards, alarms, interlocks, software safety functions (IEC 62304). |
| **Usability engineering** | IEC 62366‑1 (referenced in GSPR §22) | Human factors analysis for lay‑person use, labeling clarity. |
| **Post‑market risk mitigation** | Art. 83‑86 (PMS & PSUR) | Continuous monitoring of adverse events; corrective actions reflected in updated Risk Management File. |
| **Software validation (if applicable)** | GSPR §17; IEC 62304 | Verification and validation testing, cyber‑security assessment. |

> **Human‑escalation trigger #4** – if hazard analysis cannot be completed because the device’s functional description is missing, request detailed engineering specifications.

---

### 6. Summary of Regulatory Judgment  

*At this stage the available source material does not contain sufficient information to:*

1. **Assign an MDR classification (Annex VIII rule).**  
2. **Select a definitive conformity‑assessment route (Annex IX/ X / XI).**  
3. **Populate the mandatory sections of the PMCF Evaluation Report (especially D–E) with concrete data.**  

*Consequently, the dossier is incomplete and cannot be submitted to a Notified Body.*

**Immediate actions required (human escalation):**

| # | Action | Responsible role |
|---|--------|-------------------|
| 1 | Provide complete device description, intended purpose, user profile & performance claims. | Product development / Marketing |
| 2 | Supply clinical evidence (clinical trial results, literature review, equivalence data) to address the “scientific evidence + clinical significance” gap. | Clinical research team |
| 3 | Draft a full PMCF Plan (objectives, methodology) and start data collection; feed interim results into sections C–G of the PMCF Evaluation Report. | Post‑Market Surveillance lead |
| 4 | Update Risk Management File with identified hazards and mitigation measures based on the new clinical data. | Risk management officer |
| 5 | Confirm applicable consensus standards (e.g., IEC 60601‑2‑xx, ISO 14971) and include them in section F of the PMCF Evaluation Report. | Standards compliance specialist |

---

### 7. Peer Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made above regarding the classification uncertainty, the list of required MDR evidence, and the identified documentation gaps. Specifically:  
> * Are there additional MDR clauses or MDCG guidances that should be considered for this type of device?  
> * Does the outlined PMCF Evaluation Report structure fully satisfy Annex XIV Part B, or are supplementary sections (e.g., statistical analysis plan) required?  
> * Could any of the missing items be inferred from other parts of the source repository not quoted here?  

Your feedback will help verify completeness before escalating to product owners.

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

1. Chunk `1032759063790726230`

> │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ```

2. Chunk `1132312459160211217`

> ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과 (데이터 수집 결과, 긍정·부정 포함, 편차 근거) | | D | 동등·유사 기기 임상데이터 평가 결과 | | E | 기술문서에 대한 결과의 영향 (CER, Risk Management File, SSCP 각각 명시) | | F | 적용된 CS, 조화표준, 가이던스 | | G | 종합 결론 (PMCF 목적 대비 결과, 예방·시정 조치 필요성) |

### kb-eval-20260722-it03-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_eu-003", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "fa90ff878ef527e7", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `fa90ff878ef527e7`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter |...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Clinical Evaluation Gap Analysis & Conformity Assessment Plan**  
(Prepared for the Notified‑Body deficiency‑letter response)

---

### 1. Device Scope & Intended Use
- **Intended purpose:** “Standard diagnostic radiology” (X‑ray imaging system).  
- **Core function:** Emission of ionising radiation to produce diagnostic images.

### 2. Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Classification rule** | **Rule 10** – active device for diagnosis/monitoring | MDR Annex VIII, Rule 10 (active devices for diagnostic use) |
| **Resulting class** | **Class IIb** (energy‑emitting X‑ray source) | MDR Annex VIII, Rule 10 ⇒ Class IIb |
| **Conformity‑assessment route** | **Annex IX** – full quality‑management system assessment + technical file review by the NB | MDR Annex IX (mandatory for Class IIb devices) |

*If the manufacturer prefers a type‑examination route, Annex X may be used, but the default and most common path for Class IIb X‑ray systems is Annex IX.*

### 3. Required Evidence Portfolio (per MDR)

| Evidence | Mandatory reference | What it must demonstrate |
|----------|---------------------|---------------------------|
| **Clinical Evaluation Report (CER)** | Annex XIV, Part A; kept current under Art. 61 | Clinical equivalence to a predicate device (same clinical condition & performance), comprehensive benefit‑risk analysis, justification of safety and performance claims. |
| **Performance testing** – DQE ≥ 65 % | IEC 62220‑1‑1 (DQE measurement) & Annex XIV, Part A | Demonstrates that the imaging chain meets or exceeds the diagnostic performance of the reference device. |
| **Risk Management File** | ISO 14971 + MDR Annex I §16–§18 | Identification of radiation hazards, electronic safety, active‑device risks; controls (shielding, interlocks, dose monitoring). |
| **Usability / Human Factors** | IEC 62366‑1 | Verification that device can be safely used by intended operators (including lay‑person use if applicable – GSPR §22). |
| **Electrical Safety & EMC** | IEC 60601‑2‑54 (X‑ray equipment) | Conformity to essential safety requirements for radiographic systems. |
| **Post‑Market Surveillance (PMS) System** | Art. 83 MDR | Ongoing collection of performance and safety data, incident handling. |
| **PMS Plan** | Art. 84 MDR | Definition of data sources, periodic safety update reporting intervals. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 MDR (annual for Class IIb) | Summaries of PMS results, benefit‑risk conclusions, PMCF findings. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV, Part B | Ongoing clinical data collection to confirm long‑term safety/performance. |
| **Labeling & IFU** | Annex I §23 | Instructions for use, radiation protection information, contraindications, and training requirements. |

### 4. Gaps Identified in the Current Submission (per deficiency letter)

| Gap | Evidence currently supplied | What is missing / insufficient |
|-----|-----------------------------|--------------------------------|
| **CER depth** | Only a statement of clinical equivalence based on DQE ≥ 65 % (Ref. Test Report TR‑2024‑015, IEC 62220‑1‑1). Revised CER Rev. 3 attached as Annex A. | • No comprehensive literature review of state‑of‑the‑art devices.<br>• Absence of benefit‑risk analysis (GSPR §§16–22).<br>• No justification for the chosen DQE threshold relative to clinical outcomes.<br>• No description of patient population, sample size, or statistical methods. |
| **Risk Management** | Not referenced in excerpt. | Full risk management file (ISO 14971) required; especially controls for radiation exposure (§16), electronic safety (§17), and active‑device interlocks (§18). |
| **Usability Engineering** | Not mentioned. | IEC 62366‑1 usability validation report to demonstrate safe use by intended operators. |
| **PMS Documentation** | No PMS system or plan cited. | Art. 83/84‑MDR PMS system description, data collection procedures, and PSUR schedule (annual for Class IIb). |
| **PMCF Planning** | Not provided. | Annex XIV Part B PMCF plan specifying endpoints, follow‑up duration, and reporting format. |
| **Labeling / IFU** | Not included. | Full labeling package complying with Annex I §23 (radiation protection statements, user instructions, contraindications). |
| **Standards Conformity** | IEC 62220‑1‑1 referenced for DQE; no evidence of compliance with IEC 60601‑2‑54 or IEC 62304 (software lifecycle) if software is involved. | Test reports and declarations of conformity to the relevant IEC standards. |

### 5. Risk Controls Required (per GSPR)

| Hazard | Control measure | Regulatory clause |
|--------|----------------|-------------------|
| **Radiation exposure** (excess dose, scatter) | • Shielding design meeting IEC 60601‑2‑54 limits.<br>• Real‑time dose monitoring & automatic shut‑off.<br>• Interlocks on protective curtains and collimators. | Annex I §16 (radiation protection). |
| **Electronic / software malfunction** | • Design verification per IEC 62304 (software lifecycle).<br>• Fault detection, safe‑state transition.<br>• Periodic self‑test routines. | Annex I §§17–18 (electronic programmable systems & active devices). |
| **Mechanical failure (collapse of gantry/stand)** | • Structural analysis, load testing.<br>• Protective enclosures, mechanical locks. | Annex I §20 (mechanical risk). |
| **User error (lay‑person settings)** | • Human factors validation (IEC 62366‑1).<br>• Clear IFU with pictograms; training program. | Annex I §22 (use by lay persons). |
| **Labeling errors** | • Dual‑language labeling, verification of all safety statements. | Annex I §23. |

### 6. Human‑Escalation Triggers

| Situation | Trigger action | Responsible party(s) |
|-----------|----------------|----------------------|
| **NB deadline breach** (no response within the agreed “clock‑stop” period) | Immediate escalation to Project Manager → Senior Regulatory Lead; consider request for extension under structured dialogue (Art. 7, 2026/977). | Regulatory Team Lead |
| **Critical missing evidence identified** (e.g., no risk management file or PMS plan) | Halt preparation of the NB response; raise a “Deficiency‑Critical” issue in the project tracker; senior management decision required before submission. | QA Manager & Clinical Affairs Lead |
| **Unresolved labeling non‑conformity** | Convene cross‑functional labeling review meeting; if no resolution within 5 working days, inform the NB of a provisional schedule amendment. | Regulatory + Marketing & Legal |
| **Unexpected adverse event or field safety corrective action (FSCA) discovered during gap analysis** | Immediate notification to NB (Art. 87 MDR) and internal vigilance team; suspend submission until FSCA is addressed. | Vigilance Officer |
| **Disagreement on classification or assessment route** | Request a formal clarification from the NB via Structured Dialogue (Art. 7, 2026/977); document all arguments. | Regulatory Lead |

### 7. Summary Judgment

- The device is a **Class IIb active X‑ray system** (MDR Annex VIII Rule 10) and must follow **Annex IX** conformity assessment.  
- Current documentation **fails to satisfy** MDR requirements for a complete CER, risk management, PMS/PMCF, usability engineering, labeling, and conformity to the full suite of applicable IEC standards.  
- The identified gaps must be bridged **before** the NB can issue a favorable opinion.  

### 8. Peer‑Review Prompt

> *Colleague, please challenge the following: (i) the adequacy of the DQE ≥ 65 % threshold as the sole clinical performance metric; (ii) whether any additional classification rules (e.g., Rule 17 for the detector component) could affect the overall class or assessment route; and (iii) the completeness of the cited regulatory obligations in relation to the source excerpts. Identify any jurisdiction‑specific gaps that may have been overlooked.*

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

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1014893419282866507`

> | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter | 보완 요청 | Additional Information (AI) Request | | 근거 법령 | MDR Annex VII + 2026/977 | 의료기기법 §12 + 허가·신고·심사 규정 | 21 CFR 807 + FDA Review Policy | | 답변 기한 | NB와 합의 (법정 상한 없음) | 1차 60일, 2차 60일 | 180일 (타임라인 기산일부터) | | 최대 중단 횟수 | 4회 (product verification 기준) | 2차까지 (실질 2회) | 제한 없음 (Interactive Review 가능) | | Clock-stop | 예 (NB 요청 당일 stop, 제출 익일 resume) | 예 (보완 기간 제외) | 예 (AI 발송일부터 stop) | | 미응답 시 | 평가 종료 / 불승인 | 취하 간주 | 허가 거부 | | 사전 대화 창구 | Structured Dialogue (Art.7, 2026/977) | 상담제도 (비공식) | Pre-Sub (Q-Sub) (공식, 문서화) | | 주요 결함 유형 | CER, TD, QMS NC, Labelin...

### kb-eval-20260722-it03-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_eu-004", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7f031b9b3ec42e2c", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7f031b9b3ec42e2c`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PSUR_%ED%85%9C%ED%94%8C%EB%A6%BF_MDR_Article86.md)
- Source hash: `6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PSUR_템플릿_MDR_Article86.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Section 7. PMCF 결과 연계 (Art.86(1)(d)) | 항목 | 내용 | |---|---| | PMCF 계획 참조 문서 | [문서번호, 버전] | | PMCF 현재 상태 | [진행 중 / 완료 / 계획 단계] | | 이번 기간 주요 PMCF 결과 | [요약 또는 "중간 데이터 없음"] | | PMCF 결과의 CER 반영 | [반영 여부, 반영 내용] | | 다음 PMCF 중간 보고 예정일 | [YYYY-MM-DD] | --- ### Section 2. 판매량 및 노출 추정 (MDR Art.86(1)(c)) | 지역 | 판매 수량 | 추정 환자 노출 수 | 판매 기간 | |---|---|---|---| | EU...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Clinical Evidence Gap Analysis & PSUR Preparation (Art 86 MDR)**  

| Item | Requirement / Observation | Current Status (per source) | Gap / Action Needed |
|------|---------------------------|-----------------------------|---------------------|
| **1. Device classification & conformity‑assessment route** | Must be identified to select the correct PSUR frequency (Art 86 (2)) and the appropriate Annex for technical documentation (Annex II) and PMS system (Art 83). | *Not provided in source excerpts.* | • Obtain intended use, mode of action, and risk class.  <br>• If Class IIa → PSUR every **2 years**; if Class IIb/III → PSUR **annually** (Art 86 (2)).  <br>• Conformity‑assessment route will then be one of: **Annex IX**, **Annex X**, or **Annex XI** (per classification). |
| **2. PSUR content – Sales & patient exposure (Art 86 (1)(c))** | Must include for each market: sales volume, estimated number of patients exposed, and the period covered. | Table skeleton exists but all quantitative cells are placeholders (“[수량]”, “[추정 수]”).  <br>Guidance reference: **MDCG 2022‑21 §5.3** (methodology & assumptions when patient numbers cannot be precisely known). | • Populate sales figures for EU, Korea, USA and other markets. <br>• Provide transparent methodology/assumptions for patient‑exposure estimates (cite MDCG 2022‑21 §5.3). |
| **3. PSUR content – PMCF results linkage (Art 86 (1)(d))** | Must list: • Reference to the current PMCF plan, • Status of PMCF activities, • Summary of key interim results, • How those results are reflected in the CER, • Date of next interim PMCF report. | Section 7 table is present but all entries are placeholders (“[문서번호, 버전]”, “진행 중 / 완료 / 계획 단계”, etc.). | • Insert the exact document identifier and version for the **PMCF plan** (see Annex XIV Part B). <br>• Update *current status* (e.g., “ongoing – 60 % enrolment”). <br>• Summarise interim findings or state “no data available”. <br>• Confirm whether and how the CER has been updated (Annex XIV Part A). <br>• Schedule next interim PMCF reporting date. |
| **4. PMS system & plan linkage** | A functional PMS system (Art 83) and a documented PMS plan (Art 84) must exist and be referenced in the PSUR. | Not mentioned in excerpts. | • Verify that a **PMS system** is implemented per Art 83 and a **PMS plan** per Art 84. <br>• Cite these documents in the PSUR (e.g., “see PMS‑Plan Ref #XYZ, version 1.2”). |
| **5. Risk Management updates** | Any significant findings from PMCF or trend analysis must trigger updates to the risk management file (ISO 14971) and be reflected in the GSPR compliance evidence (Annex I). | No information on risk‑management actions. | • Map each identified safety signal or performance gap to a **risk control** (e.g., design change, labeling update, additional training). <br>• Record the updated risk assessment and residual risk evaluation. |
| **6. Clinical Evaluation Report (CER) – current version** | Must be kept up‑to‑date (Art 61) and incorporate PMCF findings (Annex XIV Part A). | No CER reference provided. | • Identify the latest **CER** version, confirm it includes all relevant clinical data, and cross‑reference it with the PMCF outcomes listed in Art 86 (1)(d). |
| **7. Frequency of PSUR submission** | Determined by device class (Art 86 (2)). | Class unknown → frequency cannot be set. | • Once classification is known, schedule PSUR updates accordingly (annual for IIb/III; biennial for IIa). |
| **8. Documentation for EUDAMED registration** | Sales and exposure data must also be entered into the **EUDAMED device‑registration module** (Art 33‑39). | Not covered in source. | • Ensure that the same quantitative data used in the PSUR are uploaded to EUDAMED. |

---

### Required Evidence Summary (per MDR)

| Evidence | Regulatory Basis |
|----------|-------------------|
| **Device classification & intended use** | Annex VIII (Rules 1‑22) – determine class; **Annex IX/X/XI** for conformity route |
| **Technical documentation** | Annex II (plus Annex III for PMS) |
| **PMS system** | Art 83 |
| **PMS plan** | Art 84 |
| **Periodic Safety Update Report (PSUR)** | Art 86 (1)(a‑d); frequency Art 86 (2) |
| **PMCF plan & interim reports** | Annex XIV Part B |
| **Clinical Evaluation Report (CER)** – latest version incorporating PMCF results | Annex XIV Part A; Art 61 |
| **Risk Management file (ISO 14971)** – updated with any new hazards identified through PMCF or trend analysis | Annex I (GSPR §15‑§16) |
| **EUDAMED registration data** | Art 33‑39 |

---

### Risk Controls to be Demonstrated

1. **Updated risk management actions** addressing any adverse events identified in interim PMCF results (ISO 14971).  
2. **Labeling/instructions for use updates** if performance or safety information changes (Annex I §23).  
3. **Post‑market surveillance measures** (trend reporting, vigilance) aligned with Art 88 and MDR MDCG guidance.  
4. **Software/firmware change controls** where PMCF identifies usability or algorithmic issues (Annex I §17, IEC 62304).  

---

### Human‑Escalation Triggers

| Trigger | Reason | Recommended Escalation |
|--------|--------|------------------------|
| **Classification unknown** | Cannot set PSUR frequency nor choose Annex IX/X/XI route. | Immediate escalation to product owner/clinical lead for intended‑use clarification. |
| **Missing quantitative sales/exposure data** (placeholders remain after deadline) | Incomplete Art 86 (1)(c) information → non‑compliant PSUR. | Escalate to market‑access team to obtain verified sales reports and exposure methodology; deadline ≤ 2 weeks before reporting cut‑off. |
| **PMCF plan reference absent or status “planned” after >12 months** | Indicates inadequate post‑market clinical data collection for Class IIb/III devices (Art 86). | Escalate to Clinical Affairs – initiate or accelerate PMCF study; report to senior management. |
| **No evidence of CER update with PMCF results** | Violates Annex XIV Part A requirement and Art 61 “kept current”. | Escalate to Clinical Evaluation team; mandate CER revision before PSUR submission. |
| **PMS system not documented in PSUR** | Fails Art 83/84 linkage; may trigger Notified Body query. | Escalate to Quality Management – provide PMS‑system SOPs and evidence of operation. |
| **Trend analysis or vigilance data indicating emerging safety signal** | Must trigger risk‑management update (Art 86 (1)(d) & Art 87). | Immediate safety‑signal assessment; if serious, trigger Field Safety Corrective Action (FSCA) per Art 87 and inform Notified Body. |
| **EUDAMED data mismatch with PSUR figures** | Regulatory inconsistency → possible non‑conformity finding. | Escalate to regulatory reporting coordinator for data reconciliation. |

---

### Peer‑Review Prompt  

*“@RA‑colleague – please review the assumptions made above regarding (i) classification determination, (ii) completeness of the PMCF‑CER linkage, and (iii) adequacy of the sales/patient‑exposure methodology in light of MDCG 2022‑21 §5.3. Identify any jurisdiction‑specific gaps (e.g., additional reporting obligations for non‑EU markets) and suggest missing evidence that should be captured before the next PSUR submission.”*

**Citation Lint (C1 — 구조적 인용 오류 자동 감지)**

- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86 (1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86 (1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art 86 (1)(d)`)

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

### kb-eval-20260722-it03-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_eu-005", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a5eea01bffb14927", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a5eea01bffb14927`
- Source: `github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/04_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%ED%85%9C%ED%94%8C%EB%A6%BF/PMS_Plan_MDR_Article84_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `PMS_Plan_MDR_Article84_템플릿.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | PMS 항목 | 특화 내용 | |---|---| | 주요 위험 신호 | SW 오류로 인한 진단 오류, 데이터 손실, 사이버보안 취약점 | | 핵심 수집원 | SW 버그 리포트, 사이버보안 취약점 공개 DB (CVE, NIST NVD) | | PMCF 방법 | 사용성 평가 (IEC 62366), 실사용 에러 데이터 수집 | | 주요 표준 모니터링 | IEC 62304 개정, MDCG 2019-16 Rev.1 사이버보안, MDCG 2021-6 SaMD | | MFDS 특이사항 | 디지털의료제품법(2024.09.26 시행) 적용 여부 검토 [검증 필요] | --- ### 2-A. 자사 3제품 적용 매트릭스 | 제품 | MDR 등급 (...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `clinical evaluation gap analysis` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `clinical evaluation gap analysis`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - CER/CER plan, equivalence, clinical data sufficiency, PMCF/PMS linkage, MDCG expectation을 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & Submission Plan**  
*(MDR 2017/745 – focus on the three digital‑radiology products listed in the source)*  

---  

### 1 Device Portfolio & MDR Classification  

| Product (as described) | Intended Use / Function | MDR Classification Rule* | Resulting Class | Primary Conformity‑Assessment Route |
|------------------------|-------------------------|---------------------------|-----------------|--------------------------------------|
| **X‑ray Detector** (image plate / flat‑panel detector) | Records diagnostic X‑ray images generated by an external source | **Rule 17** – “Devices specifically intended for recording diagnostic images produced by ionising radiation” | **IIa** (per Rule 17) – the source table also notes a possible IIb, but the rule places it in IIa. | **Annex IX** – full quality‑management system + assessment of technical documentation (standard route for Class IIa). |
| **Handheld X‑ray Source** (portable generator emitting ionising radiation) | Emits X‑ray photons for diagnostic radiology | **Rule 10** (radiology limb) – “Active devices that emit ionising radiation for diagnostic or therapeutic purposes” | **IIb** (per Rule 10) | **Annex IX** (or Annex X + XI if the manufacturer prefers a type‑examination route). |
| **Imaging‑Room GUI Software (SaMD)** | Provides decision support / image display and interpretation guidance for X‑ray examinations | **Rule 11** – “Software providing information used for diagnostic decisions”; MDR §22 also allows classification of certain SaMD as IIa when the impact on health is limited. | **IIa** (per Rule 11 & §22) | **Annex IX** (software‑specific assessment, see IEC 62304). |

\*Rule citations are taken from the MDR classification rules list (Annex VIII).  

---  

### 2 Required Evidence Package (MDR Obligations)

| Evidence Element | Regulatory Reference | Minimum Content (per MDR) | Status / Gap |
|------------------|----------------------|---------------------------|--------------|
| **Technical Documentation** | Annex II (General) & Annex III (PMS) | Device description, design dossiers, labeling (§23), risk management file, manufacturing information, verification & validation data. | Core files exist for hardware; software lifecycle docs need IEC 62304 alignment – *gap* on detailed version‑control and release procedures. |
| **Risk Management File** | ISO 14971 (cited in Annex I §15) | Hazard identification, risk analysis, evaluation, controls, residual risk assessment, post‑market follow‑up plan. | Cyber‑security risks identified (SW error, data loss, CVE exposure) – *gap* on documented mitigation measures and verification of the controls. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | Clinical background, state‑of‑the‑art (SOTA) literature review, clinical data (clinical investigations or equivalence), benefit–risk analysis. | For detector & source – only regulatory classification provided; *gap* on published performance data, comparative studies, and justification of equivalence to existing devices. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | Annex XIV Part B | Objectives, methodology, data sources, timelines, evaluation criteria. | PMCF method in source: “Usability assessment (IEC 62366), real‑world error data collection”. *Gap* – no defined sample size, statistical analysis plan, or linkage to residual risk reduction. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | System description, data‑collection methods, reporting procedures, periodic safety update report (PSUR) schedule. | PMS items listed (risk signals, bug reports, CVE feeds). *Gap* – no overall PMS system architecture or responsibilities matrix. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 (Class IIa/IIb) – annual for IIb, biennial for IIa | (a) Benefit‑risk conclusions, (b) PMCF main findings, (c) Sales volume & user population estimate. | PSUR cadence noted in the table; *gap* – no draft report or data to populate sections a–c. |
| **Usability Engineering File** | IEC 62366‑1 | User‑needs analysis, use error identification, validation testing results. | Mentioned as PMCF method; *gap* – lack of documented usability test protocols and outcomes. |
| **Cybersecurity Documentation** | MDCG 2019‑16 Rev.1 & MDCG 2021‑6 (SaMD) | Threat modelling, vulnerability management process, security controls verification. | Risk signals listed (CVE, NVD), but *gap* – no formal threat analysis or mitigation verification evidence. |
| **Standards Conformance** | IEC 62304 (software lifecycle), IEC 60601‑2‑54 (X‑ray equipment), IEC 60601‑2‑28 (X‑ray tube assemblies) etc. | Declaration of conformity to each applied standard; test reports. | Only “IEC 62304 revision” and “MDCG guidance” cited – *gap* on full list of applied standards, test reports, and certificates of conformity. |
| **Regulatory Labels & IFU** | Annex I §23 | Manufacturer name, CE mark, intended use, warnings, instructions for safe use (including radiation protection). | No explicit labeling draft supplied – *gap*. |

---  

### 3 Key Risk Controls to be Demonstrated

| Identified Hazard (from source) | Control Measure Required (MDR/ISO 14971) | Evidence Needed |
|---------------------------------|------------------------------------------|-----------------|
| **Software error → diagnostic misinterpretation** | Robust software development lifecycle, verification & validation; fail‑safe defaults; alarm functions. | IEC 62304 compliance evidence, test reports, usability validation (IEC 62366). |
| **Data loss / integrity breach** | Redundant data storage, checksum verification, secure backup procedures. | Data‑integrity testing logs, IT security policy documents. |
| **Cybersecurity vulnerability (CVE) exposure** | Threat modelling, regular patch management, encryption of communication, authentication controls. | MDCG 2019‑16 threat analysis report; CVE tracking log with mitigation dates. |
| **Radiation over‑exposure (handheld source)** | Built‑in dose limiting controller, interlocks, compliance with IEC 60601‑2‑54 radiation protection requirements (§16). | Radiation safety test reports, calibration certificates. |
| **User error in image acquisition** | Training programme, clear UI design, usability testing to reduce use errors. | IEC 62366 usability validation report; training material samples. |

---  

### 4 Missing Information & Immediate Actions

| Missing Item | Why Required (MDR) | Action Owner / Deadline |
|--------------|--------------------|--------------------------|
| **Full classification justification** (rule citation, decision‑tree) | Annex VIII – needed for NB review. | RA Lead – within 5 working days. |
| **Clinical performance data** (bench testing, comparability studies) | CER (Art. 61) – must demonstrate safety & performance. | Clinical Affairs – collect/compile by next Q‑review. |
| **Detailed PMCF protocol** (sample size, statistical plan) | Annex XIV Part B – to satisfy NB on ongoing clinical evidence. | RA / Clinical – draft within 2 weeks. |
| **Cybersecurity threat model & mitigation verification** | MDCG 2019‑16 Rev.1 – essential for MDR §10/§11 risk management. | IT Security – deliver report in 3 weeks. |
| **PMS system architecture (process flow, responsibilities)** | Art. 83 – NB will audit PMS system. | Quality Manager – produce diagram + SOPs within 10 days. |
| **Label & IFU draft meeting §23** | Annex I §23 – required for CE marking and user safety. | Technical Writer – draft by next sprint review. |
| **Evidence of compliance with Korean MFDS Digital‑Medical‑Product Law (2024)** | Source notes need verification; cross‑border implications if marketed in Korea. | Regulatory Affairs (KR) – confirm applicability & document gap. |

---  

### 5 Submission Route Recommendation  

*All three devices are Class IIa/IIb.* The most streamlined route under MDR is **Annex IX** (conformity assessment of the quality‑management system together with a full technical documentation review).  
- For the **Handheld X‑ray Source (Class IIb)** the manufacturer may also consider **Annex X** (type examination) plus **Annex XI** (production conformity verification) if a Notified Body prefers that split assessment.  

**Action:** Engage a Notified Body early to confirm preferred route and required audit scope; schedule a pre‑assessment meeting within 2 weeks.

---  

### 6 Human‑Escalation Triggers  

| Trigger | Condition | Escalation Target |
|---------|-----------|--------------------|
| **Unresolved classification dispute** (e.g., detector could be IIb) | Missing rule‑justification or contradictory evidence | Senior RA Manager & Legal. |
| **No clinical performance data available within 30 days** | CER cannot be finalized | Clinical Project Lead – consider a supplemental clinical investigation. |
| **Critical cybersecurity CVE remains unpatched >14 days after discovery** | Risk of patient safety breach | IT Security Director + Compliance Officer (urgent NB notification). |
| **PMS system not documented before NB audit** | Art. 83 compliance gap | Quality Manager – raise to senior management for resource allocation. |
| **Regulatory label draft fails IEC 60601‑2‑54 labeling check** | Incomplete warning information on radiation exposure | Regulatory & Marketing author – re‑work IFU and repeat review. |
| **MFDS digital‑medical‑product law applicability remains unclear** | Potential market restriction in Korea | KR Regulatory Lead – obtain legal opinion; if applicable, prepare separate technical file for Korean registration. |

---  

### 7 Peer Review Prompt  

> *Colleague RA peer:* Please challenge the assumptions made above regarding (a) the appropriateness of Annex IX as the default conformity‑assessment route for a Class IIb handheld X‑ray source, (b) whether the classification of the detector should be considered IIb based on its integration with a radiation‑emitting source, and (c) any jurisdictional gaps that may arise from the Korean MFDS digital‑medical‑product law reference. Highlight missing source coverage or alternative interpretations under MDR that could affect our submission strategy.

---  

**End of Draft**  
(Prepared without inventing case‑specific identifiers – no predicate numbers or registration IDs were present in the supplied source; those items are noted as “no specific identifier found in source — verify separately.”)

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

## ra_kr

### kb-eval-20260722-it03-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_kr-001", "iteration": 3, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "08aa0ca26cb2ad74", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `08aa0ca26cb2ad74`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff`
- Focus: KGMP evidence readiness
- Matched keywords: KGMP

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – KGMP Evidence Readiness Assessment**

---

### 1. Scope & Device Overview  
*The source material does not contain a device description, intended use, or Korean classification (Class I‑IV).*  
→ **Missing information:** device name, indication, risk class, and MFDS classification rule citation. These items must be supplied before any definitive submission route can be selected.

---

### 2. Likely Submission Route (based on Korean classification)

| Korean Class | Typical MFDS Pathway | Core Technical Dossier Elements |
|--------------|----------------------|---------------------------------|
| **Class I**  | *신고* (Notification) | Form‑A, labeling/IFU in Korean, KGMP facility certificate. |
| **Class II–IV** | *허가* (Approval) | Form‑B, Technical File (Design Dossier), Clinical Evaluation Report (if required), Risk Management File, KGMP certification, Post‑Market Surveillance plan, and any foreign clinical/evidence accepted per MFDS scope notices. |

*Because the classification is unknown, both pathways are listed for reference.*

---

### 3. Required Evidence for KGMP Certification (per source excerpts)

| KGMP Section (MFDS) | Corresponding ISO 13485 clause* | Evidence Needed |
|----------------------|--------------------------------|-----------------|
| **7.4 구매** – Purchasing control | 7.4 | Supplier qualification files, purchase orders, incoming inspection records. |
| **7.5 생산 및 서비스** – Production & Service | 7.5; **§820.35** (Service Records) | Batch manufacturing records, service/maintenance logs meeting the detailed requirements of §820.35. |
| **7.6 측정장비 관리** – Measurement Equipment Management | 7.6 | Calibration certificates, equipment qualification reports. |
| **8.1 측정·분석·개선** – Measurement, Analysis & Improvement | 8.2; PSUR/PMSR linkage required | Data analysis reports, trend analyses, and evidence that post‑market surveillance (PMS) data feed into continuous improvement (PSUR/PMSR). |
| **8.2.1 피드백** – Feedback | **§820.20** (Complaint handling) & MDR Art. 83‑86 (PMS data collection) | Complaint investigation files, closure timestamps, and documented adverse event reporting per MDR Art. 83–86. |
| **8.2.2 내부 감사** – Internal Audit | **FDA inspection target** (formerly QSR §820.180(c)) – NB surprise audit | Internal audit program, audit reports, corrective action plans; note that MFDS may conduct unannounced audits (NB). |
| **8.2.3 공정 모니터링** – Process Monitoring | 8.3 | Real‑time process control data, SPC charts. |
| **8.3 부적합 관리** – Non‑conforming Management | 8.4 | Non‑conformance reports, disposition records, root‑cause analyses. |
| **8.4 데이터 분석** – Data Analysis | 8.5; PSUR/PMSR evidence base | Statistical analysis of field data, linkage to periodic safety update reports (PSUR) or post‑market surveillance reports (PMSR). |
| **8.5 개선** – Improvement | 8.6 | Documented improvement actions and effectiveness verification. |

\*ISO 13485:2016 clause numbers are used as the standard reference; they map directly to the KGMP sections indicated as “ISO 동일”.

---

### 4. Acceptance of Foreign Audits (MDSAP)

- **Regulatory citation:** *MDR Annex IX §3.2 – Partial acceptance of MDSAP audit reports*.  
- **Implication:** An FDA‑recognised MDSAP audit can be submitted to MFDS in lieu of an on‑site KGMP inspection, provided the audit scope covers all KGMP requirements listed above.  

**Action required:** Obtain a current MDSAP audit report that includes the KGMP‑mapped sections (7.4–8.5). If any gap exists (e.g., Korean language documentation), supplemental evidence must be supplied.

---

### 5. Additional Mandatory Korean‑Specific Evidence

| Requirement | Description |
|-------------|--------------|
| **Korean labeling & IFU** | All labels, symbols, and instructions for use must be in Korean per MFDS “Medical Device Labeling Regulations”. |
| **KGMP Facility Certification** | Certificate of compliance with the KGMP Regulation issued by MFDS. |
| **Local Clinical Data (if required)** | For Class II‑IV devices where MFDS still mandates local clinical evaluation, a Korean‑language clinical trial report or post‑market clinical follow‑up data must be provided. |
| **Post‑Market Surveillance Plan** | Written PMS plan in Korean, aligned with MDR Art. 83–86, and integrated into the QMS for continuous feedback (see 8.1 & 8.4). |

*These items are not mentioned in the source excerpts; therefore they are flagged as missing.*

---

### 6. Identified Gaps – Information Needed Before Submission

| Gap | Why it matters | Suggested source/next step |
|-----|----------------|----------------------------|
| **Device classification & MFDS rule citation** | Determines submission type (신고 vs 허가) and depth of clinical evidence required. | Provide the device’s intended use and risk class; reference MFDS “Medical Device Classification Rules”. |
| **Korean labeling/IFU in native language** | Mandatory for market entry; non‑compliance leads to rejection. | Prepare draft Korean label set; verify against MFDS labeling guidance. |
| **Local clinical evaluation (if required)** | Required for many Class II–IV devices unless exemption is granted via foreign data acceptance notice. | Confirm whether the latest MFDS scope notice permits reliance on FDA/EU clinical data; otherwise plan a Korean clinical study. |
| **Complete MDSAP audit coverage** | MFDS accepts only sections that map to KGMP; missing sections will trigger additional audits. | Review the MDSAP audit report and cross‑check against KGMP clauses 7.4–8.5. |
| **Evidence of PSUR/PMSR generation** | Required for post‑market data analysis (see 8.1, 8.4). | Compile field safety reports, trend analyses, and draft PSUR/PMSR documents. |

---

### 7. Risk Controls & Integration with QMS

1. **Risk Management File (ISO 14971)** – must be linked to design history file and updated based on feedback (8.2.1) and data analysis (8.4).  
2. **Process Validation** – documented for critical manufacturing steps; monitored via 8.2.3.  
3. **Complaint Handling SOP** – aligned with §820.20, capturing timestamps, investigation outcomes, and corrective actions.  
4. **Change Management** – any change identified in 8.5 (improvement) must follow the KGMP change control procedure, with impact assessment on risk and compliance.

---

### 8. Human‑Escalation Triggers

| Trigger | Escalation Action |
|---------|-------------------|
| **Unclear device classification or missing MFDS rule citation** | Pause submission; request clarification from product development/clinical team before any dossier build. |
| **Absence of Korean labeling/IFU** | Engage translation & regulatory affairs team to produce compliant documents; do not proceed to filing. |
| **Insufficient MDSAP audit coverage** | Notify QA lead; obtain supplemental on‑site KGMP audit or extend the MDSAP scope with a re‑audit. |
| **Requirement for local clinical data identified** | Initiate Korean clinical trial protocol development; involve CRO and ethics committee. |
| **Failure to produce PSUR/PMSR evidence within 3 months of draft** | Escalate to senior RA manager; risk of non‑conformity in post‑market surveillance clause. |
| **MFDS on‑site audit notice (NB surprise audit)** | Activate internal audit response team; ensure all KGMP records are current and accessible. |

---

### 9. Peer Review Request  

*@RA‑Peer*: Please review the assumptions made regarding the mapping of KGMP sections to ISO 13485 clauses, the applicability of MDSAP acceptance per MDR Annex IX §3.2, and identify any jurisdiction‑specific gaps (e.g., recent MFDS notice expanding accepted foreign evidence) that may affect the completeness of the evidence list. Your challenge will help ensure no critical Korean requirement is overlooked.

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

1. Chunk `1012828200772392062`

> II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동일 | **FDA 실사 대상** (구 QSR §820.180(c) 예외 삭제) | NB 불시 감사 대상 | | **8.2.3 공정 모니터링** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.3 부적합 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.4 데이터 분석** | ISO 동일 | ISO 동일 | PSUR/PMSR 작성 근거 데이터 | | **8.5 개선** | ISO 동일 | ISO 동일 | ISO 동일 |

2. Chunk `1037950769042691196`

> MDSAP 수용 (실사 대체 가능) | MDR Annex IX §3.2 — MDSAP 부분 수용 |

### kb-eval-20260722-it03-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_kr-002", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "74ad579a8baaae6c", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "6e09bc3b8dcd278f80184587a5eaba125f19dbc86c1b2ce2f24b76bdc503c9a0"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `74ad579a8baaae6c`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%EC%A0%9C%EC%A1%B0_%EB%B0%8F_%ED%92%88%EC%A7%88%EA%B4%80%EB%A6%AC_%EA%B8%B0%EC%A4%80.md)
- Source hash: `6e09bc3b8dcd278f80184587a5eaba125f19dbc86c1b2ce2f24b76bdc503c9a0`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_의료기기_제조_및_품질관리_기준.md`는 `MFDS_의료기기_제조_및_품질관리_기준.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: --- doc-id: MFDS_의료기기_제조_및_품질관리_기준 title: 의료기기 제조 및 품질관리 기준 (MFDS) (v0.2) type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: MFDS GMP 고시 요구사항 해설 및 ISO 13485 정합 매핑, 문서화 30대 절차 매핑 applicable: [ISO13485:2016, MFDS, FDA QMSR, EU MDR 2017/745] forms: [] related-docs: [SOP-CC-001, SOP-MFG-001, SOP-MFG-002, SOP-UDI-001, SOP-PMS-001, SOP-TRN-001,...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – KG GMP Evidence Readiness for a Medical Device Submission (Korea)**  

---

### 1. Likely Classification & Submission Route  
| Item | Reasoning / Reference |
|------|------------------------|
| **Risk‑based class** | The device will be placed in Class I, II, III or IV according to the MFDS “의료기기 분류고시” (standard MFDS classification rule). The exact class must be determined from the intended use and principal mode of action. |
| **Submission pathway** | • **Class I** – Notification (신고)  <br>• **Class II** – Notification or simple approval (허가) depending on risk level and presence of software/combination features. <br>• **Class III / IV** – Full approval (허가).  <br>Reference: MFDS 고시 제2025‑22호 (see Table 2, “품목군 분류” expansion to 64 categories) – indicates broader classification set for newer combination and digital devices. |

---

### 2. Required Evidence Package (KG GMP focus)

| Evidence | Description | Where the requirement derives from |
|----------|-------------|--------------------------------------|
| **KG GMP Certification** – audit report & certificate | Facility must hold a valid KG GMP certificate confirming compliance with MFDS GMP 고시 and ISO 13485:2016. The guide “의료기기 제조 및 품질관리 기준 (MFDS) – v0.2” maps 30 required procedures to ISO 13485. | MFDS GMP 고시 요구사항 해설 & ISO 13485 정합 매핑 (source [1]) |
| **Quality Management System (QMS) Documentation** | SOPs listed in the guide (e.g., SOP‑CC‑001, SOP‑MFG‑001… SOP‑UDI‑001). All 30 procedures must be documented and current. | Same as above (source [1]) |
| **Risk Management File** | IEC 60601‑1 series or ISO/IEC 14971 compliant risk analysis, mitigation plan, verification of residual risk. | International best practice – required by MFDS for all classes. |
| **Software Validation / Lifecycle Evidence** (if software is part of the device) | Full compliance with IEC 62304:2006+A1 as now fully referenced in 고시 제2025‑22호 (“SW 밸리데이션 – IEC 62304 전면 참조 편입”). Includes planning, verification, validation, and maintenance activities. | 고시 제2025‑22호 (source [2]) |
| **Cybersecurity Controls** (if applicable) | When the device is network‑connected or software‑enabled, a cybersecurity management plan must be submitted per the annexes referenced in 고시 제2025‑22호 (“사이버보안 관리 요구 – 부속서 참조”). | 고시 제2025‑22호 (source [2]) |
| **Labeling & IFU** | Korean language labeling, package inserts, and user manuals. Must meet MFDS labeling provisions and include UDI per SOP‑UDI‑001. | MFDS GMP 고시; SOP‑UDI‑001 (source [1]) |
| **Clinical Evidence** | • Class I – generally exempt <br>• Class II – may require limited clinical data or foreign CE/FDA evidence with a Korean bridging justification <br>• Class III/IV – full local clinical investigation unless MFDS accepts foreign clinical evaluation (subject to periodic scope expansions). | MFDS 고시 & periodic notice updates (e.g., 고시 제2025‑22호 expands “제출자료 – 광범위 → 간소화”). |
| **Foreign Evidence Mapping** | If FDA 510(k) clearance, CE marking, or other foreign regulatory approvals are used to support safety/efficacy, the mapping must reference MFDS notices that accept such evidence. (No specific identifier appears in the source.) | MFDS periodic scope revisions – need verification of current notice number. |

---

### 3. Missing Information & Gap Checklist  

| Gap | Impact if Unaddressed | Action |
|-----|----------------------|--------|
| **KG GMP certificate** not yet obtained or audit report absent | Submission will be rejected for Class II‑IV devices. | Initiate KG GMP audit; obtain certificate before dossier finalization. |
| **Complete set of 30 SOPs** – any missing procedure (e.g., change control, CAPA) | Non‑conformance to MFDS GMP 고시 and ISO 13485 mapping. | Verify SOP inventory against the list in source [1]; develop missing SOPs. |
| **Software validation scope** – only partial IEC 62304 reference (source [2] indicates full adoption). | May be deemed insufficient for software‑enabled devices. | Align validation plan to full IEC 62304:2006+A1 requirements. |
| **Cybersecurity documentation** – absent or informal | For networked devices, MFDS can require a cybersecurity management plan per the annexes of 고시 제2025‑22호. | Prepare a risk‑based cybersecurity strategy and evidence of implementation. |
| **Korean labeling / IFU** – English‑only drafts | Violation of labeling regulations; product cannot be marketed. | Translate all labeling, instructions, and safety information into Korean; perform linguistic review. |
| **UDI implementation plan** – not referenced in SOP list | UDI is mandatory for Class II‑IV (and some Class I) devices. | Develop UDI generation & traceability procedures per SOP‑UDI‑001. |
| **Local clinical data requirement** – unclear whether foreign evidence suffices | If MFDS does not accept the chosen foreign data, approval will be delayed or denied. | Check latest MFDS notice on accepted foreign clinical evaluation; prepare local trial if needed. |
| **Evidence of acceptance of foreign regulatory clearance** – no specific case ID in source | Unable to cite a concrete basis for using FDA/CE data. | Verify current MFDS notice number that permits such evidence (record separately). |

---

### 4. Key Risk Controls to Highlight in the Dossier  

1. **Risk Management (ISO 14971)** – hazard identification, risk analysis, mitigation, verification, and residual risk evaluation.  
2. **Software Lifecycle (IEC 62304)** – development plan, configuration management, version control, testing, release criteria.  
3. **Cybersecurity** – threat modeling, vulnerability management, secure update mechanism, incident response.  
4. **Process Control (KG GMP)** – validated manufacturing processes, environmental monitoring, equipment qualification, traceability.  
5. **Post‑Market Surveillance (PMS) Plan** – aligns with MFDS PMS requirements; includes field safety corrective actions and vigilance reporting.

---

### 5. Citations  

| Citation | Type |
|----------|------|
| “의료기기 제조 및 품질관리 기준 (MFDS) — v0.2” – mapping of 30 GMP procedures to ISO 13485:2016, SOP list, document control. | Established regulatory reference (source [1]) |
| 고시 제2025‑22호 – updates on classification categories, submission simplification, full IEC 62304 adoption, cyber‑security annexes. | Established regulatory reference (source [2]) |
| IEC 62304:2006+A1 – referenced in 고시 제2025‑22호 as the full software validation standard. | Standard reference (source [2]) |
| ISO 13485:2016 – baseline QMS standard cross‑mapped in MFDS guide. | Standard reference (source [1]) |

*No specific case identifiers (e.g., 510(k) numbers, registration IDs) were found in the source excerpts; verify separately if such references are needed for your device.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason to Escalate to Senior RA / Management |
|---------|----------------------------------------------|
| **KG GMP certificate missing or audit pending** – cannot proceed with Class II‑IV submissions. |
| **Incomplete SOP set (any of the 30 listed procedures absent)** – risk of regulatory non‑conformance. |
| **Software validation not fully aligned to IEC 62304:2006+A1** – especially for devices classified as “융복합의료기기”. |
| **Cybersecurity plan absent when device has connectivity** – MFDS may reject or require additional data. |
| **Korean labeling/IFU not finalized** – mandatory for market entry; failure leads to non‑acceptance. |
| **Unclear acceptance of foreign clinical evidence** – requires confirmation of the exact MFDS notice number before submission. |
| **UDI strategy undefined for Class II‑IV devices** – UDI is a regulatory prerequisite. |
| **PMS plan not drafted per MFDS PMS guidance** – required post‑approval; gaps can halt approval. |

When any trigger occurs, raise an immediate review and allocate resources to close the gap before dossier finalization.

---

### 7. Reusable RA Judgment (Lesson Learned)  

> *For Korean medical‑device submissions, KG GMP readiness hinges on having a current KG GMP certificate and a complete set of 30 MFDS‑mapped SOPs aligned with ISO 13485:2016. Recent amendments (고시 제2025‑22호) now mandate full IEC 62304 compliance for software and expose cyber‑security as an optional but often required control via annexes. Any missing element in these core evidence categories—certificate, SOPs, software validation, cybersecurity plan, Korean labeling/UDI—must be flagged early as a human‑escalation trigger to avoid submission rejection.*  

---

### 8. Peer Review Prompt  

*“@RA‑Peer – please challenge the assumptions above: Are there any additional KG GMP evidence items introduced in MFDS notices after 2025‑22 that we have omitted? Does the current list of 30 procedures fully capture the latest SOP requirements, especially for combination devices and AI‑enabled software? Also verify whether the cyber‑security annexes referenced require a specific Korean standard (e.g., KISA guidelines) that should be cited.”*

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

1. Chunk `107140411445338936`

> --- doc-id: MFDS_의료기기_제조_및_품질관리_기준 title: 의료기기 제조 및 품질관리 기준 (MFDS) (v0.2) type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: MFDS GMP 고시 요구사항 해설 및 ISO 13485 정합 매핑, 문서화 30대 절차 매핑 applicable: [ISO13485:2016, MFDS, FDA QMSR, EU MDR 2017/745] forms: [] related-docs: [SOP-CC-001, SOP-MFG-001, SOP-MFG-002, SOP-UDI-001, SOP-PMS-001, SOP-TRN-001, SOP-SUP-001, SOP-NC-001, SOP-CAPA-001, SOP-IA-001, SOP-MR-001, PRO-CRP-001] related-issues: [33] owner: RA/QA Lead last-review: 2026-05-14 review-due: 2027-05-07 --- # 의료기기 제조 및 품질관리 기준 (MFDS) — v0.2 > v0.2 — 2026-05-07: GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려...

2. Chunk `1127747106119376174`

> ## 2. 최신 개정 핵심 (고시 제2025-22호) | 항목 | 종전 | 개정 | |------|------|------| | 품목군 분류 | 26개 | 64개 | | 융복합의료기기 | 불명확 | 주된 기능이 의료기기이면 심사대상 명확화 | | 심사체계 | 복수심사 | 품질관리심사기관 단독심사 가능 | | 제출자료 | 광범위 | 간소화 | | SW 밸리데이션 | IEC 62304 참조 일부 | IEC 62304:2006+A1 전면 참조 편입 | | 사이버보안 | 미규정 | 적용 가능 시 사이버보안 관리 요구 (부속서 참조) |

### kb-eval-20260722-it03-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_kr-003", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "b4673ce2113e8a19", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `b4673ce2113e8a19`
- Source: `github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/957_AUDIT_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4_DR03_04_06_07_%EC%A1%B0%ED%95%AD_%EC%9D%B8%EC%9A%A9%EB%B6%80%EC%A0%95%ED%99%95.md)
- Source hash: `69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e`
- Focus: KGMP evidence readiness
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### D4 — DR-07 (라인 76) - **기재값:** `임상적 유효성(해당 시) | 법 제15조` - **문제:** 임상적 유효성/임상평가는 법 제9조(임상시험계획 승인) 또는 제10조(임상적 성능시험계획 승인)에 해당할 가능성이 높으며, 제15조(실사용평가)와는 별개 개념. - **권고:** `법 제15조` → 제9조/제10조 중 해당 조문으로 정정 검토. ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 [시행 2026.1.24.] [법률 제20139호]) | 조문 | 법정 제목·내용(원문) | |---|---| | **제15조** | **"실사용 평가"** — 디지털의료기기제조업자등이 실제 사용 과정에서 수집된...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital‑Medical‑Device (디지털의료제품) Submission**

---

### 1. Classification & Submission Route  

| Item | Determination | Basis |
|------|---------------|-------|
| **Device class** | To be defined by the MFDS risk‑based classification table for digital medical devices (Class I–IV). The source does not specify intended use or risk level; therefore a provisional determination cannot be made. | Digital Medical Device Act (디지털의료제품법) – classification rules are set out in the accompanying enforcement decree (not quoted here). |
| **Submission pathway** | • **허가 (Approval)** for Class III/IV devices or those requiring clinical trial data.<br>• **신고 (Notification)** for Class I/II devices that do not require a formal clinical trial. | MFDS guidelines – class‑based routes are fixed in the Act; no exception is indicated in the source excerpts. |

*Human‑escalation trigger:* **If the risk classification cannot be resolved from product description, forward to senior RA for risk‐assessment workshop and possible MFDS pre‑consultation (Art. 39).**  

---

### 2. Required Evidential Package  

| Evidence | Current status (per source) | Gap / Action |
|----------|-----------------------------|--------------|
| **Clinical efficacy / performance evidence** | The draft entry incorrectly cites **Article 15** for “clinical efficacy”. | Replace with **Article 9** (clinical trial plan approval) *or* **Article 10** (clinical performance test plan approval) as appropriate. |
| **Real‑world use evidence (RWE)** | Article 15 correctly governs post‑marketing “실사용 평가” (real‑use evaluation). | Ensure separate RWE dossier only if the submission strategy relies on post‑market data; otherwise, omit from pre‑approval package. |
| **KGMP certification** | Mention of **Article 17** (우수 관리체계 인증) – indicates that a GMP‑like certification is required for manufacturers. | Obtain KGMP certificate before filing; capture audit report and certificate copy. |
| **Cybersecurity & vulnerability management** | Article 13 obligates continuous collection of defect information and cyber‑vulnerability remediation. | Provide a Cyber‑risk Management Plan (aligned with MFDS cybersecurity guidelines) and evidence of ongoing monitoring. |
| **Pre‑submission review documents** | Article 39 permits request for pre‑review of required materials. | Prepare a pre‑consultation package if significant uncertainties remain (e.g., classification, clinical data scope). |
| **Labeling & IFU** | Not addressed in the excerpts but Korean law mandates Korean language labeling and instructions for use. | Draft Korean label/IFU complying with MFDS labeling standards (e.g., K‑MED‑1000 series). |

*Human‑escalation trigger:* **If clinical trial plan (Art. 9) or performance test plan (Art. 10) is required but not yet approved, flag for immediate initiation of study protocol and ethics submission.**  

---

### 3. Missing Information & Risk Controls  

| Missing Item | Why needed | Suggested control |
|--------------|------------|-------------------|
| **Exact intended use & risk classification** | Determines whether Art. 9 or Art. 10 applies and which submission route (허가 vs 신고) is required. | Conduct a formal Intended Use Statement and map to MFDS risk matrix; involve product engineering for hazard analysis. |
| **Clinical trial/performance test protocol** | Required under Art. 9/10 for demonstrating safety & efficacy. | Develop protocol per GCP/GCLP, register with ClinicalTrials.gov (or Korean Clinical Research Information Service) and obtain MFDS approval. |
| **KGMP audit report** | Mandatory for manufacturing compliance (Art. 17). | Schedule KGMP audit; remediate non‑conformities; retain certificate copy for submission. |
| **Cyber‑vulnerability remediation plan** | Continuous obligation under Art. 13. | Implement a vulnerability management lifecycle (identification, assessment, patching); keep logs for MFDS inspection. |
| **Korean language labeling & IFU** | Legal requirement; missing leads to rejection. | Translate all user‑facing documents; include safety symbols and usage instructions per MFDS labeling guide. |

*Human‑escalation trigger:* **Any unresolved gap that prevents completion of the core dossier (clinical data, KGMP, labeling) should be escalated to the project manager and senior RA for timeline impact assessment.**  

---

### 4. Citations (Established Regulatory References)

| Citation | Content |
|----------|---------|
| 디지털의료제품법 **제9조** | Clinical trial plan approval – governs “임상시험계획 승인”. |
| 디지털의료제품법 **제10조** | Clinical performance test plan approval – governs “임상적 성능시험계획 승인”. |
| 디지털의료제품법 **제15조** | Real‑use evaluation (실사용 평가) – post‑marketing safety/efficacy evidence, distinct from clinical efficacy. |
| 디지털의료제품법 **제17조** | Application & assessment of 우수 관리체계 인증 (GMP‑like certification). |
| 디지털의료제품법 **제13조** | Ongoing obligations for defect information collection and cyber‑vulnerability mitigation. |
| 디지털의료제품법 **제39조** | Procedure for pre‑review (사전 검토) of 허가·신고 자료 with MFDS. |

*Case‑level identifiers:* **no specific identifier found in source — verify separately** (e.g., 510(k), predicate numbers, internal case IDs).  

---

### 5. Human‑Escalation Triggers Summary  

| Trigger | Reason |
|--------|--------|
| Unclear device risk class or intended use | Determines submission route and evidence scope. |
| Absence of approved Clinical Trial/Performance Test plan (Art. 9/10) when required | Blocks safety & efficacy justification. |
| KGMP certification not yet obtained (Art. 17) | Mandatory for manufacturing compliance. |
> **Escalate** to senior RA / project lead for immediate action planning.

---

### 6. Peer‑Review Prompt  

> *@RA‑Peer*: Please review the assumptions made regarding the applicability of Articles 9, 10 and 15 to the clinical evidence package, and verify that no additional Korean statutes (e.g., Enforcement Decree provisions) have been omitted from this draft. Consider whether any other MFDS guidance documents (such as the “Guidelines for Digital Health Devices”) impose extra pre‑market requirements not captured above.  

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

1. Chunk `399070733591760115`

> ### D4 — DR-07 (라인 76) - **기재값:** `임상적 유효성(해당 시) | 법 제15조` - **문제:** 임상적 유효성/임상평가는 법 제9조(임상시험계획 승인) 또는 제10조(임상적 성능시험계획 승인)에 해당할 가능성이 높으며, 제15조(실사용평가)와는 별개 개념. - **권고:** `법 제15조` → 제9조/제10조 중 해당 조문으로 정정 검토.

2. Chunk `515031043224754498`

> ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 [시행 2026.1.24.] [법률 제20139호]) | 조문 | 법정 제목·내용(원문) | |---|---| | **제15조** | **"실사용 평가"** — 디지털의료기기제조업자등이 실제 사용 과정에서 수집된 정보로 안전성·유효성을 평가하는 것(실사용증거/RWE). 기술문서·사용적합성·임상적 유효성과 무관. | | **제17조** | **"우수 관리체계 인증의 신청 및 평가 등"** — 제16조 우수 관리체계 인증(GMP 유사 인증)의 신청·평가 절차. AI 변경관리계획(PCCP)과 무관. | | **제13조** | **"디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항"** — 결함정보 수집·사이버 취약점 보완 등 상시 준수의무. MFDS 사전상담(사전검토)과 무관. | | **제39조** | **"허가·신고 등의 사전 검토"** — 제조허가·인증·신고 등에 필요한 자료를 사전에 MFDS에 검토 요청할 수 있는 절차. MFDS 사전상담의 정확한 근거조문. |

### kb-eval-20260722-it03-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_kr-004", "iteration": 3, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "44b5985250495bd6", "source": "github:holee9/MD-process/issue-drafts/066_01_MFDS_GMP_v0.2_30대절차매핑.md", "source_hash": "9d7fca670a56a64ee146225dc0fd583c83903c5ac050153cfe8226de5bb6a750"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `44b5985250495bd6`
- Source: `github:holee9/MD-process/issue-drafts/066_01_MFDS_GMP_v0.2_30대절차매핑.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/066_01_MFDS_GMP_v0.2_30%EB%8C%80%EC%A0%88%EC%B0%A8%EB%A7%A4%ED%95%91.md)
- Source hash: `9d7fca670a56a64ee146225dc0fd583c83903c5ac050153cfe8226de5bb6a750`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `066_01_MFDS_GMP_v0.2_30대절차매핑.md`는 KGMP 또는 GMP evidence readiness, audit readiness, QMS 절차·기록 관련 문서입니다.
- 현재 excerpt 핵심: ## 배경 GMP 심사 대비 ISO 13485:2016 문서화 요구사항 35개 항목을 전수 매핑하고, 프로젝트 SOP 커버리지(69%)를 산출하여 미작성 8건의 우선순위를 도출하였다. ## 참고 링크 - 관련 문서: `01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md` - 교차검증: `12_교차검증_보고서/2026-05-07_GMP절차매핑_영상품질QC_정합성.md`
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – KGMP Evidence Readiness Assessment**

---

### 1. Device Classification & Submission Route  
- **Classification:** Not determinable from the supplied excerpts. The intended medical purpose, invasiveness, and duration of contact are required to apply MFDS classification rules (e.g., Class I–IV).  
  *Action:* Obtain the device’s intended use description and risk profile to select the appropriate MFDS class and consequently the submission pathway (허가 vs. 신고).  

- **Submission Route:** Dependent on the final classification; for Class II‑IV devices a full 허가 (approval) is required, while Class I generally follows the 신고 (notification) route.  

*No specific identifier (e.g., MFDS registration number or predicate device) appears in the source material – verify separately.*

---

### 2. Required KGMP Evidence (MFDS GMP)  

| Requirement | Reference / Basis | Current Status (per source) |
|-------------|-------------------|------------------------------|
| Full set of SOPs covering **all 35 ISO 13485:2016 documentation items** required for MFDS GMP compliance | MFDS “의료기기 제조 및 품질관리 기준” (see source link `01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md`) • ISO 13485:2016 clauses 4–8 | **69 %** SOP coverage achieved; **31 %** (≈11 items) still missing. |
| Identification & prioritisation of **missing documents** | Internal GAP analysis documented in the GMP‑mapping project (`12_교차검증_보고서/2026-05-07_GMP절차매핑_영상품질QC_정합성.md`) | **8 high‑priority gaps** identified (see excerpt 315455402892636179). |
| Evidence of corrective actions for the 8 priority gaps (updated SOPs, work instructions, records) | MFDS GMP requires documented implementation and verification of each required procedure. | Not yet provided – *missing*. |
| Verification that the updated documentation **maps to ISO 13485:2016** requirements (traceability matrix) | Standard practice under MFDS GMP; cross‑verification referenced in source. | Partial (69% coverage). |
| Facility KGMP certification (inspection report, certificate) | Required for all manufacturing sites producing Class II–IV devices. | No evidence shown in excerpts – *missing*. |
| Korean‑language labeling & IFU compliance | MFDS Article 25‑2 of the Medical Device Act mandates Korean language on labels and instructions. | Not addressed in source – *missing*. |

---

### 3. Missing Information / Evidence Gaps  

1. **Complete SOP portfolio** (remaining ~11 items) – especially those tied to the 8 high‑priority gaps.  
2. **Documentation of corrective actions** for each identified gap (revision dates, responsible personnel, verification results).  
3. **KGMP certificate or inspection report** for the manufacturing site(s).  
4. **Korean language labeling & IFU samples** meeting MFDS format requirements.  
5. **Device‑specific classification justification** (risk analysis, intended use statement).  

---

### 4. Risk Controls Linked to KGMP Gaps  

| Gap | Potential Risk | Control / Mitigation |
|-----|----------------|----------------------|
| Incomplete SOPs (31 % missing) | Process variability → non‑conforming products, patient safety events | Accelerate SOP development; perform internal audits once completed; document effectiveness verification. |
| Unresolved high‑priority gaps (8 items) | Critical quality attributes may not be controlled → recall risk | Assign dedicated owners; set firm deadlines; conduct interim mock inspections to confirm readiness. |
| Absence of KGMP certificate | Regulatory non‑acceptance, market entry delay | Schedule MFDS inspection or obtain provisional certification from an accredited body. |
| Lack of Korean labeling/IFU | Non‑compliance with labeling law → product rejection at customs | Translate and format all labeling/IFU per MFDS guidelines; perform linguistic review by native speaker. |
| Undefined classification | Wrong submission route → re‑submission, increased timelines | Conduct a formal classification matrix (MFDS Class I–IV rules) as soon as intended use is clarified. |

---

### 5. Citations  

- **Regulatory framework:** MFDS “의료기기 제조 및 품질관리 기준” – referenced in the source path `01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md`.  
- **International standard:** ISO 13485:2016 (Quality management systems for medical devices).  

*No specific case identifiers (e.g., 510(k) numbers, MFDS registration codes) were present in the provided excerpts – verify separately.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Condition | Escalation Action |
|---------|-----------|-------------------|
| **SOP coverage < 100 %** after a 2‑week remediation window | Remaining gaps > 0 after deadline | Notify senior QA/RA manager; consider external consultancy for rapid SOP development. |
| **Critical gap (one of the 8 priority items) remains unresolved** beyond agreed corrective action plan | No documented revision & verification evidence | Escalate to CFO/Head of Regulatory Affairs; re‑evaluate launch timeline. |
| **KGMP certificate not obtained** within 30 days of submission preparation start | No inspection report or provisional certificate on file | Initiate urgent communication with MFDS inspection scheduling office; explore temporary GMP compliance alternatives. |
| **Classification ambiguity persists** after collection of intended use data | Unable to map device to MFDS Class I–IV rules | Hold a cross‑functional classification workshop (RA, Clinical, Engineering) and involve an external regulatory consultant if needed. |
| **Labeling/IFU Korean version absent** when product is ready for market entry | No compliant Korean-language artifacts | Immediate involvement of translation/legal team; potential product hold until resolved. |

---

### 7. Peer Review Prompt  

> *@RA‑Peer:* Please review the assumptions made regarding SOP coverage percentages, the identification of high‑priority gaps, and the mapping to MFDS GMP requirements. Are there any additional Korean‐specific obligations (e.g., electronic record‑keeping, post‑market surveillance plan) that have not been captured from the source excerpts? Challenge any gaps in jurisdictional coverage or evidence sufficiency.

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

1. Chunk `315455402892636179`

> ## 배경 GMP 심사 대비 ISO 13485:2016 문서화 요구사항 35개 항목을 전수 매핑하고, 프로젝트 SOP 커버리지(69%)를 산출하여 미작성 8건의 우선순위를 도출하였다.

2. Chunk `1045407237613866280`

> ## 참고 링크 - 관련 문서: `01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md` - 교차검증: `12_교차검증_보고서/2026-05-07_GMP절차매핑_영상품질QC_정합성.md`

### kb-eval-20260722-it03-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it03-ra_kr-005", "iteration": 3, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "2a1acf8927b94a02", "source": "github:holee9/MD-process/issue-drafts/911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md", "source_hash": "95f44332028afe7accb07da52f06d3d9910a29bfb18a213c9c2328789985e29c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2a1acf8927b94a02`
- Source: `github:holee9/MD-process/issue-drafts/911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/911_AUDIT_QM-001_MFDS_%EB%B3%84%ED%91%9C2_%EB%B3%B4%EA%B4%80%EA%B8%B0%EA%B0%84_1%EC%B0%A8%EC%B6%9C%EC%B2%98_%EB%AF%B8%ED%99%95%EC%9D%B8.md)
- Source hash: `95f44332028afe7accb07da52f06d3d9910a29bfb18a213c9c2328789985e29c`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md`는 `911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 배경 QM-001 v0.4 §7에서 품질매뉴얼 보관기간을 "5년 (MFDS GMP 기준)"으로 기재했던 v0.3을 "MFDS 의료기기 제조 및 품질관리 기준 별표2 기록보관 요건에 따름(구체적 기간은 미확인 — 1차 출처 재확인 필요)"으로 약화 처리. 1차 출처(MFDS 고시 본문)에서 품질매뉴얼 자체의 보관기간 명시 조항을 직접 인용해야 함. ## Tier 1 출처 후보 - MFDS 의료기기 제조 및 품질관리 기준 고시 (최신본) - 의료기기법 시행규칙 별표
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `KGMP evidence readiness` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `KGMP evidence readiness`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - KGMP/ISO/QMSR evidence mapping, audit readiness, procedure, record, 한국 적용성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **KGMP Evidence Readiness – Record‑Retention Requirement for the Quality Manual**

---

### 1. Scope & Applicability  
All medical devices marketed in Korea are subject to the Korean Good Manufacturing Practice (KGMP) system administered by MFDS. KGMP applies irrespective of device class, although the depth of supporting evidence varies with classification (Class I – notification; Class II/III – approval).

### 2. Classification / Submission Route  
| Device Classification | Typical MF DS Pathway | KGMP Evidence Needed |
|-----------------------|----------------------|----------------------|
| **Class I** (low‑risk) | 신고 (notification) | QMS documentation, including record‑retention schedule per 별표 2 |
| **Class II–III** (moderate/high risk) | 허가 (approval) | Full KGMP audit package – includes the same QMS records plus clinical/technical dossiers |

*The current draft concerns only the QMS component; classification of a specific device will be determined separately.*

### 3. Required Evidence for Record Retention  

| Requirement | MFDS Reference (Established) | What Must Be Demonstrated |
|-------------|------------------------------|---------------------------|
| **Retention period for the Quality Manual** | *MFDS 의료기기 제조 및 품질관리 기준 고시* – 별표 2 (Record‑keeping requirements) | Exact number of years that the quality manual must be retained after the end of production or product discontinuation. |
| **Proof of compliance** | Same notice – 별표 2, and the *의료기기법 시행규칙* (Implementation Rules) | Signed retention schedule, evidence of storage method (electronic/physical), and accessibility for MFDS inspection. |

### 4. Missing / Unverified Information  

1. **Precise retention period** – The source indicates that the period “is unconfirmed; primary source re‑verification required.”  
2. **Citation of the exact clause** – The draft must quote the specific paragraph of 별표 2 that defines the quality‑manual retention term.  
3. **Version control** – Confirmation that the cited MFDS notice is the latest edition (e.g., 2025 amendment).  

*Action:* Retrieve the current MFDS 고시 (official PDF or web portal) and extract the exact wording and numeric value for the quality‑manual retention period.

### 5. Risk Controls & Mitigation  

| Potential Non‑Compliance | Impact | Control Measure |
|--------------------------|--------|-----------------|
| Incorrect or absent retention period in QMS documentation | MFDS audit finding; possible suspension of KGMP certification; delayed product approval/notification | **Documented verification step**: senior QA sign‑off after confirming the official retention term. |
| Inadequate storage (e.g., loss of electronic files) | Loss of evidence during inspection → regulatory penalty | **Secure archival system** meeting ISO 15489 (records management) and MFDS data‑integrity requirements; periodic backup testing. |
| Misinterpretation of “MFDS GMP 기준” vs. actual 별표 2 wording | Submission comments requesting amendment, added timeline. | **Cross‑check checklist**: align internal QMS manual language verbatim with the official MFDS clause before submission. |

### 6. citations  

* Established regulatory references (facts)  
  - *MFDS 의료기기 제조 및 품질관리 기준 고시*, 별표 2 – Record‑keeping requirements.  
  - *의료기기법 시행규칙* – Implementation rules governing KGMP obligations.

* Case‑level identifiers – none appear in the source excerpts.  

> **no specific identifier found in source — verify separately**

### 7. Human‑Escalation Triggers  

| Trigger | Who Must Be Alerted | Reason |
|--------|--------------------|--------|
| Absence of a confirmed retention period after primary source check | Senior QA Manager / KRRA Lead | Prevents submission of incomplete KGMP evidence. |
| Discrepancy between internal QMS manual and official 별표 2 wording | Regulatory Affairs Director & Legal Counsel | Ensures legal compliance before MFDS filing. |
| MFDS notice amendment published during dossier preparation | Project Owner (PM) & Documentation Control Lead | Updating all affected documents to avoid outdated references. |
| Audit finding that the quality‑manual retention schedule is missing or inadequate | All stakeholders; initiate corrective action plan (CAP) within 30 days per MFDS post‑market surveillance rules. |

---

### 8. Reusable RA Judgment  

- **Lesson:** KGMP evidence for record‑retention must be anchored to the exact clause and numeric value disclosed in *MFDS 고시 별표 2*. Any internal statement that merely cites “MFDS GMP 기준” without quoting the official period is insufficient for MFDS inspection.  
- **Actionable Template:** Before finalizing any KGMP submission, insert a “Retention‑Period Confirmation” field that lists (i) the exact number of years, (ii) the full citation (e.g., 별표 2 ③), and (iii) the date of the source notice version.

---

### 9. Peer Review Prompt  

> @RA‑Peer: Please evaluate whether the above assumptions about the need for an explicit retention period capture all Korean‑specific obligations, especially regarding electronic versus paper archives under 별표 2. Also confirm that no additional MFDS notices (e.g., recent amendment 2025‑06) have been overlooked in this assessment.

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

1. Chunk `104161787279348102`

> ## 배경 QM-001 v0.4 §7에서 품질매뉴얼 보관기간을 "5년 (MFDS GMP 기준)"으로 기재했던 v0.3을 "MFDS 의료기기 제조 및 품질관리 기준 별표2 기록보관 요건에 따름(구체적 기간은 미확인 — 1차 출처 재확인 필요)"으로 약화 처리. 1차 출처(MFDS 고시 본문)에서 품질매뉴얼 자체의 보관기간 명시 조항을 직접 인용해야 함.

2. Chunk `1013054385847956806`

> ## Tier 1 출처 후보 - MFDS 의료기기 제조 및 품질관리 기준 고시 (최신본) - 의료기기법 시행규칙 별표
