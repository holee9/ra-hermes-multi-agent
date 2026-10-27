# KB Eval Checksheet - 2026-10-27 Iteration 01

Reviewer workflow:

1. Check exactly one score per case.
2. Mark the fast checks that are true.
3. Add a correction note only when score is 1 or the issue is not obvious from the boxes.
4. Commit the checked Markdown. Ingest runs separately and defaults to dry-run.

Total cases: 15

## ra_us

### kb-eval-20261027-it01-ra_us-001

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_us-001", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "83a42162e010ad46", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md", "source_hash": "1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `83a42162e010ad46`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/README.md)
- Source hash: `1a3ae2d7b7033bdbe8b27463ab710e5ce46c5752e3fab8f92a3045d3be751c11`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `README.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용 ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Info...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Predicate Strategy**

---

### 1. Device Synopsis (to be completed by the project team)  
- **Intended Use:** *[Insert concise statement of clinical indication]*  
- **Device Class & CFR Part:** Likely **Class II** medical imaging device regulated under **21 CFR §892**. The exact sub‑section depends on function: e.g., a PACS‑type processing/analysis software would fall under **§892.2050 (Medical image management and processing system)**; an image storage unit under **§892.2010**, etc. *Confirm the appropriate subsection once the intended use is finalised.*  

---

### 2. Submission Route  
- **Premarket Notification (510(k))** – the standard pathway for Class II devices with a suitable predicate.  
- If no reasonable predicate exists, consider **De Novo classification** (21 CFR §812) as an alternative route.

---

### 3. Predicate Device Strategy (per source excerpt [2])  

| Step | Action | Comment |
|------|--------|---------|
| 1 | Search FDA 510(k) database for devices of the same **intended use** and **technological characteristics**. | Must document search terms, date of search, and results. |
| 2 | Build a **Substantial Equivalence (SE) comparison table** that maps each predicate’s specifications to the new device. | Include performance, materials, software algorithms, labeling, etc. |
| 3 | Prepare **510(k) Summary**, **Performance Test Reports**, **Biocompatibility**, **EMC** data as listed in source excerpt [2]. | Use eSTAR templates for electronic submission. |
| 4 | Submit via **eSTAR portal**; be ready to address FDA’s Additional Information (AI) requests (21 CFR §807.92). | AI response window is 180 calendar days per guidance. |

*Source excerpt [2] provides the overall flow but does not supply a specific identifier – “no specific identifier found in source — verify separately.”*

---

### 4. Required Evidence Package  

| Category | Typical Content | Regulatory Basis |
|----------|-----------------|------------------|
| **Device Description & Indications for Use** | Narrative, labeling draft, IFU (see eSTAR_01_Device_Description_IFU guide) | 21 CFR §807.87; FDA Guidance “Content of Premarket Submissions” |
| **Substantial Equivalence Table** | Side‑by‑side comparison with predicate(s) | 21 CFR §807.92(d)(3) |
| **Performance Testing** | Bench, animal, or clinical data demonstrating that the device meets its intended use and matches predicate performance | 21 CFR §§892.2050 (if applicable); FDA Guidance “Medical Device Clinical Performance Testing” |
| **Biocompatibility** | ISO 14971‑based risk analysis; ISO 10993‑1 (2018) testing report | 21 CFR §820.80; ISO 14971 (2019) |
| **Electrical Safety & Electromagnetic Compatibility** | IEC 60601‑1 (2005+A1:2012+A2:2020); IEC 61000‑4‑6/3 for EMC | 21 CFR §§892.2010–892.2050 (device‑specific) |
| **Software Validation** *(if applicable)* | IEC 62304 (2006+A1:2015) lifecycle documentation; Predetermined Change Control Plan (PCCP) if AI‑driven features are present | 21 CFR §820.30; FDA Guidance “Predetermined Change Control Plans for AI/ML” (Dec 2024) |
| **Labeling** | Full label set, UDI placement per 21 CFR §§830.10–830.60 | 21 CFR §801, §830 |
| **Quality System Documentation** | ISO 13485:2016‑aligned QMSR (effective Feb 2026) – design controls, corrective actions, CAPA | 21 CFR Part 820 (QMSR) |

*All references above are framework citations; no instance identifiers appear in the source excerpts.*

---

### 5. Identified Information Gaps  

| Gap | Impact on submission | Recommended action |
|-----|----------------------|--------------------|
| **Exact device classification subsection** – needed to cite correct §892.* | Determines required performance tests & labeling content. | Conduct a functional breakdown with engineering; map to CFR §892 list. |
| **Predicate device details (K numbers, 510(k) numbers)** – not yet identified. | SE table cannot be completed; FDA may issue an RTA. | Perform structured database search; record predicate identifiers. |
| **Biocompatibility testing plan** – only generic reference present. | If missing, FDA may request additional data under AI. | Align material list with ISO 14971 hazard analysis; schedule testing per ISO 10993‑1. |
| **Software change‑control strategy** – PCCP not drafted if AI/ML features exist. | Absence could delay review of future updates. | Draft a PCCP outlining permissible algorithm modifications; submit as part of the 510(k) (or later under FDA guidance). |
| **UDI issuance plan** – no GUDID submission evidence yet. | Non‑compliance with Part 830 may trigger enforceable action. | Prepare UDI carrier, label content, and GUDID file per §830.300–330. |

*All gaps are derived from the process outline in source excerpt [2] and the generic device description guide in excerpt [1]; no specific IDs were provided.*

---

### 6. Risk Management Controls (per ISO 14971:2019 & FDA QMSR)  

| Control | Application |
|---------|-------------|
| **Hazard identification & risk analysis** | Perform a full FMEA linked to intended use; output documented in the design dossier. |
| **Design controls (21 CFR §820.30)** | Include design inputs/outputs, verification, validation, and design transfer. |
| **Usability engineering (IEC 62366‑1:2020)** | Conduct formative/usability testing to mitigate user error. |
| **Software lifecycle management** – IEC 62304 & PCCP | Establish version control, change impact analysis, and post‑market monitoring plan. |
| **Post‑Market Surveillance (21 CFR §822)** | Set up a Medical Device Reporting (MDR) system; monitor adverse events under Part 803. |

---

### 7. Regulatory Citations  

| Area | Citation (framework) |
|------|----------------------|
| Classification – Imaging devices | **21 CFR Part 892** (e.g., §892.2050 for image management software) |
| Premarket Notification | **21 CFR Part 807** |
| Quality System Regulation (effective 2026‑02) | **21 CFR Part 820** |
| Unique Device Identification | **21 CFR Part 830**, §§830.10–830.60 |
| Biocompatibility standard | **ISO 10993‑1:2018** |
| Risk management standard | ** ISO 14971:2019** |
| Software lifecycle | **IEC 62304:2006+A1:2015** |
| Electromagnetic compatibility | **IEC 60601‑1:2005+A1:2012+A2:2020** |
| Usability engineering | **IEC 62366‑1:2015+A1:2020** |
| Predetermined Change Control Plan guidance | FDA Final Guidance, Dec 2024 (PCCP) |

*All citations are framework references; no instance identifiers were extracted from the source material.*

---

### 8. Human‑Escalation Triggers  

| Trigger | Reason for escalation to senior RA / regulatory leadership |
|--------|------------------------------------------------------------|
| **Unresolved classification** – inability to map device to a specific §892 subsection after analysis. | Could affect the entire submission strategy (510(k) vs De Novo). |
| **No viable predicate found** after exhaustive FDA database search. | May require a De Novo request or additional clinical data, extending timelines. |
| **Missing biocompatibility or EMC test reports** at the time of eSTAR package assembly. | FDA may issue an AI that stalls review; risk to schedule. |
| **PCCP not drafted for AI/ML components** when the device includes adaptive algorithms. | Future software changes could be non‑compliant, leading to enforcement action. |
| **UDI/GUDID submission incomplete** prior to 510(k) filing. | Non‑conformance with Part 830 may prompt a form 483 or FDA warning. |
| **RTA (Refuse‑to‑Accept) issued by FDA review team** during electronic submission. | Immediate corrective action needed; senior oversight required. |

When any trigger occurs, the responsible RA must log the issue in the project risk register and notify the regulatory manager within one business day.

---

### 9. Reusable Regulatory Judgment (to be recorded in the knowledge base)

> *For a Class II imaging device, the default pathway is a 510(k) submission supported by a well‑documented predicate search, SE comparison table, and a complete performance/biocompatibility evidence package aligned to the applicable §892 subsection. Missing classification or predicate data automatically escalates to senior regulatory oversight; absence of required risk management artifacts (ISO 14971 analysis, design controls per 21 CFR 820) similarly triggers escalation.*

---

### 10. Peer‑Review Prompt  

> **To an RA colleague:** Please review the assumptions above—particularly the inferred classification under §892, the completeness of the predicate search strategy, and the identified evidence gaps. Confirm whether any jurisdiction‑specific considerations (e.g., recent QMSR updates or AI/ML guidance) have been omitted, and suggest additional sources or internal data that should be incorporated before finalizing the 510(k) package.

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

1. Chunk `906877802391288013`

> ## eSTAR 섹션별 작성 가이드 (자동보강 시리즈) - [eSTAR_01_Device_Description_IFU](eSTAR_01_Device_Description_IFU.md) — Device Description / Indications for Use 작성 가이드 + 자사 3개 제품 적용

2. Chunk `534746203396750433`

> ## 제출 절차 개요 1. Predicate Device 조사 (FDA 510(k) Database) 2. Substantial Equivalence 비교표 작성 3. 510(k) Summary, 성능시험, 생체적합성, 전자파 등 섹션 준비 4. eSTAR 템플릿을 통한 전자 제출 5. FDA 심사 질의(AI: Additional Information) 대응

### kb-eval-20261027-it01-ra_us-002

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_us-002", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "2310538c00e9aa67", "source": "github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md", "source_hash": "fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `2310538c00e9aa67`
- Source: `github:holee9/ra-project/05_전문가교육/Week03_FDA_510k_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week03_FDA_510k_%EC%83%81%EC%84%B8.md)
- Source hash: `fb38dba1c457918e230b2e38430da06a9aba19617c6deec5127fb384d53d31ab`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `Week03_FDA_510k_상세.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – X‑ray Imaging Device (Daily Growth Case)**  

---

### 1. Bottom‑line regulatory path  
| Predicate outcome | Submission route |
|-------------------|------------------|
| **Legally marketed predicate exists, same intended use and technological characteristics, performance ≥ predicate** → **Traditional 510(k) clearance** | ✔︎ Use the SE‑5 decision flow (DP 2–DP 5). |
| Any “No” at DP 1, DP 2, DP 4 or insufficient performance data → **Not Substantially Equivalent (NSE)** | ❌ Pursue a De Novo classification request (or PMA if high risk). |

> **Current assessment** – The source only supplies the SE‑5 decision framework; no predicate has been identified yet. Until a qualified predicate and comparative data are assembled, the device must be treated as NSE → **De Novo** is the fallback route.

---

### 2. Device classification (US)  
*Imaging equipment that emits ionizing radiation.*  

- Likely **Class II** under **21 CFR Part 892** (radiology/imaging).  
- The exact subsection (e.g., §892.2010‑§892.2050) for an X‑ray system is not stated in the source – **verify separately**.

---

### 3. Predicate‑strategy using SE‑5 steps (source [2])  

| Decision Point | Question & Requirement | Action if “Yes” | Action if “No” |
|----------------|------------------------|-----------------|---------------|
| **DP1** – Is the predicate a legally marketed device? | Must be cleared or approved in the U.S. market. | Proceed to DP2. | Device is NSE → De Novo/PMA. |
| **DP2** – Same intended use? | Intended use must match exactly (e.g., “diagnostic X‑ray imaging of the chest”). | Proceed to DP3. | NSE → De Novo/PMA. |
| **DP3** – Same technological characteristics? | Comparable x‑ray tube voltage, detector type, shielding, etc. | Skip DP4 and go to DP5. | Go to DP4. |
| **DP4** – Do the differences raise new safety/effectiveness questions? | Any novel feature (e.g., AI‑based dose optimization) must be justified. | If “No”, proceed to DP5; if “Yes”, NSE → De Novo/PMA. |
| **DP5** – Performance data show ≥ predicate performance? | Bench, animal, and/or clinical data demonstrating at least equivalent image quality & radiation safety. | **Traditional 510(k) (SE)** possible. | NSE → De Novo/PMA. |

*Action*: Identify at least one cleared X‑ray device that satisfies DP1–DP5; compile a side‑by‑side comparison matrix.

---

### 4. Required evidentiary package for a **Traditional 510(k)**  

| Section (eSTAR) | Evidence needed |
|-----------------|-----------------|
| **Device Description** | Detailed technical specifications, block diagram, labeling copy. |
| **Intended Use & Indications** | Precise statement matching predicate; include clinical setting. |
| **Technological Comparison** | Table showing identical or non‑critical differences (DP 3–4). |
| **Performance Testing** | • Imaging performance (spatial resolution, contrast, dose metrics) <br>• Radiation safety (shielding, leakage, beam quality) <br>• Compatibility testing with existing accessories. |
| **Software/Algorithm Validation** *(if applicable)* | IEC 62304‑compliant software lifecycle documentation; AI/ML change plan per FDA “Predetermined Change Control Plan (PCCP)” guidance (Dec 2024). |
| **Risk Management** | ISO 14971:2019 risk analysis, risk control measures, residual risk evaluation. |
| **Electrical Safety & EMC** | IEC 60601‑1 compliance test reports. |
| **Biocompatibility** *(if patient‑contacting materials)* | ISO 10993‑1:2018 testing results. |
| **Sterilization / Reprocessing** *(if reusable)* | Validation data per applicable standards. |
| **Labeling & UDI** | Draft label meeting 21 CFR Part 801 and Part 830 (UDI format). |
| **Quality System** | Evidence of ISO 13485:2016‑based QMS; recent 510(k) audit summary. |

---

### 5. Missing information from the source  

| Item | Why needed | Current status |
|------|------------|----------------|
| Exact **intended use statement** for the X‑ray product | Determines DP2 & labeling requirements. | Not provided. |
| List of **candidate predicate devices** (cleared numbers, K‑numbers) | Drives DP1–DP5 comparison. | Absent. |
| Detailed **technological characteristics** (tube voltage range, detector type, dose‑modulation features) | Needed for DP3/DP4 analysis. | Missing. |
| **Performance data** (bench / clinical) that demonstrate ≥ predicate performance | Required for DP5. | Not supplied. |
| Confirmation of the **CFR subsection** governing this X‑ray system | Determines classification & applicable special controls. | Needs verification. |
| Evidence of compliance with **QMSR (21 CFR Part 820)** post‑Feb 2026 changes | Mandatory for all submissions. | No mention. |

---

### 6. Risk control measures (ISO 14971:2019)  

1. **Radiation exposure** – Shielding design, dose monitoring, ALARA compliance.  
2. **Electrical safety** – IEC 60601‑1 built‑in protective earth, leakage current limits.  
3. **Software reliability** – IEC 62304 lifecycle, PCCP for AI updates.  
4. **Mechanical hazards** – Secure mounting, tip‑over protection.  
5. **User error mitigation** – Human factors testing, clear UI labeling, training materials.

---

### 7. Key citations  

| Category | Citation |
|----------|----------|
| **Regulatory framework** | *21 CFR Part 892* – imaging devices (classification rule). |
| **SE‑5 decision flow** | FDA 2014 Guidance, Appendix A (source [2]). |
| **Quality Management System Regulation** | *21 CFR Part 820* (QMSR effective Feb 2026). |
| **UDI requirements** | *21 CFR Part 830* (labeling §830.10 onward). |
| **Risk management standard** | ISO 14971:2019. |
| **Software change control guidance** | FDA “Predetermined Change Control Plan (PCCP)” final guidance, Dec 2024. |
| **Performance & safety standards** | IEC 60601‑1:2005+A1:2012+A2:2020; IEC 62304:2006+A1:2015; ISO 10993‑1:2018. |
| **No specific predicate identifier found in source – verify separately** | (predicate device numbers, K‑numbers). |

---

### 8. Human‑escalation triggers  

| Trigger | Action required |
|---------|-----------------|
| **Uncertainty on predicate legality or market status (DP1)** | Pause submission; senior RA to perform a clearance database search and confirm predicate. |
| **Intended use mismatch (DP2) or new safety questions (DP4)** | Escalate to project lead for redesign or consider De Novo pathway. |
| **Insufficient performance data (DP5 “No”)** | Initiate additional bench/clinical testing; senior engineering sign‑off required before proceeding. |
| **Missing classification subsection** | Flag to regulatory counsel; obtain FDA staff clarification or reference the latest product code list. |
| **QMSR non‑compliance (Part 820) after Feb 2026** | Immediate corrective action plan; involve Quality Assurance Manager. |
| **UDI labeling gaps** | Halt final label submission; coordinate with UDI issuance team. |

When any of these triggers occur, the RA should log a “Regulatory hold” in the project tracker and notify the device development lead for resolution before further work.

---

### 9. Peer‑review request  

*@RA‑Peer*: Please review the predicate‑selection assumptions, completeness of the evidence checklist relative to the eSTAR sections, and any jurisdiction‑specific gaps (e.g., special controls for X‑ray systems). Highlight missing CFR subsections or additional FDA guidance that should be referenced.

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

1. Chunk `1061195424067242245`

> ## 11. 평가 기준 | 평가 항목 | 배점 | 기준 | |-----------|------|------| | 510(k) 유형 3가지 구분 | 20점 | Traditional/Abbreviated/Special 조건·차이 정확 설명 | | SE 5단계 적용 | 30점 | 가상 제품 시나리오에서 NSE/SE 판정 근거 도출 | | eSTAR 핵심 섹션 식별 | 20점 | 자사 X-ray 제품에 필요한 섹션 완성 나열 | | 3지역 비교 | 15점 | FDA/MFDS/MDR 핵심 차이 3가지 이상 기술 | | 21 CFR 1020 요건 | 15점 | 적용 조항 및 핵심 수치 요건 정확 기술 | **합격 기준**: 70점 이상 / 과제 3-2 SE 비교표 제출 필수 ---

2. Chunk `1072507187378217632`

> ### 4.1 SE 5단계 Decision Point (FDA 2014 Guidance Appendix A) ``` DP1. Predicate이 Legally Marketed Device인가? │ No → NSE (De Novo 또는 PMA) │ Yes ↓ DP2. 동일한 Intended Use인가? │ No → NSE │ Yes ↓ DP3. 동일한 Technological Characteristics인가? │ Yes → DP5 │ No ↓ DP4. 다른 기술특성이 Different Questions of Safety & Effectiveness를 제기하는가? │ Yes → NSE │ No ↓ DP5. 성능 데이터가 새 장치 ≥ Predicate 수준임을 입증하는가? │ Yes → SE (Clearance 가능) │ No → NSE ```

### kb-eval-20261027-it01-ra_us-003

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_us-003", "iteration": 1, "matched_keywords": ["FDA", "510k", "PMA"], "profile_id": "ra-us", "scenario_id": "720c9b30aa77e9c1", "source": "github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md", "source_hash": "3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `720c9b30aa77e9c1`
- Source: `github:holee9/ra-project/01_규제지식베이스/미국_FDA/510k_PMA_가이던스/eSTAR_02_Substantial_Equivalence.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EB%AF%B8%EA%B5%AD_FDA/510k_PMA_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/eSTAR_02_Substantial_Equivalence.md)
- Source hash: `3dc6451c8fb0c0779986ca1f774751abaa624ea3f680b2839e30bf8238ce7f69`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k, PMA

