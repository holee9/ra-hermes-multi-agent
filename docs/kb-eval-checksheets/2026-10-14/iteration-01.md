# KB Eval Checksheet - 2026-10-14 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261014-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "926089d7e8d49168", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/PCCP_AI_Device_작성가이드.md", "source_hash": "d37e14047a656fb817ee60afd8825496718d21340d06d9d321951cba304d1df6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `926089d7e8d49168`
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

> **Regulatory Draft – SaMD Change Impact Assessment (Predetermined Change‑Control Plan)**  

---

### 1. Bottom‑line regulatory path  
- **Device class:** Likely **Class II** under **21 CFR §892.2050** (Medical image management and processing system) *provided the software’s intended use is image analysis/processing*. Confirmation of the exact subsection is required based on the final “intended use” statement.  
- **Submission route:** Standard **510(k)** pre‑market notification, citing a predicate cleared under the same §892.2050 class. If no suitable predicate exists, consider a **De Novo** request.  

---

### 2. Required evidentiary package (per FDA PCCP guidance)  

| Element | What must be provided | Source / citation |
|---------|----------------------|-------------------|
| **Predetermined Change‑Control Plan (PCCP)** | Complete plan covering the four mandatory sections (Data Management, Retraining Practices, Performance Evaluation, Updated Procedures). The plan must describe how each change will be pre‑authorized and documented. | Federal Register 2024‑28361 (Final guidance on PCCP) |
| **Device description & intended use** | Clear narrative of clinical indication, patient population, operating environment, and user interface. Needed to lock classification and predicate search. | No specific identifier found in source — verify separately |
| **Predicate comparison** | Side‑by‑side matrix showing technological characteristics and intended use vs. cleared device(s). Include 510(k) numbers. | No specific identifier found in source — verify separately |
| **Risk Management File** | ISO 14971–based risk analysis, including new hazards introduced by the change (e.g., data bias, algorithm drift). Update FMEAs with residual risk scores. | Framework reference – ISO 14971 (risk management) |
| **Software Validation & Verification** | • V&V protocol and report covering updated algorithm performance against pre‑defined acceptance criteria.<br>• Statistical significance testing per the “Performance Evaluation” item of PCCP. | No specific identifier found in source — verify separately |
| **Clinical/Real‑world Performance Data** | • Retrospective or prospective data set demonstrating maintained safety/effectiveness after change.<br>• Bias mitigation documentation (training/validation data version control). | No specific identifier found in source — verify separately |
| **Usability/Human Factors** | Updated “Updated Procedures” section must include user communication plan and IFU revisions. Conduct a limited usability test if UI changes are introduced. | No specific identifier found in source — verify separately |
| **QMS compliance** | Evidence of compliance with **21 CFR Part 820** (Quality System Regulation) for design control, change management, and post‑market surveillance. | Framework reference – 21 CFR Part 820 |
| **UDI labeling (if applicable)** | Conformity to **21 CFR Part 830** labeling requirements for any new device version. | Framework reference – 21 CFR Part 830 |
| **Cybersecurity** | Updated threat model, vulnerability management plan, and any software patches required by the change. | No specific identifier found in source — verify separately |

---

### 3. Missing information that must be supplied before a submission can be finalized  

1. **Exact intended use statement** – to confirm class/subsection.  
2. **Predicate device(s) identification** – 510(k) numbers and comparison matrix.  
3. **Quantitative performance criteria** – acceptance thresholds, statistical power calculations for re‑training validation.  
4. **Data set provenance** – source, size, demographic breakdown, versioning control logs.  
5. **Change impact analysis** – quantitative risk assessment showing that residual risk after change remains “acceptable” per ISO 14971.  
6. **User communication plan details** – specific modalities (e‑mail, UI alerts) and timing for IFU updates.  

---

### 4. Key risk controls (aligned with FDA AI/ML SaMD guidance & ISO 14971)

| Risk | Control |
|------|---------|
| **Algorithmic bias / data drift** | Robust data management procedures (version control, bias monitoring) as defined in the “Data Management” PCCP item. |
| **Unintended performance degradation after retraining** | Pre‑defined acceptance criteria; rollback strategy documented under “Retraining Practices”. |
| **Incorrect user interpretation of updated output** | Updated IFU with clear change log; usability testing for UI modifications. |
| **Cybersecurity vulnerabilities introduced by new code** | Secure software development lifecycle (SSDLC) controls, periodic penetration testing, and patch management per QMS. |
| **Loss of traceability for model versions** | Maintain a master log linking each deployed version to its training data, validation results, and change‑control record. |

---

### 5. Human‑escalation triggers (when the change must be reviewed/approved by senior regulatory or clinical leads)

- **Change alters intended use, target population, or clinical indication.**  
- **Performance metrics fall outside pre‑defined acceptance criteria** in the “Performance Evaluation” section.  
- **Significant increase in residual risk** (> 10 % absolute increase) after the change impact analysis.  
- **New cybersecurity vulnerability rating ≥ high severity** without immediate mitigation.  
- **Regulatory filing requirement shift** (e.g., from 510(k) to De Novo or PMA).  

When any trigger occurs, the change must be escalated to the **Regulatory Affairs Lead** and, where applicable, the **Clinical Safety Committee** for a formal decision before implementation.

---

### 6. Citations  

| Item | Citation type |
|------|---------------|
| Predetermined Change‑Control Plan guidance (final FDA guidance) | Instance identifier – Federal Register 2024‑28361 |
| Classification of image‑processing software | Framework reference – **21 CFR §892.2050** |
| Quality System Regulation requirements | Framework reference – **21 CFR Part 820** |
| UDI labeling obligations | Framework reference – **21 CFR Part 830** |
| Risk management methodology | Framework reference – **ISO 14971** |

---

### 7. Human‑escalation prompt for peer review  

> *"Please challenge the assumptions made about device classification, the completeness of the PCCP elements identified from the source, and any jurisdiction‑specific gaps (e.g., EU MDR interplay) that may affect our submission strategy."*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> '잔여위험 >10% 절대 증가'는 근거 없는 임계값(내부 기준으로 표기할 것). 'Quality System Regulation' 명칭은 QMSR으로 갱신.

**Source Excerpts**

1. Chunk `1108970615905232706`

