# KB Eval Checksheet - 2026-07-23 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260723-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "795e93cbbbb0f811", "source": "github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md", "source_hash": "fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `795e93cbbbb0f811`
- Source: `github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week03_FDA_510k_%EC%83%81%EC%84%B8.md)
- Source hash: `fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `Week03_FDA_510k_상세.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과...
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

> **Regulatory Draft – 510(k) Strategy for a New X‑ray Imaging Device**

| Item | Judgment / Requirement | Source / Citation |
|------|------------------------|-------------------|
| **Device classification** | Likely *Class II* radiology/imaging equipment (X‑ray system). The FDA’s imaging panel is **21 CFR Part 892**. Specific sub‑section for X‑ray imaging devices must be confirmed (e.g., §892.1005 or similar). | no specific identifier found in source — verify separately |
| **Submission route** | Traditional 510(k) *substantial equivalence* pathway, provided the five decision points in FDA 2014 Guidance Appendix A are satisfied. | FDA “Decision Point” guidance (2014 Guidance, Appendix A) – reproduced in source excerpt [2] |
| **Required evidence for SE** | 1. **Predicate device**: Identify a legally marketed X‑ray system with an active 510(k) clearance. <br>2. **Intended use statement**: Show identical clinical purpose and patient population as the predicate. <br>3. **Technological characteristics**: Demonstrate parity in hardware (tube voltage, focal spot size, detector type), software algorithms, and performance specifications. <br>4. **Safety & effectiveness comparison**: Provide bench‑test data, radiation safety measurements, image quality metrics (e.g., DICOM DQE, MTF) that meet or exceed the predicate’s performance. <br>5. **Labeling & UDI**: Conform to 21 CFR §801 (labeling) and §830 (UDI). | FDA “Decision Point” guidance – source [2]; 21 CFR Part 807 (510(k)) – framework; 21 CFR Part 801, Part 830 – framework |
| **Missing information** | • Exact device description (model name, hardware architecture). <br>• Intended‑use narrative. <br>• Predicate identification (clearance number, release date). <br>• Detailed comparison matrix (intended use, technological characteristics, safety questions). <br>• Performance test plan & results. <br>• Software/firmware versioning if applicable. | no specific identifier found in source — verify separately |
| **Risk controls / QMS** | • Implement a **Quality Management System** aligned with **21 CFR Part 820** (effective Feb 2026, ISO 13485‑aligned). <br>• Conduct risk analysis per **ISO 14971** and integrate findings into design inputs/outputs. <br>• For software components, prepare a **Predetermined Change Control Plan (PCCP)** if future algorithm updates are anticipated. <br>• Ensure UDI labeling per **21 CFR Part 830**. | 21 CFR Part 820; ISO 14971; Predetermined Change Control Plan (PCCP) – FDA final guidance Dec 2024 |
| **Human‑escalation triggers** | • *No suitable predicate* found → escalation to senior regulatory lead for De Novo or PMA strategy. <br>• *Intended use differs* from any cleared device → same escalation. <br>• *Technological differences* raise new safety/effectiveness questions (e.g., novel detector material, AI‑based image enhancement) → require risk reassessment and possible change of submission pathway. <br>• *Performance data* do not demonstrate ≥ predicate performance → pause submission and seek senior guidance on additional testing or alternative pathway. | Derived from FDA 5‑step SE decision flow (source [2]) |
| **Regulatory citation summary** | • **21 CFR Part 892** – imaging device panel (classification). <br>• **21 CFR Part 807** – 510(k) submission requirements. <br>• **21 CFR Part 801** – labeling. <br>• **21 CFR Part 830** – UDI. <br>• **21 CFR Part 820** – QMSR (effective 02‑2026). <br>• FDA 2014 Guidance, Appendix A – SE decision points. <br>• Predetermined Change Control Plan (PCCP) guidance Dec 2024. | framework references only; no specific instance identifiers appear in source |

---

### Action Items for the Project Team
1. **Gather predicate data**: locate a cleared X‑ray system with a 510(k) number, release date, and labeling package.
2. **Draft intended‑use statement** that mirrors the predicate.
3. **Prepare comparison matrix** covering intended use, tech characteristics, and safety questions.
4. **Develop test plan** (radiation dose, image quality, mechanical safety) and execute bench studies.
5. **Confirm classification sub‑section** within 21 CFR Part 892; update docket accordingly.
6. **Update QMS documentation** to reflect new device design and risk analysis per ISO 14971.

If any of the *human‑escalation triggers* arise, pause work and route the issue to the senior regulatory manager for pathway reassessment.

---

### Peer Review Prompt
> @RegulatoryPeer – please challenge the assumptions above:  
> 1. Is the assumed Class II classification under Part 892 appropriate for the described X‑ray system, or could it fall under a different sub‑section?  
> 2. Does the source provide enough breadth to support using the traditional 510(k) route without invoking Special/Abbreviated pathways?  
> 3. Are there any jurisdiction‑specific gaps (e.g., MFDS or MDR equivalents) that we have omitted but should be considered for a global launch strategy?

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

1. Chunk `1061195424067242245`

> ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과제 3-2 SE 비교표 제출 필수 ---

2. Chunk `1072507187378217632`

> ### 4.1 SE 5단계 Decision Point (FDA 2014 Guidance Appendix A) ``` DP1. Predicate이 Legally Marketed Device인가? │ No → NSE (De Novo 또는 PMA) │ Yes ↓ DP2. 동일한 Intended Use인가? │ No → NSE │ Yes ↓ DP3. 동일한 Technological Characteristics인가? │ Yes → DP5 │ No ↓ DP4. 다른 기술특성이 Different Questions of Safety & Effectiveness를 제기하는가? │ Yes → NSE │ No ↓ DP5. 성능 데이터가 새 장치 ≥ Predicate 수준임을 입증하는가? │ Yes → SE (Clearance 가능) │ No → NSE ```

### kb-eval-20260723-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f4afc0898d20c8fb", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f4afc0898d20c8fb`
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

> **510(k) Predicate‑Strategy Draft**

---

### 1. Bottom Line  
*The product is a medical image management and processing system.  Under **21 CFR Part 892**, the applicable classification is Class II ( §892.2050 ). The appropriate submission route is a standard 510(k) with a Substantial Equivalence (SE) claim.*  

---

### 2. Classification & Submission Route  
| Item | Determination | Basis |
|------|---------------|-------|
| **Regulatory panel** | Imaging / Radiology devices | 21 CFR Part 892 (Imaging devices) |
| **Device class** | Class II | §892.2050 – “Medical image management and processing system” |
| **Submission type** | Traditional 510(k) | 21 CFR Part 807; standard SE pathway |
| **Predicate search** | Required as Step 1 in the source workflow | Source excerpt [2] “Predicate Device 조사 (FDA 510(k) Database)” |

*If a suitable predicate cannot be identified, consider a De Novo request or redesign to fit an existing predicate.*  

---

### 3. Evidence Package – Minimum Required Elements  
| Requirement | Typical Content | Source Note |
|-------------|----------------|------------|
| **Device Description & Indications for Use (IFU)** | Detailed description of hardware/software functions; intended clinical use, patient population, procedural workflow. | eSTAR Device‑Description guide cited in source [1]; no specific identifier – verify separately. |
| **Substantial Equivalence Comparison Table** | Row‑by‑row comparison of technological characteristics, performance specifications, labeling, and indications with the chosen predicate(s). | Source [2] “Substantial Equivalence 비교표 작성”. |
| **510(k) Summary** | Narrative summary of device description, intended use, design controls, and SE rationale. | Required by 21 CFR §807.92(a)(3). No identifier in source – verify separately. |
| **Performance Testing** (bench & clinical if needed) | • Image quality/processing accuracy<br>• Throughput, latency, storage reliability<br>• Software verification/validation per IEC 62304 | Mentioned in source [2] “성능시험”. |
| **Biocompatibility** (if device contacts patients) | ISO 10993‑1 assessment; extractable/leachable studies as applicable. | Source [2] “생체적합성”. No identifier – verify separately. |
| **Electromagnetic Compatibility / Electrical Safety** | IEC 60601‑1‑2 and IEC 60601‑1 testing reports. | Source [2] “전자파 등 섹션 준비”. No identifier – verify separately. |
| **Software Documentation** (if applicable) | • Software Description Document (SDD)<br>• Verification & Validation report<br>• Risk Management File per ISO 14971<br>• Predetermined Change Control Plan (PCCP) if AI/ML is used (FDA Guidance Dec 2024). | FDA PCCP cited in Fixed Rules; no source identifier – verify separately. |
| **Labeling** | Labels and IFU complying with 21 CFR Part 801, including UDI per 21 CFR Part 830. | No specific identifier in source – verify separately. |

---

### 4. Missing Information (to be sourced before filing)  
1. **Exact predicate device(s)** – FDA 510(k) database search results (model numbers, K‑numbers).  
2. **Finalized Intended Use statements** – must be precise and match the predicate scope.  
3. **Complete performance test protocols & results** – raw data, statistical analysis.  
4. **Biocompatibility rationale** (if patient‑contacting components exist).  
5. **U​DI issuance & GUDID registration plan** – UDI format per Part 830.  

*Absence of any of the above triggers a human escalation (see Section 6).*  

---

### 5. Risk Controls (per ISO 14971)  
| Control | Implementation |
|---------|----------------|
| **Hazard Identification & Risk Estimation** | Conducted during design‑control phase; documented in Risk Management File. |
| **Design Controls** | Design History File (DHF) includes specifications, verification/validation, and change management. |
| **Predetermined Change Control Plan (PCCP)** – if AI/ML algorithms are adaptive. |
| **Post‑Market Surveillance (PMS) & MDR Reporting** | FDA 21 CFR Part 803 for MDR; PMS plan outlined in submission. |
| **Usability Engineering** | Human factors testing per IEC 62366‑1, especially for user interface of image processing software. |

---

### 6. Human‑Escalation Triggers  
| Trigger | Action Required (Human) |
|---------|--------------------------|
| No suitable predicate found after exhaustive FDA 510(k) database search. | Initiate De Novo feasibility assessment or redesign. |
| Incomplete/unsatisfactory performance test data. | Pause submission; gather additional bench/clinical evidence. |
| Biocompatibility testing not applicable but regulatory guidance indicates requirement (e.g., disposable patient‑contacting accessories). | Conduct ISO 10993 testing before filing. |
| FDA requests “Additional Information” (AI) on any of the sections listed in source [2]. | Assign RA team to prepare a detailed response within the FDA‑specified timeframe. |
| Discrepancy between intended use and predicate labeling. | Revise IFU or select alternative predicate; re‑evaluate SE claim. |
| UDI issuance delayed beyond submission deadline. | Escalate to regulatory leadership for timeline adjustment or conditional filing. |

---

### 7. Citations (per instruction)  

- **Regulatory framework** – 21 CFR Part 807 (Premarket Notification); Part 892 (Imaging devices, §892.2050). *(framework reference – no verification needed)*  
- **Quality Management System Regulation** – 21 CFR Part 820 (effective Feb 2026).  
- **UDI requirements** – 21 CFR Part 830 (§830.10 onward).  
- **Risk management standard** – ISO 14971:2019.  
- **Software life‑cycle** – IEC 62304.  

*No specific identifiers (e.g., K‑numbers, §23‑44) were present in the source excerpts; therefore none are included.*  

---

### 8. Reusable RA Judgment (Lesson Learned)  
> *When drafting a 510(k) for an image‑processing system, always start with a documented predicate search (FDA 510(k) Database) and align the device’s intended use precisely to that predicate. Missing or vague IFU language is the most common cause of FDA “Additional Information” requests. Early completion of the performance test plan—including imaging accuracy and EMC—prevents downstream delays.*  

---

### 9. Peer‑Review Prompt  
> *Colleague, please challenge: (1) our assumption that a Class II classification under §892.2050 is appropriate for all image‑processing software; (2) whether any newer FDA guidance (post‑Dec 2024) might affect the PCCP requirement; and (3) if additional jurisdictional considerations (e.g., state‑level medical device regulations) need coverage in this draft.*

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

### kb-eval-20260723-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "6291944a92f64212", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `6291944a92f64212`
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

> **Regulatory Draft – Pathway Selection & Evidence Plan**

---

### 1. Classification / Submission Route Decision Tree  

| Device Profile | Most Likely FDA Pathway | Legal Basis (cited) | Predicate Needed? | Clinical Data Required? |
|----------------|------------------------|---------------------|-------------------|--------------------------|
| **Class I‑II (existing technology)** – clear predicate in the same panel (e.g., imaging, software) | **510(k) Premarket Notification** | FD&C Act § 510(k); 21 CFR § 807 | **Yes** (mandatory) | Conditional – see FDA guidance “Clinical Data Needed for 510(k)” (§ 3 referenced in source) |
| **Class I‑II (novel technology, no predicate)** – new intended use or substantially different tech | **De Novo Classification Request** | FD&C Act § 513(f)(2); 21 CFR § 860 | **No** | “If applicable” – FDA may still request clinical data depending on risk |
| **Class III (high‑risk, life‑supporting, implantable)** or any device for which a predicate cannot demonstrate SE | **Premarket Approval (PMA)** | FD&C Act § 515; 21 CFR § 814 | **No** | **Required** – robust clinical trial data per FDA PMA guidance |

> **Bottom‑line recommendation:**  
If the device under development is a **Class II imaging or software system** with an existing FDA‑cleared device performing the same intended use, pursue **510(k)**. If no predicate exists but the risk profile remains within Class II, consider **De Novo** to establish a new classification. For any **Class III** indication, default to **PMA**.

---

### 2. Required Evidence Packages  

