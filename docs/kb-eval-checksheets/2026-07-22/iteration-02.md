# KB Eval Checksheet - 2026-07-22 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260722-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_us-001", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f4afc0898d20c8fb", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

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

> **Regulatory Draft – 510(k) Predicate‑Strategy Blueprint**

| Item | Assessment / Action | Basis |
|------|---------------------|-------|
| **1. Device Classification & Submission Pathway** | • Determine the product’s **device class** by cross‑referencing its intended use and technology with the FDA device classification database (21 CFR 807). <br>• If the device is a **Class II** imaging, storage or communication system, the applicable special control is found in **21 CFR 892** (e.g., §892.2050 for image‑management software). <br>• For non‑imaging Class II devices the default route is a **Traditional 510(k)**; for novel Class III technology consider **De Novo** or **PMA** if no appropriate predicate exists. | 21 CFR 807 (submission); 21 CFR 892 (imaging) |
| **2. Predicate Device Identification** | • Search the FDA 510(k) database using keywords that match the new device’s technology and intended use. <br>• Populate a **Substantial‑Equivalence Comparison Table** per eSTAR guidance (Step 2 of the submission flow). | Source excerpt [2] – “Predicate Device 조사 (FDA 510(k) Database)” |
| **3. Required Evidentiary Package** | • **510(k) Summary** (per §807.92) <br>• **Device Description & Indications for Use** – follow the eSTAR template (eSTAR_01_Device_Description_IFU) (Step 1 of source). <br>• **Performance Testing** – bench, safety, and if applicable, clinical data demonstrating equivalence to predicate. <br>• **Biocompatibility** – per ISO 10993‑1 (referenced in 21 CFR 820). <br>• **Electromagnetic Compatibility / RF Emissions** – per IEC 60601‑1‑2 (cited under “전자파” in source). <br>• **Software Validation** (if software) – include verification/validation plan, and a **Predetermined Change Control Plan (PCCP)** for AI/ML updates (FDA Guidance Dec 2024). | 21 CFR 807; ISO 10993‑1; IEC 60601‑1‑2; PCCP guidance |
| **4. Missing Information (to be supplied by sponsor)** | • **Exact Intended Use & Indications** – needed for classification and predicate match.<br>• **Device Technology Description** (hardware, software modules, imaging modality, etc.).<br>• **Proposed Predicate 510(k) Numbers** – none identified in source; “no specific identifier found in source — verify separately.”<br>• **Risk Management File** – ISO 14971 analysis with identified hazards and mitigations.<br>• **Labeling & IFU Drafts** – to satisfy 21 CFR 801. | Source provides only procedural steps, not device‑specific data. |
| **5. Risk Controls (per ISO 14971 & QMSR)** | • Perform **Hazard Identification** → **Risk Estimation** → **Risk Evaluation** → **Risk Control Measures** (protective labeling, safety interlocks, software error handling). <br>• Implement a **Design History File (DHF)** and **Device Master Record (DMR)** in compliance with **21 CFR 820** (QMSR effective Feb 2026). <br>• For AI/ML components, embed a **PCCP** that pre‑authorises permissible algorithmic updates. | 21 CFR 820; ISO 14971; PCCP guidance |
| **6. Human‑Escalation Triggers** | 1. **Unresolved Classification** – if device does not clearly map to an existing CFR part or class, pause and seek FDA “Q‑Submission” for classification request.<br>2. **No Adequate Predicate** – inability to locate a predicate with same intended use/technology; consider De Novo pathway; escalate to senior regulatory lead.<br>3. **Insufficient Performance Data** – gaps in bench or safety testing that prevent demonstration of substantial equivalence; trigger escalation to engineering for test plan revision.<br>4. **Missing Risk Management Evidence** – incomplete ISO 14971 file; pause submission preparation.<br>5. **Regulatory Change Control** – any planned post‑market software change not covered by the PCCP must be flagged and reviewed before inclusion in the 510(k). | Internal risk‑escalation policy (no external citation required) |
| **7. Citations Summary** | • Classification & submission rule: **21 CFR 807**, **21 CFR 892** (where applicable). <br>• Quality System: **21 CFR 820**. <br>• Biocompatibility: ISO 10993‑1. <br>• EMC/EMI: IEC 60601‑1‑2. <br>• AI/ML change control: **Predetermined Change Control Plan (PCCP)** – FDA final guidance Dec 2024. | Established regulatory references (Rule 1). No case‑level identifiers found in source — “no specific identifier found in source — verify separately.” |

---

**Peer Review Prompt**

> *Colleague, please challenge the assumptions above: Is the reliance on 21 CFR 892 appropriate without a confirmed imaging modality? Are there any overlooked FDA programs (e.g., Special 510(k) or Abbreviated Pathway) that could accelerate clearance for a software‑only device? Verify whether the eSTAR template aligns with current FDA electronic submission standards (eCTD vs. 510(k) E‑submission). Also confirm that all cited standards are still current as of FY 2026.*

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

### kb-eval-20260722-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_us-002", "iteration": 2, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "c5264cbb7637ac12", "source": "github:holee9/MD-process/issue-drafts/959_FDA_510k_RTA_기초보강_3주차_재이월.md", "source_hash": "a1390fed4a348d82a21f4d285d1ac98116b6aaa3b15e4ccdb5e57413d03ac232"} -->

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

> **Regulatory Draft – 510(k) Predicate‑Strategy Assessment**

---

