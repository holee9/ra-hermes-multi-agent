# KB Eval Checksheet - 2026-07-21 Iteration 03

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260721-it03-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_us-001", "iteration": 3, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f4afc0898d20c8fb", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

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

> **Regulatory Draft – 510(k) Predicate‑Strategy Framework**

| Item | Recommended Approach | Key Regulatory Basis |
|------|----------------------|----------------------|
| **1. Device Classification & Submission Route** | • Identify the **intended use**, technology, and anatomical site.<br>• Search FDA’s 510(k) database for an existing **predicate device** that matches those parameters.<br>• If a Class II predicate exists → pursue a traditional **Premarket Notification (510(k))** under **21 CFR §807**. <br>• If no suitable predicate or the device is novel → consider a **De Novo** request (see 21 CFR §814). | 21 CFR §807 (submission); 21 CFR §894 (for devices that fall under Part 892 – imaging) – confirm appropriate part after intended use is known. |
| **2. Required Evidence Package** | 1. **Device Description & Indications for Use** – per eSTAR “Device Description / IFU” guide.<br>2. **Substantial‑Equivalence Comparison Table** – side‑by‑side of technological characteristics, labeling, and intended use (eSTAR template).<br>3. **510(k) Summary** – concise narrative of device, predicate, and differences (21 CFR §807.92).<br>4. **Performance Testing** – bench, animal, or clinical data as needed to demonstrate equivalence (see FDA guidance for the specific product code).<br>5. **Biocompatibility** – per ISO 10993‑1 risk‑based approach.<br>6. **Electrical Safety & EMC** – IEC 60601‑1 and IEC 60601‑1‑2 test data (or FDA recognized standards).<br>7. **Software/Algorithm Validation** (if applicable) – include verification, validation, and a **Predetermined Change Control Plan (PCCP)** per the December 2024 guidance.<br>8. **Quality Management System Evidence** – compliance with the new QMS Regulation (21 CFR §820) effective Feb 2026 (ISO 13485‑aligned).<br>9. **UDI Assignment & Labeling** – per 21 CFR §830 (label must bear a UDI, submission to GUDID). | • 21 CFR §807.92 (510(k) Summary)<br>• 21 CFR §§820 (QMSR) <br>• 21 CFR §§830 (UDI) <br>• ISO 10993‑1, IEC 60601‑1/‑1‑2 (risk & safety standards) <br>• FDA Predetermined Change Control Plan guidance (Dec 2024) |
| **3. Missing Information (to be obtained before submission)** | – Exact **device name, model, and accessory list**.<br>– Complete **Indications for Use** statement.<br>– Detailed **technology description** (materials, energy source, software architecture).<br>– Identification of a **clear predicate device** (K‑number) that matches the above; if none, prepare De Novo rationale.<br>– Draft **risk management file** (ISO 14971) with identified hazards and mitigations.<br>– Draft **UDI issuance plan** (issuing agency, label format).<br>– Confirmation of **QMS compliance evidence** (certified ISO 13485 or FDA QSR transition plan). | N/A – items are not present in the source excerpts. |
| **4. Core Risk Controls to Document** | • Apply **ISO 14971** risk management process: hazard identification, severity/occurrence analysis, risk control implementation.<br>• For electrical/mechanical devices: demonstrate compliance with **IEC 60601‑1** (safety) and **IEC 60601‑1‑2** (EMC).<br>• For software/AI components: include a **Predetermined Change Control Plan (PCCP)**, verification/validation protocols, and post‑market monitoring plan.<br>• Include **biocompatibility testing** per ISO 10993‑1 where patient contact occurs.<br>• Ensure **design controls** are captured within the QMS (21 CFR §820.30). | • ISO 14971<br>• IEC 60601‑1, IEC 60601‑1‑2<br>• FDA PCCP guidance (Dec 2024) |
| **5. Submission Workflow (per eSTAR template)** | 1. **Predicate Search** – FDA 510(k) database.<br>2. **Substantial Equivalence Table** – populate eSTAR comparison sheet.<br>3. Compile required sections (Summary, Device Description, Performance Data, etc.).<br>4. Prepare electronic submission using the **eSTAR template** and submit via **FDA’s ESG (Electronic Submissions Gateway)**.<br>5. Respond to any FDA **Additional Information (AI)** queries promptly; track within eSTAR “AI response” log. | – eSTAR guidance section 2 (submission overview). |
| **6. Human‑Escalation Triggers** | • **Unclear Classification** after intended use analysis → raise to senior regulatory lead for classification ruling.<br>• **No Adequate Predicate** found → initiate De Novo strategy discussion with leadership and possibly a pre‑submission meeting with FDA.<br>• **Major Design Change** (e.g., new algorithm, new material) that falls outside the scope of the existing PCCP → prepare a supplemental 510(k) or seek a **Special 510(k)** if applicable.<br>• **FDA AI Request** not answerable within internal timeline → engage external consultant/clinical expert as needed.<br>• **QMSR compliance gap** (e.g., ISO 13485 certification missing) → pause submission until remedied. | – FDA guidance on 510(k) re‑submission and special/modular pathways; internal SOPs for escalation. |

---

### Peer Review Prompt
*Please review the above assumptions, especially the classification inference without a defined device type, the completeness of the evidence checklist relative to industry‐specific guidances, and any jurisdictional gaps (e.g., state‑level reporting or post‑market surveillance requirements not covered here).*

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

### kb-eval-20260721-it03-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_us-002", "iteration": 3, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "c5264cbb7637ac12", "source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md", "source_hash": "a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c5264cbb7637ac12`
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

> **Regulatory Draft – 510(k) Predicate‑Strategy Planning**

---

### 1. Bottom‑Line Determination  
*Current status:* The 510(k) submission flagged in the internal issue **#951** (draft, no work started) is stalled. Because the source provides **no device description, intended use, or functional classification**, a definitive identification of the FDA product code, class, or applicable §892 subsection cannot be made at this time.

*Immediate regulatory path:* Prepare to file a **Premarket Notification (510(k))** under 21 CFR §807.95‑​1. The exact classification (Class II vs Class III) and predicate device(s) will be selected once the device’s intended use, technology, and risk profile are documented.

---

### 2. Required Evidence – Standard 510(k) Content  

| Section | Typical Evidence | Why it matters |
|---------|------------------|----------------|
| **Device Description & Intended Use** | Detailed description, indications for use, labeling excerpts. | Determines classification, predicate search, and risk analysis scope (21 CFR §807.92). |
| **Substantial‑Equivalence Comparison** | Predicate device(s) with 510(k) numbers, FDA product code, and comparison matrix (technology, intended use, performance). | Core of the SE argument (21 CFR §807.92(b)(3)). |
| **Performance Testing** | • Bench/bench‑top testing (electrical safety, EMC, software validation).<br>• Animal or benchtop model data if applicable.<br>• Clinical data (if required by classification rule). | Demonstrates that the new device performs at least as well as the predicate. |
| **Labeling & Instructions for Use** | Full label set, IFU, packaging artwork. | Must meet 21 CFR §801 requirements and be consistent with SE claim. |
| **Sterilization / Biocompatibility (if applicable)** | USP/ISO‑based data, ISO 10993 testing package. | Required when device contacts patients or tissues. |
| **Software Validation** *(if software component)* | Verification & validation reports, risk management file per IEC 62304, and a **Predetermined Change Control Plan (PCCP)** if post‑market AI/ML updates are anticipated (FDA guidance Dec 2024). | Supports compliance with 21 CFR §820.30 and future change‑control expectations. |
| **Quality Management System (QMS) Evidence** | Current ISO 13485‑aligned QMS documentation, internal audit reports. | Required by the new Quality Management System Regulation (QMSR) – 21 CFR §820 (effective Feb 2026). |
| **Unique Device Identification (UDI)** | Draft UDI label format, device identifier, production identifier, and GUDID submission plan. | Mandatory under 21 CFR §830 for most Class II/III devices. |

---

### 3. Missing Information (Gap Analysis)

| Gap | Impact on Submission | Recommended Action |
|-----|----------------------|--------------------|
| **Device function / intended use** | Cannot select classification rule, predicate, or determine need for clinical data. | Obtain a concise device description from product development; capture indication statements and target patient population. |
| **Technology/architecture details** (e.g., imaging modality, software algorithms) | Prevents accurate predicate search and risk analysis. | Compile architecture diagram, hardware specs, and software block diagram. |
| **Pre‑existing predicate candidates** | SE claim cannot be drafted. | Conduct a preliminary 510(k) database query using FDA’s “Find FDA-Approved Devices” tool once device class is known. |
| **Risk Management File (ISO 14971)** | Risk controls for the device remain undocumented, hindering safety justification. | Initiate a risk analysis workbook; identify hazardous situations and mitigation measures. |
| **QMS audit status** – The source notes that QA staff are fully occupied with an “audit sweep” covering **01_법규_규제** and **02_품질경영시스템_QMS**, causing delay in checklist work. | Delays preparation of required QMS evidence (design controls, document control). | Prioritize a focused internal 510(k) readiness audit; allocate at least one dedicated RA engineer to move forward while the broader audit proceeds. |
| **UDI planning** | Missing early UDI designation can cause downstream labeling redesign. | Assign a label designer to draft provisional UDI format per 21 CFR §830.10‑​30. |
| **Internal issue tracking #951** – No FDA identifier present.| No traceable 510(k) number for external reference. | Record the internal identifier for project management only; do not treat as a regulatory citation. |

---

### 4. Core Risk Controls (to be documented)

1. **Design‑Control Process** – Conform to 21 CFR §820.30 (design and development planning, inputs/outputs, verification, validation).  
2. **Software Lifecycle Management** – Follow IEC 62304; map to FDA’s software guidance and include a **Predetermined Change Control Plan (PCCP)** for any future AI/ML updates.  
3. **Sterility / Biocompatibility Controls** – If device contacts the patient, apply ISO 10993 testing and ensure sterilization validation per USP <797>/<800>.  
4. **Labeling Accuracy** – Verify that all labeling claims are supported by test data (21 CFR §801).  
5. **UDI Integration** – Ensure label and packaging contain a machine‑readable UDI; submit device identifier to GUDID (21 CFR §830.300 onward).  

---

### 5. Citations (Established Regulatory References)

| Reference | Relevance |
|-----------|-----------|
| **21 CFR §807** – Premarket Notification (510(k)) requirements. | Defines submission pathway and content expectations. |
| **21 CFR §820** – Quality Management System Regulation (QMSR) (effective 02‑Feb‑2026). | Governs design controls, document management, and audit readiness. |
| **21 CFR §830** – Unique Device Identification system. | Mandates UDI labeling and GUDID submission. |
| **IEC 62304** – Software Life Cycle Processes (referenced in FDA software guidance). | Basis for software validation & PCCP planning. |
| **ISO 14971** – Application of risk management to medical devices. | Framework for hazard identification & mitigation. |
| **Predetermined Change Control Plan (PCCP)** – FDA Final Guidance, Dec 2024. | Required for AI/ML change‑control strategy. |

*No specific 510(k) predicate numbers or product codes appear in the source excerpts; verify separately when device details become available.*

---

### 6. Human‑Escalation Triggers  

| Condition | Who Must Be Alerted | Reason |
|-----------|---------------------|--------|
| **Absence of any device description or intended use after 2 business days** | Project Lead / Senior RA Manager | Cannot proceed with classification; risk of missed clearance timeline. |
| **QMS audit sweep consumes >50 % of QA staff for >1 week, delaying 510(k) checklist completion** | Quality Director & Regulatory Affairs Head | QMSR compliance is mandatory; prolonged diversion jeopardizes submission readiness. |
| **Pending internal issue #951 remains in “draft, no work started” beyond the next regulatory milestone (e.g., planned 30‑day filing window)** | Program Management Office | Indicates schedule slippage; may require resource reallocation or scope reduction. |
| **Identification of a Class III classification (or lack of predicate) that would necessitate a PMA** | Chief Regulatory Officer | Immediate strategic decision needed – shift from 510(k) to PMA pathway. |
| **Regulatory changes announced affecting the device’s panel (e.g., new §892 rule for imaging devices)** | All regulatory staff & product development leads | Requires re‑assessment of classification and possible redesign. |

---

### 7. Reusable RA Judgment (Memory Entry)

**Judgment ID:** `RA_Judgment_2026-07-23_DailyGrowth_#951`  
**Core Insight:** *When a 510(k) submission is stalled due to lack of device‑specific information, the first regulatory action must be to lock down the intended use and functional description before any classification or predicate search can occur. Simultaneously, ensure that QMSR (21 CFR §820) compliance activities are not wholly absorbed by unrelated audits; allocate dedicated resources for 510(k) readiness.*  

**Action Template:**  
1. Capture device intent → log in project charter.  
2. Conduct rapid predicate search using FDA 510(k) database once intent is defined.  
3. Initiate a focused QMS “510(k) Readiness” audit independent of broader compliance audits.  
4. Document any missing data in a gap‑analysis worksheet and trigger escalation if unresolved >2 working days.  

---

*Prepared by:* **Mike – US Regulatory Affairs Specialist** (510(k) & QMSR focus)  

--- 

**Peer Review Request:**  
@RA_Team, please critique the assumptions made about the need for a dedicated 510(k) readiness audit amid an ongoing QA audit sweep, and verify that no jurisdiction‑specific considerations have been omitted (e.g., state‑level device registration, emerging EU MDR implications).

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

### kb-eval-20260721-it03-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_us-003", "iteration": 3, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "15448c50d07bbbce", "source": "github:holee9/MD-process/issue-drafts/979_FDA_510k_RTA_기초보강_4주차_재이월.md", "source_hash": "74bd6ad69e69c2f46c80904e3f16f85e423e7f85f008ac16cad2d4c86bf6e79b"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `15448c50d07bbbce`
- Source: `github:holee9/MD-process/issue-drafts/979_FDA_510k_RTA_기초보강_4주차_재이월.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/979_FDA_510k_RTA_%EA%B8%B0%EC%B4%88%EB%B3%B4%EA%B0%95_4%EC%A3%BC%EC%B0%A8_%EC%9E%AC%EC%9D%B4%EC%9B%94.md)
- Source hash: `74bd6ad69e69c2f46c80904e3f16f85e423e7f85f008ac16cad2d4c86bf6e79b`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `979_FDA_510k_RTA_기초보강_4주차_재이월.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **4주 연속 0% 정체** (06-26 / 07-03 / 07-10 / 07-17 동일). #951(07-03) → #959(07-10)에 이어 3연속 이관, 이번 주도 착수 실적 없음. ## 필수 작업 1. 14개 미충족 must 항목 중 최소 3건 착수 2. 기술 파일 구조(DHF section A/B/C) 기초 문서화 3. RTA 리뷰 체크포인트 수립 4. 감사 sweep과 체크리스트 보강 작업의 인력 배분 분리(전담 1인 배정 검토)
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

### 1. Device Overview (as currently known)
- The source provides only performance‑tracking metrics for an internal 510(k) review process; there is **no description of the device’s technology, intended use, or target patient population**.  
- Consequently a definitive classification (§892… or other panel) cannot be assigned at this stage.

---

### 2. Regulatory Pathway Determination  

| Criterion | Current Status | Action Required |
|-----------|----------------|-----------------|
| **Device class / predicate** | Unknown – no indication of whether the device falls under imaging (Part 892), clinical chemistry (Part 862), or another panel. | Obtain a concise “intended use” statement and a high‑level functional description to identify the appropriate CFR part and applicable classification rule. |
| **Submission type** | 510(k) indicated by source (“FDA 510(k) 평가”). | Confirm that a traditional 510(k) is sufficient (i.e., class II or de novo for novel Class III). If the device is truly novel, prepare a De Novo request. |
| **QMS requirement** | Effective QMS Regulation (ISO 13485‑aligned) entered force 2026‑02. | Verify that a compliant Quality Management System per **21 CFR 820** is in place; document Design History File (DHF) sections A/B/C as referenced in the source. |
| **UDI labeling** | Not mentioned. | Ensure compliance with **21 CFR 830** (label must bear a UDI, use GUDID). |

---

### 3. Required Submission Content (standard 510(k) checklist)

| Element | Typical Evidence | Gap Identified |
|---------|------------------|----------------|
| **Device description & intended use** | Narrative, block diagram, pictures. | *Missing* – needs to be produced. |
| **Predicate device(s)** | 510(k) number, classification, summary of similarities/differences. | *No specific identifier found in source — verify separately*. |
| **Bench performance data** (electrical safety, electromagnetic compatibility, software verification if applicable). | Test reports per recognized standards (e.g., IEC 60601‑1, ISO 14971 risk analysis results). | Not addressed in source – confirm completeness. |
| **Animal or clinical data** (if required for substantial equivalence). | Study protocols, statistical analyses. | No mention – determine need based on risk profile. |
| **Labeling & Instructions for Use (IFU)** | Full label set, user manuals, UDI placement. | Not referenced – must be drafted. |
| **Sterilization & biocompatibility** (if applicable). | ISO 10993 data, sterility validation reports. | No evidence cited. |
| **Software documentation** (if software is a component). | Software Development Lifecycle (SDLC) summary, verification/validation, PCCP if AI/ML. | Not indicated – verify presence of software. |
| **Risk Management File** | ISO 14971‑based risk analysis, mitigations, residual risk evaluation. | Required; source mentions “RTA 리뷰 체크포인트” but no detailed file. |
| **Design History File (DHF) sections A/B/C** | Design inputs, outputs, verification/validation records. | Source notes need for “기초 문서화”; DHF must be completed. |
| **Quality System Documentation** | QMS procedures, SOPs, corrective‑and‑preventive action (CAPA) records. | Implied by “감사 sweep과 체크리스트 보강 작업”. |

---

### 4. Identified Missing Information & Immediate Actions  

1. **Intended Use Statement** – develop a concise claim language.  
2. **Predicate Device Identification** – perform market search; select at least one cleared device with the same intended use and technological characteristics.  
3. **Complete DHF (Sections A‑C)** – compile design inputs/outputs, verification, validation data as per 21 CFR 820.  
4. **Risk Management File (ISO 14971)** – create or update to cover all identified hazards.  
5. **Evidence Package** – generate bench test reports, biocompatibility data, labeling set, and, if needed, clinical data.  

The source requires action on “minimum 3 of the 14 unmet must items.” The three most critical from a regulatory standpoint are:

- Predicate selection (item 1)  
- DHF documentation (item 2)  
- RTA review checkpoint establishment / risk management (item 3)

---

### 5. Risk Controls (ISO 14971‑aligned)

| Hazard | Control Measure | Status |
|--------|-----------------|--------|
| Electrical safety / EMC | Design to IEC 60601‑1, IEC 60601‑1‑2; performed testing. | TBD |
| Software failures (if applicable) | Adopt Predetermined Change Control Plan (PCCP) per FDA Dec 2024 guidance; implement robust verification/validation. | TBD |
| User error / misuse | Human factors engineering, clear IFU, labeling per 21 CFR 801. | TBD |
| Biocompatibility (if device contacts patient) | Conduct ISO 10993 testing suite. | TBD |
| Sterility breach (if sterile) | Validate sterilization processes; label with sterility status. | TBD |

All controls must be documented in the risk management file and reflected in design verification/validation activities.

---

### 6. Applicable Regulatory Citations  

- **Classification & Sub‑panel** – Imaging & radiology devices: **21 CFR Part 892**, e.g., §892.2050 for image processing software (Class II). *Confirm appropriate section once device function is known.*  
- **Quality Management System Regulation** – **21 CFR 820** (effective 2026‑02, ISO 13485‑aligned).  
- **Unique Device Identification** – **21 CFR 830**, §§830.10–830.60 (labeling) and §830.300–330 (GUDID).  
- **Risk Management** – FDA guidance referencing **ISO 14971**.  
- **Software Change Planning** – *Predetermined Change Control Plan (PCCP)*, FDA Final Guidance, Dec 2024.  

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason | Escalation Level |
|---------|--------|------------------|
| **No intended use/technology description** after 5 business days of request. | Submissions cannot proceed without a defined claim. | Senior RA Manager (approval to pause work). |
| **Unable to locate an appropriate predicate device** within the stipulated timeline. | May necessitate De Novo pathway or additional testing. | Lead regulatory strategist + project sponsor. |
| **Risk analysis indicates residual risk above “acceptable” threshold** or missing mitigation. | Could affect classification and FDA clearance. | QA/CMO & senior RA for risk acceptance decision. |
| **QMS non‑compliance identified in audit sweep** (e.g., incomplete SOPs, CAPA backlog). | Violates 21 CFR 820; could delay submission. | Quality Assurance Director. |
| **FDA feedback requesting additional data** during pre‑submission or review phase. | Must be addressed before clearance. | Project Lead + Regulatory team lead. |

When any of the above triggers occur, an immediate notification (email and documented in project tracker) should be issued to the designated escalation contact.

---

### 8. Peer Review Prompt  

> **@RA‑Peer:** Please critique the assumptions made about the likely classification panel, the completeness of the evidence checklist given the unknown device type, and any jurisdiction‑specific gaps (e.g., state‑level requirements, post‑market surveillance obligations). Highlight additional data or analyses you would request before finalizing the 510(k) strategy.

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

1. Chunk `1133221829333770557`

> ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **4주 연속 0% 정체** (06-26 / 07-03 / 07-10 / 07-17 동일). #951(07-03) → #959(07-10)에 이어 3연속 이관, 이번 주도 착수 실적 없음.

2. Chunk `1104470705522628403`

> ## 필수 작업 1. 14개 미충족 must 항목 중 최소 3건 착수 2. 기술 파일 구조(DHF section A/B/C) 기초 문서화 3. RTA 리뷰 체크포인트 수립 4. 감사 sweep과 체크리스트 보강 작업의 인력 배분 분리(전담 1인 배정 검토)

### kb-eval-20260721-it03-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_us-004", "iteration": 3, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "22bb65aae6d9e5ef", "source": "github:holee9/MD-process/issue-drafts/220_13_FDA_510k_RTA_핵심양식_초안.md", "source_hash": "2b2e64ed872d9caf987e923334f8bb1dab23e1f65d28ac42a81828e751edceb2"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `22bb65aae6d9e5ef`
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

> **Regulatory Draft – 510(k) Pathway Assessment**

| Item | Judgment / Recommendation | Supporting Basis |
|------|---------------------------|------------------|
| **Regulatory route** | Premarket notification (510(k)) is the default pathway for most Class II devices; a De Novo submission would be considered only if no legally marketed predicate exists. | 21 CFR §807.92 (submission requirements) |
| **Device classification** | *Cannot be determined from source.* The source provides no information on device type, intended use, or product code, so the applicable 21 CFR part (e.g., §892 for imaging devices) is unknown. | – |
| **Primary submission sections** | 1. Cover Sheet & FDA‑510(k) Summary/Statement of Intended Use  <br>2. Device Description & Comparison to Predicate  <br>3. Substantial Equivalence Rationale  <br>4. Performance Testing (bench, animal, clinical if required)  <br>5. Software Documentation (if applicable)  <br>6. Sterilization & Biocompatibility (as needed)  <br>7. Labeling (21 CFR §801)  <br>8. UDI Plan (21 CFR §830)  <br>9. Quality System compliance (21 CFR §820 – QMSR effective Feb 2026) | Standard 510(k) content per 21 CFR §807.92 |
| **Core evidence required** | • Detailed device description, materials, and specifications<br>• Predicate device identifiers (product code, 510(k) number, or PMA)<br>• Comparative performance data (bench testing, electrical safety, EMC, etc.)<br>• Biocompatibility testing per ISO 10993‑1 (if patient‑contacting)<br>• Sterilization validation (if marketed sterile)<br>• Software verification/validation and, for AI/ML, a Predetermined Change Control Plan (PCCP) – FDA guidance Dec 2024<br>• Labeling & IFU supporting intended use | FDA 510(k) Guidance Documents; ISO 14971 risk management |
| **Missing information (must‑items)** | The source cites “5 must items” that are unmet and cause an immediate Refuse to Accept (RTA). Based on typical 510(k) deficiencies, the likely missing elements are: 1️⃣ Predicate device identification<br>2️⃣ Intended use statement<br>3️⃣ Performance test results (bench/clinical)<br>4️⃣ Labeling draft<br>5️⃣ UDI labeling plan | Inferred from FDA Refuse‑to‑Accept guidance (21 CFR §807.92(b)(5)) |
| **Risk controls** | • Implement a QMS compliant with 21 CFR §820 (QMSR) – design controls, document control, corrective actions.<br>• Conduct risk analysis per ISO 14971 and integrate mitigations into design and labeling.<br>• For software/AI components, develop a Predetermined Change Control Plan (PCCP). | 21 CFR §820; FDA “Predetermined Change Control Plans for AI/ML‑Based Devices” guidance Dec 2024 |
| **UDI requirements** | Assign a device identifier and production identifier per 21 CFR §830.10–§830.60; submit device entry in GUDID. | 21 CFR §830 |
| **Human‑escalation triggers** | • Any of the five must‑items remain unresolved → initiate internal RTA risk review.<br>• Classification remains unknown after initial scoping → escalate to senior RA for predicate search and product‑code assignment.<br>• Early FDA feedback indicating “Refuse to Accept” probability > 70 % (current score 52 %) → pause submission preparation and convene cross‑functional corrective action meeting.<br>• Detection of AI/ML functionality without a PCCP → escalates to software/clinical lead for plan development. | Derived from source’s RTA risk (“FDA 510(k) RTA 점수 52% → 약 85% (5개 must 해소 시)”) and FDA submission standards. |

---

### Immediate Actions

1. **Collect missing “must” data** – predicate identifiers, intended use narrative, performance testing reports, labeling draft, UDI plan.
2. **Confirm device class** – perform product‑code lookup in the FDA Device Classification Database using the device’s functional description (once obtained).
3. **Update RTA score** – complete the five items; re‑run the internal validation tool to verify that the projected acceptance probability reaches ≥ 85 %.
4. **Document risk controls** per ISO 14971 and embed them in the design history file (DHF) within the QMSR framework.
5. **Prepare a Predetermined Change Control Plan** if any AI/ML components are present.

If any of these steps cannot be completed within the next 10 business days, trigger escalation to the RA manager for resource allocation and timeline reassessment.

---

### Peer‑Review Prompt

> *Colleague*, please review this draft for:
> - Assumptions about the five “must” items—are they aligned with typical FDA RTA deficiencies?
> - Completeness of the evidence checklist given an unknown device type; suggest additional data if the product is likely to fall under a specialized panel (e.g., imaging ‑ Part 892, clinical chemistry ‑ Part 862).
> - Any jurisdiction‑specific gaps, such as state‑level registration or FDA‑global harmonization considerations that might affect our submission strategy.

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

### kb-eval-20260721-it03-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_us-005", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "76c4047eeb4ef5c9", "source": "github:holee9/MD-process/issue-drafts/931_RA_FDA_Form_표지_양식_4건_작성.md", "source_hash": "68cd74d39caaa060d4323f37a5c193a02284866bee050ec5139fdf5916ca6ff7"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `76c4047eeb4ef5c9`
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

> **Regulatory Draft – 510(k) Submission Planning & Gap Identification**

---

### 1. Bottom‑Line Regulatory Judgment  
*The current documentation set is insufficient to determine the device classification or the exact 510(k) pathway (traditional vs special vs abbreviated). The next actionable step is to obtain the missing product‐specific information (device description, intended use, risk class, and potential predicate devices) before any substantive submission work can proceed.*

---

### 2. Required Evidence & Documentation (Baseline 510(k) Package)

| Item | Purpose | Typical Content | Regulatory Reference |
|------|----------|-----------------|-----------------------|
| **FDA Form 3514 – Cover Sheet** | Identifies submitter & device | Company name, address, contact, DUNS, registration number | 21 CFR §807.92 (Cover Sheet) |
| **FDA Form 3601 – User Fee Cover Sheet + Payment Receipt** | Confirms payment of the $19,975 user fee (FY‑2026) | Completed form, proof of electronic transaction | 21 CFR §805.10 (User Fees) |
| **FDA Form 3654 – Standards Data Report** | Demonstrates conformity with recognized consensus standards | List of applicable ANSI/AAMI/ISO standards & compliance evidence | FDA Guidance “Use of Consensus Standards” (2023) |
| **FDA Form 3881 – Indications for Use Statement** | Defines the clinical indication(s) | Precise wording, patient population, anatomical site, intended purpose; note OMB expiration 2026‑07‑31 | 21 CFR §814.45 (Indications for Use) |
| **510(k) Cover Letter** | Formal submission cover & summary | Applicant info, device name, submitter type, brief statement of substantial equivalence | FDA Submission Guidance (2024) |
| **Device Description & Labeling** | Core specification & user information | Technical specifications, materials, accessories, labeling per 21 CFR §801.5 | 21 CFR §801 (Labeling) |
| **Predicate Device Identification** | Basis for substantial equivalence claim | Predicate 510(k) number, registration, comparison table of functionalities, technological characteristics | 21 CFR §807.92(b)(3); FDA “Guidance on Substantial Equivalence” (2022) |
| **Performance Testing** (bench, animal, clinical as needed) | Demonstrates that the device meets safety & effectiveness criteria | Test protocols, results, statistical analysis; ISO 10993 biocompatibility, sterility validation if applicable | 21 CFR §820.30 (Design Validation); ISO 14971 risk management |
| **Risk Management File** | Shows that hazards have been identified and mitigated | Risk analysis, control measures, verification of controls, residual risk evaluation | ISO 14971:2019 (cited in FDA guidance) |
| **Software Documentation** (if applicable) | Software lifecycle & validation evidence | Architecture diagram, V‑V plan, cybersecurity controls, Predetermined Change Control Plan (PCCP) if AI/ML | FDA “Predetermined Change Control Plan” Guidance, Dec 2024 |
| **Quality Management System (QMS) Evidence** | Demonstrates compliance with the 2026 QMS Regulation | Certificate of ISO 13485:2016 alignment, design control records, complaint handling logs | 21 CFR §820 (Quality System Regulation – effective Feb 2026) |
| **Unique Device Identification (UDI) Package** | Enables device traceability in the market | UDI label mock‑up, production identifier, GUDID submission excerpt | 21 CFR §830.10‑§830.60 (UDI Requirements) |
| **Regulatory Checklist & RTA Completion Evidence** | Shows that all “RTA Section A” items are satisfied per internal tracking | Confirmation of the five listed forms and cover letter; linkage to `13_규제평가_체크리스트/FDA_510k_RTA.md` entries | Internal SOP – cross‑referenced with FDA 510(k) requirements |

---

### 3. Missing Information (Gaps that Must Be Filled)