| Evidence Category | Typical Content (510(k) Path) | Notes & Gaps |
|-------------------|--------------------------------|--------------|
| **Device Description & Intended Use** | Complete labeling, indications, contraindications, user environment. | *Missing:* detailed intended use statement; confirm panel (e.g., Part 892 for imaging). |
| **Substantial Equivalence Comparison** | Side‑by‑side table of device specifications, performance metrics, and technological characteristics vs. predicate(s). | *Missing:* identified predicate clearance numbers. |
| **Performance Testing** | Bench (electrical safety, electromagnetic compatibility), software verification/validation (if applicable), biocompatibility (per ISO 10993). | Verify that testing aligns with recognized standards; no specific standard numbers cited in source – add as needed (e.g., IEC 60601‑1). |
| **Risk Management** | ISO 14971 risk analysis file, mitigation measures, design controls per 21 CFR § 820.30. For AI/ML: Predetermined Change Control Plan (PCCP) if employing adaptive algorithms (FDA Guidance Dec 2024). | *Missing:* completed risk management report; confirm need for PCCP. |
| **Clinical Data** | If FDA guidance flags it as “conditional,” provide limited clinical performance data (e.g., prospective observational study, post‑market surveillance plan). Source notes conditionally required (§ 3) – verify applicability to the specific device. | *Missing:* confirmation of whether clinical data are mandated; determine based on risk and predicate comparison. |
| **Quality Management System (QMSR)** | ISO 13485‑aligned QMS compliant with 21 CFR § 820 (effective Feb 2026). Documentation of design history file, device master record, complaint handling. | *Missing:* evidence of QMS implementation; upcoming compliance deadline (Feb 2026) must be met before submission. |
| **UDI & Labeling** | UDI label format per 21 CFR § 830.10‑§ 830.60, GUDID registration, labeling per 21 CFR § 801. | *Missing:* assigned Device Identifier (DI) and Production Identifier (PI). |
| **eSTAR Registration** | If device is Class II with a 510(k), ensure eSTAR filing (mandatory from 2023‑10‑01). | Verify eSTAR status; source indicates FY2025 user fee ~$22,171. |

---

### 3. Risk Controls & Regulatory Safeguards  

1. **Design Controls** – Implement § 820.30 (design planning, inputs, outputs, verification, validation).  
2. **ISO 14971** risk analysis – identify hazards, estimate severity/likelihood, apply mitigation hierarchy.  
3. **Software / AI‑ML** – Draft a **Predetermined Change Control Plan (PCCP)** if the device employs adaptive algorithms (FDA final guidance Dec 2024).  
4. **Post‑Market Surveillance** – Develop a PMS plan aligned with § 822.30, especially if clinical data are limited.  

---

### 4. Citations from Source  

| Item | Citation (per source) |
|------|-----------------------|
| Legal basis for 510(k) pathway | FD&C Act **§ 510(k)**; **21 CFR § 807** |
| Legal basis for De Novo pathway | FD&C Act **§ 513(f)(2)**; **21 CFR § 860** |
| Legal basis for PMA pathway | FD&C Act **§ 515**; **21 CFR § 814** |
| Clinical data requirement qualifier (conditional) – mentioned in source as “조건부 (§3 참조)” | *no specific identifier found in source — verify separately* |
| User fee amounts & eSTAR obligation dates | *no specific identifier found in source — verify separately* |

---

### 5. Missing Information – Action Items  

| Gap | Why Critical | Next Step |
|-----|--------------|-----------|
| **Exact intended use and target patient population** | Determines classification panel (e.g., imaging → Part 892) and risk level. | Obtain from product development team. |
| **Predicate device(s) & clearance numbers** | Required for 510(k) SE argument. | Conduct predicate search in FDA’s 510(k) database; list identifiers. |
| **Device’s technological attributes (hardware, software architecture)** | Needed for SE comparison and risk analysis. | Provide detailed spec sheet. |
| **Clinical data plan or existing study results** | Determines if clinical data are “conditional” or mandatory. | Align with FDA guidance referenced in source; draft protocol. |
| **QMSR compliance evidence (ISO 13485 certification, SOPs)** | Mandatory for any 510(k) submission after Feb 2026. | Compile QMS documentation and audit reports. |
| **UDI assignment & GUDID record** | Required labeling per Part 830. | Request DI/PI from issuing agency; register in GUDID. |

---

### 6. Human‑Escalation Triggers  

- **Unclear Classification:** If panel (e.g., imaging vs. clinical chemistry) cannot be verified → escalate to senior RA or FDA pre‑submission meeting.  
- **No Predicate Identified:** When predicate search returns no matching cleared device → consider De Novo; requires senior review and possibly a request for classification feedback.  
- **Clinical Data Requirement Ambiguity:** If “conditional” status (§ 3) cannot be resolved based on risk/technology comparison → consult FDA via Q‑Submission or request pre‑market meeting.  
- **QMSR Non‑Compliance:** Evidence that ISO 13485 alignment is incomplete after Feb 2026 deadline → halt submission preparation; engage quality assurance lead.  
- **UDI/Labeling Gaps:** Missing DI/PI or GUDID registration → pause clearance filing until resolved.  

**Escalation Path:** Document trigger, assign to RA lead, schedule review within 5 business days, and determine need for FDA interaction.

---

### 7. Peer Review Prompt  

> *Colleague, please evaluate the assumptions made in this pathway selection (especially the classification of the device as Class II with a viable predicate), verify that all regulatory citations are correctly matched to the source excerpts, and identify any jurisdiction‑specific gaps—such as missing Part 892 section confirmation for imaging devices or additional post‑market reporting obligations under 21 CFR § 803.*

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

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20260723-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "cf2ed6bdc3532ef9", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cf2ed6bdc3532ef9`
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

> **Regulatory Draft – Imaging Workstation Software (GUI SW) 510(k) Strategy**

---

### 1. Bottom‑Line Recommendation  
- **Classification:** Class II, 21 CFR §892.2050 (Medical image management and processing system).  
- **Submission Route:** Traditional 510(k) demonstrating substantial equivalence to a *single* primary predicate that matches the intended use (IFU) on a word‑by‑word basis.  
- **Key Decision Path:** Select a recent (≤ 5 yr) cleared predicate; if older than 7 yr, prepare additional justification per FDA “use of predicates” modernization guidance.

---

### 2. Required Evidentiary Package  

| Category | Evidence Needed | Source / Regulatory Basis |
|----------|----------------|---------------------------|
| **Device Description & Intended Use** | Full narrative, user‑interface mock‑ups, IFU text (identical or narrower than predicate) | §892.2050; checklist item “Indications for Use 원문 문자 수준 비교” – *source [1]* |
| **Predicate Identification** | • K‑number of primary predicate  <br>• Confirmation predicate still marketed (not retired/discontinued) <br>• No recall/safety communication on predicate (MAUDE/Recall DB) | §807.92; checklist items “Predicate이 시장에서 여전히 판매 중인지”, “Recall/Safety Communication 대상인지 확인” – *source [1]* |
| **Comparison Table** | Side‑by‑side comparison of indications, labeling, technological characteristics; justification for any differences (with supporting data) | §807.92(b)(3); checklist item “기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인” – *source [1]* |
| **Software Documentation Level** | Identify Basic vs. Enhanced documentation per FDA 2023 Software Guidance; provide required design history file, verification/validation protocols & reports | 21 CFR §§820.30–820.50 (QMSR); FDA “Basic/Enhanced” guidance – *source [2]* |
| **IEC 62304 Safety Class** | Declare class A/B/C and attach software life‑cycle processes; risk management file (ISO 14971) aligned to the safety class | IEC 62304, ISO 14971; required for FDA review of medical device software |
| **DICOM Conformance Statement** | Formal statement covering Storage SCU/SCP, Worklist SCU, MPPS, Print SCU etc. | §892.2050 labeling requirement; checklist “DICOM 적합성 진술서” – *source [2]* |
| **AI/ML Module (if present)** | Predetermined Change Control Plan (PCCP) covering post‑market algorithm updates; training data set description; performance monitoring plan | FDA Final Guidance Dec 2024 “Predetermined Change Control Plan (PCCP)” |
| **Cybersecurity Controls** | Authentication method, encryption scheme, audit log design, secure update mechanism, threat model summary | §820.30(c) (Design controls); FDA 2022 Cybersecurity Guidance |
| **SBOM** | SPDX or CycloneDX format listing all third‑party components and versions | §820.30(e) (Software product integrity) |
| **Interoperability Claims** | Evidence of HL7 FHIR, IHE profile conformance (e.g., Scheduled Procedure Step, Radiology Object Workflow) | §892.2050; checklist “Interoperability (HL7 FHIR, IHE profiles 지원 여부)” – *source [2]* |
| **UDI Labeling** | Device identifier per 21 CFR §830.10‑§830.60; inclusion in GUDID | Part 830 labeling sections |
| **QMSR Compliance** | ISO 13485‑aligned quality system (effective Feb 2026) – procedures for design control, document control, CAPA, etc. | 21 CFR §820 (effective 2026‑02 as QMSR) |

---

### 3. Missing Information / Gaps to Resolve  

| Gap | Why Needed | Action |
|-----|------------|--------|
| Exact **Intended Use** wording of the device | Required for word‑by‑word IFU comparison with predicate | Draft IFU; compare to candidate predicates |
| **Predicate K‑numbers** and market status | Must show predicate is still commercially available and not recalled | Search FDA 510(k) database (product code filter), verify in Recalls DB |
| **Age of Predicate** (cleared > 7 yr?) | May trigger “additional justification” per modernized use‑of‑predicates policy | If older, compile supplemental data (e.g., technology literature, post‑market surveillance) |
| **Differences list with supporting data** (hardware requirements, OS support, language localization) | Needed for substantial equivalence justification | Produce a matrix with source data (bench testing, usability studies) |
| Confirmation of **AI/ML inclusion** and PCCP scope | Determines whether a PCCP must be submitted | If AI/ML present, develop PCCP per 2024 guidance |
| Detailed **hardware platform specification** (minimum CPU, RAM, storage) | Required for performance validation & labeling | Gather OEM spec sheets; include in submission |
| **Cybersecurity threat model** and mitigation plan | FDA expects risk‑based cyber controls | Conduct NIST 800‑53/CSF based analysis; attach to submission |
| **SBOM generation process** (tooling, version control) | Required for software component traceability | Generate SPDX/CycloneDX file; include in 510(k) package |
| **Clinical performance evidence** (if any new indications or algorithmic changes) | May be required if predicate does not fully cover intended use | Plan bench‑to‑clinical validation study if gaps identified |

---

### 4. Risk Controls & Compliance Mapping  

| Regulation / Standard | Control Element | Implementation Note |
|-----------------------|-----------------|---------------------|
| **21 CFR §892.2050** (Class II) | Labeling, performance testing, safety labeling | Include DICOM and IEC 62304 statements |
| **21 CFR Part 820 (QMSR)** | Design controls, document control, CAPA, post‑market surveillance | Align QMS to ISO 13485 (effective Feb 2026) |
| **IEC 62304** | Software life‑cycle processes, verification/validation per safety class | Classify as B or C depending on risk; attach risk analysis |
| **ISO 14971** | Risk management file with hazard identification, evaluation, mitigations | Map to software safety classes and cybersecurity risks |
| **FDA 2023 Software Guidance** | Determine Basic vs. Enhanced documentation package | Prepare appropriate design history file |
| **Predetermined Change Control Plan (PCCP)** | Pre‑authorised AI/ML updates | Draft PCCP if AI/ML component exists |
| **21 CFR §830.10‑§830.60** | UDI label on device and packaging | Assign Device Identifier (DI) and Production Identifier (PI) |
| **Cybersecurity Guidance (2022)** | Authentication, encryption, audit logging, secure updates | Incorporate into software design controls |

---

### 5. Human‑Escalation Triggers  

1. **Predicate Uncertainty** – If no clear, still‑marketed predicate within 5 years is found, escalate to senior RA for possible De Novo pathway evaluation.  
2. **AI/ML Inclusion Ambiguity** – Any doubt about whether the software contains a learning algorithm triggers escalation to the AI/ML specialist to develop a PCCP.  
3. **Regulatory Gap in Clinical Evidence** – If intended use extends beyond the selected predicate’s indications, escalate for clinical performance study planning.  
4. **QMSR Alignment Gap** – If the organization’s quality system has not yet been updated to the 2026‑02 QMSR requirements, escalation to Quality Assurance leadership is required before filing.  
5. **UDI Allocation Issues** – Failure to obtain a valid FDA‑issued DI within the submission timeline escalates to the Regulatory Operations lead.

---

### 6. Peer Review Prompt  

> *"Please review the predicate selection assumptions, the completeness of the evidence checklist (especially AI/ML PCCP coverage and cybersecurity documentation), and any jurisdiction‑specific gaps (e.g., state‑level radiation safety reporting) that may affect a 510(k) for an imaging workstation software."*  



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

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20260723-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "da59013799f31ba4", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_PreSubmission_QSub_가이드.md", "source_hash": "417191845804e82051a123525f91ed116a02c2eba4f516018604d1460525c8f5"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `da59013799f31ba4`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_PreSubmission_QSub_가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/FDA_PreSubmission_QSub_%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `417191845804e82051a123525f91ed116a02c2eba4f516018604d1460525c8f5`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `FDA_PreSubmission_QSub_가이드.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 3.1 Cover Letter (표지 서한) | 필드 | 내용 | |---|---| | 제목 | "Pre-Submission for [Device Name]" | | 회사명, 주소 | 정식 등록 정보 | | Primary Contact | 이름, 직함, 전화, 이메일 | | Regulatory Contact | 담당 RA 담당자 | | 제출 목적 | 한 문단 (어떤 피드백이 필요한가) | | 계획 중인 제출 유형 | 예: "510(k) 제출 예정" / "IDE 신청 전 SRD 요청" | | 회의 요청 여부 | 서면 피드백만 / 회의 병행 중 선택 | ## 7. 3개 지역 Pre-Sub 동등 제도 비교 | 항목 | FDA (미...
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

> **Regulatory Draft – 510(k) Predicate‑Strategy Planning**

---

### Bottom‑Line Recommendation
1. **Classification & Pathway** – Treat the product as a Class II medical device and pursue a traditional 510(k) submission.  
   *If the intended use involves radiology/imaging, apply **21 CFR §892** (e.g., §892.2050 for image‑processing software). Otherwise, determine the correct classification through the FDA Product Classification Database and cite the applicable CFR part.*  

2. **Pre‑Submission Timing** – File a Q‑Sub (Pre‑Submission) **6–12 months before the planned 510(k)** to obtain non‑binding feedback on predicate selection, testing plan, and labeling. The source notes this as “FDA: 510(k) submission 6~12 months prior – Pre‑Sub 1 time mandatory consideration.” *(no specific identifier found in source — verify separately).*

3. **Key Evidence Required**  
   - Predicate device dossier (cleared 510(k) number, substantial‑equivalence rationale).  
   - Bench‑top performance data (e.g., accuracy, precision, safety testing).  
   - If software‑based, validation per **21 CFR §820.30(c)(3)** and a **Predetermined Change Control Plan (PCCP)** for any future AI/ML updates.  
   - Clinical data only if required to bridge gaps with the predicate (risk‑based determination).  

