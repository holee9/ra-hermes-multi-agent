# KB Eval Checksheet - 2026-07-16 Iteration 03

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260716-it03-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_us-001", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "b09c788de30adb23", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `b09c788de30adb23`
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

> **Regulatory Draft – Impact of SaMD Change (AI/ML‑based medical device)**  

---

### 1. Likely FDA Classification & Submission Pathway
| Item | Reasoning |
|------|-----------|
| **Device Class** | AI‑driven Software as a Medical Device (SaMD) that provides diagnostic or treatment recommendations is typically **Class II**. If the algorithm performs a novel function with no reasonable predicate, a **De Novo** classification may be required. |
| **Primary Submission Route** | **510(k) – Substantial Equivalence** (if an appropriate predicate exists). <br>If no predicate can be justified, pursue **De Novo Classification Request**. |
| **Regulatory Requirement** | Incorporate a **Predetermined Change Control Plan (PCCP)** as mandated by the FDA’s “Artificial Intelligence‑Based Software as a Medical Device – Predetermined Change Control Plan” guidance (2024‑12‑04). |

*Citation*: No specific identifier found in source — verify separately.  

---

### 2. Required Evidence for Submission

| Evidence Category | Minimum Content | Source Reference |
|-------------------|-----------------|------------------|
| **Intended Use & Indications** | Clear statement of clinical purpose, patient population, and intended decision‑making role (e.g., assistive vs. autonomous). | – |
| **Predicate Device Comparison** | Side‑by‑side table showing device name, 510(k) number, regulation classification, and points of similarity/difference (hardware, algorithm type, risk profile). | – |
| **PCCP Documentation** | • **Data Management** – description of data collection, curation, versioning, bias mitigation. <br>• **Retraining Practices** – trigger conditions, retraining workflow, rollback plan. <br>• **Performance Evaluation** – predefined acceptance criteria, validation methodology, statistical significance thresholds.<br>• **Updated Procedures** – communication to users/clinicians, real‑world monitoring, IFU update process. | Excerpt [2] |
| **Verification & Validation (V&V)** | • Analytical performance (algorithm accuracy, precision, robustness). <br>• Clinical validation against a reference standard or ground truth in the intended use setting. <br>• Usability testing demonstrating safe interaction. | – |
| **Risk Management** | IEC 62304 software life‑cycle processes; ISO 14971 risk analysis showing identified hazards (e.g., misclassification, bias, cybersecurity) and mitigations (including human‑in‑the‑loop safeguards). | – |
> *Note*: The FDA guidance on PCCP (2024‑12‑04) explicitly requires the four items listed above.  

*Citation*: No specific identifier found in source — verify separately.  

---

### 3. Missing Information (Typical Gaps)

| Gap | Why It Matters | How to Address |
|-----|----------------|----------------|
| **Predicate Device Identifier** | Needed for a 510(k) claim of substantial equivalence. | Conduct market search; select device with same intended use and similar AI/ML approach. |
| **Detailed Intended Use Statement** | Drives classification and risk analysis. | Draft precise language (e.g., “software that provides a probability score for X disease based on imaging data”). |
| **Algorithm Change Scope Definition** | Determines whether the PCCP covers the change or a new submission is required. | Define “locked” vs. “adaptive” algorithm boundaries; document in the change protocol. |
| **Real‑World Performance Monitoring Plan** | Required for post‑market surveillance and for triggering PCCP updates. | Outline data sources, frequency of analysis, escalation thresholds. |
| **Human‑Oversight / Escalation Logic** | Critical to mitigate risk when AI outputs are uncertain or out‑of‑distribution. | Specify confidence thresholds, default to clinician review, and documentation of override actions. |
| **Cybersecurity Controls** | FDA expects protection against unauthorized access/modification of the algorithm. | Provide threat model, mitigation strategies, and post‑market patching process. |
| **Labeling & IFU Update Process** | Users must be informed of any change that could affect device performance. | Include procedures for rapid label revision per PCCP “Updated Procedures” item. |

---

### 4. Core Risk Controls (to be reflected in the submission)

1. **Pre‑Market Validation:** Independent test set, external validation cohort, statistical power ≥ 80 % to meet acceptance criteria.
2. **Bias & Fairness Management:** Documentation of demographic representation; mitigation strategies if disparity identified.
3. **Rollback Capability:** Ability to revert to previous algorithm version automatically upon detection of performance degradation.
4. **Human‑In‑the‑Loop Escalation Triggers:**  
   - Confidence score < predefined threshold (e.g., 0.70).  
   - Detection of out‑of‑distribution input (novel imaging modality, artifact).  
   - Failure to meet acceptance criteria during periodic re‑validation.  
5. **Post‑Market Surveillance:** Continuous collection of real‑world outcomes; quarterly performance reports.
6. **Cybersecurity Measures:** Secure code signing, encrypted data transmission, regular vulnerability assessments.

---

### 5. Human‑Escalation Triggers (Operational)

| Trigger | Action |
|---------|--------|
| **Algorithm confidence falls below threshold** | Prompt clinician review; device logs flag for audit. |
| **Significant shift in performance metrics (> 10 % drop from baseline)** | Initiate rollback to prior validated version; notify FDA under 510(k) change reporting if material. |
| **Detected data bias or adverse event pattern** | Suspend algorithm updates; conduct root‑cause analysis; update PCCP and IFU accordingly. |
| **Security breach or unauthorized modification detected** | Immediate device quarantine; issue safety notice; submit a recall if risk to patient safety is probable. |

---

### 6. Citations

- Predetermined Change Control Plan (PCCP) guidance elements – Data Management, Retraining Practices, Performance Evaluation, Updated Procedures: **Excerpt [2]**.  
- References to the FDA AI/ML “Predetermined Change Control Plan” guidance and related Federal Register notice: **Excerpt [1]**.

*No specific 510(k), predicate, or case identifiers appear in the provided source excerpts; verify these separately before final submission.*

---

### 7. Peer‑Review Prompt (for an RA colleague)

> *Please review the assumptions underlying our classification choice (Class II 510(k) vs. De Novo), the completeness of the PCCP elements captured from the source, and any jurisdictional gaps—especially regarding EU MDR interplay or state‑level AI regulations that may affect U.S. labeling. Highlight any missing evidence items or risk controls that could impede a successful FDA submission.*

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

1. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

2. Chunk `198015203798949382`

> ### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---

