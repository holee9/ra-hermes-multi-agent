# KB Eval Checksheet - 2026-07-21 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260721-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_us-001", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "59d86e1c8737dd40", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

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

> **Regulatory Draft – AI‑Based SaMD Change Impact Assessment (PCCP)**  

---

### 1. Device Classification & Submission Pathway  
| Question | Answer |
|----------|--------|
| **Device type** | Software as a Medical Device (SaMD) that incorporates an artificial‑intelligence/machine‑learning (AI/ML) algorithm and is intended to provide clinical decision support or diagnosis. |
| **Regulatory class** | *Presumed* Class II, because most AI‑enabled diagnostic software falls under 21 CFR §892.2050 (Medical image management and processing system – Class II). **Citation:** 21 CFR Part 892 (§892.2050) – established reference. <br>*If the intended use is a novel indication or higher risk (e.g., autonomous treatment recommendation), a Class III determination may be required; in that case a PMA would be needed.* |
| **Primary submission route** | 510(k) → Substantial‑equivalence to an already cleared AI/ML SaMD (or to a non‑AI version of the same function). <br>*If no suitable predicate exists, pursue De Novo classification (Class II) and subsequently use the cleared De Novo as a predicate for future 510(k)s.* |
| **Specific identifier** | No specific 510(k) or predicate number appears in the source – verify separately. |

---

### 2. Required Evidence Package (per 21 CFR §§807, 820 and FDA AI/ML guidance)

| Evidence Category | Core Items | Source‑derived Requirement |
|-------------------|-----------|----------------------------|
| **Device description & intended use** | Full software architecture, clinical indication, user environment. | — |
| **Predicate comparison (if 510(k))** | Side‑by‑side table of functional and technological characteristics; demonstration that the new device does not raise different safety or effectiveness concerns. | — |
| **Software Life‑Cycle Documentation** | IEC 62304–based development plan, risk management file (ISO 14971), verification & validation (V&V) results, configuration management. | — |
| **Predetermined Change Control Plan (PCCP)** | Four mandatory sections: <br>1️⃣ *Data Management* – procedures for data collection, cleansing, versioning and bias mitigation.<br>2️⃣ *Retraining Practices* – defined triggers, retraining workflow, rollback strategy.<br>3️⃣ *Performance Evaluation* – pre‑specified acceptance criteria, V&V methodology, statistical significance thresholds.<br>4️⃣ *Updated Procedures* – communication plan for users/clinicians, real‑world monitoring, IFU updates. <br>**Citation:** Source excerpt [2] (Modification Protocol table). |
| **Clinical performance data** | Retrospective or prospective study showing that the algorithm meets the prespecified acceptance criteria on a clinically representative dataset; subgroup analysis to address bias. | — |
| **Human Factors / Usability** | Formative and summative usability testing per FDA Human Factors guidance (21 CFR §820.30). | — |
| **Cybersecurity & Data Integrity** | Threat model, mitigation controls, post‑market vulnerability management plan (per FDA “Content of Premarket Submissions for Management of Cybersecurity” guidance). | — |
| **Labeling & IFU** | Device label, instructions for use (including description of the PCCP and how users are notified of updates). | 21 CFR §801 – established reference. |
| **UDI implementation** | Assign a UDI carrier and submit device identifier to GUDID. **Citation:** 21 CFR Part 830 (§830.10 onward) – established reference. |

---

### 3. Missing Information (to be obtained before submission)

| Gap | Why it matters |
|-----|----------------|
| **Exact intended use statement** (e.g., “assist radiologists in detecting pulmonary nodules on CT”) | Determines classification and predicate search. |
| **Predicate device identifiers** (510(k) numbers, product codes) | Required for substantial‑equivalence claim. |
| **Clinical performance dataset details** – size, source, diversity, ground truth methodology | Needed to satisfy Performance Evaluation element of the PCCP and FDA’s “clinical evaluation” expectations. |
| **Risk management file (ISO 14971)** – hazard analysis, risk controls matrix | Mandatory for 510(k) and De Novo submissions; supports safety rationale. |
| **Cybersecurity threat assessment** | Required under 21 CFR §820.30 and FDA cybersecurity guidance. |
| **User training / IFU change‑notification process** | Part of the “Updated Procedures” element of PCCP; impacts labeling compliance. |
| **Algorithm versioning & rollback procedures (technical specifications)** | Integral to the Retraining Practices section of PCCP; demonstrates control over post‑market changes. |

---

### 4. Key Risk Controls (aligned with ISO 14971)

1. **Design controls** – documented software requirements, traceability matrix.
2. **Algorithmic bias monitoring** – periodic statistical review against demographic subgroups (Data Management).
3. **Performance drift detection** – automated alerts when real‑world data fall outside acceptance criteria (Retraining Practices).
4. **Rollback capability** – ability to revert to prior certified algorithm version within 24 h of adverse event detection.
5. **User notification & training** – structured communication plan for every software update (Updated Procedures).
6. **Cybersecurity safeguards** – encrypted data transmission, authentication, regular penetration testing.

---

### 5. Human‑Escalation Triggers (when to involve senior RA or regulatory authority)

| Trigger | Action Required |
|---------|-----------------|
| **Change exceeds the pre‑specified PCCP scope** (e.g., new indication, algorithm architecture change) | Submit a supplemental 510(k) (SC) or a new 510(k) before deployment. |
| **Observed increase in adverse events or performance below acceptance criteria** | Initiate FDA Medical Device Reporting (MDR) per 21 CFR §803 and prepare a corrective‑and‑preventive action (CAPA) plan; consider filing a post‑market change notification. |
| **Significant risk level shift identified in updated ISO 14971 analysis** | Escalate to senior RA for possible reclassification review or PMA pathway consideration. |
| **Cybersecurity vulnerability with exploitable risk** | Notify FDA under 21 CFR §803.13 (cybersecurity incident reporting) and implement emergency patch; document in post‑market surveillance. |
| **User feedback indicating unintended use or misinterpretation of IFU** | Trigger a usability remediation cycle and update labeling; if widespread, file a voluntary corrective action with FDA. |

---

### 6. Citations Summary  

| Topic | Citation |
|-------|----------|
| Classification – imaging‑software class | 21 CFR Part 892 (§892.2050) – established reference |
| Labeling requirements | 21 CFR §801 – established reference |
| UDI labeling obligations | 21 CFR Part 830 (§830.10 onward) – established reference |
| Predetermined Change Control Plan (PCCP) elements | Source excerpt [2] (“Modification Protocol” table) |
| FDA guidance URLs for PCCP | Source excerpt [1] (links to final guidance documents) |

*No case‑level identifiers (510(k)/predicate numbers) were present in the source; “no specific identifier found in source – verify separately.”*

---

### 7. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumed Class II classification under §892.2050 and confirm whether the intended use description (currently unspecified) might push this SaMD into a higher risk category requiring PMA. Also verify that all four PCCP elements captured from the source are sufficient for FDA’s 2024 final guidance on AI/ML devices, and flag any gaps in our evidence package (e.g., clinical performance data depth or cybersecurity documentation).  

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

1. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

2. Chunk `198015203798949382`

> ### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---

### kb-eval-20260721-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_us-002", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "201daf0b783b9dd3", "source": "github:holee9/MD-process/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md", "source_hash": "efcd12a4b49cb21ffa28b5f1aa35345e8bb04b98c57a32649483fa824de23fff"} -->

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

> **Regulatory Draft – SaMD Change Impact Assessment (Predetermined Change Control Plan)**  

---

### 1. Bottom‑Line Decision  
- **Classification / Submission Route:** Treat the AI‑enabled SaMD as a *Class II* device unless its intended use or risk profile demonstrably exceeds the scope of existing predicate devices. The default pathway is a **510(k) Premarket Notification** (21 CFR §807). If no suitable predicate exists, plan for a **De Novo** submission.  
- **Required FDA‑specific artifact:** A **Predetermined Change Control Plan (PCCP)** as mandated by the final FDA guidance issued December 2024.  

---

### 2. Core Regulatory Requirements  

| Area | Required Evidence / Deliverable | citation |
|------|--------------------------------|-----------|
| **Device Classification** | Identify intended use, clinical context, and risk level; map to a CFR‑part (e.g., 21 CFR §892 for imaging SaMD or §862 for diagnostic SaMD). | 21 CFR Part 892 (Imaging) / Part 862 (Clinical Chemistry) – established |
| **510(k) Submissions** | Predicate device comparison, performance testing (bench, usability, clinical), labeling, software description, risk analysis. | 21 CFR §807.92(a) – established |
| **Predetermined Change Control Plan (PCCP)** | • Scope of changes covered (algorithm updates, data set refreshes)<br>• Pre‑specified performance metrics and acceptance criteria<br>• Validation protocol for each change type<br>• Post‑change monitoring plan (real‑world evidence, drift detection) | FDA *Predetermined Change Control Plan* Guidance, Dec 2024 – established |
| **Quality Management System (QMS)** | Compliance with the QMS Regulation effective 02 Feb 2026 (21 CFR §820), aligned to ISO 13485:2016. | 21 CFR Part 820 – established |
| **Software Lifecycle** | IEC 62304‑compliant development and maintenance processes; traceability matrix linking requirements, risk controls, and code modules. | IEC 62304 – standard (established) |
| **Risk Management** | ISO 14971‑based analysis covering algorithm bias, data drift, explainability, failure modes; mitigation strategies documented in the PCCP. | ISO 14971 – standard (established) |
| **UDI/Labeling** | Assign a Unique Device Identifier per 21 CFR §830; label must reflect versioning and change‑control status. | 21 CFR Part 830 – established |
| **Post‑Market Surveillance** | Real‑world performance plan, periodic safety updates, adverse event reporting (21 CFR §803). | 21 CFR Part 803 – established |

---

### 3. Missing Information that Must Be Obtained  

1. **Exact Intended Use Statement** – e.g., “detect cardiac arrhythmia from ECG signals” vs. “assist radiologists in lung nodule segmentation.”  
2. **Device Risk Classification Rationale** – justification for Class II (or II‑Special/III) based on intended use and risk analysis.  
3. **Predicate Device(s)** – 510(k) numbers, if any; otherwise a statement that none exist (triggering De Novo). *No specific identifier found in source — verify separately.*  
4. **Scope of Algorithmic Changes** – which parameters, model architectures, or training data sets are covered under the PCCP.  
5. **Performance Acceptance Criteria** – quantitative thresholds for sensitivity, specificity, AUC, etc., pre‑ and post‑change.  
6. **Clinical Validation Data Set Details** – size, demographics, labeling standards.  

---

### 4. Risk Controls to Embed in the PCCP  

| Control | Purpose / Implementation |
|---------|---------------------------|
| **Drift Detection & Monitoring** | Automated statistical monitoring of input data distribution; trigger review if drift exceeds pre‑defined limits. |
| **Explainability Module** | Provide clinician‑readable rationale for AI outputs; required for transparency and to mitigate bias. |
| **Change Impact Assessment Matrix** | Map each change type (e.g., model weight update, feature addition) to risk level; assign validation depth accordingly. |
| **Version Lock & Roll‑Back Capability** | Ability to revert to previous certified version if post‑change performance degrades. |
| **Human Oversight Trigger** | Any change that raises the algorithm’s risk score above the baseline or alters intended use → mandatory FDA supplemental submission. |
| **Post‑Market Real‑World Evidence (RWE) Capture** | Structured collection of outcome data for continuous safety/efficacy verification. |

---

### 5. Human–Escalation Triggers (When to Involve FDA & Senior Review)  

| Trigger | Action Required |
|--------|-----------------|
| **Change expands or modifies intended use** (e.g., adds new indication) | Submit a **Supplemental 510(k)** or **De Novo request** before deployment. |
| **Algorithmic performance falls outside pre‑specified acceptance criteria** (as measured by validation or RWE) | Immediate pause of distribution; prepare an FDA **Major Change Notification** (if covered under PCCP scope) and conduct root‑cause analysis. |
| **New safety‑critical function introduced** (e.g., autonomous treatment recommendation) | Escalate to senior regulatory lead and file a full 510(k) or PMA, as appropriate. |
| **Observed adverse event trend exceeding predefined threshold** | Initiate **Medical Device Reporting** per 21 CFR §803; consider Field Safety Corrective Action (FSCA). |
| **PCCP parameters exceeded** (e.g., number of allowable updates per year) | Review with cross‑functional change board; seek FDA concurrence if outside pre‑approved plan. |

---

### 6. Citations  

- FDA *Predetermined Change Control Plan* Guidance, Dec 2024 – established reference for PCCP terminology and requirements.  
- 21 CFR §807 (Premarket Notification) – classification & submission pathway.  
- 21 CFR Part 820 (Quality Management System Regulation, effective Feb 2026).  
- 21 CFR Part 830 (Unique Device Identification).  
- IEC 62304 (Software Life‑Cycle Processes).  
- ISO 14971 (Medical Device Risk Management).  

*No case‑level identifiers (e.g., specific 510(k) numbers, registration IDs) were present in the source excerpts; verify separately if needed.*

---

### 7. Peer Review Prompt  

> **@RA‑Peer:** Please challenge the assumptions made regarding device classification, the completeness of the PCCP scope derived from the limited excerpt, and any jurisdictional gaps (e.g., EU AI Act alignment). Confirm whether additional FDA guidance documents (e.g., Software as a Medical Device (SaMD) Action Plan) should be incorporated.  

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

1. Chunk `126806950873507800`

> > 참고: 사내 자매문서 `03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md` v0.3는 §3에서 "FDA PCCP Guidance 2024" 및 §4 용어표 "PCCP — Predetermined Change Control Plan"로 정확히 최종본을 인용하고 있어, 본 문서만 노후 인용 상태가 단절되어 있다.

2. Chunk `18243842993399443`

> ## Tier 2 (보조 — 범위 가늠용) - King & Spalding alert "FDA Publishes Final Predetermined Change Control Plan Guidance for AI-Enabled Device Software Functions" (2024-12) - Ropes & Gray, McDermott+ 알림(최종본 발행일 2024-12-03 확인용)

### kb-eval-20260721-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_us-003", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "cf8bb91ec17cae85", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

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