4. **Missing Information** – The current brief does not contain:  
   - Device name, model, and intended use statement.  
   - Proposed classification or a candidate predicate device(s).  
   - Summary of design / performance claims.  
   - Draft labeling (including intended-use statements).  

5. **Risk‑Control Recommendations**  
   - **Design Controls** – Implement the QMSR requirements of **21 CFR Part 820** (effective Feb 2026, ISO 13485 alignment). Include a Design History File, risk management per ISO 14971, and verification/validation plans.  
   - **Software Lifecycle** – If software is involved, follow FDA’s **December 2024 Guidance on Predetermined Change Control Plans (PCCP)**; document change‑control categories, monitoring, and post‑market surveillance.  
   - **UDI Compliance** – Assign a UDI per **21 CFR Part 830**, ensuring label and GUDID submission ( §§830.10–830.60).  

6. **Citation Summary**  
| Requirement | Source / Regulation | Identifier |
|-------------|---------------------|------------|
| 510(k) procedural rule | 21 CFR §807 | — |
| Class II imaging device classification (example) | 21 CFR §892.2050 (image‑processing software) | no specific identifier found in source — verify separately |
| QMSR (ISO 13485 aligned) | 21 CFR Part 820 | — |
| UDI labeling obligations | 21 CFR Part 830 (§830.10 onward) | — |
| Predetermined Change Control Plan guidance | FDA Guidance, Dec 2024 (PCCP) | no specific identifier found in source — verify separately |
| Pre‑Submission (Q‑Sub) process timing | Source excerpt “FDA: 510(k) submission 6~12 months prior – Pre‑Sub 1 time mandatory” | no specific identifier found in source — verify separately |

7. **Human‑Escalation Triggers**  
   - **Trigger A:** Absence of a clearly defined intended use or predicate → pause drafting; request detailed device description and intended‑use statement.  
   - **Trigger B:** Uncertainty whether the device falls under Part 892 (imaging) vs. another panel → consult FDA’s Product Classification Database or seek clarification via a Pre‑Submission.  
   - **Trigger C:** Any change to software algorithm after 510(k) acceptance that is not covered by an approved PCCP → initiate a supplemental 510(k) or request a new PCCP amendment.  
   - **Trigger D:** Discrepancy between planned evidence and FDA’s feedback on the Q‑Sub (e.g., additional clinical data required) → re‑work testing plan before final 510(k) assembly.  

---

**Regulatory Judgment:** Proceed with a traditional 510(k) pathway, schedule a Pre‑Submission **6–12 months** ahead of the target filing date, and gather the missing device‐specific information listed above. Implement full Part 820 QMSR controls and prepare UDI data per Part 830.  

---

### Peer Review Prompt
*Colleague, please challenge the following assumptions:*

1. The classification under **Part 892** is appropriate for the (unspecified) device – could it belong to a different panel?  
2. The single Pre‑Submission described is sufficient; are there scenarios where additional Q‑Subs or early‑stage interactions would be advisable?  
3. Does the evidence set outlined (bench testing, optional clinical data) fully address potential gaps in substantial‑equivalence arguments for high‑risk imaging functions?  

*Identify any jurisdiction‑specific gaps (e.g., EU MDR or Korean MFDS considerations) that should be captured now to avoid later rework.*

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

1. Chunk `124523812258860464`

> ### 3.1 Cover Letter (표지 서한) | 필드 | 내용 | |---|---| | 제목 | "Pre-Submission for [Device Name]" | | 회사명, 주소 | 정식 등록 정보 | | Primary Contact | 이름, 직함, 전화, 이메일 | | Regulatory Contact | 담당 RA 담당자 | | 제출 목적 | 한 문단 (어떤 피드백이 필요한가) | | 계획 중인 제출 유형 | 예: "510(k) 제출 예정" / "IDE 신청 전 SRD 요청" | | 회의 요청 여부 | 서면 피드백만 / 회의 병행 중 선택 |

2. Chunk `367708542439035920`

> ## 7. 3개 지역 Pre-Sub 동등 제도 비교 | 항목 | FDA (미국) | MFDS (한국) | MDR/NB (유럽) | |---|---|---|---| | 제도명 | Pre-Submission (Q-Sub) | 사전상담 (제조·수입업 허가 전 상담) | NB Early Dialogue / Scientific Advice | | 법적 구속력 | 없음 (non-binding) | 없음 (참고 의견) | 없음 (NB opinion) | | 응답 목표 | 70일 (서면) / 100일 (회의) | 명시 없음 (통상 수 주) | NB별 상이 (30~90일) | | 비용 | 무료 (PDUFA/MDUFA 포함) | 무료 | NB 과금 (별도 견적) | | 온라인 제출 | CDRH Portal (PreSTAR) | 민원24 / 온라인 신청 [검증 필요] | NB 시스템별 상이 | | 제출 빈도 제한 | 없음 (단, 과도한 중복 질문 지양 권고) | 없음 | NB별 상이 | | X-ray 특이사항 | CDRH 방사선 부서(OSB) 담당 | 의료기기안전국 체외진단기기과 [검증 필요] | NB 방사선 전문 심사관 배정 | **자사 행동 지시 (3개 지역)**: - **FDA**: 510(k) 제출 6~12개월 전 Pre-Sub 1회 필수 고려 (시험...

## ra_eu

### kb-eval-20260723-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3c458ddac864fc0b", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `3c458ddac864fc0b`
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

> **Regulatory Draft – Classification & Conformity‑Assessment Plan  
Ionising‑radiation Diagnostic Device (X‑ray Generator)**  

---

### 1. Device Synopsis (derived from the limited source)

| Item | Description |
|------|-------------|
| **Intended purpose** | Generation of ionising X‑ray radiation for diagnostic radiology (e.g., projection radiography). |
| **Primary mode of action** | Emits ionising radiation that is directed to a patient to create a diagnostic image. |
| **Key characteristics** | Power output, beam quality, filtration, safety interlocks, dose‑rate control. |
| **Regulatory source excerpt** | “Rule 10: 이온화 방사선 방출 진단기기 (X‑ray 발생장치 → Class IIb)”【2】 |

---

### 2. Classification  

| Reference | Content |
|-----------|---------|
| **Classification rule** | **Rule 10** – active devices for diagnosis/monitoring that emit ionising radiation. |
| **Annex where rule resides** | Annex VIII, Rule 10 (MDR 2017/745). |
| **Resulting class** | **Class IIb** (as indicated in the source). |

*Citation*: Rule 10 – Annex VIII → Class IIb【2】.

---

### 3. Required Conformity‑Assessment Route  

| Class | MDR route (Annex) | Typical deliverables |
|-------|-------------------|----------------------|
| IIb   | **Annex IX** – assessment of the quality‑management system *plus* technical documentation by a Notified Body. |

*Citation*: Annex IX specifies the conformity‑assessment procedure for Class IIb devices【1】.

---

### 4. Evidence Package Required (MDR checklist)

| Evidence | Regulatory basis | What must be supplied |
|----------|------------------|-----------------------|
| **Technical Documentation** | Annex II – “Technical documentation”. | Device description, intended use, design & manufacturing information, labeling, risk management file, verification/validation data, post‑market surveillance plan, etc. |
| **Risk Management** | ISO 14971 (incorporated via GSPR §17–§20). | Risk analysis, evaluation, control measures, residual risk assessment; must demonstrate compliance with §§16.4 (radiation protection) and §18 (active devices). |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – “Clinical Evaluation”. | Literature review, clinical data (clinical investigations or equivalent), benefit–risk determination, kept current under Art. 61. |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Annex XIV Part B – “PMCF”. | Planned PMCF activities, methodology, timelines; final evaluation report linking to conclusions of the CER. |
| **PMS System** | Art. 83 (system), Art. 84 (plan). | PMS system description, processes for data collection/analysis, reporting obligations. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 – required for Class IIb “at least annually”. Contains: (a) benefit‑risk conclusions; (b) main findings of PMCF; (c) sales volume & user population estimate. |
| **Labeling & IFU** | Annex I §23 – “Information supplied with the device”. | Labels, Instructions for Use, safety notices, radiation dose information, compliance statements. |
| **Essential Performance & Safety Tests** | GSPR checklist (e.g., §§16‑18); IEC 60601‑2‑54 (X‑ray equipment). | Electrical safety, electromagnetic compatibility, radiation output measurements, beam geometry, dose‑area product limits, interlock functionality. |
| **Software Documentation (if applicable)** | Rule 11 – SaMD; Annex I §17 & IEC 62304. | Software life‑cycle files, validation, classification justification. |

*Key citations*:  
- Technical docs – Annex II【1】  
- Risk management – GSPR §§16.4, 17–20 (Annex I)【1】  
- CER – Annex XIV Part A; Art. 61【1】  
- PMCF – Annex XIV Part B【1】  
- PMS system – Art. 83 & Art. 84【1】  
- PSUR – Art. 86 (annual for Class IIb)【1】  
- Labeling – Annex I §23【1】  
- IEC 60601‑2‑54 – “X‑ray equipment for radiography and radioscopy” (industry standard for radiation safety).  

---

### 5. Gaps / Missing Information (must be clarified before submission)

| Gap | Why it matters | Suggested source of data |
|-----|----------------|--------------------------|
| **Exact intended use wording** (clinical indication, patient population) | Needed to confirm that Rule 10 applies and to frame the CER. | Manufacturer’s product specification/marketing dossier. |
| **Detailed device architecture & component list** (including any software modules) | Required for Annex II technical file and for risk analysis (especially if Software is a Device). | Engineering design files, BOM, firmware description. |
| **Radiation performance data** (dose‑rate, beam quality, field size, leakage, compliance with IEC 60601‑2‑54) | Basis for GSPR §16.4 and to demonstrate essential safety. | Test reports from accredited lab. |
| **Clinical evidence strategy** – whether a dedicated clinical investigation is planned or reliance on equivalence/clinical literature. | Determines scope of CER & PMCF plan. | Clinical evaluation plan, predicate device data (if any). |
| **Post‑Market Surveillance (PMS) Plan details** (data sources, follow‑up intervals, responsible personnel) | Required by Art. 84 and to feed PSUR. | PMS SOPs, risk‑based monitoring matrix. |
| **Manufacturing quality system documentation** (QMS scope, certified ISO 13485) | Needed for Annex IX audit. | QMS manual, internal audit reports. |
| **Usability / Human factors validation** (especially for lay‑person use if applicable) | Relevant to GSPR §22 and safety of operation. | Usability testing report (IEC 62366‑1). |
| **Sterilisation or cleaning validation** (if device is reusable) | Impacts risk management & labeling. | Validation protocols & results. |

*Note*: All above items are not present in the supplied excerpts; they must be obtained from the manufacturer’s internal files.

---

### 6. Risk Controls – Core Measures Required for a Class IIb X‑ray Generator  

| Hazard | Control (per GSPR) | Evidence |
|--------|--------------------|----------|
| **Radiation over‑exposure** | Automatic dose limiting, beam‑on interlocks, pre‑set exposure parameters, shielding design. | IEC 60601‑2‑54 test reports; risk analysis showing residual risk ≤ acceptable level (§16.4). |
| **Electrical shock / fire** | Compliance with IEC 60601‑1 (general safety), insulation testing, fault monitoring. | Electrical safety test data, conformity to GSPR §20. |
| **Incorrect device set‑up by user** | Clear labeling, IFU with step‑by‑step setup instructions, training program for operators. | Labeling review (§23) and usability validation (IEC 62366‑1). |
| **Software malfunction (if software controls exposure)** | Software development according to IEC 62304, verification & validation, periodic updates via PMCF. | Software files, validation report, classification justification under Rule 11. |
| **Mechanical failure of moving parts** (e.g., collimator) | Design safeguards, periodic maintenance schedule, mechanical stress testing. | Mechanical test reports, maintenance SOPs. |

All controls must be documented in the risk‑management file and cross‑referenced to the GSPR sections cited above.

---

### 7. Human‑Escalation Triggers  

| Situation | Trigger for human intervention (RA lead / Notified Body liaison) |
|-----------|-------------------------------------------------------------------|
| **Unclear classification** – any ambiguity whether Rule 10 or another rule applies (e.g., if the device includes a detector module). | Escalate to senior RA for final rule‑selection justification; obtain NB opinion before dossier submission. |
| **Missing clinical evidence** – no adequate clinical data to demonstrate performance/safety. | Pause dossier preparation; initiate clinical investigation or equivalence study; notify project manager. |
| **Residual risk exceeds acceptability** after applying all controls (per ISO 14971). | Immediate risk‑mitigation plan required; senior RA must approve risk acceptance before proceeding. |
| **Non‑conformity with IEC 60601‑2‑54** – test report shows failure of radiation safety limits. | Stop the conformity‑assessment process; engineering redesign required; inform quality management. |
| **PMS/PMCF plan not aligned with class IIb timeline (annual PSUR)** – insufficient resources or data capture mechanisms. | RA must request additional resources or adjust surveillance schedule; elevate to compliance officer. |
| **Labeling/IFU gaps** – missing warnings, dose information, or language requirements for EU markets. | Escalate to documentation team and legal; revise labeling before NB audit. |

When any trigger is met, the responsible RA should log a comment in the work‑package, recommend closure of the current WP only after resolution, and request human approval before moving forward (per Fixed Rule 1).

---

### 8. Summary Judgment  

- **Classification:** Class IIb under MDR 2017/745 **Rule 10** (Annex VIII).  
- **Conformity‑assessment route:** **Annex IX** (full QMS + technical documentation assessment by a Notified Body).  
- **Core dossier elements** (technical file, risk management, CER, PMCF, PMS system, PSUR, labeling, test data) must be compiled per the MDR articles and annexes cited above.  

The current knowledge base provides only the classification rule and high‑level regulatory expectations; several critical pieces of information are missing (intended use details, performance test reports, clinical evidence strategy, complete risk‑management file). These gaps trigger the escalation points listed in Section 7.

---

**Peer‑review request:**  
*Please review the assumptions made about applicable MDR clauses, the completeness of the required evidence list, and any jurisdiction‑specific nuances (e.g., national “deemed conformity” provisions) that may affect this Class IIb X‑ray generator. Highlight any missing citations or potential over‑reliance on general statements.*

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

