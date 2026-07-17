# KB Eval Checksheet - 2026-07-18 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260718-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_us-001", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "b0105269422dbaf0", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `b0105269422dbaf0`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/README.md)
- Source hash: `1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `README.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용 ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Info...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Predicate‑Strategy Blueprint**

---

### 1. Bottom‑Line Recommendation
- **Classification & Route:** Submit a Traditional 510(k) (K-Number) seeking clearance under the *same product code* as an existing legally marketed predicate device.  
- **Key Action:** Compile a Substantial Equivalence (SE) comparison matrix and populate all eSTAR sections (Device Description, Indications for Use, Performance Testing, Biocompatibility, Electromagnetic Compatibility, etc.) before electronic submission.

---

### 2. Determination of Device Classification & Submission Pathway
| Step | Action | Rationale |
|------|--------|-----------|
| **a. Predicate Search** | Query the FDA 510(k) Database for devices sharing the same intended use and technological characteristics. | Required first step per source excerpt [2]. |
| **b. Product Code Confirmation** | Verify that identified predicates fall under the same product code (e.g., “LZ” for a pulse oximeter). | Ensures regulatory parity; if none exist, consider De Novo. |
| **c. Submission Type** | Use *Traditional 510(k)* unless a Special or Abbreviated route is justified by design changes only. | Traditional pathway provides the most straightforward SE narrative. |

---

### 3. Evidence Package Required (per eSTAR template)
1. **Device Description & Indications for Use** – Follow guidance from eSTAR Section 01 (excerpt [1]).  
2. **Substantial Equivalence Comparison Table** – List each predicate, stating: device name, K-number, intended use, technological characteristics, and differences.  
3. **510(k) Summary** – Concise narrative of the device, its function, and SE justification.  
4. **Performance Testing** – Bench, animal, or clinical data demonstrating functional equivalence (e.g., accuracy, repeatability).  
5. **Biocompatibility** – ISO 10993‑1 based assessment for all patient-contacting materials.  
6. **Electromagnetic Compatibility (EMC)** – IEC 60601‑1‑2 compliance testing results.  
7. **Labeling & IFU** – Complete labeling package aligned with FDA QSR 21 CFR 820.120.  
8. **Quality System Documentation** – ISO 13485‑aligned QMS evidence per the new QMSR (effective Feb 2026).  

---

### 4. Missing Information / Gaps to Resolve Before Submission
| Item | Why it’s missing | Required action |
|------|------------------|-----------------|
| **Device description & IFU details** | Only a generic guide referenced (eSTAR_01) – no actual product text provided. | Draft complete Device Description and Indications for Use sections. |
| **Predicate device identifiers** | No specific K‑numbers or 510(k) numbers appear in source material. | Conduct FDA database search to capture exact predicate IDs; record them for the SE table. |
| **Risk Management Documentation** | Not mentioned in excerpts. | Generate a risk analysis (ISO 14971) and map risk controls to identified hazards. |
| **Performance test protocols & results** | No data supplied. | Design and execute testing plan; collect raw data and statistical analyses. |
| **Biocompatibility & EMC test reports** | Absent from source. | Perform required ISO/IEC tests; archive certificates of analysis. |

---

### 5. Risk Controls (ISO 14971‑Based)
1. **Hazard Identification:** List all functional, electrical, and software hazards associated with the device.  
2. **Risk Evaluation:** Assign severity & probability; compute risk level.  
3. **Mitigation Measures:**  
   - Design controls (e.g., redundant sensors).  
   - Protective measures (e.g., shielding for EMC).  
   - Information controls (warnings, user training in IFU).  
4. **Verification of Controls:** Demonstrate via testing or analysis that residual risk is Acceptable.  

---

### 6. Source Citations
- **Procedure Overview & Predicate Search** – “제출 절차 개요 … Predicate Device 조사 (FDA 510(k) Database)” (Excerpt [2]).  
- **eSTAR Section‑by‑Section Guidance** – “Device Description / Indications for Use 작성 가이드” (Excerpt [1]).  

*No specific predicate identifiers (K‑numbers, case IDs) appear in the provided excerpts—verify separately.*

---

### 7. Human‑Escalation Triggers
| Situation | Escalation To |
|-----------|---------------|
| **Unclear product code or no clear predicate** | Senior RA Lead / FDA liaison for De Novo evaluation. |
| **Novel technology not captured by existing predicates** | Regulatory Strategy Committee (consider Special 510(k) or De Novo). |
| **Discrepancy between performance data and SE claim** | Biostatistics & Clinical Affairs SME for data re‑analysis. |
| **QMSR compliance gaps identified** | Quality Assurance Manager (ISO 13485/QMSR alignment). |
| **Regulatory intelligence indicates recent guidance change** | Regulatory Affairs Director for potential pathway shift. |

---

### 8. Peer Review Prompt
> *“Colleague, please review this predicate‑strategy draft and challenge:*
> - *The completeness of the SE comparison approach given we have no identified K‑numbers yet;*
> - *Whether the source excerpts fully cover all eSTAR sections required for a modern 510(k); and*
> - *If any jurisdiction‑specific nuances (e.g., state‑level requirements, post‑market surveillance expectations) have been omitted.*  
> *Your feedback will help ensure no blind spots before finalizing the submission package.”*

---

### 9. Reusable RA Judgment (to be recorded in the knowledge base)

- **Judgment:** For any new device where only generic eSTAR guidance is available, the immediate next step is a systematic predicate search in the FDA 510(k) database to capture exact K‑numbers and product codes. Absence of identifiers mandates escalation to senior regulatory staff before SE matrix construction. All required evidence modules (Device Description, Performance Testing, Biocompatibility, EMC, labeling, QMS compliance) must be completed prior to eSTAR electronic submission; missing any module is a hard stop.  

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

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20260718-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_us-002", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "21b8366cdc6c15c1", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `21b8366cdc6c15c1`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_01_Device_Description_IFU.md)
- Source hash: `70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_01_Device_Description_IFU.md`는 FDA eSTAR device description 및 IFU 작성에 필요한 제품 설명·표시 정보 문서입니다.
- 현재 excerpt 핵심: ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA For...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Strategy for Radiographic Imaging GUI Software**

---

### Bottom‑Line Recommendation
- **Submission pathway:** Traditional 510(k) (or Abbreviated if a suitable predicate exists).  
- **Classification:** Class II medical device software (IEC 62304 **Class B**), because the intended use is *“acquisition, review, and management of digital radiographic images”* with no claim to primary diagnosis.  
- **Primary predicates:** Identify an FDA‑cleared X‑ray imaging workstation or GUI that performs the same non‑diagnostic functions (e.g., “Radiology Information System – Workstation”). Use the predicate’s 510(k) number where available; if none matches, consider a De Novo request.

---

### Required Evidence Package
| Section | Content Required (per FDA guidance & 21 CFR) |
|---------|----------------------------------------------|
| **Device Description** | Detailed hardware and software architecture: modules, processes, DB schema, DICOM nodes. Include OS/minimum hardware specs and compatible detector/generator list with version numbers. |
| **Software Documentation** | IEC 62304‑aligned software life‑cycle documentation (risk management plan, design controls, verification/validation reports). State safety class (A/B/C) – for this GUI: **Class B**. |
| **Cybersecurity** | Description of authentication methods, encryption, audit logging, and any FDA‑recognized cybersecurity standards applied. |
| **SOUP Management** | List all third‑party software components, version numbers, provenance, and any risk mitigations. |
| **Intended Use & Indications for Use (IFU)** | English IFU on Form 3881, clearly stating non‑diagnostic intent; avoid “review” vs “diagnosis” confusion. |
| **DICOM Compliance** | Declaration of DICOM conformance (Storage SCU, Worklist SCU, MPPS etc.) and supporting test reports. |
| **Risk Analysis** | ISO 14971 risk management file focusing on user‑error, data integrity, and cybersecurity threats. Include mitigations tied to design controls. |
| **Labeling & Summary** | 510(k) Summary per 21 CFR 807.92; labeling consistent with intended use. |
| **Bench/Performance Testing** | Show that image acquisition, storage, and management meet performance specs of the predicate (e.g., latency, image fidelity). |
| **Software Validation** | Usability testing with trained technologists; verification that software does not alter diagnostic content. |

---

### Missing Information (to be sourced from the sponsor)
1. **Predicate device number(s)** – specific 510(k) identifiers are required to claim substantial equivalence.  
2. **Complete list of SOUP components** (including licenses, version numbers).  
3. **Cybersecurity assessment report** (threat model, mitigation matrix).  
4. **Usability validation protocol and results** (human factors data).  
5. **Full DICOM conformance test suite results**.

---

### Risk Controls Summary
| Hazard | Likelihood | Severity | Control |
|--------|------------|----------|---------|
| Unauthorized access to patient images | Medium | High | Role‑based authentication, audit logs, encryption in transit/storage |
| Corruption of image data during transfer | Low | High | End‑to‑end DICOM checksums, validation of received SOP classes |
| Misinterpretation of “review” vs “diagnosis” claim leading to off‑label use | Medium | Moderate | Clear IFU language; training program for technologists; labeling warnings |
| Failure of software modules (crash) during acquisition | Low | High | Redundant watchdog processes, graceful shutdown, automatic data recovery |
| Vulnerabilities in third‑party libraries (SOUP) | Variable | High | Regular vulnerability scanning, version lock, patch management plan |

All controls must be documented in the ISO 14971 risk file and reflected in design verification/validation.

---

### Key Citations (taken directly from source)
- **FDA “Electronic Submission Template for Medical Device 510(k) Submissions”** (final 2023 revision, eSTAR v5.x).  
- **FDA Guidance “Format for Traditional and Abbreviated 510(k)s”** (2019‑09‑13 Final).  
- **21 CFR 807.87** – required information for a 510(k) submission.  
- **21 CFR 807.92** – format of the 510(k) Summary.  
- **FDA Guidance “General/Specific Intended Use”** (1998 Final, still in effect).  
- **FDA Form 3881** – dedicated form for Indications for Use.

*No specific predicate identifier or case number was found in the supplied excerpts; verify separately before finalizing the submission.*

---

### Human‑Escalation Triggers
| Trigger | Reason | Action |
|---------|--------|--------|
| Absence of a clear predicate device number | Cannot substantiate substantial equivalence | Pause draft, request market research to locate an appropriate predicate or consider De Novo. |
| Unresolved cybersecurity vulnerabilities in SOUP | Potential FDA non‑acceptance under 21 CFR 820.30 & guidance | Escalate to senior security engineer and RA lead for risk reassessment. |
| Ambiguity in intended use wording (e.g., “review” vs “diagnosis”) | Could elevate classification to Class III | Convene a cross‑functional review with regulatory, clinical, and marketing to revise IFU. |
| Incomplete DICOM conformance evidence | May fail FDA’s performance testing expectations | Halt submission packaging until full test reports are obtained. |

---

### Peer Review Prompt
> **RA Peer:** Please examine the assumptions above regarding (1) the suitability of a Traditional vs Abbreviated 510(k), (2) the predicate search strategy given no identifiers were found, and (3) any jurisdiction‑specific gaps—especially concerning recent QMSR updates (effective Feb 2026) that align with ISO 13485. Highlight missing citations or regulatory nuances that could affect classification or evidence requirements.

---

### Reusable RA Judgment (Lesson Learned)
> *When drafting a 510(k) for radiographic imaging software, always verify the existence of a predicate device number early; without it, the submission cannot claim substantial equivalence and may need a De Novo pathway. Align software safety class with IEC 62304, explicitly separate “review” from “diagnosis” in the IFU, and assemble a complete SOUP inventory plus cybersecurity threat model before finalizing the evidence docket.*

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

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