### 1. Bottom‑Line Judgment  
*The current submission (#951 – draft status, 2026‑07‑03) cannot be advanced to a final 510(k) clearance because the device’s **type, intended use, and functional description** are missing from the source material.*  

Without this core information we cannot:

* assign a correct product classification (e.g., Class II under 21 CFR §892.2050 for medical‑image‑management software or another class),  
* identify an appropriate predicate device, or  
* define the scope of required performance, benchtop, and clinical evidence.

**Action:** Pause any further work on this submission until the above gaps are filled.  

---

### 2. Classification & Submission Route (What We Need)

| Decision Point | Required Information | Likelihood (given no data) |
|----------------|----------------------|----------------------------|
| **Product classification** – determine CFR part & section (e.g., §892.2050 for PACS‑type software, §862.xxx for clinical chemistry) | Device name, technology description, intended medical purpose, patient population | Unknown – cannot assign |
| **510(k) pathway** – standard 510(k) vs. special/abbreviated or De Novo | Whether the device is substantially equivalent to an existing legally marketed device; novelty of technology; presence of recognized predicate | Unclear – pending classification and predicate search |

*Regulatory citations (established references):*  
- Premarket notification requirements: **21 CFR §807**.  
- Imaging‑device classifications (if applicable): **21 CFR Part 892**, e.g., §892.2050 for medical image management systems (Class II).  

---

### 3. Required Evidence Once Device Is Defined

| Evidence Category | Typical Requirement (per 510(k) guidance) |
|-------------------|--------------------------------------------|
| **Device description** | Detailed specification, block diagram, software architecture (if applicable). |
| **Intended use & labeling** | Clear indication statements, user instructions – see **21 CFR §801**. |
| **Predicate comparison** | Side‑by‑side table covering function, technology, performance specs; justification of substantial equivalence. |
| **Bench testing** | Electrical safety (IEC 60601‑1), electromagnetic compatibility (IEC 60601‑1‑2), software verification/validation (if SaMD). |
| **Performance testing** | Accuracy, precision, repeatability per recognized standards (e.g., AAPM TG‑102 for imaging systems). |
| **Non‑clinical safety** | Biocompatibility (ISO 10993) where patient contact occurs. |
| **Clinical data** *(if needed)* | Pilot or pivotal study demonstrating clinical performance comparable to predicate; IRB approval and informed consent documentation. |
| **Risk management** | ISO 14971‑aligned risk analysis, including identified hazards, severity, probability, and mitigations. |
| **QMS compliance** | Certificate of registration with FDA’s QMS Regulation (**21 CFR §820**) – effective Feb 2026. |

*Note:* The new Quality Management System Regulation (QMSR) aligns with ISO 13485; evidence of compliance must be included in the submission package.

---

### 4. Missing Information (What Must Be Provided)

| Gap | Why It Matters |
|-----|----------------|
| **Device function & technology** | Determines classification, applicable standards, and predicate search. |
| **Intended use statement** | Required for labeling (§801) and to frame the substantial‑equivalence argument. |
| **Regulatory history of comparable devices** (cleared 510(k)s, K numbers) | Needed to construct a credible predicate chain. |
| **Risk analysis summary** | Demonstrates that hazards have been identified & mitigated per ISO 14971; required for both 510(k) and QMSR compliance. |
| **Evidence of QMS compliance** (e.g., audit reports, certificates) | FDA audit sweep diverted QA resources—must be documented before resubmission. |
| **Software description (if applicable)** – architecture, version control, change‑control plan | If the device includes AI/ML, a Predetermined Change Control Plan (PCCP) is required per FDA guidance Dec 2024. |

---

### 5. Core Risk Controls (to be incorporated once device details are known)

1. **Design Controls** – per 21 CFR §820.30 (design inputs, outputs, verification, validation).  
2. **Software Change Management** – Predetermined Change Control Plan (PCCP) for AI/ML updates.  
3. **Usability Engineering** – apply IEC 62366‑1 to mitigate user error.  
4. **Electromagnetic Compatibility & Electrical Safety** – IEC 60601 series testing.  
5. **Data Security & Privacy** – HIPAA compliance, encryption of PHI per 45 CFR §164. |  

---

### 6. Citations (per instruction)

| Item | Citation Type | Reference |
|------|---------------|-----------|
| FDA 510(k) regulatory framework | Established reference | **21 CFR §807** |
| Imaging‑device classification example (PACS software) | Established reference | **21 CFR Part 892, §892.2050** |
| Quality Management System Regulation (effective Feb 2026) | Established reference | **21 CFR §820** |
| Predetermined Change Control Plan (AI/ML) | Established reference | FDA Final Guidance, Dec 2024 – “Predetermined Change Control Plan (PCCP)” |
| Case‑level identifier for the current draft submission | Specific identifier (from source) | **#951 (2026‑07‑03 registration, draft status)** – see Source Excerpts [1] & [2] |

*No additional predicate K‑numbers or cleared 510(k) identifiers appear in the provided source; verification will be required once device specifics are obtained.*

---

### 7. Human‑Escalation Triggers

| Trigger | Escalation Point |
|---------|------------------|
| **Absence of device description/intended use** after request → **Immediate pause** of submission activities; notify Project Lead & Regulatory Manager. |
| **QMS audit findings unresolved** (audit sweep diverted QA) → **Escalate to Quality Assurance Director** for corrective action plan before resubmission. |
| **Unclear classification** after attempted predicate search → **Consult FDA Division of Industry and Consumer Affairs (DICA)** for formal classification request. |
| **Regulatory deadline risk** (e.g., submission scheduled >30 days without required data) → **Escalate to Senior RA Lead** to re‑prioritize resources. |

---

### 8. Peer Review Prompt
*“@RA‑Peer: Please challenge the assumptions made above regarding the need for a complete device description before any classification can be assigned, and assess whether any interim regulatory pathways (e.g., special 510(k) or abbreviated review) could be justified based solely on the limited information currently available in the source.”*

--- 

*End of draft.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 72/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,769자 | — |
| 규제 식별자 인용 | 11개 | — |
| source excerpt 근거 일치 | **0/11 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 11개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `ISO 10993` | ISO 10993 | 의료기기 생물학적 안전성 평가 — ISO 14971 위험관리에 반영 |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §892.2050`, `21 CFR §807`, `21 CFR Part 892`, `21 CFR §801`, `21 CFR §820`, `21 CFR §820.30`
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

1. Chunk `243090506975535922`

> ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **3주 연속 0% 정체** (06-26 / 07-03 / 07-10 동일). #951(2026-07-03 등록)이 미착수 상태로 재이월됨.

2. Chunk `608844759849194169`

> ## 이관 배경 - 선행 이슈: #951 (2026-07-03 등록, status: draft, 착수 실적 없음) - 원인 추정: 이번 주 개발/QA 인력이 감사(audit) sweep(01_법규_규제, 02_품질경영시스템_QMS)에 전량 투입되어 체크리스트 보강 착수 못함

### kb-eval-20260722-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_us-003", "iteration": 2, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "15448c50d07bbbce", "source": "github:holee9/MD-process/issue-drafts/979_FDA_510k_RTA_기초보강_4주차_재이월.md", "source_hash": "74bd6ad69e69c2f46c80904e3f16f85e423e7f85f008ac16cad2d4c86bf6e79b"} -->

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

> **510(k) Predicate‑Strategy Draft – Regulatory Outline**

---

### 1. Device Scope & Classification (to be confirmed)

| Item | Current Status | Action Required |
|------|----------------|-----------------|
| **Device type / function** | Not disclosed in source | Obtain a concise description of the device’s primary technology and clinical role (e.g., “software for automated detection of pulmonary nodules on CT”). |
| **Intended use statement** | Missing | Draft a clear intended‑use claim matching the functional claims of any potential predicate. |
| **Regulatory panel & CFR part** | Unknown – likely imaging‑related → **21 CFR Part 892** (radiology/imaging) if device performs image acquisition, processing, or analysis; otherwise verify against other panels. | Confirm whether the device falls under Part 892 (e.g., §892.2050 for image‑management software). |
| **Classification** | Unclear – could be Class II (most imaging software) but must be verified. | Conduct a “product code” search in FDA’s 510(k) database using the finalized intended use to locate the appropriate classification and confirm the required special controls. |

*If no suitable predicate exists after the product‑code search, prepare for a **De Novo** request (21 CFR 814).*

---

### 2. Submission Route & Core Elements

| Requirement | Typical Evidence | Source‑based Gap |
|-------------|------------------|------------------|
| **510(k) submission** – Form FDA 510(k), cover letter, table of contents | Device description; comparison to predicate (side‑by‑side table); labeling; intended use; summary of safety & effectiveness data. | No predicate or device description identified → **Missing**. |
| **Device Description (§807.92)** | Detailed specifications, hardware/software architecture, accessories, accessories list. | Missing. |
| **Predicate Comparison (§807.93(b))** | Identification of cleared predicate (510(k) number, product code); equivalence rationale; differences & mitigations. | No specific identifier found in source — verify separately. |
| **Performance Testing** | • Bench functional testing (accuracy, precision, repeatability).<br>• Clinical performance / validation study if software‑as‑a‑medical‑device (SaMD) or AI/ML.<br>• Electrical safety & EMC (if applicable). | No data provided – **Missing**. |
| **Software Documentation** (if applicable) | • Software Development Lifecycle (SDLC) plan.<br>• Verification & validation reports.<br>• Cybersecurity risk assessment (ISO 14971‑derived).<br>• *Predetermined Change Control Plan (PCCP)* for AI/ML updates – FDA Guidance Dec 2024. | No software documentation noted – **Missing**. |
| **Biocompatibility** (if patient‑contacting) | ISO 10993 testing summary. | Not addressed – **Missing** if applicable. |
| **Sterilization & Shelf Life** (if a sterile device) | Validation data, packaging description. | Not addressed – **Missing** if applicable. |
| **Labeling (§801)** | Labels, IFU, promotional material, UDI placement per **21 CFR 830** (label must bear a UDI; see §§ 830.10‑830.60). | No labeling draft supplied – **Missing**. |
| **Quality Management System (QMSR) compliance** | Conformance to **21 CFR Part 820** (new QMSR, ISO 13485‑aligned, effective Feb 2026). Include Design History File (DHF) sections A/B/C as referenced in internal task list. | DHF structure mentioned but not populated – **Missing**. |
| **UDI Assignment** | Device Identifier & Production Identifier per **21 CFR 830.10‑830.60**, registration in GUDID (§830.300‑830.360). | No UDI plan provided – **Missing**. |

---

### 3. Risk Management (ISO 14971 / FDA expectations)

1. **Hazard Identification & Risk Analysis** – Create a risk file linking each identified hazard to:
   - Likelihood of occurrence.
   - Severity of possible harm.
2. **Risk Controls** – Include design controls, software safeguards, user interface warnings, and post‑market surveillance plans.
3. **Residual Risk Evaluation** – Demonstrate that residual risks are acceptable in the context of intended use.
4. **Verification of Controls** – Provide test data or simulation results confirming effectiveness.

*Reference:* **21 CFR 820.30(c)** (design controls) & FDA guidance on “Design Control Guidance for Medical Device Manufacturers” (2005, reaffirmed 2023).

---

### 4. Evidentiary Gaps & Immediate Actions

| Gap | Why It Matters | Recommended Action |
|-----|----------------|--------------------|
| **Device description & intended use** | Determines classification, predicate search, and required testing. | Collect/confirm a one‑sentence intended‑use claim; draft detailed device specification. |
| **Predicate identification** | Core of 510(k) substantial equivalence argument. | Search FDA 510(k) database using product code once intended use is defined; record the cleared 510(k) number(s). |
| **Performance data** | Supports safety & effectiveness claim. | Develop bench protocol and, if necessary, a pivotal clinical validation plan (protocol draft, statistical analysis plan). |
| **Software documentation / PCCP** | Required for AI/ML or any SaMD; ensures FDA can pre‑authorize future algorithm updates. | Prepare SDLC artifacts, verification/validation reports, and a PCCP outlining anticipated changes and control methods. |
| **QMSR/DHF sections A–C** | New QMS regulation (effective Feb 2026) mandates documented design history. | Populate DHF with design inputs, outputs, verification, validation, risk management files; assign responsible personnel. |
| **UDI strategy** | Mandatory labeling & GUDID registration. | Generate a UDI label layout complying with §§ 830.10‑830.60; plan for issuance through an FDA‑accredited issuing agency. |

---

### 5. Citations (Established Regulatory References)

- **21 CFR Part 807** – Premarket notification (510(k)) requirements.  
- **21 CFR Part 892** – Radiology/imaging device classification; e.g., §892.2050 for medical image‑management software (if applicable).  
- **21 CFR Part 820** – Quality Management System Regulation (QMSR) effective Feb 2026, ISO 13485‑aligned.  
- **21 CFR Part 830** – Unique Device Identification system; labeling requirements in §§ 830.10‑830.60; GUDID registration §§ 830.300‑830.360.  
- **Predetermined Change Control Plan (PCCP)** – FDA final guidance, Dec 2024 (AI/ML software change management).  
- **ISO 14971** – Application of risk management to medical devices (risk analysis & controls).  

*No specific 510(k) numbers or case identifiers were present in the source excerpts; verification will be required once device details are supplied.*

---

### 6. Human‑Escalation Triggers

| Condition | Escalation To |
|-----------|---------------|
| **Unresolved classification** after product‑code search (cannot confirm Part 892 vs another panel). | Senior Regulatory Affairs Lead – classification decision. |
| **No viable predicate identified** within a reasonable search window (≥3‑month effort). | Initiate De Novo pathway discussion with regulatory counsel and senior management. |
| **Critical performance data gaps** (e.g., no bench test results for a safety‑critical function). | Project Manager – pause timeline; allocate resources for testing plan. |
| **Incomplete DHF/QMSR documentation** that would prevent FDA acceptance of design controls. | Quality System Manager – enforce QMS compliance before submission preparation. |
| **UDI issuance blocked** due to lack of accredited issuing agency or GUDID account setup. | Regulatory Compliance Officer – coordinate with agency and initiate UDI registration process. |
| **Pending AI/ML algorithm change without a PCCP** in place. | Software Lead & Regulatory Affairs – develop and obtain FDA sign‑off on the PCCP before any model update. |

---

### 7. Peer Review Prompt

> **Request:** Please review this draft for (1) completeness of assumed regulatory pathway given the limited source information, (2) potential jurisdictional gaps (e.g., if the device falls outside Part 892), and (3) adequacy of identified evidentiary requirements relative to typical 510(k) submissions for imaging‑related devices. Highlight any missing citations or alternative strategies that should be considered.

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 71/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,243자 | — |
| 규제 식별자 인용 | 12개 | — |
| source excerpt 근거 일치 | **0/12 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 12개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 10993` | ISO 10993 | 의료기기 생물학적 안전성 평가 — ISO 14971 위험관리에 반영 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR Part 892`, `Part 892`, `21 CFR 814`, `21 CFR 830`, `21 CFR Part 820`, `21 CFR 830.10`, `21 CFR 820.30`, `21 CFR Part 807`, `21 CFR Part 830`
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

1. Chunk `1133221829333770557`

> ## 개요 FDA 510(k) 평가는 2026-06-26 채점 보정 이후 **4주 연속 0% 정체** (06-26 / 07-03 / 07-10 / 07-17 동일). #951(07-03) → #959(07-10)에 이어 3연속 이관, 이번 주도 착수 실적 없음.

2. Chunk `1104470705522628403`

> ## 필수 작업 1. 14개 미충족 must 항목 중 최소 3건 착수 2. 기술 파일 구조(DHF section A/B/C) 기초 문서화 3. RTA 리뷰 체크포인트 수립 4. 감사 sweep과 체크리스트 보강 작업의 인력 배분 분리(전담 1인 배정 검토)

### kb-eval-20260722-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "22bb65aae6d9e5ef", "source": "github:holee9/MD-process/issue-drafts/220_13_FDA_510k_RTA_핵심양식_초안.md", "source_hash": "2b2e64ed872d9caf987e923334f8bb1dab23e1f65d28ac42a81828e751edceb2"} -->

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

> **Regulatory Draft – 510(k) Submission Readiness Assessment**

| Item | Findings / Recommendation |
|------|----------------------------|
| **Device Classification & Sub‑mission Route** | • Classification cannot be assigned from the source excerpt. The device’s intended use, functional description, and technology must be identified to locate the appropriate CFR part (e.g., imaging devices → 21 CFR §892; clinical chemistry → §862). <br>• If the device is Class II, a traditional 510(k) under **21 CFR §807** is the primary pathway. |
| **Current Readiness Score** | • Automated “build_readiness.py” generated an overall FDA‑510(k) **Readiness‑to‑Accept (RTA) score of 52 %**. <br>• Five mandatory (“must”) items are unmet, which will trigger a **Refuse to Accept (RTA)** determination if submitted as‑is. |
| **Regulatory Basis for RTA** | Refuse‑to‑Accept authority is codified in **21 CFR §807.91** – “Refusal of Premarket Notification Submissions.” This provision permits FDA to reject a 510(k) that does not meet required content or formatting criteria. |
| **Missing / Incomplete Elements (the “5 must items”)** | The source does not list the specific deficiencies. Typical mandatory elements include: <br>1. Device description & intended use statement<br>2. Predicate device comparison (substantial equivalence)<br>3. Performance testing data (bench, animal, clinical as appropriate)<br>4. Labeling (including UDI per **21 CFR §830.10‑§830.70**) <br>5. Quality System documentation (QMSR, **21 CFR §820**, effective 02‑Feb‑2026) <br><br>*Action*: Obtain the detailed “must” checklist from the internal readiness report and map each to the corresponding regulatory requirement. |
| **Required Evidence for a Complete 510(k)** | • **Device Description & Intended Use** – clear, concise statement aligning with FDA guidance.<br>• **Predicate Device Identification** – complete comparison table demonstrating substantial equivalence; include predicate’s 510(k) number if available (not found in source).<br>• **Performance Testing** – bench‑top accuracy, precision, safety testing per device type; clinical data where needed.<br>• **Labeling Package** – IFU, labeling, and UDI label complying with **21 CFR §830.10–§830.70** and **21 CFR §801** (labeling).<br>• **Quality System Documentation** – ISO‑13485‑aligned QMSR compliance per **21 CFR §820**, including design controls, risk management (ISO 14971) and, if applicable, a Predetermined Change Control Plan (PCCP) for AI/ML components (**FDA Guidance Dec 2024**). |
| **Risk Controls & Standards** | • Perform a risk analysis per **ISO 14971**; identify hazardous situations and implement mitigations.<br>• Apply appropriate consensus standards (e.g., IEC 60601‑1 for electrical safety, IEC 62304 for software lifecycle) – verify which are referenced in the device’s classification rule. |
| **Projected Impact of Resolving the 5 Must Items** | The source cites an expected rise in RTA score from **52 % → ≈85 %** once the five deficiencies are corrected. This suggests that the remaining 15 % of requirements are already satisfied or will be addressed later (e.g., post‑market surveillance plan). |
| **Human‑Escalation Triggers** | 1. **Unresolved Mandatory Items** – If any of the five must items cannot be remedied within the project timeline, immediately notify the Project Lead and consider a supplemental submission or De Novo request if classification is unclear.<br>2. **Classification Ambiguity** – Absence of clear device function/indication should trigger escalation to senior RA for panel determination (e.g., Part 892 vs. Part 862).<br>3. **Predicate Device Gap** – If a suitable predicate cannot be identified, flag for evaluation of alternative pathways (De Novo, PMA).<br>4. **QMSR Non‑Compliance** – Any deficiency in ISO 13485‑aligned quality system documentation must be escalated to Quality Assurance. |
| **Next Steps** | 1. Retrieve the full “must‑item” checklist from the readiness tool.<br>2. Populate a gap‑analysis matrix linking each item to its CFR/standard citation.<br>3. Draft or update the predicate comparison, performance data package, labeling, and QMSR artifacts accordingly.<br>4. Re‑run the readiness assessment after gaps are closed; target ≥ 85 % score before formal 510(k) submission. |
| **Peer Review Prompt** | *Please challenge: (a) the assumption that all five missing items map to typical mandatory 510(k) elements, (b) the completeness of the evidence list given the unknown device type, and (c) any jurisdiction‑specific considerations (e.g., state‑level regulations or FDA’s updated QMSR requirements) that may have been omitted.* |

---  
*No specific 510(k) identifiers or predicate numbers appear in the source excerpts – verify separately.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 70/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 4,819자 | — |
| 규제 식별자 인용 | 12개 | — |
| source excerpt 근거 일치 | **0/12 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 12개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §892`, `21 CFR §807`, `21 CFR §807.91`, `21 CFR §830.10`, `21 CFR §820`, `21 CFR §801`, `Part 892`, `Part 862`
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

1. Chunk `322119354378516559`

> ## 배경 `build_readiness.py` 결과 FDA 510(k) RTA 점수 52% 고착. 하기 5개 must 항목이 미충족 상태로 실제 제출 시 FDA RTA(Refuse to Accept) 직행.

2. Chunk `607901765257522135`

> ## 예상 효과 FDA 510(k) 점수 52% → 약 85% (5개 must 해소 시)

### kb-eval-20260722-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_us-005", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "76c4047eeb4ef5c9", "source": "github:holee9/MD-process/issue-drafts/931_RA_FDA_Form_표지_양식_4건_작성.md", "source_hash": "68cd74d39caaa060d4323f37a5c193a02284866bee050ec5139fdf5916ca6ff7"} -->

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

> **Regulatory Draft – 510(k) Predicate Strategy**

---

### 1. Classification & Submission Route
| Item | Determination | Basis |
|------|---------------|-------|
| **Device class** | *Undetermined – requires clarification of device type and intended use.* | FDA classification is hinged on the device’s technology (e.g., imaging → 21 CFR §892, electrophysiology → 21 CFR §882). Without a functional description we cannot assign a class. |
| **Premarket pathway** | Traditional 510(k) – 21 CFR §807 | The source lists the required FDA Forms (3514, 3601, 3654, 3881) that constitute a standard 510(k) submission package. |
| **Regulatory framework** | QMSR (ISO 13485‑aligned) – 21 CFR §820 (effective Feb 2026) | All new device submissions must be supported by an FDA‑compliant quality management system under the updated QMS Regulation. |
| **UDI requirement** | Mandatory – 21 CFR §830 | Labeling must contain a UDI per §§830.10–830.60 and be submitted to GUDID (§830.300–§830.360). |

---

### 2. Evidence Required for Substantial Equivalence  
*(Assuming a Class II device as the most common outcome for new medical image‑processing software, but adjust once technology is known.)*

| Evidence Category | Typical Content | Regulatory Reference |
|-------------------|-----------------|----------------------|
| **Device description & intended use** | Detailed specification, accessories, indications, contraindications. | 21 CFR §807.92 (Content of a 510(k)). |
| **Predicate device(s)** | FDA‑cleared 510(k) numbers, registration number, and summary of technological characteristics. | 21 CFR §807.87 (Identification of predicate). |
| **Performance testing** | • Bench/bench‑top functional verification<br>• Safety testing (electrical, thermal, RF as applicable)<br>• Software validation (verification & validation per IEC 62304) | FDA Guidance on “Software Validation for Medical Devices” and 21 CFR §820.30. |
| **Clinical data** (if needed) | Non‑clinical comparability & limited clinical study or literature supporting intended use equivalence. | FDA Guidance “Deciding When to Submit Clinical Data in a 510(k).” |
| **Risk analysis** | ISO 14971 risk management file with identified hazards, mitigations, and residual risk justification. | 21 CFR §820.30 (Design Controls). |
| **Labeling & IFU** | Device labeling, contraindications, warnings, intended user population. | 21 CFR §801 (Labeling). |
| **Sterilization validation** *(if applicable)* | Sterility assurance level data, packaging integrity testing. | FDA Guidance “Medical Device Packaging.” |
| **Software Change‑Control Plan** | Predetermined Change Control Plan (PCCP) if the device incorporates AI/ML components. | FDA Final Guidance December 2024 – “Predetermined Change Control Plan (PCCP).” |
| **UDI submission** | Device Identifier (DI), Production Identifier(s) (PI), and electronic record for GUDID. | 21 CFR §830.10‑§830.60; §830.300‑§830.360. |

---

### 3. Missing Information – Immediate Action Items
| Gap | Why it matters | Suggested source/approach |
|-----|----------------|---------------------------|
| **Device technology & intended use statement** | Determines classification, predicate selection, and required performance data. | Pull from product development specification or marketing dossier. |
| **Predicate device identifiers (clearance numbers)** | Needed to craft the substantial equivalence argument under §807.87. | Search FDA 510(k) database with key functional keywords once technology is known. |
| **Risk management file (ISO 14971)** | Demonstrates compliance with design‑control and safety requirements. | Compile from engineering risk assessments; verify against QMSR. |
> *No specific identifier found in source — verify separately.*

---

### 4. Core Risk Controls (to be reflected in the submission)
1. **Design Controls** – per 21 CFR §820.30 (including design verification & validation).  
2. **Software Lifecycle Management** – IEC 62304 compliance; include a PCCP if AI/ML is used.  
3. **UDI Integration** – ensure label and device packaging embed the UDI as defined in §830.10‑§830.60.  
4. **Manufacturing Controls** – QMSR (Part 820) SOPs for supplier qualification, process validation, and post‑market surveillance.  

---

### 5. Human‑Escalation Triggers
| Condition | Escalation Level |
|-----------|-----------------|
| *Absence of a clear device description/intended use* | Immediate senior RA review – cannot proceed to predicate search. |
| *Inability to locate at least one potential predicate device* | Flag to product development lead for possible De Novo or PMA pathway consideration. |
| **QMSR compliance gap** (e.g., missing ISO 13485 certification) | Escalate to Quality Assurance Manager for corrective action before submission prep. |
| **UDI allocation not yet assigned** | Notify Regulatory Operations Lead; UDI must be generated prior to 510(k) filing. |
| **AI/ML change‑control plan undefined** | Route to the AI/ML oversight team for PCCP development; hold submission until approved. |

---

### 6. Citations (established references)

- **21 CFR §807** – Premarket notification (510(k)) requirements.  
- **21 CFR §820** – Quality System Regulation (QMSR) effective Feb 2026, ISO 13485‑aligned.  
- **21 CFR §830** – Unique Device Identification system.  
- **21 CFR §892** – Imaging device classification (if imaging technology is later identified).  
- FDA Final Guidance “Predetermined Change Control Plan (PCCP)” – Dec 2024.  

*No case‑level specific identifiers appear in the source excerpts; verification will be required once device details are defined.*

---

### 7. Peer Review Prompt
> **Request:** Please challenge the assumptions made about the likely Class II imaging‑software classification, the completeness of the evidence checklist, and any jurisdictional gaps (e.g., state‑level registration, cybersecurity expectations). Identify missing regulatory considerations that could affect the 510(k) readiness timeline.

--- 

*End of draft.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 69/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,065자 | — |
| 규제 식별자 인용 | 14개 | — |
| source excerpt 근거 일치 | **0/14 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 14개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §892`, `21 CFR §882`, `21 CFR §807`, `21 CFR §820`, `21 CFR §830`, `21 CFR §807.92`, `21 CFR §807.87`, `21 CFR §820.30`, `21 CFR §801`, `21 CFR §830.10`, `Part 820`
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

1. Chunk `202395958248735480`

> ## 목표 영향 - 다음 분기(2026-Q3) `build_readiness.py` 재실행 시 FDA RTA Section A 5건 모두 충족 → **점수 0% → 33%** 예상.

2. Chunk `608496877809508828`

> ## 작업 범위 (Done 정의) - [ ] FDA Form 3514 — 510(k) Cover Sheet 양식 (회사명/주소/연락처 자리표시자 포함) - [ ] FDA Form 3601 — User Fee Cover Sheet 양식 + 수수료 결제 영수증 자리표시자 - [ ] FDA Form 3654 — Standards Data Report 양식 또는 자사 별도 문서 양식 - [ ] FDA Form 3881 — Indications for Use Statement 양식 (현행 OMB 만료일 2026-07-31 주의) - [ ] 510(k) Cover Letter 영문 표준 양식 (applicant name/address/contact/submitter type) - [ ] `13_규제평가_체크리스트/FDA_510k_RTA.md` 항목 A1~A5의 `related_docs:` 필드에 신규 doc-id 등록

## ra_eu

### kb-eval-20260722-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3c458ddac864fc0b", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

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

> **Regulatory Draft – Classification & Conformity Assessment (MDR 2017/745)**  

---

### 1. Device Overview (as inferred from source)

| Item | Current knowledge (source‑derived) |
|------|-------------------------------------|
| **Intended purpose** | Diagnostic X‑ray generator that emits ionising radiation. |
| **Main functional block** | Active device that produces ionising radiation for medical imaging. |
| **Software component** | Medical‑device software (SaMD) associated with the system – classification to be decided under Rule 11. |
| **Regulatory excerpts** | • *Rule 10* – “ionizing radiation emitting diagnostic devices → Class IIb”【2】<br>• *Rule 11* – SaMD classification mentioned【2】 |

---

### 2. Classification Determination  

| Regulatory reference | Reasoning |
|----------------------|-----------|
| **Annex VIII, Rule 10** (diagnostic devices that emit ionising radiation) | The X‑ray generator emits ionising radiation for diagnostic use → **Class IIb**【2】 |
| **Annex VIII, Rule 11** (SaMD) | Software that provides information used to make a diagnostic decision must be classified according to its impact. Without further detail the safe default is **Class IIa**, upgrading to **IIb/III** only if it can cause serious deterioration or death. *Pending clarification of software function.* |
| **Overall device class** | The highest applicable class governs the system: **Class IIb** (driven by the X‑ray generator). |

---

### 3. Conformity Assessment Route  

| Device class | MDR route (Annex number) | Content focus |
|--------------|--------------------------|---------------|
| **Class IIb** | **Annex IX** – Full quality‑management system (QMS) *plus* assessment of technical documentation by the Notified Body. <br>*(Alternative Annex X – type examination – is possible but less common for Class IIb devices.)* |
| **Rationale** | The device is a “higher‑risk” active medical device; MDR mandates either Annex IX or IX+X depending on NB choice. Selecting Annex IX ensures the QMS (ISO 13485) covers design, risk management, PMS and post‑market clinical follow‑up (PMCF). |

---

### 4. Required Evidence & Documentation  

| Requirement | Reference (MDR) | Typical content |
|-------------|------------------|-----------------|
| **Technical documentation** | Annex II – complete dossier (device description, design drawings, specifications, risk management file, labeling, etc.) |
| **Risk management** | ISO 14971 implemented; GSPR §16 (radiation protection), §17 (software), §18 (active devices) |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (kept current under Art. 61) – systematic literature review, clinical data, benefit‑risk analysis |
> *Must include state of the art and SOTA assessment.* |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B – plan describing objectives, methodology, timelines; report summarising results. |
| **Post‑Market Surveillance (PMS) System** | Art. 83 – PMS system description and processes. |
| **PMS Plan** | Art. 84 – documented plan outlining data collection, analysis, trending. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 (Class IIb → at least annually) – includes benefit‑risk conclusions, PMCF findings, sales volume & user population. |
| **Labeling / IFU** | Annex I §23 – instructions for use, safety information, radiation dose guidance. |
| **Applicable harmonised standards** | • IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy) <br>• IEC 62304 (software lifecycle) <br>• IEC 62366‑1 (usability) <br>• ISO 14971 (risk management) |
| **Declaration of Conformity** | Annex IV – signed EU Declaration confirming conformity with MDR. |

---

### 5. Evidential Gaps & Missing Information  

| Gap | Why needed | Suggested source/action |
|-----|------------|------------------------|
| **Exact intended use statement** (indications, target patient group, anatomical site) | Drives classification of the software (Rule 11) and defines clinical endpoints for CER/PMCF. | Obtain from product specification or marketing claim. |
| **Software functional description & decision impact analysis** | Determines whether SaMD remains Class IIa or escalates to IIb/III under Rule 11 (§17). | Provide detailed Software Architecture Document + Intended Use Matrix. |
| **Radiation dose specifications (kV, mA, exposure time, filtration)** | Required for GSPR §16 compliance and for establishing dose‑monitoring controls. | Collect from engineering data sheets or testing reports. |
| **Usability/Human Factors data** (intended users: radiographers vs. laypersons) | Affects labeling (§22) and risk mitigation measures (e.g., error‑proofing). | Conduct formative usability study; reference IEC 62366‑1. |
| **Clinical data** (pre‑market clinical investigations, existing literature on comparable X‑ray systems) | Needed for CER & PMCF planning. | Perform systematic literature search (state of the art) and/or design a small‑scale clinical investigation. |
| **Manufacturing process validation** (process controls for high‑voltage components) | Part of Annex II technical file and QMS audit under Annex IX. | Provide Process Validation Protocol & Report. |
| **PMS data collection mechanisms** (incident reporting, complaint handling, trend analysis tools) | Required by Art. 83–86; influences PSUR content. | Define PMS plan with KPI definitions. |

*Until these items are supplied, the NB will likely raise “information gap” queries.*

---

### 6. Risk Controls – Mapping to GSPR  

| Hazard area | Applicable GSPR | Suggested control(s) |
|-------------|-----------------|----------------------|
| **Radiation exposure** | §16 (Protection against radiation) | • Dose‑monitoring interlocks<br>• Automatic shut‑off if preset limits exceeded<br>• Shielding design per IEC 60601‑2‑54<br>• Patient dose documentation in IFU |
| **Software malfunction** | §17 (Electronic programmable systems) & §18 (Active devices) | • Secure boot, integrity checks<br>• Periodic software verification/validation (IEC 62304)<br>• Redundant safety algorithms for dose calculation |
| **Electrical safety / high‑voltage** | §20 (Mechanical & thermal risks) | • Insulation testing, leakage current limits per IEC 60601‑1<br>• Protective earth continuity checks |
| **User error (lay person vs. trained operator)** | §22 (Devices intended for lay persons) – *if applicable* | • Clear labeling, pictograms, training program, usability testing |
| **Implantable component** (if any) | §19 (Active implantable devices) – *not indicated* | N/A (verify that no implantable part exists). |

All controls must be documented in the **Risk Management File** (ISO 14971) and reflected in the technical documentation (Annex II).

---

### 7. Human‑Escalation Triggers  

| Situation | Trigger condition | Escalation path |
|-----------|-------------------|-----------------|
| **Classification ambiguity** (software impact not yet clarified) | No definitive Rule 11 class after initial analysis. | Immediate referral to senior RA lead for risk‑benefit assessment. |
| **Missing clinical evidence** | CER cannot be completed because of absent primary clinical data or insufficient literature. | Raise a “Clinical Evidence Gap” ticket; pause NB submission until data acquisition plan approved. |
| **PMS/PMCF plan incomplete** | No documented process for collecting post‑market data (Art 84) or no PMCF objectives defined. | Escalate to QMS manager to integrate PMS activities into the ISO 13485 system. |
| **Risk Management File not up‑to‑date** | New hazard identified (e.g., software update) without documented mitigation. | Trigger urgent review by risk‑management specialist; potential NB audit finding. |
| **Notified Body query** | NB requests additional documentation beyond what is currently compiled. | Assign a dedicated liaison to gather missing items within the agreed timeframe (usually 30 days). |
| **Regulatory deadline approaching** (e.g., transition period extension under Regulation EU 2023/607) | Less than 8 weeks remaining before required CE‑marking deadline with incomplete dossier. | Escalate to project manager for resource reallocation and potential timeline renegotiation. |

---

### 8. Peer Review Prompt  

> **Colleague, please review:**  
> - The assumption that the X‑ray generator falls under Annex VIII Rule 10 (Class IIb) given the limited device description – do we need additional product‑specific data to confirm it is not a “diagnostic imaging system” split across multiple rules?  
> - Whether the default SaMD classification as Class IIa under Rule 11 is appropriate without a detailed decision‑impact analysis.  
> - Completeness of the listed evidential requirements, especially any MDR annexes that may apply to combined hardware/software systems (e.g., Annex IX + X).  
> - Any jurisdictional nuances (e.g., national provisions for X‑ray equipment) that could affect the conformity route or required standards.

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

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20260722-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "fe263dc57fa1ee07", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

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

> **Regulatory Draft – Diagnostic X‑ray System (Active Device that Emits Ionising Radiation for Diagnosis)**  

---

### 1. Classification & Conformity‑Assessment Route  
| Item | Determination | Regulatory basis |
|------|---------------|------------------|
| **Device class** | **Class IIb** | Rule 10 (active devices for diagnosis/monitoring of vital physiological processes) – *Annex VIII, Rule 10*; the X‑ray source emits ionising radiation for diagnostic purposes and therefore is *not* a therapeutic device (Rule 9). |
| **Conformity‑assessment route** | **Annex IX** (full quality‑management‑system assessment + technical documentation) – preferred for Class IIb. <br>Alternative: **Annex X** (type‑examination) if the manufacturer elects a type‑examination route and the Notified Body accepts it. | MDR 2017/745, *Annex IX* (full assessment) and *Annex X* (type examination). |

---

### 2. Required Technical & Clinical Evidence  

| Evidence | Description | Regulatory citation |
|----------|-------------|---------------------|
| **Technical Documentation** | Complete device description, intended purpose, design‑manufacturing information, labeling, GSPR mapping, etc. | *Annex II* (technical documentation) |
| **Risk Management File** | ISO 14971‑compliant risk analysis, evaluation and control measures; updates incorporated into post‑market surveillance. | *Annex I* §§ 16–18 (radiation protection, electronic programmable systems, active devices) ; ISO 14971 |
| **Clinical Evaluation Report (CER)** | Systematic literature review & clinical data demonstrating safety & performance per state of the art. Updated continuously (Art. 61). | *Annex XIV* Part A – CER |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Planned prospective studies or registries to confirm long‑term safety/performance; final evaluation report. | *Annex XIV* Part B – PMCF plan/evaluation |
| **Post‑Market Surveillance (PMS) System** | PMS plan, periodic safety update reports (PSUR) and routine reporting procedures. | Art. 83 (PMS system), Art. 84 (PMS plan), Art. 86 (PSUR for Class IIb – annual) |
| **Standards Evidence** | Application of relevant harmonised standards: <br>• IEC 60601‑2‑54 (X‑ray equipment for radiography & radioscopy) <br>• IEC 60601‑2‑28 (X‑ray tube assemblies) <br>• IEC 62220‑1‑1 (DQE measurement, if applicable) <br>• IEC 62304 (software lifecycle) <br>• IEC 62366‑1 (usability) | Referenced standards – no verification needed |
| **Labeling & IFU** | Instructions for use, safety information, radiation dose limits, contraindications, and user training documentation. | *Annex I* Chapter III §23 (label & instructions for use) |

---

### 3. Identified Gaps / Missing Information  

| Gap | Impact if not addressed | Suggested remedy |
|-----|------------------------|-----------------|
| **Explicit intended purpose** stating “diagnostic X‑ray system for radiography/radioscopy” and confirming *no therapeutic* application. | Prevents mis‑application of Rule 9; essential for correct classification. | Draft a clear Intended Use statement and have it reviewed by the clinical team. |
| **Clinical performance data** (e.g., dose‑distribution measurements, image‑quality studies) specific to the marketed configuration. | CER will be incomplete; NB may request additional clinical investigation. | Conduct a prospective performance study or collect robust retrospective data. |
| **PMCF protocol** covering long‑term radiation safety and software updates. | Absence of PMCF will breach Art. 83/84 and may delay PSUR issuance. | Prepare a PMCF plan aligned with the risk management file; schedule interim assessments. |
| **GSPR mapping table** linking each General Safety & Performance Requirement to device specifications. | Hampers technical‑documentation review; NB may request clarification. | Populate a GSPR matrix (Art. 10) and attach to Annex II documentation. |
| **Usability validation** for lay‑person handling (if intended). | May affect compliance with §22 (use by lay persons). | Conduct usability engineering per IEC 62366‑1, document outcomes. |

*No specific case identifiers (e.g., 510(k) numbers, product codes) appear in the source excerpts – verify separately if required.*

---

### 4. Core Risk Controls (to be reflected in the risk management file)

| Hazard | Control measure(s) | Regulatory reference |
|--------|-------------------|-----------------------|
| **Ionising radiation exposure** | • Automatic dose‑limiting interlocks <br>• Real‑time dosimetry & alarm thresholds <br>• Mandatory user training on ALARA principle | §16 (Protection against radiation) – *Annex I* |
| **Electronic programmable system failure** | • Redundant safety software modules <br>• IEC 62304‑compliant development, verification and validation <br>• Periodic firmware integrity checks | §17 (Electronic programmable systems) – *Annex I* |
| **Active device malfunction (energy delivery)** | • Self‑test routine on power‑up <br>• Hardware interlocks preventing unintended emission <br>• Fail‑safe mode that disables output if fault detected | §18 (Active devices) – *Annex I* |
| **User error / mis‑interpretation of images** | • Comprehensive IFU with dose limits, positioning guidelines <br>• Integrated decision‑support prompts in diagnostic software (Rule 11 scope) | §23 (Information supplied) – *Annex I* |

---

### 5. Human‑Escalation Triggers  

| Situation | Who must be alerted | Action deadline |
|-----------|--------------------|-----------------|
| **Classification mismatch discovered** (e.g., initial mapping to Rule 5/9) | RA Lead → Notified Body Project Manager | Immediate (within 1 business day) – re‑classify and update CE‑marking plan. |
| **Missing clinical data or incomplete CER** | Clinical Affairs Lead & QA Manager | Within 3 business days – initiate data acquisition or supplemental investigation. |
| **PMS/PMCF gaps identified during routine review** | Post‑Market Surveillance Coordinator → Senior Management | Within 5 business days – define corrective actions and update PMS plan. |
| **Serious safety incident (radiation overdose, device failure)** | Vigilance Officer → National Competent Authority (via Art. 87 reporting) | Immediate (within 24 h) per MDR vigilance obligations. |
| **Non‑conformance to GSPR mapping** | Quality Management Representative | Within 2 business days – remediate technical documentation and inform Notified Body. |

---

### 6. Peer‑Review Request  

> *Please review this draft and challenge the following aspects:*  
> 1. The applicability of Rule 10 versus any possible interpretation under Rule 9 for hybrid devices that combine diagnostic imaging with limited therapeutic functions.  
> 2. Whether Annex X (type‑examination) could be a more appropriate route given the anticipated production volumes and existing NB capabilities.  
> 3. Completeness of the identified evidence list, especially regarding any mandatory “state‑of‑the‑art” literature that may have been omitted for X‑ray systems.  

--- 

*End of draft.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 88/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,094자 | — |
| 규제 식별자 인용 | 17개 | — |
| source excerpt 근거 일치 | **2/17 (11%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 15개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex II` | MDR Annex II | Technical documentation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `Art. 87` | MDR Article 87 | Reporting of serious incidents and field safety corrective actions |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `IEC 62220`, `Art. 10`
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

1. Chunk `109229213193581391`

> ### Rule 9 (Chapter III §6.1) — 오적용 반증 > "All active **therapeutic** devices intended to administer or exchange energy are classified as class IIa ... **All active devices intended to emit ionizing radiation for therapeutic purposes** ... are classified as class IIb." (진단용 X-ray에는 부적용)

2. Chunk `109346595768604468`

> ### D1 — §6 표 0-2 예시 열 - **기재값 (예시 열):** > "X-ray: MFDS 3등급, FDA Class II 510(k), **EU MDR Rule 5/9**" - **독립확인 정답:** - X-ray 시스템(진단용 이온화방사선 능동기기) = **Rule 10 → Class IIb** - 디지털 평판 디텍터(X-ray 영상 기록기기) = **Rule 17 → Class IIa** - Rule 9 = **치료용** 이온화방사선/에너지 투여 기기(진단용 X-ray 배제) - Rule 5 = 체강 대상 침습기기(X-ray 배제) - **영향:** - 규제 분류 오적용 시 EU MDR 적합성 평가 절차(Annex IX/X/XI) 선정 오류로 연결(Notified Body 인증 경로·기술문서 요구·PSUR 주기 오판정). - "MFDS 3등급 = FDA Class II = EU MDR Rule 5/9" 정합 매핑이 후속 문서(GSPR 매핑표·기술문서·CE marking plan)로 전파될 위험. - **권고수정:** - 예시 열을 다음으로 변경: > "X-ray 시스템: MFDS 3등급, FDA Class II (510(k), Product Code MQB), **EU MDR Rule 10 → Class IIb**; 평판 디텍...

### kb-eval-20260722-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e943ded4dd4d76d4", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Pathway**

---

### 1. Scope of the assessment  

The source material provides only generic procedural information (Article 51, Annex VIII classification rules; Article 61/Annex XIV CER requirements; UDI and vigilance references). No device description, intended purpose, or specific identifiers are included. Consequently a definitive class cannot be assigned at this stage.

---

### 2. Classification methodology (per MDR)

| Step | Action | Reference |
|------|--------|------------|
| 2.1 | The manufacturer must **self‑classify** the device and retain responsibility for the decision. | Art. 51 MDR; “자가 분류 책임 부담” in source [2] |
| 2.2 | Apply the **22 rules of Annex VIII** sequentially, selecting the highest class reached. | Annex VIII – Rules 1‑22 (MDR) |
| 2.3 | If doubt remains, seek clarification from the national Competent Authority or the MDCG “Borderline and Classification” Manual (latest version v2.1.1, Sep 2023). | Source [2] – “관할 CA…또는 MDCG Manual … 참조” |
| 2.4 | Record the applied rule(s) and justification in the **Technical Documentation** (Annex II). | Annex II MDR |

*Because the device’s intended medical purpose, mode of action, and technological characteristics are not disclosed, step 2 cannot be completed.*  

---

### 3. Expected conformity‑assessment routes (once class is known)

| Device class | Typical route(s) | Reference |
|--------------|------------------|-----------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration only (Annex IV Declaration of Conformity). No NB involvement. | Annex IV MDR |
| **Class I (sterile or measuring)** | Involvement of a Notified Body for the QMS assessment – **Annex IX** (full quality‑management system) plus technical documentation review. | Annex IX MDR |
| **Class IIa / IIb / III** | **Annex IX** (QMS + full technical file), possibly supplemented by **Annex X** (type‑examination) or **Annex XI** (production conformity verification) depending on the device and NB strategy. | Annexes IX–XI MDR |

The exact route will be selected after classification is finalised.

---

### 4. Required evidence per MDR (generic checklist)

| Evidence item | Content requirement | Reference |
|---------------|--------------------|-----------|
| **Technical Documentation** – design, manufacture, labeling, risk management, etc. | Must satisfy Annex II; includes device description, specifications, GSPR compliance, etc. | Annex II MDR |
| **Risk Management File** (ISO 14971) | Risk analysis, evaluation, mitigations, residual risk assessment. | Annex I §16‑§22 (GSPR) + ISO 14971 |
| **Clinical Evaluation Report (CER)** – state of the art, clinical data, benefit–risk analysis. | Must be kept current under Art. 61 and follow Annex XIV Part A. | Annex XIV Part A; Art. 61 MDR |
| **Post‑Market Surveillance (PMS) System** | Defined in Art. 83; includes PMS plan (Art. 84), periodic safety update report (PSUR for class IIa‑III, Art. 86). | Art. 83‑86 MDR |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** (if required) | Annex XIV Part B – plan, execution, and evaluation of additional clinical data. | Annex XIV Part B |
| **Unique Device Identification (UDI)** registration | Entry in EUDAMED UDI/DEV module; national portal links optional. | Source [1] – “UDI 포털…EUDAMED UDI/DEV” (generic) |
| **Vigilance / Incident Reporting** | Procedures compliant with Art. 87 (serious incident and FSCA reporting). | Art. 87 MDR |
| **Labeling & IFU** | Must meet Annex I Chapter III §23. | Annex I §23 |

---

### 5. Gaps / Missing Information (must be supplied before proceeding)

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Intended purpose & indications for use** | Drives rule selection in Annex VIII and determines clinical evidence scope. | Manufacturer to provide a clear, concise statement of intended medical purpose. |
| **Device technology description (active/passive, implantable, software, etc.)** | Needed to apply the correct classification rule (e.g., Rule 9‑11, 17). | Detailed device architecture & functional description required. |
| **Target patient population / user group** | Influences risk assessment, usability, and labeling (§22). | Provide demographics, intended users (layperson vs professional). |
| **Mode of action (energy delivery, measurement, diagnosis, therapy)** | Determines whether the device falls under Rule 9, 10, 11 or 17. | Clear description of how the device achieves its purpose. |
| **Sterility & measuring function status** (if applicable) | May elevate a Class I device to requiring NB involvement (§14). | Indicate if the device is sterile and/or performs measurements. |
| **Existing clinical data (literature, trials, registries)** | Forms basis of CER; absence triggers need for PMCF or new clinical investigation. | Supply all available clinical evidence. |
| **Manufacturer’s QMS certification status** | Required for NB assessment under Annex IX. | Provide ISO 13485 certificate and scope. |

---

### 6. Core risk‑control considerations (Annex I GSPR)

1. **General safety & performance (§1‑§9)** – Ensure the device meets essential requirements, including chemical, biological, and electrical safety.
2. **Design & manufacturing (§10‑§22)** – Apply risk control measures identified in ISO 14971; verify protection against radiation (§16) if applicable.
3. **Information supplied (§23)** – Labels, IFU, and UDI must convey safe use instructions, contraindications, and maintenance.

Each GSPR claim must be substantiated with evidence (testing reports, validation data, usability studies).

---

### 7. Human‑escalation triggers

| Trigger | Reason | Recommended escalation |
|--------|--------|-------------------------|
| **Insufficient device description to apply any Annex VIII rule** | Classification cannot be determined → risk of non‑compliance. | Pause the dossier; request full intended‑use and technology statement from the manufacturer. |
| **Missing clinical data for claimed indications** | CER would be incomplete, violating Art. 61/Annex XIV Part A. | Initiate a PMCF plan or new clinical investigation before NB submission. |
| **No ISO 13485/QMS evidence for Class IIa‑III devices** | NB cannot assess conformity under Annex IX. | Obtain/complement QMS certification; involve quality‑management lead. |
| **UDI not registered in EUDAMED (or national portal)** | Failure to meet post‑market traceability obligations (Art. 27). | Notify the regulatory project manager to open an EUDAMED entry task. |
| **Vigilance procedures absent or not aligned with Art. 87** | Could lead to delayed incident reporting and penalties. | Escalate to compliance officer; develop a vigilance SOP immediately. |

When any trigger occurs, log the issue in the project tracker, assign it to the responsible stakeholder, and place the work package on **Yellow gate** status pending resolution (per Fixed Rule 2).

---

### 8. Peer‑review request  

> **@RA‑peer:** Please review the assumptions made above—particularly the reliance on generic classification guidance without a concrete device description. Check whether any jurisdiction‑specific nuances (e.g., national CA interpretations of borderline cases) have been omitted, and confirm that all cited MDR references align with the latest consolidated text.

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

### kb-eval-20260722-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e3e29ddc12ec8317", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_DoC_양식_작성지침.md", "source_hash": "9432073e1a6f2ab2c1e92f11a1b1f4613cef136ade7183212d18a66cedaca592"} -->

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

> **Regulatory Draft – Preliminary MDR Assessment (Classification & Conformity‑Assessment Route)**  

---

### 1. Scope of the source material  
The supplied excerpts constitute a **template for the EU Declaration of Conformity (DoC)** (see Annex IV) and a signature block. No technical description, intended purpose, principle of operation, or risk‑related information about the device is present in the source. Consequently, no definitive MDR classification can be derived at this stage.

---

### 2. Immediate regulatory gaps that must be filled  

| Gap | Why it matters (MDR requirement) | Evidence needed to close the gap |
|-----|-----------------------------------|----------------------------------|
| **Intended use / indication** | Determines which **classification rule** applies (Annex VIII, Rules 1‑22). | Clear statement of clinical purpose, target patient group, mode of action, and any claims. |
| **Device description & principal design** | Needed to identify whether the device is active, invasive, software‑only, etc., and thus which rule(s) apply (e.g., Rule 9, 10, 11, 17). | Technical schematics, block diagrams, bill of materials, or software architecture summary. |
| **Risk classification** | MDR requires a justified class assignment in the technical documentation (Annex II). | Mapping of device characteristics to the applicable rule(s) with citation (e.g., “Rule 10 – active diagnostic” → Class IIa/IIb). |
| **Manufacturer details (full)** | Required on the DoC (Annex IV) and for EUDAMED registration. | Company name, address, SRN, authorised representative (if applicable). |
| **Basic UDI‑DI** | Mandatory in the DoC (Annex VI Part C) and for traceability. | Assigned Basic UDI‑DI from the European Issuing Agency. |
| **Labeling & IFU excerpt** | Must demonstrate compliance with Annex I §23 (information supplied). | Draft label, symbols, and Instructions for Use (IFU) covering hazards, contraindications, etc. |
| **Conformity‑assessment route justification** | Determines which **Annex** (IX, X or XI) will be applied and which Notified Body involvement is required. | Decision tree linking device class to the appropriate Annex (see below). |

*No specific identifiers (e.g., 510(k), EUDAMED case numbers) appear in the source – verify separately.*

---

### 3. Preliminary classification pathway (to be completed once gaps are filled)

| Step | Action | MDR reference |
|------|--------|---------------|
| **a. Determine if the device is a medical device** | Verify intended purpose is for diagnosis, prevention, monitoring, treatment or alleviation of disease. | Annex VIII – definition of “medical device”. |
| **b. Identify applicable classification rule(s)** | Match the device’s principal mode of action and technology against Rules 1‑22 (Annex VIII). Example scenarios: <br>• Active therapeutic → Rule 9 → Class IIa/IIb<br>• Active diagnostic → Rule 10 → Class IIa/IIb<br>• Software decision aid → Rule 11 → Class IIa/IIb/III | Annex VIII (Rules 1‑22). |
| **c. Assign the device class** | Based on rule outcome and any “higher‑risk” modifiers (e.g., invasiveness, duration of contact). | Annex VIII; see specific rule footnotes for class escalation. |
| **d. Select conformity‑assessment route** | *If Class IIa* → **Annex IX** (QMS + technical documentation assessment) is mandatory; Notified Body involvement required for the technical file. <br>*If Class IIb or III* → **Annex X** (type‑examination) plus **Annex XI** (production conformity verification) may be needed, depending on whether a full quality‑management system audit is chosen. | Annex IX, X, XI. |
| **e. Prepare the Technical Documentation** | Must include: device description, design/manufacturing information, risk management (ISO 14971), clinical evaluation (Annex XIV Part A), PMS plan (Art 84) and reports (Art 85‑86). | Annex II; Art 83‑86. |

*Until the intended use and technology are disclosed, the above steps remain **provisional**.*

---

### 4. Required evidence package for a complete MDR submission  

1. **Technical Documentation (Annex II)** – full dossier covering design, manufacturing, verification & validation, labeling, and post‑market surveillance system.  
2. **Risk Management File** – ISO 14971‑compliant risk analysis, evaluation of residual risks, and risk control measures. (Annex I §17‑§20).  
3. **Clinical Evaluation Report (CER)** – per Annex XIV Part A, including state‑of‑the‑art literature review and/or clinical data.  
4. **Post‑Market Surveillance (PMS) Plan** – Art 84; for Class IIa/IIb/III a Periodic Safety Update Report (PSUR) per Art 86 is required.  
5. **Usability Engineering File** (if device intended for lay users or has user interface) – IEC 62366‑1 compliance, referenced in Annex I §22.  
6. **Software Validation / Lifecycle Documentation** (if software component) – IEC 62304; classification under Rule 11 must be justified.  
7. **Electromagnetic Compatibility & Electrical Safety Test Reports** (if active/device contains electronics) – IEC 60601‑1 series as appropriate.  

*Each element must be cross‑referenced in the DoC (Annex IV) once the final class and route are established.*

---

### 5. Risk‑control considerations (pre‑emptive)

| Hazard area | Typical control measure (MDR/IEC reference) |
|-------------|----------------------------------------------|
| **Radiation exposure** (if device emits ionising radiation) | Conformity to IEC 60601‑2‑54 / IEC 60601‑2‑28; fulfil Annex I §16.4. |
| **Electrical safety & EMC** | IEC 60601‑1; Annex I §§18‑20. |
| **Software malfunction** (decision‑making software) | IEC 62304 lifecycle, IEC 82304‑1 (if applicable); Annex I §17. |
| **Usability errors** (lay‑person operation) | IEC 62366‑1 usability engineering; Annex I §22. |
| **Biocompatibility / Sterility** (if invasive) | ISO 14971 risk control and relevant MDCG guidance; Annex I §§10‑13. |

*Exact controls must be justified by the risk analysis once the device’s hazards are identified.*

---

### 6. Human‑escalation triggers  

| Trigger condition | Action required (who) |
|-------------------|-----------------------|
| **Missing intended use / indication** | Pause classification work; request a detailed Intended Use Statement from the product owner/clinical team. |
| **No Basic UDI‑DI assigned** | Escalate to regulatory project lead for allocation of a European Issuing Agency code before DoC finalisation. |
| **Unclear technology (active vs. passive)** | Convene a technical‐expert workshop (engineering + clinical) to map device functions against Annex VIII rules. |
| **Risk analysis incomplete or absent** | Engage the risk‑management team; schedule a dedicated R&R session to produce ISO 14971 file. |
| **Clinical evidence insufficient for CER** | Initiate a Clinical Evaluation Plan (CEP) draft and seek input from clinical affairs; consider prospective PMCF if required. |
| **Manufacturer SRN or Authorized Representative not available** | Notify the compliance manager to secure EUDAMED registration details; cannot sign DoC without them. |

All escalations should be logged in the project’s risk‑register and tracked as “Open Issues” until resolved.

---

### 7. Summary judgment  

*At present there is **insufficient information** to assign a definitive MDR classification or conformity‑assessment route.* The declaration template (Annex IV) is ready for completion once the missing device‑specific data are supplied. Until then, the regulatory pathway remains **open**, and the above evidence checklist should guide data collection.

---

### 8. Peer‑review prompt  

> @RA‑colleague – please review the assumptions made in the provisional classification flow (section 3) and verify that the listed evidence items align with the latest MDR guidance (including any recent MDCG clarifications). In particular, flag any **jurisdiction‑specific nuances** (e.g., national competent authority requirements for certain active devices) that may have been omitted from this draft.  

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

1. Chunk `1085205256397640486`

> 8. SIGNATURE Place, date : [도시], [YYYY-MM-DD] Name : [서명자 이름] Function : [직함 — 예: CEO, QA Director] Signature : ___________________________ For and on behalf of [회사명] ───────────────────────────────────────────── ``` ---

2. Chunk `1141859994065237405`

> ## 4. DoC 양식 (빈 템플릿) ``` EU DECLARATION OF CONFORMITY (Regulation (EU) 2017/745 on Medical Devices — Annex IV) ───────────────────────────────────────────── 1. MANUFACTURER Company name : [회사명] SRN : [EUDAMED SRN — 미취득 시 공백] Address : [등록 사업장 주소] Authorised Representative: [EU 대리인명 및 주소 — 역외 제조사 해당 시] 2. SOLE RESPONSIBILITY STATEMENT This EU Declaration of Conformity is issued under the sole responsibility of the manufacturer named above. 3. BASIC UDI-DI [Basic UDI-DI — Annex VI Part C 기준] 4. PRODUCT IDENTIFICATION Product name : [제품명] Trade name : [상품명] Model / Cat.# : [모델 번호 / 카탈로그 번호] Intended use : [의도된 사용 목적 — 간략 기재] Photograph : [첨부...

### kb-eval-20260722-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "373d752f87933ec8", "source": "github:holee9/MD-process/issue-drafts/902_AUDIT_GUIDE-VIG-001_EU_MDR_보존기한_인용부정확.md", "source_hash": "4c91abf315dbe190d6ab922f205dd0b1ee9bd66a660924704de5fca6a523f775"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `373d752f87933ec8`
- Source: `github:holee9/MD-process/issue-drafts/902_AUDIT_GUIDE-VIG-001_EU_MDR_보존기한_인용부정확.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/902_AUDIT_GUIDE-VIG-001_EU_MDR_%EB%B3%B4%EC%A1%B4%EA%B8%B0%ED%95%9C_%EC%9D%B8%EC%9A%A9%EB%B6%80%EC%A0%95%ED%99%95.md)
- Source hash: `4c91abf315dbe190d6ab922f205dd0b1ee9bd66a660924704de5fca6a523f775`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `902_AUDIT_GUIDE-VIG-001_EU_MDR_보존기한_인용부정확.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 2. 문서 기재값 vs 1차 출처 정답 | 항목 | 문서 기재 | 1차 출처 정답 | |---|---|---| | EU MDR 기술문서·기록 보존 — 비임플란트 | "Class III 10년" (한정 표기) | **모든 비임플란트 기기 10년** (Class I/IIa/IIb/III 공통) | | EU MDR 기술문서·기록 보존 — 임플란트 | 15년 | 15년 (일치) | ## 3. 1차 출처 - **EU MDR 2017/745 Article 10(8)** - 원문: "Manufacturers shall keep the technical documentation... available for the competent auth...
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

> **Regulatory Draft – Documentation Retention & Preliminary Conformity Assessment Planning**

---

### 1. Scope of the Assessment  
The source material only addresses **EU MDR 2017/745 documentation retention periods** (Art. 10(8)). No device description, intended purpose, or classification information is provided in the excerpts. Consequently, a definitive classification and conformity‑assessment route cannot be concluded at this stage.

---

### 2. Mandatory Documentation Retention (Article 10 & Annex II)

| Requirement | MDR Reference | Applicability |
|-------------|---------------|---------------|
| **Technical documentation** must be kept available for competent authorities for **at least 10 years** after the last device covered by the EU declaration of conformity has been placed on the market. For implantable devices, the period is **at least 15 years**. | Art. 10(8) MDR 2017/745 (source [2]) | All manufacturers – non‑implantable = 10 yr; implantable = 15 yr |
| **Record‑keeping for post‑market surveillance (PMS)**, including vigilance data and periodic safety update reports, follows the same retention periods. | Art. 10(8) MDR 2017/745 (source [2]) | Class I–III devices; PMS records are part of Annex III technical documentation |
| **Technical documentation content** – must satisfy Annex II (general requirements) and Annex III (PMS system). | Annex II & III MDR 2017/745 (knowledge base) | Required for all classes |

*No specific identifier (e.g., device model, EC‑type‑exam number) appears in the source excerpts – **verify separately** if such identifiers exist in the originating dossier.*

---

### 3. Preliminary Classification Checklist  

| Information Needed | Why It Is Needed | Where to Find / Evidence |
|--------------------|-----------------|---------------------------|
| **Intended purpose / indications for use** (including patient population, anatomical site) | Determines which classification rule (Annex VIII) applies (e.g., Rule 9, 10, 11, 17). | Label/IFU, marketing material, risk analysis |
| **Device nature** – active/non‑active, invasive/non‑invasive, software component, radiation emitting, implantable etc. | Governs the “Rule” selection and hence class (I, IIa, IIb, III). | Device description in technical file |
| **Energy source / therapeutic/diagnostic function** | Needed for Rule 9 (active therapeutic) vs Rule 10 (diagnostic) vs Rule 11 (software). | Functional specifications |
| **Degree of invasiveness & duration of contact** | Determines implantable status → 15‑yr retention, higher class possibly. | Clinical evaluation plan / risk management file |

*Current source does not contain any of the above; **missing information flagged** for immediate collection.*

---

### 4. Expected Conformity‑Assessment Route (once classification is known)

| Possible Class | Corresponding Annex Route |
|----------------|---------------------------|
| Class I (non‑sterile, non‑measuring) | Self‑declaration – no Notified Body involvement (Annex IV declaration). |
| Class I (sterile or measuring) | **Annex IX** – QMS assessment + technical documentation review by a NB. |
| Class IIa / IIb / III | **Annex IX** (full quality‑management system audit + technical file); for higher risk may also require **Annex X** (type‑examination) or **Annex XI** (production conformity verification) depending on device type and NB strategy. |

*Exact route cannot be selected without the classification outcome.*

---

### 5. Required Evidence Packages (once classification is set)

| Evidence Category | Typical Content | MDR Reference |
|-------------------|-----------------|---------------|
| **Technical Documentation** | Device description, design specifications, manufacturing processes, labels/IFU, risk management (ISO 14971), performance testing, clinical evaluation report (CER) – Annex II. | Annex II MDR 2017/745 |
| **Post‑Market Surveillance (PMS)** | PMS plan (Art. 84), PMS system (Art. 83), periodic safety update report (PSUR) for class IIa–III (Art. 86). | Art. 83‑86 MDR 2017/745 |
| **Clinical Evidence** | Clinical evaluation (Annex XIV Part A) and, where required, PMCF plan/evaluation (Annex XIV Part B). | Annex XIV MDR 2017/745 |
| **Quality Management System (QMS)** | ISO 13485:2016‑compliant QMS dossier; evidence of conformity‑assessment audit. | Annex IX (NB assessment) |
| **Regulatory Labels & IFU** | Compliance with §23 Annex I – labeling, symbols, UDI. | Annex I §23 MDR 2017/745 |

*All above items must be retained for the period stipulated in Art. 10(8).*

---

### 6. Risk Controls (pre‑submission)

| Control | Expected Documentation |
|---------|------------------------|
| **Risk Management File** – hazard analysis, risk evaluation, mitigation measures, residual risk assessment. | ISO 14971 file, referenced in technical documentation (Annex II §9). |
| **Usability/Human‑Factors Engineering** (if device is used by lay persons or involves software) | IEC 62366‑1 compliance evidence. |
| **Software Lifecycle Management** (if applicable) | IEC 62304 certification report; classification under Rule 11. |
| **Radiation Safety** (if emitting ionising radiation) | Compliance with §16 MDR & IEC 60601‑2‑54/28/44 as appropriate. |

*Risk control evidence must be linked to the retained technical file for at least 10 years (15 years for implants).*

---

### 7. Missing Information – Immediate Action Items  

| Item | Reason | Priority |
|------|--------|----------|
| Intended use / indications | Determines classification rule (Annex VIII) and class. | **High** |
| Device nature (active, invasive, software, radiation) | Drives Rule selection & evidence needs. | **High** |
| Whether the device is implantable | Affects retention period (15 yr) & possibly higher class. | **Medium** |
| Existing QMS certification status (ISO 13485) | Required for NB audit routes. | **Medium** |
| Clinical data availability (pre‑market studies, literature) | Needed for CER/PMCF. | **High** |
| UDI / labeling drafts | Must meet §23 Annex I. | **Low** |

*Collect these facts before proceeding to classification and route selection.*

---

### 8. Human‑Escalation Triggers  

| Situation | Trigger Action | Responsible Role |
|-----------|----------------|------------------|
| **No intended‑use statement available** | Pause the assessment; request complete device description from product development. | RA Lead → Project Manager |
| **Unclear whether device is implantable** | Escalate to Clinical & Engineering leads for classification clarification (15 yr vs 10 yr retention). | RA Lead |
| **Missing or insufficient clinical evidence** | Issue a “clinical data gap” notice; order feasibility study or literature search. | Clinical Evaluation Team |
| **Absence of ISO 13485 certification** | Prompt quality‑management audit planning; involve QMS manager. | QA Manager |
| **Discrepancy between retained documentation period and device classification (e.g., implantable classified as non‑implantable)** | Immediate review by Regulatory Compliance Officer; correct retention schedule. | Regulatory Compliance Officer |

Only after these triggers are resolved should the classification be finalized and the appropriate Annex IX/​X/​XI conformity‑assessment route be selected.

---

### 9. Peer Review Prompt  

> **@RA‑Peer:** Please challenge the assumptions made above, especially regarding (a) whether any implicit information in the source could hint at device type, (b) completeness of the evidence list for higher‑risk classes, and (c) potential jurisdiction‐specific gaps (e.g., French Décret 2018‑XX requirements). Your input will help us close remaining uncertainties before formal submission.

---

**Regulatory Judgment (preliminary)**  
- The source confirms that **all non‑implantable devices must retain technical documentation for a minimum of 10 years**, and **implantable devices for at least 15 years** (Art. 10(8) MDR 2017/745).  
- Without further device‑specific data, **no definitive classification or conformity‑assessment route can be assigned** at this time. Collect the missing information listed in Section 7 before proceeding.

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 87/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,205자 | — |
| 규제 식별자 인용 | 19개 | — |
| source excerpt 근거 일치 | **1/19 (5%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 18개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex III` | MDR Annex III | Technical documentation on post-market surveillance |
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |

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

1. Chunk `1013295490713979930`

> ## 2. 문서 기재값 vs 1차 출처 정답 | 항목 | 문서 기재 | 1차 출처 정답 | |---|---|---| | EU MDR 기술문서·기록 보존 — 비임플란트 | "Class III 10년" (한정 표기) | **모든 비임플란트 기기 10년** (Class I/IIa/IIb/III 공통) | | EU MDR 기술문서·기록 보존 — 임플란트 | 15년 | 15년 (일치) |

2. Chunk `178189066284189048`

> ## 3. 1차 출처 - **EU MDR 2017/745 Article 10(8)** - 원문: "Manufacturers shall keep the technical documentation... available for the competent authorities for a period of **at least 10 years** after the last device covered by the EU declaration of conformity has been placed on the market. **In the case of implantable devices, the period shall be at least 15 years**..." - URL: https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng - 참고: https://www.medical-device-regulation.eu/2019/07/08/mdr-article-10-general-obligations-of-manufacturers/

## ra_kr

### kb-eval-20260722-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "eb188d0bad15091e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

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

> **Regulatory Draft – Digital Medical Device (Software)  
Classification, Submission Route & Evidence Package**

---

### 1. Regulatory Context & Applicable Standards  

| Area | Korean reference (established) | International counterpart |
|------|--------------------------------|---------------------------|
| Governing act | **디지털의료기기법** and its Enforcement Rules (시행규칙) – classification provisions (제13조, 제14조) | FDA 21 CFR Part 820; EU MDR Annex IX |
| Software‑specific guidance | **MFDS SW 가이드라인** (mandatory items S‑1 ~ S‑9) | IEC 62304, IMDRF “Software as a Medical Device” (SaMD) |
| Cybersecurity | **MFDS 사이버보안 가이드라인 2025.01** (items S‑6 ~ S‑8, optional S‑10) | IEC 62443 series; FDA “Content of Premarket Submissions for Management of Cybersecurity … ” |
| KGMP facility certification | **KGMP 규정** (제10조) – required for Class II‑IV devices | ISO 13485:2016 |
| Labeling & IFU | **디지털의료기기 특화 표시기재 요건 체크리스트** (추가 항목) – Korean language mandatory | EU MDR Annex I; FDA 21 CFR 801 |

---

### 2. Device Classification (Korean MFDS)

1. **Determine risk class** by intended use, invasiveness, decision‑support level and AI/ML involvement (if any).  
   *If the software provides diagnostic or therapeutic recommendations that directly affect patient management* → typically **Class II** or higher.  

2. **Resulting classification** (example):  
   - **Class II** – “medium risk” digital medical device.  
   - **Class III/IV** only if the software is life‑supporting, highly autonomous AI/ML, or directly controls an implantable device.

> *If the intended use description does not clarify the impact on clinical decision‑making, escalation to a senior RA for classification verification is required.*

---

### 3. Submission Route  

| MFDS Class | Regulatory pathway |
|------------|--------------------|
| **Class I** (low risk) | Notification (**신고**) – minimal technical dossier. |
| **Class II–IV** (medium‑to‑high risk) | Approval (**허가**) – full technical file, clinical evidence, KGMP certificate. |

*Assuming the device lands in Class II, the route is **허가**.*

---

### 4. Core Evidence Required for 허가 (Class II)

| Evidence Category | Specific items (per MFDS guidance) | Status / Gap |
|-------------------|-------------------------------------|--------------|
| **Software Architecture & Lifecycle** | • Version, build number, release date (S‑1)  <br>• Update method & schedule (S‑2)  <br>• Minimum system requirements (S‑3)  <br>• Compatibility list & interface specs (S‑4)  <br>• Data I/O formats (DICOM/HL7) (S‑5) | All mandatory in source; verify that documentation is complete. |
| **Cybersecurity** | • Security configuration guidelines (encryption, network segmentation, access control) (S‑6)  <br>• Patch management procedure & responsible party (S‑7)  <br>• Residual risk handling plan (S‑8)  <br>*(Optional) System log management (S‑10)* | Items S‑6 ~ S‑8 are mandatory; ensure up‑to‑date in technical file. |
| **Data Management** | • Backup & recovery procedures (S‑9) | Confirm SOPs and test records exist. |
| **Risk Management** | IEC 60601‑1‑2 / IEC 62304 risk analysis, AI/ML safety case if applicable (per IMDRF guidance). | Not listed in source – gap identified. |
| **Clinical Evidence** | • Clinical evaluation report (Korean language)  <br>• If foreign clinical data used, mapping to MFDS acceptance criteria (OECD‑aligned non‑clinical data, CE/FDA clinical reports). | No clinical data mentioned – required for Class II+. |
| **Labeling & IFU** | • Korean language labeling, user manual (IFU) covering all checklist items in the “디지털의료기기 특화 표시기재 요건 체크리스트”.  <br>• AI/ML specific disclosures if relevant. | Checklist provided; full IFU not supplied – gap. |
| **KGMP Certification** | Facility certificate for software development & distribution (if classified as Class II‑IV). | No KGMP evidence cited – gap. |
| **Post‑Market Surveillance Plan** | PMS plan, adverse event reporting procedure, periodic safety update report. | Not present in excerpt – required. |

---

### 5. Missing / Unverified Information (Human‑Escalation Triggers)

| Trigger | Reason & Action |
|---------|-----------------|
| **Intended Use not defined** | Classification cannot be finalized without explicit clinical purpose; escalate to product owner for clarification. |
| **Clinical Evidence absent** | For Class II, local clinical data or justified foreign data mapping is mandatory; request study protocol or CE/FDA dossier. |
| **Risk Management file incomplete** (e.g., AI/ML safety case) | If the device contains AI/ML algorithms, MFDS expects a dedicated risk‑benefit analysis – obtain from development team. |
| **KGMP certificate missing** | Verify whether the software is manufactured in a KGMP‑certified environment; if not, seek a compliance plan or consider re‑classification to Class I (if feasible). |
| **System log management (S‑10) only recommended** | For devices handling personal health data, MFDS may treat logs as mandatory; request justification. |
| **Korean language IFU incomplete** | Any missing translation of the checklist items triggers a labeling deficiency – task translation team. |
| **Cybersecurity plan outdated** | Verify that the “MFDS 사이버보안 가이드라인 2025.01” version referenced is the latest. If newer guidance exists, obtain updated controls. |
| **No specific case identifiers in source** | “no specific identifier found in source — verify separately” for any predicate device numbers, FDA 510(k) or EU CE numbers that might support a bridge claim. |

---

### 6. Recommended Evidence Package (Submission Checklist)

1. **Technical Documentation** – software description, versioning matrix, update policy, system specs, interface list (S‑1 ~ S‑5).  
2. **Cybersecurity Dossier** – configuration guide, patch SOP, residual risk register (S‑6 ~ S‑8), optional log management plan (S‑10).  
3. **Risk Management File** – IEC 62304 life‑cycle activities, IEC 60601‑1‑2 hazards, AI/ML safety case if applicable.  
4. **Clinical Evaluation Report** – Korean language clinical data or justified foreign data mapping per MFDS scope expansion notices.  
5. **KGMP Certificate** (or exemption justification).  
6. **Labeling & IFU** – complete Korean labeling set meeting the “디지털의료기기 특화 표시기재 요건 체크리스트”.  
7. **Post‑Market Surveillance Plan** – PMS activities, adverse event reporting flowchart.  
8. **Declaration of Conformity** – cross‑referencing ISO 13485 and IEC 62304 compliance.  

---

### 7. Peer Review Prompt

> *Please review the assumptions above, especially the inferred Class II designation and the completeness of the cybersecurity checklist items (S‑6 ~ S‑8). Confirm whether any additional MFDS notices (e.g., post‑2025 scope expansions) might allow partial reliance on foreign clinical data for this device. Also check that all Korean language labeling obligations have been captured, and flag any jurisdiction‑specific gaps not addressed in the current evidence package.*

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

1. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

2. Chunk `124386539616979555`

> ## 3. 디지털의료기기 특화 표시기재 요건 체크리스트 > 일반 의료기기 표시기재 필수사항(→ IFU_필수요소_3지역_비교.md 참조)에 **추가**되는 항목

### kb-eval-20260722-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "be6f64cd81f77320", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "fea1a1e441cf787fd39d9734c1e90c658fef8dc7f0c2e0522a9a6e101555afce"} -->

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

> **Regulatory Draft – MF DS Classification & Licensing Route for a GUI‑Based Digital Medical Product (software)**  

---

### 1. Governing Korean Notices  
| Topic | Notice name | Notice No. | Effective / Implementation date |
|------|--------------|-----------|---------------------------------|
| Approval, certification, notification and review procedures for digital medical products | **디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정** | **제2025‑25호** | 2025‑04‑15 |
| Classification system & grade criteria for digital medical products | **디지털의료제품의 분류 및 등급 지정 등에 관한 규정** | **제2025‑23호** | 2025‑04‑07 |
| Digital GMP (quality‑management) standards – 8 product‑type groups, AI/ML included | **디지털 의료기기 제조 및 품질관리 기준 (디지털 GMP)** | *Separate notice* (implementation scheduled for 2025) | 2025‑??‑?? (to be confirmed) |

> **Citation rule**: The above notices are established regulatory references (Category 1). They are cited as facts and carry no “verify” caveat.

---

### 2. Preliminary Classification & Submission Route  

| Step | Action | Expected Outcome |
|------|--------|-------------------|
| **2‑1. Identify intended use** – e.g., “Provides clinicians with a graphical user interface for viewing patient‐generated ECG data and offering decision support.” | Needed to locate the correct entry in **제2025‑23호** classification table (software‑only, GUI, clinical decision support). |
| **2‑2. Map to risk class** – The classification table distinguishes four grades (Ⅰ–Ⅳ). Most pure‑GUI software without direct therapeutic function is classified **Class II** under the “Software for information/monitoring” category, but verification against the exact clause in 제2025‑23호 is required. | If confirmed Class II → **허가·심사** (full approval) route under **제2025‑25호**.<br>If Class I → **신고** (notification) may be sufficient. |
| **2‑3. Determine applicable submission type** – For Class II: submit a **“디지털 의료제품 허가 신청”** (digital medical product approval). <br>For Class I: submit a **“디지털 의료제품 신고서”** (notification). | Route selection drives required dossier depth and MFDS review schedule. |

> **Human‑Escalation Trigger #1:** *If the intended‑use statement does not clearly fit any category in 제2025‑23호, escalate to senior RA for a formal classification request (MFDS “분류심의”).*

---

### 3. Required Evidence Package  

| Evidence | MFDS Requirement (notice) | International Equivalent |
|----------|---------------------------|----------------------------|
| **Device Description & Software Architecture** | Technical dossier section per 제2025‑25호 – includes UI flow, data handling, interoperability. | ISO 82304‑1, IEC 62304 (software life‑cycle). |
| **Risk Management File** | Risk analysis and control plan required under digital GMP (notice on 디지털 GMP) and MFDS “위험관리 기준”. | ISO 14971. |
| **Software Validation & Verification** | Mandatory for all digital products; includes unit, integration, system testing, usability test results. | IEC 62304 verification/validation activities. |
| **Clinical Evaluation / Performance Data** | For Class II‑IV: Korean clinical data or equivalence justification (foreign CE/FDA data may be incorporated if MFDS accepts under “foreign clinical evaluation report” scope). | FDA 510(k) clinical data, EU MDCG guidance. |
| **Cybersecurity & Data Privacy Controls** | Must satisfy MFDS “디지털 GMP” cybersecurity controls (e.g., encryption, access logging). | IEC 62443, ISO 27001. |
| **Labeling & IFU in Korean** | All labeling, instructions for use, and software user manual must be provided in Korean (per 제2025‑25호). | FDA 21 CFR 820.120, EU MDR Annex I. |
| **Quality Management System Evidence** | KGMP certification according to the digital GMP notice (type‑specific requirements, AI/ML modules included if applicable). | ISO 13485 + digital GMP annexes. |
| **Post‑Market Surveillance Plan** | PMCF plan, adverse event reporting procedures, periodic safety update. | MFDS “시판후조사” regulations, FDA Post‑market Surveillance. |

> **Human‑Escalation Trigger #2:** *Any missing clinical data (e.g., no Korean patient cohort) for a Class II/III device must be flagged; senior RA to decide on supplemental local study or exemption request.*

---

### 4. Identified Missing Information (from source excerpts)

| Item | Reason it is Needed | Current status in provided excerpt |
|------|---------------------|------------------------------------|
| **Exact intended‑use description** – determines classification entry. | Required to locate clause in 제2025‑23호. | Not present. |
| **Risk class (Ⅰ–Ⅳ) determination** – based on intended use & functionality. | Drives submission route (허가 vs 신고). | Not provided; only a note that “GUI SW 허가 시 적용”. |
| **Implementation status of 디지털 GMP** – the notice states “2025년 내 시행” and is marked “[검증 필요]”. | Evidence of compliance must be ready before filing. | Pending verification; timeline uncertain. |
| **Reference to any foreign regulatory clearance (FDA 510(k), CE mark, etc.)** – could reduce local data burden. | Needed for equivalence justification. | No identifier found in source – verify separately. |
| **Korean language labeling drafts** – mandatory for approval. | Must be submitted with dossier. | Not mentioned. |
| **Post‑market surveillance (PMS) strategy** – required for Class II+. | Required as part of technical file. | No detail provided. |

> **Human‑Escalation Trigger #3:** *If any of the above items remain unconfirmed 30 days before the planned filing date, raise a risk‑based escalation to project lead.*

---

### 5. Core Risk Controls (to be documented)

1. **Software Development Lifecycle (SDLC) controls** – IEC 62304 compliant processes, code reviews, configuration management.  
2. **Usability & Human Factors testing** – simulated clinician workflow with the GUI; capture use errors.  
3. **Cybersecurity safeguards** – encrypted data transmission, authentication, regular vulnerability assessments per 디지털 GMP.  
4. **AI/ML monitoring (if applicable)** – performance drift detection, periodic re‑training documentation.  
5. **Traceability matrix** – linking requirements → design → verification → validation → risk controls.  

---

### 6. Human‑Escalation Triggers Summary

| Trigger | Condition | Escalation Path |
|---------|-----------|-----------------|
| **#1 Classification Uncertainty** | Intended use does not map clearly to 제2025‑23호 table. | Notify senior RA → request formal MFDS classification review (분류심의). |
| **#2 Insufficient Clinical Evidence** | No Korean clinical data for Class II/III, and no acceptable foreign equivalence cited. | Senior RA + Clinical Affairs → design supplemental local study or seek exemption. |
| **#3 Digital GMP Compliance Gap** | “디지털 GMP 고시 시행” still marked *검증 필요* close to filing deadline. | Quality Manager → accelerate internal audit; if not resolved, postpone submission. |
| **#4 Missing Korean Labeling/IFU** | Drafts not available at dossier lock‑down. | Regulatory Project Lead → engage translation/vendor for urgent KOR materials. |
| **#5 Post‑Market Surveillance Plan Deficiency** | PMS plan incomplete or lacking risk‑based monitoring metrics. | Post‑Market Surveillance Team → draft & review before filing. |

---

### 7. Peer Review Request  

> *@RA‑Peer:* Please challenge the assumptions made above, especially:  
> - The inference that a pure‑GUI software would fall into Class II under 제2025‑23호 (verify against the exact clause).  
> - Whether the “디지털 GMP” notice’s pending implementation truly blocks submission or if provisional compliance is acceptable.  
> - Any jurisdiction‑specific gaps not covered by the excerpt, such as requirements for electronic health record integration or specific cybersecurity standards mandated after 2025.  

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

1. Chunk `1131342938714268388`

> ## 1. MFDS 고시 (식약처 고시) | 고시명 | 고시 번호 | 시행일 | 핵심 내용 | 자사 영향 | |---|---|---|---|---| | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정 | 제2025-25호 | 2025-04-15 | 허가·심사 절차, 서류 요건, 평가 기준 | GUI SW 허가 시 적용 | | 디지털의료제품의 분류 및 등급 지정 등에 관한 규정 | 제2025-23호 | 2025-04-07 | 디지털의료기기 분류 체계, 등급 기준 | GUI SW 해당 여부 판단 | | 디지털의료기기 제조 및 품질관리 기준 (디지털 GMP) | 별도 고시 | 2025년 내 시행 | 8개 유형군별 GMP 요건 (AI/ML 포함) | SW GMP 적용 기준 | ---

2. Chunk `385578214769089426`

> ## 5. 모니터링 포인트 | 항목 | 상태 | 확인 주기 | |---|---|---| | 디지털 GMP 고시 시행 | 2025년 내 예정 [검증 필요] | 분기별 확인 | | 디지털의료제품법 시행규칙 개정 (총리령 제2088호) | 2026-01-23 개정 완료 | — | | 추가 가이드라인 제정 | 지속 예고 중 | 월별 mfds.go.kr 확인 | | MFDS 6종 가이드라인 후속 개정 | 2025년 이후 수시 | 분기별 확인 | ---

### kb-eval-20260722-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "943f5314e1d782b1", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "5f0192e5896bd583833f41c673027bfe34b52793e1679d1f9dc751b5f77320c3"} -->

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

> **Regulatory Draft – MFDS Classification & Licensing Route (X‑ray System — generic)**  

---

### 1. Applicable Legal Framework  
| Level | Source (established reference) |
|-------|--------------------------------|
| **Medical Device Act** (법률) | MFDS “의료기기법” |
| **Enforcement Decree** (대통령령) | 시행령 |
| **Enforcement Rule** (총리령) | 시행규칙 |
| **MFDS Notices** | *“의료기기 품목 및 품목별 등급에 관한 규정”*  <br>*“의료기기 허가·신고·심사 등에 관한 규정”*  <br>*“의료기기 GMP 심사·평가 등에 관한 규정”* |
| **Guidance** | MFDS 민원인 안내서 (multiple guides) |

*(All references are drawn from the source excerpt [1] and represent confirmed regulatory documents.)*

---

### 2. Preliminary Classification & Submission Route  

| Step | Determination | Rationale / Evidence Needed |
|------|----------------|------------------------------|
| **Device Category** | **Medical Device – Imaging (X‑ray) System** | The source mentions “X‑ray System 전용” in the MFDS detailed guide (excerpt [2]). |
| **Risk Class (1‑4)** | **Class II or Class III** – *cannot be finalized* | Korean classification follows the “품목별 등급에 관한 규정”. For X‑ray systems, class is determined by: <br>• Radiation output and body part examined <br>• Intended use (diagnostic vs. therapeutic) <br>• Presence of software/hardware risk controls.  Without the specific technical specifications and intended use, the exact class cannot be assigned. |
| **Submission Type** | **허가 (Approval)** if Class III; **신고 (Notification)** if Class II | MFDS “허가·신고·심사 등에 관한 규정” requires approval for Class III devices and notification for Class II. The route therefore hinges on the final risk class. |

**Immediate Action Required:** Obtain a detailed device description, intended indication(s), radiation specifications (kV, mA, exposure time), and any software functions to apply the classification matrix in the “품목별 등급에 관한 규정”.

---

### 3. Core Evidence Package  

| Evidence | Requirement (per MFDS) | Current Status |
|----------|------------------------|----------------|
| **Technical dossier** (design history file, risk management file, device specification) | Mandatory for all classes; depth varies with class. | Not provided – *missing*. |
| **Non‑clinical testing** (electrical safety, EMC, radiation safety, biocompatibility if applicable) | Must follow relevant Korean Standards (KS) or IEC equivalents accepted by MFDS. | *Missing*. |
| **Clinical evaluation** | • For Class III: full clinical data or pivotal study in Korea.<br>• For Class II: may use foreign clinical evaluation report if MFDS has accepted it under the latest scope revision. | No clinical data referenced – *missing*. |
| **Foreign regulatory clearances (e.g., FDA 510(k), CE mark)** | Accepted as supporting evidence only when aligned with MFDS’s periodic scope extensions for OECD‑aligned non‑clinical data and foreign clinical reports (see MFDS “규정” updates). | No such identifiers appear in the source – *no specific identifier found in source — verify separately*. |
| **KGMP certification** | Required for manufacturing sites; must be verified by MFDS GMP inspection. | Not addressed – *missing*. |
| **Korean labeling & IFU** | All labeling, package inserts and user manuals must be provided in Korean (and possibly English as a supplement). | Not addressed – *missing*. |
| **Post‑market surveillance plan** | Must comply with MFDS “시판후조사” requirements. | *Missing*. |

---

### 4. Identified Gaps & Required Information  

1. **Device‑specific information** – intended use, target patient population, anatomical site, radiation output specifications, software functions.  
2. **Risk classification data** – mapping to the “품목별 등급에 관한 규정” matrix.  
3. **Technical documentation** – design dossier, risk management file (ISO 14971‑aligned).  
4. **Non‑clinical test reports** – electrical safety (IEC 60601‑1), EMC (IEC 60601‑1‑2), radiation safety (IEC 62471 or Korean equivalent).  
5. **Clinical evidence** – either local clinical study data or validated foreign clinical evaluation report.  
6. **Manufacturing compliance** – KGMP certificate for the production facility.  
7. **Korean language labeling & IFU** – full set of labels, packaging, and instructions in Korean.  
8. **Post‑market surveillance (PMS) plan** – description of vigilance activities, adverse event reporting process.

---

### 5. Core Risk Controls (to be reflected in the dossier)

| Control | Reference / Standard | Application |
|---------|----------------------|-------------|
| **Radiation safety** | IEC 60601‑2‑XX (X‑ray equipment) or Korean KS equivalents | Shielding design, dose monitoring, interlocks. |
| **Electrical safety** | IEC 60601‑1 (general requirements) | Protective earth, leakage current limits. |
| **EMC compliance** | IEC 60601‑1‑2 | Immunity and emission testing. |
| **Software validation** (if applicable) | IEC 62304 / MFDS guidance on software as a medical device | Development lifecycle, verification & validation activities. |
| **Usability engineering** | IEC 62366‑1 | Human factors analysis for operator interface. |
| **Biocompatibility** (if patient‑contacting components) | ISO 10993‑1 | Material testing per contact type. |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger & Rationale |
|-----------|---------------------|
| **Unclear classification** – device specifications unavailable or do not map cleanly to the “품목별 등급에 관한 규정”. | Escalate to senior RA for classification consultation and possible MFDS pre‑submission inquiry. |
| **Local clinical data required** – MFDS determines that foreign clinical evaluation is insufficient for the intended use. | Notify project lead; schedule Korean site clinical study or obtain local ethics approval. |
| **KGMP certification missing** – manufacturing site not yet inspected/approved by MFDS. | Pause submission until KGMP audit completed; involve quality assurance. |
| **Labeling non‑compliance** – Korean language labeling absent or incomplete. | Immediate correction required before dossier acceptance; alert packaging & marketing teams. |
| **Post‑market surveillance plan omitted** – no PMS strategy included. | Trigger internal compliance review; draft PMS plan in line with MFDS “시판후조사” rules. |

---

### 7. Peer Review Prompt  

> *@RA‑Peer:* Please examine the assumptions made above, especially the inference that the device falls under X‑ray system classification and the consequent risk class range (II–III). Verify whether any additional Korean notices (post‑2026) might broaden accepted foreign clinical evidence for imaging devices, and flag any jurisdiction‑specific gaps in the listed evidence requirements. Also assess if the identified risk controls align with the latest MFDS technical standards for X‑ray equipment.

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

### kb-eval-20260722-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "072d449c96fdd3f6", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

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

> **Regulatory Draft – Digital Medical Device (Software as a Medical Device, SaMD)**  

---

### 1. Classification & Licensing Route  
| Item | Determination |
|------|----------------|
| **Device type** | Software‑based medical device (SaMD) – indicated by “디지털의료기기” in the source excerpts. |
| **Regulatory classification** | Apply the MFDS SaMD classification rules (risk‑based classes I–III). The 2025 Digital Medical Device Law (“디지털의료제품법”) introduced a new SaMD classification system【2】. The exact class must be derived from the device’s intended purpose, algorithmic risk, and intended user (e.g., diagnostic vs. therapeutic). |
| **Submission pathway** | – If classified **Class I** → “신고” (notification) is sufficient.<br>– If **Class II/III** → full “허가” (approval) is required, following the MFDS medical‑device approval process. |
| **GMP requirement** | All digital medical devices now require a KGMP suitability assessment (GMP 적합인정). The GMP 인증 procedure follows the flowchart in source [1] and can be performed by one of six authorized agencies, including NIDS which began handling digital‑medical‑device GMP assessments from 2025‑01‑24【1】【2】. |

---

### 2. Evidence Package – Minimum Required Documents  

| Requirement | What to Provide | Reference |
|-------------|----------------|-----------|
| **KGMP suitability assessment** | Completed audit report, corrective‑action plan (if any), and KGMP certificate (validity 3 years). | GMP flow from source [1]; NIDS eligibility noted in source [2]. |
| **Device description & intended use** | Detailed product specification, software architecture diagram, risk classification justification (MFDS SaMD rules). | MFDS SaMD classification guidance (2025‑01‑24 amendment). |
| **Technical documentation** | Design history file, verification & validation reports (including cybersecurity and usability testing). | Standard practice under ISO 13485 / MFDS technical file requirements. |
| **Clinical evidence** | • For Class I – limited clinical data or literature review may suffice.<br>• For Class II/III – local clinical trial data *or* foreign clinical evaluation that meets the MFDS “foreign clinical evaluation report” acceptance criteria (currently allowed under recent notices). | MFDS guideline updates on AI/ML‑based SaMD (2025‑05‑07) and foreign evidence acceptance. |
| **Software safety & performance** | • Software risk management file (ISO 14971).<br>• Algorithm performance metrics, validation datasets, and a post‑market surveillance plan. | MFDS SaMD guidance (AI/ML GUI) 2025‑05‑07. |
| **Labeling & IFU** | Korean language labeling, user manual, and any required safety notices written in Korean. | MFDS labeling regulations (mandatory Korean translation). |
| **Regulatory history** | If the device has prior FDA 510(k) clearance or EU CE marking, include copies together with a cross‑reference to how those data satisfy MFDS non‑clinical/clinical requirements. | MFDS practice of accepting foreign evidence under specific notices (no notice number cited here; verify separately if needed). |

---

### 3. Missing Information – Items that Must Be Clarified Before Submission  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact intended use and risk claim** | Determines the MFDS class and whether local clinical data are mandatory. | Obtain a clear statement of indication, target population, and performance claims from the sponsor. |
| **Algorithmic detail (AI/ML model type, training data source, update mechanism)** | The 2025‑05‑07 guideline adds explicit requirements for AI/ML‑based SaMD. | Provide full algorithm description, data provenance, and a change‑management plan. |
| **Evidence of conformity to the new Digital Medical Device Law** (e.g., compliance checklist). | New law may impose additional safety or documentation obligations beyond classic medical‑device rules. | Request sponsor’s self‑assessment against the 2025‑01‑24 provisions. |
| **Decision on GMP audit agency** – whether NIDS or one of the other five agencies will conduct the assessment. | Choice influences timeline and required pre‑audit documents. | Confirm agency selection early; prepare agency‑specific submission checklists. |
| **Local clinical data requirement** – does the device qualify for reliance on foreign clinical evaluation? | MFDS may still demand Korean patient data for high‑risk (Class III) devices. | Perform a gap analysis between foreign data and MFDS acceptance criteria; plan local trial if needed. |
| **Post‑market surveillance (PMS) strategy** – especially for software updates. | PMS is mandatory for all SaMD, with stricter requirements for AI/ML systems. | Draft a PMS plan that includes real‑world performance monitoring, incident reporting, and update risk assessment. |

---

### 4. Core Risk Controls to Address in the Submission  

1. **Software life‑cycle management** – conform to IEC 62304; include verification & validation at each development phase.  
2. **Cybersecurity** – perform threat modeling (ISO 27001/IEC 62443), implement secure update mechanisms, and provide a security risk assessment report.  
3. **Usability / Human factors** – conduct formative/usability testing per IEC 62366‑1; include UI screenshots and task analysis.  
4. **Data integrity & privacy** – demonstrate compliance with Korea’s Personal Information Protection Act (PIPA) for any patient data collected.  
5. **Algorithm performance monitoring** – define key performance indicators, drift detection procedures, and a process for algorithm retraining/validation.  

---

### 5. Citations  

| Source | Content Cited |
|--------|----------------|
| 【1】 | GMP 적합인정 절차 (application → audit → certification) and list of six authorized agencies, including NIDS beginning digital‑medical‑device GMP assessments from 2025‑01‑24. |
| 【2】 | Regulatory change timeline: implementation of the Digital Medical Device Law (SaMD classification & approval changes), NIDS’ expanded GMP role, AI/ML‑based GUI SaMD guidance released 2025‑05‑07, upcoming autonomous performance certification, and negative‑type change notification system expected 2026. |

*No specific identifier (e.g., predicate number, case ID) appears in the source excerpts; therefore none is provided.*  

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for Escalation |
|--------|-----------------------|
| **Unclear device class** after risk analysis – cannot finalize submission route. | Requires senior RA or regulatory affairs manager to decide whether a Class II/III approval is needed. |
| **Missing local clinical data** for a high‑risk (Class III) SaMD where foreign evidence is insufficient. | Needs sponsor decision on conducting a Korean trial; timeline impact must be reviewed by project lead. |
| **GMP audit agency selection conflict** (e.g., sponsor prefers non‑NIDS agency but NIDS has mandatory jurisdiction under new law). | Must be escalated to the compliance officer to verify statutory requirement and negotiate with sponsor. |
| **Algorithm change management plan not aligned with MFDS “autonomous performance certification” upcoming 2026**. | Escalate to the product manager & legal counsel to align update strategy with forthcoming regulatory framework. |
| **Labeling/IFU not fully translated into Korean** or missing required safety statements. | Immediate escalation to translation team and QA for compliance before filing. |
| **Any identified defect in KGMP audit report (Critical/Major)** after field inspection. | Must be reported to the sponsor’s quality assurance lead and to MFDS within statutory timelines; senior RA oversight required. |

---

### 7. Peer Review Prompt  

> *Can a fellow RA challenge the assumptions made about the applicability of foreign clinical evidence, confirm that all relevant Korean‐specific obligations (GMP agency choice, Korean labeling, AI/ML risk assessment) have been captured, and verify whether any additional notices beyond those cited might affect this SaMD’s classification or submission route?*

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

### kb-eval-20260722-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "579e45460fb897c7", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "f9e5d750ee9a694d60d790e8cbb66ce476876d3b5259fe0c129772f76a83a002"} -->

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

> **Regulatory Draft – Digital‑Medical Device (SaMD/AI) under the 디지털의료제품법**

---

### 1. Applicable Legal Framework  

| Element | Reference |
|---------|-----------|
| **Law** | *디지털의료제품법* (법률 제20139호, 시행일 2025‑01‑24)【1002132727008468922】 |
| **Enabling Decree** | 대통령령 제35219호 (2025‑01‑23 시행)【1002132727008468922】 |
| **Enforcing Ordinance** | 총리령 제1958호 (2025‑02‑28 시행)【1002132727008468922】 |
| **Regulatory Authority** | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과【1002132727008468922】 |
| **Key Implementing Rules** | *디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정* (주요 하위고시) – governs classification, licensing routes and evidentiary requirements. |

---

### 2. Device Classification & Submission Pathway  

| Risk‑Based Class (예시) | Typical MFDS Route | When Used |
|------------------------|--------------------|-----------|
| **Class I** (low risk) | 신고 (사전신고) | Simple health‑monitoring apps, non‑diagnostic functional support. |
| **Class II** (moderate risk) | 인증 (인증심사) | Devices with limited decision‑support, e.g., symptom checkers, basic image viewers. |
| **Class III** (high risk) | 허가 (허가심사) | AI‑driven diagnostic or therapeutic SaMD, especially those that output clinical decisions (e.g., AI‑based lesion detection). |

> **Determination needed:** The exact class hinges on the device’s intended use, algorithmic function and impact on patient management. Without a stated indication, a definitive classification cannot be assigned.

**Regulatory rule citation** – MFDS classification rules are contained in the *디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정* (referenced in the law’s “주요 하위고시”). This source is an established regulation; no speculative identifier is introduced.

---

### 3. Mandatory Evidence Package  

| Evidence Type | Required for Class I | Required for Class II | Required for Class III |
|---------------|----------------------|-----------------------|------------------------|
| **Technical Documentation (Design Dossier)** | ✔︎ 기본 설계·구조 설명 | ✔︎ 상세 설계·소프트웨어 아키텍처, 데이터 흐름도 | ✔︎ 전체 개발 프로세스, 위험관리 파일 (ISO 14971 기반) |
| **Software Validation & Verification** | ✔︎ 기능 테스트 보고서 | ✔︎ V‑V 계획·보고서, 알고리즘 검증 (데이터셋·성능 지표) | ✔︎ 추가 임상 성능 평가, 외부 데이터 재현性 검증 |
| **Clinical Evaluation** | ✖︎ 일반적으로 면제 | ✔︎ 문헌 기반 임상 근거(국내/외) | ✔︎ 국내 임상시험 또는 현지 실사용데이터 (MFDS 가이드라인에 따라) |
| **Korean Language Labeling & IFU** | 필수 (한글) | 필수 (한글 + 영어 선택) | 필수 (한글, 필요 시 영·중 등 다국어) |
| **KGMP Certification** | 해당 없음 (소프트웨어‑only) | 경우에 따라 제조공정이 포함될 때 KGMP 적용 | 반드시 KGMP(디지털의료기기 제조 및 품질관리 기준) 인증 필요 |
| **Cybersecurity Evidence** | ✖︎ 기본 보안 설계 | ✔︎ 사이버보안 가이드라인 적용 (2025‑01‑10)【1077225675205822581】 | ✔︎ SBOM 관리, 침해 대응 절차 포함 (동일 가이드라인)【1077225675205822581】 |
| **Foreign Evidence Acceptance** | – | MFDS는 OECD‑aligned 비임상 데이터 및 해외 임상 평가 보고서를 인정(주기적 Scope 확대) — specific notice numbers must be verified from the latest MFDS 공고. |

> **Note on foreign evidence:** The source confirms that MFDS periodically expands acceptance of overseas data, but does not list a concrete notice number. Verify the current notice (e.g., 2025‑02 MFDS 고시) before relying on foreign clinical data.

---

### 4. Missing Information – Items to Clarify with Sponsor  

1. **Intended Use & Indication** – precise clinical claim, target patient population, and care pathway.  
2. **Algorithmic Functionality** – whether the AI module performs detection, classification, risk prediction, or decision support.  
3. **Risk Classification Rationale** – mapping to MFDS Class I‑III criteria (requires a formal risk analysis).  
4. **Clinical Data Strategy** – domestic clinical trial plan, or justification for reliance on foreign data (including reference to the specific MFDS notice that permits it).  
5. **Software Architecture Details** – description of modules, embedded firmware vs. cloud service, update mechanism.  
6. **Cyber‑security Measures** – SBOM generation process, vulnerability management schedule, incident response plan (required for Class II/III per 2025‑01‑10 guideline【1077225675205822581】).  
7. **Manufacturing Facility Status** – KGMP certification status if any hardware or firmware production is in‑house.  

Until these items are provided, the submission pathway and evidence completeness cannot be finalized.

---

### 5. Core Risk Controls (per ISO 14971 & MFDS guidelines)  

| Control | Applicability |
|---------|---------------|
| **Functional Safe‑Design** – algorithmic limits, fail‑safe default output | All classes (mandatory for AI) |
| **Usability Engineering (Human‑Factors)** – IEC 62366‑1 compliance | Class II/III |
| **Cybersecurity Controls** – network isolation, encryption, SBOM, regular patching | Class II/III (per 2025‑01‑10 cyber‑security guideline)【1077225675205822581】 |
| **Post‑Market Surveillance Plan** – real‑world performance monitoring, adverse event reporting (시판후조사) | All classes; intensified for Class III |
| **Software Lifecycle Management** – IEC 62304 conformity, version control, traceability matrix | All software‑only devices |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger | Action Required |
|-----------|---------|-----------------|
| **Unresolved Classification** – sponsor cannot supply a clear risk justification | *Escalate to MFDS* via pre‑submission consultation (문의) before dossier preparation. |
| **Missing Korean IFU/Labeling** – only English documentation provided | Halt submission; require certified Korean translation & labeling review. |
| **Absence of KGMP Certification for Class III** | Immediate pause – device cannot proceed to 허가 without compliance to the “디지털의료기기 제조 및 품질관리 기준”. |
| **Inadequate Clinical Evidence** – reliance solely on foreign data without a current MFDS notice permitting it | Request sponsor to either conduct domestic clinical study or furnish the specific MFDS 고시 number that authorizes foreign data usage. |
| **Cybersecurity Gaps** – SBOM not generated for a network‑connected device (Class II/III) | Trigger internal security audit; require remediation before dossier submission. |
| **Regulatory Update Detected** – new amendment to the 디지털의료제품법 or related guidelines after 2025‑02‑28 | Re‑review classification and evidence requirements; if impact is material, inform sponsor and pause current work package. |

---

### 7. Citations Summary  

- **Legal Basis:** *디지털의료제품법* (법률 제20139호, 시행일 2025‑01‑24)【1002132727008468922】  
- **Enabling Decree & Ordinance:** 대통령령 제35219호; 총리령 제1958호【1002132727008468922】  
- **Guidelines (2024–2025):**  <br>• *디지털치료기기 임상시험 설계 가이드라인* (2024‑12) – low relevance. <br>• *생성형 AI 의료기기 허가·심사 가이드라인* (2025‑01) – medium relevance. <br>• *독립형 디지털의료기기SW 사용적합성 가이드라인* (2025‑01) – high relevance. <br>• *의료기기 사이버보안 허가·심사 가이드라인(개정)* (2025‑01‑10) – high relevance【1077225675205822581】 <br>• *디지털의료기기 전자적 침해행위 보안 지침(안)* (2025‑01) – high relevance【1077225675205822581】  

No specific case identifiers (e.g., K‑numbers, 510(k) predicates) appear in the source excerpts; therefore none are inserted.  

---

### 8. Human‑Escalation Outlook  

- **Primary escalation point:** MFDS Digital‑Health Regulation Support Team (의료기기정책과 / 디지털헬스규제지원과).  
- **Secondary internal review:** KGMP compliance office for manufacturing certification status.  
- **Timing:** Escalate immediately upon any of the triggers in Section 6, and document the escalation log in the work package comments.

---

**Peer‑Review Prompt**  

> *Please review this draft and challenge the following:* <br>
> 1. **Assumptions about classification** – Is it appropriate to present Class I/II/III as a three‑tier model without device‑specific indication? <br>
> 2. **Scope of evidence** – Are any additional Korean‑required artifacts (e.g., EMC test reports, radiation safety for AI‑enabled imaging) missing from the table? <br>
> 3. **Jurisdiction‑gap coverage** – Does the draft adequately flag all MFDS‑specific language and labeling obligations, especially concerning post‑market surveillance plans under 시판후조사?  

Your feedback will be incorporated before finalizing the submission plan.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 81/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,024자 | — |
| 규제 식별자 인용 | 3개 | — |
| source excerpt 근거 일치 | **0/3 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 3개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
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

1. Chunk `1002132727008468922`

> ## 1. 법령 개요 | 항목 | 내용 | |------|------| | 법률명 | 디지털의료제품법 (법률 제20139호, 제정 2024-01-23) | | 시행일 | 2025-01-24 | | 시행령 | 대통령령 제35219호 (2025-01-23 제정, 2025-01-24 시행) | | 시행규칙 | 총리령 제1958호 (2025-02-28 시행) | | 소관 | 식품의약품안전처(MFDS) 의료기기정책과 / 디지털헬스규제지원과 | | 주요 하위고시 | 디지털의료제품 허가·인증·신고·심사 및 평가 등에 관한 규정, 분류 및 등급 지정 규정, 디지털의료기기 제조 및 품질관리 기준, 디지털의료기기 전자적 침해행위 보안 지침(안) |

2. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |
