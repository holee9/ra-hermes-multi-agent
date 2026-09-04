# KB Eval Checksheet - 2026-07-18 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260718-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "b09c788de30adb23", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

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

> **Regulatory Draft – Impact of SaMD Algorithm Change under the Predetermined Change Control Plan (PCCP)**  

---

### 1. Device Classification & Submission Pathway
| Attribute | Determination |
|-----------|----------------|
| **Device type** | Software as a Medical Device (SaMD) that incorporates AI/ML. |
| **Regulatory class** | *Presumed* Class II – most AI‑based diagnostic or clinical decision support SaMD are classified II under 21 CFR 862. Confirmation required via predicate review. |
| **Primary submission route** | **510(k)** with a **PCCP amendment** (see FDA guidance on “Predetermined Change Control Plans for Artificial Intelligence‑Based Medical Devices”). If the change exceeds predetermined scope, a new 510(k) or De Novo may be needed. |

*Citation*: No specific identifier found in source — verify separately.

---

### 2. Required Evidence for PCCP Submission

| Pillar (per FDA guidance) | Minimum Documentation |
|----------------------------|------------------------|
| **Data Management** | - Detailed SOPs for data collection, curation, version control.<br>- Bias mitigation strategy (demographics, acquisition settings). |
| **Retraining Practices** | - Defined algorithm‑retraining triggers (e.g., performance drift > X%, new data volume Y%).<br>- Retraining workflow description, including validation set separation.<br>- Rollback plan: criteria and process to revert to prior model version. |
| **Performance Evaluation** | - Pre‑specified acceptance criteria (sensitivity, specificity, AUC) with statistical justification (e.g., α = 0.05, power ≥ 80%).<br>- Verification & Validation (V&V) methodology aligned to IEC 62304/IEC 82304.<br>- Evidence of statistical significance for any performance change. |
| **Updated Procedures** | - Communication plan for users and clinicians (IFU amendments, release notes).<br>- Real‑world monitoring strategy (post‑market performance dashboard, adverse event reporting).<br>- Procedure to update labeling/IFU when the model changes. |

*Citation*: Extracted from source [2] (Modification Protocol mandatory items).

---

### 3. Gaps / Missing Information (to be supplied before filing)

| Area | What’s missing |
|------|----------------|
| **Dataset specifics** | Exact sources, size, labeling methodology, diversity metrics, and versioning details. |
| **Trigger thresholds** | Quantitative values for “performance drift” or “data volume” that would initiate retraining. |
| **Statistical plan** | Sample‑size calculations, confidence intervals, handling of class imbalance. |
| **Rollback mechanics** | Automated vs. manual switchback, verification after rollback, documentation trail. |
| **User communication templates** | Draft IFU updates, notification timelines, and distribution channels. |
| **Risk Management file** | Updated ISO 14971 risk analysis reflecting algorithm change impacts (bias, drift, failure modes). |

---

### 4. Core Risk Controls (aligned to FDA & IEC standards)

1. **Algorithmic Bias Control** – Continuous monitoring of demographic performance; bias mitigation procedures documented in Data Management.
2. **Performance Drift Detection** – Real‑time statistical process control charts; automatic alerts when predefined thresholds are breached.
3. **Software Change Validation** – Independent V&V for each new model version, including stress testing and robustness checks.
4. **Rollback Assurance** – Verified ability to revert to prior version without loss of patient data or functionality.
5. **User Training & Documentation** – Updated IFU and training materials delivered before deployment of a new algorithm version.
6. **Post‑Market Surveillance (PMS)** – Structured adverse event reporting pathway; periodic safety update reports.

---

### 5. Human‑Escalation Triggers

| Trigger | Action Required |
|---------|-----------------|
| **Performance below acceptance criteria** (e.g., sensitivity drops > 5% from baseline) | Immediate suspension of the updated model, root‑cause analysis by R&D, and notification to FDA via a 510(k) supplement or safety notice. |
| **Serious adverse events linked to algorithm output** | Report under 21 CFR 820.80; convene a multidisciplinary review (clinical, QA, regulatory). |
| **Change exceeding predetermined scope** (new indication, substantially different input data) | File a new 510(k) or consider De Novo pathway; obtain FDA concurrence before release. |
| **Failure of rollback mechanism** | Escalate to senior management and submit a corrective action plan to FDA within the next reporting cycle. |
| **Regulatory policy update (e.g., FDA releases revised AI guidance)** | Re‑evaluate PCCP alignment, update SOPs, and submit an amendment if required. |

---

### 6. Citations

- Source [1]: Overview of FDA’s “Predetermined Change Control Plan” framework for AI devices.  
- Source [2]: Mandatory items for a Modification Protocol (Data Management, Retraining Practices, Performance Evaluation, Updated Procedures).  

*No specific 510(k) predicate or registration numbers appear in the source excerpts; verify separately before submission.*

---

### 7. Peer‑Review Prompt

> **RA Colleague, please review:**  
> - Are the assumed Class II/510(k) pathway and the identified predicate scope realistic for this SaMD?  
> - Does the evidence checklist fully capture FDA’s PCCP expectations, or are any critical elements (e.g., IEC 62304 software lifecycle documentation, cybersecurity considerations) omitted?  
> - Have we adequately addressed jurisdictional gaps, especially potential differences between U.S. and EU AI‑MD regulations referenced in source [1]?  

---

### 8. Reusable RA Judgment (Lesson Record)

**Judgment:** When evaluating AI/ML SaMD changes under a Predetermined Change Control Plan, structure the submission evidence around the four mandatory protocol elements—Data Management, Retraining Practices, Performance Evaluation, and Updated Procedures—and explicitly map each to FDA guidance citations. Flag any quantitative thresholds, dataset provenance, statistical plans, and rollback details as missing items that must be resolved before filing. Include clear human‑escalation triggers for performance degradation or scope creep to satisfy post‑market risk management obligations.  

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 147/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,331자 | — |
| 규제 식별자 인용 | 5개 | — |
| source excerpt 근거 일치 | **0/5 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 5개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 862`, `IEC 82304`, `21 CFR 820.80`
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

1. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

2. Chunk `198015203798949382`

> ### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---

### kb-eval-20260718-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "a852077f86f0109a", "source": "github:holee9/MD-process/issue-drafts/920_AUDIT_EU_AI_Act_FDA_PCCP_Draft2023_노후.md", "source_hash": "efcd12a4b49cb21ffa28b5f1aa35345e8bb04b98c57a32649483fa824de23fff"} -->

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

> **Regulatory Draft – FDA Predetermined Change Control Plan (PCCP) for AI‑Enabled SaMD**

---

### 1. Bottom Line
| Item | Recommendation |
|------|----------------|
| **Device class** | Likely **Class II** (AI‐enabled SaMD that performs “non‑critical” clinical functions). |
| **Primary submission route** | Existing 510(k) **substantial equivalence** clearance with a **PCCP‑based 510(k) supplement** for anticipated software changes. |
| **Alternative pathway** | If the change introduces a new intended use or substantially alters risk, file a **new 510(k)** (or De Novo if no predicate exists). |

---

### 2. Classification Rationale
* FDA’s **Digital Health Software Precertification Program** and traditional device classification places most AI‑enabled diagnostic/monitoring software in **Class II** under 21 CFR 862.1 (radiology) or 862.108 (clinical decision support) unless the function is life‑supporting, which would trigger Class III. The excerpt does not indicate a life‑supporting claim.

---

### 3. Submission Pathway Details
| Change Type | Applicable FDA Mechanism |
|-------------|--------------------------|
| **Within the scope of an approved PCCP** (e.g., model updates, algorithm drift corrections) | **510(k) supplement – “Changes to Software Algorithm”** (use FDA Form 3514). No new predicate required. |
| **Outside PCCP scope** (new indication, new data inputs, change in risk profile) | **New 510(k)** with appropriate predicate or **De Novo** if no predicate exists. |
| **Minor edits not affecting safety/performance** | **Special 510(k)** may be used; however, most AI updates are deemed “significant” and thus require a full supplement. |

---

### 4. Required Evidence for PCCP‑Based Changes
1. **Software Change Documentation**
   - Version control logs, change description, rationale.
2. **Verification & Validation (V&V)**
   - Unit, integration, system testing results confirming unchanged performance metrics.
3. **Algorithm Performance Data**
   – Re‑run validation dataset; report key statistical measures (AUROC, sensitivity/specificity) compared to baseline.
4. **Risk Management Update**
   – IEC 62304–compliant risk analysis reflecting new model behavior; update of ISO 14971 hazard log.
5. **Usability/Human Factors**
   – Confirmation that UI or workflow changes remain within established use error limits (per FDA Human Factors Guidance).
6. **Labeling Review**
   – Ensure intended‑use statements and performance claims continue to be accurate.

---

### 5. Missing Information / Gaps in Source
| Gap | Why it matters |
|-----|----------------|
| **Exact definition of the PCCP scope** (which algorithm parameters are covered) | Determines whether a given change is “predetermined” or requires a new submission. |
| **Reference to specific FDA guidance identifier** (e.g., DG‑2024‑XXX) | Needed for citation in the 510(k) supplement and internal SOPs. |
| **Risk control measures tied to AI drift mitigation** | Required for updating IEC 62304/ISO 14971 risk management files. |
| **Post‑market monitoring plan for AI performance** | FDA expects a continuous performance surveillance strategy under PCCP. |

*No specific identifier found in source — verify separately.*

---

### 6. Recommended Risk Controls (per IEC 62304 / ISO 14971)
1. **Algorithm Change Detection**
   - Automated drift detection thresholds with alerts to the quality team.
2. **Pre‑deployment Review Board**
   – Multidisciplinary sign‑off (clinical, cybersecurity, software engineering) before release.
3. **Rollback Capability**
   – Ability to revert to prior validated version if post‑deployment monitoring indicates degradation.
4. **Data Integrity Checks**
   – Input data validation and provenance tracking.
5. **Cybersecurity Safeguards**
   – Secure update channels; digital signatures for each software package.

---

### 7. Human‑Escalation Triggers
| Trigger | Action |
|---------|--------|
| **Change exceeds PCCP limits** (new input modality, new clinical claim) | Escalate to senior RA lead → prepare full 510(k) or De Novo dossier. |
| **Unexpected performance drop (>5% in primary metric)** | Immediate post‑market report → FDA 483/Medical Device Reporting if safety impact suspected. |
| **Adverse event linked to algorithm update** | Initiate recall workflow; file Device Recall (21 CFR 7). |
| **Regulatory guidance update (e.g., new PCCP version)** | Pause releases; re‑align SOPs and submit supplemental information as needed. |

---

### 8. Citations
- FDA **Predetermined Change Control Plan (PCCP) Guidance**, final publication Dec 2024 – referenced in internal SOP `SOP‑AIGOV‑001` (§3, §4).  
- King & Spalding alert “FDA Publishes Final Predetermined Change Control Plan Guidance for AI‑Enabled Device Software Functions” (2024‑12).  
*No specific identifier found in source — verify separately.*

---

### 9. Peer Review Prompt
> **To RA peers:** Please challenge the assumptions above regarding classification, the adequacy of a PCCP‑based 510(k) supplement for algorithm updates, and any jurisdictional gaps—particularly EU MDR implications or state‑level AI regulations that may affect our change‑control strategy.

---

### 10. Reusable RA Judgment (Recorded as final lesson)

**Judgment:**  
When an FDA‑cleared AI‑enabled SaMD intends to use a Predetermined Change Control Plan (PCCP) for software updates, the default regulatory pathway is a **510(k) supplement** covering “Changes to Software Algorithm,” provided the change stays within the predefined scope. Classification remains **Class II** unless new intended uses or risk levels push it to Class III. Required evidence includes full V&V, updated risk analysis (IEC 62304/ISO 14971), and performance re‑validation against baseline data. Any deviation from PCCP limits triggers escalation to a full 510(k) or De Novo submission. Risk controls must address drift detection, rollback capability, and cybersecurity of update distribution.

*(Stored for future reference in RA knowledge base.)*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 146/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,068자 | — |
| 규제 식별자 인용 | 4개 | — |
| source excerpt 근거 일치 | **0/4 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 4개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 862.1`, `21 CFR 7`
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

1. Chunk `126806950873507800`

> > 참고: 사내 자매문서 `03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md` v0.3는 §3에서 "FDA PCCP Guidance 2024" 및 §4 용어표 "PCCP — Predetermined Change Control Plan"로 정확히 최종본을 인용하고 있어, 본 문서만 노후 인용 상태가 단절되어 있다.

2. Chunk `18243842993399443`

> ## Tier 2 (보조 — 범위 가늠용) - King & Spalding alert "FDA Publishes Final Predetermined Change Control Plan Guidance for AI-Enabled Device Software Functions" (2024-12) - Ropes & Gray, McDermott+ 알림(최종본 발행일 2024-12-03 확인용)

### kb-eval-20260718-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "4c8c8b7e4ef63c97", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

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

> **Regulatory Draft – AI‑Enabled SaMD Change Impact Assessment**

---

### 1. Device Classification & Submission Pathway
| Question | Answer |
|----------|--------|
| **Device type** | Software as a Medical Device (SaMD) providing an AI‑enabled diagnostic/clinical decision support function. |
| **Risk class (FDA)** | *Presumed Class II* – most AI‑enabled SaMDs that provide analysis or interpretation of medical data are classified as Class II unless the function is novel or poses higher risk. |
| **Primary submission route** | 510(k) – Substantial equivalence to a predicate device with comparable intended use and algorithmic approach. <br>*If no appropriate predicate exists, pursue a De Novo request.* |
| **PCCP (Pre‑Certification / Pre‑Clearance Change Program)** | Changes that fall within the pre‑approved “scope of change” — as defined in the final “Marketing Submission Recommendations for a PCCP for AI‑Enabled DSF” (2024‑12) — may be implemented without a new 510(k), provided the transformation is limited to the parameters listed in the PCCP agreement. |
| **Regulatory citation** | No specific identifier found in source – verify separately. |

---

### 2. Evidence Required for Submission (or PCCP Change Package)

| Evidence Category | Minimum Content | Rationale |
|-------------------|-----------------|-----------|
| **Intended Use & Indications** | Clear statement aligning with predicate; description of clinical context and patient population. | Drives classification, labeling, and risk analysis. |
| **Algorithm Description** | Block diagram, input‑output specifications, model type (e.g., DL, ML), training architecture, versioning. | Needed for substantial equivalence & transparency. |
| **Data Lineage & Partitioning** | Detailed provenance of training, tuning, testing datasets; split ratios; justification of dataset representativeness. | Supports performance claims and bias analysis (source 1). |
| **Performance Validation** | • Sensitivity/Specificity or other clinically relevant metrics <br>• Statistical confidence intervals <br>• Comparison to predicate performance | Demonstrates safety/effectiveness. |
| **Bias Analysis & Mitigation** | Quantitative assessment of demographic, geographic, device‑type bias; mitigation strategies and residual risk. | Explicit requirement in source (bias analysis·mitigation). |
| **Human–AI Workflow Usability Study** | Human factors testing per IEC 62366‑1/ISO 14971 documenting user interaction, error rates, corrective actions. | Required because workflow includes clinician oversight (source 1). |
| **Cybersecurity & Data Integrity** | Threat analysis, software assurance plan, encryption/authentication controls. | Referenced in broader TPLC recommendations (source 2). |
| **Post‑Market Monitoring Plan** | Real‑world performance tracking, adverse event reporting, periodic re‑validation schedule; alignment with FDA’s “Post‑market Performance Monitoring” guidance for AI/ML SaMD. | Directly listed as a required element (source 1). |
| **Update & Version Control Plan** | Change management process, criteria for triggering new submissions vs. PCCP‐allowed updates, rollback procedures. | Stipulated in “업데이트 계획 시 PCCP” (source 1). |
| **Quality Management System (QMS)** | ISO 13485‑aligned QMS compliant with FDA’s QMSR (effective Feb 2026). | Mandatory for all Class II devices. |

---

### 3. Missing Information / Open Items
1. **Predicate Device Identification** – Exact 510(k) number, classification and decision summary.
2. **Exact Intended Use Statement** – Must be captured verbatim for SE comparison.
3. **Algorithmic Detail Level** – Model architecture, hyper‑parameters, version numbers not disclosed in excerpt.
4. **Training Data Demographics** – Specific breakdown (age, sex, race/ethnicity, disease severity) required for bias analysis.
5. **Performance Benchmark Targets** – Clinical performance thresholds agreed with FDA or derived from predicate.
6. **Human Factors Test Protocol & Results** – Sample size, task scenarios, usability metrics absent.
7. **Cybersecurity Threat Model** – Specific threats identified and mitigations not provided.
8. **Post‑Market Surveillance Metrics** – Defined key performance indicators (KPIs) for ongoing monitoring.

*Action*: Gather the above items before finalizing the 510(k) or PCCP change package.

---

### 4. Risk Controls & Mitigation Strategies
| Hazard | Likelihood/Impact | Existing Control(s) | Additional Recommended Control |
|--------|-------------------|---------------------|--------------------------------|
| **Algorithmic bias leading to diagnostic disparity** | Medium / High (clinical impact) | Bias analysis & mitigation plan (source 1). | Independent external audit of dataset representativeness; periodic re‑bias assessment after each update. |
| **Incorrect output due to software defect** | Low / Critical | Software verification & validation per IEC 62304. | Implement automated regression testing for every new model version. |
| **User misinterpretation of AI recommendation** | Medium / Moderate | Human–AI workflow design; usability study. | Mandatory training module, decision‑support labeling clarifying “output is advisory”. |
| **Cyber attack compromising data integrity** | Low / Critical | Cybersecurity controls (source 2). | Continuous monitoring, intrusion detection system, regular penetration testing. |
| **Post‑market performance drift after model update** | Medium / Moderate | Post‑market monitoring plan (source 1). | Define quantitative “performance trigger” thresholds that necessitate a supplemental 510(k) or PCCP review. |

All controls should be documented in a risk management file compliant with ISO 14971 and cross‑referenced to the QMS.

---

### 5. Human‑Escalation Triggers
| Trigger Event | Required Action |
|---------------|-----------------|
| **Algorithmic change exceeds PCCP‑approved scope** (e.g., new input modality, new clinical indication) | Immediate submission of a supplemental 510(k) or full de novo request; Notify FDA through the “Pre‑Market Submission” portal. |
| **Performance metric falls below pre‑specified threshold** (e.g., sensitivity drops >5 % from baseline) | Pause deployment, issue Field Safety Notice, and submit a Post‑Market Surveillance Report. |
| **New safety signal detected in real‑world use** (adverse event rate above expected) | Initiate FDA MedWatch reporting; convene internal risk review within 48 h. |
| **Significant cybersecurity breach affecting device functionality** | Activate incident response plan, inform FDA via “Medical Device Cybersecurity Incident” portal within 5 working days. |
| **Usability failure observed in clinical setting** (error rate >2 % for critical task) | Suspend use of the SaMD pending root‑cause analysis and corrective action. |

---

### 6. Citations
- No specific identifier found in source – verify separately.

---

### 7. Peer Review Prompt  
*Please review this draft with a focus on:*

1. **Assumptions about classification** – Are we justified in treating the SaMD as Class II based solely on the excerpt? Might there be functional aspects that elevate it to Class III?
2. **Scope of PCCP applicability** – Does the “pre‑approved change scope” truly cover model retraining, or is a new 510(k) required for any algorithmic tweak?
3. **Jurisdictional gaps** – Have we accounted for any upcoming FDA Guidance (e.g., “Proposed Regulatory Framework for Modifications to AI/ML‑Based Software”) that might affect the timing of our submission?
4. **Evidence completeness** – Is any additional data (e.g., real‑world evidence, external validation cohorts) needed beyond what is listed?

---

### 8. Reusable RA Judgment (Memory Outcome)

> *When assessing changes to an FDA‑regulated AI‑enabled SaMD, first confirm whether the modification falls within a pre‑certified change program (PCCP). If it does, only the limited documentation defined by that PCCP (bias analysis, data lineage, post‑market monitoring plan, and update procedures) is required; otherwise, treat the change as a new 510(k) submission. Key evidence includes explicit bias mitigation, human–AI workflow usability testing, cybersecurity controls, and a robust post‑market performance monitoring plan. Missing items that must be collected before any filing are: exact predicate device identifier, complete intended use statement, detailed algorithm architecture, demographic breakdown of training data, and validated performance benchmarks.*  

--- 

*Prepared by:* **Mike – US Regulatory Affairs Specialist**  
*Date:* 2026‑07‑18

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 145/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,640자 | — |
| 규제 식별자 인용 | 4개 | — |
| source excerpt 근거 일치 | **0/4 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 4개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |

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

1. Chunk `1132891599852736913`

> ### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. ---

2. Chunk `135350017850675307`

> ## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로 사전 승인된 변경 범위 운영 | | **AI-Enabled Device Software Functions: Lifecycle Management & Marketing Submission Recommendations** | **초안(Draft)** | 2025-01-06 | ⏸ 초안 유지(FY2026 B-list) | TPLC 전반 설계·제출 권고(투명성·편향·HF·사이버보안) | > 의견수렴: 수명주기 초안은 2025-04-07 코멘트 마감. 이후 확정본 미발표(2026-06 기준). ---

### kb-eval-20260718-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "1056ea3b790075ff", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_01_Device_Description_IFU.md", "source_hash": "70a781477c487e6a94c72d1041f5635cd7fba7f7316962df8815679dc18d5d7c"} -->

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

---

### 1. Bottom‑Line Determination  
| Item | Decision | Rationale |
|------|----------|-----------|
| **Device Classification** | Class II (FDA 510(k) pathway) | The software is described as a “radiographic image acquisition, review and management” tool that *does not* perform primary diagnosis or interpretation. Under 21 CFR 862.2102 (Radiology – X‑ray systems) and FDA guidance on “General/Specific Intended Use,” similar image‐acquisition/manipulation tools are classified as Class II. |
| **Submission Route** | Traditional 510(k) (or Abbreviated if a suitable predicate exists) | The source lists the required documentary elements for a full 510(k). An abbreviated route would be permissible only after confirming an identical predicate with no new intended‑use claims or novel technological characteristics. |

---

### 2. Required Evidence Checklist  

| Category | Required Document / Data | Source Reference |
|----------|---------------------------|------------------|
| **Predicate Device** | Identify a legally marketed device (510(k) number, registration) that is substantially equivalent in function, technology and indications for use. | No specific identifier found in source – verify separately. |
| **Device Description (Section 4.3)** | • High‑level software architecture (modules, processes, DB, DICOM node). <br>• Minimum OS & hardware requirements.<br>• List of compatible detectors/generators with version numbers.<br>• IEC 62304 software safety class determination (A/B/C) and justification.<br>• Statement on SOUP usage (identification, verification, risk mitigations). | Excerpt 4.3 (Chunk 120320733957089094). |
| **Intended Use & Indications** | FDA Form 3881 + narrative in English: “intended for use by trained technologists to acquire, review, and manage digital radiographic images… It is not intended for primary diagnosis or image interpretation.” | Excerpt 4.3. |
| **DICOM Compliance** | Declaration covering Storage SCU, Worklist SCU, MPPS etc.; evidence of conformance testing (e.g., IHE validation reports). | Excerpt 4.3. |
| **Cybersecurity** | Description of authentication, encryption, audit logging; security architecture diagram; any FDA‑recognised risk mitigation (e.g., NIST SP 800‑53 controls). | Excerpt 4.3. |
| **Software Development & Validation** | IEC 62304 life‑cycle documentation, verification/validation test reports, unit and integration testing evidence, traceability matrix linking requirements to tests. | Excerpt 4.3 (IEC 62304 reference). |
| **Risk Management** | ISO 14971 risk analysis file; classification justification; residual risk evaluation; mitigation for any new hazards introduced by the change. | Implicit requirement (general 510(k) and IEC 62304). |
| **Performance Testing** | Bench‑level functional testing showing equivalence to predicate for image acquisition, storage, workflow handling; if any new features, supporting clinical performance data. | Implied under “required evidence” for 510(k). |
| **Labeling & IFU** | Draft labeling, user manual, instructions for use (including intended user/setting, contraindications, warnings). | Required by 21 CFR 807.87; not present in excerpts. |
| **Summary/Statement of Equivalent** | 510(k) Summary per 21 CFR 807.92 and De Novo/Traditional narrative. | Excerpt 1.2 (regulatory references). |

---

### 3. Gaps / Missing Information  

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **Predicate identification** – No predicate device number provided. | Prevents final determination of substantial equivalence; may force a De Novo if none exists. | Conduct market search, document chosen predicate with 510(k) numbers and compare side‑by‑side. |
| **Risk Management File (ISO 14971)** – Not referenced in source. | Required for IEC 62304 class C or any Class II device. | Compile hazard analysis, risk control, residual risk evaluation. |
| **Verification & Validation Evidence** – No test reports cited. | FDA will request performance data to support equivalence. | Produce detailed V&V documentation covering functional, safety and security tests. |
| **Labeling/IFU Drafts** – Absent from excerpt. | 510(k) requires complete labeling package. | Develop drafts and include in submission. |
| **Clinical Performance (if any new claim)** – No data mentioned. | If the change adds a novel function, clinical data may be needed. | Confirm that intended use remains unchanged; otherwise plan appropriate study. |
| **SOUP Inventory** – Only “use or not” is noted, no list. | FDA expects detailed SOUP identification and mitigation. | List each third‑party component (version, license) with verification artifacts. |
| **Cybersecurity Threat Model** – High‑level description only. | May be insufficient for Class II SaMD. | Provide a formal threat analysis (e.g., NIST SP 800‑30 style). |

---

### 4. Risk Controls & Standards Alignment  

| Control | Standard / Guidance | Application |
|---------|---------------------|-------------|
| **Software Safety Classification** | IEC 62304 (Class A/B/C) | Determine class based on potential to cause injury; likely Class B for radiographic image handling, but confirm against hazard analysis. |
| **Cybersecurity** | FDA “Content of Premarket Submissions for Management of Cybersecurity” (2022); NIST SP 800‑53 Rev 5 | Implement authentication, encryption, audit logging; provide patch management plan. |
| **DICOM Compatibility** | IEC 62366‑1 + DICOM PS3.10‑3.13 | Ensure interoperability with existing radiology equipment; include conformance testing results. |
| **Risk Management** | ISO 14971:2019 (updated 2022) | Conduct risk analysis tying software hazards to mitigations (e.g., lockout after failed authentication). |
| **Quality System** | 21 CFR 820 (QSR) plus QMSR (effective Feb 2026, ISO 13485‑aligned) | Document design controls, change management, post‑market surveillance. |

---

### 5. Citations  

- FDA “Electronic Submission Template for Medical Device 510(k) Submissions” (eSTAR v5.x, final 2023).  
- FDA Guidance, **Format for Traditional and Abbreviated 510(k)s** (2019‑09‑13).  
- 21 CFR 807.87 – Information required in a 510(k) submission.  
- 21 CFR 807.92 – 510(k) Summary format.  
- FDA Guidance, **General/Specific Intended Use** (1998 Final, still effective).  
- FDA Form 3881 – Indications for Use.  

*No specific predicate or case identifiers appear in the source excerpts; verify them separately before finalizing the submission.*

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger Level | Reason |
|-----------|----------------|--------|
| **Unidentified Predicate** | Immediate escalation to senior regulatory lead. | Without a clear predicate, clearance pathway is uncertain (possible De Novo). |
| **Software Safety Class C determination** | Escalate to Clinical Affairs & FDA liaison. | Class C may require additional clinical data or PMA route. |
| **New Intended‑Use Claim (diagnostic/interpretation)** | Halt submission; consult product management and legal. | Alters classification to Class III potentially requiring PMA. |
| **Significant Cybersecurity Vulnerability identified during V&V** | Escalate to CISO & Quality Manager. | Must be resolved before filing; may affect risk analysis. |
| **Regulatory Gap in QMSR compliance (post‑Feb 2026)** | Notify quality assurance for corrective action plan. | QMSR is mandatory for all 510(k) submissions after the effective date. |

---

### 7. Peer Review Prompt  

> **To RA Peer:**  
> Please review the assumptions made above, especially:  
> 1. The classification as Class II based solely on the “no‑diagnosis” intended use claim.  
> 2. The completeness of the required evidence list given the change scope (e.g., need for clinical performance data).  
> 3. Potential jurisdictional gaps—are there any FDA guidance updates post‑2023 that could affect cybersecurity or software safety classification not captured here?  
> Provide feedback on any missing regulatory citations, overlooked risk controls, or alternative pathways (e.g., Special 510(k)) that might be applicable.

---

### 8. Reusable RA Judgment (Honcho Record)  

```json
{
  "honcho_conclude": {
    "case_id": "daily_growth_v1_2026-07-18",
    "summary": "SaMD change affecting radiographic image acquisition, review and management is likely Class II under FDA 510(k). Submission should be a Traditional (or Abbreviated if predicate identified) 510(k) with full device description, IEC 62304 classification, DICOM compliance, cybersecurity controls, SOUP inventory, risk management (ISO 14971), verification/validation data, labeling, and a clear predicate reference. Major gaps: no predicate identified, missing risk management file, V&V reports, labeling drafts, detailed SOUP list, and formal cybersecurity threat model. Escalate immediately if predicate cannot be found or intended use expands to diagnosis.",
    "actions_recommended": [
      "Conduct market search for a suitable predicate device and document 510(k) numbers.",
      "Compile ISO 14971 risk management file with hazard analysis tied to IEC 62304 class.",
      "Generate full V&V test reports covering functional, safety, and cybersecurity testing.",
      "Prepare labeling/IFU package per 21 CFR 807.87.",
      "Create detailed SOUP inventory with verification evidence.",
      "Develop formal cybersecurity threat model aligned with FDA guidance."
    ],
    "escalation_conditions": [
      "Absence of a clear predicate (possible De Novo).",
      "Software safety class determined as C.",
      "Any new intended‑use claim for diagnosis or interpretation.",
      "Discovery of critical cybersecurity vulnerabilities during testing."
    ],
    "peer_review_requested": true,
    "confidence": "high"
  }
}
```

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 144/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,922자 | — |
| 규제 식별자 인용 | 8개 | — |
| source excerpt 근거 일치 | **3/8 (37%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 5개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 862.2102`, `21 CFR 820`
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

1. Chunk `117114757705580095`

> ### 1.2 작성 근거 문서 - FDA, "Electronic Submission Template for Medical Device 510(k) Submissions" (최종 2023 개정, eSTAR v5.x 기준) - FDA Guidance, "Format for Traditional and Abbreviated 510(k)s" (2019-09-13 Final) - 21 CFR 807.87 — 510(k) 제출에 요구되는 정보 - 21 CFR 807.92 — 510(k) Summary 포맷 - FDA Guidance, "General/Specific Intended Use" (1998 Final, 현행 유효) - FDA Form 3881 (Indications for Use 전용 양식)

2. Chunk `120320733957089094`

> ### 4.3 촬영실 GUI SW (영상 획득·검사 제어 SW) - Device Description 포함 항목 - SW 아키텍처 요약(모듈·프로세스·DB·DICOM 노드) - 운영체제·하드웨어 최소 요구사항 - 호환 Detector·Generator 리스트(버전 포함) - DICOM 적합성 선언서 요약(Storage SCU, Worklist SCU, MPPS 등) - 사이버보안 특징(인증·암호화·감사 로그) - IEC 62304 SW 안전 등급(Class A/B/C) - SOUP 사용 여부·식별 정보 - Indications for Use 예시(영문) - "The [Model] software is intended for use by trained technologists to acquire, review, and manage digital radiographic images generated by compatible X-ray acquisition devices in medical facilities. It is not intended for primary diagnosis or for image interpretation." - 주의 - "Review"와 "diagnosis" 용어 구분 — 진단용 주장 시 classification 상...

### kb-eval-20260718-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "b52524355e284be8", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_04_Cybersecurity_Section.md", "source_hash": "7e58648f9843123aadf78873963b41b7b570e437b03bea2490613c3fcc407503"} -->

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

> **Regulatory Impact Assessment – SaMD Cybersecurity Change (FDA 510(k) Pathway)**  

---

### 1. Classification & Submission Route
| Element | Determination |
|---|---|
| **Device type** | Software‑only Medical Device (SaMD). |
| **Regulatory class** | **Class II** – most SaMDs fall under 21 CFR 862/868 with a predicate device, unless the software performs a “novel” function that would push it to Class III. |
| **Primary submission** | **Traditional 510(k)** (or **Special 510(k)** if the change is a software update to an already cleared device). |
| **Supporting regulations** | - Section 524B of the FD&C Act – cybersecurity obligations, including SBOM requirement【1】.<br>- QMSR (effective Feb 2026) – ISO‑13485–aligned quality system.<br>- IEC 81001‑5‑1 & NIST CSF as referenced standards for risk management. |

> **Note:** No specific predicate or 510(k) identifier appears in the source excerpts; verify predicate device number independently.

---

### 2. Required Evidence Package (What must be submitted)

| Requirement | Evidence Needed | Source |
|---|---|---|
| **SBOM (Software Bill of Materials)** | Complete, machine‑readable SBOM covering all manufacturer‑developed and third‑party components; format SPDX 2.3+ or CycloneDX 1.5+. Must include fields listed in Table (Supplier Name, Component Name, Version, Unique Identifier, Dependency Relationship, Author, Timestamp). | 【2】 |
| **Threat Model** | Documented threat model (STRIDE recommended) showing identified threats, attack vectors, and mitigations for each software component. | 【1】 |
| **Cybersecurity Management Plan / VMP (Vulnerability Management & Post‑Market Surveillance)** | CMP/VMP describing: <br>• Patch development & deployment schedule<br>• Continuous monitoring strategy (post‑market vulnerability monitoring, CVD updates)<br>• Incident response workflow<br>• Criteria for software version release. | 【1】 |
| **Penetration Testing** | Summary of third‑party penetration test report (recommended, not mandatory). Include scope, methodology, findings, and remediation actions. | 【1】 |
| **Standards Conformance** | Evidence of adherence to IEC 81001‑5‑1 and NIST CSF (e.g., gap analysis, implementation artifacts). | 【1】 |
| **Risk Management File (ISO 14971)** | Updated risk analysis incorporating new cyber threats; residual risk evaluation; verification/validation results for any functional changes introduced by the update. | General FDA expectation (21 CFR 820.30) |
| **Labeling & IFU Updates** | Revised labeling reflecting any change in intended use, warnings, or user instructions related to cybersecurity. | 510(k) Guidance |

---

### 3. Missing / Outstanding Information (To be supplied before filing)

1. **Exact Intended Use Statement** – needed to confirm classification and predicate alignment.  
2. **Predicate Device Identification** – 510(k) number, device name, and comparison matrix.  
3. **Scope of Software Change** – is this a *major* functional change or a *maintenance* update? (Determines whether a Traditional vs. Special 510(k) applies.)  
4. **Full SBOM Export** – the excerpt shows required fields; the complete file must be attached.  
5. **Pen Test Report** – while only recommended, FDA may request it for higher‑risk SaMDs.  
6. **Post‑Market Cyber Surveillance Plan Details** – frequency of vulnerability scans, responsible parties, and reporting timelines.  
7. **Evidence of QMSR compliance** – SOPs, training records, and internal audit results that address new cyber controls.  

---

### 4. Risk Controls & Mitigations (Cybersecurity‑focused)

| Control | Description | Reference |
|---|---|---|
| **SBOM Generation & Maintenance** | Automated generation of SPDX/CycloneDX SBOM for every software build; version control linking to release notes. | 【2】 |
| **Threat Modeling (STRIDE)** | Conduct at design phase and re‑evaluate on each major update. Document mitigations per threat category. | 【1】 |
| **Vulnerability Management Policy** | Define CVE severity thresholds, patch timelines (<30 days for Critical/High), and a “break‑glass” process for emergency patches. | 【1】 |
| **Secure Development Lifecycle (SDL)** | Apply NIST CSF Identify‑Protect‑Detect‑Respond‑Recover functions; code reviews, static analysis, dependency checking. | 【1】 |
| **Penetration Testing** | Annual or per‑release external testing; remediate findings before market release. | 【1】 |
| **Post‑Market Monitoring (CVD & Patch Deployment)** | Continuous monitoring of public vulnerability databases; integration with device firmware update mechanism. | 【1】 |
| **User Authentication & Access Controls** | Role‑based access to configuration settings; enforce strong password/2FA where applicable. | General best practice, referenced by IEC 81001‑5‑1 |

---

### 5. Key Citations

- **Section 524B(b)(3) – SBOM legal obligation** (FDA 2024 Guidance).  
- **Table of requirements comparison (FDA vs EU MDR vs MFDS)** showing mandatory items for FDA: SBOM, Threat Model, CMP/VMP, Post‑Market updates【1】.  
- **SBOM field definitions & format guidance (NTIA Minimum Elements, SPDX/CycloneDX)**【2】.

> *No specific 510(k) predicate number or case ID appears in the source excerpts; verify those identifiers separately.*

---

### 6. Human‑Escalation Triggers (When to Notify senior RA / Management)

| Trigger | Action |
|---|---|
| **Critical vulnerability discovered** (CVSS ≥ 9.0) that impacts a released version and cannot be patched within 30 days. | Immediate escalation to product security lead & senior RA; consider emergency FDA notification (Section 520(h)(2)). |
| **Inability to produce a complete SBOM** for any component used in the device. | Pause submission; engage engineering to generate missing data; senior RA review required. |
| **Change re‑classifies the device to Class III** after risk analysis. | Escalate to leadership for decision on PMA pathway vs. 510(k) withdrawal. |
| **Regulatory deadline missed** (e.g., FDA’s “post‑market cyber update” compliance date). | Notify regulatory manager; develop remediation plan and possibly request a meeting with FDA. |
| **Discrepancy between FDA required controls and internal QMSR evidence**. | Senior quality/Risk Management review before filing. |

---

### 7. Peer Review Prompt

> *@RA‑Peer: Please challenge the assumptions made above regarding (a) classification determination without seeing the full intended use, (b) reliance on a “Special 510(k)” versus a Traditional submission for this cybersecurity update, and (c) coverage of jurisdiction‑specific gaps such as FDA’s upcoming 2025 Cybersecurity Guidance. Identify any missing regulatory citations or evidence items that could jeopardize clearance.*  

---

### 8. Reusable RA Judgment (Lesson Learned)

**Judgment:** When a SaMD undergoes a cybersecurity‑related software update, the **mandatory SBOM per Section 524B(b)(3)** and a **formal threat model** are now core components of any FDA 510(k) submission. Absence of a complete SBOM or an up‑to‑date CMP/VMP should trigger a *submission hold* until these artifacts are supplied. Aligning the cybersecurity controls with IEC 81001‑5‑1 and NIST CSF not only satisfies FDA expectations but also facilitates harmonization with EU MDR and MFDS requirements, reducing future rework.  

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 143/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,335자 | — |
| 규제 식별자 인용 | 4개 | — |
| source excerpt 근거 일치 | **1/4 (25%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 3개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 862`, `21 CFR 820.30`
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

1. Chunk `129799210478830618`

> ## 5. 3개 지역 비교 (FDA vs MDR vs MFDS) | 요구사항 | FDA (524B + 2025 Guidance) | EU MDR (MDCG 2019-16) | MFDS (2025.01 가이드라인) | |---|---|---|---| | **법적 근거** | Section 524B, FD&C Act | GSPR Annex I §14·17·18 | 디지털의료제품법·사이버보안 가이드라인 | | **SBOM** | 법적 의무 (524B(b)(3)) | 강력 권고 | 권고 (제출 자료 포함) | | **Threat Model** | 필수 (STRIDE 권장) | 필수 (MDCG 2019-16) | 필수 | | **CMP/VMP** | 필수 | PMS 계획에 포함 | 업데이트 정책으로 요구 | | **Pen Test** | 권고 | 권고 | 권고 | | **표준 참조** | IEC 81001-5-1, NIST CSF | IEC 81001-5-1 (조화표준 진행) | IEC 81001-5-1, MFDS 자체 가이드 | | **포스트마켓** | 법적 의무 (패치, CVD, 모니터링) | PMS + Vigilance 연계 | 이상사례 보고 + 업데이트 절차 | > MDR/MFDS 영향: GUI SW의 경우 FDA 요건 충족 수준으로 작성하면...

2. Chunk `135977185938899780`

> ### 3.4 SBOM (Software Bill of Materials) **법적 의무** (Section 524B(b)(3)). **NTIA Minimum Elements** (FDA 준용): | 필드 | 설명 | 예시 | |---|---|---| | Supplier Name | SW 공급자 | OpenJDK Foundation | | Component Name | 컴포넌트 명칭 | OpenJDK | | Version | 버전 문자열 | 17.0.9 | | Unique Identifier | CPE 또는 PURL | `pkg:maven/org.openjdk/jdk@17.0.9` | | Dependency Relationship | 의존성 관계 | DependsOn: spring-boot@3.2.0 | | Author of SBOM | SBOM 작성자 | [제조사명] | | Timestamp | 생성일시 ISO 8601 | 2026-04-29T00:00:00Z | **형식**: SPDX 2.3+ 또는 CycloneDX 1.5+ (machine-readable JSON/XML 권장) **포함 범위**: - Manufacturer-developed SW (자체 개발) - Third-party commercial/licensed SW - Ope...

## ra_eu

### kb-eval-20260718-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a0fc3d166809748d", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

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

> **Regulatory Draft – Preliminary Technical Documentation Assessment (MDR 2017/745)**  

---

### 1. Classification & Conformity‑Assessment Route  
| Decision point | Required information | Evidence needed to close the gap | MDR reference |
|----------------|----------------------|----------------------------------|---------------|
| **Intended purpose / mode of action** | Precise statement of what the device does (diagnostic, therapeutic, monitoring, software‑only, etc.) and its principal intended use. | Device description document (see §1 Device Description in Annex II). | Annex II – §1 |
| **Classification rule** | Identification of the applicable rule(s) from Annex VIII (e.g., Rule 9, 10, 11, 17, or other rules). | Classification justification matrix linking intended purpose to the specific rule number. | Annex VIII |
| **Resulting class** | Class I, IIa, IIb or III derived from the rule. | None – outcome of the above step. | Annex VIII |
| **Conformity‑assessment route** (Annex IX, X or XI) | • If Class IIa/IIb/III → NB involvement required (Annex IX for full QMS & TD assessment, Annex X for type‑examination, Annex XI for production‑conformity). <br>• Class I (non‑sterile, non‑measuring) can use self‑declaration. | Declaration of Conformity draft indicating the chosen route; evidence that the NB’s scope covers the selected annex. | Annex IX / X / XI |

*Because the device’s intended purpose and mode of action are not supplied in the source material, **classification cannot be finalised** at this stage.*  

---

### 2. Required Evidence (Technical Documentation – Annex II)  

| Annex II Section | Content to be provided | Typical artefacts (examples) | Source citation |
|-------------------|------------------------|------------------------------|-----------------|
| **§1 Device Description** | • Trade name, model, catalogue number<br>• Detailed description of the device, accessories, intended purpose, and principle of operation. | Design Output – Device Description (DHF). | [1] |
| **§2 Labeling & IFU** | • Labels, packaging artwork, user‑manual/Instructions for Use (IFU) in required languages.<br>• Conformity‑marked CE logo, UDI, and any required warnings. | Device Labeling (21 CFR 801 / eSTAR §6). | [1] |
| **§3 Design & Manufacturing** | • Summary of design processes, manufacturing methods, materials, and critical specifications.<br>• Supplier list and purchased‑part specifications where relevant. | Design History File (§7.3 QMSR) – structure/material/manufacturing method. | [1] |
| **§4 GSPR Checklist** | • Mapping of each General Safety & Performance Requirement (Annex I) to supporting evidence (clinical data, bench testing, literature). | 510(k) Summary & performance test results (where applicable). | [1] |
| **§5 Risk Management** | • Fully documented risk management file (ISO 14971) covering risk analysis, evaluation, control measures and residual risks. | ISO 14971‑compliant Risk Management File (explicitly required). | [1] |
| **§6 Verification & Validation** | • Results of verification (e.g., design output meets input) and validation (clinical/bench performance in intended use environment). | V&V Reports, clinical validation data, biocompatibility test reports. | [1] |

*The source excerpt also notes that the same sections are required for all MDR‑applicable devices from Class I through III*【2】.  

---

### 3. Missing Information – Gap Analysis  

| Area | What is missing | Why it matters (Regulatory impact) |
|------|----------------|-------------------------------------|
| **Intended purpose & Mode of Action** | No statement in the excerpt. | Determines classification rule (Annex VIII) and triggers specific clinical‑evaluation requirements (Annex XIV). |
| **Classification Rule & Class** | Not identified. | Directly selects the conformity‑assessment route (Annex IX/X/XI) and NB involvement level. |
| **Clinical Evidence / Evaluation Report** | No reference to a Clinical Evaluation Report (CER) or PMS plan. | Required for all devices (Annex XIV Part A) – without it, NB will request full clinical data. |
| **Post‑Market Surveillance (PMS) Plan & Reports** | Not mentioned. | Mandatory under Art. 83–86; especially critical for Class IIa/IIb/III. |
| **Declaration of Conformity (DoC)** | Draft not supplied. | Required to prove conformity before CE marking (Annex IV). |
| **Language & Labeling Details** | Only “minimum English required”; no list of target EU languages. | NB checks that all required language versions are provided (Annex II §2). |
| **Unique Device Identification (UDI) Strategy** | No mention. | UDI registration in EUDAMED is mandatory for Class I‑III (Art. 27–31). |
| **Manufacturer’s QMS Certificate** | Absent. | Needed to demonstrate ISO 13485 compliance; prerequisite for NB assessment (Annex IX). |

---

### 4. Risk Controls – Expected Content  

1. **Risk Management Process (ISO 14971)** – documented, covering hazard identification, risk analysis, evaluation, control, and residual‑risk acceptance (source [1] §5).  
2. **Control Measures** aligned with each identified GSPR (Annex I) – e.g., design safeguards, protective labeling, user training, software validation.  
3. **Verification of Controls** – evidence that risk controls are effective (verification & validation reports, source [1] §6).  
4. **Post‑Market Risk Evaluation** – systematic collection of real‑world performance data (PMS plan) to detect emerging risks (Art. 83/84).  

---

### 5. Human‑Escalation Triggers  

| Trigger | Action Required | Responsible Role |
|--------|-----------------|------------------|
| **Unclear intended purpose / mode of action** | Pause TD preparation; request detailed use‑case from product team. | RA Lead → Product Manager |
| **Classification cannot be assigned after rule analysis** | Convene cross‑functional classification workshop (RA, Clinical, Engineering). | RA Lead |
| **Missing clinical evidence for Class IIa/IIb/III** | Initiate or update Clinical Evaluation Report; consider PMS data collection / PMCF study. | Clinical Affairs Lead |
> **Escalation point:** If any of the above items remain unresolved 2 weeks after the request, elevate to the Regulatory Steering Committee (RA Director).  

---

### 6. Citations  

| Item | Source |
|------|--------|
| Device description, labeling, design & manufacturing, GSPR checklist, risk management, verification & validation requirements – MDR Annex II structure | [1] |
| Applicability of Annex II to all classes (I‑III) and related annexes (I, XIV, XV, III) | [2] |

> **Identifier note:** No specific 510(k) or predicate identifiers appear in the provided excerpts; therefore no identifier is listed.  

---

### 7. Peer‑Review Prompt  

*“@RA‑Colleague, please review this preliminary assessment and challenge:*

1. *Are we assuming any classification rule without sufficient evidence from the device’s intended purpose?*  
2. *Does the mapping of GSPR to the required artifacts fully reflect the scope of Annex II, or are additional sub‑sections (e.g., software lifecycle documentation for Rule 11 devices) missing?*  
3. *Are there any jurisdictional gaps—particularly concerning UDI and language requirements—that we have not captured for a full EU submission?”  

--- 

**End of Draft – ready for human validation and next‑step planning.**

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 157/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,393자 | — |
| 규제 식별자 인용 | 13개 | — |
| source excerpt 근거 일치 | **7/13 (53%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 6개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art. 27`
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

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

### kb-eval-20260718-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2f66967eda81b3ef", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

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

> **Regulatory Draft – Response to Notified‑Body Deficiency Letter (MDR)**  

---

### 1. Device Synopsis  
| Item | Description |
|------|-------------|
| **Device type** | X‑ray diagnostic radiology system (includes generator, detector and image‑processing software). |
| **Intended use** | Imaging of patients for standard diagnostic radiology procedures. |
| **Key performance claim** | Detective quantum efficiency at zero spatial frequency DQE(0) ≥ 65 % (IEC 62220‑1‐1). |

*Source:* Clinical equivalence data quoted in the NB request (DQE ≥ 65 %) and referenced test report TR‑2024‑015 (Excerpt [1]).

---

### 2. Classification & Conformity‑Assessment Route  

| Aspect | Determination |
|--------|---------------|
| **MDR classification rule** | **Rule 10, Annex VIII** – active device for diagnostic imaging that emits ionising radiation. |
| **Resulting class** | **Class IIb** (the X‑ray generator is the highest‑risk element). |
| **Conformity‑assessment route** | **Annex IX** – full assessment of the Quality Management System *and* Technical Documentation by a Notified Body. |

> **Citation:** Rule 10, Annex VIII (MDR 2017/745) – classification of active radiological devices.  

---

### 3. Evidence Required under MDR  

| Requirement | Minimum documentation/evidence | MDR reference |
|-------------|--------------------------------|----------------|
| **Technical Documentation** (design, manufacturing, labeling, etc.) | Complete Annex II dossier (including device description, specifications, design files, verification & validation data). | Annex II |
| **Clinical Evaluation Report (CER)** | Updated CER demonstrating clinical equivalence to the predicate device; include performance test report (TR‑2024‑015) and DQE data; attach revised CER Rev.3 as Annex A. | Annex XIV Part A; Art. 61 |
| **Risk Management** | ISO 14971‑compliant risk analysis, with specific controls for radiation dose, beam quality, safety interlocks, and software decision support. | Annex I (GSPR) & ISO 14971 |
| **Post‑Market Surveillance (PMS)** | PMS plan (Art. 84) + periodic safety update report (PSUR) (Art. 86) appropriate for Class IIb. |
| **Usability / Human Factors** | IEC 62366‑1 evidence that user interface (software, controls) does not introduce use‑related hazards. |
| **Labeling & IFU** | Conformity with Annex I §23 – warnings, contraindications, radiation protection statements. |
| **QMS Evidence** | ISO 13485:2016 certification; any non‑conformities (NCs) raised by the NB must be closed with corrective actions. |

*Specific items already provided:* Test Report TR‑2024‑015 (IEC 62220‑1‑1) and revised CER Rev.3 (Annex A) – see Excerpt [1].

---

### 4. Gaps Highlighted in the Deficiency Letter  

| NB‑identified gap | What is missing / insufficient | Impact on conformity |
|-------------------|--------------------------------|----------------------|
| **Clinical Evaluation (CER)** | The NB flagged incomplete justification of clinical equivalence – only DQE(0) ≥ 65 % shown; no data across all clinical modes, nor statistical analysis against the predicate. | Lack of robust CER (Annex XIV Part A). |
| **Technical Documentation (TD)** | Certain design verification reports for the detector module and software algorithm are absent; labeling draft missing radiation‑protection statements. | Incomplete Annex II dossier – risk of non‑acceptance. |
| **QMS Non‑Conformities** | Outstanding NCs from previous audits not yet closed; corrective‑action records incomplete. | NB cannot issue conformity assessment (Annex IX). |
| **Post‑Market Surveillance (PMS) Plan** | No documented PMCF (post‑market clinical follow‑up) strategy for long‑term dose monitoring. | Deficiency under Art. 84/86, may affect PSUR. |

*Source of procedural context:* Table comparing NB processes and “주요 결함 유형” (major deficiency types: CER, TD, QMS NC, Labelling…) – Excerpt [2].

---

### 5. Proposed remedial actions  

| Action | Deliverable | Deadline (relative to NB clock‑stop) |
|--------|-------------|--------------------------------------|
| **Complete Clinical Equivalence Dossier** | • Expand performance data set (DQE across all kV settings, exposure modes). <br>• Statistical comparison with predicate device. <br>• Update CER narrative and attach as Annex A. | Within 20 working days of NB clock‑stop. |
| **Supply Missing Design & Verification Reports** | • Detector module validation report (IEC 60601‑2‑33).<br>• Software verification & validation summary (IEC 62304). | 25 working days. |
| **Finalize Labeling & IFU** | Revised labeling package showing radiation safety warnings, contraindications, and IEC 60601‑1 compliance statements. | 15 working days. |
| **Close QMS NCs** | • Updated corrective‑action reports for each outstanding NC.<br>• Evidence of implementation (audit trails). | 30 working days. |
| **Develop PMCF Plan** | Detailed plan covering annual dose monitoring, patient follow‑up data collection, and risk‑based sampling; align with Art. 84 & Annex XIV Part B. | 35 working days (to be submitted before PSUR deadline). |

All documents will be uploaded via the NB’s electronic portal, referencing the same version numbers as used in the deficiency letter.

---

### 6. Risk Controls Summary  

| Hazard | Control(s) | MDR reference |
|--------|------------|----------------|
| **Excessive patient radiation dose** | – Beam‑output monitoring interlock.<br>– Automatic exposure control (AEC).<br>– Dose‑area product (DAP) display with alerts. | Annex I GSPR 5, 6; ISO 14971 risk controls. |
| **Software decision error** | – IEC 62304 validated development lifecycle.<br>– Independent verification of diagnostic output.<br>– User training & IFU warnings. | Rule 11 (Annex VIII) for software impact; Annex I GSPR 12. |
| **Electrical safety / X‑ray leakage** | – Compliance with IEC 60601‑1 and IEC 60601‑2‑33 electromagnetic compatibility tests.<br>– Periodic preventive maintenance schedule. | Annex I GSPR 4, 9. |

---

### 7. Escalation Triggers (Human‑escalation points)  

| Trigger | Action |
|---------|--------|
| **NB deadline missed** (no response within the agreed clock‑stop + 5 days) | Senior RA manager alerts the Project Lead; consider formal extension request under Art. 7 of Regulation 2026/977. |
| **More than 4 clock‑stops requested** (per NB policy in Excerpt [2]) | Escalate to Head of Regulatory Affairs for senior management involvement and possible re‑evaluation of go‑to‑market timeline. |
| **New safety‑critical NC identified during QMS audit** | Immediate risk assessment; potential suspension of CE‑marking process until mitigation verified. |
| **NB issues a “non‑approval” notice** (failure to address CER/TD) | Trigger crisis response: convene cross‑functional team, prepare remedial action plan, assess impact on market launch and consider redesign if required. |

---

### 8. Peer‑Review Prompt  

> *Colleague,* please review the assumptions and coverage in this draft:  
> - Are the identified classification (Rule 10, Class IIb) and Annex IX route definitively applicable to the whole system, or should a component‑based approach (generator = IIb, detector = IIa, software = IIa/III) be justified with additional evidence?  
> - Does the listed clinical equivalence data (DQE ≥ 65 % only) meet MDR expectations for “equivalent clinical performance”, or should we also provide patient‑outcome data?  
> - Are there any jurisdiction‑specific nuances in the MDR amendment **2026/977** that might affect the clock‑stop handling or documentation format not captured here?  
> - Identify any gaps in our PMS/PMCF plan relative to Art. 84/86 for a diagnostic radiology device.  

Your feedback will be incorporated before final submission to the Notified Body.  



--- 

*Prepared by:* Theo – EU MDR Regulatory Affairs Specialist  
*Date:* 2026‑07‑18 (run ID: daily_growth_v1)  

**Note:** No specific regulator or case identifiers were present in the source excerpts; all references are derived from the provided material and MDR text.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 156/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,076자 | — |
| 규제 식별자 인용 | 15개 | — |
| source excerpt 근거 일치 | **2/15 (13%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 13개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
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

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1014893419282866507`

> | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter | 보완 요청 | Additional Information (AI) Request | | 근거 법령 | MDR Annex VII + 2026/977 | 의료기기법 §12 + 허가·신고·심사 규정 | 21 CFR 807 + FDA Review Policy | | 답변 기한 | NB와 합의 (법정 상한 없음) | 1차 60일, 2차 60일 | 180일 (타임라인 기산일부터) | | 최대 중단 횟수 | 4회 (product verification 기준) | 2차까지 (실질 2회) | 제한 없음 (Interactive Review 가능) | | Clock-stop | 예 (NB 요청 당일 stop, 제출 익일 resume) | 예 (보완 기간 제외) | 예 (AI 발송일부터 stop) | | 미응답 시 | 평가 종료 / 불승인 | 취하 간주 | 허가 거부 | | 사전 대화 창구 | Structured Dialogue (Art.7, 2026/977) | 상담제도 (비공식) | Pre-Sub (Q-Sub) (공식, 문서화) | | 주요 결함 유형 | CER, TD, QMS NC, Labelin...

### kb-eval-20260718-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "3c793b286540204c", "source": "github:holee9/MD-process/issue-drafts/943_AUDIT_CHK-DR-001_EU_MDR_Rule_5_9_X선_분류_사실오류.md", "source_hash": "8354553d723c03ea5389ea12fbe6629ab639705bcafe3dd7a3ec1381dd8206f8"} -->

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

> **Regulatory Draft – Classification & Conformity‑Assessment of a Diagnostic X‑ray System**

---

### 1. Issue Summary  
A reference table used in internal documentation incorrectly maps a *diagnostic* X‑ray system to **EU MDR Rule 5/9 → Class IIa/IIb** (see source [2]). The same table also groups the digital flat‑panel detector with the X‑ray generator under one rule. This mis‑classification propagates to the choice of conformity‑assessment route, technical‑documentation requirements and post‑market surveillance obligations.

---

### 2. Applicable Regulation & Classification Rules  

| Component | Intended Use (as clarified) | MDR Rule (Annex VIII) | Resulting Class |
|-----------|-----------------------------|----------------------|-----------------|
| X‑ray generator (emits ionising radiation for **diagnostic** imaging) | Diagnostic radiology – image acquisition only | **Rule 10** (active devices for diagnosis/monitoring; emits ionising radiation) | **Class IIb** |
| Digital flat‑panel detector (records the diagnostic image) | Image recording device | **Rule 17** (devices intended specifically for recording diagnostic images generated by X‑ray radiation) | **Class IIa** |
| Software that processes the image and provides diagnostic information | Diagnostic decision support | **Rule 11** (software providing information for diagnostic decisions) – typically Class IIa, may rise to IIb/III if decision impact is critical. | **Class IIa** (assumed) |

> **Citation:** Rule 9 description in source [1] confirms that *therapeutic* active devices are classified under Rule 9 and are excluded from diagnostic X‑ray classification. Source [2] explicitly states the correct mapping: “X‑ray system (diagnostic ionising‑radiation active device) = **Rule 10 → Class IIb**; digital flat‑panel detector = **Rule 17 → Class IIa**.”

---

### 3. Determination of Conformity‑Assessment Route  

| Device | Classification | MDR Annex for conformity assessment |
|--------|----------------|--------------------------------------|
| X‑ray generator (Class IIb) | Class IIb | **Annex IX** – Full quality‑management system audit + technical documentation review by the Notified Body. |
| Flat‑panel detector (Class IIa) | Class IIa | **Annex IX** (or Annex X if a type‑examination is preferred). The NB must assess the technical file and QMS; a full ISO 13485 audit may be optional but recommended for consistency across the system. |
| Diagnostic software (assumed Class IIa) | Class IIa | **Annex IX** or **Annex X**, depending on manufacturer strategy. |

*The whole X‑ray system is treated as a **compound device**; the highest class (IIb) governs the overall conformity‑assessment route, i.e., Annex IX.*

---

### 4. Required Technical Documentation & Evidence  

| Requirement | What Must Be Provided |
|-------------|-----------------------|
| **Technical documentation** – Annex II | Device description, intended use, risk management file, design verification/validation, software lifecycle evidence (IEC 62304), manufacturing information, labeling. |
| **Clinical Evaluation Report (CER)** – Annex XIV Part A | State‑of‑the‑art literature on diagnostic X‑ray systems, clinical data (bench, pre‑clinical, post‑market), justification of safety & performance. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan** – Annex XIV Part B | Specific to the Class IIb generator; includes surveillance of radiation dose, image quality and adverse events. |
| **Periodic Safety Update Report (PSUR)** – Art 86 | Required for Class IIb devices; at least annually for the first three years, then every two years. |
| **Risk Management File** – ISO 14971 & Annex I GSPR | Hazard analysis, risk evaluation, mitigation measures (e.g., dose‑monitoring, interlocks), residual risk assessment, post‑market risk controls. |
| **Software Documentation** – IEC 62304 + Annex IX/X evidence | Architecture, verification/validation, cybersecurity, usability testing. |
| **Declaration of Conformity** – Annex IV | Signed by the manufacturer after NB issuance of certificate. |
| **EUDAMED registration** – Art 33‑39 | Device entry, UDI, certificates, clinical investigation summary (if any). |

---

### 5. Identified Gaps / Missing Information  

1. **Explicit Intended‑Use Statement** – The current documentation mixes therapeutic and diagnostic terminology. A clear statement that the X‑ray generator is *diagnostic only* is required to justify Rule 10.  
2. **Component‑Level Classification Evidence** – Separate technical files (or annexes) for the detector (Rule 17) and software (Rule 11) are missing; their risk classifications must be demonstrated.  
3. **Clinical Data Scope** – No clinical evidence specific to diagnostic X‑ray dose optimisation or image quality is referenced. A systematic literature review and, where feasible, a small‑scale clinical investigation are needed.  
4. **PMCF Plan for the Generator** – The current PMCF plan only covers the detector; it must be extended to cover radiation safety, dose monitoring and long‑term performance of the generator.  
5. **Risk Controls Specific to Ionising Radiation** – Evidence that the device meets IEC 60601‑2‑44 (X‑ray equipment) and implements ALARA principles is not documented.  
6. **Software Validation for Diagnostic Decision Support** – No evidence that software classification under Rule 11 has been justified (e.g., impact analysis of diagnostic decisions).  

---

### 6. Recommended Risk Controls  

| Hazard | Control (reference to standards / GSPR) |
|--------|------------------------------------------|
| Unintended therapeutic radiation exposure | Interlock system, dose‑limiting circuitry, IEC 60601‑2‑44 compliance, user training. |
| Excessive cumulative dose to patient/operator | Integrated dose‑monitoring with alerts; periodic calibration (IEC 60601‑2‑44). |
| Image quality degradation leading to misdiagnosis | Automatic exposure control, routine performance checks per IEC 62471, validation of image processing algorithms (IEC 62304 + IEC 62262). |
| Software‑induced diagnostic error | Verification/validation against IEC 62304; usability testing (IEC 62366); cybersecurity safeguards (ISO 27001/ IEC 62443). |
| Device failure during use | Redundant safety checks, Failure Mode and Effects Analysis (FMEA) documented in risk management file. |

---

### 7. Human‑Escalation Triggers  

| Trigger | Action Required | Responsible Party |
|---------|-----------------|--------------------|
| Ambiguity in intended‑use wording (therapeutic vs diagnostic) | Pause submission; obtain definitive manufacturer statement and update labeling. | RA Lead + Product Owner |
| Missing clinical evidence for diagnostic performance | Initiate literature review or small‑scale clinical study before NB audit. | Clinical Evaluation Team |
| Incomplete PMCF plan for the X‑ray generator | Draft and submit revised PMCF plan to Notified Body; defer certification until accepted. | Post‑Market Surveillance Lead |
| Absence of IEC 60601‑2‑44 compliance evidence | Request test reports from supplier or conduct in‑house verification. | Design & Verification Engineer |
| Discrepancy between component classifications (detector vs generator) | Align technical files; ensure NB evaluates the highest class (IIb) for whole system. | RA Documentation Coordinator |
| Any request from Notified Body for additional data beyond what is provided | Escalate to senior regulatory manager; allocate resources for rapid evidence generation. | Regulatory Manager |

---

### 8. Citations  

* **Rule 9 (Therapeutic active devices)** – source [1]  
* **Correct classification of diagnostic X‑ray system** – source [2] (Rule 10 → Class IIb, Rule 17 → Class IIa)  
* **MDR Annex VIII – Classification rules** – MDR 2017/745, Annex VIII.  
* **Conformity‑assessment routes** – MDR Annex IX (full QMS + technical file audit).  
* **Clinical evaluation requirement** – MDR Annex XIV Part A, Art 61.  
* **PMCF & PSUR requirements** – MDR Art 84–86.  
* **Risk management** – MDR Annex I, ISO 14971.  

> *No specific identifier (e.g., 510(k) number or predicate device) appears in the source excerpts; therefore none is listed.*

---

### 9. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made above regarding (a) the exclusive diagnostic intended use of the X‑ray generator, (b) the applicability of Rule 10 versus any hybrid classification that might arise from combined therapeutic/diagnostic functions, and (c) whether the suggested evidence package fully satisfies the Notified Body’s expectations for a Class IIb active device under Annex IX. Highlight any jurisdiction‑specific gaps (e.g., Korean MFDS or FDA cross‑reference implications) that may affect our CE‑marking strategy.

---

### 10. Reusable RA Judgment (Lesson Record)

**Judgment ID:** LA‑2026‑07‑18‑X‑Ray‑Classification  
**Core Finding:** Diagnostic X‑ray systems emitting ionising radiation belong to **MDR Rule 10 → Class IIb**, not Rule 9 or Rule 5/9 as sometimes mapped from non‑EU classification tables. Digital detectors are classified under **Rule 17 → Class IIa**. Mis‑application of rules leads to an incorrect conformity‑assessment route (Annex IX vs. Annex X/XI) and downstream documentation gaps.  

**Actionable Guidance:**  
1. Verify the *intended use* wording for every component; separate therapeutic from diagnostic functions.  
2. Align internal classification tables with MDR Annex VIII rules before they are propagated to GSPR mapping, technical‑documentation templates, or CE‑marking plans.  
3. For compound devices, adopt the highest class (IIb) as the governing route and ensure all subordinate component files reference their appropriate rule/class.  

*Recorded for future reference in the RA knowledge base.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 155/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,855자 | — |
| 규제 식별자 인용 | 20개 | — |
| source excerpt 근거 일치 | **2/20 (10%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 18개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `Annex II` | MDR Annex II | Technical documentation |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Art 33` | MDR Article 33 | European database on medical devices (Eudamed) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `Art 61` | MDR Article 61 | Clinical evaluation |
| `Art 84` | MDR Article 84 | Post-market surveillance plan |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `IEC 62471`, `IEC 62262`, `ISO 27001`, `IEC 62443`
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

### kb-eval-20260718-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "e43c897461f950f2", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md", "source_hash": "96ff2d334aa377f194a63cd731ca742bb703e9899411086b8065e85bdf4bd94a"} -->

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

> **Regulatory Draft – Portable X‑ray Imaging System (Detector + Hand‑held Source + GUI Software)**  

---

### 1.   Device Scope & Intended Use  
*Portable diagnostic imaging system for acquisition of X‑ray images of the human body. The system comprises:*  

| Component | Function | MDR rule/class |
|-----------|----------|----------------|
| **Hand‑held X‑ray source** (radiation emitter) | Generates ionising radiation for diagnostic radiology | **Rule 10 – active device emitting ionising radiation → Class IIb** |
| **X‑ray detector** (image plate / flat‑panel) | Records the emitted X‑ray photons and creates a digital image | **Rule 17 – recording of diagnostic images → Class IIa** |
| **GUI software** (image display, measurement & decision support) | Provides visualisation and information used for diagnostic decisions | **Rule 11 – software providing diagnostic info → Class IIa (higher class only if it can cause death/serious deterioration)** |

*The overall system is classified at the highest applicable class → **Class IIb**.*

---

### 2.   Conformity‑Assessment Route  
| Device class | MDR Annex for assessment |
|--------------|--------------------------|
| Class IIb (non‑sterile, non‑active therapeutic) | **Annex IX** – Full quality‑management system (QMS) audit + technical documentation review by the Notified Body. |

*No Module letters are applicable under MDR; the route is defined solely by the Annex number.*

---

### 3.   Evidence Required to Satisfy GSPR (Annex I)  

| GSPR clause (Annex I) | Relevant component(s) | Evidential source (per source excerpt) | Typical evidence artefact |
|-----------------------|-----------------------|----------------------------------------|---------------------------|
| **§1 – General safety & performance** | All | IEC 60601‑1:2005+A1+A2 (Ed 3.2) – electrical safety for detector, source, GUI HW | Test reports, certification of compliance |
| **§5 – Usability** | Detector, Source, GUI SW | IEC 60601‑1‑6:2010+A1+A2; IEC 62366‑1:2015+AMD1:2020 | Human factors validation plan & report |
| **§16 – Radiation protection (general)** | Source, Detector | IEC 60601‑1‑3:2008+A1+A2; IEC 60601‑2‑28:2017; IEC 60601‑2‑54:2022 | Radiation safety test reports, shielding calculations |
| **§17 – Specific requirements for X‑ray devices** | Source (emitter) & Detector | IEC 60601‑1‑3 §17; IEC 60601‑2‑28 §17.2; IEC 60601‑2‑54 §16, §17.2 | Dose‑rate measurements, beam quality verification |
| **§18 – Software life‑cycle** | GUI SW | IEC 62304:2006+A1:2015 (embedded SW) | Software development files, verification & validation protocol & results |
| **§19 – EMC** | All | IEC 60601‑1‑2:2014+A1:2020 (§19.2) | EMC test report |
| **§20 – Electrical safety – protection against hazards** | All | IEC 60601‑1 §20 | Insulation resistance, leakage current tests |
| **§21 – Protection against mechanical hazards** | All | IEC 60601‑1 §21 | Mechanical integrity / impact testing |
| **§23 – Information supplied with the device (labeling & IFU)** | All | IEC 60601‑1‑6 §23; IEC 62366‑1 §23 | Label, user manual, risk information sheet |

**Additional GSPR clauses from chemical/biological safety (Excerpt [2]):**

| Clause | Requirement | Evidence needed |
|--------|-------------|-----------------|
| **10.1 – Toxicity free materials** | No toxic substances in contact parts | ISO 10993‑1 biological evaluation (test) for patient‑contacting surfaces |
| **10.2 – Biocompatibility with tissue, cells, fluids** | Suitability of materials | Full ISO 10993 series test portfolio (cytotoxicity, sensitisation, irritation etc.) |
| **10.3 – Limits on contaminants & residues** | Acceptable impurity levels | Analytical testing per relevant standards |
| **10.4 – Prevention of unintended material ingress** | Enclosure design verification | Design specifications + leak‑tightness test report |
| **10.5 – Nano‑material risk assessment** | Additional hazard evaluation if nanomaterials used | Risk Management File (RMF) entry & dedicated nano‑risk assessment (currently flagged as “verification needed”) |

---

### 4.   Identified Missing Information / Open Evidence Gaps  

| Gap | Impact on NB request | Action required |
|-----|----------------------|-----------------|
| **Nano‑material risk assessment (10.5)** – source marks “[검증 필요]” (verification needed). | NB will ask for a completed nano‑risk evaluation. | Conduct a dedicated risk analysis per ISO 14971, include toxicology data for nanomaterials, update RMF. |
| **Biocompatibility test reports for patient‑contacting parts** – only “TEST ISO 10993‑1” mentioned, no actual report cited. | Lack of evidence may block conformity assessment. | Perform ISO 10993 testing on all materials that contact patients (detector cover glass, source housing, cable insulation). |
| **Enclosure ingress protection verification (10.4)** – only “SPEC 인클로저 설계 검증” noted. | NB expects functional test data. | Provide design specifications plus pressure/temperature cycling tests proving ingress resistance (e.g., IP rating). |
| **Clinical Evaluation Report (CER) – state of the art & clinical performance** – not referenced in excerpts. | Required per Annex XIV Part A for all Class IIb devices. | Compile a CER covering literature review, device‑specific clinical data (pilot study), and post‑market surveillance plan. |
| **Post‑Market Surveillance Plan / PMS‑report** – not shown. | Mandatory under Art. 84/86 depending on class. | Draft PMS plan, define periodic safety update report (PSUR) schedule for Class IIb. |
| **Usability validation for GUI software** – only “IEC 62366‑1 … §5, §23” noted. | Need documented formative and summative usability testing. | Conduct user‑centred design activities, produce usability test protocol & results, map to IEC 62366‑1. |

---

### 5.   Risk Controls (ISO 14971) – High‑Level Summary  

| Hazard | Potential Harm | Control(s) |
|--------|----------------|-----------|
| **Ionising radiation exposure** (source malfunction, accidental emission) | Over‑dose, tissue damage | Interlock system, dose‑monitoring feedback, shielding, automatic shutdown, training & labeling per IEC 60601‑1‑3 §17. |
| **Electrical shock / fire** | Burns, cardiac arrest | Double insulation, leakage current limits (IEC 60601‑1 §20), protective earth, residual‑current device in supply chain. |
| **EMC interference** | Mis‑display of images, loss of data | EMC testing (IEC 60601‑1‑2) + shielding; robust grounding and filtering. |
| **Software error leading to misdiagnosis** | Incorrect clinical decision → patient harm | IEC 62304 development lifecycle, systematic verification & validation, risk control for “diagnostic information” per Rule 11, usability engineering (IEC 62366‑1). |
| **Nanomaterial release** | Cytotoxicity, inflammation | Material selection review, surface coating, containment in sealed housing; nano‑risk assessment. |
| **Ingress of contaminants (dust/water)** | Device failure, radiation leakage | Enclosure IP rating verification, sealing gaskets, protective covers. |
| **Mechanical impact / drop** | Damage to detector, loss of image quality | Mechanical design tests, protective case, handling instructions. |

All identified risks must be documented in the **Risk Management File (RMF)** with severity, probability, and mitigations; residual risk assessed as acceptable per MDR Art 61.

---

### 6.   Human‑Escalation Triggers  

| Situation | Trigger & Escalation Path |
|-----------|----------------------------|
| **Missing or unsatisfactory evidence for any GSPR clause** (e.g., nanomaterial assessment, biocompatibility) | RA Team Lead → Senior Regulatory Manager → Pause NB submission until gap closed. |
| **Unacceptable residual risk after RMF analysis** | Immediate escalation to Chief Clinical Officer & Legal for risk‑benefit re‑assessment; possible redesign. |
| **NB raises classification dispute (e.g., argues for Class III)** | Convene cross‑functional “Classification Review Board” with regulatory, clinical & safety experts; obtain legal opinion. |
| **Clinical Evaluation data insufficient to demonstrate performance** | Stop submission, trigger Clinical Trials/Investigational Study plan; involve Clinical Research Team. |
| **PMS signals serious incidents or field corrective actions** | Initiate Field Safety Corrective Action (FSCA) per Art 84; report to Competent Authority within 15 days; senior management briefing. |
| **Regulatory change affecting applicable standards (e.g., new IEC edition)** | Update technical documentation, re‑test as required; inform NB and schedule amendment of CE certificate. |

---

### 7.   Citations  

* **Classification & rules** – Rule 10 (active X‑ray emitter) → Class IIb; Rule 17 (detector) → Class IIa; Rule 11 (diagnostic software) → Class IIa (MDR Annex VIII).  
* **Conformity‑assessment route** – Annex IX (full QMS & technical file assessment).  
* **GSPR clauses & referenced standards** – directly taken from source excerpts: §§ 1, 5, 16, 17, 18, 19.2, 20, 21, 23 (Excerpt [1]); §§ 10.1‑10.5 (Excerpt [2]).  
* **Risk management requirement** – MDR Art 61 (requirement for RMF).  

> *No specific identifier (e.g., 510(k), predicate, case number) appears in the source material – verify separately.*

---

### 8.   Peer‑Review Prompt  

> **Colleague review request:**  
> Please challenge the following aspects of this draft:  
> 1. **Scope & classification** – Are there any additional functional elements (e.g., dose‑rate monitoring software) that could raise the system to a higher class under Rule 11?  
> 2. **Evidence coverage** – Does the list of required GSPR evidence fully reflect the standards referenced in the source, or are we missing any “§‑level” requirements (e.g., § 24 for environmental conditions)?  
> 3. **Jurisdictional gaps** – Considering the system will be marketed EU‑wide, have we addressed any nation‑specific requirements (e.g., German BfArM reporting obligations) that might not be covered by MDR alone?  

Your feedback will be incorporated before finalising the NB submission package.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 154/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 10,109자 | — |
| 규제 식별자 인용 | 11개 | — |
| source excerpt 근거 일치 | **4/11 (36%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 7개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art 61` | MDR Article 61 | Clinical evaluation |
| `Annex VIII` | MDR Annex VIII | Classification rules |

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

1. Chunk `1020150896244032022`

> | 조화표준 | X-ray Detector | Handheld Source | GUI SW | 연계 GSPR §§ | |---|---|---|---|---| | IEC 60601-1:2005+A1+A2 (Ed 3.2) | ● | ● | N/A | §1, §19, §20, §21 | | IEC 60601-1-2:2014+A1:2020 (EMC) | ● | ● | ● (SW HW포함 시) | §19.2 | | IEC 60601-1-3:2008+A1+A2 (방사선 방호) | ● | ● | N/A | §17 | | IEC 60601-1-6:2010+A1+A2 (사용성) | ● | ● | ● | §5, §23 | | IEC 60601-2-28:2017 (X-ray 관구) | N/A | ● | N/A | §17.2 | | IEC 60601-2-54:2022 (촬영·투시 장비) | ● | ● | N/A | §16, §17.2 | | IEC 62220-1-1:2015 (DQE) | ● | N/A | N/A | §1.1, §16.1 | | IEC 62304:2006+A1:2015 (SW 수명주기) | ● (내장SW) | ● (내장SW) | ● | §18 | | IEC 62366-1:2015+AMD1:2020 (사용성) | ● | ● | ● | §5, §23...

2. Chunk `1025819704026177008`

> ### §10 — 화학적·물리적·생물학적 특성 | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | 근거 문서 | |---|---|---|---|---|---|---| | 10.1 | 사용 재료의 독성 없음 확인 | ● | ● | N/A | TEST | ISO 10993-1 생물학적 평가 (환자 접촉 부위) | | 10.2 | 재료와 조직·세포·체액 적합성 | ● (접촉 시) | N/A | N/A | TEST | ISO 10993 시리즈 | | 10.3 | 오염물질·잔류물 허용 한도 이내 | ● | ● | N/A | TEST | 해당 표준 | | 10.4 | 의도하지 않은 물질 침투 방지 | ● | ● | N/A | SPEC | 인클로저 설계 검증 | | 10.5 | 나노소재 — 추가 위험 평가 | [검증 필요] | [검증 필요] | N/A | RMF | 나노소재 사용 여부 확인 필요 |

### kb-eval-20260718-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b6a40aca6ca36744", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

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

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Pathway**

---

### 1 Scope & Device Assumptions  
*The source excerpts do not provide a concrete device description, intended purpose, or technology type.*  
To produce a definitive classification and submission route the following information is required (see § 4 – Missing Information). Until that data is supplied the assessment below outlines the **process** that must be followed in accordance with the EU Medical Device Regulation (MDR) 2017/745.

---

### 2 Classification Procedure (Article 51 + Annex VIII)

| Step | Requirement | Regulatory source |
|------|-------------|-------------------|
| 2.1 | **Self‑classification responsibility** rests with the manufacturer. | (Art. 51 MDR) |
| 2.2 | Apply the **22 classification rules** in Annex VIII sequentially; the *highest* applicable rule determines the class. | (Annex VIII MDR) |
| 2.3 | If any doubt remains after rule application, seek an opinion from the **Competent Authority (CA)** or consult the MDCG “Borderline and Classification” manual (latest version v2.1.1 – September 2023). | (MDCG Manual v2.1.1) |
| 2.4 | Record the rule number(s) used and the rationale in the **Technical Documentation** (Annex II). | (Annex II MDR) |

> **Citation:** The excerpt explicitly references “제조사가 직접 분류 책임 부담 (자가 분류)” and “Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용” – i.e. the mandatory self‑classification process (Art. 51 + Annex VIII).  

---

### 3 Potential Conformity‑Assessment Routes (based on resulting class)

| Class | Typical MDR route | Key NB involvement | Main documentation |
|-------|-------------------|--------------------|----------------------|
| **Class I (non‑sterile, non‑measuring)** | Self‑declaration; no NB required. | None | Declaration of Conformity (Annex IV), Technical Documentation (Annex II). |
| **Class I (sterile / measuring)** | Annex IX – QMS + technical file assessment by NB. | NB reviews QMS (ISO 13485) & technical file. | Same as above plus evidence of sterilisation/measurement validation. |
| **Class IIa** | Annex IX – full NB audit of QMS and technical documentation. | Mandatory NB review. | Technical Documentation, Clinical Evaluation Report (CER) (Art. 61, Annex XIV Part A). |
| **Class IIb / III** | Annex IX *or* Annex X (type‑examination) + Annex XI (production conformity verification) where required by the specific rule (e.g., active implantable devices). | NB evaluates type‑examination, QMS, and production. | Technical Documentation, CER, **Post‑Market Surveillance (PMS) Plan** (Art. 84), **Periodic Safety Update Report (PSUR)** for IIb/III (Art. 86), plus **PMCF plan/evaluation** (Annex XIV Part B). |

> **Citation:** The requirement for a CER (“CEP + CER (Article 61, MDR Annex XIV)”) and PSUR (“Vigilance (MDR Art. 87), PSUR”) appears in excerpt [1].

---

### 4 Evidence Required per Route  

| Document | When required | Content highlights |
|----------|---------------|--------------------|
| **Clinical Evaluation Report (CER)** | All classes except pure Class I non‑measuring. | State‑of‑the‑art literature, clinical data, benefit–risk analysis – kept current under Art. 61 (Annex XIV Part A). |
| **Post‑Market Surveillance (PMS) Plan** | Mandatory for all devices; depth varies by class. | Data‑collection methods, vigilance procedures (Art. 83), periodic reporting schedule. |
| **PSUR / PMS Report** | Class IIa – PMS report (Art. 85). <br>Class IIb/III – PSUR (Art. 86). | Summary of safety data, trend analysis, corrective actions. |
| **Risk Management File** | All classes. | ISO 14971 process; identification of hazards, risk controls, residual risk evaluation. |
| **UDI Registration** | Mandatory for all MDs placed on the EU market. | Entry in EUDAMED (U­DI/DEV), cross‑reference to national UDI portal if applicable (excerpt [1] lists “UDI 포털”, “GUDID”). |
| **Authorized Representative & Importer details** | Required when manufacturer is outside the EU. | Signed Power of Attorney, registration in Art. 11 MDR; US Agent information for 510(k)‑exempt devices (excerpt [1]). |

---

### 5 Missing Information – Items Needed Before a Final Classification Decision  

| Category | Specific data required |
|----------|-----------------------|
| **Device description & intended purpose** | Full nomenclature, claims, target patient group. |
| **Technology type** | Is the device active therapeutic (Rule 9), active diagnostic/monitoring (Rule 10), software‑only (Rule 11), X‑ray imaging (Rule 17), or other? |
| **Energy modality / invasiveness** | Presence of ionising radiation, electrical energy, pharmacologic action, etc. |
| **Sterilisation / measuring function** | Determines if Class I becomes “sterile/measuring” (requires NB). |
| **Clinical data status** | Availability of clinical investigations or equivalence justification. |
| **Risk analysis outcomes** | Preliminary ISO 14971 risk management summary. |
| **Supply‑chain details** | Names & locations of Authorized Representative, Importer, and US Agent (if applicable). |
| **UDI strategy** | Planned label format, coding system, registration in EUDAMED. |

*Absence of any of the above precludes a definitive classification and thus blocks progression to the appropriate conformity‑assessment route.*

---

### 6 Key Risk Controls & GSPR Alignment (Annex I)

1. **Risk Management** – Complete ISO 14971 file; verify that residual risks are acceptable (Annex I, § 8).  
2. **Design Verification & Validation** – Demonstrate conformity to essential safety requirements (Annex I, §§ 4‑7).  
3. **Clinical Evidence** – Provide up‑to‑date CER citing state‑of‑the‑art literature (Art. 61, Annex XIV Part A).  
4. **Post‑Market Surveillance System** – Implement PMS plan & reporting mechanisms as per Art. 83–86.  
5. **UDI Integration** – Ensure traceability throughout the device life‑cycle; record in EUDAMED (Art. 33‑39).  

---

### 7 Human‑Escalation Triggers (When to Involve Senior RA, Notified Body or CA)

| Trigger | Reason & Action |
|---------|-----------------|
| **Uncertainty about applicable Annex VIII rule** | Escalate to senior RA for MDCG manual consultation; if still ambiguous, request a formal opinion from the Competent Authority. |
| **Missing clinical evidence for higher‑risk class (IIb/III)** | Pause submission; obtain clinical investigation data or robust equivalence justification before proceeding. |
| **Inability to demonstrate compliance with GSPR** (e.g., unresolved residual risk) | Immediate escalation to Technical Lead and NB liaison; remedial design changes required. |
| **UDI registration failure in EUDAMED** | Notify the UDI coordinator; resolve data‑model mismatches before CE marking can be issued. |
| **Authorized Representative not appointed for non‑EU manufacturer** | Escalate to business development/legal team – mandatory under Art. 11 MDR. |
| **Significant change in intended use after classification** | Re‑run the classification process (Art. 51) and notify NB of a new conformity‑assessment scope. |

---

### 8 Citations Summary  

| Reference | Location in source |
|-----------|--------------------|
| **Article 61, Annex XIV Part A – CER requirement** | Excerpt [1] (“CEP + CER (Article 61, MDR Annex XIV)”) |
| **Article 87 & PSUR / Vigilance** | Excerpt [1] (“Vigilance (MDR Art.87), PSUR”) |
| **Article 51 + Annex VIII – Self‑classification** | Excerpt [2] (“3.1 분류 원칙 (Article 51 + Annex VIII) … Annex VIII 22개 규칙 순차 적용”) |
| **MDCG Manual v2.1.1 (Sept 2023)** | Excerpt [2] (“최신판: 2023-09 개정 (Manual v2.1.1)”) |
| **Authorized Representative (Art. 11)** | Excerpt [1] (“Authorized Representative (Art.11)”) |
| **UDI portals & EUDAMED entry** | Excerpt [1] (“UDI 포털 … GUDID … EUDAMED UDI/DEV”) |
| **MDR Articles 83‑86 – PMS / PSUR** | Excerpts [1] (Art. 87, Art. 85, Art. 86) |

*No specific identifier such as a 510(k) number or case ID appears in the source – **no specific identifier found in source — verify separately**.*

---

### 9 Peer‑Review Prompt  

> **To: RA Peer (please review)**  
>   
> Please challenge the assumptions made above, especially:  
> 1. The completeness of the classification workflow given we have no device‑specific data.  
> 2. Whether the listed evidence items match the exact expectations for each class under current MDR guidance (e.g., any recent MDCG updates not reflected here).  
> 3. Potential jurisdictional gaps – e.g., interaction with US FDA exemptions mentioned in excerpt [1] and how they affect EU CE‑marking responsibilities.  
>   
> Highlight any missing references or alternative interpretations of the cited Articles/Annexes, and recommend additional sources (e.g., MDCG Guidance 2022‑6) that should be consulted before finalising the submission package.

--- 

**Prepared by:** Theo – EU MDR Regulatory Affairs Specialist  
*Document version for internal use only; not a formal CE‑marking submission.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 153/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,962자 | — |
| 규제 식별자 인용 | 22개 | — |
| source excerpt 근거 일치 | **8/22 (36%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 14개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art. 85` | MDR Article 85 | Post-market surveillance report (Class I) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `Art. 33` | MDR Article 33 | European database on medical devices (Eudamed) |
| `Article 87` | MDR Article 87 | Reporting of serious incidents and field safety corrective actions |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art. 51`
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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

## ra_kr

### kb-eval-20260718-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "862df3a912cbc93d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038"} -->

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

> **Regulatory Draft – Supplementary‑Response Strategy for MFDS Submission**

---

### 1. Likely Classification & Submission Route  

| Device type (assumed) | Korean classification* | Typical MFDS pathway | Reasoning |
|-----------------------|------------------------|----------------------|-----------|
| Class I (low risk)    | 신고 (Notification)   | Immediate, no review period | “신고 즉시” in source [1] |
| Class II‑III (moderate/high) | 허가 (Approval) – 일반 or 임상 포함 | 65 days (general) or 80 days (clinical) processing time, clock stops during supplement periods【1020687580074720264】 | The “허가(일반) 65일” and “허가(임상 포함) 80일” rows define the base review period. |
| Class IV (very high)  | 허가 + 인증 (KGMP)    | Certification route, 30 days, NIFDS‑委托【1020687580074720264】 | “인증 30일 NIFDS 위탁” indicates KGMP certification is required for the highest risk class. |

\*The exact class must be verified against MFDS Classification Table (제조·수입 의료기기 분류 기준).  

**Action:** Confirm the device’s risk classification using the official table; select the appropriate pathway (신고, 허가 일반, 허가 임상 포함 or 인증).

---

### 2. Core Evidence Package Required for a **허가** Submission  

| Evidence | Korean MFDS Requirement | International Equivalent | Remarks |
|----------|------------------------|---------------------------|---------|
| **Technical File / 품목허가 신청서** | Detailed device description, design & manufacturing drawings, KGMP certificate (if applicable) | FDA 510(k) or PMA technical dossier; EU Technical Documentation (Annex II/III) | Must be in Korean; English supplemental docs are allowed if accompanied by certified translation. |
| **Risk Management File (ISO 14971)** | 위험관리 보고서 including risk analysis, evaluation & control measures | Same as FDA/CE requirement | Include residual risk justification and benefit‑risk determination. |
| **Non‑clinical Testing** (bench, biocompatibility) | 시험자료 제출, conformity to Korean Standards (KS), or equivalent OECD‑aligned data accepted under recent MFDS notice (verify latest notice) | FDA non‑clinical & EU MDCG guidance | If using foreign data, cite the specific MFDS notice that allows OECD‑aligned evidence. |
| **Clinical Evaluation** | 임상시험계획서·보고서 (if “허가(임상 포함)”), or foreign CE/FDA clearance with supporting clinical evaluation report when permitted by MFDS scope expansion | FDA 510(k) clinical data, EU MDR Clinical Evaluation Report | For Class II‑III devices, local clinical data may still be required unless a current MFDS notice explicitly accepts the foreign CE/FDA evidence. |
| **Labeling (라벨·사용설명서)** | Korean language labeling, IFU, safety notices; format per MFDS “공문 문체” guidelines【1071384471244337751】 | FDA UDI/labeling, EU MDR Annex I labeling | Use the standard Korean phrasing for supplemental responses (e.g., “귀처의 보완 요청 내용…”) when replying to MFDS. |
| **Post‑Market Surveillance Plan** | 시판후조사 계획서, including adverse event reporting mechanism | FDA PMS/PSUR; EU MDR Post‑Market Surveillance plan | Required for Class II‑IV devices. |
| **KGMP Facility Certification** (if applicable) | 인증기관(NIFDS) 발행 KGMP 증명서 | ISO 13485 certification (accepted by MFDS for Class III‑IV) | NIFDS‑委托 30‑day processing time mentioned in source [1]. |

---

### 3. Gaps Usually Observed in Supplementary Submissions  

| Missing Item | Typical Reason for Deficiency | Suggested Remedy |
|--------------|------------------------------|------------------|
| **Clear reference to the specific MFDS notice** that permits foreign non‑clinical/clinical data | Authors cite “foreign data” without linking to the latest notice | Retrieve the current Notice (e.g., “MFDS 2025‑XX”) and attach it as part of the response. |
| **Korean translation of all supplementary documents** | Only English files uploaded; MFDS requires Korean for review | Provide certified Korean translations; reference the standard phrasing from source [2] when describing the supplement (e.g., “귀처의 보완 요청 내용(제○호, ○○항) …”). |
| **Documentation of pending test results** (e.g., “시험 진행 중”) | Authors note that testing is underway but give no timeline | Include a realistic schedule and request an official deadline extension if needed; use the phrasing “시험 일정상 ○월 ○일까지 보완자료 제출이 어려우므로, 기한 연장을 요청드립니다.”【1071384471244337751】. |
| **Evidence of compliance with Korean Standards (KS)** | Only foreign standards cited | Map each foreign standard to its KS counterpart; if none exists, provide an equivalence justification supported by the relevant MFDS notice. |
| **Signed KGMP certificate** for Class III/IV devices | Missing or outdated certification | Submit the most recent NIFDS‑issued KGMP certificate (30‑day processing). |

---

### 4. Risk Controls to Emphasize in the Response  

1. **Design Controls** – Show traceability matrix linking design inputs, outputs, verification & validation activities (ISO 13485 §7.3).  
2. **Software Lifecycle (if applicable)** – Demonstrate compliance with IEC 62304 and MFDS software guidance.  
3. **Biocompatibility** – Align test methods with ISO 10993‑1 and reference OECD‑aligned data where permitted.  
4. **Sterility Assurance (for sterile devices)** – Provide validated sterilization cycle and sterility assurance level (SAL) proof, referencing Korean GMP standards.  
5. **Usability / Human Factors** – Include formative/usability testing results to satisfy MFDS “사용자 안전성” expectations.

---

### 5. Citations Used  

| Source | Content Cited |
|--------|----------------|
| 【1020687580074720264】 | Processing times for 허가 (일반) 65 days, 허가(임상 포함) 80 days; 인증 30 days NIFDS‑委托; 신고 즉시. |
| 【1071384471244337751】 | Standard Korean supplement phrasing (e.g., “귀처의 보완 요청 내용…”, data attachment wording, extension request sentence). |

*No specific identifiers (e.g., case numbers, predicate device numbers) appear in the source excerpts; therefore none are included.*  

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger Condition | Recommended Escalation |
|-----------|-------------------|------------------------|
| **Clock‑stop exceeds 30 days** (supplement period) | MFDS has not responded within the expected “보완 기간” window (clock stops as per source [1]) | Notify senior RA manager; consider filing a formal inquiry to MFDS for status update. |
| **Critical data pending** (e.g., clinical trial results) | Expected delivery date of test results falls after the submission deadline or extension request denied | Escalate to project lead and sponsor for risk‑based decision on potential withdrawal or revised timeline. |
| **Regulatory notice ambiguity** (foreign evidence acceptance) | Uncertainty whether latest MFDS notice covers the foreign data being used | Seek counsel from a senior regulatory attorney or directly query MFDS via official channel. |
| **Labeling non‑compliance identified** | Reviewer flags missing Korean mandatory statements after submission | Immediate re‑submission of corrected labeling; inform quality assurance and marketing teams. |

---

### 7. Peer Review Prompt  

> **To the RA team:**  
> Please review this supplementary‑response draft and challenge the following assumptions:  
> 1. The classification inference based solely on processing‑time tables – are we confident the device does not fall into a higher class requiring KGMP certification?  
> 2. The reliance on generic “foreign data” acceptance – have we verified that the most recent MFDS notice (which may have changed after 2025) explicitly permits the specific OECD‑aligned studies we plan to submit?  
> 3. The completeness of Korean language requirements – does our current template fully satisfy all MFDS public‑notice labeling clauses, especially for devices with software components?  

Your feedback will help close any jurisdictional gaps before final submission.

---

### 8. Reusable RA Judgment (Honcho Record)  

```
honcho_conclude:
  lesson: |
    When preparing a supplemental response to an MFDS 허가 (approval) review, first verify the device’s exact Korean classification using the official MFDS Classification Table; this determines whether the pathway is 신고, 허가(일반), 허가(임상 포함), or 인증.  The base processing times are 65 days for 일반 and 80 days for 임상 포함, with clock‑stop during supplement periods (source [1]).  
    Mandatory evidence includes a Korean‑language technical file, risk management (ISO 14971) documentation, KGMP certification for Class III/IV, and clear alignment of any foreign non‑clinical/clinical data to the current MFDS notice that explicitly accepts OECD‑aligned or CE/FDA evidence.  Use the standard Korean supplement phrasing from MFDS guidance (source [2]) when addressing each request.  
    Flag missing items early—especially pending test results, Korean Standard (KS) conformity statements, and certified translations—as these trigger clock‑stop extensions and may require formal deadline extension requests.  Escalate to senior RA if the supplement period exceeds 30 days or if regulatory notice applicability is uncertain.
  peer: "ai"
```

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 152/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,020자 | — |
| 규제 식별자 인용 | 6개 | — |
| source excerpt 근거 일치 | **0/6 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 6개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex II` | MDR Annex II | Technical documentation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 10993` | ISO 10993 | 의료기기 생물학적 안전성 평가 — ISO 14971 위험관리에 반영 |

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

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `1071384471244337751`

> ### 4-C. 자주 사용하는 표현 (한국어 공문 문체) | 상황 | 표현 | |---|---| | 보완 내용 인용 | "귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다." | | 데이터 추가 제출 | "해당 데이터를 별첨 자료로 첨부하오니 검토하여 주시기 바랍니다." | | 시험 진행 중 | "현재 ○○기관에 시험 의뢰 중으로, 결과 수령 후 추가 제출 예정입니다." [검증 필요] | | 기준 적합성 | "관련 규격 ○○○ 기준을 충족함을 확인하였습니다." | | 연장 요청 | "시험 일정상 ○월 ○일까지 보완자료 제출이 어려우므로, 기한 연장을 요청드립니다." | ---

### kb-eval-20260718-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "9b4163a1bdf455ed", "source": "github:holee9/MD-process/issue-drafts/962_AUDIT_SOP-SBOM-001_디지털의료제품법_제16조_우수관리체계인증_오귀속.md", "source_hash": "54b06feb05bdd7dfc17d670d7f33374311c252e957960513a4aefe0d79a790e7"} -->

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

> **Regulatory Draft – SBOM (Software Bill of Materials) for a Digital Medical Device**

---

### 1. Applicable Legal Framework  
| Provision | Core Requirement | Relevance to SBOM |
|-----------|------------------|--------------------|
| **Digital‑Medical‑Device Act, Art. 13(2)** | “Continuous remediation of vulnerabilities arising from electronic attacks.” | Establishes a duty for manufacturers/importers to keep software components (including third‑party libraries) up‑to‑date and to manage known security weaknesses – the functional purpose of an SBOM. |
| **Digital‑Medical‑Device Act, Art. 14** | “Security measures against electronic attacks” – MFDS must issue security guidelines; manufacturers must comply. | Directly links to the need for a process that monitors component vulnerabilities (the guideline refers to a “physical‑technical management system”). An SBOM is an accepted tool for satisfying this monitoring requirement. |
| **Digital‑Medical‑Device Act, Art. 16** | “Excellent Management System Certification (quality‑, safety‑ and security‑management) – 3‑year validity.” | Provides the overarching certification mechanism; however, it does *not* prescribe SBOM creation per se. The certification may be used to demonstrate that the manufacturer’s internal processes for SBOM handling meet the security obligations of Art. 13(2) & Art. 14. |
| **MFDS Security Guideline (issued under Art. 14‑①)** | Technical and administrative controls for vulnerability management, patching, and incident response. | The guideline explicitly recommends maintaining an up‑to‑date SBOM as part of the “vulnerability tracking” process. *(Reference: MFDS Notice 2024‑04, “Guidance on Cybersecurity for Digital Medical Devices”.)* |

> **Citation rule compliance:** No specific identifier (e.g., notification number, case ID) appears in the source excerpts; therefore, no identifier is listed. All references are to article numbers and a generic guideline notice.

---

### 2. Device Classification & Submission Route  
| Factor | Determination |
|--------|----------------|
| **Device type** | Digital medical device (software‑based or software‑enabled hardware) that processes patient data or drives clinical decision support. |
| **Risk class** | According to the Korean classification matrix, most AI‑driven diagnostic/support software falls under **Class II** (moderate risk). If the software provides direct therapeutic effect or is invasive, it may be upgraded to **Class III** – a detailed functional analysis is required. |
| **Submission pathway** | • **Class II** → MFDS “신고” (notification) with attached security documentation. <br>• **Class III** → MFDS “허가” (approval) requiring full technical file and pre‑market clinical evaluation. |
| **KGMP requirement** | For Class III, the manufacturer must hold a **KGMP certificate** for the production site; for Class II, KGMP is not mandatory but strongly recommended to demonstrate compliance with Art. 16 certification. |

---

### 3. Evidence Package Required  

| Evidence Item | Legal Basis | Content Details |
|---------------|-------------|-----------------|
| **Security Management System (SMS) certification** | Art. 16 (certification), Art. 14 (security guideline) | • Certificate of “Excellent Management System” (valid ≤ 3 years). <br>• SOPs that map to the MFDS security guidelines, including SBOM generation, version control, vulnerability tracking, and patch deployment. |
| **SBOM documentation** | Art. 13(2), Art. 14 | • Complete Bill of Materials for each software release (component name, version, supplier, license). <br>• Change‑log linking SBOM updates to vulnerability disclosures (e.g., CVE entries). |
| **Vulnerability Management Report** | Art. 14 & MFDS security guideline | • Periodic risk assessment showing identified vulnerabilities, severity rating, mitigation actions, and residual risk. |
| **Software Development Lifecycle (SDLC) description** | General device quality requirement (ISO 13485:2016 Annex C). | • Flowchart of development phases, verification/validation activities, and security testing (static analysis, dynamic testing, penetration test results). |
| **Clinical Evaluation Report (if Class III)** | MFDS “의료기기 허가 심사 지침”. | • Evidence that the software’s clinical performance is not compromised by identified vulnerabilities. |
| **Labeling & IFU** | MFDS labeling guidelines | • Korean‑language user manual indicating required security updates, contact for vulnerability reporting, and a statement that an SBOM is maintained per MFDS guidance. |

*Note:* The source excerpts make clear that **Art. 16 does not itself mandate SBOM creation**, so the SBOM must be justified through Art. 13(2) & Art. 14 compliance.

---

### 4. Gaps / Missing Information (to be obtained before submission)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Exact classification outcome** (II vs III). | Determines whether a full approval dossier is needed. | Perform functional risk analysis per MFDS Classification Table; document intended use precisely. |
| **MFDS security guideline version number** (e.g., “2024‑04”). | Required for citation and to confirm that SBOM is an accepted control. | Retrieve the latest MFDS Cybersecurity Guidance from the MFDS website or official Gazette. |
| **KGMP certificate status** (if Class III). | Mandatory for manufacturing site. | Verify current KGMP certification; if absent, initiate KGMP audit. |
| **Evidence of continuous SBOM update process** (frequency, automated tooling). | Demonstrates compliance with “continuous remediation” duty. | Provide SOP showing schedule (e.g., quarterly) and toolchain (Syft, CycloneDX, etc.). |
| **Korean‑language IFU draft** including security notice. | Korean labeling is mandatory; failure leads to non‑conformance. | Prepare Korean IFU and obtain translation verification. |

---

### 5. Risk Controls Relating to SBOM  

| Hazard | Control (as per Art. 13‑2 & Art. 14) |
|--------|--------------------------------------|
| **Unpatched vulnerability in third‑party library** → Exploitation → Patient safety breach | • Maintain up‑to‑date SBOM for each release.<br>• Automated CVE scanning tied to SBOM components.<br>• Patch management SOP with defined rollout timelines (≤ 30 days for critical CVEs). |
| **Incorrect component version recorded in SBOM** → Incomplete vulnerability coverage | • Dual‑verification: automated generation + manual review by QA engineer.<br>• Version control integration (Git tag ↔︎ SBOM entry). |
| **Loss of SBOM data (integrity breach)** | • Secure storage (encrypted repository, role‑based access).<br>• Backup and audit log per Art. 16 certification requirements. |
| **Failure to follow MFDS security guideline** → Regulatory penalty | • Periodic internal audit against MFDS security checklist.<br>• Include SBOM compliance metrics in Management Review meetings (Art. 16). |

---

### 6. Human‑Escalation Triggers  

| Trigger Condition | Escalation Level | Responsible Role |
|-------------------|------------------|------------------|
| **Absence of current KGMP certificate for a Class III device** | Immediate stop of submission preparation; senior RA manager notified. | QA/RA Lead |
| **Discovery of a critical CVE (CVSS ≥ 9) in a released component without remediation plan** | Immediate reporting to MFDS security office and internal incident response team; pause distribution. | Security Officer / Product Manager |
| **MFDS releases an updated security guideline that changes SBOM requirements** | RA team must reassess SOPs within 5 business days; senior regulatory counsel notified. | Regulatory Affairs Lead |
| **Failure to produce Korean‑language IFU for a device slated for market entry** | Hold submission; legal/translation department engaged. | Documentation Manager |
| **Certification (Art. 16) expiry approaching (< 60 days)** | Initiate renewal audit; senior management briefed on timeline and resource needs. | Quality System Owner |

---

### 7. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made in this draft, especially: (1) the interpretation that SBOM obligations flow from Articles 13(2) and 14 rather than Article 16; (2) the classification rationale for placing the device in Class II/III without a detailed intended‑use statement; (3) the completeness of the evidence list given that no specific MFDS notice number is cited; and (4) any additional Korean‑specific obligations (e.g., post‑market surveillance reporting, electronic documentation filing) that may have been omitted. Highlight any jurisdictional gaps or missing source coverage.

---

### 8. Reusable RA Judgment (Honcho Record)

```
honcho_conclude:
  judgment: |
    In the Digital Medical Device Act, SBOM creation is **not** mandated by Art. 16 (“Excellent Management System Certification”). 
    The legal basis for requiring an SBOM derives from **Art. 13(2)** (continuous remediation of electronic‑attack vulnerabilities) and **Art. 14** (security measures & MFDS security guideline). 
    Therefore, regulatory submissions should reference Articles 13‑2 and 14 when justifying SBOM processes; citing Art. 16 as the direct source for SBOM is inaccurate.
  peer: "ai"
```

--- 

*Prepared by:* **Sam – Korean Regulatory Affairs Specialist (MFDS / KGMP)**  
*Date:* 2026‑07‑18

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 151/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,421자 | — |
| 규제 식별자 인용 | 5개 | — |
| source excerpt 근거 일치 | **0/5 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 5개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art. 13`, `Art. 14`, `Art. 16`
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

1. Chunk `1078549302777609829`

> ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 원문 직접 열람) | 조문 | 법정 제목·핵심 내용(원문) | |---|---| | **제13조** | "디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항" — 2호: 전자적 침해행위로부터의 취약점에 대한 지속적 보완 | | **제14조** | "전자적 침해행위로부터의 보호 조치" — 식약처장의 보안지침 마련 의무(①) + 제조업자등의 보안지침 준수 의무(②) | | **제16조(기재값)** | "우수 관리체계 인증" — 품질관리·안전관리·전자적침해행위 예방체계 등을 종합 평가하는 임의 인증(유효기간 3년). SBOM 직접 규정 아님 | | **제40조** | "디지털의료제품의 구성요소에 대한 성능평가" — 센서·AI 알고리즘 성능평가(별개 조문, AI_구성요소_단위_성능평가.md에서 정확히 인용 중 — PASS) |

2. Chunk `1111374550817299375`

> ## 독립 감사 요약 SOP-SBOM-001은 SBOM(Software Bill of Materials) 생성·관리 절차의 법적 근거로 "디지털의료제품법 제16조"를 2개소(frontmatter, §1 본문)에서 인용한다. 그러나 국가법령정보센터 원문(lsiSeq=259299, [시행 2026.1.24.] [법률 제20139호, 2024.1.23. 제정]) 직접 열람 결과, **제16조는 "우수 관리체계 인증"**(식약처장이 디지털의료기기제조업자등을 대상으로 실시하는 임의 인증제도 — 품질관리·안전관리·전자적침해행위 예방체계를 종합 평가하는 3년 유효 인증)을 규정하는 조문으로, SBOM 생성·관리 의무 자체와는 무관하다. SBOM/소프트웨어 구성요소 취약점 관리와 직접 관련된 조문은 **제14조(전자적 침해행위로부터의 보호 조치)**이다 — ① 식약처장이 "취약점을 지속적으로 감시하고 전자적 침해행위에 대응하는 물리적·기술적 관리체계에 관한 지침"(보안지침)을 마련, ② 제조업자등은 보안지침 준수 의무. 아울러 **제13조(준수사항) 제2호**도 "전자적 침해행위로부터의 취약점에 대한 지속적인 보완" 의무를 규정하여 SBOM의 취약점 추적 목적과 직접 연결된다. 참고로 제16조 ②항 3호에 "전자적 침해행위의 예방 및 대응체계"가 우수관리...

### kb-eval-20260718-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "f69d8f43954b58f7", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/진단용_방사선_발생장치_안전관리규칙_제1122호.md", "source_hash": "aff63a68606535ccc206bf522dc726414563ed06910c1de4ffa6655c6f7e55eb"} -->

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

> **Regulatory Draft – Diagnostic X‑Ray Generating Device (Safety Management Rule 제1122호)**  

---

### 1. Korean Classification & Submission Route  
| Item | MFDS position |
|------|---------------|
| **Device type** | Diagnostic radiology equipment that generates ionising radiation (X‑ray). |
| **Regulatory class** | **Class II** medical device (radiation‑generating equipment) – requires full “허가” (approval) under the Medical Device Act. |
| **Applicable rule** | *진단용 방사선 발생장치 안전관리규칙* 제1122호 (Safety Management Rule for Diagnostic Radiation‑Generating Devices). |
| **Submission pathway** | **전문 허가** – submission of a complete dossier to MFDS (device description, risk analysis, non‑clinical & clinical data, KGMP certification, Korean labeling/IFU, and evidence of compliance with the safety rule). |

> **Citation:** The source excerpts list the internal documents that map device test items to IEC standards and to the Safety Management Rule (see Table 1 in Chunk 1114051458699792259) and enumerate the performance limits required by the rule (Chunk 278739496403872085).

---

### 2. Required Evidence (per MFDS & Safety‑Management Rule)

| Evidence | What must be provided | Reference to source |
|----------|----------------------|---------------------|
| **Non‑clinical performance** | • Test reports showing compliance with IEC standards for X‑ray generators (e.g., IEC 60601‑2‑xx). <br>• Measured values for each of the 11 items listed in the rule (kVp accuracy, reproducibility, dose linearity, HVL, leakage, resolution, uniformity, SID accuracy, AEC density, etc.) – with results meeting the limits shown in Chunk 278739496403872085. | Chunk 278739496403872085 (F‑RAD‑SAFETY‑001 table). |
| **Procedural SOPs** | • **SOP‑CAL‑001** – Calibration & meter maintenance for kVp and dose meters.<br>• **SOP‑IQ‑001** – Installation verification (performance check at site).\n• **QC‑IQ‑001** – Routine quality‑control protocol for image quality.\n• **SOP‑SVC‑001** – Preventive‑maintenance & service schedule. | Chunk 1114051458699792259 (list of linked SOPs). |
| **Risk Management** | Full ISO 14971 risk analysis, highlighting ALARA design inputs and controls. Evidence of **ALARA_지원기능_설계명세** (design specification for dose‑reduction features) as per the mapping table. | Chunk 1114051458699792259 (ALARA design spec column). |
| **KGMP Certification** | Copy of current KGMP facility certificate (ISO 13485‑based). |
| **Korean Labeling/IFU** | All labels, safety warnings, and Instructions for Use in Korean language; conformity with MFDS labeling regulations. |
| **Clinical performance (if required)** | Clinical evaluation report (CER) demonstrating image‑quality adequacy for the intended anatomical target(s). If foreign CE/FDA clearance is used, a Korean translation of the clinical data must be submitted. |
| **Regulatory History** | Evidence of compliance with any prior amendments to the Safety Management Rule (e.g., “진단용 방사선 안전관리규칙 개정이력”). |

> **Citation:** No explicit MFDS dossier identifiers appear in the source excerpts; therefore, no specific 510(k), CE, or registration numbers can be cited. *“no specific identifier found in source — verify separately.”*

---

### 3. Missing Information (Gaps to resolve before submission)

| Gap | Why it matters | Action required |
|-----|----------------|-----------------|
| **Device‑specific specifications** – kVp range, focal spot size, maximum output dose, shielding design. | Required for the performance tables and risk analysis. | Provide a detailed spec sheet. |
| **Korean language labeling & IFU drafts** | Mandatory for 허가; MFDS will reject untranslated materials. | Prepare Korean versions and submit for pre‑review. |
| **KGMP certificate (copy, expiry date)** | Essential to demonstrate manufacturing compliance. | Obtain and attach the latest certificate. |
| **Clinical evidence** – clinical trial data or a CE/FDA technical file. | Needed if the device claims diagnostic efficacy beyond basic imaging. | Supply a CER or certified translation of foreign clinical data. |
| **Evidence of operator radiation‑protection measures** (e.g., shielding, dosimetry program). | MFDS requires proof that occupational exposure stays below limits. | Include a radiation safety plan and monitoring results. |
| **Full traceability matrix** linking each test item to the IEC standard and rule limit. | Demonstrates systematic compliance mapping. | Create and submit a traceability table (similar to the one in Chunk 1114051458699792259). |

---

### 4. Core Risk Controls (to be highlighted in the dossier)

1. **ALARA Design Specification** – engineered dose‑reduction features, automatic exposure control (AEC) with documented density reproducibility (±0.3 OD).  
2. **Periodic Self‑Inspection Form (F‑RAD‑SAFETY‑001)** – documented internal check of all 11 performance items; includes checkbox for customer‑PM verification.  
3. **Calibration & Maintenance SOPs** – scheduled kVp meter and dose‑rate calibrations per SOP‑CAL‑001; preventive‑maintenance program (SOP‑SVC‑001).  
4. **Quality‑Control Protocol (QC‑IQ‑001)** – routine image‑quality tests (resolution, uniformity, HVL) with defined acceptance criteria.  
5. **Interlock & Safety‑Shielding Systems** – hardware interlocks to prevent unintended exposure; compliance with leakage dose limit ≤1 mGy/h @ 1 m (rule).  
6. **User Training Program** – Korean language training modules covering safe operation, self‑inspection, and emergency procedures.  

---

### 5. Human‑Escalation Triggers (when a senior RA or the sponsor must intervene)

| Trigger | Reason for escalation |
|--------|-----------------------|
| Any measured value exceeds the limits in **F‑RAD‑SAFETY‑001** (e.g., kVp accuracy > ±10 % or leakage > 1 mGy/h). | Immediate redesign/calibration; submission cannot proceed. |
| **KGMP certificate missing or expired**. | Manufacturing compliance must be validated before dossier acceptance. |
| **Korean labeling/IFU not finalized** (translation incomplete, missing mandatory safety warnings). | MFDS will reject for language non‑conformance. |
| **Risk analysis lacks documented ALARA controls** or fails ISO 14971 verification. | Safety assessment insufficient; risk mitigation plan required. |
| **Clinical evidence absent when needed** (e.g., device intended for high‑resolution angiography). | Need to acquire clinical data or justify exemption. |
| **Discrepancy between test reports and SOP specifications** (e.g., SOP‑CAL‑001 states calibration frequency different from what is performed). | Clarify procedural alignment; avoid regulatory comment. |

When any of the above occurs, pause the submission and notify a senior RA manager for remedial action.

---

### 6. Peer‑Review Prompt  

> **To a fellow Korean RA colleague:**  
> Please examine the assumptions made in this draft—particularly (1) the classification as Class II “허가” versus possible Class III depending on output power, (2) whether the listed SOPs alone satisfy MFDS’s requirement for evidence of ongoing performance monitoring, and (3) any gaps not captured here regarding recent amendments to *진단용 방사선 발생장치 안전관리규칙* that might broaden accepted foreign data (e.g., OECD‑aligned non‑clinical studies). Highlight any jurisdiction‑specific nuances we may have missed.

---

### 7. Reusable RA Judgment (Honcho Conclude)

> **Judgment:**  
> For diagnostic X‑ray generating devices, MFDS Safety Management Rule 제1122호 requires a *전문 허가* dossier that maps each performance attribute (kVp accuracy, dose reproducibility, leakage, etc.) to explicit limits (±10 % kVp, ≤1 mGy/h leakage, …) as shown in the rule’s inspection table. Internal SOPs (CAL, IQ, QC, SVC) and a self‑inspection form (F‑RAD‑SAFETY‑001) constitute primary evidence of compliance; however, these documents must be submitted **in Korean** and linked to the corresponding IEC standards through a traceability matrix. Missing elements that routinely trigger MFDS comments are: (a) a current KGMP certificate, (b) complete Korean labeling/IFU, (c) documented operator radiation‑protection program, and (d) clinical performance data or justified exemption. Any deviation from the rule’s quantitative limits must be escalated immediately for redesign before proceeding with the submission.  

*Recorded for future reference in similar X‑ray device submissions.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 150/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,406자 | — |
| 규제 식별자 인용 | 3개 | — |
| source excerpt 근거 일치 | **0/3 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 3개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

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

1. Chunk `1114051458699792259`

> ## 5. 프로젝트 내 연계 문서 | 연계 문서 | 연계 내용 | |-----------|----------| | X-ray_장비_안전성능_표준_매핑 | 검사 항목 ↔ IEC 표준 상세 매핑 | | ALARA_지원기능_설계명세 | ALARA 설계입력·기능사양 상세 | | SOP-CAL-001 | kVp 미터, 선량계 교정 관리 | | SOP-IQ-001 | 설치검증 절차 — 설치 시 성능 확인 | | QC-IQ-001 | 영상품질 QC 프로토콜 | | SOP-SVC-001 | 서비스 활동 — PM/교정 서비스 절차 | | 진단용방사선_안전관리규칙_개정이력 | 규칙 개정 이력 추적 |

2. Chunk `278739496403872085`

> ### F-RAD-SAFETY-001: 정기검사 항목 대응 자체 점검 양식 | No. | 검사 항목 | 규칙 기준 | 출하 시험 SOP 참조 | 출하 시험 합격 기준 | 고객 PM 점검 포함 | 비고 | |-----|----------|----------|-------------------|-------------------|-----------------|------| | 1 | 관전압 정확도 | ±10% | | | ☐Yes ☐No | | | 2 | 관전압 재현성 | CV ≤5% | | | ☐Yes ☐No | | | 3 | 선량 재현성 | CV ≤10% | | | ☐Yes ☐No | | | 4 | 선량 직선성 | ±20% | | | ☐Yes ☐No | | | 5 | 반가층(HVL) | Al 규격 | | | ☐Yes ☐No | | | 6 | 누설선량 | ≤1mGy/h@1m | | | ☐Yes ☐No | | | 7 | 영상 해상도 | lp/mm 규격 | | | ☐Yes ☐No | | | 8 | 저대조도 | 규격 | | | ☐Yes ☐No | | | 9 | 균일성 | 규격 | | | ☐Yes ☐No | | | 10 | 조사야 정확도 | ±2% SID | | | ☐Yes ☐No | | | 11 | AEC 밀도 재현성 | ±0.3 OD | | |...

### kb-eval-20260718-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "7014751a297b619d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

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

> **Regulatory Draft – Digital‑Medical‑Device (Software) Submission**

---

### 1️⃣ 제품 분류·제출 경로  
| 항목 | 판단 근거 |
|------|-----------|
| **위험 등급** | 디지털 의료기기의 위험 등급은 *의도된 용도*와 *사용자(전문가/일반인)*에 따라 MFDS‑규정 제 22조·제 23조를 적용해 판단합니다. 현재 제공된 정보만으로는 정확한 등급을 확정할 수 없으므로 **예비 위험분석(Hazard Analysis)**이 선행되어야 합니다. |
| **제출 경로** | - **Ⅰ등급** → 신고 (신고서 제출)  <br> - **Ⅱ‑Ⅲ등급** → 허가 신청 (기술문서·임상·품질관리 자료 포함)  <br> - **Ⅳ등급** → 허가 + 임상시험 자료·심층 위험 관리 검토  <br>※ 등급이 확정되면 해당 경로에 맞는 전자/공식 문서를 MFDS에 제출합니다. |

---

### 2️⃣ 요구되는 증거·문서 (MFDS SW 가이드라인 기반)

| 구분 | 필수 항목 (출처) | 내용 요약 |
|------|------------------|-----------|
| **소프트웨어 식별** | S‑1: SW 버전·빌드 번호·릴리스일  <br> *디지털의료제품법 시행규칙* | 버전 관리 표, 빌드 리포트, 출시 일정표 |
| **업데이트 정책** | S‑2: SW 업데이트 방법 및 주기  <br> *MFDS SW 가이드라인* | OTA/패키지 업데이트 절차, 주기 계획서 |
| **시스템 요구 사항** | S‑3: 최소·권장 OS, CPU, RAM 등  <br> *MFDS SW 가이드라인* | 지원 OS 목록, 최소 사양표, 권고 사양표 |
| **호환 의료기기·인터페이스** | S‑4: 호환 기기 리스트 및 인터페이스 정보 | 연결 가능한 진단/치료 기기 목록, 통신 프로토콜 명세 |
| **데이터 포맷** | S‑5: DICOM·HL7 등 입출력 형식  <br> — | 데이터 교환 표준 정의서 |
| **사이버 보안 설정** | S‑6–S‑8: 암호 정책, 네트워크 분리, 접근 권한, 패치 절차, 잔류 위험 및 대처 방안  <br> *MFDS 사이버보안 가이드라인 2025.01* | 보안 설계 문서, 인증·권한 관리 매트릭스, 위험 완화 계획 |
| **백업·복구** | S‑9: 데이터 백업 및 복구 방법  <br> — | 백업 정책, DR(Disaster Recovery) 시나리오 |
| **시스템 로그** | S‑10 (권장): 로그 관리 방법  <br> *MFDS 사이버보안 가이드라인* | 로그 수집·분석 절차서 (권장은 아니지만 준비 권고) |
| **표시기재(라벨/IFU)** | ‣ 디지털의료기기 특화 표시기재 체크리스트 (Excerpt 2) | <br>① 한글 사용 의무 ② 제품명·제조사·수입자·식별코드 ③ 사용목적·사용법·주의사항·보관·폐기 지침 ④ 위험 등급 및 인증표시 ⑤ 소프트웨어 버전·업데이트 정보 등  <br>※ 상세 체크리스트는 “IFU_필수요소_3지역_비교.md” 파일을 참조 필요 |

**Citation Summary**  
- 필수 항목 S‑1~S‑9, S‑10 → 출처 [1] (Chunk 1050588546939300856)  
- 특화 표시기재 체크리스트 → 출처 [2] (Chunk 124386539616979555)

> **Note** – 본 문서에 구체적인 510(k)/predicate 번호, MFDS 허가번호 등은 원본에 포함되어 있지 않으므로 “no specific identifier found in source — verify separately” 로 표시합니다.

---

### 3️⃣ 현재 누락·보완 필요 정보  

| 분야 | 구체적 결여 내용 |
|------|-------------------|
| **의도된 용도·목표 사용자** | 제품이 치료, 진단, 모니터링 중 어느 영역에 속하는지 명시되지 않음. 등급 산정에 필수. |
| **위험 분석·리스크 매트릭스** | ISO 14971 기반 위험 관리 파일 미제공 (예: 위험 식별, 평가, 통제 계획). |
| **임상/비임상 성능 검증** | Ⅱ‑Ⅲ등급 이상에서 요구되는 임상시험계획서(CTP) 또는 해외 허가·인증 자료가 없음. |
| **사용성 시험 (UAT)** | 최종 사용자(전문의, 환자 등)를 대상으로 한 사용성 평가 결과 부재. |
| **한국어 라벨·IFU** | 특화 체크리스트는 요구하지만 실제 번역본·디자인 파일이 제출되지 않음. |
| **사이버 보안 상세 설계** | S‑6~S‑8 항목은 명시되었으나, 구체적인 암호 알고리즘, 네트워크 격리 구조도, 퍼징 테스트 결과 등 기술적 세부자료 미제공. |
| **백업·복구 시뮬레이션** | 데이터 복구 시간 목표(RTO), 복구 지점 목표(RPO) 등 구체적인 KPI가 정의되지 않음. |

---

### 4️⃣ 리스크 컨트롤 권고  

| 위험 영역 | 주요 통제 수단 (MFDS 가이드라인 기반) |
|-----------|---------------------------------------|
| **소프트웨어 결함** | - 코드 리뷰·정적 분석 <br> - 버전 관리와 변경 관리 절차 |
| **사이버 공격** | - 최신 암호 정책 적용(AES‑256 등) <br> - 방화벽·네트워크 분리, 최소 권한 원칙(PoLP) <br> - 정기 보안 패치 일정(S‑7) 및 잔류 위험 문서화(S‑8) |
| **데이터 손실** | - 일일/주간 백업 자동화(S‑9) <br> - 복구 시뮬레이션 테스트(DR 연습) |
| **사용자 오류** | - 한글 사용자 매뉴얼·IFU 제공 <br> - UI/UX 인간공학 검증, 사용성 시험 포함 |
| **호환 기기 간 인터페이스 장애** | - DICOM/Hl7 표준 프로토콜 인증 <br> - 인터페이스 호환 테스트 레포트(S‑4) |

---

### 5️⃣ 인간(전문가) Escalation Triggers  

| 상황 | 조치 |
|------|------|
| **위험 등급이 ‑Ⅳ** 또는 **임상시험 필요 여부 판단 불명** | RA팀 → 임상 전문가·의료기기 개발 팀에 등급 재확인 요청 |
| **사이버 보안 위험 항목 중 “알려진 잔류 사이버보안 위험”이 존재하고 구체적 대처 방안 미제시** | 정보보호팀/보안 컨설턴트에게 상세 리스크 완화 계획 요구 |
| **표시기재(라벨·IFU) 한글 번역·디자인 검토 미완료** | 품질관리(QMS) → 라벨링 담당 부서에 한국어 최종본 제출 요청 |
| **필수 시스템 로그 관리(S‑10)이 권장 수준에 머무르고** | 개발팀에게 로그 수집·분석 체계 구축(법적 증거 보전 목적) 요구 |
| **외국 허가·인증 자료를 활용하려 할 때 MFDS 범위 확대 여부 미확인** | 규제 전략 팀이 최신 MFDS 고시·공지 (예: 2025‑01 사이버보안 가이드라인 적용 범위) 검토 후 판단 |

---

### 6️⃣ 결론 & 다음 단계  

1. **위험 등급 산정** – 의도된 용도와 대상 사용자 정의 → 등급에 따라 신고/허가 결정.  
2. **핵심 문서 준비** – 위 표 ‘필수 항목’을 모두 포함한 기술문서·라벨·IFU 패키지 완성.  
3. **보완 데이터 확보** – 임상·비임상 성능 검증, 사용성 시험, 사이버 보안 상세 설계 등 누락된 증거 수집.  
4. **MFDS 최신 고시 확인** – 2025‑01 사이버보안 가이드라인 적용 범위 및 외국 인증 수용 여부 재검토(필요 시 추가 자료 요청).  
5. **전문가 검토·승인** – 위험 관리 파일, 라벨링, 번역본 등을 QA 팀과 법무팀이 최종 검증 후 MFDS 제출.

---

### 7️⃣ Peer‑Review Prompt  

> **동료 RA에게 질문:**  
> 1. 현 단계에서 제시된 “위험 등급 산정”을 위해 추가로 요구되는 의도·사용자 정의가 무엇이라고 보시는지?  
> 2. 제공된 체크리스트(Excerpt 2) 외에 MFDS가 최근 발표한 디지털 의료기기 표시기재 고시에서 놓친 항목은 없는가?  
> 3. 사이버보안 가이드라인(2025‑01) 적용 범위가 현재 제시된 S‑6~S‑8 항목을 넘어선 추가 요구사항(예: 인증기관 검증, 펜테스트 보고서 등)이 있을 수 있는지 검토해 주세요.  
> 4. 외국 허가·인증 자료를 활용하려 할 때 “범위 확대” 고시의 최신 버전이 반영되었는지 확인하는 최적 방법은?  

---

*Prepared by: Sam – Korean MFDS Regulatory Affairs Specialist (KGMP & Digital‑Medical‑Device focus)*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 149/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 4,340자 | — |
| 규제 식별자 인용 | 1개 | — |
| source excerpt 근거 일치 | **0/1 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 1개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

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

1. Chunk `1050588546939300856`

> | # | 항목 | 필수/권장 | 근거 | |---|---|---|---| | **SW 일반** | | | | | S-1 | **SW 버전·빌드 번호·릴리스일** | ✅ 필수 | 디지털의료제품법 시행규칙 | | S-2 | **SW 업데이트 방법 및 주기** | ✅ 필수 | MFDS SW 가이드라인 | | S-3 | **최소·권장 시스템 요건** (OS, CPU, RAM, 저장공간, 모니터 해상도, 네트워크) | ✅ 필수 | MFDS SW 가이드라인 | | S-4 | 호환 의료기기 목록 및 인터페이스 정보 | ✅ 필수 | — | | S-5 | 데이터 입출력 형식 (DICOM·HL7 등) | ✅ 필수 | — | | S-6 | 사이버보안 설정 지침 (암호 정책·네트워크 분리·접근 권한) | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-7 | 보안 패치 적용 절차 및 책임 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-8 | 알려진 잔류 사이버보안 위험 및 대처 방법 | ✅ 필수 | MFDS 사이버보안 가이드라인 2025.01 | | S-9 | 데이터 백업 및 복구 방법 | ✅ 필수 | — | | S-10 | 시스템 로그 관리 방법 | ⚠️ 권장 | MFDS 사이버보안 가이드라인 | | **AI/ML...

2. Chunk `124386539616979555`

> ## 3. 디지털의료기기 특화 표시기재 요건 체크리스트 > 일반 의료기기 표시기재 필수사항(→ IFU_필수요소_3지역_비교.md 참조)에 **추가**되는 항목

### kb-eval-20260718-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-18", "decision_ref": "kb-eval-20260718-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "4e1064335a341e0f", "source": "github:holee9/MD-process/issue-drafts/957_AUDIT_디지털의료제품법_요구사항_매트릭스_DR03_04_06_07_조항_인용부정확.md", "source_hash": "69fd83fc737cc227dd544a4a99489e380363bae13e5c30e7aca1a7dc20a4fe4e"} -->

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

> **Regulatory Draft – Digital‑Medical‑Device (디지털의료제품) Submission**

---

### 1. Tentative Classification & Submission Route  
| Item | Assessment | Rationale |
|------|------------|-----------|
| **Risk class** | *To be confirmed* – likely Class II or III depending on intended use, invasiveness and decision‑making impact (MFDS “디지털의료제품법” risk‐based matrix). | The device is a digital health product that will generate clinical evidence; higher‑risk functions usually fall into Class II/III. |
| **Submission pathway** | *허가* (full approval) rather than simple *신고* (notification) if the product performs diagnostic or therapeutic functions, requires clinical data under Articles 9/10. | The law distinguishes devices that need pre‑market clinical evaluation (Art. 9, Art. 10) from those only requiring post‑market real‑world evidence (Art. 15). |

> **Note:** No 510(k) / predicate number or Korean registration identifier appears in the source excerpts – *“no specific identifier found in source — verify separately.”*

---

### 2. Required Evidence Package  

| Evidence | Legal Basis (as cited) | What must be supplied |
|----------|-----------------------|----------------------|
| **Pre‑market Clinical Evaluation** | Article 9 “임상시험계획 승인” *or* Article 10 “임상적 성능시험계획 승인” (see source [1]) | • Approved clinical trial protocol <br>• Informed‑consent documents <br>• Data on safety & efficacy from the planned study |
| **Real‑World Evidence / Post‑market Use Evaluation** | Article 15 “실사용 평가” – evaluation of safety & effectiveness using data collected in actual use (source [2]) | • Real‑world data collection plan (RWE) <br>• Data management & analysis methodology <br>• Ongoing monitoring reports |
| **Technical Documentation** | MFDS Technical File requirements (ISO 13485‑compatible) | • Device description, intended purpose, software architecture <br>• Risk Management file (ISO 14971) <br>• Validation/verification results |
| **KGMP / “우수 관리체계 인증”** | Article 17 “우수 관리체계 인증의 신청 및 평가 등” – only applies to manufacturing quality system (source [2]) | • KGMP certificate or evidence of compliance with the Korean equivalent of GMP. If AI‑based, a *PCCP* is **not** required under Art. 17 (see source [2]). |
| **Cybersecurity & Post‑Market Surveillance** | Article 13 “디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항” – obligation to collect defect information & remediate cyber vulnerabilities (source [2]) | • Vulnerability management plan <br>• Incident reporting procedures |
| **Korean‑language labeling & IFU** | MFDS labeling rules (not quoted in source, but mandatory) | • Labels, Instructions for Use, and any software user manuals must be provided in Korean. |

---

### 3. Missing or Incomplete Information  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Incorrect legal citation for clinical efficacy** – the source flags that “임상적 유효성(해당 시) | 법 제15조” is likely erroneous; the correct provisions are Art. 9 or Art. 10 (source [1]). | Revise the technical file to reference Art. 9/10 for clinical evaluation and keep Art. 15 solely for post‑market real‑world evidence. |
| **Absence of a confirmed Clinical Evaluation Plan** – no trial protocol, endpoints, statistical plan identified. | MFDS will reject if pre‑market clinical data are missing or mis‑referenced. | Prepare a full Clinical Investigation Plan (CIP) aligned with Art. 9/10. |
| **Unclear classification** – risk class not yet justified. | Determines whether 허가 or 신고, and the extent of dossier. | Conduct a detailed risk analysis per MFDS risk matrix; document justification. |
| **KGMP certification status** – not mentioned if manufacturing is covered by “우수 관리체계 인증”. | Required for devices with manufacturing component (Art. 17). | Verify whether KGMP or equivalent quality‑system certificate exists; include copy in submission. |
| **Cybersecurity controls** – only a generic reference to Article 13, no concrete measures. | Digital health products are high‑risk for cyber threats; MFDS expects detailed mitigation plans. | Submit vulnerability assessment, patch management and incident response plan. |

---

### 4. Core Risk Controls (ISO 14971 alignment)  

| Hazard | Control Measure | Where documented |
|--------|-----------------|-------------------|
| Incorrect clinical decision support output | Validation of algorithm with clinically relevant datasets; independent verification. | risk‑management file, Clinical Evaluation Report |
| Data breach / unauthorized access | End‑to‑end encryption, role‑based access control, regular penetration testing. | Cybersecurity plan (Article 13) |
| Software malfunction leading to patient harm | IEC 62304 compliant software lifecycle; automated fail‑safe fallback to user alert. | Technical documentation & validation reports |
| Post‑market real‑world data misuse | Data governance policy, de‑identification procedures, ethical review. | Real‑World Evidence plan (Art. 15) |

---

### 5. Citations (as extracted from source)  

* **디지털의료제품법** (시행 2026.1.24., 법률 제20139호) – Articles 9, 10, 13, 15, 17, 39 (source [2]).  
* Issue identified in the draft matrix: clinical efficacy incorrectly linked to **Article 15**; correction to **Articles 9/10** recommended (source [1]).

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Recommended reviewer |
|---------|-----------------------|----------------------|
| Detection of legal citation mismatch (Art. 15 vs Art. 9/10) | Could cause MFDS rejection or post‑market audit. | Senior RA / Legal counsel |
| No definitive risk class justification before dossier assembly | Affects submission route and required evidence depth. | Device classification specialist |
| Absence of KGMP certificate when manufacturing is in scope | Mandatory for 허가 submissions involving hardware. | QA / GMP lead |
> **Escalation protocol:** Flag the issue in the project tracker, attach this draft, and request a review meeting within 2 business days.

---

### 7. Peer‑Review Prompt  

> **@RA‑Colleague**, could you please challenge the assumptions made above? Specifically:  
> - Is the classification likely to be Class II or III given the limited information we have?  
> - Does the evidence package fully satisfy MFDS expectations for a digital health product that uses AI, especially regarding pre‑market clinical data versus post‑market real‑world evidence?  
> - Are there any jurisdiction‑specific gaps (e.g., additional Korean language requirements, specific reporting templates) that we have missed?  

Your feedback will help tighten the dossier before it is submitted for MFDS review.

---

### 8. Reusable RA Judgment (Memory Outcome)

**Lesson:**  
When preparing a submission under the **디지털의료제품법**, *clinical efficacy/effectiveness must be supported by pre‑market clinical evaluation pursuant to Article 9 (clinical trial plan approval) or Article 10 (clinical performance test plan approval). The “실사용 평가” of Article 15 refers exclusively to post‑market real‑world evidence and is **not** the correct legal basis for establishing clinical efficacy. Mis‑citing Article 15 can lead to MFDS rejection; therefore, always verify that the cited article matches the nature of the data (pre‑ vs post‑market).  

**Actionable rule:**  
- If a draft matrix links “임상적 유효성” to Art. 15, automatically flag for correction to Art. 9/10.  
- Separate the evidentiary streams: pre‑market clinical trial dossier → Art. 9/10; post‑market RWE plan → Art. 15.  

*Record this judgment for future automated checks of digital‑medical‑device submissions.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 148/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,641자 | — |
| 규제 식별자 인용 | 12개 | — |
| source excerpt 근거 일치 | **0/12 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 12개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `Art. 9`, `Art. 10`, `Art. 15`, `Article 17`, `Article 13`
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

1. Chunk `399070733591760115`

> ### D4 — DR-07 (라인 76) - **기재값:** `임상적 유효성(해당 시) | 법 제15조` - **문제:** 임상적 유효성/임상평가는 법 제9조(임상시험계획 승인) 또는 제10조(임상적 성능시험계획 승인)에 해당할 가능성이 높으며, 제15조(실사용평가)와는 별개 개념. - **권고:** `법 제15조` → 제9조/제10조 중 해당 조문으로 정정 검토.

2. Chunk `515031043224754498`

> ## 1차 출처 확인 (국가법령정보센터, 디지털의료제품법 [시행 2026.1.24.] [법률 제20139호]) | 조문 | 법정 제목·내용(원문) | |---|---| | **제15조** | **"실사용 평가"** — 디지털의료기기제조업자등이 실제 사용 과정에서 수집된 정보로 안전성·유효성을 평가하는 것(실사용증거/RWE). 기술문서·사용적합성·임상적 유효성과 무관. | | **제17조** | **"우수 관리체계 인증의 신청 및 평가 등"** — 제16조 우수 관리체계 인증(GMP 유사 인증)의 신청·평가 절차. AI 변경관리계획(PCCP)과 무관. | | **제13조** | **"디지털의료기기제조업자 및 디지털의료기기수입업자의 준수사항"** — 결함정보 수집·사이버 취약점 보완 등 상시 준수의무. MFDS 사전상담(사전검토)과 무관. | | **제39조** | **"허가·신고 등의 사전 검토"** — 제조허가·인증·신고 등에 필요한 자료를 사전에 MFDS에 검토 요청할 수 있는 절차. MFDS 사전상담의 정확한 근거조문. |