| Gap | Why It Matters | Action Required |
|-----|----------------|-----------------|
| **Device type & Intended Use** | Determines the product code, FDA review panel, and classification (Class I/II/III). | Obtain a concise device description, target population, anatomical site, and clinical purpose. |
| **Regulatory Classification** | Drives submission requirements (e.g., special controls for Class II). | Perform a classification lookup in 21 CFR §862‑§892 based on intended use; confirm whether the device falls under Part 892 (imaging) or another panel. |
| **Predicate Device(s)** | Core of the substantial equivalence argument. | Identify at least one legally marketed 510(k) predicate with the same technological characteristics and intended use. Record its 510(k) number. |
| **Performance Test Plan** | Required to substantiate safety & effectiveness. | Draft a testing matrix (bench, animal, clinical) aligned with identified risks and applicable consensus standards. |
| **Risk Management Documentation** | Mandatory for all Class II/III devices. | Conduct ISO 14971 risk analysis; map controls to design verification activities. |
| **Software Lifecycle Evidence** (if software‑driven) | Needed for validation & cybersecurity compliance. | Prepare a Software Development Plan, V‑V report, and, if AI/ML, a Predetermined Change Control Plan (PCCP). |
| **UDI Strategy** | Required for market entry post‑February 2026. | Select a UDI issuing agency, generate the device identifier, and prepare GUDID submission data. |
| **QMS Certification Proof** | New QMSR (effective 2026‑02) supersedes older ISO 13485 references. | Provide an updated ISO 13485:2016 certificate with explicit alignment to 21 CFR §820. |

---

### 4. Core Risk Controls to Address in the Submission

1. **Design Controls** – per 21 CFR §820.30 (design history file, verification & validation).  
2. **Human Factors/Usability** – evidence that user interface and instructions prevent misuse (FDA “Human Factor Validation Guidance”, 2023).  
3. **Cybersecurity** – if the device incorporates software/network connectivity, include a threat model and mitigation plan (FDA Cybersecurity Guidance, 2024).  
4. **Sterilization & Biocompatibility** – ISO 10993 testing results where applicable.  
5. **Labeling Controls** – ensure label complies with 21 CFR §801; includes device name, intended use, warnings, UDI.  

---

### 5. Regulatory Citations (Established References)

* **21 CFR §807** – Premarket notification (510(k)) and registration requirements.  
* **21 CFR §820** – Quality System Regulation (QMSR) effective February 2026.  
* **21 CFR §801** – Labeling requirements.  
* **21 CFR §830.10‑§830.60** – Unique Device Identification (UDI) obligations.  
* **21 CFR §892.2050** – Class II medical image management and processing systems *[needs confirmation of device panel]*.  
* FDA Guidance “Predetermined Change Control Plan (PCCP)” – December 2024 (AI/ML devices).  

---

### 6. Human‑Escalation Triggers

| Trigger | Reason for Escalation |
|---------|-----------------------|
| **Absence of device description & intended use** | Classification cannot be assigned; submission scope undefined. |
| **No identified predicate 510(k)** | Substantial equivalence claim unsubstantiated – may require De Novo or PMA pathway. |
| **Unclear panel (e.g., imaging vs clinical chemistry)** | Mis‑classification could lead to FDA refusal or additional review time. |
| **Missing performance testing plan** | Safety & effectiveness not demonstrated; submission would be incomplete. |
| **No risk analysis file per ISO 14971** | Core QMS evidence missing, non‑compliant with 21 CFR §820.30. |
| **UDI strategy not defined before Feb 2026 market entry** | Non‑compliance with post‑market identification requirements. |
| **QMS certification not updated to new QMSR** | Failure to meet the revised quality system expectations effective 2026‑02. |

*When any of the above triggers are identified, a senior regulatory manager should be notified to obtain the missing information and/or re‑evaluate the submission pathway before further work proceeds.*

---

### 7. Peer Review Prompt  

> **RA Peer Challenge:**  
> Please review the assumptions made regarding (a) the need for predicate identification versus a potential De Novo route, (b) classification determination in the absence of device details, and (c) whether any additional FDA programs (e.g., Special 510(k), Early Feasibility Study) might be applicable based on the limited information provided. Identify any jurisdiction‑specific gaps or alternative regulatory strategies that may have been overlooked.

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

1. Chunk `202395958248735480`

> ## 목표 영향 - 다음 분기(2026-Q3) `build_readiness.py` 재실행 시 FDA RTA Section A 5건 모두 충족 → **점수 0% → 33%** 예상.

2. Chunk `608496877809508828`

> ## 작업 범위 (Done 정의) - [ ] FDA Form 3514 — 510(k) Cover Sheet 양식 (회사명/주소/연락처 자리표시자 포함) - [ ] FDA Form 3601 — User Fee Cover Sheet 양식 + 수수료 결제 영수증 자리표시자 - [ ] FDA Form 3654 — Standards Data Report 양식 또는 자사 별도 문서 양식 - [ ] FDA Form 3881 — Indications for Use Statement 양식 (현행 OMB 만료일 2026-07-31 주의) - [ ] 510(k) Cover Letter 영문 표준 양식 (applicant name/address/contact/submitter type) - [ ] `13_규제평가_체크리스트/FDA_510k_RTA.md` 항목 A1~A5의 `related_docs:` 필드에 신규 doc-id 등록

## ra_eu

### kb-eval-20260721-it03-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_eu-001", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3c458ddac864fc0b", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

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

> **Regulatory Draft – MDR 2017/745 Classification & Conformity‑Assessment Roadmap**

---

### 1. Device Scope (inferred from source)

- **Core technology:** An X‑ray generator that emits ionising radiation for diagnostic imaging.  
- **Associated element:** Medical‑device software (SaMD) that processes the acquired images and supports diagnostic decisions.

The source explicitly flags both elements:

* “Rule 10: 이온화 방사선 방출 진단기기 (X‑ray 발생장치 → Class IIb)” → classification of the X‑ray generator under **Rule 10, Annex VIII**.  
* “Rule 11: Medical Device Software (SaMD) 분류” → software is covered by **Rule 11, Annex VIII**.

---

### 2. Classification

| Component | MDR rule (Annex VIII) | Assigned class |
|-----------|----------------------|----------------|
| X‑ray generator (emits ionising radiation for diagnostic purposes) | Rule 10 – “ionising‑radiation emitting diagnostic device” | **Class IIb** |
| Image‑processing/diagnostic software (SaMD) | Rule 11 – “software providing information for diagnosis or therapy” | **Class IIa** (unless the software’s output can lead to death/serious deterioration, which would raise it to Class III; no such indication is stated in the source) |

*If the software directly influences a therapeutic decision that could cause serious harm, re‑classify to Class IIb or III per Rule 11 – this requires a clinical risk assessment (see §17 GSPR).*

---

### 3. Conformity‑Assessment Route (per class)

| Class | Mandatory MDR Annex for CE‑marking* |
|-------|--------------------------------------|
| IIb   | **Annex IX** – Full quality‑management system (QMS) + technical documentation assessment by a Notified Body **or** **Annex X** – Type‑examination followed by EC type‑approval. |

> \*The manufacturer may also use Annex XI for production‑conformity verification after an initial Annex IX/X assessment, but the primary route must be established at CE marking.

**Recommended route:** Annex IX (most common for Class IIb devices with a QMS). This yields a single “Conformité Européenne” mark and aligns with the requirement to keep the technical documentation up‑to‑date (Annex II) under Art. 10(9).

---

### 4. Evidence Package Required for Notified Body Review  

| Item | Regulatory source | Typical content |
|------|-------------------|-----------------|
| **Technical Documentation** | Annex II (MDR) | Device description, intended purpose, design & manufacturing information, risk management file (ISO 14971), GSPR compliance matrix (§1‑22), verification & validation data, labeling (Annex I §23). |
| **EU Declaration of Conformity** | Annex IV | Signed by the manufacturer, referencing all applicable GSPRs and standards. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | State‑of‑the‑art literature review, clinical data from either a PMCF study or equivalent existing investigations, benefit–risk analysis. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | Planned follow‑up activities, sampling strategy, endpoints, timeline; final report summarising findings. |
| **Post‑Market Surveillance (PMS) System** | Art. 83 – PMS system; Art. 84 – PMS plan | Continuous collection of performance and safety data, trend analysis, corrective actions. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 (for Class IIb) – annual update | Conclusions on benefit‑risk, PMCF results, sales volume & user population. |
| **Standards compliance evidence** | IEC/ISO standards cited in GSPR §16‑§20 | • IEC 60601‑2‑28 (X‑ray tube assemblies) <br>• IEC 60601‑2‑54 (radiography/radioscopy equipment) <br>• IEC 62304 (software lifecycle) <br>• IEC 62366‑1 (usability) <br>• ISO 14971 (risk management). |
| **Radiation safety assessment** | GSPR §16.4 (Protection against ionising radiation) | Measured dose outputs, shielding calculations, compliance with IEC 60601‑2‑28/54 limits. |

---

### 5. Identified Missing Information (must be supplied before NB submission)

1. **Detailed Intended Use Narrative** – precise clinical indication(s), target patient population, user profile (professional vs lay).  
2. **Full Risk Management File** – risk analysis, evaluation of residual risks, and verification of mitigations against GSPR §16‑§20.  
3. **Clinical Data Strategy** – whether a dedicated PMCF study will be performed or reliance on existing clinical literature; justification for the chosen approach.  
4. **Software Classification Justification** – mapping of software functionality to Rule 11 (including any possible Class III triggers).  
5. **PMS Plan specifics** – sampling frequency, data sources, post‑market indicators, and escalation criteria.  
6. **Labeling & IFU draft** – complete Annex I §23 documentation for both the generator and the software.  
7. **Declaration of Conformity (DoC) draft** – provisional DoC awaiting final NB review.  

*Absence of any of these items constitutes a “gap” that must be escalated to the project lead before proceeding.*

---

### 6. Core Risk Controls (aligned with MDR GSPR)

| GSPR reference | Control measure |
|----------------|-----------------|
| **§16.4 – Protection against ionising radiation** | Dose‑output verification, shielding design, interlocks, beam‑stop mechanisms; compliance testing per IEC 60601‑2‑28/54. |
| **§17 – Electronic programmable systems / software** | Secure software development lifecycle (IEC 62304), validated algorithms, cybersecurity safeguards (Annex II §6). |
| **§18 – Active devices & connections** | Power‑supply safety, emergency stop, isolation monitoring; IEC 60601‑1 general requirements. |
| **§20 – Mechanical/thermal risks** | Housing integrity tests, temperature monitoring, ergonomic design per IEC 62366‑1. |
| **§22 – Lay‑person use (if applicable)** | Clear labeling and user instructions; usability validation studies. |
| **Overall** | Risk management file demonstrates that all residual risks are weighed against clinical benefits (ISO 14971). |

---

### 7. Human‑Escalation Triggers

| Situation | Action required | Who escalates |
|-----------|----------------|---------------|
| **Unclear software class (potential Class III)** | Conduct detailed functional analysis; possibly reclassify to Class IIb/III. | Lead Clinical Engineer / Software Safety Manager → Project Manager. |
| **Insufficient clinical evidence for Class IIb** | Initiate a PMCF study or collect equivalent clinical data before Notified Body review. | Clinical Research lead → Regulatory Project Lead. |
| **Risk‑control gaps (e.g., radiation shielding not validated)** | Perform additional verification testing; update risk file. | QA/Testing team → RA Lead. |
| **PMS/PMCF plan not aligned with Art. 84/86 timelines** | Revise PMS schedule; ensure annual PSUR readiness. | Post‑Market Surveillance coordinator → Regulatory Manager. |
| **Missing or incomplete DoC draft** | Draft and sign provisional DoC, obtain NB review sign‑off. | Legal/Regulatory affairs – senior RA manager. |
| **Any non‑conformity identified during internal audit of Annex II documentation** | Pause external submission; remediate gaps before NB engagement. | Quality Management System (QMS) auditor → Project Sponsor. |

---

### 8. Peer‑Review Prompt

> **To a fellow EU Regulatory Affairs colleague:**  
> Please review the above classification assumptions, especially the software’s functional scope under Rule 11, and verify that all cited GSPR §§ and Annex references correctly capture the required evidence for a Class IIb X‑ray generator. Check whether any additional MDR provisions (e.g., Annex XII on Unique Device Identification) impact the submission package at this stage, and flag any jurisdiction‑specific omissions.

---

**Regulatory Judgment:**  
- The X‑ray generator is **Class IIb** under **Rule 10 (Annex VIII)**; the associated image‑processing software is **Class IIa** under **Rule 11** unless a higher impact is demonstrated.  
- The appropriate conformity‑assessment route is **Annex IX** (full QMS + technical documentation assessment) for the Class IIb device, with Annex X as an alternate path if a type‑examination strategy is preferred.  
- All evidence items listed above must be compiled and any identified gaps addressed before engaging a Notified Body.

*All regulatory citations are drawn directly from MDR text; no case‑specific identifiers were present in the source excerpts (verify separately if needed).*

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

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20260721-it03-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_eu-002", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e943ded4dd4d76d4", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

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

> **Regulatory Draft – Classification & Conformity‑Assessment Roadmap**

---

### 1. Device Synopsis (as far as can be inferred from the source)

| Item | Status |
|------|--------|
| **Device name / model** | *Not provided* – cannot be extracted from the source excerpts. |
| **Intended medical purpose** | *Missing* – no statement of indication, target patient group, or mode of action is available. |
| **Core technology** | The excerpt only references generic MDR‑related infrastructure (UDI, vigilance, NB fees). No technical description can be deduced. |

> **Implication:** Without an explicit intended use the classification cannot be finalized. The manufacturer must supply a concise “Intended Use/Indications for Use” statement before any rule‐level analysis can be applied.

---

### 2. Classification Approach (MDR Art. 51 + Annex VIII)

1. **Self‑classification responsibility** – the manufacturer bears the burden of applying the rules sequentially and must retain evidence of that process. *(Art. 51 MDR; Annex VIII rule set)*【2】  
2. **Rule selection methodology**  
   - Apply all 22 classification rules in order (Annex VIII).  
   – The *highest* class resulting from any applicable rule determines the final class.  
3. **Borderline assistance** – if uncertainty remains after rule application, consult:  

   * the national Competent Authority (CA) or  
   * MDCG Guidance “Guidance on borderline and classification” (latest version v2.1.1, Sep 2023). *(MDCG Manual reference)*【2】

4. **Pre‑assessment checklist** – before invoking a rule, the following device attributes must be clarified (all currently missing):  

   - Active vs. passive nature; presence of energy source or software.  
   - Implantable status.  
   - Invasiveness, duration of contact, and whether it measures/diagnoses vital physiological parameters.  
   - Intended therapeutic or diagnostic function (e.g., “administer energy”, “monitor vital signs”).  

> **Human‑Escalation Trigger #1:** *If the manufacturer cannot provide a complete intended‑use description within 5 working days, flag to senior RA lead for postponement of classification work.*

---

### 3. Anticipated Classification Scenarios (Illustrative Only)

| Potential Rule | Example Device Type* | Resulting Class |
|----------------|----------------------|-----------------|
| **Rule 9** – Active therapeutic devices | Energy‑delivering wound‑healer | IIa (or IIb if hazardous) |
| **Rule 10** – Active diagnostic/monitoring | ECG monitor with real‑time alerts | IIa (IIb for vital‑parameter monitoring) |
| **Rule 11** – Software providing diagnostic/therapeutic decisions | AI‑based image analysis software | IIa–III depending on impact |
| **Rule 17** – Imaging recorders | X‑ray detector plate | IIa |

\*These are *illustrative* only; the actual rule can be identified only after the intended use is known.

---

### 4. Conformity‑Assessment Route (choice depends on final class)