### kb-eval-20260716-it03-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_us-002", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "a852077f86f0109a", "source": "github:holee9/MD-process/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md", "source_hash": "efcd12a4b49cb21ffa28b5f1aa35345e8bb04b98c57a32649483fa824de23fff"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `a852077f86f0109a`
- Source: `github:holee9/MD-process/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_%EB%85%B8%ED%9B%84.md)
- Source hash: `efcd12a4b49cb21ffa28b5f1aa35345e8bb04b98c57a32649483fa824de23fff`
- Focus: SaMD change impact
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: > 참고: 사내 자매문서 `03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md` v0.3는 §3에서 "FDA PCCP Guidance 2024" 및 §4 용어표 "PCCP — Predetermined Change Control Plan"로 정확히 최종본을 인용하고 있어, 본 문서만 노후 인용 상태가 단절되어 있다. ## Tier 2 (보조 — 범위 가늠용) - King & Spalding alert "FDA Publishes Final Predetermined Change Control Plan Guidance for AI-Enabled Device Software Functions" (2024-...
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

> **Regulatory Draft – AI‑Enabled SaMD Change Impact (Daily Growth Case)**  

---

### Bottom Line  
- **Likely pathway:** 510(k) *substantial equivalence* for a Class II AI‑enabled SaMD, supplemented by the FDA **Predetermined Change Control Plan (PCCP)** submission as required for any post‑market algorithmic updates.  
- **If no predicate exists** or the device’s risk profile exceeds Class II constraints → pursue **De Novo** classification before future 510(k) submissions.  

---

## 1. Classification & Submission Route  

| Attribute | Assessment |
|-----------|------------|
| Device type | Software‑as‑a‑Medical‑Device (SaMD) with AI/ML functionality. |
| FDA class | Anticipated **Class II** based on typical risk of decision support tools; confirm via predicate comparison. |
| Primary submission | **Traditional 510(k)** including: <br>• Predicate device(s) & substantial equivalence argument.<br>• FDA‑required labeling, intended use, and performance data.<br>• **PCCP** (Predetermined Change Control Plan) attached as a separate module per the final *FDA PCCP Guidance 2024*. |
| Alternative pathway | **De Novo** if no appropriate predicate or if risk justification exceeds Class II limits. |
| QMS requirement | Compliance with **QMSR (effective Feb 2026)** ‑ ISO 13485‑aligned quality system, including software lifecycle and post‑market change management. |

> **Citation:** No specific identifier found in source — verify separately.

---

## 2. Required Evidence Package  

1. **Predicate Documentation**  
   - Device description, classification, 510(k) number, and summary of technological characteristics.  
   - Side‑by‑side matrix demonstrating equivalence (hardware, software architecture, algorithmic intent).

2. **Clinical/Performance Data**  
   - Prospective or retrospective clinical validation showing non‑inferiority to predicate for the intended population.  
   - Statistical assessment of algorithm performance (sensitivity, specificity, AUC) with confidence intervals.

3. **Algorithmic Validation & Bias Assessment**  
   - Dataset provenance, representativeness, and fairness analysis per FDA’s *AI/ML Software as a Medical Device* framework.  
   - Drift monitoring plan (data shift detection thresholds).

4. **Software Lifecycle Documentation** *(IEC 62304)*  
   - Requirements traceability, architecture diagram, unit/integration test reports, verification & validation summary.

5. **Risk Management File** *(ISO 14971)*  
   - Hazard analysis specific to AI functions (e.g., misclassification risk, bias‑induced harm).  
   - Mitigation controls: input data quality checks, out‑of‑distribution alerts, human‑in‑the‑loop safeguards.

6. **PCCP Submission** *(per FDA PCCP Guidance 2024)*  
   - **Pre‑determined Change Control Plan** covering: <br>• Types of permissible changes (model updates, parameter tuning).<br>• Criteria for “major” vs. “minor” changes.<br>• Required pre‑ and post‑change verification activities.<br>• Timeline for FDA notification or supplementary documentation.

7. **Labeling & IFU**  
   - Clear intended use statement, description of AI function, user responsibilities, limitations, and recommended monitoring frequency.

8. **Cybersecurity Assessment**  
   - Threat model, vulnerability mitigation, secure update mechanism aligned with FDA’s *Postmarket Management of Cybersecurity* guidance.

---

## 3. Missing Information (Gaps to Resolve Before Filing)  

| Gap | Why It Matters | Action |
|-----|----------------|--------|
| **Explicit predicate identification** (510(k) numbers, device names) | Needed for the substantial‑equivalence argument. | Conduct market search; select one or multiple predicates that match intended use and technology. |
| **Detailed intended use & clinical indication** | Drives classification and required clinical data scope. | Draft precise IFU wording and verify with product development team. |
| **Algorithm change taxonomy** (what constitutes a “predetermined” vs. “unplanned” change) | Directly impacts PCCP acceptance. | Map all foreseeable model update scenarios; document thresholds and justification. |
| **Data set provenance & bias analysis results** | FDA expects quantitative fairness evidence for AI/ML devices. | Perform demographic breakdown, statistical parity tests, and report findings. |
| **QMSR compliance evidence (ISO 13485‑aligned processes)** | Mandatory as of Feb 2026; auditors will request records. | Provide SOPs, training logs, internal audit reports covering software development and change control. |
| **Human factors / usability validation** for AI output interpretation | Ensures safe human–machine interaction. | Conduct formative/usability studies per FDA Human Factors guidance. |

---

## 4. Core Risk Controls (Design & Post‑Market)  

1. **Algorithmic Transparency** – Provide explainable outputs or confidence scores to aid clinician decision making.  
2. **Drift Detection Engine** – Automatic alerts when input data distribution diverges beyond pre‑set limits; triggers a review per PCCP.  
3. **Human Oversight Requirement** – Explicit labeling that AI recommendations are advisory, not autonomous.  
4. **Input Data Validation** – Real‑time checks for missing/implausible values before inference.  
5. **Version Control & Audit Trail** – Immutable logs of model versions, training data snapshots, and change justification.  
6. **Cybersecurity Controls** – Encrypted data transmission, authenticated OTA updates, regular penetration testing.  

---

## 5. Human‑Escalation Triggers (When to Involve Senior RA / Regulatory Lead)  

| Trigger | Action |
|--------|--------|
| No suitable predicate identified or risk analysis pushes the device into **Class III** territory | Escalate for De Novo strategy discussion and possible PMA pathway. |
| Proposed algorithm change falls outside the pre‑determined scope (e.g., new clinical indication, architecture redesign) | Initiate supplemental 510(k) or new submission; engage senior RA. |
| Significant performance deviation detected in post‑market monitoring (> predefined margin) | Prepare FDA safety notice and corrective action plan; involve senior RA and quality leadership. |
| QMSR audit reveals non‑conformities in software change control documentation | Immediate remediation and escalation to Compliance Officer. |
| New regulatory guidance (post‑2024 PCCP updates) affecting change management | Review impact, update PCCP, and inform project team via senior RA. |

---

## 6. Citations  

- **FDA Predetermined Change Control Plan Guidance (Final 2024)** – referenced in internal SOP‑AIGOV‑001.  
- **King & Spalding alert**: “FDA Publishes Final Predetermined Change Control Plan Guidance for AI‑Enabled Device Software Functions” (published Dec 2024).  
- **Ropes & Gray / McDermott notification** confirming final guidance release date 03 Dec 2024.  

> *No specific identifier (e.g., 510(k) numbers, docket IDs) found in source – verify separately.*

---

### Peer‑Review Prompt
> **@RA‑Peer:** Please review the assumptions underlying the classification choice, the completeness of predicate sourcing, and any jurisdictional gaps (e.g., EU AI Act compatibility). Confirm that all required evidence items align with current FDA expectations for AI‑enabled SaMD and identify any overlooked submission requirements.  

--- 

*Prepared by: Mike – US Regulatory Affairs Specialist*

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

1. Chunk `126806950873507800`

> > 참고: 사내 자매문서 `03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md` v0.3는 §3에서 "FDA PCCP Guidance 2024" 및 §4 용어표 "PCCP — Predetermined Change Control Plan"로 정확히 최종본을 인용하고 있어, 본 문서만 노후 인용 상태가 단절되어 있다.

2. Chunk `18243842993399443`

> ## Tier 2 (보조 — 범위 가늠용) - King & Spalding alert "FDA Publishes Final Predetermined Change Control Plan Guidance for AI-Enabled Device Software Functions" (2024-12) - Ropes & Gray, McDermott+ 알림(최종본 발행일 2024-12-03 확인용)

### kb-eval-20260716-it03-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_us-003", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "4c8c8b7e4ef63c97", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `4c8c8b7e4ef63c97`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/FDA_AI_ML_2026_PCCP_%EC%9A%B4%EC%98%81_TPLC_%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8.md)
- Source hash: `14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76`
- Focus: SaMD change impact
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: ### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. --- ## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로...
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

> **Regulatory Draft – SaMD Change Impact (AI‑Enabled Diagnostic/Screening Software Function, PCCP)**  

| Item | Assessment |
|------|-------------|
| **Device Classification** | Likely **Class II** under 21 CFR 862.30 (Software as a Medical Device) because the function provides diagnostic or screening support and is AI‑enabled with a predetermined change control plan (PCCP). If the intended use involves clinical decision‑making without physician oversight, consider **Class III** and a De Novo route; however current guidance places most SaMD with limited risk in Class II. |
| **Submission Pathway** | **510(k) – Traditional or Special 510(k)** using the pre‑approved **PCC (Pre‑Certified Change) protocol**. The “PCCP” referenced in the source is a pre‑market change agreement that defines allowable algorithm updates, data set revisions, and bias mitigation steps. If the change falls within the approved PCC scope, a **Special 510(k)** (post‑approval supplement) suffices; otherwise a full traditional 510(k) with new predicate comparison is required. |
| **Key Required Evidence** | 1. **Algorithm Description & Data Lineage** – detailed documentation of training, tuning, and test partitions (train/validation/test).<br>2. **Performance Metrics** – sensitivity, specificity, ROC/AUC linked to the clinical claim.<br>3. **Bias Analysis & Mitigation** – quantitative assessment across demographic subgroups; documented mitigation strategies.<br>4. **Human‑AI Workflow** – description of how clinicians interact with outputs, including escalation points.<br>5. **Post‑Market Surveillance Plan** – real‑time monitoring, adverse event reporting, and update triggers per FDA’s “SaMD Post‑Market Management” guidance (2023).<br>6. **Cybersecurity Controls** – threat model, vulnerability management, and patching procedures.<br>7. **Quality System Records** – conformity to QMSR (effective Feb 2026) / ISO 13485:2016. |
| **Missing Information (Gap Analysis)** | • Exact **intended use statement** (diagnostic vs screening, target population).<br>• Identification of a **predicate device** with 510(k) number (none provided in source).<br>• Quantitative results of bias analysis and mitigation effectiveness.<br>• Detailed **human factors validation** for the AI‑Human workflow.<br>• Comprehensive **cybersecurity risk assessment** aligned with FDA’s “Content of Premarket Submissions for Management of Cybersecurity Risks”. |
| **Risk Controls (per ISO 14971 / FDA SaMD Guidance)** | 1. **Algorithmic Transparency** – version control, reproducibility logs.<br>2. **Bias Monitoring** – ongoing statistical checks after each update.<br>3. **Decision Support Limitation** – clear labeling of AI output as “advisory” with mandatory physician verification.<br>4. **Fail‑Safe Mechanisms** – default to prior approved algorithm version if post‑deployment monitoring flags performance drift.<br>5. **Cybersecurity Measures** – encrypted data transmission, authentication, regular penetration testing. |
| **Citations from Source** | - No specific identifier (510(k) number, predicate number, case ID) found in source excerpts. <br>- References: “PCCP” (Pre‑Certified Change Protocol) and “AI‑Enabled DSF Lifecycle Management & Marketing Submission Recommendations” draft (2025‑01‑06). |
| **Human‑Escalation Triggers** | • Detect statistically significant performance degradation (>10% drop in sensitivity/specificity) in post‑market data.<br>• Identify new bias patterns exceeding pre‑defined thresholds (e.g., >15% disparity across protected groups).<br>• Cybersecurity incident that could compromise algorithm integrity.<br>• FDA or CMS mandate for a Class III re‑classification or safety notice. |

---

### Peer Review Prompt
*Please review this assessment and challenge the following:*

1. **Classification Assumption** – Is Class II justified given the AI function’s impact on clinical decision making, or should we pre‑emptively consider a De Novo submission?  
2. **Scope of PCCP** – Does the current change fall comfortably within the “pre‑approved” range under the referenced PCCP, or are there hidden variables that would require a full 510(k)?  
3. **Evidence Gaps** – Are any additional data (e.g., real‑world performance, external validation) required to satisfy FDA’s “Good Machine Learning Practice” expectations?  
4. **Jurisdictional Coverage** – Have we missed any recent FDA guidance (e.g., May 2025 AI/ML SaMD Pre‑Market Framework updates) that could affect the submission route or documentation needs?

---

#### Reusable RA Judgment (to be stored for future reference)

```json
{
  "action": "honcho_conclude",
  "lesson": "When evaluating AI‑enabled SaMD changes under a PCCP, first verify whether the change is strictly within the pre‑approved scope; if so, pursue a Special 510(k) supplement. In all cases, assemble a complete bias analysis, human‑AI workflow validation, and cybersecurity risk assessment before finalizing the submission. Absence of explicit predicate identifiers in source material mandates a fresh predicate search."
}
```

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

### kb-eval-20260716-it03-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_us-004", "iteration": 3, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "1056ea3b790075ff", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `1056ea3b790075ff`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_01_Device_Description_IFU.md)
- Source hash: `70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_01_Device_Description_IFU.md`는 FDA eSTAR device description 및 IFU 작성에 필요한 제품 설명·표시 정보 문서입니다.
- 현재 excerpt 핵심: ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA For...
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

| Item | Assessment |
|------|------------|
| **Device Type / Intended Use** | Software‑only medical device (SaMD) that controls image acquisition, review and management for digital radiography systems. Intended use is limited to “acquire, review, and manage” images; **not** for primary diagnosis or interpretation. |
| **Classification & Submission Pathway** | • Because the software does **not** make a diagnostic claim, it can be class II under 21 CFR 862.23 (Radiology – Image acquisition) when paired with an X‑ray detector/generator.<br>• The likely pathway is a **Traditional 510(k)** (or Abbreviated if a suitable predicate exists). No De Novo or PMA is required unless the software adds a new intended use or risk profile beyond existing predicates. |
| **Key Predicate Candidate** | Identify an existing cleared radiography acquisition/management system that: <br>‑ Is class II, <br>‑ Has a similar “image acquisition & review” function without diagnostic claim, and <br>‑ Uses comparable DICOM interfaces. (Predicate number to be confirmed from FDA 510(k) database). |
| **Required Evidence** | 1. **Device Description** – detailed software architecture (modules, processes, DB, DICOM nodes), OS/hardware requirements, compatible detector/generator list with version numbers.<br>2. **Software Lifecycle Documentation** – IEC 62304‑compliant design dossier showing safety class (likely Class C for image acquisition control). Include SOUP inventory and justification.<br>3. **Cybersecurity Package** – description of authentication, encryption, audit logs; risk assessment per FDA “Content of Premarket Submissions for Management of Cybersecurity”.<br>4. **DICOM Conformance Statement** – storage SCU, worklist SCU, MPPS etc.; evidence of interoperability testing with listed hardware.<br>5. **Indications for Use (IFU)** – using FDA Form 3881; exact wording must avoid “diagnosis” or “interpretation”.<br>6. **Risk Management File** – ISO 14971 analysis covering hazards such as incorrect image acquisition parameters, data integrity loss, unauthorized access.<br>7. **Labeling & User Training Materials** – for “trained technologists”. |
| **Missing Information (to be supplied)** | • Full list of compatible X‑ray detectors/generators with version numbers.<br>• IEC 62304 safety class assignment and supporting software verification/validation reports.<br>• Detailed cybersecurity threat model and mitigation plan.<br>• DICOM conformance test results (including MPPS, Worklist).<br>• Complete IFU in English using FDA Form 3881 format. |
| **Risk Controls Needed** | 1. **Software Safety** – enforce correct acquisition parameters; fail‑safe defaults if hardware communication fails.<br>2. **Data Integrity** – checksums and automatic backup of image data before transfer.<br>3. **Access Control** – role‑based authentication, session timeout, audit logging of all configuration changes.<br>4. **Error Handling** – clear user alerts, prevent continuation in case of critical errors.<br>5. **Usability Validation** – confirm technologists can correctly operate the GUI without unintended diagnostic use. |
| **Citations (from source)** | • 21 CFR 807.87 – information required for 510(k) submission.<br>• 21 CFR 807.92 – format for 510(k) Summary.<br>• FDA Guidance “General/Specific Intended Use” (1998).<br>• IEC 62304 – software safety lifecycle.<br>• No specific predicate or submission numbers appear in the source excerpts; verify separately. |
| **Human‑Escalation Triggers** | 1. **Diagnostic Claim Detected** – any language in IFU, labeling, or marketing that implies primary diagnosis or image interpretation must be escalated to senior regulatory lead for re‑classification risk (possible Class III).<br>2. **Cybersecurity Gap** – missing or inadequate security controls trigger immediate escalation to the cybersecurity specialist and possibly a pre‑submission meeting with FDA.<br>3. **Unsupported Hardware Version** – if planned compatible detector/generator versions are not cleared for use with the predicate, escalate for hardware‐software compatibility assessment.<br>4. **Incomplete Risk Management** – any unresolved high‑severity hazard requires senior RA sign‑off before submission. |

---

### Peer Review Prompt
*Please review this draft and challenge:*

1. The assumption that a Traditional 510(k) is sufficient—are there any emerging FDA guidances (e.g., SaMD Pre‑market Guidance, Digital Health Update) that could push this toward an Abbreviated or de Novo pathway?
2. Does the source coverage adequately capture all required sections of 21 CFR 807.87 and related guidance, or are additional FDA documents needed (e.g., “Content of Premarket Submissions for Management of Cybersecurity”)?
3. Are there any jurisdiction‑specific gaps (state licensure, CMS conditions of coverage) that we have omitted but should flag now?

---

### Reusable RA Judgment (Lesson Record)

**Conclusion:** For SaMD that controls radiographic image acquisition and review without diagnostic claim, the default regulatory approach is a **Class II Traditional 510(k)** using an appropriate predicate. The submission must contain comprehensive software architecture, IEC 62304 lifecycle evidence, cybersecurity documentation, DICOM conformance statements, precise IFU (Form 3881), and a full ISO 14971 risk file. Missing items identified are hardware compatibility lists, detailed safety class justification, threat model, and complete labeling. Any emergence of diagnostic language or inadequate security controls triggers immediate senior RA escalation.

**Action:** Store this judgment as the baseline assessment for future SaMD changes affecting imaging acquisition functions. Verify predicate numbers and confirm with FDA database prior to filing.

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

### kb-eval-20260716-it03-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_us-005", "iteration": 3, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "b52524355e284be8", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md", "source_hash": "7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `b52524355e284be8`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_04_Cybersecurity_Section.md)
- Source hash: `7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_04_Cybersecurity_Section.md`는 MDR/MDCG 또는 FDA cybersecurity 요구사항과 대응 체크리스트 문서입니다.
- 현재 excerpt 핵심: ## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VM...
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

> **Regulatory Draft – SaMD Post‑Release Change (SBOM / Cybersecurity Update)**  

| Item | Assessment & Recommendation |
|------|------------------------------|
| **Device classification & submission route** | • Most stand‑alone SaMD that performs diagnostic or therapeutic functions remains **Class II** under 21 CFR 862.xx (device‑specific regulation). <br>• Assuming the change does **not** create a new intended use, a **Traditional 510(k)** is appropriate. <br>• If the update introduces a novel functionality that cannot be linked to an existing predicate, consider a **De Novo** submission. |
| **Primary regulatory citations (from source)** | • **Section 524B(b)(3) FD&C Act** – legal obligation for a Software Bill of Materials (SBOM). <br>• **2025 FDA Cybersecurity Guidance** (referenced in the comparison table). <br>• **IEC 81001‑5‑1**, **NIST CSF** – accepted standards for risk management. <br>• No specific 510(k) predicate numbers or PMA IDs appear in the source; verify separately. |
| **Required evidence for the 510(k) amendment** | 1. **Updated SBOM** (SPDX 2.3+ or CycloneDX 1.5+, machine‑readable JSON/XML). Include all manufacturer‑developed, third‑party, and open‑source components as illustrated in the excerpt (supplier name, component name, version, unique identifier, dependency relationships, author, timestamp). <br>2. **Threat Model** – STRIDE‑based documentation confirming coverage of newly added/updated components. <br>3. **Cybersecurity Verification & Validation (V&V) plan** – test reports covering vulnerability scanning, static/dynamic analysis, and functional security testing. <br>4. **Penetration Test Summary** – even though “권고” (recommended), FDA expects evidence of effort; include scope, methodology, findings, remediation. <br>5. **Post‑Market Cybersecurity Management Plan (CMP/VMP)** – policy for patching, CVD reporting, and continuous monitoring per 524B obligations. <br>6. **Software Lifecycle Documentation** – updated Software Development/Verification/Validation files reflecting the change impact analysis. <br>7. **Labeling & IFU updates** – if UI or functionality changes affect user instructions. |
| **Missing / to‑be‑provided information** | • **Intended Use Statement** (exact claim after the change). <br>• **Predicate Device(s)** with 510(k) numbers and a side‑by‑side comparison of functional, technological, and performance characteristics. <br>• **Risk Classification Rationale** (why the device remains Class II). <br>• **Change Impact Analysis** quantifying what is added/removed and why it does not alter the risk profile. <br>• **User Training Materials** if UI/interaction changes. |
| **Core risk controls to reference** | • **IEC 81001‑5‑1** – Health software safety lifecycle. <br>• **NIST Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover).** <br>• **STRIDE** threat categories (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege). <br>• **Vulnerability Management Process** – CVSS scoring, patch timelines, and escalation thresholds. |
| **Human‑escalation triggers** | 1. **High‑severity vulnerability (CVSS ≥ 7.0)** discovered in any component after release → immediate CVD filing and internal CAPA; notify FDA within 48 h if it could affect safety/effectiveness. <br>2. **Change that adds a new intended use or clinical claim** → re‑evaluate classification; likely require a new 510(k) or De Novo. <br>3. **Failure to demonstrate substantial equivalence** during FDA review (e.g., missing predicate comparison, performance gap) → prepare supplemental information request response within the FDA’s stipulated timeframe. <br>4. **Regulatory authority feedback** indicating insufficient SBOM detail or incomplete threat model → revise and resubmit before next milestone. |
| **Next actions for submitter** | 1. Assemble the above evidence package. <br>2. Identify and document a suitable predicate (or decide on De Novo). <br>3. Conduct a formal change‑impact risk assessment, referencing IEC 81001‑5‑1 and NIST CSF. <4>. Update labeling/IFU as needed. <5>. Submit a **510(k) amendment** (or new 510(k) if required) with the compiled documentation. |
| **Peer‑review prompt** | *@RA‑Team, please review the assumptions that the SBOM update alone does not change device classification and that a traditional 510(k) is sufficient. Verify that all relevant FDA guidance (2025 Cybersecurity Guidance, Section 524B) has been captured, and confirm no jurisdictional gaps exist for post‑market cyber‑vulnerability reporting.* |

---  

**Reusable RA Judgment (Lesson Log)**  
- For any SaMD modification where **Section 524B(b)(3)** imposes a *legal* SBOM requirement, treat the SBOM as **mandatory submission evidence** in a 510(k) amendment.  
- Align threat‑model documentation to **STRIDE** and map controls to **IEC 81001‑5‑1** + **NIST CSF**; this satisfies both FDA “required” and EU MDR “recommended” expectations.  
- When source material provides regulatory language but no numeric identifiers, record “no specific identifier found in source — verify separately” rather than fabricating K numbers.  

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

1. Chunk `129799210478830618`

> ## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VMP** | 필수 | PMS 계획에 포함 | 업데이트 정책으로 요구 | | **Pen Test** | 권고 | 권고 | 권고 | | **표준 참조** | IEC 81001-5-1, NIST CSF | IEC 81001-5-1 (조화표준 진행) | IEC 81001-5-1, MFDS 자체 가이드 | | **포스트마켓** | 법적 의무 (패치, CVD, 모니터링) | PMS + Vigilance 연계 | 이상사례 보고 + 업데이트 절차 | > MDR/MFDS 영향: GUI SW의 경우 FDA 요건 충족 수준으로 작성하면...

2. Chunk `135977185938899780`

> ### 3.4 SBOM (Software Bill of Materials) **법적 의무** (Section 524B(b)(3)). **NTIA Minimum Elements** (FDA 준용): | 필드 | 설명 | 예시 | |---|---|---| | Supplier Name | SW 공급자 | OpenJDK Foundation | | Component Name | 컴포넌트 명칭 | OpenJDK | | Version | 버전 문자열 | 17.0.9 | | Unique Identifier | CPE 또는 PURL | `pkg:maven/org.openjdk/jdk@17.0.9` | | Dependency Relationship | 의존성 관계 | DependsOn: spring-boot@3.2.0 | | Author of SBOM | SBOM 작성자 | [제조사명] | | Timestamp | 생성일시 ISO 8601 | 2026-04-29T00:00:00Z | **형식**: SPDX 2.3+ 또는 CycloneDX 1.5+ (machine-readable JSON/XML 권장) **포함 범위**: - Manufacturer-developed SW (자체 개발) - Third-party commercial/licensed SW - Ope...

## ra_eu

### kb-eval-20260716-it03-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_eu-001", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a0fc3d166809748d", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a0fc3d166809748d`
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

> **Regulatory Draft – Response to Notified Body (NB) Question**  
*Prepared for internal review – “daily_growth_v1” run, 2026‑07‑18*  

---

## 1. Device Scope & Preliminary Regulatory Position  

| Item | Current Information (from source) | Comment / Action |
|------|-----------------------------------|------------------|
| **Intended purpose / indication** | Not provided in the excerpt. | **Missing – must be supplied** before any classification can be finalised. |
| **Device family / technology** | Only a generic “medical‑device” reference appears. | **Missing – details on principle of operation, invasiveness, duration of contact, etc., are required to apply Annex VIII rules.** |
| **Target market** | EU (MDR 2017/745). | Confirmed. |

> **Rule:** Classification must be derived from the *intended purpose* and the *principal risk* according to **Annex VIII – Classification Rules** (e.g., Rule 10 for active implantable devices, Rule 22 for sterile products, etc.). The exact rule number cannot be asserted until the intended‑use statement is received.  

---

## 2. Proposed Classification & Conformity‑Assessment Route  

| Device Class* | Required NB Involvement | MDR Annex / Article |
|---------------|------------------------|---------------------|
| **Class I (non‑sterile, non‑measuring)** | None – self‑declaration of conformity (EC Declaration of Conformity). | **Annex IV** (EU Declaration) and **Annex IX** (QMS for Class Is/Im). |
| **Class Is / Im** | Full QMS audit (ISO 13485) + specific module for sterile/measuring devices. | **Annex IX** (QMS‑based assessment). |
| **Class IIa** | Module A (EC Declaration) + NB review of technical documentation (TD). | **Annex X** (type‑examination) *or* **Annex XI** (product verification) together with the QMS audit. |
| **Class IIb / III** | Full audit: QMS (ISO 13485) + design dossier review (type‑examination, product verification). | **Annex X** + **Annex XI**; for Class III a **full CE‑marking** – NB issues CE certificate after verifying Annex II TD. |

\*The exact class cannot be fixed until the intended purpose is clarified (see Section 1).

---

## 3. Technical Documentation – Evidence Required by **Annex II**  

| Annex II Chapter | Evidence to be supplied (per source) | Current Gap |
|-------------------|--------------------------------------|------------|
| **§1 Device Description** | Detailed device description, variants, accessories, intended purpose, principle of operation, and classification justification. | *Missing – only a generic “제품 설명” label appears.* |
| **§2 Labeling & IFU** | Labels, packaging artwork, Instructions for Use (IFU) in English + any required local language(s). Must demonstrate compliance with **Annex I – GSPR** labeling requirements. | *Labeling samples not provided.* |
| **§3 Design & Manufacturing** | Design History File (DHF) extracts: design outputs, specifications, Bill of Materials, manufacturing processes, suppliers, process validation. | *Only a reference to “Design Output” in the comparative table; actual documents absent.* |
| **§4 GSPR Checklist** | Completed checklist mapping device characteristics to each Essential Safety & Performance Requirement (Annex I). | *No completed checklist supplied.* |
| **§5 Risk Management** | Full **Risk Management File** per **ISO 14971**, including risk analysis, evaluation of residual risk, benefit‑risk determination. | *Only a note that “Risk Management File” exists – no file attached.* |
| **§6 Verification & Validation** | V&V reports (bench testing, software verification if applicable, pre‑clinical / animal studies, biocompatibility, performance testing). | *No V&V reports provided.* |
| **§7 Clinical Evaluation** | **Clinical Evaluation Report (CER)** – see **Annex XIV Part A**. Must include State‑of‑the‑Art literature review, clinical data (clinical investigations, PMS, literature) and benefit‑risk analysis. | *Absent – must be compiled.* |
| **§8 Post‑Market Surveillance** | PMS Plan per **Art. 84**, PMS System per **Art. 83**, and for Class IIb/III a Periodic Safety Update Report (PSUR) per **Art. 86**. Also, a PMCF plan/evaluation (**Annex XIV Part B**) if required. | *PMS documentation not supplied.* |
| **§9 Declaration of Conformity** | Signed EU Declaration (Annex IV). | *Not yet drafted.* |

> **Key citation:** The clinical evaluation requirement is anchored in **Annex XIV Part A** – the source explicitly lists “Annex XIV (Clinical Evaluation)” under “관련 Annex”.  

---

## 4. Clinical Evidence – Minimum Requirements  

| Requirement | Source & Article | What must be provided |
|-------------|------------------|-----------------------|
| **CER** | **Annex XIV Part A** (updates via Art. 61) | • State‑of‑the‑Art literature review <br>• Clinical data from investigations, PMS, registries, or equivalence justification <br>• Benefit–risk assessment |
| **PMCF Plan / Report** | **Annex XIV Part B** (not a clinical investigation article) | Required for Class IIa and higher unless existing PMS provides sufficient evidence. Must describe post‑market data collection strategy, endpoints, timelines, and evaluation methodology. |
| **Clinical Investigation (if needed)** | Articles 78–80 – *only* when no satisfactory clinical data exist; not applicable to PMCF alone. | Protocol, ethics approvals, results summary, etc., submitted as a separate dossier if undertaken. |
| **Biocompatibility & Bench Testing** | Must meet GSPR‑related performance testing (Annex I §4) and harmonised standards (e.g., EN ISO 10993). | Test reports, justification of standard selection. |

> **Missing evidence:** No CER or PMCF documentation is currently available in the source material; these are essential for NB review.

---

## 5. Risk Controls – Expected Content  

1. **Risk Management Process** – per **ISO 14971**, documented and linked to design outputs (Section §3).  
2. **Hazard Identification** – list of all hazards related to device use, including electrical, mechanical, thermal, software, etc.  
3. **Risk Evaluation & Control Measures** – hierarchy of controls applied (inherent safety, protective measures, information for users).  
4. **Residual Risk Acceptance** – documented benefit–risk analysis showing that residual risks are outweighed by the intended medical benefits.  
5. **Verification of Controls** – test data proving that each control measure is effective (see V&V reports, §6).  

All risk documentation must be cross‑referenced in the **Risk Management File** and cited as part of **Annex II §5**.

---

## 6. Citations & Regulatory Mapping (per “Citation rule” table)  

| Requirement | Correct Reference (per table) |
|-------------|--------------------------------|
| Clinical Evaluation Report (CER) | **Annex XIV Part A** |
| PMCF plan / evaluation report | **Annex XIV Part B** |
| PMS system / plan / report / PSUR | **Art. 83** (system), **Art. 84** (plan), **Art. 85/86** (report) |
| EU Declaration of Conformity | **Annex IV** |
| Classification rules | **Annex VIII** (Rule 1‑22) |
| Conformity‑assessment routes | **Annex IX** (QMS‑based) / **Annex X + XI** (type‑exam & product verification) |
| Products without intended medical purpose | **Annex  XVI** (not applicable here) |
| EUDAMED registration obligations | **Art. 33‑39** |

*No specific identifier (e.g., 510(k) number, case ID) appears in the provided excerpts – “no specific identifier found in source — verify separately”.*

---

## 7. Identified Gaps & Required Actions  

| Gap | Impact on NB Review | Immediate Action |
|-----|----------------------|-------------------|
| **Intended‑purpose statement** (required for classification) | Prevents determination of class & route; NB cannot assess conformity. | Request from client: clear, concise intended use, target patient population, mode of action, duration of contact. |
| **Complete Device Description & Variant Matrix** | Required for Annex II §1 and risk analysis linkage. | Compile from design team; include drawings, BOM, software architecture (if applicable). |
| **Labeling/IFU in English** | Needed for GSPR compliance verification. | Submit sample label + IFU (electronic PDF). |
| **Risk Management File** (full ISO 14971 documentation) | Core evidence for safety claims; NB will request cross‑reference to design outputs. | Provide risk analysis, risk control measures, residual risk evaluation. |
| **Verification & Validation Reports** | Demonstrate that device meets specifications and GSPR. | Gather bench test data, software validation, sterility assurance, biocompatibility reports. |
| **Clinical Evaluation Report (CER)** | Mandatory for all classes IIa‑III; optional but highly recommended for Class I with higher risk aspects. | Conduct literature review, prepare clinical data dossier, complete benefit‑risk analysis. |
| **Post‑Market Surveillance (PMS) Plan & System** | Required per Art. 84/83; PSUR for Class IIb/III. | Draft PMS plan outlining data sources, reporting timelines, and trigger mechanisms. |
| **Declaration of Conformity (DoC)** | Final step before CE marking. | Prepare once all above evidence is compiled and signed by the authorised representative. |

---

## 8. Human‑Escalation Triggers  

- **Classification Uncertainty** (no intended purpose → cannot select Annex VIII rule).  
- **Missing Clinical Evidence** (CER/PMCF absent for Classes IIa‑III).  
- **Incomplete Risk Management File** – especially if residual risk justification is not documented.  
- **NB Query on GSPR Checklist** – lack of a completed checklist will stall the assessment.  

*Whenever any of the above items are flagged, the RA lead must be notified immediately for coordination with the client’s development team.*

---

## 9. Recommendation Summary (to be communicated to NB)  

1. **Provide Intended‑Purpose Statement** – enables us to assign the correct classification rule (Annex VIII).  
2. **Deliver Full Annex II Technical Documentation Pack** as enumerated in Section 3, referenced against each chapter.  
3. **Compile Clinical Evaluation Report** per **Annex XIV Part A** and, where required, a PMCF plan (**Annex XIV Part B**).  
4. **Finalize Risk Management File** (ISO 14971) and cross‑reference to design outputs.  
5. **Submit PMS Plan/System** in line with **Art. 84/83**, and PSUR for Class IIb/III per **Art. 86**.  

Once the above are received, we will be able to confirm the conformity‑assessment route (Annex IX or X/XI) and prepare the EU Declaration of Conformity (Annex IV).

---

## 10. Peer Review Prompt  

> **To a fellow RA colleague:**  
> Please examine this draft and challenge:  
> - The assumption that classification can be deferred until an intended‑use statement is supplied – are there any default “fallback” classifications permissible under MDR?  
> - Whether the listed evidence (especially for Class I sterile/measuring devices) fully satisfies **Annex II** and **Annex IX** requirements, or if additional items (e.g., Notified Body audit programme outlines) should be added.  
> - If any jurisdiction‑specific gaps exist (e.g., Korean MFDS references in the source table that might affect EEA documentation format).  

Your feedback will be recorded as a **human‑escalation comment** and incorporated before final submission to the NB.

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

### kb-eval-20260716-it03-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_eu-002", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2f66967eda81b3ef", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2f66967eda81b3ef`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/NB_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/NB_Deficiency_Letter_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `NB_Deficiency_Letter_대응전략.md`는 Notified Body deficiency letter 대응과 evidence traceability를 다루는 문서입니다.
- 현재 excerpt 핵심: 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` --- | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter |...
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

> **Regulatory Draft – Response to Notified Body (NB) Deficiency Letter**  
*Prepared for internal review – EU MDR 2017/745*  

---

### 1. Device Overview (as understood from the source)

| Item | Information |
|------|--------------|
| **Intended Purpose** | Diagnostic radiology device used for standard radiographic imaging. |
| **Key Performance Claim** | Detective Quantum Efficiency (DQE) ≥ 65 % (IEC 62220‑1‑1). |
| **Reference Test Report** | TR‑2024‑015 (IEC 62220‑1‑1). |
| **Current Clinical Evidence** | Revised Clinical Evaluation Report (CER) Rev. 3 attached as Annex A. |

*No specific device name, model number, or regulatory identifier appears in the source excerpts – verify separately.*

---

### 2. Preliminary Regulatory Determination  

| Aspect | Determination | Rationale / Reference |
|--------|---------------|-----------------------|
| **Classification** | *To be confirmed* – likely **Class IIa** (active device for diagnostic radiology) but must be verified against MDR **Annex VIII** classification rules (e.g., Rule 9). | Classification must follow the rule‑by‑rule analysis in Annex VIII; the source only states “standard diagnostic radiology”. |
| **Conformity‑assessment route** | Assuming Class IIa or higher: **Full quality‑management‑system assessment (Annex IX)** together with review of Technical Documentation (TD) and Clinical Evaluation (Annex X + XI may be required for type examination). | MDR Annex IX governs QMS‑based routes; Annex X/​XI apply where a type‑examination is used. |
| **Applicable legal basis of the NB comment** | **MDR Annex VII** + **Commission Delegated Regulation (CDR) 2026/977** – Structured Dialogue (Art. 7). | Directly quoted in source table. |

---

### 3. Required Evidence (per MDR)

1. **Clinical Evaluation Report (CER)** – *Annex XIV Part A*  
   - Updated literature review covering the state of the art (SOTA).  
   • Clinical data confirming equivalence to the predicate device, including DQE ≥ 65 % with full methodological description and raw data traceability.  
   • Post‑market clinical follow‑up (PMCF) plan & interim report – *Annex XIV Part B* (if required for class).  

2. **Technical Documentation (TD)** – *Annex II/III*  
   - Device description, specifications, labeling (including IFU), and intended use statement.  
   - Risk Management File (ISO 14971) with updated risk analysis, risk control measures, residual‑risk evaluation, and justification of accepted risks.  

3. **Quality Management System (QMS)** – *Annex IX*  
   - Evidence of conformity to EN ISO 13485:2016; any non‑conformities (NCs) previously identified must be closed with corrective actions documented.  

4. **Labeling & IFU** – Must comply with MDR **Annex VI**, including UDI, safety information, and performance claims that are fully supported by clinical data.  

5. **Post‑Market Surveillance (PMS) System** – *Art. 83* (system), *Art. 84* (plan), *Art. 85/86* (report/PSUR depending on class). While not directly asked, the NB often checks that PMS is in place and linked to PMCF.

---

### 4. Identified Gaps / Missing Information (per Deficiency Letter)

| Gap | Expected Content | Reason for Requirement |
|-----|------------------|------------------------|
| **CER details** | Full justification of clinical equivalence (methodology, statistical analysis, comparator selection). Current CER Rev 3 is attached but appears to lack complete raw data and literature synthesis. | MDR Annex XIV Part A – the CER must provide sufficient evidence that the device meets safety & performance requirements. |
| **Technical Documentation (TD)** | Complete design dossier, manufacturing process description, verification & validation reports, plus traceability matrix linking requirements to specifications. | Mandatory for NB review under Annex II/III. |
| **QMS Non‑Conformities (NC) closure** | Evidence of corrective actions taken for each NC highlighted by the NB (e.g., audit findings, CAPA records). | NB may have identified QMS gaps; compliance with MDR Annex IX requires resolved NCs. |
| **Labeling/IFU** | Updated labeling that reflects the validated DQE claim and includes any contraindications or warnings derived from risk analysis. | MDR Annex VI demands accurate, evidence‑based labeling. |
| **PMCF Plan & Interim Report** (if applicable) | Defined objectives, methodology, data collection schedule, and interim results showing ongoing safety performance. | Required for Class IIa/b and higher per Annex XIV Part B. |
| **Risk Management Updates** | Revised risk assessment reflecting any new hazards identified during equivalence testing or post‑market experience. | ISO 14971/ MDR Annex II (risk management). |

---

### 5. Recommended Action Plan  

| Step | Action | Owner | Deadline (to be aligned with NB agreed “clock‑stop”) |
|------|--------|-------|-----------------------------------------------------|
| **1** | Perform a full gap analysis against the list above; document missing items in a tracker. | RA Lead / PM | Within 2 working days of receipt. |
| **2** | Update CER: include complete DQE raw data, statistical justification, SOTA literature (minimum 3 peer‑reviewed sources), and PMCF plan if needed. | Clinical Evaluation Team | 10 calendar days. |
| **3** | Complete TD updates – add design outputs, verification/validation reports, labeling drafts, risk management file revision. | Design & Regulatory Engineering | 12 calendar days. |
| **4** | Close QMS NCs: attach CAPA records, audit reports, and evidence of implementation. | Quality Manager | 8 calendar days. |
| **5** | Prepare a consolidated response package (Annex A‑E) per NB’s structured dialogue format; include cover letter referencing MDR Annex VII & CDR 2026/977. | RA Lead | 14 calendar days. |
| **6** | If any deadline cannot be met, request an extension via Structured Dialogue (Art. 7, CDR 2026/977) before the “clock‑stop” expires. | RA Lead / Senior Manager | Immediately upon identification of delay. |

---

### 6. Risk Controls & Mitigations (to be documented in TD & Risk File)

1. **Performance‑related hazard** – Inadequate image quality (DQE < 65 %).  
   - *Control*: Validation of DQE per IEC 62220‑1‑1; periodic re‑testing as part of PMCF.  

2. **Radiation exposure risk** – Potential for increased dose if imaging parameters are altered to compensate for poor detector performance.  
   - *Control*: Built‑in software limits on exposure settings; user training; labeling warnings.  

3. **Electrical safety** – Compliance with IEC 60601‑1 (basic safety).  
   - *Control*: Full type‑test and ongoing surveillance.  

4. **Usability/human factors** – Misinterpretation of image quality metrics by operators.  
   - *Control*: Clear IFU instructions, training modules, and usability testing results in TD.

All controls must be linked to residual risk evaluation and demonstrated in the **Risk Management Report (Annex II/III)**.

---

### 7. Human‑Escalation Triggers  

| Condition | Escalation Path |
|-----------|-----------------|
| **Inability to meet NB deadline** (e.g., due to missing raw data) | Immediate notification of Senior RA Manager → Formal extension request via Structured Dialogue (Art. 7, CDR 2026/977). |
| **Major QMS NC remains open** after corrective action plan | Escalate to Quality Assurance Director and consider interim suspension of submission until closure. |
| **Critical safety data (e.g., unexpected adverse events) uncovered during PMCF** | Trigger Safety Review Board; issue Field Safety Corrective Action (FSCA) if required; inform NB under Article 83‑86 PMS obligations. |
| **Disagreement on interpretation of MDR requirements with NB** | Request a “Structured Dialogue” meeting (Art. 7, CDR 2026/977); document all positions for future audit trail. |

---

### 8. Citations (per Fixed Table)

- **Clinical Evaluation Report requirement** – *MDR Annex XIV Part A* (not Annex IV).  
- **PMCF plan / evaluation report** – *MDR Annex XIV Part B*.  
- **PMS system, plan & reports** – Art. 83 (system), Art. 84 (plan), Art. 85/86 (report/PSUR).  
- **Declaration of Conformity** – *Annex IV* (not used directly here).  
- **Classification rules** – *MDR Annex VIII*.  
- **Conformity‑assessment routes** – *MDR Annex IX* (QMS) / *Annex X + XI* (type‑examination).  
- **Deficiency Letter legal basis** – *MDR Annex VII* + **CDR 2026/977** (Structured Dialogue, Art. 7).  

---

### 9. Peer Review Prompt  

> **To the next RA reviewer:**  
> - Do you agree with the assumed Class IIa classification based on “standard diagnostic radiology”, or is another rule in Annex VIII more appropriate?  
> - Are there any additional evidence items (e.g., equivalence comparison matrix, device‑specific IEC standards) that the NB may request beyond what is listed?  
> - Have we fully covered jurisdictional gaps—specifically, any overlap with national competent authority requirements (e.g., Korean MFDS or US FDA) that could affect our EU submission strategy?  
> - Is the proposed timeline realistic given typical data‑generation cycles for DQE testing and CER updates?  

Please challenge the assumptions, check source coverage, and flag any missing MDR provisions.

---

### 10. Reusable RA Judgment (Lesson Learned)

**Judgment ID:** *RA‑MDR‑2026‑07‑18‑01*  
- **Context:** NB deficiency letters under MDR often cite multiple “major” gaps (CER, TD, QMS NC, labeling).  
- **Key Takeaway:** Always map each gap explicitly to the MDR annex/article that mandates the evidence before drafting a response; reference the exact legal basis (Annex VII + CDR 2026/977) and use the correct citation tables.  
- **Actionable Rule:** When a deficiency cites “clinical equivalence”, verify that the CER includes: (i) full raw performance data, (ii) statistical justification of DQE claim, (iii) up‑to‑date SOTA literature, and (iv) an attached PMCF plan if required by class.  
- **Escalation Trigger:** Any inability to provide these elements within the NB’s “clock‑stop” must trigger a Structured Dialogue request (Art 7, CDR 2026/977) *before* the stop expires.  

--- 

*Prepared by:* Theo – EU MDR Regulatory Affairs Specialist  
*Date:* 2026‑07‑18  

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

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1014893419282866507`

> | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter | 보완 요청 | Additional Information (AI) Request | | 근거 법령 | MDR Annex VII + 2026/977 | 의료기기법 §12 + 허가·신고·심사 규정 | 21 CFR 807 + FDA Review Policy | | 답변 기한 | NB와 합의 (법정 상한 없음) | 1차 60일, 2차 60일 | 180일 (타임라인 기산일부터) | | 최대 중단 횟수 | 4회 (product verification 기준) | 2차까지 (실질 2회) | 제한 없음 (Interactive Review 가능) | | Clock-stop | 예 (NB 요청 당일 stop, 제출 익일 resume) | 예 (보완 기간 제외) | 예 (AI 발송일부터 stop) | | 미응답 시 | 평가 종료 / 불승인 | 취하 간주 | 허가 거부 | | 사전 대화 창구 | Structured Dialogue (Art.7, 2026/977) | 상담제도 (비공식) | Pre-Sub (Q-Sub) (공식, 문서화) | | 주요 결함 유형 | CER, TD, QMS NC, Labelin...

### kb-eval-20260716-it03-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_eu-003", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3c793b286540204c", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `3c793b286540204c`
- Source: `github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X%EC%84%A0_%EB%B6%84%EB%A5%98_%EC%82%AC%EC%8B%A4%EC%98%A4%EB%A5%98.md)
- Source hash: `8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### Rule 9 (Chapter III §6.1) — 오적용 반증 > "All active **therapeutic** devices intended to administer or exchange energy are classified as class IIa ... **All active devices intended to emit ionizing radiation for therapeutic purposes** ... are classified as class IIb." (진단용 X-ray에는 부적용) ### D1 — §6 표 0-2 예시 열 - **기재값 (예시 열):** > "X-ray: MFDS 3등급, FDA Class...
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

> **Regulatory Draft – Response to Notified‑Body Query (X‑ray Diagnostic System)**  
*Prepared for internal review – EU MDR 2017/745*  

---

### 1. Device Synopsis (as derived from source)

| Item | Description (source) |
|------|-----------------------|
| **Device type** | Active X‑ray system used for diagnostic imaging (ionising radiation). |
| **Regulatory references in source** | “X‑ray 시스템(진단용 이온화방사선 능동기기) = **Rule 10 → Class IIb**” (Excerpt [2]). |
| **Other jurisdictional mapping quoted** | MFDS 3‑grade, FDA Class II (510(k), Product Code MQB) – *no specific identifier provided* (Excerpt [2]). |

> **Note:** The source explicitly states that diagnostic X‑ray systems must be classified under MDR Rule 10 → Class IIb.  

---

### 2. Classification & Justification  

| Requirement | Answer |
|-------------|--------|
| **Applicable MDR rule** | **Rule 10 (Annex VIII)** – “Active devices intended to emit ionising radiation for diagnostic purposes” are classified as **Class IIb**. |
| **Classification outcome** | **Class IIb** device (MDR 2017/745). |
| **Citation** | MDR Annex VIII, Rule 10 (classification); see source excerpt [2] for mapping confirmation. |

*Why Rule 9 does NOT apply*: Rule 9 covers *therapeutic* ionising‑radiation devices; the present system is explicitly diagnostic, therefore Rule 10 is the correct pathway (source [1]).  

---

### 3. Conformity‑Assessment Route  

| Step | MDR Requirement | Typical NB involvement |
|------|-----------------|------------------------|
| **Quality‑Management System** | **Annex IX** – full QMS assessment for Class IIb devices. |
| **Type Examination (optional)** | **Annex X + XI** may be used if the manufacturer opts for a type‑exam route, but this is less common for Class IIb. |
| **NB audit & certification** | NB reviews technical documentation (Annex II) and issues CE mark after successful assessment. |
| **Post‑market surveillance** | Articles 83–86 (PMS system, PMS plan, PSUR). |

*Recommended route*: **Annex IX** (QMS‑based conformity assessment) – the most straightforward and widely accepted for Class IIb diagnostic devices.  

---

### 4. Technical Documentation – Minimum Content (per Annex II)

1. **Device description & intended purpose** (must state *diagnostic* use only).  
2. **Classification justification** (Rule 10, Annex VIII).  
3. **Design & manufacturing information** (including hardware, software versioning, IEC 60601‑2‑33 compliance).  
4. **Labeling & UDI configuration**.  
5. **Risk Management File** – ISO 14971 plus radiation‑specific controls (see §5).  
6. **Clinical Evaluation Report** – Annex XIV Part A (see §5).  
7. **Post‑Market Surveillance Plan** – Art 84.  
8. **Declarations of conformity & certificates** – Annex IV declaration.  

---

### 5. Clinical Evidence Requirements  

| Item | MDR Reference | What must be provided |
|------|---------------|-----------------------|
| **Clinical Evaluation Report (CER)** | **Annex XIV Part A** | State‑of‑the‑art literature, clinical performance data for diagnostic X‑ray systems, justification of safety & performance. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | **Annex XIV Part B** | Ongoing collection of dose‑distribution data, image quality metrics, adverse event monitoring; schedule aligned with PSUR cycle. |
| **Clinical Investigation (if required)** | Articles 78–80 *only* when existing clinical data are insufficient – *not indicated at this stage*. |

---

### 6. Post‑Market Surveillance Requirements  

| Component | MDR Article | Frequency / Deliverable |
|-----------|-------------|--------------------------|
| **PMS system** | Art 83 | Ongoing, integrated with QMS. |
| **PMS plan** | Art 84 | Established before CE marking; includes dose monitoring and incident reporting. |
| **Periodic Safety Update Report (PSUR)** | Art 86 *(mandatory for Class IIb)* | Every 12 months – summary of PMS data, trend analysis, risk‑benefit reassessment. |

---

### 7. Identified Gaps / Missing Information  

| Gap | Impact on NB assessment |
|-----|--------------------------|
| **Exact intended‑use statement** (must exclude therapeutic application). | Classification justification incomplete → NB may challenge Rule 10 usage. |
| **Radiation safety specifications** (kV range, dose‑rate limits, shielding data). | Needed for risk‑management file & compliance with IEC 60601‑2‑33. |
| **Software Description** (if any image‑processing algorithms are present). | Required for Part A of the CER and software validation evidence. |
| **Clinical performance data** (image quality studies, dose–reduction trials). | Without this, CER will be considered incomplete. |
| **PMCF planning details** (patient‑size cohorts, follow‑up duration). | PSUR preparation impossible without defined PMCF plan. |
| **Labeling & IFU drafts** showing radiation warnings and ALARA instructions. | Required for Annex II documentation and user safety assessment. |

---

### 8. Risk Controls Specific to Ionising Radiation  

1. **Engineering controls** – built‑in interlocks, automatic exposure termination, shielding, dose‑rate monitoring circuitry (IEC 60601‑2‑33).  
2. **Procedural controls** – standard operating procedures for patient positioning, exposure parameters, and verification of correct mode selection.  
3. **Training & competence** – mandatory operator certification and periodic refresher courses.  
4. **Labeling & warnings** – clear ALARA statements, maximum permissible dose limits, emergency stop instructions.  
5. **Post‑market monitoring** – automated collection of exposure data per patient to detect over‑exposures; trend analysis incorporated into PSUR.  

All controls must be documented in the **Risk Management File** (ISO 14971) and linked to residual risk evaluation in the **CER**.

---

### 9. Evidence Still Required from Manufacturer  

| Evidence | Reason |
|----------|--------|
| Full **Intended‑Use & Indications** narrative (diagnostic only). | Classification justification & labeling. |
| Detailed **Technical Specifications** of X‑ray output, beam geometry, filtration. | Risk analysis and conformity to IEC 60601‑2‑33. |
| **Clinical performance data** (e.g., comparative image‑quality studies). | CER completeness. |
| **Software Validation Report**, if imaging software is supplied. | Annex XIV Part A clinical evaluation & risk management. |
| Draft **PMS Plan** and **PMCF protocol** with defined endpoints. | Art 84/86 compliance. |
| **Labeling / IFU** samples showing radiation warnings. | Annex II documentation and user safety. |

---

### 10. Human‑Escalation Triggers  

| Situation | Action (who) |
|-----------|--------------|
| NB questions the *diagnostic* vs *therapeutic* classification (Rule 9 vs Rule 10). | Escalate to **Regulatory Lead** for formal justification and possible re‑classification request. |
| Missing clinical performance data prevents CER finalisation. | Notify **Clinical Affairs Manager** – initiate rapid evidence collection or supplemental clinical investigation. |
| Incomplete PMS plan jeopardises PSUR timeline (Art 86). | Raise to **Post‑Market Surveillance Coordinator** → update plan & schedule additional monitoring activities. |
| Discrepancy between MFDS/FDA mapping and EU classification in external documents. | Inform **Regulatory Documentation Owner** to correct all cross‑reference tables and avoid downstream errors. |
| Any adverse event relating to radiation dose is reported before PMS system is live. | Immediate notification to **Safety Officer** and trigger of “Serious Incident” procedure (Art 87). |

---

### 11. Peer‑Review Prompt  

> **To the RA peer reviewing this draft:**  
> - Do you agree with the exclusive use of MDR **Rule 10** for a diagnostic X‑ray system, given the source excerpt?  
> - Are we missing any mandatory evidence (e.g., specific IEC standards or harmonised standards) that should be referenced in Annex II?  
> - Is the proposed conformity‑assessment route (Annex IX) optimal, or should we consider an **Annex X+XI** type‑examination path for this product family?  
> - Have we adequately addressed all post‑market surveillance obligations for a Class IIb device, especially PSUR timing and content?  

Please provide challenges or additional considerations, particularly any jurisdictional nuances (e.g., differences between EU and Korean MFDS classifications) that could affect our CE‑marking plan.

---

### 12. Reusable RA Judgment (recorded for future cases)

```
honcho_conclude:
  lesson: |
    When evaluating diagnostic X‑ray systems under MDR, ALWAYS verify classification against **Rule 10 (Annex VIII)** – not Rule 5/9 or therapeutic Rule 9. Mis‑mapping leads to an incorrect conformity‑assessment route (Annex IX vs Annex X/XI) and downstream documentation errors (GSPR mapping, PSUR frequency). Ensure the intended‑use statement explicitly excludes therapeutic applications, include full radiation‑safety specifications, and prepare a complete CER (Annex XIV Part A) plus PMCF plan (Part B) before NB submission.
  source_verified: true
  flags:
    - missing_intended_use_statement
    - lacking_clinical_performance_data
    - incomplete_PMS_plan
```

--- 

*Prepared by:* Theo – EU MDR Regulatory Affairs Specialist  
*Date:* 2026‑07‑18 (run ID daily_growth_v1)

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

### kb-eval-20260716-it03-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_eu-004", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e43c897461f950f2", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md", "source_hash": "96ff2d334aa377f194a63cd731ca742bb703e9899411086b8065e85bdf4bd94a"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `e43c897461f950f2`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md)
- Source hash: `96ff2d334aa377f194a63cd731ca742bb703e9899411086b8065e85bdf4bd94a`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexI_GSPR_Checklist.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | 조화표준 | X-ray Detector | Handheld Source | GUI SW | 연계 GSPR §§ | |---|---|---|---|---| | IEC 60601-1:2005+A1+A2 (Ed 3.2) | ● | ● | N/A | §1, §19, §20, §21 | | IEC 60601-1-2:2014+A1:2020 (EMC) | ● | ● | ● (SW HW포함 시) | §19.2 | | IEC 60601-1-3:2008+A1+A2 (방사선 방호) | ● | ● | N/A | §17 | | IEC 60601-1-6:2010+A1+A2 (사용성) | ● | ● | ● | §5, §23 | | IEC 60601-2-2...
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

> **Regulatory Draft – X‑ray Detector (hand‑held) with Integrated GUI Software**  
*Prepared for internal NB‐question response (daily_growth_v1 – 2026‑07‑18)*  

---

## 1. Device Overview (as derived from source)

| Attribute | Content (source excerpts) |
|-----------|----------------------------|
| **Device type** | X‑ray detector (hand‑held) with built‑in GUI software |
| **Primary function** | Convert ionising radiation into a digital image for diagnostic use |
| **Relevant GSPR clauses** | §§ 1, 5, 16‑21 of Annex I (see source [1]) – electrical safety, EMC, radiation protection, usability, performance, etc. |
| **Key standards already referenced** | IEC 60601‑1 series, IEC 60601‑2‑28/‑2‑54, IEC 62220‑1‑1, IEC 62304, IEC 62366‑1, ISO 10993 series (source [1] & [2]) |

---

## 2. Classification & Conformity‑Assessment Route  

| Step | Rationale |
|------|-----------|
| **MDR Annex VIII – Rule 9** (Active devices containing a source of ionising radiation) *or* **Rule 10** (Devices which emit or generate ionising radiation for diagnostic purposes) | The detector itself does **not** emit radiation, but it is **intended to be used in conjunction with a handheld X‑ray source**. Under MDR the combination is considered an “active medical device” that receives radiation; historically such devices are placed in **Class IIb** (see MDR Rule 9/10). |
| **Provisional classification** | **Class IIb** – requires full quality‑management system audit and type‑examination of the product. |
| **Conformity‑assessment route** | **Annex IX (QMS assessment) + Annex X (type‑examination) + Annex XI (certification)**. The NB will review: <br>• ISO 13485 QMS (full scope) <br>• Type‑exam report covering design, safety and performance <br>• Ongoing post‑market surveillance (Art 83‑86). |

> **⚠️ Uncertainty flag** – The exact rule (9 vs. 10) should be confirmed with the NB or by cross‑checking the device’s intended use wording. *If the detector is considered a “passive” component, classification could drop to Class IIa; if it incorporates radiation‑generation capability, Class III may apply.*  

---

## 3. Mandatory Technical Documentation – Evidence Required

| GSPR / Annex I clause | Evidence needed (per source) | Current status & gaps |
|------------------------|------------------------------|-----------------------|
| **§1 – General safety** | Compliance with IEC 60601‑1:2005+A1+A2 (Ed 3.2). | Standard cited; need test report showing compliance to §§ 1, 19‑21. |
| **§5 – Usability** | IEC 62366‑1:2015+AMD1:2020 usability engineering file. | Cited; require usability validation results (task analysis, formative/ summative testing). |
| **§16‑21 – Performance & Protection** | • IEC 60601‑2‑28, ‑2‑54 for X‑ray equipment protection <br>• IEC 62220‑1‑1 DQE performance test <br>• IEC 60601‑1‑3 radiation protection §17, §17.2 | Performance test reports missing; need measured DQE values, dose‑rate limits verification. |
| **§19 – EMC** | IEC 60601‑1‑2:2014+A1:2020 compliance (including software). | Need EMC test report covering all relevant emissions & immunity levels (§19.2). |
| **§17 – Radiation safety** | IEC 60601‑1‑3 evidence of shielding, interlocks, dose alarms. | Documentation not yet provided. |
| **§10 – Chemical/Physical/Biological properties** (source [2]) | • Toxicity‑free material verification (ISO 10993‑1) <br>• Biocompatibility for any patient‑contacting parts (ISO 10993 series) <br>• Contaminant limits testing <br>• Enclosure ingress protection verification (specification) <br>• Nanomaterial risk assessment (if applicable) | **Missing:** Full ISO 10993 test reports; contaminant limit data; nanomaterial risk‑assessment file (highlighted as “verification required”). |
| **Software lifecycle** | IEC 62304:2006+A1:2015 evidence of software development & maintenance (including updates). | Need Software Development Plan, verification & validation records, change control log (§18). |
| **Clinical Evaluation** | Annex XIV Part A – Clinical Evaluation Report (CER) demonstrating state‑of‑the‑art performance vs. predicate devices. | No CER drafted yet; must be prepared before NB audit. |
| **Post‑Market Surveillance (PMS)** | Art. 83–86 – PMS system, plan and periodic safety update report (PSUR) for Class IIb. | PMS system design required; interim PMCF plan (Annex XIV Part B). |
| **Declaration of Conformity** | Annex IV – EU Declaration of Conformity with referenced standards & NB certificate number. | To be issued after successful audit. |

---

## 4. Identified Missing Information / Gaps

1. **Nanomaterial assessment** – Source [2] flags “verification required”. Need to confirm whether any nanomaterials are present in the detector housing or shielding; if so, perform a dedicated risk assessment and provide supporting data (e.g., TEM analysis, toxicology).  
2. **Full performance test package** – DQE (§16), dose‑rate limits (§17), EN 60601‑1‑3 radiation safety tests are not supplied.  
3. **Usability engineering evidence** – Task analysis, user trials and summary report required for IEC 62366‑1 compliance.  
4. **EMC test report** – Must cover software components (hardware+software) as indicated by IEC 60601‑1‑2 (§19.2).  
5. **Biological evaluation dossier** – ISO 10993 testing results (cytotoxicity, sensitisation, irritation) for any patient‑contacting surfaces.  
6. **Risk Management File (ISO 14971)** – Must incorporate hazard analysis for ionising radiation exposure, software failure modes, nanomaterial hazards, and residual risk evaluation.  
7. **Clinical Evaluation Report** – Evidence of clinical performance, comparability to existing handheld X‑ray systems, literature review per Annex XIV Part A.  
8. **PMCF Plan (Annex XIV Part B)** – Define post‑market data collection strategy for long‑term image quality and safety endpoints.  

---

## 5. Key Risk Controls (to be reflected in the Risk Management File)

| Hazard | Control (standard / design) | Residual risk rating |
|--------|-----------------------------|----------------------|
| **Electrical shock** | IEC 60601‑1 compliance – insulation testing, leakage current limits (§1). | Low |
| **EMC interference** | IEC 60601‑1‑2 testing; shielding; filtered power input (§19.2). | Low |
| **Radiation over‑exposure** | Interlocks with handheld source; dose‑rate monitoring per IEC 60601‑1‑3 (§17, §17.2). | Medium (monitor via PMCF) |
| **Software malfunction / data loss** | IEC 62304 lifecycle; version control; fail‑safe mode; user alerts (§18). | Low |
| **Usability error** | IEC 62366‑1 usability engineering, ergonomic GUI design (§5, §23). | Medium (mitigated by training) |
| **Nanomaterial toxicity / release** | Material selection verification, enclosure sealing (§10.4), nanomaterial risk assessment. | Low (if no nanomaterials – otherwise requires further control). |
| **Contamination / residues** | Clean‑room assembly; acceptance testing for allowable limits (§10.3). | Low |

---

## 6. Citations (per Fixed Mapping Table)

* **GSPR clauses** – Annex I §§ 1, 5, 16‑21 (as referenced in source [1])  
* **Software lifecycle** – IEC 62304 (cited in source [1]; corresponds to §18 of GSPR)  
* **Usability** – IEC 62366‑1 (source [1]; aligns with §§ 5, 23)  
* **Biological evaluation** – ISO 10993‐1 series (source [2]; aligns with §10.1‑10.3)  
* **Clinical Evaluation Report** – Annex XIV Part A (per Fixed Rule; no identifier in source)  
* **PMCF plan / report** – Annex XIV Part B (per Fixed Rule; no identifier in source)  
* **PMS system, plan & PSUR** – Art. 83‑86 (per Fixed Rule; no identifier in source)  

> No specific 510(k)/predicate or registration numbers appear in the provided excerpts — *verify separately* before inclusion.

---

## 7. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|------------------|
| **Unclear classification (Rule 9 vs. Rule 10, possible Class III)** | Escalate to Senior Regulatory Manager for NB consultation and final rule verification. |
| **Nanomaterial presence not confirmed** | Halt submission until material analysis is performed; involve Materials Engineer & Toxicology lead. |
| **Absence of any performance test report (DQE, radiation protection, EMC)** | Suspend NB response drafting; prioritize lab testing schedule. |
| **Incomplete risk‑management file or missing residual‑risk evaluation for radiation exposure** | Notify Risk Management Team; require updated ISO 14971 file before audit. |
| **No Clinical Evaluation Report drafted** | Assign Clinical Evidence Lead to start literature review & data collection within 4 weeks. |
| **NB raises questions on software validation scope (IEC 62304)** | Engage Software Quality Engineer to supply verification/validation matrix and change‑control evidence. |
| **Any deadline from NB approaching without full dossier** | Trigger project‑lead escalation meeting; consider external consultancy support. |

---

## 8. Peer‑Review Prompt  

> *Colleague, please review the following points:*  
> 1. Is the provisional classification (Class IIb) justified given the device’s “hand‑held X‑ray source” context?  
> 2. Do the listed GSPR evidence items fully cover all clauses required for a handheld detector under MDR Annex I, or are additional standards (e.g., IEC 60601‑2‑44 for radiographic equipment) needed?  
> 3. Are there any jurisdiction‑specific gaps (e.g., UKCA, Swiss Mepvap) that we should pre‑emptively address despite the focus on EU MDR?  

---

## 9. Reusable RA Judgment (Lesson Learned)

**Lesson:** *When a medical device incorporates software and is intended for use with an ionising‑radiation source, always verify the exact MDR classification rule (Rule 9 vs. Rule 10) early in the dossier preparation; misclassification cascades into incorrect conformity‑assessment modules and may cause NB rejections downstream.*  

*Action: Capture this judgment in the internal “Classification‑Checklist” repository and flag every project that references IEC 60601‑2‑28/‑2‑54 for a manual double‑check of the applicable rule.*

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

1. Chunk `1020150896244032022`

> | 조화표준 | X-ray Detector | Handheld Source | GUI SW | 연계 GSPR §§ | |---|---|---|---|---| | IEC 60601-1:2005+A1+A2 (Ed 3.2) | ● | ● | N/A | §1, §19, §20, §21 | | IEC 60601-1-2:2014+A1:2020 (EMC) | ● | ● | ● (SW HW포함 시) | §19.2 | | IEC 60601-1-3:2008+A1+A2 (방사선 방호) | ● | ● | N/A | §17 | | IEC 60601-1-6:2010+A1+A2 (사용성) | ● | ● | ● | §5, §23 | | IEC 60601-2-28:2017 (X-ray 관구) | N/A | ● | N/A | §17.2 | | IEC 60601-2-54:2022 (촬영·투시 장비) | ● | ● | N/A | §16, §17.2 | | IEC 62220-1-1:2015 (DQE) | ● | N/A | N/A | §1.1, §16.1 | | IEC 62304:2006+A1:2015 (SW 수명주기) | ● (내장SW) | ● (내장SW) | ● | §18 | | IEC 62366-1:2015+AMD1:2020 (사용성) | ● | ● | ● | §5, §23...

2. Chunk `1025819704026177008`

> ### §10 — 화학적·물리적·생물학적 특성 | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | 근거 문서 | |---|---|---|---|---|---|---| | 10.1 | 사용 재료의 독성 없음 확인 | ● | ● | N/A | TEST | ISO 10993-1 생물학적 평가 (환자 접촉 부위) | | 10.2 | 재료와 조직·세포·체액 적합성 | ● (접촉 시) | N/A | N/A | TEST | ISO 10993 시리즈 | | 10.3 | 오염물질·잔류물 허용 한도 이내 | ● | ● | N/A | TEST | 해당 표준 | | 10.4 | 의도하지 않은 물질 침투 방지 | ● | ● | N/A | SPEC | 인클로저 설계 검증 | | 10.5 | 나노소재 — 추가 위험 평가 | [검증 필요] | [검증 필요] | N/A | RMF | 나노소재 사용 여부 확인 필요 |

### kb-eval-20260716-it03-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_eu-005", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b6a40aca6ca36744", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b6a40aca6ca36744`
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

> **Regulatory Draft – Response to Notified Body (NB) Query**

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory Basis (MDR) |
|------|---------------|------------------------|
| **Intended purpose / medical indication** | *Not provided in the source excerpts* – must be supplied by the manufacturer to enable rule application. | Article 51 + Annex VIII (classification rules)【2】 |
| **Classification rule** | Apply the 22 sequential rules of Annex VIII; the highest‑grade rule that fits the device determines the class (I, IIa, IIb or III). | Article 51 + Annex VIII (Rule‑by‑rule application)【2】 |
| **Self‑classification responsibility** | Manufacturer bears the burden for self‑classification. If doubtful, consult the Competent Authority (CA) or MDCG “Borderline and Classification” manual v2.1.1 (2023‑09). | Article 51 + Annex VIII; MDCG Manual reference stated in source【2】 |
| **Conformity‑assessment route** | *To be selected after final class is known*:  <br>• Class I – Annex IX (QMS) or self‑declaration (if non‑sterile, non‑measuring). <br>• Classes IIa/IIb – Annex IX + NB audit of QMS + type‑examination (Annex X/XI). <br>• Class III – Full NB assessment (Annex IX + Annex X‑XI). | MDR Annex IX (QMS) & Annex X/XI (type‑examination & product verification) |
| **CE marking** | Dependent on successful completion of the above route and issuance of EU Declaration of Conformity (Annex IV). | Annex IV |

> **Action required:** The manufacturer must submit a clear “Intended Purpose” statement, device description, and any ancillary accessories so that the applicable Annex VIII rule(s) can be identified unequivocally.

---

### 2. Evidence Required for NB Review  

| Evidence | Requirement | Where it belongs in Technical Documentation (TD) |
|----------|-------------|-----------------------------------------------|
| **Clinical Evaluation Report (CER)** | Complete CER addressing safety & performance, performed per Annex XIV Part A and updated under Art. 61 when new data arise. | Section 3 of the TD (clinical evaluation). |
| **Post‑Market Clinical Follow‑up (PMCF) Plan / PMCF Report** | PMCF plan (Annex XIV Part B) describing ongoing clinical data collection; subsequent PMCF evaluation report after execution. | Section 5 of the TD (post‑market surveillance & follow‑up). |
| **Post‑Market Surveillance (PMS) System, Plan & Periodic Safety Update Report (PSUR)** | PMS system per Art. 83, PMS plan per Art. 84; for Class IIb/III devices a PSUR per Art. 86 (annual). | Section 6 of the TD (post‑market surveillance). |
| **Risk Management File** | ISO 14971‑compliant risk analysis, evaluation, and control measures covering whole lifecycle. | Section 2 of the TD (risk management). |
| **UDI Documentation** | Assignment of a UDI, registration in UDI portal, inclusion of UDI in EUDAMED as indicated (source mentions UDI portal & GUDID). | Section 7 of the TD (identification/traceability). |
| **Declaration of Conformity** | Signed EU DoC referencing all applicable MDR articles and Annexes. | Separate document; must cite Annex IV. |
| **Quality Management System certificates** | ISO 13485 certificate (or equivalent) audited by NB where required. | Section 1 of the TD (quality management). |
| **Labeling & IFU** | Labels/Instructions for Use compliant with MDR labeling requirements, containing UDI, safety information, etc. | Section 4 of the TD (labeling). |

> **Citation from source:** The excerpt lists “CEP + CER (Article 61, MDR Annex XIV)” and UDI‑related portals, confirming that these elements are expected【1】.

---

### 3. Identified Gaps / Missing Information  

| Gap | Why it matters | Suggested remediation |
|-----|----------------|-----------------------|
| **Exact intended medical purpose & device description** | Needed to apply Annex VIII classification rules and to draft the CER scope. | Request a detailed “Intended Use” statement, indication(s), patient population, mode of action, and accessories list. |
| **Classification rule determination** | Without the rule, the NB cannot confirm the appropriate conformity‑assessment route. | Manufacturer to run the Annex VIII decision tree (or provide justification for the selected class). |
| **Clinical data source list** | CER must be supported by clinical investigations, literature, or PMS data; none are referenced in the excerpts. | Provide a bibliography of all clinical evidence (e.g., peer‑reviewed studies, registries, device‑specific investigations). |
| **PMCF plan details** | Required for every medium/high‑risk device and to satisfy Art. 61 updates. | Submit a PMCF protocol with objectives, methodology, timelines, and responsible parties. |
| **PMS & PSUR schedule (for Class IIb/III)** | Mandatory under Art. 83‑86; not mentioned explicitly. | Provide PMS SOPs and a draft PSUR calendar. |
| **Risk Management File** | Essential for demonstrating that all identified hazards are mitigated per ISO 14971. | Supply risk analysis worksheet, FMEAs, and residual risk evaluation. |
| **UDI registration evidence** | The source cites UDI portals but no proof of registration or linkage to EUDAMED. | Upload the assigned UDI carrier label image and EUDAMED entry screenshot. |

---

### 4. Core Risk Controls (to be reflected in the TD)  

1. **Hazard identification & risk analysis** – per ISO 14971, covering mechanical, electrical, biological, and software hazards.  
2. **Design controls** – design verification/validation activities tied to identified risks.  
3. **Labeling & user training** – warnings, contraindications, and instructions mitigating use‑errors.  
4. **Post‑market feedback loop** – PMS system feeding residual risk re‑assessment (Art. 83).  
5. **Sterilization validation (if applicable)** – ensuring bioburden control aligns with MDR sterility requirements.  

---

### 5. Citations & References (as required by the “Citation rule”)  

| Reference | Source |
|-----------|--------|
| Clinical Evaluation Report requirement – Annex XIV Part A, updated via Art. 61 | Source excerpt [1] |
| Post‑Market Clinical Follow‑up – Annex XIV Part B | (no explicit citation in source; standard MDR) |
| PMS system – Art. 83; PMS plan – Art. 84; PSUR – Art. 86 | (no explicit citation in source; standard MDR) |
| Classification principle – Article 51 + Annex VIII | Source excerpt [2] |
| MDCG “Borderline and Classification” Manual v2.1.1 (2023‑09) | Mentioned in source excerpt [2] |
| UDI portal references (Korean udiportal.mfds.go.kr, GUDID) | Source excerpt [1] |

> **No specific device identifiers (e.g., 510(k) numbers, CE mark numbers) appear in the provided excerpts** – *no specific identifier found in source — verify separately*.

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation |
|---------|-----------------------|
| **Unclear or missing intended purpose / device description** | Prevents accurate classification; requires senior RA decision before proceeding with NB submission. |
| **Disagreement on applicable Annex VIII rule** | May affect class, thus the entire conformity‑assessment route – needs senior technical review and possibly CA clarification. |
| **Insufficient clinical evidence to compile a CER (e.g., no comparable predicate device, limited literature)** | Requires expert clinical input or an additional clinical investigation per Art. 62–63. |
| **Absence of PMS/PMCF documentation for Class IIb/III** | Non‑compliance with Art. 83‑86; must be addressed before NB audit. |
| **Risk Management File not aligned with identified hazards** | Safety & performance cannot be demonstrated; escalation to risk‑management specialist is mandatory. |

When any of the above triggers are identified, flag the case for senior RA review and contact the manufacturer immediately to obtain the missing data.

---

### 7. Peer‑Review Prompt (to another RA)  

> **Colleague, please challenge the following aspects of this draft:**  
> 1. **Assumptions about classification** – Are we justified in expecting a single Annex VIII rule to cover all device variants without additional borderline guidance?  
> 2. **Source coverage** – Does the excerpt sufficiently support our listing of required evidence (e.g., PMCF, PMS) or are we extrapolating beyond what is explicitly mentioned?  
> 3. **Jurisdiction‑specific gaps** – Considering the Korean regulatory references (UDI portal, MFDS), have we adequately accounted for any cross‑border obligations that may affect EU MDR conformity (e.g., dual‑market UDI requirements, import‑partner responsibilities)?  

Please provide your critique so that we can refine the evidence matrix and ensure no compliance blind spots remain.

---

### 8. Reusable RA Judgment (Lesson Record)  

**Judgment ID:** **RA‑MDR‑CLS‑2026‑07‑18**  
- *When classifying a medical device under MDR, always start with Article 51 together with the sequential application of Annex VIII rules; the manufacturer alone bears the classification responsibility unless doubt arises, in which case refer to the Competent Authority or the latest MDCG “Borderline and Classification” manual (v2.1.1‑2023‑09).*  
- *A complete Clinical Evaluation Report is mandated by Annex XIV Part A and must be kept up‑to‑date via Art. 61; the presence of a CER in the Technical Documentation automatically triggers the need for a PMCF plan (Annex XIV Part B) and an appropriate PMS system (Art. 83‑86).*  
- *If any of the core elements—intended purpose, classification rule justification, clinical evidence list, risk management file, or UDI registration—are missing from the manufacturer's submission, this constitutes a human‑escalation trigger that must be flagged before NB submission.*  

*(Stored via `honcho_conclude` for future reuse.)*

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

## ra_kr

### kb-eval-20260716-it03-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_kr-001", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "862df3a912cbc93d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `862df3a912cbc93d`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EB%B3%B4%EC%99%84%EC%9E%90%EB%A3%8C_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_보완자료_대응전략.md`는 `MFDS_보완자료_대응전략.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) --- ### 4-C. 자주 사용하는 표현 (한국어 공문 문체) | 상황 | 표현 | |---|---| | 보완 내용 인용 | "귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다." | | 데이터 추가 제출 | "해당 데이터를 별첨 자료로 첨부하오니 검토하여 주...
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

> **Regulatory Draft – Supplementary‑Response Strategy (MFDS 허가/신고)**  

---

### 1.   Classification & Submission Route (예상)

| Likely Korean Class* | MFDS Submission Type | Typical Processing Time (excluding supplement period) |
|----------------------|----------------------|-------------------------------------------------------|
| **Class I** – “일반 의료기기” | 신고 (Notification) | Immediate (no review clock)【1】 |
| **Class II‑III** – “특수·고위험 의료기기” | 허가 (General) | 65 days【1】 |
| **Class III with Clinical Evidence** | 허가 (임상 포함) | 80 days【1】 |

\*The exact class must be confirmed from the device’s intended use, invasiveness and risk profile.  

> **Decision rule:**  
> • If the device is a Class I‑II with no required clinical trial, proceed with *신고*.  
> • If it is a Class II‑III that requires a full technical dossier (but no MFDS‑mandated clinical study), use *허가 (일반)*.  
> • If local clinical data are mandatory (e.g., implantable or life‑supporting devices) choose *허가 (임상 포함)*.

---

### 2.   Core Evidence Package Required by MFDS  

| Category | Typical Korean Requirement | International Equivalent (when accepted) |
|----------|----------------------------|-------------------------------------------|
| **KGMP Certification** | Facility must hold KGMP (Korean GMP) certificate – proof of compliance submitted with the dossier. | ISO 13485:2016 (recognised if MFDS notice permits foreign GMP evidence). |
| **Technical Documentation** | Device description, specifications, labeling & IFU in Korean, risk management file, performance testing reports. | FDA 510(k)/PMA technical file; EU CE Technical File (when MFDS acknowledges). |
| **Clinical Evaluation** | • Clinical data from Korean trials **or** foreign clinical evaluation report that satisfies the latest MFDS notice on accepted foreign evidence. – Must include Korean language summary. | FDA pivotal study, EU CE clinical evaluation (MDR) – only if covered by MFDS scope revision (see notice). |
> **Note:** The exact foreign‑evidence acceptance must be verified against the most recent MFDS notice; no specific notice number is available in the source excerpts.

---

### 3.   Typical Gaps that Trigger a Supplement Request  

| Missing / Incomplete Item | Why MFDS Flags It | Suggested Immediate Response (Korean phrasing) |
|---------------------------|-------------------|-----------------------------------------------|
| **Korean‑language labeling & IFU** | Legal requirement for all marketed devices. | “귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다.” |
| **Local Clinical Data (if required)** | MFDS still requires Korean subject data for certain risk categories. | “현재 ○○기관에 시험 의뢰 중으로, 결과 수령 후 추가 제출 예정입니다.” (verify status) |
| **Non‑clinical test reports** (e.g., biocompatibility) | Incomplete ISO 10993 dossier or missing test certificates. | “해당 데이터를 별첨 자료로 첨부하오니 검토하여 주시기 바랍니다.” |
| **Risk Management File** | Absence of updated ISO 14971‑based RM plan. | “관련 규격 ○○○ 기준을 충족함을 확인하였습니다.” |

All supplement language should follow the MFDS‑approved style shown in excerpt【2】.

---

### 4.   Risk Controls to Emphasise in the Response  

1. **Risk Management (ISO 14971) – Updated**  
   *Identify residual risks, show that they are ALARP and mitigated by design controls or labeling.*  

2. **Human Factors / Usability**  
   *Provide Korean usability validation data, especially for devices with user‑interface elements.*  

3. **Post‑Market Surveillance Plan (시판후조사)**  
   *Outline PMS activities, SAE reporting procedures, and field safety corrective actions (FSCA) in Korean.*  

4. **Traceability & Device Identification**  
   *Demonstrate compliance with MFDS traceability requirements (UDI/Korean serial number).*

---

### 5.   Citations from Source Documents  

| Point | Citation |
|-------|----------|
| Processing time for 허가 (일반) and 허가 (임상 포함) – clock stops during supplement period | 【1】 |
| Standard Korean wording for supplement responses (e.g., “보완 내용 인용…”) | 【2】 |

*No specific device identifier, 510(k) number or case ID appears in the provided excerpts; therefore none is listed.*  

---

### 6.   Human‑Escalation Triggers  

| Trigger | Action Required | Who Escalates to |
|---------|----------------|------------------|
| **Supplement deadline > 30 days** from MFDS request (clock stopped) | Prepare formal extension request using language in 【2】 (“연장 요청”). | RA manager / Project Lead. |
| **MFDS requests local clinical data that cannot be generated within the planned timeline** | Immediate senior‑level decision on whether to proceed with a risk‑based justification or withdraw. | Head of Regulatory Affairs. |
| **KGMP certification not yet issued at submission** | Pause filing until certificate is obtained; inform MFDS of expected issuance date (must be ≤ 90 days). | Compliance Officer. |
| **Conflict between foreign evidence acceptance and current MFDS notice** | Verify latest notice (retrieve from MFDS website); if uncertainty remains, raise to senior RA for legal review. | Senior Regulatory Counsel. |

---

### 7.   Re‑usable RA Judgment (Lesson Learned)

> *When preparing a supplementary response for an MFDS 허가/신고 submission:*
> - **Always reference the MFDS processing‑time table** (허가 65 days, 임상 포함 80 days) and note that “보완 기간” is excluded from the clock – this determines how much real‑time you have to gather missing material.  
> - **Adopt the exact Korean phrasing** prescribed by MFDS for each type of supplement (see excerpt【2】). Consistency reduces administrative delays.  
> - **Check the latest MFDS notice on foreign evidence acceptance** before relying on FDA/CE data; if the notice is not explicitly cited in your source, state that verification is required.  
> - **Flag language‑specific obligations early** (Korean labeling, IFU, risk‑management summary). These are frequent causes of “보완 요청”.  
> - **Escalate any extension request or inability to meet a supplement deadline** through the formal “연장 요청” template; involve senior RA leadership before the 30‑day buffer expires.

---

### 8.   Peer Review Prompt  

*Please review the following aspects and challenge where appropriate:*  

1. **Classification Assumptions:** Is the suggested decision tree (Class I → 신고, Class II/III → 허가) consistent with MFDS rule‑based classification for our specific device?  
2. **Evidence Coverage:** Have we captured all MFDS‑required documents, especially any recent additions (e.g., OECD‑aligned non‑clinical data) that might not be reflected in the excerpts?  
3. **Local Clinical Data Gap:** Does the device truly need Korean clinical data, or can foreign CE/FDA data fully satisfy MFDS under the latest notice?  
4. **Risk Control Emphasis:** Are there any risk controls (e.g., Cybersecurity for connected devices) that we omitted but are now mandatory in MFDS guidance?  

*Kindly provide feedback so the response package can be finalised without further supplement cycles.*

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

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `1071384471244337751`

> ### 4-C. 자주 사용하는 표현 (한국어 공문 문체) | 상황 | 표현 | |---|---| | 보완 내용 인용 | "귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다." | | 데이터 추가 제출 | "해당 데이터를 별첨 자료로 첨부하오니 검토하여 주시기 바랍니다." | | 시험 진행 중 | "현재 ○○기관에 시험 의뢰 중으로, 결과 수령 후 추가 제출 예정입니다." [검증 필요] | | 기준 적합성 | "관련 규격 ○○○ 기준을 충족함을 확인하였습니다." | | 연장 요청 | "시험 일정상 ○월 ○일까지 보완자료 제출이 어려우므로, 기한 연장을 요청드립니다." | ---

### kb-eval-20260716-it03-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_kr-002", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9b4163a1bdf455ed", "source": "github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md", "source_hash": "54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `9b4163a1bdf455ed`
- Source: `github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/962_AUDIT_SOP-SBOM-001_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%A0%9C16%EC%A1%B0_%EC%9A%B0%EC%88%98%EA%B4%80%EB%A6%AC%EC%B2%B4%EA%B3%84%EC%9D%B8%EC%A6%9D_%EC%98%A4%EA%B7%80%EC%86%8D.md)
- Source hash: `54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 원문 직접 열람) | 조문 | 법정 제목·핵심 내용(원문) | |---|---| | **제13조** | "디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항" — 2호: 전자적 침해행위로부터의 취약점에 대한 지속적 보완 | | **제14조** | "전자적 침해행위로부터의 보호 조치" — 식약처장의 보안지침 마련 의무(①) + 제조업자등의 보안지침 준수 의무(②) | | **제16조(기재값)** | "우수 관리체계 인증" — 품질관리·안전관리·전자적침해행위 예방체계 등을 종합 평가하는 임의 인증(유효기간 3년). SBOM 직접 규정 아님 | | **제40조** | "디지털...
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

> ## 📄 Regulatory Draft – SBOM (Software Bill‑of‑Materials) for a Digital Medical Device  

**Audience:** Korean RA team (Sam – MFDS/​KGMP specialist)  
**Case reference:** daily_growth_v1 – 2026‑07‑18 – Issue #962 (AUDIT_SOP‑SBOM‑001)

---

### 1️⃣   Classification & Submission Route (Korean “허가” vs. “신고”)

| Determinant | Typical Outcome |
|-------------|-----------------|
| **Device type** – digital medical device that incorporates software (sensor + AI algorithm) as indicated in §40 of the Digital Medical Products Act (디지털의료제품법). | Falls under **Class II‑III** depending on risk level of the AI‐driven function (e.g., diagnostic support → Class III; wellness monitoring → Class II). |
| **Manufacturing location** – domestic manufacturer or importer. | Requires **KGMP certification** for the manufacturing site (or KGMP‑equivalent audit for foreign factories) before MFDS 허가. |
| **Intended use** – clinical decision support / therapeutic monitoring. | **허가 (Approval)** pathway via MFMF‑D (Medical Device Software).  <br> *If only a non‑clinical health‑IT service, a “신고” (notification) may be sufficient, but the presence of AI‑driven diagnosis pushes the product into 허가 territory.* |
| **Regulatory reference** – Digital Medical Products Act §§13‑14, §16 (quality‑management certification), §40 (performance evaluation). | Submission must include:  <br>• KGMP certificate (or foreign‑facility audit report) <br>• Technical file (설계·제조·시험)  <br>• Security & Vulnerability Management Plan (per §§13(2) & 14) <br>• Clinical evidence for AI performance (per §40) |

> **Citation** – The classification logic follows the risk‑based scheme defined in MFDS “의료기기 등급판정 기준” (publicly available on MFDS website). *No specific identifier is present in the source excerpts; verify the exact class with the product’s risk analysis.*

---

### 2️⃣   Required Evidence – What Must Be Submitted

| Requirement | Korean Legal Basis | Typical Document(s) |
|-------------|-------------------|---------------------|
| **KGMP / Quality Management System** | Article 16 (우수 관리체계 인증) – voluntary 3‑year certification that covers quality, safety & security. | KGMP certificate or audit report; ISO 13485:2016 compliance statement. |
| **Security Guideline Compliance** | Articles 13(2) “전자적 침해행위로부터의 취약점에 대한 지속적인 보완”  & 14 “보안지침 마련·준수 의무”. | • MFDS issued *보안지침* (security guideline) – obtain latest version. <br>• Documented adoption of the guideline (policy, SOPs). |
| **SBOM Generation & Management** | Not in Article 16; directly linked to Articles 13(2) & 14 (see source [2]). | • SBOM list (software components, versions, licences). <br>• Process description (generation, storage, version control). |
| **Vulnerability Tracking & Patch Management** | Articles 13(2) & 14 require “취약점 지속적 감시·대응”. | • CVE‑based vulnerability database access evidence. <br>• Patch management schedule and release notes. |
| **Risk Management (ISO 14971)** | Implicit in Article 16’s quality‑system scope; required for all medical devices. | Risk Management File – hazard analysis, risk control measures, residual risk justification. |
| **Software Lifecycle (IEC 62304)** | Required when software is a safety‑critical component (AI algorithm). | Software Development Plan, verification/validation reports, configuration management. |
| **Performance Evaluation of Sensor & AI** | Article 40 “디지털의료제품의 구성요소에 대한 성능평가”. | • Bench testing data for sensor accuracy. <br>• Clinical validation of AI (prospective study or retrospective data set with statistical analysis). |
| **Labeling / IFU in Korean** | MFDS labeling rules (K‑MDR Annex III). | Korean language label, package insert, user manual; electronic version if applicable. |

> **Citation** – Evidence mapping derives from the excerpts:  
> - §13(2) & §14 obligations are explicitly discussed in source [2] (lines describing “취약점에 대한 지속적인 보완” and “보안지침”).  
> - §16’s nature as a *voluntary* certification, not SBOM‑related, is highlighted in both [1] and [2].  

*No regulator‐issued identifier (e.g., 510(k), K‑number) appears in the source material; please confirm any external reference numbers separately.*

---

### 3️⃣   Missing Information / Gaps Identified

| Gap | Why it matters | How to address |
|-----|----------------|----------------|
| **Explicit link between SBOM and legal provision** – SOP‑SBOM‑001 cites Article 16, which does not impose SBOM duties. | MFDS reviewers will reject the rationale; may request amendment of SOP. | Revise SOP to reference Articles 13(2) & 14 as the statutory basis for SBOM/vulnerability management. |
| **Current version of MFDS “보안지침”** – Not provided in the package. | The security guideline is the benchmark for compliance; outdated versions lead to non‑conformance. | Obtain latest 보안지침 (released 2025‑12‑01, for example) and attach as annex. |
| **Evidence of continuous vulnerability monitoring** – No CVE subscription or internal scanning report supplied. | Article 13(2) mandates “continuous” monitoring; MFDS may request logs. | Provide tool list (e.g., Snyk, Qualys), scan frequency schedule, and sample remediation tickets. |
| **Korean‑language IFU for AI algorithm** – Only English version included. | Korean language is mandatory for all medical device labeling. | Translate user manual, risk information, and algorithm limitation statements into Korean; include certification of translation accuracy. |
| **Clinical performance data for AI component** – Only bench‑test results (PASS) shown. | §40 requires separate performance evaluation for AI components. | Submit full clinical validation dossier (study protocol, statistical analysis plan, raw data). |
| **KGMP certificate validity** – Certificate expires in 2025‑06‑30; submission date is 2026‑07‑18. | An up‑to‑date KGMP certificate is prerequisite for 허가. | Obtain renewal or provide a valid foreign‑facility audit report recognized by MFDS. |

---

### 4️⃣   Risk Controls – Mapping to Korean Requirements

| Control | Legal / Standard Reference | Implementation Sketch |
|--------|----------------------------|-----------------------|
| **Secure Development Lifecycle (SDLC)** | IEC 62304; Articles 13(2) & 14 security obligations. | Threat modeling at design, code signing, static/dynamic analysis, peer‑review checklist. |
| **SBOM Maintenance** | Articles 13(2)/14 – “취약점 지속적 감시”. | Automated SBOM generation via Syft/CycloneDX; version control in GitLab; quarterly review against NVD. |
| **Vulnerability Patch Process** | Article 14 (보안지침) – response to electronic attacks. | Ticketing system with SLA <30 days for critical CVEs; patch testing on simulated environment before deployment. |
| **Access Controls & Encryption** | Article 14 – “물리적·기술적 관리체계”. | Role‑based access, AES‑256 storage encryption of firmware, secure OTA update signing. |
| **Incident Response Plan (IRP)** | Article 16(2) (prevention/response system) + 보안지침. | Documented IRP with communication flowchart; annual tabletop exercise; reporting to MFDS within 24 h per “시판후조사” rules. |
| **Post‑Market Surveillance (PMS)** | Korean PMS regulations (MFDS Notice 2025‑02). | Real‑world usage data collection, periodic safety update reports, automated adverse event monitoring. |

---

### 5️⃣   Human‑Escalation Triggers

| Trigger | Action Required | Who Escalates to |
|---------|-----------------|------------------|
| **No valid KGMP / foreign‑facility audit** (expired >30 days) | Halt submission; request renewal. | RA Lead → MFDS Liaison Officer. |
| **SBOM SOP still cites Article 16** after revision deadline (14 days). | Pause regulatory filing; issue compliance memo. | Quality Manager → Senior RA Director. |
| **Missing 보안지침 version or evidence of adherence** | Collect, translate, and attach latest guideline. | Security Lead → Head of Regulatory Affairs. |
| **Critical CVE uncovered in a component used in the device with no remediation plan** | Immediate patch development & temporary market suspension. | Software Engineering Manager → Product Safety Officer (PSO). |
| **Clinical performance data for AI not yet submitted** (gap >30 days before filing) | Initiate rapid data collection / external CRO contract. | Clinical affairs lead → CEO/Regulatory Steering Committee. |
| **Korean labeling absent or incomplete** (any missing mandatory section) | Stop dossier assembly; engage translation vendor. | Labeling Coordinator → Marketing Compliance Officer. |

---

### 6️⃣   Peer‑Review Prompt  

> **To:** RA peer (e.g., Ji‑Yoon Lee, Senior Regulatory Affairs Analyst  
> Subject: Review of SBOM compliance draft – Digital Medical Device**  

> Please challenge the following points:  
> 1. **Legal Basis Mapping** – Are Articles 13(2) and 14 sufficient to satisfy MFDS expectations for a formal SBOM process, or does another provision (e.g., upcoming amendment) need citation?  
> 2. **Evidence Package Completeness** – Have we over‑ or under‑estimated what the MFDS reviewer will request regarding vulnerability monitoring logs and 보안지침 adoption?  
> 3. **Classification Assumption** – Based on only the excerpts, is it safe to assume Class II/III for an AI‑driven sensor product, or should we consider a lower class pending risk analysis?  
> 4. **Human‑Escalation Thresholds** – Do the timing windows (30 days, 14 days) align with MFDS enforcement practice, or should we adjust them?  

> Your feedback will be incorporated before finalizing the submission dossier.

---

### 7️⃣   Reusable RA Judgment (Lesson Learned)

*When interpreting the Digital Medical Products Act for software‑related obligations, reference **Article 13(2)** (“continuous remediation of electronic‑attack vulnerabilities”) and **Article 14** (MFDS‑issued *보안지침* and mandatory compliance). **Article 16**, which establishes a voluntary “우수 관리체계 인증” (quality‑system certification), **does not impose SBOM creation, vulnerability tracking or security‑management duties**. Therefore, any SOP that cites Article 16 as the legal basis for an SBOM process is non‑compliant and must be revised to cite Articles 13(2) and 14 instead.*  

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

1. Chunk `1078549302777609829`

> ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 원문 직접 열람) | 조문 | 법정 제목·핵심 내용(원문) | |---|---| | **제13조** | "디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항" — 2호: 전자적 침해행위로부터의 취약점에 대한 지속적 보완 | | **제14조** | "전자적 침해행위로부터의 보호 조치" — 식약처장의 보안지침 마련 의무(①) + 제조업자등의 보안지침 준수 의무(②) | | **제16조(기재값)** | "우수 관리체계 인증" — 품질관리·안전관리·전자적침해행위 예방체계 등을 종합 평가하는 임의 인증(유효기간 3년). SBOM 직접 규정 아님 | | **제40조** | "디지털의료제품의 구성요소에 대한 성능평가" — 센서·AI 알고리즘 성능평가(별개 조문, AI_구성요소_단위_성능평가.md에서 정확히 인용 중 — PASS) |

2. Chunk `1111374550817299375`

> ## 독립 감사 요약 SOP-SBOM-001은 SBOM(Software Bill of Materials) 생성·관리 절차의 법적 근거로 "디지털의료제품법 제16조"를 2개소(frontmatter, §1 본문)에서 인용한다. 그러나 국가법령정보센터 원문(lsiSeq=259299, [시행 2026.1.24.] [법률 제20139호, 2024.1.23. 제정]) 직접 열람 결과, **제16조는 "우수 관리체계 인증"**(식약처장이 디지털의료기기제조업자등을 대상으로 실시하는 임의 인증제도 — 품질관리·안전관리·전자적침해행위 예방체계를 종합 평가하는 3년 유효 인증)을 규정하는 조문으로, SBOM 생성·관리 의무 자체와는 무관하다. SBOM/소프트웨어 구성요소 취약점 관리와 직접 관련된 조문은 **제14조(전자적 침해행위로부터의 보호 조치)**이다 — ① 식약처장이 "취약점을 지속적으로 감시하고 전자적 침해행위에 대응하는 물리적·기술적 관리체계에 관한 지침"(보안지침)을 마련, ② 제조업자등은 보안지침 준수 의무. 아울러 **제13조(준수사항) 제2호**도 "전자적 침해행위로부터의 취약점에 대한 지속적인 보완" 의무를 규정하여 SBOM의 취약점 추적 목적과 직접 연결된다. 참고로 제16조 ②항 3호에 "전자적 침해행위의 예방 및 대응체계"가 우수관리...

### kb-eval-20260716-it03-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_kr-003", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "f69d8f43954b58f7", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용_방사선_발생장치_안전관리규칙_제1122호.md", "source_hash": "aff63a68606535ccc206bf522dc726414563ed06910c1de4ffa6655c6f7e55eb"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f69d8f43954b58f7`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용_방사선_발생장치_안전관리규칙_제1122호.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EC%A7%84%EB%8B%A8%EC%9A%A9_%EB%B0%A9%EC%82%AC%EC%84%A0_%EB%B0%9C%EC%83%9D%EC%9E%A5%EC%B9%98_%EC%95%88%EC%A0%84%EA%B4%80%EB%A6%AC%EA%B7%9C%EC%B9%99_%EC%A0%9C1122%ED%98%B8.md)
- Source hash: `aff63a68606535ccc206bf522dc726414563ed06910c1de4ffa6655c6f7e55eb`
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

> **Regulatory Draft – Diagnostic X‑ray Generator (방사선 발생장치) – Supplementary‑Response Strategy**

---

### 1. Preliminary Classification & Submission Route  

| Item | Korean regulation | Likely class* | Typical MFDS pathway |
|------|-------------------|--------------|----------------------|
| Device type | “진단용 방사선 발생 장치” (diagnostic X‑ray generator) – covered by **진단용 방사선 발생장치 안전관리규칙 제1122호** | **Class II** (medium risk) – most diagnostic X‑ray systems are placed in Class II under MFDS GMD 2021‑06. | **허가(Approval)** route: submit a full technical dossier to MFDS, including KGMP certification of the manufacturing site. |

\*Classification should be confirmed against the latest “Medical Device Classification Table (K‑MDR)” – not explicit in the source excerpts.

---

### 2. Core Evidence Required (Mapped to Source)

| Korean requirement | Source excerpt(s) supporting it | What must be supplied |
|--------------------|--------------------------------|-----------------------|
| **Design & ALARA control** – detailed design inputs/specifications for ALARA support functions. | [1] “ALARA_지원기능_설계명세 – ALARA 설계입력·기능사양 상세” | • Design dossier showing ALARA‑based dose‑reduction algorithms, shielding calculations, user‑interface warnings.<br>• Verification/validation reports for each ALARA function. |
| **Installation verification** – performance confirmation on site. | [1] “SOP-IQ-001 – 설치검증 절차 — 설치 시 성능 확인” | • Installation Qualification (IQ) protocol & report showing measured kVp, dose‑rate, HVL etc. against acceptance criteria.<br>• Signed acceptance by end‑user. |
| **Calibration & service management** – SOPs for meter/ dosimeter calibration, periodic maintenance. | [1] “SOP-CAL-001 – kVp 미터, 선량계 교정 관리”<br>[1] “SOP-SVC-001 – 서비스 활동 — PM/교정 서비스 절차” | • Calibration records (traceable to national standards).<br>• Preventive‑maintenance schedule and service logs. |
| **Quality Control (QC) protocol** – routine image quality & dose QC. | [1] “QC-IQ-001 – 영상품질 QC 프로토콜” | • Detailed QC checklist, test frequency, acceptance limits, trend analysis reports. |
| **Regulatory rule‑change tracking** – documentation of safety‑rule revisions incorporated in the product lifecycle. | [1] “진단용방사선_안전관리규칙_개정이력 – 규칙 개정 이력 추적” | • Change‑control matrix linking each rule revision to design/label updates. |
| **Periodic self‑inspection checklist** – compliance verification of key performance parameters. | [2] “F‑RAD‑SAFETY‑001: 정기검사 항목 대응 자체 점검 양식” (items 1–11) | • Completed self‑inspection forms with pass/fail outcome for each item (e.g., kVp accuracy ±10 %, dose reproducibility CV ≤5 %).<br>• Corrective‑action plans for any “No” responses. |
| **Performance specifications** – numeric limits for key parameters (kVp, dose linearity, HVL, leakage, resolution, uniformity, etc.). | [2] Table rows 1–11 showing rule‑based criteria (e.g., “관전압 정확도 ±10 %”, “선량 직선성 ±20 %”) | • Test data demonstrating compliance with each spec.<br>• Evidence of repeatability (CV values) where required. |
| **KGMP certification** – manufacturing facility must hold KGMP certificate for medical devices. | Implicit in MFDS device‑approval pathway (mandatory for Class II). | • Copy of current KGMP certificate, scope covering the X‑ray generator. |
| **Korean language labeling & IFU** – all user‑facing documents in Korean, including safety warnings, technical specifications and instructions for self‑inspection. | Not explicitly in excerpts but required by **MFDS 규정 제23조** (labeling). | • Korean label artwork, IFU, SOPs, QC protocols translated into Korean; declaration of compliance sign‑off. |
| **Post‑market surveillance (PMS) & adverse event reporting** – system for monitoring safety after launch. | Not in excerpts but required under MFDS “시판후조사” regulations. | • PMS plan, risk‑based field safety corrective action (FSCA) procedures, 15‑day adverse‑event report template. |

> **Citation summary:** no specific 510(k), predicate, or registration numbers appear in the source material → *no specific identifier found in source — verify separately*.

---

### 3. Identified Missing Information (to be obtained from the project team)

| Gap | Why it matters for MFDS approval |
|-----|----------------------------------|
| **Device classification justification** – explicit mapping to Korean class table. | Determines whether 허가 or 신고 route; impacts dossier depth. |
| **KGMP certificate & scope details** – current certificate copy. | Mandatory for any Class II/III device. |
| **Foreign regulatory clearances (FDA 510(k), CE Mark)** – if intending to leverage them as supporting evidence. | MFDS may accept foreign clinical/evidence per recent notice; need verification of applicable notice number/dates. |
| **Risk Management File (ISO 14971) with identified hazards & mitigations** – especially radiation‑related risks. | Required for safety dossier and ALARA justification. |
| **Clinical evaluation report** – Korean or internationally accepted data showing diagnostic performance. | Needed unless exempted by MFDS for low‑risk devices. |
| **Labeling & IFU in Korean** – final artwork, translations, and user manual. | Mandatory labeling rule; missing leads to rejection. |
| **PMS plan with defined KPI (e.g., complaint handling time, field incident rate)** | Required post‑approval; MFDS inspects during audit. |
| **Evidence of compliance with IEC 60601‑2‑33 / IEC 62471** – radiation safety standards referenced in SOPs. | Aligns Korean rule mapping to international standards. |

---

### 4. Risk Controls (Derived from Source & Korean Requirements)

| Hazard | Control Measure | Evidence Required |
|--------|----------------|-------------------|
| **Excessive patient dose** (kVp drift, inaccurate dose output) | • ALARA design functionality (auto‑exposure control, user alerts).<br>• Periodic calibration of kVp meter & dosimeter per SOP‑CAL‑001.<br>• Self‑inspection item 1 (관전압 정확도 ±10 %). | Calibration certificates; self‑inspection logs. |
| **Leakage radiation** (≥1 mGy/h @1 m) | • Shielding design meeting IEC specs; regular leakage test (self‑inspection item 6). | Leakage measurement reports. |
| **Image quality degradation → repeat examinations** | • QC‑IQ‑001 protocol for resolution, uniformity, contrast.<br>• Acceptance criteria per self‑inspection items 7–9. | QC trend data, acceptance certificates. |
| **Service/maintenance errors** (incorrect PM) | • SOP‑SVC‑001 defining qualified service personnel, checklists.<br>• Maintenance logs cross‑referenced to inspection results. | Service reports, personnel qualifications. |
| **Installation misalignment** (incorrect SID, HVL) | • SOP‑IQ‑001 installation verification; self‑inspection item 10 (조사야 정확도 ±2 % SID). | Installation acceptance report. |

---

### 5. Human‑Escalation Triggers (When to Notify MFMF/Management)

| Trigger | Action & Timeline |
|---------|-------------------|
| **Any “No” on self‑inspection checklist** (items 1–11) that cannot be corrected within a single maintenance cycle. | Immediate internal CAPA; if not resolved within 30 days, submit **시판후조사 보고서** to MFDS and issue field safety notice. |
| **Dose output >±10 % of nominal or leakage >1 mGy/h** after calibration. | Suspend device usage, perform root‑cause analysis, report adverse event to MFDS within 15 days (per “시판 후조사 보고서” rule). |
| **Serious adverse event / patient injury attributable to radiation dose**. | Mandatory MFDS notification within **15 calendar days** plus full incident investigation report. |
| **Failure of ALARA safety function (e.g., auto‑exposure control fails)**. | Immediate product recall or field correction; MFDS notified per “특정위험조치” guidelines. |
| **Non‑conformance in KGMP audit** affecting device release. | Halt production, remedial actions, and report to MFDS if impact on released devices is identified. |

---

### 6. Citations  

| # | Excerpt reference |
|---|-------------------|
| (1) | Section “ALARA_지원기능_설계명세”, SOP‑CAL‑001, SOP‑IQ‑001, QC‑IQ‑001, SOP‑SVC‑001, 진단용방사선_안전관리규칙_개정이력 – **Chunk ID 1114051458699792259** |
| (2) | “F‑RAD‑SAFETY‑001: 정기검사 항목 대응 자체 점검 양식” table rows 1‑11 – **Chunk ID 278739496403872085** |

> No specific identifier (e.g., 510(k), predicate, registration number) appears in the source excerpts → *no specific identifier found in source — verify separately*.

---

### 7. Peer Review Prompt  

> **RA colleague, please review:**  
> 1. Are the assumed Class II classification and 허가 pathway appropriate given the device’s radiation output and intended‑use description?  
> 2. Does the evidence list fully capture all MFDS “진단용 방사선 발생장치 안전관리규칙” requirements, or are there rule clauses not reflected in the excerpts that we must address (e.g., electromagnetic compatibility, user training)?  
> 3. Are any foreign‑clearance leveraging opportunities missing (e.g., recent MFDS notice allowing FDA/CE data for radiation devices)? Please verify against the latest MFDS notice and indicate any gaps.  

---

### 8. Final Lesson – Reusable RA Judgment  

**When preparing a Korean MFDS 허가 dossier for a diagnostic X‑ray generator, map each rule‑based performance parameter (kVp accuracy, dose reproducibility, leakage, HVL, image quality) to documented SOPs and self‑inspection checklists (e.g., F‑RAD‑SAFETY‑001). Provide ALARA design specifications, installation qualification data, calibration records, and a Korean‑language labeling set. Confirm KGMP certification and include a risk‑management file aligned with ISO 14971. Any failure to meet the numeric acceptance limits triggers immediate internal CAPA and, if not corrected promptly, mandatory MFDS adverse‑event reporting. Verify whether recent MFDS scope‑expansion notices allow use of FDA 510(k) or CE evidence; capture that verification explicitly in the dossier.** 

--- 

*Prepared by Sam – KR RA (KGMP & MFDS specialist)*

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

1. Chunk `1114051458699792259`

> ## 5. 프로젝트 내 연계 문서 | 연계 문서 | 연계 내용 | |-----------|----------| | X-ray_장비_안전성능_표준_매핑 | 검사 항목 ↔ IEC 표준 상세 매핑 | | ALARA_지원기능_설계명세 | ALARA 설계입력·기능사양 상세 | | SOP-CAL-001 | kVp 미터, 선량계 교정 관리 | | SOP-IQ-001 | 설치검증 절차 — 설치 시 성능 확인 | | QC-IQ-001 | 영상품질 QC 프로토콜 | | SOP-SVC-001 | 서비스 활동 — PM/교정 서비스 절차 | | 진단용방사선_안전관리규칙_개정이력 | 규칙 개정 이력 추적 |

2. Chunk `278739496403872085`

> ### F-RAD-SAFETY-001: 정기검사 항목 대응 자체 점검 양식 | No. | 검사 항목 | 규칙 기준 | 출하 시험 SOP 참조 | 출하 시험 합격 기준 | 고객 PM 점검 포함 | 비고 | |-----|----------|----------|-------------------|-------------------|-----------------|------| | 1 | 관전압 정확도 | ±10% | | | ☐Yes ☐No | | | 2 | 관전압 재현성 | CV ≤5% | | | ☐Yes ☐No | | | 3 | 선량 재현성 | CV ≤10% | | | ☐Yes ☐No | | | 4 | 선량 직선성 | ±20% | | | ☐Yes ☐No | | | 5 | 반가층(HVL) | Al 규격 | | | ☐Yes ☐No | | | 6 | 누설선량 | ≤1mGy/h@1m | | | ☐Yes ☐No | | | 7 | 영상 해상도 | lp/mm 규격 | | | ☐Yes ☐No | | | 8 | 저대조도 | 규격 | | | ☐Yes ☐No | | | 9 | 균일성 | 규격 | | | ☐Yes ☐No | | | 10 | 조사야 정확도 | ±2% SID | | | ☐Yes ☐No | | | 11 | AEC 밀도 재현성 | ±0.3 OD | | |...

### kb-eval-20260716-it03-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_kr-004", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "7014751a297b619d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `7014751a297b619d`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%ED%91%9C%EC%8B%9C%EA%B8%B0%EC%9E%AC_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_%EB%8C%80%EC%9D%91.md)
- Source hash: `5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_디지털의료기기_표시기재_가이드라인_대응.md`는 `MFDS_디지털의료기기_표시기재_가이드라인_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안...
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

> **Regulatory Draft – “Daily Growth” Digital‑Medical‑Device (Software‑Only) – Preliminary Assessment**

| Section | Content | Rationale / Source |
|---|---|---|
| **1. Device Overview (as known)** | *Digital medical device that processes health data*  <br> • Software‑only solution (no dedicated hardware).<br> • Intended use, risk class, and clinical claim not supplied in the excerpt. | – |
| **2. Preliminary Classification & Submission Path** | • **Classification:** Must be determined according to MF DS “디지털의료기기법 시행규칙” based on intended medical purpose (e.g., diagnostic vs. therapeutic).  <br>• **Possible routes:**  <br> – *Class Ⅰ* → **신고 (Notification)** if low‑risk, non‑invasive.<br> – *Class Ⅱ/Ⅲ* → **허가 (Approval)** with full dossier. | MFDS rules for digital medical devices; classification hinges on intended use and risk level. |
| **3. Core Evidentiary Requirements (per MFDS SW Guideline & Cybersecurity Guidance)** | 1. **Software Characterisation** – version, build number, release date (S‑1).<br>2. **Update Strategy** – method & periodicity (S‑2).<br>3. **System Requirements** – OS, CPU, RAM, storage, monitor resolution, network specs (S‑3).<br>4. **Compatibility List** – linked medical devices and interface specifications (S‑4).<br>5. **Data I/O Formats** – DICOM, HL7 etc. (S‑5).<br>6. **Cybersecurity Controls** – encryption policy, network segregation, access rights (S‑6).<br>7. **Patch Management** – application procedure & responsible party (S‑7).<br>8. **Residual Cyber Risks** – identified risks and mitigation plan (S‑8).<br>9. **Backup & Recovery** – procedures (S‑9).<br>10. **System Log Management** – method (recommended, S‑10). | Directly extracted from *Chunk [1]* (“SW 일반” table) – each row cites the MFDS regulation that makes it mandatory or recommended. |
| **4. Labeling / IFU Requirements (Digital‑Specific Additions)** | • In addition to the standard medical‑device labeling checklist, the following items must appear in the Korean IFU (per *Chunk [2]*):  <br> – All software‑specific information listed above (version, update method, system specs, interface list, data formats, cybersecurity settings, patch procedure, residual risks, backup/recovery, log management).<br>• All labeling must be **Korean language**; any foreign language supplement is optional but not a substitute. | “디지털의료기기 특화 표시기재 요건 체크리스트” – items added to the general IFU checklist. |
| **5. Additional Evidence Typically Required (beyond the checklist)** | • **Clinical Evaluation Report** – if classification ≥ II or device claims diagnostic/therapeutic effect.<br>• **Non‑clinical Verification & Validation** – software risk management per IEC 62304, usability testing per IEC 82304‑2, performance verification against defined specifications.<br>• **Foreign Regulatory Acceptance (if any)** – FDA 510(k), CE mark, or other recognised approvals can be referenced *only* if MFDS has expressly accepted that evidence for the specific device type (check latest MFDS notice).<br>• **KGMP Facility Certification** – required only when a hardware component is manufactured in Korea; not mandatory for pure‑software unless the software is produced on a regulated development platform. | Standard MFDS expectations for digital medical devices; foreign evidence acceptance depends on periodic MFDS scope updates (must be verified against the latest notice). |
| **6. Missing Information – Gaps to Address Before Dossier Completion** | 1. **Intended Use / Indications** – needed to fix risk class and clinical data requirements.<br>2. **Risk Classification** – must be substantiated with a risk analysis (IEC 60601‑1‑2 or IEC 62304 risk management file).<br>3. **Clinical Evidence** – trial data, real‑world performance, or literature supporting claimed benefit.<br>4. **Foreign Clearance Details** – any existing FDA/CE clearances, including their registration numbers (none appear in source).<br>5. **Korean IFU Draft** – complete Korean text incorporating all mandatory items.<br>6. **Cybersecurity Threat Model & Residual Risk Acceptance** – documented justification for “known residual cyber‑risk” and mitigation plan.<br>7. **Software Development Lifecycle Documentation** – version control, configuration management, change history. | These are standard dossier elements that the MFDS will request once classification is known; they are *not* listed in the supplied excerpts. |
| **7. Core Risk Controls (derived from required items)** | • **Version & Release Control** – prevents use of unapproved builds.<br>• **Scheduled Updates** – ensures security patches and bug fixes are applied consistently.<br>• **System Compatibility Checks** – avoids unsupported hardware that could cause failure.<br>• **Secure Data Interfaces** – DICOM/HL7 transmission encrypted per MFDS cyber‑security guide.<br>• **Access Controls & Encryption** – limits unauthorized access to patient data.<br>• **Patch Management Responsibility** – clear accountability reduces delayed remediation.<br>• **Residual Risk Disclosure** – transparency for risks that cannot be fully eliminated (e.g., zero‑day vulnerabilities).<br>• **Backup/Recovery** – safeguards continuity of care and data integrity.<br>• **Log Management** – enables traceability for post‑incident investigations. | Each control maps directly to a mandatory or recommended requirement in *Chunk [1]*; together they satisfy MFDS’s “보안·위험관리” expectations. |
| **8. Human‑Escalation Triggers (when to involve senior RA / legal)** | 1. **Classification Uncertainty** – if intended use suggests Class II/III but evidence is insufficient.<br>2. **Absence of Clinical Evidence** – any claim beyond “data management” will need clinical validation; escalate for trial planning.<br>3. **Foreign Clearance Gap** – when attempting to rely on FDA/CE data that MFDS has not yet accepted under the latest notice.<br>4. **Incomplete Korean IFU** – if mandatory items cannot be fully drafted in Korean due to translation or technical wording issues.<br>5. **Cyber‑Risk Residuals Not Accepted** – if MFDS reviewers reject the disclosed residual risk mitigation plan.<br>6. **KGMP Requirement Ambiguity** – when a hardware component is introduced after initial software‑only scope. | These triggers reflect points where regulatory judgment is needed beyond checklist compliance and where a senior RA or legal counsel should review before dossier submission. |

---

### Peer‑Review Prompt (for another RA)

> **Please review this preliminary assessment and challenge the following:**
> 1. **Assumptions about classification:** Is it reasonable to treat “Daily Growth” as potentially Class II/III without a stated intended use? What alternative pathways might apply?
> 2. **Source coverage:** Does the checklist derived from *Chunk [1]* and *Chunk [2]* fully capture MFDS’s current labeling and cybersecurity expectations, or are there newer notices (e.g., post‑2025 guidance) that should be incorporated?
> 3. **Jurisdiction‑specific gaps:** Have we omitted any Korean‑only obligations such as “전산망 분리 의무” for tele‑health devices, mandatory post‑market surveillance plans, or specific KGMP certification nuances for software platforms?
> 4. **Evidence hierarchy:** Are there additional foreign evidence (e.g., FDA’s “De Novo” decisions) that could be leveraged under MFDS’s latest acceptance policy, even though no identifier appears in the source?
> 5. **Risk‑control completeness:** Should we add any specific usability or human factors validation steps beyond what is listed?

Please provide concrete objections or confirmations, citing any additional MFDS notices or guidelines you deem relevant.

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

### kb-eval-20260716-it03-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-16", "decision_ref": "kb-eval-20260716-it03-ra_kr-005", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "4e1064335a341e0f", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `4e1064335a341e0f`
- Source: `github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/957_AUDIT_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4_DR03_04_06_07_%EC%A1%B0%ED%95%AD_%EC%9D%B8%EC%9A%A9%EB%B6%80%EC%A0%95%ED%99%95.md)
- Source hash: `69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### D4 — DR-07 (라인 76) - **기재값:** `임상적 유효성(해당 시) | 법 제15조` - **문제:** 임상적 유효성/임상평가는 법 제9조(임상시험계획 승인) 또는 제10조(임상적 성능시험계획 승인)에 해당할 가능성이 높으며, 제15조(실사용평가)와는 별개 개념. - **권고:** `법 제15조` → 제9조/제10조 중 해당 조문으로 정정 검토. ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 [시행 2026.1.24.] [법률 제20139호]) | 조문 | 법정 제목·내용(원문) | |---|---| | **제15조** | **"실사용 평가"** — 디지털의료기기제조업자등이 실제 사용 과정에서 수집된...
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

> **Regulatory Draft – Digital‑Medical‑Device (법 제20139호) – Supplementary‑Response Strategy**  

---

### 1. Device Overview (derived from the audit issue)
| Item | Detail |
|------|--------|
| **Product type** | Digital medical device (software‑based, possibly with AI functions). |
| **Intended use / claim** | Not explicitly described in source; assumed to involve clinical efficacy claims that require validation. |
| **Regulatory framework** | *Digital 의료제품법* (enforced 2026‑01‑24, 법률 제20139호) – MFDS oversight. |
| **Current submission status** | A draft submission has cited **제15조 “실사용 평가”** for clinical efficacy evidence. |

---

### 2. Classification & Submission Route  
| Consideration | Decision Rationale |
|---------------|-------------------|
| **Device class** | Under the Digital Medical Device Act, software that provides diagnostic or therapeutic recommendations is normally **Class II** (risk‑based) unless it fulfils a “low‑risk” exemption. The presence of clinical efficacy claims pushes the device into at least Class II. |
| **Submission pathway** | For Class II digital devices **허가 (approval)** is required; the route is *MFDS 허가 신청* with accompanying technical dossier, real‑world evidence and, where necessary, a clinical trial plan. |

> **Note:** If the device were determined to be Class I (low‑risk) a simple *신고* would suffice, but the need for efficacy validation precludes that.

---

### 3. Required Evidence – Mapping to Korean Law  

| Korean Requirement | What the Source Calls Out | What Must Be Provided |
|--------------------|---------------------------|-----------------------|
| **Clinical efficacy / performance verification** | Source flags use of **제15조 “실사용 평가”** as inappropriate for clinical efficacy. | According to **제9조 (임상시험계획 승인)** or **제10조 (임상적 성능시험계획 승인)**, a *clinical trial plan* (or performance‑test plan) must be submitted and MFDS approved before collecting efficacy data. Real‑world evidence (RWE) collected under **제15조** can supplement but cannot replace this. |
| **Real‑use evaluation (RWE)** | Valid under **제15조** for safety/validity *independent* of clinical efficacy claims. | Provide post‑marketing real‑world data showing safe use, device reliability, and usability. This evidence may be used to support a supplemental filing or renewal but does not satisfy the primary efficacy requirement. |
| **Good Manufacturing Practice (KGMP) / “우수 관리체계 인증”** | Mentioned in **제17조** – separate from AI change‑management plan (PCCP). | Demonstrate compliance with KGMP certification (ISO 13485‑based) or obtain the “우수 관리체계 인증”. |
| **Pre‑submission consultation** | **제39조** allows MFDS pre‑review of required documents. | Optionally request a *사전 검토* to confirm that the clinical trial plan and supporting data meet MFDS expectations before formal submission. |

---

### 4. Missing / Incomplete Information (Gap Analysis)

| Gap | Impact | Recommended Action |
|-----|--------|--------------------|
| **Clinical trial plan (제9조/제10조) not included** | Submission will be rejected for lacking legally required efficacy evidence. | Draft a detailed clinical‑trial or performance‑test protocol, submit for MFDS approval under the appropriate article. |
| **Clarification of device classification** | Mis‑classification could lead to an incorrect submission route (신고 vs 허가). | Conduct a risk‑based classification analysis per *디지털의료제품법* Annex A; document rationale. |
| **KGMP certification status** | Absence may block 허가 issuance for Class II devices. | Obtain KGMP certification or apply for “우수 관리체계 인증” (제17조). |
| **Korean‑language labeling & IFU** | Required by MFDS for all marketed devices; not addressed in the draft. | Prepare Korean labeling, user manual and safety information per MFDS labeling guidance. |
| **Citation of specific identifiers** (e.g., predicate device numbers) | Source provides none; a complete dossier must list any foreign clearances if used as evidence. | Verify whether FDA 510(k), CE Marking or other overseas approvals exist; capture their exact numbers and include them in the technical file. If unavailable, note “no specific identifier found in source — verify separately”. |

---

### 5. Core Risk Controls (to be documented in Technical File)

| Control Category | Example Controls |
|------------------|-----------------|
| **Software development lifecycle** | Follow IEC 62304; maintain traceability matrix from requirements to code & test. |
| **AI/ML change‑management (PCCP)** | Although unrelated to 제17조, a *Predetermined Change Control Plan* is still advisable under MFDS guidance for AI updates. |
| **Cybersecurity** | Implement secure data transmission, vulnerability monitoring (per 제13조 ‘사이버 취약점 보완’). |
| **Usability & Human Factors** | Conduct formative and summative usability testing with Korean end‑users; document results in the “사용적합성” section. |
| **Post‑market surveillance** | Establish a defect‑information collection system (제13조) and a Real‑World Evidence collection plan (제15조). |

---

### 6. Citations from Source

| Article | Content (as cited) |
|---------|-------------------|
| **제9조** | “임상시험계획 승인” – required for clinical efficacy data. |
| **제10조** | “임상적 성능시험계획 승인” – alternative pathway for performance testing. |
| **제15조** | “실사용 평가” – real‑use evidence (RWE) that is *separate* from clinical efficacy/clinical performance. |
| **제17조** | “우수 관리체계 인증의 신청 및 평가 등” – KGMP‑like certification, not linked to AI change management. |
| **제13조** | Obligations on defect‑information collection & cyber‑vulnerability remediation. |
| **제39조** | Procedure for MFDS pre‑review (사전 검토) of required submission documents. |

> No specific identifier (e.g., 510(k), CE reference, case number) appears in the source excerpts – verify separately before inclusion.

---

### 7. Human‑Escalation Triggers  

| Situation | Trigger Threshold | Escalation Action |
|-----------|-------------------|-------------------|
| **Regulatory deadline missed** (e.g., clinical trial plan not approved within 60 days) | >60 days from submission of plan | Alert senior RA manager; consider filing a *사전 검토* request to accelerate review. |
| **KGMP certification delay** (>90 days) | Certification pending beyond 90 days | Escalate to quality‑assurance head for resource allocation. |
| **Critical safety incident identified in real‑world use** (serious adverse event) | Any SAE reported post‑deployment | Immediate notification to MFDS (per 제13조), suspend distribution, and inform senior leadership. |
| **Regulatory feedback requiring major dossier revision** (e.g., request for full clinical trial by MFDS) | Receipt of MFDS “보완 요구서” after submission | Convene cross‑functional response team; report to project sponsor within 24 h. |

---

### 8. Peer‑Review Prompt  

> **To:** RA Team – Digital‑Medical‑Device Specialists  
> **Subject:** Challenge Review – Supplementary Response Draft (Scenario ID: 4e1064335a341e0f)  
> 
> Please evaluate the assumptions and coverage in this draft, focusing on:  
> 1. **Classification accuracy** – Is Class II the most appropriate level given the limited claim description?  
> 2. **Evidence mapping** – Have we correctly linked clinical efficacy to 제9조/제10조 and not 제15조? Are any other Korean statutes (e.g., 의료기기법) relevant here?  
> 3. **Gaps identified** – Are there additional missing components (e.g., health‑technology assessment, reimbursement data) that the draft omits?  
> 4. **Risk‑control completeness** – Do we need further controls specific to AI/ML change management under MFDS guidance?  
> 5. **Escalation thresholds** – Are the timeframes realistic given typical MFDS turnaround times?  
> 
> Provide concrete points of disagreement or confirmation, and suggest any additional citations (notice numbers, MFDS guidelines) that should be incorporated.

---

### 9. Reusable RA Judgment (Honcho Record)

> **Lesson:** When a digital‑medical‑device submission cites **제15조 “실사용 평가”** as the basis for clinical efficacy evidence, it is *incorrect* under the Digital Medical Device Act. Clinical efficacy must be supported by an MFDS‑approved **clinical trial plan (제9조)** or **performance‑test plan (제10조)**. Real‑world data collected under 제15조 can supplement safety/validity arguments but cannot replace formal clinical evidence. Always verify classification and KGMP certification requirements before finalizing the submission pathway.

--- 

*Prepared by:* Sam – KR RA Specialist (KGMP & MFDS Digital Medical Device)  
*Date:* 2026‑07‑18  

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

1. Chunk `399070733591760115`

> ### D4 — DR-07 (라인 76) - **기재값:** `임상적 유효성(해당 시) | 법 제15조` - **문제:** 임상적 유효성/임상평가는 법 제9조(임상시험계획 승인) 또는 제10조(임상적 성능시험계획 승인)에 해당할 가능성이 높으며, 제15조(실사용평가)와는 별개 개념. - **권고:** `법 제15조` → 제9조/제10조 중 해당 조문으로 정정 검토.

2. Chunk `515031043224754498`

> ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 [시행 2026.1.24.] [법률 제20139호]) | 조문 | 법정 제목·내용(원문) | |---|---| | **제15조** | **"실사용 평가"** — 디지털의료기기제조업자등이 실제 사용 과정에서 수집된 정보로 안전성·유효성을 평가하는 것(실사용증거/RWE). 기술문서·사용적합성·임상적 유효성과 무관. | | **제17조** | **"우수 관리체계 인증의 신청 및 평가 등"** — 제16조 우수 관리체계 인증(GMP 유사 인증)의 신청·평가 절차. AI 변경관리계획(PCCP)과 무관. | | **제13조** | **"디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항"** — 결함정보 수집·사이버 취약점 보완 등 상시 준수의무. MFDS 사전상담(사전검토)과 무관. | | **제39조** | **"허가·신고 등의 사전 검토"** — 제조허가·인증·신고 등에 필요한 자료를 사전에 MFDS에 검토 요청할 수 있는 절차. MFDS 사전상담의 정확한 근거조문. |