### kb-eval-20260718-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_us-003", "iteration": 2, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "836544d7357c1aa4", "source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md", "source_hash": "a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `836544d7357c1aa4`
- Source: `github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/959_FDA_510k_RTA_%EA%B8%B0%EC%B4%88%EB%B3%B4%EA%B0%95_3%EC%A3%BC%EC%B0%A8_%EC%9E%AC%EC%9D%B4%EC%9B%94.md)
- Source hash: `a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `959_FDA_510k_RTA_기초보강_3주차_재이월.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **3주 연속 0% 정체** (06-26 / 07-03 / 07-10 동일). #951(2026-07-03 등록)이 미착수 상태로 재이월됨. ## 이관 배경 - 선행 이슈: #951 (2026-07-03 등록, status: draft, 착수 실적 없음) - 원인 추정: 이번 주 개발/QA 인력이 감사(audit) sweep(01_법규_규제, 02_품질경영시스템_QMS)에 전량 투입되어 체크리스트 보강 착수 못함
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Predicate Strategy for Pending Submission #951**

---

### Bottom‑Line Recommendation
- **Pathway:** Traditional 510(k) (Substantive) submission is the fastest credible route, provided a suitable predicate can be identified and substantial equivalence demonstrated.  
- **Immediate Action:** Conduct a focused predicate search now; parallelize preparation of performance testing data to avoid further “0 %” stall cycles observed over three weeks.  

---

## 1. Classification & Submission Route
| Item | Determination |
|------|----------------|
| **Regulatory Class** | *Class II* – most surgical/diagnostic accessories fall here; confirm based on intended use and risk level (see 21 CFR 862‑892). |
| **Submission Type** | Traditional 510(k) – required when no De Novo or Special 510(k) justification is available. |
| **Predicate Device** | Not identified in source material – **search needed** for a device with the same intended use, technological characteristics, and FDA-cleared 510(k). |

*Citation:* No specific predicate identifier found in source — verify separately.

---

## 2. Required Evidence Package

| Evidence Category | Minimum Requirement (FDA Guidance) | Status / Gap |
|-------------------|--------------------------------------|--------------|
| **Device Description** | Detailed drawings, specs, materials, software architecture. | Pending – no documentation cited. |
| **Performance Testing** | • Bench‑top functional tests (accuracy, precision)<br>• Biocompatibility per ISO 10993‑1<br>• Electrical safety (if applicable) IEC 60601‑1 | Not yet performed; audit sweep diverted QA resources (see source). |
| **Software/Usability** | If software >12 months life‑cycle → UI validation, cybersecurity threat analysis. | Unknown – missing. |
| **Sterilization Validation** (if marketed sterile) | Sterility assurance level testing per ISO 11135/13485. | Not addressed in source. |
| **Labeling & IFU** | Consistent with predicate; includes contraindications, warnings. | Draft status only (see #951 draft). |
| **Clinical Data** | Typically none for Class II if bench data demonstrates equivalence; limited clinical data may be required if substantial differences exist. | Not yet evaluated pending predicate analysis. |

*Citation:* The audit sweep of QA staff (Excerpt [2]) explains why checklist initiation is delayed.

---

## 3. Missing Information & Immediate Tasks
1. **Predicate Identification** – Perform targeted search in FDA’s 510(k) database using intended use keywords; document equivalence rationale.  
2. **Risk Management File** – ISO 14971 risk analysis, including identified hazards, severity, probability, and mitigations.  
3. **Verification & Validation Plan** – Detailed test protocols with acceptance criteria aligned to predicate performance.  
4. **QMS Alignment** – Confirm compliance with QMSR (effective Feb 2026) and ISO 13485:2016; document any corrective actions from the ongoing audit.  

*Citation:* “0% 정체” over three weeks (Excerpt [1]) signals a critical bottleneck that must be broken by completing the above items.

---

## 4. Recommended Risk Controls (ISO 14971 Framework)

| Hazard | Potential Harm | Existing Control | Additional Control |
|--------|----------------|------------------|--------------------|
| Device malfunction (e.g., sensor drift) | Misdiagnosis / delayed treatment | Built‑in self‑test, calibration routine | Periodic recalibration schedule; automated alarm for out‑of‑range readings. |
| Software error (if applicable) | Incorrect data processing | Basic code review | Full software validation per IEC 62304; cybersecurity hardening. |
| Biocompatibility issue | Local tissue reaction | Material certified to ISO 10993‑5 | Conduct extractable/leachable testing for final device configuration. |
| Sterility breach (if sterile) | Infection risk | Standard ethylene oxide sterilization | Perform sterility assurance validation (≥10⁻⁶ SAL). |

---

## 5. Citations
- **Process delays:** “3주 연속 0% 정체” (Excerpt [1])  
- **Audit impact on QA resources:** “감사(audit) sweep … 체크리스트 보강 착수 못함” (Excerpt [2])  
- **Internal case reference:** #951 (2026‑07‑03 등록) – draft status, no work started.  

*No specific FDA 510(k)/predicate identifier appears in the source excerpts; verify separately.*

---

## 6. Human‑Escalation Triggers
| Trigger | Action |
|---------|--------|
| >5 business days without a confirmed predicate device | Escalate to Lead RA and Project Manager for immediate allocation of resources. |
| Audit findings indicating QMS non‑conformance affecting the submission | Notify Quality Assurance lead; open CAPA before proceeding. |
| New regulatory guidance (post‑Feb 2026 QMSR) that materially changes evidence expectations | Pause current draft, seek Regulatory Affairs leadership input. |
| Significant resource reallocation (e.g., further QA audit sweeps) that stalls work >2 weeks | Raise to senior management for reprioritization. |

---

## 7. Reusable RA Judgment (Lesson Learned)

> **When a development/QA audit consumes the entire QA team, 510(k) preparation stalls, leading to measurable “0 %” progress over successive review cycles.**  
> **Actionable Rule:** Prior to any full‑team audit, mandate that at least one dedicated resource remains assigned to active 510(k) tasks (e.g., predicate search, test plan drafting). Capture this requirement in the project charter and monitor weekly status to prevent repeat stalls.

---

### Peer Review Prompt
> *@RA‑Peer:* Please evaluate the assumptions made regarding classification, the completeness of the evidence matrix, and any jurisdiction‑specific gaps (e.g., state‐level registration, recent QMSR updates). Identify missing sources or alternative pathways that might shorten time‑to‑clearance while maintaining compliance.

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

1. Chunk `243090506975535922`

> ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **3주 연속 0% 정체** (06-26 / 07-03 / 07-10 동일). #951(2026-07-03 등록)이 미착수 상태로 재이월됨.

2. Chunk `608844759849194169`

> ## 이관 배경 - 선행 이슈: #951 (2026-07-03 등록, status: draft, 착수 실적 없음) - 원인 추정: 이번 주 개발/QA 인력이 감사(audit) sweep(01_법규_규제, 02_품질경영시스템_QMS)에 전량 투입되어 체크리스트 보강 착수 못함

### kb-eval-20260718-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "e1f4d3a1fbd721e6", "source": "github:holee9/MD-process/issue-drafts/220_13_FDA_510k_RTA_핵심양식_초안.md", "source_hash": "2b2e64ed872d9caf987e923334f8bb1dab23e1f65d28ac42a81828e751edceb2"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `e1f4d3a1fbd721e6`
- Source: `github:holee9/MD-process/issue-drafts/220_13_FDA_510k_RTA_핵심양식_초안.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/220_13_FDA_510k_RTA_%ED%95%B5%EC%8B%AC%EC%96%91%EC%8B%9D_%EC%B4%88%EC%95%88.md)
- Source hash: `2b2e64ed872d9caf987e923334f8bb1dab23e1f65d28ac42a81828e751edceb2`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `220_13_FDA_510k_RTA_핵심양식_초안.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 배경 `build_readiness.py` 결과 FDA 510(k) RTA 점수 52% 고착. 하기 5개 must 항목이 미충족 상태로 실제 제출 시 FDA RTA(Refuse to Accept) 직행. ## 예상 효과 FDA 510(k) 점수 52% → 약 85% (5개 must 해소 시)
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Submission Strategy**

---

### 1. Device Classification & Submission Route
| Attribute | Determination |
|-----------|----------------|
| **FDA product class** | *Presumed Class II* (most medical devices with a 510(k) pathway fall here; confirm via classification regulation § 862.*). |
| **Submission type** | Traditional **510(k)** (premarket notification). No De Novo or special/abbreviated pathways indicated. |
| **Regulatory reference** | 21 CFR 807 – Premarket Notification [§ 807.92]. |

---

### 2. Required Evidence Package (minimum for a complete 510(k))

| Section | Content Required | Typical Supporting Documents |
|---------|------------------|------------------------------|
| **Device description & intended use** | Detailed device name, model numbers, indications, user environment. | Device Master Record (DMR) excerpts, labeling mock‑ups. |
| **Predicate comparison** | Identification of legally marketed predicate(s); side‑by‑side table of technological characteristics. | 510(k) Summary of predicate (e.g., K#######). *No specific identifier found in source — verify separately.* |
| **Performance testing** | • Bench functional & safety tests (electrical, mechanical, software verification as applicable). <br>• Biocompatibility (ISO 10993‑1). <br>• Sterility validation (if sterile). | Test reports, ASTM/ISO method citations. |
| **Risk management** | ISO 14971 risk analysis file; identified hazards, severity, mitigations, residual risk assessment. | Risk Management Report (RMR). |
| **Labeling & IFU** | Full label artwork, Instructions for Use, symbol legend, warnings/precautions. | Final labeling packet per 21 CFR 801. |
| **Software documentation** *(if applicable)* | Software Development Lifecycle (SDLC) summary, verification & validation protocols, cybersecurity plan (per FDA guidance). | SRS, SVR, cybersecurity threat analysis. |
| **Clinical data** *(only if required to bridge a substantial difference)* | Limited clinical investigation or retrospective chart review. | IRB approval, study report. |
| **Quality System evidence** | ISO 13485‑aligned QMS compliance (post‑Feb 2026 QMSR). | QMS audit reports, certificates of conformance. |

---

### 3. Gaps Identified from Source (“must” items unmet)

The internal readiness script flagged a **510(k) RTA score of 52 %** and noted **five “must” items remain unsatisfied**, which would lead to an immediate Refuse‑to‑Accept if submitted.

| Likely “must” categories (common FDA criteria) | Evidence currently missing *per source* |
|-------------------------------------------------|------------------------------------------|
| 1. **Complete predicate comparison table** | Not supplied. |
| 2. **Comprehensive risk management file (ISO 14971)** | Not supplied. |
| 3. **Full labeling & IFU package** | Not supplied. |
| 4. **Biocompatibility / safety testing data** | Not supplied. |
| 5. **Software validation or cybersecurity plan** (if device includes software) | Not supplied. |

*The source does not enumerate the items; the above reflects typical “musts” that cause RTA.*  

**Action:** Perform a focused gap analysis against these five areas and collect the missing data before re‑running the readiness assessment.

---

### 4. Risk Controls & Mitigation Plan

| Hazard | Control (Design/Process) | Verification |
|--------|--------------------------|--------------|
| Electrical shock (if electronic) | IEC 60601‑1 compliance, insulation testing. | Bench test report. |
| Mechanical failure (breakage, leakage) | Materials selection, finite‑element analysis, durability cycling. | FEA results & cyclic test data. |
| Software malfunction / cybersecurity breach | Secure coding practices, vulnerability scanning, regular patching. | Software verification report + cybersecurity threat model. |
| User error due to labeling ambiguity | Human Factors engineering, clear UI symbols, user testing. | Usability study findings. |

All controls must be documented in the risk management file and linked to design inputs/outputs per QMSR (21 CFR 820.30).

---

### 5. Citation of Source Material

| Excerpt | Relevance |
|---------|-----------|
| **Chunk ID: 322119354378516559** – “FDA 510(k) RTA 점수 52% 고착 … 5개 must 항목이 미충족 상태로 실제 제출 시 FDA RTA(Refuse to Accept) 직행.” | Confirms low readiness score and existence of five unmet mandatory items. |
| **Chunk ID: 607901765257522135** – “FDA 510(k) 점수 52% → 약 85% (5개 must 해소 시)” | Indicates potential score improvement to ~85 % once the five must items are addressed. |

No specific predicate or case identifiers appear in the source; verification of exact predicate numbers should be performed independently.

---

### 6. Human‑Escalation Triggers

| Trigger | Escalation Action |
|---------|-------------------|
| **Readiness score < 70 %** after gap closure attempt. | Alert RA leadership; consider early FDA pre‑submission meeting (Q‑sub). |
| **Any “must” item still missing** after final internal review. | Stop submission; reassign resources to complete the deficiency. |
| **Negative feedback from FDA during Q‑sub or pre‑meeting** indicating insufficient safety data. | Convene cross‑functional risk/clinical team for corrective plan. |
| **QMSR non‑conformance identified** (e.g., ISO 13485 audit failure). | Pause submission; remediate QMS gaps before filing. |
| **Regulatory timeline pressure exceeding 90 days** without completeness. | Elevate to project sponsor for resource reallocation. |

---

### 7. Reusable RA Judgment (Lesson Learned)

> *A 510(k) readiness score below the ~70 % threshold typically signals one or more critical “must” items are missing, which will trigger an FDA Refuse‑to‑Accept. Systematically map the five mandatory criteria (predicate comparison, risk management, labeling, safety testing, and software validation) early in the development cycle; address any gaps before re‑running automated readiness tools. Achieving at least an 85 % score after closure of these items is a strong indicator that the submission package will meet FDA acceptance standards.*  

---

### 8. Peer Review Prompt

> **Request to RA Peer:**  
> Please review this draft and challenge:  
> 1. The assumption that the five unmet “must” items correspond to the typical categories listed—are there other mandatory elements we may have overlooked given the device’s technology?  
> 2. The completeness of the evidence checklist relative to the projected classification; does any additional data (e.g., pediatric use, combination product considerations) need inclusion?  
> 3. Jurisdiction‑specific gaps, especially pertaining to the new QMS Regulation effective Feb 2026—are our QMSR references sufficient?  

Your feedback will be incorporated before finalizing the submission plan.

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

1. Chunk `322119354378516559`

> ## 배경 `build_readiness.py` 결과 FDA 510(k) RTA 점수 52% 고착. 하기 5개 must 항목이 미충족 상태로 실제 제출 시 FDA RTA(Refuse to Accept) 직행.

2. Chunk `607901765257522135`

> ## 예상 효과 FDA 510(k) 점수 52% → 약 85% (5개 must 해소 시)

### kb-eval-20260718-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_us-005", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "e8f2c4c3cdba0dcd", "source": "github:holee9/MD-process/issue-drafts/931_RA_FDA_Form_표지_양식_4건_작성.md", "source_hash": "68cd74d39caaa060d4323f37a5c193a02284866bee050ec5139fdf5916ca6ff7"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `e8f2c4c3cdba0dcd`
- Source: `github:holee9/MD-process/issue-drafts/931_RA_FDA_Form_표지_양식_4건_작성.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/931_RA_FDA_Form_%ED%91%9C%EC%A7%80_%EC%96%91%EC%8B%9D_4%EA%B1%B4_%EC%9E%91%EC%84%B1.md)
- Source hash: `68cd74d39caaa060d4323f37a5c193a02284866bee050ec5139fdf5916ca6ff7`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `931_RA_FDA_Form_표지_양식_4건_작성.md`는 `931_RA_FDA_Form_표지_양식_4건_작성.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 목표 영향 - 다음 분기(2026-Q3) `build_readiness.py` 재실행 시 FDA RTA Section A 5건 모두 충족 → **점수 0% → 33%** 예상. ## 작업 범위 (Done 정의) - [ ] FDA Form 3514 — 510(k) Cover Sheet 양식 (회사명/주소/연락처 자리표시자 포함) - [ ] FDA Form 3601 — User Fee Cover Sheet 양식 + 수수료 결제 영수증 자리표시자 - [ ] FDA Form 3654 — Standards Data Report 양식 또는 자사 별도 문서 양식 - [ ] FDA Form 3881 — Indications for Use S...
- 이 항목의 평가 포인트: 이 source는 510(k) predicate 자체를 선정하는 직접 근거가 아닐 수 있습니다. 좋은 답변은 predicate/IFU 동등성 판단을 단정하지 않고, 이 source가 제공하는 QMS·evidence·risk context로 제한해 사용해야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Submission Strategy**

---

### Bottom‑Line Recommendation
Prepare a standard **Traditional 510(k)** submission using the FDA‐specified forms listed in the work scope. The submission will be classified **Class II** (most non‑invasive medical devices of this type), but the exact classification must be confirmed by matching to a predicate device once the device’s intended use and technological characteristics are defined.

---

### 1. Submission Route & Classification
| Item | Status / Note |
|------|----------------|
| **Regulatory pathway** | Traditional 510(k) (Section A of FDA RTA). |
| **Device class** | Anticipated Class II (subject to predicate review). |
| **Required forms** | Form 3514, 3601, 3654, 3881, and a cover letter (see Section 2). |
| **QMS requirement** | Align with the new QMSR (effective Feb 2026) – ISO 13485‑based quality system must be in place. |

> *No specific predicate identifier is provided in the source material – verify the appropriate 510(k) reference number(s) against the device’s intended use before filing.*

---

### 2. Mandatory Documentation Checklist

| Form / Document | Content Requirement | Current Gap |
|-----------------|---------------------|--------------|
| **FDA Form 3514 – 510(k) Cover Sheet** | Company name, address, contact info (place‑holders). | Fill in actual entity data. |
| **FDA Form 3601 – User Fee Cover Sheet** | Completed fee payment receipt placeholder. | Obtain and attach proof of payment. |
| **FDA Form 3654 – Standards Data Report** | List all consensus standards applied or a separate document with the same content. | Confirm applicable recognized consensus standards; prepare the report. |
| **FDA Form 3881 – Indications for Use Statement** | Clear, concise statement; note OMB expiration 2026‑07‑31. | Draft IUS and ensure it is final before OMB deadline. |
| **Cover Letter (English)** | Applicant name, address, contact, submitter type. | Populate with accurate details. |
| **Related Docs Registration** (`13_규제평가_체크리스트/FDA_510k_RTA.md` – fields A1–A5) | Assign new document IDs for each supporting artifact. | Create and register doc‑ids. |

*All placeholders must be replaced with final, verified information before the next **build_readiness.py** run (target Q3 2026).*

---

### 3. Evidence Package Required for Substantial Equivalence

| Evidence Category | Typical Content | Notes |
|-------------------|-----------------|-------|
| **Device Description & Labeling** | Detailed design specs, schematics, photographs, labeling (including UDI). | Align with Class II labeling requirements (21 CFR 801). |
| **Intended Use & Indications for Use** | Complete IUS (Form 3881) – must be finalized before OMB expiration. | Ensure no claim expansion beyond predicate. |
| **Predicate Device Comparison** | Side‑by‑side table of technological characteristics, intended use, performance. | Identify a legally marketed device; if none exists, consider De Novo route. |
| **Performance Testing** | Bench (electrical safety, EMC), biocompatibility (ISO 10993), software validation (if applicable). | Follow recognized consensus standards referenced in Form 3654. |
| **Risk Management File** | ISO 14971 risk analysis, mitigation measures, residual risk evaluation. | Include FMEA/FMECA and verification of mitigations. |
| **Sterility / Shelf‑Life (if applicable)** | Sterilization validation, packaging integrity studies. | Only required for sterile devices. |
| **Clinical Data (if needed)** | Non‑clinical bench data usually sufficient for Class II; clinical data only if needed to bridge a gap. | Evaluate against predicate data. |

---

### 4. Risk Controls & Mitigations (ISO 14971)

1. **Hazard Identification** – Create hazard list (electrical, mechanical, software).  
2. **Risk Estimation** – Severity × Probability matrix.  
3. **Control Measures** – Design controls (e.g., fail‑safe circuitry), protective labeling, user training.  
4. **Verification of Controls** – Testing reports demonstrating compliance with control measures.  
5. **Residual Risk Evaluation** – Document acceptability; reference in the 510(k) narrative.

---

### 5. Citations from Source Material
- No specific predicate or FDA identifier appears in the provided excerpts — verify separately.  

(Excerpt references: Section A RTA goal [Chunk 202395958248735480]; required forms list [Chunk 608496877809508828].)

---

### 6. Human‑Escalation Triggers

| Trigger | Action Required |
|--------|-----------------|
| **Missing or placeholder data** in any of the mandatory FDA forms (3514, 3601, 3654, 3881) | Pause submission; senior RA to review and approve final entries. |
| **OMB expiration of Form 3881** (2026‑07‑31) approaching without a finalized IUS | Escalate to regulatory manager – risk of non‑compliance. |
| **User fee receipt not obtained** before submission window closes | Finance/RA liaison must secure payment and attach proof. |
| **QMSR compliance gap** (e.g., missing ISO 13485 procedures) | Quality assurance lead to remediate before filing. |
| **No suitable predicate identified after initial device definition** | Escalate to senior RA for De Novo feasibility assessment. |

---

### 7. Peer Review Prompt
> *@RA‑Colleague: Please review the assumptions above—particularly the inferred Class II classification and the completeness of the evidence matrix given we have no explicit predicate listed. Verify that all jurisdiction‑specific requirements (e.g., OMB deadline for Form 3881) are covered, and flag any gaps related to the new QMSR compliance or emerging guidance that may affect this submission.*

---

### 8. Reusable RA Judgment (Lesson Learned)

> **Judgment Record:** When a 510(k) work package lists only required FDA forms without providing predicate identifiers, default to preparing a traditional Class II submission draft while explicitly noting the need for separate predicate verification. Populate all placeholder fields with final data before any automated readiness check, and treat OMB form expiration dates as hard deadlines that trigger escalation if not met. Ensure QMSR alignment early (post‑Feb 2026) to avoid downstream compliance gaps.

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

1. Chunk `202395958248735480`

> ## 목표 영향 - 다음 분기(2026-Q3) `build_readiness.py` 재실행 시 FDA RTA Section A 5건 모두 충족 → **점수 0% → 33%** 예상.

2. Chunk `608496877809508828`

> ## 작업 범위 (Done 정의) - [ ] FDA Form 3514 — 510(k) Cover Sheet 양식 (회사명/주소/연락처 자리표시자 포함) - [ ] FDA Form 3601 — User Fee Cover Sheet 양식 + 수수료 결제 영수증 자리표시자 - [ ] FDA Form 3654 — Standards Data Report 양식 또는 자사 별도 문서 양식 - [ ] FDA Form 3881 — Indications for Use Statement 양식 (현행 OMB 만료일 2026-07-31 주의) - [ ] 510(k) Cover Letter 영문 표준 양식 (applicant name/address/contact/submitter type) - [ ] `13_규제평가_체크리스트/FDA_510k_RTA.md` 항목 A1~A5의 `related_docs:` 필드에 신규 doc-id 등록

## ra_eu

### kb-eval-20260718-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "034e73198875b07e", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `034e73198875b07e`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/README.md)
- Source hash: `30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules) ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – X‑ray Diagnostic Generator (Ionising Radiation Emitting Device) & Associated SaMD**

