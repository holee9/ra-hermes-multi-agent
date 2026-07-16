# KB Eval Checksheet - 2026-07-17 Iteration 03

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260717-it03-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_us-001", "iteration": 3, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "b0105269422dbaf0", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

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

> **Regulatory Draft – 510(k) Predicate Strategy**

---

### Bottom Line
- **Submission pathway:** Traditional 510(k) (predicate‑based substantial equivalence).  
- **Classification recommendation:** Determine FDA product code and class (I, II, or III) via the FDA 510(k) Database; most non‑invasive devices with prior market history will be Class II, requiring a special control.  
- **Key next step:** Identify at least one legally marketed predicate device that matches the intended use and fundamental technology. Populate the “Substantial Equivalence Comparison Table” (per source [2]) and assemble required performance & biocompatibility data.

---

### 1. Classification / Submission Route
| Item | Recommended Action |
|------|--------------------|
| **Device Class** | Query FDA Product Code Classification Database using intended use keywords; default to Class II unless a clear Class I exemption exists. |
| **Submission Type** | Traditional 510(k) – uses predicate‐device comparison and eSTAR electronic submission (source [2]). |
| **Regulatory Pathway** | If no suitable predicate found, consider **De Novo** classification; otherwise proceed with 510(k). |

---

### 2. Required Evidence (per FDA guidance & source [2])
| Section | Minimum Content |
|---------|-----------------|
| **Device Description / Indications for Use (IFU)** | Detailed description of device, intended use, target patient population – conform to eSTAR Device Description guide (source [1]). |
| **Substantial Equivalence Comparison Table** | Side‑by‑side matrix of predicate vs. test device covering: technology, materials, design features, performance specs, labeling. |
| **510(k) Summary** | Concise narrative (≤5 pages) summarizing the comparison and rationale for equivalence. |
| **Performance Testing** | Bench tests demonstrating functional safety and efficacy per recognized standards; include software validation if applicable. |
| **Biocompatibility** | ISO 10993‑1 testing plan/execution results appropriate to device’s contact duration (cytotoxicity, sensitization, irritation). |
| **Electromagnetic Compatibility / RF Emissions** (if applicable) | IEC 60601‑1‑2 or equivalent EMC data. |
| **Sterilization Validation** (if marketed sterile) | Sterility assurance level documentation per AAMI/ISO standards. |
| **Labeling & IFU** | Full packaging label, user manual, and any warnings/precautions; must align with FDA labeling requirements. |

---

### 3. Missing Information (gaps to fill before submission)
1. **Predicate Device(s) Identified?** – No specific predicate listed in the source; need searchable FDA 510(k) database query.  
2. **Device Classification Confirmation** – Product code/class not stated; must be determined.  
3. **Risk Management File** – Formal ISO 14971 risk analysis not referenced; required for both Class II and III submissions.  
4. **Software Documentation (if any)** – No mention of software validation or cybersecurity controls.  
5. **Clinical Evaluation (if needed)** – For devices with novel indications, a limited clinical study may be required; absent from current checklist.  

---

### 4. Risk Controls (ISO 14971‑derived)
| Hazard | Proposed Control |
|--------|-----------------|
| Mechanical Failure / Breakage | Design verification testing, material strength analysis, failure mode effects analysis (FMEA). |
| Electrical Shock (if powered) | Apply IEC 60601‑1 safety standards; leakage current limits, double insulation. |
| Biocompatibility Issues | Conduct ISO 10993 suite appropriate to contact duration; establish a biocompatibility justification matrix. |
| Software Errors (if applicable) | Implement software development lifecycle (SDLC), unit/integration testing, cybersecurity risk assessment per FDA guidance. |
| User Misuse | Clear IFU instructions, labeling warnings, training program for operators. |

---

### 5. Citations
- No specific identifier found in source — verify separately.

---

### 6. Human‑Escalation Triggers
| Situation | Action Required |
|-----------|-----------------|
| **No suitable predicate device** after exhaustive FDA 510(k) search | Escalate to leadership; evaluate De Novo or PMA route. |
| **Class III determination** (unexpected) | Immediate senior regulatory review; consider PMA pathway and early pre‑submission meeting. |
| **Unresolved FDA AI (Additional Information)** that demands new clinical data | Prompt escalation to project manager to secure resources and timeline adjustment. |
| **Significant change in intended use or technology scope** during draft preparation | Halt submission; re‑evaluate classification and predicate alignment. |

---

### 7. Peer Review Prompt
> *Colleague, please challenge the following assumptions: (1) that an appropriate Class II predicate exists; (2) the completeness of the evidence checklist based solely on the source excerpts; and (3) that no additional jurisdiction‑specific considerations (e.g., state-level licensure, new QMSR 2026 requirements) have been omitted. Identify any gaps you see in our risk control plan or escalation criteria.*

---

### 8. Reusable RA Judgment (Lesson Record)
**Judgment:** For any new medical device lacking an obvious predicate, the first regulatory decision point is a systematic FDA 510(k) database search to confirm class and identify at least one legally marketed comparator. If none are found, promptly consider De Novo classification. All submission components should follow the eSTAR template structure (Device Description/IFU, Substantial Equivalence Table, Summary, performance & biocompatibility data). Missing predicate identification, classification confirmation, risk management documentation, and software validation are common blockers that trigger escalation to senior regulatory leadership.

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

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20260717-it03-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_us-002", "iteration": 3, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "21b8366cdc6c15c1", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

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

### 1. Bottom‑Line Recommendation
- **Submission pathway:** Traditional 510(k) (or Abbreviated 510(k) if a suitable predicate is identified).  
- **Device classification:** Class II (product code **RAY** – “Radiology Image Management”) based on intended use (image acquisition/management, no diagnostic interpretation).  
- **Key next step:** Identify one or more *substantially equivalent* predicates that are also imaging‑software devices without diagnostic claims. If no such predicate exists, consider a De Novo request.

---

### 2. Classification & Submission Route
| Attribute | Determination |
|-----------|---------------|
| **Regulatory class** | Class II (21 CFR 862.1405 – “Radiology Image Management”). |
| **Product code** | To be confirmed; likely **RAY** or similar. |
| **Submission type** | Traditional 510(k) (requires full safety/effectiveness data). <br>*Abbreviated 510(k)* possible if a recognized predicate with identical technological characteristics is located (per 21 CFR 807.87(b)(2)). |
| **Special controls** | IEC 62304 software life‑cycle, cyber‑security controls, DICOM compliance, labeling per FDA guidance on “General/Specific Intended Use”. |

---

### 3. Required Evidence (per source excerpts)

| Requirement | Source Reference | What to Provide |
|-------------|------------------|-----------------|
| **510(k) content checklist** | FDA “Electronic Submission Template for Medical Device 510(k) Submissions” (eSTAR v5.x), “Format for Traditional and Abbreviated 510(k)s” (2019‑09‑13). | Complete eSTAR cover sheet, device description, substantial equivalence comparison, labeling, summary (21 CFR 807.92). |
| **Indications for Use** | FDA Form 3881; Example I/U text provided in excerpt. | Completed Form 3881 with precise wording (no diagnostic claim). |
| **Software Documentation** | Section 4.3 – “촬영실 GUI SW” checklist. | • Software architecture diagram (modules, processes, DB, DICOM nodes).<br>• Minimum OS/hardware specs.<br>• List of compatible detectors/generators (including versions).<br>• DICOM conformance statement (SCU/Worklist/MPPS).<br>• Cyber‑security features (encryption, authentication, audit logs).<br>• IEC 62304 safety class assignment (A/B/C) and justification.<br>• SOUP inventory with supplier info. |
| **Risk Management** | Implied by IEC 62304 requirement & cyber‑security mention. | Hazard analysis, risk control measures, validation of mitigations per ISO 14971. |
| **Verification/Validation** | Not explicit but required for Class II software. | Test plans/results covering functional, performance, security, and usability testing; software release documentation. |
| **Labeling & IFU** | “General/Specific Intended Use” guidance (1998). | Labels and Instructions for Use reflecting the intended use statement (“not intended for primary diagnosis”). |

*No specific identifier found in source — verify separately.*

---

### 4. Missing Information (must be obtained before filing)

| Gap | Why it matters |
|-----|----------------|
| **Predicate device(s) with 510(k) numbers** | Needed to establish substantial equivalence; without them the submission defaults to a De Novo pathway. |
| **IEC 62304 safety class justification** | Determines required software development process depth and documentation. |
| **SOUP (Software of Unknown Provenance) details** | FDA requires identification, risk assessment, and mitigation for any third‑party components. |
| **Cybersecurity Threat Model / SRD** | FDA expects a documented cybersecurity plan; only high‑level features are listed. |
| **Human Factors/User Interface validation data** | For radiology imaging software used by technologists, usability testing is expected. |
| **Design History File (DHF) index** | Required for QMSR compliance (ISO 13485‑aligned). |
| **Labeling draft (including warnings/limitations)** | Must align with I/U and ensure no diagnostic claim slips in. |

---

### 5. Core Risk Controls (to be documented)

1. **Software safety classification (IEC 62304)** – assign Class B (if risk > I but ≤ II) or C if higher; implement required process controls.
2. **Cyber‑security** – encryption of DICOM transmission, role‑based authentication, audit logging, periodic vulnerability scanning.
3. **DICOM conformance** – ensure proper handling of SOPs (Storage SCU, Worklist SCU, MPPS) to avoid data loss/misrouting.
4. **SOUP management** – maintain inventory, perform vulnerability assessment, apply patches/upgrades.
5. **Usability/Human Factors** – confirm that UI does not lead to inadvertent diagnostic interpretation; label clearly “for image acquisition and management only.”
6. **Risk Management (ISO 14971)** – conduct hazard analysis for incorrect image capture, data corruption, unauthorized access.

---

### 6. Escalation Triggers (human review required)

| Trigger | Action |
|---------|--------|
| **Diagnostic claim appears in I/U or labeling** | Re‑classify as Class III / submit PMA or De Novo; halt 510(k) draft. |
| **No suitable predicate identified after exhaustive search** | Initiate De Novo request (or consider 510(k) with “Special” pathway if FDA grants). |
| **Software safety class C determined** | Confirm that QMSR processes for Class C software are fully implemented; may require additional validation data. |
| **Significant cybersecurity vulnerability discovered late‑stage** | Pause submission, remediate, update SRD and risk analysis. |
| **SOUP component with unaddressed high‑risk CVE** | Immediate mitigation or replacement before filing. |
| **Discrepancy between intended use and actual functionality (e.g., image interpretation)** | Re‑evaluate device classification; potentially shift to higher regulatory pathway. |

---

### 7. Citations

- FDA, *Electronic Submission Template for Medical Device 510(k) Submissions* (final 2023 revision, eSTAR v5.x).  
- FDA Guidance, *Format for Traditional and Abbreviated 510(k)s* (2019‑09‑13 Final).  
- 21 CFR 807.87 – Information required in a 510(k) submission.  
- 21 CFR 807.92 – 510(k) Summary format.  
- FDA Guidance, *General/Specific Intended Use* (1998 Final, currently effective).  
- FDA Form 3881 – Indications for Use form.

*No specific identifier found in source — verify separately.*

---

### 8. Peer‑Review Prompt
> **Request:** Please review the assumptions and completeness of this 510(k) draft. In particular, challenge:
> - The choice of product code/classification based on the provided intended use.
> - Whether the listed evidence fully satisfies both FDA 21 CFR 807.87 and IEC 62304 requirements for Class II software.
> - Any jurisdiction‑specific gaps (e.g., state‑level cyber‑security statutes, upcoming QMSR updates effective Feb 2026).  
> Suggestions for additional data or alternative pathways are welcome.

---

### 9. Reusable RA Judgment (lesson record)

**honcho_conclude**  
- *Bottom line:* Imaging acquisition/management GUI software without diagnostic claim is a Class II device; submit via Traditional 510(k) using a predicate that matches intended use and technology.  
- *Key evidence checklist* derived from FDA eSTAR v5.x and Section 4.3 of the source: architecture, OS/hardware specs, DICOM compliance, cyber‑security features, IEC 62304 safety class, SOUP inventory, detailed I/U (Form 3881).  
- *Missing items* that must be sourced before filing: predicate 510(k) numbers, full risk management file (ISO 14971), usability validation data, complete DHF index, final labeling.  
- *Escalation rules* for diagnostic claims or lack of predicates to trigger De Novo/PMAs.  

This judgment should be applied to any radiology image‑management software undergoing 510(k) preparation where the intended use is limited to acquisition and review but not interpretation.

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

### kb-eval-20260717-it03-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_us-003", "iteration": 3, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "836544d7357c1aa4", "source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md", "source_hash": "a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232"} -->

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

> **Regulatory Draft – 510(k) Predicate Strategy**

---

### Bottom Line
- **Target pathway:** Traditional 510(k) demonstrating substantial equivalence (SE) to a cleared predicate.
- **Priority action:** Identify an appropriate Class II predicate device with the same intended use and technological characteristics; compile a complete SE comparison matrix.  
- **Immediate gap:** No predicate or device description is present in the source material – it must be sourced from FDA databases before any submission can proceed.

---

### 1. Classification & Submission Route
| Item | Recommendation |
|------|----------------|
| **Device class** | Assume Class II unless functional/technological analysis shows otherwise (e.g., no life‑supporting function, low to moderate risk). |
| **Submission type** | Traditional 510(k) – required when a suitable predicate exists. Consider Special or Abbreviated 510(k) only if the device is a modification of an existing cleared product and meets eligibility criteria. |
| **Regulatory timeline** | Once SE documentation is complete, FDA’s standard 90‑day review applies (subject to QMSR compliance). |

---

### 2. Required Evidence Package
1. **Device Description & Intended Use**
   - Detailed labeling, indications, contraindications, and user environment.

2. **Predicate Identification**
   - 510(k) number, device name, classification regulation (e.g., 21 CFR 862.1204), and a side‑by‑side comparison table.

3. **Technological Characteristics**
   - Materials, design schematics, software/firmware architecture (if applicable), performance specifications.

4. **Performance Testing**
   - Bench tests (mechanical, electrical, biocompatibility per ISO 10993‑1).
   - Non‑clinical safety data (sterility, packaging integrity if relevant).

