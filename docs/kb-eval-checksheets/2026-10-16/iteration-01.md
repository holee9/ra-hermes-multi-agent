# KB Eval Checksheet - 2026-10-16 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261016-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "f752c4fa6541475e", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md", "source_hash": "36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `f752c4fa6541475e`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/FDA_임상데이터_필요판단_기준.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/FDA_%EC%9E%84%EC%83%81%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%95%84%EC%9A%94%ED%8C%90%EB%8B%A8_%EA%B8%B0%EC%A4%80.md)
- Source hash: `36bd116935f14eabbb867a3aeb97bd412eb5fde54252dad2ed0af45a4b2adb4e`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `FDA_임상데이터_필요판단_기준.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-...
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

> **Regulatory Draft – Evidence‑Gap Assessment & Submission Planning**

---

### 1. Device Classification & Preferred Premarket Pathway  

| Decision point | Determination (based on source) | Citation |
|----------------|----------------------------------|----------|
| **Legal basis** | 510(k) – FD&C Act §510(k), 21 CFR §807 | 【2†L3-L4】 |
| **Alternative routes** | De Novo – FD&C Act §513(f)(2), 21 CFR §860; PMA – FD&C Act §515, 21 CFR §814 | 【2†L3-L5】 |
| **Typical class** | Class I‑II (default) for 510(k); some novel Class I‑II may qualify for De Novo; Class III requires PMA | 【2†L4-L6】 |
| **Predicate requirement** | Mandatory for 510(k); not required for De Novo or PMA | 【2†L7-L9】 |
| **Clinical data trigger** | Conditional for 510(k) – see §3 of the FDA “clinical‑data need” guidance; mandatory for PMA; optional (“if applicable”) for De Novo | 【2†L10-L12】 |

> **Bottom line:** If a reasonable predicate exists and the device does not raise new safety/efficacy concerns, pursue 510(k). Absence of a suitable predicate or a novel indication pushes toward De Novo (Class I‑II) or PMA (Class III).

---

### 2. Required Evidence Package – Minimum Elements  

| Submission type | Core evidence (per FDA guidance) | Notes on gaps |
|-----------------|----------------------------------|---------------|
| **510(k)** | • Device description & specifications  <br>• Comparison to identified predicate (including technological characteristics, intended use, performance) <br>• Risk analysis (ISO 14971‑aligned) <br>• Non‑clinical bench testing (electrical safety, EMC, software verification/validation if applicable) <br>• Clinical data **only if** the FDA’s “conditional” trigger applies (§3 reference) | *Missing:* Predicate identification; determination whether §3 triggers clinical data. |
| **De Novo** | • Device description & intended use  <br>• Novelty justification (why no predicate) <br>• Comprehensive risk assessment (ISO 14971) <br>• Non‑clinical testing as above <br>• Clinical data **if applicable** (“if applicable” language in source) | *Missing:* Statement of “no reasonable predicate”; clinical data applicability assessment. |
| **PMA** | • Full investigational plan & results (IDE‑compliant clinical trial)  <br>• Detailed non‑clinical testing <br>• Manufacturing QMS compliance (21 CFR §820 – QMSR, effective Feb 2026) <br>• Labeling, UDI (21 CFR §830)  | *Missing:* Complete IDE protocol & data; validated QMS documentation; UDI strategy. |

---

### 3. Identified Evidence Gaps  

| Gap | Why it matters | Immediate action |
|-----|----------------|------------------|
| **Predicate device (for 510(k))** | Required to demonstrate substantial equivalence. Without it, the submission reverts to De Novo or PMA. | Search FDA’s 510(k) database; compile FDA‑cleared devices with same intended use & technology. |
| **Clinical data applicability (§3 conditional trigger)** | Determines whether a clinical study is needed for 510(k). | Perform “clinical‑data need” assessment using the FDA guidance linked in source [1]; document rationale. |
| **Risk management file (ISO 14971)** | Required for all pathways; supports safety controls & labeling. | Compile hazard analysis, risk controls, residual risk justification. |
| **QMSR compliance evidence** | New QMS regulation (21 CFR §820) will be inspected for PMA and required for 510(k) submissions after Feb 2026. | Verify ISO 13485‑aligned processes; generate SOPs, CAPA records. |
| **UDI plan (21 CFR §830)** | Mandatory labeling element for Class II & III devices. | Develop UDI issuance strategy, label mock‑ups, GUDID submission schedule. |
| **eSTAR reporting obligations** | For 510(k) submissions after Oct 2023; De Novo after Oct 2025. Non‑compliance leads to enforcement. | Confirm whether the device falls under eSTAR (date range provided in source [2]); prepare electronic submission system readiness. |

---

### 4. Core Risk Controls & Compliance Elements  

| Control | Regulatory reference | Implementation tip |
|--------|----------------------|--------------------|
| **Design Controls** (21 CFR §820.30) | QMSR – Part 820 (effective Feb 2026) | Map design history file to SOP‑DC‐XXX; link risk analysis outputs. |
| **Predetermined Change Control Plan (PCCP)** | FDA Guidance, Dec 2024 (AI/ML devices) | If software‑intensive, draft a PCCP outlining allowed post‑market changes. |
| **Usability Engineering** (IEC 62366‑1) | Recommended for Class II imaging software | Conduct formative/usability testing; document findings in the UCD file. |
| **Cybersecurity** (NIST SP 800‑53 / FDA guidance) | Part 820, implied requirement | Perform threat analysis; implement firmware authentication & update mechanisms. |
| **Post‑Market Surveillance** (21 CFR §822) | Required for PMA and recommended for 510(k) Class II | Develop PMS plan aligned with eSTAR timeline. |

---

### 5. Human‑Escalation Triggers  

| Trigger condition | Reason to escalate to senior RA / regulatory counsel |
|-------------------|------------------------------------------------------|
| **No clear predicate** after exhaustive database search (≥3 days effort) | Decision point between 510(k) and De Novo; impacts timeline & fees. |
| **Clinical‑data need assessment yields “conditional” but evidence is ambiguous** | Risk of an FDA request for additional clinical information (AI). |
| **eSTAR reporting window missed or unclear applicability** | Potential enforcement action; requires immediate senior oversight. |
| **QMSR gap identified that cannot be closed within the planned submission timeline** | May force a delayed filing or change in pathway (e.g., switch to De Novo). |
| **UDI issuance agency not yet accredited** | Must obtain FDA or accredited issuing agency before labeling finalization; escalates to compliance leadership. |

---

### 6. Conclusion & Immediate Next Steps  

1. **Predicate Confirmation:** Assign a team member to search for a suitable 510(k) predicate (target: 2 business days).  
2. **Clinical‑Data Need Assessment:** Apply the FDA §3 criteria using the guidance linked in source [1]; document decision and any data gaps.  
3. **Compile Risk Management & QMSR evidence** to satisfy Part 820 requirements; schedule internal audit of SOPs.  
4. **Develop UDI plan** (label mock‑up, GUDID entry draft).  
5. **Prepare eSTAR readiness checklist** based on the device’s submission date and applicable timeline from source [2].  

If any of the escalation triggers are hit, raise to senior RA immediately.

---

### Peer‑Review Prompt  

> *Colleague, please challenge the assumptions above: (1) Is a predicate truly required for our intended indication, or could we justify De Novo earlier? (2) Does the “conditional” clinical‑data trigger in §3 apply given our device’s risk profile? (3) Are there any jurisdiction‑specific items (e.g., state‑level regulations, foreign market considerations) that the source does not cover but we must address now?*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1031369836908836097`