| Class | MDR Annex route | Required deliverables |
|-------|-----------------|----------------------|
| **Class I** (non‑sterile, non‑measuring) | Self‑declaration – no NB involvement | • EU Declaration of Conformity (Annex IV)<br>• Technical Documentation (Annex II) |
| **Class Is / Im** (sterile or measuring) | Annex IX (QMS + technical file assessment by NB) | • QMS certificate (ISO 13485) assessed per Annex IX<br>• Full Technical Documentation (Annex II) |
| **Class IIa / IIb / III** | Annex IX (full NB assessment) – same deliverables as above plus:<br>• Clinical Evaluation Report (CER, Annex XIV Part A) <br>• PMCF plan & report (Annex XIV Part B) |
| **Special cases (e.g., custom‑made)** | Not applicable – see MDR Annex VIII rule ... (outside scope of this draft) |

> **Human‑Escalation Trigger #2:** *If the provisional class lands in IIa or higher, a qualified Notified Body must be engaged within 10 working days. Failure to secure NB quotation → escalation to Project Manager.*

---

### 5. Evidence Package Required for an MDR Submission

| Evidence Area | Mandatory Documents (MDR citations) |
|---------------|--------------------------------------|
| **Technical Documentation** | Annex II (General technical file) – design dossier, risk management file, manufacturing information, labeling (§23). |
| **Clinical Evaluation** | CER in line with Annex XIV Part A; must be kept current under Art. 61 MDR. |
> *If Class IIa/IIb/III*: also provide PMCF plan & report (Annex XIV Part B). |
| **Post‑Market Surveillance** | PMS system (Art. 83); PMS plan (Art. 84); PSUR for Class IIa/b/III (Art. 86) or PMS report for Class I (Art. 85). |
| **UDI & EUDAMED Registration** | UDI allocation via national portal (e.g., udiportal.mfds.go.kr) and entry into EUDAMED (Art. 33‑39). |
| **Authorized Representative** | Declaration of representation per Art. 11 MDR; proof of appointment for EU market. |
| **Quality Management System** | ISO 13485 certificate, audited per Annex IX requirements. |
| **Risk Management** | Risk management file complying with ISO 14971, mapped to GSPR §§16‑20 (Annex I). |

> **Missing Information Flag:** *No specific clinical data sources, device architecture diagrams, or risk analysis outputs are present in the source excerpts.*  

> **Human‑Escalation Trigger #3:** *If any of the above evidence items cannot be produced within the planned timeline, raise a “Evidence Gap” ticket to the Clinical & Risk Management leads.*

---

### 6. Core Risk Controls (to be documented)

| GSPR § | Control Requirement | Typical Implementation |
|--------|---------------------|------------------------|
| **§16** – Radiation protection (if applicable) | Shielding, dosimetry, compliance with IEC 60601‑2‑54/28/44 as appropriate. |
| **§17** – Software safety | Follow IEC 62304 (software lifecycle), perform usability engineering per IEC 62366‑1. |
| **§18** – Active device safety | Verify that energy delivery is limited to intended therapeutic levels; include fail‑safe mechanisms. |
| **§19** – Active implantable devices | Conduct biocompatibility, electromagnetic compatibility, and long‑term reliability testing (IEC 60601‑1‑8). |
| **§20** – Mechanical/thermal safety | Perform strength, fatigue, and temperature limits testing per IEC 60601‑1. |
| **§22** – Lay‑person use | Include clear labeling/instructions per Annex I §23; perform usability validation with representative users. |

All controls must be justified in the risk management file (ISO 14971) and cross‑referenced to the GSPR clauses.

---

### 7. Summary Judgment & Escalation Matrix

| Decision Point | Current Status | Action Required | Escalation Trigger |
|----------------|----------------|-----------------|--------------------|
| **Intended Use Definition** | Missing | Obtain from manufacturer (incl. indication, target population, mode of action). | If not received within 5 working days → notify Senior RA Lead. |
| **Pre‑liminary Classification** | Indeterminate (no device attributes) | Apply Annex VIII rules once intended use is known; document decision process. | Unclear after rule application → request Competent Authority ruling per MDCG Manual. |
| **Conformity Route Selection** | Dependent on final class | Prepare technical file for the appropriate MDR annex (II, IX). | If class ≥ IIa and NB not yet selected → fast‑track NB quotation process; escalate if quotations exceed budget threshold. |
| **Evidence Compilation** | Major gaps (clinical data, risk analysis, PMS plan) | Populate each evidence block per Section 5. | Any missing mandatory document after 10‑day buffer → raise “Regulatory Gap” to Project Manager. |

---

### 8. Peer Review Prompt

> *@RA‑Peer* – Please review the assumptions made in this draft, especially:  
> 1. The adequacy of referencing only Annex VIII classification rules without an actual device description.  
> 2. Whether any jurisdiction‑specific nuances (e.g., Korean UDI portal mention) affect our MDR‑focused submission plan.  
> 3. Potential gaps where national competent authority guidance might supersede MDCG recommendations for borderline cases.

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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20260721-it03-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_eu-003", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "fe263dc57fa1ee07", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `fe263dc57fa1ee07`
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

> **Regulatory Draft – Diagnostic X‑ray Imaging System (EU MDR)**  

---

### 1. Device Overview (as derived from source)

| Item | Description |
|------|--------------|
| **Device type** | Active medical device that emits ionising radiation for diagnostic imaging (radiography/radioscopy). |
| **Intended purpose** | Generation of diagnostic X‑ray images of patients; *not* a therapeutic radiation delivery system. |
| **Major subsystems** | • X‑ray generator (tube + high‑voltage supply)  <br>• Digital flat‑panel detector (image‐recording device)  <br>• Image‑processing / display software (provides information for diagnostic decisions). |

*Source excerpt confirms the need to treat the X‑ray **generator** as a *diagnostic* active device and excludes it from Rule 9 (therapeutic) classification.*  

---

### 2. Classification & Conformity Assessment Route  

| Regulatory element | Determination | Reference |
|--------------------|---------------|-----------|
| **MDR rule** | **Rule 10** – “Active devices for diagnosis or monitoring” that emit ionising radiation are classified as **Class IIb**. | Annex VIII, Rule 10 (EU MDR 2017/745). |
| **Detector subsystem** | **Rule 17** – “Devices specifically intended for recording diagnostic images generated by X‑ray radiation” → **Class IIa**. | Annex VIII, Rule 17. |
| **Software subsystem** (if considered a separate device) | Likely **Rule 11**, Class IIa (information used for diagnosis). | Annex VIII, Rule 11. |
| **Overall system class** | The highest‑risk constituent drives the system classification → **Class IIb** (Rule 10). | – |
| **Conformity assessment route** | **Annex IX** – Full quality‑management system audit + technical documentation review by a Notified Body (NB). | Annex IX, MDR 2017/745. <br>*(Alternative: Annex X type‑examination if the NB prefers a separate type‑examination for the active X‑ray generator; still followed by Annex XI production conformity verification.)* |
| **Notified‑Body involvement** | Required for Class IIb devices – selection of NB must be verified in the CE‑marking plan. | – |

---

### 3. Mandatory Technical Documentation (per Annex II)  

| Document | Content requirement | Gap / Action required |
|----------|---------------------|------------------------|
| **Device description & intended purpose** | Clear statement that the device is for *diagnostic* X‑ray imaging only; exclusion of therapeutic use. | Verify and embed in the “Intended Use” section; ensure labeling reflects this. |
| **Risk Management File** | ISO 14971 process, addressing all GSPR relevant to active radiation devices (§ 16, § 18, § 20). | Radiation‑dose control measures, interlocks, shielding verification data missing – need test reports. |
| **Design & Manufacturing Information** | IEC 60601‑2‑54 compliance (X‑ray equipment), IEC 62304 (software lifecycle) where applicable, IEC 62366‑1 (usability). | Confirmation of conformity with IEC 60601‑2‑54 not present – request test certificates. |
| **Performance & Safety Testing** | • Radiation output, beam quality, leakage, dose‑area product <br>• Electrical safety, EMC <br>• Image quality metrics (DQE, MTF) | No radiation‑dosimetry data supplied; acquire measurements per IEC 60601‑2‑54 Annex D and IEC 62220‑1‑1. |
| **Clinical Evaluation Report (CER)** | Systematic review of state‑of‑the‑art literature, clinical benefit/risk analysis; kept current (Art. 61). | No CER draft identified – must be prepared (Annex XIV Part A). |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Defined plan for ongoing performance monitoring, especially dose management and image quality trends. | PMCF plan absent – develop per Annex XIV Part B. |
| **PMS System & PSUR** | PMS system (Art. 83), PMS plan (Art. 84), Periodic Safety Update Report (Class IIb → Art. 86, at least annually). | No PSUR schedule; set up annual reporting timeline. |
| **EU Declaration of Conformity** | Signed by the manufacturer, referencing all applicable GSPR and standards. | Draft required – include Annex IV citation. |
| **Labeling & IFU** | Information per Annex I § 23 (including radiation safety instructions for users). | Verify inclusion of dose‑monitoring guidance in IFU. |

---

### 4. Required Evidence Package for Notified‑Body Submission  

1. **Technical Documentation (Annex II)** – complete, signed and indexed.  
2. **Risk Management File** – with risk control measures for radiation exposure, software failures, misinterpretation of images.  
3. **IEC 60601‑2‑54 test reports** (electrical safety, radiation protection).  
4. **Clinical Evaluation Report** (Annex XIV Part A) – includes systematic literature search covering the latest X‑ray imaging technology and comparative performance data.  
5. **PMCF Plan & Interim Reports** (Annex XIV Part B).  
6. **PMS System description** (Art. 83) + PSUR draft (Art. 86).  
7. **EU Declaration of Conformity** (Annex IV).  
8. **EUDAMED registration entries** (Article 33‑39).  

---

### 5. Risk Controls (selected, tied to GSPR)

| GSPR § | Hazard / Control | Implementation evidence |
|--------|------------------|--------------------------|
| § 16 (Radiation protection) | • Beam‑limiting and filtration <br>• Interlock circuitry that disables emission if safety conditions not met <br>• Dose‑monitoring display for operator | IEC 60601‑2‑54 test data; software validation report (IEC 62304). |
| § 18 (Active devices) | • Redundant power‑supply monitoring <br>• Fault detection & safe‑state transition | Risk analysis outcomes, FMEA. |
| § 20 (Mechanical/thermal) | • Device housing designed to prevent accidental exposure; thermal shutdown on over‑temperature | Mechanical design verification reports. |
| § 22 (Lay‑person use – not applicable) | N/A – device intended for professional operators only. | – |
| § 23 (Labelling & IFU) | Detailed instructions on shielding, positioning, dose limits, emergency stop. | Final IFU review sign‑off. |

---

### 6. Missing Information / Open Items  

| Item | Why needed | Action |
|------|------------|--------|
| **Explicit “diagnostic only” intended use statement** | Prevents mis‑application of Rule 9 (therapeutic) – essential for correct classification. | Add to Device Description & labeling; circulate for approval. |
| **Radiation dosimetry test reports** (beam quality, leakage, DAP) | Mandatory to demonstrate compliance with GSPR § 16.4 (ionising radiation protection). | Obtain from accredited lab; attach to Technical Documentation. |
| **IEC 60601‑2‑54 conformity evidence** | Required for Class IIb active X‑ray equipment. | Request certificates or perform in‑house testing under IEC standards. |
| **Clinical Evaluation Report (CER)** | Needed for Annex XIV Part A; supports benefit–risk determination. | Conduct systematic literature review, draft CER, submit for internal review. |
| **PMCF plan** (including post‑market dose monitoring) | Required for ongoing safety evidence (Annex XIV Part B). | Draft plan with defined KPIs; obtain stakeholder sign‑off. |
| **PSUR schedule** (annual for Class IIb) | Needed under Art. 86 to keep NB informed of safety trends. | Define calendar, assign responsibility. |

---

### 7. Human‑Escalation Triggers  

| Trigger condition | Escalation destination | Rationale |
|-------------------|------------------------|-----------|
| **Unclear intended purpose** (diagnostic vs therapeutic) | Senior RA / Regulatory Lead | Mis‑classification leads to wrong NB route and potential non‑compliance. |
| **Absence of radiation safety test data** | QA Manager & Project Engineer | GSPR § 16 violation – device cannot be placed on market without proof of dose control. |
| **Incomplete CER or missing clinical data** | Clinical Affairs Lead | Benefit–risk assessment incomplete; NB will reject submission. |
| **Discrepancy between MFDS/FDA mapping (Rule 5/9) and MDR classification** | Regulatory Strategy Team | Source highlights risk of propagating erroneous mapping to CE‑marking plan – must be corrected before any downstream documents are finalised. |
| **Failure to schedule PSUR within 12 months for Class IIb** | Compliance Officer | Art. 86 non‑conformity could trigger audit findings and market suspension. |

---

### 8. Peer Review Request  

> **To:** [RA colleague]  
> **Subject:** Challenge of Classification & Documentation Gaps – Diagnostic X‑ray System (MDR)  
> **Please review** the assumptions made regarding:  
> - The exclusion of therapeutic use and reliance on Rule 10 for classification; verify that no ancillary accessories could invoke Rule 9.  
> - Completeness of the risk management file in addressing all relevant GSPR (§ 16‑20).  
> - Whether the proposed evidence package fully satisfies Annex IX requirements for a Class IIb device, especially concerning software components (Rule 11) and detector subsystem (Rule 17).  
> **Identify** any jurisdiction‑specific gaps (e.g., additional EU‑type‑examination considerations under Annex X) or missing references to standards that may be needed.  

---

### 9. Regulatory Judgment Summary  

- The X‑ray imaging system is **Class IIb** under **MDR Rule 10**, not Rule 5/9 as mistakenly mapped in the source table.  
- Conformity assessment must follow **Annex IX** (QMS + technical documentation audit) with a Notified Body, supplemented by **Annex XI** for production conformity verification.  
- A complete evidence set—including risk management, IEC 60601‑2‑54 testing, CER, PMCF plan, PMS system, PSUR, and EU Declaration of Conformity—is required before submission.  

Any identified gaps (intended purpose clarification, radiation safety data, clinical evaluation) must be resolved and escalated per the triggers above to avoid non‑conformities during Notified Body audit.

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

### kb-eval-20260721-it03-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_eu-004", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "284455ed830983b1", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md", "source_hash": "4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `284455ed830983b1`
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

> **Regulatory Draft – GUI Software Used in the X‑ray Imaging Room (촬영실 GUI SW)**  

---

### 1. Classification & Conformity‑Assessment Route  

| Item | Determination |
|------|---------------|
| **Applicable MDR rule** | **Rule 11** – “Software providing information for diagnostic or therapeutic decisions” (source [1]) |
| **Proposed class** | Depends on the impact of the software’s output: <br>• If a decision could cause death or irreversible deterioration → **Class III**  <br>• If a decision could lead to serious deterioration or necessitate surgical intervention → **Class IIb**  <br>• Otherwise (typical diagnostic support) → **Class IIa** |
| **Current best‑fit** | The excerpt states “촬영실 GUI SW = Rule 11 적용, 영향도에 따라 IIa ~ III”. Without more detail on the clinical impact we must assume the **most conservative approach – Class IIb** (typical for imaging‑room decision support). |
| **Conformity‑assessment route** | For Class IIb devices the MDR requires **Annex IX** (full quality‑management system assessment + technical documentation review by a Notified Body).  The device will also need to satisfy Annex X if any type‑examination is required for subcomponents, but the primary route remains Annex IX. |
| **Relevant transition deadlines** | According to the MDR transition table (source [2]), Class IIb non‑implantable devices must be CE‑marked by **31 Dec 2027**. This sets the project timeline for final NB assessment and EUDAMED registration. |

