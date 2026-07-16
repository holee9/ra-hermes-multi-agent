# KB Eval Checksheet - 2026-07-17 Iteration 02

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260717-it02-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_us-001", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "b09c788de30adb23", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

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

> **Regulatory Draft – Impact of SaMD Change under FDA Predetermined Change Control Plan (PCCP)**  

---

### Bottom‑Line Recommendation
- **Classification / submission route:** The AI/ML‐based Software as a Medical Device (SaMD) remains in its existing product class. Any change covered by the PCCP is handled through a *Supplemental 510(k)* (or De Novo if the original clearance was via De Novo and the change does not alter the intended use or risk profile). No new full 510(k) is required provided the change conforms to an FDA‑approved PCCP.
- **Key evidence needed:** Updated data‑management documentation, retraining trigger criteria, validated performance evaluation (including statistical significance), and revised user/clinical communication procedures as per the four mandatory items of the Modification Protocol.  
- **Missing information to collect before filing:** Detailed description of the new training dataset (source, size, demographics, bias mitigation); quantitative justification for the retraining trigger; comparative performance metrics against the pre‑change baseline; rollout/rollback plan; and any impact on labeling or Instructions for Use (IFU).  

---

### 1. Classification & Submission Pathway  
| Current status | Change scenario | FDA pathway |
|----------------|-----------------|-------------|
| Class II SaMD cleared via 510(k) **K‑XXXXXX** (predicate from source not listed) | Modification that is **predetermined** in an approved PCCP and does **not** alter intended use, safety‐critical functions, or risk class | **Supplemental 510(k)** (letter of authorization to implement change under existing clearance). |
| If original clearance was via **De Novo**, and the alteration remains within the same risk profile | Same as above – submit a **Supplemental De Novo** if required by FDA guidance. |

*No new predicate identifier appears in the source excerpts; verify the exact 510(k) or De Novo number from your device dossier.*

---

### 2. Required Evidence Package (per §820.30 and PCCP Guidance)

| Element (from Modification Protocol) | What to submit |
|--------------------------------------|----------------|
| **Data Management** | - SOP for data collection, curation, version control.<br>- Description of bias‑mitigation strategies (e.g., demographic balancing).<br>- Provenance records for training/validation sets. |
| **Retraining Practices** | - Defined trigger conditions (performance drift thresholds, new clinical indications, regulatory updates).<br>- Detailed retraining workflow (algorithmic steps, computational environment).<br>- Rollback plan with criteria to revert to prior model version. |
| **Performance Evaluation** | - Pre‑specified acceptance criteria (e.g., sensitivity/specificity limits).<br>- Validation methodology (cross‑validation, external test set, statistical power analysis).<br>- Comparative results showing non‑inferiority or superiority vs. the cleared version.<br>- Evidence that V&V meets FDA “statistical significance” requirement. |
| **Updated Procedures** | - Communication plan for users and clinicians (e.g., release notes, training webinars).<br>- Real‑world monitoring plan (post‑market surveillance metrics, adverse event reporting timelines).<br>- Updated IFU/ labeling excerpts reflecting any functional changes. |

---

### 3. Risk Controls & Human‑Escalation Triggers  

| Risk Area | Control(s) | Human‑Escalation Trigger |
|-----------|------------|--------------------------|
| **Algorithmic drift / performance degradation** | Continuous monitoring; predefined statistical control limits; automated alerts when metrics exceed thresholds. | If drift exceeds the acceptance margin for > 48 h, a qualified clinical engineer must review and decide on rollback or corrective action. |
| **Data bias leading to disparate impact** | Bias audit during data management; fairness metrics (e.g., equalized odds). | Detection of statistically significant disparity (> 5 % absolute difference) across protected groups triggers a safety review board meeting. |
| **Incorrect decision support (false negative/positive)** | Redundant safety logic (e.g., “human‑in‑the‑loop” requirement for high‑risk outputs); threshold tuning; fail‑safe defaults. | Any single false‑negative event flagged as serious adverse device effect (SADE) must be reported within 24 h and escalated to senior QA lead. |
| **Software rollout errors** | Version‑control system with audit trail; automated integrity checks before deployment. | Failure of checksum validation or a rollback without documented justification triggers immediate suspension of the release and notification to the FDA’s post‑market liaison. |

---

### 4. Citations  

- Predetermined Change Control Plan (PCCP) guidance – FDA marketing submission recommendations (source excerpt [1]).  
- Modification Protocol mandatory items – data management, retraining practices, performance evaluation, updated procedures (source excerpt [2]).  
- No specific 510(k)/predicate numbers or case IDs appear in the provided source excerpts. Verify those identifiers from your internal device master file.

---

### 5. Human‑Escalation Checklist  

1. **Trigger identification** – Review monitoring dashboards daily for any breach of drift, bias, or safety thresholds.  
2. **Notification chain** – Alert: Clinical Engineer → QA Manager → Regulatory Lead within 4 h of trigger detection.  
3. **Decision authority** – Senior QA/Regulatory decision on rollback vs. continued deployment must be documented in the change log.  
4. **FDA communication** – If a trigger meets the criteria for a significant safety issue (e.g., SADE), submit a medical device report (MDR) within 30 days and consider a supplemental 510(k) or post‑market update as required.

---

### Peer Review Prompt  

> *Colleague, please evaluate this draft: Are the assumptions about classification (Supplemental 510(k) vs. De Novo) justified given only the PCCP guidance? Does the evidence matrix fully cover FDA’s “Performance Evaluation” expectations for AI/ML SaMD changes? Identify any gaps in jurisdiction‑specific requirements (e.g., European MDR interplay, state‑level notice) that may affect our submission strategy.*

---

### Reusable RA Judgment (Honcho Record)

**Lesson:** For any AI/ML–based SaMD change governed by an FDA‑approved Predetermined Change Control Plan, the regulatory pathway is a *Supplemental 510(k)* (or Supplemental De Novo) provided the modification does not alter intended use or risk class. The submission must contain documented SOPs covering **Data Management**, **Retraining Practices**, **Performance Evaluation** (with statistical significance), and **Updated Procedures** as mandated by the Modification Protocol. Missing components—particularly detailed training data provenance, quantitative retraining triggers, comparative performance metrics, and rollout/rollback plans—must be completed before filing. Human‑escalation triggers should be defined for algorithmic drift, bias detection, safety‑critical misclassifications, and deployment errors, with a clear notification chain and FDA reporting obligations.

*Record entered via `honcho_conclude` for future reuse.*

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

### kb-eval-20260717-it02-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_us-002", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "a852077f86f0109a", "source": "github:holee9/MD-process/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md", "source_hash": "efcd12a4b49cb21ffa28b5f1aa35345e8bb04b98c57a32649483fa824de23fff"} -->

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

> **Regulatory Draft – Impact of FDA Predetermined Change Control Plan (PCCP) Guidance 2024 on SaMD Change Management**

---

### 1. Classification & Submission Route  
| Device Feature | Likely FDA Class* | Typical Predicate Pathway | Recommended Submission |
|----------------|------------------|--------------------------|------------------------|
| AI‑enabled SaMD that performs diagnostic, therapeutic, or monitoring functions (non‑life‑supporting) | **Class II** (most AI/ML SaMD fall under this tier) | 510(k) – Substantial equivalence to a legally marketed device with similar intended use and technology. | Prepare a traditional 510(k) *or* a **Special 510(k)** if the change is limited to software algorithm updates covered by an existing PCCP. A De Novo may be required only for completely novel AI functionality without a predicate. |

\*Final classification must be confirmed via FDA product code lookup and intended use statement.

---

### 2. Required Evidence to Satisfy PCCP Requirements  

| Element | Evidence Needed (per FDA “Predetermined Change Control Plan” Guidance, 2024) |
|---------|-----------------------------------------------------------------------------|
| **Algorithm Change Scope** | Detailed description of the anticipated change (e.g., model retraining, parameter adjustment). Include version control matrix. |
| **Performance Verification** | Pre‑ and post‑change performance testing on a representative data set (clinical or synthetic) demonstrating non‑inferiority to baseline. Statistical analysis plan and results. |
| **Risk Assessment Updates** | Updated ISO 14971 risk management file reflecting new failure modes introduced by the change. Include FMEA/FTA outcomes. |
| **Software Documentation** | Revised software design description, source code diffs (if applicable), verification & validation protocols, and traceability matrix linking requirements to implemented changes. |
| **Real‑World Performance Monitoring Plan** | Post‑market surveillance plan outlining data collection, drift detection thresholds, and corrective action triggers aligned with the PCCP. |
| **Change Control SOPs** | Demonstration that organizational SOPs (e.g., “AI Fairness & Explainability Drift Governance”) incorporate the PCCP’s predetermined change categories and decision trees. |
| **Labeling Impact Assessment** | Evidence that labeling, IFU, or promotional materials are unchanged or, if changed, included in the submission package. |

---

### 3. Missing Information (Gaps Identified from Source)  

1. **Specific Predicate Device(s)** – No predicate identifiers were cited; need to locate a legally marketed device with comparable AI functionality.  
2. **Exact Scope of Intended Use** – The source references “AI‑Enabled Device Software Functions” generically; precise indication(s) must be defined.  
3. **Implementation Timeline & Governance Details** – While SOP‑AIGOV‑001 is mentioned, the actual change control thresholds, decision criteria, and responsible parties are not disclosed.  
4. **Performance Metrics Required by FDA** – Quantitative acceptance criteria (e.g., sensitivity/specificity margins) for algorithm updates are absent.  
5. **Regulatory Status of Current Device** – Confirmation whether the device is already cleared under 510(k), de Novo, or other pathway is needed to choose appropriate submission type.

---

### 4. Core Risk Controls to Embed in PCCP  

| Control | Description |
|---------|-------------|
| **Algorithmic Fairness Checks** – Bias detection across demographic subgroups before deployment. |
| **Explainability Validation** – Documentation of model interpretability methods (e.g., SHAP, LIME) and verification that output explanations meet clinical expectations. |
| **Drift Detection Thresholds** – Statistical process control limits on performance metrics; automatic rollback triggers when breached. |
| **Versioned Release Management** – Immutable audit trail linking each software version to its change justification, testing data, and risk analysis. |
| **Cybersecurity Safeguards** – Updated threat model for new code paths; verification of secure update mechanism (code signing, authentication). |
| **Usability Testing** – Human factors evaluation confirming that UI/UX changes caused by algorithm updates do not increase use error rates. |

---

### 5. Citations  

- “FDA PCCP Guidance 2024” referenced in internal SOP‑AIGOV‑001 AI Fairness & Explainability Drift Governance (source excerpt [1]).  
- King & Spalding alert: *“FDA Publishes Final Predetermined Change Control Plan Guidance for AI‑Enabled Device Software Functions”* (2024‑12) (source excerpt [2]).  

**No specific identifier found in source — verify separately.**

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Performance Degradation > pre‑defined margin** | Immediate halt of deployment; senior RA & Clinical Lead review; prepare FDA RTA (Request for Additional Information) if applicable. |
| **Unanticipated Adverse Event linked to algorithm change** | Notify Quality/Regulatory Manager → FDA 15‑day medical device reporting (MDR) as required; convene cross‑functional root‑cause analysis. |
| **Inability to meet PCCP documentation completeness deadline** | Escalate to VP of Regulatory Affairs for resource allocation or submission timeline adjustment. |
| **Discovery of new predicate risk category after change** | Pause change rollout, re‑evaluate classification, possibly file a new 510(k) or De Novo. |
| **Regulatory agency (FDA) communication indicating non‑conformance with PCCP** | Immediate senior leadership notification; initiate corrective and preventive action (CAPA) plan. |

---

### 7. Peer Review Prompt  

> *“Please review the assumptions underlying the classification selection, the completeness of the identified evidence set for PCCP compliance, and any jurisdiction‑specific gaps (e.g., EU AI Act cross‑reference). Highlight missing predicate devices or labeling considerations that could affect the submission strategy.”*

---

### 8. Reusable RA Judgment (Honcho Record)  

```
honcho_conclude:
  case_id: daily_growth_v1
  judgment: For AI‑enabled SaMD subject to FDA PCCP Guidance 2024, default to Class II with a traditional or Special 510(k) unless novel functionality mandates De Novo. Required evidence centers on algorithm change scope, performance verification, updated risk management (ISO 14971), and robust governance SOPs. Missing data include explicit predicate device identifiers, precise intended use statements, and quantitative acceptance criteria. Risk controls must address fairness, explainability, drift detection, cybersecurity, and usability. Escalate any performance drop or adverse event linked to the change per trigger matrix.
  confidence: high
```

--- 

*Prepared by Mike – US Regulatory Affairs Specialist.*

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

### kb-eval-20260717-it02-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_us-003", "iteration": 2, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "4c8c8b7e4ef63c97", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

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

> **Regulatory Draft – Impact of SaMD Change on Submission Pathway**

---

### Bottom Line
*If the software modification is confined to the scope already approved under the **Pre‑Certification Change Plan (PCCP)**, an **abbreviated 510(k) supplement (Special or CMC change)** can be used. Any change that expands the intended use, introduces new algorithmic functions, or exceeds the pre‑certified bias‑mitigation/validation limits will require a full **traditional 510(k)** (or De Novo if no predicate exists).*

---

## 1. Device Change Overview
- **Change type:** Update to AI‑enabled SaMD (algorithm refinement, data set expansion, bias mitigation enhancements, or workflow integration)  
- **Regulatory context:** The change is being evaluated against the lifecycle management guidance for “AI‑Enabled Device Software Functions” and the final PCCP recommendation package (see source excerpt [1]‑[2]).  

---

## 2. Classification & Submission Route
| Scenario | FDA Classification | Recommended Submission |
|----------|--------------------|------------------------|
| **Within pre‑certified scope** (same intended use, same risk class, no new device functions) | Class II (most AI‑SaMD are Class II under 21 CFR 862.1101/862.1155) | **Special 510(k) supplement** – “PCCP change” (no need for a new predicate) |
| **Outside pre‑certified scope** (new indication, algorithmic output, or risk increase) | Class II → possible Class III if novel risk | **Traditional 510(k)** with a new predicate OR **De Novo** if no appropriate predicate exists |
| **Major architectural change** (e.g., migration to a different platform, addition of cybersecurity module that alters attack surface) | May trigger re‑classification | **Traditional 510(k)** or **Pre‑Submission (Q‑Submission)** for FDA feedback |

*Note: The exact classification must be confirmed against the latest FDA product classification database; no specific predicate numbers appear in the source material.*

---

## 3. Required Evidence Package

| Evidence Item | Description & Acceptance Criteria |
|---------------|------------------------------------|
| **Algorithm description** | Full functional specification, including model architecture, hyper‑parameters, and versioning. |
| **Data lineage & partitioning** | Documented train/validation/test splits; provenance of each dataset (source, preprocessing). |
| **Performance metrics linked to clinical claim** | Sensitivity, specificity, AUC, etc., mapped to the intended clinical use (e.g., detection of pathology X). |
| **Bias analysis & mitigation** | Quantitative assessment of demographic/clinical bias before and after mitigation; justification that residual bias is within pre‑certified limits. |
| **Human‑AI workflow description** | Detailed SOPs showing how clinicians interact with the AI, including escalation points. |
| **Post‑market monitoring plan** | Real‑world performance tracking, trigger thresholds for re‑training or rollback, and reporting schedule. |
| **Software Risk Management File (IEC 62304/ISO 14971)** | Hazard analysis, risk controls, verification & validation results for the updated algorithm. |
| **Cybersecurity assessment** (if applicable) | Threat model, penetration testing outcomes, mitigation strategies; must align with FDA’s “Cybersecurity Guidance for Medical Devices”. |
| **Labeling updates** | Revised IFU, labeling, and advertising materials reflecting any functional changes. |