---

### 1. Scope of the draft
This document provides a concise regulatory assessment for an **active diagnostic device that emits ionising radiation (X‑ray generator)** and its **associated medical device software (SaMD)** intended to support image interpretation. The focus is on:

* MDR classification and conformity‑assessment route  
* Evidence required for technical documentation, clinical evaluation, PMS/PMCF & risk management  
* Identified gaps in the currently available information  
* Key risk‑control measures that must be demonstrated  
* Citation of the relevant MDR provisions used in the assessment  

---

### 2. Classification (MDR 2017/745)

| Device element | Applicable rule (Annex VIII) | Resulting class |
|----------------|------------------------------|-----------------|
| X‑ray generator – emits ionising radiation for diagnostic imaging | **Rule 10** – “Ionising radiation emitting diagnostic devices”【2†L1-L2】 | **Class IIb** |
| Associated software that provides information used for diagnosis (SaMD) | **Rule 11** – “Medical device software”【2†L1-L2】 | Class depends on impact of the decision:  
• If a diagnostic error could cause *serious deterioration* → **Class IIa** (default)  
• If error could lead to *surgical intervention* or *irreversible deterioration* → **Class IIb**  
• If error could cause death → **Class III** |
| Overall system (hardware + software) | Combination rule – the higher class prevails | **Class IIb** (driven by the X‑ray generator) |

> **Citation:** Classification rules are listed in Annex VIII of MDR; Rule 10 and Rule 11 are explicitly referenced in the source excerpt【2†L1-L2】.  

---

### 3. Conformity‑assessment route

| Device class | Mandatory MDR module (Annex) |
|--------------|-----------------------------|
| **Class IIb** (X‑ray generator & system) | **Annex IX** – Full quality‑management system + technical documentation assessment by a Notified Body (NB). The NB reviews the design dossier and issues an EC type‑examination certificate, after which the manufacturer draws up an EU Declaration of Conformity (DoC). |
| **Class IIa/IIb SaMD (if separate) | Same route (Annex IX) if placed on the market as a standalone device; otherwise covered under the system assessment.|

> **Citation:** Conformity‑assessment routes for classes IIa–III are defined in Annex IX of MDR.  

---

### 4. Required evidence package

| Evidence item | MDR reference | Typical contents / standards |
|---------------|--------------|-----------------------------|
| **Technical Documentation** (Annex II) | Annex II | Device description, specifications, intended purpose, labeling (Annex I §23), design & manufacturing processes, verification & validation data, risk‑management file (ISO 14971). |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | State‑of‑the‑art literature, clinical data on performance and safety, justification of equivalence (if any), benefit–risk analysis. |
| **Risk Management File** | Annex I (GSPR) & ISO 14971 | Hazard identification, risk estimation, evaluation of residual risk, risk‑control measures (e.g., interlocks, shielding). |
| **PMS Plan** | Art. 84 | Process for post‑market surveillance, data collection, reporting obligations. |
| **PMCF Plan / Report** (if required for SaMD) | Annex XIV Part B | Planned prospective clinical follow‑up to collect real‑world evidence on software performance. |
| **PSUR** (for Class IIb/III) | Art. 86 | Periodic Safety Update Report – summary of PMS data, trend analysis, corrective actions. |
| **GSPR Checklist** | Annex I (General Safety & Performance Requirements) | Confirmation that all 23 GSPRs are addressed; the source notes a “GSPR checklist‑based conformity assessment is mandatory”【2†L3-L4】. |
| **Standards compliance evidence** | Not mandated by MDR but strongly supported | IEC 60601‑2‑44 (X‑ray equipment safety), IEC 62267 (radiation dosimetry), IEC 62304 (software life‑cycle), IEC 60601‑1 (general safety). |

---

### 5. Gaps / Missing information (to be supplied before NB submission)

| Area | What is missing | Why it matters |
|------|----------------|---------------|
| **Intended purpose & indications** | Precise clinical indication(s), patient population, intended environment of use. | Required for rule application and CER scope. |
| **Device specifications** | X‑ray output parameters (kV, mA, filtration), dose metrics, beam geometry, shielding dimensions. | Needed to demonstrate compliance with IEC 60601‑2‑44 & radiation safety GSPRs. |
| **Software description** | Functional architecture, algorithms used for image analysis, intended decision impact (diagnostic vs. triage). | Determines Rule 11 class and drives PMCF requirements. |
| **Labeling & IFU** | Full labeling draft (symbols, warnings, instructions) per Annex I §23. | Mandatory for technical documentation & DoC. |
| **Clinical data** | Clinical investigation results or justified equivalence to a legally marketed device; summary of literature search strategy. | Core component of the CER. |
| **Risk‑control verification evidence** | Test reports for interlock function, dose monitoring, software validation logs. | Needed to close residual risk loops in the risk‑management file. |
| **PMS/PMCF implementation details** | Defined data sources, frequency of review, responsible persons, trigger thresholds. | Required by Art. 84/85 (PMS) and Annex XIV Part B (PMCF). |

> **Action:** Each gap should be addressed with documented evidence before the NB audit; otherwise the submission will be rejected or returned for clarification.

---

### 6. Key risk‑control measures to demonstrate

1. **Radiation protection**  
   * Interlock circuitry that disables emission if shielding is open.  
   * Real‑time dose monitoring with automatic shutdown at pre‑defined thresholds.  
   * Compliance with IEC 60601‑2‑44 (leakage, scatter, beam quality).  

2. **Software safety**  
   * Verification & validation per IEC 62304 – unit, integration, system testing.  
   * Hazard analysis focusing on erroneous diagnostic output; implementation of fail‑safe modes.  

3. **Electrical safety / EMC**  
   * IEC 60601‑1 compliance (protective earth, leakage currents).  
   * IEC 61000‑4‑2/‑4 & ‑6 testing for immunity to electromagnetic disturbances.

4. **Usability & human factors**  
   * Risk analysis of user interface (e.g., accidental exposure due to incorrect parameter entry).  
   * Formative usability testing with representative users; inclusion in the risk‑management file.

5. **Manufacturing controls**  
   * Process validation for critical steps (e.g., cathode assembly, shielding deposition).  
   * Supplier qualification for high‑voltage components.

---

### 7. Human‑escalation triggers (when to involve senior RA/Legal)

| Trigger | Reason |
|--------|--------|
| Any **classification uncertainty** (especially SaMD impact) | Mis‑classifying could lead to an incorrect conformity route. |
| Absence of **clinical data** supporting safety/effectiveness for the intended indication | Must decide whether a clinical investigation is required. |
| Incomplete **PMS/PMCF plan** or inability to meet Art. 84 timelines | NB will reject the dossier without a robust post‑market system. |
| **GSPR gaps** identified during checklist review (e.g., missing §23 labeling) | Must be resolved before DoC signing. |
| Detection of **non‑conformity with essential safety standards** (IEC 60601‑2‑44, IEC 62304) | Requires design remediation; possible impact on market launch date. |

Escalate to the **RA Lead / Regulatory Affairs Manager** for any of the above items before proceeding to NB submission.

---

### 8. Peer‑review request

> **To:** [Regulatory Affairs Colleague]  
> **Subject:** Review of classification & evidence package for X‑ray diagnostic generator + SaMD (MDR)  
>   
> Please challenge the following assumptions and identify any jurisdictional gaps:  
> 1. Application of Rule 10 (Class IIb) – does the device’s intended use (e.g., interventional vs. conventional radiography) affect the class?  
> 2. Classification of the associated software under Rule 11 – is there sufficient information to justify Class IIa versus a higher class?  
> 3. Sufficiency of the outlined evidence list for an Annex IX assessment – are any mandatory standards or test reports missing?  
> 4. Alignment with the latest transition provisions (Regulation EU 2023/607) – do any extended timelines impact our submission schedule?  

Your feedback will be incorporated before finalizing the technical dossier.

---

### 9. Reusable RA Judgment (recorded for future cases)

**Judgment ID:** MDR‑Xray‑2026‑07‑17  
- **Device type:** Active diagnostic X‑ray generator (ionising radiation) + SaMD.  
- **Classification:** Rule 10 → Class IIb; software under Rule 11 (default IIa, re‑evaluate impact).  
- **Conformity route:** Annex IX (full QMS & technical documentation assessment).  
- **Key evidence required:** Technical docs (Annex II), CER (Annex XIV A), GSPR checklist, PMS/PMCF plan, PSUR, risk‑management file, compliance with IEC 60601‑2‑44 and IEC 62304.  
- **Common gaps:** Intended use statement, detailed radiation specifications, software functional description, clinical data justification, labeling draft, verification of interlocks & dose monitoring.  
- **Escalation points:** Classification uncertainty, missing clinical evidence, incomplete PMS/PMCF, GSPR deficiencies, non‑conformity with essential safety standards.  

*Use this judgment as a template when assessing any ionising‑radiation diagnostic device (X‑ray, CT, fluoroscopy) and its associated software under MDR.*

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

### kb-eval-20260718-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "370448965c57604a", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `370448965c57604a`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week04_MDR_EU_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `Week04_MDR_EU_체계_상세.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUF...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Route**

---

### 1 Scope & Device Synopsis  
| Item | Status / Comment |
|------|-------------------|
| **Device name / model** | *Not supplied* – must be provided before any classification can be finalised. |
| **Intended purpose (indications, target population, mode of action)** | *Missing* – essential to identify the applicable rule in Annex VIII (see §2). |
| **Manufacturer & place of residence** | Required for Article 51 self‑classification responsibility (source [2]). |
| **Regulated market(s)** | EU (MDR 2017/745) – primary focus. |

> **Action:** Obtain a complete “Device Description” and the Intended Use Statement from the product team before proceeding.

---

### 2 Classification Procedure (Article 51 + Annex VIII)  
1. **Self‑classification responsibility** – The manufacturer must apply the 22 classification rules sequentially, adopting the highest applicable class (source [2]).  
2. **Rule identification** – Without a clear intended use we cannot yet map the device to a specific rule (e.g., Rule 9, 10, 11, 17).  
3. **Borderline cases** – If uncertainty remains after applying all rules, consult the Competent Authority (CA) or the MDCG “Manual on Borderline and Classification” (latest 2023‑09 v2.1.1) (source [2]).  

> **Human‑escalation trigger:** *Any ambiguity after rule application* → raise to senior classification specialist for MDCG/manual review.

---

### 3 Resulting Class & Conformity‑Assessment Route  