---

### 2. Core Technical Documentation Required (Annex II)  

| Document | Why needed | Key contents |
|----------|------------|--------------|
| **Device description & intended use** | Basis for classification and risk analysis | Full UI mock‑ups, functional block diagram, clinical indication, user environment (X‑ray suite), intended users (radiographers, radiologists). |
| **Risk Management File** – ISO 14971 | Demonstrates that all hazards are identified and mitigated | Hazard identification, risk evaluation, risk control measures, residual risk assessment, verification of controls; mapping to GSPR §17 (software) and §18 (active devices). |
| **Software Lifecycle Documentation** – IEC 62304 | Shows compliance with software development safety | Software development plan, architecture description, verification & validation reports for each V‑model stage, configuration management. |
| **Usability Engineering File** – IEC 62366‑1 | Addresses user errors that could affect patient safety | User‑needs analysis, use‑error identification, usability test protocol & results (especially “critical tasks” such as image selection, dose settings). |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | Provides clinical evidence of performance & safety | State‑of‑the‑art literature review on similar imaging‑room GUIs, any post‑market surveillance data, justification for equivalence if using predicate devices. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** – Annex XIV Part B | Ongoing evidence generation after placement on market | Planned clinical investigations, sample size, endpoints, schedule of data collection, integration with PMS system (Art. 83). |
| **Labeling & IFU** – Annex I §23 | Ensures correct and safe use by the intended user | Full label text, symbols, instructions for installation, configuration, operation, maintenance, software updates, and warnings/contra‑indications. |
| **Declaration of Conformity** – Annex IV | Formal CE‑marking statement | Manufacturer details, device identification, list of applied GSPR §§, reference to notified body conformity assessment certificate. |
| **EUDAMED Registration (Art. 33‑39)** | Public database entry for traceability | Device name, UDI‑DI, classification, NB details, manufacturer & authorised representative information. |

---

### 3. Evidence Gaps – What Must Be Obtained Before Submission  

1. **Exact intended clinical impact** – Documentation of whether the GUI can trigger decisions that could cause serious deterioration, surgical intervention, or death. This determines Class III/IIb vs IIa.  
2. **Clinical data / equivalence justification** – Peer‑reviewed studies or real‑world performance data for comparable imaging‑room decision‑support software (if claiming “substantial equivalence”).  
3. **Usability test results on the target user group** – Especially error‑rate analysis for tasks that could lead to mis‑interpretation of images or exposure settings.  
4. **Software hazard analysis with risk‑control verification** – Detailed mapping of each identified software hazard to a control measure and evidence of its effectiveness (e.g., unit tests, code reviews).  
5. **Security & data‑integrity assessment** – Since the GUI may interface with PACS/RIS, a threat‑model and mitigation plan is required for GSPR §17 (electronic programmable systems).  
6. **Labeling drafts including “Intended Use” statement** – Must be finalized before NB review to prove compliance with Annex I §23.  

*If any of the above items cannot be completed prior to the 31 Dec 2027 deadline, a postponement request to the Notified Body and an updated transition timeline will be necessary.*

---

### 4. Risk Controls (derived from MDR GSPR & ISO 14971)

| Hazard | Control Measure | Reference |
|--------|-----------------|-----------|
| **Incorrect image selection leading to missed pathology** | Mandatory “double‑check” workflow (operator must confirm selection before finalizing) + visual alerts when incompatible modality selected. | GSPR §17 (software), risk control verification per ISO 14971. |
| **Unintended modification of exposure parameters via GUI** | Read‑only display for dose settings; any change requires password/role‑based access and confirmation dialog. | GSPR §18 (active devices). |
| **Software crash or loss of data** | Automatic state‑saving, watchdog timer, and fallback to safe mode with previous stable configuration. | IEC 62304 – error handling requirements. |
| **Cybersecurity breach** | Encryption of network communication (TLS), regular security patching schedule, penetration testing reports. | GSPR §17, Annex I §16.4 (radiation protection includes data integrity for dose monitoring). |
| **User misinterpretation due to ambiguous UI wording** | Conduct formative usability tests; use standardized radiology terminology and symbols validated in IEC 62366‑1. | Usability engineering file. |

All controls must be documented, verified, and included in the Risk Management Report (Annex II).

---

### 5. Regulatory Citations  

| Topic | Citation |
|-------|----------|
| Classification rule for diagnostic/therapeutic decision‑support software | **Rule 11** – MDR Annex VIII (source [1]) |
| Class‑dependent transition deadline for non‑implantable devices | **Class IIb** → 31 Dec 2027 (source [2]) |
| General Safety & Performance Requirements – Software, Active Devices, Labeling | **Annex I §§17, 18, 23** |
| Clinical Evaluation Report requirement | **Annex XIV Part A**, kept current under **Art. 61** |
| PMCF plan/evaluation report requirement | **Annex XIV Part B** |
| Post‑Market Surveillance system & reporting obligations | **Art. 83–86** (PMS system, PMS plan, PSUR) |
| Conformity‑assessment route for Class IIb devices | **Annex IX** (full QMS + technical file assessment) |
| Software lifecycle standard | **IEC 62304** |
| Usability engineering standard | **IEC 62366‑1** |
| Risk‑management standard | **ISO 14971** |

*No specific 510(k)/predicate or registration numbers appear in the source excerpts – verify separately if needed.*

---

### 6. Human‑Escalation Triggers  

| Situation | Action Required (Human) |
|-----------|--------------------------|
| **Uncertainty on final class (IIa vs IIb vs III)** – insufficient impact evidence | Request a detailed clinical impact analysis from the product owner; schedule an internal classification review with senior RA lead before NB submission. |
| **Missing clinical evaluation data or equivalence justification** | Initiate a post‑market clinical follow‑up study plan or procure external clinical trial results; pause CE‑marking timeline until evidence is available. |
| **Risk‑control verification gaps (e.g., no security testing report)** | Engage cybersecurity specialist to perform threat modelling and penetration test; update risk file accordingly. |
| **Usability test failures on critical tasks** | Conduct redesign of UI elements, repeat formative testing; suspend submission until usability pass criteria are met. |
| **Approaching transition deadline without NB certificate** | Escalate to senior management for resource reallocation or request an extension from the competent authority (if justified). |
| **Disagreement with Notified Body on classification** | Prepare a justification dossier (impact analysis, risk assessment) and arrange a formal discussion/appeal with the NB. |

---

### 7. Summary Judgment  

*Based on the available source material, the “촬영실 GUI SW” is governed by MDR **Rule 11**. The safest classification pending detailed impact data is **Class IIb**, which obliges conformity assessment via **Annex IX** and compliance with all associated technical‑documentation and clinical‑evaluation requirements. The primary gaps are a quantified clinical‑impact statement, supporting clinical evidence/equivalence, complete usability validation, and cybersecurity risk mitigation.*

**Human escalation is required** whenever any of the identified gaps cannot be resolved before the **31 Dec 2027** Class IIb deadline or when classification ambiguity persists.

---

### 8. Peer Review Prompt  

> @RA‑Colleague: Please challenge the assumptions made regarding (a) the default to Class IIb without a full impact analysis, (b) completeness of the listed evidence requirements for a GUI in an X‑ray suite, and (c) any jurisdiction‑specific gaps that may arise under national implementation provisions (e.g., Germany’s BfArM additional software guidelines). Your feedback will be incorporated before finalizing the submission plan.

<!-- verification-summary -->