**Source Summary**

- 문서 요약: `eSTAR_02_Substantial_Equivalence.md`는 FDA 510(k) substantial equivalence와 predicate 비교 항목을 정리한 eSTAR 작성 문서입니다.
- 현재 excerpt 핵심: ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medi...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **510(k) Strategy for Imaging Workstation Software (GUI SW)**  

---

### 1. Device Classification & Submission Route  
| Item | Determination |
|------|---------------|
| **Device function** | Imaging workstation software that performs image acquisition, processing, display, storage, transfer, work‑list management and quality‑assurance tools; may include AI/ML modules. |
| **Regulatory class** | Class II – “Medical image management and processing system” (21 CFR §892.2050). |
| **Submission type** | Traditional 510(k) Premarket Notification demonstrating substantial equivalence to a legally marketed predicate. |

*Reference:* 21 CFR §892.2050 (class II imaging‑software device).  

---

### 2. Predicate Selection – Checklist (derived from source [1])  

| Check | Action Required | Status / Note |
|-------|-----------------|---------------|
| **FDA 510(k) database search by product code** | Identify a predicate with the same product code. | Pending – need product‑code query. |
| **Predicate clearance date** | Prefer predicates cleared ≤ 5 yr ago; if > 7 yr, prepare “modernization” justification. | Pending – confirm dates. |
| **Market status of predicate** | Verify that the predicate is still commercially sold (not retired/discontinued). | Pending – market check. |
| **Recall/Safety‑communication history** | Search MAUDE & Recall DB for any recall or safety notice involving the predicate. | Pending – safety review. |
| **Indications for Use (IFU) comparison** | Perform line‑by‑line text comparison; ensure the new IFU is identical or more limited. | Pending – obtain both IFUs. |
| **Technological differences** | List all functional/technical deviations; provide justification data (bench, animal, clinical). | Pending – difference matrix needed. |
| **Split predicate prohibition** | Use a single primary predicate for IFU equivalence before considering any secondary reference. | Pending – confirm no split‑predicate strategy is planned. |

*Citation:* No specific identifier found in source — verify separately.

---

### 3. Required Submission Evidence  

| Category | Specific Items (US requirements) |
|----------|-----------------------------------|
| **Device Description & Intended Use** | Full narrative, labeling, and IFU text; clear statement that the software is for use on a medical imaging workstation. |
| **Predicate Comparison** | Predicate 510(k) number, product code, clearance date, market status, recall history; side‑by‑side IFU comparison table; justification of any functional differences. |
| **Software Documentation (FDA 2023 SW Guidance)** | • Level of documentation: *Basic* or *Enhanced* (determine based on software complexity and risk). <br>• Software Development Lifecycle artifacts per IEC 62304 (Safety Class A/B/C). <br>• Architecture diagram, source‑code control policy, unit‑test reports. |
| **Risk Management** | ISO 14971:2019 risk analysis file (hazard list, severity/likelihood, mitigations, residual risk evaluation). |
| **Software Safety Classification** | IEC 62304 classification (A/B/C) with supporting rationale. |
| **DICOM Conformance Statement** | Declaration of compliance for Storage SCU/SCP, Worklist SCU, MPPS, Print SCU; evidence of test results against DICOM conformance statements. |
| **Cybersecurity Controls** | Description of authentication method, encryption, audit‑logging, secure update mechanism; reference to NIST 800‑53 or FDA cybersecurity guidance. |
| **SBOM (Software Bill of Materials)** | SPDX or CycloneDX format file listing all third‑party components and versions. |
| **AI/ML Modules** *(if present)* | Predetermined Change Control Plan (PCCP) per FDA Dec 2024 guidance; training data set description, performance validation, post‑market monitoring plan. |
| **Interoperability Claims** | Evidence of HL7 FHIR and IHE profile support (e.g., testing reports, certification). |
| **Hardware/OS Requirements** | Minimum hardware specs, supported operating systems, compatibility matrix. |
| **Usability Engineering** | IEC 62366‑1:2020 usability validation report covering user interface risks. |
| **Verification & Validation (V&V)** | Test plans and results for acquisition, processing, display, storage, transfer, QA tools; performance metrics against predicate. |
| **Quality System Documentation** | 21 CFR Part 820 QMS compliance evidence (design history file, CAPA records). |
| **UDI Labeling** *(if device is to be labeled individually)* | UDI assignment per 21 CFR §830.10‑§830.60; submission of GUDID package. |

*Framework citations:*  
- 21 CFR Part 807 (510(k) requirements)  
- 21 CFR Part 820 (QMSR, ISO 13485:2016 aligned)  
- 21 CFR Part 830 (UDI) – general provisions §830.3 and labeling §§830.10‑830.60  
- IEC 62304:2006+A1:2015 (software life‑cycle processes)  
- IEC 62366‑1:2015+A1:2020 (usability engineering)  
- ISO 14971:2019 (risk management)

*Citation from source [2]:* No specific identifier found in source — verify separately.

---

### 4. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Action |
|-----|----------------------|--------|
| **Predicate product code & clearance number** | Cannot complete equivalence analysis. | Conduct FDA database search; select a predicate ≤ 5 yr old if possible. |
| **Predicate market status & recall history** | Risk of using an inactive or unsafe reference. | Verify sales status and review MAUDE/Recall DB. |
| **Exact Intended Use wording** | Needed for IFU comparison. | Draft precise intended‑use statement; align with predicate. |
| **Technological differences matrix** | Must justify any new features (e.g., AI module). | Prepare table of differences + supporting data. |
| **Software documentation level (Basic vs Enhanced)** | Determines extent of V&V evidence required. | Assess software risk class and select appropriate documentation level per FDA 2023 guidance. |
| **AI/ML PCCP** *(if AI present)* | Required pre‑market change‑control plan. | Develop PCCP covering algorithm updates, monitoring, and re‑validation. |
| **SBOM format & completeness** | Needed for cybersecurity review. | Generate SPDX or CycloneDX SBOM of all components. |
| **DICOM conformance test reports** | Mandatory for interoperability claim. | Perform DICOM compliance testing; capture results. |
| **Cybersecurity risk assessment report** | Must address FDA’s cybersecurity expectations. | Conduct threat analysis, map mitigations; include in submission. |
| **Usability validation data** | Required for software that impacts clinical interpretation. | Conduct formative and summative usability studies per IEC 62366‑1. |

---

### 5. Risk Management & Controls  

| Control Area | Required Artifact / Activity |
|--------------|-------------------------------|
| Hazard Identification & Risk Analysis | ISO 14971:2019 risk management file (initial and residual risk) |
| Software Lifecycle Hazards | IEC 62304 safety class justification; design verification of each software unit |
| Cybersecurity Threat Modeling | NIST‑based threat model, mitigation plan, post‑market monitoring |
| Usability Risks | IEC 62366‑1 usability validation report (task analysis, user testing) |
| AI/ML Algorithm Drift | PCCP with performance monitoring metrics and change‑control procedures |
| Interoperability Failures | DICOM/IHE conformance test logs; HL7 FHIR interface verification |

All above artifacts will be cross‑referenced in the Design History File (DHF) to satisfy 21 CFR Part 820.30 design‑control requirements.

---

### 6. Human‑Escalation Triggers  

| Situation | Reason for Escalation | Who Should Review |
|-----------|-----------------------|--------------------|
| Predicate clearance > 7 yr old | Requires “modernization” justification and potentially additional clinical data. | RA Lead & Regulatory Counsel |
| Predicate is discontinued or recalled | May necessitate selection of an alternative predicate or de‑novo request. | Product Manager & RA Lead |
| AI/ML module without a completed PCCP | Non‑compliant with FDA Dec 2024 guidance; submission cannot proceed. | Software Engineering Lead + RA Lead |
| Split‑predicate approach considered | Forbidden for IFU equivalence; needs senior review. | Regulatory Affairs Director |
| Security controls insufficient (e.g., no encryption, weak authentication) | Violates FDA cybersecurity expectations; could halt clearance. | Cybersecurity Officer & RA Lead |
| Evidence gaps in V&V or usability testing | Incomplete demonstration of safety/effectiveness. | QA/Testing Manager + RA Lead |
| Unresolved differences between new IFU and predicate IFU | May indicate a change in intended use → additional data required. | Clinical Affairs & RA Lead |

Escalations should be documented in the project risk‑register and communicated via the defined Change Control process (e.g., FCCP if applicable).

---

### 7. Peer Review Prompt  

> **To a fellow Regulatory Affairs colleague:**  
> Please critique the predicate selection logic, especially the handling of predicates older than seven years and the prohibition on split predicates. Verify that all required evidence items align with the latest FDA software guidance (2023) and AI/ML PCCP requirements (Dec 2024). Identify any jurisdiction‑specific gaps—particularly around UDI labeling, QMSR documentation, or additional post‑market surveillance obligations that may have been omitted.

--- 

*All framework citations are based on established CFR parts and ISO/IEC standards; no instance identifiers were present in the source excerpts.*

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

1. Chunk `1069833492575158480`

> ## 7. Predicate 선정 실무 체크리스트 - [ ] FDA 510(k) Database(accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm) 검색 — Product Code 기준 - [ ] 최근 5년 내 clearance 우선, 7년 이상 clearance는 FDA의 "use of predicates" 모던화 동향 고려하여 **추가 보강** 필요 - [ ] Predicate이 시장에서 **여전히 판매** 중인지 (retired/discontinued 확인) - [ ] Predicate이 Recall/Safety Communication 대상인지 확인 (FDA MAUDE / Medical Device Recalls DB) - [ ] Indications for Use 원문 문자 수준 비교, 자사 IFU가 **동일 또는 더 좁은가** - [ ] 기술특성 차이 항목 목록화 → 각 항목별 justification 데이터 확보 가능성 확인 - [ ] Split Predicate 구성 금지 — 1개 primary에서 IFU 동등 확인 우선

2. Chunk `1138382899539139891`

> ### 4.3 촬영실 GUI SW (Imaging Workstation SW) - Software Level of Documentation (FDA 2023 SW guidance "Basic/Enhanced") - IEC 62304 Safety Class (A/B/C) - 주요 기능 목록 (Acquisition / Processing / Display / Storage / Transfer / Worklist / QA Tools) - AI/ML 모듈 포함 여부 — 포함 시 PCCP 설정 - DICOM 적합성 진술서 (Storage SCU/SCP, Worklist SCU, MPPS, Print SCU 등) - 지원 OS 및 최소 HW 요구사항 - 보안 조치 (인증 방식, 암호화, 감사로그, 업데이트 경로) - SBOM 제공 형식 (SPDX / CycloneDX) - Interoperability (HL7 FHIR, IHE profiles 지원 여부) - 지원 언어 / 현지화

### kb-eval-20261027-it01-ra_us-004

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_us-004", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "843e276a3c427d48", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md", "source_hash": "6c864b98fca94d3a9546fde9cef298ef58210c9ac702628a937bcf05144604b6"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `843e276a3c427d48`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/T-FDA510K-B3_SE_%EB%B9%84%EA%B5%90%ED%91%9C_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `6c864b98fca94d3a9546fde9cef298ef58210c9ac702628a937bcf05144604b6`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `T-FDA510K-B3_SE_비교표_템플릿.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 개정 이력 | 버전 | 일자 | 변경 내용 | 작성자 | |------|------|-----------|--------| | v0.1 | 2026-09-09 | 골격 템플릿 신규 생성 (FDA-510K-B3 증빙 미비 해소) | RA 담당자 | --- ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance Section B.3 - FDA 510(k) Premarket Notification Database (predicate 검색·K-number 확인용, 실 predicate 선정 시 필수 조회)
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – 510(k) Predicate‑Strategy Summary**

| Item | Assessment |
|------|------------|
| **Device type & intended use** | *[Insert brief description and claimed indications]* – e.g., “Software for automated segmentation of abdominal CT images for clinical decision support.” |
| **Classification / Regulatory Pathway** | • 510(k) Traditional submission (21 CFR §807.92). <br>• Class II if the device falls under a radiology/ imaging‑software category → **§892.2050** (Medical image management and processing system – Class II). <br>*If the intended use is outside §892, classification must be derived from the FDA product code list.* |
| **Primary submission route** | Traditional 510(k) with Refuse‑to‑Accept (RTA) pre‑screening per FDA “Refuse to Accept Policy for 510(k)s” – see Guidance Section B.3 (source). |
| **Core evidentiary elements required** | 1. **Predicate identification** – K‑numbers from FDA 510(k) Premarket Notification Database (mandatory search). <br>2. **Substantial‑equivalence comparison table** (device description, intended use, technological characteristics, performance data). <br>3. **Bench / performance testing** – accuracy, precision, repeatability per recognized guidance (e.g., ACR‑MRI phantom studies for imaging software). <br>4. **Software validation** – IEC 62304 2006+A1:2015 lifecycle processes; verification & validation test reports. <br>5. **Risk management file** – ISO 14971 2019 risk analysis, mitigation plan, residual risk evaluation. <br>6. **Biocompatibility (if any patient‑contact material)** – ISO 10993‑1 2018. <br>7. **Labeling & Instructions for Use** – 21 CFR §801. |
| **Missing / incomplete information (based on source excerpt)** | • No specific predicate K‑numbers provided – *no specific identifier found in source — verify separately*. <br>• Absence of a documented Predetermined Change Control Plan (PCCP) if the device incorporates AI/ML updates. <br>• No evidence of compliance with the **QMS Regulation (Part 820)** that became effective 2026‑02 (ISO 13485 2016‑aligned). <br>• UDI allocation strategy not described – §830.10 onward required. |
| **Risk Controls (per ISO 14971:2019)** | 1. Hazard identification for software failure modes (incorrect segmentation, data loss). <br>2. Mitigation: redundant algorithm check, user‑override capability, audit trail logging. <br>3. Protective measures: training program, post‑market surveillance plan (voluntary reports under §806). |
| **Key citations (framework references)** | • 21 CFR §807 – Premarket notification (510(k)) requirements. <br>• 21 CFR §892.2050 – Class II imaging‑software classification. <br>• ISO 14971 2019 – Risk management for medical devices. <br>• IEC 62304 2006+A1:2015 – Software lifecycle processes. <br>• ISO 10993‑1 2018 – Biological evaluation of medical devices. <br>• 21 CFR §820 – Quality Management System Regulation (effective Feb 2026). <br>• 21 CFR §830.10–§830.60 – UDI requirements. |
| **Human‑escalation triggers** | 1. **Predicate Gap:** After a reasonable search of the FDA Premarket Notification Database no suitable K‑number can be identified → pause submission and seek senior RA input or consider De Novo classification. <br>2. **Risk‑analysis Deficiency:** Incomplete or unverified residual risk assessment – require senior risk‑management review before filing. <br>3. **QMS Non‑Compliance:** Evidence that the organization has not implemented the 2026 QMS Regulation → trigger escalation to Quality Assurance leadership. <br>4. **UDI Allocation Issue:** Absence of a UDI issuing agency agreement – must be resolved prior to submission. <br>5. **AI/ML Change Plan Missing:** No PCCP documented where required – elevate to product‑development lead and regulatory manager. |
| **Next steps** | 1. Conduct exhaustive predicate search (FDA 510(k) database) → capture K‑numbers & compare. <br>2. Compile the Substantial‑Equivalence matrix with all technical attributes. <br>3. Finalize risk management dossier per ISO 14971. <br>4. Verify QMS compliance with Part 820 and prepare UDI labeling package. <br>5. Draft RTA response checklist; submit for internal review before filing. |

---

**Peer‑review prompt**

*Please challenge the assumptions above:*

1. Is the classification under **§892.2050** appropriate given the limited device description, or might another product code apply?  
2. Have we captured all evidence elements required for a software‑intensive imaging device (e.g., clinical performance data, usability testing)?  
3. Are there any jurisdiction‑specific gaps—such as missing references to FDA’s 2024 Predetermined Change Control Plan guidance—that need clarification before finalizing the submission plan?  

*Your feedback will be incorporated into the final regulatory strategy.*

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

1. Chunk `162881704545950641`

> ## 개정 이력 | 버전 | 일자 | 변경 내용 | 작성자 | |------|------|-----------|--------| | v0.1 | 2026-09-09 | 골격 템플릿 신규 생성 (FDA-510K-B3 증빙 미비 해소) | RA 담당자 | ---

2. Chunk `349912156821510479`

> ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance Section B.3 - FDA 510(k) Premarket Notification Database (predicate 검색·K-number 확인용, 실 predicate 선정 시 필수 조회)

### kb-eval-20261027-it01-ra_us-005

<!-- kb_eval_case {"agent": "ra_us", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_us-005", "iteration": 1, "matched_keywords": ["FDA", "510k"], "profile_id": "ra-us", "scenario_id": "068814db781214e3", "source": "github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A1_Cover_Letter_템플릿.md", "source_hash": "27034e7259b482d0ed24713a8f35b4d9f41831499a0ac3e06bb99100802d0bf5"} -->

- Agent: `ra_us` / Mike (US)
- Scenario: `068814db781214e3`
- Source: `github:holee9/MD-process/01_법규_규제/03_미국_FDA/T-FDA510K-A1_Cover_Letter_템플릿.md`
- Source link: [Open source document](https://github.com/holee9/MD-process/blob/main/01_%EB%B2%95%EA%B7%9C_%EA%B7%9C%EC%A0%9C/03_%EB%AF%B8%EA%B5%AD_FDA/T-FDA510K-A1_Cover_Letter_%ED%85%9C%ED%94%8C%EB%A6%BF.md)
- Source hash: `27034e7259b482d0ed24713a8f35b4d9f41831499a0ac3e06bb99100802d0bf5`
- Focus: 510(k) predicate strategy
- Matched keywords: FDA, 510k

**Source Summary**

- 문서 요약: `T-FDA510K-A1_Cover_Letter_템플릿.md`는 FDA 510(k), predicate, substantial equivalence 또는 product code 판단을 다루는 문서입니다.
- 현재 excerpt 핵심: ## 관련 문서 | 문서 | 연계 내용 | |------|-----------| | 13_규제평가_체크리스트/FDA_510k_RTA.md | FDA-510K-A1~A5 (Section A: Submission Coverage) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B1_Device_Description_템플릿.md | Device Description (본 Cover Letter의 Device Trade Name/Common Name 근거) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md | Predicate Device 비교 근거 | ## 출처 - FDA, "Refus...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `510(k) predicate strategy` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `510(k) predicate strategy`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - predicate 선정, IFU 범위, 기술적 차이, substantial equivalence를 입증할 data 필요성을 중심으로 확인합니다.
  - FDA 업무에서는 predicate/IFU, substantial equivalence, QMSR/design-control, AI/cybersecurity, submission evidence 영향을 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft: 510(k) Predicate‑Strategy Blueprint**

---

### 1. Classification & Submission Route  
- **Device Class:** Determine under **21 CFR Part 892** (Imaging – radiology & image‑processing). The exact sub‑section (e.g., §892.2050 for “Medical image management and processing system”) must be confirmed from the device’s intended use description. *No specific identifier found in source – verify separately.*  
- **Regulatory Pathway:** Standard **510(k) Premarket Notification** (21 CFR Part 807). The submission will follow the **FDA‑510K‑A1 → A5** coverage sections outlined in the internal “FDA_510k_RTA.md” checklist.

---

### 2. Core Submission Elements (per FDA Refuse‑to‑Accept Policy)  
| Element | What to Provide | Current Status from Source | Gap / Missing Information |
|---|---|---|---|
| **Device Description** | Trade name, common name, intended use, device classification, fundamental technology, description of patient population and clinical environment. | Template referenced: *T‑FDA510K‑B1_Device_Description_템플릿.md* – assumed to be populated. | No excerpt confirming completion; verify that all fields (especially intended use) are filled. |
| **Predicate Comparison Table** | Side‑by‑side comparison of the proposed device with a legally marketed predicate: Indications for Use, technological characteristics, performance specifications, labeling, and risk controls. | Template referenced: *T‑FDA510K‑B3_SE_비교표_템플릿.md*. | Specific predicates (510(k) number, registration number) not identified in the excerpts – need selection and justification. |
| **510(k) Cover Letter** | Summary of submission contents, statement of substantial equivalence, list of included modules, and reference to any FDA guidance used. | Current document is a cover‑letter template; assumes inclusion of above sections. | No evidence that the cover letter cites the exact RTA policy or includes regulatory citations; must be added. |
| **Bench/Software Validation** | Verification & validation reports (IEC 62304 software life‑cycle, IEC 60601‑1 safety testing if applicable). | Not mentioned in source excerpts. | Required evidence missing – plan and generate test protocols and reports. |
| **Risk Management File** | ISO 14971:2019 risk analysis, mitigation measures, residual risk evaluation, and verification of risk controls. | Not referenced. | Must be prepared and cross‑referenced to the predicate comparison. |
| **Labeling & UDI** | Full labeling package (USPI, IFU) complying with 21 CFR Part 801; UDI label per 21 CFR §830.10 onward. | No mention of labeling or UDI compliance in excerpts. | Create labeling set and assign a Unique Device Identifier; include GUDID submission plan. |
| **QMS Documentation** | ISO 13485:2016‑aligned Quality Management System (effective under QMSR, 21 CFR Part 820). | Not discussed. | Ensure current QMS is in place; provide evidence of QMS compliance (e.g., SOP list, audit reports). |
| **Predetermined Change Control Plan (PCCP)** – if AI/ML component | Documented plan for pre‑authorised modifications. | No mention. | Required only when the device incorporates adaptive algorithms; develop PCCP if applicable. |

---

### 3. Evidence Package – Minimum Required Documents  
1. Completed **Device Description** (B1 template).  
2. **Predicate Device Comparison Table** (B3 template) with at least one cleared predicate identified by its 510(k) number. *(instance identifier needed – verify separately)*  
3. **Bench‑test data** (performance, accuracy, safety) aligned to the intended use.  
4. **Software/Hardware validation reports** (IEC 62304, IEC 60601‑1 as appropriate).  
5. **Risk Management File** (ISO 14971:2019).  
6. **Labeling set** meeting 21 CFR Part 801 and UDI labeling per §830.10+.  
7. **Quality System evidence** (QMSR compliance, SOP list, audit certificates).  

---

### 4. Risk Controls – Mapping to Substantial Equivalence  
| Hazard | Control in Predicate | Proposed Control (New Device) | Verification |
|---|---|---|---|
| Incorrect image acquisition parameters | Calibration routine, hardware interlocks | Same calibration plus software checksum verification | Bench testing against tolerance limits |
| Data loss/corruption during storage | Redundant RAID, error‑checking codes | Implement CRC + automatic backup to secure server | Simulated failure mode testing |
| User interface misuse leading to incorrect settings | UI lockouts, training prompts | Context‑sensitive help and mandatory confirmation dialogs | Usability study with target users |
| Electrical safety (if applicable) | IEC 60601‑1 compliance testing | Same test protocol; add leakage current monitoring | Accredited lab test report |

*All controls must be documented in the risk management file and shown to meet or exceed those of the predicate.*

---

### 5. Citations (per source excerpts)

| Requirement | Source Citation |
|---|---|
| Submission coverage sections A1–A5 | “FDA‑510K‑A1~A5 (Section A: Submission Coverage)” – listed in **13_규제평가_체크리스트/FDA_510k_RTA.md**. |
| Device description template | “T‑FDA510K‑B1_Device_Description_템플릿.md” – referenced in the related documents table. |
| Predicate comparison template | “T‑FDA510K‑B3_SE_비교표_템플릿.md” – referenced in the related documents table. |
| Refuse‑to‑Accept Policy reference | FDA, *“Refuse to Accept Policy for 510(k)s” Guidance* (no specific identifier provided). |
| Classification under Part 892 | Implicit via imaging device context; exact § number not given – verify separately. |

---

### 6. Human‑Escalation Triggers  

| Trigger | Action Required | Escalation Point |
|---|---|---|
| **Missing predicate identification** (no cleared 510(k) number selected) | Pause submission build, perform market search, select appropriate predicate. | RA lead → Regulatory Project Manager |
| **Insufficient bench‑test data** (performance gap > 10 % of predicate) | Generate additional testing plan; consider supplemental data request. | QA Lead → Senior RA |
| **Unresolved labeling discrepancies** (UDI format non‑conformant) | Engage labeling specialist, revise label artwork. | Regulatory Affairs Manager |
| **QMSR non‑compliance indication** (ISO 13485 audit finding) | Implement corrective actions; document in SOP list. | Quality Assurance Director |
| **AI/ML change‑control needed but PCCP absent** | Draft and submit Predetermined Change Control Plan before filing. | AI/ML Lead → RA Manager |
| **FDA RTA “Refuse to Accept” notice received** (e.g., missing module) | Respond within 30 days with corrected documents; update project schedule. | Submission Coordinator → Project Sponsor |

If any of the above triggers materialize, the responsible functional lead must **notify the Regulatory Lead** and **document the issue in the project risk register** before proceeding.

---

### 7. Recommended Next Steps  

1. Confirm the exact imaging‑device classification (§892.xxx) based on intended use.  
2. Select a cleared predicate (include 510(k) number, regulation date).  
3. Populate B1 and B3 templates with complete information; link each claim to supporting evidence.  
4. Assemble the evidence package listed in Section 3; perform internal “Refuse‑to‑Accept” pre‑review using the checklist (A1–A5).  
5. Conduct a gap analysis against FDA’s RTA guidance; remediate any deficiencies before electronic submission.  

---

### 8. Peer Review Prompt  

*Please review this draft and challenge:*

- The adequacy of the predicate selection approach given only template references are shown.  
- Any missing US‑specific requirements (e.g., GUDID filing, labeling nuances) not captured from the source excerpts.  
- Potential jurisdictional gaps where EU/Korean terminology might have been unintentionally carried over.  

Your feedback will be used to finalize the submission plan and close any outstanding regulatory gaps.

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

1. Chunk `108125790997756669`

> ## 관련 문서 | 문서 | 연계 내용 | |------|-----------| | 13_규제평가_체크리스트/FDA_510k_RTA.md | FDA-510K-A1~A5 (Section A: Submission Coverage) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B1_Device_Description_템플릿.md | Device Description (본 Cover Letter의 Device Trade Name/Common Name 근거) | | 01_법규_규제/03_미국_FDA/T-FDA510K-B3_SE_비교표_템플릿.md | Predicate Device 비교 근거 |

2. Chunk `137836772921583289`

> ## 출처 - FDA, "Refuse to Accept Policy for 510(k)s" Guidance (최신 개정판 확인 후 인용 필요 — 본 v0.1은 구조만 정의, 조항 원문 대조 미실시)

## ra_eu

### kb-eval-20261027-it01-ra_eu-001

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_eu-001", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "c3d3b070c47181e3", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md", "source_hash": "30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `c3d3b070c47181e3`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/README.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/README.md)
- Source hash: `30ad9d6af8345bc4dfae385cd55ad2f19049a4be6ad5bbfc551121a40f4e7622`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `README.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules) ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MDR 2017/745 Classification & Conformity‑Assessment Route**  

