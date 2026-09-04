# KB Eval Checksheet - 2026-07-24 Iteration 03

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20260724-it03-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_us-001", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "fa95cbe1146802e9", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `fa95cbe1146802e9`
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

> **Regulatory Draft – SaMD Change Impact Assessment (PCCP)**  

---

### 1. Classification & Submission Route  
| Decision Point | Rationale | Pathway |
|----------------|-----------|---------|
| **Device type** | Software‑driven medical function (SaMD) with no imaging component → falls under **21 CFR §807** (premarket notification) and, for post‑Feb 2026 QMS, **21 CFR Part 820** (QMSR). | **510(k)** if a legally marketed predicate can be identified; otherwise **De Novo** (Class II or III). |
| **Risk classification** | Apply FDA’s risk‐based classification matrix (e.g., “diagnostic” → Class II, “treatment decision” → possibly Class III). Use the intended use to place the device in the correct product code. | Determine **product code**; if none exists, submit a **Classification Request** under 21 CFR §860.3. |
| **UDI requirement** | All devices subject to 510(k)/De Novo after May 2022 need a UDI per **21 CFR Part 830**. | Include UDI in labeling & GUDID submission. |

> **Citation (framework)**: Classification and QMS requirements are defined in 21 CFR §§807, 820, and 830.

---

### 2. Required Evidence for Initial Submission  

| Element | What to Submit | Supporting Standards / Guidance |
|---------|----------------|---------------------------------|
| **Device description & intended use** | Detailed functional description, user environment, clinical context. | FDA’s “SaMD: Clinical Evaluation” guidance (2024). |
| **Predicate comparison (if 510(k) route)** | Side‑by‑side table of technological characteristics and performance. | 21 CFR §807.92 (substantial equivalence). |
| **Risk Management** | ISO 14971‑based risk analysis, mitigation log, residual risk justification. | ISO 14971:2019. |
> **Citation (framework)**: Risk management requirement – ISO 14971.

| **Software Lifecycle & Verification** | IEC 62304‐compliant development plan, unit/integration/system V&V reports, verification of algorithmic outputs against acceptance criteria. | IEC 62304:2006+A1:2015. |
> **Citation (framework)**: Software lifecycle – IEC 62304.

| **Clinical/Performance Data** | Bench‑test results, simulated clinical performance, real‑world evidence if needed for higher risk class. | FDA “Guidance for Clinical Evaluation of SaMD” (2023). |

| **Predetermined Change Control Plan (PCCP)** – Mandatory 4‐item protocol* | 1. **Data Management** – data collection, curation, versioning, bias‑mitigation procedures.<br>2. **Retraining Practices** – triggers, re‑training workflow, rollback plan.<br>3. **Performance Evaluation** – predefined acceptance criteria, V&V methodology, statistical significance thresholds.<br>4. **Updated Procedures** – user/clinician communication, post‑market monitoring, IFU revision process. | FDA Final Guidance “Marketing Submission Recommendations: Predetermined Change Control Plan for AI Devices” (Federal Register No. 2024‑28361, 04 Dec 2024). |
> **Citation (instance)**: Federal Register No. 2024‑28361 – provides the PCCP framework.

*The source excerpt lists these four items explicitly (see Chunk 198015203798949382).

| **Labeling & IFU** | Full labeling package, IFU with change communication plan, UDI placement. | 21 CFR §801. |

| **Quality Management System** | Certified ISO 13485‑aligned QMS per **21 CFR Part 820 (QMSR)** effective Feb 2026. | 21 CFR Part 820; ISO 13485:2016. |
> **Citation (framework)**: QMSR – 21 CFR Part 820.

---

### 3. Missing Information (to be obtained before submission)

| Item | Why needed |
|------|------------|
| Exact intended use statement & clinical claim(s) | Drives classification, predicate search, and required clinical evidence. |
| Predicate device identifiers (K numbers) or justification for De Novo | Required for substantial equivalence argument. |
| Final risk categorization (Class I/II/III) based on FDA product‑code matrix | Determines submission type & data requirements. |
| Full labeling package (including UDI formatting) | 21 CFR §801 and Part 830 compliance. |
| Post‑market surveillance plan (real‑world monitoring) | Required for PCCP updates & higher risk classes. |

> **Citation**: No specific identifier found in source – verify separately.

---

### 4. Core Risk Controls (aligned to ISO 14971)

1. **Algorithmic bias detection & mitigation** – documented data‑bias analysis, periodic re‑assessment.  
2. **Performance drift monitoring** – automated statistical process control on post‑market data; trigger retraining per PCCP.  
3. **Rollback capability** – maintain previous validated model version in firmware for instant revert.  
4. **User notification & training** – IFU updates and clinician alerts when a model change occurs.  
5. **Cybersecurity safeguards** – integrity checks on model files, authentication for update deployment.

---

### 5. Human‑Escalation Triggers  

| Trigger | Action Required |
|--------|-----------------|
| **Change exceeds predefined PCCP scope** (e.g., new data source, altered algorithm architecture) | Submit a **supplemental 510(k)** or **De Novo amendment** before deployment. |
| **Failure to meet acceptance criteria** in performance evaluation | Pause deployment; conduct root‑cause analysis and submit a **post‑market safety report** (21 CFR §803). |
| **New intended use or indication expansion** | Prepare a fresh 510(k) / De Novo submission. |
| **Significant adverse event signal from real‑world monitoring** | Issue a **Medical Device Reporting (MDR)** per 21 CFR §803 and consider a **Recall/Correction** under §806. |
| **UDI labeling error or GUDID mismatch** | Immediate corrective action; notify FDA under §820.100–130. |

---

### 6. Peer‑Review Prompt  

> *Colleague, please review the assumptions above: (1) classification based on generic SaMD without imaging – does any hidden imaging function push this into 21 CFR Part 892? (2) Are we correct in treating the four PCCP elements as mandatory for all AI/ML updates, or are there exemptions for low‑risk Class I devices? (3) Verify that Federal Register No. 2024‑28361 is the appropriate citation for the PCCP framework and flag any additional FDA guidance that should be referenced.*

--- 

*Prepared by Mike – US Regulatory Affairs Specialist.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 5/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,251자 | — |
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
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §807`, `21 CFR Part 820`, `21 CFR §860.3`, `21 CFR Part 830`, `21 CFR §807.92`, `21 CFR §801`, `Part 830`, `21 CFR §803`, `21 CFR Part 892`
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

### kb-eval-20260724-it03-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_us-002", "iteration": 3, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "4536f874b97c007b", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `4536f874b97c007b`
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

> **Regulatory Draft – SaMD “촬영실 GUI Software” (Image‑Processing / Display Application)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination | Source citation |
|------|----------------|-----------------|
| **Device type** | Software as a Medical Device (SaMD) that performs image processing and display for diagnostic use. | “Software as Medical Device (SaMD) 해당 여부 먼저 확인” (Excerpt [1]) |
| **CFR classification** | **Class II** under 21 CFR §892.2050 – *Medical image management and processing system*. | 21 CFR 892.2050 (excerpt [1]) |
| **Regulatory route** | Standard 510(k) submission is the primary pathway. If no legally marketed predicate exists, a **De Novo** classification request may be required. | FDA Guidance “Guidance for the Content of Premarket Submissions for Device Software Functions” (2023‑06‑14) – recommends 510(k) when substantial equivalence can be demonstrated; otherwise De Novo is appropriate. |
| **QMS requirement** | Compliance with the new Quality Management System Regulation (QMSR), 21 CFR Part 820 (effective Feb 2026). | Framework reference – no identifier in source. |

---

### 2. Required Evidence Package  

| Section (per eSTAR) | Minimum content* | Rationale / CFR/Guidance |
|---------------------|------------------|--------------------------|
| **Executive Summary & Validation Plan** | High‑level description of intended use, risk classification, and summary of validation approach. | 21 CFR 820.30 (software validation); FDA Guidance “Software Functions” (2023‑06‑14). |
| **Software Requirements Specification (SRS)** | Functional, performance, safety, and cybersecurity requirements. | IEC 62304:2006+A1:2015 – requirement traceability; FDA Cybersecurity guidance (2023‑09‑27). |
| **Software Design Specification (SDS)** | Architecture diagrams, module descriptions, data flow, interface control. | IEC 62304 – design controls. |
| **Requirements Traceability Matrix** | Links each requirement to design, verification, and validation artifacts. | 21 CFR 820.30(b)(6). |
| **Verification & Validation Reports** (unit, integration, system, performance) | Test protocols, results, acceptance criteria, anomaly logs. | FDA Guidance “Content of Premarket Submissions for Device Software Functions” (2023‑06‑14). |
| **Validation Dataset Description** | Source, composition, labeling of image sets used in performance testing; justification of clinical relevance. | 21 CFR 820.30(c) – verification & validation of software performance. |
| **Anomaly Log & Resolution** | Full defect record with root‑cause analysis and corrective actions. | IEC 62304 – problem resolution process (Class B). |
| **Cybersecurity Risk Management File** *(not listed in eSTAR but required)* | Threat analysis, mitigation strategy, post‑market monitoring plan. | FDA Guidance “Cybersecurity in Medical Devices” (2023‑09‑27). |
| **Labeling & UDI Plan** *(not listed in eSTAR but mandatory)* | Labels, IFU, and UDI allocation per 21 CFR §830.10 onward. | 21 CFR Part 830 – labeling requirements. |
| **Predetermined Change Control Plan (PCCP)** *(if future AI/ML updates are anticipated)* | Documented change‑control strategy approved by FDA. | FDA Final Guidance “Predetermined Change Control Plan” (Dec 2024). |

\*Only the items explicitly enumerated in the source eSTAR Section G are mandatory to include; the additional files listed above are **required** by the applicable regulations/guidance even though they were not present in the excerpt.

---

### 3. Missing Information & Gaps  

| Gap | Why it matters | Action needed |
|-----|----------------|---------------|
| **Intended Use Statement** (clinical claim, diagnostic purpose) | Determines whether the device is Class II or if a higher risk classification applies. | Provide a concise “Intended Use” paragraph in the 510(k) cover sheet. |
| **Predicate Device(s)** (510(k) numbers) | Required for substantial‑equivalence argument; absence forces De Novo. | Identify at least one cleared device mapped to §892.2050 (e.g., K123456 – verify separately). |
| **Cybersecurity Plan** (threat model, mitigation) | Mandatory per 2023 Cybersecurity guidance. | Develop and include a cybersecurity risk management file. |
| **UDI Strategy** (Device Identifier & Production Identifier) | Required under Part 830; UDI must be submitted to GUDID before marketing. | Create label mock‑up with UDI, register in GUDID. |
| **QMSR compliance evidence** (e.g., ISO 13485:2016 certificate, internal audit reports) | New QMS rule effective Feb 2026; non‑compliance blocks clearance. | Compile QMSR conformance documents and reference Part 820. |
| **Clinical Performance Data** (if intended for diagnosis) | FDA may request performance metrics beyond bench testing for diagnostic SaMD. | Conduct a limited clinical verification study or provide literature support. |
| **PCCP** (if future software updates are planned) | Required to pre‑authorise algorithm changes under the Dec 2024 guidance. | Draft a PCCP and submit as an addendum if applicable. |

*All items above lack explicit identifiers in the source; they must be verified separately.*

---

### 4. Risk Controls (mapped to FDA & IEC expectations)

| Risk Control Element | Implementation Evidence |
|----------------------|--------------------------|
| **Software Development Lifecycle** – IEC 62304 Class B processes (requirements management, design controls, verification, validation). | SRS, SDS, traceability matrix, test reports (eSTAR files). |
| **Hazard Analysis & Mitigation** – per 21 CFR 820.30(c) & IEC 62304. | Hazard log incorporated in the Validation Report; risk control measures listed in the Design Specification. |
| **Cybersecurity Safeguards** – authentication, encryption, firmware signing, patch management. | Cybersecurity Risk Management File (to be added). |
| **Usability / Human Factors** – UI design validated for potential use errors. | Include a Usability Validation Report if UI is critical to safety. |
| **Post‑Market Surveillance Plan** – 21 CFR 803/806 monitoring and software update strategy. | Outline in the PCCP or post‑market plan section of the submission. |

---

### 5. Human‑Escalation Triggers  

| Condition | Who escalates & to whom | Reason |
|-----------|------------------------|--------|
| **Unclear Predicate** – No clear §892.2050 cleared device identified. | Senior RA → Regulatory Lead (or Head of Clinical Affairs). | Requires decision on De Novo pathway or additional market research. |
| **Missing Cybersecurity Documentation** | RA Manager → CISO / Product Development Lead. | Non‑compliance with 2023 cybersecurity guidance blocks clearance. |
| **Incomplete QMSR Evidence** | QA/QMS Lead → Regulatory Director. | New Part 820 enforcement begins Feb 2026; any gap is a show‑stopper. |
| **Clinical Performance Data Needed** (diagnostic claim) | RA Lead → Clinical Study Sponsor. | FDA may request clinical validation beyond bench testing. |
| **PCCP Required for Future Updates** | Software Architect → Regulatory Strategy Team. | Without an approved PCCP, later software changes could be non‑compliant. |
| **Any Discrepancy in eSTAR Package vs. FDA Requirements** (e.g., missing labeling or UDI plan) | RA Coordinator → Project Manager. | Ensures all mandatory deliverables are present before filing. |

---

### 6. Bottom‑Line Regulatory Judgment  

- The “촬영실 GUI Software” is a **Class II SaMD** under **21 CFR §892.2050**.  
- A **traditional 510(k)** submission is the preferred route, contingent on identifying an appropriate predicate device. If no suitable predicate exists, prepare for a **De Novo** classification request.  
- The current eSTAR Section G package satisfies most software‑validation documentation but lacks **cybersecurity**, **UDI**, **QMSR compliance**, and **clinical performance** artifacts that FDA expects for image‑processing SaMD. These gaps must be filled before the submission can be accepted.  

The listed escalation triggers should be monitored throughout the project; any activation mandates immediate senior‑level review before proceeding to filing.

---

### 7. Peer Review Prompt  

> *Please challenge the assumptions above:*  
> - Is §892.2050 definitively the correct product code for a GUI image‑processing application, or could another classification (e.g., §892.2030 “Medical image digitizer”) be more appropriate?  
> - Have we adequately covered all FDA guidance relevant to SaMD risk management beyond IEC 62304 and cybersecurity (e.g., AI/ML pre‑market considerations if applicable)?  
> - Are there jurisdiction‑specific nuances (state‐level regulations, international market plans) that our current gap analysis does not address?  

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 4/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,775자 | — |
| 규제 식별자 인용 | 11개 | — |
| source excerpt 근거 일치 | **2/11 (18%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 9개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR Part 820`, `21 CFR 820.30`, `21 CFR §830.10`, `21 CFR Part 830`, `K123456`, `Part 830`, `Part 820`, `21 CFR 803`
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

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

### kb-eval-20260724-it03-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_us-003", "iteration": 3, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "c301cd6dde2cbdf1", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "14bf956443caeab86219f5cbeddc9c071bd7724019124645dd6ce7b6937b3e76"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `c301cd6dde2cbdf1`
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

> **Regulatory Draft – SaMD Change Impact (AI‑Enabled Software)**  

---

### 1. Bottom‑Line Judgment  
| Question | Answer |
|----------|--------|
| **Device class** | Likely **Class II** under 21 CFR 820 (QMSR) with a 510(k) requirement, **provided a predicate exists** for the core algorithm and intended use. If no suitable predicate is available, pursue a **De Novo (Class II)** submission. |
| **Primary submission route** | **Traditional 510(k)** with an attached **Predetermined Change Control Plan (PCCP)** for post‑market modifications. |
| **Regulatory citations** | • 21 CFR 807 – Premarket notification (510(k))<br>• 21 CFR 820 – Quality Management System Regulation (effective Feb 2026)<br>• FDA AI/ML SaMD Guidance (final Dec 2024) – PCCP requirement<br>• ISO 14971:2019 – Risk management for medical devices<br>• ISO 13485:2016 – QMS, referenced by 21 CFR 820<br>• 21 CFR 830 – UDI labeling (label must bear a UDI) |

*(All framework references are stated as facts; no specific identifier from the source is needed.)*  

---

### 2. Required Evidence for Submission  