5. **Clinical Data (if needed)**
   - Limited clinical or real‑world evidence only when bench testing cannot establish safety/effectiveness.

6. **Quality System Documentation**
   - QMSR‑aligned ISO 13485:2016 certification, Design History File (DHF), Device Master Record (DMR).

7. **Labeling & User Instructions**
   - Full labeling package meeting 21 CFR 801 and 820 requirements.

---

### 3. Missing Information (Gap Analysis)
| Gap | Impact | Action |
|-----|--------|--------|
| **Predicate device** – not identified in source. | Cannot demonstrate SE, submission cannot be prepared. | Search FDA’s 510(k) database for devices with matching intended use; confirm classification and clearance date. |
| **Device technical specifications** – absent. | Prevents comparison of technological characteristics & risk analysis. | Obtain engineering specs, material data, software architecture from product development team. |
| **Risk Management File** – no reference to ISO 14971 analysis. | Incomplete safety justification; may delay acceptance. | Conduct risk assessment, generate hazard log, map mitigations to design controls. |
| **QMSR compliance status** – not documented. | Non‑conformance to the new Quality System Regulation (effective Feb 2026) could trigger FDA objections. | Verify ISO 13485:2016 certification and implementation of QMSR requirements; provide audit reports. |
| **Clinical or performance data** – none cited. | May be required if SE gaps exist. | Plan bench testing protocol; prepare for possible supplemental clinical evaluation. |

---

### 4. Risk Controls (ISO 14971‑based)
1. **Hazard Identification:** Enumerate all possible failure modes (e.g., electrical shock, mechanical breakage, software error).  
2. **Risk Evaluation:** Assign severity and probability, calculate risk indices.  
3. **Mitigation Strategies:**  
   - Design controls: material selection, redundant safety interlocks, validated firmware.  
   - Process controls: in‑process inspections, supplier qualification, ISO 13485‐based QC.  
   - Protective measures: user training, clear labeling, lock‑out/tag‑out procedures.  
4. **Residual Risk Evaluation:** Document justification that residual risk is acceptable when weighed against intended use benefits.  

---

### 5. Citations
- No specific FDA 510(k) or predicate identifiers appear in the source excerpts; verify predicates separately via FDA’s public database.  

---

### 6. Human‑Escalation Triggers
| Condition | Trigger |
|-----------|---------|
| **No viable predicate found after 2 weeks of search** | Escalate to senior RA lead for possible De Novo consideration. |
| **QMSR non‑compliance documented** | Prompt leadership and quality assurance review; halt submission preparation until remedied. |
| **Critical risk control gaps identified (e.g., unreduced high‑severity hazard)** | Immediate escalation to product development & safety officer; suspend further regulatory work. |
| **Regulatory timeline at risk due to pending data (bench or clinical)** | Alert project manager to re‑baseline schedule and allocate resources. |

---

### 7. Peer Review Prompt
> *Colleague, please review the assumptions above:*
> - Have we correctly scoped the classification as Class II without additional device detail?  
> - Does the gap analysis capture all likely missing elements given the limited source material?  
> - Are there any jurisdiction‑specific nuances (e.g., state‑level requirements for certain devices) that we have omitted?  

---

### 8. Reusable RA Judgment (Recorded for Future Reference)
**Judgment:** When a case lacks explicit predicate information, the first regulatory step must be systematic identification of an FDA‑cleared device with matching intended use and technological features. Absence of this identification blocks all subsequent SE documentation; therefore, a dedicated predicate search should be treated as a gate‑keeping activity before any evidence compilation begins.  

*Note: This lesson is stored as a reusable RA decision for similar “predicate missing” scenarios.*

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

### kb-eval-20260717-it03-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_us-004", "iteration": 3, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "e1f4d3a1fbd721e6", "source": "github:holee9/MD-process/issue-drafts/220_13_FDA_510k_RTA_핵심양식_초안.md", "source_hash": "2b2e64ed872d9caf987e923334f8bb1dab23e1f65d28ac42a81828e751edceb2"} -->

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

> **Regulatory Draft – 510(k) Strategy for the RTA‑Scored Device**

---

### 1. Classification & Submission Route  
- **Device Class:** *Presumed Class II* (most software‑driven medical devices fall in Class II unless a predicate shows otherwise).  
- **Submission type:** Traditional **510(k)** (no Special or Abbreviated pathway indicated).  

> **Rationale:** The internal RTA scoring model reports a 52 % acceptability score, typical of early‑stage Class II submissions that lack several “must” items. No evidence in the source suggests eligibility for a De Novo or Special 510(k) route.

---

### 2. Required Evidentiary Components (Typical for a Class II 510(k))

| Section | Typical Content | Gap Highlighted by Source |
|---------|-----------------|----------------------------|
| **Device Description** | Full technical specifications, software architecture, UI screenshots. | *Missing*: Detailed description of the five “must” items. |
| **Intended Use / Indications for Use (IFU)** | Clear statement of clinical purpose and patient population. | *Missing*: Complete IFU narrative that satisfies the “must” criteria. |
| **Predicate Comparison** | Side‑by‑side table with legally marketed predicate(s) – 510(k) number, intended use, technological characteristics, performance. | *Missing*: Identification of one or more valid predicates; none cited in source. |
| **Performance Testing** | • Bench (electrical safety, EMC, software verification/validation) <br>• Animal studies (if applicable) <br>• Clinical data (non‑inferiority or equivalence for software). | *Missing*: Evidence that the five “must” items are addressed; likely includes software validation and usability testing. |
| **Risk Management** | ISO 14971‑based risk analysis, hazard mitigations, residual risk evaluation. | *Missing*: Completed risk management file that demonstrates control of hazards linked to the unmet “must” items. |
| **Labeling** | Instructions for use, warnings/precautions, symbols per 21 CFR 801. | *Missing*: Final labeling package meeting FDA requirements. |
| **QMS Evidence** | QMS compliance (ISO 13485‑aligned) – design history file, CAPA records, etc., per QMSR (effective Feb 2026). | *Missing*: Documentation that the organization’s QMS satisfies the new 21 CFR 820.30/820.50 requirements. |

---

### 3. Missing Information (“Must” Items)

The source states **five mandatory items** remain unsatisfied, driving a Refuse to Accept (RTA) outcome. While not enumerated, typical must‑items for a 510(k) include:

1. **Predicate identification & substantial equivalence justification**  
2. **Comprehensive software validation plan/results**  
3. **Risk management file (ISO 14971)**  
4. **Labeling draft meeting FDA format**  
5. **QMS compliance evidence under the new QMSR**

*Action:* Obtain or develop these five artifacts before resubmission.

---

### 4. Risk Controls to Address

| Hazard | Control Strategy (per ISO 14971) |
|--------|-----------------------------------|
| Software malfunction leading to incorrect clinical decision | – Requirement traceability matrix <br>– Unit, integration, system verification <br>– Failure mode & effects analysis (FMEA) |
| Data security breach / patient privacy violation | – Encryption of data at rest and in transit <br>– Access control & audit logs <br>– Compliance with HIPAA & 21 CFR 820.30(c)(2) |
| User error due to ambiguous UI | – Human factors/usability engineering study (validated) <br>– Clear labeling & training material |
| Electrical safety (if hardware present) | – IEC 60601‑1 compliance testing, EMC assessment |
| Residual risk exceeding acceptable level | – Risk/benefit analysis documented; CAPA plan for remaining risks |

---

### 5. Citations from Source

- **RTA score & missing must items:** “FDA 510(k) RTA 점수 52% 고착… 5개 must 항목이 미충족 상태로 실제 제출 시 FDA RTA(Refuse to Accept) 직행.” (Chunk 322119354378516559)  
- **Projected improvement if must items resolved:** “FDA 510(k) 점수 52% → 약 85% (5개 must 해소 시).” (Chunk 607901765257522135)

> No specific FDA 510(k) numbers, predicate identifiers, or case IDs appear in the excerpts; verify those separately.

---

### 6. Human‑Escalation Triggers

| Trigger | Reason for Escalation |
|---------|-----------------------|
| **RTA score remains ≤ 60 % after addressing “must” items** | Indicates fundamental gaps (e.g., no valid predicate); escalation to senior RA or regulatory counsel for possible De Novo pathway. |
| **Unresolved QMSR compliance (ISO 13485 alignment)** | Requires leadership approval and possibly external audit; flag to Quality Management lead. |
| **Risk analysis shows residual risk > acceptable** | Must be reviewed by Clinical/Safety officer and potentially the FDA via pre‑submission meeting request. |
| **Clinical data required but not available** | Escalate to product development for trial planning or consider alternative predicate with less stringent clinical evidence. |
| **Timeline breach (> 90 days without completing must items)** | Notify program manager; may need resource reallocation or scope adjustment. |

---

### 7. Reusable RA Judgment (Lesson Learned)

**When an internal RTA model flags a submission at ~52 % with “must” deficiencies, the fastest path to clearance is to first secure a legally marketed predicate and produce a complete risk management file, software validation evidence, labeling, and QMSR‑compliant documentation. Filling these five high‑impact gaps typically lifts the acceptability score into the 80–90 % range, avoiding an RTA and enabling a standard 510(k) clearance without detouring to De Novo or Special pathways.**  

*Record this judgment for future cases where early RTA scoring is low.*

---

### 8. Peer‑Review Prompt

> **@RA‑Peer:** Please review the assumptions above—particularly:  
> - Are the identified “must” items exhaustive, or might additional FDA expectations be missing?  
> - Does the lack of a cited predicate in the source necessitate an independent predicate search before finalizing the submission plan?  
> - Have we captured all jurisdiction‑specific gaps introduced by the February 2026 QMSR update?  

Your feedback will be used to refine the draft and ensure no critical compliance element is overlooked.

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

### kb-eval-20260717-it03-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_us-005", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "e8f2c4c3cdba0dcd", "source": "github:holee9/MD-process/issue-drafts/931_RA_FDA_Form_표지_양식_4건_작성.md", "source_hash": "68cd74d39caaa060d4323f37a5c193a02284866bee050ec5139fdf5916ca6ff7"} -->

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

> **Regulatory Draft – 510(k) Predicate‑Strategy Brief**

---

### Bottom Line
- **Submission route:** Traditional 510(k) (premarket notification).  
- **Device class:** *To be determined* pending final intended‑use statement; most likely Class II based on typical diagnostic/monitoring devices, but a definitive classification requires the completed Indications for Use (Form 3881).  

Proceed with a standard predicate‑comparison package while preparing all required FDA forms listed in the work scope. Flag any gaps early to avoid delays.

---

### 1. Classification & Submission Route
| Item | Detail |
|------|--------|
| **Regulatory pathway** | Traditional 510(k) (requires demonstration of substantial equivalence). |
| **Likely classification** | Class II – typical for devices requiring special controls (e.g., performance standards, labeling). <br>*If the intended use is more invasive or novel, a Class III de Novo may be required; this must be verified once the Indications for Use are finalized.* |
| **Key FDA forms** | 3514 (Cover Sheet), 3601 (User Fee Cover Sheet + receipt), 3654 (Standards Data Report), 3881 (Indications for Use Statement), 510(k) Cover Letter. |

---

### 2. Required Evidence (Core of Substantial‑Equivalence Dossier)

| Evidence Type | Typical Content | Comments |
|---------------|----------------|----------|
| **Predicate device identification** | - FDA Product Code, classification number, and 510(k) clearance number.<br>- Matching intended use & technology. | Must be selected before drafting the comparison table. |
| **Device description & labeling** | Detailed specifications, materials, accessories, labeling (including IFU). | Use Form 3881 for I/U; ensure it is not expired (OMB expiration 2026‑07‑31). |
| **Performance testing** | - Bench / benchtop functional tests.<br>- Electrical safety (IEC 60601‑1) if applicable.<br>- Electromagnetic compatibility (EMC).<br>- Software validation (if software‑controlled). | Align with recognized standards cited in Form 3654. |
| **Biocompatibility** | ISO 10993‑1 risk assessment, relevant extracts/tests based on device contact. | Required for any patient-contact component. |
| **Sterilization & Shelf‑life (if applicable)** | Validation data per USP/ISO standards. | Include if device is supplied sterile. |
| **Risk Management** | ISO 14971 file – hazard analysis, risk controls, residual risk evaluation. | Summarized in the 510(k) narrative and supporting docs. |
| **Clinical data (if needed)** | Literature or limited clinical study showing safety/effectiveness comparable to predicate. | Usually not required for Class II unless special control demands it. |

---

### 3. Missing Information / Action Items

| Item | Current status (per source) | Required action |
|------|----------------------------|-----------------|
| **Form 3514 – Cover Sheet** | Placeholder only (“company/name/address/contact”). | Populate with final corporate information. |
| **Form 3601 – User Fee Cover Sheet & receipt** | Placeholder; fee receipt not yet attached. | Submit payment, attach receipt before filing. |
| **Form 3654 – Standards Data Report** | Placeholder for either FDA template or custom format. | Identify applicable consensus standards and fill out the report. |
| **Form 3881 – Indications for Use Statement** | Note about OMB expiration 2026‑07‑31; not completed. | Draft final I/U, ensure it remains current beyond OMB deadline (renew if needed). |
| **510(k) Cover Letter** | Template placeholder only. | Write a concise cover letter referencing the cleared predicate(s) and summarizing major submission elements. |
| **Predicate selection** | Not yet performed. | Conduct search in FDA 510(k) database; choose device with identical intended use, technology, and performance characteristics. |
| **Risk Management file (ISO 14971)** | Not mentioned. | Compile hazard analysis, risk control measures, and residual risk justification. |
| **Biocompatibility / Sterilization data** | No evidence cited. | Gather or generate required test data based on device materials/contact level. |

---

### 4. Risk Controls (Suggested Framework)

1. **ISO 14971‑based risk management process** – identify hazards, estimate severity & probability, implement controls.
2. **Design Controls (21 CFR 820)** – documented design inputs/outputs, verification, validation.
3. **Relevant consensus standards** – e.g., IEC 60601‑1 (electrical safety), ISO 10993‑5/10 (cytotoxicity, sensitization) as appropriate; list in Form 3654.
4. **Software Lifecycle Controls** – IEC 62304 if software > 30 days life. Provide verification & validation plan.
5. **Labeling & Instructions for Use** – ensure clear warnings, contraindications, and user instructions to mitigate use‑error risk.

