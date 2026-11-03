# KB Eval Checksheet - 2026-11-03 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261103-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "c1eeff974145cf5c", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "9035874d34b5edcdd28016407f6e15acef59268d534313b39dacbc6fa1f99f85"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c1eeff974145cf5c`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/FDA_AI_ML_2026_PCCP_%EC%9A%B4%EC%98%81_TPLC_%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8.md)
- Source hash: `9035874d34b5edcdd28016407f6e15acef59268d534313b39dacbc6fa1f99f85`
- Focus: SaMD change impact
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-09-18 (주간모니터 #17 — §9 추가: 방사선 CAD 510(k) 면제 청원 **거부** 확정, 91 FR 58817) / 2026-06-17 (#4 — §8 방사선 ML 정량영상 SW 분류) > 근거: https://www.federalregister.gov/documents/2026/06/17/2026-12166/medical-devices-radiology-devices-classification-of-the-radiological-machine-learning-based | https://www.fda.gov/regulatory-information/search-fda-guidance-docu...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Impact Assessment for a Radiology CAD SaMD Update**

---

### 1. Device Overview (derived from source)

| Item | Description |
|------|-------------|
| **Device type** | Machine‑learning based computer‑aided detection (CAD) software for radiological image analysis (quantitative imaging). |
| **Intended use** *(not explicitly in source – to be finalized)* | “Assist qualified health professionals in detecting/characterizing … on [modality] images” (typical CAD language). |
| **Regulatory status of similar devices** | *Radiology CAD 510(k) exemption petition was denied* – 91 FR 58817 (see source [1]). Therefore the device is **not exempt** and must be cleared via a traditional 510(k). |
| **Applicable FDA classification** | Class II, 21 CFR §892.2050 – *Medical image management and processing system* (software that performs CAD functions). This is a framework reference; no identifier appears in the source. |

---

### 2. Recommended Submission Route  

| Pathway | Rationale |
|--------|-----------|
| **Traditional 510(k) with Substantial Equivalence** | The FDA has denied exemption for radiology‑CAD (source [1]), indicating that the default pathway remains a conventional 510(k). A predicate device from the same product code (e.g., “MDS” – CAD) must be identified. |
| **Inclusion of a Predetermined Change Control Plan (PCCP)** | The source lists “업데이트 계획 시 PCCP” as required for post‑approval changes (source [2]). The PCCP should be submitted as part of the 510(k) to pre‑authorize future algorithm updates. |

---

### 3. Evidence Required for the 510(k) Package  

| Category | Specific Items (per FDA guidance & ISO/IEC standards) |
|----------|------------------------------------------------------|
| **Device Description** | Detailed block diagram, software architecture, major functions, description of the ML model type (e.g., CNN), and versioning. |
| **Intended Use Statement** | Precise clinical claim, target population, imaging modality, anatomic area. *Missing – must be defined.* |
| **Predicate Comparison** | Side‑by‑side table of device specifications, intended use, and performance claims versus the selected predicate (clearance number). *Missing – predicate not yet identified.* |
| **Analytical Performance & Verification** | • Algorithm accuracy, sensitivity, specificity on validation set.<br>• Data lineage: training / tuning / testing splits (source [2] emphasizes this).<br>• Reproducibility and robustness tests (e.g., variations in image acquisition). |
| **Clinical Evaluation** | Clinical study or retrospective analysis linking performance metrics to clinical outcomes; justification of statistical equivalence/non‑inferiority to predicate. |
| **Bias Analysis & Mitigation** | Bias assessment across demographics, imaging equipment, sites; documented mitigation strategies (source [2] highlights “편향 분석·완화”). |
| **Human–AI Workflow** | Description of how clinicians interact with the software, override capabilities, and decision‑making responsibilities (“Human‑AI 워크플로우” in source [2]). |
| **Risk Management File** | ISO 14971:2019 risk analysis, risk control measures, residual risk evaluation; classification of software hazards per IEC 62304. |
| **Usability Engineering** | IEC 62366‑1‑based user‑interface validation to ensure safe use in the intended workflow. |
| **Software Lifecycle Documentation** | Development plan, verification & validation summary, configuration management (ISO 13485–aligned QMSR). |
| **Post‑Market Surveillance Plan** | Ongoing performance monitoring, adverse event reporting procedures, and criteria for triggering a change request (source [2] includes “시판 후 모니터링”). |
| **Predetermined Change Control Plan (PCCP)** | Scope of anticipated changes, pre‑specified testing matrix, and decision tree for when FDA review is required. The PCCP guidance linked in source [1] provides the template. |
| **Labeling & UDI** | 21 CFR §801 labeling requirements; UDI placement per 21 CFR §830.10‑§830.60 (framework reference). |
| **Regulatory Submissions Forms** | FDA 510(k) Cover Sheet, Summary/Statement of Claim, Truthful and Accurate Statement, etc. |

---

### 4. Gaps / Missing Information (to be addressed before submission)

| Gap | Action Needed |
|-----|----------------|
| Exact *intended use* wording | Draft with clinical input; ensure alignment with predicate claims. |
| Predicate device identification & clearance number | Perform search in FDA’s 510(k) database for radiology CAD devices of the same product code. |
| Detailed dataset description (size, source institutions, patient demographics) | Provide de‑identified summary tables and justification of representativeness. |
| Performance thresholds linked to clinical claim | Define acceptable sensitivity/specificity margins; include statistical analysis plan. |
| Bias mitigation documentation (algorithmic fairness techniques) | Include quantitative results before/after mitigation. |
| Human factors validation protocol & report | Conduct formative/usability testing per IEC 62366‑1. |
| Post‑market monitoring metrics & escalation criteria | Define specific thresholds (e.g., drift in false‑positive rate > X % triggers a PCCP amendment). |
| Predetermined Change Control Plan scope | Identify which algorithmic changes are “anticipated” vs. “unanticipated.” |
| Labeling content (indications, contraindications, warnings) | Draft per 21 CFR §801 and FDA’s SaMD labeling guidance. |

---

### 5. Key Risk Controls (per ISO 14971 & IEC 62304)

1. **Algorithm performance degradation detection** – automated statistical monitoring; trigger alerts if key metrics deviate beyond pre‑set limits.  
2. **Human override & final decision authority** – UI design ensures clinician must confirm or reject CAD output before patient management decisions.  
3. **Fail‑safe mode** – If software crashes or yields “no result,” system defaults to “no assistance” and logs the event.  
4. **Cybersecurity safeguards** – Integrity checks, encrypted data transmission, periodic penetration testing (per FDA Cybersecurity Guidance).  
5. **Audit trails & version control** – All model updates recorded with timestamp, data set version, and justification (supporting PCCP).  
6. **Usability safety controls** – Color‑coded warnings, clear display of confidence scores to avoid misinterpretation.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required |
|--------|-----------------|
| **Algorithmic performance drift** (e.g., sensitivity ↓ > 5 % vs. baseline) | Immediate internal review; submit a **PCCP amendment** to FDA for pre‑market approval of the change. |
| **New data source added** that differs in demographics or imaging parameters without prior bias analysis | Pause deployment, conduct fresh bias assessment, update PCCP scope, and notify FDA if risk profile changes. |
| **Change to intended use** (e.g., new anatomic site or modality) | Submit a supplemental 510(k) (or full 510(k) if substantial change). |
| **Unexpected adverse event rate** exceeding post‑market surveillance thresholds (per PMA §803, but applied via FDA’s voluntary reporting for Class II) | File a Medical Device Report (MDR) under 21 CFR §803 and consider field correction/removal per 21 CFR §806. |
| **Failure of human‑AI handoff** (e.g., clinicians unable to override) | Immediate corrective action; update labeling & training; submit a **PCCP change** if workflow modification is needed. |

---

### 7. Citations  

| Item | Source citation |
|------|-----------------|
| FDA denial of CAD exemption, 91 FR 58817 | Excerpt [1] (“방사선 CAD 510(k) 면제 청원 **거부** 확정, 91 FR 58817”) |
| Guidance on Predetermined Change Control Plan (PCCP) | Excerpt [1] – FDA guidance links listed under “marketing‑submission‑recommendations‑predetermined‑change‑control‑plan‑artificial‑intelligence”. |
| Required submission contents (bias analysis, human‑AI workflow, post‑market monitoring, PCCP) | Excerpt [2] (“편향 분석·완화”, “Human‑AI 워크플로우”, “시판 후 모니터링”, “업데이트 계획 시 PCCP”). |
| Classification of radiology ML software (Class II, §892.2050) | Framework reference – 21 CFR §892.2050 (medical image management and processing systems). No specific identifier appears in the source. |
| Standard editions for risk management & QMSR | Framework references: ISO 14971:2019; ISO 13485:2016; IEC 62304 2006+A1:2015; IEC 62366‑1 2015+A1:2020 (current editions per knowledge base). |

*No additional instance identifiers were present in the provided excerpts; all other citations are framework references.*

---

### 8. Human Review & Escalation Checklist  

- [ ] Verify intended use statement and confirm it aligns with a cleared predicate.  
- [ ] Identify and document the exact predicate device (clearance number).  
- [ ] Complete missing dataset, bias analysis, and performance threshold documentation.  
- [ ] Draft and obtain internal sign‑off on the PCCP; ensure scope matches FDA guidance.  
- [ ] Conduct usability testing per IEC 62366‑1 and incorporate results.  
- [ ] Prepare post‑market surveillance plan with quantitative escalation thresholds.  

**If any of the above items remain unresolved, pause submission preparation and elevate to senior RA leadership for additional guidance.**

---

### 9. Peer Review Prompt  

> *Colleague, please review the assumptions regarding (1) classification under §892.2050, (2) completeness of the evidence matrix relative to FDA’s current AI/ML guidance, and (3) any jurisdiction‑specific gaps (e.g., UDI labeling, QMSR compliance). Highlight any missing regulatory citations or required supplemental information that could affect the 510(k) strategy.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1034015376307744884`

> > 최종 갱신: 2026-09-18 (주간모니터 #17 — §9 추가: 방사선 CAD 510(k) 면제 청원 **거부** 확정, 91 FR 58817) / 2026-06-17 (#4 — §8 방사선 ML 정량영상 SW 분류) > 근거: https://www.federalregister.gov/documents/2026/06/17/2026-12166/medical-devices-radiology-devices-classification-of-the-radiological-machine-learning-based | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing | https://www.federal...

2. Chunk `1132891599852736913`

> ### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. ---

### kb-eval-20261103-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "b0c302332e67e1b3", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `b0c302332e67e1b3`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/PCCP_AI_Device_%EC%9E%91%EC%84%B1%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6`
- Focus: SaMD change impact
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `PCCP_AI_Device_작성가이드.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-sof...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – SaMD AI Change‑Control Impact Assessment**

---

### 1. Device Classification & Submission Pathway  
| Attribute | Determination |
|-----------|----------------|
| **Device type** | Software as a Medical Device (SaMD) incorporating AI/ML. |
| **Regulatory panel** | Dependent on intended use; most SaMD are classified under the FDA’s appropriate medical device panel (e.g., radiology → 21 CFR §892, clinical decision support → 21 CFR §809).  *No specific panel cited in source – verify with intended‑use claim.* |
| **Risk class** | • If the software provides diagnostic or therapeutic recommendations → **Class II** (most AI/ML SaMD). <br>• If it is life‑supporting, high‑risk decision making without human oversight → **Class III**.  *Intended use must be supplied to lock classification.* |
| **Premarket submission** | • Existing legally marketed predicate ⇒ **510(k) – Substantial equivalence** (21 CFR §807). <br>• No predicate or novel algorithmic function ⇒ **De Novo** request (21 CFR §806). |

---

### 2. Required Evidence Package  

| Category | Required Content |
|----------|------------------|
| **Device Description** | Detailed intended‑use statement, functional block diagram, software architecture, versioning. |
| **Predicate Comparison (if 510(k))** | Predicate 510(k) number, summary of similarities/differences, justification for equivalence. *No predicate ID in source – verify separately.* |
| **Quality Management System** | Compliance with **21 CFR Part 820** (QMSR effective Feb 2026, ISO 13485:2016‑aligned). Include SOPs for change control, software lifecycle, risk management. |
| **Software Lifecycle & Validation** | IEC 62304:2006+A1:2015 compliance; design history file, verification & validation plans/results, unit/integration testing records. |
| **Risk Management** | ISO 14971:2019‑based risk analysis (hazard identification, severity/likelihood scoring, mitigations). Document residual risk evaluation. |
| **Clinical Performance Data** | Clinical study or real‑world evidence demonstrating that the device meets pre‑specified performance criteria for its intended use. |
| **Predetermined Change Control Plan (PCCP)** *(per FDA AI/ML guidance – see source)* | 1️⃣ **Data Management** – procedures for data collection, curation, version control, bias mitigation.<br>2️⃣ **Retraining Practices** – trigger conditions, retraining workflow, rollback strategy.<br>3️⃣ **Performance Evaluation** – pre‑defined acceptance criteria, V&V methodology, statistical significance requirements.<br>4️⃣ **Updated Procedures** – user/clinician communication plan, real‑world monitoring, IFU revision process. <br>*Source excerpt lists these four mandatory items.* |
| **Labeling & UDI** | 21 CFR §801 labeling content; 21 CFR §830 (UDI) label and GUDID submission. |
| **Cybersecurity** | Threat model, vulnerability mitigation, post‑market monitoring plan (aligned with FDA Cybersecurity Guidance). |
| **Post‑Market Surveillance** | Voluntary correction/removal plan under 21 CFR §806; adverse event reporting per 21 CFR §803. |

---

### 3. Missing Information (to be obtained before submission)

| Item | Why needed |
|------|------------|
| Precise **intended use / indication** (e.g., “assist radiologists in detecting lung nodules”) | Determines panel, classification, predicate search. |
| **Predicate device number** (if pursuing 510(k)) or justification for De Novo route | Required for substantial‑equivalence argument. |
| **Risk classification rationale** (risk matrix, level of decision impact) | Drives submission type and evidence depth. |
| **Labeling draft** (including intended user, contraindications, warnings) | Needed for 21 CFR §801 compliance. |
| **UDI strategy** (device identifier format, label layout) | Required under Part 830. |
| **Cybersecurity threat analysis** (catalog of identified threats & mitigations) | FDA expects documented controls. |
| **Clinical performance plan** (study protocol or real‑world data sources) | Evidence of safety/effectiveness. |
| **Algorithm change limits** (numeric thresholds triggering a new PCCP submission) | Determines when a modification requires FDA review vs. internal control only. |

*All missing items are not present in the source excerpt; “no specific identifier found in source – verify separately.”*

---

### 4. Core Risk Controls (aligned to standards)

| Control | Standard / Guidance |
|---------|----------------------|
| **Software lifecycle & documentation** | IEC 62304:2006+A1:2015 |
| **Usability / Human factors engineering** | IEC 62366‑1:2015+A1:2020 |
| **Risk management process** | ISO 14971:2019 (Amd 1:2024 updates) |
| **Bias detection & mitigation** | FDA AI/ML PCCP guidance (Data Management element). |
| **Performance monitoring / statistical control** | PCCP Performance Evaluation element; V&V methods per IEC 62304. |
| **Rollback mechanism for retraining** | PCCP Retraining Practices element. |
| **User communication of updates** | PCCP Updated Procedures element, labeling change management per 21 CFR §801. |

---

### 5. Key Citations  

| Source Type | Reference |
|-------------|-----------|
| **Framework – Regulation** | 21 CFR Part 820 (QMSR); 21 CFR Part 807 (510(k)); 21 CFR Part 806 (correction/removal); 21 CFR Part 803 (MDR reporting). |
| **Framework – Standards** | ISO 14971:2019; IEC 62304:2006+A1:2015; IEC 62366‑1:2015+A1:2020. |
| **Instance – Guidance URLs** | FDA “Predetermined Change Control Plan for AI/ML Devices” (final guidance, Dec 2024) – source excerpt lists the URL and the four mandatory PCCP elements. *No CFR section number provided in source; note accordingly.* |
| **Instance – Section on Modification Protocol** | Table of 4 required items (Data Management, Retraining Practices, Performance Evaluation, Updated Procedures) – taken directly from source chunk 198015203798949382. |

*All instance identifiers are drawn verbatim from the source; no invented numbers.*

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Absence of a clear predicate** or decision to pursue **De Novo** | Senior RA must convene a classification meeting and obtain senior management approval before filing. |
| **Risk class determined as Class III** (high‑risk algorithm, no human oversight) | Immediate escalation to Director of Regulatory Affairs; consider PMA pathway. |
| **Performance evaluation fails pre‑specified acceptance criteria** during validation or post‑market monitoring | Suspend deployment, conduct root‑cause analysis, and submit a corrective action report per 21 CFR §806. |
| **Algorithm change exceeds PCCP predefined limits** (e.g., new data source, altered model architecture) | Prepare and submit a supplemental 510(k) (if already cleared) or a new 510(k)/De Novo as appropriate. |
| **Serious adverse event linked to the SaMD** reported in the field | Initiate FDA‑required MDR report under 21 CFR §803 within 30 days; notify senior leadership and legal. |
| **Cybersecurity breach impacting device functionality or data integrity** | Escalate to CISO & Regulatory Lead; file a safety notice per 21 CFR §806 and consider FDA notification if patient risk exists. |

---

### 7. Reusable RA Judgment (to be recorded in the knowledge base)

> *When evaluating an AI/ML SaMD, always verify the intended‑use claim before assigning panel or class. If the device incorporates a learning algorithm that will be updated after market launch, the FDA requires a **Predetermined Change Control Plan (PCCP)** containing four specific elements: (1) Data Management, (2) Retraining Practices, (3) Performance Evaluation, and (4) Updated Procedures. Absence of any one element constitutes an incomplete submission per the December 2024 FDA AI/ML guidance.*  

---

### 8. Peer‑Review Prompt

> **Colleague, please review:**  
> 1. Are we assuming the correct regulatory panel without a stated intended use?  
> 2. Does the missing predicate information affect our recommendation of a 510(k) versus De Novo pathway?  
> 3. Have we captured all FDA‑required elements for a PCCP, or are there additional items (e.g., change impact analysis, post‑implementation monitoring) in later guidance updates that need inclusion?  
> 4. Are any EU/Korean references inadvertently influencing this US‑focused draft?

--- 

*End of regulatory draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> ① De Novo 근거를 "21 CFR §806"으로 인용 — §806는 교정·회수 보고이며 De Novo는 Part 860/§807.87? (코퍼스 표준: 21 CFR 860, FD&C §513(f)(2)) ② "Voluntary correction/removal plan under 21 CFR §806" — §806는 의무 보고(10-29·11-02와 동일 계열).

**Source Excerpts**

1. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

2. Chunk `198015203798949382`

> ### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---

### kb-eval-20261103-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "3bef611fb54f41d6", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `3bef611fb54f41d6`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_03_Performance_Testing_Bench_Test.md)
- Source hash: `9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_03_Performance_Testing_Bench_Test.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Imaging‑Room GUI Software (SaMD)**  

| Item | Assessment & Required Actions |
|------|------------------------------|
| **Device Classification** | • Class II under 21 CFR §892.2050 (Image Processing Software). <br>• No indication of a higher‐risk subclass; IEC 62304 analysis (see below) points to **Software‑Class B** (hazard → “moderate” risk). |
| **Regulatory Submission Pathway** | • 510(k) Premarket Notification (most efficient route for a Class II SaMD). <br>• Reference: 21 CFR §807.92 (substantial equivalence). |
| **Core Submission Content** (per FDA “Content of Premarket Submissions for Device Software Functions” guidance, 14 Jun 2023) | 1. **Device Description & Intended Use** – concise statement of clinical context and imaging workflow.<br>2. **Predicate Device Identification** – 510(k) number(s) for a cleared image‑processing/display software with comparable functionality (e.g., a DICOM viewer + basic processing).<br>3. **Software Functional Specification** – requirements, architecture diagram, traceability matrix (Source [2] shows RMS file).<br>4. **Risk Management File** – IEC 62304 hazard analysis linked to ISO 14971 risk controls (see “Risk Controls” below).<br>5. **Cybersecurity Documentation** – per FDA “Cybersecurity in Medical Devices” guidance (27 Sep 2023). Include threat model, mitigation strategy, post‑market update plan.<br>6. **Verification & Validation Evidence** – Unit, Integration, System test results; Performance testing (Section G of eSTAR) with validation dataset description and anomaly log (Source [2]).<br>7. **Labeling & UDI** – 21 CFR §801 labeling requirements; 21 CFR §830.10‑§830.60 UDI label content and GUDID submission.<br>8. **QMS Documentation** – Part 820 (design controls, software development records). |
| **Evidence Already Identified in Source** | • eSTAR “Section G” package list (Source [2]) provides the expected documentation set for software performance testing.<br>• Classification basis (21 CFR §892.2050) and IEC 62304 reference (Source [1]). |
| **Missing / Insufficient Information** | 1. **Intended Use Statement** – explicit clinical indication, user population, setting.<br>2. **Predicate Device(s)** – clearance numbers & comparison table.<br>3. **Software Architecture Detail** – flowcharts, module descriptions beyond the high‑level list.<br>4. **Usability/ Human Factors Data** – if UI influences diagnostic decisions (required for “intended use” involving interpretation).<br>5. **Post‑Market Surveillance / Cybersecurity Update Plan** – schedule, responsible party, vulnerability management process.<br>6. **Labeling Samples (IFU, Quick‑Start Guide)** – FDA expects drafts in the 510(k) package.<br>7. **UDI Label Mock‑up** – format, device identifier, production identifier.<br>8. **Registration & Listing Confirmation** – Establishment registration under 21 CFR §807.40 and product listing (§807.92). |
| **Risk Controls (per IEC 62304 & ISO 14971)** | • **Software Hazard Analysis** – identify hazards (e.g., incorrect image rendering, loss of data, erroneous window/level settings).<br>• **Classification** – Class B → requires **design verification**, **risk control measures**, and **software release testing**.<br>• **Risk Control Measures** – input validation, error handling, redundancy for critical functions, audit trails, user alerts for out‑of‑range parameters.<br>• **Verification/Validation Tests** – documented in the eSTAR package (unit, integration, system, performance).<br>• **Cybersecurity Controls** – authentication, encryption of data at rest/in transit, secure update mechanism, vulnerability monitoring. |
| **Key Citations** | • 21 CFR §892.2050 – Image Processing Software (Class II). <br>• FDA Guidance “Content of Premarket Submissions for Device Software Functions” (14 Jun 2023) – framework reference. <br>• FDA Guidance “Cybersecurity in Medical Devices” (27 Sep 2023) – framework reference. <br>• IEC 62304:2006+A1:2015 – software lifecycle processes (framework reference). <br>• No specific identifier found in source — verify separately for any predicate 510(k) numbers, labeling text, and UDI format requirements. |
| **Human‑Escalation Triggers** | 1. **Predicate Ambiguity** – if no cleared device matches the functional scope, consider a De Novo request; flag to senior regulatory lead.<br>2. **Risk Management Gaps** – missing hazard analysis or inadequately addressed Class C hazards → pause submission and engage risk‑engineer.<br>3. **Cybersecurity Deficiency** – lack of vulnerability management plan → route to cybersecurity specialist before filing.<br>4. **Incomplete eSTAR Package** – any missing test artefacts (e.g., integration test results) → hold for QA review.<br>5. **UDI/Labeling Non‑conformance** – if label mock‑up fails 21 CFR §830 checks, refer to labeling lead.<br>6. **QMS Documentation Gaps** – absent design‑control records per Part 820 → initiate corrective action plan with QMS manager. |
| **Next Steps (Actionable)** | 1. Draft intended use & predicate comparison matrix.<br>2. Complete software architecture diagrams and update the Requirements Traceability Matrix.<br>3. Produce risk analysis file (IEC 62304 hazard log + ISO 14971 risk control plan).<br>4. Assemble full eSTAR Section G artefacts; verify completeness against FDA guidance checklist.<br>5. Create labeling draft & UDI label prototype; run internal 830 compliance check.<br>6. Schedule cybersecurity review meeting (include IT‑security lead). <br>7. Submit for senior RA sign‑off once all triggers cleared. |

---  

**Peer Review Prompt**  
*Please review the assumptions above, especially the identification of a suitable predicate device and any potential gaps where EU/Korean regulatory concepts may have been unintentionally merged into the US pathway. Confirm that all cited framework references are appropriate for a Class II SaMD and flag any jurisdiction‑specific omissions.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> 경로 근거 "21 CFR §807.92 (substantial equivalence)" — §807.92는 Summary/Statement 조항, SE 결정은 §807.100(a). 반복 패턴(10-28 us-001/003 이후 3회차).

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

### kb-eval-20261103-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "eaf946e5258ca8cd", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md", "source_hash": "17067eef9c351571ca7c8dedcea62a4c6b790ae298cec359778dca145c690031"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `eaf946e5258ca8cd`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_05_Software_Section.md)
- Source hash: `17067eef9c351571ca7c8dedcea62a4c6b790ae298cec359778dca145c690031`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_05_Software_Section.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. --- + SOUP (IEC 62304) | SOUP 목록 (IEC 62304...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – SaMD Change Impact Assessment**

---

### 1. Device Classification & Submission Pathway  
- **Regulatory Class:** Class II (Software as a Medical Device that provides diagnostic or therapeutic information) → subject to **21 CFR §807** 510(k) requirements.  
- **Primary Predicate:** Identify an already‑cleared 510(k) for the same clinical function and software architecture (e.g., a cleared imaging analysis tool). *No specific predicate number is supplied in the source – verify separately.*  

### 2. Submission Type
| Change | FDA Pathway |
|--------|------------|
| Minor software update (no new intended use, no change to risk level) | **Traditional 510(k)** with updated Software Description and Risk Management File. |
| Substantial modification that alters risk profile or algorithm performance | **Special 510(k)** (if the device is already cleared) or a **new Traditional 510(k)** demonstrating substantial equivalence. |
| Introduction of AI/ML adaptive learning beyond pre‑specified limits | Require a **Predetermined Change Control Plan (PCCP)** per FDA’s Dec 2024 guidance; may be submitted as part of a Special 510(k) or via a separate **Supplement** to the original 510(k). *Source mentions PCCP*【2】.  

### 3. Core Evidentiary Requirements  

| Requirement | Content | Source / Standard |
|-------------|---------|-------------------|
| **Risk Management File (RMF)** | • Risk Management Plan with acceptance criteria <br>• Hazard analysis, risk evaluation, risk controls, residual risk determination <br>• Traceability matrix linking hazards → controls → verification activities | ISO 14971:2019 (cited in source)【1】; linkage to IEC 62304 §7 (source)【1】 |
| **Software Development Lifecycle Documentation** | • Software Requirement Specification (SRS) <br>• Architecture / Design Description (incl. module decomposition) <br>• Verification & Validation plan and reports (unit, integration, system testing) | IEC 62304 2006+A1:2015 (standard reference – no specific identifier in source). |
| **Software Bill of Materials (SBOM)** | Complete enumeration of third‑party components, including open‑source (SOUP) items. Required under FDA “524B” guidance. | Source lists SBOM & SOUP requirement【2】. |
| **Predetermined Change Control Plan (PCCP)** (if AI/ML adaptive) | • Defined pre‑specified change algorithm <br>• Monitoring plan, performance metrics, and post‑market data collection <br>• FDA‑approved change control documentation | FDA Final Guidance Dec 2024 – “Predetermined Change Control Plan (PCCP)” (source)【2】. |
| **Labeling & UDI** | • Indications for use, contraindications, user instructions, and software version labeling <br>• Unique Device Identifier on label/ packaging per 21 CFR §830.10‑§830.60 | Part 820 QMS requirements (general) & Part 830 UDI provisions – standard references, no specific numbers in source. |
| **Human Factors / Usability Validation** | Evidence that the UI and interaction flow support safe use, especially for AI/ML outputs. | IEC 62366‑1 2015+A1:2020 (standard reference). |

### 4. Identified Missing Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Predicate device number** | Needed to complete the substantial equivalence argument. | Search FDA 510(k) database for a cleared SaMD with identical intended use and similar algorithmic architecture; document clearance number. |
| **Detailed description of AI/ML change scope** (e.g., learning mode, re‑training triggers) | Determines whether PCCP is sufficient or a new 510(k) is required. | Provide a clear statement of the adaptive behavior limits and map to PCCP elements. |
| **SOUP component list with provenance** | Required for SBOM compliance; impacts cybersecurity risk assessment. | Compile a Bill of Materials including version, license, known vulnerabilities (e.g., via Snyk or NVD). |
| **Clinical performance data for the updated algorithm** (if performance changes) | Must support claim that the device remains safe and effective. | Conduct retrospective analysis or prospective study; include statistical plan. |
| **Verification of risk controls post‑change** (traceability matrix update) | Ensures residual risk remains acceptable after modification. | Update RMF and provide verification test results linking each control to the revised hazard. |

### 5. Risk Controls & Verification  

1. **Software Hazard Identification** – Perform updated failure mode & effects analysis (FMEA) focusing on AI/ML output drift.  
2. **Mitigation Strategies** – Implement runtime monitoring, anomaly detection, and a “human‑in‑the‑loop” override for outlier predictions.  
3. **Verification Activities** – Unit tests for each modified module; integration testing of the AI pipeline; system validation using representative clinical data sets. Traceability to RMF via matrix (source indicates such a matrix is required)【1】.  

### 6. Legal / CFR Citations (framework references)  

| Topic | Citation |
|-------|----------|
| Device classification & 510(k) pathway | **21 CFR §807** (Premarket Notification). |
| Quality Management System requirements | **21 CFR §820**. |
| Unique Device Identifier requirements | **21 CFR §830.10‑§830.60**. |
| Risk management process | ISO 14971:2019 (no identifier needed). |
| Software life‑cycle processes | IEC 62304 2006+A1:2015 (no identifier needed). |
| Usability engineering | IEC 62366‑1 2015+A1:2020 (no identifier needed). |
| AI/ML change control guidance | FDA “Predetermined Change Control Plan (PCCP)” Final Guidance, Dec 2024 (source)【2】. |

### 7. Human‑Escalation Triggers  

| Situation | Trigger for senior RA / regulatory counsel |
|-----------|--------------------------------------------|
| **No suitable predicate identified** – must decide between new 510(k) or De Novo pathway. |
| **Proposed AI/ML change exceeds pre‑specified limits in PCCP** – requires FDA Pre‑Submission (Q‑Submission) and possibly a new Traditional 510(k). |
| **Residual risk after change is judged unacceptable** – necessitates redesign or additional mitigations before filing. |
| **Significant SOUP vulnerability discovered post‑release** – initiate Field Safety Notice under **21 CFR §806**, and assess need for corrective action reporting. |
| **FDA issues an Additional Information (AI) request exceeding 180 days to respond** – senior RA must prioritize resources and consider filing a supplement or re‑submission strategy. |

---

### 8. Next Steps  

1. **Predicate Search & Clearance Number Confirmation** – assign to analyst, verify separately.  
2. **Produce Updated RMF**, including traceability matrix, risk analysis for new AI/ML behavior.  
3. **Compile SBOM & SOUP List** with version control.  
4. **Draft PCCP** (if applicable) and attach to Special 510(k) submission package.  
5. **Prepare clinical performance data plan** aligned with FDA expectations for the updated algorithm.  

---

#### Peer‑Review Prompt
> *Colleague, please review: (1) the adequacy of the identified predicate search approach; (2) whether all AI/ML change scenarios have been captured vis‑à‑vis the PCCP guidance; and (3) any U.S.–specific gaps in cybersecurity or post‑market surveillance that may affect the submission strategy.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

### kb-eval-20261103-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "561774b6ad9d5a3e", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `561774b6ad9d5a3e`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_02_Substantial_Equivalence.md)
- Source hash: `3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_02_Substantial_Equivalence.md`는 FDA 510(k) substantial equivalence와 predicate 비교 항목을 정리한 eSTAR 작성 문서입니다.
- 현재 excerpt 핵심: ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medi...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `SaMD change impact` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `SaMD change impact`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - software/AI/cyber 변경이 submission route, PCCP/change control, validation, risk controls에 미치는 영향을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Imaging Workstation Software (SaMD)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|----------------|
| **Regulatory panel** | Radiology / imaging devices → **21 CFR Part 892** (source‑based knowledge). |
| **Class** | Class II – “Medical image management and processing system” → **§892.2050** (fact). |
| **Primary submission route** | **510(k) Premarket Notification** with a substantial‑equivalence argument. |
| **Alternative if no suitable predicate** | Consider **De Novo classification** or a PMA only if the device is Class III (unlikely for standard image workstations). |

---

### 2. Required Evidence Package  

| Evidence Category | Specific Items | Source Reference / Note |
|-------------------|----------------|--------------------------|
| **Predicate Selection** | • Identify a primary predicate cleared within the past **5 years**; if older than 7 years, provide additional justification (modern‑use trend). <br>• Verify that the predicate is still marketed (not retired/discontinued). <br>• Confirm no recall or safety communication on the predicate (MAUDE/Recall DB). <br>• Perform side‑by‑side comparison of **Indications for Use** – must be identical or narrower. <br>• List all technical differences and supply justification data per item. | Checklist in excerpt [1]; “no specific identifier found in source — verify separately” for actual predicate K‑numbers. |
| **Software Documentation Level** | • Declare documentation level (Basic vs Enhanced) per FDA 2023 Software Guidance. <br>• Provide IEC 62304 development lifecycle documentation; assign Safety Class (A/B/C). | Excerpt [2] – “Software Level of Documentation (FDA 2023 SW guidance ‘Basic/Enhanced’) – IEC 62304 Safety Class (A/B/C)”. |
| **Functional Specification** | • Detailed list of functions: Acquisition, Processing, Display, Storage, Transfer, Worklist, QA Tools. <br>• Description of any **AI/ML module** and associated **Predetermined Change Control Plan (PCCP)** if present. | Excerpt [2] – function list; “AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정”. |
| **Interoperability & Standards Conformance** | • DICOM conformance statement covering Storage SCU/SCP, Worklist SCU, MPPS, Print SCU, etc. <br>• HL7 FHIR / IHE profile support (if claimed). <br>• Provide supported OS and minimum hardware requirements. | Excerpt [2] – “DICOM 적합성 진술서 … Interoperability (HL7 FHIR, IHE profiles)”. |
| **Cybersecurity** | • Authentication mechanisms, encryption, audit‑log strategy, secure update path. <br>• SBOM in SPDX or CycloneDX format. | Excerpt [2] – “보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) – SBOM 제공 형식”. |
| **Risk Management** | • ISO 14971:2019 risk analysis & mitigations (including software‑specific hazards). <br>• IEC 62304 verification/validation test reports. | General regulatory requirement; no specific identifier in source. |
| **Labeling & UDI** | • Label & IFU consistent with §801 (labeling) and §830 (UDI) requirements. <br>• UDI carrier on device label/package, entry into GUDID. | Part 801 & Part 830 – factual citations. |
| **Quality Management System** | • QMS compliant with **21 CFR Part 820** (effective Feb 2026, ISO 13485‑aligned). <br>• SOPs covering software lifecycle, change control, post‑market surveillance. | Part 820 – fact. |
| **Performance & Clinical Validation** | • Bench testing for image quality, latency, data integrity. <br>• Usability testing with target users; if AI/ML claims diagnostic assistance, consider limited clinical validation per FDA’s “Good Machine Learning Practice” guidance (2024). | No identifier in source – verify separately. |
| **Post‑Market Surveillance Plan** | • Routine monitoring for software updates, adverse events (21 CFR 803), and field corrections/removals (21 CFR 806). | Part 803 & 806 – factual. |

---

### 3. Missing Information (to be obtained before filing)

| Gap | Required Action |
|-----|-----------------|
| **Predicate device identifier(s)** (K‑numbers, 510(k) numbers) and their clearance dates. | Search FDA 510(k) database per checklist [1]; document K‑numbers. |
| **Exact intended use statement** for the new software (IFU text). | Draft IFU; compare to predicate wording. |
| **Safety class assignment (A/B/C)** under IEC 62304 with rationale. | Perform software hazard analysis. |
| **Evidence of AI/ML module’s change‑control plan** (PCCP) if any ML component is present. | Develop PCCP or confirm none exists. |
| **Cybersecurity risk assessment report** and detailed SBOM. | Conduct FDA‑aligned cybersecurity assessment; generate SPDX/CycloneDX file. |
| **Performance test data** (e.g., DICOM compliance, image processing accuracy, latency). | Execute verification/validation protocols; collect quantitative results. |
| **Usability/Human factors testing results** for the GUI. | Conduct formative and summative usability studies per IEC 62366‑1. |
| **QMS documentation excerpts** (SOPs, design history file) showing compliance with Part 820/QM SR. | Compile relevant SOPs and records. |

---

### 4. Core Risk Controls to Highlight in the 510(k)

1. **Software Development Lifecycle (IEC 62304)** – documented processes for planning, requirements, design, implementation, verification, validation, maintenance.
2. **Risk Management (ISO 14971:2019)** – hazard identification, risk estimation, mitigation, residual risk evaluation; specific controls for:
   * Image data corruption/integrity loss
   * Unauthorized access / cyber‑attack
   * Incorrect AI/ML output (if applicable)
3. **Cybersecurity Controls** – authentication, encryption of transmitted/stored DICOM objects, audit logging, secure OTA update mechanism.
4. **DICOM Conformance** – adherence to relevant SOPs for SCU/SCP services; validation against IHE profiles.
5. **Usability Safeguards** – UI design per IEC 62366‑1 to prevent operator error (e.g., clear worklist management, confirmation dialogs).
6. **Post‑Market Surveillance** – procedures for monitoring software updates, field safety notices, adverse event reporting.

---

### 5. Key Citations  

| Type | Citation |
|------|----------|
| **Framework / Regulation** | 21 CFR Part 892 §892.2050 (Class II “Medical image management and processing system”). |
| **Framework** | 21 CFR Part 807 – Premarket Notification (510(k)). |
| **Framework** | 21 CFR Part 820 – Quality Management System Regulation (effective Feb 2026). |
| **Framework** | 21 CFR Part 830 – Unique Device Identification (UDI) requirements. |
| **Framework** | ISO 14971:2019, ISO 13485:2016, IEC 62304:2006+A1:2015, IEC 62366‑1:2015+A1:2020 (risk & usability). |
| **Source excerpt – Predicate checklist** | Excerpt [1] – “Predicate 선정 실무 체크리스트 … 최근 5년 내 clearance 우선…”. |
| **Source excerpt – Software documentation** | Excerpt [2] – “4.3 촬영실 GUI SW (Imaging Workstation SW) – Software Level of Documentation … IEC 62304 Safety Class (A/B/C)… AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정… DICOM 적합성 진술서… 보안 조치 … SBOM 제공 형식”. |
| **No specific device identifiers** | “no specific identifier found in source — verify separately” for predicate numbers, recall IDs, etc. |

---

### 6. Human‑Escalation Triggers  

| Situation | Action Required (Human RA) |
|-----------|----------------------------|
| **No suitable recent predicate** (≤ 5 yr, still marketed, no recalls) after exhaustive search. | Escalate to senior RA/Regulatory Lead → consider **De Novo** or PMA pathway. |
| **AI/ML module present** but PCCP not yet defined. | Senior AI/ML specialist and RA must develop a **Predetermined Change Control Plan (PCCP)** before submission. |
| **Safety Class C (highest risk) under IEC 62304** identified. | Escalate to senior RA for possible **Class III** assessment → may require PMA. |
| **Cybersecurity controls insufficient** per FDA’s 2023 Software Guidance. | Immediate remediation; senior RA sign‑off before filing. |
| **Significant technical differences** with predicate that cannot be justified with data. | Conduct additional bench/clinical studies; senior RA must approve the justification narrative. |
| **Incomplete or missing QMS documentation** (e.g., SOPs, design history). | QA/QMS lead to provide missing artifacts before 510(k) assembly. |

---

### 7. Bottom‑Line Regulatory Judgment  

- The imaging workstation software is a **Class II SaMD**, cleared via **510(k)** with substantial equivalence to an appropriately recent and still‑marketed predicate.  
- A complete submission must include the evidence items listed in Section 2, address all gaps identified in Section 3, and embed the risk controls of Section 4.  
- Immediate human escalation is required if any of the triggers in Section 6 arise; otherwise the draft 510(k) package can proceed to compilation for FDA review.

---

**Peer‑Review Prompt (for another RA):**  

> Please challenge the assumptions above:  
> • Are we confident that §892.2050 fully captures this workstation’s intended use, or might a different subsection apply?  
> • Does the checklist in excerpt [1] miss any recent FDA guidance on “split predicates” or the newer “use of predicates” modernization policy?  
> • Is the AI/ML PCCP requirement adequately addressed given the 2024 FDA guidance on predetermined change control?  
> • Have we accounted for all cybersecurity expectations under the 2023 Software Guidance, especially regarding post‑market updates?  

Your feedback will ensure the submission strategy is robust and jurisdictionally sound.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

## ra_eu

### kb-eval-20261103-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "01a0f04eac42dc6a", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `01a0f04eac42dc6a`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `fca0891fdb985565c0693f44d2a6ca9a5822e159de2dd9f2c3bbc02e2dde0e66`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- ### 1-B. Deficiency Letter 정의 NB가 conformity assessment 과정에서 제조사 제출 서류의 결함·불명확·누락 사항을 서면으로 통...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Response to Notified‑Body Deficiency Letter**  
*Device: Diagnostic X‑ray imaging detector (standard radiology)*  

---  

### 1. Device Overview (as inferred from the source)  
- Intended use : “Standard diagnostic radiology” (same clinical condition as the predicate device).  
- Core performance claim : Detective Quantum Efficiency (DQE) ≥ 65 % (reference TR‑2024‑015, IEC 62220‑1‑1).  
- Clinical documentation : Revised Clinical Evaluation Report (CER) Rev. 3 attached as **Annex A**.  

---  

### 2. Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory Basis |
|------|---------------|------------------|
| **MDR classification rule** | **Rule 17** – “Devices specifically intended for recording diagnostic images generated by X‑ray radiation.” | Annex VIII, Rule 17 → **Class IIa** |
| **Corresponding Art. 52 paragraph** | Class IIa devices follow the route laid down in **Art. 52(6)**. | MDR Art. 52(6) |
| **Conformity‑assessment route** | **Annex IX** – full QMS (ISO 13485 : 2016) + technical‑documentation assessment by the NB. | Annex IX (stand‑alone) |

> **Citation:** Classification Rule 17 (Annex VIII); Art. 52(6) for Class IIa; Annex IX as the assessment route.  

---  

### 3. Evidence Required Under MDR  

| Category | Required Artefact(s) | Minimum Content (MDR reference) |
|----------|----------------------|----------------------------------|
| **Technical Documentation** – Section 6.1 of Annex II | • Device description, intended use, variants<br>• Design & manufacturing information<br>• GSPR compliance (Annex I §16‑§22)<br>• Verification & validation results (including DQE test) | Annex II §§1‑6 |
| **Clinical Evaluation** | Revised CER Rev. 3 (Annex A) demonstrating clinical equivalence to a predicate device. | Annex XIV Part A; kept current under Art. 61 |
| **Bench Test / Performance Data** | • IEC 62220‑1‑1 DQE test report TR‑2024‑015 (DQE ≥ 65 %).<br>• Additional image‑quality assessments (e.g., contrast‑to‑noise ratio) if requested. | Annex XIV Part A – “clinical data” may include equivalence testing. |
| **Risk Management File** | RMF per ISO 14971 : 2019 (EN A11:2021) covering:<br>– Radiation hazards (Annex I §16)<br>– Software safety (if any, Annex I §17 & IEC 62304)<br>– Usability (IEC 62366‑1) | Annex I §3‑§9; ISO 14971 |
| **Usability Engineering** (if device is user‑operated) | IEC 62366‑1 usability file demonstrating mitigation of use‑error risks (§5 GSPR). | Annex I §5 |
| **Post‑Market Surveillance** | • PMS plan (Art. 84) <br>• Periodic Safety Update Report (PSUR) – Class IIa, update ≤ 2 years (Art. 86) | Art. 83‑86 |
| **EU Declaration of Conformity** | Completed DoC with reference to all applicable standards and NB certificate number. | Art. 19; Annex IV content list |
| **Summary of Safety & Clinical Performance (SSCP)** – *not required* for Class IIa (only for Class III / implantables). | – | – |

---  

### 4. Gaps / Missing Information Identified in the Deficiency Letter  

| Gap | What is Missing | Why it Matters (Regulatory) |
|-----|----------------|-----------------------------|
| **Risk Management File** | No RMF provided; no evidence of risk controls for ionising‑radiation exposure, software safety or use‑error mitigation. | Required by Annex I §§3‑5 and ISO 14971 (risk management). |
| **PMS Plan / PSUR** | No PMS plan (Art. 84) nor periodic safety update report (Art. 86) included. | Obligatory post‑market documentation for Class IIa devices. |
| **Labeling & IFU** | Annex I §23 (labelling, instructions for use) not referenced in the submission. | Needed to demonstrate compliance with GSPR and to support safe use. |
| **Verification of Radiation Protection** | Only DQE data supplied; no evidence of compliance with Annex I §16 (radiation protection), e.g., shielding test, leakage measurements, IEC 60601‑2‑28/54 conformity. | MDR requires proof that radiation hazards are adequately controlled. |
| **Software Documentation** (if applicable) | No IEC 62304 software lifecycle file attached; no software hazard analysis. | Required when the detector includes embedded software (Annex I §17). |
| **Declaration of Conformity** | Not referenced in the material sent to NB. | Mandatory for CE‑marking (Art. 19). |

> *No specific identifier found in source — verify separately* for the above gaps where the source did not quote an exact article or annex number.

---  

### 5. Recommended Risk Controls (to be reflected in the RMF)  

| Hazard | Control Measure | Supporting Standard |
|--------|-----------------|----------------------|
| **Ionising‑radiation exposure** | • Interlock on X‑ray generator <br>• Adequate shielding of detector housing <br>• Alarm for over‑exposure | IEC 60601‑2‑28 (X‑ray tube assemblies) & IEC 60601‑2‑54 (radiography equipment) |
| **Electrical safety** | • Built‑in protective earth, leakage current limits | IEC 60601‑1 (2005+A1:2012+A2:2020) |
| **Software malfunction** | • Software development per IEC 62304; verification of error handling; failure mode analysis | IEC 62304 |
| **Use‑error (operator)** | • Ergonomic design, clear labeling, training instructions, usability testing per IEC 62366‑1 | IEC 62366‑1 |
| **Mechanical/thermal hazards** | • Robust enclosure, temperature monitoring, compliance with IEC 60601‑1 §20 | IEC 60601‑1 |

---  

### 6. Citations (Framework vs. Instance)  

| Category | Citation Type | Reference |
|----------|---------------|-----------|
| Classification rule | **Framework** | Rule 17 – Annex VIII |
| Conformity‑assessment route | **Framework** | Art. 52(6); Annex IX |
| Clinical evaluation requirement | **Framework** | Annex XIV Part A; Art. 61 |
| PMCF requirement (if needed) | **Framework** | Annex XIV Part B |
| PMS system & plan | **Framework** | Art. 83, Art. 84 |
| PSUR cadence for Class IIa | **Framework** | Art. 86(2) – ≤ 2‑year update |
| GSPR sections relevant | **Framework** | Annex I §§16‑23 (radiation protection, software, labeling) |
| Test report & DQE threshold | **Instance** | “Test Report TR‑2024‑015, IEC 62220‑1‑1; DQE ≥ 65 %” – *as cited in source* |
| Revised CER | **Instance** | “Revised CER Rev. 3 attached as Annex A” – *as cited in source* |

---  

### 7. Human‑Escalation Triggers (when to involve senior staff / management)  

1. **Classification Uncertainty** – If the NB questions whether the device is a detector only (Rule 17, Class IIa) or part of an X‑ray system that might invoke Rule 10/9 → require senior regulatory decision.  
2. **Insufficient Radiation‑Protection Evidence** – Requests for additional IEC 60601‑2‑28/54 test data; escalation to engineering and safety teams.  
3. **Software Scope Expansion** – Discovery that embedded software performs diagnostic functions (Rule 11) may raise class to IIb or III → senior legal/regulatory review required.  
4. **PMS / PSUR Deficiency** – NB demands a complete PMS plan/PSUR before certificate issuance; involve the post‑market surveillance manager.  
5. **Risk Management Gaps** – Missing RMF elements identified → escalation to risk‑management lead for immediate compilation.  

---  

### 8. Peer‑Review Prompt  

> **Request:** Please review the assumptions made regarding (a) the device’s classification under Rule 17 versus possible inclusion of Rule 10/11 aspects, (b) completeness of the listed evidence against the NB’s expectations, and (c) any jurisdiction‑specific gaps that may arise (e.g., alignment with IEC 60601‑2‑28 vs. IEC 62220‑1‑1). Highlight missing citations or areas needing verification.  

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

### kb-eval-20261103-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e1df9b13e28b6106", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e1df9b13e28b6106`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_MDR_2017_745.md)
- Source hash: `15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `EU_MDR_2017_745.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | |...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – X‑ray Imaging System (radiography / radioscopy)  
Prepared for Notified Body submission**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory basis |
|------|----------------|------------------|
| **Device type** | Active medical device that emits ionising radiation for diagnostic purposes (radiography / radioscopy). | IEC 60601‑2‑54 (safety) + MDR Annex VIII Rule 10 (active devices emitting ionising radiation). |
| **MDR class** | **Class IIb** – because the emitted radiation can cause serious health effects if improperly controlled. | MDR Annex VIII, Rule 10 → Class IIb. |
| **Conformity‑assessment route** | **Option A:** Annex IX (full quality‑management system + technical‑documentation assessment).  <br>**Option B:** Annex X (type‑examination) together with Annex XI (production conformity verification). | Art. 52(4) MDR – “Class IIb devices shall be placed on the market … either by Annex IX or by Annex X + XI.” |

*Recommended route:* **Annex IX** (single‑step QMS + TD assessment) is usually the most efficient for a complete system that integrates hardware, software and radiation components.

---

### 2. Required Evidence Package  

| # | Evidence required (what the NB must see) | Where it belongs in the dossier* | Regulatory citation |
|---|-------------------------------------------|----------------------------------|----------------------|
| **1** | **Technical Documentation (TD)** – complete sections‑by‑section as per Annex II §§1‑6 (device description, intended use, design & manufacturing information, GSPR compliance, benefit–risk analysis, verification & validation). | Annex II “Structure of the technical documentation”. | MDR Annex II |
| **2** | **GSPR Mapping Report** – matrix linking each requirement of Annex I ( §§1‑9, 16‑23) to evidence in the TD. | Annex II §6.1 + internal GSPR checklist (e.g. *GSPR 체크리스트*). | MDR Annex I; internal “GSPR 체크리스트 활용” (Source [1]). |
| **3** | **Risk Management File (RMF)** – risk analysis, evaluation of residual risk, risk control measures and verification per ISO 14971:2019. | Annex I §3 (risk‑management system). | MDR Annex I §3; ISO 14971 (2019). |
| **4** | **Clinical Evaluation Report (CER)** – up‑to‑date evaluation of clinical performance, literature review and/or clinical investigation data. Must be kept current under Art. 61. | Annex XIV Part A (clinical evaluation). | MDR Annex XIV Part A; Art. 61 |
| **5** | **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – defined objectives, methodology, timelines and interim findings. | Annex XIV Part B (PMCF). | MDR Annex XIV Part B |
| **6** | **Post‑Market Surveillance (PMS) Plan** – systematic collection & analysis of post‑market data; includes periodic safety update report (PSUR). | Art. 84 (PMS plan); Art. 86 (PSUR for Class IIb, annual). | MDR Art. 84, Art. 86 |
| **7** | **Quality Management System documentation** – ISO 13485:2016‑based QMS manual, SOPs (e.g., *SOP‑CC‑001*, *SOP‑PSUR‑001*), internal audit records. | Annex IX §§2‑4 (QMS assessment). | MDR Annex IX; ISO 13485 (2016) |
| **8** | **Device‑specific standards & test reports** – IEC 60601‑2‑54 (radiation safety), IEC 60601‑1 (general requirements), IEC 62304 (software life‑cycle), IEC 62366‑1 (usability). | Annex II §5 (verification & validation) and Annex I §16, §17. | MDR Annex I §§16‑17; listed standards in Source [2]. |
| **9** | **Labeling & IFU** – conformity with Annex I §23 (information supplied with the device), including radiation warnings, user training instructions, UDI. | Annex II §6.1 and Annex IV (Declaration of Conformity). | MDR Annex I §23; MDR Annex IV. |
| **10** | **EU Declaration of Conformity (DoC)** – signed by the manufacturer, containing all mandatory content (manufacturer details, device identification, conformity‑assessment route, standards applied, signed declaration). | Annex IV (content) & Art. 19 (obligation). | MDR Art. 19; Annex IV. |
| **11** | **EUDAMED registration record** – device identifier, UDI‑DI, manufacturer and authorised representative data, conformity‑assessment details. | Art. 33‑39 (electronic database obligations). | MDR Art. 33‑39. |

\* *The “TD plan” and “check‑list” referenced in Source [1] (F‑MDR‑TD‑CHK‑001) should be used to verify that each of the above items is captured before NB submission.*

---

### 3. What Is Currently Missing / Needs Further Development  

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Intended use statement** (indications, patient population, clinical setting) – not present in the excerpts. | Drives classification, clinical evaluation scope & labeling (§23). | RA to obtain final wording from product‑owner; insert into TD §1. |
| **Detailed design & V&V data** for hardware (X‑ray tube, detector) and software (image‑processing algorithm). | Required for Annex II §§5‑6 (verification & validation) and IEC 62304 compliance. | R&D to supply test reports; QA to integrate into TD. |
| **Clinical evidence** – systematic literature search strategy, selection criteria, state‑of‑the‑art analysis, any clinical investigation results. | Core of the CER (Annex XIV Part A) and needed for benefit‑risk justification. | Clinical team to draft CER; RA to map to GSPR. |
| **PMCF plan details** – target sample size, follow‑up duration, endpoints, data collection methods. | Required by Annex XIV Part B; influences PSUR content (Art. 86). | Clinical‑RA liaison to define and document in PMCF Plan. |
| **PMS system implementation** – procedures for complaint handling, field safety corrective actions (FSCA), trend analysis. | Art. 83/84/85/86 demand a functional PMS; missing leads to non‑conformity findings. | QA to produce SOPs (e.g., *SOP‑FSC‑001*); RA to verify completeness. |
| **Risk control measures for radiation dose** – specific interlocks, automatic exposure limits, user training records. | GSPR §16 (radiation protection) and risk analysis (§3). | Risk team to add controls; evidence through test reports & SOPs. |
| **UDI‑DI allocation & labeling artwork** – not shown in source material. | Required for EUDAMED registration and Annex I §23. | Manufacturer’s regulatory affairs to generate UDI, update labeling. |
| **Declaration of Conformity draft** – signature authority, reference to all applied standards. | Mandatory Art. 19; NB will review for completeness. | RA Lead to prepare DoC after all evidence compiled. |

---

### 4. Key Risk Controls (to be documented in the RMF and GSPR mapping)  

1. **Radiation safety** – dose‑monitoring sensor, automatic shut‑off if exposure exceeds preset limit, shielding design per IEC 60601‑2‑54 §16.4.  
2. **Electrical safety** – compliance with IEC 60601‑1 (protective earthing, leakage current limits).  
3. **Software reliability** – IEC 62304 classified as Class C (since software directly influences diagnostic decision); verification & validation test suites; fail‑safe mode on abnormal inputs.  
4. **Usability / user error mitigation** – Human factors analysis per IEC 62366‑1; clear labeling, lock‑out mechanisms for non‑sterile configurations.  
5. **Manufacturing controls** – Process validation of X‑ray tube assembly (IEC 60601‑2‑28), calibration records, batch release criteria.  
6. **Post‑market monitoring** – Real‑time dose reporting to central server, periodic review of incident reports per Art. 87.  

All above must be linked to the corresponding GSPR clauses (§3 risk management system; §4 risk control measures; §16 radiation protection; §17 electronic programmable systems; §23 labeling).

---

### 5. Human‑Escalation Triggers (when to involve senior staff or pause submission)  

| Trigger | Reason | Escalated to |
|---------|--------|--------------|
| **Unresolved classification doubt** (e.g., component considered a separate instrument that could be Class IIa) | Mis‐classification leads to wrong conformity route. | Senior RA Manager / Legal counsel. |
| **Missing clinical data** – no up‑to‑date CER or incomplete literature search. | NB will reject the dossier; benefit‑risk cannot be demonstrated. | Clinical Lead & RA Lead. |
| **Incomplete GSPR mapping** (evidence gaps for any of §§1‑9, 16‑23). | Non‑conformity finding on Annex I compliance. | QA Lead + Risk Manager. |
| **PMS/PMCF plan not aligned with Art. 86 timing** (annual PSUR not scheduled). | Post‑market obligations unmet → non‑conformity. | Post‑Market Surveillance Coordinator. |
| **Risk controls not verified** (e.g., radiation interlock test report missing). | Safety hazard; NB will issue a corrective action. | Engineering Lead / Quality Manager. |
| **DoC draft lacking required signatory or standard references** | Declaration of conformity invalid under Art. 19. | Regulatory Affairs Director. |

When any trigger is hit, the responsible person must **log the issue in the project risk register**, halt further NB submission steps, and notify the RA Lead for corrective action.

---

### 6. Peer‑Review Request  

> *“Please review this draft: verify that the classification (Class IIb via Rule 10) and chosen conformity route (Annex IX vs. Annex X+XI) are appropriate for the full X‑ray system described. Confirm that all required evidence items have been captured, especially the clinical evaluation and PMCF elements. Highlight any gaps in the GSPR mapping or PMS framework that may need additional documentation before NB submission.”*  

--- 

**End of draft**

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> "PSUR for Class IIb, annual" — Art. 86(1)상 IIb는 최소 2년(III·이식형만 연간). 소스에 주기 없음 → 모델 내재 오류.

**Source Excerpts**

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `1072636411107495596`

> --- doc-id: EU_MDR_2017_745 title: "EU MDR — Regulation (EU) 2017/745 요약 및 적용 지침" type: Guide version: v0.3.1 status: draft category: 01_법규_규제 purpose: "EU MDR 2017/745 핵심 요구사항, 2026 일정, 기술문서 구성 및 X-ray 시스템 적용 지침" applicable: [EU MDR 2017/745, EU MDR GSPR Annex I, ISO13485:2016, ISO14971:2019, IEC 62304, IEC 60601-1, IEC 60601-2-54, UDI] forms: [F-MDR-TD-CHK-001] related-docs: - GSPR_정합표준_매핑표 - GSPR_체크리스트_v0.2_템플릿 - PRRC_역할_및_한미_대응자_매핑 - EU_AI_Act_MDR_중첩적용_매핑 - ISO13485_2016_요약 - SOP-CC-001 - SOP-PSUR-001 - SOP-FSCA-001 - TF-TD-001 related-issues: [4, 5, 22, 33, 989] owner: RA/QA Lead last-review: 2026-07-23 review-due: 2027-06-09 --- # EU...

### kb-eval-20261103-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b6bba111c2585b88", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b6bba111c2585b88`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md)
- Source hash: `d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexII_Technical_Documentation_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMS...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Notified Body Query Response (MDR 2017/745)**  

---

### 1. Device‑information that must be supplied before any classification can be confirmed  

| Information | Why it is needed | Where it is used in the MDR |
|-------------|------------------|----------------------------|
| **Exact intended purpose / indication** (including patient population, clinical setting and claimed therapeutic/diagnostic effect) | Drives the selection of the appropriate rule in Annex VIII and therefore the device class. | Annex VIII – classification rules; Art 52 – determination of conformity‑assessment route. |
| **Mode(s) of action** (e.g., active therapeutic, diagnostic, software decision support, energy source) | Needed to map the device onto Rule 9, 10, 11 or 17 (or other relevant rule). | Annex VIII – Rules 9–11, 17; Art 52. |
| **Key technological characteristics** (e.g., presence of a measuring function, sterility, re‑usability) | Determines whether the “Is/Im/Ir” sub‑category applies for Class I devices. | Annex VIII – rules for Class I (sterile, measuring, reusable surgical). |
| **Whether the device is invasive or implantable** | Influences both classification and additional requirements such as the Summary of Safety & Clinical Performance (SSCP) for Class III/implantables. | Art 32; Annex XV (clinical investigation). |

> **Current status:** The source excerpt only provides a generic “Technical Documentation” matrix (Annex II §1‑6). No device‑specific description, intended use or mode of action is present → *classification cannot be finalised*.

---

### 2. Preliminary classification pathway (framework)

| Possible class | MDR provision (Art.) | Conformity‑assessment route (Annex) | Notified‑Body involvement |
|----------------|----------------------|-------------------------------------|----------------------------|
| **Class I (non‑sterile, non‑measuring, non‑reusable surgical)** | Art 52(7) | Self‑declaration – technical documentation (Annex II & III) + EU Declaration of Conformity (Art 19). | No NB required. |
| **Class Is / Im / Ir** | Art 52(7) | Annex IX (chapters I & III) *or* Annex XI Part A – limited NB scope on sterile/measuring/reuse aspect. | Limited NB audit. |
| **Class IIa** | Art 52(6) | Annex IX (full QMS + technical‑doc assessment) **or** Annex II/III + Annex XI §10. | NB required for QMS & technical file review. |
| **Class IIb** | Art 52(4) | Annex IX (full QMS + technical‑doc) **or** Annex X (type‑examination) + Annex XI (production conformity). | NB required – full assessment or type‑exam route. |
| **Class III** | Art 52(3) | Annex IX (full) **or** Annex X + Annex XI. | NB required – highest scrutiny. |

> **Action:** Once the intended purpose and mode of action are clarified, apply the relevant rule from Annex VIII to fix the class, then select the appropriate route per Art 52.

---

### 3. Evidence required in the Technical Documentation (Annex II §§1‑6)

| Annex II § | Content element | Minimum evidence (per MDR) |
|------------|-----------------|-----------------------------|
| **§1 – Device Description** | Intended purpose, indications, contraindications, user profile, principle of operation. | Completed “Device Description” section of the DHF; clear statement of intended use. |
| **§2 – Labeling & IFU** | Labels, symbols, instructions for use (including safety information). | Final label artwork and full IFU in required languages (minimum English + NB‑requested language). |
| **§3 – Design & Manufacturing Information** | Device architecture, drawings, specifications, manufacturing processes, traceability of components. | Design History File (DHF) entries, process flow diagrams, supplier declarations. |
| **§4 – General Safety & Performance Requirements (GSPR) Checklist** | Mapping to Annex I GSRPs, including verification of each requirement. | Completed GSPR checklist with supporting test reports, bench‑testing data, biocompatibility evidence (ISO 14971 risk file referenced). |
| **§5 – Risk Management** | Risk Management File (RMF) per ISO 14971. | Risk analysis, evaluation of residual risks, risk control measures, verification of controls. |
| **§6 – Verification & Validation** | Results of verification (design verification) and validation (clinical/usable‑validation). | V&V reports, software verification (IEC 62304 if applicable), usability testing (IEC 62366‑1), clinical validation data. |

> **Missing from source:** Concrete documents for each element are not supplied; only a matrix linking MDR sections to other jurisdictions is shown.

---

### 4. Clinical Evidence (Annex XIV Part A – Clinical Evaluation Report)

| Requirement | Typical evidence | Where it belongs in the TD |
|-------------|------------------|----------------------------|
| State‑of‑the‑art literature review | Systematic search of peer‑reviewed studies, clinical guidelines. | Annex II §6 (clinical evaluation) and CER (Annex XIV Part A). |
| Clinical data from EU‑market or equivalent | Post‑Marketing Clinical Follow‑up (PMCF) data, registries, prospective/retrospective studies. | PMCF plan & report (Annex XIV Part B); incorporated in the CE‑marking technical file. |
| Benefit–risk determination | Summarised conclusions of clinical data against intended purpose. | CER; also feeds into GSPR §8 (benefit‑risk) and PSUR (Art 86). |

> **Current status:** No clinical evaluation or PMCF plan is referenced in the excerpt → a major gap for any class > I.

---

### 5. Post‑Market Surveillance (PMS)

| Article | Requirement | Documentation |
|---------|-------------|----------------|
| Art 83 | PMS system (processes, responsibilities). | PMS System description (Annex III). |
| Art 84 | PMS plan (planned activities, data collection). | PMS Plan (Annex III). |
| Art 85 | PMS report for Class I. | Annual PMS Report (if applicable). |
| Art 86 | Periodic Safety Update Report (PSUR) for Class IIa/IIb/III. | PSUR containing benefit‑risk conclusions, PMCF findings, sales data (updated at least every 2 years for IIa, annually for IIb/III). |

> **Missing:** No PMS system, plan or PSUR is mentioned → required before NB approval.

---

### 6. Risk Management – Core Controls

| GSPR reference | Required control |
|----------------|------------------|
| Annex I §3 (risk‑management system) | Full RMF per ISO 14971:2019, including risk analysis, evaluation of residual risks and verification of controls. |
| Annex I §4 (risk control) | Implementation of protective measures (design safeguards, alarms, user training). |
| Annex I §5 (use‑error) | Usability engineering (IEC 62366‑1) to minimise use errors; inclusion in IFU. |
| Annex I §6–8 (lifetime, transport, side‑effects) | Specification of device life‑cycle, packaging & transport validation, post‑market monitoring for known side effects. |

> **Current evidence:** Only a generic “Risk Management” row is shown; the actual RMF, risk analysis worksheets and verification results are not provided.

---

### 7. Identified Gaps / Information Needed from the Manufacturer  

| Gap | What must be supplied |
|-----|------------------------|
| **Exact intended purpose & mode of action** | Narrative description plus any claim‑supporting data (clinical/bench). |
| **Classification rule justification** | Mapping to Annex VIII rule(s) with supporting evidence (e.g., energy source, measuring function). |
| **Completed sections of Annex II** (device description, labeling, design & manufacturing, GSPR checklist, risk management, verification & validation). | Full drafts or final documents for each §1‑6. |
| **Clinical Evaluation Report (CER)** – state‑of‑the‑art literature, clinical data, benefit–risk analysis. |
| **PMCF plan / report** (if class IIa/IIb/III). |
| **PMS system & plan** (Art 83‑84) and PSUR (Art 86) where applicable. |
| **Usability evaluation evidence** (IEC 62366‑1) if the device is used by lay persons or has a high use‑error potential (§22 GSPR). |
| **Declaration of Conformity (DoC)** – Art 19 content once all above are in place. | Draft DoC with reference to applicable standards and conformity‑assessment route. |

---

### 8. Suggested NB Response Template  

> *“Dear Manufacturer,*  
>  
> *In order to assess your CE‑marking dossier we require the items listed below. Without these, we cannot confirm the device class nor proceed with the appropriate conformity‑assessment route (Art 52, Annex IX or Annex X+XI). Please provide:*
> 
> 1. **Intended purpose and mode of action** – to enable classification under Annex VIII (Rule 9, 10, 11 or 17 as applicable).  
> 2. **Completed Annex II sections (§1‑6)** with supporting evidence (device description, labeling, design & manufacturing data, GSPR checklist, risk‑management file, verification & validation reports).  
> 3. **Clinical Evaluation Report** in compliance with Annex XIV Part A and corresponding clinical data.  
> 4. **PMCF plan/report** (Annex XIV Part B) if the device is Class IIa/IIb/III.  
> 5. **PMS system & plan** (Art 83‑84) and the first PSUR (Art 86) where applicable.  
> 6. **Usability engineering evidence** for devices intended for lay users or with critical use‑error risk (Annex I §22).  
> 7. **Draft EU Declaration of Conformity** (Art 19, Annex IV) referencing the selected conformity‑assessment route.  
> 
> *Please address each point and forward the documentation within 30 calendar days.*  
>   
> *Regards,*  
> *[NB name]*”

---

### 9. Human‑Escalation Triggers  

| Trigger | Reason for escalation |
|--------|-----------------------|
| **No response or incomplete information after the NB request deadline** | Requires senior RA manager to decide on a non‑conformity notice (NCN) or suspension of assessment. |
| **Inconsistent intended purpose vs. provided clinical data** | Needs expert clinical evaluation review to avoid mis‑classification. |
| **Missing risk‑management verification for a critical residual risk** | May indicate unsafe design – escalation to the NB’s safety officer and possibly to competent authorities (Art 87). |
| **Device appears to be an “active implantable” or software with a high‑risk decision impact but no SSCP draft** | Immediate escalation to senior compliance because Art 32 requires an SSCP for Class III/implantables. |
| **Manufacturer claims conformity without an applicable QMS (ISO 13485) in place** | Escalate to NB quality‑management audit lead; non‑compliance with Art 10(9). |

---

### 10. Peer‑Review Request  

*“@RA‑Colleague – please challenge the assumptions above, especially:*  

- *The completeness of the evidence list for each Annex II sub‑section (are any MDR‑specific tests missing?)*  
- *Whether additional annexes (e.g., Annex XV for clinical investigations) might be required given the unknown device type.*  
- *Any jurisdictional nuances that could affect the classification or PMS obligations (e.g., devices incorporating AI software).*  

*Your feedback will help close remaining gaps before final NB communication.”*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> "PSUR ≥2yr for IIa, annually for IIb/III" — IIb는 2년. 경로 표기(Annex II/III+XI §10 포함)는 이번엔 정확.

**Source Excerpts**

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

### kb-eval-20261103-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7347c8f664640894", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7347c8f664640894`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수). ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Notified‑Body Query Response (X‑ray medical device)**  