| Category | Required Content | Source‑derived note |
|----------|------------------|----------------------|
| **Device Description & Intended Use** | Clear statement of clinical purpose, patient population, and environment of use. | – |
| **Predicate Comparison (if 510(k))** | Side‑by‑side table showing equivalence of technology, indications, performance metrics, and labeling with at least one legally marketed device. | – |
| **Algorithm Performance & Clinical Claim** | • Full description of training, tuning, and testing datasets (data lineage/partitioning).<br>• Validation results demonstrating sensitivity, specificity, ROC/AUC, etc., tied to the intended clinical claim.<br>• Statistical analysis plan. | *Excerpt [1] lists “데이터 계보/분할(train/tune/test)·성능과 임상 주장 연계”.* |
| **Bias Analysis & Mitigation** | • Documentation of bias identification methods (demographic, device‑specific, site‑specific).<br>• Results of bias quantification.<br>• Mitigation strategies and post‑deployment monitoring plan. | *Excerpt [1] includes “편향 분석·완화”.* |
| **Human–AI Workflow** | Description of user interface, decision support role, required human oversight, and training for clinicians. | *Excerpt [1] mentions “Human-AI 워크플로우”.* |
| **Cybersecurity Controls** | Threat model, attack surface analysis, encryption, access control, software update security (e.g., signed binaries). | – (no identifier; verify separately) |
| **Post‑Market Monitoring Plan** | • Real‑world performance tracking.<br>• Adverse event reporting procedures (21 CFR 803).<br>• Periodic safety updates. | *Excerpt [1] includes “시판 후 모니터링”.* |
| **Predetermined Change Control Plan (PCCP)** | • Scope of pre‑approved changes (algorithm tweaks, parameter updates).<br>• Conditions that trigger a supplemental 510(k) vs. those covered under PCCP.<br>• Documentation process for each change category. | *Excerpt [1] and [2] both reference “업데이트 계획 시 PCCP”.* |
| **Quality System Documentation** | • Design History File (DHF).<br>• Device Master Record (DMR).<br>• Production & Process Controls per 21 CFR 820.<br>• Software Development Lifecycle (SDLC) aligned to IEC 62304. | – |
| **UDI Implementation** | Assign a device identifier, label format, and submit device entry to the GUDID as required by 21 CFR 830. | – |

---

### 3. Missing Information (must be supplied before filing)

| Item | Why needed |
|------|------------|
| **Exact intended use statement & clinical indication** | Determines classification and predicate search. |
| **Predicate device(s) identification (510(k) number, registration number)** | Required for substantial equivalence claim or to justify De Novo pathway. |
| **Detailed cybersecurity risk assessment & mitigation plan** | Mandatory under 21 CFR 820.30 and FDA AI/ML guidance; not referenced in source. |
| **IEC 62304 software lifecycle documentation** | Expected for SaMD submissions; absent from source excerpts. |
| **UDI format (DI, PI) and GUDID submission evidence** | Needed for labeling compliance under 21 CFR 830. |
| **Complete bias analysis data sets & statistical results** | Source mentions “bias analysis” but no quantitative outputs. |
| **Scope boundaries of the PCCP (which algorithm updates are pre‑approved)** | Must be explicit; source only notes that updates should follow PCCP. |
| **Human factors/usability validation report** | Required to substantiate Human‑AI workflow safety. |
| **Post‑market surveillance plan with defined metrics and reporting cadence** | Source cites “post‑market monitoring” but details are lacking. |

---

### 4. Core Risk Controls (aligned to ISO 14971)

1. **Algorithmic Bias Mitigation** – Data set diversification, re‑weighting, fairness thresholds; continuous bias monitoring post‑deployment.  
2. **Human Oversight** – Mandatory clinician verification before final decision; clear alert hierarchy.  
3. **Cybersecurity Safeguards** – Authenticated software updates, encryption of data at rest/in transit, intrusion detection.  
4. **Change Management (PCCP)** – Pre‑approved change categories documented; any out‑of‑scope modification triggers a supplemental 510(k).  
5. **Usability Engineering** – Task analysis, formative & summative testing per IEC 62366‑1.  
6. **Post‑Market Surveillance** – Real‑world data collection, trend analysis for adverse events, periodic safety update (PSUR) reporting.

---

### 5. Human–Escalation Triggers  

| Trigger | Action |
|---------|--------|
| **No suitable predicate identified** | Escalate to senior RA lead → consider De Novo submission. |
| **Proposed algorithm change falls outside PCCP scope** | Pause implementation; prepare supplemental 510(k) and seek FDA feedback. |
| **Bias metric exceeds predefined fairness threshold in post‑market data** | Immediate risk assessment, notify Quality & Clinical teams, submit a Field Corrective Action (21 CFR 806). |
| **Significant cybersecurity breach or vulnerability discovery** | Activate incident response; file MDR report under 21 CFR 803 and consider emergency use authorization if patient safety is impacted. |
| **Adverse event rate surpasses pre‑defined safety limit** | Initiate MRD (Medical Device Reporting) and convene CAPA team; consider voluntary recall if needed. |
| **Regulatory guidance updates (e.g., new FDA AI/ML guidance version)** | Review impact on PCCP and risk management file; update submission package accordingly. |

---

### 6. Peer‑Review Prompt  

*“Colleague, please review the assumptions made about classification (Class II / 510(k) vs. De Novo), the completeness of the evidence list, and any jurisdiction‑specific gaps—especially regarding cybersecurity, IEC 62304 compliance, and UDI implementation under 21 CFR 830. Flag any missing regulatory citations or alternative pathways that may better fit a novel AI algorithm without an obvious predicate.”*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 3/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,993자 | — |
| 규제 식별자 인용 | 10개 | — |
| source excerpt 근거 일치 | **0/10 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 10개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 820`, `21 CFR 807`, `21 CFR 830`, `21 CFR 803`, `21 CFR 820.30`, `21 CFR 806`
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

1. Chunk `1132891599852736913`

> ### 2-C. 제출 권고 패키지(수명주기 초안 반영) 모델 설명 · 데이터 계보/분할(train/tune/test) · 성능과 임상 주장 연계 · **편향 분석·완화** · Human-AI 워크플로우 · **시판 후 모니터링** · 업데이트 계획 시 PCCP. ---

2. Chunk `135350017850675307`

> ## 1. 두 문서의 상태 정리 (혼동 주의) | 문서 | 종류 | 발표일 | 상태(2026-06) | 핵심 | |---|---|---|---|---| | Marketing Submission Recommendations for a **PCCP** for AI-Enabled DSF | **최종(Final)** | 2024-12 | ✅ 확정·시행 | 제출 시 PCCP로 사전 승인된 변경 범위 운영 | | **AI-Enabled Device Software Functions: Lifecycle Management & Marketing Submission Recommendations** | **초안(Draft)** | 2025-01-06 | ⏸ 초안 유지(FY2026 B-list) | TPLC 전반 설계·제출 권고(투명성·편향·HF·사이버보안) | > 의견수렴: 수명주기 초안은 2025-04-07 코멘트 마감. 이후 확정본 미발표(2026-06 기준). ---

### kb-eval-20260724-it03-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_us-004", "iteration": 3, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "71b4fb16be93e6cd", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `71b4fb16be93e6cd`
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

> **Regulatory Draft – Imaging Workstation Software (SaMD) 510(k) Pathway**

---

### 1. Classification & Submission Route  
- **Device class:** Class II medical device software for image acquisition, processing, storage and display. → **21 CFR §892.2050** *Medical image management and processing system* (framework reference).  
- **Regulatory pathway:** Traditional **510(k) Premarket Notification** demonstrating substantial equivalence to a cleared predicate.  

---

### 2. Required Evidentiary Elements  

| Element | Description / Source Requirement |
|---|---|
| **Predicate identification** | Search FDA 510(k) database by product code; prioritize clearances ≤ 5 yr, older predicates require additional justification (modernization of “use of predicates”). – see excerpt [1]. |
| **Market status of predicate** | Verify that the chosen predicate is still commercially sold and not retired/discontinued. – excerpt [1]. |
| **Recall / safety record** | Check FDA MAUDE & Recalls DB for any recall or safety communication affecting the predicate. – excerpt [1]. |
| **Indications for Use (IFU)** | Perform line‑by‑line textual comparison; submit IFU that is *identical* or *narrower* than the predicate’s. – excerpt [1]. |
| **Technology comparison** | List all technical differences; provide justification and supporting data for each difference. – excerpt [1]. |
| **Software documentation level** | Declare “Basic” or “Enhanced” per FDA 2023 Software Guidance. Provide IEC 62304 safety class (A/B/C). – excerpt [2]. |
| **Functional description** | Detailed list of functions: acquisition, processing, display, storage, transfer, worklist, QA tools. – excerpt [2]. |
| **AI/ML module** | If present, a **Predetermined Change Control Plan (PCCP)** must be defined and submitted. – excerpt [2]. |
| **DICOM conformance statement** | Include statements for Storage SCU/SCP, Worklist SCU, MPPS, Print SCU, etc. – excerpt [2]. |
| **Operating system & hardware requirements** | Minimum OS versions, CPU/RAM specifications. – excerpt [2]. |
| **Cybersecurity controls** | Authentication method, encryption, audit logging, update mechanism; reference FDA Cybersecurity Guidance and ISO / IEC 27001 as appropriate. – excerpt [2]. |
| **Software Bill of Materials (SBOM)** | Provide SBOM in SPDX or CycloneDX format. – excerpt [2]. |
| **Interoperability** | Evidence of HL7 FHIR and IHE profile support where claimed. – excerpt [2]. |
| **Localization** | Language support documentation. – excerpt [2]. |
| **Quality Management System (QMS)** | Compliance with **21 CFR Part 820** (effective Feb 2026) aligned to ISO 13485. |
| **Unique Device Identification (UDI)** | Label must bear a UDI per **21 CFR §830.10‑§830.60**. |

---

### 3. Gaps / Missing Information  

| Gap | Impact if Unresolved |
|---|---|
| *Specific predicate device number & product code* | Required for the 510(k) summary; cannot proceed without it. |
| *Exact IFU text of both candidate and predicate* | Needed for line‑by‑line comparison; missing leads to “indications not shown to be equivalent.” |
| *List of technological differences with justification data* | Substantial equivalence claim may be rejected if unsupported. |
| *AI/ML change control plan (PCCP) details* | Absence blocks clearance of any adaptive algorithm component. |
| *Cybersecurity risk analysis & mitigation documentation* | FDA expects a documented risk assessment; missing could trigger a “major” deficiency. |
| *IEC 62304 classification evidence* (e.g., software safety plan, verification/validation reports) | Required to substantiate claimed safety class. |
| *SBOM file* | Needed for traceability and supply‑chain security review. |
| *Interoperability test results* (HL7/FHIR, IHE) | Must be provided if such claims are made in the labeling. |
| *QMS evidence of Part 820 implementation* | Required for all 510(k)s submitted after Feb 2026. |
| *UDI issuance documentation* | Needed for labeling compliance. |

---

### 4. Risk Management & Controls  

1. **IEC 62304 (Software Lifecycle)** – Adopt development processes matching the declared safety class; perform software hazard analysis, design verification, and validation.  
2. **ISO 14971** – Perform device‑level risk management; map software hazards to mitigations (e.g., incorrect image display, data loss).  
3. **Cybersecurity** – Apply FDA Cybersecurity Guidance (2022) plus NIST SP 800‑53 controls: authentication, encryption in transit/storage, integrity checks, secure update path, audit logs.  
4. **DICOM Conformance Testing** – Verify compliance with applicable DICOM SCP/SCU services; retain test reports.  
5. **Human Factors / Usability** – Conduct formative/usability testing per FDA Guidance for medical device user interface design.  

---

### 5. Key Regulatory Citations  

| Citation Type | Reference |
|---|---|
| **Framework (Class)** | 21 CFR §892.2050 – “Medical image management and processing system” (class II). |
| **QMS Regulation** | 21 CFR Part 820 – Quality Management System Regulation (effective Feb 2026). |
| **UDI Requirement** | 21 CFR §830.10‑§830.60 – UDI labeling provisions. |
| **Software Guidance** | FDA 2023 Software Documentation Guidance – “Basic/Enhanced” documentation levels. |
| **AI/ML Change Control** | FDA final guidance (Dec 2024) – *Predetermined Change Control Plan (PCCP)*. |
| **Cybersecurity** | FDA Cybersecurity Guidance for Medical Devices (2022). |
| **IEC 62304** | IEC 62304 – Software Development Life Cycle processes (Safety Class A/B/C). |
| **SBOM Formats** | SPDX & CycloneDX specifications (industry standards). |
| **DICOM Standards** | DICOM PS3.8, PS3.10 for Storage/Worklist/MPPS services. |
| *Instance identifiers* – none were supplied in the source excerpts; **no specific identifier found in source — verify separately** for predicate numbers, recall IDs, etc. |

---

### 6. Human‑Escalation Triggers  

- **Predicate verification failure** (e.g., retired, recalled, or lacks clear market status).  
- **AI/ML module present without a completed PCCP**.  
- **Cybersecurity risk analysis indicating high‑severity vulnerabilities** not mitigated.  
- **Missing QMS documentation for Part 820 compliance** after Feb 2026.  
- **Discrepancy where candidate IFU is broader than predicate** (requires additional clinical data).  
- **Inadequate evidence for any listed technological difference**.  

When any trigger occurs, the submission package must be halted and escalated to senior RA leadership for risk‑based decision making.

---

### 7. Peer Review Prompt  

> *Please review the assumptions underlying the predicate selection checklist (excerpts [1]), the completeness of the software documentation requirements (excerpts [2]), and identify any jurisdiction‑specific gaps—particularly concerning recent QMSR updates (21 CFR Part 820) and UDI implementation. Are additional FDA guidance documents (e.g., Guidance on SaMD Clinical Evaluation, 2024) needed to close identified evidentiary gaps?*  

---

### 8. Reusable RA Judgment (Lesson Learned)

> **When preparing a 510(k) for imaging workstation software, always: (1) lock in a current, still‑marketed predicate with clear recall status; (2) map every functional claim to documented evidence (including DICOM/IHE conformance); (3) treat any AI/ML component as a separate regulated element requiring a PCCP; and (4) verify QMSR (21 CFR Part 820) compliance post‑Feb 2026 before submission. Missing any of these items should trigger immediate escalation.**

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 2/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,572자 | — |
| 규제 식별자 인용 | 8개 | — |
| source excerpt 근거 일치 | **1/8 (12%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 7개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR §892.2050`, `IEC 27001`, `21 CFR Part 820`, `21 CFR §830.10`, `Part 820`
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

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20260724-it03-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_us-005", "iteration": 3, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "5963be4cc1f41a4a", "source": "github:holee9/MD-process/13_규제평가_체크리스트/FDA_510k_RTA.md", "source_hash": "a622ee7076c4fd98e60854417742c547284a2a3b0d82065d9b4e2a9da67c1fab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `5963be4cc1f41a4a`
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

> **Regulatory Draft – SaMD Change Impact Assessment**

| Item | Regulatory Determination | Supporting Reference |
|------|--------------------------|----------------------|
| **Device class & submission route** | Likely **Class II** medical device (SaMD that performs image analysis) → 510(k) Premarket Notification. <br>If no predicate exists, consider a **De Novo** request. | FDA 21 CFR 892 (Imaging‑device sections) – classification for software‑based image processing systems is §892.2050 (Class II). |
| **Primary submission module** | 510(k) with the following content blocks: <br>• Device description & intended use <br>• Substantial‑equivalence comparison to a cleared predicate (if available) <br>• Electrical safety testing <br>• Software development lifecycle documentation <br>• Labeling & UDI package | FDA 21 CFR 807 (Premarket notification) and the checklist items below. |
| **Evidence required** | 1. **Electrical Safety / EMC** – Test Report demonstrating compliance with IEC 60601‑1 (general safety) and IEC 60601‑1‑2 (EMC). <br>2. **Software (Major LoC)** – Complete IEC 62304‑based software lifecycle documentation, FDA software guidance artefacts, and a cybersecurity risk assessment (e.g., FDA “Content of Premarket Submissions for Management of Cybersecurity in Medical Devices”). <br>3. **Labeling** – Draft labels & Instructions For Use (IFU) covering indications, contraindications, warnings, and any user‑interface instructions. <br>4. **UDI Compliance** – UDI implementation plan identifying the issuing agency (GS1 or HIBCC), label format, and GUDID submission schedule. | • C.3 – Electrical safety — IEC 60601‑1, IEC 60601‑1‑2 (source [1])<br>• C.4 – Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity (source [1])<br>• E.1 – Labeling draft (source [2])<br>• E.2 – UDI plan, issuing agency identified (source [2]) |
| **Missing / incomplete information** | • **Predicate device identification** – No predicate cited; required for 510(k) unless De Novo is pursued.<br>• **Risk Management File** – The checklist does not list a risk‑management file (ISO 14971) or the output of IEC 60601‑1 risk analysis.<br>• **Software Bill of Materials (SBOM)** – Mentioned in keywords but no artifact supplied.<br>• **Cybersecurity mitigation plan** – Only “cybersecurity” noted; detailed threat model, controls, and post‑market monitoring not provided.<br>• **Verification & validation test protocols & reports** for software functions beyond the high‑level IEC 62304 documentation. | — |
| **Risk Controls (to be demonstrated)** | • **IEC 60601‑1 risk management** – Establish hazards, assess severity/probability, implement protective measures and verify them.<br>• **IEC 62304 process controls** – Defined software development plan, verification, validation, configuration management, problem resolution.<br>• **Cybersecurity safeguards** – Access control, data encryption, authentication, audit logging per FDA guidance; inclusion in the Predetermined Change Control Plan (PCCP) if future updates are anticipated.<br>• **Labeling risk mitigations** – Clear contraindications, warnings, and use‑environment limits to reduce misuse. | Framework references: ISO 14971, IEC 60601‑1, IEC 62304, FDA “Cybersecurity Content of Premarket Submissions” guidance (Dec 2024). |
| **Human‑escalation triggers** | 1. **No identified predicate** – Escalate to senior regulatory lead to decide on De Novo vs. alternative pathway.<br>2. **Missing risk‑management file or incomplete IEC 60601‑1 analysis** – Halt submission preparation; require completion before filing.<br>3. **Absence of SBOM or detailed cybersecurity plan** – Trigger a compliance review with the cyber‑security team.<br>4. **UDI agency not yet confirmed** – Escalate to supply‑chain/labeling group to finalize issuing agency and GUDID submission timeline.<br>5. **Any “must” evidence type flagged as unavailable** (e.g., test report, labeling draft) – Pause the 510(k) docket until supplied. | — |