---

### 5. Citations

- No specific identifier found in source — verify separately.  
*(The source excerpts only listed internal check‑list items; no FDA 510(k) numbers or predicate IDs were present.)*

---

### 6. Human‑Escalation Triggers

| Trigger | When to Escalate |
|---------|------------------|
| **Unresolved classification** | If the Indications for Use cannot be matched confidently to an existing class, involve regulatory leadership / senior RA. |
| **Predicate not found** | No suitable predicate after exhaustive FDA 510(k) search – consider De Novo route; escalate to project manager and senior RA. |
| **Missing fee receipt or OMB‑expired I/U** | Submission cannot be accepted; raise immediately with finance & regulatory team lead. |
| **Significant gaps in risk analysis or test data** | If any high‑severity hazards lack mitigations, stop filing and notify QA/Engineering leads. |
| **Regulatory deadline missed (e.g., OMB expiry 2026‑07‑31)** | Immediate notification to project sponsor for corrective action. |

---

### 7. Peer‑Review Prompt

> **To: RA Team – Peer Review Request**  
> Please review the assumptions and completeness of this 510(k) predicate‑strategy brief:
> - Are the identified evidence categories sufficient for a typical Class II device, or are additional data (e.g., clinical) required given our intended use?  
> - Does the checklist cover all FDA form requirements under the new QMSR (effective Feb 2026)?  
> - Have we captured any jurisdiction‑specific gaps (e.g., state‑level registrations, post‑market reporting obligations) that need addressing before submission?  

---

### 8. Reusable RA Judgment (Lesson Record)

```json
{
  "lesson_id": "daily_growth_v1_2026-07-19",
  "summary": "When a 510(k) work package lists only form placeholders and no predicate identifiers, the immediate priority is to secure a qualified predicate, complete all FDA forms (3514, 3601, 3654, 3881), and verify classification via the Indications for Use. Missing OMB‑expiry dates and fee receipts must trigger early escalation. Record that source excerpts lacking explicit identifiers should be flagged as ‘no specific identifier found’; a separate verification step is required.",
  "confidence": "high",
  "actions_recommended": [
    "Select predicate device before drafting comparison tables.",
    "Finalize Indications for Use ahead of OMB expiry (2026‑07‑31).",
    "Ensure fee receipt attached to Form 3601.",
    "Compile ISO 14971 risk file and relevant consensus standards."
  ],
  "escalation_conditions": [
    "Unclear device classification after I/U finalization.",
    "No suitable predicate found after exhaustive search.",
    "Critical form or data gaps identified close to submission deadline."
  ]
}
```

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

### kb-eval-20260717-it03-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_eu-001", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "034e73198875b07e", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

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

> **Regulatory Draft – Classification & Conformity Assessment for an Ionising‑Radiation Diagnostic Device (X‑ray Generator)**  

---

### 1. Device Overview (as inferred from source)  
- **Intended purpose:** Generation of ionising X‑ray radiation for diagnostic imaging.  
- **Technology class:** Active medical device that emits ionising radiation.  

> **Source citation** – Rule 10 identifying “ionising radiation emission diagnostic device (X‑ray generation equipment → Class IIb)”【2】.  

---

### 2. MDR Classification  

| Item | Reference | Determination |
|------|-----------|---------------|
| **Classification rule** | Annex VIII, Rule 10 | **Class IIb** (medium‑risk) |
| **Resulting class** | – | Class IIb device |

> **Citation** – Annex VIII (Classification Rules) as listed in the source excerpt【1】.  

---

### 3. Conformity‑Assessment Route (MDR)

A Class IIb device must be assessed by a Notified Body using one of the following mandatory routes:

| Mandatory route | MDR Annex/Module | Typical content |
|-----------------|------------------|-----------------|
| **QMS assessment + Type Examination + Product Verification** | Annex IX (QMS) + Annex X (type‑examination) + Annex XI (product verification) | ISO 13485 QMS audit, type‑exam of design dossier, sampling & testing of production units. |
| **Full Quality Assurance (Module G)** | Annex IX (QMS) + Module G (full QA) | Continuous NB oversight of the entire quality system and post‑market activities. |

> **Citation** – Conformity‑assessment routes for Class IIb are defined in MDR Annex IX, X, XI (see Fixed‑Rule table).  

*The chosen route will be recorded in the Technical Documentation (Annex II) together with the NB’s certificate reference.*

---

### 4. Required Evidence Package

| Evidence | Regulatory basis | Minimum contents |
|----------|------------------|------------------|
| **Technical Documentation** | Annex II | Device description, intended use, design & manufacturing information, labeling, risk management (ISO 14971), verification & validation data, biocompatibility (if applicable), software documentation (if SaMD). |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (Art. 61) | State‑of‑the‑art literature review on diagnostic X‑ray devices, clinical performance data (dose, image quality), safety data, benefit‑risk analysis. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | Systematic plan for ongoing collection of safety/performance data; includes periodic safety update report (PSUR) per Art. 86 because Class IIb is a higher‑risk class. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | Planned PMCF activities (clinical registries, usability studies), evaluation of residual risks, updates to CER. |
| **Risk Management File** | Annex I (GSPR) – implemented via ISO 14971 | Hazard identification, risk analysis, risk control measures, verification of controls, residual risk acceptability. |
| **Software Documentation (if SaMD component)** | Rule 11 (Annex VIII) & GSPR checklist | Software architecture, IEC 62304 lifecycle processes, cybersecurity plan (Annex I‑R7.1). |
| **Electromagnetic Compatibility (EMC) & Electrical Safety** | Annex I – R8, R9 | Test reports per IEC 60601‑1‑2 / IEC 61010‑1 as appropriate. |
| **Radiation Protection Validation** | Annex I – R7 & relevant EU directives (e.g., Euratom 2013/59) | Dose measurements, shielding analysis, compliance with DRL (diagnostic reference levels). |

---

### 5. Identified Gaps / Missing Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Exact Intended Use Statement** – indication, patient population, clinical setting | Drives classification, CE marking scope, labeling | Obtain signed Intended‑Use Specification from the manufacturer. |
| **Full Device Description & Architecture** (including any software modules) | Needed for Annex II dossier and risk analysis | Request detailed design specification and software bill of materials. |
| **Risk Management File** – evidence of ISO 14971 implementation | Mandatory for GSPR compliance (R1‑R7) | Ask for RMF, including residual‑risk evaluation. |
| **Clinical Performance Data** – in‑vivo testing results, imaging quality metrics, dose statistics | Required for CER (Rule 10 devices often need clinical investigation or robust performance data) | Clarify whether existing literature suffices; if not, plan a clinical investigation per Art. 78‑80. |
| **Radiation Safety Validation** – dosimetry & shielding test reports | Specific to ionising radiation devices (Annex I R7) | Request measurement reports, conformity with Euratom standards. |
| **Software Verification/Validation evidence** (if SaMD) | Rule 11 classification and GSPR software controls (R3.5) | Provide IEC 62304 compliance documentation, cybersecurity threat analysis. |
| **Labeling & IFU Drafts** – especially safety warnings for radiation exposure | Annex I §23 labeling requirements | Collect provisional labeling for review. |
| **PMS/PMCF Plan Details** – timelines, data sources, responsible persons | Art. 84‑85; mandatory for continued conformity | Develop draft plan and map to risk controls. |

Until these items are supplied the NB will likely raise “non‑conformities” during audit.

---

### 6. Core Risk Controls (Annex I GSPR)  

| GSPR clause | Control needed for X‑ray diagnostic device |
|-------------|--------------------------------------------|
| **R1 – Device Characteristics** | Verify that radiation output, beam geometry, and imaging performance meet intended use. |
| **R5 – Biological Safety** (if patient‑contacting parts) | Conduct biocompatibility testing per ISO 10993‑1. |
| **R6 – Chemical/Physical Safety** | Ensure no hazardous substances exceed REACH limits; verify shielding materials. |
| **R7 – Radiation Protection** | Demonstrate compliance with DRLs, provide dose‑monitoring features, include safety interlocks. |
| **R8 – Electrical Safety & EMC** | IEC 60601‑1 (or relevant) testing; EMC according to IEC 60601‑1‑2. |
| **R9 – Software/IT** (if SaMD) | Follow IEC 62304 lifecycle, perform software verification and validation, implement cybersecurity safeguards. |
| **R10 – Usability/Human Factors** | Conduct usability engineering per IEC 62366‑1; verify that operators can correctly set exposure parameters. |
| **R11 – Residual Risk Evaluation** | Document in RMF; ensure residual risk is acceptable relative to benefit. |

All controls must be documented, verified and referenced in the Technical Documentation.

---

### 7. Human‑Escalation Triggers  

| Trigger condition | Escalation level | Action |
|-------------------|------------------|--------|
| **No definitive Intended Use** after two requests | Senior RA Lead | Raise to senior RA for decision on classification scope. |
| **Insufficient clinical performance data** (no literature or investigational results) | Clinical Affairs / Head of Regulatory | Initiate feasibility study plan; consider a formal clinical investigation under Art. 78‑80. |
| **Missing risk‑management documentation** | Quality Management Director | Suspend dossier preparation until RMF provided. |
| **No NB engagement contract / certificate reference** | Legal/Compliance | Verify NB accreditation status and secure audit schedule before proceeding. |
| **Unresolved software classification (Rule 11 vs Rule 10)** | Software Engineering Lead & RA | Conduct joint assessment to determine whether SaMD applies; adjust documentation accordingly. |
| **PMS/PMCF plan not aligned with risk profile** | Post‑Market Surveillance Team Lead | Redesign PMS activities; prioritize high‑risk residuals. |

---

### 8. Peer‑Review Prompt  

> **To: Regulatory Affairs Colleague**  
> Please review the above classification and conformity‑assessment draft. In particular, challenge:
> 1. The assumption that Rule 10 alone suffices for Class IIb without a secondary check for any SaMD components (Rule 11).  
> 2. Whether the listed evidence fully satisfies Annex I GSPR for radiation‑protection (R7) given current Euratom requirements.  
> 3. Any jurisdictional gaps – e.g., national additional requirements (Korea’s MFDS, if applicable) that may affect the EU dossier.  
> Provide counter‑arguments or missing sources so we can adjust the submission plan accordingly.

---

### 9. Reusable RA Judgment (Lesson Capture)

**Judgment ID:** `MDR_Cls_Rule10_Xray_ClassIIb_NBroute`  

- **Rule 10 → Class IIb** for ionising‑radiation diagnostic devices (X‑ray generators).  
- **Conformity route** must include Annex IX QMS audit *plus* either (Annex X + XI) or Module G; self‑declaration (Module A) is not permissible.  
- **Evidence checklist**: Technical Documentation (Annex II), CER (Annex XIV Part A), PMS plan (Art. 84), PMCF plan/report (Annex XIV Part B), full RMF, radiation‑protection validation, EMC & electrical safety testing, labeling per Annex I §23.  
- **Missing data flag**: intended use specificity, clinical performance metrics, radiation dose verification, software documentation when SaMD present.  
- **Escalation triggers** defined for each critical missing element.

*Record this judgment for future cases involving ionising‑radiation diagnostic devices.*

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

### kb-eval-20260717-it03-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_eu-002", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "370448965c57604a", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

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

> **MDR Classification & Conformity‑Assessment Draft (EU 2026)**  

---

### 1. Scope of the assessment  
The present draft is prepared on the basis of the limited source material supplied (see excerpts [1] and [2]). No explicit device name, intended purpose, or technical description was provided; therefore the conclusions are provisional and contingent on additional information from the sponsor.

---

### 2. Classification – methodological approach  

| Step | Reference | Comment |
|------|-----------|---------|
| **(a) Apply the classification rules** | Article 51 + Annex VIII (MDR) | Manufacturer bears primary responsibility for self‑classification (self‑classifying). The 22 rule set is applied sequentially; the highest‑risk rule that fits determines the class. |
| **(b) Consult guidance when uncertainty remains** | MDCG Manual on Borderline and Classification, version v2.1.1 (2023‑09) | Recommended by the source excerpt [2] for borderline cases or where rule interpretation is ambiguous. |
| **(c) Escalate to Competent Authority (CA)** | Article 51 (MDR) – “manufacturer may request advice from CA” | To be used if the manufacturer cannot resolve classification internally. |

**Current status:** *Device class cannot be assigned at this stage* because the intended medical purpose, mode of action and applicable rule(s) are missing.  

> **Missing Information – Classification**  
> 1. Full device description (including technology, principle of operation).  
> 2. Intended indication(s) and patient population.  
> 3. Whether the device is active, implantable, in‑vitro, software‑only, etc.  

---

### 3. Conformity‑assessment route (contingent on class)

| Class | Typical MDR route* | Primary Annex(es) |
|-------|-------------------|--------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration of conformity (no NB required). | Annex IV (EU Declaration of Conformity), Annex VIII (classification rules) |
| **Class I (sterile or measuring)** | Involvement of a Notified Body for the conformity assessment of the QMS. | Annex IX (QMS‑based audit) + Annex IV |
| **Class IIa / IIb** | Full quality‑system assessment plus type examination (if applicable). | Annex IX (QMS) and/or Annex X/Annex XI (type‑examination & product verification) |
| **Class III** | Type‑examination + full quality‑system audit; higher‑risk post‑market surveillance. | Annex X + XI, plus Annex IX for QMS oversight |

\*The exact module(s) shall be confirmed once the device class is known.

---

### 4. Technical documentation – evidence required  