| Item | Assessment & Requirement | Regulatory basis / citation |
|------|--------------------------|------------------------------|
| **1. Device classification** | The equipment emits ionising radiation for diagnostic purposes. Under **Annex VIII Rule 10** “active devices that emit ionising radiation for diagnosis or therapy” the default class is **IIb**. The source confirms this: *“이온화 방사선 기기 (X‑ray)는 Class IIb 이상 → NB 인증 필수.”* | Annex VIII Rule 10 (framework)  ; source [1] |
| **2. Conformity‑assessment route** | Class IIb devices must follow the MDR routes laid out in **Art. 52(4)**: <br>• **Annex IX** – full quality‑management‑system & technical‑documentation assessment (single NB)  <br>or <br>• **Annex X + Annex XI** – type‑examination plus production conformity verification (NB involved in both steps). | Art. 52(4) MDR 2017/745 (framework) |
| **3. Core elements of the Technical Documentation (TD)** *(to be submitted to the NB)* | • Device description, intended purpose and indications <br>• Design & manufacturing information (including IEC 60601‑2‑54 compliance for X‑ray equipment) <br>• Risk Management File (ISO 14971:2019) – covering radiation protection (§16), electrical safety (§18), use‑error (§5) <br>• Verification & validation reports (bench, electromagnetic compatibility, radiation output) <br>• **Clinical Evaluation Report** (CER) – state‑of‑the‑art literature analysis, clinical performance data (Annex XIV Part A, Art. 61) <br>• **Post‑Market Clinical Follow‑up** (PMCF) plan & evaluation report (Annex XIV Part B) <br>• PMS system (Art. 83), PMS plan (Art. 84) and PSUR (annual for Class IIb, Art. 86) <br>• EU Declaration of Conformity (Art. 19 & Annex IV content) | Annex II §6.1 (TD structure); Annex XIV Part A/Part B; Art. 61, 83‑86; ISO 14971:2019; IEC 60601‑2‑54 (framework) |
| **4. Clinical evidence required** | • SOTA literature covering dose limits, image quality and safety outcomes for the specific X‑ray modality <br>• If literature does not fully demonstrate equivalence/safety, a **clinical investigation** under MDR Art. 66 may be required (especially for new indications or novel technology). <br>• PMCF data must be collected throughout the product life‑cycle and summarised in the PSUR. | Annex XIV Part A; Art. 66 (framework) |
| **5. Missing information / gaps identified from source** | 1. The exact MDR coding (MDxxxx) for this device in the NANDO database – “no specific identifier found in source — verify separately.” <br>2. Detailed intended‑use statement and indication list. <br>3. Full risk‑analysis results (including residual risk justification). <br>4. Clinical data package (clinical literature list, bench test reports, any existing clinical investigation protocol). <br>5. QMS audit report and evidence of NB‑approved ISO 13485:2016 implementation. <br>6. Non‑conformity response documentation required for the NB audit (source [2] lists it as a needed artefact). | Source [1] (classification) & [2] (document checklist); gaps flagged per MDR requirements |
| **6. Core risk controls to be demonstrated** | • **Radiation protection** – compliance with Annex I §16 (dose limits, shielding, interlocks). <br>• **Electrical safety** – IEC 60601‑2‑54 conformity; residual risks addressed in RMF (§3‑9 of Annex I). <br>• **Usability / use‑error mitigation** – Application of IEC 62366‑1 (usability engineering) to meet Annex I §5. <br>• **Software life‑cycle** (if software is part of the device) – IEC 62304 compliance, addressing Annex I §17. <br>• **Design verification & validation** – per ISO 14971 and MDR Annex II §§5‑6. | Annex I §§3‑9, 16‑18; IEC 60601‑2‑54, IEC 62366‑1, IEC 62304 (framework) |
| **7. Human‑escalation triggers** | • **Classification doubt** – if the device includes additional functionality that could move it to Rule 9 or Rule 11, senior RA must be consulted. <br>• **MDR code missing** – require senior regulatory manager to confirm correct NANDO entry before NB submission. <br>• **Insufficient clinical evidence** – escalation to Clinical Lead for decision on a new MDR‑compliant investigation. <br>• **NB contract/quotation issues** – involve Procurement & Legal when the comparison table or audit contract (source [2]) reveals non‑conformity with internal policies. <br>• **Non‑conformities identified during NB audit** – trigger Quality‑Assurance escalation per Art. 84(2) and internal CAPA process. |
| **8. Suggested next actions** | 1. Retrieve the device’s MDR code (MDxxxx) from NANDO and record it in the TD index.<br>2. Compile the artefacts listed in source [2] (candidate NB comparison, audit contract/quote, Technical‑Documentation‑Assessment report, Non‑conformity response material, QMS audit file).<br>3. Draft the Clinical Evaluation Report using latest SOTA publications; verify whether a supplementary clinical investigation is needed.<br>4. Build the PMS plan (Art. 84) and schedule PSUR preparation (annual for Class IIb, Art. 86). | — |

