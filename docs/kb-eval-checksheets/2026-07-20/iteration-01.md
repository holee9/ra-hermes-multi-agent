# KB Eval Checksheet - 2026-07-20 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260720-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "cfec7e87e34c3351", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md", "source_hash": "7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503"} -->

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

> **Regulatory Draft – Cyber‑Security Evidence Package for 510(k) Submission**

---

### 1. Classification & Submission Pathway  
| Item | Determination |
|------|---------------|
| **Device Class** (based on intended use & FDA product code) | *Assumed Class II* – most software‑enabled medical devices fall in Class II unless a predicate indicates otherwise. |
| **Regulatory Route** | Traditional 510(k) with Substantial Equivalence claim. <br>*Legal basis*: **Section 524B(b)(3), FD&C Act** (mandatory SBOM requirement). |
| **Relevant FDA Guidance** | “2025 Cybersecurity Guidance for Medical Devices” (referred to in source as *524B + 2025 Guidance*). |

*If the device is Class I or III, the pathway would shift to de Novo/PMAs; this must be verified before final submission.*

---

### 2. Mandatory Evidence Items (per FDA 524B & 2025 Guidance)

| # | Evidence Required | Detail / Format |
|---|-------------------|-----------------|
| **1** | **Software Bill of Materials (SBOM)** | • Must cover *all* software in the device: manufacturer‑developed, third‑party licensed, open source. <br>• Acceptable formats: **SPDX 2.3+** or **CycloneDX 1.5+** (machine‑readable JSON/XML). <br>• Fields per NTIA Minimum Elements (Supplier Name, Component Name, Version, Unique Identifier [CPE/PURL], Dependency Relationship, Author, Timestamp). |
| **2** | **Threat Model** | • Conduct using the **STRIDE** methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial‑of‑Service, Elevation of Privilege). <br>• Document identified threats, risk level, and mitigations. |
| **3** | **Cybersecurity Management Plan (CMP) / Vulnerability Management Plan (VMP)** | • Define processes for *pre‑market* security design, *post‑market* monitoring, patch deployment, incident response, and CVD reporting. |
| **4** | **Penetration Test Report** *(recommended but not mandatory)* | • Independent or internal testing of the device’s attack surface. Include scope, methodology (e.g., OWASP Mobile/IoT), findings, and remediation actions. |
| **5** | **Standards Conformance Evidence** | • Demonstrate compliance with **IEC 81001‑5‑1** (Cybersecurity for medical devices) and alignment to the **NIST Cybersecurity Framework (CSF)** – include mapping matrix. |
| **6** | **Post‑Market Surveillance (PMS) / Vigilance Plan** | • Ongoing monitoring of vulnerabilities, patch lifecycle, and adverse event reporting (per FDA requirement for “patch, CVD, monitoring”). |

---

### 3. Evidentiary Gaps Identified from Source

| Gap | Why Critical & What to Supply |
|-----|------------------------------|
| **Device Classification & Predicate** | Needed to confirm Class II status and identify a legally marketed predicate for the SE claim. |
| **Complete SBOM** | Source only shows field schema; actual populated list of components is missing. |
| **Full Threat Model Documentation** | Only “STRIDE recommended” noted – need concrete threat enumeration, likelihood/impact scores, and controls. |
| **CMP/VMP Detail** | General requirement indicated; must provide full process documentation, roles, timelines. |
| **Pen Test Results** | Guidance lists as *recommended*; absence will be flagged during review if not supplied. |
| **IEC 81001‑5‑1 & NIST CSF Mapping** | No evidence of systematic mapping; need matrix linking device controls to standard requirements. |
| **Post‑Market Patch Management Records** | Demonstrate capability to issue timely patches, track deployment, and report CVDs. |

---

### 4. High‑Level Risk Controls (to be reflected in the submission)

1. **Secure Software Development Lifecycle (SSDLC)** – code review, static/dynamic analysis, dependency scanning.  
2. **Authentication & Authorization** – role‑based access control, multi‑factor authentication for critical functions.  
3. **Data Protection** – encryption at rest (AES‑256) and in transit (TLS 1.3).  
4. **Patch Management** – automated vulnerability feed, defined patch release window (<30 days for critical CVEs).  
5. **Incident Response** – documented playbook, escalation matrix, forensic logging.  
6. **Supply Chain Controls** – vendor assessments, provenance verification of third‑party components (via SBOM).  

Each control should be linked to the corresponding threat in the STRIDE model and mapped to IEC 81001‑5‑1/NIST CSF controls.

---

### 5. Citations

| Item | Source |
|------|--------|
| Legal basis for SBOM requirement | **Section 524B(b)(3), FD&C Act** (explicitly cited in source) |
| Guidance reference | **2025 FDA Cybersecurity Guidance** (referenced as “524B + 2025 Guidance”) |
| SBOM format standards | **SPDX 2.3+**, **CycloneDX 1.5+** (source statement) |
| Threat model method | **STRIDE** (required per source) |
| Standard references | **IEC 81001‑5‑1**, **NIST Cybersecurity Framework** (listed under “표준 참조”) |

*No specific predicate numbers, 510(k) identifiers, or case IDs appear in the provided excerpts – verify separately.*

---

### 6. Human‑Escalation Triggers

| Trigger | Action Required |
|---------|-----------------|
| **Missing or incomplete SBOM** | Pause submission; request full component inventory from development. |
| **Absence of documented threat model** | Escalate to cybersecurity team lead for risk analysis completion. |
| **No CMP/VMP or insufficient detail** | Engage regulatory affairs manager to draft/expand plans per IEC 81001‑5‑1. |
| **Penetration test not performed when device classified as high‑risk (e.g., Class IIb/III)** | Seek senior RA review; consider external testing vendor engagement. |
| **Failure to map controls to IEC 81001‑5‑1/NIST CSF** | Forward to QA for standards alignment verification. |
| **Unclear device classification or predicate** | Immediate consultation with FDA liaison – potential need to shift submission pathway (e.g., De Novo). |
| **Post‑market patch process not demonstrable** | Alert product management; develop SOPs before filing. |

---

### 7. Summary Judgment

- The device is *most likely* a **Class II** medical device requiring a **traditional 510(k)** submission with substantial equivalence, anchored on **Section 524B(b)(3)** SBOM mandate and the 2025 FDA Cybersecurity Guidance.
- Core evidence gaps (complete SBOM, threat model, CMP/VMP, standards mapping, post‑market patch plan) must be remedied before filing.  
- Immediate human escalation is needed for any of the triggers above; otherwise, proceed to compile the full cybersecurity section and attach it as part of the 510(k) technical file.

---

**Peer Review Prompt (for another RA):**  

> *Please challenge the assumptions made about device classification, the completeness of the required evidence list, and potential jurisdictional gaps (e.g., EU MDR or MFDS alignments) that might affect our submission strategy.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 117/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,840자 | — |
| 규제 식별자 인용 | 1개 | — |
| source excerpt 근거 일치 | **1/1 (100%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 0개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 낮음**

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "77b9bccadf30a05f", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

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

> **Regulatory Draft – AI/ML‑Based Medical Device (SaMD) Submission Plan**

| Item | Assessment & Requirement |
|------|---------------------------|
| **1. Classification / Submission Route** | • Default assumption: **Class II** device (most diagnostic/clinical decision‑support AI tools).<br>• Apply 21 CFR 862.XXXXX (refer to FDA product code for the intended use) – if a legally marketed predicate exists, pursue a **Traditional 510(k)**.<br>• If no suitable predicate can be identified, prepare a **De Novo** request (21 CFR 860.10). |
| **2. Required Evidentiary Package** | • **Device Description & Intended Use** – clear statement of clinical indication, user environment, and patient population.<br>• **Predicate Comparison (if 510(k))** – side‑by‑side table of technological characteristics and intended use.<br>• **Software Verification & Validation (V&V)** per IEC 62304 and FDA’s “Software Precertification/AI/ML Guidance”. Include unit, integration, system testing, and cybersecurity assessment (21 CFR 820.70).<br>• **Clinical Performance Data** – retrospective validation on training/validation sets *and* prospective clinical study or real‑world evidence that meets the pre‑specified acceptance criteria.<br>• **Risk Management Dossier** – ISO 14971 risk analysis, identified hazards, mitigations, and residual risk justification.<br>• **Predetermined Change Control Plan (PCCP)** – fully populated per FDA AI/ML guidance (see Section 3.2 below).<br>• **Labeling & IFU** – instructions for use, contraindications, and description of post‑market monitoring plan. |
| **3. PCCP Elements Required (per source excerpt [2])** | 1. **Data Management** – procedures for data collection, cleaning, version control, and bias mitigation.<br>2. **Retraining Practices** – explicit trigger conditions, retraining workflow, and rollback strategy.<br>3. **Performance Evaluation** – predefined acceptance criteria, V&V methodology, statistical significance thresholds.<br>4. **Updated Procedures** – communication plan for users/clinicians, real‑world monitoring, IFU update process. |
| **4. Identified Evidence Gaps in Current Documentation** | • **Intended Use / Indication** – not present in source material; must be defined to determine classification and predicate.<br>• **Predicate Device Identifier** – no specific 510(k) number supplied; need search of FDA database.<br>• **Algorithm Architecture & Training Data Details** – missing description of model type, input features, dataset size, representativeness.<br>• **Clinical Validation Results** – quantitative performance metrics (sensitivity, specificity, ROC‑AUC, confidence intervals) not provided.<br>• **Risk Management File** – ISO 14971 analysis absent; hazards specific to AI (e.g., data drift) need documentation.<br>• **Post‑Market Surveillance Plan** – real‑world monitoring schedule and metrics not described. |
| **5. Core Risk Controls & Standards** | • **ISO 14971** – risk management lifecycle.<br>• **IEC 62304** – software life‑cycle processes (including configuration management for algorithm updates).<br>• **IEC 82304‑2** – health‑software safety requirements (optional but supportive).<br>• **FDA Guidance Documents**: <br> - “Artificial Intelligence/Machine Learning‑Based Software as a Medical Device Action Plan” (2021).<br> - “Predetermined Change Control Plan for AI/ML‑Based SaMD” (2024–2025) – cited in source [1].<br>• **21 CFR 820** – QMS requirements; note the new QMSR (effective Feb 2026) aligns with ISO 13485. |
| **6. Citations** | • FDA classification rule: 21 CFR 862 (class‑specific product code).<br>• 510(k) procedural regulation: 21 CFR 807.<br>• De Novo pathway: 21 CFR 860.10.<br>• Risk management standard: ISO 14971:2019.<br>• Software life‑cycle: IEC 62304:2006 (amended 2021).<br>• Predetermined Change Control Plan guidance – FDA website links listed in source [1] (no specific identifier found in source — verify separately).<br>• Modification protocol requirements – FDA AI/ML guidance excerpt [2] (no specific identifier found in source — verify separately). |
| **7. Human‑Escalation Triggers** | *Escalate to Senior Regulatory Manager / Lead RA* when any of the following are identified: <br>1. **Uncertain Classification** – insufficient information to justify Class I/II/III.<br>2. **No Predicate Identified** after exhaustive FDA 510(k) search.<br>3. **Insufficient Clinical Evidence** – performance data not meeting pre‑specified acceptance criteria or lacking prospective validation.<br>4. **Incomplete PCCP** – any of the four mandatory items missing or inadequately described.<br>5. **Risk Management Deficiencies** – hazards unaddressed, residual risk > acceptable level, or lack of ISO 14971 documentation.<br>6. **QMSR Non‑Compliance** – QMS processes not aligned with the new FDA Quality Management System Regulation (effective Feb 2026). |
| **8. Bottom‑Line Regulatory Judgment** | *Assuming a Class II indication and an existing predicate can be located, the fastest credible path is a Traditional 510(k) that incorporates a fully documented Predetermined Change Control Plan.* If no predicate exists or if the AI algorithm represents a novel mode of action, pursue a De Novo request with expanded clinical evidence. All evidence gaps listed above must be closed before filing to avoid FDA review delays. |

---

**Peer Review Prompt**

> @RA‑Colleague – please challenge the assumptions made regarding (a) inferred Class II classification without a stated indication, (b) completeness of the PCCP checklist based solely on the two source excerpts, and (c) any jurisdiction‑specific gaps that might affect submission under the new FDA QMSR effective February 2026.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 116/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 5,757자 | — |
| 규제 식별자 인용 | 9개 | — |
| source excerpt 근거 일치 | **0/9 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 9개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 862`, `21 CFR 860.10`, `21 CFR 820.70`, `IEC 82304`, `21 CFR 820`, `21 CFR 807`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "9ba6eb208136bc02", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

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

> **Regulatory Draft – X‑ray Imaging System (US Market)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|---------------|
| **FDA Product Code / Class** | *Class II* – Diagnostic X‑ray system is designated a Class II device under 21 CFR 862.1780 (X‑ray System). |
| **Submission Type** | Traditional **510(k) Premarket Notification** (substantial equivalence) is the standard route for Class II devices unless a De Novo request is warranted (not anticipated here). |
| **Regulatory Basis** | 21 CFR 862.1780; 21 CFR 820 (QMS); 21 CFR 803 (MDR reporting); 21 CFR 830 (software) if applicable; 21 CFR 11 (electronic records). |

> **Note:** No predicate device number or specific 510(k) identifier appears in the source material. *“no specific identifier found in source — verify separately”*.

---

### 2. Core Evidence Required for 510(k)

| Evidence Category | Required Content | Source‑based Gap |
|-------------------|------------------|-----------------|
| **Substantial‑Equivalence Comparison** | Side‑by‑side table of technology, intended use, performance, and labeling against a legally marketed predicate. | Predicate not provided in source – needs external confirmation. |
| **Device Description & Specification** | Detailed drawings, bill of materials, component specifications (including X‑ray tube, detector, software). | Not addressed in excerpt – must be supplied. |
| **Performance Testing** | • Electrical safety (IEC 60601‑1)  <br>• Radiation safety (dose measurements, IEC 60601‑2‑33)  <br>• Image quality metrics (MTF, NPS, DQE)  <br>• Software validation if applicable (21 CFR 830). | No testing data referenced – missing. |
| **Risk Management File** | ISO 14971 risk analysis, mitigations, residual risk evaluation, and linkage to design controls. | Not mentioned in source – must be compiled. |
| **Labeling & IFU** | Full labeling set (User’s Manual, Safety Information, UDI placement). | No labeling evidence cited – required. |
| **Quality System Documentation** | • FDA QMSR §820.35‑compliant *Record Management* SOPs <br>• ISO 13485:2016 §4.2.5 procedures (already recognized) <br>• Integration of additional FDA record‑keeping requirements (e.g., retention periods, audit trails). | Source indicates only ISO 13485 §4.2.5 is **insufficient**; specific QMSR‑extra elements are missing. |
| **Electronic Records Compliance** | 21 CFR Part 11 validation for any electronic record system used in manufacturing, QC, or post‑market surveillance. | Not covered – needs evidence. |
| **Post‑Market Surveillance (PMS) Plan** | Routine PSURs, MDR reporting processes (21 CFR 803). | No PMS documentation referenced. |

---

### 3. Identified Evidence Gaps & Required Actions  

| Gap | Why It Matters | Action Needed |
|-----|----------------|---------------|
| **FDA QMSR §820.35‑specific record controls** | FDA requires *additional* record‑keeping elements beyond ISO 13485 §4.2.5 (e.g., specific retention periods, traceability of design changes, MDR logs). | Develop SOPs and evidence that the system meets all §820.35 provisions; produce example records for review. |
| **Retention Period Documentation** | §820.35 mandates defined retention periods for design history files, device history records, etc. | Define retention schedule (e.g., 10 years post‑distribution) and provide policy documents. |
| **Electronic Record Validation (21 CFR Part 11)** | If records are stored electronically, validation is mandatory. | Conduct Part 11 validation protocol; supply test results and SARs. |
| **Software Lifecycle Documentation** (if software present) | 21 CFR 830 requires documentation of software development plan, hazard analysis, verification/validation. | Compile Software Development File (SDF) following IEC 62304 / FDA guidance. |
| **Risk Management Integration with Records** | ISO 14971 demands that risk controls be traceable to records; missing linkage can cause non‑compliance. | Map each risk control to specific QMSR record artifacts (e.g., FRACAS, CAPA). |
| **MDR & PSUR Processes** | 21 CFR 803/822 require timely reporting of adverse events and periodic safety updates. | Draft MDR SOPs, event log templates, and a PSUR schedule. |
| **Predicate Identification** | Substantial equivalence cannot be demonstrated without a cleared predicate device. | Perform market search; select appropriate predicate and capture its 510(k) number. |

---

### 4. Required Risk Controls (aligned with FDA QMSR & ISO 14971)

1. **Design Input Verification** – Ensure all intended uses, performance specs, and safety limits are captured in a *Design Input Record* compliant with §820.35.  
2. **Change Control** – Formal Change Request and Impact Analysis records retained for the device’s lifecycle.  
3. **Corrective & Preventive Action (CAPA)** – CAPA logs must include root‑cause analysis, implementation evidence, and effectiveness checks; stored per §820.35.  
4. **Software Validation / Verification** – If any embedded software is used for image acquisition or record handling, conduct unit, integration, and system validation with traceability to risk controls.  
5. **Data Backup & Recovery** – Document backup frequency, off‑site storage, and restoration testing to protect essential records (design history, device history).  
6. **UDI Implementation** – Assign a UDI per 21 CFR 830.30; maintain labeling and database records as required by the QMSR.  

---

### 5. Citations (Regulatory References)

| Citation | Basis |
|----------|-------|
| **21 CFR 820.35** – Record Management requirements | FDA QMSR regulation, mandatory extra to ISO 13485 §4.2.5. |
| **ISO 13485:2016 §4.2.5** – Documentation of records (basic requirement) | Incorporated by reference in QMSR; insufficient alone per source. |
| **21 CFR 862.1780** – Classification of X‑ray systems (Class II) | Determines 510(k) pathway. |
| **21 CFR 803** – Medical Device Reporting | Post‑market reporting obligations. |
| **21 CFR 830** – Software as a medical device | Applies if system includes software. |
| **21 CFR 11** – Electronic records & signatures | Required for electronic QMSR records. |
| **ISO 14971:2019** – Risk management for medical devices | Underpins risk control documentation. |

> No predicate/device 510(k) numbers or specific case identifiers appear in the source excerpts; *“no specific identifier found in source — verify separately”*.

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger Point | Escalation Target |
|-----------|---------------|-------------------|
| **Unresolved QMSR §820.35 gaps** (e.g., no retention schedule) | Identification of missing record‑control SOPs or evidence during pre‑submission review. | RA/QA Lead → Senior Regulatory Manager. |
| **Inadequate electronic records validation** | Failure to produce Part 11 SARs or test reports. | QA Validation Team Lead + Regulatory Lead. |
| **Missing predicate device** | Unable to cite a cleared 510(k) reference after market search. | Product Development Manager & Regulatory Lead (decision on De Novo vs 510(k)). |
| **Software lifecycle documentation absent** (if applicable) | No SDF/IEC 62304 evidence. | Software Engineering Lead + Regulatory Lead. |
| **Risk‑control traceability to records not demonstrable** | Gap in risk management file linking to QMSR records. | Risk Management Team → Regulatory Lead. |
| **Post‑market surveillance plan incomplete** | No MDR SOP or PSUR schedule ready. | Clinical/PMM Team → Regulatory Lead. |

When any of the above triggers are met, the responsible individual must **raise a formal issue in the project tracking system**, attach all current evidence, and request a **Regulatory Review Board (RRB) meeting** within 5 business days.

---

### 7. Peer Review Prompt  

> *"Please review this draft for completeness of QMSR‑specific record‑management requirements, appropriateness of the identified evidence gaps, and any jurisdiction‑specific nuances that may have been overlooked (e.g., state radiation licensing). Highlight assumptions that need validation or additional source coverage."*  

--- 

**End of Draft**

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 115/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,183자 | — |
| 규제 식별자 인용 | 12개 | — |
| source excerpt 근거 일치 | **5/12 (41%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 7개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 862.1780`, `21 CFR 11`, `21 CFR 830.30`, `21 CFR 820.35`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "b5d5f367b8986f30", "source": "github:holee9/MD-process/12_교차검증_보고서/2026-04-24_FDA_SBOM_제출물_사전점검.md", "source_hash": "ac0684e8e800838432db917f22348c24c3a819a9824cb391474182b6de2ad600"} -->

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