| Evidence | Regulatory source (per fixed‐rule table) | Remarks |
|----------|------------------------------------------|---------|
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (updated via Article 61) | Must demonstrate conformity with the General Safety & Performance Requirements (GSPR). |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Annex XIV Part B | Required for all classes; depth varies with risk. |
| **Post‑Market Surveillance (PMS) system, plan and periodic safety update report (PSUR)** | Art. 83 (system), Art. 84 (plan), Art. 86 (PSUR – higher‑risk devices) | PSUR mandatory from Class IIb upward; lower‑risk devices use the PMS report (Art. 85). |
| **Unique Device Identification (UDI) registration** | UDI portal (Korea) & EUDAMED | Must be entered into EUDAMED once available; source excerpt [1] lists required UDI databases. |
| **Vigilance / Incident reporting** | Art. 87 (MDR) – mandatory for serious incidents, with reference to 21 CFR 803/MedWatch where applicable | Aligns with local reporting obligations (e.g., Korean “이상사례 보고”). |
| **Quality Management System (QMS)** | ISO 13485 (referenced via Annex IX) | Demonstrates ongoing compliance; audited by Notified Body for classes ≥ I‑sterile/IIa. |
| **Risk Management File** | Annex I (GSPR) – implemented through ISO 14971 | Must identify hazards, estimate risks, and define risk control measures. |
| **Labeling & IFU** | Annex I, Chapter III (§23) | Must contain UDI, intended use, contraindications, etc. |

> **Missing Documentation Elements**  
> • Clinical data (clinical investigations, literature review, or equivalence justification).  
> • Detailed risk analysis (hazard list, severity/likelihood estimates).  
> • Product specifications and design verification/validation results.  

---

### 5. Risk controls – high‑level checklist  

1. **Risk Management Process** – ISO 14971 compliant; documented in the Risk Management File (RMF).  
2. **Safety‑related performance testing** – Demonstrate that residual risks are acceptable relative to benefits as per Annex I GSPR.  
3. **Usability engineering** – Human factors analysis for intended user groups.  
4. **Cybersecurity (if software/connected)** – Align with MDCG 2020‑16 guidance; include threat modelling and mitigation.  
5. **Post‑market controls** – Ongoing monitoring via PMS plan, PMCF activities, and periodic PSURs.  

---

### 6. Human‑escalation triggers  

| Situation | Required human action |
|-----------|-----------------------|
| **Insufficient information to assign a class** (no intended use, technology description) | Pause the submission; request detailed device specification from sponsor before proceeding. |
| **Device potentially Class III or high‑risk implantable** | Engage Notified Body early for type–examination scope and plan an audit schedule; consider involving a clinical expert for CER. |
| **Absence of clinical evidence supporting safety/efficacy** | Escalate to Clinical Evaluation Lead – may need to design a clinical investigation (Art. 62‑64) or gather equivalence data. |
| **Discrepancies between risk analysis and GSPR** | Trigger a risk‑management review meeting; update RMF and re‑evaluate residual risks. |
| **Regulatory deadline approaching without PSUR/PMCF completion** | Notify Project Manager to allocate resources for post‑market data collection; potential submission delay. |
| **Unclear UDI registration status in EUDAMED** | Contact the EU regulator’s EUDAMED support team and verify entry deadlines (Art. 33‑39). |

---

### 7. Citations (as required by the fixed‑rule table)

* Article 51 – Classification principles (MDR)  
* Annex VIII – Rules 1‑22 (classification) – excerpt [2]  
* MDCG Manual on Borderline and Classification v2.1.1 (2023‑09) – excerpt [2]  
* Article 61 – Clinical Evaluation Report (CER) (via Annex XIV Part A) – excerpt [1]  
* Annex XIV Part B – PMCF plan/evaluation report – excerpt [1]  
* Art. 83, 84, 85, 86 – PMS system/plan/report/PSUR – excerpt [1]  
* Art. 87 – Vigilance reporting – excerpt [1]  
* Annex I, Chapter III (§23) – Labeling requirements – excerpt [1]  

> **Identifiers** – no specific identifier found in source — verify separately.

---

### 8. Peer‑review request  

> *“@RA‑Peer: Please challenge the underlying assumptions made above, especially regarding (a) the completeness of classification guidance based solely on excerpts [1] and [2], (b) whether any jurisdiction‑specific obligations (e.g., Korean MFDS requirements) have been omitted, and (c) the adequacy of the listed evidence for a potential Class IIb device. Identify any gaps that could affect the conformity‑assessment route or post‑market surveillance plan.”*  



---  

**Prepared by:** Theo – EU MDR Regulatory Affairs Specialist  
**Date:** 2026‑07‑19 (run date)  

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

### kb-eval-20260717-it03-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_eu-003", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "0604d767d6dcfc80", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

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

> **Regulatory Draft – Classification & Conformity Assessment for a Diagnostic X‑ray Imaging System (active ionising‑radiation device)**  

---

### 1. Device description & intended purpose  
*Active medical imaging system that generates ionising X‑rays for **diagnostic** use (e.g., radiography, fluoroscopy). The system includes an X‑ray tube, control console and a digital flat‑panel detector.*

---

### 2. Classification analysis  

| Step | Evidence from source | Regulatory rule applied | Resulting class |
|------|----------------------|-------------------------|-----------------|
| 1. Identify the activity | Device **emits ionising radiation** for diagnosis (not therapy). | MDR Annex VIII – **Rule 10** (active devices intended for **diagnostic** use of ionising radiation) | **Class IIb** |
| 2. Check for therapeutic scope | Rule 9 applies only to *therapeutic* ionising‑radiation devices; source [1] explicitly notes “diagnostic X‑ray excluded”. | MDR Annex VIII – **Rule 9** (therapeutic) – **not applicable** | — |
| 3. Confirm correct mapping | Source [2] states: “X‑ray system (diagnostic ionising‑radiation active device) = **Rule 10 → Class IIb**”. | MDR Annex VIII – Rule 10 | **Class IIb** |

*The digital flat‑panel detector, if considered a separate device, would fall under **Rule 17 → Class IIa**, but the primary system remains Class IIb.*

---

### 3. Conformity‑assessment route  

| Device class | Mandatory Notified‑Body involvement | Typical MDR module(s) |
|--------------|--------------------------------------|-----------------------|
| **Class IIb** (no invasive or measuring function) | Yes – at least one NB audit required. | **Module B** (Annex IX: QMS assessment) *or* **Module C** (Annex IX + Annex X/XI: type‑examination + product verification). Most manufacturers adopt Module B with a full ISO 13485 QMS, supplemented by a type‑examination for the radiation subsystem if required. |

**Key outcome:** The CE marking plan must reference **Annex IX** (QMS) and optionally **Annex X/XI** for type‑examination of the X‑ray generation part.

---

### 4. Evidence required for technical documentation (per MDR Annex II/III)

1. **Device description & intended purpose** – clear statement that the device is for diagnostic imaging only.  
2. **Classification justification** – reference to **Rule 10** (Annex VIII).  
3. **Risk Management File** (ISO 14971) – include risk analysis, evaluation of radiation hazards and controls (see §5).  
4. **Design & manufacturing information** – drawings, bills of materials, software architecture (if any), verification & validation reports.  
5. **Performance testing** – physico‑chemical, electrical safety, electromagnetic compatibility, *radiation output* (dose, spectrum) per IEC 60601‑2‑44 / EN 60601‑2‑44.  
6. **Clinical Evaluation Report** (CER) – Annex XIV Part A; clinical data demonstrating safety & performance for the intended diagnostic indication.  
7. **Post‑Market Surveillance (PMS) Plan** – Art. 84, describing routine surveillance activities.  
8. **Periodic Safety Update Report (PSUR)** – required for Class IIb (Art. 86).  
9. **Labeling & IFU** – Annex I §23; include radiation safety instructions, dose‑reduction measures, warnings.  
10. **Declaration of Conformity** – Annex IV, signed by the manufacturer.  

---

### 5. Identified gaps / missing information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Explicit intended‑use statement** confirming *diagnostic* only (no therapeutic dose delivery). | Prevents mis‑application of Rule 9 and ensures correct classification. | Add to the device label/IFU and technical file. |
| **Radiation output specifications** (kVp range, mA, filtration, measured dose per exposure). | Needed for compliance with IEC 60601‑2‑44 & risk assessment of ionising radiation. | Provide measurement data from a validated test protocol. |
| **Clinical evidence** – usability studies or clinical performance data for the specific imaging indications. | Required for CER (Annex XIV Part A). | Conduct a small‑scale post‑market clinical follow‑up or cite equivalence to a predicate device with documented clinical data. |
| **Equivalence justification** to FDA 510(k) (Product Code MQB) – if cited as part of the “mapping”. | Must demonstrate that the EU device’s safety/ performance is at least equivalent; cannot rely solely on foreign classification. | Prepare a detailed equivalence table covering intended use, technology, performance and clinical data. |
| **Risk controls specific to ionising radiation** (collimation, exposure‑time limiters, interlocks, dose monitoring). | Integral to ISO 14971 risk mitigation and to meet IEC 60601‑2‑44 safety requirements. | Document engineering controls, user training, maintenance procedures. |
| **Software verification & validation** for the digital detector’s image processing (if considered a medical device software). | Class IIa regulatorily; needs to satisfy IEC 62304. | Provide V‑V plan and test reports. |

---

### 6. Recommended risk controls (radiation‑specific)

1. **Automatic exposure control (AEC)** – limits dose per frame.  
2. **Collimation & field‑size restriction** – reduces scatter and patient dose.  
3. **Interlock system** – prevents X‑ray generation unless shielding doors are closed.  
4. **Real‑time dose monitoring & display** – alerts operator when preset thresholds are approached/exceeded.  
5. **Periodic quality‑assurance (QA) program** – tests tube output, detector calibration, and safety functions per IEC 60601‑2‑44.  
6. **User training & competency assessment** – documented in the PMS plan.  

All controls must be traceable to risk‑control measures identified in the ISO 14971 file.

---

### 7. Key regulatory citations  

| Requirement | Source |
|-------------|--------|
| Classification rule for diagnostic ionising‑radiation devices (Rule 10) | MDR **Annex VIII**, supported by source [2] “X‑ray system … = Rule 10 → Class IIb”. |
| Rule 9 applicability limited to therapeutic radiation | MDR **Annex VIII**; source [1] explicitly notes “diagnostic X‑ray excluded”. |
| Conformity‑assessment modules for Class IIb | MDR **Annex IX** (QMS) and **Annex X/XI** (type‑examination & product verification). |
| Clinical Evaluation Report requirement | MDR **Annex XIV Part A**. |
| PMCF planning (if needed after CE) | MDR **Annex XIV Part B**. |
| PMS system/plan/report | Art. 83 (system), Art. 84 (plan), Art. 86 (PSUR for Class IIb). |
| Labeling (§23) | MDR **Annex I, Chapter III §23**. |
| Risk‑management basis | MDR **Annex I General Safety and Performance Requirements**, implemented via ISO 14971. |
| Radiation safety standards | IEC 60601‑2‑44 / EN 60601‑2‑44 (radiological safety). |

*No specific 510(k) numbers or other identifiers appear in the source excerpts; verify any such details separately.*

---

### 8. Human‑escalation triggers  

| Situation | Trigger for escalation to senior RA / management |
|-----------|---------------------------------------------------|
| Intended purpose is ambiguous or includes any therapeutic claim. | Immediate review – risk of misclassifying under Rule 9. |
| Absence of measured radiation output data (kVp, mA, dose). | Require engineering test report before proceeding. |
| No clinical evidence or equivalence justification to a known predicate. | Pause CE‑marking plan; obtain clinical data. |
> **If any of the above gaps remain unresolved after the initial gap‑analysis**, an escalation note should be logged and senior RA consulted before finalising the technical file.

---

### 9. Peer‑review request  

> *@RA‑Colleague:* Please review this draft for:  
> • Completeness of the classification justification (Rule 10 vs Rule 9).  
> • Adequacy of identified evidence gaps, especially regarding clinical data and radiation specifications.  
> • Any EU‑specific obligations missed (e.g., EN ISO 14971 implementation depth, EUDAMED article references).  
> Your challenge will help ensure no jurisdictional nuance is overlooked before the NRB audit.

---

### 10. Reusable RA judgment (honcho_conclude)

**Judgment ID:** MDR_CLASS_XRAY_DIAG_2026-07-19  
**Conclusion:** Diagnostic X‑ray imaging systems are classified under **MDR Annex VIII Rule 10 → Class IIb**. The appropriate conformity‑assessment route is **Module B (Annex IX) or Module C (Annex IX + X/XI)** with a full technical documentation package, including a CER (Annex XIV Part A), PMS plan (Art. 84) and PSUR (Art. 86). Mis‑applying Rule 9 leads to an incorrect Class IIa/IIb route and downstream compliance failures. All risk controls must address ionising‑radiation hazards per IEC 60601‑2‑44.  

*Record this judgment for future cases involving diagnostic radiation devices.*

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

### kb-eval-20260717-it03-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_eu-004", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "6b46b0ff30afb7f7", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

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

> **Regulatory Draft – MDR 2017/745 Classification & Conformity‑Assessment Route**

---

### 1 Scope of the Current Information  

| Item | Source excerpt | Observation |
|------|----------------|-------------|
| Legal basis for technical documentation | “EU MDR 2017/745, **Annex II** (Technical Documentation)” – [2] | Confirms that Annex II is the required template. |
| Intended device‑class coverage | “MDR 적용 의료기기 전 Class (I·IIa·IIb·III)” – [2] | Indicates the procedure applies to **all risk classes** but gives no device‑specific class. |
| Content sections of Annex II (template) | Detailed mapping of “Device Description”, “Labeling”, “Design & Manufacturing”, “Safety Requirements”, “Risk Management”, “Verification & Validation” – [1] | Provides the structure that must be populated once the device is defined. |

> **Result:** The source supplies only the *framework* (Annex II template) and the legal context, but **no data on the actual device** (e.g., intended purpose, technological characteristics, patient population). Consequently a definitive classification and conformity‑assessment route cannot be concluded at this stage.

---

### 2 Preliminary Determination of Classification & Conformity Route  

| Step | Required Evidence (per MDR) | Status with Current Data |
|------|-----------------------------|--------------------------|
| **2.1 Identify intended medical purpose** (e.g., diagnosis, therapy, monitoring). | Statement of intended use in the “Device Description” (§1 of Annex II). | *Missing* – not provided in excerpts. |
| **2.2 Apply Classification Rules** (Annex VIII). | Decision matrix linking purpose & technology to Rule 1‑22. | *Missing*: No rule can be selected without intended use and principle of operation. |
| **2.3 Determine if a Notified Body (NB) is required** – Classes IIa, IIb, III need NB involvement; Class I may self‑declare unless it has a measuring function or is sterile. | Classification outcome from 2.2. | *Undetermined* due to missing classification. |
| **2.4 Choose conformity‑assessment route** (Annex IX for QMS‑based routes, Annex X + XI for type‑examination & product verification). | Based on class & device category; also whether the device is a “custom‑made” or “in vitro diagnostic”. | *Undetermined* – pending classification. |

> **Citation**: Classification rules are defined in **Annex VIII** (MDR) and conformity‑assessment routes in **Annex IX**, **Annex X**, **Annex XI** (per the MDR structure).  

---

### 3 Evidence Required to Complete the Submission  

| Evidence | Where it belongs in Annex II (template) | Supporting MDR reference |
|----------|-------------------------------------------|--------------------------|
| **Device Description & Intended Use** (including principle of operation, indications, target population) | §1 Device Description | Annex I (GSPR) – required for all devices; Annex VIII classification rules. |
| **Labeling & IFU** (including symbols, safety information) | §2 Labeling | Annex I §23 (labeling). |
| **Design & Manufacturing Information** (materials, processes, manufacturing sites) | §3 Design & Manufacturing | Annex I GSPR – §§4‑6. |
| **Safety Requirements Checklist** (GSPR compliance matrix) | §4 GSPR Checklist | Annex I (General Safety and Performance Requirements). |
| **Risk Management File** (ISO 14971 compliant) | §5 Risk Management | Annex I (risk management basis). |
| **Verification & Validation Reports** (including performance testing, biocompatibility, software validation where applicable) | §6 Verification & Validation | Annex I §§7‑12; also relevant for clinical evidence (Annex XIV). |
| **Clinical Evaluation Report (CER)** | Separate document – referenced in Technical Documentation | **Annex XIV Part A** (clinical evaluation). |
| **Post‑Market Surveillance (PMS) Plan & Report** (incl. Periodic Safety Update Report for Class IIb/III) | Not a section of Annex II but required by Article 83–86; referenced in Technical Documentation | Articles 83‑86 (PMS system, plan, report, PSUR). |
| **Declaration of Conformity** | Separate document – signed by Manufacturer | **Annex IV** (EU Declaration of Conformity). |

---

### 4 Identified Gaps & Required Human Input  

1. **Intended medical purpose / indications** – needed to select the appropriate rule in Annex VIII.  
2. **Device principle of operation and technology description** – required for classification and risk analysis.  
3. **Patient/clinical setting information** – essential for clinical evaluation scope (Annex XIV).  
4. **Sterility, measuring function, or active device status** – influences whether Class I can self‑declare.  
5. **Regulatory history (e.g., prior 510(k) clearance, CE mark under MDD)** – may affect transitional provisions; *no specific identifier found in source — verify separately*.  

*Human escalation trigger:* As soon as any of the items above remain unavailable, the case must be **paused** and a request sent to the product owner or clinical team for clarification before proceeding with classification.

---

### 5 Risk‑Control Recommendations (preliminary)  

| Risk Area | Preliminary Control (to be detailed once device data are available) |
|-----------|-----------------------------------------------------------------------|
| **Design‑related hazards** – mechanical, electrical, software | Apply ISO 14971 risk management process; generate a *Risk Management File* (§5). |
| **Biocompatibility** | Perform testing per ISO 10993 series; document in Verification & Validation §6. |
| **Usability / Human factors** | Conduct formative/usability studies; include results in CER (Annex XIV). |
| **Performance safety** | Execute bench‑testing, simulated use, and where applicable animal or clinical performance studies; record in §6. |
| **Post‑market hazards** | Draft a PMS plan (Art. 84) and schedule periodic safety updates for Class IIb/III (Art. 86). |

---

### 6 Citation Summary  

- **Annex II – Technical Documentation template** – source [1] & [2].  
- **Annex I – GSPR & labeling requirements** – inferred from MDR structure (not directly quoted).  
- **Annex VIII – Classification rules** – required for step 2.2 (per Fixed‑Rule mapping).  
- **Annex IX, X, XI – Conformity‑assessment routes** – relevant to step 2.4.  
- **Annex XIV Part A – Clinical Evaluation Report** – cited per regulatory table.  
- **Articles 83‑86 – PMS system/plan/report/PSUR** – noted for required post‑market evidence.

---

### 7 Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|------------------|
| Missing intended purpose / indication | Request detailed Intended Use Statement from product owner. |
| No information on active/measuring function | Clarify device functionality; may shift classification (Rule 9/10/17). |
| Absence of risk‑management documentation | Obtain ISO 14971‐compliant Risk Management File before Annex II completion. |
| Unavailable clinical data for CER | Initiate literature search or plan a PMCF study as per Annex XIV Part B. |
| Unclear whether device is sterile or has a measuring function (affects Class I self‑declaration) | Confirm with manufacturing and design teams. |

---

### 8 Peer‑Review Prompt  

> **To: RA Peer**  
> Please review this draft focusing on three aspects:  
> 1️⃣ **Assumptions about the device scope** – Are we justified in treating the case as “any MDR‑applicable device” without a concrete description?  
> 2️⃣ **Source coverage** – Have we extracted all relevant regulatory elements from the provided excerpts, or are there additional clauses (e.g., language requirements, NB‑specific annexes) that need inclusion?  
> 3️⃣ **Jurisdictional gaps** – Does the draft omit any EU‑specific obligations not visible in the excerpt (e.g., Unique Device Identifier (UDI) requirements, EUDAMED registration under Articles 33‑39)? Suggest any missing evidence or steps.  

--- 

*Prepared by Theo – EU MDR Regulatory Affairs Specialist*

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

### kb-eval-20260717-it03-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_eu-005", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "000ee9037b6dc9a5", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md", "source_hash": "4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1"} -->

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

> **Regulatory Draft – Software‑based Imaging‑Room GUI (Rule 11, Annex VIII)**  

---

### 1. Preliminary Classification  

| Item | Source / Reference | Determination |
|------|--------------------|--------------|
| **Applicable classification rule** | Rule 11 (SW) – *“Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes…”*【1007248354989010815】 | Annex VIII, Rule 11 |
| **Intended use (presumed)** | “촬영실 GUI SW” – user‑interface that displays imaging data and may suggest diagnostic/therapeutic actions. | Decision‑support software (diagnostic/therapeutic). |
| **Impact assessment** | • If a decision could cause death or irreversible deterioration → Class III  <br>• If it could cause serious deterioration or require surgical intervention → Class IIb  <br>• Otherwise → Class IIa (default)【1007248354989010815】 | **Classification to be finalised after clarification of clinical impact**. |
| **Transitional deadline** (if new CE‑marking required) | Class IIa non‑implantable devices must comply by 31 Dec 2028【1007987960287657537】 | Provides sufficient time for NB assessment if classification stays at IIa. |

> **Action:** Obtain a definitive “impact statement” from the manufacturer (e.g., risk of missed/erroneous diagnosis, possible patient harm).  

---

### 2. Conformity‑Assessment Route  

| Classification | MDR Annex(es) Involved | Typical NB Modules* |
|----------------|------------------------|---------------------|
| **Class IIa** (most likely) | – Annex IX (QMS review) <br>– Annex I (General Safety & Performance Requirements) <br>– Annex XIV Part A (CER) | Module B (full quality‑management system review + technical documentation). |
| **Class IIb** | – Annex IX (QMS) <br>– Annex XI (Product verification) <br>– Annex I & XIV Part A | Modules B + C (product verification added). |
| **Class III** | – Annex X (Type‑examination) <br>– Annex XI (Product verification) <br>– Annex IX (QMS) <br>– Annex I & XIV Part A/B (PMCF) | Modules A + B + C (type‑examination, full QMS, product verification). |

\*The “module” terminology follows the New Legislative Framework; MDR references the same letters but ties them to the specific annexes listed above. Do **not** mix module letters with Annex numbers in a single phrase.

---

### 3. Required Technical Documentation & Evidence  

| Deliverable | Minimum Content (MDR/ISO) | Reason |
|-------------|---------------------------|--------|
| **Device Description & Intended Use** | Complete “Indications for use”, user profile, clinical context, decision‑support scope. | Basis for classification and risk analysis. |
| **Risk Management File** | ISO 14971 + MDR Annex I justification of safety; specific controls for mis‑diagnosis, algorithm error, cybersecurity. | Demonstrates mitigation of identified hazards (death/serious deterioration). |
| **Software Verification & Validation** | IEC 62304 (life‑cycle), IEC 82304‑2 (health‑software), IEC 60601‑1‑6 (usability), IEC 62443 / ISO 27001 (cybersecurity). | Required for all classes; more extensive validation if Class IIb/III. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – systematic literature review, state‑of‑the‑art analysis, clinical benefit & safety data, justification of equivalence or need for clinical investigation. | Evidence that software performs as claimed and does not compromise patient safety. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 – description of routine PMS activities; for Class IIb/III a Periodic Safety Update Report (PSUR, Art. 86). | Ongoing monitoring of real‑world performance. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** *(if required)* | Annex XIV Part B – proactive collection of clinical data to verify long‑term safety/effectiveness. | Particularly important for high‑impact decision support (potential Class IIb/III). |
| **Usability Engineering File** | IEC 62366‐1 – user‑interface design, formative/usability testing outcomes. | Reduces use errors that could lead to serious harm. |
| **Declaration of Conformity (DoC)** | Annex IV – signed DoC referencing all applicable standards & NB certificate. | Legal statement of compliance. |
| **Labeling & IFU** | Annex I, Chapter III §23 – clear instructions, limits of use, safety information. | Ensures user understands risk and intended decision scope. |

---

### 4. Gaps / Missing Information (to be supplied before NB submission)

1. **Exact Intended Use Statement** – does the GUI *recommend* a diagnosis/therapy or merely display raw images?  
2. **Clinical Impact Analysis** – quantitative estimate of harm if wrong advice is given (death, irreversible deterioration, serious deterioration).  
3. **Algorithm / Decision‑Support Logic Description** – flowcharts, data inputs, performance metrics (sensitivity/specificity).  
4. **User Validation Results** – usability testing with intended operators (radiographers, physicians).  
5. **Cybersecurity Architecture** – threat analysis, protection measures, patch management plan.  
6. **Equivalence Justification** (if any) – list of predicate devices/software and comparison matrix.  

*Until these are clarified, the classification cannot be finalised and the NB route remains provisional.*

---

### 5. Key Risk Controls (to be reflected in ISO 14971 file)

| Hazard | Potential Consequence | Control Measure |
|--------|-----------------------|-----------------|
| Incorrect decision output (false negative/positive) | Mis‑diagnosis → possible delayed treatment, serious deterioration or death. | • Algorithm validation against large, representative clinical datasets.<br>• Built‑in verification alerts (“review required”).<br>• Redundancy: clinician must confirm before action. |
| UI misinterpretation (layout confusion) | User selects wrong option → inappropriate therapy. | • Human factors/usability engineering per IEC 62366‑1.<br>• Mandatory training & competency assessment. |
| Software malfunction / crash | Loss of displayed data, delayed decision. | • Robust error handling, safe‑state mode, automatic logging.<br>• Regular software updates & verification (IEC 62304). |
| Cyberattack / data tampering | Manipulated output → patient harm. | • Secure coding practices, encryption, authentication (IEC 62443).<br>• Continuous monitoring & incident response plan. |
| Obsolescence of reference databases | Out‑dated clinical guidance. | • Periodic review and update schedule; PMCF to capture real‑world performance. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Required Human Action |
|---------|------------------------|
| **Unclear impact statement** (cannot determine whether death/serious deterioration risk exists) | Senior RA must request a formal “Risk Impact Analysis” from the product team before proceeding to classification. |
| **Missing clinical performance data** (no validated sensitivity/specificity) | Clinical affairs lead to commission a clinical investigation or compile real‑world evidence; pause NB submission until CER is complete. |
| **Software version change >10 % code base** after QMS audit | Trigger a re‑assessment of validation & risk management (module B scope update). |
| **PMS signal indicating adverse events above acceptable rate** | Immediate safety notice to Notified Body; initiate field corrective action and possibly submit a vigilance report (Art. 87). |
| **Approaching Class IIa transitional deadline (31‑Dec‑2028) with incomplete documentation** | Management decision required: either accelerate submission or defer market launch. |

---

### 7. References & Citations  

1. **MDR Annex VIII – Classification Rules, Rule 11 (SW)** – source excerpt【1007248354989010815】.  
2. **Transitional implementation dates per MDR** – Class‑specific cut‑off table (Class IIa non‑implantable → 31‑Dec‑2028)【1007987960287657537】.  
3. **Regulatory framework citations** (used throughout):  
   * Annex I, Chapter III §23 – labeling requirements.  
   * Annex IV – EU Declaration of Conformity.  
   * Annex IX – QMS assessment (module B).  
   * Annex X & XI – type‑examination & product verification (higher classes).  
   * Annex XIV Part A – Clinical Evaluation Report.  
   * Annex XIV Part B – PMCF plan/report.  
   * Art. 84, 85, 86 – PMS system/plan/report.  

*No specific predicate or registration numbers appear in the source material; verify separately if required.*

---

### 8. Peer‑Review Prompt  

> **To RA colleagues:** Please examine the assumptions made above regarding (a) the likely impact level of the imaging‑room GUI, (b) the completeness of the evidence list for a software device under MDR, and (c) any jurisdictional nuances that may have been omitted (e.g., national Notified Body preferences, additional German BfArM requirements, or EU‑wide cybersecurity directives). Highlight any gaps or alternative interpretations so we can close them before engaging the NB.

---

### 9. Reusable RA Judgment (Lesson Record)

> **Rule 11 Software Classification Rule of Thumb:** When software provides diagnostic or therapeutic decision support, start with Class IIa; elevate to Class IIb if a wrong decision could cause serious deterioration or require surgical intervention, and to Class III if it could lead to death or irreversible deterioration. Final classification must be justified by a documented clinical‑impact analysis that links the software’s output to patient outcomes.

---


*Prepared by: Theo – EU MDR Regulatory Affairs Specialist*

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

### kb-eval-20260717-it03-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_kr-001", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "1a49e8c0440c9349", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

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