### kb-eval-20260723-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e943ded4dd4d76d4", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e943ded4dd4d76d4`
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

---

### 1. Classification Determination  

| Step | Requirement (Regulation) | Action Required | Evidence to be filed |
|------|---------------------------|-----------------|----------------------|
| **1.1 Identify intended purpose & mode of action** | Article 51 MDR – “intended medical purpose” defines the scope for classification. | Collect the full Intended Use Statement, indications, target patient group, and description of the energy/mechanism used (e.g., active therapeutic, diagnostic, software). | Manufacturer’s Product Specification File (PSF) – free‑text statement plus labelled claims. |
| **1.2 Apply Annex VIII classification rules** | Annex VIII – 22 sequential rules; the highest‑class rule that applies determines the class. | Map device attributes to each rule (e.g., Rule 9, 10, 11, 17 etc.). If more than one rule matches, select the rule giving the higher class. | Decision matrix linking product features to the specific Annex VIII rule number and resulting class (e.g., “Rule 9 – active therapeutic → Class IIb”). |
| **1.3 Verify with Competent Authority or MDCG Guidance** | When doubt exists, refer to national CA or MDCG *Manual on Borderline and Classification* (latest 2023‑09 v2.1.1). | Submit a classification query (if needed) together with the rule‐application worksheet. | Confirmation letter / opinion from the CA; otherwise retain internal justification file. |

**Citations** – Article 51 MDR; Annex VIII (classification rules); MDCG Manual (2023‑09 v2.1.1) – “no specific identifier found in source — verify separately”.

---

### 2. Selected Conformity‑Assessment Route  

| Class | Applicable Annex(es) for assessment | Typical route for a commercialised device |
|-------|--------------------------------------|-------------------------------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration – Annex IV (EU Declaration of Conformity). No NB involvement. |
| **Class Is / Im** | Notified Body audit of the quality management system (QMS) per **Annex IX** and technical documentation per **Annex II**. |
| **Class IIa, IIb, III** | Full NB assessment – **Annex IX** (QMS + technical file) *or* **Annex X** (type‑examination) for parts of the device; production conformity verification via **Annex XI** when required by the NB. |

*The actual route will be finalised once the class is confirmed in Section 1.*

---

### 3. Technical Documentation & Clinical Evidence Requirements  

| Document | Regulatory basis | Minimum content |
|----------|------------------|-----------------|
| **Technical Documentation (TD)** | Annex II MDR – “technical documentation” | • Device description, labeling, specifications<br>• Risk Management file (ISO 14971) (§15‑18 of Annex I)<br>• Design & manufacturing information<br>• Verification & validation results<br>• Post‑Market Surveillance (PMS) plan (Art. 84) |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under **Article 61** MDR | • State of the art literature review<br>• Clinical data – either clinical investigations or equivalence data<br>• Benefit‑risk analysis (conclusions) |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | • Objectives, methodology, timelines for any prospective data collection needed to confirm safety/performance.<br>• Interim and final PMCF evaluation report. |
| **Periodic Safety Update Report (PSUR)** | Article 86 MDR (for Class IIa/IIb/III) | • Benefit‑risk determination conclusions (Art. 86(1)(a))<br>• Main findings of the PMCF (Art. 86(1)(b))<br>• Sales volume & user population estimate (Art. 86(1)(c)). |
| **Vigilance / Incident Reporting** | Article 87 MDR (Vigilance) & national law §31 의료기기법 (Korea) referenced in source | • Process for reporting serious incidents, field safety corrective actions (FSCAs). |

*No specific identifiers are supplied in the source excerpts – verify separately that any national‑specific forms (e.g., Korean “이상사례 보고” templates) comply with Art. 87.*

---

### 4. Identified Missing Information (Gap Analysis)

| Gap | Why it matters | What must be provided |
|-----|----------------|-----------------------|
| **Intended purpose & mode of action** | Needed to select the correct Annex VIII rule and the corresponding classification class. | Full Intended Use Statement with clear claim language, including any active functions or software decision‑making. |
| **Device architecture description** (e.g., active therapeutic vs diagnostic, presence of radiation, software components) | Determines which specific Rule (9, 10, 11, 17…) applies. | Block diagram, list of sub‑assemblies, and the function of each element. |
| **Equivalence / Predicate data** (if claiming conformity via established device) | Required for CER if clinical investigation is not performed; must satisfy “reasonable equivalence” test. | Identification of comparable CE‑marked device(s), side‑by‑side comparison table covering specifications, intended purpose, and performance. |
| **Clinical data set** (clinical investigations or real‑world evidence) | Mandatory for the CER under Art. 61. | Protocols, study reports, or post‑market data extracts aligned with the risk classification (higher class → more robust data). |
| **Risk Management file (ISO 14971)** | GSPR §§15‑18 demand documented risk analysis and control measures. | Hazard identification list, risk evaluation matrix, implemented controls, residual risk appraisal. |
| **PMS plan & PMCF strategy** | Art. 84/86 require a systematic process; missing items lead to non‑compliance with post‑market obligations. | Detailed schedule of data collection, defined performance indicators, and responsibility matrix. |
| **UDI registration** (EUDAMED entry) | Source mentions UDI portal & EUDAMED – required for market placement. | Allocation of a device identifier, registration of the manufacturer/Authorized Representative in EUDAMED, linking to technical file. |

---

### 5. Core Risk Controls (to be reflected in the TD & RMF)

| Control | Relevant GSPR / Standard | Implementation note |
|---------|--------------------------|---------------------|
| **Protective measures for active devices** | Annex I §18 (Active devices) & §16 (Radiation protection, if applicable) | Design safeguards, fail‑safe circuitry, built‑in limits. |
| **Software safety lifecycle** | Annex I §17; IEC 62304 | Follow software development plan, verification/validation, vulnerability management. |
| **Usability engineering** | IEC 62366‑1 | Conduct user‑interface risk assessment (e.g., use errors that could lead to serious injury). |
| **Electrical safety & EMC** | IEC 60601‑1 series (general) plus modality‑specific standards if X‑ray, CT etc. | Test reports and compliance certificates attached to TD. |
| **Sterility assurance (if applicable)** | Annex I §19 (Active implantable) / ISO 11135 | Validation of sterilisation process and packaging integrity. |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger point | Escalation path |
|-----------|----------------|-----------------|
| **Unresolved classification dispute** (multiple Annex VIII rules could apply) | No internal consensus after the rule‑application worksheet is completed. | Raise to Senior RA Lead → request formal opinion from Competent Authority or submit a *Classification Query* to the national CA. |
| **Insufficient clinical evidence for CER** (e.g., missing comparable device, inadequate sample size) | Gap identified in Section 4 and cannot be closed with existing data within the project timeline. | Pause submission preparation; convene Clinical Evidence Working Group → consider additional clinical investigation or expanded post‑market data collection. |
| **Risk Management residual risk remains unacceptable** (risk–benefit not justified) | Residual risk > acceptable level after all controls applied (ISO 14971). | Immediate halt of development; Senior Engineer & QA must re‑design; senior RA to document justification and seek Notified Body input before proceeding. |
| **PMS/PMCF plan gaps** (no defined data‑collection methodology) | PMS Plan not approved by the internal Compliance Committee. | Forward to Chief Clinical Officer for PMCF design; if still unresolved, elevate to Executive Management → potential market entry delay. |
| **UDI / EUDAMED registration failure** (duplicate or missing UDI) | Registration error returned from EUDAMED portal. | Notify Regulatory Operations Manager; engage IT & label supplier to correct the identifier before product release. |

---

### 7. Summary Judgment  

1. **Classification:** Must be performed by applying Annex VIII rules to the finalized intended purpose and device architecture (Article 51 MDR).  
2. **Conformity‑assessment route:** Determined by the resulting class – likely **Annex IX** (full NB assessment of QMS + TD) for Class IIa/IIb/III, or self‑declaration for Class I.  
3. **Evidence package:** Complete Technical Documentation (Annex II), up‑to‑date CER (Article 61 Annex XIV Part A), a PMCF plan/report (Annex XIV Part B), PSUR (Art. 86) where applicable, and fully functional PMS system (Art. 83‑84).  
4. **Current gaps:** Intended use wording, detailed device description, risk‑management file, clinical data/equivalence justification, PMS/PMCF strategy, UDI registration details. These must be supplied before the NB can accept the dossier.  

**Escalation:** Any of the triggers listed in Section 6 should be raised to senior RA leadership immediately; unresolved items block the submission timeline.

---

### 8. Peer‑Review Prompt  

> *Colleague,* could you verify that our interpretation of the classification workflow (Article 51 + Annex VIII) aligns with the latest MDCG Manual version referenced (2023‑09 v2.1.1)? Also, please review the sufficiency of the identified clinical evidence gaps—especially whether a comparable CE‑marked predicate can be assumed without additional justification under Art. 61 MDR. Finally, assess if any jurisdiction‑specific requirements (e.g., Korean 의료기기법 §31 reporting) need separate handling beyond the EU framework.

--- 

*Prepared by Theo – EU MDR Regulatory Affairs Specialist.*

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

### kb-eval-20260723-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e3e29ddc12ec8317", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md", "source_hash": "9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e3e29ddc12ec8317`
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

> **Regulatory Draft – MDR Classification & Conformity Assessment Route**

---

### 1️⃣ Device Summary (as derived from the template)

| Item | Information Present in Source | Comments / Gap |
|------|------------------------------|----------------|
| **Manufacturer name** | Yes – placeholder `[회사명]` | Requires actual legal name. |
| **Authorized representative** | Yes – placeholder | Needs full name and address if manufacturer is outside the EU. |
| **Basic UDI‑DI** | Yes – placeholder “[Basic UDI‑DI — Annex VI Part C 기준]” | Must be allocated in EUDAMED before DoC signing. |
| **Product identification (name, trade name, model/Cat.#)** | Yes – placeholders | Real values required. |
| **Intended use** | Yes – placeholder “[의도된 사용 목적 — 간략 기재]” | Critical for classification; must be a clear, concise statement of the medical purpose. |
| **Signature block (date, name, function, signature)** | Present (Section 8) | Must be completed by an authorised signatory (e.g., CEO or QA Director). |
| **SRN (EUDAMED registration number)** | Placeholder “[EUDAMED SRN — 미취득 시 공백]” | Needs to be obtained prior to DoC issuance. |

> **Missing Information** – The template does not contain any technical description, mode of action, intended patient population, or risk‑related attributes. Without these the classification cannot be determined and the conformity route remains unknown.

---

### 2️⃣ Classification Approach (MDR 2017/745)

| Step | Requirement | Evidence Needed | Likelihood / Comment |
|------|-------------|-----------------|----------------------|
| **a) Identify intended purpose** | Precise wording of “intended use” in the DoC. | Text from Section 4 of the template (to be supplied). | *Missing – cannot apply classification rules.* |
| **b) Determine device category** | Is it active, invasive, software, measuring, etc.? | Technical description, principle of operation, energy source. | *Missing.* |
| **c) Apply relevant rule(s) from Annex VIII** (e.g., Rule 9‑17). | Choice depends on the answers in (a) & (b). | – | *Pending.* |
| **d) Assign Risk Class** | Result of step c. | – | *Pending.* |

> **Regulatory citation:** Classification rules are set out in **Annex VIII**, MDR 2017/745.  
> *(no specific identifier found in source — verify separately)*

---

### 3️⃣ Conformity Assessment Route (per device class)

| Device Class | Likely Annex for CE‑Marking* | Required Notified Body Involvement |
|--------------|-----------------------------|------------------------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration – no NB required. | None (Annex IV DoC only). |
| **Class I (sterile or measuring)** | **Annex IX** (QMS + technical file review) | NB must assess the QMS and part of the technical documentation. |
| **Class IIa / IIb / III** | **Annex IX** (full QMS & technical file assessment) – or **Annex X** (type‑examination) for devices where a type‑examination is mandatory (e.g., custom‑made, implantable active). | NB assessment of the complete technical documentation and/or type‑examination. |

> *The exact annex depends on the final risk class once classification is known.*

> **Regulatory citation:** Conformity assessment routes are defined in **Annex IX**, **Annex X**, and **Annex XI** of MDR 2017/745.  
> *(no specific identifier found in source — verify separately)*

---

### 4️⃣ Required Evidence Package (Technical Documentation)

| Element | Content Requirement | Source / Regulatory Basis |
|---------|--------------------|---------------------------|
| **a) Device description & specification** | Detailed description, diagrams, specifications, variants. | Annex II – Technical documentation. |
| **b) Intended purpose & labeling** | Clear statement, indications, contraindications, instructions for use (IFU). | Annex I §23 (labeling), Annex II. |
| **c) Design verification & validation** | Test reports, risk control verification, software validation if applicable. | Annex II; ISO 14971 for risk management; IEC 62304 for software. |
| **d) Clinical Evaluation Report (CER)** | Systematic review of clinical data, state‑of‑the‑art literature, benefit–risk analysis. | **Annex XIV Part A** (kept current under Art. 61). |
| **e) Post‑Market Surveillance (PMS) system** | PMS plan (Art. 84), PMS report/PSUR (Art. 85/86). | Art. 83, 84, 85, 86. |
| **f) Risk Management File** | Hazard analysis, risk evaluation, residual risk assessment, risk control measures. | Annex I (General Safety & Performance Requirements) implemented via ISO 14971. |
| **g) UDI‑DI registration** | Allocation and entry in EUDAMED (Annex VI Part C). | Annex VI. |
| **h) Declaration of Conformity** | Completed DoC (Annex IV) signed by authorised person, includes SRN, Basic UDI‑DI, product ID, intended use. | **Annex IV** – EU Declaration of Conformity. |
| **i) Quality Management System** | ISO 13485 certification (or equivalent) for classes requiring NB involvement. | Annex IX (QMS assessment). |

> **Regulatory citations:** The above items are directly derived from MDR Articles and Annexes as noted; the source excerpt only provides the DoC template layout, not the substantive regulatory references.  
> *(no specific identifier found in source — verify separately for each element)*

---

### 5️⃣ Risk Controls (Key Areas to Address)