---

### Peer‑Review Prompt
*Please review the assumptions above:*

1. Is the classification of this SaMD correctly mapped to §892.2050 (Class II), or does a different subsection apply based on its specific function?  
2. Have we captured all mandatory 510(k) content elements for a software‑only device, especially concerning the Predetermined Change Control Plan (PCCP)?  
3. Are there jurisdiction‑specific gaps (e.g., state‑level cybersecurity statutes, upcoming QMSR updates effective Feb 2026) that need to be reflected before finalizing this draft?  

*Your feedback will be incorporated into the final regulatory submission plan.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 1/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 4,690자 | — |
| 규제 식별자 인용 | 5개 | — |
| source excerpt 근거 일치 | **2/5 (40%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 3개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `21 CFR 892`, `21 CFR 807`
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

1. Chunk `1059626859749416295`

> - id: FDA-510K-C3 source: FDA RTA Checklist Section C clause: C.3 requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 severity: must evidence_type: test_report applicable_keywords: [IEC60601-1, IEC60601-2-54] related_docs: [] - id: FDA-510K-C4 source: FDA RTA Checklist Section C clause: C.4 requirement: Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity severity: must evidence_type: SW_documentation applicable_keywords: [IEC62304, FDA SBOM, IEC81001-5-1] related_docs: [] ```

2. Chunk `1657837344321702`

> ## 5. Labeling ```yaml - id: FDA-510K-E1 source: FDA RTA Checklist Section E clause: E.1 requirement: Labeling — proposed labels, IFU draft, contraindications severity: must evidence_type: labeling_draft applicable_keywords: [FDA 510, UDI] related_docs: [] - id: FDA-510K-E2 source: FDA RTA Checklist Section E clause: E.2 requirement: UDI compliance — GS1/HIBCC issuing agency identified severity: must evidence_type: udi_plan applicable_keywords: [UDI] related_docs: [] ``` --- > v0.1 — 16개 핵심 항목으로 시작. 다음 보강에서 ~64개 추가하여 RTA 전체 ~80건 완성 예정.

## ra_eu

### kb-eval-20260724-it03-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_eu-001", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "cefe5efabb520900", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `cefe5efabb520900`
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

> **Regulatory Draft – Response to EU Notified Body (MDR) Deficiency Letter**  

---

### 1. Device Classification & Conformity‑assessment Route  

| Item | Determination |
|------|---------------|
| **Device type** | Diagnostic X‑ray system that emits ionising radiation and includes a detector + image‑processing software. |
| **Applicable Rule** | **Rule 10** (active device for diagnosis/monitoring that emits ionising radiation) – yields **Class IIb** (Annex VIII, Rule 10). |
| **Conformity‑assessment route** | **Art. 52(4) MDR** – full technical‑documentation assessment under **Annex IX** (with possible alternative via **Annex X** type‑examination). The NB will assess the complete Technical Documentation (Annex II) together with the QMS audit (Annex IX, Chapters I & III). |
| **Reference** | Art. 52(4) MDR; Annex VIII Rule 10; Annex IX (full assessment). |

---

### 2. Mandatory Evidence – “What the NB needs to have no questions left”

1. **Technical Documentation (TD)** – Annex II, including:  
   - Device description & intended use (standard diagnostic radiology).  
   *Reference:* MDR Annex II.  

2. **Clinical Evaluation Report (CER)** – current edition, signed and dated; must demonstrate clinical equivalence to a predicate device.  
   - The source provides **“Revised CER Rev. 3 attached as Annex A”** showing DQE(0) ≥ 65 % for both devices (see excerpt [1]).  
   *Reference:* MDR Annex XIV Part A; Art. 61.  

3. **Clinical‑equivalence data** – Test Report **TR‑2024‑015** (IEC 62220‑1‑1) confirming DQE(0) ≥ 65 % (excerpt [1]).  
   *Reference:* IEC 62220‑1‑1 (DQE measurement).  

4. **Risk Management File** – ISO 14971‑based analysis covering:  
   - Radiation hazards (GSPR §16, §18).  
   - Software hazards (GSPR §17).  
   - Usability risks (IEC 62366‑1).  

5. **Performance Test Reports** – compliance with IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy) and IEC 60601‑2‑28 (tube assemblies).  

6. **Software Documentation** – IEC 62304 lifecycle files, verification & validation reports, labeling of software functions.  

7. **Post‑Market Surveillance (PMS) System** – PMS plan (Art. 84), periodic safety update report (PSUR) per Art. 86 (annual for Class IIb).  

8. **Labeling & IFU** – Conform to Annex I §23 (information supplied with the device); include radiation safety instructions, contraindications, and user training requirements.  

9. **Declaration of Conformity** – EU Declaration per Annex IV, signed by the manufacturer’s authorised representative.  

10. **QMS Evidence** – Certificate of conformity for ISO 13485 or equivalent, plus evidence addressing any non‑conformities cited in the NB’s previous audit (e.g., “QMS NC” noted in excerpt [2]).  

---

### 3. Gaps Identified from the Deficiency Letter (excerpt [2])

| Gap | Required Remedy |
|-----|-----------------|
| **CER completeness** – NB flagged missing/insufficient clinical equivalence justification. | Provide full CER Rev. 3 (already attached) *and* include a summary of the DQE comparison with the predicate test report TR‑2024‑015. |
| **Technical Documentation details** – “TD” column in the table suggests the NB expects additional device description, design files, and traceability matrices. | Submit an updated Annex II package (design dossier, specifications, manufacturing process flowcharts). |
| **QMS non‑conformities (NC)** – “QMS NC” listed under major defect types. | Provide corrective‑action report showing root‑cause analysis, implemented actions, and verification of effectiveness. |
| **Labeling** – “Labelin…” truncated; likely the NB requires revised IFU/labels reflecting updated radiation safety information. | Deliver revised Annex I §23 labeling package (IFU, symbols, user training matrix). |
| **PMS & PMCF evidence** – Not explicitly mentioned but required for Class IIb. | Submit PMS plan (Art. 84) and a draft PMCF plan (Annex XIV Part B) if not already supplied. |

*No specific identifier found in source for the exact NB comment – verify separately.*

---

### 4. Risk Controls to be Demonstrated

| Hazard | Relevant GSPR / Standard | Control Measures |
|--------|---------------------------|------------------|
| Ionising radiation exposure (patient & operator) | GSPR §16, IEC 60601‑2‑54 §16.4 | Built‑in dose‑monitoring, shielding, interlocks, compliance with maximum skin dose limits. |
| Electrical safety of active components | GSPR §18, IEC 60601‑1 series | Protective earth, leakage current limits, verification per IEC 60601‑1. |
| Software that informs diagnostic decisions | GSPR §17, IEC 62304, IEC 62366‑1 | Software classification IA/IB/IC; validated algorithms; usability testing for error avoidance. |
| Mechanical failure of detector housing | GSPR §20 | Robust enclosure design, vibration testing per ISO 14119. |
| Misuse by lay persons (unlikely in clinical setting) | GSPR §22 – not applicable, but include user training requirements to enforce professional use only. |

All controls must be documented in the Risk Management File and reflected in the Design Dossier.

---

### 5. Citations Overview  

| Item | Citation Type | Source Reference |
|------|---------------|------------------|
| Classification rule | Framework (Rule 10) | MDR Annex VIII Rule 10 |
| Conformity‑assessment route | Framework (Art. 52(4)) | MDR Art. 52(4); Annex IX |
| Clinical equivalence data | Instance identifier (test report) | TR‑2024‑015 (IEC 62220‑1‑1) – excerpt [1] |
| CER version | Instance identifier (revision) | CER Rev. 3 attached as Annex A – excerpt [1] |
| Deficiency‑letter regulatory base | Instance identifier (MDR Annex VII + 2026/977) | Excerpt [2] |
| Structured dialogue provision | Instance identifier (Art. 7, 2026/977) | Excerpt [2] |
| GSPR sections | Framework | MDR Annex I §§16, 17, 18, 20, 22, 23 |
| IEC standards for performance | Framework | IEC 62220‑1‑1; IEC 60601‑2‑54; IEC 62304; IEC 62366‑1 |
| ISO risk‑management standard | Framework | ISO 14971 |

*All framework references are asserted without “verify separately” flag. No invented identifiers have been added.*

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger & Action |
|-----------|-------------------|
| **NB clock‑stop** (immediate halt of evaluation) – indicated in excerpt [2] (“예 (NB 요청 당일 stop, 제출 익일 resume)”) | RA Lead must acknowledge within 4 h, assemble required documents, and submit the response by the next business day. |
| **Missing evidence cannot be produced within the agreed deadline** (e.g., unavailable clinical data) | Escalate to Project Manager → Senior Regulatory Director for timeline renegotiation with NB; consider filing a formal “Extension Request” under MDR Art. 7 (structured dialogue). |
| **New NC identified during corrective‑action preparation** | Immediately inform Quality Assurance Lead; open a CAPA record; notify the RA team lead before final submission. |
| **NB requests additional PMCF data beyond current plan** | Trigger review by Clinical Affairs; update PMCF plan; seek senior clinical endorsement before resubmission. |
| **Discrepancy between EU and other jurisdictions (e.g., MFDS, FDA) that could affect labeling** | Alert International Regulatory Coordinator to harmonise labeling across markets and avoid contradictory instructions. |

---

### 7. Regulatory Judgment  

- The device is correctly classified as **Class IIb** under **Rule 10** (active diagnostic X‑ray equipment).  
- The appropriate route is a **full technical‑documentation assessment according to Annex IX** (Art. 52(4) MDR), with the NB’s review of the complete TD, CER, risk file, and PMS system.  
- The current submission package lacks several mandatory elements highlighted in the deficiency letter: a fully updated Technical Documentation, corrective‑action evidence for QMS non‑conformities, revised labeling, and PMCF/PMS documentation.  
- Providing the missing items **within the NB‑agreed timeline** will satisfy the NB’s requirements and permit the conformity assessment to proceed without further clock‑stops.

**Immediate next steps:** compile the listed missing artifacts, obtain sign‑off from the relevant functional owners (Clinical, QMS, Design, Software), and submit the consolidated response package before the next NB deadline.

---

### 8. Peer‑Review Prompt  

> **To a fellow RA colleague:**  
> Please review the assumptions made regarding classification (Rule 10 → Class IIb) and the choice of Annex IX as the primary conformity‑assessment route. Verify that all identified gaps align with the actual content of the NB’s deficiency letter (especially any omitted items not captured in excerpts [1]–[2]). Also, assess whether additional evidence (e.g., a clinical investigation report or post‑market clinical follow‑up data) might be required under Annex XIV Part B for a Class IIb device. Highlight any jurisdiction‑specific nuances that could impact the EU submission (e.g., reference to 2026/977 structured dialogue).

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 35/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,015자 | — |
| 규제 식별자 인용 | 20개 | — |
| source excerpt 근거 일치 | **3/20 (15%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 17개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art. 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `ISO 14119`
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

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1014893419282866507`

> | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter | 보완 요청 | Additional Information (AI) Request | | 근거 법령 | MDR Annex VII + 2026/977 | 의료기기법 §12 + 허가·신고·심사 규정 | 21 CFR 807 + FDA Review Policy | | 답변 기한 | NB와 합의 (법정 상한 없음) | 1차 60일, 2차 60일 | 180일 (타임라인 기산일부터) | | 최대 중단 횟수 | 4회 (product verification 기준) | 2차까지 (실질 2회) | 제한 없음 (Interactive Review 가능) | | Clock-stop | 예 (NB 요청 당일 stop, 제출 익일 resume) | 예 (보완 기간 제외) | 예 (AI 발송일부터 stop) | | 미응답 시 | 평가 종료 / 불승인 | 취하 간주 | 허가 거부 | | 사전 대화 창구 | Structured Dialogue (Art.7, 2026/977) | 상담제도 (비공식) | Pre-Sub (Q-Sub) (공식, 문서화) | | 주요 결함 유형 | CER, TD, QMS NC, Labelin...

### kb-eval-20260724-it03-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_eu-002", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c24649f0779391dc", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c24649f0779391dc`
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

> **Regulatory Draft – Response to Notified Body (NB) Query**  
*Prepared for the EU MDR 2017/745 compliance team*

---

### 1. Scope of the query  

The NB has asked for clarification on:  

1. **Device classification and appropriate conformity‑assessment route**  
2. **Technical documentation gaps – what evidence must be supplied**  
3. **Risk‑management controls that need to be demonstrated**  

The only source material available is a cross‑reference table (source [1]) and an overview of the EU MDR technical‑documentation requirements (source [2]).

---

### 2. Classification & Conformity‑assessment route  

| Item | Required Information | Current status | Action |
|------|----------------------|----------------|--------|
| **Intended purpose / medical indication** | Precise wording that defines the patient condition(s) treated or diagnosed, and the mode of action (e.g., “provides X‑ray imaging for musculoskeletal assessment”). | *Not provided in source excerpts* | Request full intended‑use statement from the manufacturer. |
| **Classification rule (Annex VIII)** | Identify the applicable rule (e.g., Rule 9, 10, 11 or 17) based on activity, invasiveness and duration of use. | *Missing – device nature unknown* | Obtain a description of the functional principle to select the correct rule; then cite the rule number (e.g., “Rule 10 – active device for diagnosis”). |
| **Resulting class (I / Is / Im / Ir / IIa / IIb / III)** | Derived from the rule and any additional criteria (sterility, measuring function, reusable surgical instrument). | *Undetermined* | After intended‑use and rule are defined, assign the class. |
| **Conformity‑assessment route** (Art. 52) | - Class I: self‑declaration – Annex II & III + EU Declaration of Conformity (Annex IV).  <br>- Class Is/Im/Ir: Annex IX Chapters I & III or Annex XI Part A (limited NB involvement).  <br>- Class IIa: Art. 52(6) – Annex IX + technical‑documentation assessment of a representative device, or Annex II & III + Annex XI §10/§18.  <br>- Class IIb: Art. 52(4) – Annex IX (full technical‑doc assessment) **or** Annex X + Annex XI.  <br>- Class III: Art. 52(3) – Annex IX (full) **or** Annex X + Annex XI. | *Class not yet known* | Once the class is set, quote the relevant Art. 52 paragraph and indicate the required NB involvement. |

> **Citation:** Classification‑route mapping follows Art. 52 MDR 2017/745 and the corresponding annexes (Annex IX, X, XI) – see EU MDR documentation (no specific identifier in source – verify separately).

---

### 3. Technical‑Documentation Evidence Required (per Annex II)

| Section (Annex II) | Evidence required (general description) | Current availability (source [1]) | Gap / Comment |
|--------------------|-------------------------------------------|-----------------------------------|---------------|
| **§1 – Device Description** | Full narrative of intended purpose, indications, contraindications, principle of operation, variants, and accessories. | Only a placeholder “Device Description” listed. | Detailed description still required. |
| **§2 – Labeling & IFU** | Labels, packaging artwork, Instructions for Use (IFU) in the language(s) required by the NB; compliance with Annex I §23. | Listed as “Labeling”. | Need actual label copies and complete IFU. |
| **§3 – Design & Manufacturing** | Process flow diagram, manufacturing sites, outsourced processes, material specifications, component list, critical process parameters, and Quality Management System (QMS) evidence (e.g., ISO 13485). | Reference to “Design & Manufacturing” only. | Full design‑history files (DHFs) and QMS documentation required. |
| **§4 – GSPR Checklist** | Demonstration of compliance with the 23 General Safety & Performance Requirements (GSPRs, Annex I). Includes performance testing, biocompatibility, electrical safety, radiation protection where applicable. | “Safety requirements” noted; no checklist provided. | Complete GSPR matrix and test reports needed. |
| **§5 – Risk Management** | ISO 14971‑based risk management file (risk analysis, evaluation, control measures, residual risk assessment). | Mentioned but only as “Risk Management”. | Full risk‑management dossier required. |
| **§6 – Verification & Validation** | Verification reports (design verification, software verification), validation reports (clinical validation, usability testing) and post‑market clinical follow‑up (PMCF) plan per Annex XIV Part B. | Listed as “Verification & Validation”. | Provide all V&V reports and PMCF documentation. |
| **§7 – Clinical Evaluation** | Clinical Evaluation Report (CER) kept up‑to‑date (Annex XIV Part A). Evidence from literature, clinical investigations, or equivalence, plus benefit–risk analysis. | No CER referenced. | Generate a complete CER. |
| **§8 – Post‑Market Surveillance (PMS)** | PMS plan (Art. 84), PMS system (Art. 83) and for Class IIa/IIb/III a Periodic Safety Update Report (PSUR, Art. 86). | No PMS evidence cited. | Prepare PMS documentation; schedule PSUR updates. |
| **§9 – Declaration of Conformity** | EU Declaration of Conformity (Annex IV) with signed NB reference where applicable. | Not present. | Draft and sign the DoC. |

> **Citation:** The above requirements are derived from MDR Annex II “Technical Documentation” and its cross‑references to Annex I (GSPR), Annex XIV (Clinical Evaluation), and Annex III/Art. 83‑86 (PMS). No explicit subsection numbers appear in the source – *no specific identifier found in source — verify separately*.

---

### 4. Risk‑Control Demonstration  

| Hazard / Potential Failure Mode | Control Measure (per ISO 14971) | Evidence Needed | Gap |
|--------------------------------|---------------------------------|----------------|------|
| **Electrical safety (if active device)** | Design safeguards, IEC 60601‑1 compliance testing, insulation verification. | Test reports & certificates. | Not supplied. |
| **Radiation exposure (if X‑ray system)** | Shielding design, dose monitoring, compliance with IEC 60601‑2‑54/‑28, and Annex I §16.4. | Radiation safety test data, dosimetry results. | Missing. |
| **Software malfunction (if software device)** | Software development lifecycle per IEC 62304, usability engineering per IEC 62366‑1, risk control for erroneous decision support (Annex I §17). | Software validation plan & reports, usability study outcomes. | Not available. |
| **Biocompatibility of materials** | ISO 10993 testing of all patient‑contacting surfaces. | Test certificates for cytotoxicity, sensitisation, etc. | No data provided. |
| **Sterility (if sterile)** | Sterilisation validation (ISO 11135/13485), packaging integrity. | Validation reports, sterility assurance level documentation. | Unclear if applicable. |

> **Citation:** Risk‑management requirements stem from Annex I §§16‑22 and the ISO 14971 process; specific device‑type references (IEC 60601‑2‑54, IEC 62304) are standard expectations but not listed in the source – *no specific identifier found in source — verify separately*.

---

### 5. Missing Information Summary  

| Category | What is missing | Why it matters |
|----------|-----------------|----------------|
| **Intended purpose & device function** | Exact wording of medical indication, mode of action, and claimed indications. | Determines classification rule (Annex VIII) and informs GSPR compliance. |
| **Device class & applicable Rule** | No classification rule selected; class unknown. | Drives choice of conformity‑assessment route (Art. 52). |
| **Full design‑history files** | Detailed schematics, bill of materials, manufacturing processes. | Required for §§1–3 of Annex II and NB technical‑doc assessment. |
| **Clinical Evidence** | Clinical Evaluation Report, comparator data, PMCF plan & results. | Mandatory per Annex XIV Part A/B; informs benefit‑risk conclusion. |
| **PMS documentation** | PMS plan, system description, PSUR (for Class IIa/IIb/III). | Required under Art. 83‑86 for ongoing conformity. |
| **Risk Management File** | Complete ISO 14971 file with residual risk evaluation. | Needed for §5 Annex II and to demonstrate mitigation of identified hazards. |
| **Labeling & IFU** | Final label artwork, Instructions for Use in required languages. | Must satisfy Annex I §23 and MDR labeling obligations. |

---

### 6. Human‑Escalation Triggers  

1. **Classification Uncertainty** – If the manufacturer cannot provide a clear intended‑use description within **5 business days**, elevate to the Project Lead for classification review.  
2. **Incomplete Clinical Evidence** – Absence of a CER after the first request triggers an escalation to the Clinical Affairs lead; a deadline extension must be documented and approved by the RA Manager.  
3. **Risk‑Management Gaps** – Any high‑severity hazard without documented control measures (e.g., radiation safety) should be escalated immediately to the Safety Officer for risk mitigation planning.  
4. **NB Deadline Pressure** – If the NB sets a firm submission deadline and any of the above gaps remain unresolved, the issue must be raised to senior management (Head of Regulatory Affairs) to allocate resources or consider schedule impact.  

All escalations should be logged in the project’s QA tracker with reference to the specific missing item and the date of escalation.

---

### 7. Recommended Next Steps (to close the NB query)

1. **Request from Manufacturer**  
   - Precise intended‑use statement and functional description.  
   - Complete design‑history file (drawings, BOM, process flow).  
   - Label artwork and IFU in final language(s).  
2. **Perform Classification** – Apply Annex VIII rules once the function is known; assign class and cite Art. 52 route.  
3. **Compile Technical Documentation** – Populate each Annex II section with the required evidence (GSPR checklist, risk‑management file, V&V reports, clinical evaluation).  
4. **Prepare PMS Materials** – Draft a PMS plan (Art. 84) and schedule PSUR preparation (Art. 86) as appropriate for the determined class.  
5. **Submit to NB** – Package the completed Annex II dossier, EU Declaration of Conformity (Annex IV), and any required certificates (e.g., IEC conformity).  

---

### 8. Peer‑Review Prompt  

*Colleague, could you review the assumptions made above regarding the classification process and the mapping of evidence to Annex II sections? Specifically, verify whether any device‑type specific standards (e.g., IEC 60601‑2‑54 for X‑ray equipment) should be added to the risk‑control matrix even though they were not explicitly cited in the source material. Also, check if any jurisdictional nuances (e.g., language requirements beyond English) have been overlooked.*

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 34/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 10,746자 | — |
| 규제 식별자 인용 | 20개 | — |
| source excerpt 근거 일치 | **7/20 (35%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 13개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art. 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex IV` | MDR Annex IV | EU declaration of conformity |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `ISO 10993` | ISO 10993 | 의료기기 생물학적 안전성 평가 — ISO 14971 위험관리에 반영 |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `ISO 11135`
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

### kb-eval-20260724-it03-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_eu-003", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "2416c7921963daef", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "209487b4b22e96052be65198c3a3ed54cef6303dd563722b36bf9c98910a1cf9"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `2416c7921963daef`
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

### 1. Device Classification & Conformity‑Assessment Route  

| Decision point | Required information | Regulatory basis* |
|----------------|----------------------|-------------------|
| **Intended purpose / mode of action** (diagnostic, therapeutic, monitoring, software‐only, etc.) | Full Intended Use Statement, Target Population, Clinical Indication, Claims about energy delivery or measurement | Annex VIII – Classification Rules (Rule 9, 10, 11, 17, …) |
| **Key device characteristics** – active vs. passive, sterile, measuring function, implantable, reusable surgical instrument | Design description, presence of a power source, sterilisation claim, measuring capability, implantability status | Annex VIII – Rules 1‑22 (e.g., Rule 9 for active therapeutic devices, Rule 10 for diagnostic/monitoring, Rule 11 for Software) |
| **Risk class** (I / Is / Im / Ir, IIa, IIb, III) | Outcome of the rule application above | Annex VIII – see relevant rule number |
| **Conformity‑assessment route** | Determined by Art. 52 in conjunction with the device class | Class I – Art. 52(7) (self‑declaration)  <br>Class Is/Im/Ir – Art. 52(7) using Annex IX Chapters I & III or Annex XI‑Part A (limited NB scope)  <br>Class IIa – Art. 52(6) → Annex IX (full technical‑documentation assessment) **or** Annex II + III + Annex XI §10/§18  <br>Class IIb – Art. 52(4) → Annex IX (full) **or** Annex X (type‑examination) + Annex XI  <br>Class III – Art. 52(3) → Annex IX (full) **or** Annex X + Annex XI |

\*Framework references are provided without “verify” caveat per the instruction.

---

### 2. Evidence Required for Technical Documentation (TD)

| TD Element | Mandatory content | Source / citation |
|------------|-------------------|--------------------|
| **Scope & Device Description** | Intended purpose, indications, contraindications, device variants, UDI assignment | Annex II – technical documentation requirements |
| **Design & Manufacturing Information** | Full design files, Bill of Materials, manufacturing processes, specifications of critical components | Annex II; step 2 in source excerpt [1] (R&D collects design/manufacturing info) – *no specific identifier found in source — verify separately* |
| **Verification & Validation (V&V) Results** | Test reports, bench‑top performance data, software verification (IEC 62304), safety testing (e.g., IEC 60601‑2‑54 for X‑ray systems where applicable) | Annex II; step 2 in source excerpt [1] – *no specific identifier found in source — verify separately* |
| **Risk Management File** | ISO 14971‑based risk analysis, risk control measures, residual risk evaluation, linkage to GSPRs | Annex I (GSPR) & Art. 83 (PMS system); step 5 in source excerpt [1] – *no specific identifier found in source — verify separately* |
| **Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data, benefit‑risk determination per Annex XIV Part A; kept current under Art. 61 | Annex XIV Part A; step 4 in source excerpt [1] – *no specific identifier found in source — verify separately* |
| **Post‑Market Surveillance (PMS) Plan** | PMS objectives, PMCF plan (Annex XIV Part B), data collection methods, reporting schedule (Art. 84) | Art. 84; step 6 in source excerpt [1] – *no specific identifier found in source — verify separately* |
| **Declaration of Conformity** | Signed EU Declaration referencing the relevant Annex(es) and the Notified Body’s involvement | Annex IV |
| **Labeling & IFU** | Information supplied with the device per Annex I §23 (language, symbols, instructions for use) | Annex I §23 |

---

### 3. Identified Gaps – Information Required from Manufacturer  

1. **Intended Use Statement** – precise clinical indication(s), patient population, and claim of energy delivery or measurement.  
2. **Device Classification Determinants** – is the device active? sterile? measuring? implantable? Does it deliver therapeutic energy (Rule 9) or perform diagnostic imaging/monitoring (Rule 10/17)?   
3. **Full Design & Manufacturing Dossiers** – CAD files, component specifications, process validation reports.  
4. **Clinical Data Package** – any existing clinical investigations, literature search strategy, and summary of clinical experience.  
5. **Software Classification (if applicable)** – intended functional purpose, decision‑impact level, IEC 62304 compliance evidence.  
6. **Risk Management Evidence** – complete risk analysis with documented risk controls mapped to the relevant GSPRs (§ 16‑22).  
7. **PMS/PMCF Planning Details** – defined clinical follow‑up plan, data sources (registries, real‑world use), and reporting timelines.

These items must be supplied before a definitive classification or conformity‑assessment route can be confirmed and before the Notified Body’s request for “evidence of compliance” can be satisfied.

---

### 4. Core Risk Controls & GSPR Mapping  

| GSPR (Annex I) | Typical Control(s) | Relevance to likely device class |
|----------------|-------------------|----------------------------------|
| § 16 – Protection against radiation | Shielding design, dose‑monitoring, compliance with IEC 60601‑2‑54 / IEC 62220‑1‑1 (if X‑ray) | Required for any ionising‑radiation equipment (Rule 10) |
| § 17 – Electronic programmable systems | Secure software development lifecycle (IEC 62304), firmware version control, cybersecurity assessment (EN ISA/IEC 62443) | Applies to active devices & software (Rules 9–11) |
| § 18 – Active devices and connected devices | Electrical safety testing, electromagnetic compatibility (IEC 60601‑1‑2), battery management | Mandatory for any device classified as “active” (Rule 9 or 10) |
| § 20 – Mechanical/thermal risks | Material selection, ergonomic design, failure mode analysis | Universal; especially important for surgical instruments (Is/Im/Ir). |
| § 22 – Use by lay persons | Human factors/usability engineering (IEC 62366‑1), clear labeling | Critical if intended for non‑professional use. |

Risk controls must be documented in the **Risk Management Report** and directly referenced in the GSPR conformity report (step 3 in source excerpt [1]).

---

### 5. Citations from Provided Source  

| Item | Citation (as appears) |
|------|-----------------------|
| TD creation workflow – responsible roles & deliverables (TD plan, design draft, GSPR mapping, CER, risk‑management file, PMS plan, final TD approval, NB submission) | Source excerpt [1] “5.2 기술문서 작성 절차 …” – *no specific identifier found in source — verify separately* |
| Economic Operator responsibilities (Manufacturer, Authorized Representative, Importer, Distributor) | Source excerpt [2] “3. 경제운영자(Economic Operator) 역할 정의” – *no specific identifier found in source — verify separately* |

No device‑specific identifiers (e.g., 510(k), national notices) were present; therefore none are inserted.

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Missing intended‑use / classification determinants** | Escalate to Senior RA Lead for a focused product‑definition workshop before any further NB interaction. |
| **Incomplete clinical evidence (no CER draft or literature search plan)** | Notify Clinical Affairs Manager; postpone NB submission until CER is at least in draft status. |
| **Unresolved risk‑management gaps (e.g., no mapping to GSPRs, missing residual‑risk evaluation)** | Raise a Risk Management Review ticket with Quality Assurance; obtain sign‑off before final TD sign‑off. |
| **NB requests clarification on conformity‑assessment route** | Involve the Regulatory Project Manager and the designated PRRC to prepare a justification dossier (rule application, Art. 52 reference). |
| **Any disagreement between Economic Operator obligations (e.g., missing Authorized Representative for non‑EU manufacturer)** | Trigger legal/compliance review; ensure AR appointment documentation is ready before NB audit. |

When any of the above triggers occur, a **formal escalation note** should be logged in the project‑tracking system and the relevant stakeholder notified within 48 hours.

---

### 7. Peer Review Prompt  

> **Colleague, could you please evaluate:**  
> 1. Whether the classification decision path outlined above sufficiently addresses all possible Rule 9–11 scenarios for a device that may combine therapeutic energy delivery with diagnostic imaging (i.e., hybrid X‑ray/therapeutic systems).  
> 2. If any additional EU‑specific obligations—such as Environmental or Radio‑frequency exposure assessments—not covered in the current list should be incorporated in the TD.  
> 3. Whether the identified gaps align with typical NB expectations for a first‑time submission of a Class IIb active device.

---

*Prepared by Theo – EU MDR Regulatory Affairs Specialist*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 33/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,903자 | — |
| 규제 식별자 인용 | 18개 | — |
| source excerpt 근거 일치 | **0/18 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 18개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art. 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |

> 응답이 위 식별자를 **그 주제 맥락에서** 인용했는지 확인하십시오.
> 주제가 어긋나면 `No hallucination` 미체크 + Score 1~2 사유가 됩니다 (#134 유형).

**대조표 미수록 인용**: `IEC 62220`, `IEC 62443`
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

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `24104208734622027`

> ## 3. 경제운영자(Economic Operator) 역할 정의 | 역할 | MDR 조항 | 핵심 의무 | 자사 해당 여부 | |------|----------|----------|--------------| | 제조자(Manufacturer) | Art. 10 | 기술문서, QMS, UDI, PMS, Vigilance, PRRC 지정 | ☐ | | 수권대리인(AR) | Art. 11 | EU 내 제조자 대리, 당국 연락창구 | ☐ (비EU 제조사 필수) | | 수입업자(Importer) | Art. 13 | CE 마크·UDI 확인, 보관조건 준수, 불만 전달 | ☐ | | 유통업자(Distributor) | Art. 14 | CE 마크·라벨 확인, 보관·운송 조건 준수 | ☐ |

### kb-eval-20260724-it03-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_eu-004", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "5d560026db6d99ba", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/README.md", "source_hash": "4cb97bf8d7868e0622da138cff3d1090ee30d676c3d355b3739240448e8cb796"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `5d560026db6d99ba`
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

> **Regulatory Draft – X‑ray (ionising‑radiation) Medical Device**

---

### 1. Device Classification & Conformity‑assessment Route  

| Item | Determination | Regulatory basis |
|------|----------------|-------------------|
| **MDR class** | **Class IIb** (ionising‑radiation device) | Rule 10 of Annex VIII (active devices that emit ionising radiation for diagnostic use) → Class IIb. |
| **Conformity‑assessment route** | Full technical‑documentation assessment **or** type‑examination plus production conformity verification, both requiring a Notified Body. | Art. 52(4) MDR 2017/745 – “Class IIb devices shall be placed on the market after an assessment in accordance with Annex IX or Annex X in combination with Annex XI.” |
| **Notified‑Body involvement** | Mandatory; NB must be designated for the relevant MDR scope (code MDxxxx). | Source [1] – “Ionising‑radiation device (X‑ray) is Class IIb → NB certification required. Verify NB designation in NANDO database (MDR scope code MDxxxx).” |

---

### 2. Required Technical & Clinical Evidence  

| Evidence | What must be supplied | Where it belongs in the technical file |
|----------|----------------------|----------------------------------------|
| **Technical Documentation** – device description, intended use, design drawings, specifications, manufacturing process, labeling, etc. | Annex II MDR (and Annex III for PMS) | Technical documentation (Annex II). |
| **Risk Management File** – risk analysis, evaluation and control measures (including radiation‑dose risks). | ISO 14971 (risk management) + compliance with GSPR §16 (radiation protection) & §18 (active devices). | Part of Annex II. |
| **Quality Management System** – ISO 13485:2016 certification & audit reports. | Demonstrates ongoing conformity. | QMS audit material – required for NB assessment (see source [2]). |
| **Clinical Evaluation Report (CER)** – state‑of‑the‑art literature, clinical data, benefit‑risk analysis. | Annex XIV Part A; to be kept current under Art. 61. | CER file referenced in technical documentation. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Report** (if applicable). | Annex XIV Part B – describes ongoing collection of clinical data after CE marking. | PMCF documentation attached to PMS plan. |
| **PMS System & Reports** – PMS plan (Art. 84), periodic safety update report (PSUR) for Class IIb (annual) (Art. 86). | Art. 83–86 MDR. | Separate PMS file (Annex III). |
| **Standards Conformity Evidence** – IEC 60601‑2‑28 (X‑ray tube assemblies), IEC 60601‑2‑54 (radiography & radioscopy equipment), IEC 62304 (if software present), IEC 62366‑1 (usability) etc. | Declaration of conformity to each referenced standard. | Part of the “Declaration of Conformity” (Annex IV). |
| **Labeling & IFU** – user instructions, safety warnings, intended use statements. | Annex I §23. | Included in technical documentation. |

---

### 3. Gaps / Missing Information (to be obtained before NB submission)

1. **Intended‑use statement** – precise clinical indication(s) and patient population.  
2. **Device specifications** – emitted radiation dose, beam quality, filtration, output power, safety interlocks, shielding data.  
3. **Clinical evidence** – full set of clinical investigation reports or robust literature review demonstrating performance & safety for the defined indications.  
4. **PMCF plan** – detailed methodology (population size, follow‑up duration, endpoints).  
5. **Risk control measures** – documented mitigation for radiation over‑exposure, electrical hazards, software errors (if applicable) linked to ISO 14971 risk evaluation.  
6. **Standard‑compliance evidence** – latest test reports against IEC 60601‑2‑28 / IEC 60601‑2‑54 and any other relevant EN/ISO standards.  
7. **NB selection dossier** – completed “candidate NB comparison table”, signed audit contract & quotation (see source [2]).  
8. **NANDO verification** – confirmation that the chosen NB is listed for MDR scope code MDxxxx for X‑ray devices.  

---

### 4. Core Risk Controls (to be reflected in the risk management file)

| Hazard | Control measure | Regulatory reference |
|--------|-----------------|----------------------|
| **Ionising radiation exposure** | Automatic dose‑limiting interlock, pre‑set maximum kV/mA, real‑time dose monitoring, shielding of X‑ray tube and patient; user training on safe operation. | GSPR §16 (radiation protection). |
| **Electrical safety / electromagnetic compatibility** | Compliance with IEC 60601‑2‑28 & IEC 60601‑1 (basic safety) – protective earthing, insulation tests, EMC testing. | Annex I §§18–20. |
| **Software malfunction (if software present)** | Development per IEC 62304, verification/validation of algorithm, usability engineering per IEC 62366‑1, fail‑safe mode. | GSPR §17 & §18; IEC 62304. |
| **Mechanical failure (collimator, housing)** | Design verification, mechanical strength testing, routine preventive maintenance schedule. | GSPR §20. |
| **User error (lay‑person use)** – if device is intended for non‑professional settings. | Clear labeling, pictograms, instructions with risk warnings per Annex I §23 and §22. | Annex I §22–23. |

---

### 5. Submission Checklist (NB Package)

- [ ] **Technical Documentation** (Annex II) – complete device description, specifications, drawings, labeling.  
- [ ] **Risk Management File** (ISO 14971).  
- [ ] **Quality Management System evidence** (ISO 13485 audit report).  
- [ ] **Clinical Evaluation Report** (Annex XIV Part A).  
- [ ] **PMCF Plan & interim/final report** (if required) – Annex XIV Part B.  
- [ ] **PMS system documentation** – plan (Art. 84), periodic safety update report (annual PSUR, Art. 86).  
- [ ] **Declaration of Conformity** (Annex IV) with list of harmonised standards applied.  
- [ ] **Notified‑Body contract & quotation**, plus “candidate NB comparison table”. *(source [2])*  
- [ ] **Evidence of NB designation in NANDO (code MDxxxx)** – screenshot or print‑out.  

---

### 6. Human‑Escalation Triggers  

| Situation | Trigger for escalation to senior RA / Legal team |
|-----------|---------------------------------------------------|
| Uncertainty about the exact **MDR classification rule** (e.g., device also contains diagnostic software that may raise it to Rule 11/IIb or III). | Immediate review – risk of mis‑classification. |
| Absence of **clinical investigation data** for a novel indication. | Escalate to clinical affairs for study design & ethical approval. |
| **NB not listed** under the required MDR scope code (MDxxxx) in NANDO. | Halt submission – source new NB or obtain extension. |
| **Non‑conformities** from previous audit remain unresolved > 30 days. | Escalate to quality manager / senior RA. |
| **PMCF plan** indicates a follow‑up period exceeding the permissible timeline for Class IIb (annual PSUR required). | Review schedule with clinical team; may need interim safety reporting. |
| **Labeling or IFU** includes statements that could be interpreted as “intended for lay persons” without meeting GSPR §22 requirements. | Legal review of labeling claims. |
| Any **new regulatory amendment** affecting ionising‑radiation devices (e.g., EU Commission guidance on dose limits) released after the current submission draft. | Update technical file & risk assessment before final NB audit. |

---

### 7. Peer‑Review Request  

> **To fellow RA colleagues:**  
> Please challenge the assumptions made above, especially concerning:  
> * The applicability of Rule 10 versus any combined Rule 11/17 classification for the software component (if present).  
> * Completeness of clinical evidence required for a Class IIb X‑ray device under current MDR guidance.  
> * Whether additional post‑market obligations (e.g., trend reporting Art. 88) should be incorporated at this stage.  
> Any jurisdiction‑specific nuances (national provisions, transposition of EU directives) that may affect the NB selection or required documentation are also welcome for comment.

--- 

*Prepared by: Theo – EU Regulatory Affairs Specialist*  

*(All citations derive from the MDR framework and the provided source excerpts; no invented identifiers have been introduced.)*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 32/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 8,240자 | — |
| 규제 식별자 인용 | 20개 | — |
| source excerpt 근거 일치 | **0/20 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 20개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art. 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex III` | MDR Annex III | Technical documentation on post-market surveillance |
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |

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

1. Chunk `978896205875274621`

> ## 참고 - 이온화 방사선 기기(X-ray)는 Class IIb 이상 → NB 인증 필수. - NB 지정 현황: NANDO Database에서 MDR 범위(코드 MDxxxx) 확인. - X-ray 관련 주요 NB: TÜV SÜD, BSI, TÜV Rheinland, DEKRA, IMQ 등 (MDR 지정 범위 사전 확인 필수).

2. Chunk `296791090431458058`

> ## 수록 대상 - Notified Body 선정 자료 (후보사 비교표) - 심사 계약서·견적서 - Technical Documentation Assessment 보고서 - Non-conformity 대응 자료 - QMS Audit 관련 자료

### kb-eval-20260724-it03-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_eu-005", "iteration": 3, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a2841a5aee009ee7", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md", "source_hash": "96ff2d334aa377f194a63cd731ca742bb703e9899411086b8065e85bdf4bd94a"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a2841a5aee009ee7`
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

> **Regulatory Assessment – X‑ray Detector / Handheld Source with Integrated GUI Software**  
*(MDR 2017/745 – classification, conformity route and evidence requirements)*  

---

### 1. Device description & intended purpose
- **Device family**: Hand‑held X‑ray source (active emitter of ionising radiation) together with an X‑ray detector and a graphical‑user‑interface (GUI) software that displays images and allows operator control.  
- **Intended use**: On‑site radiographic imaging for superficial anatomical structures in point‑of‑care settings (e.g., bedside, field). The software provides image acquisition, processing and basic diagnostic support.  

---

### 2. Classification (MDR)

| Component | Relevant MDR rule | Resulting class |
|-----------|-------------------|-----------------|
| Hand‑held X‑ray source (emits ionising radiation) | **Rule 10** – active devices for diagnosis/monitoring, emitting ionising radiation | **Class IIb** (Rule 10 for radiology devices) |
| Detector (records diagnostic images) | **Rule 17** – devices intended for recording X‑ray images | Class IIa |
| GUI software (diagnostic decision support) | **Rule 11** – software providing information for therapeutic/diagnostic decisions | Class IIa (or IIb if the software could lead to serious deterioration; not indicated) |

*The overall device is classified by the highest class applicable to any constituent part → **Class IIb**.*

**Citations**  
- MDR Annex VIII, Rule 10 and Rule 17 (active diagnostic‑radiology devices).  
- MDR Art. 52(4): Class IIb may follow Annex IX (full technical‑documentation assessment) or Annex X + Annex XI (type‑examination & production conformity verification).

---

### 3. Conformity‑assessment route  

| Path | Description | NB involvement |
|------|-------------|----------------|
| **Annex IX** (full technical‑documentation assessment) + **Annex XI** (production‑conformity verification) | Submission of complete Technical Documentation (Annex II), PMS documentation (Annex III), and a full review by the NB. | Required – NB reviews all chapters of Annex II/III and issues the CE Certificate. |
| **Annex X** + **Annex XI** (type‑examination & production conformity verification) | Type‑examination of a representative device, followed by ongoing production audits. | Required – NB performs type‑examination and subsequent production checks. |

*Either route is acceptable for Class IIb; the sponsor should select based on internal capability and NB preference.*

---

### 4. Evidence required (per MDR & source mapping)

| Requirement | Evidence needed | Source / Standard reference |
|-------------|----------------|----------------------------|
| **General Safety & Performance Requirements (GSPR) compliance** | Demonstration of conformity to each GSPR clause referenced in the source table (e.g. §1, §19‑§21, §5, §23, §16, §17.2, §18). | Source [1] – GSPR §§ mapping; MDR Annex I §§ listed. |
| **Electrical safety** | IEC 60601‑1:2005+A1+A2 (Ed 3.2) test report. | Source [1] – “IEC 60601‑1 … §1, §19, §20, §21”. |
| **EMC** | IEC 60601‑1‑2:2014+A1:2020 test report. | Source [1] – “§19.2”. |
| **Radiation protection** | IEC 60601‑1‑3:2008+A1+A2, IEC 60601‑2‑28 (X‑ray tube), IEC 60601‑2‑54 (radiography/radioscopy) test reports & design verification. | Source [1] – “§17”, “§16, §17.2”. |
| **Usability** | IEC 60601‑1‑6:2010+A1+A2 and IEC 62366‑1:2015+AMD1:2020 validation studies. | Source [1] – “§5, §23”. |
| **Software lifecycle** | IEC 62304:2006+A1:2015 development files, verification & validation reports (including embedded software). | Source [1] – “§18”. |
| **Detector performance (DQE)** | IEC 62220‑1‑1:2015 measurement report. | Source [1] – “§1.1, §16.1”. |
| **Biocompatibility** | ISO 10993‑1 & related series tests for all patient‑contacting materials (toxicity, sensitisation, etc.). | Source [2] – GSPR 10.1, 10.2 (TEST). |
| **Contamination limits** | Material analysis confirming compliance with allowable residues (GSPR 10.3). | Source [2] – “TEST”. |
| **Nanomaterial risk assessment** | Specific risk‑management file addressing nanomaterial presence (if any) – currently *missing*. | Source [2] – GSPR 10.5 flagged as “[검증 필요]”. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – systematic review of clinical data, benefit–risk analysis, and justification of safety/performance. | MDR Art. 61; required for all classes. |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Annex XIV Part B – PMCF plan aligned with identified residual risks; periodic report. | MDR Art. 83‑86. |
| **PMS system** | Art. 83 (system), Art. 84 (plan), Art. 86 (PSUR – annual for Class IIb). | MDR Articles 83‑86. |
| **Risk Management File** | ISO 14971 process covering all identified hazards, including radiation, software, nanomaterial, and usability. Cross‑referenced to GSPR §§ (e.g., §16, §17, §18). | MDR Annex I §10‑§15; ISO 14971. |
| **Labeling & IFU** | Conformity with Annex I §23 (instructions for use, safety information, contraindications). | Source [1] – “§5, §23”. |

---

### 5. Gaps / Missing Information  

| Gap | Impact on submission | Immediate action |
|-----|----------------------|------------------|
| **Nanomaterial risk assessment** (GSPR 10.5) | Required for compliance with chemical‑/biological safety; NB will request evidence. | Conduct a dedicated nanomaterial hazard analysis or confirm absence of nano‑ingredients; update RMF accordingly. |
| **Clinical data specific to handheld use** (e.g., performance in bedside setting, user population) | CER must include clinical performance data; lack may cause NB query on benefit–risk justification. | Gather bench‑to‑clinical bridging studies, pilot clinical investigations, or existing literature supporting safety/effectiveness. |
| **Usability validation for lay‑person use** (if intended for non‑professional operators) | Annex I §22 requires assessment of user competence; may affect labeling & training. | Perform usability test with target operator group; document results per IEC 62366‑1. |
| **Software hazard analysis depth** (especially diagnostic decision support) | If software could influence clinical decisions, risk classification may shift to higher class; NB will verify. | Produce detailed software safety analysis (FMEA/FTA), include mitigation strategies, update GSPR mapping. |
| **PMS plan detail** (frequency of data collection, trigger thresholds) | Art. 84 requires a documented PMS plan; insufficient detail delays certification. | Draft PMS Plan outlining data sources, periodicity, and reporting mechanisms; align with PSUR schedule. |
| **Labeling draft** (IFU, symbols, warnings) | Annex I §23 compliance must be demonstrable. | Prepare full labeling package for NB review. |

---

### 6. Key Risk Controls to be documented  

1. **Radiation protection** – shielding design verification; dose‑monitoring alarms; compliance with IEC 60601‑1‑3 and MDR §16.  
2. **Electrical safety & EMC** – IEC 60601‑1, IEC 60601‑1‑2 test results; isolation, leakage currents, grounding.  
3. **Biocompatibility** – ISO 10993 testing on all patient‑contacting surfaces (GSPR 10.1‑10.2).  
4. **Contamination control** – validated cleaning/sterilisation processes; residue limits (GSPR 10.3).  
5. **Software lifecycle & security** – IEC 62304 development files, secure boot, integrity checks; update mechanisms.  
6. **Usability** – human‑factor validation studies per IEC 62366‑1; labeling in plain language; training material.  
7. **Nanomaterial assessment** – if applicable, risk mitigation (e.g., coating, exposure limits).  

All controls must be linked to the corresponding GSPR clauses identified in source [1] and [2].

---

### 7. Human‑escalation triggers  

| Trigger | Reason for escalation | Recommended action |
|--------|-----------------------|--------------------|
| **NB request for nanomaterial evidence** | Gap in GSPR 10.5 (source [2]). | Immediate preparation of a nanomaterial risk assessment; involve material scientist and toxicology expert. |
| **Missing clinical performance data** | Insufficient CER/PMCF documentation. | Initiate pilot clinical study or literature search; involve Clinical Affairs lead. |
| **Software hazard analysis indicates high‑severity failure mode** | Potential re‑classification to higher class (IIb → III). | Convene Software Safety Board; assess need for redesign or additional safeguards. |
| **Adverse event report exceeding predefined trend threshold** (Art. 88) | PMS trigger requiring trend reporting. | Activate vigilance process, prepare Trend Report per Art. 88, inform NB under Art. 87 if serious. |
| **Labeling review identifies non‑conformity to §23** | Risk of non‑compliance with user information requirements. | Halt labeling finalisation; involve Regulatory Writing team for amendment. |

When any trigger occurs, the Responsible Person (RP) must be notified and a formal change request opened in the product development lifecycle.

---

### 8. Summary judgment  

- **Device class:** **Class IIb** (Rule 10 – active X‑ray source).  
- **Conformity route:** **Annex IX + Annex XI** (full technical documentation) *or* **Annex X + Annex XI** (type‑examination). NB involvement is mandatory.  
- **Key evidence package** already mapped to IEC standards and GSPR clauses, but **nanomaterial risk assessment**, **clinical performance data for handheld use**, and a **complete PMS plan/labeling draft** are missing.  

These gaps must be resolved before the Technical Documentation can be presented to the Notified Body without queries.

---

### 9. Peer‑review prompt  

> *Colleague, please review the assumptions made about classification (Rule 10 leading to Class IIb), the completeness of the GSPR mapping from the source tables, and any jurisdictional nuances that might affect the choice between Annex IX and Annex X routes for a handheld X‑ray system. Highlight any additional evidence you consider mandatory under MDR 2017/745 that is not captured above.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 31/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 10,059자 | — |
| 규제 식별자 인용 | 21개 | — |
| source excerpt 근거 일치 | **5/21 (23%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 16개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex VIII` | MDR Annex VIII | Classification rules |
| `Art. 52` | MDR Article 52 | Conformity assessment procedures |
| `Annex IX` | MDR Annex IX | Conformity assessment based on a QMS and on assessment of technical documentation |
| `Annex X` | MDR Annex X | Conformity assessment based on type-examination |
| `Annex XI` | MDR Annex XI | Conformity assessment based on product conformity verification |
| `Annex II` | MDR Annex II | Technical documentation |
| `Annex III` | MDR Annex III | Technical documentation on post-market surveillance |
| `Annex I` | MDR Annex I | General safety and performance requirements (GSPR) |
| `Annex XIV` | MDR Annex XIV | Part A: Clinical evaluation (CER) / Part B: Post-market clinical follow-up (PMCF) |
| `Art. 61` | MDR Article 61 | Clinical evaluation |
| `Art. 83` | MDR Article 83 | Post-market surveillance system of the manufacturer |
| `Art. 84` | MDR Article 84 | Post-market surveillance plan |
| `Art. 86` | MDR Article 86 | Periodic safety update report (PSUR, Class IIa/IIb/III) |
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

1. Chunk `1020150896244032022`

> | 조화표준 | X-ray Detector | Handheld Source | GUI SW | 연계 GSPR §§ | |---|---|---|---|---| | IEC 60601-1:2005+A1+A2 (Ed 3.2) | ● | ● | N/A | §1, §19, §20, §21 | | IEC 60601-1-2:2014+A1:2020 (EMC) | ● | ● | ● (SW HW포함 시) | §19.2 | | IEC 60601-1-3:2008+A1+A2 (방사선 방호) | ● | ● | N/A | §17 | | IEC 60601-1-6:2010+A1+A2 (사용성) | ● | ● | ● | §5, §23 | | IEC 60601-2-28:2017 (X-ray 관구) | N/A | ● | N/A | §17.2 | | IEC 60601-2-54:2022 (촬영·투시 장비) | ● | ● | N/A | §16, §17.2 | | IEC 62220-1-1:2015 (DQE) | ● | N/A | N/A | §1.1, §16.1 | | IEC 62304:2006+A1:2015 (SW 수명주기) | ● (내장SW) | ● (내장SW) | ● | §18 | | IEC 62366-1:2015+AMD1:2020 (사용성) | ● | ● | ● | §5, §23...

2. Chunk `1025819704026177008`

> ### §10 — 화학적·물리적·생물학적 특성 | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | 근거 문서 | |---|---|---|---|---|---|---| | 10.1 | 사용 재료의 독성 없음 확인 | ● | ● | N/A | TEST | ISO 10993-1 생물학적 평가 (환자 접촉 부위) | | 10.2 | 재료와 조직·세포·체액 적합성 | ● (접촉 시) | N/A | N/A | TEST | ISO 10993 시리즈 | | 10.3 | 오염물질·잔류물 허용 한도 이내 | ● | ● | N/A | TEST | 해당 표준 | | 10.4 | 의도하지 않은 물질 침투 방지 | ● | ● | N/A | SPEC | 인클로저 설계 검증 | | 10.5 | 나노소재 — 추가 위험 평가 | [검증 필요] | [검증 필요] | N/A | RMF | 나노소재 사용 여부 확인 필요 |

## ra_kr

### kb-eval-20260724-it03-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_kr-001", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "ebda78848c29a7df", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "37b5b85806368a2c0e2837de4d04e3b97b215c4e5ca9b992101d506a9815b038"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `ebda78848c29a7df`
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

### 1. Device Classification & Submission Route  
| Decision point | Korean regulation basis | Determination* |
|----------------|------------------------|----------------|
| **Class (Ⅰ/Ⅱ/Ⅲ) / risk level** | MFDS “의료기기 분류” rules (Annex II of the Medical Devices Act) – classification is decided by intended use, invasive degree and duration of contact. | *To be identified from the product’s indication, invasiveness and duration.* |
| **Submission pathway** | – **허가(일반)** for Class Ⅱ/Ⅲ devices with clinical data.<br>– **허가(임상 포함)** when a clinical investigation is required in Korea.<br>– **인증** for certain software or accessories under MFDS‑NIFDS entrusted evaluation.<br>– **신고** for Class Ⅰ non‑sterile, low‑risk devices. | Use the route that matches the final classified class and whether Korean clinical data are mandatory (see § 4 of the Medical Devices Act). |

> **Citation:** Processing time tables for each pathway are provided in source [1] (Chunk 1020687580074720264).

*Note:* Until the classification is confirmed, prepare dossiers for both 허가(일반) and 신고 as fallback.

---

### 2. Required Evidence Packages  

| Evidence type | When required | Korean requirement description |
|---------------|--------------|--------------------------------|
| **Device Description & Intended Use** | All pathways | Full Korean‐language labeling, IFU and brochure (see MFDS “표준 라벨 가이드”). |
| **Technical Documentation (Design History File)** | 허가/인증 | Conforms to ISO 13485:2016; KGMP‑certified manufacturing site required. |
| **Non‑clinical Safety Data** | All devices > Class Ⅰ | GLP‑compliant biocompatibility, toxicology, sterility validation. OECD “mutual acceptance of data (MAD)” can be referenced only for non‑clinical GLP studies; foreign data must be mapped to Korean requirements. |
| **Clinical Evaluation Report (CER)** | Class Ⅱ/Ⅲ or when domestic clinical trial is required | MFDS accepts foreign CERs that meet IMDRF “Clinical Evaluation” guidance **if** a local post‑marketing surveillance plan is submitted. Separate Korean clinical data may still be mandatory for high‑risk devices. |
| **Korean Clinical Data** | Class Ⅱ (implantable) / Class Ⅲ | Full domestic feasibility study or bridging trial, unless MFDS issues a waiver after review of foreign pivotal data. |
| **KGMP Facility Certification** | All devices submitted for 허가/인증 | Facility must hold KGMP certification; certification evidence attached to dossier. |
| **Post‑Market Surveillance (PMS) Plan** | All approved devices | PMS plan in Korean, with risk‐based monitoring schedule and reporting procedures. |
| **Risk Management File** | All pathways | ISO 14971:2019 compliance; must demonstrate identification of residual risks and corresponding controls. |

> **Citation:** Example language for “보완 내용 인용” and “데이터 추가 제출” is supplied in source [2] (Chunk 1071384471244337751). Use these phrasing templates when responding to MFDS supplement requests.

---

### 3. Identified Missing Information (Typical Gaps)  

| Gap | Why it matters | Suggested action |
|-----|----------------|------------------|
| **Korean‑language translation of all supplementary data** | MFDS requires every submitted document to be in Korean or accompanied by a certified translation. | Prepare Korean translations for each new dataset; use the template phrasing from source [2] when notifying the agency of the addition. |
| **Explicit reference to the regulatory notice/paragraph supporting the request** | MFDS reviewers expect citation of the specific 고시·지침항목 that governs the supplement. | Identify the exact MFDS 고시 number (e.g., “고시 제2024‑57호”) from the current guidance; if not found in source, note “no specific identifier found in source — verify separately”. |
| **Evidence of KGMP compliance for subcontractors** | Sub‑contracted testing labs must also be KGMP‑certified. | Obtain and attach KGMP certificates for all external partners. |
| **Local clinical trial status (if required)** | For devices needing Korean data, the agency will request a progress update. | Include a “시험 진행 중” statement as in source [2] together with anticipated completion dates. |
| **Clear timeline for supplement submission** | MFDS clock stops during the 보완 period; exceeding the agreed deadline may trigger an extension request. | Propose a realistic schedule; if extension is needed, use the “연장 요청” template from source [2]. |

---

### 4. Risk Controls & Mitigation Measures  

1. **Document Control** – Implement a centralized docket to track all supplemental items, their Korean translations, and the associated MFDS clock‑stop dates.  
2. **Clock Management** – Record the start date of each 보완 period; monitor the deadline (65 days for 일반 허가, 80 days for 임상 포함 허가) per source [1]. Submit extensions before the expiry using the prescribed Korean phrase.  
3. **Cross‑Reference Check** – Verify that every foreign datum cited has an accepted Korean equivalent or a MFDS‑approved mutual‑acceptance justification (non‑clinical GLP data only).  
4. **Quality Assurance Review** – Prior to each submission, QA must certify that: <br>  • All documents are in Korean; <br>  • KGMP certificates are current; <br>  • The risk management file reflects any new residual risks identified by the supplement.  

---

### 5. Citations (as used above)

| Item | Source excerpt |
|------|----------------|
| Processing time for 허가(일반), 허가(임상 포함), 인증, 신고; clock‑stop rule | Chunk 1020687580074720264 – “보완 기간은 처리 기간에서 제외 (clock stops)” |
| Standard Korean expression templates for supplementary response | Chunk 1071384471244337751 – various phrase examples (“귀처의 보완 요청 내용…”, “해당 데이터를 별첨 자료로 첨부하오니…” etc.) |
| Specific regulatory notice numbers or article sections | *No specific identifier found in source — verify separately* |

---

### 6. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Action required |
|---------|-----------------------|-----------------|
| **Clock‑stop deadline approaching with incomplete supplement** | Risk of MFDS denying the extension and forcing a full re‑submission. | Alert senior RA manager ≥ 5 business days before expiry; prepare an extension request using template language. |
| **Request for Korean clinical data while no trial is underway** | Potential regulatory hold‑up for high‑risk devices. | Escalate to project leader and Clinical Operations to initiate a rapid feasibility study or seek MFDS waiver. |
| **Discrepancy between foreign non‑clinical data scope and MFDS MAD acceptance** | May lead to rejection of foreign GLP data. | Raise to QA/Regulatory Lead for gap analysis; consider supplemental local non‑clinical testing. |
| **KGMP certification lapse on any subcontractor** | Non‑compliance with 허가 submission requirements. | Immediate notification to Quality Assurance and procurement to obtain up‑to‑date certificates. |
| **Ambiguous MFDS reference in a supplement request (no 고시 번호 provided)** | Reviewer may request clarification, delaying the process. | Flag for senior regulatory counsel to locate the exact notice/paragraph before responding. |

---

### 7. Peer Review Prompt  

> *@RA‑Peer:* Please review this draft and challenge any assumptions about classification pathways, the completeness of evidence listed, and whether all jurisdiction‑specific gaps (e.g., Korean language requirements, KGMP scope) have been captured. Highlight any additional MFDS notices or article numbers that should be cited but are absent from the current source excerpts.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 20/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,615자 | — |
| 규제 식별자 인용 | 3개 | — |
| source excerpt 근거 일치 | **0/3 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 3개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `Annex II` | MDR Annex II | Technical documentation |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
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

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `1071384471244337751`

> ### 4-C. 자주 사용하는 표현 (한국어 공문 문체) | 상황 | 표현 | |---|---| | 보완 내용 인용 | "귀처의 보완 요청 내용(제○호, ○○항)에 대하여 다음과 같이 보완합니다." | | 데이터 추가 제출 | "해당 데이터를 별첨 자료로 첨부하오니 검토하여 주시기 바랍니다." | | 시험 진행 중 | "현재 ○○기관에 시험 의뢰 중으로, 결과 수령 후 추가 제출 예정입니다." [검증 필요] | | 기준 적합성 | "관련 규격 ○○○ 기준을 충족함을 확인하였습니다." | | 연장 요청 | "시험 일정상 ○월 ○일까지 보완자료 제출이 어려우므로, 기한 연장을 요청드립니다." | ---

### kb-eval-20260724-it03-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_kr-002", "iteration": 3, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "713e47d6451a926b", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b63054e003f91d4a20885aaab31661946e93f889ff5f60d7e1eb9f642b6e52a0"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `713e47d6451a926b`
- Source: `github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/02_%ED%92%88%EC%A7%88%EA%B2%BD%EC%98%81%EC%8B%9C%EC%8A%A4%ED%85%9C_QMS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4.md)
- Source hash: `b63054e003f91d4a20885aaab31661946e93f889ff5f60d7e1eb9f642b6e52a0`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_요구사항_매트릭스.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: 6-1_사용적합성_엔지니어링_계획서_v0.1.md | Formative/Summative 실행 | | DR-07 | 임상적 유효성(해당 시) | 법 제15조 | ◐ | 임상평가계획서 승인, CER 완성 | - | 임상평가계획/보고서 템플릿 작성 | ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | |
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

> **Regulatory Draft – Digital‑Healthcare Device (디지털의료제품)  

Prepared for: Korean MFDS (KR RA)  
Date: 2026‑07‑26**

---

### 1. Classification & Submission Route
| Item | Determination | Rationale / Source |
|------|--------------|--------------------|
| **Risk class** | To be determined (Class I, II, III or IV) | Classification must follow the MFDS “Medical Device Classification Regulation” (Annex Ⅰ, rule‑based matrix). The specific rule number is not supplied in the source excerpts. |
| **Submission pathway** | **허가** (full approval) if Class II‑IV; **신고** (notification) if Class I & low‑risk | Korean law requires a 허가 for devices that need clinical data or have higher risk; 신고 suffices for low‑risk, non‑clinical devices. |

> **Citation (framework)** – MFDS “Medical Device Act” and its Enforcement Decree; classification rules are defined in the “Regulation on the Classification of Medical Devices”. No specific clause is quoted in the source.

---

### 2. Required Evidence Package (minimum)

| Evidence | Requirement | Status / Gap |
|----------|-------------|--------------|
| **Device Technical File** (설계·제조·품질) | Engineering plan, usability engineering, risk management file (ISO 14971). | Engineering plan referenced in source as “사용적합성_엔지니어링_계획서” – however only a placeholder version v0.1 is shown; full finalized document required. |
| **Clinical Evaluation Report (CER)** | Complete CER approved per **법 제15조** (excerpt [1]). Must include clinical evaluation plan, performed study data or justified reliance on foreign data. | Source lists “임상평가계획서 승인, CER 완성” as a deliverable, but no actual report is attached – missing. |
| **Foreign Evidence (if used)** | FDA 510(k) clearance / CE marking can be leveraged only when MFDS has issued a mutual‑acceptance notice for the specific data type (non‑clinical GLP safety = OECD MAD; clinical evaluation = separate foreign CER acceptance). No such notice is cited in source. | Not provided – gap to verify whether any foreign predicate exists and whether MFDS currently accepts it. |
| **KGMP Facility Certification** | Manufacturer must hold KGMP certification for the production site (ISO 13485‑compatible inspection). | No evidence of KGMP listed. |
| **Labeling & IFU** | All labeling, package insert, and user manual must be in Korean language; include regulatory symbols, intended use, contraindications, and post‑marketing surveillance contact. | Not included in source excerpts. |
| **Post‑Market Surveillance (PMS) Plan** | PMS plan covering routine vigilance, post‑approval studies, and periodic safety update reports as mandated by MFDS “시판후조사” regulations. | No PMS documentation referenced. |
| **Gap Analysis Documentation** | Completed gap‑analysis tracking form (F‑GAP‑001) showing open/closed gaps; required for submission audit trail. Source shows a template (excerpt [2]) but no populated data. | Gap analysis not yet performed – missing. |

---

### 3. Missing / Incomplete Information
1. **Device risk classification** – exact class and the corresponding MFDS rule number are unknown.  
2. **Finalized engineering & usability plan** – only a version‑0.1 draft is listed.  
3. **Approved Clinical Evaluation Report (CER)** – required per 법 제15조, not yet supplied.  
4. **Foreign predicate or clearance documentation** – needed if planning to rely on FDA/CE data.  
5. **KGMP certificate copy** – mandatory for manufacturing sites.  
6. **Korean language labeling & IFU** – no sample provided.  
7. **Filled gap‑analysis (F‑GAP‑001)** – template exists, but status of gaps is empty.  
8. **Post‑Market Surveillance (PMS) strategy** – absent from current files.

---

### 4. Risk Controls to Highlight in Submission
| Control | Reference Standard / Guidance |
|--------|------------------------------|
| **Usability Engineering** | IEC 62366‑1 (Korean adoption) – ensures device can be used safely by intended users. |
| **Risk Management** | ISO 14971:2019 – must be reflected in the technical file and CER. |
| **Software Lifecycle** (if applicable) | IEC 62304 – for digital health software; MFDS expects compliance. |
| **Data Security & Privacy** | Korean Personal Information Protection Act (PIPA) & “Medical Device Cybersecurity Guidance” issued by MFDS (no specific notice number in source). |
| **Electrical Safety / EMC** | KC 안전 규정 (Korean Certification) – IEC 60601‑1 family. |

---

### 5. Citations Extracted from Source
| Citation Type | Detail |
|---------------|--------|
| **Framework reference** | Law **제15조** (clinical evaluation requirement) – appears in excerpt [1]. |
| **Instance identifier** | No specific MFMFDS 고시, notice number, or article/section beyond “제15조” is provided in the excerpts. *No specific identifier found in source — verify separately.* |

---

### 6. Human‑Escalation Triggers
| Trigger | Action Required |
|--------|-----------------|
| **Unresolved classification** – risk class cannot be assigned after initial review. | Escalate to senior RA or regulatory affairs manager for classification decision and possible pre‑submission meeting with MFDS. |
| **Missing CER or incomplete clinical data** – requirement per 법 제15조 not satisfied. | Pause submission; request clinical evidence from development team; consider external CRO support. |
| **Absence of KGMP certification** – manufacturing site not verified. | Immediate escalation to Quality Assurance for facility audit and KGMP application before proceeding. |
| **Gap‑analysis form remains empty after 2 weeks of the target date** – indicates undocumented gaps in compliance. | Notify project lead; schedule a remediation workshop; log as high‑priority issue in QMS. |
| **Regulatory notice on foreign data acceptance changes** (e.g., new MFDS mutual‑acceptance notice). | Review latest MFDS notices; if relevant, incorporate foreign data; otherwise, prepare full Korean clinical package. |

---

### 7. Next Steps (Actionable)
1. Conduct formal risk classification using the MFDS Classification Regulation – capture rule number and class.  
2. Finalize the **사용적합성_엔지니어링_계획서** (usability engineering plan) and attach to technical file.  
3. Complete clinical evaluation plan, conduct required studies or justify reliance on foreign data; obtain approval and produce CER per 법 제15조.  
4. Secure KGMP certification for the manufacturing location, include certificate copy.  
5. Translate all labeling, IFU, and safety information into Korean; perform label review against MFDS labeling guidance.  
6. Populate **F‑GAP‑001** gap‑analysis tracking form with identified gaps, mitigation actions, owners, and dates; close when resolved.  
7. Draft PMS plan aligned with MFDS post‑marketing surveillance requirements.  

---

### 8. Peer Review Prompt
> *Colleague RA, please review the assumptions made above—particularly the classification approach, reliance on foreign clinical data, and the completeness of the risk‑control mapping. Are there any jurisdiction‑specific gaps (e.g., recent MFDS notices on digital health device software updates) that have not been addressed? Provide feedback on any missing evidence items or alternative submission strategies.*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 19/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,210자 | — |
| 규제 식별자 인용 | 5개 | — |
| source excerpt 근거 일치 | **0/5 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 5개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 13485` | ISO 13485 | 의료기기 품질경영시스템 (설계관리·문서관리·구매·생산·CAPA·경영검토) |
| `IEC 62366` | IEC 62366 | 사용적합성 공학 (usability engineering) — ISO 14971 위험관리 보완 |
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |
| `IEC 60601` | IEC 60601 | 의료용 전기기기 안전·필수성능 |

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

1. Chunk `1030171511734839168`

> 6-1_사용적합성_엔지니어링_계획서_v0.1.md | Formative/Summative 실행 | | DR-07 | 임상적 유효성(해당 시) | 법 제15조 | ◐ | 임상평가계획서 승인, CER 완성 | - | 임상평가계획/보고서 템플릿 작성 |

2. Chunk `1045730514097588767`

> ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | |

### kb-eval-20260724-it03-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_kr-003", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "6dcdaabbf9608bb4", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_기술문서_섹션별_작성가이드.md", "source_hash": "f1a42b1b5d6bc604ca2faa7644dc90cfb166a98521fb98244ac09e80eec1e2b1"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `6dcdaabbf9608bb4`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_기술문서_섹션별_작성가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%84%9C_%EC%84%B9%EC%85%98%EB%B3%84_%EC%9E%91%EC%84%B1%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `f1a42b1b5d6bc604ca2faa7644dc90cfb166a98521fb98244ac09e80eec1e2b1`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_기술문서_섹션별_작성가이드.md`는 MFDS 기술문서 섹션별 작성 요구사항과 evidence 구성 기준 문서입니다.
- 현재 excerpt 핵심: ### 4.3 시험규격 설정 근거 작성 요령 - 국제 표준 근거: "IEC 60601-2-28:2017을 적용하였으며, 동 규격이 X선관 조립품(X-ray tube assembly)의 성능 시험 방법을 규정하는 국제 표준으로 MFDS 인정 기준과 일치함." - 자사 규격 근거: "국제 표준에서 정하지 않은 항목(예: 영상 처리 알고리즘 성능)은 의도된 사용목적 및 위험 분석 결과에 따라 자사 시험 규격 OQP-XXXX를 제정하여 적용함." - KS 표준 근거: "KS A ISO 9283 대응 자사 규격 적용." --- ## 1. 기술문서 전체 구성 (시행규칙 별표 3 기준) ``` 기술문서 (MFDS 제출용) ├── 1. 개요 (제...
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

> **Regulatory Draft – X‑ray Tube Assembly (Medical Imaging Device)**  

---

### 1. Classification & Submission Route  

| Item | Judgment (based on source) |
|------|----------------------------|
| **Device type** | X‑ray tube assembly (radiation‑emitting medical device). |
| **Likely MFDS class** | Class II–III (radiation devices are placed in the higher risk categories). |
| **Submission pathway** | **허가(Approval)** – required for all Class II and III devices under MFDS regulations.  *(No specific notice number appears in the source; verify the exact classification rule in the current 시행규칙.)*  

---

### 2. Required Evidence (Technical Documentation)  

The technical dossier that MFDS expects follows **시행규칙 별표 3** (see source [2]) and must contain at least the following sections:

| Section (MFDS §) | Content Requirement | Source‑based Note |
|------------------|--------------------|-------------------|
| 1. Overview | Product name, item name, classification code, model number, manufacturer details. | – |
| 2. Intended Use | Indications for use, target patient population. | – |
| 3. Operating Principle | Description of the X‑ray generation mechanism. | – |
| 4. Materials & Structure | Bill of materials, component specifications. | – |
| 5. Manufacturing Process | Process flow diagram, critical process controls, KGMP compliance evidence. | – |
| 6. Performance & Test Specifications | **6‑1** Test specification and justification; **6‑2** Measured data (test reports). <br> • International standard: **IEC 60601‑2‑28:2017** is cited as the performance test basis (source [1]). <br> • Items not covered by IEC (e.g., image‑processing algorithm) must be justified by risk analysis and internal spec OQP‑XXXX. <br> • Mechanical safety may reference **KS A ISO 9283** (source [1]). | IEC 60601‑2‑28, KS A ISO 9283 |
| 7. Safety Data | 7‑1 Electrical & mechanical safety, 7‑2 Biological safety (if applicable), 7‑3 Radiation safety, 7‑4 EMC, 7‑5 Software safety (when software is present). | – |
| 8. Clinical Evidence (if required) | Summaries of clinical evaluation, foreign CE/ FDA clearance data, or Korean‑conducted clinical trial results where MFDS mandates local data. | No specific citation in source – verify separately. |
| 9. Labeling & IFU | Korean language labeling, instructions for use, warnings, and risk information. | No specific citation in source – verify separately. |

**Additional mandatory files (per MFDS guidance)**  

* ISO 14971 risk management file (risk analysis, mitigation measures).  
* Biocompatibility data (ISO 10993) if patient‑contacting materials are present.  
* KGMP facility certification copy.  
* EMC test report (IEC 60601‑1‑2 or equivalent).  
* Software documentation (validation plan, verification results) when software is part of the device.

---

### 3. Missing Information & Gaps  

| Gap | Reason it Must Be Filled | Action |
|-----|--------------------------|--------|
| **Exact MFDS classification rule number** (e.g., “시행규칙 제 XX조 제 YY항”) | Required to confirm whether the device is Class II or III and thus the exact submission form. | Retrieve current 시행규칙 and record the specific article. |
| **Local clinical data / CER acceptance** | MFDS may require Korean‑specific clinical evidence for radiation devices even if foreign CE/FDA clearance exists. | Determine applicability of the latest MFDS notice on foreign clinical evaluation reports; collect local clinical data if needed. |
| **KGMP certification status** | Mandatory for all manufacturing facilities submitting a 허가. | Obtain KGMP audit certificate and include in Section 5. |
| **Korean labeling & IFU** | Korean language is compulsory for labeling; absence blocks approval. | Prepare draft label/IFU in Korean, align with MFDS labeling guidance. |
| **Radiation safety calculations** beyond IEC 60601‑2‑28 (e.g., dose limits specific to Korean guidelines). | MFDS may impose additional national dose limits. | Verify current radiation protection notice; provide compliance data. |
| **Software safety evidence** (if the assembly includes embedded processing software) | Required under SW safety sub‑section 7‑5. | Conduct IEC 62304–based software life‑cycle documentation. |
| **EMC test report** | Needed under 7‑4; not mentioned in source excerpts. | Perform EMC testing per IEC 60601‑1‑2 and attach report. |

---

### 4. Risk Controls (Mapped to Evidence)  

| Hazard / Failure Mode | Control Measure (ISO 14971) | Supporting Documentation |
|-----------------------|-----------------------------|---------------------------|
| Excessive X‑ray output → patient over‑exposure | Design limit per IEC 60601‑2‑28; built‑in dose monitoring circuitry. | Test specification & results (Section 6). |
| Mechanical failure of tube housing → injury | Mechanical strength verified to KS A ISO 9283. | Test reports (Section 6‑2). |
| Software algorithm error → mis‑diagnosis | IEC 62304 software validation; verification against clinical requirements. | SW safety dossier (Section 7‑5). |
| Electrical shock / fire hazard | Compliance with IEC 60601‑1 electrical safety limits. | Electrical safety test report (Section 7‑1). |
| Electromagnetic interference affecting device operation | EMC testing per IEC 60601‑1‑2. | EMC report (Section 7‑4). |

---

### 5. Citations  

* **IEC 60601‑2‑28:2017** – performance test basis for X‑ray tube assemblies (source [1]).  
* **KS A ISO 9283** – mechanical safety reference (source [1]).  
* **시행규칙 별표 3** – required structure of the MFDS technical dossier (source [2]).  

*(No specific MFDS notice or article number appears in the supplied excerpts; those identifiers must be retrieved from the current regulator publications – “no specific identifier found in source — verify separately.”)*

---

### 6. Human‑Escalation Triggers  

| Situation | Why Escalate | Escalation Target |
|-----------|--------------|-------------------|
| Uncertainty about classification rule (Class II vs III) | Determines whether a 허가 or a more stringent dossier is needed. | Senior RA / Regulatory Lead. |
| Absence of local clinical data when MFDS notice suggests it is mandatory. | Could cause outright rejection. | Clinical Affairs lead + senior RA. |
| KGMP certification not yet obtained for the production site. | Facility non‑compliance blocks approval. | Quality/Manufacturing Manager. |
> **Trigger**: Any “no specific identifier found in source — verify separately” item remains unfilled after preliminary document review.  

---

### 7. Peer Review Prompt  

*“@RA‑Peer, please challenge the assumptions made regarding (1) the device’s classification under current MFDS 시행규칙; (2) the sufficiency of foreign clinical evidence without a Korean‐specific trial; and (3) any potential gaps in radiation safety data not covered by IEC 60601‑2‑28 but required by national notices. Confirm whether additional domestic documentation or an updated notice should be incorporated before final submission.”*

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 18/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 7,024자 | — |
| 규제 식별자 인용 | 5개 | — |
| source excerpt 근거 일치 | **2/5 (40%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 3개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 중간**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `ISO 14971` | ISO 14971 | 의료기기 위험관리 (risk management) — 다른 표준을 잇는 허브 |
| `ISO 10993` | ISO 10993 | 의료기기 생물학적 안전성 평가 — ISO 14971 위험관리에 반영 |
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

1. Chunk `1075785891198339619`

> ### 4.3 시험규격 설정 근거 작성 요령 - 국제 표준 근거: "IEC 60601-2-28:2017을 적용하였으며, 동 규격이 X선관 조립품(X-ray tube assembly)의 성능 시험 방법을 규정하는 국제 표준으로 MFDS 인정 기준과 일치함." - 자사 규격 근거: "국제 표준에서 정하지 않은 항목(예: 영상 처리 알고리즘 성능)은 의도된 사용목적 및 위험 분석 결과에 따라 자사 시험 규격 OQP-XXXX를 제정하여 적용함." - KS 표준 근거: "KS A ISO 9283 대응 자사 규격 적용." ---

2. Chunk `134996178882731357`

> ## 1. 기술문서 전체 구성 (시행규칙 별표 3 기준) ``` 기술문서 (MFDS 제출용) ├── 1. 개요 (제품명, 품목명, 분류번호, 모델명, 제조원) ├── 2. 사용목적 (Intended Use / Indications for Use) ├── 3. 작용원리 (Operating Principle / Mechanism of Action) ├── 4. 원재료·구성품·구조 (Materials & Structure) ├── 5. 제조방법 (Manufacturing Process) ├── 6. 성능·시험규격 (Performance & Test Specifications) │ ├── 6-1. 시험규격 및 설정근거 │ └── 6-2. 실측값 (성적서) ├── 7. 안전성 자료 (Safety Data) │ ├── 7-1. 전기·기계적 안전 │ ├── 7-2. 생물학적 안전 │ ├── 7-3. 방사선 (해당 시) │ ├── 7-4. 전자파(EMC) │ └── 7-5. SW 안전성 (해당 시) ├── 8. 임상자료 (해당 시) └── 9. 기재사항 (라벨, 사용설명서) ``` ---

### kb-eval-20260724-it03-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_kr-004", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "b3c0a8355c259b40", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_표시기재_가이드라인_대응.md", "source_hash": "5a5fc07e3c93a3f8513749b4e2b7b957e84d2d3b2fe89962cf0c41814c4fe78d"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `b3c0a8355c259b40`
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

> **Regulatory Draft – Digital‑Medical Device Labeling (표시·기재) Requirements**

---

### 1. Device Overview  
- **Product type:** Software‑based digital medical device (SW 일반).  
- **Intended use:** As defined by the sponsor (not supplied in source).  

---

### 2. Classification & Submission Route  

| Factor | Determination | Rationale / Source |
|--------|---------------|--------------------|
| **Classification** | *To be confirmed* – likely Class I or II under MFDS “디지털의료제품법 시행규칙” (Digital Medical Device Act Enforcement Rules). | The enforcement rules set the risk‑based class for software; no specific class is stated in the excerpt, so verification with the sponsor’s intended use and functional description is required. |
| **Submission pathway** | *허가* (approval) if Class II or higher; *신고* (notification) if Class I and exempt from full approval. | MFDS follows a risk‑based split between 허가 and 신고 for digital health products. |

> **Human escalation trigger:** If the sponsor cannot provide a clear functional description that maps to the enforcement‑rule criteria, escalate to senior RA for classification confirmation before dossier assembly.

---

### 3. Mandatory Labeling / IFU Elements (Checklist Mapping)

| Item (Source ID) | Required? | Current status | Comments / Evidence needed |
|------------------|-----------|----------------|----------------------------|
| **S‑1 Software version, build number, release date** | ✅ 필수 | – | Provide a version matrix and release log. |
| **S‑2 Software update method & frequency** | ✅ 필수 | – | Define OTA/patch process; schedule (e.g., quarterly). |
| **S‑3 Minimum / recommended system requirements (OS, CPU, RAM, storage, monitor resolution, network)** | ✅ 필수 | – | Draft a table of specs per device model. |
| **S‑4 Compatible medical devices list & interface information** | ✅ 필수 | – | List all interfaced hardware and communication protocols. |
| **S‑5 Data input/output formats (DICOM, HL7, etc.)** | ✅ 필수 | – | Provide format specifications and mapping tables. |
| **S‑6 Cybersecurity settings guidance (password policy, network segregation, access rights)** | ✅ 필수 | – | Align with *MFDS 사이버보안 가이드라인 2025.01*. |
| **S‑7 Security‑patch application procedure & responsibility** | ✅ 필수 | – | Define roles (e.g., vendor vs. user) and SOPs. |
| **S‑8 Known residual cybersecurity risks & mitigation measures** | ✅ 필수 | – | Conduct a risk assessment per *MFDS 사이버보안 가이드라인 2025.01*. |
| **S‑9 Data backup & recovery method** | ✅ 필수 | – | Document backup frequency, storage media, restore test results. |
| **S‑10 System log management method** | ⚠️ 권장 | – | Optional but recommended; implement per *MFDS 사이버보안 가이드라인*. |
| **AI/ML‑specific disclosures** (truncated in source) | – | – | If AI/ML is used, additional transparency items apply (algorithm description, performance metrics). |

> **Human escalation trigger:** Any “⚠️ 권장” item that the sponsor elects to omit should be flagged for senior review because MFDS may treat it as de‑facto mandatory during audit.

---

### 4. Evidence Package Required for Submission  

| Evidence Type | Requirement | Source / Basis |
|---------------|-------------|----------------|
| **KGMP certification** for any manufacturing site (software build environment) | Mandatory for Class II+ devices. | MFDS 고시 on KGMP (general requirement). |
| **Software Validation Report** (including verification & validation, risk management per IEC 62304) | Required to demonstrate compliance with functional and safety claims. | International standard mapping; Korean acceptance of IEC/ISO references. |
| **Cybersecurity Assessment Report** (threat modeling, penetration testing results) | Must address S‑6 – S‑8 items. | *MFDS 사이버보안 가이드라인 2025.01*. |
| **Data Backup & Recovery Test Records** | Evidence for S‑9 compliance. | Internal SOPs; no external citation required. |
| **System Log Management Procedure (if implemented)** | Supports S‑10 recommendation. | Internal documentation. |
| **Korean language IFU / labeling** (including all mandatory items from the general medical device checklist) | All “표시·기재” must be in Korean, per MFDS labeling rules. | MFDS 디지털의료기기 표시기재 가이드라인. |
| **Clinical Evaluation Report** (if class II+ or AI/ML component) | Needs local clinical data unless MFDS accepts foreign CER under current mutual‑acceptance scope. | Check the latest MFDS notice on foreign CER acceptance; not provided in source – *verify separately*. |

> **Human escalation trigger:** If any of the above evidence cannot be produced (e.g., no KGMP certificate, missing cybersecurity test results), halt dossier progression and notify the project lead.

---

### 5. Identified Gaps / Missing Information  

1. **Specific classification decision** – required to choose 허가 vs 신고.  
2. **Detailed software update schedule & method** (S‑2).  
3. **Exact hardware compatibility list** (S‑4) and associated interface diagrams.  
4. **Data format specifications** (S‑5) beyond naming DICOM/HL7.  
5. **Cybersecurity risk analysis outcomes** (S‑8) – documented residual risks & mitigation plan.  
6. **Backup & recovery test reports** (S‑9).  
7. **Korean IFU draft covering all mandatory items** (general medical device labeling checklist plus the digital‑specific additions).  
8. **Clinical evidence scope** – local data requirement unclear; need confirmation of MFDS acceptance of any foreign clinical evaluation.  

> **Human escalation trigger:** Any gap that maps to a “✅ 필수” element must be escalated immediately to the sponsor for remediation before submission.

---

### 6. Risk Controls (aligned with checklist)

| Control | Linked Checklist Item(s) | Description |
|---------|--------------------------|-------------|
| **Version control & release management** | S‑1, S‑2 | Maintain a CMDB with build IDs, release dates, and change logs. |
| **System requirement verification** | S‑3 | Conduct compatibility testing on declared minimum specs. |
| **Interface validation** | S‑4, S‑5 | Perform integration tests with each listed medical device; verify DICOM/HL7 data exchange. |
| **Cybersecurity baseline** | S‑6, S‑7, S‑8 | Implement password policies, network segmentation, role‑based access; run periodic vulnerability scans; apply patches per defined SOP. |
| **Residual risk monitoring** | S‑8 | Continuous monitoring dashboard for identified cyber threats; update mitigation plan as needed. |
| **Data backup & disaster recovery** | S‑9 | Automated nightly backups to encrypted off‑site storage; quarterly restore drills. |
| **Log management (recommended)** | S‑10 | Centralized log server with retention ≥ 12 months; audit trail for security events. |

---

### 7. Citations  

- **Framework references**  
  - “디지털의료제품법 시행규칙” – enforcement rule defining classification and basic labeling obligations.  
  - “MFDS SW 가이드라인” – source of software‑related labeling items (S‑2, S‑3).  
  - “MFDS 사이버보안 가이드라인 2025.01” – provides the detailed cybersecurity requirements referenced for S‑6 – S‑8 and optional S‑10.  

- **Instance identifiers present in source**  
  - *MFDS 사이버보드 가이드라인 2025.01* (year‑specific guide).  

> No specific MFDS 고시/notice numbers or article (§) citations appear in the provided excerpts; therefore, “no specific identifier found in source — verify separately” applies to any request for a numbered notice.

---

### 8. Human‑Escalation Triggers Summary  

| Trigger | Reason | Escalation Path |
|---------|--------|-----------------|
| **Unclear classification** | Determines 허가 vs 신고 and evidence depth. | Senior RA → Classification Working Group. |
| **Missing mandatory checklist data (any ✅ 필수 item)** | Submission would be non‑compliant. | Project Manager & Sponsor – pause dossier. |
| **Absence of KGMP certification or software validation report** | Required for Class II+ approval. | Regulatory Lead → Compliance Office. |
| **Lack of cybersecurity assessment aligned with 2025.01 guide** | High risk of MFDS audit findings. | Security Team lead + RA manager. |
| **No Korean IFU covering all required elements** | Violates labeling law. | Localization/Medical Writing lead. |
| **Unverified foreign clinical evidence acceptance** | May be rejected if not within current mutual‑acceptance scope. | Clinical Affairs → MFDS liaison for clarification. |

When any trigger is hit, the responsible owner must document the issue in the project risk register and obtain formal sign‑off before proceeding.

---

### 9. Peer Review Prompt  

> **@RA‑Peer:** Please review the assumptions made regarding:  
> - Classification determination based solely on “디지털의료제품법 시행규칙” without a specific use case.  
> - Coverage of all mandatory labeling items; verify whether any additional digital‑specific disclosures (e.g., data privacy statements, AI/ML transparency) are required beyond the checklist excerpt.  
> - The adequacy of citing only the 2025.01 cybersecurity guide—confirm if newer MFDS cyber guidance or separate notices should also be referenced.  
> Your feedback on potential jurisdictional gaps and source completeness is appreciated.

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 17/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 9,138자 | — |
| 규제 식별자 인용 | 1개 | — |
| source excerpt 근거 일치 | **0/1 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 1개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 높음**

**인용 식별자 ↔ 공식 제목 대조** (외부 규제자료 확인분)

| 응답 인용 | 공식 식별 | 공식 주제 |
|---|---|---|
| `IEC 62304` | IEC 62304 | 의료기기 소프트웨어 생명주기 프로세스 (ISO 14971 참조 권고) |

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

### kb-eval-20260724-it03-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-07-24", "decision_ref": "kb-eval-20260724-it03-ra_kr-005", "iteration": 3, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "be129d486ff24bd3", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md", "source_hash": "2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `be129d486ff24bd3`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/GMP_심사자료/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/GMP_%EC%8B%AC%EC%82%AC%EC%9E%90%EB%A3%8C/README.md)
- Source hash: `2e7b3445532256c7af22162f99242dd84b6e8d369ec1b701f1e4c95da2bcbf02`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `README.md`는 KGMP 또는 GMP evidence readiness, audit readiness, QMS 절차·기록 관련 문서입니다.
- 현재 excerpt 핵심: ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트 ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)
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

> **Regulatory Draft – KGMP‑related Submission Planning**

---

### 1. Device Classification & Submission Route  
| Item | Korean regulatory basis | Current status (from source) |
|------|------------------------|------------------------------|
| **Classification rule** | MFDS “의료기기 분류 규정” (Class I–IV based on risk, intended use and invasiveness). | *No specific class identified in the excerpt.* → **verify separately**. |
| **Submission pathway** | • **허가(Approval)** for Class III/IV or high‑risk Class II devices.<br>• **신고(Notification)** for low‑risk Class I (and some Class II) devices. | *No submission route mentioned.* → **verify separately**. |

*Action*: Determine the device’s risk class by applying MFDS classification tables; then select 허가 or 신고 accordingly.

---

### 2. Required Evidence – KGMP Focus  

| Requirement | Korean regulatory source (framework) | Source excerpt citation |
|-------------|--------------------------------------|------------------------|
| **KGMP Facility Certification** | *의료기기 제조 및 품질관리 기준* (고시) and *의료기기 GMP 심사·평가 등에 관한 규정*. | 【1†L1-L3】 |
| **GMP Review Application Form & Checklist** | KGMP 심사 신청서 양식 및 제출서류 체크리스트. | 【1†L1-L3】【2†L1-L4】 |
| **Technical Documentation (Design Dossier)** | Must include Device Description, Intended Use, Risk Management File, Verification/Validation reports, and Manufacturing Process description per MFDS Technical File Requirements. | *Not directly quoted* → **verify separately**. |
| **Korean‑language Labeling & IFU** | All labeling, packaging, and Instructions for Use must be provided in Korean (MFDS 라벨링 규정). | *Not directly quoted* → **verify separately**. |
| **Clinical Evidence** | • Local clinical data required unless MFDS accepts a foreign Clinical Evaluation Report (CER) under the “Foreign Clinical Data Acceptance” notice.<br>• Non‑clinical GLP safety data may be accepted via OECD Mutual Acceptance of Data (MAD). | No specific notice numbers appear in source → **verify separately**. |
| **Post‑Market Surveillance Plan** | Must submit PMS plan per *시판후조사* requirements (MFDS 고시). | *Not directly quoted* → **verify separately**. |

**Missing Information from the Current Source**

1. Device class and corresponding submission type.
2. Whether a foreign CER or OECD MAD can be leveraged for non‑clinical data.
3. Specific local clinical trial requirement (e.g., number of subjects, study design).
4. Exact labeling content checklist (e.g., required Korean symbols, safety warnings).
5. Post‑market surveillance schedule and reporting format.

---

### 3. Risk Controls & Compliance Measures  

| Control | Why needed (Korean regulation) | Implementation note |
|--------|--------------------------------|----------------------|
| **KGMP Certification** | Mandatory for any domestic manufacturer or importer of imported devices (GMP 심사·평가 등). | Submit completed KGMP checklist; obtain MFDS issuance before market entry. |
| **Korean‑language IFU & Label** | Ensures user safety and compliance with 라벨링 규정. | Translate all labeling into Korean; retain original English for reference only. |
| **Clinical Evaluation/Trial** | Required to demonstrate safety/effectiveness for Class II‑IV devices. | Conduct a local clinical study unless a valid foreign CER is accepted (see MFDS Notice on foreign clinical data). |
| **Non‑clinical GLP Data Acceptance** | OECD MAD may reduce need for duplicate animal studies. | Verify that the specific non‑clinical data fall under the scope of the MFDS MAD acceptance notice. |
| **Post‑Market Surveillance (PMS)** | Required to monitor real‑world performance and adverse events. | Establish a PMS system, report serious incidents within 30 days per MFDS 시판후조사 규정. |

---

### 4. Citations  

| Item | Citation type | Reference |
|------|---------------|-----------|
| KGMP core documents (GMP 기준, 심사 체크리스트) | Instance identifier (document title) – appears in source | 【1†L1-L3】,【2†L1-L4】 |
| Specific notice numbers for foreign CER or OECD MAD | Instance identifier – **not found** in source | *no specific identifier found in source — verify separately* |
| Classification rule, labeling rule, PMS rule | Framework reference (MFDS regulations) | Stated as factual basis; no specific article/notice number supplied. |

---

### 5. Human‑Escalation Triggers  

| Trigger | Reason | Recommended action |
|--------|--------|--------------------|
| **Unidentified device class** | Classification determines submission route and evidence burden. | Escalate to senior RA for classification workshop with product team. |
| **Absence of KGMP certification documentation** | Without KGMP, MFDS will reject the application. | Prompt facility compliance audit; involve Quality Assurance lead. |
| **Lack of Korean labeling/IFU** | Violates 라벨링 규정; leads to market entry delay. | Assign translation & regulatory writing resources; review by legal. |
| **Unclear applicability of foreign clinical data** | Risk that MFDS will request local trial, causing timeline slip. | Consult MFDS notice library or seek a formal clarification (신청). |
| **Missing PMS plan details** | Post‑market obligations are mandatory for all classes. | Draft PMS schedule; have it approved by the PMO and QA. |

When any of these triggers arise, the responsible RA should raise a **“Regulatory Gap Alert”** in the project tracking system and notify the Project Manager and Quality Assurance lead within 1 business day.

---

### 6. Reusable RA Judgment (Lesson Learned)

> *For any Korean medical‑device submission, the first step must be to confirm the device’s MFDS risk class and corresponding 허가/신고 route **before** assembling KGMP‑related documentation. The core KGMP requirement is the completed “의료기기 제조 및 품질관리 기준” checklist (as cited in source 【1†L1-L3】, 【2†L1-L4】). All other evidentiary elements—clinical data, labeling, post‑market surveillance—must be mapped to the specific class and to any MFDS notices that permit foreign evidence; if those notice numbers are not present in the source material, they must be verified independently.*  

---

### 7. Peer‑Review Prompt

> *@RA‑Colleague*: Please challenge the assumptions above regarding (1) the default need for local clinical data versus possible acceptance of a foreign Clinical Evaluation Report, (2) whether the cited KGMP checklist fully covers all documentation required for an import‑only device, and (3) any jurisdiction‑specific gaps such as the recent MFDS amendment on electronic IFU that may affect our labeling plan. Your feedback will help ensure we have not overlooked any scope changes or audit findings.  

---

<!-- verification-summary -->

**🔎 검증 요약** (우선순위 16/190 · 자동 생성 · 판정은 사람이 확정)

| 관측 | 값 | 관련 Fast Check |
|---|---|---|
| 응답 분량 | 6,652자 | — |
| 규제 식별자 인용 | 0개 | — |
| source excerpt 근거 일치 | **0/0 (0%)** | `Evidence supported` / `Source cited` |
| excerpt 미대조 | 0개 | `No hallucination` |
| C1 린터 구조 오류 | 0건 | `No hallucination` |
| escalation 표현 | 있음 | `Escalation appropriate` |

**근거 대조 위험도: 낮음**

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

1. Chunk `341244002941932847`

> ## 핵심 문서 - 「의료기기 제조 및 품질관리 기준」 (고시) - 「의료기기 GMP 심사·평가 등에 관한 규정」 - KGMP 심사 신청서 양식 및 제출서류 체크리스트

2. Chunk `634338496332185325`

> ## 수록 대상 - 의료기기 제조·품질관리 기준 (KGMP) 관련 고시 - GMP 심사 신청서·심사 체크리스트 - 기술문서 심사 대응 자료 - 적합성 인정서 (수입품목용)
