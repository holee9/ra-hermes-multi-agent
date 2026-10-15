# KB Eval Checksheet - 2026-10-15 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261015-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f3ad4313f3421a8e", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f3ad4313f3421a8e`
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

### 1. Device Classification & Submission Pathway
| Item | Determination |
|------|----------------|
| **Regulatory panel** | Imaging‑related devices fall under **21 CFR Part 892** (Radiology / imaging). |
| **Class** | Most image‑management and processing systems are Class II, regulated under **§892.2050** (Medical image management and processing system). *Citation*: no specific identifier found in source — verify separately. |
| **Submission type** | Traditional **510(k) Premarket Notification** (Section 807). The submission will consist of: 1) Predicate device identification, 2) Substantial equivalence comparison table, 3) 510(k) Summary, 4) Performance testing, 5) Biocompatibility, 6) EMC (electromagnetic compatibility). *Citation*: no specific identifier found in source — verify separately. |

---

### 2. Predicate Device Strategy
| Step | Action |
|------|--------|
| **Predicate search** | Use the FDA 510(k) database to locate cleared devices with the same intended use and technology (e.g., other PACS‑type processing/analysis software). *Citation*: source line “Predicate Device 조사 (FDA 510(k) Database)”【2】 |
| **Substantial equivalence matrix** | Populate a side‑by‑side comparison of: • Intended Use, • Technological Characteristics, • Performance specifications, • Labeling. Highlight any differences and provide supporting data to demonstrate that the differences do not raise new safety or effectiveness concerns. *Citation*: source line “Substantial Equivalence 비교표 작성”【2】 |
| **Predicate selection criteria** | Choose a predicate with: <br>‑ Same Class (II) and same §892 subsection; <br>‑ Cleared within the last five years (to leverage recent guidance); <br>‑ No pending regulatory actions. |

---

### 3. Required Evidence Packages
| Category | Typical Content | Notes |
|----------|-----------------|-------|
| **Device Description & IFU** | Detailed device architecture, software versioning, user interface screenshots, labeling/Instructions for Use (IFU). *Citation*: source “Device Description / Indications for Use 작성 가이드”【1】 |
| **Performance Testing** | • Benchmarking against predicate (image quality metrics, processing speed). <br>• Accuracy & precision of analysis algorithms. <br>• Stress testing under worst‑case conditions. |
| **Biocompatibility** | ISO 10993‑1 compliant assessment for any patient‑contact materials (e.g., monitor housing, cables). |
| **Electromagnetic Compatibility (EMC)** | IEC 60601‑1‑2 compliance testing (radiated and conducted emissions/reception). |
| **Software Validation** | Verification/validation per FDA’s “General Principles of Software Validation” guidance; include a Predetermined Change Control Plan (PCCP) if post‑market algorithm updates are anticipated. *Citation*: no specific identifier found in source — verify separately. |
| **Labeling** | 21 CFR Part 801 requirements; UDI labeling per 21 CFR Part 830 (label must bear a UDI). *Citation*: no specific identifier found in source — verify separately. |

---

### 4. Identified Gaps / Missing Information
| Gap | Impact | Action Required |
|-----|--------|-----------------|
| **Predicate device numbers** | Needed for the comparison table and to reference cleared devices in the submission. | Conduct detailed FDA 510(k) database search; capture K‑Numbers. |
| **Specific performance test protocols** | Without clear protocol, cannot demonstrate equivalence. | Draft test plans aligned with predicate’s test methods (refer to their Summary/Device History Files). |
| **Biocompatibility data for all patient‑contact components** | Absence may trigger FDA information requests. | Perform ISO 10993 testing or provide existing data package. |
| **EMC test reports** | Required for Class II devices; missing data delays clearance. | Arrange IEC 60601‑1‑2 testing in an accredited lab. |
| **Predetermined Change Control Plan (PCCP) outline** | If the software includes AI/ML, FDA expects a PCCP to manage future algorithm updates. | Draft PCCP describing change categories, pre‑market review pathways, and post‑market monitoring. |
| **UDI implementation details** | UDI assignment is mandatory; lacking this may cause submission deficiencies. | Generate device identifier per 21 CFR Part 830, register in GUDID. |

---

### 5. Risk Controls (per ISO 14971 / FDA QMSR)
1. **Hazard Identification** – List all software‑related hazards (e.g., incorrect image processing, data corruption).  
2. **Risk Mitigation** – Implement: <br>‑ Robust input validation; <br>‑ Redundant storage; <br>‑ Audit trails for algorithm versioning; <br>‑ User training & warnings in IFU.  
3. **Verification of Controls** – Include verification test results in the submission.  
4. **Post‑Market Surveillance** – Define a PMS plan (complaint handling, adverse event reporting per 21 CFR Part 803).  

*Citation*: no specific identifier found in source — verify separately.

---

### 6. Human‑Escalation Triggers
| Situation | Trigger |
|-----------|---------|
| **Missing predicate identifiers** | Escalate to senior RA lead for database extraction before draft can proceed. |
| **Unresolved performance gaps after initial testing** | Flag to engineering leadership; may require redesign or additional validation. |
| **FDA issuing an Additional Information (AI) request** | Immediately involve the regulatory project manager and technical SMEs to prepare a response within the FDA‑specified timeframe. |
| **Changes to intended use emerging from market feedback** | Initiate a supplemental 510(k) or De Novo evaluation; escalate to QA/QMS for impact assessment. |
| **Discovery of non‑conformities in QMSR (Part 820) during internal audit** | Escalate to compliance officer and consider filing a corrective/preventive action (CAPA). |

---

### 7. Summary Judgment
- The device is most likely a **Class II medical image management and processing system** under **§892.2050**, requiring a **traditional 510(k) submission**.
- Core evidence: predicate comparison, performance testing, biocompatibility, EMC, software validation, labeling, and UDI compliance.
- Several critical data elements (predicate numbers, test protocols, PCCP) are currently missing; they must be obtained before the submission can be finalized.

---

### 8. Peer Review Prompt
> **@RA‑Team** – Please challenge the assumptions above:  
> • Are we confident that §892.2050 is the correct classification for this specific functionality?  
> • Does the source provide enough guidance on the exact sections to cite, or should we verify additional FDA guidance documents (e.g., 2024 AI/ML Change Control Guidance)?  
> • Have we captured any jurisdiction‑specific gaps, such as state‑level radiology regulations, that might affect the 510(k) strategy?  

Your feedback will be incorporated before finalizing the submission package.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 'predicate의 Device History Files' → predicate 공개문서는 510(k) Summary(DHF는 자사 내부 문서)로 수정. §892.2050 검증 플래그 처리는 모범적.

**Source Excerpts**

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20261015-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "7c3c4dd45c90a84c", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `7c3c4dd45c90a84c`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/FDA_%EC%9E%84%EC%83%81%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%95%84%EC%9A%94%ED%8C%90%EB%8B%A8_%EA%B8%B0%EC%A4%80.md)
- Source hash: `36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `FDA_임상데이터_필요판단_기준.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-...
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

### 1. Bottom‑Line Recommendation  
- **Primary pathway:** Premarket Notification (510(k)) — seek substantial equivalence to an FDA‑cleared predicate that matches the intended use, technology, and risk profile.  
- **Escalation trigger:** If no legally marketed predicate exists or if the device’s technological differences exceed typical SE limits, move to a De Novo request; if the device is Class III or requires pivotal clinical data, prepare a PMA.

---

### 2. Classification & Submission Route  

| Attribute | Determination |
|-----------|---------------|
| **Regulatory basis** | FD&C Act §510(k) and **21 CFR §807** (submission, establishment registration/listing). |
| **Device class** | Class II (default for most imaging/diagnostic hardware; confirm via 21 CFR §892 classification panel). |
| **Predicate requirement** | Mandatory – a cleared device that demonstrates the same intended use and comparable technological characteristics. |
| **Clinical data** | Conditional – required only if the SE comparison is insufficient to resolve safety & effectiveness (see §3 of FDA guidance “FDA 임상데이터 필요 판단 기준”). *No specific identifier found in source — verify separately.* |

---

### 3. Evidence Package for a 510(k) Submission  

| Required Element | Detail |
|------------------|--------|
| **Device description** | Full specification, labeling, intended use statement, and user environment. |
| **Predicate comparison matrix** | Side‑by‑side table covering: indications for use, technology (hardware/software), performance specifications, and risk profile. Highlight ≤ 30 % differences in design or performance parameters. |
| **Performance testing** | Bench, benchtop, and (if applicable) animal studies per recognized standards (e.g., IEC 60601‑2‑xx for imaging equipment). |
| **Software validation** (if applicable) | Verification & validation reports; reference the Predetermined Change Control Plan (PCCP) if a post‑market change‑control strategy is anticipated. |
| **Risk management** | ISO 14971‑based risk analysis, including residual risk justification and mitigation measures. |
| **Labeling** | Draft labels complying with **21 CFR §801** (including UDI per **21 CFR §830**). |
| **Quality System** | Conformity to the QMSR (**21 CFR §820**, effective 02‑2026, ISO 13485‑aligned). |
| **Clinical data** | Include only if the SE argument cannot address safety/efficacy; otherwise reference FDA guidance “clinical data: 조건부 (§3)”. *No specific identifier found in source — verify separately.* |

---

### 4. Missing Information – Items to Obtain Before Submission  

1. **Exact intended use & patient population** (including any off‑label expansions).  
2. **Candidate predicate devices** – FDA 510(k) numbers, release dates, and labeling excerpts.  
3. **Technical specifications** – detailed schematics, software architecture, and performance thresholds.  
4. **Risk analysis results** – list of identified hazards and corresponding mitigations.  
5. **Labeling draft** (including UDI carrier format).  
6. **Evidence of compliance with current QMSR (Part 820) and UDI (Part 830) requirements.**  

---

### 5. Risk Controls & Standards  

- **Risk Management:** ISO 14971:2019 (risk analysis, evaluation, control).  
- **Electrical Safety / EMC:** IEC 60601‑1 series as applicable to imaging hardware.  
- **Software Lifecycle:** IEC 62304; incorporate a **Predetermined Change Control Plan (PCCP)** for post‑market algorithm updates.  
- **Quality Management System:** QMSR – **21 CFR §820** (ISO 13485‑aligned) effective 02‑2026.  

---

### 6. Key Citations  

| Item | Citation |
|------|----------|
| Legal basis for 510(k) | FD&C Act §510(k); **21 CFR §807** |
| Predicate requirement | *mandatory* – same source as above |
| Clinical‑data condition | “조건부 (§3 참조)” – *no specific identifier found in source — verify separately* |
| De Novo legal basis (if needed) | FD&C Act §513(f)(2); **21 CFR §860** |
| PMA legal basis (if needed) | FD&C Act §515; **21 CFR §814** |
| Imaging‑device classification panel | 21 CFR Part 892 (radiology & imaging devices) – confirm exact sub‑section for the device type. |
| UDI requirements | **21 CFR §830** (general provisions onward). |
| QMSR requirement effective Feb 2026 | **21 CFR §820** (ISO 13485‑aligned). |
| Predetermined Change Control Plan guidance | FDA Final Guidance, Dec 2024 – “Predetermined Change Control Plan (PCCP)”. |

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **No suitable predicate** identified after exhaustive search of FDA’s 510(k) database. | Escalate to senior RA for De Novo feasibility study. |
| **Technological differences > 30 %** or new risk category uncovered in ISO 14971 analysis. | Escalate for clinical data requirement assessment; consider De Novo or PMA pathway. |
| **QMSR non‑conformance** (e.g., missing CAPA records, incomplete design controls). | Pause submission; involve Quality Assurance leadership to remediate. |
| **UDI implementation gaps** (label lacks required UDI format). | Escalate to labeling/Regulatory Operations for corrective action before filing. |
| **FDA feedback requesting additional clinical evidence** during 510(k) review. | Initiate supplemental clinical protocol development and submit a revised 510(k) response. |
| **Regulatory timeline shift** (e.g., new guidance affecting classification). | Notify project manager; reassess pathway selection with updated regulatory intelligence. |

---

### 8. Peer‑Review Prompt  

> *@RA‑Colleague*: Please review the predicate‑selection assumptions, the completeness of the evidence matrix, and any jurisdiction‑specific gaps (e.g., alignment with the new QMSR or UDI implementation details). Highlight any missing identifiers or sections that need verification against the latest FDA guidance.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> '차이 ≤/> 30%' — FDA SE 기준에 존재하지 않는 수치. SE는 정성 판정(2014 'The 510(k) Program' 가이던스). 경로별 근거표(§510(k)·§513(f)(2)/§860·§515/§814)는 원문 충실.

**Source Excerpts**

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20261015-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "0d1acd7931396d8b", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `0d1acd7931396d8b`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_02_Substantial_Equivalence.md)
- Source hash: `3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_02_Substantial_Equivalence.md`는 FDA 510(k) substantial equivalence와 predicate 비교 항목을 정리한 eSTAR 작성 문서입니다.
- 현재 excerpt 핵심: ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medi...
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

> **Regulatory Draft – Imaging Workstation Software (GUI) – 510(k) Predicate Strategy**

---

### 1. Device Overview & Intended Use  
- **Device type:** Clinical imaging work‑station software that provides acquisition, processing, display, storage and transfer of radiology images; may include AI/ML‐based analysis tools.  
- **Intended use (proposed):** “To acquire, process, view, store and transmit DICOM‑compliant medical images for diagnostic interpretation in radiology departments. Optional AI/ML functions provide automated lesion detection assistance within the same workflow.”  

---

### 2. Classification & Submission Route  

| Item | Determination |
|------|---------------|
| **Regulatory class** | Class II device (medical image management and processing system) – per FDA’s imaging‑device classification table. <br>*Citation:* no specific identifier found in source — verify separately (expected §892.2050). |
| **Premarket submission** | Traditional 510(k) with substantial equivalence claim. |
| **QMS requirement** | Must operate under the Quality Management System Regulation (QMSR, 21 CFR 820) effective 02‑Feb‑2026. |

---

### 3. Predicate Strategy (per source checklist)

1. **Search FDA 510(k) database by product code** – identify all cleared devices with the same product code within the past 5 years; prioritize those ≤5 yr old.  
2. **Age filter:** If a candidate is >7 yr old, prepare additional justification (FDA “use of predicates” modernization trend).  
3. **Market status check:** Confirm each predicate is still commercially available (no retire/discontinue flag).  
4. **Recall/safety‑communication review:** Verify no open recalls or MAUDE safety alerts for the predicate.  
5. **Indications‑for‑Use (IFU) comparison:** The sponsor’s IFU must be identical to or narrower than the predicate’s wording, at the literal text level.  
6. **Technical differences matrix:** List every functional/technological deviation; attach supporting data that demonstrates no new safety–effectiveness concerns.  
7. **Split‑predicate prohibition:** Use a single primary predicate for IFU equivalence; secondary “supporting” predicates only for ancillary features after the primary equivalence is established.  

*All steps above are directly taken from the source checklist (Excerpt [1]).*

---

### 4. Required Evidence & Documentation