> **FDA Premarket Submission – Cybersecurity Evidence Requirements (SBOM & Management Plan)**  

---

### 1. Likely Classification / Submission Pathway  
| Device risk level (assumed) | FDA filing type | Reasoning |
|------------------------------|-----------------|-----------|
| Class II (moderate‑risk) or Class I with special controls | **510(k)** (traditional, special, or “abbreviated”) | Most medical devices that require a cybersecurity posture fall under 21 CFR §812.2; a 510(k) is the default pathway unless the device is novel (de Novo) or high‑risk (PMA). |
| Class III (high‑risk) | **PMA** or **De Novo** (if no predicate) | Same SBOM/cybersecurity expectations apply per FDA Guidance, but filing type changes. |

*No specific device identifier appears in the source; confirm actual classification before finalizing route.*

---

### 2. Required Evidence for Acceptance (per FDA policy effective 1 Oct 2025)

| Requirement | What must be supplied | Regulatory reference |
|-------------|----------------------|-----------------------|
| **Software Bill of Materials (SBOM)** – complete, machine‑readable list of all software components (including third‑party libraries) used in the device. | Full SBOM with version numbers, licenses, and provenance. | 21 CFR §812.2 (submission content); FDA Guidance “Content of Premarket Submissions for Management of Cybersecurity in Medical Devices” (Sept 2022). |
| **Cybersecurity Management Plan (CMP)** – documented processes covering the lifecycle. | • Post‑market vulnerability monitoring procedure.<br>• Patch development & deployment schedule.<br>• Coordinated Vulnerability Disclosure (CVD) policy.<br>• Security‑updates distribution mechanism.<br>• Risk assessment and mitigation strategy. | Same as above; QMSR 2026 (“ISO 13485‑aligned Quality Management System Regulation”). |
| **Risk Control Documentation** – mapping of identified threats to mitigations, referencing IEC 62443 or NIST SP 800‑53 controls. | Threat model, FMEA/FMECA with cybersecurity items, and documented controls. | FDA Guidance (2022) § “Cybersecurity Risk Assessment”. |

*If any element is absent, the FDA will issue a **Refuse to Accept (RTA)** notice under 21 CFR §812.3(b)(1).*

---

### 3. Gaps Identified in Source Excerpts  

| Item (source) | Current status (per table) | Missing / Incomplete evidence |
|---------------|----------------------------|--------------------------------|
| **Post‑market vulnerability monitoring** | Marked “○” (needs reinforcement). | Detailed SOP, responsible persons, frequency, and reporting timeline. |
| **Patch strategy & schedule** | Marked “◐” (partial). | Defined patch release cycle, criteria for urgent patches, validation procedures. |
| **Coordinated Vulnerability Disclosure (CVD) policy** | Marked “○” (policy not yet established). | Formal CVD policy document, contact points, public disclosure timeline. |
| **Security‑updates distribution mechanism** | Marked “◐”. | Secure delivery method (e.g., signed OTA updates), verification steps, rollback plan. |
| **SBOM** | Not mentioned in the excerpt. | Full SBOM must be compiled; absence triggers RTA. |

*No specific predicate device numbers or registration identifiers were found – verify separately.*

---

### 4. Recommended Risk Controls & Standards Alignment  

1. **Adopt IEC 62443‑3‑3 (System Security Requirements) / NIST SP 800‑53 Rev 5 controls** for:  
   - Access control, audit logging, secure configuration, and vulnerability management.  
2. **Implement a Secure Development Lifecycle (SDL)** referencing NIST CSF v1.1, with stage‑gate reviews that produce the SBOM at each build.  
3. **Document threat modeling per ISO 14971** (risk analysis) and map findings to the CMP.  

These controls satisfy both FDA guidance and the forthcoming QMSR requirements (effective Feb 2026).

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger | Escalation action |
|-----------|---------|-------------------|
| Any **required cybersecurity deliverable** (SBOM, CMP element) remains incomplete after internal pre‑submission review. | **Missing evidence flag** – > 1 working day before planned filing date. | Notify Regulatory Lead; elevate to Senior Management for resource allocation or schedule adjustment. |
| **RTA risk** identified (e.g., SBOM absent). | **Regulatory rejection risk** > 50 % per internal scoring matrix. | Immediate stop‑work, convene cross‑functional remediation team, and prepare a Request for Additional Information (RAI) response plan. |
| **CVD policy or vulnerability monitoring SOP** not finalized ≥ 30 days before filing. | **Timeline breach** of critical security deliverable. | Escalate to Chief Technology Officer and Legal for liability assessment; consider delaying submission. |
| New FDA guidance or QMSR amendments issued after internal review completion but before filing. | **Regulatory change alert**. | Regulatory affairs must re‑evaluate compliance; if gaps arise, reopen the pre‑submission checklist and inform all stakeholders. |

---

### 6. Summary Judgment  

- The project plans a pre‑market submission in 2026; FDA now *requires* an SBOM and a fully documented Cybersecurity Management Plan.  
- Current internal state shows partial or missing elements for post‑market monitoring, patch strategy, CVD policy, update distribution, and no SBOM evidence is referenced.  
- Without these, the filing will be **refused to accept (RTA)** per 21 CFR §812.3(b)(1).  

**Immediate actions:** compile a complete SBOM; finalize SOPs for vulnerability monitoring, patching, CVD, and update delivery; map controls to IEC 62443/NIST standards; re‑run the internal pre‑submission checklist.

---

### 7. Peer Review Request  

> *@RA‑Peer: Please challenge the assumptions above—particularly the inference that a 510(k) is appropriate without a known predicate, the completeness of the listed regulatory references, and any jurisdiction‑specific gaps (e.g., state‑level medical device cybersecurity statutes).*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 114/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,061자 | — |
| 규제 식별자 인용 | 5개 | — |
| source excerpt 근거 일치 | **0/5 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 5개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §812.2`, `IEC 62443`, `21 CFR §812.3`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "99858299f7dd0170", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

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

> **Regulatory Draft – AI‑Enabled Software Functions (PCCP Scope)**  

---

### 1. Device Synopsis (derived from source)
* **Product type** – Software‑Only, AI/ML‑enabled medical device (“AI‑Enabled DSF”).  
* **Intended use** – Perform data‐driven clinical decision support or diagnostic interpretation; incorporated in a Human‑AI workflow.  
* **Lifecycle management** – Subject to the FDA Pre‑Certification Collaborative Program (PCCP) which permits pre‑approved change ranges for AI updates, bias mitigation, and post‑market monitoring.

---

### 2. Likely Classification & Submission Route  

| Factor | Determination |
|--------|----------------|
| **CFR reference** | 21 CFR 862 – Device Classification (generic device type: “Software Used in Medical Devices” or “Clinical Decision Support Software”). |
| **Risk level** | Assuming the software provides *diagnostic* output that informs clinical management, it falls under **Class II** (moderate risk). |
| **Primary pathway** | **510(k) – Substantial equivalence** to an FDA‑cleared predicate SaMD with comparable intended use and algorithmic approach. |
| **Alternate if no predicate** | **De Novo classification** (request for Class II designation). |
| **PCCP impact** | If the device is already enrolled in PCCP, a **Special 510(k) – PCCP amendment** can be used for updates that stay within the pre‑approved change envelope. |

*No specific predicate number appears in the source; verify separately.*

---

### 3. Required Evidentiary Package (minimum for a standard 510(k))

| Evidence | Description |
|----------|-------------|
| **Device description** | Architecture, data flow diagram, hardware/software interface. |
| **Intended use & Indications for Use** | Precise clinical claim linking AI output to patient care. |
| **Algorithm design** | Model type, training data sources, versioning, hyper‑parameters. |
| **Data provenance & split** | Detailed description of train/validation/test datasets (size, demographics, labeling process). |
| **Performance validation** | Clinical performance metrics (sensitivity, specificity, AUC) with statistical confidence; linkage to clinical benefit. |
| **Bias analysis & mitigation plan** | Assessment across protected attributes (race, gender, age); documented mitigation strategies. |
| **Human‑AI workflow** | UI/UX description, role of clinician, decision override procedures. |
| **Risk Management File** | ISO 14971‑based FMEA/FMECA covering software hazards, cyber‑security, bias‑related risks. |
| **Software Validation** | IEC 62304‑compliant design verification & validation reports; test cases for updates. |
| **Post‑Market Surveillance (PMS) plan** | Ongoing performance monitoring, adverse event reporting, drift detection, schedule for periodic re‑validation. |
| **Update & Change Management** | Description of PCCP pre‑approved change range; procedures for out‑of‑scope modifications. |
| **QMS compliance** | Alignment with QMSR (effective Feb 2026), ISO 13485:2016 mappings, and 21 CFR 820. |

---

### 4. Gaps Identified from Source Excerpts  

| Gap | Why it matters | Recommended action |
|-----|----------------|--------------------|
| **Explicit bias analysis & mitigation** – mentioned only as “편향 분석·완화” without details. | FDA expects quantitative bias assessment and a documented mitigation plan for SaMD. | Provide dataset demographic breakdown, fairness metrics (e.g., equalized odds), and algorithmic adjustments. |
| **Post‑market monitoring (PMS) specifics** – listed as “시판 후 모니터링” but no concrete plan. | PCCP requires a defined PMS protocol to trigger updates within the pre‑approved envelope. | Draft a monitoring dashboard, define performance thresholds, and outline reporting timelines. |
| **Update plan tied to PCCP** – referenced (“업데이트 계획 시 PCCP”) without scope definition. | FDA will need to see which changes are covered under the PCCP change range vs. those requiring separate submissions. | Map each anticipated software change (e.g., model retraining, new data sources) to the PCCP envelope; flag out‑of‑scope items. |
| **Human‑AI workflow description** – noted but no detail on clinician decision authority. | Human factors risk analysis must show how clinicians interact with AI output and can override it. | Submit usability test results, task analyses, and error‑recovery procedures. |
| **Cybersecurity controls** – absent in excerpt although required for AI/ML SaMD. | FDA’s “Content of Premarket Submissions for Management of Cybersecurity” guidance applies. | Provide threat model, secure coding practices, vulnerability management plan. |

---

### 5. Core Risk Controls (to be reflected in the RMP & QMS)

1. **Algorithmic Transparency** – Version control, explainability reports per FDA’s “Good Machine Learning Practice (GMLP)” guidance.  
2. **Bias Mitigation** – Pre‑deployment fairness testing; continuous re‑assessment post‑deployment.  
3. **Cybersecurity** – Network isolation, encryption of input/output data, regular penetration testing.  
4. **Usability / Human Factors** – IEC 62366‑1 compliance; simulated clinical use studies.  
5. **Software Lifecycle** – IEC 62304 processes integrated with QMSR documentation (design controls, change control).  

---

### 6. Key Regulatory Citations  

| Reference | Relevance |
|-----------|-----------|
| **21 CFR 862** – Classification of medical devices | Determines Class II status for clinical decision support software. |
| **21 CFR 820** – Quality System Regulation (QSR) | Baseline QMS requirements; superseded/augmented by QMSR (2026). |
| **FDA “Software as a Medical Device (SaMD): Clinical Evaluation” Guidance (Nov 2021)** | Framework for clinical performance evidence. |
| **FDA “Proposed Regulatory Framework for Modifications to AI/ML‑Based SaMD” (April 2022)** | Sets expectations for change management, bias analysis, PMS. |
| **Good Machine Learning Practice (GMLP) Draft Guidance (Jan 2023)** | Recommended practices for data management, model development, and monitoring. |
| **QMSR – Quality Management System Regulation (effective Feb 2026), aligned with ISO 13485** | Mandatory quality system for all medical device manufacturers post‑Feb 2026. |

*No specific 510(k) predicate numbers or case IDs appear in the source; verify separately.*

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Performance drift** – validation metrics fall below pre‑defined thresholds (e.g., ≥5 % drop in sensitivity). | Issue a field corrective action; submit a PCCP amendment or new 510(k) if out of scope. |
| **Detected bias escalation** – disparity >10 % across protected groups emerges in real‑world use. | Initiate risk mitigation, update model, and notify FDA via a supplemental PCCP report. |
| **Cybersecurity breach** – unauthorized access to algorithm or patient data. | Execute incident response plan; submit a “Major Modification” report under 21 CFR 814.30(b). |
| **Adverse event trend** – ≥3 serious device‑related injuries linked to AI output within 6 months. | File a MedWatch 8220 report; consider voluntary recall if hazard cannot be mitigated quickly. |
| **Out‑of‑scope software change** – new algorithmic feature not covered by PCCP envelope. | Prepare and submit a conventional 510(k) or De Novo request before deployment. |

---

### 8. Peer Review Prompt  

> *Please review the assumptions made about classification, the completeness of the evidentiary checklist, and any jurisdiction‑specific gaps (e.g., state‑level AI regulations, CMS coverage considerations). Highlight missing citations or alternative pathways that may be more efficient for this AI‑Enabled DSF.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 113/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,736자 | — |
| 규제 식별자 인용 | 7개 | — |
| source excerpt 근거 일치 | **0/7 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 7개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 862`, `21 CFR 820`, `21 CFR 814.30`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "c4cae2cb43c85deb", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

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

> **Regulatory Draft – Gap Analysis for Clinical Evaluation (MDR 2017/745)**  

---

### 1. Preliminary Determination of Classification & Conformity‑Assessment Route  
| Item | Current status | Required action / evidence |
|------|----------------|----------------------------|
| **Device class** | *Not determinable from the supplied excerpts.* The MDR classification requires a full understanding of: <br>• Intended medical purpose (diagnostic, therapeutic, monitoring, etc.)  <br>• Duration of intended contact with the body  <br>• Whether the device is active, implantable or uses/measures energy. | Obtain the **Intended Use Statement** and a **device description** (including technical characteristics). Apply the appropriate **Classification Rule(s) (Annex VIII)** – e.g., Rule 9‑11 for active devices, Rule 22 for lay‑person use, etc. |
| **Conformity‑assessment route** | Undetermined pending classification.  | Once class is known: <br>• Class I → self‑declaration (Annex IV) and PMS report Art 85. <br>• Classes IIa/IIb/III → **Annex IX** (QMS + technical documentation assessment) *or* **Annex X** (type examination) *or* **Annex XI** (production conformity verification), depending on the Notified Body’s scope and the presence of a “significant change” to a previously certified device. |

---

### 2. Clinical Evaluation – Required Evidence (MDR)

| Evidence Element | MDR Requirement | Current Gap |
|------------------|-----------------|------------|
| **Clinical Evaluation Report (CER)** | Must be compiled in accordance with **Annex XIV Part A** and kept current under **Art. 61**.  Includes: <br>• State‑of‑the‑art literature review <br>• Clinical data from the device itself or from an equivalent device <br>• Benefit‑risk determination (incl. conclusions) | No CER draft, literature search, nor clinical data have been supplied. |
| **Equivalence justification** | Must meet the MDCG 2020‑5 criteria for equivalence *and* satisfy MDR‑added requirement that the **user type be identical** (e.g., HCP‑only vs. lay‑person).  The source excerpt explicitly notes: “동일한 사용자 유형 … MDR 추가”. | No comparator device has been identified, and user‑type alignment has not been verified. |
| **Clinical data from equivalent devices** | When equivalence is claimed, the **clinical performance data** (e.g., safety, efficacy) of the predicate must be comparable and **cover the same intended purpose, patient population, clinical condition, anatomical site and user type**. | No predicate device identified; therefore no clinical data package assembled. |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Required for all devices except those fully covered by robust pre‑market clinical data (Art 83‑84). PMCF details are set out in **Annex XIV Part B**. | No PMCF plan present; cannot determine if exemption applies. |
| **Risk Management File (RMF)** | Must be performed per **ISO 14971**, integrated with the CER, and demonstrate that residual risks are acceptable under **GSPR §16‑§20** (including radiation protection if applicable). | RMF not provided in supplied material; risk controls related to user type (e.g., training requirements for lay‑person devices) have not been demonstrated. |
| **Technical Documentation** | Must comply with **Annex II** (device description, labeling – Annex I §23, GSPR fulfilment, etc.). | Technical documentation absent; therefore cannot link clinical evidence to the device’s claimed performance. |

---

### 3. Specific Gap‑Analysis Findings

1. **Equivalence User‑Type Requirement Not Addressed**  
   *Citation*: The excerpt states “동일한 사용자 유형 … MDR 추가”, confirming that the MDR now requires identical user type for equivalence (MDR — no specific annex, but derived from GSPR §17 & §22).  

2. **Missing Clinical Evidence Sources**  
   - No literature review (state‑of‑the‑art) supplied.  
   - No clinical data set (clinical investigations or post‑market data) for the device under evaluation.  
   - No evidence that any claimed equivalent device satisfies all MDR equivalence criteria (same intended purpose, patient group, anatomical site, and **user type**).  

3. **Insufficient Documentation of Benefit–Risk Assessment**  
   The CER must include a benefit‑risk conclusion (**Art 61(4)‑(6)**) – absent here.

4. **Absence of PMCF Planning**  
   Without demonstrable pre‑market data, a **PMCF plan (Annex XIV Part B)** is mandatory; none has been provided.

5. **Risk Controls Linked to User Type Not Evidenced**  
   If the device is intended for lay users, additional safeguards (usability testing per **IEC 62366‑1**, training instructions per **GSPR §22**) are required – no such evidence is presented.

6. **Technical Documentation & Labeling Gaps**  
   No copy of labeling (Instructions for Use) to verify compliance with **Annex I §23** and the user‑type information requirements.

---

### 4. Recommended Evidence Package to Close Gaps

| Required Document | Content Summary | Source / Standard |
|-------------------|-----------------|--------------------|
| **Device Description & Intended Use** | Detailed description of device, indication(s), mode of action, target population, anatomical site, duration of use, and user type (HCP vs. lay). | MDR Art 2(1) & Annex VIII classification rules |
| **Classification Rationale** | Application of the relevant **Rule(s)** from **Annex VIII** with justification. | MDR Annex VIII |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | <ul><li>State‑of‑the‑art literature review (search strategy, inclusion/exclusion criteria).</li><li>Clinical data from the device or equivalent(s) – safety & performance outcomes.</li><li>Benefit–risk analysis (conclusions per Art 61(4)‑(6)).</li></ul> | MDR Art 61; **MDCG 2020‑5**, **MDCG 2020‑6**, **MDCG 2024‑3** |
| **Equivalence Justification Dossier** | <ul><li>Identification of predicate device (including EU Device ID, if any).</li><li>Side‑by‑side table confirming identical intended purpose, patient group, clinical condition, anatomical site, and user type.</li></ul> | **MDCG 2020‑5** – equivalence criteria |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | PMCF objectives, methodology, schedule, identified residual risks, PMS integration. | Annex XIV Part B; Art 84/86 |
| **Risk Management File (RMF)** | Risk analysis, evaluation, control measures, verification of controls, residual risk assessment linked to clinical data. | ISO 14971; GSPR §16‑§20 |
| **Usability Engineering file** (if lay user) | Use‑error analysis, validation testing per **IEC 62366‑1**, training instructions. | IEC 62366‑1 |
| **Labeling & IFU** | Full Instructions for Use including mandatory safety information, user type designation, contraindications. | Annex I §23 |
| **Technical Documentation (Annex II)** | Consolidated file containing all above elements plus design specifications, manufacturing processes, verification/validation results. | MDR Annex II |

---

### 5. Human‑Escalation Triggers  

| Trigger | When to Escalate to Senior RA / Regulatory Lead |
|--------|-------------------------------------------------|
| **No identified predicate device** or the predicate’s user type differs from the target device (e.g., HCP‑only vs. lay‑person). | Immediate escalation – equivalence cannot be claimed; need new clinical data. |
| **Clinical evidence insufficient to satisfy Art 61(4)‑(6)** (i.e., benefit–risk conclusion cannot be substantiated). | Escalate for decision on whether a full clinical investigation is mandatory. |
| **Unclear classification after applying all applicable Rules** (e.g., device contains active software, ambiguous energy source). | Escalate to senior RA for expert rule‑interpretation and possible consultation with the Notified Body. |
| **PMCF plan absent while pre‑market data are not robust** (i.e., no pivotal clinical trial or valid equivalence). | Escalate for approval of a PMCF protocol and allocation of resources. |
| **Risk controls linked to user type missing** (e.g., lack of usability testing for lay‑person devices). | Escalate to the safety engineer and senior RA for risk mitigation strategy. |
| **Technical Documentation non‑conformant with Annex II** (missing labeling, GSPR evidence). | Escalate for comprehensive documentation gap‑fill before the conformity‑assessment audit. |

---

### 6. Peer‑Review Prompt  

> **Colleague, could you challenge the assumptions made in this gap analysis?**  
> - Does the interpretation of the MDR-added “identical user type” requirement align with your understanding of GSPR §17/§22 and MDCG 2020‑5?   
> - Are there any additional sources (e.g., national competent authority guidance) that might affect equivalence justification for devices aimed at lay users?  
> - Have we captured all necessary evidence elements for a **Class IIa** device under **Annex IX**, or should we consider an alternative route (Annex X or XI)?  

---

*Prepared by:* Theo – EU MDR Regulatory Affairs Specialist  
*Date:* 2026‑07‑18

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 127/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,051자 | — |
| 규제 식별자 인용 | 15개 | — |
| source excerpt 근거 일치 | **3/15 (20%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 12개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Art 85` | MDR Article 85 | Post-market surveillance report (Class I) |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Art 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `Art 84` | MDR Article 84 | Post-market surveillance plan |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art 2`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "5feb7a42a490709b", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

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

> **Regulatory Gap‑Analysis Draft – Clinical Evaluation & PMCF (MDR 2017/745)**  

---

### 1. Device Classification & Conformity‑Assessment Route  
| Item | Requirement / Decision point | Current status | Gap |
|------|------------------------------|----------------|-----|
| **Intended purpose & mode of action** (e.g., “diagnostic imaging”, “active therapeutic”, “software as a medical device”) | Needed to apply the appropriate rule in Annex VIII (Rules 1‑22) and determine class (I, IIa, IIb, III). | *Not provided* – the source only lists generic placeholders such as “clinical application area”, “target population”, “user type” and “core performance”. | **Missing**: explicit statement of intended medical purpose, target indication, patient population, and user. |
| **Classification rule** (e.g., Rule 9, 10, 11, 17) | Must be cited by number from Annex VIII. | *Cannot be assigned* without the purpose description. | **Missing**: identification of the applicable classification rule. |
| **Resulting class** (I / IIa / IIb / III) | Determined from the rule in the previous step. | *Undetermined*. | **Missing**: final class assignment. |
| **Conformity‑assessment route** – Annex IX, X or XI | • Class I (non‑sterile, non‑measuring) → self‑declaration (Annex IV). <br>• Classes IIa/IIb/III → Notified Body involvement; choice of Annex IX (QMS + technical file), Annex X (type‑examination) or Annex XI (production conformity verification) depending on the device type. | *Cannot be selected* until class is known. | **Missing**: selection of the appropriate Annex route and identification of the Notified Body. |

> **Human‑escalation trigger #1:** If intended purpose, classification rule, or resulting class cannot be established within 2 weeks, raise to the Project Lead for clarification from the product team.

---

### 2. Clinical Evidence Requirements (MDR)  

| Requirement | Regulation / Standard | Current evidence | Gap |
|-------------|-----------------------|------------------|-----|
| **Clinical Evaluation Report (CER)** – comprehensive assessment of clinical data, benefit‑risk analysis, and justification of conformity. | Annex XIV Part A; kept current under Art. 61. | No CER drafted; only a placeholder table indicating “no scientific evidence + no clinical significance” appears in the source excerpt. | **Missing**: full CER (including literature review, clinical investigations, post‑market clinical follow‑up data). |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** – prospective plan describing objectives, methodology, and schedule. | Annex XIV Part B; Art. 84 (PMS plan) links to PMCF. | No PMCF plan supplied. | **Missing**: documented PMCF plan (including sample size, endpoints, data collection methods). |
| **PMCF Evaluation Report** – final evaluation of the executed PMCF activities. | Annex XIV Part B (Section 5.2 in source). | The source lists the required sections (A‑G) but no actual content is provided. | **Missing**: completion of Sections A–G with real data; see Table 1 below. |
| **PMS System & Reports** – continuous collection and analysis of post‑market data, PSUR for classes IIa‑III. | Art. 83 (system), Art. 84 (plan), Art. 86 (PSUR). | Not referenced in the excerpt. | **Missing**: PMS system description, periodic safety update report (if class IIa/IIb/III). |
| **Risk Management File (RMF)** – ISO 14971‑based file linking risk controls to clinical data and PMCF findings. | Annex I GSPR §15–§18; ISO 14971. | Not mentioned. | **Missing**: up‑to‑date RMF with residual risk evaluation, verification of risk control effectiveness via clinical evidence. |
| **Usability / Human Factors Evaluation** (if applicable). | IEC 62366‑1. | No reference. | **Potential gap** depending on device type (e.g., intended for lay users §22). |

> **Human‑escalation trigger #2:** If the CER, PMCF plan, or RMF are not supplied within 4 weeks, notify the Clinical Documentation Lead to initiate data collection strategies.

---

### 3. Required Content of the **PMCF Evaluation Report** (per source excerpt)

| Section | Description (as defined in source) | Evidence needed |
|---------|--------------------------------------|-----------------|
| **A – Manufacturer contact details** | Contact information for the entity responsible for PMCF. | Full name, address, email, phone of the responsible person. |
| **B – Device description** | Updated device description if any changes occurred; otherwise refer to the original PMCF plan. | Current version of the device’s intended use, specifications, and any modifications since the plan. |
| **C – Results of performed PMCF activities** | Presentation of collected data (both positive and negative), justification for any deviations from the planned protocol. | Raw data sets, statistical analysis, explanation of outliers or protocol amendments. |
| **D – Evaluation of clinical data from equivalent / similar devices** | Comparative assessment with data from other devices deemed equivalent or clinically similar. | Summary tables, justification of equivalence (e.g., same intended use, comparable performance). |
| **E – Impact on technical documentation** | Explicit statements on how PMCF results affect the CER, Risk Management File, and Summary of Safety‑and‑Performance Characteristics (SSPC). | Updated CER sections, revised risk control listings, modified SSPC tables. |
| **F – Applied consensus standards, harmonised standards and guidance** | List of standards/guidance used to analyse data (e.g., MDCG guidance, IEC standards). | Full citations (e.g., MDCG 2020‑5‑6‑7‑8, IEC 60601‑2‑54). |
| **G – Overall conclusion** | Assessment of whether PMCF objectives were met and any required corrective/preventive actions. | Decision matrix (met / partially met / not met) with agreed follow‑up activities. |

> **Human‑escalation trigger #3:** If any of the above sections remain incomplete after the scheduled PMCF closure date, flag to the Quality Manager for possible Notified Body inquiry.

---

### 4. Risk Controls & GSPR Alignment  

| GSPR Clause (Annex I) | Expected evidence / control | Current status |
|------------------------|----------------------------|----------------|
| **§16 – Protection against radiation** (if device emits ionising radiation). | Compliance with IEC 60601‑2‑54 or IEC 60601‑2‑44; dose limits, shielding verification. | Not addressed – no indication of radiation use. |
| **§17 – Electronic programmable systems / software** | IEC 62304 lifecycle documentation; security measures; software classification per Rule 11. | No software description supplied. |
| **§18 – Active devices & connections** | IEC 60601‑1 (general safety); verification of active components, battery safety. | Not mentioned. |
| **§20 – Mechanical / thermal risks** | Finite element analysis, burst testing, temperature limits. | No data provided. |
| **§22 – Devices intended for lay users** | Human factors evaluation per IEC 62366‑1; labelling per §23. | User type not defined. |

> **Human‑escalation trigger #4:** If the device falls under any of the above GSPR clauses and supporting evidence is absent, immediate escalation to the Risk Management Team is required.

---

### 5. Summary Judgment & Action Items  

| Decision / Finding | Required Next Step |
|--------------------|---------------------|
| **Classification cannot be determined** (missing intended purpose & mode of action). | Obtain a definitive Intended Use Statement from product development; map to Annex VIII rule(s). |
| **Technical documentation incomplete** (no CER, RMF, PMCF plan/report). | Draft and circulate CER outline; develop PMCF plan per MDCG 2020‑5‑6‑7‑8 guidance. |
| **PMCF evaluation report sections A–G are placeholders only**. | Populate each section with real data, standards citations, and impact statements. |
| **Potential gaps in GSPR compliance** (radiation, software, active device). | Conduct gap analysis against Annex I clauses; perform any missing testing or documentation. |
| **PMS system not evidenced** (Art. 83‑86). | Define PMS system architecture, assign responsibilities, schedule PSURs if class IIa/IIb/III. |

**Overall regulatory position:** *Insufficient clinical and post‑market evidence to support conformity under MDR at this stage.* The Notified Body would request a complete Clinical Evaluation Report, a validated PMCF plan & evaluation report, and an aligned Risk Management File before any CE marking can be issued.

---

### 6. Human‑Escalation Triggers (recap)

| Trigger | When to raise |
|--------|----------------|
| **1** – No intended use / classification rule defined within 2 weeks. | Immediate notification to Project Lead. |
| **2** – Missing CER, PMCF plan, or RMF after 4 weeks. | Alert Clinical Documentation Lead & Quality Manager. |
| **3** – Incomplete PMCF Evaluation Report sections (A‑G) post‑PMCF closure. | Notify Quality Manager for Notified Body follow‑up. |
| **4** – Absence of required GSPR evidence (radiation, software, active device). | Escalate to Risk Management Team and possibly to senior management. |

---

### 7. Peer‑Review Prompt  

*Colleague,* please challenge the assumptions made above:  

1. Are we correct in interpreting the MDCG 2020‑5‑6‑7‑8 guidance excerpt as mandating all seven sections (A–G) for **every** PMCF evaluation report, or are any of them optional depending on device class?  
2. Given that no explicit intended use is present, does the safest interim approach involve assigning the device to the most conservative classification (Class III) until further data are obtained?  
3. Have we captured all relevant MDR articles/Annexes for a Class IIa medical device with software components, or are additional citations (e.g., Art. 10‑13 on clinical investigations) required at this stage?  

Your feedback will help ensure the gap analysis is both complete and proportionate.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 126/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,934자 | — |
| 규제 식별자 인용 | 16개 | — |
| source excerpt 근거 일치 | **0/16 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 16개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art. 10`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "789ba6dc229a9fa9", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

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

> **Regulatory Draft – Clinical Evaluation Gap Analysis for a Diagnostic X‑ray Device (Standard Radiography)**  

---

### 1. Device Classification & Conformity‑Assessment Route  
| Element | Determination | Regulatory Basis |
|---|---|-|
| **Primary classification rule** | **Rule 10 (Active devices for diagnosis and monitoring – emitting ionising radiation)** → **Class IIb** | MDR Annex VIII, Rule 10 (active diagnostic X‑ray equipment) |
| **Secondary components** (detector & image‑processing software) | Detector: Rule 17 → Class IIa  <br>Software: Rule 11 → Class IIa (unless decision impact warrants higher class) | MDR Annex VIII, Rules 17 & 11 |
| **Overall system class** | The system is deemed **Class IIb** because the X‑ray source governs the risk profile. | MDR Annex VIII, Rule 10 interpretation |
| **Conformity‑assessment route** | **Annex IX** – Full quality‑management‑system audit + assessment of technical documentation (including clinical evaluation) by the Notified Body. | MDR Annex IX |

---

### 2. Evidence Required to Satisfy the NB (per Deficiency Letter)  

| Required Evidence | What Must Be Delivered | Regulatory Reference |
|---|---|---|
| **Clinical Evaluation Report (CER)** – updated, demonstrating clinical equivalence with a predicate device. | • Revised CER Rev. 3 (already attached as Annex A). <br>• Gap‑analysis narrative linking DQE ≥ 65 % to performance claim. | MDR Annex XIV Part A; kept current under Art. 61 |
| **Performance Test Report** – DQE measurement per IEC 62220‑1‑1. | • Original test report TR‑2024‑015 (referenced in source). <br>• Raw data and measurement protocol. | IEC 62220‑1‑1 (DQE) |
| **Risk Management File** (incl. updated risk controls for radiation exposure). | • ISO 14971 compliant file, with residual risk justification and ALARA implementation. | MDR Annex I §16, §18; ISO 14971 |
| **Usability Engineering / Human Factors Report** (if device intended for lay‑person or complex workflow). | • IEC 62366‑1 Usability evaluation report covering labeling & IFAU. | MDR Annex I §22; IEC 62366‑1 |
| **Software Lifecycle Documentation** (if software is a medical device component). | • IEC 62304 compliant development file, verification/validation evidence. | MDR Annex I §17 |
| **Electrical Safety / General Requirements** | • IEC 60601‑2‑54 compliance report (X‑ray equipment). | MDR Annex I §18; IEC 60601‑2‑54 |
| **Labeling & IFU** (in English and any EU language required) | • Updated label/IFU reflecting radiation warnings, contraindications, and safe use instructions. | MDR Annex I §23 |
| **Post‑Market Surveillance (PMS) Plan & Report** (class IIb) | • PMS plan per Art. 84; periodic safety update report (PSUR) per Art. 86. | Art. 84, Art. 86 |
| **Declaration of Conformity (DoC)** | • Signed DoC referencing all relevant standards and the NB’s certificate number. | MDR Annex IV |

---

### 3. Identified Gaps / Missing Information (per the Deficiency Letter)  

| Gap Category | Specific Missing Item | Impact if Unaddressed |
|---|---|---|
| **Clinical Evidence** | • No explicit justification of clinical equivalence beyond DQE ≥ 65 % (need comparative clinical outcome data, literature review, or PMCF results). | NB will consider the CER insufficient (Art. 61) → non‑conformity. |
| **Technical Documentation (TD)** | • Absence of complete IEC 60601‑2‑54 test report; incomplete traceability matrix linking risk controls to design outputs. | TD deemed incomplete – Annex II non‑conformity. |
| **Quality Management System (QMS)** | • Outstanding NCs from previous audit not closed; missing records for corrective actions. | QMS non‑conformities under Annex IX → possible suspension of certificate. |
| **Labeling** | • Radiation safety warnings not aligned with §16.4 of Annex I; user instructions lack “ALARA” guidance. | Non‑compliant labeling (Annex I §23). |
| **PMS/PMCF** | • No PMS plan submitted; no PMCF study protocol to support long‑term performance claims. | Failure to meet Art. 84–86 obligations. |

---

### 4. Risk Controls Required (to close the above gaps)  

1. **Radiation Protection – Annex I §16.4**  
   - Implement dose‑monitoring software with audible/visual alerts when exposure approaches predefined limits.  
   - Conduct a thorough risk‑benefit analysis quantifying residual risk after ALARA measures (ISO 14971).  

2. **Active Device Safety – Annex I §§18 & 19**  
   - Design interlocks to prevent accidental emission; redundant safety checks on power supply and tube current.  

3. **Software Validation – IEC 62304**  
   - Unit, integration, and system testing with traceability to risk control measures (e.g., error handling for dose calculation).  

4. **Usability Controls – IEC 62366‑1**  
   - Human factors validation with representative operators (radiographers) focusing on label comprehension and correct positioning of the detector.  

5. **Electrical Safety – IEC 60601‑2‑54**  
   - Verification of grounding, leakage currents, and electromagnetic compatibility per the standard.  

6. **Labeling Controls – Annex I §23**  
   - Include clear contraindications, exposure limits, and emergency stop instructions; perform a labeling verification test with end‑users.  

7. **Post‑Market Surveillance & PMCF**  
   - Establish a PMS plan (Art. 84) with periodic safety update reports (PSUR per Art. 86) that capture real‑world DQE performance, adverse events, and field corrective actions.

---

### 5. Citations (Established Regulatory References)

- **Classification Rule:** MDR Annex VIII, Rule 10 (active diagnostic X‑ray equipment) → Class IIb.  
- **Clinical Evaluation Requirement:** MDR Annex XIV Part A; Art. 61.  
- **Performance Standard for DQE:** IEC 62220‑1‑1.  
- **Risk Management:** ISO 14971; MDR Annex I §§16–18.  
- **Usability Engineering:** IEC 62366‑1.  
- **Software Lifecycle:** IEC 62304.  
- **Electrical Safety for X‑ray:** IEC 60601‑2‑54.  
- **Labeling Requirements:** MDR Annex I §23.  
- **PMS System & PSUR:** Art. 84 (PMS plan), Art. 86 (PSUR) – applicable to Class IIb devices.  
- **Deficiency‑Letter Process (EU NB):** MDR Annex VII + 2026/977; Structured Dialogue per Art. 7, 2026/977.  

*Case‑level identifiers present in source:*  
- Test Report **TR‑2024‑015** (DQE measurement).  
- Clinical Evaluation Report **Rev. 3** (attached as Annex A).  

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger | Action Required |
|---|---|---|
| **NB deadline missed** (clock‑stop expires without submission) | Immediate escalation to senior RA manager and legal counsel; prepare for possible non‑approval notification. |
| **Unresolved QMS NCs after corrective action** (≥ 2 weeks) | Escalate to Quality Assurance Director for root‑cause review and potential CAPA overhaul. |
| **Insufficient clinical equivalence evidence** (no additional clinical data within 30 days) | Prompt senior Clinical Evaluation Lead to commission supplemental PMCF or literature search. |
| **PMS plan not approved by NB** (feedback received) | Escalate to Post‑Market Surveillance Lead to redesign PSUR schedule; inform senior management of timeline impact. |
| **Labeling non‑conformance flagged** (radiation warnings missing) | Immediate involvement of Regulatory Affairs & Marketing to issue revised IFU; halt distribution until corrected labeling is in place. |

---

### 7. Summary Judgment  

- The device is classified as **Class IIb** under MDR Rule 10 and must follow the **Annex IX** conformity‑assessment route.  
- To close the NB’s Deficiency Letter, the manufacturer must submit: an updated CER with robust clinical equivalence justification (beyond DQE ≥ 65 %), full IEC 60601‑2‑54 safety test report, complete risk‑management file, QMS corrective‑action evidence, revised labeling, and a compliant PMS/PMCF plan.  
- Failure to address any of the identified gaps within the mutually agreed clock‑stop will trigger a formal escalation to senior RA leadership and may result in certificate suspension or non‑approval.

---

**Peer Review Prompt**

> *Colleague, please review this draft for: (1) completeness of the identified evidence gaps against the MDR requirements; (2) correctness of the classification reasoning and chosen conformity‑assessment route; (3) any overlooked jurisdiction‑specific obligations (e.g., EUDAMED registration, post‑market trend reporting under Art. 88); and (4) suitability of the escalation triggers for our internal risk‑management framework.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 125/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,512자 | — |
| 규제 식별자 인용 | 17개 | — |
| source excerpt 근거 일치 | **3/17 (17%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 14개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex II` | MDR Annex II | Technical documentation |
| `Art. 88` | MDR Article 88 | Trend reporting |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "1a0db0a88fb10ce0", "source": "github:holee9/ra-project/04_기술문서_템플릿/PSUR_템플릿_MDR_Article86.md", "source_hash": "6d65b5430b94bb35420a09d1eb40376cf69cae93da81ff32b60fc2f2377cbb13"} -->

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

> **Regulatory Draft – Clinical Evaluation Gap Analysis & Post‑Market Surveillance (PSUR) Requirements**  

*Prepared for internal review – EU MDR 2017/745*  

---