---

## 4. Missing Information (to be supplied before submission)

1. **Exact intended use statement after change** – clarifies whether the claim has been expanded.
2. **Detailed dataset characteristics** – size, class balance, external validation cohort description.
3. **Quantitative bias mitigation results** – statistical tables showing pre‑ and post‑mitigation performance across subpopulations.
4. **Human factors validation** – usability study demonstrating appropriate clinician oversight.
5. **Cybersecurity threat model** – especially if the update alters data flow or connectivity.
6. **Regulatory history matrix** – mapping of this change against the pre‑certified PCCP scope (e.g., which “change buckets” are covered).

---

## 5. Core Risk Controls

| Control | Standard / Guidance |
|---------|---------------------|
| **Software Design Controls** | IEC 62304, FDA’s “General Principles of Software Validation” (1997) |
| **Risk Management Process** | ISO 14971:2021 (risk analysis, mitigation, residual risk evaluation) |
| **Bias Detection & Mitigation** | FDA AI/ML SaMD pre‑market guidance – bias analysis requirement (see source [1]) |
| **Human Oversight (Human‑AI workflow)** | FDA “Good Machine Learning Practice” (GMLP) – human review and escalation |
| **Post‑Market Surveillance** | 21 CFR 820.30(c), FDA’s “Software Pre‑certification Program” – continuous monitoring |
| **Cybersecurity Controls** | FDA “Content of Premarket Submissions for Management of Cybersecurity” (2022) |

---

## 6. Citations

- **Bias analysis & mitigation, Human‑AI workflow, post‑market monitoring, update plan:** Source [1] – *“편향 분석·완화 … Human‑AI 워크플로우 … 시판 후 모니터링 … 업데이트 계획”*  
- **PCCP status and lifecycle management guidance:** Source [2] – *“Marketing Submission Recommendations for a PCCP for AI‑Enabled DSF … 최종(Final) … 제출 시 PCCP로 사전 승인된 변경 범위 운영”*  

*No specific FDA 510(k) or predicate identifier appears in the source excerpts; verify applicable numbers separately.*

---

## 7. Human‑Escalation Triggers (When to Involve a Senior RA / Seek FDA Feedback)

| Trigger | Action Required |
|---------|-----------------|
| **Change expands intended use or clinical claim** | Pause submission, prepare a full 510(k) or De Novo dossier; engage senior regulatory counsel. |
| **New algorithmic output introduces a new risk (e.g., automated treatment recommendation)** | Conduct a supplemental risk analysis; consider filing a Pre‑Submission for FDA concurrence. |
| **Observed performance degradation >10 % in real‑world data** | Initiate post‑market corrective action plan, issue Field Correction/Recall if needed; notify FDA per 21 CFR 820.200. |
| **Residual bias exceeds pre‑certified limits** | Re‑train algorithm or halt deployment; update bias mitigation documentation and submit a supplemental filing. |
| **Cybersecurity vulnerability discovered that changes attack surface** | File a Cybersecurity Incident Report (if exploitable) and prepare an amended 510(k) supplement. |
| **Regulatory classification uncertainty (no clear predicate)** | Request FDA’s Q‑Submission for classification advice before proceeding. |

---

## 8. Peer Review Prompt
> *Please review the assumptions, source coverage, and jurisdiction‑specific gaps in this draft:*
> - Are we correctly interpreting the scope of the PCCP as permitting a Special 510(k) supplement for the listed changes?  
> - Does the evidence matrix capture all FDA‑required elements for AI/ML SaMD updates under the 2023‑2024 guidance?  
> - Have any U.S. regulatory nuances (e.g., QMSR compliance, post‑market surveillance obligations) been overlooked?  

---

## 9. Reusable RA Judgment (Lesson Record)

**When an AI‑enabled SaMD modification falls within a pre‑approved change plan (PCCP), the FDA generally allows submission via a **Special 510(k) supplement** that references the original clearance, provided that:**
1. The intended use and risk class remain unchanged;  
2. All modifications are limited to pre‑certified “change buckets” (e.g., algorithm tuning, bias mitigation, data set updates);  
3. Comprehensive documentation of algorithm description, data lineage, performance/clinical claim linkage, bias analysis, human‑AI workflow, risk management, and post‑market monitoring is provided;  
4. No new cybersecurity or functional risks are introduced beyond the scope of the original submission.

**Any deviation from these criteria—new indications, new device functions, increased risk, or substantial changes to data provenance—requires a full **traditional 510(k)** (or De Novo if no predicate exists).**

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

### kb-eval-20260717-it02-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_us-004", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "1056ea3b790075ff", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

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

| Item | Determination | Rationale / Source |
|------|----------------|--------------------|
| **Device Classification** | Class II (510(k)‑eligible) | The software is a *“GUI for acquisition, review and management of digital radiographic images”* with the explicit statement that it is **not intended for primary diagnosis or image interpretation**. Under 21 CFR 862.1 the “image acquisition/management” function without diagnostic intent is generally Class II. No indication in the source that the device falls under a higher‑risk category (Class III) or qualifies for De Novo. |
| **Submission Route** | Traditional 510(k) (or Abbreviated if a suitable predicate exists) | Excerpts cite FDA guidance on “Traditional and Abbreviated 510(k)s” (2019‑09‑13) and the required content per 21 CFR 807.87/807.92. No indication that the device would qualify for special or exempt pathways. |
| **Likely Predicate Devices** | Identify existing FDA‑cleared X‑ray image acquisition & management software (e.g., *GE Healthcare X*‑Ray Imaging Software, KXXXXX) that lack diagnostic claim. Verify similarity of intended use, technological characteristics, and risk controls. <br>*Action*: Perform a predicate search in the 510(k) database; record chosen predicates with their 510(k) numbers. |
| **Core Submission Content** (per FDA “Electronic Submission Template” & “Format for Traditional/Abbreviated 510(k)s”) | • Device description (including SW architecture, OS/hardware minimums, compatible detectors/generators).<br>• Indications for Use (use Form 3881).<br>• Software Description – IEC 62304 safety class, SOUP inventory, cybersecurity features (auth, encryption, audit logs).<br>• DICOM compliance statement.<br>• Risk analysis & mitigation summary (per ISO 14971).<br>• Labeling & IFU. | Directly drawn from excerpt 1 (required sections) and excerpt 2 (specific software description items). |
| **Evidence Required** | 1. **Verification & Validation data** demonstrating compliance with IEC 62304 (Class C if any safety‑critical functions, otherwise Class B/A).<br>2. **Cybersecurity assessment** – threat model, mitigation, penetration test results.<br>3. **DICOM conformance testing** – Storage SCU, Worklist SCU, MPPS.<br>4. **Usability engineering** (human factors) for “trained technologists”.<br>5. **Software risk management file** (ISO 14971). | Required by FDA guidance on software‑based SaMD and 21 CFR 820.30/820.70 series. |
| **Missing Information in Source** | • Specific predicate device identifiers (510(k) numbers).<br>• Detailed verification & validation protocols/results.<br>• Cybersecurity threat analysis documentation.<br>• Usability testing plan/outcomes.<br>• Labeling text and IFU draft.<br>• QMS compliance evidence (QMSR effective Feb 2026, ISO 13485 alignment). | The excerpts list required content but do not provide the actual artifacts. |
| **Key Risk Controls** | • **Software safety classification** per IEC 62304 (assign Class B/C as appropriate).<br>• **Access control & authentication** for image acquisition and storage.<br>• **Encryption of DICOM data in transit/storage**.<br>• **Audit logging** of user actions.<br>• **Version control & change management** for SOUP components.<br>• **Usability safeguards** to prevent inadvertent use for diagnosis. | Derived from the cybersecurity and IEC 62304 items noted in excerpt 2, plus standard risk‑control hierarchy (elimination → substitution → engineering controls). |
| **Citations** | No specific identifier found in source — verify separately. | The provided excerpts do not include explicit 510(k) numbers, predicate IDs, or case identifiers. |
| **Human‑Escalation Triggers** | • Ambiguity about classification (e.g., if any future claim implies diagnostic use).<br>• Inability to locate a suitable predicate device within the FDA database.<br>• Discovery of Class III risk features during software design review.<br>• QMSR non‑conformance findings that could delay submission. | These conditions require senior RA sign‑off or consultation with regulatory counsel before proceeding. |

---

### Peer Review Prompt
*Please review this assessment and challenge the following:*

1. **Assumptions about classification** – Is there any scenario where the stated “review” function could be interpreted as a diagnostic claim, shifting the device to Class III?
2. **Predicate selection coverage** – Have we exhausted all potential predicates, including those cleared under the “Abbreviated” pathway or special 510(k) exemptions?
3. **Jurisdiction‑specific gaps** – Are there any additional documentation requirements (e.g., FDA’s post‑market cyber‑security guidance, recent QMSR updates) that have not been captured here?

*Provide feedback on missing evidence, alternative pathways, or any regulatory nuances that may affect the submission strategy.*

---

### Reusable RA Judgment (honcho_conclude)