---

### Peer‑review request
*“@RA‑Colleague – please review the assumptions made about classification (Rule 10 → Class IIb), the completeness of the listed documentation against MDR Annex II/IV requirements, and verify that no jurisdiction‑specific items (e.g., IVDR or national exceptions) have been omitted. Highlight any gaps in source coverage or missing identifier verification.”*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> "PSUR (annual for Class IIb, Art. 86)" 2회 — IIb는 2년.

**Source Excerpts**

1. Chunk `978896205875274621`

> ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수).

2. Chunk `296791090431458058`

> ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료

### kb-eval-20261103-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b0f24d874b620a8b", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b0f24d874b620a8b`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week04_MDR_EU_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `Week04_MDR_EU_체계_상세.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUF...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `Notified Body question response` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `Notified Body question response`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - NB deficiency에 직접 답했는지, evidence와 annex reference가 추적 가능하게 연결됐는지 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Assessment Draft – Classification & CE‑Marking Pathway (NB question response)**  

---

### 1. Scope of the enquiry  
The Notified Body (NB) has asked for a preliminary regulatory judgement covering:

* **Device classification** and the consequent conformity‑assessment route;  
* **Evidence required** to satisfy MDR obligations;  
* **Gaps that must be filled before a submission can be made;**  
* **Risk‑control expectations**; and  
* **Triggers for human escalation** (e.g., when CA advice or senior‐RA sign‑off is needed).  

The only source material supplied are two excerpted sections from the internal “MDR 요약” document (see Source [1]–[2]). No specific device description, intended purpose, or technical characteristics have been provided.

---

### 2. Applicable regulatory framework  

| Reference | Content |
|-----------|---------|
| **Regulation (EU) 2017/745 (MDR)** – Art. 51 & Annex VIII | Classification principles – manufacturer bears the sole responsibility for self‑classification; rules are applied sequentially and the highest applicable class prevails. *(source [2])* |
| MDR Art. 61, **Annex XIV Part A** | Requirement to compile a Clinical Evaluation Report (CER) and a Declaration of Conformity (DoC). *(source [1])* |
| MDR Art. 87 | Vigilance reporting obligations (serious incidents/FSCA). *(source [1])* |
| MDR Art. 83‑86 | Post‑market surveillance system, plan, PSUR (for class IIa/b/III) and PMS report (class I). |
| MDR Art. 11 | Requirement for an Authorized Representative when the manufacturer is established outside the EU. |
| MDR Art. 52 – Conformity‑assessment routes (Annex IX or Annex X + XI) | Determines which NB involvement is required based on the final class. |
| **ISO 14971:2019** (risk management) – referenced by GSPR §3‑9. |
| **ISO 13485:2016** – QMS requirement for classes I (sterile/measuring/reusable) and higher. |

*Instance identifiers that appear in the source*:  

- Korean Medical Device Act “의료기기법 §31” (post‑market incident reporting).  
- MDR cross‑reference to U.S. 21 CFR 803 & MedWatch (used only as a comparative note).  

These are reproduced verbatim because they are present in the source material; no invented numbers have been added.

---

### 3. Classification – Preliminary view  

| Step | Required input | Current status |
|------|----------------|----------------|
| **Identify intended medical purpose** (diagnosis, therapy, monitoring, etc.) | Indication, patient population, anatomical site, invasiveness, sterility, measuring function | *Not provided* |
| **Determine mode of action / energy source** | Active vs. passive, ionising radiation, software‑driven decision support, therapeutic energy | *Not provided* |
| **Apply Annex VIII rules sequentially** (Rule 1‑22) | Device description matched against each rule; highest class applies | *Cannot be executed without the above data* |

> **Conclusion:**  Classification cannot be finalised at this stage. The NB should request a complete “Device Description & Intended Use” package before proceeding with any classification decision.

---

### 4. Conformity‑assessment route (once class is known)

| Final MDR class | Relevant Art. 52 paragraph | Required NB involvement |
|-----------------|----------------------------|--------------------------|
| **Class I** (non‑sterile, non‑measuring, non‑reusable) | Art. 52(7) – self‑declaration only | No NB needed |
| **Class Is / Im / Ir** | Art. 52(7) – Annex IX §2 or Annex XI Part A (limited scope) | NB required for sterile/measuring/reusable aspects |
| **Class IIa** | Art. 52(6) – Full Annex IX assessment (QMS + technical documentation) | NB involvement mandatory |
| **Class IIb** | Art. 52(4) – Either full Annex IX or Annex X + XI (type‑examination & production conformity verification) | NB involvement mandatory |
| **Class III** | Art. 52(3) – Full Annex IX or Annex X + XI (type‑examination & production conformity verification) | NB involvement mandatory |

*The route will be definitively assigned once the class is established.*

---

### 5. Evidence required for CE marking  

| Evidence item | Where mandated (MDR) | Brief content |
|---------------|----------------------|--------------|
| **Technical documentation** (device description, design & manufacturing information, GSPR fulfilment, verification/validation) | Annex II §1‑6 |
| **Risk Management File** (risk analysis, evaluation, control measures) | Annex I §§3‑9; ISO 14971:2019 |
| **Clinical Evaluation Report (CER)** | Art. 61 & Annex XIV Part A |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Annex XIV Part B (required for all classes ≥ IIa; optional for class I if justified) |
| **PMS system & plan** | Art. 83‑84 (mandatory for all devices) |
| **Periodic Safety Update Report (PSUR)** | Art. 86 – required for classes IIa, IIb, III (frequency: ≥ 2 yr for IIa; annual for IIb/III) |
| **Vigilance reporting** (serious incidents / FSCA) | Art. 87 (and Korean “의료기기법 §31” for local reporting) |
| **Unique Device Identification (UDI)** – registration in EUDAMED | UDI‑Portal, linkage to GUDID if marketed in the US (source [1]) |
| **Declaration of Conformity** | Art. 19 & Annex IV (content includes classification, conformity‑assessment route, and reference to standards) |
| **Labeling & IFU** | Annex I §23 – must contain essential safety information, intended use, and any contraindications |
| **Authorized Representative documentation** (if manufacturer outside EU) | Art. 11 – proof of appointment, scope, contact details |

---

### 6. Gaps / Missing Information (must be supplied before a submission)

1. **Complete device description** – indications, target population, anatomical site, intended users, and environment of use.  
2. **Intended purpose and mode of action** – necessary to apply Annex VIII rules (e.g., Rule 9‑11, 17).  
3. **Classification rule(s) hypothesised** – at least one candidate rule to be justified; otherwise the NB cannot confirm the class.  
4. **Clinical data** – literature review, clinical investigations, or equivalence justification supporting safety/effectiveness.  
5. **PMCF plan (or rationale for exemption)** – especially for classes IIa‑III.  
6. **Risk Management File** – preliminary risk analysis and identified residual risks.  
7. **PMS & vigilance procedures** – draft PMS plan, incident‑reporting workflow aligned with Art. 83‑87.  
8. **UDI assignment strategy** – device identifier, packaging level, and EUDAMED registration schedule.  
9. **Label/IFU drafts** – to verify compliance with Annex I §23.  
10. **Evidence of Authorized Representative (if applicable)** – signed power of attorney, contact details.  

*Each missing item is a “show‑stopper” for the NB’s technical file review.*

---

### 7. Risk‑control expectations  

| Requirement | Reference | Typical deliverable |
|-------------|-----------|---------------------|
| **Risk management system** (policy, plan, execution) | Annex I §3; ISO 14971:2019 | Risk Management Plan + RMF (risk analysis, evaluation, control, post‑production monitoring) |
| **Residual risk assessment & benefit–risk determination** | Annex I §8 – “known and foreseeable risks shall be outweighed by the benefits” | Benefit‑risk summary embedded in CER/PMCF reports |
| **Specific safety requirements** (e.g., for active devices, radiation, software) | Annex I §§16‑22 (depending on device type) | Evidence of conformity to IEC 60601‑2‑54, IEC 62304, IEC 62366‑1 etc. where applicable |
| **Usability engineering** (use‑error reduction) | Annex I §5 – “use errors shall be taken into account” | IEC 62366‑1 usability validation report |
| **Design controls for sterile/measuring/reusable surgical instruments** | Annex IX §2 (if Is/Im/Ir) | Sterility validation, measurement accuracy data, reusable instrument handling instructions |

---

### 8. Post‑Market Surveillance & Vigilance  

* **PMS System** – must be established per Art. 83 and described in the technical documentation (Annex III).  
* **PMS Plan** – Art. 84; includes procedures for trend analysis, PSUR preparation, and field safety corrective actions.  
* **PSUR** – required for classes IIa‑III (Art. 86); must contain benefit‑risk conclusions, PMCF findings, and sales/usage data.  
* **Vigilance reporting** – Art. 87; serious incident reporting to the Competent Authority within 15 days (aligned with Korean “의료기기법 §31”). The source also cites MDR cross‑reference to US 21 CFR 803 & MedWatch, indicating that comparable vigilance structures must be in place for any U.S. market activities.

---

### 9. Unique Device Identification (UDI)

* **Assignment** – device identifier per MDR Annex II §6.1; registration through the EUDAMED UDI/DEV module.  
* **Cross‑border** – source lists “UDI 포털 (udiportal.mfds.go.kr)” and GUDID access, implying that a UDI strategy must also cover any intended US market (if applicable).

---

### 10. Authorized Representative & Importer  

* If the manufacturer is non‑EU, an EU **Authorized Representative** must be appointed per Art. 11; their details appear in the DoC and on the label.  
* For devices imported into Korea, a local import licence holder (“수입자”) functions as the “domestic importer” – this information must be reflected in the technical file (source [1]).

---

### 11. Human‑Escalation Triggers  

| Situation | Action required |
|-----------|-----------------|
| **Insufficient device description / intended use** | Pause NB review; request full Intended Use Statement from manufacturer before proceeding with classification. |
| **Unclear classification after applying Annex VIII rules** | Escalate to senior RA or Competent Authority for guidance (refer to MDCG Manual on Borderline and Classification v2.1.1, 2023‑09 – source [2]). |
| **Missing clinical evidence for class IIa/b/III** | Trigger a Clinical Evaluation Gap Analysis; halt submission until CER/PMCF data are provided. |
| **Risk Management File incomplete or residual risk not justified** | Require completion of RMF and benefit‑risk justification before NB sign‑off. |
| **PMS plan absent or does not meet Art. 84** | Send a “PMS Deficiency Notice” and request remediation before audit. |
| **Vigilance reporting process not aligned with Art. 87 / 의료기기법 §31** | Notify the manufacturer to implement a compliant incident‑reporting workflow; involve the CA if timeliness cannot be assured. |
| **UDI registration in EUDAMED pending beyond 30 days of market entry** | Escalate to the AR and NB, noting potential non‑conformity with MDR Art. 27 (UDI obligations). |

---

### 12. Summary Judgment  

*Given the present information, a definitive classification cannot be rendered. The NB must obtain the full device description and intended use to apply Annex VIII rules correctly.*  
*Once the class is established, the appropriate conformity‑assessment route will follow Art. 52 (Annex IX for classes Is/Im/Ir/IIa/IIb/III; possible Annex X + XI for IIb/III). All evidence listed in Section 5 must be compiled and integrated into a complete technical file before the NB can issue a conformity‑assessment opinion.*

---

### 13. Peer‑review prompt  

> **To another RA colleague:**  
> Please challenge the assumptions made herein, especially regarding (a) whether any of the source excerpts provide implicit clues about the device’s likely class; (b) the completeness of the evidence checklist for borderline or software‑intensive devices; and (c) any jurisdiction‑specific obligations that may have been omitted (e.g., additional Korean post‑market reporting requirements beyond “의료기기법 §31”).  

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

> "PSUR ≥2yr IIa, annual for IIb/III" — IIb는 2년.

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

## ra_kr

### kb-eval-20261103-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "2ab5c2cc6be0971e", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "e14006879a7b7ab39dd0ecfd162427da3e451ed2ff187ebb988bf9beba930afe"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `2ab5c2cc6be0971e`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EB%B3%B4%EC%99%84%EC%9E%90%EB%A3%8C_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `e14006879a7b7ab39dd0ecfd162427da3e451ed2ff187ebb988bf9beba930afe`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_보완자료_대응전략.md`는 `MFDS_보완자료_대응전략.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) --- ### Type 1: 기술문서 보완 (가장 빈번) **빈번 사유** - 성능 데이터 불충분 (시험 방법·결과 누락) - 작용원리·사용목적 기술 불명확 - 위험관리 파일 연계 미흡 (ISO 14971) - SW 문서 미흡 (IEC 62304 산출물 누락) - 생물학적 안전성 평가...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Supplementary‑Response Strategy for MFDS 허가 / 인증 Review**  

---

### 1. Anticipated Classification & Submission Route  
| Example product (from source) | Typical Korean grade* | Default MFDS route |
|------------------------------|----------------------|--------------------|
| X‑ray Detector               | 3등급 or 4등급       | 허가                |
| Handheld X‑ray Source        | 3등급 or 4등급       | 허가                |
| 촬영실 GUI SW (software)    | 2등급 (인증 대상)   | 인증*               |

\* **Note:** The exact grade must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」.  
**Framework reference:** MFDS_인허가_상세가이드.md §2 (등급 및 인허가 경로).  

---

### 2. Processing‑time Benchmarks (from source)  

| Review type | Standard processing time* |
|-------------|---------------------------|
| 허가 (general) | **65 days** (clock stops during supplement period) |
| 허가 (clinical data included) | **80 days** |
| 인증 | **30 days** (NIFDS‑委托) |
| 신고 | Immediate |

\* Source: excerpt [1] – “허가 심사 처리 기간 (정상 회차)”.

These figures set realistic internal target dates for the *clock‑stop* period after a supplement request is issued.

---

### 3. Typical Deficiencies Requiring Supplementation  
(derived from Type 1 technical‑document supplement, most frequent cause)

| Deficiency category | Representative gaps (source [2]) |
|---------------------|----------------------------------|
| **Performance data** | Missing test methods/results (e.g., DQE/MTF for detector, kVp·mA output for source) |
| **Principle of operation / intended use** | Ambiguous description |
| **Risk‑management file linkage** | Incomplete ISO 14971 documentation; missing traceability to performance data |
| **Software documentation** | Absent IEC 62304 deliverables (e.g., software architecture, verification/validation reports) |
| **Biological safety evaluation** | No ISO 10993‑1 evidence for materials contacting patients or operator |

---

### 4. Required Evidence Package (per MFDS & Korean standards)

| Evidence type | Standard / Guideline | Intended purpose |
|---------------|----------------------|------------------|
| **Performance testing** | IEC 62220‑1‑1 (X‑ray detector), IEC 60601‑1‑3 (radiation protection) | Verify image quality, radiation output, safety functions |
| **Risk Management File** | ISO 14971 (2019) | Identify hazards, evaluate risks, document mitigations and verification |
| **Software Lifecycle Documentation** | IEC 62304 (2006+A1:2015) & IEC 81001‑5‑1 (2021) for cybersecurity | Demonstrate development process, validation, cyber‑risk controls |
| **Biological Safety Assessment** | ISO 10993‑1 (2018) | Show material biocompatibility per intended contact duration |
| **KGMP Facility Certification** | MFDS KGMP regulations (Medical Device Act 제28조) | Facility compliance for manufacturing/QA |
| **Labeling & IFU** | MFDS labeling requirements (Korean language, safety warnings) | Ensure user‑visible information meets domestic rules |
| **Clinical Evaluation (if applicable)** | MFDS Clinical Evaluation Guidance (for devices requiring clinical data) | Provide safety/effectiveness evidence; may be replaced by foreign CER only when expressly accepted (see MFDS notice – *no specific identifier found in source — verify separately*) |

All documents must be compiled according to the “Technical Documentation” format required for 허가/인증 submissions.

---

### 5. Gap Analysis – Missing Information (relative to typical deficiencies)

| Item | Current status (based on source) | Action needed |
|------|----------------------------------|---------------|
| **DQE / MTF data** for X‑ray detector | Only mentioned as “예상 항목” – not yet supplied | Initiate test with accredited lab; estimate turnaround within 2–3 weeks. |
| **kVp·mA output & radiation protection data** for handheld source | Anticipated gap, no data present | Arrange measurement per IEC 60601‑1‑3; capture calibration reports. |
| **Software lifecycle artefacts** (design docs, V&V) for GUI SW | “IEC 62304 산출물 누락” noted | Compile architecture, code listings, test cases; map to risk controls. |
| **Risk‑management traceability matrix** | “위험관리 파일 연계 미흡” flagged | Update ISO 14971 file; cross‑reference each hazard to performance/clinical data. |
| **Biocompatibility (ISO 10993‑1)** | “생물학적 안전성 평가 누락” cited | Perform material testing or submit existing foreign CER if acceptable (requires verification). |

---

### 6. Risk Controls & Mitigation Measures  

* Apply ISO 14971 hazard analysis to each identified gap – e.g., missing performance data translates to *risk of inadequate diagnostic accuracy*.  
* For software, enforce IEC 62304 development phases and incorporate IEC 81001‑5‑1 cybersecurity controls (access control, audit logging).  
* Biocompatibility risks mitigated by material substitution or additional testing per ISO 10993‑1.  
* Establish a **Supplement Response Tracker** linked to MFDS clock‑stop dates; if the projected supplement completion exceeds the standard processing time (65/80 days), trigger escalation.

---

### 7. Citation Summary  

| Category | Source citation |
|----------|-----------------|
| Processing‑time table | Excerpt [1] – “허가 심사 처리 기간 (정상 회차)” |
| Typical deficiency list & response strategy | Excerpt [2] – “Type 1: 기술문서 보완 (가장 빈번)” |
| Standards referenced (framework) | ISO 14971 (2019), ISO 10993‑1 (2018), IEC 62304 (2006+A1:2015), IEC 62220‑1‑1, IEC 60601‑1‑3, IEC 81001‑5‑1 (2021) – cited as factual standards (no specific identifier from source required). |
| Instance identifiers (e.g., MFDS notice numbers) | **No specific identifier found in source — verify separately** |

---

### 8. Human‑Escalation Triggers  

| Trigger condition | Responsible party & escalation pathway |
|-------------------|----------------------------------------|
| **Supplement deadline > MFDS clock‑stop allowance** (i.e., projected response > 65 days for 허가 or > 30 days for 인증) | RA Lead → Senior Regulatory Manager (within 2 working days). |
| **Critical safety data missing** (e.g., biocompatibility, radiation protection) | RA → QA/Clinical Team → Immediate senior management brief. |
| **Regulatory notice requiring foreign CER acceptance is ambiguous** | RA ↔ Legal / External Consultant → Seek clarification before submission (documented in GAP log). |
| **Failure to obtain test results from external lab within agreed timeline** | Project Manager → Procurement & Vendor Management → Issue corrective action plan. |

---

### 9. Peer‑Review Prompt  

*“Please review the assumptions made regarding device grades and the inferred need for 허가 versus 인증. Verify that the identified missing evidence aligns with the latest MFDS technical‑document supplement guidance, and assess whether any additional Korean‑specific obligations (e.g., post‑market surveillance plan, local clinical data) have been overlooked in this draft.”*  

--- 

*Prepared by Sam – Korea Regulatory Affairs Specialist (MFDS/KGMP).*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `233519449609923302`

> ### Type 1: 기술문서 보완 (가장 빈번) **빈번 사유** - 성능 데이터 불충분 (시험 방법·결과 누락) - 작용원리·사용목적 기술 불명확 - 위험관리 파일 연계 미흡 (ISO 14971) - SW 문서 미흡 (IEC 62304 산출물 누락) - 생물학적 안전성 평가 누락 (ISO 10993-1) **대응 전략** 1. 보완 요청서 접수 즉시 내용 분류 (Type, 소관 부서, 데이터 필요 여부) 2. 추가 시험이 필요한 항목은 즉시 시험 의뢰 (기간 역산 필요) 3. 보완서 구조: 요청 항목별 번호 대응 + 인용 근거 명시 4. 규격 시험 기관과 보완 기한 내 결과 수령 가능 여부 사전 확인 **자사 3제품 적용** | 제품 | 주요 보완 예상 항목 | |---|---| | X-ray Detector | DQE·MTF 시험 데이터, IEC 62220-1-1 적합성 | | Handheld X-ray Source | kVp·mA 출력 특성, 방사선 방호 (IEC 60601-1-3) | | 촬영실 GUI SW | IEC 62304 SW 수명주기 산출물, Cybersecurity (2025.01) | ---

### kb-eval-20261103-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "f1ddb942dbb5bad5", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용_방사선_발생장치_안전관리규칙_제1122호.md", "source_hash": "8e5622383f729436446aa67d700c35059c6cdd8849fd219b3198ab924db9275b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f1ddb942dbb5bad5`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용_방사선_발생장치_안전관리규칙_제1122호.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EC%A7%84%EB%8B%A8%EC%9A%A9_%EB%B0%A9%EC%82%AC%EC%84%A0_%EB%B0%9C%EC%83%9D%EC%9E%A5%EC%B9%98_%EC%95%88%EC%A0%84%EA%B4%80%EB%A6%AC%EA%B7%9C%EC%B9%99_%EC%A0%9C1122%ED%98%B8.md)
- Source hash: `8e5622383f729436446aa67d700c35059c6cdd8849fd219b3198ab924db9275b`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `진단용_방사선_발생장치_안전관리규칙_제1122호.md`는 `진단용_방사선_발생장치_안전관리규칙_제1122호.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 5. 프로젝트 내 연계 문서 | 연계 문서 | 연계 내용 | |-----------|----------| | X-ray_장비_안전성능_표준_매핑 | 검사 항목 ↔ IEC 표준 상세 매핑 | | ALARA_지원기능_설계명세 | ALARA 설계입력·기능사양 상세 | | SOP-CAL-001 | kVp 미터, 선량계 교정 관리 | | SOP-IQ-001 | 설치검증 절차 — 설치 시 성능 확인 | | QC-IQ-001 | 영상품질 QC 프로토콜 | | SOP-SVC-001 | 서비스 활동 — PM/교정 서비스 절차 | | 진단용방사선_안전관리규칙_개정이력 | 규칙 개정 이력 추적 | ### F-RAD-SAFETY-001: 정기검사...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Diagnostic‑X‑ray Generation Device (진단용 방사선 발생장치)**  

---

### 1. Korean Classification & Submission Route  
| Item | MFDS Determination |
|------|-------------------|
| **Device grade** | Likely **4등급** (high‑risk) — diagnostic X‑ray generators are normally placed in the highest risk tier under 「의료기기 품목 및 품목별 등급에 관한 규정」. *Confirmation required* (no specific grade identifier appears in the source). |
| **Regulatory path** | **허가** (MFDS approval) – required for 3등급·4등급 devices. |

> **Citation:** no specific identifier found in source — verify separately.

---

### 2. Core Evidentiary Requirements  

| Requirement | Content to be submitted | Reference / Mapping |
|-------------|------------------------|---------------------|
| **KGMP Facility Certification** | Proof of compliance with KGMP (의료기기법 제28조) for the manufacturing site(s). | MFDS KGMP guidance (framework). |
| **Technical Documentation (TMF)** | • Device description, intended use, indications.<br>• Korean‑language labeling & IFU (all safety statements in Korean).<br>• Risk Management File – ISO 14971:2019 (risk analysis, risk control measures, ALARA design input).<br>• Design Specification linking to the “ALARA 지원기능 설계명세” listed in the project‑linked document. | ISO 14971 (2019) – framework. |
| **Performance & Safety Test Reports** | • kVp (관전압시험) – compliance with PAE ±10% (별표1 “라”).<br>• Dose reproducibility (조사선량 재현성시험, AEC 포함) – CV ≤5% (별표1 “다”).<br>• Beam linearity – ±20%.<br>• Half‑value layer (HV​L) – Al specifications.<br>• Leakage dose ≤1 mGy/h @ 1 m.<br>• Image resolution, low contrast, uniformity – per IEC 60601‑1/IEC 62304 test criteria.<br>All tests must be traceable to the SOPs listed (SOP‑CAL‑001, SOP‑IQ‑001, QC‑IQ‑001, SOP‑SVC‑001). | *Source excerpt [2]* provides the exact acceptance criteria; mapping to IEC standards is standard practice. |
| **Software Documentation** (if applicable) | Software Development Lifecycle documentation, verification & validation per IEC 62304:2006+A1:2015. | IEC 62304 (2006+A1:2015) – framework. |
| **Clinical Evaluation** | • Clinical data demonstrating safety and performance in the intended indication.<br>• If foreign clinical evaluation reports are used, they must be acceptable under the latest MFDS notice on foreign CER acceptance (specific notice number not provided in source). Otherwise, Korean‑origin data required for 4등급. | No specific identifier found in source — verify separately. |
| **Post‑Market Surveillance Plan** | PMS activities, periodic safety updates, and adverse event reporting procedures per MFDS 시판후조사 규정. | MFDS 시판후조사 규정 – framework. |

---

### 3. Missing Information / Gaps  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Definitive grade confirmation** | The exact classification determines the submission route and evidence depth. | Verify against 「의료기기 품목 및 품목별 등급에 관한 규정」; if not 4등급, adjust pathway accordingly. |
| **Intended use statement & indication list** | Required for risk analysis, labeling, clinical evaluation scope. | Obtain from sponsor’s product specification. |
| **Korean‑language label mock‑up** | MFDS requires all labeling (including safety warnings) in Korean; missing labels prevent approval. | Request draft Korean label/IFU. |
| **Clinical data strategy** | For 4등급, local clinical data are normally mandatory unless a specific MFDS notice permits foreign CER use. | Clarify sponsor’s plan; request copy of any foreign CER and confirm acceptance under the latest MFDS notice. |
| **Evidence of conformity to ALARA principle** | “ALARA 지원기능 설계명세” is listed, but no supporting documentation shown. | Request design inputs, calculations, and validation reports demonstrating ALARA compliance. |
| **Traceability matrix linking test criteria to IEC standards** | MFDS reviewers expect clear mapping; the source provides only acceptance limits. | Prepare a matrix that aligns each test item (e.g., kVp, HVL) with the relevant IEC clause. |

---

### 4. Key Risk Controls (derived from source & Korean requirements)

| Hazard | Control Measure | Evidence |
|--------|-----------------|----------|
| Excessive tube voltage (kVp drift) | Calibration SOP‑CAL‑001; periodic self‑check per F‑RAD‑SAFETY‑001, item 1. | Calibration records; SOP. |
| Dose over‑exposure to patient/operator | Dose reproducibility & leakage limits (≤1 mGy/h); ALARA design functions; AEC performance test (item 2). | Test reports; software verification of ALARA algorithms. |
| Image quality degradation (resolution, uniformity) | QC‑IQ‑001 imaging QC protocol; periodic service SOP‑SVC‑001. | QC logs; service records. |
| High voltage breakdown / HVL variance | HVL test (item 4) per IEC 60601‑1; preventive maintenance schedule. | Test data; maintenance plan. |
| Software/firmware malfunction (if applicable) | IEC 62304 compliant development lifecycle; periodic software verification per SOP‑IQ‑001. | Software validation dossier. |

---

### 5. Citations  

| Type | Citation Detail |
|------|-----------------|
| **Framework references** (no verification caveat) | ISO 14971:2019 – risk management.<br>ISO 13485:2016 – QMS requirements.<br>IEC 60601‑1:2005+A1:2012+A2:2020 – safety general requirements for medical electrical equipment.<br>IEC 62304:2006+A1:2015 – software lifecycle. |
| **Instance identifiers** (only when present) | No specific identifier found in source — verify separately. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason | Escalation Point |
|---------|--------|-------------------|
| **Unconfirmed device grade** | Classification determines the whole submission path. | Senior RA / regulatory affairs manager review before dossier assembly. |
| **Absence of Korean labeling draft** | MFDS will reject any submission lacking compliant label/IFU. | Labeling specialist contacted; deadline set. |
| **Insufficient clinical evidence for 4등급** | Mandatory local clinical data unless a specific MFDS notice permits foreign CER. | Clinical affairs lead to provide additional data or request exemption. |
| **Failure to demonstrate ALARA compliance** (no design spec, calculation, or test) | Core safety principle; non‑compliance blocks approval. | Engineering team engaged for supplemental documentation. |
| **Non‑mapped performance test criteria** (no IEC reference matrix) | MFDS reviewers require traceability to recognized standards. | Quality assurance prepares mapping; senior QA sign‑off required. |
| **Any discrepancy between SOPs listed in the source and actual SOP availability** | Gaps may indicate missing quality system elements. | QA manager conducts gap analysis and initiates SOP creation/update. |

---

### 7. Peer Review Prompt  

*“@RA‑Peer, please evaluate the assumptions made above: *

1. *Is the default classification of diagnostic X‑ray generators as 4등급 appropriate for this specific product line, or might any sub‑category fall under a lower grade?*  
2. *Does the source provide sufficient basis to claim that foreign clinical evaluation reports could be acceptable, given no notice number is cited?*  
3. *Are there any additional Korean regulatory instruments (e.g., 고시 제2025‑22호) that we should reference for the safety test limits listed in F‑RAD‑SAFETY‑001?*  

*Your feedback on any jurisdictional gaps or missing evidence will be incorporated before final dossier preparation.”*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1114051458699792259`

> ## 5. 프로젝트 내 연계 문서 | 연계 문서 | 연계 내용 | |-----------|----------| | X-ray_장비_안전성능_표준_매핑 | 검사 항목 ↔ IEC 표준 상세 매핑 | | ALARA_지원기능_설계명세 | ALARA 설계입력·기능사양 상세 | | SOP-CAL-001 | kVp 미터, 선량계 교정 관리 | | SOP-IQ-001 | 설치검증 절차 — 설치 시 성능 확인 | | QC-IQ-001 | 영상품질 QC 프로토콜 | | SOP-SVC-001 | 서비스 활동 — PM/교정 서비스 절차 | | 진단용방사선_안전관리규칙_개정이력 | 규칙 개정 이력 추적 |

2. Chunk `1114990759153006214`

> ### F-RAD-SAFETY-001: 정기검사 항목 대응 자체 점검 양식 | No. | 검사 항목 | 규칙 기준 | 출하 시험 SOP 참조 | 출하 시험 합격 기준 | 고객 PM 점검 포함 | 비고 | |-----|----------|----------|-------------------|-------------------|-----------------|------| | 1 | 관전압시험 | PAE ±10% (별표1 "라") | | | ☐Yes ☐No | | | 2 | 조사선량 재현성시험(AEC 포함) | CV ≤5%(0.05) (별표1 "다", 단일 항목) | | | ☐Yes ☐No | | | 3 | 선량 직선성 | ±20% | | | ☐Yes ☐No | | | 4 | 반가층(HVL) | Al 규격 | | | ☐Yes ☐No | | | 5 | 누설선량 | ≤1mGy/h@1m | | | ☐Yes ☐No | | | 6 | 영상 해상도 | lp/mm 규격 | | | ☐Yes ☐No | | | 7 | 저대조도 | 규격 | | | ☐Yes ☐No | | | 8 | 균일성 | 규격 | | | ☐Yes ☐No | | | 9 | 조사야 정확도 | ±2% SID | | | ☐Yes ☐No | | | 10 | AEC 밀도 재현성 | ±0.3 OD | |...

### kb-eval-20261103-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "5bef9b2343a71831", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5bef9b2343a71831`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%ED%91%9C%EC%8B%9C%EA%B8%B0%EC%9E%AC_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_%EB%8C%80%EC%9D%91.md)
- Source hash: `7f7da02c831fb1539ec6f9095f23a553f724c4611950f8aadf8d3cab1bf61b42`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_디지털의료기기_표시기재_가이드라인_대응.md`는 `MFDS_디지털의료기기_표시기재_가이드라인_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 9. 의료기기법 일부개정 (법률 제21949호, 공포 2026-09-15) — 온라인 표시·광고 규제 강화 | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 |...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital Medical‑Device Software (General‑Purpose “SW 일반”)**

---

### 1. Korean Classification & Submission Route  
| Item | Current Evidence | RA Judgment |
|------|------------------|------------|
| **Device grade** | Not identified in the source excerpts. | The grade (1등급 ~ 4등급) must be confirmed from **「의료기기 품목 및 품목별 등급에 관한 규정」**.  <br>→ *If the device is 1등급 → 신고*  <br>*If 2등급 → 인증 (MFDS‑designated 심사기관 review)*  <br>*If 3·4등급 → 허가.* |
| **Relevant legislative amendment** | 의료기기법 일부개정 (법률 제21949호, 공포 2026‑09‑15) – strengthens online display/advertising regulation. | The amendment expands the labeling burden for digital products; compliance must be demonstrated in the submission. |

> **Human‑Escalation Trigger #1** – *Classification uncertainty*: request a formal grade determination before finalizing the dossier.

---

### 2. Required Evidence (per MFDS SW & Cybersecurity Guidelines)

| Requirement | Source (Citation) | Minimum Evidence to Submit |
|-------------|-------------------|----------------------------|
| **Software version / build number / release date** | ✅ S‑1 – *디지털의료제품법 시행규칙* | Software Release Sheet (Korean translation) showing version, build ID, and official release date. |
| **Software update method & schedule** | ✅ S‑2 – *MFDS SW 가이드라인* | Update Policy Document describing delivery mechanism (OTA, manual), frequency, and rollback procedure. |
| **Minimum / recommended system specifications** (OS, CPU, RAM, storage, monitor resolution, network) | ✅ S‑3 – *MFDS SW 가이드라인* | System Requirements Specification (Korean) listing mandatory and optional specs. |
| **List of compatible medical devices & interface details** | ✅ S‑4 – *(no explicit source cited)* | Compatibility Matrix detailing each device model, connector type, communication protocol, and any required adapters. <br>*(Citation note: no specific identifier found in source – verify separately.)* |
| **Data input/output format (DICOM, HL7, etc.)** | ✅ S‑5 – *(no explicit source cited)* | Data Exchange Specification describing supported standards, version numbers, and mapping tables. <br>*(Citation note: no specific identifier found in source – verify separately.)* |
| **Cybersecurity configuration guidance** (password policy, network segmentation, access rights) | ✅ S‑6 – *MFDS 사이버보안 가이드라인 2025.01* | Cybersecurity Configuration Manual (Korean) with detailed settings and justification. |
| **Security‑patch deployment procedure & responsibility assignment** | ✅ S‑7 – *MFDS 사이버보안 가이드라인 2025.01* | Patch Management Plan including schedule, responsible roles, verification steps, and change‑control records. |
| **Known residual cyber‑risk & mitigation strategy** | ✅ S‑8 – *MFDS 사이버보안 가이드라인 2025.01* | Residual Risk Register (post‑risk‑assessment) identifying any remaining vulnerabilities and their accepted mitigations. |
| **Data backup & recovery methodology** | ✅ S‑9 – *(no explicit source cited)* | Backup & Disaster Recovery SOP describing frequency, storage media, encryption, and restoration test results. <br>*(Citation note: no specific identifier found in source – verify separately.)* |
| **System log management method** (recommended) | ⚠️ S‑10 – *MFDS 사이버보안 가이드라인* | Log Management Procedure covering collection, retention period, integrity checks, and access controls. *(Recommendation; inclusion strengthens the dossier.)* |
| **AI/ML component description & validation** | “**AI/ML…**” truncated in source – no details provided. | • Algorithm Description (architecture, training data, intended use). <br>• Performance Evaluation Report (clinical or simulated). <br>• Explainability & bias mitigation plan.<br>*(Citation note: no specific identifier found in source – verify separately.)* |

---

### 3. Additional Mandatory Dossiers (Not Covered in Source)

| Item | Reason for Requirement | Evidence Needed |
|------|-----------------------|-----------------|
| **Risk Management File** (ISO 14971 2019) | Core Korean requirement for all medical devices (KGMP). | Risk Management Plan, Hazard Analyses, Risk Evaluation Table, and post‑market risk‑monitoring plan. |
| **Korean Language Labeling & IFU** | MFDS insists on Korean‑only labeling for domestic market. | Full product label, packaging text, and Instructions for Use in Korean; include all items listed above. |
| **KGMP Facility Certification** (품질관리 기준) | Required for manufacturing of devices ≥2등급. | KGMP certificate issued by MFDS or recognized accreditation body. |
| **Clinical Evidence (if required)** | Depending on device grade and risk level, local clinical data may be mandatory. | Clinical Evaluation Report (CER) – Korean‑language version; if foreign CER is used, verify acceptance under current MFDS notice. |
| **Foreign Clearance Reference** (e.g., FDA 510(k), EU CE) | Often accepted as supporting evidence but not a substitute for local requirements. | Copies of clearance certificates and bridging justification. *(Citation note: no specific identifier found in source – verify separately.)* |

> **Human‑Escalation Trigger #2** – *Evidence gaps*: if any of the above items cannot be supplied within the project timeline, flag to senior RA/Project Lead for mitigation (e.g., additional clinical study, KGMP certification plan).

---

### 4. Risk Controls & Compliance Measures

1. **Cybersecurity** – Implement the controls enumerated in S‑6 through S‑10; conduct penetration testing and periodic vulnerability scans; retain reports for MFDS review.  
2. **Software Lifecycle Management** – Align with IEC 62304 (2006+A1:2015) for software development processes; maintain version control and configuration management.  
3. **Usability Engineering** – Follow IEC 62366‑1 (2015+A1:2020) to verify that UI/UX meets Korean user expectations, especially for AI/ML decision support.  
4. **Post‑Market Surveillance (PMS)** – Establish a PMS system per MFDS “시판후조사” requirements; include adverse event reporting, field safety corrective actions, and periodic safety update reports.  

---

### 5. Citation Summary

| Category | Reference |
|----------|-----------|
| Legislative amendment strengthening online display/advertising | 의료기기법 일부개정 (법률 제21949호, 공포 2026‑09‑15) |
| Software labeling items (S‑1~S‑9) | 디지털의료제품법 시행규칙; MFDS SW 가이드라인 |
| Cybersecurity items (S‑6~S‑10) | MFDS 사이버보안 가이드라인 2025.01 |
| Standards for risk management, software life‑cycle, usability | ISO 14971:2019; IEC 62304 2006+A1:2015; IEC 62366‑1 2015+A1:2020 |

*No other specific notice or article numbers appear in the provided excerpts; any additional identifiers must be verified separately.*

---

### 6. Human‑Escalation Triggers (Decision Points)

| # | Trigger | Action Required |
|---|---------|-----------------|
| **1** | Uncertain device grade (1~4등급) | Obtain formal classification from MFDS or refer to the “의료기기 품목 및 품목별 등급에 관한 규정”. |
| **2** | Missing AI/ML documentation (algorithm, validation) | Pause dossier finalization; collect model details, training data provenance, and performance metrics. |
| **3** | Absence of KGMP certificate for manufacturing site | Initiate KGMP certification process or secure a subcontractor with valid certification. |
| **4** | Incomplete Korean labeling/IFU (e.g., missing S‑4, S‑5, backup/recovery details) | Engage translation/technical writing team to produce the required Korean documents. |
| **5** | No clinical evidence where grade or risk level mandates it | Plan and conduct a local clinical study or seek MFDS acceptance of foreign CER under current notice. |

Escalation should be reported to the **Project Lead & Senior RA Manager** with a risk‑impact matrix indicating potential timeline extensions.

---

### 7. Peer Review Prompt

> *Please review the assumptions made regarding (a) the missing AI/ML component details, (b) the implied need for KGMP certification based on the unspecified grade, and (c) any jurisdiction‑specific gaps not covered by the cited MFDS guidelines (e.g., post‑market reporting periods or labeling layout specifications). Identify any additional evidence that should be gathered before final submission.*

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

1. Chunk `1044206327041877533`

> ## 9. 의료기기법 일부개정 (법률 제21949호, 공포 2026-09-15) — 온라인 표시·광고 규제 강화

2. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

### kb-eval-20261103-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "03f6a50f1f7cc52b", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_6종_가이드라인_요약.md", "source_hash": "ad43d170968f637c7a8f6ecabcf4eafcc3bb63e22454c7980fcbc5708829050b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `03f6a50f1f7cc52b`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_6종_가이드라인_요약.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_6%EC%A2%85_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_%EC%9A%94%EC%95%BD.md)
- Source hash: `ad43d170968f637c7a8f6ecabcf4eafcc3bb63e22454c7980fcbc5708829050b`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_디지털의료기기_6종_가이드라인_요약.md`는 `MFDS_디지털의료기기_6종_가이드라인_요약.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 2. 6종 가이드라인 개요 | 번호 | 구분 | 가이드라인명 | 주요 적용 대상 | |---|---|---|---| | 1 | **제정** | 디지털의료기기소프트웨어 허가·심사 가이드라인 | 내장형·독립형 소프트웨어 전반 공통 기본서 | | 2 | 개정 | 의료기기 소프트웨어 허가·심사 가이드라인 | **내장형** 소프트웨어 + 의료기기 연동 앱·웹 | | 3 | 개정 | 인공지능기술이 적용된 디지털의료기기 허가·심사 가이드라인 | MLMD(Machine Learning-enabled Medical Device) 전반 | | 4 | 개정 | 가상융합기술이 적용된 디지털의료기기 허가·심사 가이드라인 | VR·AR·MR 기술 적용...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Digital‑Medical‑Device Software (AI/ML‑enabled)  

Prepared for: Korean RA team (MFDS jurisdiction)**  

---

### 1. Device Overview (to be completed by the project owner)  
| Item | Comment |
|------|---------|
| **Intended use / indication** | e.g., “Automated analysis of retinal images for diabetic retinopathy screening” – *required to finalize classification and clinical‑data needs*. |
| **Device type** | AI/ML‑enabled software (stand‑alone or embedded). |
| **Technology** | Machine‑Learning model, possible continuously‑learning algorithm. |
| **Target user** | Healthcare professional / patient (specify). |
| **Risk level** | Not yet determined – must be mapped to the Korean grade 1‑4등급 per 「의료기기 품목 및 품목별 등급에 관한 규정」. |

> **Action:** Confirm the above details; they drive every subsequent regulatory step.

---

### 2. Classification & Submission Route  

| Korean Grade | Typical submission track | When applicable (based on device facts) |
|--------------|--------------------------|----------------------------------------|
| **1등급** | 신고 (notification) | Low‑risk, non‑invasive software without diagnostic claim. |
| **2등급** | 인증 (technical‑document review by MFDS‑designated 심사기관) | Moderate risk; e.g., diagnostic support tools that do not provide final decision. |
| **3등급 / 4등급** | 허가 (full approval by MFDS) | High‑risk, therapeutic delivery or autonomous diagnosis, especially if continuous‑learning is intended. |

> **Current status:** No grade is provided in the source material. The project must obtain the correct grade from the official “의료기기 품목 및 품목별 등급에 관한 규정” (MFDS_인허가_상세가이드.md §2). *No specific identifier found in source – verify separately.*

---

### 3. Required Evidence (per the six digital‑medical‑device guidelines)  

| Evidence Category | Mandatory items under the relevant guideline(s) |
|-------------------|--------------------------------------------------|
| **Technical Documentation** | • System architecture, algorithm type & structure.<br>• Training‑data set management plan (source, curation, labeling).<br>• Performance evaluation methodology and results (including sensitivity/specificity, ROC curves, etc.).<br>• Statement on whether the algorithm is continuously learning (Continuously Learning 여부) – must be disclosed in the “성능(기능) 또는 특성” section. |
| **Risk Management** | • ISO 14971:2019–based risk analysis (hazard identification, risk evaluation, mitigation).<br>• Specific AI‑risk controls (bias mitigation, data drift monitoring). |
| **Clinical Evidence** | • If foreign clinical evaluation reports are used, they must meet the MFDS acceptance criteria for CERs; otherwise a Korean‐conducted clinical study is required (see MFDS guidance on “인공지능기술이 적용된 디지털의료기기 허가·심사 가이드라인”). |
| **Cybersecurity** | • Conformity with IEC 81001‑5‑1:2021 (referenced in MFDS cyber‑security guideline). |
| **Quality System** | • KGMP certification for the manufacturing organization (법률 제28조, 2026‑07‑01 개편 이후 적용). |
| **Labeling & IFU** | • All labeling, instructions for use and software user manual must be in Korean, meeting MFDS labeling requirements. |
| **Post‑Market Surveillance** | • PMS plan per MFDS 시판후조사 규정 (including periodic safety updates for AI models). |

> **Guideline citations:**  
> – “인공지능기술 적용 디지털의료기기 허가·심사 가이드라인 (개정)” – core AI/ML requirements (training‑data plan, algorithm description, performance, continuous learning) are explicitly listed in the source excerpt.  
> – Terminology & scope harmonised with **고시 제2025‑23호** and **고시 제2025‑25호** (see source).  

---

### 4. Gaps / Missing Information (to trigger a “human‑escalation”)  

| Gap | Why it matters | Escalation trigger |
|-----|----------------|-------------------|
| **Device grade (1‑4등급)** not yet assigned | Determines submission track and evidence depth. | Immediate review with classification expert; cannot proceed to dossier assembly without this decision. |
| **Korean‑language labeling draft** | MFDS requires all user‑facing documents in Korean; missing drafts block dossier completeness. | Flag to label/translation team; hold submission until completed. |
| **Local clinical data plan** | If foreign CER is not acceptable under current MFDS policy, a Korean clinical study must be planned. | Escalate to Clinical Development Lead if foreign evidence cannot be justified. |
| **Continuous‑learning algorithm declaration** – decision whether the model will update post‑approval. | Continuous learning triggers additional notification and periodic performance re‑evaluation requirements (see AI guideline). | Notify regulatory manager; may require separate “AI algorithm 업데이트 신고” before market launch. |
| **KGMP certification status** of the software development/maintenance environment. | KGMP is mandatory for any medical‑device manufacturer, including software only. | Escalate to Quality Assurance if certification not yet obtained. |
| **Cybersecurity risk assessment** (IEC 81001‑5‑1) documentation. | MFDS cyber‑security guideline demands a formal assessment; missing → non‑compliance. | Alert IT/Engineering for evidence collection. |

---

### 5. Risk Management & Control Measures  

| Control | Standard / Guideline Basis | Implementation Note |
|---------|----------------------------|---------------------|
| **Hazard analysis & risk evaluation** | ISO 14971:2019 (risk‑management framework) | Conduct full FMEA covering data quality, algorithm bias, misclassification. |
| **Algorithm performance monitoring** | AI guideline – “훈련 데이터셋 관리 계획”, “성능평가 방법” | Define real‑world performance metrics; set thresholds for corrective action. |
| **Data governance** | AI guideline – training‑data management plan | Document data provenance, anonymisation, and consent. |
| **Cybersecurity controls** | IEC 81001‑5‑1:2021 (referenced by MFDS) | Implement secure coding, vulnerability scanning, incident response plan. |
| **Post‑market surveillance (PMS)** | MFDS 시판후조사 규정 | Submit periodic safety reports; include AI drift detection results. |

---

### 6. Additional Korean Regulatory Obligations  

1. **KGMP facility certification** – mandatory for any entity that manufactures, assembles, or modifies the software intended as a medical device (법률 제28조).  
2. **Labeling & IFU in Korean** – must comply with MFDS labeling standards; any foreign language material is supplementary only.  
3. **Electronic submission format** – use the MFDS e‑submission portal (HIRA/MFDS), providing documents in HWP or PDF as specified.  

---

### 7. Human‑Escalation Triggers (summary)  

| Condition | Who to Alert | Reason |
|-----------|--------------|--------|
| Grade not yet defined / ambiguous | Classification specialist & Project Lead | Determines submission pathway. |
| Lack of Korean labeling/IFU draft | Regulatory affairs – documentation team | Required for dossier completeness. |
> If any of the above gaps remain unresolved after 5 business days, the regulatory manager must be notified to decide whether to pause the filing schedule.

---

### 8. References (as extracted from source)  

| Type | Citation |
|------|----------|
| **Guideline – AI‑enabled digital medical device** | “인공지능기술 적용 디지털의료기기 허가·심사 가이드라인 (개정)” – core AI/ML requirements. |
| **Notice numbers defining terminology & scope** | 고시 제2025‑23호, 고시 제2025‑25호 (mentioned in source excerpt [2]). |
| **Standard for risk management** | ISO 14971:2019 (framework reference). |
| **Standard for quality‑management system** | ISO 13485:2016 (framework reference). |
| **Cybersecurity standard referenced by MFDS** | IEC 81001‑5‑1:2021 (framework reference). |

> No other instance identifiers (e.g., device registration numbers, specific article/section numbers) appeared in the source excerpts; therefore none are inserted.  

---

### 9. Peer‑Review Prompt  

*To the RA peer reviewing this draft:*  

- **Assumptions:** The device is assumed to be AI/ML‑enabled software. Confirm whether it is stand‑alone or embedded, and whether continuous learning will be employed.  
- **Source Coverage:** Verify that no additional guideline versions (e.g., newer amendment notices) exist beyond those cited (2025‑23호, 2025‑25호).  
- **Jurisdiction Gaps:** Check if any supplemental MFDS “공통 안전성·유효성 검토 기준” apply to this device class, and whether a local clinical trial exemption is possible under the current foreign CER acceptance policy.  

Please challenge any gaps or suggest additional evidence items needed for a complete submission.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1059459999498570675`

> ## 2. 6종 가이드라인 개요 | 번호 | 구분 | 가이드라인명 | 주요 적용 대상 | |---|---|---|---| | 1 | **제정** | 디지털의료기기소프트웨어 허가·심사 가이드라인 | 내장형·독립형 소프트웨어 전반 공통 기본서 | | 2 | 개정 | 의료기기 소프트웨어 허가·심사 가이드라인 | **내장형** 소프트웨어 + 의료기기 연동 앱·웹 | | 3 | 개정 | 인공지능기술이 적용된 디지털의료기기 허가·심사 가이드라인 | MLMD(Machine Learning-enabled Medical Device) 전반 | | 4 | 개정 | 가상융합기술이 적용된 디지털의료기기 허가·심사 가이드라인 | VR·AR·MR 기술 적용 의료기기 | | 5 | 개정 | 디지털치료기기 허가·심사 가이드라인 | **독립형** SW 중 질병 예방·관리·치료 목적 제품 | | 6 | 개정 | 인공지능기술이 적용된 디지털의료기기 임상시험방법 설계 가이드라인 | AI 적용 의료기기 임상시험계획 승인 | > **구조**: 가이드라인 1번(신제정)이 기본서 역할, 2~6번은 기본서를 보완하는 계층 구조. ---

2. Chunk `14197495515627229`

> ### 3-3. 인공지능기술 적용 디지털의료기기 허가·심사 가이드라인 (개정) **주요 개정 내용**: - 용어·적용범위를 고시 제2025-23호·제2025-25호에 맞게 정비 - 첨단기술 정의 예시 추가 → 디지털의료기기 특성 명확화 - '성능(기능) 또는 특성' 항목에 **디지털기술 세부특성 기재사항** 추가 - 동등비교를 통한 제출자료 범위[별표7], 절차표 삭제 (신고시 체계 반영) **MLMD 핵심 요건**: 훈련 데이터셋 관리 계획, 알고리즘 유형·구조, 성능평가 방법, 지속학습(Continuously Learning) 여부 신고.

### kb-eval-20261103-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-11-03", "decision_ref": "kb-eval-20261103-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "53f15be8211d6cdf", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `53f15be8211d6cdf`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EC%82%AC%EC%9D%B4%EB%B2%84%EB%B3%B4%EC%95%88_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_2025_%EB%8C%80%EC%9D%91.md)
- Source hash: `87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_사이버보안_가이드라인_2025_대응.md`는 `MFDS_사이버보안_가이드라인_2025_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 | ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `supplementary-response strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `supplementary-response strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 보완 요청 대응 구조, 요청 evidence, rationale, 한국어 표현, escalation 필요성을 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Cybersecurity Regulatory Draft – MFDS Submission (Korean Medical Devices)**  

---

### 1. Device Classification & Submission Route  
| Korean grade | Typical submission route | Relevance of the cyber‑security guideline |
|--------------|--------------------------|-------------------------------------------|
| **1등급** | 신고 (notification) | Cyber‑security requirements are *not* a statutory prerequisite for pure “신고” items, but MFDS may still request a brief security statement if the device processes personal health data. |
| **2등급** | 인증 (technical‑documentation review by an MFDS‑designated 심사기관) | The 2025 cyber‑security guideline is expressly applied to devices undergoing 인증. All 35 RA items must be addressed in the submission dossier. |
| **3등급·4등급** | 허가 (full approval by MFDS) | Full compliance with the 35 cyber‑security requirements is mandatory; the security dossier forms a core part of the 허가 package. |

> **Action:** The exact grade for the product must be confirmed from 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS_인허가_상세가이드.md §2). Until that is known, assume the most stringent route (**인증/허가**) and prepare the full security dossier.

---

### 2. Applicable Regulations & Standards  

| Category | Reference (framework) | Source citation |
|----------|----------------------|-----------------|
| Legal basis for the guideline | **디지털의료제품법** (effective 2025‑01‑24) 및 의료기기법 시행규칙 | Excerpt [1] – “법적 근거」 |
| Cybersecurity Guideline document | *의료기기의 사이버보안 허가·심사 가이드라인* (개정일 2025‑01‑10) | Excerpt [1] |
| International alignment | IMDRF **N60** / **N73**; IEC **81001‑5‑1** (2021) | Excerpt [1] – “조화 목적” |
| Korean‐language requirement | All labeling, IFU and security documentation must be provided in Korean per MFDS 고시 on labeling (no specific notice number appears in the source). | — |
| KGMP compliance | 제조·품질관리자는 KGMP(의료기기법 제28조) 인증을 받아야 함. | Standard knowledge |

*No instance‑level identifiers (e.g., 고시 번호, 조/항) are present in the supplied excerpts; verification of exact notice numbers is required separately.*

---

### 3. Required Evidence & Documentation  

| Requirement Category (RA‑01 ~ RA‑35) | Typical evidence to be submitted |
|-------------------------------------|----------------------------------|
| **보안 설계 원칙** (Secure by design, Defense‑in‑depth, Least privilege) | Security Architecture Diagram; Design Rationale; Threat Modeling report |
| **인증·접근 제어** (User authentication, role‑based access, session management) | Access‑Control Policy; IAM configuration screenshots; Session timeout settings |
| **암호화** (Data at rest & in transit encryption, key management) | Encryption algorithm list (e.g., AES‑256); Key‑management SOP; Certificate chain documentation |
| **소프트웨어 무결성** (Code signing, boot integrity, SBOM) | Code‑signing certificates; Bootloader verification flow; Software Bill‑of‑Materials (SBOM) in SPDX format |
| **네트워크 보안** (Port minimization, firewall, TLS version) | Network topology with closed ports; Firewall rule set; TLS 1.2/1.3 configuration evidence |
| **취약점 관리** (CVE monitoring, patch cadence, CVD policy) | Vulnerability Management Plan; CVE feed subscription proof; Patch‑release schedule |
| **감사·로그** (Security event logging, log protection, access history) | Log‑collection architecture; Sample logs with tamper‑evidence; Retention policy (≥ 12 months) |
| **업데이트·유지보수** (Secure update mechanism, remote management security) | OTA update process description; Digital signature verification for updates; Remote‑access hardening controls |

Additional mandatory items:  

* **Korean-language Security Dossier** – full description of all above items in Korean.  
* **KGMP Certificate** – proof that the manufacturing site is KGMP‑certified.  
* **Risk Management File (ISO 14971:2019)** – to demonstrate that identified cyber risks have been mitigated per the 35 RA controls.  

---

### 4. Identified Gaps / Missing Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Device grade & intended use** | Determines whether 인증 or 허가 route applies and which sections of the guideline are enforceable. | Obtain the product’s classification from the MFDS “품목·등급” list. |
| **Existing security controls description** | Needed to map current state against the 35 RA items. | Conduct an internal gap analysis and produce a control‑mapping matrix. |
| **Foreign regulatory evidence (e.g., FDA 510(k), CE Mark)** | MFDS may accept foreign CERs for non‑clinical data, but only if explicitly referenced in a notice; no such identifier is present in the source. | Verify whether any foreign clearance exists and request MFDS guidance on acceptance. |
| **Exact 고시 번호 or 조/항** that mandates cyber‑security compliance for each grade | Without precise citation, reviewers may request clarification. | Search MFDS 고시 database for the latest “의료기기 사이버보안” notice (e.g., 고시 제2025‑xx호) and record the number. |
| **Korean‑language labeling & IFU** beyond security dossier | Required by law; omission blocks approval. | Prepare Korean label mock‑ups and IFU sections reflecting security warnings. |

---

### 5. Recommended Risk Control Alignment  

| RA Category | Suggested control (example) | Reference to guideline |
|------------|-----------------------------|------------------------|
| 보안 설계 원칙 | Adopt “Secure Development Lifecycle” (SDL) with threat modeling at each phase. | Excerpt [2] – category **보안 설계 원칙** |
| 인증·접근 제어 | Implement multi‑factor authentication for all privileged users; enforce least‑privilege RBAC. | Excerpt [2] – **인증·접근 제어** |
| 암호화 | Use AES‑256 GCM for data at rest; TLS 1.3 with forward secrecy for transmission. | Excerpt [2] – **암호화** |
| 소프트웨어 무결성 | Digitally sign all firmware; verify bootloader signatures on power‑up; maintain an SBOM. | Excerpt [2] – **소프트웨어 무결성** |
| 네트워크 보안 | Close all non‑essential ports; deploy a hardware firewall with logging; enforce TLS 1.3 only. | Excerpt [2] – **네트워크 보안** |
| 취약점 관리 | Subscribe to NVD CVE feed; schedule monthly vulnerability scans; apply patches within 30 days of release. | Excerpt [2] – **취약점 관리** |
| 감사·로그 | Centralize logs in a tamper‑evident SIEM; retain for ≥ 12 months; restrict log access to security team. | Excerpt [2] – **감사·로그** |
| 업데이트·유지보수 | Deploy signed OTA updates; require device authentication before remote commands; document update rollback procedure. | Excerpt [2] – **업데이트·유지보수** |

All controls should be cross‑referenced to the ISO 14971 risk analysis and documented in Korean.

---

### 6. Human‑Escalation Triggers  

| Trigger condition | Required human action |
|-------------------|-----------------------|
| **Unclear device grade** (cannot locate product in the MFDS 등급 list) | RA lead to request clarification from product development; if unresolved, escalate to senior regulatory manager. |
| **Missing 고시 번호 or 조/항 for cyber‑security requirement** | Assign a researcher to query the MFDS 고시 database; if still unavailable after 5 business days, involve legal counsel. |
| **Foreign clearance evidence not accepted** (MFDS rejects FDA/CE CER) | Senior RA to negotiate with MFDS via 공식 질의 (official inquiry). |
| **Significant gaps in any of the 35 RA categories (>30 % of controls missing)** | Immediate project pause; conduct a detailed security redesign before resubmission. |
| **Failure to obtain KGMP certification for manufacturing site** | Halt submission; engage quality‑system experts to achieve KGMP compliance; report status to senior management. |
| **Korean‑language labeling not finalized 30 days before planned filing** | Trigger translation team escalation; legal review of Korean text for regulatory compliance. |

---

### 7. Peer‑Review Prompt  

> **Please review:**  
> - Whether the assumption that the 35 cyber‑security RA items apply to **both 인증 and 허가** routes is accurate, or if MFDS distinguishes a subset for 1등급 신고.  
> - The completeness of the evidence list (are any mandatory artifacts—e.g., ‘Cyber‑Risk Management Plan’ as defined in IMDRF N73—still missing?).  
> – Any additional Korean‑specific citations (고시 번호, 조/항) that should be incorporated now rather than flagged for later verification.  

--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
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

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---