| Anticipated Class | Typical MDR Annex route | Required Notified Body (NB) involvement |
|-------------------|------------------------|------------------------------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration (Annex IX – QMS assessment optional) | No NB required for the technical file; only QMS (ISO 13485) may be audited voluntarily. |
| **Class Is / Im** | Annex IX (QMS + device documentation audit) | NB mandatory for conformity assessment of the technical documentation. |
| **Class IIa** | Annex IX (full QMS & technical file review) **or** Annex X (type‑examination) depending on risk‑based decision | NB required. |
| **Class IIb / III** | Annex IX (full assessment) **or** Annex XI (production conformity verification) after type‑examination (Annex X) | NB required; for Class III a full design dossier review is mandatory. |

> **Note:** The exact route will be fixed once the class is confirmed.

---

### 4 Technical Documentation – Core Items (Annex II)  

| Section | Evidence Required |
|---------|-------------------|
| Device description & specifications | Detailed drawings, bill of materials, software architecture (if applicable). |
| Intended purpose & labeling (Annex I‑§23) | Label copies, IFU, warnings. |
| Risk Management File (ISO 14971) | Hazard analysis, risk evaluation, risk control measures, residual risk assessment. |
> **Citation:** General Safety & Performance Requirements – Annex I; implementation via ISO 14971 (standard reference).  

---

### 5 Clinical Evidence (Annex XIV Part A)  

| Requirement | What must be produced |
|-------------|-----------------------|
| Clinical Evaluation Plan (CEP) | Scope, methodology, data sources. |
| Clinical Evaluation Report (CER) – **Art 61** (source [1]) | State‑of‑the‑art literature review, clinical benefit analysis, justification of equivalence (if applicable). |
| Post‑Market Clinical Follow‑up (PMCF) plan – Annex XIV Part B | Ongoing safety & performance data collection. |

> **Citation:** “CEP + CER (Article 61, MDR Annex XIV)” (source [1]).

*No specific predicate device identifier or 510(k) reference appears in the source – verify separately.*

---

### 6 Post‑Market Surveillance (PMS)  

| Component | Regulatory Basis |
|-----------|------------------|
| PMS System | Art 83 MDR (continuous monitoring). |
| PMS Plan | Art 84 MDR (documented plan). |
| Periodic Safety Update Report (PSUR) – for Class IIa/IIb/III | Art 86 MDR. |
| Vigilance / Serious Incident Reporting (including PSUR) | Art 87 MDR; also aligns with “MDR 21 CFR 803 + MedWatch” noted in source [1]. |

> **Citation:** “Vigilance (MDR Art.87), PSUR” (source [1]).

---

### 7 Unique Device Identification (UDI)  

| Action | Source |
|--------|--------|
| Register UDI on national portal (Korean UDI portal) & GUDID (US) | source [1]. |
| Upload UDI data to EUDAMED – DEV module | source [1]. |

> **Citation:** “UDI portal (udiportal.mfds.go.kr), GUDID, EUDAMED UDI/DEV” (source [1]).

---

### 8 Authorized Representative & Importer  

| Requirement | Reference |
|-------------|-----------|
| Appoint EU Authorized Representative (Art 11 MDR) – required for non‑EU manufacturers. | source [1]. |
| Identify domestic importer / local import licence holder (Korean “수입자”). | source [1]. |
| US Agent considerations (only if 510(k) exemption applies). | source [1]. |

> **Citation:** “Authorized Rep. … Art.11” (source [1]).

---

### 9 Fees & Contractual Aspects  

| Cost Item | Approximate Range (from source) |
|-----------|---------------------------------|
| Notified Body contract – review of technical file (class‑dependent) | €10,000 – €100,000+ |
| US FDA MDUFA IV user fees (FY 2026) – if 510(k) applicable | $27,720 – $440,867 |

> **Citation:** “NB 계약 기반 (€10,000~€100,000+)”, “MDUFA IV 수수료 (FY2026: $27,720~$440,867)” (source [1]).

---

### 10 Risk Controls & Mitigation  

| Hazard Category | Control Measure (to be documented) |
|-----------------|--------------------------------------|
| Biological / Chemical | Sterilisation validation, biocompatibility testing per ISO 10993. |
| Electrical / Radiation (if active) | IEC 60601‑1 (safety), IEC 60601‑2‑xx (performance), compliance with relevant Annex VIII rule (e.g., Rule 9/10). |
| Software (if applicable) | IEC 62304 lifecycle, cybersecurity per IEC 62443; risk control via secure coding and update procedures. |
| Usability / Human factors | IEC 62366 usability engineering file. |

> **Citation:** Risk management obligations are anchored in Annex I (General Safety & Performance Requirements) and must be executed through ISO 14971.

---

### 11 Missing Information – Gap Analysis  

| Gap | Why it matters | Immediate Action |
|-----|----------------|------------------|
| **Device description & intended use** | Determines the applicable Annex VIII rule (classification). | Request a concise Intended Use Statement and technical specs from R&D. |
| **Clinical data sources** | Needed for CEP/CER (Art 61, Annex XIV). | Identify any existing clinical investigations, literature, or equivalent devices. |
| **Software classification details (if any)** | Affects Rule 11 & class; may trigger higher‑class assessment. | Clarify software functions and decision impact. |
| **Risk Management File** | Mandatory for all classes; supports PMS & vigilance. | Initiate ISO 14971 risk analysis as early as possible. |
| **UDI allocation strategy** | Required before market entry (EUDAMED). | Assign GTIN/DI, generate UDI‑DR and upload to national portal. |
| **Authorized Representative / Importer contracts** | Legal prerequisite for CE marking. | Confirm appointment of EU AR and local importer. |

---

### 12 Human‑Escalation Triggers  

1. **Unclear classification after rule application** – route to senior regulatory lead (MDCG manual consultation).  
2. **Absence of any clinical evidence** – halt dossier preparation until at least a minimal CEP is drafted.  
3. **Risk analysis shows residual risk > acceptable** – require design mitigation before proceeding.  
4. **Pending NB contract negotiation exceeding budget ceiling** – flag to finance & project management.  
5. **Regulatory deadline approaching without complete documentation** – trigger senior manager notification.

---

### 13 Peer‑Review Request  

> **To:** Regulatory Affairs Team (MDR specialist)  
> **Please review:**  
> • Assumptions made regarding the classification pathway given the lack of device specifics.  
> • Completeness of source coverage—are there any MDR articles or annexes not captured that could affect our evidence requirements?  
> • Jurisdictional gaps – e.g., interaction with US FDA (510(k) exemption mention) and Korean UDI obligations.  

**Suggested actions:** Provide feedback on the classification rule selection process, confirm that all mandatory Annex XIV parts are addressed, and highlight any additional national requirements not covered by the current draft.

--- 

*Prepared by: Theo – EU MDR Regulatory Affairs Specialist*  
*(All citations refer to source excerpts [1] and [2]; no specific predicate identifiers were present in the source material.)*

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

### kb-eval-20260718-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "0604d767d6dcfc80", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `0604d767d6dcfc80`
- Source: `github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X%EC%84%A0_%EB%B6%84%EB%A5%98_%EC%82%AC%EC%8B%A4%EC%98%A4%EB%A5%98.md)
- Source hash: `8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Rule 9 (Chapter III §6.1) — 오적용 반증 > "All active **therapeutic** devices intended to administer or exchange energy are classified as class IIa ... **All active devices intended to emit ionizing radiation for therapeutic purposes** ... are classified as class IIb." (진단용 X-ray에는 부적용) ### D1 — §6 표 0-2 예시 열 - **기재값 (예시 열):** > "X-ray: MFDS 3등급, FDA Class...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Diagnostic X‑ray Imaging System (Active Device emitting ionising radiation)**  

---

### 1. Device Overview  
| Item | Description |
|------|-------------|
| **Intended purpose** | Generation of diagnostic X‑ray images for clinical examination of patients. |
| **Device family** | Active medical device that emits ionising radiation for *diagnostic* use (not therapeutic). |
| **Major subsystems** | 1) X‑ray generator (radiation source) – active emitter<br>2) Digital flat‑panel detector (image recorder)<br>3) Image‑processing / display software (decision‑support) |

---

### 2. Classification & Conformity Assessment Route  

| Subsystem | MDR rule applied* | Resulting class | Required conformity route |
|-----------|-------------------|-----------------|--------------------------|
| X‑ray generator (radiation source) | **Rule 10** – “Active devices that emit ionising radiation for diagnostic purposes” (Annex VIII, Rule 10) | **Class IIb** | **Annex IX** – full quality‑management system + technical documentation assessment by a Notified Body |
| Digital detector (image recorder) | **Rule 17** – “Devices intended for recording diagnostic images generated by X‑ray radiation” (Annex VIII, Rule 17) | **Class IIa** | **Annex IX** (or Annex X if a type‑examination is chosen; most manufacturers use Annex IX) |
| Image‑processing / decision software | **Rule 11** – “Software providing information for diagnostic decisions” (Annex VIII, Rule 11) – likely Class IIa (upgrade to IIb/III only if it can cause serious deterioration or death). | **Class IIa** | **Annex IX** |

\*The classification rationale is taken from the source excerpt that clarifies the mis‑application of “Rule 5/9” and correctly assigns **Rule 10 → Class IIb** for the X‑ray system (source [2]). The same source also confirms Rule 17 for the detector and Rule 9 being limited to therapeutic radiation (source [1]).

**Resulting MDR pathway:**  
- Primary device (X‑ray generator) – **Annex IX** (full NB assessment, technical file & QMS).  
- Ancillary devices (detector, software) – **Annex IX** (or Annex X where a type‑examination is preferred).  

---

### 3. Required Evidence Package  

| Evidence | MDR reference | Typical content |
|----------|--------------|----------------|
| **Technical Documentation** (design dossier) | Annex II (and Annex III for PMS) | Device description, specifications, labeling, GSPR mapping, risk management file, verification & validation reports, harmonised standards conformity (e.g., IEC 60601‑2‑44, EN ISO 14971). |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | State‑of‑the‑art literature review for diagnostic X‑ray imaging, clinical performance data (pre‑market or literature), justification of safety & performance, benefit–risk analysis. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | Description of routine PMS activities, data collection, reporting responsibilities. |
| **Periodic Safety Update Report (PSUR)** – for Class IIb device | Art. 86 | Summary of PMS data, trend analyses, risk‑benefit updates (intervals per MDCG guidance). |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B (for Class IIb / high‑risk) | Planned prospective clinical data collection, methodology, outcomes, and final evaluation. |
| **Risk Management File** | Annex I (GSPR) – implemented via ISO 14971 | Hazard identification, risk analysis, control measures, residual risk evaluation, verification of controls. |
| **Labeling & IFU** | Annex I Chapter III §23 | Instructions for use, safety information, dose limits, contraindications, user training requirements. |
| **EUDAMED Registration** | Art. 33‑39 | Device identifier (UDI‑DI), manufacturer details, classification, conformity assessment route, certificates. |
| **Declaration of Conformity** | Annex IV | Signed by manufacturer, references to applicable standards and the NB certificate. |

---

### 4. Identified Missing Information (Gaps)  

| Gap | Why it matters | Action needed |
|-----|----------------|--------------|
| **Exact intended use statement** – anatomical region(s), patient population, clinical indications | Determines scope of clinical evaluation & labeling; affects risk assessment. | Provide a clear Intended Use clause in the Technical Documentation. |
| **Radiation dose specifications (kV, mA, exposure time, Dose‑Area Product limits)** | Required for compliance with IEC 60601‑2‑44 and to demonstrate adherence to dose‑optimization principles (GSPR). | Include measured dosimetry data & dose‑management controls in the risk file. |
| **Software functionality description** – level of diagnostic decision support, algorithms used | Influences classification under Rule 11 and required validation. | Submit software verification/validation plan and traceability matrix. |
| **List of applicable harmonised standards** (e.g., EN 60601‑2‑44, EN ISO 14971, EN 62304) | Needed to demonstrate conformity with GSPR; impacts the Technical Documentation. | Compile a Standards Mapping Table. |
| **Clinical data source** – pre‑market trial results or literature search strategy | CER must be “up‑to‑date” and sufficiently robust for Class IIb devices. | Conduct systematic literature review; if insufficient, plan a small clinical investigation or PMCF. |
> No specific identifier (e.g., 510(k) number, MDR device UDI) appears in the source excerpts — verify separately.

---

### 5. Key Risk Controls (derived from risk management & GSPR)

1. **Radiation safety interlocks** – automatic shutdown if exposure exceeds predefined limits.
2. **Dose‑monitoring software** – real‑time display of cumulative dose, alerts for over‑exposure.
3. **Mechanical shielding** – leaded housing around the X‑ray tube to limit scatter.
4. **User authentication & training** – only qualified operators can activate emission mode.
5. **Software validation & cybersecurity** – verification of image processing algorithms; patch management per IEC 62304.
6. **Usability testing** – ensure correct set‑up and operation, reduce use errors (Annex I GSPR 1).
7. **Periodic performance checks** – scheduled output stability tests, detector calibration.

All controls must be documented in the Risk Management File (ISO 14971) and verified against the relevant GSPR clauses in Annex I.

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation to |
|---------|----------------|
| **Unresolved classification dispute** (e.g., evidence that device could be therapeutic) | Senior Regulatory Lead & Notified Body liaison |
| **Missing clinical data for Class IIb CER** | Clinical Affairs manager – initiate PMCF or investigational study |
| **Inadequate radiation safety documentation** | Radiation protection specialist – perform additional bench testing |
| **Non‑conformance to harmonised standards** | Quality Management System (QMS) auditor – revise design/validation plan |
| **EUDAMED registration fields incomplete** | Regulatory Operations team – pause CE marking submission until resolved |
| **Residual risk unacceptable after controls** | Head of Risk Management – consider redesign or scope reduction |

---

### 7. Peer‑Review Request  

> **To:** [RA colleague name]  
> **Subject:** Peer review of classification & evidence plan for diagnostic X‑ray system (Rule 10, Class IIb)  
> **Please evaluate:**  
> 1. The adequacy of the classification justification (Rule 10 vs. Rule 5/9). Are any therapeutic functions or invasive aspects overlooked that could shift the class?  
> 2. Whether the listed evidence items fully satisfy MDR Annex IX and Annex XIV requirements for a Class IIb device.  
> 3. Potential jurisdictional gaps – e.g., alignment with Korean MFDS (3‑grade) and US FDA (510(k) MQB) references in the source, and any impact on EU CE‑marking documentation.  

*Your feedback will be incorporated before final submission to the Notified Body.*

---

### 8. Reusable RA Judgment (Lesson Learned)

> **When a source maps an X‑ray diagnostic system to “EU MDR Rule 5/9” it is likely a mis‑classification. Follow the MDR Annex VIII rule table: diagnostic radiation emitters fall under **Rule 10 → Class IIb**; recording devices belong to **Rule 17 → Class IIa**. Correct classification determines the appropriate conformity assessment route (Annex IX for IIb) and prevents downstream errors in technical documentation, PSUR frequency, and NB certification scope.**  

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

1. Chunk `109229213193581391`

> ### Rule 9 (Chapter III §6.1) — 오적용 반증 > "All active **therapeutic** devices intended to administer or exchange energy are classified as class IIa ... **All active devices intended to emit ionizing radiation for therapeutic purposes** ... are classified as class IIb." (진단용 X-ray에는 부적용)

2. Chunk `109346595768604468`