### 1. Device Identification (Information Required)
| Item | Current status | Comment |
|------|----------------|---------|
| Trade name / model | **missing** – “no specific identifier found in source — verify separately” | Needed to locate the applicable classification rule (Annex VIII) and to reference the device in EUDAMED. |
| Intended medical purpose (indication, target population, mode of action) | **missing** – “no specific identifier found in source — verify separately” | Determines classification (Rule 9‑11‑17 etc.) and informs clinical evaluation scope. |
| Core device description (materials, technology, active vs. passive) | **missing** – “no specific identifier found in source — verify separately” | Required for risk management and to select applicable GSPR (§16‑22). |

*Human‑escalation trigger*: **If any of the above items remain undefined, halt PSUR preparation and classification work until clarified.**

---

### 2. Classification & Conformity‑Assessment Route (pre‑submission)

| Step | Requirement | Current evidence | Gap / Action |
|------|-------------|------------------|--------------|
| Identify applicable rule (Annex VIII) – e.g., Rule 9, 10, 11, 17 etc. | Device purpose & technology must be mapped to a rule. | **missing** – no intended use or device type provided. | Conduct classification workshop; obtain manufacturer’s “Intended Use” statement. |
| Assign risk class (I, IIa, IIb, III) based on the rule. | Dependent on step‑above. | **missing** | Same as above. |
| Choose conformity‑assessment route (Annex IX, X or XI). | Determined by class and whether a Notified Body is required for technical‑documentation review. | **missing** – classification unknown. | Once class is known: <ul><li>Class I → self‑declaration (Annex IV).</li><li>Class IIa/IIb/III → Annex IX (QMS + TB assessment) or Annex X (type‑examination) as appropriate.</li></ul> |

*Human‑escalation trigger*: **Classification unknown → cannot select annex route. Escalate to product owner for intended‑use clarification.**

---

### 3. Clinical Evidence Required (MDR Art.61, Annex XIV)

| Requirement | Reference | Current provision (source) | Gap |
|-------------|-----------|----------------------------|-----|
| **Clinical Evaluation Report (CER)** – up‑to‑date, covering benefit–risk determination. | Annex XIV Part A; kept current under Art. 61. | Not present in excerpt. | Draft CER based on device type, literature review (SOTA), and clinical data. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** – documented, with objectives, methodology, timelines. | Annex XIV Part B; referenced in PSUR Section 7 (Art.86(1)(d)). | Table asks for “PMCF 계획 참조 문서” (reference document) but value missing. | Obtain signed PMCF plan document number & version. |
| **PMCF Interim/Final Report** – results linked to CER updates. | Art. 86(1)(d). | Section 7 provides placeholders (“이번 기간 주요 PMCF 결과”, “PMCF 결과의 CER 반영”) but no data. | Populate with actual interim findings, assess impact on benefit–risk, update CER accordingly. |
| **State‑of‑the‑Art (SOTA) literature review** – to support clinical performance claims. | Annex XIV Part A, §4.2. | Not addressed in source. | Conduct systematic literature search; document methodology. |

*Human‑escalation trigger*: **If PMCF results are not integrated into the CER within 30 days of data availability, flag to Clinical Affairs lead.**

---

### 4. PSUR Content (MDR Art.86) – Current State vs. Required Elements  

| Art.86(1) Sub‑clause | Requirement | Source excerpt | Present? | Gap / Action |
|----------------------|-------------|---------------|----------|--------------|
| **(a) Conclusions of benefit–risk determination** | Summary of overall safety & performance, including clinical data. | Not in excerpts. | ❌ | Add to PSUR narrative; reference updated CER. |
| **(b) Main findings of PMCF** | Summarise outcomes, trends, corrective actions. | Section 7 (PMCF 결과 연계) outlines required table but contains placeholders only. | ⚠️ (structure present, data missing) | Fill with real results; indicate if any safety signals detected. |
| **(c) Sales volume & patient exposure** | Quantitative market data per region; methodology if estimates used. | Section 2 provides a template for EU/Korea/USA/Other sales & exposure, and cites MDCG 2022‑21 §5.3. | ⚠️ (template present, figures missing). | Insert actual numbers; if estimations are required, document assumptions per MDCG 2022‑21 §5.3. |
| **(d) Summary of any field safety corrective actions (FSCAs)** | Description, justification, and impact on risk. | Not shown in excerpts. | ❌ | Gather from vigilance system; include in PSUR. |
| **(e) Update of the technical documentation** | Reference to any changes in design, labeling, or instructions for use. | Not shown. | ❌ | Verify if any post‑market modifications occurred; update Annex II accordingly. |

*Human‑escalation trigger*: **If sales/exposure data cannot be substantiated with documented methodology (per MDCG 2022‑21 §5.3), PSUR must be held until compliant estimation is produced.**

---

### 5. Risk Management & Controls (ISO 14971, Annex I GSPR)

| Control | Reference | Current evidence | Gap |
|---------|-----------|------------------|-----|
| **Risk management file** – risk analysis, evaluation, control measures, residual risk acceptance criteria. | ISO 14971; Annex I §16‑22 (risk‑related GSPR). | Not referenced in source excerpts. | Obtain latest RMF; ensure linkage to PMCF findings. |
| **Protective measures for radiation (if applicable)** | Annex I §16.4 (protection against ionising radiation). | Unknown – device type not defined. | Verify if the device emits or records ionising radiation; apply relevant standards (e.g., IEC 60601‑2‑54, IEC 60601‑2‑28). |
| **Usability and Human Factors** | IEC 62366‑1; Annex I §23 (information supplied). | Not addressed. | Conduct usability validation if device intended for lay users (§22). |
| **Software safety (if software is a component/device)** | IEC 62304; Annex I §17. | Unknown. | Confirm software classification (Rule 11) and apply appropriate lifecycle processes. |

*Human‑escalation trigger*: **Any unmitigated residual risk > accepted level must be escalated to the Risk Management Committee before PSUR finalisation.**

---

### 6. Documentation Summary & Next Steps  

| Action | Owner | Deadline |
|--------|-------|----------|
| Provide complete device description, intended use, and classification rationale. | Product Development / Marketing | **T+5 days** |
| Supply signed PMCF plan (document number & version). | Clinical Affairs | **T+7 days** |
| Populate PSUR Section 2 with validated sales‑volume & patient‑exposure data; include methodology per MDCG 2022‑21 §5.3. | Market Access / Business Intelligence | **T+10 days** |
| Deliver interim PMCF results and update CER accordingly. | Clinical Affairs | **T+15 days** |
| Compile risk‑management file updates reflecting post‑market data. | Quality Management | **T+12 days** |
| Draft full PSUR (including sections a‑e) for Notified Body review. | Regulatory Affairs Lead | **T+20 days** |

*If any of the above items remain incomplete after the listed deadline, the PSUR cannot be submitted and a formal escalation to senior management is required.*

---

### 7. Peer Review Prompt  

> **Colleague’s task:**  
> - Challenge the assumptions made about classification pathways given the absent device information.  
> - Verify whether the PSUR template sections captured from the source fully satisfy Art. 86(1) for a Class IIa device (or indicate any additional mandatory elements).  
> - Confirm that all cited MDCG guidance (2022‑21 §5.3) and MDR articles are correctly applied, and note any jurisdiction‑specific gaps (e.g., UK MHRA post‑market reporting differences).  

---

*End of Draft.*

**Citation Lint (C1 — 구조적 인용 오류 자동 감지)**

- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art.86(1)(d)`)
- ⚠️ Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c). (`Art. 86(1)(d)`)

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 124/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,247자 | — |
| 규제 식별자 인용 | 13개 | — |
| source excerpt 근거 일치 | **1/13 (7%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 12개 | `No hallucination` |
| C1 린터 구조 오류 | 6건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

⚠️ **C1 구조 오류** (존재할 수 없는 하위 식별자 — Score 1 후보):
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).
- Art.86(1)(d) does not exist — Art.86(1) has only (a)/(b)/(c).

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Art.61` | MDR Article 61 | Clinical evaluation |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Annex II` | MDR Annex II | Technical documentation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "494153e2c89c488c", "source": "github:holee9/ra-project/04_기술문서_템플릿/PMS_Plan_MDR_Article84_템플릿.md", "source_hash": "703b0644c3d1ec9bab0c119bfa42a2dad76e804132491e7991800c9d14432fee"} -->

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

> **Regulatory Draft – Clinical Evaluation / Post‑Market Surveillance / Classification & Conformity Assessment (MDR 2017/745)**  

---

### 1. Device Portfolio & Proposed MDR Classification  

| Product | Primary Intended Use (as inferred) | Applicable MDR Classification Rule* | Resulting Class | Required NB Route |
|---------|------------------------------------|--------------------------------------|-----------------|-------------------|
| **X‑ray Detector** | Captures diagnostic X‑ray images generated by an external source. | Rule 17 (devices intended for recording diagnostic images produced by ionising radiation) | IIa | Annex IX (full quality‑management system + technical documentation assessment). |
| **Handheld X‑ray Source** | Generates ionising radiation for on‑site diagnostic radiography. | Rule 10 (active devices that emit ionising radiation for diagnostic purposes) | IIb | Annex IX. |
| **Imaging GUI Software (SaMD)** | Provides image‑display, manipulation and decision‑support information for X‑ray examinations. | Rule 11 (software providing information used in diagnosis/therapy) – cited MDR §22 for classification of “software intended to assist diagnosis” → Class IIa. | IIa | Annex IX. |

\*Rule citations are taken from the MDR classification matrix (Annex VIII).  

**Reference:**  
- Rule 17 → Class IIa (active recording device) – MDR Annex VIII, Rule 17.  
- Rule 10 (radiology limb) → Class IIb – MDR Annex VIII, Rule 10.  
- Rule 11 & §22 (software) → Class IIa – MDR Annex VIII, Rule 11 & §22.

---

### 2. Required Evidence for each device  

| Evidence Item | Where required in the Technical Documentation (Annex II) | Comments / Current Status |
|---------------|----------------------------------------------------------|---------------------------|
| **General Safety & Performance Requirements (GSPR)** – §§1‑23, especially §§16 (radiation protection), §17 (software), §18 (active devices) | Annex II, Chapter I/II. | Need explicit mapping of device features to each GSPR. |
| **Risk Management File** (ISO 14971) | Annex II, Chapter II. | Must include risk control measures for radiation exposure, software error, cybersecurity and data loss (see Section 1‑PMS items). |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A, kept current under Art 61 | Required for all three devices. | Only high‑level PMS signals are listed; no clinical data sources identified yet. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – Annex XIV Part B | Needed especially for SaMD (software usability & diagnostic error). | PMCF method “usability assessment (IEC 62366)” noted, but missing detailed protocol and KPI definitions. |
| **Post‑Market Surveillance (PMS) Plan** – Art 84 | Must describe data sources (bug reports, CVE/NVD, user error logs) and monitoring of standards updates (IEC 62304, MDCG 2019‑16 Rev.1, MDCG 2021‑6). | Plan outlined in excerpt but missing schedule, responsibilities, linkage to PSUR/PSUR content. |
| **Periodical Safety Update Report (PSUR)** – Art 86 | Class IIa: every 2 years; Class IIb: annually. | Matrix shows “PSUR 2 yr/annual” as mandatory, but no draft PSUR or data pool is referenced. |
| **Labeling & IFU** – Annex I §23 | Must contain warnings on radiation safety, cybersecurity, software version control. | No labeling extracts provided. |
| **Usability Engineering File** – IEC 62366‑1 | Supports PMS and risk analysis for GUI software. | Only “사용성 평가 (IEC 62366)” mentioned; full usability engineering documentation not yet produced. |
| **Cybersecurity Documentation** – MDCG 2019‑16 Rev.1 & 2021‑6, NIST CVE/NVD feeds | Required to satisfy §17 (software) and §18 (active devices). | Risk signals listed (“SW 오류… 사이버보안 취약점”), but mitigation strategy not detailed. |
| **Regulatory Confirmation for MFDS applicability** – Korean Digital Medical Device Law (2024‑09‑26) | Not an EU requirement, but needed for parallel market launch and to verify any additional local obligations that could affect the EU technical file. | Flagged as “검증 필요”. |

---

### 3. Identified Gaps / Missing Information  

| Gap | Why it matters | Impact if not addressed |
|-----|----------------|--------------------------|
| **Explicit Intended Use Statements** (including clinical indication, patient population, mode of use) | Required for classification verification and to define the scope of the CER & PMCF. | Classification uncertainty; possible re‑classification or need for additional conformity route. |
| **Clinical Data Sources & Literature Review** (state‑of‑the‑art, device‑specific studies) | Core of Annex XIV Part A CER. | Incomplete CER → NB may request supplemental clinical evidence, delaying conformity assessment. |
| **Detailed PMCF Protocol** (sample size, endpoints, data collection timeline) | Needed to meet Art 84 & Annex XIV Part B. | PSUR will lack robust benefit‑risk conclusions; NB may reject the PMS plan. |
| **Full Risk Management File** (including residual risk evaluation for radiation dose, software malfunction, cybersecurity breach) | Links risk controls to GSPR §16, §17, §18. | Non‑compliance with Art 10 & Annex I → NB audit comments. |
| **Usability Engineering Validation Results** (task analysis, formative/ summative testing outcomes) | Supports IEC 62366 compliance and mitigates diagnostic error risk. | Unaddressed usability risks may be deemed unacceptable for SaMD. |
| **Cybersecurity Controls Documentation** (threat modeling, patch management, incident response) | Required by MDCG 2019‑16 Rev.1 & 2021‑6, reflected in §17/§18. | Potential non‑conformity with “essential safety requirements” for software. |
| **Labeling Draft (IFU, symbols, CE mark statement)** | Needed for Annex I §23 and to communicate radiation precautions. | Incomplete technical file; NB may request labeling before final conformity assessment. |
| **Verification of MFDS applicability** (whether Korean law adds any mandatory post‑market obligations that overlap with EU PMS) | Could affect data collection scope, especially if harmonised requirements differ. | Missing verification could lead to regulatory gaps in a dual‑market strategy. |

---

### 4. Risk Controls – Mapping to Identified Risks  

| Identified Risk (from PMS excerpt) | Corresponding Control (ISO 14971 / IEC standards) | GSPR reference |
|-----------------------------------|--------------------------------------------------|----------------|
| Software error causing diagnostic misinterpretation | • Rigorous unit & integration testing (IEC 62304).<br>• Formal verification & validation per IEC 62304 Rev.2.<br>• Deployment of a post‑release monitoring module to capture runtime errors. | §17, §18 |
| Data loss / integrity breach | • Redundant data storage with checksum verification.<br>• Secure backup procedures and encrypted transmission (MDCG 2021‑6). | §17 |
| Cybersecurity vulnerability (CVE/NVD) | • Threat modeling & regular penetration testing.<br>• Patch management linked to CVE feed (NIST NVD).<br>• Secure boot & authentication mechanisms. | §17, §18 |
| Radiation overexposure (Handheld source) | • Built‑in dose‐limiting firmware.<br>• Real‑time dosimetry with automatic shut‑off.<br>• User training & procedural safeguards. | §16.4 |
| Diagnostic error due to GUI misuse | • IEC 62366 usability testing (task analysis, error‑recognition).<br>• Clear on‑screen warnings and context‑sensitive help.<br>• Human factors validation report. | §22, §23 |

---

### 5. Conformity Assessment Route  

All three devices fall into **Class IIa** or **Class IIb** → mandatory involvement of a Notified Body (NB). The appropriate MDR route is:

- **Annex IX** – Full quality‑management system assessment combined with technical documentation review.  
  *Rationale*: Class IIa/IIb require NB audit of the QMS (ISO 13485 compliant) and verification that the technical file satisfies Annex II, Annex XIV (CER & PMCF), Art 83–86 (PMS/PSUR). No alternative “self‑certification” route exists for these classes.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required | Who escalates |
|---------|------------------|---------------|
| **Unresolved classification** (e.g., ambiguous intended use leading to possible Rule 11 vs. Rule 10) | Convene a cross‑functional review with clinical, regulatory & engineering leads; seek NB advice before dossier submission. | Regulatory Lead (Theo). |
| **Missing clinical evidence for CER** | Initiate targeted clinical study or literature search; document gap mitigation plan. | Clinical Evaluation Team. |
> **Escalation:** If no feasible data source can be identified within 4 weeks, inform senior management to consider redesign or scope reduction.

| Insufficient PMCF protocol (no defined KPIs, sample size) | Draft detailed PMCF plan, obtain stakeholder sign‑off; submit to NB for review. | Project Manager / RA Lead. |
> **Escalation:** If NB flags the PMCF as inadequate during pre‑audit, pause submission and re‑work plan.

| Cybersecurity mitigation not documented or outdated (MDCG guidance version mismatch) | Update security dossier, map CVE handling process; perform external penetration test. | IT Security Lead (escalate to Chief Technology Officer). |
> **Escalation:** Any identified critical vulnerability must be reported per Art 87 within 24 h and trigger a field‑safety corrective action.

| MFDS applicability verification pending | Conduct legal analysis, obtain local regulatory counsel confirmation; update technical file. | Regulatory Affairs – International. |
> **Escalation:** If Korean law imposes extra post‑market obligations that conflict with EU PMS scope, raise to Product Strategy Board.

---

### 7. Regulatory Judgment (Summary)  

- **Classification**: X‑ray Detector → Class IIa (Rule 17); Handheld X‑ray Source → Class IIb (Rule 10); Imaging GUI Software → Class IIa (Rule 11, §22).  
- **Conformity Assessment**: All three require the **Annex IX** route (full QMS + TA audit).  
- **Evidence Required**: Complete CER (Annex XIV‑A), PMCF Plan & Report (Annex XIV‑B), PMS Plan (Art 84) leading to PSURs (Art 86), full risk management, usability & cybersecurity documentation, labeling/IFU.  
- **Current Gaps**: Intended use definition, clinical data sources, detailed PMCF protocol, comprehensive risk management file, finalized usability and cybersecurity mitigation records, draft labeling, MFDS applicability verification.  

**Immediate next steps:** Populate the identified gaps, produce the missing deliverables, and schedule an internal NB‑readiness review. Escalation points are flagged above; any trigger that materialises must be raised to senior management before proceeding to the Notified Body audit.

---

### 8. Peer Review Prompt  

> *Colleague, please challenge the following:*  
> 1. Are the applied MDR classification rules (Rule 17, Rule 10, Rule 11/§22) correctly matched to the described device functions?  
> 2. Does the source excerpt provide sufficient coverage of PMS data streams to satisfy Art 84‑86, or are additional sources needed?  
> 3. Are there any jurisdiction‑specific (e.g., Korean MFDS) obligations that could affect the EU technical file not yet captured?  
> 4. Identify any other potential evidence gaps (clinical, risk, labeling) that may delay the Annex IX assessment.

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 123/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 11,351자 | — |
| 규제 식별자 인용 | 15개 | — |
| source excerpt 근거 일치 | **2/15 (13%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 13개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex II` | MDR Annex II | Technical documentation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art 61` | MDR Article 61 | Clinical evaluation |
| `Art 84` | MDR Article 84 | Post-market surveillance plan |
| `Art 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `Art 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art 87` | MDR Article 87 | Reporting of serious incidents and field safety corrective actions |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art 10`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "0b49ee1afb6a7904", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "1f7581a31c4c152b66cf0460934ef96ec9205ef647cccf95efb57981151002ff"} -->

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

> **Regulatory Draft – KGMP Evidence Readiness Assessment**

---

### 1. Device Classification & Submission Route (Korean MFDS)

| Item | Determination | Rationale / Citation |
|------|---------------|----------------------|
| **Risk class** | *Not determinable from available source excerpts* | No device description, intended use, or risk‑based criteria are provided. MFDS classification (Class I, II, III, or IV) must be derived from the “Medical Device Act” and its Annex A tables. |
| **Submission pathway** | *Pending classification* → **허가(Approval)** for Class II–IV; **신고(Notification)** for Class I devices without special controls. | MFDS requires a 허가 신청 for devices classified as Class II, III or IV (or Class I with special control). Without a clear class, the appropriate route cannot be finalized. |

> **Human‑escalation trigger #1** – *If classification cannot be resolved within 5 business days of this draft, request detailed device specification (intended use, patient population, modality, etc.) from product development.*

---

### 2. Core Evidence Required for MFDS 허가 (or 신고)

| Evidence Category | Korean Requirement | Mapping to International Standards / Foreign Evidence Accepted |
|-------------------|--------------------|---------------------------------------------------------------|
| **KGMP Facility Certification** | Certificate of compliance with KGMP (Korean Good Manufacturing Practice) – includes QMS audit report. | Aligns with ISO 13485:2016; MFDS now accepts *MDSAP* inspection reports as a substitute for on‑site KGMP audits per MDR Annex IX §3.2【1037950769042691196】. |
| **Quality Management System (QMS) Documentation** | Full QMS manual covering clauses 7–8 of the KGMP regulation; evidence that each ISO‑equivalent clause is satisfied. | Directly comparable to ISO 13485:2016. The source shows a one‑to‑one mapping for purchase control, production/service, equipment management, measurement/analysis, feedback, internal audit (including FDA inspection scope), process monitoring, nonconformity management, data analysis and continual improvement【1012828200772392062】. |
| **Non‑clinical / Bench Testing** | OECD‑aligned biocompatibility & safety studies; test reports meeting MFDS’s “규제기준”. | Foreign non‑clinical data accepted when aligned with OECD GLP or ISO 10993 series (MFDS notice on foreign evidence – verify latest notice number). |
| **Clinical Evaluation / Local Clinical Data** | If the device is a Class IIa–IV, an MFDS‑approved clinical evaluation report (Korean language) is required unless a CE mark with sufficient post‑market surveillance data can be leveraged under the “foreign clinical evaluation” pathway. | MFDS has expanded acceptance of foreign CE clinical evaluation reports (see recent MFDS notice on foreign clinical evidence; exact notice number to be retrieved). |
| **Labeling & IFU** | Korean language labeling, packaging, and Instructions for Use complying with MFDS Annex III. | No foreign exception – all labeling must be provided in Korean even if a CE mark is present. |
| **Post‑Market Surveillance (PMS) Plan** | PMS plan referencing PSUR/PMSR data; mandatory collection of PMS data as per MDR Art. 83‑86 (mirrored in MFDS regulations). The source notes “PSUR/PMSR 연동” for measurement & analysis and data analysis sections【1012828200772392062】. |
| **Device Master File / Technical Documentation** | Complete technical file (design dossier) including risk management file per ISO 14971. | Foreign equivalents accepted when fully translated into Korean. |

> **Human‑escalation trigger #2** – *If KGMP certification is not yet secured or MDSAP report unavailable, initiate a parallel on‑site audit request with MFDS.*

---

### 3. Gaps / Missing Information (Based Solely on Source Excerpts)

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **Device classification** – No risk class or intended use disclosed. | Cannot select 허가 vs 신고, nor determine required clinical evidence. | Obtain device description, indication, and applicable MFDS Annex A criteria from the development team. |
| **KGMP certification status** – Not mentioned whether a KGMP certificate exists or if an MDSAP report will be used. | Required for 허가; missing would stall acceptance of QMS evidence. | Confirm KGMP audit outcome or acquire an up‑to‑date MDSAP inspection report. |
| **Local clinical data requirement** – No indication whether the device is exempt from Korean clinical trials through CE/foreign clearance. | May necessitate a Korean clinical trial, extending timelines. | Review MFDS “Foreign Clinical Evaluation” notice to assess eligibility; request any existing EU clinical evaluation report. |
| **Korean language labeling & IFU** – Not addressed in excerpt. | Mandatory for market entry; omission leads to non‑conformity findings. | Prepare Korean translations and verify against MFDS labeling guidance (e.g., MFDS Notice No. 2020‑xx). |
| **Risk management file** – No reference in source material. | Risk analysis required under both ISO 14971 and MFDS regulations. | Compile a risk management dossier aligned with the device’s hazard profile. |

> **Human‑escalation trigger #3** – *If any of the above gaps remain unresolved after the next review cycle (7 days), flag to senior RA lead for escalation to regulatory affairs manager.*

---

### 4. Key Risk Controls Evidenced by the Source Mapping

| KGMP Clause | Corresponding ISO 13485 / FDA QSR Reference | Control Objective |
|-------------|--------------------------------------------|-------------------|
| **7.4 구매 (Purchasing)** | ISO 13485 §7.4; FDA §820.50 – Purchasing Controls | Ensure purchased items meet specified requirements; traceability. |
| **7.5 생산 및 서비스** | ISO 13485 §7.5; FDA §820.30 – Production/Process Controls | Maintain controlled manufacturing environment and service delivery. |
| **7.6 측정장비 관리** | ISO 13485 §7.6; FDA §820.72 – Calibration & Maintenance | Guarantee accuracy of measuring equipment used for product verification. |
| **8.1 측정·분석·개선 (Measurement, Analysis and Improvement)** | ISO 13485 §8.2; FDA §820.100 – Data Analysis | Use data to drive continual improvement; link to PSUR/PMSR. |
| **8.2.1 피드백** | ISO 13485 §8.2.1; FDA §820.20 – Complaint Handling (recording completion) | Capture and resolve complaints promptly, satisfying MDR Art. 83‑86. |
| **8.2.2 내부 감사** | ISO 13485 §8.2.2; FDA §820.180(c) – Internal Audits (now without exemption for NB audits) | Conduct regular internal QMS audits, including potential unannounced inspections. |
| **8.2.3 공정 모니터링** | ISO 13485 §8.2.3; FDA §820.100 – Process Monitoring | Real‑time monitoring of critical processes to detect deviations. |
| **8.3 부적합 관리** | ISO 13485 §8.3; FDA §820.90 – Nonconforming Product Control | Identify, isolate, and disposition non‑conforming items. |
| **8.4 데이터 분석** | ISO 13485 §8.2.4; FDA §820.100 (Data Analysis) | Generate evidence for PSUR/PMSR submissions. |
| **8.5 개선** | ISO 13485 §8.5; FDA §820.100 – Corrective & Preventive Actions | Implement CAPA based on analysis outcomes. |

These controls demonstrate a robust QMS foundation that can satisfy MFDS KGMP expectations when accompanied by the required documentation and Korean‑specific artifacts.

---

### 5. Citations (Established References)

| Citation | Type |
|----------|------|
| **§820.35 – Service Records** (FDA QSR) | Established regulatory reference |
| **§820.20 – Complaint Handling Completion Record** (FDA QSR) | Established regulatory reference |
| **MDR Annex IX §3.2 – Partial Acceptance of MDSAP** (EU Medical Device Regulation) | Established regulatory reference |
| **MDR Art. 83‑86 – PMS Data Collection Obligations** | Established regulatory reference |

*No case‑level identifiers (e.g., 510(k) numbers, predicate device IDs) appear in the source excerpts; therefore none are listed.*

---

### 6. Human‑Escalation Triggers Summary

| Trigger | Condition | Action |
|---------|-----------|--------|
| **#1** | Device classification remains undefined after request for product info. | Escalate to senior RA lead for clarification and possible consultation with MFDS. |
| **#2** | KGMP certification or MDSAP report is not available within 10 days. | Initiate on‑site audit planning; involve quality assurance manager. |
| **#3** | Any of the identified evidence gaps (local clinical data, Korean labeling, risk management file) persist beyond the next review checkpoint (7 days). | Elevate to regulatory affairs manager for timeline impact assessment and potential external consultancy. |

---

### 7. Peer Review Prompt

> **@RA‑Peer:** Please evaluate whether the assumed equivalence between the ISO‑13485 clauses listed in the source and the Korean KGMP requirements is complete, especially regarding any recent MFDS notices that may have introduced additional Korean‑specific obligations (e.g., electronic record‑keeping standards or updated labeling annexes). Also, confirm if any foreign clinical evidence acceptance criteria have changed since the last known MDR Annex IX update, which could affect the need for local clinical data. Your challenge of these assumptions will help ensure no jurisdictional gaps remain.

--- 

*End of regulatory draft.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 122/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,317자 | — |
| 규제 식별자 인용 | 6개 | — |
| source excerpt 근거 일치 | **2/6 (33%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 4개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `ISO 10993` | ISO 10993 | 의료기기 생물학적 안전성 평가 — ISO 14971 위험관리에 반영 |
| `Annex III` | MDR Annex III | Technical documentation on post-market surveillance |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "27d2643c8fd56aa9", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "6e09bc3b8dcd278f80184587a5eaba125f19dbc86c1b2ce2f24b76bdc503c9a0"} -->

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

> **Regulatory Draft – KG GMP Evidence Readiness (MFDS)**  

---

### 1. Device Classification & Submission Route  
| Item | Requirement | Comment |
|------|-------------|---------|
| **Intended Use / Indications** | Must be defined in Korean to allow MFDS “품목분류 고시” determination. | No intended‑use statement is present in the source excerpts – **missing**. |
| **Risk Class (MFDS)** | Determined by the MFDS medical‑device classification notice (품목분류). Classes Ⅰ, Ⅱ, Ⅲ, Ⅳ map to “신고” (notification) for Ⅰ/Ⅱ and “허가” (approval) for Ⅲ/Ⅳ. | Classification cannot be assigned without functional description – **missing**. |
| **Submission Route** | • Class Ⅰ & low‑risk Class Ⅱ → **신고** (simple notification). <br>• High‑risk Class Ⅱ, all Class Ⅲ/Ⅳ → **허가** (full approval) with full dossier. | Determination pending classification step. |

*Citation:* MFDS 품목분류 고시 (current edition) – established regulatory reference (no source excerpt needed).  

---

### 2. KGMP Evidence – Required Documentation (per MFDS 고시 제2025‑22호)  
| Required Item | Regulatory Basis | Current Status |
|---------------|------------------|----------------|
| **Quality Manual & QMS** (aligned to ISO 13485:2016) | “MFDS GMP 고시 요구사항 해설 및 ISO 13485 정합 매핑” – see source [1] (Chunk 107140411445338936). | **Present** only as a high‑level mapping; detailed manual still required. |
| **30 Core SOPs** (e.g., SOP‑CC‑001, SOP‑MFG‑001 … SOP‑NC‑001) | Listed in source [1]; MFDS expects complete SOP set for each QMS process. | SOP titles identified, but full content not provided – **missing**. |
| **Design & Development Dossier** (design history file, DHF) | Required for all classes; especially critical for Class Ⅱ‑고위험 and above. | Not referenced in source – **missing**. |
| **Risk Management File** (ISO 14971) | Mandatory for any device with risk > trivial. | No evidence shown – **missing**. |
| **Software Validation** (if applicable) | Updated requirement: “IEC 62304 전면 참조 편입” – see source [2] (Chunk 1127747106119376174). | Must provide full IEC 62304:2006+A1 compliance evidence; not yet supplied – **missing**. |
| **Cybersecurity Management** (if applicable) | “사이버보안 관리 요구(부속서 참조)” introduced in 고시 제2025‑22호 – source [2]. | No cybersecurity plan provided – **missing**. |
| **KGMP Certificate** (MFDS 인증) | Required for any manufacturing facility submitting a 허가 dossier; must be current and reflect compliance with the 30 SOPs. | Not shown in source – **missing**. |
| **Device‑Specific Non‑clinical Data** (biocompatibility, bench testing) | Accepted if OECD‑aligned or referenced by foreign regulatory clearance; MFDS now allows broader “광범위” data submissions per 고시 제2025‑22호 – source [2]. | No non‑clinical data listed – **missing**. |
| **Clinical Evaluation Report (CER)** | Local clinical data required when foreign evidence insufficient; MFDS may accept CE/FDA data if device class and risk permit. | No CER referenced – **missing**. |
| **Labeling & IFU in Korean** | Mandatory for market entry; must meet MFDS labeling regulations (Korean language, lot/expiry, warnings). | Not present in source – **missing**. |

---

### 3. Identified Gaps (Information Needed to Close the Dossier)

| Gap | Why Critical | Action |
|-----|--------------|--------|
| **Intended‑Use Statement & Device Description (Korean)** | Drives classification, labeling, and clinical evidence need. | Obtain from product owner / marketing. |
| **Risk Class Determination** | Determines submission pathway (신고 vs 허가). | Perform MFDS risk‑class mapping once intended use is known. |
| **Full SOP Set & QMS Documentation** | MFDS inspection will audit each of the 30 core processes. | Draft, review, and approve all SOPs; map to ISO 13485 clauses. |
| **Design History File (DHF) & Design Controls** | Required for Class Ⅱ‑고위험+ and all 허가 submissions. | Compile specifications, design reviews, verification/validation reports. |
| **IEC 62304 Software Validation Evidence** | New mandatory reference per 고시 제2025‑22호; missing leads to rejection. | Conduct full software life‑cycle activities, produce validation protocol & report. |
| **Cybersecurity Management Plan** (if device includes software/networking) | MFDS now expects documented controls when applicable. | Perform threat analysis, define mitigation measures, document in a Cybersecurity Dossier. |
| **KGMP Certificate for Manufacturing Site** | Essential proof of GMP compliance; without it no 허가 can be granted. | Secure current KGMP audit report or schedule an MFDS‑approved audit. |
| **Non‑clinical & Clinical Evidence** | Must satisfy safety/effectiveness requirements; foreign data acceptance is limited to OECD‑aligned studies. | Gather biocompatibility, performance testing reports; determine need for local clinical trial or CE/FDA bridge study. |
| **Korean Labeling/IFU** | Legal prerequisite; MFDS rejects submissions lacking Korean language labeling. | Prepare label artwork and IFU in Korean; submit for MFDS review. |

---

### 4. Risk Controls (Mapping to Evidence)

| Control Area | Standard / Guideline | Evidence Needed |
|--------------|----------------------|-----------------|
| **Overall QMS** | ISO 13485:2016 | Quality Manual, SOPs, internal audit reports. |
| **Product‑Specific Risk Management** | ISO 14971 | RMF (Risk Management File) with hazard analysis, FMEA, risk acceptability justification. |
| **Software Life‑Cycle** | IEC 62304:2006+A1 | Software Development Plan, verification & validation test reports, configuration management records. |
| **Cybersecurity** | MFDS 부속서 “사이버보안 관리 요구” (2025‑22) | Threat model, security architecture diagram, incident response SOPs. |
| **Post‑Market Surveillance (PMS)** | MFDS PMS 규정, ISO 13485 clause 8.2.1 | PMS plan, vigilance reporting procedure, field safety corrective action (FSCA) process. |

---

### 5. Citations  

* Established regulatory references (facts):  
  * MFMF 고시 제2025‑22호 – expanded submission material scope and SOP mapping (source [2]).  
  * ISO 13485:2016 – QMS standard aligned with MFDS GMP requirements (source [1]).  
  * IEC 62304:2006+A1 – full software validation reference (source [2]).  

* Case‑level identifiers: none appear in the provided excerpts. → **no specific identifier found in source — verify separately**.

---

### 6. Regulatory Judgment & Human‑Escalation Triggers  

| Trigger | Reason for Escalation |
|--------|-----------------------|
| **Unresolved Device Classification** (intended use unknown) | Cannot determine submission route; risk of applying wrong regulatory pathway. |
| **Missing KGMP Certificate** | MFDS will reject any 허가 dossier without proven manufacturing GMP compliance. |
| **Incomplete Software Validation / IEC 62304 evidence** (for devices with software) | New mandatory requirement under 고시 제2025‑22호; omission leads to non‑acceptance. |
| **Absence of Cybersecurity Plan where applicable** | MFDS may deem the dossier insufficient for devices with connectivity. |
| **Lack of Korean labeling / IFU** | Legal prerequisite – MFDS will request revisions before review can proceed. |
| **Insufficient clinical evidence (no CER, no foreign bridge data)** | If local clinical trial is required, omission blocks approval. |
| **Any contradictory or outdated SOPs vs ISO 13485 mapping** | MFDS auditors compare directly; discrepancy triggers a “supplementary information” request. |

*If any of the above triggers are observed, the RA lead should immediately notify the project manager and halt dossier submission until the gap is resolved.*  

---

### 7. Peer‑Review Prompt  

> **Colleague Review Request:**  
> Please examine the assumptions made regarding the necessity of a full IEC 62304 validation package and the cybersecurity management plan, given that the source excerpts only note the regulatory shift (high‑level mention) but do not detail product‑specific software scope. Also verify whether the “30 core SOPs” list is exhaustive for KGMP compliance or if any additional MFDS‑specific procedures are required under the latest 고시 제2025‑22호. Highlight any jurisdictional gaps (e.g., labeling nuances, local clinical data thresholds) that may have been overlooked.

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 121/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,215자 | — |
| 규제 식별자 인용 | 3개 | — |
| source excerpt 근거 일치 | **2/3 (66%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 1개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "eea60cd4f902896b", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

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

> **Regulatory Draft – Korean Digital‑Medical Device (DM‑Device) – Evidence Readiness for KGMP**

---

### 1. Product Scope & Likely Classification  

| Item | Detail |
|------|--------|
| **Applicable law** | Digital Medical Device Act (디지털의료제품법), effective 2026‑01‑24 (Law No. 20139). |
| **Reference articles** | Art. 9 – Clinical trial plan approval; Art. 10 – Clinical performance test plan approval; Art. 13 – Ongoing compliance (defect reporting, cyber‑vulnerability mitigation); Art. 15 – “Real‑world use evaluation” (RWE); Art. 17 – Application & assessment of the “Excellent Management System” certification (GMP‑type); Art. 39 – Pre‑submission review with MFDS. |
| **Classification basis** | Under the Medical Device Act (MDA) and its classification tables, DM‑devices are classified by risk (Class I–IV). The act does **not** change the risk‐based class; it adds supplemental obligations (e.g., Art. 13 cyber duties).  <br>→ If the device is a software‑only AI diagnostic tool that performs high‑risk clinical decision support, it will typically be **Class III** or **IV** under MDA. The exact subclass should be confirmed by MFDS pre‑consultation (Art. 39). |
| **Submission route** | • **Class I / II** – “Notification” (신고)  <br>• **Class III / IV** – “License/Approval” (허가) with full technical dossier and clinical evidence.  <br>→ Given the likely high‑risk nature, assume **license (허가)** pathway. |

---

### 2. Evidence Required for a License Application  

| Evidence | MFDS requirement | Where it originates in the Act / Standard |
|----------|------------------|---------------------------------------------|
| **Technical Documentation** (Design Dossier, risk management file, software verification & validation) | Article 39 (pre‑review) + MDA Annex 3 | MFDS Technical File requirements; ISO 13485:2016 (quality system). |
| **KGMP Certificate** for manufacturing site | Article 17 – “Excellent Management System” certification (K‑GMP equivalent) | MFDS GMP‑type audit, reference to **Good Manufacturing Practice (GMP) for Medical Devices** (pharma law). |
| **Clinical Evidence** – either: <br>· Clinical trial results **(Art. 9)**  <br>· Clinical performance test results **(Art. 10)** | Article 9 or Article 10 (whichever is appropriate to the device) | Must be approved by MFDS before data collection; aligns with **ISO 14155** for clinical investigations of medical devices. |
| **Real‑World Evidence (RWE) / Post‑Market Real‑Use Evaluation** – optional, supplementary | Article 15 – “실사용 평가” (real‑use evaluation) | Used only after market launch to support ongoing safety & efficacy; not a substitute for pre‑market clinical data. |
| **Cybersecurity & Vulnerability Management Plan** | Article 13 – Ongoing compliance (defect collection, cyber vulnerability mitigation) | MFDS guidance on “Medical Device Cybersecurity” (2024‑07 notice). |
| **AI Change‑Management / PCCP** (if AI‑based) | Not linked to Art. 17; separate MFDS AI guideline (2023‑12) | Demonstrates controlled algorithm updates. |
| **Labeling & IFU in Korean** | MDA § 30 (labeling), MFDS notification format | All labeling, instructions for use, and promotional material must be in Korean. |

---

### 3. Gaps / Missing Information Identified in Source  

| Gap | Reason (source) | Required action |
|-----|----------------|-----------------|
| **Mis‑alignment of “clinical efficacy” with Art. 15** | The source (D4 – DR‑07) flags that clinical efficacy/assessment likely belongs to Art. 9 or Art. 10, not Art. 15. | Revise the dossier to cite **Art. 9** (clinical trial approval) *or* **Art. 10** (clinical performance test) for any pre‑market clinical data. Remove any claim that Art. 15 covers efficacy. |
| **Absence of KGMP certification reference** | No mention of Art. 17 compliance in the excerpt. | Obtain or confirm “Excellent Management System” (KGMP) certificate before submission; attach audit report. |
| **No explicit pre‑submission consultation record** | Art. 39 is noted but no evidence that a pre‑review request has been filed. | Submit a pre‑consultation request to MFDS per Art. 39, documenting intended evidentiary package. |
| **Cyber‑vulnerability & AI change management not addressed** | Article 13 obligations are listed in the source but there is no plan described. | Prepare a cybersecurity risk assessment and an AI algorithm change‑control (PCCP) document. |
| **Korean language labeling / IFU missing** | Not mentioned in source; required under MDA. | Create Korean‐language label & IFU, ensure compliance with MFDS labeling rules. |

---

### 4. Risk Controls to be Demonstrated  

1. **Software Lifecycle Management** – conform to IEC 62304 (medical device software life‑cycle processes).  
2. **Usability Engineering** – per IEC 62366‑1; include human factors validation for UI/UX.  
3. **Cybersecurity Safeguards** – network protection, authentication, regular vulnerability scanning; documented in a “Cybersecurity Management Plan” referenced to Art. 13.  
4. **AI Algorithm Governance** – PCCP (Post‑Change Clinical Performance) covering data drift monitoring, version control, and re‑validation after each update.  
5. **Quality System (KGMP)** – ISO 13485‑based quality management system audited for “Excellent Management System” certification (Art. 17).  

---

### 5. Citations (Established Regulatory References)

| Citation | Content |
|----------|---------|
| Digital Medical Device Act, Art. 9 | Clinical trial plan approval requirement. |
| Digital Medical Device Act, Art. 10 | Clinical performance test plan approval requirement. |
| Digital Medical Device Act, Art. 13 | Ongoing compliance – defect reporting & cyber‑vulnerability mitigation. |
| Digital Medical Device Act, Art. 15 | Definition of “real‑use evaluation” (RWE) – **not** clinical efficacy. |
| Digital Medical Device Act, Art. 17 | Procedure for “Excellent Management System” certification (KGMP‑type). |
| Digital Medical Device Act, Art. 39 | Pre‑submission review procedure with MFDS. |
| ISO 13485:2016 | Quality management system requirements for medical device manufacturers. |
| IEC 62304 | Software life‑cycle processes for medical devices. |
| IEC 62366‑1 | Usability engineering in medical devices. |
| ISO 14155 | Clinical investigation of medical devices (aligned with Art. 9/10). |

*No specific case identifiers (e.g., 510(k), predicate numbers) appear in the source excerpts; therefore: **no specific identifier found in source — verify separately**.*

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger for RA / Project Lead |
|-----------|-------------------------------|
| Uncertainty whether clinical data must be submitted under Art. 9 or Art. 10 (device class ambiguous). | **Escalate** to MFDS via pre‑consultation (Art. 39) before dossier finalisation. |
| KGMP certificate not yet issued or audit pending. | Pause submission; **escalate** to Quality/Manufacturing lead for immediate certification action. |
| Cybersecurity plan incomplete or lacking vulnerability remediation schedule. | **Escalate** to Software Development & Security teams – risk of MFDS rejection under Art. 13. |
| Real‑world evidence being used as primary efficacy data without prior clinical trial approval. | **Escalate** to Clinical Affairs – re‑align evidentiary strategy to Art. 9/10. |
| Korean labeling/IFU not finalized or translation pending. | **Escalate** to Regulatory Documentation team – MFDS rejects non‑Korean labeling. |

---

### 7. Summary Judgment  

- The device is likely a **high‑risk (Class III/IV) digital medical device**, requiring a **license (허가)** pathway.
- Pre‑market clinical evidence must be obtained through **Art. 9** (clinical trial) or **Art. 10** (performance test); **Art. 15** can only support post‑market RWE, not primary efficacy.
- KGMP certification (Article 17) and a complete Korean‑language labeling set are mandatory before submission.
- Cybersecurity obligations (Art. 13) and AI change‑management (PCCP) must be documented and integrated into the risk management file.
- Immediate actions: correct the regulatory citation from Art. 15 to Art. 9/10, secure KGMP certificate, submit a pre‑consultation request (Art. 39), and prepare Korean labeling.

**Human escalation is required whenever any of the above evidence gaps remain unresolved before dossier closure.**

---

### 8. Peer Review Prompt  

*@RA‑Peer*: Please challenge the assumptions made regarding (1) the classification of this AI‑based software as Class III/IV without a detailed functional description, (2) the sufficiency of citing only Articles 9 and 10 for clinical evidence in lieu of potential hybrid evidence pathways, and (3) any jurisdiction‑specific gaps that may exist between the Digital Medical Device Act and the underlying Medical Device Act, especially concerning labeling exceptions. Your feedback will help ensure full coverage of Korean regulatory obligations.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 120/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,979자 | — |
| 규제 식별자 인용 | 16개 | — |
| source excerpt 근거 일치 | **0/16 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 16개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art. 9`, `Art. 10`, `Art. 13`, `Art. 15`, `Art. 17`, `Art. 39`, `ISO 14155`
> MDR 주요 조문·부속서 및 표준 6종 외 식별자입니다. source 근거 여부를 직접 확인하십시오.

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "8846cdbbcfe9b155", "source": "github:holee9/MD-process/issue-drafts/066_01_MFDS_GMP_v0.2_30대절차매핑.md", "source_hash": "9d7fca670a56a64ee146225dc0fd583c83903c5ac050153cfe8226de5bb6a750"} -->

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

> **Regulatory Draft – KGMP Evidence Readiness**

---

### 1. Device Classification & Submission Route (to be confirmed)

| Item | Current Status | Required Action |
|------|----------------|-----------------|
| **Risk class (Ⅰ‑Ⅳ)** | *Not identified in source* – no information on intended use, patient population, or risk level. | Conduct a classification assessment according to MFDS “의료기기 등급‧분류 기준” (KMH‑MDR Annex III). |
| **Submission type** | Dependent on the determined class: <br>• Class Ⅰ – 신고 (Notification) <br>• Class Ⅱ,Ⅲ – 허가 (Approval) <br>• Class IV – 허가(특별허가) | Resolve classification before selecting the pathway. |

*Human‑escalation trigger:* If classification cannot be determined within 5 business days, the RA lead must be alerted to engage product development for intended‑use clarification.

---

### 2. KGMP Evidence Package – Required Elements  

| KGMP Requirement (MFDS “의료기기 제조 및 품질관리 기준”) | Evidence Needed | Current Gap (per source) |
|----------------------------------------------------------|-----------------|---------------------------|
| **Documentation of ISO 13485:2016 requirements** – 35 items mapped by the project team. | Complete, Korean‑language SOPs / work instructions covering each item; cross‑reference matrix to MFDS clauses. | 8 items remain undocumented (priority list identified). |
| **SOP Coverage** | Evidence that all critical processes are covered by SOPs ≥ 90 % (industry benchmark) and that the remaining gaps are mitigated. | Current coverage reported at 69 %; 31 % of required SOPs missing. |
| **Facility Qualification / Validation** | Process validation reports, equipment qualification (IQ/OQ/PQ), cleaning validation where applicable. | Not mentioned in source; assume missing. |
| **Quality Management System (QMS) Audits** | Internal audit reports and corrective action records demonstrating compliance with KGMP. | No evidence cited. |
| **Non‑clinical & Clinical Evidence** (if class Ⅱ–Ⅳ) | – Non‑clinical safety data (bench, animal studies).<br>– Clinical evaluation report (CER) or foreign clinical data accepted per MFDS scope expansions (e.g., FDA 510(k) predicate, CE mark). | No identifiers found in source – verify separately. |
| **Labeling & IFU** | Korean‑language labeling, instructions for use, safety information, and traceability code per MFDS “라벨·사용설명서 기준”. | Not addressed in source. |
| **Post‑Market Surveillance (PMS) Plan** | PMS system description, adverse event reporting procedures, periodic safety update report (PSUR). | Not mentioned. |