| GSPR § | Typical Requirement | Control Measures Needed |
|--------|--------------------|--------------------------|
| **§ 16** – Protection against radiation | If device emits ionising or non‑ionising radiation, demonstrate compliance with limits. | Apply IEC 60601‑2‑54 / 28 / 44 as appropriate; perform dosimetry testing. |
| **§ 17** – Electronic programmable systems | For devices containing software/hardware that can be reprogrammed. | Follow IEC 62304 (software life‑cycle) and IEC 62366‑1 (usability). |
| **§ 18** – Active devices & connections | If device is active, show safe interaction with power sources and other equipment. | Conduct electrical safety testing per IEC 60601‑1; provide protection against excessive currents. |
| **§ 20** – Mechanical/thermal risks | Verify structural integrity, ergonomics. | Perform mechanical stress tests, thermal analysis. |
| **§ 22** – Use by lay persons | If intended for non‑professional use, demonstrate usability and safety. | Usability engineering file (IEC 62366‑1). |
| **§ 23** – Information supplied with the device | Clear IFU, labeling, warnings. | Draft comprehensive Instructions For Use, CE marking label, symbols per ISO 15223‑1.

> **Regulatory citation:** General Safety and Performance Requirements are set out in **Annex I**, §§ 16–23.  
> *(no specific identifier found in source — verify separately)*

---

### 6️⃣ Gaps & Missing Information (What must be supplied before a submission can proceed)

| Gap | Why it matters | Action Required |
|-----|----------------|-----------------|
| **Exact intended use** | Drives classification & clinical evaluation scope. | Provide concise, medically‑accurate statement. |
| **Technical description / mode of action** | Needed for risk analysis and to select the correct classification rule (Annex VIII). | Supply device architecture, energy source, patient contact points. |
| **Risk Management File (ISO 14971)** | Demonstrates compliance with GSPR § 16‑22. | Compile hazard analysis, risk control measures, residual risk evaluation. |
| **Clinical data** | Required for CER (Annex XIV Part A). | Gather pre‑market clinical investigation results or equivalence justification. |
| **PMS & PMCF plans** | Mandatory for classes IIa–III (Art. 84, Annex XIV Part B). | Define post‑market data collection strategy and schedule. |
| **EUDAMED SRN** | Must be listed on the DoC; without it the declaration is incomplete. | Register device in EUDAMED and obtain SRN. |
| **Authorized Representative details (if applicable)** | Required by MDR for non‑EU manufacturers. | Provide name, address, EU contact point. |
| **Signatory authority** | Declaration must be signed by a person with appropriate responsibility (e.g., CEO, QA Director). | Confirm signatory’s role and include date. |
| **UDI‑DI allocation** | Must be unique and registered in EUDAMED (Annex VI). | Apply for Basic UDI‑DI and embed on labeling & DoC. |

---

### 7️⃣ Human‑Escalation Triggers

| Trigger | Condition | Escalation Path |
|---------|-----------|-----------------|
| **Classification uncertainty** | Intended use or device description incomplete → cannot apply Annex VIII rule(s). | Notify Project Lead to obtain full intended‑use statement; if unavailable within 5 working days, raise to Regulatory Manager. |
| **Missing SRN / UDI‑DI** | DoC template contains blank placeholders. | Prompt Manufacturing/Regulatory affairs for EUDAMED registration; if not secured within 10 days, halt DoC finalisation. |
| **Absent clinical evidence** | No CER or justification of equivalence supplied. | Escalate to Clinical Evaluation Lead; schedule a dedicated clinical data collection plan. |
| **Risk Management File absent / incomplete** | No ISO 14971 file linked to the device. | Raise to Quality Manager for immediate compilation; if not delivered within 7 days, issue a non‑conformance record. |
> These triggers are designed to prevent submission of an incomplete or non‑compliant DoC to the Notified Body.

---

### 8️⃣ Peer Review Prompt

*“@RA‑Peer, please review the assumptions made in this draft, especially: (1) the inference that classification will follow Annex VIII once intended use is supplied; (2) completeness of the evidence checklist against MDR Articles/Annexes; and (3) any jurisdictional nuances that may affect devices destined for EU markets but manufactured outside the Union. Highlight any missing regulatory citations or steps that could cause a Notified Body query.”*

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

1. Chunk `1085205256397640486`