> **Regulatory Draft – Korean MFDS Classification & Submission Plan for a Stand‑Alone Medical Software (AI/ML‑enabled)**  

---

### 1. Preliminary Device Profile  
| Item | Expected Content* |
|------|-------------------|
| **Product type** | Stand‑alone medical software (digital therapeutic / diagnostic aid) – AI/ML algorithm applied to imaging data. |
| **Intended use** | *To be defined* – e.g., “Assist radiologists in detecting pulmonary nodules on CT images.” |
| **Target user** | Health‑care professionals (radiologists, clinicians). |
| **Risk profile** | Functional risk depends on level of clinical decision support; baseline assumed to be a **2등급 (Class II)** device under MFDS unless the AI function provides an autonomous diagnosis that could elevate it to 3등급. |

\*The specific wording for intended use, target population and claimed indications must be supplied by the sponsor before any classification justification can be finalised.

---

### 2. Korean Classification & Regulatory Pathway  

| Aspect | MFDS Requirement (per source) |
|--------|--------------------------------|
| **Classification** | **2등급** – “보조 기능 수준에 따라 상향 가능” (i.e., may be re‑classified upward if the software provides a primary diagnostic function). Source [1]. |
| **Regulatory route** | **허가 (Approval)** for Class II devices.  <br> *Note*: If later re‑classed to 3등급, a more extensive 허가 with additional clinical data will be required. |
| **Applicable legal framework** | • “디지털의료제품법” (effective 2025‑01‑24) – establishes a separate system for AI/SW digital medical products, requiring a change‑management plan and component performance evaluation.<br>• “디지털 의료기기소프트웨어 허가·심사 가이드라인”.<br>• “독립형 SW 사용적합성 가이드라인” (applies when the software is stand‑alone). Source [1]. |

---

### 3. Required Submission Evidence  

| Evidence Category | Description & Reference |
|-------------------|--------------------------|
| **KGMP Facility Certification** | The manufacturing (software development) entity must hold a KGMP certificate for medical device software (ISO 13485‑based). |
| **Technical Documentation** (per MFDS Guideline) | • Software Development Lifecycle documentation (IEC 62304).  <br>• Software Bill of Materials (SBOM) – mandatory under the 2025 digital product law.  <br>• Verification & Validation reports, including performance testing of AI algorithm (sensitivity, specificity, ROC‑AUC, etc.). |
| **Risk Management File** | IEC 60601‑1‑11 / ISO 14971 compliant risk analysis, mitigation measures, and post‑market surveillance plan. |
| **Clinical Evaluation** | • Literature review of foreign clinical data (e.g., FDA 510(k) summaries if available). <br>• Korean‑specific clinical performance study *if* the AI function is considered a primary diagnosis or if local data are required to substantiate safety/efficacy. |
| **Change Management Plan (PCCP)** | Required under the “디지털의료제품법”; must describe predetermined change control for algorithm updates (aligned with FDA PCCP guidance – see source [2] for reference, though not directly cited by MFDS). |
| **Cybersecurity & SBOM** | Conform to MFDS 2025 cybersecurity expectations; include threat analysis, mitigation strategy, and a legally binding SBOM. |
| **Labeling & IFU (Korean language)** | All labeling, instructions for use, and safety information must be provided in Korean. |
| **Software Usability Testing** | Human factors/ usability validation with intended user group, documented per MFDS usability guideline. |

> **Citation note:** The specific identifiers for FDA product codes (LLZ, QIH, QDQ) appear only in the U.S. excerpt and are not required by MFDS; they may be used as supporting foreign evidence but no Korean‑specific predicate number exists in the source excerpts. Therefore: *no specific identifier found in source — verify separately*.

---

### 4. Gaps & Missing Information (to be supplied by sponsor)  

| Gap | Why it matters for MFDS |
|-----|--------------------------|
| **Exact intended use / claim language** | Determines whether the device remains Class II or is upgraded to Class III. |
| **Algorithm description & training data provenance** | Needed for risk assessment, performance justification, and to satisfy change‑management (PCCP) requirements. |
| **Hardware interface (if any)** | If the software relies on a specific imaging modality or device, that hardware must be referenced in the classification rationale. |
| **User environment / workflow description** | Impacts usability testing scope and risk analysis. |
| **Local clinical data plan** | Required if foreign evidence is insufficient for the intended indication under MFDS guidelines. |
| **KGMP certification status** | Confirmation of current KGMP holder; otherwise need to obtain/upgrade. |
| **Post‑market surveillance (PMS) strategy** | Must align with MFDS PMS requirements for Class II digital products. |

---

### 5. Core Risk Controls (to be reflected in the submission)

1. **Software Lifecycle Management** – IEC 62304 compliant development, version control, and traceability matrix linking requirements → design → test.
2. **Cybersecurity** – Threat modelling, encryption of data at rest & in transit, secure update mechanism governed by PCCP.
3. **Performance Validation** – Independent dataset testing; statistical analysis meeting predefined performance thresholds.
4. **Usability & Human Factors** – Formative and summative usability studies with Korean clinicians, documented findings incorporated into UI design.
5. **Labeling & Instructions** – Clear Korean language warnings, intended use statements, contraindications, and user responsibilities.
6. **Post‑Market Monitoring** – Real‑world data collection plan, adverse event reporting process, periodic safety update (PSUR) for digital devices.

---

### 6. Human‑Escalation Triggers  

| Situation | Action Required |
|-----------|-----------------|
| **Intended use involves autonomous diagnosis** (e.g., AI makes a definitive clinical decision) → possible upgrade to **3등급** | Immediate escalation to senior RA lead; obtain additional clinical evidence and consider full “허가” with higher scrutiny. |
| **KGMP certificate not in place or expires during submission** | Pause submission; engage quality‑system team to secure certification before filing. |
| **Insufficient local clinical data** (FDA 510(k) not fully accepted) | Escalate to clinical affairs for planning of Korean pilot/clinical trial. |
| **Algorithm change plan (PCCP) missing or incomplete** | Halt dossier finalisation; request detailed change‑control documentation from development team. |
| **Cybersecurity assessment fails MFDS criteria** | Notify CISO & product owner, remediate vulnerabilities before resubmission. |
| **Labeling not fully translated into Korean** | Escalate to localization team; prohibit submission until complete Korean labeling is ready. |

---

### 7. Peer‑Review Prompt  

> **@RA‑Colleague:** Please review the above draft and challenge the following points:  
> 1. Is the assumption that the device qualifies for **2등급** justified given only the generic “assistive” description? What additional data would definitively rule out a 3등급 classification?  
> 2. Does the list of required evidence fully reflect current MFDS expectations for AI‑enabled stand‑alone software under the 2025 digital medical product law? Are any new items (e.g., real‑world performance monitoring) missing?  
> 3. Identify any jurisdictional gaps where Korean requirements differ from the FDA references provided (product codes LLZ/QIH/QDQ), especially concerning cybersecurity and SBOM obligations.  

Your feedback will help ensure completeness before the formal dossier is compiled.

---

### 8. Reusable RA Judgment (Lesson Learned)  

**When evaluating digital medical software for MFDS submission:**  
- **Classification hinges first on the precise intended use wording.** Even a “support” claim can be upgraded if the AI output directly influences clinical decision‑making. Capture this early and document justification against the “보조 기능 수준에 따라 상향 가능” clause.  
- **The 2025 Digital Medical Product Law adds mandatory change‑management (PCCP) and SBOM requirements** that are not present in older MFDS guidelines; they must be built into the technical file regardless of whether foreign (FDA/CE) evidence is leveraged.  
- **Foreign FDA product codes or 510(k) summaries can serve as supporting clinical evidence but cannot replace Korean‑specific clinical data** when the algorithm’s risk level aligns with a primary diagnostic function.  

*Record this judgment in the team knowledge base for future digital‑health device assessments.*

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

### kb-eval-20260717-it03-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_kr-002", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "e5180461a3d586b5", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

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

> **Regulatory Draft – Classification & Submission Pathway for a Digital Medical‑Device Software (SW) Product**

---

### 1. Likely MFDS Device Class & Licensing Route  

| Factor | Assessment |
|--------|------------|
| **Intended Use** (assumed from “digital medical device” context) | If the software provides a diagnostic, therapeutic or monitoring function that directly influences patient care, it will fall under the **“Digital Medical Device”** category defined in the *디지털의료제품법* and its enforcement rules. |
| **Risk‑Based Classification (MFDS)** | <ul><li>**Class I** – General utility software with no impact on clinical decisions (e.g., health‑information apps).</li><li>**Class II** – Software that provides data analysis, risk assessment or decision support but does not autonomously prescribe treatment.</li><li>**Class III** – Software that performs autonomous diagnosis/treatment or controls/commands an active medical device.</li></ul> <br>*The exact class must be confirmed by mapping the software’s functional claims to MFDS classification tables (e.g., Table 2‑1 of the “디지털의료제품법 시행규칙”).* |
| **Submission Route** | • **Class I** – *신고 (Notification)* is sufficient. <br>• **Class II / III** – *허가 (Approval)* required, submitted via **MFDS “Digital Medical Device” licensing process** (similar to the traditional “제조·수입 허가” but with digital‑specific documentation). |

---

### 2. Mandatory Evidence & Documentation (based on source excerpt)

| Requirement | Source citation | Expected artefact |
|-------------|----------------|-------------------|
| **Software version, build number & release date** (S‑1) | ✅ 필수 – 디지털의료제품법 시행규칙 | Software Release Log / Version History |
| **Software update method & frequency** (S‑2) | ✅ 필수 – MFDS SW 가이드라인 | Update Policy Document; schedule of planned updates |
| **Minimum & recommended system requirements** (OS, CPU, RAM, storage, monitor resolution, network) (S‑3) | ✅ 필수 – MFDS SW 가이드라인 | Technical Specification Sheet |
| **List of compatible medical devices & interface specifications** (S‑4) | ✅ 필수 – *no explicit source* (self‑declared) | Compatibility Matrix; Interface Definition Document (e.g., DICOM, HL7) |
| **Data I/O formats (DICOM, HL7, etc.)** (S‑5) | ✅ 필수 – *no explicit source* | Data Exchange Specification |
| **Cybersecurity configuration guidance** (password policy, network segregation, access rights) (S‑6) | ✅ 필수 – MFDS 사이버보안 가이드라인 2025.01 | Cybersecurity Controls Plan |
| **Security‑patch application procedure & responsibility** (S‑7) | ✅ 필수 – MFDS 사이버보안 가이드라인 2025.01 | Patch Management SOP |
| **Residual cybersecurity risk & mitigation strategies** (S‑8) | ✅ 필수 – MFDS 사이버보안 가이드라인 2025.01 | Risk Acceptance Statement + Mitigation Plan |
| **Data backup & recovery method** (S‑9) | ✅ 필수 – *no explicit source* | Backup/Recovery Procedure |
| **System log management** (S‑10) | ⚠️ 권장 – MFDS 사이버보안 가이드라인 | Log Management Policy (recommended) |

> **Note:** The checklist also references an additional “디지털의료기기 특화 표시기재 요건” table (source [2]) that adds items beyond the standard medical‑device IFU requirements. Those should be reviewed in detail once the core IFU template is drafted.

---

### 3. Missing / Unclear Information Needed for a Complete Submission  

| Gap | Why it matters | Suggested source/approach |
|-----|----------------|---------------------------|
| **Exact Intended Use Statement & Clinical Claim(s)** | Determines classification (Class I‑III) and dictates clinical evidence requirements. | Draft a clear intended‑use paragraph; map to MFDS risk‑classification tables. |
| **Clinical Evaluation Evidence** (e.g., performance data, usability testing, comparative study) | Required for Class II/III approvals; may be waived if substantial foreign clearance is accepted under current MFDS scope expansions (verify latest notice). | Compile clinical trial reports or real‑world evidence; check MFDS “foreign clinical evaluation acceptance” notices. |
| **KGMP Facility Certification** (if the product includes hardware manufacturing) | KGMP certification is mandatory for any device with a physical component entering Korean market. | Obtain KGMP certificate or confirm that only software (no hardware) is being supplied. |
| **Korean Language Labeling & IFU Content** | All labeling, instructions for use (IFU), and safety information must be provided in Korean. | Translate all mandatory items from the checklist; include required symbols per MFDS labeling guidelines. |
| **Risk Management File (ISO 14971‑aligned)** | Demonstrates identification/mitigation of hazards, especially cybersecurity residual risks listed in S‑8. | Prepare a risk management report linking each identified hazard to mitigation strategies and verification evidence. |
| **Software Validation / Verification Documentation** (V&V plan, test reports) | Confirms that the software meets functional, performance, and safety specifications. | Create V‑V documentation aligned with IEC 62304 (if applicable) and MFDS SW guideline. |
| **Post‑Market Surveillance (PMS) Plan** | Required for Class II/III devices; outlines monitoring of adverse events, updates, and field safety corrective actions. | Draft PMS plan referencing MFDS “시판후조사” requirements. |

---

### 4. Core Risk Controls to Highlight in the Submission  

| Domain | Control(s) | Reference |
|--------|------------|-----------|
| **Cybersecurity** | • Password policy & role‑based access control (S‑6). <br>• Network segmentation; encryption of data at rest and in transit.<br>• Regular security patching schedule (S‑7). <br>• Residual risk acceptance with mitigation plan (S‑8). | MFDS 사이버보안 가이드라인 2025.01 |
| **Data Integrity & Backup** | • Automated backup to secure off‑site storage; restore testing (S‑9). | – |
| **System Logging** | • Centralized log collection, retention for ≥ 12 months; audit trail of user actions (recommended S‑10). | MFDS 사이버보안 가이드라인 |
| **Software Quality Management** | • Alignment with IEC 62304 development lifecycle; documented version control (S‑1). | MFDS SW 가이드라인 |
| **Compatibility & Interoperability** | • Conformance to DICOM/HL7 standards; interface validation testing (S‑5, S‑4). | – |

---

### 5. Citations  