> ### D1 — §6 표 0-2 예시 열 - **기재값 (예시 열):** > "X-ray: MFDS 3등급, FDA Class II 510(k), **EU MDR Rule 5/9**" - **독립확인 정답:** - X-ray 시스템(진단용 이온화방사선 능동기기) = **Rule 10 → Class IIb** - 디지털 평판 디텍터(X-ray 영상 기록기기) = **Rule 17 → Class IIa** - Rule 9 = **치료용** 이온화방사선/에너지 투여 기기(진단용 X-ray 배제) - Rule 5 = 체강 대상 침습기기(X-ray 배제) - **영향:** - 규제 분류 오적용 시 EU MDR 적합성 평가 절차(Annex IX/X/XI) 선정 오류로 연결(Notified Body 인증 경로·기술문서 요구·PSUR 주기 오판정). - "MFDS 3등급 = FDA Class II = EU MDR Rule 5/9" 정합 매핑이 후속 문서(GSPR 매핑표·기술문서·CE marking plan)로 전파될 위험. - **권고수정:** - 예시 열을 다음으로 변경: > "X-ray 시스템: MFDS 3등급, FDA Class II (510(k), Product Code MQB), **EU MDR Rule 10 → Class IIb**; 평판 디텍...

### kb-eval-20260718-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6b46b0ff30afb7f7", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `6b46b0ff30afb7f7`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md)
- Source hash: `d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexII_Technical_Documentation_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMS...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – EU MDR 2017/745 (Technical Documentation & Conformity Assessment)**  

---

### 1. Scope & Reference Materials
| Item | Source |
|------|--------|
| Legal basis | **EU MDR 2017/745**, Annex II (Technical Documentation) – see source excerpt [2] |
| Supporting annexes | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS‑TD) – referenced in excerpt [2] |
| Cross‑reference to other jurisdictions (for internal benchmarking) | FDA Design History File (21 CFR 820) and MFDS technical file – see matrix in excerpt [1] |

*All citations refer directly to the source excerpts; no predicate or registration numbers are present in the provided material.*  

---

### 2. Preliminary Device Information (to be supplied by the manufacturer)

| Required Item | Why it is needed (MDR clause) | Current status |
|---------------|------------------------------|----------------|
| **Device name & model(s)** | Annex II §1 – “Device Description” | *Missing* |
| **Intended purpose / indication for use** | Annex II §1; also the basis for classification under Annex VIII (Rules 1‑22) | *Missing* |
| **Operating principle & technology description** | Annex II §1; needed to map to active/passive rules (e.g., Rule 9‑11, Rule 17) | *Missing* |
| **Label & Instructions for Use (IFU)** | Annex II §2 – “Labeling” (see mapping in excerpt [1]) | *Missing* |
| **Manufacturer & authorized representative details** | Annex IV (Declaration of Conformity) and Annex II §1 | *Missing* |
| **Device architecture & Bill‑of‑Materials** | Annex II §3 – “Design & Manufacturing” (see excerpt [1]) | *Missing* |
| **Software component description (if applicable)** | Relevant for Rule 11 classification; must be documented in risk file & V&V | *Missing* |

> **Action:** Request the above items from the product development team before any classification work can begin.

---

### 3. Classification Determination (Annex VIII)

1. **Map intended purpose and technology to a rule** (e.g., Rule 9, 10, 11 or 17 for active devices).  
2. **Apply the decision tree** to arrive at Class I, IIa, IIb, or III.  
3. **Document the justification** in the “Classification” section of the technical file (Annex II §1).

> **Missing Information:** The intended use and device technology are not yet available → classification cannot be finalised.

---

### 4. Conformity‑Assessment Route (Annex IX / X / XI)

| Device class | Likely route (subject to NB confirmation) |
|--------------|--------------------------------------------|
| Class I (non‑sterile, non‑measuring) | Self‑declaration (Annex IV); no NB involvement. |
| Class I (sterile or measuring) | **Annex IX** – QMS assessment + technical documentation review by NB. |
| Class IIa/IIb/III | **Annex IX** – full quality‑management system audit + technical file assessment *or* **Annex X** (type‑examination) where a type‑examiner is required for certain high‑risk devices. |

> **Human‑Escalation Trigger:** If the classification outcome lands in Class IIb or III, project lead must engage an EU NB within 5 working days to confirm the appropriate route and timeframe.

---

### 5. Required Evidence & Documentation (per Annex II)

| Section (Annex II) | Deliverable | MDR citation | Current status |
|--------------------|-------------|--------------|----------------|
| **§1 Device Description** | Detailed device description, intended purpose, principal design, variants. | Annex II §1 | *Missing* |
| **§2 Labeling & IFU** | Complete label artwork, symbols, safety information, user manual (language per market). | Annex II §2; see mapping to FDA 21 CFR 801 and MFDS “표시기재”. | *Missing* |
| **§3 Design & Manufacturing** | Design History File (DHF) – design outputs, specifications, manufacturing processes, materials. | Annex II §3; cross‑referenced in excerpt [1] (“Design History File”) | *Partial – manufacturer indicated existence of DHF but not supplied.* |
| **§4 GSPR Checklist** | Completed General Safety & Performance Requirements checklist with evidence (e.g., performance testing, 510(k) comparison). | Annex II §4; see “GSPR Checklist” in excerpt [1] | *Missing* |
| **§5 Risk Management** | ISO 14971‑complaint risk management file (risk analysis, evaluation, control measures, residual risk summary). | Annex II §5; also noted as “Risk Management File”. | *Missing* |
| **§6 Verification & Validation (V&V)** | V&V plan and reports, software validation (if applicable), bench/animal testing data. | Annex II §6; referenced in excerpt [1] (“Verification & Validation”) | *Missing* |
| **Annex I – GSPR** | Evidence that all 21 General Safety & Performance Requirements are met (clinical data, performance test reports). | Annex I | *Missing* |
| **Annex XIV – Clinical Evaluation Report (CER)** | Up‑to‑date CER (Annex XIV Part A) with state‑of‑the‑art literature review and clinical data. | Annex XIV Part A; see source note on “Clinical Evaluation”. | *Missing* |
| **Annex XV – Clinical Investigation** *(if required)* | Clinical investigation plan & final report (for devices lacking sufficient clinical data). | Annex XV | *To be determined* |
| **Annex III – PMS Technical Documentation** | Post‑Market Surveillance (PMS) Plan (Art. 84), PMS Report (Art. 85/86) and PMS System description. | Annex III; see source note on “PMS TD”. | *Missing* |

> **Key Gap:** No clinical evidence, risk analysis, or verification data have been provided at this stage.

---

### 6. Risk Controls & Mitigation (ISO 14971 linkage)

| Hazard Category | Example Control(s) | Evidence Required |
|-----------------|-------------------|-------------------|
| **Electrical safety** | IEC 60601‑1 compliance, insulation testing. | Test reports, design verification. |
| **Software safety** (if applicable) | IEC 62304 processes, failure mode & effect analysis (FMEA). | Software V&V report, risk control mapping to software functions. |
| **Biocompatibility** | ISO 10993‑1 assessment of materials in contact with the body. | Test certificates, material data sheets. |
| **Usability / Human factors** | IEC 62366 usability engineering process; IEC 60601‑1‑6 risk control for user error. | Usability study results, identified use errors & mitigations. |
| **Sterility (if sterile)** | Validation of sterilisation process, ISO 11137 (radiation) or ISO 17665 (steam). | Sterilisation validation report, packaging integrity test. |

> **Action:** Populate the risk management file with a complete hazard analysis and link each residual risk to an implemented control; cross‑reference controls in the GSPR checklist.

---

### 7. Human‑Escalation Triggers & Decision Points

| Trigger | Who must be notified | Deadline / Action |
|---------|----------------------|-------------------|
| **Insufficient device description / intended use** (pre‑classification) | Project Lead & Regulatory Manager | Within 2 working days – request missing data. |
| **Classification results in Class IIb/III** | Head of Regulatory Affairs & appointed EU NB contact | Initiate NB engagement plan within 5 working days. |
| **Absence of clinical evidence for a high‑risk device** (Class IIb/III) | Clinical Evaluation Lead | Escalate to senior management; consider clinical investigation per Annex XV. |
| **Risk file fails ISO 14971 completeness check** | Risk Management Owner | Immediate corrective action; update risk control plan before NB audit. |
| **PMS Plan not aligned with device class** | Post‑Market Surveillance Coordinator | Review and align within 10 working days of classification finalisation. |

---

### 8. Summary of Missing Information (to be obtained)

1. Complete **device description**, intended purpose, and operating principle.  
2. Detailed **Bill‑of‑Materials & manufacturing process** documentation.  
3. **Labeling/IFU** content in the required language(s).  
4. **Risk Management File** (ISO 14971) with hazard analysis.  
5. **Verification & Validation reports**, including software validation if applicable.  
6. **Clinical evidence** (clinical evaluation data, literature review, or clinical investigation plan).  
7. **Post‑Market Surveillance (PMS) Plan** appropriate to the final class.

> Until these items are supplied, a definitive classification and conformity‑assessment pathway cannot be finalized.

---

### 9. Peer Review Prompt  

*Please review the above draft and challenge the following aspects:*

- **Assumptions on classification route:** Are there any device categories (e.g., active implantable, radiological) where Annex X might be mandatory rather than Annex IX?  
- **Source coverage:** Does the provided source adequately support all required documentation elements, or are additional MDR clauses (e.g., Article 10 on conformity‑assessment procedures) needed for completeness?  
- **Jurisdictional gaps:** Are there any EU‑specific requirements (e.g., Unique Device Identification, EUDAMED registration – Art. 33‑39) that have been omitted and should be highlighted at this stage?

*Your feedback will help ensure the regulatory package is complete before submission to the Notified Body.*

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

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

### kb-eval-20260718-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "000ee9037b6dc9a5", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md", "source_hash": "4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `000ee9037b6dc9a5`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_%EC%9D%B8%ED%97%88%EA%B0%80_%EC%83%81%EC%84%B8%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_인허가_상세가이드.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 2.3 Rule 11 (SW) > Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as class IIa. > 단, decision may cause (a) death or irreversible deterioration → **Class III**; (b) serious deterioration or surgical intervention → **Class IIb**. > Software intended to monitor physiological...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Classification & Conformity Assessment Route for Imaging‑Room GUI Software (Rule 11)**  

---

### 1. Device Summary (derived from source)

| Item | Description |
|------|-------------|
| **Intended purpose** | Software that provides information to the operator of an X‑ray/CT imaging suite and is used to support diagnostic or therapeutic decisions (e.g., image‑review, exposure guidance). |
| **Regulatory reference** | Rule 11 (Annex VIII) – “Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes”【1†L1-L4】. |
| **Preliminary impact assessment** | The software can potentially influence clinical decisions that may lead to: <br>‑ *Serious deterioration or surgical intervention* → Class IIb (Rule 11 b).<br>‑ *Death or irreversible deterioration* → Class III (Rule 11 a).<br>If the decision impact is limited to “general” diagnostic support without immediate danger, Class IIa applies. |
| **Current classification proposal** | **Class IIa – IIb – III** pending confirmation of the exact clinical impact (see §2). |

---

### 2. Classification Determination  

1. **Apply Rule 11 (Annex VIII)**  
   - Software that “provides information which is used to take decisions with diagnosis or therapeutic purposes” → baseline **Class IIa**【1†L1-L4】.  
   - Escalate to **Class IIb** if a decision could cause *serious deterioration* or require *surgical intervention* (Rule 11(b)).  
   - Escalate to **Class III** if a decision could cause *death* or *irreversible deterioration* (Rule 11(a)).

2. **Evidence required to substantiate impact level**  
   - Clinical use case descriptions, patient risk analysis, and “decision consequence matrix” linking software output to clinical outcomes.  
   - Expert opinion from the treating specialty (radiology/interventional radiology).  

3. **Decision point** – *Missing Information* (see §5). Until the impact level is documented, the exact class remains provisional.

---

### 3. Conformity Assessment Route  

| Device Class | Applicable MDR Annex(es) | Required NB Involvement |
|--------------|--------------------------|------------------------|
| **Class IIa** | **Annex IX** (QMS + Technical Documentation assessment) – NB reviews the technical file and issues a CE certificate. | Limited scope: NB audits QMS (ISO 13485) and verifies Annex II documentation. |
| **Class IIb / III** | **Annex IX** (same route, but with deeper NB scrutiny). For Class III, additional requirements may apply (e.g., design dossier review, clinical investigation data). | Full NB assessment of technical documentation, PMS plan, and for Class III a possible *design dossier* evaluation under the “strict” schedule. |

> **Note on transition periods** – The MDR transition deadlines for non‑implantable Class IIb / IIa devices are 31 December 2028【2†L5-L7】. The software therefore remains within the current MDR regime without a forced re‑classification deadline, but early compliance is advisable.

---

### 4. Required Technical Documentation (Annex II) & Clinical Evidence  

| Section | Required Artefacts |
|---------|--------------------|
| **1. Device Description** | Complete functional specification, software architecture diagram, intended user(s), operating environment. |
| **2. Intended Use** | Precise claim wording; decision‑impact statement supporting the chosen class. |
| **3. Design & Development** | IEC 62304 (software life‑cycle) evidence: development plan, verification/validation protocols and reports, traceability matrix. |
| **4. Risk Management** | ISO 14971 risk management file – identification of hazards related to decision support, evaluation of residual risk, justification for risk controls. |
| **5. Usability Engineering** | IEC 62366‑1 usability validation (human factors) focusing on information presentation and operator interaction. |
| **6. Cybersecurity** | IEC 62443 / ISO/IEC 27001 controls: threat model, secure update mechanism, encryption of patient data. |
| **7. Clinical Evaluation Report (CER)** – Annex XIV Part A | State‑of‑the‑art literature review; post‑market clinical follow‑up (PMCF) plan (Annex XIV Part B). For Class IIb/III, consider a *clinical investigation* to generate primary data. |
| **8. PMS System** – Art. 83 & 84 | PMS plan covering incident reporting, trend analysis, and periodic safety update report (PSUR) for Class IIb/III (Art. 86). |
| **9. Labeling & IFU** – Annex I §23 | Full user manual, software instructions for use, risk information, and performance claims. |

---

### 5. Missing Information / Evidence Gaps  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Exact clinical impact of the decision support** (death vs serious deterioration vs general) | Determines whether Class IIa, IIb or III applies. | Obtain a detailed “decision consequence matrix” from clinical SMEs and document in the intended‑use statement. |
| **Clinical validation data** (real‑world performance, sensitivity/specificity of software output) | Needed for CER and to justify residual risk level. | Run a prospective observational study or compile retrospective case series; draft PMCF plan accordingly. |
| **Software verification & validation traceability** (IEC 62304 compliance evidence) | Mandatory for Annex II Technical Documentation. | Compile test logs, verification matrices, release notes. |
| **Usability evaluation results** (human‑factors testing of GUI) | Critical to mitigate use errors leading to mis‑diagnosis. | Conduct formative and summative usability studies with representative operators; include findings in the risk file. |
| **Cybersecurity assessment** (threat model, secure update process) | MDR requires protection against unauthorized access that could affect clinical decisions. | Produce a cybersecurity risk analysis and mitigation plan per IEC 62443/ISO 27001. |
| **PMS/PMCF data collection strategy** | Required for continued compliance; PSUR preparation for Class IIb/III. | Define KPIs, incident reporting pathways, and schedule for periodic safety update reports (Art. 86). |

---

### 6. Core Risk Controls (ISO 14971)  

1. **Information Accuracy Control** – Automated verification of image metadata before display; error‑checking algorithms to flag missing data.  
2. **Alarm & Alert Management** – Distinct visual/audible alerts when software indicates a high‑risk decision (e.g., “exposure exceeds safe limit”).  
3. **Fail‑Safe Mode** – If critical software component fails, system defaults to “read‑only” mode and directs user to manual assessment.  
4. **Access Control & Authentication** – Role‑based login; audit trails for all decisions supported by the GUI.  
5. **Usability Safeguards** – Consistent colour coding, confirmation dialogs before applying treatment parameters derived from software output.  
6. **Cybersecurity Measures** – Signed firmware/software updates, encrypted communication with imaging hardware, regular vulnerability scanning.

---

### 7. Human‑Escalation Triggers  

| Trigger | Escalation To | Reason |
|---------|---------------|--------|
| **Unresolved classification impact** (cannot justify Class IIa vs IIb/III) | Senior RA / Clinical Lead | Classification decision directly affects conformity route and NB workload. |
| **Insufficient clinical evidence** (no validated performance data) | Clinical Research Team & Project Management | Required for CER; may necessitate a formal clinical investigation. |
| **PMS deadline approaching without PMCF plan** (e.g., > 6 months before 31 Dec 2028) | Quality Manager / Regulatory Director | Non‑compliance with Art. 84/86 could lead to audit findings. |
| **Cybersecurity vulnerability identified in the field** | IT Security Officer & RA Lead | Immediate risk to patient safety; triggers post‑market incident reporting (Art. 83). |
| **Usability failure observed during pilot use** | Human Factors Engineer & RA | Must be mitigated before market launch to avoid user error risks. |

---

### 8. Summary of Next Steps  

1. **Finalize impact assessment** – obtain clinical expert statements and document the decision‑consequence matrix.  
2. **Select classification (IIa/IIb/III) and corresponding NB pathway (Annex IX).**  
3. **Compile technical documentation per Annex II**, focusing on the identified gaps above.  
4. **Develop & execute a PMCF plan** (Annex XIV Part B) aligned with the chosen class.  
5. **Schedule internal peer review** (see below).

---

### 9. Peer‑Review Prompt  

> *Colleague, please challenge the assumptions made in this draft:*  
> - Is the decision‑impact matrix sufficient to justify a Class IIa versus IIb/III classification under Rule 11?  
> - Does the source material adequately cover all MDR clauses (e.g., transition deadlines) applicable to this software, or are we missing jurisdiction‑specific guidance (e.g., national implementation variations)?  
> - Are there any additional evidence requirements (e.g., specific clinical investigation design for Class III) that have not been captured here?  

Your feedback will be incorporated before final submission to the Notified Body.

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

1. Chunk `1007248354989010815`

> ### 2.3 Rule 11 (SW) > Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as class IIa. > 단, decision may cause (a) death or irreversible deterioration → **Class III**; (b) serious deterioration or surgical intervention → **Class IIb**. > Software intended to monitor physiological processes: 일반 IIa / immediate danger IIb. > Others: Class I. **→ 촬영실 GUI SW = Rule 11 적용, 영향도에 따라 IIa ~ III**

2. Chunk `1007987960287657537`

> ### 7.1 차등 시한 | Class | 시한 | |---|---| | Class III **custom-made** implantable | 2026-05-26 | | Class III / Class IIb **implantable** (sutures·screws 등 제외) | **2027-12-31** | | Class IIb **non-implantable** / IIa / Is / Im | **2028-12-31** |

## ra_kr

### kb-eval-20260718-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "1a49e8c0440c9349", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `1a49e8c0440c9349`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98_%EA%B8%B0%EC%A4%80/%EC%A0%9C%ED%92%88%EB%B3%84_%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98.md)
- Source hash: `f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `제품별_등급분류.md`는 `제품별_등급분류.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우) ### 3.2 미국 (FDA) — **Class II** - **Product Code 후보**: **LLZ** (Medical Image Management and Processing System) / **QIH...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Korean MFDS Pathway for an AI‑Enabled Medical‑Software System**

---

### 1. Classification & Submission Route  
| Item | KR (MFDS) | Basis / Citation |
|------|-----------|------------------|
| **Risk class** | **2등급 (Class II)** – can be raised to a higher class depending on the level of “보조 기능” (supportive function). | MFDS “의료용 소프트웨어 허가·심사 가이드라인” & **Digital Medical Device Act** (디지털의료제품법) effective 2025‑01‑24 – see source [1]. |
| **Submission type** | **허가 (Approval)** – required for Class II devices. | Same as above; no “신고 (Notification)” pathway for this class. |

> **Note:** If the software is determined to be an “independent” digital medical device (stand‑alone application) the **독립형 SW 사용적합성 가이드라인** applies in addition to the general software guideline.

---

### 2. Core Evidence Package Required by MFDS  

| Evidence | Korean Requirement | Typical International Equivalent | Source |
|----------|-------------------|----------------------------------|--------|
| **Device description & intended use** | Detailed description in Korean, including clinical purpose, user environment, and AI/ML functions. | FDA 510(k) device description; EU MDCG guidance. | — |
| **Risk Management File** (ISO 14971) | Full risk analysis, risk control measures, residual risk evaluation, and benefit‑risk justification. | Same for FDA/EU. | — |
| **Software Development Lifecycle Documentation** (IEC 62304) | Development plan, architecture, verification & validation reports, configuration management. | Required by FDA 510(k) for software; EU MDR Annex II. | — |
| **Performance/Validation Data** | Bench testing, algorithm accuracy, robustness, and user‑interface usability studies performed according to Korean “디지털의료기기소프트웨어 허가·심사 가이드라인”. | FDA performance testing; EU MDCG 2020‑5. | — |
| **Clinical Evaluation Report (CER)** | Clinical data supporting safety & efficacy – may include foreign clinical evidence if accepted under MFDS scope extensions (see MFDS notices on foreign CE/FDA data). Local Korean data often required for AI/ML devices. | FDA 510(k) clinical data; EU MDCG 2021‑24. | — |
| **Change Management Plan** | For AI/ML – a **변경관리계획** covering algorithm updates, retraining, and post‑marketing monitoring as stipulated in the Digital Medical Device Act (2025). | FDA PCCP (Predetermined Change Control Plan) guidance. | Source [1] (reference to “변경관리계획”). |
| **Cybersecurity & SBOM Documentation** | Security architecture, threat analysis, mitigation measures; Software Bill of Materials as per new Korean cyber‑regulation aligning with the 2023 MFDS/ISO 27001 expectations. | FDA Cybersecurity Guidance (2023) and SBOM obligations under U.S. Section 524B (Omnibus). | Source [2] (US context shows parallel trend; Korean rule emerging under Digital Medical Device Act). |
| **Labeling & IFU** | All labeling, instructions for use (IFU), and promotional material must be in **Korean language**, with clear statements of intended use, contraindications, warnings, and disposal. | FDA labeling (§ 803) & EU MDR Annex I. | — |
| **KGMP Certification** (if device is manufactured domestically) | Facility must hold a **Korean Good Manufacturing Practice (KGMP)** certificate for medical devices (ISO 13485‑based). | ISO 13485 certification requirement for FDA/EU. | — |

> **Missing identifiers:** No specific 510(k) predicate number, MFDS registration number, or product code appears in the source excerpts. Verify these separately before final submission.

---

### 3. Identified Gaps / Missing Information  

| Gap | Why it matters & impact on approval |
|-----|--------------------------------------|
| **Precise Intended Use Statement** (Korean) | Determines classification ceiling; vague claims may trigger re‑classification to higher risk class. |
| **Local Clinical Evidence** for AI/ML algorithm performance | MFDS often requires Korean patient data when the algorithm is trained on non‑local datasets. Absence may delay approval or require additional bridging studies. |
| **Detailed Change Management Plan (변경관리계획)** for future AI updates | Without a documented plan, MFDS could reject the dossier under the 2025 Digital Medical Device Act. |
| **KGMP status of manufacturing site** | If manufacturing occurs in Korea, KGMP certification is mandatory; lacking it will halt processing at the “허가심사” stage. |
| **Cybersecurity Architecture & SBOM** specific to Korean regulations | Emerging requirement; insufficient documentation may be deemed non‑compliant with the new cybersecurity provisions. |
| **Korean language labeling files (PDF/Print) and packaging artwork** | MFDS rejects submissions without complete Korean-language labeling set. |
| **Evidence of conformity to 독립형 SW 사용적합성 가이드라인** (if applicable) | Missed compliance may re‑classify the product or force additional testing. |

---

### 4. Core Risk Controls to Emphasize in Dossier  

1. **Algorithm Transparency & Explainability** – Document model decision logic, training data provenance, and performance metrics across relevant populations.  
2. **Robust Cybersecurity Framework** – Apply defense‑in‑depth, regular vulnerability scanning, secure updates via signed firmware/software packages; include SBOM.  
3. **Software Version Control & Traceability** – Align with IEC 62304 and MFDS change‑management requirements; maintain trace matrix from user needs to code modules.  
4. **Human‑Machine Interaction Safeguards** – UI design that prevents misuse, alerts for out‑of‑range inputs, failsafe defaults.  
5. **Post‑Market Surveillance (PMS) Plan** – Real‑world performance monitoring, incident reporting workflow in Korean, and periodic safety updates per MFDS “시판후조사”.  

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger Action |
|-----------|----------------|
| **Unclear classification** (e.g., software functions could be therapeutic) | Escalate to senior RA lead for a formal MFDS pre‑submission meeting request. |
| **Missing local clinical data** or unclear acceptance of foreign evidence under current MFDS notice | Prompt senior RA to consult with MFDS liaison office; consider conducting bridging study. |
| **KGMP certification not yet obtained** | Immediately involve Quality Assurance/Manufacturing to start KGMP audit process before dossier finalization. |
| **Regulatory notice on AI/ML change control (new 2025 act) released after initial draft** | Pause submission, have regulatory lead review the updated notice, and revise 변경관리계획 accordingly. |
| **Discrepancy between Korean labeling draft and intended‑use description** | Halt final dossier assembly; involve medical writing & translation team to resolve. |

---

### 6. Citations (as extracted from source)  

- MFDS “의료용 소프트웨어 허가·심사 가이드라인” – classification basis for **2등급** (source [1]).  
- Digital Medical Device Act (디지털의료제품법), effective 2025‑01‑24 – establishes AI/SW dedicated framework and change‑management requirement (source [1]).  
- 독립형 SW 사용적합성 가이드라인 – separate applicability for stand‑alone software (source [1]).  

> *No specific FDA predicate numbers, MFDS registration IDs, or product codes appear in the provided excerpts; please verify these identifiers independently before filing.*

---

### 7. Peer‑Review Prompt  

*“@RA‑Peer, please review this draft and challenge:*

- *Are we correctly interpreting the 2등급 ceiling given the AI functionalities?*  
- *Do we have sufficient coverage of MFDS’s recent notice on accepting foreign clinical evidence for AI/ML devices?*  
- *Have we captured all Korean‑specific obligations (language, KGMP, SBOM) without over‑relying on US FDA guidance?*  

*Your feedback will help confirm jurisdictional gaps and ensure the dossier meets current MFDS expectations.”*

---

## Honcho Conclusion – Reusable RA Judgment  

**Lesson:**  
When a digital medical‑software device is classified as **2등급** under the 2025 Digital Medical Device Act, the Korean submission must include (a) a **변경관리계획** for AI/ML updates, (b) compliance with both the general “의료용 소프트웨어 허가·심사 가이드라인” and the separate **독립형 SW 사용적합성 가이드라인** if applicable, and (c) newly emerging Korean cybersecurity documentation (SBOM, cyber‑risk analysis). Absence of explicit local clinical data for AI algorithms is a common gap; MFDS may still accept foreign evidence but only when explicitly referenced in the latest notice—therefore always verify the current notice before reliance.  

**Actionable Rule:**  
*For any AI‑enabled medical software targeting Korean market, automatically flag the need to (1) obtain or confirm KGMP certification of the manufacturing site, (2) prepare a Korean‑language labeling set, and (3) secure a detailed change‑management plan aligned with the 2025 Act before finalizing the 허가 dossier.*

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

### kb-eval-20260718-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "e5180461a3d586b5", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `e5180461a3d586b5`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%ED%91%9C%EC%8B%9C%EA%B8%B0%EC%9E%AC_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_%EB%8C%80%EC%9D%91.md)
- Source hash: `5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_디지털의료기기_표시기재_가이드라인_대응.md`는 `MFDS_디지털의료기기_표시기재_가이드라인_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MFDS Classification & Licensing Path for a Digital Medical‑Device Software (SW) Product**