---

### 1️⃣ Device Overview (derived from the source)

| Item | Description (as inferred from the excerpts) |
|------|---------------------------------------------|
| **Intended Use** | Diagnostic device that emits ionising radiation (X‑ray generator). |
| **Software Component** | Medical‑device software (SaMD) that may be used to process or display the X‑ray images. |
| **Relevant MDR Sections** | Annex I (GSPR), Annex II (Technical Documentation), Annex III (PMS), Annex VIII (Classification Rules). |
| **Key Classification Rules Cited** | **Rule 10** – “Ionising‑radiation‑emitting diagnostic devices → Class IIb”  <br> **Rule 11** – SaMD classification (class depends on impact of the decision support). |

*Citation*: Rule 10 and Rule 11 are explicitly mentioned in source excerpt [2]; Annex I, II, III, VIII are listed in source excerpt [1].

---

### 2️⃣ Classification & Conformity‑Assessment Route  

| Attribute | Determination |
|-----------|----------------|
| **MDR Class** | **Class IIb** – because the device emits ionising radiation for diagnostic purposes (Rule 10). |
| **Conformity‑assessment route** | **Annex IX** (full quality‑management system + technical‑documentation assessment by a Notified Body) – required for all Class IIb devices (Art. 52(4)). <br> *Alternative route* (Annex X + XI) is also permitted for Class IIb, but Annex IX alone satisfies the minimum requirement and is the most common path for X‑ray systems. |
| **NB involvement** | Mandatory – a Notified Body must review the QMS (ISO 13485:2016) and assess the complete technical documentation (Annex II). |

*Citation*: Classification rule (Rule 10 → Class IIb) from source [2]; conformity‑assessment routes per Art. 52(4) and Annex IX/​X + XI – framework reference.

---

### 3️⃣ Required Evidence & Documentation  

| Section | Mandatory Content (MDR / ISO / IEC) | Where it belongs |
|---------|--------------------------------------|------------------|
| **Technical Documentation** | Device description, intended purpose, variants, labeling, IFU, drawings, specifications; conformity to GSPR (Annex I). | Annex II §1‑6 |
| **Quality Management System** | ISO 13485:2016 certificate; procedures covering design, production, post‑market activities. | Annex IX Chapter I & III |
| **Risk Management File** | Risk analysis, risk control measures, residual‑risk evaluation, benefit–risk determination (ISO 14971:2019). | Annex I §3 (framework) + Annex II §6.1 |
| **Clinical Evaluation Report (CER)** | State‑of‑the‑art literature review, clinical data (pre‑market), benefit‑risk analysis; kept current (Art. 61, Annex XIV Part A). | Annex II §6.1 / Annex XIV Part A |
| **Post‑Market Surveillance (PMS) System** | PMS plan (Art. 84), PMS procedures & reporting system (Art. 83), periodic safety update report (PSUR) for Class IIb (Art. 86, at least annually). | Annex III + Art. 86 |
| **Post‑Market Clinical Follow‑up (PMCF)** | PMCF plan (Annex XIV Part B) and interim/final evaluation reports (benefit–risk updates, real‑world performance of radiation output & software). | Annex XIV Part B |
| **Usability/ Human Factors** | IEC 62366‑1:2015+A1:2020 usability engineering file – especially for operator interaction with X‑ray controls. | GSPR §5, §22 |
| **Radiation Safety** | Evidence of compliance with ionising‑radiation protection (Annex I §16; IEC 60601‑2‑54). | Annex I §16 |
| **Software Validation** | IEC 62304:2006+A1:2015 development lifecycle & verification/validation evidence for SaMD. | GSPR §17, §18 |
| **Labeling & IFU** | Full labeling complying with Annex I §23 (language, symbols, safety information). | Annex II §5 / Annex I §23 |

*All items above are derived from MDR framework references; no specific identifiers appear in the source excerpts.*

---

### 4️⃣ Gaps – Missing Information (to be supplied before submission)

| Gap | Why it matters | Evidence needed |
|-----|----------------|-----------------|
| **Exact Intended Use Statement** | Drives classification and risk analysis. | Manufacturer’s intended‑use description. |
| **Device Architecture & Variants** | Required for Annex II §1‑2 (device description). | Technical drawings, BOM, software architecture diagram. |
| **Clinical Data Package** | Supports CER & PMCF; essential for benefit–risk conclusion. | Clinical investigation report or equivalent clinical performance data (e.g., multicentre study results). |
| **Radiation Output Test Reports** | Demonstrates compliance with §16 (radiation safety) and IEC 60601‑2‑54. | Accredited test reports, calibration certificates. |
| **Software Hazard Analysis & Verification Results** | Required for SaMD risk management (Rule 11) and IEC 62304 compliance. | Hazard analysis matrix, unit/integration/system test logs. |
| **Usability Evaluation Report** | Addresses GSPR §5 (use‑error) and §22 (lay‑person use). | Human‑factors testing results with representative operators. |
| **PMS & PMCF Plans** (detailed activities, timelines, sample sizes) | Needed for Art. 84/​86 compliance; early detection of safety signals. | Draft PMS plan, PMCF study protocol. |
| **Declaration of Conformity (DoC) content** | Must include all required items per Art. 19 & Annex IV. | Completed DoC draft. |

*Note*: No specific identifiers are supplied in the source material for any of these gaps; therefore “no specific identifier found in source — verify separately” applies.

---

### 5️⃣ Key Risk Controls (derived from GSPR & standards)

| Hazard Category | Control Measure | Reference |
|-----------------|-----------------|-----------|
| **Ionising radiation exposure** | Shielding design, interlock safety, automatic exposure control, compliance with IEC 60601‑2‑54. | Annex I §16; IEC 60601‑2‑54. |
| **Software malfunction / erroneous image processing** | IEC 62304 development lifecycle, verification & validation, fail‑safe defaults, regular software updates under a change‑control procedure. | Annex I §17/§18; IEC 62304. |
| **User error (operator misuse)** | Usability engineering (IEC 62366‑1), training programme, clear labeling (Annex I §23). | GSPR §§5, 22; IEC 62366‑1. |
| **Electrical safety** | Compliance with IEC 60601‑1 (general requirements for medical electrical equipment). | Annex I §18. |
| **Residual risk after controls** | Benefit–risk analysis documented in CER & RMF; periodic review via PSUR/PMCF. | Annex I §8; Art. 61, Annex XIV Part A/B. |

---

### 6️⃣ Human‑Escalation Triggers (action points that require a responsible person’s decision)

| Trigger | Condition | Required Human Decision |
|--------|-----------|--------------------------|
| **Unclear Intended Use** | Absence of a definitive purpose statement. | Senior product manager must define & sign‑off intended use. |
| **Insufficient Clinical Evidence** | No clinical investigation or adequate performance data available. | Clinical affairs lead must commission/obtain appropriate study; pause submission until data are received. |
| **Risk Management Incomplete** | Open items in RMF (e.g., unmitigated residual risks). | Risk‑management officer must close/open risk controls and obtain top‑management approval. |
| **Software Classification Ambiguity** | SaMD impact not yet mapped to Rule 11 class. | Software lead with clinical team must perform classification analysis and document basis. |
| **PMS/PMCF Plan Gaps** | Missing monitoring activities, sample size calculations, or timelines. | Post‑market surveillance manager must complete the plan; NA review cannot proceed without it. |
| **Notified Body Query** | NB raises “non‑conformity” on any of the above items. | Project lead must coordinate corrective actions and provide evidence before next audit milestone. |

When any trigger is hit, the relevant function (e.g., Clinical Affairs, Risk Management, Software Development) must be alerted via formal change request or project‑status update; the submission cannot advance to NB assessment until resolved.

---

### 7️⃣ Summary of Regulatory Judgment

- **MDR Classification:** **Class IIb** (Rule 10 – ionising‑radiation diagnostic device).  
- **Conformity‑assessment route:** **Annex IX** (full QMS + technical‑documentation assessment) – mandatory NB involvement; Annex X + XI is an alternative but not required.  
- **Core documentation set:** Technical file (Annex II), CER (Annex XIV Part A), PMCF plan & report (Annex XIV Part B), PMS system (Art. 83‑86), RMF (ISO 14971:2019, Annex I §3).  
- **Key missing items:** Precise intended use, complete clinical data package, radiation safety test reports, software validation evidence, detailed PMS/PMCF plans, usability evaluation results, and a draft DoC.  

These gaps must be closed before the Notified Body can accept the dossier for review.

---

### 8️⃣ Peer‑Review Prompt

> **To the RA peer reviewing this draft:**  
> Please examine (a) the assumption that Rule 10 alone determines Class IIb without any interplay from Rule 11 for the software component; (b) whether all applicable IEC standards (e.g., IEC 60601‑2‑54, IEC 62304, IEC 62366‑1) have been correctly linked to the relevant GSPR clauses; and (c) if any additional MDR requirements—such as “implantable” provisions or special labeling for ionising radiation devices—have been overlooked. Highlight any jurisdiction‑specific nuances that could affect the chosen conformity‑assessment route.

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

1. Chunk `447774914011501626`

> ## 수록 대상 - MDR 2017/745 원문 (영문·국문 번역본) - 개정 Regulation (EU) 2023/607 (전환기간 연장) - Annex I (General Safety and Performance Requirements, GSPR) - Annex II (Technical Documentation) - Annex III (Post-Market Surveillance) - Annex VIII (Classification Rules)

2. Chunk `488982025572022524`

> ## 핵심 포인트 - **Rule 10**: 이온화 방사선 방출 진단기기 (X-ray 발생장치 → Class IIb) - **Rule 11**: Medical Device Software (SaMD) 분류 - **GSPR** 체크리스트 기반 적합성 평가 필수 - **PMS / PMCF / PSUR** 체계 구축 필요

### kb-eval-20261027-it01-ra_eu-002

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_eu-002", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "f5804857c401f69d", "source": "github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md", "source_hash": "83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `f5804857c401f69d`
- Source: `github:holee9/ra-project/05_전문가교육/Week04_MDR_EU_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week04_MDR_EU_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `83fe77d38e73c00b0d546abfffb6985d20fda1d3f898e6532af93bd999c6b8ae`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `Week04_MDR_EU_체계_상세.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUF...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Preliminary MDR Classification & Conformity‑Assessment Planning**

---

### 1. Scope of the assessment  
The source material does not contain a description of the device’s intended purpose, design‐features or patient population. Consequently a definitive class cannot be assigned at this stage; the draft therefore outlines the **process** that must be followed once those data become available and flags the information gaps that must be closed before any formal submission.

---

### 2. Classification methodology (per MDR)

| Step | Action | Regulatory basis |
|------|--------|-------------------|
| 2.1 | Manufacturer performs *self‑classification* – applies the sequence of the 22 rules in **Annex VIII** and adopts the highest resulting class. | Art. 51 MDR + Annex VIII (rule hierarchy) |
| 2.2 | If any doubt remains, consult the national Competent Authority (CA) or the MDCG “Borderline‑and‑Classification” manual (latest version v2.1.1 – Sep 2023). | Art. 51 MDR; MDCG guidance (non‑legislative) |
| 2.3 | Record the rule number(s) applied and justification in the **Technical Documentation – Section 1.4 “Classification”** (Annex II §1.4). | Annex II, §1.4 |

> **Missing information required to apply Step 2:**  
> • Full intended purpose / indications for use (including patient/clinical setting)  
> • Description of the energy source or measurement function (to decide between Rules 9–11, 17, etc.)  
> • Whether the device is active, invasive, sterile, a measuring instrument or software‑only  

---

### 3. Anticipated conformity‑assessment routes (once class is known)

| MDR Class | Art. 52 reference | Required NB involvement | Typical route |
|-----------|-------------------|------------------------|---------------|
| **I** (non‑sterile, non‑measuring, non‑reusable surgical) | Art. 52(7) – self‑declaration | No NB | Technical Documentation (Annex II/III) + EU DoC (Art. 19 & Annex IV) |
| **Is / Im / Ir** | Art. 52(7) – limited NB scope (sterile, measuring or reusable surgical) | Yes (limited) | Annex IX Chapters I & III *or* Annex XI Part A |
| **IIa** | Art. 52(6) | Yes | Annex IX (QMS + technical‑doc assessment of a representative device) |
| **IIb** | Art. 52(4) | Yes | Annex IX (full QMS + technical‑doc) *or* Annex X (type‑examination) + Annex XI |
| **III** | Art. 52(3) | Yes | Annex IX (full assessment) *or* Annex X + Annex XI |

> The exact route will be chosen once the class is fixed; the draft assumes a **Class IIa/IIb** device unless evidence points otherwise.

---

### 4. Evidence package required for MDR submission  

| Deliverable | Regulatory location | Typical contents |
|-------------|---------------------|------------------|
| **Technical Documentation (TD)** | Annex II §§1‑6 | Device description, design & manufacturing information, GSPR compliance (Annex I), risk management file, verification/validation data, labeling (Annex I §23) |
| **EU Declaration of Conformity** | Art. 19; content in Annex IV | Manufacturer details, device identification, conformity‑assessment route citation, reference to standards, signed by authorised person |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A; kept current under Art. 61 | State‑of‑the‑art literature review, clinical data (pre‑market & post‑market), benefit–risk analysis |
| **Post‑Market Clinical Follow‑up (PMCF) plan & report** | Annex XIV Part B | Planned studies, methodology, endpoints, interim/final results |
| **PMS system & reports** | Art. 83‑86 | PMS Plan (Art. 84), periodic safety update report (PSUR – Art. 86) for Class IIa/IIb/III; incident reporting per Art. 87 |
| **UDI registration** | EUDAMED (device registration) | UDI‑DI, issuing agency, packaging levels |
| **Authorized Representative documentation** | Art. 11 | Evidence of appointment, contact details in EUDAMED |
| **Relevant standards & conformity‑assessment evidence** | Various – see “Current standard editions” table | IEC 60601‑2‑54 (radiography), ISO 14971:2019, ISO 13485:2016, etc. |

> **Reference excerpts:**  
> • “CEP + CER (Article 61, MDR Annex XIV)” – confirms need for CE marking and a CER (framework reference).  
> • “UDI … EUDAMED UDI/DEV” – validates requirement to register the UDI in EUDAMED.  
> • “시판 후 감시 … Vigilance (MDR Art. 87), PSUR” – obliges PMS plan, vigilance and PSUR (Art 87 & Art 86).  
> • “Authorized Representative … (Art. 11)” – mandatory appointment of an EU‑based AR.

---

### 5. Identified gaps (information needed before a definitive submission)

| Gap | Why it matters | Action |
|-----|----------------|--------|
| **Intended purpose & indications** | Drives rule selection in Annex VIII and determines class. | Obtain the manufacturer’s labeling/IFU draft. |
| **Device architecture (active vs passive, software‑only)** | Determines applicability of Rules 9‑11, 17 and associated standards (IEC 60601‑2‑54, IEC 62304, etc.). | Request a block diagram and functional description. |
| **Sterility / measuring function** | Triggers Is/Im/Ir sub‑classes requiring NB involvement. | Clarify packaging & intended use. |
| **Clinical data inventory** (pre‑market studies, existing CE devices, literature) | Required for the CER (Annex XIV Part A). | Compile all available clinical evidence. |
| **Risk Management File** (ISO 14971 compliance) | Needed for Annex I §§3‑8 and to support GSPR fulfilment. | Request current RMF or initiate risk analysis. |
| **PMS plan draft** | Must address Art. 84 & Art. 86 reporting cadence. | Draft PMS plan aligned with device class. |
| **UDI allocation strategy** | Needed for EUDAMED registration and traceability. | Decide on issuing agency and format. |
| **Authorized Representative (AR) appointment** | Required under Art. 11 before placing on EU market. | Identify or confirm AR. |

---

### 6. Core risk‑control considerations (mapped to Annex I)

| Annex I § | Requirement | Typical controls for a generic medical device |
|-----------|-------------|----------------------------------------------|
| §3 (Risk Management System) | Implement ISO 14971:2019 – risk analysis, evaluation, control, review. | RMF with residual‑risk acceptance criteria. |
| §4 (Risk Control Measures) | Apply protective measures & verify effectiveness. | Design safeguards, alarms, user training. |
| §5 (Use‑error Risks) | Identify potential use errors and mitigate. | Human factors engineering per IEC 62366‑1. |
| §6 (Device Lifetime) | Define service life, maintenance schedule. | Lifetime testing, replacement intervals. |
| §7 (Transport & Storage) | Protect against damage during logistics. | Packaging validation, temperature monitoring. |
| §8 (Benefit–risk determination) | Demonstrate that benefits outweigh residual risks. | Clinical evidence summary in CER. |
| §23 (Labeling & IFU) | Provide clear instructions, warnings, contraindications. | Draft labeling compliant with MDR Annex I §23. |

---

### 7. Human‑escalation triggers  

| Situation | Trigger | Who must be alerted / next step |
|-----------|---------|---------------------------------|
| **Classification ambiguity** (multiple rules could apply) | Unable to select a single rule after internal review. | Escalate to senior RA lead for CA or MDCG consultation. |
| **Missing clinical evidence** (no comparable CE device, insufficient literature) | CER cannot be completed to a “current” status under Art. 61. | Pause submission; initiate clinical investigation per Art. 62/63. |
| **Residual risk not acceptable** (RMF shows unjustified residual hazards) | Benefit–risk conclusion fails Annex I §8. | Conduct design redesign or add protective measures before proceeding. |
| **PMS plan does not meet class‑specific cadence** (e.g., PSUR missing for Class IIb) | Non‑compliance with Art. 86 reporting schedule. | Update PMS documentation; involve NB if required. |
| **No EU Authorized Representative identified** | Mandatory under Art. 11 prior to CE marking. | Senior compliance manager must appoint/contract an AR. |
| **UDI strategy incomplete** (no issuing agency selected) | EUDAMED registration cannot be completed. | Assign UDI coordinator; liaise with GUDID/EU‑UDI database. |

---

### 8. Summary judgment  

*At present the device cannot be definitively classified or assigned a conformity‑assessment route because essential product information is missing.* The regulatory pathway will follow **Article 51 + Annex VIII** for self‑classification, and once the class is determined the appropriate **Art. 52** route (Annex IX alone, or Annex X + XI) will be selected. All MDR evidence items listed in Section 4 must be assembled, with particular focus on the Clinical Evaluation Report, PMS system (Art. 83‑86), and Risk Management File (ISO 14971:2019).  

**Immediate actions:** obtain the missing product data (intended use, architecture, clinical evidence) and conduct a preliminary risk analysis. Until these are provided, no formal submission can be prepared.

---

### 9. Peer‑review request  

> *Colleague, could you evaluate whether the classification workflow outlined above fully respects the hierarchy of Annex VIII rules given our unknown device characteristics? Please also check that all MDR citations (Art. 51, Art. 52 paragraphs, Art. 61, Art. 83‑87, Art. 11, Art. 19) are correctly linked to the required deliverables and flag any jurisdictional gaps (e.g., reliance on Korean “의료기기법 §31”).*

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

1. Chunk `1024305232637496780`

> 요 多) | CEP + CER (Article 61, MDR Annex XIV) | | UDI | UDI 포털 (udiportal.mfds.go.kr) | GUDID (accessgudid.nlm.nih.gov) | EUDAMED UDI/DEV | | 시판 후 감시 | 이상사례 보고 (의료기기법 §31) | MDR 21 CFR 803 + MedWatch | Vigilance (MDR Art.87), PSUR | | Authorized Rep. | 수입자 (국내 수입업허가자) | US Agent (510(k) 면제 외) | Authorized Representative (Art.11) | | 수수료 | 품목별 허가 수수료 | MDUFA IV 수수료 (FY2026: $27,720~$440,867) | NB 계약 기반 (€10,000~€100,000+) |

2. Chunk `1026819504541667541`

> ### 3.1 분류 원칙 (Article 51 + Annex VIII) - 제조사가 직접 분류 책임 부담 (자가 분류) - Annex VIII 22개 규칙 순차 적용 → 해당하는 가장 높은 등급 적용 - 의심 시 관할 CA(Competent Authority) 또는 MDCG Manual on Borderline and Classification 참조 - 최신판: 2023-09 개정 (Manual v2.1.1)

### kb-eval-20261027-it01-ra_eu-003

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_eu-003", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "b4f23aeb22f4f084", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md", "source_hash": "d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `b4f23aeb22f4f084`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexII_Technical_Documentation_Template.md)
- Source hash: `d4de24b69463ef4cb88bca0ca127e22d1e0fc81e768639ad038739bfabaa4731`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexII_Technical_Documentation_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMS...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Planning**

---

### 1. Situation Overview  
The source material supplies a generic technical‑documentation template (MDR Annex II) and a summary of the legal framework, but **no device‑specific data** (intended purpose, mode of action, patient population, etc.) are present. Consequently a definitive classification cannot be rendered at this stage.

---

### 2. Classification & Conformity‑Assessment Route  

| Step | What is required | How to obtain it | Likely outcome (if information were supplied) |
|------|------------------|------------------|-----------------------------------------------|
| **a) Define Intended Use & Mode of Action** | Narrative description, indications, contraindications, user group. | Manufacturer’s product‑definition dossier. | Determines which *Classification Rule* (Annex VIII) applies – e.g., Rule 9, 10, 11, 17 for active devices; Rules 1‑8 for non‑active. |
| **b) Apply the appropriate Classification Rule** | Identify rule number and class (I, Is/Im/Ir, IIa, IIb, III). | Cross‑check against Annex VIII. | **If a Class I device:** self‑declaration under Art. 52(7). <br>**If Class Is/Im/Ir:** limited NB involvement per Art. 52(7). <br>**If Class IIa, IIb or III:** NB‑involved route per Art. 52(6)–(3). |
| **c) Select Conformity‑Assessment Route** | Annex IX (QMS + TD assessment) for all classes except where the alternative Annex X + XI is chosen for Class IIb/III. | Decision matrix in MDR, Art. 52. | – **Annex IX only** (full NB review). <br>– **Annex X + XI** (type‑examination + production verification) where appropriate. |

*Because the intended use and rule are absent, the draft records a **“classification pending”** status and flags the need for those inputs.*  

---

### 3. Evidence Required (per class & route)

| Class / Route | Technical Documentation (Annex II §1‑6) | Clinical Evaluation (Annex XIV Part A) | PMCF (Annex XIV Part B) | PMS (Art. 83‑86) | Notified‑Body Deliverables |
|---------------|------------------------------------------|----------------------------------------|-------------------------|------------------|----------------------------|
| **Class I (self‑declaration)** | Device description, labelling, design & manufacturing, GSPR checklist, risk‑management summary, verification & validation reports. *(All listed in source excerpt §1–§6)* | No NB review; CER must be kept current (Art. 61). | Optional if deemed necessary. | PMS plan (Art. 84) and annual report (Art. 85). | None |
| **Class Is/Im/Ir** | Same as Class I **plus** evidence of sterility, measuring function or reusable‑surgical nature. | CER required; NB may request limited clinical data. | PMCF plan for the sterile/measuring aspect. | PMS plan + periodic reporting (Art. 85). | NB review of Annex IX Chapter III (or Annex XI Part A) for the specific attribute. |
| **Class IIa** | Full Annex II contents; additionally a *representative* device’s technical file assessed under Annex IX §4. | CER (Annex XIV Part A). | PMCF plan & interim report (Annex XIV Part B). | PSUR every 2 years (Art. 86). | NB assessment of QMS (Annex IX Chapter I) and technical documentation (Annex IX §4). |
| **Class IIb** | Same as IIa, but *all* devices in the generic group require assessment (or each implantable individually). | CER + stronger clinical evidence. | PMCF plan; periodic updates. | PSUR annually (Art. 86). | Either Annex IX full‑assessment route **or** Annex X + XI (type‑examination & production verification). |
| **Class III** | Complete Annex II dossier; rigorous GSPR compliance. | CER with highest level of clinical evidence. | Comprehensive PMCF program. | PSUR annually (Art. 86). | Annex IX full assessment **or** Annex X + XI. |

*All rows reference the generic template shown in source excerpt [1] (sections §1‑§6) and the legal anchor listed in source excerpt [2] (Annex II, Annex I GSPR, Annex XIV).*

---

### 4. Identified Documentation Gaps (from source)

| Required Item | Presence in Source | Gap |
|---------------|-------------------|-----|
| **Device Description** (intended use, principle of operation) – §1 | Mentioned as “§1 Device Description” but no content supplied. | → Need full narrative and classification‑rule justification. |
| **Labeling / IFU** – §2 | Listed in the template; actual label/IFU not provided. | → Provide label text, symbols, instructions (Annex I §23). |
| **Design & Manufacturing Details** – §3 | Template references “Design History File”, but no detailed BOM, process flow or manufacturing controls present. | → Supply drawings, material specifications, process validation. |
| **GSPR Checklist** – §4 | Referenced; actual checklist absent. | → Complete Annex I GSPR mapping for each requirement (§1‑9, §10‑22, §23). |
| **Risk Management File** – §5 | ISO 14971 cited, but no risk analysis, evaluation of residual risk or benefit‑risk determination attached. | → Deliver full RMF per Annex I §3 and §§4‑8. |
| **Verification & Validation (V&V) Reports** – §6 | Mentioned; test protocols/results not supplied. | → Generate V&V plan, bench/clinical test data, acceptance criteria. |
| **Clinical Evaluation Report (CER)** | Not present in the excerpt. | → Mandatory for all classes > I; must be prepared per Annex XIV Part A. |
| **PMCF Plan / Report** | Not shown. | → Required for Classes Is/Im/Ir, IIa‑III; develop per Annex XIV Part B. |
| **PMS Documentation (Plan, Reports, PSUR)** | Only legal references cited. | → Draft PMS plan (Art. 84) and schedule PSURs (Art. 86). |

---

### 5. Risk Controls – Core Requirements

1. **Risk Management System** – ISO 14971 (2019 edition) *as required by Annex I §3*.  
2. **GSPR Mapping** – Complete checklist against the 23 requirements (Annex I §§1‑9, 10‑22, 23).  
3. **Usability / Use‑Error Analysis** – Apply IEC 62366‑1 (2020) for human factors where relevant (Annex I §5).  
4. **Software Lifecycle** – If software is involved, follow IEC 62304 (2006+A1:2015) and Annex I §17.  
5. **Electrical Safety / Radiation Protection** – For active devices, comply with IEC 60601‑2‑54 or other pertinent sub‑standards (Annex I §16 & §18).  

All above are referenced in the source summary (*“Annex I (GSPR)”* appears in excerpt [2]).

---

### 6. Human‑Escalation Triggers

| Trigger | Reason | Action Required |
|--------|--------|------------------|
| **Missing Intended Use / Mode of Action** | Prevents rule selection & classification. | Request a complete *Device Description* from the product team. |
| **Absence of Clinical Evidence (CER, PMCF)** | NB cannot verify benefit‑risk. | Initiate clinical‑evaluation planning; assign CE/clinical liaison. |
> **Escalation:** If any of the above items remain outstanding after two working days, raise to the Regulatory Lead for *Classification Decision* and *NB Engagement Strategy*.  

| **Incomplete Risk Management File** | Residual risk not demonstrably acceptable. | Assign risk‑engineer to complete RMF; flag to Quality Manager. |
| **Unfinished PMS Plan/PSUR schedule** (for Class IIa‑III) | Violates Art. 84/86 reporting obligations. | Task post‑market surveillance owner to draft plan within 5 days. |

These triggers are derived from the MDR obligations (Art. 83‑86) and the template requirements shown in source excerpt [1].

---

### 7. Citations (per instruction)

| Item | Source citation |
|------|-----------------|
| **MDR Annex II – Technical Documentation structure** | Source [1] “§1 Device Description … §6 Verification & Validation”. |
| **Annex I – GSPR** | Source [2] “Annex I (GSPR)”. |
| **Legal basis (EU MDR 2017/745)** | Source [2] “법적 근거 EU MDR 2017/745, Annex II”. |
| **Applicable annexes for clinical evaluation & PMS** | Source [2] “Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD)”. |
| **Classification‑rule reference framework** | No specific rule number appears in the source – *no specific identifier found in source — verify separately*. |
| **ISO 14971 edition** | Framework reference (standard edition 2019) – no source identifier needed. |
| **IEC 62366‑1, IEC 62304, IEC 60601‑2‑54** | Framework references; not quoted from the source. |

---

### 8. Peer‑Review Prompt  

> *“Colleague, please review the assumptions underlying the ‘classification pending’ status and the evidence matrix above. In particular: (a) verify that the listed documentation gaps align with the MDR Annex II template; (b) confirm whether any of the cited annexes (XIV, XV, III) impose additional mandatory items for the device categories we may encounter; and (c) highlight any jurisdiction‑specific omissions (e.g., language requirements beyond English) that could affect NB review.”*  

--- 

**End of Draft**.

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

1. Chunk `1018876481739455645`

> | 섹션 | MDR Annex II | FDA Design History File (21 CFR 820 / QMSR 2024) | MFDS 기술문서 (의료기기법 시행규칙 별표 3) | |---|---|---|---| | 제품 설명 | §1 Device Description | Design Output, Device Description (DHF) | 제1장 사용목적·작용원리 | | 라벨·IFU | §2 Labeling | Device Labeling (21 CFR 801; eSTAR §6) | 제3장 표시기재 | | 설계·제조 | §3 Design & Manufacturing | Design History File (§7.3 QMSR) | 제2장 구조·원재료·제조방법 | | 안전성 요구사항 | §4 GSPR Checklist | 510(k) SE comparison + Performance testing | 제4장 성능 / 제5장 안전성 | | 위험관리 | §5 Risk Management | Risk Management File (ISO 14971; not explicitly DHF) | 안전성 평가 (Risk 포함) | | 검증·유효성 확인 | §6 Verification & Validation | V&V Reports (DHF), Bi...

2. Chunk `1043015132787588014`

> ## 개요 | 항목 | 내용 | |---|---| | 법적 근거 | EU MDR 2017/745, **Annex II** (Technical Documentation) | | 적용 대상 | MDR 적용 의료기기 전 Class (I · IIa · IIb · III) | | 발효일 | 2021-05-26 (Class IIb/III full enforcement) | | 관련 Annex | Annex I (GSPR), Annex XIV (Clinical Evaluation), Annex XV (Clinical Investigation), Annex III (PMS TD) | | 언어 | 최소 영어 필수; NB 요구 언어 추가 | ---

### kb-eval-20261027-it01-ra_eu-004

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_eu-004", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "27fb295ca12e7c7c", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md", "source_hash": "ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `27fb295ca12e7c7c`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_2017_745/MDR_AnnexIII_PMS_TD_Template.md)
- Source hash: `ad5402d408dd51e69da524b4e92e5b9020ddb6c1e35ad971d5bf0902885a34b2`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_AnnexIII_PMS_TD_Template.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MDR Classification & Conformity‑Assessment Summary for the Three In‑House X‑ray Products**

| Product | Intended Use (as inferred from source) | MDR Class* | Primary MDR Rule (Annex VIII) | Conformity‑assessment route (Art. 52) | Core Evidence Required (MDR/ISO) |
|---------|----------------------------------------|------------|------------------------------|--------------------------------------|-----------------------------------|
| **X‑ray Detector** | Detects diagnostic X‑ray images; used in radiography systems | IIa | Rule 17 – “devices intended for recording diagnostic X‑ray images” | Art. 52(6): **Annex IX** (QMS + technical‑documentation assessment of one representative device per category) – NB involvement required.  <br>Alternative: **Annex II** + **Annex III** + **Annex XI §10** (production conformity verification) – verify separately. | • Clinical Evaluation Report (CER) – Annex XIV Part A  <br>• PMS Plan (Art. 84) & PMS System (Art. 83)  <br>• Periodic Safety Update Report (PSUR) every **2 years** – Art. 86  <br>• Risk Management File (RMF) – Annex I §3‑9, ISO 14971:2019  <br>• IEC 62220‑1‑1 DQE test data (referenced in source)  |
| **Handheld X‑ray Source** | Portable active emitter of ionising radiation for diagnostic use | IIb | Rule 10 – “active devices emitting ionising radiation for diagnostic radiology” | Art. 52(4): **Annex IX** (full QMS + technical‑documentation assessment of one representative device per generic group) *or* **Annex X + Annex XI** (type‑examination + production conformity verification).  NB involvement mandatory. | • CER – Annex XIV Part A  <br>• PMS Plan & System (Art. 84/83)  <br>• PSUR every **1 year** – Art. 86  <br>• PMCF plan/evidence – Annex XIV Part B (clinical data “actively collected” per source)  <br>• IEC 60601‑2‑28 (X‑ray tube assemblies) & IEC 60601‑2‑54 (radiography equipment) test reports  <br>• Battery safety assessment, mechanical‑damage analysis  |
| **GUI Software (SaMD)** | Provides image display and decision support for X‑ray diagnostics | IIa | Rule 11 – “software providing information used for diagnostic decisions” (risk level consistent with Class IIa) | Art. 52(6): **Annex IX** (QMS + technical‑documentation assessment of one representative device).  NB involvement required. | • CER – Annex XIV Part A  <br>• PMS Plan & System (Art. 84/83)  <br>• PSUR every **2 years** – Art. 86  <br>• PMCF plan/evaluation – Annex XIV Part B (mandatory “error‑data collection” per source)  <br>• IEC 62304 (software lifecycle) compliance evidence  <br>· IEC 62366‑1 (usability engineering) records  <br>· Bug‑log & maintenance records (referenced in source) |

\*Classification is taken directly from the source table (“Class IIa”, “Class IIb”). The corresponding MDR rules are identified according to Annex VIII classification rules.

---

### 1. Required Evidence – Checklist per Product  

| Evidence | Where Required by MDR | Status (based on source) |
|----------|----------------------|---------------------------|
| **Technical Documentation** (Annex II §1‑6) | All devices – mandatory for NB review | “CER, RMF, IEC 62220‑1‑1 test data” etc. listed – partially present; full TD still needed (design files, labeling, UDI, manufacturing processes). |
| **Risk Management File** | Annex I §3‑9; ISO 14971:2019 | Mentioned (“CER, RMF”) – confirm complete risk analysis for radiation over‑exposure, battery failure, software misuse. |
| **Clinical Evaluation Report (CER)** | Annex XIV Part A (Art. 61) | Cited as required but no concrete CER attached – **missing**. |
| **Post‑Market Surveillance Plan** | Art. 84 | “PMS 담당 데이터 소스” table defines data sources – a formal written PMS plan still needed. |
| **Post‑Market Surveillance System** | Art. 83 | Implied via “Vigilance 시스템, EUDAMED”, but system description and responsibilities not shown – **missing**. |
| **Periodic Safety Update Report (PSUR)** | Art. 86 – frequency 2 yr (IIa) / 1 yr (IIb) | Frequency indicated; no PSUR drafts provided – **missing**. |
| **Post‑Market Clinical Follow‑up (PMCF) Plan & Evaluation** | Annex XIV Part B | For handheld source – “clinical data actively collected” noted; for GUI SW – “error‑data collection mandatory”. Detailed PMCF protocol not supplied – **missing**. |
| **U​DI Registration in EUDAMED** | Art. 33‑39 | “UDI 등록 + Vigilance 보고” listed – registration evidence required. |
| **IEC / ISO Test Reports** | Relevant GSPR (Annex I §§16‑18) | • Detector – IEC 62220‑1‑1 DQE data cited.<br>• Handheld source – no IEC 60601‑2‑28/54 reports shown – **missing**.<br>• GUI SW – IEC 62304 maintenance record referenced, but full lifecycle documentation missing. |
| **Labeling & IFU (Annex I §23)** | Required for all classes | No labeling extracts supplied – **missing**. |

---

### 2. Identified Gaps / Missing Information  

1. **Complete Clinical Evaluation Report** (including state‑of‑the‑art literature review, clinical data summary).  
2. **Formal PMS Plan & System description** (organisational responsibilities, trigger thresholds, reporting flow to EUDAMED).  
3. **Full Risk Management File** with residual risk evaluation and verification of risk‑control measures for each identified hazard (radiation dose, mechanical failure, battery explosion, software misinterpretation).  
4. **Production‑conformity evidence** for the handheld source (type‑examination certificate if Annex X route is chosen; otherwise detailed batch‑release testing records).  
5. **IEC 60601‑2‑28 / IEC 60601‑2‑54 compliance reports** for the handheld X‑ray source (electrical safety, electromagnetic compatibility, radiation protection).  
6. **Usability/ Human Factors validation** for GUI SW (IEC 62366‑1) – test protocols, user‑testing results.  
7. **Labeling & IFU** including symbols, contraindications, warnings, and UDI matrix.  
8. **Evidence of PMCF activities** (study protocol, enrollment numbers, interim analysis) particularly for the handheld source where “clinical data actively collected” is recommended.  

---

### 3. Risk Controls – Mapping to MDR GSPR (§1‑9)  

| Hazard | Potential Harm | Primary Control(s) | MDR Reference |
|--------|----------------|--------------------|--------------|
| **Radiation over‑exposure** (detector & handheld source) | Tissue damage, stochastic effects | • Built‑in dose‑monitoring circuitry<br>• Automatic shut‑off at preset dose thresholds<br>• Operator training & exposure‑time limits<br>• Compliance with IEC 60601‑2‑54 (radiation safety) | Annex I §16 (Radiation protection), §18 (Active devices) |
| **Mechanical failure / battery rupture** (handheld source) | Burns, explosion, device immobilisation | • Robust housing, impact testing per IEC 60601‑2‑54<br>• Battery management system with over‑charge/over‑discharge protection<br>• Periodic functional safety checks | Annex I §20 (Mechanical & thermal risks), §6 (Device lifetime) |
| **Software error / mis‑display** (GUI) | Misdiagnosis, inappropriate treatment | • IEC 62304 compliant software development lifecycle<br>• Automated self‑test at start‑up; error logging & safe‑state fallback<br>• Usability testing per IEC 62366‑1 to minimise use errors<br>• Post‑market error‑data collection (mandatory PMCF) | Annex I §17 (Electronic programmable systems), §5 (Use‑error risks) |
| **Data integrity / cyber‑security breach** (all devices) | Loss of patient data, tampering of device settings | • Secure firmware signing, access control<br>• Regular security updates (documented in maintenance log) | Annex I §3 (Risk management), emerging GSPR guidance on cybersecurity (to be integrated). |

---

### 4. Relevant MDR / Standards Citations  

| Item | Citation |
|------|----------|
| Classification rules (Rule 17, Rule 10, Rule 11) | **Annex VIII** – read applicable rule numbers. |
| Conformity‑assessment routes per class | **Art. 52(6)** for Class IIa; **Art. 52(4)** for Class IIb. |
| Clinical Evaluation Report requirement | **Annex XIV Part A** (kept current under Art. 61). |
| PMCF plan & evaluation report | **Annex XIV Part B**. |
| PMS system & plan | **Art. 83** (system) and **Art. 84** (plan). |
| PSUR frequency (2 yr for IIa, 1 yr for IIb) | **Art. 86(2)**. |
| Risk Management File basis | **Annex I §3** (risk‑management system) – ISO 14971:2019. |
| General Safety & Performance Requirements (GSPR) referenced for hazards | **Annex I §§16, 17, 18, 20**. |
| UDI registration obligation | **Art. 33‑39** (EUDAMED). |
| IEC test standards mentioned in source | **IEC 62220‑1‑1** (DQE measurement), **IEC 60601‑2‑28**, **IEC 60601‑2‑54**, **IEC 62304**, **IEC 62366‑1** – current editions as per the reference table. |
| No specific device‑identifiers, decree numbers or article sub‑paragraphs appear in the source excerpts. | *no specific identifier found in source — verify separately* |

---

### 5. Human‑Escalation Triggers  

| Trigger Condition | Action Required (Human) |
|-------------------|--------------------------|
| **Missing or incomplete CER** | Halt NB submission; request full clinical evaluation documentation before any conformity‑assessment step proceeds. |
| **Absence of formal PMS Plan/System** | Pause PSUR preparation; develop written PMS plan, assign responsible person‑in‑charge, and update EUDAMED vigilance module. |
> *Escalate to the Quality Management Lead (QML) for immediate drafting and sign‑off.* |
| **Unverified IEC 60601‑2‑28/54 compliance** (handheld source) | Stop type‑examination or Annex IX technical‑documentation assessment until test reports are obtained. |
> *Escalate to the Engineering & Test Lead for commissioning of safety testing.* |
| **PMCF data collection not defined or insufficient** (especially for handheld source) | Suspend submission; formulate a detailed PMCF protocol, obtain ethics/clinical site agreements, and schedule data capture. |
> *Escalate to Clinical Affairs Manager.* |
| **PSUR update overdue relative to required frequency** | Issue compliance warning; postpone CE‑marking renewal until the latest PSUR is compiled and NR (Notified Body) approves. |
> *Escalate to Regulatory Project Coordinator.* |
| **Risk analysis shows residual risk > acceptable limit** (e.g., radiation dose exceeding thresholds) | Immediate risk mitigation actions, redesign or additional safeguards; cannot proceed to conformity assessment. |
> *Escalate to Head of Risk Management & senior management for risk acceptance decision.* |
| **UDI registration not complete in EUDAMED** | Block the declaration of conformity; ensure UDI dossier is uploaded and validated. |
> *Escalate to EUDAMED compliance officer.* |

---

### 6. Regulatory Judgment  

- All three products are correctly classified under MDR (Detector IIa, Handheld Source IIb, GUI SaMD IIa).  
- The **appropriate conformity‑assessment routes** are: Annex IX for the Detector and GUI; Annex IX *or* Annex X + XI for the handheld source.  
- Current documentation (as reflected in the source) provides high‑level evidence (e.g., PSUR frequency, data sources, linked standards) but **lacks several mandatory deliverables**: full Clinical Evaluation Report, formal PMS plan/system, complete risk management file, detailed IEC 60601 test reports for the handheld source, and a complete PMCF protocol.  

Consequently, **the submission cannot be considered ready for Notified‑Body review** until the gaps identified above are closed. The escalation triggers listed must be acted upon promptly to avoid project delays.

---

### Peer‑Review Prompt  

> *Colleague, please challenge the assumptions made in this draft:*
> 
> 1. Are the classification rules (Rule 17, Rule 10, Rule 11) applied correctly given the limited product descriptions?  
> 2. Does the chosen conformity‑assessment route for each class align with current MDR practice for X‑ray devices (especially regarding optional Annex X + XI use)?  
> 3. Have we omitted any MDR‑specific evidence (e.g., “Summary of Safety and Clinical Performance” for Class III/implantable devices) that might be required for future product extensions?  
> 4. Are the identified risk controls sufficient to satisfy Annex I GSPR §§16, 17, 18, 20, or are additional measures (e.g., electromagnetic compatibility testing) needed?  

Please review and provide feedback on any missing regulatory obligations or alternative pathways that could streamline the submission while remaining compliant.

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

1. Chunk `1039815103287926448`

> ## 자사 3개 제품 영향 맵핑 | 요구사항 | X-ray Detector (Class IIa) | Handheld X-ray Source (Class IIb) | GUI SW (Class IIa) | |---|---|---|---| | 적용 보고서 유형 | PSUR | PSUR | PSUR | | PSUR 갱신 주기 | **2년** | **1년** | **2년** | | PMCF 필요성 | 동등성 클레임 검토 후 결정 | 이온화 방사선 → 임상 데이터 적극 수집 권고 | SaMD → 사용 중 오류 데이터 수집 필수 | | PMS 담당 데이터 소스 | DQE 저하, 픽셀 결함, 환자선량 초과 | 선량 초과, 기계적 손상, 배터리 이상 | SW 오류, 영상 표시 오류, 사용성 이슈 | | EUDAMED 의무 | UDI 등록 + Vigilance 보고 | UDI 등록 + Vigilance 보고 | UDI 등록 (SaMD) + Vigilance | | 연계 문서 | CER, RMF, IEC 62220-1-1 시험 데이터 | CER, RMF, 방사선 선량 모니터링 데이터 | CER, IEC 62304 유지보수 기록, Bug log | ---

2. Chunk `27496288286129299`

> ### 1.1(a) — 정보 수집원 (Sources of Information) | # | 정보 수집원 | 수집 방법 | 주기 | X-ray Detector | Handheld Source | GUI SW | |---|---|---|---|---|---|---| | 1 | Serious incidents + PSURs + FSCAs | Vigilance 시스템, EUDAMED | 즉시/분기 | ● | ● | ● | | 2 | 비심각 사고 + 부작용 데이터 | Complaint 관리 시스템 | 월별 | ● | ● | ● | | 3 | Trend reporting 데이터 | 내부 통계 집계 | 분기 | ● | ● | ● | | 4 | 전문 학술지·기술 DB·레지스트리 | PubMed, IEC/ISO DB, MAUDE | 반기 | ● | ● | ● | | 5 | 사용자·유통사·수입업자 피드백 및 불만 | CRM, 서비스 데이터 | 월별 | ● | ● | ● | | 6 | 동종 유사 기기 공개 정보 | 경쟁사 TD, EUDAMED, MAUDE DB | 반기 | ● | ● | ● | > 범례: ● 적용 / ○ 해당 없음

### kb-eval-20261027-it01-ra_eu-005

<!-- kb_eval_case {"agent": "ra_eu", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_eu-005", "iteration": 1, "matched_keywords": ["MDR"], "profile_id": "ra-eu", "scenario_id": "18eb2c4361447a4e", "source": "github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md", "source_hash": "4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1"} -->

- Agent: `ra_eu` / Theo (EU)
- Scenario: `18eb2c4361447a4e`
- Source: `github:holee9/ra-project/01_규제지식베이스/유럽_CE_MDR/MDR_인허가_상세가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EC%9C%A0%EB%9F%BD_CE_MDR/MDR_%EC%9D%B8%ED%97%88%EA%B0%80_%EC%83%81%EC%84%B8%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `4c8b9d6c012d9a29f4e1941e69343b644f771191a691b419b328661a5e8eaba1`
- Focus: MDR classification and conformity route
- Matched keywords: MDR

**Source Summary**

- 문서 요약: `MDR_인허가_상세가이드.md`는 EU MDR classification, conformity route, technical documentation 또는 MDR 운영 요구사항 문서입니다.
- 현재 excerpt 핵심: ### 2.3 Rule 11 (SW) > Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as class IIa. > 단, decision may cause (a) death or irreversible deterioration → **Class III**; (b) serious deterioration or surgical intervention → **Class IIb**. > Software intended to monitor physiological...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MDR classification and conformity route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MDR classification and conformity route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - MDR rule/class, conformity assessment route, NB involvement, technical documentation evidence를 중심으로 확인합니다.
  - EU MDR 업무에서는 classification/conformity route, CER/PMS/PMCF/NB response, EUDAMED, MDR evidence traceability를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Classification & Conformity Assessment Route for the “Radiology‑Room GUI Software” (Rule 11)**  

---

### 1. Device Synopsis (as derived from source)

| Attribute | Interpretation |
|-----------|----------------|
| **Intended use** (from source) – *“촬영실 GUI SW”* → software that provides information used to make diagnostic or therapeutic decisions in the radiology suite (e.g., image‑display, measurement, automated recommendation). |
| **Relevant MDR rule** | Rule 11 (software providing information for diagnosis/therapy) – see source [1]. |
| **Potential decision impact** | - If a wrong output could lead to death or irreversible deterioration → **Class III**  <br>‑ If it may cause serious deterioration or require surgical intervention → **Class IIb**  <br>‑ Otherwise (moderate/low impact) → **Class IIa**. |
| **Current classification hypothesis** | The source states “*촬영실 GUI SW = Rule 11 적용, 영향도에 따라 IIa ~ III*”. Hence the final class depends on the *impact assessment* that must be supplied by the manufacturer.

---

### 2. Classification Determination (MDR)

| MDR Reference | Requirement / Guidance |
|---------------|------------------------|
| **Rule 11** (Annex VIII) – “Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes …” → Class IIa; escalation to IIb/III per impact. *(source [1])* |
| **Art. 52(3‑6)** – Mapping of class to conformity route (see internal classification table). |

**Decision tree**

1. **Impact = death / irreversible deterioration** → **Class III**.  
2. **Impact = serious deterioration or surgical intervention** → **Class IIb**.  
3. **Impact = moderate/low (e.g., routine image viewing, non‑critical measurements)** → **Class IIa**.

*Action*: Obtain a detailed “impact analysis” from the OEM that documents clinical scenarios, outcomes of erroneous output, and the severity of harm.  

---

### 3. Conformity Assessment Route (per class)

| Class | MDR Article & Annex | Required Notified‑Body involvement |
|-------|----------------------|-------------------------------------|
| **III** | Art 52(3) – **Annex IX** (full QMS + technical‑documentation assessment) *or* **Annex X** (type‑examination) **+ Annex XI** (production conformity verification). | Full NB review required; route X+XI typically chosen for implantable/critical software. |
| **IIb** | Art 52(4) – **Annex IX** (full QMS + technical‑documentation assessment of a representative device) *or* **Annex X + XI**. | NB review required; Annex IX is the most common route for non‑implantable Class IIb software. |
| **IIa** | Art 52(6) – **Annex IX** (QMS + technical‑documentation assessment). | NB review mandatory but less extensive than for IIb/III. |

*Note*: For all classes above I, a **quality‑management system** compliant with **ISO 13485:2016** is mandatory (Art 10(9) & Annex IX §2).

---

### 4. Required Technical Evidence (MDR Annex II §§1‑6)

| Section | Mandatory Content | MDR Reference |
|---------|-------------------|---------------|
| **1 – Device description & specification** | Detailed function, architecture diagram, intended users, operating environment, hardware/software interfaces. | Annex II §1 |
| **2 – Manufacturer & authorised representative** | Legal entity details, UDI‑Device Identifier (if applicable). | Annex II §2 |
| **3 – Design & manufacturing information** | Software development lifecycle (IEC 62304), version control, configuration management, release procedures. | Annex II §3 |
| **4 – General Safety & Performance Requirements (GSPR)** | Demonstration of compliance with all relevant §§1‑9 (risk management), §§16‑18 (electrical/active device aspects), §§23 (labelling). | Annex I §§1‑9, 16‑18, 23 |
| **5 – Benefit–Risk analysis & Risk Management File** | ISO 14971:2019 risk analysis, residual risk evaluation, acceptability criteria, risk control measures. | Annex II §5; Annex I §3‑9 |
| **6 – Verification & validation (including clinical evidence)** | • Software verification per IEC 62304 <br>• Usability engineering per IEC 62366‑1 <br>• Clinical Evaluation Report (CER) – Annex XIV Part A (kept up to date, Art 61). <br>• PMCF plan & evaluation report – Annex XIV Part B. | Annex II §6.1; Annex XIV Parts A/B |

**Additional MDR‑specific evidence**

- **Post‑Market Surveillance (PMS) system** – Art 83; **PMS plan** – Art 84.  
- **Periodic Safety Update Report (PSUR)** for Class IIb/III – Art 86 (annual).  
- **Summary of Safety and Clinical Performance (SSCP)** if the software is classified as **Class III implantable** – Art 32 (not typical for a GUI, but required if declared implantable).  

---

### 5. Identified Missing Information (gaps to be resolved before dossier preparation)

| Gap | Why it matters | Suggested source / action |
|-----|----------------|---------------------------|
| **Exact decision impact description** (clinical consequence of erroneous output) | Determines class (IIa/IIb/III). | Request a “Clinical Impact Matrix” from the OEM; include case studies. |
| **Intended user group & environment** (radiology technicians, radiologists, lay persons) | Influences GSPR §22 and usability requirements. | Obtain user‑profile documentation. |
| **Software architecture & safety‑critical functions list** | Needed for risk analysis (ISO 14971) and IEC 62304 classification (A/B/C). | Request software design dossier / module breakdown. |
| **Verification & validation test reports** (unit, integration, system testing, usability) | Mandatory to demonstrate compliance with IEC 62304 and IEC 62366‑1. | Acquire validated test protocols & results. |
| **Clinical evaluation data** – literature review or device‑specific clinical investigation | Required for CER (Annex XIV Part A). | Conduct state‑of‑the‑art (SOTA) search; plan/execute a PMCF study if existing data insufficient. |
| **PMS & PSUR schedules** (especially for Class IIb/III) | Art 86 mandates periodic updates; deadlines in source [2] indicate upcoming compliance dates. | Draft PMS plan aligned with class‑specific update frequency. |
| **UDI implementation strategy** (if applicable) | Required under MDR Art 27 & Annex IV for Classes IIa and above. | Define packaging, labeling, EUDAMED registration plan. |

---

### 6. Risk Controls (MDR GSPR §3‑9)

1. **Risk Management File (RMF)** – ISO 14971:2019; link identified hazards to risk control measures.  
2. **Software safety classification** per IEC 62304 (determine if the software contains *safety‑related functions*).  
3. **Usability engineering** – IEC 62366‑1:2015+A1:2020 to mitigate use‑error risks (§5).  
4. **Cybersecurity** – Apply Annex I §8 (protection against foreseeable misuse) and consider EN ISO/IEC 27001 as supporting evidence.  
5. **Electromagnetic compatibility** (if software interacts with hardware) – IEC 60601‑1 requirements (§16).  
6. **Labeling & IFU** – Ensure clear instructions for use, warnings about decision impact, and contraindications per Annex I §23.

---

### 7. Human‑Escalation Triggers

| Trigger | Reason | Escalation target |
|--------|--------|-------------------|
| **Unclear impact level** (manufacturer cannot provide definitive clinical consequence) | Classification cannot be finalized → risk of inappropriate conformity route. | Senior Regulatory Manager + Clinical Expert for impact assessment. |
| **Missing RMF or incomplete hazard analysis** | Non‑compliance with GSPR §3‑9; NB will reject dossier. | Quality‑Management Lead to initiate risk‑analysis workshop. |
| **Absence of clinical evidence (no literature, no PMCF)** for a Class IIb/III device | CER cannot be compiled → Art 61 breach. | Clinical Evaluation Team to design/launch a post‑market clinical follow‑up study. |
| **Approaching statutory deadline** (e.g., Class III implantable deadline 2026‑05‑26 from source [2]) | Regulatory non‑conformity risk if not cleared before date. | Project Manager to accelerate submission schedule; consider provisional certification route. |
| **NB feedback requiring additional verification data** | NB may request more software validation or usability test results. | Regulatory Affairs + Engineering to produce supplemental evidence within NB’s timeline. |

---

### 8. Summary Judgment

- The “Radiology‑Room GUI Software” falls under **MDR Rule 11** (software for diagnostic/therapeutic decisions).  
- **Final classification (IIa, IIb or III) depends on a formal impact analysis** that quantifies the clinical consequences of erroneous software output.  
- Once the class is confirmed, the appropriate conformity‑assessment route is:  

  *Class III* → Annex IX **or** Annex X + XI (full NB review).  
  *Class IIb* → Annex IX **or** Annex X + XI.  
  *Class IIa* → Annex IX only.

- The dossier must contain the full set of MDR technical‑documentation elements (Annex II §§1‑6), a **CER** (Annex XIV Part A), a **PMCF plan/report** (Annex XIV Part B), and an operational **PMS system** (Art 83‑86).  

- Several critical information gaps have been identified; they must be resolved before the Technical Documentation can be compiled.  

---

### 9. Peer Review Prompt

> *Colleague, could you verify that our interpretation of Rule 11’s impact thresholds aligns with the latest MDR guidance? Also, please check whether any recent MDCG guidance (e.g., MDCG‑2022‑7) introduces additional evidence requirements for diagnostic software that we have not captured here.*  

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

1. Chunk `1007248354989010815`

> ### 2.3 Rule 11 (SW) > Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as class IIa. > 단, decision may cause (a) death or irreversible deterioration → **Class III**; (b) serious deterioration or surgical intervention → **Class IIb**. > Software intended to monitor physiological processes: 일반 IIa / immediate danger IIb. > Others: Class I. **→ 촬영실 GUI SW = Rule 11 적용, 영향도에 따라 IIa ~ III**

2. Chunk `1007987960287657537`

> ### 7.1 차등 시한 | Class | 시한 | |---|---| | Class III **custom-made** implantable | 2026-05-26 | | Class III / Class IIb **implantable** (sutures·screws 등 제외) | **2027-12-31** | | Class IIb **non-implantable** / IIa / Is / Im | **2028-12-31** |

## ra_kr

### kb-eval-20261027-it01-ra_kr-001

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_kr-001", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS", "디지털의료제품법"], "profile_id": "ra-kr", "scenario_id": "f13f0edefab0c7b6", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md", "source_hash": "e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `f13f0edefab0c7b6`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_디지털의료제품법_하위고시_추적.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EB%94%94%EC%A7%80%ED%84%B8%EC%9D%98%EB%A3%8C%EC%A0%9C%ED%92%88%EB%B2%95_%ED%95%98%EC%9C%84%EA%B3%A0%EC%8B%9C_%EC%B6%94%EC%A0%81.md)
- Source hash: `e6f3293fcf2624db7670d4d8d7e40f63a441dfc5499eb57b2e435f6392fd8e66`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS, 디지털의료제품법

**Source Summary**

- 문서 요약: `MFDS_디지털의료제품법_하위고시_추적.md`는 디지털의료제품법, SaMD/AI, SBOM/cyber 의무와 전환 리스크 관련 문서입니다.
- 현재 excerpt 핵심: ### 2-1. 2025-10-31 임상시험 가이드라인 9종 개정 (분기#2 추가) 식약처는 디지털의료제품법 하위 규정 시행 후속으로 임상시험 가이드라인 9종을 전면 개정. AI 디지털의료기기 7종(관상동맥협착·대장암·알츠하이머성 치매·유방암·전립선암·폐암/폐결절·허혈성뇌졸중) + 디지털치료기기 2종(임상시험 설계·불면증 개선). 핵심 변경: AI 추가 사용군 vs 임상의 단독진단군 **비교설계**, 분석적 임상정확도 제시, 적응증별 유효성 평가지표 예시, 전향적 임상 원칙 명확화, 효과 크기 입증·탈락률 관리 실무지침 추가. - 자사 영향: 자사 GUI SW가 AI 보조 기능 탑재 시 임상시험 설계 직접 영향. 현재 미탑재이나 향...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – P3 촬영실 GUI SW (Digital Medical‑Device Software)**  

---

### 1. Device Synopsis  
- **Product name (working title):** P3 촬영실 GUI SW  
- **Intended use:** Human–machine interface for X‑ray imaging systems (viewing, manipulation and storage of radiographic images). No AI‑based diagnostic function is currently implemented; future AI assistance is being considered.  
- **Regulatory category in source:** “디지털의료기기소프트웨어에 해당” (digital medical‑device software).

---

### 2. Classification & Submission Route  

| Item | Korean regulatory reference | Draft determination | Notes / verification needed |
|------|----------------------------|---------------------|-----------------------------|
| **Device grade** | 디지털의료제품법 시행규칙 (2026‑01‑23 개정) – 등급표 및 적용 기준 | Likely **2등급** (software that supports a Class II medical device but provides no direct diagnostic/therapeutic function). The source states “GUI SW가 2등급이든 등급 미지정이든 … 면제·대체 경로”. | *No specific grade number is given in the excerpt* → **no specific identifier found in source — verify separately** with the official 등급표 (「의료기기 품목 및 품목별 등급에 관한 규정」). |
| **Regulatory pathway** | MFDS 인증 제도 for 2등급 devices (technical‑document review by designated 심사기관) | **인증** – submission of a full technical dossier to an MFDS‑designated examination agency (e.g., KTL, KTC). If the exemption/alternative route under §25 is applicable, a supplemental justification will be required. | Confirmation of whether the “면제·대체 경로” applies must be obtained from the specific provision (§25 each sub‑paragraph) – **no specific identifier found in source — verify separately**. |

---

### 3. Required Evidence Package  

| Category | Mandatory items (Korean law/standard) | Remarks / gaps |
|----------|----------------------------------------|----------------|
| **Quality Management System** | KGMP 인증 (의료기기법 제28조) – ISO 13485:2016‑based QMS | Existing ISO 13485 certification can be leveraged; ensure it is recognized as “KGMP 적합성인정”. |
| **Software Development & Validation** | IEC 62304:2006+A1:2015 (software life‑cycle); IEC 62366‑1:2020 (usability engineering) | Provide software development plan, verification/validation reports, risk‑based testing matrix. |
| **Risk Management** | ISO 14971:2019 (risk analysis, evaluation, control) | Hazard list, risk acceptability criteria, residual risk justification. |
| **Labeling & IFU** | MFDS labeling rule (Korean language required for all labels, packaging, and Instructions For Use). | Draft Korean label/IFU; include symbols per IEC 60601‑1 series where applicable. |
| **Clinical Evaluation** | • If AI module is *not* present: clinical data may be exempt under §25 of the 시행규칙 (subject to verification). <br>• If AI will be added later: comparative design trial required by the 2025‑10‑31 임상시험 가이드라인 개정 (AI + physician vs. physician‑only) – analysis of analytical accuracy, effectiveness size, dropout management. | The source notes the new guideline but does **not** provide a notice number; therefore **no specific identifier found in source — verify separately**. |
| **Non‑clinical / Safety Tests** | ISO 10993‑1:2018 (biological safety) – if any hardware contact; otherwise not applicable. | Not required for pure software. |
| **Cybersecurity** | IEC 81001‑5‑1:2021 (cybersecurity framework) – referenced by MFDS cybersecurity guidance. | Include threat analysis, vulnerability management plan. |

---

### 4. Missing / Open Items  

1. **Exact device grade** – retrieve the official 등급표 for “영상·진단용 소프트웨어” to confirm 2등급 status.  
2. **Specific provision (§25 each sub‑paragraph)** of the 「디지털의료제품법 시행규칙」(2026‑01‑23 개정) that governs clinical‑data exemption or alternative pathway; the source only alludes to its existence.  
3. **Whether AI functionality will be integrated** before market entry – this changes both classification (potential upgrade to a higher grade) and clinical‑evaluation requirements.  
4. **Foreign clinical evidence** – if any foreign CE/FDA data are planned for use, confirm MFDS acceptance under the latest OECD MAD or CER scope notices (not covered in source).  

---

### 5. Risk Controls Summary  

| Hazard | Control (design / process) | Reference |
|--------|----------------------------|-----------|
| Incorrect image display / loss of fidelity | IEC 62304‑based verification, pixel‑integrity checks, automated rollback on error detection. | IEC 62304:2006+A1:2015 |
| User misinterpretation of UI elements | IEC 62366‑1 usability testing; Korean language UI labeling, mandatory warnings in Korean. | IEC 62366‑1:2020 |
| Unauthorized access / data breach | IEC 81001‑5‑1 cyber‑security safeguards (authentication, encryption, audit logs). | IEC 81001‑5‑1:2021 |
| Software update failure (especially if AI added later) | Fail‑safe design, version control, mandatory field‐upgrade validation per KGMP. | KGMP/ISO 13485:2016 |
| Residual risk not acceptable | ISO 14971 risk acceptance criteria; residual risk justification in technical file. | ISO 14971:2019 |

---

### 6. Citation Log  

| Type | Source excerpt (ID) | Cited element |
|------|---------------------|---------------|
| **Framework reference** | — | MFDS 디지털의료제품법 시행규칙, 의료기기법 제28조 (KGMP), ISO 13485:2016, IEC 62304:2006+A1:2015, ISO 14971:2019, IEC 62366‑1:2020, IEC 81001‑5‑1:2021 |
| **Instance identifier – guideline revision** | 1127968925422991528 | “2025‑10‑31 임상시험 가이드라인 9종 개정” (no formal notice number supplied) → **no specific identifier found in source — verify separately** |
| **Instance identifier – 시행규칙 amendment** | 198902914416608487 | 「디지털의료제품법 시행규칙」(2026‑01‑23 개정) (no formal 고시 번호 supplied) → **no specific identifier found in source — verify separately** |

---

### 7. Human‑Escalation Triggers  

| Situation | Reason for escalation | Action |
|-----------|----------------------|--------|
| **Uncertain device grade** (cannot locate definitive 등급 entry) | Incorrect classification leads to wrong submission route. | Escalate to senior RA or legal team to obtain official 등급표 confirmation. |
| **§25 exemption language unclear** (clinical‑data waiver) | Applying an inappropriate exemption could cause regulatory rejection. | Request legal/Regulatory affairs review of the exact 시행규칙 text; involve MFDS liaison if needed. |
| **Planned AI module addition** (post‑launch) | May shift grade to a higher level and trigger mandatory comparative clinical trial per 2025‑10‑31 guideline. | Submit change‑management plan; seek early MFMFDS pre‑submission advice. |
| **Foreign clinical evidence intended** (e.g., FDA 510(k) predicate) | Need to verify that the current OECD MAD / CER scope notices cover such data. | Engage external consultant or MFDS contact to confirm acceptability before dossier compilation. |
| **Labeling/IFU translation issues** (Korean language compliance) | Non‑compliant labeling results in market entry delay. | Escalate to medical writing team with timeline for Korean translation review. |

---

### 8. Peer Review Prompt  

> *Please challenge the assumptions made above, especially:*  
> 1. The inference that P3 GUI SW is a **2등급** device without explicit grade citation.  
> 2. The reliance on §25 of the 시행규칙 for a possible clinical‑data exemption – does the current amendment actually contain such language?  
> 3. Whether any foreign clinical data could be leveraged under the latest MFDS acceptance notices (OECD MAD vs. CER).  

Your input will help fill the identified gaps before final dossier preparation.

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

### kb-eval-20261027-it01-ra_kr-002

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_kr-002", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "09c205a3b12f0055", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md", "source_hash": "a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `09c205a3b12f0055`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/등급분류_기준/제품별_등급분류.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98_%EA%B8%B0%EC%A4%80/%EC%A0%9C%ED%92%88%EB%B3%84_%EB%93%B1%EA%B8%89%EB%B6%84%EB%A5%98.md)
- Source hash: `a047ec8b14b83d2c89134381bd3e4cd25f790016c8145d757a146226dee3d5d9`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `제품별_등급분류.md`는 `제품별_등급분류.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정 ###...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – MFDS Classification & Licensing Route (2등급 인증)**  

---

### 1. Device Overview & Intended Use  
| Item | Description |
|------|-------------|
| **Product family** | Integrated medical imaging system consisting of a detector module, radiation source module and accompanying software. |
| **Primary function** | Capture diagnostic images (detector) and optionally emit radiation for interventional guidance (source). |
| **Software role** | Image acquisition‐control, processing & display (SW classified under Rule 11 of the EU MDR; Korean digital‑medical‑software guidelines apply). |
| **Target market** | Domestic South Korea – to be marketed as a single system or as separate “detector only” and “source+detector” configurations. |

---

### 2. MFDS Grade Determination  

- The source explicitly states the product is **2등급** under Korean regulation, with the note that a higher grade may apply if the auxiliary function is deemed more critical【1112950876551682081】.  
- Classification basis: *디지털의료기기소프트웨어 허가·심사 가이드라인* and the “디지털의료제품법” (effective 2025‑01‑24) which introduces a distinct pathway for AI/Software‑enabled digital medical products【1112950876551682081】.  

**Result:** **2등급 → 인증** route (technical‑document review by an MFDS‑designated 심사기관).  

*No specific notice or article number is provided in the source for this classification rule – verify separately.*  

---

### 3. Submission Route & Designated Review Body  

| Step | Action | Responsible Party |
|------|--------|-------------------|
| **A‑code request** | Secure MFDS 품목코드 (A‑code) before dossier assembly. | Sponsor / Korean RA lead |
| **Technical file preparation** | Compile KGMP evidence, QMS documentation (ISO 13485:2016), risk management (ISO 14971:2019), software lifecycle (IEC 62304 2006+A1:2015). | QMS & Development teams |
| **심사기관 selection** | Choose an MFDS‑designated 심사기관 (e.g., KTL, KTC) that accepts 2등급 인증. | Sponsor |
| **Submission** | Submit Technical File + A‑code application via the MFDS e‑submission portal. | Sponsor |
| **MFDS review & approval** | MFDS performs conformity assessment; issuance of 인증서 (certificate). | MFDS |

---

### 4. Required Evidence Pack  

| Category | Specific Documents / Data | Remarks |
|----------|---------------------------|---------|
| **Device Specification** | Detailed specs: rated voltage, current, intended use, anatomical application, software functions. *(Missing – to be obtained from product strategy task list)*【1097646391221557778】 | Must be finalized before A‑code filing. |
| **Regulatory Codes** | MFDS 품목코드 (A‑code). | Pending – see “Missing Information”. |
| **Foreign Reference** | FDA 510(k) predicate device identification (via FDA Product Classification Database). | Needed for potential reliance on foreign data; not yet selected. |
| **EU Alignment** | Confirmation of EU MDR Rule 10/Rule 11 applicability (detector = IIa, source = IIb). | Already noted but final judgment required. |
| **Software Documentation** | • Software Development Plan & Lifecycle (IEC 62304) <br>• Software Verification & Validation reports <br>• Change Management Plan (per “디지털의료제품법”) <br>• Independent software suitability guideline (if standalone). | Guideline cited in source; no specific identifier provided – verify separately. |
| **Clinical Evidence** | • Clinical evaluation report (CER) based on Korean clinical data or accepted foreign CER (only if MFDS has granted mutual acceptance under the latest notice). <br>• Non‑clinical safety data (ISO 10993‑1 2018 or GLP toxicology). | No specific notice number in source – verify separate. |
| **Quality Management** | KGMP compliance certification, SOPs, device master record. | Required for 인증 route. |
| **Risk Management** | ISO 14971:2019 risk analysis file, hazard log, mitigation measures. | Needed irrespective of grade. |

---

### 5. Missing Information & Gap Analysis  

| Gap | Impact on Submission | Recommended Action |
|-----|----------------------|--------------------|
| **Final product specifications (voltage, current, intended anatomical site, software role)** | Cannot complete technical file; A‑code may be delayed. | Complete “제품 전략·사양 확정” checklist – assign responsible engineer. |
| **MFDS 품목코드 (A‑code) assignment** | Required before dossier upload. | Submit preliminary specification to MFDS for code allocation. |
| **Predicate device selection (FDA 510(k))** | Determines eligibility of foreign clinical/non‑clinical data. | Perform FDA database search; document selected predicate. |
| **EU MDR Rule 10/Rule 11 final judgment** | Affects classification of detector vs source and may influence Korean grade if auxiliary function is high. | Conduct formal EU regulatory assessment; decide system versus component strategy. |
| **Digital Medical Products Act (2025‑01‑24) detailed requirements** – change‑management plan, performance evaluation for AI/SW | Without these, software portion may be deemed non‑conformant. | Review the “디지털의료제품법” guidance; develop required documents. |
| **Specific notice numbers for Korean guidelines** (e.g., 고시 제xxxx호) | Needed for precise citation in submission dossier. | Request official MFDS guideline copies or confirm via MFDS website. |

---

### 6. Risk Controls & Compliance Framework  

| Control Area | Standard / Guideline | Implementation Notes |
|--------------|----------------------|----------------------|
| **Quality Management System** | KGMP (Medical Devices Act 제28조) – certification requirement for 인증 route. | Establish GMP‑aligned QMS, undergo KGMP audit. |
| **Risk Management** | ISO 14971:2019 (risk analysis, evaluation, control). | Perform risk management plan; link to design inputs/outputs. |
| **Software Lifecycle** | IEC 62304 2006+A1:2015. | Document software development processes, verification & validation, release procedures. |
| **Usability / Human Factors** | IEC 62366‑1 2020. | Conduct usability engineering for UI and operator interaction. |
| **Electrical Safety & EMC** | IEC 60601‑1 2005+A1:2012+A2:2020. | Generate safety test reports; ensure compliance with Korean safety standards. |
| **Biocompatibility (if any patient‐contacting materials)** | ISO 10993‑1 2018. | Provide material data, toxicology testing where applicable. |

---

### 7. Citations  

| Source Chunk ID | Citation Detail |
|-----------------|-----------------|
| 1097646391221557778 | Checklist items for product specification, A‑code confirmation, FDA predicate search, EU MDR Rule 10/Rule 11 assessment, Notified Body selection, and system vs component strategy. |
| 1112950876551682081 | Classification as **2등급**, reference to *디지털의료기기소프트웨어 허가·심사 가이드라인* and the “디지털의료제품법” (effective 2025‑01‑24) governing AI/SW digital medical products. |

*No specific regulatory instrument numbers (e.g., 고시 제xxx호, §xx‑yy) appear in the provided excerpts – verification of exact identifiers is required before final dossier submission.*

---

### 8. Human‑Escalation Triggers  

| Situation | Trigger Condition | Escalation Action |
|-----------|-------------------|-------------------|
| **Incomplete product specifications** | Any “□” item remains unchecked in the specification checklist. | Notify Project Lead & Engineering Manager to finalize specs within 5 business days. |
| **A‑code not secured** | MFDS has not issued a 품목코드 after submission of preliminary data. | Escalate to Regulatory Director for direct MFDS liaison. |
| **Unresolved classification grade** (potential upward shift to 3등급) | New evidence shows auxiliary function exceeds “보조 기능 수준”. | Immediate risk‑benefit re‑assessment; prepare contingency plan for 3등급 허가 pathway. |
| **Missing foreign regulatory identifiers** (e.g., predicate device, EU rule decision) | No documented FDA predicate or EU MDR rule outcome within the technical file. | Escalate to International Regulatory Lead for rapid lookup and documentation. |
| **Non‑conformant software documentation** | Absence of change‑management plan required by “디지털의료제품법”. | Trigger a compliance audit; involve Software Architecture Lead and Legal Counsel. |

---

### 9. Peer Review Prompt  

> *“Colleague, please review the assumptions made regarding the 2등급 classification based on the cited digital‑medical‑software guidelines, and verify whether any recent MFDS 고시 (post‑2025) could alter the certification vs 허가 pathway for integrated detector‑source systems. Also, assess if the identified gaps—especially the pending A‑code and EU MDR rule determination—are sufficiently highlighted for escalation.”*  

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

1. Chunk `1097646391221557778`

> ## 5. 제품 전략·사양 확정 To-Do (firm 데이터 의존) - [ ] 각 제품의 상세 사양(정격관전압·관전류·용도·적용부위·SW 역할) 확보 - [ ] 식약처 품목코드(A-code) 확정 - [ ] FDA Product Classification Database 직접 조회 → Predicate Device 선정 - [ ] EU MDR Rule 10 적용 최종 판단 (Detector=IIa 영상기록 / Source=IIb 방출; SW는 Rule 11). 특히 Detector 단독 판매 건 - [ ] Notified Body 선정 (NANDO 데이터베이스 기반) - [ ] 통합 시스템 vs 개별 구성품 허가 전략 결정

2. Chunk `1112950876551682081`

> ### 3.1 국내 (MFDS) — **2등급** (보조 기능 수준에 따라 상향 가능) - **근거**: 의료용 소프트웨어 허가·심사 가이드라인, 「디지털의료기기소프트웨어 허가·심사 가이드라인」 - **2025년 신법**: 「디지털의료제품법」 2025-01-24 시행 – AI/SW 적용 디지털의료제품 별도 체계 (변경관리계획, 구성요소 성능평가 등) - **독립형 SW 사용적합성 가이드라인** 별도 적용 (독립형인 경우)

### kb-eval-20261027-it01-ra_kr-003

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_kr-003", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "6668d69c1224c36d", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md", "source_hash": "07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `6668d69c1224c36d`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/MFDS_인허가_상세가이드.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/MFDS_%EC%9D%B8%ED%97%88%EA%B0%80_%EC%83%81%EC%84%B8%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- Source hash: `07149b419276d9cb9aaa7384bb44a23db18dc48038096c40b05f09601f162365`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_인허가_상세가이드.md`는 `MFDS_인허가_상세가이드.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수 ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – “촬영실 GUI SW” (2등급)  

Prepared for: Korean MFDS Regulatory Affairs (KR‑RA)  
Reference source: *MFDS_인허가_상세가이드.md* (excerpt IDs 1025612737507787646, 39359892234270838)  

---

## 1. Device Classification & Submission Route  

| Item | Determination |
|------|----------------|
| **Korean grade** | **2등급** (as explicitly stated in the source “촬영실 GUI SW (2등급)”) |
| **Regulatory pathway** | **인증** – technical‑documentation review by an MFDS‑designated 심사기관. The source also notes that a parallel route under the *디지털의료제품법* may be considered (“경로: 인증 (또는 디지털의료제품법 경로 병용 검토)”). |
| **Relevant Korean legal framework** | 의료기기법 → 시행령 → 시행규칙; MFDS 고시 “의료기기 품목 및 품목별 등급에 관한 규정” and “의료기기 허가·신고·심사 등에 관한 규정”.  <br> *No specific notice/decree number is provided in the source – verify separately.* |

---

## 2. Core Evidence Required for 인증  

| Requirement | Supporting Standard / Guidance | Notes on Application |
|-------------|--------------------------------|----------------------|
| **Quality‑Management System (KGMP)** | 의료기기법 제28조 (KGMP) – facility must hold KGMP certification. | Facility status to be confirmed (missing). |
| **Software Lifecycle & Development** | IEC 62304 (2006+A1:2015) – software safety lifecycle. | Source cites “IEC 62304 기반 수명주기”. |
| **Cyber‑security** | IEC 81001‑5‑1 (2021) – cybersecurity for medical device software; MFDS cyber‑security guidance (referenced in national guidelines). | Required because GUI SW is network‑connected. |
| **Usability / Human Factors** | IEC 62366‑1 (2015+A1:2020). | Source mentions “사용적합성”. |
| **Risk Management** | ISO 14971 (2019). | Must be submitted as part of the technical file. |
| **AI‑related Controls (if AI is incorporated)** | *Generative‑AI 가이드라인* (MFDS 2023‑xx, name only – no identifier in source) and change‑management plan. | Evidence required for algorithm validation, bias mitigation, post‑market monitoring. |
| **Labeling & IFU** | MFDS 고시 “의료기기 라벨링·사용설명서 등에 관한 규정”. Korean language mandatory for all labeling, symbols, and user instructions. | No label draft provided – missing. |
| **Clinical Evaluation (if required)** | 의료기기 허가·신고·심사 등에 관한 규정 – local clinical data may be required for 2등급 where “임상시험대상 제외 사유” does not apply. | Determine whether foreign CER can be accepted under the latest MFDS notice on mutual acceptance of foreign clinical evaluation reports (no specific notice number in source – verify). |
| **Change‑Management Plan** | MFDS guidance for software updates (referenced by “변경관리계획 활용”). | Must describe impact analysis, validation, and post‑market surveillance. |
| **Software Validation & Verification Report** | IEC 62304 + internal QA procedures. | Required as part of the technical dossier. |

---

## 3. Missing / Unclear Information (Gap Analysis)

| Gap | Why it matters | Action needed |
|-----|----------------|---------------|
| **Intended Use Statement** (e.g., “real‑time imaging display for radiology suite”) | Determines risk classification nuances and clinical evidence scope. | Obtain finalized intended use from product team. |
| **Target Population & Environment** (in‑hospital, outpatient, pediatric, etc.) | Affects usability testing and labeling. | Clarify with development lead. |
| **Detailed AI Description** (algorithm type, training data, performance metrics) | Drives need for AI‑specific risk controls and possible additional clinical evidence. | Provide AI technical dossier & validation plan. |
| **KGMP Certification Status of Development Facility** | Mandatory for 인증; lack of certification blocks submission. | Verify KGMP certificate or plan to obtain it before filing. |
| **Korean Language Labeling & IFU Drafts** | MFDS requires all labeling in Korean; missing drafts prevent dossier completion. | Prepare and have Korean‑language review completed. |
| **Cyber‑security Architecture Details** (threat model, patch strategy) | Required under IEC 81001‑5‑1 and MFDS cyber‑security guidance. | Submit security risk assessment & mitigation plan. |
| **Clinical Evaluation Strategy** – whether foreign clinical evaluation report can be used or local data needed. | Determines need for additional trials or data collection. | Check latest MFDS notice on acceptance of foreign CERs; if not covered, schedule Korean clinical study. |
| **Change‑Management Procedures** (frequency of updates, version control) | Required for software devices and for AI model changes. | Provide documented SOPs. |

---

## 4. Recommended Risk Controls (mapping to standards)

| Hazard Category | Control Measure | Standard Reference |
|-----------------|----------------|---------------------|
| Software malfunction leading to incorrect image display | Fault‑tree analysis, unit & integration testing, code reviews, IEC 62304 verification activities | IEC 62304 |
| Unauthorized access / data breach | Encryption of data in transit & at rest, authentication mechanisms, regular penetration testing per IEC 81001‑5‑1 | IEC 81001‑5‑1 |
| User error (misinterpretation of GUI) | Usability engineering process, formative and summative usability tests, IEC 62366‑1 compliance | IEC 62366‑1 |
| AI algorithm bias / performance drift | Dataset documentation, bias mitigation strategies, continuous monitoring plan, Generative‑AI 가이드라인 adherence | MFDS AI guideline |
| Software updates introducing new hazards | Change‑impact analysis, regression testing, post‑market surveillance for update‑related incidents | IEC 62304 + MFDS change‑management guidance |

---

## 5. Human‑Escalation Triggers  

| Situation | Reason to Escalate to Senior RA / Regulatory Lead |
|-----------|---------------------------------------------------|
| **Unclear classification** – if additional functionality (e.g., AI decision support) pushes the device into 3등급 or requires 허가. | Immediate review of grade and pathway. |
| **KGMP certification not yet obtained** – facility cannot submit 인증 without KGMP. | Escalate to manufacturing compliance for urgent certification. |
| **Foreign clinical evidence acceptance uncertain** – no clear MFDS notice available in source. | Senior RA must verify latest MFDS notice or seek clarification from MFDS. |
| **AI component scope expands** (e.g., adaptive learning after market) without a pre‑approved change‑management plan. | Escalate for AI risk management review and possible additional clinical evaluation. |
| **Labeling draft not approved in Korean** – language errors could cause rejection. | Legal/translation team involvement required before dossier finalization. |
| **Cyber‑security assessment reveals critical vulnerabilities** that cannot be mitigated before launch. | Immediate product freeze and security remediation plan. |

---

## 6. Reusable RA Judgment (Recorded Lesson)

> *For a 2등급 software medical device such as “촬영실 GUI SW”, the MFDS 인증 pathway is mandatory, with a technical dossier anchored on IEC 62304, IEC 62366‑1, ISO 14971, and IEC 81001‑5‑1. KGMP certification of the development/manufacturing site, Korean‑language labeling/IFU, and a documented change‑management plan are non‑negotiable prerequisites. When AI functions are present, MFDS’s Generative‑AI guideline must be applied in parallel with risk‑based validation. Any ambiguity regarding acceptance of foreign clinical evaluation reports or classification shifts caused by AI features should trigger senior RA escalation before dossier submission.*  

---

## 7. Peer Review Prompt  

**@RA‑Peer:** Please review the assumptions made above, especially:  

1. Whether the “디지털의료제품법” parallel route could be more appropriate given the software’s intended use.  
2. The completeness of the evidence list for AI components – are there additional MFDS guidelines (e.g., *AI in Medical Devices* notice) that should be cited?  
3. Any overlooked Korean‑specific obligations (e.g., post‑market surveillance reporting frequency for 2등급 software under 의료기기법).  

Your feedback will help close remaining gaps before finalizing the certification submission package.

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

1. Chunk `1025612737507787646`

> ### 1.1 전통 의료기기 체계 - **의료기기법** (법률) → 시행령 (대통령령) → 시행규칙 (총리령) - 식약처 고시: 「의료기기 품목 및 품목별 등급에 관한 규정」, 「의료기기 허가·신고·심사 등에 관한 규정」, 「의료기기 GMP 심사·평가 등에 관한 규정」 등 - 민원인 안내서(가이드라인) 다수

2. Chunk `39359892234270838`

> ### 10.3 촬영실 GUI SW (2등급) - 경로: 인증 (또는 디지털의료제품법 경로 병용 검토) - 핵심: IEC 62304 기반 수명주기 / 사이버보안 / 사용적합성 - AI 포함 시: 생성형 AI 가이드라인 / 변경관리계획 활용 --- 작성: 도메인 전문가 · 검토(QA11, 2026-06-09): 진입문서 현행성 재검증 — 핵심 규제사실 반영 확인. · 상태: 승인 · 일자: 2026-06-09

### kb-eval-20261027-it01-ra_kr-004

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_kr-004", "iteration": 1, "matched_keywords": ["MFDS", "국내_MFDS"], "profile_id": "ra-kr", "scenario_id": "d3afbf6357dd8894", "source": "github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md", "source_hash": "87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `d3afbf6357dd8894`
- Source: `github:holee9/ra-project/01_규제지식베이스/국내_MFDS/법령_고시_가이드라인/MFDS_사이버보안_가이드라인_2025_대응.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/01_%EA%B7%9C%EC%A0%9C%EC%A7%80%EC%8B%9D%EB%B2%A0%EC%9D%B4%EC%8A%A4/%EA%B5%AD%EB%82%B4_MFDS/%EB%B2%95%EB%A0%B9_%EA%B3%A0%EC%8B%9C_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8/MFDS_%EC%82%AC%EC%9D%B4%EB%B2%84%EB%B3%B4%EC%95%88_%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8_2025_%EB%8C%80%EC%9D%91.md)
- Source hash: `87919716384b28757469b31df3fedbbf4ecd9e615cba6dcab53f062b40b1b07e`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS, 국내_MFDS

**Source Summary**

- 문서 요약: `MFDS_사이버보안_가이드라인_2025_대응.md`는 `MFDS_사이버보안_가이드라인_2025_대응.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 | ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Cyber‑Security Requirements for a Medical Device (MFDS)**  

---

### 1. Korean Classification & Submission Route  
| Item | Assessment |
|------|------------|
| **Device grade (1~4등급)** | Not stated in the source. The appropriate grade must be confirmed from 「의료기기 품목 및 품목별 등급에 관한 규정」 (MFDS_인허가_상세가이드.md §2). |
| **Resulting submission track** | • 1등급 → 신고  <br>• 2등급 → 인증 (심사기관 검토) <br>• 3·4등급 → 허가.  The exact track can be selected only after the grade is verified. |

*Citation*: no specific identifier found in source — verify separately.

---

### 2. Applicable MFMF Cyber‑Security Guideline  
| Element | Detail |
|---------|--------|
| **Guideline title** | “의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서)” |
| **Revision date** | 2025‑01‑10【1】 |
| **Legal basis** | 「디지털의료제품법」(2025‑01‑24 시행) 및 의료기기법 시행규칙【1】 |
| **International alignment** | IMDRF N60/N73, IEC 81001‑5‑1 (reference standards)【1】 |

*Citation*: no specific identifier found in source — verify separately.

---

### 3. Required Evidence for Submission  

| Requirement | Evidence to be provided | Remarks |
|-------------|------------------------|---------|
| **Compliance with the 35 cyber‑security RA items** | • A matrix mapping each of the 35 items (RA‑01 ~ RA‑35) to device design / documentation.<br>• Test reports or audit records that demonstrate implementation of each control. | The exact numbering (RA‑01‒RA‑35) is listed in the official PDF; reference it when preparing the matrix【2】. |
| **Security‑by‑Design & Defense‑in‑Depth** | Design dossier showing threat modelling, security architecture, and mitigation strategies. |
| **Authentication / Access Control** | UML/flow diagrams of user authentication, role‑based access, session management; penetration test results. |
| **Encryption & Key Management** | Cryptographic algorithm specifications, key lifecycle procedures, validation of TLS version compliance. |
| **Software Integrity (Code Signing, SBOM)** | Signed binaries, code‑signing certificates, Software Bill of Materials (SBOM) list. |
| **Network Security** | Network topology, firewall ruleset, port‑restriction policy, TLS configuration proof. |
| **Vulnerability Management** | CVE monitoring plan, patch schedule, documented CVD (Cyber‑Vulnerability Disclosure) process. |
| **Audit & Logging** | Log retention policy, sample security event logs, tamper‑evidence mechanisms. |
| **Update / Maintenance Mechanism** | Secure OTA update workflow, authentication of remote management sessions. |
| **KGMP Facility Certification** | Certificate of compliance with KGMP (medical device law 제28조). |
| **Korean Language Labeling & IFU** | Full label and Instructions for Use in Korean, meeting MFDS labeling rules. |
| **Local Clinical Evidence (if required)** | Clinical evaluation report per Korean guideline; note that foreign CER acceptance is separate from the OECD MAD regime. |

*Citation*: no specific identifier found in source — verify separately.

---

### 4. Identified Gaps / Missing Information  

| Gap | Impact on Submission | Suggested Action |
|-----|----------------------|------------------|
| **Device grade (1~4등급)** | Determines whether the route is 신고, 인증 or 허가. | Retrieve the device’s classification from the MFDS “품목별 등급” list; if ambiguous, request clarification from MFDS or a certified 심사기관. |
| **Exact RA‑01 ~ RA‑35 numbering** | Needed to reference each requirement precisely in the submission dossier. | Obtain the official PDF of the 2025 guideline (referenced in【2】) and extract the full list. |
| **Evidence of KGMP compliance** | Mandatory for all grades except low‑risk notifications. | Confirm that manufacturing occurs at a KGMP‑certified site or plan to obtain certification before filing. |
| **Korean‑language labeling & IFU** | MFMF requires Korean language for all market materials. | Prepare label and IFU drafts in Korean; conduct translation verification. |
| **Local clinical data (if 3·4등급)** | May be required regardless of foreign CER acceptance. | Assess whether a domestic clinical investigation is needed per MFDS guidelines; plan accordingly. |
| **Specific MFDS notice or decree number** | Formal reference in the submission dossier. | Verify the exact 고시/공지 번호 for the cyber‑security guideline (e.g., “고시 제2025‑XX호”) from the MFDS website; currently not present in source excerpts. |

---

### 5. Risk Controls & Mitigation Strategy  

| Control Category (from the 35 RA items) | Implementation Example | How it satisfies MFDS expectation |
|----------------------------------------|-----------------------|-----------------------------------|
| **Secure Design Principles** | Threat‑model documented; security features embedded from concept phase. | Aligns with “Secure by design, Defense-in-depth, Least privilege” requirement【2】. |
| **Authentication & Access Control** | Multi‑factor authentication for maintenance mode; RBAC enforced in software. | Meets “사용자 인증, 역할 기반 접근, 세션 관리”. |
| **Encryption** | AES‑256 storage encryption; TLS 1.3 for all communications; HSM for key protection. | Satisfies “저장·전송 데이터 암호화, 키 관리”. |
| **Software Integrity** | Code signing with SHA‑256 certificate; bootloader verifies signature before launch; SBOM generated by automated tooling. | Addresses “코드 서명, 부트 무결성 검증, SBOM 관리”. |
| **Network Security** | Hardened OS, only required ports open; firewall rules audited quarterly. | Covers “포트 최소화, 방화벽, TLS 버전 요건”. |
| **Vulnerability Management** | CVE feed integrated into ticketing system; patches released within 30 days of vulnerability disclosure. | Aligns with “CVE 모니터링, 패치 주기, CVD 정책”. |
| **Audit & Logging** | Immutable log storage on write‑once media; audit trail retained ≥5 years. | Satisfies “보안 이벤트 로깅, 로그 보호, 접근 이력”. |
| **Update / Maintenance** | Signed OTA updates; remote session encrypted with mutual TLS; update process logged and verified. | Meets “보안 업데이트 메커니즘, 원격 관리 보안”. |

---

### 6. Human‑Escalation Triggers  

| Situation | Who Should Be Alerted | Reason |
|-----------|----------------------|--------|
| **Uncertain device grade** (cannot locate the grade in MFDS list) | RA Team Lead & Regulatory Affairs Manager | Incorrect submission track will cause rejection or delay. |
| **Missing official 고시/공지 number for the cyber‑security guideline** | Senior RA / Compliance Officer | Needed for precise citation in dossier; risk of non‑conformance if omitted. |
| **KGMP certification not yet obtained** (manufacturing site pending) | Quality Assurance & Project Manager | Manufacturing compliance is a prerequisite for any filing. |
| **Local clinical data requirement identified late** (after foreign CER assumed sufficient) | Clinical Affairs Lead | Absence will trigger MFDS request for additional evidence, extending timelines. |
| **Cyber‑security test results fail to meet one of the 35 RA items** | Product Development Lead & Security Engineer | Must remediate before dossier finalization; non‑compliant controls cause outright denial. |
| **Labeling/IFU not fully Korean** (drafts only in English) | Medical Writing / Localization Team | MFDS mandates Korean language; omission will be flagged during review. |

---

### 7. Peer Review Prompt  

> *Please challenge the assumptions made above regarding the classification determination, the completeness of the listed evidence items, and any potential jurisdiction‑specific gaps (e.g., post‑market surveillance obligations, KGMP timing, or interplay with OECD MAD for non‑clinical data). Confirm whether additional MFDS notices or detailed RA‑01 ~ RA‑35 listings are required to finalize the submission package.*

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

1. Chunk `1019410569588059809`

> ## 1. 개정 개요 | 항목 | 내용 | |---|---| | 문서명 | 의료기기의 사이버보안 허가·심사 가이드라인 (민원인 안내서) | | 개정일 | 2025-01-10 | | 법적 근거 | 「디지털의료제품법」(2025-01-24 시행), 의료기기법 시행규칙 | | 주무기관 | 식품의약품안전평가원 의료기기심사부 | | 핵심 변경 | 사이버보안 요구사항 **15개 → 35개** 확장 | | 조화 목적 | IMDRF N60/N73, IEC 81001-5-1 등 국제표준과 조화 → 해외 진출 원활화 |

2. Chunk `1070294818097866704`

> ### 3.2 RA 요구사항 35개 주요 카테고리 2025.01 개정으로 IMDRF N60 기준 35개로 확장된 요구사항은 아래 8개 카테고리로 분류 (정확한 RA-01~RA-35 번호는 공식 가이드라인 PDF 참조): | 카테고리 | 주요 요구사항 | |---|---| | **보안 설계 원칙** | Secure by design, Defense-in-depth, Least privilege | | **인증·접근 제어** | 사용자 인증, 역할 기반 접근, 세션 관리 | | **암호화** | 저장 데이터·전송 데이터 암호화, 키 관리 | | **소프트웨어 무결성** | 코드 서명, 부트 무결성 검증, SBOM 관리 | | **네트워크 보안** | 포트 최소화, 방화벽, TLS 버전 요건 | | **취약점 관리** | CVE 모니터링, 패치 주기, CVD 정책 | | **감사·로그** | 보안 이벤트 로깅, 로그 보호, 접근 이력 | | **업데이트·유지보수** | 보안 업데이트 메커니즘, 원격 관리 보안 | ---

### kb-eval-20261027-it01-ra_kr-005

<!-- kb_eval_case {"agent": "ra_kr", "base_date": "2026-10-27", "decision_ref": "kb-eval-20261027-it01-ra_kr-005", "iteration": 1, "matched_keywords": ["MFDS"], "profile_id": "ra-kr", "scenario_id": "c47aed9f54a1f73a", "source": "github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md", "source_hash": "76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b"} -->

- Agent: `ra_kr` / Sam (KR)
- Scenario: `c47aed9f54a1f73a`
- Source: `github:holee9/ra-project/05_전문가교육/Week02_MFDS_체계_상세.md`
- Source link: [Open source document](https://github.com/holee9/ra-project/blob/main/05_%EC%A0%84%EB%AC%B8%EA%B0%80%EA%B5%90%EC%9C%A1/Week02_MFDS_%EC%B2%B4%EA%B3%84_%EC%83%81%EC%84%B8.md)
- Source hash: `76ebe188f3b551d01fd9ef7caae908fae7c5e48f91a4545619856baf9d4bba7b`
- Focus: MFDS classification and licensing route
- Matched keywords: MFDS

**Source Summary**

- 문서 요약: `Week02_MFDS_체계_상세.md`는 `Week02_MFDS_체계_상세.md` source에서 선택된 규제 지식 문서입니다.
- 현재 excerpt 핵심: ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 --- ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|------...
- 이 항목의 평가 포인트: 이 source는 focus와 직접 또는 보조적으로 연결됩니다. 좋은 답변은 source에서 확인되는 사실만 사용하고, 부족한 판단은 추가 확인 필요사항으로 남겨야 합니다.
- 빠른 판단 기준: 답변이 `MFDS classification and licensing route` 관점의 판단을 source 근거와 한계 안에서 제시하면 높게 평가하고, source가 말하지 않는 결론을 단정하면 낮게 평가합니다.

**Evaluation Target**

- 기대 산출물: 이 source를 근거로 `MFDS classification and licensing route`에 대한 간결한 RA 판단을 확인합니다.
- 주요 확인 기준:
  - 한국 classification/licensing route, technical document 필요사항, KGMP 연계, MFDS-specific evidence를 중심으로 확인합니다.
  - MFDS 업무에서는 licensing/classification, KGMP, digital medical product 의무, supplementary-response strategy, 한국 규제 evidence readiness를 해당되는 범위에서 확인합니다.
  - 제시된 source excerpt를 근거로 판단했는지 확인합니다. 일반 규제 지식만으로 답한 경우는 낮게 평가합니다.
  - 필요한 RA 판단, evidence gap, 후속 조치가 명확히 드러나는지 확인합니다.
  - source에서 확인된 사실과 추정/추가 확인 필요 사항을 구분했는지 확인합니다.
  - source만으로 판단이 부족한 경우 human escalation 필요성을 표시했는지 확인합니다.
  - `No hallucination`/`Escalation appropriate`는 Agent Response을 기준으로 판정합니다.

**Agent Response** (실제 생성된 응답 — no_hallucination/escalation_appropriate 판정 대상)

> **Regulatory Draft – Korean MF D S Pathway for a Digital‑Medical Device (SaMD)**  

---

### 1. Target classification & submission route  
| Step | Korean regulatory element | Decision | Rationale |
|------|---------------------------|----------|------------|
| **Device type** | Digital medical device / SaMD (software that performs a medical function without accessory hardware) | **Likely 2등급 or 3등급** – classification depends on risk level defined in the “MFDS 디지털의료기기 가이드라인” (see § AI/ML‑based GUI SW classification). The source does not state the exact grade; therefore the grade must be verified against 「의료기기 품목 및 품목별 등급에 관한 규정」. | ‑ |
| **Submission track** | - 1등급 → 신고<br>- 2등급 → 인증 (technical‑document review by an MFDS‑designated 심사기관)<br>- 3·4등급 → 허가 | **If classified as 2등급 → 인증**; if the risk assessment places it in 3등급, then **허가**. The default for digital medical devices is 인증 unless the device’s intended use/treatment level warrants 허가. | No specific grade identifier found in source – verify separately. |
| **KGMP (GMP) 인정** | KGMP 적합인증 required for manufacturers of 2등급–4등급 devices. | **Apply for GMP 적합인정** before submission; the procedure is detailed in Source [1]. | The GMP process includes document review, on‑site inspection, defect notification (Critical/Major/Minor), corrective‑action submission and issuance of a 3‑year 인증서. |
| **선정 심사기관** | Six designated agencies (KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea). | For digital medical devices **NIDS may also be considered** per the 2025‑01‑24 policy change (Source [2]). | Include NIDS in the shortlist when selecting a 심사기관. |

---

### 2. Required evidence package  

| Evidence type | Korean requirement | Typical source | Gap to fill |
|---------------|-------------------|----------------|-------------|
| **KGMP certification** | Valid KGMP 적합인정서 (3 yr validity) issued by an approved 심사기관. | Manufacturer’s GMP audit report & certificate. | Confirm that the chosen 심사기관 has performed the on‑site inspection and issued a certificate; if not, schedule before submission. |
| **Device description & intended use** | Clear Korean‑language description of function, target patient group, and clinical indication. | Technical file (Korean translation required). | Ensure full Korean IFU/labeling draft is ready for review. |
| **Risk Management File** | Compliance with ISO 14971:2019 (risk analysis, risk control measures, residual risk acceptability). | Risk management plan & report. | Verify linkage to Korean “위험도 평가” requirements; if not yet prepared in Korean, translate and map. |
| **Software documentation** | Conformity to IEC 62304 2006+A1:2015 (software life‑cycle) AND IEC 62366‑1 2015+A1:2020 (usability). | Software design dossier, verification/validation reports. | Confirm that AI/ML components meet the new MFDS 가이드라인 (see 2025‑05‑07 change – Source [2]). |
| **Clinical Evaluation** | For SaMD, local clinical data may be required unless a foreign CER is accepted under MFDS “foreign clinical evaluation report” acceptance policy. | Clinical trial report or CER from an FDA‑cleared/CE‑marked comparator. | Identify whether the device can rely on foreign CER; if not, plan a Korean clinical study. |
| **Labeling & IFU** | All labeling, packaging, and Instructions for Use must be in Korean (Korean language requirement). | Draft Korean label set. | Verify that all safety warnings, symbols, and content meet MFDS Annex II‑3 style; missing translations are a gap. |
| **Post‑Market Surveillance (PMS) plan** | Outline of 시판후조사 activities compliant with MFDS § 시판 후 조사 규정. | PMS SOPs, adverse event reporting process. | Draft needed if not yet prepared. |

---

### 3. Risk controls specific to digital medical devices  

| Control | Korean regulatory context | Implementation note |
|---------|---------------------------|---------------------|
| **Software lifecycle management** (IEC 62304) | Mandatory for SaMD; MFDS aligns with IEC 62304. | Establish version control, change‑impact analysis, and traceability matrices. |
| **Usability engineering** (IEC 62366‑1) | Required to mitigate use‑error risks. | Conduct formative/usability testing with Korean end‑users; document findings in a usability report. |
| **Cybersecurity** (IEC 81001‑5‑1 2021 referenced by MFDS) | Must address data integrity, authentication, and firmware update security. | Include threat analysis, mitigation strategies, and patch management plan. |
| **AI/ML model governance** | New MFDS 가이드라인 6종 (2025‑05‑07) adds specific clinical‑validation and change‑management requirements for AI/ML‑based GUIs. | Provide a “Algorithm Change Management Plan” that defines pre‑market performance verification and post‑marketing monitoring of algorithm drift. |
| **Data protection & privacy** | Korean Personal Information Protection Act (PIPA) applies to patient data processed by SaMD. | Incorporate data encryption, consent management, and anonymization procedures. |

---

### 4. Missing information / open items  

1. **Exact device grade (1~4등급)** – not disclosed in source; must be confirmed against the MFDS digital‑medical‑device classification table.  
2. **Whether foreign clinical evaluation report is acceptable** – requires verification of MFDS’s latest “foreign CER acceptance” notice (no identifier found in source).  
3 **Selected 심사기관** – decision pending; need to assess NIDS eligibility and capacity alongside the traditional six agencies.  
4. **Korean language IFU draft** – ensure complete translation before KGMP inspection.  

---

### 5. Human‑escalation triggers  

| Trigger | Action required | Escalation point |
|---------|-----------------|------------------|
| **Grade not determined** within 3 working days of the draft review. | Pause submission preparation; request classification ruling from MFDS (e.g., via 품목별 등급 문의). | RA lead → Regulatory affairs manager. |
| **KGMP certificate pending** beyond scheduled launch date. | Initiate expedited GMP audit with chosen 심사기관; consider alternate agency if timeline at risk. | Project manager → Senior QA. |
| **Foreign CER acceptance uncertain** after literature review. | Submit a formal inquiry to MFDS (문의) with the foreign study details. | RA lead → Legal/compliance liaison. |
| **AI/ML algorithm change required post‑submission** before final 허가. | Activate Algorithm Change Management Plan; submit supplemental data per “네거티브 방식 변경허가제” (2026 예정 – Source [2]). | Product development lead → Regulatory affairs manager. |
| **Korean labeling incomplete** 48 hours prior to GMP inspection. | Halt further activities until full Korean IFU set is approved. | Marketing & regulatory coordination meeting. |

---

### 6. Citations  

- **KGMP 적합인정 절차** – Source [1] (process flow, list of six 심사기관).  
- **디지털의료제품법 시행 및 NIDS 권한 확대** – 2025‑01‑24 change (Source [2]).  
- **MFDS 디지털의료기기 가이드라인 6종 제·개정 (AI/ML GUI SW)** – 2025‑05‑07 (Source [2]).  
- **예정된 자율 성능 인증제 및 네거티브 방식 변경허가제** – 2026 예정 items (Source [2]).  
- **ISO 14971:2019, ISO 13485:2016, IEC 62304 2006+A1:2015, IEC 62366‑1 2015+A1:2020, IEC 81001‑5‑1 2021** – framework references (no specific source required).  

*No specific MFDS 고시 or article numbers were identified in the provided excerpts; those identifiers must be verified separately.*

---

### 7. Peer‑review prompt  

> **To a fellow RA colleague:**  
> - Are there any additional Korean classification rules or recent MFDS notices (post‑2026‑01) that could affect the grade determination for this SaMD?  
> - Does the source coverage adequately capture all required GMP‑related documents, especially concerning NIDS as a potential 심사기관?  
> - Have we omitted any jurisdiction‑specific obligations (e.g., PIPA privacy provisions, specific post‑market reporting forms) that should be highlighted before finalizing this draft?

--- 

*End of regulatory judgment.*

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

1. Chunk `1078228256164017760`

> ### 5.2 GMP 적합인정 절차 ``` GMP 심사 신청 → 심사기관 배정 → 품질문서 심사 → 제조소 현장조사 → 결함사항 통보(3개 등급: Critical/Major/Minor) → 시정 조치 제출 → 적합인정서 발급 (유효기간 3년, 갱신 필요) ``` **심사기관 6개** (모든 품목군 대상): KTL, KTR, 한국화학융합시험연구원, 한국건설생활환경시험연구원, TÜV SÜD Korea, TÜV Rheinland Korea **디지털의료기기**: NIDS가 2025-01-24부터 GMP 적합판정 업무 수행 ---

2. Chunk `1121184088796802935`

> ## 7. 2025~2026 주요 규제 변경사항 | 일자 | 변경 내용 | 영향 | |------|----------|------| | 2025-01-24 | 디지털의료제품법 시행 | SaMD 분류·허가 체계 변화, NIDS 권한 확대 | | 2025-01-24 | NIDS 디지털의료기기 GMP 적합판정 업무 시작 | 심사기관 선택 시 NIDS 추가 고려 | | 2025-05-07 | MFDS 디지털의료기기 가이드라인 6종 제·개정 | AI/ML 기반 GUI SW 분류·임상 요건 확인 필요 | | 2026 예정 | 자율 성능 인증제 (디지털의료기기) | 선인증 → 후감독 방식 도입 예정 | | 2026 예정 | 네거티브 방식 변경허가제 | 중요 변경만 사전허가, 경미 변경 사후 신고 | ---