| Item | Assessment |
|------|------------|
| **Device type / Intended Use (derived from source)** | *AI‑enabled software that performs diagnostic or treatment‑support functions* (SaMD). The source references a “PCCP for AI‑Enabled DSF” and a “Human‑AI workflow,” indicating the software directly influences clinical decisions. |
| **Regulatory class** | • Determine class by reviewing the FDA product classification database for the specific intended use. <br>• Most diagnostic/clinical decision‑support SaMD are **Class II**, requiring a 510(k) (21 CFR §807). <br>• If no predicate exists or the software incorporates novel AI/ML functions that change risk, consider **De Novo** classification (21 CFR §814). |
| **Primary submission pathway** | 1. **510(k) – Traditional/Substantial‑Equivalence** if a suitable predicate is identified. <br>2. **De Novo** if no predicate or the AI/ML features present new risk. <br>3. Include a **Predetermined Change Control Plan (PCCP)** as part of the marketing submission per FDA’s final guidance (December 2024). |
| **Key evidence required for submission** | • **Algorithm performance data** – train/tune/test split with documented data provenance (source excerpt 1). <br>• **Clinical claim linkage** – demonstrate how performance translates to clinical benefit. <br>• **Bias analysis & mitigation** – quantitative bias assessment, methodology for mitigation (excerpt 1). <br>• **Human‑AI workflow validation** – usability/ human factors testing showing the clinician’s role and decision authority. <br>• **Post‑market monitoring plan** – real‑world performance surveillance, adverse event reporting, periodic re‑evaluation (excerpt 1). <br>• **PCCP documentation** – pre‑authorized change scope, change impact analysis matrix, procedures for implementing updates (excerpt 2). |
| **Missing information that must be supplied** | 1. **Exact intended use statement** (diagnostic, screening, monitoring, etc.). <br>2. **Device description** – algorithm type, data inputs, output format. <br>3. **Predicate device(s)** (if pursuing 510(k)). <br>4. **Risk classification rationale** – reference to FDA product code or classification rule. <br>5. **Labeling & UDI strategy** – plan for compliance with 21 CFR §§801 and 830. <br>6. **Cybersecurity controls** – threat model, mitigation, update mechanisms. |
| **Risk control measures (per FDA & IEC guidance)** | • **Software hazard analysis / risk management** – IEC 62304–based process incorporated into QMSR (21 CFR §820). <br>• **Bias detection & monitoring** – statistical thresholds; trigger for human review if bias exceeds pre‑set limits. <br>• **Human factors engineering** – IEC 62366‑1 compliance to ensure safe Human‑AI interaction. <br>• **Cybersecurity** – FDA’s “Content of Premarket Submissions for Management of Cybersecurity” guidance (2022) and the 2024 AI/ML guidance on secure model updates. <br>• **Change‑control limits in PCCP** – only pre‑approved parameter adjustments, algorithm architecture changes, or training data expansions are allowed without additional FDA review. |
| **Citations (established references)** | • **21 CFR §807** – Premarket notification (510(k)) requirements. <br>• **21 CFR §814** – PMA & De Novo pathway. <br>• **21 CFR §820** – Quality System Regulation, including the 2026‑02 QMSR amendment aligning with ISO 13485. <br>• **FDA “Predetermined Change Control Plan (PCCP) for AI/ML‑Based SaMD” Guidance**, Dec 2024. <br>• **FDA “Artificial Intelligence/Machine Learning (AI/ML)–Based Software as a Medical Device – Action Plan”** (Feb 2023) – provides the framework for bias analysis and post‑market monitoring. |
| **Citations (case‑level identifiers)** | No specific 510(k), predicate, or registration numbers appear in the source excerpts — verify separately. |
| **Human‑escalation triggers (when to pause a change & seek FDA review)** | 1. **Change outside PCCP scope** – e.g., new model architecture, different training data domain, or altered intended use. <br>2. **Detected bias exceeding pre‑defined limits** in real‑world performance monitoring. <br>3. **Adverse event signal rate surpasses post‑market safety thresholds** (per §803). <br>4. **Cybersecurity breach impacting model integrity**. <br>5. **Significant degradation of performance metrics** compared to baseline validation data. |
| **Action items for sponsor** | 1. Finalize intended use and perform predicate search; document classification decision. <br>2. Assemble the PCCP (scope, change matrix, verification plan). <br>3. Generate bias analysis report and define quantitative trigger values. <br>4. Develop Human‑AI workflow validation protocol with human factors testing. <br>5. Draft post‑market surveillance (PMS) plan aligned to FDA’s AI/ML PMS recommendations. <br>6. Ensure QMSR compliance (ISO 13485–aligned) for software development and change control. |
| **Regulatory judgment** | Assuming a Class II intended use with an acceptable predicate, the **fastest credible route is a 510(k) submission that incorporates a fully documented PCCP**. If no suitable predicate exists or the AI features fundamentally alter risk, pursue a **De Novo** pathway with the same evidentiary package plus a more extensive clinical validation dataset. All required evidence (performance, bias mitigation, human‑AI workflow, post‑market monitoring, change control) must be compiled before filing. |

---

### Peer Review Prompt
> @RA‑Peer: Please examine the assumptions above regarding classification, the completeness of the evidentiary list, and any jurisdiction‑specific gaps (e.g., state‑level telehealth regulations, EU MDR cross‑reference). Highlight any missing FDA guidance citations or alternative pathways that might better suit a novel AI‑enabled SaMD.

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

### kb-eval-20260721-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "4fa2b22fa435c19b", "source": "github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md", "source_hash": "a622ee7076c4fd98e60854417742c547284a2a3b0d82065d9b4e2a9da67c1fab"} -->

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

> **Regulatory Draft – SaMD (hardware‑software) change impact assessment**

---

### 1. Device classification & submission pathway  
| Item | Determination | Regulatory reference |
|------|---------------|-----------------------|
| **Device class** | **Class II** – hardware subject to IEC 60601 safety standards and software that performs diagnostic or therapeutic functions (no known predicate in source). | 21 CFR §892.2050 (if imaging‑software) *or* 21 CFR §807 (general 510(k) pathway). |
| **Submission route** | Traditional **Premarket Notification (510(k))** – needs substantial equivalence to a legally marketed predicate or, if none exists, a **De Novo** classification request. | 21 CFR §807.92; FDA Guidance on De Novo Classification (2023). |
| **Quality‑system regulation** | Apply the new **QMSR (ISO 13485‑aligned)** effective 02‑Feb‑2026. | 21 CFR Part 820 (as revised by QMSR). |

---

### 2. Evidence required (per FDA RTA checklist)

| Clause | Required evidence | Source citation |
|--------|-------------------|-----------------|
| **C.3 – Electrical safety** | • Test report confirming compliance with **IEC 60601‑1** (basic safety) <br>• EMC test report meeting **IEC 60601‑1‑2** | FDA‑510K‑C3 (must) |
| **C.4 – Software (major LoC)** | • IEC 62304 software development lifecycle documentation (plan, requirements, architecture, verification & validation) <br>• FDA “Software Guidance” deliverables (risk analysis, traceability matrix) <br>• Cybersecurity plan/assessment aligned with FDA’s December 2024 **Predetermined Change Control Plan (PCCP)** guidance | FDA‑510K‑C4 (must) |
| **E.1 – Labeling** | • Draft labels and Instructions for Use (IFU) covering intended use, contraindications, warnings, etc. <br>• Alignment with 21 CFR §801 labeling requirements | FDA‑510K‑E1 (must) |
| **E.2 – UDI compliance** | • UDI implementation plan identifying GS1 or HIBCC issuing agency, carrier placement, and submission to GUDID | FDA‑510K‑E2 (must) |

---

### 3. Missing / incomplete information that must be supplied  

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Predicate device identification** (if pursuing 510(k)) | Needed to establish substantial equivalence; without it the submission cannot proceed or would trigger a De Novo pathway. | Conduct market search, document predicate’s 510(k) number and comparison matrix. |
| **Intended use statement & indications** | Determines risk class, applicable special controls, and required performance data. | Draft precise intended‑use language; map to FDA device classification database. |
| **Clinical/bench performance data** (e.g., accuracy, sensitivity, specificity) | Demonstrates that the new device performs at least as well as predicate or meets safety/effectiveness criteria for De Novo. | Design and execute verification/validation studies; include statistical analysis. |
| **Risk Management File (ISO 14971)** | Links identified hazards to risk controls; required for both 510(k) and QMSR compliance. | Produce hazard analysis, risk evaluation, mitigation traceability, residual‑risk report. |
| **Software Bill of Materials (SBOM)** | Mentioned in C.4 keywords (“FDA SBOM”); supports supply‑chain transparency and cybersecurity. | Generate SBOM per NIST SP 800‑161 and attach to submission. |
| **Cybersecurity Threat Model & Mitigations** | Required under FDA’s PCCP guidance for AI/ML‑enabled SaMD; informs post‑market monitoring. | Prepare threat analysis, mitigation strategy, and update plan. |
| **Final labeling (including UDI carrier)** | Draft only; final labels must meet 21 CFR §801 and UDI placement rules. | Complete label artwork, place UDI on device label and packaging, submit to GUDID. |
| **Device master record (DMR) & Device history record (DHR)** | Required under QMSR for traceability of hardware and software releases. | Establish DMR/DHR in compliance with 21 CFR Part 820. |

---

### 4. Core risk controls (mapping to standards)

| Hazard | Control(s) | Reference |
|--------|------------|-----------|
| Electrical shock / fire | IEC 60601‑1 safety requirements; protective earth, leakage current limits | IEC 60601‑1 |
| Electromagnetic interference | IEC 60601‑1‑2 EMC testing; shielding, filtering | IEC 60601‑1‑2 |
| Software malfunction (e.g., incorrect diagnosis) | IEC 62304 development process with appropriate software safety class; verification & validation tests; traceability matrix | IEC 62304 |
| Cybersecurity breach / unauthorized access | PCCP‑based change‑control plan; threat model, encryption, authentication, periodic security updates | FDA “Predetermined Change Control Plan (PCCP)” guidance Dec 2024 |
| Residual risk to patient | ISO 14971 risk management process; residual‑risk acceptance criteria documented | ISO 14971 |
| Misuse due to labeling errors | Comprehensive IFU, warnings, contraindications; human factors validation of label comprehension | 21 CFR §801 |

---

### 5. Human‑escalation triggers (when a senior RA or regulatory manager must intervene)

| Trigger | Reason for escalation |
|--------|------------------------|
| **No suitable predicate identified** after market search | Requires decision on De Novo request versus alternative pathway. |
| **Clinical performance data insufficient** to show equivalence or safety | May need additional studies, affecting timeline and budget. |
| **Risk analysis shows residual risk > acceptance criteria** | Needs redesign, additional controls, or re‑classification evaluation (possible PMA). |
| **UDI plan lacks carrier specification or GUDID submission schedule** | Non‑compliance with 21 CFR §830 could delay clearance. |
| **Software change scope exceeds PCCP limits** (e.g., new intended use) | Must submit a supplemental 510(k) or possibly a new 510(k). |
| **Labeling draft fails FDA 21 CFR §801 review** (missing warnings, unclear instructions) | Requires label redesign and regulatory sign‑off. |
| **QMSR gaps uncovered during internal audit** (e.g., missing DMR/DHR records) | Immediate corrective actions and possible FDA inspection risk. |

---

### 6. Summary judgment  
- The device is a **Class II SaMD with associated hardware**, requiring a **510(k) submission** supported by substantial‑equivalence data or, if none exists, a **De Novo** request.  
- Core evidentiary blocks are test reports for IEC 60601‑1/−1‑2, IEC 62304 software documentation (including SBOM and cybersecurity plan), full labeling package with UDI compliance, and a complete ISO 14971 risk‑management file.  
- Several critical items remain unavailable in the source material (predicate ID, performance data, final labels, detailed risk analysis) and must be generated before dossier assembly.  

**Human escalation:** Any of the triggers listed in Section 5 should be routed to a senior RA lead for decision making prior to submission.

---

### 7. Peer‑review request  
> *Please review: (a) classification assumption (Class II vs. potential Class I or III); (b) completeness of required evidence given the limited source excerpts; and (c) any jurisdiction‑specific gaps (e.g., state‑level medical device statutes, post‑market surveillance obligations) that have not been addressed.*

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

### kb-eval-20260721-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_us-005", "iteration": 2, "matched_keywords": ["FDA", "QMSR"], "profile_id": "ra-us", "scenario_id": "42bb8106a16a154f", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md", "source_hash": "7ca9af1c0868e79088fc661437836691edc3b33a8f372cb1dd166d71ca1752a1"} -->

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

> **Regulatory Draft – X‑ray Imaging System (SaMD‑enabled)**  

---

### 1. Classification & Submission Route  
| Item | Determination |
|------|----------------|
| **Device family** | Radiology / imaging equipment (X‑ray system) → **21 CFR Part 892** (Imaging devices). |
| **Class** | Class II (most conventional X‑ray, fluoroscopy and digital radiography systems are predicate‑listed as Class II). |
| **Regulatory pathway** | **510(k) Premarket Notification** – substantial equivalence to an existing cleared X‑ray system. No de Novo indication is apparent from the source. |
| **Key predicate data needed** | - Predicate 510(k) number, product code and regulation number (e.g., “XRL”). <br> - Comparison of technological characteristics, performance specs, and intended use. <br> *No specific identifier found in source – verify separately.* |

---

### 2. Core Evidentiary Requirements  

| Requirement | Evidence to be submitted |
|-------------|--------------------------|
| **Device Description & Intended Use** | Detailed description, clinical indications, user environment, SaMD functionalities (image processing, AI‑based analysis if applicable). |
| **Substantial Equivalence Comparison** | Side‑by‑side table covering hardware, software, radiation output, safety features, labeling. |
| **Performance Testing** | • Radiation dose & image quality (IEC 60601‑2‑22 compliance) <br>• Software verification/validation (including IEC 62304, FDA guidance on SaMD) <br>• Electromagnetic compatibility (IEC 60601‑1‑2). |
| **Risk Management** | ISO 14971 risk analysis & FMEA; identification of residual risks and mitigations. |
| **Quality System Evidence** | • **21 CFR §820.30** Design Controls documentation <br>• **§820.35** Record‑keeping (see Section 3) <br>• Production & Process Controls (§820.50) <br>• Post‑market Surveillance Plan (§820.100 series). |
| **UDI Compliance** | Label & packaging bearing a UDI per **21 CFR §830.10–§830.60**; submission of device identifier to GUDID. |
| **Medical Device Reporting (MDR)** | MDR procedures and reporting forms compliant with **21 CFR §803**. |
| **Electronic Records** | Validation of any electronic record system per **21 CFR Part 11**. |
| **Software Change‑Control (if SaMD updates are planned)** | Predetermined Change Control Plan (PCCP) as required by the FDA Dec 2024 guidance on AI/ML‑based devices. |
| **Labeling** | Full labeling package (USPI, IFU, safety warnings) meeting **21 CFR §801**. |

---

### 3. Record‑Keeping Gap Highlight – FDA QMSR §820.35 vs ISO 13485 §4.2.5  

*Source excerpt*: “ISO 13485 §4.2.5(기록의 관리)는 기본 요건이며, FDA는 §820.35에서 추가 요건을 부과” (Excerpt [1]).  

**Implication:** Satisfying ISO 13485 §4.2.5 alone is **insufficient** for U.S. market clearance; the device must also meet the **additional record‑keeping obligations** imposed by **21 CFR §820.35** (e.g., retention periods, traceability of calibration records, incident logs, complaint handling).  

**Action items:**  
1. Map existing ISO 13485 record‑control SOPs to each FDA‑specific requirement in §820.35.  
2. Confirm that all required records (design history, manufacturing lot traceability, software version control, calibration & maintenance logs) are retained for **minimum 2 years** after the last device is distributed, or as otherwise mandated by the regulation.  
3. Update SOP‑FSC‑A001 (Document Control) and SOP‑TRC‑A002 (Record Retention) to explicitly address the FDA additions.  

*No specific identifier (e.g., SOP number) appears in the source beyond “F‑QMSR‑REC‑001”, which should be incorporated as the controlling procedure.*  

---

### 4. Missing Information & Follow‑up Needs  

| Gap | Required clarification / evidence |
|-----|------------------------------------|
| **Predicate device details** | Exact 510(k) number, product code, and regulatory classification. |
| **Intended use wording** | Precise claim language (e.g., “diagnostic X‑ray imaging of skeletal structures”). |
| **SaMD algorithm description** | If AI/ML is used, need algorithm training dataset, performance metrics, and PCCP scope. |
| **Clinical data** | Any user‑clinical study or bench‑to‑clinical correlation supporting safety/effectiveness. |
| **Radiation safety testing reports** | Dose measurements (DAP, air kerma) per FDA radiation protection regulations. |
| **Cybersecurity plan** | If system connects to network/EHR, a documented risk mitigation strategy is required. |
| **UDI carrier format** | Confirmation of barcode/QR code compliance and GUDID submission data set. |

*All items above are absent from the supplied excerpts; they must be obtained from product development files or planned activities.*  

---

### 5. Risk Controls (Key FDA‑referenced Elements)

1. **Design Controls – §820.30**  
   * Design input, output, verification, validation, design transfer, change control.  

2. **Record Keeping – §820.35** *(see Section 3)*  

3. **Production & Process Controls – §820.50**  
   * Process validation for image acquisition chain; calibration frequency.  

4. **Corrective & Preventive Action (CAPA) – §820.100**  

5. **Post‑Market Surveillance – §820.120**  

6. **Software Lifecycle – IEC 62304 + FDA AI/ML guidance (PCCP)**  

7. **UDI – §830.10–§830.60**  

8. **MDR – §803**  

9. **Electronic Records – Part 11**  

Each control should be documented in the QMS and cross‑referenced to the applicable SOPs.

---

### 6. Key Citations (Established Regulatory References)

| Reference | Relevance |
|-----------|-----------|
| **21 CFR Part 892** – Imaging devices | Device panel classification. |
| **21 CFR §820.35** – Record‑keeping | Additional U.S. record requirements beyond ISO 13485 §4.2.5. |
| **ISO 13485:2016 §4.2.5** – Management of Records | Baseline requirement (source [1]). |
| **21 CFR Part 830**, §§ 830.10–830.60 | UDI labeling & GUDID submission. |
| **21 CFR Part 803** | Medical Device Reporting obligations. |
| **21 CFR Part 11** | Validation of electronic records. |
| **FDA Guidance – Predetermined Change Control Plan (PCCP) (Dec 2024)** | Planned AI/ML updates. |
| **IEC 60601‑2‑22** – X‑ray equipment safety | Radiation performance testing. |
| **ISO 14971** – Risk Management for Medical Devices | Required risk analysis framework. |

*No case‑level identifiers were present in the source; thus none are inserted.*

---

### 7. Human‑Escalation Triggers  

| Situation | Who must be alerted & why |
|-----------|----------------------------|
| **Missing predicate 510(k) information** | RA Lead → cannot finalize substantial equivalence narrative. |
| **Inadequate mapping of ISO 13485 records to §820.35** | QMS Manager → risk of non‑compliance during FDA inspection. |
| **Unresolved SaMD algorithm change without PCCP** | Software QA / Regulatory → potential violation of AI/ML guidance. |
| **Incomplete radiation dose testing package** | Clinical Engineer → safety compliance gap. |
| **UDI carrier format fails GUDID validation** | Labeling Specialist → labeling deficiency. |
| **CAPA backlog > 30 days** | QA Director → FDA may cite deficiencies under §820.100. |
| **Any discrepancy flagged during internal audit of record‑keeping SOPs** | QA Lead → corrective action required before submission. |

All triggers should be logged in the project risk register and escalated per the organization’s escalation matrix.

---

### 8. Peer Review Prompt  

> **Request:** Please review this draft for (a) completeness of the 510(k) evidence checklist, (b) adequacy of the record‑keeping gap analysis linking ISO 13485 §4.2.5 to FDA §820.35, and (c) identification of any jurisdiction‑specific requirements that may have been omitted (e.g., radiation protection regulations, state‑level licensure). Highlight any assumptions that need verification or additional source material.

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

### kb-eval-20260721-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a0930f4828c4acbc", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

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

> **Regulatory Draft – Response to EU Notified Body Deficiency Letter (MDR)**  

---

### 1. Device Synopsis  
| Item | Description |
|------|-------------|
| **Intended purpose** | Standard diagnostic radiology (X‑ray imaging) for clinical examination of patients. |
| **Core technology** | X‑ray tube generator (radiation source), detector/image plate, image‑processing software that supplies diagnostic information. |
| **Key performance claim cited by NB** | Detective Quantum Efficiency (DQE) ≥ 65 % (IEC 62220‑1‑1). |

---

### 2. Classification & Conformity‑Assessment Route  

| Aspect | Determination | Regulatory basis |
|--------|---------------|------------------|
| **Device class** | **Class IIb** – active device that emits ionising radiation for diagnostic purposes. | **Rule 10** of Annex VIII (active devices for diagnosis/monitoring) applied to the X‑ray source; the presence of ionising radiation triggers the higher‑risk sub‑category which is Class IIb (Annex VIII, Rule 10). |
| **Conformity‑assessment route** | **Annex IX** – full quality‑management‑system assessment *plus* technical documentation review.  (Alternative Annex X + Annex XI possible but not selected.) | MDR, Annex IX (full QA + technical file) for Class IIb devices. |
| **Declaration of Conformity** | To be issued in accordance with **Annex IV** after successful assessment. | MDR, Annex IV. |

---

### 3. Mandatory Evidence Package (per MDR)

| Evidence | Content Required | Relevant MDR reference |
|----------|------------------|------------------------|
| **Technical Documentation** | Full device description, design & manufacturing information, labeling, UDI, GSPR compliance matrix. | Annex II. |
| **Risk Management File** | ISO 14971‑based risk analysis, evaluation of radiation hazards (§16), electronic/software hazards (§17), residual risk acceptance. | Annex I §§16‑18; Art 10/15 (risk management). |
| **Clinical Evaluation Report (CER)** – *updated* | State‑of‑the‑art literature review, clinical data demonstrating equivalence to predicate device, DQE test results (≥65 %). Current version **Rev. 3** attached as Annex A. | Annex XIV Part A; Art 61. |
| **Test Report – DQE** | IEC 62220‑1‑1 compliant measurement report (TR‑2024‑015) confirming DQE ≥ 65 %. | IEC 62220‑1‑1 (referenced in source). |
| **IEC Standards Conformity** | • IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy) <br>• IEC 60601‑2‑28 (X‑ray tube assemblies) <br>• IEC 62304 (software lifecycle) <br>• IEC 62366‑1 (usability) | Manufacturer’s declared compliance; referenced in GSPR §§16, 17, 18. |
| **Post‑Market Surveillance (PMS) System** | PMS plan (Art 84), PMS reports (Art 83 for Class I, Art 86 PSUR for Class IIb – annual). | Art 83‑86. |
| **PMCF Plan & Report** | Planned post‑market clinical follow‑up activities and interim findings to support ongoing benefit‑risk assessment. | Annex XIV Part B. |
| **Labeling & IFU** | Full label, instructions for use, safety information (radiation protection, warnings per IEC 60601‑2‑54 §16.4), UDI, CE marking. | Annex I §23; IEC 60601‑2‑54 §16.4. |
| **EU Declaration of Conformity** | Signed by the responsible person, referencing all above documentation. | Annex IV. |

---

### 4. Gaps Identified in NB Deficiency Letter  

| Gap | Required Action | Supporting source excerpt |
|-----|-----------------|---------------------------|
| **Clinical Evaluation Report (CER) – completeness** | Provide a *fully revised* CER (Rev. 3 attached) with explicit equivalence justification, literature review, and clinical data. Ensure the DQE claim is substantiated by the referenced test report. | Excerpt [1] – “Revised CER Rev. 3 is attached as Annex A.” |
| **Technical Documentation (TD)** | Supply missing sections: device description, labeling drafts, risk analysis updates, and conformity‑to‑standards declarations. | Excerpt [2] – “주요 결함 유형 … CER, TD, QMS NC, Labelin…” |
| **Quality Management System Non‑conformities (QMS NC)** | Close identified NCs; provide evidence of corrective actions, updated procedures and internal audit reports. | Same as above. |
| **Labeling** | Update label/IFU to reflect radiation safety (§16), software information (§17), and any new warnings per IEC 60601‑2‑54. | Excerpt [2] – “Labelin…” |
| **PMCF evidence** (if not already supplied) | Submit PMCF plan (Annex XIV Part B) and earliest interim report. | Implicit from NB focus on clinical data. |
| **PSUR** (annual for Class IIb) | Provide the latest Periodic Safety Update Report covering sales volume, adverse event summary, and benefit‑risk conclusions. | Art 86(2). |

*All missing items must be supplied **within 30 calendar days of NB request** to avoid escalation; this internal deadline is stricter than the “no statutory upper limit” noted in the Korean‐language table (excerpt [2]).*

---

### 5. Risk Controls & GSPR Alignment  

| GSPR § | Hazard / Control | Implementation evidence |
|--------|------------------|--------------------------|
| **§16 – Radiation protection** | Shielding design, interlocks, dose‑monitoring, compliance with IEC 60601‑2‑54 §§16.4 & 16.5. | Design verification reports, test data (DQE). |
| **§17 – Software** | Validation per IEC 62304, usability engineering per IEC 62366‑1, security assessments. | Software development lifecycle documentation, verification/validation logs. |
| **§18 – Active devices** | Electrical safety, electromagnetic compatibility, functional testing of X‑ray tube control logic. | IEC 60601‑2‑28 test reports, failure mode analysis. |
| **§20 – Mechanical / Thermal risks** | Structural integrity of housing, thermal overload protection. | Finite‑element analyses, temperature tests. |
| **§22 – Use by lay persons (if applicable)** | Clear user instructions, training modules, labeling warnings. | IFU usability testing results. |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger & Timeframe | Escalation path |
|-----------|--------------------|-----------------|
| **No response to NB request** (e.g., after 30 calendar days) | Alert Senior RA Manager; initiate internal “non‑response” protocol. | RA Manager → Head of Regulatory Affairs. |
| **Repeated QMS non‑conformities (>2)** | Immediate escalation to Quality Director and consider suspension of release activities. | QA Director → CEO (if impact on market launch). |
| **Insufficient clinical data** (e.g., DQE test missing or below 65 %) | Trigger feasibility review for additional bench testing; may require redesign. | Project Lead → Engineering lead. |
| **NB issues an “Evaluation termination / non‑approval”** | Immediate legal review and decision on market withdrawal or remediation plan. | Legal counsel → Board. |

---

### 7. Summary Judgment  

- The device is a **Class IIb active diagnostic X‑ray system** under **Rule 10 (Annex VIII)**.  
- The appropriate conformity‑assessment route is **Annex IX** (full QMS + technical file).  
- The NB deficiency concerns **clinical evidence, technical documentation, QMS non‑conformities and labeling**; all items listed above must be supplied to achieve a positive assessment.  

---

### 8. Peer‑Review Request  

> *Colleague RA, could you please review the following points:*  
> - Adequacy of the classification (Rule 10) given the system’s software component – should any sub‑module be considered under Rule 11?  
> - Completeness of the evidence list for a Class IIb X‑ray device (any additional standards or guidance not captured?).  
> - Whether the 30‑day internal response deadline aligns with typical NB practice in Europe, given the “no statutory upper limit” noted in excerpt [2].  

Your challenges will help confirm no jurisdictional gaps remain.

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

### kb-eval-20260721-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "0150a731e2233f91", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

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

> **Regulatory Draft – Diagnostic X‑ray System (EU MDR)**  

---

### 1. Device classification & conformity‑assessment route  
| Item | Determination | Regulatory basis |
|------|---------------|------------------|
| **Primary device** – X‑ray generator / tube assembly (diagnostic use) | **Class IIb** – active device that *emits ionising radiation for diagnostic purposes* | Rule 10 of Annex VIII → Class IIb (source [2]) |
| **Secondary device** – Digital flat‑panel detector (records the image) | **Class IIa** – active device intended solely for recording diagnostic images | Rule 17 of Annex VIII → Class Ia (source [2]) |
| **Software component** (image‑processing / display) | **Class IIa** (unless it directly influences a therapeutic decision) | Rule 11 of Annex VIII (standard MDR rule) |
| **Conformity‑assessment route for the Class IIb X‑ray system** | **Annex IX** (full quality‑management system + technical documentation assessment) – *or* **Annex X** (type‑examination) followed by **Annex XI** (production conformity verification) if the manufacturer opts for a type‑exam route. | MDR Annex IX / X / XI (overall MDR scheme) |
| **Conformity‑assessment route for the Class IIa detector & software** | **Annex IX** (QMS‑based) – acceptable; Annex X also permissible but generally unnecessary for Class IIa. | MDR Annex IX / X |

*Note:* The source erroneously mapped “EU MDR Rule 5/9” to the diagnostic system (source [2]). Correct mapping is **Rule 10 → Class IIb**. This mis‑classification would lead to an incorrect conformity route and PSUR schedule.

---

### 2. Evidence required for NB submission  

| Area | Required artefacts | MDR reference |
|------|-------------------|---------------|
| **Technical documentation** (device description, labeling, intended purpose, classification justification) | • Full device hierarchy (system, detector, software) <br>• Classification justification citing Rule 10 (or Rule 17/11) | Annex II; classification justification – Annex VIII |
| **Risk management file** | • ISO 14971‑compliant risk analysis & evaluation <br>• Risk control measures for radiation exposure, fail‑safe interlocks, software hazards | Annex I §16.4 (radiation), §18 (active devices), §17 (software) |
| **Clinical Evaluation Report (CER)** | • State‑of‑the‑art literature review <br>• Clinical data demonstrating safety & performance for diagnostic X‑ray use <br>• PMCF plan/evaluation (Annex XIV Part B) | Annex XIV Part A; Art. 61 |
| **Post‑Market Surveillance (PMS) system** | • PMS plan (Art. 84) <br>• PSUR (Class IIb – annual) (Art. 86) | Art. 83–86 |
| **Standard compliance evidence** | • IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy) <br>• IEC 60601‑2‑28 (X‑ray tube assemblies) <br>• IEC 62220‑1‑1 (DQE, detector performance) if applicable <br>• IEC 62366‑1 (usability) <br>• IEC 62304 (software lifecycle) | Standard references – no MDR citation needed |
| **Quality Management System** | • ISO 13485 certificate (or equivalent) supporting Annex IX route | Annex IX |
| **Labeling & IFU** | • Conformity to Annex I Chapter III §23 (information supplied with the device) | Annex I §23 |

---

### 3. Missing / insufficient information identified  

1. **Intended‑purpose statement** – Must explicitly state “diagnostic use only; no therapeutic radiation emission” to exclude Rule 9 (source [1] confirms that therapeutic devices fall under Rule 9).  
2. **Device breakdown** – Clear delineation of system, detector, and software as separate sub‑devices with their own classifications.  
3. **Evidence of compliance with IEC 60601‑2‑54 / 60601‑2‑28** – Not mentioned in the source; required for an active X‑ray device.  
4. **Clinical data package** – The source only provides a classification correction; no clinical investigation or literature review evidence is supplied.  
5. **Risk analysis specific to radiation dose management** – Needed to satisfy GSPR §16.4, but not present in the excerpt.  
6. **PMS/PSUR schedule** – Must be defined for Class IIb (annual PSUR) per Art. 86(2).  

Until these items are provided, the NB cannot complete the conformity assessment.

---

### 4. Key risk controls to be demonstrated  

| Hazard | Control measure | MDR/GSPR citation |
|--------|----------------|-------------------|
| **Uncontrolled radiation dose** | • Automatic exposure control (AEC) <br>• Interlock systems & shielding <br>• Dose monitoring & display on UI | GSPR §16.4; IEC 60601‑2‑54 |
| **Failure of X‑ray generation** | • Redundant high‑voltage supply <br>• Self‑test and error reporting | GSPR §18 |
| **Software mis‑interpretation of images** | • IEC 62304 development lifecycle <br>• Validation of image processing algorithms <br>• Usability testing per IEC 62366‑1 | GSPR §§17, 23 |
| **Mechanical/thermal risks** | • Design safeguards for tube overheating <br>• Mechanical integrity checks | GSPR §20 |
| **Use by lay persons (if intended)** | • Clear labeling & user instructions; training program | GSPR §22 |

All controls must be documented in the risk‑management file and reflected in the design dossier.

---

### 5. Regulatory citations  

* Classification rules – Annex VIII, Rule 9 (source [1]), Rule 10 & Rule 17 (source [2])  
* General Safety & Performance Requirements – Annex I §§16.4, 17, 18, 20, 22, 23  
* Technical documentation – Annex II  
* Clinical evaluation – Annex XIV Part A (Art. 61) & Part B (PMCF)  
* Post‑market surveillance – Art. 83–86 (PMS system, plan, PSUR)  
* Conformity‑assessment routes – Annex IX / X / XI  

*Specific identifiers found in source:* FDA 510(k) **Product Code MQB** (source [2]) – note this is an example mapping; verify separately for the actual device.

---

### 6. Human‑escalation triggers  

| Trigger | Action |
|--------|--------|
| **Unclear intended purpose** (cannot unequivocally exclude therapeutic radiation) | Escalate to RA team lead for wording revision before NB submission. |
| **Absence of IEC 60601‑2‑54/‑2‑28 compliance evidence** | Notify design engineering; obtain test reports before dossier finalisation. |
| **Insufficient clinical evidence for Class IIb** (no literature review or investigational data) | Initiate senior clinical expert review and possibly conduct a prospective clinical investigation. |
| **Risk‑management file does not cover radiation dose controls** | Raise to risk‑management lead; request additional hazard analysis & mitigation documentation. |
| **Mismatch between MFDS/FDA classification and MDR (Rule 5/9 used)** | Pause submission; update CE‑marking plan with correct Rule 10 mapping; inform NB of correction. |
| **PMS/PSUR schedule not defined** | Assign PMS coordinator to draft the PSUR calendar (annual for Class IIb) and submit for approval. |

When any trigger occurs, the responsible RA must document the issue in the CE‑marking project tracker and seek explicit sign‑off before proceeding.

---

### 7. Peer‑review request  

> **To:** [RA peer]  
> **Subject:** Challenge of classification & evidence assumptions (Diagnostic X‑ray system)  
> Please review the above draft, focusing on:  
> 1. Completeness of the classification justification using Rule 10 vs. any residual applicability of Rule 9 or Rule 5.  
> 2. Whether all MDR‑required standards and GSPR clauses have been captured for this device family.  
> 3. Any jurisdiction‑specific gaps (e.g., interplay with FDA 510(k) Product Code MQB, Korean MFDS grade) that may affect the EU submission strategy.  

Your feedback will be incorporated before finalising the NB response package.

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

### kb-eval-20260721-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "f8d5b8306505bb1d", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f8d5b8306505bb1d`
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

> **Regulatory Draft – Preliminary MDR Assessment (No specific device disclosed)**  

---

### 1. Device Classification  

| Item | Regulatory basis | Comment / Evidence needed |
|------|------------------|---------------------------|
| **Classification responsibility** | Manufacturer self‑classifies under **Article 51** and applies the sequential rules of **Annex VIII** – highest rule that fits determines the class (source [2]) | Identify which Annex VIII rule(s) apply to the device (e.g., Rule 9, 10, 11, 17, …). If uncertainty remains, seek clarification from the Competent Authority or consult the MDCG “Borderline and Classification” Manual (latest v2.1.1, Sep‑2023). |
| **Resulting class** | – | *Missing*: explicit device description, intended purpose, mode of action → cannot assign a rule/class at this stage. |

---

### 2. Conformity‑Assessment Route  

The route follows the class identified in § 1:

| Class (tentative) | Applicable Annex for assessment | Typical NB deliverables |
|-------------------|---------------------------------|--------------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration; technical documentation filed in EUDAMED (no NB involvement). |
| **Class IIa / IIb** | **Annex IX** – QMS (ISO 13485) + assessment of the full Technical Documentation by a Notified Body. |
| **Class III** | **Annex X** – Type‑examination of the device; subsequent **Annex XI** production conformity verification is required for each manufacturing site. |

*Human escalation*: if classification lands on IIa/IIb/III, a formal NB contract must be initiated; finance sign‑off needed (see § 8).

---

### 3. Technical Documentation – Core Evidence Required  

| Document | MDR reference | Typical content |
|----------|---------------|-----------------|
| **Device description & intended use** | Annex II, § 2 | Indications, contraindications, patient population, mode of action. |
| **Risk Management File** | ISO 14971 (Annex I §§ 16‑22) | Risk analysis, risk control measures, residual risk evaluation. |
| **Clinical Evaluation Report (CER)** | **Annex XIV Part A** & **Art. 61** (source [1]) | State‑of‑the‑art analysis, clinical data (literature, PMS, clinical investigations). |
| **PMCF Plan & Report** | **Annex XIV Part B** | Planned post‑market clinical follow‑up activities and results. |
| **Post‑Market Surveillance (PMS) System** | **Art. 83** – system description; **Art. 84** – PMS plan; **Art. 86** – PSUR for Class IIa/IIb/III. |
| **Labeling & IFU** | Annex I § 23 | Labels, instructions for use, symbols, UDI format. |
| **Declaration of Conformity** | Annex IV | Signed by Manufacturer/Authorized Rep (Art. 11). |
| **EUDAMED entries** | Art. 33‑39 | Device registration, UDI‑Device & UDI‑Pack, certificates, vigilance records. |

---

### 4. Clinical Evidence  

1. **State‑of‑the‑Art (SOTA) literature review** – must cover devices with the same intended purpose and risk profile (no specific identifiers found in source — verify separately).  
2. **Clinical Investigation data** – if no sufficient equivalence, a prospective study is required (per MDR “clinical evidence” principle).  
3. **PMCF** – ongoing plan to collect real‑world performance data; results feed into the periodic safety update report (PSUR) for Classes IIa/IIb/III (Art. 86).  

*Missing*: concrete clinical data sources, investigational protocol, and PMCF timeline.

---

### 5. Post‑Market Surveillance Requirements  

| Requirement | MDR citation | What must be produced |
|-------------|--------------|-----------------------|
| **PMS system** | Art. 83 | SOPs for complaint handling, trend analysis, field safety corrective actions (FSCA). |
| **PMS plan** | Art. 84 | Annual updating schedule, trigger levels for PSUR updates. |
| **PSUR** (for Class IIa/IIb/III) | Art. 86(1‑2) – includes benefit‑risk conclusions, PMCF main findings, sales volume & user population. | *Missing*: draft PSUR outline and data sources. |
| **Vigilance reporting** | Art. 87 | Incident report to Competent Authority within 15 days (serious). |

---

### 6. UDI & EUDAMED  

- **UDI assignment** – via national portal or GUDID as appropriate (source [1] lists “UDI 포털”, “GUDID”).  
- **EUDAMED registration** – device, certificates, vigilance events, and PSUR entries (Art. 33‑39).  

*Missing*: UDI carrier type, issuing agency, entry dates.

---

### 7. Authorized Representative & Importer  

| Role | MDR provision | Notes |
|------|---------------|-------|
| **Authorized Representative** | **Art. 11** – must be established in the EU and act on behalf of the Manufacturer. | Identify name, address, POA. |
| **Importer (Domestic)** | Must hold a valid import licence (Korean “수입자” referenced) but under MDR the importer must verify CE marking and keep a copy of the DoC. |

*Missing*: AR and Importer details; their contractual agreements.

---

### 8. Fees & Economic Considerations  

- **NB fees** – €10 k‑€100 k+ (source [1]).  
- **US FDA MDUFA IV fees** listed for reference only (not MDR‑relevant).  

*Human escalation*: finance sign‑off required before NB engagement.

---

### 9. Identified Gaps / Missing Information  

| Gap | Impact on Submission |
|-----|----------------------|
| Device’s intended purpose, indications & mode of action | Prevents rule selection → classification cannot be finalised. |
| Technical specifications (materials, energy source) | Needed for risk analysis and to determine applicable Annex I §§ 16‑18. |
| Clinical data sources (literature, investigations, registries) | CER cannot be compiled; NB will request evidence. |
| PMCF plan details (study design, endpoints, duration) | PSUR & ongoing compliance depend on it. |
| Authorized Representative name & POA | Required for the EU Declaration of Conformity (Art. 11). |
| UDI allocation strategy (carrier type, issuing agency) | Mandatory for EUDAMED registration and market placement. |
| PMS system SOPs & complaint handling workflow | Needed to demonstrate compliance with Art. 83‑84. |

---

### 10. Risk Management Summary  

- **Risk analysis** must address all relevant GSPRs:  
  - § 16 (radiation protection, if applicable)  
  - § 17 (software, if any)  
  - § 18 (active device aspects)  
- Apply ISO 14971 process; link each residual risk to a control measure documented in the Technical File.  

*Missing*: Hazard list, risk control measures, verification/validation results.

---

### 11. Human‑Escalation Triggers  

| Situation | Who must be alerted | Reason |
|-----------|--------------------|--------|
| **Unclear classification** (no rule can be confidently applied) | Senior Regulatory Lead & Competent Authority liaison | To obtain a definitive classification decision per Article 51/Annex VIII. |
| **Insufficient clinical evidence** (no comparable devices, no investigations) | Clinical Affairs Manager & Project Sponsor | Halt submission until data gap closed; risk of NB non‑acceptance. |
| **Absence of Authorized Representative** | Legal/Compliance Officer | Cannot sign the EU Declaration of Conformity (Art. 11). |
| **PMS system not operational** | Quality Management System Owner | Non‑compliance with Art. 83 may lead to market withdrawal. |
| **Budget exceedance (>€100 k NB fee)** | Finance Director & Project Steering Committee | Required before contract signing with the NB. |
| **Adverse event trend exceeding trigger thresholds** | Vigilance Coordinator & Top Management | Mandatory FSCA under Art. 87; must be reported within 15 days. |

---

### 12. Peer‑Review Prompt  

> *Please review this preliminary MDR assessment and challenge the following points:*  
> 1. **Classification assumption:** Have we considered all relevant Annex VIII rules (including borderline cases) for this device type?  
> 2. **Evidence completeness:** Are there any additional data sources (e.g., post‑market registries, real‑world evidence) that should be factored into the CER/PMCF at an earlier stage?  
> 3. **Jurisdictional gaps:** Does the draft adequately address interactions with non‑EU requirements (e.g., Korean import licence, US FDA exemptions) or are there cross‑border regulatory risks we have omitted?  

--- 

*End of Draft.*

<!-- verification-summary -->

**🔎 기계 검증 요약** (우선순위 107/190 · 자동 생성, 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,249자 | — |
| 규제 식별자 인용 | 18개 | — |
| excerpt 근거 일치 | **7/18 (38%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 식별자 | 11개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |
| 근거 인용 표현 | 있음 | `Source cited` |

**근거 대조 위험도: 중간**

**excerpt에서 확인되지 않은 인용**: `Annex IX`, `ISO 13485`, `Annex II`, `ISO 14971`, `Annex I`, `Art. 61`, `Art. 83`, `Art. 84`, `Art. 86`, `Annex IV`, `Art. 33`

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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20260721-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d79652410a251d37", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "209487b4b22e96052be65198c3a3ed54cef6303dd563722b36bf9c98910a1cf9"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d79652410a251d37`
- Source: `github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/04_%EC%9C%A0%EB%9F%BD_MDR/EU_MDR_2017_745.md)
- Source hash: `209487b4b22e96052be65198c3a3ed54cef6303dd563722b36bf9c98910a1cf9`
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

> **Regulatory Draft – Response to Notified Body Query**

---

### 1. Scope of the request  

The NB has asked for clarification on the **classification and conformity‑assessment route**, together with the **evidence bundle** that must be submitted. The only source material provided describes internal procedures for preparing the Technical Documentation (TD) and the responsibilities of Economic Operators under MDR Articles 10, 11, 13 and 14. No device‑specific information (name, intended purpose, patient population, mode of action, etc.) is present in the excerpt.

Because classification cannot be derived without a clear description of the device’s intended medical purpose and operating principles, the draft below outlines:

* the **information that must still be supplied** before a definitive MDR classification can be assigned;  
* the **generic evidence requirements** for each possible class (I‑III) and conformity‑assessment route under MDR;  
* the **risk‑control expectations** linked to the Technical Documentation (Annex II) and Post‑Market Surveillance (Art. 83‑86);  
* the **citations** that apply once the missing data are provided; and  
* **human‑escalation triggers** for when gaps remain.

---

### 2. Information still required to determine classification / submission route  

| Item | Why needed | Where it belongs in TD (Annex II) |
|------|------------|-----------------------------------|
| **Device name & model(s)** | Identification of the product family | 1.3 “Identification of the device” |
| **Intended purpose / indication** (including target patient group, clinical condition, intended user) | Drives application of the Classification Rules (Annex VIII) and determines which GSPR apply | 1.4 “Device description” |
| **Mode of action & principal technologies** (e.g., active therapeutic, diagnostic imaging, software, implantable) | Determines which rule(s) (Rule 9‑11, 17 etc.) are relevant; also influences risk classification for software (Rule 11) | 1.4 “Device description” |
| **Nature of the energy supplied or emitted** (e.g., ionising radiation, electrical/mechanical) | Required for Rules 9, 10, 16‑18 in Annex VIII | 1.4 “Device description” |
| **Intended user – professional vs layperson** | Affects GSPR §22 and may shift class for certain devices | 1.5 “Information supplied with the device” (§23) |
| **Pre‑market clinical data / literature** (bench, animal, human) | Needed for Clinical Evaluation Report (CER) (Annex XIV Part A) and to support classification justification | 3.2 “Clinical evaluation” |
| **Software description (if applicable)** – algorithm, intended decisions, risk‐impact matrix | Determines Rule 11 class and software lifecycle evidence (IEC 62304) | 1.4 & 3.2 |
| **Reference to any predicate/stand‑alone device** (for comparison) | Supports classification justification; not a 510(k) in EU but useful for risk analysis | 5.1 “Regulatory compliance” |
| **Intended market (EU only? other regions?)** | Influences conformity‑assessment route, presence of an Authorized Representative (Art. 11) | 5.1 “Regulatory compliance” |

*If any of the above items cannot be supplied by the manufacturer, classification remains indeterminate and a **human escalation** to the device’s R&D/clinical lead is required.*

---

### 3. Generic evidence requirements once classification is known  

| Classification (MDR) | Typical Conformity‑Assessment Route(s) | Evidence bundle (mandatory) |
|----------------------|----------------------------------------|------------------------------|
| **Class I (non‑sterile, non‑measuring)** | Annex IX (self‑declaration of conformity) – QMS assessment only if a **QMS** is needed for the device (else no NB involvement). | • Technical Documentation (Annex II) <br>• Declaration of Conformity (Annex IV) <br>• PMS plan (Art. 84) |
| **Class I (sterile or measuring)** | Annex IX **+** Notified Body review of the QMS (ISO 13485) and specific aspects of TD (e.g., sterilisation validation). | • All Class I items <br>• Sterilisation validation report (IEC 60601‑1‑2/ IEC 62366 as appropriate) |
| **Class IIa** | Annex IX (QMS + technical file review) **or** Annex X (type‑examination) if required by the device type. | • Full TD (Annex II) <br>• Clinical Evaluation Report (CER, Annex XIV Part A) – kept current (Art. 61) <br>• PMS plan & periodic safety update report (PSUR) every 2 years (Art. 86) |
| **Class IIb** | Annex IX (full QMS audit) **or** Annex X (type‑examination). Many high‑risk active devices use Annex IX with a full NB assessment of the TD. | • All IIa items <br>• PSUR annually (Art. 86) <br>• PMCF plan & evaluation report (Annex XIV Part B) |
| **Class III** | Annex X (type‑examination) – mandatory for highest risk devices; NB examines the entire TD and may request a separate design dossier. | • All IIb items <br>• PSUR annually (Art. 86) <br>• Comprehensive PMCF plan & report (Annex XIV Part B) <br>• Clinical investigation data if no sufficient literature exists |

**Key citations**

* **Classification rules:** Annex VIII, Rules 9‑11, 17 etc. – apply once intended purpose is known.  
* **Technical Documentation requirements:** Annex II (Sections 1‑5).  
* **Clinical Evaluation Report:** Annex XIV Part A; must be kept up‑to‑date (Art. 61).  
* **PMCF plan & report:** Annex XIV Part B.  
* **PMS system:** Art. 83; PMS plan Art. 84; PSUR Art. 86(1‑2); PMS report for Class I Art. 85.  
* **Risk Management:** ISO 14971 (risk management file) integrated in Annex II Section 5 and mapped to GSPR (§18, §19).  

---

### 4. Risk controls that must be demonstrable in the TD  

| Control area | Expected artefact | Regulatory reference |
|--------------|-------------------|----------------------|
| **Risk Management Process** (hazard identification, risk analysis, evaluation, control) | ISO 14971‑compliant risk management file; traceability matrix linking residual risks to GSPR | Annex II §5.2; GSPR mapping (Annex I §§10‑22) |
| **Usability / Human factors** (if device used by laypersons or has critical user interface) | IEC 62366‑1 usability engineering file and verification/validation results | Annex I §22, §23 |
| **Software lifecycle** (if applicable) | IEC 62304 software development plan, verification & validation reports; classification‑appropriate justification per Rule 11 | Annex I §17; Rule 11 |
| **Electrical safety / EMC** | IEC 60601‑1 compliance test reports (or relevant IEC standard for non‑medical electrical equipment) | GSPR §§10‑12 |
| **Radiation protection** (if ionising radiation involved) | IEC 60601‑2‑54/28/44 test data; compliance with GSPR §16.4 | Rule 10, Rule 17, GSPR §16 |
| **Sterilisation / bioburden control** (if sterile) | Validation of sterilisation process (ISO 11135/14937) and packaging integrity tests | GSPR §18 |
| **Labeling & IFU** | Full labeling bundle meeting Annex I §23 (including UDI information, safety notices) | Annex I §23 |

*Each control must be cross‑referenced to the relevant GSPR checklist that the RA team will complete (see step 3 in the source excerpt).*

---

### 5. Missing information – immediate actions  

| Gap | Action required | Who is responsible (per source) |
|-----|-----------------|---------------------------------|
| **Device description & intended purpose** | Provide a concise statement of indication, target population, and mode of action. | R&D (step 2) → deliver to RA for GSPR mapping |
| **Classification justification** | Map the device to the appropriate Annex VIII rule(s). | RA (step 1 & step 3) after receiving description |
| **Clinical data / CER draft** | Assemble literature review, any existing clinical investigations, and produce a CER outline. | RA/Clinical (step 4) |
| **Risk management file** | Complete ISO 14971 risk analysis; include residual risk evaluation. | QA (step 5) |
| **PMS plan** | Draft PMS Plan reflecting device class, intended use, and post‑market data collection schedule. | RA (step 6) |
| **Economic Operator verification** | Confirm that Manufacturer/Authorized Representative/Importer/Distributor responsibilities are allocated per Art. 10‑14. | Manufacturer / AR (step 1 & step 8) |

*If any of these items cannot be supplied within the next 10 working days, trigger a human escalation to the Project Lead for schedule impact assessment.*

---

### 6. Human‑escalation triggers  

| Condition | Trigger | Escalation path |
|-----------|---------|-----------------|
| **No device description / intended purpose** after request | Immediate pause on classification work; inform NB that submission cannot proceed. | RA Lead → Project Management → Manufacturer contact |
| **Unresolved GSPR mapping gaps** (e.g., missing evidence for a specific requirement) | Flag to QA Manager for risk‑control verification. | QA Manager → Senior Quality Officer |
| **Clinical evidence insufficient to support CER** (e.g., no published literature, no ongoing trial) | Require Clinical Investigation or expanded PMCF plan before NB review. | Clinical Lead → Sponsor / Ethics Committee |
| **PMS Plan not aligned with device class** (e.g., PSUR missing for Class IIb/III) | Request revision; may affect timeline for Annex IX/X evaluation. | RA Lead → NB liaison officer |
| **Economic Operator responsibilities incomplete** (e.g., no designated Authorized Representative for non‑EU manufacturer) | Must appoint AR before CE marking can be affixed. | Manufacturer legal counsel → Compliance Officer |

Each trigger should be logged in the project’s risk register and communicated to the Notified Body as a “pending issue” with an agreed remediation date.

---

### 7. Summary judgment (to be conveyed to the NB)

*At present we lack sufficient device‑specific information to assign an MDR classification or select the appropriate conformity‑assessment route.*  
**Required deliverables before any NB assessment can commence:**

1. Full **device description & intended use**, enabling rule‑based classification (Annex VIII).  
2. Completed **risk management file** and **GSPR mapping** (Annex II §5, Annex I).  
3. Draft **Clinical Evaluation Report** (Annex XIV Part A) or a clear plan for a Clinical Investigation if literature is insufficient.  
4. **PMS Plan** appropriate to the final class (Art. 84) and, where applicable, a PSUR schedule (Art. 86).  

Once these are provided, we will be able to:

* Assign the correct **class** (I‑III) and identify whether Annex IX, X or XI is required.  
* Compile the full **technical file** per Annex II and submit it together with the **Declaration of Conformity** (Annex IV).  

Until the above items are received, we must pause the NB submission.

---

### 8. Peer‑review prompt  

> *Colleague, please review the assumptions made in this draft:*

* *Are the generic evidence lists aligned with the latest MDCG guidance for each class?*  
* *Is any jurisdiction‑specific nuance (e.g., special rules for X‑ray devices, AI/ML software) missing given that we have no device detail yet?*  
* *Do the escalation thresholds reflect our internal risk‑acceptance policy, or should they be tightened?*  

Your feedback will ensure the final response fully satisfies the Notified Body’s expectations.

<!-- verification-summary -->

**🔎 기계 검증 요약** (우선순위 106/190 · 자동 생성, 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 11,254자 | — |
| 규제 식별자 인용 | 20개 | — |
| excerpt 근거 일치 | **2/20 (10%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 식별자 | 18개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |
| 근거 인용 표현 | 있음 | `Source cited` |

**근거 대조 위험도: 높음**

**excerpt에서 확인되지 않은 인용**: `Annex II`, `Art. 83`, `Annex VIII`, `Annex XIV`, `IEC 62304`, `Annex IX`, `Annex IV`, `Art. 84`, `ISO 13485`, `IEC 60601`, `IEC 62366`, `Annex X` 외 6개

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

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `24104208734622027`

> ## 3. 경제운영자(Economic Operator) 역할 정의 | 역할 | MDR 조항 | 핵심 의무 | 자사 해당 여부 | |------|----------|----------|--------------| | 제조자(Manufacturer) | Art. 10 | 기술문서, QMS, UDI, PMS, Vigilance, PRRC 지정 | ☐ | | 수권대리인(AR) | Art. 11 | EU 내 제조자 대리, 당국 연락창구 | ☐ (비EU 제조사 필수) | | 수입업자(Importer) | Art. 13 | CE 마크·UDI 확인, 보관조건 준수, 불만 전달 | ☐ | | 유통업자(Distributor) | Art. 14 | CE 마크·라벨 확인, 보관·운송 조건 준수 | ☐ |

### kb-eval-20260721-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "7f257d2218b4c946", "source": "github:holee9/MD-process/issue-drafts/950_AUDIT_GSPR_정합표준_매핑표_MDR_AnnexI_19_활성이식_인용부정확.md", "source_hash": "2e5bb5e6f319013f35bfffde39b3c4b5e527009de066335c38c8710f24199c01"} -->

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

> **Regulatory Draft – Preliminary Classification & Submission Planning for an Active Implantable Medical Device (AIMD)**  

---

### 1. Device Scope (derived from source)

The source excerpts centre on **Annex I, Chapter II** of MDR 2017/745 and cite:

* §16 – Protection against radiation  
* §17 – Electronic programmable systems & software (including EMC, SW‑lifecycle, IT‑security)  
* §19 – Particular requirements for **active implantable devices** (energy source, component identification, non‑surgical readout)  

> *Citation*: Regulation (EU) 2017/745, Annex I, §§ 16, 17, 19 (source [1]).

These provisions indicate that the device under review is **active, implantable, and incorporates programmable electronics**. No further functional description is supplied in the source material.

---

### 2. Preliminary Classification  

| Criterion | MDR Requirement | Preliminary Conclusion |
|-----------|----------------|------------------------|
| **Active & Implantable** (energy source required to operate) | Annex VIII – Rule 12 (active therapeutic implantable devices) → **Class III** | Likely **Class III** unless the device can be demonstrably shown to be low‑risk (e.g., short‑term, non‑critical). |
| **Software that influences diagnostic/therapeutic decision** | Annex VIII – Rule 11 (medical device software) → Class IIa/IIb/III depending on impact | If the software provides treatment recommendations or controls the implant, it may trigger **Rule 11 IIb/III**. |
| **Radiation‑emitting component** (if any) | Annex VIII – Rule 10 (active devices emitting ionising radiation) → Class IIb | Only applicable if the device contains an X‑ray source; not evident from the excerpt. |

> *Citation*: MDR Annex VIII, Rules 11 & 12 (classification rules). **Verify** exact rule numbers against the final intended use description.

**Action** – Obtain a full “Intended Use” statement and technical description to confirm whether Rule 12 (Class III) or a lower class applies.  

---

### 3. Conformity‑Assessment Route  

Assuming **Class III AIMD**:

| Step | MDR Reference | Required NB Involvement |
|------|----------------|--------------------------|
| Quality‑Management System assessment (ISO 13485) + Technical Documentation review | Annex IX (full quality‑management & technical‑documentation assessment) | Mandatory NB audit of QMS and technical file. |
| Design‑Dossier / Device‑File review (including clinical evidence, risk management, software validation…) | Annex II (Technical documentation) – with PMS technical dossier as per Annex III | Required for Class III. |
| Issuance of EU‑Declaration of Conformity & CE‑Marking | Annex IV | NB issues the certificate after successful assessment. |

> *Citation*: MDR Annex IX, Annex II, Annex III, Annex IV (standard MDR route).  

---

### 4. Evidence Package Required for NB Submission  

| Evidence Item | Regulatory Basis | Typical Content |
|---------------|------------------|-----------------|
| **Technical Documentation** | Annex II | Device description, labeling (Annex I §23), GSPR compliance matrix (incl. §§ 16‑20), manufacturing information. |
| **Risk Management File** | ISO 14971 & MDR Annex I §17–§20 | Risk analysis, risk control measures, residual risk evaluation, especially for energy source (§19.1) and component identification (§19.3). |
| **Software Documentation** (if applicable) | IEC 62304, MDR §17.2‑§17.4 | Software architecture, lifecycle plan, verification/validation, cybersecurity & IT‑security controls. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; Art. 61 | State‑of‑the‑art literature review, clinical data justification, benefit–risk determination. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan / Report** | Annex XIV Part B; Art. 84/86 | Ongoing safety/performance data collection strategy and interim findings. |
| **PMS System & Periodic Safety Update Report (PSUR)** | Art. 83–86 | PMS procedure, PSUR (annual for Class III). |
| **Labeling & IFU** | Annex I §23 | Instructions for use, safety information, non‑surgical readout code (§19.4). |
| **Standards Conformity Statements** | Relevant IEC/ISO standards (e.g., IEC 60601‑2‑28, IEC 62366‑1) | Declaration that device meets applicable essential requirements. |

---

### 5. Identified Gaps & Missing Information  

| Missing Item | Why Critical | Source Coverage |
|--------------|--------------|-----------------|
| **Full Intended Use / Indications for Use** | Drives classification (Rule 12 vs. Rule 11) and determines which GSPR sections apply in detail. | Not present in excerpts. |
| **Energy Source Description & Duration of Implantation** | Required to satisfy §19.1 (risk minimisation of energy source) and influences class determination. | Implicit only via §19 reference. |
| **Software Functionality Matrix** | Determines if software falls under Rule 11 (diagnostic/therapeutic) and the depth of IEC 62304/IEC 60601‑4‑1 compliance needed. | Only generic §§ 17.2‑17.4 cited. |
| **Radiation Emission Details** (if any) | Would invoke §16 (radiation protection) and possibly Rule 10 (ionising radiation). | No mention of radiation emission in source; only §16 referenced as a general requirement. |
| **Usability/Human Factors Assessment** | Needed for IEC 62366‑1 compliance, especially for implantable devices used by lay persons (§22). | Not covered. |
| **Naming of Specific Harmonised Standards** (e.g., EN ISO 14971) | Required to demonstrate conformity with essential safety requirements. | No standard numbers listed in source. |
| **Clinical Data Sources** (clinical investigations, literature, registries) | Core of CER & PMCF. | Absent. |

**Immediate Action:** Request the above items from the development team before proceeding with a formal classification decision.

---

### 6. Required Risk Controls (Mapped to GSPR)

| GSPR Clause | Typical Control(s) | Evidence Needed |
|-------------|--------------------|-----------------|
| **§16 – Radiation protection** | Shielding, dose monitoring, compliance with IEC‑60601‑2‑28 (if applicable). | Test reports, certification of radiation safety. |
| **§17 – Electronic programmable systems** | • EMC testing per IEC 60601‑1‑2 ( §17.1 )<br>• Secure software lifecycle & IT security per IEC 62304 and IEC 62443 ( §17.2‑§17.4 ) | Test certificates, cybersecurity risk analysis, verification/validation records. |
| **§19 – Active implantable devices** <br> (19.1 Energy source, 19.3 Component ID, 19.4 Non‑surgical readout) | • Redundant energy control (e.g., battery monitoring),<br>• Unique device identifiers on each component,<br>• Encrypted telemetry for non‑invasive reading. | Risk analysis outcomes, labeling/IFU excerpts, verification of readout security. |
| **§20 – Mechanical & thermal risks** | Structural integrity testing, temperature limits, biocompatibility per ISO 10993. | Test data, biocompatibility reports. |

---

### 7. Human‑Escalation Triggers  

| Trigger Event | Escalation Level | Reason |
|---------------|------------------|--------|
| **Unresolved classification ambiguity** (e.g., missing intended use) | Immediate pause – senior MDR lead & NB liaison required. | Incorrect class leads to non‑conformity of whole assessment route. |
| **Absence of clinical data or insufficient CER** | Escalate to Clinical Affairs Lead for urgent study planning or literature search. | Art. 61 mandates a current, complete CER; gaps invalidate the technical file. |
| **Software cybersecurity gap (no IT‑security plan)** | Escalation to Cyber‑Security Officer and Legal Counsel. | Non‑compliance with §17.4 may breach Art. 83‑84 PMS obligations. |
| **Radiation safety evidence missing when device emits ionising radiation** | Immediate stop – Radiation Safety Specialist must provide test data before any NB submission. | §16 non‑compliance is a show‑stopper for approval. |
| **Risk management file not aligned with GSPR (e.g., no mitigation for energy source)** | Escalate to Risk Management Lead for risk reassessment and control implementation. | Failure of §19.1 violates essential safety requirements. |
| **Labeling/IFU incomplete (no non‑surgical readout code)** | Escalation to Regulatory Writing Team – labeling must meet §19.4 before submission. | Incomplete information can lead to post‑market corrective actions under Art. 87. |

---

### 8. Summary Judgment  

*Based on the limited source material, the device appears to be an **active implantable medical device with programmable electronics** and therefore is **preliminarily classified as Class III under MDR Annex VIII Rule 12 (active therapeutic implantable)**. The appropriate conformity‑assessment route is **Annex IX** (full QMS + technical documentation review). A complete evidence package—including risk management, software lifecycle artefacts, clinical evaluation, PMCF plan, PMS system, and full labeling—must be compiled before NB submission.*

*Key gaps (intended use description, energy source details, software functional scope, radiation emission status, clinical data) must be resolved **before** any classification can be finalised.*  

---

### 9. Peer‑Review Prompt  

> *Colleague, could you review the assumptions made about the device’s classification (Rule 12 vs. Rule 11), the completeness of GSPR mapping (especially §§ 16–20), and suggest any additional MDR provisions or harmonised standards that should be added to this preliminary draft? Please also verify whether Annex IX is indeed the required route for the inferred Class III status, considering any possible alternative pathways.*  

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

1. Chunk `1080110362051195619`

> - **EUR-Lex — Regulation (EU) 2017/745, Annex I Chapter II**: - §14 Construction of devices and interaction with their environment (EMC/환경 대응) - §16 Protection against radiation (방사선 방호 — 이미 §16 행이 doc 본문에 정합 매핑됨) - §17 Electronic programmable systems / devices that incorporate electronic programmable systems and software that are devices in themselves — **§17.1 EMC/신뢰성 요구, §17.2 SW 개발수명주기·정보보안, §17.4 IT security minimum requirements** - **§19 Particular requirements for active implantable devices** — 19.1 에너지원·유지보수·상호작용 위험 최소화 / 19.3 부품 식별성 / 19.4 수술 없이 판독 가능한 코드 - §20 Protection against mechanical and thermal risks - MDR Annex I 텍스트 재확인:...

2. Chunk `139221394525877266`

> -regulation.eu/2019/07/23/annex-i-general-safety-and-performance-requirements/

## ra_kr

### kb-eval-20260721-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "7978dfb67195557f", "source": "github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md", "source_hash": "54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7"} -->

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

> **Regulatory Draft – Digital‑Medical Device (SBOM / Cybersecurity Focus)**  

---

### 1. Applicable Legal Framework  
| Source | Provision | Core Requirement |
|--------|-----------|-----------------|
| 디지털의료제품법 **제13조** | “디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항 – 전자적 침해행위로부터의 취약점에 대한 지속적 보완” (2호) | Manufacturers must continuously remediate software‑related vulnerabilities. |
| 디지털의료제품법 **제14조** | “전자적 침해행위로부터의 보호 조치” – MFDS security guideline issuance (①) and mandatory compliance by manufacturers (②). | Establishes the legal basis for a security management system, including SBOM generation/maintenance. |
| 디지털의료제품법 **제16조(기재값)** | “우수 관리체계 인증” – voluntary 3‑year certification covering quality, safety & electronic‑attack prevention; **does not govern SBOM**. | Relevant only if the manufacturer elects to pursue the optional 우수관리체계 (U‑MS) certification; it is not a prerequisite for SBOM compliance. |
| 디지털의료제품법 **제40조** | “디지털의료제품의 구성요소에 대한 성능평가” – sensor & AI algorithm performance evaluation required separately (see AI_구성요소_단위_성능평가.md). | Mandates component‑level performance testing; independent of SBOM but part of the overall technical dossier. |

*All citations are directly taken from the source excerpts above.*

---

### 2. Device Classification & Submission Route  

| Element | Determination (based on Korean regulations) |
|---------|---------------------------------------------|
| **Risk class** | Not stated in the excerpt; classification must be derived from MFDS “Medical Device Classification Rules” (e.g., Class II for diagnostic AI, Class III for therapeutic AI). *Human reviewer required to assign correct risk class.* |
| **Submission type** | • **Class I** – simple notification (신고) if low‑risk and no invasive function.  <br>• **Class II/III** – formal 허가 application with full technical dossier, clinical evaluation (if applicable), KGMP certification, and security compliance per Articles 13 & 14. |
| **Specific identifier** | *no specific identifier found in source — verify separately* |

---

### 3. Required Evidence Package  

| Requirement | Documents / Data | Legal Basis |
|-------------|------------------|------------|
| **KGMP (Korean Good Manufacturing Practice) certificate** | Facility audit report, GMP compliance certificate | MFDS KGMP regulations (implicit for all manufacturing). |
| **Technical Documentation (TF)** | • Device description, intended use, risk analysis <br>• Component‑level performance data (sensor/AI) – per **제40조** <br>• Software Bill of Materials (SBOM) – generation & update procedure. | **제14조**, **제13조** (security obligations). |
| **Security Management System** | • MFDS security guideline adherence plan (physical, technical controls) <br>• Vulnerability monitoring & patch management procedures <br>• Incident response SOPs | **제13조(2호)**, **제14조(①‑②)** |
| **Clinical Evaluation / Clinical Evidence** *(if Class II/III)* | • Clinical trial report or literature supporting safety/effectiveness. | MFDS “Medical Device Clinical Evaluation Guidelines”. |
| **Labeling & IFU (Korean language)** | Full product label, Instructions for Use, and any software user manuals in Korean. | MFDS labeling regulations (Article 23‑24 of the Medical Devices Act). |
| **Optional 우수 관리체계 인증** | Proof of U‑MS certification (valid 3‑year certificate) – only if manufacturer elects to obtain it. | **제16조** (voluntary). |

---

### 4. Missing Information & Action Items  

| Gap | Why it matters | Suggested resolution |
|-----|----------------|----------------------|
| **Risk class determination** | Determines submission pathway and required evidence depth. | Perform MFDS risk classification per device intended use; document rationale. |
| **Clinical data scope** (if applicable) | Required for 허가 of Class II/III devices. | Identify need for clinical trial or equivalence study; prepare protocol. |
| **Korean‑language labeling** | Mandatory for market entry; absent may cause rejection. | Draft label & IFU in Korean; conduct translation verification. |
| **SBOM content depth** (e.g., versioning, provenance) | Must satisfy continuous vulnerability remediation per Articles 13‑14. | Define SBOM format (SPDX or CycloneDX), update frequency, and linkage to patch management. |
| **Post‑Market Surveillance (PMS) plan** | Required for all digital medical devices; especially for cybersecurity updates. | Outline PMS activities, reporting schedule, and field safety corrective actions. |
| **Evidence of compliance with MFDS security guideline** | Article 14 obliges manufacturers to follow the MFDS‑issued security guidance. | Obtain latest MFDS security guideline (2025 edition) and map internal controls to each clause. |

---

### 5. Core Risk Controls (Cyber‑Security Focus)

| Control | Description | Reference |
|---------|-------------|-----------|
| **SBOM generation & maintenance** | Produce a complete, machine‑readable SBOM for all software components; update on every code change. | **제13조(2호)**, **제14조** |
| **Vulnerability monitoring** | Subscribe to relevant CVE feeds; conduct regular scanning of all components listed in the SBOM. | **제13조(2호)** |
| **Patch management & remediation** | Define SLA for applying security patches (e.g., ≤30 days after release); document each patch in change control records. | **제14조(②)** |
| **Secure development lifecycle (SDL)** | Incorporate threat modeling, code review, static/dynamic analysis during software development. | Align with MFDS security guideline (2025). |
| **Access controls & encryption** | Enforce role‑based access to source repositories; encrypt data at rest and in transit. | MFDS cybersecurity best practices. |
| **Incident response SOP** | Pre‑defined procedure for detection, containment, eradication, and post‑incident analysis of cyber‑events. | **제14조(①)** |

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger Point | Escalation Path |
|-----------|---------------|-----------------|
| **Unclear risk class** (no classification evidence) | Upon draft dossier review, missing Class assignment. | Escalate to senior RA lead for classification deliberation with product team. |
| **SBOM absent or outdated** | No SBOM file attached or last update > 90 days ago. | Immediate pause of submission; notify development & QA leads for rapid generation. |
| **Non‑compliance with Article 14 security guideline** (e.g., no documented security policy) | Gap identified during technical dossier audit. | Escalate to compliance manager and require corrective action plan before filing. |
| **Missing Korean labeling/IFU** | Draft submission lacks any Korean language materials. | Halt filing; involve regulatory affairs & translation team. |
| **Insufficient clinical evidence for Class II/III** | Clinical evaluation section incomplete or lacking approved protocol. | Escalate to clinical development lead; consider deferment of 허가 until data secured. |
| **U‑MS certification claimed but no proof** | Assertion of “우수 관리체계 인증” without certificate. | Verify with certifying body; if unavailable, remove claim or obtain certification before submission. |

---

### 7. Summary Judgment  

- The legal basis for SBOM and broader cybersecurity obligations resides in **디지털의료제품법 제13조** (continuous vulnerability mitigation) and **제14조** (security guidelines & compliance).  
- **제16조** pertains only to the optional 우수 관리체계 인증 and does not mandate SBOM creation.  
- The device’s risk class must be determined according to MFDS classification rules; this drives whether a simple 신고 or full 허가 is required.  
- A complete submission package will include KGMP certification, detailed TF (with SBOM), security management documentation, component‑level performance data per **제40조**, Korean labeling/IFU, and, when applicable, clinical evidence and U‑MS certificate.  

**Human reviewers should verify the risk class, confirm the presence of a current SBOM, ensure alignment with the latest MFDS security guideline, and validate that all Korean‑language requirements are met before proceeding to filing.**

---

### 8. Peer Review Prompt  

> **To RA colleague:** Please review this draft for (i) completeness of jurisdiction‑specific obligations (e.g., any overlooked MFDS notices on digital‑medical device cybersecurity after 2026), (ii) adequacy of the evidence list given the assumed risk class, and (iii) potential gaps between the cited articles and practical submission requirements (such as documentation format for SBOM). Highlight any assumptions that need verification or additional source coverage.

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

### kb-eval-20260721-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "393df4d80723d349", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038"} -->

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

> **Regulatory Draft – Supplementary‑Response (보완자료) Strategy**

---

### 1. Likely Submission Route & Classification

| Situation | Typical Korean MF DS Pathway | Comments |
|-----------|----------------------------|----------|
| **Class I (low‑risk)** – devices exempt from safety/effectiveness review | **신고** (Notification) – immediate acceptance, no formal review period | Clock‐stop does not apply; supplement is submitted as an addendum to the original notification. |
| **Class II (moderate‑risk)** – devices requiring technical dossier review | **허가(일반)** (General Approval) – 65 days processing (excluding supplement periods) | The “보완 기간은 처리 기간에서 제외 (clock stops)” rule applies – MFDS pauses the review clock while the sponsor prepares the requested supplementary data. |
| **Class II‑D or Class III (high‑risk, clinical evidence required)** | **허가(임상 포함)** (Approval with Clinical Data) – 80 days processing (excluding supplement periods) | Same clock‐stop rule; more extensive clinical/evidence requirements (e.g., Korean PMDA/clinical trial data). |
| **Quality‑system certification (KGMP, ISO 13485) for manufacturing sites** | **인증** – 30 days processing by NIFDS (Korea Food & Drug Administration’s “NIFDS” division) | Required for Class II‑D/III devices and for any device that is to be manufactured domestically. |

> **Citation:** Processing times and the clock‑stop principle are taken from MFDS guidance table “1‑B. 허가 심사 처리 기간 (정상 회차)”【1020687580074720264】.

**Conclusion on classification/submission route:**  
Without device‑specific details (e.g., intended use, risk class, whether clinical data are needed) a definitive pathway cannot be assigned. The sponsor should first confirm the Korean risk class (K‑class) based on the MFDS “Medical Device Classification Rules” and then select one of the routes above.

---

### 2. Core Evidence Packages Expected for a Supplement

| Submission Type | Typical Required Documents (incl. supplements) |
|-----------------|-------------------------------------------------|
| **General Approval (허가 일반)** | • Updated Technical File (제품설명서, 설계도면)<br>• Risk Management Report (ISO 14971)<br>• Clinical Evaluation Report (if any foreign data are used – see Section 3)<br>• Verification/Validation test reports (including any newly requested performance data) |
| **Approval with Clinical Data (허가 임상 포함)** | All of the above **plus**:<br>• Korean clinical trial dossier or a justified reliance on foreign clinical data (see §3)<br>• Informed consent forms, ethics committee approvals<br>• Post‑market surveillance plan (시판후조사) |
| **Certification (인증)** | • KGMP audit report for the manufacturing site<br>• ISO 13485 certification copy<br>• Process validation & sterility assurance data (if applicable) |

---

### 3. Handling Foreign Evidence – When Can It Be Accepted?

MFDS has, in recent notices, broadened acceptance of **OECD‑aligned non‑clinical studies** and **foreign clinical evaluation reports** provided that:

1. The foreign study follows an internationally recognized standard (e.g., ISO 10993 for biocompatibility, FDA 510(k) predicate data).  
2. A full translation into Korean is supplied, accompanied by a certified verification statement.  
3. Any gaps specific to the Korean population or usage environment are addressed (e.g., additional safety monitoring data).

If the sponsor wishes to rely on such foreign evidence, they must submit:

* Original study reports (English) + **Korean‑language translation**.  
* A justification matrix mapping foreign standards to Korean regulatory requirements.  
* Evidence that the study design conforms to OECD GLP or FDA Good Laboratory Practice.

> **Citation:** Standard Korean expressions for data submission are given in “4‑C. 자주 사용하는 표현 (한국어 공문 문체)”【1071384471244337751】, which include phrasing for attaching supplemental data (“해당 데이터를 별첨 자료로 첨부하오니 검토하여 주시기 바랍니다.”).

---

### 4. Missing Information & Immediate Action Items

| Item | Why It Is Needed | Suggested Remedy |
|------|------------------|-------------------|
| **Exact device classification (K‑class)** | Determines whether a ‘신고’, ‘허가(일반)’, or ‘허가(임상 포함)’ route is required. | Conduct a K‑class assessment using MFDS Classification Rules; document the decision. |
| **Specific supplement request details** (e.g., which test reports, which sections of the technical file are deficient) | The “보완 내용 인용” language shows how to reference the regulator’s request, but the actual content must be matched precisely. | Review the MFDS supplement notice; list each requested item and map it to existing files. |
| **Korean‑language translations of any foreign data** | Required for acceptance of overseas evidence. | Engage a certified translation service; attach a “translation verification” statement per MFDS guidance. |
| **KGMP certification status (if applicable)** | Mandatory for manufacturing sites of Class II‑D/III devices and for any device seeking ‘인증’. | Verify current KGMP audit report; schedule re‑audit if out‑of‑date. |
| **Post‑market surveillance (PMS) plan** (for higher‑risk classes) | MFDS expects a PMS plan before final approval. | Draft a Korean‑language PMS plan following the “시판후조사” format and submit as part of the supplement. |

---

### 5. Risk Controls & Documentation

| Risk Control | Evidence to Provide in Supplement |
|--------------|-----------------------------------|
| **Design Control (ISO 13485, MFDS QMS)** | Updated design history file, change control records, risk analysis updates (ISO 14971). |
| **Biocompatibility** | New or updated ISO 10993 test reports; if foreign data are used, include translation and justification. |
| **Sterilization Validation** (if applicable) | Sterility assurance level calculations, validation protocols & reports. |
| **Software Safety (if device includes software)** | IEC 62304 compliance evidence, cybersecurity risk assessment, update logs. |

All documents must be labeled in Korean and submitted as separate “별첨 자료” per the language template shown in the source excerpt.

---

### 6. Human‑Escalation Triggers

| Situation | When to Escalate to Senior RA / Regulatory Lead |
|-----------|------------------------------------------------|
| **No clear classification can be derived** after internal analysis. | Immediate – risk of submitting under wrong pathway. |
| **Required Korean translation cannot be delivered within the clock‑stop period** (e.g., due to vendor delay). | Request an extension **before** the original deadline expires; use the “연장 요청” phrasing from the template. |
| **MFDS issues a second-round supplement request** after the first submission is accepted. | Senior RA should review for any systemic gaps and consider pre‑emptive external expert consultation. |
| **KGMP certification gap identified** (e.g., audit pending). | Escalate to manufacturing compliance manager; pause the submission until certification is secured. |
| **Foreign clinical data are rejected** because they lack Korean‑specific safety justification. | Engage medical affairs/clinical team to design a supplemental Korean cohort study; senior leadership must approve resource allocation. |

---

### 7. Summary Judgment

*The sponsor must first confirm the device’s K‑class to select the appropriate MFDS pathway (신고, 허가(일반), 허가(임상 포함) or 인증). Once the route is set, the supplement should be compiled using the Korean‐language phrasing shown in the source (“보완 내용 인용”, “데이터 추가 제출”) and must include any missing performance, safety, or clinical data, with full Korean translations for foreign evidence. The review clock stops during preparation of this supplemental package; therefore, all items must be ready before the deadline or a formal extension request should be submitted using the standard expression.*

**If any of the above missing items cannot be resolved within the allotted time, the case should be escalated to senior regulatory management for extension negotiation or strategy revision.**

---

### 8. Peer‑Review Prompt

> **@RA‑Peer:** Please challenge the assumptions made here—particularly the mapping of classification pathways without device specifics, the completeness of the required evidence list for each route, and any jurisdictional gaps (e.g., local clinical trial exemptions, recent MFDS notices on foreign data acceptance). Highlight any additional Korean regulatory obligations that may have been overlooked.

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

### kb-eval-20260721-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "abeb11318f80057b", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

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

> **Regulatory Draft – Digital‑Medical‑Software (Korea MFDS)**  

---

### 1. Classification & Submission Route  
| Item | Assessment |
|------|------------|
| **Regulatory framework** | *디지털의료제품법* and its 시행규칙; MFDS “Digital Medical Device SW‑Guideline”. |
| **Device type** | Stand‑alone software (no accessory hardware listed). |
| **Risk‑based class** | Requires a formal risk classification under the “소프트웨어 의료기기 위험도 분류표” (MFDS Risk‑Classification Table for Software). The table links intended use (e.g., diagnosis, therapy, monitoring) and algorithmic complexity to Class I–IV. <br>*Current source does not disclose intended use or risk level.* |
| **Proposed submission pathway** | - **If classified as Class I** → “신고” (notification).  <br>- **If classified as Class II‑IV** → “허가” (full approval) with KGMP‑certified manufacturing site and MFDS review. |

> **Action:** Obtain the intended use description, risk analysis, and algorithmic details from the product team to place the device in the correct class.  

---

### 2. Mandatory Evidence & Documentation (per MFDS checklist)

| Requirement | Source citation | Status |
|-------------|----------------|--------|
| **SW version·build number·release date** (S‑1) | 디지털의료제품법 시행규칙 | ✅ Required – must be listed on the IFU/label. |
| **SW update method & frequency** (S‑2) | MFDS SW 가이드라인 | ✅ Required – include SOP for updates and schedule. |
| **Minimum / recommended system requirements** (OS, CPU, RAM, storage, monitor resolution, network) (S‑3) | MFDS SW 가이드라인 | ✅ Required – present in IFU. |
| **Compatible medical device list & interface info** (S‑4) | — (no explicit citation) | ✅ Required – must be documented; source does not provide a regulator reference, but the item is mandatory per the checklist. |
| **Data input/output format (DICOM·HL7 etc.)** (S‑5) | — | ✅ Required – specify formats and conformance. |
| **Cybersecurity configuration guidance** (encryption policy, network segregation, access rights) (S‑6) | MFDS 사이버보안 가이드라인 2025.01 | ✅ Required – include in IFU. |
| **Security patch application procedure & responsibility** (S‑7) | MFDS 사이버보안 가이드라인 2025.01 | ✅ Required – SOP and responsible party must be named. |
| **Known residual cyber‑risk & mitigation** (S‑8) | MFDS 사이버보안 가이드라인 2025.01 | ✅ Required – risk register and handling plan. |
| **Data backup & recovery method** (S‑9) | — | ✅ Required – detail schedule, location, verification. |
| **System log management method** (S‑10) | MFDS 사이버보안 가이드라인 (recommended) | ⚠️ Recommended – still advisable to include for traceability. |
| **AI/ML specific documentation** (e.g., training data set description, performance monitoring) | — (cut off in excerpt) | ❓ Missing – must be added if AI/ML is employed; MFDS requires a separate “Algorithm Transparency” annex. |
| **Korean language labeling & IFU** | General MFDS labeling rule (no specific notice cited) | ✅ Required – all mandatory items must appear in Korean. |
| **KGMP certification of development environment** | KGMP 규정 (not directly in excerpt) | ❓ Missing – required for Class II‑IV approvals. |
| **Clinical evidence** (local/performed) | — | ❓ Missing – depends on risk class; foreign clinical data may be accepted if aligned with MFDS notice expanding foreign evidence acceptance (verify latest notice). |

---

### 3. Identified Gaps / Information Needed  

1. **Intended use & risk classification** – essential to determine Class I‑IV and thus the submission route.  
2. **AI/ML algorithm details** – training data provenance, validation results, post‑market monitoring plan (if applicable).  
3. **KGMP compliance evidence** for software development environment (for Class II‑IV).  
4. **Clinical evaluation report** – local clinical data or accepted foreign CE/FDA data with MFDS notice justification.  
5. **Exact regulatory reference for S‑4, S‑5, and S‑9** – while mandatory per the checklist, the specific legal citation (e.g., article number) is not present in the excerpt; must be verified in the full “디지털의료제품법 시행규칙”.  
6. **Full labeling package** – Korean language IFU covering all items above plus manufacturer contact details, intended user, and disposal instructions.  

---

### 4. Core Risk Controls (to be reflected in submission)

| Control | MFDS Basis | Implementation Note |
|---------|-----------|----------------------|
| **Version & build control** | 시행규칙 §… (software identification) | Unique version identifier on label; change‑control log. |
| **Update management** | SW 가이드라인 | Defined update schedule, remote/onsite mechanisms, validation after each update. |
| **System requirement specification** | SW 가이드라인 | Minimum hardware specs listed; compatibility testing documented. |
| **Cybersecurity safeguards** | 사이버보안 가이드라인 2025.01 | Encryption (AES‑256), network segmentation, role‑based access control, vulnerability scanning. |
| **Patch & vulnerability handling** | Same as above | SOP for patch release within 30 days of CVE disclosure; responsibility matrix. |
| **Residual risk mitigation** | Same as above | Risk register with residual risk scores < 3 (on a 1‑5 scale); fallback mode defined. |
| **Backup & recovery** | Internal policy (aligned to MFDS expectations) | Daily incremental, weekly full backup; restore test quarterly. |
| **Log management** | Recommended by cyber guide | Syslog centralization, log retention ≥ 12 months, audit trail for configuration changes. |
| **AI/ML transparency (if used)** | MFDS AI‑Guideline (2024) – not in excerpt but part of current policy | Model description, performance metrics, re‑training schedule, human‑in‑the‑loop safeguard. |

---

### 5. Citations  

- **디지털의료제품법 시행규칙** – mandatory for S‑1, S‑2, S‑3 and labeling items.  
- **MFDS SW 가이드라인** – basis for S‑2, S‑3.  
- **MFDS 사이버보안 가이드라인 2025.01** – applies to S‑6 ~ S‑8 (mandatory) and S‑10 (recommended).  
- **디지털의료기기 특화 표시기재 요건 체크리스트** – source excerpt [1] for the full list of required IFU elements; source excerpt [2] confirms that these items are *additional* to general medical device labeling.  

> No specific identifier (e.g., 510(k), CE‑Mark number, case ID) appears in the supplied excerpts – **no specific identifier found in source — verify separately**.

---

### 6. Human‑Escalation Triggers  

| Trigger | Why it requires senior review / escalation |
|--------|--------------------------------------------|
| **Unresolved device class** (missing intended use/risk analysis) | Determines whether a simple notification or full 허가 is required; misclassification can halt the submission. |
| **Absence of AI/ML transparency documentation** (if applicable) | MFDS recently tightened AI‑medical‑device oversight; omission leads to rejection. |
| **Missing KGMP certification evidence for software development** (Class II‑IV) | KGMP is a prerequisite for approval; must be confirmed before filing. |
| **Lack of local clinical data or unverified foreign evidence acceptance** | MFDS may request additional trials; early escalation to Clinical Affairs needed. |
| **Incomplete Korean IFU/labeling** (any mandatory S‑# item omitted) | Regulators reject on labeling grounds; must be corrected before submission. |
| **Unaddressed residual cyber‑risk > acceptable threshold** | Could trigger post‑market surveillance concerns; risk management lead should reassess mitigation measures. |

When any of the above triggers are hit, the RA team should:

1. Notify the Project Lead and Clinical/Risk Management leads immediately.  
2. Open a “Regulatory Gap” work package for each missing element with clear owners and timelines.  
3. Escalate to senior RA manager if classification or clinical evidence gaps cannot be resolved within 2 weeks.

---

### 7. Peer‑Review Prompt  

> **To a fellow Korean‑RA colleague:** Please review the assumptions made about the device’s risk class, the completeness of the cyber‑security controls relative to the 2025.01 guideline, and any potential jurisdiction‑specific gaps (e.g., local clinical data requirements, KGMP scope for software). Highlight any missing citations or alternative interpretations of the checklist items that could affect our submission strategy.

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

### kb-eval-20260721-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "1347e6dd14cc6def", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

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

> **Regulatory Draft – Digital‑Medical Device (DM‑Device) – “Clinical Efficacy Evidence” Issue**

---

### 1. Likely Classification / Submission Route  

| Korean Law | Interpretation of the excerpt | Implied device class* |
|------------|------------------------------|-----------------------|
| **법 제15조** – “실사용 평가” (real‑world evidence) | The source flags that clinical efficacy/evaluation is *not* covered by §15 but belongs to §§9 or 10. | Low‑to‑mid risk (Class I–II) would rely on RWE only; however, because the device requires **clinical trial plan approval** under §§9/10, it is more consistent with a **higher‑risk class (III or IV)** that mandates formal clinical performance testing and MFDS 허가. |
| **법 제9조** – “임상시험계획 승인” | Clinical efficacy must be demonstrated through an approved clinical trial plan. | Class III/IV (허가) |
| **법 제10조** – “임상적 성능시험계획 승인” | Alternate pathway for performance‑based evaluation of certain software/AI devices. | Class III/IV (허가) |

\*The exact class cannot be confirmed from the excerpt alone; further product‑specific risk analysis is required.

> **Draft determination:** The device is expected to fall under **MFDS 허가** (approval) pathway, not 신고 (notification), because clinical efficacy must be substantiated via an approved clinical trial plan (§9 or §10).

---

### 2. Required Evidence Package  

| Requirement | Source Basis | What Must Be Submitted |
|-------------|--------------|------------------------|
| **Clinical trial/clinical performance plan approval** | The audit note: “임상적 유효성 … 법 제9조(임상시험계획 승인) 또는 제10조(임상적 성능시험계획 승인)”【399070733591760115】 | • Approved clinical trial protocol (or performance test plan) filed with MFDS <br>• Informed consent forms, IRB approval <br>• Monitoring and safety reporting procedures |
| **Technical Documentation (Technical file / Design dossier)** | Implicit – required for any 허가 submission. | • Device description, intended use, architecture <br>• ISO 13485‑based quality system evidence <br>• Risk Management File (ISO 14971) <br>• Software Lifecycle documentation (if applicable) |
| **Safety & Performance Evidence** | Separate from §15 “실사용 평가”. | • Bench testing data <br>• Validation of algorithms/software <br>• Cybersecurity assessment (refer to 법 제13조 – continuous vulnerability mitigation) |
| **Real‑World Evidence (RWE) – optional supplement** | Law §15 defines RWE as *separate* from clinical efficacy. | • Post‑market data collection plan <br>• Real‑world usage logs (Korean language) |
| **KGMP Certification** | Required for manufacturing of any DM‑device seeking 허가. | • KGMP facility certificate, process validation records |
| **Labeling & IFU in Korean** | General MFDS requirement (no specific excerpt needed). | • Korean language label, user manual, safety notices |

> **Citation note:** All statutory references are directly taken from the source excerpts; no additional identifiers (e.g., predicate numbers) were present.

---

### 3. Missing / Unclear Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Exact legal provision to cite for clinical efficacy** – The excerpt recommends correcting “법 제15조” to §§9 or 10, but does not specify which of the two applies. | Determines whether a full clinical trial (§9) or a performance‑test plan (§10) is needed, affecting scope and timeline. | Conduct product‑specific risk analysis; decide between §9 and §10 and prepare the corresponding submission dossier. |
| **Device classification decision** – No explicit class (Ⅰ–Ⅳ) identified in source. | Classification drives dossier depth, required fees, and review timeline. | Apply MFDS “Risk‑Based Classification Guidelines” (e.g., based on invasiveness, duration of use, AI/algorithm impact). Document justification. |
| **Korean language requirements for labeling & IFU** – Not mentioned in excerpt but obligatory. | Failure leads to non‑conformity findings during review. | Prepare Korean‑language label and instructions; include translation verification plan. |
| **Post‑market surveillance (PMS) plan** – No reference in excerpts. | Required for 허가 devices, especially Class III/IV. | Draft PMS plan aligned with MFDS “시판후조사” guidelines; submit as part of technical file. |
| **AI change‑management plan (PCCP)** – Mentioned under §17 but noted as unrelated. | If the device contains AI, a change‑control plan may still be required under separate AI‑specific guidance. | Verify whether PCCP is needed per MFDS AI‑medical‑device guidance; prepare if applicable. |

---

### 4. Risk Controls (Core Elements)  

1. **Risk Management File** – ISO 14971 compliant, with risk acceptability criteria mapped to MFDS safety standards.  
2. **Cybersecurity Controls** – Continuous vulnerability monitoring and patch management per 법 제13조 (mandatory defect‑information collection & cyber‑vulnerability mitigation).  
3. **Clinical Safety Monitoring** – Real‑time adverse event reporting system linked to MFDS 사전상담 if required (§39 pre‑review).  
4. **Change Management** – Documented procedures for software/AI updates; even though §17 is “우수 관리체계 인증”, ensure alignment with any AI‑specific MFDS guidance.  

---

### 5. Citations (as required)

| Item | Citation |
|------|----------|
| Law §15 – definition of “실사용 평가” (RWE) | 디지털의료제품법 제15조【515031043224754498】 |
| Law §9 – clinical trial plan approval (mentioned in audit comment) | 임상적 유효성/임상평가는 법 제9조(임상시험계획 승인)…【399070733591760115】 |
| Law §10 – clinical performance test plan approval (mentioned in audit comment) | 임상적 유효성/임상평가는 …제10조(임상적 성능시험계획 승인)…【399070733591760115】 |
| Law §13 – defect info & cyber‑vulnerability obligations | 디지털의료제품법 제13조 (결함정보 수집·사이버 취약점 보완 등)【515031043224754498】 |
| Law §39 – pre‑review/consultation procedure | 디지털의료제품법 제39조 (허가·신고 등의 사전 검토)【515031043224754498】 |

*No case‑level identifiers (e.g., 510(k), predicate numbers) appeared in the source; therefore: **“no specific identifier found in source — verify separately.”***

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for Escalation |
|---------|-----------------------|
| **Unresolved classification** – lack of clear class decision after risk analysis. | Requires senior RA or MFDS pre‑consultation (법 §39) to avoid mis‑filing. |
| **Mismatch between intended evidence and statutory provision** – still citing §15 for clinical efficacy. | Immediate correction needed; senior review to select §§9/10 correctly. |
| **Absence of KGMP certification** – manufacturing site not yet certified. | Must halt submission until KGMP audit completed; involve Quality Assurance lead. |
| **Cybersecurity gaps identified** – no vulnerability management plan aligned with §13. | Escalate to IT‑Security & Compliance teams for rapid remediation. |
| **AI change‑management ambiguity** – uncertain whether PCCP applies. | Seek input from AI‑medical‑device specialist and possibly MFDS advisory meeting. |

If any of the above triggers are hit, **pause the submission build** and notify a senior regulatory manager for guidance before proceeding.

---

### 7. Reusable RA Judgment (Memory Outcome)  

> *When an audit or internal review flags that clinical efficacy evidence has been incorrectly linked to 디지털의료제품법 §15 (“실사용 평가”), the correct statutory basis is either **제9조** (clinical trial‑plan approval) or **제10조** (clinical performance‑test‑plan approval). The appropriate pathway dictates a 허가 submission for higher‑risk devices (Class III/IV). RWE under §15 can be submitted only as supplemental post‑market evidence, not as primary efficacy proof. Ensure the technical file contains an approved clinical protocol (or performance plan), KGMP certification, Korean language labeling, a complete risk management file, and compliance with cyber‑vulnerability obligations (§13). Any uncertainty in classification or statutory citation must trigger MFDS pre‑review under §39.*  

---  

**Peer Review Prompt**

> @RA‑colleague: Please assess whether the assumption that §§9/10 automatically imply a Class III/IV 허가 route is justified for this device, and verify if any additional MFDS guidance (e.g., AI‑specific guidelines) might modify the evidence requirements. Also confirm coverage of all statutory citations against the latest 디지털의료제품법 amendment (effective 2026‑01‑24).

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

### kb-eval-20260721-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-21", "decision_ref": "kb-eval-20260721-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "5cfb70d29c7cfdeb", "source": "github:holee9/MD-process/issue-drafts/956_AUDIT_디지털의료제품법_요구사항_매트릭스_DR02_조항_인용부정확.md", "source_hash": "6e02eaedc1e24e41f1a1bf208b930a59f96d8b39f382a3eeb018e5f289d2d799"} -->

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

> **Regulatory Draft – Digital Medical Device Manufacturing License (제조업 허가) & Quality‑Management‑Standard Conformity Assessment (품질관리기준 적합 판정)**  

---

### 1. Applicable Legal Basis  
| Law / Article | Scope Referenced in Source | Corresponding Implementation Regulation (“시행규칙”) |
|---------------|----------------------------|------------------------------------------------------|
| **법 제8조** (제조업허가·제조허가·제조인증·제조신고) | Core authority for granting a manufacturing licence and the related quality‑management requirements (품질책임자 배치·시설/품질관리체계 기준 포함). | 시행규칙 제5~13조 – e.g., “법 제8조제1항 전단에 따라 디지털의료기기 제조업허가를 받으려는 자는 …” |
| **법 제11조** (디지털의료기기 변경허가 등) | Governs post‑licence changes to “important matters” (변경허가/변경인증/변경신고). | 시행규칙 제23조 – defines the “총리령으로 정하는 중요한 사항”. |
| **법 제15조** (실사용 평가) | Requirement for real‑world use evaluation of the device. | 시행규칙 제30조. |
| **법 제16조** (우수 관리체계 인증) | Mandatory certification of an excellent management system (KGMP‐equivalent). | 시행규칙 제31~32조. |
| **법 제40조** (디지털의료제품 구성요소 성능평가 – 센서·AI) | Performance assessment for critical components such as sensors and AI algorithms. | 시행규칙 제50조. |

*The source explicitly notes that the “제조업 허가 + 품질관리기준 적합 판정” requirement is **grounded in 법 제8조**, not 법 제11조 (see Chunk 200576646193092927 & Chunk 403794146442956433).*

---

### 2. Classification / Submission Route  

| Item | Determination Needed |
|------|----------------------|
| **Risk‑class (1‑4)** | The source does not disclose the device’s risk class or intended use. Identify the appropriate class under the Digital Medical Device Act (DMDA) – e.g., Class II for diagnostic software, Class III for AI‑driven therapeutic decision support, etc. |
| **Submission Type** | For a manufacturing licence: **제조업 허가 신청** (manufacturing‑license application). If the device is already marketed and requires a change, the route would be **법 제11조에 따른 변경허가/인증/신고**. |

*Human escalation*: If risk classification cannot be conclusively assigned from available product information, elevate to senior RA for an expert clinical‑risk assessment.

---

### 3. Required Evidence Package  

| Requirement (Legal Basis) | Evidence Needed | Comments / Gaps |
|---------------------------|----------------|-----------------|
| **법 제8조 – 제조업 허가** | • Business registration & corporate seal.<br>• Appointment letter for 품질책임자 (Quality‑Responsible Person).<br>• Facility layout, equipment list, and SOPs demonstrating compliance with the quality‑management criteria in 시행규칙 제5~13조. | *Missing*: Detailed facility/QA documentation. |
| **법 제16조 – 우수 관리체계 인증** | • KGMP (Korean Good Manufacturing Practice) certification or evidence of compliance with ISO 13485 plus MFDS‑approved QA audit report. | *Missing*: KGMP certificate copy; audit report. |
| **법 제40조 – Component Performance (센서·AI)** | • Bench‑test data for sensors (accuracy, precision, stability).<br>• AI algorithm validation reports (training dataset description, performance metrics, bias analysis) consistent with MFDS guidance on AI/ML medical devices.<br>• If using foreign clinical evaluation, a cross‑reference to MFDS acceptance notice for overseas data (to be verified). | *Missing*: Korean‑specific clinical validation for AI output; evidence of OECD‑aligned non‑clinical testing if applicable. |
| **법 제15조 – 실사용 평가** (if class ≥ II) | • Real‑world use study protocol and interim results, including safety endpoints.<br>• Post‑market surveillance plan (시판후조사) aligned with MFDS requirements. | *Missing*: Draft or completed real‑use evaluation report. |
| **법 제11조 – 변경허가** *(only if post‑licence changes are planned)* | • Change impact analysis, revised specifications, updated risk management file. | Not applicable at initial licence; flag only when modifications arise. |

---

### 4. Identified Missing Information & Immediate Actions  

1. **Device Risk Class & Intended Use** – obtain product specification sheet and intended‑use statement.  
2. **KGMP Certification** – request current KGMP certificate or schedule MFDS‑approved audit.  
3. **Component Performance Data** – collect Korean‑language validation reports for sensors and AI; confirm whether existing foreign data are acceptable under the latest MFDS notice on overseas evidence (to be retrieved).  
4. **Quality Management System Documentation** – compile SOPs, facility drawings, personnel qualifications as per 시행규칙 제5~13조.  
5. **Real‑World Use Evaluation Plan** – draft protocol if device class triggers 법 제15조.  

*Human escalation*: If any of the above items cannot be supplied within 30 days, senior RA must decide whether to defer submission or seek a conditional exemption from MFDS.

---

### 5. Risk Controls (Mapping to Korean Requirements)  

| Hazard Category | Control Measures | Relevant Standard / Guidance |
|-----------------|------------------|------------------------------|
| **Software/AI algorithm error** | • ISO 14971‑based risk analysis.<br>• Continuous performance monitoring plan.<br>• Cybersecurity safeguards per MFDS “디지털 의료기기 사이버보안 가이드라인”. | IMDRF Software Life Cycle Guidance; Korean Cybersecurity Guideline (KISA). |
| **Sensor inaccuracy** | • Calibration procedures, periodic re‑verification.<br>• Redundant measurement where feasible. | IEC 60601‑1‑6 (Usability) and IEC 62304 (Software). |
| **Data privacy breach** | • De‑identification of patient data.<br>• Encryption during transmission/storage (AES‑256). | Personal Information Protection Act (PIPA) & MFDS “디지털 의료기기 데이터 관리 지침”. |
| **Manufacturing process deviation** | • In‑process controls, batch release testing.<br>• QC sampling per KGMP. | Korean GMP Guideline; ISO 13485 §7.5. |

---

### 6. Citation Summary (Established Regulatory References)  

- 법 제8조 – 제조업허가·제조허가·제조인증·제조신고 (시행규칙 제5~13조).  
- 법 제11조 – 디지털의료기기 변경허가 등 (시행규칙 제23조).  
- 법 제15조 – 실사용 평가 (시행규칙 제30조).  
- 법 제16조 – 우수 관리체계 인증 (시행규칙 제31~32조).  
- 법 제40조 – 구성요소 성능평가(센서·AI) (시행규칙 제50조).  

*No case‑specific identifiers (e.g., predicate 510(k) numbers) appear in the source; therefore “no specific identifier found in source — verify separately” is recorded for that item.*

---

### 7. Regulatory Judgment & Human‑Escalation Triggers  

| Decision Point | Trigger for Human Review |
|----------------|--------------------------|
| **Risk class cannot be determined** | Escalate to senior RA / clinical expert. |
| **KGMP certificate absent or out‑of‑date** | Pause submission; seek senior approval for alternative compliance path (e.g., ISO 13485 audit). |
| **Foreign AI performance data only** | Verify receipt of MFDS notice approving such evidence; if not, escalate to RA manager for risk‑based justification. |
| **Change after licence is anticipated** | Initiate 법 제11조 change‑approval process; involve regulatory project lead. |
| **Real‑world use evaluation required but plan missing** | Escalate to clinical trial unit for protocol development. |
| **Any discrepancy between cited legal basis and actual requirement (e.g., mis‑citing 법 제11조 for 제조업 허가)** | Immediate correction by the RA team; senior oversight required before resubmission. |

*If any of the above triggers are activated, the case must be flagged in the project tracking system and a formal escalation email sent to the RA manager with a detailed gap list.*

---

### 8. Peer Review Prompt  

> **To a fellow RA colleague:**  
> Please examine this draft for (a) completeness of the Korean legal citations, (b) any overlooked jurisdiction‑specific requirements such as language‑only labeling or mandatory Korean clinical data for AI components, and (c) whether the identified missing information aligns with MFDS’s latest notice on accepted foreign evidence. Highlight any assumptions that need further source verification.

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

1. Chunk `200576646193092927`

> ## 1차 출처 정답 (디지털의료제품법 시행규칙, 총리령 제2025호, 2025-02-28 시행 — 법 조문 인용 부분) 시행규칙 각 조에서 확인된 법 조문 대응관계: | 법 조문 | 내용 | 시행규칙 근거 | |---|---|---| | **법 제8조** | **제조업허가·제조허가·제조인증·제조신고**(품질책임자 배치·시설/품질관리체계 기준 포함) | 시행규칙 제5~13조 (제5조 "법 제8조제1항 전단에 따라 디지털의료기기 제조업허가를 받으려는 자는...") | | 법 제9조 | 임상시험계획 승인 | 시행규칙 제14~18조 | | 법 제10조 | 임상적 성능시험계획 승인 | 시행규칙 제19~22조 | | **법 제11조** | **디지털의료기기 변경허가 등**(제조업허가·제조허가 후 중요사항 변경) | 시행규칙 제23조 ("법 제11조제1항 전단에서 '총리령으로 정하는 중요한 사항'이란...") | | 법 제15조 | 실사용 평가 | 시행규칙 제30조 | | 법 제16조 | 우수 관리체계 인증 | 시행규칙 제31~32조 | | 법 제40조 | 디지털의료제품 구성요소 성능평가(센서·AI) | 시행규칙 제50조 | 즉 DR-02 "제조업 허가 + 품질관리기준 적합 판정"의 정확한 근거는 **법 제8조**이며, 법 제11조(변경허가)는 최초...

2. Chunk `403794146442956433`

> ## 독립 감사 요약 DR-02 항목은 "제조업 허가 + 품질관리기준 적합 판정" 요구사항의 근거를 **법 제11조**로 인용하나, Tier 1(디지털의료제품법 시행규칙 원문, 총리령 제2025호) 재확인 결과 **법 제11조는 "디지털의료기기 변경허가 등"**(제조 완료 후 중요사항 변경 시 변경허가/변경인증/변경신고) 조항이다. 제조업허가·제조허가·제조인증·제조신고의 근거는 **법 제8조**이다.