---

### 1. Tentative MFDS Classification & Submission Route  

| Item | Reasoning |
|------|-----------|
| **Device type** | Pure software (“디지털의료기기” / “Digital medical device”) – no hardware listed in the source. |
| **Risk class (예상)** | • If the software performs diagnostic, therapeutic or monitoring functions that influence patient care decisions → **Class II** or higher.<br>• If it is a simple health‑information app with no direct clinical impact → **Class I**. <br>*Classification must be confirmed by mapping the intended use to MFDS risk‑classification tables (MFDS 고시 제2023‑XX호).​* |
| **Submission pathway** | • **Class I** – *신고* (notification) is sufficient.<br>• **Class II–IV** – *허가* (approval) via the appropriate MFDS application (e.g., “의료기기 허가 신청”).<br>*The exact route will be selected after final risk‑class determination.* |

---

### 2. Mandatory Evidence & Documentation Required (per MFDS Digital‑Medical‑Device Guidelines)

| Requirement (Source reference) | Status | Comments / Needed Documents |
|--------------------------------|--------|------------------------------|
| **S‑1 : Software version·build number·release date** – 필수【1】 | ☐ Missing | Provide a clear list of each software release with version, build ID and official release date. |
| **S‑2 : Update method & frequency** – 필수【1】 | ☐ Missing | Describe OTA/manual update mechanisms, schedule (e.g., quarterly), and responsible party. |
| **S‑3 : Minimum / recommended system specifications (OS, CPU, RAM, storage, monitor resolution, network)** – 필수【1】 | ☐ Missing | Provide a table of required hardware/environment specs for each supported platform. |
| **S‑4 : List of compatible medical devices & interface information** – 필수【1】 | ☐ Missing | Identify every medical device that the software can interoperate with, including communication protocols and connector details. |
| **S‑5 : Data input/output formats (DICOM, HL7, etc.)** – 필수【1】 | ☐ Missing | Specify all supported data standards, version numbers, and mapping tables. |
| **S‑6 : Cybersecurity configuration guidance (password policy, network segregation, access rights)** – 필수【1】 | ☐ Missing | Include a cybersecurity control matrix aligned with MFDS 사이버보안 가이드라인 2025.01. |
| **S‑7 : Security‑patch application procedure & responsible party** – 필수【1】 | ☐ Missing | Outline patch lifecycle, validation steps and accountability. |
| **S‑8 : Known residual cybersecurity risks & mitigation actions** – 필수【1】 | ☐ Missing | Summarize risk assessment (ISO 14971) outcomes for cyber threats and planned mitigations. |
| **S‑9 : Data backup & recovery method** – 필수【1】 | ☐ Missing | Provide backup schedule, storage location, restoration testing results. |
| **S‑10 : System log management method** – 권장⚠️【1】 | ☐ Optional (but highly recommended) | Detail log collection, retention period, and review process. |
| **Digital‑medical‑device specific labeling checklist items** – 필수 (additional to generic IFU)【2】 | ☐ Missing | Include all extra label/IFU elements required for digital devices (e.g., software version, cybersecurity statements). |

> **Note:** The above table reflects *absence* of the required artifacts in the current dossier; each must be generated before MFDS submission.

---

### 3. Risk‑Control Measures to Be Demonstrated  

| Control | Applicable Standard / Guideline | Evidence Needed |
|---------|---------------------------------|-----------------|
| **Software lifecycle & development process** | IEC 62304 (Medical device software – life cycle processes) | Development plan, verification/validation reports, traceability matrix. |
| **General risk management** | ISO 14971 (Risk Management for Medical Devices) | Risk Management File with identified hazards, severity/occurrence analysis, mitigations—including cyber‑risk controls. |
| **Cybersecurity** | MFDS 사이버보안 가이드라인 2025.01 (cited in S‑6~S‑8) | Cyber‑risk assessment, penetration‑test results, security architecture documentation, patch management SOPs. |
| **Usability / Human factors** (if UI influences clinical decisions) | IEC 62366‑1 | Usability testing reports, user interface specifications. |
| **Software validation (including AI/ML components, if any)** | MFDS “AI/ML” guidance (not shown in excerpt – request separately) | Validation dataset, performance metrics, algorithm change‑control procedures. |

---

### 4. Missing Information & Gap Summary  

| Gap Category | What is Missing | Impact on Submission |
|--------------|-----------------|----------------------|
| **Product definition** | Precise intended use, clinical claim, target patient population. | Determines risk class; without it MFDS cannot place the device in a classification tier. |
| **Technical specifications** (S‑1 to S‑9) | All items listed above. | Mandatory for Class II+ 허가; omission leads to rejection or request for additional information. |
| **Labeling / IFU content** | Digital‑device specific checklist items (source [2]). | Required under MFDS 규정 for digital products; lack triggers a “보완 요청”. |
| **Foreign evidence (if applicable)** | CE‑mark, FDA 510(k) or other overseas clearance that may be referenced. | If used to support Korean approval, must meet latest MFDS acceptance scope (e.g., OECD‑aligned data). Verify current notice before citing. |
| **KGMP certification** (for software hosted on a medical device production facility) | Facility compliance certificate. | Required for any “제조업 허가” or when the software is considered part of the device’s manufacturing process. |

---

### 5. Human‑Escalation Triggers  

1. **Classification Uncertainty** – If intended use cannot be clearly mapped to a risk class, pause and route to senior RA lead for classification decision.  
2. **Mandatory Data Missing** – Any “✅ 필수” item (S‑1 ~ S‑9) absent → immediate stop of dossier preparation; notify product owner & development team.  
3. **Cybersecurity Deficiency** – If residual cyber risk cannot be reduced to an acceptable level per MFDS 사이버보안 가이드라인, trigger escalation to CISO/QA for remediation plan.  
4. **Labeling Gap** – Missing digital‑device specific labeling elements (source [2]) → flag to Marketing & Documentation lead; cannot submit until resolved.  
5. **Foreign Evidence Acceptance** – If intending to rely on overseas clearance, verify the latest MFDS notice that expands accepted foreign evidence; if ambiguous, escalate to regulatory affairs manager for clarification before inclusion.  

---

### 6. Draft citation list  

| Cited Item | Source |
|------------|--------|
| S‑1 ~ S‑10 (mandatory software information) | 【1】 “디지털의료제품법 시행규칙” & MFDS 사이버보안 가이드라인 2025.01 |
| Digital‑medical‑device labeling checklist addition | 【2】 “디지털의료기기 특화 표시기재 요건 체크리스트” |

*No specific identifier (e.g., notice number, article code) appears in the source excerpts; verify the exact MFDS notices separately before final submission.*

---

### 7. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review this draft and challenge the following points:  
> 1. The assumed risk class (I vs II) based solely on “software‑only” – are there any functional clues in the product brief that could shift it to Class III/IV?  
> 2. Whether the checklist items captured from source [1] cover all MFDS mandatory labeling requirements for digital devices, or if additional elements (e.g., software safety notice, adverse event reporting info) are missing.  
> 3. The adequacy of referencing the MFDS 사이버보안 가이드라인 2025.01 without quoting the specific article numbers – does the current version still apply, or has a newer amendment been issued?  
> 4. Any potential reliance on foreign clinical evidence that could be permissible under recent MFDS scope expansions; request confirmation of the exact notice number if you have it.  

Your feedback will help close any jurisdiction‑specific gaps before we move to the formal MFDF submission package.

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

1. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

2. Chunk `124386539616979555`

> ## 3. 디지털의료기기 특화 표시기재 요건 체크리스트 > 일반 의료기기 표시기재 필수사항(→ IFU_필수요소_3지역_비교.md 참조)에 **추가**되는 항목

### kb-eval-20260718-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "39ca8fb2e959a790", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `39ca8fb2e959a790`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital Medical‑Device Software (GUI SW)**  

---

### 1. Applicable MFDS Regulations  
| Regulation | 고시 번호 | 시행일 | Core Scope |
|------------|-----------|--------|------------|
| “디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정” | **제2025‑25호** | 2025‑04‑15 | 허가·심사 절차, 서류 요건, 평가 기준 – applies to all digital medical product submissions. |
| “디지털의료제품의 분류 및 등급 지정 등에 관한 규정” | **제2025‑23호** | 2025‑04‑07 | Classification matrix for digital medical devices (including GUI software). |
| “디지털 의료기기 제조 및 품질관리 기준 (디지털 GMP)” – implementation scheduled for 2025 | 별도 고시 | 2025년 내 시행* | 8 유형군별 GMP 요건 (AI/ML 포함). |

\*Note: The monitoring point in the source indicates that the **digital‑GMP 고시** is “검증 필요” and should be checked quarterly (see excerpt [2]).

---

### 2. Likely Classification & Submission Route  

| Device Type | Typical Use (GUI only) | Expected Class* | MFDS Pathway |
|-------------|------------------------|----------------|--------------|
| Software that **only provides information display, data visualization or workflow assistance** and does **not perform diagnosis, treatment, or risk‑mitigating calculations** | Graphical User Interface (GUI) for clinicians/participants | **Class I** (lowest risk) | **신고 (Notification)** – no full 허가 required, but must submit a notification dossier per 고시 제2025‑25호. |

\*If the software incorporates any of the following, re‑evaluate to Class II or higher: automated decision support, AI/ML inference that influences clinical decisions, direct patient monitoring, or data that become part of a therapeutic regimen.

---

### 3. Required Submission Evidence (per 고시 제2025‑25호)

| Category | Mandatory Documents / Artefacts |
|----------|----------------------------------|
| **Product Information** | - Korean‑language product name & description <br> - Intended use statement (Korean) <br> - Risk classification justification (reference to 고시 제2025‑23호 matrix) |
| **Risk Management** | - ISO 14971 risk management file (hazard analysis, risk control measures, residual risk evaluation) <br> - Cybersecurity assessment (if network‑connected) |
| **Software Engineering** | - IEC 62304 software life‑cycle documentation (development plan, verification & validation results) <br> - Usability engineering file (IEC 62366) for GUI design |
| **Clinical Evaluation** | - Clinical evaluation report (CER) supporting safety & performance. For Class I, a literature review may be sufficient; if foreign clinical data are used, confirm acceptance under the latest MFDS scope expansion (see MFDS 6‑type guideline updates post‑2025). |
| **Labeling / IFU** | - Korean language labeling, user manual, and any patient‑facing instructions (must comply with MFDS labeling standards) |
| **Quality System Evidence** | - If the digital‑GMP 고시 is in force for the device type (check quarterly), provide evidence of compliance with the relevant GMP type (e.g., Type 3 for software). Until the 고시 becomes effective, a quality management system certificate based on ISO 13485 is acceptable. |
| **Other** | - Declaration of conformity to applicable international standards (ISO 14971, IEC 62304) <br> - List of predicate devices (if any foreign 510(k)/CE equivalence is claimed – only cite if the source contains a concrete identifier). |

---

### 4. Gaps / Missing Information (to be resolved before dossier finalisation)

| Item | Why it matters |
|------|----------------|
| **Precise intended use wording** (including target user, environment, and claim scope) | Determines classification under 고시 제2025‑23호. |
| **Confirmation of digital‑GMP applicability** for the device type (type‑group) | The monitoring table (excerpt [2]) flags “디지털 GMP 고시 시행 – 2025년 내 예정 [검증 필요]”. Need to verify whether the high‑risk GMP requirements already apply or are pending. |
| **Local clinical data requirement** – does the intended use fall under an exemption where foreign CER is acceptable? | MFDS has been expanding acceptance of OECD‑aligned foreign evidence, but the exact scope must be checked in the latest 6‑type guideline revision (post‑2025). |
| **Korean language labeling draft** (including safety symbols, contraindications, etc.) | Mandatory for all submissions; omission leads to rejection. |
| **Cybersecurity plan** (if device communicates over network) | Required risk control per MFDS and ISO 14971. |
| **Verification of predicate or foreign clearance numbers** – none appear in the provided excerpts. Must be sourced separately if you intend to claim equivalence. |

---

### 5. Core Risk Controls to Emphasise  

1. **Hazard Identification & Mitigation** (ISO 14971) – focus on UI‑related misuse, data entry errors, and incorrect display of information.  
2. **Usability Engineering** – conduct formative and summative usability tests with intended Korean users; document findings in the IEC 62366 file.  
3. **Cybersecurity** – implement authentication, encryption, and regular patching; provide a threat‑model and mitigation plan.  
4. **Software Verification & Validation** – unit, integration, system testing per IEC 62304; final validation against intended use claims.  
5. **Post‑Market Surveillance (PMS) Plan** – signal detection procedures, periodic safety update reports (PSUR), and a clear reporting pathway to MFDS.

---

### 6. Citations  

- 고시명: **디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정**, **제2025‑25호**, 시행일 2025‑04‑15 (source [1]).  
- 고시명: **디지털의료제품의 분류 및 등급 지정 등에 관한 규정**, **제2025‑23호**, 시행일 2025‑04‑07 (source [1]).  
- “디지털 GMP 고시 시행” monitoring point – pending verification, scheduled for 2025 (source [2]).  
- “디지털의료제품법 시행규칙 개정 (총리령 제2088호)”, amendment completed 2026‑01‑23 (source [2]).

*No specific foreign identifier (e.g., FDA 510(k) number, CE certificate) appears in the provided excerpts.*

---

### 7. Human‑Escalation Triggers  

| Trigger | Action |
|---------|--------|
| **Unclear classification** after initial matrix check (e.g., AI/ML features ambiguous) | Escalate to senior RA for a formal risk‐based classification workshop. |
| **Digital‑GMP 고시 status pending** beyond the quarterly verification cycle | Notify quality‑system manager & consider provisional ISO 13485 compliance; flag for MFDS clarification before submission. |
| **Requirement for local clinical data** that cannot be satisfied with existing foreign evidence | Request a feasibility study or Korean pilot data, and inform project sponsor of timeline impact. |
| **Korean language labeling draft rejected** by internal review (e.g., missing safety symbols) | Engage medical‑writer/legal translation specialist immediately. |
| **Cybersecurity plan deficiencies identified during internal audit** | Halt submission preparation; involve IT security team to remediate. |

---

### 8. Peer‑Review Prompt  

> **To the RA colleague reviewing this draft:**  
> - Are the classification assumptions (Class I, 신고) fully supported by the device’s functional description? If any AI/ML or decision‑support element exists, how should we adjust the risk class?  
> - Have we captured all MFDS evidence requirements under 고시 제2025‑25호, especially concerning the emerging digital‑GMP regime? Are there any additional mandatory documents (e.g., “Software Design Dossier”) that we missed?  
> - Given that no foreign clearance identifiers are present in the source material, is our approach to rely on external evidence adequately justified, or should we request explicit confirmation from MFDS on scope acceptance?  

Please challenge any assumptions, point out gaps in source coverage, and highlight jurisdiction‑specific nuances that may have been overlooked.  

---

### 9. Reusable RA Judgment (Memory Record)  

> **Lesson:**  
> When assessing a digital medical‑device software (GUI‑only) under the 2025 MFDS regulations, reference 고시 제2025‑23호 for classification and 고시 제2025‑25호 for submission requirements. A GUI that solely displays information without diagnostic or therapeutic function is generally **Class I** and follows the **신고** pathway. Required evidence includes Korean‑language labeling, ISO 14971 risk management, IEC 62304 software documentation, and a clinical evaluation (literature review may suffice). Verify the status of the **digital‑GMP 고시** (implementation expected in 2025) before claiming GMP compliance; until then, ISO 13485 certification is acceptable. If foreign clinical data are to be used, confirm acceptance under the latest MFDS scope expansion (post‑2025 6‑type guideline updates). Flag any ambiguity in intended use, pending digital‑GMP applicability, or missing local clinical data for senior‑RA escalation.  

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

1. Chunk `1131342938714268388`

> ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건 (AI/ML 포함) | SW GMP 적용 기준 | ---

2. Chunk `385578214769089426`

> ## 5. 모니터링 포인트 | 항목 | 상태 | 확인 주기 | |---|---|---| | 디지털 GMP 고시 시행 | 2025년 내 예정 [검증 필요] | 분기별 확인 | | 디지털의료제품법 시행규칙 개정 (총리령 제2088호) | 2026-01-23 개정 완료 | — | | 추가 가이드라인 제정 | 지속 예고 중 | 월별 mfds.go.kr 확인 | | MFDS 6종 가이드라인 후속 개정 | 2025년 이후 수시 | 분기별 확인 | ---

### kb-eval-20260718-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "761294def6a48449", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "5f0192e5896bd583833f41c673027bfe34b52793e1679d1f9dc751b5f77320c3"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `761294def6a48449`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%B8%ED%97%88%EA%B0%80_%EC%83%81%EC%84%B8%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `5f0192e5896bd583833f41c673027bfe34b52793e1679d1f9dc751b5f77320c3`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_인허가_상세가이드.md`는 `MFDS_인허가_상세가이드.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수 # MFDS 인허가 상세 가이드 (국내, X-ray System 전용) > 웹 리서치 교차검증 반영 – 2026-04-22 기준
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MFDS Classification & Licensing Pathway**

---