| Evidence | Source Requirement | Comments |
|----------|-------------------|----------|
| **Predicate list with K‑numbers** | Checklist step “FDA 510(k) Database … 검색” | Must include clearance number, product code, and status. |
| **Side‑by‑side IFU comparison** | “Indications for Use 원문 문자 수준 비교” | Provide full text excerpts; highlight any narrower phrasing. |
| **Technical differences justification** | “기술특성 차이 항목 목록화 … 데이터 확보 가능성 확인” | Include bench, simulation or clinical data as needed. |
| **Software Documentation Level** (Basic vs Enhanced) | FDA 2023 Software Guidance (referenced in Excerpt [2]) | Determine appropriate level; if Enhanced, include verification/validation traceability matrices. |
| **IEC 62304 safety class determination (A/B/C)** | Excerpt [2] | Class‑C devices will need more rigorous V&V and risk control evidence. |
| **Risk Management File** (ISO 14971) | Implicit – required for all software medical devices. |
| **Cybersecurity Plan** (access controls, encryption, audit logs, update mechanisms) | “보안 조치 … 인증 방식, 암호화, 감사로그, 업데이트 경로” | Align with FDA’s 2022 Cybersecurity “Content of Premarket Submissions”. |
| **DICOM Conformance Statement** (SCU/SCP, Worklist, MPPS, Print, etc.) | “DICOM 적합성 진술서 …” | Must reference DICOM PS3‑10 and IHE profiles if claimed. |
| **AI/ML Component Documentation** – Predetermined Change Control Plan (PCCP) | “AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정” | Provide PCCP scope, change categories, monitoring plan per FDA Dec 2024 guidance. |
| **Software Bill of Materials (SBOM)** (SPDX or CycloneDX format) | “SBOM 제공 형식 …” | Include third‑party component versions; map to known vulnerabilities. |
| **Interoperability Claims** (HL7 FHIR, IHE profiles) | “Interoperability (HL7 FHIR, IHE profiles 지원 여부)” | Provide test reports for each claimed integration. |
| **Labeling & UDI** | 21 CFR 801 & 830 | Include device label, IFU, and UDI data sheet; register in GUDID. |

---

### 5. Identified Gaps / Missing Information (to be supplied before filing)

1. **Concrete predicate K‑numbers** – only the selection process is described; exact cleared devices have not been listed.  
2. **Full Proposed IFU text** – needed for literal comparison with predicates.  
3. **Technical differences matrix** – currently a placeholder; must be populated with quantitative/qualitative justification data.  
4. **Software risk class (IEC 62304)** – classification not yet assigned; impacts the depth of V&V required.  
5. **Cybersecurity threat model & mitigation plan** – high‑level mention only; need detailed architecture and test results.  
6. **PCCP documentation** – if AI/ML is present, a completed PCCP (scope, change categories, post‑market monitoring) must be attached.  
7. **SBOM export** – format choice decided but actual SBOM not generated.  
8. **DICOM conformance testing reports** – evidence of passing DICOM compliance suites absent.  
9. **Interoperability test data** (FHIR/IHE) – no proof of successful integration yet provided.  

---

### 6. Risk Management & Controls

| Control | Rationale |
|---------|-----------|
| **ISO 14971 risk analysis** (hazard identification, severity/probability ranking, mitigation) | Core FDA requirement for all medical devices. |
| **IEC 62304 lifecycle processes** (development planning, configuration management, verification/validation) | Aligns software safety class with required V&V depth. |
| **Cybersecurity measures** – authentication, encryption of PHI at rest/in transit, immutable audit log, secure OTA update path | Addresses FDA 2022 cybersecurity guidance and protects against ransomware/unauthorized access. |
| **PCCP for AI/ML** – pre‑specified change categories, monitoring plan, periodic performance re‑evaluation | Ensures controlled evolution of algorithm without new 510(k) submissions per Dec 2024 guidance. |
| **DICOM/IHE conformance statements & test reports** | Guarantees interoperability within radiology workflow and compliance with imaging standards. |
| **SBOM + vulnerability management** (e.g., use of NIST CVE database) | Enables rapid response to component‑level security findings. |
| **Labeling clarity (21 CFR 801)** – explicit warnings for AI assistance, user training requirements | Mitigates misuse or overreliance on decision‑support algorithms. |
| **UDI assignment & GUDID registration** (21 CFR 830) | Required for market entry and post‑market tracking. |

---

### 7. Regulatory References

| Topic | Reference (as derived from source) |
|-------|------------------------------------|
| Predicate selection checklist – product code search, age filter, market status, recall check, IFU comparison, split‑predicate rule | Excerpt [1] – “Predicate 선정 실무 체크리스트”. |
| Software documentation level (Basic/Enhanced), IEC 62304 class, AI/ML PCCP requirement, DICOM statement, security measures, SBOM format, interoperability claims | Excerpt [2] – “촬영실 GUI SW (Imaging Workstation SW)”. |
| Classification of medical image management & processing systems (Class II) | no specific identifier found in source — verify separately (expected §892.2050). |
| QMSR (21 CFR 820), Labeling (21 CFR 801), UDI (21 CFR 830) | framework references – factual statements, no verification needed. |

---

### 8. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Predicate is discontinued or under active recall** | Pause submission; select alternate predicate; inform senior RA lead. |
| **AI/ML module cannot be fully covered by a PCCP (e.g., unspecifiable future changes)** | Escalate to product leadership for possible De Novo pathway or PMA consideration. |
| **Technical differences introduce new intended uses (broader than predicates)** | Conduct additional clinical data collection; consider filing as a novel device. |
| **Inability to assign IEC 62304 Class C** – insufficient safety‑class justification | Escalate to software engineering lead for redesign or re‑classification; may affect submission timeline. |
| **Cybersecurity plan fails to meet FDA “Content of Premarket Submissions” expectations (e.g., no threat model)** | Route to cybersecurity specialist; update documentation before 510(k) docket finalization. |
| **Missing critical evidence (SBOM, DICOM test report, risk analysis)** after the internal deadline | Notify project manager; reevaluate go‑no‑go decision. |

When any of these triggers occur, a formal **Risk Review Board** meeting should be convened and a written escalation note filed in the regulatory tracking system.

---

### 9. Peer‑Review Prompt  

> *Colleague, please review the assumptions underlying our predicate selection (single primary predicate only), the completeness of the AI/ML change‑control plan, and any jurisdiction‑specific gaps (e.g., European MDR considerations) that may affect this U.S. 510(k) strategy. Highlight missing data sources or alternative pathways you consider prudent.*