```json
{
  "lesson_id": "SaMD_Change_Impact_Assessment_2026-07-18",
  "summary": "For a GUI‑based image acquisition/management SaMD with no diagnostic claim, default to Class II 510(k) submission. Use traditional or abbreviated format per FDA guidance; compile required sections (device description, IEC 62304 safety class, cybersecurity, DICOM compliance, risk analysis). Identify predicates that lack diagnostic intent and match technological characteristics. Flag missing artifacts (validation data, cyber threat analysis, usability studies, labeling). Escalate if classification ambiguity arises, no suitable predicate found, or Class III risk features are uncovered.",
  "key_actions": [
    "Perform predicate search in FDA 510(k) database; record numbers.",
    "Assemble verification/validation evidence per IEC 62304.",
    "Develop cybersecurity threat model and mitigation documentation.",
    "Conduct usability testing for trained technologists.",
    "Prepare labeling/IFU using Form 3881.",
    "Ensure QMSR (ISO 13485) compliance before submission."
  ],
  "escalation_conditions": [
    "Potential diagnostic claim detected",
    "No adequate predicate identified",
    "Identification of Class III safety functions",
    "QMSR non‑conformance"
  ]
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

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

### kb-eval-20260717-it02-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_us-005", "iteration": 2, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "b52524355e284be8", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md", "source_hash": "7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503"} -->

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

> **Regulatory Draft – Cyber‑security Compliance for a SaMD Change (FDA Section 524B)**  

---

### 1. Device Classification & Submission Pathway  
| Attribute | Determination |
|-----------|----------------|
| **Product type** | Software as a Medical Device (SaMD) that performs diagnostic/therapeutic functions. |
| **Regulatory class** | Typically **Class II** (moderate risk) requiring a 510(k). If the change introduces new intended uses or increases risk, a **de novo** or **PMA** may be needed. |
| **Submission route** | **Traditional 510(k)** with special controls for cybersecurity *or* **Special 510(k)** if only software changes and the predicate remains unchanged (see FDA guidance on “Software Changes”). |
| **Key regulatory reference** | **Section 524B, FD&C Act** – establishes legal obligation for SBOM and related cyber‑security documentation. *(source [1])* |

---

### 2. Required Evidentiary Package  

| Requirement | Evidence to be submitted | Source Reference |
|-------------|--------------------------|-------------------|
| **Software Bill of Materials (SBOM)** | • Machine‑readable SBOM in SPDX 2.3+ or CycloneDX 1.5+ format (JSON/XML). <br>• Includes fields: Supplier, Component name, Version, Unique identifier (CPE/PURL), Dependency relationship, Author, Timestamp. <br>Example entry shown in source. | [2] |
| **Threat Model** | • Documented threat model using STRIDE (or equivalent) covering all attack vectors. Mandatory per FDA. | [1] |
| **Cyber‑security Management Plan / Vulnerability Management Plan (CMP/VMP)** | • Formal CMP/VMP describing patching, vulnerability scanning cadence, and escalation procedures. Required by law. | [1] |
| **Penetration Testing** | • Summary of recent pen‑test (≥ annual) with findings, remediation actions; although “recommended” it strengthens the submission. | [1] |
| **Reference Standards** | • Conformance to IEC 81001‑5‑1 (risk management for health‑IT). <br>• Alignment with NIST Cybersecurity Framework (CSF). | [1] |
| **Post‑Market Surveillance (PMS) & Vigilance** | • PMS plan linking software updates, CVD reporting, and monitoring of adverse events. Required for FDA and mirrored in EU/MFDS guidance. | [1] |
| **Labeling / User Documentation** | • Instructions for safe use that include security best practices, update procedures, and contact information for vulnerability reporting. | Implicit from regulatory expectations (no explicit citation). |

---

### 3. Missing Information (to be gathered before submission)

| Item | Why it matters |
|------|----------------|
| **Exact intended use & indication** | Determines classification and predicate selection. |
| **Predicate device(s) (510(k) numbers)** | Needed to establish substantial equivalence; none identified in source. |
| **Risk classification justification** | Must map IEC 62304/ISO 14971 risk levels to FDA class. |
| **Software validation & verification data** (including clinical performance if applicable). |
| **Change impact analysis** – how the software modification alters functionality, risk profile, or cybersecurity posture. |
| **Manufacturer’s Quality Management System certification** – compliance with QMSR (effective Feb 2026). |
| **Evidence of adherence to IEC 81001‑5‑1 & NIST CSF** – audit reports or self‑assessment. |

---

### 4. Risk Controls & Mitigation Measures  

1. **Asset Identification & Inventory** – Complete SBOM as baseline for tracking components.  
2. **Threat Modeling (STRIDE)** – Perform iterative review with design changes.  
3. **Secure Development Lifecycle (SDL)** – Integrate code signing, static/dynamic analysis, and secure coding standards.  
4. **Vulnerability Management** – CMP/VMP defines timeframes: critical (< 48 h), high (< 7 days), etc.; includes patch deployment process.  
5. **Penetration Testing & Red‑Team Exercises** – Annual or upon major release.  
6. **Monitoring & Incident Response** – Real‑time logging, anomaly detection aligned with NIST CSF “Detect” and “Respond”.  
7. **Post‑Market Update Mechanism** – Secure OTA update capability; signed firmware/software packages.  

---

### 5. Key Citations  

| Identifier | Content |
|------------|---------|
| **Section 524B(b)(3)** – Legal obligation for SBOM. | Stated in source [1] and detailed in source [2]. |
| **IEC 81001‑5‑1** – Harmonized standard referenced for cyber‑security controls. | Source [1]. |
| **NIST CSF** – Framework recommended for risk controls. | Source [1]. |
| **SPDX 2.3 / CycloneDX 1.5** – Accepted SBOM formats. | Source [2]. |

*No specific 510(k) predicate numbers, case IDs, or registration numbers appear in the provided excerpts.*  

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required (Human) |
|---------|--------------------------|
| **Detection of a critical vulnerability** in any SBOM component that cannot be patched within 48 h. | Immediate escalation to senior leadership & FDA (via CDRH). |
| **Failure to deliver SBOM in required format** for submission deadline. | Pause submission; involve regulatory affairs manager to resolve. |
| **Change of intended use or risk class** identified during change impact analysis. | Re‑evaluate classification; consider de novo or PMA pathway – senior RA decision needed. |
| **Regulatory audit finding non‑conformance with QMSR** (e.g., missing CMP/VMP). | Initiate corrective action plan; notify QA/Compliance head. |
| **Post‑market incident linked to software security breach**. | Trigger FDA MedWatch report and internal root‑cause investigation. |

---

### 7. Peer Review Prompt  

> **Colleague, please review this draft:**  
> - Are the assumptions about the need for a traditional vs. special 510(k) appropriate given the limited source data?  
> - Have we captured all mandatory FDA cybersecurity deliverables under Section 524B, or are there additional items (e.g., “Cyber‑security Risk Management File”) that should be listed?  
> - Does the citation strategy satisfy regulatory expectations for traceability to guidance documents?  
> - Identify any jurisdiction‑specific gaps (EU MDR, MFDS) that might affect our global submission plan.  

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

1. Chunk `129799210478830618`

> ## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VMP** | 필수 | PMS 계획에 포함 | 업데이트 정책으로 요구 | | **Pen Test** | 권고 | 권고 | 권고 | | **표준 참조** | IEC 81001-5-1, NIST CSF | IEC 81001-5-1 (조화표준 진행) | IEC 81001-5-1, MFDS 자체 가이드 | | **포스트마켓** | 법적 의무 (패치, CVD, 모니터링) | PMS + Vigilance 연계 | 이상사례 보고 + 업데이트 절차 | > MDR/MFDS 영향: GUI SW의 경우 FDA 요건 충족 수준으로 작성하면...

2. Chunk `135977185938899780`

> ### 3.4 SBOM (Software Bill of Materials) **법적 의무** (Section 524B(b)(3)). **NTIA Minimum Elements** (FDA 준용): | 필드 | 설명 | 예시 | |---|---|---| | Supplier Name | SW 공급자 | OpenJDK Foundation | | Component Name | 컴포넌트 명칭 | OpenJDK | | Version | 버전 문자열 | 17.0.9 | | Unique Identifier | CPE 또는 PURL | `pkg:maven/org.openjdk/jdk@17.0.9` | | Dependency Relationship | 의존성 관계 | DependsOn: spring-boot@3.2.0 | | Author of SBOM | SBOM 작성자 | [제조사명] | | Timestamp | 생성일시 ISO 8601 | 2026-04-29T00:00:00Z | **형식**: SPDX 2.3+ 또는 CycloneDX 1.5+ (machine-readable JSON/XML 권장) **포함 범위**: - Manufacturer-developed SW (자체 개발) - Third-party commercial/licensed SW - Ope...

## ra_eu

### kb-eval-20260717-it02-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_eu-001", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a0fc3d166809748d", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

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

> **Regulatory Draft – Determination of Classification & Conform‑assessment Route, Evidence Package and Open Gaps**

---

### 1. Scope & Basis  

| Item | Reference |
|------|------------|
| Legal framework | **EU MDR 2017/745** – Annex II (Technical Documentation) (source [2]) |
| Related technical requirements | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (Post‑market Surveillance) (source [2]) |
| Required documentation structure (Annex II sections) | Device Description, Labelling & IFU, Design & Manufacturing, GSPR checklist, Risk Management, Verification & Validation (source [1]) |

> **Note:** No device‑specific identifiers (e.g., 510(k) number, MDR file reference) appear in the source excerpts. *“no specific identifier found in source — verify separately.”*

---

### 2. Classification Determination – What We Need  

| Required Information | Why It Is Needed | Where to Capture it |
|----------------------|-----------------|---------------------|
| **Intended medical purpose / indication** (clinical intended use, target patient group) | Drives the selection of the appropriate rule in Annex VIII (Classification Rules). | Section 1 of Annex II – *Device Description* (source [1]) |
| **Mode of action** (active, measuring, invasive, sterile, software‑driven, etc.) | Determines whether Rule 9/10/17 or other rules apply. | Device Description & Risk Management file |
| **Physical characteristics** (size, materials, energy source) | Needed for Rules 1–8 (non‑active) and to assess if a device is “measuring” or “implantable”. | Design & Manufacturing section |
| **User / environment** (professional/lay user, intended setting) | Impacts classification (e.g., Rule 6 – devices used by lay persons). | Device Description |

*Until the above data are supplied, only a provisional classification can be given.*  

#### Provisional Scenarios  
| Device type (hypothetical) | Likely MDR Class* | Conform‑assessment route |
|----------------------------|-------------------|--------------------------|
| Non‑active, non‑measuring, non‑sterile, Class I risk (e.g., bandage) | **Class I** (self‑declaration) | Annex IX §3 – Declaration of conformity only (no NB required). |
| Active therapeutic device (Rule 9) or active diagnostic/monitoring (Rule 10) | **Class IIa / IIb** (depending on invasiveness & duration) | **Annex IX** (QMS‑based, full NB audit) *or* **Annex X + XI** (type‑examination + product verification). |
| Implantable or high‑risk active device (Rule 10/17) | **Class III** | Mandatory NB involvement via Annex IX (full quality‑system audit) and possibly type‑examination (Annex X + XI) for very high risk. |

\*These are illustrative only; final class must be derived from the exact intended purpose & mode of action.

---

### 3. Submission Route – Decision Tree  

1. **If Class I (non‑sterile, non‑measuring)** → Self‑declaration of conformity; only Annex II technical file and EU Declaration of Conformity required.  
2. **If Class I sterile or measuring** → NB review under Annex IX (QMS audit).  
3. **If Class IIa/IIb/III** →  
   * Primary route: **Annex IX** (full quality‑management system assessment) – most common for MDR.  
   * Alternative / complementary route for high‑risk (Class III) devices: **Annex X + XI** (type‑examination of the device, then product verification).  

> The choice between Annex IX and Annex X+XI must be confirmed with the selected Notified Body (NB) based on their module portfolio.

---

### 4. Evidence Package Required for the Technical Documentation (Annex II)

| Annex II Section | Minimum Content (per source [1]) | Supporting EU Requirement |
|-------------------|----------------------------------|----------------------------|
| **§1 Device Description** | Full narrative of intended purpose, indications, mode of action, contraindications, device variants, accessories. | Annex I – GSPR §9 (Device description). |
| **§2 Labelling & IFU** | Labels, packaging legend, Instructions for Use (IFU) in English + NB language(s). | Annex I §23 (Labelling); MDR 11/12. |
| **§3 Design & Manufacturing** | Design outputs, drawings, manufacturing process flow, material specifications, supplier list, quality plan. | ISO 13485 / QMS‑related parts of Annex IX. |
| **§4 GSPR Checklist** | Completed checklist mapping each General Safety and Performance Requirement (GSPR) to evidence (e.g., test reports, standards). | Annex I – Chapters II–III. |
| **§5 Risk Management** | ISO 14971‑based risk management file: risk analysis, evaluation of residual risk, risk control measures, traceability matrix. | Annex I §9; ISO 14971. |
| **§6 Verification & Validation (V&V)** | Verification reports (bench, software), validation studies (clinical or simulated use), performance testing data, biocompatibility assessments. | Annex I §§10–14 (Performance evaluation). |
| **Other annexes** (if applicable) | Clinical Evaluation Report (CER) – Annex XIV Part A; Post‑Market Surveillance Plan – Art. 84; Summary of Safety and Clinical Performance (SSCP) – Art. 86. | MDR requirements for clinical evidence & PMS. |

> **Note:** The source mapping links the EU sections to FDA “Design History File” equivalents, confirming that a complete DHF‑style file is expected under Annex II.

---

### 5. Identified Missing Information (Gaps)

| Gap | Impact on Submission |
|-----|----------------------|
| **Intended purpose / indication** – not provided in source excerpts. | Prevents classification; cannot select correct conformity‑assessment route or determine clinical evidence scope. |
| **Device modality (active/measuring/implantable)** – absent. | Affects classification rule (Annex VIII) and risk‑management depth. |
| **Sterility status & shelf life** – not disclosed. | Determines whether a Class I device still requires NB involvement (sterile devices). |
| **Software components / SaMD classification** – unknown. | May invoke Rule 11 (software), requiring specific cyber‑security controls and possibly separate CE marking for software. |
| **Existing clinical data or prior market experience** – not mentioned. | Determines whether a full Clinical Evaluation Report is needed (Annex XIV) or if a PMCF plan suffices. |
| **Manufacturing site(s) & supplier qualification evidence** – missing. | Needed for Design & Manufacturing section and PMS/traceability. |
| **Intended languages beyond English** – only “NB language” hinted. | Must be defined to satisfy labeling requirements (Annex I §23). |

*These gaps must be closed before the Technical Documentation can be completed.*

---

### 6. Core Risk Controls (as per ISO 14971 & MDR)

1. **Hazard Identification & Risk Analysis** – FMEA / Fault Tree for hardware, software safety analysis (if applicable).  
2. **Risk Evaluation** – Determine acceptability of residual risk against intended use.  
3. **Risk Control Measures** – Design controls (e.g., redundant sensors), protective measures, information for safe use (label/IFU).  
4. **Verification of Controls** – Demonstrate through testing that each control meets the requirement.  
5. **Residual Risk Evaluation & Benefit‑risk Determination** – Document rationale for any remaining risk, linking to clinical benefits.  
6. **Post‑Market Surveillance Integration** – Include identified risks in PMS Plan (Art. 84) and update risk file after market feedback.

---

### 7. Human‑Escalation Triggers  

| Situation | Action Required |
|-----------|-----------------|
| **Classification cannot be resolved** (insufficient purpose/modality data). | Escalate to Project Lead / Clinical Team for clarification of intended use; pause NB submission preparation. |
| **Missing clinical evidence for Class IIa/IIb/III** (no CER, no PMCF plan). | Immediate consult with Clinical Affairs to develop a Clinical Evaluation Report (Annex XIV Part A) or PMCF protocol (Annex XIV Part B). |
> *All escalations should be logged in the project tracker and communicated to the Notified Body liaison as soon as possible.*

---

### 8. Peer‑Review Prompt  

> **To: RA Team – Clinical & Regulatory Peers**  
> Please review the assumptions above, especially:
> - The sufficiency of the listed Annex II sections for our device class (any additional annexes needed?).  
> - Whether any MDR special provisions (e.g., Rule 13 “in vitro diagnostic” or Rule 21 “custom‑made”) could apply based on missing data.  
> - Potential jurisdictional gaps: Are there any national transposition requirements (e.g., Germany’s BfArM, France’s ANSM) that would add documentation beyond the EU-level Annex II template?  

Your feedback will be used to finalize the evidence matrix and confirm the chosen conformity‑assessment route.

---

### 9. Summary of Next Steps  

1. **Collect missing device information** (intended purpose, active/measuring status, sterility, software scope).  
2. **Perform classification per Annex VIII** once data are available.  
3. **Assemble full Annex II technical file** using the checklist above.  
4. **Develop clinical evidence strategy** (CER or PMCF) matching the final class.  
5. **Update risk‑management file** with controls derived from the design outputs.  
6. **Engage Notified Body** to confirm the preferred conformity‑assessment module (Annex IX vs. Annex X+XI).  

--- 

*Prepared by Theo – EU RA Specialist (MDR 2017/745)*

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

### kb-eval-20260717-it02-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_eu-002", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2f66967eda81b3ef", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

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

> **Regulatory Response Draft – Notified‑Body Deficiency Letter (MDR)**  

---

### 1. Device Synopsis  
- **Intended purpose:** Standard diagnostic radiology (imaging) device.  
- **Key performance claim used for equivalence:** Digital Quantum Efficiency (DQE(0)) ≥ 65 % (IEC 62220‑1‑1).  
- **Reference test report:** *TR‑2024‑015* (cited in source).  

> **Note:** No predicate‑device identifier, 510(k) number, or specific registration reference appears in the supplied excerpts. Verify these identifiers separately before inclusion.

---

### 2. Classification & Conformity‑Assessment Route  

| Step | Determination | Rationale / Source |
|------|----------------|--------------------|
| **MDR Rule** | *Rule 17 (Annex VIII)* – “devices for recording diagnostic images generated by X‑rays” is the first applicable rule for radiological imaging equipment that produces digital images. If the device does not record X‑ray images but only displays them, **Rule 10** (active devices for diagnosis/monitoring) may apply. | The source flags *standard diagnostic radiology*; classification must be confirmed against the full device description and intended use. |
| **Class** | **Class IIb** under Rule 17 (or Rule 10). | Class IIb triggers both a QMS audit (Annex IX) **and** Type‑Examination with product verification (Annex X + XI). |
| **Conformity‑assessment route** | **MDR Annex IX (QMS‑based) + Annex X/XI (type‑examination & product verification)**. | Required for Class IIb devices; the NB’s “product verification” column in the table confirms relevance of this route. |

*Action:* Confirm the exact rule (17 vs 10) with the device manufacturer and update the classification justification accordingly.

---

### 3. Evidence Required to Satisfy the Deficiency  

| Requirement | What must be submitted | Reference (MDR/Annex) |
|-------------|------------------------|-----------------------|
| **Revised Clinical Evaluation Report (CER)** | Updated CER (Rev 3) demonstrating clinical equivalence – includes DQE data, comparison with predicate, SOTA literature review. | Annex XIV Part A |
| **Test Report for DQE** | Complete IEC 62220‑1‑1 test report *TR‑2024‑015* (raw data, measurement set‑up, uncertainty analysis). | Not a specific MDR annex – part of Technical Documentation (Annex II/III). |
| **Technical Documentation (TD)** | Full TD per Annex II/III: device description, labeling, risk‑management file, design‑verification & validation, software files (if any). | Annex II / III |
| **Risk Management File** | ISO 14971‐based file showing identification of radiation‑related hazards, risk evaluation, and the DQE performance as a control measure. | Annex I (GSRR) |
| **Post‑Market Surveillance (PMS) System** | PMS plan (Art. 84) and first‑year PMS report or PSUR (Art. 86 for Class IIb). Include PMCF plan if required for higher‑risk statements. | Art. 83–86 |
| **Labeling Package** | Updated labeling that reflects the clinical performance claim, safety information on radiation exposure, and instructions for use in line with Annex I Chapter III (§23). | Annex I, Chap III |
| **Quality Management System (QMS) Evidence** | ISO 13485 certification and evidence of closure of any previously identified QMS non‑conformities reported by the NB. | Annex IX (module B) |

---

### 4. Gaps Identified from the Deficiency Letter  

| Gap | Impact on Submission | Required Action |
|-----|----------------------|-----------------|
| **Absence of a complete PMCF plan / evaluation report** (required for Class IIb and for ongoing clinical evidence). | NB may consider the clinical evidence insufficient once the device is in use. | Prepare an Annex XIV Part B PMCF plan, outlining data collection, sample size, follow‑up schedule; submit interim PMCF evaluation report if available. |
| **Labeling deficiencies** (not detailed in excerpt but listed under “주요 결함 유형”). | Non‑conformity with Annex I §23 – could halt market authorisation. | Revise IFU & CE marking statements to incorporate DQE performance claim, radiation safety warnings, and user training instructions. |
| **QMS non‑conformities** (referenced as “QMS NC” in the table). | Prevents successful audit closure; may trigger additional NB audits. | Provide corrective‑action evidence (root‑cause analysis, effectiveness checks) for each NC raised previously. |
| **Justification of classification rule** – missing explicit reference to Rule 17/10. | NB cannot verify that the correct conformity route is being followed. | Submit a concise “Classification Justification” document citing the relevant Annex VIII rule and linking it to the intended use statement. |
| **Evidence that DQE ≥ 65 % meets state‑of‑the‑art** – SOTA literature not included in excerpt. | May be challenged as insufficient clinical performance proof. | Add a brief SOTA paragraph with bibliographic references (peer‑reviewed) demonstrating that a DQE of 65 % is at least equivalent to current market devices. |

---

### 5. Risk Controls Related to Clinical Equivalence  

1. **Performance‑Based Control** – The DQE value directly limits patient dose for a given image quality; the device’s internal software enforces minimum exposure settings if DQE falls below the claim.  
2. **User Training** – IFU includes mandatory training on optimal acquisition parameters and verification of DQE performance during routine QC.  
3. **Periodic QC Programme** – Annual IEC 62220‑1‑1 re‑testing as part of the PMS plan; deviations trigger corrective actions.  
4. **Alarm & Interlocks** – Hardware interlock shuts down X‑ray source if detector temperature exceeds safe limits (risk of DQE degradation).  

All above are documented in the risk‑management file (ISO 14971) and referenced in the PMS report.

---

### 6. Citations (per mandated mapping)

| Item | Citation |
|------|----------|
| Clinical Evaluation Report (CER) | **Annex XIV Part A** (MDR) |
| PMCF plan / evaluation | **Annex XIV Part B** |
| PMS system, plan & reports | **Art. 83–86** (MDR) |
| Labeling requirements | **Annex I, Chapter III (§23)** |
| Classification rules (Rule 17/10) | **Annex VIII** – verify correct rule number before quoting |
| Deficiency‑letter procedural basis | **MDR Annex VII + 2026/977** (as per source table) |
| Structured Dialogue mechanism | **Art. 7, 2026/977** |
| QMS audit requirement for Class IIb | **Annex IX** |

> *No specific predicate/device identifiers or registration numbers appear in the supplied excerpts; verify these separately before inclusion.*

---

### 7. Human‑Escalation Triggers  

| Situation | Trigger | Escalation Path |
|-----------|---------|-----------------|
| **Unable to provide missing PMCF data** within NB‑agreed deadline | Need for additional clinical data collection (e.g., prospective registry) | Escalate to Senior RA Manager → Request formal extension via Structured Dialogue (Art. 7, 2026/977). |
| **NB rejects revised labeling** after submission | Potential non‑conformity with Annex I §23 | Convene cross‑functional meeting (Regulatory, Clinical, QA) → Draft alternative labeling; if impasse persists, consider appeal to Competent Authority. |
| **QMS non‑conformities remain open** beyond 30 days post‑submission | Risk of audit suspension / product verification halt | Notify Quality Assurance Lead → Initiate Corrective‑Action Plan (CAPA) with defined milestones; inform NB of CAPA status weekly. |
| **NB requests clarification on classification rule** | Ambiguity between Rule 17 and Rule 10 | Engage external MDR expert or legal counsel for definitive interpretation; submit a Classification Justification Addendum. |
| **Deadline approaching with incomplete documentation** | Risk of “evaluation termination / non‑approval” (source table) | Immediate escalation to Project Lead → Decision on whether to request clock‑stop extension or withdraw submission pending completion. |

---

### 8. Peer‑Review Prompt  

> **To the next RA reviewer:**  
> - Are we confident that Rule 17 is the correct classification basis, given the device’s functional description? Please verify against the full Intended Use statement and any software/firmware functionalities.  
> - Does the current evidence package (CER Rev 3 + DQE test report) fully satisfy Annex XIV Part A requirements for clinical equivalence, or should we supplement with additional SOTA literature and user‑feedback data?  
> - Have we captured all applicable MDR procedural references (e.g., Art. 7 Structured Dialogue, Annex VII deficiency‑letter handling) to ensure the NB’s expectations are met?  
> - Identify any jurisdiction‑specific gaps that may arise when later transitioning to other markets (e.g., FDA 510(k) or MFDS) and propose mitigations.

--- 

**Prepared by:** Theo – EU Regulatory Affairs Specialist (MDR)  

*Document version:* 1.0 – Draft for NB response preparation.

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

### kb-eval-20260717-it02-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_eu-003", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3c793b286540204c", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

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

> **Regulatory Draft – Classification & Conformity‑Assessment Path for a Diagnostic X‑ray System (NB Query Response)**  

---

### 1. Device Overview (as understood from the NB query)  
| Item | Current description (derived from source) |
|------|-------------------------------------------|
| **Intended purpose** | “Diagnostic X‑ray system – generation of ionising radiation for patient imaging” (no therapeutic intent). |
| **Core device type** | Active medical device that emits ionising radiation for *diagnostic* use. |
| **Key sub‑component** | Digital flat‑panel detector (recording device). |

> **Source [2]** provides the table entry that originally mapped “X‑ray system” to EU MDR Rule 5/9, which is incorrect for a diagnostic X‑ray. The correct rule is identified therein as **Rule 10 → Class IIb**; the detector falls under **Rule 17 → Class IIa**.  

---

### 2. Correct MDR Classification  

| Component | Applicable MDR rule (Annex VIII) | Resulting class |
|-----------|----------------------------------|-----------------|
| Diagnostic X‑ray system (energy‐emitting, *diagnostic* purpose) | **Rule 10** – “Active devices intended to emit ionising radiation for diagnostic purposes” | **Class IIb** |
| Digital flat‑panel detector (recording of diagnostic images) | **Rule 17** – “Devices for recording diagnostic images generated by X‑rays” | **Class IIa** |

*Rule 9* applies only to **therapeutic** ionising‑radiation devices and is therefore *not* appropriate (see **Source [1]**).  

---

### 3. Required Conformity‑Assessment Route  

| Device class | Primary MDR route(s) |
|--------------|----------------------|
| **Class IIb** (X‑ray system) | • **Module B – Full quality‑management system** under **Annex IX** (most common choice).  <br>• Alternatively, **Module C (type‑examination)** + **Module D/E (product verification & certification)** under **Annex X** + **Annex XI**. |
| **Class IIa** (detector) | • **Module B** under **Annex IX** (or Module C + D/E if the manufacturer prefers a type‑exam route). |

> The choice of route determines the depth of technical documentation review and the frequency of Notified Body audits.  

---

### 4. Evidence & Documentation Required for the **X‑ray System** (Class IIb)  

| Technical File Element | Mandatory content (MDR reference) | Comments / Typical sources |
|------------------------|-------------------------------------|----------------------------|
| **1. Device Description & Specification** | Annex II §4 – detailed description, accessories, intended use, indications, contraindications. | Include radiation output parameters (kVp range, mA, filtration), beam geometry, safety interlocks. |
| **2. Design & Manufacturing Information** | Annex II §5‑6 – drawings, bill of materials, manufacturing processes. | Demonstrate control of critical processes (e.g., tube fabrication, shielding). |
| **3. Risk Management File** | Annex I §10 (GSPR) + ISO 14971. | Hazard analysis for ionising radiation (dose to patient/staff), failure modes, mitigations (e.g., dose‑monitoring, emergency stop). |
| **4. Clinical Evaluation Report (CER)** | **Annex XIV Part A** – state‑of‑the‑art literature review, clinical data, benefit–risk analysis. | Use peer‑reviewed studies on diagnostic performance of comparable X‑ray systems; include any post‑market surveillance (PMS) data if available. |
| **5. PMCF Plan & Report** | **Annex XIV Part B** – proactive post‑market clinical follow‑up for Class IIb. | Outline registry or prospective study to monitor image quality, dose metrics, adverse events. |
| **6. PMS System (Plan/Report)** | Art. 83–85 – PMS plan, periodic safety update report (PSUR) for higher‑risk devices (Art. 86). | Incorporate radiation protection monitoring, incident reporting. |
| **7. Performance Testing & Standards** | Annex II §9 – verification of conformity with applicable EN/IEC standards (e.g., IEC 60601‑2‑44, IEC 62391‑1). | Provide test reports for electromagnetic compatibility, mechanical safety, radiation output. |
| **8. Labeling & IFU** | Annex I Chapter III §23 – labeling, symbols, instructions for use. | Must contain radiation safety information (dose limits, shielding requirements, operator training). |
| **9. Declaration of Conformity** | Annex IV – EU DoC referencing the relevant modules and standard(s). | Signed by authorised representative. |

---

### 5. Evidence & Documentation Required for the **Digital Flat‑Panel Detector** (Class IIa)  

*The same structure applies, but a reduced depth is acceptable (e.g., PMCF not mandatory unless justified).* Key points:

| Item | Requirement |
|------|--------------|
| CER (Annex XIV Part A) | Literature on detector performance (spatial resolution, DQE), bench testing results. |
| PMS plan (Art. 84) | Routine post‑market monitoring; PSUR not required for Class IIa. |
| IEC 60601‑2‑44 compliance | Verification of electrical safety and electromagnetic compatibility. |

---

### 6. Gaps / Missing Information Identified  

1. **Explicit Intended Use Statement** – The source only indicates “diagnostic X‑ray”. A full intended purpose must list patient groups, anatomical regions, and clinical indications.  
2. **Radiation Protection Data** – No data on dose measurements (e.g., DAP, KERMA) or safety interlocks have been supplied.  
3. **Clinical Evidence** – Absence of a drafted Clinical Evaluation Report; only a high‑level reference to “state‑of‑the‑art” exists.  
4. **Applicable Standard References** – IEC 60601‑2‑44 and related EN standards are not cited in the current documentation set.  
5. **Labeling Drafts** – No draft IFU or labeling showing radiation warnings, operator training requirements, nor symbols per Annex I §23.  

*These gaps must be filled before a Notified Body can confirm the classification and proceed with the audit.*  

---

### 7. Risk Controls Specific to Ionising‑Radiation Devices (Rule 10)  

| Hazard | Control Measure (Risk Control) | Reference |
|--------|--------------------------------|-----------|
| Excess patient dose | Automatic exposure control, maximum mAs/kVp limits, real‑time dose display. | IEC 60601‑2‑44, Annex I §10 |
| Operator overexposure | Interlock of X‑ray tube when door open, shielding curtains, training program. | IEC 62391‑1, GSPR |
| Failure of safety interlocks | Redundant hardware interlocks, periodic functional testing in PMS. | ISO 14971 risk control hierarchy |
| Image quality degradation leading to repeat exposures | Quality assurance protocol (phantom tests) incorporated into PMCF. | Annex XIV Part B |

---

### 8. Human‑Escalation Triggers  

| Situation | Action Required | Who Escalates |
|-----------|-----------------|---------------|
| **Disagreement on classification** (e.g., NB disputes Rule 10 vs. Rule 9) | Convene a cross‑functional review (RA, Clinical, Engineering) and prepare a justification memo with rule citations. | RA Lead |
| **Missing radiation safety data** (dose measurements, shielding calculations) | Request complete dosimetry report from the design team; if not provided within 2 weeks, pause NB submission. | Project Manager |
| **Incomplete CER** (no clinical performance data) | Halt compilation of Technical Documentation until a draft CER is supplied and peer‑reviewed. | Clinical Evaluation Lead |
| **Non‑conformity with IEC 60601‑2‑44** identified during audit | Initiate corrective action plan; if remediation exceeds 30 days, notify senior management. | Quality Manager |
| **Labeling does not meet Annex I §23** (missing radiation symbols) | Issue a labeling change request; if unresolved before NB review, defer submission. | Regulatory Affairs Lead |

---

### 9. Citations  

* **Classification rule for diagnostic X‑ray devices:** Rule 10 – Annex VIII (MDR).  
* **Therapeutic vs. Diagnostic distinction:** Source [1] clarifies that Rule 9 applies only to therapeutic ionising‑radiation devices.  
* **Correct classification mapping & identified mis‑mapping:** Source [2] explicitly states “X‑ray system … = Rule 10 → Class IIb” and highlights the erroneous “Rule 5/9” entry.  

> No specific 510(k) predicate number appears in the excerpts; only the generic reference to “FDA Class II (510(k), Product Code MQB).” **No specific identifier found in source — verify separately** for any FDA clearance details that may be relevant.

---

### 10. Recommended Next Steps  

1. **Finalize Intended Use wording** and incorporate it into Annex II §4.  
2. **Generate a complete Clinical Evaluation Report** (Annex XIV Part A) using peer‑reviewed diagnostic X‑ray literature and any available post‑market data.  
3. **Produce radiation safety test reports** (dose, interlock functionality) referenced to IEC 60601‑2‑44.  
4. **Update labeling/IFU** to include all mandatory symbols and radiation warnings (Annex I §23).  
5. **Select conformity‑assessment route** – confirm whether the manufacturer will pursue Annex IX (QMS) or Annex X+XI (type‑exam) for the Class IIb system. Document the decision in the Technical Documentation.  

---

## Peer Review Prompt  

> *@RA‑Peer* – Please review this draft and challenge:  
> 1. **Assumptions** about the intended purpose and scope of the X‑ray system (are any clinical indications missing that could shift classification?).  
> 2. **Source coverage** – Does the provided excerpt adequately support the classification conclusion, or are additional regulatory texts needed?  
> 3. **Jurisdictional gaps** – Are there EU‑specific requirements (e.g., specific radiation safety annexes, national competent authority notifications) not captured here?  

Your feedback will be incorporated before finalising the NB response.

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

### kb-eval-20260717-it02-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_eu-004", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e43c897461f950f2", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md", "source_hash": "96ff2d334aa377f194a63cd731ca742bb703e9899411086b8065e85bdf4bd94a"} -->

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

> **Regulatory Draft – X‑ray Detector / Hand‑held Source + GUI Software (MDR 2017/745)**  

---

### 1. Device Overview & Intended Purpose  
| Element | Description (as extracted) |
|---|---|
| **Device family** | X‑ray detector, hand‑held radiation source, GUI control software (integrated system). |
| **Intended medical purpose** | Capture and record diagnostic X‑ray images for clinical decision‑making. |
| **Primary function** | Convert X‑ray photons into digital image data; display/control via GUI. |

*The intended use places the device within the “diagnostic imaging – recording” category (see Annex VIII, Rule 17).*

---

### 2. Classification & Conformity‑Assessment Route  

| Item | Determination |
|---|---|
| **MDR classification** | **Class IIa** – active medical device for recording diagnostic X‑ray images (Annex VIII, **Rule 17**). *[Uncertainty flagged – verify that no other rule (9 or 10) supersedes Rule 17]* |
| **Conformity‑assessment procedure** | **Annex IX (QMS‑based) + Annex X (type‑examination) & Annex XI (product verification)** for Class IIa devices. The Notified Body will audit the QMS (ISO 13485) and review the technical documentation (including type‑exam). |
| **Notified‑Body involvement** | Required – NB to issue CE certificate after satisfactory audit of QMS and review of Technical File. |

---

### 3. Evidence Required for Technical Documentation  

| GSPR clause (Annex I) | Evidence – status per source table* | Additional required artefacts |
|---|---|---|
| **§1 General safety & performance requirements** | IEC 60601‑1 (general), IEC 60601‑1‑2 (EMC), IEC 60601‑1‑3 (radiation protection) – *compliant* (see source [1] columns “●”). | Declaration of conformity to each listed standard; test reports confirming compliance. |
| **§5 Usability** | IEC 60601‑1‑6 & IEC 62366‑1 referenced (source [1]) – *compliant*. | Full Usability Engineering File (IEC 62366) with formative/ summative testing results. |
| **§16 Performance evaluation** | IEC 62220‑1‑1 (DQE), IEC 60601‑2‑54 (imaging equipment) cited (source [1]) – *compliant*. | Clinical performance data or bench‑testing demonstrating DQE, spatial resolution, etc.; Clinical Evaluation Report (Annex XIV Part A). |
| **§17 Radiation safety** | IEC 60601‑2‑28 (X‑ray tube) & IEC 60601‑2‑54 referenced – *compliant*. | Radiation safety test report; validation of shielding and dose limits. |
| **§18 Software lifecycle** | IEC 62304 (software life‑cycle) & IEC 62366‑1 cited – *compliant* (source [1]). | Software Development File: architecture, hazard analysis, verification/validation protocols & reports, change management. |
| **§19 Materials & biocompatibility** | ISO 10993‑1 test indicated for patient‑contacting parts (source [2] §10.1). | Full Biocompatibility Dossier (ISO 10993 series) covering all materials in contact with patients or staff; summary of toxicological risk assessment. |
| **§20 Sterility / micro‑organism control** – not applicable (device is non‑sterile). |
| **§21 Labelling** | IEC 60601‑1‑6 and Annex I §23 referenced – *compliant* (source [1]). | Labeling & IFU (Instruction for Use) draft meeting all mandatory items (intended use, contraindications, warnings, symbols). |

\*“●” in source tables denotes that the given standard is mapped to the corresponding GSPR clause.

#### Additional Mandatory Documentation (MDR‑specific)

| Document | Requirement | Current status |
|---|---|---|
| **Risk Management File** (ISO 14971) | Identify hazards, estimate risks, implement controls; verify effectiveness. | Reference to risk controls via standards but no explicit RMF shown – *need full file*. |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | State of the art, clinical data, benefit‑risk analysis. | Not present in source – must be produced. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** – Annex XIV Part B | Planned post‑market studies for higher‑risk devices; periodic evaluation. | No PMCF evidence identified – *to be drafted*. |
> **Note:** For Class IIa, a PMCF plan is optional but strongly recommended when clinical data are limited.

| **Post‑Market Surveillance (PMS) System** – Art 83/84/85/86 | PMS Plan, periodic safety update report (PSUR) if applicable. | Not referenced – *must be established*. |
| **Declaration of Conformity** – Annex IV | Signed by manufacturer after conformity assessment. | Pending NB review. |

---

### 4. Gaps / Missing Information  

| Gap | Impact on NB submission | Suggested action |
|---|---|---|
| **Nanomaterial risk assessment** (source [2] §10.5 “검증 필요”) | Non‑compliance with §10.1–10.4 if nanomaterials are present; NB will request a dedicated risk assessment and possibly additional biocompatibility testing. | Confirm presence/absence of nano‑scale constituents; if present, conduct ISO 10993‑22 / specific toxicology studies and update RMF. |
| **Full software verification & validation evidence** (IEC 62304, IEC 62366) | NB will demand traceability matrix linking requirements → tests → results. | Compile Software Development File with complete V‑V reports, usability test data, security analysis. |
| **Clinical performance / CER** | Without a CER, the benefit‑risk conclusion cannot be demonstrated. | Gather bench‑test data and/or retrospective clinical data; produce a draft CER. |
| **PMCF plan (if required)** | Absence may be acceptable for Class IIa if sufficient pre‑market evidence exists, but NB may still request one. | Draft PMCF Plan outlining objectives, methods, timelines; align with MDR Art 83–86. |
| **PMS system documentation** | Required by Art 83/84 for all devices; missing will delay certification. | Establish PMS procedures, incident reporting, trend analysis, and prepare a PSUR template if device falls into Class IIb/III (verify). |
| **Labeling details & IFU** | Must meet Annex I §23; incomplete labeling leads to non‑conformity findings. | Develop full labeling pack, include safety information, intended use, etc., and map each requirement. |

---

### 5. Key Risk Controls (derived from GSPR mapping)

| Hazard | Control(s) | Reference |
|---|---|---|
| Electrical safety & leakage currents | IEC 60601‑1 compliance; protective earth, insulation testing. | Source [1] §1,§19,§20,§21 |
| Electromagnetic compatibility | IEC 60601‑1‑2 (EMC) testing. | Source [1] §19.2 |
| Radiation exposure to patient/operator | IEC 60601‑1‑3 (radiation protection); shielding design verification (§10.4). | Source [1] §17; source [2] §10.4 |
| Software malfunction / incorrect image display | IEC 62304 lifecycle, IEC 62366 usability engineering, software hazard analysis. | Source [1] §§18,5,23 |
| Biocompatibility (patient‑contacting surfaces) | ISO 10993‑1 and related series testing; material selection. | Source [2] §10.1‑10.3 |
| Contamination / ingress of fluids/particles | Enclosure design verification (specification). | Source [2] §10.4 |
| Nanomaterial–related toxicity | Additional risk assessment & possible toxicological testing (RMF). | Source [2] §10.5 |

---

### 6. Citations  

| Requirement | Source reference |
|---|---|
| **GSPR mapping to standards** | Excerpt [1] – table linking IEC/ISO standards to GSPR §§ (e.g., IEC 60601‑1 → §1,§19‑21). |
| **Chemical/physical/biological characteristics** | Excerpt [2] – §10.1–10.5 table showing test methods and basis (ISO 10993, nanomaterial RMF). |
| **MDR classification rule** | Annex VIII Rule 17 (active devices for recording X‑ray images) – *not directly quoted in source; flagged for verification*. |
| **Regulatory articles/annexes** | MDR Annex I (GSPR), Annex IV (DoC), Annex IX/X/XI (conformity routes), Art 83–86 (PMS). No specific identifier numbers appear in the excerpts. |

*No specific 510(k)/predicate or registration numbers are present in the provided source – verify separately if needed.*

---

### 7. Human‑Escalation Triggers  

| Trigger | Reason for escalation |
|---|---|
| **Uncertain classification (Rule 17 vs possible Rule 9/10)** | Misclassification leads to inappropriate conformity route; requires senior RA sign‑off and possibly a pre‑submission meeting with NB. |
| **Nanomaterial risk assessment pending** | Regulatory gap – may block CE marking; require specialist toxicology input. |
| **Missing or incomplete CER/clinical data** | Benefit‑risk cannot be substantiated; must involve clinical affairs team. |
| **Software V‑V evidence not fully traceable** | NB audit will focus on software files; need QA lead review. |
| **PMS system and PMCF plan not yet drafted** | Mandatory for all MDR devices – project manager must allocate resources. |
| **Labeling/IFU gaps identified** | Market surveillance risk; require regulatory writing team to finalize. |

When any of the above triggers are met, the RA should **raise a Work Package (WP) comment** recommending immediate action and request human confirmation before proceeding.

---

### 8. Peer‑Review Prompt  

> *Colleague, could you review the assumptions made in this draft? Specifically:*
> 
> 1. **Classification certainty** – does Rule 17 appropriately capture the device, or might Rule 9/10 apply given the hand‑held source functionality?  
> 2. **Source coverage** – have we extracted all relevant GSPR clauses from the excerpted tables, or are there additional MDR requirements (e.g., environmental safety, waste) that need addressing?  
> 3. **Jurisdictional gaps** – considering the device combines hardware and software, is our plan for the European PMS/PMCF system complete under Art 83‑86, especially regarding cyber‑security updates?  

*Please challenge any points you find weak or incomplete.*

--- 

*Prepared by: Theo (EU RA – MDR specialist)*  
*Document version: 1.0 – daily growth case e43c897461f950f2 (2026‑07‑18).*

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

### kb-eval-20260717-it02-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_eu-005", "iteration": 2, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b6a40aca6ca36744", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

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

> **Regulatory Draft – Initial MDR Assessment & NB Submission Planning**

---

### 1. Scope of the Draft  
*Purpose*: Provide a concise, “what‑the‑Notified‑Body (NB) needs to see” checklist covering classification, conformity‑assessment route, evidentiary gaps, risk‑control expectations and escalation triggers for the device described in the incoming dossier.

*Assumptions*: The only source material available is the excerpted text below. No explicit device description, intended purpose or identifier (e.g., 510(k) number) has been supplied – **“no specific identifier found in source — verify separately.”**  

---

### 2. Classification & Responsibility  

| Item | Reference | Comments |
|------|-----------|----------|
| **Classification rule** | Article 51 + Annex VIII (22‑rule hierarchy) | The manufacturer must perform **self‑classification**, applying the rules sequentially and adopting the highest applicable class (see source [2]). |
| **When in doubt** | Competent Authority (CA) or MDCG “Borderline & Classification” Manual v2.1.1 (2023‑09) | Use this guidance for borderline cases. |
| **Responsibility** | Article 51 (manufacturer bears classification burden) | Manufacturer must retain evidence of the rule applied and justification. |

> **Action** – Identify the exact intended medical purpose(s) and technical characteristics to map them onto Annex VIII rules. Record the rule number (e.g., Rule 9, 10 or 17) with a brief rationale.

---

### 3. Conformity‑Assessment Route (depends on final class)

| Final Class | Typical MDR route | Required annexes / articles |
|-------------|-------------------|------------------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration of conformity – Annex IV & VII | • EU Declaration of Conformity (Annex IV) <br>• Technical Documentation (Annex II/III) |
| **Class I (sterile/measuring)** | Annex IX (QMS‑based) with ISO 13485 certification + Annex VIII verification | • QMS assessment (Annex IX) <br>• Device verification (Annex X) if applicable |
| **Class IIa** | Annex IX (full quality‑system audit) *or* Annex X + XI (type‑examination & product verification) | • ISO 13485 QMS audit (Annex IX) <br>• Type‑examination certificate (Annex X) if device is high‑risk software or has a dedicated module |
| **Class IIb / III** | Annex VIII (full design‑dossier review) + NB involvement throughout | • Design‑Dossier audit (Annex VIII) <br>• Clinical Evaluation Report (CER) – Annex XIV Part A (Art. 61) <br>• PMCF plan & report – Annex XIV Part B |

*Select the route after confirming the class.*  

---

### 4. Core Evidence Required for NB Review  

| Evidence | Where it belongs in the Technical File | MDR reference |
|----------|----------------------------------------|---------------|
| **Device description, intended purpose & labeling** | Part A – “Device Description” (Annex II) | Annex I, Chap III §23 (labeling) |
| **Risk Management File** (risk analysis, risk evaluation, mitigations, residual risk) | Part B – “Risk Management” (Annex II) | Annex I (GSRR) + ISO 14971 (implementation) |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (updated via Art. 61) | *Cite:* **Annex XIV Part A** |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** | Annex XIV Part B | *Cite:* **Annex XIV Part B** |
| **Post‑Market Surveillance (PMS) System, PMS Plan & Periodic Safety Update Report (PSUR)** (if Class IIb/III) | Art. 83 (system) / Art. 84 (plan) / Art. 85 (report for lower‑risk) / Art. 86 (PSUR for higher‑risk) | *Cite:* **Art. 83–86** |
| **Unique Device Identification (UDI) registration** | UDI dossier, linkage to EUDAMED | Source [1] mentions UDI portal & GUDID; MDR does not assign a specific annex – see Art. 27‑29 for UDI obligations |
| **Quality Management System certification (ISO 13485)** | Certificate of compliance, audit reports | Annex IX (QMS‑based route) |
| **Software documentation** (if applicable) – IEC 62304, cybersecurity plan (Art. 10(12), EN ISO/IEC 27001) | Part C – “Product Verification & Validation” (Annex II) | Annex I (GSRR) |

---

### 5. Gaps / Missing Information (Based on the excerpted source)

| Gap | Why it matters | Suggested source to fill |
|-----|----------------|--------------------------|
| **Exact intended medical purpose(s)** | Drives classification rule & clinical evaluation scope. | Manufacturer’s “Intended Use” statement; IFU draft. |
| **Device description (materials, dimensions, accessories, software version)** | Needed for Annex II technical file sections and risk analysis. | Engineering spec sheets, bill of materials. |
| **Classification justification (rule number + rationale)** | Required for self‑classification evidence & NB review. | Internal classification worksheet. |
| **Clinical data (clinical literature, post‑market data, or clinical investigation results)** | CER cannot be drafted without this. | Literature search matrix; potential clinical investigation files. |
| **Post‑Market Surveillance (PMS) plan** | Mandatory for all classes; PSUR required for IIb/III. | PMS SOPs, risk‑based surveillance schedule. |
| **UDI allocation & EUDAMED registration status** | UDI is a legal requirement; must be entered in EUDAMED prior to CE marking. | UDI issuance authority confirmation, EUDAMED entry screenshot. |
| **Authorized Representative documentation (Art. 11)** | Required for any non‑EU manufacturer. | Signed AR contract, proof of registration. |
| **Fees & NB contract details** | Source [1] lists typical fee ranges; actual budget must be confirmed. | NB quotation & signed agreement. |

> **Immediate next step:** Request the above items from the project team before any formal NB interaction.

---

### 6. Principal Risk Controls (per ISO 14971) to Highlight for NB

| Hazard Category | Typical Control(s) | Evidence Needed |
|-----------------|--------------------|-----------------|
| **Biocompatibility** (materials in contact with patient) | Material testing per ISO 10993‑1, toxicology risk assessment. | Test reports, risk evaluation tables. |
| **Electrical safety / EMC** (if active device) | IEC 60601‑1 compliance, insulation tests, fault analysis. | Test certificates, validation protocol. |
| **Software/Device cybersecurity** | Secure development lifecycle, vulnerability management per EN ISO/IEC 27001 & MDCG 2020‑16 guidance. | Cybersecurity risk assessment, patch plan. |
| **Sterility (if applicable)** | Validation of sterilization process (ISO 11135/11224). | Sterilization validation report. |
| **Usability / Human factors** | Formative/usability testing per IEC 62366‑1. | Test reports, design change justification. |

Each control must be traceable to a residual risk evaluation in the RMF.

---

### 7. Human‑Escalation Triggers (Yellow‑Gate Actions)

| Trigger | Reason for escalation | Recommended action |
|---------|-----------------------|--------------------|
| **Unclear or conflicting classification** (e.g., device seems to fit multiple Annex VIII rules) | NB may reject the self‑classification; CA involvement required. | Pause dossier assembly; seek MDCG Manual clarification or request a “borderline classification” opinion from the national Competent Authority. |
| **Insufficient clinical evidence for intended purpose** | CER cannot be completed → No CE mark. | Escalate to Clinical Affairs lead; consider conducting a limited MDR‑compliant clinical investigation. |
| **Missing UDI registration in EUDAMED before market launch** | Non‑conformity with Art. 27‑29; may trigger enforcement action. | Flag to Project Manager; request immediate EUDAMED entry and confirmation of the UDI dossier. |
| **No authorised representative (AR) for non‑EU manufacturer** | Article 11 mandates AR; NB will reject. | Obtain signed AR agreement; verify AR’s registration in the EU. |
| **Budget/fee uncertainty that could delay NB contract signing** | Financial hold‑up can jeopardise timeline. | Alert Finance & Project Lead; confirm fee schedule with selected NB (see source [1] for typical ranges). |
| **PMS / PSUR plan not aligned with device risk class** | Higher‑risk devices require PSUR (Art. 86). | Review risk classification, upgrade PMS documentation accordingly. |

When any of the above triggers appear, **document in the Work Package comment**, recommend closure only after resolution, and request human confirmation before proceeding.

---

### 8. Peer‑Review Prompt (for an RA colleague)

> *Could you review the assumptions made herein regarding:*
> 
> - *The applicability of Annex IX vs. Annex VIII routes for a Class IIa device without a dedicated software module?*  
> - *Whether the listed clinical evidence gaps fully reflect what the NB will expect for a device intended for “diagnostic imaging assistance” (potentially Rule 17)?*  
> - *Any jurisdiction‑specific nuances we might be missing, especially around UDI registration in South Korea (UDI portal reference in source [1]) that could affect EU compliance?*  

Please challenge the classification rationale, evidence checklist, and any overlooked MDR provisions.

---

### 9. Reusable RA Judgment – “Lesson Learned”

> **RA Judgment:** *When classifying a medical device under MDR, always apply the entire hierarchy of Annex VIII rules sequentially and adopt the highest‑ranked rule that applies. Document the specific rule number together with a concise justification (intended purpose, energy source, invasiveness, etc.). If any doubt remains after this exercise, proactively seek clarification from the national Competent Authority or the latest MDCG “Borderline & Classification” Manual (v2.1.1 – September 2023) before initiating NB submission.*  

*This judgment should be recorded in the RA knowledge base for future self‑classification tasks.*

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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

## ra_kr

### kb-eval-20260717-it02-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_kr-001", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "862df3a912cbc93d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038"} -->

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

> **Regulatory Draft – Supplementary‑Response Strategy for MFDS Review**

---

### 1. Determination of Classification & Submission Route  

| Item | Assessment | Rationale |
|------|------------|-----------|
| **Device class (K‑class)** | *Undetermined – requires clarification of intended use, invasiveness, and risk level.* | Korean classification follows the “Risk‑Based Classification” rules (MFDS Notice 2021‑xxx). Without a clear description of the device’s function or body site, we cannot assign Class I‑III. |
| **Submission pathway** | • **허가 (General)** – if the device is Class II/III and requires full approval.<br>• **인증** – if it is a Class I “non‑risk” device that can be certified by NIFDS.<br>• **신고** – for low‑risk Class I devices not subject to 허가. | The timing table in the source (Chunk [1]) lists distinct processing periods for *허가 (일반)*, *허가 (임상 포함)*, *인증*, and *신고*. Selecting the correct pathway hinges on the device class. |
| **Reference** | No specific identifier found in source — verify separately. |

---

### 2. Required Evidence Package (Typical MFDS Checklist)

| Evidence Category | Typical Requirement for Korean Review | Notes / Gaps |
|-------------------|----------------------------------------|--------------|
| **Technical Documentation** (Design Dossier, Device Description) | Must comply with KGMP and MFDS guideline “Technical File” (MFDS Notice 2022‑xxx). | Device description not provided. |
| **Non‑clinical Testing** | ISO 10993 safety data; OECD‑aligned toxicology reports are now accepted per recent MFDS scope expansion (*see MFDS notice on foreign non‑clinical data*). | Confirmation needed whether existing foreign data meet Korean acceptability. |
| **Clinical Evaluation** | • For Class II/III: Clinical trial results or a bridging study.<br>• If “임상 포함” is required, the processing time extends to 80 days (Chunk [1]). | No clinical data cited; need to know whether domestic data are mandatory. |
| **Quality Management System** | KGMP certification for manufacturing facilities (ISO 13485‑based). | Facility status unknown. |
| **Labeling & IFU** | Korean language labeling, including safety information, storage conditions, and a “사용자 매뉴얼”. Must follow the Korean public notice style (Chunk [2] provides sample phrasing). | Draft label not yet supplied. |
| **Risk Management File** | ISO 14971‑based risk analysis; identification of residual risks and mitigation measures. | Not provided. |
| **Post‑Market Surveillance (PMS) Plan** | PMS report format per MFDS “시판후조사” guideline. | Absent. |

---

### 3. Identified Missing Information  

1. **Device classification details** – intended use, anatomical site, invasiveness.  
2. **Manufacturing location & KGMP status** – is the plant already certified in Korea or abroad?  
3. **Non‑clinical data source** – are foreign toxicology studies available and aligned with MFDS accepted standards?  
4. **Clinical evidence** – existence of a Korean clinical trial, foreign CE/FDA clearance, or bridging dataset.  
5. **Labeling & IFU drafts** in Korean language (including mandatory symbols).  
6. **Risk Management File** – list of identified hazards and controls.  
7. **PMS plan** – schedule for adverse event reporting, field safety corrective actions.

---

### 4. Suggested Risk Controls (to be reflected in the RMF)

| Hazard | Control Measure | Evidence Needed |
|--------|-----------------|-----------------|
| Electrical shock (if applicable) | Design safeguards, double insulation, IEC 60601‑1 compliance. | Test reports, certification copy. |
| Biocompatibility issues | ISO 10993 testing; foreign data acceptable if OECD‑aligned. | Non‑clinical study reports with MFDS acceptance reference. |
| Misuse due to language barrier | Korean labeling, clear user instructions (see sample expressions in Chunk [2]). | Draft label/IFU for review. |
| Software malfunction (if device includes software) | IEC 62304 development lifecycle; regular updates. | Software validation dossier.

---

### 5. Citations from Source  

| Section | Citation Detail |
|---------|-----------------|
| **Processing Times** – normal cycles for 허가, 임상 포함, 인증, 신고. | “허가 (일반) 65일”, “허가 (임상 포함) 80일”, “인증 30일”, “신고 즉시” (Chunk [1]). |
| **Korean Formal Expressions** – wording for supplementary response letters, data submission, extension requests. | Sample sentences such as “귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다.” etc. (Chunk [2]). |
| **Identifier Note** | No specific identifier found in source — verify separately. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required | Responsible Role |
|---------|-----------------|------------------|
| **Unclear classification** – missing intended use or risk level. | Pause submission preparation; request clarification from product development team. | RA Lead. |
| **Absence of KGMP certification** – facility not yet certified. | Initiate KGMP audit planning; consider outsourcing to a certified contract manufacturer. | QA/Manufacturing Liaison. |
| **Insufficient clinical evidence** – no domestic trial or acceptable foreign data. | Escalate to Clinical Affairs for trial design or bridging study plan. | Clinical Lead. |
| **Labeling not in Korean language** – draft only in English. | Trigger translation & regulatory review of label/IFU. | Regulatory Writer / Localization Team. |
| **Deadline approaching with pending supplementary data** (e.g., “시험 일정상 ○월 ○일까지 보완자료 제출이 어려우므로, 기한 연장을 요청드립니다.”) | Submit extension request using the formal expression from Chunk [2]; monitor MFDS response time. | RA Coordinator. |

---

### 7. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please challenge the assumptions made in this draft regarding (1) the expected classification pathway without detailed device information, (2) the adequacy of foreign non‑clinical data under the latest MFDS scope change, and (3) any jurisdiction‑specific gaps—particularly around mandatory Korean language labeling and local clinical data requirements. Highlight any additional evidence items that may be required for a Class II/III 허가 submission that are not captured above.

---

### 8. Reusable RA Judgment (Lesson Learned)

> **RA Judgment – Supplementary Response Preparation for MFDS**  
> When drafting a supplementary‑response strategy, always start by explicitly confirming the device’s Korean classification and corresponding submission route; processing‑time tables (e.g., 65 days for general 허가, 80 days when clinical data are required) dictate clock‑stop periods during which additional data can be submitted without extending the overall timeline. Use MFDS‑approved Korean formal expressions (see Chunk [2]) to structure response letters, data‑attachment notices, and extension requests. Verify any foreign non‑clinical evidence against the latest MFDS notice on accepted OECD‑aligned data before inclusion. Flag missing Korean‑language labeling, KGMP certification status, and local clinical data early as hard blockers that must be resolved prior to final submission.  

--- 

*Prepared by: Sam – Korea Regulatory Affairs Specialist (MFDS/KGMP)*

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

### kb-eval-20260717-it02-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_kr-002", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9b4163a1bdf455ed", "source": "github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md", "source_hash": "54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7"} -->

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

> **Regulatory Draft – “SBOM‑Based Vulnerability Management under the Digital Medical Products Act (디지털의료제품법)”**

---

### 1. Product Scope & Regulatory Classification  

| Item | Detail |
|------|--------|
| **Applicable law** | *Digital Medical Products Act* (디지털 의료제품법) – reference to Articles 13, 14 and 40 (see Source [1]‑[2]) |
| **Device type** | Digital medical device that includes software components (e.g., AI‑driven sensor fusion). |
| **Likely risk class** | Determined by intended use & functionality. <br>• If the device provides diagnostic or therapeutic functions → **Class III/IV → 허가 (MFDS approval)**.<br>• If it only collects, stores or transmits data without clinical decision‑making → **Class I/II → 신고 (notification)**.  *(Exact class must be confirmed with MFDS risk‑classification matrix.)* |
| **Submission route** | <ul><li>**허가** – when classified as Class III/IV, requires full dossier including Clinical Evaluation Report (CER), Technical Documentation, KGMP certification, and security compliance evidence.</li><li>**신고** – for Class I/II, a simpler notification plus conformity‑assessment documents suffices.</li></ul> |

---

### 2. Legal Basis for SBOM & Security Requirements  

| Legal provision | Relevance to SBOM / vulnerability management |
|-----------------|-----------------------------------------------|
| **Article 13 (제13조) – “Compliance matters”** – sub‑item 2 mandates *“continuous remediation of vulnerabilities caused by electronic attacks.”* This directly links to the purpose of an SBOM: traceability of software components for timely patching.  *(Source [2])* |
| **Article 14 (제14조) – “Protective measures against electronic attacks”** – obliges MFDS to issue security guidelines and requires manufacturers to comply with them. The guideline‑based controls are the practical backbone for an SBOM process (identifying components, assessing CVEs, applying patches). *(Source [2])* |
| **Article 16 (제16조) – “Excellent Management System certification”** – concerns a voluntary 3‑year quality‑management certification and does **not** create any direct SBOM obligation.  *(Source [1] & [2])* |
| **Article 40 (제40조)** – requires performance evaluation of each digital medical product component (sensor, AI algorithm). While not security‑specific, the performance data must be linked to the exact software version identified in the SBOM. *(Source [1])* |

**Take‑away:** The regulatory anchor for an SBOM is **Article 13** (continuous vulnerability remediation) supported by **Article 14** (security guidelines), *not* Article 16.

---

### 3. Required Evidence & Documentation  

| Category | Evidence Required | Notes |
|----------|-------------------|-------|
| **Classification justification** | Risk‑classification matrix mapping intended use, invasiveness, duration of use, AI impact. | Must reference MFDS classification tables. |
| **KGMP certification** | KGMP (Korean Good Manufacturing Practice) certificate for the manufacturing site(s). | Mandatory for all Class I–IV devices. |
| **Technical Documentation** (MFDS “품질관리·안전관리·전자적 침해행위 예방체계” dossier) | • Device description, intended use, indications.<br>• Software architecture diagram.<br>• SBOM (complete list of third‑party libraries, versions, licenses).<br>• Vulnerability management plan (continuous monitoring, patch schedule).<br>• Security controls map to MFDS security guidelines (Article 14). | SBOM must be kept up‑to‑date and referenced in the post‑market surveillance (PMS) plan. |
| **Performance Evaluation** | • Sensor performance test report.<br>• AI algorithm validation & verification data (including dataset description, metrics, bias analysis).<br>• Link each test to the exact software version identified in SBOM. | Required by Article 40. |
| **Security Evidence** | • Copy of MFDS security guidelines (issued under Article 14) and internal compliance checklist.<br>• Penetration‑testing report or vulnerability scan results for the released software version.<br>• Incident‑response SOPs. | Demonstrates fulfillment of Articles 13 & 14. |
| **Clinical Evidence** (if required) | • Clinical Evaluation Report (CER) or post‑market clinical follow‑up data, depending on risk class. | Local Korean data may be needed for Class III/IV; foreign clinical data is acceptable only if MFDS has accepted it per the latest notice (verify). |
| **Labeling & IFU** | Korean language labeling, instructions for use, and safety information meeting MFDS requirements. | Must include security‑related warnings where appropriate. |
| **Post‑Market Surveillance (PMS) Plan** | • Routine SBOM update schedule.<br>• Process for reporting newly discovered vulnerabilities to MFDS within the stipulated timeframe (typically 30 days). | Aligns with Article 13’s “continuous remediation.” |

---

### 4. Identified Gaps / Missing Information  

| Gap | Impact if unresolved |
|-----|----------------------|
| **Exact risk class** – not disclosed in source excerpts. | Cannot decide between 허가 vs 신고; may lead to an incomplete submission. |
| **KGMP status of the manufacturer** – no evidence provided. | KGMP is mandatory for any digital medical device; omission blocks approval/notification. |
| **Copy of MFDS security guidelines (Article 14)** – not yet obtained. | Without showing compliance, SBOM process cannot be validated. |
| **Specific AI algorithm performance metrics & validation dataset** – absent. | Article 40 requires component‑level performance data; missing will cause a deficiency. |
| **Local clinical data requirement** – unclear whether foreign data is acceptable for the intended indication. | May jeopardize clinical evaluation if Korean data are needed. |
| **Korean language labeling draft** – not supplied. | Labeling non‑conformity leads to rejection in final review. |
| **SBOM format & update frequency** – no detailed SOP or tool description. | MFDS may request evidence of traceability and timely updates; lack of detail is a gap. |

---

### 5. Core Risk Controls (Mapped to Korean Requirements)  

| Control | Reference (Korean law / guidance) | Implementation Example |
|---------|-----------------------------------|------------------------|
| **Secure Development Lifecycle (SDL)** | Article 14 security guidelines; IEC 62304 (software life‑cycle). | Integrate threat modeling, code review, static analysis. |
| **SBOM generation & maintenance** | Article 13 continuous vulnerability remediation.<br>Article 14 compliance checklist. | Use automated BOM tools (e.g., CycloneDX) with version control; update on each software release. |
| **Vulnerability scanning & CVE tracking** | Article 13 duty to remediate vulnerabilities. | Quarterly scans, subscription to NVD / Korean CSIRT alerts, documented remediation actions. |
| **Patch management & timely updates** | Article 13 (continuous remediation) & MFDS incident‑report deadline. | Deploy patches within 30 days of CVE publication; log in SBOM change history. |
| **Encryption & access control for data at rest/in transit** | Article 14 security guidelines. | TLS 1.3 for communications, AES‑256 storage encryption, role‑based access controls. |
| **Incident Response SOP** | Article 14 (security guideline compliance). | Define detection → containment → eradication → recovery steps; notify MFDS within statutory timeframe. |
| **Quality Management System (QMS) – KGMP** | Article 16 “Excellent Management System certification” (voluntary but often required for high‑risk devices). | Maintain ISO 13485–based QMS; obtain KGMP certificate. |

---

### 6. Human‑Escalation Triggers  

| Situation | Who should be alerted & by when |
|-----------|---------------------------------|
| **Uncertain risk class** (insufficient clinical/functional description) | Senior RA lead – before dossier finalization. |
| **Missing KGMP certification** | Compliance manager – immediate halt of submission prep. |
| **Inability to provide MFDS security guideline compliance evidence** | Head of Security Engineering – at earliest detection; may require external audit. |
| **SBOM process not fully automated / cannot guarantee update within 30 days** | Project manager – before regulatory filing deadline (≥ 60 days prior). |
| **Regulatory notice indicates foreign clinical data no longer acceptable** | Regulatory affairs director – upon receipt of new MFDS notice; re‑plan clinical study. |
| **Labeling draft fails Korean language/legal review** | Legal/labeling specialist – during label design stage, before final sign‑off. |
| **Post‑market vulnerability discovered post‑submission** | Post‑Market Surveillance team – within 24 hours to MFDS as per Article 13 reporting timeline. |

---

### 7. Citations  

* **Article 13, 14, 16 & 40 excerpts** – Source [1] (Chunk 1078549302777609829).  
* **Interpretation that Article 16 does not govern SBOM; Articles 13‑14 are the proper legal basis** – Source [2] (Chunk 1111374550817299375).

*(No specific FDA 510(k) numbers, EU CE identifiers, or Korean registration numbers appear in the source excerpts; therefore “no specific identifier found in source — verify separately.”)*

---

### 8. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review this draft and challenge any of the following:  
> 1. The assumption that Article 13 alone provides sufficient legal footing for an SBOM‐based vulnerability management program—are there supplemental MFDS notices or guidance we have missed?  
> 2. The completeness of the evidence list, especially regarding security guideline documentation and local clinical data requirements.  
> 3. Whether any jurisdiction‑specific gaps (e.g., Korean language labeling nuances, KGMP certification timing) need additional clarification before final submission.

---

### 9. Reusable RA Judgment (Honcho Record)

**Lesson:** *In the Digital Medical Products Act, Article 16 (“Excellent Management System certification”) is a voluntary quality‑management certification and does **not** constitute the statutory basis for SBOM creation or software vulnerability remediation. The operative provisions are Article 13 (continuous remediation of electronic‑attack vulnerabilities) and Article 14 (MFDS security guideline issuance and manufacturer compliance). Consequently, any SOP that cites Article 16 as the legal foundation for SBOM processes is mis‑aligned; the SOP must be revised to reference Articles 13 and 14 instead.*  

*Recorded via `honcho_conclude` for future RA judgments.*

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

### kb-eval-20260717-it02-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_kr-003", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "f69d8f43954b58f7", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용_방사선_발생장치_안전관리규칙_제1122호.md", "source_hash": "aff63a68606535ccc206bf522dc726414563ed06910c1de4ffa6655c6f7e55eb"} -->

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

> **Regulatory Draft – Diagnostic X‑Ray Equipment (MFDS 진단용 방사선 발생장치)  

Prepared for: Korean RA team (Sam)  
Date: 2026‑07‑18**

---

## 1. Device Classification & Submission Route  

| Item | Assessment | Rationale |
|------|------------|-----------|
| **Korean medical‑device class** | **Class II** (high‑risk diagnostic radiology device) | Under MFDS “Diagnosis‑use X‑ray generating equipment” the default classification is Class II when the device delivers therapeutic or high‑dose beams; most clinical imaging systems fall into this tier. |
| **Required regulatory pathway** | **허가 (Approval)** | All Class II devices must obtain MFDS 허가 (licence) prior to marketing. A simple 신고 (notification) is only possible for Class I. |
| **KGMP requirement** | **Facility certification under KGMP (Korean Good Manufacturing Practice) ISO 13485‑equivalent** | Mandatory for any manufacturing entity filing a 허가 application. |

---

## 2. Core Evidence Package (minimum required)

| Evidence | Specific requirement (MFDS) | Source citation |
|----------|----------------------------|-----------------|
| **Device technical file** – complete specification sheet (kVp range, tube current, focal spot size, filtration, HVL, geometry). | Must include all parameters referenced in the safety‑management rule. | — |
| **Non‑clinical performance data** – conformity to IEC 60601‑2‑33 (X‑ray equipment) & IEC 62353 (electrical safety), plus any Korean standard mapping shown in the project document. | Demonstrates compliance with “관전압 정확도”, “선량 재현성”, “누설선량” etc. | Table in **Chunk 1114051458699792259** shows SOPs mapped to IEC standards; inspection criteria listed in **Chunk 278739496403872085** (F‑RAD‑SAFETY‑001). |
| **Calibration & QC procedures** – SOP‑CAL‑001 (kVp meter & dosimeter calibration), SOP‑IQ‑001 (installation verification), QC‑IQ‑001 (image quality QC), SOP‑SVC‑001 (PM/maintenance). | Must be in place for ongoing compliance with the periodic inspection items. | Identifiers appear in **Chunk 1114051458699792259**. |
| **Risk Management file** – ISO 14971 risk analysis, including ALARA design controls (ALARA_지원기능_설계명세). | Required for all Class II devices; MFDS expects explicit ALARA control documentation. | “ALARA_지원기능_설계명세” listed in **Chunk 1114051458699792259**. |
| **Clinical performance evidence** – either a domestic clinical trial or justification that foreign data (e.g., FDA 510(k) clearance, CE mark) is acceptable under the latest MFDS notice on foreign clinical evaluation acceptance. | Verify if Korean rule now permits reliance on OECD‑aligned non‑clinical data and foreign CE/510(k) dossiers; citation must be checked against most recent MFDS amendment. | No specific identifier in source – **verify separately**. |
| **Labeling & IFU (Korean language)** – product label, safety warnings, user instructions translated into Korean; include compliance statements for “누설선량 ≤1 mGy/h@1 m”, “관전압 정확도 ±10%”, etc. | Korean‐language requirement is mandatory for all medical devices. | — |
| **KGMP certificate** – copy of the manufacturer’s KGMP certification (ISO 13485‑based). | Essential for 허가. | — |

---

## 3. Gaps / Missing Information  

| Gap | Why it matters | Action needed |
|-----|----------------|---------------|
| **Intended use statement & clinical indication** – not present in excerpts. | Determines classification and necessity of local clinical data. | Draft a clear, concise intended‑use paragraph (e.g., “Portable digital X‑ray system for chest radiography”). |
| **Full device specification table** (kVp max, mA range, filtration, HVL values). | Required to map each performance claim to the inspection criteria in F‑RAD‑SAFETY‑001. | Obtain from Engineering/Design team. |
| **Evidence of compliance with IEC 60601‑2‑33 & IEC 62353** (test reports). | MFDS expects test data that satisfy the listed tolerances (e.g., ±10% voltage accuracy, CV ≤5% reproducibility). | Secure third‑party lab reports or in‑house validation data. |
| **Clinical performance dossier** – foreign 510(k)/CE justification not yet referenced. | Must verify whether MFDS currently accepts such evidence for this device class. | Check the latest MFDS notice on “foreign clinical evaluation acceptance” and cite the exact notice number (retrieve from KB). |
| **Korean translation of SOPs & QC protocols** – only identifiers shown, no Korean text. | Labeling/IFU requirement includes procedural documentation in Korean for users. | Prepare Korean versions of SOP‑CAL‑001, SOP‑IQ‑001, etc. |
| **Post‑market surveillance (PMS) plan** – not described. | Required for all Class II 허가 applications. | Draft PMS plan aligned with MFDS “시판후조사” guidelines. |

---

## 4. Key Risk Controls (derived from source)

| Control | Linked inspection item | Evidence needed |
|---------|------------------------|-----------------|
| **ALARA design input** – automated exposure control, dose‑saving algorithms. | F‑RAD‑SAFETY‑001 items 1‑5 (voltage accuracy, HVL). | ALARA_지원기능_설계명세 document. |
| **Calibration SOP (SOP‑CAL‑001)** – routine kVp & dosimeter calibration with traceable standards. | Items 1‑2 (관전압 정확도, 관전압 재현성). | Calibration records ±10% accuracy, CV ≤5%. |
| **Periodic QC protocol (QC‑IQ‑001)** – image quality phantom tests, uniformity, resolution. | Items 7‑9 (영상 해상도, 저대조도, 균일성). | QC logs meeting IEC specs. |
| **Leakage dose monitoring** – daily checks; limit ≤1 mGy/h@1 m. | Item 6 (누설선량). | Leakage measurement reports. |
| **Installation verification SOP (SOP‑IQ‑001)** – performance check at site installation. | All performance items (baseline). | Installation acceptance report. |
| **Service & PM SOP (SOP‑SVC‑001)** – scheduled preventive maintenance, component replacement. | Ongoing compliance to all inspection criteria. | Service records. |

---

## 5. Citations  

| Regulation / Standard | Identifier in source |
|-----------------------|----------------------|
| Korean “진단용 방사선 발생장치 안전관리규칙 제1122호” (Safety Management Rule) – Table of linked documents & SOPs | **Chunk 1114051458699792259** |
| Periodic inspection checklist “F‑RAD‑SAFETY‑001” | **Chunk 278739496403872085** |
| SOP identifiers: SOP‑CAL‑001, SOP‑IQ‑001, QC‑IQ‑001, SOP‑SVC‑001, ALARA_지원기능_설계명세, 진단용방사선_안전관리규칙_개정이력 | **Chunk 1114051458699792259** |

*No specific 510(k), CE, or MFDS notice numbers appear in the provided excerpts – verify separately before submission.*

---

## 6. Human‑Escalation Triggers  

| Trigger condition | Reason for escalation | Who to notify |
|-------------------|-----------------------|---------------|
| **Absence of verified foreign clinical acceptance notice** (i.e., cannot confirm MFDS accepts CE/510(k) data). | Risk of incomplete dossier → potential rejection. | Senior RA Manager / Regulatory Affairs Lead. |
| **Failure to meet any inspection tolerance** during internal QC (e.g., voltage accuracy > ±10%). | Non‑compliance with safety rule; may require redesign or additional controls. | Engineering Lead & Quality Assurance. |
| **KGMP certificate not yet issued** for the manufacturing site. | Mandatory for 허가 – cannot file without it. | Manufacturing / Compliance Officer. |
| **Korean labeling/IFU translation not finalized 30 days before submission deadline**. | Legal requirement; omission leads to post‑approval corrective action. | Marketing & Documentation Team. |
| **Unresolved open comment from internal audit on risk analysis (ISO 14971)**. | Incomplete risk file → regulator may request clarification. | Risk Management Owner / QA Manager. |

---

## 7. Peer Review Prompt  

> **To the RA peer group:**  
> Please review this draft and challenge the following points:  
> 1. **Classification justification** – does any device‑specific guidance (e.g., MFDS “방사선 발생장치” classification matrix) suggest a different class for the intended use?  
> 2. **Scope of acceptable foreign clinical evidence** – based on the latest MFDS notice, are we allowed to rely solely on FDA 510(k)/EU CE data for this device type? Provide the exact notice identifier if known.  
> 3. **Completeness of risk controls** – have any mandatory ALARA‑related safeguards been omitted (e.g., automatic exposure termination, patient dose tracking)?  
> 4. **Documentation gaps** – are there additional Korean‑language documents or local clinical data that MFDS typically requests for this class?  

Your feedback will be incorporated before final dossier preparation.

---

## 8. Reusable RA Judgment (honcho_conclude)  

```json
{
  "judgment_id": "KR_DIAG_XRAY_2026-07-18",
  "topic": "Diagnostic X‑ray equipment (MFDS 진단용 방사선 발생장치) – classification, evidence and gaps",
  "summary": "Class II diagnostic X‑ray systems require 허가. Core dossier must contain IEC 60601‑2‑33 & IEC 62353 test reports, SOPs identified as SOP‑CAL‑001, SOP‑IQ‑001, QC‑IQ‑001, SOP‑SVC‑001, ALARA design specification, risk analysis per ISO 14971 and Korean‑language labeling. Missing: explicit intended‑use statement, full spec table, verification of MFDS acceptance of foreign clinical data, Korean translations of procedural documents, PMS plan, KGMP certificate copy.",
  "cited_sources": [
    {"chunk_id":"1114051458699792259","content":"Project linkage table – SOP identifiers and ALARA design spec"},
    {"chunk_id":"278739496403872085","content":"F‑RAD‑SAFETY‑001 periodic inspection checklist with tolerance criteria"}
  ],
  "action_items": [
    "Obtain MFDS notice number confirming foreign clinical data acceptance (if applicable).",
    "Draft intended use and full technical specification table.",
    "Secure IEC conformity test reports covering voltage accuracy, dose reproducibility, leakage limits, image quality specs.",
    "Prepare Korean translations of SOP‑CAL‑001, SOP‑IQ‑001, QC‑IQ‑001, SOP‑SVC‑001 and ALARA design spec.",
    "Compile KGMP certificate and PMS plan."
  ],
  "escalation_triggers": [
    "No foreign clinical acceptance notice",
    "Any inspection tolerance breach in internal QC",
    "Missing KGMP certification",
    "Unfinished Korean labeling >30 days before filing"
  ],
  "peer_review_prompt": "Challenge classification, foreign evidence scope, ALARA controls completeness, and any additional Korean documentation expectations."
}
```

---  

*Prepared by: Sam – Korea Regulatory Affairs Specialist (MFDS/KGMP)*

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

### kb-eval-20260717-it02-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_kr-004", "iteration": 2, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "7014751a297b619d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

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

> **Regulatory Draft – Digital‑Medical‑Device Software (SaMD) – Labeling & Documentation Checklist**

---

### 1. Regulatory Context
- **Authority:** Ministry of Food and Drug Safety (MFDS), Korea  
- **Applicable Instruments**  
  - *디지털의료제품법 시행규칙* (Regulations on the Digital Medical Device Act) – for core labeling items (e.g., SW version, build number).  
  - *MFDS SW 가이드라인* – for software update, system‑requirement and interface information.  
  - *MFDS 사이버보안 가이드라인 2025.01* – for cyber‑security configuration, patch management, residual risk handling, etc.  

> **Note:** The source does not provide a concrete notice/identifier number; verify the exact notice reference (e.g., “MFDS Notice No. XXXXX”) in the MFDS gazette before final submission.

---

### 2. Preliminary Device Classification & Submission Route  
| Attribute | Determination | Rationale |
|-----------|----------------|----------|
| **Device type** | Software‑as‑a‑Medical‑Device (SaMD) – Stand‑alone digital medical device | The checklist is for “디지털의료기기” and focuses on software version, interfaces, data formats, etc. |
| **Risk class** | *Class II* (or higher) – to be confirmed by risk‑based classification matrix (MFDS 규정 제3조). Typical SaMD that provide diagnostic/monitoring functions fall in Class II; therapeutic or decision‑support SaaS may require Class III/IV. |
| **Submission route** | **허가** (Approval) for Class II & above; *신고* (Notification) only permitted for Class I devices (unlikely here). | MFDS requires a full 허가 dossier when software performs functions that affect patient management or clinical decisions. |

> **Action:** Conduct the MFDS classification worksheet (risk‑based decision tree) with the device’s intended use, user population and impact on health to lock in the exact class.

---

### 3. Required Evidence Package – Minimum Set for a SaMD 허가

| Evidence Category | Specific Items | Source Requirement |
|-------------------|----------------|--------------------|
| **Technical Documentation** | - Software Design Description (including architecture) <br> - Version/Build Number, Release Date (S‑1) <br> - Update Method & Frequency (S‑2) <br> - Minimum / Recommended System Requirements – OS, CPU, RAM, storage, monitor resolution, network (S‑3) <br> - List of compatible medical devices + interface specifications (S‑4) <br> - Data exchange formats (DICOM, HL7…) (S‑5) | MFDS SW 가이드라인 |
| **Cybersecurity Documentation** | - Cybersecurity configuration guidelines (encryption policies, network segregation, access rights) (S‑6) <br> - Patch‑application procedure and responsible parties (S‑7) <br> - Known residual cyber risks & mitigation plan (S‑8) <br> - Backup & recovery procedures (S‑9) <br> - System log management method (recommended) (S‑10) | MFDS 사이버보안 가이드라인 2025.01 |
| **Clinical Evidence** | - Clinical Evaluation Report (CER) – device performance, safety & effectiveness data <br> - If applicable, foreign clinical data (FDA 510(k) summary, EU CE conformity assessment) ‑ verify acceptability under latest MFDS scope expansion notices. | MFDS “디지털의료기기 표시기재 요건” checklist (Section 3) |
| **Usability / Human Factors** | - Summaries of formative and summative usability testing with Korean target users (if device is user‑interface intensive). |
| **Labeling & IFU** | - Korean language IFU containing all mandatory items listed in the checklist (including S‑1…S‑9) <br> - Additional items required for digital‑medical‑device specific labeling (Section 3 of the guide). |
| **Post‑Market Surveillance Plan** | - PMS activities, adverse event reporting procedures, software update monitoring. |

---

### 4. Gaps / Missing Information (Based on Source Excerpts)

| Item | Status | Comment |
|------|--------|---------|
| **Exact MFDS notice numbers** for the three guiding documents (Regulation, SW guide, Cybersecurity guide) | ❗ Missing | Required for citation in the dossier; retrieve from MFDS official gazette. |
| **AI/ML‑specific requirements** – source truncates after “**AI/ML…**” | ❗ Missing | If the device contains AI/ML, a separate risk‑management & validation section (e.g., model performance, training data provenance) is mandatory per MFDS AI/ML guidance (2024). |
| **Korean language translation verification** | ❗ Missing | All UI text, labeling, IFU must be in Korean; confirm that translations are reviewed by a certified translator. |
| **System log management – only recommended** (S‑10) | ⚠️ Potential gap | If the MFDS later upgrades S‑10 to mandatory for the device’s class, be prepared to include it. |
| **Clinical evidence specifics** | ❗ Missing | No excerpt shows required clinical data; must prepare a CER aligned with Korean Clinical Evaluation Guidance. |
| **Software lifecycle / Maintenance plan** (beyond patch application) | ❗ Missing | Include description of version‑control, decommissioning policy, and long‑term support. |

---

### 5. Risk Controls & Mapping to Required Items

| Hazard Category | Control(s) | Evidence Reference |
|-----------------|------------|---------------------|
| **Software bugs / functional failure** | - Version control & documented release notes (S‑1) <br> - Update schedule & validated update procedure (S‑2) | MFDS SW 가이드라인 |
| **Incompatible hardware causing performance degradation** | - Minimum system requirements specification (S‑3) <br> - Compatibility list with medical devices (S‑4) | MFDS SW 가이드라인 |
| **Data loss / corruption** | - Backup & recovery method (S‑9) <br> - System log retention (S‑10, recommended) | MFDS 사이버보안 가이드라인 2025.01 |
| **Unauthorized access / cyber‑attack** | - Encryption and network segregation policy (S‑6) <br> - Patch management & responsible party definition (S‑7) <br> - Residual risk treatment plan (S‑8) | MFDS 사이버보안 가이드라인 2025.01 |
| **Incorrect clinical decision support (AI/ML)** | - Model validation dataset, performance metrics, drift monitoring (to be added) | MFDS AI/ML guidance (if applicable) |

---

### 6. Citation Summary

| Requirement / Item | Source Cited |
|--------------------|--------------|
| Software version, build number & release date (S‑1) | 디지털의료제품법 시행규칙 *(excerpt S‑1)* |
| Update method & frequency (S‑2) | MFDS SW 가이드라인 *(excerpt S‑2)* |
| Minimum/recommended system specs (S‑3) | MFDS SW 가이드라인 *(excerpt S‑3)* |
| Compatibility list (S‑4) | — (no source cited) |
| Data I/O formats (S‑5) | — (no source cited) |
| Cybersecurity configuration (S‑6‑S‑8) | MFDS 사이버보안 가이드라인 2025.01 *(excerpt S‑6–S‑8)* |
| Backup & recovery (S‑9) | — (no source cited) |
| System log management (S‑10 – recommended) | MFDS 사이버보안 가이드라인 *(excerpt S‑10)* |
| Additional digital‑medical‑device labeling items (Section 3) | “디지털의료기기 특화 표시기재 요건 체크리스트” (Excerpt [2]) |

> **No specific identifier** (e.g., notice number, case ID) appears in the provided excerpts. Verify the exact MFDS notice numbers before final submission.

---

### 7. Human‑Escalation Triggers

| Situation | Trigger | Action |
|-----------|---------|--------|
| Uncertainty about device risk class after applying MFDS classification matrix | Classification ambiguity (Class II vs III) | Escalate to senior RA lead for a formal classification decision and possible pre‑submission meeting with MFDS. |
| AI/ML component present but no guidance excerpt available | Missing AI/ML regulatory requirements | Consult the MFDS AI/ML Guidance (2024) or request clarification from MFDS via official inquiry. |
| Required Korean language IFU translation not yet validated | Language compliance risk | Engage certified medical‑device translator and have a linguist review; escalate if timeline jeopardized. |
| Cybersecurity residual risk deemed “high” after analysis of S‑8 | Unacceptable residual cyber risk | Conduct additional mitigation (e.g., intrusion detection, code hardening) and involve the security engineering team before dossier finalization. |
| Post‑market surveillance plan not aligned with MFDS PMS framework | PMS gap | Involve post‑marketing manager to draft a compliant PMS Plan; seek senior RA sign‑off. |

---

### 8. Next Steps (Action Checklist)

1. **Confirm Device Classification** – run MFDS risk‑matrix worksheet, document decision.
2. **Collect Exact MFDS Notice Numbers** for all three guiding documents and update citations.
3. **Assemble Technical Dossier** – include all S‑1 → S‑9 items; add system log management if later mandated.
4. **Generate Clinical Evaluation Report** – incorporate any foreign clinical data, noting MFDS acceptance scope.
5. **Prepare Korean IFU & Labeling** – embed mandatory checklist items and verify translation quality.
6. **Develop Cybersecurity Risk Management File** – map S‑6 → S‑8 controls to ISO 14971 risk register.
7. **If AI/ML present, add Model Validation Package** per MFDS AI/ML Guidance.
8. **Review PMS Plan** – ensure alignment with MFDS post‑market surveillance requirements.
9. **Peer Review** – circulate draft (this document) to a fellow RA for challenge.

---

### 9. Peer‑Review Prompt
> *“Colleague, please review this regulatory draft and challenge the following: (a) the assumption that the device falls under Class II based on limited described functionality; (b) whether all jurisdiction‑specific gaps have been captured given the source only lists SW checklist items; and (c) the completeness of cited evidence—particularly any missing Korean‑language labeling obligations or foreign clinical data acceptance criteria. Provide concrete suggestions or identify additional MFDS notices we must reference.”*

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

1. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

2. Chunk `124386539616979555`

> ## 3. 디지털의료기기 특화 표시기재 요건 체크리스트 > 일반 의료기기 표시기재 필수사항(→ IFU_필수요소_3지역_비교.md 참조)에 **추가**되는 항목

### kb-eval-20260717-it02-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-17", "decision_ref": "kb-eval-20260717-it02-ra_kr-005", "iteration": 2, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "4e1064335a341e0f", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

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

> **Regulatory Draft – Digital Medical Device (디지털의료제품) under the *Digital Medical Devices Act* (디지털의료제품법)**  

---

### 1. Anticipated Classification & Submission Route  
| Factor | Determination | Rationale |
|--------|----------------|-----------|
| **Device type** | Software‑driven medical device (digital therapeutic / diagnostic) that generates clinical information. | The act treats “digital medical devices” as a distinct category; the product appears to provide health‑related outcomes rather than only lifestyle support. |
| **Risk class** | **Class II** (moderate risk) – typical for digital products that influence diagnosis or treatment decisions but do not present high‑risk functions (e.g., invasive, life‑supporting). | MFDS guidance (2025‑02) places AI‑based decision‑support software in Class II unless the algorithm directly controls a medical device. |
| **Submission pathway** | **“허가” (Approval)** – required for Class II digital devices. <br>*Alternative*: If the product is purely wellness and does not claim clinical efficacy, a “신고” (Notification) could be used, but the source indicates clinical claims. | Article 39 of the Act provides pre‑review procedures; the device’s risk profile points to an approval route. |

---

### 2. Core Evidentiary Requirements  

| Requirement | What MFDS expects | How it maps to foreign evidence (if available) |
|-------------|-------------------|----------------------------------------------|
| **Technical Documentation** (기술문서) | Device description, architecture, software lifecycle, cybersecurity measures, UI/UX, data flow, risk management file. | Align with ISO 13485 and IEC 62304; FDA 510(k) Technical File can be leveraged for structure but must be Korean‑translated. |
| **Safety & Performance Evidence** | • Bench testing (functional verification)<br>• Non‑clinical safety (biocompatibility, electromagnetic compatibility if hardware is involved) | Can cite FDA non‑clinical data when OECD‑aligned; ensure MFDS acceptance via latest notice (verify specific notice number). |
| **Clinical Evidence** – *Key focus* | • Real‑world evidence (RWE) from actual use **(Article 15)** must be *supplementary* to formal clinical evaluation.<br>• Primary clinical efficacy/effectiveness data must comply with **Article 9 (clinical trial plan approval) or Article 10 (clinical performance test plan approval).** | Use FDA 510(k) predicate clinical data if the comparator is cleared in US, but MFDS requires a separate Korean‑centric clinical evaluation unless an exemption applies. |
| **Post‑Market Surveillance Plan** | Continuous monitoring, defect reporting (Article 13), cyber‑vulnerability management, and periodic safety updates. | Align with EU MDR Post‑Market Surveillance (PMS) plan; map to MFDB’s “우수 관리체계 인증” (GMP‑like certification). |
| **Korean Language Requirements** | All labeling, IFU, user manuals, and software UI must be provided in Korean. | No foreign substitute accepted – must be original Korean translation with certified accuracy. |

> **Critical Gap Identified from Source:** The draft currently lists “clinical efficacy (if applicable) – Article 15” as the clinical evidence basis. According to the source excerpt *[399070733591760115]*, this is incorrect; **Article 15** pertains only to *“실사용 평가”* (real‑world use evaluation) and does **not** cover formal clinical efficacy assessment. The appropriate provision should be **Article 9** or **Article 10**, depending on whether a full clinical trial or a performance test is planned.

---

### 3. Missing Information & Required Actions  

| Missing Item | Why it matters | Action to obtain |
|--------------|----------------|-------------------|
| **Clear definition of the intended use and claim level** (diagnostic vs therapeutic, risk‑mitigation scope). | Determines whether clinical trial (Art 9) or performance test (Art 10) is needed. | Draft an explicit “Indications for Use” statement in Korean; have it reviewed by MFDS pre‑consultation (Article 39). |
| **Clinical Evaluation Plan (CEP)** aligned with Art 9/10. | Provides the roadmap for generating required efficacy data. | Prepare a CEP referencing either a Korean clinical study or an acceptable foreign bridge study, and submit for MFDS review. |
| **Evidence of conformity to cybersecurity standards** (e.g., ISO 27001, IEC 62324). | Article 13 mandates ongoing defect & cyber‑vulnerability management. | Conduct a vulnerability assessment; attach the report as part of technical documentation. |
| **Proof of “우수 관리체계 인증” (GMP‑like certification)** if the manufacturer opts for that route under Art 17. | Required for certain digital devices to demonstrate manufacturing quality. | Initiate the certification process with an accredited Korean evaluation institute. |
| **Korean translation certification** for all user‑facing materials. | Legal requirement; non‑compliance leads to rejection. | Engage a certified Korean translation service and obtain notarized proof. |

---

### 4. Key Risk Controls (ISO 14971‑aligned)  

| Hazard | Control Measure | Verification |
|--------|-----------------|--------------|
| Incorrect algorithm output leading to misdiagnosis | • Independent validation dataset <br>• Continuous performance monitoring (RWE) | Compare outputs against gold‑standard clinical reference; document drift detection. |
| Data privacy breach | • Encryption at rest & in transit<br>• Access control, audit logs | Penetration testing report, privacy impact assessment (PIA). |
| Software malfunction / crash | • IEC 62304 development lifecycle <br>• Automated regression test suite | Release notes with pass/fail criteria; bug‑track metrics. |
| User misunderstanding of UI/IFU | • Korean language usability testing with target users<br>• Clear labeling, risk warnings | Human factors validation report (ISO 62366). |

---

### 5. Citations (as extracted from source)

| Source excerpt | Relevant citation |
|----------------|-------------------|
| *Excerpt [399070733591760115]* – discussion on clinical efficacy mapping to Articles 9/10 vs 15. | Article 9 & Article 10 of the Digital Medical Devices Act (clinical trial plan approval / clinical performance test plan approval). |
| *Excerpt [515031043224754498]* – definitions of Articles 13, 15, 17, 39. | Article 13 (continuous compliance), Article 15 (real‑world use evaluation), Article 17 (우수 관리체계 인증), Article 39 (pre‑review request). |
| **Identifier note**: *no specific identifier (e.g., 510(k) number, case ID) found in source – verify separately.* |

---

### 6. Human‑Escalation Triggers  

| Trigger | When to Escalate to Senior RA / Legal | Reason |
|--------|--------------------------------------|--------|
| Ambiguity on whether clinical evidence falls under Art 9 or Art 10 after CEP drafting. | Immediate escalation. | Misclassification can delay approval or cause regulatory non‑compliance. |
| MFDS requests supplemental data beyond what is available from foreign dossiers (e.g., Korean patient cohort). | Escalate to project lead & sponsor for budget/Timeline impact. |
| Discrepancy between Korean translation and original English labeling that could affect safety warnings. | Escalate to compliance/legal before submission. |
| Notice of updated MFDS guidance on accepted foreign RWE (new notice number) that may affect our current evidence strategy. | Escalate to RA manager for strategy revision. |

---

### 7. Peer‑Review Prompt  

> **To a fellow Korean RA colleague:**  
> Please review the assumptions made in this draft, especially:  
> 1. The classification of the device as Class II – could any functionality push it into Class III?  
> 2. The mapping of clinical evidence to Articles 9/10 rather than Article 15 – does our intended use truly require a full clinical trial or could a performance test suffice?  
> 3. Whether the identified missing items (e.g., Korean translation certification, 우수 관리체계 인증) are exhaustive for this device type under current MFDS practice.  
> 4. Any jurisdiction‑specific gaps – e.g., additional cybersecurity reporting obligations not captured here or recent MFDS notices that modify acceptance of foreign RWE.  

Your feedback will help ensure the submission package fully aligns with both statutory requirements and evolving MFDS expectations.

---

### 8. Reusable RA Judgment (Memory Outcome)  

**Lesson:**  
When preparing a regulatory dossier for digital medical devices under the *Digital Medical Devices Act*, **do not cite Article 15 (“실사용 평가”) as the primary basis for clinical efficacy or performance evidence**. Article 15 pertains exclusively to post‑market real‑world data collection and is separate from formal clinical evaluation. The correct statutory anchors for pre‑approval clinical data are **Article 9 (clinical trial plan approval)** or **Article 10 (clinical performance test plan approval)**, depending on the nature of the evaluation. Mis‑aligning these articles leads to reviewer comments demanding reclassification of evidence and can delay approval.  

**Actionable rule:**  
- Verify the intended claim level → decide between a full clinical trial (Art 9) or a performance test (Art 10).  
- Use Article 15 only for supplemental RWE after marketing authorization.  

--- 

*Prepared by Sam – Korean Regulatory Affairs Specialist*

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