### 1. Applicable Legal Framework  
- **Medical Device Act (법률)** → **Enforcement Decree (시행령, 대통령령)** → **Enforcement Rules (시행규칙, 총리령).**  
- Relevant MFDS notices:  
  - *「의료기기 품목 및 품목별 등급에 관한 규정」* – defines product‑type classifications and grade assignments.  
  - *「의료기기 허가·신고·심사 등에 관한 규정」* – outlines the permissible submission routes (허가, 신고, 심사) for each class.  
  - *「의료기기 GMP 심사·평가 등에 관한 규정」* – governs KGMP certification of manufacturing sites.  

*(Source [1] – “전통 의료기기 체계 …”.)*  

---

### 2. Determination of Device Class & Submission Route  

| Device Category (example) | MFDS Class | Typical Submission Type | Key Regulatory Citation |
|---------------------------|------------|--------------------------|--------------------------|
| General‑purpose X‑ray System (as referenced in the guide) | **Class II** (or higher if high‑risk functions are present) | **허가** (full approval) – mandatory for Class II and above; **신고** only for Class I. | *MFDS 인허가 상세 가이드 (X‑ray System 전용)* – indicates that X‑ray systems follow the 허가 pathway. *(Source [2]).* |

> **Action:** Verify the exact class of your specific X‑ray system by cross‑referencing the product’s intended use, risk profile, and technical specifications against the *품목 및 품목별 등급에 관한 규정*.  

---

### 3. Required Evidence Package (허가 신청)  

| Evidence Category | Typical Content | MFDS Reference |
|-------------------|----------------|----------------|
| **Device Description** | Technical specifications, design drawings, intended use, labeling mock‑ups (Korean). | 「의료기기 허가·신고·심사 등에 관한 규정」 |
| **Non‑Clinical Testing** | Electrical safety, electromagnetic compatibility, radiation protection data; OECD‑aligned toxicology if applicable. | Same as above; note that recent MFDS scope expansions accept foreign non‑clinical data when aligned with OECD standards (see latest MFDS notice – confirm date). |
| **Clinical Evaluation** | Local clinical trial results *or* a well‑justified reliance on foreign CE/FDA clearance with bridging data, provided the device’s risk class permits. | Same as above; Korean law may still require limited local data for Class II devices. |
| **Risk Management File** | ISO 14971‑compliant risk analysis, mitigation measures, post‑market surveillance plan. | Implicit in 허가 심사 규정. |
| **KGMP Certification** | Facility KGMP audit report (ISO 13485‑based) for the manufacturing site(s). | 「의료기기 GMP 심사·평가 등에 관한 규정」 |
| **Labeling & IFU** | Korean language labeling, user manual, safety notices; compliance with MFDS labeling guidelines. | Same as above. |

> **Note:** No specific identifier (e.g., 510(k) number, predicate device ID) appears in the source excerpts; therefore **“no specific identifier found in source — verify separately.”**  

---

### 4. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Remedy |
|-----|----------------------|--------|
| **Exact Device Class** – The excerpt only states X‑ray systems are covered by the detailed guide; it does not disclose the class of a specific model. | Mis‑routing (e.g., filing a 신고 instead of 허가) can cause rejection or legal penalties. | Conduct a formal classification analysis per *품목 및 품목별 등급에 관한 규정* and document justification. |
| **Local Clinical Data Requirement** – Unclear whether foreign clinical evidence alone suffices for this device type. | Potential lack of required efficacy/safety data leading to additional studies. | Determine if the device is exempt from local trials under MFDS’s “foreign clinical evaluation report” acceptance policy; if not, plan a limited Korean site study. |
| **KGMP Status of Manufacturing Site** – No evidence that the production facility already holds KGMP certification. | Production cannot commence until KGMP audit passes; submission may be delayed. | Obtain or update KGMP certificate; include audit report in dossier. |
| **Korean Language Labeling Drafts** – Not mentioned in source excerpts. | Failure to meet labeling requirements will halt approval. | Prepare Korean labeling/IFU and submit for MFDS review as part of the dossier. |

---

### 5. Risk Controls & Compliance Measures  

1. **Classification Verification** – Use a cross‑functional team (RA, engineering, clinical) to map device functions against the *품목 및 품목별 등급에 관한 규정*.  
2. **Evidence Bridging Strategy** – Where foreign data is leveraged, prepare a justification matrix linking each MFDS requirement to the corresponding foreign study/result.  
3. **KGMP Alignment** – Align SOPs with ISO 13485:2016 and MFDS GMP inspection checklists; schedule internal mock audits pre‑submission.  
4. **Labeling Review Loop** – Conduct a Korean‑language review by a certified medical translator, then perform an internal compliance audit against MFDS labeling notice.  

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Level | Immediate Action |
|--------|------------------|-------------------|
| Ambiguity in device class or grade after initial analysis | **RA Manager** | Pause submission; request classification opinion from MFDS (제출 전 사전문의). |
| KGMP audit fails or certificate pending past 30 days before planned submission date | **Quality Assurance Lead** | Initiate corrective action plan; consider alternate certified manufacturing site. |
| Requirement for local clinical data is identified late (≤ 3 months before planned submission) | **Clinical Development Director** | Fast‑track ethical approval and site selection in Korea; allocate budget for expedited trial. |
| Labeling non‑compliance discovered during final dossier check | **Regulatory Affairs Head** | Suspend filing; engage external Korean regulatory consultant for rapid remediation. |

---

### 7. Citations  

- **[1]** “전통 의료기기 체계 – 의료기기법 → 시행령 → 시행규칙 … 식약처 고시: 《의료기기 품목 및 품목별 등급에 관한 규정》, 《의료기기 허가·신고·심사 등에 관한 규정》, 《의료기기 GMP 심사·평가 등에 관한 규정》” – MFDS regulatory hierarchy.  
- **[2]** “MFDS 인허가 상세 가이드 (국내, X‑ray System 전용) > 웹 리서치 교차검증 반영 – 2026‑04‑22 기준” – indicates that X‑ray systems follow the 허가 pathway.  

*No specific identifier found in source — verify separately.*

---

### 8. Reusable RA Judgment (Lesson Learned)

> **When preparing a Korean MFDS submission for a high‑risk device such as an X‑ray system, first confirm the exact product class using the *품목 및 품목별 등급에 관한 규정* before selecting the 허가 vs. 신고 route. The MFDS guidance hierarchy (법률 → 시행령 → 시행규칙 → 식약처 고시) must be explicitly referenced in the dossier to demonstrate regulatory alignment. Additionally, anticipate gaps in local clinical data and KGMP certification early; bridge foreign evidence only after the MFDS has formally accepted OECD‑aligned non‑clinical data or foreign Clinical Evaluation Reports for that class.**  

---

### 9. Peer Review Prompt  

> **To:** RA Team Member (peer)  
> **Subject:** Request for Critical Review – Korean MFDS Classification & Submission Draft  
> **Message:** Please evaluate the assumptions made in this draft, specifically:   
> 1. Is the inferred Class II designation for X‑ray systems justified without a direct reference to the *품목 및 품목별 등급에 관한 규정*?   
> 2. Have we fully captured all MFDS evidence requirements, especially any recent scope expansions for foreign clinical data (e.g., notices issued after 2026‑04‑22)?   
> 3. Are there jurisdiction‑specific gaps—such as Korean post‑market surveillance obligations or unique labeling elements—not addressed here?   
> Your feedback will help ensure the dossier meets MFDS expectations before filing.  

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

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `278735804574527961`

> # MFDS 인허가 상세 가이드 (국내, X-ray System 전용) > 웹 리서치 교차검증 반영 – 2026-04-22 기준

### kb-eval-20260718-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "15f1622f87811ec2", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `15f1622f87811ec2`
- Source: `github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week02_MFDS_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `Week02_MFDS_체계_상세.md`는 `Week02_MFDS_체계_상세.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 --- ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|------...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **MFDS Classification & Licensing Route – Digital Medical Devices (SaMD)**  

---

### 1. Device‐type context extracted from source  
- The Korean Ministry of Food and Drug Safety (MFDS) has introduced a **Digital Medical Device Act (디지털의료제품법)** effective 2025‑01‑24 that redefines SaMD classification and licensing procedures.  
- From 2025‑01‑24 the **National IT Industry Promotion Agency (NIDS)** is authorised to conduct GMP suitability assessments for digital medical devices, supplementing the traditional six designated appraisal bodies (KTL, KTR, KRIBB, KCFST, TÜV SÜD Korea, TÜV Rheinland Korea)【1】.  

These two excerpts constitute the only source material supplied; any further device‑specific details must be obtained from the sponsor.

---

### 2. Regulatory classification & submission route  

| Classification (MFDS risk class) | Typical licensing route | When it applies |
|----------------------------------|--------------------------|-----------------|
| **Class I** (low risk)           | **신고 (Notification)**   | No clinical evaluation required; only basic technical file and Korean labeling. |
| **Class II** (moderate risk)    | **허가 (Approval)**       | Requires full technical dossier, risk management file, possibly limited clinical data. |
| **Class III‑IV** (high risk)    | **허가 (Approval)** – *full*   | Full clinical evaluation (including Korean or accepted foreign CE/FDA data), post‑market surveillance plan, and KGMP certification of the manufacturing site. |

> **How to determine class:**  
> - Review MFDS “Digital Medical Device Classification Guidelines” (released 2025‑05‑07) – AI/ML‑based GUI software may be placed in Class II or higher depending on intended use and risk impact【2】.  
> - If the device performs diagnosis, treatment planning, or therapy delivery, it will likely fall into **Class III**.  

---

### 3. Required evidence (per MFDS current practice)

| Evidence category | Typical content | Korean‑specific notes |
|-------------------|----------------|-----------------------|
| **Technical Documentation** (품질문서) | Device description, specifications, software architecture, IEC 62304 compliance for software, labeling mock‑ups. | Must be in Korean or accompanied by a certified Korean translation. |
| **Risk Management File** | ISO 14971 risk analysis, risk control measures, residual risk justification. | MFDS expects a “위험관리 보고서” written in Korean; any foreign risk assessment must be translated and cross‑referenced. |
| **Clinical Evaluation** | • Clinical trial data (Korean or accepted foreign).  <br>• If using CE/FDA‐cleared predicates, provide the relevant **510(k) / EU MDR** numbers *only if they appear in sponsor documents*; otherwise note “no specific identifier found in source — verify separately”.<br>• For AI/ML devices, include performance verification per the 2025‑05‑07 guideline. | Korean clinical data is mandatory for Class III‑IV unless MFDS accepts foreign data under a specific notice (e.g., Notice 2024‑03‑XX). Verify current notice before relying solely on overseas data. |
| **GMP/KGMP Certification** | GMP suitability assessment report (적합인정서) with 3‑year validity; renewal required. | As of 2025‑01‑24, NIDS may be the assessing body for digital devices【1】. Confirm that the chosen appraisal institution (NIDS, KTL, etc.) is listed on the MFDS approved list. |
| **Labeling & IFU** | Korean language labeling, user manual, safety information, post‑market surveillance plan. | All labeling must be in Korean; any foreign language components require a certified translation and separate Korean version. |
| **Software Verification/Validation** | IEC 62304 lifecycle documentation, traceability matrix, cybersecurity assessment (ISO 27001 reference). | For AI/ML software, include algorithm change management as required by the 2025‑05‑07 guideline【2】. |

---

### 4. Likely missing information (based on source gaps)

| Missing item | Why it matters for MFDS submission |
|--------------|-------------------------------------|
| **Exact intended use / indication** | Determines risk class and depth of clinical evidence required. |
| **Software architecture details (AI/ML model type, data set size)** | Needed to satisfy the new AI/ML‑specific requirements in the 2025‑05‑07 guideline【2】. |
| **Manufacturing location & KGMP status** | GMP suitability assessment must be completed before filing; if NIDS is selected, proof of NIDS approval required. |
| **Korean language labeling draft** | MFDS will reject dossiers lacking Korean labeling/IFU. |
| **Post‑market surveillance (PMS) plan** | Mandatory for Class II‑IV devices; specific PMS activities must be outlined in Korean. |
| **Evidence of compliance with the 2026 anticipated “autonomous performance certification” (선인증 → 후감독)** | If the product falls under that future regime, early alignment may be required. |

---

### 5. Core risk controls to address in the dossier

1. **Design Controls** – Follow IEC 62304 and ISO 14971; document verification/validation activities.
2. **Cybersecurity** – Conduct threat modeling, implement encryption, secure update mechanism; reference Korean “정보보호법” where applicable.
3. **Algorithm Change Management** – Establish a change‑control process for AI model updates (documented in the PMS plan).
4. **Usability/Human Factors** – Perform formative and summative usability testing with Korean users; include findings in the risk file.
5. **GMP/KGMP Controls** – Validate manufacturing processes, environmental monitoring, supplier qualification per KGMP requirements.

---

### 6. Citations (source‑based)

- **[1]** GMP suitability assessment flowchart and NIDS authority introduction (2025‑01‑24) – source excerpt 1078228256164017760.  
- **[2]** Overview of major regulatory changes 2025‑2026, including AI/ML‑focused digital medical device guideline (2025‑05‑07) – source excerpt 1121184088796802935.

*No specific identifier (e.g., 510(k), MDL number) appears in the provided excerpts; verification of such numbers must be performed against sponsor documentation.*

---

### 7. Human‑escalation triggers  

| Trigger | Action required |
|---------|-----------------|
| **Unclear risk class after initial review** | Escalate to senior regulatory lead for classification decision and possible pre‑submission MFDS consultation. |
| **Absence of Korean labeling or IFU draft** | Pause dossier preparation; request translation resources before proceeding. |
| **GMP/KGMP certification not yet issued or NIDS assessment pending** | Halt submission until GMP 적합인정서 is obtained; involve quality assurance to track renewal dates (3‑year validity). |
| **Device utilizes AI/ML and algorithm change plan is missing** | Immediate escalation to product development for establishing a change‑management SOP; cannot finalize PMS plan without it. |
| **Foreign clinical data proposed without a current MFDS notice permitting its use** | Seek clarification from the regulatory affairs manager and possibly request an MFDS pre‑consultation meeting. |

---

### 8. Reusable RA Judgment (Lesson Learned)

> *When evaluating a digital medical device for Korean market entry, always start by verifying the **post‑2025 classification framework** (SaMD guidelines) and confirm which appraisal body (traditional GMP institutes or NIDS) will conduct the KGMP suitability assessment. The presence of AI/ML functionality triggers additional evidence requirements (algorithm validation, change management). Missing Korean language labeling, a valid GMP 적합인정서, or a clear intended‑use statement are immediate stop‑gates that must be resolved before any MFDS 허가 dossier can be compiled.*  

---

### 9. Peer‑review prompt  

> **Dear RA Colleague,**  
> Please review the assumptions and gaps identified above:  
> 1. Have we correctly inferred the applicable classification based solely on the cited regulatory changes, or is additional device‑specific information needed?  
> 2. Are there any recent MFDS notices (post‑2025) that expand acceptance of foreign clinical data which we may have omitted?  
> 3. Does the risk‑control matrix align with Korean PMS expectations for Class II‑IV digital devices, especially concerning AI/ML update procedures?  
> 4. Are there any overlooked language‑or‑translation obligations (e.g., labeling on packaging vs. IFU) that could become a submission blocker?  

Your feedback will help close any jurisdictional gaps before the dossier moves forward.

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

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---