> > 최종 갱신: 2026-05-15 (자동보강 #45) > 근거: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.federalregister.gov/documents/2024/12/04/2024-28361 | https://www.foley.com/insights/publications/2025/01/fda-final-guidance-ai-device-software-predetermined-change-control-plan/ | https://health.ec.europa.eu/latest-updates/mdcg-2025-6-faq-interplay-between-medical-devices-regulation-vitro-diagnostic-medical-devices-2025-06-19_en | https://bioin.or.kr/board.do?bid=system&cmd=view&num=332039 # PCCP (Predetermined Change Contr...

2. Chunk `198015203798949382`

> ### 3.2 Modification Protocol (변경 프로토콜) 4개 필수 항목: | 항목 | 포함 내용 | |---|---| | **Data Management** | 훈련·검증 데이터 수집·정제·버전관리 절차, 데이터 편향 관리 | | **Retraining Practices** | 알고리즘 재학습 트리거 조건, 재학습 절차, Rollback 계획 | | **Performance Evaluation** | 사전 정의된 허용 기준 (Acceptance Criteria), V&V 방법론, 통계적 유의성 요건 | | **Updated Procedures** | 사용자·임상진 커뮤니케이션 계획, 실세계 모니터링 계획, IFU 업데이트 절차 | ---

### kb-eval-20261014-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "fb075a6ebc5dc725", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_03_Performance_Testing_Bench_Test.md", "source_hash": "9f94737b713dbd5c6fa5242761b479fa1ec962b8561d7e2afccf2ec9f884e7fc"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `fb075a6ebc5dc725`
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

> **Regulatory Draft – SaMD “촬영실 GUI Software” (Image Processing & Display)**  

---

### 1. Classification & Submission Pathway  
| Item | Determination | Basis |
|------|----------------|-------|
| **Device type** | Software as a Medical Device (SaMD) – Image processing/display software used in an imaging suite. | Source § 3.3.1 “Software as Medical Device (SaMD)” |
| **FDA product class** | Class II | 21 CFR §892.2050 (Image Processing Software) |
| **Regulatory route** | 510(k) Premarket Notification – Substantial equivalence to a legally marketed predicate image‑processing software under the same CFR section. | No specific predicate identifier found in source — verify separately |

---

### 2. Core Submission Content (eSTAR Section G + FDA Guidance)

| Required Element | Description & Evidence Needed |
|------------------|--------------------------------|
| **Device description & intended use** | Clear statement of clinical function, user environment, and indication (diagnostic vs. non‑diagnostic). *Missing*: explicit intended use wording. |
| **Predicate comparison** | Identify a cleared device classified under 21 CFR §892.2050; table comparing functionality, technology, and indications. *Missing*: predicate device name/510(k) number. |
| **Software Requirements Specification (SRS)** | Complete functional and performance requirements. Already required in eSTAR package (see source). |
| **Software Design Specification (SDS)** | Architecture diagrams, module descriptions, interface specs. Included in eSTAR. |
| **Risk Management File** | IEC 62304 risk classification rationale; hazard analysis & mitigations per ISO 14971. *Missing*: full FMEA/FMECA and risk control measures. |
| **Software Validation Plan & Report** | Unit, integration, system, performance testing with traceability to SRS (Rationale Traceability Matrix). eSTAR provides test results packages; must include acceptance criteria, statistical analysis of performance, and documentation of anomalies. |
| **Cybersecurity Documentation** | Threat model, security controls, update strategy per FDA “Cybersecurity in Medical Devices” Guidance (2023‑09‑27). *Missing*: detailed cybersecurity risk assessment & mitigation plan. |
| **Usability/Human Factors** (if user interaction influences clinical decision) | Summative usability testing per IEC 62366‑1. *Missing*: any human‑factors evidence. |
| **Labeling & UDI** | Labels with required statements, intended use, and a Unique Device Identifier as mandated by 21 CFR §830.10 onward. *Missing*: draft labeling and UDI assignment plan. |
| **Quality Management System (QMS) compliance** | Conformance to QMSR (21 CFR §820) aligned with ISO 13485:2016, evidence of SOPs for software lifecycle, change control (Predetermined Change Control Plan if applicable). *Missing*: QMS certificates and documented PCCP. |
| **Software Lifecycle Documentation** | IEC 62304 process artifacts (development plan, configuration management, verification/validation records). Already referenced; need full audit trail. |

---

### 3. Risk Controls & Classification Rationale  

| IEC 62304 Class | Expected Harm | Example Software | Determination for GUI SW |
|-----------------|---------------|------------------|--------------------------|
| **Class B** | Minor injury or minor impact on clinical decision | General DICOM viewer + basic processing | Source table indicates typical use falls in Class B; risk controls must mitigate “moderate” hazards (e.g., incorrect image rendering). |

*Key Risk Controls to Include*  
- Input validation & error handling.  
- Verification of algorithm output against reference datasets.  
- Audit trail of user actions and software version.  
- Secure communication (TLS) for DICOM data exchange.  
- Periodic security patches governed by a **Predetermined Change Control Plan (PCCP)** (FDA final guidance Dec 2024).  

---

### 4. Evidentiary Gaps – Items Requiring Completion Before Submission  

| Gap | Why Critical |
|-----|---------------|
| **Explicit Intended Use Statement** | Drives predicate selection and labeling. |
| **Predicate Device Identification (510(k) number)** | Mandatory for substantial equivalence claim. |
| **Full Hazard Analysis & Risk Control Documentation** | Required by IEC 62304/ISO 14971 and FDA guidance; supports classification justification. |
| **Cybersecurity Threat Model & Mitigation Plan** | FDA expects documented controls per 2023 cybersecurity guidance. |
| **Usability/Human‑Factors Evidence (if applicable)** | Needed when software influences user decisions. |
| **Labeling Draft & UDI Assignment** | Required by 21 CFR §801 and §830.10 onward. |
| **QMSR (21 CFR §820) Compliance Proof** | Demonstrates FDA‑acceptable quality system for Class II devices. |
| **Predetermined Change Control Plan (if future AI/ML updates)** | Pre‑authorizes post‑market software modifications. |

---

### 5. Human‑Escalation Triggers  

1. **Missing Predicate Device** – Halt submission drafting; conduct market search and secure a suitable cleared comparator.  
2. **Incomplete Risk Management File** – Escalate to risk management lead for completion of FMEA, ISO 14971 analysis, and mitigation verification.  
3. **Cybersecurity Documentation Deficit** – Direct cybersecurity specialist to produce threat model & remediation plan before FDA review.  
4. **Labeling/UDI Gaps** – Engage labeling team; verify compliance with 21 CFR §801 and §830.10‑§830.60.  
5. **QMSR Non‑conformance** – Notify Quality Assurance to provide current ISO 13485 certificate and SOPs covering software development & change control.  
6. **Usability Evidence Required** – If functional claims affect clinical interpretation, trigger human factors review; otherwise document rationale for exemption.  

Each trigger should be logged in the project risk register and escalated to the Regulatory Project Lead for decision before proceeding to 510(k) compilation.

---

### 6. Peer Review Prompt  
*“Please review the assumptions made regarding classification (Class II under §892.2050), the sufficiency of the listed eSTAR deliverables, and any jurisdiction‑specific omissions—especially around predicate identification, cybersecurity documentation, and QMSR evidence. Identify gaps or alternative pathways that may affect clearance timing.”*

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> 원문의 'AEC·판독지원 포함 시 Class C 가능(Pre-Sub 확인 권장)' 조건이 다시 누락됨 — Class B 판정 시 전제 조건 병기 필요. 'Rationale→Requirements Traceability Matrix' 오타.

**Source Excerpts**

1. Chunk `1062081291234175249`

> ### 3.3 제품 3: 촬영실 GUI Software (영상 처리·표시 소프트웨어) #### 3.3.1 적용 규정·분류 - **Software as Medical Device (SaMD)** 해당 여부 먼저 확인 - 21 CFR 892.2050 (Class II) — Image Processing Software - FDA Guidance, "Guidance for the Content of Premarket Submissions for Device Software Functions" (2023-06-14 Final) - FDA Guidance, "Cybersecurity in Medical Devices" (2023-09-27 Final) - IEC 62304:2006+A1:2015 — Software lifecycle processes #### 3.3.2 SW Risk Class 결정 (IEC 62304) | Class | 기준 | 해당 SW 예시 | |-------|------|-------------| | A | SW 오동작 → 위해 없음 | 단순 뷰어 (진단 목적 아닌 경우) | | B | SW 오동작 → 경미한 위해 | 일반 DICOM viewer + basic processing | | C | SW 오동작 → 심각한 위해 또는...

2. Chunk `202482899914058233`

> #### 3.3.4 eSTAR 제출 패키지 구성 ``` eSTAR Section G (Performance Testing — Software): ├── Executive_Summary_GUI_SW_Validation.pdf ├── Software_Requirements_Specification.pdf ├── Software_Design_Specification.pdf ├── Requirements_Traceability_Matrix.xlsx ├── Software_Validation_Plan.pdf ├── Software_Validation_Report.pdf │ ├── Unit_Test_Results/ │ ├── Integration_Test_Results/ │ ├── System_Test_Results/ │ └── Performance_Test_Results/ ├── Validation_Dataset_Description.pdf └── Anomaly_Log_and_Resolution.xlsx └ 발견된 defect 및 해결 이력 ``` ---

### kb-eval-20261014-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA"], "profile_id": "ra-us", "scenario_id": "627c420a0b04790a", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md", "source_hash": "c24941843162416a7f4f756d0760525a63940e76c74c7aae200c4f4ffcfad8fe"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `627c420a0b04790a`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/FDA_AI_ML_2026_PCCP_%EC%9A%B4%EC%98%81_TPLC_%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8.md)
- Source hash: `c24941843162416a7f4f756d0760525a63940e76c74c7aae200c4f4ffcfad8fe`
- Focus: SaMD change impact
- Matched keywords: FDA

**Source Summary**

- 문서 요약: `FDA_AI_ML_2026_PCCP_운영_TPLC_업데이트.md`는 AI/ML 의료기기의 PCCP 및 변경관리 계획 작성 가이드입니다.
- 현재 excerpt 핵심: ### 8-E. Action (촬영실 GUI SW 팀 즉시 조치) 1. 자사 ML 정량영상 기능 로드맵을 **§892.2055 특수통제 7요소 체크리스트**로 매핑(설계초기). PCCP 동봉 결정 시 §2-A 3대 구성요소(Description/Protocol/Impact)와 §8-B(2)~(4) 일치 확인. 2. 학습데이터 코호트 정의서에 **인구학·교란요인·영상장비특성별 하위집단** 명시(§8-B(1)(ii)·(iii) 직접 요구). 3. 라벨링 SOP에 **버전이력·PCCP 변경통지** 절차 추가(§8-B(4)(vii)). 기존 IFU 템플릿(`04_템플릿/IFU_*`)에 PCCP 섹션 보강. 4. QMSR 설계관리 절차서에...
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

> **Regulatory Draft – ML‑Based Quantitative Imaging Software (SaMD)**  

---

### 1. Classification & Submission Pathway  
| Item | Determination |
|------|---------------|
| **Device class** | Class II – “Medical image management and processing system” (21 CFR §892.2050). The FDA’s recent classification notice (Federal Register 2026‑12166) places radiology‑focused ML devices in this class. |
| **Regulatory route** | Traditional 510(k) submission. A prior petition for exemption from 510(k) review was denied (see Federal Register notice 2026‑12166). Therefore a substantive substantial‑equivalence argument is required. |

### 2. Core Evidence Required  

| Requirement | Content to be supplied |
|-------------|------------------------|
| **Predicate device(s)** | Identify at least one cleared device in the same class and with comparable intended use (e.g., a FDA‑cleared radiology image analysis package). Provide 510(k) numbers and a side‑by‑side comparison of functional, performance, and labeling attributes. |
| **Device description** | Full software architecture, algorithms (including ML model type, training/validation datasets), versioning scheme, intended use statement, UI screenshots, hardware platform (if any). |
| **Algorithm validation** | • Training data set demographics & stratification (population, confounding factors, equipment‑specific subgroups) – as required by the internal checklist referenced in §8‑B(1)(ii)/(iii). <br>• Independent testing dataset with statistical power to demonstrate accuracy, precision, repeatability, and robustness across device settings. |
| **Clinical performance** | Prospective or retrospective clinical study (or well‑justified bridging data) showing that the software’s quantitative outputs are at least as accurate/clinically useful as the predicate. Include sensitivity, specificity, limits of agreement, bias analysis. |
| **Risk Management** | ISO 14971‑based risk analysis file covering software hazards, failure modes, residual risk, and mitigation controls (including IEC 62304 processes). |
| **Software lifecycle documentation** | • Summary of the Predetermined Change Control Plan (PCCP) – description, protocol, impact assessment as per FDA guidance (December 2024). <br>• Software Development Plan, Verification & Validation reports, version control matrix. |
| **Quality System compliance** | Evidence of adherence to QMSR (21 CFR §820), including design controls (§820.30) and traceability matrices linking requirements to verification outputs. The source mentions addition of a “특수통제 추적성 매트릭스” – confirm that this aligns with §820.30 inputs/outputs. |
| **UDI & Labeling** | Assign a UDI according to 21 CFR §§830.10‑§830.60; submit labeling package complying with 21 CFR §801 (IFU, safety information, PCCP section). |
| **Cybersecurity** | FDA’s “AI/ML‑Enabled Device Software Functions” guidance – describe threat model, safeguards, post‑market monitoring plan. |

### 3. Missing / To‑Be Confirmed Information  

| Item | Why needed & source note |
|------|-------------------------|
| Exact intended use wording (clinical indication, patient population) | Not present in excerpts; essential for predicate comparison. |
| Predicate device identifiers (510(k) numbers) | Must be sourced from FDA databases; not supplied here. |
| Detailed algorithm architecture and “black‑box” explainability strategy | Required to support substantial‑equivalence claim and risk analysis; absent. |
| Full PCCP documentation (Description, Protocol, Impact) | Excerpt cites §2‑A components but does not include the actual plan. |
| Verification that the device meets the “special control checklist” referenced as **§892.2055** – no such section exists in current Part 892; this appears to be an internal designation. → *no specific identifier found in source — verify separately*. |
| Evidence of compliance with IEC 62304 (software lifecycle) and IEC 60601‑1‑2 (EMC) if the software interacts with radiology hardware. | Not mentioned in excerpts. |

### 4. Recommended Risk Controls  

1. **Design controls** – per §820.30, maintain requirements traceability to verification results.  
2. **Software safety classification** – follow IEC 62304 (class B).  
3. **Residual risk acceptance** – documented in ISO 14971 file; ensure any remaining risk is “as low as reasonably practicable” (ALARP).  
4. **Cybersecurity safeguards** – authentication, integrity checks, secure update mechanism aligned with FDA AI/ML guidance.  
5. **PCCP implementation** – pre‑authorise foreseeable changes; maintain change log and impact assessments for each version release.  

### 5. Key Citations  

| Reference | Type |
|-----------|------|
| 21 CFR §892.2050 – Class II “Medical image management and processing system” | Framework reference (classification rule) |
| Federal Register notice **2026‑12166** – “Classification of Radiological Machine‑Learning Based Devices” (2026‑06‑17) | Instance identifier (regulatory instrument) |
| FDA Guidance – *Predetermined Change Control Plan for AI/ML* (Dec 2024) | Framework reference |
| 21 CFR §820.30 – Design controls | Framework reference |
| 21 CFR §§830.10‑§830.60 – UDI requirements | Framework reference |
| 21 CFR §801 – Labeling | Framework reference |

*No specific identifier found in source for the “§892.2055 특수통제 7요소 체크리스트” – verify separately.*

### 6. Human‑Escalation Triggers  

| Trigger | Action Required |
|---------|-----------------|
| **Absence of a suitable predicate** (no cleared device with comparable intended use) | Escalate to senior regulatory lead; consider De Novo pathway. |
| **Significant algorithm change** (new model architecture, training data set >30 % different) not covered by existing PCCP | Pause release; submit supplemental 510(k) or new 510(k). |
| **Unresolved UDI issuance** (FDA has not assigned a device identifier) | Notify QMS manager and engage FDA via pre‑sub. meeting request. |
| **Adverse event rate > pre‑defined threshold** (e.g., serious injury related to quantitative output) | Initiate Medical Device Reporting per 21 CFR §803; consider Field Action. |
| **QoS non‑conformance in design verification** (failure to meet performance specs) | Halt labeling finalization; conduct root‑cause analysis and re‑test before submission. |
| **Cybersecurity breach or vulnerability disclosure** | Immediate Incident Response; notify FDA under 21 CFR §806 if required. |

---

### 7. Peer Review Prompt  

*“Colleague, please review the assumptions made regarding (a) the applicability of 21 CFR §892.2050 to this ML‑based quantitative imaging software, (b) the completeness of the predicate device search given the recent FDA classification notice 2026‑12166, and (c) any jurisdiction‑specific gaps—particularly Korean internal references such as ‘§892.2055’ and the Korean‑language checklist—that might affect U.S. submission requirements.”*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> FR 2026-12166(신규 분류 공고)과 91 FR 58817(510(k) 면제 청원 거부) 공고 혼동. '데이터셋 >30% 변화' 근거 없는 수치. §820.30 인용은 원문 전파(원문은 2026-10-14 정정 완료 — ISO 13485 §7.3, §820.10 경유).

**Source Excerpts**

1. Chunk `1025191857057590007`

> ### 8-E. Action (촬영실 GUI SW 팀 즉시 조치) 1. 자사 ML 정량영상 기능 로드맵을 **§892.2055 특수통제 7요소 체크리스트**로 매핑(설계초기). PCCP 동봉 결정 시 §2-A 3대 구성요소(Description/Protocol/Impact)와 §8-B(2)~(4) 일치 확인. 2. 학습데이터 코호트 정의서에 **인구학·교란요인·영상장비특성별 하위집단** 명시(§8-B(1)(ii)·(iii) 직접 요구). 3. 라벨링 SOP에 **버전이력·PCCP 변경통지** 절차 추가(§8-B(4)(vii)). 기존 IFU 템플릿(`04_템플릿/IFU_*`)에 PCCP 섹션 보강. 4. QMSR 설계관리 절차서에 §892.2055 특수통제 추적성 매트릭스 추가(§820.30 입력·출력 매핑). ---

2. Chunk `1034015376307744884`

> > 최종 갱신: 2026-09-18 (주간모니터 #17 — §9 추가: 방사선 CAD 510(k) 면제 청원 **거부** 확정, 91 FR 58817) / 2026-06-17 (#4 — §8 방사선 ML 정량영상 SW 분류) > 근거: https://www.federalregister.gov/documents/2026/06/17/2026-12166/medical-devices-radiology-devices-classification-of-the-radiological-machine-learning-based | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing | https://www.federal...

### kb-eval-20261014-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "6e87122ab7767f26", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_05_Software_Section.md", "source_hash": "17067eef9c351571ca7c8dedcea62a4c6b790ae298cec359778dca145c690031"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `6e87122ab7767f26`
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

| Item | Determination / Requirement | Rationale & Citations |
|------|----------------------------|-----------------------|
| **1. Device Classification & Submission Pathway** | • Likely **Class II** (special controls) with a 510(k) submission under **21 CFR §807**. <br>• If the software is an image‑processing/analysis tool for radiology, the appropriate device class is **§892.2050 – Medical image management and processing system (Class II)**. | • FDA’s classification framework places most SaMD in Class II unless low‑risk (Class I) or high‑risk (Class III). <br>• Imaging‑related functions fall under **21 CFR Part 892**; the nearest listed class is §892.2050. |
| **2. Core Submission Content** | • **510(k) Summary/Statement** identifying predicate device(s). <br>• **Device Description & Intended Use** (clinical indication, user population, environment of use). <br>• **Software Documentation** per IEC 62304 (SDLC plan, architecture, design specs, verification & validation reports). <br>• **Risk Management File** (RM Plan, Hazard Analysis, Risk Controls, Residual Risk Evaluation) conforming to ISO 14971:2019. <br>• **SBOM** and SOUP inventory with justification of use. <br>• **Predetermined Change Control Plan (PCCP)** for any AI/ML model updates (FDA Dec 2024 final guidance). <br>• **Cybersecurity Assessment** (threat modeling, mitigation). <br>• **Labeling** complying with 21 CFR §801. | • ISO 14971:2019 – required risk management content. <br>• IEC 62304 §7 – software hazard analysis linked to architecture design (source excerpt [1]). <br>• FDA “Predetermined Change Control Plan (PCCP)” guidance Dec 2024 – AI/ML change control (source excerpt [2]; no identifier supplied → verify separately). |
| **3. Evidence Package** | • **Analytical Performance**: software functional testing, algorithm accuracy, precision, reproducibility. <br>• **Clinical Validation** (if claim involves diagnosis or treatment decisions): prospective/retrospective clinical study data, or literature support where appropriate. <br>• **Verification & Validation** reports demonstrating that the implementation meets design inputs and user needs. <br>• **Usability Engineering** per IEC 62366‑1 if UI poses safety risk. <br>• **Cybersecurity Vulnerability Test Results** (e.g., penetration testing, patch management). | • FDA guidance on SaMD performance & clinical evaluation (no specific identifier in source – verify separately). |
| **4. Missing Information (to be provided before final submission)** | • Exact **intended use statement** and **clinical indication**.<br>• Identification of a **predicate device** (510(k) number, registration date, classification reference).<br>• Detailed **risk analysis matrix** linking hazards → controls → verification traceability (source excerpt [1] mentions “위험 → 통제 조치 → 검증 추적성 매트릭스” but the actual matrix is not supplied).<br>• **SOUP list** with version, supplier, justification and any known vulnerabilities.<br>• **SBOM** – full component inventory (source notes SBOM requirement, no details provided).<br>• **PCCP scope**: pre‑specified change types, monitoring criteria, post‑change verification plan. | All items flagged as absent from the source excerpts; they must be assembled for a complete 510(k) package. |
| **5. Key Risk Controls (to be documented)** | • **Risk Management Process** per ISO 14971:2019 – hazard identification, risk analysis, evaluation, mitigation, residual‑risk acceptance.<br>• **Software Development Lifecycle controls** (IEC 62304) – architecture design, coding standards, unit/integration testing, verification traceability.<br>• **SOUP Management** – use‑restriction, vulnerability monitoring, patching strategy.<br>• **Cybersecurity Controls** – authentication, encryption, audit logging, secure update mechanism.<br>• **PCCP** – predefined change categories, validation of updated AI/ML models before deployment.<br>• **Post‑Market Surveillance Plan** – periodic safety updates, incident reporting (21 CFR §803). | References: ISO 14971, IEC 62304 §7 (source [1]), FDA PCCP guidance (source [2]). |
| **6. Human‑Escalation Triggers** | • **Change outside PCCP scope** (e.g., new algorithm architecture, different input data) → requires supplemental 510(k) or PMA amendment.<br>• **Residual risk exceeds acceptance criteria** after mitigation → pause deployment; conduct additional testing and re‑submit risk analysis.<br>• **Discovery of a critical vulnerability in SOUP component** that cannot be patched promptly → issue field correction/removal (21 CFR §806) and notify FDA.<br>• **Failure to meet performance specifications in validation** → halt market release; redesign or collect additional clinical data.<br>• **Regulatory feedback indicating mis‑classification** (e.g., predicate not appropriate) → reassess classification; consider De Novo pathway. | These triggers align with FDA’s change‑control expectations and post‑market reporting requirements. |

---

### Peer Review Prompt
*Please review the above assumptions about device class, required evidence, and identified gaps. In particular:*

1. *Is the use of §892.2050 appropriate without a confirmed imaging claim?*  
2. *Are any additional FDA guidance documents (e.g., “Clinical Decision Support Software” policy) relevant to this SaMD?*  
3. *Does the outlined evidence package sufficiently address AI/ML‑specific validation per the PCCP framework?*  

**Action:** Provide comments or corrections so that the final submission checklist can be finalized.

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> PCCP 범위 밖 변경은 'supplemental 510(k)'가 아니라 새 510(k)/De Novo/PMA Supplement(같은 KB 기준). ISO 14971:2019·SBOM/524B 인용 정확.

**Source Excerpts**

1. Chunk `1023300943338888510`

> ### 5.3 Document 3: Risk Management File **목적**: ISO 14971:2019 준거 소프트웨어 위험 관리 근거. **필수 포함**: - Risk Management Plan (허용 기준 포함) - 위험 분석·평가·통제·잔여 위험 허용성 판단 - Risk Management Report - 위험 → 통제 조치 → 검증 추적성 매트릭스 **IEC 62304 § 7 연계**: 위험 상황에 기여하는 소프트웨어 항목 분석 결과를 아키텍처 설계(§5.3)와 연결. 이 분석이 Document 1·2·3을 동시에 채우는 핵심 교차점. ---

2. Chunk `1150973762104113645`

> + SOUP (IEC 62304) | SOUP 목록 (IEC 62304 준수) | SOUP 목록 (IEC 62304) + SBOM (SBOM 의무는 FDA 524B; MDR은 명시 SBOM 요건 없음 — MDCG 2019-16 사이버보안 준용) | | AI/ML 소프트웨어 | PCCP (Predetermined Change Control Plan, 2024 Final) | AI 의료기기 가이드라인 (MFDS 2025) | MDCG 2021-6 AI 가이던스 |

### kb-eval-20261014-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_us-005", "iteration": 1, "matched_keywords": ["QMSR"], "profile_id": "ra-us", "scenario_id": "1aabb4c3b87fc3fd", "source": "github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md", "source_hash": "0b4d90c3b335bff693c8b64a4f4fa30c683c429ccbc99a427eed2081e27deb02"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `1aabb4c3b87fc3fd`
- Source: `github:holee9/ra-project/01_규제지식베이스/국제표준_IEC_ISO/KGMP_QMSR_ISO13485_비교_통합전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EC%A0%9C%ED%91%9C%EC%A4%80_IEC_ISO/KGMP_QMSR_ISO13485_%EB%B9%84%EA%B5%90_%ED%86%B5%ED%95%A9%EC%A0%84%EB%9E%B5.md)
- Source hash: `0b4d90c3b335bff693c8b64a4f4fa30c683c429ccbc99a427eed2081e27deb02`
- Focus: SaMD change impact
- Matched keywords: QMSR

**Source Summary**

- 문서 요약: `KGMP_QMSR_ISO13485_비교_통합전략.md`는 ISO 13485를 공통 QMS master로 두고 KGMP, FDA QMSR, EU MDR의 지역별 추가 요구사항을 통합 관리하는 전략 문서입니다.
- 현재 excerpt 핵심: II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동...
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

> **Regulatory Draft – SaMD Change‑Impact Assessment for “촬영실 GUI SW” (Imaging‑Room GUI Software, independent medical device)**  

---

### 1. Device Classification & Submission Pathway  
| Item | Determination | Rationale / Citation |
|------|---------------|-----------------------|
| **Regulatory panel** | Imaging / radiology devices | 21 CFR Part 892 governs imaging equipment. |
| **Device class** | Class II (moderate risk) – Medical image management and processing system | Sub‑category matches §892.2050 (Class II). |
| **Premarket route** | Traditional 510(k) premarket notification | Required for new or substantially equivalent Class II devices (21 CFR §807). |
| **Alternative pathway** | De Novo classification (if no suitable predicate) | Consider if a predicate cannot be identified. |

---

### 2. Core Evidentiary Requirements  

| Requirement | Evidence to submit | Source / Regulatory citation |
|-------------|-------------------|------------------------------|
| **Intended Use & Indications for Use** | Clear narrative, user population, clinical setting (imaging suite) | No specific identifier found in source – verify separately. |
| **Predicate Device Identification** | 510(k) number(s), comparison matrix (functional and technological characteristics) | No specific identifier found in source – verify separately. |
| **Software Development Lifecycle (SDLC)** | Full lifecycle documentation: SDP, SRS, SAD, SVP, SVR (all required) | KGMP ↔ QMSR mapping; IEC 62304 Safety Class C (see source). |
| **Software Validation** | Verification & validation plan/report, regression‑test automation results, change‑control SOPs | IEC 62304 §8.1 (source). |
| **Risk Management File** | ISO 14971 risk analysis, risk evaluation, mitigations, and verification of controls; traceability matrix to software requirements | No specific identifier found in source – verify separately. |
| **Cybersecurity** | Threat model, SBOM, compliance with MFDS Cybersecurity Guideline 2025, FDA 524B PCCP, MDCG 2019‑16 Rev.1 | Source lists all three frameworks. |
| **AI/ML Change Management (if applicable)** | Predetermined Change Control Plan (PCCP) per FDA final guidance (Dec 2024), alignment with EU AI Act Art.43(4) pre‑approval change process | FDA PCCP (2024‑12‑03 Final); EU AI Act Reg. 2024/1689 Art.43(4) – source. |
| **Post‑Market Surveillance (PMS) / Periodic Safety Update Report (PSUR)** | PMS plan, PSUR data collection, linkage to IEC 62304 & MDR Art.83‑86 (as noted) | Source notes “PSUR/PMSR 연동”. |
| **Complaint handling** | Complaint investigation records; completion timestamps per §820.20 | §820.20 – source. |
| **Service / Maintenance Records** | Detailed service logs, preventive maintenance documentation per §820.35 | §820.35 – source. |
| **Internal Audits & FDA Inspection Readiness** | Audit program, corrective‑action records; note that “FDA 실사 대상” (formerly QSR §820.180(c) exemption removed) applies | Source. |
| **Quality Management System (QMS)** | Conformance to new QMSR (21 CFR §820, effective 02‑2026), ISO 13485 alignment, documented procedures for all above elements | Source mapping table; “QMSR” referenced throughout. |
| **Labeling & UDI** | Label draft meeting §801, UDI assignment per Part 830 (label must bear a UDI, §§830.10–830.60) | No specific identifier found in source – verify separately. |

---

### 3. Identified Information Gaps  

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **Exact Intended Use statement** | Needed for predicate comparison & labeling | Obtain from product marketing/clinical team. |
| **Predicate device(s) with cleared 510(k) numbers** | Required to demonstrate substantial equivalence | Perform market search; document differences. |
| **Risk Management File (ISO 14971)** | Mandatory for Class II devices | Compile FMEA/FMECA, risk control verification. |
| **AI/ML algorithm change scope** (if present) | Determines need for PCCP & possible new 510(k) | Define algorithm versioning, trigger criteria, submit PCCP. |
| **UDI issuance plan** | Part 830 compliance before market launch | Select issuing agency, generate GUDID submission. |
| **Clinical validation data (if required)** | May be needed if software performs image analysis/diagnosis | Prepare study protocol or real‑world performance data. |
| **Software Bill of Materials (SBOM)** | Cybersecurity evidence per FDA & MDCG guidance | Generate SBOM for all third‑party components. |

---

### 4. Key Risk Controls (mapping to ISO 14971)  

| Hazard | Control(s) | Verification Evidence |
|--------|------------|-----------------------|
| Incorrect image display / manipulation | IEC 62304 Class C software safety mechanisms; UI usability testing; functional verification | Validation test reports, traceability matrix. |
| Unauthorized access / data breach | Threat model, SBOM, encryption, authentication per MFDS 2025 & FDA PCCP | Cybersecurity assessment report, penetration‑test results. |
| Algorithm drift (AI/ML) | Predetermined Change Control Plan (PCCP) with pre‑specified performance boundaries; continuous monitoring | PCCP document, monitoring logs, PSUR updates. |
| Software bugs introduced by updates | Regression test automation, change‑control SOP, configuration management per QMSR §820.35 | Test automation logs, change request records. |
| Failure to maintain service/maintenance logs | Service record requirement (§820.35) | Completed service log entries. |

---

### 5. Regulatory Citations (as appeared in source)

| Citation | Meaning |
|----------|---------|
| **§820.20** – Complaint investigation completion timestamp | Required for feedback handling (source: 8.2.1). |
| **§820.35** – Service records detailed requirements | Required for production/service documentation (source: 7.5). |
| **IEC 62304 §8.1** – Software validation activities | Basis for SDLC validation (source: SW 밸리데이션 line). |
| **FDA 524B PCCP** – Predetermined Change Control Plan guidance (Dec 2024) | AI/ML change‑control framework (source). |
| **MDCG 2019‑16 Rev.1** – EU cybersecurity guidelines for medical devices | Complementary cyber risk control (source). |
| **MFDS 사이버보안 가이드라인 2025** – Korean cybersecurity guideline | Additional regional requirement (source). |
| **EU AI Act Reg. 2024/1689 Art.43(4)** – Pre‑approval change for high‑risk AI medical devices | Aligns with FDA PCCP concept (source). |

---

### 6. Human‑Escalation Triggers  

1. **Change to Intended Use, Indications, or Clinical Function** → Pause release; trigger regulatory review and possible new 510(k).  
2. **Introduction of new AI/ML algorithm version that exceeds pre‑specified performance bounds** → Require submission of updated PCCP and possibly supplemental 510(k).  
3. **Failure to close a complaint within the timeframe required by §820.20** → Escalate to senior QA & consider FDA MDR (Medical Device Reporting) filing.  
4. **Detection of a cybersecurity vulnerability classified as “high severity”** → Immediate incident response; notify FDA (if required) and MFDS, suspend deployment until mitigation.  
5. **Regulatory inspection finding non‑conformance to QMSR (e.g., missing service records §820.35)** → Escalate to compliance officer for corrective action plan.  

---

### 7. Action Summary  

| Immediate actions | Owner | Due |
|-------------------|-------|-----|
| Draft Intended Use & Indications statement | Product Management | 2026‑10‑21 |
| Identify qualified predicate 510(k)(s) | Regulatory Lead | 2026‑10‑28 |
| Compile Risk Management File (ISO 14971) | QA/RA | 2026‑11‑04 |
| Prepare PCCP (if AI/ML present) | Software Engineering & RA | 2026‑11‑11 |
| Generate SBOM & conduct threat modelling | Cybersecurity Team | 2026‑11‑11 |
| Map all QMSR procedures to §820.20, §820.35, IEC 62304 | QMS Lead | 2026‑11‑18 |
| Draft labeling & UDI plan (Part 830) | Labeling Specialist | 2026‑11‑25 |

---

#### Peer‑Review Prompt  
*Please review the assumptions above:*

- *Is §892.2050 the most appropriate classification for a GUI that controls imaging acquisition, or should another subsection be considered?*  
- *Have we captured all evidence gaps, especially concerning EU MDR/AI Act obligations?*  
- *Are there any jurisdiction‑specific requirements (e.g., MFDS registration) that need explicit inclusion beyond what is noted?*  

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> '§820.20 — 불만 파일'은 원문(KGMP_QMSR_비교) 오류의 전파였고 원문은 §820.35(a)로 정정 완료(2026-10-14) — 이 답변 기준일에는 원문이 미정정 상태였음. 이후 인용 시 §820.35(a) 사용.

**Source Excerpts**

1. Chunk `1012828200772392062`

> II Tech Doc 연계 | | **7.4 구매** | ISO 동일 | ISO 동일 | ISO 동일 | | **7.5 생산 및 서비스** | ISO 동일 | §820.35 — Service Records 상세 요건 추가 | ISO 동일 | | **7.6 측정장비 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.1 측정·분석·개선** | ISO 동일 | ISO 동일 | ISO 동일 + PSUR/PMSR 연동 | | **8.2.1 피드백** | ISO 동일 | §820.20 — 불만 조사 완료 시점 기록 | PMS 데이터 수집 의무 (MDR Art. 83~86) | | **8.2.2 내부 감사** | ISO 동일 | **FDA 실사 대상** (구 QSR §820.180(c) 예외 삭제) | NB 불시 감사 대상 | | **8.2.3 공정 모니터링** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.3 부적합 관리** | ISO 동일 | ISO 동일 | ISO 동일 | | **8.4 데이터 분석** | ISO 동일 | ISO 동일 | PSUR/PMSR 작성 근거 데이터 | | **8.5 개선** | ISO 동일 | ISO 동일 | ISO 동일 |

2. Chunk `1111721272977030404`

> ### 5-3. 촬영실 GUI SW (SaMD — 독립형 의료 소프트웨어) | QMS 요건 | KGMP | QMSR | MDR | 맵핑 포인트 | |---|---|---|---|---| | SW 개발 수명주기 | 디지털의료제품법령 연계 | IEC 62304 Safety Class C | IEC 62304 Class C | SDP·SRS·SAD·SVP·SVR 전 문서 필수 | | SW 밸리데이션 | KGMP + 디지털의료제품법 | IEC 62304 §8.1 | IEC 62304 §8.1 | Regression Test 자동화, 변경 관리 SOP | | 사이버보안 | MFDS 사이버보안 가이드라인 2025 | FDA 524B PCCP | MDCG 2019-16 Rev.1 | Threat Model + SBOM + PCCP 통합 | | AI/ML 기능 (해당 시) | 디지털의료제품법 | FDA PCCP (2024-12-03 Final) | EU AI Act (Reg. 2024/1689): AI 의료기기=고위험, MDR 적합성평가에 통합, 고위험 의무 2027-08-02 적용 | PCCP(FDA) ↔ AI Act Art.43(4) 사전확정 변경(재적합성평가 불요) 유사 — 작성 필요 여부 판단 | | 불만 처리 | MFDS 보고 | MDR 30일...

## ra_eu

### kb-eval-20261014-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d6eecc9bbb14765c", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d6eecc9bbb14765c`
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

> **Regulatory Draft – Determination of Classification, Conformity‑Assessment Route and Required Evidence**

---

### 1. Device information required before classification  
| Item | Why needed | Current status (source) |
|------|------------|------------------------|
| Trade name / model | Identifies the product family | not provided |
| Intended purpose (indication, target patient group, mode of action) | Drives the rule‑based classification (Annex VIII) and determines whether the device is active, measuring, invasive, etc. | missing – only a generic “제품 설명” placeholder in §1 Device Description (source [1]) |
| Duration of contact with the body & invasiveness | Determines applicability of Rules 9–11, 17, 22‑23 | missing |
| Software component (if any) and its decision impact | Needed for Rule 11 classification | not disclosed |
| Sterility / measuring function | Triggers the limited scope NB route for Is/Im/Ir | not disclosed |
| Materials & manufacturing process | Required for Annex II §3 Design & Manufacturing | only a generic reference in source [1] |

**Conclusion:** Classification cannot be finalised until the above data are supplied.

---

### 2. Likely classification pathway (framework citation)  

- **Art. 52 MDR 2017/745** defines the conformity‑assessment route once the class is known.  
| Class | Mandatory NB involvement (per Art. 52) | Possible routes |
|-------|-----------------------------------------|----------------|
| I (non‑sterile, non‑measuring, non‑reusable surgical) | **Art. 52(7)** – self‑declaration; technical documentation Annex II & III + EU Declaration of Conformity Annex IV | No NB required |
| Is / Im / Ir | **Art. 52(7)** – limited‑scope NB audit (Annex IX Ch.I & III or Annex XI Part A) | NB only for sterile/measuring/reusable aspect |
| IIa | **Art. 52(6)** – full technical‑documentation assessment by NB (Annex IX Ch.I & III + §4) *or* Annex II/III + Annex XI §10 or §18 | NB required |
| IIb | **Art. 52(4)** – either Annex IX full assessment (representative device per generic group) **or** Annex X type‑examination plus Annex XI | NB required |
| III | **Art. 52(3)** – Annex IX full assessment *or* Annex X + Annex XI | NB required |

> **Citation:** Art. 52 MDR 2017/745; Annex II (Technical Documentation) – source [2].

---

### 3. Technical documentation – evidence to be compiled (Annex II)

| Annex II Chapter | Content that must be provided | Source citation |
|------------------|--------------------------------|-----------------|
| **§1 Device Description** | Full narrative of intended purpose, indications, contraindications, principle of operation, and variants. | source [1] – “§1 Device Description” |
| **§2 Labeling** | Labels & IFU meeting Annex I §23 (including symbols, warnings, CE mark). | source [1] – “§2 Labeling” |
| **§3 Design & Manufacturing** | Detailed description of design, materials, manufacturing processes, and quality‑management evidence. | source [1] – “§3 Design & Manufacturing” |
| **§4 GSPR Checklist** | Mapping of each General Safety & Performance Requirement (Annex I §§1‑23) to supporting data (e.g., bench test results, biocompatibility). | source [1] – “§4 GSPR Checklist” |
| **§5 Risk Management** | Complete ISO 14971 risk management file (hazard analysis, risk evaluation, control measures, residual risk assessment). | source [1] – “§5 Risk Management” |
| **§6 Verification & Validation** | V&V protocols and reports demonstrating conformity to the specification and intended purpose. | source [1] – “§6 Verification & Validation” |

*All sections must be compiled in the language(s) required by the NB (minimum English, plus any additional language stipulated).*

---

### 4. Clinical evidence (Annex XIV)

| Requirement | Evidence needed |
|-------------|-----------------|
| **Clinical Evaluation Report (CER)** – Annex XIV Part A, kept current under Art. 61 | Systematic literature review, clinical data from equivalent devices, and/or post‑market clinical follow‑up (PMCF) results. |
| **PMCF Plan & Report** – Annex XIV Part B (for Class IIa–III) | Prospective or retrospective study plan, methodology, safety endpoints, and final analysis. |

> **Citation:** Annex XIV (clinical evaluation); Art. 61 MDR – source [2] (related annexes listed).

---

### 5. Post‑Market Surveillance (PMS)

| Article / Annex | Required artefact |
|-----------------|-------------------|
| **Art. 83** – PMS system | Organized process for collecting and analysing post‑market data. |
| **Art. 84** – PMS plan | Detailed description of activities, frequency, and responsibilities. |
| **Art. 86** – Periodic Safety Update Report (PSUR) for Class IIa/IIb/III | Benefit–risk conclusions, PMCF findings, sales volume & user population. Updated at least every 2 years (IIa) or annually (IIb/III). |
| **Annex III** – PMS technical documentation | Integration of PMS data into the overall technical file. |

> **Citation:** Articles 83‑86 MDR; Annex III – source [2].

---

### 6. Risk controls & GSPR compliance

1. **Risk Management (ISO 14971) → Annex I §§10‑22**  
   *Identify hazards related to the device’s intended use, apply inherent safety, protective measures and information for users (e.g., warnings, training).*

2. **Verification of design outputs against risk control measures** – documented in §6 Verification & Validation (source [1]).

3. **Labeling & IFU** must contain all required safety information per Annex I §23 (source [1] §2).

4. **Usability engineering (IEC 62366‑1)** if the device is intended for lay users or has a user interface (not explicit in source – to be confirmed).

---

### 7. Identified gaps / missing information

| Gap | Impact on regulatory dossier |
|-----|------------------------------|
| **Intended purpose & mode of action** | Prevents rule‑based classification; blocks preparation of §1 Device Description and GSPR mapping. |
| **Whether the device is sterile, measuring or a reusable surgical instrument (Is/Im/Ir)** | Determines need for limited‑scope NB audit. |
| **Software classification details (if any)** | Affects Rule 11 application and possibly higher class (IIb/III). |
| **Clinical data source(s) – equivalence justification** | Needed for CER & PMCF plan; without it the clinical evaluation cannot be completed. |
| **Materials & manufacturing process specifics** | Required for §3 Design & Manufacturing, biocompatibility assessment, and risk analysis. |
| **Intended user (professional vs lay)** | Influences Annex I §§22‑23 labeling requirements and possibly the need for additional usability testing. |

---

### 8. Human‑escalation triggers

| Trigger condition | Recommended escalation |
|-------------------|------------------------|
| *Unable to resolve classification after receiving intended purpose* | Escalate to Senior RA Lead for rule‑application workshop (Annex VIII). |
| *Missing or insufficient clinical data for CER* | Notify Clinical Development team; trigger a formal gap analysis before NB submission. |
| *Risk management file does not demonstrate residual risk < acceptability criteria* | Raise to Head of R&D/Quality for redesign or additional safety testing. |
| *NB raises non‑conformities on any Annex II chapter during audit* | Open a corrective‑action work package; inform Project Manager and senior compliance officer. |
| *PMS system not operational within 6 months of market launch* (Art. 83) | Escalate to Post‑Market Surveillance Lead – possible regulatory breach. |

---

### 9. Peer‑review prompt  

> **Colleague request:** Please review the assumptions made above, especially the mapping of Annex II sections to the required deliverables and the identification of classification routes. Verify that no jurisdiction‑specific obligations (e.g., MFDS annexes mentioned in source [1]) have been omitted for a device intended for European market only. Highlight any additional evidence that may be required under the latest MDCG guidance or recent MDR amendments.

--- 

*Prepared by Theo – EU RA Specialist*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

### kb-eval-20261014-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "0096ecffd586d10d", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/NB_심사자료/NB_Deficiency_Letter_대응전략.md", "source_hash": "a15dac973609fe746d7da46354e047b528ec5e8df970abafcb115620bea402ba"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `0096ecffd586d10d`
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

> **Regulatory Draft – EU MDR Assessment of a Diagnostic X‑ray System**

---

### 1. Device Classification & Conformity‑Assessment Route  

| Item | Determination | Regulatory citation |
|------|---------------|---------------------|
| **Intended purpose** | “Standard diagnostic radiology” (X‑ray imaging) | – |
| **Core technology** | Active device that *emits ionising radiation* for diagnosis | MDR Rule 10 (Annex VIII) |
| **Resulting class** | **Class IIb** (active X‑ray equipment) | Rule 10 → Class IIb |
| **Chosen conformity‑assessment route** | Full technical‑documentation assessment by a Notified Body (NB) – **Annex IX** (Chapters I & III) plus post‑market verification (Annex XI) | Art. 52(4) MDR; Annex IX; Annex XI |

*Notes*:  
- Rule 10 places the system in Class IIb because it emits ionising radiation for diagnostic purposes.  
- The NB’s deficiency‑letter reference to “MDR Annex VII + 2026/977” concerns the procedural framework (structured dialogue, Art. 7 of the 2026/977 amendment) rather than a different classification route.

---

### 2. Evidence Required by the Notified Body  

| Evidence | Content required | Where it is mandated |
|----------|------------------|----------------------|
| **Clinical Evaluation Report (CER)** – latest version (Rev. 3) | • Clinical background, state‑of‑the‑art literature <br>• Clinical data demonstrating safety & performance <br>• Equivalence justification (see § 2 below) | Annex XIV Part A; kept current under Art. 61 |
| **Clinical equivalence dossier** | – Declaration that the device treats the *same clinical condition* as the predicate (standard diagnostic radiology). <br>– Demonstrated equivalent performance: DQE(0) ≥ 65 % (Test Report TR‑2024‑015, IEC 62220‑1‑1). | Annex XIV Part A; MDR Annex VII (equivalence requirement) |
| **Device‑specific test reports** | • IEC 60601‑2‑54 (X‑ray equipment for radiography/radioscopy) <br>• IEC 60601‑2‑28 (X‑ray tube assemblies) <br>• IEC 62220‑1‑1 (DQE measurement, report TR‑2024‑015) | MDR Annex IX Chapters I & III (technical documentation) |
| **Risk Management File** | • ISO 14971‑based risk analysis <br>• Controls for radiation protection (Annex I §16), electronic safety (§17), active device hazards (§18) <br>• Updated after any post‑market data | Annex I (GSPR); Annex IX |
| **Labeling & IFU** | • Conformity with Annex I §23 (labels, instructions for use) <br>• Specific warnings on radiation dose, user training, contraindications | Annex IV (Declaration of conformity) + Annex I §23 |
| **Quality Management System (QMS)** | • EN ISO 13485 certification <br>• Evidence of no outstanding QMS non‑conformities (or corrective actions) | Annex IX Chapters I & III |
| **Post‑Market Surveillance (PMS) Plan** | • PMS system per Art. 83 <br>• PSUR (Class IIb – annual) per Art. 86(2) | Art. 84 (plan), Art. 86 (PSUR) |
| **Declaration of Conformity** | Signed EU Declaration referencing all applicable GSRPs | Annex IV |

---

### 3. Identified Gaps & Missing Information (as highlighted in the NB deficiency letter)

1. **Clinical Evaluation – completeness**  
   *Missing*: Full justification for clinical equivalence beyond DQE value; lack of comparative clinical outcome data.  

2. **Technical Documentation – labeling**  
   *Missing*: Final version of IFU with radiation dose information, user training requirements, and compliance statements to Annex I §16‑§18.  

3. **Risk Management – residual risk assessment**  
   *Missing*: Updated risk evaluation after incorporation of the new DQE data; demonstration that residual risks are “acceptable” per Art. 10(9).  

4. **PMS & PSUR**  
   *Missing*: Draft PMS plan (Art. 84) and first‑year PSUR (Art. 86) – required for Class IIb devices before final approval.  

5. **QMS non‑conformities**  
   *Missing*: Evidence of closure of previously identified QMS NCs noted in earlier NB audit reports (no specific identifier supplied in source).  

6. **Standards compliance evidence** – IEC 60601‑2‑54 and IEC 60601‑2‑28 test certificates not attached.  

7. **Structured Dialogue documentation**  
   *Missing*: Minutes of the Art. 7 (2026/977) dialogue confirming agreed submission deadline.

---

### 4. Required Risk Controls & Mitigations

| Hazard | Control measure (per GSPR) | Reference |
|--------|----------------------------|-----------|
| **Radiation exposure to patient / staff** | • Interlock system, dose‑rate monitoring, automatic shut‑off <br>• Warning indicators and audible alarms <br>• Periodic calibration & verification of output (IEC 60601‑2‑54) | Annex I §16.4; IEC 60601‑2‑54 |
| **Electrical safety / EMC** | • Compliance with IEC 60601‑1 series, IEC 60601‑1‑2 (EMC) <br>• Protective earth, leakage current limits | Annex I §§10‑12 |
| **Software malfunction** (image acquisition/processing) | • IEC 62304‑based software lifecycle <br>• Usability testing per IEC 62366‑1 <br>• Fail‑safe default mode on error | Annex I §17; IEC 62304 |
| **Active device failure** (high voltage generator) | • Redundant safety circuits, over‑current protection <br>• Regular maintenance schedule | Annex I §18 |
| **User error (lay‑person use)** – not applicable (device intended for trained operators). | – | Annex I §22 |

All controls must be reflected in the Risk Management File and verified during the NB’s technical documentation review (Annex IX).

---

### 5. Human‑Escalation Triggers  

| Situation | Trigger point | Action & responsible role |
|-----------|---------------|----------------------------|
| **NB does not receive a response within the agreed deadline** (see Table in source – “답변 기한”) | Deadline passed without submission | RA Manager escalates to senior regulatory counsel; initiate formal request for extension via structured dialogue (Art. 7, 2026/977). |
| **Persistent QMS non‑conformities after two submissions** | Two consecutive deficiency letters concerning the same QMS NCs | Senior QA lead issues a “stop‑work” notice; project pause until corrective actions are verified. |
| **Inadequate clinical equivalence data (e.g., DQE alone insufficient)** | NB requests additional clinical outcome data | Clinical affairs team prepares supplemental clinical study or post‑market data collection plan; RA updates CER accordingly. |
| **PMS/PSUR not delivered by the first annual deadline** | 12 months after market launch for Class IIb | Risk management officer informs senior management; consider applying for a temporary extension under Art. 84(5). |
| **Regulatory change (e.g., new amendment to MDR or IEC standards)** | Publication of a relevant amendment before CE marking issuance | Regulatory affairs leads a impact assessment; update technical documentation and risk file within 30 days. |

If any trigger is activated, the case should be *flagged* in the project‑tracking system as **“Escalation – NB deadline breach”** or similar, with an assigned owner and target resolution date.

---

### 6. Summary Judgment  

- The X‑ray diagnostic system is **Class IIb** under MDR Rule 10 (active device emitting ionising radiation).  
- The appropriate conformity‑assessment route is **Annex IX** (full technical documentation assessment) combined with post‑market verification per **Annex XI** (Art. 52(4)).  
- The NB’s deficiency letter reveals gaps in the **CER/clinical equivalence justification, labeling, risk management updates, PMS/PSUR evidence, QMS closure, and conformity to IEC 60601‑2‑54 / ‑28**.  
- Addressing these items with the listed evidences and controls will satisfy the NB’s requirements and enable issuance of the CE marking.

---

### 7. Peer‑Review Prompt  

> **To a fellow EU RA:** Please review the assumptions made regarding (1) classification under Rule 10 versus any possible mixed‑rule approach for detector components, (2) the sufficiency of DQE ≥ 65 % as the sole equivalence metric, and (3) whether an Annex X type‑examination route could be viable given the device’s radiation safety scope. Identify any jurisdiction‑specific considerations that may have been overlooked (e.g., national “harmonised standards” adoption status or additional reporting obligations under local implementing regulations).  

---

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> ① 'MDR Annex VII=동등성 근거' — 동등성은 Art.61+Annex XIV(Annex VII은 NB 절차). ② 'Annex IX + Annex XI(post-market verification)'는 존재하지 않는 조합(Art 52(4): Annex IX 단독 또는 Annex X+XI). ③ PSUR 연1회 근거는 Art.86(1)(86(2)는 주기 조정 조항). ④ 'Art.84(5) 연장' 근거 없음. clock-stop·2026/977 Art.7·GSPR §16/17/18은 정확(10-10 대비 개선).

**Source Excerpts**

1. Chunk `1005517747960005544`

> 3. Clinical equivalence: - Same clinical condition: Both indicated for standard diagnostic radiology. - Equivalent clinical performance: DQE(0) ≥ 65% for both devices (Ref. Test Report TR-2024-015, IEC 62220-1-1). Revised CER Rev. 3 is attached as Annex A. ``` ---

2. Chunk `1014893419282866507`

> | 항목 | EU NB (MDR) | MFDS (국내) | FDA (미국) | |---|---|---|---| | 공식 용어 | Deficiency Letter | 보완 요청 | Additional Information (AI) Request | | 근거 법령 | MDR Annex VII + 2026/977 | 의료기기법 §12 + 허가·신고·심사 규정 | 21 CFR 807 + FDA Review Policy | | 답변 기한 | NB와 합의 (법정 상한 없음) | 1차 60일, 2차 60일 | 180일 (타임라인 기산일부터) | | 최대 중단 횟수 | 4회 (product verification 기준) | 2차까지 (실질 2회) | 제한 없음 (Interactive Review 가능) | | Clock-stop | 예 (NB 요청 당일 stop, 제출 익일 resume) | 예 (보완 기간 제외) | 예 (AI 발송일부터 stop) | | 미응답 시 | 평가 종료 / 불승인 | 취하 간주 | 허가 거부 | | 사전 대화 창구 | Structured Dialogue (Art.7, 2026/977) | 상담제도 (비공식) | Pre-Sub (Q-Sub) (공식, 문서화) | | 주요 결함 유형 | CER, TD, QMS NC, Labelin...

### kb-eval-20261014-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "a55885aa493a826e", "source": "github:holee9/MD-process/01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md", "source_hash": "15785f85bc1d2f5a79e327cf79517b4ec3e1639d879aca7d8246fbabd9afb2b5"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `a55885aa493a826e`
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

> **Regulatory Draft – X‑ray Radiography / Radioscopy System (EU MDR 2017/745)**  

---

### 1. Device Overview (as understood from the source)

| Item | Description |
|------|-------------|
| **Intended purpose** | Medical imaging system for projection radiography and fluoroscopy (diagnostic use of ionising radiation). |
| **Core technology** | X‑ray tube assembly, detector/image plate, image‑processing software. |
| **Relevant standards cited in the source** | IEC 60601‑2‑54 (X‑ray equipment), IEC 62304 (software life‑cycle), ISO 14971 (risk management), ISO 13485:2016 (QMS). |

---

### 2. Classification & Conformity‑Assessment Route  

| Aspect | Determination |
|--------|---------------|
| **MDR classification rule** | The system emits ionising radiation for diagnostic purposes → **Rule 10 (active devices for diagnosis/monitoring)**. Rule 10 places the device in **Class IIb** (see MDR Annex VIII, Rule 10). |
| **Applicable article** | **Art. 52(4) MDR 2017/745** – mandatory NB involvement for Class IIb. |
| **Conformity‑assessment route(s)** | 1. **Primary:** Annex IX (full technical documentation assessment) §§ I & III + Annex IX §4 assessment of the representative device. <br>2. **Alternative:** Annex X (type examination) *plus* Annex XI (production conformity verification). |
| **NB involvement** | Required for all steps listed above (technical file review, type‑examination or full dossier audit, issuance of certificate). |

---

### 3. Mandatory Technical Documentation (TD) – MDR Annex II  

| TD Section | Evidence required | Current status (per source) | Gap / Action |
|------------|-------------------|-----------------------------|--------------|
| **1. Device description & intended use** | Detailed functional description, indications, contraindications, user groups. | Not listed in the excerpt. | Obtain from R&D design dossier. |
| **2. Design & manufacturing information** | Manufacturing flow chart, Bill of Materials, process validation (including X‑ray tube assembly). | “설계·제조 정보” to be collected (Step 2) – not yet completed. | Collect and integrate into TD. |
| **3. Verification & Validation (V&V)** | Test reports (electrical safety, radiation output, image quality, software verification per IEC 62304/IEC 60601‑2‑54). | “V&V 결과 수집” planned (Step 2) – no evidence shown. | Ensure all test data are complete and traceable. |
| **4. Risk Management** | ISO 14971 risk management file, including residual risk evaluation (§18 MDR GSPR). | “위험관리 파일 통합” scheduled (Step 5) – pending. | Finalise RMF & map to GSPRs §§ 16‑20. |
| **5. Clinical Evaluation Report (CER)** | Annex XIV Part A CER, up‑to‑date with state‑of‑the‑art literature and any clinical data (including PMCF). | “임상평가 보고서(CER) 작성·갱신” (Step 4) – no artefact supplied. | Prepare full CER; verify inclusion of radiation safety clinical evidence. |
| **6. Post‑Market Surveillance (PMS)** | PMS Plan (Art. 84), PMS Report/PSUR (Art. 86 for Class IIb). | “PMS 계획서 작성” (Step 6) – plan not shown. | Draft PMS plan; schedule PSUR (annual). |
| **7. Labelling & IFU** | Labels, Instructions for Use, IEC‑60601‑2‑54 safety information (§16 MDR GSPR). | Not mentioned. | Develop and map to Annex I §23. |
| **8. UDI & Registry** | Unique Device Identifier issued, EUDAMED registration (Art. 33‑39). | No evidence provided. | Obtain UDI code; register device in EUDAMED. |

*All sections must be compiled into the approved Technical Documentation (Step 7 – “전체 TD 검토·승인”).*

---

### 4. Clinical Evidence Requirements  

| Requirement | Source/legal basis | Expected content |
|-------------|-------------------|------------------|
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 MDR. | • Systematic literature review of diagnostic X‑ray systems (state‑of‑the‑art). <br>• Clinical data from any pre‑market clinical investigations (if required) or equivalence justification with a recognised predicate device. <br>• Post‑Market Clinical Follow‑up (PMCF) plan & interim results (Annex XIV Part B). |
| **Post‑Market Clinical Follow‑up (PMCF)** | Annex XIV Part B. | • Prospective clinical data collection on radiation dose, image quality, adverse events. <br>• Alignment with GSPR §16 (radiation protection) and §17 (software). |
| **PSUR** (Periodic Safety Update Report) | Art. 86 MDR – required annually for Class IIb. | • Benefit‑risk determination conclusions.<br>• Summary of PMCF findings.<br>• Sales volume & user population estimate. |

*The source only mentions “임상평가 보고서(CER) 작성·갱신” (Step 4); no concrete CER or PMCF documentation is available – **missing**.*

---

### 5. Risk Controls – Mapping to GSPR (Annex I)

| GSPR § | Control measure required for X‑ray system | Current evidence |
|--------|-------------------------------------------|-------------------|
| **§16 – Radiation protection** | ‑ Shielding design, dose monitoring, compliance with IEC 60601‑2‑54 limits. | Not yet demonstrated; need radiation safety test reports. |
| **§17 – Electronic programmable systems / software** | ‑ Software validation per IEC 62304; cybersecurity assessment; usability per IEC 62366‑1. | No software lifecycle documentation provided. |
| **§18 – Active devices & connectivity** | ‑ Electrical safety, electromagnetic compatibility (EMC), fail‑safe modes for tube emission control. | Pending V&V results. |
| **§20 – Mechanical / thermal risks** | ‑ Physical robustness of gantry, protection against overheating of X‑ray tube. | Not shown. |
| **§22 – Use by lay persons** *(if intended)* | ‑ Clear IFU, safety interlocks. | No IFU available. |

*All controls must be reflected in the Risk Management File and cross‑referenced to the GSPR checklist (Step 3 – “GSPR 매핑 완성”).*

---

### 6. Submission Checklist for NB

1. **Approved Technical Documentation** (Annex II) – complete and signed off (Step 7).  
2. **Declaration of Conformity** (Annex IV).  
3. **Certificate of Free Sale / CE marking certificate** (issued by NB after conformity assessment).  
4. **PMS Plan & PSUR** (Art. 84, Art. 86) – at least the plan ready before submission; first PSUR due within 12 months of market entry.  
5. **UDI registration in EUDAMED** (Art. 33‑39).  
6. **Evidence of conformity to IEC 60601‑2‑54** (type test report or NB‑issued certificate).  

---

### 7. Identified Missing Information & Immediate Actions

| Missing Item | Why critical | Action Owner | Deadline |
|--------------|---------------|--------------|----------|
| Complete **V&V test reports** (radiation output, image quality, EMC) | Fulfils Annex II §§ 3‑5 and GSPR §16‑18. | R&D & QA | +2 weeks |
| Fully populated **Risk Management File** with GSPR mapping | Required for NB review & Art. 83 PMS system. | RA/QA | +1 week |
| **Clinical Evaluation Report (CER)** – final version including PMCF plan | Annex XIV Part A; informs benefit‑risk assessment. | RA/Clinical | +3 weeks |
| **PMS Plan** (Art. 84) and first **PSUR draft** (Art. 86) | Ongoing post‑market obligations for Class IIb. | RA Lead | +4 weeks |
| **Labeling & IFU** compliant with Annex I §23 & IEC 60601‑2‑54 | Mandatory for market entry. | RA/QA | +2 weeks |
| **UDI issuance & EUDAMED registration** | Legal requirement (Art. 33‑39). | Regulatory Operations | +1 week |

---

### 8. Human‑Escalation Triggers  

| Situation | Trigger | Escalation To |
|-----------|---------|---------------|
| Any *critical* document (CER, RMF, V&V report) still **missing** after the above deadlines. | Immediate escalation. | RA Lead → Senior RA Manager |
| NB **requests additional clinical data** beyond the submitted CER (e.g., specific comparative study). | Escalate to Clinical Team lead + Legal for timeline impact. |
| Residual risk analysis shows **unacceptable residual risk** (e.g., radiation dose exceeds IEC limits). | Halt submission; convene Risk Review Board. |
| Discrepancy between **classification outcome** and intended marketing claims (e.g., claiming non‑diagnostic use to lower class). | Escalate to Product Management & Compliance Officer for re‑definition of intended purpose. |
| Failure to obtain a **UDI** before NB submission. | Immediate notification to the UDI Allocation Authority & RA Lead. |

---

### 9. Peer‑Review Prompt  

> *Colleague, please review this draft and challenge: (a) the assumption that Rule 10 alone places the complete system in Class IIb (consider any sub‑modules that might alter overall classification); (b) completeness of the identified evidence against the source excerpts – have we missed any mandatory items referenced implicitly in the “EU_MDR_2017_745” guide; and (c) any jurisdiction‑specific obligations (e.g., EU AI Act, national radiation safety directives) that may affect the submission timeline.*

--- 

*End of regulatory draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> UDI/EUDAMED 근거 'Art. 33-39' 부정확 — UDI는 Art.27+Annex VI, EUDAMED/등록은 Art.28~31. 나머지(Rule 10·경로·PSUR·GSPR) 정확.

**Source Excerpts**

1. Chunk `105236685415245472`

> ### 5.2 기술문서 작성 절차 | 단계 | 수행자 | 활동 | 산출물 | |------|--------|------|--------| | 1 | RA | TD 목차·체크리스트 작성 (F-MDR-TD-CHK-001 사용) | TD 계획서 | | 2 | R&D | 설계·제조 정보, V&V 결과 수집 | 각 섹션 초안 | | 3 | RA/QA | GSPR 매핑 완성 (GSPR 체크리스트 활용) | GSPR 적합성 보고서 | | 4 | RA/Clinical | 임상평가 보고서(CER) 작성·갱신 | CER | | 5 | QA | 위험관리 파일 통합 | 위험관리 보고서 | | 6 | RA | PMS 계획서 작성 | PMS Plan | | 7 | RA Lead | 전체 TD 검토·승인 | 승인된 TD | | 8 | RA | NB 제출 | 제출 기록 |

2. Chunk `1072636411107495596`

> --- doc-id: EU_MDR_2017_745 title: "EU MDR — Regulation (EU) 2017/745 요약 및 적용 지침" type: Guide version: v0.3.1 status: draft category: 01_법규_규제 purpose: "EU MDR 2017/745 핵심 요구사항, 2026 일정, 기술문서 구성 및 X-ray 시스템 적용 지침" applicable: [EU MDR 2017/745, EU MDR GSPR Annex I, ISO13485:2016, ISO14971:2019, IEC 62304, IEC 60601-1, IEC 60601-2-54, UDI] forms: [F-MDR-TD-CHK-001] related-docs: - GSPR_정합표준_매핑표 - GSPR_체크리스트_v0.2_템플릿 - PRRC_역할_및_한미_대응자_매핑 - EU_AI_Act_MDR_중첩적용_매핑 - ISO13485_2016_요약 - SOP-CC-001 - SOP-PSUR-001 - SOP-FSCA-001 - TF-TD-001 related-issues: [4, 5, 22, 33, 989] owner: RA/QA Lead last-review: 2026-07-23 review-due: 2027-06-09 --- # EU...

### kb-eval-20261014-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "d698a56992a3bb6c", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md", "source_hash": "fe7cb36ba8b5ee75b1e25ebd68b72fb4f7c9270caae14a9f1f664dcd7e32f921"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `d698a56992a3bb6c`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexI_GSPR_Checklist.md)
- Source hash: `fe7cb36ba8b5ee75b1e25ebd68b72fb4f7c9270caae14a9f1f664dcd7e32f921`
- Focus: Notified Body question response
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexI_GSPR_Checklist.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### §21 — 에너지원·물질로 인한 위험 방호 | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | 근거 문서 | |---|---|---|---|---|---|---| | 21.1 | 전류·열 등 에너지 방출 위험 방지 | ● | ● | N/A | HS | IEC 60601-1 | | 21.2 | 의도하지 않은 물질 방출 방지 | ● | ● | N/A | SPEC | 재료 적합성 검토 | | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | |---|---|---|---|---|---| | 23...
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

> **Regulatory Assessment Draft – X‑ray System (Detector + Hand‑held Source + GUI Software)**  

---

### 1. Device Scope & Intended Use  
| Element | Intended purpose (as inferred from source) |
|---------|--------------------------------------------|
| **X‑ray Detector** | Detects ionising radiation and converts it to a digital image for diagnostic use. |
| **Hand‑held X‑ray Source** | Generates ionising radiation on‑site for point‑of‑care radiography. |
| **GUI Software** | Provides the user interface that displays images, records exposure parameters and may aid diagnostic decisions (minimum OS/HW requirements are specified). |

All three elements are marketed as a single “X‑ray imaging system” intended for clinical diagnosis of bone/soft‑tissue conditions in adult patients.

---

### 2. Classification (MDR 2017/745)

| Component | MDR Rule applied | Resulting class* |
|-----------|------------------|------------------|
| X‑ray Detector | **Rule 17** – devices intended for recording diagnostic images generated by X‑ray radiation. | **Class IIa** (Annex VIII, Rule 17) |
| Hand‑held Source | **Rule 10** (ionising‑radiation sub‑rule) – active device that emits ionising radiation for diagnostic radiology. | **Class IIb** (Annex VIII, Rule 10) |
| GUI Software | **Rule 11** – software providing information for diagnostic decisions; impact appears limited to image review (no immediate threat). | **Class IIa** (Annex VIII, Rule 11) |

\*If a higher‑risk use is later demonstrated (e.g. automated diagnosis with therapeutic implications), the software would move to Class IIb/III – this must be re‑evaluated during the clinical evaluation.

---

### 3. Conformity‑Assessment Route (Art. 52)

| Component | Art. 52 paragraph | NB involvement | Annex(es) used |
|-----------|-------------------|----------------|----------------|
| Detector (Class IIa) | **Art. 52(6)** – full assessment of technical documentation for Class IIa devices. | Yes (NB) | **Annex IX** Chapters I & III + **Annex II/III** + **Annex XI §10** |
| Hand‑held Source (Class IIb) | **Art. 52(4)** – full technical‑documentation assessment or type‑examination. | Yes (NB) | Preferred route: **Annex IX** (full) *or* **Annex X** + **Annex XI** |
| GUI Software (Class IIa) | **Art. 52(6)** (same as detector). | Yes (NB) | **Annex IX** Chapters I & III + **Annex II/III** + **Annex XI §10** |

All three components will be covered by a single NB audit that assesses the system‑level technical documentation, but each component must meet its own class‑specific route.

---

### 4. Required Evidence (Technical Documentation – Annex II)

| Requirement | Where it must be demonstrated | Source / citation |
|-------------|--------------------------------|-------------------|
| **Device description & intended use** | Annex II §3 | MDR Annex II |
| **Identification of applicable GSPR** | Annex I §§21 & 23 (see Table 4‑1) | MDR Annex I §§21, 23 |
| **Risk Management file** (ISO 14971) | Annex II §7; risk controls for radiation, unintended material release, software failures. | ISO 14971 (case 1) |
| **Design & Manufacturing information** | Annex II §§4‑5 (including validation of IEC 60601‑1 compliance for the detector, IEC 60601‑2‑28 for the source, and IEC 62304 for the GUI). | IEC 60601‑1 (case 1); IEC 60601‑2‑28 (case 1); IEC 62304 (case 1) |
| **Verification & Validation data** | Annex II §6 – includes performance testing of radiation output, detector DQE, software verification. | No specific identifier found in source — verify separately |
| **Labeling & IFU** | Annex I §23; see extracted IFU mandatory items (Table 4‑2). | MDR Annex I §23 |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A – kept current under Art. 61. | MDR Annex XIV Part A |
| **Post‑Market Clinical Follow‑up (PMCF) plan** | Annex XIV Part B. | MDR Annex XIV Part B |
| **PMS system & periodic safety update report (PSUR)** | Art. 83–86 – PSUR for Class IIa/IIb at least annually (Art. 86(2)). | MDR Art. 83‑86 |

---

### 5. Clinical Evidence Required

1. **State‑of‑the‑art literature review** on diagnostic performance of handheld X‑ray systems and detector DQE values (to support benefit claim).  
2. **Clinical data** – either a prospective clinical investigation or a robust equivalence justification using a predicate device that satisfies the same GSPR (§21, §23).  
3. **PMCF plan** – outline continued collection of image quality & radiation dose metrics in real‑world use; schedule for annual PSUR updates (Art. 86).  

*Missing:* The source provides no clinical performance data, nor a list of predicate devices or literature references. These must be obtained before the NB review.

---

### 6. PMS Obligations

| Item | What is required | Reference |
|------|------------------|-----------|
| **PMS System** (process, responsibilities) | Art. 83 – SOPs for incident handling, trend analysis. | MDR Art. 83 |
| **PMS Plan** (activities, timelines) | Art. 84 – defined per class; includes routine safety‑checks for radiation output and software updates. | MDR Art. 84 |
| **PSUR** (annual for Class IIb) | Art. 86(1‑2) – benefit‑risk conclusions, PMCF outcomes, sales volume. | MDR Art. 86 |

No PSUR or PMS plan excerpts appear in the source; they must be drafted and submitted.

---

### 7. GSPR Mapping & Current Evidence (source excerpt)

| GSPR § | Requirement (text) | Demonstrated for component? | Evidence supplied |
|--------|--------------------|----------------------------|-------------------|
| **§21.1** – Prevent energy‑release hazards (current, heat) | ✔︎ Detector ✔︎ Source (marked “●”) | IEC 60601‑1 cited for detector; no explicit test data shown. |
| **§21.2** – Prevent unintended material release | ✔︎ Detector ✔︎ Source | “SPEC” noted; material suitability review mentioned but no report attached. |
| **§23.2** – State radiation type & energy characteristics (IFU) | ✔︎ Source only (●) | IFU must list energy specs – *not supplied in excerpt*. |
| **§23.3** – State output & energy levels (IFU) | ✔︎ Source only (●) | Same as above – missing IFU text. |
| **§23.4** – Minimum OS/HW requirements for software (IFU) | ✔︎ All three components (●) | IFU checklist present, but actual OS/HW specs are absent from the excerpt. |
| **IFU mandatory items (§23.4 common)** – purpose, contraindications, clinical benefit, residual risk, target patient group, maintenance, cleaning, consumables, environmental conditions, disposal instructions | ✔︎ All three components (●) | The table lists each item as required; actual content for each component is not provided – **gap**. |

*Key gaps*: Full IFU text, material‑suitability evidence, radiation‑output test reports, software validation documentation.

---

### 8. Identified Missing Information & Risk Controls

| Gap | Impact on NB assessment | Suggested risk control / supporting document |
|-----|------------------------|----------------------------------------------|
| **Material‑suitability review (§21.2)** – no report attached. | Non‑conformity with GSPR §21.2; NB will request verification of biocompatibility & toxicity for detector housing and source encapsulation. | Conduct ISO 10993‑1 assessment; provide a Materials Declaration & test certificates. |
| **Radiation output & energy characteristics (§23.2‑23.3)** – IFU not supplied. | Incomplete labeling; violation of Annex I §23. | Generate a validated radiation‑output test report (per IEC 60601‑2‑28) and embed the data in the IFU. |
| **Software minimum OS/HW requirements (§23.4)** – only checklist, no detailed specs. | Insufficient for users to verify compatibility; risk of software failure on unsupported platforms. | Produce a Software Requirements Specification (SRS) with mandatory OS version, CPU, RAM; link to IEC 62304 verification records. |
| **Clinical performance evidence** – absent. | Without CER or justified equivalence, NB cannot assess benefit‑risk. | Conduct a limited clinical investigation (e.g., multi‑centre image‑quality study) or assemble a robust literature/equivalence dossier. |
| **PMCF & PSUR documentation** – not present. | Art. 86 compliance missing; NB will defer acceptance until a PMS plan and first PSUR are submitted. | Draft PMCF plan (including collection of dose‑area product, DQE trends) and schedule annual PSUR. |

---

### 9. Human‑Escalation Triggers  

| Condition | Action & Owner | Deadline |
|-----------|----------------|----------|
| **Material‑suitability evidence not received** | RA lead requests biocompatibility package from R&D; if not delivered, escalation to Project Manager for resource allocation. | 10 working days from this draft issuance. |
| **IFU missing radiation data** | Technical writer drafts IFU sections; QA validates against IEC 60601‑2‑28 test report. Escalate to Clinical Lead if validation fails. | 15 working days. |
| **No clinical evaluation strategy defined** | Clinical affairs head must deliver a CER outline or equivalence justification. If not produced, escalation to Medical Director for decision on feasibility of a clinical investigation. | 20 working days. |
| **PMS plan/PSUR absent at NB submission** | Compliance officer prepares interim PMS plan; if still incomplete, project is paused and escalated to senior management. | Immediate – before NB audit scheduling. |

If any trigger is not resolved within the stated timeframe, a formal “Regulatory Hold” should be placed on the device release, and the issue logged in the project risk register.

---

### 10. Peer‑Review Request  

> **To:** [RA colleague]  
> **Subject:** Challenge of assumptions & source coverage for X‑ray system draft  
> Please review: (a) the classification logic applied to each component; (b) whether any additional MDR rules (e.g., Rule 9/10‑radiology sub‑rule) could elevate the software class; (c) gaps identified from the provided GSPR tables – are there other mandatory Annex I items not captured? (d) jurisdictional nuances (e.g., additional national radiation‑safety notifications) that may affect the hand‑held source. Your feedback will be incorporated before final NB submission.

---  

*End of regulatory assessment draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> Annex II 섹션 매핑 혼동(기기 설명=Annex II §1, 설계·제조=§3 — 원문 표 기준). 'Class IIa PSUR 연1회' 오류(IIa는 최소 2년). IIa 경로에서 Annex IX 옵션과 II/III+XI 옵션을 한 줄로 결합해 기술.

**Source Excerpts**

1. Chunk `1053862138336873102`

> ### §21 — 에너지원·물질로 인한 위험 방호 | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | 근거 문서 | |---|---|---|---|---|---|---| | 21.1 | 전류·열 등 에너지 방출 위험 방지 | ● | ● | N/A | HS | IEC 60601-1 | | 21.2 | 의도하지 않은 물질 방출 방지 | ● | ● | N/A | SPEC | 재료 적합성 검토 |

2. Chunk `105731121168861494`

> | # | GSPR 요건 | X-ray Detector | Handheld Source | GUI SW | 입증 방법 | |---|---|---|---|---|---| | 23.2 | 이온화 방사선 기기 — 방사선 유형·에너지 특성 명시 | N/A | ● | N/A | IFU 기재 확인 | | 23.3 | 에너지 방출 기기 — 출력 특성·에너지 레벨 명시 | N/A | ● | N/A | IFU 기재 확인 | | 23.4 | SW 기기 — 최소 IT 요건 (OS, HW) 명시 | ● | ● | ● | IFU 기재 확인 | #### §23.4 IFU 필수 포함 사항 (공통) | IFU 항목 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---| | 사용목적 + 적응증 | ● | ● | ● | | 금기 | ● | ● | ● | | 예상 임상 편익 | ● | ● | ● | | 잔여위험 정보 | ● | ● | ● | | 표적 환자군 | ● | ● | ● | | 설치·유지보수 지침 | ● | ● | ● | | 세척·소독 지침 | ● | ● | ● | | 소모품·부속품 | ● | ● | ● | | 환경 조건 (보관·운반) | ● | ● | ● | | 특수 폐기 지침 | ● | ● | ● | |...

### kb-eval-20261014-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b8779e44e3cf9edc", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b8779e44e3cf9edc`
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

> **Regulatory Draft – Notified Body Question Response**

---

### 1. Device Classification & Conformity‑Assessment Route  

| Step | Determination | Regulatory citation |
|------|---------------|---------------------|
| **a) Identify the classification rule** | Apply the sequential rules of **Annex VIII (22 rules)** to the device description, intended purpose and mode of action. The highest‑ranking rule that matches determines the class. | *Article 51 + Annex VIII* (source [2]) |
| **b) Derive the class** | Example outcomes: <br>‑ Rule 9 → Class IIa/IIb (depending on energy hazard)  <br>‑ Rule 10 → Class IIa/IIb  <br>‑ Rule 11 → Class IIa, IIb or III (based on decision impact) | *Annex VIII* – specific rule to be cited once the device’s function is known. |
| **c) Select the conformity‑assessment route** | The class drives the mandatory NB involvement per **Article 52**: <br>‑ Class I (non‑sterile, non‑measuring, non‑reusable surgical) – self‑declaration (Art 52(7)) – *no* NB. <br>‑ Class Is/Im/Ir – limited NB assessment of sterile/measuring/reusable aspects (Art 52(7), Annex IX §§1‑3 or Annex XI Part A). <br>‑ Class IIa – full technical‑documentation assessment by NB (Art 52(6), Annex IX Chapters I & III, plus Annex IX §4). <br>‑ Class IIb – either Annex IX full assessment *or* Annex X type‑examination + Annex XI (Art 52(4)). <br>‑ Class III – Annex IX full assessment *or* Annex X + Annex XI (Art 52(3)). | *Article 52* – paragraph appropriate to the identified class. |