*Human‑escalation trigger:* Any of the above evidence items that remain absent after a 10‑day remediation window must be escalated to the Project Manager and senior RA for risk assessment.

---

### 3. Risk Controls & Alignment with Standards  

| Control Area | Korean Requirement / Standard | Mapping to KGMP Evidence |
|--------------|-------------------------------|--------------------------|
| **Risk Management** | ISO 14971 (adopted by MFDS) – risk analysis, evaluation, control, and post‑market monitoring. | Include a complete Risk Management File (RMF) referenced in the QMS SOPs. |
| **Process Controls** | KGMP mandates documented process controls, batch release criteria, and deviation handling. | Provide SOPs for manufacturing steps; document deviations and CAPA for the 8 missing items. |
| **Traceability** | MFDS requires unique device identifier (UDI) or serial number linked to lot records. | Show traceability matrix in the QMS documentation. |
| **Supplier Management** | Supplier qualification per KGMP “공급자 관리”. | Submit supplier audit reports and quality agreements. |

*Human‑escalation trigger:* If any risk control is not demonstrably linked to documented evidence, raise a non‑conformance to Quality Assurance within 3 days.

---

### 4. Citations  

| Topic | Citation (established regulatory reference) |
|-------|---------------------------------------------|
| KGMP certification requirements | MFDS “의료기기 제조 및 품질관리 기준” (제조·품질 관리 기준). |
| ISO 13485:2016 documentation mapping | Internal project mapping of 35 ISO 13485 items – see source excerpt [1]. |
| SOP coverage analysis | Project SOP coverage report (69 %); priority list of 8 missing SOPs – source excerpt [1]. |
| Cross‑verification documents | `01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조 및 품질관리 기준.md` and `12_교차검증_보고서/2026-05-07_GMP절차매핑_영상품질QC_정합성.md` – source excerpt [2]. |
| Device classification rules | MFDS “의료기기 등급‧분류 기준” (Annex III of the Korean Medical‑Device Regulation). |
| Clinical/foreign evidence acceptance scope | Latest MFDS notice expanding accepted foreign clinical evaluation reports (specific notice number to be verified). |

*Case‑level specific identifiers*: No 510(k), predicate, or registration numbers appear in the source excerpts – **no specific identifier found in source — verify separately**.

---

### 5. Human‑Escalation Triggers Summary  

| Trigger | Condition | Escalation Path |
|---------|-----------|-----------------|
| Classification unknown | No risk class defined after initial assessment | Notify RA Lead → Product Development for intended‑use clarification |
| KGMP documentation gaps > 0 | Any of the 8 missing SOP items remain unresolved after 10 days | Raise to Project Manager & senior RA; open non‑conformance in QMS |
| Missing mandatory evidence (clinical, labeling, PMS) | Evidence absent after 5 day gap from submission checklist | Escalate to Regulatory Strategy Lead for supplemental data plan |
| Risk control not linked to documented evidence | Unresolved risk mitigation in RMF or process controls | Immediate report to Quality Assurance & initiate CAPA |
| Deadline breach for KGMP certification | Submission of KGMP dossier > 30 days overdue from project schedule | Senior management notification; consider timeline reset |

---

### 6. Reusable RA Judgment (Lesson Learned)

> **When preparing a KGMP evidence package, first confirm device classification to define the submission route and required clinical/non‑clinical data. Then perform an exhaustive mapping of ISO 13485:2016 documentation requirements against MFDS “제조 및 품질관리 기준”. Any uncovered SOPs or process controls must be prioritized (as demonstrated by the 8 high‑priority gaps) and addressed within a defined remediation window, with clear escalation triggers for each missing element. Early verification of foreign clinical evidence acceptance scope prevents later delays.**

---

#### Peer Review Prompt  
*Please review this draft:*

1. **Assumptions:** Have I correctly assumed that all 35 ISO 13485 items are mandatory under current MFDS KGMP guidance, or are any exempt for low‑risk Class Ⅰ devices?  
2. **Source Coverage:** Does the reliance on excerpts [1] and [2] adequately capture all required evidence elements, or are additional regulatory documents (e.g., MFDS notice on foreign clinical data) missing from the analysis?  
3. **Jurisdiction Gaps:** Are there any Korean‑specific obligations—such as electronic submission format, Korean language labeling details, or post‑approval change management—that need explicit mention beyond what is listed?

*Kindly challenge the above points and suggest any additional items that should be incorporated before finalizing.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 119/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,287자 | — |
| 규제 식별자 인용 | 3개 | — |
| source excerpt 근거 일치 | **1/3 (33%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 2개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex III` | MDR Annex III | Technical documentation on post-market surveillance |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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

### kb-eval-20260720-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-20", "decision_ref": "kb-eval-20260720-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "0dcf58c86b60f918", "source": "github:holee9/MD-process/issue-drafts/911_AUDIT_QM-001_MFDS_별표2_보관기간_1차출처_미확인.md", "source_hash": "95f44332028afe7accb07da52f06d3d9910a29bfb18a213c9c2328789985e29c"} -->

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

> **Regulatory Draft – KGMP Evidence Readiness (Quality‑Manual Retention Requirement)**  

---

### 1. Device Classification & Submission Route  
| Item | Assessment | Comment |
|------|------------|---------|
| **Classification (risk class)** | *Not identifiable from source.* The device’s intended use, invasiveness, duration of contact and other risk determinants must be reviewed to apply the Korean Medical‑Device Act (MDA) classification rules (e.g., §§3‑5 of the MDA). | Determine Class I / II / III / IV before selecting submission pathway. |
| **Possible Submission Pathways** | • **Class I** – Notification (신고)  <br>• **Class II** – Conditional Approval (조건부 허가) or General Approval (일반 허가) depending on risk & product type  <br>• **Class III / IV** – Full Approval (허가) with full technical dossier | The final route is driven by the classified risk level. |

### 2. Core Evidence Required for KGMP‑Compliant Submission  
| Category | Required Item | Korean Regulatory Basis |
|----------|---------------|------------------------|
| **KGMP Certification** | Facility must hold a current KGMP certificate (MFDS 고시 “의료기기 제조 및 품질관리 기준” 별표 2). | MFDS 고시 – 의료기기 제조·품질관리 기준, 별표 2 |
| **Quality‑Manual & Document Retention** | • Up‑to‑date Quality Manual  <br>• Defined retention period for the Quality Manual (and related QMS records) | MFDS 고시 “별표 2 기록보관 요건” – specifies the required storage duration for each QMS document. |
| **Technical Documentation (Design Dossier)** | Design History File, Device Description, Intended Use, Labeling, IFU, Software Files, etc. | MDA 시행규칙 §§13‑16 (technical file requirements). |
| **Risk Management** | ISO 14971‑based risk analysis & risk control report; evidence that retained records support post‑market risk controls. | MFDS 고시 – 위험도 관리 요구사항 (별표 2) |
> **Citation:** “의료기기 제조 및 품질관리 기준 별표 2 기록보관 요건” (MFDS 고시). The source excerpt notes that the exact retention period must be extracted directly from this notice; it is currently *unverified*.

| **Clinical Evaluation** | • Clinical evidence satisfying Korean requirements (local clinical data if required, or accepted foreign CE/FDA data per MFDS notice on expanded foreign evidence). | MFDS 고시 – 임상평가 기준 (연혁 2023‑xx) |
| **Labeling & IFU** | All labeling and Instructions for Use must be in Korean, with mandatory statements (e.g., “제조사·수입자 연락처”, “보관 기간” etc.). | MFDS 고시 – 라벨링 요건 (별표 4). |
| **Post‑Market Surveillance** | PMS plan, adverse event reporting system, and periodic safety update reports. | MFDS 고시 – 시판후조사 규정 (별표 5). |

### 3. Gaps / Missing Information Identified from Source  

| Gap | Why it Matters | Action Required |
|-----|----------------|-----------------|
| **Exact retention period for the Quality Manual** | The source states “구체적 기간은 미확인 – 1차 출처 재확인 필요”. Without a definitive number, KGMP compliance cannot be demonstrated. | Retrieve the latest MFDS 고시 (medical‑device manufacturing & quality‑control standards) and quote the precise retention period for the Quality Manual (e.g., “5 years” if specified). |
| **Device–specific classification** | Classification drives the submission route and evidence set. | Conduct a risk‑based classification exercise using MDA §§3‑5; document justification. |
| **Intended Use & Indications** | Needed for classification, clinical evaluation scope, labeling. | Obtain from product development team or marketing dossier. |
| **Predicate device / foreign clearance references (if any)** | If leveraging FDA 510(k) or CE Mark data, must verify MFDS acceptance per the latest notice expanding foreign evidence. | Identify any existing foreign regulatory clearances; confirm their admissibility under current MFDS guidance. |
| **Korean‑language labeling & IFU** | Mandatory for market entry; absence will block approval. | Prepare Korean translation and ensure compliance with labeling checklist. |
| **Evidence of change‑control & document‑archiving procedures** | Required to support the retention claim and overall QMS compliance. | Provide SOPs describing record archiving, access control, and disposal after the statutory period. |

### 4. Risk Controls Related to Documentation Retention  

| Control | Description | Reference |
|--------|-------------|-----------|
| **Document‑Control SOP** (QMS‑D‑001) | Defines creation, review, approval, distribution, and storage of QMS records, including the Quality Manual. | MFDS 고시 – 별표 2 (기록보관 요건). |
| **Retention Schedule Matrix** | Maps each document type to its statutory retention period; includes periodic audit verification that files remain intact for the required duration. | Same as above; must reflect verified period from the 고시. |
| **Physical & Electronic Archiving** | Dual‑mode storage (on‑site + secure cloud) with disaster‑recovery plan; ensures accessibility throughout the mandated interval. | KGMP facility audit criteria (§4.4). |
| **Periodic QMS Audits** | Internal audits every 12 months to verify that records are retained per schedule and that any overdue disposal is prevented. | MFDS 고시 – 품질관리 규정 (별표 2). |

### 5. Human‑Escalation Triggers  

1. **Unverified Retention Period** – If the exact statutory period cannot be confirmed within 3 business days, senior RA/QA lead must be notified to halt submission preparation until clarification is obtained.  
2. **Classification Ambiguity** – When risk classification cannot be resolved after initial assessment, elevate to cross‑functional review (RA, Clinical, Engineering) and suspend dossier finalization.  
3. **Foreign Evidence Acceptance Uncertainty** – If any foreign clinical or non‑clinical data are planned for use, a formal request to MFDS (or an experienced regulatory consultant) is required before inclusion; escalation to the RA manager if response exceeds 2 weeks.  
4. **Korean Labeling Deficiency** – Any missing Korean translation or mandatory label statement must trigger immediate QA/Regulatory liaison with the localization team; submission freeze until resolved.  
5. **KGMP Certificate Lapse** – If the KGMP certificate is due to expire within the next 90 days, initiate renewal process and notify project leadership; do not submit filings without a valid certification.

### 6. Summary Judgment  

- The **core deficiency** in the current evidence set is the *unverified statutory retention period* for the Quality Manual as required by MFDS 고시 “의료기기 제조 및 품질관리 기준 별표 2”.  
- Until this period is extracted from the latest official notice and documented, the KGMP compliance claim remains incomplete and must be **escalated** to senior RA/QA for resolution.  
- Additional gaps (device classification, intended use, labeling in Korean, any planned foreign evidence) also need closure before a submission route can be definitively selected.  

---

### Peer‑Review Prompt  

> @RA‑Peer: Please review the assumptions made regarding the KGMP documentation retention requirement and the classification pathway. Are there other MFDS notices or recent guideline updates (e.g., post‑2023 scope extensions on foreign evidence) that might affect the evidentiary expectations for this dossier? Highlight any jurisdiction‑specific gaps not covered here.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 118/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,218자 | — |
| 규제 식별자 인용 | 1개 | — |
| source excerpt 근거 일치 | **0/1 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 1개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

> excerpt는 source의 일부 chunk만 담으므로 미대조가 곧 창작은 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 합니다.

<!-- /verification-summary -->
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
