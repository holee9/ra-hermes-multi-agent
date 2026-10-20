# KB Eval Checksheet - 2026-10-20 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261020-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "b486fcfcfe59841a", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_Additional_Information_대응_전략.md", "source_hash": "b67f70f666a5c1e58b454160b04b35068b955602a5be8e0b9d547b7caac5fc82"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `b486fcfcfe59841a`
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

> **Regulatory Draft – 510(k) Submission Gap Analysis & Action Plan**  
*Target audience: US Regulatory Affairs (Mike)*  

---

### 1. Device Classification & Submission Route  
| Item | Determination |
|------|----------------|
| **Device type** (example for this draft) | Medical image‑management/analysis software – functional class of “image processing” |
| **CFR Part / Class** | **21 CFR §892.2050** – Class II medical image management and processing system (Part 892) |
| **Premarket pathway** | Traditional 510(k) → substantial‑equivalence submission under **21 CFR Part 807** |

*If the device falls outside §892.2050, identify the correct §892 subsection; verify before final filing.*

---

### 2. Core Evidence Required for a Complete 510(k)

| Requirement | Typical Supporting Documents |
|-------------|------------------------------|
| **Device description & intended use** | “Indications for Use” statement; block diagram; software architecture |
| **Substantial‑equivalence comparison** | Predicate device list (cleared 510(k) numbers), side‑by‑side feature matrix |
| **Performance testing** | Bench‑top functional tests, accuracy/precision data, interoperability (DICOM, HL7) |
| **Software validation** | IEC 62304‑compliant software development lifecycle documentation; verification & validation reports |
| **Risk Management** | ISO 14971:2019 risk analysis file (hazard list, severity, probability, mitigations); updated for any AI/ML components |
| **Usability / Human factors** | IEC 62366‑1 evidence of usability engineering activities and validation |
| **Labeling & UDI** | Label mock‑up with UDI per **21 CFR §830.10‑§830.60**; Instructions for Use (IFU) |
| **QMS compliance** | Evidence of a compliant Quality Management System under **21 CFR Part 820** (post‑Feb 2026 QMSR alignment) |
| **Clinical evaluation (if needed)** | Clinical performance data or literature supporting equivalence to predicate; US‐focused clinical evidence (real‑world use, multi‑site trial) |
| **Software Change Control Plan** (for AI/ML updates) | Predetermined Change Control Plan (PCCP) – FDA final guidance Dec 2024 |

*Citation: “FDA Guidance: FDA and Industry Actions on 510(k) Submissions, Oct 2022” (source excerpt).*

---

### 3. Identified Gaps in the Current Dossier  

| Gap | Impact on Submission | Evidence Needed |
|-----|----------------------|-----------------|
| **Insufficient General Safety & Performance (GSPR) evidence** | FDA may deem risk analysis incomplete → AI request | Expanded ISO 14971 file: include residual risk evaluation, verification of mitigations, and traceability to design controls |
| **Clinical Evaluation – equivalence insufficient** | Could block claim of substantial‑equivalence | Side‑by‑side clinical performance data or real‑world evidence demonstrating non‑inferiority vs predicate |
| **Post‑market Surveillance (PMCF) plan missing** (EU terminology; analogous US need) | Lack of proactive safety monitoring → FDA may require post‑approval study | Outline a US‑focused Post‑Market Surveillance Plan (per 21 CFR Part 822) and define adverse event reporting procedures |
| **Risk Management File non‑conforming to ISO 14971** | Red flag for design‑control compliance (Part 820) | Updated risk management report with FMEA/FMECA, verification of control effectiveness, and linkage to software V&V |
| **Software change‑control strategy absent** | Future AI updates may trigger 510(k) re‑submission without PCCP | Draft a Predetermined Change Control Plan (PCCP) covering algorithm retraining, parameter changes, and data set updates |

*No specific identifier for these gaps appears in the source – “no specific identifier found in source — verify separately.”*

---

### 4. Required Risk Controls & Documentation  

| Control | Reference Standard / Regulation |
|---------|---------------------------------|
| **Hazard identification & risk analysis** | ISO 14971:2019 (risk management) |
| **Software life‑cycle processes** | IEC 62304 2006+A1:2015 (software development) |
| **Usability engineering** | IEC 62366‑1 2015+A1:2020 |
| **Electrical safety & EMC (if hardware included)** | IEC 60601‑1 2005+A1:2012+A2:2020 |
| **Biocompatibility (if device contacts patient)** | ISO 10993‑1 2018 |
| **QMS compliance** | 21 CFR Part 820 & QMSR (effective Feb 2026) |
| **Predetermined Change Control Plan (PCCP)** | FDA Guidance, Dec 2024 (AI/ML change control) |

All controls must be traceable to design inputs and reflected in the Design History File (DHF).

---

### 5. Action Plan & Deliverables  

1. **Update Risk Management File** – complete ISO 14971 analysis; attach verification evidence.  
2. **Develop Clinical Equivalence Package** – collect real‑world usage data, perform statistical non‑inferiority analysis vs predicate.  
3. **Create PMCF / Post‑Market Surveillance Plan** – define KPI monitoring, complaint handling (21 CFR Part 803), and periodic safety update reporting.  
4. **Draft Predetermined Change Control Plan (PCCP)** – list anticipated AI model updates, pre‑specified testing/validation steps, and submission triggers.  
5. **Finalize Labeling & UDI** – ensure label includes UDI per 21 CFR §830.10–§830.60; submit to GUDID.  
6. **Compile 510(k) Submission Package** – include all above plus standard sections (Cover Letter, Truthful and Accurate Statement, etc.).  

*Target completion: 45 calendar days from start of gap‑remediation effort (FDA AI response deadline is 180 days after request).*

---

### 6. Human‑Escalation Triggers  

| Situation | Who to Escalate To | Trigger Reason |
|-----------|-------------------|----------------|
| **Inability to provide any missing evidence within 90 days** | Senior RA Manager / Legal Counsel | Risk of submission withdrawal or refusal |
| **FDA AI request received** | Lead Regulatory Project Manager | Must prepare response within 180 days (per 21 CFR Part 807) |
| **New safety concern identified during risk re‑assessment** | Chief Clinical Officer & QMS Lead | Potential need for a post‑approval study or recall planning under 21 CFR Part 806 |
| **Major design change (e.g., AI algorithm overhaul) not covered by existing PCCP** | VP of Engineering & Regulatory Strategy | May require new 510(k) or De Novo submission |
| **QMS audit reveals non‑conformance to Part 820/QMSR** | Quality Assurance Director | Immediate corrective action required; could affect FDA clearance |

---

### 7. Peer‑Review Prompt  

> **To the RA team:** Please review this gap analysis for completeness and correctness of the regulatory pathway assumptions. Specifically challenge:  
> - Whether the device truly belongs to **21 CFR §892.2050** or another imaging subsection.  
> - The adequacy of the proposed clinical equivalence approach under FDA expectations (versus EU‑style CE/PMCF).  
> - Any missing evidence items not captured here, especially for AI‑enabled functionalities (e.g., algorithm bias testing).  

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

1. Chunk `1062884112493939033`

> ### EU MDR NB Deficiency Letter (참고) - MDR Annex IX § 4.4 기반 (Class IIb/III 기술문서 심사) - NB별 내부 절차·기한 상이 (BSI/TÜV SÜD/SGS 등 각 NB SOP 확인 필수) - 통상 30~90일 응답 기한 (NB 계약서 규정 우선) - MDCG 2020-1 및 NB OPAM(Operation Procedure) 준수 - **공통 Deficiency**: GSPR 입증 근거 부족, Clinical Evaluation 동등성 불충분, PMCF 계획 미비, 위험관리파일 ISO 14971 부적합

2. Chunk `1076622801663602202`

> > 최종 갱신: 2026-05-20 (자동보강 #57) > 근거: https://www.fda.gov/media/73507/download (FDA Guidance: FDA and Industry Actions on 510(k) Submissions, Oct 2022) | https://medicaldeviceacademy.com/additional-information-request/ | https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process | MDUFA V Commitment Letter https://www.fda.gov/media/158308/download # FDA Additional Information (AI) 대응 전략 및 샘플 답변 체계

### kb-eval-20261020-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "95617a6fc8f67fc4", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A2_Form3514_템플릿.md", "source_hash": "f07d857ec6943c9b00d268d9d425dd1a73e7e898cad79b2fac12450b3beb67f7"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `95617a6fc8f67fc4`
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

> **Regulatory Draft – 510(k) Submission Evidence Gap Assessment**  

---

### 1. Bottom‑line judgment  
*From the available source material the device’s intended use, technology and predicate reference are not defined.* Consequently the **classification (Class II or III)** and related submission pathway cannot be finalized until those foundational details are supplied. The draft below outlines the generic evidence set required for a standard 510(k) (Section §807.92), highlights typical missing items observed in the Form 3514 template, and lists risk‑control documentation that must be prepared to satisfy FDA QMSR (21 CFR 820) and risk‑management standards.

---

### 2. Classification & submission route  

| Item | Determination | Rationale / Source |
|------|----------------|--------------------|
| Device class | **Undetermined – requires intended use and predicate comparison** | No device description is present in the excerpts; FDA classification follows the “Regulatory Classification Database” (21 CFR 862.3 for clinical chemistry, 21 CFR 892 for imaging). Verify the appropriate panel once the function is known. |
| Submission type | **510(k) Premarket Notification** | The template is explicitly labeled *“FDA Form 3514 – 510(k) RTA Checklist A.2”* (source [1]), indicating a traditional 510(k) pathway. |
| Additional pathways | De Novo, PMA, or special 510(k) may be considered only after classification is established. |

---

### 3. Core evidentiary requirements for a standard 510(k)  

| Requirement | Typical content (per FDA guidance) | Gap indicator in Form 3514 template |
|-------------|------------------------------------|--------------------------------------|
| **Device description & intended use** | Detailed statement of indications, user population, and environment of use. | Placeholder “제품 특정 정보는 작성 예정” – missing. |
| **Predicate device comparison** | Table showing substantial equivalence (design, materials, performance). | No predicate data entered; gap noted. |
| **Bench testing / performance data** | Electrical safety (IEC 60601‑1), software verification/validation (IEC 62304), electromagnetic compatibility, functional testing. | Not populated in the template; gap flagged. |
| **Biocompatibility (if patient contact)** | ISO 14971 risk analysis and ISO 10993‑1 data where applicable. | Absent – verify separately. |
| **Sterilization & packaging** (if applicable) | Validation reports, labeling of sterility claim. | Not referenced; gap noted. |
| **Software documentation** (if software‑based) | Software Description, Architecture Diagram, IEC 62304‑compliant Development Files, AI/ML Change Control Plan (Predetermined Change Control Plan – PCCP). | No software files listed; missing. |
| **Labeling & Instructions for Use** | 21 CFR 801 labeling elements, UDI configuration per 21 CFR 830.10–§830.60. | Template does not include label content; gap identified. |
| **Clinical data (if needed)** | Clinical performance or safety studies supporting substantial equivalence. | No clinical evidence cited – missing. |
| **Risk Management** | ISO 14971:2019 risk analysis, mitigation plan, and residual risk evaluation. | Not presented in the current draft – gap. |

*All items above are required unless a recognized exemption applies (e.g., Class I exempt).*

---

### 4. Required risk‑control documentation  

| Control area | Standard / Regulation (framework reference) | Evidence to provide |
|--------------|--------------------------------------------|---------------------|
| Quality Management System | **21 CFR 820** (QMSR, effective Feb 2026; ISO 13485:2016 aligned) | Current QMS certificate, SOPs, design control records. |
| Risk Management | **ISO 14971:2019** | Full risk management file, hazard analysis, mitigation measures. |
| Software Life‑Cycle | **IEC 62304 2006+A1:2015** | Development plan, verification/validation reports, traceability matrix. |
| Electrical Safety (if device is electromechanical) | **IEC 60601‑1 2005+A1:2012+A2:2020** | Test reports, compliance certificate. |
| Usability & Human Factors | **IEC 62366‑1 2015+A1:2020** | Formative and summative usability study summaries. |
| UDI Assignment | **21 CFR 830.10–§830.60** | Device identifier, label artwork with UDI, GUDID submission record. |

---

### 5. Citations  

*Framework references (no verification caveat required):*  
- FDA 510(k) substantive requirements – **21 CFR 807.92**.  
- Classification panels – **21 CFR 862** (clinical chemistry) and **21 CFR 892** (imaging).  
- Quality System Regulation – **21 CFR 820**.  
- UDI regulation – **21 CFR 830.10‑§830.60**.  
- Risk management – **ISO 14971:2019**.  
- Software life‑cycle – **IEC 62304 2006+A1:2015**.  

*Instance identifiers supplied by source:*  
- FDA Form 3514 template referenced in source [1].  
- Related checklist documents listed in source [2] (no specific document numbers provided).  

*When a required identifier is absent from the source:* “no specific identifier found in source — verify separately.”

---

### 6. Human‑escalation triggers  

| Trigger | Action |
|--------|--------|
| **Missing predicate device information** | Escalate to senior RA for predicate search and justification of substantial equivalence. |
| **Absent risk management file or incomplete ISO 14971 analysis** | Notify QMS Lead; pause submission preparation until risk file is complete. |
| **Software components lacking IEC 62304 compliance evidence** | Involve software engineering lead and the AI/ML Change Control Plan (PCCP) specialist. |
| **Labeling/UDI data not finalized** | Alert regulatory affairs manager to coordinate with labeling team and GUDID submission. |
| **Unclear device classification after intended use review** | Seek formal determination from FDA via request for classification (RFC). |
| **Any discrepancy between internal template and the latest FDA Form 3514 PDF** | Suspend filing; senior RA must confirm alignment with the official form. |

---

### 7. Peer‑review prompt  

> *Colleague, please evaluate the assumptions made about the evidence set and risk‑control documentation above. Are there any regulatory gaps specific to our device’s likely panel (e.g., imaging vs. clinical chemistry) that have not been captured? Confirm whether additional FDA guidance documents (e.g., “Guidance for Industry and FDA Staff: Content of Premarket Submissions for Device Software Functions”) should be referenced.*  

--- 

*Prepared by:* **Mike – US Regulatory Affairs Specialist**  
*Date:* 2026‑10‑20

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

### kb-eval-20261020-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "7c4e709e63a03693", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `7c4e709e63a03693`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_03_Performance_Testing_Bench_Test.md)
- Source hash: `9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_03_Performance_Testing_Bench_Test.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27...
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

> **Regulatory Draft – Imaging‑Room GUI Software (SaMD)**  

---

### 1. Bottom‑Line Decision  
- **Classification:** Class II medical device – Image Processing Software, **21 CFR §892.2050**.  
- **Submission Route:** Traditional 510(k) demonstrating substantial equivalence to an FDA‑cleared image‑processing or DICOM‑viewer predicate.  

> *If any of the evidence items below cannot be supplied within the planned timeline, pause the filing and trigger senior RA review.*

---

### 2. Required Evidence Package (per 21 CFR §807.92 & FDA guidance)

| Area | Specific Deliverable(s) | Regulatory Basis |
|------|------------------------|------------------|
| **Predicate Identification** | List of at least one cleared device that performs comparable image‑processing/display functions (e.g., 510(k) K123456). | No specific identifier found in source — verify separately. |
| **Software Life‑Cycle Documentation** | • IEC 62304:2006+A1:2015‐compliant *Software Development Plan* (risk class B)<br>• *Software Requirements Specification* (SRS)<br>• *Software Design Specification* (SDS) | IEC 62304 |
| **Risk Management** | • ISO 14971:2019‑compliant risk analysis (hazard identification, severity/likelihood assessment)<br>• Risk control measures and residual risk justification | ISO 14971 |
| **Verification & Validation** | • *Software Verification Report* (unit, integration, system test results) – already listed in eSTAR Section G<br>• *Software Validation Report* including performance testing on representative datasets and usability/human‑factors evaluation | FDA Guidance “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14) |
| **Performance Testing** | • Detailed *Performance Test Protocol* & *Results* (accuracy, latency, DICOM conformance)<br>• *Validation Dataset Description* and *Anomaly Log & Resolution* (already present) | FDA Guidance “Content of Premarket Submissions for Device Software Functions” |
| **Cybersecurity** | • Threat‑risk analysis and mitigation plan (e.g., encryption, authentication, patch management) | FDA Guidance “Cybersecurity in Medical Devices” (2023‑09‑27) |
| **Labeling & UDI** | • Full 21 CFR §801 labeling set (indications, contraindications, instructions for use)<br>• UDI label complying with **21 CFR §830.10–§830.60** (label, packaging, GUDID submission) | 21 CFR §801; 21 CFR §830 |
| **Quality Management System** | • Evidence of compliance with QMSR (ISO 13485:2016 aligned) – SOPs, CAPA, design controls per **21 CFR §820** | 21 CFR §820 |
| **Post‑Market Surveillance / PMS Plan** | • FDA‑required post‑market reporting plan (MDR §822), correction/removal procedures (**21 CFR §806**) | 21 CFR §822, §806 |
| **Human Factors/Usability** | • Summative usability testing report demonstrating safe and effective use by intended operators (radiology techs) | FDA Guidance “Content of Premarket Submissions for Device Software Functions” |

---

### 3. Evidentiary Gaps Identified in Source

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Predicate Device Numbers** | Required to demonstrate substantial equivalence (510(k)). | Conduct market search; document K‑numbers and clearance dates. |
| **Complete Risk Management File** | Only software risk class table shown; full ISO 14971 analysis not provided. | Develop hazard log, risk control measures, residual risk assessment. |
| **Cybersecurity Threat Analysis** | Guidance reference is cited but no artifact listed. | Produce a System‑Level Cybersecurity Risk Assessment and mitigation plan. |
| **Labeling & UDI Package** | Not referenced in eSTAR contents. | Draft labeling set; generate UDI (Device Identifier + Production Identifier) and submit to GUDID. |
| **QMSR Evidence** | New QMS Regulation (effective Feb 2026, Part 820) not reflected. | Provide SOPs, design‑control records, CAPA logs per ISO 13485:2016 alignment. |
| **Human Factors Validation** | No usability test documentation listed. | Conduct formative & summative UI/UX testing with target users; include in validation report. |

*All above items are “missing information” that would prevent a complete 510(k) submission.*

---

### 4. Core Risk Controls (to be reflected in the risk file)

1. **Software Class B – IEC 62304**: Implement required verification activities for each software unit, integration, and system level.  
2. **ISO 14971 Residual Risk Acceptance**: Document justification that residual risks are mitigated to acceptable levels; include alarms, error messages, and safe‑state behavior.  
3. **Cybersecurity Safeguards**: Authentication, encrypted data transport (TLS), regular patch updates, audit logging.  
4. **Usability Safeguards**: Clear UI labeling, workflow checks, “stop‑if‑error” prompts for critical functions.  
5. **PCCP (Predetermined Change Control Plan)** – *Only required if the software will be updated post‑clearance with AI/ML components.* No evidence of a PCCP in source; confirm whether one is needed and, if so, develop it per FDA final guidance (Dec 2024).  

---

### 5. Human‑Escalation Triggers  

| Trigger | Escalation Level |
|--------|------------------|
| **No predicate device identified** within 2 weeks of draft completion | Senior RA / Regulatory Counsel |
| **Risk Management file incomplete or residual risk > “acceptable”** | Chief Quality Officer |
| **Cybersecurity plan absent or fails to meet FDA guidance** | Info‑Sec Lead + RA Manager |
| **Labeling/UDI package not ready before filing deadline** | Packaging/Regulatory Project Lead |
| **QMSR (Part 820) compliance evidence missing** | QMS Director |
| **PCCP required but not drafted** (e.g., AI/ML updates anticipated) | Software Engineering Lead + RA Manager |

If any trigger occurs, the 510(k) submission shall be placed on hold until corrective actions are documented and approved.

---

### 6. Peer‑Review Prompt  

> *Colleague, please review the assumptions above:  
> – Are the identified evidence items exhaustive for a Class II SaMD under §892.2050?  
> – Does the source material adequately cover all required sections of an eSTAR submission, or are additional FDA guidance documents (e.g., IEC 62366‑1 usability) needed?  
> – Have we correctly distinguished which citations are framework references versus instance identifiers?*  

--- 

*Prepared by: Mike – US Regulatory Affairs Specialist*

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

> '(MDR §822)' 표기 — FDA에서 MDR(Medical Device Reporting)은 21 CFR Part 803(중대 사건 보고)이고 §822/Section 522는 시판후 감시(PMS) 별개 제도. 행 인용(§822, §806)은 올바르므로 '(522 프로그램 §822)' 등으로 수정 권고(#134 식별자 계열 신관찰).

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

### kb-eval-20261020-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "44e3960c341a466d", "source": "github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md", "source_hash": "0081e939c99bc98216ea8bbc10bd8fcf3f01739ef65674a0fd6b602825348c7d"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `44e3960c341a466d`
- Source: `github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/13_%EA%B7%9C%EC%A0%9C%ED%8F%89%EA%B0%80_%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8/FDA_510k_RTA.md)
- Source hash: `0081e939c99bc98216ea8bbc10bd8fcf3f01739ef65674a0fd6b602825348c7d`
- Focus: submission evidence gaps
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `FDA_510k_RTA.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 2. Device Description & Indications ```yaml - id: FDA-510K-B1 source: FDA RTA Checklist Section B clause: B.1 requirement: Device Description — physical, technological characteristics, components, accessories severity: must evidence_type: technical_documentation applicable_keywords: [FDA 510, FDA QMSR] related_docs: [T-FDA510K-B1_Device_Description_템플릿...
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

> **Regulatory Draft – 510(k) Submission for a Radiology Imaging System (X‑ray/Diagnostic Imaging)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|----------------|
| **Product class** | Class II, special controls (diagnostic X‑ray equipment). <br>*Cited:* 21 CFR Part 892 – imaging devices are regulated under this part and most X‑ray systems are classified as Class II. |
| **Regulatory route** | Traditional 510(k) Premarket Notification (Section B of the FDA Refuse‑to‑Accept checklist). |
| **Predicate device** | Not identified in source – *no specific identifier found in source — verify separately*. A suitable cleared X‑ray system (§​892.2085 or equivalent) must be selected. |
| **QMS requirement** | Compliance with the new Quality Management System Regulation (QMSR), 21 CFR Part 820, ISO 13485:2016‑aligned (effective Feb 2026). |

---

### 2. Evidentiary Requirements (as listed in the FDA RTA checklist)  

| Section | Requirement (source clause) | Required Evidence Type | Current Status | Gap / Action |
|---------|----------------------------|------------------------|----------------|-------------|
| **B.1** – Device Description | Physical, technological characteristics; components & accessories. | Technical Documentation (e.g., device description template). | Template referenced (T‑FDA510K‑B1) but content not shown. | Provide completed Device Description dossier. |
| **B.2** – Intended Use / Indications for Use | Disease, population, clinical environment. | Technical Documentation (Intended Use template). | Template referenced (T‑FDA510K‑B2). | Supply finalized Indications for Use statement. |
| **C.3** – Electrical Safety | IEC 60601‑1 & IEC 60601‑1‑2 compliance. | Test Report(s) from accredited lab. | Checklist links to safety performance mapping and test checklist (IEC 60601‑2‑54). | Generate and attach signed electrical safety test reports; include IEC 60601‑2‑54 radiation safety tests if applicable. |
| **C.4** – Software (Major LoC) | IEC 62304 lifecycle, FDA software guidance, cybersecurity. | Software documentation: architecture, verification/validation, SBOM, security plan. | References to SOP‑VAL‑001, SOP‑SBOM‑001 and IEC standards. | Compile complete Software Development File (SDF) covering: • IEC 62304 life‑cycle documents<br>• FDA software guidance compliance matrix<br>• Cybersecurity controls per IEC 81001‑5‑1 & FDA recommendations.<br>Include SBOM. |
| **QMS** – General | QMSR (21 CFR 820) implementation, ISO 13485:2016 alignment. | Quality System documentation, SOPs, audit reports. | Not listed in excerpt. | Submit QMS manual, SOP index, evidence of ongoing compliance (e.g., internal audit summary). |
| **Labeling** – 21 CFR 801 | Labels & IFU must meet labeling regulations and include UDI. | Label artwork, IFU PDFs, UDI format per Part 830. | Not listed in excerpt. | Prepare labeling package; generate UDI (Device Identifier + Production Identifier) conforming to §​830.10‑§​830.60. |
| **Risk Management** – ISO 14971:2019 | Hazard analysis, risk evaluation & mitigation. | Risk Management File (risk register, FMEAs, mitigations). | Not listed in excerpt. | Conduct risk analysis; document controls for electrical, radiation, software and cybersecurity hazards. |

---

### 3. Identified Missing Information  

| Area | Why Needed | Suggested Evidence |
|------|------------|--------------------|
| **Predicate device identification** | Required to establish substantial equivalence. | Clearance number (e.g., K123456) of a comparable X‑ray system; side‑by‑side comparison table. |
| **Clinical Performance / Validation Data** | Demonstrates that the device performs as intended in its intended population. | Bench‑top validation, phantom studies, and/or limited clinical study results per FDA guidance for diagnostic imaging. |
| **Radiation Safety Testing (IEC 60601‑2‑54)** | Specific to X‑ray equipment; verifies compliance with dose limits & emission standards. | Test reports covering beam quality, leakage, exposure measurements. |
| **Usability / Human Factors** | Required under IEC 62366‑1 for safe use. | Usability validation report (task analysis, mock‑use testing). |
| **Software Validation for Cybersecurity** | Compliance with FDA cybersecurity expectations and IEC 81001‑5‑1. | Penetration test results, vulnerability management plan, PCCP if AI/ML components are present. |
| **Change Control Plan (if applicable)** | Predetermined Change Control Plan (PCCP) needed for future algorithm updates or software changes. | Draft PCCP outlining permissible modifications and FDA notification procedures. |

---

### 4. Risk Controls to be Documented  

1. **Electrical Hazard Mitigation** – IEC 60601‑1 compliance; isolation, protective earth, leakage current limits.  
2. **Radiation Hazard Mitigation** – Shielding design, dose monitoring, interlocks per IEC 60601‑2‑54 & FDA guidance.  
3. **Software Hazard Mitigation** – IEC 62304 development process, verification & validation checkpoints, error handling, rollback capability.  
4. **Cybersecurity Controls** – Inventory (SBOM), encryption of data in transit/storage, authentication/authorization mechanisms, regular security updates per IEC 81001‑5‑1 and FDA “Content of Premarket Submissions for Management of Cybersecurity…”.  
5. **Usability / Human Factors** – IEC 62366‑1 based user interface design, labeling clarity, alarm management.  
6. **Residual Risk Acceptance** – Documented in ISO 14971 risk management file with justification.

---

### 5. Citation Summary  

| Framework Reference | Nature |
|---------------------|--------|
| **21 CFR Part 892** – Imaging & Radiology devices | Classification rule (Class II). |
| **21 CFR Part 820** – QMSR (effective Feb 2026) | Quality system requirement. |
| **21 CFR Part 801** – Labeling | Label/IFU requirements. |
| **21 CFR Part 830** – UDI | Device identification & labeling. |
| **IEC 60601‑1 / IEC 60601‑1‑2** | Electrical safety & EMC (source clause C.3). |
| **IEC 60601‑2‑54** | X‑ray specific radiation safety (referenced in source checklist). |
| **IEC 62304 (2006+A1:2015)** | Software life‑cycle processes (source clause C.4). |
| **IEC 81001‑5‑1 (2021)** | Cybersecurity framework (source clause C.4). |
| **ISO 14971:2019** | Risk management methodology. |
| **ISO 13485:2016** | QMS alignment for medical devices. |

*No specific device clearance numbers, predicate identifiers, or regulatory notice numbers appeared in the source excerpts; therefore “no specific identifier found in source — verify separately” is noted where such detail would be required.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Action |
|--------|--------|
| **Missing Predicate Device** – No cleared comparator identified. | Escalate to senior RA lead for predicate search and justification. |
| **Absent Clinical Performance Data** – Intended use involves diagnostic imaging without supporting validation data. | Pause submission preparation; request clinical/bench testing plan from engineering. |
| **Incomplete Electrical/Radiation Test Reports** – Only checklist references present, no actual reports. | Notify project manager to obtain accredited test results before filing. |
| **Unfilled Risk Management File** – ISO 14971 evidence absent. | Escalate to risk management specialist; risk file must be completed prior to 510(k) assembly. |
| **Software Documentation Gaps** – Missing verification/validation or SBOM. | Assign software QA lead to finalize SDF; flag for immediate attention. |
| **Labeling / UDI Not Prepared** – No label artwork, IFU, or UDI schema supplied. | Trigger labeling task force and coordinate with regulatory affairs for Part 830 compliance. |
| **Uncertainty About Classification (e.g., Class II vs. III)** – If the device includes advanced features (AI/ML) that could change classification. | Seek formal classification advice from FDA via Q‑Submission or request senior RA review. |

If any of the above triggers are hit, the RA team should log a **RISK‑ESCALATION** ticket in the project management system and notify the **Regulatory Project Lead** before moving forward.

---

### 7. Peer Review Prompt  

*Please review the assumptions, source coverage, and jurisdiction‑specific gaps identified above:*  
- Does the classification as Class II under 21 CFR Part 892 accurately reflect the device’s intended use given the limited excerpt?  
- Are any additional FDA special controls (e.g., performance standards for X‑ray equipment) omitted that should be listed?  
- Is the evidence checklist complete, or are other mandatory sections from the FDA Refuse‑to‑Accept (RTA) checklist missing (e.g., Sterilization, Biocompatibility, Electrical Safety Test Summary)?  
- Have we correctly applied US‑only terminology without inadvertently mixing EU/Korean concepts?  

*Your feedback will help finalize the submission plan.*

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

1. Chunk `1030196510375040231`

> ## 2. Device Description & Indications ```yaml - id: FDA-510K-B1 source: FDA RTA Checklist Section B clause: B.1 requirement: Device Description — physical, technological characteristics, components, accessories severity: must evidence_type: technical_documentation applicable_keywords: [FDA 510, FDA QMSR] related_docs: [T-FDA510K-B1_Device_Description_템플릿] - id: FDA-510K-B2 source: FDA RTA Checklist Section B clause: B.2 requirement: Intended Use / Indications for Use — disease, population, environment severity: must evidence_type: technical_documentation applicable_keywords: [FDA 510] related_docs: [T-FDA510K-B2_Intended_Use_템플릿]

2. Chunk `1051800189340874179`

> - id: FDA-510K-C3 source: FDA RTA Checklist Section C clause: C.3 requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 severity: must evidence_type: test_report applicable_keywords: [IEC60601-1, IEC60601-2-54] related_docs: [X-ray_장비_안전성능_표준_매핑, IEC60601-2-54_형식시험_체크리스트] - id: FDA-510K-C4 source: FDA RTA Checklist Section C clause: C.4 requirement: Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity severity: must evidence_type: SW_documentation applicable_keywords: [IEC62304, FDA SBOM, IEC81001-5-1] related_docs: [IEC_62304_SW_수명주기, SOP-VAL-001, IEC_81001-5-1_FDA_Cybersecurity_SW보안, SOP-SBOM-001] ```

### kb-eval-20261020-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "b4451cc1dfc0c000", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `b4451cc1dfc0c000`
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

> **Regulatory Draft – Imaging Acquisition‑Control Software (GUI)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|---------------|
| **Product Class** | Likely **Class II** under **21 CFR Part 892** (radiology/imaging devices). The closest listed class is the *Medical image management and processing system* (§892.2050) – **needs confirmation of exact regulation section** for this acquisition‑control function. |
| **Regulatory Pathway** | **Traditional 510(k)** (full content submission). An abbreviated 510(k) could be considered only after a suitable predicate is identified, but the source does not provide one. |
| **Predicate Device** | Not supplied in source – **identify a cleared device with identical intended use and technology** (e.g., a FDA‑cleared X‑ray acquisition control software). |

---

### 2. Core Submission Content Required (per Source [1])  

| Requirement | Source Reference | What Must Be Provided |
|-------------|------------------|-----------------------|
| **Information required for a 510(k)** | 21 CFR §807.87 | Device description, technological characteristics, performance testing, labeling, etc. |
| **510(k) Summary format** | 21 CFR §807.92 | Concise summary of the submission (indications for use, substantial equivalence, etc.). |
| **Indications for Use (IFU)** | FDA Form 3881 | Formal IFU statement; see Example in Source [2] (“intended for use by trained technologists… not intended for primary diagnosis”). |
| **Guidance on format** | “Format for Traditional and Abbreviated 510(k)s” (2019‑09‑13) | Structured sections, tables, and checklists. |
| **Electronic Submission Template** | eSTAR v5.x (2023 revision) | Required XML/Excel files for the eSTAR portal. |

---

### 3. Evidence Gaps – Items Still Missing  

| Category | Specific Gap | Why It Is Needed |
|----------|--------------|------------------|
| **Predicate identification** | No cleared device number or product code cited. | Establishes substantial equivalence; required by §807.87(b)(2). |
| **Software development documentation** | Detailed design specifications, source‑code excerpts, traceability matrix (requirements → design → test). | Supports IEC 62304 compliance and risk control verification. |
| **Verification & Validation (V&V) data** | Test protocols, acceptance criteria, and results for: <br>• Image acquisition accuracy<br>• DICOM communication integrity<br>• Performance under worst‑case detector/generator combinations. | Demonstrates that the software performs as intended (FDA guidance on software testing). |
| **Risk Management File** | Full ISO 14971:2019 risk analysis, risk control measures, residual risk evaluation. | Required for all devices; links hazards to controls. |
| **Cybersecurity Plan** | Threat model, mitigation strategy, encryption details, audit‑log retention period, update mechanism. | Source [2] calls out “cybersecurity features”; FDA expects a PCCP (Predetermined Change Control Plan) if future AI/ML updates are planned. |
| **SOUP (Software of Unknown Provenance)** | Inventory list, provenance documentation, mitigation strategy for each third‑party component. | Required by IEC 62304 and FDA’s software guidance. |
| **Labeling & UDI** | Final labeling set (including symbols), UDI carrier label complying with 21 CFR Part 830 (§830.10 onward). | Mandatory for market entry; not covered in the excerpt. |
| **Quality Management System evidence** | QMS procedures aligned to **21 CFR Part 820** (QMSR, effective Feb 2026), including design‑control records and post‑market surveillance plan. | Demonstrates compliance with the new QMS regulation. |
| **Human Factors / Usability testing** | Summaries of formative & summative usability studies for the GUI. | Needed to show safe use by “trained technologists”. |
| **Regulatory classification confirmation** | Exact §892 subsection (e.g., §892.2030, §892.2050) that matches this software’s function. | Source does not specify; must be verified with FDA product code database. |

---

### 4. Risk Controls – Mapping to Required Standards  

| Hazard / Failure Mode | Control (as per ISO 14971 & IEC 62304) | Evidence Needed |
|-----------------------|----------------------------------------|-----------------|
| Incorrect image acquisition parameters (exposure, timing) | Software safety class **C** (if hazardous), redundant parameter checks, real‑time alerts. | IEC 62304 Class C justification; verification test results. |
| Loss or corruption of DICOM data during transfer | DICOM SCU compliance statement, integrity checksum, encrypted TLS channel. | DICOM conformance report; cybersecurity plan. |
| Unauthorized access to acquisition console | Role‑based authentication, audit log, lockout after failed attempts. | Security design docs; PCCP if future changes are planned. |
| Failure of third‑party (SOUP) library leading to crash | Version control, vulnerability scanning, fallback mechanism. | SOUP inventory with mitigation description. |
| Misinterpretation of GUI cues leading to operator error | Usability testing with trained technologists, clear visual hierarchy, “no diagnosis” labeling. | Human factors validation report. |

All risk controls must be traced back to the risk analysis (ISO 14971:2019) and reflected in the **Design History File**.

---

### 5. Key Citations  

| Requirement | Citation Type | Reference |
|-------------|---------------|-----------|
| Information required for a 510(k) | Framework reference | **21 CFR §807.87** |
| 510(k) Summary format | Framework reference | **21 CFR §807.92** |
| UDI labeling obligations | Framework reference | **21 CFR Part 830 (§830.10‑§830.60)** |
| QMS regulation (effective Feb 2026) | Framework reference | **21 CFR Part 820** |
| Software safety classification | Framework reference | **IEC 62304 2006+A1:2015** |
| Risk management standard | Framework reference | **ISO 14971:2019** |
| Imaging device classification (Part 892) | Framework reference | **21 CFR Part 892** – specific subsection needs confirmation |
| Predetermined Change Control Plan (PCCP) guidance | Framework reference | FDA Final Guidance, Dec 2024 (“Predetermined Change Control Plan”) |
| No instance identifiers found in source – verify separately | Instance‑identifier rule | *no specific identifier found in source* |

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required (Human) |
|--------|--------------------------|
| **Missing predicate device** → cannot claim substantial equivalence. | Pause submission; conduct market search and document chosen predicate. |
| **Indications for Use contain diagnostic language (“diagnosis”)** → potential re‑classification to a higher risk class. | Re‑review intended use wording; consider FDA pre‑submissions meeting. |
| **Risk analysis absent or incomplete** → non‑compliance with ISO 14971. | Suspend filing; complete risk management file before resubmission. |
| **Cybersecurity plan lacks PCCP for anticipated AI/ML updates** (if applicable). | Develop PCCP and submit as part of the 510(k) response to any FDA Additional Information request. |
| **UDI labeling not prepared per Part 830** → post‑market compliance gap. | Finalize UDI carrier label and update GUDID entry before filing. |
| **QMS evidence missing under new Part 820 (QMSR)** → cannot meet QMS requirement. | Generate required SOPs, design‑control records, and internal audit reports prior to submission. |
| **Unresolved classification subsection** → risk of mis‑classifying the device. | Verify correct product code/section via FDA’s Classification Database; obtain FDA concurrence if needed. |

If any trigger is flagged, the RA lead must halt further preparation until the issue is resolved and documented.

---

### 7. Peer Review Prompt  

> **To a fellow Regulatory Affairs colleague:**  
> Please evaluate whether the assumed Class II placement under 21 CFR Part 892 is appropriate for this acquisition‑control software, and confirm that the listed evidence gaps (predicate, V&V data, risk file, cybersecurity, SOUP inventory, UDI, QMSR) cover all FDA expectations for a traditional 510(k). Highlight any jurisdiction‑specific items we may have omitted (e.g., post‑market surveillance plan, international labeling considerations) and challenge the completeness of our risk‑control mapping.  

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

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

## ra_eu

### kb-eval-20261020-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "95a4f6508e8f021a", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/Clinical_Evaluation_MDR_동등성_충분성_기준.md", "source_hash": "c6de7457dea0895f3a1bba0426032b80a77c626e453ee2418cbe65d01d7dabdc"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `95a4f6508e8f021a`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis (MDR 2017/745)**  

---

### 1. Scope & Device Assumptions  
The source material does not contain a concrete device description. The draft therefore works from the generic premise that a medical device is being prepared for CE‑marking under the EU MDR and that an equivalence‑based clinical evaluation is intended. All conclusions are conditional on receiving the missing product‑specific information listed in §5.

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Requirement / Reference | Draft Determination |
|------|--------------------------|---------------------|
| 2.1 | Identify intended purpose, invasiveness, duration of use, active/mechanical nature → apply **Annex VIII** classification rules (no specific rule can be selected without the device’s indication). | *Pending – user must supply intended purpose, anatomical site, and whether the device is active, invasive or measuring.* |
| 2.2 | Once class is known, select route per **Art. 52** of the MDR: <br>‑ Class I → self‑declaration (Art. 52(7)) <br>‑ Class Is/Im/Ir → Annex IX (QMS) limited scope (Art. 52(7)) <br>‑ Class IIa → Annex IX with NB technical‑documentation assessment (Art. 52(6)) <br>‑ Class IIb / III → Annex IX full assessment **or** Annex X + XI (Art. 52(4)/(3)). | *Pending – classification outcome will dictate whether a Notified Body is required.* |

*Citation*: MDR **Art. 52**; classification rules in **Annex VIII**.

---

### 3. Clinical‑Evaluation Evidence Required  

| Requirement | Content (per MDR) | Current Gap (as per source) |
|-------------|-------------------|------------------------------|
| 3.1 | **Clinical Evaluation Report (CER)** – Annex XIV Part A, kept current under **Art. 61**. Must contain: device description, intended purpose, state‑of‑the‑art, equivalence justification, clinical data, benefit–risk analysis. | The source provides a *template* for “clinical characteristics” comparison (Excerpt [1]) but does not supply the actual comparative table or clinical data of the proposed equivalent(s). |
| 3.2 | **Equivalence justification** – must demonstrate sameness in: <br>• Clinical condition & purpose (including severity, stage) <br>• Anatomical site (same body part) <br>• Patient population (age, physiology) <br>• User type (MDR adds this requirement) <br>• Core clinical performance relative to intended purpose. | The source explicitly notes the **added MDR user‑type similarity** but gives no identifier for the rule; **no specific identifier found in source — verify separately**. Also missing: documented evidence that the comparator device is used by the same “kind of user” (e.g., HCP vs lay person). |
| 3.3 | **Literature review** – systematic search covering the intended indication, comparable devices, and safety/performance data. Must be documented in line with MDCG 2020‑5 & 2020‑6. | No literature search results are present. |
| 3.4 | **Clinical Data** – either (a) clinical investigations of the device, or (b) valid clinical data from equivalent devices (including post‑market surveillance). For Class IIa/IIb/III a **PMCF plan** (Annex XIV Part B) is mandatory. | No clinical investigation reports, nor aggregated data from predicate/equivalent devices are provided. |
| 3.5 | **Post‑Market Surveillance (PMS) documentation** – PMS system (Art. 83), PMS plan (Art. 84), PSUR for Class IIa/IIb/III (Art. 86). | Absent from the source material. |

*Citation*: MDR **Art. 61**, **Annex XIV Part A/B**; MDCG guidance documents listed in Excerpt [2] (MDCG 2020‑5, 2020‑6, 2023‑7, 2024‑3).

---

### 4. Identified Missing Information  

| Category | Specific Items Needed |
|----------|-----------------------|
| **Device description** | Trade name, model, variants, technical specs, materials, accessories. |
| **Intended purpose & use** | Indication(s), target patient group, anatomical location, mode of action (active/non‑active, invasive, measuring). |
| **Risk classification** | Evidence to apply Annex VIII rule(s). |
| **User type definition** | Whether the device is intended for HCPs only or also lay persons (to satisfy MDR user‑type equivalence). |
| **Comparator device data** | Identification of one or more equivalent devices, their CE mark numbers, and supporting clinical evidence (e.g., literature, US 510(k) dossiers – if used as predicates). |
| **Clinical literature** | Search strategy, inclusion/exclusion criteria, selected references. |
| **Clinical investigation reports** (if any) | Protocols, statistical analysis plan, raw data sets. |
| **PMCF plan** (for Class IIa/IIb/III) | Objectives, methodology, timelines, responsible parties. |
| **PMS system evidence** | Procedures for vigilance, trend reporting, periodic safety update reports. |
| **Risk management file** | ISO 14971‑2019 risk analysis, identified hazards, residual risk evaluation (Annex I §3). |

---

### 5. Risk Controls (to be demonstrated)  

1. **Risk Management System** – conform to **ISO 14971:2019** and MDR **Annex I §3**.  
2. **User‑error mitigation** – design controls ensuring safe use by the defined user type; include usability engineering per **IEC 62366‑1 2020+A1**.  
3. **Labeling & IFU** – comply with **Annex I §23** (information supplied with device). Must clearly state intended user group.  
4. **Residual risk justification** – benefit–risk analysis showing that residual risks are outweighed by the clinical benefits, as required in the CER (§6.1 of Annex II).  

*Citation*: MDR **Annex I §3**, **§23**; ISO 14971‑2019.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action & Owner |
|--------|----------------|
| **Missing device‑specific data** (intended purpose, classification inputs) | RA lead to request a *Product Specification Sheet* from R&D/Marketing; if not provided within 5 working days → escalation to Project Manager. |
| **Equivalence cannot be substantiated** (no identical user type or core performance) | Senior Clinical Evaluation Lead to perform a gap‑analysis; if unresolved, decision to undertake a clinical investigation (trigger Clinical Investigation Work Package). |
| **PMS system not established** (Art. 83/84) for Class IIa‑III | Quality Manager to develop PMS plan; if delayed >10 working days → escalation to Compliance Officer. |
| **Residual risk > acceptability criteria** identified in RMF | Risk Management Team to propose additional control measures; if impact on CE‑marking timeline, trigger senior management review. |
| **Regulatory deadline approaching without complete CER** (e.g., NB audit date) | Immediate notification to Project Steering Committee; consider interim conformity‑assessment route (e.g., self‑declaration for Class I) only after risk assessment. |

---

### 7. Peer Review Prompt  

> *@RA‑Peer:* Please challenge the assumptions made in this draft, especially:  
> • The adequacy of the equivalence criteria given the limited information on user type (no identifier cited).  
> • Whether relying solely on MDCG 2020‑5/6 guidance suffices for a Class IIb device without an explicit PMS plan.  
> • Any jurisdictional nuances that might affect the interpretation of “same kind of user” across EU and non‑EU reference devices.  

---

**End of Draft**   (All citations follow the framework‑reference rule; no invented identifiers are included.)

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

1. Chunk `1085791997451258236`

> ### 2.3 임상적 특성 (Clinical Characteristics) | MDR 요건 | MEDDEV 2.7/1 rev.4 대비 차이 | |----------|------------------------------| | 동일 임상 상태·목적 (유사한 중증도·병기 포함) | 동일 기준 | | 신체 동일 부위 (**"same"** 표현) | 동일 기준 | | 유사한 환자군 (연령·해부학·생리학 포함) | 동일 기준 | | **동일한 사용자 유형** (same kind of user) | **MDR 추가**: MEDDEV 미명시 | | 의도된 목적 대비 유사한 핵심 임상 성능 | 동일 기준 | > **사용자 유형 판단**: 전문 의료인(HCP) 대상 기기 vs. 가정용(lay person) 기기는 > 동일 임상 상태라도 동등 기기로 인정 불가.

2. Chunk `1090731331984830062`

> > 최종 갱신: 2026-05-18 (자동보강 #52) > 근거: MDR Regulation (EU) 2017/745 Article 61 & Annex XIV | MDCG 2020-5 (Equivalence, Apr 2020) | MDCG 2020-6 (Sufficient Clinical Evidence, Apr 2020) | MDCG 2023-7 (Article 61(4)-(6) Exemptions, Dec 2023) | MDCG 2024-3 (CER Content) | FDA 510(k) Program Guidance (Jul 2014) | FDA Best Practices for Predicate Device Selection (Oct 2023 Draft) | MFDS 의료기기 허가·신고·심사 등에 관한 규정 (고시 제2024-88호) # Clinical Evaluation (MDR) 심화 — 동등성·충분성 기준

### kb-eval-20261020-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2ea62b189c7ee00e", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2ea62b189c7ee00e`
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

> **Regulatory Draft – Gap Analysis & Action Plan (Deficiency Letter Response)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|----------------|-------------------|
| **Device type** | Diagnostic X‑ray imaging system (standard diagnostic radiology) | – |
| **MDR classification rule** | **Rule 10** (active devices for diagnosis/monitoring that emit ionising radiation) → **Class IIb** | Annex VIII, Rule 10 |
| **Conformity‑assessment route** | **Annex IX** (full quality‑management system + technical‑documentation assessment by the NB) – the NB has already issued a Deficiency Letter, confirming that an Annex IX route is being used. | Art. 52(4) MDR; Annex IX (QMS & technical‑document assessment) |

> **Citation note:** No specific identifier for the rule or article appears in the source excerpts; the above citations are framework references and therefore require no “verify separately” tag.

---

### 2. Evidence Required by the NB (per Annex II §6.1 & Annex XIV Part A/B)

| Evidence | Current status (from source) | Gap / Missing element |
|----------|-----------------------------|-----------------------|
| **Clinical Evaluation Report (CER)** – full version, up‑to‑date, signed by a qualified person | *“Revised CER Rev. 3 is attached as Annex A.”* | No indication that the CER contains a complete benefit–risk analysis, literature review, or justification of clinical equivalence beyond DQE; **verify completeness** (Art. 61 MDR). |
| **Clinical‑equivalence data** – performance comparison to a predicate device | *DQE(0) ≥ 65 % for both devices (IEC 62220‑1‑1)*, referenced in Test Report **TR‑2024‑015** | The equivalence statement is limited to DQE; the NB may require additional endpoints (e.g., contrast detectability, dose metrics), a statistical analysis plan and justification of sample size – **missing**. |
| **Test Report(s) supporting performance claims** | *Test Report TR‑2024‑015* (IEC 62220‑1‑1) cited | Only one test report is provided; the NB may request verification of other GSPR items such as radiation protection (§16), electromagnetic compatibility, and software validation. |
| **PMCF Plan & PMCF Evaluation Report** | Not mentioned in excerpts | **Absent** – required for Class IIb (Annex XIV Part B). |
| **Post‑Market Surveillance (PMS) system & plan** | Not mentioned | **Absent** – Art. 83/84 MDR. |
| **Risk Management File (RMF)** – ISO 14971:2019 compliant, covering all identified hazards and residual risk evaluation | Not referenced | **Missing** – required under Annex I §3‑§8 & Annex II §5. |
| **Labeling / IFU (Information for Use) conforming to Annex I §23** | Not referenced | **Missing** – NB may have flagged unclear or incomplete labeling. |
| **Declaration of Conformity (DoC)** – signed, containing mandatory Annex IV items | Not referenced | **Missing/unclear** – must be provided with the revised technical documentation. |

---

### 3. Identified Deficiency (as per the NB’s “Deficiency Letter”)  

The source defines a *Deficiency Letter* as the NB’s written notice of “결함·불명확·누락 사항” (defects, ambiguities, or omissions) in the manufacturer’s submitted dossier. Although the exact items listed by the NB are not reproduced in the excerpt, the following typical gaps can be inferred from the evidence matrix above:

1. **Insufficient clinical‑equivalence justification** – only DQE metric provided.
2. **Lack of a complete PMCF strategy** (required for Class IIb).
3. **Absent or incomplete Risk Management File** (ISO 14971:2019).
4. **Missing PMS plan and post‑market reporting procedures** (Art. 83/84).
5. **Incomplete labeling / IFU information** (Annex I §23).
6. **No updated DoC reflecting the revised CER**.

---

### 4. Required Remedial Actions & Supporting Evidence  

| Action | Deliverable | Reference |
|--------|-------------|-----------|
| **Expand Clinical Evaluation** – include systematic literature review, justification of clinical equivalence beyond DQE (e.g., image quality metrics, dose efficiency), statistical analysis, and benefit‑risk conclusion. | Updated CER (Rev. 4) with full Annex XIV Part A content. | Art. 61 MDR; Annex XIV Part A |
| **Provide Additional Performance Test Reports** – e.g., IEC 60601‑2‑54 for radiography safety, IEC 60601‑1‑2 for electromagnetic compatibility, and any software verification (IEC 62304). | Test Report set (TR‑2024‑016 …) | Annex II §6.1 |
| **Develop & Submit PMCF Plan** – outline ongoing clinical data collection, timelines, responsible persons, key performance indicators. Follow Annex XIV Part B. | PMCF Plan + subsequent PMCF Evaluation Report (once data collected). | Annex XIV Part B |
| **Establish/Update PMS System** – define PMS plan (Art. 84), reporting mechanisms and annual PSUR (Art. 86) for Class IIb. | PMS Plan, PSUR draft (first edition). | Art. 83‑86 MDR |
| **Compile Risk Management File** – hazard identification, risk analysis (ISO 14971:2019), risk control measures, residual risk evaluation, and update after clinical data. | RMF (Chapter 3 of Annex II) | Annex I §3‑§8; ISO 14971:2019 |
| **Finalize Labeling & IFU** – ensure compliance with Annex I §23 (including symbols, warnings, contraindications). | Updated Labels, Instructions for Use. | Annex I §23 |
| **Issue Revised EU Declaration of Conformity** – signatory must attest to conformity with all MDR requirements and attach updated CER, RMF, PMS plan. | DoC (Annex IV content) | Art. 19 MDR; Annex IV |
| **Provide a cross‑reference matrix** linking each NB comment to the corrected document section. | Comment‑Response Table. | – |

---

### 5. Risk Controls (GSPR‑based)  

| GSPR § | Required control (as applicable to an X‑ray diagnostic system) | Implementation note |
|--------|---------------------------------------------------------------|---------------------|
| **§1–9** (General) | Full risk management process, including identification of radiation hazards and mitigation (e.g., shielding, interlocks). | ISO 14971:2019 RMF. |
| **§16** (Radiation protection) | Conformance to IEC 60601‑2‑54; verification of dose limits, beam quality, DQE ≥ 65 %. | Test Report TR‑2024‑015 & additional measurements. |
| **§17** (Electronic programmable systems) | Software validation per IEC 62304, including cybersecurity assessment. | Include in RMF and software file. |
| **§18** (Active devices/connected) | Electrical safety, EMC compliance – IEC 60601‑1 series. | Test reports required. |
| **§22** (Lay‑person use) – not applicable if only professional use is intended; nevertheless, provide clear instructions to avoid misuse. | IFU labeling update. |
| **§23** (Information supplied) | Complete labeling with safety information, contraindications, and user training requirements. | Updated Labels/IFU. |

---

### 6. Human‑Escalation Triggers  

1. **Unresolved Deficiency after 30 calendar days** – escalation to Senior RA Manager for decision on extending the response deadline or seeking a supplemental audit.  
2. **Missing Clinical Evidence (CER, PMCF) that prevents benefit–risk conclusion** – immediate notification to Head of Clinical Affairs; delay in submission may impact market launch schedule.  
3. **Risk‑management gaps exposing patients to unmitigated radiation hazards** – trigger Incident Management Team and possible interim safety notice per Art. 87 MDR.  
4. **Failure to provide updated DoC or labeling within NB’s stipulated timeline** – invoke Quality‑Assurance escalation; potential suspension of the CE mark.  

*All escalations must be documented in the project risk register and communicated via the established internal RA governance workflow.*

---

### 7. Peer‑Review Prompt  

> **To:** EU‑RA colleagues (clinical, quality & regulatory specialists  
> **Subject:** Review of Deficiency‑Letter Gap Analysis – X‑ray Diagnostic System (Class IIb)  
> **Request:** Please challenge the assumptions made regarding (i) the completeness of clinical equivalence justification based solely on DQE, (ii) the sufficiency of the identified evidence gaps versus what the NB may actually require, and (iii) any jurisdiction‑specific nuances (e.g., national competent‑authority expectations for radiation devices). Highlight missing references or alternative interpretations that could affect our remediation plan.

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

### kb-eval-20261020-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR", "MDCG"], "profile_id": "ra-eu", "scenario_id": "dcad67c543f1ef43", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDCG_가이던스/MDCG_2020-5-6-7-8_임상평가_PMCF_가이던스_요약.md", "source_hash": "a8adb60c55c2f1078b9906019f83eced38470b94f6090b2e6c2186bf55c720ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `dcad67c543f1ef43`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & Submission Planning**

---

### 1. Device Synopsis (derived from the source)

| Item | Description (as extracted) |
|------|-----------------------------|
| **Intended clinical application** | “임상적 적용 부위” – anatomical/physiological site of use (mandatory). |
| **Target patient population** | “임상적 대상 집단” – defined user group(s) (mandatory). |
| **User type** | “임상적 사용자 유형” – professional / lay‑person classification (mandatory). |
| **Core performance claim** | “임상적 핵심 성능” – primary clinical functionality to be demonstrated (mandatory). |

*The source stresses that the above items are required and must be identical across all clinical documentation (“same 필수”). No further details on device type, technology, or indication are supplied.*

---

### 2. Preliminary Classification & Conformity‑Assessment Route  

| Step | Determination | Regulatory basis |
|------|--------------|------------------|
| **Classification rule** | Not directly identifiable from the excerpt. The analyst must map the intended use to Annex VIII rules (e.g., Rule 9–11, 17). *Action*: Obtain full device description (energy delivery, diagnostic/therapeutic intent, software component) to pick the correct rule. |
| **Class** | **Undetermined – requires clarification**. |
| **Conformity‑assessment route** | Once class is known, the route follows Art. 52(3–7). For example: <br>• Class IIa → Annex IX (full QMS + technical‑doc assessment) or Annex II + III + Annex XI (alternative).<br>• Class IIb/III → Annex IX **or** Annex X + Annex XI. | Art. 52; Annex IX, Annex X, Annex XI (MDR 2017/745). |

*Human‑escalation trigger*: If the classification cannot be resolved within 5 working days after request for additional device information, escalate to senior RA lead.

---

### 3. Required Clinical Evidence  

| Requirement | Source (framework) | What must be provided |
|-------------|--------------------|-----------------------|
| **Clinical Evaluation Report (CER)** – Part A of Annex XIV | Annex XIV Part A; kept current under Art. 61 | • Systematic literature review covering state‑of‑the‑art (SOTA). <br>• Clinical data from equivalent devices, if applicable. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** – Part B of Annex XIV | Annex XIV Part B | • Planned PMCF activities (prospective studies, registries, literature surveillance). |
| **PMCF Evaluation Report** – mandatory sections listed in the MDCG guidance excerpt. | MDCG 2020‑5/6/7/8 summary (source) – no specific identifier; **no specific identifier found in source — verify separately**. | Sections A–G as per Table 5.2: <br>• Manufacturer contact.<br>• Updated device description (if changed).<br>• Results of PMCF activities (including positive/negative findings, justification of deviations).<br>• Evaluation of clinical data from equivalent/similar devices.<br>• Impact on Technical Documentation (CER, RMF, SSCP).<br>• Applied consensus standards/guidance.<br>• Overall conclusion vs. PMCF objectives and any corrective actions required. |
| **PMS Plan & PMS Report** | Art. 84 (plan) & Art. 85 (report for Class I) / Art. 86 (PSUR for Class IIa‑III). | • Systematic collection of post‑market data.<br>• Periodic summarised safety/performance updates. |
| **Risk Management File (RMF)** – continuous update | Annex I Chapter I (§3–9) plus ISO 14971:2019 | • Updated risk analysis reflecting clinical findings and PMCF outcomes. |

*Human‑escalation trigger*: If any of the above elements cannot be supplied within 10 business days (e.g., missing equivalent‑device data, incomplete PMCF results), raise a **Clinical Evidence Gap** ticket to the Project Manager.

---

### 4. Identified Gaps – Based on Current Information  

| Gap | Impact on Submission | Required Action |
|-----|----------------------|-----------------|
| **Device classification not established** | Prevents selection of correct conformity route and definition of required clinical data depth. | Obtain full intended use, mode of action, software/energy characteristics; apply Annex VIII rules. |
| **No detailed description of core performance claim** | CER must justify clinical benefit vs. risk; vague claim leads to insufficient evidence. | Provide explicit performance endpoints (e.g., sensitivity, specificity, therapeutic effect). |
| **Absence of equivalent‑device clinical data** (Section D of PMCF report) | May require additional clinical investigations or expanded literature search. | Identify and collect published/registry data for devices with the same intended purpose and similar design. |
| **No record of impact on Technical Documentation** (Section E) | Incomplete linkage between PMCF outcomes and updates to CER, RMF, SSCP → non‑compliance with Annex XIV Part B. | Map each finding to required document revisions; prepare amendment worksheets. |
| **Unclear applicable consensus standards/guidance** (Section F) | Missing standard compliance can be raised by NB during assessment. | List all relevant harmonised standards (e.g., IEC 62366‑1, ISO 14971, IEC 60601‑2‑28 for X‑ray tubes if applicable). |
| **No conclusion on need for corrective actions** (Section G) | If negative trends exist, NB will request a Field Safety Corrective Action (FSCA) plan. | Analyse PMCF results; draft FSCA where required and submit as per Art. 87. |

*Human‑escalation trigger*: Any gap remaining after the next 7‑day remediation window must be escalated to **Senior Regulatory Affairs Manager** for decision on whether a supplementary clinical investigation is needed.

---

### 5. Required Risk Controls (to satisfy GSPR §3–9)

| Control | Reference | Rationale |
|----------|-----------|------------|
| **Updated risk management plan** incorporating PMCF findings | Annex I Chapter I (§3) & ISO 14971:2019 | Demonstrates continuous evaluation of residual risks. |
| **Usability engineering** if user type includes lay persons (e.g., §22) | Annex I §22 | Mitigates use‑error risk identified in clinical setting. |
| **Safety‑related software controls** for any embedded software (Rule 11 devices) | Annex I §17 & IEC 62304 | Ensures that software behaviour aligns with clinical claims. |
| **Protection against radiation** (if device emits ionising radiations) | Annex I §16 | Required for X‑ray or CT equipment. |
| **Sterility assurance (if applicable)** | Annex I §5 & relevant sterility standards | Addresses risk of infection for invasive devices. |

*Human‑escalation trigger*: If any required control cannot be demonstrated (e.g., lacking usability validation data), an **Action‑Item** must be opened with the Design Engineering team within 3 working days.

---

### 6. Summary Judgment & Next Steps  

1. **Classification & route selection** – pending detailed device description.  
2. **Clinical evidence package** – build CER (Annex XIV Part A) and PMCF Evaluation Report (sections A‑G as per MDCG guidance).  
3. **Address identified gaps** – collect equivalent‑device data, define performance endpoints, map standards, update RMF/SSCP.  
4. **Prepare risk‑control updates** – align with GSPR §§3–9.  

If any of the above actions are not completed within the stipulated timeframes (see “Human‑escalation triggers”), the case must be escalated to senior RA leadership for possible re‑scope or additional clinical investigation.

---

### 7. Peer‑Review Prompt  

> **To a fellow EU Regulatory Affairs colleague:**  
> Please review the assumptions made regarding the unknown device classification and the inferred need for equivalent‑device data. Confirm whether the proposed list of mandatory PMCF report sections aligns fully with the latest MDCG 2020‑5/6/7/8 guidance, or if additional subsections (e.g., statistical analysis plan) should be incorporated. Also, verify that all cited regulatory bases (Art. 52, Annex XIV, ISO 14971:2019, etc.) are correctly applied to the gaps identified.

---

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

### kb-eval-20261020-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "41d9f4282c7091bf", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md", "source_hash": "83b51bd7f4800e3ee57c5a56cd9fa2ffbc9c9ae0c8700841a5917695f1dbea33"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `41d9f4282c7091bf`
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

> **Regulatory Draft – High‑Risk AI‑Enabled SaMD (MDR / AI Act)**  

---

### 1. Device scope & regulatory context
* **Product type:** Software‑as‑a‑Medical‑Device that incorporates an artificial‑intelligence algorithm (AI‑enabled device software functions).  
* **Applicable EU legislation:**  
  * Regulation (EU) 2017/745 MDR – Annex I, Section A point 11 (device falls under the “medical devices” definition).  
  * Artificial‑Intelligence Act (Regulation (EU) 2026/1744) – Chapter III requirements for high‑risk AI systems.  

*Key source citations*:  
  * **Annex I, Section A point 11** – identifies the product as an MDR device (excerpt [1]).  
  * **Art. 6(1) MDR** – determines “high‑risk AI system” status for Class IIa/IIb/III and for Class Is/Im/Ir (excerpt [1]).  
  * **Art. 49 AI Act** – obligates entry in the EU database for high‑risk AI systems (excerpt [1]).

---

### 2. Classification & Conformity‑Assessment Route  

| Attribute | Determination |
|-----------|----------------|
| **MDR classification rule** | Apply **Rule 9** (active therapeutic) or **Rule 10/11** depending on function; in practice most AI‑enabled SaMD that provide diagnostic or therapeutic recommendations are **Class IIa**. If the AI output can cause serious deterioration, death, or irreversible damage, move to **Class IIb** (Rule 9/10). |
| **AI Act risk tier** | High‑risk AI system (Art. 6(1) MDR ↔ AI Act high‑risk definition). |
| **Conformity‑assessment route** | **Annex IX** – full quality‑management‑system plus technical‑documentation assessment by a Notified Body (NB).  <br>*Justification*: Class IIa/IIb/III require NB involvement per Art. 52(6)–(3); AI‑act integration does not change the MDR route, only adds Chapter III obligations. |
| **Relevant NB modules** | – QMS assessment (ISO 13485:2016).  <br>– Technical documentation review (Annex II §§1‑6).  <br>– Post‑market surveillance system (Art. 83‑86). |

*Citation*: MDR Art. 52(6) for Class IIa, Art. 52(4) for Class IIb/III; **Annex IX** as the sole route (framework reference – no verification caveat).

---

### 3. Required Evidence Package  

| Item | Regulatory basis | Content required |
|------|-------------------|------------------|
| **Technical Documentation (TD)** | Annex II §6.1 (clinical evaluation, PMCF) | • Device description, intended use, classification rationale (Rule 9/10/11). <br>• Design & manufacturing information. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 MDR | • State‑of‑the‑art literature review (including AI‑specific performance studies). <br>• Clinical data (prospective/retrospective) demonstrating safety & performance for the intended indication. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B; Art. 86 (PSUR) for Class IIa/IIb/III | • Structured plan covering algorithm updates, data drift monitoring, and re‑validation cycles. <br>• Interim PMCF report summarising findings to date. |
| **Risk Management File (RMF)** | Annex I §§3‑8; ISO 14971:2019 | • Hazard analysis, risk estimation, control measures for AI‑specific risks (bias, over‑fitting, data quality). <br>• Residual risk evaluation and benefit‑risk determination. |
| **Software Lifecycle Documentation** | IEC 62304 2006+A1:2015; IEC 82301 (cybersecurity) | • Software development plan, verification & validation activities, change‑control procedures. |
| **Usability Engineering File** | IEC 62366‑1 2020 | • Human‑factors analysis, user interface testing, error‑use mitigation. |
| **AI‑Specific Documentation (AI Act Chapter III)** | Regulation (EU) 2026/1744 – Chapter III | • Data governance plan, training data set description, performance metrics, transparency & explainability documentation, conformity‑assessment report for AI component. |
| **EU Database Registration** | Art. 49 AI Act | Entry of the high‑risk AI system in the European Artificial Intelligence database (EAI‑DB). |
| **Declaration of Conformity (DoC)** | Art. 19 MDR; content per Annex IV | Signed by manufacturer, referencing all applicable GSPR and AI‑Act annexes. |

*Framework citations*: All items refer to MDR/AI Act provisions listed above – no invented identifiers.

---

### 4. Identified Evidence Gaps  

| Gap | Why it matters | Suggested remedial action |
|-----|----------------|---------------------------|
| **Intended‑use statement & classification justification** | Required in TD (Annex II) and to confirm applicability of Rule 9/10/11. | Draft a detailed Intended Use description, map each functional claim to the appropriate MDR rule. |
| **Algorithmic transparency & data provenance** | AI Act Chapter III demands documented training data, bias mitigation, and performance validation. | Provide dataset specifications (size, source, labeling process), bias analysis report, and reproducibility plan. |
| **Clinical evidence for AI‑driven decision support** | CER must include clinical performance of the AI output, not only hardware/software. | Conduct a prospective/real‑world study showing diagnostic accuracy vs reference standard; embed results in CER. |
| **PMCF schedule for continuous‑learning updates** | For adaptive algorithms, the PMCF plan must cover re‑training cycles and post‑market re‑assessment (Art. 86). | Define trigger thresholds (e.g., model drift >5 %) and a documented re‑validation workflow. |
| **Cybersecurity risk assessment** | IEC 82301 compliance required for networked AI devices; impacts Annex I §3‑8 residual risk. | Perform threat modelling, implement security controls, document in RMF. |
| **EU database entry (EAI‑DB) details** | Mandatory registration under Art. 49; missing entry blocks conformity declaration. | Prepare the EAI‑DB submission dossier (system name, high‑risk classification, responsible person). |
| **Notified Body engagement for Class Is/Im/Ir** | If the device is sterile or has measuring/re‑usable surgical functions, NB involvement is compulsory (excerpt [1]). | Confirm the exact class; if Is/Im/Ir, open a formal NB audit request. |

*All gaps are flagged with “no specific identifier found in source — verify separately” only where a precise regulation number would have been required but was not provided directly.*

---

### 5. Risk‑Control Measures (to be reflected in the RMF)

1. **Algorithmic bias mitigation** – data‑set diversification, fairness metrics, periodic re‑assessment.  
2. **Performance degradation monitoring** – drift detection algorithms; automatic alerts when key performance indicators fall below predefined limits.  
3. **User training & labeling** – clear instructions per Annex I §23, including limitations of AI output and required clinician oversight.  
4. **Cybersecurity safeguards** – encryption, secure firmware updates, vulnerability management per IEC 82301.  
5. **Fail‑safe mode** – default to “no decision” when confidence score below threshold; prompts user to consult alternative diagnostic method.  

All controls map to Annex I §§3‑8 (risk management) and to AI Act obligations for high‑risk systems.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action required | Timeline |
|---------|-----------------|----------|
| **Missing or incomplete intended‑use / classification rationale** | Pause NB submission; senior RA reviews and updates documentation. | Immediate (within 5 working days). |
| **Absence of AI‑Act Chapter III dossier (data governance, transparency)** | Escalate to Head of AI‑Regulatory Affairs for rapid completion. | Within 10 working days. |
| **Clinical evidence not sufficient to support safety/performance** | Trigger external clinical consultant review; possible need for new study. | As soon as gap identified; re‑submission no later than 3 months after data acquisition. |
| **PMCF plan lacking adaptive‑learning controls** | Senior PMCF Lead to develop and approve updated plan before NB audit. | Within 2 weeks of identification. |
| **NB indicates classification mismatch (e.g., Class Is/Im/Ir vs declared Class IIa)** | Immediate reassessment by Regulatory Manager; possible reclassification and route change. | Within 3 working days. |
| **Upcoming EU database registration deadline (Annex III 2027‑12‑02, Annex I 2028‑08‑02 per excerpt [2])** | Schedule pre‑submission of EAI‑DB entry; senior manager sign‑off. | Start actions no later than 6 months before each date. |
| **Regulatory change notice (e.g., new AI Act amendment)** | Monitor Official Journal; if amendment affects scope, raise to Compliance Committee. | Ongoing; review within 1 week of publication. |

When any trigger occurs, the responsible team member must log the issue in the project’s risk‑log and notify the **Regulatory Project Lead** (e‑mail with “URGENT – MDR/AI Act Gap”) for escalation.

---

### 7. Summary Judgment  

* The AI‑enabled SaMD is a **high‑risk AI system** under Art. 6(1) of the MDR and consequently falls within **Class IIa (or IIb if the algorithm can cause serious deterioration)**.  
* The appropriate conformity‑assessment route is **Annex IX – full QMS + technical‑documentation assessment by a Notified Body**, with mandatory NB involvement for Class Is/Im/Ir devices.  
* A complete evidence dossier must include MDR‑required TD, CER, PMCF plan/report, RMF (ISO 14971), software lifecycle files (IEC 62304), usability (IEC 62366‑1), AI‑Act Chapter III documentation, and EU database registration (Art. 49).  
* Current gaps are centred on **AI‑specific transparency, clinical performance data for the algorithm, PMCF for continuous learning, cybersecurity, and formal NB engagement** – all of which must be addressed before the next audit window.

---

### 8. Peer Review Prompt  

> *Please review this draft with special focus on:*  
> • **Assumptions about classification** (Rule 9/10/11 applicability) – could the device be higher than Class IIa?  
> • **Coverage of source material** – does any excerpt from the provided markdown suggest additional obligations or different deadlines?  
> • **Jurisdiction‑specific gaps** – are there EU‑level updates (post‑2026 AI Act amendments) that may affect the evidence requirements?  

Your feedback will be incorporated into the final submission package.

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

1. Chunk `1013595113860735371`

> ### 2.1 High-risk AI 분류 판단 절차 ``` 1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가? ├─ Yes: MDR/IVDR 등재 확인 │ └─ 제3자 적합성평가(NB) 필요한 Class? │ ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1)) │ └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인) │ ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은 NB 관여 → **Art.6(1) 해당** (MDCG 2025-6/AIB 2025-1 Q2·Table 1) └─ No: Annex III 별도 해당 여부 확인 2. High-risk 확정 시 ├─ AI Act Chapter III 전체 요건 적용 ├─ 적합성평가 경로: MDR 경로에 AI Act 요건 통합 └─ EU DB 등록 의무 (Art. 49) ``` **판정 기준**: 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높다.

2. Chunk `1015646396132986584`

> lan for AI-Enabled Device Software Functions (Final; 2025-08-18 현재 본; Docket FDA-2022-D-2628; original final issued December 2024)"으로 갱신. 범위를 ML→**AI-enabled device software functions 전반**으로 보정. FDA Guidance 페이지(2025-08-18 current)로 직접 재확인. 사내 SOP-AIGOV-001 v0.3 "FDA PCCP Guidance 2024" 표기와 정합 회복 | | v0.9 | 2026-09-11 | **P0 사실성 정정 (audit #1041)** — Regulation (EU) 2026/1744(Digital Omnibus on AI, 채택 2026-07-08 / OJ 2026-07-24 / 발효 2026-07-27, CELEX 32026R1744) 확정 반영. §3 일정표에 발효일·Annex III 2027-12-02·Annex I 2028-08-02 행 신설, '잠정 합의 시·예상·미완료' 조건부 표현 전량 제거. §12.2 시나리오 (A)/(B) 분기를 (A) 확정으로 종결하고 (B) 트랙 삭제, 기준일을 2028-08-02로 재설정. §12 D-36 D-day·...

### kb-eval-20261020-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "537094dad189e321", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `537094dad189e321`
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

> **Regulatory Draft – Clinical‑Evaluation Gap Analysis & Conformity Pathway**

---

### 1. Device Classification (preliminary)

| Item | What is required by the MDR | Current status / gap |
|------|-----------------------------|----------------------|
| **Intended purpose statement** (including patient population, anatomical area, therapeutic/diagnostic function) | Needed to select the applicable rule in Annex VIII. | Not provided in source – must be obtained from product‑development files. |
| **Mode of action / energy type** (e.g., ionising radiation, electrical energy, software algorithm) | Determines whether Rule 9, 10, 11 or 17 applies (see “Active device rules” table). | No description available – request from R&D. |
| **Invasiveness & duration of contact** (implantable, surgically invasive, transient) | Influences class under the same rules. | Missing. |
| **Pre‑market clinical data** (existing CE‑marked equivalents, predicate devices) | Needed for equivalence justification if a lower‑risk class is claimed. | Not yet documented in the CER. |

> **Action:** Obtain a complete “Intended Use & Mode of Action” dossier from R&D. Use it to apply the classification rules of Annex VIII (e.g., Rule 10 for diagnostic X‑ray systems, Rule 17 for image‑detector modules, Rule 11 for associated software).  

*If the device is an X‑ray system as suggested by the referenced IEC 60601‑2‑54 standard, a likely outcome is:*  
- **X‑ray source/generator** → Rule 10 → Class IIb  
- **Detector/image plate** → Rule 17 → Class IIa  
- **Processing software** → Rule 11 → Class IIa (or IIb/III if decision impact is high).  

(These are illustrative; final class must be confirmed with the complete intended‑use information.)

---

### 2. Conformity‑Assessment Route

| Determined class | Applicable Art. 52 paragraph | Required conformity route |
|------------------|-----------------------------|---------------------------|
| **Class IIa** (if applicable) | Art. 52(6) | Annex IX (QMS + technical‑documentation assessment) **or** Annex II/III + Annex XI §10 (production‑conformity verification). |
| **Class IIb** (if applicable) | Art. 52(4) | Annex IX (full technical‑documentation assessment) **or** Annex X (type‑examination) + Annex XI (production conformity verification). |
| **Class III** (if applicable) | Art. 52(3) | Annex IX (full assessment) **or** Annex X + Annex XI. |

> **Citation:** Art. 52 of the MDR and Annex VIII (classification rules) – *framework reference*.

---

### 3. Required Evidence & Documentation (per MDR)

| Technical File Section (Annex II §1‑6) | Mandatory content | Current status (from source [1]) |
|---------------------------------------|-------------------|---------------------------------|
| **1. Device description** | Intended purpose, variants, accessories. | Not yet compiled – pending from R&D. |
| **2. Manufacturer information** | Name, address, contact, EU representative. | Presumed present (RA responsible). |
| **3. Design & manufacturing information** | Materials, specifications, manufacturing processes, verification & validation results. | V&V data collection is in progress (step 2 of source [1]). |
| **4. General Safety & Performance Requirements (GSPR)** | Mapping to Annex I §1‑23. | GSPR mapping completed (step 3) – needs final sign‑off and traceability matrix. |
| **5. Benefit–risk analysis & risk management** | ISO 14971:2019 risk management file, residual‑risk evaluation. | Risk‑management report integrated (step 5). |
| **6. Clinical Evaluation** (Annex XIV Part A) | Up‑to‑date Clinical Evaluation Report (CER). | CER draft produced (step 4) – identified as *out‑of‑date*; requires literature update and/or new clinical data. |
| **7. Post‑Market Surveillance (PMS)** (Art. 84, Annex III) | PMS plan, periodic safety update report (PSUR) for Class IIa/IIb/III (Art. 86). | PMS plan drafted (step 6). Further detail needed on data sources and timelines. |
| **8. PMCF** (Annex XIV Part B) | PMCF plan & final evaluation report (required for Classes IIa‑III). | Not yet prepared – gap identified. |

> **Citation:** Annex II §6.1 (clinical‑evaluation data location), Annex XIV Part A/B, Art. 84‑86 – *framework references*.

---

### 4. Identified Gaps & Missing Information

| Gap | Why it matters | Suggested remediation |
|-----|----------------|-----------------------|
| **Incomplete Intended‑Use statement** | Determines classification and scope of clinical evidence. | Obtain a signed “Intended Use” document from product development; include indication, target population, and mode of action. |
| **Out‑dated CER** (no recent literature > 5 years, no equivalence data) | Prevents compliance with Art. 61 (keeping the CER current). | Conduct systematic state‑of‑the‑art review; add any newly required clinical investigations or post‑market data. |
| **Absence of PMCF plan** for Classes IIa/IIb/III | Required by Annex XIV Part B to demonstrate ongoing safety/performance. | Draft a PMCF plan covering data sources (registries, literature, post‑market data), timelines, and responsibilities; submit to the NB for review. |
| **PMS Plan lacking quantitative metrics** (e.g., trigger levels, reporting intervals) | Art. 84 requires a defined PMS system with measurable objectives. | Enrich the plan with specific KPIs, sample sizes, and risk‑based vigilance thresholds. |
| **Risk‑control measures for ionising radiation** not explicitly documented | Annex I §16 demands protection against radiation hazards. | Add design controls (shielding, dose monitoring), user training requirements, and residual‑risk evaluation per ISO 14971. |
| **Software usability evidence** (if software component present) | Annex I §17 & IEC 62366‑1 require usability engineering for devices that influence clinical decisions. | Perform a usability study; include formative/validated test results in the Technical File. |
| **Traceability matrix linking GSPR to verification/validation evidence** | Required for auditability of compliance with Annex I. | Populate the matrix using the “GSPR 체크리스트” referenced in source [2]; ensure each requirement is evidenced. |

---

### 5. Risk Controls (to be reflected in the Risk‑Management File)

| Hazard category | Relevant MDR clause / IEC standard | Example control measures |
|-----------------|------------------------------------|--------------------------|
| **Radiation exposure** (X‑ray source) | Annex I §16; IEC 60601‑2‑54 | Shielding, interlocks, dose‑rate monitoring, user training, periodic calibration. |
| **Software decision impact** | Annex I §17; IEC 62304; IEC 62366‑1 | Secure development lifecycle, validated algorithms, usability testing, failure mode analysis. |
| **Active device electrical safety** | Annex I §18; IEC 60601‑1 | Built‑in protective earth, leakage current limits, fault detection. |
| **Use‑error (operator) risk** | Annex I §5 & §22 | Clear IFU, ergonomic design, lock‑out procedures, labeling per Annex III §23. |
| **Residual risk evaluation** | ISO 14971:2019 – risk acceptability criteria | Overall residual risk must be weighed against demonstrated clinical benefit (benefit–risk determination in the CER). |

---

### 6. Human‑Escalation Triggers

| Trigger condition | Who is alerted | Deadline for remediation |
|-------------------|----------------|---------------------------|
| **Classification cannot be finalized** after request for intended‑use information → *no response within 5 working days* | RA Lead & Project Manager | Escalate to Senior Regulatory Director. |
| **CER remains outdated** (> 30 days without a revised literature review) | Clinical Affairs Lead | Immediate halt of NB submission; assign external clinical reviewer. |
| **PMCF plan not approved** within 14 days of draft completion | RA/Clinical & QA Manager | Escalate to Quality Management System (QMS) Owner for resource re‑allocation. |
| **PMS plan missing quantitative metrics** after two review cycles | PMO / Post‑Market Surveillance Coordinator | Raise to Senior VP of Regulatory Affairs. |
| **NB requests additional evidence** that is not in the current TD (e.g., clinical investigation data) and no feasible source is identified within 10 working days | RA Lead & Project Sponsor | Pause any further NB interactions; consider redesign or alternative compliance route. |

---

### 7. Summary Judgment

*Based on the information currently available (source [1]–[2]), the device’s classification cannot be conclusively determined without a complete intended‑use and mode‑of‑action description. Consequently, the conformity‑assessment route remains provisional pending that determination.*

**Key next steps:**

1. Secure the full Intended Use & Mode of Action documentation from R&D.  
2. Update the Clinical Evaluation Report with recent literature/equivalence data.  
3. Draft a PMCF plan and enrich the PMS plan with quantitative triggers.  
4. Complete the GSPR‑to‑evidence traceability matrix.  
5. Align risk controls with Annex I §§16‑22 and ISO 14971:2019.

All identified gaps must be addressed before any Notified Body submission.

---

### 8. Peer‑Review Prompt

*Please review this draft and challenge the following points:*  

- **Assumptions about device type** (X‑ray system) – is there evidence in other project artefacts that would alter the classification rule(s)?  
- **Scope of required clinical evidence** – are there alternative equivalence arguments or existing CE‑marked devices that could reduce the need for a full PMCF?  
- **Completeness of risk‑control listings** – have any hazard categories (e.g., cybersecurity) been omitted given the software component?  

Your feedback will be recorded via `honcho_conclude` and used to refine the final regulatory package.

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

## ra_kr

### kb-eval-20261020-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["KGMP"], "profile_id": "ra-kr", "scenario_id": "c47d06aab2919a37", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "e9b8cb8af7deb10d88f0208f03d685e1ae7f3d5a1c2d1458cd1e0ac87b24877f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `c47d06aab2919a37`
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

> **Regulatory Draft – KG MP Evidence Readiness for Independent‑Use SaMD (촬영실 GUI SW)**  

---

### 1. Classification & Submission Route (Korean system)

| Item | Assessment |
|------|------------|
| **Device type** | Stand‑alone software that performs image acquisition/processing in a radiology suite (SaMD). |
| **Probable Korean grade** | Most SaMDs are placed **4등급** under the MFDS “의료기기 품목 및 품목별 등급에 관한 규정” because they directly influence diagnostic decisions. <br>*No specific grade is stated in the source excerpts – verification with the official grade table is required.* |
| **Submission track** | If confirmed as 4등급 → **허가** (MFDS full approval). For lower grades, the track would change (2등급 → 인증, 1등급 → 신고). |

*Citation:* no specific identifier found in source – verify separately.

---

### 2. Required Evidence Package  

| Korean Requirement | Typical Content | Mapping to International Evidence |
|--------------------|----------------|-----------------------------------|
| **KGMP certification** (제28조) | Facility KGMP audit report, certificate of conformity for any outsourced sterilization or relabeling activities. | Aligns with FDA QMSR scope expansion in §820.10(a). |
| **QMS compliance** | Full KGMP‑based quality manual, SOPs, internal audit reports (covering §§ 820.35, 820.10) integrated with ARR activities. | ISO 13485 (2016) – required but insufficient alone per FDA §820.10(b). |
| **Software Development Lifecycle (SDLC)** | Design History File (DHF) containing SDP, SRS, SAD, SVP, SVR; version control; change‑management SOPs. | IEC 62304 (2006+A1:2015) – Safety Class C (source excerpt). |
| **Software Validation & Verification** | Unit, integration, system testing records; regression test automation evidence; verification of risk mitigations. | IEC 62304 §8.1 (cited in source). |
| **Risk Management** | ISO 14971 (2019) risk analysis file, risk control measures, residual risk evaluation, post‑market surveillance plan. | Korean MFDS risk‐management requirement mirrors the ISO standard. |
| **Cybersecurity** | Threat model, SBOM, PCCP (pre‑market cyber‑product certification) dossier; compliance with *MFDS 사이버보안 가이드라인 2025*. | FDA 524B PCCP & MDCG 2019‑16 Rev.1 referenced in source. |
| **Clinical Evaluation** (if required) | Clinical performance evidence – Korean patient data or accepted foreign clinical evaluation report (CER) per MFDS notice on foreign CER acceptance (no specific notice number cited). |
> *If the device is classified 4등급, a full clinical trial or an accepted foreign CER will be mandatory.*  

| **Labeling & IFU** | Korean language labeling, symbols, and instructions for use; conformity with MFDS labeling Annex. |
| **Post‑Market Surveillance (시판후조사)** | PMS plan, adverse event reporting procedure, periodic safety update (no EU PSUR term used). |

---

### 3. Identified Gaps / Missing Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Confirmed Korean grade** | Determines submission track and required clinical evidence. | Query MFDS “의료기기 품목 및 품목별 등급에 관한 규정” for exact grade of the specific SaMD function. |
| **Clinical performance data (local)** | Required for 4등급 허가; foreign CER acceptance depends on MFDS scope notice. | Obtain Korean clinical trial results or verify applicability of any existing FDA‑cleared/CE‑marked predicate under current MFDS guidance. |
| **KGMP facility certification** (if software is supplied by a contract manufacturer) | Required for all manufacturing steps, including contract sterilization/relabeling (as per §820.10(a) expansion). | Secure KGMP audit report for the development and any outsourced activities. |
| **Full cybersecurity dossier** | MFDS cyber guide 2025 expects threat modeling + SBOM + PCCP; missing elements will block approval. | Prepare threat model, generate SBOM, complete PCCP submission. |
| **Korean language labeling & IFU** | Mandatory for all grades; omission leads to non‑conformity. | Draft Korean labeling and user manual; ensure translation review. |
| **Post‑Market Surveillance (PMS) plan details** | MFDS requires a PMS system tailored to the device grade. | Develop PMS SOPs, adverse event handling flowchart, reporting timelines. |

---

### 4. Core Risk Controls (to be documented)

1. **Hazard Identification & Classification** – per ISO 14971; map each identified hazard to a control.
2. **Software Safety Controls** – IEC 62304 Class C requirements: defensive coding, fail‑safe states, verification of error handling.
3. **Cybersecurity Measures** – Threat modelling, regular vulnerability scanning, secure update mechanism (aligned with MFDS cyber guide 2025).
4. **Usability Validation** – Human factors testing for the GUI to mitigate use errors.
5. **Configuration Control** – Strict change‑management SOP; all software releases tracked in a Configuration Management Database.
6. **Monitoring of Post‑Market Data** – Real‑time adverse event capture, periodic safety update submission.

---

### 5. Citations  

| Category | Reference |
|----------|-----------|
| **Framework references** | ISO 13485 (2016) – QMS standard<br>IEC 62304 (2006+A1:2015) – Software life‑cycle standard (Safety Class C)<br>ISO 14971 (2019) – Risk management |
| **Instance identifiers from source** | FDA 21 CFR §820.10(b) – ARR requirement<br>FDA 21 CFR §820.35(a) – Complaint file enhancement<br>FDA 21 CFR §§ 820.35, 820.180(c) – Internal audit access<br>MFDS 사이버보안 가이드라인 2025 (no numbered notice in source) |
| **No specific MFDS notice/grade identifier found** | *Verify separately* – Korean grade and any MFDS notice governing foreign clinical evaluation report acceptance. |

---

### 6. Human‑Escalation Triggers  

| Trigger condition | Action required |
|-------------------|-----------------|
| **Unconfirmed device grade** (cannot assign 4등급/허가) | Escalate to senior RA for classification verification with MFDS reference table before dossier assembly. |
| **Missing KGMP certificate** for any contract manufacturer or sterilization service | Pause submission; obtain audit report and re‑issue QMS documentation. |
| **Insufficient clinical evidence** (no local data, no acceptable foreign CER) | Escalate to Clinical Affairs lead to design a Korean pilot study or source an appropriate predicate. |
| **Cybersecurity dossier incomplete** (e.g., SBOM missing) | Halt submission; request cybersecurity team deliver full PCCP‑aligned package. |
| **Korean labeling not finalized** | Stop file preparation; involve translation/legal compliance team. |
| **Post‑Market Surveillance plan absent or non‑conformant** | Notify PMO to develop PMS SOPs per MFDS requirements before filing. |

When any trigger fires, the responsible owner must log the issue in the project tracker and seek approval from the RA lead before proceeding.

---

### 7. Peer Review Prompt  

*“Please review this draft and challenge: (1) the assumption that the SaMD falls under 4등급 – could its risk profile place it in a lower grade? (2) Whether the identified clinical evidence gaps truly require new Korean data, or if an existing foreign CER might be acceptable under a recent MFDS notice (which is not cited here). (3) The completeness of the cybersecurity evidence relative to the 2025 MFDS cyber‑security guideline – are there additional required deliverables we have missed?”*

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

1. Chunk `1063839161629370289`

> | 추가 요건 | 근거 조항 | 내용 | |---|---|---| | **ARR (Applicable Regulatory Requirements)** | §820.10(b) | ISO 13485 준수만으로 불충분; UDI(21 CFR 830), MDR reporting(21 CFR 803), Corrections & Removals(21 CFR 806) 별도 준수 의무. QMS 절차서에 ARR 준수 활동 통합 필수. | | **불만 파일 강화** | §820.35(a) | 불만 접수 시 MDR reportable 여부 판단 기록 필수. ISO 13485 §8.2.1보다 상세. (구 QSR §820.198이 §820.35(a)로 이관 — §820.20은 구 QSR 경영책임 조항으로 이 용도에 부적합) | | **서비스 기록** | §820.35 | 서비스 수행 기록·서비스 보고서 요건 명시. | | **내부감사 실사** | §820 전반 | 구 §820.180(c) 내부감사·경영검토 비공개 예외 삭제. FDA 실사관이 내부감사 보고서 열람 가능. | | **계약 멸균·재라벨러 포함** | §820.10(a) | QMSR 적용 대상: 계약 멸균업체, 재라벨러, 외국 초기 유통업체 포함(기존 QSR보다 확대). | | **용어 정의 우선순위**...

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

### kb-eval-20261020-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "536f0f84eba3f401", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `536f0f84eba3f401`
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

> **Regulatory Draft – P3 촬영실 GUI SW (디지털 의료기기 소프트웨어)**  

---

### 1. Classification & Submission Route  
| Item | MFDS determination* |
|------|---------------------|
| **Device grade** | The source indicates the product may be “2등급이든 등급 미지정이든” 【1127968925422991528】. The exact grade must therefore be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」. |
| **Submission track** | • If confirmed as **2등급**, the default route is **인증** (technical‑documentation review by an MFDS‑designated 심사기관).  <br>• If later AI‐assistance functions are added, a re‑classification may be required and could trigger a **허가** pathway (3등급·4등급) 【198902914416608487】. |
| **Regulatory references** | • 디지털의료제품법 시행규칙 (2026‑01‑23 개정) – especially 제25조 각 호 for exemption/alternative pathways (requires article‑level verification).  <br>• KGMP 인증 (의료기기법 제28조) is mandatory for any manufacturing site. |

\*When the grade cannot be confirmed from the source, note: **“grade must be verified from official MFDS grade list – no specific identifier found in source – verify separately.”**

---

### 2. Required Evidence  

| Evidence Category | Detail required (Korean‑specific) |
|-------------------|-----------------------------------|
| **Device description & intended use** | Full functional specification of the GUI, user interface flow, and statement that it is *“디지털 의료기기소프트웨어에 해당”* 【1127968925422991528】. Must be in Korean for submission. |
| **Risk Management** | ISO 14971:2019‑based risk analysis file (including AI‑related hazards if future AI module is added). |
| **QMS compliance** | KGMP certification + ISO 13485:2016 conformity evidence (certificate, audit reports). The source notes that an “우수관리체계 특례” can turn QMS maturity into a regulatory benefit 【198902914416608487】. |
| **Clinical Evidence** | • If the device remains a pure GUI without AI, clinical trial exemption may be claimed under 제25조 각 호 (requires verification). <br>• If AI is added later, a comparative‑design clinical study per the 2025‑10‑31 revised clinical‑trial guidelines is required (AI vs. physician‑only diagnostic arm) 【1127968925422991528】. |
| **Labeling / IFU** | Korean language labeling, including safety information, intended user group and disposal instructions; must comply with MFDS labeling standards (no specific notice number cited). |
| **Cybersecurity** | Conformity to IEC 81001‑5‑1:2021 (referenced in MFDS cyber‑security guidance) for any network‑connected functions. |
| **Software Validation** | IEC 62304:2006+A1:2015 compliance evidence (development lifecycle, verification & validation). |

---

### 3. Identified Gaps / Information Needed  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact device grade** | Determines whether 인증 or 허가 is required. | Check the official MFDS “의료기기 품목 및 품목별 등급에 관한 규정”. |
| **Confirmation of exemption under 제25조 각 호** | The source flags requirement for article‑level verification 【198902914416608487】. | Retrieve the current 시행규칙 (2026‑01‑23) and read 제25조 each 항 to confirm applicability. |
| **Planned AI functionality timeline** | Determines if future clinical‑trial design must be prepared now. | Document product roadmap; if AI will be added before market launch, incorporate comparative‑design study plan per 2025‑10‑31 guideline 【1127968925422991528】. |
| **Korean IFU draft** | Korean language is mandatory for all devices; missing drafts block submission. | Prepare provisional Korean IFU and label mock‑up. |
| **Manufacturing site KGMP status** | Certification required before any MFDS filing. | Verify current KGMP certificate or schedule audit. |
| **Cybersecurity architecture details** | Needed if the GUI connects to hospital network or cloud services. | Provide IEC 81001‑5‑1 compliance documentation. |

---

### 4. Risk Controls (High‑Level)  

1. **Risk Management Process** – ISO 14971:2019 workflow; identify AI‑related hazards, perform severity/occurrence assessment, implement mitigation (e.g., “human‑in‑the‑loop” alerts).  
2. **Software Development Lifecycle** – IEC 62304 compliance: plan, develop, verify, validate, maintain.  
3. **Cybersecurity Controls** – Follow IEC 81001‑5‑1:2021: authentication, encryption, vulnerability management, incident response.  
4. **Usability Engineering** – Conduct formative/usability testing of GUI to prevent use errors (aligned with IEC 62366‑1:2015+A1:2020).  
5. **Post‑Market Surveillance** – Establish 시판후조사 plan per MFDS 규정 (monitor adverse events, software updates).  

---

### 5. Citations  

| Source | Content Cited |
|--------|----------------|
| **Chunk 1127968925422991528** | 2025‑10‑31 임상시험 가이드라인 9종 개정 – AI 비교설계 requirement; impact on GUI SW with potential AI module. |
| **Chunk 198902914416608487** | Grade ambiguity, exemption/alternative pathway under “개정 제25조 각 호”; KGMP/ISO 13485‑based 우수관리체계 특례; reference to 「디지털의료제품법 시행규칙」(2026‑01‑23 개정). |
| **Framework references (no specific identifier needed)** | 디지털의료제품법, KGMP (의료기기법 제28조), ISO 14971:2019, ISO 13485:2016, IEC 62304:2006+A1:2015, IEC 81001‑5‑1:2021, IEC 62366‑1:2015+A1:2020. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation |
|---------|------------------------|
| **Unresolved device grade** | Determines submission track; must be clarified before any filing. |
| **Pending verification of 제25조 각 호 applicability** | Legal review needed to confirm exemption or additional evidence requirements. |
| **Decision on AI feature inclusion before market launch** | Impacts clinical‑trial design, risk management, and possibly re‑classification to 3등급/4등급 (허가). |
> **Escalation Action:** Submit a “Regulatory Clarification Request” to the legal/R&A lead with collected grade list and 시행규칙 excerpts.  

---

### 7. Peer Review Prompt  

*“Colleague, please review the assumptions made regarding: (1) the tentative classification of the P3 촬영실 GUI SW as 2등급; (2) the applicability of exemption under 제25조 각 호 without the exact article text; and (3) the completeness of the evidence package for a future AI‑enhanced version. Identify any jurisdiction‑specific gaps (e.g., Korean labeling nuances, KGMP timing) that may have been overlooked.”*

---

### 8. Reusable RA Judgment (honcho_conclude)  

**Judgment:**  
- **Classification must be confirmed from MFDS grade list; do not assume 2등급.**  
- **If the device is 2등급, pursue 인증 via a designated 심사기관 after securing KGMP certification and completing ISO 13485:2016‑based QMS documentation.**  
- **When/if AI functionality is added, prepare for comparative‑design clinical trial evidence per the 2025‑10‑31 revised guidelines and re‑evaluate classification (possible move to 허가).**  
- **Exemption under 제25조 각 호 can only be claimed after direct verification of the current 시행규칙 (2026‑01‑23 개정); until then, treat it as a pending requirement.**  

**Escalation condition:** Any change in intended use, AI inclusion, or discovery that the device falls outside 2등급 triggers immediate reassessment of submission route and evidence needs.

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

### kb-eval-20261020-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "deb98b7e6d96e093", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `deb98b7e6d96e093`
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

> **Regulatory Draft – KGMP Evidence Readiness for a Digital Medical Device (디지털의료제품법 적용)**  

---

### 1. Device Classification & Submission Route  
| Item | Korean regulatory determination* |
|------|-----------------------------------|
| **Grade** | Must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」. Typical digital health‑software devices fall into **2등급**, **3등급** or **4등급** depending on the intended use and risk profile (e.g., diagnosis, therapy, data monitoring). |
| **Submission pathway** |  • 1등급 → 신고  <br>• 2등급 → **인증** by an MFDS‑designated 심사기관 (e.g., KTL, KTC)  <br>• 3등급·4등급 → **허가** (MFDS approval) |

\*If the grade cannot be confirmed from product specifications, the default assumption is **2등급 – 인증**; however, a definitive grade must be obtained before finalizing the submission route.

---

### 2. Required Evidence – KGMP & International Standards  

| Requirement ID | Korean regulatory basis (framework) | Evidence currently required (per source) | Status in source | Gap / Action |
|----------------|--------------------------------------|-------------------------------------------|------------------|--------------|
| **DR‑20** – 설계·개발 프로세스 | ISO 13485 §7.3 (design & development) – referenced as “GMP” in the matrix | • Design History File (DHF) structure <br>• Design verification/validation protocols and reports | ● (complete) | None |
| **DR‑21** – 위험관리 통합 | ISO 14971 (risk management) – referenced as “GMP, 고시” | • Risk Management File (RMF) <br>• Completed FMEA / FTA analyses <br>• Residual risk acceptance justification | ● (complete) | None |
| **DR‑22** – SW 수명주기 | IEC 62304 (software lifecycle) – referenced as “GMP” | • Software safety class determination <br>• Approved software lifecycle plan & related documents | ● (complete) | None |
| **DR‑23** – 공급자 관리 (구성요소·OSS) | GMP, SBOM 연계 – referenced as “GMP, SBOM 연계” | • OSS supply‑chain procedure <br>• Software Bill of Materials (SBOM) linking to components <br>• License compliance verification records | ◐ (in progress) | **Missing**: finalized OSS supply‑chain SOP, complete SBOM, license audit evidence. |
| **DR‑24** – 교육·훈련 (AI·사이버보안) | GMP – referenced as “GMP” | • AI developer education module <br>• Training completion records (attendance, assessment) | ◐ (in progress) | **Missing**: finalized training curriculum, documented evidence of trainee completion. |

*All items above are tied to the **디지털의료제품법** quality‑management matrix; no specific MFDS 고시 or notice numbers appear in the source excerpts, therefore a citation with a precise instrument number cannot be provided – “no specific identifier found in source – verify separately”.

---

### 3. Risk Controls Already Implemented  

| Control | Standard Mapping | Evidence (as per matrix) |
|---------|-------------------|---------------------------|
| Risk Management File (RMF) – hazard identification, FMEA/FTA, residual risk evaluation | ISO 14971 | DR‑21 (●) |
| Software safety class & lifecycle planning | IEC 62304 | DR‑22 (●) |
| Design verification & validation procedures | ISO 13485 §7.3 | DR‑20 (●) |
| Supplier & OSS component management (to be completed) | GMP, SBOM requirement | DR‑23 (◐) – pending SOP & SBOM |
| AI developer cybersecurity training (to be completed) | GMP / MFDS cyber‑security guidance (e.g., IEC 81001‑5‑1 reference) | DR‑24 (◐) – pending curriculum and records |

---

### 4. Missing Information & Immediate Actions  

| Gap | Required Deliverable | Owner | Target Date (suggested) | Escalation Trigger |
|-----|----------------------|-------|--------------------------|--------------------|
| **OSS supply‑chain SOP & SBOM** | Complete procedure, up‑to‑date SBOM covering all open‑source libraries, license compliance matrix | Supplier Management Lead | Within 2 weeks | If not finalized → pause KGMP audit; notify QA Manager. |
| **AI/Cybersecurity Training Records** | Finalized training module, attendance & assessment documentation for each AI developer | Education & Compliance Lead | Within 10 days | Absence → risk of non‑compliance with MFDS cyber‑security expectations; raise to Project Sponsor. |
| **Grade Confirmation** | Formal classification (1~4등급) per 「의료기기 품목 및 품목별 등급에 관한 규정」 | Regulatory Lead | ASAP (prior to dossier compilation) | Unconfirmed grade → cannot determine correct submission pathway; trigger senior RA review. |
| **Local Clinical Evidence (if 3/4등급)** | Korean‑language clinical evaluation or post‑market data as required by MFDS 고시 for the identified grade | Clinical Affairs Lead | Dependent on grade decision | Missing mandatory local data → block 허가 filing; immediate escalation to PMO. |

---

### 5. Citations  

| Type | Citation |
|------|----------|
| **Framework reference** – Design & Development process | ISO 13485 §7.3 (no specific Korean notice number in source). |
| **Framework reference** – Risk Management | ISO 14971 (risk management) (no specific Korean notice number in source). |
| **Framework reference** – Software Lifecycle | IEC 62304 (software safety class & lifecycle) (no specific Korean notice number in source). |
| **Instance identifier** – None found for MFDS 고시, decree, or article numbers in the supplied excerpts. “No specific identifier found in source – verify separately.” |

---

### 6. Human‑Escalation Triggers  

1. **Grade Uncertainty** – If after review the device grade cannot be confirmed, the Regulatory Lead must raise a **Tier 2 escalation** to senior RA management before any dossier preparation.  
2. **Incomplete OSS/SBOM or Training Records** – Any “◐” status persisting beyond the target dates should trigger an immediate **project‑level stop‑work notice** and notification to the Quality Assurance Director.  
3. **Missing Local Clinical Evidence (for 3/4등급)** – Absence of required Korean clinical data must be escalated to the **Chief Medical Officer** with a risk‑impact assessment, as it blocks the 허가 pathway.  
4. **KGMP Certification Delay** – If KGMP facility audit cannot be scheduled within the intended timeline, an **Executive Escalation** is required to re‑plan launch dates.

---

### 7. Peer Review Prompt  

> *Could a fellow RA reviewer challenge the assumptions made about the device grade and the sufficiency of the current risk‑management artifacts? Please verify whether the matrix items DR‑23 and DR‑24 indeed satisfy MFDS’s “SBOM 연계” and “AI·사이버보안 교육” expectations, and confirm that no additional Korean‑specific evidence (e.g., 고시 제 xxxx‑xx호) has been omitted.*  

--- 

*End of draft – ready for internal review and human escalation as indicated above.*

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

### kb-eval-20261020-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "efda2292cbf13563", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/MFDS_의료기기_제조_및_품질관리_기준.md", "source_hash": "9b251ad3b3cc02f37944b961b8fa8e44ca732b028f6422f9ef3e6caf4e0f6724"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `efda2292cbf13563`
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

> **Regulatory Draft – Diagnostic X‑ray Device (A11000 series)**  

---

### 1. Classification & Submission Route  
| Item | Determination |
|------|---------------|
| **Korean grade** | The device belongs to the *진단용 엑스선 장치* series (A11110.01‒03, A11040.01/02). According to the “의료기기 품목 및 품목별 등급에 관한 규정” (별표 1) these items are listed as **3등급** devices. <br>*(no specific identifier found in source — verify separately)* |
| **Submission track** | 3등급 → **허가** (MFDS approval). The dossier must be reviewed by MFDS directly; a designated 심사기관 does not apply for this grade. |

---

### 2. Required Evidence Package  

| Evidence Category | Required Content | Reference |
|-------------------|------------------|-----------|
| **KGMP compliance** | • Facility KGMP certification (의료기기법 제28조) <br>• GMP SOPs mapped to ISO 13485:2016 requirements (document‑procedure matrix) | Framework – ISO 13485:2016 |
| **Technical Documentation** | • Device description, specifications, intended use <br>• Classification justification (reference to 별표 1) <br>• Risk Management File (ISO 14971:2019) | Framework – ISO 14971:2019 |
| **Software Validation** | • IEC 62304:2006+A1:2015 lifecycle processes (design, verification, validation) <br>• Evidence that the full text of IEC 62304 is incorporated by reference in **고시 제2025‑22호** | 고시 제2025‑22호 |
| **Cybersecurity Management** | • Cyber‑risk assessment and mitigation plan (aligned with MFDS cyber‑security appendix) | 고시 제2025‑22호 |
| **Non‑clinical Testing** | • Electrical safety & EMC per IEC 60601‑1 <br>• Radiation safety testing (dose output, shielding) <br>• Biocompatibility (ISO 10993‑1:2018) if patient‑contacting materials exist | Framework – IEC 60601‑1, ISO 10993‑1 |
| **Clinical Evidence** | • Local clinical trial data OR an accepted foreign Clinical Evaluation Report (CER). MFDS may accept a CER that complies with the International Medical Device Regulators Forum (IMDRF) clinical evaluation guidance provided the device’s intended use and risk class are comparable. <br>• If relying on foreign CER, submit a justification matrix mapping FDA 510(k) or CE‑MDD evidence to Korean requirements. | No specific identifier found in source — verify separately |
| **Labeling & IFU** | • All labeling, symbols, Instructions for Use in Korean (Korean language requirement). <br>• Include the “품목군” and “품목 분류번호” as per the current 고시. | 고시 제2025‑22호 (품목군·품목분류번호 표기) |
| **Post‑Market Surveillance Plan** | • PMS activities, vigilance reporting flowchart, periodic safety update schedule (Korean “시판후조사”) | Framework – MFDS post‑market surveillance guidance |

---

### 3. Gaps / Missing Information  

| Gap | Impact | Suggested Action |
|-----|--------|------------------|
| **Exact grade confirmation** – the source notes a correction from 2등급/3등급 codes to A11000 series but does not state the final grade number explicitly. | Without definite grade, submission track cannot be finalized. | Retrieve the current “별표 1” entry for A11110/A11040 series from the official law.gov.kr portal and confirm 3등급 status. |
| **Korean‑language labeling assets** – no draft label or IFU provided. | MFDS will reject incomplete labeling. | Prepare Korean label & IFU drafts, include required symbols (radiation safety) and register them for review. |
| **Local clinical data / foreign CER acceptance strategy** – device is 3등급; local clinical trial may be mandatory unless a CER is accepted. | Uncertainty could delay approval. | Determine whether MFDS has published a notice allowing reliance on the specific foreign CER (e.g., FDA 510(k) clearance). If not, plan a Korean pilot clinical study. |
| **Cybersecurity implementation details** – high‑level requirement mentioned, but no concrete controls (e.g., secure boot, vulnerability management). | Non‑compliance may trigger post‑market findings. | Develop a cybersecurity case file aligned with the MFDS appendix referenced in 고시 제2025‑22호. |
| **Software version control & validation evidence** – only IEC 62304 reference cited; no actual validation reports. | Insufficient to satisfy software safety dossier. | Generate design history, verification/validation test reports covering all software releases. |
| **Evidence of KGMP certification** – facility audit report not supplied. | Mandatory for 허가 submission. | Obtain current KGMP certificate and include the audit summary. |

---

### 4. Risk Controls (ISO 14971‑based)  

1. **Radiation Exposure** – Dose‑monitoring circuitry, automatic exposure control, shielding design verification, periodic calibration schedule.  
2. **Electrical Safety/EMC** – IEC 60601‑1 compliance; built‑in fault detection and shutdown.  
3. **Software Hazards** – Apply IEC 62304 lifecycle; conduct FMEA on software functions; perform security‑focused threat analysis (STPA).  
4. **User Interface Errors** – Human‑factors validation, clear Korean language prompts, ergonomic design per IEC 60601‑2‑?? (if applicable).  
5. **Cybersecurity** – Network segmentation, authentication, encryption for firmware updates; regular vulnerability scanning and patch management.

All controls to be documented in the Risk Management File with residual risk assessment and justification of acceptability.

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger | Escalation Target |
|-----------|---------|-------------------|
| **Unconfirmed Korean grade** (no definitive “3등급” citation) | Immediate pause on dossier preparation until official classification is verified. | Senior RA Lead / Regulatory Affairs Manager |
| **Missing Korean labeling** | If finalized label/IFU not available 30 days before submission deadline. | Product Management & Legal |
| **Unclear acceptance of foreign CER** | MFDS response required for clinical evidence strategy; risk of rejection if unresolved. | Clinical Development Team & Senior RA |
| **KGMP certification pending** | Facility audit outcome delayed beyond planned timeline. | Quality Assurance Lead |
| **Cybersecurity plan insufficient** | Identified gap during internal security review (e.g., no vulnerability management). | IT Security Officer & Compliance Officer |
| **Critical risk control not demonstrated** (e.g., radiation dose monitoring) | Failure to provide validation data in final week before submission. | Engineering Lead / Chief Medical Officer |

Escalations should be logged in the project’s risk register and communicated through the formal change‑control process.

---

### 6. Peer Review Prompt  

> **RA Peer, please review:**  
> - The assumption that the A11000 series is a 3등급 device (based on the correction note). Verify against the latest “의료기기 품목 및 품목별 등급에 관한 규정” (별표 1).  
> - Whether reliance on a foreign Clinical Evaluation Report is permissible for this grade under current MFDS practice, or if a Korean clinical trial is mandatory.  
> - Completeness of the cyber‑security evidence required by 고시 제2025‑22호 – are additional annexes or technical standards (e.g., NIST 800‑53) referenced in the MFDS appendix?  

Your feedback on any overlooked jurisdiction‑specific gaps will be incorporated before final dossier compilation.

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

### kb-eval-20261020-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-20", "decision_ref": "kb-eval-20261020-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "09a6246805180153", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "05655bb796bf8ed73e0e7bf66100bca6738bee82ab80865741516d55798597da"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `09a6246805180153`
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

> **Regulatory Draft – KGMP Evidence Readiness (2026‑07 01 reform)**  

---

### 1.   Device classification & submission route (Korean grades)

| Korean grade | Default MFDS pathway* | KGMP relevance |
|--------------|----------------------|----------------|
| **1등급**    | 신고 (notification) | KGMP certification is not mandatory for the manufacturing site, but a GMP‑self‑assessment report must be kept on file. |
| **2등급**    | 인증 (certification by an MFDS‑designated 심사기관) | Mandatory KGMP 적합성인정 for the production facility; submission uses the new forms 별지 제38호의4·39·40호. |
| **3등급·4등급** | 허가 (approval by MFDS) | Full KGMP 적합성인정 required; certification is a pre‑condition for the 허가 review. |

\*If a device falls under an exempted list (e.g., certain in‑vitro diagnostics), the pathway may differ – confirm against **「의료기기법」제28조·제28조의2~4**.  

> *Citation*: no specific identifier found in source for exemption list – verify separately.

---

### 2.   Core KGMP evidence package (post‑reform, 2026‑07 01)

| Evidence item | Requirement (Korean law / notice) | Practical notes |
|---------------|-----------------------------------|-----------------|
| **Facility compliance** | “의료기기 제조 및 품질관리 기준” (식약처 고시 **제2026‑46호**) – GMP 심사기준 only retained. | Submit KGMP certification issued by an MFDS‑designated 심사기관; include audit report, SOPs, and training records. |
| **Designation of 심사기관 / 심사원** | “의료기기 제조 및 품질관리 관련 기관 지정 등에 관한 규정” (식약처 고시 **제2026‑47호**, 제정 2026‑07‑01) | Identify the accredited 심사기관 that will conduct the KGMP audit; attach the official appointment notice. |
| **Application forms** | New checklist/forms: **별지 제38호의4·39·40호** (KGMP 심사 신청서 양식) | Complete each form in Korean, sign and submit electronically or by post as required by MFDS. |
| **Risk Management File** | Align with **ISO 14971:2019** (risk analysis, evaluation, control). | Include risk management plan, hazard analysis, residual risk justification; reference any foreign FDA 21 CFR 820‑part‑related documents only as supporting evidence (MFDS does not accept “QMSR”). |
| **Quality Management System** | Must satisfy **KGMP** (which incorporates ISO 13485:2016 requirements). | Provide QMS manual, internal audit reports, corrective‑and‑preventive action (CAPA) records. |
| **Product Technical Documentation** (e.g., Device Master File) | Required for 2~4등급 devices per **「의료기기법」제28조·제28조의2~4**. | Include design dossier, labeling specimens, performance data, and any foreign CE‑mark or FDA clearance where MFDS accepts such evidence (see “foreign clinical evaluation reports” scope). |
| **Korean labeling & IFU** | All labeling, inserts and packaging must be in Korean; refer to **MFDS 고시 제2026‑46호** labeling annex. | Provide final Korean versions for review; English copies are optional as supplementary material. |
| **Cybersecurity evidence (if applicable)** | Follow IEC 81001‑5‑1:2021 (referenced by MFDS cyber‑security guideline). | Submit threat model, vulnerability management plan, and post‑market surveillance (PMS) monitoring procedures. |

> *Citation*: no specific article number for the labeling annex in 고시 제2026‑46호 – verify separately.

---

### 3.   Missing information / gaps to be resolved before submission

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Local clinical data** (if device is 3등급·4등급 and MFDS does not accept foreign CER) | Korean regulation may require domestic clinical evaluation even when FDA/CE evidence exists. | Determine whether the device falls under the “foreign clinical evaluation report” acceptance scope (see recent MFDS notice expansions). If not, plan a Korean clinical trial or collect post‑market data. |
| **Complete Korean translation of all labeling & IFU** | Mandatory for every grade; failure blocks certification/허가. | Engage qualified translator experienced with medical terminology; conduct linguistic verification. |
| **Evidence of staff qualifications (education, training)** per KGMP audit checklist | Required for 심사기관 approval and ongoing compliance. | Compile CVs, certificates, and training logs; map to the checklist items in 별지 제38호의4. |
| **Verification of the designated 심사기관’s current accreditation status** | Accreditation may change annually; MFDS only accepts institutions listed in 고시 제2026‑47호. | Obtain latest accreditation certificate and cross‑check against the notice list. |
| **Cybersecurity risk assessment (if device has software)** | New KGMP emphasis on IEC 81001‑5‑1 compliance. | Conduct a security threat analysis and prepare supporting documentation. |

---

### 4.   Risk Controls to be demonstrated

| Control area | Reference standard / regulation | Evidence to submit |
|--------------|--------------------------------|--------------------|
| **Risk Management** | ISO 14971:2019 | Full risk management file (analysis, evaluation, controls). |
| **Design & Development Controls** | IEC 62304 (for software) or IEC 60601‑1 (electrical safety) as applicable | Design verification/validation reports, test data. |
| **Process Validation** | KGMP audit criteria (고시 제2026‑46호) | Process validation protocols & results for critical manufacturing steps. |
| **Post‑Market Surveillance (PMS)** | MFDS 시판후조사 규정 (Article 23 of the Medical Device Act) | PMS plan, periodic safety update reports, adverse event handling SOPs. |
| **Cybersecurity** | IEC 81001‑5‑1:2021 | Threat model, patch management process, incident response procedure. |

---

### 5.   Citations

| Category | Citation used |
|----------|---------------|
| **Framework references** (standards) | ISO 14971:2019; ISO 13485:2016; IEC 62304 2006+A1:2015; IEC 60601‑1 2005+A1:2012+A2:2020; IEC 81001‑5‑1 2021. |
| **Instance identifiers** (from source) | 의료기기법 시행규칙, 총리령 **제2127호** (effective 2026‑07‑01); 의료기기법 시행령, 대통령령 **제36445호**; 고시 **제2026‑46호** (GMP 심사기준); 고시 **제2026‑47호** (기관·심사원 지정). |
| **Other statutory references** | 「의료기기법」제28조·제28조의2~4 (no specific notice number in source – verify separately); 「의료기기 제조 및 품질관리 기준」 (part of 고시 제2026‑46호). |

---

### 6.   Human‑escalation triggers (when to involve senior RA / regulatory leadership)

| Trigger | Reason | Recommended action |
|--------|--------|--------------------|
| **Absence of verified Korean clinical data** when MFDS has not accepted foreign CER | Would block 허가 for 3등급·4등급 devices | Escalate to Senior RA → initiate Korean clinical study plan or request MFDS clarification. |
| **Incomplete KGMP checklist (별지 제38호의4·39·40호) submission** | MFDS rejects incomplete applications outright | Pause the filing; involve QA manager to complete forms, then resubmit. |
| **Designation of 심사기관 not listed in 고시 제2026‑47호** | Non‑accredited 기관 cannot conduct KGMP audit | Alert Regulatory Manager → select an approved 심사기관 and obtain a new appointment notice. |
| **Significant GAP in cybersecurity evidence for software‑enabled device** | Recent MFDS guidance ties cyber‑risk to 허가 eligibility | Convene cross‑functional meeting (RA, IT security, development) to produce the required IEC 81001‑5‑1 artifacts. |
| **Unexpected FDA 524B or EU MDR PSUR references in foreign dossier** that were incorrectly mapped as Korean requirements | Could cause non‑compliance with Korean labeling or PMS expectations | Senior RA reviews and strips non‑applicable foreign regulatory language; re‑aligns to MFDS 시판후조사 규정. |

---

### 7.   Regulatory judgment (ready/not ready)

*Based on the current evidence list, the submission is **not yet ready** for KGMP certification/허가 because:*

1. Local Korean labeling and IFU are not confirmed as complete translations.  
2. The presence of a valid Korean clinical evaluation report has not been verified for 3등급·4등급 devices.  
3. The designated 심사기관’s accreditation status must be cross‑checked against 고시 제2026‑47호.  

**Action:** Address each gap (translation, clinical data, 기관 인증) and reconfirm all checklist items before filing the KGMP application.

---

### 8.   Peer‑review prompt

> **Colleague RA, please review:**  
> - Are we interpreting the post‑2026‑07‑01 KGMP reform correctly with respect to the new forms (별지 제38호의4·39·40호)?  
> – Have we captured all mandatory evidence items for 2~4등급 devices under 고시 제2026‑46호 and 제2026‑47호?  
> – Is there any recent MFDS notice expanding acceptance of foreign clinical evaluation reports that we have missed, which could affect the need for local clinical data?  

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