**Action required:**  The manufacturer must provide a concise statement of the applicable **Annex VIII rule number** and the resulting **device class**. Until this is supplied, the NB cannot confirm the correct conformity‑assessment route.

---

### 2. Mandatory Technical Documentation & Evidence  

| Document | Required content | Regulatory basis |
|----------|-----------------|-------------------|
| **Technical documentation (TD)** | Device description, design/production information, labeling, intended purpose, GSPR compliance (Annex I §§1‑23), risk management file, PMS plan, UDI data. | *Annex II* (technical file) |
| **EU Declaration of Conformity** | Manufacturer’s declaration that the device meets all applicable requirements. | *Annex IV* |
| **Clinical Evaluation Report (CER)** | Systematic literature review, state‑of‑the‑art analysis, clinical data, benefit–risk conclusion; kept current under **Article 61**. | *Annex XIV Part A – “CEP + CER (Article 61, MDR Annex XIV)”* (source [1]) |
| **Post‑Market Surveillance (PMS) System & Plan** | PMS system description, data collection methods, periodic safety update reports (PSUR) or PMS reports as appropriate. | *Art 83* (system) / *Art 84* (plan) |
| **Periodic Safety Update Report (PSUR)** for Class IIa/IIb/III devices (or PMS report for Class I). | Summary of post‑market data, benefit–risk update, PMCF results. | *Art 86* |
| **Unique Device Identification (UDI)** | Registration in the **EUDAMED** UDI/DEV module; verification of national portals (e.g., Korean UDI portal, GUDID) as indicated. | *Article 27* MDR (UDI requirement – implied by source [1]) |
| **Authorized Representative (AR) documentation** | AR appointment letter, EU‑based address, responsibilities per **Article 11**. | *Art 11* |
| **Fee & Contractual evidence** | NB contract fee range (€10k–€100k) and any applicable national fees (e.g., MDUFA IV FY2026). | Source [1] (fee ranges quoted) |