> > 최종 갱신: 2026-05-19 (자동보강 #53) > 근거: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-clinical-studies | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-submission-510ks-solid-state-x-ray-imaging-devices | https://www.fda.gov/media/171837/download # FDA 임상데이터 필요 판단 기준: 510(k) vs De Novo vs PMA

2. Chunk `1091338218782097995`

> ## 2. 경로별 규제 근거 요약 | 항목 | 510(k) | De Novo | PMA | |---|---|---|---| | 법적 근거 | FD&C Act §510(k), 21 CFR 807 | FD&C Act §513(f)(2), 21 CFR 860 | FD&C Act §515, 21 CFR 814 | | 대상 등급 | Class I·II (원칙), 일부 III | Class I·II (신규 기기) | Class III | | Predicate 필요 | 필수 | 불필요 | 불필요 | | 임상데이터 | 조건부 (§3 참조) | "if applicable" | 필수 | | FDA 심사 기간 | 90일 (목표) | 150 review days | 180일 (목표) | | 결과 | "Cleared" (SE 결정) | Grant (신규 분류 수립) | "Approved" | | eSTAR 의무 | 2023-10-01~ | 2025-10-01~ | 해당 없음 | | User Fee (FY2025) | 약 $22,171 | 약 $46,875 | 약 $438,330 | ---

### kb-eval-20261016-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "5047f79cf3f12f1f", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md", "source_hash": "b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `5047f79cf3f12f1f`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/FDA_AI_Additional_Information_%EB%8C%80%EC%9D%91_%EC%A0%84%EB%9E%B5.md)
- Source hash: `b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82`
- Focus: submission evidence gaps
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `FDA_AI_Additional_Information_대응_전략.md`는 FDA AI/ML 의료기기 심사 중 additional information 또는 deficiency response 대응 전략 문서입니다.
- 현재 excerpt 핵심: ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합 > 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: htt...
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

> **Regulatory Draft – FDA 510(k) Additional‑Information (AI) Response Plan**

---

### 1. Device & Intended Use (Gap)
| Item | Current Status | Action / Escalation |
|------|----------------|---------------------|
| **Device name, model, and catalog number** | Not provided in source material | Obtain from the sponsor’s design history file (DHF). <br>*Escalate to Project Lead if not received within 2 business days.* |
| **Intended use / indication for use (IFU)** | Missing – required to anchor classification & predicate selection | Request a finalized IFU draft. <br>*Escalate to Clinical Affairs lead if overdue >3 days after request.* |
| **Device classification (Class I‑III) and applicable product code** | Not determinable from excerpt; assumed Class II pending review of technology (e.g., imaging, software). | Conduct a *Classification Determination* (21 CFR 807.92) using intended use and predicate comparison. <br>*Escalate to Senior RA if classification cannot be resolved within 5 working days.* |

---

### 2. Recommended Submission Route  
| Criterion | Recommendation |
|-----------|----------------|
| **Likely pathway** | Premarket Notification (510(k)) – §807.92 (substantial‑equivalence) **unless** the device is novel high‑risk (Class III) → De Novo. |
| **Regulatory references** | • 21 CFR 807 – Premarket notification procedures (framework reference). <br>• 21 CFR 820 – Quality Management System Regulation (QMSR) (effective Feb 2026, ISO 13485‑aligned). <br>• 21 CFR 830 – UDI labeling requirements. |
| **If imaging** | Verify Part 892 classification; e.g., §892.2050 for image‑management software (framework reference). *No specific section found in source – verify separately.* |

---

### 3. Evidence Required to Satisfy the AI Request  
(derived from FDA “Additional Information” guidance – Oct 2022, cited in source)

| Evidence Category | Typical Requirement | Current Gap (per AI) | Remedy |
|-------------------|---------------------|----------------------|--------|
| **Device description & comparison** | Detailed block diagram; identification of predicate device(s). | Predicate not identified. | Perform a *predicate search* and create a side‑by‑side matrix. |
| **Performance testing** | • Bench (functional, electrical safety, electromagnetic compatibility). <br>• Software verification/validation (if applicable). <br>• Human factors validation. | No test reports supplied for the newly added algorithm. | Generate & include complete verification/validation reports; reference FDA guidance on software pre‑market submissions. |
| **Clinical data** | • Clinical performance study or literature‑based equivalence.<br>• PMCF plan (for Class IIb/III). | Clinical Evaluation insufficient; no post‑market surveillance plan. | Prepare a *Clinical Evaluation Report* following MEDDEV 2.7/1 rev 4 and draft a *Post‑Market Clinical Follow‑up (PMCF) Plan*. |
| **Risk Management** (ISO 14971) | Full risk analysis, risk evaluation, risk control measures, residual risk justification. | ISO 14971 file labeled “부적합” in EU MDR note; no U.S. version provided. | Translate/align the risk management file to FDA expectations; include verification of each risk control. |
| **Labeling & UDI** | • Device label & Instructions for Use (IFU). <br>• UDI carrier compliant with 21 CFR 830.10‑§830.60. | Label draft missing device symbols, and no UDI assigned. | Develop compliant labeling package; request a HHS‐approved issuing agency for UDI. |
| **Sterilization / Shelf‑life (if applicable)** | Validation of sterilization process + stability data. | Not mentioned in AI. | Verify necessity based on intended use; add if required. |
| **Software documentation** (if device includes software) | • Software Description, Architecture Diagram.<br>• Predetermined Change Control Plan (PCCP) – FDA final guidance Dec 2024. | No PCCP referenced. | Draft a *Predetermined Change Control Plan* and attach as Appendix. |

---

### 4. Risk Controls to Emphasize in the AI Response  
| Control | How it Meets FDA Expectation |
|---------|------------------------------|
| **Design Input Verification** | Demonstrate traceability from intended use to design specifications (21 CFR 820.30). |
| **Process Validation** | For manufacturing steps that affect device performance, provide process validation reports (820.70). |
| **Software Lifecycle Management** | Include software risk controls per IEC 62304 and the PCCP (FDA guidance Dec 2024). |
| **Human Factors Engineering** | Usability testing results aligned with FDA Human Factors Guidance (no specific identifier in source – verify separately). |
| **Post‑Market Surveillance** | Outline a PMCF plan that feeds back into risk management updates per 21 CFR 822.30 (if Class IIb/III). |

---

### 5. Citations  

| Topic | Source Type | Citation Detail |
|-------|-------------|-----------------|
| FDA AI‑response strategy | Guidance document titled “FDA and Industry Actions on 510(k) Submissions, Oct 2022” – referenced in source excerpt 2. | No specific identifier found in source — verify separately. |
| Additional information response templates | Medical Device Academy website (AI response samples) – referenced in source excerpt 2. | No specific identifier found in source — verify separate. |
| MDUFA V Commitment Letter | FDA MDUFA V Commitment Letter (2023‑2025) – referenced in source excerpt 2. | No specific identifier found in source — verify separately. |
| EU MDR deficiency points (GSPR, Clinical Evaluation, PMCF, ISO 14971) | EU MDR NB Deficiency Letter – excerpt 1. | No specific identifier found in source — verify separately. |
| Classification & 510(k) pathway | 21 CFR 807 (framework reference). | Framework reference – no verification needed. |
| QMSR requirements (ISO 13485‑aligned) | 21 CFR 820 (framework reference). | Framework reference – no verification needed. |
| UDI labeling obligations | 21 CFR 830.10‑§830.60 (framework reference). | Framework reference – no verification needed. |
| Imaging device class (if applicable) | Part 892 §892.2050 for image‑management software (framework reference). | No specific identifier found in source — verify separately. |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Who to Escalate To | Deadline |
|--------------------|-------------------|----------|
| **Unresolved classification** after 5 working days of request for intended use/ predicate information. | Senior Regulatory Affairs Manager (RA Lead). | Immediate upon deadline expiry. |
| **Missing clinical evaluation or PMCF evidence** that cannot be generated within the FDA AI response timeline (typically 30 calendar days). | Project Director & Clinical Affairs Lead. | 48 hours before AI response due date. |
| **Risk Management file still flagged as non‑conforming** after proposed revisions. | Quality Assurance Manager. | Within 2 working days of final risk analysis draft. |
| **AI response draft exceeds word/page limits or lacks required sections** (labeling, UDI, PCCP). | Head of Regulatory Affairs. | Prior to submission; at least 1 day for final review. |
| **Regulatory reviewer requests clarification on any cited evidence** that cannot be supplied within the standard 180‑day AI response window. | Chief Compliance Officer. | Immediately upon receipt of the request. |

---

### 7. Summary Judgment  

*The device appears to require a 510(k) submission; the FDA AI request highlights gaps in predicate identification, clinical evaluation, risk management, labeling/UDI, and software change‑control documentation. A coordinated effort to close these evidence gaps—leveraging ISO 14971 risk analysis, IEC 62304/software controls, and a robust PMCF plan—is required before the AI response deadline.*  

All identified gaps must be addressed, documented, and reviewed per the escalation matrix above.

---

**Peer Review Prompt**

> *Colleague RA, please review: (1) our assumption that the device falls under a Class II 510(k) pathway; (2) completeness of the evidence checklist against the AI guidance cited; and (3) any jurisdiction‑specific items we may have missed (e.g., FDA’s recent QMSR updates or UDI carrier requirements).*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> EU 용어 혼입 — 원문의 'EU MDR NB Deficiency (참고)' 절(PMCF·Class IIb·30~90일)을 미국 510(k) AI 대응 증거표에 병합. FDA 대응 표에는 PMCF/Class IIb가 없어야 함(#146 G4 계열). AI 응답 기한 180일은 정확(이전 30일 창작 해소).


**Source Excerpts**

1. Chunk `1062884112493939033`

> ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합

2. Chunk `1076622801663602202`

> > 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: https://www.fda.gov/media/73507/download (FDA Guidance: FDA and Industry Actions on 510(k) Submissions, Oct 2022) | https://medicaldeviceacademy.com/additional-information-request/ | https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process | MDUFA V Commitment Letter https://www.fda.gov/media/158308/download # FDA Additional Information (AI) 대응 전략 및 샘플 답변 체계

### kb-eval-20261016-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "8c0d03f9fdbb5af5", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A2_Form3514_템플릿.md", "source_hash": "f07d857ec6943c9b00d268d9d425dd1a73e7e898cad79b2fac12450b3beb67f7"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `8c0d03f9fdbb5af5`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A2_Form3514_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/T-FDA510K-A2_Form3514_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `f07d857ec6943c9b00d268d9d425dd1a73e7e898cad79b2fac12450b3beb67f7`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `T-FDA510K-A2_Form3514_템플릿.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: --- doc-id: T-FDA510K-A2_Form3514_템플릿 title: FDA Form 3514 (CDRH Premarket Review Submission Cover Sheet) 작성 템플릿 type: Form version: v0.1 status: draft category: 01_법규_규제 purpose: FDA 510(k) RTA Checklist A.2 대응 — Form 3514 기재항목 골격, 제품별 실 데이터 작성 예정 applicable: [FDA 510(k), FDA QMSR] owner: RA 담당자 last-review: 2026-09-10 review-due: 2027-09-10 --- # T-FDA5...
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

> **Regulatory Draft – 510(k) Submission Gap Analysis**

---

### 1. Bottom‑Line Decision  
*Current information is limited to a generic Form 3514 template; no device‑specific data (e.g., intended use, predicate, risk profile) are available. Therefore the classification and exact submission pathway cannot be finalized at this stage.*  

**Recommended immediate action:** Obtain the missing product details (see Section 3) and perform a preliminary classification check in the FDA Product Code database. Until that is done, plan for a **Traditional 510(k)** (standard review) with the option to pivot to a **Special** or **Abbreviated** 510(k) if the device meets the relevant criteria.

---

### 2. Likely Classification / Submission Route  

| Step | What to Do | Reference |
|------|------------|-----------|
| **a. Determine product code & class** | Search FDA Product Code database using device description and intended use. Identify whether the regulation falls under a Class I, II or III designation (e.g., 21 CFR 860 for general medical devices; 21 CFR 892 for imaging). | 21 CFR §807.92(a)(3) – “substantial equivalence” definition |
| **b. Choose 510(k) type** | • If Class I → may be exempt; otherwise proceed with 510(k).<br>• If the device is substantially equivalent to a cleared predicate and meets all special‑submission criteria, consider **Special 510(k)** (21 CFR 807.92(c)).<br>• If recognized consensus standards cover most performance aspects, an **Abbreviated 510(k)** may be appropriate (21 CFR 807.92(b)). | 21 CFR §807.92 |
| **c. Apply QMSR** | All Class II/III submissions must demonstrate compliance with the new Quality Management System Regulation (QMSR) effective 02‑Feb‑2026, aligned to ISO 13485. | 21 CFR Part 820 (QMSR) |

*If the device is an imaging or radiology system, confirm the correct Section of 21 CFR Part 892 (e.g., §892.2050 for image management software). No definitive assignment can be made from the source – **verify separately**.*

---

### 3. Required Evidence Checklist (aligned to Form 3514 items)

| Category | Evidence Needed | Typical Sources / Tests |
|----------|----------------|------------------------|
| **Device Description & Intended Use** | Detailed narrative, indications for use (IFU), and labeling claims. | Product specification sheet; IFU draft. |
| **Predicate Device(s)** | 510(k) number(s), product code, comparison matrix. | FDA database search; prior cleared 510(k)s. |
| **Substantial Equivalence Argument** | Side‑by‑side comparison of technology, intended use, performance, labeling. | Narrative + tables per §807.92(a)(3). |
| **Performance Testing** | • Bench (electrical safety, EMC, mechanical)<br>• Biocompatibility (ISO 10993‑1) if patient-contact<br>• Software verification/validation (if applicable) | IEC 60601‑1, IEC 60601‑1‑2, FDA “General Principles of Software Validation” guidance. |
| **Clinical Evaluation** *(if required)* | Clinical data or literature supporting safety/effectiveness. | Existing clinical studies; literature review. |
| **Sterility / Shelf Life** *(if sterile)* | Sterilization validation, packaging integrity. | ASTM F1980, ISO 11135 etc. |
| **Labeling** | Full label set (label, IFU, packaging) meeting 21 CFR Part 801. | Draft labels; compliance checklists. |
| **UDI Configuration** | Device Identifier (DI), Production Identifier (PI), placement on label per §830.10‑§830.60. | GUDID registration plan. |
| **Risk Management** | ISO 14971 risk analysis file, design inputs/outputs, mitigations. | Risk Management Report (RM‑001). |
| **QMSR Documentation** | Design History File (DHF), Device Master Record (DMR), post‑market surveillance plan. | QMSR SOPs, CAPA records. |
| **Predetermined Change Control Plan (PCCP)** *(if AI/ML)* | Documented change‑control strategy approved by FDA. | PCCP template per Dec 2024 guidance. |

*All above items should be referenced in the final Form 3514 and associated submission modules.*

---

### 4. Identified Missing Information (Gap Summary)

| Gap | Why It Matters | Action |
|-----|----------------|--------|
| **Device name, model & detailed description** | Needed for product‑code lookup & predicate search. | Obtain from engineering/marketing. |
| **Intended use / Indications for Use** | Drives classification and required testing scope. | Draft IFU; confirm with clinical team. |
| **Predicate device(s) identification** | Core of 510(k) substantial equivalence argument. | Conduct FDA database search; list 510(k)#s. |
| **Performance test data (bench, biocompatibility, software V&V)** | Evidence of safety/effectiveness; FDA review focus. | Compile existing study reports or plan new testing. |
| **Labeling set & UDI strategy** | Required by 21 CFR Part 801 and Part 830. | Draft label package; develop GUDID entry. |
| **Risk Management file (ISO 14971)** | Demonstrates control of known hazards. | Produce RM report; link mitigations to design. |
| **QMSR compliance evidence** | Mandatory for Class II/III devices after 2026‑02. | Map SOPs to ISO 13485 clauses; prepare audit package. |
| **PCCP (if AI/ML)** | Pre‑authorizes future software changes. | Draft PCCP or confirm not applicable. |

*No specific identifier (e.g., 510(k) number, CFR section beyond the generic references) appears in the source excerpts – “no specific identifier found in source — verify separately.”*

---

### 5. Risk Controls to be Documented

1. **Design Control** – per 21 CFR 820.30; traceability matrix linking user needs → design inputs → outputs → verification/validation.
2. **Hazard Analysis** – ISO 14971‑2019 process, updated after each design change.
3. **Mitigation Strategies** – engineering controls (e.g., shielding), protective labeling, software safeguards.
4. **Post‑Market Surveillance** – FDA’s PMCF plan for Class II devices; adverse event reporting per 21 CFR 803.
5. **Change Management** – PCCP (if AI/ML) or standard change control SOPs (SOP‑CA‑001).

---

### 6. Human‑Escalation Triggers

| Trigger | Escalation Target | Timeline |
|--------|-------------------|----------|
| **Unable to assign product code / class** | Product Owner & Regulatory Lead | Immediate – pause submission planning. |
| **No suitable predicate identified** | Regulatory Strategy Manager | Within 2 business days of discovery. |
| **Critical performance data missing (e.g., safety testing)** | Engineering Project Lead | Immediate; halt any further FDA filing preparation. |
| **FDA Additional Information (AI) request with ≤30 days remaining** | RA Manager & Senior Director | Same‑day notification; daily status updates until response. |
| **QMSR non‑conformance identified during internal audit** | Quality Assurance Head | Within 1 business day; initiate CAPA. |
| **PCCP required but not prepared for AI/ML device** | Software Lead & Regulatory Lead | Immediate; develop PCCP before submission. |

---

### 7. Peer Review Prompt  
> *Please review the assumptions made above—especially the classification pathway, the completeness of the evidence checklist, and the identified gaps. Are there any jurisdiction‑specific requirements (e.g., special controls for certain device types) that have been omitted? Suggest additional items or challenge the proposed escalation thresholds.*

---

*Prepared by: Mike – US FDA Regulatory Affairs Specialist*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1058200072933812620`

> --- doc-id: T-FDA510K-A2_Form3514_템플릿 title: FDA Form 3514 (CDRH Premarket Review Submission Cover Sheet) 작성 템플릿 type: Form version: v0.1 status: draft category: 01_법규_규제 purpose: FDA 510(k) RTA Checklist A.2 대응 — Form 3514 기재항목 골격, 제품별 실 데이터 작성 예정 applicable: [FDA 510(k), FDA QMSR] owner: RA 담당자 last-review: 2026-09-10 review-due: 2027-09-10 --- # T-FDA510K-A2 FDA Form 3514 작성 템플릿 (v0.1 — 골격) > **주의**: 본 문서는 FDA 공식 양식(Form 3514)의 **대체물이 아니다**. 실제 제출은 FDA 배포 최신 양식 원본(PDF)에 기재해야 하며, 본 문서는 사내 사전 준비용 기재항목 정리 골격이다. 제품 특정 정보는 **작성 예정**.

2. Chunk `279861482758419519`

> ## 관련 문서 | 문서 | 연계 내용 | |------|-----------| | 13_규제평가_체크리스트/FDA_510k_RTA.md | FDA-510K-A2 | | 01_법규_규제/03_미국_FDA/T-FDA510K-A1_Cover_Letter_템플릿.md | Cover Letter 기재정보와 정합 | | 01_법규_규제/03_미국_FDA/T-FDA510K-A5_Form3654_Standards_템플릿.md | 표준 적합성 목록 정합 |

### kb-eval-20261016-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "398a40108786b1fa", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `398a40108786b1fa`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_01_Device_Description_IFU.md)
- Source hash: `70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_01_Device_Description_IFU.md`는 FDA eSTAR device description 및 IFU 작성에 필요한 제품 설명·표시 정보 문서입니다.
- 현재 excerpt 핵심: ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA For...
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

> **Regulatory Draft – Imaging‑Acquisition GUI Software (Radiography)**  

---

### Bottom‑Line Decision  
- **Classification:** Likely Class II imaging device under **21 CFR §892.x** (software‑based acquisition/control). *Exact subsection needs confirmation.*  
- **Submission pathway:** Traditional 510(k) (Premarket Notification) → include a Substantial‑Equivalence comparison to an FDA‑cleared predicate (e.g., a radiography acquisition controller such as K1234567).  

---

## 1. Classification & Submission Route
| Item | Detail |
|------|--------|
| **CFR Part** | 21 CFR Part 892 – Imaging devices (radiography) |
| **Probable Class** | Class II (requires special controls) |
| **Regulatory Pathway** | Traditional 510(k) (per 21 CFR §807.87) with a Summary (§807.92). |
| **QMS Requirement** | Quality Management System Regulation – Part 820 (effective Feb 2026, ISO‑13485 aligned). |

*Note: The device is software that controls image acquisition; it does not perform primary diagnosis, so it falls outside the “image interpretation” class (§892.2050) but within the acquisition/communication category (likely §892.2020 or §892.2030). Verify the exact subsection.*

---

## 2. Minimum Evidence Package for 510(k)

| Category | Required Content (per FDA guidance & CFR) |
|----------|--------------------------------------------|
| **Device Description** | Full hardware and software architecture, OS/hardware platform, compatible detectors/generators (with version). *Source [2] lists these items.* |
| **Intended Use** | Statement on “acquire, review, and manage digital radiographic images” – not for primary diagnosis. Must be submitted on FDA Form 3881. *(see source [1])* |
| **Predicate Device** | Identify cleared device (e.g., Kxxxxxx) with same intended use & technology. Provide comparison matrix. |
| **Performance Testing** | • Image‑quality metrics (MTF, NPS, DQE). <br>• Radiation dose compliance (IEC 60601‑2‑33). <br>• DICOM conformance (Storage SCU, Worklist SCU, MPPS). |
| **Software Validation** | IEC 62304 lifecycle documentation; verification and validation reports; classification (Class A/B/C) justification. *(source [2] mentions IEC 62304)* |
| **SOUP Management** | List of third‑party components, versioning, risk assessment. |
| **Cybersecurity** | Authentication, encryption, audit logging, PCCP (Predetermined Change Control Plan) if post‑market changes anticipated. |
| **Risk Management** | ISO 14971 file covering hazards from software errors, radiation exposure, user error; risk controls mapping to FDA special controls for radiography controllers. |
| **Labeling & IFU** | Draft labeling, instructions for use (IFU), and warning statements; must align with 21 CFR §801. |
| **510(k) Summary** | As required by §807.92 – concise description of device, comparison, testing, and conclusions. |
| **QMS Documentation** | Design history file (DHF), CAPA records, complaint handling per Part 820. |

---

## 3. Evidentiary Gaps Identified in Source Material
| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Predicate device not named** | Essential for substantial‑equivalence claim. | Perform market search; select a cleared acquisition controller with matching intended use. |
| **Performance test data absent** | FDA requires objective evidence of image quality and radiation safety. | Conduct bench testing per AAPM TG‑150/151 guidelines; include results in the submission. |
| **DICOM interoperability report missing** | Required to demonstrate conformity with DICOM SCU functions listed. | Execute conformance testing against IHE Radiology profiles; attach certificates. |
| **Software validation plan summary not provided** | Needed for IEC 62304 compliance demonstration. | Submit verification/validation protocols and summaries. |
| **SOUP inventory not detailed** | FDA expects full disclosure of third‑party software components. | Compile an exhaustive list with supplier attestations. |
| **Cybersecurity controls only described briefly** | Must satisfy the 2024 PCCP guidance if future modifications are planned. | Develop a formal PCCP and include in the submission. |
| **Risk Management File not referenced** | ISO 14971 is mandatory for Class II devices. | Provide full risk analysis, control measures, and residual risk evaluation. |
| **Labeling/IFU draft missing** | Required by §801; also needed for Form 3881. | Prepare labeling package and submit with the 510(k). |

*All gaps are derived from the source excerpts (see [1] & [2]) – items not mentioned are assumed absent.*

---

## 4. Core Risk Controls (to be documented)

| Hazard | Control | Reference |
|--------|---------|-----------|
| Unauthorized software access | Role‑based authentication, strong password policy, timeout lockout. | IEC 62304; FDA PCCP guidance (Dec 2024). |
| Data tampering / integrity loss | End‑to‑end TLS encryption for DICOM transmission; immutable audit logs. | FDA Cybersecurity Guidance 2023. |
| Software failure causing missed images | Watchdog timer, forced safe‑state shutdown, redundant image buffer. | IEC 60601‑1 (general safety). |
| Radiation overexposure due to controller error | Interlock with generator; dose monitoring and automatic abort if thresholds exceeded. | IEC 60601‑2‑33. |
| SOUP component vulnerability | Vulnerability scanning, periodic updates per PCCP, documented mitigation plan. | ISO 14971 risk control. |

---

## 5. Key Citations (framework references)

- **21 CFR §807.87** – Information required in a 510(k) submission. *(source [1])*  
- **21 CFR §807.92** – Format of the 510(k) Summary. *(source [1])*  
- **FDA Form 3881** – Indications for Use statement. *(source [1])*  
- **FDA Guidance “General/Specific Intended Use” (1998)** – Defines intended‑use language. *(source [1])*  
- **IEC 62304** – Software life‑cycle processes & safety class. *(source [2])*  
- **ISO 14971** – Medical device risk management. *(no specific identifier found in source — verify separately)*  
- **21 CFR Part 820** – Quality Management System Regulation (effective Feb 2026). *(no specific identifier found in source — verify separately)*  
- **Predetermined Change Control Plan (PCCP)** – FDA final guidance, Dec 2024. *(no specific identifier found in source — verify separately)*  

---

## 6. Human‑Escalation Triggers

| Situation | Action Required |
|-----------|-----------------|
| **Predicate not confirmed** | Pause submission; senior RA to approve predicate selection. |
| **Performance data incomplete or fails acceptance criteria** | Engineering validation lead must repeat testing; RA hold until satisfactory. |
| **Cybersecurity plan insufficient for PCCP** | Security specialist review; update and resubmit. |
| **Risk Management File missing any hazard analysis** | Risk manager must complete ISO 14971 file before filing. |
| **Labeling draft not aligned with intended use or warnings** | Regulatory affairs lead to revise labeling; hold submission. |
| **QMS compliance (Part 820) not demonstrated** | Quality assurance to provide audit report; no 510(k) filing until QMS certified. |

When any trigger fires, the Work Package should be set to “Yellow Gate” for human review; do **not** close automatically.

---

## 7. Peer‑Review Prompt
*Please challenge the following assumptions:*

1. The device falls under **§892.2020/2030** rather than §892.2050 – confirm the correct classification code.  
2. The listed intended‑use language avoids “diagnosis” sufficiently to stay in Class II; verify with a senior RA or FDA pre‑submission question.  
3. The adequacy of cybersecurity controls without a formal PCCP – do we need an explicit plan now, or can it be added later?  

---

## 8. Reusable RA Judgment (to be recorded)
- **Rule:** Imaging acquisition/control software that does not perform primary diagnosis is classified as Class II under 21 CFR §892.x; submit a traditional 510(k) with full device description, intended‑use statement on Form 3881, predicate comparison, performance testing, IEC 62304 compliance, ISO 14971 risk file, cybersecurity plan (PCCP), and QMS documentation per Part 820.  
- **Gap Checklist:** Predicate identified, image‑quality & dose data, DICOM conformance report, full SOUP inventory, software validation summary, labeling/IFU draft, risk management file, PCCP.  

*End of draft.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
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

### kb-eval-20261016-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "8ebd0d028931f952", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md", "source_hash": "17067eef9c351571ca7c8dedcea62a4c6b790ae298cec359778dca145c690031"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `8ebd0d028931f952`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_05_Software_Section.md)
- Source hash: `17067eef9c351571ca7c8dedcea62a4c6b790ae298cec359778dca145c690031`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_05_Software_Section.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. --- + SOUP (IEC 62304) | SOUP 목록 (IEC 62304...
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

> **Regulatory Draft – Software‑Based Medical Device (Evidence Gap Assessment)**  

---

### 1. Classification & Submission Pathway  
| Item | Decision Rationale |
|------|-------------------|
| **Device Class** | Pending determination. The software’s intended use, risk profile, and clinical context must be mapped to the FDA device classification database. If it performs image processing/analysis (e.g., PACS‑type functions) it most likely falls under **Class II – Medical Image Management & Processing System (§892.2050)**. If the function is lower‑risk (e.g., simple data conversion) a **Class I** determination may apply. |
| **Regulatory Route** | Assuming Class II, the appropriate pathway is a **510(k) Premarket Notification (21 CFR §807)** with a “substantial equivalence” argument to an FDA‑cleared predicate. If no suitable predicate exists, a **De Novo** classification request would be required. |

*Citation*: 21 CFR Part 892 for imaging devices; 21 CFR Part 807 for 510(k) (framework – no specific identifier needed).  

---

### 2. Mandatory Submission Evidence (per FDA QMSR & device‑specific guidance)

| Evidence Category | Required Artifacts | Source Basis |
|-------------------|--------------------|--------------|
| **Risk Management** | • Risk Management Plan (including acceptance criteria) <br>• Hazard analysis, risk evaluation, and risk control measures <br>• Residual risk acceptability rationale <br>• Risk Management Report <br>• Traceability matrix linking hazards → controls → verification results | ISO 14971:2019 (framework). The source excerpt specifies the same components. |
| **Software Development Process** | • Software Development Plan (SDP) <br>• Architecture & design documentation (linked to risk analysis) <br>• Verification & Validation Protocols/Reports (including unit, integration, system testing) <br>• IEC 62304 compliance evidence – especially §7 linking software items to architecture | IEC 62304 §7 (framework). |
| **SOUP Management** | • List of all third‑party / open‑source components (SOUP) <br>• Rationale for inclusion, known vulnerabilities, mitigation actions | “SOUP (IEC 62304)” mentioned in source. No identifier supplied – verify separately. |
| **Software Bill of Materials (SBOM)** | • Complete SBOM per FDA’s software supply chain guidance (Guidance “Supply Chain Security” – 2024) | Source notes SBOM obligation under “FDA 524B”. No specific identifier found – verify separately. |
| **AI/ML Change Control** (if applicable) | • Predetermined Change Control Plan (PCCP) detailing pre‑specified modifications, monitoring, and post‑market performance plan | PCCP (final guidance Dec 2024) cited in source; no document number provided – verify separately. |
| **Labeling & UDI** | • Label and IFU complying with 21 CFR §801 <br>• Unique Device Identifier (UDI) assigned per 21 CFR §830 (label must bear a UDI) | Part 801, Part 830 (framework). |
| **Clinical/Performance Evidence** | • Bench‑testing data confirming functional performance <br>• If the software claims clinical decision support, appropriate clinical validation data (prospective or retrospective studies) | Standard 510(k) requirements; no identifier in source – verify separately. |
| **Quality Management System (QMS)** | • QMS documentation aligned with the new FDA Quality Management System Regulation (effective Feb 2026) – ISO 13485‑aligned <br>• SOPs covering design control, risk management, post‑market surveillance, complaint handling | 21 CFR Part 820 (framework). |

---

### 3. Gaps Identified from Source Excerpts  

| Missing Information | Why It Is Needed | Potential Impact if Unaddressed |
|---------------------|------------------|---------------------------------|
| **Intended Use Statement** | Determines classification, predicate search, labeling claims, and risk scope. | Prevents accurate class determination; may force De Novo instead of 510(k). |
| **Predicate Device(s)** | Required for a 510(k) substantial‑equivalence claim. | No predicate → inability to submit 510(k); must pursue De Novo or PMA. |
| **Clinical Performance Data** (if applicable) | Needed when software provides diagnostic/clinical decision support. | FDA may issue an Additional Information (AI) request, delaying clearance. |
| **Complete SBOM** | FDA’s supply‑chain security expectations; essential for cybersecurity risk management. | May trigger a “major deficiency” in the 510(k) review. |
| **SOUP Vulnerability Mitigation Evidence** | Demonstrates that known open‑source issues are addressed per IEC 62304. | Could result in a refusal to accept (RTA) decision on software hygiene. |
| **Predetermined Change Control Plan (PCCP)** (for AI/ML) | Required to pre‑authorise future algorithm updates. | Lack of PCCP can force the device into a higher regulatory burden (e.g., PMA) or delay clearance. |
| **Verification Traceability Matrix** linking risk controls to test results (explicit in source but not yet produced). | Shows that every mitigated hazard has been verified. | May be cited as insufficient design control evidence. |
| **UDI Assignment Strategy & GUDID Submission** | FDA’s UDI rule mandates registration in the Global Unique Device Identification Database (GUDID). | Non‑compliance can halt market entry even after clearance. |

---

### 4. Recommended Risk Controls (aligned to ISO 14971 & IEC 62304)

1. **Hazard Identification** – Use a software hazard analysis (e.g., FMEA) covering functional, security, and usability hazards.  
2. **Risk Control Measures** – Implement design controls (input validation, fail‑safe modes), cybersecurity safeguards (patch management per SBOM), and AI/ML monitoring per PCCP.  
3. **Verification & Validation** – Map each risk control to a verification activity; document results in the traceability matrix (as highlighted in source).  
4. **Residual Risk Evaluation** – Conduct a formal acceptability assessment; record justification for any residual risks that remain.  
5. **Post‑Market Surveillance Plan** – Include mechanisms for adverse event reporting (21 CFR §803) and software updates per PCCP.

*Citation*: ISO 14971:2019, IEC 62304 §7 (framework).  

---

### 5. Human‑Escalation Triggers  

| Condition | Action Required | Escalation To |
|-----------|-----------------|---------------|
| **Unable to identify a suitable predicate** after exhaustive search | Initiate De Novo strategy or consider PMA pathway | Senior Regulatory Lead & Project Manager |
| **Missing SBOM or incomplete SOUP list** when reviewer flags as “major deficiency” | Compile full SBOM, perform vulnerability assessment, update risk file | QMS Manager / Cybersecurity Specialist |
| **FDA Issues an Additional Information (AI) request exceeding 180 days without a response plan** | Prepare and submit a complete response; consider requesting extension if justified | Regulatory Affairs Director |
| **PCCP not drafted for AI/ML software** before 510(k) submission deadline | Draft PCCP, align with FDA guidance; obtain internal sign‑off | Head of Software Engineering & RA Lead |
| **Residual risk deemed unacceptable by QA** | Perform additional mitigations or redesign; update RMF and V&V evidence | Design Engineer Lead |
| **UDI/GUDID registration incomplete after clearance** | Finalize UDI label, submit to GUDID, verify entry | Labeling/Manufacturing Ops |

When any trigger occurs, the responsible functional owner must log a corrective action in the QMS (21 CFR §820.100) and notify the Regulatory Affairs team immediately.

---

### 6. Peer‑Review Prompt  

> *“Colleague, please evaluate whether our assumptions about device classification (potentially Class II under §892.2050) are justified given the limited functional description we have. Also, confirm that we have captured all evidence gaps implied by the source excerpts—especially any items that might require separate FDA guidance numbers or external standards not listed here.”*  

--- 

**End of Draft**

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1023300943338888510`

> ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. ---

2. Chunk `1150973762104113645`

> + SOUP (IEC 62304) | SOUP 목록 (IEC 62304 준수) | SOUP 목록 (IEC 62304) + SBOM (SBOM 의무는 FDA 524B; MDR은 명시 SBOM 요건 없음 — MDCG 2019-16 사이버보안 준용) | | AI/ML 소프트웨어 | PCCP (Predetermined Change Control Plan, 2024 Final) | AI 의료기기 가이드라인 (MFDS 2025) | MDCG 2021-6 AI 가이던스 |

## ra_eu

### kb-eval-20261016-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "d2798f6531cc2363", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "2f93a4746d3d174e7f695947b694c3f0046f06724636f8946eeb24843322c943"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d2798f6531cc2363`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDCG_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/Clinical_Evaluation_MDR_%EB%8F%99%EB%93%B1%EC%84%B1_%EC%B6%A9%EB%B6%84%EC%84%B1_%EA%B8%B0%EC%A4%80.md)
- Source hash: `2f93a4746d3d174e7f695947b694c3f0046f06724636f8946eeb24843322c943`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR, MDCG

**Source Summary**

- 문서 요약: `Clinical_Evaluation_MDR_동등성_충분성_기준.md`는 EU MDR clinical evaluation, CER/CER plan, equivalence 또는 clinical data sufficiency 관련 문서입니다.
- 현재 excerpt 핵심: ### 7.2 Handheld X-ray Source | 규제 항목 | 세부 내용 | |-----------|-----------| | **MDR 분류** | Class IIb (Rule 9 — 방사선 발생 기기) | | **임상조사 의무** | 없음 (Class IIb) — 그러나 충분성 입증 요건 강화 | | **동등성 핵심 포인트** | ① 기술: 관전압(kV)·관전류(mA)·선량 특성·초점 크기·SID(선원-피부거리) 유사성 ② 생물: 비접촉 기기 — 생물학적 특성 N/A ③ 임상: 동일 촬영 부위 목적·동일 사용자 유형(방사선사/의사) | | **FDA** | 510(k) — 기존 handheld portable X-ray...
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

> **Regulatory Draft – Hand‑held X‑ray Source (MDR 2017/745)**  

---

### 1. Device Synopsis  
- **Intended purpose:** Generation of ionising X‑ray beams for diagnostic radiography using a portable, hand‑held form factor. Operated by qualified radiation professionals (radiologists / radiographers).  
- **Key design attributes (from source):** Tube voltage (kV), tube current (mA), dose‑rate characteristics, focal spot size, source‑to‑image‑distance (SID). No patient‑contact component; biological safety not applicable.  

---

### 2. MDR Classification & Conformity Assessment Route  
| Item | Requirement / Reference |
|------|--------------------------|
| **Classification rule** | **Rule 9** – “Active devices that emit ionising radiation” → **Class IIb** (source excerpt: *“MDR 분류 → Class IIb (Rule 9 — 방사선 발생 기기)”*). |
| **Applicable article** | Art. 52(4) MDR 2017/745 – Class IIb devices must undergo a conformity‑assessment procedure involving an NB. |
| **Conformity‑assessment route** | **Annex IX** (full technical‑documentation assessment by the Notified Body) *or* **Annex X + Annex XI** (type‑examination plus production conformity verification). Cite: Art. 52(4) & Annex IX/ X / XI. |
| **NB involvement** | Required – NB will review the Technical Documentation (Annex II), the PMCF plan (Annex XIV Part B) and issue the EU Declaration of Conformity (Annex IV). |

---

### 3. Clinical Evaluation Requirements  

#### 3.1 General MDR Obligation  
- **Clinical Evaluation Report (CER)** – mandatory under **Annex XIV Part A**; must be kept up‑to‑date (Art. 61).  

#### 3.2 Equivalence Argument (source guidance)  
| Equivalence domain | Source‑derived key points |
|--------------------|---------------------------|
| **Technical** | Same tube voltage, current, dose characteristics, focal spot size and SID (as listed in the “동등성 핵심 포인트”). |
| **Biological** | Device is non‑contact → no biological safety data required (source: *“비접촉 기기 — 생물학적 특성 N/A”*). |
| **Clinical** | Same anatomical region, same user type (radiation professionals) and same imaging purpose (source: “동일 촬영 부위 목적·동일 사용자 유형”). |

#### 3.3 Clinical Investigation Requirement  
- **No mandatory clinical investigation** for Class IIb per source (*“임상조사 의무 – 없음 (Class IIb)”*), but **enhanced sufficiency of equivalence evidence** is required – i.e., robust dose‑comparability data, scatter‑radiation safety assessment and clinical literature review.  

#### 3.4 Post‑Market Clinical Follow‑up (PMCF)  
- Required because the hand‑held form factor introduces new usage patterns (source: “PMCF – 필요”). Must be documented in a **PMCF plan** (Annex XIV Part B).  

---

### 4. Evidence Package – What Must Be Submitted  

| Evidence | MDR / Standard Reference | Comment |
|----------|--------------------------|---------|
| **Technical Documentation (Annex II)** covering design, manufacturing, labeling, risk management (ISO 14971) | Annex II; ISO 14971 | Includes drawings, bill of materials, specifications of kV, mA, focal spot, SID. |
| **Risk Management File** | Annex I §17‑§20; ISO 14971 | Must address radiation protection (§16), active device hazards (§18). |
| **Electrical Safety & Performance Testing** | IEC 60601‑1‑3 (radiation safety) ; IEC 60601‑2‑28 (X‑ray tube assemblies) | Demonstrate compliance with dose output, beam quality and scatter limits. |
| **Usability / Human Factors Evaluation** | IEC 62366‑1 (usability engineering) | Special focus on hand‑held ergonomics and operator positioning. |
| **Clinical Evidence – Equivalence Dossier** | Annex XIV Part A; MEDDEV 2.7/1 rev.4 | • Comparative bench data (dose‑rate, dose distribution, scatter).<br>• Literature review of clinical performance for comparable handheld X‑ray devices.<br>• Statement on identical intended use and user group (source excerpt 2). |
| **PMCF Plan & Interim Reports** | Annex XIV Part B; Art. 84/86 | Define data‑collection methods for new usage patterns (e.g., field exposure logs, incident reporting). |
| **Labeling & IFU** | Annex I §23 | Include radiation safety warnings, operator training requirements and contraindications. |

---

### 5. Gaps / Missing Information (Gap Analysis)  

| Gap | Why it matters | Suggested data collection |
|-----|----------------|---------------------------|
| **Quantitative dose‑comparability** between the handheld device and the predicate handheld X‑ray system (e.g., % deviation in air‑kerma, DAP). | MDR demands evidence that radiation output is at least as safe/effective as the reference; otherwise NB will request a clinical investigation. | Conduct calibrated beam‑output measurements on phantoms; document statistical analysis. |
| **Scatter‑radiation distribution** for hand‑held operation (operator exposure). | §16 of Annex I requires protection against ionising radiation for both patient and staff. | Perform occupational dose mapping using dosimeters at typical operator positions. |
| **Usability data for new form factor** (hand tremor, positioning reproducibility). | IEC 62366‑1 obliges demonstration of safe use; hand‑held devices may introduce new use errors. | Run a formative usability study with representative HCPs; capture task success rates and error modes. |
| **Clinical literature covering the same anatomical region with handheld X‑ray** (especially recent publications). | Required for CER Section “Clinical Literature” (Annex XIV Part A). | Systematic literature search (last 10 years); evaluate relevance to intended use. |
| **PMCF data collection schedule and KPI definitions** (e.g., number of procedures, adverse events). | Annex XIV Part B mandates a defined PMCF plan; lack of detail will be flagged by NB. | Draft a PMCF protocol with milestones (e.g., 12‑month interim report) and define acceptance criteria for dose variability and incident rates. |
| **Labeling for lay‑person use** – confirmation that device is *not* intended for lay users, as MDR adds user‑type equivalence requirement (source 2). | If labeling allows unintended user groups, the equivalence claim fails. | Explicitly state “intended for use by qualified radiation professionals only” in IFU and label. |

---

### 6. Risk Controls & GSPR Alignment  

| GSPR § | Control(s) to be demonstrated |
|--------|--------------------------------|
| **§16 – Radiation protection** | IEC 60601‑1‑3 compliance; scatter dose mapping; shielding recommendations. |
| **§17 – Software / programmable systems** (if device includes embedded control software) | IEC 62304 lifecycle documentation; verification & validation of software functions that influence beam parameters. |
| **§18 – Active devices** | Risk analysis for unintended emission, fail‑safe modes, interlocks. |
| **§20 – Mechanical/thermal risks** | Ergonomic design to prevent hand fatigue or overheating; mechanical robustness testing. |
| **§22 – Use by lay persons** | Statement of intended user group (qualified HCP); training program description. |
| **§23 – Label & IFU** | Full labeling compliance, symbols for radiation safety, contraindications, maintenance schedule. |

All risk controls must be documented in the **Risk Management File** and cross‑referenced in the Technical Documentation.

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required (human) |
|---------|--------------------------|
| **Dose‑output deviation > 10 %** from predicate device or exceeds national dose limits. | Halt NB submission; initiate a supplemental clinical investigation or redesign to meet acceptable output. |
| **Scatter‑radiation measurements indicate operator dose > ALARA threshold** (e.g., > 20 µSv per procedure). | Immediate risk assessment, update protective measures, and inform the Notified Body of corrective actions. |
> *Escalate to senior regulatory manager for NB communication.* |
| **Usability study shows task failure ≥ 5 %** in critical positioning steps. | Conduct redesign or additional training; resubmit updated usability engineering documentation. |
| **PMCF interim report (12‑month) fails to meet KPI** (e.g., > 2 % adverse events). | Initiate corrective action plan, consider a post‑market clinical investigation, and notify the NB per Art. 86(3). |
> *Escalate to Clinical Affairs Lead for rapid response.* |
| **NB raises “user‑type equivalence” objection** (per source 2). | Provide additional justification that only qualified HCPs will operate the device; if insufficient, modify labeling or restrict intended use. |

---

### 8. Summary Judgment  

- The hand‑held X‑ray source is a **Class IIb** device under **Rule 9**.  
- Conformity assessment must follow **Art. 52(4) – Annex IX (full technical‑documentation review)** or the alternative **Annex X + XI** route, involving a Notified Body.  
- Clinical evidence rests on **equivalence** to an existing handheld X‑ray system; however, **dose‑output, scatter radiation, and usability data** are currently missing and must be generated to satisfy MDR sufficiency criteria (Annex XIV Part A).  
- A **PMCF plan** is mandatory because of the new hand‑held form factor (Annex XIV Part B).  

The identified gaps should be addressed before dossier assembly. Any failure to meet the above triggers must be escalated promptly to senior regulatory and clinical leadership.

---

### 9. Peer Review Prompt  

*Colleague, please review the following:*  

1. **Assumptions on equivalence** – Are the technical parameters listed sufficient to claim “same performance” under MDR, or should additional beam‑quality metrics be added?  
2. **Scope of required clinical literature** – Does the current plan capture all relevant publications for the intended anatomical region and user group?  
3. **PMCF design** – Is the proposed 12‑month interim reporting interval appropriate for a Class IIb hand‑held X‑ray device, or should a more frequent schedule be justified?  
4. **Risk control completeness** – Are any GSPR sections (e.g., §§ 24‑25 on environmental impact) overlooked for this device type?  

Please challenge the above and flag any jurisdiction‑specific considerations (e.g., national radiation protection directives) that have not been covered.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [x] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 케이스 결함 기입 — 원문 7.2표 'Rule 9 — 방사선 발생 기기'는 KB 원본 오류(진단용 이온화 방사선 기기는 Rule 10, Rule 9는 치료용 — 웹 교차검증 2026-10-16, zechmeister-solutions·EUR-Lex). 응답은 원문 충실 인용이고 Class IIb 결론 자체는 정확 → #144 경로 원본 정정 대상(ra-project 소스).

**Source Excerpts**

1. Chunk `1033154794446940076`

> ### 7.2 Handheld X-ray Source | 규제 항목 | 세부 내용 | |-----------|-----------| | **MDR 분류** | Class IIb (Rule 9 — 방사선 발생 기기) | | **임상조사 의무** | 없음 (Class IIb) — 그러나 충분성 입증 요건 강화 | | **동등성 핵심 포인트** | ① 기술: 관전압(kV)·관전류(mA)·선량 특성·초점 크기·SID(선원-피부거리) 유사성 ② 생물: 비접촉 기기 — 생물학적 특성 N/A ③ 임상: 동일 촬영 부위 목적·동일 사용자 유형(방사선사/의사) | | **FDA** | 510(k) — 기존 handheld portable X-ray 대비 SE, 방사선 선량 차이 시 임상데이터 필요 가능성 있음 | | **MFDS** | 3등급 방사선 발생기 — 동등 기기 임상 자료 제출 필요. 신규 형태(handheld)는 임상시험 자료 요구 가능 [firm 임상전략] | | **CER 핵심 섹션** | 방사선 선량 평가 (IEC 60601-1-3), 사용 환경 안전성 (산란방사선), 임상 문헌 | | **PMCF** | 필요 — handheld 폼팩터 특성상 신규 사용 패턴 모니터링 필요 |

2. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

### kb-eval-20261016-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "eee0c04e85e83749", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `eee0c04e85e83749`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & MDR Submission Planning**

---

### 1. Device Scope (what is *known* from the source)

| Item | Information extracted from source | Gap / comment |
|------|-----------------------------------|---------------|
| **Intended medical purpose** | Not provided – only generic headings “임상적 적용 부위”, “임상적 대상 집단”, “임상적 사용자 유형” (clinical indication, target group, user type) appear in the excerpt. | *Missing* – essential for classification (Annex VIII) and for drafting the CER (Annex XIV Part A). |
| **Core performance claims** | Mentioned as “임상적 핵심 성능” but no specific claim listed. | *Missing* – needed to define endpoints for clinical evaluation and PMCF. |
| **Scientific/clinical significance** | The source notes “과학적 근거 + 임상적 유의성 없음 결론” (no scientific basis or clinical relevance). | Indicates a current lack of evidential justification; must be addressed before any conformity assessment. |

> **Regulatory implication:** Until the intended purpose, user profile and performance claims are defined, a definitive MDR class cannot be assigned (Art 52 & Annex VIII). This also precludes finalising the Clinical Evaluation Report (CER) required by Annex XIV Part A (kept current under Art 61).

---

### 2. Preliminary Classification & Conformity‑Assessment Route

| Step | Required input | Current status | Action |
|------|----------------|---------------|--------|
| **Identify applicable rule(s)** (Annex VIII) | Device’s intended purpose, mode of action, invasiveness, duration of contact, whether active, measuring or sterile. | Not available. | Obtain a complete Intended Use Statement from the manufacturer. |
| **Determine class** | Apply the most restrictive rule that matches the device. | Undetermined. | *Human escalation*: Request clarification before any downstream activities. |
| **Select route (Art 52)** | Based on class: <br>‑ Class I → self‑declaration (Art 52(7)). <br>‑ Class IIa/IIb/III → NB‑involved assessment (Annex IX, X or XI). | Unknown. | Classification decision will drive the required NB involvement. |

*Citation*: Art 52 MDR 2017/745 – classification determines the conformity‑assessment route; Annex VIII contains the rule set.

---

### 3. Required Evidence Package under MDR

| Evidence type | Regulatory reference | Contents (minimum) |
|---------------|----------------------|--------------------|
| **Technical Documentation** | Annex II (and Annex III for PMS) | Device description, design & manufacturing information, labeling, GSPR compliance (Annex I), risk‑management file (ISO 14971). |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art 61 | • Clinical background<br>• State of the art literature review<br>• Clinical data – pre‑market & post‑market<br>• Benefit‑risk analysis (link to RMF)<br>• Conclusions. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** | Annex XIV Part B | • Objectives, methodology, timeline, responsible parties, data sources, statistical analysis plan. |
| **PMCF Evaluation Report** | Annex XIV Part B – Section 5.2 (source excerpt) | Required sections A–G as listed in the source: <br>‑ **A** Manufacturer contact<br>‑ **B** Device description (updated if changed)<br>‑ **C** Results of PMCF activities (incl. deviations & justification)<br>‑ **D** Assessment of clinical data from equivalent/similar devices<br>‑ **E** Impact on technical documentation (CER, RMF, SSCP)<br>‑ **F** Applied Common Specifications, harmonised standards and guidance<br>‑ **G** Overall conclusion (alignment with PMCF objectives & need for corrective actions). |
| **Post‑Market Surveillance (PMS) System** | Art 83 & Art 84 | PMS plan, periodic safety update report (PSUR – Art 86 for class IIa/IIb/III or PMS report – Art 85 for class I). |
| **Usability Evaluation (if applicable)** | Annex I §22; IEC 62366‑1 | Human factors testing results supporting safe use by the defined user group. |

---

### 4. Identified Gaps & Immediate Actions

| Gap | Why it matters | Evidence needed | Owner / Deadline |
|-----|----------------|-----------------|-------------------|
| **Intended purpose, target population & user type** (excerpt 1) | Drives classification, determines clinical endpoints, and is required in the CER. | Clear Intended Use Statement; description of patient demographics and operator qualifications. | Manufacturer – within 2 weeks. |
| **Core performance claims** (excerpt 1) | Needed to select appropriate clinical endpoints & comparators for CER/PMCF. | List of functional / performance specifications, including success criteria. | R&D lead – within 2 weeks. |
| **Scientific/clinical significance justification** (excerpt 1) | Current conclusion “no scientific basis” blocks benefit‑risk argument; must be substantiated before NB review. | Literature review covering state of the art; pre‑market clinical data or robust equivalence rationale. | Clinical affairs – within 4 weeks. |
| **PMCF plan (not provided)** | Mandatory for Class IIa and higher devices; informs continuous safety assessment. | Full PMCF plan outlining objectives, methodology, patient enrolment numbers, timelines. | Clinical & PMCF lead – draft in 3 weeks. |
| **Risk‑management file linkage** | Annex XIV Part B requires that PMCF results feed back to RMF (section E). | Updated risk analysis showing new hazards identified or mitigated through PMCF. | Risk‑manager – after first PMCF data collection. |
| **Applicable harmonised standards / Common Specifications** (section F of PMCF report) | Needed to demonstrate compliance with GSPR (§17‑§19 for active/software devices). | List of IEC/ISO standards applied (e.g., IEC 60601‑2‑54, IEC 62304, ISO 14971). | QA – concurrent with technical file. |

> **Human‑escalation trigger #1:** *If the intended purpose cannot be defined within 2 weeks, classification and subsequent conformity‑assessment steps must be halted and escalated to senior regulatory management for decision on project continuation.*

> **Human‑escalation trigger #2:** *Any negative trend or serious safety signal emerging from PMCF (section C) that contradicts the declared benefit‑risk profile requires immediate reporting under Art 87 (Vigilance) and possible field‑safety corrective action (FSCA).*

---

### 5. Risk Controls & Mapping to GSPR

| Hazard area | Likely GSPR clause(s) (Annex I) | Suggested control (link to RMF) |
|-------------|---------------------------------|---------------------------------|
| **Radiation exposure** (if device emits ionising radiation) | §16 – Protection against radiation (incl. §16.4 for ionising). | Design shielding, dose‑monitoring software, user training; risk controls documented in RMF. |
| **Active software decision support** | §17 – Electronic programmable systems & software; §18 – Active devices. | IEC 62304 compliant development lifecycle, verification/validation against clinical outcomes; post‑market monitoring of algorithm performance (PMCF). |
| **User error (lay‑person use)** | §22 – Devices intended for lay users. | Usability testing per IEC 62366‑1; clear labeling (§23) and instructions for use. |
| **Implantable components** (if any) | §19 – Active implantable devices. | Sterility assurance, biocompatibility data, long‑term follow‑up in PMCF. |

All risk controls must be reflected in the **Risk Management File** (ISO 14971) and linked to the **CER/PMCF** outcomes (Annex XIV Part B section E).

---

### 6. Summary & Regulatory Judgment

*At present the device cannot be assigned an MDR class nor a conformity‑assessment route because critical information on intended use, target population, user type and core performance is missing.*  
The **minimum evidence** required to progress includes:

1. Complete Intended Use Statement (incl. indication, patient/operator groups).  
2. Defined performance claims with measurable endpoints.  
3. A scientific/clinical justification (state‑of‑the‑art literature and/or pre‑market clinical data).  
4. Draft PMCF plan aligned with the above claims.  

Until these are supplied, any submission to a Notified Body would be incomplete and likely rejected on formal grounds (Annex II documentation gaps, Annex XIV CER incompleteness).

---

### 7. Human‑Escalation Triggers

| Condition | Action required |
|-----------|-----------------|
| **Missing intended purpose / performance claims after the 2‑week deadline** | Escalate to Regulatory Project Lead for go/no‑go decision; pause all downstream activities. |
| **Negative or inconclusive PMCF results (section C)** | Initiate Art 87 vigilance reporting; convene corrective‑action task force; update RMF and CER accordingly. |
| **Identification of a new hazard not covered by existing risk controls** | Immediate risk‑assessment update; potential temporary suspension of device deployment pending mitigation. |

---

### 8. Peer‑Review Prompt

> *Colleague, please review the assumptions made in this draft:*
> 
> • *Are the identified gaps (intended use, performance claims, scientific justification) sufficient to block classification under MDR?*  
> • *Does the mapping of required evidence to the cited regulatory provisions reflect current MDCG guidance (especially the PMCF report structure)?*  
> • *Are there any jurisdiction‑specific nuances (e.g., national post‑market requirements) that we have omitted for this device class?*  

Your feedback will be used to refine the risk‑benefit narrative and ensure completeness before the next regulatory submission milestone.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1032759063790726230`

> │ │ [임상적] 적용 부위 │ (same 필수) │ │ │ │ [임상적] 대상 집단 │ │ │ │ │ [임상적] 사용자 유형│ (same 필수) │ │ │ │ [임상적] 핵심 성능 │ │ │ │ └────────────────────┴──────────────┴──────────────┴─────────────────┘ 각 차이항목: 과학적 근거 + 임상적 유의성 없음 결론 ```

2. Chunk `1132312459160211217`

> ### 5.2 PMCF Evaluation Report 필수 섹션 | 섹션 | 내용 | |------|------| | A | 제조사 연락처 | | B | 기기 설명 (변경 시 갱신, 미변경 시 Plan 참조) | | C | 수행된 PMCF 활동 결과 (데이터 수집 결과, 긍정·부정 포함, 편차 근거) | | D | 동등·유사 기기 임상데이터 평가 결과 | | E | 기술문서에 대한 결과의 영향 (CER, Risk Management File, SSCP 각각 명시) | | F | 적용된 CS, 조화표준, 가이던스 | | G | 종합 결론 (PMCF 목적 대비 결과, 예방·시정 조치 필요성) |

### kb-eval-20261016-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "ff134bbd2c9b3bcd", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `ff134bbd2c9b3bcd`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통...
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

> **Regulatory Draft – Clinical‑Evidence Gap Analysis & Submission Planning  
(Diagnostic Radiology X‑ray System)**  

---

### 1 Device Overview (as derived from the source)

| Item | Description |
|------|--------------|
| **Intended purpose** | “Standard diagnostic radiology” – generation of X‑ray images for clinical diagnosis. |
| **Key performance claim** | Detective Quantum Efficiency (DQE) ≥ 65 % (reference: Test Report TR‑2024‑015, IEC 62220‑1‑1). |
| **Evidence supplied** | Revised Clinical Evaluation Report (CER Rev. 3) attached as Annex A (source [1]). |

---

### 2 Regulatory Classification & Conformity‑Assessment Route  

| Regulatory element | Determination | Citation |
|--------------------|---------------|----------|
| **MDR Rule** | The device *actively emits ionising radiation* for diagnostic purposes. → **Rule 10 (Annex VIII)**. | Annex VIII, Rule 10 (active devices emitting ionising radiation for diagnostic radiology). |
| **Resulting class** | **Class IIb** (Rule 10 leads to IIb; any software that influences the diagnostic decision would be ≤ IIa but the system is classified by its highest‑risk component). | — |
| **Conformity‑assessment route** | **Art 52(4)** – full technical‑documentation assessment under **Annex IX** (or alternative Annex X + XI) with NB involvement. | Art 52(4), Annex IX (full technical‑doc assessment). |

---

### 3 Required Technical & Clinical Evidences (MDR Checklist)

| Requirement (MDR clause) | What must be provided | Current status / Gap |
|---------------------------|-----------------------|----------------------|
| **Technical Documentation** – design, manufacturing, labeling, GSPR compliance. | Annex II (plus Annex III for PMS). | No evidence of complete Annex II package; risk‑management file, IEC 60601‑2‑54 conformity and labeling (§23) missing. |
| **Clinical Evaluation Report (CER)** – state‑of‑the‑art literature, clinical data, equivalence justification. | Annex XIV Part A; kept current per Art 61. | CER Rev. 3 attached (source [1]) but lacks: <br>• Systematic literature search methodology<br>• Clinical performance data beyond DQE (e.g., image quality studies, patient outcomes). |
| **Demonstration of Clinical Equivalence** | Comparative bench testing (DQE) and literature; justification that device performs at least as well as predicate. | DQE ≥ 65 % shown (TR‑2024‑015); however: <br>• No traceability to a specific predicate device identifier.<br>• No statistical analysis of equivalence margin. |
| **Risk Management File** – ISO 14971 compliant, covering radiation hazards (§16) and software safety (§17). | Annex I §16‑§18; IEC 62304 for software; IEC 60601‑2‑54 for radiation protection. | Not supplied in the excerpt – gap identified. |
| **Usability / Human Factors** | IEC 62366‑1 validation report (especially for lay‑person use if applicable). | No evidence provided. |
| **Post‑Market Surveillance (PMS) System & Plan** | Art 83 (system), Art 84 (plan). | No PMS plan or system description submitted – gap. |
| **Periodic Safety Update Report (PSUR)** (Class IIb) | Art 86 (annual update). | Not yet prepared; schedule needed. |
| **Labeling & IFU** | Annex I §23 requirements (warnings, radiation safety info). | No labeling package attached – gap. |
| **Software Validation** (if applicable) | IEC 62304 lifecycle documentation; IEC 82304‑2 if software is a medical device on its own. | Missing. |
| **Declaration of Conformity** | Annex IV signed by manufacturer. | Not mentioned. |

---

### 4 Risk Controls Needed (to close identified gaps)

| Hazard | Control (per GSPR) | Supporting Standard / Clause |
|--------|--------------------|------------------------------|
| **Ionising radiation exposure** | – Radiation shielding design, interlocks, dose‑output monitoring.<br>– Compliance with IEC 60601‑2‑54 (radiography/radioscopy).<br>– Information on dose limits in IFU (§16.4). | Annex I §16; IEC 60601‑2‑54. |
| **Electrical safety / electromagnetic compatibility** | – IEC 60601‑1 series compliance.<br>– Conducted and radiated emission testing. | Annex I §§10‑12. |
| **Software malfunction influencing diagnostic decision** | – IEC 62304 development lifecycle, verification/validation plan.<br>– IEC 62366‑1 usability validation (risk control for user errors). | Annex I §17; IEC 62304; IEC 62366‑1. |
| **Usability errors (lay‑person operation)** | – Human factors testing, labeling with clear warnings (§22). | Annex I §22. |
| **Mechanical/thermal hazards** | – Mechanical integrity tests, temperature monitoring. | Annex I §20. |

---

### 5 Evidence Deficiencies Highlighted by the NB (derived from source)

*The source excerpt defining a “Deficiency Letter” (source [2]) reminds us that the NB will formally request any missing or unclear documentation.*  

| Expected NB Request | What must be prepared before reply |
|----------------------|------------------------------------|
| **Clarification of Clinical Equivalence** – proof that DQE meets the ≥ 65 % claim and is comparable to predicate. | Provide full test report (TR‑2024‑015) with measurement methodology, calibration traceability, statistical analysis; reference IEC 62220‑1‑1. |
| **Missing Risk Management File** | Submit ISO 14971‑conformant risk management dossier covering radiation hazards (§16). |
| **Absent PMS Plan** | Draft Art 84 PMS plan (including PMCF activities) and submit for NB review. |
| **Incomplete Technical Documentation** | Compile Annex II technical file (design dossier, IEC 60601‑2‑54 conformity, labeling, declaration of conformity). |

---

### 6 Human‑Escalation Triggers (When to Involve Senior RA / Management)

| Trigger | Reason | Action Required |
|--------|--------|-----------------|
| **NB issues a Deficiency Letter requesting additional clinical data** | The NB will not clear the device until all gaps are closed. | Senior RA to review and approve supplemental clinical evidence; possibly engage external testing lab for DQE repeat. |
| **Risk Management File lacks radiation‑hazard analysis** | Non‑compliance with Annex I §16 could lead to rejection or market‑withdrawal. | Immediate escalation to the Risk‑Management Lead and Product Owner for completion. |
| **Disagreement on classification (Rule 10 vs. Rule 11 for software)** | Ambiguity may affect conformity‑assessment route and timeline. | Convene a cross‑functional classification board; involve legal counsel if needed. |
| **PMS Plan not ready before NB submission deadline** | PMS is mandatory for Class IIb; missing plan blocks acceptance of technical documentation. | Flag to Project Manager; re‑schedule submission or request extension from NB. |
| **Labeling package fails Annex I §23 review** | Label/IFU deficiencies cause non‑conformity. | Trigger a design‑change control and senior QA sign‑off before resubmission. |

---

### 7 Next Steps (Action Items)

1. **Compile complete Technical Documentation (Annex II)** – include risk file, IEC 60601‑2‑54 test reports, labeling, Declaration of Conformity.  
2. **Expand CER** – add systematic literature review, clinical performance data beyond DQE, and a clear predicate device reference.  
3. **Finalize PMS System & Plan (Art 83/84)** – schedule PMCF activities; draft PSUR schedule per Art 86.  
4. **Perform software validation** (IEC 62304/IEC 62366‑1) if the system contains dedicated diagnostic software.  
5. **Prepare response to anticipated NB Deficiency Letter**, attaching all missing documents with clear cross‑references.  

---

### 8 Peer Review Request

*Please review this draft and challenge any of the following:*  

- The assumption that the whole system falls under **Rule 10 → Class IIb** (are there separate modules that could lower overall classification?).  
- Completeness of the listed evidence gaps against the NB’s typical deficiency patterns.  
- Any jurisdiction‑specific requirements (e.g., Korean MFDS “보완 요청” equivalents) that might affect EU submission timing or content.  

Your feedback will be incorporated before the final NB response package is assembled.

--- 

*End of draft.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1107467848736309543`

> ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통지하는 문서. 국내 MFDS "보완 요청", FDA "Additional Information (AI) Request"에 해당하는 EU MDR 용어. ---

### kb-eval-20261016-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "55f7496daba8ea52", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `55f7496daba8ea52`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_MDR_2017_745.md)
- Source hash: `15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_MDR_2017_745.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | |...
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

> **Regulatory Draft – X‑ray Diagnostic Imaging System (Active Device that Emits Ionising Radiation)**  

---

### 1. Device Classification & Conformity‑Assessment Route  
| Item | Regulatory basis | Determination |
|------|-------------------|---------------|
| **Device class** | Rule 10 (active device emitting ionising radiation for diagnostic radiology) → Class IIb | **Class IIb** |
| **Conformity‑assessment route** | Art. 52(4) MDR 2017/745 – “Annex IX Chapters I & III + Annex IX §4 technical‑documentation assessment of one representative device per generic group (or every device individually if implantable), or Annex X + Annex XI” | **Full technical‑documentation assessment under Annex IX** (NB involvement required) |

*Citation*: Rule 10, Art. 52(4) – MDR 2017/745.

---

### 2. Mandatory Evidence & Documentation Packages  

| Deliverable | Content Required (MDR clauses) | Typical source documents |
|-------------|--------------------------------|--------------------------|
| **Technical documentation (TD)** | Annex II – complete device description, design‑manufacturing information, labeling, UDI, etc. | F‑MDR‑TD‑CHK‑001 checklist; design files; manufacturing records |
| **GSPR mapping report** | Annex I GSRPs mapped to TD sections (completed via GSPR checklist) | “GSPR 적합성 보고서” (step 3 in the process flow) |
| **Risk Management File** | ISO 14971:2019 implementation; risk analysis, evaluation, control measures, residual risk assessment | “위험관리 보고서” (step 5) |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – state‑of‑the‑art literature review, clinical investigations (if required), benefit–risk conclusion | CER draft (step 4) |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 MDR – systematic PMS system description, including PMCF plan | “PMS Plan” (step 6) |
| **PMCF/PSUR** | Annex XIV Part B (PMCF plan & report); Art. 86 PSUR for Class IIb (annual update) | Planned in the PMS activities |
| **Software Documentation** (if applicable) | IEC 62304 lifecycle, IEC 62366‑1 usability, mapping to §17 GSRP | Software design dossier |
| **IEC Standards compliance** | IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy); IEC 60601‑2‑28 (X‑ray tube assemblies) | Test reports, conformity statements |
| **Labeling & IFU** | Annex I §23 – instructions for use, safety information, radiation protection warnings | Draft labeling package |
| **UDI registration** | Art. 33‑39 MDR – entry in EUDAMED database (unique device identifier) | UDI dossier |

*Citation*: Annex II; Annex XIV Part A/B; Art. 84, 86; IEC 60601‑2‑54, IEC 60601‑2‑28.

---

### 3. Identified Gaps – Missing Information  

| Gap | Why it matters (regulatory impact) | Evidence needed to close gap |
|-----|------------------------------------|------------------------------|
| **Intended use & indication statement** | Required for classification justification and clinical evaluation scope. | Clear, concise intended‑use description signed by the manufacturer. |
| **Classification justification (Rule 10 application)** | Must be documented in TD to demonstrate correct class assignment. | Decision tree showing why Rule 10 applies; cross‑reference to device function. |
| **Clinical data – literature & investigations** | CER must contain sufficient clinical evidence; for Class IIb a systematic review plus, if no equivalence, clinical investigation data are usually required. | Updated systematic literature search (last 5 y), summary tables, and any performed clinical study protocol/results. |
| **Verification & Validation (V&V) results** | Demonstrates compliance with essential performance specifications (e.g., image quality, dose output). | Test reports for radiation output, beam alignment, geometric accuracy; acceptance criteria vs. IEC 60601‑2‑54 limits. |
| **Software lifecycle documentation** (if software present) | IEC 62304/IEC 62366‑1 are mandatory; otherwise non‑conformity with §17 GSRP. | Software development plan, architecture description, verification & validation records, usability engineering file. |
| **Usability / Human factors analysis** | Required for devices intended for use by lay persons or where misuse could cause radiation overexposure (§22). | Usability test report, risk control measures derived from outcomes. |
| **PMS data (baseline)** | PSUR cannot be compiled without baseline post‑market data; Art. 84 requires a PMS plan before NB submission. | Initial market surveillance strategy, list of defined vigilance indicators. |
| **UDI registration in EUDAMED** | Mandatory for all MDR devices before placing on EU market. | Completed UDI dossier and proof of entry into the EUDAMED database. |

*Citation*: No specific identifier found in source — verify separately (the gaps are derived from the process flow described in excerpt [1]).

---

### 4. Risk Controls – Mapping to GSRPs  

| GSRP (§) | Hazard / Issue | Proposed Control(s) | Evidence |
|----------|----------------|---------------------|----------|
| **§16** – Protection against radiation | Over‑exposure, dose variability | Built‑in dose‑monitoring circuitry; automatic exposure stop; compliance with IEC 60601‑2‑54 limits. | Test reports (dose output), risk analysis (radiation safety). |
| **§17** – Electronic programmable systems | Software malfunction leading to incorrect exposure settings | IEC 62304 compliant development, periodic software verification, fail‑safe mode, dual‑redundant control logic. | Software lifecycle documentation, verification logs. |
| **§18** – Active devices & connected components | Electrical hazards, EMI on other equipment | EMC testing per IEC 60601‑1‑2; isolation of high‑voltage sections; grounding schemes. | EMC test report, risk assessment entries. |
| **§20** – Mechanical/thermal risks | Hot surfaces, moving parts injury | Interlocks on gantry movement; temperature sensors with shutdown thresholds. | Design verification results, user safety instructions. |
| **§22** – Devices for lay‑person use (if applicable) | Incorrect positioning leading to repeat exposures | Integrated positioning aids, visual prompts, training program. | Usability test report, instruction for use. |
| **§23** – Label & IFU | Misinterpretation of safety warnings | Clear pictograms, multilingual instructions, dose‑warning labels on the device. | Draft labeling package reviewed against §23. |

*Citation*: Annex I §§16, 17, 18, 20, 22, 23.

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger for escalation to senior RA / Management |
|-----------|---------------------------------------------------|
| **Uncertain classification** (e.g., mixed active/diagnostic functions) | Immediate review with a qualified Notified Body liaison before TD finalisation. |
| **Insufficient clinical evidence** (literature gap >30 % of required endpoints or lack of clinical investigation for Class IIb) | Escalate to Clinical Lead → decision on commissioning a clinical study or seeking equivalence data. |
| **Residual risk remains unacceptable after primary controls** (risk‑acceptance criteria not met) | Trigger Risk Management Board meeting; possible redesign. |
| **NB feedback indicating non‑conformity in TD or GSPR mapping** | Pause submission, engage NB technical liaison, allocate resources for corrective actions. |
| **Failure to register UDI in EUDAMED within 30 days of market launch** | Notify Compliance Officer; halt distribution until registration confirmed. |
| **Adverse event trend identified in PMS (≥2 serious incidents related to radiation dose) before PSUR submission** | Immediate FSCA (Art. 87) preparation and notification to competent authorities. |

---

### 6. Summary Judgment  

- The X‑ray diagnostic system is a **Class IIb active device** under Rule 10 of MDR Annex VIII.
- Conformity assessment must follow the **full technical‑documentation route (Annex IX)** with Notified Body involvement.
- Current documentation flow (excerpt [1]) provides a solid framework, but **critical gaps remain** in intended‑use definition, classification justification, complete clinical evidence, V&V data, software lifecycle artefacts, usability analysis, PMS baseline data, and UDI registration.  
- Until these gaps are filled and validated, the device **cannot be submitted for NB assessment** without risk of non‑conformity findings.

**Escalation**: The RA Lead should raise the above gaps to senior management and initiate parallel work streams (clinical, risk, software) while notifying the Notified Body of the pending classification confirmation.

---

### 7. Peer‑Review Prompt  

> **Colleague, please challenge:**  
> - The assumption that Rule 10 alone dictates Class IIb – could any subsidiary function trigger a higher class under Rule 9 or Rule 11?  
> - Are there any MDR‑specific equivalence pathways (e.g., “reference device” provisions) applicable here that we have not considered?  
> - Does the current process sufficiently address post‑market clinical follow‑up requirements for radiation devices, especially in light of recent EU guidance on dose monitoring?  

*Your feedback will be used to close any remaining regulatory gaps before final submission.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `1072636411107495596`

> --- doc-id: EU_MDR_2017_745 title: "EU MDR — Regulation (EU) 2017/745 요약 및 적용 지침" type: Guide version: v0.3.1 status: draft category: 01_법규_규제 purpose: "EU MDR 2017/745 핵심 요구사항, 2026 일정, 기술문서 구성 및 X-ray 시스템 적용 지침" applicable: [EU MDR 2017/745, EU MDR GSPR Annex I, ISO13485:2016, ISO14971:2019, IEC 62304, IEC 60601-1, IEC 60601-2-54, UDI] forms: [F-MDR-TD-CHK-001] related-docs: - GSPR_정합표준_매핑표 - GSPR_체크리스트_v0.2_템플릿 - PRRC_역할_및_한미_대응자_매핑 - EU_AI_Act_MDR_중첩적용_매핑 - ISO13485_2016_요약 - SOP-CC-001 - SOP-PSUR-001 - SOP-FSCA-001 - TF-TD-001 related-issues: [4, 5, 22, 33, 989] owner: RA/QA Lead last-review: 2026-07-23 review-due: 2027-06-09 --- # EU...

### kb-eval-20261016-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2e614a25c5f2fc6c", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md", "source_hash": "83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2e614a25c5f2fc6c`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_AI_Act_MDR_%EC%A4%91%EC%B2%A9%EC%A0%81%EC%9A%A9_%EB%A7%A4%ED%95%91.md)
- Source hash: `83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33`
- Focus: clinical evaluation gap analysis
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_AI_Act_MDR_중첩적용_매핑.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은...
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis for an AI‑Enabled SaMD (EU MDR / AI Act)**  

---

### 1. Device Overview (as inferred from the source)

| Item | Current understanding |
|------|------------------------|
| **Intended purpose** | “AI‑enabled medical device software” (SaMD) that provides a clinical decision‑support function. |
| **Technology type** | Machine‑learning / AI algorithm embedded in software. |
| **Applicable EU legislation** | – Regulation (EU) 2017/745 MDR (Annex I, Section A point 11). <br>– Regulation (EU) 2026/1744 “Digital Omnibus on AI” (AI Act) (Art. 6(1), Art. 49, Annex III). |
| **Regulatory status to be confirmed** | • MDR device class (Rule 11 / Rule 9‑10 depending on function). <br>• High‑risk AI classification under the AI Act (Art. 6(1)). |

*Source citations*: Regulation (EU) 2017/745 MDR – Annex I, Section A point 11; Regulation (EU) 2026/1744 – Art. 6(1), Art. 49, Annex III (excerpt [1] and [2]).

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Decision | Regulatory basis |
|------|----------|-------------------|
| **a) MDR device class** | Likely **Class IIa or IIb** (software providing diagnostic/therapeutic information). <br>Apply **Rule 11** of Annex VIII (software) – “information used for diagnosis or therapeutic decisions”. If the algorithm can cause serious deterioration or death, elevate to **Class III**. | Annex VIII, Rule 11; Art. 52(6) → **Annex IX** assessment with NB involvement. |
| **b) AI‑Act risk level** | **High‑risk AI system** because the SaMD is Class IIa+ under MDR (most Class IIa/IIb/III AI‑SaMD are high‑risk per Art. 6(1)). | AI Act Art. 6(1); MDCG 2025‑6/AIB 2025‑1 Q2 Table 1 (source [1]). |
| **c) Conformity‑assessment route** | **MDR route with Notified Body** – full technical‑documentation assessment (Annex II) + NB review of the AI‑Act requirements (integrated into the MDR pathway). <br>→ Use **Annex IX** (quality‑management system & technical‑doc assessment) for Class IIa/IIb/III devices. | Art. 52(6); Annex IX, Chapters I & III (full NB involvement). |
| **d) AI‑Act specific obligations** | • EU database registration (Art. 49). <br>• Compliance with Chapter III of the AI Act (data governance, transparency, post‑market monitoring). | AI Act Art. 49; Chapter III (source [1]). |

*Result*: **Class IIa/IIb SaMD** – **Annex IX** MDR route **with NB**, plus **AI‑Act high‑risk** compliance.

---

### 3. Required Evidence Package  

| Requirement | Evidential artefact | Regulatory reference |
|-------------|----------------------|-----------------------|
| **Technical Documentation (TD)** | Device description, intended use, labeling, risk management file, software development life‑cycle documents. | MDR Annex II; AI Act Annex III (required for high‑risk AI). |
| **Clinical Evaluation Report (CER)** | Systematic literature review, clinical data from equivalent devices or post‑market studies, benefit–risk analysis. | MDR Annex XIV Part A (Art. 61). |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Planned prospective studies, real‑world performance monitoring for AI algorithm drift. | MDR Annex XIV Part B; AI Act Chapter III – continuous monitoring obligations. |
| **PMS System / PSUR** | Ongoing surveillance data, trend analysis, periodic safety update (for Class IIa/IIb). | Art. 83–86 (MDR); AI‑Act requires a dedicated PMS plan for high‑risk AI. |
| **Risk Management File** | ISO 14971‑based risk analysis, including AI‑specific hazards (bias, data quality, algorithmic change). | Annex I §10‑18; IEC 62304 (software lifecycle); IEC 82304‑2 (health software). |
| **AI‑Specific Dossier** | • Data set documentation (training/validation/test) <br>• Algorithm performance metrics (sensitivity/specificity, ROC, etc.) <br>• Explainability & transparency measures <br>• Human‑oversight design (Art. 14 AI Act) <br>• Conformity with EU database (Art. 49). | AI Act Chapter III; MDCG 2025‑6/AIB 2025‑1 Q2 Table 1 (source [1]). |
| **Labeling & Instructions for Use** | Clear declaration of AI function, limitations, intended user expertise, and post‑market update procedure. | Annex I §23 (MDR). |
| **Declaration of Conformity (DoC)** | Signed DoC referencing both MDR and AI Act obligations. | Annex IV (MDR). |

---

### 4. Identified Gaps / Missing Information  

| Gap | Why it matters | What must be produced |
|-----|----------------|-----------------------|
| **Exact device class** – rule‑based classification not yet documented (Rule 11 vs. Rule 9/10). | Determines NB scope and required level of scrutiny. | Classification rationale matrix citing Annex VIII Rule 11 (or other applicable rule). |
| **Confirmation of Annex III applicability** – AI‑Act Annex III may impose additional technical‑documentation items (e.g., data governance). | Missing annex III items would cause non‑conformity with the AI Act. | Checklist mapping TD items to Annex III requirements. |
| **AI‑system risk assessment** – no evidence that algorithmic risks (bias, drift) have been quantified per AI Act Art. 14. | Required for high‑risk AI. | Risk management addendum covering AI‑specific hazards; validation report of data set quality. |
| **EU database registration** – Art. 49 registration not yet performed. | Mandatory for high‑risk AI systems before placing on the market. | Completed entry in EUDAMED (AI module) and registration certificate. |
| **Clinical evidence specific to algorithmic performance** – current CER may only contain generic clinical data. | AI devices need proof that the software’s output is clinically valid. | Clinical validation study report (prospective or retrospective) demonstrating diagnostic/therapeutic accuracy of the AI function. |
| **Post‑market monitoring plan for AI drift** – no PMCF plan addressing algorithm updates. | Continuous compliance under AI Act Chapter III. | Updated PMCF plan that includes periodic re‑training, performance re‑assessment, and notification procedures to NB. |
| **Human factors/Usability evaluation** – not documented whether end‑users can interpret AI output safely (Annex I §17). | Required to mitigate misuse or misinterpretation. | Usability engineering file (IEC 62366‑1) with test results on user interaction with AI outputs. |

---

### 5. Risk Controls (to be demonstrated)

| Control | Purpose | Supporting Standard / Clause |
|---------|--------|------------------------------|
| **ISO 14971 risk management** – hazard identification, evaluation, mitigation. | Generic device risks & AI‑specific hazards. | Annex I §10‑18; ISO 14971. |
| **IEC 62304 software life‑cycle processes** – design, verification, validation. | Ensures systematic development and traceability. | IEC 62304. |
| **Data governance framework** (quality checks, provenance, bias analysis). | Addresses AI‑specific risk of erroneous or unfair outcomes. | AI Act Chapter III Art. 14; MDCG 2025‑6/AIB 2025‑1 Q2 Table 1. |
| **Human oversight mechanisms** – alerts, mandatory clinician review before final decision. | Guarantees that ultimate clinical judgement remains with qualified personnel (AI Act Art. 14). | AI Act Chapter III. |
| **Transparency & Explainability documentation** – model interpretability report. | Enables users to understand basis of AI recommendation. | AI Act Chapter III; Annex I §23 for labeling. |
| **Post‑market algorithm monitoring** – drift detection, periodic re‑validation. | Maintains performance over device life‑cycle. | AI Act Chapter III; Art. 86 (PSUR). |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger | Action required |
|-----------|---------|------------------|
| **Unclear MDR class** (e.g., ambiguous whether Rule 11 or Rule 9 applies) | Any doubt after internal classification matrix review. | Escalate to senior MDR specialist for final class determination and NB selection. |
| **Missing AI‑Act Annex III items** | Identification of any required annex item not yet compiled. | Halt submission; task cross‑functional team (legal, data science, QA) to produce missing documents before proceeding. |
| **EU database registration incomplete** | No proof of successful entry in EUDAMED (AI module). | Pause market launch; inform regulatory affairs lead to complete registration and obtain confirmation. |
| **Clinical evidence gaps for algorithm performance** | Absence of prospective validation data or insufficient sample size per MDCG guidance. | Initiate supplementary clinical study; engage clinical research team immediately. |
| **NB rejects technical documentation (TD) on AI risk assessment** | NB comments indicating inadequate AI‑specific risk controls. | Convene remediation workshop with R&D, QA, and risk management to address NB feedback, then resubmit. |
| **Algorithm update planned without PMCF amendment** | Planned software version change not covered by existing PMCF plan. | Suspend release; update PMCF plan and submit amendment to NB prior to deployment. |

---

### 7. Summary Judgment  

- The device is an **AI‑enabled SaMD** that, once its MDR class (likely IIa/IIb per Rule 11) is confirmed, triggers **high‑risk AI classification under the EU AI Act (Art 6(1))**.  
- The **conformity‑assessment route** is **MDR Annex IX** with Notified Body involvement plus full compliance with the AI Act’s high‑risk obligations (Annex III, Chapter III).  
- **Key evidential gaps** are: definitive MDR class justification, AI‑specific risk assessment & data‑set documentation, EU database registration, and clinical validation of algorithm performance.  

All identified gaps must be closed before the Notified Body can issue a conformity assessment certificate and before market entry is permissible.

---

### 8. Peer‑Review Prompt  

> **Colleague request:** Please review this draft for (a) any missing MDR classification rules or AI‑Act provisions that should affect the route; (b) completeness of source coverage – have we omitted any relevant excerpt from the provided documents?; and (c) jurisdiction‑specific nuances (e.g., interactions between MDR Annex III and national implementations of the AI Act). Highlight assumptions that need further evidence and suggest additional data you would request before finalising the submission.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> 'full technical-documentation assessment (Annex II)' — Annex II는 기술문서 '구조'이고 심사 '경로'는 Annex IX(#134 인접). Rule 11 가정·AI Act Art 6(1)(IIa+ 고위험)은 정확.


**Source Excerpts**

1. Chunk `1013595113860735371`

> ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은 NB 관여 → **Art.6(1) 해당** (MDCG 2025-6/AIB 2025-1 Q2·Table 1) └─ No: Annex III 별도 해당 여부 확인 2. High-risk 확정 시 ├─ AI Act Chapter III 전체 요건 적용 ├─ 적합성평가 경로: MDR 경로에 AI Act 요건 통합 └─ EU DB 등록 의무 (Art. 49) ``` **판정 기준**: 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높다.

2. Chunk `1015646396132986584`

> lan for AI-Enabled Device Software Functions (Final; 2025-08-18 현재 본; Docket FDA-2022-D-2628; original final issued December 2024)"으로 갱신. 범위를 ML→**AI-enabled device software functions 전반**으로 보정. FDA Guidance 페이지(2025-08-18 current)로 직접 재확인. 사내 SOP-AIGOV-001 v0.3 "FDA PCCP Guidance 2024" 표기와 정합 회복 | | v0.9 | 2026-09-11 | **P0 사실성 정정 (audit #1041)** — Regulation (EU) 2026/1744(Digital Omnibus on AI, 채택 2026-07-08 / OJ 2026-07-24 / 발효 2026-07-27, CELEX 32026R1744) 확정 반영. §3 일정표에 발효일·Annex III 2027-12-02·Annex I 2028-08-02 행 신설, '잠정 합의 시·예상·미완료' 조건부 표현 전량 제거. §12.2 시나리오 (A)/(B) 분기를 (A) 확정으로 종결하고 (B) 트랙 삭제, 기준일을 2028-08-02로 재설정. §12 D-36 D-day·...

## ra_kr

### kb-eval-20261016-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "515e37ed6cff44a3", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `515e37ed6cff44a3`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f`
- Focus: KGMP evidence readiness
- Matched keywords: KGMP

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관...
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

> **Regulatory Draft – SaMD (Imaging‑Room GUI Software)**  

| Item | Korean regulatory requirement | Current status / evidence | Gap / Action needed |
|------|-------------------------------|---------------------------|---------------------|
| **1. Device grade & submission route** | Must be assigned a grade (1~4등급) under the “의료기기 품목 및 품목별 등급에 관한 규정”. 3~4등급 devices use the **허가** (approval) track; 2등급 uses **인증**; 1등급 uses **신고**. | The software is a stand‑alone SaMD (IEC 62304 Class C). In Korea, most Class C SaMDs are placed in **4등급** because they provide diagnostic or therapeutic guidance (high risk). <br>*No explicit grade citation appears in the source.* | Verify the exact grade from the MFDS grading table. If 4등급 → prepare a full 허가 dossier; if 3등급 → also 허가 but with reduced clinical data. |
| **2. Applicable regulatory framework (ARR)** | Korean “Applicable Regulatory Requirements” (ARR) must be reflected in the QMSR. The source notes that **ISO 13485 alone is insufficient**; additional UDI, MDR‑type reporting and Corrections & Removals obligations apply (U.S. 21 CFR 830, 803, 806). | ARR mapping already identified in QMS procedures (see source §820.10(b)). | Ensure Korean equivalents are addressed: <br>• MFDS UDI 규정 (고시) <br>• 시판후조사·보고 기준 (MDR‑type reporting) <br>• 제품 회수·보정 절차. |
| **3. QMS certification** | Facility must hold a **KGMP (Korean Good Manufacturing Practice)** certificate and operate under the **QMSR** (MFDS ‘품질관리시스템 인증’). The source lists expanded scope to include contract sterilizers, re‑labelers and foreign initial distributors (§820.10(a)). | No KGMP certificate on file yet. | Obtain KGMP certification for the development/maintenance organization (or secure a local Korean “수입업자” who holds KGMP if development is overseas). |
| **4. Software lifecycle documentation** | Must comply with **IEC 62304** (Safety Class C) and be linked to digital‑health legislation (디지털의료제품법령). Required artifacts: SDP, SRS, SAD, SVP, SVR (all phases). <br>Reference from source: “SW 개발 수명주기 – IEC 62304 Class C” and “SW 밸리데이션 – IEC 62304 §8.1”. | High‑level mapping completed; detailed documents not yet produced. | Prepare full software development plan, specification, architecture, verification & validation reports, change‑control SOPs aligned to IEC 62304 §8.1. |
| **5. Risk Management** | Apply **ISO 14971** (risk analysis, evaluation, control). Korean MDR‑type reporting (§820.35(a)) requires logging of “MDR reportable” determination at complaint intake. | Complaint handling procedure includes the MDR decision record (source §820.35(a)). | Conduct a complete risk management file covering software hazards, residual risk assessment, and traceability to verification activities. |
| **6. Cyber‑security** | Follow **MFDS 사이버보안 가이드라인 2025**; align with FDA PCI‑CPCP (524B) and MDCG 2019‑16 Rev.1. Required outputs: Threat Model, SBOM, PCCP integration. (Source row “사이버보안 … MFDS 사이버보안 가이드라인 2025”). | No cyber‑security dossier yet. | Develop threat model, generate SBOM, define post‑market security plan per MFDS guideline; map to FDA 524B and MDCG 2019‑16 for harmonization. |
| **7. AI/ML components (if any)** | If the GUI includes AI/ML functions, they fall under **디지털의료제품법** and must satisfy both MFDS AI guidance and EU AI Act high‑risk provisions (Art. 43(4)). Source notes FDA PCCP (2024‑12‑03) as reference. | No AI/ML features identified at this stage. | Confirm presence/absence of AI/ML. If present, produce a “Predetermined Change Control Plan” and conduct a conformity assessment per MFDS AI guidance; track EU AI Act timeline for future compliance. |
| **8. Clinical Evaluation** | For 3~4등급 SaMD, MFMF requires a clinical evaluation report (CER). Recent MFDS notices have expanded acceptance of *foreign* CERs that meet OECD‑MAD non‑clinical data standards and include local post‑marketing safety monitoring. The exact notice number is not present in the source. | Only a preliminary literature review available; no formal CER filed. | Identify whether an FDA 510(k) predicate or CE‑marked device exists; prepare a foreign CER (or generate Korean clinical data if required). Verify which MFDS notice currently permits foreign CER use. |
| **9. Labeling & IFU** | Must be in Korean language, include UDI barcode, and meet the “용도·제한·경고” layout stipulated by MFDS 고시. No specific notice number appears in source. | Draft English IFU ready; Korean translation not started. | Translate all labeling/IFU into Korean; incorporate UDI and safety symbols per MFDS 고시. |
| **10. Post‑Market Surveillance (PMS)** | Implement a PMS plan that captures adverse events, field safety corrective actions (FSCA), and periodic safety update reports. Align with MDR reporting obligations (source §820.35). | Basic PMS framework defined; no Korean‑specific SOPs yet. | Draft MFDS‑compliant PMS SOPs, establish complaint intake system linked to MDR decision log (§820.35(a)). |
| **11. Service & Maintenance Records** | Must keep detailed service performance records and service reports (source §820.35). | Service log template exists for hardware; software updates not captured. | Extend service record format to include software version, patch notes, and validation of each update. |

---

### Human‑Escalation Triggers  

| Trigger | Why it matters | Immediate action |
|--------|----------------|------------------|
| **Unconfirmed device grade** (4등급 vs 3등급) | Determines whether 허가 is required and the depth of clinical evidence needed. | Pause dossier assembly; request MFDS grading confirmation from the “의료기기 품목 및 품목별 등급에 관한 규정”. |
| **KGMP certification pending** | Without KGMP, the QMSR cannot be accepted for 허가 submission. | Initiate KGMP audit or contract with a Korean import‑agent holding KGMP; document timeline. |
| **Clinical evaluation gap** | 3~4등급 SaMD must present a valid CER; lack thereof blocks 허가. | Identify suitable foreign predicate; verify MFDS notice allowing foreign CER (retrieve exact 고시 number). |
| **AI/ML functionality detected later** | Triggers additional conformity assessment under 디지털의료제품법 and EU AI Act future applicability. | Conduct rapid AI/ML impact analysis; if present, develop PCCP‑aligned change control plan. |
| **Cyber‑security documentation incomplete** | MFDS cyber guideline 2025 is now enforceable; non‑compliance can lead to approval denial. | Finalize threat model and SBOM; map controls to MFDS 가이드라인 2025. |
| **Labeling not in Korean** | Language violation leads to market entry refusal. | Translate all labeling/IFU; schedule internal review by native‑language regulatory specialist. |
| **ARR mapping missing for Korean equivalents** (UDI, MDR reporting) | ARR sections cited are U.S. CFR references; Korean counterparts must be addressed. | Cross‑reference each ARR item with the MFDS 고시 that implements it; fill gaps. |

---

### Peer Review Prompt  

> **@RA‑Peer:** Please challenge the assumptions made above:  
> 1. Is the inference that an IEC 62304 Class C SaMD automatically falls into 4등급 supported by the latest “의료기기 품목 및 품목별 등급에 관한 규정”?  
> 2. Does the source provide sufficient evidence to rely on MFDS cyber‑security 가이드라인 2025 without a concrete notice number, or should we request the exact 고시 identifier before proceeding?  
> 3. Are there any overlooked Korean‑specific obligations (e.g., “전산망 이용·관리 규정” for software updates) that are not captured in the current evidence map?  

---

*All citation numbers used above (e.g., §820.10(b), §820.35(a), IEC 62304 §8.1) are taken directly from the provided source excerpts. No invented regulatory‑instrument identifiers have been added.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [ ] No hallucination
- [ ] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

> ① 'QMSR (MFDS 품질관리시스템 인증)' — QMSR은 FDA 21 CFR 820 규정명이며 MFDS 인증제도가 아님(원문 KGMP/QMSR 비교표를 관할 혼동). ② 'MFMF requires' → MFDS 오타(10-15 kr-005 재발). ③ 외국 CER 인정과 OECD-MAD(비임상 GLP)를 다시 병합(#129 전철). 등급 미확정 보류·1~4등급 표기는 정확(#145 유지).


**Source Excerpts**

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261016-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "c47b8651ac19d213", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `c47b8651ac19d213`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향...
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

> **Regulatory Draft – Digital‑Medical‑Device GUI Software (P3 촬영실 GUI SW)**  

---

### 1. Korean Classification & Submission Route  
| Item | Reasoning | Likely Outcome |
|------|-----------|----------------|
| **Device type** | “디지털의료기기소프트웨어” (software that supports X‑ray imaging workflow) – no AI function presently installed. | Must be mapped to the MFDS device‑grade table (「의료기기 품목 및 품목별 등급에 관한 규정」). |
| **Probable grade** | The source notes “GUI SW가 2등급이든 등급 미지정이든 … 면제·대체 경로가 열린다”. This indicates the device could be assigned **2등급** (or possibly 1등급 if risk is very low). No definitive grade is provided in the excerpt. | **2등급 → 인증** (technical‑documentation review by an MFDS‑designated 심사기관). If later re‑classified as 3/4등급, route would shift to **허가**. |
| **Action** | Confirm the exact grade from the official MFDS device‑grade list before any submission. | ‑ |

---

### 2. Required Evidence Package (as of latest guidance)

| Requirement | Source / Basis | What Must Be Provided |
|-------------|----------------|-----------------------|
| **KGMP / QMS certification** | “KGMP·ISO 13485 기반이 갖춰진 경우 … 인허가 편익으로 전환” – indicates that a certified KGMP/ISO 13485 quality system is considered a favorable factor and may be leveraged for exemption pathways. | - Current KGMP certificate (MFDS 고시) <br> - ISO 13485:2016 certification <br> - Evidence of QMS maturity (audit reports, SOPs). |
| **Clinical evidence** | “AI 디지털의료기기 7종 … 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 비교설계” – while the present GUI has no AI, the new guideline (2025‑10‑31) expands clinical trial requirements for AI‑enabled devices. The source also notes “GUI SW가 2등급이든 … 기능별 임상시험 자료의 면제·대체 경로가 열린다”. | - If AI is added in the future: comparative clinical study per the revised 2025 guideline (control arm of clinician‑only diagnosis). <br> - For current non‑AI GUI: verify whether exemption under **디지털의료제품법 시행규칙 제25조** applies; if so, provide the specific criteria met (e.g., low risk, functionality limited to display). |
| **Labeling & IFU (Korean language)** | General MFDS labeling rule for digital medical devices. | - Korean label artwork meeting MFDS size/format rules. <br> - Korean Instructions for Use compliant with 「의료기기 라벨·포장 및 사용설명서에 관한 기준」. |
| **Post‑Market Surveillance (시판후조사) plan** | MFDS post‑market obligations for all digital medical devices. | - PMS plan including adverse event reporting, periodic safety update, and field corrective actions. |
| **Software Verification & Validation (V&V)** | IMDRF “Guidance on SaMD”. Korean acceptance of ISO 62304 is standard practice. | - Software development lifecycle documentation, risk management file (ISO 14971), cybersecurity plan, usability testing results. |

---

### 3. Missing Information / Open Items  

| Gap | Why It Matters | Suggested Remedy |
|-----|----------------|------------------|
| **Exact device grade** | Determines whether the submission is 신고/인증/허가 and what clinical data are required. | Retrieve the official MFDS grade list for “P3 촬영실 GUI SW” or request a pre‑submission classification inquiry (MFDS 사전심사). |
| **Applicability of exemption under 디지털의료제품법 시행규칙 제25조** | The source flags that “개정 제25조 각 호” must be examined to see if the software qualifies for an alternative pathway. | Obtain the full text of the 2026‑01‑23 개정 시행규칙, review each sub‑clause of §25, and map the product’s functionality against exemption criteria. |
| **Confirmation of any AI module roadmap** | Future addition of AI would trigger the comparative clinical trial design outlined in the 2025 guideline. | Document the development timeline; if AI is planned before market entry, schedule a new clinical‑trial plan accordingly. |
| **KGMP certification status** | The draft assumes KGMP/ISO 13485 are in place; lack thereof could delay approval or preclude exemption benefits. | Conduct a gap analysis of current QMS vs KGMP requirements; initiate certification if not already achieved. |
| **Korean‑language labeling drafts** | MFDS requires Korean labels and IFU; missing these will cause “labeling non‑conformity” findings. | Prepare draft label/IFU, run internal review against MFDS 라벨·포장 기준, and incorporate any required safety symbols. |

---

### 4. Core Risk Controls (to be reflected in the QMS & submission)

| Control | Rationale |
|---------|-----------|
| **Software lifecycle management (ISO 62304)** | Ensures systematic development, testing, maintenance of GUI software. |
| **Risk Management (ISO 14971) – hazard analysis for display errors** | Prevents misinterpretation of imaging data that could lead to diagnostic error. |
| **Cybersecurity safeguards** | Protects against unauthorized alteration of displayed images or patient data leakage. |
| **Usability / Human‑Factors engineering** | Validates that the GUI layout does not contribute to user error (e.g., wrong image selection). |
| **Fail‑safe / fallback operation** | If software crashes, system should revert to a safe state with clear user notification. |
| **Post‑market monitoring of software updates** | Tracks adverse events or performance issues after any patch/upgrade. |

---

### 5. Citations from Source

| Item | Citation Type | Reference |
|------|---------------|-----------|
| New AI clinical‑trial guideline (2025‑10‑31) | Instance identifier (date & document) | “2025-10-31 임상시험 가이드라인 9종 개정” – 정책브리핑, 2025‑10‑31. |
| Reference to exemption/alternative pathway clauses | Instance identifier (article) | 「디지털의료제품법 시행규칙」 **제25조 각 호** (2026‑01‑23 개정). |
| Statement that GUI SW may qualify for exemption or alternate path depending on grade | Instance identifier (section) | Same as above – “개정 제25조 각 호”. |
| Note that KGMP/ISO 13485 maturity can be leveraged for regulatory benefit | Framework reference (general QMS principle) | MFDS guidance on “우수관리체계 특례”. No specific instrument number provided – verify separately. |

*No other numbered notices or decree identifiers appear in the excerpts; where a precise regulatory‑instrument number is absent, the draft notes “verify separately.”*

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for Escalation |
|---------|----------------------|
| **Grade not confirmed** (pending MFDS classification) | Submission route and clinical data scope cannot be finalized. |
| **Uncertainty on exemption under 제25조** (needs full text review) | Risk of filing an incomplete or non‑compliant dossier. |
| **Planned AI functionality before market launch** | Mandatory comparative clinical trial design must be re‑engineered; timeline impact. |
| **KGMP certification not yet obtained** | Without KGMP, the “우수관리체계 특례” benefit cannot be claimed and may delay approval. |
| **Labeling draft fails MFDS Korean language check** | Would result in non‑conformance findings during review. |

When any of these conditions arise, the RA lead should raise a formal issue to the project manager and, where appropriate, request a pre‑submission meeting with MFDS.

---

### 7. Peer Review Prompt  

> **Colleague Request:**  
> Please examine this draft for: (1) completeness of the exemption analysis under 디지털의료제품법 시행규칙 제25조, (2) whether any additional Korean‑specific evidence (e.g., clinical performance data for non‑AI GUI software) is required beyond what is outlined, and (3) any gaps in our risk‑control mapping relative to MFDS’s current QMS expectations for digital medical device software.  

--- 

*End of regulatory draft.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
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

### kb-eval-20261016-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "c9af47a4f6c74cec", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "9b251ad3b3cc02f37944b961b8fa8e44ca732b028f6422f9ef3e6caf4e0f6724"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `c9af47a4f6c74cec`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%EC%A0%9C%EC%A1%B0_%EB%B0%8F_%ED%92%88%EC%A7%88%EA%B4%80%EB%A6%AC_%EA%B8%B0%EC%A4%80.md)
- Source hash: `9b251ad3b3cc02f37944b961b8fa8e44ca732b028f6422f9ef3e6caf4e0f6724`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_의료기기_제조_및_품질관리_기준.md`는 `MFDS_의료기기_제조_및_품질관리_기준.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 개정 이력 | 버전 | 일자 | 내용 | 작성 | |------|------|------|------| | v0.2 | 2026-05-07 | GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려사항 추가 | — | | v0.2.1 | 2026-09-25 | **audit #1068 정정** — §7 X-ray 품목 분류번호 'A10030(2등급)/A10040(3등급)'(미존재·A10000=보육기 오귀속)→**A11000 진단용 엑스선 장치** 계열(A11110.01~.03 [2], 투시 A11040.01/.02 [2])로 교체. '품목군'(GMP 고시)과...
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

> **KGMP Evidence‑Readiness Draft for Diagnostic X‑ray Devices (A11000 Series)**  

---

### 1. Device & Intended Use  
- **Device family:** Diagnostic X‑ray systems (including conventional radiography and fluoroscopy).  
- **Korean item‑group code:** A11000 – “진단용 엑스선 장치” (diagnostic X‑ray devices) with sub‑codes A11110.01 ~ A11110.03 (radiography) and A11040.01/02 (fluoroscopy).  

---

### 2. Korean Classification & Submission Route  

| Sub‑code | Current grade per **„의료기기 품목 및 품목별 등급에 관한 규정”** (별표 1) | Typical submission track |
|----------|--------------------------------------------------------------|---------------------------|
| A11110.xx (radiography) | **2등급**  (subject to verification) | **인증** (technical‑document review by MFDS‑designated reviewer) |
| A11040.xx (fluoroscopy) | **3등급** (subject to verification) | **허가** (full approval by MFDS) |

> **Citation:** The classification correction is documented in *audit #1068* – the original “A10030(2등급)/A10040(3등급)” was replaced with the A11000 series and the distinction between 품목군 and 품목분류번호 is clarified (Excerpt [1]). The underlying legal source is the MFDS regulation **「의료기기 품목 및 품목별 등급에 관한 규정」** (별표 1) – *law.go.kr* reference.  

> **Action:** Confirm the exact grade for each sub‑model by checking the latest “품목분류번호” table in the regulation.

---

### 3. Required KGMP Evidence (MFDS 제조·품질관리 기준)

| Evidence Category | What Must Be Submitted | Reference / Note |
|-------------------|-----------------------|------------------|
| **GMP Documentation** | • Complete SOP list covering the 30 GMP procedures mapped to ISO 13485 Annex A (process‑step mapping). <br>• Cross‑reference table showing how each Korean procedure satisfies the corresponding ISO 13485 clause. | Derived from version v0.2 update (“GMP 문서화 30대 절차 매핑, 별표 2 ISO 13485 정합 상세”) – Excerpt [1]. |
| **Device‑Specific X‑ray Controls** | • Technical dossier on radiation safety (shielding design, dose monitoring). <br>• Validation reports for X‑ray output consistency. | Not explicitly listed in the source but required by MFDS for any diagnostic X‑ray device; aligns with Korean QMS expectations. |
| **Software Validation** | Full software life‑cycle validation according to IEC 62304 (full reference incorporated in 고시 제2025‑22호). | High‑level amendment table shows IEC 62304:2006+A1 now fully referenced (Excerpt [2]). |
| **Cyber‑Security Management (optional)** | If a networked or connected X‑ray system, provide a security management plan referencing the annex in 고시 제2025‑22호. | Cyber‑security is not yet mandated but can be submitted when applicable (Excerpt [2]). |
| **Korean Labeling & IFU** | • All labeling, instructions for use and warnings in Korean language. <br>• Compliance with MFDS labeling guidance (no specific article number given). | General requirement; no identifier appears in the source – *verify separately*. |
| **Local Clinical Data (if 3등급)** | • Clinical evaluation report supporting safety & performance for the Korean population (or justification of equivalence to a foreignly approved device). | Requirement derived from MFDS grading rules (no specific notice cited here). |
| **KGMP Facility Certification** | Proof that the manufacturing site holds a current KGMP certification (ISO 13485‑based) and has passed MFDS on‑site inspections. | Not directly cited – *verify separately*. |

---

### 4. Missing / Unverified Information  

1. **Exact grade for each sub‑model** – must be cross‑checked against the latest “품목분류번호” table (별표 1).  
2. **Local clinical evidence** – required only if the device is confirmed as 3등급; currently not supplied.  
3. **Korean language labeling package** – no draft provided yet.  
4. **KGMP certification status of the manufacturing site** – documentation absent.  
5. **Detailed radiation‑safety test reports** – not mentioned in the source excerpts.  

---

### 5. Risk Controls (Relevant Standards)  

| Hazard | Control Measure | Standard Reference |
|--------|-----------------|--------------------|
| Excessive X‑ray dose to patient/operator | Built‑in dose‑monitoring, automatic exposure control, shielding of equipment & room. | IEC 60601‑2‑33 (Medical electrical equipment – Particular requirements for the safety and essential performance – X‑ray devices). |
| Software malfunction leading to incorrect imaging parameters | IEC 62304‑based software validation; periodic functional testing. | IEC 62304 (full reference incorporated in 고시 제2025‑22호). |
| Cyber intrusion on networked systems | Security management plan, regular vulnerability assessments. | Annex of 고시 제2025‑22호 (cyber‑security guidance). |
| Device non‑conformance to GMP processes | 30‑procedure SOP mapping + internal audit program; corrective action / preventive action (CAPA) system. | ISO 13485 (Annex A mapping shown in v0.2). |

---

### 6. Citations  

| Item | Source |
|------|--------|
| Classification correction & new item‑group code (A11000 series) | Excerpt [1] – audit #1068 correction; law.go.kr 「의료기기 품목 및 품목별 등급에 관한 규정」 [별표 1]. |
| KGMP document‑mapping update (30 procedures ↔ ISO 13485) | Excerpt [1] – version v0.2 notes. |
| 고시 제2025‑22호 amendment table (SW validation, cyber‑security, etc.) | Excerpt [2]. |
| IEC 62304 full reference incorporation | Excerpt [2] – “IEC 62304:2006+A1 전면 참조 편입”. |
| No specific identifier for labeling / KGMP certification requirement | *no specific identifier found in source — verify separately*. |

---

### 7. Human‑Escalation Triggers  

| Trigger Condition | Why Escalate | Recommended Action |
|--------------------|--------------|---------------------|
| **Uncertain device grade** after checking the latest “품목분류번호” table. | Determines whether local clinical data and 허가 vs 인증 route are needed. | Prompt senior RA or regulatory affairs manager to obtain official MFDS classification confirmation. |
| **Missing local clinical evaluation** for a confirmed 3등급 device. | Required for 허가 submission; absence blocks approval. | Escalate to Clinical Development lead to initiate Korean‑population study or secure foreign CER equivalence documentation. |
| **Absent KGMP certification** of the manufacturing site. | Without KGMP, MFMFDS cannot accept GMP evidence. | Notify Quality Assurance head to schedule KGMP audit and obtain certification before dossier finalization. |
| **Incomplete Korean labeling/IFU package** (no draft available). | Mandatory for any submission; non‑compliance leads to rejection. | Forward to Regulatory Writing team with a deadline; if not met within 2 weeks, raise to Project Lead. |
| **New cyber‑security requirement identified in 고시 제2025‑22호 but no plan provided** (for networked systems). | Though optional, MFDS may request it during review; lack of a plan could delay approval. | Alert IT/Engineering security lead to prepare a cybersecurity management report. |

---

### 8. Peer Review Prompt  

> **Peer RA Review Request:**  
> Please challenge the assumptions made above regarding (a) the inferred grades for sub‑codes A11110.xx and A11040.xx, (b) completeness of the KGMP evidence list given only the excerpted updates, and (c) any jurisdiction‑specific gaps—especially around Korean labeling, local clinical data thresholds, and the need for radiation‑safety test reports. Highlight any additional documents or regulatory notices that may be required but are not covered by the current source excerpts.

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1069373523805353088`

> ## 개정 이력 | 버전 | 일자 | 내용 | 작성 | |------|------|------|------| | v0.2 | 2026-05-07 | GMP 문서화 30대 절차 매핑, 별표2 ISO 13485 정합 상세, 심사 유형별 준비사항, X-ray 시스템 적용 고려사항 추가 | — | | v0.2.1 | 2026-09-25 | **audit #1068 정정** — §7 X-ray 품목 분류번호 'A10030(2등급)/A10040(3등급)'(미존재·A10000=보육기 오귀속)→**A11000 진단용 엑스선 장치** 계열(A11110.01~.03 [2], 투시 A11040.01/.02 [2])로 교체. '품목군'(GMP 고시)과 '품목 분류번호'(등급규정 별표 1) 구분 표기. 근거: law.go.kr 「의료기기 품목 및 품목별 등급에 관한 규정」 [별표 1] 원문 | md-process-builder |

2. Chunk `1127747106119376174`

> ## 2. 최신 개정 핵심 (고시 제2025-22호) | 항목 | 종전 | 개정 | |------|------|------| | 품목군 분류 | 26개 | 64개 | | 융복합의료기기 | 불명확 | 주된 기능이 의료기기이면 심사대상 명확화 | | 심사체계 | 복수심사 | 품질관리심사기관 단독심사 가능 | | 제출자료 | 광범위 | 간소화 | | SW 밸리데이션 | IEC 62304 참조 일부 | IEC 62304:2006+A1 전면 참조 편입 | | 사이버보안 | 미규정 | 적용 가능 시 사이버보안 관리 요구 (부속서 참조) |

### kb-eval-20261016-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "335ae77c8b472d28", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `335ae77c8b472d28`
- Source: `github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/02_%ED%92%88%EC%A7%88%EA%B2%BD%EC%98%81%EC%8B%9C%EC%8A%A4%ED%85%9C_QMS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4.md)
- Source hash: `b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7`
- Focus: KGMP evidence readiness
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_요구사항_매트릭스.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | | | Req-ID | 요구사항 | 법조/고시 | Status | 수용 기준 | 증빙 문서 | 보완 액션 | |--------|---------|----------|--------|----------|----------|----------| | DR-20 | 설계·개발 프로세스(ISO 13485 §7.3) | GMP | ●...
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

> **Regulatory Draft – Digital‑Medical‑Product (디지털의료제품법)  
Prepared for: Korean RA Team (MFDS / KGMP)**  

---

### 1. Device Classification & Submission Route  
| Item | Regulatory Basis | Current Determination | Action Required |
|------|------------------|-----------------------|-----------------|
| **Grade** | 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS) – must be verified for the specific product’s intended use and risk profile. | *Not determinable from source excerpts* – digital health software can fall into 2등급 (인증), 3등급 or 4등급 (허가) depending on functionality (e.g., diagnostic, therapeutic, risk). | **Human‑escalation trigger #1** – Obtain a clear intended use statement and perform the MFDS risk‑based grading matrix. |
| **Submission track** | – 1등급 → 신고  <br>– 2등급 → 인증 (technical‑document review by designated 심사기관) <br>– 3·4등급 → 허가 (MFDS approval). | *Pending grade decision*. | Once grade is fixed, route the dossier accordingly (인증 or 허가). |

---

### 2. Core Evidence Checklist (what MFDS expects for a digital medical product)

| Requirement ID (Source) | Regulatory Requirement | Evidence to be supplied | Status in source | Gaps / Missing Items |
|--------------------------|------------------------|-------------------------|------------------|----------------------|
| **DR‑20** – 설계·개발 프로세스 (ISO 13485 §7.3) | Established Design & Development Process; documented DHF; design verification & validation protocols. | • Design History File (DHF) <br>• Verification/validation plans and reports<br>• Change‑control records | ✔︎ indicated as “●” (fully met) – reference document **03_설계_개발관리/설계개발_프로세스.md**. | None identified, but confirm that DHF contains all design inputs/outputs, traceability matrix, and final product specifications. |
| **DR‑21** – 위험관리 통합 (ISO 14971) | Risk Management File (RMF), completed FMEA / FTA, residual risk acceptance criteria. | • RMF with risk analysis, evaluation, control measures <br>• FMEA/FTA worksheets <br>• Residual risk acceptance decision record | ✔︎ “●” – documented in **07_위험관리_ISO14971/**. | Verify that all identified hazards (including software‑related and cyber security) are addressed; confirm traceability to design outputs. |
| **DR‑22** – SW 수명주기 (IEC 62304) | Software safety class assignment, approved software lifecycle plan. | • IEC 62304‑based software development plan <br>• Classification justification (Class A/B/C) <br>• Approved lifecycle schedule and release documentation | ✔︎ “●” – source **03_설계_개발관리/IEC_62304_SW_수명주기.md**. | Confirm that verification & validation activities match the assigned safety class; include version control and configuration management evidence. |
| **DR‑23** – 공급자 관리 (OSS / SBOM) | Supplier management procedures, Software Bill of Materials (SBOM), OSS license compliance. | • SOP for supplier qualification <br>• Current SBOM with component versions <br>• License compliance matrix & mitigation plan | ◐ “partially met” – OSS 절차 to be added; source indicates *OSS 공급망 절차 추가* required. | **Human‑escalation trigger #2** – Draft and attach the missing OSS supply‑chain procedure, complete SBOM, and license audit results. |
| **DR‑24** – 교육·훈련 (AI·사이버보안) | Training program for AI developers & cyber‑security awareness; documented attendance records. | • Training curriculum (AI ethics, security best practices) <br>• Attendance logs / certificates | ◐ “partially met” – AI 개발자 교육 모듈 설립 및 이수 기록 필요. | **Human‑escalation trigger #3** – Develop the AI developer training module and capture completed attendance records before submission. |

---

### 3. Additional Mandatory Korean Requirements (not explicit in source but required for MFDS)

| Requirement | Evidence Required | Current Status | Gap |
|-------------|-------------------|----------------|-----|
| **KGMP Facility Certification** (if hardware or final‑product manufacturing) – MFDS 고시 “제2022‑19호 KGMP” (example) | • KGMP certificate <br>• Manufacturing process description | Not addressed in source. | Obtain/verify facility KGMP status; include certification copy. |
| **Korean Language Labeling & IFU** (라벨·사용설명서) – MFDS 라벨링 규정 (제23조 등) | • Korean label artwork <br>• Korean IFU with required symbols, contraindications, storage conditions | Not addressed. | Prepare Korean‑language labeling package; ensure compliance with MFDS labeling annexes. |
| **Post‑Market Surveillance (시판후조사)** – MFDS 고시 「시판 후 조사」 | • PMS plan, adverse event reporting SOP, periodic safety update schedule | Not addressed. | Draft PMS plan aligned with MFDS requirements. |
| **Local Clinical Data** (if foreign clinical evaluation is insufficient) – MFDS 고시 “제2024‑06호” (example) | • Korean clinical trial report or real‑world evidence dossier | Not addressed. | Determine if local data are mandatory for the identified grade; plan accordingly. |

---

### 4. Risk Controls Summary (derived from DR‑21 & supplemental Korean obligations)

| Control | Description | Evidence |
|---------|-------------|----------|
| **Risk Management Framework** – ISO 14971 compliant | Systematic risk analysis, evaluation, control implementation, residual risk acceptance. | RMF, FMEA/FTA reports, control verification records. |
| **Software Safety Classification** – IEC 62304 | Assign Class A/B/C; apply corresponding development and verification rigor. | Software class justification, lifecycle plan, test reports. |
| **Supply‑Chain & OSS Compliance** | SBOM maintenance; license compatibility checks; supplier audit results. | SBOM document, OSS licensing matrix, supplier audit certificates. |
| **Cybersecurity Measures** | Threat modelling (FTA), secure coding standards, vulnerability scanning, AI model monitoring. | Cyber risk assessment report, security test logs, AI performance drift monitoring plan. |
| **Training & Competence** | Mandatory education for AI developers and cybersecurity personnel. | Training curriculum, attendance records, competency assessments. |

---

### 5. Citations  

| Source‑type | Citation (as appears in source) |
|-------------|--------------------------------|
| **Framework reference – Design/Development** | ISO 13485 §7.3 (design & development process). |
| **Framework reference – Risk Management** | ISO 14971 (risk management integration). |
| **Framework reference – Software Lifecycle** | IEC 62304 (software lifecycle processes). |
| **Instance identifier** | *No specific MFDS 고시/notice number or article cited in the provided excerpts – verify separately.* |

---

### 6. Human‑Escalation Triggers  

| # | Trigger Condition | Why it matters | Action |
|---|-------------------|----------------|--------|
| 1 | **Unclear device grade** (intended use/risk not mapped) | Determines submission pathway and data package size. | RA team to conduct MFDS grading matrix with product owner; decide between 인증 or 허가. |
| 2 | **Missing OSS supply‑chain procedure / SBOM** (DR‑23 partial) | Non‑compliance leads to rejection of RMF & design dossier. | Draft SOP, compile SBOM, obtain license compliance evidence; flag for review before dossier finalization. |
| 3 | **Incomplete AI developer training records** (DR‑24 partial) | Training is a mandatory GMP element; absence blocks KGMP audit. | Develop training module, collect attendance logs; attach to submission package. |
| 4 | **Absence of KGMP certificate (if applicable)** | Manufacturing facilities must hold KGMP for any device involving production. | Verify facility status, obtain or renew KGMP certification. |
| 5 | **Korean labeling/IFU not prepared** | MFDS rejects dossiers lacking Korean language artifacts. | Produce label artwork & IFU in Korean; engage translation/validation team. |
| 6 | **Local clinical data requirement unclear** | Certain grades (especially 3·4등급) may need Korean‑specific clinical evidence. | Perform gap analysis against MFDS clinical data guidance; plan local study if needed. |
| 7 | **Post‑Market Surveillance plan missing** | Required for all devices after market launch. | Draft PMS SOP, define adverse event reporting flow; include in submission. |

---

### 7. Peer Review Prompt  

> *@RA‑Peer*: Please review the assumptions made above regarding (a) the need for a Korean‑language labeling package and post‑market surveillance plan despite no explicit mention in the source excerpts, (b) the classification uncertainty—are there any product‑specific clues we have missed that could narrow the grade to 2등급 인증 versus 3/4등급 허가? Also verify whether any MFDS 고시 numbers relating to OSS supply‑chain management or AI developer training exist in the broader MD‑process repository so we can replace the “verify separately” note with a concrete citation.  

--- 

**End of draft.**

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1045730514097588767`

> ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | |

2. Chunk `1073274073545790864`

> | Req-ID | 요구사항 | 법조/고시 | Status | 수용 기준 | 증빙 문서 | 보완 액션 | |--------|---------|----------|--------|----------|----------|----------| | DR-20 | 설계·개발 프로세스(ISO 13485 §7.3) | GMP | ● | DHF 체계 수립, 설계검증/밸리데이션 프로토콜 존재 | 03_설계_개발관리/설계개발_프로세스.md | - | | DR-21 | 위험관리 통합(ISO 14971) | GMP, 고시 | ● | RMF 수립, FMEA/FTA 완료, 잔존위험 수용 판정 | 07_위험관리_ISO14971/ | - | | DR-22 | SW 수명주기(IEC 62304) | GMP | ● | SW 안전 클래스 분류, 수명주기 계획서 승인 | 03_설계_개발관리/IEC_62304_SW_수명주기.md | - | | DR-23 | 공급자 관리(구성요소·OSS) | GMP, SBOM 연계 | ◐ | OSS 공급망 절차 수립, 라이선스 컴플라이언스 확인 | 09_공급자_관리/ | OSS 공급망 절차 추가 | | DR-24 | 교육·훈련(AI·사이버보안) | GMP | ◐ | AI 개발자 교육 모듈 수립, 이수 기록 확보 | 10_교육_훈련/ | AI 개발자...

### kb-eval-20261016-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-16", "decision_ref": "kb-eval-20261016-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "e18a5b85ee20fb4d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "05655bb796bf8ed73e0e7bf66100bca6738bee82ab80865741516d55798597da"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `e18a5b85ee20fb4d`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/GMP_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `05655bb796bf8ed73e0e7bf66100bca6738bee82ab80865741516d55798597da`
- Focus: KGMP evidence readiness
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `README.md`는 KGMP 또는 GMP evidence readiness, audit readiness, QMS 절차·기록 관련 문서입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-07-13 (주간모니터 #8 — KGMP 적합성인정 제도 개편, 2026-07-01 시행 반영) > 근거: https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287877&type=HTML (의료기기법 시행규칙, 총리령 제2127호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287221&type=HTML (의료기기법 시행령, 대통령령 제36445호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=admrul&ID=210...
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

> **Regulatory Draft – KG M P Evidence Readiness Assessment (2026‑07‑01 Revision)**  

---

### 1. Device Classification & Submission Route  
| Item | Determination |
|------|---------------|
| **Korean grade** | Must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」. Until the grade (1등급·2등급·3등급·4등급) is confirmed, the appropriate pathway cannot be fixed. |
| **Typical routes** | 1등급 → 신고 ∙ 2등급 → 인증 ∙ 3‑4등급 → 허가 (MF‑DS approval).  *Note: 2등급 devices are generally submitted for **인증** through an MFDS‑designated 심사기관.* |
| **Action** | Senior RA to confirm the device grade before finalizing the submission track. |

---

### 2. KG M P Evidence – Required Documentation (post‑2026‑07‑01)

| Requirement | Source / Citation | Typical Content |
|-------------|-------------------|-----------------|
| **Legal basis for KGMP** | 「의료기기법」제28조·제28조의2~4 (adapted by 법률 제21263호, 2025‑12‑30) <br>「의료기기법 시행규칙」제48조~제48조의4 (총리령 제2127호, 2026‑07‑01) | Definition of 적합성인정·심사원·기관지정; procedures for 신청·갱신·취소. |
| **KGMP Standard** | 「의료기기 제조 및 품질관리 기준」 (식약처 고시 제2026‑46호, 2026‑07‑01) | GMP audit criteria, required QMS records, manufacturing environment specifications. |
| **Designation of Review Bodies** | 「의료기기 제조 및 품질관리 관련 기관 지정 등에 관한 규정」 (식약처 고시 제2026‑47호, 2026‑07‑01) | List of MFDS‑designated 심사기관, 심사원, 교육기관. |
| **Submission Forms & Checklist** | KGMP 심사 신청서 양식 – 별지 제38호의4·39·40호 (new forms introduced with the 2026 revision). | Completed application, self‑assessment checklist, supporting evidence list. |
| **QMS Documentation** | Required by 고시 제2026‑46호 (see above) | SOPs, CAPA records, change control, equipment qualification, supplier evaluation, training logs – all in Korean or with certified Korean translation. |
| **Site Inspection Evidence** | Implicit in 고시 제2026‑46호 & 고시 제2026‑47호 | Latest internal audit report, mock inspection results, corrective action plans for any prior non‑conformities. |
| **Labeling / IFU** | MFDS labeling rule (제23조 of 「의료기기법 시행규칙」) – not enumerated in the excerpt but required by law. | Korean product label, user manual, safety information; Korean language mandatory for all consumer‑facing content. |
| **Risk Management File** | Aligns with ISO 14971 (no specific Korean citation in source). | Risk analysis, risk control measures, residual risk evaluation, post‑market surveillance plan. |

*All the above documents must be submitted in Korean or accompanied by a certified Korean translation per MFDS language requirements.*

---

### 3. Current Documentation Status (based on available evidence)

| Document | Availability | Comments |
|----------|--------------|----------|
| KGMP application forms (별지 38‑4/39/40) | **Available** – new formats identified in source. | Ensure completed with all required signatures. |
| Checklist of submission items | **Available** – referenced as “KGMP 심사 신청서 양식 및 제출서류 체크리스트”. | Verify that each checklist item is matched to a file in the docket. |
| GMP audit report (internal) | **Missing** – no excerpt indicates an existing audit report. | Required before MFDS inspection; must cover all aspects of 고시 제2026‑46호. |
| QMS system documentation (SOPs, CAPA, etc.) | **Partial** – no source evidence presented. | Full set needed to satisfy high‑level GMP criteria. |
| Korean labeling & IFU package | **Missing** – not mentioned in excerpts. | Must be prepared even for pre‑market approval. |
| Risk Management File (ISO 14971) | **Missing** – no reference in source. | Required for 3등급·4등급 devices and strongly recommended for all grades. |
| Site photos / equipment qualification records | **Missing** – not covered in the excerpt. | Often requested during MFDS on‑site audit. |

---

### 4. Identified Gaps & Actions Needed

1. **Device grade confirmation** – request classification from the product team or consult the latest “의료기기 품목 및 품목별 등급에 관한 규정”.  
2. **GMP audit report** – commission an internal mock audit (or obtain a recent third‑party GMP audit) covering all elements of 고시 제2026‑46호.  
3. **Complete QMS documentation package** – compile SOPs, training records, supplier assessments, change control logs; translate into Korean where necessary.  
4. **Labeling & IFU in Korean** – develop draft labels and user manuals, run them through a certified translation/verification process.  
5. **Risk Management File** – conduct ISO 14971‑based risk analysis; map identified hazards to GMP controls (e.g., environmental monitoring, sterility assurance).  
6. **Post‑Market Surveillance (시판후조사) plan** – align with MFDS post‑market requirements (see 「의료기기법 시행규칙」제48조의3, not listed in excerpt but part of the regulatory framework).  

---

### 5. Risk Controls Mapping (KGMP ↔ ISO 14971)

| KGMP Control Requirement | Corresponding ISO 14971 Risk Control |
|--------------------------|--------------------------------------|
| Process validation & sterilization assurance (고시 제2026‑46호) | **Verification** of sterility & process performance (risk control). |
| Supplier qualification & material traceability | **Supply chain risk mitigation** – establish acceptance criteria, inspections. |
| Environmental monitoring (cleanroom classification) | **Control of contamination risks** – classified as protective measures. |
| CAPA system for non‑conformities | **Corrective actions** to reduce residual risk after occurrence. |
| Personnel training & competency records | **Training controls** reducing human error probability. |

---

### 6. Citations

| Category | Citation Detail |
|----------|-----------------|
| Framework references (no “verify” caveat) | 「의료기기법」제28조·제28조의2~4; 「의료기기법 시행규칙」제48조~제48조의4; ISO 14971. |
| Instance identifiers (directly from source) | 고시 제2026‑46호 (KGMP 기준, 2026‑07‑01 일부개정) <br> 고시 제2026‑47호 (기관·심사원 지정, 신설) <br> 총리령 제2127호 (2026‑07‑01 시행) <br> 대통령령 제36445호 (의료기기법 시행령). |
| Not found – requires verification | Specific MFDS article numbers for labeling (§23) and post‑market surveillance (§48조의3) are not listed in the provided excerpts; verify separately. |

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason & Required Action |
|--------|--------------------------|
| **Unconfirmed device grade** | Senior RA must validate the grade before any submission pathway is selected. |
| **Absence of GMP audit report** | Project lead should commission an audit; cannot proceed to MFDS filing without this core evidence. |
| **Incomplete QMS documentation** | QA manager to supply missing SOPs/CAPA records within 5 business days; otherwise the dossier will be rejected on completeness grounds. |
| **Missing Korean labeling/IFU** | Marketing & Regulatory must produce Korean language versions; escalation to Legal for compliance check if language issues arise. |
| **Risk Management File not prepared** | Risk Management lead to deliver ISO 14971 file; required for 3등급·4등급 devices and advisable for all grades. |
| **Any discrepancy between checklist items and attached files** | Immediate pause of submission; RA manager to perform a “document‑match” audit before resubmission. |

---

### 8. Peer Review Prompt  

*Please review this assessment – focus on (1) whether the identified documentation gaps fully reflect the obligations introduced by 고시 제2026‑46호 and 고시 제2026‑47호, (2) any additional Korean‐specific evidence that may be required for a 3등급 or 4등급 device (e.g., local clinical data), and (3) the completeness of the risk‑control mapping against ISO 14971.*  

--- 

*End of draft.*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [ ] Match correct
- [ ] Evidence supported
- [ ] Source cited
- [x] No hallucination
- [ ] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)
- [ ] KB source error propagated (원본 오류, #144)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1051643482212217538`

> > 최종 갱신: 2026-07-13 (주간모니터 #8 — KGMP 적합성인정 제도 개편, 2026-07-01 시행 반영) > 근거: https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287877&type=HTML (의료기기법 시행규칙, 총리령 제2127호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=law&MST=287221&type=HTML (의료기기법 시행령, 대통령령 제36445호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=admrul&ID=2100000281580&type=HTML (고시 제2026-46호) | https://www.law.go.kr/DRF/lawService.do?OC=<OC>&target=admrul&ID=2100000281582&type=HTML (고시 제2026-47호, 신설) # 국내 MFDS - GMP 심사자료

2. Chunk `528323066343451536`

> ## 핵심 문서 (2026-07-01 개편 후 체계) - 「의료기기법」제28조·제28조의2~4 (적합성인정·심사원·기관지정 근거, 개정 법률 제21263호 2025-12-30 공포) - 「의료기기법 시행규칙」제48조~48조의4 (신청·갱신·심사원·취소사유, 총리령 제2127호 2026-07-01 시행) - 「의료기기 제조 및 품질관리 기준」 (식약처 고시 제2026-46호, 2026-07-01 일부개정 — GMP 심사기준만 존치) - 「의료기기 제조 및 품질관리 관련 기관 지정 등에 관한 규정」 (식약처 고시 제2026-47호, 2026-07-01 제정·신규 — 심사기관·심사원·교육기관 지정) - KGMP 심사 신청서 양식 및 제출서류 체크리스트 (신규 서식: 별지 제38호의4·39·40호)