--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> FDA 사이버 가이던스 '2022' 인용 오류 — 2018 초안→2023-09-27 최종, 2022 판본 부재(10-10 us-004 이후 재발, #134). Predicate 체크리스트 7단계는 원문 완전 충실.

**Source Excerpts**

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20261015-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "88425b03460ec352", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `88425b03460ec352`
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

> **Regulatory Draft – Imaging‑Acquisition GUI Software (Radiology) – 510(k) Strategy**

| Item | Assessment |
|------|------------|
| **Device Classification** | Class II, imaging‑device software under **21 CFR 892.2050** (Medical image management and processing system). The intended use “acquire, review, and manage digital radiographic images … not for primary diagnosis or interpretation” aligns with the existing predicate class II devices in this panel. |
| **Submission Route** | Traditional **510(k) pre‑market notification** (per 21 CFR 807.87). No indication of eligibility for an abbreviated or special pathway in the source. |
| **Core Submission Sections (per FDA guidance)** | 1. Cover Sheet & Form 3881 (Indications for Use).<br>2. 510(k) Summary (21 CFR 807.92).<br>3. Device Description – software architecture, OS/hardware requirements, compatible detector/generator list, DICOM node functions.<br>4. Substantial Equivalence Comparison to predicate(s).<br>5. Software Validation Report (IEC 62304‑compliant risk class, verification & validation activities, SOUP inventory).<br>6. Cybersecurity Documentation (authenticity, encryption, audit logs).<br>7. Performance Testing (image acquisition quality, DICOM conformance, work‑list and MPPS performance).<br>8. Human Factors / Usability Test (technologist workflow).<br>9. Labeling & IFU (including “not for diagnosis” disclaimer).<br>10. QMS compliance evidence (21 CFR 820, QMSR effective 02‑Feb‑2026). |
| **Required Evidence** | • **Software Development Lifecycle** report per IEC 62304 (risk class B/C as applicable).<br>• **Verification & Validation** data: functional testing, stress/robustness, DICOM SCU/SCP compliance, MPPS timing.<br>• **Cybersecurity**: threat model, mitigation controls, penetration test summary.<br>• **Compatibility Matrix** with listed X‑ray detectors/generators (including firmware versions).<br>• **Usability / Human Factors** study confirming safe use by trained technologists.<br>• **Labeling & IFU** showing intended use and limitation (“not for primary diagnosis”).<br>• **Quality System Records** demonstrating QMSR conformity (design controls, change control – Predetermined Change Control Plan if post‑market updates are anticipated). |
| **Missing / Incomplete Information (from source)** | • Specific predicate device(s) with 510(k) numbers.<br>• Detailed performance test protocols & results (e.g., image quality metrics, DICOM conformance testing reports).<br>• Human factors/usability validation data.<br>• Full cybersecurity risk assessment and mitigation plan.<br>• Complete software BOM for SOUP components.\*<br>• UDI labeling plan per **21 CFR 830** (label must bear a UDI; source does not mention it). |
| **Key Risk Controls (to be documented)** | 1. **Software risk classification & safety controls** – IEC 62304 Class B/C mitigation (e.g., watchdog timers, error handling).<br>2. **Cybersecurity** – authentication, encryption of DICOM transmission, audit logging, periodic vulnerability assessment.<br>3. **Data integrity** – checksum/verification on image acquisition and storage.<br>4. **User training & interface design** – prevent inadvertent “diagnosis” claims; clear UI labeling.<br>5. **Change‑control** – Predetermined Change Control Plan (PCCP) for future algorithm updates or OS patches. |
| **Citations (framework references)** | • 21 CFR 807.87 – required information for a 510(k).<br>• 21 CFR 807.92 – format of the 510(k) Summary.<br>• FDA Guidance “Format for Traditional and Abbreviated 510(k)s” (Final, 13‑Sep‑2019).<br>• FDA Guidance “Electronic Submission Template for Medical Device 510(k) Submissions” (final 2023, eSTAR v5.x).<br>• FDA Guidance “General/Specific Intended Use” (1998 Final).<br>• IEC 62304 – medical device software lifecycle processes. |
| **Human‑Escalation Triggers** | 1. **No identified predicate** – requires expert review to select an appropriate cleared comparator.<br>2. **Missing performance data** – pause submission until test results are generated and reviewed.<br>3. **Incomplete cybersecurity documentation** – escalate to CISO/InfoSec for risk assessment completion.<br>4. **QMSR evidence absent** – involve Quality Assurance lead to gather design‑control records.<br>5. **UDI plan not addressed** – forward to regulatory labeling team for UDI strategy. |
| **Regulatory Judgment** | The GUI software is a Class II imaging acquisition system that must be cleared via a traditional 510(k). All core submission elements are defined in the source, but definitive predicate identification, complete performance testing, human‑factors validation, full cybersecurity risk mitigation, and UDI compliance remain pending. Until these gaps are resolved, the filing cannot proceed to FDA submission. |

---

**Peer Review Prompt**  
> *Request:* A fellow RA colleague, please review the above draft for (a) completeness of predicate identification strategy, (b) any overlooked FDA special or abbreviated 510(k) options for imaging software, and (c) potential jurisdiction‑specific gaps (e.g., state‑level radiation safety rules). Highlight assumptions that may need validation against the full device dossier.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

### kb-eval-20261015-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "a355ace57245bc18", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md", "source_hash": "6c864b98fca94d3a9546fde9cef298ef58210c9ac702628a937bcf05144604b6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `a355ace57245bc18`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/T-FDA510K-B3_SE_%EB%B9%84%EA%B5%90%ED%91%9C_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `6c864b98fca94d3a9546fde9cef298ef58210c9ac702628a937bcf05144604b6`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `T-FDA510K-B3_SE_비교표_템플릿.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 개정 이력 | 버전 | 일자 | 변경 내용 | 작성자 | |------|------|-----------|--------| | v0.1 | 2026-09-09 | 골격 템플릿 신규 생성 (FDA-510K-B3 증빙 미비 해소) | RA 담당자 | --- ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance Section B.3 - FDA 510(k) Premarket Notification Database (predicate 검색·K-number 확인용, 실 predicate 선정 시 필수 조회)
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

> **Regulatory Draft – 510(k) Predicate‑Strategy for New Device Submission**

---

### 1. Classification & Submission Route  
| Item | Determination | Governing Reference |
|------|---------------|---------------------|
| **Device Class** | *To be confirmed* – initial assumption: Class II (most imaging, diagnostic, or software‑based medical devices fall in this range). | 21 CFR § 807.90 (classification criteria) |
| **Regulatory Pathway** | Premarket Notification (510(k)) – “Traditional” submission with substantial equivalence argument. | 21 CFR § 807.92(a) |

> *If the device is found to be novel or lacks an appropriate predicate, consider a De Novo classification request per 21 CFR § 814.94.*

---

### 2. Predicate Identification Strategy  

| Step | Action | Source / Guidance |
|------|--------|-------------------|
| **2.1** | Query the FDA 510(k) Premarket Notification Database for devices with *identical intended use, technology, and indications*.| “Refuse to Accept Policy for 510(k)s” – Guidance Section B.3 (required predicate search). |
| **2.2** | Verify each candidate’s K‑number, classification, and decision summary. | FDA 510(k) database (no specific identifier found in source — verify separately). |
| **2.3** | Prioritize predicates that are *cleared within the last 10 years* and have *publicly available performance data*; document rationale for selection. | 21 CFR § 807.92(b)(1) (substantial equivalence comparison). |

**Outcome:** Compile a short list (≥2) of the most comparable cleared devices, noting their K‑numbers and any known gaps relative to the new device.

---

### 3. Required Evidence Package  

| Category | Minimum Content | Rationale / Regulatory Basis |
|----------|----------------|-----------------------------|
| **Device Description** | Trade name, model, specifications, block diagram, software architecture (if applicable). | 21 CFR § 807.92(b)(2) – description of device. |
| **Intended Use & Indications for Use** | Exact language to be placed on labeling; compare with predicate’s intended use. | 21 CFR § 801.2 (labeling). |
| **Technological Comparison** | Side‑by‑side table covering: principle of operation, materials, energy source, user interface, accessories, and performance claims. | 21 CFR § 807.92(b)(3) – comparison to predicate. |
| **Performance Testing** | • Bench testing (accuracy, precision, repeatability) <br>• Animal or bench‑simulated studies if required (e.g., safety of radiation emitting devices). <br>• Clinical data only when non‑clinical data cannot demonstrate equivalence. | 21 CFR § 820.30 (design verification); ISO 14971 for risk‑based testing. |
| **Software Validation** *(if software component >30 % of device)* | Verification/validation plan, unit tests, integration tests, cybersecurity threat analysis, and *Predetermined Change Control Plan (PCCP)* if AI/ML is used. | FDA Guidance “Predetermined Change Control Plan (PCCP)” – Dec 2024. |
| **Biocompatibility / Sterilization** *(if applicable)* | ISO 10993 testing per device contact level; sterilization validation report. | 21 CFR § 820.50 (process validation). |
| **UDI Compliance** | Device identifier, production identifier, label and packaging format per Part 830. | 21 CFR § 830.10‑830.60 (UDI labeling requirements). |
| **QMSR Alignment** | Evidence of ISO 13485–aligned Quality Management System implementation (post‑Feb 2026 QMSR). | 21 CFR Part 820 (Quality System Regulation) and new QMSR provisions. |

---

### 4. Gaps / Missing Information (based on current documentation)

| Gap | Impact | Required Action |
|-----|--------|-----------------|
| **Predicate K‑numbers not yet identified** | Submission cannot proceed without a documented predicate. | Perform database search per Step 2; if none suitable, consider De Novo pathway. |
| **Risk Management File absent** | ISO 14971 required for design dossier and FDA review. | Conduct risk analysis, generate FMEA/FMECA, define mitigations. |
| **Software Change‑Control Plan not drafted** (if AI/ML or software updates anticipated) | May trigger Refuse to Accept if post‑market modifications are unaddressed. | Draft PCCP detailing permissible algorithm changes and FDA notification triggers. |
| **UDI labeling prototype missing** | Non‑compliance with Part 830 leads to RTA/Refuse to Accept. | Create label mock‑ups with UDI in accordance with 21 CFR § 830.10‑§ 830.60. |
| **Evidence of compliance with new QMSR (effective Feb 2026)** | Absence may be cited as a non‑conforming quality system element. | Provide QMS audit report showing ISO 13485 alignment and Part 820 implementation. |

---

### 5. Risk Controls & Mitigation Strategy  

| Control | Description | Reference |
|---------|-------------|-----------|
| **Design Controls** (per § 820.30) | Requirement specifications, design inputs/outputs, verification, validation, design transfer. | 21 CFR § 820.30 |
| **Risk Management** (ISO 14971) | Identify hazards, estimate risk, implement mitigations, verify effectiveness. | ISO 14971:2023 (framework reference). |
| **Cybersecurity** (if software) | Threat modeling, secure boot, encryption, periodic security updates per PCCP. | FDA Guidance “Predetermined Change Control Plan (PCCP)” – Dec 2024. |
| **Sterilization Validation** (if applicable) | Bioburden testing, cycle qualification, routine monitoring. | 21 CFR § 820.75 (process validation). |
| **Human Factors / Usability** | Conduct formative and summative usability testing to ensure safe use in intended environment. | FDA Guidance “Use of Human Factors Engineering” – 2016 (framework reference). |

---

### 6. Citations  

- **Framework references** (no specific identifier needed):  
  - 21 CFR § 807.92 (substantial equivalence criteria)  
  - 21 CFR § 820.30 (design controls)  
  - 21 CFR Part 892 – imaging device classifications (if the device is an imaging system).  

- **Instance identifiers** (none appear in source excerpts):  
  - *No specific identifier found in source — verify separately.*

---

### 7. Human‑Escalation Triggers  

| Trigger | When to Escalate | Action |
|---------|------------------|--------|
| **No suitable predicate identified after exhaustive search** | ≥5 candidate devices reviewed with no acceptable technological/indication match. | Escalate to senior RA lead for De Novo consideration. |
| **Risk rating ≥ high (risk > 1 × 10⁻³ fatality per use)** or unresolved hazardous failure modes. | Immediate. | Convene cross‑functional risk review; consider PMA route. |
| **Missing QMSR evidence** after 2 weeks of document request. | Immediate. | Notify project manager; pause submission preparation. |
| **UDI labeling non‑conformity detected by QA** | Upon discovery. | Halt final package assembly; correct label design before filing. |
| **FDA Refuse to Accept (RTA) notice received** | At receipt. | Trigger corrective action plan and rapid response team. |

---

### 8. Regulatory Judgment  

*Based on the current evidence set, the device is most plausibly a Class II medical device suitable for a traditional 510(k) submission, provided an appropriate predicate can be documented and all missing items (risk file, UDI labeling, QMSR compliance, PCCP where applicable) are resolved. If no predicate exists or risk analysis reveals high‑severity hazards that cannot be mitigated through design controls alone, a De Novo classification request should be prepared.*

---

### 9. Peer Review Prompt  

*Please review the assumptions above—particularly the provisional device class, the completeness of the required evidence list, and any jurisdiction‑specific gaps (e.g., state‑level reporting requirements). Highlight any missing regulatory citations or alternative pathways that may better suit this product.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [x] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [ ] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> ① 'De Novo per 21 CFR §814.94' — De Novo는 Part 860 Subpart D(§860.200~260), §814.94는 PMA 조항. ② '§807.90 classification criteria' — §807.90은 510(k) 제출 양식 조항. ③ 'ISO 14971:2023' 부존재 판본(현행 2019; 10-10 '14971:2021'과 동일 계열의 판본 창작). ④ 'SW >30%'·'위험 1×10⁻³' 근거 없는 수치. ※ '10년 내 predicate'는 FDA 초안 가이던스(2023-09)의 실제 권고 기준이나 무출처. 원문이 4줄 뼈대(v0.1)라 대부분 일반지식으로 구성.

**Source Excerpts**

1. Chunk `162881704545950641`

> ## 개정 이력 | 버전 | 일자 | 변경 내용 | 작성자 | |------|------|-----------|--------| | v0.1 | 2026-09-09 | 골격 템플릿 신규 생성 (FDA-510K-B3 증빙 미비 해소) | RA 담당자 | ---

2. Chunk `349912156821510479`

> ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance Section B.3 - FDA 510(k) Premarket Notification Database (predicate 검색·K-number 확인용, 실 predicate 선정 시 필수 조회)

## ra_eu

### kb-eval-20261015-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "fbebdcb1e1145fec", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `fbebdcb1e1145fec`
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

> **MDR Classification & Conformity‑Assessment Draft – Ionising‑Radiation Diagnostic Device (X‑ray Generator)**  

---  

### 1. Classification  
| Item | Determination | Reference |
|------|---------------|-----------|
| **Device type** – X‑ray generator that emits ionising radiation for diagnostic purposes. | **Class IIb** (Rule 10) | “Rule 10: 이온화 방사선 방출 진단기기 (X‑ray 발생장치 → Class IIb)”【2】 |
| **Applicable rule** – Rule 10 (active device that emits ionising radiation for diagnosis). |  | Annex VIII, Rule 10 – “Active devices for diagnosis and monitoring” (energy emitted) |
| **Resulting class** – IIb. |  | — |

### 2. Conformity‑Assessment Route  
| Class | MDR Article & Paragraph | Required route(s) (Annex) | NB involvement |
|-------|------------------------|---------------------------|----------------|
| IIb   | Art. 52(4)               | **Annex IX** (full technical‑documentation assessment of the device) *or* **Annex X** (type‑examination) **plus Annex XI** (production conformity verification). | NB required – full audit of technical documentation and/or type‑exam, plus production verification. |

> **Chosen route for this draft:** Annex IX (full technical‑documentation assessment) + Annex XI (production conformity verification), because the device is a Class IIb active system and an NB will already be engaged for design‑dossier review.

### 3. Documentation & Evidence Required  

| Deliverable | Core contents | Regulatory citation |
|-------------|---------------|---------------------|
| **Technical Documentation** | Device description, intended use, labeling, design dossiers, manufacturing information, risk management file, verification/validation data, software documentation (if applicable). | Annex II (Technical Documentation)【1】 |
| **EU Declaration of Conformity** | Signed declaration referencing the device, applicable GSPR and standards. | Annex IV |
| **Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data from comparable devices, benefit–risk analysis. Must be kept current (Art. 61) and follow Annex XIV Part A. | Annex XIV Part A; Art. 61 |
| **Post‑Market Surveillance (PMS) System** | PMS plan (Art. 84), PMS procedures (Art. 83). Include reporting of serious incidents, trend analysis. | Art. 83 & 84 |
| **Periodic Safety Update Report (PSUR)** | For Class IIb: at least annually. Must contain benefit‑risk conclusions, PMCF results, sales volume and user population data. | Art. 86(1)–(2) |
| **PMCF Plan / Evaluation Report** (if applicable) | If the device’s clinical evidence is not fully covered by existing literature or registries. Annex XIV Part B. | Annex XIV Part B |
| **Risk Management File** | ISO 14971‑based risk analysis, evaluation of residual risks, risk control measures, verification of controls. | Annex I GSPR §18 (active devices) & ISO 14971 |
| **GSPR Compliance Checklist** | Demonstration of conformity with all 23 GSPR (Annex I). Particular focus on: <br>• §16 – protection against ionising radiation<br>• §18 – active device requirements<br>• §22 – lay‑person use (if applicable) | Annex I; “GSPR 체크리스트 기반 적합성 평가 필수”【2】 |
| **Standards & Harmonised References** (where applicable) | • IEC 60601‑2‑28 – X‑ray tube assemblies <br>• IEC 60601‑2‑54 – X‑ray equipment for radiography/radioscopy <br>• IEC 62304 – software lifecycle (if SaMD component) <br>• IEC 62366‑1 – usability engineering | No specific identifiers in source – verify separately |

### 4. Identified Missing Information  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Exact Intended Use / Indications** | Determines clinical claim, risk classification nuances, and required clinical data. | Obtain a finalized IFU/Indications statement from the manufacturer. |
| **Software Scope (if any)** | Rule 11 may apply for SaMD components; classification could increase to IIb or III depending on decision impact. | Define software functionality, intended user, and risk class per Rule 11. Provide IEC 62304‑compliant dossier if applicable. |
| **Clinical Data Strategy** | Need either sufficient literature/clinical investigation data or a PMCF plan to satisfy Annex XIV Part A. | Conduct a gap analysis of existing clinical evidence; develop PMCF plan where gaps remain. |
| **Labeling & IFU Content** (Annex I §23) | Must include radiation warnings, user instructions, contraindications, and compliance marks. | Draft labeling per GSPR §23 and verify with NB. |
| **Manufacturing Process Validation** | Required for Annex IX assessment; ensures consistent performance of X‑ray tube assembly. | Provide process validation protocols & reports (e.g., welding, vacuum integrity). |
| **PMS Plan Details** (Art. 84) | Must outline data collection after market launch, including incident reporting and trend analysis. | Draft PMS plan with defined KPIs, monitoring methods, and responsibilities. |
| **Post‑Market Clinical Follow‑up (PMCF) Scope** | Required for Class IIb; must be integrated into PSUR. | Outline PMCF objectives, methodology, timelines, and reporting structure. |

### 5. Risk Controls & Mitigations  

| Hazard | Control measure (per GSPR) | Reference |
|--------|----------------------------|-----------|
| **Radiation exposure to patient/operator** | Design shielding, interlocks, dose‑monitoring, compliance with IEC 60601‑2‑28/54; periodic calibration. | Annex I §16.4 (radiation protection). |
| **Electrical safety of high‑voltage components** | Apply IEC 60601‑1 requirements, isolation testing, leakage current limits. | Annex I §18 (active devices) & IEC 60601 series. |
| **Software malfunction (if SaMD)** | Implement IEC 62304 lifecycle, verification/validation, usability engineering per IEC 62366‑1. | Annex I §17 (electronic programmable systems). |
| **Mechanical failure of tube housing** | Conduct mechanical stress analysis, verify endurance under repeated use cycles. | Annex I §20 (mechanical risks). |
| **Incorrect usage by lay persons (if intended)** | Provide clear labeling, training materials; implement user‑interface design to prevent misuse. | Annex I §22 (lay‑person devices). |

### 6. Human‑Escalation Triggers  

| Trigger condition | Reason for escalation | Escalation destination |
|-------------------|-----------------------|------------------------|
| **Unresolved classification ambiguity** (e.g., software component could shift device to Rule 11‑IIb/III) | May affect conformity route and required NB involvement. | Senior Regulatory Lead → Decision on final class & route. |
| **Insufficient clinical evidence** after literature gap analysis | Non‑compliance with Annex XIV Part A; risk of NB query or market denial. | Clinical Evidence Team → Initiate PMCF study design or collect additional data. |
| **Missing or incomplete PMS plan** (no defined KPIs, reporting cadence) | Violates Art. 84; PSUR cannot be compiled. | Post‑Market Surveillance Manager → Draft/complete PMS plan before NB audit. |
| **Labeling draft fails GSPR §23 checklist** | Could lead to non‑conformity findings on labeling during audit. | Regulatory & Marketing Communications → Revise IFU/labels. |
| **Risk Management file lacking verification of residual risks** | Inadequate justification for risk acceptability; NB may request additional controls. | Risk Management Lead → Perform missing verification testing. |
| **NB audit schedule approaching with outstanding documentation gaps** | Timeline risk for market entry. | Project Manager → Re‑prioritise resources, inform senior management. |

---  

### 7. Peer‑Review Prompt  

*Please review the above draft and challenge any of the following:*  

1. **Assumptions about classification** – Is Rule 10 unequivocally applicable given the device’s intended use, or might additional functionalities invoke Rule 11?  
2. **Coverage of source material** – Does the excerpt provide sufficient basis for all cited requirements, or are there gaps that need supplemental references (e.g., specific Annex I §§)?  
3. **Jurisdiction‑specific considerations** – Are any EU‑wide obligations missing (e.g., EUDAMED registration under Art. 33‑39) that should be highlighted at this stage?  

Your feedback will help ensure completeness before the dossier is presented to the Notified Body.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> ① '선택 루트: Annex IX + Annex XI' — 존재하지 않는 조합(Art 52(4): Annex IX 단독 또는 Annex X+XI; 10-14 eu-002 이후 재발, #134). ② 'EUDAMED Art 33-39' — UDI/등록은 Art 27·28·29-31, EUDAMED 33-34(35-39는 인증기관 조문). GSPR §16.4/§17/§18·PSUR 연1회는 정확.

**Source Excerpts**

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261015-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "11a3549b26bf47b3", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `11a3549b26bf47b3`
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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Roadmap**

| Item | Description / Requirement | Regulatory basis (citation) |
|------|----------------------------|------------------------------|
| 1. Device description | *[Insert brief generic description of the medical device, e.g., “electronic blood‑pressure monitor with Bluetooth data transmission”]* | — |
| 2. Intended purpose & target population | *[Specify clinical indication, user group (health‑care professional or lay person), and environment of use]* | — |
| 3. Classification approach | • Apply the **self‑classification** principle set out in **Article 51 MDR** together with the sequential rule system of **Annex VIII**. <br>• The highest‑ranking rule that matches the device’s intended purpose determines the class.<br>• If uncertainty remains, consult the national Competent Authority (CA) or the MDCG *Manual on Borderline and Classification* (latest 2023‑09 v2.1.1). | Article 51; Annex VIII (22 rules); MDCG Manual (2023‑09) |
| 4. Pre‑liminary class determination (example) | • **Rule 9** – active therapeutic device → Class IIa (or IIb if hazardous energy is delivered). <br>• **Rule 10** – active diagnostic/monitoring → Class IIa (or IIb for vital physiological parameters). <br>*(Actual rule to be selected after the intended‑use description is finalised.)* | Annex VIII Rule 9 / Rule 10 |
| 5. Conformity‑assessment route (per Art. 52) | • **Class I** – self‑declaration, no NB involvement (Art. 52(7)). <br>• **Class Is/Im/Ir** – limited NB review of the sterile/measuring aspect (Art. 52(7), Annex IX Chap. I & III or Annex XI Part A). <br>• **Class IIa** – full NB assessment of technical documentation (Annex IX Chapters I‑III + §4) *or* alternative route via Annex II/III plus Annex XI §10/§18. <br>• **Class IIb** – NB assessment of one device per generic group (Annex IX §§1‑4) *or* type‑examination (Annex X) + production verification (Annex XI). <br>• **Class III** – full NB technical‑documentation assessment (Annex IX) *or* Annex X + Annex XI. | Art. 52(3–7); Annex IX; Annex X; Annex XI |
| 6. Technical documentation (TD) | • Core TD per **Annex II** (design dossier, risk‑management file, labeling, etc.). <br>• PMS‑related TD in **Annex III**. | Annex II; Annex III |
| 7. Clinical evidence & CER | • Prepare a **Clinical Evaluation Report (CER)** according to **Annex XIV Part A**, kept up‑to‑date under **Article 61 MDR**. <br>• If ongoing data collection is required, develop a **Post‑Market Clinical Follow‑up (PMCF) plan** and corresponding evaluation report (Annex XIV Part B). | Annex XIV Part A; Article 61; Annex XIV Part B |
| 8. Post‑market surveillance (PMS) system | • Establish a PMS system per **Article 83 MDR** and a PMS plan (**Art. 84**). <br>• For Class I devices, submit an annual PMS report (**Art. 85**); for Classes IIa–III, produce a Periodic Safety Update Report (PSUR) at least every two years (Class IIa) or annually (Classes IIb/III) per **Article 86**. | Art. 83; Art. 84; Art. 85; Art. 86 |
| 9. Vigilance & incident reporting | • Report serious adverse events and field‑safety corrective actions in line with **MDR Article 87** (European vigilance). <br>• Align with national obligations such as “의료기기법 §31” for Korea (mentioned in source) where applicable for imported devices. | Art. 87; Korean 의료기기법 §31 (comparative) |
| 10. Unique Device Identification (UDI) | • Register the device’s UDI in **EUDAMED** (UDI/DEV module). <br>• Ensure interoperability with national portals (e.g., UDI portal, GUDID) for market entry outside the EU. | EUDAMED regulation (no specific article cited in source) |
| 11. Authorized Representative (AR) | • Appoint an EU‑based AR and enter its details in **Annex IV** (Declaration of Conformity). <br>• For non‑EU manufacturers, also consider a local importer/agent per national law. | Art. 11; Annex IV |
| 12. Fees & contractual aspects | • Budget for NB contract fees (€10 k–€100 k) and, if applicable, US FDA MDUFA IV fees (FY2026 range $27,720 – $440,867). | Source excerpt – fee ranges listed |
| 13. Missing information (to be supplied by the manufacturer) | 1. **Exact intended use & clinical indications** – needed to select the correct Annex VIII rule.<br>2. **Device architecture & principal modes of action** – required for risk‑management and GSPR mapping (§16‑22).<br>3. **Proposed labeling (including IFU)** – to verify compliance with §23 of Annex I.\<br>4. **Clinical data sources** (premarket studies, literature) – for the CER.<br>5. **Risk management file (ISO 14971)** – risk controls and residual risk analysis.<br>6. **Software classification (if applicable)** – to determine whether Rule 11 applies.<br>7. **Manufacturing processes & quality‑system evidence** – needed for NB audit (e.g., ISO 13485). | — |
| 14. Key risk‑control expectations (GSPR) | • **§16** – Radiation protection (if device emits ionising radiation).<br>• **§17** – Software safety and cybersecurity (if software is a medical device).<br>• **§18** – Active devices & associated accessories.<br>• **§20** – Mechanical/thermal hazards.<br>• **§22** – Usability for lay‑person use. | Annex I §§16, 17, 18, 20, 22 |
| 15. Human‑escalation triggers (when to involve senior staff / CA) | • **Unresolved classification** after applying all Annex VIII rules → raise to Competent Authority for clarification.<br>• **No suitable NB identified** for Class IIa/IIb/III → senior management must select and contract an appropriate NB before proceeding.<br>• **Insufficient clinical evidence** (e.g., no comparable predicate, gaps in literature) → stop the CE‑marking timeline and engage a clinical expert panel.<br>• **Failure to meet PMS reporting cadence** (missed PSUR or PMS report) → trigger internal compliance audit and possible CA notification.<br>• **Adverse event severity** exceeding stipulated thresholds per Art. 87 → immediate vigilance report and possible field‑safety corrective action. | Article 51 & Annex VIII; Art. 52; Art. 61/87; Art. 86 (PSUR cadence) |

---

### Peer‑Review Prompt
> **Colleague, please review:**  
> 1. The adequacy of the classification reasoning given only a placeholder intended use – are any high‑risk rules likely to apply that we have not considered?  
> 2. Whether all MDR articles and annexes referenced (e.g., Art. 61 for CER, Art. 87 for vigilance) fully cover the obligations for this device type, or if additional provisions (such as Art. 70 on post‑market clinical follow‑up) should be added.  
> 3. Potential gaps concerning national transposition (e.g., Korean “의료기기법 §31”) that could affect imports and whether we need a separate regulatory pathway for those markets.

*Please challenge the assumptions, verify source coverage, and flag any jurisdiction‑specific omissions.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 참고: Art 85 Class I PMS 보고서의 주기는 '필요 시 갱신' — '연1회' 표현은 완화 필요(식별자 자체는 정확).

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261015-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "4c6a2fadd4ac031f", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md", "source_hash": "9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `4c6a2fadd4ac031f`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_DoC_%EC%96%91%EC%8B%9D_%EC%9E%91%EC%84%B1%EC%A7%80%EC%B9%A8.md)
- Source hash: `9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_DoC_양식_작성지침.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` --- ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ─────────────────────────...
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

> **Regulatory Draft – MDR 2017/745 Classification & Conformity‑Assessment Planning**

---

### 1. Device Synopsis (as currently documented)

| Item | Present in source | Comment / Gap |
|------|-------------------|---------------|
| Manufacturer name, address, SRN, authorised representative | Yes – template fields provided (Chunk 2) | Values still to be completed |
| Product name, trade name, model/Catalogue number | Yes – placeholder fields (Chunk 2) | Must be populated with exact wording |
| Intended use / indication | **Missing** – only “Intended use : […]” placeholder | Critical for rule selection (Annex VIII) |
| Photographs / drawings | Placeholder only (Chunk 2) | Needed for technical documentation (Annex II) |
| Signature block (date, function, name) | Yes – signature template present (Chunk 1) | To be signed by authorised person once dossier is complete |

> **Bottom line:** The source provides a *blank* EU Declaration of Conformity (DoC) template but no product‑specific data. Until the intended use and functional description are supplied, classification cannot be fixed.

---

### 2. Classification Determination – What Must Be Obtained

1. **Collect functional description & intended medical purpose**  
   → Map to the relevant rule(s) in Annex VIII (e.g., Rule 9, 10, 11, 17 or any of Rules 1‑22 for non‑active devices).  

2. **Apply the rule hierarchy** (most restrictive rule governs).  

3. **Resulting device class** will dictate the conformity‑assessment route per Art. 52:

| Class | Reference (Art. 52) | Primary Conformity‑Assessment Route |
|-------|---------------------|--------------------------------------|
| I (non‑sterile, non‑measuring, non‑reusable‑surgical) | Art. 52(7) | Self‑declaration – technical file (Annex II & III) + EU DoC (Annex IV). No NB involvement. |
| Is / Im / Ir | Art. 52(7) | Annex IX Chapters I & III *or* Annex XI Part A – limited NB review for sterile/measure/reusable aspect. |
| IIa | Art. 52(6) | Annex IX (full technical‑documentation assessment of one representative device) **or** Annex II & III + Annex XI §10/§18. NB involvement required. |
| IIb | Art. 52(4) | Annex IX (assessment of each generic group) **or** Annex X (type‑examination) + Annex XI. NB involvement required. |
| III | Art. 52(3) | Annex IX (full assessment) **or** Annex X + Annex XI. NB involvement required. |

*Citation*: MDR 2017/745, Art. 52; classification rules in Annex VIII.

> **Action:** Once the intended use is defined, select the applicable rule(s) and determine the class accordingly.

---

### 4. Conformity‑Assessment Route – Decision Tree (once class known)

| Class | Mandatory NB Modules | Key Documents to Submit |
|-------|----------------------|--------------------------|
| I (non‑sterile) | None (self‑declaration) | Technical documentation (Annex II), PMS plan (Art. 84), EU DoC (Annex IV). |
| Is / Im / Ir | Limited Annex IX/XI review (sterility, measuring function) | Same as Class I plus NB‑review of sterile/measuring aspects. |
| IIa | Full Annex IX technical‑file assessment *or* Annex II + III + Annex XI §10/§18 | Technical documentation (Annex II), PMS system (Art. 83), Clinical Evaluation Report (CER, Annex XIV Part A), PMCF plan (Annex XIV Part B). |
| IIb | Full Annex IX assessment *or* Annex X + Annex XI | All items for Class IIa **plus** a PSUR (Art. 86) and, if using Annex X, type‑examination certificate. |
| III | Annex IX (full) *or* Annex X + Annex XI | Same as IIb; PSUR required annually (Art. 86). |

> **Citation:** MDR Art. 52; Conformity‑assessment routes defined in Annex IX, X and XI.

---

### 5. Evidence Required for the Technical Documentation (Annex II)

| Section (Annex II) | Required Content | Current Status | Gap |
|--------------------|------------------|----------------|-----|
| Device description & specification | Detailed description, intended purpose, indications, mode of action | Placeholder only | **Missing** – needs full narrative and functional diagram. |
| UDI‑DI (basic UDI) | Basic UDI‑DI per Annex VI Part C | Field present but empty | **Missing** value. |
| Risk Management File | ISO 14971 compliant risk analysis, updated with benefit‑risk conclusions | No evidence provided | **Missing** – must be compiled. |
| Clinical Evaluation (Annex XIV Part A) | CER covering state of the art, clinical data, literature review, conclusion on safety & performance | Not present | **Missing** – must be produced. |
| PMCF Plan / Report (Annex XIV Part B) | Planned post‑market clinical follow‑up activities and subsequent report | Not present | **Missing** for Class IIa/IIb/III devices. |
| PMS System (Art. 83) & PMS Plan (Art. 84) | Procedures, responsibilities, data collection methods, periodic safety update reports (PSUR or PMS report according to class) | No evidence | **Missing** – to be established. |
| Labelling & IFU (Annex I §23) | Labels, instructions for use, symbols, language requirements | Placeholder only | **Missing** – must be drafted and verified. |
| Manufacturing information (Annex II §7‑9) | Process description, quality management system (ISO 13485), facilities, sterilisation validation if applicable | Not supplied | **Missing**. |

> **Citation:** MDR Annex II (Technical Documentation); risk management per ISO 14971; clinical evaluation per Annex XIV Part A; PMCF per Annex XIV Part B; PMS system Art. 83‑86.

---

### 6. Risk Controls – Preliminary Guidance

| Hazard Category | Relevant GSPR (§) | Typical control measures (to be documented) |
|-----------------|-------------------|---------------------------------------------|
| Radiation exposure (if device emits ionising radiation) | §16.4 (Protection against ionising radiation) | Shielding, dose monitoring, compliance with IEC 60601‑2‑28/‑54 etc. |
| Software decision support | §17 (Electronic programmable systems) & §18 (Active devices) | IEC 62304 lifecycle, verification/validation of algorithms, cybersecurity measures. |
| Mechanical / thermal risks | §§20‑22 | Design safeguards, protective labeling for lay users, ergonomic testing (IEC 62366‑1). |
| Sterility (if applicable) | Relevant to Is/Im/Ir classification – additional NB review required | Validation of sterilisation cycle, aseptic handling procedures. |

> **Citation:** MDR Annex I §§16‑23; IEC standards cited where appropriate (e.g., IEC 60601‑2‑54 for X‑ray equipment).

---

### 7. Missing Information – Immediate Next Steps

| Required Item | Reason | Source of Gap |
|---------------|--------|--------------|
| **Exact intended use / indication** | Determines classification rule (Annex VIII) and clinical evidence scope. | Absent from template (Chunk 2). |
| **Functional description & mode of action** | Needed for risk analysis, GSPR mapping, and classification. | Not provided. |
| **Risk Management File (ISO 14971)** | Mandatory for all classes; underpins CER. | No file referenced. |
| **Clinical data / literature review** | Required for CER (Annex XIV Part A). | No data in source. |
| **PMCF plan & report (if Class IIa‑III)** | Needed to satisfy ongoing safety evaluation. | Not present. |
| **PMS system description / PSUR schedule** | Obligations under Art. 83‑86. | Missing. |
| **UDI/Basic UDI‑DI number** | Required on labeling and in EUDAMED (Annex VI). | Placeholder only. |
| **Full labeling & IFU** | Must meet Annex I §23. | Not supplied. |

*All gaps must be closed before a Conformity Assessment can be initiated.*

---

### 8. Human‑Escalation Triggers

| Trigger Condition | Action Required | Responsible Person |
|--------------------|-----------------|---------------------|
| **No intended‑use statement** after first data‑gathering session (48 h) | Halt all downstream activities; request clarification from product development lead. | RA Lead / Project Manager. |
| **Classification cannot be assigned** (insufficient functional info) after 5 business days of investigation | Escalate to senior regulatory manager for decision on additional evidence or redesign. | RA Team Lead. |
| **Risk Management File not completed** within the timeline set for technical‑file assembly (2 weeks) | Notify quality management; consider postponing NB submission. | QA Director. |
| **Clinical Evaluation Report draft >30 days overdue** after data collection closure | Escalate to Clinical Affairs Head; evaluate need for external consultancy. | RA Lead. |
| **PMS system not defined** before first batch release | Stop market launch; involve senior compliance officer. | Manufacturing/Quality Manager. |

---

### 9. Summary Judgment (to be reviewed by the human)

*Given the current state of documentation (only a skeletal EU DoC template), the device’s MDR classification cannot be fixed and therefore no specific conformity‑assessment route can yet be selected. The immediate regulatory priority is to obtain a precise intended‑use statement and functional description, after which the applicable rule(s) from Annex VIII will determine the class per Art. 52. Once the class is known, the corresponding NB module (Annex IX/ X / XI) and the full set of technical‑documentation elements (risk management, CER, PMCF, PMS, labeling, UDI) must be prepared in line with the references listed above.*

---

### 10. Peer Review Prompt

> **Colleague, could you verify:**  
> 1. Whether any additional classification nuances (e.g., combined active/diagnostic functions) might affect rule selection once the intended use is known?  
> 2. If there are jurisdiction‑specific supplements in our market (e.g., national post‑market reporting requirements) that should be captured alongside Art. 83‑86?  
> 3. Whether any of the missing items listed above have already been generated elsewhere in the project files but were not reflected in the provided excerpts?

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 'Annex II §7-9' 부존재 — Annex II는 1~6절뿐(설계·제조=§3). '§§20-22' 묶음도 부정확(§20=기계·열, §22=일반인 사용). 빈 DoC 템플릿에 '분류 확정 불가'로 보수 처리한 점은 모범적.

**Source Excerpts**

1. Chunk `1085205256397640486`

> 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` ---

2. Chunk `1141859994065237405`

> ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ───────────────────────────────────────────── 1. MANUFACTURER Company name : [회사명] SRN : [EUDAMED SRN — 미취득 시 공백] Address : [등록 사업장 주소] Authorised Representative: [EU 대리인명 및 주소 — 역외 제조사 해당 시] 2. SOLE RESPONSIBILITY STATEMENT This EU Declaration of Conformity is issued under the sole responsibility of the manufacturer named above. 3. BASIC UDI-DI [Basic UDI-DI — Annex VI Part C 기준] 4. PRODUCT IDENTIFICATION Product name : [제품명] Trade name : [상품명] Model / Cat.# : [모델 번호 / 카탈로그 번호] Intended use : [의도된 사용 목적 — 간략 기재] Photograph : [첨부...

### kb-eval-20261015-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d5a57f771d436ef2", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d5a57f771d436ef2`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수). ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료
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

> **Regulatory Draft – X‑ray Medical Device (Ionising Radiation Equipment)**  

---

### 1. Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory Basis |
|------|---------------|------------------|
| **Device class** | **Class IIb** – ionising radiation equipment for diagnostic use | MDR 2017/745, Annex VIII Rule 10 (active devices emitting ionising radiation) → Class IIb. The source explicitly states “X‑ray is Class IIb or above”. |
| **Conformity‑assessment route** | **Annex IX full technical‑documentation assessment + Annex XI production‑conformity verification** (or Annex X type‑examination as alternative) | Art. 52(4) MDR – mandatory NB involvement for Class IIb devices; route can be performed via Annex IX (full TB assessment) **or** Annex X (type‑examination) together with Annex XI. |
| **Notified Body requirement** | Yes – an NB must be designated in the NANDO database (MDR code MDxxxx). | Source: “NB 인증 필수…NANDO Database에서 MDR 범위(코드 MDxxxx) 확인.” |

---

### 2. Required Technical & Clinical Evidence  

| Evidence | Content Summary | Regulatory Reference |
|----------|----------------|----------------------|
| **Technical Documentation (TD)** | Device description, intended use, labeling, design dossier, manufacturing information, verification & validation data, IEC 60601‑2‑28 compliance (X‑ray tube assemblies). | Annex II MDR; risk management per ISO 14971 (Annex I §17/§18). |
| **Risk Management File** | Hazard identification, risk analysis, evaluation of radiation exposure (§16 GSPR), risk control measures, residual risk & benefit‑risk determination. | Annex I §§16–18; ISO 14971. |
| **Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data (bench, animal, pre‑market clinical investigations) demonstrating safety & performance for the intended diagnostic indication. | Annex XIV Part A; kept current under Art. 61 MDR. |
| **Post‑Market Surveillance (PMS) System** | Integrated PMS plan (Art. 84), periodic safety update report (PSUR) (Art. 86) – at least annually for Class IIb. | Art. 83–86 MDR. |
| **PMCF Plan & Report** | Planned post‑market clinical follow‑up activities, methodology, data collection schedule; final evaluation report. | Annex XIV Part B. |
| **Usability Engineering File** (if software/UI) | Human factors analysis, validation of user interface per IEC 62366‑1. | Annex I §17 (electronic programmable systems). |
| **Labeling & IFU** | Full labeling in accordance with §23 Annex I; includes radiation safety information, warnings, contraindications, UDI. | Annex I §23. |
| **Declaration of Conformity** | Signed EU Declaration referencing all applicable MDR annexes and standards. | Annex IV. |
| **EUDAMED Registration** | Unique device identifier (UDI‑DI), manufacturer & NB details, classification, intended purpose entered in EUDAMED. | Art. 33–39 MDR. |