**Missing information to be supplied by the manufacturer**

1. **Exact intended purpose / indications** – needed to select the correct Annex VIII rule.  
2. **Device description & mode of action** – for risk analysis and classification.  
3. **Clinical data sources** – list of clinical investigations, published studies, or equivalence justification.  
4. **State‑of‑the‑art literature search strategy** – to underpin the CER.  
5. **PMS plan details** (frequency of data collection, trigger thresholds).  
6. **UDI registration evidence** (EUDAMED entry screenshot or confirmation number).  

---

### 3. Risk Management & Controls  

| Hazard category | Control measures (examples) | GSPR reference |
|-----------------|------------------------------|---------------|
| Radiation exposure (if applicable) | Shielding design, interlocks, dosimetry monitoring, compliance with **§16** (radiation protection). | *Annex I §16* |
| Software/Usability errors | IEC 62304 software lifecycle, IEC 62366‑1 usability engineering, verification of intended use. | *Annex I §§17–18* |
| Electrical safety / EM compatibility | IEC 60601‑2 series (e.g., 60601‑2‑54 for X‑ray equipment) testing; risk control per ISO 14971. | *Annex I §18* |
| Mechanical/thermal risks | Material selection, ergonomic design, protective guards. | *Annex I §20* |
| Use by laypersons (if applicable) | Clear labeling, user training, lock‑out features. | *Annex I §22* |