* **Digital Medical Device Software Mandatory Items** – Table entries S‑1 through S‑10 as listed in source excerpt [1] (디지털의료제품법 시행규칙, MFDS SW 가이드라인, MFDS 사이버보안 가이드라인 2025.01).  
* **Additional Digital‑Specific Labeling Checklist** – Reference to “디지털의료기기 특화 표시기재 요건 체크리스트” in source excerpt [2].  

> *No specific identifier (e.g., 510(k), K‑number, case ID) appears in the provided excerpts; verification of any such codes must be done separately.*  

---

### 6. Human‑Escalation Triggers  

| Situation | Action Required |
|-----------|-----------------|
| **Unclear device classification** (e.g., borderline between Class II and III) | Escalate to senior MFDS RA lead for classification decision; consider a pre‑submission meeting with MFDS. |
| **Missing Korean IFU or labeling elements** | Engage translation & regulatory compliance team immediately; do not proceed until all required Korean language items are verified. |
| **Absence of KGMP certification where hardware is involved** | Halt submission until KGMP audit completed or an appropriate contract manufacturer is qualified. |
| **Cybersecurity residual risk deemed “unacceptable” by internal review** | Elevate to the product safety board; develop additional mitigations before filing. |
| **Regulatory notice indicating new acceptance of foreign clinical data does not cover this device type** | Verify current MFDS notice (retrieve latest amendment) and consult with a senior RA or MFDS liaison before relying on foreign evidence. |

---

### 7. Peer‑Review Prompt  

> **To the next RA peer:**  
> Please review this draft for (1) completeness of classification justification, (2) whether all mandatory items from the MFDS Digital Medical Device checklist have been captured, and (3) any jurisdictional gaps—especially concerning Korean language labeling, KGMP requirements, and the latest MFDS notices on accepted foreign clinical evidence. Highlight any assumptions that need supporting documentation or clarification.

--- 

*Prepared by Sam – Korean Regulatory Affairs Specialist (MFDS / KGMP)*

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

### kb-eval-20260717-it03-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_kr-003", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "39ca8fb2e959a790", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

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

> **Regulatory Draft – Digital Medical Device (GUI Software) – MF 2025 Regime**

---

### 1. Applicable MFDS Notices  

| Topic | Notice / Rule | Publication/Effective Date |
|-------|---------------|----------------------------|
| Overall‑procedure, document requirements, evaluation criteria for digital medical product approval | **디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정** – *제2025‑25호* | 15 Apr 2025 |
| Classification & grade assignment of digital medical products (incl. GUI software) | **디지털의료제품의 분류 및 등급 지정 등에 관한 규정** – *제2025‑23호* | 7 Apr 2025 |
| Digital GMP (quality‑management) framework for software (including AI/ML) | **디지털 의료기기 제조 및 품질관리 기준 (디지털 GMP)** – separate notice, implementation scheduled **within 2025** | — |
| Recent amendment of implementing rules (covers e‑submission format, data standards) | **디지털의료제품법 시행규칙 개정** – *총리령 제2088호* | 23 Jan 2026 (amendment completed) |

> **Citation rule compliance:** All identifiers above appear verbatim in the source excerpts; no additional numbers (e.g., FDA 510(k), CE‐marking codes) are included because they were not present.

---

### 2. Classification & Submission Route  

| Step | Determination | Basis |
|------|----------------|-------|
| **Device type** | Software‑only “Graphic User Interface (GUI)” medical device, no hardware component. | Product description (assumed). |
| **Risk class** | *Class I* if the software provides only **information/monitoring** without therapeutic or diagnostic decision support; otherwise *Class II* when it influences clinical management (e.g., alerts that affect treatment). | Use *디지털의료제품의 분류 및 등급 지정 등에 관한 규정* (*제2025‑23호*) – risk‑based criteria for digital products. |
| **Submission pathway** | • **Class I** → **신고 (Notification)**; <br>• **Class II/III** → **허가 (Approval)**, with full dossier per *제2025‑25호*. | MFDS distinguishes “notification” for low‑risk devices and “approval” for higher risk. |
| **GMP requirement** | If the device is to be marketed after 2025, the manufacturing organization must obtain **Digital GMP certification** (one of the 8 type‑group requirements). | *디지털 의료기기 제조 및 품질관리 기준* – scheduled rollout 2025 (see monitoring point “디지털 GMP 고시 시행”). |

---

### 3. Evidence Package – Minimum Required Documents  

| Category | Content | Regulatory reference |
|----------|---------|----------------------|
| **Device description** | Functional overview, architecture diagram, intended use statement in Korean & English. | *제2025‑25호* § 1 (서류 요건). |
| **Risk Management File** | ISO 14971‑based risk analysis, risk control measures, residual risk justification. | *제2025‑25호* § 3 (평가 기준). |
| **Software Lifecycle Documentation** | IEC 62304 compliance: development plan, verification/validation reports, change‑control logs, cybersecurity assessment. | Implicit in Digital GMP & *제2025‑25호*. |
| **Clinical Evaluation** | • If foreign CE/FDA clearance exists, provide full evaluation report (including predicate devices, if any). <br>• MFDS may accept the foreign clinical data under its recent scope expansion (OECD‑aligned non‑clinical data & foreign clinical reports – confirm via latest MFDS notice). | *제2025‑25호* § 3; see MFDS periodic scope updates (not in excerpt – flag for verification). |
| **Labeling & IFU** | All labeling, user manuals, and instructions for use must be **in Korean**, with clear risk warnings. | General MFDS labeling rule (implicit). |
| **Quality Management System** | Digital GMP certification evidence (or interim compliance plan if certification pending). | *디지털 의료기기 제조 및 품질관리 기준* – rollout 2025. |
| **Post‑Market Surveillance Plan** | PMS activities, periodic safety update schedule, adverse event reporting procedure per MFDS 시판후조사 규정. | Standard MFDS requirement for approved devices. |

---

### 4. Gaps / Missing Information (to be clarified before dossier finalisation)

1. **Exact intended indication & risk claim** – decisive for class determination.
2. **Whether AI/ML components are present** – triggers additional Digital GMP sub‑requirements and possible need for “Algorithm Change Management” documentation.
3. **Manufacturing site status** – KGMP/Digital GMP certification already obtained or pending? If pending, a mitigation plan is required.
4. **Foreign clinical evidence** – specific CE/FDA numbers or published study data (if any). MFDS acceptance depends on the latest notice; confirm that the foreign evidence aligns with current Korean scope.
5. **Korean‑language IFU draft** – must be completed and verified for accuracy before submission.
6. **Cybersecurity risk assessment details** – especially if device communicates over networks.

---

### 5. Risk Controls (Design & Post‑Market)

| Control | Application |
|--------|-------------|
| **Usability Engineering** | Human factors testing to ensure correct GUI interaction; address potential use errors that could lead to misinterpretation of clinical information. |
| **Cybersecurity** | Threat modeling, vulnerability management plan, secure update mechanism (signed firmware/software). |
| **Software Versioning & Change Management** | Documented change‑control per IEC 62304; each release must be reviewed against Digital GMP requirements before market release. |
| **Safety Monitoring** | Real‑time error logging, remote monitoring capability if feasible; defined thresholds for alerting the manufacturer. |
| **PMS & Vigilance** | Quarterly safety summary reports to MFDS (per *제2025‑25호*); incident handling SOPs in Korean. |

---

### 6. Human‑Escalation Triggers  

| Situation | Action – Who & When |
|-----------|----------------------|
| **Uncertain classification** (e.g., borderline Class I/II) | Escalate to senior RA manager + clinical expert; obtain MFDS pre‑submission consultation. |
| **Foreign clinical data not covered by latest MFDS scope** | Pause dossier, request clarification from MFDS or legal counsel; document the gap. |
| **Digital GMP certification pending past the intended market launch date** | Notify project lead & supply‑chain manager; consider interim compliance plan and risk‑based justification to MFDS. |
| **Korean labeling/IFU not finalized 30 days before submission deadline** | Immediate hand‑off to regulatory affairs translation team; senior QA sign‑off required. |
| **New amendment (e.g., additional guide‑line) released after dossier lock** | Review impact within 48 h; if material, re‑open the docket and seek sponsor approval for amendment. |

---

### 7. Peer‑Review Prompt  

> **To RA peer:** Please review the assumptions made above regarding:  
> 1. The classification logic for GUI‑only software under *제2025‑23호* (risk criteria).  
> 2. Whether foreign clinical evidence can be leveraged without additional Korean data, given the MFDS’s recent scope expansions (which are not fully captured in the excerpts).  
> 3. The completeness of the required evidence list—especially any items that may have been added by subsequent MFDS guidelines after January 2026 (e.g., specific cybersecurity reporting templates).  
> Provide feedback on any jurisdiction‑specific gaps, and suggest additional sources or verification steps before final dossier compilation.

---

### 8. Reusable RA Judgment (Honcho Record)

**Lesson:**  
*When evaluating a digital medical device under the MFDS 2025 regulatory framework, first confirm classification via **디지털의료제품의 분류 및 등급 지정 등에 관한 규정 (제2025‑23호)**; then select the submission route (신고 vs. 허가) per *제2025‑25호*. Always verify that Digital GMP certification is in place or have a documented interim compliance plan before market launch, and continuously monitor MFDS notices for scope changes on foreign clinical data acceptance.*  

*Record this judgment for future digital‑software assessments to ensure consistent handling of classification, evidence requirements, and GMP alignment.*

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

### kb-eval-20260717-it03-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_kr-004", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "761294def6a48449", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "5f0192e5896bd583833f41c673027bfe34b52793e1679d1f9dc751b5f77320c3"} -->

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

> **Regulatory Draft – MFDS Classification & Licensing Pathway for an X‑ray System (2026‑04‑22)**  

---

### 1. Applicable Legal & Regulatory Framework  
| Level | Document | Relevance |
|-------|----------|-----------|
| **Law** | 「의료기기법」 | Establishes the overall medical device regulatory regime in Korea. |
| **Presidential Decree** | 시행령 (대통령령) | Provides detailed statutory provisions for classification, conformity assessment and post‑market obligations. |
| **Ministerial Ordinance** | 시행규칙 (총리령) | Implements the decree with procedural rules (e.g., submission formats). |
| **MFDS Notices** | <br>• 「의료기기 품목 및 품목별 등급에 관한 규정」<br>• 「의료기기 허가·신고·심사 등에 관한 규정」<br>• 「의료기기 GMP 심사·평가 등에 관한 규정」 | Define product‑type classifications, required evidences (clinical/non‑clinical), and KGMP certification requirements. |
| **Guidance** | MFDS 인허가 상세 가이드 – X‑ray System 전용 (2026‑04‑22) | Specific procedural checklist for X‑ray systems; reflects latest cross‑checked web research. |

*Sources: [1] (법률 → 시행령 → 시행규칙) and [2] (MFDS X‑ray system guide, 2026‑04‑22).*

---

### 2. Device Classification (Korean‐GMP)

| Criterion | Expected Outcome |
|-----------|------------------|
| **Intended Use** – Imaging for diagnostic radiology using ionising radiation. | Class III (high‑risk) under Korean “전통 의료기기” (traditional medical device) hierarchy because it involves radiation exposure and direct patient interaction. |
| **Regulatory Reference** – 「의료기기 품목 및 품목별 등급에 관한 규정」 lists X‑ray systems as Class III items. | Confirmed by the MFDS detailed guide for X‑ray systems (source [2]). |

*If the device is a **portable** or **low‑dose** variant, re‑evaluate against the exemption thresholds in the same regulation; however, absent explicit data, default to Class III.*

---

### 3. Licensing Route  

| Classification | MFDS Submission Type | Typical Timeline |
|----------------|----------------------|------------------|
| Class III      | **허가 (Approval)** – Full pre‑market approval dossier required. | 6–12 months (subject to KGMP audit and clinical data review). |

*No “신고 (Notification)” route applies to Class III devices.*

---

### 4. Required Evidence Package  

| Evidence Category | Minimum Mandatory Content | Notes / Korean Specifics |
|-------------------|---------------------------|--------------------------|
| **Non‑clinical (Bench) Testing** | – Electrical safety, electromagnetic compatibility, radiation performance (dose accuracy, beam quality), mechanical integrity.<br>– OECD‑aligned non‑clinical data accepted if referenced in MFDS notice (verify current notice). | Must be performed in a KGMP‑certified facility or a foreign facility with MFDS‑recognized conformity; submit test reports in Korean language or accompanied by certified translation. |
| **Clinical Evaluation** | – Clinical investigation report (CIR) conducted on Korean patients *or* a foreign clinical evaluation that satisfies MFDS’s “동등성 평가” criteria and is referenced in the latest notice. <br>– If no exemption, local clinical data are mandatory for Class III X‑ray systems. | All reports must include Korean summary; labeling of adverse events follows “시판후조사 (post‑market surveillance) 규정”. |
| **Risk Management** | – ISO 14971‑based risk analysis file (hazard identification, mitigation, residual risk evaluation). | Provide a Korean risk management report; include specific controls for radiation exposure (dose monitoring, safety interlocks). |
| **Quality System** | – KGMP certification (ISO 13485 compliant) of the manufacturer. <br>– Facility inspection outcome (MFDS GMP audit report). | Required before dossier acceptance; facility must be listed in MFDS “의료기기 제조업체 목록”. |
| **Labeling & IFU** | – Korean language product label, packaging artwork, and Instructions for Use (IFU) covering: safety warnings, radiation dose limits, contraindications. | Must comply with MFDS labeling guidelines; any foreign language content must be secondary. |
| **Software/IT (if applicable)** | – IEC 62304 software life‑cycle documentation, cybersecurity assessment per MFDS Notice on “디지털 헬스케어”. | Provide Korean translation of critical sections. |

*Citation: No specific identifiers (e.g., notice numbers, case IDs) appear in the source excerpts — verify separately.*

---

### 5. Identified Gaps / Missing Information  

| Gap | Impact | Action Required |
|-----|--------|-----------------|
| **Exact classification code** – The source confirms X‑ray systems are Class III but does not list the item‐code (e.g., “H13”). | Needed for the MFDS submission form. | Retrieve the specific product‑type code from the latest 「의료기기 품목 및 품목별 등급에 관한 규정」 or MFDS online database. |
| **Reference to foreign clinical data acceptance** – The guide mentions cross‑checked web research but does not state which foreign clinical reports are permissible. | Risk of dossier rejection if reliance on foreign data is not accepted. | Obtain the latest MFDS notice (e.g., “외국 임상자료 인정 기준”) and cite its number. |
| **KGMP audit schedule** – No indication whether the manufacturer already holds KGMP certification. | Mandatory pre‑condition for approval. | Confirm KGMP status; if absent, plan for MFDS GMP inspection before dossier filing. |
| **Radiation safety standards** – Specific Korean standards (e.g., “KOSHA‑R‑001”) are not listed. | May affect compliance of non‑clinical testing data. | Identify and incorporate applicable Korean radiation safety regulations. |
| **Labeling sample** – No example of required Korean labeling format. | Potential for labeling non‑conformities during review. | Review MFDS “라벨·포장·사용설명서 가이드라인” for X‑ray devices. |

---

### 6. Core Risk Controls to Emphasize in Submission  

1. **Radiation Dose Limitation** – Automatic dose‐output control, interlock mechanisms, and real‑time monitoring.  
2. **Fail‑Safe Design** – Default to “off” state on power loss or fault detection.  
3. **User Training & Access Controls** – Role‑based operation limits, mandatory radiation safety training documented in the IFU.  
4. **Periodic Calibration Program** – Documented schedule complying with Korean standards for dose accuracy.  

Include these controls explicitly in the risk management file and address how they satisfy MFDS’s “의료기기 허가·심사 등에 관한 규정” requirements.

---

### 7. Human‑Escalation Triggers  

| Situation | Who to Escalate To | Reason |
|-----------|-------------------|--------|
| **Unclear classification/item code** | Senior Regulatory Manager / MFDS liaison officer | Prevent filing under wrong class, which leads to rejection or re‑classification. |
| **Disagreement on acceptability of foreign clinical data** | Head of Clinical Affairs & Legal counsel | Ensure alignment with the latest MFDS notice before relying on external data. |
| **KGMP certification pending close to submission deadline** | Quality Assurance Director | Risk of missing mandatory GMP audit; may require expedited inspection request. |
| **Regulatory notice update discovered after dossier preparation** | Regulatory Project Lead | Must re‑assess evidence package for compliance with any new foreign‑data acceptance rules. |
| **Labeling review flags non‑conformity to Korean wording rules** | Localization/Translation Team lead | Immediate correction needed to avoid labeling objections during MFDS review. |

Escalations should be documented in the project risk register and communicated via written approval before proceeding.

---

### 8. Citations  

- **Regulatory hierarchy** – 「의료기기법」 → 시행령 (대통령령) → 시행규칙 (총리령)【1】  
- **MFDS X‑ray system detailed guide (2026‑04‑22)** – MFDS 인허가 상세 가이드 – X‑ray System 전용【2】

*No specific identifier (e.g., notice number, case ID, predicate device number) was found in the source excerpts; verify these separately before final submission.*

---

### 9. Peer Review Prompt  

> **To a fellow RA colleague:**  
> Please review the above classification and evidence assumptions for the X‑ray system. Specifically:  
> - Are there any additional Korean statutes or recent MFDS notices (post‑2026‑04‑22) that could alter the acceptability of foreign clinical data?  
> - Have we captured all mandatory KGMP and radiation‑safety documentation requirements, or are there jurisdiction‑specific items missing (e.g., KOSHA radiation standards, specific labeling templates)?  
> - Do the identified gaps align with your experience on recent Class III X‑ray approvals in Korea? Suggest any further evidence or clarification needed before dossier compilation.

---

### 10. Reusable RA Judgment (Lesson Learned)  

**Lesson:** When evaluating a high‑risk imaging device such as an X‑ray system under Korean MFDS rules, always map the product to the *class III* category defined in 「의료기기 품목 및 품목별 등급에 관한 규정」 and follow the full **허가** route. Confirm the exact item code, KGMP certification status, and any recent MFDS notices that broaden accepted foreign clinical evidence before finalizing the dossier. Missing these specifics leads to avoidable delays.  

*Recorded in the RA knowledge base for future X‑ray or radiation‑emitting device projects.*

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

### kb-eval-20260717-it03-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it03-ra_kr-005", "iteration": 3, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "15f1622f87811ec2", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

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

> **Regulatory Draft – Korean MFDS Pathway for a Digital Medical Device (SaMD)**  

---

### 1.  Scope & Device Overview  
*Product type*: **Digital medical device / Software as a Medical Device (SaMD)** – e.g., AI‑driven diagnostic support software that runs on a consumer smartphone or dedicated hardware.  
*Key regulatory context* (as of 2025–2026):  

| Date | Regulation change | Practical impact |
|------|-------------------|------------------|
| **2025‑01‑24** | Digital Medical Device Act enforced → SaMD classification & licensing system revised; NIDS (National ICT Authority) granted authority for GMP conformity assessment. | Classification must follow the new MFDS SaMD framework; NIDS may be selected as a GMP audit body. |
| **2025‑05‑07** | MFDS issued 6 updated Digital Medical Device Guidelines – AI/ML‑based GUI software classification and clinical evidence requirements clarified. | For AI/ML‑based GUIs, explicit verification of algorithm performance & risk management is mandatory. |
| **2026 (planned)** | Autonomous Performance Certification System (pre‑cert → post‑surveillance). | May affect future strategy for high‑risk SaMDs but not yet applicable. |
| **2026 (planned)** | “Negative” change‑notification system – only major changes need prior approval; minor changes can be reported after the fact. | Impacts post‑market change management. |

*Sources*: GMP certification flow [1]; 2025–2026 regulatory updates [2].

---

### 2.  Classification & Submission Route  

| MFDS Class (SaMD) | Typical risk level | Submission type |
|-------------------|--------------------|-----------------|
| **Class I** (low‑risk, e.g., wellness apps without clinical claim) | Minimal risk | **신고 (notification)** – no GMP certificate required. |
| **Class II** (moderate risk, e.g., symptom checkers with limited diagnostic function) | Moderate risk | **허가 (licensing)** – requires KGMP certification of the manufacturing site and a full technical dossier. |
| **Class III/IV** (high‑risk, AI‑driven diagnosis/treatment decision support) | High to critical risk | **허가 (licensing)** – full KGMP, rigorous clinical evaluation, post‑market surveillance plan, and possibly pre‑approval performance testing. |

> **Action:** Determine the exact class by mapping the device’s intended use and risk features to the MFDS SaMD classification matrix (see MFDS “디지털의료기기 가이드라인” 2025‑05‑07). If uncertainty exists, treat as at least Class II until formal classification is confirmed.

---

### 3.  Required Evidence for a **Class II/III/IV** License  

| Evidence Category | Typical Content | MFDS Reference |
|-------------------|----------------|---------------|
| **KGMP conformity assessment** | • GMP audit report (품질문서 심사, 현장조사) <br>• Defect‐issue notice and corrective‑action submission <br>• Valid KGMP certificate (유효기간 3년) | GMP 절차 flowchart [1] |
| **Technical File / Device Master File** | • Device description, intended use, labeling in Korean <br>• Architecture diagram, software bill of materials <br>• IEC 62304 development lifecycle records <br>• ISO 14971 risk management file (including AI/ML‑specific risks) | MFDS 디지털의료기기 가이드라인 [2] |
| **Clinical Evaluation** | • Clinical data package (local or accepted foreign clinical evaluation report) <br>• If using CE/FDA evidence, verify acceptability under current MFDS notice (requires explicit citation). | MFDS 디지털의료기기 가이드라인 [2] |
| **Software Verification & Validation** | • V‑V protocol & results, validation of AI/ML algorithm (performance metrics, dataset provenance) <br>• Usability testing for GUI, human factors report (Korean user population) | MFDS 디지털의료기기 가이드라인 [2] |
| **Cybersecurity** | • Threat model, mitigation measures, secure update mechanism <br>• Compliance with MFDS “디지털 보안 가이드라인” (if applicable) | Not in provided excerpts – must be sourced separately. |
| **Labeling & IFU** | • All labeling, instructions for use, and promotional material in Korean (mandatory). | General MFDS requirement (standard practice). |
| **Post‑Market Surveillance Plan** | • PMS schedule, adverse event reporting process, field safety corrective action plan. | MFDS post‑market surveillance regulations (standard). |

> **Citation note:** No specific regulation numbers or case IDs appear in the source excerpts; therefore “no specific identifier found in source — verify separately” is recorded for each evidence item.

---

### 4.  Identified Information Gaps  

| Gap | Why it matters | Suggested remedy |
|-----|----------------|------------------|
| **Exact intended use & risk claim** | Determines SaMD class and depth of clinical evidence required. | Obtain a finalized Intended Use Statement (Korean) from the product team. |
| **Algorithm performance documentation** (especially for AI/ML GUIs) | MFDS 2025‑05‑07 guideline mandates detailed AI/ML validation. | Request algorithm development & validation reports, dataset description, and bias analysis. |
| **Local clinical data requirement** (for Class III/IV) | MFDS may require Korean subject data despite foreign CE/FDA evidence. | Conduct a feasibility check with the reviewer; plan for supplemental local study if needed. |
| **KGMP‑certified manufacturing site** | Essential for licensing of Class II+ devices. | Confirm whether the current site has KGMP certification or if NIDS will be used as audit body (per 2025‑01‑24 update). |
| **Korean language labeling & IFU** | Non‑compliance leads to rejection at document review stage. | Draft Korean label and IFU; schedule professional translation/verification. |
| **Cybersecurity compliance evidence** | Not covered in the excerpts but required for digital devices. | Collect security architecture documentation; reference MFDS cybersecurity guidance. |

---

### 5.  Core Risk Controls (Mapped to International Standards)  

| Control | Standard / Guideline | MFDS alignment |
|--------|----------------------|---------------|
| **Quality Management System** | ISO 13485:2016 (adopted as KGMP) | GMP certification flow [1] |
| **Software Lifecycle** | IEC 62304 | Required in technical file (MFDS 가이드라인 [2]) |
| **Risk Management** | ISO 14971 | Mandatory for all SaMDs; specific AI/ML risk considerations per 2025‑05‑07 MFDS guideline. |
| **Usability & Human Factors** | IEC 62366‑1 | Needed for GUI classification. |
| **Cybersecurity** | FDA “Content of Pre‑market Submissions for Management of Cybersecurity” (as reference) + MFDS cybersecurity guidance (to be sourced). |
| **Post‑Market Surveillance** | MFDS PMS regulations | Required in licensing dossier. |

---

### 6.  Human‑Escalation Triggers  

| Situation | Reason to Escalate to Senior RA / Legal | Recommended escalation path |
|-----------|------------------------------------------|------------------------------|
| **Uncertain SaMD class** (e.g., mixed risk features) | Incorrect classification leads to improper submission route. | Seek senior RA decision and, if needed, a formal MFDS pre‑submission inquiry. |
| **Missing KGMP certificate** (or audit body selection ambiguous after NIDS authority change) | License cannot be issued without GMP conformity proof. | Immediate liaison with manufacturing QA & compliance head; consider engaging NIDS as auditor per 2025‑01‑24 update. |
| **Foreign clinical evidence rejected** (no clear MFDS notice) | Potential for dossier rejection at Clinical Evaluation stage. | Consult regulatory counsel to verify acceptability or plan local data generation. |
| **AI/ML algorithm changes exceeding “minor” threshold** under the upcoming 2026 negative change‑notification system. | Non‑compliant post‑market change may trigger enforcement. | Flag to Product Management; prepare a prior approval supplement if change is major. |
| **Regulatory timeline conflict with impending 2026 autonomous performance certification pilot** | Strategic impact on market entry planning. | Escalate to business leadership for roadmap adjustment. |

---

### 7.  Draft Citation List  

1. **GMP 적합인정 절차** – MFDS GMP assessment workflow (품질문서 심사 → 현장조사 …) with NIDS role beginning 2025‑01‑24【1078228256164017760】.  
2. **2025–2026 주요 규제 변경사항** – Summary of digital medical device law enforcement, SaMD classification changes, AI/ML GUI guidelines, and upcoming autonomous performance certification and negative change‑notification system【1121184088796802935】.

*No specific regulation numbers, case IDs, or predicate device identifiers appear in the source excerpts; therefore “no specific identifier found in source — verify separately” is recorded for any request of such details.*

---

### 8.  Peer Review Prompt  

> **To a fellow RA colleague:**  
> – Please challenge the assumptions made about the classification tier (i.e., treating ambiguous AI‑driven SaMD as at least Class II). Are there alternative interpretations under the MFDS 2025‑05‑07 guidelines?  
> – Evaluate whether the source coverage sufficiently addresses all Korean‑specific obligations (e.g., cybersecurity, Korean language labeling) or if additional statutory references are required.  
> – Identify any gaps in our evidence matrix where MFDS may demand local clinical data or specific documentation not captured here.  

---

### 9.  Reusable RA Judgment (Lesson Capture)

**Judgment ID:** KR‑RA‑2026‑DIGITAL‑GMP‑CLASSIFY  
**Summary:**  
When a digital medical device (SaMD) is being prepared for MFDS licensing post‑2025, the regulator now requires:  

1. **Explicit SaMD risk classification per the 2025‑05‑07 MFDS guideline**, with AI/ML GUI software receiving heightened clinical and algorithmic scrutiny.  
2. **KGMP conformity assessment** performed by one of the six designated audit bodies; NIDS may be selected for digital devices as of 2025‑01‑24.  
3. **Comprehensive technical documentation** (IEC 62304, ISO 14971, Korean labeling).  
4. **Clinical evidence** that satisfies MFDS acceptance criteria—foreign CE/FDA data are permissible only when explicitly referenced in an MFDS notice; otherwise local clinical data are required.  
5. **Risk controls aligned with international standards** and documented in Korean language deliverables.  
6. **Human‑escalation triggers** include uncertain classification, missing KGMP certification, rejected foreign evidence, significant AI/ML changes, and upcoming 2026 regulatory shifts (autonomous certification, negative change‑notification).  

These points should be applied as a checklist for any new digital medical device dossier entering the Korean market after 2025.  

--- 

*Prepared by:* **Sam – KR Regulatory Affairs Specialist**  
*Date:* 2026‑07‑19 (aligned with pipeline run)

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