---

### 3. Gaps / Missing Information (to be supplied before NB submission)

1. **Exact intended use statement** – clinical indication(s), patient population, mode of operation.  
2. **MDR classification rule justification** – a written rationale linking the device to Annex VIII Rule 10.  
3. **Device family grouping** – whether this is a single‑type device or part of a generic group (relevant for Annex IX assessment).  
4. **Clinical data package** – results of any pre‑market clinical investigations, equivalence justification if relying on predicate devices.  
5. **Performance testing reports** – radiation output stability, beam quality, dose measurements, safety alarms (IEC 60601‑2‑28).  
6. **Software documentation** (if applicable) – software development lifecycle file per IEC 62304.  
7. **Usability test outcomes** – especially for operators with limited training.  
8. **Labeling draft** – full “Instructions for Use” in all required EU languages, including radiation safety warnings.  
9. **PMS‑Plan & PMCF‑Plan details** – schedule, responsibilities, data capture methods.  
10. **QMS audit report & NB contract** – evidence of a compliant ISO 13485‑based QMS and signed assessment contract (source lists “심사 계약서·견적서”).  

---

### 4. Principal Risk Controls (to be reflected in the risk management file)

| Hazard | Control Measure(s) |
|--------|-------------------|
| **Excessive radiation dose to patient** | Design of shielding, interlocks, automatic exposure control; compliance with §16 GSPR and IEC 60601‑2‑28. |
| **Electrical safety / leakage currents** | Compliance with IEC 60601‑1 general requirements; protective earth, double‑insulation. |
| **Mechanical failure of X‑ray tube** | Robust mechanical design, routine preventive maintenance schedule, built‑in fault detection. |
| **Software misuse (if software‐driven) causing incorrect exposure settings** | Software validation per IEC 62304, user authentication, audit trail, fail‑safe defaults. |
| **Operator error (incorrect positioning, selection of parameters)** | Comprehensive IFU with pictograms, training program, ergonomic UI design (IEC 62366‑1). |
| **Radiation leakage to environment / staff** | Physical shielding of device housing, warning signs, safety interlocks, periodic radiation surveys. |

---

### 5. Citations  

*Framework references (no verification caveat required):*  
- MDR Annex VIII Rule 10 – classification of active ionising‑radiation devices (Class IIb).  
- Art. 52(4) MDR – conformity‑assessment routes for Class IIb.  
- Annex IX, Annex X, Annex XI – possible assessment pathways.  
- Annex II – Technical Documentation requirements.  
- Annex IV – EU Declaration of Conformity.  
- Annex I §§16–18 – General Safety and Performance Requirements (radiation protection, active devices).  
- Annex XIV Part A/B – Clinical Evaluation Report & PMCF documentation.  
- Art. 83‑86 MDR – PMS system, plan, report, PSUR.  

*Instance identifiers (appear in source):*  
- “Class IIb 이상 → NB 인증 필수” – confirms class level and NB necessity (no further identifier).  
- “NANDO Database…코드 MDxxxx” – indicates the need to locate the MDR code in NANDO (exact code not provided).  

*No specific identifiers for standards, articles or other documents were found in the source excerpts; these will be verified separately.*

---

### 6. Human‑Escalation Triggers  

| Situation | Action Required (Human) |
|-----------|--------------------------|
| **Unresolved classification justification** – missing Rule 10 reference or ambiguous intended use. | Senior RA to review and produce a formal classification report before NB engagement. |
| **Incomplete clinical evidence** – no pre‑market investigation data or insufficient literature coverage. | Clinical affairs team to design/execute a clinical study; pause submission until data are available. |
| **Missing QMS audit & NB contract documents** – “심사 계약서·견적서” not yet secured. | Procurement / legal to finalize NB selection, negotiate contract, obtain signed audit plan. |
| **Absent or outdated PMS‑Plan/PMCF‑Plan** – cannot generate PSUR for Class IIb. | PMS manager must draft and submit plans; postpone conformity‑assessment until approved by NB. |
| **Non‑conformities identified in technical‑documentation assessment report** – flagged “Non-conformity 대응 자료”. | RA to coordinate corrective actions with engineering; only after closure may the submission proceed. |
| **NANDO MDR code not located (MDxxxx unknown)** – inability to confirm NB designation scope. | Regulatory liaison to query NANDO database or contact Competent Authority for clarification. |

---

### 7. Summary Judgment  

- The X‑ray device is a **Class IIb** medical device under MDR, requiring **Notified Body involvement** via Annex IX (or Annex X) plus Annex XI production verification.
- A complete **Technical Documentation**, **Risk Management File**, **Clinical Evaluation Report**, and **PMS/PMCF plans** must be compiled and verified against the listed GSPR clauses before NB assessment.
- Current gaps (intended use, clinical data, performance testing, labeling, QMS audit evidence) must be resolved; any outstanding items trigger the escalation actions above.

---

### 8. Peer‑Review Prompt  

*“Colleague, could you challenge our assumptions regarding the classification (Rule 10 vs possible Rule 9/17 cross‑mapping), verify that the selected conformity route (Annex IX + Annex XI) is optimal for this X‑ray system, and identify any jurisdiction‑specific documentation (e.g., national radiation safety notices) that may have been missed in our evidence list?”*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 표에는 경로 or-구조를 정확히 썼으나 요약문 'Annex IX (or Annex X) plus Annex XI'가 다시 혼합으로 뭉개짐. 'EUDAMED Art 33-39' 재발(#134).

**Source Excerpts**

1. Chunk `978896205875274621`

> ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수).

2. Chunk `296791090431458058`

> ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료

### kb-eval-20261015-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "58a05faa485d7051", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `58a05faa485d7051`
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

> **Regulatory Draft – Classification & Conformity‑Assessment Pathway (EU MDR 2017/745)**  

---

### 1. Scope of the draft  
This document provides a structured outline of the regulatory pathway that must be followed for any medical device intended for the European Union market when its classification and conformity‑assessment route are still to be defined. It lists the evidence required, identifies typical gaps, maps risk‑control measures, and flags points at which human escalation is mandatory.

> **Source basis** – The structure of Annex II (Technical Documentation) and the related MDR articles/annexes are taken from the internal knowledge base excerpts (see sources [1] and [2]). No device‑specific data are supplied in the source material; therefore, the draft remains generic and must be populated with the product‑specific information by the development team.

---

### 2. Classification – initial determination  

| Step | Action | Reference |
|------|--------|-----------|
| 2.1 | Define the **intended purpose** (including target patient population, anatomical site, mode of action) and any **principal intended functions** (diagnostic, therapeutic, monitoring, software‑driven). | MDR Annex VIII – classification rules (Rules 1‑22). |
| 2.2 | Map the identified functions to the **relevant rule(s)** (e.g., Rule 9 for active therapeutic devices, Rule 10 for active diagnostic/monitoring devices, Rule 11 for software, Rule 17 for X‑ray image‑recording devices). | MDR Annex VIII – Rules 9, 10, 11, 17. |
| 2.3 | Assign the **device class** (I, Is/Im/Ir, IIa, IIb, III) according to the rule outcome and any additional criteria (sterility, measuring function, invasive use). | MDR Annex VIII – classification matrix. |
| 2.4 **If** the intended purpose or principal functions are not yet fully described, **human escalation** is required to obtain a definitive device description before proceeding to step 3. | — |

*Note*: No specific rule number can be cited here because the device’s intended use is unknown from the source material.

---

### 3. Conformity‑Assessment Route (per Art. 52)  

| Device Class | Applicable Article(s) | Required NB Involvement & Annex(es) |
|--------------|-----------------------|--------------------------------------|
| **Class I** (non‑sterile, non‑measuring, non‑reusable surgical) | Art. 52(7) – self‑declaration | No Notified Body; technical documentation per Annex II & III + EU Declaration of Conformity (Annex IV). |
| **Is / Im / Ir** | Art. 52(7) – limited NB scope for sterile, measuring or reusable surgical aspect | NB audit limited to relevant aspect under Annex IX Chapters I & III **or** Annex XI Part A. |
| **Class IIa** | Art. 52(6) – full assessment of technical documentation (representative device) | NB assessment per Annex IX Chapters I & III **or** mixed route Annex II & III + Annex XI §10/§18. |
| **Class IIb** | Art. 52(4) – full technical‑documentation assessment or type‑examination | NB assessment via Annex IX (full) **or** Annex X (type‑examination) together with Annex XI. |
| **Class III** | Art. 52(3) – most stringent route | NB assessment per Annex IX (full) **or** Annex X + Annex XI. |

*Human escalation trigger*: If the class determined in Section 2 conflicts with any existing market authorisation or internal risk‑classification, a senior RA must review the classification logic.

---

### 4. Technical Documentation – required contents (Annex II)

| Annex II Chapter | Content Required | MDR clause |
|-------------------|------------------|------------|
| **§1 Device Description** | Comprehensive description of the device, its variants, and intended purpose. | Annex II §1 |
| **§2 Labelling & IFU** | Labels, symbols, instructions for use (IFU) meeting Annex I §23. | Annex II §2 |
| **§3 Design & Manufacturing** | Detailed design specifications, manufacturing processes, validated engineering drawings, and control of critical characteristics. | Annex II §3 |
| **§4 GSPR Checklist** | Evidence that all 23 General Safety & Performance Requirements of Annex I are satisfied (e.g., performance testing, biocompatibility). | Annex II §4 |
| **§5 Risk Management** | Risk Management File complying with ISO 14971, including risk analysis, evaluation and control measures. | Annex II §5 |
| **§6 Verification & Validation** | Verification reports (bench, pre‑clinical) and Validation reports (clinical verification, usability testing). | Annex II §6 |

*Source note*: The mapping of these sections to equivalents in other jurisdictions is shown in source excerpt [1]; no device‑specific identifiers are present – **verify separately** that each subsection has been fully populated for the product under assessment.

---

### 5. Clinical Evidence  

| Requirement | What must be provided | MDR reference |
|-------------|----------------------|---------------|
| **Clinical Evaluation Report (CER)** | Systematic literature review, clinical data from equivalent devices, and a benefit‑risk analysis kept up to date. | Annex XIV Part A; Art. 61 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | Planned activities (prospective studies, registries, complaint analysis) that generate additional clinical data after CE marking. | Annex XIV Part B |
| **PMCF Evaluation Report** | Results of the PMCF activities and their impact on the benefit‑risk determination. | Annex XIV Part B |
| **Periodic Safety Update Report (PSUR)** – for Class IIa/IIb/III | Summarised clinical data, PMS results, and updated benefit‑risk conclusions. Updated at least every 2 years (IIa) or annually (IIb/III). | Art. 86(1‑2) |
| **PMS Report** – for Class I | Summary of post‑market surveillance activities and any serious incidents. | Art. 85 |

*Missing information*: At this stage the draft lacks:

- The actual clinical data set(s) (clinical investigations, equivalence justification, registries).
- A defined PMCF plan with timelines, sample sizes, and endpoints.
- Evidence that the device meets the relevant GSPR through performance testing.

**Human escalation trigger**: Any gap in the CER or absence of a PMCF plan must be escalated to the Clinical Affairs lead before NB submission.

---

### 6. Post‑Market Surveillance (PMS) System  

| Element | Requirement | MDR reference |
|---------|-------------|---------------|
| **PMS System** | Integrated quality‑management system covering complaint handling, trend analysis, and field safety corrective actions. | Art. 83 |
| **PMS Plan** | Documented plan describing the systematic collection, analysis and use of PMS data. | Art. 84 |
| **Periodic Reporting** | PSUR for Classes IIa/IIb/III; PMS report for Class I. | Art. 86 (PSUR), Art. 85 (PMS report) |

*Missing elements*: The current dossier does not contain a written PMS plan nor evidence of an operational PMS system.  

**Human escalation trigger**: Immediate review by the Quality‑Management responsible party to confirm that the PMS system is compliant before any NB audit.

---

### 7. Risk Management & GSPR Alignment  

| Activity | Expected Artefact | MDR / Standard reference |
|----------|-------------------|---------------------------|
| **Risk analysis (hazard identification, estimation)** | Updated risk management file with risk‑acceptability criteria. | ISO 14971; Annex II §5 |
| **Verification of safety requirements** | Test reports demonstrating compliance with relevant GSPR clauses (e.g., §16 radiation protection, §17 electronic programmable systems, §18 active devices). | Annex I §§16‑18 |
| **Usability engineering** (if device intended for lay users) | Usability validation report. | IEC 62366‑1; Annex I §22 |
| **Software lifecycle documentation** (if applicable) | Software development file per IEC 62304. | IEC 62304; Annex I §17 |

*Missing information*: No evidence of usability testing, software safety analyses, or specific GSPR verification for radiation, active, or mechanical risks has been identified in the source material.

**Human escalation trigger**: Any unaddressed GSPR must be escalated to the Risk‑Management team before proceeding with NB review.

---

### 8. Summary of Identified Gaps  

| Gap | Impact on Submission | Required Action |
|-----|----------------------|-----------------|
| **Undefined intended purpose / principal functions** | Prevents classification and selection of appropriate conformity route. | Obtain final product specification from engineering; document in Annex II §1. |
| **Missing clinical data & CER** | Cannot satisfy Annex XIV Part A, leading to NB rejection. | Conduct literature review, collect equivalence data or plan a clinical investigation; draft CER. |
| **Absent PMCF plan** | Required for classes IIa‑III; failure leads to non‑compliance with Art. 61 & 86. | Develop detailed PMCF protocol; assign responsibilities and timelines. |
| **No PMS system / plan** | Violates Art. 83‑84; NB will request evidence of post‑market monitoring. | Implement PMS processes, document in a PMS Plan, integrate into QMS. |
| **Incomplete risk‑management file** | GSPR compliance cannot be demonstrated (Annex I). | Complete ISO 14971‐based risk analysis; perform verification of each relevant GSPR clause. |
| **Labeling & IFU not validated against Annex I §23** | May cause non‑conformity findings during audit. | Produce final labeling in required languages; conduct usability testing where needed. |

---

### 9. Human‑Escalation Triggers  

1. **Classification Uncertainty** – any doubt about the applicable rule or resulting class → senior RA review.
2. **Clinical Evidence Deficiency** – lack of CER, clinical investigation data, or PMCF plan → escalation to Clinical Affairs & Project Management.
3. **PMS System Gaps** – missing PMS plan/system → Quality‑Management lead must be involved before NB audit scheduling.
4. **Risk‑Management Incomplete** – unidentified hazards or unverified GSPR → Risk‑Management team intervention.
5. **Notified Body Feedback** – any NB request for additional documentation during assessment → immediate response coordination by the regulatory lead.

---

### 10. Peer‑Review Prompt  

> **Request to RA peer:** Please evaluate this draft for (i) completeness of the classification logic given the lack of product detail, (ii) adequacy of the listed evidence requirements against the latest MDR guidance, and (iii) any jurisdiction‑specific nuances that may have been overlooked (e.g., language requirements, EUDAMED registration steps). Highlight assumptions that need verification and suggest additional sources or checklists to close identified gaps.  

--- 

*Prepared by Theo – EU MDR Regulatory Affairs Specialist.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

## ra_kr

### kb-eval-20261015-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "d025889ee4010fdb", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `d025889ee4010fdb`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98_%EA%B8%B0%EC%A4%80/%EC%A0%9C%ED%92%88%EB%B3%84_%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98.md)
- Source hash: `a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `제품별_등급분류.md`는 `제품별_등급분류.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정 ###...
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

> **Regulatory Draft – MFDS Classification & Licensing Pathway (Software‑Based Medical Device)**  

---

### 1. Determined Korean Grade & Submission Route  
| Item | Finding | Source |
|------|---------|--------|
| **Korean grade** | **2등급** (may be upgraded to a higher grade depending on the level of auxiliary function) | Excerpt [2] – “국내 (MFDS) — 2등급 …” |
| **Submission track** | **인증** – technical‑document review by an MFDS‑designated 심사기관 (e.g., KTL, KTC). Only products exempted from 인증 would go to 허가; no such exemption is indicated. | MFDS_인허가_상세가이드.md §2 (등급 및 인허가 경로) – framework reference |

**Implication:** The dossier will be prepared for the **인증** pathway, not a 신고 or 허가 submission.

---

### 2. Core Regulatory Requirements & Required Evidence  

| Requirement | Typical Evidence Needed | Notes / Gaps |
|-------------|------------------------|--------------|
| **A‑code (품목코드) assignment** | Confirmation of MFDS product code (A‑code). | Not yet identified – missing in the current To‑Do list. |
| **Classification justification** | • Risk analysis per IEC 62304/82304‑2<br>• Function description showing auxiliary nature<br>• Reference to “디지털의료기기소프트웨어 허가·심사 가이드라인” (framework) | Need documented rationale that the device remains 2등급; verify if any function could elevate it. |
| **Software validation & performance** | • Verification & Validation plans & reports (IEC 62304, IEC 82304‑2)<br>• Usability testing (ISO 9241‑210) | No evidence listed – must be generated. |
| **Clinical evaluation** | • Clinical Evaluation Report (CER) aligned with “디지털의료기기소프트웨어 허가·심사 가이드라인”.<br>• If foreign CER is used, confirm MFDS acceptance via the latest notice (no specific notice number found in source – verify separately). | Foreign FDA predicate and EU MDR rule reference are noted, but Korean clinical data may still be required. |
| **Korean labeling & IFU** | • Labels, packaging artwork, and Instructions for Use fully in Korean (per MFDS labeling ordinance). | Not yet prepared – a separate Korean translation task is needed. |
| **Post‑Market Surveillance (시판후조사) plan** | • PMS plan, periodic safety update report (PSUR), adverse event reporting procedure. | Must be drafted per MFDS “시판후조사 안내”. |
| **KGMP / Manufacturing site compliance** | • If any hardware (e.g., sensor, connector) is part of the system, KGMP certification for the manufacturing facility.<br>• For pure software, a self‑declaration of compliance with MFDS software production standards may suffice. | No statement on hardware presence – missing information. |
| **Cybersecurity & Data Privacy** | • Threat analysis and mitigation plan (ISO 27001/IEC 62443 references).<br>• Personal data handling in line with “개인정보 보호법”. | Not mentioned yet. |
| **Change Management (for AI/SW updates)** | • Change‑control procedures per the 2025‑01‑24 “디지털의료제품법” (framework). | Needs a documented plan. |

---

### 3. Missing Information & Action Items  

1. **Exact intended use / indication** – required for classification and CER.  
2. **Detailed product specifications** (rated voltage, current, application site, software role) – referenced in To‑Do list but not yet defined.  
3. **Predicate device details** – FDA Product Classification Database lookup is noted; need to capture 510(k) number or EU MDR rule outcome.  
4. **Selection of a Notified Body (if any components fall under 3등급·4등급)** – currently undecided.  
5. **Confirmation of whether the software is “독립형”** – determines applicability of the “독립형 SW 사용적합성 가이드라인”.  
6. **Local clinical data requirement** – verify if MFDS requires Korean patient data for this device category (no specific identifier found in source – verify separately).  

---

### 4. Risk Controls (ISO 14971‑based)  

| Hazard Category | Control Measure | Evidence |
|-----------------|----------------|----------|
| Software malfunction leading to incorrect diagnosis/therapy | • Robust verification & validation per IEC 62304<br>• Automated error detection & fail‑safe logging | Validation test reports |
| Cyber‑attack / unauthorized data access | • Network segmentation, encryption (TLS 1.3)<br>• Regular penetration testing | Security assessment report |
| Usability errors (misinterpretation of UI) | • Human factors engineering (ISO 9241‑210)<br>• Simulated use studies with Korean users | Usability study results |
| Regulatory non‑compliance (labeling, language) | • Dual‑language checklist before market launch<br>• Independent linguistic review | Signed labeling compliance checklists |

---

### 5. Citation Summary  

- **Framework references** (no verification caveat required):  
  - “디지털의료기기소프트웨어 허가·심사 가이드라인” – basis for 2등급 classification and software‑specific requirements.  
  - “디지털의료제품법” (effective 2025‑01‑24) – governs AI/SW change management, performance evaluation.  

- **Instance identifiers** (must appear in source; otherwise note verification needed):  
  - No specific MFDS 고시/notice number or article/section cited for the 2등급 rule – *no specific identifier found in source — verify separately*.  
  - No explicit FDA predicate device number or EU MDR Rule 10/11 reference provided in excerpts – *no specific identifier found in source — verify separately*.

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for Escalation |
|---------|-----------------------|
| **Unclear grade (potential upgrade to 3등급/4등급)** | If functional analysis suggests a therapeutic or diagnostic function beyond auxiliary support, the submission must shift from 인증 to 허가. Immediate risk‑assessment meeting required. |
| **A‑code not yet assigned** | MFDS will reject dossier without a valid 품목코드. Escalate to product management for code application. |
| **Missing Korean labeling/IFU** | Non‑Korean materials lead to non‑compliance with MFDS labeling ordinance; stop submission until completed. |
> **Escalation point:** Any of the above items should be raised to the RA Lead and Project Manager within 2 business days for corrective action planning.

---

### 7. Peer Review Prompt  

*“@RA‑Peer, please challenge the assumptions made in this draft:  
- Are we confident that a software‑only device can remain 2등급 given the “auxiliary function” qualifier?  
- Have we sufficiently accounted for MFDS’s current stance on accepting foreign clinical evaluation reports (no notice number cited)?  
- Is any hardware component implied by the “rated voltage/current” specification, thereby triggering KGMP obligations?  
- Are there any additional Korean‑specific statutory references beyond those listed that we should cite?”*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> '2등급 → 인증(지정 심사기관)' 정확(#145 유지). '순수 SW는 자가선언으로 GMP 면제 가능' — 근거 없음: 디지털의료제품법 제8조④(신청 전 품질관리체계 의무)·제24조②(SW 품질관리기준 적합판정, 유효 3년). 사용적합성은 ISO 9241-210보다 IEC 62366-1이 MFDS 기준.

**Source Excerpts**

1. Chunk `1097646391221557778`

> ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정

2. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

### kb-eval-20261015-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "8b7746da74b271ad", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `8b7746da74b271ad`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향...
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

> **Regulatory Draft – P3 Imaging‑Room GUI Software (Digital Medical Device Software)**  

---

### 1. Device Synopsis  
| Item | Description |
|------|-------------|
| **Product name** | P3 촬영실 GUI SW (graphical‑user‑interface software for X‑ray imaging rooms) |
| **Intended use** | Provides image acquisition/display and workflow support for radiographers; no diagnostic interpretation function. |
| **Key functionalities** | 1) Image preview & basic manipulation; 2) System parameter setting; 3) Optional AI‑assistance module (currently not implemented, but may be added in future revisions). |

---

### 2. Korean Regulatory Classification & Submission Route  

| Question | Current Finding | Evidence Needed |
|----------|----------------|-----------------|
| **Is the software a “digital medical device” under the *디지털의료제품법*?** | The source flags the product as “디지털의료기기소프트웨어에 해당하는 경우”. Confirmation required. | Review of the *디지털의료제품법 시행규칙* (2026‑01‑23 amendment) to determine whether a GUI that does not perform autonomous diagnosis is classified as a medical device and, if so, its **grade**. |
| **If it is a medical device, what grade?** | The excerpt mentions “2등급이든 등급 미지정이든”. The exact grade is **uncertain**. | Locate the specific clause that assigns grades to software‑type devices (often §3–§4 matrix). Verify against the latest *디지털의료제품법 시행규칙* and cross‑reference with 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **Submission pathway** | - If grade = 2등급 → **인증** (technical‑documentation review by an MFDS‑designated 심사기관).<br>- If grade = 1등급 → **신고**.<br>- If grade = 3~4등급 → **허가**. | Confirmation of the grade will fix the pathway. Until then, prepare documentation for both 인증 and 신고 as a fallback. |

---

### 3. Required Evidence (based on anticipated 2등급 인증)  

| Category | Required Items | Notes / Gaps |
|----------|----------------|--------------|
| **Quality Management System** | • KGMP certification for software manufacturers.<br>• ISO 13485:2016‑based QMS (or higher maturity can be leveraged under the “우수관리체계 특례”). | The source notes that a mature QMS can be converted into regulatory advantage – ensure current QMS meets at least **ISO 13485** and is mapped to KGMP. |
| **Technical Documentation** | • Device description, specifications, intended use.<br>• Software architecture & hazard analysis (FTA/FMEA).<br>• Cybersecurity risk assessment (per MFDS guidance on digital health). | None identified in source – must be prepared internally. |
| **Clinical Evidence** | • For *pure* GUI functions (no AI), clinical data may be exempt under **제25조 각 호** of the 시행규칙 (see “면제·대체 경로”).<br>• If an AI module is added later, a **비교설계** clinical trial must demonstrate analytical accuracy and effectiveness per the 2025‑10‑31 clinical‑trial guideline revision. | The specific exemption criteria in 제25조 각 호 need to be verified; if not met, a full clinical evaluation will be required. |
| **Labeling & IFU** | • Korean language labeling (product name, intended use, warnings).<br>• User manual with clear instructions for safe operation.<br>• If AI is added later, separate AI‑specific safety information in Korean. | No Korean labeling drafts currently available – to be created. |
| **Post‑Market Surveillance** | • PMS plan aligned with MFDS 시판후조사 requirements (risk‑based monitoring, periodic safety update reports). | Detail level not yet defined. |

---

### 4. Missing / Unverified Information  

1. **Exact grade determination** – confirm via the latest *디지털의료제품법 시행규칙* (2026‑01‑23 amendment).  
2. **Applicability of 면제·대체 경로** – read the full text of **제25조 각 호** to decide whether clinical data can be waived.  
3. **Whether any future AI function will change classification** – assess impact of potential AI add‑on on grade and required clinical trial design (comparative vs. single‑arm).  
4. **Official notice number for the 2026‑01‑23 amendment** – not provided in source; must retrieve the exact 고시/시행규칙 번호 for citation.  

---

### 5. Risk Controls & Mitigations  

| Hazard | Control Measures (Korean‑specific) |
|--------|------------------------------------|
| **User interface misoperation** | • UI/UX ergonomics testing with Korean radiographers.<br>• Clear on‑screen prompts in Korean.<br>• Fail‑safe defaults that prevent unintended exposure. |
| **Cybersecurity breach** | • Encryption of network communication (TLS 1.3).<br>• Regular vulnerability scanning & firmware updates.<br>• Incident response SOP in Korean. |
| **Incorrect AI output (if added)** | • Dual‑check design: AI suggestions must be confirmed by a qualified radiologist.<br>• Performance thresholds defined per 2025‑10‑31 guideline (accuracy, effect size). |
| **Regulatory non‑compliance** | • Mapping of all MFDS labeling/IFU requirements to internal checklist.<br>• Periodic audit against KGMP & ISO 13485. |

---

### 6. Citations  

- **Framework references**  
  - *디지털의료제품법* and its 시행규칙 (2026‑01‑23 amendment).  
  - MFDS “임상시험 가이드라인” revision dated **2025‑10‑31** (AI digital medical devices).  
  - KGMP & ISO 13485:2016 as the accepted QMS baseline.  

- **Instance identifiers present in source**  
  - **제25조 각 호** – cited as the clause that defines exemption/alternative pathways for certain clinical data requirements. *(no further identifier supplied; verify entire article text)*.  

*No specific 고시/notice numbers or case IDs were provided in the excerpts; those must be sourced independently.*

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required |
|--------|-----------------|
| **Grade remains unconfirmed after initial review** | Escalate to senior RA / legal counsel to obtain official classification from MFDS or a certified Korean regulatory consultant. |
| **Exemption under 제25조 각 호 is ambiguous** | Obtain a formal interpretation from MFDS (e.g., via 문의) and document the decision. |
| **Decision to add AI functionality** | Conduct a gap analysis against the 2025‑10‑31 clinical‑trial guideline; prepare a comparative clinical study plan and seek early scientific advice from MFDS. |
| **KGMP certification not yet held** | Initiate KGMP audit process; if timeline exceeds submission deadline, consider alternate pathway (e.g., provisional exemption) after legal review. |
| **Labeling draft fails Korean language check** | Forward to native‑language compliance specialist for review and revision before filing. |

---

### 8. Reusable RA Judgment (to be stored in the knowledge base)

> *For P3 촬영실 GUI SW, classification under the *디지털의료제품법* must be verified; preliminary evidence suggests it could fall into **2등급** (subject to 인증). The device can potentially leverage **제25조 각 호** exemption for clinical data, but this requires a full read‑through of the amended 시행규칙. A mature KGMP/ISO 13485 QMS is a strategic asset under the 우수관리체계 특례 and should be documented accordingly. Any future AI module will shift both classification and evidence requirements, invoking the 2025‑10‑31 clinical‑trial guideline revisions.*

---

### 9. Peer Review Prompt  

> **Colleague, please challenge**:  
> - Are we correctly interpreting the applicability of *제25조 각 호* for a non‑diagnostic GUI?  
> - Have we captured all possible exemption routes (e.g., “기능별 면제” vs. “대체 경로”) that could reduce the evidence burden?  
> - Is there any recent MFDS notice (post‑2026‑01‑23) that reclassifies software‑type devices, which we might have missed in this source set?  

--- 

*End of draft.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1127968925422991528`

> ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향후 AI 모듈 추가 가능성 고려해 비교설계 원칙 사전 학습 권고. - 출처: 정책브리핑 2025-10-31(https://www.korea.kr/briefing/pressReleaseView.do?newsId=156724315) ---

2. Chunk `198902914416608487`

> - 영향 제품: **P3 촬영실 GUI SW**(디지털의료기기소프트웨어에 해당하는 경우). P1 X-ray Detector·P2 Handheld X-ray Source는 의료기기법 체계 적용으로 **직접 영향 없음**(§3·§4 매트릭스 유지). - 나항은 자사에 **유리한 완화**다. GUI SW가 2등급이든 등급 미지정이든 기능별 임상시험 자료의 **면제·대체 경로가 열린다**. 다만 면제·대체의 개별 요건(개정 제25조 각 호)은 조문 전문 확인이 필요하다 — `[검증 필요]`. - 가항은 요건의 삭제가 아니라 **근거 조문의 이동(고시 → 시행규칙)** 이다. 「디지털의료제품법 시행규칙」(2026-01-23 개정)의 해당 조문을 확인해야 실제 의무 범위를 알 수 있다 — `[검증 필요]`. - 다항의 우수관리체계 특례는 **QMS 성숙도를 인허가 편익으로 전환**하는 제도다. KGMP·ISO 13485 기반이 갖춰진 경우 중장기 활용 가치가 있다. **행동 (Action)**

### kb-eval-20261015-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "96668d35c19960fe", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `96668d35c19960fe`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%B8%ED%97%88%EA%B0%80_%EC%83%81%EC%84%B8%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_인허가_상세가이드.md`는 `MFDS_인허가_상세가이드.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수 ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재...
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

> **Regulatory Draft – 촬영실 GUI 소프트웨어 (2등급)**
---

### 1. Device Classification & Submission Route
| Item | Korean Regulatory Requirement | Current Finding |
|------|------------------------------|-----------------|
| **Grade** | Determined as **2등급** by MFDS “의료기기 품목 및 품목별 등급에 관한 규정”. | Confirmed in source excerpt [2]. |
| **Submission Track** | **인증** (technical‑document review by MFDS‑designated 심사기관). Alternative/parallel path may be required under the *Digital Medical Products Act* if the software is considered a “디지털 의료제품” – this must be evaluated. | Certified route indicated in source excerpt [2]; note possible dual‑track. |

> **Citation (framework):** 의료기기법 → 시행령 → 시행규칙; 고시 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」【1】.

---

### 2. Required Evidence Package for 인증 (2등급)

| Evidence | Korean Requirement | International Equivalent | Notes |
|----------|-------------------|---------------------------|-------|
| **Technical Documentation** (설계·개발 파일) | Must comply with MFDS “의료기기 허가·신고·심사 등에 관한 규정”. | ISO 13485‑based DMD. | Include Korean language versions of all documents. |
| **Software Lifecycle Management** | IEC 62304 기반 수명주기 관리 (개발, 검증·확인, 유지보수). | IEC 62304. | Documented in “소프트웨어 생애주기 계획서”. |
| **Risk Management File** | ISO 14971 적용; MFDS risk‑management guidance. | ISO 14971. | Include 위험도 평가, 위험 통제 및 검증 기록. |
| **Usability (Human Factors)** | IEC 62366‑1 사용적합성 시험. | IEC 62366‑1. | Must be performed with Korean end‑users and documented in Korean. |
| **Cybersecurity** | MFDS 사이버보안 가이드라인 (referencing IEC 62443). | IEC 62443 series. | Include 위협 모델링, 보안 설계 및 취약점 관리 기록. |
| **AI Component (if present)** | – Generation‑AI 가이드라인 적용.<br>– 알고리즘 투명성·편향·데이터 품질 검증.<br>– 변경관리계획 활용. | MFDS AI 의료기기 가이드라인; ISO IEC 23894 (AI 위험 관리) as reference. | Evidence must show compliance with the latest MFDS AI guidance. |
| **Labeling & IFU** | All labeling, 사용설명서 and 사용자 매뉴얼 in Korean; must meet 고시 “의료기기 라벨·사용설명서 등에 관한 규정”. | EU MDR Annex I, FDA 510(k) labeling rules. | Include QR‑code for electronic version if desired. |
| **Clinical Evaluation** (optional) | Generally not mandatory for 2등급, but MFDS may request a limited 임상평가 보고서 when safety/성능이 새로운 경우. | ISO 14155 (if required). | Prepare a minimal clinical evaluation plan ready for submission. |
| **KGMP / 제조 시설** | If the software is delivered on medical‑grade hardware, that hardware must be KGMP‑certified; pure “software only” generally exempt from GMP audit but still needs “품질관리 체계”. | ISO 13485. | Verify whether the hosting device falls under 의료기기 GMP 심사·평가. |
| **Change Management Plan** | Required especially when AI updates are anticipated; must reference MFDS 변경관리 규정. | IEC 62304 change‑control appendix. | Include versioning, impact analysis and Korean documentation of each change. |

> **Citation (framework):** IEC 62304, IEC 14971, IEC 62366‑1, IEC 62443 series (as referenced by MFDS). No specific notice numbers appear in the source – verify separately.

---

### 3. Missing Information & Open Questions
| Gap | Why it matters | Action / Escalation |
|-----|----------------|----------------------|
| **Exact intended use statement** (incl. target patient population, clinical setting) | Needed for grade justification and risk analysis. | Request from product team; if ambiguous, elevate to senior RA for classification confirmation. |
| **Confirmation whether the software falls under *Digital Medical Products Act*** | Determines need for additional regulatory track or dual submission. | Conduct a law‑mapping check; if unclear, escalate to legal counsel/RA lead. |
| **Presence & scope of AI functionality** (type of generative AI, training data, update frequency) | Triggers AI‑specific guidelines and extra documentation. | Obtain detailed AI design dossier; if AI is present, flag for senior review. |
| **Korean language labeling draft** (including font size, mandatory symbols) | Mandatory for all 2등급 devices; non‑compliance blocks certification. | Prepare provisional label; submit to QA/Compliance for verification before MFDS submission. |
| **Local clinical data requirement** (whether MFDS will request a clinical evaluation) | May be required if the device introduces new technology or claims. | Prepare a minimal clinical evaluation plan ready for rapid deployment; flag for senior review if risk profile is high. |
| **KGMP status of any bundled hardware** | If hardware is part of the system, KGMP certification may be needed. | Verify with manufacturing partner; if absent, trigger KGMP audit planning. |

---

### 4. Core Risk Controls to Highlight in Submission
1. **Design‑time risk control** – Failure mode analysis (FMEA) linked to IEC 14971.
2. **Software verification & validation** – Unit, integration, system testing per IEC 62304; traceability matrix linking requirements → tests.
3. **Cybersecurity safeguards** – Network isolation, encryption, secure boot, periodic vulnerability scans.
4. **Usability engineering** – Formative and summative usability studies with Korean clinicians; mitigate use‑error risks.
5. **AI governance** – Algorithmic accountability framework (data provenance, bias analysis, performance monitoring); change‑management plan for model updates.
6. **Post‑market surveillance (시판후조사) plan** – Real‑world usage monitoring, adverse event reporting system in Korean, periodic safety update reports.

---

### 5. Human‑Escalation Triggers
| Trigger | Reason | Escalation Path |
|--------|--------|-----------------|
| **Uncertainty about classification or dual regulatory track** (Digital Medical Products Act) | Misclassification leads to rejection or delayed certification. | Raise to RA Team Lead + Legal Counsel for a formal MFDS clarification request. |
| **AI component confirmed** – lacking AI‑specific documentation | MFDS has strict AI guidance; non‑compliance blocks approval. | Immediate escalation to Senior RA & AI Technical Specialist; consider early consult with MFDS. |
| **Korean language labeling draft not finalized** | Labeling errors are a common cause of certification failure. | Escalate to Compliance / QA Manager for urgent review. |
| **KGMP certification gap for bundled hardware** | Manufacturing compliance is mandatory for any device part considered a medical device. | Notify Production/Quality Lead; schedule KGMP audit and report to RA lead. |
| **Request from MFDS for local clinical data** (outside of standard 2등급 expectations) | May require additional resources and timeline extension. | Promptly involve Clinical Affairs and senior RA to develop CE plan. |
| **Significant change in intended use or risk profile during development** | Alters risk assessment and possibly grade. | Escalate to RA Lead for re‑classification and amendment of submission dossier. |

---

### 6. Reusable Judgment (Honcho Conclusion)

*When a Korean software medical device is identified as **2등급**, the default MFDS pathway is **인증** via a designated 심사기관. The evidence package must include IEC 62304‑based lifecycle documentation, ISO 14971 risk management, IEC 62366‑1 usability testing, cybersecurity controls per MFDS/IEC 62443 guidance, and Korean‑language labeling. If the software incorporates generative AI, the MFDS *Generation‑AI* guidelines and a formal change‑management plan become mandatory. Any uncertainty about dual compliance under the Digital Medical Products Act, missing Korean labeling, or lack of KGMP certification for bundled hardware triggers immediate escalation to senior RA leadership.*

---

### 7. Peer Review Prompt
> **To:** RA peer (e.g., Ji‑yeon Lee)  
> **Subject:** Review of 2등급 촬영실 GUI SW 인증 Draft  
> Please challenge the assumptions above:  
> 1. Is the classification as 2등급 definitively supported by the current MFDS 고시, or could any functional claim push it to 3등급?  
> 2. Does the referenced “Digital Medical Products Act” pathway truly apply to this GUI software, and what criteria should we use to decide on dual submission?  
> 3. Are there any additional Korean‑specific evidence items (e.g., 전자기 호환성시험, 의료기기용 소프트웨어 보안 인증) that we have missed?  
> 4. Verify whether any MFDS notice number or article is required for the AI guideline citation; if so, obtain it.  

Your feedback will be incorporated before finalizing the submission dossier.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 'IEC 14971' → ISO 14971(3회 반복 오타). 'MFDS 사이버 가이드라인이 IEC 62443 참조' — 원문 근거는 IEC 81001-5-1. 2등급 인증 경로·고시 명칭은 원문 충실.

**Source Excerpts**

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `39359892234270838`

> ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재검증 — 핵심 규제사실 반영 확인. · 상태: 승인 · 일자: 2026-06-09

### kb-eval-20261015-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "15eb06961eabaa0e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `15eb06961eabaa0e`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EC%82%AC%EC%9D%B4%EB%B2%84%EB%B3%B4%EC%95%88_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_2025_%EB%8C%80%EC%9D%91.md)
- Source hash: `87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_사이버보안_가이드라인_2025_대응.md`는 `MFDS_사이버보안_가이드라인_2025_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 | ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개...
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

> **Regulatory Draft – Cyber‑Security Requirements for Medical Devices (MFDS Guideline 2025‑01)**  

---

### 1. Applicable Korean Grade & Submission Route  
| Korean grade | Typical MFDS track | Comment |
|--------------|-------------------|---------|
| **1등급** | 신고 (notification) | Only if the device is a simple, low‑risk accessory that falls under the “신고” list in 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **2등급** | 인증 (technical‑document review by an MFDS‑designated 심사기관) | Most cyber‑security‑focused devices (e.g., software‑only or hardware with moderate risk) are placed in this grade. The default track is **인증**, not 허가. |
| **3등급·4등급** | 허가 (full MFDS approval) | High‑risk therapeutic, implantable, or life‑supporting devices must obtain 허가. |

> **Judgment:**  The guideline itself does not assign a grade; the applicable grade must be verified against the official “품목별 등급” table. **Action:** Confirm the device’s Korean grade before selecting the submission track.

---

### 2. Core Evidence Required for Submission  

| Evidence | MFDS requirement (framework) | Source citation |
|----------|------------------------------|-----------------|
| **KGMP certificate** for the manufacturing site (if a 3등급·4등급 device). | Compliance with 의료기기법 시행규칙 KGMP provisions. | No specific identifier in source – verify separately. |
| **Korean‑language labeling & IFU** that include a summary of cybersecurity controls and user responsibilities. | Labeling must be in Korean per MFDS labeling regulations. | No specific identifier in source – verify separately. |
| **Technical dossier** containing: <br>• Device description, intended use, risk classification.<br>• Software architecture diagram.<br>• Cybersecurity risk management plan (per IEC 62443/ISO 14971).<br>• Evidence that all 35 RA items are met. | MFDS “의료기기의 사이버보안 허가·심사 가이드라인” requires demonstrable compliance with the listed requirements. | 【1】 |
| **Verification of International Standards alignment** (IMDRF N60/N73, IEC 81001‑5‑1). | The guideline’s “조화 목적” explicitly references these standards. | 【1】 |
| **Foreign clinical or non‑clinical data (if used)** – must be mapped to Korean requirements; acceptance depends on MFDS mutual‑acceptance notices. | Separate MFDS notice governs MAD for GLP safety data and CER for foreign clinical evaluation reports. | No specific identifier in source – verify separately. |
| **Software Bill of Materials (SBOM) & Code Signing certificates**. | Required under the “소프트웨어 무결성” category. | 【2】 |
| **Vulnerability Management Plan** (CVE monitoring, patch schedule). | Required under “취약점 관리”. | 【2】 |

---

### 3. Missing / Unconfirmed Information  

1. **Exact Korean grade of the device** – must be cross‑checked with the official grade table.  
2. **Whether the device is a software‑only product or includes hardware** – influences KGMP applicability and clinical data needs.  
3. **Existence of foreign clinical evidence** – if used, the specific MFDS notice that permits its use must be identified.  
4. **Localization status of user manuals & risk management files** (Korean translation).  
5. **Evidence of prior compliance with earlier (15‑item) cybersecurity guideline** – may reduce duplication but needs explicit statement.

---

### 4. Risk‑Control Measures Required by the Guideline  

| Category (RA‑01 ~ RA‑35) | Mandatory Controls (as per 2025 revision) |
|--------------------------|--------------------------------------------|
| **보안 설계 원칙** | Secure‑by‑design, defense‑in‑depth architecture, least‑privilege access controls. |
| **인증·접근 제어** | User authentication mechanisms, role‑based access control (RBAC), session timeout & management. |
| **암호화** | Encryption of data at rest and in transit; robust key‑management procedures. |
| **소프트웨어 무결성** | Code signing for all binaries, boot integrity verification, maintain an up‑to‑date SBOM. |
| **네트워크 보안** | Minimal open ports, firewall rulesets, TLS 1.2+ for communications. |
| **취약점 관리** | Continuous CVE monitoring, regular security patch cycles, documented CVD policy. |
| **감사·로그** | Secure logging of security events, tamper‑evident log storage, audit‑trail access logs. |
| **업데이트·유지보수** | Authenticated secure update mechanism, remote management protected by cryptographic controls. |

All 35 individual RA items (RA‑01 ~ RA‑35) are enumerated in the official PDF; the summary above reflects the eight thematic groups identified in the source. 

---

### 5. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Suggested action |
|---------|----------------------|------------------|
| **Grade uncertainty** – device not found in the “품목별 등급” table. | Wrong submission track leads to rejection. | Pause dossier preparation; request senior RA or MFDS liaison clarification. |
| **Missing Korean translation** of labeling/IFU. | Non‑compliance with language requirement results in post‑market penalties. | Escalate to translational quality team and legal for verification. |
| **Absence of KGMP certificate (for 3/4등급)**. | Certification is mandatory before 허가 submission. | Notify manufacturing QA; suspend filing until certificate obtained. |
| **Foreign clinical data without identified MFDS acceptance notice**. | Risk of dismissal of the data by reviewers. | Escalate to regulatory strategy lead to locate proper MFDS mutual‑acceptance notice or plan local study. |
| **Inadequate evidence for any of the 35 RA items** (e.g., no SBOM, no patch policy). | Failure to meet guideline will block approval. | Trigger internal audit; assign cybersecurity engineer to produce missing artifact. |
| **Regulatory timeline clash** – guideline effective date (2025‑01‑10) vs planned submission before confirmatory evidence is ready. | Submissions must reference the latest version of the guideline. | Escalate scheduling to project manager to adjust timeline. |

---

### 6. Citations  

* **Guideline overview & legal basis:** “의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서)”, 개정일 2025‑01‑10, 법적 근거 「디지털의료제품법」(2025‑01‑24 시행), 의료기기법 시행규칙【1】.  
* **RA requirement categories (35 items → 8 groups):** Table in Section 3.2 listing the eight categories and example controls【2】.  

> *No specific MFDS notice number or article/section identifier appears in the provided excerpts; any such identifier must be verified separately before inclusion.*

---

### 7. Peer‑Review Prompt  

> **@RA‑Peer** – Please review the assumptions above:  
> 1. Is the classification inference (defaulting to 2등급 → 인증) appropriate for a software‑driven medical device with cybersecurity controls?  
> 2. Does the evidence checklist cover all MFDS expectations for foreign clinical data acceptance under current mutual‑acceptance notices?  
> 3. Are there any jurisdiction‑specific gaps (e.g., post‑market surveillance, cyber‑incident reporting) that have not been captured from the guideline excerpt?  

--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 'KGMP certificate (if a 3등급·4등급 device)' 축소 — 의료기기법 제6조④는 등급 불문 신청 전 제조·품질관리체계를 의무화(2등급 인증에도 적용, 등급 간 차이는 심사기관뿐). '기본 트랙은 인증, 허가 아님' 명시는 정확.

**Source Excerpts**

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---

### kb-eval-20261015-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-15", "decision_ref": "kb-eval-20261015-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "34e8e32617c3969b", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `34e8e32617c3969b`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%ED%91%9C%EC%8B%9C%EA%B8%B0%EC%9E%AC_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_%EB%8C%80%EC%9D%91.md)
- Source hash: `7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_디지털의료기기_표시기재_가이드라인_대응.md`는 `MFDS_디지털의료기기_표시기재_가이드라인_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 9. 의료기기법 일부개정 (법률 제21949호, 공포 2026-09-15) — 온라인 표시·광고 규제 강화 | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 |...
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

> **Regulatory Draft – Digital‑Medical‑Device (Software) Submission**

---

### 1. Classification & Licensing Route  

| Item | Determination |
|------|---------------|
| **Device type** | General‑purpose medical software (“SW 일반”) as listed in the MFDS digital‑medical‑device guidance (source [2]). |
| **Applicable legal basis** | Amendment to the Medical Device Act – *법률 제21949호* (published 2026‑09‑15) that strengthens online labeling/advertising rules (source [1]). |
| **Korean grade** | Must be assigned **1등급, 2등급, 3등급 or 4등급** according to the risk‑based matrix in 「의료기기 품목 및 품목별 등급에 관한 규정」. The exact grade cannot be inferred from the excerpt; a detailed functional claim and intended use analysis is required. |
| **Submission track** | • **1등급 → 신고**  <br>• **2등급 → 인증** (technical‑document review by an MFDS‑designated 심사기관)  <br>• **3/4등급 → 허가** (full MFDS approval). The appropriate track will be selected once the grade is confirmed. |

*Action*: Confirm intended use and risk profile; map to the Korean grading table. Until the grade is known, prepare a provisional “grade‑determination package” for MFDS review.

---

### 2. Required Evidence (per MFDS digital‑medical‑device labeling guideline)

| No. | Requirement (mandatory/ recommended) | Source / Reference |
|-----|---------------------------------------|--------------------|
| **S‑1** | Software version, build number, release date | “디지털의료제품법 시행규칙” (framework reference, source [2]) |
| **S‑2** | Update method & frequency | MFDS SW 가이드라인 (framework) |
| **S‑3** | Minimum / recommended system specifications (OS, CPU, RAM, storage, display resolution, network) | MFDS SW 가이드라인 |
| **S‑4** | List of compatible medical devices + interface details | – (no external citation; must be supplied by applicant) |
| **S‑5** | Data exchange formats (DICOM, HL7, etc.) | – |
| **S‑6** | Cyber‑security settings (encryption policy, network segmentation, access rights) | MFDS 사이버보안 가이드라인 2025.01 |
| **S‑7** | Security‑patch application procedure & responsible party | MFDS 사이버보안 가이드라인 2025.01 |
| **S‑8** | Known residual cyber‑security risks & mitigation plan | MFDS 사이버보안 가이드라인 2025.01 |
| **S‑9** | Data backup & recovery methodology | – |
| **S‑10** | System log management method (recommended) | MFDS 사이버보안 가이드라인 2025.01 |
| **AI/ML …** | (If applicable, additional AI/ML transparency and performance documentation required; not listed in the excerpt but part of the current MFDS guidance.) |

*Additional evidence generally required for all grades*  

1. **Technical file** – design history, software architecture diagram, verification & validation reports.  
2. **Risk management dossier** – ISO 14971‑compliant risk analysis, including cyber‑risk controls (S‑6 to S‑8).  
3. **Clinical evaluation** – local clinical data for 3/4등급 or a foreign CER accepted under the current MFDS notice (specific notice number not provided in source → *verify separately*).  
4. **KGMP compliance** – facility certification required for 3/4등급 devices (manufacturing site must hold KGMP certificate).  

---

### 3. Missing Information (must be obtained before dossier finalisation)

| Gap | Why it matters | Suggested source |
|-----|----------------|-----------------|
| **Intended use / claim** | Drives risk classification and clinical evidence scope. | Product marketing/labeling statements. |
| **Risk grade (1–4등급)** | Determines whether 신고, 인증 or 허가 is needed. | Apply MFDS grading matrix (Regulation § ... – reference in internal KB). |
| **Korean‑language labeling & IFU** | Mandatory for all grades; no exemption noted. | Korean translation of label, user manual, and online display content. |
| **Compatibility device list (S‑4)** | Required mandatory item; currently blank. | Manufacturer’s hardware integration documentation. |
| **Data format specifications (S‑5)** | Must be declared to meet interoperability expectations. | Technical specs of data exchange modules. |
| **Foreign clinical evaluation acceptance notice** | If leveraging FDA 510(k) / CE Mark, need the specific MFDS notice that permits mutual acceptance. | Search MFDS public notices post‑2026; *verify separately* as not in source. |
| **Post‑market surveillance plan** | Required for 3/4등급 and recommended for lower grades. | PMS SOPs, adverse event reporting workflow. |

---

### 4. Risk Controls & Mitigation Strategy  

| Control Area | Description | Reference |
|--------------|-------------|-----------|
| **Software version control** | Maintain a traceable repository linking each release to its validation data (S‑1). | MFDS SW 가이드라인 |
| **Update governance** | Define update frequency, rollout mechanism, and emergency patch process (S‑2, S‑7). | MFDS SW 가이드라인 / 사이버보안 가이드라인 |
| **System requirement verification** | Test software on declared minimum hardware; document performance margins (S‑3). | MFDS SW 가이드라인 |
| **Interface compatibility verification** | Validate data exchange with each listed compatible device (S‑4, S‑5). | Internal test reports |
| **Cybersecurity safeguards** | Implement encryption, network segmentation, role‑based access, and hardened OS configuration (S‑6). | MFDS 사이버보안 가이드라인 2025.01 |
| **Residual risk treatment** | Identify any remaining cyber risks after controls; define monitoring & response procedures (S‑8). | MFDS 사이버보안 가이드라인 2025.01 |
| **Backup & recovery** | Scheduled data backups, offsite storage, and restore testing (S‑9). | Internal SOP |
| **Log management (recommended)** | Centralized log collection, retention ≥ 12 months, audit‑trail analysis (S‑10). | MFDS 사이버보안 가이드라인 2025.01 |
| **Post‑Market Surveillance** | Continuous monitoring of adverse events & security incidents; periodic safety updates to MFMF. | MFDS PMS regulations (framework) |

---

### 5. Citations  

| Item | Citation type | Reference |
|------|--------------|-----------|
| Legal amendment enabling stricter online labeling/advertising | Instance identifier (specific instrument number) | *법률 제21949호*, 공포 2026‑09‑15 (source [1]) |
| Mandatory software information items (S‑1 to S‑9) | Framework reference (regulation/guideline name) | “디지털의료제품법 시행규칙”, “MFDS SW 가이드라인”, “MFDS 사이버보안 가이드라인 2025.01” (source [2]) |
| No specific MFDS notice number for foreign clinical evidence in the provided excerpts | – | *no specific identifier found in source — verify separately* |

---

### 6. Human‑Escalation Triggers  

| Trigger condition | Reason for escalation |
|-------------------|-----------------------|
| **Unresolved grade (1–4등급) after risk analysis** | Determines submission pathway; requires senior RA decision. |
| **Missing Korean label/IFU** | Non‑compliance with mandatory language requirement; must be addressed before filing. |
| **Absence of a verified MFDS notice permitting foreign clinical data use** | Could invalidate reliance on FDA 510(k) / CE reference; legal review needed. |
| **Any mandatory item (S‑1 to S‑9) lacking supporting documentation** | Deficiency will cause rejection at technical review; needs immediate remediation. |
| **KGMP certification pending for a 3/4등급 device** | Manufacturing compliance is a pre‑condition for 허가; escalation to QMS lead required. |
| **Identified residual cyber‑risk without mitigation plan** | Security breach risk → must be resolved before market entry. |
| **Discrepancy between declared system requirements and actual test data** | Potential safety issue → raise to product engineering & QA leadership. |

*When any of the above triggers are flagged, route the dossier to a senior RA manager for review and possible pause of submission until the gap is closed.*

---

### 7. Peer‑Review Prompt  

> **Colleague Review Request:**  
> Please challenge the assumptions made in this draft, specifically:  
> 1. The completeness of the mandatory information list (S‑1 ~ S‑9) for a general‑purpose medical software – are there other items (e.g., AI/ML transparency disclosures) that should be added from the latest MFDS guidance?  
> 2. The adequacy of the evidence plan for leveraging foreign clinical evaluation – does the current public notice landscape (post‑2026) provide any additional pathways we may have missed?  
> 3. Potential gaps in Korean language obligations beyond labeling and IFU, such as online advertising statements under the recent amendment (*법률 제21949호*).  

Your feedback will be incorporated before finalizing the submission package.

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> '로그 12개월' 근거 없는 수치(내부 기준으로 표기할 것). 'MFMF'→MFDS 오타. 법률 제21949호·S-1~S-10·1~4등급 트랙는 원문 완전 충실.

**Source Excerpts**

1. Chunk `1044206327041877533`

> ## 9. 의료기기법 일부개정 (법률 제21949호, 공포 2026-09-15) — 온라인 표시·광고 규제 강화

2. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...