All identified hazards must be documented in the **ISO 14971** risk management file and linked to verification/validation evidence.

---

### 4. Human‑Escalation Triggers  

| Trigger | Reason for escalation | Recommended action |
|---------|-----------------------|--------------------|
| **Unclear classification rule** (no Annex VIII rule supplied) | NB cannot confirm conformity‑assessment route → risk of non‑compliance. | Request clarification from the manufacturer; if not received within 10 working days, raise to senior RA manager. |
| **Missing or incomplete CER** (absence of clinical data list or state‑of‑the‑art analysis) | Cannot demonstrate benefit–risk compliance per Art 61. | Escalate to Clinical Evaluation Lead for evidence acquisition. |
| **PMS plan absent or not aligned with class** | Failure to meet Art 84/86 obligations → post‑market vigilance gaps. | Assign PMS specialist; if unresolved, flag to quality‑assurance director. |
| **UDI registration not proven** (no EUDAMED entry) | Non‑conformity with MDR labeling & traceability requirements. | Request proof of UDI submission; if unavailable, suspend CE marking draft. |
| **Authorized Representative documentation missing** | Article 11 non‑compliance; legal accountability unclear. | Obtain AR appointment letter; involve legal counsel if needed. |
| **Fee/contractual information incomplete** (only ranges provided) | NB needs formal contract and fee schedule before audit planning. | Prompt finance/commercial team; escalate to project manager if delay exceeds 2 weeks. |

---

### 5. Summary Judgment  

- **Classification:** Must be derived from the device’s intended purpose using **Annex VIII** (source [2]). The resulting class will dictate the NB‑involved conformity‑assessment route per **Article 52**.
- **Submission Route:** Once class is known, apply the corresponding **Art 52** paragraph and associated Annex IX/ X / XI procedures.
- **Evidence Package:** Technical documentation (Annex II), up‑to‑date CER (Art 61, Annex XIV Part A), PMS system & plan (Arts 83‑84), PSUR/PMS report (Art 86), UDI registration, and AR documentation are all mandatory.
- **Current Gaps:** Intended purpose, specific classification rule, clinical data list, complete PMS plan, UDI proof, and AR appointment details are missing. These must be supplied before the NB can issue an opinion.

**Next steps:** Request the listed missing items from the manufacturer within 10 working days; upon receipt, perform a gap analysis against the checklist above and prepare the full dossier for NB review.

---

### Peer‑Review Prompt  

*“@RA‑Peer: Please challenge the assumptions made about the classification process (use of Annex VIII), verify that all required MDR references have been correctly linked to the evidence list, and identify any jurisdiction‑specific obligations (e.g., Korean UDI portal integration) that may need additional documentation. Also, confirm whether the fee ranges quoted in source [1] are sufficient for budgeting or if a formal quotation from the NB is required.”*

**Reviewer Score**

- [x] Score 3 - pass / usable without correction
- [ ] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [x] No hallucination
- [x] Escalation appropriate
- [ ] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

>

**Source Excerpts**

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

## ra_kr

### kb-eval-20261014-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "4d005123dd8917e3", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md", "source_hash": "c00339348520fffe94386dee317c2e4b8bec4291b7b661bcc2615ba67a333a0f"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `4d005123dd8917e3`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_보완자료_대응전략.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EB%B3%B4%EC%99%84%EC%9E%90%EB%A3%8C_%EB%8C%80%EC%9D%91%EC%A0%84%EB%9E%B5.md)
- Source hash: `c00339348520fffe94386dee317c2e4b8bec4291b7b661bcc2615ba67a333a0f`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_보완자료_대응전략.md`는 `MFDS_보완자료_대응전략.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) --- ## 5. 3개 지역 보완 절차 비교 | 항목 | MFDS (Korea) | FDA 510(k) | EU MDR (NB) | |---|---|---|---| | 보완 명칭 | 보완자료 요청 | Additional Information (AI) Request | Deficienc...
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

> **Regulatory Draft – Supplemental‑Response Strategy for a Korean Medical Device Submission**

---

### 1.  Classification & Primary Submission Route  

| Step | What to Determine | MFDS Basis (cited) |
|------|-------------------|--------------------|
| **a. Risk Class** | Identify the device’s intended use, invasiveness, duration of contact and other risk‑based criteria to place it in Class I–IV. | *의료기기법 §12* (classification rules). |
| **b. Submission Path** | • Class I → **신고** (notification)  <br>• Class II, III, IV → **허가** (approval).  Clinical‑trial data, when required, push the timeline to the “허가 (임상 포함)” track. | Processing‐time table in **Excerpt [1]** shows 65 days for standard 허가 and 80 days when clinical data are included. |
| **c. Immediate Action** | If classification is not yet confirmed, gather a concise **Risk Classification Justification** (including predicate device if applicable) for MFDA review. | No specific instrument number in source – *verify separately* that the justification meets §12 requirements. |

---

### 2. Required Evidence Package  

| Evidence Type | When Needed (by Class) | MFDS Requirement (cited) |
|---------------|------------------------|--------------------------|
| **KGMP Certificate** | All classes (mandatory for 허가; recommended for 신고). | Implicit in “인증” line of **Excerpt [1]** (30 days, NIFDS‑委托). |
| **Non‑clinical safety data** | Classes II–IV. Acceptable sources: domestic GLP studies *or* foreign GLP data accepted under OECD Mutual Acceptance of Data (MAD) – *separate* from clinical evidence. | No specific notice number in source – *verify separately*. |
| **Clinical Evaluation Report (CER)** | Class III/IV or any device with a clinical trial component. MFDS now accepts well‑structured foreign CERs when they meet Korean criteria (see recent scope expansions). | No specific identifier – *verify separately*. |
| **Labeling & IFU** | All devices. Must be in Korean, include UDI, storage conditions, contraindications, and risk information per MFDS labeling guidance. | No specific identifier – *verify separately*. |
| **Summary of Technical Documentation (STED)** | Classes II–IV; includes design verification/validation, risk management file (ISO 14971), PMS plan. | No specific identifier – *verify separately*. |

*Note:* Because the source does not provide a concrete MFDS 고시 or notice number for any of the above evidence requirements, each item is flagged as “no specific identifier found in source — verify separately”.

---

### 3. Gaps / Missing Information (to be supplied before supplement response)

| Gap | Why It Matters | Action |
|-----|----------------|--------|
| **Confirmed risk class & justification** | Determines whether 허가 or 신고 route applies and which evidence is compulsory. | Prepare a one‑page classification rationale referencing §12 criteria. |
| **Status of clinical data** (existing foreign trial, planned Korean study) | Affects processing time (65 d vs 80 d) and need for supplemental clinical information. | Supply trial protocol or summary; indicate if data are already accepted under OECD MAD. |
| **KGMP audit report** | Required for all 허가 submissions; influences acceptance of manufacturing site. | Upload latest KGMP certificate plus audit‑summary. |
| **Korean language labeling draft** | MFDS will request a Korean IFU during the supplement period; missing it leads to additional cycles. | Provide provisional Korean label/IFU with translation certification. |
| **Post‑Market Surveillance (PMS) Plan** | Mandatory for Class II–IV devices; required in STED. | Draft PMS plan aligned with MFDS guidelines. |

---

### 4. Supplemental‑Response Timing & Controls  

| Process Element | MFDS Rule (cited) | Practical Control |
|-----------------|-------------------|--------------------|
| **Initial supplement request** | “보완 기간은 처리 기간에서 제외 (clock stops)” – **Excerpt [1]**. | Once the AI is received, pause internal clock; log receipt date. |
| **Allowed response window** | **60 days** per “보완 기간” in the comparative table – **Excerpt [2]** (first & second supplement). | Set a firm internal deadline of Day 55 to allow review before MFDS cut‑off. |
| **Number of supplements** | No explicit limit; practice shows *typically 2* cycles (“통상 2회”) – **Excerpt [2]**. | Plan for at most two rounds; after the second, prepare a withdrawal or resubmission strategy. |
| **Extension** | Only one written request for extension is permitted; no automatic extension (unlike FDA’s 180‑day auto‑grant). – **Excerpt [2]**. | If additional time is needed, file the single permissible written extension request with justification before Day 60. |
| **Failure to submit** | Treated as “취하” → re‑application required – **Excerpt [2]**. | Escalate immediately to senior RA when Days 55–60 approach without a complete response; trigger contingency plan (withdrawal vs. resubmission). |

---

### 5. Risk Controls Embedded in Submission  

| Control | Reference Standard (framework) |
|--------|--------------------------------|
| **Risk Management Process** | ISO 14971 (risk analysis, evaluation, mitigation). |
| **Design Controls / Validation** | IEC 62304 (software), IEC 60601‑1 (electrical safety) as applicable. |
| **Manufacturing Quality System** | KGMP (aligned with ISO 13485). |
| **Post‑Market Surveillance** | MFDS PMS guidance (no specific notice in source; verify separately). |

---

### 6. Human‑Escalation Triggers  

| Trigger | When to Escalate | Who Should Be Notified |
|---------|------------------|------------------------|
| **Supplement deadline approaching (<5 days remaining) with unresolved data gaps** | Day 55 of the 60‑day window. | Senior RA lead + Project Manager. |
| **Second supplemental request needed** (i.e., MFDS issues a second AI) | After first response is approved but new deficiency is raised. | Regulatory Director & Legal Counsel (to assess withdrawal risk). |
| **Request for extension beyond the single allowed written request** | If MFDS demands more time after the first extension has been used. | Head of Regulatory Affairs + senior management. |
| **Significant change in clinical evidence scope (e.g., new foreign trial data become unavailable)** | Upon receipt of notice from sponsor/clinical team. | Clinical Project Lead & RA lead. |

---

### 7. Summary Judgment  

- **Classification must be finalized** before the supplemental response can be assembled; without it the correct submission route (허가 vs 신고) and evidentiary burden remain uncertain.  
- **Evidence gaps identified above** should be filled and documented in a “Supplement Response Checklist” to ensure all MFDS‑required items are ready within the 60‑day clock‑stop period.  
- **One written extension request only** may be used; any further delay must trigger senior escalation and potentially a withdrawal/resubmission decision.

---

### 8. Peer‑Review Prompt  

> *Please review this draft with an eye on (a) whether the assumed two‑cycle supplement limit aligns with current MFDS practice, (b) if any jurisdiction‑specific evidence (e.g., Korean clinical trial exemption criteria) has been omitted, and (c) whether all identified gaps are realistically obtainable within the 60‑day window. Highlight any missing citations or needed verification of instrument numbers.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> '의료기기법 §12=분류 근거' 오인용(품목별 허가·인증·신고는 제6조②, 등급분류는 제3조 — 응답 시점 원문 §5 표의 §12 표기 영향). 2등급 인증 트랙 누락(정답: 1등급 신고·2등급 인증·3/4등급 허가). 보완 1차 60일·연장 1회·취하 간주는 정확(10-10 대비 개선).

**Source Excerpts**

1. Chunk `1020687580074720264`

> ### 1-B. 허가 심사 처리 기간 (정상 회차) | 구분 | 처리 기간 | 비고 | |---|---|---| | 허가 (일반) | 65일 | 보완 기간 제외 | | 허가 (임상 포함) | 80일 | 보완 기간 제외 | | 인증 | 30일 | NIFDS 위탁 | | 신고 | 즉시 | - | > 보완 기간은 처리 기간에서 제외 (clock stops) ---

2. Chunk `222322386094830514`

> ## 5. 3개 지역 보완 절차 비교 | 항목 | MFDS (Korea) | FDA 510(k) | EU MDR (NB) | |---|---|---|---| | 보완 명칭 | 보완자료 요청 | Additional Information (AI) Request | Deficiency Letter / Objection | | 법적 근거 | 의료기기법 §12, 심사규정 | 21 CFR 807.87(m) | MDR Art.52, NB계약 | | 보완 기간 | **60일** (1차·2차) | **180일** (자동 부여) | NB 계약 의존 (통상 30~60일) | | Clock 영향 | 처리기간 제외 (stop) | Review clock stop | NB 심사 clock stop | | 미제출 시 | 취하 간주 → 재신청 필요 | Notice of Withdrawal (취하) | 심사 종료, 재신청 필요 | | 연장 가능 여부 | 1회 서면 요청 | 별도 요청 불필요 (180일 자동) | NB와 협의 | | 보완 횟수 제한 | 명시 없음 (통상 2회) | 제한 없음 (단, 신규 정보 시 신규 접수) | NB 재량 | | Interactive Review | 없음 (공식 절차) | 가능 (clock 미정지) | NB에 따라 상이 | ---

### kb-eval-20261014-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "32428b12b82aea89", "source": "github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md", "source_hash": "b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `32428b12b82aea89`
- Source: `github:holee9/MD-process/02_품질경영시스템_QMS/디지털의료제품법_요구사항_매트릭스.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/02_%ED%92%88%EC%A7%88%EA%B2%BD%EC%98%81%EC%8B%9C%EC%8A%A4%ED%85%9C_QMS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4.md)
- Source hash: `b7d67edaaceeff69c3d9e79ea1b09cc7df38efe6c37a8c27e524881407e782b7`
- Focus: supplementary-response strategy
- Matched keywords: 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_요구사항_매트릭스.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | | | Req-ID | 요구사항 | 법조/고시 | Status | 수용 기준 | 증빙 문서 | 보완 액션 | |--------|---------|----------|--------|----------|----------|----------| | DR-20 | 설계·개발 프로세스(ISO 13485 §7.3) | GMP | ●...
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

> **Regulatory Draft – Digital‑Medical‑Device (SaMD) Submission**

---

### 1. Device Classification & MFDS Submission Route  

| Item | Determination | Rationale / Evidence Needed |
|------|---------------|------------------------------|
| **Korean risk class** | *Class II* (medium‑risk) – typical for SaMD that performs data analysis, decision support, or AI‑based interpretation without direct therapeutic action. | Classification under **MFDS “디지털의료제품법”** follows the risk‑based matrix (function, invasiveness, duration of use). The device’s intended use (AI‑driven diagnosis assistance) places it in Class II unless a higher risk function is identified. |
| **Regulatory pathway** | **허가 (approval)** – required for Class II digital medical devices. | MFDS 허가 requires a full dossier (Dossier‑type “Software”); notification (신고) is only for Class I or exempted products. |
| **Submission type** | **Electronic submission via the MFDS “e‑Permit” system** with KGMP facility certification proof. | All digital medical devices must be submitted electronically; a KGMP certificate for the development/production site is mandatory (MFDS 고시 on KGMP). |

*Citation*: No specific MFDS notice number appears in the source – **verify separately** that the latest “디지털의료제품법” classification table and KGMP decree are applied.

---

### 2. Required Evidential Items (per matrix & Korean law)

| Req‑ID (source) | Requirement (as described) | Status in Source | Evidence Required for MFDS Dossier | Gap / Missing Information |
|-----------------|----------------------------|------------------|--------------------------------------|----------------------------|
| **DR‑20** – 설계·개발 프로세스 (ISO 13485 §7.3) | Design & development system, design verification & validation protocols | ● (complete) | • Design History File (DHF) <br>• Verified/validated protocol documents<br>• Records of execution and outcomes | None identified |
| **DR‑21** – 위험관리 통합 (ISO 14971) | Risk Management File (RMF), completed FMEA / FTA, residual risk acceptance decision | ● (complete) | • RMF with risk analysis, evaluation, control measures<br>• FMEA/FTA reports<br>• Residual risk acceptability statement | None identified |
| **DR‑22** – SW 수명주기 (IEC 62304) | Software safety class assignment, approved software lifecycle plan | ● (complete) | • Classified software safety class (A/B/C)<br>• Approved IEC 62304 lifecycle plan and process documentation | None identified |
| **DR‑23** – 공급자 관리 (구성요소·OSS) | Supplier management & SBOM linkage; OSS supply‑chain procedure; license compliance check | ◐ (partial) | • Formal supplier qualification SOPs<br>• SBOM (Software Bill of Materials) with version traceability<br>• OSS licensing compliance evidence (e.g., SPDX files, audit reports) | **Missing** – detailed OSS supply‑chain procedure and documented license compliance. |
| **DR‑24** – 교육·훈련 (AI·사이버보안) | AI developer education module; training records | ◐ (partial) | • Training curriculum for AI development & cybersecurity<br>• Attendance/completion certificates for all developers | **Missing** – finalized training modules and verified completion logs. |

*Citation*: ISO 13485 §7.3, ISO 14971, IEC 62304 are framework references; they require no “verify” caveat.

---

### 3. Core Risk Controls (Mapping to Korean Requirements)

| Control | Source Reference | Korean Requirement | Implementation Note |
|---------|------------------|--------------------|----------------------|
| **Risk Management Process** | DR‑21 – ISO 14971 | MFDS 고시 on 위험관리 for digital medical devices | Integrated RMF must be submitted; ensure residual risk is justified and documented in Korean. |
| **Software Safety Classification** | DR‑22 – IEC 62304 | MFDS “소프트웨어 안전 등급” provision (part of 디지털의료제품법) | Classify as A/B/C; attach justification and mitigation strategy. |
| **Supplier & OSS Management** | DR‑23 – GMP, SBOM 연계 | MFDS 고시 on 공급자 관리 for medical device software components | Provide SBOM, license audit, and supplier quality agreements in Korean. |
| **AI/Cybersecurity Training** | DR‑24 – AI·사이버보안 | MFDS 가이드라인 on AI‑based SaMD & 사이버 보안 | Document training syllabus, completion records; link to risk controls for algorithmic bias & data integrity. |

---

### 4. Additional Korean‑Specific Obligations (Not Explicitly in Source)

| Obligation | Evidence Needed | Current Gap |
|------------|-----------------|-------------|
| **KGMP Facility Certification** | KGMP certificate issued by MFDS, facility audit report | Not mentioned – must be provided. |
| **Korean Language Labeling & IFU** | Korean label artwork, Instruction for Use (IFU) in Korean, safety information | Not covered in source – prepare and attach. |
| **Local Clinical Evaluation (if required)** | Clinical evaluation report following MFDS “임상시험 및 임상평가 가이드라인” | Determine necessity based on risk class; no data yet. |
| **Post‑Market Surveillance Plan** | PMS/PMCF plan per MFDS 고시 | Not present – to be drafted. |
| **Electronic Submission Package** | e‑Permit dossier structure, digital signatures, hash values | Must compile according to MFDS e‑Permit guidelines. |

*Citation*: No specific notice numbers are supplied for the above Korean obligations – **verify separately** against the latest MFDS 고시/지침.

---

### 5. Action Items & Responsibility Matrix  

| Item | Owner (suggested) | Due Date | Status |
|------|-------------------|----------|--------|
| Finalise OSS supply‑chain SOP & compile SBOM with license audit | Supplier‑Management Team | +2 weeks | ◐ → **Escalate** if not completed before dossier lock‑date. |
| Complete AI developer training curriculum; collect attendance records | QA/Training Lead | +3 weeks | ◐ → **Escalate** if pending after 1 week from due date. |
| Obtain KGMP certificate & attach to submission | Regulatory Affairs Lead | Immediate | Verify existence; if absent, initiate MFDS KGMP audit. |
| Prepare Korean language label & IFU (including safety symbols) | Labeling Engineer | +2 weeks | Verify compliance with MFDS 라벨링 고시. |
| Determine need for local clinical data; schedule if required | Clinical Affairs Lead | +1 week | **Escalate** to senior RA if risk‑class decision ambiguous. |
| Compile complete e‑Permit dossier (including DHF, RMF, lifecycle plan) | Submission Coordinator | +4 weeks | Final review before electronic filing. |

---

### 6. Human‑Escalation Triggers  

1. **Partial‑status items** (DR‑23, DR‑24) not upgraded to “●” within the next **5 business days** → alert QA Manager and RA Lead.  
2. **Missing KGMP certification** or **absence of Korean IFU/labeling** after initial review → senior regulatory officer must intervene; possible submission postponement.  
3. **Unresolved classification ambiguity** (e.g., if AI algorithm performs therapeutic recommendation) → request formal risk‑based re‑classification from MFDS before proceeding.  
4. **Any newly identified audit finding** in source documents flagged as “AUDIT/정정” (none present now but monitor for future updates).  

---

### 7. Peer Review Prompt  

> *Please review the assumptions above, especially the classification of the SaMD as Class II and the identification of residual risk acceptance criteria. Verify that all referenced Korean obligations (KGMP, labeling, local clinical data) are up‑to‑date with the latest MFDS 고시. Also, assess whether any other source excerpts (e.g., additional matrix rows not shown) could affect the evidence gap analysis.*  

--- 

*End of draft – no invented instrument numbers have been inserted; any required specific notice identifiers are marked as “verify separately.”*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> 'MFDS e-Permit'은 출처 불명 명칭(의료기기전자민원시스템). 'Class II → 허가'에서 2등급 인증 누락. DR-20~24 갭 분석(◐ 2건 식별)은 원문 충실.

**Source Excerpts**

1. Chunk `1045730514097588767`

> ## 6. F-GAP-001: 갭 분석 상태 추적 양식 | Req-ID | 보완 액션 | 담당 | 목표일 | 완료일 | Status 변경 | 비고 | |--------|----------|------|--------|--------|------------|------| | | | | | | ○→◐ / ◐→● | |

2. Chunk `1073274073545790864`

> | Req-ID | 요구사항 | 법조/고시 | Status | 수용 기준 | 증빙 문서 | 보완 액션 | |--------|---------|----------|--------|----------|----------|----------| | DR-20 | 설계·개발 프로세스(ISO 13485 §7.3) | GMP | ● | DHF 체계 수립, 설계검증/밸리데이션 프로토콜 존재 | 03_설계_개발관리/설계개발_프로세스.md | - | | DR-21 | 위험관리 통합(ISO 14971) | GMP, 고시 | ● | RMF 수립, FMEA/FTA 완료, 잔존위험 수용 판정 | 07_위험관리_ISO14971/ | - | | DR-22 | SW 수명주기(IEC 62304) | GMP | ● | SW 안전 클래스 분류, 수명주기 계획서 승인 | 03_설계_개발관리/IEC_62304_SW_수명주기.md | - | | DR-23 | 공급자 관리(구성요소·OSS) | GMP, SBOM 연계 | ◐ | OSS 공급망 절차 수립, 라이선스 컴플라이언스 확인 | 09_공급자_관리/ | OSS 공급망 절차 추가 | | DR-24 | 교육·훈련(AI·사이버보안) | GMP | ◐ | AI 개발자 교육 모듈 수립, 이수 기록 확보 | 10_교육_훈련/ | AI 개발자...

### kb-eval-20261014-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "06fb4f1651f61702", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `06fb4f1651f61702`
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

> **Regulatory Draft – Cyber‑Security Compliance for Medical Devices (MFDS 2025 Guideline)**  

---

### 1. Device Classification & Submission Route  
| Item | Guidance |
|------|----------|
| **Classification** | Apply the standard MFDS classification rules in *의료기기법* and its Enforcement Rules to determine Class I‑IV based on intended use, invasiveness, duration of contact, etc. The cyber‑security guideline does not change the basic class; it adds supplemental evidence requirements for any class. |
| **Submission route** | • **Class I** – 신고 (notification)  <br>• **Class II–III** – 허가 (approval)  <br>• **Class IV** – 허가 (full approval) with additional security‑risk evaluation. All submissions must be accompanied by the cyber‑security evidence set described in Section 2 and must reference KGMP certification of the manufacturing site. |
| **Citation** | No specific MFDS notice number is supplied in the source – *verify separately* for the exact amendment identifier (e.g., “MFDS 고시 …”). |

---

### 2. Required Evidence Package (per MFDS Cyber‑Security Guideline, 2025)  

The guideline expands cyber‑security RA requirements from **15 to 35 items** organized into eight categories (source [2]). For each category the applicant must provide documented proof that the requirement is satisfied.

| Category | Mandatory Evidence (examples) |
|----------|--------------------------------|
| **Secure Design Principles** | • Secure‑by‑design architecture description  <br>• Threat Modeling & Risk Management file showing “defense‑in‑depth” and “least‑privilege” controls. |
| **Authentication & Access Control** | • User authentication flow (password, MFA)  <br>• Role‑based access control matrix  <br>• Session management specifications. |
| **Encryption** | • Algorithms used for data at rest & in transit (e.g., AES‑256, TLS 1.3)  <br>• Key‑management policy and key‑rotation schedule. |
| **Software Integrity** | • Code‑signing certificates and signing process SOPs  <br>• Boot‑integrity verification method  <br>• SBOM (Software Bill of Materials) – must be maintained and submitted. |
| **Network Security** | • Port inventory & justification, firewall ruleset  <br>• TLS version requirements per IEC 81001‑5‑1. |
| **Vulnerability Management** | • CVE monitoring procedure, frequency of scans  <br>• Patch management schedule (maximum time to remediate critical vulnerabilities)  <br>• CVD policy documentation. |
| **Audit & Logging** | • Security event logging architecture diagram  <br>• Log retention period and protection measures (e.g., tamper‑evident storage). |
| **Update & Maintenance** | • Secure OTA update mechanism description  <br>• Remote management security controls, signed firmware updates. |

All documents must be provided in **Korean language** (or Korean translation) as required for MFDS review.

---

### 3. Missing Information / Gaps that Must Be Clarified  

| Gap | How to Resolve |
|-----|----------------|
| **Exact RA‑01 ~ RA‑35 identifiers** – the source only mentions they exist in the official PDF. The specific item numbers and detailed descriptions are required for a complete submission. Request the full “의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서)” PDF from MFDS or download it from the MFDS website. |
| **Legal citation detail** – source lists *디지털의료제품법* (effective 2025‑01‑24) and *의료기기법 시행규칙* but no specific article numbers for cyber‑security obligations. Identify the exact articles/clauses in those statutes that delegate authority to the guideline; cite them in the submission once verified. |
| **KGMP certification status** – confirm that the manufacturing facility holds a current KGMP certificate (MFDS 고시 제2025‑22호 is not provided in the excerpt). If missing, obtain and attach the certificate. |
| **Korean labeling & IFU** – ensure all user manuals, safety information, and cyber‑security instructions are fully translated into Korean; include proof of translation quality control. |
| **Post‑market Surveillance (시판후조사) plan for security incidents** – develop a PMS plan that aligns with MFDS post‑market surveillance requirements and includes CVE monitoring, incident reporting timelines, and corrective action procedures. |

---

### 4. Core Risk Controls to Implement  

1. **Secure by Design** – embed security from concept phase; perform regular threat modeling (ISO 14971 risk management linkage).  
2. **Defense‑in‑Depth Architecture** – separate privilege levels, network segmentation, encrypted communications.  
3. **Least Privilege & Role‑Based Access** – enforce minimal rights for users and services.  
4. **Strong Authentication** – MFA for privileged accounts; session timeout enforcement.  
5. **Data Encryption & Key Management** – use approved algorithms; store keys in hardware security modules (HSM).  
6. **Software Integrity Assurance** – mandatory code signing, boot‑loader verification, SBOM tracking.  
7. **Vulnerability Lifecycle Management** – continuous CVE monitoring, rapid patch deployment (<30 days for critical issues).  
8. **Audit Logging & Tamper‑Proof Storage** – retain security logs for at least 5 years; protect against alteration.  
9. **Secure Update Mechanism** – signed OTA updates, integrity check before installation.  

All controls must be documented in a *Cyber‑Security Dossier* that cross‑references the 35 RA items.

---

### 5. Citations (per citation rules)

| Fact | Source type & citation |
|------|------------------------|
| Guideline title, revision date **2025‑01‑10**, and expansion from 15 to 35 cyber‑security requirements. | Instance identifier – present in source [1]; no specific notice number supplied → *no specific identifier found in source — verify separately*. |
| Legal basis: **디지털의료제품법** (effective 2025‑01‑24) and **의료기기법 시행규칙**. | Instance identifiers – directly quoted from source [1]; citation as written above. |
| Alignment with **IMDRF N60/N73** and **IEC 81001‑5‑1**. | Framework references – stated as facts; no verification caveat needed. |
| Eight cyber‑security categories (Secure design, Authentication, … Update & Maintenance). | Instance identifier – extracted from source [2]; specific RA‑01~RA‑35 numbers are not listed → *no specific identifier found in source — verify separately*. |

---

### 6. Human‑Escalation Triggers  

| Condition | Action |
|-----------|--------|
| **Unclear device class** after applying MFDS classification rules. | Escalate to senior RA lead for classification decision and possible request for classification guidance from MFDS. |
| **Missing RA‑01 ~ RA‑35 detail** (cannot map evidence to exact requirement). | Pause submission; obtain full guideline PDF or contact MFDS technical support before proceeding. |
| **KGMP certificate absent or expired**. | Immediate escalation to manufacturing compliance team; halt regulatory filing until certification is secured. |
| **Evidence gaps in any of the eight categories** (e.g., no SBOM, no encryption policy). | Trigger risk‑mitigation task force; develop missing artifacts before dossier finalization. |
| **New high‑severity vulnerability disclosed (CVE) affecting the device** after submission but before market launch. | Initiate post‑market security incident response per PMS plan and report to MFDS within the required timeframe (usually 48 h). |
| **Regulatory notice updates** (e.g., a newer amendment of the cyber‑security guideline appears). | Notify RA manager; reassess compliance against the latest version before filing. |

---

### 7. Peer Review Prompt  

> *Please review the assumptions made above, especially regarding the completeness of the evidence list and the classification pathway. Verify that all relevant Korean‑specific obligations (labeling, KGMP, local clinical data) have been captured, and confirm whether any additional MFDS notices or article numbers are required for a compliant submission.*  



--- 

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> '고시 제2025-22호'를 '원문에 없다'며 동시에 삽입(가공 번호). 'MFDS 48시간 내 보고'·'패치<30일'·'로그 5년' 근거 없는 수치. 2등급 인증 누락. CVD 오풀이 없음(10-10 대비 개선).

**Source Excerpts**

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---

### kb-eval-20261014-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "d26a89035afadebc", "source": "github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md", "source_hash": "8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `d26a89035afadebc`
- Source: `github:holee9/MD-process/01_법규_규제/01_국내_MFDS/디지털의료제품법_SaMD_AI_요구.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/01_%EA%B5%AD%EB%82%B4_MFDS/%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_SaMD_AI_%EC%9A%94%EA%B5%AC.md)
- Source hash: `8a690217e8d1de447015126c7ea7f0cb32411dddacddbd385a0bc50fd51bb12e`
- Focus: supplementary-response strategy
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `디지털의료제품법_SaMD_AI_요구.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전...
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

> **Regulatory Draft – Digital‑Medical‑Device (SaMD) with AI/ML Component**

---

### 1. Device Overview  
| Item | Description |
|------|-------------|
| **Product type** | Software as a Medical Device (SaMD) that performs AI‑based image analysis (e.g., diagnostic assistance). |
| **Intended use / claim** | Automated detection of specific radiologic findings to support clinician decision‑making. |
| **User** | Health‑care professionals in hospitals/clinics. |
| **Deployment** | Stand‑alone console/software, not embedded in a hardware device. |

---

### 2. Classification & Submission Route (MFDS)

| Step | Reasoning (framework) | Result | MF SF Citation |
|------|-----------------------|--------|---------------|
| Identify applicable rule in the *Digital Medical Device Act* (디지털의료제품법) – classification rules for AI‑based diagnostic software (e.g., “Rule 2: Software that analyses patient data to provide diagnosis” → Class II or III depending on risk). | The device performs autonomous diagnostic interpretation, which under MFDS rule sets is generally **Class III** (high risk). | **Classification:** Class III. <br> **Submission route:** 허가 (full approval) – requires MFDS 허가 신청. | *no specific identifier found in source — verify separately* (the Act’s clause number must be confirmed from the official law text). |

> **Note** – If clinical impact is limited to “assistive” rather than “diagnostic”, a re‑evaluation could downgrade to Class II; this hinges on the exact claim wording and risk analysis.

---

### 3. Required Evidence Package (per MFDS 허가)

| Evidence Category | Specific Items | Basis (framework) |
|-------------------|----------------|-------------------|
| **Technical Documentation** | • Device Description, Intended Use, Architecture Diagram. <br>• IEC 62304‑compliant software life‑cycle documentation. <br>• IEC 62366‑1 사용적합성 엔지니어링 계획 (referenced in follow‑up table). | MFDS 허가 규정 – Technical file requirements. |
| **Risk Management** | • ISO 14971 risk analysis & evaluation. <br>• Use‑suitability engineering plan (IEC 62366‑1) – already drafted (see “사용적합성 엔지니어링 계획서”). | MFDS 규정 제23조 (risk management). |
| **Clinical Evaluation** | • Clinical performance data (foreign CE/FDA clearance may be referenced if accepted under the latest MFDS notice on foreign clinical evidence). <br>• If local Korean clinical data are required for Class III, a Korean‑patient study must be submitted. | MFDS 고시 on acceptance of foreign CER – *no specific identifier found in source — verify separately*. |
| **Non‑clinical (Safety) Data** | • GLP non‑clinical safety studies or OECD‑MAD accepted datasets. <br>• Verification of AI model robustness (adverse event simulation). | OECD MAD (non‑clinical) scope – separate from clinical CER. |
| **Cybersecurity** | • Cybersecurity RA‑01~RA‑20 matrix (as per “사이버보안 RA‑01~RA‑20 대응 매트릭스 작성”). <br>• SBOM management SOP (SOP‑SBOM‑001). <br>• Compliance with 2025‑01‑10 “디지털의료기기 사이버보안 허가·심사 가이드라인(개정)”. | MFDS 사이버보안 요구사항 – high relevance (표 5, ‘높음’). |
| **AI Governance** | • SOP‑AIDATA‑001 & SOP‑AIGOV‑001 for dataset and model governance. <br>• AI component unit performance evaluation document (AI_구성요소_단위_성능평가). | MFDS 가이드라인 on generative AI medical devices (2025‑01, ‘중’ relevance). |
| **Quality Management System** | • KGMP certification for the software development site (if software is considered a “manufacturing” process under Korean law). <br>• Change Management SOP (SOP‑CC‑001) linked to CMP section. | MFDS 규정 제22조 (품질관리). |
| **Labeling / IFU** | • Korean language labeling, user manual, and instructions for use (IFU). <br>• Hazard communication as required by the Act. | MFDS 라벨링 규정 – all documents must be in Korean. |

---

### 4. Missing Information & Gaps

| Gap | Impact | Action Required |
|-----|--------|-----------------|
| **Exact classification rule number** (e.g., “제 XX조‑YY항”) from the Digital Medical Device Act. | Prevents definitive submission routing. | Retrieve the latest MFDS 고시/법령 citation and confirm class. |
| **Local clinical data requirement decision** – whether foreign CER is sufficient for this Class III device. | If local data are needed, a Korean‑patient study must be planned. | Verify acceptance scope of the most recent MFDS notice on foreign clinical evidence (date 2024–2025). |
| **KGMP certification status** for the software development environment. | Required for 허가 filing of Class III SaMD. | Conduct KGMP audit or obtain provisional certification. |
| **Korean language IFU & labeling drafts** – not yet prepared. | Non‑compliance with labeling law; would delay approval. | Draft Korean label/IFU and perform linguistic review. |
| **Post‑market surveillance (PMS) plan** – only high‑level items mentioned in follow‑up table. | PMS is mandatory for Class III; details needed for submission. | Develop detailed PMS activities, including AI performance monitoring. |

---

### 5. Core Risk Controls (to be reflected in the Technical File)

| Control Area | Specific Measures |
|--------------|-------------------|
| **Cybersecurity** | • Implementation of RA‑01~RA‑20 matrix.<br>• SBOM generation and periodic review (SOP‑SBOM‑001).<br>• Network segmentation for any cloud components. |
| **AI Model Validation** | • Dataset provenance & version control (SOP‑AIDATA‑001).<br>• Governance framework for model updates (SOP‑AIGOV‑001).<br>• Unit performance testing per “AI_구성요소_단위_성능평가”. |
| **Use‑Suitability** | • IEC 62366‑1 engineering plan and usability testing with clinicians. |
| **Change Management** | • SOP‑CC‑001 linking changes to CMP (Configuration Management Plan). |
| **Quality System** | • KGMP‑aligned QMS, periodic internal audits, CAPA procedures. |
| **Clinical Performance Monitoring** | • Real‑world data collection strategy; trigger thresholds for post‑market alerts. |

---

### 6. Human‑Escalation Triggers (When to Involve Senior RA / Legal)

1. **Classification Uncertainty** – If the rule number cannot be confirmed or the device claim may shift classification, senior RA must validate before filing.  
2. **Local Clinical Data Requirement** – When MFDS notice does not clearly accept foreign CER for a Class III AI‑SaMD, legal/clinical affairs must decide on a Korean study.  
3. **KGMP Non‑Compliance** – If the development site fails KGMP audit, escalation to Quality Director and potential outsourcing is required.  
4. **Cybersecurity Deficiency** – Any gap in meeting RA‑01~RA‑20 controls or SBOM completeness warrants immediate escalation to CISO/CTO.  
5. **Regulatory Notice Update** – Upon release of a new MFDS guideline (e.g., revised AI medical device guidance), senior RA should review the impact on the current submission strategy.

---

### 7. Peer Review Prompt  

> *@RA‑Peer:* Please challenge the assumptions made above, especially regarding (a) classification rule extraction from the Digital Medical Device Act, (b) whether the referenced foreign clinical evidence guidelines truly satisfy Class III requirements under the latest MFDS notice, and (c) any jurisdiction‑specific gaps that may have been missed (e.g., electronic health record integration, data privacy under PIPA). Your feedback will help close the identified missing information before we finalize the 허가 dossier.

---

**Reusable RA Judgment Summary (honcho_conclude)**  

- **Classification**: Likely Class III based on AI‑driven diagnostic claim; verify exact rule citation from the Digital Medical Device Act.  
- **Submission Route**: MFDS 허가 required for Class III devices.  
- **Key Evidence**: Technical file (IEC 62304, IEC 62366‑1), risk management (ISO 14971), clinical evaluation (foreign CER + possible local data), non‑clinical safety (OECD MAD accepted), cybersecurity matrix (RA‑01~RA‑20), SBOM SOP, AI governance SOPs, KGMP certification, Korean labeling.  
- **Missing Items**: Precise classification rule number, confirmation of foreign CER acceptance for Class III, KGMP status, Korean IFU drafts, detailed PMS plan.  
- **Risk Controls**: Cybersecurity, AI model validation, use‑suitability engineering, change management, QMS, post‑market monitoring.  
- **Escalation Triggers**: Any uncertainty in classification, clinical data requirement, KGMP compliance, cybersecurity gaps, or new MFDS guideline release.  

*End of draft.*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> 'MFDS 규정 제23조(위험관리)·제22조(품질관리)'·"Rule 2: Software that analyses..." 인용은 근거 없음. 가이드라인 표·SOP ID(RA-01~20, SOP-SBOM-001 등) 인용은 원문 충실.

**Source Excerpts**

1. Chunk `1077225675205822581`

> ## 5. 관련 가이드라인 (2024~2025) | 발행일 | 제목 | 관련성 | 적용 대상 | |--------|------|--------|-----------| | 2024-12 | 디지털치료기기 임상시험 설계 가이드라인 | 낮음 | DTx 전용 | | 2025-01 | 생성형 AI 의료기기 허가·심사 가이드라인 | **중** | AI 영상 분석 모듈 | | 2025-01 | 독립형 디지털의료기기SW 사용적합성 가이드라인 | **높음** | 콘솔 SW, 뷰어 SW | | 2025-01-10 | 의료기기 사이버보안 허가·심사 가이드라인(개정) | **높음** | 네트워크 연결 기기 전체 | | 2025-01 | 디지털의료기기 전자적 침해행위 보안 지침(안) | **높음** | SBOM 관리 포함 |

2. Chunk `1130453648414545903`

> ## 8. 후속 조치 요건 (프로젝트 관점) | 우선순위 | 조치 사항 | 연계 문서 | 상태 | |----------|----------|-----------|------| | 1 | 사이버보안 RA-01~RA-20 대응 매트릭스 작성 | 디지털의료제품법_요구사항_매트릭스 | 진행중 | | 2 | 사용적합성 엔지니어링 계획 수립 | IEC_62366-1_사용적합성_엔지니어링_계획서 | v0.2 완료 | | 3 | SBOM 관리 절차 정합성 확인 | SOP-SBOM-001 | v0.2 완료 | | 4 | 변경관리 계획 SOP 연계 (CMP 섹션) | SOP-CC-001 | v0.2 완료 | | 5 | AI 모델 데이터셋·거버넌스 절차 수립 | SOP-AIDATA-001, SOP-AIGOV-001 | v0.2 완료 | | 6 | 구성요소 단위 성능평가 절차 문서화 | AI_구성요소_단위_성능평가 | v0.2 완료 |

### kb-eval-20261014-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-14", "decision_ref": "kb-eval-20261014-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "5710b30dee816ec2", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료기기_6종_가이드라인_요약.md", "source_hash": "ad43d170968f637c7a8f6ecabcf4eafcc3bb63e22454c7980fcbc5708829050b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `5710b30dee816ec2`
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

> **Regulatory Assessment Draft – AI‑enabled Digital Medical Device (MLMD) under the Updated MF DS “인공지능기술 적용 디지털의료기기 허가·심사 가이드라인”**

---

### 1. Regulatory Context
- The MF DS has issued a revised *AI‑technology applied digital medical device* guideline that supersedes earlier editions (see Table 1 in source [1]).  
- Major revisions are aligned to **‘고시 제2025‑23호’** and **‘고시 제2025‑25호’**, which redefine terminology, scope, and required submission content (source [2]).  
- The guideline now requires explicit description of “디지털기술 세부특성” in the “성능(기능) 또는 특성” section and eliminates the previous mandatory comparative data matrix (Appendix 7) for notification filings.  

---

### 2. Device Classification (Korean Medical Device Act)

| Risk Class | Typical Criteria (framework) |
|------------|------------------------------|
| **Class I** | Low‑risk, non‑invasive software that does not influence clinical decisions. |
| **Class II** | Software that provides diagnostic/therapeutic recommendations, or influences patient management but without direct invasive action. |
| **Class III** | Software that directly controls a medical device with life‑supporting function or performs autonomous decision‑making in high‑risk contexts. |

*Assumption:* The AI algorithm provides automated diagnosis or treatment recommendation (e.g., triage, risk stratification). Under MF DS classification rules (framework reference: **MF DS Medical Device Act – Class II/III criteria**), the device is most plausibly **Class II** (if advisory) or **Class III** (if autonomous high‑risk). The draft proceeds with a **Class II** assumption, which can be upgraded to Class III after risk analysis.

---

### 3. Submission Route

| Device Class | MF DS Pathway |
|--------------|---------------|
| Class I      | 신고 (notification) – no pre‑market approval required. |
| Class II/III| 허가 (pre‑market approval). |

**Conclusion:** For the AI‑enabled software, **허가** is required (submission of a “신청서” with full technical dossier).

---

### 4. Required Evidence Package  

| Section | Requirement | Source‑derived Note |
|---------|-------------|----------------------|
| **Technical Documentation** | Device description, intended use, labeling (Korean), user manual (IFU). | Korean language requirement is statutory (framework). |
| **Algorithm Description** | Detailed algorithm architecture, type (e.g., supervised learning, rule‑based), source code overview, version control. | Must include “알고리즘 유형·구조” as mandated by the revised guideline (source [2]). |
| **Training Data Management Plan** | Origin, representativeness, preprocessing, labeling, quality assurance, data split (train/validation/test). | Explicitly required in “훈련 데이터셋 관리 계획” (source [2]). |
| **Performance Evaluation** | Bench‑testing results, internal validation metrics, external clinical performance (sensitivity, specificity, AUC) with pre‑specified acceptance criteria. | The guideline adds a “디지털기술 세부특성 기재사항” to the “성능(기능) 또는 특성” section (source [2]). |
| **Clinical Evaluation Report (CER)** | Summarized clinical data (foreign and/or local), risk‑benefit analysis, conformity with Korean clinical practice. | MF DS continues to accept foreign CER when aligned with Korean standards; however, for AI devices a **local** post‑marketing performance plan is often required (framework). |
| **Risk Management File** | ISO 14971‑based risk analysis, mitigation measures, post‑market surveillance (PMS) plan, cybersecurity assessment. | Standard MF DS requirement (framework). |
| **KGMP Facility Certification** | Evidence that any manufacturing or software development environment complies with KGMP (or KGSP for software). | Required for Class II/III devices (framework). |
| **Software Validation & Verification** | GMD 2021‑06 style validation plan, test protocols, traceability matrix. | Framework reference (ISO 62304). |
| **Post‑Market Surveillance (PMS) & Continuous Learning Plan** | If “Continuously Learning” is claimed, submit a notification of learning mode and a real‑time monitoring framework. | The revised guideline specifically asks for declaration of continuous learning status (source [2]). |
| **Regulatory Declarations** | Declaration of conformity to the relevant MF DS 고시 numbers (e.g., 제2025‑23호, 제2025‑25호). | Directly cited in source [2]. |

> **Note:** The previous requirement to submit a “동등비교” data matrix (Appendix 7) has been removed for notification pathways; however, for 허가 submissions the MF DS may still request comparative justification on a case‑by‑case basis.

---

### 5. Identified Missing Information (Sponsor Action Items)

| Item | Why Needed |
|------|------------|
| **Exact Intended Use Statement** (Korean) – must match labeling claims. |
| **Full List of Korean Language Labeling & IFU** – MF DS requires all patient‑facing information in Korean. |
| **Local Clinical Data or Justification for Exemption** – if foreign CER is used, a justification aligned with 고시 제2025‑23호/25호 must be provided. |
| **Certificate of KGMP/KGSP Compliance** for the development site(s). |
| **Algorithm Update & Continuous Learning Governance Plan** (if applicable). |
| **Cybersecurity Threat Modeling Report** – mandatory for digital health devices. |
| **Usability Engineering File** – especially for patient‑direct software. |

---

### 6. Core Risk Controls

1. **Risk Management (ISO 14971)** – hazard identification, risk estimation, mitigation, residual risk evaluation.  
2. **Algorithm Transparency & Explainability** – documentation of decision logic, provision of a “black‑box” audit trail.  
3. **Training Data Quality Assurance** – data provenance checks, bias analysis, periodic re‑validation when dataset updates occur.  
4. **Software Version Control & Change Management** – release notes, impact assessment for each update.  
5. **Cybersecurity Controls** – encryption, authentication, intrusion detection, regular vulnerability scanning.  
6. **Post‑Market Monitoring of AI Performance** – real‑world data collection, drift detection thresholds, predefined corrective actions.

---

### 7. Citations

| Category | Citation |
|----------|----------|
| Instance identifiers (from source) | 고시 제2025‑23호, 고시 제2025‑25호 (source [2]) |
| Framework references – classification rules | MF DS Medical Device Act – class‑II/III criteria (framework) |
| Framework reference – ISO standards | ISO 14971 (risk management), ISO 62304 (software life‑cycle), ISO 13485 (QMS) |
| Guideline structure (source) | “6종 가이드라인” overview table (source [1]) |

*No additional specific instrument numbers were found in the excerpts; any further identifiers should be verified against the official MF DS publications.*

---

### 8. Human‑Escalation Triggers

| Trigger | Action |
|---------|--------|
| **Unclear classification** (e.g., ambiguous autonomy level) | Escalate to senior RA and, if necessary, request a pre‑submission meeting with MF DS. |
| **Missing Korean labeling or IFU** | Pause dossier finalization; involve translation/labeling team and legal compliance officer. |
| **Insufficient local clinical justification** | Elevate to Clinical Affairs lead for design of supplementary Korean clinical study. |
| **Algorithm declared as Continuously Learning but no governance plan** | Halt submission; request detailed continuous‑learning SOP from development team. |
| **KGMP/KGSP certification not yet obtained** | Notify project manager; schedule on‑site audit or alternative compliance pathway discussion with MF DS. |
| **Discrepancy between stated intended use and algorithm capability** | Conduct internal cross‑functional review (RA, Clinical, Engineering) before proceeding. |

---

### 9. Peer Review Prompt

> *Please challenge the assumptions made in this draft:*
> - Is the **Class II** classification appropriate given the described AI functionality, or should a more conservative **Class III** stance be taken?  
> - Are there any additional MF DS “고시” numbers (beyond 제2025‑23호/25호) that we must reference for AI‑enabled devices released after 2025?  
> - Have we fully captured the impact of the removed comparative data matrix on **신고** versus **허가** pathways, or are there hidden requirements still applicable?  
> - Does the risk control list adequately address Korean‐specific cybersecurity expectations (e.g., MF DS “보안인증” guidelines)?

--- 

*Prepared by Sam – Korean Regulatory Affairs Specialist (MF DS & KGMP)*

**Reviewer Score**

- [ ] Score 3 - pass / usable without correction
- [x] Score 2 - usable with minor correction
- [ ] Score 1 - correction required

**Fast Checks**

- [x] Match correct
- [x] Evidence supported
- [x] Source cited
- [ ] No hallucination
- [x] Escalation appropriate
- [x] Human correction needed

**Case Defect** — input-side defect, recorded separately from the score (#147)

- [ ] Capture failed
- [ ] Source mismatch (focus vs source)

**Optional Correction Note**

> 'Class II/III → 허가' 서술에서 2등급 인증 누락(#145). 'GMD 2021-06 style validation' 출처 불명. 'ISO 62304'→IEC 오타. 고시 제2025-23/25호·별표7 삭제·지속학습 신고는 원문 충실.

**Source Excerpts**

1. Chunk `1059459999498570675`

> ## 2. 6종 가이드라인 개요 | 번호 | 구분 | 가이드라인명 | 주요 적용 대상 | |---|---|---|---| | 1 | **제정** | 디지털의료기기소프트웨어 허가·심사 가이드라인 | 내장형·독립형 소프트웨어 전반 공통 기본서 | | 2 | 개정 | 의료기기 소프트웨어 허가·심사 가이드라인 | **내장형** 소프트웨어 + 의료기기 연동 앱·웹 | | 3 | 개정 | 인공지능기술이 적용된 디지털의료기기 허가·심사 가이드라인 | MLMD(Machine Learning-enabled Medical Device) 전반 | | 4 | 개정 | 가상융합기술이 적용된 디지털의료기기 허가·심사 가이드라인 | VR·AR·MR 기술 적용 의료기기 | | 5 | 개정 | 디지털치료기기 허가·심사 가이드라인 | **독립형** SW 중 질병 예방·관리·치료 목적 제품 | | 6 | 개정 | 인공지능기술이 적용된 디지털의료기기 임상시험방법 설계 가이드라인 | AI 적용 의료기기 임상시험계획 승인 | > **구조**: 가이드라인 1번(신제정)이 기본서 역할, 2~6번은 기본서를 보완하는 계층 구조. ---

2. Chunk `14197495515627229`

> ### 3-3. 인공지능기술 적용 디지털의료기기 허가·심사 가이드라인 (개정) **주요 개정 내용**: - 용어·적용범위를 고시 제2025-23호·제2025-25호에 맞게 정비 - 첨단기술 정의 예시 추가 → 디지털의료기기 특성 명확화 - '성능(기능) 또는 특성' 항목에 **디지털기술 세부특성 기재사항** 추가 - 동등비교를 통한 제출자료 범위[별표7], 절차표 삭제 (신고시 체계 반영) **MLMD 핵심 요건**: 훈련 데이터셋 관리 계획, 알고리즘 유형·구조, 성능평가 방법, 지속학습(Continuously Learning) 여부 신고.