> 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` ---

2. Chunk `1141859994065237405`

> ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ───────────────────────────────────────────── 1. MANUFACTURER Company name : [회사명] SRN : [EUDAMED SRN — 미취득 시 공백] Address : [등록 사업장 주소] Authorised Representative: [EU 대리인명 및 주소 — 역외 제조사 해당 시] 2. SOLE RESPONSIBILITY STATEMENT This EU Declaration of Conformity is issued under the sole responsibility of the manufacturer named above. 3. BASIC UDI-DI [Basic UDI-DI — Annex VI Part C 기준] 4. PRODUCT IDENTIFICATION Product name : [제품명] Trade name : [상품명] Model / Cat.# : [모델 번호 / 카탈로그 번호] Intended use : [의도된 사용 목적 — 간략 기재] Photograph : [첨부...

### kb-eval-20260723-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "894386d2889e8a10", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `894386d2889e8a10`
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

> **Regulatory Draft – X‑ray Medical Device (Ionising Radiation)  
MDR 2017/745 – Classification & Conformity Assessment**

---

### 1. Primary Regulatory Determination  

| Item | Finding | Regulatory Basis |
|------|---------|------------------|
| **Device type** | Ionising‑radiation emitting equipment for medical diagnosis (X‑ray system). | — |
| **Applicable MDR rule** | **Rule 10** – active devices used for the diagnosis or monitoring of physiological processes and which emit ionising radiation. | *Annex VIII, Rule 10* |
| **Resulting class** | **Class IIb** (the minimum class for any X‑ray device that emits ionising radiation). | *Rule 10 → Class IIb*; source excerpt ①: “이온화 방사선 기기(X-ray)는 **Class IIb 이상** → NB 인증 필수.” |
| **Conformity‑assessment route** | **Annex IX** – full quality‑management‑system assessment together with the technical documentation by a Notified Body (NB). | *MDR Annex IX* (QMS + Technical Documentation) |
| **Alternative route** (if a type‑examination is also required) | **Annex X** may be used for a separate type‑examination, but the NB will still need to assess the QMS per Annex IX for Class IIb devices. | *MDR Annex X* (type‑examination) – optional adjunct |

---

### 2. Evidence Package Required by the Notified Body  

| # | Evidence / Deliverable | Core content (regulatory citation) |
|---|------------------------|------------------------------------|
| **1** | **Technical Documentation** (TD) | Annex II – device description, intended purpose, classification justification, design & manufacturing information, labeling (§23), GSPR compliance (Annex I §§1‑22). |
| **2** | **Risk Management File** | ISO 14971 + MDR Annex I §16–§20. Demonstrate controls for radiation exposure, electrical safety, software hazards, etc. |
| **3** | **Clinical Evaluation Report (CER)** | Annex XIV Part A – systematic SOTA literature review, clinical data, benefit‑risk analysis. |
| **4** | **Post‑Market Surveillance (PMS) Plan** | Art. 84 – description of PMS system, data collection, vigilance procedures. |
| **5** | **Periodic Safety Update Report (PSUR)** (starting after first market entry) | Art. 86(1)(a‑c); for Class IIb the PSUR must be updated **annually**. |
| **6** | **Labeling & IFU** | Annex I §23 – symbols, safety information, contraindications, radiation protection instructions. |
| **7** | **Performance / Safety Test Reports** (e.g., X‑ray output, beam quality) | IEC 60601‑2‑54 (radiography/radioscopy), IEC 60601‑2‑28 (tube assemblies). |
| **8** | **Software Validation Documentation** (if software is part of the device) | IEC 62304 lifecycle, IEC 62366‑1 usability. |
| **9** | **QMS Certification Scope** | Certificate issued under ISO 13485:2016; scope must cover Class IIb X‑ray devices and include all relevant processes. |
| **10** | **Notified Body Selection Dossier** (comparative NB matrix) | Source excerpt ②: “Notified Body 선정 자료 … Technical Documentation Assessment 보고서 … QMS Audit 관련 자료.” |

---

### 3. Gaps / Missing Information (to be obtained before NB submission)

1. **Exact Intended Use Statement** – anatomical region(s), clinical indications, patient population.  
2. **Classification rule justification** – explicit reference to Rule 10 and why the device is not covered by a lower‑risk rule.  
3. **Clinical data source list** – clinical investigations, post‑market clinical follow‑up (PMCF) studies, or literature that satisfies Annex XIV Part A.  
4. **SOTA literature review matrix** – latest peer‑reviewed publications (≤ 5 years).  
5. **PMCF Plan** – objectives, endpoints, follow‑up schedule; required under Annex XIV Part B.  
6. **Labeling draft** – full Instructions for Use (IFU) and safety labels for lay users (§22 if applicable).  
7. **List of applied harmonised standards & edition numbers** – e.g., IEC 60601‑2‑54:2020, IEC 62304:2006+A1:2015, ISO 14971:2019.  
8. **Radiation protection calculations** (dose limits, shielding) to demonstrate compliance with GSPR §16 and the Euratom Directive 2013/59/Euratom (if applicable).  
9. **Usability testing results** – especially for devices intended for use by non‑clinical personnel (§22).  

*Each missing item should be captured in a “Regulatory Gap Register” and escalated to the project lead for rapid closure.*

---

### 4. Key Risk Controls (linked to GSPR)

| GSPR § | Hazard | Primary Control(s) | Supporting Evidence |
|--------|--------|--------------------|---------------------|
| **§16** – Radiation protection | Excess patient/operator dose | - Beam‑output calibration per IEC 60601‑2‑54<br>- Automatic exposure control (AEC) algorithms validated<br>- Shielding design calculations (Euratom Directive) |
| **§17** – Electronic programmable systems | Software malfunction leading to incorrect exposure settings | - IEC 62304 compliant software lifecycle<br>- Fault tree analysis & failure mode effects analysis (FMEA) |
| **§18** – Active devices & connected accessories | Unsafe electrical connections or power failures | - IEC 60601‑1 safety testing, IEC 60601‑2‑54 specific tests |
| **§20** – Mechanical/thermal risks | Device overheating, mechanical impact on patient | - Thermal mapping, mechanical stress analysis, protective housing design |
| **§22** – Use by lay persons (if applicable) | Misuse leading to overexposure | - Usability engineering per IEC 62366‑1, clear pictograms and safety warnings in IFU |

All controls must be traceable to the risk management file (ISO 14971) and reflected in the technical documentation.

---

### 5. Notified Body Interaction Checklist  

| Step | Deliverable | NB Review Outcome |
|------|-------------|-------------------|
| **A** | Selection dossier (NB comparison matrix, contract & quote) – see source excerpt ②. | NB acceptance of chosen body and signed audit‑contract. |
| **B** | QMS Audit (ISO 13485) – scope includes Class IIb X‑ray devices. | Observation report → corrective action plan (if non‑conformities). |
| **C** | Technical Documentation Assessment Report (TDAR). | NB issues “Conformity assessment opinion” and CE marking certificate. |
| **D** | Post‑market surveillance reporting (annual PSUR) – Art. 86. | Ongoing compliance verification. |

---

### 6. Human‑Escalation Triggers  

| Trigger | When to Escalate | To Whom |
|---------|------------------|--------|
| **Missing Intended Use / Classification justification** | As soon as the draft TD lacks a clear statement or rule reference. | Project Lead & Senior RA. |
| **Insufficient Clinical Evidence** (no PMCF plan, lacking SOTA matrix) | Prior to CER finalisation. | Clinical Affairs Lead. |
| **Open Non‑conformities from QMS audit** | Any unresolved observation after the NB’s audit report deadline. | Quality Manager. |
| **Unresolved Radiation‑dose calculations** | If dose‑limit compliance cannot be demonstrated. | Safety Engineer / Radiology Expert. |
| **Deadline for PSUR submission approaching without draft** | Within 3 months of market launch. | Post‑Market Surveillance Coordinator. |
| **NB rejects any element of TD** | Immediate feedback from NB indicating missing or inadequate evidence. | Project Lead and Legal/Regulatory Compliance Officer. |

Escalations should be logged in the project’s risk‑register and accompanied by a mitigation action plan.

---

### 7. Reusable RA Judgment (Lesson Learned)

> **When an ionising‑radiation medical device is identified, MDR Rule 10 automatically places it in Class IIb; NB certification is therefore mandatory.** The conformity route must be Annex IX (QMS + TD assessment). Prior to any NB engagement the sponsor must provide a complete classification justification, a detailed intended‑use description, and a full clinical‑evaluation dossier that satisfies Annex XIV Part A. Absence of any of these items triggers immediate escalation.  

*Capture this judgment in the RA knowledge base for future X‑ray or other ionising‑radiation device projects.*

---

### 8. Peer‑Review Prompt  

> **@RA‑Peer:** Please challenge the assumptions made above, especially:  
> • Whether any parts of the device could be re‑classified under a lower rule (e.g., Rule 9) based on its functionality.  
> • The completeness of the listed standards – are additional harmonised standards required for specific X‑ray modalities (CT, fluoroscopy)?  
> • Potential gaps concerning Euratom Directive alignment and whether an additional national conformity assessment is needed in any EU Member State.  

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

1. Chunk `978896205875274621`

> ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수).

2. Chunk `296791090431458058`

> ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료

### kb-eval-20260723-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "0de278aaaee362d3", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `0de278aaaee362d3`
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

> **Regulatory Draft – MDR Technical Documentation (Annex II) – Preliminary Scope Assessment**

| # | Topic | Required Elements (per MDR) | Current Status & Gaps | Action / Evidence Needed | Regulatory citation |
|---|-------|-----------------------------|----------------------|--------------------------|---------------------|
| 1 | **Device description** (Section §1 of Annex II) | – Trade name, model, catalogue number<br>– Summary of the device’s intended purpose and mode(s) of action<br>– Diagram / exploded view showing main components | • Only a generic “product description” placeholder is present in the source table. No detailed narrative or nomenclature has been supplied. | • Draft a complete Device Description that maps each functional block to its role in achieving the intended medical purpose. | Annex II §1; no specific identifier needed beyond the framework reference |
| 2 | **Intended use / labeling** (Section §2) | – Full Intended Use statement (clinical indication, patient population, user profile)<br>– Labeling and IFU content outline (per GSPR §23) | • No explicit intended‑use text is available. The source only lists “라벨·IFU” linked to §2. | • Obtain the Manufacturer’s Intended Use claim; align with labeling draft that satisfies GSPR §23. | Annex II §2; GSPR §23 |
| 3 | **Classification & Conformity‑assessment route** | – Apply the appropriate Classification Rule (Annex VIII) based on intended purpose and mode of action.<br>– Select the conformity‑assessment procedure (Annex IX, X or XI). | • Intended purpose and mode of action are missing → classification cannot be determined. | • Once Intended Use is defined, run the rule matrix (e.g., Rule 9, 10, 11, 17 etc.) to allocate Class I–III.<br>• Choose the route: <br> ‑ **Annex IX** for QMS + technical file assessment (Class IIa/IIb/III),<br> ‑ **Annex X** for type‑examination (if applicable), or<br> ‑ **Annex XI** for production conformity verification (generally for Class I when a NB is not required). | Annex VIII (classification rules); Annex IX, X, XI (conformity routes) |
| 4 | **General Safety & Performance Requirements (GSPR) checklist** (Section §4) | – Completed GSPR matrix covering §§1‑23 of Annex I.<br>– Evidence of compliance for each requirement (e.g., test reports, risk analysis). | • Only a placeholder “GSPR Checklist” is shown; no populated matrix or supporting data. | • Populate the GSPR checklist with referenced evidence (e.g., performance testing for §16‑radiation, software validation for §17). | Annex II §4; Annex I (GSPRs) |
| 5 | **Risk Management** (Section §5) | – Risk Management File per ISO 14971 (risk analysis, evaluated controls, residual risk assessment).<br>– Linkage to design outputs and verification results. | • Source mentions “Risk Management File (ISO 14971)” but no actual file or traceability matrix is supplied. | • Compile a complete RMF; include risk control measures, benefit‑risk determination, and post‑market surveillance (PMS) considerations (Art. 83). | Annex II §5; ISO 14971 |
| 6 | **Verification & Validation** (Section §6) | – Verification reports confirming that design outputs meet inputs.<br>– Validation (including clinical validation) proving conformity to intended use.<br>– Software V&V if applicable (IEC 62304). | • “V&V Reports (DHF)” are referenced but no concrete reports exist in the current package. | • Generate verification protocols/results (bench, electrical safety, EMC, sterilisation, etc.).<br>• For devices with clinical claims, produce a Clinical Evaluation Report (CER) per Annex XIV Part A and, where required, a PMCF plan (Annex XIV Part B). | Annex II §6; Annex XIV Parts A & B |
| 7 | **Clinical Evidence** | – CER (Annex XIV Part A) that includes state‑of‑the‑art literature review, clinical data, and benefit–risk analysis.<br>– If the device is Class IIa/IIb/III, a PMCF plan/report must be prepared (Annex XIV Part B). | • No CER or PMCF documentation referenced. | • Conduct a systematic literature search; collect any existing clinical data (e.g., CE‑marked equivalents, post‑market surveillance, registry data).<br>• Draft the CER and decide whether a prospective PMCF study is required. | Annex XIV Part A & B |
| 8 | **Labels & IFU** (Section §2 / GSPR §23) | – Device label, packaging, and Instructions for Use in required languages.<br>– Compliance with IEC 60601‑1 labeling requirements where applicable. | • No concrete label/IFU drafts available. | • Produce draft label and IFU; perform usability validation (IEC 62366‑1). | Annex II §2; GSPR §23 |
| 9 | **Post‑Market Surveillance (PMS) system** | – PMS Plan (Art. 84), PMS Report (Art. 85 for Class I, Art. 86 for higher classes).<br>– Trend reporting (Art. 88). | • No PMS documentation identified. | • Define a PMS plan consistent with the device’s risk class; schedule PSURs (annual for IIb/III, biennial for IIa). | Art. 83‑86, 88 |
|10| **Declaration of Conformity & EU‑type examination** | – EU Declaration of Conformity (Annex IV) signed by the manufacturer.<br>– CE mark affixed according to Regulation (EU) 2017/745. | • Not yet prepared. | • Once technical documentation is complete and conformity assessment successful, draft the DoC and apply the CE marking. | Annex IV |

### Human‑Escalation Triggers

| Trigger | Reason for Escalation | Recommended Owner |
|---------|----------------------|-------------------|
| **Missing Intended Use / Mode of Action** | Classification cannot be performed; risk classification unknown → could lead to incorrect conformity route. | Product Development Lead & Regulatory Manager |
| **Device classified as Class III or a high‑risk active device (Rule 9/10/11)** | Requires Notified Body assessment under Annex IX and annual PSURs; higher regulatory scrutiny. | Senior RA / QMS Lead |
| **Absence of Clinical Evaluation Report for Class IIa‑III** | Non‑compliance with Annex XIV Part A → No CE marking possible. | Clinical Affairs & RA |
| **No PMS Plan (Art. 84) for devices >Class I** | Violates post‑market obligations; could trigger market surveillance actions. | Post‑Market Surveillance Lead |
| **Software component classified as a medical device (Rule 11)** without IEC 62304 lifecycle evidence | Software risk not demonstrated ⇒ non‑conformity with GSPR §17. | Software Development Lead & RA |
| **Labeling/IFU draft fails usability testing** | Potential for misuse; violation of GSPR §22/§23. | Usability Engineer & Regulatory Lead |

If any of the above triggers are identified during the documentation build, the issue must be escalated immediately to the designated owner for remediation before proceeding with Notified Body submission.

---

### Peer‑Review Prompt
> **To: RA Team – please review**  
> - Are there any additional MDR Annexes or Articles (e.g., specific § or sub‑paragraph) that should be referenced given the device type once its intended use is clarified?  
> - Does the current list of required evidence fully cover the GSPR checklist for a potential active medical device (Rule 9/10) or software (Rule 11)?  
> - Are there jurisdiction‑specific gaps not captured here (e.g., language requirements beyond English, national conformity‑assessment nuances)?

*Please challenge the assumptions above and highlight any missing source coverage or local regulatory considerations.*

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

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

## ra_kr

### kb-eval-20260723-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "caa50bd63f5609e3", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "f0c024377fc1b2e26c65ce2d0137ad3acfe458759690107440eee38bdd328736"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `caa50bd63f5609e3`
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

> **Regulatory Draft – Korean MFDS Pathway for the Digital Medical Software (AI‑enabled)  

---

### 1️⃣ Classification & Licensing Route  
| Item | Determination | Rationale / Source |
|------|---------------|--------------------|
| **Korean risk class** | **2등급 (Class II)** | Stated in source excerpt [1] – “국내 (MFDS) — 2등급 …” |
| **Regulatory route** | **허가 (Approval)** for Class II medical software | Under MFDS practice, Class II devices require a formal 허가 submission (not a simple 신고). |
| **Applicable MFDS guidance** | • “의료용 소프트웨어 허가·심사 가이드라인”  <br>• “디지털의료기기소프트웨어 허가·심사 가이드라인”  <br>• “독립형 SW 사용적합성 가이드라인”(if the product is a stand‑alone software) | All three are referenced in excerpt [1] as the basis for classification and submission requirements. No specific notice number is provided in the source; verify the exact 고시/공고 designation separately before final filing. |
| **Relevant statutory framework** | “디지털의료제품법” (effective 2025‑01‑24) – new law handling AI/SW‑based digital medical products, mandating change‑management plans and component performance verification. | Cited in excerpt [1]; the exact article/section number is not supplied. |

---

### 2️⃣ Required Evidentiary Dossiers  

| Evidence Category | Minimum Content | Source Reference |
|-------------------|----------------|------------------|
| **Technical Documentation (Design Dossier)** | • Device description, intended use, functional specifications <br>• Software architecture diagram, risk management file (ISO 14971) <br>• Verification & validation reports (including AI algorithm performance) <br>• Change‑management plan per the 2025 digital medical product law | Implicit from “변경관리계획, 구성요소 성능평가 등” mentioned in excerpt [1]. |
| **Software Usability / Suitability** | • Independent‑software‑use‑appropriateness assessment (if stand‑alone) as per the “독립형 SW 사용적합성 가이드라인”. | Excerpt [1]. |
| **Clinical Evaluation** | • Clinical performance data demonstrating safety and efficacy for intended AI functions; if local clinical data are required, a Korean cohort report. | Not explicitly listed in source – flag as missing information (see Section 4). |
| **Cybersecurity & SBOM** | • Security architecture description, penetration test results <br>• Software Bill of Materials (SBOM) per U.S. “Section 524B, Omnibus 2022” guidance is not mandatory in Korea but can be leveraged to meet MFDS expectations for AI/ML‑enabled software. | Cybersecurity references are from the FDA excerpt [2]; Korean MFDS does not yet prescribe SBOM, but referencing it demonstrates best practice and may facilitate review. |
| **Labeling & IFU** | • All labeling, instructions for use (IFU), and promotional material in Korean language; include risk information, intended user, and AI/ML limitation statements. | Standard MFDS requirement – no specific identifier supplied. |
| **Post‑Market Surveillance Plan** | • PMS activities per “시판후조사” obligations (e.g., periodic safety update reports). | Implicit MFDS post‑market requirement; not in source excerpt. |

---

### 3️⃣ Missing / Unclear Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Exact MFMF 고시/notice number for the “디지털의료기기소프트웨어 허가·심사 가이드라인”** | Needed to cite correctly in the submission dossier. | Retrieve latest 고시 reference from MFDS website or official gazette. |
| **Whether the software is classified as *독립형* (stand‑alone) vs. embedded** | Determines applicability of the “독립형 SW 사용적합성 가이드라인”. | Clarify product architecture; if stand‑alone, prepare additional suitability evidence. |
| **Local Korean clinical performance data** | MFDS may require domestic clinical evidence for AI algorithms that impact diagnostic decisions. | Conduct a feasibility study or collect retrospective Korean patient data; document justification if foreign data are used under mutual acceptance provisions (see note below). |
| **Exact article/section of the 2025 “디지털의료제품법” governing change‑management** | Required to align the Change Management Plan with statutory language. | Locate the specific 조/항 in the law text; cite it in the dossier. |
| **Risk classification for AI/ML lifecycle (predetermined change control plan)** | FDA guidance on PCCP is mentioned in excerpt [2]; Korean MFDS has a parallel expectation under the new digital medical product law. | Prepare a predefined change‑control strategy and map it to MFDS expectations; reference the law rather than the FDA document. |

---

### 4️⃣ Core Risk Controls (to be documented)  

| Control | Description | Alignment with MFDS guidance |
|--------|-------------|-------------------------------|
| **Software Safety & Reliability** | Unit, integration, system testing; verification of AI algorithm against ground‑truth datasets. | Covered by “구성요소 성능평가” in the 2025 law (excerpt [1]). |
| **Cybersecurity Hardening** | Secure coding practices, vulnerability scanning, authentication controls, SBOM for traceability. | While SBOM is a U.S. requirement (excerpt [2]), presenting it aligns with MFDS’s increasing focus on cyber risk for digital devices. |
| **Human Factors / Usability Engineering** | Conduct formative and summative usability tests with Korean end‑users; document UI/UX risk mitigations. | Implicit in “사용적합성 가이드라인”. |
| **Change Management (Predetermined Change Control Plan)** | Define allowable software updates, monitoring of AI performance drift, and submission triggers for major changes. | Required by the 2025 digital medical product law (“변경관리계획”). |
| **Post‑Market Monitoring** | Real‑world data collection plan, adverse event reporting system, periodic safety update reports in Korean. | Standard MFDS post‑market surveillance (시판후조사). |

---

### 5️⃣ Citations  

| Category | Citation Detail |
|----------|-----------------|
| **Classification rule** | “국내 (MFDS) — 2등급 …” – source [1] |
| **Guideline references** | “의료용 소프트웨어 허가·심사 가이드라인, 디지털의료기기소프트웨어 허가·심사 가이드라인” – source [1] |
| **Digital medical product law** | 「디지털의료제품법」 2025‑01‑24 시행 – source [1] |
| **Independent software suitability guideline** | “독립형 SW 사용적합성 가이드라인” – source [1] |
| **FDA product code & cybersecurity notes (for reference only)** | FDA Class II product codes LLZ/QIH/QDQ, 510(k) requirement, SBOM legal duty (Section 524B), PCCP guidance – source [2] |

*No specific MFDS 고시/notice number or article/section was supplied in the excerpts; those identifiers must be verified separately.*

---

### 6️⃣ Human‑Escalation Triggers  

| Trigger | Situation | Action Required |
|--------|-----------|-----------------|
| **Unclear regulatory instrument number** | When the exact 고시/notice identifier for the software approval guideline cannot be located. | RA lead to retrieve official MFDS 고시 number and update submission checklist before dossier finalization. |
| **Ambiguity on stand‑alone vs. embedded status** | Product architecture not definitively classified. | Engineering team to confirm classification; if stand‑alone, invoke “독립형 SW 사용적합성 가이드라인” compliance. |
| **Insufficient Korean clinical data** | FDA/CE evidence only; MFDS reviewer requests local performance data. | Initiate rapid Korean pilot study or request conditional acceptance based on foreign data under mutual acceptance provisions (MAD) – document justification and seek pre‑meeting with MFDS. |
| **Change‑Management plan misalignment** | Drafted plan does not reference the specific article of the 2025 law. | Legal/RA to locate exact 조/항, revise plan, and obtain internal sign‑off before submission. |
| **Cybersecurity evidence gap** | SBOM or security testing results missing for AI components. | Security team to perform required assessments; incorporate findings into technical dossier. |

When any of the above triggers occur, the responsible RA should raise a formal issue in the project’s risk register and request senior review before proceeding.

---

### 7️⃣ Peer‑Review Prompt  

> **@RA‑Peer:** Please review this draft for (a) completeness of Korean‐specific evidence requirements, (b) whether any additional MFDS notices or statutes (e.g., specific 조/항 of the 디지털의료제품법) have been omitted, and (c) any gaps in aligning AI/ML lifecycle controls with Korean expectations. Highlight any assumptions that need validation or sources we should retrieve to replace the “verify separately” placeholders.

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

### kb-eval-20260723-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "eb188d0bad15091e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `eb188d0bad15091e`
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

> **Regulatory Draft – MF DS Classification & Licensing Route (Digital‑Medical Software)**  

---

### 1. Preliminary Device Assessment  
| Item | Comment |
|------|---------|
| **Device type** | Software‑only digital medical device (no hardware). |
| **Intended use / claim** | *Not provided in source* – must be defined to apply MFDS risk‑classification rules (e.g., “diagnostic assistance”, “monitoring”, “therapy”). |
| **Regulatory category** | Determined by MFDS “디지털의료제품법 시행규칙” (Digital Medical Device Enforcement Rules). The device will fall into one of the MFDS classes I–IV based on intended use and risk.  |

> **Citation** – Classification basis: *디지털의료제품법 시행규칙* (see Source [1]).

---

### 2. Selected Submission Route  

| MFDS Pathway | When applicable |
|--------------|-----------------|
| **허가 (Approval)** | Class III‑IV devices or any device requiring clinical evidence. |
| **신고 (Notification)** | Class I‑II devices that do not need pre‑market safety/clinical data beyond software documentation. |
| **시험·인증** | If the software is a “digital health product” subject to the MFDS digital‑medical‑device testing guidelines, a separate performance test may be required before submission. |

*The exact route must be confirmed once the intended use and risk class are clarified.*

---

### 3. Core Evidentiary Package (per MFDS checklist)  

| Evidence | Requirement (mandatory/optional) | Source citation |
|----------|----------------------------------|-----------------|
| **Software version, build number & release date** | ✅ Mandatory | 디지털의료제품법 시행규칙 (Source [1]) |
| **Software update method & schedule** | ✅ Mandatory | MFDS SW 가이드라인 (Source [1]); *no specific identifier found in source – verify separately* |
| **Minimum / recommended system requirements (OS, CPU, RAM, storage, display resolution, network)** | ✅ Mandatory | MFDS SW 가이드라인 (Source [1]); *no specific identifier found in source – verify separately* |
| **List of compatible medical devices & interface specifications** | ✅ Mandatory | — (Source [1]; item S‑4) |
| **Data input/output formats (e.g., DICOM, HL7)** | ✅ Mandatory | — (Source [1]; item S‑5) |
| **Cybersecurity configuration guidelines (password policy, network segregation, access rights)** | ✅ Mandatory | MFDS 사이버보안 가이드라인 2025.01 (Source [1]) |
| **Security‑patch application procedure & responsible party** | ✅ Mandatory | MFDS 사이버보안 가이드라인 2025.01 (Source [1]) |
| **Known residual cybersecurity risks & mitigation plan** | ✅ Mandatory | MFDS 사이버보안 가이드라인 2025.01 (Source [1]) |
| **Data backup & recovery procedures** | ✅ Mandatory | — (Source [1]; item S‑9) |
| **System log management method** | ⚠️ Recommended | MFDS 사이버보건 가이드라인 (Source [1]) |
| **AI/ML specific documentation** *(if applicable)* | Not detailed in source – must be added per “디지털의료기기 특화 표시기재 요건 체크리스트” | Source [2] indicates additional items beyond the general checklist. |
| **Labeling / IFU (Korean language) required elements** | Mandatory for all digital medical devices; see MFDS Digital‑Medical‑Device Labeling Checklist (referenced in Source [2]) | No specific instrument number supplied – verify separately. |
| **KGMP certification** *(only if hardware is involved or software is classified as Class III/IV)* | May be required; not covered in the excerpts. | — |

---

### 4. Missing Information & Gap Analysis  

| Gap | Why it matters / impact on submission |
|-----|----------------------------------------|
| **Precise intended use and clinical claim** | Determines risk class and whether clinical data are needed (e.g., performance evaluation, safety‑efficacy study). |
| **Clinical evidence (if Class II‑IV)** | Required for 허가; absent → cannot proceed with approval. |
| **Detailed AI/ML documentation (training data, algorithm change management, explainability)** | Needed if the product uses AI/ML; MFDS has separate “AI/ML 디지털의료기기” guidance. |
| **Korean language labeling & IFU content checklist** | Mandatory for market entry; must include warnings, contraindications, user instructions in Korean. |
| **KGMP facility certification (if applicable)** | Required for manufacturing of hardware or software that is part of a Class III/IV device. |
| **Exact references to MFDS “SW 가이드라인” and “디지털의료제품법 시행규칙” documents** (e.g., notice number, revision date) | The source only names the guidelines; precise document edition should be cited in the submission dossier. |
| **Post‑market surveillance plan** | Required for 허가 submissions; not mentioned in excerpts. |
| **System log management (recommended item S‑10)** – decision whether to adopt as mandatory or keep as recommendation. |

---

### 5. Core Risk Controls (derived from checklist)  

1. **Version control & traceability** – capture build number, release date, and change logs.  
2. **Secure update mechanism** – authenticated, signed patches; defined schedule.  
3. **Minimum system specifications** – ensure performance limits are met on all supported platforms.  
4. **Interface validation** – document compatible medical device list & data exchange standards (DICOM/HL7).  
5. **Cybersecurity safeguards** – password policies, network segmentation, role‑based access control as per MFDS 사이버보안 가이드라인 2025.01.  
6. **Patch management responsibility matrix** – clear owner for security updates.  
7. **Residual risk mitigation** – documented residual risks with contingency procedures (Source [1] S‑8).  
8. **Backup & recovery** – regular data backups, tested restoration process (S‑9).  

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Unclear risk class after intended use definition** | Escalate to senior regulatory lead for classification decision; may need MFDS pre‑submission inquiry. |
| **Clinical data required but not available** | Pause submission; initiate clinical study plan or seek existing foreign CE/FDA data that can be leveraged (subject to MFDS mutual‑acceptance rules). |
| **AI/ML components present without documented algorithm change management** | Escalate to AI/ML compliance specialist; prepare additional documentation per MFDS AI/ML guidance. |
| **Korean labeling elements missing or incomplete** | Trigger immediate revision of IFU; involve Korean language expert. |
| **KGMP certification gap for hardware‑integrated software** | Escalate to manufacturing QA for facility audit and certification. |
| **Cybersecurity residual risk deemed “high” without feasible mitigation** | Escalate to product management/CTO for redesign or risk acceptance process (including possible MFDS safety review). |
| **Any citation in the dossier refers only to a guideline name with no version/notice number** | Flag for verification; obtain exact document reference before final submission. |

---

### 7. Summary Judgment  

*Based on the supplied MFDS checklist items, the digital‑medical software must compile a comprehensive technical file covering software versioning, update policy, system requirements, interface specifications, cybersecurity controls, data backup/recovery, and labeling in Korean. The ultimate classification (and thus whether a 허가 or 신고 route is required) hinges on the precise intended use and associated risk level; this information is currently missing.*  

**Next steps:**  
1. Capture the device’s intended use and claim.  
2. Map the claim to MFDS risk‑classification rules (디지털의료제품법 시행규칙).  
3. Determine if clinical evidence or AI/ML supplemental documentation is needed.  
4. Gather the exact versions of the referenced MFDS guidelines (SW 가이드라인, 사이버보안 가이드라인 2025.01) and obtain a Korean‑language IFU checklist per Source [2].  

---

### 8. Peer‑Review Prompt  

> **Colleague, could you review:**
> - Whether any additional MFDS “digital medical device” labeling items from the “특화 표시기재 요건 체크리스트” (Source [2]) have been omitted here?
> - If our assumption that a clinical study may be required for Class II‑IV devices aligns with recent MFDS notice expansions on foreign clinical data acceptance.
> - Any jurisdiction‑specific gaps, especially regarding KGMP applicability to software‑only products.  

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

1. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

2. Chunk `124386539616979555`

> ## 3. 디지털의료기기 특화 표시기재 요건 체크리스트 > 일반 의료기기 표시기재 필수사항(→ IFU_필수요소_3지역_비교.md 참조)에 **추가**되는 항목

### kb-eval-20260723-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "be6f64cd81f77320", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `be6f64cd81f77320`
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

> **Regulatory Draft – Digital‑Medical Software (GUI SW) Under MFDS**

---

### 1. Applicable MFMF Regulatory Instruments  

| Topic | Source Instrument | Identifier (as given in source) | Effective / Issue Date |
|-------|-------------------|----------------------------------|------------------------|
| Classification & grading of digital medical products | “디지털의료제품의 분류 및 등급 지정 등에 관한 규정” | **제2025‑23호** | 2025‑04‑07 |
| Licensing, certification, notification and review procedures (including GUI SW) | “디지털의료제품 허가·인증·신고·심사·평가 등에 관한 규정” | **제2025‑25호** | 2025‑04‑15 |
| Digital GMP requirements (8 device‑type groups, AI/ML included) – still to be published | “디지털 의료기기 제조 및 품질관리 기준 (디지털 GMP)” | *별도 고시* (no specific number in source) | slated for 2025 (see monitoring point) |
| Revised implementation rules of the Digital‑Medical‑Device Act | “디지털의료제품법 시행규칙 개정 (총리령 제2088호)” | **총리령 제2088호** | 2026‑01‑23 |

*No other instrument numbers appear in the supplied excerpts; any further identifier must be verified from the official Gazette.*

---

### 2. Classification & Submission Route  

| Step | Action | Basis |
|------|--------|-------|
| **a) Determine class** – Apply the classification matrix of **제2025‑23호** (e.g., Class I, II, III based on risk level, invasiveness, and data‑driven decision impact). | The product is a GUI software that provides medical information but does not execute autonomous therapeutic decisions. Preliminary assessment places it in **Class II** (non‑invasive, moderate risk) – subject to MFDS **허가** (approval), not just 신고 (notification). | 디지털의료제품 허가·인증·신고·심사·평가 규정 (**제2025‑25호**) requires 허가 for Class II/III devices. |
| **b) Select licensing pathway** – File a **허가 신청** (full approval) with MFMF, using the submission format prescribed in **제2025‑25호**. | GUI SW falls under the “software medical device” category of that notice; therefore it is not eligible for the simplified 신고 route. | Same as above. |

---

### 3. Required Evidence Package  

| Category | Specific Items (Korean regulatory language) | Reference |
|----------|---------------------------------------------|-----------|
| **Technical Documentation** (per Annex II of MFDS 규정) | • Device description, intended use (in Korean) <br>• System architecture diagram <br>• Software Bill of Materials <br>• Version control & change‑management records | Framework: ISO 13485; Korean rule – no explicit identifier needed. |
| **Risk Management** | • ISO 14971‑based risk analysis (risk identification, evaluation, controls) <br>• Residual risk justification in Korean | Framework reference only. |
| **Software Development Lifecycle** | • IEC 62304 compliance evidence (development plan, verification & validation protocols, test reports) <br>• Cybersecurity measures per MFDS digital‑GMP guidance (once published) | IEC 62304; future Digital GMP notice (no identifier). |
| **Clinical Evaluation** | • Clinical performance data or literature supporting intended use <br>• If foreign CER is used, it must be accepted under the latest MFDS amendment (check for any recent “mutual acceptance” notice – not present in current source) | No specific MFDS notice cited; verify if a later “foreign CER acceptance” notice exists. |
| **Labeling & IFU** | • Korean‑language labeling, package insert, and user manual meeting the “Korean medical device labeling standards.” <br>• QR code or URL for post‑market updates (if applicable) | Framework: MFDS labeling guidelines (general). |
| **GMP Compliance** | • Proof of compliance with Digital GMP requirements for the relevant device type (type 2 – software). Until the separate 고시 is issued, reference “디지털 의료기기 제조 및 품질관리 기준” and note pending final details. | 별도 고시 – no number supplied. |
| **Regulatory Fees & Forms** | • Completed MFDS 허가 신청서 (Form A) <br>• Fee payment receipt | Standard MFDS procedure (no specific identifier). |

---

### 4. Missing Information / Gaps  

1. **Exact Intended Use Statement in Korean** – needed to drive classification and clinical evaluation scope.  
2. **Final Digital GMP 고시 details** – the forthcoming notice (2025) is still under verification; until then required GMP evidence may be provisional.  
3. **Foreign Clinical Evaluation Report acceptance** – no current MFDS notice on mutual acceptance of foreign CERs is present in source; confirmation required before using FDA 510(k) or EU CE data.  
4. **Cybersecurity Controls** – specific Korean requirements (e.g., “디지털 의료기기 사이버보안 가이드라인”) are not listed in the excerpt; obtain latest guidance.  
5. **Post‑market Surveillance Plan** – MFDS requires a PMS plan aligned with the device class; details absent from source.

---

### 5. Risk Controls & Mitigations  

| Hazard | Control (as per Korean regulation) | Supporting Standard |
|--------|-----------------------------------|---------------------|
| Incorrect display of clinical data | UI/UX verification, colour‑coding, mandatory warning messages in Korean | IEC 62304, ISO 14971 |
| Unauthorized software modification | Digital signature & integrity checks; restricted admin access | MFDS 디지털 GMP (once published) |
| Cyber attack leading to data breach | Encryption of data at rest/transit; regular vulnerability scanning | Korean cyber‑security guideline for medical devices (if any) |
| Residual risk exceeding acceptability | Perform benefit‑risk analysis, obtain expert panel review | ISO 14971 |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Action Required | Escalation Level |
|-------------------|-----------------|------------------|
| **Classification ambiguity** (e.g., risk analysis suggests Class I but intended use includes decision support) | Convene internal classification board; seek MFDS pre‑submission consultation. | Senior RA Lead |
| **Pending Digital GMP 고시 not yet finalized** and the submission deadline is approaching | Pause submission; request provisional compliance statement from MFDS or defer to next review cycle. | Project Manager / Regulatory Affairs Director |
| **Foreign clinical evidence being considered** without a confirming MFDS notice of mutual acceptance | Obtain legal counsel; possibly generate Korean clinical data before filing. | Clinical Development Lead |
| **Critical labeling discrepancy identified in Korean translation** | Immediate correction, re‑review by language specialist, flag to project lead. | QA Manager |
| **Cybersecurity vulnerability discovered after draft submission** | Issue a risk‑based amendment request to MFDS; notify affected users per PMS plan. | Post‑Market Surveillance Team |

---

### 7. Peer‑Review Prompt  

*“Please review the above regulatory judgment for any overlooked Korean‑specific obligations, especially regarding (a) the status of the Digital GMP 고시 and its impact on the required evidence, (b) potential MFDS notices that might now accept foreign clinical evaluation reports, and (c) the adequacy of the risk‑control mapping to current Korean cybersecurity guidance. Highlight any assumptions that need additional source verification.”*

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

### kb-eval-20260723-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "943f5314e1d782b1", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "5f0192e5896bd583833f41c673027bfe34b52793e1679d1f9dc751b5f77320c3"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `943f5314e1d782b1`
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

> **Regulatory Draft – MFDS Classification & Licensing Route for an X‑ray Imaging System (Domestic Market)**  

---

### 1. Governing Framework  
| Element | Korean legal source (framework) |
|---------|--------------------------------|
| Primary legislation | **Medical Device Act (의료기기법)** |
| Implementing decree | **Medical Device Enforcement Decree (시행령, 대통령령)** |
| Detailed rules | **Medical Device Enforcement Regulation (시행규칙, 총리령)** |
| MFDS notices that define device items & classes | 「**의료기기 품목 및 품목별 등급에 관한 규정**」 |
| MFDS notice governing approval/notification procedures | 「**의료기기 허가·신고·심사 등에 관한 규정**」 |
| MFDS GMP inspection regulation | 「**의료기기 GMP 심사·평가 등에 관한 규정**」 |

*No specific 고시 (notice) or article numbers were supplied in the source excerpts; those identifiers must be verified separately if required for submission documents.*

---

### 2. Device Classification (K‑Class)

| Step | Reasoning |
|------|-----------|
| **Reference** | The MFDS “품목 및 등급 규정” classifies radiological equipment (X‑ray generators, diagnostic X‑ray systems) as **K‑Class III** devices because they present a high level of risk to patients and operators. |
| **Result** | The device falls under **K‑Class III**, which mandates **허가 (approval)** rather than simple 신고 (notification). |

*Note: Exact classification must be cross‑checked against the current “품목 및 등급 규정” table; if a newer amendment re‑grades certain X‑ray sub‑categories, that would alter the route.*

---

### 3. MFDS Submission Route  

| Requirement | Details |
|-------------|---------|
| **Submission type** | **허가 (approval)** – full technical dossier submitted to MFDS under the “의료기기 허가·심사” process. |
| **Application form** | MFDS 허가 신청서 (electronic submission via HIRA/MFDS portal). |
| **Review schedule** | Standard review period for Class III devices is up to 6 months, extendable if additional data are requested. |

---

### 4. Required Evidence Package  

| Category | Specific items (Korean‑language emphasis) |
|----------|-------------------------------------------|
| **Device Description** | Technical specifications, intended use statement, list of accessories, diagrams with Korean labeling. |
| **Design & Manufacturing** | ISO 13485:2016 quality‑management system certificate; **KGMP** facility certification (MFDS GMP 심사·평가 규정). |
| **Risk Management** | Full ISO 14971 risk‑management file, including hazard analysis and risk control measures, with residues justified in Korean. |
| **Non‑clinical Safety Data** | GLP‑compliant biocompatibility tests, radiation safety testing per IEC 60601‑2‑44 (or newer edition). MFDS currently accepts foreign non‑clinical data under the OECD **Mutual Acceptance of Data (MAD)** framework – only for GLP safety studies. |
| **Clinical Evaluation** | • Local clinical study report *unless* a foreign Clinical Evaluation Report (CER) is accepted under the latest MFDS notice expanding foreign clinical evidence acceptance (specific notice number not provided in source).  <br>• If foreign CER is used, it must be translated into Korean and include a bridge analysis to Korean use conditions. |
| **Labeling & IFU** | All labeling, packaging artwork, and Instructions for Use (IFU) must be in **Korean**; include warnings, contraindications, and operator safety information per MFDS labeling guideline. |
| **Software / Cybersecurity (if applicable)** | IEC 62304 software life‑cycle documentation; security risk assessment per Korean guidance on medical device cybersecurity. |
| **Performance Testing** | Bench testing results demonstrating compliance with relevant performance standards (e.g., IEC 60601‑2‑44, IEC 62471 for photobiological safety). |
| **Post‑Market Surveillance Plan** | Outline of 시판후조사 activities, adverse event reporting procedure, and field safety corrective action (FSCA) process. |

*No specific MFDS 고시 or article numbers were extracted from the source; those citations must be added after verification.*

---

### 5. Identified Information Gaps  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended‑use description** (clinical indication, patient population) | Determines classification finer points and clinical evidence scope. | Obtain from product development team; draft Korean wording. |
| **Predicate device or foreign clearance data** (e.g., FDA 510(k), CE mark) | May support acceptance of foreign CER under MFDS’s expanded scope. | Collect all foreign regulatory dossiers and translate key sections. |
| **KGMP certification status of the manufacturing site** | Mandatory for Class III approval. | Confirm current KGMP audit report; schedule re‑audit if expired. |
| **Korean labeling artwork** | Required at submission; non‑compliance leads to rejection. | Prepare draft labels/IFU in Korean and submit for internal review. |
| **Local clinical trial data or justification for exemption** | MFDS may demand a Korean clinical study unless waiver criteria are met. | Conduct gap analysis against MFDS “clinical evaluation” requirements; plan trial if needed. |
| **Reference to the specific MFDS notice that permits foreign CER** | Needed to explicitly cite regulatory basis in the dossier. | Search MFDS 고시 database (post‑2026) for the relevant notice number and article; record it. |

---

### 6. Core Risk Controls (to be documented in the Technical File)

1. **Radiation dose management** – automatic exposure control, dose‑area product monitoring, compliance with IEC 60601‑2‑44 limits.  
2. **Operator safety interlocks** – door sensors, emergency stop, shielding verification.  
3. **Electrical safety** – adherence to IEC 60601‑1 requirements (leakage current, insulation).  
4. **Software validation** – unit, integration, system testing per IEC 62304; cybersecurity hardening.  
5. **User training program** – Korean language training modules and competency assessments.  

---

### 7. Human‑Escalation Triggers  

| Trigger | Escalation to |
|--------|----------------|
| Uncertainty about **K‑Class** (e.g., device variant not listed in current “품목 및 등급 규정”) | Request a formal classification inquiry (MFDS 사전심사) before dossier preparation. |
| Absence of **KGMP certification** or pending audit findings | Pause submission; engage the manufacturing compliance team and schedule MFDS GMP inspection. |
| Requirement for **local clinical data** that cannot be generated within project timeline | Escalate to senior RA lead for risk‑based waiver request or consider market postponement. |
| Missing **specific MFDS 고시 number** that justifies use of foreign CER | Convene a regulatory liaison meeting with MFDS to obtain guidance and capture the precise notice reference. |
| Language compliance issues (labeling not fully Korean) flagged by internal QA | Halt filing; route to medical‑communications for translation and regulatory review. |

---

### 8. Peer Review Prompt  

> **Colleague, please challenge the assumptions above:**  
> - Have we correctly assumed a Class III designation for all X‑ray systems under the current “품목 및 등급 규정”? Could any sub‑type be Class II?  
> - Are there any recent MFDS notices (post‑2026) that expand foreign clinical evidence acceptance beyond what is captured here, and do they affect our need for a Korean trial?  
> - Have we omitted any mandatory Korean‑specific documentation (e.g., “의료기기 안전성정보제공서”) that would be required for Class III 허가?  
> Your feedback will help close any jurisdictional gaps.

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

### kb-eval-20260723-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-23", "decision_ref": "kb-eval-20260723-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "072d449c96fdd3f6", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `072d449c96fdd3f6`
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

> **Regulatory Draft – MFDS Classification & Licensing Route for a Digital Health Software‑Medical Device (SaMD)**  

---

### 1. Preliminary Determination of Device Class  
| Criterion | Observation from source | MFDS rule applied* | Tentative class |
|-----------|------------------------|--------------------|-----------------|
| Product type | “디지털의료기기” (digital medical device) – software‑only, potentially AI/ML driven GUI | MFDS ‘디지털의료제품법’ and the 2025 MFDS 디지털의료기기 가이드라인 (6종) define SaMD classification based on intended use, risk to patient, and level of clinical decision support. | **Class II** if the software provides diagnostic or therapeutic information that influences clinical decisions without direct actuation; **Class I** only if pure health‑information/fitness tracking.  

\*Framework reference – MFDS ‘디지털의료제품법 시행’ (2025‑01‑24) and MFDS 디지털의료기기 가이드라인 6종 (2025‑05‑07). No specific article or notice number is cited in the source excerpts; therefore no instance identifier is attached.

**Regulatory judgment:**  
- **If the software outputs diagnostic suggestions, risk level corresponds to Class II.**  
- **If it only records/monitors data without influencing clinical decisions, Class I may be appropriate.**  

*Human‑escalation trigger:* When intended use description is ambiguous or missing, a senior RA must confirm the classification before proceeding to the submission pathway.

---

### 2. Applicable Submission Route  
| Classification | MFDS pathway (Korean terminology) | Typical dossier components |
|----------------|-----------------------------------|----------------------------|
| Class I (low‑risk) | **신고** (notification) – “간이 허가·신고” | Summary of device description, Korean label/IFU, KGMP compliance statement. |
| Class II (moderate‑risk) | **허가** (full approval) – “제2류 의료기기 허가” | Full technical dossier: device description, risk management file, clinical evaluation (or exempt if foreign CER accepted), GMP compliance certificate, Korean labeling, post‑market surveillance plan. |

*Human‑escalation trigger:* If the device is borderline between Class I and II, a senior RA or regulatory affairs manager must decide whether to pursue 허가 (full approval) to avoid later re‑classification.

---

### 3. Required Evidence – Checklist  

| Evidence type | MFDS requirement (derived from guidelines) | Availability in current dossier | Gap / Action |
|---------------|--------------------------------------------|---------------------------------|--------------|
| **KGMP certification** | GMP 적합인정 절차 (GMP review → 현장조사 → 적합인정서, validity 3 years). NIDS listed as a possible GMP assessment body since 2025‑01‑24. | None reported. | Obtain KGMP certificate from an authorized agency (e.g., KTL, TÜV SÜD Korea, or NIDS). |
| **Risk Management** | ISO 14971 compliance; MFDS expects documented risk analysis and mitigation. | Not mentioned. | Prepare full Risk Management File (RMF) per ISO 14971. |
| **Clinical Evidence** | For Class II SaMD, either: (a) Korean clinical study, or (b) foreign Clinical Evaluation Report (CER) accepted under MFDS mutual‑acceptance policy for non‑clinical data **only**; clinical data still require local justification. The 2025‑05‑07 guideline emphasises AI/ML‑based GUI software needs specific clinical validation. | No clinical data cited. | Plan Korean pilot study or submit foreign CER with justification of relevance; identify any MFDS notice that permits limited reliance on foreign data (must be verified). |
| **Software Documentation** | Software Development Life Cycle (SDLC) documentation, verification/validation reports, cybersecurity assessment per MFDS guidance for digital health devices. | Not indicated. | Compile SDLC artifacts, validation summary, and cybersecurity plan. |
| **Labeling & IFU** | Korean language labeling mandatory; user manual must be in Korean and meet MFDS labeling requirements (e.g., device name, intended use, warnings). | No mention of Korean translation. | Produce Korean label and Instructions for Use (IFU); secure translation verification. |
| **Post‑Market Surveillance (PMS) Plan** | Mandatory PMS plan for Class II devices; includes 시판후조사 reporting obligations. | Not provided. | Draft PMS plan aligned with MFDS post‑market requirements. |

*Human‑escalation trigger:* Any missing mandatory evidence (KGMP, risk management, clinical data, Korean labeling) must be escalated to the project lead for resource allocation before dossier assembly.

---

### 4. Risk Controls Specific to Digital Health SaMD  

1. **Algorithm Transparency & Version Control** – Document algorithm logic, training data provenance, and maintain version‑control logs.  
2. **Cybersecurity Measures** – Implement encryption of stored/ transmitted patient data; conduct vulnerability assessments per MFDS digital‑medical‑device cybersecurity guide (2025 revision).  
3. **Usability Testing** – Conduct Human Factors Engineering (HFE) studies in Korean user population to verify safe UI interaction, especially for AI/ML‑based GUIs.  
4. **Fail‑Safe / Default Modes** – Define and test fallback behavior when the software encounters unexpected inputs or network loss.  
5. **Data Integrity & Traceability** – Ensure audit trails for data input/output per ISO 13485 requirements adapted to digital devices.

*Human‑escalation trigger:* If any of the above controls cannot be demonstrated (e.g., no cybersecurity assessment), senior engineering and RA must jointly decide on project continuation or redesign.

---

### 5. Citations  

| Item | Source citation (as appearing in provided excerpts) |
|------|----------------------------------------------------|
| GMP approval procedure (KGMP) | “GMP 적합인정 절차 … 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요)” – Chunk 1078228256164017760 |
| NIDS involvement in digital‑medical‑device GMP assessment | “디지털의료기기: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행” – Chunk 1078228256164017760 |
| Recent regulatory changes (2025–2026) – SaMD classification & AI/ML requirements | Table under **7. 2025~2026 주요 규제 변경사항** – Chunk 1121184088796802935 |
| MFDS digital‑medical‑device guideline issuance dates | Same table, rows for 2025‑01‑24 (디지털의료제품법 시행) and 2025‑05‑07 (가이드라인 6종 제·개정) – Chunk 1121184088796802935 |

*No instance identifiers (e.g., 고시 번호, 조/항) were present in the source; therefore none are listed.*

---

### 6. Human‑Escalation Triggers Summary  

| Situation | Trigger Condition | Escalation Path |
|-----------|-------------------|-----------------|
| Unclear device classification (Class I vs II) | Ambiguous intended use or risk description | RA Manager → Clinical/Regulatory Strategy meeting |
| Missing KGMP certificate | No GMP approval evidence available | Quality Assurance Lead to initiate certification process |
| Absence of clinical/evidence data | No local study or acceptable foreign CER | Project Sponsor / Clinical Affairs for trial planning |
| Korean labeling not prepared | IFU/label only in English | Translation team lead + RA sign‑off |
| Incomplete risk management file | ISO 14971 RMF not drafted | Senior QA Engineer & RA to develop RMF ASAP |
| Cybersecurity assessment lacking | No documented security controls | IT Security Lead with RA to produce assessment report |

When any trigger fires, the responsible stakeholder must document the issue in the project’s regulatory tracker and seek senior approval before further dossier compilation.

---

### 7. Peer‑Review Prompt  

> **To a fellow RA colleague:** Please review this draft for (1) completeness of classification rationale given only the limited source excerpts, (2) any overlooked MFDS‑specific obligations (e.g., notification vs. permit filing nuances for digital SaMD), and (3) potential gaps in mapping foreign clinical evidence acceptance under current MFDS policy. Suggest additional Korean regulatory instruments that may need to be verified or cited once the full documentation set is available.

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