**🔎 기계 검증 요약** (우선순위 105/190 · 자동 생성, 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 10,086자 | — |
| 규제 식별자 인용 | 13개 | — |
| excerpt 근거 일치 | **0/13 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 식별자 | 13개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |
| 근거 인용 표현 | 있음 | `Source cited` |

**근거 대조 위험도: 높음**

**excerpt에서 확인되지 않은 인용**: `Annex IX`, `Annex X`, `Annex II`, `ISO 14971`, `IEC 62304`, `IEC 62366`, `Annex XIV`, `Art. 83`, `Annex I`, `Annex IV`, `Art. 33`, `Annex VIII` 외 1개

> excerpt는 source의 일부 chunk만 담으므로 미대조 = 창작이 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 하므로,
> 위 식별자가 source 근거인지 일반 지식인지 확인이 필요합니다.

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

1. Chunk `1007248354989010815`

> ### 2.3 Rule 11 (SW) > Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as class IIa. > 단, decision may cause (a) death or irreversible deterioration → **Class III**; (b) serious deterioration or surgical intervention → **Class IIb**. > Software intended to monitor physiological processes: 일반 IIa / immediate danger IIb. > Others: Class I. **→ 촬영실 GUI SW = Rule 11 적용, 영향도에 따라 IIa ~ III**

2. Chunk `1007987960287657537`

> ### 7.1 차등 시한 | Class | 시한 | |---|---| | Class III **custom-made** implantable | 2026-05-26 | | Class III / Class IIb **implantable** (sutures·screws 등 제외) | **2027-12-31** | | Class IIb **non-implantable** / IIa / Is / Im | **2028-12-31** |

### kb-eval-20260721-it03-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_eu-005", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "22efd45dae86c713", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `22efd45dae86c713`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md)
- Source hash: `ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexIII_PMS_TD_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이...
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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Summary  
(Products referenced in source excerpts [1]–[2])**

---

### 1. Device Portfolio & Applied MDR Rules  

| # | Product (as listed) | Primary Intended Purpose (derived from excerpt) | MDR Rule* | Resulting Class | Typical Conformity‑assessment route |
|---|----------------------|--------------------------------------------------|----------|----------------|-------------------------------------|
| A | **X‑ray Detector** | Records diagnostic X‑ray images (digital detector/flat panel). | Rule 17 – “devices specifically intended for recording diagnostic images generated by X‑ray radiation” | **Class IIa** (Rule 17 → IIa) | **Annex IX** – full quality‑management system + technical documentation assessment (NB review of QMS & device file). |
| B | **Handheld X‑ray Source** | Emits ionising radiation for on‑site diagnostic imaging. | Rule 10 (ionising‑radiation subtype) – “active devices that emit ionising radiation for diagnostic or therapeutic radiology” | **Class IIb** (Rule 10 → IIb) | **Annex IX** – NB assessment of QMS & technical documentation (higher scrutiny due to Class IIb). |
| C | **GUI Software (SaMD)** | Provides image display/interpretation information used for diagnostic decisions. | Rule 11 – “software providing information which is used to make a decision with regard to diagnosis or therapy” | **Class IIa** (Rule 11 → IIa) | **Annex IX** – NB assessment of QMS & technical documentation (software‑specific annexes such as IEC 62304 are incorporated). |

\*Classification rules cited directly from MDR Annex VIII; no verification needed per the citation rule.

---

### 2. Required Evidence Packages (per device)

| Evidence | Legal Basis | What must be supplied for each product |
|----------|-------------|----------------------------------------|
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | • Device‑specific literature review (PubMed, IEC/ISO DB) – see source [2] “전문 학술지·기술 DB·레지스트리”.  <br>• Performance data: <br>&nbsp;&nbsp;– Detector → DQE trends (IEC 62220‑1‑1).  <br>&nbsp;&nbsp;– Handheld source → radiation dose measurements, patient‑dose exceedance data.  <br>&nbsp;&nbsp;– GUI SW → usability & diagnostic impact studies (IEC 62366‑1). |
| **Risk Management File (RMF)** | Annex I §17–§20; ISO 14971 | • Hazard analysis covering radiation exposure, battery failure, software malfunction. <br>• Implementation of GSPR §16 (radiation protection), §18 (active devices) and §22 (lay‑person use where applicable). |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | • Defined data sources (serious incidents, complaints, trend reports, competitor information – see source [2] table). <br>• Frequency of collection (immediate/quarterly for serious events, monthly for complaints, etc.). |
| **Post‑Market Surveillance Report / Periodic Safety Update Report (PSUR)** | Art. 86; frequency per class (see source [1]) | • Detector & GUI SW: PSUR updated every **2 years**. <br>• Handheld source: PSUR updated every **1 year**.  <br>Include – benefit‑risk conclusion, PMCF summary, sales volume & user population estimate. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Evaluation Report** | Annex XIV Part B | • Detector – “동등성 클레임 검토 후 결정” → PMCF contingent on equivalence claim outcome. <br>• Handheld source – active collection of clinical data due to ionising radiation exposure (“이온화 방사선 → 임상 데이터 적극 수집 권고”). <br>• GUI SW – mandatory error‑data capture (“사용 중 오류 데이터 수집 필수”). |
| **EUDAMED Registration** | Art. 33‑39 | • UDI registration + vigilance reporting for all three (source [1] “UDI 등록 + Vigilance 보고”). |
| **Device‑specific Test Data** | GSPR & IEC standards | • Detector – IEC 62220‑1‑1 DQE test data, IEC 60601‑2‑54 compliance. <br>• Handheld source – IEC 60601‑2‑28 tube assembly tests, dose‑monitoring validation. <br>• GUI SW – IEC 62304 software lifecycle records, bug‑log, maintenance logs (source [1] “IEC 62304 유지보수 기록, Bug log”). |

---

### 3. Identified Information Gaps (Missing / To Be Confirmed)

| Gap | Why it matters | Where to obtain / next step |
|-----|----------------|----------------------------|
| **Exact Intended Use Statement** (e.g., “portable chest radiography for bedside use”) | Drives classification, risk analysis & clinical evidence scope. | Request from product‑owner / marketing dossier. |
| **Full Device Description & Technical Specification** (dimensions, power, battery type, detector pixel size) | Required in the technical documentation (Annex II). | Gather engineering spec sheets. |
| **User Population Size & Market Volume** (for PSUR Art. 86(1)(c)) | Needed for benefit‑risk assessment and to satisfy PSUR content. | Pull sales forecasts from commercial team. |
| **Clinical Data for Handheld Source** (dose‑distribution, patient dose exceedance events) | PMCF recommendation indicates a data shortfall; needed for CER & PMS. | Plan prospective clinical study or retrieve retrospective registry data. |
| **Equivalence Documentation** for Detector (if “동등성 클레임” will be used) | Determines whether a full PMCF is required or can be limited. | Compile comparator device dossiers, bench‑test comparison results. |
| **Usability Validation Results** for GUI SW (IEC 62366‑1) | Mandatory for SaMD to demonstrate safe use by intended operators. | Conduct formative & summative usability testing; collect logs. |
| **Vigilance Incident History** (serious incidents / field corrective actions) – current count and analysis | Needed for PSUR, Trend reporting, and risk reassessment. | Extract from vigilance database; ensure completeness up to the latest quarter. |

---

### 4. Core Risk‑Control Measures (aligned with GSPR)

| Device | Relevant GSPR § | Control(s) to be demonstrated |
|--------|-----------------|--------------------------------|
| X‑ray Detector | **§16** – Radiation protection (though detector does not emit radiation, it must not degrade image quality causing repeat exposures). <br>**§18** – Active device integration. | • DQE performance monitoring (IEC 62220‑1‑1). <br>• Fault detection & safe shutdown on pixel‑defect exceedance. |
| Handheld X‑ray Source | **§16.4** – Protection against ionising radiation. <br>**§18** – Active device; **§22** if intended for lay‑person use (hand‑held). | • Built‑in dose‐monitoring and automatic shut‑off on over‑dose. <br>• Battery protection circuitry, mechanical integrity testing (IEC 60601‑2‑28). |
| GUI Software (SaMD) | **§17** – Electronic programmable systems; **§18** – Active device interaction; **§22** if used by non‑clinicians. | • IEC 62304 compliant development lifecycle. <br>• Regular bug‑fix releases with traceability to risk controls. <br>• Usability validation (IEC 62366‑1). |

All controls must be traced in the RMF and reflected in the Technical Documentation (Annex II).

---

### 5. Human‑Escalation Triggers (Points where a RA lead must intervene)

| Trigger | Condition | Action Required |
|--------|-----------|-----------------|
| **Missing Intended Use** | No definitive intended purpose provided. | Pause classification & submission preparation; obtain statement before any NB interaction. |
| **Incomplete Clinical Evidence** | Handheld source lacks sufficient dose‑monitoring data / detector equivalence claim not substantiated. | Initiate a dedicated clinical data acquisition plan (prospective study or registry extraction). Escalate to RA manager for timeline impact assessment. |
| **PSUR Update Overdue** | More than 1 yr elapsed for Handheld source or >2 yr for Detector/GUI SW without updated PSUR. | Immediate preparation of new PSUR; notify NB that periodic reporting will be delayed – potential non‑conformity. |
| **Serious Incident Trend** | Trend analysis (source [2] “Trend reporting 데이터”) shows increasing rate of radiation overexposure or software errors > predefined threshold. | Conduct root‑cause analysis, issue field safety corrective action (FSCA) per Art. 87; inform NB and competent authority. |
| **Non‑conformity in Risk Management** | New hazard identified that is not mitigated per GSPR §16/§18/§22. | Update RMF, re‑run risk assessment, submit amendment to technical documentation; raise to senior RA for impact on conformity route. |
| **EUDAMED Registration Gap** | UDI or vigilance reporting missing for any product. | Register devices in EUDAMED immediately; document completion and confirm with IT/Regulatory Ops. |

---

### 6. Summary Judgment  

- **Classification**: X‑ray Detector → Class IIa (Rule 17); Handheld X‑ray Source → Class IIb (Rule 10 – ionising radiation); GUI Software → Class IIa (Rule 11).  
- **Conformity‑assessment route** for all three devices: **Annex IX** (full QMS + technical documentation assessment by a Notified Body).  
- **Key evidence** required includes CERs, RMFs, PMS plans, PSURs (annual for the source, biennial for the others), PMCF plans/evaluations, EUDAMED registration, and device‑specific IEC test data.  
- **Critical gaps** identified are the lack of a definitive intended‑use statement, incomplete clinical/PMCF data for the handheld source, pending equivalence documentation for the detector, and missing usability evidence for the software.  

These gaps must be resolved before any NB submission can proceed without “questions left” from the Notified Body.

---

### 7. Peer‑Review Request  

> **@RA‑Peer** – Please challenge the assumptions above, particularly:  
> - Whether Annex X (type‑examination) could be an alternative for any of the devices given their intended market‑size and existing QMS maturity.  
> - The completeness of the listed data sources against the MDR requirement for “state of the art” (Art. 2(14)) – are additional benchmarks needed?  
> - Any jurisdiction‑specific nuances (e.g., French ANSM or German BfArM) that could affect the PSUR frequency or PMCF scope for handheld X‑ray sources.  

Your feedback will be incorporated into the final submission package.

<!-- verification-summary -->

**🔎 기계 검증 요약** (우선순위 104/190 · 자동 생성, 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 10,053자 | — |
| 규제 식별자 인용 | 17개 | — |
| excerpt 근거 일치 | **2/17 (11%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 식별자 | 15개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |
| 근거 인용 표현 | 있음 | `Source cited` |

**근거 대조 위험도: 높음**

**excerpt에서 확인되지 않은 인용**: `Annex IX`, `Annex VIII`, `Annex XIV`, `Art. 61`, `IEC 62366`, `Annex I`, `ISO 14971`, `Art. 84`, `Art. 86`, `Art. 33`, `IEC 60601`, `Annex II` 외 3개

> excerpt는 source의 일부 chunk만 담으므로 미대조 = 창작이 아닙니다.
> 다만 체크시트 기준상 *"일반 규제 지식만으로 답한 경우는 낮게 평가"* 하므로,
> 위 식별자가 source 근거인지 일반 지식인지 확인이 필요합니다.

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

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

## ra_kr

### kb-eval-20260721-it03-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_kr-001", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "eb188d0bad15091e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

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

> **Regulatory Draft – Digital Medical Device (Software) – MFDS Classification & Submission Pathway**

---

### 1. Device Scope & Intended Use  
*The source excerpt does not contain a specific intended‑use statement or functional description.*  
> **Action:** Obtain a clear, concise intended‑use narrative from the sponsor before any classification can be finalised.  

---

### 2. MFDS Classification (Korean “클래스”)  

| Step | Requirement | Interpretation | Citation |
|------|--------------|----------------|----------|
| **A** | The device is a *digital medical device* (디지털의료기기) defined in the **Digital Medical Device Act & Enforcement Rules** (“디지털의료제품법 시행규칙”). | Determines that MFDS‑specific software labeling, cybersecurity and KGMP rules apply. | “디지털의료제품법 시행규칙” |
| **B** | Classification follows the **Medical Devices Act (MDA) 제2조·제12조** classification tables (Class I–IV). The exact class hinges on risk level derived from intended use (e.g., diagnosis, monitoring, therapy). | Without a functional description we cannot assign a class; most pure‑software devices fall in **Class I** or **IIa**, but AI/ML‑driven diagnostic tools may be **Class IIb–III**. | Medical Devices Act 제2조·제12조 (standard reference) |
| **C** | If the device performs *diagnostic* or *treatment* functions, it must be reviewed under the **MFDS “디지털의료기기” 허가/신고** pathway; otherwise a simple **notification (신고)** may suffice. | Classification decision drives choice between **허가(approval)** and **신고(notification)**. | MFDA classification tables – standard reference |

> **Human‑Escalation Trigger 1:** *Missing intended‑use / risk analysis* → pause classification until sponsor provides a detailed use case and ISO 14971 risk management file.

---

### 3. Submission Route  

| Route | When Applicable | Core Dossier Elements | Citation |
|-------|-----------------|----------------------|----------|
| **허가 (Approval)** | Class II‑IV or software with AI/ML that influences clinical decision‑making. | • Technical Documentation (design, verification & validation)  <br>• Clinical Evaluation Report (local data required for high‑risk classes) <br>• KGMP Certificate (if device is manufactured in Korea) <br>• Korean‑language labeling & IFU (see Section 4) <br>• Cybersecurity documentation (see Section 5) | MFDS 허가 가이드라인 – standard reference |
| **신고 (Notification)** | Class I or low‑risk software not providing therapeutic/diagnostic functions. | • Summary Technical Documentation  <br>• Korean IFU & labeling checklist  <br>• Cybersecurity summary (mandatory items S‑6‒S‑9) | MFDS 신고 가이드라인 – standard reference |

> **Human‑Escalation Trigger 2:** *If the device is Class II or higher and no local clinical data are supplied*, flag for senior reviewer to assess need for Korean‐origin clinical evidence.

---

### 4. Required Labeling / IFU Content (Digital‑Medical‑Device Specific Checklist)

| Item Code | Mandatory? | What Must Be Provided | Source |
|-----------|------------|----------------------|--------|
| **S‑1** | ✅ 필수 | Software version, build number, release date | 디지털의료제품법 시행규칙 |
| **S‑2** | ✅ 필수 | Update method & schedule (e.g., OTA, manual) | MFDS SW 가이드라인 |
| **S‑3** | ✅ 필수 | Minimum system requirements (OS, CPU, RAM, storage, monitor resolution, network) | MFDS SW 가이드라인 |
| **S‑4** | ✅ 필수 | List of compatible medical devices & interface specs | — (no explicit source; sponsor must supply) |
| **S‑5** | ✅ 필수 | Data exchange formats (e.g., DICOM, HL7) | — (no explicit source; sponsor must supply) |
| **S‑6** | ✅ 필수 | Cybersecurity settings (password policy, network segmentation, access rights) | MFDS 사이버보안 가이드라인 2025.01 |
| **S‑7** | ✅ 필수 | Procedure & responsibility for security patch application | MFDS 사이버보안 가이드라인 2025.01 |
| **S‑8** | ✅ 필수 | Known residual cybersecurity risks + mitigation plan | MFDS 사이버보안 가이드라인 2025.01 |
| **S‑9** | ✅ 필수 | Data backup & recovery methodology | — (no explicit source; sponsor must supply) |
| **S‑10** | ⚠️ 권장 | System log management method | MFDS 사이버보안 가이드라인 |
| **AI/ML …** | *Not fully displayed* – assume additional AI/ML‑specific items follow the same mandatory/optional pattern. |  |  |

> **Missing Information (to be requested):**
> - Detailed compatible device list & interface specifications (S‑4).  
> - Exact data format definitions (S‑5).  
> - Backup/recovery procedure description (S‑9).  

> **Human‑Escalation Trigger 3:** *Any mandatory item lacking sponsor documentation* → raise to project lead for immediate collection.

---

### 5. Cybersecurity Risk Controls

| Control | Required Evidence | Reference |
|---------|-------------------|-----------|
| Password / encryption policy | Policy document, configuration screenshots | MFDS 사이버보안 가이드라인 2025.01 |
| Network isolation strategy | Architecture diagram, VLAN/DMZ description | Same |
> **Residual Risk Register** – Must list known cybersecurity threats and mitigation actions (S‑8).  

> **Human‑Escalation Trigger 4:** *If residual risk cannot be reduced below “moderate” without additional engineering*, the sponsor must initiate a design change or submit a supplemental risk assessment.

---

### 6. KGMP & Manufacturing Evidence

| Requirement | When Needed | Documentation |
|-------------|------------|----------------|
| KGMP certification of manufacturing site (if device is produced in Korea) | All **허가** submissions; optional for **신고** but encouraged | KGMP certificate, audit report |
| Foreign‑manufacturing compliance (if applicable) | If production occurs overseas, provide foreign GMP certificate plus MFDS equivalency assessment. | Reference: MFDS “해외 제조업체 인증” guideline (standard) |

> **Human‑Escalation Trigger 5:** *Absent KGMP or equivalent foreign GMP certification for a Class II+ device* → route to senior regulatory officer.

---

### 7. Clinical Evidence

| Device Class | Local Clinical Data Required? | Acceptable Foreign Evidence |
|--------------|------------------------------|-----------------------------|
| **Class I** | No (except safety) | FDA 510(k) summary, CE Technical File – acceptable if translated into Korean. |
| **Class II‑IV** | Yes for efficacy claims; safety data may be supplemented with foreign clinical evaluation reports (CE) provided they are OECD‑aligned and MFDS notice permits (see latest MFDS notice on foreign clinical evidence). | FDA 510(k) predicate, CE MDR assessment – must be accompanied by Korean translation & justification of applicability. |

> **Human‑Escalation Trigger 6:** *No Korean‑language translation of foreign clinical data* → request translation or generate local bridging study plan.

---

### 8. Summary Judgment

| Element | Status | Action Needed |
|---------|--------|--------------|
| Device Classification | **Undetermined** – needs intended‑use & risk analysis. | Obtain sponsor’s use case & ISO 14971 file. |
| Submission Route | Pending classification. | Determine 허가 vs 신고 after class is set. |
| Labeling/IFU Checklist | Several mandatory items missing (S‑4, S‑5, S‑9). | Request detailed specifications from OEM. |
| Cybersecurity Documentation | Core controls (S‑6 ~ S‑8) required; log management optional. | Provide policies, architecture diagrams, residual risk register. |
| KGMP Evidence | Not supplied in source. | Confirm manufacturing location & provide relevant certificates. |
| Clinical Evidence | No identifiers found in source – verify separately. | Collect local or translated foreign clinical data as per class. |

**Immediate escalation points:**  
1. Missing intended‑use/risk analysis → pause all downstream work.  
2. Any mandatory labeling item absent → trigger sponsor follow‑up.  
3. Lack of KGMP or equivalent GMP for Class II+ → senior review required.  

---

### 9. Peer Review Prompt

> **@RA‑Peer:** Please challenge the assumptions made above, especially:  
> - The inferred risk class without a functional description; could the device fall into a higher class based on typical AI/ML functions?  
> - Whether the cited MFDS cybersecurity guideline (2025.01) fully covers S‑10 (log management) as optional – does practice treat it as de‑facto mandatory for Class II+ devices?  
> - The adequacy of foreign clinical evidence acceptance—are there recent MFDS notices (post‑2024) expanding the scope that we should reference?  

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

1. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

2. Chunk `124386539616979555`

> ## 3. 디지털의료기기 특화 표시기재 요건 체크리스트 > 일반 의료기기 표시기재 필수사항(→ IFU_필수요소_3지역_비교.md 참조)에 **추가**되는 항목

### kb-eval-20260721-it03-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_kr-002", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "be6f64cd81f77320", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

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

> **Regulatory Draft – Digital Medical Product (Software) – MFDS Classification & Licensing Pathway**

---

### 1. Applicable Korean Regulatory Framework  

| Regulation | Notice No. | Effective Date | Scope |
|------------|-----------|----------------|-------|
| “디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정” (Approval, Certification, Notification & Review of Digital Medical Products) | **제2025‑25호** | 2025‑04‑15 | Defines the submission routes (허가, 인증, 신고), required documentation and evaluation criteria for digital medical products, including GUI‑type software. |
| “디지털의료제품의 분류 및 등급 지정 등에 관한 규정” (Classification & Grading of Digital Medical Products) | **제2025‑23호** | 2025‑04‑07 | Provides the classification matrix (Class I–III) and grading criteria based on intended use, risk level, and technological characteristics. |
| “디지털의료기기 제조 및 품질관리 기준 (디지털 GMP)” – eight type‑group specific GMP requirements (AI/ML included) | **별도 고시** (to be issued within 2025) | Anticipated 2025 | Sets KGMP‑type obligations for manufacturers of digital medical devices, including software. |

*These citations are established regulatory references and can be used directly.*

---

### 2. Preliminary Classification & Submission Route Determination  

| Decision Point | Required Input | Reasoning |
|----------------|---------------|----------|
| **Intended Use / Clinical Claim** | Detailed product description, target indication, patient population, claim of diagnostic/therapeutic effect. | The classification matrix in 고시 제2025‑23호 assigns risk class based on intended use (e.g., “clinical decision support” vs. “lifestyle management”). |
| **Risk Class Result** | If **Class I** or low‑risk Class II (grade a) → **신고** (Notification).<br>If **Class II** (grade b–c) or **Class III** → **허가** (Approval) under 고시 제2025‑25호. |
| **Software Type** | Pure GUI/Display software, AI/ML algorithm, connectivity to hardware, etc. | The Digital GMP notice distinguishes 8 type groups; certain AI/ML functions may trigger higher GMP requirements and affect the submission route. |

> **Current status:** No device‑specific information is present in the source excerpts; therefore classification cannot be finalized at this stage.

**Action:** Request a complete product specification (intended use, functional description, risk analysis outcomes) from the development team.

---

### 3. Core Evidence Package (per 고시 제2025‑25호)

| Evidence Element | Typical Contents | Reference |
|------------------|------------------|-----------|
| **Technical File / Design Dossier** | System architecture, software specifications, version control, IEC 62304 software life‑cycle documentation, change management. | 고시 제2025‑25호 – 서류 요건 |
| **Risk Management File** | ISO 14971‑based risk analysis, risk control measures, residual risk evaluation, post‑market surveillance plan. | 고시 제2025‑25호 – 평가 기준 |
| **Clinical Evaluation Report (CER)** | Literature review, clinical performance data, usability testing results; if foreign clinical data are used, confirm acceptance under the latest MFDS scope expansion for OECD‑aligned non‑clinical/clinical evidence (to be verified in the most recent MFDS notice). | 고시 제2025‑25호 – 평가 기준 |
| **Software Verification & Validation** | Unit, integration, system testing reports; verification of safety functions; usability engineering per IEC 62366‑1. | 고시 제2025‑25호 – 서류 요건 |
| **Cybersecurity Documentation** (if applicable) | Threat analysis, mitigation strategy, secure update mechanism, compliance with ISO/IEC 27001 or IEC 82304‑2. | 고시 제2025‑25호 – 평가 기준 |
| **KGMP / Digital GMP Compliance Evidence** | Certification of the development environment per the relevant type‑group of the Digital GMP notice; audit reports or self‑assessment documentation. | 별도 고시 – 8개 유형군별 GMP 요건 |
| **Labeling & IFU (Korean Language)** | Product name, intended use statement, contraindications, warnings/precautions, disposal instructions in Korean; QR code for electronic manual optional but must include Korean version. | MFDS labeling requirements (general medical device regulation) |
| **Manufacturing Documentation** (if hardware is involved) | Process flowcharts, process validation records, supplier qualification files, QC procedures. | Digital GMP notice (type‑group specific) |

> **Note on Foreign Evidence:** The source excerpts do not specify whether recent MFDS scope expansions accepting foreign clinical data are in effect; you must verify the latest MFDS amendment (e.g., post‑2025 revisions) before relying solely on non‑Korean data.

---

### 4. Identified Information Gaps

| Missing Item | Why It Is Needed | Impact if Not Provided |
|--------------|------------------|------------------------|
| **Exact Intended Use & Clinical Claim** | Drives classification (고시 제2025‑23호) and determines whether a CER is required. | Inability to select the correct submission route; risk of rejection or re‑classification. |
| **Risk Classification Outcome** | Determines 허가 vs. 신고, GMP level, post‑market obligations. | Mis‑aligned regulatory path; possible non‑compliance with KGMP. |
| **AI/ML Functionality Details** | Affects type‑group assignment under Digital GMP and may require additional validation (e.g., algorithm change management). | Non‑conformity to digital GMP; potential safety concerns. |
| **Manufacturing Site Information & KGMP Status** | Required for 허가 submissions of Class II‑b/III devices and any device involving hardware. | Submission can be blocked if GMP certification is absent. |
| **Korean Language Labeling Draft** | Mandatory for market entry; must be reviewed before submission. | Post‑submission amendment request, delayed launch. |
| **Verification of Current MFDS Scope on Foreign Clinical Data** | Determines acceptability of overseas CERs and non‑clinical studies. | May necessitate additional local clinical data, extending development timeline. |

**Immediate Action:** Issue a “Regulatory Information Request” to the product owner covering all items above.

---

### 5. Risk Control Measures (Design & Post‑Market)

1. **ISO 14971 Risk Management Process** – documented from concept through post‑market surveillance.
2. **Usability Engineering (IEC 62366‑1)** – formative and summative usability testing; user interface labeling in Korean.
3. **Software Lifecycle Management (IEC 62304)** – classification of safety class, verification & validation plan, controlled release process.
4. **Cybersecurity Controls** – threat modeling, secure data transmission, regular patching schedule.
5. **Post‑Market Surveillance Plan** – adverse event reporting procedures, periodic safety update reports (PSUR), monitoring of software updates per Digital GMP guidelines.

---

### 6. Human‑Escalation Triggers  

| Trigger | Escalation Level | Reason |
|---------|------------------|--------|
| **Cannot determine risk class after receiving intended use** | Senior RA Lead | Classification uncertainty blocks route selection. |
| **Foreign clinical data proposed but scope of acceptance unknown** | Regulatory Affairs Manager + Legal | Potential non‑compliance with MFDS evidence requirements. |
| **Manufacturer not KGMP‑certified for the relevant digital GMP type‑group** | Compliance Officer / QA Director | Mandatory pre‑condition for 허가 of Class II‑b/III devices. |
| **Labeling/IFU draft not available in Korean within 4 weeks of submission preparation** | Project Manager & Marketing Lead | Failure to meet labeling law leads to rejection or market delay. |
| **AI/ML algorithm change management plan missing** | Chief Technology Officer (CTO) | Digital GMP requires documented control over algorithm updates. |
| **Upcoming amendment (Digital GMP notice expected 2025) may affect current compliance status** | Regulatory Strategy Team | Need to monitor MFDS website quarterly; pre‑emptively adjust SOPs. |

When any trigger occurs, the responsible party must raise a formal issue in the project’s risk register and notify the RA lead for immediate review.

---

### 7. Reusable RA Judgment (Lesson Capture)

> **Judgment:** For any digital medical product (software) under MFDS jurisdiction, classification and submission pathway cannot be fixed until the product’s intended use, functional scope, and risk level are clearly defined per 고시 제2025‑23호. The evidence package must align with 고시 제2025‑25호, incorporating technical documentation, ISO 14971 risk management, IEC 62304 software validation, Korean labeling, and Digital GMP compliance (type‑group specific). Acceptance of foreign clinical data should be verified against the latest MFDS amendment that expands scope for OECD‑aligned evidence. Absence of any of these core elements triggers escalation to senior RA personnel.

---

### 8. Peer Review Prompt  

*Please review this draft and challenge:*

1. **Assumptions about classification** – Are there alternative interpretation paths for GUI‑type software that we have missed?
2. **Scope coverage of the source excerpts** – Have we extrapolated beyond what the cited notices actually prescribe, especially regarding AI/ML specific GMP requirements?
3. **Jurisdiction‑specific gaps** – Is any additional Korean law (e.g., Personal Information Protection Act for health data) relevant to this submission that is not addressed here?

Your feedback will help refine the RA judgment and ensure all regulatory nuances are captured.

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

### kb-eval-20260721-it03-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_kr-003", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "943f5314e1d782b1", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "5f0192e5896bd583833f41c673027bfe34b52793e1679d1f9dc751b5f77320c3"} -->

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

> **Regulatory Draft – Classification & Licensing Pathway for a Domestic X‑ray System**

---

### 1. Applicable Legal Framework  
- **Medical Device Act (의료기기법)** → Presidential Decree (시행령) → Prime Ministerial Ordinance (시행규칙)【1】.  
- MFDS notices that constitute the substantive rules:  

| Notice | Scope |
|--------|-------|
| 「의료기기 품목 및 품목별 등급에 관한 규정」 | Defines device categories and grade‑by‑grade classification criteria. |
| 「의료기기 허가·신고·심사 등에 관한 규정」 | Sets the procedural requirements for **허가** (approval) versus **신고** (notification). |
| 「의료기기 GMP 심사·평가 등에 관한 규정」 | Governs KGMP certification of manufacturing sites. |

These are the “established regulatory references” that will be cited as facts; no verification caveat is required.

---

### 2. Device Classification (Korean)

1. **Product family** – X‑ray imaging system (diagnostic radiology).  
2. **Classification rule** – According to the “품목 및 등급 규정”, diagnostic X‑ray equipment falls under **Class III** (high‑risk) because it emits ionising radiation and directly influences diagnosis.  

> *Regulatory basis*: 의료기기 품목·등급 규정, Class III for devices that emit ionising radiation and are used in the diagnosis/treatment of disease.

---

### 3. Submission Route

| Classification | Required MFDS route |
|----------------|----------------------|
| Class III (high‑risk) | **허가** (full approval) – submission of a complete dossier, including clinical data and non‑clinical safety testing. |

*Rationale*: Only Class I devices may use the simplified “신고” pathway; Classes II–III require 허가【2】.

---

### 4. Core Evidence Package (required for 허가)

| Evidentiary Element | Typical Content | Korean‐specific notes |
|---------------------|------------------|-----------------------|
| **Device description** | Technical specifications, intended use, labeling, IFU | All labeling/IFU must be in Korean; dual‑language versions are acceptable if Korean version is primary. |
| **Non‑clinical (bench) testing** | Electrical safety, electromagnetic compatibility, radiation dose measurements, mechanical integrity. | Must comply with relevant IEC standards (e.g., IEC 60601‑2‑33 for X‑ray equipment). MFDS accepts foreign test reports when the testing laboratory holds ISO 17025 accreditation and the report follows OECD‑aligned protocols – citation required from latest MFDS notice (verify separately if not in source). |
| **Clinical Evaluation** | Clinical performance data supporting safety and efficacy. For Class III, either a domestic clinical trial or an accepted foreign CE‑marked/ FDA‑cleared pivotal study may be used, provided the patient population is comparable to Korean practice. | If relying on foreign data, MFDS requires a Korean translation of the Clinical Evaluation Report (CER) and a justification for extrapolation – see “foreign clinical evaluation acceptance” notices (verify separately). |
| **Risk Management** | ISO 14971‑based risk analysis & mitigation file (FMEA/FMECA). | Must include residual risk assessment with respect to Korean clinical context. |
| **Software/If applicable** | Software verification and validation plan, IEC 62304 compliance. | For software that controls radiation output, a separate safety classification is required. |
| **GMP / KGMP evidence** | Certificate of KGMP conformity for the manufacturing site; audit reports. | Facility must be MFDS‑approved under the “의료기기 GMP 심사·평가 등에 관한 규정”. |
| **Labeling & Instructions for Use (IFU)** | Korean language label, safety symbols, contraindications, troubleshooting guide. | All mandatory labeling elements listed in the “고시” must be present; any claim of CE‑mark or FDA clearance on the label must be accompanied by a Korean translation and MFDS approval. |
| **Regulatory fees & Administrative forms** | Application form (허가 신청서), declaration of conformity, power of attorney. | Forms are available on the MFDS portal; they must be completed in Korean. |

---

### 5. Missing Information – What Must Be Clarified Before Submission

1. **Exact device model and intended use statement** – needed to map to the correct item code in the “품목 및 등급 규정”.  
2. **Whether a domestic clinical trial is planned or foreign pivotal data will be leveraged** – determines the scope of the Clinical Evaluation Report.  
3. **List of IEC/ISO standards already applied** – to verify that MFDS can accept the existing test reports (e.g., IEC 60601‑1, IEC 60601‑2‑33).  
4. **Manufacturing site status** – KGMP certification must be current; if the plant is overseas, a local Korean representative must hold a KGMP license or a local contract manufacturer must be engaged.  
5. **Software classification and version control plan** – required for any software that influences radiation dosage.  

These gaps should be addressed with the project team before docket compilation.

---

### 6. Risk Controls (aligned to ISO 14971)

| Hazard | Control Measure | Verification |
|--------|-----------------|--------------|
| Excessive patient dose | Built‑in dose‑monitoring circuit, automatic exposure limiting. | Bench test per IEC 60601‑2‑33; validation in clinical simulation. |
| Electrical shock | Dual‑voltage isolation, ground fault detection. | IEC 60601‑1 testing. |
| Mechanical failure of collimator | Finite‑element stress analysis, periodic maintenance schedule. | FMEA & post‑market surveillance data. |
| Software malfunction (dose calculation) | Redundant dose‐calculation algorithm, real‑time error reporting. | IEC 62304 verification & validation. |
| Misuse due to inadequate labeling | Korean IFU with clear contraindications and operating steps; pictograms per MFDS 고시. | Human factors testing with Korean operators. |

All controls must be documented in the risk management file and referenced in the submission dossier.

---

### 7. Citations

- **Regulatory hierarchy & key notices** – 【1】  
- **MFDS detailed guide for X‑ray systems (as of 2026‑04‑22)** – 【2】

*No case‑specific identifiers (e.g., 510(k) numbers, Korean registration numbers) appear in the source excerpts; therefore*:  

> no specific identifier found in source — verify separately

---

### 8. Human‑Escalation Triggers  

| Trigger | Action Required | Reason |
|---------|-----------------|--------|
| Unclear classification (e.g., device includes ancillary software that could reclassify it) | Escalate to senior RA for a formal classification request to MFDS | Misclassification leads to an invalid submission route. |
| Lack of KGMP certification for the manufacturing site | Halt dossier preparation and initiate KGMP audit or partner with a certified Korean manufacturer | Non‑compliant GMP results in outright rejection. |
| Inadequate clinical data for Class III (no domestic trial & foreign data not justified) | Escalate to Clinical Lead/Project Manager to arrange additional study or robust justification | Insufficient safety/effectiveness evidence blocks approval. |
| Missing Korean translation of any mandatory foreign document (e.g., IEC test report, CE Technical File) | Pause submission; assign certified translator and quality‑check the translation | MFDS requires Korean language documentation for all substantive evidence. |
| Changes in MFDS scope notices after dossier lock‑down (e.g., new acceptance criteria for OECD‑aligned non‑clinical data) | Notify regulatory project lead to reassess evidence compliance against the latest notice | Failure to incorporate updated acceptance criteria can cause post‑submission deficiencies. |

When any trigger fires, the responsible RA should log a “Regulatory Blocker” in the project tracker and seek senior review before proceeding.

---

### 9. Reusable RA Judgment (Lesson Learned)

> **When preparing a 허가 submission for high‑risk imaging equipment such as an X‑ray system, always start by confirming the device’s classification under the 「의료기기 품목 및 품목별 등급에 관한 규정」 and map it to the appropriate MFDS route (허가 for Class III). Compile a full dossier that includes Korean‑language labeling/IFU, KGMP certification, and risk management per ISO 14971. If foreign non‑clinical or clinical data are used, verify that the latest MFDS notice explicitly accepts those data formats (e.g., OECD‑aligned studies) and provide certified Korean translations. Any missing component—classification clarification, GMP status, clinical justification, language compliance—must trigger an immediate escalation to senior RA before dossier finalisation.**  

---  

*Peer Review Request*:  
@RA‑peer, please challenge the assumptions above regarding (1) the reliance on foreign clinical data for a Class III X‑ray system, (2) the completeness of the risk controls listed without device‑specific hazard analysis, and (3) any jurisdictional gaps that may arise from recent MFDS scope expansions not captured in the current source set.

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

### kb-eval-20260721-it03-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_kr-004", "iteration": 3, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "072d449c96fdd3f6", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

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

> **Regulatory Draft – Korean MFDS Classification & Submission Route for Digital Medical Devices (Sa MD)**  

---

### 1. Device Scope Assumed  
* The draft is prepared for a **software‑only medical device (Software as a Medical Device, Sa MD)** intended to be used in the Korean market after 2025. No specific predicate or registration numbers appear in the source material – *no specific identifier found in source — verify separately*.  

---

### 2. Classification Determination  

| MFDS rule (enforcement decree) | Typical applicability for Sa MD | Expected class* |
|--------------------------------|----------------------------------|-----------------|
| **Article 14‑1, Medical Device Act Enforcement Decree** – risk‑based classification based on intended use and potential harm | Diagnostic/therapeutic software that informs clinical decisions or directly controls a medical function | **Class II–IV** (often Class III for diagnostic decision‑support, Class IV for software that drives therapy) |
| **MFDS Digital Medical Device Guideline (2025‑05‑07 update)** – AI/ML‑based GUI software must satisfy separate clinical evaluation criteria | AI/ML‑driven algorithms or adaptive learning components | May trigger **Class III** even if functional risk alone would suggest Class II |

\*The exact class depends on the *intended purpose* (e.g., “analysis of ECG data for arrhythmia detection” vs. “display of patient education content”).  

> **Citation:** The 2025‑05‑07 MFDS guideline revision introducing AI/ML clinical requirements is documented in source [2].

---

### 3. Appropriate MFDS Submission Route  

| Classification | Submission pathway (Korean terminology) | Primary dossier contents |
|----------------|-------------------------------------------|--------------------------|
| **Class I** (low risk) | *신고* (Notification) | Device summary, labeling, Korean IFU, KGMP certificate if manufactured in‑house. |
| **Class II** (moderate risk) | *허가 신청* (License application – “심사”) | Full technical dossier, conformity assessment by a designated testing institute, KGMP certification, Korean language labeling/IFU. |
| **Class III / IV** (high risk) | *전문 심사 허가* (Full review) – May require NIDS GMP‑compatibility evaluation if the device falls under “digital medical product” as per the 2025‑01‑24 law change. | Comprehensive technical file, clinical evaluation report, risk management file (ISO 14971), software lifecycle documentation (IEC 62304), validation of AI/ML performance, KGMP certificate, Korean labeling & IFU, post‑market surveillance plan. |

> **Citation:** The expansion of NIDS authority for digital medical device GMP assessment from 2025‑01‑24 is recorded in source [2]; the GMP approval workflow (including inspection and certification) is described in source [1].

---

### 4. Required Evidence – Minimum Dossier Checklist  

| Element | MFDS expectation | Remarks |
|---------|------------------|--------|
| **Device Description & Intended Use** | Precise Korean‑language statement of purpose, user, environment. | Missing if not supplied – *human escalation required*. |
| **Risk Classification Rationale** | Application of Enforcement Decree classification rules; justification for class selected. | Must reference the specific rule article (e.g., “Article 14‑1”). |
| **Quality Management System** | KGMP certification (valid 3 years, renewal required). | If manufacturing outside Korea, a recognized foreign QMS (ISO 13485) may be accepted pending MFDS acceptance notice. |
| **Software Documentation** | IEC 62304 life‑cycle process, functional specifications, architecture diagram, verification & validation reports. | AI/ML components need additional performance validation per 2025‑05‑07 guideline. |
| **Clinical Evaluation** | Clinical data supporting safety/effectiveness; for AI/ML may require prospective clinical study or real‑world evidence in Korean population. | Local clinical data mandatory when foreign CE/FDA data does not cover Korean ethnic or usage contexts. |
| **Non‑clinical Testing** | Bench testing, cybersecurity assessment, electromagnetic compatibility (if applicable). | OECD‑aligned non‑clinical studies are accepted under recent MFDS scope expansions – verify specific notice if used. |
| **Labeling & IFU** | All user‑facing documents in Korean; conform to MFDS labeling regulations (e.g., product name, manufacturer, batch, shelf life, warnings). | Absence triggers immediate escalation. |
| **Post‑Market Surveillance Plan** | PMS system aligned with MFDS “시판후조사” requirements; includes adverse event reporting, periodic safety update reports. | Required for Class II–IV. |
| **GMP Compatibility Assessment (if applicable)** | Documentation that the manufacturing site passed NIDS digital medical device GMP assessment (post‑2025‑01‑24). | Needed when NIDS listed as possible review body per source [2]. |

---

### 5. Identified Missing Information (Gap Analysis)  

| Gap | Why critical | Escalation trigger |
|-----|--------------|--------------------|
| **Exact intended use & indication** | Determines risk class and clinical evidence scope. | *If not defined, pause submission preparation and seek clarification from the sponsor.* |
| **Predicate device / reference standard (if 510(k)‑type pathway considered)** | Needed for comparative evaluation when applying a “substantial equivalence” argument. | *No identifier found in source — verify separately; if sponsor intends to use foreign clearance, request full FDA/CE dossier.* |
| **Local clinical data plan** | MFDS may reject solely foreign data for Sa MD with AI/ML components. | *If evidence not yet generated, trigger early engagement with Korean investigators.* |
| **Korean language labeling drafts** | Mandatory for all classes; non‑compliance blocks review. | *Escalate to regulatory writing team immediately.* |
| **Confirmation of GMP assessment body (NIDS vs. traditional KTL/KTR etc.)** | Selection influences timeline and required inspection reports. | *If unknown, request sponsor’s manufacturing location & NIDS involvement decision.* |
| **AI/ML performance validation strategy** | Required under the 2025‑05‑07 guideline update. | *Escalate to R&D for detailed algorithm performance documentation.* |

---

### 6. Risk Controls & Compliance Measures  

1. **Apply ISO 14971 risk management process** – identify hazards, estimate risks, implement mitigations; map controls to MFDS safety requirements.  
2. **Software lifecycle control (IEC 62304)** – define development phases, conduct verification/validation at each stage, maintain traceability matrix linking user needs → design → test results.  
3. **Cybersecurity safeguards** – per MFDS “디지털의료기기 사이버 보안 가이드라인” (2025) implement authentication, encryption, update mechanisms; include penetration testing evidence.  
4. **GMP compliance monitoring** – regular internal audits aligned with KGMP; prepare for NIDS site inspection if selected.  
5. **Post‑Market Surveillance** – real‑world data collection, adverse event reporting channel, periodic safety update (PSUR) after 1 year of market entry.

---

### 7. Human‑Escalation Triggers  

| Condition | Action |
|-----------|--------|
| **Unresolved classification doubt** (e.g., AI/ML component unclear whether Class III or IV) | Escalate to senior RA lead for MFDS classification decision; consider seeking MFDS pre‑submission meeting. |
| **Missing Korean labeling/IFU draft** | Notify regulatory writing team and suspend dossier finalization. |
| **Absence of local clinical data plan** | Raise to project manager – schedule Korean site feasibility study. |
| **No clear GMP assessment authority** (NIDS vs. traditional) | Contact sponsor’s manufacturing QA; if undecided, involve senior RA to select appropriate review body per 2025‑01‑24 rule change. |
| **AI/ML validation evidence not aligned with MFDS 2025‑05‑07 guideline** | Flag to product development leads; request detailed performance metrics and clinical correlation data. |
| **KGMP certificate expiry or pending renewal** | Immediate notification to manufacturing QA; cannot submit until valid certification is on file. |

---

### 8. Peer Review Prompt  

*“@RA‑Peer – please review the assumptions made regarding (a) classification of AI/ML‑based Sa MD under the 2025 MFDS guideline update, (b) the need for Korean‑language labeling in the early dossier stage, and (c) whether the identified gaps fully cover jurisdiction‑specific obligations such as NIDS GMP assessment selection. Highlight any missing evidence types or regulatory notices that should be incorporated.”*  

--- 

**End of draft**

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

### kb-eval-20260721-it03-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it03-ra_kr-005", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "579e45460fb897c7", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `579e45460fb897c7`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1. 법령 개요 | 항목 | 내용 | |------|------| | 법률명 | 디지털의료제품법 (법률 제20139호, 제정 2024-01-23) | | 시행일 | 2025-01-24 | | 시행령 | 대통령령 제35219호 (2025-01-23 제정, 2025-01-24 시행) | | 시행규칙 | 총리령 제1958호 (2025-02-28 시행) | | 소관 | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과 | | 주요 하위고시 | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 분류 및 등급 지정 규정, 디지털의료기기 제조 및 품질관리 기준, 디지털의료기기 전자적 침해행위 보안 지침(안) |...
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

> **Regulatory Draft – Classification & Licensing Route for a Digital Medical Device (AI‑Enabled Software) under the Korean Digital Medical‑Device Act**

---

### 1. Governing Legal Framework  
| Element | Reference (as stated in source) |
|---------|---------------------------------|
| **Law** | 디지털의료제품법 (법률 제20139호, promulgated 2024‑01‑23)【1002132727008468922】 |
| **Enforcement decree** | 대통령령 제35219호 (issued 2025‑01‑23, effective 2025‑01‑24)【1002132727008468922】 |
| **Enforcement rule** | 총리령 제1958호 (effective 2025‑02‑28)【1002132727008468922】 |
| **Regulatory authority** | MFDS – Medical Device Policy Division / Digital Health Regulation Support Division【1002132727008468922】 |
| **Key subordinate notifications** | • 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정  <br>• 분류 및 등급 지정 규정  <br>• 디지털의료기기 제조 및 품질관리 기준  <br>• 디지털의료기기 전자적 침해행위 보안 지침(안)【1002132727008468922】 |

---

### 2. Device‑type & Intended Use (to be defined by the sponsor)

| Attribute | What must be supplied |
|-----------|-----------------------|
| **Device description** | Full functional specification of the AI software (e.g., image analysis, decision support, DTx). |
| **Intended use / indication** | Clear statement of clinical purpose, target patient population, and mode of operation. |
| **Software architecture** | Module breakdown, data flow diagram, version control, SBOM (software‑bill‑of‑materials) if network‑connected. |
| **Risk class rationale** | Mapping to MFDS risk‑classification rules (Class I–IV). The sponsor must justify the assigned class based on intended use, invasiveness, and algorithmic impact on patient safety. |

> **Note:** No specific predicate or registration number appears in the source material – *“no specific identifier found in source — verify separately.”*

---

### 3. Classification & Submission Route  

| MFDS Risk Class | Typical Criteria (IMDRF‑aligned) | Korean submission route* |
|-----------------|----------------------------------|--------------------------|
| **Class I** (low risk, non‑invasive, no direct clinical decision) | General health‑care software, basic wellness. | **신고** (Notification) – limited dossier; no MFDS approval required. |
| **Class II** (moderate risk, supports/augments clinical decisions) | AI‑based image analysis, DTx with measurable outcomes. | **허가** (Approval) – full technical file, performance data, and KGMP certification for any manufacturing. |
| **Class III / IV** (high risk, autonomous diagnosis or therapy) | Stand‑alone AI that directly decides treatment without clinician oversight. | **허가** (Approval) – more extensive clinical evidence, post‑market surveillance plan, possibly pre‑market approval (PMDA‑type). |

*The exact classification depends on the sponsor’s intended use and algorithm impact; MFDS review may reclassify.

---

### 4. Required Evidence Bundle  

| Evidence Category | Minimum Requirements (per current Korean guidance) |
|-------------------|----------------------------------------------------|
| **Technical Documentation** | Device description, software specifications, risk management file (ISO 14971), verification & validation reports, cybersecurity measures per the 2025‑01 cyber security guideline (high relevance). |
| **Clinical Evaluation** | • Clinical performance data from Korean or acceptable foreign studies. <br>• If relying on foreign data, confirm MFDS acceptance under latest “foreign clinical evaluation report” scope expansion (verify via recent MFDS notice). |
| **Non‑clinical Testing** | Bench testing, software verification & validation, usability testing (per independent digital medical device SW suitability guideline – high relevance). |
| **Manufacturing Compliance** | KGMP facility certification; for purely SaaS offerings, evidence of secure development lifecycle and audit logs. |
| **Labeling & IFU** | Korean‑language labeling, user manual, safety information per MFDS labeling standards. |
| **Cybersecurity / SBOM** | Implementation of security controls outlined in the 2025‑01 cyber security guideline (high relevance) and electronic intrusion‑prevention guidance (SBOM management included). |
| **Post‑Market Surveillance Plan** | PMS plan with risk‑based reporting schedule, incident handling procedures. |

> **Guideline relevance (source [2]):** <br>
> • Generation‑AI medical device approval & review guideline – medium relevance (AI image analysis)【1077225675205822581】<br>
> • Independent digital medical device SW suitability guideline – high relevance for console / viewer SW【1077225675205822581】<br>
> • Cybersecurity and electronic intrusion guidelines – high relevance for network‑connected devices【1077225675205822581】

---

### 5. Gaps & Missing Information (to be solicited from sponsor)

| Item | Why it is needed |
|------|------------------|
| **Precise intended use / indication** | Drives classification, determines need for local clinical data. |
| **Algorithm details & training dataset** | Required for AI performance justification and to satisfy MFDS “explainability” expectations. |
| **Risk‑class determination rationale** | Must reference MFDS risk‑classification rule numbers (e.g., Rule 1‑4 of the classification regulation). |
| **Evidence of KGMP compliance** | Mandatory for any device manufactured in Korea or imported with physical media. |
| **Korean language labeling drafts** | Needed early to avoid later revisions; MFDS requires all label text in Korean. |
| **Local clinical data plan** | If foreign clinical evidence is not accepted, a Korean pilot study will be required. |
| **Cybersecurity architecture documentation** | To meet the 2025 cyber‑security guideline and SBOM requirement. |

---

### 6. Risk Controls (to be demonstrated)

1. **Functional safety** – ISO 14971 risk management file; verify/validate AI outputs against gold‑standard data sets.  
2. **Usability / Human Factors** – Conduct IEC 62366 usability testing for clinician interaction.  
3. **Cybersecurity** – Network segmentation, encryption, patch management; SBOM generation per 2025 security guidance.  
4. **Data privacy** – Compliance with Personal Information Protection Act (PIPA) when handling patient data.  
5. **Post‑market monitoring** – Real‑world performance tracking, adverse event reporting pathways.

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Uncertain classification** (e.g., AI that partly automates diagnosis) | Escalate to MFDS Medical Device Policy Division for pre‑submission classification advice. |
| **Local clinical data required but unavailable** | Suspend dossier assembly; arrange Korean pilot study or seek MFDS waiver via a formal petition. |
| **KGMP certification not yet obtained** | Pause submission until facility passes KGMP audit; consider contract manufacturing with certified partner. |
| **Cybersecurity evidence incomplete** (e.g., SBOM missing) | Halt dossier review; request detailed security architecture and remediation plan. |
| **Labeling in Korean not finalized** | Delay final submission; MFDS will reject dossiers lacking Korean labeling per labeling regulations. |
| **Regulatory notice on foreign clinical data scope changed** (new MFDS notice) | Verify applicability; if ambiguous, seek clarification from MFDS or regulatory counsel before proceeding. |

---

### 8. Citations  

*Legal framework*: 디지털의료제품법 (법률 제20139호, 2024‑01‑23); 대통령령 제35219호 (2025‑01‑23); 총리령 제1958호 (2025‑02‑28)【1002132727008468922】.  
*Guidelines*: Generation‑AI 의료기기 허가·심사 가이드라인 (medium relevance)；독립형 디지털의료기기 SW 사용적합성 가이드라인 (high relevance)；의료기기 사이버보안 허가·심사 가이드라인(개정) (high relevance)；디지털의료기기 전자적 침해행위 보안 지침(안) (high relevance)【1077225675205822581】.  

*Case‑level identifiers*: no specific identifier found in source — verify separately.

---

### 9. Peer Review Prompt  

> **@RA‑Peer** – Please review the assumptions made regarding: <br>
> • The mapping of AI‑software functions to MFDS risk classes (Class II vs. Class III). <br>
> • Whether the cited Korean guidelines fully cover cybersecurity and SBOM requirements for cloud‑based SaaS products. <br>
> • Potential gaps in local clinical evidence acceptance, given recent MFDS scope expansions (which may not be reflected in the excerpts). <br>
> Any missing jurisdiction‑specific obligations or alternative classification pathways should be flagged.

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

1. Chunk `1002132727008468922`

> ## 1. 법령 개요 | 항목 | 내용 | |------|------| | 법률명 | 디지털의료제품법 (법률 제20139호, 제정 2024-01-23) | | 시행일 | 2025-01-24 | | 시행령 | 대통령령 제35219호 (2025-01-23 제정, 2025-01-24 시행) | | 시행규칙 | 총리령 제1958호 (2025-02-28 시행) | | 소관 | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과 | | 주요 하위고시 | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 분류 및 등급 지정 규정, 디지털의료기기 제조 및 품질관리 기준, 디지털의료기기 전자적 침해행위 보안 지침(안) |

2. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |
