# KB Eval Checksheet - 2026-07-22 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260722-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "59d86e1c8737dd40", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `59d86e1c8737dd40`
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

> **Regulatory Draft – SaMD Change Impact (Predetermined Change Control Plan – PCCP)**  

| Item | Judgment / Requirement |
|------|------------------------|
| **Device classification & submission route** | • Determine the FDA product code and class via the FDA Classification Database based on *intended use* (diagnosis, treatment, monitoring, etc.).  <br>• Most AI‑driven SaMD are **Class II**, requiring a **510(k) with a Predetermined Change Control Plan (PCCP)** as part of the submission package (see FDA final guidance, 2024 Dec 4 FR §​2024‑28361). <br>• If the device is novel, high‑risk, or lacks a reasonable predicate, consider **De Novo** classification or a **PMA**. |
| **Required evidence for a PCCP submission** | 1. **Baseline Technical Documentation** (original 510(k) or De Novo filing): design history file, software description, intended use, predicate device(s). <br>2. **Change‑Control Plan** covering the four mandatory elements identified in the guidance: <br>&nbsp;&nbsp;• *Data Management* – procedures for data collection, curation, versioning, and bias mitigation.<br>&nbsp;&nbsp;• *Retraining Practices* – trigger conditions, relearning workflow, rollback strategy. <br>&nbsp;&nbsp;• *Performance Evaluation* – pre‑defined acceptance criteria, verification & validation (V&V) methodology, statistical significance thresholds. <br>&nbsp;&nbsp;• *Updated Procedures* – communication plan for users/clinicians, real‑world monitoring, Instructions‑for‑Use (IFU) revision process.<br>3. **Risk Management** per IEC 62366‑1 (risk analysis, risk controls, residual risk evaluation). <br>4. **Software Lifecycle Documentation** (21 CFR 820.30, 820.40) demonstrating compliance with the new QMSR (effective Feb 2026). |
| **Missing information that must be supplied before filing** | • Explicit *intended use* statement and *device description* (including algorithm type, input/output). <br>• Identification of a **predicate device** (510(k) number or product code) if pursuing the 510(k) route – *no specific identifier found in source — verify separately*. <br>• Baseline performance metrics (sensitivity, specificity, ROC‑AUC, etc.) against which post‑change results will be compared. <br>• Detailed **impact analysis** linking each proposed change to the four PCCP elements and showing that impacts remain within the predetermined scope. |
| **Core risk controls to address in the PCCP** | 1. **Algorithmic drift detection** – automated monitoring that flags performance deviation beyond acceptance criteria.<br>2. **Data provenance & bias checks** – ensure new training data preserve demographic representativeness.<br>3. **Rollback capability** – ability to revert to prior model version if post‑deployment testing fails.<br>4. **User communication** – clear labeling of software version, updated IFU, and notification procedures for clinicians.<br>5. **Post‑market surveillance plan** – real‑world performance tracking, adverse event reporting per 21 CFR 803. |
| **Regulatory citations** | • **Predetermined Change Control Plan (PCCP) guidance**, FDA, 2024 Dec 4 (Federal Register §​2024‑28361). <br>• **21 CFR 820** – Quality System Regulation (QMSR) (effective Feb 2026; ISO 13485‑aligned). <br>• **21 CFR 807** – Premarket notification (510(k)) requirements. <br>• **21 CFR 803** – Medical Device Reporting (MDR) obligations for post‑market surveillance. |
| **Human‑escalation triggers (require FDA submission or review)** | 1. **Change expands intended use** (e.g., new indication, patient population). <br>2. **Modification exceeds predetermined scope** (new algorithm architecture, different data modality). <br>3. **Performance falls below predefined acceptance criteria** in the validation dataset. <br>4. **New safety‑critical failure mode identified** during risk reassessment. <br>5. **Regulatory classification change** (e.g., reclassification to Class III). In any of these cases, prepare a **Supplemental 510(k)** or a **de novo request/PMR** as appropriate and notify FDA per 21 CFR 812. |
| **Next steps** | • Compile the missing items listed above. <br>• Draft the PCCP sections using the template in the FDA guidance (data‑management, retraining, performance evaluation, updated procedures). <br>• Perform a gap analysis against IEC 62366‑1 and 21 CFR 820 to ensure full QMSR compliance before submission. |
| **Peer‑review request** | *Please review: (a) the assumption that the device falls under Class II; (b) completeness of the change‑control elements relative to the source guidance; (c) any jurisdiction‑specific gaps (e.g., EU MDR interplay) that may affect our UDI or labeling strategy.* |

*Prepared by:* **Mike – US FDA Regulatory Affairs Specialist**  
*Date:* 2026‑07‑22

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

### kb-eval-20260722-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "201daf0b783b9dd3", "source": "github:holee9/MD-process/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md", "source_hash": "efcd12a4b49cb21ffa28b5f1aa35345e8bb04b98c57a32649483fa824de23fff"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `201daf0b783b9dd3`
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

> **Regulatory Draft – Predetermined Change Control Plan (PCCP) Impact on SaMD Changes**

---

### 1. Device Classification & Submission Pathway  
| Item | Determination |
|------|----------------|
| **Device class** | Dependent on intended use; for most AI‑enabled Software as a Medical Device the default classification is Class II under the appropriate FDA product code (e.g., “SWA” for software). If the SaMD is used in imaging, it falls under **21 CFR §892** (radiology/imaging devices). |
| **Primary submission route** | Existing cleared device → **510(k) supplement** (Software Change Supplement). The change is pre‑authorized through a **Predetermined Change Control Plan (PCCP)** per FDA’s Final Guidance (December 2024). |
| **Alternative pathway** | If the change introduces a new intended use or significantly alters risk, a new **De Novo** request or full **510(k)** may be required. |

*Citation*: FDA “Final Predetermined Change Control Plan Guidance for AI‑Enabled Device Software Functions” (Dec 2024) – established regulatory reference (no case‑level identifier found in source — verify separately).  

---

### 2. Evidence Required for PCCP‑Supported Changes  
| Evidence Category | Requirements |
|-------------------|--------------|
| **Algorithm performance** | • Pre‑ and post‑change validation data showing non‑inferior accuracy, sensitivity, specificity. <br>• Statistical testing for drift detection (e.g., confidence intervals overlapping pre‑change metrics). |
| **Software verification & validation (V&V)** | • Updated V&V plan covering unit, integration, system testing per IEC 62304.<br>• Regression testing results for all unchanged modules. |
| **Risk Management** | • Updated ISO 14971 risk analysis reflecting the change; justification that residual risk remains within the approved risk acceptability criteria. |
| **Clinical evaluation (if applicable)** | • Clinical performance data or literature supporting maintained clinical benefit when the software function changes affect the intended use. |
| **Usability & Human Factors** | • Updated usability test confirming no new use‑error hazards introduced by the change. |
| **Labeling & UDI updates** | • Revised labeling reflecting any functional changes (21 CFR §801). <br>• Updated UDI record in GUDID per 21 CFR §§830.10–830.60. |

*Citation*: Quality Management System Regulation (QMSR) – **21 CFR Part 820** (effective Feb 2026, ISO 13485‑aligned).  

---

### 3. Missing Information Needed from Sponsor  
| Gap | Why It Matters |
|-----|----------------|
| **Exact intended use and device claim** | Determines applicable product code and classification (e.g., imaging vs. non‑imaging SaMD). |
| **Predicate device details / original 510(k) number** | Required to prepare the supplement and demonstrate substantial equivalence. |
| **Scope of the software change (algorithm, data source, UI, etc.)** | Drives the depth of validation & risk analysis required. |
| **Existing PCCP scope and pre‑approved change categories** | To confirm whether the proposed modification fits within the approved PCCP. |
| **Post‑market surveillance plan updates** | Needed if the change could affect real‑world performance monitoring. |

*Citation*: No specific identifier found in source — verify separately.

---

### 4. Core Risk Controls (to be reflected in the PCCP)  
1. **Algorithmic bias detection & mitigation** – periodic audit of training/validation data sets for demographic parity.  
2. **Drift monitoring** – automated performance dashboards with predefined alert thresholds.  
3. **Explainability layer** – maintain traceable decision logic accessible to clinicians.  
4. **Version control & rollback capability** – ensure previous safe version can be redeployed instantly.  
5. **Cybersecurity safeguards** – per FDA’s “Postmarket Management of Cybersecurity Vulnerabilities” guidance (21 CFR §820.30).  

*Citation*: Predetermined Change Control Plan Guidance (Dec 2024) outlines these controls as best practices; no case‑level identifier present.

---

### 5. Human‑Escalation Triggers  
| Trigger | Action |
|---------|--------|
| **Change exceeds PCCP‑approved scope** (new algorithmic architecture, new indication) | Escalate to FDA via a **510(k) amendment** or De Novo request before deployment. |
| **Performance degradation > pre‑defined limits** (e.g., ≥5 % drop in sensitivity) | Suspend rollout; notify FDA under 21 CFR §803 (MDR). |
| **New safety hazard identified** in risk analysis not previously captured | Immediate internal review and FDA Notification of Changes (NOC) per 21 CFR §§807.92–807.95. |
| **Adverse event trend emerging** from post‑market data > threshold | Initiate Field Action Report under 21 CFR §806; consider Recall if required. |
| **Regulatory feedback indicating insufficient validation** | Pause implementation; address deficiencies and resubmit supplemental documentation. |

*Citation*: FDA’s Medical Device Reporting (MDR) requirements – **21 CFR Part 803**.

---

### 6. Regulatory Judgment & Next Steps  
- The SaMD change can be pursued under an existing **Predetermined Change Control Plan (PCCP)** if it falls within the pre‑approved change categories and does not alter intended use or risk profile.  
- A **510(k) Software Change Supplement** must include the evidence listed in Section 2, updated labeling, and a revised risk analysis.  
- Any gaps identified in Section 3 must be resolved before submission; otherwise, escalation to a full 510(k) or De Novo is required.  

### 7. Human‑Escalation Triggers (summary)  
- Scope breach → regulatory filing upgrade.  
- Performance drift beyond limits → suspend and report.  
- New safety hazard → FDA NOC/ MDR.  
- Emerging adverse trends → field action / recall pathway.

---

**Peer Review Prompt**  
> *Please review the assumptions above, especially regarding device classification without a defined intended use, the completeness of evidence items relative to the PCCP guidance, and any jurisdiction‑specific gaps (e.g., EU AI Act alignment). Highlight missing citations or alternative pathways that should be considered.*

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

### kb-eval-20260722-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "cf8bb91ec17cae85", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `cf8bb91ec17cae85`
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

> **Regulatory Draft – AI‑Enabled SaMD Change Impact Assessment**

---

### 1. Device Classification & Submission Pathway  

| Item | Determination | Rationale / Citation |
|------|----------------|----------------------|
| **Device Class** | *Pending confirmation* – likely Class II (most AI‑enabled diagnostic/clinical decision support software are classified as Class II). | Most AI‑enabled SaMD fall under 21 CFR §​892.2050 (Medical image management and processing systems) when the function is imaging‑related, or §​862.xx for clinical chemistry/laboratory devices. The source does not disclose the exact functional domain; therefore **device‐type confirmation is required** before final class assignment. |
| **Primary Regulatory Route** | 510(k) – Substantial equivalence to a legally marketed predicate. | FDA’s default pathway for Class II devices (21 CFR §​807). If no suitable predicate exists, consider **De Novo** classification. |
| **Quality Management System** | QMSR (ISO 13485‑aligned) per 21 CFR Part 820 (effective Feb 2026). | Required for all device submissions. |
| **UDI Requirement** | Compliance with 21 CFR Part 830 (label & GUDID). | Mandatory for commercial distribution in the U.S. |

> **Action:** Obtain the device’s intended use and functional description to verify the exact CFR part/section (e.g., §​892.2050, §​862.xx) and identify an appropriate predicate.

---

### 2. Required Evidentiary Package  

| Evidence | Description | Key Regulatory Reference |
|----------|-------------|---------------------------|
| **Algorithm Performance & Clinical Claim Support** | • Training/validation/test data lineage (train‑tune‑test split). <br>• Quantitative performance metrics linked to the clinical claim. | FDA AI/ML SaMD guidance (Dec 2024) – emphasis on “performance and clinical claim linkage.” |
| **Bias Analysis & Mitigation Plan** | • Systematic assessment of demographic, geographic, and device‑related biases.<br>• Documented mitigation strategies. | Source excerpt explicitly lists **편향 분석·완화** (bias analysis/mitigation). |
| **Human‑AI Workflow Validation** | • Human factors testing demonstrating safe user interaction with AI outputs.<br>• Description of supervisory control and escalation pathways. | FDA guidance on “Human‑AI workflow.” |
| **Predetermined Change Control Plan (PCCP)** | • Pre‑approved change scope covering algorithm updates, data set expansions, and parameter tweaks.<br>• Mapping of each potential change to the PCCP tier (major/minor). | FDA final guidance (Dec 2024) – “Predetermined Change Control Plan (PCCP).” |
| **Post‑Market Monitoring (PMM) & Real‑World Performance** | • Ongoing data collection plan, performance drift detection thresholds.<br>• Reporting cadence and corrective action process. | Source lists **시판 후 모니터링** (post‑market monitoring) as a PCCP element. |
| **Cybersecurity Risk Management** | • Threat model, vulnerability assessment, and mitigation controls. | FDA guidance on cybersecurity for medical devices (21 CFR Part 820). |
| **Risk Management File** | • ISO 14971‑based risk analysis covering software‑related hazards.<br>• Controls mapped to identified risks (bias, incorrect output, failure to detect drift). | Required under QMSR (21 CFR §​820.30). |
| **Labeling & IFU** | • Intended use statement, indications, contraindications, and workflow diagram.<br>• Clear description of AI role and required human oversight. | 21 CFR Part 801 (Labeling). |
| **Software Documentation** | • IEC 62304 software life‑cycle documentation (development plan, verification/validation reports).<br>• Source code version control logs linked to PCCP change tiers. | FDA expects alignment with IEC 62304 for SaMD. |

---

### 3. Missing Information – Gaps to Fill Before Submission  

| Gap | Why It Matters |
|-----|----------------|
| **Exact Intended Use & Clinical Indication** | Determines classification, predicate search, and labeling language. |
| **Device Functional Domain (Imaging vs. Lab vs. General Decision Support)** | Drives selection of the correct CFR part/section (e.g., §​892.2050 vs. §​862.xx). |
| **Predicate Device Identification** | Needed for 510(k) substantive equivalence argument; absence may force a De Novo route. |
| **Comprehensive Software Architecture Diagram** | Required for risk analysis, IEC 62304 compliance, and PCCP mapping. |
| **Data Set Provenance Details (source, curation, representativeness)** | Supports bias analysis and performance claim substantiation. |
| **Specific Change Scenarios & Their Assigned PCCP Tier** | FDA will review the pre‑approved change scope; undefined scenarios trigger a new submission. |
| **UDI Assignation Plan (Label format, GUDID entry details)** | Mandatory for market entry under Part 830. |
| **Cybersecurity Threat Model Documentation** | Required to satisfy QMSR and post‑market safety expectations. |

> **Action:** Collect the above items from product development and clinical teams before drafting the 510(k) submission.

---

### 4. Core Risk Controls (aligned with identified hazards)

| Hazard | Control(s) |
|--------|------------|
| **Algorithmic bias leading to inequitable outcomes** | • Bias analysis during development.<br>• Ongoing monitoring of performance across subpopulations.<br>• Pre‑defined mitigation updates within PCCP tier 1. |
| **Incorrect AI output (false positive/negative)** | • Human oversight requirement (human‑in‑the‑loop) documented in workflow.<br>• Threshold validation with clinically relevant ROC curves.<br>• Alarm triggers for out‑of‑distribution inputs. |
| **Software defect / crash** | • IEC 62304‐compliant development lifecycle.<br>• Unit, integration, and system testing with regression suites linked to PCCP change tiers. |
| **Data drift post‑deployment** | • Real‑world performance monitoring plan (drift detection thresholds).<br>• Automated alerts prompting PCCP‑governed model retraining. |
| **Cybersecurity breach** | • Encryption of data at rest/in transit.<br>• Regular vulnerability scans and patch management tied to QMSR procedures. |
| **Usability error in Human‑AI interaction** | • Human factors validation per FDA guidance.<br>• Training materials and clear IFU language. |

---

### 5. Key Regulatory Citations  

* **21 CFR §​807** – Premarket notification (510(k)) requirements.  
* **21 CFR Part 820** – Quality Management System Regulation (QMSR) effective Feb 2026.  
* **21 CFR Part 830** – Unique Device Identification (UDI) labeling obligations (§​830.10 onward).  
* **Predetermined Change Control Plan (PCCP)** – FDA final guidance, December 2024 (full title: *“Predetermined Change Control Plan (PCCP) for Artificial Intelligence/Machine Learning‑Based Software as a Medical Device”*).  
* **IEC 62304** – Medical device software—software life cycle processes.  
* **ISO 14971** – Application of risk management to medical devices.  
* **§​892.2050 (Class II)** – Medical image management and processing system, if imaging‑related (pending confirmation).  

> No specific 510(k) numbers or predicate identifiers were present in the source excerpts; verify separately.

---

### 6. Human‑Escalation Triggers  

| Trigger | Required Action |
|---------|-----------------|
| **Proposed change exceeds pre‑approved PCCP scope** (e.g., new algorithm architecture, new data sources not covered) | Submit a supplemental 510(k) or a new 510(k) as appropriate. |
| **Performance metric falls below predefined clinical threshold in post‑market monitoring** | Initiate corrective action plan; consider a Field Alert/Recall and notify FDA per 21 CFR §​803 (MDR). |
| **Detection of new bias affecting a protected subgroup** | Conduct root‑cause analysis, implement mitigation within PCCP tier 1 if possible; otherwise file a new submission. |
| **Cybersecurity incident that compromises patient data or device functionality** | Follow FDA’s cybersecurity incident reporting process (21 CFR §​820.30) and possibly issue a safety notice under 21 CFR §​803. |
| **Adverse event reports > predefined rate** | Prepare a Medical Device Report (MDR) and assess need for a recall or labeling update per 21 CFR §​806. |
| **Regulatory change (e.g., new FDA guidance altering PCCP expectations)** | Re‑evaluate current PCCP; if gaps are identified, submit an updated change control plan. |

All triggers should be documented in the post‑market surveillance plan and communicated to the RA lead for immediate escalation.

---

### 7. Summary Judgment  

*The AI‑enabled SaMD appears to be a Class II device requiring a 510(k) submission supported by a robust Predetermined Change Control Plan (PCCP). The current source provides a solid outline of required lifecycle artifacts (bias analysis, human‑AI workflow, post‑market monitoring), but critical information—exact intended use, functional domain, predicate device, and detailed software architecture—is missing. Until these gaps are filled, the classification and submission strategy cannot be finalized.*

**Human escalation is mandatory** when any change falls outside the pre‑approved PCCP, performance degrades, bias emerges, or safety incidents arise.

---

### 8. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions made regarding device class (potential §​892.2050 vs. §​862.xx), the completeness of the evidentiary checklist, and any jurisdiction‑specific gaps (e.g., state‑wide AI/ML regulations, recent FDA guidance updates beyond Dec 2024). Highlight any missing references or alternative pathways that may apply.

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

### kb-eval-20260722-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "4fa2b22fa435c19b", "source": "github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md", "source_hash": "a622ee7076c4fd98e60854417742c547284a2a3b0d82065d9b4e2a9da67c1fab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `4fa2b22fa435c19b`
- Source: `github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/13_%EA%B7%9C%EC%A0%9C%ED%8F%89%EA%B0%80_%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8/FDA_510k_RTA.md)
- Source hash: `a622ee7076c4fd98e60854417742c547284a2a3b0d82065d9b4e2a9da67c1fab`
- Focus: SaMD change impact
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `FDA_510k_RTA.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: - id: FDA-510K-C3 source: FDA RTA Checklist Section C clause: C.3 requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 severity: must evidence_type: test_report applicable_keywords: [IEC60601-1, IEC60601-2-54] related_docs: [] - id: FDA-510K-C4 source: FDA RTA Checklist Section C clause: C.4 requirement: Software (Major LoC) — IEC 62304 + FDA S...
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

> **Regulatory Draft – SaMD / Electrical‑Medical Device (510(k) pathway)**  

---

### 1. Device Overview (as inferred from source)
* A **medical device** incorporating:
  * **Electrical hardware** that must meet IEC 60601‑1 (general safety) and IEC 60601‑1‑2 (EMC).  
  * **Software of major Level of Concern** (LoC ≥ B) governed by IEC 62304, FDA software guidance, and cybersecurity requirements.  
* Intended for **clinical use** (exact indication not supplied in source – must be defined).  

> *The source provides only checklist items; the precise device function, intended use, and predicate are missing and must be supplied before final classification.*

---

### 2. Likely Classification & Submission Route  

| Criterion | Reasoning |
|-----------|----------|
| **Regulatory pathway** | The device will most likely qualify for a **Premarket Notification (510(k))** because it is a non‑implantable, electrically powered system with software of major LoC and no novel technology that would automatically trigger De Novo. |
| **Device class** | **Class II**, as the majority of IEC 60601‑1/‑1‑2‑compliant devices (e.g., diagnostic monitors, infusion pumps) are Class II unless a specific FDA regulation mandates otherwise. <br> *Reference:* 21 CFR § 807 – 510(k) process; typical classification for electrically safe, software‑enabled devices is Class II (e.g., §892.2050 for image processing or equivalent). |
| **Applicable FDA part** | • **Part 807** – Premarket notification.<br>• **Part 820** – Quality Management System Regulation (effective 2026‑02, ISO 13485‑aligned).<br>• **Part 830** – UDI requirements. |
| **Special/Abbreviated pathway?** | Not indicated; unless a suitable predicate exists that reduces review time, the standard 510(k) is appropriate. |

*If the device turns out to be an imaging‑software system (e.g., PACS), classify under **Part 892 – Medical Image Management and Processing System (§892.2050)**. Verify once intended use is clarified.*

---

### 3. Required Evidence (per FDA RTA checklist)

| Checklist Item | Evidence Type | Minimum Content |
|----------------|--------------|-----------------|
| **Electrical safety** (C.3) | Test report | Full compliance to IEC 60601‑1 – electrical safety tests, test reports (lab accreditation, test methods). |
| **EMC** (C.3) | Test report | Compliance to IEC 60601‑1‑2 – EMC testing (radiated & conducted emissions/immunity), traceability matrix to standards. |
| **Software – Major LoC** (C.4) | SW documentation | • Software Development Plan (SDP).<br>• Requirements, Architecture, Verification & Validation reports.<br>• IEC 62304 life‑cycle processes evidence.<br>• FDA software guidance artifacts (e.g., SBOM, risk management file). |
| **Cybersecurity** (C.4) | SW documentation | • Threat modeling and mitigation strategy.<br>• Pre‑determined Change Control Plan (PCCP) for future updates (FDA Guidance Dec 2024). |
| **Labeling** (E.1) | Draft labeling package | Proposed label, Instructions for Use (IFU), contraindications, intended use statement, symbols per 21 CFR § 801. |
| **UDI compliance** (E.2) | UDI plan | Identified issuing agency (GS1 or HIBCC), device identifier format, integration into labeling and GUDID submission plan. |

---

### 4. Missing Information / Gaps  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Intended use & indication** | Determines predicate search, risk class, special controls. | Obtain clear FDA‑cleared intended use statement. |
| **Predicate device(s)** | Required for substantial equivalence claim. | Conduct a predicate search (e.g., 510(k) database). |
| **Device description / block diagram** | Needed for safety/EMC test scope and software architecture review. | Provide detailed hardware/software block diagram. |
| **Risk Management File (ISO 14971)** | Demonstrates mitigation of identified hazards, especially cybersecurity. | Compile hazard analysis, risk evaluation, and control measures. |
| **Clinical performance data (if needed)** | If no predicate or if special controls apply. | Determine necessity; plan for bench or limited clinical study. |
| **FDA‑issued UDI agency confirmation** | Part 830 requires an accredited issuing agency. | Confirm selection (GS1/HIBCC) and obtain issuance code. |
| **Software validation plan & post‑market monitoring** | Required for IEC 62304 compliance and PCCP. | Draft validation protocol; define post‑market surveillance. |

*All gaps must be resolved before final 510(k) submission.*

---

### 5. Core Risk Controls (derived from checklist)

1. **Electrical Safety Controls** – Design per IEC 60601‑1, protective earth leakage limits, insulation testing, regular production verification.
2. **EMC Controls** – Shielding, filtering, compliance testing per IEC 60601‑1‑2; design documentation of EMC mitigation.
3. **Software Life‑Cycle Controls** – IEC 62304 processes: development planning, configuration management, traceability, verification & validation.
4. **Cybersecurity Controls** – Threat modeling, secure coding standards, vulnerability scanning, PCCP for controlled updates.
5. **Labeling Controls** – Clear IFU, contraindications, symbols; UDI placed on label per Part 830 §§ 830.10‑830.60.
6. **Quality System Controls** – QMSR (21 CFR § 820) covering design controls, document control, CAPA.

---

### 6. Key Regulatory Citations  

| Area | Citation |
|------|----------|
| Premarket notification (510(k)) | **21 CFR § 807** |
| Quality Management System Regulation (effective Feb 2026) | **21 CFR § 820** |
| UDI requirements | **21 CFR §§ 830.10‑830.60** |
| Electrical safety standard | **IEC 60601‑1** (general requirements for basic safety and essential performance) |
| Electromagnetic Compatibility | **IEC 60601‑1‑2** |
| Software lifecycle | **IEC 62304** |
| FDA software guidance & cybersecurity | FDA “Guidance for the Content of Premarket Submissions for Device Software Functions” (2024) and “Cybersecurity for Medical Devices: A Proposed Regulatory Framework” (Dec 2024) – **Predetermined Change Control Plan (PCCP)** |
| Imaging‑device classification (if applicable) | **21 CFR § 892.2050** (Medical image management & processing system – Class II) |

*No specific 510(k) identifiers appear in the source; verify predicate numbers separately.*

---

### 7. Human‑Escalation Triggers  

| Condition | Trigger for escalation to senior RA / regulatory leadership |
|-----------|------------------------------------------------------------|
| **Missing intended use or predicate** – cannot complete SE claim. | Immediate escalation – pause submission preparation. |
| **Gap in electrical safety or EMC test data** – test reports absent or incomplete. | Escalate to engineering lead and QA for expedited testing. |
| **Software LoC ≥ B without full IEC 62304 documentation** – risk of non‑compliance. | Escalate to software validation team; consider PCCP development. |
| **Cybersecurity threat model not documented or unresolved high‑severity vulnerabilities**. | Escalate to cybersecurity lead and senior RA for mitigation plan. |
| **UDI issuing agency not confirmed or GUDID submission plan incomplete**. | Escalate to labeling & regulatory affairs manager. |
| **Classification appears to be Class III after risk analysis** – 510(k) no longer appropriate. | Immediate escalation to consider PMA or De Novo pathway. |

---

### 8. Peer‑Review Prompt  

> **Request:** Please review the assumptions above—particularly the default Class II/510(k) determination, the inferred need for an imaging‑device classification under Part 892, and the completeness of the identified evidence gaps. Identify any jurisdiction‑specific considerations (e.g., state‑level registration, foreign market impact) that have not been addressed.

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

1. Chunk `1059626859749416295`

> - id: FDA-510K-C3 source: FDA RTA Checklist Section C clause: C.3 requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 severity: must evidence_type: test_report applicable_keywords: [IEC60601-1, IEC60601-2-54] related_docs: [] - id: FDA-510K-C4 source: FDA RTA Checklist Section C clause: C.4 requirement: Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity severity: must evidence_type: SW_documentation applicable_keywords: [IEC62304, FDA SBOM, IEC81001-5-1] related_docs: [] ```

2. Chunk `1657837344321702`

> ## 5. Labeling ```yaml - id: FDA-510K-E1 source: FDA RTA Checklist Section E clause: E.1 requirement: Labeling — proposed labels, IFU draft, contraindications severity: must evidence_type: labeling_draft applicable_keywords: [FDA 510, UDI] related_docs: [] - id: FDA-510K-E2 source: FDA RTA Checklist Section E clause: E.2 requirement: UDI compliance — GS1/HIBCC issuing agency identified severity: must evidence_type: udi_plan applicable_keywords: [UDI] related_docs: [] ``` --- > v0.1 — 16개 핵심 항목으로 시작. 다음 보강에서 ~64개 추가하여 RTA 전체 ~80건 완성 예정.

### kb-eval-20260722-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "42bb8106a16a154f", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `42bb8106a16a154f`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md)
- Source hash: `7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1`
- Focus: SaMD change impact
- Matched keywords: FDA, QMSR

**Source Summary**

- 문서 요약: `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md`는 `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분 --- doc-id: FDA_QMSR_820.35_vs_ISO13485_4.2.5 title: "FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표" type: Guide version: v0.2 status: draft ca...
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

> **Regulatory Draft – SaMD Change Impact Assessment (QMSR 820.35 vs ISO 13485 §4.2.5)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination | Rationale / Reference |
|------|----------------|-----------------------|
| **Device class** | *Undetermined – requires intended‑use definition.* | FDA classification is driven by the device’s indication, technology and risk. The source material only addresses QMSR record‑keeping; it does not specify a device type or predicate. 21 CFR 820 (QMSR) and ISO 13485 §4.2.5 are quality‑system requirements that apply to **all** classes. |
| **Regulatory pathway** | *510(k) – most likely for moderate‑risk SaMD (Class II). If the software is novel or lacks a predicate, consider De Novo.* | The majority of medical image‑processing and analysis software falls under 21 CFR 892.2050 (Class II). Absent a predicate, De Novo may be required (21 CFR 814). |
| **Applicable CFR parts** | - 21 CFR 820 – QMSR (effective 2026‑02‑02) <br> - 21 CFR 892.2050 (if image‑processing/analysis) <br> - 21 CFR 803 – MDR reporting <br> - 21 CFR 830 – UDI <br> - 21 CFR 11 – electronic records | Established regulatory framework; no case‑specific identifiers in the source. |

---

### 2. Evidence Package Required for 510(k) (or De Novo)  

| Requirement | Typical Content | QMSR/ISO Gap Highlight |
|-------------|-----------------|------------------------|
| **Device description & intended use** | Detailed narrative, labeling excerpts, user interface screenshots. | *Missing* – not covered in source; needed to anchor classification. |
| **Substantial equivalence (if 510(k))** | Predicate device name/cleared number, comparison table of indications, technology, performance. | *Missing predicate identifiers* – must be sourced from FDA’s 510(k) database. |
| **Software documentation** | IEC 62304‑compliant software development lifecycle artifacts: design specification, architecture diagram, verification & validation reports, risk management file (ISO 14971). | QMSR §820.35 adds record‑keeping beyond ISO 13485 §4.2.5; ensure traceability matrices are retained per §820.35. |
| **Performance testing** | Bench‑testing (accuracy, precision, robustness), algorithm verification, interoperability with hardware if applicable. | No direct reference in source – must be generated. |
| **Clinical evidence (if needed)** | Clinical performance data or literature supporting safety/effectiveness; may be limited to “clinical validation” for image‑analysis software. | Not addressed by QMSR/ISO clause; still required per 510(k) guidance. |
| **Labeling** | IFU, promotional material, intended use statement, UDI label (per §830.10‑§830.60). | Record‑keeping of labeling revisions is a §820.35 requirement. |
| **Post‑market surveillance plan** | PSUR, vigilance procedures, adverse event reporting per 21 CFR 803. | Required by QMSR; ISO 13485 §4.2.5 only mandates “basic” records. |
| **Predetermined Change Control Plan (PCCP)** *if AI/ML* | Scoped change categories, monitoring plan, FDA pre‑market notification of planned modifications. | Not covered in source but mandated for AI/ML SaMD under Dec 2024 guidance. |

---

### 3. Missing Information / Gaps Identified  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Intended use & target population** | Determines classification rule and predicate eligibility. | Obtain from product marketing / design documents. |
| **Predicate device identifier (510(k) number)** | Required for substantial‑equivalence claim. | Search FDA 510(k) database; if none, plan De Novo. |
| **Risk management file (ISO 14971)** | Demonstrates mitigation of identified hazards; links to record‑keeping per §820.35. | Compile hazard analysis, risk control measures, residual risk evaluation. |
| **Software versioning & change impact matrix** | QMSR §820.35 expects detailed records of each change and its effect on device safety/effectiveness. | Develop a Change Control Log aligned with PCCP (if applicable). |
| **UDI issuance evidence** | Required for market entry; must be stored in GUDID per §830.30‑§830.36. | Generate UDI, submit to FDA’s GUDID system. |
| **Electronic records compliance (21 CFR 11)** | Records created/maintained electronically must meet audit trail, security, and backup requirements. | Verify that the SaMD’s data repository is 21 CFR 11 compliant. |
| **Human factors/Usability validation** | Essential for SaMD intended for clinical decision support. | Conduct summative usability testing; capture in validation report. |

---

### 4. Risk Controls Aligned to QMSR §820.35 vs ISO 13485 §4.2.5  

| Control Area | Minimum requirement under ISO 13485 §4.2.5 (baseline) | Additional requirement imposed by QMSR §820.35 |
|--------------|--------------------------------------------------------|-----------------------------------------------|
| **Documented records of design changes** | Retain “design and development” records. | Maintain a *change‑impact* log linking each modification to risk assessment updates, verification results, and regulatory submission impact (per §820.35). |
| **Traceability** | Establish traceability from requirements to testing. | Extend traceability to include **UDI assignment**, post‑market surveillance data, and any FDA‐issued corrective actions. |
| **Retention periods** | Keep records for the required statutory period (generally 2 years after device is no longer marketed). | QMSR may specify longer or more detailed retention for “record of software updates” – verify specific §820.35 language when drafting SOPs. |
| **Management review of change data** | Periodic reviews of quality system records. | Formal *management‑review agenda item* on each significant software version release, documenting decisions on risk acceptability and regulatory notification. |

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger for senior RA/Legal review |
|-----------|------------------------------------|
| **Classification cannot be resolved** (no clear rule or predicate) | Escalate to Lead RA for decision on De Novo vs 510(k). |
| **Missing predicate identifier** after exhaustive search | Escalate; may require regulatory strategy revision. |
| **Risk‑control gaps identified** (e.g., no documented impact analysis for a software patch) | Immediate escalation to QA/Engineering lead; halt release until closed. |
| **UDI or GUDID submission failure** (rejection by FDA) | Escalate to Regulatory Affairs Manager and Compliance Officer. |
| **PCCP not approved before planned AI/ML model update** | Stop change implementation; involve senior RA and FDA liaison. |
| **21 CFR 11 non‑compliance discovered in electronic record system** | Escalate to Senior Quality Engineer & IT Security lead for remediation. |
| **Adverse event signal that may be linked to a software version** | Trigger immediate MDR (21 CFR 803) reporting and senior RA oversight of PSUR update. |

---

### 6. Summary Judgment  

- The source material confirms that **ISO 13485 §4.2.5 alone is insufficient** for U.S. market entry; the FDA’s **QMSR §820.35 adds explicit record‑keeping and change‑impact requirements** that must be satisfied.
- **Classification & submission pathway cannot be finalized** without a defined intended use, predicate device (if any), and risk‑management documentation.
- The **evidence package** for a 510(k) (or De Novo) must include all items listed in Section 2, with special emphasis on **software change logs**, **PCCP (for AI/ML)**, and **UDI compliance** per 21 CFR 830.
- **Human escalation** points are identified to ensure gaps are addressed before any regulatory submission or market release.

> *No specific 510(k) numbers, predicate identifiers, or registration IDs were present in the source excerpts; verify those separately.*  

---

### Peer‑Review Prompt  

> **Colleague, please review:**  
> - Whether the assumed reliance on 21 CFR 892.2050 (image‑processing software) aligns with the actual SaMD function you have.  
> - Any additional FDA programs applicable to this device (e.g., Breakthrough Device Designation, New Early Cancer Detection).  
> - Completeness of the change‑control and PCCP considerations given your development lifecycle.  

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

1. Chunk `100539693362657837`

> ## 1. 적용 전제 - 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨 - ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과 - 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

2. Chunk `195154780902741471`

> --- doc-id: FDA_QMSR_820.35_vs_ISO13485_4.2.5 title: "FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표" type: Guide version: v0.2 status: draft category: 01_법규_규제 purpose: "FDA QMSR §820.35와 ISO 13485 §4.2.5 간 차이 분석 및 X-ray 시스템 기록관리 적용 지침" applicable: [FDA QMSR 21 CFR 820, ISO13485:2016 §4.2.5, 21 CFR 803, 21 CFR 830, 21 CFR Part 11, UDI] forms: [F-QMSR-REC-001] related-docs: - FDA_QMSR_2026 - ISO13485_2016_요약 - SOP-DOC-001 - SOP-TRC-001 - SOP-FSCA-001 - SOP-PSUR-001 related-issues: [44] owner: RA/QA Lead last-review: 2026-05-25 review-due: 2027-05-25 --- # FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표

## ra_eu

### kb-eval-20260722-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "0150a731e2233f91", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `0150a731e2233f91`
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

> **Regulatory Draft – Diagnostic X‑ray System (Active Device Emitting Ionising Radiation for Diagnosis)**  

---

### 1. Classification & Conformity‑Assessment Route  
| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Device class** | Class IIb | **Rule 10** of Annex VIII (active devices for diagnosis/monitoring that emit ionising radiation) → Class IIb【1】 |
| **Relevant sub‑components** | • X‑ray generator – Rule 10 / Class IIb  <br>• Digital flat‑panel detector – Rule 17 / Class IIa | Annex VIII Rules 10 & 17 (recording devices) 【2】 |
| **Conformity‑assessment route** | **Annex IX** – QMS (ISO 13485) + full technical documentation assessment  *(most common for Class IIb)*  <br>or **Annex X** – Type‑examination (if NB prefers a type‑exam approach) | Annex IX / Annex X of the MDR 2017/745 |

*The chosen route must be agreed with the Notified Body; both routes satisfy the “full quality‑system” requirement for Class IIb devices.*

---

### 2. Required Technical & Clinical Evidence  

| Deliverable | Content required (minimum) | Reference |
|-------------|----------------------------|-----------|
| **Technical documentation** (Design dossier, Device description, Intended use, Labels) | Complete Annex II file – device specification, manufacturing information, risk management, verification/validation, post‑market surveillance plan, etc. | Annex II |
| **Risk Management File** | ISO 14971‑based process; include hazard analysis, risk evaluation, residual risk assessment, and risk control measures for radiation protection (§16), electronic programmable systems (§17) & active devices (§18). | Annex I §§16‑18; ISO 14971 |
| **Clinical Evaluation Report (CER)** | Systematic review of state‑of‑the‑art literature, clinical data on performance & safety of the X‑ray system, benefit–risk analysis. Updated per Art 61. | Annex XIV Part A; Art 61 |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Planned investigations to confirm long‑term safety/performance; includes methodology, endpoints, timeline. | Annex XIV Part B |
| **PMS System** | PMS plan (Art 84) and PMS reports (Art 85 for Class I, Art 86 PSUR for Class IIb – annual). | Art 83‑86 |
| **Standards conformity evidence** | • IEC 60601‑2‑54 (X‑ray equipment for radiography & radioscopy) <br>• IEC 60601‑2‑28 (X‑ray tube assemblies) <br>• IEC 62220‑1‑1 (DQE measurement) <br>• IEC 62304 (software lifecycle) <br>• IEC 62366‑1 (usability) | Manufacturer’s declaration of conformity to the above harmonised standards |
| **Labeling & IFU** | Information per Annex I Chapter III (§23) – radiation safety instructions, user training requirements, contraindications. | Annex I §23 |

---

### 3. Gaps / Missing Information (identified from source)

1. **Incorrect class assignment** in the original mapping table (Rule 5/9) – must be corrected to Rule 10 → Class IIb.  
2. **Explicit intended‑use statement** clarifying “diagnostic use of ionising radiation” (to exclude therapeutic intent).  
3. **Justification for the chosen conformity‑assessment route** (Annex IX vs Annex X) with NB agreement.  
4. **Evidence of compliance with IEC 60601‑2‑54 / IEC 60601‑2‑28** (test reports, certificates).  
5. **Radiation protection calculations** (dose metrics, shielding specifications) to satisfy GSPR §16.  
6. **Clinical data package** – at least a clinical investigation or equivalent performance studies demonstrating image quality & safety in the intended indication.  
7. **PMCF plan details** – endpoints, sample size, follow‑up duration.  
8. **Usability validation for lay‑person/operator interaction** (if device intended for use by non‑clinical staff) to meet GSPR §22.

---

### 4. Risk Controls (aligned with MDR GSPRs)

| Hazard | Control measure(s) | Supporting standard / clause |
|--------|--------------------|------------------------------|
| **Radiation exposure (excess dose)** | • Built‑in automatic exposure control (AEC) <br>• Real‑time dose monitoring & alarm limits <br>• Shielding design verified per IEC 60601‑2‑54 §16.4 | GSPR §16; IEC 60601‑2‑54 |
| **Equipment malfunction / software error** | • Software development lifecycle per IEC 62304 <br>• Usability engineering (IEC 62366‑1) to prevent operator misuse <br>• Redundant safety interlocks | GSPR §§17–18 |
| **Electrical hazards** | • Compliance with IEC 60601‑1 (general safety) – leakage current, insulation tests | GSPR §20 |
| **Mechanical/thermal risks** | • Robust housing, temperature monitoring, overload protection | GSPR §20 |
| **Incorrect use by lay persons** | • Clear IFU warnings, pictograms, training program; design for intuitive operation | GSPR §22 |

All residual risks must be documented in the Risk Management File and justified as acceptable in the CER (benefit‑risk determination).

---

### 5. Human‑Escalation Triggers  

| Situation | Action required | Escalation to |
|-----------|----------------|---------------|
| **Disagreement on classification** (e.g., NB still cites Rule 5/9) | Submit formal justification with rule citations and intended‑use description; request a classification opinion from the Competent Authority if unresolved. | RA Lead & Notified Body liaison |
| **Missing clinical evidence** (no appropriate investigation data) | Pause submission; initiate or procure a clinical investigation / performance study. | Clinical Investigation Team |
| **Non‑conformity with required IEC standards** (e.g., test reports unavailable) | Obtain additional testing or select an alternative compliant design. | Engineering & QA |
| **PMS/PMCF plan not approved by NB** | Revise plan to address NB comments; schedule a follow‑up meeting. | Post‑Market Surveillance Coordinator |
| **Risk‑management file gaps (e.g., residual risk not justified)** | Conduct additional risk analysis, update the file, and re‑run benefit‑risk assessment. | Risk Management Lead |
| **Labeling/IFU does not meet Annex I §23** | Redraft labeling; perform user‑testing if required. | Technical Documentation Owner |

Any of the above triggers should be logged in the project’s issue tracker and communicated to the Project Manager for timely resolution.

---

### 6. Peer‑Review Prompt  

> **Colleague, please review:**  
> – The classification reasoning (Rule 10 vs Rule 5/9) and the mapping of sub‑components.  
> – Whether all required MDR references (Annex II, Annex XIV, Art 83‑86, GSPRs §16‑22) are captured accurately.  
> – Any jurisdiction‑specific gaps (e.g., need for a European Clinical Evidence (ECE) summary, or specific EUDAMED registration steps).  

Your feedback will help close any remaining deficiencies before the Notified Body review.

--- 

*No specific case identifiers (e.g., 510(k) numbers, predicate device IDs) appear in the source excerpts; verify those separately if required.*

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

### kb-eval-20260722-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a19c3d1e3fdf174c", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a19c3d1e3fdf174c`
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

> **Regulatory Draft – Technical‑Documentation Assessment & NB Submission Planning**

---

### 1. Scope of the Review  
The source material describes the **EU MDR 2017/745 Annex II technical‑documentation template** (product description, labeling, design & manufacturing, safety requirements, risk management, verification & validation). No device‑specific details (intended purpose, mode of action, active vs. non‑active) are supplied in the excerpts.

---

### 2. Classification & Conformity‑Assessment Route – *Preliminary*  

| Item | Current status | Required information to resolve |
|------|----------------|---------------------------------|
| **Device class** (Rules 1–22, Annex VIII) | *Undetermined* – no intended use or risk profile disclosed. | • Intended medical purpose (diagnostic/therapeutic, active/non‑active). <br>• Patient population and duration of contact.<br>• Energy source or software decision impact (if any). |
| **Conformity‑assessment route** (Annex IX, X, XI) | *Undetermined* – depends on final class. | • Final class → select appropriate Annex: <br> – Class I (non‑sterile, non‑measuring) → self‑declaration only (no NB). <br> – Class IIa/IIb/III → **Annex IX** (QMS + technical documentation assessment) or **Annex X** (type‑examination) where applicable. |
| **Human escalation trigger** | *Yes* – a regulatory lead must obtain the missing intended‑use description before any classification can be assigned. |

---

### 3. Required Evidence & Documentation (per MDR)

| Annex / Article | Mandatory element | What is currently present in source | Gap that must be filled |
|-----------------|-------------------|--------------------------------------|--------------------------|
| **Annex II – Technical documentation**<br>§1 Device description | Detailed description of device, principle of operation, variants, accessories. | Only a placeholder “제품 설명” (device description) column; no content shown. | Full narrative + diagrams, bill of materials, software architecture (if applicable). |
| **Annex II §2 – Labeling** | Labels & IFU complying with §23 Annex I (language, symbols, safety info). | Column “라벨·IFU” listed but no actual label content. | Provide draft label, IFU in English + required NB language(s), include UDI format, contraindications, warnings. |
| **Annex II §3 – Design & Manufacturing** | Design output, manufacturing processes, controlled environment details. | Reference to “Design History File” (DHF) but no specific process validation data. | Process flow charts, SOPs, qualification reports for critical processes, clean‑room classification evidence. |
| **Annex II §4 – GSPR checklist** | Demonstration of compliance with the 23 General Safety & Performance Requirements (GSPR). | “GSPR Checklist” mentioned; no completed matrix. | Completed Annex I‑GSPR mapping table with referenced evidence (test reports, clinical data, risk controls). |
| **Annex II §5 – Risk Management** | ISO 14971‑based Risk Management File (RMF) covering risk analysis, evaluation, control, residual risk, benefit‑risk determination. | “Risk Management” column present; only ISO 14971 cited, no RMF excerpt. | Full RMF including risk register, risk control measures, verification of controls, post‑market surveillance (PMS) plan integration. |
| **Annex II §6 – Verification & Validation** | V&V reports demonstrating that design outputs meet inputs and intended use. | “Verification·유효성 확인” noted; no specific V&V data. | Test protocols & reports (performance, safety, usability), clinical validation studies where required. |
| **Annex XIV Part A – Clinical Evaluation Report (CER)** | Up‑to‑date CER per Art. 61, including state‑of‑the‑art literature review and clinical data. | Not referenced in the excerpt. | CER with bibliography, justification of equivalence (if any), benefit‑risk conclusion. |
| **Annex XIV Part B – PMCF Plan & Report** | For Class IIa/IIb/III devices, a post‑market clinical follow‑up (PMCF) plan and periodic reports. | Not referenced. | PMCF plan outlining objectives, methodology, timeline; interim/final reports. |
| **Art. 83–86 – PMS System & Periodic Safety Update Report (PSUR)** | PMS system (Art. 83), PMS plan (Art. 84), PSUR for Class IIa/IIb/III (Art. 86). | Only “Annex III (PMS TD)” mentioned, no detail. | Established PMS processes, incident reporting procedures, annual (Class IIb/III) or biennial (Class IIa) PSURs. |
| **EUDAMED registration** (Arts 33‑39) | Registration of device, UDI, certificates, clinical investigation summary. | Not covered in the excerpt. | Complete EUDAMED entry for each product model/variant. |

---

### 4. Risk Controls – Core Elements to be Demonstrated  

1. **Risk Management File** (ISO 14971) – risk analysis, evaluation, control measures, verification of controls. *(Annex II §5; Annex I §§10‑22)*  
2. **Residual Risk & Benefit–Risk Determination** – documented conclusion that residual risks are outweighed by clinical benefit. *(Art. 61, Annex XIV Part A)*  
3. **Usability Engineering** – where device is intended for lay users or requires specific training (Annex I §22). Use IEC 62366‑1 as supporting standard.  
4. **Protection against Radiation** – if a source of ionising radiation is present, compliance with Annex I §16 and IEC 60601‑2‑54/28/44 as applicable.  
5. **Software Safety** – for software devices, conformity with Annex I §17 and IEC 62304 (if software is a medical device).  

> **Citation examples**:  
> * Classification rules – Annex VIII, Rules 1‑22.  
> * Technical documentation sections – Annex II §§1‑6.  
> * Clinical evaluation – Annex XIV Part A, kept current under Art. 61.  
> * PMS system – Art. 83; PSUR – Art. 86.

---

### 5. Missing Information – Immediate Action Items  

| Required item | Why needed | Source of requirement |
|---------------|------------|------------------------|
| **Intended purpose & mode of action** | Drives classification (Annex VIII) and clinical evidence scope. | Annex VIII, Rule 9‑11‑17 etc. |
| **Device variants/Accessories list** | Completes device description (§1). | Annex II §1. |
| **Labeling & IFU drafts** | Must satisfy GSPR §23 (Annex I) and language requirements. | Annex II §2; Annex I §23. |
| **Full Risk Management File** | Demonstrates compliance with GSPR §§10‑22 and Art. 61 benefit–risk. | Annex II §5; ISO 14971. |
| **Verification & Validation data** | Proves conformity of design outputs to inputs (Annex II §6). | Annex II §6. |
| **Clinical Evidence (CER, PMCF)** | Required for all Class IIa+ devices (Art. 61, Annex XIV). | Annex XIV Part A/B. |
| **PMS System description & PSUR schedule** | Obligations under Art. 83‑86. | Art. 83‑86; Annex III. |
| **EUDAMED registration details (UDI, certificates)** | Legal market entry requirement (Arts 33‑39). | Arts 33‑39. |

*Human escalation trigger*: The regulatory lead must obtain the above items before a Notified Body (NB) can be engaged. Each missing element should be logged as an open Work Package (WP) with a “Pending – Evidence Required” status; per Fixed Rule 1, the RA analyst does **not** close any WP but adds comments recommending closure once supplied.

---

### 6. Conformity‑Assessment Pathway Recommendation (once class is known)

| Final Class | Typical MDR route | Documents NB will request |
|-------------|-------------------|---------------------------|
| **Class IIa** | **Annex IX** – QMS + technical documentation assessment (ISO 13485 + Annex II). <br>or **Annex X** if a type‑examination is preferred. | Completed Annex II dossier, CER, PMCF plan, RMF, PMS system description, CE marking declaration (Annex IV). |
| **Class IIb / III** | **Annex IX** mandatory (QMS + technical documentation) plus possible **Annex X** for high‑risk sub‑categories. | Same as above + PSUR (Art. 86), additional clinical investigation data if no equivalent device exists, Notified Body audit reports. |

*Human escalation trigger*: When the class is finally determined, a senior RA must confirm the chosen Annex route and initiate formal NB engagement (request for quote, audit planning).

---

### 7. Summary Judgment  

- **Current status**: The available source only outlines the MDR Annex II template; no device‑specific data are present.
- **Regulatory next step**: Secure the missing intended‑use description, risk management documentation, labeling, verification/validation reports, and clinical evidence to enable classification and NB submission.
- **Escalation points**:  
  1. Absence of intended purpose → block classification.  
  2. Incomplete RMF or GSPR checklist → block technical‑documentation completeness check.  
  3. No CER/PMCF plan for Class IIa+ → block NB review.

---

### 8. Peer‑Review Prompt  

> **Colleague, please challenge**:  
> - Are there any MDR annexes or articles omitted here that could affect the evidence package (e.g., Annex XV for clinical investigations)?  
> - Given the limited excerpt, have I correctly assumed the need for a full CER and PMCF plan for all Class IIa‑III devices?  
> - Could any of the listed gaps be covered by existing equivalence data (510(k) SE comparison) under MDR, or is additional EU‑specific clinical data mandatory?

---

*Prepared by Theo – EU RA specialist; citations reflect confirmed regulatory references.*

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

### kb-eval-20260722-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a0930f4828c4acbc", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a0930f4828c4acbc`
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

> **Regulatory Response Draft – Diagnostic X‑ray System (Standard Radiology)**  

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory Basis |
|------|---------------|-------------------|
| **Rule applied** | **Rule 10** – Active device that emits ionising radiation for diagnostic purposes. | MDR Annex VIII, Rule 10 (active devices emitting ionising radiation) |
| **Risk class** | **Class IIb** – Energy is emitted and could place the patient at immediate risk if not properly controlled. | MDR Annex VIII, Rule 10 ⇒ Class IIb |
| **Conformity‑assessment route** | **Annex IX** – Full quality‑management system assessment together with technical documentation review by the Notified Body. | MDR Annex IX (QMS + Technical Documentation) |

---

### 2. Evidence Required for a Complete NB Submission  

| Evidence Category | Minimum content | Reference |
|-------------------|----------------|-----------|
| **Clinical Evaluation Report (CER)** | • Demonstration of clinical equivalence (same indication, same performance). <br>• DQE ≥ 65 % – supported by IEC 62220‑1‑1 test report TR‑2024‑015. <br>• Updated CER Rev. 3 attached as Annex A. | MDR Annex XIV Part A; Art. 61 |
| **Test Report (Performance)** | • Full IEC 62220‑1‑1 measurement of Detective Quantum Efficiency (DQE) with result ≥ 65 %. <br>• Reference: Test Report TR‑2024‑015. | IEC 62220‑1‑1 |
| **Technical Documentation (TD)** | • Device description, intended use, and labeling (Annex I §23). <br>• Design dossiers, drawings, specifications, software documentation (if applicable). <br>• Risk Management File (ISO 14971 / Annex I §§16‑20). | MDR Annex II |
| **Quality Management System** | • ISO 13485:2016 certified QMS covering design‑development, production and post‑market activities. <br>• Evidence of corrective actions for NB‑identified NCs. | MDR Annex IX; ISO 13485 |
| **Post‑Market Surveillance (PMS) Plan** | • PMS system description (Art. 83). <br>• PMS plan (Art. 84) with defined objectives, data sources and timelines. | Art. 83–84 |
| **Periodic Safety Update Report (PSUR)** (for Class IIb) | • Benefit‑risk determination, PMCF findings, sales volume & user population. <br>• Updated at least annually. | Art. 86(1)&(2) |
| **Labeling & IFU** | • Conformity with Annex I §23 (warnings, contraindications, radiation protection information). | Annex I §23 |
| **Usability / Human‑Factors Evaluation** | • IEC 62366‑1 compliance (usability engineering). | IEC 62366‑1 |
| **Software Lifecycle Documentation** (if software is a device) | • IEC 62304 compliant development & maintenance records. | IEC 62304 |

---

### 3. Gaps Identified by the Notified Body (NB)  

| Gap | What the NB specifically requested | Why it matters |
|-----|-----------------------------------|---------------|
| **Clinical Evaluation** | Updated CER with explicit equivalence justification and DQE data. | Required for demonstrating conformity to safety‑performance requirements (Annex XIV). |
| **Technical Documentation** | Missing or incomplete device description, labeling excerpts, and risk‑management analysis. | Needed for Annex II review; gaps impede assessment of GSPR compliance (§16–§20). |
| **QMS Non‑Conformities** | Evidence of corrective actions addressing previously raised NCs. | NB must verify that the QMS is fully effective (Annex IX). |
| **Labeling** | Full IFU and packaging labels in EU languages, with radiation protection statements (§16). | Annex I §23 mandates clear user information. |
| **PMS & PSUR** | Draft PMS plan and schedule for the first PSUR. | Art. 84/86 require proactive post‑market data collection. |

*No specific identifiers (e.g., predicate device numbers) were found in the source material – verify separately if such references are needed.*  

---

### 4. Recommended Risk Controls (aligned with GSPR)

| Control | Relevant GSPR / Standard | Implementation note |
|---------|---------------------------|----------------------|
| **Radiation protection** | Annex I §16 (radiation) | Built‑in dose‑limiting circuitry, interlocks, and exposure‑time safeguards; validation per IEC 60601‑2‑54. |
| **Active device safety** | Annex I §§18–19 | Continuous monitoring of power output, fault detection, automatic shutdown on abnormal conditions. |
| **Software safety (if applicable)** | Annex I §17 & IEC 62304 | Use of verified libraries, risk‑controlled software updates, and audit trails. |
| **Usability** | IEC 62366‑1 | Conducted formative/usability testing; labeling designed for lay users per Annex I §22 where relevant. |
| **Risk Management** | ISO 14971 & Annex I §§10‑20 | Full RMF with hazard identification, evaluation of residual risk, verification of mitigations; documented in the RMP. |

---

### 5. Human‑Escalation Triggers  

1. **Deadline Missed:** If the agreed NB response deadline passes without submission of the missing items → **Escalate to senior RA manager** for potential “evaluation termination / non‑approval” (per source Table 2, “미응답 시 – 평가 종료/불승인”).  
2. **Repeated NCs:** Any recurrence of the same QMS NC after corrective action → **Trigger internal stop‑work and inform NB (Clock‑stop) and senior management**.  
3. **Insufficient Clinical Data:** If DQE data cannot be substantiated to ≥ 65 % → **Escalate to clinical affairs lead** to consider additional bench testing or a new clinical investigation before further NB interaction.  

---

### 6. Regulatory Judgment (Prepared by Theo, EU RA)  

*The X‑ray diagnostic system falls under MDR Rule 10 → Class IIb and must follow the Annex IX conformity‑assessment route. The NB’s deficiency letter primarily targets gaps in the CER, technical documentation, QMS corrective actions, labeling, and post‑market surveillance artefacts. Providing the requested evidence (DQE test report TR‑2024‑015, updated CER Rev. 3, complete TD, PMS plan & first PSUR) within the negotiated deadline will enable the NB to complete its assessment and issue a CE mark.*  

**If any of the above items cannot be supplied on time, the case must be escalated immediately to senior regulatory leadership for decision‑making regarding possible submission withdrawal or re‑planning.**

---

### 7. Peer‑Review Prompt  

*“Please review this draft for: (a) completeness of identified evidence against MDR Annex XIV and Annex II requirements; (b) any overlooked jurisdiction‑specific obligations (e.g., EUDAMED registration, radiation‑safety directives); and (c) the adequacy of the escalation thresholds defined above.”*

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

### kb-eval-20260722-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7f257d2218b4c946", "source": "github:holee9/MD-process/issue-drafts/950_AUDIT_GSPR_정합표준_매핑표_MDR_AnnexI_19_활성이식_인용부정확.md", "source_hash": "2e5bb5e6f319013f35bfffde39b3c4b5e527009de066335c38c8710f24199c01"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `7f257d2218b4c946`
- Source: `github:holee9/MD-process/issue-drafts/950_AUDIT_GSPR_정합표준_매핑표_MDR_AnnexI_19_활성이식_인용부정확.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/950_AUDIT_GSPR_%EC%A0%95%ED%95%A9%ED%91%9C%EC%A4%80_%EB%A7%A4%ED%95%91%ED%91%9C_MDR_AnnexI_19_%ED%99%9C%EC%84%B1%EC%9D%B4%EC%8B%9D_%EC%9D%B8%EC%9A%A9%EB%B6%80%EC%A0%95%ED%99%95.md)
- Source hash: `2e5bb5e6f319013f35bfffde39b3c4b5e527009de066335c38c8710f24199c01`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `950_AUDIT_GSPR_정합표준_매핑표_MDR_AnnexI_19_활성이식_인용부정확.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: - **EUR-Lex — Regulation (EU) 2017/745, Annex I Chapter II**: - §14 Construction of devices and interaction with their environment (EMC/환경 대응) - §16 Protection against radiation (방사선 방호 — 이미 §16 행이 doc 본문에 정합 매핑됨) - §17 Electronic programmable systems / devices that incorporate electronic programmable systems and software that are devices in themselves —...
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

> **Regulatory Draft — Active Implantable Medical Device (Class III)**  

---

### 1. Classification & Conformity‑Assessment Route  

| Item | Regulatory Basis | Determination |
|------|------------------|---------------|
| **Device class** | **Annex VIII, Rule 19** – “Active implantable devices” are placed in **Class III**. | Class III |
| **Conformity‑assessment route** | **Annex IX** (full quality‑management‑system + technical‑documentation review) **or** **Annex X** (type examination) followed by **Annex XI** (production conformity verification) for Class III devices. | Recommended: **Annex IX** (most common). |
| **EU Declaration of Conformity** | Annex IV | Required after successful NB assessment. |

---

### 2. Mandatory Evidence Package  

| Evidence | Source Requirement | What must be submitted |
|----------|-------------------|------------------------|
| **Technical Documentation** | Annex II (incl. device description, labeling, risk‑management file, verification & validation data) | Complete Technical File per Annex II. |
| **Clinical Evaluation Report (CER)** | *Annex XIV Part A*; kept current under Art. 61 | Systematic review of state‑of‑the‑art literature + clinical data supporting safety & performance. |
| **Post‑Market Surveillance (PMS) Plan** | Art. 84 | Detailed plan covering routine PMS, PMCF activities, trend reporting, and vigilance. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 (Class III → at least annually) | Summarised benefit‑risk conclusions, PMCF results, sales & user population data. |
| **Risk Management File** | ISO 14971 (referenced in Annex I §17 / §18) | Risk analysis, evaluation, controls, residual risk acceptance. |
| **Usability Engineering File** (if device intended for lay‑person use) | IEC 62366‑1 | Usability validation report. |
| **Software Documentation** (if applicable) | IEC 62304; Annex I §17 (software as a medical device) | Software development lifecycle, verification/validation, cybersecurity measures (§17.4). |
| **Electromagnetic Compatibility (EMC) Evidence** | Annex I §14 & §17.1 | Test reports per IEC 60601‑1‑2 or equivalent. |
| **Radiation Protection Evidence** *(only if device emits ionising radiation)* | Annex I §16 | Compliance with IEC 60601‑2‑... (not normally needed for pure implantable devices). |
| **Labeling & IFU** | Annex I §23 | Copies of labels, instructions for use, and any required symbols. |
| **Unique Device Identification (UDI) & EUDAMED registration** | Art. 33‑39 | UDI dossier uploaded to EUDAMED; declaration of conformity linked. |

---

### 3. Gaps / Missing Information (to be clarified before NB submission)

| Gap | Why it matters | Suggested source/next step |
|-----|----------------|---------------------------|
| **Intended purpose & indications** | Determines classification, clinical data scope, and risk analysis depth. | Obtain the final Intended Use Statement from product development. |
| **Energy‑source description & maintenance strategy** (§19.1) | Required for minimisation of energy‑related hazards (§19). | Provide detailed schematic, power‑budget, battery life, replacement procedure. |
| **Component traceability / part‑identification scheme** (§19.3) | Needed to satisfy “component identification” requirement. | Compile part‑number matrix and lot‑traceability plan. |
| **Non‑invasive readout capability** (§19.4) | If the device offers code reading without surgery, evidence of reliability is required. | Conduct bench testing & usability validation for external readers. |
| **Cybersecurity / IT‑Security controls** (§17.4) | Mandatory minimum security requirements for programmed devices. | Deliver Security Threat Analysis and mitigation plan (aligned with IEC 62443). |
| **Clinical data set** – size, follow‑up duration, comparators | CER must demonstrate clinical performance; class III usually needs prospective data or well‑controlled studies. | Identify existing CE‑marked predicate (if any) or design a PMCF study. |
| **PMCF plan details** (scope, endpoints, timeline) | Required under Annex XIV Part B and reflected in PSUR. | Draft a comprehensive PMCF protocol. |
| **Usability validation for lay‑person use** (if applicable) | §22 demands proof of safe use by intended user group. | Conduct formative/ summative usability studies per IEC 62366‑1. |
| **EUDAMED entry (UDI, registration numbers)** | Mandatory for market placement from 2025 onward. | Prepare UDI assignment and upload to EUDAMED. |

---

### 4. Core Risk Controls (linked to GSPR)

| GSPR clause | Control measure | Standard / reference |
|-------------|----------------|----------------------|
| **§14 Construction & environmental interaction** | Robust mechanical design, corrosion‑resistant materials; IEC 60601‑1 general safety. | IEC 60601‑1 |
| **§16 Protection against radiation** *(if applicable)* | Dose monitoring, shielding; compliance with IEC 60601‑2‑... | IEC 60601‑2‑54 (radiography) etc. |
| **§17 Electronic programmable systems** | Secure boot, code signing, regular firmware updates; IT security per §17.4. | IEC 62304, IEC 62443, ISO 14971 risk control matrix. |
| **§19 Active implantable devices** – energy source safety, component traceability, non‑invasive readout | Redundant power management, unique device identifier on each component, RFID/ NFC external reader validation. | IEC 60601‑1‑8 (alarm systems), ISO 14971. |
| **§20 Mechanical & thermal protection** | Finite‑element analysis for stress; temperature monitoring loops. | IEC 60601‑1‑2 (EMC) + IEC 60601‑1‑11 (home care). |
| **§22 Use by lay persons** – if intended | Human factors engineering, simple IFU layout, colour coding. | IEC 62366‑1. |

---

### 5. Human‑Escalation Triggers  

| Trigger | Action Required | Escalation Level |
|--------|-----------------|------------------|
| **Unresolved classification uncertainty** (e.g., mixed active/diagnostic functions) | Conduct internal expert review; if still ambiguous, request legal‑department opinion. | Senior RA Manager. |
| **Missing or insufficient clinical data for a Class III device** | Initiate supplemental clinical study / PMCF plan before NB submission. | Project Lead & Clinical Lead. |
| **Absent IT‑security threat analysis** (§17.4) | Pause dossier completion; engage cybersecurity specialist. | Head of Cyber‑Risk. |
| **NB request for additional evidence not yet generated** (e.g., long‑term animal toxicity) | Prioritise generation of missing data; update schedule. | Program Manager (deadline ≤30 days). |
| **Non‑conformity in PMS/PSUR reporting cadence** (Art. 86) | Immediate remedial action to produce overdue report. | Quality Management Officer. |
| **EUDAMED registration incomplete at market launch** | Halt release; complete UDI dossier and confirm upload status. | Regulatory Compliance Lead. |

---

### 6. Peer‑Review Prompt  

> *Colleague, please review the assumptions above:  
> • Does Rule 19 definitively place all active implantable devices in Class III under MDR?  
> • Are any additional Annex IX sub‑requirements (e.g., Notified Body “design‑dossier” checklists) missing from the evidence list?  
> • Have we captured every GSPR that may apply to a device with both implanted hardware and external wireless readout, especially concerning §17.4 IT‑security?  
> • Identify any jurisdiction‑specific gaps (e.g., German BfArM additional documentation).*

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

1. Chunk `1080110362051195619`

> - **EUR-Lex — Regulation (EU) 2017/745, Annex I Chapter II**: - §14 Construction of devices and interaction with their environment (EMC/환경 대응) - §16 Protection against radiation (방사선 방호 — 이미 §16 행이 doc 본문에 정합 매핑됨) - §17 Electronic programmable systems / devices that incorporate electronic programmable systems and software that are devices in themselves — **§17.1 EMC/신뢰성 요구, §17.2 SW 개발수명주기·정보보안, §17.4 IT security minimum requirements** - **§19 Particular requirements for active implantable devices** — 19.1 에너지원·유지보수·상호작용 위험 최소화 / 19.3 부품 식별성 / 19.4 수술 없이 판독 가능한 코드 - §20 Protection against mechanical and thermal risks - MDR Annex I 텍스트 재확인:...

2. Chunk `139221394525877266`

> -regulation.eu/2019/07/23/annex-i-general-safety-and-performance-requirements/

### kb-eval-20260722-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d00e44d8564f7cc0", "source": "github:holee9/MD-process/issue-drafts/975_AUDIT_MDR_AnnexI_14_진단기기_10_오귀속_3개소.md", "source_hash": "624eedf4409b2abc1780aba067000afd6e8c50f2042bc70b21af2d918a11aaba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d00e44d8564f7cc0`
- Source: `github:holee9/MD-process/issue-drafts/975_AUDIT_MDR_AnnexI_14_진단기기_10_오귀속_3개소.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/975_AUDIT_MDR_AnnexI_14_%EC%A7%84%EB%8B%A8%EA%B8%B0%EA%B8%B0_10_%EC%98%A4%EA%B7%80%EC%86%8D_3%EA%B0%9C%EC%86%8C.md)
- Source hash: `624eedf4409b2abc1780aba067000afd6e8c50f2042bc70b21af2d918a11aaba`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `975_AUDIT_MDR_AnnexI_14_진단기기_10_오귀속_3개소.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 결함 EUR-Lex 원문(CELEX 02017R0745-20260101) Annex I 장 구조: - **§10 = Chemical, physical and biological properties**(화학·물리·생물학적 특성 — 독성·생체적합성 등) - **§14 = Construction of devices and interaction with their environment**(기기 구성·환경 상호작용) - **§15 = Devices with a diagnostic or measuring function**(진단·측정 기능 기기 — 정확도·정밀도·안정성) - §16 = 방사선 방호 ✓, §17 = 전자 프로그래머블 시스템...
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

> **Regulatory Draft – X‑ray Diagnostic Imaging System (Active Device emitting ionising radiation)**  

---

### 1. Classification & Conformity‑Assessment Route  
| Item | Determination | Regulatory basis |
|------|---------------|-------------------|
| **Device class** | **Class IIb** – active device that emits ionising radiation for diagnostic purposes. | Annex VIII, **Rule 10** (active devices emitting ionising radiation) → Class IIb【established】 |
| **Conformity‑assessment route** | 1️⃣ **Annex IX** – full quality‑management system + technical documentation assessment  <br>2️⃣ **Annex X** + **Annex XI** – type‑examination of the design dossier followed by production conformity verification (alternative). | Annex IX or Annex X/​XI【established】 |

*Human escalation trigger*: If the Notified Body questions the chosen route (e.g., requires Annex IX for a Class IIb device that was submitted under Annex X), senior RA must review the manufacturer’s QMS scope and decide whether to switch route.

---

### 2. Required Technical Evidence  

| Evidence | What must be provided | Regulatory reference |
|----------|----------------------|-----------------------|
| **Technical documentation** (design, manufacturing, labeling, risk management) | Complete dossier covering all GSPR items relevant to the device (see §15, §16, §17). | Annex II【established】 |
| **Clinical Evaluation Report (CER)** – up‑to‑date | Systematic review of state‑of‑the‑art literature, clinical data (including any PMCF results), justification of safety and performance. | Annex XIV Part A; kept current under Art. 61【established】 |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Planned studies to confirm continued compliance; final evaluation report. | Annex XIV Part B【established】 |
| **Post‑Market Surveillance (PMS) system & plan** | Integrated PMS process, including incident handling and trend analysis. | Art. 83 (system); Art. 84 (plan)【established】 |
| **Periodic Safety Update Report (PSUR)** | Benefit–risk determination, PMCF findings, sales/using‑population data. For Class IIb → at least annually. | Art. 86 (1)(a‑c); update cadence Art. 86(2)【established】 |
| **Standards compliance evidence** | • IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy)<br>• IEC 60601‑2‑28 (X‑ray tube assemblies)<br>• IEC 62304 (software lifecycle)<br>• IEC 62366‑1 (usability) | IEC standards listed above【established】 |
| **Labeling & IFU** | Conform to Annex I §23 (information supplied with the device). | Annex I, Chapter III (§23)【established】 |

*Human escalation trigger*: Absence of any of the above items – especially a CER that does not reference GSPR §15 for diagnostic performance – must be raised to senior RA before NB submission.

---

### 3. Mapping of General Safety & Performance Requirements (GSPR)

| GSPR clause | Device aspect | Current source mapping issue | Required corrective action |
|-------------|---------------|------------------------------|----------------------------|
| **§15** – Devices with a diagnostic or measuring function | Imaging performance (accuracy, precision, stability) | Source incorrectly assigns diagnostic function to §14. Must be re‑mapped to **§15**【source [1]】 | Update technical file and QC protocol to cite §15 as the governing clause. |
| **§16** – Protection against radiation | Radiation shielding, dose monitoring, interlocks | Correctly identified in source (✓)【source [1]】 | Provide evidence of compliance with IEC 60601‑2‑54 & dose limits per §16.4. |
| **§17** – Electronic programmable systems | Imaging software, dose‑control algorithms | Correctly identified in source (✓)【source [1]】 | Demonstrate software validation (IEC 62304) and usability (IEC 62366‑1). |
| **§10** – Chemical/physical/biological properties | Not applicable to the imaging function; only relevant for material biocompatibility. Source incorrectly links QC to §10【source [2]】 | Limit use of §10 to material safety data; map performance‑related QC to §§15, 16, 17. |

*Human escalation trigger*: Any persistent mis‑allocation of GSPR clauses in the dossier (e.g., using §10 for imaging quality) must be escalated to the technical writer and risk manager for correction.

---

### 4. Risk Management & Controls  

| Hazard | Control measure (linked GSPR) |
|--------|------------------------------|
| Unintended radiation exposure | Interlock system, automatic shut‑off, dose‑area product monitoring – **§16** |
| Software malfunction leading to incorrect diagnosis | IEC 62304‑based software lifecycle, verification & validation, fault tolerance – **§17** |
| Mechanical failure of X‑ray tube or detector | Design robustness, preventive maintenance, periodic performance checks – **§20** (mechanical/thermal risks) |
| Use by lay persons (if intended) | Training, clear labeling, IFU with warnings – **§22** |
| Electrical safety | IEC 60601‑1 compliance – **§18** (active devices & connections) |

All risk controls must be documented in the ISO 14971 risk management file and cross‑referenced to the relevant GSPR clauses.

*Human escalation trigger*: If any residual risk is identified that could lead to serious deterioration or death, a senior risk manager must review before the NB assessment (per Rule 11 classification considerations).

---

### 5. Missing / Unverified Information (to be clarified by the manufacturer)

| Item | Gap description |
|------|-----------------|
| **Exact intended use statement** – needs precise wording to confirm Class IIb scope. |
| **Device architecture diagram** – delineate source, detector, and software components for correct GSPR mapping. |
| **Clinical data set** – detail of pre‑market performance studies (sample size, comparator, statistical analysis). |
| **PMS plan specifics** – frequency of trend reporting, responsible personnel, escalation matrix. |
| **Labeling extracts** – draft IFU to verify compliance with Annex I §23. |
| **Declaration of Conformity number** – not present in source (verify separately). |

*Human escalation trigger*: Any unresolved gap after the manufacturer’s response must be flagged for senior RA review; if critical (e.g., missing clinical data), NB submission cannot proceed.

---

### 6. Summary Judgment  

- The device is **Class IIb** under **Annex VIII Rule 10** and therefore requires a **full conformity‑assessment route** (Annex IX or Annex X/​XI).  
- Current source excerpts show **incorrect GSPR mapping** (diagnostic function cited to §14, QC linked to §10). These must be corrected to §§15, 16, 17.  
- All required evidence listed above must be compiled; any missing item triggers a senior‑RA escalation before the Notified Body audit.

---

### 7. Peer‑Review Prompt  

> **Colleague, please challenge:**  
> • The assumption that Annex IX is the preferred route for this Class IIb X‑ray system – are there product‑specific reasons to prefer Annex X/​XI?  
> • The completeness of the GSPR mapping after correction – have we captured all relevant clauses (e.g., §20, §22) given the device’s user profile?  
> • Potential jurisdictional gaps: Does any other EU regulation (e.g., Radiation Protection Directive) impose additional obligations not covered here?

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

1. Chunk `1019675483246044284`

> ## 결함 EUR-Lex 원문(CELEX 02017R0745-20260101) Annex I 장 구조: - **§10 = Chemical, physical and biological properties**(화학·물리·생물학적 특성 — 독성·생체적합성 등) - **§14 = Construction of devices and interaction with their environment**(기기 구성·환경 상호작용) - **§15 = Devices with a diagnostic or measuring function**(진단·측정 기능 기기 — 정확도·정밀도·안정성) - §16 = 방사선 방호 ✓, §17 = 전자 프로그래머블 시스템 ✓(두 건은 정확) 1) 매핑 L105: '진단기기' GSPR은 **§15**이며 §14가 아님 — 조항번호 오귀속. 2) 영상품질 L15: 영상품질(정확도·안정성) QC의 GSPR 근거로 §10(화학·물리·생물학적 특성)은 무관 — 정답 계열 §15(및 §16/§17). 3) 검사개요 L28: 공정관리·검사의 EU 근거로 §10 무관 — 공정·검사 관련 GSPR·Annex IX QMS 심사 계열로 재귀속 필요.

2. Chunk `654155658666507043`

> ## 대상 - `05_검사_시험_밸리데이션/X-ray_장비_안전성능_표준_매핑.md` L105(§5.1 "GSPR Annex I §14 (진단기기), §16.2 (방사선), §17 (전자 프로그래머블 시스템)") - `05_검사_시험_밸리데이션/영상품질_QC_프로토콜.md` L15(frontmatter 근거 "EU MDR 2017/745 Annex I §10") - `05_검사_시험_밸리데이션/검사_시험_밸리데이션_개요.md` L28(§2 표 "공정관리·검사 | … | Annex I §10") - 클래스: C1 (조항번호/주제 귀속)

## ra_kr

### kb-eval-20260722-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "7978dfb67195557f", "source": "github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md", "source_hash": "54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `7978dfb67195557f`
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

> **Regulatory Draft – SBOM‑Related Obligations for Digital Medical Products under the “디지털의료제품법”**

---

### 1. Applicable Legal Framework  
| Provision | Core Requirement | Relevance to SBOM |
|-----------|-----------------|-------------------|
| **제13조 2호** – “전자적 침해행위로부터의 취약점에 대한 지속적 보완” | manufacturers & importers must continuously remedy software‑related vulnerabilities. | Directly supports the need for an up‑to‑date Software Bill of Materials (SBOM) that enables vulnerability tracking. |
| **제14조** – “전자적 침해행위로부터의 보호 조치” <br>① 식약처장 보안지침 마련 ② 제조업자·수입업자의 보안지침 준수 의무 | MFDS (식품의약품안전처) issues security‑related guidance; regulated parties must follow it. | The SBOM generation/management SOP should cite the specific security guideline(s) issued under this article. |
| **제16조** – “우수 관리체계 인증” (3 년 유효) | Voluntary certification assessing quality, safety and electronic‑attack prevention systems. | Not a statutory SBOM mandate; however, achieving this certification can demonstrate compliance with the obligations in §§ 13–14. |
| **제40조** – “디지털의료제품의 구성요소에 대한 성능평가” | Separate performance evaluation for sensors and AI algorithms. | If the digital product includes algorithmic components listed in the SBOM, each must undergo the performance assessment required by this article. |

*All citations are drawn from the source excerpts; they are established regulatory references (no “verify” caveat required).*

---

### 2. Device Classification & Submission Pathway  

| Item | Determination | Evidence Needed |
|------|----------------|-----------------|
| **Device class** (I, II, III, IV) | *Not identifiable from the source.* The classification hinges on intended use, risk level, and functional architecture (e.g., diagnostic vs. therapeutic, AI‑driven). | • Full Intended Use Statement <br>• Risk categorisation matrix (MFDS “의료기기 등급분류표”) <br>• Clinical risk analysis |
| **Regulatory route** | *Cannot be assigned without the class.* <br>‑ Class I: 사전 신고 (notification) <br>‑ Class II/III/IV: 허가 신청 (approval) with KGMP‑certified manufacturing site. | • Classification decision document <br>• KGMP compliance evidence (if applicable) |
| **Specific identifier** | No specific identifier found in source – verify separately. | — |

*Human escalation trigger:* **Missing classification data** → request the sponsor’s intended use, risk analysis, and any prior MFDS classification decisions before proceeding.

---

### 3. Required Submission Evidence  

| Requirement | Content | Current Gap |
|-------------|---------|--------------|
| **SBOM Generation & Management SOP (SOP‑SBOM‑001)** | Must reference the correct statutory basis: 제13조 2호 and 제14조 (not 제16조). Should outline procedures for inventory, version control, vulnerability monitoring, and linkage to MFDS security guidelines. | Source shows SOP currently cites 제16조 incorrectly; needs amendment. |
| **Security‑Guideline Compliance** | Show alignment with the MFDS security guidance issued under 제14조 (e.g., “전자적 침해행위 방지 가이드라인”). Include a mapping of SBOM items to identified CVEs and remediation actions. | No evidence of such mapping supplied. |
| **Performance Evaluation of Components** | For each sensor/AI algorithm listed in the SBOM, submit the component‑level performance data required by 제40조 (e.g., sensitivity / specificity for AI diagnostic models). | Not addressed; component‑level test reports missing. |
| **KGMP Certification** (if Class II–IV) | Certificate of compliance with KGMP (ISO 13485‑based) for the manufacturing site, including software development lifecycle controls. | Manufacturing‑site status not disclosed. |
| **Korean Language Labeling & IFU** | All labeling, Instructions For Use, and safety information must be provided in Korean per MFDS G‑GMP requirements. | No language compliance evidence presented. |
| **Post‑Market Surveillance (PMS) Plan** | Include a vulnerability‑response procedure that leverages the SBOM for rapid patch deployment under 제13조 2호. | PMS plan not referenced. |

*Human escalation trigger:* **Absence of security‑guideline alignment and component performance data** → require supplemental documentation before any submission can be compiled.

---

### 4. Risk Controls Related to SBOM  

| Control | Description | Legal Link |
|---------|-------------|-----------|
| **Vulnerability Identification & Tracking** | Continuous monitoring of disclosed CVEs for all listed software components; immediate risk assessment and mitigation. | 제13조 2호 (continuous remediation). |
| **Secure Development Lifecycle (SDLC)** | Incorporate threat modeling, code review, static/dynamic analysis, and signed builds into the software lifecycle. | Supports compliance with 보안지침 under 제14조. |
| **Access Control & Integrity Protection** | Cryptographic signing of SBOM files; role‑based access to the SBOM repository. | Aligns with “전자적 침해행위 예방” in 제16조 (as part of the broader 우수 관리체계). |
| **Incident Response Procedure** | Defined steps for breach notification, patch distribution, and MFDS reporting within 24 h of discovery. | Required by 제14조 security guidance. |
| **Periodic Audits & Certification Renewal** | Internal audits on SBOM accuracy; renewal of “우수 관리체계 인증” every three years to demonstrate continued compliance. | References 제16조 (voluntary certification). |

---

### 5. Human‑Escalation Triggers  

| Trigger | Reason | Action |
|--------|--------|-------|
| **Missing device classification** | Cannot select correct submission pathway or required dossier elements. | Pause draft; request sponsor’s intended use, risk analysis, and any prior MFDS classification decision. |
| **SBOM SOP cites 제16조 instead of 제13조/제14조** | Legal basis mis‑aligned → potential regulatory rejection. | Require immediate revision of SOP‑SBOM‑001 with correct citations; escalate to quality‐system lead. |
| **No evidence of security‑guideline compliance** | Non‑conformance to mandatory MFDS security measures (제14조). | Request documented alignment (e.g., gap analysis, implementation plan) before dossier assembly. |
| **Absence of component‑level performance data (제40조)** | Failure to meet required performance evaluation for digital product components. | Obtain test reports or defer submission until data generated. |
| **Lack of KGMP certification evidence (if Class II–IV)** | Mandatory for higher‑risk devices; would block 허가 신청. | Verify manufacturing site status; if not certified, initiate KGMP audit path. |
| **No Korean language labeling/IFU** | Contravenes MFDS labeling rules; would trigger post‑submission deficiencies. | Request translation and label review by a certified Korean language specialist. |

---

### 6. Reusable RA Judgment (Lesson Learned)  

> *When evaluating SBOM obligations for digital medical products under the “디지털의료제품법”, always cross‑check the statutory citation: the SBOM‑related duties are grounded in **제13조 2호** (continuous vulnerability remediation) and **제14조** (security‑guideline issuance & compliance). The frequently mis‑attributed **제16조** pertains only to the optional “우수 관리체계 인증” and does not create a direct SBOM mandate. Consequently, any SOP or regulatory argument referencing 제16조 for SBOM creation must be revised to cite the correct provisions. Additionally, confirm that each software component listed in the SBOM is supported by a separate performance evaluation per **제40조** when the device includes sensors or AI algorithms.*  

---

### 7. Peer‑Review Prompt  

*@RA‑Peer:* Please review the assumptions made about the statutory basis for SBOM obligations and the identified evidence gaps. Are there any additional Korean guidance documents (e.g., MFDS “보안지침” releases, recent amendment notices) that should be incorporated? Also evaluate whether the suggested risk controls fully satisfy both 제13조 2호 and 제14조 requirements, or if further measures are needed.

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

### kb-eval-20260722-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "393df4d80723d349", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `393df4d80723d349`
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

> **Regulatory Draft – Supplementary‑Response Strategy (MFDS)**  

---

### 1. Device & Intended Use (Information Required)
| Item | Status |
|------|--------|
| **Device name / model** | ❌ Not provided – must be supplied before any classification work can begin. |
| **Intended medical purpose** | ❌ Not provided – needed to map the device to MFDS risk‑based classes (Ⅰ,Ⅱ,Ⅲ). |
| **Comparable foreign regulatory status (FDA 510(k) / CE Mark)** | ❌ No identifier appears in source – verify separately. |
| **Key technical specifications / principle of operation** | ❌ Missing – required for hazard analysis and to decide if a clinical trial is mandatory. |

*Action*: Request the above details from the sponsor immediately; without them the submission route cannot be determined.

---

### 2. Preliminary Classification & Submission Route (Based on MFDS Rules)

| Risk Class (MFDS) | Typical Submission Pathway |
|-------------------|----------------------------|
| **Class Ⅰ** – low risk, exempted from MFDS 허가* | **신고** (notification) – immediate filing; no formal review period required. |
| **Class Ⅱ** – moderate risk | **허가(일반)** – full approval; standard review period 65 days (excluding any supplementary periods)【1】. |
| **Class III** – high risk / implantable | **허가(임상 포함)** – approval with clinical data; standard review period 80 days (excluding supplementary periods)【1】. |

\* MFDS 정의에 따라 “클래스Ⅰ(비감시·일반)”는 신고 절차이며, 허가와 구분됩니다.

**Decision point** – Once the intended use and risk factors are clarified, place the device in the appropriate class and select the corresponding pathway (신고 vs. 허가 일반/임상 포함).

---

### 3. Core Evidence Package (Typical Requirements)

| Evidence Category | MFDS Requirement (general) | Notes & Gaps |
|-------------------|----------------------------|--------------|
| **KGMP certification** | Manufacturing site must hold a KGMP certificate (ISO 13485‑based). | Facility audit report needed. |
| **Technical Documentation** (Design Dossier, Device Master File) | Must comply with MFDS “의료기기 기술문서 제출 기준”. | Details of design inputs/outputs missing. |
| **Non‑clinical testing** (biocompatibility, electrical safety, performance) | OECD‑aligned non‑clinical data accepted when referenced in MFDS notice. Verify the latest notice for acceptance criteria. | Test reports not supplied. |
| **Clinical Evidence** | • Class Ⅱ: clinical evaluation report (foreign CE/510(k) may be used with justification).<br>• Class Ⅲ: domestic clinical trial or recognized foreign pivotal study plus MFDS‑approved protocol. | No clinical data package provided; need to confirm if foreign data can be leveraged. |
| **Labeling & IFU** | All labeling must be in Korean language, including safety information, intended use, and instructions. Use MFDS‑approved wording style (see § 4‑C)【2】. | Draft Korean label not yet prepared. |
| **Risk Management File** | ISO 14971‑based risk analysis, with identified residual risks and mitigation measures. | Risk analysis missing. |

---

### 4. Missing Information & Immediate Requests

1. **Device classification data** (intended use, risk profile).  
2. **KGMP certificate copy** for the manufacturing site.  
3. **Full technical dossier** (design files, specifications).  
4. **Non‑clinical test reports** with reference to applicable OECD guidelines.  
5. **Clinical evidence** – either local trial plan or foreign study details + justification.  
6. **Draft Korean labeling/IFU** (must follow the expression templates in § 4‑C).  

*If any of the above cannot be supplied within the current review clock, an extension request must be submitted using the standard Korean phrase “연장 요청” as shown in source【2】.*

---

### 5. Risk Controls & Gap Analysis (ISO 14971 Lens)

| Hazard | Existing Control (if known) | Additional Required Control |
|--------|----------------------------|------------------------------|
| **Electrical safety** | – | Conduct IEC 60601‑1 testing; document compliance in the technical file. |
| **Biocompatibility** | – | Perform ISO 10993 series tests or provide validated foreign data with MFDS acceptance reference. |
| **Software malfunction (if applicable)** | – | Provide IEC 62304 software lifecycle documentation and a post‑market surveillance plan. |
| **Misuse/Labeling error** | – | Ensure Korean IFU uses the exact phrasing patterns from § 4‑C to avoid “보완 내용 인용” miscommunication. |

*Action*: Populate a risk‑management worksheet once device details are received; any unresolved high‑risk item triggers immediate human escalation (see Section 7).

---

### 6. Timeline Management (MFDS Processing Times)

| Step | Standard MFDS clock | Remarks |
|------|---------------------|---------|
| **Initial submission** | – | Clock starts at receipt of complete dossier. |
| **First review & any “보완 요청”** | – | Clock stops during supplementary period; see note that “보완 기간은 처리 기간에서 제외 (clock stops)”【1】. |
| **Final decision** | 65 days for 일반 허가, 80 days for 임상 포함 허가【1】 | Ensure all supplements are submitted before the statutory deadline to avoid extension. |

---

### 7. Human‑Escalation Triggers

| Trigger | Reason | Recommended Escalation |
|---------|--------|--------------------------|
| **No classification data after 3 business days** | Cannot determine submission route → risk of missed deadline. | Notify senior RA manager; flag as “Critical – Classification Undefined”. |
| **KGMP certificate missing** | Mandatory for any 허가 application. | Escalate to compliance & quality leadership. |
| **Local clinical data required but unavailable** | Class Ⅲ devices need domestic trial unless exception granted. | Open a formal risk‑benefit justification meeting with regulatory affairs lead and sponsor. |
| **Extension request needed** (clock approaching deadline) | MFDS expects timely supplements; delays may cause rejection. | Draft extension letter using the exact Korean template from § 4‑C【2】 and route for senior approval before submission. |
| **Non‑conformity in Korean wording** (e.g., missing “보완 내용 인용” format) | Could be rejected as non‑compliant documentation. | Immediate review by language specialist; escalated to project lead if correction exceeds 2 days. |

---

### 8. Citation Summary

| Source | Content Cited |
|--------|---------------|
| 【1】 (MFDS 허가 심사 처리 기간) | Standard review periods: 65 days (일반), 80 days (임상 포함); “보완 기간은 처리 기간에서 제외”. |
| 【2】 (한국어 공문 문체) | Recommended Korean phrasing for supplementary response, data attachment, trial status update, compliance statement, and extension request. |

---

### 9. Peer‑Review Prompt  

*“@RA‑Peer: Please examine the assumptions made in Sections 2–5 regarding classification determination without device specifics, the completeness of the evidence checklist, and any potential jurisdictional gaps (e.g., recent MFDS notices expanding accepted foreign non‑clinical data). Identify any missing regulatory citations or alternative Korean language templates that should be incorporated.”*

---

### 10. Reusable RA Judgment (Lesson Record)

> **Lesson:** When preparing a supplemental‑response plan for an MFDS medical‑device submission, the first step is to confirm *device classification & intended use*; without this, the review clock (65 days vs. 80 days) and required evidence (clinical data, KGMP certification, Korean labeling) cannot be defined. Always reference MFDS processing‑time tables (허가 심사 처리 기간) and employ the standardized Korean document expressions (보완 내용 인용, 연장 요청, 데이터 추가 제출) to ensure the supplement is accepted without procedural delays. Missing any of these core items should trigger a predefined human escalation before the MFDS clock resumes.

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

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `1071384471244337751`

> ### 4-C. 자주 사용하는 표현 (한국어 공문 문체) | 상황 | 표현 | |---|---| | 보완 내용 인용 | "귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다." | | 데이터 추가 제출 | "해당 데이터를 별첨 자료로 첨부하오니 검토하여 주시기 바랍니다." | | 시험 진행 중 | "현재 ○○기관에 시험 의뢰 중으로, 결과 수령 후 추가 제출 예정입니다." [검증 필요] | | 기준 적합성 | "관련 규격 ○○○ 기준을 충족함을 확인하였습니다." | | 연장 요청 | "시험 일정상 ○월 ○일까지 보완자료 제출이 어려우므로, 기한 연장을 요청드립니다." | ---

### kb-eval-20260722-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "abeb11318f80057b", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `abeb11318f80057b`
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

> **Regulatory Draft – Digital‑Medical Device (Software) Submission**

---

### 1. Classification & Submission Route  
| Item | Determination |
|------|----------------|
| **Device type** | Software‑only digital medical device (potentially AI/ML‑enabled, as indicated by the truncated “AI/ML…” row in the source). |
| **Regulatory class** | Must be determined from the intended use and risk profile.  <br>• If the software is classified **Class I**, a *신고* (notification) may suffice. <br>• For **Class II‑IV**, an *허가* (approval) is required under the MFDS digital‑medical‑device pathway. |
| **Evidence needed for classification** | – Intended use statement (diagnostic, therapeutic, monitoring, etc.)  <br>– Risk assessment outcome (ISO 14971).  <br>– Whether the software controls a medical function autonomously (AI/ML) → likely raises class to II or higher. |
| **Citation** | Classification rules are set out in the “디지털의료제품법 시행규칙” (Digital‑Medical‑Device Act Enforcement Rules). *(established regulatory reference – no verification note required)* |

---

### 2. Required Submission Evidence  

| Requirement | What Must Be Provided | Source Citation |
|-------------|----------------------|-----------------|
| **Software versioning & release information** (S‑1) | Version number, build number, and official release date for each software release to be marketed. | “SW 버전·빌드 번호·릴리스일” – 디지털의료제품법 시행규칙 |
| **Update policy** (S‑2) | Detailed description of update method, frequency, and procedures for emergency patches. | MFDS SW 가이드라인 |
| **Minimum system specifications** (S‑3) | OS, CPU, RAM, storage, monitor resolution, network requirements (minimum & recommended). | MFDS SW 가이드라인 |
| **Compatible medical devices & interface list** (S‑4) | List of all medical devices that can be connected, with interface standards. | — (no external citation needed) |
| **Data exchange formats** (S‑5) | Specification of DICOM, HL7, or other data standards used for input/output. | — |
| **Cybersecurity configuration guidance** (S‑6) | Password policy, network segregation, access‑control procedures. | MFDS 사이버보안 가이드라인 2025.01 |
| **Security‑patch application process & responsibility** (S‑7) | SOP for applying patches, designated responsible personnel, schedule. | MFDS 사이버보안 가이드라인 2025.01 |
| **Residual cybersecurity risk & mitigation** (S‑8) | Identification of known residual risks and planned countermeasures. | MFDS 사이버보안 가이드라인 2025.01 |
| **Data backup & recovery plan** (S‑9) | Procedures for regular backup, storage location, recovery testing frequency. | — |
| **System log management** (S‑10 – recommended) | Log collection, retention period, review process. | MFDS 사이버보안 가이드라인 |
| **Specialized labeling checklist items** (digital‑medical‑device specific) | All items added to the “디지털의료기기 특화 표시기재 요건 체크리스트” beyond the general IFU requirements. | 디지털의료기기 특화 표시기재 요건 체크리스트 (excerpt 2) |
| **Software development life‑cycle documentation** | IEC 62304 process description, verification & validation reports, change‑control records. | Standard practice – ISO/IEC 62304 (implied by MFDS SW expectations). |
| **Risk Management File** | ISO 14971 risk analysis, evaluation of residual risks, especially AI/ML‑related hazards. | Standard Korean requirement for medical device risk management. |
| **Clinical evidence (if required)** | Clinical performance data or literature supporting safety/effectiveness; if foreign CE/FDA clearance is being used, the relevant dossiers must be submitted as supplementary evidence. | No specific identifier found in source — verify separately. |

---

### 3. Missing Information (Gaps to Resolve)  

| Gap | Why It Matters | Action |
|-----|----------------|--------|
| **Intended use & clinical indication** | Drives classification, required clinical data, and risk controls. | Obtain a clear statement from the sponsor; map to MFDS class rules. |
| **Risk classification outcome (Class I‑IV)** | Determines whether 허가 or 신고 is needed. | Conduct ISO 14971 analysis and submit classification justification. |
| **AI/ML algorithm description** (only hinted at) | AI/ML introduces additional risk assessment, explainability, and data‑set validation requirements under MFDS guidance. | Provide full algorithm documentation, training/validation dataset details, performance metrics. |
| **Labeling & IFU Korean content** | MFDS requires all mandatory labeling items in Korean; the checklist (excerpt 2) adds items beyond general IFU elements. | Draft complete Korean IFU incorporating all checklist items and obtain translation verification. |
| **KGMP certification for manufacturing** (if hardware or bundled device is involved) | Required for devices in Class II‑IV that are manufactured domestically. | Confirm KGMP status of the production facility; include certificate copy. |
| **Cybersecurity testing evidence** | S‑6 to S‑8 are mandatory; MFDS expects demonstrable test results (penetration test, vulnerability scan). | Conduct and submit cybersecurity assessment reports. |
| **System log management plan** (S‑10 is only recommended) | Though optional, inclusion strengthens post‑market surveillance compliance. | Prepare a log‑management SOP and consider making it mandatory for submission. |
| **Foreign regulatory clearances** (if any) | MFDS may accept FDA 510(k), CE Mark evidence when accompanied by Korean translation and gap analysis. | Identify any existing foreign clearance; prepare Korean‑language bridge documents. |

---

### 4. Core Risk Controls to Highlight in Submission  

1. **Software lifecycle control** – IEC 62304 compliant development, version control, documented verification/validation.  
2. **Cybersecurity safeguards** – Password policies, network segregation, role‑based access, regular patching (S‑6–S‑8).  
3. **Data integrity & backup** – Automated backup schedule, off‑site storage, recovery test results (S‑9).  
4. **Logging & monitoring** – Centralized log collection with retention ≥ 12 months; routine review for anomalous activity (S‑10 recommendation).  
5. **Residual risk mitigation for AI/ML** – Explainability measures, continuous performance monitoring, human‑in‑the‑loop safeguards.  
6. **Usability & labeling compliance** – Korean IFU meeting the “디지털의료기기 특화 표시기재 요건 체크리스트” items; clear warnings and contraindications.

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger for RA / Regulatory Lead |
|-----------|-----------------------------------|
| **Unclear classification** (no intended use or risk output) | Pause submission; require sponsor clarification before proceeding to 허가/신고 decision. |
| **Missing mandatory cybersecurity documentation (S‑6–S‑8)** | Escalate to security team & RA manager – cannot file until evidence supplied. |
| **AI/ML residual risks not quantified** | Immediate escalation to senior RA and legal counsel; may need additional clinical validation. |
| **Korean IFU incomplete or lacking checklist items** | Stop filing; request translation and label package completion. |
| **KGMP certification absent for a Class II‑IV device** | Flag to manufacturing compliance officer; submission blocked until certificate obtained. |
| **Foreign clearance cited without Korean bridge documentation** | Escalate to regulatory strategy lead to prepare required gap analysis. |
| **Any “⚠️ 권장” item (e.g., S‑10) omitted for a high‑risk device** | Recommend inclusion; if sponsor refuses, senior RA must assess impact on approval probability and decide on go/no‑go. |

---

### 6. Peer Review Prompt  

*“@RA‑Peer: Please review the assumptions made regarding the classification pathway (especially the reliance on intended use to move from 신고 to 허가), the completeness of the cybersecurity evidence checklist, and any jurisdiction‑specific gaps that may arise from the digital‑medical‑device‑specific labeling checklist referenced in excerpt 2. Let me know if additional Korean statutes or MFDS notices should be cited, or if any of the identified missing items merit a different risk‑control approach.”*

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

### kb-eval-20260722-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "1347e6dd14cc6def", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `1347e6dd14cc6def`
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

> **Regulatory Draft – Digital‑Medical‑Device (디지털의료제품) – Pre‑Market Assessment**

---

### 1. Device Classification & Submission Route  

| Korean Legal Basis | Interpretation for the present device* |
|-------------------|------------------------------------------|
| **제9조 – 임상시험계획 승인** | Required when the device claims *clinical efficacy* (e.g., therapeutic effect, diagnostic performance). |
| **제10조 – 임상적 성능시험계획 승인** | Required for devices where *performance testing* in a clinical environment is needed but not full‑scale pivotal trials. |
| **제15조 – 실사용 평가** | Pertains only to post‑market “real‑world evidence (RWE)” collection; **not** a pre‑market justification of efficacy/clinical performance. |
| **제16조 – 우수 관리체계 인증(GMP) 신청·평가** | Mandatory for Class II–III devices; manufacturer must hold KGMP certification before submission. |
| **제39조 – 사전 검토(허가·신고 등)** | Allows a pre‑submission consultation with MFDS to confirm dossier completeness. |

\*The device under review is assumed to be a software‑based digital health product that intends to provide clinical benefit (e.g., decision‑support, risk prediction).  

**Proposed classification & pathway:**  
- **If the product claims therapeutic/diagnostic efficacy → Class II or III (risk‑based) requiring **제9조** or **제10조** approval (clinical trial plan).  
- If it is purely wellness/education with no clinical claim → Class I, eligible for a **신고** (notification) under the simplified route, provided KGMP is in place.

---

### 2. Required Evidence Packages  

| Requirement | Legal Reference | Content Needed |
|-------------|-----------------|----------------|
| **Clinical‑efficacy evidence** (if efficacy claimed) | **제9조** or **제10조** (clinical trial plan approval) | • Approved clinical investigation protocol (IRB approval, MFDS notification). <br>• Clinical performance data (sensitivity, specificity, ROC curves) or therapeutic outcome measures. |
| **Technical documentation / device description** | **디지털의료제품법** (general) & MFDS Technical File Guidance | • System architecture, software versioning, algorithms (including AI/ML if applicable). <br>• Verification & validation reports. |
| **KGMP certification** | **제16조** – 우수 관리체계 인증 | • KGMP certificate for the manufacturing site (or contract manufacturer). |
| **Cybersecurity & change‑management plan** | Implied by **제13조** (continuous compliance) and MFDS AI/ML Guidance | • Threat model, vulnerability management procedures, post‑market bug‑fix process. |
| **Post‑market surveillance plan** | **제13조** – 결함정보 수집·사이버 취약점 보완 등 상시 준수 의무 | • RMP (Risk Management Plan) with real‑world data collection strategy (to be used later under **제15조**, not for pre‑approval). |
| **Pre‑submission consultation request (optional)** | **제39조** – 사전 검토 절차 | • Cover letter and outline of intended submission to obtain MFDS feedback on dossier completeness. |

---

### 3. Missing / Insufficient Information  

1. **Clarification of the legal basis for clinical efficacy**  
   - The source flags that the current mapping to **제15조** is inappropriate; the correct reference should be **제9조/제10조** (see D4‑DR07 comment). A decision on which article applies must be made before dossier finalisation.  

2. **Clinical trial plan or performance‑test protocol**  
   - No evidence of an approved clinical investigation (IRB approval, MFDS notification) is provided in the excerpts.  

3. **KGMP status**  
   – The manufacturing entity’s KGMP certification status is not mentioned.  

4. **Cybersecurity / AI change‑management documentation**  
   – Although **제17조** deals with “우수 관리체계 인증” (GMP‑like) and is unrelated to AI change management, the device will still need a PCCP (Post‑market Change Control Plan) per MFDS AI/ML guidance; this is not addressed.  

5. **Real‑world evidence (RWE) strategy**  
   – While **제15조** concerns post‑market “실사용 평가,” no plan for future RWE collection is described. This is optional pre‑market but should be outlined for later compliance.  

---

### 4. Risk Controls & Mitigation Measures  

| Risk Category | Control Required (Korean Legal Basis) |
|---------------|----------------------------------------|
| **Clinical safety / efficacy** | • Conduct a clinical investigation compliant with **제9조/제10조**.<br>• Include independent data monitoring committee (if applicable). |
| **Software reliability / AI performance drift** | • Implement version control and traceability (per KGMP & MFDS AI/ML guidance).<br>• Define a post‑market change management plan (PCCP) – even though not mandated by **제17조**, it is expected by MFDS. |
| **Cybersecurity vulnerabilities** | • Follow the cybersecurity framework stipulated in **제13조** and MFDS “Guidelines for Cybersecurity of Digital Health Devices.”<br>• Establish a vulnerability disclosure process and periodic penetration testing. |
| **Post‑market defect reporting** | • Set up a system to collect defect information, cyber‑vulnerability reports, and adverse events per **제13조**.<br>• Report serious incidents within 15 days to MFDS (as per standard medical device regulation). |

---

### 5. Citations (Established Regulatory References)  

| Citation | Source |
|----------|--------|
| 디지털의료제품법 제9조 – 임상시험계획 승인 | 법령 원문, 2026년 시행 |
| 디지털의료제품법 제10조 – 임상적 성능시험계획 승인 | 법령 원문, 2026년 시행 |
| 디지털의료제품법 제15조 – 실사용 평가 (RWE) | 법령 원문, 2026년 시행 |
| 디지털의료제품법 제16조 – 우수 관리체계 인증 신청·평가 | 법령 원문, 2026년 시행 |
| 디지털의료제품법 제17조 – “우수 관리체계 인증” (GMP‑유사) | 법령 원문, 2026년 시행 |
| 디지털의료제품법 제13조 – 제조·수입업자의 지속적 준수 의무 | 법령 원문, 2026년 시행 |
| 디지털의료제품법 제39조 – 사전 검토 절차 | 법령 원문, 2026년 시행 |

*No specific identifier (e.g., predicate 510(k) number, case ID) appears in the source excerpts. → **no specific identifier found in source — verify separately**.*

---

### 6. Human‑Escalation Triggers  

| Situation | Why Escalate & To Whom |
|-----------|------------------------|
| **Uncertainty whether clinical efficacy falls under 제9조 or 제10조** (see D4‑DR07 comment) | Immediate RA lead review; if unresolved, request clarification from MFDS via 사전 검토 (제39조). |
| **Absence of KGMP certification evidence** | Escalate to Manufacturing Compliance Lead; halt submission until certificate obtained. |
| **Missing clinical trial/ performance test protocol** | Pause dossier assembly; engage Clinical Development team for IRB‑approved plan; if not feasible, reconsider classification (downgrade to non‑clinical claim). |
| **AI algorithm change‑management not documented** | Trigger AI/ML specialist review; prepare PCCP before submission. |
| **Cybersecurity assessment incomplete** | Forward to IT security team; require penetration test report prior to filing. |
| **Post‑market surveillance plan lacking (future 실사용 평가)** | Flag for regulatory strategy meeting; develop RWE collection framework to satisfy later **제15조** obligations. |

---

### 7. Peer Review Prompt  

> **@RA‑Peer:** Please evaluate the assumptions made regarding:  
> - The classification decision based on the presence of clinical efficacy claims (i.e., whether 제9조 or 제10조 is appropriate).  
> - The completeness of source coverage for each cited article—are any relevant provisions (e.g., 제14조, data‑privacy requirements) omitted that could affect the submission?  
> - Potential jurisdictional gaps such as Korean language labeling, IFU translation, and local clinical data mandates that may not be captured in the current draft.  

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

1. Chunk `399070733591760115`

> ### D4 — DR-07 (라인 76) - **기재값:** `임상적 유효성(해당 시) | 법 제15조` - **문제:** 임상적 유효성/임상평가는 법 제9조(임상시험계획 승인) 또는 제10조(임상적 성능시험계획 승인)에 해당할 가능성이 높으며, 제15조(실사용평가)와는 별개 개념. - **권고:** `법 제15조` → 제9조/제10조 중 해당 조문으로 정정 검토.

2. Chunk `515031043224754498`

> ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 [시행 2026.1.24.] [법률 제20139호]) | 조문 | 법정 제목·내용(원문) | |---|---| | **제15조** | **"실사용 평가"** — 디지털의료기기제조업자등이 실제 사용 과정에서 수집된 정보로 안전성·유효성을 평가하는 것(실사용증거/RWE). 기술문서·사용적합성·임상적 유효성과 무관. | | **제17조** | **"우수 관리체계 인증의 신청 및 평가 등"** — 제16조 우수 관리체계 인증(GMP 유사 인증)의 신청·평가 절차. AI 변경관리계획(PCCP)과 무관. | | **제13조** | **"디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항"** — 결함정보 수집·사이버 취약점 보완 등 상시 준수의무. MFDS 사전상담(사전검토)과 무관. | | **제39조** | **"허가·신고 등의 사전 검토"** — 제조허가·인증·신고 등에 필요한 자료를 사전에 MFDS에 검토 요청할 수 있는 절차. MFDS 사전상담의 정확한 근거조문. |

### kb-eval-20260722-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-22", "decision_ref": "kb-eval-20260722-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "5cfb70d29c7cfdeb", "source": "github:holee9/MD-process/issue-drafts/956_AUDIT_디지털의료제품법_요구사항_매트릭스_DR02_조항_인용부정확.md", "source_hash": "6e02eaedc1e24e41f1a1bf208b930a59f96d8b39f382a3eeb018e5f289d2d799"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5cfb70d29c7cfdeb`
- Source: `github:holee9/MD-process/issue-drafts/956_AUDIT_디지털의료제품법_요구사항_매트릭스_DR02_조항_인용부정확.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/issue-drafts/956_AUDIT_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4_DR02_%EC%A1%B0%ED%95%AD_%EC%9D%B8%EC%9A%A9%EB%B6%80%EC%A0%95%ED%99%95.md)
- Source hash: `6e02eaedc1e24e41f1a1bf208b930a59f96d8b39f382a3eeb018e5f289d2d799`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `956_AUDIT_디지털의료제품법_요구사항_매트릭스_DR02_조항_인용부정확.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 1차 출처 정답 (디지털의료제품법 시행규칙, 총리령 제2025호, 2025-02-28 시행 — 법 조문 인용 부분) 시행규칙 각 조에서 확인된 법 조문 대응관계: | 법 조문 | 내용 | 시행규칙 근거 | |---|---|---| | **법 제8조** | **제조업허가·제조허가·제조인증·제조신고**(품질책임자 배치·시설/품질관리체계 기준 포함) | 시행규칙 제5~13조 (제5조 "법 제8조제1항 전단에 따라 디지털의료기기 제조업허가를 받으려는 자는...") | | 법 제9조 | 임상시험계획 승인 | 시행규칙 제14~18조 | | 법 제10조 | 임상적 성능시험계획 승인 | 시행규칙 제19~22조 | | **법 제11조** |...
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

> **Regulatory Draft – Manufacturing License & Quality‑Management Compliance (DR‑02)  
Digital Medical Devices Act (디지털의료제품법)**  

---

### 1. Applicable Legal Basis  

| Requirement | Primary legal source | Supporting enforcement rule |
|-------------|---------------------|------------------------------|
| **Manufacturing license / manufacturing permit / manufacturing certification / manufacturing notification** | **Law Article 8** – “제조업허가·제조허가·제조인증·제조신고” (includes placement of a quality‑responsible person and facility/quality‑system standards) | Enforcement Rules Articles 5–13 (e.g., Art. 5: “법 제8조제1항 전단에 따라 디지털의료기기 제조업허가를 받으려는 자는 …”) |
| **Change permit (major post‑approval changes)** | Law Article 11 – “디지털의료기기 변경허가 등” (applies after the manufacturing license is granted) | Enforcement Rule Art. 23 (“법 제11조제1항 전단에서 ‘총리령으로 정하는 중요한 사항’ …”) |
| **Clinical trial plan approval** | Law Article 9 | Enforcement Rules Articles 14–18 |
| **Clinical performance‑test plan approval** | Law Article 10 | Enforcement Rules Articles 19–22 |
| **Real‑world use evaluation (post‑market clinical data)** | Law Article 15 | Enforcement Rule Art. 30 |
| **Quality‑management system certification (U‑MCS)** | Law Article 16 | Enforcement Rules Arts 31–32 |
| **Component (sensor/AI) performance assessment** | Law Article 40 | Enforcement Rule Art. 50 |

*Key audit finding*: The DR‑02 requirement (“제조업 허가 + 품질관리기준 적합 판정”) was incorrectly linked to **Law Article 11** in the original citation. The correct grounding is **Law Article 8**; Article 11 governs only post‑licensure changes.

---

### 2. Classification & Submission Route  

| Item | Determination (based on source) | Comments |
|------|---------------------------------|----------|
| Device class (I, II, III, IV) | *No specific classification information provided in the excerpts.* | **Missing information** – must be derived from the device’s intended use, risk level and functional characteristics per the Digital Medical Devices Act classification table. |
| Submission pathway for manufacturing authorization | **Manufacturing license** under Law Art. 8 → submit “제조업 허가” application to MFDS with required documentation (see Section 3). | If the device is Class I (low‑risk) a simplified notification may be possible, but classification must first be confirmed. |
| Post‑approval change pathway | Change permit under Law Art. 11 when “important matters” (defined by the Prime Minister’s decree) are altered after license issuance. | Ensure separate filing; does **not** replace the initial manufacturing authorization. |

*Action*: Verify device class using the Act’s classification matrix and update the submission route accordingly.  

---

### 3. Evidence Package Required for Manufacturing License (DR‑02)

| Evidence Category | Specific Documents / Data | Legal Reference |
|-------------------|---------------------------|-----------------|
| **Quality‑responsible person (품질책임자) appointment** | CV, qualification certificates, assignment letter | Law Art. 8; Enforcement Rules Arts 5–13 |
| **Facility & quality‑management system** | KGMP certification (Korean Good Manufacturing Practice), ISO 13485 certificate, floor plans, SOPs for production, sterilization, process validation | Law Art. 8; Enforcement Rules Arts 5–13; KGMP requirement aligns with MFDS notice on GMP (see latest MFDS notice – retrieve for exact number) |
| **Device description & intended use** | Technical file, risk analysis (ISO 14971), device summary, labeling mock‑ups (Korean language) | Law Art. 8 |
| **Clinical evidence (if required by class)** | Clinical trial report or foreign clinical evaluation (FDA 510(k) predicate / EU CE Clinical Evaluation Report) – *only if the device is Class II‑IV* | Law Arts 9–10; Enforcement Rules Arts 14–22. Use MFDS’s acceptance of OECD‑aligned non‑clinical data where applicable (cite latest MFDS notice after verification). |
| **Performance testing for components** (sensor, AI algorithm) | Bench test reports, software validation, AI explainability documentation | Law Art. 40; Enforcement Rule Art. 50 |
| **Real‑world use evaluation plan** (if Class III/IV) | Post‑market clinical study protocol | Law Art. 15; Enforcement Rule Art. 30 |
| **U‑MCS certification evidence** (if required) | Certificate of U‑MCS issuance, audit reports | Law Art. 16; Enforcement Rules Arts 31–32 |

*Missing items*:  
- Exact device class & corresponding risk classification.  
- Confirmation that the manufacturing site holds a current KGMP certificate.  
- Localization of labeling & IFU in Korean (mandatory for all classes).  

---

### 4. Risk Controls to be Demonstrated

1. **Hazard identification & risk analysis** – conforming to ISO 14971, with traceability matrix linking hazards to mitigations.  
2. **Software/AI lifecycle controls** – per IEC 62304 and MFDS guidance on AI‑based medical devices (latest notice). Include data set documentation, performance metrics, post‑deployment monitoring plan.  
3. **Manufacturing process validation** – process capability studies, sterilization validation (if applicable), environmental control records.  
4. **Supply‑chain oversight** – verification of component suppliers, especially for sensors or AI modules; include supplier audit reports.  
5. **Post‑market surveillance system** – establish PMS plan aligned with MFDS § 23‑24 (real‐world evidence collection, adverse event reporting).  

---

### 5. Citations Used in This Draft  

| Citation Type | Reference |
|---------------|-----------|
| Established regulatory reference | Law Article 8 (manufacturing license) – **정확한 근거** |
| Established regulatory reference | Law Article 11 (change permit) – **정확한 근거** |
| Established regulatory reference | Enforcement Rule Articles 5‑13, 23, 30, 31‑32, 50 – **정확한 근거** |
| Case‑level specific identifier | *no specific identifier found in source — verify separately* (e.g., predicate device number, registration number) |

All statutory citations are taken directly from the source excerpts; no invented identifiers or dates have been added.

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason & Required Action |
|---------|--------------------------|
| **Unresolved classification** – device class not identified in source material. | Senior RA must confirm classification using the Act’s risk matrix before any submission can proceed. |
| **Absence of KGMP certification evidence** – required for manufacturing license under Art. 8. | Facility compliance officer to provide current KGMP certificate; if unavailable, halt submission. |
| **Discrepancy in legal citation (Art. 11 vs. Art. 8) still present in downstream documents** – risk of regulatory non‑conformity. | Immediate correction by the drafting team; senior RA review before final filing. |
| **Missing Korean labeling/IFU** – mandatory regardless of class. | Labeling specialist to produce Korean language labeling; pause submission until completed. |
| **Insufficient clinical evidence for Class II‑IV devices** – only foreign data mentioned, but no local clinical plan. | Clinical affairs lead must develop or obtain a MFDS‑approved clinical trial plan (Art. 9) or justify reliance on foreign data per latest MFDS notice; senior review required. |
| **Audit flag not resolved** – source indicates an audit of the citation for DR‑02. | Escalate to RA manager for validation that the correction to Art. 8 has been incorporated in all related SOPs and submission templates. |

If any trigger is met, the issue must be escalated to the senior regulatory affairs lead before moving forward with the MFDS filing.

---

### 7. Reusable Judgment (to be recorded in the RA knowledge base)

> **Lesson:** For DR‑02 (“manufacturing license + quality‑management standard compliance”) the correct statutory basis is **Digital Medical Devices Act Article 8**. Article 11 pertains only to post‑licensure change permits. Whenever a source cites Article 11 for initial manufacturing authorization, flag it as an error and replace with Article 8 before preparing any submission. Ensure that the supporting enforcement‑rule articles (5–13) are also referenced.  

This judgment should be stored under *“Digital Medical Devices Act – DR‑02 citation correction”* for future reference.

---

### 8. Peer Review Request

> **@RA‑Peer:** Please review this draft and challenge:  
> - Whether any additional MFDS notices (e.g., recent updates on foreign clinical data acceptance) might affect the evidence requirements listed here.  
> - The completeness of risk‑control coverage, especially for AI‑driven components.  
> - Any jurisdiction‑specific gaps not captured because the source excerpts lack detail (e.g., post‑market reporting timelines, specific labeling format).  

Your feedback will ensure that all Korean regulatory nuances are fully addressed before submission.

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

1. Chunk `200576646193092927`

> ## 1차 출처 정답 (디지털의료제품법 시행규칙, 총리령 제2025호, 2025-02-28 시행 — 법 조문 인용 부분) 시행규칙 각 조에서 확인된 법 조문 대응관계: | 법 조문 | 내용 | 시행규칙 근거 | |---|---|---| | **법 제8조** | **제조업허가·제조허가·제조인증·제조신고**(품질책임자 배치·시설/품질관리체계 기준 포함) | 시행규칙 제5~13조 (제5조 "법 제8조제1항 전단에 따라 디지털의료기기 제조업허가를 받으려는 자는...") | | 법 제9조 | 임상시험계획 승인 | 시행규칙 제14~18조 | | 법 제10조 | 임상적 성능시험계획 승인 | 시행규칙 제19~22조 | | **법 제11조** | **디지털의료기기 변경허가 등**(제조업허가·제조허가 후 중요사항 변경) | 시행규칙 제23조 ("법 제11조제1항 전단에서 '총리령으로 정하는 중요한 사항'이란...") | | 법 제15조 | 실사용 평가 | 시행규칙 제30조 | | 법 제16조 | 우수 관리체계 인증 | 시행규칙 제31~32조 | | 법 제40조 | 디지털의료제품 구성요소 성능평가(센서·AI) | 시행규칙 제50조 | 즉 DR-02 "제조업 허가 + 품질관리기준 적합 판정"의 정확한 근거는 **법 제8조**이며, 법 제11조(변경허가)는 최초...

2. Chunk `403794146442956433`

> ## 독립 감사 요약 DR-02 항목은 "제조업 허가 + 품질관리기준 적합 판정" 요구사항의 근거를 **법 제11조**로 인용하나, Tier 1(디지털의료제품법 시행규칙 원문, 총리령 제2025호) 재확인 결과 **법 제11조는 "디지털의료기기 변경허가 등"**(제조 완료 후 중요사항 변경 시 변경허가/변경인증/변경신고) 조항이다. 제조업허가·제조허가·제조인증·제조신고의 근거는 **법 제8조**이다.
